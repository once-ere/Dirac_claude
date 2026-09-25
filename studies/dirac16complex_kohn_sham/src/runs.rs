//! The parameter matrix and the subcommands `spectrum`, `scf`, `excited`,
//! `thermo`, `emt` (and `all`).
//!
//! Reference numbers (computed, deterministic, recorded in every summary):
//! * closed shells of the non-interacting spectrum at m = 1, L = 3: N_mid is
//!   the closed-shell number nearest 100 and N_large the one nearest 1000;
//! * `lambda_hat_1 = 0.1 m^7 / S_ref`, `lambda_hat_2 = 1.0 m^7 / S_ref` with
//!   `S_ref = max_y |S_p(y)|` of the non-interacting N_mid ground state at
//!   m = 1, L = 3, so that `|lambda S_p|/m` reaches 0.1 and 1.0 there.
//!
//! Matrix (canonical run, no `--quick`; H = 1, a4_0 = 0, Delta k = 0.25 m,
//! 301 grid points unless stated):
//! * scf (T = 0): m = 1, L = 3, N in {8, N_mid, N_large} x lambda_hat in
//!   {0, +-lh1, +-lh2}; L in {2, 4} with N in {8, N_mid}, lambda_hat in {0, lh1};
//!   m = 3, L = 3, N in {8, N_mid}, lambda_hat in {0, +-lh1}; a4_0 = 0.5
//!   rescaling pair; grid 601 and Delta k = 0.125 m (N x 8, same density)
//!   convergence runs; Hellmann-Feynman dE/dm checks.
//! * excited: KS gaps, particle-hole list and Delta-SCF for m = 1, L = 3,
//!   N in {8, N_mid, N_large}, lambda_hat in {0, +-lh1, +-lh2}.
//! * thermo: T/m in {0, 0.1, 0.3, 1} for m = 1, L = 3, N in {8, N_mid},
//!   lambda_hat in {0, lh1}; C_V by central differences in T.
//! * emt: EMT profiles and averages for the T = 0 set (m = 1, L = 3) and
//!   one finite-T case.
//!
//! `--quick` keeps N in {8, N_mid}, lambda_hat in {0, lh1}, T <= 0.3 and no
//! N_large / lh2 runs (for smoke tests; not the canonical artifacts).

use std::path::Path;

use crate::blocks;
use crate::emt;
use crate::exchange::{filled_shell_check, gas_chemical_potential, gas_moments, kernel_check};
use crate::geometry::{curvature_check, geometry_json};
use crate::math::{exp, PI};
use crate::output::{standard_summary, write_csv, write_json, Json};
use crate::scf::{
    self, closed_shell_numbers, compute_spectrum, delta_scf, particle_number_from_density, solve,
    standard_params, Occupation, Params, Solution, Spectrum, Window,
};
use crate::shooting::{Potential, Shooter, DEFAULT_TOLERANCES};
use crate::theory;
use crate::{ExperimentSummary, RunContext, Tolerances};

/// Reference numbers shared by the subcommands.
#[derive(Clone, Debug)]
pub struct Reference {
    pub n_mid: f64,
    pub n_large: f64,
    pub closed_shells: Vec<(f64, f64)>,
    pub s_ref: f64,
    pub lambda_hat_1: f64,
    pub lambda_hat_2: f64,
}

pub fn config_lines() -> Vec<String> {
    vec![
        "geometry         = static primordial field, y = ln(sin z)/(6H) in [-L, 0], H = 1, Z2 brane at y = 0".to_string(),
        "reduction        = eight 2x2 blocks (s, c1, c2); real system a' = M a + (s eps - kappa k) b, b' = -(s eps + kappa k) a - M b".to_string(),
        "boundary         = parity +/-: b(0) = 0 / a(0) = 0; bag: b(-L) = 0 (gamma^0 chi = +chi)".to_string(),
        "eigenvalues      = Pruefer shooting (CVODE), theta(0; eps) = n pi (+pi/2), bracket + Illinois".to_string(),
        "exchange         = e_x = -lambda (n^2 + S^2)/32 (exact uniform gas, any T); v_s = -lambda S/16, v_x = -lambda n/16".to_string(),
        "pseudo-potential = M_eff = m + (15/16) lambda S_p, eps -> eps - v_x(y); S_p, n_p proper (e^{-6Hy})".to_string(),
        "occupations      = Fermi-Dirac, normal ordering (sea holes = antiparticles), mu by bisection".to_string(),
        "mixing           = Anderson (beta 0.4, history 6), tolerance 1e-10 on (n_c, S_c)".to_string(),
        "matrix           = L in {2,3,4}, m/H in {1,3}, Delta k = 0.25 m, a4_0 in {0, 0.5}, T/m in {0, 0.1, 0.3, 1}".to_string(),
        format!("tolerances       = rtol {:e} atol {:e} max_step {}", DEFAULT_TOLERANCES.rtol, DEFAULT_TOLERANCES.atol, DEFAULT_TOLERANCES.max_step),
        format!("threads          = {}", scf::worker_threads()),
    ]
}

fn tolerances_of(ctx: &RunContext) -> Tolerances {
    ctx.tolerances(DEFAULT_TOLERANCES)
}

fn params_for(
    ctx: &RunContext,
    m: f64,
    length: f64,
    lambda_hat: f64,
    temperature: f64,
    n: f64,
) -> Params {
    let mut p = standard_params(m, length, lambda_hat, temperature, n);
    p.tolerances = tolerances_of(ctx);
    p
}

fn label(p: &Params, lambda_name: &str) -> String {
    let t = if p.temperature == 0.0 {
        "T0".to_string()
    } else {
        format!("T{}", trim_float(p.temperature / p.m))
    };
    let mut s = format!(
        "m{}_L{}_N{}_{}_{}",
        trim_float(p.m),
        trim_float(p.length),
        p.n_particles as i64,
        lambda_name,
        t
    );
    if p.a4 != 0.0 {
        s.push_str(&format!("_a4{}", trim_float(p.a4)));
    }
    if p.grid_n != 301 {
        s.push_str(&format!("_g{}", p.grid_n));
    }
    if p.delta_k_over_m != 0.25 {
        s.push_str(&format!("_dk{}", trim_float(p.delta_k_over_m)));
    }
    s
}

fn trim_float(v: f64) -> String {
    let s = format!("{v}");
    s.replace('.', "p").replace('-', "m")
}

