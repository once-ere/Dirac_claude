//! Kohn-Sham self-consistency (SPEC section 7, ks-theory.json).
//!
//! Levels: for every lattice shell n2 (|k| = dk sqrt(n2), degeneracy
//! g = 4 r3(n2) per level of each block type j = +-1), every block type j and
//! brane parity, the levels are labelled by the Pruefer index l (shoot.rs).
//! Particles (fillingConvention of ks-theory.json, a CONVENTION): the positive
//! branch = the labels whose lambda = 0 level at the same slice is positive,
//! plus the k = 0 brane zero modes (even parity, l = 0, both j); a label keeps
//! its branch when the interaction is switched on (the label is the continuous
//! continuation).  Since the levels of a sector increase with l, the particle
//! labels of a sector are exactly l >= l_min(sector).  The negative branch is
//! the normal-ordered sea and contributes nothing to N, n, S or T.
//!
//! Densities (proper, per proper 7-volume), w = w_Z2 = 1/2, P = e^{-6Hy}/Vol_7:
//!   n = sum w g f P (a^2+b^2), S = sum w g f P j 2ab, Q = sum w g f P (a^2-b^2),
//!   t_o = P j (a^2 - b^2).
//! Potentials: M_eff = m + (15/16) lambda S, v_v = -(1/16) lambda n
//! [+ w_Q = lambda Q / 16 in the exact-Fock variant];
//! e_int = lambda [(15/32) S^2 - (1/32) n^2] [+ lambda Q^2 / 32].
//! N = sum g f over both parities = particle number of the doubled
//! (universe + Z2 image) system; the patch holds N/2.
//! E_KS = sum g f eps - 2 Vol_7 int e^{6Hy} e_int dy (doubled system).

pub use crate::mermin::MerminForm;
use crate::model::*;
use crate::shoot::*;
use std::collections::BTreeMap;

pub type Key = (u32, i32, Parity, i64);

pub const SECTORS: [(i32, Parity); 4] = [(1, Parity::Even), (1, Parity::Odd), (-1, Parity::Even), (-1, Parity::Odd)];

#[derive(Clone, Debug)]
pub struct SectorSpec {
    pub shell: Shell,
    pub j: i32,
    pub parity: Parity,
    pub ell_min: i64,
    pub nlev: usize,
}

#[derive(Clone, Debug)]
pub struct Level {
    pub key: Key,
    pub k: f64,
    pub eps: f64,
    pub deg: f64,
    pub prof: Vec<f64>,
}

#[derive(Clone, Debug)]
pub enum Occ {
    Aufbau,
    Fixed(BTreeMap<Key, f64>),
    Mermin,
}

#[derive(Clone, Debug)]
pub struct Dens {
    pub n: Vec<f64>,
    pub s: Vec<f64>,
    pub q: Vec<f64>,
    /// sum w g f kappa |k| t_o  (= 3 x the kinetic part of p3)
    pub tk: Vec<f64>,
    /// sum w g f eps n_o
    pub k4: Vec<f64>,
    /// sum w g f [(eps - v) n_o - M s_o - kappa |k| t_o - w_Q q_o]
    pub ky: Vec<f64>,
    /// sum w g f [|eps - v| n_o + |M s_o| + |kappa k t_o| + |w_Q q_o|] (scale of the cancelling terms of p8)
    pub kyabs: Vec<f64>,
}

impl Dens {
    fn zeros(nf: usize) -> Dens {
        Dens { n: vec![0.0; nf], s: vec![0.0; nf], q: vec![0.0; nf], tk: vec![0.0; nf], k4: vec![0.0; nf], ky: vec![0.0; nf], kyabs: vec![0.0; nf] }
    }
}

#[derive(Clone, Copy, Debug)]
pub struct Coeffs {
    pub meff: f64,
    pub vv: f64,
}

#[derive(Clone, Debug)]
pub struct State {
    pub phys: Physics,
    pub specs: Vec<SectorSpec>,
    pub levels: Vec<Level>,
    pub occ: Vec<f64>,
    pub pots: Pots,
    pub dens: Dens,
    pub mu: f64,
    pub e_band: f64,
    pub e_int: f64,
    pub e_ks: f64,
    pub e_var: f64,
    pub entropy: f64,
    pub omega_direct: f64,
    pub iters: usize,
    pub resid: f64,
    pub history: Vec<(usize, f64, f64)>,
    pub open_shell: bool,
    pub evals: usize,
    pub path: String,
    pub max_brane_residual: f64,
}

