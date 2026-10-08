//! Stage 5: the {+M, -M} pairing of the Kohn-Sham states of dirac16complex
//! and dirac16complex00 in the static primordial field (subcommand `pairs`;
//! STAGE5_SPEC section 5, theorems T3 and T4; the exact theory is
//! `artifacts/dirac16complex/pair-creation/pairing-theory.json`, section T3,
//! written by `wolfram/Dirac16ComplexPairing.wl`).
//!
//! # The three universes of one configuration
//!
//! A configuration is (statistics, |m|, L = 3, N, lambda_hat, T).  For it
//! three Kohn-Sham problems are solved with the Stage-4 machinery
//! (`scf::solve_ground`: exact T = 0 aufbau, continuation in the coupling
//! from lambda = 0 where needed; `scf::delta_scf`; `emt::compute`):
//!
//! * `plusM`: the Stage-4 problem P(m, theta = 0): mass +|m|, tip bag
//!   `b(-L) = 0`, both brane parities (for dirac16complex with m = 1 these
//!   are exactly the Stage-4 runs, and the numbers are compared with the
//!   committed Stage-4 summaries);
//! * `minusM`: the -M universe with the TRANSFORMED boundary conditions:
//!   mass -|m| (bare mass, hence M_eff), the SAME lambda and statistics, the
//!   tip bag `a(-L) = 0` (bag angle theta -> pi - theta = pi), the brane
//!   parity sectors exchanged (both are present in every Stage-4 state, so
//!   this is a relabelling), the same k, N, T and continuation path.  By
//!   pairing-theory.json T3.theoremStandardRule it is the exact image of
//!   plusM under the block form of gamma^8 (sigma2 between the partner
//!   blocks (j, s2, s3) <-> (-j, s2, s3); in this crate's real variables
//!   `chi = (a, i b)`: the swap `(a, b) -> (b, a)` with the block type
//!   s -> -s): identical spectra with multiplicities, occupations, mu, E, F,
//!   S_ent, KS gap, particle-hole list, Delta-SCF, n_p, v_x and EMT profiles
//!   (rho, p_y, p_3, p_t), while S_p and M_eff change sign.  Level map:
//!   `(shell, parity p, block type s, Pruefer index n) -> (shell, -p, -s,
//!   -n)` with the same eps (shooting.rs header);
//! * `minusM_control`: mass -|m| with the UNTRANSFORMED tip bag `b(-L) = 0`
//!   (T3.untransformedBCControl): a different problem, with the
//!   tip-localised zero mode `(e^{-My}, 0)`, the mixed-sector levels
//!   `q cos qL - M sin qL = 0` instead of `q cos qL + M sin qL = 0`, and a
//!   sub-gap bound state `tanh(kappa L) = kappa/M` for M L > 1.  Its ground
//!   state is solved by the direct Stage-4 SCF attempt without the coupling
//!   continuation ([`GroundSolver::Direct`]; converged results are
//!   identical to `solve_ground`'s, non-converged ones are recorded), and
//!   only when its first SCF update satisfies the window premise of the
//!   solver ([`first_update_shift`]); at lambda = 0 it always runs (the
//!   exact control of the theory).  At lambda != 0 the free control state
//!   has its zero modes at the tip, where the proper-density factor is
//!   e^{6HL}; a control whose first update violates the premise is
//!   recorded as not run, with the measured shift bound (pairing.json,
//!   summary.json controlOutcomes; for plusM the first-order
//!   pseudo-potential is 0.1 |m| resp. 1 |m| by the construction of
//!   lambda_hat_1,2).
//!
//! # What is compared and reported
//!
//! * Pairing deviations plusM vs minusM (they must vanish to solver
//!   precision): levels by the key map (eps, f, weight, multiplicity), the
//!   sorted spectra, the orbital swap `(a, b) -> +-(b, a)` of every matched
//!   level, mu, E, F, S_ent, N, KS gap, the particle-hole list, Delta-SCF
//!   (T = 0), the profiles n_c, n_p, v_x, rho, p_y, p_3, p_t (equal) and
//!   S_c, S_p, M_eff (opposite), the EMT proper-volume averages.
//! * Pair totals (T3.pairTotalsKS): the mirror pair plusM + minusM (the
//!   ordinary -M universe with the standard expectation rule and the same
//!   lambda): E = 2E_+, N = 2N, S = 0, EMT averages doubled; the Krein-image
//!   pair plusM - minusM (the gamma^8 image with the Krein metric -B, which
//!   carries -lambda and reverses every one-body density and energy;
//!   T3.theoremImageRule): E = 0, charge 0, <rho> = <p_y> = <p_3> = <p_t> = 0,
//!   S = 2 S_+.
//! * The control: plusM vs minusM_control (must differ).
//! * The opposite coupling: plusM(lambda) vs minusM(-lambda) (the ordinary
//!   KS problem with -lambda does NOT map, T3.whatMustTransform.lambda).
//! * The two statistics at lambda = 0 are the same problem (bit for bit).
//! * A lambda-independent free section: the free spectra of the three
//!   universes (m in {1, 3}, L in {2, 3, 4}), the key map on them, the
//!   analytic k = 0 box spectra (with the control's mixed-sector levels and
//!   bound state), the zero-mode profiles and their localisation, the
//!   first-order splitting constants c(M) and c_ctrl(M) against the closed
//!   forms (and the values exported in pairing-theory.json), and the 16 x 16
//!   block map of gamma^8 in this crate's basis.
//!
//! # First excited state
//!
//! T = 0: the KS gap, the particle-hole list with the occupation floor 1e-12
//! (STAGE4_SPEC E4.9, as `runs::excited_run`) and Delta-SCF.  T > 0 (T/m =
//! 0.1 for one N): the Mermin state (mu, E, F, S_ent), the KS gap (HOMO/LUMO:
//! highest particle level with f >= 1/2, lowest with f < 1/2) and the
//! particle-hole list with the finite-T rule (holes f >= 1/2, particles
//! f < 1/2, E4.9); the excitation spectrum is the run's levels.csv.
//! Delta-SCF is the T = 0 construction of Stage 4 (scf::delta_scf fills the
//! sea completely) and is not computed at T > 0.
//!
//! # Units and negative mass
//!
//! H = 1; lambda_hat = lambda m^6 is even in m, so the -M universes carry the
//! same lambda; Delta k = 0.25 |m|, the windows, margins, smearings and the
//! ratios max|lambda S_p|/m, max|v_x|/m use |m| (`Params::mass_scale`); T is
//! given in units of |m|.  The couplings lambda_hat_1,2 of (|m|, L, N) are
//! the Stage-4 ones (`runs::Reference::coupling`, the free plusM ground
//! state), used unchanged for both statistics.
//!
//! Output (default root `artifacts/dirac16complex/pair-creation/rust`):
//! `<root>/pairs/` with `summary.json`, `pairs-summary.csv`,
//! `free-spectrum-m<m>-L<L>-<universe>.csv`, `free-section.json` and one
//! directory per configuration, `<label>/pairing.json` and
//! `<label>/<universe>/{levels.csv, profiles.csv, history.csv,
//! particle-hole.csv, levels-excited.csv (T = 0), run.json}`.

use std::collections::HashMap;
use std::path::Path;
use std::sync::Arc;

use crate::blocks::{self, C16};
use crate::emt;
use crate::exchange::Statistics;
use crate::jsonread;
use crate::math::{cos, exp, sin, tanh, PI};
use crate::output::{write_csv, write_json, Json};
use crate::runs::{
    finish, lambda_set, levels_header, levels_rows, params_for, reference, reference_json,
    run_json, tolerances_of, trim_float, Reference, PH_OCCUPATION_FLOOR,
};
use crate::scf::{
    self, compute_spectrum, delta_scf, particle_number_from_density, solve_ground, Densities, Key,
    Occupation, Params, Solution, Spectrum, State, Window,
};
use crate::shooting::{Potential, Shooter, TipBag};
use crate::{ExperimentSummary, RunContext};

/// Default output root of `pairs` (the subcommand writes into `<root>/pairs/`).
pub const PAIRS_OUTPUT_ROOT: &str = "artifacts/dirac16complex/pair-creation/rust";
/// The exact pairing theory (Wolfram export), read for cross-checks.
pub const PAIRING_THEORY_PATH: &str = "artifacts/dirac16complex/pair-creation/pairing-theory.json";
/// Committed Stage-4 summaries (read only) for the plusM reproduction checks.
pub const STAGE4_EXCITED_SUMMARY: &str =
    "artifacts/dirac16complex/kohn-sham/rust/excited/summary.json";
pub const STAGE4_SCF_SUMMARY: &str = "artifacts/dirac16complex/kohn-sham/rust/scf/summary.json";
pub const STAGE4_SPECTRUM_DIR: &str = "artifacts/dirac16complex/kohn-sham/rust/spectrum";
/// Tip cutoff of the pairs matrix (STAGE5_SPEC T4).
pub const PAIRS_LENGTH: f64 = 3.0;
/// Temperature of the finite-T runs, in units of |m|.
pub const THERMAL_T_OVER_M: f64 = 0.1;
// The finite-T runs use N = N_mid(|m|) of the Stage-4 reference (112 for
// |m| = 1 and 3; `--quick`: N = 8), see [`matrix`].

/// Pairing tolerances ("solver precision"): eigenvalues and orbital
/// energies (absolute, units of |m|).
pub const PAIRING_EPS_TOLERANCE: f64 = 1.0e-8;
/// Energies E, F, mu, S_ent, N, gap, Delta-SCF: |dX| <= rtol |X| + atol |m|.
pub const PAIRING_ENERGY_RTOL: f64 = 1.0e-8;
pub const PAIRING_ENERGY_ATOL: f64 = 1.0e-9;
/// Occupations and weights (absolute).
pub const PAIRING_OCCUPATION_TOLERANCE: f64 = 1.0e-7;
/// Profiles (n, S, M_eff, v_x, rho, p's): max |dX| <= rtol max |X|.
pub const PAIRING_PROFILE_RTOL: f64 = 1.0e-7;
/// Normalised orbitals: max |a_+ - sigma b_-|, |b_+ - sigma a_-|.
pub const PAIRING_ORBITAL_TOLERANCE: f64 = 1.0e-7;
/// The control and the opposite coupling must differ by more than this
/// factor times the pairing deviation of the same quantity (and by more
/// than CONTROL_MIN_DIFFERENCE absolutely).
pub const CONTROL_FACTOR: f64 = 1.0e3;
pub const CONTROL_MIN_DIFFERENCE: f64 = 1.0e-6;
/// Small momentum of the first-order zero-mode splitting (d eps/dk by
/// Hellmann-Feynman at this k; eps(k) is odd in k, so the error is O(k^2)).
pub const SPLITTING_K: f64 = 1.0e-4;

/// The three universes of a configuration.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Universe {
    /// +|m|, tip bag b(-L) = 0 (the Stage-4 problem).
    Plus,
    /// -|m|, tip bag a(-L) = 0 (the transformed boundary conditions).
    Minus,
    /// -|m|, tip bag b(-L) = 0 (untransformed: the control).
    Control,
}

impl Universe {
    pub const ALL: [Universe; 3] = [Universe::Plus, Universe::Minus, Universe::Control];

    pub fn mass_sign(self) -> f64 {
        match self {
            Universe::Plus => 1.0,
            Universe::Minus | Universe::Control => -1.0,
        }
    }

    pub fn tip(self) -> TipBag {
        match self {
            Universe::Minus => TipBag::A,
            Universe::Plus | Universe::Control => TipBag::B,
        }
    }

    pub fn name(self) -> &'static str {
        match self {
            Universe::Plus => "plusM",
            Universe::Minus => "minusM",
            Universe::Control => "minusM_control",
        }
    }

    /// Ground-state solver of the universe ([`GroundSolver`]).
    pub fn solver(self) -> GroundSolver {
        match self {
            Universe::Plus | Universe::Minus => GroundSolver::Continuation,
            Universe::Control => GroundSolver::Direct,
        }
    }

    pub fn describe(self) -> &'static str {
        match self {
            Universe::Plus => "+M universe: mass +|m|, tip bag b(-L) = 0 (theta = 0), both brane parities (the Stage-4 problem)",
            Universe::Minus => "-M universe with the transformed boundary conditions: mass -|m|, the same lambda and statistics, tip bag a(-L) = 0 (theta = pi), both brane parities (exchanged)",
            Universe::Control => "-M universe with the UNTRANSFORMED boundary conditions (control): mass -|m|, tip bag b(-L) = 0 (theta = 0), both brane parities; ground state by the direct Stage-4 SCF attempt (no coupling continuation), run only when its first SCF update satisfies the window premise of the solver",
        }
    }
}

/// Image of a level key under the block map of gamma^8:
/// (shell, parity, block type, Pruefer index) -> (shell, -parity, -type, -index).
pub fn image_key(key: Key) -> Key {
    (key.0, -key.1, -key.2, -key.3)
}

/// One configuration of the pairs matrix.
#[derive(Clone, Debug)]
pub struct Config {
    pub statistics: Statistics,
    /// |m| > 0.
    pub mass: f64,
    pub length: f64,
    pub n: f64,
    pub lambda_name: String,
    pub lambda_hat: f64,
    /// T / |m|.
    pub t_over_m: f64,
}

impl Config {
    pub fn label(&self) -> String {
        let t = if self.t_over_m == 0.0 {
            "T0".to_string()
        } else {
            format!("T{}", trim_float(self.t_over_m))
        };
        format!(
            "{}_m{}_L{}_N{}_{}_{}",
            self.statistics.short_label(),
            trim_float(self.mass),
            trim_float(self.length),
            self.n as i64,
            self.lambda_name,
            t
        )
    }

    /// Label of the same configuration with another coupling name.
    pub fn label_with(&self, lambda_name: &str) -> String {
        let mut other = self.clone();
        other.lambda_name = lambda_name.to_string();
        other.label()
    }

    /// The requested Kohn-Sham parameters of one universe.
    pub fn params(&self, ctx: &RunContext, universe: Universe) -> Params {
        let mut p = params_for(
            ctx,
            universe.mass_sign() * self.mass,
            self.length,
            self.lambda_hat,
            self.t_over_m * self.mass,
            self.n,
        );
        p.statistics = self.statistics;
        p.tip_bag = universe.tip();
        p
    }

    pub fn to_json(&self) -> Json {
        Json::object(vec![
            ("label", Json::str(&self.label())),
            ("statistics", Json::str(self.statistics.field_name())),
            ("exchangeSign", Json::Float(self.statistics.sign())),
            (
                "massCoefficient_MeffEquals_m_plus_coefficient_lambda_Sp",
                Json::Float(self.statistics.mass_coefficient()),
            ),
            ("absMass", Json::Float(self.mass)),
            ("L", Json::Float(self.length)),
            ("N", Json::Float(self.n)),
            ("lambdaName", Json::str(&self.lambda_name)),
            ("lambdaHat", Json::Float(self.lambda_hat)),
            ("lambda", Json::Float(self.lambda_hat / self.mass.powi(6))),
            ("TOverAbsM", Json::Float(self.t_over_m)),
            ("T", Json::Float(self.t_over_m * self.mass)),
        ])
    }
}

// ---------------------------------------------------------------------------
// one universe: ground state, first excited state, EMT, files
// ---------------------------------------------------------------------------

/// Particle-hole excitation (energy, eps_hole, eps_particle, k_hole, k_particle).
pub type Excitation = (f64, f64, f64, f64, f64);

/// Number of particle-hole excitations listed (as in Stage 4).
pub const PARTICLE_HOLE_COUNT: usize = 12;

/// Particle-hole list of a ground state (particle-branch levels only, as in
/// Stage 4).  T = 0 (exact or smeared occupations): holes f >
/// PH_OCCUPATION_FLOOR, particles f < 1 - PH_OCCUPATION_FLOOR (identical to
/// `runs::excited_run`); T > 0: holes f >= 1/2, particles f < 1/2
/// (STAGE4_SPEC E4.9).
pub fn particle_hole(ground: &Solution) -> Vec<Excitation> {
    let thermal = ground.params.temperature > 0.0;
    let is_hole = |s: &State| {
        s.branch > 0
            && if thermal {
                s.f >= 0.5
            } else {
                s.f > PH_OCCUPATION_FLOOR
            }
    };
    let is_particle = |s: &State| {
        s.branch > 0
            && if thermal {
                s.f < 0.5
            } else {
                s.f < 1.0 - PH_OCCUPATION_FLOOR
            }
    };
    let occupied: Vec<&State> = ground
        .spectrum
        .states
        .iter()
        .filter(|s| is_hole(s))
        .collect();
    let empty: Vec<&State> = ground
        .spectrum
        .states
        .iter()
        .filter(|s| is_particle(s))
        .collect();
    let mut ph: Vec<Excitation> = Vec::new();
    for i in &occupied {
        for a in &empty {
            if a.eps > i.eps {
                ph.push((a.eps - i.eps, i.eps, a.eps, i.k, a.k));
            }
        }
    }
    ph.sort_by(|x, y| x.0.partial_cmp(&y.0).unwrap_or(std::cmp::Ordering::Equal));
    ph.truncate(PARTICLE_HOLE_COUNT);
    ph
}

/// Everything computed for one universe.
pub struct UniverseData {
    pub ground: Solution,
    pub rows: Vec<emt::Row>,
    pub emt: emt::Summary,
    pub excitations: Vec<Excitation>,
    /// T = 0: the Delta-SCF state (Err: why it is undefined); T > 0: None.
    pub excited: Option<Result<Solution, String>>,
}

impl UniverseData {
    pub fn gap(&self) -> f64 {
        self.ground.gap().unwrap_or(f64::NAN)
    }

    pub fn delta_scf(&self) -> f64 {
        match &self.excited {
            Some(Ok(ex)) => ex.energies.total - self.ground.energies.total,
            _ => f64::NAN,
        }
    }

    pub fn excited_energy(&self) -> f64 {
        match &self.excited {
            Some(Ok(ex)) => ex.energies.total,
            _ => f64::NAN,
        }
    }

    pub fn excited_converged(&self) -> bool {
        matches!(&self.excited, Some(Ok(ex)) if ex.converged)
    }
}