/// Compute the reference numbers (free spectrum at m = 1, L = 3).
pub fn reference(ctx: &RunContext) -> Result<Reference, String> {
    let params = params_for(ctx, 1.0, 3.0, 0.0, 0.0, 8.0);
    let potential = scf::build_potential(&params, &scf::Densities::zero(params.grid_n));
    let window = Window {
        eps_lo: -1.0,
        eps_hi: 3.2,
    };
    let spectrum = compute_spectrum(&params, &potential, window, &Default::default())?;
    let shells = closed_shell_numbers(&spectrum, 1300.0);
    let pick = |target: f64| -> f64 {
        shells
            .iter()
            .filter(|(n, _)| *n > 8.0)
            .min_by(|a, b| {
                (a.0 - target)
                    .abs()
                    .partial_cmp(&(b.0 - target).abs())
                    .unwrap()
            })
            .map(|(n, _)| *n)
            .unwrap_or(target)
    };
    let n_mid = pick(100.0);
    let n_large = pick(1000.0);
    let mut mid = params.clone();
    mid.n_particles = n_mid;
    let ground = solve(&mid, &Occupation::Zero, None, 0.0)?;
    let s_ref = ground
        .densities
        .s_c
        .iter()
        .zip(mid.grid().iter())
        .map(|(s, y)| (s * crate::geometry::density_factor(mid.h, *y)).abs())
        .fold(0.0, f64::max);
    if s_ref.partial_cmp(&0.0) != Some(std::cmp::Ordering::Greater) {
        return Err("reference: S_ref vanishes".to_string());
    }
    Ok(Reference {
        n_mid,
        n_large,
        closed_shells: shells,
        s_ref,
        lambda_hat_1: 0.1 / s_ref,
        lambda_hat_2: 1.0 / s_ref,
    })
}

fn reference_json(r: &Reference) -> Json {
    Json::object(vec![
        ("nMid", Json::Float(r.n_mid)),
        ("nLarge", Json::Float(r.n_large)),
        (
            "sRef_maxProperScalarDensity_free_nMid",
            Json::Float(r.s_ref),
        ),
        ("lambdaHat1", Json::Float(r.lambda_hat_1)),
        ("lambdaHat2", Json::Float(r.lambda_hat_2)),
        (
            "closedShells_N_epsHomo",
            Json::Array(
                r.closed_shells
                    .iter()
                    .map(|(n, e)| Json::floats(&[*n, *e]))
                    .collect(),
            ),
        ),
    ])
}

// ---------------------------------------------------------------------------
// writers
// ---------------------------------------------------------------------------

fn levels_header() -> Vec<String> {
    [
        "n2",
        "k",
        "multiplicity",
        "parity",
        "s",
        "index",
        "eps",
        "branch",
        "eps_free",
        "f",
        "weight",
        "scalar_charge",
        "pressure_charge",
        "matching_residual",
        "winding_residual",
        "sign_changes",
        "theta_residual",
    ]
    .iter()
    .map(|s| s.to_string())
    .collect()
}

fn levels_rows(spectrum: &Spectrum) -> Vec<Vec<f64>> {
    spectrum
        .states
        .iter()
        .map(|st| {
            vec![
                st.n2 as f64,
                st.k,
                st.mult,
                st.parity as f64,
                st.s as f64,
                st.index as f64,
                st.eps,
                st.branch as f64,
                st.eps_free,
                st.f,
                st.weight,
                (st.s as f64) * st.level.scalar_charge,
                (st.s as f64) * st.level.pressure_charge,
                st.level.matching_residual,
                st.level.winding_residual,
                st.level.sign_changes as f64,
                st.level.theta_residual,
            ]
        })
        .collect()
}

fn write_solution(
    dir: &Path,
    summary: &mut ExperimentSummary,
    name: &str,
    solution: &Solution,
) -> Result<(Vec<emt::Row>, emt::Summary), String> {
    let sub = dir.join(name);
    std::fs::create_dir_all(&sub).map_err(|e| format!("cannot create {}: {e}", sub.display()))?;
    write_csv(
        &sub.join("levels.csv"),
        &levels_header(),
        &levels_rows(&solution.spectrum),
    )?;
    summary.add_file(&format!("{name}/levels.csv"));
    let (rows, emt_summary) = emt::compute(solution);
    // HOMO profile
    let homo_key = solution.filling.homo.map(|h| h.0);
    let homo = homo_key.and_then(|key| solution.spectrum.states.iter().find(|s| s.key() == key));
    let header: Vec<String> = [
        "y",
        "z",
        "n_c",
        "n_p",
        "S_c",
        "S_p",
        "M_eff",
        "v_x",
        "L_s",
        "rho",
        "p_y",
        "p_3",
        "p_t",
        "conservation_residual",
        "homo_a",
        "homo_b",
        "volume_factor",
    ]
    .iter()
    .map(|s| s.to_string())
    .collect();
    let table: Vec<Vec<f64>> = rows
        .iter()
        .enumerate()
        .map(|(i, r)| {
            vec![
                r.y,
                r.z,
                r.n_c,
                r.n_p,
                r.s_c,
                r.s_p,
                r.m_eff,
                r.v_x,
                r.l_s,
                r.rho,
                r.p_y,
                r.p_3,
                r.p_t,
                r.conservation,
                homo.map(|s| s.level.a[i]).unwrap_or(0.0),
                homo.map(|s| s.level.b[i]).unwrap_or(0.0),
                crate::geometry::volume_factor(solution.params.h, r.y),
            ]
        })
        .collect();
    write_csv(&sub.join("profiles.csv"), &header, &table)?;
    summary.add_file(&format!("{name}/profiles.csv"));
    let hist_header: Vec<String> = [
        "iteration",
        "residual_n",
        "residual_S",
        "mu",
        "E",
        "F",
        "states",
        "integrations",
    ]
    .iter()
    .map(|s| s.to_string())
    .collect();
    let hist: Vec<Vec<f64>> = solution
        .history
        .iter()
        .map(|h| {
            vec![
                h.iteration as f64,
                h.residual_n,
                h.residual_s,
                h.mu,
                h.energy,
                h.free,
                h.states as f64,
                h.integrations as f64,
            ]
        })
        .collect();
    write_csv(&sub.join("history.csv"), &hist_header, &hist)?;
    summary.add_file(&format!("{name}/history.csv"));
    let record = run_json(solution, &emt_summary);
    write_json(&sub.join("run.json"), &record)?;
    summary.add_file(&format!("{name}/run.json"));
    Ok((rows, emt_summary))
}

