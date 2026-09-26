//! Agreement check against the exact Wolfram theory file
//! `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json` (written by
//! another Stage-4 verifier).  When the file is absent the comparison is
//! recorded as not run; when it is present the following are compared with
//! this crate's own derivation:
//!
//! * geometry: `G^mu_nu`, `rho_req`, `p_req`, extrinsic curvature, Israel
//!   brane stress, `R = -42 H^2`;
//! * reduction: the theory's explicit (unnormalised Gaussian-integer) basis
//!   is loaded, normalised, checked for unitarity, and the fixture operators
//!   `A0, A1, A4, C, B, BC, gamma^4 gamma^1, J, K1, K2` are transformed with
//!   it: they must be 2x2 block diagonal and every block must equal the form
//!   this crate derived (`blocks::expected_form`) for the labels
//!   `(s, c1) = (J, -Im K1)` MEASURED on that basis.  The theory's own label
//!   letters `(j, s2, s3)` are related to the measured ones and the relation
//!   is recorded (the theory file labels its blocks by `j = -J`);
//! * exchange: filled-shell ratio 1/8, the closed form `-(lambda/32)(n^2+S^2)`,
//!   the kernel and the LDA potentials (string content);
//! * the brane zero-mode splitting `d eps_0/dk` at `k = 0`: the theory's
//!   closed form `c = e^{-a4} (2M/(2M-H)) (1 - e^{-(2M-H)L})/(1 - e^{-2ML})`
//!   against this crate's shooting derivative (5-point stencil).
//!
//! The SHA-256 of the theory file is recorded (own implementation, no
//! dependencies).

use std::fs;
use std::sync::Arc;

use crate::blocks::{expected_form, Operators, C16, N};
use crate::exchange::{exchange_energy_density, gas_chemical_potential, gas_moments};
use crate::jsonread::{parse, Value};
use crate::math::exp;
use crate::output::Json;
use crate::shooting::{Potential, Shooter};
use crate::Tolerances;

pub const THEORY_PATH: &str = "artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json";
pub const EXCHANGE_TABLE_PATH: &str = "artifacts/dirac16complex/kohn-sham/exchange-table.json";

/// One comparison item.
#[derive(Clone, Debug)]
pub struct Item {
    pub name: String,
    pub passed: bool,
    pub detail: String,
}

/// Outcome of the comparison.
#[derive(Clone, Debug, Default)]
pub struct Comparison {
    /// File compared (THEORY_PATH or EXCHANGE_TABLE_PATH).
    pub path: String,
    pub present: bool,
    pub sha256: String,
    pub items: Vec<Item>,
    pub notes: Vec<(String, String)>,
}

impl Comparison {
    fn item(&mut self, name: &str, passed: bool, detail: String) {
        self.items.push(Item {
            name: name.to_string(),
            passed,
            detail,
        });
    }

    pub fn to_json(&self) -> Json {
        let mut pairs = vec![
            ("path", Json::str(&self.path)),
            (
                "status",
                Json::str(if self.present {
                    "compared"
                } else {
                    "not-run (file absent)"
                }),
            ),
            ("sha256", Json::str(&self.sha256)),
        ];
        let checks: Vec<(String, Json)> = self
            .items
            .iter()
            .map(|i| {
                (
                    i.name.clone(),
                    Json::object(vec![
                        ("passed", Json::Bool(i.passed)),
                        ("detail", Json::str(&i.detail)),
                    ]),
                )
            })
            .collect();
        pairs.push(("checks", Json::Object(checks)));
        let notes: Vec<(String, Json)> = self
            .notes
            .iter()
            .map(|(k, v)| (k.clone(), Json::str(v)))
            .collect();
        pairs.push(("notes", Json::Object(notes)));
        Json::object(pairs)
    }
}

