//! Pruefer-angle shooting for the levels of one (k, parity) 2x2 problem.
//!
//! Block type s = +1 (blocks 0..3; the s = -1 blocks are the same problem
//! with eps -> -eps, see `blocks.rs`).  With `chi = (a, i b)` the reduced
//! Kohn-Sham equation on the tip-cutoff interval y in [-L, 0] reads
//!
//! ```text
//! a' =  M(y) a + (E(y) - kappa(y) k) b,      E(y) = eps - v_x(y),
//! b' = -(E(y) + kappa(y) k) a - M(y) b,      kappa(y) = e^{-Hy - a4_0},
//! ```
//!
//! with `M(y) = m + lambda S_p + v_s` and the LDA vector potential `v_x`.
//!
//! Boundary conditions.  Brane y = 0 (Z2 parity `Psi(-y) = +- gamma^0
//! Psi(y)`): `chi(0)` is a gamma^0 = sigma_z eigenvector, i.e. `b(0) = 0`
//! (parity +) or `a(0) = 0` (parity -).  Tip cutoff y = -L: the bag
//! condition `gamma^0 chi(-L) = +chi(-L)`, i.e. `b(-L) = 0`.  Both kill the
//! y-current `-i chi^dagger (BC gamma^0) chi = -2 s Re(a conj(i b))`, which
//! vanishes identically for real (a, b): a standing wave carries no current.
//! (In signature (4,4) the hidden direction is space-like with
//! (gamma^0)^2 = +1, so the MIT-type condition n.gamma chi = +-chi carries no
//! factor i and coincides with a gamma^0 projection.)  The + sign at -L is
//! chosen because it admits no tip-localised zero mode for M > 0 (the -
//! sign would give the cutoff artefact `b = e^{-My}` in the odd channel);
//! for parity + and k = 0 it gives the exact brane zero mode `a = e^{My}`,
//! `b = 0`, `eps = 0`, whose energy is lifted by k.
//!
//! Pruefer form: `a = r cos(theta)`, `b = -r sin(theta)`:
//!
//! ```text
//! theta' = E(y) + kappa k cos(2 theta) - M sin(2 theta),   theta(-L) = 0,
//! (ln r)' = M cos(2 theta) + kappa k sin(2 theta).
//! ```
//!
//! `d theta'/d eps = 1 > 0`, so `Theta(eps) := theta(0; eps)` is strictly
//! increasing (comparison theorem): the levels of parity + are exactly the
//! solutions of `Theta(eps) = n pi`, those of parity - of
//! `Theta(eps) = pi/2 + n pi`, n in Z, one for each n (Sturm-type
//! oscillation theorem for the 1D Dirac operator).  `n` is the level index; every level in a window is
//! found, none is missed, and the node-count criterion is the winding of
//! the profile, re-measured from the linear solution.
//!
//! Level search: bracket the target in eps by step doubling, then Illinois
//! regula falsi on `Theta(eps) - target`.  Profiles: the linear system plus
//! the accumulators `I_n' = a^2 + b^2`, `I_S' = -2 a b`, `I_p' = -kappa k
//! (a^2 - b^2)` is integrated once at the level with CVODE, rescaled after
//! any output point where a^2 + b^2 leaves [1e-40, 1e40] (the driver
//! re-initialises CVODE there), and normalised to `int (a^2 + b^2) dy = 1`.
//!
//! Bilinears of the normalised level (block type s): number density
//! `a^2 + b^2`, scalar density `-2 s a b`, 3-space pressure bilinear
//! `-s kappa k (a^2 - b^2)`; Hellmann-Feynman: `d eps/d M = int (-2 a b)`,
//! `d eps/d k = -int kappa (a^2 - b^2)` (checked in the unit tests).

use std::cell::Cell;
use std::rc::Rc;
use std::sync::Arc;

use crate::driver::{Integration, RhsFn, Session, SolverConfig};
use crate::math::{atan2, cos, exp, sin, PI};
use crate::spline::Spline;
use crate::Tolerances;

/// Potentials and geometry of one Kohn-Sham problem on the grid.
#[derive(Clone, Debug)]
pub struct Potential {
    pub h: f64,
    pub a4: f64,
    /// Tip cutoff y = -L.
    pub length: f64,
    /// Uniform grid y_0 = -L, ..., y_{n-1} = 0.
    pub grid: Vec<f64>,
    pub m_eff: Spline,
    pub v_x: Spline,
}

impl Potential {
    /// Constant-mass, zero-potential problem on `n` grid points.
    pub fn free(h: f64, a4: f64, length: f64, mass: f64, n: usize) -> Self {
        let dy = length / (n as f64 - 1.0);
        let grid = grid_points(length, n);
        Self {
            h,
            a4,
            length,
            grid,
            m_eff: Spline::constant(-length, dy, n, mass),
            v_x: Spline::constant(-length, dy, n, 0.0),
        }
    }

    pub fn kappa(&self, y: f64) -> f64 {
        exp(-self.h * y - self.a4)
    }

