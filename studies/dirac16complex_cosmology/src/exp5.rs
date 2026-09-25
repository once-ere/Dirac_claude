//! EXP-5 -- the extra-time sector: the ultrahyperbolic instability.
//!
//! Primordial deflation of the extra times, c(t) = h_5 = h_6 = h_7 = e^{-H t}
//! (H = 1), and a mode with extra-time momentum q along x5 (k = 0, m = 1):
//! k_5/h_5 = Q(t) = q e^{H t}, so
//! `h(t) = -i m gamma^4 - Q(t) gamma^4 gamma^5` and
//! `h^2 = E^2(t) I` with `E^2 = m^2 - Q^2 = m^2 - q^2 e^{2Ht}`, which turns
//! negative at `t* = ln(m/q)/H`.  h is not Hermitian (gamma^4 gamma^5 is
//! real antisymmetric) but it is B-pseudo-Hermitian (`h^dagger B = B h`), so
//! the Krein norm u^dagger B u is conserved exactly while the Hilbert norm
//! u^dagger u is not; for t > t* it grows super-exponentially.
//!
//! WKB: with kappa(t) = sqrt(Q^2 - m^2) (t > t*),
//! `W(t) = int_{t*}^t kappa dt' = (1/H) [sqrt(Q^2 - m^2) - m arccos(m/Q)]`.
//! Leading order: d ln(u^dagger u)/dt = 2 kappa.  First adiabatic order
//! (derived from the 2x2 reduction h = m sigma_z + Q i sigma_y (x) I_8, the
//! right/left eigenvectors of the growing mode and the |v|^2 = 2Q^2
//! normalisation): d ln(u^dagger u)/dt = 2 kappa - m^2/kappa^2 (H = 1), whose
//! integral is 2 W - (1/2) ln(1 - m^2/Q^2).  Both are compared over the window
//! [t* + 1.5, t* + 3] (away from the turning point, where WKB fails).
//!
//! Initial spinor: positive-energy eigenvector of h(0) (E0 = sqrt(m^2 - q^2))
//! that is also a C = +-1 eigenvector (C commutes with h(t) for momentum
//! along x5), so u^dagger B u = +- E0/m != 0.
//!
//! Krein drift: in float64, u^dagger B u is an O(1) difference of O(u^dagger
//! u) ~ 1e16 terms at the end, so its absolute value cannot be computed
//! better than ~1e-16 u^dagger u.  The conservation check therefore uses the
//! drift normalised by max(u^dagger u, 1) (identical to the absolute drift
//! while u^dagger u <= 1), plus the absolute drift up to t*.

use crate::driver::{integrate, uniform_targets, Integration, RhsFn, SolverConfig};
use crate::math::{acos, exp, log};
use crate::output::{fmt17, standard_summary, write_csv, write_json, Json};
use crate::spinor::{
    energy_projector, energy_squared, involution_projector, mode_rhs, norm_hilbert, norm_krein,
    range_basis, Algebra, CMat16, CVec16,
};
use crate::{ExperimentSummary, RunContext, Tolerances};

pub const EXPERIMENT: &str = "exp5";
pub const HUBBLE: f64 = 1.0;
pub const MASS: f64 = 1.0;
pub const Q_VALUES: [f64; 2] = [0.05, 0.1];
pub const C_SIGNS: [f64; 2] = [1.0, -1.0];
/// t_end = t* + EXTRA_TIME.
pub const EXTRA_TIME: f64 = 3.0;
pub const OUTPUT_INTERVALS: usize = 600;
/// WKB comparison window [t* + WINDOW_START, t_end].
pub const WINDOW_START: f64 = 1.5;
pub const DEFAULT_TOLERANCES: Tolerances = Tolerances {
    rtol: 1.0e-10,
    atol: 1.0e-12,
    max_step: 0.02,
};
/// Relative tolerance of the leading-order WKB growth comparison.  The
/// neglected first-order term int m^2/kappa^2 dt is ~0.024 against a growth
/// exponent ~31 (0.08 %); the budget adds the transient (decaying mode) and
/// higher adiabatic orders.
pub const WKB0_LIMIT: f64 = 1.0e-2;
/// Relative tolerance of the first-order WKB growth comparison.
pub const WKB1_LIMIT: f64 = 2.0e-3;
/// Normalised Krein drift limit.
pub const KREIN_LIMIT: f64 = 1.0e-8;
pub const EIGEN_LIMIT: f64 = 1.0e-12;

