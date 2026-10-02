//! Mermin chemical potential: the root mu of sum_i g_i f((eps_i - mu)/T) = N,
//! f(x) = 1/(1 + e^x), solved with a well-conditioned residual.
//!
//! The defect this module removes.  The direct count sum g f - N (kept below
//! only as `DirectCount`, for diagnostics and negative controls) carries an
//! absolute rounding error of order eps_mach N, because occupations close to 1
//! are rounded to 1.  It therefore fixes mu only to about eps_mach N/(dN/dmu).
//! Deep in the activated regime (gap >> T, dN/dmu ~ e^{-gap/2T}/T) that is
//! ~1e-9 m: the cross-check (reports/ks-crosscheck.json, thermo_state_functions)
//! found 8.27e-10 m for N8_lamm1_a00_T10 (dN/dmu = 1.24e-6).
//!
//! Exact rewriting about a split set S, a prefix of the levels sorted by energy
//! (first the T = 0 filling, finally the levels below the root):
//!
//!   sum g f - N = P - Hl - d,
//!   P  = sum_{i not in S} g_i f(x_i)     thermal particles above the split,
//!   Hl = sum_{i in S} g_i f(-x_i)        thermal holes below it (the factor
//!                                        1 - f(x) = f(-x) is evaluated as f(-x),
//!                                        never as 1 - f),
//!   d  = N - sum_{i in S} g_i            exact (integer-valued sums).
//!
//! With S = {eps < mu} every term is at most 2 g f (1 - f), and
//! dN/dmu = sum g f (1 - f)/T, so the residual is accurate to
//! eps_mach (P + Hl + |d|) <= 4 eps_mach T dN/dmu per term: mu is fixed to
//! O(n eps_mach T) plus the spacing of the doubles at mu.  `Root::bound` states
//! this bound for every solve, `Root::bound_direct` the bound of the direct count.
//!
//! Two exactly equivalent forms with different rounding paths:
//! * `LogBalance` (canonical numerics): Lambda(mu) = ln(P + d-) - ln(Hl + d+),
//!   d+- = max(+-d, 0); every sum is a log-sum-exp of ln g - softplus(+-x), so
//!   nothing underflows and Lambda is nearly linear (slope ~ 2/T when activated).
//!   Safeguarded Newton in a sign bracket, then bisection of a tight bracket down
//!   to adjacent doubles; the endpoint with the smaller |Lambda| is returned.
//! * `LinearDeviation` (refined numerics): R(mu) = (P - Hl) - d in the linear
//!   domain, sums in descending level order, plain bisection.
//! The refined run uses the second form, so |canonical - refined| of mu (and of
//! Omega = F - mu N) contains the rounding error of the root instead of sharing
//! it (the direct count of both runs carried the same rounding).
//!
//! Split passes: the first pass uses the T = 0 filling of the given levels (the
//! longest energy-ordered prefix with sum g <= N); if the root found lies outside
//! the gap of that split, the split is moved to the levels below the root and the
//! root is solved again (at most three passes).

use std::cmp::Ordering;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum MerminForm {
    /// canonical: log balance of the thermal particles and holes about the split, Newton + bisection
    LogBalance,
    /// refined run: linear deviation from the split filling, descending summation, bisection
    LinearDeviation,
    /// the former direct count sum g f - N by bisection (diagnostics and negative controls only)
    DirectCount,
}

impl MerminForm {
    pub fn tag(self) -> &'static str {
        match self {
            MerminForm::LogBalance => "LogBalance",
            MerminForm::LinearDeviation => "LinearDeviation",
            MerminForm::DirectCount => "DirectCount",
        }
    }
}

/// Result of a Mermin root solve.
#[derive(Clone, Copy, Debug)]
pub struct Root {
    pub mu: f64,
    /// dN/dmu = sum g f (1 - f)/T at mu
    pub dn_dmu: f64,
    #[allow(dead_code)]
    /// P + Hl + |d| for the split of the final pass (= {eps < mu} unless three passes did not settle):
    /// the size of the terms of the well-conditioned residual
    pub magnitude: f64,
    /// rounding bound of the well-conditioned forms: (n + 2) eps_mach magnitude/(dN/dmu) + 2 eps_mach |mu|
    pub bound: f64,
    /// rounding bound of the direct count: (n + 2) eps_mach N/(dN/dmu) + 2 eps_mach |mu|
    pub bound_direct: f64,
    /// split passes used (1 if the T = 0 filling already brackets the root)
    pub passes: usize,
    #[allow(dead_code)]
    /// residual evaluations
    pub evals: usize,
}