    pub fn dy(&self) -> f64 {
        self.length / (self.grid.len() as f64 - 1.0)
    }
}

/// -L + i dy, exact end points.
pub fn grid_points(length: f64, n: usize) -> Vec<f64> {
    (0..n)
        .map(|i| {
            if i + 1 == n {
                0.0
            } else {
                -length + length * (i as f64) / (n as f64 - 1.0)
            }
        })
        .collect()
}

/// Solver statistics accumulated by a shooting session.
#[derive(Clone, Copy, Debug, Default)]
pub struct Stats {
    pub integrations: i64,
    pub steps: i64,
    pub rhs_evals: i64,
    pub rescales: i64,
    /// Profile integrations that needed the fallback ladder of
    /// [`Shooter::profile`] (the primary BDF integration failed).
    pub profile_retries: i64,
}

impl Stats {
    fn absorb(&mut self, run: &Integration) {
        self.integrations += 1;
        self.steps += run.steps;
        self.rhs_evals += run.rhs_evals;
    }

    /// Add every counter of `other`.
    pub fn add(&mut self, other: &Stats) {
        self.integrations += other.integrations;
        self.steps += other.steps;
        self.rhs_evals += other.rhs_evals;
        self.rescales += other.rescales;
        self.profile_retries += other.profile_retries;
    }

    /// Counter differences `self - before`.
    pub fn since(&self, before: &Stats) -> Stats {
        Stats {
            integrations: self.integrations - before.integrations,
            steps: self.steps - before.steps,
            rhs_evals: self.rhs_evals - before.rhs_evals,
            rescales: self.rescales - before.rescales,
            profile_retries: self.profile_retries - before.profile_retries,
        }
    }
}

/// Adams-Moulton is used for the Pruefer equation of shells with
/// k kappa(-L) <= ADAMS_STIFFNESS_LIMIT (oscillatory, non-stiff), BDF beyond
/// (measured: Adams needs 2.6x fewer steps at k = 0.5, L = 3, BDF 1.3-2.4x
/// fewer at k = 3 and 8).
pub const ADAMS_THETA_DEFAULT: bool = true;
pub const ADAMS_STIFFNESS_LIMIT: f64 = 20.0;
/// Stop the regula falsi when |theta(0) - target| is below this (the ODE
/// tolerance limits the eigenvalues to ~1e-9 anyway).
pub const THETA_TOLERANCE: f64 = 1.0e-11;
/// |eps| below this is the exact zero mode and is set to 0.
pub const ZERO_SNAP: f64 = 1.0e-10;

/// Fallback ladder of the profile integration: (Adams instead of BDF,
/// divisor of max_step, band of a^2 + b^2 kept by rescaling at the output
/// points).  Variant 0 is the production integration.  MEASURED failure
/// that motivated the ladder (thermo, lambda_hot, T = m, N = 8, shell
/// n2 = 1718, parity +, Pruefer index -2, eps = -18.89693): the potentials
/// are smooth, but the solution amplitude had grown to ~1e17 (evanescent
/// growth e^{k int kappa dy} from the tip) and one component passed through
/// zero at a step point; the fixed atol = 1e-14 is then below the round-off
/// of a component of that scale, the BDF error test failed repeatedly and h
/// collapsed to 3.6e-9 (CVODE flag -3).  BDF with max_step/10 fails the same
/// way; keeping the amplitude O(1) (variant 1: band [1e-2, 1e2]) makes the
/// absolute tolerance meaningful again, and Adams (variants 2, 3) steps
/// differently.  Every retry is counted (`Stats::profile_retries`, run.json
/// `profileRetries`) and the profile is validated like any other.
pub const PROFILE_LADDER: [(bool, f64, (f64, f64)); 4] = [
    (false, 1.0, (1.0e-40, 1.0e40)),
    (false, 1.0, (1.0e-2, 1.0e2)),
    (true, 10.0, (1.0e-40, 1.0e40)),
    (true, 10.0, (1.0e-2, 1.0e2)),
];

pub const DEFAULT_TOLERANCES: Tolerances = Tolerances {
    rtol: 1.0e-12,
    atol: 1.0e-14,
    max_step: 0.05,
};

/// The shooting engine for one potential.
pub struct Shooter {
    pub potential: Arc<Potential>,
    pub tolerances: Tolerances,
    pub stats: Stats,
    /// Use Adams-Moulton (functional iteration) for the Pruefer equation
    /// instead of BDF (the profile integration always uses BDF).
    pub adams_theta: bool,
    /// Parameters read by the right-hand sides of the persistent sessions.
    eps_cell: Rc<Cell<f64>>,
    k_cell: Rc<Cell<f64>>,
    theta_adams: Option<Session>,
    theta_bdf: Option<Session>,
    profile_session: Option<Session>,
}

