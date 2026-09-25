//! Numerically exact 2x2 block reduction of the reduced Dirac operator.
//!
//! The Kohn-Sham equation of STAGE4_SPEC section 2 for the ansatz
//! `Psi = e^{-i eps x4} e^{i k x1} W^{-3} chi(y)` is
//!
//! ```text
//! chi' = [ M(y) A0 - i kappa(y) k A1 + i eps A4 ] chi,
//! A0 = gamma^0,  A1 = gamma^0 gamma^1,  A4 = gamma^0 gamma^4.
//! ```
//!
//! `A0, A1, A4` generate Cl(2,1) (A0^2 = A4^2 = 1, A1^2 = -1, pairwise
//! anticommuting); its centre contains `J = A0 A1 A4` (real symmetric,
//! J^2 = 1, traceless).  `K1 = gamma^2 gamma^3` and `K2 = gamma^5 gamma^6`
//! (real antisymmetric, squares -1) commute with A0, A1, A4, C and B.  The
//! joint eigenspaces of (J, iK1, iK2) are the eight 2x2 blocks; inside each
//! block the first basis vector is the gamma^0 = +1 eigenvector `v` (range of
//! the rank-1 projector `P = (1+sJ)(1+c1 iK1)(1+c2 iK2)(1+A0)/16`) and the
//! second is `w = A1 v`.  This module builds that basis in floating point
//! from the fixture constants of `generated.rs`, checks it against the exact
//! Gaussian-integer basis the generator wrote (same construction, exact
//! arithmetic), and verifies the block forms
//!
//! ```text
//! A0 -> sigma_z,   A1 -> [[0,-1],[1,0]] = -i sigma_y,   A4 -> -s sigma_x,
//! gamma^4 -> -i s sigma_y,  C -> -c1 sigma_y,  B -> c1 s I,  BC -> -s sigma_y,
//! gamma^4 gamma^1 -> s sigma_z,  BC gamma^0 -> -i s sigma_x
//! ```
//!
//! to 1e-14, together with the Clifford identities of the blocks.  Hence,
//! with `chi = (a, i b)` (a, b real) in the block of type `s`, the reduced
//! equation is the REAL system
//!
//! ```text
//! a' =  M a + (s eps - kappa k) b,
//! b' = -(s eps + kappa k) a - M b,
//! ```
//!
//! and the bilinears of the expectation-value rule `<Psi^dagger X Psi> =
//! chi^dagger B X chi` are: number density `chi^dagger chi = a^2 + b^2`,
//! scalar density `chi^dagger (BC) chi = -2 s a b`, 3-space pressure
//! bilinear `chi^dagger gamma^4 gamma^1 chi = s (a^2 - b^2)`, y-current
//! `-i chi^dagger (BC gamma^0) chi = -2 s Re(a * conj(i b)) = 0` for real
//! a, b (standing waves carry no y-current; every gamma^0-eigenvector
//! boundary condition kills it).  Block types: s = +1 (blocks 0..3) and
//! s = -1 (blocks 4..7); the s = -1 system is the s = +1 system with
//! eps -> -eps, and (k, eps) -> (-k, -eps) is a symmetry of each block.

use crate::generated::{
    BLOCK_BASIS_IM, BLOCK_BASIS_RE, BLOCK_BASIS_UNIT_SQUARED_INVERSE, BLOCK_COUNT, BLOCK_LABELS,
    BLOCK_SOURCE_COLUMN, B_IMAG, CHARGE, GAMMA,
};
use crate::output::Json;

pub const N: usize = 16;
pub type Real16 = [[f64; N]; N];

/// Complex 16x16 matrix as separate real and imaginary parts.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct C16 {
    pub re: Real16,
    pub im: Real16,
}

/// Complex 2x2 matrix.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct C2 {
    pub re: [[f64; 2]; 2],
    pub im: [[f64; 2]; 2],
}

fn rmul(a: &Real16, b: &Real16) -> Real16 {
    let mut out = [[0.0; N]; N];
    for i in 0..N {
        for k in 0..N {
            let aik = a[i][k];
            if aik != 0.0 {
                for j in 0..N {
                    out[i][j] += aik * b[k][j];
                }
            }
        }
    }
    out
}

impl C16 {
    pub fn zero() -> Self {
        Self {
            re: [[0.0; N]; N],
            im: [[0.0; N]; N],
        }
    }

    pub fn identity() -> Self {
        let mut m = Self::zero();
        for i in 0..N {
            m.re[i][i] = 1.0;
        }
        m
    }