pub fn ctx_for<'a>(grid: &'a Grid, phys: &Physics, pots: &'a Pots) -> Ctx<'a> {
    Ctx { grid, kap0: (-phys.a4).exp(), pots, tip_angle: 0.5 * phys.tip_theta }
}

pub fn kmag(phys: &Physics, sh: Shell) -> f64 {
    phys.dk * (sh.n2 as f64).sqrt()
}

/// Lowest particle label of a sector from the lambda = 0 problem at the same slice.
pub fn ell_min(grid: &Grid, phys: &Physics, sh: Shell, j: i32, parity: Parity) -> Result<i64, String> {
    let free = Pots::free(grid.nf, phys.m);
    let ctx = ctx_for(grid, phys, &free);
    let sec = Sector { k: kmag(phys, sh), j, parity };
    let phi0 = shoot(&ctx, sec, 0.0, None).phi;
    let pi = std::f64::consts::PI;
    if sh.n2 == 0 {
        // a k = 0 level at eps = 0 exactly is a brane zero mode: particle by the convention of ks-theory.json
        let off = match parity {
            Parity::Even => 0.0,
            Parity::Odd => 0.5 * pi,
        };
        let ln = ((phi0 - off) / pi).round() as i64;
        if (phi0 - target(parity, ln)).abs() < 1e-12 {
            return Ok(ln);
        }
    }
    let l = match parity {
        Parity::Even => (phi0 / pi).floor() as i64 + 1,
        Parity::Odd => ((phi0 - 0.5 * pi) / pi).floor() as i64 + 1,
    };
    let d = (phi0 - target(parity, l)).abs().min((phi0 - target(parity, l - 1)).abs());
    if d < 1e-8 {
        return Err(format!("zero-energy level away from k = 0 (n2 {}, j {}, {:?})", sh.n2, j, parity));
    }
    Ok(l)
}

/// Solve every level of the label set in the given potentials.
pub fn solve_levels(grid: &Grid, phys: &Physics, specs: &[SectorSpec], pots: &Pots, guesses: &BTreeMap<Key, f64>, tol: f64) -> Result<(Vec<Level>, usize), String> {
    let ctx = ctx_for(grid, phys, pots);
    let mut out = Vec::new();
    let mut evals = 0;
    for sp in specs {
        let sec = Sector { k: kmag(phys, sp.shell), j: sp.j, parity: sp.parity };
        let mut prev: Option<f64> = None;
        for i in 0..sp.nlev {
            let l = sp.ell_min + i as i64;
            let key = (sp.shell.n2, sp.j, sp.parity, l);
            let t = target(sp.parity, l);
            let guess = match guesses.get(&key) {
                Some(&g) => g,
                None => prev.map(|p| p + 0.5).unwrap_or(0.0),
            };
            let (eps, ne) = find_level(&ctx, sec, t, guess, prev, tol).map_err(|e| format!("level {:?}: {}", key, e))?;
            evals += ne;
            let prof = profile(&ctx, sec, eps);
            out.push(Level { key, k: sec.k, eps, deg: 4.0 * sp.shell.r3 as f64, prof });
            prev = Some(eps);
        }
    }
    Ok((out, evals))
}

/// T = 0 aufbau with exact degeneracy groups (|d eps| <= deg_tol); an open
/// last group is filled as a uniform ensemble (flagged).
pub fn aufbau(levels: &[Level], n: f64, deg_tol: f64) -> Result<(Vec<f64>, bool, f64), String> {
    let mut idx: Vec<usize> = (0..levels.len()).collect();
    idx.sort_by(|&a, &b| levels[a].eps.partial_cmp(&levels[b].eps).unwrap().then(levels[a].key.cmp(&levels[b].key)));
    let mut occ = vec![0.0; levels.len()];
    let mut left = n;
    let mut i = 0;
    let mut open = false;
    let mut efermi = f64::NAN;
    while i < idx.len() && left > 0.0 {
        let e0 = levels[idx[i]].eps;
        let mut jend = i;
        let mut gsum = 0.0;
        while jend < idx.len() && levels[idx[jend]].eps - e0 <= deg_tol {
            gsum += levels[idx[jend]].deg;
            jend += 1;
        }
        let f = if gsum <= left + 1e-9 { 1.0 } else { left / gsum };
        if f < 1.0 {
            open = true;
        }
        for &k in &idx[i..jend] {
            occ[k] = f;
        }
        left -= f * gsum;
        if left.abs() < 1e-9 {
            left = 0.0;
        }
        efermi = levels[idx[jend - 1]].eps;
        i = jend;
    }
    if left > 0.0 {
        return Err(format!("not enough particle levels for N = {} (missing {})", n, left));
    }
    Ok((occ, open, efermi))
}