/// One level of the s = +1 problem at (k, parity).
#[derive(Clone, Debug)]
pub struct Level {
    pub k: f64,
    pub parity: i32,
    /// Pruefer index n (target n pi or pi/2 + n pi).
    pub index: i64,
    pub eps: f64,
    /// theta(0; eps) - target after the search.
    pub theta_residual: f64,
    /// |b(0)| (parity +) or |a(0)| (parity -) divided by r(0), from the linear solution.
    pub matching_residual: f64,
    /// Winding of the linear profile (atan2 unwrapped) minus the target.
    pub winding_residual: f64,
    /// Sign changes of the matched component along the grid.
    pub sign_changes: usize,
    /// Normalised profile on the grid.
    pub a: Vec<f64>,
    pub b: Vec<f64>,
    /// int (-2 a b) dy  (= scalar charge of the s = +1 state = d eps/d M).
    pub scalar_charge: f64,
    /// int (-kappa k (a^2 - b^2)) dy (= k d eps/d k: the 3-space pressure bilinear, s = +1).
    pub pressure_charge: f64,
    /// int (a^2 + b^2) dy before normalisation, in the final rescaled units.
    pub raw_norm: f64,
}

fn target(parity: i32, n: i64) -> f64 {
    if parity > 0 {
        n as f64 * PI
    } else {
        PI / 2.0 + n as f64 * PI
    }
}

impl Shooter {
    pub fn new(potential: Arc<Potential>, tolerances: Tolerances) -> Self {
        Self {
            potential,
            tolerances,
            stats: Stats::default(),
            adams_theta: ADAMS_THETA_DEFAULT,
            eps_cell: Rc::new(Cell::new(0.0)),
            k_cell: Rc::new(Cell::new(0.0)),
            theta_adams: None,
            theta_bdf: None,
            profile_session: None,
        }
    }

    fn theta_rhs(&self) -> RhsFn {
        let pot = Arc::clone(&self.potential);
        let eps_cell = Rc::clone(&self.eps_cell);
        let k_cell = Rc::clone(&self.k_cell);
        Box::new(move |y, th, dth| {
            let m = pot.m_eff.eval(y);
            let e = eps_cell.get() - pot.v_x.eval(y);
            let kk = pot.kappa(y) * k_cell.get();
            let two = 2.0 * th[0];
            dth[0] = e + kk * cos(two) - m * sin(two);
            Ok(())
        })
    }

    fn profile_rhs(&self) -> RhsFn {
        let pot = Arc::clone(&self.potential);
        let eps_cell = Rc::clone(&self.eps_cell);
        let k_cell = Rc::clone(&self.k_cell);
        Box::new(move |y, st, d| {
            let m = pot.m_eff.eval(y);
            let e = eps_cell.get() - pot.v_x.eval(y);
            let kap = pot.kappa(y);
            let kk = kap * k_cell.get();
            let (a, b) = (st[0], st[1]);
            d[0] = m * a + (e - kk) * b;
            d[1] = -(e + kk) * a - m * b;
            d[2] = a * a + b * b;
            d[3] = -2.0 * a * b;
            d[4] = -kk * (a * a - b * b);
            Ok(())
        })
    }

    /// Pruefer-equation solver: Adams for non-stiff shells (k e^{HL + a4}
    /// small: the evanescent attraction rate 2 kappa k stays moderate), BDF
    /// otherwise; both are exact to the tolerances.
    fn config(&self, k: f64) -> SolverConfig {
        let stiffness = (k * self.potential.kappa(-self.potential.length)).abs();
        if self.adams_theta && stiffness <= ADAMS_STIFFNESS_LIMIT {
            SolverConfig::adams(
                self.tolerances.rtol,
                self.tolerances.atol,
                self.tolerances.max_step,
            )
            .with_stop_time(0.0)
        } else {
            SolverConfig::bdf(
                self.tolerances.rtol,
                self.tolerances.atol,
                self.tolerances.max_step,
            )
            .with_stop_time(0.0)
        }
    }

    /// theta(0; eps) for the Pruefer equation.
    pub fn theta_end(&mut self, k: f64, eps: f64) -> Result<f64, String> {
        self.eps_cell.set(eps);
        self.k_cell.set(k);
        let cfg = self.config(k);
        let use_adams = cfg.method == crate::driver::Method::Adams;
        let y0 = [0.0];
        let t0 = -self.potential.length;
        if use_adams && self.theta_adams.is_none() {
            self.theta_adams = Some(Session::new(&y0, t0, self.theta_rhs(), &cfg)?);
        }
        if !use_adams && self.theta_bdf.is_none() {
            self.theta_bdf = Some(Session::new(&y0, t0, self.theta_rhs(), &cfg)?);
        }
        let session = if use_adams {
            self.theta_adams.as_mut()
        } else {
            self.theta_bdf.as_mut()
        }
        .ok_or_else(|| "internal: theta session missing".to_string())?;
        let run = session.run(&y0, t0, &[0.0], None)?;
        self.stats.absorb(&run);
        Ok(run.states[1][0])
    }

