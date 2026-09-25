//! EXP-3 -- 4D-effective late universe: the dirac16complex condensate as dark energy.
//!
//! Stabilised extra dimensions (b, c constant), units H0 = 1, densities in
//! units of 3 H0^2 / kappa_4, independent variable N = ln a (a = 1 today):
//!
//! ```text
//! E^2(N) = Omega_r a^-4 + Omega_m a^-3 + rho_psi,
//! rho_psi = A sigma (1 + x0 sigma),  p_psi = A x0 sigma^2,  A = Omega_psi / (1 + x0),
//! w = x0 sigma / (1 + x0 sigma),     x0 = lambda S0 / (2 m),  sigma = S / S0.
//! ```
//!
//! The condensate is OBTAINED FROM THE EVOLVING SPINOR (mean field, k = 0
//! mode, expectation-value rule of NUMERICS_CONTRACT): with mode density
//! n = n0 a^-3 (4D-effective volume V ~ a^3) and scalar density per mode
//! s(u) = u^dagger (-i gamma^4) u,
//! `sigma = a^-3 s(u) / s(u0)`.  The spinor obeys `i du/dt = h u` with
//! `h = M_eff (-i gamma^4)`, `M_eff = m + U'(S) = m (1 + 2 x0 sigma)`,
//! i.e. in N (dt/dN = 1/(H0 E)):
//!
//! ```text
//! du/dN = -i (h / H0) u / E,   h / H0 = (M_eff / H0) (-i gamma^4),
//! M_eff / H0 = mu (1 + 2 x0 sigma) / (1 + 2 x0).
//! ```
//!
//! mu = M_eff(a = 1) / H0 in {3, 7} is the reduced frequency of the contract,
//! fixed at the normalisation epoch a = 1 (M_eff varies with sigma; it
//! vanishes exactly at the phantom crossing).  The bare mass is
//! m / H0 = mu / (1 + 2 x0) (recorded per run).  Real fermions have
//! m / H0 > 1e30; the two small values demonstrate that rho, p and w do not
//! depend on the spinor phase (they depend on s(u), which is conserved).
//!
//! ODE state (35 reals), all integrated by CVODE in N:
//! * `[0]` H0 (t - t0), `d/dN = 1/E` (time measured from today; for the
//!   bouncing models there is no big bang, so no age is defined);
//! * `[1]` comoving distance D_C (units c/H0), `d/dN = -1/(a E)`: from
//!   `dD_C/dz = 1/E` and `z = e^{-N} - 1`, `dz/dN = -1/a`.  D_C > 0 in the
//!   past branch, D_C < 0 (formal, no redshift) in the future branch;
//! * `[2..34]` the spinor u in C^16 (re0..re15, im0..im15);
//! * `[34]` ln sigma, `d ln sigma/dN = -3 + (ds/dN)/s` with
//!   `ds/dN = 2 Re(u^dagger (-i gamma^4) du/dN)` evaluated from the spinor RHS
//!   (the 4D volume dilution plus the spinor's scalar-density source): this
//!   reproduces `d sigma/dN = -3 sigma` from the spinor's scalar density.
//!
//! E and M_eff in the RHS use the spinor-derived sigma.  The initial spinor
//! is the positive-energy rest eigenvector of h(a = 1) that is also a B = +1
//! eigenvector (s(u0) = 1, u0^dagger B u0 = 1).  Because h(t) is always a
//! multiple of -i gamma^4, the exact solution is `u(N) = e^{-i Phi(N)} u0`,
//! `Phi = int_0^N (M_eff / H0) / E dN'`, so s(u), u^dagger u and u^dagger B u
//! are conserved and sigma = a^-3 exactly.
//!
//! Energy-momentum from the spinor bilinears (NUMERICS_CONTRACT (A), (B); in
//! units of Omega, n_hat = a^-3 / s(u0), eps_hat = u^dagger (h/m) u):
//! `rho_psi = A (n_hat eps_hat - x0 sigma^2)`, `p_psi = A x0 sigma^2`,
//! `KE_L = (A/2) n_hat eps_hat`, `PE_L = rho_psi - KE_L`,
//! `KE_H = A n_hat sum_j p_j(u) = 0` (k = 0), `PE_H = A (sigma + x0 sigma^2)`.
//! Closed forms: `KE_L = (Omega_psi/2) sigma (1 + 2 x0 sigma)/(1 + x0)`,
//! `PE_L = (Omega_psi/2) sigma/(1 + x0)`.
//! Deceleration `q = (2 Omega_r a^-4 + Omega_m a^-3 + rho + 3 p) / (2 E^2)`
//! (= -1 - d ln E/dN), adiabatic sound speed `c_s^2 = dp/drho =
//! 2 x0 sigma / (1 + 2 x0 sigma)`, luminosity distance `d_L = (1 + z) D_C`
//! and the H0-free distance modulus `mu_H0free = 5 log10(d_L H0 / c)`
//! (the constant `5 log10(c / (H0 10 pc))` is dropped; `nan` for z <= 0).
//!
//! MEASURED DEVIATION FROM THE CONTRACT: for every x0 < 0 the attractive
//! self-interaction makes rho_psi ~ -a^-6 dominate, and E^2 reaches 0 (a
//! bounce, H = 0) at a_b > 1/3.5: z_b = 0.388, 0.423, 0.633, 0.890 for
//! x0 = -0.462654, -0.433107, -0.3, -0.2.  a_b is the unique root in (0, 1) of
//! `(Omega_m + A) a^3 + Omega_r a^2 + A x0 = 0` (E^2 a^6 with sigma = a^-3).
//! The backward branch therefore cannot reach N = ln(1/3.5); it stops at the
//! last grid point with N >= N_b + BOUNCE_MARGIN, and the check verifies
//! that the stop sits exactly there (E^2 > 0 everywhere).  Only x0 = 0 (dust)
//! reaches the contract's range.
//!
//! Output: one CSV per (x0, mu) with the two branches joined in increasing
//! N (N = 0 present once, `branch` = -1 / 0 / +1), and summary.json.
//! Transcendentals: exp, log from sundials_libm; log10(x) = log(x) / log(10)
//! and x^(1/3) = exp(log(x) / 3) (neither is in sundials_libm).

use crate::driver::{
    integrate, integrate_backward, uniform_targets, Integration, RhsFn, SolverConfig,
};
use crate::math::{exp, log};
use crate::output::{fmt17, standard_summary, write_csv, write_json, Json};
use crate::spinor::{
    energy_projector, involution_projector, mode_energy, mode_pressure, mode_rhs, norm_hilbert,
    norm_krein, range_basis, scalar_density, Algebra, CVec16, STATE_REALS, TRANSVERSE,
};
use crate::{ExperimentSummary, RunContext, Tolerances};