    pub fn real(re: &Real16) -> Self {
        Self {
            re: *re,
            im: [[0.0; N]; N],
        }
    }

    pub fn mul(&self, o: &Self) -> Self {
        let rr = rmul(&self.re, &o.re);
        let ii = rmul(&self.im, &o.im);
        let ri = rmul(&self.re, &o.im);
        let ir = rmul(&self.im, &o.re);
        let mut out = Self::zero();
        for i in 0..N {
            for j in 0..N {
                out.re[i][j] = rr[i][j] - ii[i][j];
                out.im[i][j] = ri[i][j] + ir[i][j];
            }
        }
        out
    }

    pub fn add(&self, o: &Self) -> Self {
        let mut out = *self;
        for i in 0..N {
            for j in 0..N {
                out.re[i][j] += o.re[i][j];
                out.im[i][j] += o.im[i][j];
            }
        }
        out
    }

    /// (a + i b) * self
    pub fn scale(&self, a: f64, b: f64) -> Self {
        let mut out = Self::zero();
        for i in 0..N {
            for j in 0..N {
                out.re[i][j] = a * self.re[i][j] - b * self.im[i][j];
                out.im[i][j] = a * self.im[i][j] + b * self.re[i][j];
            }
        }
        out
    }

    pub fn sub(&self, o: &Self) -> Self {
        self.add(&o.scale(-1.0, 0.0))
    }

    pub fn dagger(&self) -> Self {
        let mut out = Self::zero();
        for i in 0..N {
            for j in 0..N {
                out.re[i][j] = self.re[j][i];
                out.im[i][j] = -self.im[j][i];
            }
        }
        out
    }

    pub fn max_abs(&self) -> f64 {
        let mut value: f64 = 0.0;
        for i in 0..N {
            for j in 0..N {
                value = value
                    .max((self.re[i][j] * self.re[i][j] + self.im[i][j] * self.im[i][j]).sqrt());
            }
        }
        value
    }

    pub fn trace_re(&self) -> f64 {
        (0..N).map(|i| self.re[i][i]).sum()
    }

    fn column_norm2(&self, j: usize) -> f64 {
        (0..N)
            .map(|i| self.re[i][j] * self.re[i][j] + self.im[i][j] * self.im[i][j])
            .sum()
    }
}

/// The generators and labels of the reduction, built from the fixture.
#[derive(Clone, Debug)]
pub struct Operators {
    pub a0: C16,
    pub a1: C16,
    pub a4: C16,
    pub j: C16,
    pub k1: C16,
    pub k2: C16,
    pub c: C16,
    pub b: C16,
    pub gamma4: C16,
    pub bc: C16,
    pub g4g1: C16,
    pub bcg0: C16,
}

impl Operators {
    pub fn new() -> Self {
        let g: Vec<C16> = GAMMA.iter().map(C16::real).collect();
        let a0 = g[0];
        let a1 = g[0].mul(&g[1]);
        let a4 = g[0].mul(&g[4]);
        let j = a0.mul(&a1).mul(&a4);
        let k1 = g[2].mul(&g[3]);
        let k2 = g[5].mul(&g[6]);
        let c = C16::real(&CHARGE);
        let b = C16 {
            re: [[0.0; N]; N],
            im: B_IMAG,
        };
        Self {
            a0,
            a1,
            a4,
            j,
            k1,
            k2,
            c,
            b,
            gamma4: g[4],
            bc: b.mul(&c),
            g4g1: g[4].mul(&g[1]),
            bcg0: b.mul(&c).mul(&g[0]),
        }
    }
}

impl Default for Operators {
    fn default() -> Self {
        Self::new()
    }
}

/// The nine block forms with their expected Pauli structure.
pub const FORM_NAMES: [&str; 9] = [
    "A0",
    "A1",
    "A4",
    "gamma4",
    "C",
    "B",
    "BC",
    "gamma4gamma1",
    "BCgamma0",
];

fn pauli(name: char, fr: f64, fi: f64) -> C2 {
    let (re, im): ([[f64; 2]; 2], [[f64; 2]; 2]) = match name {
        'x' => ([[0.0, 1.0], [1.0, 0.0]], [[0.0; 2]; 2]),
        'y' => ([[0.0; 2]; 2], [[0.0, -1.0], [1.0, 0.0]]),
        'z' => ([[1.0, 0.0], [0.0, -1.0]], [[0.0; 2]; 2]),
        _ => ([[1.0, 0.0], [0.0, 1.0]], [[0.0; 2]; 2]),
    };
    let mut out = C2 {
        re: [[0.0; 2]; 2],
        im: [[0.0; 2]; 2],
    };
    for p in 0..2 {
        for q in 0..2 {
            out.re[p][q] = fr * re[p][q] - fi * im[p][q];
            out.im[p][q] = fr * im[p][q] + fi * re[p][q];
        }
    }
    out
}

