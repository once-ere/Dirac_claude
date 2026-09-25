//! 16x16 complex linear algebra for the dirac16complex mode equations.
//!
//! * [`CMat16`]: a complex 16x16 matrix stored as separate real and
//!   imaginary parts (`re[i][j] + i im[i][j]`, row i, column j, zero-based).
//! * [`CVec16`]: a spinor u in C^16.  In every ODE state vector the spinor
//!   occupies 32 consecutive reals in the layout
//!   `(re u_0, ..., re u_15, im u_0, ..., im u_15)` ([`CVec16::from_state`],
//!   [`CVec16::write_state`]).
//! * [`Algebra`]: gamma^a (a = 0..7), the products gamma^4 gamma^j, the
//!   charge matrix C, B = -i C gamma^4 and the chirality, all taken from
//!   `generated.rs` (which the generator verified exactly against the
//!   algebra fixture).
//! * The mode Hamiltonian (NUMERICS_CONTRACT "Physics common to all
//!   experiments"):  `i du/dt = h(t) u`,
//!   `h = -i M_eff gamma^4 - gamma^4 sum_{j != 4} (k_j / h_j) gamma^j`.
//!   Hermitian iff the extra-time momenta k_5, k_6, k_7 vanish.
//! * Bilinears `u^dagger M u` and the expectation-value rule of the
//!   positive-norm (J = B) quantization: `<Psi^dagger M Psi> = u^dagger B M u`
//!   ([`b_expectation`]); hence the scalar density
//!   `s(u) = u^dagger B C u = u^dagger (-i gamma^4) u` and the energy
//!   `<Psi^dagger B h Psi> = u^dagger h u`.
//! * Exact eigenvectors without a linear-algebra crate: whenever
//!   `h^2 = E^2 I` (true for the mode Hamiltonian at fixed t, E^2 =
//!   M^2 + sum_space (k/h)^2 - sum_time (k/h)^2), `P_+- = (I +- h/E)/2` are the
//!   spectral projectors; applying a product of commuting projectors to the
//!   basis vectors e_0..e_15 and Gram-Schmidt orthonormalising gives an
//!   orthonormal basis of the joint eigenspace ([`range_basis`]).
//! * Exact propagator for constant h with h^2 = E^2 I, E > 0:
//!   `exp(-i h t) = cos(E t) I - i sin(E t) h / E` ([`exact_propagator`]).

use crate::generated::{B_IMAG, CHARGE, CHIRALITY, GAMMA};
use crate::math::{cos, sin};

pub const N: usize = 16;
/// Number of reals a spinor occupies in an ODE state vector.
pub const STATE_REALS: usize = 32;
/// Transverse (non-time) frame indices T = {0,1,2,3,5,6,7}.
pub const TRANSVERSE: [usize; 7] = [0, 1, 2, 3, 5, 6, 7];

pub type RMat16 = [[f64; N]; N];

/// Complex 16x16 matrix.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct CMat16 {
    pub re: RMat16,
    pub im: RMat16,
}

/// Complex 16-vector (spinor).
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct CVec16 {
    pub re: [f64; N],
    pub im: [f64; N],
}