/// t* = ln(m/q)/H.
pub fn turning_time(q: f64) -> f64 {
    log(MASS / q) / HUBBLE
}

/// Q(t) = k_5/h_5 = q e^{H t}.
pub fn extra_time_momentum(q: f64, t: f64) -> f64 {
    q * exp(HUBBLE * t)
}

/// W(t) = int_{t*}^t sqrt(Q^2 - m^2) dt' (0 for t <= t*).
pub fn wkb_integral(q: f64, t: f64) -> f64 {
    let big_q = extra_time_momentum(q, t);
    if big_q <= MASS {
        0.0
    } else {
        ((big_q * big_q - MASS * MASS).sqrt() - MASS * acos(MASS / big_q)) / HUBBLE
    }
}

fn momenta(q: f64, t: f64) -> [f64; 8] {
    [0.0, 0.0, 0.0, 0.0, 0.0, extra_time_momentum(q, t), 0.0, 0.0]
}

#[derive(Clone, Debug)]
struct RunSpec {
    id: String,
    q: f64,
    c_sign: f64,
    t_star: f64,
    t_end: f64,
    energy0: f64,
    u0: CVec16,
    eigen_residual: f64,
}

fn label_q(q: f64) -> String {
    format!("{q}").replace('.', "p")
}

fn build_runs(alg: &Algebra) -> Result<Vec<RunSpec>, String> {
    let charge = CMat16::from_real(&alg.charge);
    let mut runs = Vec::new();
    for &q in &Q_VALUES {
        let kh = momenta(q, 0.0);
        let h0 = alg.mode_hamiltonian(MASS, &kh);
        let energy0 = energy_squared(MASS, &kh).sqrt();
        for &c_sign in &C_SIGNS {
            let projector =
                energy_projector(&h0, energy0, 1.0).mul(&involution_projector(&charge, c_sign));
            let u0 = *range_basis(&projector, 1.0e-8)
                .first()
                .ok_or_else(|| "empty (E0, C) eigenspace".to_string())?;
            let residual = h0
                .apply(&u0)
                .max_abs_diff(&u0.scale(energy0, 0.0))
                .max(charge.apply(&u0).max_abs_diff(&u0.scale(c_sign, 0.0)));
            let t_star = turning_time(q);
            runs.push(RunSpec {
                id: format!("q{}_C{}", label_q(q), if c_sign > 0.0 { "p" } else { "m" }),
                q,
                c_sign,
                t_star,
                t_end: t_star + EXTRA_TIME,
                energy0,
                u0,
                eigen_residual: residual,
            });
        }
    }
    Ok(runs)
}

fn rhs_for(alg: &Algebra, q: f64) -> RhsFn {
    let alg = alg.clone();
    Box::new(move |t, y, ydot| {
        let h = alg.mode_hamiltonian(MASS, &momenta(q, t));
        mode_rhs(&h, y, ydot);
        Ok(())
    })
}

fn header() -> Vec<String> {
    let mut header: Vec<String> = ["t", "Q", "E2", "kappa", "wkb_W"]
        .iter()
        .map(|s| s.to_string())
        .collect();
    header.extend((0..16).map(|i| format!("u_re_{i}")));
    header.extend((0..16).map(|i| format!("u_im_{i}")));
    for name in [
        "norm_hilbert",
        "norm_krein",
        "ln_norm_hilbert",
        "krein_drift",
        "krein_drift_normalized",
    ] {
        header.push(name.to_string());
    }
    header
}

struct RunOutcome {
    spec: RunSpec,
    file: String,
    integration: Integration,
    rows: Vec<Vec<f64>>,
    krein0: f64,
    max_drift_abs: f64,
    max_drift_normalized: f64,
    max_drift_before_tstar: f64,
    window: (f64, f64),
    gamma_num: f64,
    gamma_wkb0: f64,
    gamma_wkb1: f64,
    rate_early: f64,
    rate_late: f64,
    sign_change_ok: bool,
    final_norm: f64,
}

fn index_at_or_after(times: &[f64], t: f64) -> usize {
    times
        .iter()
        .position(|&x| x >= t)
        .unwrap_or(times.len() - 1)
}