#[inline]
pub fn fermi(x: f64) -> f64 {
    if x > 0.0 {
        let e = (-x).exp();
        e / (1.0 + e)
    } else {
        1.0 / (1.0 + x.exp())
    }
}

/// Mermin occupations: mu from sum g f = N with the well-conditioned residual of
/// mermin.rs (form `form`: LogBalance in the canonical numerics, LinearDeviation
/// in the refined run).  The former direct bisection on sum g f - N fixed mu only
/// to eps_mach N/(dN/dmu) (~1e-9 m in deeply activated states).
pub fn mermin(levels: &[Level], n: f64, temp: f64, form: MerminForm) -> Result<(Vec<f64>, f64), String> {
    let eps: Vec<f64> = levels.iter().map(|l| l.eps).collect();
    let deg: Vec<f64> = levels.iter().map(|l| l.deg).collect();
    let r = crate::mermin::solve(&eps, &deg, n, temp, form)?;
    Ok((levels.iter().map(|l| fermi((l.eps - r.mu) / temp)).collect(), r.mu))
}

pub fn densities(grid: &Grid, phys: &Physics, levels: &[Level], occ: &[f64], pots: &Pots) -> Dens {
    let nf = grid.nf;
    let mut d = Dens::zeros(nf);
    let vol7 = phys.vol7();
    let kap0 = (-phys.a4).exp();
    for (lv, &f) in levels.iter().zip(occ) {
        if f == 0.0 {
            continue;
        }
        let wgf = 0.5 * lv.deg * f;
        let j = lv.key.1 as f64;
        for p in 0..nf {
            let a = lv.prof[2 * p];
            let b = lv.prof[2 * p + 1];
            let c = wgf / (grid.e6[p] * vol7);
            let nn = a * a + b * b;
            let qq = a * a - b * b;
            let ss = j * 2.0 * a * b;
            let tt = j * qq;
            let kk = kap0 * grid.ew[p] * lv.k;
            d.n[p] += c * nn;
            d.s[p] += c * ss;
            d.q[p] += c * qq;
            d.tk[p] += c * kk * tt;
            d.k4[p] += c * lv.eps * nn;
            d.ky[p] += c * ((lv.eps - pots.v[p]) * nn - pots.mass[p] * ss - kk * tt - pots.wq[p] * qq);
            d.kyabs[p] += c * ((lv.eps - pots.v[p]).abs() * nn + (pots.mass[p] * ss).abs() + (kk * tt).abs() + (pots.wq[p] * qq).abs());
        }
    }
    d
}

/// e_int on the fine grid.
pub fn e_int(phys: &Physics, co: Coeffs, d: &Dens) -> Vec<f64> {
    let lam = phys.lambda;
    (0..d.n.len())
        .map(|p| {
            let mut e = lam * (0.5 * co.meff * d.s[p] * d.s[p] + 0.5 * co.vv * d.n[p] * d.n[p]);
            if phys.functional == Functional::Exx {
                e += phys.exx_frac * lam * d.q[p] * d.q[p] / 32.0;
            }
            e
        })
        .collect()
}

fn pots_vec(p: &Pots, m: f64) -> Vec<f64> {
    let mut x = Vec::with_capacity(3 * p.v.len());
    x.extend(p.mass.iter().map(|&x| x - m));
    x.extend_from_slice(&p.v);
    x.extend_from_slice(&p.wq);
    x
}