    /// Find the level of index `n` for (k, parity) starting from `guess`
    /// (`initial_step`: first bracketing step; small for warm starts).
    pub fn find_level(
        &mut self,
        k: f64,
        parity: i32,
        n: i64,
        guess: f64,
        initial_step: f64,
    ) -> Result<(f64, f64), String> {
        let t = target(parity, n);
        let mut e0 = guess;
        let mut f0 = self.theta_end(k, e0)? - t;
        if f0 == 0.0 {
            return Ok((e0, 0.0));
        }
        // bracket by step doubling in the direction that reduces |f|; the
        // first step is at least the Newton-like estimate |f0| / L of the
        // distance to the root (d Theta / d eps = L for a free particle at
        // high energy; Theta is monotone, so an under- or overshoot only
        // changes the number of bracketing evaluations, never the root)
        let direction = if f0 < 0.0 { 1.0 } else { -1.0 };
        let mut step = initial_step.max(1.05 * f0.abs() / self.potential.length);
        let mut e1 = e0 + direction * step;
        let mut f1 = self.theta_end(k, e1)? - t;
        let mut tries = 0;
        while f0 * f1 > 0.0 {
            e0 = e1;
            f0 = f1;
            step *= 2.0;
            e1 = e0 + direction * step;
            f1 = self.theta_end(k, e1)? - t;
            tries += 1;
            if tries > 60 {
                return Err(format!(
                    "find_level: no bracket for k={k} parity={parity} n={n}"
                ));
            }
        }
        // Illinois regula falsi
        let (mut lo, mut flo, mut hi, mut fhi) = if e0 < e1 {
            (e0, f0, e1, f1)
        } else {
            (e1, f1, e0, f0)
        };
        let mut side = 0;
        let mut best = (lo, flo);
        for _ in 0..200 {
            let e = (lo * fhi - hi * flo) / (fhi - flo);
            let f = self.theta_end(k, e)? - t;
            if f.abs() < best.1.abs() {
                best = (e, f);
            }
            if f.abs() < THETA_TOLERANCE {
                return Ok((e, f));
            }
            if f * flo < 0.0 {
                hi = e;
                fhi = f;
                if side == -1 {
                    flo *= 0.5;
                }
                side = -1;
            } else {
                lo = e;
                flo = f;
                if side == 1 {
                    fhi *= 0.5;
                }
                side = 1;
            }
            if (hi - lo).abs() <= 1e-14 * lo.abs().max(hi.abs()).max(1.0) {
                return Ok(best);
            }
        }
        Ok(best)
    }

    /// Index range of the levels with eps in [eps_lo, eps_hi]: (n_min, n_max)
    /// (inclusive) for the given parity; `None` when the window is empty.
    pub fn index_window(
        &mut self,
        k: f64,
        parity: i32,
        eps_lo: f64,
        eps_hi: f64,
    ) -> Result<Option<(i64, i64)>, String> {
        let th_lo = self.theta_end(k, eps_lo)?;
        let th_hi = self.theta_end(k, eps_hi)?;
        let offset = if parity > 0 { 0.0 } else { PI / 2.0 };
        // n with th_lo < offset + n pi < th_hi
        let n_min = ((th_lo - offset) / PI).floor() as i64 + 1;
        let n_max = ((th_hi - offset) / PI).ceil() as i64 - 1;
        if n_max < n_min {
            Ok(None)
        } else {
            Ok(Some((n_min, n_max)))
        }
    }

    /// All levels with eps in the window, with profiles.  `warm` gives
    /// previous eigenvalues by index (warm start).
    pub fn levels(
        &mut self,
        k: f64,
        parity: i32,
        eps_lo: f64,
        eps_hi: f64,
        warm: &[(i64, f64)],
    ) -> Result<Vec<Level>, String> {
        let mut out = Vec::new();
        let Some((n_min, n_max)) = self.index_window(k, parity, eps_lo, eps_hi)? else {
            return Ok(out);
        };
        let mut previous: Option<f64> = None;
        for n in n_min..=n_max {
            let warm_value = warm.iter().find(|(i, _)| *i == n).map(|(_, e)| *e);
            let guess = warm_value
                .or(previous.map(|e| e + PI / self.potential.length))
                .unwrap_or(0.5 * (eps_lo + eps_hi));
            let initial_step = if warm_value.is_some() {
                1e-3 * guess.abs().max(1.0)
            } else {
                0.25
            };
            let (eps, residual) = self.find_level(k, parity, n, guess, initial_step)?;
            // the exact brane zero mode (theta = 0 identically) is found to
            // |eps| < THETA_TOLERANCE/L: snap it to 0 so that it is classified
            // as a particle state (eps >= 0) in both block types
            let eps = if eps.abs() < ZERO_SNAP { 0.0 } else { eps };
            previous = Some(eps);
            let mut level = self.profile(k, parity, eps).map_err(|e| {
                format!(
                    "profile of level k = {k}, parity = {parity}, index = {n}, eps = {eps}: {e}"
                )
            })?;
            level.index = n;
            level.theta_residual = residual;
            out.push(level);
        }
        Ok(out)
    }

