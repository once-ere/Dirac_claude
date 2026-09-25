//! dirac16complex_cosmology command-line entry.
//!
//! ```text
//! dirac16complex_cosmology <print-config|exp1|exp2|exp3|exp4|exp5|all>
//!     [--output DIR]   output root (default artifacts/dirac16complex/numerics);
//!                      experiment N writes into DIR/expN/
//!     [--rtol X]       replace every experiment's default relative tolerance
//!     [--atol X]       replace every experiment's default absolute tolerance
//!     [--refined]      rtol/10, atol/10, max_step/2 (convergence runs)
//! ```
//!
//! Contract (planet_Mercury style): every check prints `PASS - name: detail`
//! or `FAIL - name: detail`; the LAST stdout line is `SUCCESS` (exit code 0)
//! or `FAILURE` (exit code 1).

#![forbid(unsafe_code)]
#![deny(warnings)]

use std::path::PathBuf;

use dirac16complex_cosmology::output::fmt17;
use dirac16complex_cosmology::{
    exp1, exp2, exp3, exp4, exp5, ExperimentSummary, RunContext, DEFAULT_OUTPUT_ROOT, ENGINE,
    FIXTURE_PATH, FIXTURE_SHA256, FIXTURE_SOURCE, STUDY,
};

const USAGE: &str = "usage: dirac16complex_cosmology <print-config|exp1|exp2|exp3|exp4|exp5|all> \
[--output DIR] [--rtol X] [--atol X] [--refined]";

type Runner = fn(&RunContext) -> Result<ExperimentSummary, String>;

const EXPERIMENTS: [(&str, Runner); 5] = [
    ("exp1", exp1::run),
    ("exp2", exp2::run),
    ("exp3", exp3::run),
    ("exp4", exp4::run),
    ("exp5", exp5::run),
];

fn parse_positive(value: &str, flag: &str) -> Result<f64, String> {
    let parsed = value
        .parse::<f64>()
        .map_err(|error| format!("invalid value for {flag}: {error}"))?;
    if !parsed.is_finite() || parsed <= 0.0 {
        return Err(format!("{flag} must be finite and positive"));
    }
    Ok(parsed)
}

fn parse(arguments: &[String]) -> Result<(String, RunContext), String> {
    let command = arguments
        .first()
        .ok_or_else(|| format!("missing subcommand\n{USAGE}"))?
        .clone();
    let known = command == "print-config"
        || command == "all"
        || EXPERIMENTS.iter().any(|(name, _)| *name == command);
    if !known {
        return Err(format!("unknown subcommand {command}\n{USAGE}"));
    }
    let mut ctx = RunContext::new(PathBuf::from(DEFAULT_OUTPUT_ROOT));
    let mut index = 1;
    while index < arguments.len() {
        let flag = arguments[index].as_str();
        match flag {
            "--refined" => {
                ctx.refined = true;
                index += 1;
                continue;
            }
            "--output" | "--rtol" | "--atol" => {}
            _ => return Err(format!("unknown option {flag}\n{USAGE}")),
        }
        let value = arguments
            .get(index + 1)
            .ok_or_else(|| format!("missing value for {flag}"))?;
        match flag {
            "--output" => ctx.output_root = PathBuf::from(value),
            "--rtol" => ctx.rtol = Some(parse_positive(value, flag)?),
            _ => ctx.atol = Some(parse_positive(value, flag)?),
        }
        index += 2;
    }
    Ok((command, ctx))
}

fn print_config(ctx: &RunContext) -> bool {
    println!("study            = {STUDY}");
    println!("engine           = {ENGINE}");
    println!("fixture          = {FIXTURE_PATH}");
    println!("fixture sha256   = {FIXTURE_SHA256}");
    println!("fixture source   = {FIXTURE_SOURCE}");
    println!("output root      = {}", ctx.output_root.display());
    println!(
        "rtol override    = {}",
        ctx.rtol.map(fmt17).unwrap_or_else(|| "none".to_string())
    );
    println!(
        "atol override    = {}",
        ctx.atol.map(fmt17).unwrap_or_else(|| "none".to_string())
    );
    println!("refined          = {}", ctx.refined);
    println!("state layout     = spinor u in C^16 as 32 reals (re0..re15, im0..im15)");
    let experiment_lines = exp1::config_lines()
        .into_iter()
        .chain(exp2::config_lines())
        .chain(exp3::config_lines())
        .chain(exp4::config_lines())
        .chain(exp5::config_lines());
    for line in experiment_lines {
        println!("{line}");
    }
    let names: Vec<&str> = EXPERIMENTS.iter().map(|(name, _)| *name).collect();
    println!("all              = {}", names.join(", "));
    true
}

fn run_one(name: &str, runner: Runner, ctx: &RunContext) -> bool {
    println!("== {name} ==");
    match runner(ctx) {
        Ok(summary) => {
            for check in &summary.checks {
                println!(
                    "{} - {}: {}",
                    if check.passed { "PASS" } else { "FAIL" },
                    check.name,
                    check.detail
                );
            }
            println!(
                "{name}: solver_steps={} rhs_evaluations={} files={} verdict={}",
                summary.solver_steps,
                summary.rhs_evaluations,
                summary.files.len(),
                summary.verdict()
            );
            summary.passed()
        }
        Err(error) => {
            println!("FAIL - {name}: {error}");
            false
        }
    }
}

fn main() {
    let arguments: Vec<String> = std::env::args().skip(1).collect();
    let passed = match parse(&arguments) {
        Err(error) => {
            println!("ERROR: {error}");
            false
        }
        Ok((command, ctx)) => match command.as_str() {
            "print-config" => print_config(&ctx),
            "all" => {
                let mut all = true;
                for (name, runner) in EXPERIMENTS {
                    all &= run_one(name, runner, &ctx);
                }
                all
            }
            name => match EXPERIMENTS.iter().find(|(n, _)| *n == name) {
                Some((n, runner)) => run_one(n, *runner, &ctx),
                None => false,
            },
        },
    };
    println!("{}", if passed { "SUCCESS" } else { "FAILURE" });
    std::process::exit(if passed { 0 } else { 1 });
}