fn vec_pots(x: &[f64], m: f64) -> Pots {
    let nf = x.len() / 3;
    Pots { mass: x[..nf].iter().map(|&d| m + d).collect(), v: x[nf..2 * nf].to_vec(), wq: x[2 * nf..].to_vec() }
}

fn out_vec(phys: &Physics, co: Coeffs, d: &Dens) -> Vec<f64> {
    let lam = phys.lambda;
    let mut x = Vec::with_capacity(3 * d.n.len());
    x.extend(d.s.iter().map(|&s| lam * co.meff * s));
    x.extend(d.n.iter().map(|&n| lam * co.vv * n));
    if phys.functional == Functional::Exx {
        x.extend(d.q.iter().map(|&q| phys.exx_frac * lam * q / 16.0));
    } else {
        x.extend(std::iter::repeat(0.0).take(d.n.len()));
    }
    x
}

struct Anderson {
    depth: usize,
    beta: f64,
    xs: Vec<Vec<f64>>,
    rs: Vec<Vec<f64>>,
    best: f64,
}

fn solve_dense(mut a: Vec<Vec<f64>>, mut b: Vec<f64>) -> Option<Vec<f64>> {
    let n = b.len();
    for c in 0..n {
        let mut piv = c;
        for r in c + 1..n {
            if a[r][c].abs() > a[piv][c].abs() {
                piv = r;
            }
        }
        if a[piv][c].abs() < 1e-300 {
            return None;
        }
        a.swap(c, piv);
        b.swap(c, piv);
        for r in c + 1..n {
            let f = a[r][c] / a[c][c];
            if f != 0.0 {
                for k in c..n {
                    a[r][k] -= f * a[c][k];
                }
                b[r] -= f * b[c];
            }
        }
    }
    let mut x = vec![0.0; n];
    for c in (0..n).rev() {
        let mut s = b[c];
        for k in c + 1..n {
            s -= a[c][k] * x[k];
        }
        x[c] = s / a[c][c];
    }
    if x.iter().all(|v| v.is_finite()) {
        Some(x)
    } else {
        None
    }
}

impl Anderson {
    fn next(&mut self, x: &[f64], r: &[f64]) -> Vec<f64> {
        let rn = r.iter().fold(0.0f64, |m, v| m.max(v.abs()));
        if rn > 10.0 * self.best && !self.xs.is_empty() {
            self.xs.clear();
            self.rs.clear();
        }
        self.best = self.best.min(rn);
        self.xs.push(x.to_vec());
        self.rs.push(r.to_vec());
        if self.xs.len() > self.depth {
            self.xs.remove(0);
            self.rs.remove(0);
        }
        loop {
            let m = self.xs.len();
            let c = if m == 1 {
                Some(vec![1.0])
            } else {
                let mut a = vec![vec![0.0; m + 1]; m + 1];
                let mut dmax = 0.0f64;
                for i in 0..m {
                    for k in 0..m {
                        let mut s = 0.0;
                        for (u, v) in self.rs[i].iter().zip(&self.rs[k]) {
                            s += u * v;
                        }
                        a[i][k] = s;
                    }
                    dmax = dmax.max(a[i][i]);
                }
                for (i, row) in a.iter_mut().enumerate().take(m) {
                    row[i] += 1e-12 * dmax;
                    row[m] = 1.0;
                }
                for k in 0..m {
                    a[m][k] = 1.0;
                }
                let mut b = vec![0.0; m + 1];
                b[m] = 1.0;
                solve_dense(a, b).map(|v| v[..m].to_vec())
            };
            match c {
                Some(c) => {
                    let n = x.len();
                    let mut out = vec![0.0; n];
                    for (i, ci) in c.iter().enumerate() {
                        for p in 0..n {
                            out[p] += ci * (self.xs[i][p] + self.beta * self.rs[i][p]);
                        }
                    }
                    return out;
                }
                None => {
                    self.xs.remove(0);
                    self.rs.remove(0);
                }
            }
        }
    }
}

pub struct RunInput<'a> {
    pub phys: Physics,
    pub num: &'a Numerics,
    pub co: Coeffs,
    pub specs: Vec<SectorSpec>,
    pub occ: Occ,
    pub start: Option<Pots>,
    pub guesses: BTreeMap<Key, f64>,
}

