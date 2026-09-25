//! EXP-2 -- self-consistent 8D Einstein - dirac16complex homogeneous cosmology.
//!
//! Background (NUMERICS_CONTRACT "Physics common to all experiments"), t = x4,
//! lapse 1, kappa = kappa_8 = 1:
//! `ds^2 = -dt^2 + b^2 dx0^2 + a^2 (dx1^2 + dx2^2 + dx3^2) - c^2 (dx5^2 + dx6^2 + dx7^2)`,
//! H_b = b'/b, H_a = a'/a, H_c = c'/c, Theta = H_b + 3 H_a + 3 H_c,
//! V = b a^3 c^3 (7-volume, V_0 = 1 at t = 0).  The signs of the metric
//! components drop out of the mixed Einstein tensor, which gives
//!   constraint  sum_{i<j} H_i H_j = 3 H_b H_a + 3 H_b H_c + 3 H_a^2 + 3 H_c^2
//!               + 9 H_a H_c = kappa rho,
//!   evolution   H_i' = -H_i Theta + kappa (rho - p) / 6   (D = 8: 1/(D-2)).
//!
//! Matter: the mean-field dirac16complex condensate in the k = 0 mode,
//! `i du/dt = h u`, `h = -i M_eff gamma^4`, `M_eff = m + lambda S`,
//! `S = S_0 (V_0/V) s(u)`, `s(u) = u^dagger (-i gamma^4) u` (expectation-value
//! rule; = 1 on positive-energy rest eigenvectors), U(S) = (lambda/2) S^2.
//! With the mode density n = S_0 V_0 / V (as in EXP-1):
//!   rho  = n u^dagger h u - (lambda/2) S^2  (= m S + (lambda/2) S^2)
//!   p    = n p_j(u) + (lambda/2) S^2        (p_j(u) = 0 at k = 0; isotropic)
//!   KE_L = (1/2) n u^dagger h u = (1/2) S M_eff,  PE_L = rho - KE_L = m S / 2
//!   KE_H = n sum_j p_j(u) = 0,  PE_H = m S + (lambda/2) S^2 = rho
//!   w = p / rho,  w_eff = -1 + (Theta / (3 H_a)) (1 + w)  (3-space observer),
//!   bound = Theta^2 - 3 H_a^2 - 2 kappa rho  (= H_b^2 + 3 H_c^2 on the
//!   constraint surface, hence >= 0).
//! State (38 reals): ln b, ln a, ln c, H_b, H_a, H_c, u (re0..re15, im0..im15).
//!
//! Initial data: H_b = 0, H_a = 1, H_c = -0.2, ln b = ln a = ln c = 0, u(0)
//! the first vector of the joint (h = +M_eff, B = +1) eigenspace (a
//! positive-energy rest eigenvector with positive Krein norm).  x0 := lambda
//! S_0 / (2m) is the run parameter; S_0 is fixed by the constraint:
//! with lambda = 2 m x0 / S_0 the density at t = 0 is
//! `rho = m S_0 s0 (1 + x0 s0)`, s0 = s(u(0)) (= 1 up to rounding), which is
//! linear in S_0, so `S_0 = C_0 / (kappa m s0 (1 + x0 s0))` with C_0 the
//! constraint left-hand side (= 1.32).  Runs x0 in {0, -0.4, +0.5}.
//!
//! Exact solution (derived here, re-derived by the checker).  rho - p = m S
//! is lambda-independent and S V = S_0 s0 is constant, so the evolution
//! equations alone give `V'' = (7/6) kappa m S_0 s0` and
//! `(H_i V)' = kappa m S_0 s0 / 6 =: beta`, i.e.
//!   V(t) = 1 + Theta_0 t + alpha t^2,  alpha = 7 beta / 2,
//!   H_i(t) = (H_i0 + beta t) / V(t),
//!   ln h_i(t) = (1/7) ln V + (H_i0 - Theta_0/7) J(t),  J = int_0^t dt'/V,
//!   u(t) = exp(-i (m t + lambda S_0 s0 J(t))) u(0).
//! With D = Theta_0^2 - 4 alpha > 0 (true for all three runs) V has the two
//! negative roots r_+ = -2/(Theta_0 + sqrt D) (the Kasner-type singularity
//! t_s = r_+, V -> 0 linearly) and r_- = -(Theta_0 + sqrt D)/(2 alpha), and
//! J(t) = [log1p(-t/r_+) - log1p(-t/r_-)] / sqrt D.  Late times: V ~ alpha
//! t^2, H_i t -> 2/7 (8D dust), (H_i - H_j) V = const, w_eff -> 4/3.  Near
//! t_s: H_i / Theta -> p_i = (H_i0 + beta t_s)/sqrt D (Kasner exponents,
//! sum p_i = 1, sum p_i^2 = 1 - 2 kappa m x0 S_0 s0^2 / D; the lambda term is
//! a stiff w = 1 component).
//!
//! Output grid: uniform in the e-fold clock nu = ln V_exact(t), step 0.05,
//! nu in [-7, 18.5]: t_k = T(nu_k), T(nu) = 2 expm1(nu) / (Theta_0 +
//! sqrt(D + 4 alpha e^nu)) (the inverse of the quadratic).  Only the sampling
//! times use the exact solution; CVODE integrates the full 38-dimensional
//! system without it.  Backward the run stops at V/V_0 = e^{-7} (about
//! 1e-3 in t above t_s, where everything is still regular); forward it ends
//! at V/V_0 = e^{18.5} (t ~ 1e4), where the relative anisotropy
//! 7 max|H_i - H_j| / Theta is below 1e-3 for every run.  Both branches use a
//! stop time, so CVODE never steps past the ends (in particular never
//! towards t_s).
//!
//! Solver: CVODE Adams-Moulton + fixed-point iteration (non-stiff: all
//! rates are O(Theta); the spinor oscillates with |M_eff| over ~1e4 time
//! units, where BDF damping would spoil the norm conservation), rtol 1e-12,
//! atol 1e-15, max_step 0.02.  The step cap is needed: left to itself
//! (steps ~0.045 at rtol 1e-12) Adams accumulates a systematic amplitude
//! error of ~5e-13 per step on the oscillating spinor, so u^dag u = s(u)
//! drifts by 1.7e-7 over the forward branch and the constraint residual
//! (rho carries s(u)) reaches 3e-8; with max_step = 0.02 the drift is
//! 4e-10 and the relative constraint residual 1.3e-10.

use crate::driver::{integrate, integrate_backward, Integration, RhsFn, SolverConfig};
use crate::math::{atan, cos, exp, expm1, log, log1p, sin};
use crate::output::{fmt17, standard_summary, write_csv, write_json, Json};
use crate::spinor::{
    energy_projector, involution_projector, mode_energy, mode_pressure, mode_rhs, norm_hilbert,
    norm_krein, range_basis, scalar_density, Algebra, CVec16, STATE_REALS, TRANSVERSE,
};
use crate::{ExperimentSummary, RunContext, Tolerances};

pub const EXPERIMENT: &str = "exp2";
pub const KAPPA: f64 = 1.0;
pub const MASS: f64 = 1.0;
/// Initial Hubble rates (hidden space b, 3-space a, extra times c).
pub const HUBBLE_B0: f64 = 0.0;
pub const HUBBLE_A0: f64 = 1.0;
pub const HUBBLE_C0: f64 = -0.2;
/// Run parameters x0 = lambda S_0 / (2 m).
pub const X0_VALUES: [f64; 3] = [0.0, -0.4, 0.5];
/// Output grid: uniform in nu = ln V_exact with this step.
pub const LN_VOLUME_STEP: f64 = 0.05;
/// nu down to -BACKWARD_INTERVALS * step = -7.
pub const BACKWARD_INTERVALS: usize = 140;
/// nu up to FORWARD_INTERVALS * step = 18.5.
pub const FORWARD_INTERVALS: usize = 370;
/// ln b, ln a, ln c, H_b, H_a, H_c.
pub const GRAVITY_REALS: usize = 6;
pub const STATE_LEN: usize = GRAVITY_REALS + STATE_REALS;
/// Group (0 = b, 1 = a, 2 = c) of the transverse directions 0,1,2,3,5,6,7.
pub const GROUP_OF: [usize; 7] = [0, 1, 1, 1, 2, 2, 2];

