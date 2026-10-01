//! Shooting for the 2 x 2 block equations in the hidden coordinate y.
//!
//! Block equation (ks-theory.json, blockEquation.realForm), chi = (a, i b) with
//! a, b real:
//!     a' = M a - (K + j (eps - v)) b,
//!     b' = (j (eps - v) - K) a - M b,
//! K(y) = kappa(y) k + j w_Q(y), kappa = e^{-Hy - a4,0}; w_Q = 0 for the
//! canonical (uniform-gas exchange) functional, w_Q = lambda Q/16 for the
//! exact-Fock variant.
//!
//! Method (justification): the problem is a 1D Dirac (first-order 2 x 2)
//! eigenproblem with separated boundary conditions; the Pruefer angle
//! theta = atan2(b, a) obeys theta' = j(eps - v) - K cos 2theta - M sin 2theta,
//! and d theta(0)/d eps = j int r^2 dy / r(0)^2, so Phi(eps) = j theta(0) is
//! STRICTLY INCREASING in eps.  The tip condition fixes theta(-L) = theta_tip/2
//! (canonical theta_tip = 0: b(-L) = 0), the ASSUMED Z2 brane conditions are
//! b(0) = 0 (even parity, Phi = l pi) and a(0) = 0 (odd parity,
//! Phi = pi/2 + l pi).  Every eigenvalue is therefore the unique root of
//! Phi(eps) = t_l for an integer label l (oscillation theorem): no level in a
//! window can be missed, and the label l is a topological level index that is
//! preserved under continuous changes of the potentials (it is used to follow
//! levels between slices, couplings and SCF iterations).
//!
//! Integration: classical RK4 on a uniform grid of G steps, h = L/G; the
//! potentials are stored on the fine grid of 2G+1 points (nodes and step
//! midpoints) so that every RK4 stage uses exact stored values.  Orbital
//! values at the midpoints are completed by cubic Hermite interpolation from
//! the node values and the node derivatives (error O(h^4), the order of RK4).
//! Integrals use Simpson's rule on the fine grid.

use crate::model::Parity;
use std::f64::consts::PI;

pub struct Grid {
    pub g: usize,
    #[allow(dead_code)]
    pub l: f64,
    #[allow(dead_code)]
    pub hh: f64,
    pub h: f64,
    pub nf: usize,
    pub y: Vec<f64>,
    pub simpson: Vec<f64>,
    /// e^{-H y}
    pub ew: Vec<f64>,
    /// e^{6 H y} (proper 7-volume per coordinate volume)
    pub e6: Vec<f64>,
}

impl Grid {
    pub fn new(hh: f64, l: f64, g: usize) -> Grid {
        let nf = 2 * g + 1;
        let h = l / g as f64;
        let y: Vec<f64> = (0..nf).map(|f| -l * ((nf - 1 - f) as f64 / (nf - 1) as f64)).collect();
        let hf = 0.5 * h;
        let mut simpson = vec![0.0; nf];
        for (f, w) in simpson.iter_mut().enumerate() {
            *w = if f == 0 || f == nf - 1 {
                hf / 3.0
            } else if f % 2 == 1 {
                4.0 * hf / 3.0
            } else {
                2.0 * hf / 3.0
            };
        }
        let ew = y.iter().map(|&y| (-hh * y).exp()).collect();
        let e6 = y.iter().map(|&y| (6.0 * hh * y).exp()).collect();
        Grid { g, l, hh, h, nf, y, simpson, ew, e6 }
    }
    pub fn integrate(&self, f: &[f64]) -> f64 {
        let mut s = 0.0;
        for i in 0..self.nf {
            s += self.simpson[i] * f[i];
        }
        s
    }
}

/// Potentials on the fine grid.
#[derive(Clone, Debug)]
pub struct Pots {
    pub mass: Vec<f64>,
    pub v: Vec<f64>,
    pub wq: Vec<f64>,
}

impl Pots {
    pub fn free(nf: usize, m: f64) -> Pots {
        Pots { mass: vec![m; nf], v: vec![0.0; nf], wq: vec![0.0; nf] }
    }
}

pub struct Ctx<'a> {
    pub grid: &'a Grid,
    /// e^{-a4,0}
    pub kap0: f64,
    pub pots: &'a Pots,
    /// initial Pruefer angle theta_tip / 2
    pub tip_angle: f64,
}

#[derive(Clone, Copy, Debug)]
pub struct Sector {
    /// |k| (coordinate 3-momentum)
    pub k: f64,
    pub j: i32,
    #[allow(dead_code)]
    pub parity: Parity,
}

#[derive(Clone, Copy, Debug)]
pub struct Shot {
    pub phi: f64,
    pub dphi: f64,
    pub max_step_angle: f64,
}

/// Target value of Phi for label l.
pub fn target(parity: Parity, l: i64) -> f64 {
    match parity {
        Parity::Even => l as f64 * PI,
        Parity::Odd => 0.5 * PI + l as f64 * PI,
    }
}

