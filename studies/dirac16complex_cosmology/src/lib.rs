//! dirac16complex_cosmology -- Stage-3 numerics of the dirac16complex programme.
//!
//! Every ODE in this crate is integrated with the vendored pure-Rust SUNDIALS
//! 7.8.0 CVODE engine (`vendor/rustSolveIt/sundials_rs`); nothing is stepped by
//! hand.  Conventions are those of CONTRACT.md and NUMERICS_CONTRACT.md
//! (zero-based indices, eta = diag(1,1,1,1,-1,-1,-1,-1), t = x4).
//!
//! # Shared API for the experiment modules (read this before editing expN.rs)
//!
//! Each experiment lives in exactly one file `src/expN.rs` and exposes exactly
//!
//! ```text
//! pub fn run(ctx: &crate::RunContext) -> Result<crate::ExperimentSummary, String>
//! ```
//!
//! `main.rs` dispatches the subcommands `exp1` .. `exp5` and `all` to these
//! functions, prints every check as `PASS - name: detail` / `FAIL - ...`, and
//! prints the final `SUCCESS` / `FAILURE` line (exit code 0 / 1).  Returning
//! `Err(message)` counts as a failure of that experiment.  An experiment module
//! needs nothing outside its own file; it can use:
//!
//! * [`RunContext`] -- the output root and the command-line tolerance options.
//!   - `ctx.experiment_dir("expN")` creates `<output>/expN/` and removes a stale
//!     `summary.json` there, so a failed run can never leave an old verdict.
//!   - `ctx.tolerances(Tolerances { rtol, atol, max_step })` applies `--rtol`,
//!     `--atol` (replace the defaults) and `--refined` (rtol/10, atol/10,
//!     max_step/2) to the experiment's own defaults.  Record the result in
//!     summary.json (the standard summary does this).
//! * [`ExperimentSummary`] -- `ExperimentSummary::new("expN")`, then
//!   `summary.check(name, passed, detail)` for every self-check,
//!   `summary.add_file("name.csv")` for every written file (the Python
//!   checkers compare exactly these files for repeat-run byte identity) and
//!   `summary.add_stats(steps, rhs_evals)`.
//! * [`output`] -- deterministic writers: `output::write_csv(path, &header,
//!   &rows)` (header row, `fmt_e(v, 17)`, LF, trailing newline) and the
//!   ordered JSON value [`output::Json`] with `output::write_json`.
//!   `output::standard_summary(ctx, &summary, &tolerances, solver_description,
//!   extra_fields)` builds the fixed-order summary.json document
//!   (schemaVersion, study, experiment, fixture hash, engine, tolerances,
//!   the experiment's own fields, files, solver totals, checks, verdict);
//!   `output::write_json(&dir.join("summary.json"), &doc)` writes it.
//!   Order: write every data file and `add_file` it, record every check,
//!   build the document with `standard_summary` (it appends "summary.json"
//!   to the file list and derives the verdict from the checks), write it,
//!   then `summary.add_file("summary.json")` and return the summary.
//!   Never put absolute paths or timings into outputs: the repeat run writes
//!   into a different directory and must be byte-identical.
//! * [`driver`] -- `driver::integrate(y0, t0, &targets, rhs, &cfg)` with a
//!   boxed `'static` closure `rhs(t, y, ydot) -> Result<(), String>` (move
//!   owned data into it), and `driver::integrate_backward` for decreasing
//!   targets; `driver::uniform_targets(t0, t1, n)` builds an exact uniform
//!   grid.  `SolverConfig::bdf(rtol, atol, max_step)` (Newton + dense) or
//!   `SolverConfig::adams(..)` (fixed-point iteration), optionally
//!   `.with_stop_time(t_end)`; `cfg.describe()` is the solver string for
//!   summary.json.  The returned `Integration` holds `times[0] = t0`,
//!   `states[0] = y0`, then one entry per target, plus the CVODE counters.
//!   `src/exp1.rs` (BDF) and `src/exp5.rs` (Adams) are worked examples.
//! * [`spinor`] -- 16x16 complex matrices [`spinor::CMat16`], spinors
//!   [`spinor::CVec16`] stored in the ODE state as 32 reals
//!   `(re0..re15, im0..im15)`, the precomputed [`spinor::Algebra`] (gamma^a,
//!   gamma^4 gamma^j, C, B, chirality from `generated.rs`), the mode
//!   Hamiltonian `h = -i M_eff gamma^4 - gamma^4 sum_j (k_j/h_j) gamma^j`, the
//!   RHS of `i du/dt = h u`, bilinears, the expectation-value rule
//!   `<Psi^dagger M Psi> = u^dagger B M u`, projector-based eigenvectors and
//!   the exact propagator for constant h.
//! * [`math`] -- deterministic transcendental functions (sundials_libm).
//!   Use these, never `f64::exp` & co., so outputs are reproducible.
//! * the generated algebra constants re-exported below.

#![forbid(unsafe_code)]
#![deny(warnings)]

pub mod driver;
pub mod exp1;
pub mod exp2;
pub mod exp3;
pub mod exp4;
pub mod exp5;
mod generated;
pub mod output;
pub mod spinor;

use std::fs;
use std::path::PathBuf;

pub use generated::{
    B_IMAG, CHARGE, CHIRALITY, ETA, FIXTURE_PATH, FIXTURE_SHA256, FIXTURE_SOURCE, FRAME_DIMENSION,
    GAMMA, SPINOR_DIMENSION,
};