fn real_mul(a: &RMat16, b: &RMat16) -> RMat16 {
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

impl CMat16 {
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

    pub fn from_real(re: &RMat16) -> Self {
        Self {
            re: *re,
            im: [[0.0; N]; N],
        }
    }

    pub fn from_imag(im: &RMat16) -> Self {
        Self {
            re: [[0.0; N]; N],
            im: *im,
        }
    }

    pub fn mul(&self, other: &Self) -> Self {
        let rr = real_mul(&self.re, &other.re);
        let ii = real_mul(&self.im, &other.im);
        let ri = real_mul(&self.re, &other.im);
        let ir = real_mul(&self.im, &other.re);
        let mut out = Self::zero();
        for i in 0..N {
            for j in 0..N {
                out.re[i][j] = rr[i][j] - ii[i][j];
                out.im[i][j] = ri[i][j] + ir[i][j];
            }
        }
        out
    }

    pub fn add(&self, other: &Self) -> Self {
        let mut out = *self;
        for i in 0..N {
            for j in 0..N {
                out.re[i][j] += other.re[i][j];
                out.im[i][j] += other.im[i][j];
            }
        }
        out
    }

    pub fn sub(&self, other: &Self) -> Self {
        self.add(&other.scale(-1.0, 0.0))
    }

    /// Multiply by the complex scalar (a + i b).
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

    /// Largest entry modulus (max-norm).
    pub fn max_abs(&self) -> f64 {
        let mut value: f64 = 0.0;
        for i in 0..N {
            for j in 0..N {
                value = value.max(self.re[i][j].hypot(self.im[i][j]));
            }
        }
        value
    }

    /// max |M - M^dagger| (0 for a Hermitian matrix).
    pub fn hermiticity_defect(&self) -> f64 {
        self.sub(&self.dagger()).max_abs()
    }

    pub fn apply(&self, v: &CVec16) -> CVec16 {
        let mut out = CVec16::zero();
        for i in 0..N {
            let mut re = 0.0;
            let mut im = 0.0;
            for j in 0..N {
                re += self.re[i][j] * v.re[j] - self.im[i][j] * v.im[j];
                im += self.re[i][j] * v.im[j] + self.im[i][j] * v.re[j];
            }
            out.re[i] = re;
            out.im[i] = im;
        }
        out
    }

    pub fn trace(&self) -> (f64, f64) {
        let mut re = 0.0;
        let mut im = 0.0;
        for i in 0..N {
            re += self.re[i][i];
            im += self.im[i][i];
        }
        (re, im)
    }
}

impl CVec16 {
    pub fn zero() -> Self {
        Self {
            re: [0.0; N],
            im: [0.0; N],
        }
    }

    pub fn basis(index: usize) -> Self {
        let mut v = Self::zero();
        v.re[index] = 1.0;
        v
    }

    /// Read the spinor from `state[0..32]` = (re0..re15, im0..im15).
    pub fn from_state(state: &[f64]) -> Self {
        let mut v = Self::zero();
        v.re.copy_from_slice(&state[..N]);
        v.im.copy_from_slice(&state[N..STATE_REALS]);
        v
    }

    /// Write the spinor into `state[0..32]` in the same layout.
    pub fn write_state(&self, state: &mut [f64]) {
        state[..N].copy_from_slice(&self.re);
        state[N..STATE_REALS].copy_from_slice(&self.im);
    }

    pub fn to_state(&self) -> Vec<f64> {
        let mut state = vec![0.0; STATE_REALS];
        self.write_state(&mut state);
        state
    }

    /// Hermitian inner product self^dagger other = (re, im).
    pub fn dot(&self, other: &Self) -> (f64, f64) {
        let mut re = 0.0;
        let mut im = 0.0;
        for i in 0..N {
            re += self.re[i] * other.re[i] + self.im[i] * other.im[i];
            im += self.re[i] * other.im[i] - self.im[i] * other.re[i];
        }
        (re, im)
    }

    pub fn norm2(&self) -> f64 {
        self.dot(self).0
    }

    /// self + (a + i b) other
    pub fn axpy(&self, a: f64, b: f64, other: &Self) -> Self {
        let mut out = *self;
        for i in 0..N {
            out.re[i] += a * other.re[i] - b * other.im[i];
            out.im[i] += a * other.im[i] + b * other.re[i];
        }
        out
    }

    pub fn scale(&self, a: f64, b: f64) -> Self {
        Self::zero().axpy(a, b, self)
    }

    /// max_i |self_i - other_i|
    pub fn max_abs_diff(&self, other: &Self) -> f64 {
        let mut value: f64 = 0.0;
        for i in 0..N {
            value = value.max((self.re[i] - other.re[i]).hypot(self.im[i] - other.im[i]));
        }
        value
    }

    /// Euclidean distance |self - other|_2.
    pub fn distance(&self, other: &Self) -> f64 {
        self.axpy(-1.0, 0.0, other).norm2().sqrt()
    }
}

/// The Clifford data needed by the experiments, precomputed once.
#[derive(Clone, Debug)]
pub struct Algebra {
    /// gamma^a, a = 0..7 (real).
    pub gamma: [RMat16; 8],
    /// gamma^4 gamma^j, j = 0..7 (real; index 4 is -I and never used).
    pub g4g: [RMat16; 8],
    /// C = gamma^0 gamma^1 gamma^2 gamma^3 (real symmetric).
    pub charge: RMat16,
    /// B = -i C gamma^4 (Hermitian, B^2 = I).
    pub b: CMat16,
    /// gamma^8 = gamma^0 ... gamma^7 = diag(-I8, +I8).
    pub chirality: RMat16,
    /// -i gamma^4 (so that s(u) = u^dagger (-i gamma^4) u).
    pub minus_i_g4: CMat16,
}

impl Default for Algebra {
    fn default() -> Self {
        Self::new()
    }
}

impl Algebra {
    pub fn new() -> Self {
        let gamma = GAMMA;
        let mut g4g = [[[0.0; N]; N]; 8];
        for (j, product) in g4g.iter_mut().enumerate() {
            *product = real_mul(&gamma[4], &gamma[j]);
        }
        Self {
            gamma,
            g4g,
            charge: CHARGE,
            b: CMat16::from_imag(&B_IMAG),
            chirality: CHIRALITY,
            minus_i_g4: CMat16::from_imag(&gamma[4]).scale(-1.0, 0.0),
        }
    }

    pub fn gamma_c(&self, a: usize) -> CMat16 {
        CMat16::from_real(&self.gamma[a])
    }

    /// h = -i M gamma^4 - sum_{j != 4} kh[j] gamma^4 gamma^j, with
    /// kh[j] = k_j / h_j (physical momenta; kh[4] is ignored).
    pub fn mode_hamiltonian(&self, m_eff: f64, kh: &[f64; 8]) -> CMat16 {
        let mut h = CMat16::zero();
        for i in 0..N {
            for j in 0..N {
                h.im[i][j] = -m_eff * self.gamma[4][i][j];
                let mut re = 0.0;
                for &a in &TRANSVERSE {
                    re -= kh[a] * self.g4g[a][i][j];
                }
                h.re[i][j] = re;
            }
        }
        h
    }
}

/// E^2 = M^2 + sum_{j<4} kh_j^2 - sum_{j>4} kh_j^2 (h^2 = E^2 I).
pub fn energy_squared(m_eff: f64, kh: &[f64; 8]) -> f64 {
    let mut value = m_eff * m_eff;
    for &a in &TRANSVERSE {
        if a < 4 {
            value += kh[a] * kh[a];
        } else {
            value -= kh[a] * kh[a];
        }
    }
    value
}

/// RHS of i du/dt = h u in the 32-real layout: with u = x + i y and
/// h = hr + i hi,  dx/dt = hr y + hi x,  dy/dt = hi y - hr x.
pub fn mode_rhs(h: &CMat16, y: &[f64], ydot: &mut [f64]) {
    for i in 0..N {
        let mut dx = 0.0;
        let mut dy = 0.0;
        for j in 0..N {
            let xr = y[j];
            let xi = y[N + j];
            dx += h.re[i][j] * xi + h.im[i][j] * xr;
            dy += h.im[i][j] * xi - h.re[i][j] * xr;
        }
        ydot[i] = dx;
        ydot[N + i] = dy;
    }
}

/// u^dagger M u = (re, im).
pub fn expectation(u: &CVec16, m: &CMat16) -> (f64, f64) {
    u.dot(&m.apply(u))
}

/// u^dagger M u for a real matrix M.
pub fn expectation_real(u: &CVec16, m: &RMat16) -> (f64, f64) {
    expectation(u, &CMat16::from_real(m))
}

/// Expectation-value rule: <Psi^dagger M Psi> = u^dagger B M u.
pub fn b_expectation(alg: &Algebra, u: &CVec16, m: &CMat16) -> (f64, f64) {
    expectation(u, &alg.b.mul(m))
}

/// Hilbert norm u^dagger u.
pub fn norm_hilbert(u: &CVec16) -> f64 {
    u.norm2()
}

/// Krein norm u^dagger B u (real because B is Hermitian).
pub fn norm_krein(alg: &Algebra, u: &CVec16) -> f64 {
    expectation(u, &alg.b).0
}

/// Scalar density per mode s(u) = u^dagger (-i gamma^4) u = u^dagger B C u.
pub fn scalar_density(alg: &Algebra, u: &CVec16) -> f64 {
    expectation(u, &alg.minus_i_g4).0
}

/// Mode energy eps(u) = u^dagger h u (real part; the imaginary part vanishes
/// for Hermitian h).
pub fn mode_energy(h: &CMat16, u: &CVec16) -> f64 {
    expectation(u, h).0
}

/// Mode pressure p_j(u) = -(k_j/h_j) u^dagger gamma^4 gamma^j u (no sum).
pub fn mode_pressure(alg: &Algebra, u: &CVec16, kh_j: f64, j: usize) -> f64 {
    -kh_j * expectation_real(u, &alg.g4g[j]).0
}

/// P = (I + sign h / E) / 2 (spectral projector when h^2 = E^2 I, E > 0).
pub fn energy_projector(h: &CMat16, energy: f64, sign: f64) -> CMat16 {
    CMat16::identity()
        .add(&h.scale(sign / energy, 0.0))
        .scale(0.5, 0.0)
}

/// (I + sign M) / 2 for an involution M (M^2 = I), e.g. B or C.
pub fn involution_projector(m: &CMat16, sign: f64) -> CMat16 {
    CMat16::identity().add(&m.scale(sign, 0.0)).scale(0.5, 0.0)
}

/// Orthonormal basis of the range of `projector`: apply it to e_0..e_15,
/// Gram-Schmidt (modified, two passes) against the vectors already accepted,
/// accept a vector when its remaining norm exceeds `threshold`.
pub fn range_basis(projector: &CMat16, threshold: f64) -> Vec<CVec16> {
    let mut basis: Vec<CVec16> = Vec::new();
    for index in 0..N {
        let mut v = projector.apply(&CVec16::basis(index));
        for _pass in 0..2 {
            for q in &basis {
                let (re, im) = q.dot(&v);
                v = v.axpy(-re, -im, q);
            }
        }
        let norm = v.norm2().sqrt();
        if norm > threshold {
            basis.push(v.scale(1.0 / norm, 0.0));
        }
    }
    basis
}

/// exp(-i h t) = cos(E t) I - i sin(E t) h / E for constant h with
/// h^2 = E^2 I and E > 0.
pub fn exact_propagator(h: &CMat16, energy: f64, t: f64) -> CMat16 {
    let c = cos(energy * t);
    let s = sin(energy * t);
    CMat16::identity()
        .scale(c, 0.0)
        .add(&h.scale(0.0, -s / energy))
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::driver::{integrate, uniform_targets, RhsFn, SolverConfig};
    use crate::generated::ETA;

    fn real_equal(a: &RMat16, b: &RMat16) -> bool {
        (0..N).all(|i| (0..N).all(|j| a[i][j] == b[i][j]))
    }

    fn transpose(a: &RMat16) -> RMat16 {
        let mut t = [[0.0; N]; N];
        for i in 0..N {
            for j in 0..N {
                t[i][j] = a[j][i];
            }
        }
        t
    }

    #[test]
    fn clifford_relations_from_generated_constants() {
        let alg = Algebra::new();
        for (a, eta_a) in ETA.iter().enumerate() {
            for b in 0..8 {
                let ab = real_mul(&alg.gamma[a], &alg.gamma[b]);
                let ba = real_mul(&alg.gamma[b], &alg.gamma[a]);
                for i in 0..N {
                    for j in 0..N {
                        let expected = if a == b && i == j { 2.0 * eta_a } else { 0.0 };
                        assert_eq!(ab[i][j] + ba[i][j], expected, "a={a} b={b}");
                    }
                }
            }
            let t = transpose(&alg.gamma[a]);
            let sign = if a < 4 { 1.0 } else { -1.0 };
            assert!((0..N).all(|i| (0..N).all(|j| t[i][j] == sign * alg.gamma[a][i][j])));
        }
    }

    #[test]
    fn charge_b_and_chirality_identities() {
        let alg = Algebra::new();
        let c = real_mul(
            &real_mul(&alg.gamma[0], &alg.gamma[1]),
            &real_mul(&alg.gamma[2], &alg.gamma[3]),
        );
        assert!(real_equal(&c, &alg.charge));
        assert!(real_equal(&transpose(&c), &c));
        for a in 0..8 {
            let cg = real_mul(&c, &alg.gamma[a]);
            let cgt = transpose(&cg);
            assert!((0..N).all(|i| (0..N).all(|j| cgt[i][j] == -cg[i][j])));
        }
        let mut chir = alg.gamma[0];
        for a in 1..8 {
            chir = real_mul(&chir, &alg.gamma[a]);
        }
        assert!(real_equal(&chir, &alg.chirality));
        for i in 0..N {
            assert_eq!(alg.chirality[i][i], if i < 8 { -1.0 } else { 1.0 });
        }
        // B = -i C gamma^4 Hermitian, B^2 = I, B C = -i gamma^4.
        let b_expected = CMat16::from_real(&real_mul(&c, &alg.gamma[4])).scale(0.0, -1.0);
        assert_eq!(alg.b, b_expected);
        assert_eq!(alg.b.hermiticity_defect(), 0.0);
        assert_eq!(alg.b.mul(&alg.b), CMat16::identity());
        assert_eq!(alg.b.mul(&CMat16::from_real(&c)), alg.minus_i_g4);
    }

    #[test]
    fn hamiltonian_hermitian_only_in_good_sector() {
        let alg = Algebra::new();
        let good = [0.3, -0.7, 1.1, 0.4, 0.0, 0.0, 0.0, 0.0];
        let h = alg.mode_hamiltonian(1.3, &good);
        assert!(h.hermiticity_defect() < 1e-15);
        // [B, h] = 0 in the good sector.
        assert!(alg.b.mul(&h).sub(&h.mul(&alg.b)).max_abs() < 1e-15);
        let bad = [0.3, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0];
        let hb = alg.mode_hamiltonian(1.0, &bad);
        assert!(hb.hermiticity_defect() > 0.9);
        // B-pseudo-Hermiticity h^dagger B = B h holds in every sector.
        assert!(hb.dagger().mul(&alg.b).sub(&alg.b.mul(&hb)).max_abs() < 1e-15);
    }

    #[test]
    fn energy_eigenvalues_are_plus_minus_sqrt_m2_k2() {
        let alg = Algebra::new();
        for (m, kh) in [
            (1.0, [0.0; 8]),
            (1.0, [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            (1.0, [2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            (0.7, [0.2, 0.3, -0.4, 0.9, 0.0, 0.0, 0.0, 0.0]),
        ] {
            let h = alg.mode_hamiltonian(m, &kh);
            let e2 = energy_squared(m, &kh);
            let k2: f64 = (0..4).map(|a| kh[a] * kh[a]).sum();
            assert!((e2 - (m * m + k2)).abs() < 1e-15);
            let e = e2.sqrt();
            // h^2 = E^2 I
            assert!(h.mul(&h).sub(&CMat16::identity().scale(e2, 0.0)).max_abs() < 1e-14);
            for sign in [1.0, -1.0] {
                let p = energy_projector(&h, e, sign);
                assert!((p.trace().0 - 8.0).abs() < 1e-13);
                let basis = range_basis(&p, 1e-8);
                assert_eq!(basis.len(), 8);
                for v in &basis {
                    let hv = h.apply(v);
                    assert!(hv.max_abs_diff(&v.scale(sign * e, 0.0)) < 1e-13);
                    assert!((mode_energy(&h, v) - sign * e).abs() < 1e-13);
                    assert!((v.norm2() - 1.0).abs() < 1e-14);
                }
                // joint eigenspaces with B are 4-dimensional
                for bsign in [1.0, -1.0] {
                    let joint = p.mul(&involution_projector(&alg.b, bsign));
                    let jb = range_basis(&joint, 1e-8);
                    assert_eq!(jb.len(), 4);
                    for v in &jb {
                        assert!((norm_krein(&alg, v) - bsign).abs() < 1e-13);
                    }
                }
            }
        }
        // extra-time momentum: E^2 = m^2 - q^2
        let bad = [0.0, 0.0, 0.0, 0.0, 0.0, 0.6, 0.0, 0.0];
        let h = alg.mode_hamiltonian(1.0, &bad);
        assert!((energy_squared(1.0, &bad) - 0.64).abs() < 1e-15);
        assert!(
            h.mul(&h)
                .sub(&CMat16::identity().scale(0.64, 0.0))
                .max_abs()
                < 1e-14
        );
    }

    #[test]
    fn rest_eigenvector_scalar_density_is_one() {
        let alg = Algebra::new();
        let h = alg.mode_hamiltonian(1.0, &[0.0; 8]);
        let basis = range_basis(&energy_projector(&h, 1.0, 1.0), 1e-8);
        for v in &basis {
            assert!((scalar_density(&alg, v) - 1.0).abs() < 1e-14);
            // s(u) = u^dagger B C u (expectation-value rule)
            let s = b_expectation(&alg, v, &CMat16::from_real(&alg.charge)).0;
            assert!((s - 1.0).abs() < 1e-14);
            // u^dagger C u vanishes on these eigenvectors
            assert!(expectation_real(v, &alg.charge).0.abs() < 1e-14);
        }
    }

    #[test]
    fn cvode_matches_exact_solution_for_constant_h() {
        let alg = Algebra::new();
        let kh = [2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0];
        let h = alg.mode_hamiltonian(1.0, &kh);
        let e = energy_squared(1.0, &kh).sqrt();
        let mut u0 = CVec16::zero();
        for i in 0..N {
            u0.re[i] = 1.0 + 0.1 * i as f64;
            u0.im[i] = 0.3 - 0.05 * i as f64;
        }
        let u0 = u0.scale(1.0 / u0.norm2().sqrt(), 0.0);
        let targets = uniform_targets(0.0, 5.0, 50);
        for cfg in [
            SolverConfig::bdf(1e-11, 1e-13, 0.01),
            SolverConfig::adams(1e-11, 1e-13, 0.01),
        ] {
            let run = integrate(u0.to_state(), 0.0, &targets, rhs_clone(&h), &cfg).unwrap();
            for (t, y) in run.times.iter().zip(&run.states) {
                let exact = exact_propagator(&h, e, *t).apply(&u0);
                let u = CVec16::from_state(y);
                assert!(u.max_abs_diff(&exact) < 1e-8, "{:?} t={t}", cfg.method);
                assert!((u.norm2() - 1.0).abs() < 1e-8);
            }
        }
    }

    fn rhs_clone(h: &CMat16) -> RhsFn {
        let hc = *h;
        Box::new(move |_t, y, ydot| {
            mode_rhs(&hc, y, ydot);
            Ok(())
        })
    }
}