/// Expected block form of operator `name` on the block with label (s, c1, c2).
pub fn expected_form(name: &str, s: f64, c1: f64) -> C2 {
    match name {
        "A0" => pauli('z', 1.0, 0.0),
        "A1" => pauli('y', 0.0, -1.0),
        "A4" => pauli('x', -s, 0.0),
        "gamma4" => pauli('y', 0.0, -s),
        "C" => pauli('y', -c1, 0.0),
        "B" => pauli('1', c1 * s, 0.0),
        "BC" => pauli('y', -s, 0.0),
        "gamma4gamma1" => pauli('z', s, 0.0),
        _ => pauli('x', 0.0, -s),
    }
}

/// Result of the numerical derivation.
#[derive(Clone, Debug)]
pub struct Reduction {
    /// Orthonormal basis: columns 2b, 2b+1 are (v, w) of block b.
    pub basis: C16,
    pub labels: [[i32; 3]; BLOCK_COUNT],
    /// max |basis - exact generated basis| over all entries.
    pub basis_defect_vs_generated: f64,
    /// max over operators and off-diagonal 2x2 blocks of |entry|.
    pub off_block_defect: f64,
    /// max over operators and blocks of |block - expected form|.
    pub form_defect: f64,
    /// max defect of the Clifford identities of the 2x2 blocks.
    pub clifford_defect: f64,
    /// max |Tr J|, |J^2 - 1|, |K^2 + 1|, commutator defects.
    pub label_defect: f64,
    /// Rank-1 test of the eight projectors: |Tr P - 1| and |P^2 - P|.
    pub projector_defect: f64,
    /// Per operator and block: the 2x2 form found (complex).
    pub forms: Vec<Vec<C2>>,
}

fn block_of(y: &C16, b: usize) -> C2 {
    let mut out = C2 {
        re: [[0.0; 2]; 2],
        im: [[0.0; 2]; 2],
    };
    for p in 0..2 {
        for q in 0..2 {
            out.re[p][q] = y.re[2 * b + p][2 * b + q];
            out.im[p][q] = y.im[2 * b + p][2 * b + q];
        }
    }
    out
}

fn c2_defect(a: &C2, b: &C2) -> f64 {
    let mut value: f64 = 0.0;
    for p in 0..2 {
        for q in 0..2 {
            let dr = a.re[p][q] - b.re[p][q];
            let di = a.im[p][q] - b.im[p][q];
            value = value.max((dr * dr + di * di).sqrt());
        }
    }
    value
}

fn c2_mul(a: &C2, b: &C2) -> C2 {
    let mut out = C2 {
        re: [[0.0; 2]; 2],
        im: [[0.0; 2]; 2],
    };
    for p in 0..2 {
        for q in 0..2 {
            for r in 0..2 {
                out.re[p][q] += a.re[p][r] * b.re[r][q] - a.im[p][r] * b.im[r][q];
                out.im[p][q] += a.re[p][r] * b.im[r][q] + a.im[p][r] * b.re[r][q];
            }
        }
    }
    out
}

fn c2_add(a: &C2, b: &C2, sb: f64) -> C2 {
    let mut out = *a;
    for p in 0..2 {
        for q in 0..2 {
            out.re[p][q] += sb * b.re[p][q];
            out.im[p][q] += sb * b.im[p][q];
        }
    }
    out
}