pub const EXPERIMENT: &str = "exp3";
pub const OMEGA_R: f64 = 0.00009;
pub const OMEGA_M: f64 = 0.305;
pub const OMEGA_PSI: f64 = 0.69491;
/// x0 = lambda S0 / (2m); w0 = x0 / (1 + x0) = -0.861, -0.764, ..., 0 (dust).
pub const X0_VALUES: [f64; 5] = [-0.462654, -0.433107, -0.3, -0.2, 0.0];
/// Reduced frequency mu = M_eff(a = 1) / H0.
pub const MU_VALUES: [f64; 2] = [3.0, 7.0];
/// a range of the contract: [1/3.5, 2].
pub const A_MIN_INVERSE: f64 = 3.5;
pub const A_MAX: f64 = 2.0;
pub const BACKWARD_INTERVALS: usize = 320;
pub const FORWARD_INTERVALS: usize = 160;
/// The backward branch of a bouncing model stops at N >= N_b + margin.
pub const BOUNCE_MARGIN: f64 = 0.01;
/// Adams + fixed point (non-stiff, oscillatory spinor phase).
pub const DEFAULT_TOLERANCES: Tolerances = Tolerances {
    rtol: 1.0e-11,
    atol: 1.0e-13,
    max_step: 0.01,
};
/// Self-check limits.
pub const CLOSURE_LIMIT: f64 = 1.0e-14;
pub const EIGEN_LIMIT: f64 = 1.0e-12;
pub const SIGMA_LIMIT: f64 = 1.0e-8;
pub const SIGMA_STATE_LIMIT: f64 = 1.0e-12;
pub const LEAK_LIMIT: f64 = 1.0e-12;
pub const NORM_LIMIT: f64 = 1.0e-8;
pub const MU_LIMIT: f64 = 1.0e-8;
pub const CLOSED_LIMIT: f64 = 1.0e-8;
pub const IDENTITY_LIMIT: f64 = 1.0e-12;
pub const ROOT_LIMIT: f64 = 1.0e-7;
pub const W0_LIMIT: f64 = 1.0e-9;
pub const WA_LIMIT: f64 = 1.0e-5;

// State layout.
const TIME: usize = 0;
const DISTANCE: usize = 1;
const SPINOR: usize = 2;
const LN_SIGMA: usize = SPINOR + STATE_REALS;
const STATE_SIZE: usize = LN_SIGMA + 1;
const ZERO_MOMENTA: [f64; 8] = [0.0; 8];

/// N = ln a at the contract's lower end a = 1/3.5.
pub fn n_min() -> f64 {
    -log(A_MIN_INVERSE)
}

/// N = ln 2.
pub fn n_max() -> f64 {
    log(A_MAX)
}

fn cube_root(x: f64) -> f64 {
    if x == 0.0 {
        0.0
    } else {
        exp(log(x) / 3.0)
    }
}

fn log10(x: f64) -> f64 {
    log(x) / log(10.0)
}

/// The 4D-effective dirac16complex dark-energy model for one (x0, mu).
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Model {
    pub x0: f64,
    pub mu: f64,
}

impl Model {
    /// A = Omega_psi / (1 + x0).
    pub fn amplitude(&self) -> f64 {
        OMEGA_PSI / (1.0 + self.x0)
    }

    pub fn rho_psi(&self, sigma: f64) -> f64 {
        self.amplitude() * sigma * (1.0 + self.x0 * sigma)
    }

    pub fn p_psi(&self, sigma: f64) -> f64 {
        self.amplitude() * self.x0 * sigma * sigma
    }

    /// E^2 at N for a given condensate sigma.
    pub fn e2(&self, n: f64, sigma: f64) -> f64 {
        OMEGA_R * exp(-4.0 * n) + OMEGA_M * exp(-3.0 * n) + self.rho_psi(sigma)
    }

    /// Closed form with sigma = a^-3.
    pub fn e2_closed(&self, n: f64) -> f64 {
        self.e2(n, exp(-3.0 * n))
    }

    /// Deceleration parameter q = -1 - d ln E / dN.
    pub fn deceleration(&self, n: f64, sigma: f64) -> f64 {
        let e2 = self.e2(n, sigma);
        (2.0 * OMEGA_R * exp(-4.0 * n)
            + OMEGA_M * exp(-3.0 * n)
            + self.rho_psi(sigma)
            + 3.0 * self.p_psi(sigma))
            / (2.0 * e2)
    }

    /// M_eff / H0 = mu (1 + 2 x0 sigma) / (1 + 2 x0).
    pub fn meff_over_h0(&self, sigma: f64) -> f64 {
        self.mu * (1.0 + 2.0 * self.x0 * sigma) / (1.0 + 2.0 * self.x0)
    }

    /// m / H0 = mu / (1 + 2 x0).
    pub fn mass_over_h0(&self) -> f64 {
        self.mu / (1.0 + 2.0 * self.x0)
    }

    pub fn w0(&self) -> f64 {
        self.x0 / (1.0 + self.x0)
    }

    /// Tangent CPL wa = -dw/da at a = 1 = 3 x0 / (1 + x0)^2.
    pub fn wa_tangent(&self) -> f64 {
        3.0 * self.x0 / ((1.0 + self.x0) * (1.0 + self.x0))
    }

    /// a at which rho_psi = 0 (x0 < 0): |x0|^(1/3).
    pub fn a_zero(&self) -> Option<f64> {
        (self.x0 < 0.0).then(|| cube_root(-self.x0))
    }

    /// a of the phantom crossing w = -1 (x0 < 0): (2|x0|)^(1/3).
    pub fn a_cross(&self) -> Option<f64> {
        (self.x0 < 0.0).then(|| cube_root(-2.0 * self.x0))
    }