pub const DEFAULT_TOLERANCES: Tolerances = Tolerances {
    rtol: 1.0e-12,
    atol: 1.0e-15,
    max_step: 0.02,
};

/// A-priori self-check limits.
pub const EIGEN_LIMIT: f64 = 1.0e-12;
pub const INITIAL_CONSTRAINT_LIMIT: f64 = 1.0e-14;
/// Relative constraint residual (task: < 1e-9).
pub const CONSTRAINT_LIMIT: f64 = 1.0e-9;
/// Conserved quantities: s(u) (= S V / (S_0 V_0)), u^dag u, u^dag B u,
/// (H_i - H_j) V (relative to the largest initial difference).
pub const CONSERVATION_LIMIT: f64 = 1.0e-9;
/// Identity bound = H_b^2 + 3 H_c^2 + 2 residual (relative to Theta^2).
pub const IDENTITY_LIMIT: f64 = 1.0e-13;
/// Relative agreement with the exact solution (V, H_i, ln h_i).  Near t_s
/// the solution is ill-conditioned (a shift dt_s of the singularity changes
/// H by dt_s / (t - t_s)), so the error is divided by the amplification
/// 1 + |t_s| / (t - t_s) (<= ~900 at the backward end).
pub const EXACT_LIMIT: f64 = 1.0e-9;
/// Spinor vs the exact u(t) = exp(-i phi(t)) u0, split into the
/// phase-invariant shape error |u - (u0^dag u) u0| + ||u0^dag u| - 1|
/// (limit CONSERVATION_LIMIT) and the phase error arg(u0^dag u e^{i phi}).
/// The phase error is NOT a truncation error: CVODE accumulates its internal
/// time as t_n += h, which rounds by up to ulp(t_n)/2 per step, and with
/// ~7e5 steps of the constant capped size h = max_step up to t ~ 1e4
/// (ulp ~ 1.8e-12) the rounding is systematic: for t_n in [2^k, 2^(k+1))
/// every step adds the same e_k = fl(t_n + h) - (t_n + h), and the measured
/// phase-drift rate equals M_eff e_k / h in every binade (e.g. -9.10e-13 per
/// unit time for k = 8..11 and +2.18e-11 for k >= 12 at h = 0.02; the
/// checker verifies this in exact Fraction arithmetic).  The state is
/// correct for the elapsed time sum(h) but labelled with the rounded t_n,
/// so the phase error is bounded by max|M_eff| N_steps ulp(t_end)/2 (plus
/// PHASE_TRUNCATION_ALLOWANCE for the tolerance-controlled part); it does not
/// shrink under --refined (twice the steps).
pub const PHASE_TRUNCATION_ALLOWANCE: f64 = 1.0e-9;
/// Late-time convergence (anisotropy, H_i t -> 2/7, w, w_eff -> 4/3).
pub const LATE_TIME_LIMIT: f64 = 1.0e-3;
/// Kasner exponents extrapolated to V = 0 from the three smallest-V rows
/// (extrapolation error O(V^3), plus the solver error amplified near t_s).
pub const KASNER_LIMIT: f64 = 1.0e-6;

/// Constraint left-hand side in the grouped form of the contract.
pub fn pair_sum(hb: f64, ha: f64, hc: f64) -> f64 {
    3.0 * hb * ha + 3.0 * hb * hc + 3.0 * ha * ha + 3.0 * hc * hc + 9.0 * ha * hc
}

/// Sum over i < j of |H_i H_j| (scale of the constraint terms).
pub fn pair_abs_sum(hb: f64, ha: f64, hc: f64) -> f64 {
    3.0 * (hb * ha).abs()
        + 3.0 * (hb * hc).abs()
        + 3.0 * ha * ha
        + 3.0 * hc * hc
        + 9.0 * (ha * hc).abs()
}

/// The exact background (see the module documentation).
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Background {
    pub theta0: f64,
    /// beta = kappa m S_0 V_0 s0 / 6.
    pub beta: f64,
    /// alpha = 7 beta / 2.
    pub alpha: f64,
    /// D = theta0^2 - 4 alpha.
    pub disc: f64,
    /// r_+ = t_s (the singularity), r_- (the far root).
    pub root_near: f64,
    pub root_far: f64,
}

impl Background {
    pub fn new(theta0: f64, source: f64) -> Result<Self, String> {
        let beta = KAPPA * source / 6.0;
        let alpha = 3.5 * beta;
        let disc = theta0 * theta0 - 4.0 * alpha;
        if !(theta0 > 0.0 && alpha > 0.0 && disc > 0.0) {
            return Err(format!(
                "exp2: need theta0 > 0, alpha > 0, D > 0 (theta0 = {}, alpha = {}, D = {})",
                fmt17(theta0),
                fmt17(alpha),
                fmt17(disc)
            ));
        }
        let root = disc.sqrt();
        Ok(Self {
            theta0,
            beta,
            alpha,
            disc,
            root_near: -2.0 / (theta0 + root),
            root_far: -(theta0 + root) / (2.0 * alpha),
        })
    }

    pub fn volume(&self, t: f64) -> f64 {
        self.alpha * (t - self.root_near) * (t - self.root_far)
    }

    /// J(t) = int_0^t dt' / V(t').
    pub fn j_integral(&self, t: f64) -> f64 {
        (log1p(-t / self.root_near) - log1p(-t / self.root_far)) / self.disc.sqrt()
    }

    pub fn hubble(&self, h0: f64, t: f64) -> f64 {
        (h0 + self.beta * t) / self.volume(t)
    }

    pub fn ln_scale(&self, h0: f64, t: f64) -> f64 {
        log(self.volume(t)) / 7.0 + (h0 - self.theta0 / 7.0) * self.j_integral(t)
    }

    /// Inverse of nu = ln V(t) on the branch t > t_s.
    pub fn time_at_ln_volume(&self, nu: f64) -> f64 {
        2.0 * expm1(nu) / (self.theta0 + (self.disc + 4.0 * self.alpha * exp(nu)).sqrt())
    }

    /// Kasner exponent lim_{t -> t_s} H_i / Theta.
    pub fn kasner(&self, h0: f64) -> f64 {
        (h0 + self.beta * self.root_near) / self.disc.sqrt()
    }
}

/// Everything derived from one state vector.
#[derive(Clone, Copy, Debug)]
struct Fields {
    volume: f64,
    theta: f64,
    s_mode: f64,
    big_s: f64,
    m_eff: f64,
    energy_mode: f64,
    rho: f64,
    p: f64,
    w: f64,
    ke_l: f64,
    pe_l: f64,
    ke_h: f64,
    pe_h: f64,
    residual: f64,
    relative: f64,
    bound: f64,
    w_eff: f64,
    norm_hilbert: f64,
    norm_krein: f64,
}