#[inline(always)]
fn rhs(m: f64, kk: f64, je: f64, a: f64, b: f64) -> (f64, f64) {
    (m * a - (kk + je) * b, (je - kk) * a - m * b)
}

/// Integrate from the tip to the brane.  If `store` is given (length 2 nf),
/// the node values (a, b) are written at the even fine indices.
pub fn shoot(ctx: &Ctx, sec: Sector, eps: f64, mut store: Option<&mut [f64]>) -> Shot {
    let gr = ctx.grid;
    let p = ctx.pots;
    let jf = sec.j as f64;
    let kk = sec.k * ctx.kap0;
    let h = gr.h;
    let hh = 0.5 * h;
    let h6 = h / 6.0;
    let mut a = ctx.tip_angle.cos();
    let mut b = ctx.tip_angle.sin();
    let mut theta = ctx.tip_angle;
    let mut raw = b.atan2(a);
    let coef = |f: usize| -> (f64, f64, f64) { (p.mass[f], kk * gr.ew[f] + jf * p.wq[f], jf * (eps - p.v[f])) };
    let mut acc = 0.0;
    let mut r2p = a * a + b * b;
    let mut maxd: f64 = 0.0;
    if let Some(s) = store.as_deref_mut() {
        s[0] = a;
        s[1] = b;
    }
    let (mut m0, mut k0, mut e0) = coef(0);
    for i in 0..gr.g {
        let (m1, k1, e1) = coef(2 * i + 1);
        let (m2, k2, e2) = coef(2 * i + 2);
        let (p1a, p1b) = rhs(m0, k0, e0, a, b);
        let (p2a, p2b) = rhs(m1, k1, e1, a + hh * p1a, b + hh * p1b);
        let (p3a, p3b) = rhs(m1, k1, e1, a + hh * p2a, b + hh * p2b);
        let (p4a, p4b) = rhs(m2, k2, e2, a + h * p3a, b + h * p3b);
        a += h6 * (p1a + 2.0 * p2a + 2.0 * p3a + p4a);
        b += h6 * (p1b + 2.0 * p2b + 2.0 * p3b + p4b);
        let nr = b.atan2(a);
        let mut d = nr - raw;
        if d > PI {
            d -= 2.0 * PI;
        } else if d <= -PI {
            d += 2.0 * PI;
        }
        maxd = maxd.max(d.abs());
        theta += d;
        raw = nr;
        let r2 = a * a + b * b;
        acc += hh * (r2p + r2);
        r2p = r2;
        if let Some(s) = store.as_deref_mut() {
            s[2 * (2 * i + 2)] = a;
            s[2 * (2 * i + 2) + 1] = b;
        }
        if r2 > 1e250 {
            let sc = 1.0 / r2.sqrt();
            a *= sc;
            b *= sc;
            acc *= sc * sc;
            r2p *= sc * sc;
            if let Some(s) = store.as_deref_mut() {
                for x in s[..2 * (2 * i + 2) + 2].iter_mut() {
                    *x *= sc;
                }
            }
        }
        m0 = m2;
        k0 = k2;
        e0 = e2;
    }
    Shot { phi: jf * theta, dphi: acc / r2p, max_step_angle: maxd }
}

/// Root of Phi(eps) = t by a safeguarded Newton iteration with a bracket.
/// `lower`: an energy known to satisfy Phi < t (e.g. the previous level).
pub fn find_level(ctx: &Ctx, sec: Sector, t: f64, guess: f64, lower: Option<f64>, tol: f64) -> Result<(f64, usize), String> {
    let evals = std::cell::Cell::new(0usize);
    let ev = |e: f64| -> Result<Shot, String> {
        evals.set(evals.get() + 1);
        let s = shoot(ctx, sec, e, None);
        if !(s.max_step_angle < 2.0) || !s.phi.is_finite() {
            return Err(format!("Pruefer angle step {} too large at eps {} (k {}, j {})", s.max_step_angle, e, sec.k, sec.j));
        }
        Ok(s)
    };
    let mut ec = guess;
    let s = ev(ec)?;
    let mut gc = s.phi - t;
    let mut dc = s.dphi;
    if gc == 0.0 {
        return Ok((ec, evals.get()));
    }
    let mut lo;
    let mut hi;
    if gc < 0.0 {
        lo = ec;
        let mut step = ((-gc / dc) * 1.2).clamp(1e-4, 2.0);
        loop {
            let e = lo + step;
            let s = ev(e)?;
            let g = s.phi - t;
            if g >= 0.0 {
                hi = e;
                if g.abs() < gc.abs() {
                    ec = e;
                    gc = g;
                    dc = s.dphi;
                }
                break;
            }
            lo = e;
            ec = e;
            gc = g;
            dc = s.dphi;
            step *= 2.0;
            if evals.get() > 400 {
                return Err(format!("no upper bracket for t {} from {}", t, guess));
            }
        }
    } else {
        hi = ec;
        if let Some(lb) = lower {
            lo = lb;
        } else {
            let mut step = ((gc / dc) * 1.2).clamp(1e-4, 2.0);
            loop {
                let e = hi - step;
                let s = ev(e)?;
                let g = s.phi - t;
                if g <= 0.0 {
                    lo = e;
                    if g.abs() < gc.abs() {
                        ec = e;
                        gc = g;
                        dc = s.dphi;
                    }
                    break;
                }
                hi = e;
                ec = e;
                gc = g;
                dc = s.dphi;
                step *= 2.0;
                if evals.get() > 400 {
                    return Err(format!("no lower bracket for t {} from {}", t, guess));
                }
            }
        }
    }
    if gc == 0.0 {
        return Ok((ec, evals.get()));
    }
    let mut prev_abs = f64::INFINITY;
    for _ in 0..300 {
        if hi - lo <= tol {
            break;
        }
        let mut en = ec - gc / dc;
        let bisect = !(en > lo && en < hi) || gc.abs() > 0.5 * prev_abs;
        if bisect {
            en = 0.5 * (lo + hi);
        }
        prev_abs = gc.abs();
        let s = ev(en)?;
        let g = s.phi - t;
        let step = (en - ec).abs();
        ec = en;
        gc = g;
        dc = s.dphi;
        if g == 0.0 {
            break;
        }
        if g < 0.0 {
            lo = en;
        } else {
            hi = en;
        }
        if step <= tol && !bisect {
            break;
        }
    }
    Ok((ec, evals.get()))
}