pub fn run_scf(grid: &Grid, inp: &RunInput) -> Result<State, String> {
    let phys = &inp.phys;
    let num = inp.num;
    let nf = grid.nf;
    let mut x = match &inp.start {
        Some(p) => pots_vec(p, phys.m),
        None => vec![0.0; 3 * nf],
    };
    if phys.lambda == 0.0 {
        x = vec![0.0; 3 * nf];
    }
    let mut guesses = inp.guesses.clone();
    let mut and = Anderson { depth: num.anderson_depth, beta: num.anderson_beta, xs: vec![], rs: vec![], best: f64::INFINITY };
    let mut history = Vec::new();
    let mut evals = 0;
    let mut last_good: Option<Vec<f64>> = None;
    let mut backtracks = 0usize;
    let mut best_res = f64::INFINITY;
    for it in 1..=num.scf_max_iter {
        let pots = vec_pots(&x, phys.m);
        let xmax = x.iter().fold(0.0f64, |m, v| m.max(v.abs()));
        let solved = if xmax > 50.0 * phys.m.abs() { Err(format!("potentials left the physical range (max {:.3e} m)", xmax)) } else { solve_levels(grid, phys, &inp.specs, &pots, &guesses, num.root_tol) };
        let (levels, ne) = match solved {
            Ok(v) => v,
            Err(e) => {
                // backtrack towards the last iterate whose levels were solved, reset the mixing history
                if let Some(g) = &last_good {
                    if backtracks < 12 {
                        backtracks += 1;
                        x = x.iter().zip(g).map(|(a, b)| 0.5 * (a + b)).collect();
                        and.xs.clear();
                        and.rs.clear();
                        and.best = f64::INFINITY;
                        continue;
                    }
                }
                return Err(format!("iteration {}: {}", it, e));
            }
        };
        last_good = Some(x.clone());
        evals += ne;
        for l in &levels {
            guesses.insert(l.key, l.eps);
        }
        let (occ, open, mu) = match &inp.occ {
            Occ::Aufbau => {
                let (o, open, ef) = aufbau(&levels, phys.n, num.deg_tol)?;
                (o, open, ef)
            }
            Occ::Fixed(map) => {
                let o: Vec<f64> = levels.iter().map(|l| *map.get(&l.key).unwrap_or(&0.0)).collect();
                let tot: f64 = levels.iter().zip(&o).map(|(l, f)| l.deg * f).sum();
                if (tot - phys.n).abs() > 1e-9 {
                    return Err(format!("fixed occupations hold {} particles, N = {}", tot, phys.n));
                }
                let missing: f64 = map.iter().filter(|(k, _)| !levels.iter().any(|l| &l.key == *k)).map(|(_, f)| *f).sum();
                if missing > 0.0 {
                    return Err("fixed occupation of a label outside the label set".into());
                }
                (o, false, f64::NAN)
            }
            Occ::Mermin => {
                let (o, mu) = mermin(&levels, phys.n, phys.temp, num.mermin_form)?;
                (o, false, mu)
            }
        };
        let dens = densities(grid, phys, &levels, &occ, &pots);
        let xo = out_vec(phys, inp.co, &dens);
        let r: Vec<f64> = xo.iter().zip(&x).map(|(a, b)| a - b).collect();
        let res = r.iter().fold(0.0f64, |m, v| m.max(v.abs()));
        let ei = e_int(phys, inp.co, &dens);
        let w6: Vec<f64> = (0..nf).map(|p| grid.e6[p] * ei[p]).collect();
        let vol2 = 2.0 * phys.vol7();
        let e_int_tot = vol2 * grid.integrate(&w6);
        let e_band: f64 = levels.iter().zip(&occ).map(|(l, f)| l.deg * f * l.eps).sum();
        let pe: Vec<f64> = (0..nf).map(|p| grid.e6[p] * ((pots.mass[p] - phys.m) * dens.s[p] + pots.v[p] * dens.n[p] + pots.wq[p] * dens.q[p])).collect();
        let e_var = e_band - vol2 * grid.integrate(&pe) + e_int_tot;
        let e_ks = e_band - e_int_tot;
        history.push((it, res, e_ks));
        if std::env::var("KS_DEBUG").is_ok() {
            let xm = x.iter().fold(0.0f64, |m, v| m.max(v.abs()));
            eprintln!("  scf it {} res {:.3e} max|x| {:.3e} E {:.12e} lam {} a4 {} T {}", it, res, xm, e_ks, phys.lambda, phys.a4, phys.temp);
        }
        if res <= num.scf_tol || phys.lambda == 0.0 {
            let mut entropy = 0.0;
            let mut omega = f64::NAN;
            if let Occ::Mermin = inp.occ {
                let t = phys.temp;
                let mut lg = 0.0;
                for (l, _) in levels.iter().zip(&occ) {
                    let xx = (l.eps - mu) / t;
                    // -[f ln f + (1-f) ln(1-f)] = ln(1+e^{-|x|}) + |x| / (1 + e^{|x|})
                    let ax = xx.abs();
                    entropy += l.deg * ((-ax).exp().ln_1p() + ax * fermi(ax));
                    // ln(1 + e^{-x})
                    lg += l.deg * if xx > 0.0 { (-xx).exp().ln_1p() } else { -xx + xx.exp().ln_1p() };
                }
                omega = -t * lg - e_int_tot;
            }
            let mbr = levels.iter().map(|l| brane_residual(&l.prof, nf, l.key.2)).fold(0.0f64, f64::max);
            return Ok(State {
                phys: phys.clone(),
                specs: inp.specs.clone(),
                levels,
                occ,
                pots,
                dens,
                mu,
                e_band,
                e_int: e_int_tot,
                e_ks,
                e_var,
                entropy,
                omega_direct: omega,
                iters: it,
                resid: res,
                history,
                open_shell: open,
                evals,
                path: String::new(),
                max_brane_residual: mbr,
            });
        }
        best_res = best_res.min(res);
        if it > 60 && res > 1e3 * best_res {
            return Err(format!("SCF diverging at iteration {} (residual {:e}, best {:e})", it, res, best_res));
        }
        x = and.next(&x, &r);
    }
    Err(format!("SCF not converged in {} iterations (last residual {:e})", num.scf_max_iter, history.last().map(|h| h.1).unwrap_or(f64::NAN)))
}