/// `density` = S_0 V_0 (the mode density is density / V).
fn fields(alg: &Algebra, density: f64, lambda: f64, state: &[f64]) -> Fields {
    let (hb, ha, hc) = (state[3], state[4], state[5]);
    let volume = exp(state[0] + 3.0 * state[1] + 3.0 * state[2]);
    let theta = hb + 3.0 * ha + 3.0 * hc;
    let u = CVec16::from_state(&state[GRAVITY_REALS..]);
    let n = density / volume;
    let s_mode = scalar_density(alg, &u);
    let big_s = n * s_mode;
    let m_eff = MASS + lambda * big_s;
    let h = alg.mode_hamiltonian(m_eff, &[0.0; 8]);
    let energy_mode = mode_energy(&h, &u);
    let lagrangian = 0.5 * lambda * big_s * big_s; // S U' - U
    let mut gradient = 0.0;
    for &j in &TRANSVERSE {
        gradient += mode_pressure(alg, &u, 0.0, j);
    }
    let rho = n * energy_mode - lagrangian;
    let p = n * gradient / 7.0 + lagrangian;
    let ke_l = 0.5 * n * energy_mode;
    let pe_l = rho - ke_l;
    let ke_h = n * gradient;
    let pe_h = MASS * big_s + 0.5 * lambda * big_s * big_s;
    let residual = pair_sum(hb, ha, hc) - KAPPA * rho;
    let relative = residual.abs() / (pair_abs_sum(hb, ha, hc) + KAPPA * rho.abs());
    let w = p / rho;
    Fields {
        volume,
        theta,
        s_mode,
        big_s,
        m_eff,
        energy_mode,
        rho,
        p,
        w,
        ke_l,
        pe_l,
        ke_h,
        pe_h,
        residual,
        relative,
        bound: theta * theta - 3.0 * ha * ha - 2.0 * KAPPA * rho,
        w_eff: -1.0 + theta * (1.0 + w) / (3.0 * ha),
        norm_hilbert: norm_hilbert(&u),
        norm_krein: norm_krein(alg, &u),
    }
}

fn rhs_for(alg: &Algebra, density: f64, lambda: f64) -> RhsFn {
    let alg = alg.clone();
    Box::new(move |_t, y, ydot| {
        let f = fields(&alg, density, lambda, y);
        let source = KAPPA * (f.rho - f.p) / 6.0;
        for group in 0..3 {
            ydot[group] = y[3 + group];
            ydot[3 + group] = -y[3 + group] * f.theta + source;
        }
        let h = alg.mode_hamiltonian(f.m_eff, &[0.0; 8]);
        mode_rhs(&h, &y[GRAVITY_REALS..], &mut ydot[GRAVITY_REALS..]);
        Ok(())
    })
}

/// "0" -> "0", "-0.4" -> "m0p4", "0.5" -> "0p5".
fn label_number(value: f64) -> String {
    let text = if value == value.trunc() {
        format!("{}", value as i64)
    } else {
        format!("{value}")
    };
    text.replace('.', "p").replace('-', "m")
}

#[derive(Clone, Debug)]
struct RunSpec {
    id: String,
    x0: f64,
    /// S_0 (condensate density at V_0 = 1).
    s0_density: f64,
    lambda: f64,
    /// s(u(0)).
    s0: f64,
    m_eff0: f64,
    rho0: f64,
    c0: f64,
    relative0: f64,
    eigen_residual: f64,
    krein0: f64,
    u0: CVec16,
    background: Background,
}

fn initial_spinor(alg: &Algebra, m_eff: f64) -> Result<(CVec16, f64), String> {
    if m_eff <= 0.0 {
        return Err(format!(
            "exp2: M_eff(0) = {} must be positive",
            fmt17(m_eff)
        ));
    }
    let h = alg.mode_hamiltonian(m_eff, &[0.0; 8]);
    let projector = energy_projector(&h, m_eff, 1.0).mul(&involution_projector(&alg.b, 1.0));
    let u0 = *range_basis(&projector, 1.0e-8)
        .first()
        .ok_or_else(|| "exp2: empty (h = +M, B = +1) eigenspace".to_string())?;
    let residual = h
        .apply(&u0)
        .max_abs_diff(&u0.scale(m_eff, 0.0))
        .max(alg.b.apply(&u0).max_abs_diff(&u0));
    Ok((u0, residual))
}

fn build_run(alg: &Algebra, x0: f64) -> Result<RunSpec, String> {
    let c0 = pair_sum(HUBBLE_B0, HUBBLE_A0, HUBBLE_C0);
    // The rest eigenvector does not depend on M_eff > 0 (gamma^4 u = i u);
    // take it at M = m, then solve the constraint for S_0.
    let (u_probe, _) = initial_spinor(alg, MASS)?;
    let s0 = scalar_density(alg, &u_probe);
    let s0_density = c0 / (KAPPA * MASS * s0 * (1.0 + x0 * s0));
    let lambda = 2.0 * MASS * x0 / s0_density;
    let m_eff0 = MASS + lambda * s0_density * s0;
    let (u0, eigen_residual) = initial_spinor(alg, m_eff0)?;
    let s0 = scalar_density(alg, &u0);
    let mut y0 = vec![0.0; STATE_LEN];
    y0[3] = HUBBLE_B0;
    y0[4] = HUBBLE_A0;
    y0[5] = HUBBLE_C0;
    u0.write_state(&mut y0[GRAVITY_REALS..]);
    let f0 = fields(alg, s0_density, lambda, &y0);
    let theta0 = HUBBLE_B0 + 3.0 * HUBBLE_A0 + 3.0 * HUBBLE_C0;
    let background = Background::new(theta0, MASS * s0_density * s0)?;
    Ok(RunSpec {
        id: format!("x0_{}", label_number(x0)),
        x0,
        s0_density,
        lambda,
        s0,
        m_eff0: f0.m_eff,
        rho0: f0.rho,
        c0,
        relative0: f0.relative,
        eigen_residual,
        krein0: f0.norm_krein,
        u0,
        background,
    })
}

fn initial_state(spec: &RunSpec) -> Vec<f64> {
    let mut y0 = vec![0.0; STATE_LEN];
    y0[3] = HUBBLE_B0;
    y0[4] = HUBBLE_A0;
    y0[5] = HUBBLE_C0;
    spec.u0.write_state(&mut y0[GRAVITY_REALS..]);
    y0
}

fn header() -> Vec<String> {
    let mut header: Vec<String> = ["t", "ln_b", "ln_a", "ln_c", "H_b", "H_a", "H_c"]
        .iter()
        .map(|s| s.to_string())
        .collect();
    header.extend((0..16).map(|i| format!("u_re_{i}")));
    header.extend((0..16).map(|i| format!("u_im_{i}")));
    for name in [
        "V",
        "Theta",
        "s_u",
        "S",
        "M_eff",
        "energy_mode",
        "rho",
        "p",
        "w",
        "KE_L",
        "PE_L",
        "KE_H",
        "PE_H",
        "constraint_residual",
        "constraint_relative",
        "bound",
        "w_eff",
        "norm_hilbert",
        "norm_krein",
    ] {
        header.push(name.to_string());
    }
    header
}

#[derive(Clone, Debug, Default)]
struct Measures {
    max_relative: f64,
    max_s_drift: f64,
    max_hilbert_drift: f64,
    max_krein_drift: f64,
    max_anisotropy_drift: f64,
    min_bound: f64,
    max_identity_defect: f64,
    max_exact_volume: f64,
    max_exact_hubble: f64,
    max_exact_ln_scale: f64,
    max_exact_spinor: f64,
    max_spinor_shape: f64,
    max_spinor_phase: f64,
    max_m_eff_forward: f64,
    max_m_eff_backward: f64,
    /// on rows with rho > 0 and H_a > 0
    min_theta_over_3ha: f64,
    min_w_eff_positive_energy: f64,
    /// rows with KE_L < 0, w < -1 (rho > 0), rho < 0
    negative_kinetic_rows: i64,
    phantom_rows: i64,
    negative_energy_rows: i64,
    phantom_iff_negative_kinetic: bool,
    phantom_volume_range: (f64, f64),
    negative_energy_volume_max: f64,
    min_rho: f64,
}