#[inline]
fn fermi(x: f64) -> f64 {
    if x > 0.0 {
        let e = (-x).exp();
        e / (1.0 + e)
    } else {
        1.0 / (1.0 + x.exp())
    }
}

/// (softplus(x), softplus(-x)) = (ln(1 + e^x), ln(1 + e^-x)), both to relative precision.
#[inline]
fn softplus_pair(x: f64) -> (f64, f64) {
    let l = (-x.abs()).exp().ln_1p();
    if x > 0.0 {
        (x + l, l)
    } else {
        (l, l - x)
    }
}

struct Problem<'a> {
    eps: &'a [f64],
    deg: &'a [f64],
    /// level indices in ascending energy (ties by index)
    order: Vec<usize>,
    n: f64,
    t: f64,
}

impl<'a> Problem<'a> {
    fn x(&self, i: usize, mu: f64) -> f64 {
        (self.eps[i] - mu) / self.t
    }
    /// d = N - sum of g over the first k levels (exact for integer-valued g and N)
    fn deficit(&self, k: usize) -> f64 {
        let gs: f64 = self.order[..k].iter().map(|&i| self.deg[i]).sum();
        self.n - gs
    }
    /// T = 0 filling: the longest prefix with sum g <= N
    fn split_t0(&self) -> usize {
        let mut cum = 0.0;
        let mut k = 0;
        for &i in &self.order {
            if cum + self.deg[i] <= self.n + 1e-9 * self.n.max(1.0) {
                cum += self.deg[i];
                k += 1;
            } else {
                break;
            }
        }
        k
    }
    /// number of levels with eps < mu (a prefix of the order)
    fn split_below(&self, mu: f64) -> usize {
        self.order.iter().take_while(|&&i| self.eps[i] < mu).count()
    }

    /// Lambda(mu) = ln(P + d-) - ln(Hl + d+) and dLambda/dmu (> 0).
    fn log_balance(&self, k: usize, d: f64, mu: f64, buf: &mut Vec<(f64, f64)>) -> (f64, f64) {
        // per level: (ln of its term, ln of its derivative weight g f (1 - f)); the first k are holes
        buf.clear();
        let (mut mp, mut mh) = (f64::NEG_INFINITY, f64::NEG_INFINITY);
        for (pos, &i) in self.order.iter().enumerate() {
            let (spx, spm) = softplus_pair(self.x(i, mu));
            let lg = self.deg[i].ln();
            let term = if pos < k { lg - spm } else { lg - spx };
            buf.push((term, lg - spx - spm));
            if pos < k {
                mh = mh.max(term);
            } else {
                mp = mp.max(term);
            }
        }
        let dm = (-d).max(0.0);
        let dp = d.max(0.0);
        if dm > 0.0 {
            mp = mp.max(dm.ln());
        }
        if dp > 0.0 {
            mh = mh.max(dp.ln());
        }
        let (mut sp, mut sdp, mut sh, mut sdh) = (0.0, 0.0, 0.0, 0.0);
        for (pos, &(term, w)) in buf.iter().enumerate() {
            if pos < k {
                sh += (term - mh).exp();
                sdh += (w - mh).exp();
            } else {
                sp += (term - mp).exp();
                sdp += (w - mp).exp();
            }
        }
        if dm > 0.0 {
            sp += (dm.ln() - mp).exp();
        }
        if dp > 0.0 {
            sh += (dp.ln() - mh).exp();
        }
        let lam = (mp + sp.ln()) - (mh + sh.ln());
        let dlam = (sdp / sp + sdh / sh) / self.t;
        (lam, dlam)
    }

    /// R(mu) = (P - Hl) - d, sums in descending level order.
    fn linear_deviation(&self, k: usize, d: f64, mu: f64) -> f64 {
        let (mut ps, mut hs) = (0.0, 0.0);
        for pos in (0..self.order.len()).rev() {
            let i = self.order[pos];
            let x = self.x(i, mu);
            if pos < k {
                hs += self.deg[i] * fermi(-x);
            } else {
                ps += self.deg[i] * fermi(x);
            }
        }
        (ps - hs) - d
    }

