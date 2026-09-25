//! dirac16complex_kohn_sham -- Stage-4 Kohn-Sham (Mermin finite-temperature
//! LDA) solver for the dirac16complex fermion gas in the static primordial
//! gravitational field (STAGE4_SPEC.md, CONTRACT.md, NUMERICS_CONTRACT.md).
//!
//! Every differential equation is integrated with the vendored pure-Rust
//! SUNDIALS 7.8.0 CVODE engine (`vendor/rustSolveIt/sundials_rs`): the
//! eigenvalue problems are solved by shooting in the proper hidden
//! coordinate y from the tip cutoff y = -L to the brane y = 0 (module
//! [`shooting`]), never by a matrix discretisation.
//!
//! # Shared infrastructure (origin: Stage-3 crate studies/dirac16complex_cosmology)
//!
//! `RunContext`, `Tolerances`, `ExperimentSummary`, `Check`, the `math`
//! module and the modules `driver` (CVODE closure trampoline) and `output`
//! (deterministic CSV/JSON writers) are copies of the Stage-3 code of this
//! repository (GPL-3.0-or-later); the copies are credited in each file.
//!
//! # Module map
//!
//! * [`blocks`]    -- numerically exact 2x2 block reduction of the reduced
//!   Dirac operator, derived from the fixture constants by joint projectors
//!   and verified against the exact basis of `generated.rs` and the Clifford
//!   identities (to 1e-14).
//! * [`geometry`]  -- the static primordial field in the warped form, its
//!   curvature, the two extensions beyond y = 0 and the Israel brane stress.
//! * [`exchange`]  -- the uniform-gas Hartree-Fock exchange functional of the
//!   contact interaction (closed form), its LDA potentials, and the
//!   quadrature verification.
//! * [`spline`]    -- natural cubic splines for the potentials on the y grid.
//! * [`shooting`]  -- Pruefer-angle shooting (CVODE) for the levels of one
//!   (k, parity) 2x2 problem, node-count verification, profile integration.
//! * [`scf`]       -- shells, occupations (T = 0 and Fermi-Dirac), densities,
//!   potentials, Anderson mixing, the self-consistency loop, Delta-SCF,
//!   thermodynamics.
//! * [`emt`]       -- energy-momentum profiles, proper-volume averages, w's,
//!   brane-localised fraction, comparison with the required source.
//! * [`runs`]      -- the parameter matrix and the subcommands.
//!
//! Units: H = 1.  All output numbers are written with `fmt_e(v, 17)`.

#![forbid(unsafe_code)]
#![deny(warnings)]

pub mod blocks;
pub mod driver;
pub mod emt;
pub mod exchange;
mod generated;
pub mod geometry;
pub mod output;
pub mod runs;
pub mod scf;
pub mod shooting;
pub mod spline;

use std::fs;
use std::path::PathBuf;

pub use generated::{
    B_IMAG, BLOCK_BASIS_IM, BLOCK_BASIS_RE, BLOCK_BASIS_UNIT_SQUARED_INVERSE, BLOCK_COUNT,
    BLOCK_LABELS, BLOCK_SOURCE_COLUMN, CHARGE, CHIRALITY, ETA, FIXTURE_PATH, FIXTURE_SHA256,
    FIXTURE_SOURCE, FRAME_DIMENSION, GAMMA, SPINOR_DIMENSION,
};

/// Name recorded as "study" in every summary.json.
pub const STUDY: &str = "dirac16complex-kohn-sham";
/// Version of the summary.json layout written by [`output::standard_summary`].
pub const SCHEMA_VERSION: i64 = 1;
/// Solver engine identification recorded in every summary.json.
pub const ENGINE: &str = "sundials_rs 7.8.0 CVODE (pure Rust, vendor/rustSolveIt)";
/// Default output root (relative to the current working directory).
pub const DEFAULT_OUTPUT_ROOT: &str = "artifacts/dirac16complex/kohn-sham/rust";

/// Deterministic elementary functions (origin: Stage-3 lib.rs).
///
/// All transcendental functions come from `sundials_core::sundials_libm`
/// (host-independent).  `sqrt`, `abs`, `mul_add` are IEEE-exact.  Defined
/// here: `tanh`, `pow`, `softplus`, `atan2` (through `atan`, exact
/// quadrant logic) and `asinh`.
pub mod math {
    pub use sundials_core::sundials_libm::{
        acos, acosh, asin, atan, cos, cosh, exp, expm1, log, log1p, sin, sinh,
    };

    pub const PI: f64 = std::f64::consts::PI;

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

    /// atan2(y, x) built on the deterministic atan.
    pub fn atan2(y: f64, x: f64) -> f64 {
        if x > 0.0 {
            atan(y / x)
        } else if x < 0.0 {
            if y >= 0.0 {
                atan(y / x) + PI
            } else {
                atan(y / x) - PI
            }
        } else if y > 0.0 {
            PI / 2.0
        } else if y < 0.0 {
            -PI / 2.0
        } else {
            0.0
        }
    }

    /// Fermi-Dirac occupation 1/(e^x + 1), overflow-free.
    pub fn fermi(x: f64) -> f64 {
        if x >= 0.0 {
            let e = exp(-x);
            e / (1.0 + e)
        } else {
            1.0 / (exp(x) + 1.0)
        }
    }
}

/// Integration tolerances (after command-line overrides).
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Tolerances {
    pub rtol: f64,
    pub atol: f64,
    pub max_step: f64,
}

/// What `main.rs` hands to every subcommand.
#[derive(Clone, Debug)]
pub struct RunContext {
    /// Output root; subcommand X writes into `<output_root>/X/`.
    pub output_root: PathBuf,
    /// `--rtol`: replaces the default relative tolerance.
    pub rtol: Option<f64>,
    /// `--atol`: replaces the default absolute tolerance.
    pub atol: Option<f64>,
    /// `--refined`: divide rtol and atol by 10 and max_step by 2.
    pub refined: bool,
    /// `--quick`: a reduced parameter matrix (documented in runs.rs); the
    /// canonical artifacts are produced WITHOUT this flag.
    pub quick: bool,
}

impl RunContext {
    pub fn new(output_root: PathBuf) -> Self {
        Self {
            output_root,
            rtol: None,
            atol: None,
            refined: false,
            quick: false,
        }
    }

    /// Apply the command-line options to the default tolerances.
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

/// One self-check of a subcommand.
#[derive(Clone, Debug)]
pub struct Check {
    pub name: String,
    pub passed: bool,
    pub detail: String,
}

/// The result a subcommand returns to `main.rs`.
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
