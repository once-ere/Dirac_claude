//! EXP-1 -- primordial (pair-creation) field: the frozen dirac16complex.
//!
//! Background (CONTRACT section 9, t = H x4, H = 1): the notebook field with
//! the primordial-window profile
//! `a4'(t) = A (1 + tanh((t - t1)/D)) (1 - tanh((t - t2)/D)) / 4`,
//! A in {1, 2}, t1 = 2, t2 = 7, D = 0.5, and its exact integral
//! `a4(t) = int_{-inf}^t a4' = A D / (2 (1 - e^{-2(t2-t1)/D}))
//!          [softplus(2(t-t1)/D) - softplus(2(t-t2)/D)]`
//! (from sigma(a) sigma(-b) = (sigma(a) - sigma(b)) / (1 - e^{b-a}) for the
//! logistic sigma).  Scale factors at fixed x0: 3-space e^{a4}, extra times
//! e^{-a4} (the constant s^{1/6} factors are dropped), 7-volume
//! V = e^{3 a4} e^{-3 a4} = const.
//!
//! Sector k = q = 0 with a hidden-space plane wave in zeta = ln(sin z)/(6H):
//! `Psi = e^{-3 H zeta} e^{i K zeta} u(t)` reduces the Dirac equation to
//! `gamma^4 du/dt = (M_eff - i K gamma^0) u`, i.e. `i du/dt = h u` with the
//! mode Hamiltonian `h = -i M_eff gamma^4 - gamma^4 sum_j (k_j/h_j) gamma^j`
//! at k_0/h_0 = K (K is the momentum conjugate to the proper hidden-space
//! length zeta) and k_j/h_j = 0/h_j(t) for the 3-space and extra-time
//! directions.  The a4 dependence enters h only through these zero
//! entries, so the two profiles must give identical spinors (they do,
//! bit for bit, because 0/h = 0 exactly).
//!
//! Mean field: `M_eff = m + lambda S`, `S = S0 s(u)`, `s(u) = u^dagger (-i
//! gamma^4) u` (expectation-value rule), S0 the fixed density (volume)
//! factor; `U(S) = (lambda/2) S^2`.  Per unit mode density n = S0:
//!   rho   = S0 u^dagger h u - (lambda/2) S^2
//!   p_j   = S0 p_j(u) + (lambda/2) S^2,  p_j(u) = -(k_j/h_j) u^dagger gamma^4 gamma^j u
//!   KE_H  = S0 sum_j p_j(u),  PE_H = m S + (lambda/2) S^2  (rho = KE_H + PE_H)
//!   KE_L  = (1/2) K_4 = (1/2) S0 u^dagger h u,  PE_L = rho - KE_L
//! (K_4 = <Psi^dagger B h Psi> on shell; homogeneous rest state:
//! KE_L = S M_eff / 2, PE_L = (m S + 2U - S U')/2 as in NUMERICS_CONTRACT).
//! w = pbar / rho with pbar = (1/7) sum_{j in T} p_j; w_L = (KE_L - PE_L)/rho.
//!
//! Einstein source the field would need (kappa = 1):
//! rho_req = -3H^2(7 + a4'^2), p_req,0 = -3H^2(a4'^2 - 5),
//! p_req,1..3 = H^2(15 - 3a4'^2 + a4''), p_req,5..7 = H^2(15 - 3a4'^2 - a4'').
//!
//! Exact solution (constant M_eff): h is constant with h^2 = E^2 I,
//! u(t) = exp(-i h t) u0 = (cos E t - i sin E t h/E) u0, E = sqrt(M_eff^2 + K^2).

use crate::driver::{integrate, uniform_targets, Integration, RhsFn, SolverConfig};
use crate::math::{exp, softplus, tanh};
use crate::output::{fmt17, standard_summary, write_csv, write_json, Json};
use crate::spinor::{
    energy_projector, energy_squared, exact_propagator, involution_projector, mode_energy,
    mode_pressure, mode_rhs, norm_hilbert, norm_krein, range_basis, scalar_density, Algebra,
    CMat16, CVec16, TRANSVERSE,
};
use crate::{ExperimentSummary, RunContext, Tolerances};