/// SHA-256 (FIPS 180-4) of a byte string, lower-case hex.
pub fn sha256_hex(data: &[u8]) -> String {
    const K: [u32; 64] = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4,
        0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe,
        0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f,
        0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
        0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
        0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116,
        0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7,
        0xc67178f2,
    ];
    let mut h: [u32; 8] = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab,
        0x5be0cd19,
    ];
    let mut message = data.to_vec();
    let bit_length = (data.len() as u64).wrapping_mul(8);
    message.push(0x80);
    while message.len() % 64 != 56 {
        message.push(0);
    }
    message.extend_from_slice(&bit_length.to_be_bytes());
    for chunk in message.chunks(64) {
        let mut w = [0u32; 64];
        for (i, word) in w.iter_mut().enumerate().take(16) {
            *word = u32::from_be_bytes([
                chunk[4 * i],
                chunk[4 * i + 1],
                chunk[4 * i + 2],
                chunk[4 * i + 3],
            ]);
        }
        for i in 16..64 {
            let s0 = w[i - 15].rotate_right(7) ^ w[i - 15].rotate_right(18) ^ (w[i - 15] >> 3);
            let s1 = w[i - 2].rotate_right(17) ^ w[i - 2].rotate_right(19) ^ (w[i - 2] >> 10);
            w[i] = w[i - 16]
                .wrapping_add(s0)
                .wrapping_add(w[i - 7])
                .wrapping_add(s1);
        }
        let mut a = h;
        for i in 0..64 {
            let s1 = a[4].rotate_right(6) ^ a[4].rotate_right(11) ^ a[4].rotate_right(25);
            let ch = (a[4] & a[5]) ^ (!a[4] & a[6]);
            let t1 = a[7]
                .wrapping_add(s1)
                .wrapping_add(ch)
                .wrapping_add(K[i])
                .wrapping_add(w[i]);
            let s0 = a[0].rotate_right(2) ^ a[0].rotate_right(13) ^ a[0].rotate_right(22);
            let maj = (a[0] & a[1]) ^ (a[0] & a[2]) ^ (a[1] & a[2]);
            let t2 = s0.wrapping_add(maj);
            a[7] = a[6];
            a[6] = a[5];
            a[5] = a[4];
            a[4] = a[3].wrapping_add(t1);
            a[3] = a[2];
            a[2] = a[1];
            a[1] = a[0];
            a[0] = t1.wrapping_add(t2);
        }
        for i in 0..8 {
            h[i] = h[i].wrapping_add(a[i]);
        }
    }
    h.iter().map(|x| format!("{x:08x}")).collect()
}

fn numbers(value: Option<&Value>) -> Option<Vec<f64>> {
    value?.as_array()?.iter().map(|v| v.as_rational()).collect()
}

fn same_list(a: &[f64], b: &[f64]) -> bool {
    a.len() == b.len() && a.iter().zip(b.iter()).all(|(x, y)| x == y)
}