fn execute(
    alg: &Algebra,
    spec: RunSpec,
    tolerances: &Tolerances,
) -> Result<(RunOutcome, &'static str), String> {
    let cfg = SolverConfig::adams(tolerances.rtol, tolerances.atol, tolerances.max_step)
        .with_stop_time(spec.t_end);
    let targets = uniform_targets(0.0, spec.t_end, OUTPUT_INTERVALS);
    let integration = integrate(
        spec.u0.to_state(),
        0.0,
        &targets,
        rhs_for(alg, spec.q),
        &cfg,
    )
    .map_err(|error| format!("run {}: {error}", spec.id))?;
    let krein0 = norm_krein(alg, &spec.u0);
    let mut rows = Vec::with_capacity(integration.times.len());
    let mut ln_norms = Vec::with_capacity(integration.times.len());
    let (mut max_abs, mut max_norm, mut max_before) = (0.0f64, 0.0f64, 0.0f64);
    let mut sign_change_ok = true;
    for (t, state) in integration.times.iter().zip(&integration.states) {
        let u = CVec16::from_state(state);
        let big_q = extra_time_momentum(spec.q, *t);
        let e2 = energy_squared(MASS, &momenta(spec.q, *t));
        let kappa = if e2 < 0.0 { (-e2).sqrt() } else { 0.0 };
        let hilbert = norm_hilbert(&u);
        let krein = norm_krein(alg, &u);
        let drift = krein - krein0;
        let normalized = drift / hilbert.max(1.0);
        max_abs = max_abs.max(drift.abs());
        max_norm = max_norm.max(normalized.abs());
        if *t <= spec.t_star {
            max_before = max_before.max(drift.abs());
        }
        if (*t < spec.t_star && e2 <= 0.0) || (*t > spec.t_star && e2 >= 0.0) {
            sign_change_ok = false;
        }
        let ln_norm = log(hilbert);
        ln_norms.push(ln_norm);
        let mut row = vec![*t, big_q, e2, kappa, wkb_integral(spec.q, *t)];
        row.extend_from_slice(state);
        row.extend([hilbert, krein, ln_norm, drift, normalized]);
        rows.push(row);
    }
    let times = &integration.times;
    let last = times.len() - 1;
    let ia = index_at_or_after(times, spec.t_star + WINDOW_START);
    let (ta, tb) = (times[ia], times[last]);
    let gamma_num = ln_norms[last] - ln_norms[ia];
    let gamma_wkb0 = 2.0 * (wkb_integral(spec.q, tb) - wkb_integral(spec.q, ta));
    let qa = extra_time_momentum(spec.q, ta);
    let qb = extra_time_momentum(spec.q, tb);
    let first_order =
        0.5 * (log(1.0 - MASS * MASS / (qb * qb)) - log(1.0 - MASS * MASS / (qa * qa))) / HUBBLE;
    let gamma_wkb1 = gamma_wkb0 - first_order;
    // average growth rates of ln(u^dag u) just after t* and at the end
    let i0 = index_at_or_after(times, spec.t_star);
    let i1 = index_at_or_after(times, spec.t_star + 1.0);
    let i2 = index_at_or_after(times, spec.t_star + 2.0);
    let rate_early = (ln_norms[i1] - ln_norms[i0]) / (times[i1] - times[i0]);
    let rate_late = (ln_norms[last] - ln_norms[i2]) / (times[last] - times[i2]);
    let final_norm = rows[last][37];
    let file = format!("run_{}.csv", spec.id);
    Ok((
        RunOutcome {
            spec,
            file,
            integration,
            rows,
            krein0,
            max_drift_abs: max_abs,
            max_drift_normalized: max_norm,
            max_drift_before_tstar: max_before,
            window: (ta, tb),
            gamma_num,
            gamma_wkb0,
            gamma_wkb1,
            rate_early,
            rate_late,
            sign_change_ok,
            final_norm,
        },
        cfg.describe(),
    ))
}