pub const EXPERIMENT: &str = "exp1";
pub const HUBBLE: f64 = 1.0;
pub const MASS: f64 = 1.0;
pub const KAPPA: f64 = 1.0;
pub const T_START: f64 = 0.0;
pub const T_END: f64 = 10.0;
pub const OUTPUT_INTERVALS: usize = 200;
pub const WINDOW_T1: f64 = 2.0;
pub const WINDOW_T2: f64 = 7.0;
pub const WINDOW_WIDTH: f64 = 0.5;
pub const AMPLITUDES: [f64; 2] = [1.0, 2.0];
pub const HIDDEN_MOMENTA: [f64; 3] = [0.0, 0.5, 2.0];
/// Mode density S0 of the lambda = 0 runs.
pub const DENSITY_FREE: f64 = 1.0;
/// The lambda != 0 run: coupling, density S0, hidden momentum K.
pub const LAMBDA_COUPLING: f64 = 0.5;
pub const LAMBDA_DENSITY: f64 = 1.0;
pub const LAMBDA_MOMENTUM: f64 = 0.5;
/// Default tolerances.  The BDF global error measured over the ~1300 steps
/// of one run is ~500 rtol (rtol 1e-10 gives 4e-8 norm drift, above the a
/// priori 1e-8 conservation limit), so the default is rtol = 1e-12.
pub const DEFAULT_TOLERANCES: Tolerances = Tolerances {
    rtol: 1.0e-12,
    atol: 1.0e-14,
    max_step: 0.02,
};
/// Self-check limits (absolute).
pub const EXACT_LIMIT: f64 = 1.0e-7;
pub const FROZEN_LIMIT: f64 = 1.0e-8;
pub const NORM_LIMIT: f64 = 1.0e-8;
pub const PROFILE_LIMIT: f64 = 1.0e-12;
pub const VOLUME_LIMIT: f64 = 1.0e-13;
pub const EIGEN_LIMIT: f64 = 1.0e-12;

/// The primordial-window a4 profile.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Profile {
    pub amplitude: f64,
    pub t1: f64,
    pub t2: f64,
    pub width: f64,
}

impl Profile {
    pub fn new(amplitude: f64) -> Self {
        Self {
            amplitude,
            t1: WINDOW_T1,
            t2: WINDOW_T2,
            width: WINDOW_WIDTH,
        }
    }

    pub fn label(&self) -> String {
        format!("A{}", label_number(self.amplitude))
    }

    pub fn a4_prime(&self, t: f64) -> f64 {
        let t1 = tanh((t - self.t1) / self.width);
        let t2 = tanh((t - self.t2) / self.width);
        self.amplitude * (1.0 + t1) * (1.0 - t2) / 4.0
    }

    pub fn a4_second(&self, t: f64) -> f64 {
        let t1 = tanh((t - self.t1) / self.width);
        let t2 = tanh((t - self.t2) / self.width);
        self.amplitude / (4.0 * self.width)
            * ((1.0 - t1 * t1) * (1.0 - t2) - (1.0 + t1) * (1.0 - t2 * t2))
    }

    pub fn a4(&self, t: f64) -> f64 {
        let d = 2.0 * (self.t2 - self.t1) / self.width;
        let prefactor = self.amplitude * self.width / (2.0 * (1.0 - exp(-d)));
        prefactor
            * (softplus(2.0 * (t - self.t1) / self.width)
                - softplus(2.0 * (t - self.t2) / self.width))
    }
}

/// "0.5" -> "0p5", "2" -> "2".
fn label_number(value: f64) -> String {
    let text = if value == value.trunc() {
        format!("{}", value as i64)
    } else {
        format!("{value}")
    };
    text.replace('.', "p").replace('-', "m")
}

/// Einstein requirement (rho_req, p_req[8]) for kappa = KAPPA (p[4] = 0).
pub fn einstein_requirement(a4p: f64, a4pp: f64) -> (f64, [f64; 8]) {
    let h2 = HUBBLE * HUBBLE;
    let rho = -3.0 * h2 * (7.0 + a4p * a4p) / KAPPA;
    let p0 = -3.0 * h2 * (a4p * a4p - 5.0) / KAPPA;
    let p_space = h2 * (15.0 - 3.0 * a4p * a4p + a4pp) / KAPPA;
    let p_time = h2 * (15.0 - 3.0 * a4p * a4p - a4pp) / KAPPA;
    (
        rho,
        [p0, p_space, p_space, p_space, 0.0, p_time, p_time, p_time],
    )
}

/// k_j / h_j at time t: K along the hidden direction, 0/h_j elsewhere.
pub fn momenta(k_hidden: f64, a4: f64) -> [f64; 8] {
    let scale_space = exp(a4);
    let scale_time = exp(-a4);
    [
        k_hidden,
        0.0 / scale_space,
        0.0 / scale_space,
        0.0 / scale_space,
        0.0,
        0.0 / scale_time,
        0.0 / scale_time,
        0.0 / scale_time,
    ]
}