/// Derive the reduction from the fixture constants and verify everything.
pub fn derive() -> Reduction {
    let ops = Operators::new();
    let ident = C16::identity();
    // label operators
    let mut label_defect: f64 = ops.j.trace_re().abs();
    label_defect = label_defect.max(ops.j.mul(&ops.j).sub(&ident).max_abs());
    label_defect = label_defect.max(ops.k1.mul(&ops.k1).add(&ident).max_abs());
    label_defect = label_defect.max(ops.k2.mul(&ops.k2).add(&ident).max_abs());
    label_defect = label_defect.max(ops.j.sub(&ops.j.dagger()).max_abs());
    for x in [&ops.j, &ops.k1, &ops.k2, &ops.a0] {
        for y in [&ops.j, &ops.k1, &ops.k2, &ops.a0] {
            label_defect = label_defect.max(x.mul(y).sub(&y.mul(x)).max_abs());
        }
    }
    for x in [&ops.a1, &ops.a4, &ops.c, &ops.b] {
        for y in [&ops.j, &ops.k1, &ops.k2] {
            label_defect = label_defect.max(x.mul(y).sub(&y.mul(x)).max_abs());
        }
    }
    let mut basis = C16::zero();
    let mut projector_defect: f64 = 0.0;
    let mut basis_defect: f64 = 0.0;
    let unit = 1.0 / BLOCK_BASIS_UNIT_SQUARED_INVERSE.sqrt();
    for (b, label) in BLOCK_LABELS.iter().enumerate() {
        let s = label[0] as f64;
        let c1 = label[1] as f64;
        let c2 = label[2] as f64;
        let p = ident
            .add(&ops.j.scale(s, 0.0))
            .mul(&ident.add(&ops.k1.scale(0.0, c1)))
            .mul(&ident.add(&ops.k2.scale(0.0, c2)))
            .mul(&ident.add(&ops.a0))
            .scale(1.0 / 16.0, 0.0);
        projector_defect = projector_defect.max((p.trace_re() - 1.0).abs());
        projector_defect = projector_defect.max(p.mul(&p).sub(&p).max_abs());
        // first column with a nonzero norm (same choice as the generator)
        let mut column = N;
        for j in 0..N {
            if p.column_norm2(j) > 1e-12 {
                column = j;
                break;
            }
        }
        projector_defect = projector_defect.max(if column == BLOCK_SOURCE_COLUMN[b] {
            0.0
        } else {
            1.0
        });
        let norm = p.column_norm2(column).sqrt();
        let mut v = [(0.0, 0.0); N];
        for (i, item) in v.iter_mut().enumerate() {
            *item = (p.re[i][column] / norm, p.im[i][column] / norm);
        }
        // w = A1 v (A1 real, orthogonal: |w| = |v| = 1)
        let mut w = [(0.0, 0.0); N];
        for (i, item) in w.iter_mut().enumerate() {
            let mut re = 0.0;
            let mut im = 0.0;
            for (row_entry, vk) in ops.a1.re[i].iter().zip(v.iter()) {
                re += row_entry * vk.0;
                im += row_entry * vk.1;
            }
            *item = (re, im);
        }
        for i in 0..N {
            basis.re[i][2 * b] = v[i].0;
            basis.im[i][2 * b] = v[i].1;
            basis.re[i][2 * b + 1] = w[i].0;
            basis.im[i][2 * b + 1] = w[i].1;
            basis_defect = basis_defect.max((v[i].0 - BLOCK_BASIS_RE[b][0][i] * unit).abs());
            basis_defect = basis_defect.max((v[i].1 - BLOCK_BASIS_IM[b][0][i] * unit).abs());
            basis_defect = basis_defect.max((w[i].0 - BLOCK_BASIS_RE[b][1][i] * unit).abs());
            basis_defect = basis_defect.max((w[i].1 - BLOCK_BASIS_IM[b][1][i] * unit).abs());
        }
    }
    // orthonormality
    let gram = basis.dagger().mul(&basis);
    projector_defect = projector_defect.max(gram.sub(&ident).max_abs());
    // block forms
    let operators = [
        &ops.a0,
        &ops.a1,
        &ops.a4,
        &ops.gamma4,
        &ops.c,
        &ops.b,
        &ops.bc,
        &ops.g4g1,
        &ops.bcg0,
    ];
    let mut off_block_defect: f64 = 0.0;
    let mut form_defect: f64 = 0.0;
    let mut forms: Vec<Vec<C2>> = Vec::new();
    for (name, op) in FORM_NAMES.iter().zip(operators.iter()) {
        let y = basis.dagger().mul(op).mul(&basis);
        for i in 0..N {
            for j in 0..N {
                if i / 2 != j / 2 {
                    off_block_defect = off_block_defect
                        .max((y.re[i][j] * y.re[i][j] + y.im[i][j] * y.im[i][j]).sqrt());
                }
            }
        }
        let mut per_block = Vec::new();
        for (b, label) in BLOCK_LABELS.iter().enumerate() {
            let found = block_of(&y, b);
            let expected = expected_form(name, label[0] as f64, label[1] as f64);
            form_defect = form_defect.max(c2_defect(&found, &expected));
            per_block.push(found);
        }
        forms.push(per_block);
    }
    // Clifford identities of the found 2x2 blocks: A0^2 = 1, A1^2 = -1,
    // A4^2 = 1, anticommutators zero, gamma4 = A0 A4, BC = B C,
    // gamma4gamma1 = gamma4 (A0 A1), BCgamma0 = BC A0, J = A0 A1 A4 = s.
    let one = pauli('1', 1.0, 0.0);
    let mut clifford_defect: f64 = 0.0;
    for (b, label) in BLOCK_LABELS.iter().enumerate() {
        let a0 = forms[0][b];
        let a1 = forms[1][b];
        let a4 = forms[2][b];
        let g4 = forms[3][b];
        let c = forms[4][b];
        let bb = forms[5][b];
        let bc = forms[6][b];
        let g4g1 = forms[7][b];
        let bcg0 = forms[8][b];
        clifford_defect = clifford_defect.max(c2_defect(&c2_mul(&a0, &a0), &one));
        clifford_defect = clifford_defect.max(c2_defect(&c2_mul(&a1, &a1), &pauli('1', -1.0, 0.0)));
        clifford_defect = clifford_defect.max(c2_defect(&c2_mul(&a4, &a4), &one));
        let zero = pauli('1', 0.0, 0.0);
        clifford_defect = clifford_defect.max(c2_defect(
            &c2_add(&c2_mul(&a0, &a1), &c2_mul(&a1, &a0), 1.0),
            &zero,
        ));
        clifford_defect = clifford_defect.max(c2_defect(
            &c2_add(&c2_mul(&a0, &a4), &c2_mul(&a4, &a0), 1.0),
            &zero,
        ));
        clifford_defect = clifford_defect.max(c2_defect(
            &c2_add(&c2_mul(&a1, &a4), &c2_mul(&a4, &a1), 1.0),
            &zero,
        ));
        clifford_defect = clifford_defect.max(c2_defect(&c2_mul(&a0, &a4), &g4));
        clifford_defect = clifford_defect.max(c2_defect(&c2_mul(&bb, &c), &bc));
        clifford_defect = clifford_defect.max(c2_defect(&c2_mul(&g4, &c2_mul(&a0, &a1)), &g4g1));
        clifford_defect = clifford_defect.max(c2_defect(&c2_mul(&bc, &a0), &bcg0));
        let j = c2_mul(&c2_mul(&a0, &a1), &a4);
        clifford_defect = clifford_defect.max(c2_defect(&j, &pauli('1', label[0] as f64, 0.0)));
    }
    Reduction {
        basis,
        labels: BLOCK_LABELS,
        basis_defect_vs_generated: basis_defect,
        off_block_defect,
        form_defect,
        clifford_defect,
        label_defect,
        projector_defect,
        forms,
    }
}