fn params_json(p: &Params) -> Json {
    Json::object(vec![
        ("H", Json::Float(p.h)),
        ("m", Json::Float(p.m)),
        ("a4_0", Json::Float(p.a4)),
        ("L", Json::Float(p.length)),
        ("gridPoints", Json::Int(p.grid_n as i64)),
        ("deltaKOverM", Json::Float(p.delta_k_over_m)),
        ("ell", Json::Float(p.ell())),
        ("lambdaHat", Json::Float(p.lambda_hat)),
        ("lambda", Json::Float(p.lambda())),
        ("T", Json::Float(p.temperature)),
        ("N", Json::Float(p.n_particles)),
        ("fCut", Json::Float(p.f_cut)),
        ("mixBeta", Json::Float(p.mix_beta)),
        ("mixHistory", Json::Int(p.mix_history as i64)),
        ("tol", Json::Float(p.tol)),
        ("rtol", Json::Float(p.tolerances.rtol)),
        ("atol", Json::Float(p.tolerances.atol)),
    ])
}

fn run_json(s: &Solution, e: &emt::Summary) -> Json {
    let en = &s.energies;
    Json::object(vec![
        ("parameters", params_json(&s.params)),
        ("converged", Json::Bool(s.converged)),
        ("iterations", Json::Int(s.iterations as i64)),
        (
            "finalResidualN",
            Json::Float(s.history.last().map(|h| h.residual_n).unwrap_or(f64::NAN)),
        ),
        (
            "finalResidualS",
            Json::Float(s.history.last().map(|h| h.residual_s).unwrap_or(f64::NAN)),
        ),
        ("mu", Json::Float(s.filling.mu)),
        (
            "epsHomo",
            Json::Float(s.filling.homo.map(|h| h.1).unwrap_or(f64::NAN)),
        ),
        (
            "epsLumo",
            Json::Float(s.filling.lumo.map(|l| l.1).unwrap_or(f64::NAN)),
        ),
        ("ksGap", Json::Float(s.gap().unwrap_or(f64::NAN))),
        ("seaTop", Json::Float(s.filling.sea_top)),
        ("particleBottom", Json::Float(s.filling.particle_bottom)),
        (
            "branchOverlap",
            Json::Bool(s.filling.sea_top > s.filling.particle_bottom),
        ),
        ("nTotal", Json::Float(en.n_total)),
        (
            "nFromDensity",
            Json::Float(particle_number_from_density(&s.params, &s.densities)),
        ),
        ("ksSum", Json::Float(en.ks_sum)),
        ("hartreeEnergy", Json::Float(en.hartree)),
        ("exchangeEnergy", Json::Float(en.exchange)),
        ("energy", Json::Float(en.total)),
        ("entropy", Json::Float(en.entropy)),
        ("freeEnergy", Json::Float(en.free)),
        ("grandPotential", Json::Float(en.grand)),
        ("scalarTotal", Json::Float(en.scalar_total)),
        ("maxLambdaSOverM", Json::Float(en.max_lambda_s_over_m)),
        ("windowLo", Json::Float(s.window.eps_lo)),
        ("windowHi", Json::Float(s.window.eps_hi)),
        ("states", Json::Int(s.spectrum.states.len() as i64)),
        ("shellsUsed", Json::Int(s.spectrum.shells_used as i64)),
        (
            "maxMatchingResidual",
            Json::Float(s.spectrum.max_matching_residual),
        ),
        (
            "maxWindingResidual",
            Json::Float(s.spectrum.max_winding_residual),
        ),
        (
            "maxThetaResidual",
            Json::Float(s.spectrum.max_theta_residual),
        ),
        ("integrations", Json::Int(s.stats.integrations)),
        ("solverSteps", Json::Int(s.stats.steps)),
        ("rescales", Json::Int(s.stats.rescales)),
        ("emt", emt_json(e)),
    ])
}

fn emt_json(e: &emt::Summary) -> Json {
    Json::object(vec![
        ("energyFromRho", Json::Float(e.energy_from_rho)),
        ("energyTotal", Json::Float(e.energy_total)),
        ("rhoAvg", Json::Float(e.rho_avg)),
        ("pYAvg", Json::Float(e.p_y_avg)),
        ("p3Avg", Json::Float(e.p_3_avg)),
        ("pTAvg", Json::Float(e.p_t_avg)),
        ("wY", Json::Float(e.w_y)),
        ("w3", Json::Float(e.w_3)),
        ("wT", Json::Float(e.w_t)),
        (
            "braneFraction_within_1_over_H",
            Json::Float(e.brane_fraction),
        ),
        (
            "tipFraction_within_1_over_H_of_cutoff",
            Json::Float(e.tip_fraction),
        ),
        ("properVolume", Json::Float(e.proper_volume)),
        ("rhoRequired_kappa1", Json::Float(e.rho_required)),
        ("kappaNeeded", Json::Float(e.kappa_needed)),
        (
            "conservationResidualMax_normalised",
            Json::Float(e.conservation_max),
        ),
        ("rhoMax", Json::Float(e.rho_max)),
        ("rhoMin", Json::Float(e.rho_min)),
    ])
}

fn finish(
    ctx: &RunContext,
    dir: &Path,
    summary: &mut ExperimentSummary,
    extra: Vec<(&str, Json)>,
) -> Result<(), String> {
    let tol = tolerances_of(ctx);
    let doc = standard_summary(
        ctx,
        summary,
        &tol,
        "CVODE BDF/Adams Pruefer shooting + BDF profiles (see shooting.rs)",
        extra,
    );
    write_json(&dir.join("summary.json"), &doc)?;
    summary.add_file("summary.json");
    Ok(())
}

fn relative(a: f64, b: f64) -> f64 {
    (a - b).abs() / a.abs().max(b.abs()).max(1e-300)
}

// ---------------------------------------------------------------------------
// spectrum
// ---------------------------------------------------------------------------