/// Normalised orbital on the fine grid: interleaved (a, b), int (a^2+b^2) dy = 1.
pub fn profile(ctx: &Ctx, sec: Sector, eps: f64) -> Vec<f64> {
    let gr = ctx.grid;
    let p = ctx.pots;
    let mut s = vec![0.0; 2 * gr.nf];
    shoot(ctx, sec, eps, Some(&mut s));
    let jf = sec.j as f64;
    let kk = sec.k * ctx.kap0;
    let deriv = |f: usize, a: f64, b: f64| -> (f64, f64) { rhs(p.mass[f], kk * gr.ew[f] + jf * p.wq[f], jf * (eps - p.v[f]), a, b) };
    let h = gr.h;
    for i in 0..gr.g {
        let f0 = 2 * i;
        let f2 = 2 * i + 2;
        let (a0, b0) = (s[2 * f0], s[2 * f0 + 1]);
        let (a2, b2) = (s[2 * f2], s[2 * f2 + 1]);
        let (da0, db0) = deriv(f0, a0, b0);
        let (da2, db2) = deriv(f2, a2, b2);
        s[2 * (f0 + 1)] = 0.5 * (a0 + a2) + h / 8.0 * (da0 - da2);
        s[2 * (f0 + 1) + 1] = 0.5 * (b0 + b2) + h / 8.0 * (db0 - db2);
    }
    let mut nrm = 0.0;
    for f in 0..gr.nf {
        nrm += gr.simpson[f] * (s[2 * f] * s[2 * f] + s[2 * f + 1] * s[2 * f + 1]);
    }
    let sc = 1.0 / nrm.sqrt();
    for x in s.iter_mut() {
        *x *= sc;
    }
    s
}

/// Boundary residual of a normalised profile at the brane (b(0) for even, a(0) for odd).
pub fn brane_residual(prof: &[f64], nf: usize, parity: Parity) -> f64 {
    match parity {
        Parity::Even => prof[2 * (nf - 1) + 1].abs(),
        Parity::Odd => prof[2 * (nf - 1)].abs(),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn free_k0_even_spectrum_and_zero_mode() {
        let grid = Grid::new(1.0, 3.0, 600);
        let pots = Pots::free(grid.nf, 1.0);
        let ctx = Ctx { grid: &grid, kap0: 1.0, pots: &pots, tip_angle: 0.0 };
        let sec = Sector { k: 0.0, j: 1, parity: Parity::Even };
        let (e0, _) = find_level(&ctx, sec, target(Parity::Even, 0), 0.0, None, 1e-13).unwrap();
        assert_eq!(e0, 0.0);
        for l in 1..4i64 {
            let (e, _) = find_level(&ctx, sec, target(Parity::Even, l), 0.0, None, 1e-13).unwrap();
            let exact = (1.0f64 + (l as f64 * PI / 3.0).powi(2)).sqrt();
            assert!((e - exact).abs() < 5e-9, "l {} eps {} exact {}", l, e, exact);
        }
    }

    #[test]
    fn phi_is_increasing_for_both_block_types() {
        let grid = Grid::new(1.0, 3.0, 300);
        let pots = Pots::free(grid.nf, 1.0);
        let ctx = Ctx { grid: &grid, kap0: 1.0, pots: &pots, tip_angle: 0.0 };
        for j in [1, -1] {
            let sec = Sector { k: 0.75, j, parity: Parity::Odd };
            let mut prev = f64::NEG_INFINITY;
            for i in 0..200 {
                let s = shoot(&ctx, sec, -4.0 + 0.04 * i as f64, None);
                assert!(s.phi > prev && s.dphi > 0.0);
                prev = s.phi;
            }
        }
    }
}