/// Solve M = m + lambda S0 M / sqrt(M^2 + K^2) (positive-energy eigenmode,
/// s(u) = M/E) by Newton's method from M = m.
pub fn self_consistent_mass(m: f64, lambda: f64, s0: f64, k: f64) -> f64 {
    let mut mass = m;
    for _ in 0..100 {
        let e2 = mass * mass + k * k;
        let e = e2.sqrt();
        let f = mass - m - lambda * s0 * mass / e;
        let df = 1.0 - lambda * s0 * k * k / (e2 * e);
        let step = f / df;
        mass -= step;
        if step == 0.0 {
            break;
        }
    }
    mass
}

#[derive(Clone, Debug)]
struct RunSpec {
    id: String,
    profile: Profile,
    k_hidden: f64,
    lambda: f64,
    density: f64,
    spinor_label: &'static str,
    energy_sign: Option<f64>,
    krein_sign: Option<f64>,
    u0: CVec16,
    m_eff0: f64,
}

#[derive(Clone, Copy, Debug)]
struct Observables {
    s: f64,
    m_eff: f64,
    energy_mode: f64,
    rho: f64,
    p: [f64; 7],
    p_mean: f64,
    w: f64,
    ke_l: f64,
    pe_l: f64,
    ke_h: f64,
    pe_h: f64,
    w_l: f64,
    norm_hilbert: f64,
    norm_krein: f64,
}

fn observables(alg: &Algebra, spec: &RunSpec, a4: f64, u: &CVec16) -> Observables {
    let kh = momenta(spec.k_hidden, a4);
    let s_mode = scalar_density(alg, u);
    let s = spec.density * s_mode;
    let m_eff = MASS + spec.lambda * s;
    let h = alg.mode_hamiltonian(m_eff, &kh);
    let energy_mode = mode_energy(&h, u);
    let lagrangian = 0.5 * spec.lambda * s * s; // S U' - U
    let mut p = [0.0; 7];
    let mut gradient = 0.0;
    for (slot, &j) in TRANSVERSE.iter().enumerate() {
        let pj = mode_pressure(alg, u, kh[j], j);
        gradient += pj;
        p[slot] = spec.density * pj + lagrangian;
    }
    let rho = spec.density * energy_mode - lagrangian;
    let p_mean = p.iter().sum::<f64>() / 7.0;
    let ke_h = spec.density * gradient;
    let pe_h = MASS * s + 0.5 * spec.lambda * s * s;
    let ke_l = 0.5 * spec.density * energy_mode;
    let pe_l = rho - ke_l;
    Observables {
        s,
        m_eff,
        energy_mode,
        rho,
        p,
        p_mean,
        w: p_mean / rho,
        ke_l,
        pe_l,
        ke_h,
        pe_h,
        w_l: (ke_l - pe_l) / (ke_l + pe_l),
        norm_hilbert: norm_hilbert(u),
        norm_krein: norm_krein(alg, u),
    }
}

fn run_header() -> Vec<String> {
    let mut header = vec!["t".to_string()];
    header.extend((0..16).map(|i| format!("u_re_{i}")));
    header.extend((0..16).map(|i| format!("u_im_{i}")));
    for name in ["S", "M_eff", "energy_mode", "rho"] {
        header.push(name.to_string());
    }
    header.extend(TRANSVERSE.iter().map(|j| format!("p_{j}")));
    for name in [
        "p_mean",
        "w",
        "KE_L",
        "PE_L",
        "KE_H",
        "PE_H",
        "w_L",
        "norm_hilbert",
        "norm_krein",
        "exact_error",
    ] {
        header.push(name.to_string());
    }
    header
}

fn background_header() -> Vec<String> {
    [
        "t",
        "a4",
        "a4_prime",
        "a4_second",
        "scale_3space",
        "scale_extratime",
        "volume_ratio",
        "theta",
        "rho_req",
        "p_req_0",
        "p_req_1",
        "p_req_2",
        "p_req_3",
        "p_req_5",
        "p_req_6",
        "p_req_7",
        "p_mean_req",
        "w_req",
    ]
    .iter()
    .map(|s| s.to_string())
    .collect()
}

fn background_row(profile: &Profile, t: f64) -> Vec<f64> {
    let a4 = profile.a4(t);
    let a4p = profile.a4_prime(t);
    let a4pp = profile.a4_second(t);
    let scale_space = exp(a4);
    let scale_time = exp(-a4);
    let volume = scale_space * scale_space * scale_space * scale_time * scale_time * scale_time;
    // H_b = 0, H_a = H a4', H_c = -H a4'
    let theta = 3.0 * HUBBLE * a4p + 3.0 * (-HUBBLE * a4p);
    let (rho, p) = einstein_requirement(a4p, a4pp);
    let p_mean = TRANSVERSE.iter().map(|&j| p[j]).sum::<f64>() / 7.0;
    let mut row = vec![
        t,
        a4,
        a4p,
        a4pp,
        scale_space,
        scale_time,
        volume,
        theta,
        rho,
    ];
    row.extend(TRANSVERSE.iter().map(|&j| p[j]));
    row.push(p_mean);
    row.push(p_mean / rho);
    row
}