pub fn run_spectrum(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let dir = ctx.experiment_dir("spectrum")?;
    let mut summary = ExperimentSummary::new("spectrum");
    // exact algebra
    let reduction = blocks::derive();
    write_json(&dir.join("reduction.json"), &reduction.to_json())?;
    summary.add_file("reduction.json");
    summary.check(
        "reduction_exact_to_1e14",
        reduction.max_defect() < 1e-14,
        &format!("max defect {:e}", reduction.max_defect()),
    );
    summary.check(
        "reduction_basis_matches_generated",
        reduction.basis_defect_vs_generated < 1e-15,
        &format!("{:e}", reduction.basis_defect_vs_generated),
    );
    summary.check(
        "reduction_four_blocks_per_type",
        reduction.labels.iter().filter(|l| l[0] == 1).count() == 4,
        "s = +1 on blocks 0..3",
    );
    // geometry
    write_json(&dir.join("geometry.json"), &geometry_json(1.0, 0.0))?;
    summary.add_file("geometry.json");
    let curvature_defect = curvature_check(1.0, 0.0).max(curvature_check(1.0, 0.5));
    summary.check(
        "geometry_curvature_closed_forms",
        curvature_defect < 1e-7,
        &format!("R = -42, G = (15,15,15,15,21,15,15,15); numerical defect {curvature_defect:e}"),
    );
    let closed = crate::geometry::curvature_closed_form(1.0);
    summary.check(
        "geometry_required_source_negative",
        closed.rho_required == -21.0 && closed.p_required.iter().all(|p| *p == 15.0),
        "rho_req = -21 H^2/kappa, p_req = +15 H^2/kappa",
    );
    summary.check(
        "geometry_brane_stress_pattern",
        closed.brane_stress == [-10.0, -10.0, -10.0, -12.0, -10.0, -10.0, -10.0],
        "S = -(H/kappa) diag(10,10,10,12,10,10,10); rho_brane = +12 H/kappa",
    );
    // exchange
    let (kernel, closed_form) = kernel_check(1.0, 1.3, 0.4, 12.0, 20, 8);
    let (kernel_b, closed_b) = kernel_check(1.0, -0.2, 1.0, 30.0, 24, 8);
    let shell = [0.0, 0.5, 2.0]
        .iter()
        .map(|k| filled_shell_check(1.0, *k))
        .fold(0.0, f64::max);
    summary.check(
        "exchange_kernel_identity",
        kernel.max(kernel_b) < 1e-11,
        &format!(
            "max |Tr[BC P BC P] - 4[1 + ab(M^2 - k.k')/EE']| = {:e}",
            kernel.max(kernel_b)
        ),
    );
    summary.check(
        "exchange_closed_form_uniform_gas",
        closed_form.max(closed_b) < 1e-9,
        &format!(
            "relative defect of -(n^2+S^2)/16 vs quadrature: {:e}, {:e}",
            closed_form, closed_b
        ),
    );
    summary.check(
        "exchange_filled_shell_one_eighth",
        shell < 1e-12,
        &format!("{shell:e}"),
    );
    // uniform-gas table S(n, T), pressure, energy (for the LDA documentation)
    let mut gas_rows = Vec::new();
    for t in [0.0, 0.1, 0.3, 1.0] {
        for n in [1e-4, 1e-3, 1e-2, 1e-1, 1.0] {
            let mu = gas_chemical_potential(1.0, n, t, 60.0, 400);
            let mo = gas_moments(1.0, mu, t, 60.0, 400);
            gas_rows.push(vec![
                t,
                n,
                mu,
                mo.n,
                mo.s,
                mo.energy,
                mo.pressure,
                -(mo.n * mo.n + mo.s * mo.s) / 32.0,
            ]);
        }
    }
    write_csv(
        &dir.join("uniform-gas-table.csv"),
        &[
            "T",
            "n_target",
            "mu",
            "n",
            "S",
            "energy_density",
            "pressure",
            "e_x_over_lambda",
        ]
        .iter()
        .map(|s| s.to_string())
        .collect::<Vec<_>>(),
        &gas_rows,
    )?;
    summary.add_file("uniform-gas-table.csv");
    write_json(
        &dir.join("exchange-check.json"),
        &Json::object(vec![
            ("closedForm", Json::str("e_x(n, S) = -lambda (n^2 + S^2)/32; v_s = -lambda S/16; v_v = -lambda n/16; exact for the isotropic uniform 8-fold gas at every T (normal ordering)")),
            ("kernelDefect", Json::Float(kernel.max(kernel_b))),
            ("closedFormRelativeDefect", Json::Float(closed_form.max(closed_b))),
            ("filledShellDefect", Json::Float(shell)),
            ("source", Json::str("own quadrature (exchange.rs); artifacts/dirac16complex/kohn-sham/exchange-table.json was not consulted")),
        ]),
    )?;
    summary.add_file("exchange-check.json");
    // free spectra and analytic box comparison
    let mut box_defect: f64 = 0.0;
    let mut residual_max: f64 = 0.0;
    for m in [1.0, 3.0] {
        for length in [2.0, 3.0, 4.0] {
            let params = params_for(ctx, m, length, 0.0, 0.0, 8.0);
            let mut p = params.clone();
            p.shell_cap = 16;
            let potential = scf::build_potential(&p, &scf::Densities::zero(p.grid_n));
            let spectrum = compute_spectrum(
                &p,
                &potential,
                Window {
                    eps_lo: -4.0 * m,
                    eps_hi: 4.0 * m,
                },
                &Default::default(),
            )?;
            residual_max = residual_max
                .max(spectrum.max_matching_residual)
                .max(spectrum.max_winding_residual);
            let name = format!(
                "free-spectrum-m{}-L{}.csv",
                trim_float(m),
                trim_float(length)
            );
            write_csv(&dir.join(&name), &levels_header(), &levels_rows(&spectrum))?;
            summary.add_file(&name);
            // analytic k = 0: parity + eps = 0, +-sqrt(m^2 + (n pi/L)^2); parity -: tan(pL) = -p/m
            for st in spectrum.states.iter().filter(|s| s.n2 == 0 && s.s == 1) {
                let expected = if st.parity == 1 {
                    let p = (st.index.abs() as f64) * PI / length;
                    (st.index.signum() as f64) * (m * m + p * p).sqrt()
                } else {
                    odd_box_root(m, length, st.index)
                };
                box_defect = box_defect.max((st.eps - expected).abs());
            }
        }
    }
    summary.check(
        "free_box_spectrum_analytic",
        box_defect < 1e-8,
        &format!("max |eps - analytic| at k = 0 over m, L: {box_defect:e}"),
    );
    summary.check(
        "level_residuals_small",
        residual_max < 1e-6,
        &format!("max matching/winding residual {residual_max:e}"),
    );
    // a4_0 rescaling: spectrum(k, a4) == spectrum(k e^{-a4}, 0)
    let mut rescale_defect: f64 = 0.0;
    {
        let base = std::sync::Arc::new(Potential::free(1.0, 0.0, 3.0, 1.0, 301));
        let shifted = std::sync::Arc::new(Potential::free(1.0, 0.5, 3.0, 1.0, 301));
        let mut s0 = Shooter::new(base, tolerances_of(ctx));
        let mut s1 = Shooter::new(shifted, tolerances_of(ctx));
        for k in [0.25, 1.0] {
            for parity in [1, -1] {
                let a = s1.levels(k, parity, -3.0, 3.0, &[])?;
                let b = s0.levels(k * exp(-0.5), parity, -3.0, 3.0, &[])?;
                if a.len() != b.len() {
                    rescale_defect = 1.0;
                } else {
                    for (x, y) in a.iter().zip(b.iter()) {
                        rescale_defect = rescale_defect.max((x.eps - y.eps).abs());
                    }
                }
            }
        }
    }
    summary.check(
        "a4_rescaling_k_to_k_exp_minus_a4",
        rescale_defect < 1e-9,
        &format!("max |eps(k, a4=0.5) - eps(k e^{{-0.5}}, 0)| = {rescale_defect:e}"),
    );
    // agreement with the exact Wolfram theory file, when present
    let comparison = theory::compare(theory::THEORY_PATH, tolerances_of(ctx));
    if comparison.present {
        for item in &comparison.items {
            summary.check(&item.name, item.passed, &item.detail);
        }
    }
    write_json(&dir.join("theory-agreement.json"), &comparison.to_json())?;
    summary.add_file("theory-agreement.json");
    // reference numbers
    let reference = reference(ctx)?;
    summary.check(
        "closed_shells_found",
        reference.n_mid > 8.0 && reference.n_large > reference.n_mid,
        &format!(
            "N_mid = {}, N_large = {}",
            reference.n_mid, reference.n_large
        ),
    );
    summary.check(
        "coupling_scale_positive",
        reference.s_ref > 0.0,
        &format!(
            "S_ref = {:e}, lambda_hat_1 = {:e}, lambda_hat_2 = {:e}",
            reference.s_ref, reference.lambda_hat_1, reference.lambda_hat_2
        ),
    );
    let closed_rows: Vec<Vec<f64>> = reference
        .closed_shells
        .iter()
        .map(|(n, e)| vec![*n, *e])
        .collect();
    write_csv(
        &dir.join("closed-shells-m1-L3.csv"),
        &["N", "eps_homo"]
            .iter()
            .map(|s| s.to_string())
            .collect::<Vec<_>>(),
        &closed_rows,
    )?;
    summary.add_file("closed-shells-m1-L3.csv");
    finish(
        ctx,
        &dir,
        &mut summary,
        vec![
            ("reference", reference_json(&reference)),
            (
                "theoryAgreement",
                Json::str(if comparison.present {
                    "compared (theory-agreement.json)"
                } else {
                    "not-run: kohn-sham-theory.json absent"
                }),
            ),
            ("exchangeTable", theory::exchange_table_note()),
        ],
    )?;
    Ok(summary)
}