    /// One integration of the linear profile system at the current (eps, k)
    /// with the solver variant `variant` of the fallback ladder
    /// ([`PROFILE_LADDER`]): the method, the maximum step and the band of
    /// a^2 + b^2 outside which the state is rescaled (CVodeReInit) at an
    /// output point.  Variant 0 is the persistent BDF session used for every
    /// production integration.  Returns the run, the log scale applied after
    /// each target and the number of rescalings.
    pub fn integrate_profile(
        &mut self,
        variant: usize,
    ) -> Result<(Integration, Vec<f64>, i64), String> {
        let tol = self.tolerances;
        let (adams, step_divisor, band) = PROFILE_LADDER[variant.min(PROFILE_LADDER.len() - 1)];
        let max_step = tol.max_step / step_divisor;
        let cfg = if adams {
            SolverConfig::adams(tol.rtol, tol.atol, max_step)
        } else {
            SolverConfig::bdf(tol.rtol, tol.atol, max_step)
        }
        .with_stop_time(0.0);
        let (band_lo, band_hi) = band;
        let y0 = [1.0, 0.0, 0.0, 0.0, 0.0];
        let t0 = -self.potential.length;
        let targets: Vec<f64> = self.potential.grid[1..].to_vec();
        let mut log_scales: Vec<f64> = Vec::with_capacity(targets.len());
        let mut rescales = 0i64;
        let mut fresh = if variant == 0 {
            if self.profile_session.is_none() {
                self.profile_session = Some(Session::new(&y0, t0, self.profile_rhs(), &cfg)?);
            }
            None
        } else {
            Some(Session::new(&y0, t0, self.profile_rhs(), &cfg)?)
        };
        let run = {
            let mut adjust = |_y: f64, st: &mut [f64]| -> bool {
                let r2 = st[0] * st[0] + st[1] * st[1];
                if r2 > band_hi || (r2 < band_lo && r2 > 0.0) {
                    let r = r2.sqrt();
                    st[0] /= r;
                    st[1] /= r;
                    st[2] /= r2;
                    st[3] /= r2;
                    st[4] /= r2;
                    log_scales.push(crate::math::log(r));
                    rescales += 1;
                    true
                } else {
                    log_scales.push(0.0);
                    false
                }
            };
            let session = match fresh.as_mut() {
                Some(session) => session,
                None => self
                    .profile_session
                    .as_mut()
                    .ok_or_else(|| "internal: profile session missing".to_string())?,
            };
            session.run(&y0, t0, &targets, Some(&mut adjust))?
        };
        Ok((run, log_scales, rescales))
    }

    /// Integrate the linear system at eps and build the normalised profile.
    /// If the primary BDF integration fails (CVODE error), the fallback
    /// ladder of [`Shooter::integrate_profile`] is tried in order and the
    /// retry is counted in `stats.profile_retries`; the profile is then
    /// validated like every other one (matching and winding residuals).
    pub fn profile(&mut self, k: f64, parity: i32, eps: f64) -> Result<Level, String> {
        self.eps_cell.set(eps);
        self.k_cell.set(k);
        let grid = self.potential.grid.clone();
        let (run, log_scales, rescales) = match self.integrate_profile(0) {
            Ok(result) => result,
            Err(first) => {
                self.stats.profile_retries += 1;
                let mut messages = vec![first];
                let mut outcome = None;
                for variant in 1..PROFILE_LADDER.len() {
                    match self.integrate_profile(variant) {
                        Ok(result) => {
                            outcome = Some(result);
                            break;
                        }
                        Err(message) => messages.push(message),
                    }
                }
                outcome.ok_or_else(|| {
                    format!(
                        "all profile integration variants failed: {}",
                        messages.join("; ")
                    )
                })?
            }
        };
        self.stats.absorb(&run);
        self.stats.rescales += rescales;
        let n = grid.len();
        // cumulative log scale after each target (index i of the grid, i >= 1)
        let mut cumulative = vec![0.0; n];
        for i in 1..n {
            cumulative[i] = cumulative[i - 1] + log_scales[i - 1];
        }
        let total = cumulative[n - 1];
        let last = &run.states[n - 1];
        let raw_norm = last[2];
        if raw_norm.partial_cmp(&0.0) != Some(std::cmp::Ordering::Greater) || !raw_norm.is_finite()
        {
            return Err(format!("profile: non-positive norm at eps={eps}"));
        }
        let scale = 1.0 / raw_norm.sqrt();
        let mut a = vec![0.0; n];
        let mut b = vec![0.0; n];
        for i in 0..n {
            let st = &run.states[i];
            let factor = exp(cumulative[i] - total) * scale;
            a[i] = st[0] * factor;
            b[i] = st[1] * factor;
        }
        let r0 = (last[0] * last[0] + last[1] * last[1]).sqrt();
        let matching_residual = if parity > 0 {
            last[1].abs()
        } else {
            last[0].abs()
        } / r0;
        // winding: theta with a = r cos theta, b = -r sin theta, unwrapped
        let mut theta_prev = 0.0;
        let mut winding = 0.0;
        for i in 1..n {
            let th = atan2(-run.states[i][1], run.states[i][0]);
            let mut d = th - theta_prev;
            while d > PI {
                d -= 2.0 * PI;
            }
            while d < -PI {
                d += 2.0 * PI;
            }
            winding += d;
            theta_prev = th;
        }
        let offset = if parity > 0 { 0.0 } else { PI / 2.0 };
        let index_from_winding = ((winding - offset) / PI).round();
        let winding_residual = winding - (offset + index_from_winding * PI);
        let matched = if parity > 0 { &b } else { &a };
        let mut sign_changes = 0;
        let mut previous_sign = 0.0;
        for (i, value) in matched.iter().enumerate() {
            if i == 0 || i + 1 == n {
                continue;
            }
            if *value != 0.0 {
                let sgn = value.signum();
                if previous_sign != 0.0 && sgn != previous_sign {
                    sign_changes += 1;
                }
                previous_sign = sgn;
            }
        }
        Ok(Level {
            k,
            parity,
            index: index_from_winding as i64,
            eps,
            theta_residual: 0.0,
            matching_residual,
            winding_residual,
            sign_changes,
            a,
            b,
            scalar_charge: last[3] / raw_norm,
            pressure_charge: last[4] / raw_norm,
            raw_norm,
        })
    }
}