fn run_json(o: &RunOutcome) -> Json {
    let run = &o.integration;
    Json::object(vec![
        ("id", Json::str(&o.spec.id)),
        ("file", Json::str(&o.file)),
        ("q", Json::Float(o.spec.q)),
        ("cSign", Json::Float(o.spec.c_sign)),
        ("tStar", Json::Float(o.spec.t_star)),
        ("tEnd", Json::Float(o.spec.t_end)),
        ("energy0", Json::Float(o.spec.energy0)),
        ("initialEigenResidual", Json::Float(o.spec.eigen_residual)),
        ("kreinNorm0", Json::Float(o.krein0)),
        ("finalNormHilbert", Json::Float(o.final_norm)),
        (
            "kreinDrift",
            Json::object(vec![
                ("maxAbs", Json::Float(o.max_drift_abs)),
                ("maxNormalized", Json::Float(o.max_drift_normalized)),
                ("maxAbsBeforeTStar", Json::Float(o.max_drift_before_tstar)),
            ]),
        ),
        (
            "wkb",
            Json::object(vec![
                ("tA", Json::Float(o.window.0)),
                ("tB", Json::Float(o.window.1)),
                ("gammaNumeric", Json::Float(o.gamma_num)),
                ("gammaLeading", Json::Float(o.gamma_wkb0)),
                ("gammaFirstOrder", Json::Float(o.gamma_wkb1)),
                (
                    "relDevLeading",
                    Json::Float((o.gamma_num - o.gamma_wkb0) / o.gamma_wkb0),
                ),
                (
                    "relDevFirstOrder",
                    Json::Float((o.gamma_num - o.gamma_wkb1) / o.gamma_wkb1),
                ),
            ]),
        ),
        ("rateEarly", Json::Float(o.rate_early)),
        ("rateLate", Json::Float(o.rate_late)),
        (
            "solver",
            Json::object(vec![
                ("steps", Json::Int(run.steps)),
                ("rhsEvals", Json::Int(run.rhs_evals)),
                ("errTestFails", Json::Int(run.err_test_fails)),
                ("nonlinIters", Json::Int(run.nonlin_iters)),
                ("nonlinConvFails", Json::Int(run.nonlin_conv_fails)),
                ("lastOrder", Json::Int(run.last_order as i64)),
            ]),
        ),
    ])
}

/// Configuration lines for `print-config`.
pub fn config_lines() -> Vec<String> {
    vec![
        format!(
            "exp5: H = {}, m = {}, q = {:?}, C signs = {:?}",
            fmt17(HUBBLE),
            fmt17(MASS),
            Q_VALUES,
            C_SIGNS
        ),
        format!(
            "exp5: t in [0, t* + {}], {} output intervals, WKB window [t* + {}, t_end]",
            fmt17(EXTRA_TIME),
            OUTPUT_INTERVALS,
            fmt17(WINDOW_START)
        ),
        format!(
            "exp5: default rtol = {}, atol = {}, max_step = {}, method Adams + fixed point",
            fmt17(DEFAULT_TOLERANCES.rtol),
            fmt17(DEFAULT_TOLERANCES.atol),
            fmt17(DEFAULT_TOLERANCES.max_step)
        ),
    ]
}