/// Load and compare; `zero_mode_slope` is this crate's d eps_0/dk at k = 0
/// for (H, M, L, a4) = (1, 1, 3, 0) in the s = +1 block.
pub fn compare(path: &str, tolerances: Tolerances) -> Comparison {
    let mut out = Comparison {
        path: path.to_string(),
        ..Comparison::default()
    };
    let Ok(bytes) = fs::read(path) else {
        out.notes
            .push(("reason".to_string(), format!("{path} absent")));
        return out;
    };
    out.present = true;
    out.sha256 = sha256_hex(&bytes);
    let text = match String::from_utf8(bytes) {
        Ok(t) => t,
        Err(e) => {
            out.item("theory_parse", false, format!("not UTF-8: {e}"));
            return out;
        }
    };
    let doc = match parse(&text) {
        Ok(d) => d,
        Err(e) => {
            out.item("theory_parse", false, e);
            return out;
        }
    };
    out.item("theory_parse", true, "parsed".to_string());
    // geometry
    let einstein = numbers(doc.path(&["geometry", "curvature", "einsteinMixedValues"]));
    out.item(
        "theory_geometry_einstein",
        einstein
            .as_deref()
            .is_some_and(|v| same_list(v, &[15.0, 15.0, 15.0, 15.0, 21.0, 15.0, 15.0, 15.0])),
        format!("{einstein:?} vs (15,15,15,15,21,15,15,15)"),
    );
    let rho = doc
        .path(&["geometry", "requiredSource", "rhoValue"])
        .and_then(|v| v.as_rational());
    let p = doc
        .path(&["geometry", "requiredSource", "pValue"])
        .and_then(|v| v.as_rational());
    out.item(
        "theory_geometry_required_source",
        rho == Some(-21.0) && p == Some(15.0),
        format!("rho_req {rho:?}, p_req {p:?} vs -21, +15"),
    );
    let ricci = doc
        .path(&["geometry", "curvature", "ricciScalar"])
        .and_then(|v| v.as_str())
        .unwrap_or("");
    out.item(
        "theory_geometry_ricci_scalar",
        ricci.contains("-42"),
        format!("'{ricci}'"),
    );
    let extrinsic = numbers(doc.path(&["geometry", "extrinsicCurvature", "values"]));
    out.item(
        "theory_geometry_extrinsic",
        extrinsic
            .as_deref()
            .is_some_and(|v| same_list(v, &[1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0])),
        format!("{extrinsic:?} vs (1,1,1,0,1,1,1) H"),
    );
    let brane = numbers(doc.path(&["geometry", "extensions", "E2_Z2mirror", "braneStressValues"]));
    out.item(
        "theory_geometry_brane_stress",
        brane
            .as_deref()
            .is_some_and(|v| same_list(v, &[-10.0, -10.0, -10.0, -12.0, -10.0, -10.0, -10.0])),
        format!("{brane:?} vs -(10,10,10,12,10,10,10) H/kappa"),
    );
    // reduction: their basis on our operators
    let ops = Operators::new();
    let basis_rows = doc
        .path(&[
            "reduction",
            "blockDiagonalisation",
            "basisMatrixUnnormalised",
        ])
        .and_then(|v| v.as_array());
    let norm2 = doc
        .path(&["reduction", "blockDiagonalisation", "columnNormSquared"])
        .and_then(|v| v.as_rational())
        .unwrap_or(8.0);
    let mut label_relation = String::new();
    match basis_rows {
        Some(rows) if rows.len() == N => {
            let mut u = C16::zero();
            let mut ok = true;
            for (i, row) in rows.iter().enumerate() {
                match row.as_array() {
                    Some(entries) if entries.len() == N => {
                        for (j, entry) in entries.iter().enumerate() {
                            let pair = entry.as_array();
                            let re = pair.and_then(|p| p.first()).and_then(|v| v.as_rational());
                            let im = pair.and_then(|p| p.get(1)).and_then(|v| v.as_rational());
                            match (re, im) {
                                (Some(re), Some(im)) => {
                                    u.re[i][j] = re / norm2.sqrt();
                                    u.im[i][j] = im / norm2.sqrt();
                                }
                                _ => ok = false,
                            }
                        }
                    }
                    _ => ok = false,
                }
            }
            out.item(
                "theory_basis_read",
                ok,
                format!("16x16 basis, column norm^2 {norm2}"),
            );
            if ok {
                let gram = u.dagger().mul(&u).sub(&C16::identity()).max_abs();
                out.item(
                    "theory_basis_unitary",
                    gram < 1e-14,
                    format!("max |U^dagger U - 1| = {gram:e}"),
                );
                let operators: [(&str, &C16); 10] = [
                    ("A0", &ops.a0),
                    ("A1", &ops.a1),
                    ("A4", &ops.a4),
                    ("gamma4", &ops.gamma4),
                    ("C", &ops.c),
                    ("B", &ops.b),
                    ("BC", &ops.bc),
                    ("gamma4gamma1", &ops.g4g1),
                    ("BCgamma0", &ops.bcg0),
                    ("J", &ops.j),
                ];
                let mut off: f64 = 0.0;
                let mut transformed = Vec::new();
                for (name, op) in operators.iter() {
                    let y = u.dagger().mul(op).mul(&u);
                    for i in 0..N {
                        for j in 0..N {
                            if i / 2 != j / 2 {
                                off = off.max(
                                    (y.re[i][j] * y.re[i][j] + y.im[i][j] * y.im[i][j]).sqrt(),
                                );
                            }
                        }
                    }
                    transformed.push((*name, y));
                }
                let yk1 = u.dagger().mul(&ops.k1).mul(&u);
                let yk2 = u.dagger().mul(&ops.k2).mul(&u);
                for y in [&yk1, &yk2] {
                    for i in 0..N {
                        for j in 0..N {
                            if i / 2 != j / 2 {
                                off = off.max(
                                    (y.re[i][j] * y.re[i][j] + y.im[i][j] * y.im[i][j]).sqrt(),
                                );
                            }
                        }
                    }
                }
                out.item("theory_basis_block_diagonalises", off < 1e-14, format!("max off-block entry {off:e} over A0, A1, A4, gamma4, C, B, BC, gamma4gamma1, BCgamma0, J, K1, K2"));
                // measured labels and forms
                let yj = &transformed[9].1;
                let mut form_defect: f64 = 0.0;
                let mut relation_counts = [0i32; 4];
                for b in 0..8 {
                    let s = yj.re[2 * b][2 * b];
                    let c1 = -yk1.im[2 * b][2 * b];
                    let c2 = -yk2.im[2 * b][2 * b];
                    form_defect = form_defect
                        .max((s.abs() - 1.0).abs())
                        .max((c1.abs() - 1.0).abs());
                    for (name, y) in transformed.iter().take(9) {
                        let expected = expected_form(name, s, c1);
                        for pq in 0..4 {
                            let (pp, qq) = (pq / 2, pq % 2);
                            let dr = y.re[2 * b + pp][2 * b + qq] - expected.re[pp][qq];
                            let di = y.im[2 * b + pp][2 * b + qq] - expected.im[pp][qq];
                            form_defect = form_defect.max((dr * dr + di * di).sqrt());
                        }
                    }
                    // theory labels
                    let their = |key: &str| {
                        doc.path(&[
                            "reduction",
                            "blockDiagonalisation",
                            "blocks",
                            &b.to_string(),
                            key,
                        ])
                        .and_then(|v| v.as_rational())
                        .unwrap_or(f64::NAN)
                    };
                    let (j, s2, s3) = (their("j"), their("s2"), their("s3"));
                    if j == -s {
                        relation_counts[0] += 1;
                    }
                    if j == s {
                        relation_counts[1] += 1;
                    }
                    if s2 == c1 {
                        relation_counts[2] += 1;
                    }
                    if s3 == c2 {
                        relation_counts[3] += 1;
                    }
                }
                out.item(
                    "theory_basis_reproduces_our_block_forms",
                    form_defect < 1e-14,
                    format!("max |block - expected_form(J_measured, -Im K1_measured)| = {form_defect:e}"),
                );
                label_relation = format!(
                    "blocks with theory j = -J_measured: {}, j = +J_measured: {}; s2 = -Im(K1) (our c1): {}; s3 = -Im(K2) (our c2): {}",
                    relation_counts[0], relation_counts[1], relation_counts[2], relation_counts[3]
                );
            }
        }
        _ => out.item(
            "theory_basis_read",
            false,
            "basisMatrixUnnormalised missing or not 16 rows".to_string(),
        ),
    }
    if !label_relation.is_empty() {
        out.notes
            .push(("labelRelation".to_string(), label_relation));
    }
    // exchange
    let ratio = doc
        .path(&["exchange", "filledShell", "ratio"])
        .and_then(|v| v.as_rational());
    out.item(
        "theory_exchange_filled_shell",
        ratio == Some(0.125),
        format!("{ratio:?} vs 1/8"),
    );
    let closed = doc
        .path(&["exchange", "uniformGas", "closedFormTex"])
        .and_then(|v| v.as_str())
        .unwrap_or("");
    out.item(
        "theory_exchange_closed_form",
        closed.contains("\\frac{\\lambda}{32}") && closed.contains("n^2+S^2"),
        format!("'{closed}' vs e_x = -(lambda/32)(n^2 + S^2)"),
    );
    let kernel = doc
        .path(&["exchange", "kernel", "plusPlus"])
        .and_then(|v| v.as_str())
        .unwrap_or("");
    out.item(
        "theory_exchange_kernel",
        kernel.replace(' ', "").contains("4[1+(m^2-p.q)/(E_pE_q)]"),
        format!("'{kernel}' vs 4[1 + (m^2 - p.q)/(E_p E_q)]"),
    );
    let vv = doc
        .path(&["exchange", "uniformGas", "ldaPotentials", "v_v"])
        .and_then(|v| v.as_str())
        .unwrap_or("");
    let vs = doc
        .path(&["exchange", "uniformGas", "ldaPotentials", "v_s"])
        .and_then(|v| v.as_str())
        .unwrap_or("");
    out.item(
        "theory_exchange_lda_potentials",
        vv.replace(' ', "").contains("-(lambda/16)n")
            && vs.replace(' ', "").contains("-(lambda/16)S"),
        format!("'{vv}'; '{vs}'"),
    );
    // zero-mode splitting: their closed form vs our shooting derivative (M = 1, L = 3, a4 = 0, H = 1)
    let (h, m, length) = (1.0, 1.0, 3.0);
    let c_theory = (2.0 * m / (2.0 * m - h)) * (1.0 - exp(-(2.0 * m - h) * length))
        / (1.0 - exp(-2.0 * m * length));
    let mut shooter = Shooter::new(
        Arc::new(Potential::free(h, 0.0, length, m, 301)),
        tolerances,
    );
    let dk = 1e-3;
    let mut eps = Vec::new();
    let mut failed = false;
    for f in [-2.0, -1.0, 1.0, 2.0] {
        match shooter.find_level(f * dk, 1, 0, 0.0, 1e-3) {
            Ok((e, _)) => eps.push(e),
            Err(_) => failed = true,
        }
    }
    if failed || eps.len() != 4 {
        out.item(
            "theory_zero_mode_splitting",
            false,
            "shooting failed".to_string(),
        );
    } else {
        let slope = (eps[0] - 8.0 * eps[1] + 8.0 * eps[2] - eps[3]) / (12.0 * dk);
        out.item(
            "theory_zero_mode_splitting",
            (slope.abs() - c_theory).abs() < 1e-6,
            format!("our d eps_0/dk (s = +1) = {slope} vs theory c = {c_theory} (theory: +c k for its j = +1, i.e. our s = -1)"),
        );
    }
    out
}