/// How the ground state of a universe is solved.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum GroundSolver {
    /// `scf::solve_ground` (plusM, minusM): the exact T = 0 occupations
    /// first and, only if they do not converge, the continuation in the
    /// coupling from lambda = 0 with the smearing ladder (STAGE4_SPEC E4.8);
    /// at T > 0 the Fermi-Dirac loop.
    Continuation,
    /// The direct attempt of `solve_ground` only (the control): the same
    /// SCF loop with the Stage-4 limits (80 iterations, stagnation after 20
    /// without a factor-2 improvement); when it converges the result is
    /// identical to `solve_ground`'s, when it does not, the continuation
    /// (up to 2400 further iterations) is not attempted and the outcome is
    /// recorded as not converged.  Reason (measured): at lambda != 0 the
    /// control's tip-localised zero modes sit where the proper-density
    /// factor e^{-6Hy} is e^{6HL} = 6.6e7 (L = 3), so |lambda S_p| and
    /// |v_x| exceed the window premise of the solver already at
    /// lambda_hat_1; the control is not the image of the +M universe, and
    /// its only role is to show that the pairing fails without the
    /// transformed boundary conditions (exactly so at lambda = 0).  The
    /// control is run only when its FIRST SCF update satisfies the window
    /// premise ([`first_update_shift`] <= |window floor|, the solver's own
    /// validity condition; the analogue of the Stage-4 thermo rule that runs
    /// a point only when its first-order pseudo-potential lies inside the
    /// window); otherwise it is recorded as not run, with the measured
    /// first-update shift bound.
    Direct,
}

/// The first SCF update of a universe: one SCF iteration from zero
/// densities (the free state of its boundary conditions, occupied as in the
/// run) and the shift bound max|M_eff - m| + max|v_x| of the potentials its
/// output densities produce, with |window floor| (the premise of the
/// solver's windows, see [`Digest::window_floor`]).  Returns (shift bound,
/// |window floor|).
pub fn first_update_shift(params: &Params) -> Result<(f64, f64), String> {
    let mut p = params.clone();
    p.max_iter = 1;
    let mode = if p.temperature > 0.0 {
        Occupation::Thermal
    } else {
        Occupation::Zero
    };
    let first = scf::solve(&p, &mode, None, 0.0)?;
    let potential = scf::build_potential(params, &first.densities);
    let shift = potential
        .m_eff
        .values
        .iter()
        .map(|m| (m - params.m).abs())
        .fold(0.0, f64::max)
        + potential
            .v_x
            .values
            .iter()
            .map(|v| v.abs())
            .fold(0.0, f64::max);
    Ok((shift, -params.window_floor()))
}

/// Ground state (from zero densities; see [`GroundSolver`]), EMT, the
/// particle-hole list and, at T = 0, Delta-SCF (for the direct solver only
/// when the ground state converged).
pub fn compute_universe(params: &Params, solver: GroundSolver) -> Result<UniverseData, String> {
    let ground = match solver {
        GroundSolver::Continuation => solve_ground(params, None, 0.0)?,
        GroundSolver::Direct => {
            let mode = if params.temperature > 0.0 {
                Occupation::Thermal
            } else {
                Occupation::Zero
            };
            scf::solve(params, &mode, None, 0.0)?
        }
    };
    let (rows, emt_summary) = emt::compute(&ground);
    let excitations = particle_hole(&ground);
    let excited = if params.temperature > 0.0 {
        None
    } else if solver == GroundSolver::Direct && !ground.converged {
        Some(Err(
            "Delta-SCF not attempted: the ground state of the direct SCF attempt did not converge"
                .to_string(),
        ))
    } else {
        Some(delta_scf(&ground))
    };
    Ok(UniverseData {
        ground,
        rows,
        emt: emt_summary,
        excitations,
        excited,
    })
}

fn header(names: &[&str]) -> Vec<String> {
    names.iter().map(|s| s.to_string()).collect()
}

/// The profile table of `runs::write_solution` (same columns).
fn profile_table(solution: &Solution, rows: &[emt::Row]) -> (Vec<String>, Vec<Vec<f64>>) {
    let homo_key = solution.filling.homo.map(|h| h.0);
    let homo = homo_key.and_then(|key| solution.spectrum.states.iter().find(|s| s.key() == key));
    let names = header(&[
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
    ]);
    let table = rows
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
    (names, table)
}

fn history_table(solution: &Solution) -> (Vec<String>, Vec<Vec<f64>>) {
    let names = header(&[
        "iteration",
        "residual_n",
        "residual_S",
        "mu",
        "E",
        "F",
        "states",
        "integrations",
    ]);
    let rows = solution
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
    (names, rows)
}

fn pair_run_json(cfg: &Config, universe: Universe, params: &Params) -> Json {
    let mut pairs = match cfg.to_json() {
        Json::Object(p) => p,
        _ => Vec::new(),
    };
    pairs.push(("universe".to_string(), Json::str(universe.name())));
    pairs.push((
        "universeDescription".to_string(),
        Json::str(universe.describe()),
    ));
    pairs.push(("m".to_string(), Json::Float(params.m)));
    pairs.push(("tipBag".to_string(), Json::str(params.tip_bag.describe())));
    pairs.push((
        "bagAngleTheta".to_string(),
        Json::Float(params.tip_bag.bag_angle()),
    ));
    pairs.push((
        "brane".to_string(),
        Json::str("both parity sectors: parity + b(0) = 0, parity - a(0) = 0 (chi = (a, i b))"),
    ));
    pairs.push((
        "requestedParameters".to_string(),
        crate::runs::params_json(params),
    ));
    Json::Object(pairs)
}

fn excited_json(d: &UniverseData) -> Json {
    let thermal = d.ground.params.temperature > 0.0;
    let mut pairs: Vec<(&str, Json)> = vec![
        ("ksGap", Json::Float(d.gap())),
        (
            "epsHomo",
            Json::Float(d.ground.filling.homo.map(|h| h.1).unwrap_or(f64::NAN)),
        ),
        (
            "epsLumo",
            Json::Float(d.ground.filling.lumo.map(|h| h.1).unwrap_or(f64::NAN)),
        ),
        (
            "particleHoleRule",
            Json::str(if thermal {
                "T > 0 (STAGE4_SPEC E4.9): holes f >= 1/2, particles f < 1/2 (particle branch)"
            } else {
                "T = 0 (STAGE4_SPEC E4.9): holes f > 1e-12, particles f < 1 - 1e-12 (particle branch)"
            }),
        ),
        (
            "lowestParticleHole",
            Json::Float(d.excitations.first().map(|p| p.0).unwrap_or(f64::NAN)),
        ),
        (
            "particleHoleExcitations",
            Json::floats(&d.excitations.iter().map(|p| p.0).collect::<Vec<_>>()),
        ),
    ];
    match &d.excited {
        None => pairs.push((
            "deltaScf",
            Json::str("not computed at T > 0: Delta-SCF is the T = 0 construction of Stage 4; the finite-T excitation spectrum is levels.csv"),
        )),
        Some(Ok(ex)) => {
            pairs.push(("deltaScf", Json::Float(d.delta_scf())));
            pairs.push(("E1", Json::Float(ex.energies.total)));
            pairs.push(("excitedConverged", Json::Bool(ex.converged)));
            pairs.push(("excitedIterations", Json::Int(ex.iterations as i64)));
        }
        Some(Err(message)) => {
            pairs.push(("deltaScf", Json::Float(f64::NAN)));
            pairs.push(("deltaScfError", Json::str(message)));
        }
    }
    Json::object(pairs)
}

/// Write the files of one universe into `<dir>/<label>/<universe>/`.
fn write_universe(
    dir: &Path,
    summary: &mut ExperimentSummary,
    cfg: &Config,
    universe: Universe,
    params: &Params,
    outcome: &Result<UniverseData, String>,
) -> Result<(), String> {
    let rel = format!("{}/{}", cfg.label(), universe.name());
    let sub = dir.join(&rel);
    std::fs::create_dir_all(&sub).map_err(|e| format!("cannot create {}: {e}", sub.display()))?;
    let d = match outcome {
        Err(message) => {
            write_json(
                &sub.join("run.json"),
                &Json::object(vec![
                    ("label", Json::str(&rel)),
                    ("universe", Json::str(universe.name())),
                    ("pairRun", pair_run_json(cfg, universe, params)),
                    ("error", Json::str(message)),
                ]),
            )?;
            summary.add_file(&format!("{rel}/run.json"));
            return Ok(());
        }
        Ok(d) => d,
    };
    summary.add_stats(d.ground.stats.steps, d.ground.stats.rhs_evals);
    write_csv(
        &sub.join("levels.csv"),
        &levels_header(),
        &levels_rows(&d.ground.spectrum),
    )?;
    summary.add_file(&format!("{rel}/levels.csv"));
    let (names, table) = profile_table(&d.ground, &d.rows);
    write_csv(&sub.join("profiles.csv"), &names, &table)?;
    summary.add_file(&format!("{rel}/profiles.csv"));
    let (names, table) = history_table(&d.ground);
    write_csv(&sub.join("history.csv"), &names, &table)?;
    summary.add_file(&format!("{rel}/history.csv"));
    let ph_rows: Vec<Vec<f64>> = d
        .excitations
        .iter()
        .map(|p| vec![p.0, p.1, p.2, p.3, p.4])
        .collect();
    write_csv(
        &sub.join("particle-hole.csv"),
        &header(&[
            "excitation",
            "eps_hole",
            "eps_particle",
            "k_hole",
            "k_particle",
        ]),
        &ph_rows,
    )?;
    summary.add_file(&format!("{rel}/particle-hole.csv"));
    if let Some(Ok(ex)) = &d.excited {
        summary.add_stats(ex.stats.steps, ex.stats.rhs_evals);
        write_csv(
            &sub.join("levels-excited.csv"),
            &levels_header(),
            &levels_rows(&ex.spectrum),
        )?;
        summary.add_file(&format!("{rel}/levels-excited.csv"));
    }
    let mut record = match run_json(&d.ground, &d.emt) {
        Json::Object(pairs) => pairs,
        _ => Vec::new(),
    };
    record.insert(0, ("label".to_string(), Json::str(&rel)));
    record.insert(1, ("universe".to_string(), Json::str(universe.name())));
    record.push(("pairRun".to_string(), pair_run_json(cfg, universe, params)));
    record.push(("firstExcitedState".to_string(), excited_json(d)));
    write_json(&sub.join("run.json"), &Json::Object(record))?;
    summary.add_file(&format!("{rel}/run.json"));
    Ok(())
}

// ---------------------------------------------------------------------------
// digests and pairing deviations
// ---------------------------------------------------------------------------

/// Compact record of one universe (kept for the comparisons across
/// configurations: opposite coupling, statistics at lambda = 0).
#[derive(Clone, Debug)]
pub struct Digest {
    pub converged: bool,
    pub fallback_stage: i32,
    pub smearing: f64,
    pub iterations: usize,
    /// (key, eps, f, weight, multiplicity), in spectrum order.
    pub levels: Vec<(Key, f64, f64, f64, f64)>,
    pub energy: f64,
    pub free: f64,
    pub mu: f64,
    pub entropy: f64,
    pub n_total: f64,
    pub n_density: f64,
    pub scalar_total: f64,
    pub gap: f64,
    pub delta_scf: f64,
    pub excited_energy: f64,
    pub excited_converged: bool,
    pub excitations: Vec<f64>,
    /// Profiles on the grid, in the order of [`PROFILE_NAMES`].
    pub profiles: Vec<Vec<f64>>,
    /// Proper-volume averages, in the order of [`AVERAGE_NAMES`].
    pub averages: Vec<f64>,
    pub energy_from_rho: f64,
    pub conservation_max: f64,
    pub max_lambda_s_over_m: f64,
    pub max_v_x_over_m: f64,
    /// max|M_eff - m| + max|v_x| of the final potentials: the largest shift
    /// of a level from its free partner (scf.rs, FreeLevels::classify).
    pub shift_bound: f64,
    /// The window floor of the solver (every particle-branch level lies
    /// above it when shift_bound <= -window_floor: the premise of the
    /// Stage-4 windows, see Params::window_floor).
    pub window_floor: f64,
    /// Proper-density factor e^{-6Hy} on the grid (proper = factor x coordinate).
    pub factor: Vec<f64>,
    /// The SCF convergence norm D = max(max|n_c|, max|S_c|) of the output
    /// densities (scf.rs: the residuals are max|out - in| / D).
    pub density_scale: f64,
    /// The residuals max|n_out - n_in| / D and max|S_out - S_in| / D of the
    /// last iteration (whose input densities built the final potentials).
    pub final_residual_n: f64,
    pub final_residual_s: f64,
    /// Proper 7-volume (per coordinate extra-time volume) of the grid.
    pub proper_volume: f64,
    /// lambda of the run.
    pub lambda: f64,
}

/// How a profile is compared (the norm of the pairing check).
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum ProfileNorm {
    /// Coordinate densities n_c, S_c: max|X_+ - sign X_-| / D, with D the
    /// SCF convergence norm max(max|n_c|, max|S_c|) (scf.rs): the SCF fixes
    /// both densities only to tol x D, so a density that is small compared
    /// with D (S_c of the brane zero modes) cannot pair better than that.
    Density,
    /// Proper densities n_p, S_p (factor e^{-6Hy} x coordinate): compared
    /// divided by the factor, in the norm D.  (Relative to their own maximum
    /// the tip amplification e^{6HL} of the SCF resolution would dominate.)
    ProperDensity,
    /// v_x = sg (lambda/16) n_p: divided by the factor, in the norm
    /// (|lambda|/16) D.
    ProperPotential,
    /// M_eff: max|M_+ + M_-| / max|M_eff| (M_eff ~ +-m, no cancellation).
    Mass,
    /// EMT profiles rho, p_y, p_3, p_t (proper): divided by the factor,
    /// relative to the maximum of the quotient.
    ProperEmt,
}

/// Profile names, the sign they carry under the pairing map (+1:
/// identical, -1: opposite) and the norm of the comparison.
pub const PROFILE_NAMES: [(&str, f64, ProfileNorm); 10] = [
    ("n_c", 1.0, ProfileNorm::Density),
    ("n_p", 1.0, ProfileNorm::ProperDensity),
    ("v_x", 1.0, ProfileNorm::ProperPotential),
    ("rho", 1.0, ProfileNorm::ProperEmt),
    ("p_y", 1.0, ProfileNorm::ProperEmt),
    ("p_3", 1.0, ProfileNorm::ProperEmt),
    ("p_t", 1.0, ProfileNorm::ProperEmt),
    ("S_c", -1.0, ProfileNorm::Density),
    ("S_p", -1.0, ProfileNorm::ProperDensity),
    ("M_eff", -1.0, ProfileNorm::Mass),
];

/// Proper-volume averages and their sign under the pairing map.
pub const AVERAGE_NAMES: [(&str, f64); 6] = [
    ("rhoAvg", 1.0),
    ("pYAvg", 1.0),
    ("p3Avg", 1.0),
    ("pTAvg", 1.0),
    ("nPAvg", 1.0),
    ("sPAvg", -1.0),
];

impl Digest {
    pub fn of(d: &UniverseData) -> Self {
        let g = &d.ground;
        let rows = &d.rows;
        let column = |f: &dyn Fn(&emt::Row) -> f64| -> Vec<f64> { rows.iter().map(f).collect() };
        let profiles = vec![
            column(&|r| r.n_c),
            column(&|r| r.n_p),
            column(&|r| r.v_x),
            column(&|r| r.rho),
            column(&|r| r.p_y),
            column(&|r| r.p_3),
            column(&|r| r.p_t),
            column(&|r| r.s_c),
            column(&|r| r.s_p),
            column(&|r| r.m_eff),
        ];
        let e = &d.emt;
        Digest {
            converged: g.converged,
            fallback_stage: g.params.fallback_stage,
            smearing: g.params.smearing,
            iterations: g.iterations,
            levels: g
                .spectrum
                .states
                .iter()
                .map(|s| (s.key(), s.eps, s.f, s.weight, s.mult))
                .collect(),
            energy: g.energies.total,
            free: g.energies.free,
            mu: g.filling.mu,
            entropy: g.energies.entropy,
            n_total: g.energies.n_total,
            n_density: particle_number_from_density(&g.params, &g.densities),
            scalar_total: g.energies.scalar_total,
            gap: d.gap(),
            delta_scf: d.delta_scf(),
            excited_energy: d.excited_energy(),
            excited_converged: d.excited_converged(),
            excitations: d.excitations.iter().map(|p| p.0).collect(),
            profiles,
            averages: vec![
                e.rho_avg, e.p_y_avg, e.p_3_avg, e.p_t_avg, e.n_p_avg, e.s_p_avg,
            ],
            energy_from_rho: e.energy_from_rho,
            conservation_max: e.conservation_max,
            max_lambda_s_over_m: g.energies.max_lambda_s_over_m,
            max_v_x_over_m: g.energies.max_v_x_over_m,
            shift_bound: g
                .potential
                .m_eff
                .values
                .iter()
                .map(|m| (m - g.params.m).abs())
                .fold(0.0, f64::max)
                + g.potential
                    .v_x
                    .values
                    .iter()
                    .map(|v| v.abs())
                    .fold(0.0, f64::max),
            window_floor: g.params.window_floor(),
            factor: rows
                .iter()
                .map(|r| crate::geometry::density_factor(g.params.h, r.y))
                .collect(),
            density_scale: {
                let n = g
                    .densities
                    .n_c
                    .iter()
                    .map(|v| v.abs())
                    .fold(1e-300, f64::max);
                let s = g
                    .densities
                    .s_c
                    .iter()
                    .map(|v| v.abs())
                    .fold(1e-300, f64::max);
                n.max(s)
            },
            final_residual_n: g.history.last().map(|h| h.residual_n).unwrap_or(f64::NAN),
            final_residual_s: g.history.last().map(|h| h.residual_s).unwrap_or(f64::NAN),
            proper_volume: e.proper_volume,
            lambda: g.params.lambda(),
        }
    }

    /// The window premise of the solver holds (see [`Digest::window_floor`]).
    pub fn window_premise(&self) -> bool {
        self.shift_bound <= -self.window_floor
    }