/// Free levels of one shell (all four sectors, nlev levels from l_min).
pub fn free_shell_levels(grid: &Grid, phys: &Physics, sh: Shell, nlev: usize, tol: f64) -> Result<Vec<(SectorSpec, Vec<f64>)>, String> {
    let free = Pots::free(grid.nf, phys.m);
    let ctx = ctx_for(grid, phys, &free);
    let mut out = Vec::new();
    for (j, par) in SECTORS {
        let lm = ell_min(grid, phys, sh, j, par)?;
        let sec = Sector { k: kmag(phys, sh), j, parity: par };
        let mut prev: Option<f64> = None;
        let mut e = Vec::new();
        for i in 0..nlev {
            let l = lm + i as i64;
            let (eps, _) = find_level(&ctx, sec, target(par, l), prev.map(|p| p + 0.5).unwrap_or(0.0), prev, tol)?;
            e.push(eps);
            prev = Some(eps);
        }
        out.push((SectorSpec { shell: sh, j, parity: par, ell_min: lm, nlev }, e));
    }
    Ok(out)
}

/// Free levels of one sector up to an energy cutoff (at most `cap` levels).
pub fn free_sector_upto(grid: &Grid, phys: &Physics, sh: Shell, j: i32, par: Parity, ecut: f64, tol: f64, cap: usize) -> Result<(SectorSpec, Vec<f64>), String> {
    let free = Pots::free(grid.nf, phys.m);
    let ctx = ctx_for(grid, phys, &free);
    let lm = ell_min(grid, phys, sh, j, par)?;
    let sec = Sector { k: kmag(phys, sh), j, parity: par };
    let mut prev: Option<f64> = None;
    let mut e = Vec::new();
    for i in 0..cap {
        let l = lm + i as i64;
        let (eps, _) = find_level(&ctx, sec, target(par, l), prev.map(|p| p + 0.5).unwrap_or(0.0), prev, tol)?;
        if eps > ecut {
            break;
        }
        e.push(eps);
        prev = Some(eps);
    }
    Ok((SectorSpec { shell: sh, j, parity: par, ell_min: lm, nlev: e.len() }, e))
}