/// Relative tolerance of the closed form against the tabulated quadrature.
pub const TABLE_CLOSED_FORM_TOLERANCE: f64 = 1.0e-10;
/// Rows of the 3-space table recomputed with this crate's own gas
/// quadrature: T >= this (units of m).  The fixed 400-node Gauss-Legendre
/// rule of `exchange::gas_moments` does not resolve the Fermi edge at lower
/// T; those rows are measured and reported, not checked.
pub const TABLE_OWN_GAS_MIN_T: f64 = 0.3;
/// Relative tolerance on S(n, T) and absolute tolerance (in units of
/// T + |mu|) on mu(n, T) for the recomputed 3-space rows.
pub const TABLE_OWN_GAS_TOLERANCE: f64 = 1.0e-7;

/// Cross-check against the optional uniform-gas exchange table
/// `exchange-table.json` (written by the independent sympy checker of this
/// stage).  STAGE4_SPEC E4.7: the exchange is exactly local and this crate
/// uses the closed form `e_x = -(lambda/32)(n^2 + S^2)` (exchange.rs,
/// verified by its own quadrature); the table is used ONLY as a cross-check:
///
/// * every row of the tables `d3` (momentum in 3-space) and `d4` (momentum
///   in y and 3-space): the tabulated double-quadrature value
///   `exOverLambda_quadrature` against [`exchange_energy_density`]`(1, n, S)`
///   at the tabulated (n, S), relative [`TABLE_CLOSED_FORM_TOLERANCE`];
/// * the rows of `d3` (the gas of `exchange::gas_moments`) with
///   T >= [`TABLE_OWN_GAS_MIN_T`]: S(n, T) and mu(n, T) recomputed with this
///   crate's quadrature (bisection for mu, 400 Gauss-Legendre nodes on
///   [0, 60 m]).
pub fn exchange_table_check(path: &str) -> Comparison {
    let mut out = Comparison {
        path: path.to_string(),
        ..Comparison::default()
    };
    let Ok(bytes) = fs::read(path) else {
        out.notes
            .push(("reason".to_string(), format!("{path} absent")));
        return out;
    };
    out.present = true;
    out.sha256 = sha256_hex(&bytes);
    let doc = match String::from_utf8(bytes)
        .map_err(|e| format!("not UTF-8: {e}"))
        .and_then(|text| parse(&text))
    {
        Ok(d) => d,
        Err(e) => {
            out.item("exchange_table_parse", false, e);
            return out;
        }
    };
    out.item("exchange_table_parse", true, "parsed".to_string());
    let number = |row: &Value, key: &str| row.get(key).and_then(|v| v.as_rational());
    for table in ["d3", "d4"] {
        let rows = doc
            .path(&["tables", table, "rows"])
            .and_then(|v| v.as_array())
            .cloned()
            .unwrap_or_default();
        let mut worst: f64 = 0.0;
        let mut unreadable = 0usize;
        for row in &rows {
            match (
                number(row, "n"),
                number(row, "S"),
                number(row, "exOverLambda_quadrature"),
            ) {
                (Some(n), Some(s), Some(quadrature)) => {
                    let closed = exchange_energy_density(1.0, n, s);
                    let scale = closed.abs().max(quadrature.abs()).max(1e-300);
                    worst = worst.max((closed - quadrature).abs() / scale);
                }
                _ => unreadable += 1,
            }
        }
        out.item(
            &format!("exchange_table_{table}_closed_form"),
            !rows.is_empty() && unreadable == 0 && worst < TABLE_CLOSED_FORM_TOLERANCE,
            format!(
                "{} rows ({unreadable} unreadable): max relative |-(n^2+S^2)/32 - e_x/lambda (table quadrature)| = {worst:e}",
                rows.len()
            ),
        );
    }
    // own 3-space gas quadrature against the d3 rows
    let rows = doc
        .path(&["tables", "d3", "rows"])
        .and_then(|v| v.as_array())
        .cloned()
        .unwrap_or_default();
    let (mut worst_s, mut worst_mu, mut checked) = (0.0f64, 0.0f64, 0usize);
    let (mut low_s, mut low_mu, mut low_rows) = (0.0f64, 0.0f64, 0usize);
    for row in &rows {
        let (Some(n), Some(t), Some(s), Some(mu)) = (
            number(row, "n"),
            number(row, "T"),
            number(row, "S"),
            number(row, "mu"),
        ) else {
            continue;
        };
        if t <= 0.0 {
            continue;
        }
        let own_mu = gas_chemical_potential(1.0, n, t, 60.0, 400);
        let own = gas_moments(1.0, own_mu, t, 60.0, 400);
        let ds = (own.s - s).abs() / s.abs().max(1e-300);
        let dmu = (own_mu - mu).abs() / (t + mu.abs());
        if t >= TABLE_OWN_GAS_MIN_T {
            worst_s = worst_s.max(ds);
            worst_mu = worst_mu.max(dmu);
            checked += 1;
        } else {
            low_s = low_s.max(ds);
            low_mu = low_mu.max(dmu);
            low_rows += 1;
        }
    }
    out.item(
        "exchange_table_d3_own_gas_quadrature",
        checked > 0 && worst_s < TABLE_OWN_GAS_TOLERANCE && worst_mu < TABLE_OWN_GAS_TOLERANCE,
        format!(
            "{checked} rows with T >= {TABLE_OWN_GAS_MIN_T} m: max relative |S_own - S_table| = {worst_s:e}, max |mu_own - mu_table|/(T + |mu|) = {worst_mu:e}; measured only ({low_rows} rows with 0 < T < {TABLE_OWN_GAS_MIN_T} m, Fermi edge unresolved by the fixed rule): {low_s:e}, {low_mu:e}"
        ),
    );
    out.notes.push((
        "use".to_string(),
        "cross-check only: the Kohn-Sham potentials use the exact closed form e_x = -(lambda/32)(n^2 + S^2), v_s = -(lambda/16) S, v_v = -(lambda/16) n (STAGE4_SPEC E4.7)".to_string(),
    ));
    out
}