    /// Bitwise equality of every number (the statistics identity at lambda = 0).
    pub fn bitwise_equal(&self, other: &Digest) -> bool {
        // +0 and -0 count as equal: every writer prints v + 0.0 (output.rs)
        let same = |a: f64, b: f64| {
            (a + 0.0).to_bits() == (b + 0.0).to_bits() || (a.is_nan() && b.is_nan())
        };
        let same_vec =
            |a: &[f64], b: &[f64]| a.len() == b.len() && a.iter().zip(b).all(|(x, y)| same(*x, *y));
        self.converged == other.converged
            && self.iterations == other.iterations
            && self.levels.len() == other.levels.len()
            && self.levels.iter().zip(&other.levels).all(|(x, y)| {
                x.0 == y.0 && same(x.1, y.1) && same(x.2, y.2) && same(x.3, y.3) && same(x.4, y.4)
            })
            && same(self.energy, other.energy)
            && same(self.free, other.free)
            && same(self.mu, other.mu)
            && same(self.entropy, other.entropy)
            && same(self.scalar_total, other.scalar_total)
            && same(self.gap, other.gap)
            && same(self.delta_scf, other.delta_scf)
            && same_vec(&self.excitations, &other.excitations)
            && self
                .profiles
                .iter()
                .zip(&other.profiles)
                .all(|(a, b)| same_vec(a, b))
            && same_vec(&self.averages, &other.averages)
    }
}

/// (max |x_i - sign y_i|, max(max|x|, max|y|)).
pub fn profile_deviation(x: &[f64], y: &[f64], sign: f64) -> (f64, f64) {
    if x.len() != y.len() {
        return (f64::INFINITY, 0.0);
    }
    let dev = x
        .iter()
        .zip(y)
        .map(|(a, b)| (a - sign * b).abs())
        .fold(0.0, f64::max);
    let scale = x.iter().chain(y).map(|v| v.abs()).fold(0.0, f64::max);
    (dev, scale)
}

/// Every eps repeated by its multiplicity, sorted (a key-independent
/// description of the spectrum with degeneracies).
pub fn spectrum_multiset(levels: &[(Key, f64, f64, f64, f64)]) -> Vec<f64> {
    let mut out: Vec<f64> = Vec::new();
    for (_, eps, _, _, mult) in levels {
        for _ in 0..(mult.round() as usize) {
            out.push(*eps);
        }
    }
    out.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
    out
}