/// (label, energy sign, Krein (B) sign, spinor); signs are None for the
/// generic superposition.
type InitialSpinor = (&'static str, Option<f64>, Option<f64>, CVec16);

fn initial_spinors(alg: &Algebra, m_eff: f64, k: f64) -> Result<Vec<InitialSpinor>, String> {
    let kh = [k, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    let h = alg.mode_hamiltonian(m_eff, &kh);
    let e = energy_squared(m_eff, &kh).sqrt();
    let pick = |esign: f64, bsign: f64| -> Result<CVec16, String> {
        let projector = energy_projector(&h, e, esign).mul(&involution_projector(&alg.b, bsign));
        range_basis(&projector, 1.0e-8)
            .first()
            .copied()
            .ok_or_else(|| "empty joint eigenspace".to_string())
    };
    let mut mix = CVec16::zero();
    for i in 0..16 {
        mix.re[i] = 1.0 + 0.1 * i as f64;
        mix.im[i] = 0.3 - 0.05 * i as f64;
    }
    let mix = mix.scale(1.0 / mix.norm2().sqrt(), 0.0);
    Ok(vec![
        ("pos_Bp", Some(1.0), Some(1.0), pick(1.0, 1.0)?),
        ("pos_Bm", Some(1.0), Some(-1.0), pick(1.0, -1.0)?),
        ("neg_Bp", Some(-1.0), Some(1.0), pick(-1.0, 1.0)?),
        ("mix", None, None, mix),
    ])
}

fn build_runs(alg: &Algebra) -> Result<Vec<RunSpec>, String> {
    let mut runs = Vec::new();
    for &amplitude in &AMPLITUDES {
        let profile = Profile::new(amplitude);
        for &k in &HIDDEN_MOMENTA {
            for (label, esign, bsign, u0) in initial_spinors(alg, MASS, k)? {
                runs.push(RunSpec {
                    id: format!("{}_K{}_{}", profile.label(), label_number(k), label),
                    profile,
                    k_hidden: k,
                    lambda: 0.0,
                    density: DENSITY_FREE,
                    spinor_label: label,
                    energy_sign: esign,
                    krein_sign: bsign,
                    u0,
                    m_eff0: MASS,
                });
            }
        }
        let m_star = self_consistent_mass(MASS, LAMBDA_COUPLING, LAMBDA_DENSITY, LAMBDA_MOMENTUM);
        let spinors = initial_spinors(alg, m_star, LAMBDA_MOMENTUM)?;
        let (label, esign, bsign, u0) = spinors[0];
        runs.push(RunSpec {
            id: format!(
                "{}_K{}_{}_lambda{}",
                profile.label(),
                label_number(LAMBDA_MOMENTUM),
                label,
                label_number(LAMBDA_COUPLING)
            ),
            profile,
            k_hidden: LAMBDA_MOMENTUM,
            lambda: LAMBDA_COUPLING,
            density: LAMBDA_DENSITY,
            spinor_label: label,
            energy_sign: esign,
            krein_sign: bsign,
            u0,
            m_eff0: m_star,
        });
    }
    Ok(runs)
}

fn rhs_for(alg: &Algebra, spec: &RunSpec) -> RhsFn {
    let alg = alg.clone();
    let profile = spec.profile;
    let k = spec.k_hidden;
    let lambda = spec.lambda;
    let density = spec.density;
    Box::new(move |t, y, ydot| {
        let kh = momenta(k, profile.a4(t));
        let m_eff = if lambda != 0.0 {
            MASS + lambda * density * scalar_density(&alg, &CVec16::from_state(y))
        } else {
            MASS
        };
        let h = alg.mode_hamiltonian(m_eff, &kh);
        mode_rhs(&h, y, ydot);
        Ok(())
    })
}

struct RunOutcome {
    spec: RunSpec,
    file: String,
    integration: Integration,
    rows: Vec<Vec<f64>>,
    energy: f64,
    max_exact: f64,
    drift_rho: f64,
    drift_p: f64,
    drift_s: f64,
    drift_hilbert: f64,
    drift_krein: f64,
    range_p: f64,
    drift_meff: f64,
    eigen_residual: f64,
    first: Observables,
}

fn execute(
    alg: &Algebra,
    spec: RunSpec,
    cfg: &SolverConfig,
    targets: &[f64],
) -> Result<RunOutcome, String> {
    let integration = integrate(
        spec.u0.to_state(),
        T_START,
        targets,
        rhs_for(alg, &spec),
        cfg,
    )
    .map_err(|error| format!("run {}: {error}", spec.id))?;
    let kh0 = [spec.k_hidden, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
    let h0: CMat16 = alg.mode_hamiltonian(spec.m_eff0, &kh0);
    let energy = energy_squared(spec.m_eff0, &kh0).sqrt();
    let eigen_residual = match (spec.energy_sign, spec.krein_sign) {
        (Some(esign), Some(bsign)) => {
            let hu = h0.apply(&spec.u0);
            let bu = alg.b.apply(&spec.u0);
            hu.max_abs_diff(&spec.u0.scale(esign * energy, 0.0))
                .max(bu.max_abs_diff(&spec.u0.scale(bsign, 0.0)))
        }
        _ => 0.0,
    };
    let mut rows = Vec::with_capacity(integration.times.len());
    let mut first: Option<Observables> = None;
    let (mut max_exact, mut drift_rho, mut drift_p, mut drift_s) = (0.0f64, 0.0f64, 0.0f64, 0.0f64);
    let (mut drift_hilbert, mut drift_krein, mut drift_meff) = (0.0f64, 0.0f64, 0.0f64);
    let mut p_min = [f64::INFINITY; 7];
    let mut p_max = [f64::NEG_INFINITY; 7];
    for (t, state) in integration.times.iter().zip(&integration.states) {
        let u = CVec16::from_state(state);
        let obs = observables(alg, &spec, spec.profile.a4(*t), &u);
        let exact = exact_propagator(&h0, energy, *t - T_START).apply(&spec.u0);
        let error = u.distance(&exact);
        max_exact = max_exact.max(error);
        let reference = *first.get_or_insert(obs);
        drift_rho = drift_rho.max((obs.rho - reference.rho).abs());
        drift_s = drift_s.max((obs.s - reference.s).abs());
        drift_hilbert = drift_hilbert.max((obs.norm_hilbert - reference.norm_hilbert).abs());
        drift_krein = drift_krein.max((obs.norm_krein - reference.norm_krein).abs());
        drift_meff = drift_meff.max((obs.m_eff - spec.m_eff0).abs());
        for slot in 0..7 {
            drift_p = drift_p.max((obs.p[slot] - reference.p[slot]).abs());
            p_min[slot] = p_min[slot].min(obs.p[slot]);
            p_max[slot] = p_max[slot].max(obs.p[slot]);
        }
        let mut row = vec![*t];
        row.extend_from_slice(state);
        row.extend([obs.s, obs.m_eff, obs.energy_mode, obs.rho]);
        row.extend_from_slice(&obs.p);
        row.extend([
            obs.p_mean,
            obs.w,
            obs.ke_l,
            obs.pe_l,
            obs.ke_h,
            obs.pe_h,
            obs.w_l,
            obs.norm_hilbert,
            obs.norm_krein,
            error,
        ]);
        rows.push(row);
    }
    let range_p = (0..7)
        .map(|slot| p_max[slot] - p_min[slot])
        .fold(0.0, f64::max);
    let file = format!("run_{}.csv", spec.id);
    Ok(RunOutcome {
        first: first.ok_or_else(|| "no samples".to_string())?,
        spec,
        file,
        integration,
        rows,
        energy,
        max_exact,
        drift_rho,
        drift_p,
        drift_s,
        drift_hilbert,
        drift_krein,
        range_p,
        drift_meff,
        eigen_residual,
    })
}

fn optional_sign(value: Option<f64>) -> Json {
    value.map(Json::Float).unwrap_or(Json::Null)
}

fn run_json(outcome: &RunOutcome) -> Json {
    let spec = &outcome.spec;
    let run = &outcome.integration;
    let obs = &outcome.first;
    Json::object(vec![
        ("id", Json::str(&spec.id)),
        ("file", Json::str(&outcome.file)),
        ("profile", Json::str(&spec.profile.label())),
        ("amplitude", Json::Float(spec.profile.amplitude)),
        ("hiddenMomentumK", Json::Float(spec.k_hidden)),
        ("lambda", Json::Float(spec.lambda)),
        ("density", Json::Float(spec.density)),
        ("initialSpinor", Json::str(spec.spinor_label)),
        ("energySign", optional_sign(spec.energy_sign)),
        ("kreinSign", optional_sign(spec.krein_sign)),
        ("mEff", Json::Float(spec.m_eff0)),
        ("energyE", Json::Float(outcome.energy)),
        ("initialEigenResidual", Json::Float(outcome.eigen_residual)),
        (
            "initial",
            Json::object(vec![
                ("S", Json::Float(obs.s)),
                ("rho", Json::Float(obs.rho)),
                ("p", Json::floats(&obs.p)),
                ("pMean", Json::Float(obs.p_mean)),
                ("w", Json::Float(obs.w)),
                ("KE_L", Json::Float(obs.ke_l)),
                ("PE_L", Json::Float(obs.pe_l)),
                ("KE_H", Json::Float(obs.ke_h)),
                ("PE_H", Json::Float(obs.pe_h)),
                ("w_L", Json::Float(obs.w_l)),
                ("normHilbert", Json::Float(obs.norm_hilbert)),
                ("normKrein", Json::Float(obs.norm_krein)),
            ]),
        ),
        (
            "maxAbsDrift",
            Json::object(vec![
                ("rho", Json::Float(outcome.drift_rho)),
                ("pressures", Json::Float(outcome.drift_p)),
                ("S", Json::Float(outcome.drift_s)),
                ("mEff", Json::Float(outcome.drift_meff)),
                ("normHilbert", Json::Float(outcome.drift_hilbert)),
                ("normKrein", Json::Float(outcome.drift_krein)),
            ]),
        ),
        ("pressureRange", Json::Float(outcome.range_p)),
        ("maxExactError", Json::Float(outcome.max_exact)),
        (
            "solver",
            Json::object(vec![
                ("steps", Json::Int(run.steps)),
                ("rhsEvals", Json::Int(run.rhs_evals)),
                ("linRhsEvals", Json::Int(run.lin_rhs_evals)),
                ("jacEvals", Json::Int(run.jac_evals)),
                ("linSetups", Json::Int(run.lin_setups)),
                ("errTestFails", Json::Int(run.err_test_fails)),
                ("nonlinIters", Json::Int(run.nonlin_iters)),
                ("nonlinConvFails", Json::Int(run.nonlin_conv_fails)),
            ]),
        ),
    ])
}

/// Configuration lines for `print-config`.
pub fn config_lines() -> Vec<String> {
    vec![
        format!(
            "exp1: H = {}, m = {}, kappa = {}",
            fmt17(HUBBLE),
            fmt17(MASS),
            fmt17(KAPPA)
        ),
        format!(
            "exp1: a4' window t1 = {}, t2 = {}, width = {}, amplitudes A = {:?}",
            fmt17(WINDOW_T1),
            fmt17(WINDOW_T2),
            fmt17(WINDOW_WIDTH),
            AMPLITUDES
        ),
        format!("exp1: hidden momenta K = {HIDDEN_MOMENTA:?}; spinors pos_Bp, pos_Bm, neg_Bp, mix"),
        format!(
            "exp1: lambda run lambda = {}, S0 = {}, K = {}",
            fmt17(LAMBDA_COUPLING),
            fmt17(LAMBDA_DENSITY),
            fmt17(LAMBDA_MOMENTUM)
        ),
        format!(
            "exp1: t in [{}, {}], {} output intervals",
            fmt17(T_START),
            fmt17(T_END),
            OUTPUT_INTERVALS
        ),
        format!(
            "exp1: default rtol = {}, atol = {}, max_step = {}, method BDF + Newton + dense",
            fmt17(DEFAULT_TOLERANCES.rtol),
            fmt17(DEFAULT_TOLERANCES.atol),
            fmt17(DEFAULT_TOLERANCES.max_step)
        ),
    ]
}

/// Run EXP-1.
pub fn run(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let directory = ctx.experiment_dir(EXPERIMENT)?;
    let tolerances = ctx.tolerances(DEFAULT_TOLERANCES);
    let cfg = SolverConfig::bdf(tolerances.rtol, tolerances.atol, tolerances.max_step)
        .with_stop_time(T_END);
    let targets = uniform_targets(T_START, T_END, OUTPUT_INTERVALS);
    let mut grid = vec![T_START];
    grid.extend_from_slice(&targets);
    let alg = Algebra::new();
    let mut summary = ExperimentSummary::new(EXPERIMENT);

    // Backgrounds.
    let mut background_json = Vec::new();
    let mut rho_req_max = f64::NEG_INFINITY;
    let mut volume_defect = 0.0f64;
    for &amplitude in &AMPLITUDES {
        let profile = Profile::new(amplitude);
        let rows: Vec<Vec<f64>> = grid.iter().map(|&t| background_row(&profile, t)).collect();
        let file = format!("background_{}.csv", profile.label());
        write_csv(&directory.join(&file), &background_header(), &rows)?;
        summary.add_file(&file);
        let column = |index: usize| rows.iter().map(move |row| row[index]);
        let rho_max = column(8).fold(f64::NEG_INFINITY, f64::max);
        let rho_min = column(8).fold(f64::INFINITY, f64::min);
        let w_min = column(17).fold(f64::INFINITY, f64::min);
        let w_max = column(17).fold(f64::NEG_INFINITY, f64::max);
        let a4_final = rows[rows.len() - 1][1];
        rho_req_max = rho_req_max.max(rho_max);
        volume_defect = column(6).fold(volume_defect, |acc, v| acc.max((v - 1.0).abs()));
        background_json.push(Json::object(vec![
            ("profile", Json::str(&profile.label())),
            ("file", Json::str(&file)),
            ("amplitude", Json::Float(amplitude)),
            ("a4Final", Json::Float(a4_final)),
            ("rhoReqMin", Json::Float(rho_min)),
            ("rhoReqMax", Json::Float(rho_max)),
            ("wReqMin", Json::Float(w_min)),
            ("wReqMax", Json::Float(w_max)),
        ]));
    }

    // Spinor runs.
    let specs = build_runs(&alg)?;
    let mut outcomes = Vec::with_capacity(specs.len());
    for spec in specs {
        let outcome = execute(&alg, spec, &cfg, &targets)?;
        write_csv(&directory.join(&outcome.file), &run_header(), &outcome.rows)?;
        summary.add_file(&outcome.file);
        summary.add_stats(outcome.integration.steps, outcome.integration.rhs_evals);
        outcomes.push(outcome);
    }

    // Profile independence: every A2 run against its A1 twin.
    let mut profile_difference = 0.0f64;
    let mut pairs = 0usize;
    for outcome in &outcomes {
        if outcome.spec.profile.amplitude != AMPLITUDES[0] {
            continue;
        }
        let twin_id = outcome.spec.id.replacen(
            &outcome.spec.profile.label(),
            &Profile::new(AMPLITUDES[1]).label(),
            1,
        );
        let twin = outcomes
            .iter()
            .find(|other| other.spec.id == twin_id)
            .ok_or_else(|| format!("missing twin run {twin_id}"))?;
        for (a, b) in outcome
            .integration
            .states
            .iter()
            .zip(&twin.integration.states)
        {
            for (x, y) in a.iter().zip(b) {
                profile_difference = profile_difference.max((x - y).abs());
            }
        }
        pairs += 1;
    }

    let max_of = |f: &dyn Fn(&RunOutcome) -> f64, only_eigen: bool| {
        outcomes
            .iter()
            .filter(|o| !only_eigen || o.spec.energy_sign.is_some())
            .map(f)
            .fold(0.0f64, f64::max)
    };
    let max_exact = max_of(&|o| o.max_exact, false);
    let max_rho = max_of(&|o| o.drift_rho, false);
    let max_p_eigen = max_of(&|o| o.drift_p, true);
    let max_s_eigen = max_of(&|o| o.drift_s, true);
    let max_hilbert = max_of(&|o| o.drift_hilbert, false);
    let max_krein = max_of(&|o| o.drift_krein, false);
    let max_eigen_residual = max_of(&|o| o.eigen_residual, true);
    let max_meff_lambda = outcomes
        .iter()
        .filter(|o| o.spec.lambda != 0.0)
        .map(|o| o.drift_meff)
        .fold(0.0f64, f64::max);
    let mixed_range = outcomes
        .iter()
        .filter(|o| o.spec.energy_sign.is_none() && o.spec.k_hidden != 0.0)
        .map(|o| o.range_p)
        .fold(0.0f64, f64::max);

    summary.check(
        "exact_solution_all_runs",
        max_exact <= EXACT_LIMIT,
        &format!(
            "max |u - exp(-iht)u0| = {} (limit {})",
            fmt17(max_exact),
            fmt17(EXACT_LIMIT)
        ),
    );
    summary.check(
        "rho_frozen_all_runs",
        max_rho <= FROZEN_LIMIT,
        &format!("max |rho(t) - rho(0)| = {}", fmt17(max_rho)),
    );
    summary.check(
        "pressures_and_S_frozen_eigenstate_runs",
        max_p_eigen <= FROZEN_LIMIT && max_s_eigen <= FROZEN_LIMIT,
        &format!(
            "max |p_j(t) - p_j(0)| = {}, max |S(t) - S(0)| = {}",
            fmt17(max_p_eigen),
            fmt17(max_s_eigen)
        ),
    );
    summary.check(
        "hilbert_norm_conserved",
        max_hilbert <= NORM_LIMIT,
        &format!("max |u^dag u - 1| drift = {}", fmt17(max_hilbert)),
    );
    summary.check(
        "krein_norm_conserved",
        max_krein <= NORM_LIMIT,
        &format!("max |u^dag B u| drift = {}", fmt17(max_krein)),
    );
    summary.check(
        "a4_profile_independence",
        pairs * 2 == outcomes.len() && profile_difference <= PROFILE_LIMIT,
        &format!(
            "{pairs} run pairs, max |state_A1 - state_A2| = {}",
            fmt17(profile_difference)
        ),
    );
    summary.check(
        "einstein_source_negative_energy",
        rho_req_max < 0.0,
        &format!("max rho_req = {}", fmt17(rho_req_max)),
    );
    summary.check(
        "seven_volume_constant",
        volume_defect <= VOLUME_LIMIT,
        &format!("max |V/V0 - 1| = {}", fmt17(volume_defect)),
    );
    summary.check(
        "initial_joint_eigenvectors",
        max_eigen_residual <= EIGEN_LIMIT,
        &format!(
            "max |h u0 - E u0|, |B u0 - b u0| = {}",
            fmt17(max_eigen_residual)
        ),
    );
    summary.check(
        "lambda_run_meff_constant",
        max_meff_lambda <= FROZEN_LIMIT,
        &format!("max |M_eff(t) - M*| = {}", fmt17(max_meff_lambda)),
    );

    let m_star = self_consistent_mass(MASS, LAMBDA_COUPLING, LAMBDA_DENSITY, LAMBDA_MOMENTUM);
    let extra = vec![
        (
            "parameters",
            Json::object(vec![
                ("H", Json::Float(HUBBLE)),
                ("m", Json::Float(MASS)),
                ("kappa", Json::Float(KAPPA)),
                ("windowT1", Json::Float(WINDOW_T1)),
                ("windowT2", Json::Float(WINDOW_T2)),
                ("windowWidth", Json::Float(WINDOW_WIDTH)),
                ("amplitudes", Json::floats(&AMPLITUDES)),
                ("hiddenMomenta", Json::floats(&HIDDEN_MOMENTA)),
                ("densityFree", Json::Float(DENSITY_FREE)),
                ("lambdaCoupling", Json::Float(LAMBDA_COUPLING)),
                ("lambdaDensity", Json::Float(LAMBDA_DENSITY)),
                ("lambdaMomentum", Json::Float(LAMBDA_MOMENTUM)),
                ("lambdaSelfConsistentMass", Json::Float(m_star)),
            ]),
        ),
        (
            "grid",
            Json::object(vec![
                ("tStart", Json::Float(T_START)),
                ("tEnd", Json::Float(T_END)),
                ("outputIntervals", Json::Int(OUTPUT_INTERVALS as i64)),
                ("sampleCount", Json::Int(grid.len() as i64)),
            ]),
        ),
        (
            "stateLayout",
            Json::str("u_re_0..u_re_15, u_im_0..u_im_15 (u = re + i im in C^16)"),
        ),
        (
            "limits",
            Json::object(vec![
                ("exact", Json::Float(EXACT_LIMIT)),
                ("frozen", Json::Float(FROZEN_LIMIT)),
                ("norm", Json::Float(NORM_LIMIT)),
                ("profile", Json::Float(PROFILE_LIMIT)),
                ("volume", Json::Float(VOLUME_LIMIT)),
                ("eigen", Json::Float(EIGEN_LIMIT)),
            ]),
        ),
        ("backgrounds", Json::Array(background_json)),
        ("runs", Json::Array(outcomes.iter().map(run_json).collect())),
        (
            "measurements",
            Json::object(vec![
                ("maxExactError", Json::Float(max_exact)),
                ("maxRhoDrift", Json::Float(max_rho)),
                ("maxPressureDriftEigenstates", Json::Float(max_p_eigen)),
                ("maxScalarDensityDriftEigenstates", Json::Float(max_s_eigen)),
                ("maxHilbertNormDrift", Json::Float(max_hilbert)),
                ("maxKreinNormDrift", Json::Float(max_krein)),
                ("maxProfileDifference", Json::Float(profile_difference)),
                ("maxRhoReq", Json::Float(rho_req_max)),
                ("maxVolumeDefect", Json::Float(volume_defect)),
                ("maxLambdaMeffDrift", Json::Float(max_meff_lambda)),
                ("mixedStatePressureRange", Json::Float(mixed_range)),
            ]),
        ),
        (
            "notes",
            Json::Array(vec![
                Json::str(
                    "rho = S0 u^dag h u is frozen for every initial spinor (h constant and Hermitian).",
                ),
                Json::str(
                    "Pressures and S are frozen for energy eigenstates only; for the mixed state with \
                     K != 0 they oscillate at frequency 2E (interference of the +E and -E sectors), \
                     exactly as the exact solution predicts (mixedStatePressureRange).",
                ),
                Json::str(
                    "The a4 profile enters h only through k_j/h_j with k_j = 0, so both profiles give \
                     bit-identical spinors; the Einstein source rho_req is negative throughout.",
                ),
            ]),
        ),
    ];
    let doc = standard_summary(ctx, &summary, &tolerances, cfg.describe(), extra);
    write_json(&directory.join("summary.json"), &doc)?;
    summary.add_file("summary.json");
    Ok(summary)
}