    fn direct_count(&self, mu: f64) -> f64 {
        self.eps.iter().zip(self.deg).map(|(&e, &g)| g * fermi((e - mu) / self.t)).sum::<f64>()
    }

    fn bracket(&self) -> (f64, f64) {
        let emin = self.eps.iter().fold(f64::INFINITY, |m, &e| m.min(e));
        let emax = self.eps.iter().fold(f64::NEG_INFINITY, |m, &e| m.max(e));
        (emin - 60.0 * self.t - 1.0, emax + 60.0 * self.t + 1.0)
    }

    /// LogBalance root with split k: safeguarded Newton, then bisection to adjacent doubles.
    fn solve_log(&self, k: usize, guess: f64, evals: &mut usize) -> f64 {
        let d = self.deficit(k);
        let (mut lo, mut hi) = self.bracket();
        let mut buf = Vec::with_capacity(self.order.len());
        let mut mu = if guess > lo && guess < hi { guess } else { 0.5 * (lo + hi) };
        let mut converged = false;
        for _ in 0..200 {
            let (l, dl) = self.log_balance(k, d, mu, &mut buf);
            *evals += 1;
            if l == 0.0 {
                return mu;
            }
            if l < 0.0 {
                lo = mu;
            } else {
                hi = mu;
            }
            let step = -l / dl;
            let mut next = mu + step;
            if !next.is_finite() || next <= lo || next >= hi {
                next = 0.5 * (lo + hi);
            }
            if next == mu || (next - mu).abs() <= 4.0 * f64::EPSILON * mu.abs().max(self.t) {
                mu = next;
                converged = true;
                break;
            }
            mu = next;
        }
        if !converged {
            mu = 0.5 * (lo + hi);
        }
        // tight sign bracket around mu (expanding), then bisection to adjacent doubles
        let mut w = 8.0 * f64::EPSILON * mu.abs().max(self.t);
        let (mut a, mut b, mut la, mut lb);
        loop {
            a = (mu - w).max(lo);
            b = (mu + w).min(hi);
            la = self.log_balance(k, d, a, &mut buf).0;
            lb = self.log_balance(k, d, b, &mut buf).0;
            *evals += 2;
            if la == 0.0 {
                return a;
            }
            if lb == 0.0 {
                return b;
            }
            if la < 0.0 && lb > 0.0 {
                break;
            }
            if a == lo && b == hi {
                // cannot happen for a monotone Lambda; fall back to the plain bracket
                break;
            }
            w *= 16.0;
        }
        loop {
            let mid = 0.5 * (a + b);
            if mid <= a || mid >= b {
                break;
            }
            let l = self.log_balance(k, d, mid, &mut buf).0;
            *evals += 1;
            if l == 0.0 {
                return mid;
            }
            if l < 0.0 {
                a = mid;
                la = l;
            } else {
                b = mid;
                lb = l;
            }
        }
        if la.abs() <= lb.abs() {
            a
        } else {
            b
        }
    }