struct RunOutcome {
    spec: RunSpec,
    file: String,
    forward: Integration,
    backward: Integration,
    rows: Vec<Vec<f64>>,
    measures: Measures,
    /// final (t_end) values
    t_end: f64,
    t_back: f64,
    final_anisotropy: f64,
    final_ht: [f64; 3],
    final_w: f64,
    final_w_eff: f64,
    hc_crossing: f64,
    /// H_i / Theta at the backward end (V = e^-7)
    kasner_end: [f64; 3],
    /// extrapolated to V = 0
    kasner_measured: [f64; 3],
    kasner_sum_squares_measured: f64,
    backward_volume: f64,
    /// max|M_eff| N_steps ulp(|t_end|)/2 summed over both branches
    phase_bound: f64,
}

fn execute(
    alg: &Algebra,
    spec: RunSpec,
    tolerances: &Tolerances,
) -> Result<(RunOutcome, &'static str), String> {
    let bg = spec.background;
    let forward_targets: Vec<f64> = (1..=FORWARD_INTERVALS)
        .map(|k| bg.time_at_ln_volume(LN_VOLUME_STEP * k as f64))
        .collect();
    let backward_targets: Vec<f64> = (1..=BACKWARD_INTERVALS)
        .map(|k| bg.time_at_ln_volume(-LN_VOLUME_STEP * k as f64))
        .collect();
    let t_end = forward_targets[FORWARD_INTERVALS - 1];
    let t_back = backward_targets[BACKWARD_INTERVALS - 1];
    let cfg_forward = SolverConfig::adams(tolerances.rtol, tolerances.atol, tolerances.max_step)
        .with_stop_time(t_end);
    let cfg_backward = SolverConfig::adams(tolerances.rtol, tolerances.atol, tolerances.max_step)
        .with_stop_time(t_back);
    let density = spec.s0_density;
    let forward = integrate(
        initial_state(&spec),
        0.0,
        &forward_targets,
        rhs_for(alg, density, spec.lambda),
        &cfg_forward,
    )
    .map_err(|error| format!("run {} forward: {error}", spec.id))?;
    let backward = integrate_backward(
        initial_state(&spec),
        0.0,
        &backward_targets,
        rhs_for(alg, density, spec.lambda),
        &cfg_backward,
    )
    .map_err(|error| format!("run {} backward: {error}", spec.id))?;

    // ascending time: backward branch reversed (without t = 0), then forward
    let mut samples: Vec<(f64, &Vec<f64>)> = Vec::new();
    for index in (1..backward.times.len()).rev() {
        samples.push((backward.times[index], &backward.states[index]));
    }
    for (t, state) in forward.times.iter().zip(&forward.states) {
        samples.push((*t, state));
    }

    let h0 = [HUBBLE_B0, HUBBLE_A0, HUBBLE_C0];
    let differences = [(1usize, 0usize), (2, 0), (1, 2)];
    let max_initial_difference = differences
        .iter()
        .map(|&(i, j)| (h0[i] - h0[j]).abs())
        .fold(0.0f64, f64::max);
    let mut m = Measures {
        min_bound: f64::INFINITY,
        min_theta_over_3ha: f64::INFINITY,
        min_w_eff_positive_energy: f64::INFINITY,
        phantom_iff_negative_kinetic: true,
        phantom_volume_range: (f64::INFINITY, f64::NEG_INFINITY),
        min_rho: f64::INFINITY,
        ..Measures::default()
    };
    let mut rows = Vec::with_capacity(samples.len());
    let mut hc_crossing = f64::NAN;
    let mut previous: Option<(f64, f64)> = None;
    for (t, state) in &samples {
        let t = *t;
        let f = fields(alg, density, spec.lambda, state);
        let (hb, ha, hc) = (state[3], state[4], state[5]);
        m.max_relative = m.max_relative.max(f.relative);
        m.max_s_drift = m.max_s_drift.max((f.s_mode - spec.s0).abs());
        m.max_hilbert_drift = m.max_hilbert_drift.max((f.norm_hilbert - 1.0).abs());
        m.max_krein_drift = m.max_krein_drift.max((f.norm_krein - spec.krein0).abs());
        for &(i, j) in &differences {
            let drift = ((state[3 + i] - state[3 + j]) * f.volume - (h0[i] - h0[j])).abs();
            m.max_anisotropy_drift = m.max_anisotropy_drift.max(drift / max_initial_difference);
        }
        m.min_bound = m.min_bound.min(f.bound);
        let identity = hb * hb + 3.0 * hc * hc + 2.0 * f.residual;
        m.max_identity_defect = m
            .max_identity_defect
            .max((f.bound - identity).abs() / (f.theta * f.theta));
        // exact solution
        let amplification = 1.0 + bg.root_near.abs() / (t - bg.root_near);
        let v_exact = bg.volume(t);
        m.max_exact_volume = m
            .max_exact_volume
            .max((f.volume / v_exact - 1.0).abs() / amplification);
        let rates_exact = [
            bg.hubble(HUBBLE_B0, t),
            bg.hubble(HUBBLE_A0, t),
            bg.hubble(HUBBLE_C0, t),
        ];
        // sum over the 7 directions of |H_i|
        let scale = rates_exact[0].abs() + 3.0 * rates_exact[1].abs() + 3.0 * rates_exact[2].abs();
        for group in 0..3 {
            m.max_exact_hubble = m
                .max_exact_hubble
                .max((state[3 + group] - rates_exact[group]).abs() / scale / amplification);
            let ln_exact = bg.ln_scale(h0[group], t);
            m.max_exact_ln_scale = m
                .max_exact_ln_scale
                .max((state[group] - ln_exact).abs() / (1.0 + ln_exact.abs()) / amplification);
        }
        let phase = MASS * t + spec.lambda * spec.s0_density * spec.s0 * bg.j_integral(t);
        let (cos_phase, sin_phase) = (cos(phase), sin(phase));
        let u_exact = spec.u0.scale(cos_phase, -sin_phase);
        let u = CVec16::from_state(&state[GRAVITY_REALS..]);
        m.max_exact_spinor = m.max_exact_spinor.max(u.distance(&u_exact));
        let (z_re, z_im) = spec.u0.dot(&u);
        let shape = u.distance(&spec.u0.scale(z_re, z_im))
            + ((z_re * z_re + z_im * z_im).sqrt() - 1.0).abs();
        m.max_spinor_shape = m.max_spinor_shape.max(shape);
        // arg(z e^{i phi}) for z e^{i phi} = 1 + O(1e-7)
        let rotated_re = z_re * cos_phase - z_im * sin_phase;
        let rotated_im = z_re * sin_phase + z_im * cos_phase;
        let phase_error = if rotated_re > 0.0 {
            atan(rotated_im / rotated_re).abs()
        } else {
            std::f64::consts::PI
        };
        m.max_spinor_phase = m.max_spinor_phase.max(phase_error);
        if t >= 0.0 {
            m.max_m_eff_forward = m.max_m_eff_forward.max(f.m_eff.abs());
        } else {
            m.max_m_eff_backward = m.max_m_eff_backward.max(f.m_eff.abs());
        }
        // sign structure
        if f.rho > 0.0 && ha > 0.0 {
            m.min_theta_over_3ha = m.min_theta_over_3ha.min(f.theta / (3.0 * ha));
            m.min_w_eff_positive_energy = m.min_w_eff_positive_energy.min(f.w_eff);
        }
        if f.ke_l < 0.0 {
            m.negative_kinetic_rows += 1;
        }
        if f.rho < 0.0 {
            m.negative_energy_rows += 1;
            m.negative_energy_volume_max = m.negative_energy_volume_max.max(f.volume);
        } else {
            let phantom = f.w < -1.0;
            if phantom {
                m.phantom_rows += 1;
                m.phantom_volume_range.0 = m.phantom_volume_range.0.min(f.volume);
                m.phantom_volume_range.1 = m.phantom_volume_range.1.max(f.volume);
            }
            if phantom != (f.ke_l < 0.0) {
                m.phantom_iff_negative_kinetic = false;
            }
        }
        m.min_rho = m.min_rho.min(f.rho);
        if let Some((t_prev, hc_prev)) = previous {
            if hc_prev < 0.0 && hc >= 0.0 && hc_crossing.is_nan() {
                hc_crossing = t_prev + (t - t_prev) * (-hc_prev) / (hc - hc_prev);
            }
        }
        previous = Some((t, hc));

        let mut row = vec![t];
        row.extend_from_slice(state);
        row.extend([
            f.volume,
            f.theta,
            f.s_mode,
            f.big_s,
            f.m_eff,
            f.energy_mode,
            f.rho,
            f.p,
            f.w,
            f.ke_l,
            f.pe_l,
            f.ke_h,
            f.pe_h,
            f.residual,
            f.relative,
            f.bound,
            f.w_eff,
            f.norm_hilbert,
            f.norm_krein,
        ]);
        rows.push(row);
    }
    if m.phantom_rows == 0 {
        m.phantom_volume_range = (f64::NAN, f64::NAN);
    }
    let last = &forward.states[forward.states.len() - 1];
    let f_end = fields(alg, density, spec.lambda, last);
    let (hb, ha, hc) = (last[3], last[4], last[5]);
    let spread = (ha - hb).abs().max((ha - hc).abs()).max((hb - hc).abs());
    // Kasner exponents: H_i / Theta at the three smallest volumes,
    // extrapolated quadratically in V to V = 0 (H_i/Theta is analytic in V
    // at the singularity; the extrapolation error is O(V^3) ~ 1e-9).
    let count = backward.states.len();
    let first = &backward.states[count - 1];
    let f_back = fields(alg, density, spec.lambda, first);
    let mut nodes = [(0.0f64, [0.0f64; 3]); 3];
    for (slot, node) in nodes.iter_mut().enumerate() {
        let state = &backward.states[count - 1 - slot];
        let f = fields(alg, density, spec.lambda, state);
        *node = (
            f.volume,
            [state[3] / f.theta, state[4] / f.theta, state[5] / f.theta],
        );
    }
    let kasner_end = nodes[0].1;
    let mut kasner_measured = [0.0f64; 3];
    for (k, &(vk, ref rk)) in nodes.iter().enumerate() {
        let mut weight = 1.0;
        for (j, &(vj, _)) in nodes.iter().enumerate() {
            if j != k {
                weight *= (0.0 - vj) / (vk - vj);
            }
        }
        for group in 0..3 {
            kasner_measured[group] += weight * rk[group];
        }
    }
    let kasner_sum_squares_measured = kasner_measured[0] * kasner_measured[0]
        + 3.0 * kasner_measured[1] * kasner_measured[1]
        + 3.0 * kasner_measured[2] * kasner_measured[2];
    let phase_bound = m.max_m_eff_forward * forward.steps as f64 * ulp(t_end) / 2.0
        + m.max_m_eff_backward * backward.steps as f64 * ulp(t_back) / 2.0;
    let file = format!("run_{}.csv", spec.id);
    let outcome = RunOutcome {
        phase_bound,
        file,
        t_end,
        t_back,
        final_anisotropy: 7.0 * spread / f_end.theta,
        final_ht: [hb * t_end, ha * t_end, hc * t_end],
        final_w: f_end.w,
        final_w_eff: f_end.w_eff,
        hc_crossing,
        kasner_end,
        kasner_measured,
        kasner_sum_squares_measured,
        backward_volume: f_back.volume,
        spec,
        forward,
        backward,
        rows,
        measures: m,
    };
    Ok((outcome, cfg_forward.describe()))
}