/// Analytic odd-parity box level of index n (tan(pL) = -p/M): the n-th
/// positive root p_n lies in ((n + 1/2) pi/L, (n + 3/2) pi/L) for n >= 0;
/// negative indices mirror.
fn odd_box_root(m: f64, length: f64, index: i64) -> f64 {
    let n = if index >= 0 { index } else { -index - 1 } as f64;
    let g = |p: f64| crate::math::sin(p * length) * m + p * crate::math::cos(p * length);
    let mut a = (n + 0.5) * PI / length + 1e-12;
    let mut b = (n + 1.5) * PI / length - 1e-12;
    if g(a) * g(b) > 0.0 {
        return f64::NAN;
    }
    for _ in 0..200 {
        let mid = 0.5 * (a + b);
        if g(a) * g(mid) <= 0.0 {
            b = mid;
        } else {
            a = mid;
        }
    }
    let p = 0.5 * (a + b);
    let e = (m * m + p * p).sqrt();
    if index >= 0 {
        e
    } else {
        -e
    }
}

// ---------------------------------------------------------------------------
// scf
// ---------------------------------------------------------------------------

fn lambda_set(r: &Reference, quick: bool) -> Vec<(String, f64)> {
    if quick {
        vec![
            ("lam0".to_string(), 0.0),
            ("lamp1".to_string(), r.lambda_hat_1),
        ]
    } else {
        vec![
            ("lam0".to_string(), 0.0),
            ("lamp1".to_string(), r.lambda_hat_1),
            ("lamm1".to_string(), -r.lambda_hat_1),
            ("lamp2".to_string(), r.lambda_hat_2),
            ("lamm2".to_string(), -r.lambda_hat_2),
        ]
    }
}

fn n_set(r: &Reference, quick: bool) -> Vec<f64> {
    if quick {
        vec![8.0, r.n_mid]
    } else {
        vec![8.0, r.n_mid, r.n_large]
    }
}

fn solve_and_write(
    ctx: &RunContext,
    dir: &Path,
    summary: &mut ExperimentSummary,
    params: &Params,
    lambda_name: &str,
    records: &mut Vec<Json>,
) -> Result<Solution, String> {
    let name = label(params, lambda_name);
    let mode = if params.temperature > 0.0 {
        Occupation::Thermal
    } else {
        Occupation::Zero
    };
    let solution = solve(params, &mode, None, 0.0)?;
    let (_, e) = write_solution(dir, summary, &name, &solution)?;
    let n_density = particle_number_from_density(params, &solution.densities);
    summary.check(
        &format!("{name}_converged"),
        solution.converged,
        &format!(
            "{} iterations, residual {:e}",
            solution.iterations,
            solution
                .history
                .last()
                .map(|h| h.residual_n.max(h.residual_s))
                .unwrap_or(f64::NAN)
        ),
    );
    summary.check(
        &format!("{name}_particle_number"),
        (n_density - params.n_particles).abs() <= 1e-6 * params.n_particles
            && (solution.energies.n_total - params.n_particles).abs() <= 1e-8 * params.n_particles,
        &format!(
            "N(density) = {n_density}, sum weights = {}",
            solution.energies.n_total
        ),
    );
    summary.check(
        &format!("{name}_energy_from_rho"),
        relative(e.energy_from_rho, e.energy_total) < 1e-6
            || (e.energy_from_rho - e.energy_total).abs() < 1e-8,
        &format!("{} vs {}", e.energy_from_rho, e.energy_total),
    );
    summary.check(
        &format!("{name}_emt_conservation"),
        e.conservation_max < 1e-3,
        &format!("normalised max residual {:e}", e.conservation_max),
    );
    let _ = ctx;
    let mut record = match run_json(&solution, &e) {
        Json::Object(pairs) => pairs,
        _ => Vec::new(),
    };
    record.insert(0, ("label".to_string(), Json::str(&name)));
    record.insert(1, ("lambdaName".to_string(), Json::str(lambda_name)));
    records.push(Json::Object(record));
    Ok(solution)
}