/// Simpson integration of f on the uniform grid (n odd; n even falls back to
/// trapezoid on the last interval).
pub fn simpson(dy: f64, f: &[f64]) -> f64 {
    let n = f.len();
    if n < 2 {
        return 0.0;
    }
    let mut total = 0.0;
    let mut i = 0;
    while i + 2 < n {
        total += dy / 3.0 * (f[i] + 4.0 * f[i + 1] + f[i + 2]);
        i += 2;
    }
    if i + 1 < n {
        total += 0.5 * dy * (f[i] + f[i + 1]);
    }
    total
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::math::tanh;

    fn shooter(mass: f64, length: f64, n: usize) -> Shooter {
        Shooter::new(
            Arc::new(Potential::free(1.0, 0.0, length, mass, n)),
            DEFAULT_TOLERANCES,
        )
    }

    /// parity - box levels: tan(p L) = -p/M, eps = +-sqrt(M^2 + p^2).
    fn odd_box_momenta(mass: f64, length: f64, count: usize) -> Vec<f64> {
        // roots of g(p) = sin(pL) M + p cos(pL) in each interval ((n-1/2)pi/L, (n+1/2)pi/L)
        let g = |p: f64| sin(p * length) * mass + p * cos(p * length);
        let mut roots = Vec::new();
        let mut n = 0;
        while roots.len() < count {
            let lo = (n as f64 - 0.5) * PI / length + 1e-9;
            let hi = (n as f64 + 0.5) * PI / length - 1e-9;
            let (mut a, mut b) = (lo.max(1e-9), hi);
            if g(a) * g(b) < 0.0 {
                for _ in 0..200 {
                    let m = 0.5 * (a + b);
                    if g(a) * g(m) <= 0.0 {
                        b = m;
                    } else {
                        a = m;
                    }
                }
                let p = 0.5 * (a + b);
                if p > 1e-6 {
                    roots.push(p);
                }
            }
            n += 1;
        }
        roots
    }

    #[test]
    fn free_box_spectrum_parity_plus() {
        let (mass, length) = (1.0, 3.0);
        let mut sh = shooter(mass, length, 301);
        let levels = sh.levels(0.0, 1, -4.0, 4.0, &[]).unwrap();
        let expected: Vec<(i64, f64)> = (-3i64..=3)
            .map(|n| {
                let p = n.abs() as f64 * PI / length;
                (n, (n.signum() as f64) * (mass * mass + p * p).sqrt())
            })
            .collect();
        assert_eq!(
            levels.len(),
            expected.len(),
            "{:?}",
            levels.iter().map(|l| l.eps).collect::<Vec<_>>()
        );
        for (level, (n, e)) in levels.iter().zip(expected.iter()) {
            assert_eq!(level.index, *n);
            assert!(
                (level.eps - e).abs() < 1e-9,
                "n={n} eps={} expected {e}",
                level.eps
            );
            assert!(
                level.matching_residual < 1e-8,
                "{}",
                level.matching_residual
            );
            assert!(
                level.winding_residual.abs() < 1e-6,
                "{}",
                level.winding_residual
            );
            // Hellmann-Feynman d eps/d M = scalar charge, exact box: M/eps for eps != 0
            if *n != 0 {
                assert!(
                    (level.scalar_charge - mass / e).abs() < 1e-8,
                    "{} vs {}",
                    level.scalar_charge,
                    mass / e
                );
            } else {
                assert!(level.scalar_charge.abs() < 1e-8);
                // zero mode a = e^{My} normalised, b = 0
                let norm = (2.0 * mass / (1.0 - exp(-2.0 * mass * length))).sqrt();
                for (y, a) in sh.potential.grid.iter().zip(level.a.iter()) {
                    assert!((a - norm * exp(mass * y)).abs() < 1e-8);
                }
                assert!(level.b.iter().all(|b| b.abs() < 1e-8));
            }
            let norm = simpson(
                sh.potential.dy(),
                &level
                    .a
                    .iter()
                    .zip(level.b.iter())
                    .map(|(a, b)| a * a + b * b)
                    .collect::<Vec<_>>(),
            );
            assert!((norm - 1.0).abs() < 1e-6, "norm {norm}");
        }
        // spectrum symmetric under eps -> -eps at k = 0
        for n in 1..=3usize {
            assert!((levels[3 + n].eps + levels[3 - n].eps).abs() < 1e-9);
        }
    }

    #[test]
    fn free_box_spectrum_parity_minus() {
        let (mass, length) = (1.0, 3.0);
        let mut sh = shooter(mass, length, 301);
        let levels = sh.levels(0.0, -1, -4.0, 4.0, &[]).unwrap();
        let momenta = odd_box_momenta(mass, length, 4);
        let positive: Vec<f64> = levels
            .iter()
            .filter(|l| l.eps > 0.0)
            .map(|l| l.eps)
            .collect();
        let negative: Vec<f64> = levels
            .iter()
            .filter(|l| l.eps < 0.0)
            .map(|l| -l.eps)
            .collect();
        let expected: Vec<f64> = momenta
            .iter()
            .map(|p| (mass * mass + p * p).sqrt())
            .filter(|e| *e < 4.0)
            .collect();
        assert_eq!(
            positive.len(),
            expected.len(),
            "{positive:?} vs {expected:?}"
        );
        for (e, x) in positive.iter().zip(expected.iter()) {
            assert!((e - x).abs() < 3e-9, "{e} vs {x}");
        }
        for (e, x) in negative.iter().rev().zip(expected.iter()) {
            assert!((e - x).abs() < 3e-9, "{e} vs {x}");
        }
        // no zero mode and no evanescent level for M > 0: tanh(qL) = -q/M has no root
        assert!(levels.iter().all(|l| l.eps.abs() > 0.5));
        let _ = tanh(1.0);
    }

    #[test]
    fn momentum_confines_and_lifts_the_zero_mode() {
        // In the s = +1 block at k > 0 the brane mode (index 0) moves to
        // NEGATIVE energy (its mirror at -k, i.e. the s = -1 block, to
        // positive energy): the brane branch is a light two-sign mode with
        // |eps_0(k)| growing with k.  The lowest |eps| over all levels grows
        // with k (confinement raises the lowest excitation).
        let (mass, length) = (1.0, 3.0);
        let mut sh = shooter(mass, length, 301);
        let mut previous_zero = 0.0;
        let mut previous_gap = 0.0;
        for k in [0.25, 0.5, 1.0, 2.0] {
            let atk = sh.levels(k, 1, -4.0, 4.0, &[]).unwrap();
            let zero_k = atk.iter().find(|l| l.index == 0).unwrap();
            assert!(
                zero_k.eps < -previous_zero,
                "brane mode not lifted at k={k}: {}",
                zero_k.eps
            );
            previous_zero = -zero_k.eps;
            let gap = atk
                .iter()
                .map(|l| l.eps.abs())
                .fold(f64::INFINITY, f64::min);
            assert!(
                gap > previous_gap,
                "lowest |eps| not raised at k={k}: {gap}"
            );
            previous_gap = gap;
            // Hellmann-Feynman in k: d eps/dk = pressure_charge / k (5-point stencil)
            let dk = 1e-3;
            let mut shifted = Vec::new();
            for f in [-2.0, -1.0, 1.0, 2.0] {
                shifted.push(sh.levels(k + f * dk, 1, -4.0, 4.0, &[]).unwrap());
            }
            for level in atk.iter().filter(|l| l.index >= 0 && l.index <= 1) {
                let e: Vec<f64> = shifted
                    .iter()
                    .map(|set| set.iter().find(|l| l.index == level.index).unwrap().eps)
                    .collect();
                let fd = (e[0] - 8.0 * e[1] + 8.0 * e[2] - e[3]) / (12.0 * dk);
                assert!(
                    (fd - level.pressure_charge / k).abs() < 1e-7,
                    "k={k} n={} fd={fd} hf={}",
                    level.index,
                    level.pressure_charge / k
                );
            }
        }
        // (k, eps) -> (-k, -eps) symmetry of the block
        let plus = sh.levels(0.5, 1, -3.0, 3.0, &[]).unwrap();
        let minus = sh.levels(-0.5, 1, -3.0, 3.0, &[]).unwrap();
        assert_eq!(plus.len(), minus.len());
        for (p, m) in plus.iter().zip(minus.iter().rev()) {
            assert!((p.eps + m.eps).abs() < 1e-9);
        }
    }

    #[test]
    fn hellmann_feynman_in_mass_with_nonuniform_potential() {
        // M(y) = 1 + 0.3 sin(2y), v(y) = 0.2 cos(3y): d eps/d(M shift) = scalar charge, d eps/d(v shift) = 1
        let (length, n) = (3.0, 301);
        let build = |dm: f64, dv: f64| {
            let dy = length / (n as f64 - 1.0);
            let grid = grid_points(length, n);
            let m: Vec<f64> = grid.iter().map(|y| 1.0 + dm + 0.3 * sin(2.0 * y)).collect();
            let v: Vec<f64> = grid.iter().map(|y| dv + 0.2 * cos(3.0 * y)).collect();
            Arc::new(Potential {
                h: 1.0,
                a4: 0.0,
                length,
                grid,
                m_eff: Spline::new(-length, dy, m),
                v_x: Spline::new(-length, dy, v),
            })
        };
        let mut base = Shooter::new(build(0.0, 0.0), DEFAULT_TOLERANCES);
        let levels = base.levels(0.5, -1, -3.0, 3.0, &[]).unwrap();
        let d = 1e-3;
        let mut shifted: Vec<Shooter> = [-2.0, -1.0, 1.0, 2.0]
            .iter()
            .map(|f| Shooter::new(build(f * d, 0.0), DEFAULT_TOLERANCES))
            .collect();
        let mut vup = Shooter::new(build(0.0, d), DEFAULT_TOLERANCES);
        for level in &levels {
            let e: Vec<f64> = shifted
                .iter_mut()
                .map(|s| {
                    s.find_level(0.5, -1, level.index, level.eps, 1e-3)
                        .unwrap()
                        .0
                })
                .collect();
            let fd = (e[0] - 8.0 * e[1] + 8.0 * e[2] - e[3]) / (12.0 * d);
            assert!(
                (fd - level.scalar_charge).abs() < 1e-7,
                "n={} fd={fd} hf={}",
                level.index,
                level.scalar_charge
            );
            let (ev, _) = vup
                .find_level(0.5, -1, level.index, level.eps, 1e-3)
                .unwrap();
            assert!(((ev - level.eps) / d - 1.0).abs() < 1e-6);
        }
    }

    #[test]
    fn rescaling_handles_deep_evanescence() {
        // k = 6 at L = 4: growth e^{k(e^L - 1)} ~ e^{321} would overflow without rescaling
        let mut sh = shooter(1.0, 4.0, 401);
        let levels = sh.levels(6.0, 1, -12.0, 12.0, &[]).unwrap();
        assert!(!levels.is_empty());
        assert!(sh.stats.rescales > 0);
        for level in &levels {
            assert!(level.a.iter().all(|x| x.is_finite()));
            let norm = simpson(
                sh.potential.dy(),
                &level
                    .a
                    .iter()
                    .zip(level.b.iter())
                    .map(|(a, b)| a * a + b * b)
                    .collect::<Vec<_>>(),
            );
            assert!(
                (norm - 1.0).abs() < 1e-4,
                "norm {norm} at eps {}",
                level.eps
            );
            assert!(level.matching_residual < 1e-7);
        }
    }

    #[test]
    fn profile_fallback_variants_agree_with_the_primary_integration() {
        // every variant of the retry ladder of `profile` must reproduce the
        // primary integration: compare the
        // rescaled end states of a bound level (k = 2, L = 3, rescalings on)
        let mut sh = shooter(1.0, 3.0, 301);
        let levels = sh.levels(2.0, 1, -4.0, 4.0, &[]).unwrap();
        let level = levels.last().expect("a level in [-4, 4]");
        sh.eps_cell.set(level.eps);
        sh.k_cell.set(2.0);
        let (base, base_scales, _) = sh.integrate_profile(0).unwrap();
        let last = base.states.last().unwrap().clone();
        for variant in 1..PROFILE_LADDER.len() {
            let (run, scales, _) = sh.integrate_profile(variant).unwrap();
            let end = run.states.last().unwrap();
            // the rescaling sequence may differ; compare scale-free quantities
            let total = |s: &[f64]| s.iter().sum::<f64>();
            let shift = (total(&scales) - total(&base_scales)).abs();
            let norm = |s: &[f64]| s[0] * s[0] + s[1] * s[1];
            // matched component (parity +: b(0) = 0) and the normalised charges
            assert!(end[1].abs() / norm(end).sqrt() < 1e-7, "variant {variant}");
            for c in [3, 4] {
                let a = end[c] / end[2];
                let b = last[c] / last[2];
                assert!(
                    (a - b).abs() < 1e-8 * b.abs().max(1.0),
                    "variant {variant} c {c}: {a} vs {b}"
                );
            }
            assert!(shift.is_finite());
        }
    }

    #[test]
    fn simpson_is_exact_for_cubics() {
        let f: Vec<f64> = (0..11).map(|i| (i as f64 * 0.1).powi(3)).collect();
        assert!((simpson(0.1, &f) - 0.25).abs() < 1e-14);
    }
}