/// Note about the optional exchange table (summary.json of `spectrum`).
pub fn exchange_table_note(check: &Comparison) -> Json {
    let status = if !check.present {
        "absent; the crate uses its own exact closed form -(lambda/32)(n^2+S^2), verified by its own quadrature (exchange.rs)"
    } else if check.items.iter().all(|i| i.passed) {
        "present; used as a cross-check only (exchange-table-check.json: all items passed); the Kohn-Sham potentials use the exact closed form"
    } else {
        "present; used as a cross-check only (exchange-table-check.json: at least one item FAILED); the Kohn-Sham potentials use the exact closed form"
    };
    Json::object(vec![
        ("path", Json::str(EXCHANGE_TABLE_PATH)),
        ("status", Json::str(status)),
        ("sha256", Json::str(&check.sha256)),
    ])
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn exchange_table_cross_check_passes_when_present() {
        // the table is written by another verifier; absent -> nothing to check
        let check = exchange_table_check(&format!("../../{EXCHANGE_TABLE_PATH}"));
        if !check.present {
            return;
        }
        assert!(check.items.len() >= 4);
        for item in &check.items {
            println!("{}: {}", item.name, item.detail);
            assert!(item.passed, "{}: {}", item.name, item.detail);
        }
    }

    #[test]
    fn sha256_known_answers() {
        assert_eq!(
            sha256_hex(b""),
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        );
        assert_eq!(
            sha256_hex(b"abc"),
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
        );
    }
}