/// Name recorded as "study" in every summary.json.
pub const STUDY: &str = "dirac16complex-cosmology";
/// Version of the summary.json layout written by [`output::standard_summary`].
pub const SCHEMA_VERSION: i64 = 1;
/// Solver engine identification recorded in every summary.json.
pub const ENGINE: &str = "sundials_rs 7.8.0 CVODE (pure Rust, vendor/rustSolveIt)";
/// Default output root (relative to the current working directory).
pub const DEFAULT_OUTPUT_ROOT: &str = "artifacts/dirac16complex/numerics";

/// Deterministic elementary functions.
///
/// All transcendental functions come from `sundials_core::sundials_libm`
/// (exp, log, expm1, log1p, sin, cos, atan, asin, acos, sinh, cosh, acosh),
/// which are host-independent.  `sqrt`, `abs`, `mul_add` are IEEE-exact and
/// used from `f64` directly.  Not available in sundials_libm and therefore
/// defined here: `tanh` (through expm1, overflow-free), `pow` (as
/// exp(b log x), x > 0) and `softplus` (log(1 + e^x) through log1p).
pub mod math {
    pub use sundials_core::sundials_libm::{
        acos, acosh, asin, atan, cos, cosh, exp, expm1, log, log1p, sin, sinh,
    };

    /// tanh(x) = -expm1(-2|x|) / (2 + expm1(-2|x|)) * sign(x); never overflows.
    pub fn tanh(x: f64) -> f64 {
        if x.is_nan() {
            return x;
        }
        let e = expm1(-2.0 * x.abs());
        let value = -e / (2.0 + e);
        if x < 0.0 {
            -value
        } else {
            value
        }
    }

    /// x^y for x > 0, computed as exp(y log x).
    pub fn pow(x: f64, y: f64) -> f64 {
        exp(y * log(x))
    }

    /// softplus(x) = log(1 + e^x) = max(x, 0) + log1p(e^{-|x|}).
    pub fn softplus(x: f64) -> f64 {
        x.max(0.0) + log1p(exp(-x.abs()))
    }
}

/// Integration tolerances of one experiment (after command-line overrides).
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Tolerances {
    pub rtol: f64,
    pub atol: f64,
    pub max_step: f64,
}

/// What `main.rs` hands to every experiment.
#[derive(Clone, Debug)]
pub struct RunContext {
    /// Output root; experiment N writes into `<output_root>/expN/`.
    pub output_root: PathBuf,
    /// `--rtol`: replaces the experiment's default relative tolerance.
    pub rtol: Option<f64>,
    /// `--atol`: replaces the experiment's default absolute tolerance.
    pub atol: Option<f64>,
    /// `--refined`: divide rtol and atol by 10 and max_step by 2.
    pub refined: bool,
}

impl RunContext {
    pub fn new(output_root: PathBuf) -> Self {
        Self {
            output_root,
            rtol: None,
            atol: None,
            refined: false,
        }
    }

    /// Apply the command-line options to an experiment's default tolerances.
    pub fn tolerances(&self, defaults: Tolerances) -> Tolerances {
        let mut result = defaults;
        if let Some(rtol) = self.rtol {
            result.rtol = rtol;
        }
        if let Some(atol) = self.atol {
            result.atol = atol;
        }
        if self.refined {
            result.rtol /= 10.0;
            result.atol /= 10.0;
            result.max_step /= 2.0;
        }
        result
    }

    /// Create `<output_root>/<name>/` and remove a stale summary.json in it.
    pub fn experiment_dir(&self, name: &str) -> Result<PathBuf, String> {
        let directory = self.output_root.join(name);
        fs::create_dir_all(&directory)
            .map_err(|error| format!("cannot create {}: {error}", directory.display()))?;
        let stale = directory.join("summary.json");
        if stale.exists() {
            fs::remove_file(&stale)
                .map_err(|error| format!("cannot remove stale {}: {error}", stale.display()))?;
        }
        Ok(directory)
    }
}

/// One self-check of an experiment.
#[derive(Clone, Debug)]
pub struct Check {
    pub name: String,
    pub passed: bool,
    pub detail: String,
}

/// The result an experiment returns to `main.rs`.
#[derive(Clone, Debug, Default)]
pub struct ExperimentSummary {
    pub experiment: String,
    pub checks: Vec<Check>,
    /// Files written into the experiment directory (relative names, in
    /// writing order, summary.json last).
    pub files: Vec<String>,
    pub solver_steps: i64,
    pub rhs_evaluations: i64,
}

impl ExperimentSummary {
    pub fn new(experiment: &str) -> Self {
        Self {
            experiment: experiment.to_string(),
            ..Self::default()
        }
    }

    /// Record a self-check; returns `passed` for convenience.
    pub fn check(&mut self, name: &str, passed: bool, detail: &str) -> bool {
        self.checks.push(Check {
            name: name.to_string(),
            passed,
            detail: detail.to_string(),
        });
        passed
    }

    pub fn add_file(&mut self, name: &str) {
        self.files.push(name.to_string());
    }

    pub fn add_stats(&mut self, steps: i64, rhs_evaluations: i64) {
        self.solver_steps += steps;
        self.rhs_evaluations += rhs_evaluations;
    }

    /// True when every check passed (and there is at least one).
    pub fn passed(&self) -> bool {
        !self.checks.is_empty() && self.checks.iter().all(|check| check.passed)
    }

    pub fn verdict(&self) -> &'static str {
        if self.passed() {
            "SUCCESS"
        } else {
            "FAILURE"
        }
    }
}