/// Hellmann-Feynman check dE/dm = int S_p dV_p (5-point stencil, delta = 1e-3 m).
fn hellmann_feynman(params: &Params, solution: &Solution) -> Result<(f64, f64), String> {
    let d = 1e-3 * params.m;
    let mut values = Vec::new();
    for f in [-2.0, -1.0, 1.0, 2.0] {
        let mut p = params.clone();
        p.m = params.m + f * d;
        // keep lambda, l, Delta k fixed (they are defined through the unperturbed m)
        p.lambda_hat = params.lambda() * p.m.powi(6);
        p.delta_k_over_m = params.delta_k() / p.m;
        let s = solve(
            &p,
            &Occupation::Zero,
            Some(&solution.densities),
            solution.filling.mu,
        )?;
        if !s.converged {
            return Err("hellmann_feynman: shifted run did not converge".to_string());
        }
        values.push(s.energies.total);
    }
    let fd = (values[0] - 8.0 * values[1] + 8.0 * values[2] - values[3]) / (12.0 * d);
    Ok((fd, solution.energies.scalar_total))
}

pub fn run_scf(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let dir = ctx.experiment_dir("scf")?;
    let mut summary = ExperimentSummary::new("scf");
    let reference = reference(ctx)?;
    let mut records = Vec::new();
    let lambdas = lambda_set(&reference, ctx.quick);
    let ns = n_set(&reference, ctx.quick);
    // A: m = 1, L = 3
    let mut hf_targets: Vec<(String, Params, Solution)> = Vec::new();
    for n in &ns {
        for (lname, lh) in &lambdas {
            let params = params_for(ctx, 1.0, 3.0, *lh, 0.0, *n);
            let solution = solve_and_write(ctx, &dir, &mut summary, &params, lname, &mut records)?;
            if (*n == reference.n_mid) && (lname == "lam0" || lname == "lamp1") {
                hf_targets.push((label(&params, lname), params.clone(), solution));
            }
        }
    }
    // B: L dependence
    for length in [2.0, 4.0] {
        for n in [8.0, reference.n_mid] {
            for (lname, lh) in lambdas.iter().take(2) {
                let params = params_for(ctx, 1.0, length, *lh, 0.0, n);
                solve_and_write(ctx, &dir, &mut summary, &params, lname, &mut records)?;
            }
        }
    }
    // C: m = 3
    let m3_lambdas: Vec<(String, f64)> = if ctx.quick {
        lambdas.clone()
    } else {
        lambdas.iter().take(3).cloned().collect()
    };
    for n in [8.0, reference.n_mid] {
        for (lname, lh) in &m3_lambdas {
            let params = params_for(ctx, 3.0, 3.0, *lh, 0.0, n);
            solve_and_write(ctx, &dir, &mut summary, &params, lname, &mut records)?;
        }
    }
    // D: a4_0 = 0.5 rescaling pair (N_mid, lambda_hat_1)
    {
        let mut a = params_for(ctx, 1.0, 3.0, reference.lambda_hat_1, 0.0, reference.n_mid);
        a.a4 = 0.5;
        let sa = solve_and_write(ctx, &dir, &mut summary, &a, "lamp1", &mut records)?;
        let mut b = params_for(ctx, 1.0, 3.0, reference.lambda_hat_1, 0.0, reference.n_mid);
        b.delta_k_over_m = 0.25 * exp(-0.5);
        let sb = solve_and_write(ctx, &dir, &mut summary, &b, "lamp1", &mut records)?;
        // same spectra; the densities differ by the torus volume l^3 (a4 does not
        // rescale l), so compare E per particle only after mapping: with Delta k
        // -> Delta k e^{-a4} the volume grows by e^{3 a4}; the a4 = 0.5 run at the
        // original l is therefore the b run at density x e^{1.5}.  Exact statement
        // checked: single-particle spectra coincide (levels.csv) -- compare eps.
        let mut worst: f64 = 0.0;
        let free_a = sa
            .spectrum
            .states
            .iter()
            .filter(|s| s.weight == 0.0)
            .count();
        let _ = free_a;
        for (x, y) in sa.spectrum.states.iter().zip(sb.spectrum.states.iter()) {
            if x.n2 == y.n2 && x.parity == y.parity && x.s == y.s && x.index == y.index && x.n2 == 0
            {
                worst = worst.max((x.eps - y.eps).abs());
            }
        }
        summary.check("a4_rescaling_pair_k0_levels_agree", worst < 1e-8, &format!("k = 0 levels of the a4 = 0.5 run and the Delta k e^{{-0.5}} run: max |d eps| = {worst:e} (finite-k levels differ only through the density, see run.json)"));
    }
    // E: grid and Delta k convergence (N_mid, lambda_hat_1)
    {
        let base = params_for(ctx, 1.0, 3.0, reference.lambda_hat_1, 0.0, reference.n_mid);
        let base_solution = solve(&base, &Occupation::Zero, None, 0.0)?;
        let mut fine = base.clone();
        fine.grid_n = 601;
        let fine_solution = solve_and_write(ctx, &dir, &mut summary, &fine, "lamp1", &mut records)?;
        let grid_defect = relative(fine_solution.energies.total, base_solution.energies.total);
        summary.check(
            "grid_refinement_energy",
            grid_defect < 1e-5,
            &format!(
                "E(601) = {}, E(301) = {}, relative {grid_defect:e}",
                fine_solution.energies.total, base_solution.energies.total
            ),
        );
        let mut dk = base.clone();
        dk.delta_k_over_m = 0.125;
        dk.n_particles = 8.0 * reference.n_mid;
        let dk_solution = solve_and_write(ctx, &dir, &mut summary, &dk, "lamp1", &mut records)?;
        let per_particle = (
            dk_solution.energies.total / dk.n_particles,
            base_solution.energies.total / base.n_particles,
        );
        summary.check(
            "delta_k_halved_recorded",
            dk_solution.converged,
            &format!(
                "E/N at Delta k = 0.125 (N x 8): {} vs {} at 0.25",
                per_particle.0, per_particle.1
            ),
        );
    }
    // Hellmann-Feynman
    for (name, params, solution) in &hf_targets {
        let (fd, hf) = hellmann_feynman(params, solution)?;
        let ok = (fd - hf).abs() <= 1e-5 * hf.abs().max(1.0);
        summary.check(
            &format!("{name}_hellmann_feynman_dE_dm"),
            ok,
            &format!("finite difference {fd} vs int S_p dV_p = {hf}"),
        );
    }
    finish(
        ctx,
        &dir,
        &mut summary,
        vec![
            ("reference", reference_json(&reference)),
            ("runs", Json::Array(records)),
        ],
    )?;
    Ok(summary)
}

// ---------------------------------------------------------------------------
// excited
// ---------------------------------------------------------------------------