impl Reduction {
    /// Largest of all defects.
    pub fn max_defect(&self) -> f64 {
        self.basis_defect_vs_generated
            .max(self.off_block_defect)
            .max(self.form_defect)
            .max(self.clifford_defect)
            .max(self.label_defect)
            .max(self.projector_defect)
    }

    /// JSON document describing the reduction (basis, labels, forms, defects).
    pub fn to_json(&self) -> Json {
        let mut blocks = Vec::new();
        for (b, label) in self.labels.iter().enumerate() {
            let mut cols = Vec::new();
            for c in 0..2 {
                let mut entries = Vec::new();
                for i in 0..N {
                    entries.push(Json::floats(&[
                        self.basis.re[i][2 * b + c],
                        self.basis.im[i][2 * b + c],
                    ]));
                }
                cols.push(Json::Array(entries));
            }
            let mut forms = Vec::new();
            for (f, name) in FORM_NAMES.iter().enumerate() {
                let m = &self.forms[f][b];
                forms.push((
                    *name,
                    Json::Array(
                        (0..2)
                            .map(|p| {
                                Json::Array(
                                    (0..2)
                                        .map(|q| Json::floats(&[m.re[p][q], m.im[p][q]]))
                                        .collect(),
                                )
                            })
                            .collect(),
                    ),
                ));
            }
            blocks.push(Json::object(vec![
                ("index", Json::Int(b as i64)),
                (
                    "label_s_c1_c2",
                    Json::Array(label.iter().map(|x| Json::Int(*x as i64)).collect()),
                ),
                ("kreinSign_c1s", Json::Int((label[0] * label[1]) as i64)),
                ("basisColumns_v_w_re_im", Json::Array(cols)),
                ("forms_re_im", Json::object(forms)),
            ]));
        }
        Json::object(vec![
            ("labelOperators", Json::str("J = gamma^0 gamma^1 gamma^4 (s), i gamma^2 gamma^3 (c1), i gamma^5 gamma^6 (c2); first vector: gamma^0 = +1")),
            ("expectedForms", Json::str("A0 -> sigma_z, A1 -> -i sigma_y, A4 -> -s sigma_x, gamma4 -> -i s sigma_y, C -> -c1 sigma_y, B -> c1 s, BC -> -s sigma_y, gamma4gamma1 -> s sigma_z, BCgamma0 -> -i s sigma_x")),
            ("realSystem", Json::str("chi = (a, i b): a' = M a + (s eps - kappa k) b, b' = -(s eps + kappa k) a - M b; n = a^2 + b^2, S = -2 s a b, p1-bilinear = s (a^2 - b^2)")),
            ("basisDefectVsExactGenerated", Json::Float(self.basis_defect_vs_generated)),
            ("offBlockDefect", Json::Float(self.off_block_defect)),
            ("formDefect", Json::Float(self.form_defect)),
            ("cliffordDefect", Json::Float(self.clifford_defect)),
            ("labelDefect", Json::Float(self.label_defect)),
            ("projectorDefect", Json::Float(self.projector_defect)),
            ("blocks", Json::Array(blocks)),
        ])
    }
}