/// Deviation of universe b from the pairing image of universe a.
#[derive(Clone, Debug, Default)]
pub struct Deviation {
    pub states_a: usize,
    pub states_b: usize,
    pub matched: usize,
    pub mult_mismatch: usize,
    pub max_eps: f64,
    pub max_f: f64,
    pub max_weight: f64,
    /// Multisets (eps repeated by multiplicity): number of entries and the
    /// max |d eps| (NaN when the counts differ).
    pub multiset_a: usize,
    pub multiset_b: usize,
    pub sorted_eps: f64,
    /// (name, |a - b|, |a|) for the scalar observables that must coincide.
    pub scalars: Vec<(&'static str, f64, f64)>,
    /// |S_a + S_b| and |S_a| of the total scalar charge (must flip).
    pub scalar_total_flip: (f64, f64),
    /// Particle-hole excitation energies: max |d| (NaN when the counts differ).
    pub excitations: f64,
    /// (name, sign, deviation in the norm of [`ProfileNorm`], that norm,
    /// raw max |a - sign b|, raw max(max|a|, max|b|)) of the profiles.
    pub profiles: Vec<(&'static str, f64, f64, f64, f64, f64)>,
    /// (name, sign, |a - sign b|, max(|a|, |b|), |a - sign b| x proper
    /// volume) of the proper-volume averages.
    pub averages: Vec<(&'static str, f64, f64, f64, f64)>,
    /// Orbitals: max over matched levels of min over sigma of
    /// max_y (|a_a - sigma b_b|, |b_a - sigma a_b|); NaN when not computed.
    pub orbital_swap: f64,
    pub orbitals_compared: usize,
}

pub fn deviation(a: &Digest, b: &Digest) -> Deviation {
    let index: HashMap<Key, usize> = b.levels.iter().enumerate().map(|(i, l)| (l.0, i)).collect();
    let mut out = Deviation {
        states_a: a.levels.len(),
        states_b: b.levels.len(),
        orbital_swap: f64::NAN,
        ..Deviation::default()
    };
    for (key, eps, f, w, mult) in &a.levels {
        if let Some(j) = index.get(&image_key(*key)) {
            let other = &b.levels[*j];
            out.matched += 1;
            out.max_eps = out.max_eps.max((eps - other.1).abs());
            out.max_f = out.max_f.max((f - other.2).abs());
            out.max_weight = out.max_weight.max((w - other.3).abs());
            if *mult != other.4 {
                out.mult_mismatch += 1;
            }
        }
    }
    let ma = spectrum_multiset(&a.levels);
    let mb = spectrum_multiset(&b.levels);
    out.multiset_a = ma.len();
    out.multiset_b = mb.len();
    out.sorted_eps = if ma.len() == mb.len() {
        ma.iter()
            .zip(&mb)
            .map(|(x, y)| (x - y).abs())
            .fold(0.0, f64::max)
    } else {
        f64::NAN
    };
    // both undefined (NaN): (NaN, NaN), counted as agreement; exactly one
    // undefined: (inf, 0), a failure; otherwise (|x - y|, |x|)
    let pair = |x: f64, y: f64| {
        if x.is_nan() && y.is_nan() {
            (f64::NAN, f64::NAN)
        } else if x.is_nan() || y.is_nan() {
            (f64::INFINITY, 0.0)
        } else {
            ((x - y).abs(), x.abs())
        }
    };
    for (name, x, y) in [
        ("E", a.energy, b.energy),
        ("F", a.free, b.free),
        ("mu", a.mu, b.mu),
        ("S_entropy", a.entropy, b.entropy),
        ("N_sumWeights", a.n_total, b.n_total),
        ("N_fromDensity", a.n_density, b.n_density),
        ("ksGap", a.gap, b.gap),
        ("deltaScf", a.delta_scf, b.delta_scf),
        ("E1", a.excited_energy, b.excited_energy),
    ] {
        let (d, s) = pair(x, y);
        out.scalars.push((name, d, s));
    }
    out.scalar_total_flip = (
        (a.scalar_total + b.scalar_total).abs(),
        a.scalar_total.abs(),
    );
    out.excitations = if a.excitations.len() == b.excitations.len() {
        a.excitations
            .iter()
            .zip(&b.excitations)
            .map(|(x, y)| (x - y).abs())
            .fold(0.0, f64::max)
    } else {
        f64::NAN
    };
    for (i, (name, sign, norm)) in PROFILE_NAMES.iter().enumerate() {
        let (raw_dev, raw_scale) = profile_deviation(&a.profiles[i], &b.profiles[i], *sign);
        let divided =
            |x: &[f64]| -> Vec<f64> { x.iter().zip(&a.factor).map(|(v, f)| v / f).collect() };
        let (d, s) = match norm {
            ProfileNorm::Density => (raw_dev, a.density_scale),
            ProfileNorm::ProperDensity => (
                profile_deviation(&divided(&a.profiles[i]), &divided(&b.profiles[i]), *sign).0,
                a.density_scale,
            ),
            ProfileNorm::ProperPotential => (
                profile_deviation(&divided(&a.profiles[i]), &divided(&b.profiles[i]), *sign).0,
                a.lambda.abs() / 16.0 * a.density_scale,
            ),
            ProfileNorm::Mass => (raw_dev, raw_scale),
            ProfileNorm::ProperEmt => {
                profile_deviation(&divided(&a.profiles[i]), &divided(&b.profiles[i]), *sign)
            }
        };
        out.profiles.push((name, *sign, d, s, raw_dev, raw_scale));
    }
    // averages: relative, or in energy units (deviation x proper volume <=
    // the energy tolerance: <rho> V_p = E, so the average of a cancelling
    // profile is held to the accuracy of the energy)
    for (i, (name, sign)) in AVERAGE_NAMES.iter().enumerate() {
        let x = a.averages[i];
        let y = b.averages[i];
        out.averages.push((
            name,
            *sign,
            (x - sign * y).abs(),
            x.abs().max(y.abs()),
            (x - sign * y).abs() * a.proper_volume,
        ));
    }
    out
}

/// Orbital swap check on two spectra with profiles (see
/// [`Deviation::orbital_swap`]): (max deviation, number of matched levels).
pub fn orbital_swap(a: &Spectrum, b: &Spectrum) -> (f64, usize) {
    let index: HashMap<Key, &State> = b.states.iter().map(|s| (s.key(), s)).collect();
    let mut worst: f64 = 0.0;
    let mut count = 0usize;
    for st in &a.states {
        if let Some(other) = index.get(&image_key(st.key())) {
            let mut best = f64::INFINITY;
            for sigma in [1.0, -1.0] {
                let mut dev: f64 = 0.0;
                for i in 0..st.level.a.len().min(other.level.a.len()) {
                    dev = dev
                        .max((st.level.a[i] - sigma * other.level.b[i]).abs())
                        .max((st.level.b[i] - sigma * other.level.a[i]).abs());
                }
                best = best.min(dev);
            }
            worst = worst.max(best);
            count += 1;
        }
    }
    (worst, count)
}

impl Deviation {
    /// The levels coincide (every level matched, multiplicities equal, eps,
    /// f and weights within the tolerances, and the multisets agree).
    pub fn levels_pass(&self, mass: f64) -> bool {
        self.matched > 0
            && self.matched == self.states_a
            && self.matched == self.states_b
            && self.mult_mismatch == 0
            && self.max_eps <= PAIRING_EPS_TOLERANCE * mass
            && self.max_f <= PAIRING_OCCUPATION_TOLERANCE
            && self.max_weight <= PAIRING_OCCUPATION_TOLERANCE
            && self.sorted_eps.is_finite()
            && self.sorted_eps <= PAIRING_EPS_TOLERANCE * mass
    }

    /// Scalar `name` within rtol |X| + atol |m| (NaN on both sides counts
    /// as equal: an undefined quantity is undefined in both universes).
    pub fn scalar_pass(&self, name: &str, mass: f64) -> bool {
        self.scalars
            .iter()
            .filter(|(n, _, _)| *n == name)
            .all(|(_, d, s)| {
                if d.is_nan() {
                    s.is_nan()
                } else {
                    *d <= PAIRING_ENERGY_RTOL * s + PAIRING_ENERGY_ATOL * mass
                }
            })
    }

    pub fn scalar(&self, name: &str) -> f64 {
        self.scalars
            .iter()
            .find(|(n, _, _)| *n == name)
            .map(|x| x.1)
            .unwrap_or(f64::NAN)
    }

    /// Every profile within PAIRING_PROFILE_RTOL in its norm (a vanishing
    /// norm requires a vanishing deviation).
    pub fn profiles_pass(&self) -> bool {
        self.profiles
            .iter()
            .all(|(_, _, d, s, _, _)| *d <= PAIRING_PROFILE_RTOL * s)
    }

    /// Every average within PAIRING_PROFILE_RTOL relative, or within the
    /// energy tolerance PAIRING_ENERGY_ATOL |m| after multiplication with the
    /// proper volume.
    pub fn averages_pass(&self, mass: f64) -> bool {
        self.averages.iter().all(|(_, _, d, s, integrated)| {
            *d <= PAIRING_PROFILE_RTOL * s || *integrated <= PAIRING_ENERGY_ATOL * mass
        })
    }

    pub fn profile(&self, name: &str) -> (f64, f64) {
        self.profiles
            .iter()
            .find(|p| p.0 == name)
            .map(|p| (p.2, p.3))
            .unwrap_or((f64::NAN, f64::NAN))
    }

    /// Worst profile deviation in its norm.
    pub fn worst_profile_relative(&self) -> f64 {
        self.profiles
            .iter()
            .map(|(_, _, d, s, _, _)| if *s > 0.0 { d / s } else { *d })
            .fold(0.0, f64::max)
    }

    pub fn to_json(&self) -> Json {
        let scalars: Vec<(&str, Json)> = self
            .scalars
            .iter()
            .map(|(n, d, s)| (*n, Json::floats(&[*d, *s])))
            .collect();
        let profiles: Vec<(&str, Json)> = self
            .profiles
            .iter()
            .map(|(n, sign, d, s, rd, rs)| (*n, Json::floats(&[*sign, *d, *s, *rd, *rs])))
            .collect();
        let averages: Vec<(&str, Json)> = self
            .averages
            .iter()
            .map(|(n, sign, d, s, v)| (*n, Json::floats(&[*sign, *d, *s, *v])))
            .collect();
        Json::object(vec![
            ("statesA", Json::Int(self.states_a as i64)),
            ("statesB", Json::Int(self.states_b as i64)),
            ("matchedByImageKey", Json::Int(self.matched as i64)),
            (
                "multiplicityMismatches",
                Json::Int(self.mult_mismatch as i64),
            ),
            ("maxAbsDeltaEps", Json::Float(self.max_eps)),
            ("maxAbsDeltaOccupation", Json::Float(self.max_f)),
            ("maxAbsDeltaWeight", Json::Float(self.max_weight)),
            ("multisetEntriesA", Json::Int(self.multiset_a as i64)),
            ("multisetEntriesB", Json::Int(self.multiset_b as i64)),
            ("sortedSpectrumMaxAbsDeltaEps", Json::Float(self.sorted_eps)),
            ("scalars_absDifference_absValueA", Json::object(scalars)),
            (
                "scalarTotalFlip_absSum_absValueA",
                Json::floats(&[self.scalar_total_flip.0, self.scalar_total_flip.1]),
            ),
            ("particleHoleMaxAbsDelta", Json::Float(self.excitations)),
            (
                "profileNorms",
                Json::str("n_c, S_c: max|X_plusM - sign X_minusM| in the SCF norm D = max(max|n_c|, max|S_c|); n_p, S_p: (X / e^{-6Hy}) in the norm D; v_x: (X / e^{-6Hy}) in the norm (|lambda|/16) D; M_eff: relative to max|M_eff|; rho, p_y, p_3, p_t: (X / e^{-6Hy}) relative to its maximum"),
            ),
            (
                "profiles_sign_deviation_norm_rawMaxAbsDeviation_rawScale",
                Json::object(profiles),
            ),
            (
                "averages_sign_absDeviation_scale_absDeviationTimesProperVolume",
                Json::object(averages),
            ),
            ("orbitalSwapMaxDeviation", Json::Float(self.orbital_swap)),
            ("orbitalsCompared", Json::Int(self.orbitals_compared as i64)),
        ])
    }
}

// ---------------------------------------------------------------------------
// committed Stage-4 numbers (read only)
// ---------------------------------------------------------------------------

/// Committed Stage-4 numbers of the runs that plusM of dirac16complex
/// repeats exactly: label -> (E, KS gap, Delta-SCF (NaN if not recorded), mu).
#[derive(Clone, Debug, Default)]
pub struct Stage4Numbers {
    pub runs: HashMap<String, (f64, f64, f64, f64)>,
    pub sources: Vec<(String, bool)>,
}

fn number(value: Option<&jsonread::Value>) -> f64 {
    value.and_then(|v| v.as_rational()).unwrap_or(f64::NAN)
}

/// Read the committed Stage-4 excited and scf summaries (the excited
/// record wins where both exist: it carries Delta-SCF).
pub fn load_stage4_numbers() -> Stage4Numbers {
    let mut out = Stage4Numbers::default();
    for (path, energy_key, has_delta) in [
        (STAGE4_SCF_SUMMARY, "energy", false),
        (STAGE4_EXCITED_SUMMARY, "E0", true),
    ] {
        let parsed = std::fs::read_to_string(path)
            .ok()
            .and_then(|text| jsonread::parse(&text).ok());
        out.sources.push((path.to_string(), parsed.is_some()));
        let Some(doc) = parsed else { continue };
        let Some(runs) = doc.get("runs").and_then(|r| r.as_array()) else {
            continue;
        };
        for run in runs {
            let Some(label) = run.get("label").and_then(|l| l.as_str()) else {
                continue;
            };
            let entry = (
                number(run.get(energy_key)),
                number(run.get("ksGap")),
                if has_delta {
                    number(run.get("deltaScf"))
                } else {
                    f64::NAN
                },
                number(run.get("mu")),
            );
            out.runs.insert(label.to_string(), entry);
        }
    }
    out
}

// ---------------------------------------------------------------------------
// one configuration
// ---------------------------------------------------------------------------

/// What one configuration contributes to the summary.
pub struct ConfigOutcome {
    pub config: Config,
    pub digests: Vec<Option<Digest>>,
    pub errors: Vec<Option<String>>,
    /// (first-update shift bound, |window floor|) per universe.
    pub gates: Vec<Option<(f64, f64)>>,
    pub pairing: Option<Deviation>,
    pub control: Option<Deviation>,
    pub record: Json,
    pub csv_row: Vec<f64>,
}

fn digest_json(d: &Digest) -> Json {
    Json::object(vec![
        ("converged", Json::Bool(d.converged)),
        ("iterations", Json::Int(d.iterations as i64)),
        (
            "zeroTemperatureFallbackStage",
            Json::Int(d.fallback_stage as i64),
        ),
        ("occupationSmearing", Json::Float(d.smearing)),
        ("states", Json::Int(d.levels.len() as i64)),
        ("E", Json::Float(d.energy)),
        ("F", Json::Float(d.free)),
        ("mu", Json::Float(d.mu)),
        ("S_entropy", Json::Float(d.entropy)),
        ("N_sumWeights", Json::Float(d.n_total)),
        ("N_fromDensity", Json::Float(d.n_density)),
        ("scalarTotal", Json::Float(d.scalar_total)),
        ("ksGap", Json::Float(d.gap)),
        ("deltaScf", Json::Float(d.delta_scf)),
        ("E1", Json::Float(d.excited_energy)),
        ("excitedConverged", Json::Bool(d.excited_converged)),
        ("particleHoleExcitations", Json::floats(&d.excitations)),
        ("rhoAvg", Json::Float(d.averages[0])),
        ("pYAvg", Json::Float(d.averages[1])),
        ("p3Avg", Json::Float(d.averages[2])),
        ("pTAvg", Json::Float(d.averages[3])),
        ("nPAvg", Json::Float(d.averages[4])),
        ("sPAvg", Json::Float(d.averages[5])),
        ("energyFromRho", Json::Float(d.energy_from_rho)),
        (
            "conservationResidualMax_normalised",
            Json::Float(d.conservation_max),
        ),
        ("maxLambdaSOverAbsM", Json::Float(d.max_lambda_s_over_m)),
        ("maxVxOverAbsM", Json::Float(d.max_v_x_over_m)),
        (
            "shiftBound_maxAbsMeffMinusM_plus_maxAbsVx",
            Json::Float(d.shift_bound),
        ),
        ("windowFloor", Json::Float(d.window_floor)),
        ("windowPremiseHolds", Json::Bool(d.window_premise())),
    ])
}

/// Pair totals (pairing-theory.json T3.pairTotalsKS) of plusM p and minusM q.
fn pair_totals_json(p: &Digest, q: &Digest) -> Json {
    let sums = |sign: f64| -> Json {
        let mut pairs: Vec<(&str, Json)> = vec![
            ("E", Json::Float(p.energy + sign * q.energy)),
            ("F", Json::Float(p.free + sign * q.free)),
            ("charge_N", Json::Float(p.n_total + sign * q.n_total)),
            (
                "scalarTotal",
                Json::Float(p.scalar_total + sign * q.scalar_total),
            ),
        ];
        for (i, (name, _)) in AVERAGE_NAMES.iter().enumerate() {
            pairs.push((name, Json::Float(p.averages[i] + sign * q.averages[i])));
        }
        Json::object(pairs)
    };
    Json::object(vec![
        (
            "mirrorPair",
            Json::object(vec![
                ("definition", Json::str("plusM + minusM: the ordinary -M universe (standard expectation rule, the same lambda) with the +M universe")),
                ("expected", Json::str("E = 2 E_+, F = 2 F_+, charge 2N, scalarTotal = 0, <rho>, <p_y>, <p_3>, <p_t>, <n_p> doubled, <S_p> = 0")),
                ("totals", sums(1.0)),
            ]),
        ),
        (
            "kreinImagePair",
            Json::object(vec![
                ("definition", Json::str("plusM - minusM for every one-body density and energy: the identity X + (-X) = 0 between the +M values and the (-m, -lambda) formulas evaluated on the same state (T1krein.consequence (a), STAGE5_SPEC erratum E5.1); not a cancellation between two universes (under its own anticommutator -B the gamma^8 image is the same quantum system as +M, with energy +H_+ and charge +Q_+)")),
                ("expected", Json::str("E = 0, F = 0, charge 0, <rho> = <p_y> = <p_3> = <p_t> = <n_p> = 0, scalarTotal = 2 S_+, <S_p> = 2 <S_p>_+")),
                ("totals", sums(-1.0)),
            ]),
        ),
    ])
}

/// Header of pairs-summary.csv.
pub fn summary_csv_header() -> Vec<String> {
    header(&[
        "exchange_sign",
        "abs_m",
        "L",
        "N",
        "lambda_hat",
        "T_over_abs_m",
        "E_plus",
        "E_minus",
        "E_control",
        "F_plus",
        "F_minus",
        "mu_plus",
        "mu_minus",
        "gap_plus",
        "gap_minus",
        "gap_control",
        "delta_scf_plus",
        "delta_scf_minus",
        "delta_scf_control",
        "scalar_total_plus",
        "scalar_total_minus",
        "rho_avg_plus",
        "rho_avg_minus",
        "max_lambda_S_over_m_plus",
        "dev_eps",
        "dev_sorted_eps",
        "dev_E",
        "dev_F",
        "dev_mu",
        "dev_gap",
        "dev_delta_scf",
        "dev_particle_hole",
        "dev_scalar_total_flip",
        "dev_profiles_worst_relative",
        "dev_orbital_swap",
        "mirror_E",
        "mirror_N",
        "mirror_scalar_total",
        "mirror_rho_avg",
        "krein_E",
        "krein_N",
        "krein_scalar_total",
        "krein_rho_avg",
        "krein_p_y_avg",
        "krein_p_3_avg",
        "krein_p_t_avg",
        "control_status",
        "control_dev_sorted_eps",
        "control_dE",
        "control_dgap",
        "plus_converged",
        "minus_converged",
        "iterations_plus",
        "iterations_minus",
    ])
}

/// Run the three universes of `cfg`, write their files and pairing.json,
/// record the checks.
pub fn run_configuration(
    ctx: &RunContext,
    dir: &Path,
    summary: &mut ExperimentSummary,
    cfg: &Config,
    stage4: &Stage4Numbers,
) -> Result<ConfigOutcome, String> {
    let label = cfg.label();
    let mass = cfg.mass;
    let mut data: Vec<Result<UniverseData, String>> = Vec::new();
    let mut gates: Vec<Result<(f64, f64), String>> = Vec::new();
    for universe in Universe::ALL {
        let params = cfg.params(ctx, universe);
        let start = std::time::Instant::now();
        let gate = first_update_shift(&params);
        let outcome = match (&gate, universe) {
            (Ok((shift, floor)), Universe::Control) if shift > floor => Err(format!(
                "not run: the first SCF update violates the window premise of the solver: shift bound max|M_eff - m| + max|v_x| = {shift} > |window floor| = {floor} (the untransformed tip bag puts the zero modes at the tip, where the proper-density factor is e^{{6HL}})"
            )),
            (Err(message), Universe::Control) => {
                Err(format!("not run: the first SCF update failed: {message}"))
            }
            _ => compute_universe(&params, universe.solver()),
        };
        gates.push(gate);
        // progress on stderr only (no file depends on it)
        match &outcome {
            Ok(d) => eprintln!(
                "[pairs] {label} {}: converged {} iterations {} E {} gap {} ({:.1} s)",
                universe.name(),
                d.ground.converged,
                d.ground.iterations,
                d.ground.energies.total,
                d.gap(),
                start.elapsed().as_secs_f64()
            ),
            Err(message) => eprintln!(
                "[pairs] {label} {}: error {message} ({:.1} s)",
                universe.name(),
                start.elapsed().as_secs_f64()
            ),
        }
        write_universe(dir, summary, cfg, universe, &params, &outcome)?;
        data.push(outcome);
    }
    // per-universe checks (plusM and minusM are required to be proper KS states)
    for (universe, outcome) in Universe::ALL.iter().zip(&data) {
        if *universe == Universe::Control {
            continue;
        }
        let tag = format!("{label}_{}", universe.name());
        let d = match outcome {
            Err(message) => {
                summary.check(&format!("{tag}_solved"), false, message);
                continue;
            }
            Ok(d) => d,
        };
        let g = &d.ground;
        summary.check(
            &format!("{tag}_converged"),
            g.converged,
            &format!(
                "{} iterations, fallback stage {}, smearing {}",
                g.iterations, g.params.fallback_stage, g.params.smearing
            ),
        );
        let n_density = particle_number_from_density(&g.params, &g.densities);
        summary.check(
            &format!("{tag}_particle_number"),
            (n_density - cfg.n).abs() <= 1e-6 * cfg.n
                && (g.energies.n_total - cfg.n).abs() <= 1e-8 * cfg.n,
            &format!(
                "N(density) = {n_density}, sum weights = {}",
                g.energies.n_total
            ),
        );
        let e = &d.emt;
        summary.check(
            &format!("{tag}_energy_from_rho"),
            (e.energy_from_rho - e.energy_total).abs() <= 1e-6 * e.energy_total.abs()
                || (e.energy_from_rho - e.energy_total).abs() < 1e-8,
            &format!("{} vs {}", e.energy_from_rho, e.energy_total),
        );
        summary.check(
            &format!("{tag}_emt_conservation"),
            e.conservation_max < 1e-3,
            &format!("normalised max residual {:e}", e.conservation_max),
        );
        let digest = Digest::of(d);
        summary.check(
            &format!("{tag}_window_premise"),
            digest.window_premise(),
            &format!(
                "shift bound max|M_eff - m| + max|v_x| = {} <= |window floor| = {} (every particle-branch level inside the window)",
                digest.shift_bound, -digest.window_floor
            ),
        );
        summary.check(
            &format!("{tag}_gap_positive"),
            d.gap() > 0.0,
            &format!("eps_LUMO - eps_HOMO = {}", d.gap()),
        );
        match &d.excited {
            None => {}
            Some(Err(message)) => {
                summary.check(&format!("{tag}_delta_scf_defined"), false, message);
            }
            Some(Ok(ex)) => {
                summary.check(
                    &format!("{tag}_delta_scf_converged"),
                    ex.converged,
                    &format!("{} iterations", ex.iterations),
                );
                summary.check(
                    &format!("{tag}_delta_scf_positive"),
                    d.delta_scf() > 0.0,
                    &format!("E1 - E0 = {}, KS gap = {}", d.delta_scf(), d.gap()),
                );
            }
        }
    }
    let digests: Vec<Option<Digest>> = data
        .iter()
        .map(|o| o.as_ref().ok().map(Digest::of))
        .collect();
    let errors: Vec<Option<String>> = data.iter().map(|o| o.as_ref().err().cloned()).collect();
    // Stage-4 reproduction (dirac16complex plusM at T = 0 is a Stage-4 run)
    let mut stage4_record = Json::str("not applicable (no committed Stage-4 run with these parameters, or non-canonical tolerances)");
    let canonical = !ctx.refined && ctx.rtol.is_none() && ctx.atol.is_none();
    if cfg.statistics == Statistics::Anticommuting && cfg.t_over_m == 0.0 && canonical {
        let stage4_label = format!(
            "m{}_L{}_N{}_{}_T0",
            trim_float(cfg.mass),
            trim_float(cfg.length),
            cfg.n as i64,
            cfg.lambda_name
        );
        if let (Some(expected), Some(Some(p))) = (stage4.runs.get(&stage4_label), digests.first()) {
            // bitwise after v + 0.0 (the writers print -0 as 0, output.rs)
            let same = |a: f64, b: f64| (a + 0.0).to_bits() == (b + 0.0).to_bits() || b.is_nan();
            let ok = expected.0.is_finite()
                && expected.3.is_finite()
                && same(p.energy, expected.0)
                && same(p.gap, expected.1)
                && same(p.delta_scf, expected.2)
                && same(p.mu, expected.3);
            summary.check(
                &format!("{label}_plusM_reproduces_stage4"),
                ok,
                &format!(
                    "Stage-4 run {stage4_label}: E {} vs {}, gap {} vs {}, Delta-SCF {} vs {} (NaN: not recorded there), mu {} vs {} (bitwise)",
                    p.energy, expected.0, p.gap, expected.1, p.delta_scf, expected.2, p.mu, expected.3
                ),
            );
            stage4_record = Json::object(vec![
                ("stage4Run", Json::str(&stage4_label)),
                ("bitwiseEqual", Json::Bool(ok)),
                (
                    "stage4_E_gap_deltaScf_mu",
                    Json::floats(&[expected.0, expected.1, expected.2, expected.3]),
                ),
            ]);
        }
    }
    // pairing plusM vs minusM
    let mut pairing: Option<Deviation> = None;
    if let (Some(Some(p)), Some(Some(q))) = (digests.first(), digests.get(1)) {
        let mut dev = deviation(p, q);
        if let (Ok(dp), Ok(dq)) = (&data[0], &data[1]) {
            let (worst, count) = orbital_swap(&dp.ground.spectrum, &dq.ground.spectrum);
            dev.orbital_swap = worst;
            dev.orbitals_compared = count;
        }
        let tag = format!("{label}_pairing");
        summary.check(
            &format!("{tag}_levels"),
            dev.levels_pass(mass),
            &format!(
                "{} / {} / {} levels (plusM / minusM / matched by (shell, -p, -s, -n)), multiplicity mismatches {}, max |d eps| = {:e}, max |d f| = {:e}, max |d w| = {:e}, sorted spectra ({} / {} entries) max |d eps| = {:e}",
                dev.states_a, dev.states_b, dev.matched, dev.mult_mismatch, dev.max_eps, dev.max_f, dev.max_weight, dev.multiset_a, dev.multiset_b, dev.sorted_eps
            ),
        );
        summary.check(
            &format!("{tag}_orbitals_swap"),
            dev.orbitals_compared == dev.matched
                && dev.orbitals_compared > 0
                && dev.orbital_swap <= PAIRING_ORBITAL_TOLERANCE,
            &format!(
                "(a, b)_plusM = +-(b, a)_minusM for {} matched levels: max deviation {:e}",
                dev.orbitals_compared, dev.orbital_swap
            ),
        );
        let energies_ok = ["E", "F", "mu", "S_entropy", "N_sumWeights", "N_fromDensity"]
            .iter()
            .all(|n| dev.scalar_pass(n, mass));
        summary.check(
            &format!("{tag}_mu_E_F_entropy_N"),
            energies_ok,
            &format!(
                "|dE| = {:e}, |dF| = {:e}, |d mu| = {:e}, |dS_ent| = {:e}, |dN| = {:e}, |dN(density)| = {:e} (E = {})",
                dev.scalar("E"), dev.scalar("F"), dev.scalar("mu"), dev.scalar("S_entropy"), dev.scalar("N_sumWeights"), dev.scalar("N_fromDensity"), p.energy
            ),
        );
        let excited_ok = dev.scalar_pass("ksGap", mass)
            && dev.scalar_pass("deltaScf", mass)
            && dev.scalar_pass("E1", mass)
            && dev.excitations.is_finite()
            && dev.excitations <= PAIRING_EPS_TOLERANCE * mass
            && p.excitations.len() == q.excitations.len();
        summary.check(
            &format!("{tag}_first_excited_state"),
            excited_ok,
            &format!(
                "|d gap| = {:e}, particle-hole list ({} / {}) max |d| = {:e}, |d Delta-SCF| = {:e}, |d E1| = {:e} (gap {}, Delta-SCF {})",
                dev.scalar("ksGap"), p.excitations.len(), q.excitations.len(), dev.excitations, dev.scalar("deltaScf"), dev.scalar("E1"), p.gap, p.delta_scf
            ),
        );
        let (flip, scale) = dev.scalar_total_flip;
        summary.check(
            &format!("{tag}_scalar_charge_flips"),
            flip <= PAIRING_ENERGY_RTOL * scale + PAIRING_ENERGY_ATOL * mass,
            &format!(
                "|S_total(plusM) + S_total(minusM)| = {flip:e} (S_total(plusM) = {})",
                p.scalar_total
            ),
        );
        let profile_detail: Vec<String> = dev
            .profiles
            .iter()
            .map(|(n, sign, d, s, _, _)| {
                format!(
                    "{n} ({}): {d:e} of {s:e}",
                    if *sign > 0.0 { "equal" } else { "opposite" }
                )
            })
            .collect();
        summary.check(
            &format!("{tag}_profiles"),
            dev.profiles_pass(),
            &format!(
                "max |X_plus - sign X_minus| on the grid: {}",
                profile_detail.join(", ")
            ),
        );
        let average_detail: Vec<String> = dev
            .averages
            .iter()
            .map(|(n, _, d, s, v)| format!("{n}: {d:e} of {s:e} (x V_p: {v:e})"))
            .collect();
        summary.check(
            &format!("{tag}_emt_averages"),
            dev.averages_pass(mass),
            &average_detail.join(", "),
        );
        // pair totals
        let s_avg_index = 5;
        let mirror_s = (p.scalar_total + q.scalar_total).abs();
        let mirror_s_avg = (p.averages[s_avg_index] + q.averages[s_avg_index]).abs();
        let mirror_ok = mirror_s
            <= PAIRING_ENERGY_RTOL * p.scalar_total.abs() + PAIRING_ENERGY_ATOL * mass
            && mirror_s_avg
                <= PAIRING_PROFILE_RTOL
                    * p.averages[s_avg_index]
                        .abs()
                        .max(q.averages[s_avg_index].abs())
            && (p.energy + q.energy - 2.0 * p.energy).abs()
                <= PAIRING_ENERGY_RTOL * p.energy.abs() + PAIRING_ENERGY_ATOL * mass
            && (p.n_total + q.n_total - 2.0 * cfg.n).abs() <= 1e-8 * cfg.n;
        summary.check(
            &format!("{label}_mirror_pair_totals"),
            mirror_ok,
            &format!(
                "plusM + minusM: E = {} (2 E_+ = {}), charge = {}, scalarTotal = {:e}, <S_p> = {:e}, <rho> = {}",
                p.energy + q.energy,
                2.0 * p.energy,
                p.n_total + q.n_total,
                p.scalar_total + q.scalar_total,
                p.averages[s_avg_index] + q.averages[s_avg_index],
                p.averages[0] + q.averages[0]
            ),
        );
        let krein_e = (p.energy - q.energy).abs();
        let krein_n = (p.n_total - q.n_total).abs();
        let krein_emt_ok = (0..4).all(|i| {
            (p.averages[i] - q.averages[i]).abs()
                <= PAIRING_PROFILE_RTOL * p.averages[i].abs().max(q.averages[i].abs())
        });
        let krein_s = (p.scalar_total - q.scalar_total - 2.0 * p.scalar_total).abs();
        let krein_ok = krein_e <= PAIRING_ENERGY_RTOL * p.energy.abs() + PAIRING_ENERGY_ATOL * mass
            && krein_n <= 1e-8 * cfg.n
            && krein_emt_ok
            && krein_s <= PAIRING_ENERGY_RTOL * p.scalar_total.abs() + PAIRING_ENERGY_ATOL * mass;
        summary.check(
            &format!("{label}_krein_image_pair_totals"),
            krein_ok,
            &format!(
                "plusM - minusM: E = {:e}, charge = {:e}, <rho> = {:e}, <p_y> = {:e}, <p_3> = {:e}, <p_t> = {:e}, scalarTotal = {} (2 S_+ = {})",
                p.energy - q.energy,
                p.n_total - q.n_total,
                p.averages[0] - q.averages[0],
                p.averages[1] - q.averages[1],
                p.averages[2] - q.averages[2],
                p.averages[3] - q.averages[3],
                p.scalar_total - q.scalar_total,
                2.0 * p.scalar_total
            ),
        );
        pairing = Some(dev);
    }
    // the control
    let mut control: Option<Deviation> = None;
    let mut control_status = 0.0;
    let mut control_note = String::new();
    match (digests.first(), digests.get(2), &errors[2]) {
        (Some(Some(p)), Some(Some(c)), _) => {
            let dev = deviation(p, c);
            control_status = if c.converged { 1.0 } else { -1.0 };
            let reference_dev = pairing.as_ref().map(|d| d.sorted_eps).unwrap_or(0.0);
            let threshold = (CONTROL_FACTOR * reference_dev.max(0.0)).max(CONTROL_MIN_DIFFERENCE);
            let spectrum_differs = dev.multiset_a != dev.multiset_b || dev.sorted_eps > threshold;
            let de = (p.energy - c.energy).abs();
            let dgap = (p.gap - c.gap).abs();
            let observable_differs = de > CONTROL_MIN_DIFFERENCE || dgap > CONTROL_MIN_DIFFERENCE;
            control_note = format!(
                "control converged {}; spectra: {} / {} entries, sorted max |d eps| = {:e} (threshold {threshold:e}); |dE| = {de:e}, |d gap| = {dgap:e} (gap plusM {}, control {})",
                c.converged, dev.multiset_a, dev.multiset_b, dev.sorted_eps, p.gap, c.gap
            );
            if c.converged {
                summary.check(
                    &format!("{label}_control_differs"),
                    spectrum_differs && observable_differs,
                    &control_note,
                );
            } else if cfg.lambda_hat == 0.0 {
                summary.check(&format!("{label}_control_converged"), false, &control_note);
            }
            control = Some(dev);
        }
        (_, _, Some(message)) => {
            control_status = if message.starts_with("not run") {
                -3.0
            } else {
                -2.0
            };
            control_note = format!("control not solved: {message}");
            if cfg.lambda_hat == 0.0 {
                summary.check(&format!("{label}_control_converged"), false, &control_note);
            }
        }
        _ => {}
    }
    // the first SCF updates of plusM and minusM pair as well
    if let (Ok((sp, _)), Ok((sm, _))) = (&gates[0], &gates[1]) {
        summary.check(
            &format!("{label}_first_update_shift_pairs"),
            (sp - sm).abs() <= PAIRING_PROFILE_RTOL * sp.abs().max(sm.abs())
                || (sp - sm).abs() <= PAIRING_ENERGY_ATOL * mass,
            &format!("shift bound of the first SCF update: plusM {sp}, minusM {sm}"),
        );
    }
    let gate_json: Vec<(&str, Json)> = Universe::ALL
        .iter()
        .zip(&gates)
        .map(|(u, g)| {
            (
                u.name(),
                match g {
                    Ok((shift, floor)) => Json::floats(&[*shift, *floor]),
                    Err(message) => Json::str(message),
                },
            )
        })
        .collect();
    // pairing.json
    let universes: Vec<(&str, Json)> = Universe::ALL
        .iter()
        .zip(digests.iter().zip(&errors))
        .map(|(u, (d, e))| {
            let value = match (d, e) {
                (Some(d), _) => digest_json(d),
                (None, Some(message)) => Json::object(vec![("error", Json::str(message))]),
                _ => Json::Null,
            };
            (u.name(), value)
        })
        .collect();
    let totals = match (digests.first(), digests.get(1)) {
        (Some(Some(p)), Some(Some(q))) => pair_totals_json(p, q),
        _ => Json::Null,
    };
    let record = Json::object(vec![
        ("configuration", cfg.to_json()),
        ("universes", Json::object(universes)),
        (
            "levelMap",
            Json::str("plusM (shell, parity p, block type s, Pruefer index n) -> minusM (shell, -p, -s, -n), same eps; orbital (a, b) -> +-(b, a)"),
        ),
        (
            "pairingDeviation_plusM_vs_minusM",
            pairing.as_ref().map(|d| d.to_json()).unwrap_or(Json::Null),
        ),
        ("pairTotals", totals),
        (
            "controlDeviation_plusM_vs_minusMControl",
            control.as_ref().map(|d| d.to_json()).unwrap_or(Json::Null),
        ),
        ("controlOutcome", Json::str(&control_note)),
        (
            "firstUpdateShiftBound_absWindowFloor",
            Json::object(gate_json),
        ),
        ("stage4Reproduction", stage4_record),
    ]);
    let rel = format!("{label}/pairing.json");
    write_json(&dir.join(&rel), &record)?;
    summary.add_file(&rel);
    let csv_row = csv_row(
        cfg,
        &digests,
        pairing.as_ref(),
        control.as_ref(),
        control_status,
    );
    Ok(ConfigOutcome {
        config: cfg.clone(),
        digests,
        errors,
        gates: gates.iter().map(|g| g.as_ref().ok().copied()).collect(),
        pairing,
        control,
        record,
        csv_row,
    })
}

fn csv_row(
    cfg: &Config,
    digests: &[Option<Digest>],
    pairing: Option<&Deviation>,
    control: Option<&Deviation>,
    control_status: f64,
) -> Vec<f64> {
    let nan = f64::NAN;
    let get = |i: usize, f: &dyn Fn(&Digest) -> f64| -> f64 {
        digests
            .get(i)
            .and_then(|d| d.as_ref())
            .map(f)
            .unwrap_or(nan)
    };
    let both = |f: &dyn Fn(&Digest, &Digest) -> f64| -> f64 {
        match (digests.first(), digests.get(1)) {
            (Some(Some(p)), Some(Some(q))) => f(p, q),
            _ => nan,
        }
    };
    let pd = |f: &dyn Fn(&Deviation) -> f64| -> f64 { pairing.map(f).unwrap_or(nan) };
    vec![
        cfg.statistics.sign(),
        cfg.mass,
        cfg.length,
        cfg.n,
        cfg.lambda_hat,
        cfg.t_over_m,
        get(0, &|d| d.energy),
        get(1, &|d| d.energy),
        get(2, &|d| d.energy),
        get(0, &|d| d.free),
        get(1, &|d| d.free),
        get(0, &|d| d.mu),
        get(1, &|d| d.mu),
        get(0, &|d| d.gap),
        get(1, &|d| d.gap),
        get(2, &|d| d.gap),
        get(0, &|d| d.delta_scf),
        get(1, &|d| d.delta_scf),
        get(2, &|d| d.delta_scf),
        get(0, &|d| d.scalar_total),
        get(1, &|d| d.scalar_total),
        get(0, &|d| d.averages[0]),
        get(1, &|d| d.averages[0]),
        get(0, &|d| d.max_lambda_s_over_m),
        pd(&|d| d.max_eps),
        pd(&|d| d.sorted_eps),
        pd(&|d| d.scalar("E")),
        pd(&|d| d.scalar("F")),
        pd(&|d| d.scalar("mu")),
        pd(&|d| d.scalar("ksGap")),
        pd(&|d| d.scalar("deltaScf")),
        pd(&|d| d.excitations),
        pd(&|d| d.scalar_total_flip.0),
        pd(&|d| d.worst_profile_relative()),
        pd(&|d| d.orbital_swap),
        both(&|p, q| p.energy + q.energy),
        both(&|p, q| p.n_total + q.n_total),
        both(&|p, q| p.scalar_total + q.scalar_total),
        both(&|p, q| p.averages[0] + q.averages[0]),
        both(&|p, q| p.energy - q.energy),
        both(&|p, q| p.n_total - q.n_total),
        both(&|p, q| p.scalar_total - q.scalar_total),
        both(&|p, q| p.averages[0] - q.averages[0]),
        both(&|p, q| p.averages[1] - q.averages[1]),
        both(&|p, q| p.averages[2] - q.averages[2]),
        both(&|p, q| p.averages[3] - q.averages[3]),
        control_status,
        control.map(|d| d.sorted_eps).unwrap_or(nan),
        match (digests.first(), digests.get(2)) {
            (Some(Some(p)), Some(Some(c))) => (p.energy - c.energy).abs(),
            _ => nan,
        },
        match (digests.first(), digests.get(2)) {
            (Some(Some(p)), Some(Some(c))) => (p.gap - c.gap).abs(),
            _ => nan,
        },
        get(0, &|d| if d.converged { 1.0 } else { 0.0 }),
        get(1, &|d| if d.converged { 1.0 } else { 0.0 }),
        get(0, &|d| d.iterations as f64),
        get(1, &|d| d.iterations as f64),
    ]
}

// ---------------------------------------------------------------------------
// the lambda-independent free section (exact statements)
// ---------------------------------------------------------------------------

/// Positive roots of g on (0, q_max] (uniform scan with `steps` intervals,
/// bisection of every sign change; the scan starts at 1e-9 q_max so that
/// the trivial root q = 0 is excluded).
pub fn positive_roots(g: &dyn Fn(f64) -> f64, q_max: f64, steps: usize) -> Vec<f64> {
    let h = q_max / steps as f64;
    let mut roots = Vec::new();
    let mut q0 = 1e-9 * q_max;
    let mut g0 = g(q0);
    for i in 1..=steps {
        let q1 = h * i as f64;
        let g1 = g(q1);
        if g0 == 0.0 {
            roots.push(q0);
        } else if g0 * g1 < 0.0 {
            let (mut a, mut b, mut ga) = (q0, q1, g0);
            for _ in 0..200 {
                let mid = 0.5 * (a + b);
                let gm = g(mid);
                if ga * gm <= 0.0 {
                    b = mid;
                } else {
                    a = mid;
                    ga = gm;
                }
            }
            roots.push(0.5 * (a + b));
        }
        q0 = q1;
        g0 = g1;
    }
    roots
}

/// The sub-gap bound state of the control's mixed sector (odd parity,
/// tip b(-L) = 0, mass -M): kappa in (0, M) with tanh(kappa L) = kappa/M;
/// exists iff M L > 1 (pairing-theory.json T3.untransformedBCControl).
pub fn control_bound_state_kappa(mass: f64, length: f64) -> Option<f64> {
    if mass * length <= 1.0 {
        return None;
    }
    let h = |kappa: f64| mass * tanh(kappa * length) - kappa;
    let (mut a, mut b) = (1e-12 * mass, mass);
    if h(a) * h(b) > 0.0 {
        return None;
    }
    for _ in 0..200 {
        let mid = 0.5 * (a + b);
        if h(a) * h(mid) <= 0.0 {
            b = mid;
        } else {
            a = mid;
        }
    }
    Some(0.5 * (a + b))
}

/// Analytic k = 0 levels (block type s = +1) of the three universes in the
/// window [-limit, limit], sorted.  `even`: parity sector with the
/// Stage-4-type quantisation (b(-L) = b(0) = 0 for plusM and the control,
/// a(-L) = a(0) = 0 for minusM): eps = 0 (the zero mode) and
/// +-sqrt(M^2 + (n pi/L)^2); the mixed sectors: M sin qL + q cos qL = 0
/// (plusM odd, minusM even) and q cos qL - M sin qL = 0 plus the bound
/// state (control odd).
pub fn analytic_k0_levels(
    universe: Universe,
    parity: i32,
    mass: f64,
    length: f64,
    limit: f64,
) -> Vec<f64> {
    let pure = matches!(
        (universe, parity),
        (Universe::Plus, 1) | (Universe::Minus, -1) | (Universe::Control, 1)
    );
    let q_max = (limit * limit - mass * mass).max(0.0).sqrt();
    let mut out: Vec<f64> = Vec::new();
    let push_pm = |e: f64, out: &mut Vec<f64>| {
        if e <= limit {
            out.push(e);
            out.push(-e);
        }
    };
    if pure {
        out.push(0.0);
        let mut n = 1;
        loop {
            let q = n as f64 * PI / length;
            if q > q_max {
                break;
            }
            push_pm((mass * mass + q * q).sqrt(), &mut out);
            n += 1;
        }
    } else if universe == Universe::Control {
        let g = |q: f64| q * cos(q * length) - mass * sin(q * length);
        for q in positive_roots(&g, q_max, 4000) {
            push_pm((mass * mass + q * q).sqrt(), &mut out);
        }
        if let Some(kappa) = control_bound_state_kappa(mass, length) {
            push_pm((mass * mass - kappa * kappa).sqrt(), &mut out);
        }
    } else {
        let g = |q: f64| mass * sin(q * length) + q * cos(q * length);
        for q in positive_roots(&g, q_max, 4000) {
            push_pm((mass * mass + q * q).sqrt(), &mut out);
        }
    }
    out.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
    out
}

/// First-order splitting constant of the brane zero-mode band of plusM and
/// minusM (eps = -+ c k): c = e^{-a4} (2M/(2M - H)) (1 - e^{-(2M-H)L}) /
/// (1 - e^{-2ML}) (Stage 4, E4.4; the same for the transformed -M universe).
pub fn splitting_paired(mass: f64, h: f64, length: f64, a4: f64) -> f64 {
    exp(-a4) * (2.0 * mass / (2.0 * mass - h)) * (1.0 - exp(-(2.0 * mass - h) * length))
        / (1.0 - exp(-2.0 * mass * length))
}

/// The control's constant (tip-localised zero mode (e^{-My}, 0)):
/// c_ctrl = e^{-a4} (2M/(2M + H)) (e^{(2M+H)L} - 1)/(e^{2ML} - 1).
pub fn splitting_control(mass: f64, h: f64, length: f64, a4: f64) -> f64 {
    exp(-a4) * (2.0 * mass / (2.0 * mass + h)) * (exp((2.0 * mass + h) * length) - 1.0)
        / (exp(2.0 * mass * length) - 1.0)
}

/// Where the k = 0 zero mode lives: (parity, expected (a, b) profile
/// shape, localisation exponent of |chi|^2 toward the brane).
fn zero_mode_expectation(universe: Universe) -> (i32, &'static str, f64) {
    match universe {
        Universe::Plus => (1, "(a, b) = (N e^{My}, 0), brane-localised", 1.0),
        Universe::Minus => (-1, "(a, b) = (0, +-N e^{My}), brane-localised", 1.0),
        Universe::Control => (1, "(a, b) = (+-N_c e^{-My}, 0), TIP-localised", -1.0),
    }
}

/// One block of the gamma^8 map: (from block, to block, alpha = (re, im)).
pub type BlockPhase = (usize, usize, (f64, f64));

/// The 16 x 16 block map of gamma^8 in this crate's block basis (blocks.rs):
/// V^dagger gamma^8 V maps block (s, c1, c2) onto (-s, c1, c2) with the 2x2
/// form alpha [[0, -1], [1, 0]], |alpha| = 1, i.e. with chi = (a, i b) the
/// swap (a, b) -> (b, a) up to the phase -i alpha.  Returns (defect, per
/// block (from, to, alpha)).
pub fn gamma8_block_map() -> (f64, Vec<BlockPhase>) {
    let reduction = blocks::derive();
    let v = reduction.basis;
    let g8 = C16::real(&crate::CHIRALITY);
    let y = v.dagger().mul(&g8).mul(&v);
    let mut defect: f64 = reduction.max_defect();
    let mut phases = Vec::new();
    let labels = reduction.labels;
    for (b, label) in labels.iter().enumerate() {
        let partner = labels
            .iter()
            .position(|l| l[0] == -label[0] && l[1] == label[1] && l[2] == label[2]);
        let Some(p) = partner else {
            return (f64::INFINITY, phases);
        };
        // alpha = Y[w_p, v_b]
        let alpha = (y.re[2 * p + 1][2 * b], y.im[2 * p + 1][2 * b]);
        let entry = |r: usize, c: usize| (y.re[r][c], y.im[r][c]);
        let abs = |z: (f64, f64)| (z.0 * z.0 + z.1 * z.1).sqrt();
        defect = defect.max((abs(alpha) - 1.0).abs());
        defect = defect.max(abs(entry(2 * p, 2 * b)));
        defect = defect.max(abs(entry(2 * p + 1, 2 * b + 1)));
        let upper = entry(2 * p, 2 * b + 1);
        defect = defect.max(abs((upper.0 + alpha.0, upper.1 + alpha.1)));
        // every other block of column pair b vanishes
        for r in 0..16 {
            if r / 2 != p {
                defect = defect
                    .max(abs(entry(r, 2 * b)))
                    .max(abs(entry(r, 2 * b + 1)));
            }
        }
        phases.push((b, p, alpha));
    }
    (defect, phases)
}

/// The two splitting constants and the exact-theory strings of
/// pairing-theory.json (when present): (sha256, c(M = 1), c_ctrl(M = 1),
/// statisticsFormulas, T3 checks passed / total).
pub struct TheoryExport {
    pub present: bool,
    pub sha256: String,
    pub c_values: Option<(f64, f64)>,
    pub statistics_formulas: String,
    pub t3_checks: (usize, usize),
    pub theorem_standard_rule: String,
}

fn count_true(value: Option<&jsonread::Value>) -> (usize, usize) {
    match value {
        Some(jsonread::Value::Object(pairs)) => (
            pairs
                .iter()
                .filter(|(_, v)| matches!(v, jsonread::Value::Bool(true)))
                .count(),
            pairs.len(),
        ),
        _ => (0, 0),
    }
}

pub fn read_theory_export(path: &str) -> TheoryExport {
    let mut out = TheoryExport {
        present: false,
        sha256: String::new(),
        c_values: None,
        statistics_formulas: String::new(),
        t3_checks: (0, 0),
        theorem_standard_rule: String::new(),
    };
    let Ok(bytes) = std::fs::read(path) else {
        return out;
    };
    out.sha256 = crate::theory::sha256_hex(&bytes);
    let Ok(text) = String::from_utf8(bytes) else {
        return out;
    };
    let Ok(doc) = jsonread::parse(&text) else {
        return out;
    };
    out.present = true;
    if let Some(values) = doc
        .path(&[
            "T3",
            "untransformedBCControl",
            "valuesM1H1L3a0_floatLabelled",
        ])
        .and_then(|v| v.as_str())
    {
        // "{1.905...`17., 13.42...`17.}" (Wolfram InputForm of two reals)
        let numbers: Vec<f64> = values
            .trim_matches(|c| c == '{' || c == '}')
            .split(',')
            .filter_map(|part| part.split('`').next())
            .filter_map(|x| x.trim().parse::<f64>().ok())
            .collect();
        if numbers.len() == 2 {
            out.c_values = Some((numbers[0], numbers[1]));
        }
    }
    if let Some(s) = doc
        .path(&["T3", "numericsPrescription", "statisticsFormulas"])
        .and_then(|v| v.as_str())
    {
        out.statistics_formulas = s.to_string();
    }
    if let Some(s) = doc
        .path(&["T3", "theoremStandardRule"])
        .and_then(|v| v.as_str())
    {
        out.theorem_standard_rule = s.to_string();
    }
    out.t3_checks = count_true(doc.path(&["T3", "checks"]));
    out
}

/// The free section: free spectra of the three universes, the key map, the
/// analytic k = 0 spectra, the zero modes, the splitting constants, the
/// gamma^8 block map and the exact-theory export.
pub fn free_section(
    ctx: &RunContext,
    dir: &Path,
    summary: &mut ExperimentSummary,
    theory_export: &TheoryExport,
) -> Result<Json, String> {
    let canonical = !ctx.refined && ctx.rtol.is_none() && ctx.atol.is_none();
    let mut records: Vec<Json> = Vec::new();
    let masses: Vec<f64> = vec![1.0, 3.0];
    let lengths: Vec<f64> = if ctx.quick {
        vec![3.0]
    } else {
        vec![2.0, 3.0, 4.0]
    };
    let mut map_worst: f64 = 0.0;
    let mut map_ok = true;
    let mut orbital_worst: f64 = 0.0;
    let mut analytic_worst: f64 = 0.0;
    let mut analytic_ok = true;
    let mut zero_worst: f64 = 0.0;
    let mut zero_ok = true;
    let mut stage4_same = true;
    let mut stage4_compared = 0usize;
    let mut control_differs = true;
    for mass in &masses {
        for length in &lengths {
            let mut spectra: Vec<Spectrum> = Vec::new();
            for universe in Universe::ALL {
                let mut p = params_for(ctx, universe.mass_sign() * mass, *length, 0.0, 0.0, 8.0);
                p.shell_cap = 16;
                p.tip_bag = universe.tip();
                let potential = scf::build_potential(&p, &Densities::zero(p.grid_n));
                let spectrum = compute_spectrum(
                    &p,
                    &potential,
                    Window {
                        eps_lo: -4.0 * mass,
                        eps_hi: 4.0 * mass,
                    },
                    &Default::default(),
                )?;
                summary.add_stats(spectrum.stats.steps, spectrum.stats.rhs_evals);
                let name = format!(
                    "free-spectrum-m{}-L{}-{}.csv",
                    trim_float(*mass),
                    trim_float(*length),
                    universe.name()
                );
                write_csv(&dir.join(&name), &levels_header(), &levels_rows(&spectrum))?;
                summary.add_file(&name);
                if universe == Universe::Plus && canonical {
                    // the plusM free spectrum is the Stage-4 free spectrum, byte for byte
                    let stage4 = format!(
                        "{STAGE4_SPECTRUM_DIR}/free-spectrum-m{}-L{}.csv",
                        trim_float(*mass),
                        trim_float(*length)
                    );
                    if let (Ok(a), Ok(b)) = (std::fs::read(dir.join(&name)), std::fs::read(&stage4))
                    {
                        stage4_compared += 1;
                        stage4_same &= a == b;
                    } else {
                        stage4_same = false;
                    }
                }
                spectra.push(spectrum);
            }
            // key map plusM -> minusM
            let index: HashMap<Key, &State> =
                spectra[1].states.iter().map(|s| (s.key(), s)).collect();
            let mut matched = 0usize;
            let mut worst: f64 = 0.0;
            for st in &spectra[0].states {
                if let Some(other) = index.get(&image_key(st.key())) {
                    matched += 1;
                    worst = worst.max((st.eps - other.eps).abs());
                    if st.mult != other.mult {
                        map_ok = false;
                    }
                }
            }
            let (orbital, compared) = orbital_swap(&spectra[0], &spectra[1]);
            map_ok &= matched == spectra[0].states.len()
                && matched == spectra[1].states.len()
                && worst <= PAIRING_EPS_TOLERANCE * mass
                && compared == matched
                && orbital <= PAIRING_ORBITAL_TOLERANCE;
            map_worst = map_worst.max(worst);
            orbital_worst = orbital_worst.max(orbital);
            // analytic k = 0 (s = +1) and the zero modes
            let mut universe_records: Vec<(&str, Json)> = Vec::new();
            for (u, spectrum) in Universe::ALL.iter().zip(&spectra) {
                let mut parity_records: Vec<(&str, Json)> = Vec::new();
                for parity in [1i32, -1] {
                    let mut numeric: Vec<f64> = spectrum
                        .states
                        .iter()
                        .filter(|s| s.n2 == 0 && s.s == 1 && s.parity == parity)
                        .map(|s| s.eps)
                        .collect();
                    numeric.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
                    let analytic = analytic_k0_levels(*u, parity, *mass, *length, 4.0 * mass);
                    let defect = if numeric.len() == analytic.len() {
                        numeric
                            .iter()
                            .zip(&analytic)
                            .map(|(a, b)| (a - b).abs())
                            .fold(0.0, f64::max)
                    } else {
                        f64::INFINITY
                    };
                    analytic_ok &= defect <= 1e-8 * mass;
                    analytic_worst = analytic_worst.max(defect);
                    parity_records.push((
                        if parity > 0 {
                            "parityPlus"
                        } else {
                            "parityMinus"
                        },
                        Json::object(vec![
                            ("numeric", Json::floats(&numeric)),
                            ("analytic", Json::floats(&analytic)),
                            ("maxAbsDefect", Json::Float(defect)),
                        ]),
                    ));
                }
                let (zp, shape, direction) = zero_mode_expectation(*u);
                let zero = spectrum
                    .states
                    .iter()
                    .find(|s| s.n2 == 0 && s.s == 1 && s.parity == zp && s.index == 0);
                let mut zero_record = Json::str("zero mode not found");
                match zero {
                    None => zero_ok = false,
                    Some(z) => {
                        let m_abs = *mass;
                        let norm2 = if direction > 0.0 {
                            2.0 * m_abs / (1.0 - exp(-2.0 * m_abs * length))
                        } else {
                            2.0 * m_abs / (exp(2.0 * m_abs * length) - 1.0)
                        };
                        let norm = norm2.sqrt();
                        let grid = crate::shooting::grid_points(*length, z.level.a.len());
                        let (big, small) = if *u == Universe::Minus {
                            (&z.level.b, &z.level.a)
                        } else {
                            (&z.level.a, &z.level.b)
                        };
                        let sign = if big[big.len() / 2] < 0.0 { -1.0 } else { 1.0 };
                        let mut dev: f64 = z.eps.abs();
                        for (i, y) in grid.iter().enumerate() {
                            let expected = norm * exp(direction * m_abs * y);
                            dev = dev
                                .max((sign * big[i] - expected).abs())
                                .max(small[i].abs());
                        }
                        let last = big.len() - 1;
                        let ratio = (big[last] * big[last] + small[last] * small[last])
                            / (big[0] * big[0] + small[0] * small[0]);
                        let expected_ratio = exp(direction * 2.0 * m_abs * length);
                        let ratio_defect = (ratio / expected_ratio - 1.0).abs();
                        zero_ok &= dev <= 1e-8 && ratio_defect <= 1e-7;
                        zero_worst = zero_worst.max(dev);
                        zero_record = Json::object(vec![
                            ("expected", Json::str(shape)),
                            ("parity", Json::Int(zp as i64)),
                            ("eps", Json::Float(z.eps)),
                            ("maxProfileDefect", Json::Float(dev)),
                            ("braneOverTipDensityRatio", Json::Float(ratio)),
                            ("expectedRatio_exp_pm_2ML", Json::Float(expected_ratio)),
                        ]);
                    }
                }
                universe_records.push((
                    u.name(),
                    Json::object(vec![
                        ("states", Json::Int(spectrum.states.len() as i64)),
                        ("k0Levels_s1", Json::object(parity_records)),
                        ("zeroMode", zero_record),
                    ]),
                ));
            }
            // the control's free spectrum differs from plusM
            let ma: Vec<f64> = spectrum_multiset(
                &spectra[0]
                    .states
                    .iter()
                    .map(|s| (s.key(), s.eps, 0.0, 0.0, s.mult))
                    .collect::<Vec<_>>(),
            );
            let mc: Vec<f64> = spectrum_multiset(
                &spectra[2]
                    .states
                    .iter()
                    .map(|s| (s.key(), s.eps, 0.0, 0.0, s.mult))
                    .collect::<Vec<_>>(),
            );
            let control_dev = if ma.len() == mc.len() {
                ma.iter()
                    .zip(&mc)
                    .map(|(a, b)| (a - b).abs())
                    .fold(0.0, f64::max)
            } else {
                f64::INFINITY
            };
            control_differs &= control_dev > CONTROL_MIN_DIFFERENCE;
            records.push(Json::object(vec![
                ("absM", Json::Float(*mass)),
                ("L", Json::Float(*length)),
                ("matchedByImageKey", Json::Int(matched as i64)),
                (
                    "statesPlusMinusControl",
                    Json::floats(&[
                        spectra[0].states.len() as f64,
                        spectra[1].states.len() as f64,
                        spectra[2].states.len() as f64,
                    ]),
                ),
                ("mapMaxAbsDeltaEps", Json::Float(worst)),
                ("orbitalSwapMaxDeviation", Json::Float(orbital)),
                (
                    "controlSortedSpectrumMaxAbsDeltaEps",
                    Json::Float(control_dev),
                ),
                ("universes", Json::object(universe_records)),
            ]));
        }
    }
    summary.check(
        "free_block_map_plusM_to_minusM",
        map_ok,
        &format!(
            "free spectra (|m| = 1, 3; L = {:?}; shells n2 <= 16; eps in [-4|m|, 4|m|]): every level of plusM (m, b(-L) = 0) is a level of minusM (-m, a(-L) = 0) with key (shell, -p, -s, -n): max |d eps| = {map_worst:e}, orbital swap max deviation {orbital_worst:e}",
            lengths
        ),
    );
    summary.check(
        "free_box_spectra_analytic_k0",
        analytic_ok,
        &format!("k = 0, s = +1, both parities, three universes (incl. the control's q cos qL - M sin qL = 0 levels and its bound state tanh(kappa L) = kappa/M): max |eps - analytic| = {analytic_worst:e}"),
    );
    summary.check(
        "free_zero_modes_and_localisation",
        zero_ok,
        &format!("plusM (N e^{{My}}, 0), minusM (0, N e^{{My}}), control (N_c e^{{-My}}, 0) and the brane/tip density ratios e^{{+-2ML}}: max profile defect {zero_worst:e}"),
    );
    summary.check(
        "free_control_spectrum_differs",
        control_differs,
        "the free spectrum of minusM_control (-m, b(-L) = 0) differs from plusM for every (|m|, L)",
    );
    if canonical {
        summary.check(
            "free_plusM_spectra_equal_stage4_bytes",
            stage4_same && stage4_compared == masses.len() * lengths.len(),
            &format!("{stage4_compared} plusM free spectra compared byte for byte with {STAGE4_SPECTRUM_DIR}/free-spectrum-m*-L*.csv"),
        );
    }
    // first-order splitting constants of the zero-mode band
    let mut splitting_records: Vec<Json> = Vec::new();
    let mut splitting_ok = true;
    let mut splitting_worst: f64 = 0.0;
    for mass in &masses {
        for length in &lengths {
            let paired = splitting_paired(*mass, 1.0, *length, 0.0);
            let ctrl = splitting_control(*mass, 1.0, *length, 0.0);
            let mut measured: Vec<(&str, Json)> = Vec::new();
            for universe in Universe::ALL {
                let potential = Arc::new(
                    Potential::free(1.0, 0.0, *length, universe.mass_sign() * mass, 301)
                        .with_tip(universe.tip()),
                );
                let mut shooter = Shooter::new(potential, tolerances_of(ctx));
                let (zp, _, _) = zero_mode_expectation(universe);
                let levels = shooter.levels(SPLITTING_K, zp, -0.25 * mass, 0.25 * mass, &[])?;
                summary.add_stats(shooter.stats.steps, shooter.stats.rhs_evals);
                let slope = levels
                    .iter()
                    .find(|l| l.index == 0)
                    .map(|l| l.pressure_charge / SPLITTING_K)
                    .unwrap_or(f64::NAN);
                let expected = match universe {
                    Universe::Plus => -paired,
                    Universe::Minus => paired,
                    Universe::Control => -ctrl,
                };
                let defect = ((slope - expected) / expected).abs();
                splitting_ok &= defect <= 1e-6;
                splitting_worst = splitting_worst.max(defect);
                measured.push((universe.name(), Json::floats(&[slope, expected, defect])));
            }
            splitting_records.push(Json::object(vec![
                ("absM", Json::Float(*mass)),
                ("L", Json::Float(*length)),
                ("cPaired", Json::Float(paired)),
                ("cControl", Json::Float(ctrl)),
                ("slope_expected_relativeDefect", Json::object(measured)),
            ]));
        }
    }
    summary.check(
        "free_zero_mode_splitting_closed_forms",
        splitting_ok,
        &format!("d eps/dk of the s = +1 zero-mode band at k = {SPLITTING_K:e} (Hellmann-Feynman): plusM -c(M), minusM +c(M), control -c_ctrl(M); max relative defect {splitting_worst:e}"),
    );
    // exact-theory export
    let theory_c = theory_export.c_values;
    if theory_export.present {
        let ok = match theory_c {
            Some((c, cc)) => {
                ((c - splitting_paired(1.0, 1.0, 3.0, 0.0)) / c).abs() <= 1e-12
                    && ((cc - splitting_control(1.0, 1.0, 3.0, 0.0)) / cc).abs() <= 1e-12
            }
            None => false,
        };
        summary.check(
            "theory_splitting_values_agree",
            ok,
            &format!(
                "pairing-theory.json T3.untransformedBCControl.valuesM1H1L3a0 = {:?} vs this crate's closed forms c = {}, c_ctrl = {} (M = H = 1, L = 3)",
                theory_c,
                splitting_paired(1.0, 1.0, 3.0, 0.0),
                splitting_control(1.0, 1.0, 3.0, 0.0)
            ),
        );
        let formulas = &theory_export.statistics_formulas;
        let needed = [
            "e_x = -(lambda/32)(n^2 + S^2)",
            "M_eff = m + (15/16) lambda S_p",
            "v_x = -(lambda/16) n_p",
            "e_x = +(lambda/32)(n^2 + S^2)",
            "M_eff = m + (17/16) lambda S_p",
            "v_x = +(lambda/16) n_p",
        ];
        summary.check(
            "theory_statistics_formulas_used",
            needed.iter().all(|n| formulas.contains(n))
                && Statistics::Anticommuting.mass_coefficient() == 15.0 / 16.0
                && Statistics::Commuting.mass_coefficient() == 17.0 / 16.0,
            &format!("pairing-theory.json T3.numericsPrescription.statisticsFormulas: {formulas}"),
        );
        summary.check(
            "theory_t3_checks_true",
            theory_export.t3_checks.1 > 0 && theory_export.t3_checks.0 == theory_export.t3_checks.1,
            &format!(
                "{} of {} T3 checks of the exact theory are true",
                theory_export.t3_checks.0, theory_export.t3_checks.1
            ),
        );
    }
    // gamma^8 block map (16 x 16, this crate's basis)
    let (defect, phases) = gamma8_block_map();
    summary.check(
        "gamma8_block_map_sigma2_between_partner_blocks",
        defect < 1e-14 && phases.len() == 8,
        &format!("V^dagger gamma^8 V maps block (s, c1, c2) onto (-s, c1, c2) as alpha [[0, -1], [1, 0]] (chi = (a, i b) -> -i alpha (b, i a)); defect {defect:e}"),
    );
    let phase_json: Vec<Json> = phases
        .iter()
        .map(|(b, p, alpha)| {
            Json::object(vec![
                ("fromBlock", Json::Int(*b as i64)),
                ("toBlock", Json::Int(*p as i64)),
                ("alpha_re_im", Json::floats(&[alpha.0, alpha.1])),
            ])
        })
        .collect();
    let doc = Json::object(vec![
        ("description", Json::str("lambda-independent exact statements checked numerically: free spectra of plusM (m, b(-L) = 0), minusM (-m, a(-L) = 0) and minusM_control (-m, b(-L) = 0); the key map (shell, p, s, n) -> (shell, -p, -s, -n) with the orbital swap; the analytic k = 0 spectra; the zero modes; the splitting constants; the gamma^8 block map")),
        ("spectra", Json::Array(records)),
        ("splitting", Json::Array(splitting_records)),
        ("gamma8BlockMap", Json::object(vec![
            ("defect", Json::Float(defect)),
            ("blocks", Json::Array(phase_json)),
        ])),
    ]);
    write_json(&dir.join("free-section.json"), &doc)?;
    summary.add_file("free-section.json");
    Ok(Json::object(vec![
        ("file", Json::str("free-section.json")),
        ("mapMaxAbsDeltaEps", Json::Float(map_worst)),
        ("orbitalSwapMaxDeviation", Json::Float(orbital_worst)),
        ("analyticK0MaxDefect", Json::Float(analytic_worst)),
        ("zeroModeMaxProfileDefect", Json::Float(zero_worst)),
        ("splittingMaxRelativeDefect", Json::Float(splitting_worst)),
        ("gamma8BlockMapDefect", Json::Float(defect)),
    ]))
}

// ---------------------------------------------------------------------------
// the subcommand
// ---------------------------------------------------------------------------

/// Couplings of the committed Stage-4 scf summary: (m, L, N, lambda_hat_1,
/// lambda_hat_2).
pub fn load_stage4_couplings() -> Vec<(f64, f64, f64, f64, f64)> {
    let Some(doc) = std::fs::read_to_string(STAGE4_SCF_SUMMARY)
        .ok()
        .and_then(|text| jsonread::parse(&text).ok())
    else {
        return Vec::new();
    };
    let Some(list) = doc
        .path(&["reference", "couplings"])
        .and_then(|v| v.as_array())
    else {
        return Vec::new();
    };
    list.iter()
        .map(|c| {
            (
                number(c.get("m")),
                number(c.get("L")),
                number(c.get("N")),
                number(c.get("lambdaHat1")),
                number(c.get("lambdaHat2")),
            )
        })
        .collect()
}

/// The configurations of the pairs matrix, in run order.  Canonical: both
/// statistics x |m| in {1, 3} x N in {8, N_mid(|m|)} (the Stage-4 closed
/// shells; N_mid(1) and N_mid(3) from the Stage-4 reference) x lambda_hat
/// in {0, +-lambda_hat_1, +-lambda_hat_2} of (|m|, L = 3, N) at T = 0, and
/// the same at T/|m| = 0.1 for N = N_mid(|m|).  `--quick`: |m| = 1, N = 8,
/// lambda_hat in {0, +-lambda_hat_1}, T = 0 and T/|m| = 0.1.
pub fn matrix(ctx: &RunContext, reference: &Reference) -> Result<Vec<Config>, String> {
    let masses: Vec<f64> = if ctx.quick { vec![1.0] } else { vec![1.0, 3.0] };
    let mut out = Vec::new();
    for statistics in Statistics::ALL {
        for mass in &masses {
            let n_mid = if *mass == 1.0 {
                reference.n_mid
            } else {
                reference.n_mid_m3
            };
            let ns: Vec<f64> = if ctx.quick {
                vec![8.0]
            } else {
                vec![8.0, n_mid]
            };
            let thermal_n = if ctx.quick { 8.0 } else { n_mid };
            for n in ns {
                let c = reference.coupling(*mass, PAIRS_LENGTH, n)?;
                let mut lambdas = lambda_set(&c, false);
                if ctx.quick {
                    lambdas.truncate(3);
                }
                for (lambda_name, lambda_hat) in lambdas {
                    let temperatures: Vec<f64> = if n == thermal_n {
                        vec![0.0, THERMAL_T_OVER_M]
                    } else {
                        vec![0.0]
                    };
                    for t_over_m in temperatures {
                        out.push(Config {
                            statistics,
                            mass: *mass,
                            length: PAIRS_LENGTH,
                            n,
                            lambda_name: lambda_name.clone(),
                            lambda_hat,
                            t_over_m,
                        });
                    }
                }
            }
        }
    }
    Ok(out)
}

/// The KS potentials of a digest are the formulas of its statistics applied
/// to the input densities of the last SCF iteration: M_eff = m + (1 +
/// sg/16) lambda S_p^in and v_x = sg (lambda/16) n_p^in, while the profiles
/// hold the OUTPUT densities of that iteration, which differ from the input
/// by at most the recorded residuals times the norm D (scf.rs).  Hence node
/// by node, exactly up to rounding,
///
/// ```text
/// |M_eff - m - (1 + sg/16) lambda S_p| <= (1 + sg/16) |lambda| e^{-6Hy} r_S D,
/// |v_x - sg (lambda/16) n_p|            <= (|lambda|/16) e^{-6Hy} r_n D.
/// ```
///
/// Returns (ok, worst ratio defect/bound for M_eff, for v_x); a ratio <= 1
/// means the bound holds (a rounding allowance of 1e-13 |m| and 1e-13 max|v_x|
/// is added to the bounds).
pub fn potentials_follow_formulas(
    d: &Digest,
    cfg: &Config,
    universe: Universe,
) -> (bool, f64, f64) {
    let m = universe.mass_sign() * cfg.mass;
    let lambda = d.lambda;
    let n_p = &d.profiles[1];
    let v_x = &d.profiles[2];
    let s_p = &d.profiles[8];
    let m_eff = &d.profiles[9];
    let coefficient = cfg.statistics.mass_coefficient();
    let sg = cfg.statistics.sign();
    let v_scale = v_x.iter().map(|v| v.abs()).fold(0.0, f64::max);
    let mut ratio_m: f64 = 0.0;
    let mut ratio_v: f64 = 0.0;
    for i in 0..n_p.len() {
        let f = d.factor[i];
        let bound_m = coefficient * lambda.abs() * f * d.final_residual_s * d.density_scale
            + 1e-13 * cfg.mass;
        let bound_v =
            lambda.abs() / 16.0 * f * d.final_residual_n * d.density_scale + 1e-13 * v_scale;
        let dm = (m_eff[i] - (m + coefficient * lambda * s_p[i])).abs();
        let dv = (v_x[i] - sg * lambda * n_p[i] / 16.0).abs();
        ratio_m = ratio_m.max(if bound_m > 0.0 { dm / bound_m } else { dm });
        ratio_v = ratio_v.max(if bound_v > 0.0 { dv / bound_v } else { dv });
    }
    (ratio_m <= 1.0 && ratio_v <= 1.0, ratio_m, ratio_v)
}

pub fn run_pairs(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let dir = ctx.experiment_dir("pairs")?;
    let mut summary = ExperimentSummary::new("pairs");
    let canonical = !ctx.refined && ctx.rtol.is_none() && ctx.atol.is_none();
    let theory_export = read_theory_export(PAIRING_THEORY_PATH);
    let stage4 = load_stage4_numbers();
    let reference = reference(ctx)?;
    let free = free_section(ctx, &dir, &mut summary, &theory_export)?;
    let configs = matrix(ctx, &reference)?;
    // the couplings are the Stage-4 ones (canonical tolerances: bit for bit)
    if canonical {
        let committed = load_stage4_couplings();
        let mut compared = 0usize;
        let mut same = true;
        for c in reference.couplings.borrow().iter() {
            if let Some(k) = committed
                .iter()
                .find(|k| k.0 == c.m && k.1 == c.length && k.2 == c.n)
            {
                compared += 1;
                same &= k.3.to_bits() == c.lambda_hat_1.to_bits()
                    && k.4.to_bits() == c.lambda_hat_2.to_bits();
            } else {
                same = false;
            }
        }
        summary.check(
            "couplings_equal_stage4",
            same && compared > 0,
            &format!("{compared} (|m|, L, N) couplings compared bit for bit with {STAGE4_SCF_SUMMARY} reference.couplings"),
        );
    }
    let mut outcomes: Vec<ConfigOutcome> = Vec::new();
    let mut table: Vec<Vec<f64>> = Vec::new();
    for cfg in &configs {
        let outcome = run_configuration(ctx, &dir, &mut summary, cfg, &stage4)?;
        // the KS potentials follow the formulas of the statistics
        for (i, universe) in [Universe::Plus, Universe::Minus].iter().enumerate() {
            if let Some(Some(d)) = outcome.digests.get(i) {
                let (ok, rel_m, rel_v) = potentials_follow_formulas(d, cfg, *universe);
                summary.check(
                    &format!("{}_{}_potentials_follow_statistics", cfg.label(), universe.name()),
                    ok,
                    &format!(
                        "M_eff = m + {} lambda S_p and v_x = {} (lambda/16) n_p on the grid, within the SCF residual bound of the last iteration: worst defect/bound {rel_m:e} (M_eff), {rel_v:e} (v_x)",
                        cfg.statistics.mass_coefficient(),
                        if cfg.statistics.sign() > 0.0 { "+" } else { "-" }
                    ),
                );
            }
        }
        table.push(outcome.csv_row.clone());
        outcomes.push(outcome);
    }
    // opposite coupling: plusM(lambda) vs minusM(-lambda) must NOT pair
    let find = |label: &str| outcomes.iter().find(|o| o.config.label() == label);
    let mut opposite: Vec<Json> = Vec::new();
    for o in &outcomes {
        let partner_name = match o.config.lambda_name.as_str() {
            "lamp1" => "lamm1",
            "lamm1" => "lamp1",
            "lamp2" => "lamm2",
            "lamm2" => "lamp2",
            _ => continue,
        };
        let partner_label = o.config.label_with(partner_name);
        let Some(partner) = find(&partner_label) else {
            continue;
        };
        let (Some(Some(p)), Some(Some(q))) = (o.digests.first(), partner.digests.get(1)) else {
            continue;
        };
        let dev = deviation(p, q);
        let reference_eps = o
            .pairing
            .as_ref()
            .map(|d| d.max_eps)
            .unwrap_or(0.0)
            .max(partner.pairing.as_ref().map(|d| d.max_eps).unwrap_or(0.0));
        let reference_e = o
            .pairing
            .as_ref()
            .map(|d| d.scalar("E"))
            .unwrap_or(0.0)
            .max(
                partner
                    .pairing
                    .as_ref()
                    .map(|d| d.scalar("E"))
                    .unwrap_or(0.0),
            );
        let de = (p.energy - q.energy).abs();
        let eps_threshold = (CONTROL_FACTOR * reference_eps).max(CONTROL_MIN_DIFFERENCE);
        let e_threshold = (CONTROL_FACTOR * reference_e).max(CONTROL_MIN_DIFFERENCE);
        let differs =
            dev.max_eps > eps_threshold || dev.matched != dev.states_a || de > e_threshold;
        summary.check(
            &format!("{}_opposite_coupling_does_not_map", o.config.label()),
            differs,
            &format!(
                "plusM({}) vs minusM({}) by the key map: {} of {} levels matched, max |d eps| = {:e} (pairing deviation {reference_eps:e}), |dE| = {de:e} (pairing deviation {reference_e:e})",
                o.config.lambda_name, partner_name, dev.matched, dev.states_a, dev.max_eps
            ),
        );
        opposite.push(Json::object(vec![
            ("plusM", Json::str(&o.config.label())),
            ("minusM", Json::str(&partner_label)),
            ("matchedByImageKey", Json::Int(dev.matched as i64)),
            ("statesPlusM", Json::Int(dev.states_a as i64)),
            ("maxAbsDeltaEps", Json::Float(dev.max_eps)),
            ("absDeltaE", Json::Float(de)),
            ("E_plusM_lambda", Json::Float(p.energy)),
            ("E_minusM_minusLambda", Json::Float(q.energy)),
            ("pairingDeviationEps", Json::Float(reference_eps)),
            ("pairingDeviationE", Json::Float(reference_e)),
            ("differs", Json::Bool(differs)),
        ]));
    }
    // the two statistics: identical at lambda = 0, different at lambda != 0
    let mut statistics_records: Vec<Json> = Vec::new();
    for o in outcomes
        .iter()
        .filter(|o| o.config.statistics == Statistics::Commuting)
    {
        let mut other_cfg = o.config.clone();
        other_cfg.statistics = Statistics::Anticommuting;
        let Some(other) = find(&other_cfg.label()) else {
            continue;
        };
        let label = o.config.label();
        if o.config.lambda_hat == 0.0 {
            let identical = Universe::ALL.iter().enumerate().all(|(i, _)| {
                match (o.digests.get(i), other.digests.get(i)) {
                    (Some(Some(a)), Some(Some(b))) => a.bitwise_equal(b),
                    (Some(None), Some(None)) => true,
                    _ => false,
                }
            });
            summary.check(
                &format!("{label}_lambda0_statistics_identical"),
                identical,
                &format!("lambda = 0: {label} and {} are the same problem (every number of the three universes bit for bit)", other_cfg.label()),
            );
            statistics_records.push(Json::object(vec![
                ("commuting", Json::str(&label)),
                ("anticommuting", Json::str(&other_cfg.label())),
                ("bitwiseIdentical", Json::Bool(identical)),
            ]));
        } else if let (Some(Some(a)), Some(Some(b))) = (o.digests.first(), other.digests.first()) {
            let de = a.energy - b.energy;
            let dv = profile_deviation(&a.profiles[2], &b.profiles[2], -1.0);
            summary.check(
                &format!("{label}_statistics_change_the_state"),
                de.abs() > 1e-10 * o.config.mass,
                &format!(
                    "plusM: E(dirac16complex00) - E(dirac16complex) = {de:e}; v_x(00) vs -v_x: max |v_00 + v| = {:e} of {:e} (the exchange sign)",
                    dv.0, dv.1
                ),
            );
            statistics_records.push(Json::object(vec![
                ("commuting", Json::str(&label)),
                ("anticommuting", Json::str(&other_cfg.label())),
                ("E_plusM_commuting", Json::Float(a.energy)),
                ("E_plusM_anticommuting", Json::Float(b.energy)),
                ("deltaE", Json::Float(de)),
                ("gap_plusM_commuting", Json::Float(a.gap)),
                ("gap_plusM_anticommuting", Json::Float(b.gap)),
            ]));
        }
    }
    write_csv(
        &dir.join("pairs-summary.csv"),
        &summary_csv_header(),
        &table,
    )?;
    summary.add_file("pairs-summary.csv");
    let control_outcomes: Vec<Json> = outcomes
        .iter()
        .map(|o| {
            let status = match (o.digests.get(2), o.errors.get(2)) {
                (Some(Some(d)), _) if d.converged => "converged",
                (Some(Some(_)), _) => "not converged",
                (_, Some(Some(e))) if e.starts_with("not run") => {
                    "not run (first SCF update outside the window premise)"
                }
                (_, Some(Some(_))) => "not solved (error)",
                _ => "absent",
            };
            let gate = match o.gates.get(2) {
                Some(Some((shift, floor))) => Json::floats(&[*shift, *floor]),
                _ => Json::Null,
            };
            let premise = o
                .digests
                .get(2)
                .and_then(|d| d.as_ref())
                .map(|d| Json::Bool(d.window_premise()))
                .unwrap_or(Json::Null);
            let shift = o
                .digests
                .get(2)
                .and_then(|d| d.as_ref())
                .map(|d| Json::Float(d.shift_bound))
                .unwrap_or(Json::Null);
            Json::object(vec![
                ("label", Json::str(&o.config.label())),
                ("status", Json::str(status)),
                ("windowPremiseHolds", premise),
                ("shiftBound", shift),
                ("firstUpdateShiftBound_absWindowFloor", gate),
                (
                    "error",
                    o.errors
                        .get(2)
                        .and_then(|e| e.as_ref())
                        .map(|e| Json::str(e))
                        .unwrap_or(Json::Null),
                ),
            ])
        })
        .collect();
    let configurations: Vec<Json> = outcomes
        .iter()
        .map(|o| {
            let pairing = o.pairing.as_ref();
            Json::object(vec![
                ("label", Json::str(&o.config.label())),
                (
                    "file",
                    Json::str(&format!("{}/pairing.json", o.config.label())),
                ),
                (
                    "pairingMaxAbsDeltaEps",
                    Json::Float(pairing.map(|d| d.max_eps).unwrap_or(f64::NAN)),
                ),
                (
                    "pairingAbsDeltaE",
                    Json::Float(pairing.map(|d| d.scalar("E")).unwrap_or(f64::NAN)),
                ),
                (
                    "pairingWorstProfileRelative",
                    Json::Float(
                        pairing
                            .map(|d| d.worst_profile_relative())
                            .unwrap_or(f64::NAN),
                    ),
                ),
                (
                    "pairTotals",
                    object_field(&o.record, "pairTotals").unwrap_or(Json::Null),
                ),
            ])
        })
        .collect();
    // the worst pairing deviations over the matrix (headline numbers)
    let mut paired = 0usize;
    let mut worst_eps: f64 = 0.0;
    let mut worst_e_relative: f64 = 0.0;
    let mut worst_gap: f64 = 0.0;
    let mut worst_delta_scf: f64 = 0.0;
    let mut worst_profile: f64 = 0.0;
    let mut worst_orbital: f64 = 0.0;
    let mut worst_scalar_flip_relative: f64 = 0.0;
    for o in &outcomes {
        if let (Some(d), Some(Some(p))) = (&o.pairing, o.digests.first()) {
            paired += 1;
            worst_eps = worst_eps.max(d.max_eps / o.config.mass);
            let e = d.scalar("E");
            worst_e_relative = worst_e_relative.max(if p.energy != 0.0 {
                e / p.energy.abs()
            } else {
                e
            });
            let g = d.scalar("ksGap");
            if g.is_finite() {
                worst_gap = worst_gap.max(g / o.config.mass);
            }
            let x = d.scalar("deltaScf");
            if x.is_finite() {
                worst_delta_scf = worst_delta_scf.max(x / o.config.mass);
            }
            worst_profile = worst_profile.max(d.worst_profile_relative());
            if d.orbital_swap.is_finite() {
                worst_orbital = worst_orbital.max(d.orbital_swap);
            }
            let (flip, scale) = d.scalar_total_flip;
            worst_scalar_flip_relative =
                worst_scalar_flip_relative.max(if scale > 0.0 { flip / scale } else { flip });
        }
    }
    summary.check(
        "every_configuration_paired",
        paired == outcomes.len() && !outcomes.is_empty(),
        &format!(
            "{paired} of {} configurations have both plusM and minusM solved (their pairing checks are listed per configuration)",
            outcomes.len()
        ),
    );
    let pairing_worst = Json::object(vec![
        ("configurationsCompared", Json::Int(paired as i64)),
        ("maxAbsDeltaEpsOverAbsM", Json::Float(worst_eps)),
        ("maxRelativeDeltaE", Json::Float(worst_e_relative)),
        ("maxAbsDeltaGapOverAbsM", Json::Float(worst_gap)),
        ("maxAbsDeltaDeltaScfOverAbsM", Json::Float(worst_delta_scf)),
        ("maxProfileDeviationRelative", Json::Float(worst_profile)),
        ("maxOrbitalSwapDeviation", Json::Float(worst_orbital)),
        (
            "maxScalarTotalFlipRelative",
            Json::Float(worst_scalar_flip_relative),
        ),
    ]);
    let (t3_true, t3_total) = theory_export.t3_checks;
    finish(
        ctx,
        &dir,
        &mut summary,
        vec![
            (
                "pairingTheory",
                Json::object(vec![
                    ("path", Json::str(PAIRING_THEORY_PATH)),
                    ("present", Json::Bool(theory_export.present)),
                    ("sha256", Json::str(&theory_export.sha256)),
                    ("t3ChecksTrue", Json::Int(t3_true as i64)),
                    ("t3ChecksTotal", Json::Int(t3_total as i64)),
                    ("theoremStandardRule", Json::str(&theory_export.theorem_standard_rule)),
                ]),
            ),
            ("reference", reference_json(&reference)),
            (
                "matrix",
                Json::object(vec![
                    ("statistics", Json::str("dirac16complex (sg = -1: e_x = -(lambda/32)(n^2 + S^2), M_eff = m + (15/16) lambda S_p, v_x = -(lambda/16) n_p) and dirac16complex00 (sg = +1: e_x = +(lambda/32)(n^2 + S^2), M_eff = m + (17/16) lambda S_p, v_x = +(lambda/16) n_p)")),
                    ("absMasses", Json::str(if ctx.quick { "1" } else { "1, 3" })),
                    ("L", Json::Float(PAIRS_LENGTH)),
                    ("particleNumbers", Json::str(if ctx.quick { "8" } else { "8 and N_mid(|m|) (Stage-4 reference: closed shell nearest 100)" })),
                    ("couplings", Json::str(if ctx.quick { "lambda_hat in {0, +-lambda_hat_1} of (|m|, L, N)" } else { "lambda_hat in {0, +-lambda_hat_1, +-lambda_hat_2}: the Stage-4 couplings of (|m|, L, N), the same numbers for both statistics and for the three universes" })),
                    ("temperatures", Json::str(if ctx.quick { "T = 0 and T/|m| = 0.1 (N = 8)" } else { "T = 0 for every N; T/|m| = 0.1 for N = N_mid(|m|)" })),
                    ("universes", Json::Array(Universe::ALL.iter().map(|u| Json::object(vec![
                        ("name", Json::str(u.name())),
                        ("description", Json::str(u.describe())),
                    ])).collect())),
                    ("configurations", Json::Int(configs.len() as i64)),
                ]),
            ),
            (
                "pairingTolerances",
                Json::object(vec![
                    ("epsAbsolutePerAbsM", Json::Float(PAIRING_EPS_TOLERANCE)),
                    ("energyRelative", Json::Float(PAIRING_ENERGY_RTOL)),
                    ("energyAbsolutePerAbsM", Json::Float(PAIRING_ENERGY_ATOL)),
                    ("occupationAbsolute", Json::Float(PAIRING_OCCUPATION_TOLERANCE)),
                    ("profileRelative", Json::Float(PAIRING_PROFILE_RTOL)),
                    ("orbitalAbsolute", Json::Float(PAIRING_ORBITAL_TOLERANCE)),
                    ("controlFactor", Json::Float(CONTROL_FACTOR)),
                    ("controlMinimumDifference", Json::Float(CONTROL_MIN_DIFFERENCE)),
                ]),
            ),
            ("freeSection", free),
            ("pairingWorst", pairing_worst),
            (
                "excitedStateRule",
                Json::str("T = 0: KS gap, particle-hole list (occupation floor 1e-12, STAGE4_SPEC E4.9) and Delta-SCF (scf::delta_scf); T > 0: the Mermin state, the KS gap (HOMO/LUMO by f >= 1/2 / f < 1/2) and the particle-hole list with holes f >= 1/2, particles f < 1/2 (E4.9); Delta-SCF is a T = 0 construction and is not computed at T > 0"),
            ),
            (
                "stage4Sources",
                Json::Array(
                    stage4
                        .sources
                        .iter()
                        .map(|(p, ok)| Json::object(vec![("path", Json::str(p)), ("read", Json::Bool(*ok))]))
                        .collect(),
                ),
            ),
            ("configurations", Json::Array(configurations)),
            ("oppositeCoupling", Json::Array(opposite)),
            ("statistics", Json::Array(statistics_records)),
            ("controlOutcomes", Json::Array(control_outcomes)),
        ],
    )?;
    Ok(summary)
}

/// A field of an output JSON object (cloned).
fn object_field(value: &Json, key: &str) -> Option<Json> {
    match value {
        Json::Object(pairs) => pairs.iter().find(|(k, _)| k == key).map(|(_, v)| v.clone()),
        _ => None,
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::scf::{solve, standard_params};
    use crate::shooting::DEFAULT_TOLERANCES;

    fn free_shooter(mass: f64, length: f64, tip: TipBag) -> Shooter {
        Shooter::new(
            Arc::new(Potential::free(1.0, 0.0, length, mass, 301).with_tip(tip)),
            DEFAULT_TOLERANCES,
        )
    }

    #[test]
    fn real_system_swap_identity() {
        // P N_s(M, kappa k, eps) P = N_{-s}(-M, kappa k, eps), P = [[0, 1], [1, 0]]
        for s in [1.0, -1.0] {
            for (m, kk, eps) in [(0.7, 1.3, -0.4), (-2.0, 0.0, 3.1), (1.0, -0.5, 0.0)] {
                let n = blocks::real_system(m, kk, eps, s);
                let swapped = [[n[1][1], n[1][0]], [n[0][1], n[0][0]]];
                let image = blocks::real_system(-m, kk, eps, -s);
                for p in 0..2 {
                    for q in 0..2 {
                        assert_eq!(swapped[p][q], image[p][q], "s={s} m={m}");
                    }
                }
            }
        }
    }

    #[test]
    fn image_key_is_an_involution() {
        let key: Key = (7, 1, -1, -3);
        assert_eq!(image_key(key), (7, -1, 1, 3));
        assert_eq!(image_key(image_key(key)), key);
        assert_eq!(TipBag::B.swapped(), TipBag::A);
        assert_eq!(TipBag::A.swapped().swapped(), TipBag::A);
        assert_eq!(TipBag::default(), TipBag::B);
        assert_eq!(TipBag::B.pruefer_angle(), 0.0);
        assert_eq!(TipBag::A.bag_angle(), PI);
    }

    #[test]
    fn gamma8_is_sigma2_between_partner_blocks() {
        let (defect, phases) = gamma8_block_map();
        assert!(defect < 1e-14, "{defect}");
        assert_eq!(phases.len(), 8);
        for (b, p, alpha) in &phases {
            // partner has the opposite block type s (blocks 0..3 <-> 4..7)
            assert_eq!(
                blocks::derive().labels[*b][0],
                -blocks::derive().labels[*p][0]
            );
            assert!(((alpha.0 * alpha.0 + alpha.1 * alpha.1) - 1.0).abs() < 1e-14);
        }
    }

    #[test]
    fn block_map_on_the_free_spectrum() {
        // plusM (m = 1, b(-L) = 0) and minusM (m = -1, a(-L) = 0): the s = +1
        // level (p, n, eps) of plusM is the s = -1 level (-p, -n, eps) of
        // minusM, i.e. (v_x = 0) the s = +1 level (-p, -n, -eps) of minusM,
        // with the orbital (a, b) -> +-(b, a)
        let mut plus = free_shooter(1.0, 3.0, TipBag::B);
        let mut minus = free_shooter(-1.0, 3.0, TipBag::A);
        for k in [0.0, 0.25, 1.0] {
            for parity in [1i32, -1] {
                let a = plus.levels(k, parity, -3.5, 3.5, &[]).unwrap();
                let b = minus.levels(k, -parity, -3.5, 3.5, &[]).unwrap();
                assert_eq!(a.len(), b.len(), "k={k} p={parity}");
                assert!(!a.is_empty());
                for level in &a {
                    let image = b
                        .iter()
                        .find(|l| l.index == -level.index)
                        .unwrap_or_else(|| panic!("k={k} p={parity} n={}: no image", level.index));
                    assert!(
                        (image.eps + level.eps).abs() < 1e-9,
                        "k={k} p={parity} n={}: {} vs {}",
                        level.index,
                        level.eps,
                        image.eps
                    );
                    let mut best = f64::INFINITY;
                    for sigma in [1.0, -1.0] {
                        let mut dev: f64 = 0.0;
                        for i in 0..level.a.len() {
                            dev = dev
                                .max((level.a[i] - sigma * image.b[i]).abs())
                                .max((level.b[i] - sigma * image.a[i]).abs());
                        }
                        best = best.min(dev);
                    }
                    assert!(best < 1e-7, "k={k} p={parity} n={}: {best}", level.index);
                    // S = -2 s a b flips: the minus level is used as an s = -1 state
                    assert!((level.scalar_charge - image.scalar_charge).abs() < 1e-8);
                }
            }
        }
        // the same at the level of the Kohn-Sham spectrum (keys and multiplicities)
        let mut p = standard_params(1.0, 3.0, 0.0, 0.0, 8.0);
        p.shell_cap = 9;
        let mut q = p.clone();
        q.m = -1.0;
        q.tip_bag = TipBag::A;
        let window = Window {
            eps_lo: -2.5,
            eps_hi: 2.5,
        };
        let sp = compute_spectrum(
            &p,
            &scf::build_potential(&p, &Densities::zero(p.grid_n)),
            window,
            &Default::default(),
        )
        .unwrap();
        let sq = compute_spectrum(
            &q,
            &scf::build_potential(&q, &Densities::zero(q.grid_n)),
            window,
            &Default::default(),
        )
        .unwrap();
        assert_eq!(sp.states.len(), sq.states.len());
        let index: HashMap<Key, &State> = sq.states.iter().map(|s| (s.key(), s)).collect();
        for st in &sp.states {
            let other = index
                .get(&image_key(st.key()))
                .unwrap_or_else(|| panic!("no image of {:?}", st.key()));
            assert!((st.eps - other.eps).abs() < 1e-9);
            assert_eq!(st.mult, other.mult);
        }
        let (worst, count) = orbital_swap(&sp, &sq);
        assert_eq!(count, sp.states.len());
        assert!(worst < 1e-7, "{worst}");
    }

    #[test]
    fn negative_mass_free_box_spectrum_is_analytic() {
        for (mass, length) in [(1.0, 3.0), (3.0, 2.0), (0.25, 3.0)] {
            for universe in Universe::ALL {
                let mut sh = free_shooter(universe.mass_sign() * mass, length, universe.tip());
                for parity in [1i32, -1] {
                    let limit = 4.0 * mass.max(1.0);
                    let mut numeric: Vec<f64> = sh
                        .levels(0.0, parity, -limit, limit, &[])
                        .unwrap()
                        .iter()
                        .map(|l| l.eps)
                        .collect();
                    numeric.sort_by(|a, b| a.partial_cmp(b).unwrap());
                    let analytic = analytic_k0_levels(universe, parity, mass, length, limit);
                    assert_eq!(
                        numeric.len(),
                        analytic.len(),
                        "{} p={parity} M={mass} L={length}: {numeric:?} vs {analytic:?}",
                        universe.name()
                    );
                    for (x, y) in numeric.iter().zip(&analytic) {
                        assert!(
                            (x - y).abs() < 1e-8,
                            "{} p={parity}: {x} vs {y}",
                            universe.name()
                        );
                    }
                }
            }
        }
        // the sub-gap bound state of the control exists iff M L > 1
        assert!(control_bound_state_kappa(1.0, 3.0).is_some());
        assert!(control_bound_state_kappa(0.25, 3.0).is_none());
        let kappa = control_bound_state_kappa(1.0, 3.0).unwrap();
        assert!((tanh(3.0 * kappa) - kappa).abs() < 1e-14 && kappa > 0.5 && kappa < 1.0);
        let mut control = free_shooter(-1.0, 3.0, TipBag::B);
        let odd = control.levels(0.0, -1, -0.99, 0.99, &[]).unwrap();
        assert_eq!(
            odd.len(),
            2,
            "{:?}",
            odd.iter().map(|l| l.eps).collect::<Vec<_>>()
        );
        let mut plus = free_shooter(1.0, 3.0, TipBag::B);
        assert!(plus.levels(0.0, -1, -0.99, 0.99, &[]).unwrap().is_empty());
    }

    #[test]
    fn zero_mode_localisation_for_negative_mass() {
        let (mass, length) = (1.0, 3.0);
        // minusM: (a, b) = (0, +-N e^{My}) (brane); control: (+-N_c e^{-My}, 0) (tip)
        let norm = (2.0 * mass / (1.0 - exp(-2.0 * mass * length))).sqrt();
        let norm_c = (2.0 * mass / (exp(2.0 * mass * length) - 1.0)).sqrt();
        let mut minus = free_shooter(-mass, length, TipBag::A);
        let zero = minus
            .levels(0.0, -1, -0.5, 0.5, &[])
            .unwrap()
            .into_iter()
            .find(|l| l.index == 0)
            .expect("minusM zero mode in parity -");
        assert_eq!(zero.eps, 0.0);
        let grid = crate::shooting::grid_points(length, 301);
        let sign = zero.b[150].signum();
        for (i, y) in grid.iter().enumerate() {
            assert!(zero.a[i].abs() < 1e-12);
            assert!((sign * zero.b[i] - norm * exp(mass * y)).abs() < 1e-8);
        }
        let mut control = free_shooter(-mass, length, TipBag::B);
        let zero_c = control
            .levels(0.0, 1, -0.05, 0.05, &[])
            .unwrap()
            .into_iter()
            .find(|l| l.index == 0)
            .expect("control zero mode in parity +");
        assert_eq!(zero_c.eps, 0.0);
        let sign = zero_c.a[0].signum();
        for (i, y) in grid.iter().enumerate() {
            assert!(zero_c.b[i].abs() < 1e-12);
            assert!((sign * zero_c.a[i] - norm_c * exp(-mass * y)).abs() < 1e-8);
        }
        // the splitting constants at M = H = 1, L = 3 (pairing-theory.json values)
        let c = splitting_paired(1.0, 1.0, 3.0, 0.0);
        let cc = splitting_control(1.0, 1.0, 3.0, 0.0);
        // (Wolfram values 1.905148253644866438..., 13.421975197576823014...)
        assert!((c / 1.905_148_253_644_866_5 - 1.0).abs() < 1e-14, "{c}");
        assert!((cc / 13.421_975_197_576_823 - 1.0).abs() < 1e-14, "{cc}");
    }

    #[test]
    fn statistics_sign_in_the_kohn_sham_potentials() {
        // same densities, both statistics: v_x opposite, (M_eff - m) in the ratio 17/15
        let mut p = standard_params(1.0, 3.0, 0.05, 0.0, 8.0);
        let grid = p.grid();
        let densities = Densities {
            n_c: grid.iter().map(|y| 1e-3 * exp(2.0 * y)).collect(),
            s_c: grid.iter().map(|y| 4e-4 * exp(1.5 * y)).collect(),
        };
        let anti = scf::build_potential(&p, &densities);
        p.statistics = Statistics::Commuting;
        let comm = scf::build_potential(&p, &densities);
        for i in 0..grid.len() {
            let va = anti.v_x.values[i];
            let vc = comm.v_x.values[i];
            assert!(va < 0.0 && vc > 0.0 && (va + vc).abs() <= 1e-15 * va.abs());
            let ra = anti.m_eff.values[i] - 1.0;
            let rc = comm.m_eff.values[i] - 1.0;
            // M_eff - m is formed by a subtraction from m = 1 (cancellation ~1e-12)
            assert!((rc / ra - 17.0 / 15.0).abs() < 1e-9, "{} {}", ra, rc);
        }
    }

    #[test]
    fn stage4_defaults_are_unchanged() {
        let p = standard_params(1.0, 3.0, 0.01, 0.0, 8.0);
        assert_eq!(p.statistics, Statistics::Anticommuting);
        assert_eq!(p.tip_bag, TipBag::B);
        let text = crate::runs::params_json(&p).to_text();
        assert!(!text.contains("statistics") && !text.contains("tipBag"));
        let mut q = p.clone();
        q.statistics = Statistics::Commuting;
        q.tip_bag = TipBag::A;
        let text = crate::runs::params_json(&q).to_text();
        assert!(text.contains("\"statistics\": \"dirac16complex00\""));
        assert!(text.contains("\"tipBag\": \"a(-L) = 0"));
        // negative mass: the scales are those of |m|
        let mut r = p.clone();
        r.m = -1.0;
        assert_eq!(r.delta_k(), p.delta_k());
        assert_eq!(r.window_floor(), p.window_floor());
        assert_eq!(r.lambda(), p.lambda());
    }

    #[test]
    fn direct_solver_equals_solve_ground_when_it_converges() {
        // the control's direct SCF attempt is the first stage of solve_ground
        let p = standard_params(1.0, 2.0, 0.05, 0.0, 32.0);
        let a = compute_universe(&p, GroundSolver::Continuation).unwrap();
        let b = compute_universe(&p, GroundSolver::Direct).unwrap();
        assert!(a.ground.converged && b.ground.converged);
        assert!(Digest::of(&a).bitwise_equal(&Digest::of(&b)));
        assert_eq!(Universe::Control.solver(), GroundSolver::Direct);
        assert_eq!(Universe::Minus.solver(), GroundSolver::Continuation);
    }

    #[test]
    fn first_update_gate() {
        // lambda = 0: no shift; lambda != 0: plusM and minusM have the same
        // first update (the free states pair), the control a much larger one
        let free = standard_params(1.0, 3.0, 0.0, 0.0, 8.0);
        let (shift, floor) = first_update_shift(&free).unwrap();
        assert_eq!(shift, 0.0);
        assert!((floor - (2.5 + 2.0 * PI / 3.0)).abs() < 1e-14);
        let p = standard_params(1.0, 3.0, 0.009729890470551316, 0.0, 8.0);
        let mut q = p.clone();
        q.m = -1.0;
        q.tip_bag = TipBag::A;
        let mut c = p.clone();
        c.m = -1.0;
        let (sp, _) = first_update_shift(&p).unwrap();
        let (sq, _) = first_update_shift(&q).unwrap();
        let (sc, fc) = first_update_shift(&c).unwrap();
        assert!((sp - sq).abs() < 1e-9 * sp, "{sp} vs {sq}");
        // lambda_hat_1 of (1, 3, 8): first-order pseudo-potential 0.1 m (v_x)
        assert!(sp > 0.09 && sp < 0.2, "{sp}");
        assert!(sc > fc, "control first update {sc} vs floor {fc}");
    }

    #[test]
    fn interacting_kohn_sham_states_pair_exactly() {
        // the SCF level of T3: (m, lambda, b(-L) = 0) and (-m, lambda, a(-L) = 0)
        for statistics in Statistics::ALL {
            let mut p = standard_params(1.0, 2.0, 0.05, 0.0, 32.0);
            p.statistics = statistics;
            let mut q = p.clone();
            q.m = -1.0;
            q.tip_bag = TipBag::A;
            let a = solve(&p, &Occupation::Zero, None, 0.0).unwrap();
            let b = solve(&q, &Occupation::Zero, None, 0.0).unwrap();
            assert!(a.converged && b.converged);
            let rel = (a.energies.total - b.energies.total).abs() / a.energies.total.abs();
            assert!(
                rel < 1e-9,
                "{statistics:?}: {} vs {}",
                a.energies.total,
                b.energies.total
            );
            assert!((a.filling.mu - b.filling.mu).abs() < 1e-9);
            assert!(
                (a.energies.scalar_total + b.energies.scalar_total).abs()
                    < 1e-9 * a.energies.scalar_total.abs().max(1e-12)
            );
            let index: HashMap<Key, &State> =
                b.spectrum.states.iter().map(|s| (s.key(), s)).collect();
            for st in &a.spectrum.states {
                let other = index.get(&image_key(st.key())).expect("image level");
                assert!((st.eps - other.eps).abs() < 1e-9);
                assert!((st.weight - other.weight).abs() < 1e-12);
            }
            for i in 0..p.grid_n {
                let scale = a.densities.n_c.iter().fold(0.0f64, |x, y| x.max(y.abs()));
                assert!((a.densities.n_c[i] - b.densities.n_c[i]).abs() < 1e-8 * scale);
                assert!((a.densities.s_c[i] + b.densities.s_c[i]).abs() < 1e-8 * scale);
                assert!((a.potential.m_eff.values[i] + b.potential.m_eff.values[i]).abs() < 1e-9);
                assert!((a.potential.v_x.values[i] - b.potential.v_x.values[i]).abs() < 1e-9);
            }
        }
    }
}
