//! lovelock_gkd command line.
//!
//!   lovelock_gkd print-config
//!   lovelock_gkd gkd-selftest [--exhaustive-max P] [--output DIR]
//!   lovelock_gkd lovelock --output DIR [--brute-force-k2]
//!
//! `lovelock` computes, exactly and from the metric alone, the Christoffel symbols, the
//! Riemann tensor, and the three non-zero Lovelock tensors of equation (4.38) for n = 8
//! (k = 1, 2, 3) with GKD, writes every component, runs the checks and exits with status
//! 1 if any check fails.

// Tensor formulas read best with explicit index loops (a, b, c, d over the 8 coordinates).
#![allow(clippy::needless_range_loop)]

use lovelock_gkd::geometry::{Geometry, COORD, DIM};
use lovelock_gkd::gkd::{compare_exhaustive, compare_random, GKD};
use lovelock_gkd::lovelock::{brute_force_numeric, divergence, lovelock_contravariant, lovelock_mixed, lovelock_scalar};
use lovelock_gkd::output::{json_str, tensor_json, tensor_markdown};
use lovelock_gkd::poly::{Point, Poly, SV};
use lovelock_gkd::rational::Rational;
use std::fmt::Write as _;
use std::fs;
use std::path::PathBuf;
use std::time::Instant;

const METRIC_AS_GIVEN: &str = "{{exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0,0},{0,exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0},{0,0,exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0},{0,0,0,-1,0,0,0,0},{0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0},{0,0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0},{0,0,0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0},{0,0,0,0,0,0,0,Cot[6 H x8]^2}}";

struct Check {
    name: String,
    passed: bool,
    detail: String,
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let cmd = args.get(1).map(String::as_str).unwrap_or("");
    let opt = |name: &str| args.iter().position(|a| a == name).and_then(|i| args.get(i + 1)).cloned();
    let flag = |name: &str| args.iter().any(|a| a == name);
    match cmd {
        "print-config" => print_config(),
        "gkd-selftest" => {
            let pmax: usize = opt("--exhaustive-max").map(|s| s.parse().expect("--exhaustive-max")).unwrap_or(4);
            std::process::exit(gkd_selftest(pmax, opt("--output").map(PathBuf::from)));
        }
        "lovelock" => {
            let out = PathBuf::from(opt("--output").expect("lovelock needs --output DIR"));
            std::process::exit(run_lovelock(&out, flag("--brute-force-k2")));
        }
        _ => {
            eprintln!("usage: lovelock_gkd print-config | gkd-selftest [--exhaustive-max P] [--output DIR] | lovelock --output DIR [--brute-force-k2]");
            std::process::exit(2);
        }
    }
}

fn print_config() {
    println!("program          = lovelock_gkd {}", env!("CARGO_PKG_VERSION"));
    println!("metric (as given) = {}", METRIC_AS_GIVEN);
    println!("coordinates      = x1 x2 x3 (3-space), x4 (time), x5 x6 x7 (extra times), x8 (hidden; z = 6 H x8)");
    println!("riemann          = R^a_bcd = d_c G^a_db - d_d G^a_cb + G^a_ce G^e_db - G^a_de G^e_cb (MTW)");
    println!("lovelock (4.38)  = A_(k)^lh = sqrt(g) g^jl kdelta[{{j,j1..j2k}},{{h,h1..h2k}}] R^j1j2_h1h2 ... , k = 1, 2, 3 (n = 8, m = 4)");
    println!("gkd              = GKD(lower, upper) = Det[Outer[delta, lower, upper]] = sign of the permutation, or 0");
}

fn gkd_selftest(pmax: usize, out: Option<PathBuf>) -> i32 {
    let t0 = Instant::now();
    let mut lines = Vec::new();
    let mut ok = true;
    for p in 1..=pmax {
        let (n, bad) = compare_exhaustive(p, 8);
        ok &= bad == 0;
        println!("{} - GKD vs literal Det[Outer[delta,...]], all {} pairs of index lists of length {} over 8 values: {} mismatches", if bad == 0 { "PASS" } else { "FAIL" }, n, p, bad);
        lines.push(format!("{{\"p\": {}, \"mode\": \"exhaustive\", \"pairs\": {}, \"mismatches\": {}}}", p, n, bad));
    }
    for p in (pmax + 1)..=9 {
        let (n, bad, nz) = compare_random(p, 8, 200_000, 0x2545F4914F6CDD1D ^ p as u64);
        ok &= bad == 0;
        println!("{} - GKD vs literal determinant, {} pseudo-random pairs of length {} ({} nonzero): {} mismatches", if bad == 0 { "PASS" } else { "FAIL" }, n, p, nz, bad);
        lines.push(format!("{{\"p\": {}, \"mode\": \"random\", \"pairs\": {}, \"nonzero\": {}, \"mismatches\": {}}}", p, n, nz, bad));
    }
    println!("gkd-selftest: {} ({:.1} s)", if ok { "SUCCESS" } else { "FAILURE" }, t0.elapsed().as_secs_f64());
    if let Some(dir) = out {
        fs::create_dir_all(&dir).unwrap();
        let body = format!("{{\n  \"program\": \"lovelock_gkd gkd-selftest\",\n  \"definition\": {},\n  \"results\": [\n    {}\n  ],\n  \"verdict\": {}\n}}\n",
            json_str("kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]"),
            lines.join(",\n    "), json_str(if ok { "SUCCESS" } else { "FAILURE" }));
        fs::write(dir.join("gkd-selftest.json"), body).unwrap();
    }
    if ok { 0 } else { 1 }
}