/// The T = 0 label set: shells in increasing n2 until the lowest level of a
/// shell lies above max(LUMO, eps_F) + margin; occupied shells and the next one
/// carry `nlev_occ` levels per sector, the others their lowest level only.
pub fn specs_t0(grid: &Grid, phys: &Physics, margin: f64, nlev_occ: usize, tol: f64) -> Result<Vec<SectorSpec>, String> {
    let mut all_shells = shells(400);
    let mut per_shell: Vec<Vec<(SectorSpec, Vec<f64>)>> = Vec::new();
    let mut si = 0;
    loop {
        if si >= all_shells.len() {
            let n2max = all_shells.last().unwrap().n2 * 2;
            all_shells = shells(n2max);
        }
        let sh = all_shells[si];
        let lv = free_shell_levels(grid, phys, sh, nlev_occ, tol)?;
        let lowest = lv.iter().map(|(_, e)| e[0]).fold(f64::INFINITY, f64::min);
        per_shell.push(lv);
        si += 1;
        // aufbau over everything so far
        let mut lev: Vec<(f64, f64)> = Vec::new();
        for s in &per_shell {
            for (sp, e) in s {
                for &x in e {
                    lev.push((x, 4.0 * sp.shell.r3 as f64));
                }
            }
        }
        lev.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
        let total: f64 = lev.iter().map(|x| x.1).sum();
        if total < phys.n + 1.0 {
            continue;
        }
        let mut cum = 0.0;
        let mut ef = f64::NAN;
        let mut lumo = f64::NAN;
        for (e, g) in &lev {
            if cum < phys.n - 1e-9 {
                cum += g;
                ef = *e;
            } else if *e - ef > 1e-9 {
                lumo = *e;
                break;
            }
        }
        if lumo.is_nan() {
            continue;
        }
        if lowest > lumo.max(ef) + margin {
            break;
        }
        if si > 20000 {
            return Err("label set: too many shells".into());
        }
    }
    // which shells are occupied in the free aufbau
    let mut lev: Vec<(f64, u32)> = Vec::new();
    for s in &per_shell {
        for (sp, e) in s {
            for &x in e {
                lev.push((x, sp.shell.n2));
            }
        }
    }
    lev.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap().then(a.1.cmp(&b.1)));
    let mut occ_max_n2 = 0;
    {
        let mut cum = 0.0;
        let mut e_last = f64::NAN;
        for (e, n2) in &lev {
            let g = 4.0 * per_shell.iter().flatten().find(|(sp, _)| sp.shell.n2 == *n2).unwrap().0.shell.r3 as f64;
            if cum < phys.n - 1e-9 || (*e - e_last).abs() <= 1e-9 {
                cum += g;
                e_last = *e;
                occ_max_n2 = occ_max_n2.max(*n2);
            } else {
                break;
            }
        }
    }
    let mut specs = Vec::new();
    let mut extra_done = false;
    for s in &per_shell {
        let n2 = s[0].0.shell.n2;
        let full = n2 <= occ_max_n2 || !extra_done;
        if n2 > occ_max_n2 {
            extra_done = true;
        }
        for (sp, _) in s {
            let mut sp = sp.clone();
            sp.nlev = if full { nlev_occ } else { 1 };
            specs.push(sp);
        }
    }
    Ok(specs)
}

/// The thermal label set: every particle level with free energy below ecut.
pub fn specs_thermal(grid: &Grid, phys: &Physics, ecut: f64, tol: f64) -> Result<Vec<SectorSpec>, String> {
    let mut specs = Vec::new();
    let mut all_shells = shells(400);
    let mut si = 0;
    loop {
        if si >= all_shells.len() {
            let n2max = all_shells.last().unwrap().n2 * 2;
            all_shells = shells(n2max);
        }
        let sh = all_shells[si];
        si += 1;
        let mut any = false;
        for (j, par) in SECTORS {
            let (sp, e) = free_sector_upto(grid, phys, sh, j, par, ecut, tol, 400)?;
            if !e.is_empty() {
                any = true;
                specs.push(sp);
            }
        }
        if !any && sh.n2 > 0 {
            break;
        }
        if si > 200000 {
            return Err("thermal label set: too many shells".into());
        }
    }
    Ok(specs)
}