pub fn run_excited(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let dir = ctx.experiment_dir("excited")?;
    let mut summary = ExperimentSummary::new("excited");
    let reference = reference(ctx)?;
    let mut records = Vec::new();
    let mut table = Vec::new();
    for n in n_set(&reference, ctx.quick) {
        for (lname, lh) in lambda_set(&reference, ctx.quick) {
            let params = params_for(ctx, 1.0, 3.0, lh, 0.0, n);
            let name = label(&params, &lname);
            let ground = solve(&params, &Occupation::Zero, None, 0.0)?;
            summary.check(
                &format!("{name}_ground_converged"),
                ground.converged,
                &format!("{} iterations", ground.iterations),
            );
            let gap = ground.gap().unwrap_or(f64::NAN);
            // particle-hole list: lowest 12 excitations eps_a - eps_i (occupied i, empty a)
            let occupied: Vec<&scf::State> = ground
                .spectrum
                .states
                .iter()
                .filter(|s| s.branch > 0 && s.f > 0.0)
                .collect();
            let empty: Vec<&scf::State> = ground
                .spectrum
                .states
                .iter()
                .filter(|s| s.branch > 0 && s.f < 1.0)
                .collect();
            let mut ph: Vec<(f64, f64, f64, f64, f64)> = Vec::new();
            for i in &occupied {
                for a in &empty {
                    if a.eps > i.eps {
                        ph.push((a.eps - i.eps, i.eps, a.eps, i.k, a.k));
                    }
                }
            }
            ph.sort_by(|x, y| x.0.partial_cmp(&y.0).unwrap());
            ph.truncate(12);
            let ph_rows: Vec<Vec<f64>> = ph.iter().map(|p| vec![p.0, p.1, p.2, p.3, p.4]).collect();
            let sub = dir.join(&name);
            std::fs::create_dir_all(&sub).map_err(|e| e.to_string())?;
            write_csv(
                &sub.join("particle-hole.csv"),
                &[
                    "excitation",
                    "eps_hole",
                    "eps_particle",
                    "k_hole",
                    "k_particle",
                ]
                .iter()
                .map(|s| s.to_string())
                .collect::<Vec<_>>(),
                &ph_rows,
            )?;
            summary.add_file(&format!("{name}/particle-hole.csv"));
            write_csv(
                &sub.join("levels.csv"),
                &levels_header(),
                &levels_rows(&ground.spectrum),
            )?;
            summary.add_file(&format!("{name}/levels.csv"));
            let (delta_scf, excited_energy, excited_converged, excited_iterations) =
                match delta_scf(&ground) {
                    Ok(ex) => {
                        write_csv(
                            &sub.join("levels-excited.csv"),
                            &levels_header(),
                            &levels_rows(&ex.spectrum),
                        )?;
                        summary.add_file(&format!("{name}/levels-excited.csv"));
                        (
                            ex.energies.total - ground.energies.total,
                            ex.energies.total,
                            ex.converged,
                            ex.iterations as i64,
                        )
                    }
                    Err(message) => {
                        summary.check(&format!("{name}_delta_scf_defined"), false, &message);
                        (f64::NAN, f64::NAN, false, 0)
                    }
                };
            if delta_scf.is_finite() {
                summary.check(
                    &format!("{name}_delta_scf_converged"),
                    excited_converged,
                    &format!("{excited_iterations} iterations"),
                );
                summary.check(
                    &format!("{name}_delta_scf_positive"),
                    delta_scf > 0.0,
                    &format!("E1 - E0 = {delta_scf}, KS gap = {gap}"),
                );
            }
            summary.check(
                &format!("{name}_gap_positive"),
                gap > 0.0,
                &format!("eps_LUMO - eps_HOMO = {gap}"),
            );
            table.push(vec![
                n,
                lh,
                ground.energies.total,
                ground.filling.mu,
                gap,
                delta_scf,
                excited_energy,
                ground.energies.max_lambda_s_over_m,
            ]);
            records.push(Json::object(vec![
                ("label", Json::str(&name)),
                ("N", Json::Float(n)),
                ("lambdaHat", Json::Float(lh)),
                ("E0", Json::Float(ground.energies.total)),
                ("mu", Json::Float(ground.filling.mu)),
                (
                    "epsHomo",
                    Json::Float(ground.filling.homo.map(|h| h.1).unwrap_or(f64::NAN)),
                ),
                (
                    "epsLumo",
                    Json::Float(ground.filling.lumo.map(|h| h.1).unwrap_or(f64::NAN)),
                ),
                ("ksGap", Json::Float(gap)),
                ("deltaScf", Json::Float(delta_scf)),
                ("E1", Json::Float(excited_energy)),
                (
                    "lowestParticleHole",
                    Json::Float(ph.first().map(|p| p.0).unwrap_or(f64::NAN)),
                ),
                (
                    "maxLambdaSOverM",
                    Json::Float(ground.energies.max_lambda_s_over_m),
                ),
                ("groundIterations", Json::Int(ground.iterations as i64)),
                ("excitedIterations", Json::Int(excited_iterations)),
            ]));
        }
    }
    write_csv(
        &dir.join("excitations.csv"),
        &[
            "N",
            "lambda_hat",
            "E0",
            "mu",
            "ks_gap",
            "delta_scf",
            "E1",
            "max_lambda_S_over_m",
        ]
        .iter()
        .map(|s| s.to_string())
        .collect::<Vec<_>>(),
        &table,
    )?;
    summary.add_file("excitations.csv");
    finish(
        ctx,
        &dir,
        &mut summary,
        vec![
            ("reference", reference_json(&reference)),
            ("runs", Json::Array(records)),
        ],
    )?;
    Ok(summary)
}

// ---------------------------------------------------------------------------
// thermo
// ---------------------------------------------------------------------------