fn run_lovelock(out: &PathBuf, brute_k2: bool) -> i32 {
    fs::create_dir_all(out).unwrap();
    let t0 = Instant::now();
    let geo = Geometry::new();
    let mut checks: Vec<Check> = Vec::new();
    let mut add = |name: &str, passed: bool, detail: String| {
        println!("{} - {}: {}", if passed { "PASS" } else { "FAIL" }, name, detail);
        checks.push(Check { name: name.to_string(), passed, detail });
    };

    // --- curvature checks ---
    let entries = geo.nonzero_mixed();
    let mut antisym = true;
    let mut bianchi = true;
    for a in 0..DIM {
        for b in 0..DIM {
            for c in 0..DIM {
                for d in 0..DIM {
                    let r = &geo.riemann_mixed[a][b][c][d];
                    antisym &= *r == -&geo.riemann_mixed[b][a][c][d] && *r == -&geo.riemann_mixed[a][b][d][c];
                    let s = &(&geo.riemann[a][b][c][d] + &geo.riemann[a][c][d][b]) + &geo.riemann[a][d][b][c];
                    bianchi &= s.is_zero();
                }
            }
        }
    }
    add("riemann_antisymmetry", antisym, format!("R^ab_cd = -R^ba_cd = -R^ab_dc exactly for all 4096 index lists; {} nonzero entries", entries.len()));
    add("riemann_first_bianchi", bianchi, "R^a_bcd + R^a_cdb + R^a_dbc = 0 exactly for all 4096 index lists".to_string());
    let s_free = entries.iter().all(|e| !e.4.contains(SV));
    add("mixed_riemann_free_of_sin_third", s_free, "every R^ab_cd is free of Sin[6 H x8]^(1/3) (the warp cancels in mixed components)".to_string());

    // --- Lovelock tensors k = 1, 2, 3 (and 4) ---
    let mut ps = Vec::new();
    let mut as_ = Vec::new();
    let mut ls = Vec::new();
    let mut counter_lines = Vec::new();
    for k in 1..=4usize {
        let tk = Instant::now();
        let (p, cnt) = lovelock_mixed(&geo, k);
        let (l, lcnt) = lovelock_scalar(&geo, k);
        let a = lovelock_contravariant(&geo, &p);
        let nonzero = p.iter().flatten().filter(|x| !x.is_zero()).count();
        println!("k = {}: {} index-list leaves, {} GKD calls, {} nonzero GKD values, {} nonzero components of P_(k), {:.1} s", k, cnt.leaves, cnt.gkd_calls, cnt.gkd_nonzero, nonzero, tk.elapsed().as_secs_f64());
        counter_lines.push(format!("{{\"k\": {}, \"leaves\": {}, \"gkdCalls\": {}, \"gkdNonzero\": {}, \"scalarGkdCalls\": {}, \"nonzeroComponents\": {}}}", k, cnt.leaves, cnt.gkd_calls, cnt.gkd_nonzero, lcnt.gkd_calls, nonzero));
        ps.push(p);
        as_.push(a);
        ls.push(l);
    }

    // P_(1) = -4 G
    let g_e = geo.einstein_mixed();
    let mut k1_ok = true;
    for h in 0..DIM {
        for j in 0..DIM {
            k1_ok &= ps[0][h][j] == g_e[h][j].scale(Rational::int(-4));
        }
    }
    add("k1_equals_minus_4_einstein", k1_ok, "P_(1)^h_j = -4 G^h_j exactly (G from the Ricci tensor, an independent route)".to_string());
    for k in 1..=3usize {
        let p = &ps[k - 1];
        // trace identity
        let mut tr = Poly::zero();
        for h in 0..DIM {
            tr = &tr + &p[h][h];
        }
        let expect = ls[k - 1].scale(Rational::int((DIM - 2 * k) as i128));
        add(&format!("k{}_trace_identity", k), tr == expect, format!("sum_h P_({})^h_h = (8 - {}) L_({}) exactly", k, 2 * k, k));
        // divergence
        let div = divergence(&geo, p);
        add(&format!("k{}_divergence_free", k), div.iter().all(|x| x.is_zero()), format!("nabla_h P_({})^h_j = 0 exactly for j = x1..x8", k));
        // symmetry of P_hj = g_hh P^h_j
        let mut sym = true;
        for h in 0..DIM {
            for j in 0..DIM {
                sym &= &geo.g[h] * &p[h][j] == &geo.g[j] * &p[j][h];
            }
        }
        add(&format!("k{}_symmetric", k), sym, format!("g_hh P_({})^h_j = g_jj P_({})^j_h exactly (so A_({})^lh = A_({})^hl)", k, k, k, k));
        let sf = p.iter().flatten().all(|x| !x.contains(SV));
        add(&format!("k{}_free_of_sin_third", k), sf, format!("every P_({})^h_j is free of Sin[6 H x8]^(1/3)", k));
    }
    add("k4_tensor_vanishes", ps[3].iter().flatten().all(|x| x.is_zero()), "P_(4) = 0 identically: GKD of 9 indices in 8 dimensions is 0 (pigeonhole), so (4.38) stops at k = m - 1 = 3".to_string());
    println!("info - L_(4) (8 indices, the 8-dimensional Euler density, not zero in general; its field equations P_(4) vanish identically): {}", ls[3].to_mathematica());

    // brute force (no pruning) at a numerical point
    let q = Point { h: 0.23, a4: 0.17, a1: 0.61, a2: -0.37, a3: 0.29, a4d4: 0.0, x8: 0.41 };
    for k in 1..=(if brute_k2 { 2 } else { 1 }) {
        let tb = Instant::now();
        let (bf, calls) = brute_force_numeric(&geo, k, &q);
        let mut worst: f64 = 0.0;
        for h in 0..DIM {
            for j in 0..DIM {
                let exact = ps[k - 1][h][j].eval(&q);
                worst = worst.max((exact - bf[h][j]).abs() / exact.abs().max(1.0));
            }
        }
        add(&format!("k{}_brute_force_numeric", k), worst < 1e-10, format!("literal sum over all {} index lists with GKD weights (no pruning) at H = 0.23, a4 = 0.17, a4' = 0.61, a4'' = -0.37, x8 = 0.41: max relative deviation from the exact P_({}) = {:.2e}", calls, k, worst));
        println!("info - brute force k = {} took {:.1} s", k, tb.elapsed().as_secs_f64());
    }

    // --- write the outputs ---
    let mut curv = String::from("{\n");
    writeln!(curv, "  \"program\": \"lovelock_gkd lovelock\",").unwrap();
    writeln!(curv, "  \"metricAsGiven\": {},", json_str(METRIC_AS_GIVEN)).unwrap();
    writeln!(curv, "  \"coordinates\": [\"x1\", \"x2\", \"x3\", \"x4\", \"x5\", \"x6\", \"x7\", \"x8\"],").unwrap();
    writeln!(curv, "  \"metricDiagonal\": [{}],", geo.g.iter().map(|x| json_str(&x.to_mathematica())).collect::<Vec<_>>().join(", ")).unwrap();
    writeln!(curv, "  \"sqrtAbsDetG\": {},", json_str(&geo.sqrt_g.to_mathematica())).unwrap();
    let mut chr = Vec::new();
    for a in 0..DIM {
        for b in 0..DIM {
            for c in b..DIM {
                if !geo.christoffel[a][b][c].is_zero() {
                    chr.push(format!("    {{\"a\": \"{}\", \"b\": \"{}\", \"c\": \"{}\", \"value\": {}}}", COORD[a], COORD[b], COORD[c], json_str(&geo.christoffel[a][b][c].to_mathematica())));
                }
            }
        }
    }
    writeln!(curv, "  \"christoffelNonzero_b_le_c\": [\n{}\n  ],", chr.join(",\n")).unwrap();
    let rm: Vec<String> = entries.iter().map(|(a, b, c, d, v)| format!("    {{\"up\": [\"{}\", \"{}\"], \"down\": [\"{}\", \"{}\"], \"value\": {}}}", COORD[*a], COORD[*b], COORD[*c], COORD[*d], json_str(&v.to_mathematica()))).collect();
    writeln!(curv, "  \"riemannMixedNonzero\": [\n{}\n  ],", rm.join(",\n")).unwrap();
    writeln!(curv, "  \"ricciMixed\": {},", tensor_json(&geo.ricci_mixed, "  ")).unwrap();
    writeln!(curv, "  \"ricciScalar\": {},", json_str(&geo.ricci_scalar.to_mathematica())).unwrap();
    writeln!(curv, "  \"einsteinMixed\": {}", tensor_json(&g_e, "  ")).unwrap();
    curv.push_str("}\n");
    fs::write(out.join("curvature.json"), curv).unwrap();

    let mut lt = String::from("{\n");
    writeln!(lt, "  \"program\": \"lovelock_gkd lovelock\",").unwrap();
    writeln!(lt, "  \"definition\": {},", json_str("A_(k)^{lh} = sqrt(g) g^{jl} kδ[{j,j1,...,j2k},{h,h1,...,h2k}] R^{j1j2}_{h1h2} ... R^{j(2k-1)j2k}_{h(2k-1)h2k}; P_(k)^h_j = kδ[...] R ... R; L_(k) = kδ[{j1..j2k},{h1..h2k}] R ... R; n = 8, m = 4, k = 1, 2, 3")).unwrap();
    writeln!(lt, "  \"normalisationNote\": {},", json_str("The usual normalised Lovelock tensors are E_(k)^h_j = -P_(k)^h_j / 2^(k+1); E_(1) = G (Einstein).")).unwrap();
    for k in 1..=3usize {
        writeln!(lt, "  \"L{}\": {},", k, json_str(&ls[k - 1].to_mathematica())).unwrap();
        writeln!(lt, "  \"P{}_mixed_up_h_down_j\": {},", k, tensor_json(&ps[k - 1], "  ")).unwrap();
        writeln!(lt, "  \"A{}_contravariant_l_h\": {},", k, tensor_json(&as_[k - 1], "  ")).unwrap();
    }
    writeln!(lt, "  \"k4\": \"identically zero (GKD of 9 indices in 8 dimensions)\"").unwrap();
    lt.push_str("}\n");
    fs::write(out.join("lovelock-tensors.json"), lt).unwrap();

    let mut md = String::new();
    writeln!(md, "# Lovelock tensors of the test metric, all components (generated by lovelock_gkd)\n").unwrap();
    writeln!(md, "Metric as given: `{}`\n", METRIC_AS_GIVEN).unwrap();
    writeln!(md, "Curvature convention: MTW. $\\sqrt{{g}} = {}$ (that is, $\\cos(6Hx_8)$ on $0<6Hx_8<\\pi/2$).\n", geo.sqrt_g.to_latex()).unwrap();
    writeln!(md, "Ricci scalar: $R = {}$\n", geo.ricci_scalar.to_latex()).unwrap();
    for k in 1..=3usize {
        writeln!(md, "## k = {}\n", k).unwrap();
        writeln!(md, "Lovelock scalar $L_{{({})}} = {}$\n", k, ls[k - 1].to_latex()).unwrap();
        writeln!(md, "### Mixed $P_{{({})}}{{}}^h{{}}_j$ (all 64 components)\n", k).unwrap();
        md.push_str(&tensor_markdown(&format!("P_{{({})}}", k), &ps[k - 1], true, false));
        writeln!(md, "\n### Contravariant density $A_{{({})}}^{{lh}} = \\sqrt{{g}}\\,g^{{jl}}P_{{({})}}{{}}^h{{}}_j$ (all 64 components)\n", k, k).unwrap();
        md.push_str(&tensor_markdown(&format!("A_{{({})}}", k), &as_[k - 1], true, true));
        md.push('\n');
    }
    fs::write(out.join("lovelock-components.md"), md).unwrap();

    let all_ok = checks.iter().all(|c| c.passed);
    let mut rep = String::from("{\n");
    writeln!(rep, "  \"program\": \"lovelock_gkd lovelock\",").unwrap();
    writeln!(rep, "  \"gkdSelfCheck\": {{\"length3Pair\": {}, \"transposition\": {}}},", GKD(&[0, 1, 2], &[1, 2, 0]), GKD(&[0, 1], &[1, 0])).unwrap();
    writeln!(rep, "  \"counters\": [\n    {}\n  ],", counter_lines.join(",\n    ")).unwrap();
    let cl: Vec<String> = checks.iter().map(|c| format!("    {}: {{\"passed\": {}, \"detail\": {}}}", json_str(&c.name), c.passed, json_str(&c.detail))).collect();
    writeln!(rep, "  \"checks\": {{\n{}\n  }},", cl.join(",\n")).unwrap();
    writeln!(rep, "  \"checkCount\": {},", checks.len()).unwrap();
    writeln!(rep, "  \"failedCheckCount\": {},", checks.iter().filter(|c| !c.passed).count()).unwrap();
    writeln!(rep, "  \"verdict\": {}", json_str(if all_ok { "SUCCESS" } else { "FAILURE" })).unwrap();
    rep.push_str("}\n");
    fs::write(out.join("lovelock-report.json"), rep).unwrap();
    println!("check_count={}", checks.len());
    println!("failed_check_count={}", checks.iter().filter(|c| !c.passed).count());
    println!("lovelock: {} ({:.1} s)", if all_ok { "SUCCESS" } else { "FAILURE" }, t0.elapsed().as_secs_f64());
    if all_ok { 0 } else { 1 }
}