    /// LinearDeviation root with split k: bisection.
    fn solve_linear(&self, k: usize, evals: &mut usize) -> f64 {
        let d = self.deficit(k);
        let (mut lo, mut hi) = self.bracket();
        for _ in 0..400 {
            let mid = 0.5 * (lo + hi);
            if mid <= lo || mid >= hi {
                break;
            }
            *evals += 1;
            if self.linear_deviation(k, d, mid) < 0.0 {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        0.5 * (lo + hi)
    }

    /// The former direct count (bisection on sum g f < N), unchanged.
    fn solve_direct(&self, evals: &mut usize) -> f64 {
        let (mut lo, mut hi) = self.bracket();
        for _ in 0..400 {
            let mid = 0.5 * (lo + hi);
            if mid <= lo || mid >= hi {
                break;
            }
            *evals += 1;
            if self.direct_count(mid) < self.n {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        0.5 * (lo + hi)
    }

    /// dN/dmu, P + Hl + |d| (split k: the first k levels) and the two rounding bounds at mu.
    fn bounds(&self, mu: f64, k: usize) -> (f64, f64, f64, f64) {
        let d = self.deficit(k);
        let (mut dn, mut ps, mut hs) = (0.0, 0.0, 0.0);
        for (pos, &i) in self.order.iter().enumerate() {
            let x = self.x(i, mu);
            let (spx, spm) = softplus_pair(x);
            dn += self.deg[i] * (-spx - spm).exp();
            if pos < k {
                hs += self.deg[i] * fermi(-x);
            } else {
                ps += self.deg[i] * fermi(x);
            }
        }
        let dn = dn / self.t;
        let mag = ps + hs + d.abs();
        let m = self.order.len() as f64 + 2.0;
        let ulp = 2.0 * f64::EPSILON * mu.abs();
        let (b, bd) = if dn > 0.0 { (m * f64::EPSILON * mag / dn + ulp, m * f64::EPSILON * self.n / dn + ulp) } else { (f64::INFINITY, f64::INFINITY) };
        (dn, mag, b, bd)
    }
}

/// Solve sum_i g_i f((eps_i - mu)/T) = N for mu.
pub fn solve(eps: &[f64], deg: &[f64], n: f64, t: f64, form: MerminForm) -> Result<Root, String> {
    if eps.len() != deg.len() {
        return Err("mermin: levels and degeneracies differ in length".into());
    }
    if !(t > 0.0) {
        return Err(format!("mermin: temperature {} not positive", t));
    }
    let total: f64 = deg.iter().sum();
    if total <= n {
        return Err(format!("thermal window holds {} states for N = {}", total, n));
    }
    let mut order: Vec<usize> = (0..eps.len()).collect();
    order.sort_by(|&a, &b| eps[a].partial_cmp(&eps[b]).unwrap_or(Ordering::Equal).then(a.cmp(&b)));
    let p = Problem { eps, deg, order, n, t };
    let mut evals = 0;
    let mut passes = 0;
    let mut k_used = 0;
    let mu = match form {
        MerminForm::DirectCount => {
            passes = 1;
            let mu = p.solve_direct(&mut evals);
            k_used = p.split_below(mu);
            mu
        }
        _ => {
            let mut k = p.split_t0();
            // first guess: the middle of the gap of the T = 0 filling
            let guess = match (k.checked_sub(1).map(|j| eps[p.order[j]]), p.order.get(k).map(|&i| eps[i])) {
                (Some(a), Some(b)) => 0.5 * (a + b),
                (Some(a), None) => a,
                (None, Some(b)) => b,
                (None, None) => 0.0,
            };
            let mut mu = guess;
            for pass in 1..=3 {
                passes = pass;
                mu = match form {
                    MerminForm::LogBalance => p.solve_log(k, mu, &mut evals),
                    _ => p.solve_linear(k, &mut evals),
                };
                k_used = k;
                let k1 = p.split_below(mu);
                if k1 == k {
                    break;
                }
                k = k1;
            }
            mu
        }
    };
    let (dn_dmu, magnitude, bound, bound_direct) = p.bounds(mu, k_used);
    Ok(Root { mu, dn_dmu, magnitude, bound, bound_direct, passes, evals })
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::json::parse;

    fn all_forms(eps: &[f64], deg: &[f64], n: f64, t: f64) -> (Root, Root, Root) {
        (
            solve(eps, deg, n, t, MerminForm::LogBalance).unwrap(),
            solve(eps, deg, n, t, MerminForm::LinearDeviation).unwrap(),
            solve(eps, deg, n, t, MerminForm::DirectCount).unwrap(),
        )
    }

    /// Two levels, 0 (g = 8, the k = 0 zero modes) and D (g = 24), N = 8: the root is
    /// mu = D - T ln(sqrt(1 + 3 e^{D/T}) + 1) in closed form (no cancellation).
    #[test]
    fn two_level_closed_form() {
        for &(gap, t) in &[(0.43f64, 0.01f64), (0.43, 0.02), (0.17, 0.01), (0.064, 0.05), (0.3, 0.004)] {
            let exact = gap - t * ((1.0 + 3.0 * (gap / t).exp()).sqrt() + 1.0).ln();
            let (a, b, _) = all_forms(&[0.0, gap], &[8.0, 24.0], 8.0, t);
            for r in [a, b] {
                assert!((r.mu - exact).abs() <= r.bound + 4.0 * f64::EPSILON * exact.abs(), "gap {} T {}: mu {} exact {} bound {}", gap, t, r.mu, exact, r.bound);
                assert!(r.bound < 1e-14, "bound {}", r.bound);
            }
        }
    }

    /// Deep activation (gap/T = 1000): the thermal terms underflow in the linear domain,
    /// the log balance still finds the symmetric root mu = gap/2.
    #[test]
    fn log_balance_survives_underflow() {
        let r = solve(&[0.0, 10.0], &[8.0, 8.0], 8.0, 0.01, MerminForm::LogBalance).unwrap();
        assert!((r.mu - 5.0).abs() <= 8.0 * f64::EPSILON * 5.0, "mu {}", r.mu);
    }

    /// An open T = 0 shell (N inside a degenerate group) and a split that must be re-pivoted.
    #[test]
    fn open_shell_and_repivot() {
        let eps = [0.0, 0.0, 0.1, 0.1, 0.1, 0.35];
        let deg = [4.0, 4.0, 12.0, 12.0, 12.0, 24.0];
        for &n in &[8.0, 20.0, 26.0, 44.0] {
            for &t in &[0.005, 0.02, 0.2] {
                let (a, b, d) = all_forms(&eps, &deg, n, t);
                let tol = a.bound.max(b.bound);
                assert!((a.mu - b.mu).abs() <= tol, "N {} T {}: {} vs {} (bound {})", n, t, a.mu, b.mu, tol);
                assert!((d.mu - a.mu).abs() <= d.bound_direct, "direct {} vs {} (bound {})", d.mu, a.mu, d.bound_direct);
                let count: f64 = eps.iter().zip(&deg).map(|(&e, &g)| g * fermi((e - a.mu) / t)).sum();
                assert!((count - n).abs() <= 1e-12 * n);
            }
        }
    }

    /// The 40-digit mpmath roots of tools/mermin_roots_mp.py on the exact final levels of the
    /// thermal states with the largest conditioning bound of the direct count.
    #[test]
    fn forty_digit_roots() {
        let fx = parse(include_str!("../tools/mermin-roots-40digit.json")).unwrap();
        let states = fx.get("fixture").and_then(|x| x.as_arr()).unwrap();
        assert!(states.len() >= 4);
        let mut worst_direct: f64 = 0.0;
        let mut worst_bound_new: f64 = 0.0;
        for s in states {
            let num = |k: &str| s.get(k).and_then(|x| x.as_str()).unwrap().parse::<f64>().unwrap();
            let n = num("N");
            let t = num("T");
            let root = num("root40");
            let mu_run = num("muRun");
            let lv = s.get("levels").and_then(|x| x.as_arr()).unwrap();
            let eps: Vec<f64> = lv.iter().map(|l| l.as_arr().unwrap()[0].as_str().unwrap().parse().unwrap()).collect();
            let deg: Vec<f64> = lv.iter().map(|l| l.as_arr().unwrap()[1].as_str().unwrap().parse().unwrap()).collect();
            let (a, b, d) = all_forms(&eps, &deg, n, t);
            let id = s.get("id").and_then(|x| x.as_str()).unwrap();
            assert_eq!(a.mu.to_bits(), mu_run.to_bits(), "{}: the canonical form must reproduce the run's mu", id);
            assert!((a.mu - root).abs() <= a.bound, "{}: LogBalance {} vs root {} (bound {})", id, a.mu, root, a.bound);
            assert!((b.mu - root).abs() <= b.bound, "{}: LinearDeviation {} vs root {} (bound {})", id, b.mu, root, b.bound);
            assert!((d.mu - root).abs() <= d.bound_direct, "{}: direct count outside its own bound", id);
            worst_direct = worst_direct.max((d.mu - root).abs());
            worst_bound_new = worst_bound_new.max(a.bound.max(b.bound));
        }
        // negative control: the former direct count misses the root by far more than the new bound
        assert!(worst_direct > 1e3 * worst_bound_new, "direct count {:e} vs new bound {:e}", worst_direct, worst_bound_new);
    }
}