pub fn run_thermo(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let dir = ctx.experiment_dir("thermo")?;
    let mut summary = ExperimentSummary::new("thermo");
    let reference = reference(ctx)?;
    let mut records = Vec::new();
    let mut table = Vec::new();
    let temperatures: Vec<f64> = if ctx.quick {
        vec![0.0, 0.1, 0.3]
    } else {
        vec![0.0, 0.1, 0.3, 1.0]
    };
    for n in [8.0, reference.n_mid] {
        for (lname, lh) in lambda_set(&reference, true) {
            let mut previous: Option<Solution> = None;
            let mut previous_free = f64::INFINITY;
            for t in &temperatures {
                let params = params_for(ctx, 1.0, 3.0, lh, *t, n);
                let name = label(&params, &lname);
                let mode = if *t > 0.0 {
                    Occupation::Thermal
                } else {
                    Occupation::Zero
                };
                let solution = solve(
                    &params,
                    &mode,
                    previous.as_ref().map(|p| &p.densities),
                    previous.as_ref().map(|p| p.filling.mu).unwrap_or(0.0),
                )?;
                let (_, e) = write_solution(&dir, &mut summary, &name, &solution)?;
                summary.check(
                    &format!("{name}_converged"),
                    solution.converged,
                    &format!("{} iterations", solution.iterations),
                );
                summary.check(
                    &format!("{name}_particle_number"),
                    (solution.energies.n_total - n).abs() <= 1e-8 * n,
                    &format!("sum weights = {}", solution.energies.n_total),
                );
                // C_V = dE/dT by central differences (fully self-consistent), delta = 0.05 T
                let c_v = if *t > 0.0 {
                    let d = 0.05 * t;
                    let mut e_pm = Vec::new();
                    for f in [-1.0, 1.0] {
                        let mut p = params.clone();
                        p.temperature = t + f * d;
                        let s = solve(
                            &p,
                            &Occupation::Thermal,
                            Some(&solution.densities),
                            solution.filling.mu,
                        )?;
                        if !s.converged {
                            return Err(format!(
                                "{name}: C_V run at T = {} did not converge",
                                p.temperature
                            ));
                        }
                        e_pm.push(s.energies.total);
                    }
                    (e_pm[1] - e_pm[0]) / (2.0 * d)
                } else {
                    0.0
                };
                if *t > 0.0 {
                    summary.check(
                        &format!("{name}_heat_capacity_positive"),
                        c_v > 0.0,
                        &format!("C_V = {c_v}"),
                    );
                    summary.check(
                        &format!("{name}_free_energy_decreases"),
                        solution.energies.free
                            <= previous_free + 1e-9 * previous_free.abs().max(1.0),
                        &format!(
                            "F = {} (previous {})",
                            solution.energies.free, previous_free
                        ),
                    );
                    summary.check(
                        &format!("{name}_entropy_positive"),
                        solution.energies.entropy > 0.0,
                        &format!("S = {}", solution.energies.entropy),
                    );
                }
                previous_free = solution.energies.free;
                let gap = solution.gap().unwrap_or(f64::NAN);
                table.push(vec![
                    n,
                    lh,
                    *t,
                    solution.filling.mu,
                    solution.energies.total,
                    solution.energies.free,
                    solution.energies.entropy,
                    c_v,
                    gap,
                    solution.spectrum.states.len() as f64,
                    solution.spectrum.shells_used as f64,
                    e.w_y,
                    e.w_3,
                    e.brane_fraction,
                ]);
                let mut record = match run_json(&solution, &e) {
                    Json::Object(pairs) => pairs,
                    _ => Vec::new(),
                };
                record.insert(0, ("label".to_string(), Json::str(&name)));
                record.push(("heatCapacity".to_string(), Json::Float(c_v)));
                records.push(Json::Object(record));
                previous = Some(solution);
            }
        }
    }
    write_csv(
        &dir.join("thermodynamics.csv"),
        &[
            "N",
            "lambda_hat",
            "T",
            "mu",
            "E",
            "F",
            "S_entropy",
            "C_V",
            "ks_gap",
            "states",
            "shells",
            "w_y",
            "w_3",
            "brane_fraction",
        ]
        .iter()
        .map(|s| s.to_string())
        .collect::<Vec<_>>(),
        &table,
    )?;
    summary.add_file("thermodynamics.csv");
    finish(
        ctx,
        &dir,
        &mut summary,
        vec![
            ("reference", reference_json(&reference)),
            ("temperaturesOverM", Json::floats(&temperatures)),
            ("runs", Json::Array(records)),
        ],
    )?;
    Ok(summary)
}

// ---------------------------------------------------------------------------
// emt
// ---------------------------------------------------------------------------

pub fn run_emt(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let dir = ctx.experiment_dir("emt")?;
    let mut summary = ExperimentSummary::new("emt");
    let reference = reference(ctx)?;
    let mut records = Vec::new();
    let mut table = Vec::new();
    let mut cases: Vec<(Params, String)> = Vec::new();
    for n in n_set(&reference, ctx.quick) {
        for (lname, lh) in lambda_set(&reference, ctx.quick).iter().take(3) {
            cases.push((params_for(ctx, 1.0, 3.0, *lh, 0.0, n), lname.clone()));
        }
    }
    cases.push((
        params_for(ctx, 1.0, 3.0, reference.lambda_hat_1, 0.3, reference.n_mid),
        "lamp1".to_string(),
    ));
    for (params, lname) in &cases {
        let solution = solve_and_write(ctx, &dir, &mut summary, params, lname, &mut records)?;
        let (_, e) = emt::compute(&solution);
        summary.check(
            &format!(
                "{}_rho_positive_mismatch_with_required_source",
                label(params, lname)
            ),
            e.rho_avg > 0.0 && e.kappa_needed < 0.0,
            &format!(
                "<rho> = {} > 0 while rho_req = -21 H^2/kappa: kappa would have to be {} < 0",
                e.rho_avg, e.kappa_needed
            ),
        );
        table.push(vec![
            params.n_particles,
            params.lambda_hat,
            params.temperature,
            e.rho_avg,
            e.p_y_avg,
            e.p_3_avg,
            e.p_t_avg,
            e.w_y,
            e.w_3,
            e.w_t,
            e.brane_fraction,
            e.tip_fraction,
            e.energy_total,
            e.energy_from_rho,
            e.conservation_max,
            e.rho_required,
            e.kappa_needed,
            e.rho_max,
            e.rho_min,
        ]);
    }
    write_csv(
        &dir.join("emt-summary.csv"),
        &[
            "N",
            "lambda_hat",
            "T",
            "rho_avg",
            "p_y_avg",
            "p_3_avg",
            "p_t_avg",
            "w_y",
            "w_3",
            "w_t",
            "brane_fraction",
            "tip_fraction",
            "E",
            "E_from_rho",
            "conservation_residual",
            "rho_required_kappa1",
            "kappa_needed",
            "rho_max",
            "rho_min",
        ]
        .iter()
        .map(|s| s.to_string())
        .collect::<Vec<_>>(),
        &table,
    )?;
    summary.add_file("emt-summary.csv");
    finish(ctx, &dir, &mut summary, vec![("reference", reference_json(&reference)), ("requiredSource", Json::str("rho_req = -21 H^2/kappa < 0, p_req = +15 H^2/kappa (w_req = -5/7) from G^mu_nu; the Kohn-Sham state has rho > 0")), ("runs", Json::Array(records))])?;
    Ok(summary)
}
