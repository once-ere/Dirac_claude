//! Theory inputs of the solver and their numerical cross-check.
//!
//! Reads `Revision/kohn_sham/ks-theory.json` (the exact block basis, the
//! Kohn-Sham coefficients, the brane-band slope) and the gamma fixture
//! `Revision/algebra/gammas.json`, and verifies in floating point (independent
//! of the Wolfram and sympy code that produced them) that in the exported basis
//! V the 16-component instantaneous Hamiltonian
//!     h = i g4 g8 d_y - kappa k g4 g1 + M (-i g4) + v
//! is block diagonal with the 2 x 2 blocks
//!     h_j = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v,
//! and that the density matrices used by the solver have the stated block
//! forms (n: B B = 1, S: B C = j sigma2, Q: B g8 -> sigma3 via B B g8 = g8,
//! current: -i B C g1 = j sigma3).  g1 = gamma^(x1), g4 = gamma^(x4),
//! g8 = gamma^(x8) in the author's coordinates.

use crate::json::{obj, parse, Json};
use crate::report::Report;

#[derive(Clone, Copy, Debug, PartialEq)]
pub struct C {
    pub re: f64,
    pub im: f64,
}

impl C {
    pub const ZERO: C = C { re: 0.0, im: 0.0 };
    pub fn new(re: f64, im: f64) -> C {
        C { re, im }
    }
    pub fn mul(self, o: C) -> C {
        C::new(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    }
    pub fn add(self, o: C) -> C {
        C::new(self.re + o.re, self.im + o.im)
    }
    pub fn sub(self, o: C) -> C {
        C::new(self.re - o.re, self.im - o.im)
    }
    pub fn conj(self) -> C {
        C::new(self.re, -self.im)
    }
    pub fn scale(self, s: f64) -> C {
        C::new(self.re * s, self.im * s)
    }
    pub fn abs(self) -> f64 {
        self.re.hypot(self.im)
    }
}

/// Dense complex matrix, row major.
#[derive(Clone, Debug)]
pub struct M {
    pub r: usize,
    pub c: usize,
    pub a: Vec<C>,
}

impl M {
    pub fn zeros(r: usize, c: usize) -> M {
        M { r, c, a: vec![C::ZERO; r * c] }
    }
    pub fn eye(n: usize) -> M {
        let mut m = M::zeros(n, n);
        for i in 0..n {
            m.a[i * n + i] = C::new(1.0, 0.0);
        }
        m
    }
    pub fn at(&self, i: usize, j: usize) -> C {
        self.a[i * self.c + j]
    }
    pub fn set(&mut self, i: usize, j: usize, x: C) {
        self.a[i * self.c + j] = x;
    }
    pub fn mul(&self, o: &M) -> M {
        assert_eq!(self.c, o.r);
        let mut m = M::zeros(self.r, o.c);
        for i in 0..self.r {
            for k in 0..self.c {
                let x = self.at(i, k);
                if x == C::ZERO {
                    continue;
                }
                for j in 0..o.c {
                    let y = m.at(i, j).add(x.mul(o.at(k, j)));
                    m.set(i, j, y);
                }
            }
        }
        m
    }
    pub fn adj(&self) -> M {
        let mut m = M::zeros(self.c, self.r);
        for i in 0..self.r {
            for j in 0..self.c {
                m.set(j, i, self.at(i, j).conj());
            }
        }
        m
    }
    pub fn scale(&self, s: C) -> M {
        M { r: self.r, c: self.c, a: self.a.iter().map(|x| x.mul(s)).collect() }
    }
    pub fn add(&self, o: &M) -> M {
        M { r: self.r, c: self.c, a: self.a.iter().zip(&o.a).map(|(x, y)| x.add(*y)).collect() }
    }
    pub fn sub(&self, o: &M) -> M {
        M { r: self.r, c: self.c, a: self.a.iter().zip(&o.a).map(|(x, y)| x.sub(*y)).collect() }
    }
    pub fn max_abs(&self) -> f64 {
        self.a.iter().fold(0.0, |m, x| m.max(x.abs()))
    }
}

/// Pauli matrices: 0 = identity, 1, 2, 3.
pub fn pauli(k: usize) -> M {
    let mut m = M::zeros(2, 2);
    match k {
        0 => {
            m.set(0, 0, C::new(1.0, 0.0));
            m.set(1, 1, C::new(1.0, 0.0));
        }
        1 => {
            m.set(0, 1, C::new(1.0, 0.0));
            m.set(1, 0, C::new(1.0, 0.0));
        }
        2 => {
            m.set(0, 1, C::new(0.0, -1.0));
            m.set(1, 0, C::new(0.0, 1.0));
        }
        _ => {
            m.set(0, 0, C::new(1.0, 0.0));
            m.set(1, 1, C::new(-1.0, 0.0));
        }
    }
    m
}

/// Parse an exact entry: integer, "p/q", or the strings "0", "1", "-1", "I", "-I".
fn entry(j: &Json) -> Result<C, String> {
    if let Some(x) = j.as_f64() {
        return Ok(C::new(x, 0.0));
    }
    let s = j.as_str().ok_or("matrix entry is neither number nor string")?.trim();
    let c = match s {
        "0" => C::new(0.0, 0.0),
        "1" => C::new(1.0, 0.0),
        "-1" => C::new(-1.0, 0.0),
        "I" => C::new(0.0, 1.0),
        "-I" => C::new(0.0, -1.0),
        _ => {
            if let Some((p, q)) = s.split_once('/') {
                let p: f64 = p.trim().parse().map_err(|_| format!("bad rational {}", s))?;
                let q: f64 = q.trim().parse().map_err(|_| format!("bad rational {}", s))?;
                C::new(p / q, 0.0)
            } else {
                return Err(format!("unsupported matrix entry {}", s));
            }
        }
    };
    Ok(c)
}

fn real_matrix(j: &Json) -> Result<M, String> {
    let rows = j.as_arr().ok_or("matrix is not an array")?;
    let n = rows.len();
    let mut m = M::zeros(n, n);
    for (i, r) in rows.iter().enumerate() {
        let r = r.as_arr().ok_or("row is not an array")?;
        if r.len() != n {
            return Err("matrix not square".into());
        }
        for (k, x) in r.iter().enumerate() {
            m.set(i, k, entry(x)?);
        }
    }
    Ok(m)
}

fn complex_matrix(j: &Json) -> Result<M, String> {
    if let (Some(re), Some(im)) = (j.get("re"), j.get("im")) {
        let a = real_matrix(re)?;
        let b = real_matrix(im)?;
        Ok(M { r: a.r, c: a.c, a: a.a.iter().zip(&b.a).map(|(x, y)| C::new(x.re, y.re)).collect() })
    } else {
        real_matrix(j)
    }
}

fn rational(s: &str) -> Result<f64, String> {
    let s = s.trim();
    if let Some((p, q)) = s.split_once('/') {
        let p: f64 = p.trim().parse().map_err(|_| format!("bad rational {}", s))?;
        let q: f64 = q.trim().parse().map_err(|_| format!("bad rational {}", s))?;
        Ok(p / q)
    } else {
        s.parse().map_err(|_| format!("bad number {}", s))
    }
}

/// The numbers the solver takes from the theory file.
#[derive(Clone, Debug)]
pub struct TheoryInputs {
    pub meff_coeff: f64,     // 15/16
    pub vv_coeff: f64,       // -1/16
    pub ex_n2: f64,          // -1/32
    pub ex_s2: f64,          // -1/32
    pub slope_m1h1l3: f64,   // brane-band slope c at M = H = 1, L = 3, a4 = 0
    pub sha_theory: String,
    pub sha_gammas: String,
    /// ks-theory.json adiabaticity.history and its status label (PRESCRIBED BACKGROUND)
    pub history: String,
    pub history_status: String,
}

pub fn read_and_check(root: &std::path::Path, rep: &mut Report) -> Result<TheoryInputs, String> {
    let tpath = root.join("Revision/kohn_sham/ks-theory.json");
    let gpath = root.join("Revision/algebra/gammas.json");
    let tbytes = std::fs::read(&tpath).map_err(|e| format!("{}: {}", tpath.display(), e))?;
    let gbytes = std::fs::read(&gpath).map_err(|e| format!("{}: {}", gpath.display(), e))?;
    let sha_t = crate::sha256::hex(&tbytes);
    let sha_g = crate::sha256::hex(&gbytes);
    let th = parse(std::str::from_utf8(&tbytes).map_err(|e| e.to_string())?)?;
    let ga = parse(std::str::from_utf8(&gbytes).map_err(|e| e.to_string())?)?;

    // --- coefficients ---------------------------------------------------
    let kp = th.path(&["exchange", "kohnShamPotentials"]).ok_or("kohnShamPotentials missing")?;
    let meff = rational(kp.get("Meff_coefficient_of_lambda_S").and_then(|x| x.as_str()).ok_or("Meff coeff")?)?;
    let vv = rational(kp.get("vv_coefficient_of_lambda_n").and_then(|x| x.as_str()).ok_or("vv coeff")?)?;
    let ug = th.path(&["exchange", "uniformGas"]).ok_or("uniformGas missing")?;
    let exn = rational(ug.get("coefficient_n2").and_then(|x| x.as_str()).ok_or("n2 coeff")?)?;
    let exs = rational(ug.get("coefficient_S2").and_then(|x| x.as_str()).ok_or("S2 coeff")?)?;
    let slope: f64 = th
        .path(&["checksNumeric", "braneBandSlope_M1_H1_L3_a0"])
        .and_then(|x| x.as_str())
        .ok_or("slope missing")?
        .parse()
        .map_err(|_| "slope parse")?;
    // the history a4 = A H x4 and its label: a PRESCRIBED BACKGROUND, not a solution of the a4 equations
    let history = th.path(&["adiabaticity", "history"]).and_then(|x| x.as_str()).ok_or("adiabaticity.history missing")?.to_string();
    let history_status = th
        .path(&["adiabaticity", "historyStatus"])
        .and_then(|x| x.as_str())
        .ok_or("adiabaticity.historyStatus missing (the PRESCRIBED BACKGROUND label of the history)")?
        .to_string();
    if !history_status.starts_with("PRESCRIBED BACKGROUND") || !history.contains("PRESCRIBED BACKGROUND") {
        return Err("ks-theory.json: the history a4 = A H x4 is not labelled as a PRESCRIBED BACKGROUND".into());
    }
    // e_int = e_H + e_x = (1/2) S^2 + ex_s2 S^2 + ex_n2 n^2 (per lambda); M_eff - m = d e/dS, v = d e/dn
    let ok_coeff = (meff - 15.0 / 16.0).abs() < 1e-15
        && (vv + 1.0 / 16.0).abs() < 1e-15
        && (exn + 1.0 / 32.0).abs() < 1e-15
        && (exs + 1.0 / 32.0).abs() < 1e-15
        && ((1.0 + 2.0 * exs) - meff).abs() < 1e-15
        && (2.0 * exn - vv).abs() < 1e-15;
    rep.check(
        "theory_input_coefficients",
        ok_coeff,
        format!(
            "ks-theory.json (sha256 {}): M_eff = m + {} lambda S, v_v = {} lambda n, e_x = ({} n^2 + {} S^2) lambda; consistent: M_eff - m = d e_int/dS with e_int = (1/2 + {}) lambda S^2 + {} lambda n^2, v_v = d e_int/dn",
            &sha_t[..16], meff, vv, exn, exs, exs, exn
        ),
    );

    // --- gammas -------------------------------------------------------------
    let gl = ga.get("gamma").and_then(|x| x.as_arr()).ok_or("gamma missing")?;
    if gl.len() != 8 {
        return Err("expected 8 gammas".into());
    }
    let mut g: Vec<M> = Vec::new();
    for x in gl {
        g.push(real_matrix(x)?);
    }
    let eta = [1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0];
    let mut cliff = 0.0f64;
    for a in 0..8 {
        for b in 0..8 {
            let ac = g[a].mul(&g[b]).add(&g[b].mul(&g[a]));
            let target = if a == b { M::eye(16).scale(C::new(2.0 * eta[a], 0.0)) } else { M::zeros(16, 16) };
            cliff = cliff.max(ac.sub(&target).max_abs());
        }
    }
    let cmat = real_matrix(ga.get("C").ok_or("C missing")?)?;
    let bmat = complex_matrix(ga.get("B").ok_or("B missing")?)?;
    let (g1, g4, g8) = (&g[0], &g[3], &g[7]);
    let c_def = g8.mul(&g[0]).mul(&g[1]).mul(&g[2]);
    let b_def = cmat.mul(g4).scale(C::new(0.0, -1.0));
    let fix_dev = c_def.sub(&cmat).max_abs().max(b_def.sub(&bmat).max_abs());
    rep.check(
        "gamma_fixture_numeric",
        cliff == 0.0 && fix_dev == 0.0,
        format!(
            "gammas.json (sha256 {}): {{gamma^a, gamma^b}} = 2 eta^ab exactly in floating point (max deviation {:e}), C = g8 g1 g2 g3 and B = -i C g4 reproduced (max deviation {:e})",
            &sha_g[..16], cliff, fix_dev
        ),
    );

    // --- block basis ------------------------------------------------------------
    let bb = th.get("blockBasis").ok_or("blockBasis missing")?;
    let rows = bb.get("unnormalisedColumns2Sqrt2V").and_then(|x| x.as_arr()).ok_or("basis missing")?;
    let mut v = M::zeros(16, 16);
    let norm = 1.0 / (2.0 * 2f64.sqrt());
    for (i, r) in rows.iter().enumerate() {
        let r = r.as_arr().ok_or("basis row")?;
        for (k, x) in r.iter().enumerate() {
            v.set(i, k, entry(x)?.scale(norm));
        }
    }
    let labels: Vec<(f64, f64, f64)> = bb
        .get("labels")
        .and_then(|x| x.as_arr())
        .ok_or("labels")?
        .iter()
        .map(|l| {
            let l = l.as_arr().unwrap();
            let f = |i: usize| rational(l[i].as_str().unwrap()).unwrap();
            (f(0), f(1), f(2))
        })
        .collect();
    let unit = v.adj().mul(&v).sub(&M::eye(16)).max_abs();
    let i_ = C::new(0.0, 1.0);
    let mi = C::new(0.0, -1.0);
    // operators of the instantaneous Hamiltonian and of the densities
    let ops: Vec<(&str, M)> = vec![
        ("i g4 g8 (d_y term)", g4.mul(g8).scale(i_)),
        ("-i g4 (mass term)", g4.scale(mi)),
        ("-g4 g1 (momentum term)", g4.mul(g1).scale(C::new(-1.0, 0.0))),
        ("B B (number density n)", bmat.mul(&bmat)),
        ("B C (scalar density S)", bmat.mul(&cmat)),
        ("B B g8 (Q = <Psi^dag B g8 Psi>)", bmat.mul(&bmat).mul(g8)),
        ("-i B C g1 (current t)", bmat.mul(&cmat).mul(g1).scale(mi)),
        ("g8", g8.clone()),
        ("B", bmat.clone()),
    ];
    let mut off = 0.0f64;
    let mut formdev = 0.0f64;
    for (name, op) in &ops {
        let w = v.adj().mul(op).mul(&v);
        for bi in 0..8 {
            for bj in 0..8 {
                let blk = {
                    let mut m = M::zeros(2, 2);
                    for p in 0..2 {
                        for q in 0..2 {
                            m.set(p, q, w.at(2 * bi + p, 2 * bj + q));
                        }
                    }
                    m
                };
                if bi != bj {
                    off = off.max(blk.max_abs());
                    continue;
                }
                let (j, s2, _s3) = labels[bi];
                let expect = match *name {
                    "i g4 g8 (d_y term)" => pauli(1).scale(C::new(0.0, -j)),
                    "-i g4 (mass term)" => pauli(2).scale(C::new(j, 0.0)),
                    "-g4 g1 (momentum term)" => pauli(3).scale(C::new(j, 0.0)),
                    "B B (number density n)" => pauli(0),
                    "B C (scalar density S)" => pauli(2).scale(C::new(j, 0.0)),
                    "B B g8 (Q = <Psi^dag B g8 Psi>)" => pauli(3),
                    "-i B C g1 (current t)" => pauli(3).scale(C::new(j, 0.0)),
                    "g8" => pauli(3),
                    _ => pauli(0).scale(C::new(j * s2, 0.0)),
                };
                formdev = formdev.max(blk.sub(&expect).max_abs());
            }
        }
    }
    rep.check(
        "block_reduction_numeric",
        unit < 1e-14 && off < 1e-14 && formdev < 1e-14,
        format!(
            "basis V of ks-theory.json (rows = spinor components): |V^dag V - 1| = {:.1e}; off-block entries of V^dag X V {:.1e}; diagonal blocks equal the solver's forms (i g4 g8 -> -i j sigma1, -i g4 -> j sigma2, -g4 g1 -> j sigma3, B B -> 1, B C -> j sigma2, B B g8 -> sigma3, -i B C g1 -> j sigma3, g8 -> sigma3, B -> j s2) to {:.1e}: the 2x2 equation h_j = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v integrated by the solver is the 16-component Hamiltonian",
            unit, off, formdev
        ),
    );

    Ok(TheoryInputs {
        meff_coeff: meff,
        vv_coeff: vv,
        ex_n2: exn,
        ex_s2: exs,
        slope_m1h1l3: slope,
        sha_theory: sha_t,
        sha_gammas: sha_g,
        history,
        history_status,
    })
}

pub fn inputs_json(t: &TheoryInputs) -> Json {
    obj(vec![
        ("ksTheorySha256", t.sha_theory.clone().into()),
        ("gammasSha256", t.sha_gammas.clone().into()),
        ("MeffCoefficientOfLambdaS", t.meff_coeff.into()),
        ("vvCoefficientOfLambdaN", t.vv_coeff.into()),
        ("exchangeCoefficientN2", t.ex_n2.into()),
        ("exchangeCoefficientS2", t.ex_s2.into()),
        ("braneBandSlopeTheory_M1_H1_L3", t.slope_m1h1l3.into()),
        ("adiabaticityHistory", t.history.clone().into()),
    ])
}