/// Spacing of the doubles at |x| (unit in the last place).
fn ulp(x: f64) -> f64 {
    let magnitude = x.abs();
    f64::from_bits(magnitude.to_bits() + 1) - magnitude
}

fn solver_json(run: &Integration) -> Json {
    Json::object(vec![
        ("steps", Json::Int(run.steps)),
        ("rhsEvals", Json::Int(run.rhs_evals)),
        ("errTestFails", Json::Int(run.err_test_fails)),
        ("nonlinIters", Json::Int(run.nonlin_iters)),
        ("nonlinConvFails", Json::Int(run.nonlin_conv_fails)),
        ("lastOrder", Json::Int(run.last_order as i64)),
        ("lastStep", Json::Float(run.last_step)),
    ])
}

/// Predicted sum of squared Kasner exponents 1 - 2 kappa m x0 S_0 s0^2 / D.
fn kasner_sum_squares_predicted(spec: &RunSpec) -> f64 {
    1.0 - 2.0 * KAPPA * MASS * spec.x0 * spec.s0_density * spec.s0 * spec.s0 / spec.background.disc
}

fn run_json(o: &RunOutcome) -> Json {
    let s = &o.spec;
    let bg = &s.background;
    let m = &o.measures;
    Json::object(vec![
        ("id", Json::str(&s.id)),
        ("file", Json::str(&o.file)),
        ("x0", Json::Float(s.x0)),
        ("S0", Json::Float(s.s0_density)),
        ("lambda", Json::Float(s.lambda)),
        ("scalarDensity0", Json::Float(s.s0)),
        ("mEff0", Json::Float(s.m_eff0)),
        ("rho0", Json::Float(s.rho0)),
        ("constraintLhs0", Json::Float(s.c0)),
        ("constraintRelative0", Json::Float(s.relative0)),
        ("initialEigenResidual", Json::Float(s.eigen_residual)),
        ("kreinNorm0", Json::Float(s.krein0)),
        (
            "exact",
            Json::object(vec![
                ("theta0", Json::Float(bg.theta0)),
                ("alpha", Json::Float(bg.alpha)),
                ("beta", Json::Float(bg.beta)),
                ("discriminant", Json::Float(bg.disc)),
                ("singularityTime", Json::Float(bg.root_near)),
                ("farRoot", Json::Float(bg.root_far)),
                (
                    "kasnerExponents",
                    Json::floats(&[
                        bg.kasner(HUBBLE_B0),
                        bg.kasner(HUBBLE_A0),
                        bg.kasner(HUBBLE_C0),
                    ]),
                ),
                (
                    "kasnerSumSquares",
                    Json::Float(kasner_sum_squares_predicted(s)),
                ),
                ("extraTimeTurnTime", Json::Float(-HUBBLE_C0 / bg.beta)),
                ("mEffZeroVolume", Json::Float(-2.0 * s.x0 * s.s0)),
                ("rhoZeroVolume", Json::Float(-s.x0 * s.s0)),
            ]),
        ),
        (
            "grid",
            Json::object(vec![
                ("tBack", Json::Float(o.t_back)),
                ("tEnd", Json::Float(o.t_end)),
                ("volumeBack", Json::Float(o.backward_volume)),
                ("rows", Json::Int(o.rows.len() as i64)),
            ]),
        ),
        (
            "measurements",
            Json::object(vec![
                ("maxConstraintRelative", Json::Float(m.max_relative)),
                ("maxScalarDensityDrift", Json::Float(m.max_s_drift)),
                ("maxHilbertNormDrift", Json::Float(m.max_hilbert_drift)),
                ("maxKreinNormDrift", Json::Float(m.max_krein_drift)),
                (
                    "maxAnisotropyVolumeDrift",
                    Json::Float(m.max_anisotropy_drift),
                ),
                ("minBound", Json::Float(m.min_bound)),
                ("maxBoundIdentityDefect", Json::Float(m.max_identity_defect)),
                ("maxExactVolumeError", Json::Float(m.max_exact_volume)),
                ("maxExactHubbleError", Json::Float(m.max_exact_hubble)),
                ("maxExactLnScaleError", Json::Float(m.max_exact_ln_scale)),
                ("maxExactSpinorError", Json::Float(m.max_exact_spinor)),
                ("maxSpinorShapeError", Json::Float(m.max_spinor_shape)),
                ("maxSpinorPhaseError", Json::Float(m.max_spinor_phase)),
                ("spinorPhaseRoundingBound", Json::Float(o.phase_bound)),
                (
                    "minThetaOver3HaPositiveEnergy",
                    Json::Float(m.min_theta_over_3ha),
                ),
                (
                    "minWeffPositiveEnergy",
                    Json::Float(m.min_w_eff_positive_energy),
                ),
                ("negativeKineticRows", Json::Int(m.negative_kinetic_rows)),
                ("phantomRows", Json::Int(m.phantom_rows)),
                ("phantomVolumeMin", Json::Float(m.phantom_volume_range.0)),
                ("phantomVolumeMax", Json::Float(m.phantom_volume_range.1)),
                ("negativeEnergyRows", Json::Int(m.negative_energy_rows)),
                (
                    "negativeEnergyVolumeMax",
                    Json::Float(m.negative_energy_volume_max),
                ),
                ("minRho", Json::Float(m.min_rho)),
                ("finalAnisotropy", Json::Float(o.final_anisotropy)),
                ("finalHubbleTimesT", Json::floats(&o.final_ht)),
                ("finalW", Json::Float(o.final_w)),
                ("finalWeff", Json::Float(o.final_w_eff)),
                ("extraTimeTurnTimeMeasured", Json::Float(o.hc_crossing)),
                ("kasnerAtBackwardEnd", Json::floats(&o.kasner_end)),
                ("kasnerExtrapolated", Json::floats(&o.kasner_measured)),
                (
                    "kasnerSumSquaresExtrapolated",
                    Json::Float(o.kasner_sum_squares_measured),
                ),
            ]),
        ),
        (
            "solver",
            Json::object(vec![
                ("forward", solver_json(&o.forward)),
                ("backward", solver_json(&o.backward)),
            ]),
        ),
    ])
}