/// Real 2x2 reduced system for block type `s`: returns the matrix
/// `[[M, s eps - kappa k], [-(s eps + kappa k), -M]]` acting on (a, b).
pub fn real_system(m: f64, kappa_k: f64, eps: f64, s: f64) -> [[f64; 2]; 2] {
    [[m, s * eps - kappa_k], [-(s * eps + kappa_k), -m]]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn reduction_is_exact_to_1e14() {
        let red = derive();
        assert!(red.label_defect == 0.0, "{}", red.label_defect);
        assert!(red.projector_defect < 1e-14, "{}", red.projector_defect);
        assert!(
            red.basis_defect_vs_generated < 1e-15,
            "{}",
            red.basis_defect_vs_generated
        );
        assert!(red.off_block_defect < 1e-14, "{}", red.off_block_defect);
        assert!(red.form_defect < 1e-14, "{}", red.form_defect);
        assert!(red.clifford_defect < 1e-14, "{}", red.clifford_defect);
        // four blocks of each type s
        assert_eq!(red.labels.iter().filter(|l| l[0] == 1).count(), 4);
    }

    #[test]
    fn complex_block_equation_equals_real_system() {
        // chi' = [M sigma_z - kappa k sigma_y - i s eps sigma_x] chi with chi = (a, i b)
        let (m, kk, eps) = (0.7, 1.3, -0.4);
        for s in [1.0, -1.0] {
            let a0 = expected_form("A0", s, 1.0);
            let a1 = expected_form("A1", s, 1.0);
            let a4 = expected_form("A4", s, 1.0);
            // coefficient matrix M A0 - i kk A1 + i eps A4
            let mut coef = C2 {
                re: [[0.0; 2]; 2],
                im: [[0.0; 2]; 2],
            };
            for p in 0..2 {
                for q in 0..2 {
                    coef.re[p][q] = m * a0.re[p][q] + kk * a1.im[p][q] - eps * a4.im[p][q];
                    coef.im[p][q] = m * a0.im[p][q] - kk * a1.re[p][q] + eps * a4.re[p][q];
                }
            }
            let (a, b) = (0.31, -0.77);
            let chi = [(a, 0.0), (0.0, b)];
            let mut d = [(0.0, 0.0); 2];
            for (p, dp) in d.iter_mut().enumerate() {
                for (q, cq) in chi.iter().enumerate() {
                    dp.0 += coef.re[p][q] * cq.0 - coef.im[p][q] * cq.1;
                    dp.1 += coef.re[p][q] * cq.1 + coef.im[p][q] * cq.0;
                }
            }
            let sys = real_system(m, kk, eps, s);
            let da = sys[0][0] * a + sys[0][1] * b;
            let db = sys[1][0] * a + sys[1][1] * b;
            assert!((d[0].0 - da).abs() < 1e-15 && d[0].1.abs() < 1e-15, "s={s}");
            assert!((d[1].1 - db).abs() < 1e-15 && d[1].0.abs() < 1e-15, "s={s}");
        }
    }
}