    /// Bounce a_b in (0, 1) where E^2 = 0 (x0 < 0): the root of
    /// (Omega_m + A) a^3 + Omega_r a^2 + A x0 (increasing, f(0) < 0 < f(1)).
    pub fn bounce(&self) -> Option<f64> {
        if self.x0 >= 0.0 {
            return None;
        }
        let amp = self.amplitude();
        let f = |a: f64| ((OMEGA_M + amp) * a + OMEGA_R) * a * a + amp * self.x0;
        let (mut lo, mut hi) = (0.0f64, 1.0f64);
        for _ in 0..200 {
            let mid = 0.5 * (lo + hi);
            if mid <= lo || mid >= hi {
                break;
            }
            if f(mid) < 0.0 {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        Some(0.5 * (lo + hi))
    }
}

/// "0.5" -> "0p5", "-0.3" -> "m0p3", "3" -> "3".
fn label_number(value: f64) -> String {
    let text = if value == value.trunc() {
        format!("{}", value as i64)
    } else {
        format!("{value}")
    };
    text.replace('.', "p").replace('-', "m")
}

/// Lagrange interpolation value and derivative at x through (nodes, values).
fn lagrange(nodes: &[f64], values: &[f64], x: f64) -> (f64, f64) {
    let mut value = 0.0;
    let mut derivative = 0.0;
    for (i, (&xi, &yi)) in nodes.iter().zip(values).enumerate() {
        let mut basis = 1.0;
        let mut basis_derivative = 0.0;
        for (j, &xj) in nodes.iter().enumerate() {
            if j == i {
                continue;
            }
            let factor = (x - xj) / (xi - xj);
            basis_derivative = basis_derivative * factor + basis / (xi - xj);
            basis *= factor;
        }
        value += yi * basis;
        derivative += yi * basis_derivative;
    }
    (value, derivative)
}

/// All sign changes of `values` along increasing `ns`, each refined by
/// bisection on the 4-point Lagrange interpolant around the bracket.
fn sign_change_roots(ns: &[f64], values: &[f64]) -> Vec<f64> {
    let mut roots = Vec::new();
    let count = ns.len();
    for i in 0..count.saturating_sub(1) {
        let (left, right) = (values[i], values[i + 1]);
        if left == 0.0 {
            roots.push(ns[i]);
            continue;
        }
        if left * right >= 0.0 {
            continue;
        }
        let start = i.saturating_sub(1).min(count.saturating_sub(4));
        let nodes = &ns[start..start + 4];
        let vals = &values[start..start + 4];
        let (mut lo, mut hi) = (ns[i], ns[i + 1]);
        let lo_sign = left.signum();
        for _ in 0..200 {
            let mid = 0.5 * (lo + hi);
            if mid <= lo || mid >= hi {
                break;
            }
            if lagrange(nodes, vals, mid).0.signum() == lo_sign {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        roots.push(0.5 * (lo + hi));
    }
    roots
}

/// Closed-form roots of `g(N)` bracketed on the grid `ns`, refined by bisection.
fn closed_form_roots(ns: &[f64], g: &dyn Fn(f64) -> f64) -> Vec<f64> {
    let mut roots = Vec::new();
    for pair in ns.windows(2) {
        let (gl, gr) = (g(pair[0]), g(pair[1]));
        if gl == 0.0 {
            roots.push(pair[0]);
            continue;
        }
        if gl * gr >= 0.0 {
            continue;
        }
        let (mut lo, mut hi) = (pair[0], pair[1]);
        for _ in 0..200 {
            let mid = 0.5 * (lo + hi);
            if mid <= lo || mid >= hi {
                break;
            }
            if g(mid).signum() == gl.signum() {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        roots.push(0.5 * (lo + hi));
    }
    roots
}

fn rhs_for(alg: &Algebra, model: Model, s0: f64) -> RhsFn {
    let alg = alg.clone();
    Box::new(move |n, y, ydot| {
        let spinor = &y[SPINOR..SPINOR + STATE_REALS];
        let u = CVec16::from_state(spinor);
        let s = scalar_density(&alg, &u);
        let a = exp(n);
        let sigma = exp(-3.0 * n) * s / s0;
        let e2 = model.e2(n, sigma);
        if e2.is_nan() || e2 <= 0.0 {
            // Recoverable failure (non-finite derivative): CVODE retries
            // with a smaller step.  Never reached with the bounce margin.
            ydot.iter_mut().for_each(|value| *value = f64::NAN);
            return Ok(());
        }
        let e = e2.sqrt();
        ydot[TIME] = 1.0 / e;
        ydot[DISTANCE] = -1.0 / (a * e);
        let h_over_e = alg.mode_hamiltonian(model.meff_over_h0(sigma) / e, &ZERO_MOMENTA);
        mode_rhs(&h_over_e, spinor, &mut ydot[SPINOR..SPINOR + STATE_REALS]);
        let du = CVec16::from_state(&ydot[SPINOR..SPINOR + STATE_REALS]);
        let ds = 2.0 * u.dot(&alg.minus_i_g4.apply(&du)).0;
        ydot[LN_SIGMA] = -3.0 + ds / s;
        Ok(())
    })
}

fn header() -> Vec<String> {
    let mut header: Vec<String> = ["N", "a", "z", "branch", "H0t", "D_C"]
        .iter()
        .map(|s| s.to_string())
        .collect();
    header.extend((0..16).map(|i| format!("u_re_{i}")));
    header.extend((0..16).map(|i| format!("u_im_{i}")));
    for name in [
        "ln_sigma",
        "E",
        "q",
        "rho_psi",
        "p_psi",
        "w",
        "KE_L",
        "PE_L",
        "KE_H",
        "PE_H",
        "Omega_psi",
        "Omega_m",
        "cs2",
        "M_eff_over_H0",
        "s_u",
        "sigma_spinor",
        "sigma_state",
        "sigma_analytic",
        "norm_hilbert",
        "norm_krein",
        "eigen_leak",
        "rho_closed",
        "p_closed",
        "w_closed",
        "d_L",
        "mu_H0free",
    ] {
        header.push(name.to_string());
    }
    header
}

/// Column indices of the derived quantities (after the 39 state columns).
mod col {
    pub const N: usize = 0;
    pub const E: usize = 39;
    pub const Q: usize = 40;
    pub const RHO: usize = 41;
    pub const P: usize = 42;
    pub const W: usize = 43;
    pub const KE_L: usize = 44;
    pub const PE_L: usize = 45;
    pub const KE_H: usize = 46;
    pub const PE_H: usize = 47;
    pub const OMEGA_PSI: usize = 48;
    pub const CS2: usize = 50;
    pub const SIGMA_SPINOR: usize = 53;
    pub const SIGMA_STATE: usize = 54;
    pub const SIGMA_ANALYTIC: usize = 55;
    pub const HILBERT: usize = 56;
    pub const KREIN: usize = 57;
    pub const LEAK: usize = 58;
    pub const RHO_CLOSED: usize = 59;
    pub const P_CLOSED: usize = 60;
    pub const W_CLOSED: usize = 61;
    pub const COUNT: usize = 64;
}

fn observables_row(
    alg: &Algebra,
    model: &Model,
    s0: f64,
    n: f64,
    branch: f64,
    y: &[f64],
) -> Vec<f64> {
    let a = exp(n);
    let z = exp(-n) - 1.0;
    let a3inv = exp(-3.0 * n);
    let u = CVec16::from_state(&y[SPINOR..SPINOR + STATE_REALS]);
    let s = scalar_density(alg, &u);
    let sigma = a3inv * s / s0;
    let sigma_state = exp(y[LN_SIGMA]);
    let e2 = model.e2(n, sigma);
    let e = e2.sqrt();
    let amp = model.amplitude();
    let x0 = model.x0;
    // eps_hat = u^dagger (h/m) u with h/m = (M_eff/m)(-i gamma^4).
    let h_hat = alg.mode_hamiltonian(1.0 + 2.0 * x0 * sigma, &ZERO_MOMENTA);
    let eps_hat = mode_energy(&h_hat, &u);
    let n_hat = a3inv / s0;
    let rho = amp * (n_hat * eps_hat - x0 * sigma * sigma);
    let p = amp * x0 * sigma * sigma;
    let ke_l = 0.5 * amp * n_hat * eps_hat;
    let pe_l = rho - ke_l;
    let gradient: f64 = TRANSVERSE
        .iter()
        .map(|&j| mode_pressure(alg, &u, ZERO_MOMENTA[j], j))
        .sum();
    let ke_h = amp * n_hat * gradient;
    let pe_h = amp * (sigma + x0 * sigma * sigma);
    let q = (2.0 * OMEGA_R * exp(-4.0 * n) + OMEGA_M * a3inv + rho + 3.0 * p) / (2.0 * e2);
    let cs2 = 2.0 * x0 * sigma / (1.0 + 2.0 * x0 * sigma);
    let hilbert = norm_hilbert(&u);
    let krein = norm_krein(alg, &u);
    let ou = alg.minus_i_g4.apply(&u);
    let leak = 0.5 * u.distance(&ou) / hilbert.sqrt();
    let rho_closed = model.rho_psi(a3inv);
    let p_closed = model.p_psi(a3inv);
    let w_closed = x0 * a3inv / (1.0 + x0 * a3inv);
    let d_l = (1.0 + z) * y[DISTANCE];
    let mu_modulus = if z > 0.0 && d_l > 0.0 {
        5.0 * log10(d_l)
    } else {
        f64::NAN
    };
    let mut row = vec![n, a, z, branch, y[TIME], y[DISTANCE]];
    row.extend_from_slice(&y[SPINOR..SPINOR + STATE_REALS]);
    row.extend([
        y[LN_SIGMA],
        e,
        q,
        rho,
        p,
        p / rho,
        ke_l,
        pe_l,
        ke_h,
        pe_h,
        rho / e2,
        OMEGA_M * a3inv / e2,
        cs2,
        model.meff_over_h0(sigma),
        s,
        sigma,
        sigma_state,
        a3inv,
        hilbert,
        krein,
        leak,
        rho_closed,
        p_closed,
        w_closed,
        d_l,
        mu_modulus,
    ]);
    row
}

#[derive(Clone, Debug)]
struct RunSpec {
    id: String,
    model: Model,
    u0: CVec16,
    s0: f64,
    eigen_residual: f64,
}

struct RunOutcome {
    spec: RunSpec,
    file: String,
    backward: Integration,
    forward: Integration,
    rows: Vec<Vec<f64>>,
    backward_end: f64,
    backward_reached_contract: bool,
    bounce_stop_ok: bool,
    hubble_positive: bool,
    // Maxima over the run.
    sigma_dev: f64,
    sigma_state_dev: f64,
    leak: f64,
    hilbert_dev: f64,
    krein_dev: f64,
    rho_closed_dev: f64,
    p_closed_dev: f64,
    w_closed_dev: f64,
    identity_dev: f64,
    e0: f64,
    omega_psi0: f64,
    // Diagnostics from the data.
    zero_roots: Vec<f64>,
    cross_roots: Vec<f64>,
    q_roots: Vec<f64>,
    q_roots_closed: Vec<f64>,
    w0_data: f64,
    wa_data: f64,
    q0: f64,
    cs2_0: f64,
}

fn initial_spinor(alg: &Algebra, mu: f64) -> Result<(CVec16, f64), String> {
    let h0 = alg.mode_hamiltonian(mu, &ZERO_MOMENTA);
    let projector = energy_projector(&h0, mu, 1.0).mul(&involution_projector(&alg.b, 1.0));
    let u0 = *range_basis(&projector, 1.0e-8)
        .first()
        .ok_or_else(|| "empty (h, B) eigenspace".to_string())?;
    let residual = h0
        .apply(&u0)
        .max_abs_diff(&u0.scale(mu, 0.0))
        .max(alg.b.apply(&u0).max_abs_diff(&u0));
    Ok((u0, residual))
}

fn build_runs(alg: &Algebra) -> Result<Vec<RunSpec>, String> {
    let mut runs = Vec::new();
    for &x0 in &X0_VALUES {
        if 1.0 + 2.0 * x0 <= 0.0 {
            return Err(format!(
                "x0 = {x0}: M_eff(a=1) = m (1 + 2 x0) must be positive"
            ));
        }
        for &mu in &MU_VALUES {
            let (u0, eigen_residual) = initial_spinor(alg, mu)?;
            runs.push(RunSpec {
                id: format!("x0_{}_mu{}", label_number(x0), label_number(mu)),
                model: Model { x0, mu },
                s0: scalar_density(alg, &u0),
                u0,
                eigen_residual,
            });
        }
    }
    Ok(runs)
}

/// Backward output grid: the uniform grid N_k = N_min k / BACKWARD_INTERVALS,
/// truncated at N_b + BOUNCE_MARGIN for a bouncing model.
fn backward_targets(model: &Model) -> Vec<f64> {
    let full = uniform_targets(0.0, n_min(), BACKWARD_INTERVALS);
    match model.bounce() {
        Some(a_b) if log(a_b) + BOUNCE_MARGIN > n_min() => {
            let limit = log(a_b) + BOUNCE_MARGIN;
            full.into_iter().filter(|&n| n >= limit).collect()
        }
        _ => full,
    }
}

fn solver(tolerances: &Tolerances, stop: f64) -> SolverConfig {
    SolverConfig::adams(tolerances.rtol, tolerances.atol, tolerances.max_step).with_stop_time(stop)
}

fn max_abs_by(rows: &[Vec<f64>], f: &dyn Fn(&[f64]) -> f64) -> f64 {
    rows.iter().map(|row| f(row).abs()).fold(0.0f64, f64::max)
}

/// Scale of rho and p at a row: A sigma (1 + |x0| sigma).
fn density_scale(model: &Model, row: &[f64]) -> f64 {
    let sigma = row[col::SIGMA_ANALYTIC];
    model.amplitude() * sigma * (1.0 + model.x0.abs() * sigma)
}

/// w difference scaled by its condition number |1 + x0 sigma| / max(1, |w|)
/// (dw / w = (d sigma / sigma) / (1 + x0 sigma) near the rho_psi zero).
fn w_scaled(model: &Model, row: &[f64], dw: f64) -> f64 {
    let sigma = row[col::SIGMA_ANALYTIC];
    dw * (1.0 + model.x0 * sigma).abs() / row[col::W_CLOSED].abs().max(1.0)
}

fn execute(alg: &Algebra, spec: RunSpec, tolerances: &Tolerances) -> Result<RunOutcome, String> {
    let model = spec.model;
    let mut y0 = vec![0.0; STATE_SIZE];
    spec.u0.write_state(&mut y0[SPINOR..SPINOR + STATE_REALS]);
    y0[LN_SIGMA] = 0.0;

    let back_targets = backward_targets(&model);
    let backward_end = *back_targets
        .last()
        .ok_or_else(|| format!("run {}: empty backward grid", spec.id))?;
    let backward = integrate_backward(
        y0.clone(),
        0.0,
        &back_targets,
        rhs_for(alg, model, spec.s0),
        &solver(tolerances, backward_end),
    )
    .map_err(|error| format!("run {} backward: {error}", spec.id))?;
    let fwd_targets = uniform_targets(0.0, n_max(), FORWARD_INTERVALS);
    let forward = integrate(
        y0,
        0.0,
        &fwd_targets,
        rhs_for(alg, model, spec.s0),
        &solver(tolerances, n_max()),
    )
    .map_err(|error| format!("run {} forward: {error}", spec.id))?;

    // Join: backward reversed (N increasing), N = 0 once, forward.
    let mut rows = Vec::with_capacity(backward.times.len() + forward.times.len() - 1);
    for index in (0..backward.times.len()).rev() {
        let branch = if index == 0 { 0.0 } else { -1.0 };
        rows.push(observables_row(
            alg,
            &model,
            spec.s0,
            backward.times[index],
            branch,
            &backward.states[index],
        ));
    }
    for index in 1..forward.times.len() {
        rows.push(observables_row(
            alg,
            &model,
            spec.s0,
            forward.times[index],
            1.0,
            &forward.states[index],
        ));
    }
    let i0 = backward.times.len() - 1;

    let backward_reached_contract = backward_end == n_min();
    let back_step = n_min().abs() / BACKWARD_INTERVALS as f64;
    let bounce_stop_ok = match model.bounce() {
        Some(a_b) => {
            let gap = backward_end - log(a_b);
            (BOUNCE_MARGIN..BOUNCE_MARGIN + back_step * (1.0 + 1.0e-12)).contains(&gap)
        }
        None => backward_reached_contract,
    };
    let hubble_positive = rows.iter().all(|row| row[col::E] > 0.0);

    let sigma_dev = max_abs_by(&rows, &|r| {
        r[col::SIGMA_SPINOR] / r[col::SIGMA_ANALYTIC] - 1.0
    });
    let sigma_state_dev = max_abs_by(&rows, &|r| {
        r[col::SIGMA_STATE] / r[col::SIGMA_ANALYTIC] - 1.0
    });
    let leak = max_abs_by(&rows, &|r| r[col::LEAK]);
    let hilbert_dev = max_abs_by(&rows, &|r| r[col::HILBERT] - 1.0);
    let krein_dev = max_abs_by(&rows, &|r| r[col::KREIN] - 1.0);
    let rho_closed_dev = max_abs_by(&rows, &|r| {
        (r[col::RHO] - r[col::RHO_CLOSED]) / density_scale(&model, r)
    });
    let p_closed_dev = max_abs_by(&rows, &|r| {
        (r[col::P] - r[col::P_CLOSED]) / density_scale(&model, r)
    });
    let w_closed_dev = max_abs_by(&rows, &|r| {
        w_scaled(&model, r, r[col::W] - r[col::W_CLOSED])
    });
    let identity_dev = max_abs_by(&rows, &|r| {
        let scale = density_scale(&model, r);
        let sigma = r[col::SIGMA_SPINOR];
        let pe_closed = 0.5 * model.amplitude() * sigma;
        ((r[col::KE_L] + r[col::PE_L] - r[col::RHO]).abs()
            + (r[col::KE_L] - r[col::PE_L] - r[col::P]).abs()
            + r[col::KE_H].abs()
            + (r[col::PE_H] - r[col::RHO]).abs()
            + (r[col::PE_L] - pe_closed).abs())
            / scale
    });

    let ns: Vec<f64> = rows.iter().map(|r| r[col::N]).collect();
    let column = |index: usize| -> Vec<f64> { rows.iter().map(|r| r[index]).collect() };
    let zero_roots = sign_change_roots(&ns, &column(col::RHO));
    let rho_plus_p: Vec<f64> = rows.iter().map(|r| r[col::RHO] + r[col::P]).collect();
    let cross_roots = sign_change_roots(&ns, &rho_plus_p);
    let q_roots = sign_change_roots(&ns, &column(col::Q));
    let q_numerator = |n: f64| {
        let sigma = exp(-3.0 * n);
        2.0 * OMEGA_R * exp(-4.0 * n)
            + OMEGA_M * sigma
            + model.rho_psi(sigma)
            + 3.0 * model.p_psi(sigma)
    };
    let q_roots_closed = closed_form_roots(&ns, &q_numerator);
    // Tangent CPL: 5-point Lagrange derivative at N = 0 (non-uniform steps).
    let nodes = &ns[i0 - 2..i0 + 3];
    let ws: Vec<f64> = rows[i0 - 2..i0 + 3].iter().map(|r| r[col::W]).collect();
    let (_, dw_dn) = lagrange(nodes, &ws, 0.0);
    let today = &rows[i0];

    let file = format!("run_{}.csv", spec.id);
    Ok(RunOutcome {
        file,
        backward_end,
        backward_reached_contract,
        bounce_stop_ok,
        hubble_positive,
        sigma_dev,
        sigma_state_dev,
        leak,
        hilbert_dev,
        krein_dev,
        rho_closed_dev,
        p_closed_dev,
        w_closed_dev,
        identity_dev,
        e0: today[col::E],
        omega_psi0: today[col::OMEGA_PSI],
        zero_roots,
        cross_roots,
        q_roots,
        q_roots_closed,
        w0_data: today[col::W],
        // a = e^N: dw/da = dw/dN at a = 1.
        wa_data: -dw_dn,
        q0: today[col::Q],
        cs2_0: today[col::CS2],
        spec,
        backward,
        forward,
        rows,
    })
}

fn optional(value: Option<f64>) -> Json {
    value.map(Json::Float).unwrap_or(Json::Null)
}

fn redshift(a: Option<f64>) -> Json {
    optional(a.map(|a| 1.0 / a - 1.0))
}

fn roots_json(roots: &[f64]) -> Json {
    Json::Array(
        roots
            .iter()
            .map(|&n| {
                Json::object(vec![
                    ("N", Json::Float(n)),
                    ("a", Json::Float(exp(n))),
                    ("z", Json::Float(exp(-n) - 1.0)),
                ])
            })
            .collect(),
    )
}

fn integration_json(run: &Integration) -> Json {
    Json::object(vec![
        ("steps", Json::Int(run.steps)),
        ("rhsEvals", Json::Int(run.rhs_evals)),
        ("errTestFails", Json::Int(run.err_test_fails)),
        ("nonlinIters", Json::Int(run.nonlin_iters)),
        ("nonlinConvFails", Json::Int(run.nonlin_conv_fails)),
        ("lastOrder", Json::Int(run.last_order as i64)),
    ])
}

fn relative_root_error(roots: &[f64], expected: Option<f64>) -> f64 {
    match expected {
        Some(a) => {
            if roots.len() != 1 {
                f64::INFINITY
            } else {
                (exp(roots[0]) - a).abs() / a
            }
        }
        None => {
            if roots.is_empty() {
                0.0
            } else {
                f64::INFINITY
            }
        }
    }
}

fn run_json(o: &RunOutcome) -> Json {
    let model = &o.spec.model;
    Json::object(vec![
        ("id", Json::str(&o.spec.id)),
        ("file", Json::str(&o.file)),
        ("x0", Json::Float(model.x0)),
        ("mu", Json::Float(model.mu)),
        ("massOverH0", Json::Float(model.mass_over_h0())),
        ("s0", Json::Float(o.spec.s0)),
        ("initialEigenResidual", Json::Float(o.spec.eigen_residual)),
        (
            "backward",
            Json::object(vec![
                ("points", Json::Int(o.backward.times.len() as i64 - 1)),
                ("nEnd", Json::Float(o.backward_end)),
                ("aEnd", Json::Float(exp(o.backward_end))),
                ("zEnd", Json::Float(exp(-o.backward_end) - 1.0)),
                (
                    "reachedContractMinimum",
                    Json::Bool(o.backward_reached_contract),
                ),
                ("stopConsistentWithBounce", Json::Bool(o.bounce_stop_ok)),
                ("solver", integration_json(&o.backward)),
            ]),
        ),
        (
            "forward",
            Json::object(vec![
                ("points", Json::Int(o.forward.times.len() as i64 - 1)),
                (
                    "nEnd",
                    Json::Float(o.forward.times[o.forward.times.len() - 1]),
                ),
                ("solver", integration_json(&o.forward)),
            ]),
        ),
        (
            "measured",
            Json::object(vec![
                ("E0", Json::Float(o.e0)),
                ("OmegaPsi0", Json::Float(o.omega_psi0)),
                ("w0", Json::Float(o.w0_data)),
                ("waTangent", Json::Float(o.wa_data)),
                ("q0", Json::Float(o.q0)),
                ("cs2Today", Json::Float(o.cs2_0)),
                ("rhoZeros", roots_json(&o.zero_roots)),
                ("phantomCrossings", roots_json(&o.cross_roots)),
                ("decelerationSignChanges", roots_json(&o.q_roots)),
                (
                    "decelerationSignChangesClosedForm",
                    roots_json(&o.q_roots_closed),
                ),
            ]),
        ),
        (
            "maxDeviation",
            Json::object(vec![
                ("sigmaSpinorVsAnalytic", Json::Float(o.sigma_dev)),
                ("sigmaStateVsAnalytic", Json::Float(o.sigma_state_dev)),
                ("eigenspaceLeak", Json::Float(o.leak)),
                ("normHilbert", Json::Float(o.hilbert_dev)),
                ("normKrein", Json::Float(o.krein_dev)),
                ("rhoVsClosedForm", Json::Float(o.rho_closed_dev)),
                ("pVsClosedForm", Json::Float(o.p_closed_dev)),
                ("wVsClosedFormScaled", Json::Float(o.w_closed_dev)),
                ("splitIdentities", Json::Float(o.identity_dev)),
            ]),
        ),
    ])
}

fn model_json(model: &Model) -> Json {
    let bounce = model.bounce();
    Json::object(vec![
        ("x0", Json::Float(model.x0)),
        ("amplitudeA", Json::Float(model.amplitude())),
        ("w0", Json::Float(model.w0())),
        ("waTangent", Json::Float(model.wa_tangent())),
        ("aZero", optional(model.a_zero())),
        ("zZero", redshift(model.a_zero())),
        ("aPhantomCrossing", optional(model.a_cross())),
        ("zPhantomCrossing", redshift(model.a_cross())),
        ("aBounce", optional(bounce)),
        ("zBounce", redshift(bounce)),
        ("nBounce", optional(bounce.map(log))),
        (
            "contractBackwardRangeReachable",
            Json::Bool(bounce.is_none_or(|a_b| log(a_b) + BOUNCE_MARGIN <= n_min())),
        ),
        ("q0", Json::Float(model.deceleration(0.0, 1.0))),
        (
            "cs2Today",
            Json::Float(2.0 * model.x0 / (1.0 + 2.0 * model.x0)),
        ),
    ])
}

/// Configuration lines for `print-config`.
pub fn config_lines() -> Vec<String> {
    vec![
        format!(
            "exp3: Omega_r = {}, Omega_m = {}, Omega_psi = {}, x0 = {:?}, mu = M_eff(1)/H0 = {:?}",
            fmt17(OMEGA_R),
            fmt17(OMEGA_M),
            fmt17(OMEGA_PSI),
            X0_VALUES,
            MU_VALUES
        ),
        format!(
            "exp3: N in [ln(1/{}), ln {}], {} + {} output intervals, bounce margin {}",
            fmt17(A_MIN_INVERSE),
            fmt17(A_MAX),
            BACKWARD_INTERVALS,
            FORWARD_INTERVALS,
            fmt17(BOUNCE_MARGIN)
        ),
        format!(
            "exp3: default rtol = {}, atol = {}, max_step = {}, method Adams + fixed point",
            fmt17(DEFAULT_TOLERANCES.rtol),
            fmt17(DEFAULT_TOLERANCES.atol),
            fmt17(DEFAULT_TOLERANCES.max_step)
        ),
    ]
}

/// Run EXP-3.
pub fn run(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let directory = ctx.experiment_dir(EXPERIMENT)?;
    let tolerances = ctx.tolerances(DEFAULT_TOLERANCES);
    let alg = Algebra::new();
    let mut summary = ExperimentSummary::new(EXPERIMENT);
    let mut outcomes: Vec<RunOutcome> = Vec::new();
    for spec in build_runs(&alg)? {
        let outcome = execute(&alg, spec, &tolerances)?;
        if outcome.rows.iter().any(|row| row.len() != col::COUNT) {
            return Err("internal: row width mismatch".to_string());
        }
        write_csv(&directory.join(&outcome.file), &header(), &outcome.rows)?;
        summary.add_file(&outcome.file);
        for run in [&outcome.backward, &outcome.forward] {
            summary.add_stats(run.steps, run.rhs_evals);
        }
        outcomes.push(outcome);
    }

    // mu independence: the two mu runs of every x0 share the N grid.
    let mut mu_json = Vec::new();
    let (mut mu_rho, mut mu_p, mut mu_w, mut mu_sigma) = (0.0f64, 0.0f64, 0.0f64, 0.0f64);
    let mut grids_match = true;
    for &x0 in &X0_VALUES {
        let pair: Vec<&RunOutcome> = outcomes.iter().filter(|o| o.spec.model.x0 == x0).collect();
        let (first, second) = (pair[0], pair[1]);
        let model = first.spec.model;
        grids_match &= first.rows.len() == second.rows.len();
        let (mut d_rho, mut d_p, mut d_w, mut d_sigma) = (0.0f64, 0.0f64, 0.0f64, 0.0f64);
        for (r1, r2) in first.rows.iter().zip(&second.rows) {
            grids_match &= r1[col::N] == r2[col::N];
            let scale = density_scale(&model, r1);
            d_rho = d_rho.max((r1[col::RHO] - r2[col::RHO]).abs() / scale);
            d_p = d_p.max((r1[col::P] - r2[col::P]).abs() / scale);
            d_w = d_w.max(w_scaled(&model, r1, r1[col::W] - r2[col::W]).abs());
            d_sigma = d_sigma.max(
                (r1[col::SIGMA_SPINOR] - r2[col::SIGMA_SPINOR]).abs() / r1[col::SIGMA_ANALYTIC],
            );
        }
        mu_rho = mu_rho.max(d_rho);
        mu_p = mu_p.max(d_p);
        mu_w = mu_w.max(d_w);
        mu_sigma = mu_sigma.max(d_sigma);
        mu_json.push(Json::object(vec![
            ("x0", Json::Float(x0)),
            (
                "runs",
                Json::Array(vec![Json::str(&first.spec.id), Json::str(&second.spec.id)]),
            ),
            ("rhoMaxScaledDiff", Json::Float(d_rho)),
            ("pMaxScaledDiff", Json::Float(d_p)),
            ("wMaxConditionScaledDiff", Json::Float(d_w)),
            ("sigmaMaxRelDiff", Json::Float(d_sigma)),
        ]));
    }

    let fold = |f: &dyn Fn(&RunOutcome) -> f64| outcomes.iter().map(f).fold(0.0f64, f64::max);
    let closure = (OMEGA_R + OMEGA_M + OMEGA_PSI - 1.0).abs();
    let e0_dev = fold(&|o| (o.e0 - 1.0).abs());
    let omega0_dev = fold(&|o| (o.omega_psi0 - OMEGA_PSI).abs());
    let eigen = fold(&|o| o.spec.eigen_residual);
    let s0_dev = fold(&|o| (o.spec.s0 - 1.0).abs());
    let sigma_dev = fold(&|o| o.sigma_dev);
    let sigma_state_dev = fold(&|o| o.sigma_state_dev);
    let leak = fold(&|o| o.leak);
    let hilbert = fold(&|o| o.hilbert_dev);
    let krein = fold(&|o| o.krein_dev);
    let rho_dev = fold(&|o| o.rho_closed_dev);
    let p_dev = fold(&|o| o.p_closed_dev);
    let w_dev = fold(&|o| o.w_closed_dev);
    let identity = fold(&|o| o.identity_dev);
    let zero_dev = fold(&|o| relative_root_error(&o.zero_roots, o.spec.model.a_zero()));
    let cross_dev = fold(&|o| relative_root_error(&o.cross_roots, o.spec.model.a_cross()));
    let q_root_dev = fold(&|o| {
        if o.q_roots.len() != o.q_roots_closed.len() {
            f64::INFINITY
        } else {
            o.q_roots
                .iter()
                .zip(&o.q_roots_closed)
                .map(|(x, y)| (exp(*x) - exp(*y)).abs() / exp(*y))
                .fold(0.0, f64::max)
        }
    });
    let w0_dev = fold(&|o| (o.w0_data - o.spec.model.w0()).abs());
    let wa_dev = fold(&|o| {
        let expected = o.spec.model.wa_tangent();
        (o.wa_data - expected).abs() / expected.abs().max(1.0)
    });
    let bounce_ok = outcomes
        .iter()
        .all(|o| o.bounce_stop_ok && o.hubble_positive);

    summary.check(
        "closure_E0_equals_1",
        closure <= CLOSURE_LIMIT && e0_dev <= CLOSURE_LIMIT && omega0_dev <= CLOSURE_LIMIT,
        &format!(
            "|Omega_r + Omega_m + Omega_psi - 1| = {}, max |E(0) - 1| = {}, max |Omega_psi(1) - Omega_psi| = {}",
            fmt17(closure),
            fmt17(e0_dev),
            fmt17(omega0_dev)
        ),
    );
    summary.check(
        "initial_positive_energy_B_eigenvector",
        eigen <= EIGEN_LIMIT && s0_dev <= EIGEN_LIMIT,
        &format!(
            "max |h u0 - mu u0|, |B u0 - u0| = {}, max |s(u0) - 1| = {}",
            fmt17(eigen),
            fmt17(s0_dev)
        ),
    );
    summary.check(
        "sigma_from_spinor_equals_a_minus_3",
        sigma_dev <= SIGMA_LIMIT,
        &format!(
            "max |a^3 sigma_spinor - 1| = {} (limit {})",
            fmt17(sigma_dev),
            fmt17(SIGMA_LIMIT)
        ),
    );
    summary.check(
        "ln_sigma_state_reproduces_minus_3",
        sigma_state_dev <= SIGMA_STATE_LIMIT,
        &format!(
            "max |a^3 exp(ln sigma) - 1| = {} (limit {})",
            fmt17(sigma_state_dev),
            fmt17(SIGMA_STATE_LIMIT)
        ),
    );
    summary.check(
        "spinor_stays_in_rest_eigenspace",
        leak <= LEAK_LIMIT,
        &format!("max |(1 - (-i gamma^4)) u| / (2 |u|) = {}", fmt17(leak)),
    );
    summary.check(
        "hilbert_and_krein_norms_conserved",
        hilbert <= NORM_LIMIT && krein <= NORM_LIMIT,
        &format!(
            "max |u^dag u - 1| = {}, max |u^dag B u - 1| = {}",
            fmt17(hilbert),
            fmt17(krein)
        ),
    );
    summary.check(
        "rho_p_w_mu_independent",
        grids_match && mu_rho <= MU_LIMIT && mu_p <= MU_LIMIT && mu_w <= MU_LIMIT,
        &format!(
            "mu = 3 vs 7: rho {}, p {}, w (condition-scaled) {}, sigma {} (limit {})",
            fmt17(mu_rho),
            fmt17(mu_p),
            fmt17(mu_w),
            fmt17(mu_sigma),
            fmt17(MU_LIMIT)
        ),
    );
    summary.check(
        "rho_p_w_match_closed_form",
        rho_dev <= CLOSED_LIMIT && p_dev <= CLOSED_LIMIT && w_dev <= CLOSED_LIMIT,
        &format!(
            "scaled max deviation rho {}, p {}, w {} (limit {})",
            fmt17(rho_dev),
            fmt17(p_dev),
            fmt17(w_dev),
            fmt17(CLOSED_LIMIT)
        ),
    );
    summary.check(
        "kinetic_potential_split_identities",
        identity <= IDENTITY_LIMIT,
        &format!(
            "KE_L + PE_L = rho, KE_L - PE_L = p, KE_H = 0, PE_H = rho, PE_L = (A/2) sigma: max {}",
            fmt17(identity)
        ),
    );
    summary.check(
        "hubble_positive_backward_stop_at_predicted_bounce",
        bounce_ok,
        &format!(
            "E > 0 on every row; x0 < 0 stops at N_b + [{}, {} + dN), x0 = 0 reaches ln(1/3.5)",
            fmt17(BOUNCE_MARGIN),
            fmt17(BOUNCE_MARGIN)
        ),
    );
    summary.check(
        "rho_psi_zero_at_cube_root_abs_x0",
        zero_dev <= ROOT_LIMIT,
        &format!("max |a_zero - |x0|^(1/3)| / a = {}", fmt17(zero_dev)),
    );
    summary.check(
        "phantom_crossing_at_cube_root_2abs_x0",
        cross_dev <= ROOT_LIMIT,
        &format!("max |a_cross - (2|x0|)^(1/3)| / a = {}", fmt17(cross_dev)),
    );
    summary.check(
        "deceleration_sign_changes_match_closed_form",
        q_root_dev <= ROOT_LIMIT,
        &format!("max relative a deviation = {}", fmt17(q_root_dev)),
    );
    summary.check(
        "tangent_cpl_w0_wa",
        w0_dev <= W0_LIMIT && wa_dev <= WA_LIMIT,
        &format!(
            "max |w(1) - x0/(1+x0)| = {}, max |wa_FD - 3x0/(1+x0)^2| / max(|wa|,1) = {}",
            fmt17(w0_dev),
            fmt17(wa_dev)
        ),
    );

    let deviations: Vec<Json> = X0_VALUES
        .iter()
        .filter_map(|&x0| {
            let model = Model { x0, mu: MU_VALUES[0] };
            model.bounce().map(|a_b| {
                Json::str(&format!(
                    "x0 = {x0}: E^2 = 0 (bounce, H = 0) at a_b = {:.6} > 1/3.5 (z_b = {:.6} < 2.5); \
                     a < a_b (z > z_b) does not exist in this model, so the contract's backward \
                     range down to N = ln(1/3.5) is unreachable; the backward branch stops at \
                     N_b + {BOUNCE_MARGIN}.",
                    a_b,
                    1.0 / a_b - 1.0
                ))
            })
        })
        .collect();
    let extra = vec![
        (
            "parameters",
            Json::object(vec![
                ("OmegaR", Json::Float(OMEGA_R)),
                ("OmegaM", Json::Float(OMEGA_M)),
                ("OmegaPsi", Json::Float(OMEGA_PSI)),
                ("x0Values", Json::floats(&X0_VALUES)),
                ("muValues", Json::floats(&MU_VALUES)),
                (
                    "muDefinition",
                    Json::str("mu = M_eff(a=1)/H0; M_eff/H0 = mu (1 + 2 x0 sigma)/(1 + 2 x0); m/H0 = mu/(1 + 2 x0)"),
                ),
                ("aMin", Json::Float(1.0 / A_MIN_INVERSE)),
                ("aMax", Json::Float(A_MAX)),
                ("nMin", Json::Float(n_min())),
                ("nMax", Json::Float(n_max())),
                ("backwardIntervals", Json::Int(BACKWARD_INTERVALS as i64)),
                ("forwardIntervals", Json::Int(FORWARD_INTERVALS as i64)),
                ("bounceMargin", Json::Float(BOUNCE_MARGIN)),
            ]),
        ),
        (
            "stateLayout",
            Json::str(
                "H0t = H0 (t - t0), D_C (c/H0), u_re_0..u_re_15, u_im_0..u_im_15, ln_sigma; \
                 independent variable N = ln a",
            ),
        ),
        (
            "equations",
            Json::object(vec![
                ("dH0t_dN", Json::str("1/E")),
                ("dDC_dN", Json::str("-1/(a E)  (dD_C/dz = 1/E, z = e^-N - 1)")),
                ("du_dN", Json::str("-i (M_eff/H0)(-i gamma^4) u / E")),
                ("dlnsigma_dN", Json::str("-3 + 2 Re(u^dag (-i gamma^4) du/dN) / s(u)")),
                ("sigma", Json::str("a^-3 s(u) / s(u0), s(u) = u^dag (-i gamma^4) u")),
                ("E2", Json::str("Omega_r a^-4 + Omega_m a^-3 + A sigma (1 + x0 sigma), A = Omega_psi/(1+x0)")),
                ("muH0free", Json::str("5 log10((1+z) D_C), constant 5 log10(c/(H0 10 pc)) dropped; nan for z <= 0")),
            ]),
        ),
        (
            "limits",
            Json::object(vec![
                ("closure", Json::Float(CLOSURE_LIMIT)),
                ("eigen", Json::Float(EIGEN_LIMIT)),
                ("sigmaSpinor", Json::Float(SIGMA_LIMIT)),
                ("sigmaState", Json::Float(SIGMA_STATE_LIMIT)),
                ("eigenspaceLeak", Json::Float(LEAK_LIMIT)),
                ("norm", Json::Float(NORM_LIMIT)),
                ("muIndependence", Json::Float(MU_LIMIT)),
                ("closedForm", Json::Float(CLOSED_LIMIT)),
                ("identity", Json::Float(IDENTITY_LIMIT)),
                ("root", Json::Float(ROOT_LIMIT)),
                ("w0", Json::Float(W0_LIMIT)),
                ("wa", Json::Float(WA_LIMIT)),
            ]),
        ),
        (
            "models",
            Json::Array(
                X0_VALUES
                    .iter()
                    .map(|&x0| model_json(&Model { x0, mu: MU_VALUES[0] }))
                    .collect(),
            ),
        ),
        ("runs", Json::Array(outcomes.iter().map(run_json).collect())),
        ("muIndependence", Json::Array(mu_json)),
        (
            "measurements",
            Json::object(vec![
                ("closureDefect", Json::Float(closure)),
                ("maxE0Deviation", Json::Float(e0_dev)),
                ("maxInitialEigenResidual", Json::Float(eigen)),
                ("maxSigmaSpinorDeviation", Json::Float(sigma_dev)),
                ("maxSigmaStateDeviation", Json::Float(sigma_state_dev)),
                ("maxEigenspaceLeak", Json::Float(leak)),
                ("maxHilbertNormDrift", Json::Float(hilbert)),
                ("maxKreinNormDrift", Json::Float(krein)),
                ("maxMuDiffRho", Json::Float(mu_rho)),
                ("maxMuDiffP", Json::Float(mu_p)),
                ("maxMuDiffW", Json::Float(mu_w)),
                ("maxMuDiffSigma", Json::Float(mu_sigma)),
                ("maxRhoClosedFormDeviation", Json::Float(rho_dev)),
                ("maxPClosedFormDeviation", Json::Float(p_dev)),
                ("maxWClosedFormDeviation", Json::Float(w_dev)),
                ("maxSplitIdentityDeviation", Json::Float(identity)),
                ("maxRhoZeroRelError", Json::Float(zero_dev)),
                ("maxPhantomCrossingRelError", Json::Float(cross_dev)),
                ("maxDecelerationRootRelError", Json::Float(q_root_dev)),
                ("maxW0Deviation", Json::Float(w0_dev)),
                ("maxWaTangentRelDeviation", Json::Float(wa_dev)),
            ]),
        ),
        ("contractDeviations", Json::Array(deviations)),
        (
            "notes",
            Json::Array(vec![
                Json::str(
                    "sigma = a^-3 exactly: h(t) is a multiple of -i gamma^4, so the rest eigenvector only \
                     acquires the phase Phi = int (M_eff/H0) dN / E; rho, p, w depend on s(u) = 1, not on \
                     the phase, hence not on mu.",
                ),
                Json::str(
                    "For x0 < 0 the attractive four-fermion term makes rho_psi negative for a < |x0|^(1/3) \
                     and E^2 vanishes at a_b (bounce): the model has no matter era and no z > z_b.",
                ),
                Json::str(
                    "w has a pole where rho_psi = 0 and M_eff = 0 at the phantom crossing w = -1 (KE_L = 0); \
                     c_s^2 = 2 x0 sigma/(1 + 2 x0 sigma) is negative today for every x0 < 0 \
                     (gradient instability of perturbations).",
                ),
                Json::str(
                    "CPL fits (w(a) least squares, distance-modulus fits) and the fine x0 scan are done by \
                     scripts/analyze_dirac16complex_exp3.py (fits.json).",
                ),
            ]),
        ),
    ];
    let description = solver(&tolerances, n_max()).describe();
    let doc = standard_summary(ctx, &summary, &tolerances, description, extra);
    write_json(&directory.join("summary.json"), &doc)?;
    summary.add_file("summary.json");
    Ok(summary)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn closure_and_closed_forms() {
        assert!((OMEGA_R + OMEGA_M + OMEGA_PSI - 1.0).abs() <= CLOSURE_LIMIT);
        for &x0 in &X0_VALUES {
            let model = Model { x0, mu: 3.0 };
            assert!((model.e2_closed(0.0) - 1.0).abs() < 1e-15);
            assert!((model.rho_psi(1.0) - OMEGA_PSI).abs() < 1e-15);
            assert!((model.p_psi(1.0) / model.rho_psi(1.0) - model.w0()).abs() < 1e-15);
            if let Some(a0) = model.a_zero() {
                assert!(model.rho_psi(1.0 / (a0 * a0 * a0)).abs() < 1e-12);
                let ac = model.a_cross().unwrap();
                let sigma = 1.0 / (ac * ac * ac);
                assert!((model.rho_psi(sigma) + model.p_psi(sigma)).abs() < 1e-12);
                assert!(model.meff_over_h0(sigma).abs() < 1e-12);
            }
        }
    }

    #[test]
    fn bounce_is_the_root_of_e2() {
        for &x0 in &X0_VALUES[..4] {
            let model = Model { x0, mu: 3.0 };
            let a_b = model.bounce().unwrap();
            assert!(a_b > 1.0 / A_MIN_INVERSE && a_b < 1.0);
            assert!(model.e2_closed(log(a_b)).abs() < 1e-12);
            assert!(model.e2_closed(log(a_b) + 1e-6) > 0.0);
            assert!(model.a_zero().unwrap() > a_b);
        }
        assert!(Model { x0: 0.0, mu: 3.0 }.bounce().is_none());
    }

    #[test]
    fn lagrange_is_exact_on_quartics() {
        let nodes = [-0.02, -0.01, 0.0, 0.013, 0.026];
        let f = |x: f64| 1.0 + 2.0 * x - 3.0 * x * x + 4.0 * x * x * x - 5.0 * x * x * x * x;
        let values: Vec<f64> = nodes.iter().map(|&x| f(x)).collect();
        let (v, d) = lagrange(&nodes, &values, 0.0);
        assert!((v - 1.0).abs() < 1e-13 && (d - 2.0).abs() < 1e-9);
        let roots = sign_change_roots(&[0.0, 1.0, 2.0, 3.0], &[-1.5, -0.5, 0.5, 1.5]);
        assert_eq!(roots.len(), 1);
        assert!((roots[0] - 1.5).abs() < 1e-14);
    }

    #[test]
    fn short_integration_keeps_sigma_and_phase() {
        let alg = Algebra::new();
        let model = Model { x0: -0.3, mu: 3.0 };
        let (u0, residual) = initial_spinor(&alg, model.mu).unwrap();
        assert!(residual < 1e-12);
        let s0 = scalar_density(&alg, &u0);
        let mut y0 = vec![0.0; STATE_SIZE];
        u0.write_state(&mut y0[SPINOR..SPINOR + STATE_REALS]);
        let targets = uniform_targets(0.0, 0.5, 10);
        let cfg = SolverConfig::adams(1e-11, 1e-13, 0.01).with_stop_time(0.5);
        let run = integrate(y0, 0.0, &targets, rhs_for(&alg, model, s0), &cfg).unwrap();
        for (n, y) in run.times.iter().zip(&run.states) {
            let row = observables_row(&alg, &model, s0, *n, 1.0, y);
            assert!((row[col::SIGMA_SPINOR] / row[col::SIGMA_ANALYTIC] - 1.0).abs() < 1e-9);
            assert!((row[col::RHO] - row[col::RHO_CLOSED]).abs() < 1e-9);
            assert!(row[col::LEAK] < 1e-12);
        }
    }
}
