//! Revision Kohn-Sham solver for dirac16complex in the author's primordial
//! field (Revision/SPEC.md section 7, Revision/kohn_sham/ks-theory.json).
//!
//! Usage (from the repository root):
//!   revision_ks_solver all [--out DIR] [--report FILE] [--refined] [--threads N] [--timing FILE] [--quick]
//! Defaults: --out Revision/kohn_sham/results, --report <out>/solver-report.json.
//! Every check prints `PASS - name: detail` / `FAIL - name: detail` on stderr;
//! the last stdout line is SUCCESS or FAILURE (exit code 0 / 1).

mod analysis;
mod json;
mod mermin;
mod model;
mod report;
mod runs;
mod scf;
mod sha256;
mod shoot;
mod spectrum;
mod theory;

use std::path::PathBuf;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() >= 2 && args[1] == "single" {
        single(&args);
        return;
    }
    if args.len() < 2 || args[1] != "all" {
        eprintln!("usage: revision_ks_solver all [--root DIR] [--out DIR] [--report FILE] [--refined] [--threads N] [--timing FILE] [--quick]");
        eprintln!("       revision_ks_solver single --m M --lambda L --a4 A --N N --out FILE.json [--tip-theta TH] [--T T] [--exx] [--margin W] [--profiles FILE.csv] [--mermin-levels FILE.json] [--refined] [--root DIR]");
        std::process::exit(2);
    }
    let mut root = PathBuf::from(".");
    let mut out: Option<PathBuf> = None;
    let mut report: Option<PathBuf> = None;
    let mut refined = false;
    let mut quick = false;
    let mut threads = std::thread::available_parallelism().map(|n| n.get()).unwrap_or(4).min(22);
    let mut timing = None;
    let mut i = 2;
    while i < args.len() {
        match args[i].as_str() {
            "--root" => {
                root = PathBuf::from(&args[i + 1]);
                i += 1;
            }
            "--out" => {
                out = Some(PathBuf::from(&args[i + 1]));
                i += 1;
            }
            "--report" => {
                report = Some(PathBuf::from(&args[i + 1]));
                i += 1;
            }
            "--threads" => {
                threads = args[i + 1].parse().expect("--threads N");
                i += 1;
            }
            "--timing" => {
                timing = Some(PathBuf::from(&args[i + 1]));
                i += 1;
            }
            "--refined" => refined = true,
            "--quick" => quick = true,
            a => {
                eprintln!("unknown argument {}", a);
                std::process::exit(2);
            }
        }
        i += 1;
    }
    let out = out.unwrap_or_else(|| root.join("Revision/kohn_sham/results"));
    let report = report.unwrap_or_else(|| out.join("solver-report.json"));
    let num = if refined { model::Numerics::refined() } else { model::Numerics::canonical() };
    let cfg = runs::Cfg { root: root.clone(), out, report, num, threads, quick, timing };
    let mut rep = report::Report::default();
    let th = match theory::read_and_check(&root, &mut rep) {
        Ok(t) => t,
        Err(e) => {
            eprintln!("theory input: {}", e);
            println!("FAILURE");
            std::process::exit(1);
        }
    };
    match runs::run_all(&cfg, &th, rep) {
        Ok(true) => println!("SUCCESS"),
        Ok(false) => {
            println!("FAILURE");
            std::process::exit(1);
        }
        Err(e) => {
            eprintln!("error: {}", e);
            println!("FAILURE");
            std::process::exit(1);
        }
    }
}

fn single(args: &[String]) {
    let mut root = PathBuf::from(".");
    let mut o = runs::SingleOpts { m: 1.0, lambda: 0.0, a4: 0.0, n: 8.0, tip_theta: 0.0, temp: 0.0, exx: false, margin: 0.85, out: PathBuf::from("single.json"), profiles: None, mermin_levels: None };
    let mut refined = false;
    let mut i = 2;
    let val = |i: usize| -> f64 { args.get(i + 1).and_then(|s| s.parse().ok()).unwrap_or_else(|| panic!("{} needs a number", args[i])) };
    while i < args.len() {
        match args[i].as_str() {
            "--m" => { o.m = val(i); i += 1; }
            "--lambda" => { o.lambda = val(i); i += 1; }
            "--a4" => { o.a4 = val(i); i += 1; }
            "--N" => { o.n = val(i); i += 1; }
            "--tip-theta" => { o.tip_theta = val(i); i += 1; }
            "--T" => { o.temp = val(i); i += 1; }
            "--margin" => { o.margin = val(i); i += 1; }
            "--exx" => o.exx = true,
            "--refined" => refined = true,
            "--out" => { o.out = PathBuf::from(&args[i + 1]); i += 1; }
            "--profiles" => { o.profiles = Some(PathBuf::from(&args[i + 1])); i += 1; }
            "--mermin-levels" => { o.mermin_levels = Some(PathBuf::from(&args[i + 1])); i += 1; }
            "--root" => { root = PathBuf::from(&args[i + 1]); i += 1; }
            a => { eprintln!("unknown argument {}", a); std::process::exit(2); }
        }
        i += 1;
    }
    let num = if refined { model::Numerics::refined() } else { model::Numerics::canonical() };
    let mut rep = report::Report::default();
    let th = theory::read_and_check(&root, &mut rep).unwrap_or_else(|e| { eprintln!("theory input: {}", e); std::process::exit(1) });
    match runs::run_single(&num, &th, &o) {
        Ok(true) => println!("SUCCESS"),
        Ok(false) => { println!("FAILURE"); std::process::exit(1); }
        Err(e) => { eprintln!("error: {}", e); println!("FAILURE"); std::process::exit(1); }
    }
}