/// Run EXP-5.
pub fn run(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let directory = ctx.experiment_dir(EXPERIMENT)?;
    let tolerances = ctx.tolerances(DEFAULT_TOLERANCES);
    let alg = Algebra::new();
    let mut summary = ExperimentSummary::new(EXPERIMENT);
    let mut outcomes = Vec::new();
    let mut solver = "";
    for spec in build_runs(&alg)? {
        let (outcome, description) = execute(&alg, spec, &tolerances)?;
        solver = description;
        write_csv(&directory.join(&outcome.file), &header(), &outcome.rows)?;
        summary.add_file(&outcome.file);
        summary.add_stats(outcome.integration.steps, outcome.integration.rhs_evals);
        outcomes.push(outcome);
    }
    let fold = |f: &dyn Fn(&RunOutcome) -> f64| outcomes.iter().map(f).fold(0.0f64, f64::max);
    let eigen = fold(&|o| o.spec.eigen_residual);
    let krein_norm = fold(&|o| o.max_drift_normalized);
    let krein_before = fold(&|o| o.max_drift_before_tstar);
    let dev0 = fold(&|o| ((o.gamma_num - o.gamma_wkb0) / o.gamma_wkb0).abs());
    let dev1 = fold(&|o| ((o.gamma_num - o.gamma_wkb1) / o.gamma_wkb1).abs());
    let krein_nonzero = outcomes.iter().all(|o| o.krein0.abs() > 0.5);
    let growth_ok = outcomes
        .iter()
        .all(|o| o.final_norm > 1.0e10 && o.rate_late > 2.0 * o.rate_early && o.rate_early > 0.0);
    summary.check(
        "energy_squared_changes_sign_at_tstar",
        outcomes.iter().all(|o| o.sign_change_ok),
        "E^2(t) > 0 before t* and < 0 after on every grid point",
    );
    summary.check(
        "initial_positive_energy_C_eigenvector",
        eigen <= EIGEN_LIMIT && krein_nonzero,
        &format!("max residual {}, all |u0^dag B u0| > 0.5", fmt17(eigen)),
    );
    summary.check(
        "krein_norm_conserved_normalized",
        krein_norm <= KREIN_LIMIT,
        &format!(
            "max |d(u^dag B u)| / max(u^dag u, 1) = {} (limit {})",
            fmt17(krein_norm),
            fmt17(KREIN_LIMIT)
        ),
    );
    summary.check(
        "krein_norm_conserved_before_tstar",
        krein_before <= KREIN_LIMIT,
        &format!("max |d(u^dag B u)| for t <= t* = {}", fmt17(krein_before)),
    );
    summary.check(
        "hilbert_norm_superexponential_growth",
        growth_ok,
        &format!(
            "final u^dag u min = {}, late/early growth-rate ratio min = {}",
            fmt17(
                outcomes
                    .iter()
                    .map(|o| o.final_norm)
                    .fold(f64::INFINITY, f64::min)
            ),
            fmt17(
                outcomes
                    .iter()
                    .map(|o| o.rate_late / o.rate_early)
                    .fold(f64::INFINITY, f64::min)
            )
        ),
    );
    summary.check(
        "growth_matches_wkb_leading_order",
        dev0 <= WKB0_LIMIT,
        &format!(
            "max relative deviation {} (limit {})",
            fmt17(dev0),
            fmt17(WKB0_LIMIT)
        ),
    );
    summary.check(
        "growth_matches_wkb_first_order",
        dev1 <= WKB1_LIMIT,
        &format!(
            "max relative deviation {} (limit {})",
            fmt17(dev1),
            fmt17(WKB1_LIMIT)
        ),
    );
    let extra = vec![
        (
            "parameters",
            Json::object(vec![
                ("H", Json::Float(HUBBLE)),
                ("m", Json::Float(MASS)),
                ("qValues", Json::floats(&Q_VALUES)),
                ("cSigns", Json::floats(&C_SIGNS)),
                ("extraTime", Json::Float(EXTRA_TIME)),
                ("outputIntervals", Json::Int(OUTPUT_INTERVALS as i64)),
                ("wkbWindowStart", Json::Float(WINDOW_START)),
                ("momentumDirection", Json::Int(5)),
            ]),
        ),
        (
            "stateLayout",
            Json::str("u_re_0..u_re_15, u_im_0..u_im_15 (u = re + i im in C^16)"),
        ),
        (
            "limits",
            Json::object(vec![
                ("wkbLeading", Json::Float(WKB0_LIMIT)),
                ("wkbFirstOrder", Json::Float(WKB1_LIMIT)),
                ("kreinNormalized", Json::Float(KREIN_LIMIT)),
                ("eigen", Json::Float(EIGEN_LIMIT)),
            ]),
        ),
        ("runs", Json::Array(outcomes.iter().map(run_json).collect())),
        (
            "measurements",
            Json::object(vec![
                ("maxKreinDriftNormalized", Json::Float(krein_norm)),
                ("maxKreinDriftBeforeTStar", Json::Float(krein_before)),
                (
                    "maxKreinDriftAbs",
                    Json::Float(fold(&|o| o.max_drift_abs)),
                ),
                ("maxRelDevWkbLeading", Json::Float(dev0)),
                ("maxRelDevWkbFirstOrder", Json::Float(dev1)),
            ]),
        ),
        (
            "notes",
            Json::Array(vec![
                Json::str(
                    "u^dag u grows like exp(2 W(t)); u^dag B u is conserved (B-pseudo-Hermitian h). \
                     This is why quantisation and cosmology are restricted to the q = 0 sector.",
                ),
                Json::str(
                    "The absolute Krein drift at late times is bounded by float64 cancellation \
                     (~1e-16 u^dag u); the normalised drift is the meaningful conservation measure.",
                ),
            ]),
        ),
    ];
    let doc = standard_summary(ctx, &summary, &tolerances, solver, extra);
    write_json(&directory.join("summary.json"), &doc)?;
    summary.add_file("summary.json");
    Ok(summary)
}