/// Configuration lines (for a `print-config` listing).
pub fn config_lines() -> Vec<String> {
    vec![
        format!(
            "exp2: kappa_8 = {}, m = {}, H_b0 = {}, H_a0 = {}, H_c0 = {}, x0 = {:?}",
            fmt17(KAPPA),
            fmt17(MASS),
            fmt17(HUBBLE_B0),
            fmt17(HUBBLE_A0),
            fmt17(HUBBLE_C0),
            X0_VALUES
        ),
        format!(
            "exp2: output grid uniform in ln V, step {}, ln V in [-{}, {}]",
            fmt17(LN_VOLUME_STEP),
            fmt17(LN_VOLUME_STEP * BACKWARD_INTERVALS as f64),
            fmt17(LN_VOLUME_STEP * FORWARD_INTERVALS as f64)
        ),
        format!(
            "exp2: default rtol = {}, atol = {}, max_step = {}, method Adams + fixed point",
            fmt17(DEFAULT_TOLERANCES.rtol),
            fmt17(DEFAULT_TOLERANCES.atol),
            fmt17(DEFAULT_TOLERANCES.max_step)
        ),
    ]
}

/// Run EXP-2.
pub fn run(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let directory = ctx.experiment_dir(EXPERIMENT)?;
    let tolerances = ctx.tolerances(DEFAULT_TOLERANCES);
    let alg = Algebra::new();
    let mut summary = ExperimentSummary::new(EXPERIMENT);
    let mut outcomes = Vec::new();
    let mut solver = "";
    for &x0 in &X0_VALUES {
        let spec = build_run(&alg, x0)?;
        let (outcome, description) = execute(&alg, spec, &tolerances)?;
        solver = description;
        write_csv(&directory.join(&outcome.file), &header(), &outcome.rows)?;
        summary.add_file(&outcome.file);
        summary.add_stats(outcome.forward.steps, outcome.forward.rhs_evals);
        summary.add_stats(outcome.backward.steps, outcome.backward.rhs_evals);
        outcomes.push(outcome);
    }

    let fold = |f: &dyn Fn(&RunOutcome) -> f64| outcomes.iter().map(f).fold(0.0f64, f64::max);
    let eigen = fold(&|o| o.spec.eigen_residual.max((o.spec.s0 - 1.0).abs()));
    let relative0 = fold(&|o| o.spec.relative0);
    let constraint = fold(&|o| o.measures.max_relative);
    let s_drift = fold(&|o| o.measures.max_s_drift);
    let norm_drift = fold(&|o| o.measures.max_hilbert_drift.max(o.measures.max_krein_drift));
    let anisotropy = fold(&|o| o.measures.max_anisotropy_drift);
    let min_bound = outcomes
        .iter()
        .map(|o| o.measures.min_bound)
        .fold(f64::INFINITY, f64::min);
    let identity = fold(&|o| o.measures.max_identity_defect);
    let exact = fold(&|o| {
        o.measures
            .max_exact_volume
            .max(o.measures.max_exact_hubble)
            .max(o.measures.max_exact_ln_scale)
    });
    let spinor_exact = fold(&|o| o.measures.max_exact_spinor);
    let spinor_shape = fold(&|o| o.measures.max_spinor_shape);
    let spinor_phase_ok = outcomes
        .iter()
        .all(|o| o.measures.max_spinor_phase <= o.phase_bound + PHASE_TRUNCATION_ALLOWANCE);
    let spinor_phase = fold(&|o| o.measures.max_spinor_phase);
    let phase_bound = fold(&|o| o.phase_bound);
    let late = fold(&|o| {
        let ht = o
            .final_ht
            .iter()
            .map(|v| (3.5 * v - 1.0).abs())
            .fold(0.0f64, f64::max);
        o.final_anisotropy
            .max(ht)
            .max(o.final_w.abs())
            .max((o.final_w_eff - 4.0 / 3.0).abs())
    });
    let kasner = fold(&|o| {
        let bg = &o.spec.background;
        let predicted = [
            bg.kasner(HUBBLE_B0),
            bg.kasner(HUBBLE_A0),
            bg.kasner(HUBBLE_C0),
        ];
        (0..3)
            .map(|g| (o.kasner_measured[g] - predicted[g]).abs())
            .fold(0.0f64, f64::max)
            .max(
                (o.kasner_sum_squares_measured - kasner_sum_squares_predicted(&o.spec)).abs()
                    / kasner_sum_squares_predicted(&o.spec),
            )
    });
    let turn_ok = outcomes.iter().all(|o| {
        let first = &o.forward.states[0];
        let last = &o.forward.states[o.forward.states.len() - 1];
        let predicted = -HUBBLE_C0 / o.spec.background.beta;
        first[5] < 0.0 && last[5] > 0.0 && (o.hc_crossing - predicted).abs() <= 1.0e-2 * predicted
    });
    let theta_ratio_min = outcomes
        .iter()
        .map(|o| o.measures.min_theta_over_3ha)
        .fold(f64::INFINITY, f64::min);
    let dust = outcomes
        .iter()
        .find(|o| o.spec.x0 == 0.0)
        .ok_or_else(|| "exp2: no dust run".to_string())?;
    let dust_w_eff_min = dust.measures.min_w_eff_positive_energy;
    let dust_bound = -1.0 + 1.0 / 3.0f64.sqrt();
    let attractive = outcomes
        .iter()
        .find(|o| o.spec.x0 < 0.0)
        .ok_or_else(|| "exp2: no attractive run".to_string())?;
    let phantom_ok = outcomes
        .iter()
        .all(|o| o.measures.phantom_iff_negative_kinetic)
        && attractive.measures.phantom_rows > 0
        && outcomes
            .iter()
            .filter(|o| o.spec.x0 >= 0.0)
            .all(|o| o.measures.phantom_rows == 0 && o.measures.negative_energy_rows == 0);

    summary.check(
        "initial_positive_energy_rest_eigenvector",
        eigen <= EIGEN_LIMIT,
        &format!(
            "max |h u0 - M u0|, |B u0 - u0|, |s(u0) - 1| = {}",
            fmt17(eigen)
        ),
    );
    summary.check(
        "initial_constraint_solved",
        relative0 <= INITIAL_CONSTRAINT_LIMIT,
        &format!("max relative residual at t = 0: {}", fmt17(relative0)),
    );
    summary.check(
        "constraint_preserved",
        constraint <= CONSTRAINT_LIMIT,
        &format!(
            "max |sum H_iH_j - kappa rho| / (sum |H_iH_j| + kappa |rho|) = {} (limit {})",
            fmt17(constraint),
            fmt17(CONSTRAINT_LIMIT)
        ),
    );
    summary.check(
        "S_times_V_constant",
        s_drift <= CONSERVATION_LIMIT,
        &format!(
            "max |s(u) - s(u0)| = max |S V/(S_0 V_0) - s0| = {}",
            fmt17(s_drift)
        ),
    );
    summary.check(
        "spinor_norms_conserved",
        norm_drift <= CONSERVATION_LIMIT,
        &format!("max |u^dag u - 1|, |u^dag B u - 1| = {}", fmt17(norm_drift)),
    );
    summary.check(
        "anisotropy_times_volume_constant",
        anisotropy <= CONSERVATION_LIMIT,
        &format!(
            "max |(H_i - H_j) V - (H_i0 - H_j0)| / max|H_i0 - H_j0| = {}",
            fmt17(anisotropy)
        ),
    );
    summary.check(
        "bound_nonnegative",
        min_bound >= 0.0 && identity <= IDENTITY_LIMIT,
        &format!(
            "min (Theta^2 - 3H_a^2 - 2 kappa rho) = {}, max |bound - (H_b^2 + 3H_c^2 + 2 res)|/Theta^2 = {}",
            fmt17(min_bound),
            fmt17(identity)
        ),
    );
    summary.check(
        "exact_solution",
        exact <= EXACT_LIMIT,
        &format!(
            "max relative error of V, H_i, ln h_i vs the closed form (per 1 + |t_s|/(t - t_s)) = {}",
            fmt17(exact)
        ),
    );
    summary.check(
        "spinor_exact_shape",
        spinor_shape <= CONSERVATION_LIMIT,
        &format!(
            "max |u - (u0^dag u) u0| + ||u0^dag u| - 1| = {} (u stays on the ray of u0)",
            fmt17(spinor_shape)
        ),
    );
    summary.check(
        "spinor_exact_phase_within_time_rounding",
        spinor_phase_ok,
        &format!(
            "max |arg(u0^dag u) + m t + lambda S_0 J(t)| = {} <= max|M_eff| N_steps ulp(t_end)/2 (max {}) + {}; total |u - u_exact| = {}",
            fmt17(spinor_phase),
            fmt17(phase_bound),
            fmt17(PHASE_TRUNCATION_ALLOWANCE),
            fmt17(spinor_exact)
        ),
    );
    summary.check(
        "late_time_isotropic_dust",
        late <= LATE_TIME_LIMIT,
        &format!(
            "at t_end: max of 7 max|H_i - H_j|/Theta, |7 H_i t/2 - 1|, |w|, |w_eff - 4/3| = {}",
            fmt17(late)
        ),
    );
    summary.check(
        "extra_times_turn_to_expansion",
        turn_ok,
        "H_c(0) < 0, H_c(t_end) > 0, crossing at -H_c0/beta within 1 %",
    );
    summary.check(
        "theta_exceeds_sqrt3_Ha_for_positive_energy",
        theta_ratio_min > 1.0 / 3.0f64.sqrt() && dust_w_eff_min > dust_bound,
        &format!(
            "min Theta/(3H_a) (rho > 0) = {}, dust min w_eff = {} > {}",
            fmt17(theta_ratio_min),
            fmt17(dust_w_eff_min),
            fmt17(dust_bound)
        ),
    );
    summary.check(
        "backward_kasner_exponents",
        kasner <= KASNER_LIMIT,
        &format!(
            "H_i/Theta extrapolated to V = 0: max |p_i - p_i,exact|, relative sum p_i^2 deviation = {}",
            fmt17(kasner)
        ),
    );
    summary.check(
        "phantom_iff_negative_kinetic_energy",
        phantom_ok,
        &format!(
            "w < -1 <=> KE_L < 0 on rho > 0 rows; x0 = {}: {} phantom rows for V/V0 in [{}, {}], {} rho < 0 rows",
            fmt17(attractive.spec.x0),
            attractive.measures.phantom_rows,
            fmt17(attractive.measures.phantom_volume_range.0),
            fmt17(attractive.measures.phantom_volume_range.1),
            attractive.measures.negative_energy_rows
        ),
    );

    let extra = vec![
        (
            "parameters",
            Json::object(vec![
                ("kappa", Json::Float(KAPPA)),
                ("m", Json::Float(MASS)),
                ("hubbleB0", Json::Float(HUBBLE_B0)),
                ("hubbleA0", Json::Float(HUBBLE_A0)),
                ("hubbleC0", Json::Float(HUBBLE_C0)),
                ("x0Values", Json::floats(&X0_VALUES)),
                ("lnVolumeStep", Json::Float(LN_VOLUME_STEP)),
                ("backwardIntervals", Json::Int(BACKWARD_INTERVALS as i64)),
                ("forwardIntervals", Json::Int(FORWARD_INTERVALS as i64)),
                (
                    "lnVolumeMin",
                    Json::Float(-LN_VOLUME_STEP * BACKWARD_INTERVALS as f64),
                ),
                (
                    "lnVolumeMax",
                    Json::Float(LN_VOLUME_STEP * FORWARD_INTERVALS as f64),
                ),
                ("initialSpinor", Json::str("first vector of the (h = +M_eff, B = +1) eigenspace")),
            ]),
        ),
        (
            "stateLayout",
            Json::str(
                "ln_b, ln_a, ln_c, H_b, H_a, H_c, u_re_0..u_re_15, u_im_0..u_im_15 \
                 (u = re + i im in C^16); rows in increasing t (backward branch, t = 0, forward branch)",
            ),
        ),
        (
            "limits",
            Json::object(vec![
                ("eigen", Json::Float(EIGEN_LIMIT)),
                ("initialConstraint", Json::Float(INITIAL_CONSTRAINT_LIMIT)),
                ("constraint", Json::Float(CONSTRAINT_LIMIT)),
                ("conservation", Json::Float(CONSERVATION_LIMIT)),
                ("identity", Json::Float(IDENTITY_LIMIT)),
                ("exact", Json::Float(EXACT_LIMIT)),
                ("spinorShape", Json::Float(CONSERVATION_LIMIT)),
                ("phaseTruncationAllowance", Json::Float(PHASE_TRUNCATION_ALLOWANCE)),
                ("lateTime", Json::Float(LATE_TIME_LIMIT)),
                ("kasner", Json::Float(KASNER_LIMIT)),
            ]),
        ),
        ("runs", Json::Array(outcomes.iter().map(run_json).collect())),
        (
            "measurements",
            Json::object(vec![
                ("maxInitialEigenResidual", Json::Float(eigen)),
                ("maxInitialConstraintRelative", Json::Float(relative0)),
                ("maxConstraintRelative", Json::Float(constraint)),
                ("maxScalarDensityDrift", Json::Float(s_drift)),
                ("maxNormDrift", Json::Float(norm_drift)),
                ("maxAnisotropyVolumeDrift", Json::Float(anisotropy)),
                ("minBound", Json::Float(min_bound)),
                ("maxBoundIdentityDefect", Json::Float(identity)),
                ("maxExactError", Json::Float(exact)),
                ("maxSpinorExactError", Json::Float(spinor_exact)),
                ("maxSpinorShapeError", Json::Float(spinor_shape)),
                ("maxSpinorPhaseError", Json::Float(spinor_phase)),
                ("maxSpinorPhaseRoundingBound", Json::Float(phase_bound)),
                ("maxLateTimeDeviation", Json::Float(late)),
                ("maxKasnerDeviation", Json::Float(kasner)),
                ("minThetaOver3HaPositiveEnergy", Json::Float(theta_ratio_min)),
                ("dustMinWeff", Json::Float(dust_w_eff_min)),
            ]),
        ),
        (
            "notes",
            Json::Array(vec![
                Json::str(
                    "rho - p = m S is lambda-independent, so the three runs differ only through S_0 \
                     (fixed by the constraint); V(t) is exactly quadratic and H_i V exactly linear in t.",
                ),
                Json::str(
                    "Backward, every run reaches a Kasner-type singularity V -> 0 at t_s = r_+; the \
                     lambda S^2/2 term is a stiff (w = 1) component there, so sum p_i^2 = 1 - 2 kappa m \
                     x0 S_0 / D differs from the vacuum value 1 unless x0 = 0.",
                ),
                Json::str(
                    "x0 = -0.4: M_eff = m (1 + 2 x0 V0/V) < 0 for V < 0.8 V0 (KE_L < 0, phantom w < -1 \
                     while rho > 0) and rho < 0 for V < 0.4 V0, where Theta > sqrt(3) H_a no longer \
                     follows from the bound (the bound itself, = H_b^2 + 3H_c^2, stays >= 0).",
                ),
                Json::str(
                    "The spinor stays the gamma^4 = +i eigenvector, u(t) = exp(-i int M_eff) u0, so \
                     s(u) = 1 and S V = S_0 V_0 are exact; the output grid does not resolve the spinor \
                     phase at late times (it is uniform in ln V).",
                ),
                Json::str(
                    "The spinor phase error (~2e-7 at t ~ 1e4) is the rounding of CVODE's internal time \
                     t_n += h with the capped constant step h = max_step (a fixed e_k per step in each \
                     binade [2^k, 2^(k+1)) of t_n), not truncation: it stays below max|M_eff| N_steps \
                     ulp(t_end)/2 and does not shrink under --refined; the phase-invariant spinor \
                     shape error (2e-10) does.",
                ),
            ]),
        ),
    ];
    let doc = standard_summary(ctx, &summary, &tolerances, solver, extra);
    write_json(&directory.join("summary.json"), &doc)?;
    summary.add_file("summary.json");
    Ok(summary)
}

#[cfg(test)]
mod tests {
    use super::*;

    /// The 7 transverse Hubble rates from the group rates in state[3..6].
    fn group_rates(state: &[f64]) -> [f64; 7] {
        let mut rates = [0.0; 7];
        for (slot, rate) in rates.iter_mut().enumerate() {
            *rate = state[3 + GROUP_OF[slot]];
        }
        rates
    }

    #[test]
    fn grouped_pair_sum_equals_seven_direction_sum() {
        for (hb, ha, hc) in [(0.0, 1.0, -0.2), (0.3, -0.7, 1.1), (2.0, 0.5, 0.25)] {
            let rates = group_rates(&[0.0, 0.0, 0.0, hb, ha, hc]);
            let mut sum = 0.0;
            for i in 0..7 {
                for j in (i + 1)..7 {
                    sum += rates[i] * rates[j];
                }
            }
            assert!((sum - pair_sum(hb, ha, hc)).abs() < 1e-14);
        }
        assert!((pair_sum(HUBBLE_B0, HUBBLE_A0, HUBBLE_C0) - 1.32).abs() < 1e-15);
    }

    #[test]
    fn initial_data_satisfy_the_constraint() {
        let alg = Algebra::new();
        for &x0 in &X0_VALUES {
            let spec = build_run(&alg, x0).unwrap();
            assert!(spec.relative0 < 1e-15, "x0 = {x0}: {}", spec.relative0);
            assert!((spec.s0 - 1.0).abs() < 1e-14);
            assert!((spec.s0_density - 1.32 / (1.0 + x0)).abs() < 1e-14);
            assert!((spec.lambda * spec.s0_density - 2.0 * x0).abs() < 1e-15);
            assert!(spec.eigen_residual < 1e-13);
            assert!((spec.krein0 - 1.0).abs() < 1e-14);
        }
    }

    /// Five-point central difference.
    fn derivative(f: &dyn Fn(f64) -> f64, t: f64, h: f64) -> f64 {
        (f(t - 2.0 * h) - 8.0 * f(t - h) + 8.0 * f(t + h) - f(t + 2.0 * h)) / (12.0 * h)
    }

    #[test]
    fn closed_form_background_solves_the_equations() {
        let bg = Background::new(2.4, 1.32).unwrap();
        assert!((bg.volume(0.0) - 1.0).abs() < 1e-15);
        assert_eq!(bg.j_integral(0.0), 0.0);
        let h = 1e-3;
        for &t in &[-0.4, -0.1, 0.3, 2.0, 50.0] {
            // V' / V = Theta and H' = -H Theta + m S / 6 with S = S_0 / V
            let v = bg.volume(t);
            let dv = derivative(&|x| bg.volume(x), t, h);
            let theta: f64 = [HUBBLE_B0, HUBBLE_A0, HUBBLE_A0, HUBBLE_A0]
                .iter()
                .chain([HUBBLE_C0; 3].iter())
                .map(|&h0| bg.hubble(h0, t))
                .sum();
            assert!((dv / v - theta).abs() < 1e-9 * theta.abs());
            for &h0 in &[HUBBLE_B0, HUBBLE_A0, HUBBLE_C0] {
                let rate = bg.hubble(h0, t);
                let dh = derivative(&|x| bg.hubble(h0, x), t, h);
                let source = KAPPA * 1.32 / v / 6.0;
                let scale = (rate * theta).abs() + source;
                assert!((dh + rate * theta - source).abs() < 1e-6 * scale, "t = {t}");
                let dl = derivative(&|x| bg.ln_scale(h0, x), t, h);
                assert!((dl - rate).abs() < 1e-7 * theta.abs(), "t = {t}");
            }
        }
        for &nu in &[-7.0, -0.5, 0.0, 0.05, 3.0, 18.5] {
            let t = bg.time_at_ln_volume(nu);
            assert!((log(bg.volume(t)) - nu).abs() < 1e-12, "nu = {nu}");
        }
        // deep below the grid: still on the regular branch t > t_s
        let t = bg.time_at_ln_volume(-20.0);
        assert!(t > bg.root_near && (log(bg.volume(t)) + 20.0).abs() < 1e-5);
    }

    #[test]
    fn short_integration_matches_closed_form() {
        let alg = Algebra::new();
        let spec = build_run(&alg, 0.5).unwrap();
        let bg = spec.background;
        let targets: Vec<f64> = (1..=10).map(|k| 0.1 * k as f64).collect();
        let cfg = SolverConfig::adams(1e-12, 1e-15, 0.25).with_stop_time(1.0);
        let run = integrate(
            initial_state(&spec),
            0.0,
            &targets,
            rhs_for(&alg, spec.s0_density, spec.lambda),
            &cfg,
        )
        .unwrap();
        for (t, y) in run.times.iter().zip(&run.states) {
            let f = fields(&alg, spec.s0_density, spec.lambda, y);
            assert!((f.volume / bg.volume(*t) - 1.0).abs() < 1e-10);
            assert!((y[4] - bg.hubble(HUBBLE_A0, *t)).abs() < 1e-10);
            assert!(f.relative < 1e-11);
        }
    }
}
