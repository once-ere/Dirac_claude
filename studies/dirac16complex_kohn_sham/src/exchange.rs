//! Hartree-Fock exchange of the contact interaction for the uniform
//! 8-fold-degenerate dirac16complex gas and the LDA pseudo-potential.
//!
//! Interaction `U(S) = (lambda/2) S^2`, `S = Psibar Psi`.  With the density
//! matrix `rho = sum_occ u u^dagger` and the expectation-value rule
//! (`<Psi^dagger_c Psi_b> = (rho B)_{bc}`), the Hartree-Fock energy density is
//!
//! ```text
//! e_int = (lambda/2) [ S^2 - Tr(BC rho BC rho) ],   S = Tr(BC rho),
//! ```
//!
//! (the Wick contraction of `(Psibar Psi)^2` at one point; the second term is
//! the exchange, Fock, term).  For the uniform gas in 3-space (the good
//! sector: q = 0, y bound), with the normal-ordered density matrix
//! `rho = int d^3k/(2 pi)^3 [ f_+(k) P_+(k) - f_-(k) P_-(k) ]`,
//! `P_+- = (1 +- h_k/E_k)/2`, `h_k = -i M gamma^4 - gamma^4 gamma^j k_j`, the
//! exact trace identity (verified numerically in [`kernel_check`])
//!
//! ```text
//! Tr[ BC P_a(k) BC P_b(k') ] = 4 [ 1 + a b (M^2 - k.k') / (E E') ],   a, b = +-1,
//! ```
//!
//! makes the double momentum integral separable; the angular average kills
//! `k.k'`, so with `n = 8 int (f_+ - f_-)`, `S = 8 int (M/E)(f_+ + f_-)`
//! (antiparticles have positive scalar density and negative number density):
//!
//! ```text
//! e_x(n, S) = -(lambda/2) (n^2 + S^2)/16 = -lambda (n^2 + S^2)/32,
//! ```
//!
//! EXACTLY, at every temperature, as a function of the local proper
//! densities (T enters only through n and S).  T = 0 closed form: the same.
//! The filled single-k shell of the design probe (8 states at ONE k-vector)
//! has instead `Tr = S^2/8` because there the `k.k'` term does not average
//! out; both statements are checked.
//!
//! LDA potentials: mass-type `v_s = d e_x/dS = -lambda S/16` and
//! potential-type `v_v = d e_x/dn = -lambda n/16`.  The KS equation uses
//! BOTH (they are the exact functional derivative of the LDA functional):
//! `M_eff(y) = m + lambda S_p(y) + v_s = m + (15/16) lambda S_p(y)` and
//! `eps -> eps - v_v(y)` locally.  This pair is the "Kohn-Sham fermion-gas
//! thermodynamics pseudo-potential".  No correlation term: the contact
//! interaction beyond Hartree-Fock is not renormalisable in 8D.
//!
//! Energy functional (Mermin): `F = sum_i w_i eps_i - int [ (lambda/2) S_p^2
//! + e_x ] dV_p - T S_ent` where `sum w eps` already contains
//! `int [(lambda S + v_s) S + v_v n] dV_p = int [lambda S^2 + 2 e_x] dV_p`.
//! On-shell Lagrangian density used in the EMT: `L_s = (lambda/2) S_p^2 + e_x`.

use crate::blocks::{Operators, C16};
use crate::math::{fermi, PI};

/// Exchange energy density of the uniform gas.
pub fn exchange_energy_density(lambda: f64, n: f64, s: f64) -> f64 {
    -lambda * (n * n + s * s) / 32.0
}

/// Mass-type LDA potential v_s = d e_x / dS.
pub fn v_scalar(lambda: f64, s: f64) -> f64 {
    -lambda * s / 16.0
}

/// Potential-type LDA potential v_v = d e_x / dn.
pub fn v_vector(lambda: f64, n: f64) -> f64 {
    -lambda * n / 16.0
}

/// Hartree mass shift lambda S.
pub fn hartree_mass(lambda: f64, s: f64) -> f64 {
    lambda * s
}

/// Total effective mass m + lambda S + v_s.
pub fn effective_mass(m: f64, lambda: f64, s: f64) -> f64 {
    m + hartree_mass(lambda, s) + v_scalar(lambda, s)
}

/// Interaction energy density (Hartree + exchange).
pub fn interaction_energy_density(lambda: f64, n: f64, s: f64) -> f64 {
    0.5 * lambda * s * s + exchange_energy_density(lambda, n, s)
}

/// Gauss-Legendre nodes and weights on [-1, 1] (Newton on Legendre polynomials).
pub fn gauss_legendre(n: usize) -> (Vec<f64>, Vec<f64>) {
    let mut x = vec![0.0; n];
    let mut w = vec![0.0; n];
    for i in 0..n {
        let mut z = crate::math::cos(PI * (i as f64 + 0.75) / (n as f64 + 0.5));
        let mut pp = 1.0;
        for _ in 0..100 {
            let mut p1 = 1.0;
            let mut p2 = 0.0;
            for j in 0..n {
                let p3 = p2;
                p2 = p1;
                p1 = ((2.0 * j as f64 + 1.0) * z * p2 - j as f64 * p3) / (j as f64 + 1.0);
            }
            pp = n as f64 * (z * p1 - p2) / (z * z - 1.0);
            let z1 = z;
            z = z1 - p1 / pp;
            if (z - z1).abs() < 1e-15 {
                break;
            }
        }
        x[i] = z;
        w[i] = 2.0 / ((1.0 - z * z) * pp * pp);
    }
    (x, w)
}

/// Uniform-gas moments at (M, mu, T): (n, S, e_kin, I0+, I0-, I1+, I1-)
/// with 8 internal states, normal ordering, momentum cutoff k_max.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct GasMoments {
    pub n: f64,
    pub s: f64,
    pub energy: f64,
    pub pressure: f64,
}

pub fn gas_moments(m: f64, mu: f64, t: f64, k_max: f64, nodes: usize) -> GasMoments {
    let (x, w) = gauss_legendre(nodes);
    let mut i0p = 0.0;
    let mut i0m = 0.0;
    let mut i1p = 0.0;
    let mut i1m = 0.0;
    let mut e = 0.0;
    let mut p = 0.0;
    for (xi, wi) in x.iter().zip(w.iter()) {
        let k = 0.5 * k_max * (xi + 1.0);
        let dk = 0.5 * k_max * wi;
        let energy = (m * m + k * k).sqrt();
        let (fp, fm) = if t > 0.0 {
            (fermi((energy - mu) / t), fermi((energy + mu) / t))
        } else {
            (
                if energy < mu { 1.0 } else { 0.0 },
                if energy < -mu { 1.0 } else { 0.0 },
            )
        };
        let measure = k * k * dk / (2.0 * PI * PI);
        i0p += fp * measure;
        i0m += fm * measure;
        i1p += fp * m / energy * measure;
        i1m += fm * m / energy * measure;
        e += (fp + fm) * energy * measure;
        p += (fp + fm) * k * k / (3.0 * energy) * measure;
    }
    GasMoments {
        n: 8.0 * (i0p - i0m),
        s: 8.0 * (i1p + i1m),
        energy: 8.0 * e,
        pressure: 8.0 * p,
    }
}

/// Chemical potential of the uniform gas at density n (bisection).
pub fn gas_chemical_potential(m: f64, n: f64, t: f64, k_max: f64, nodes: usize) -> f64 {
    let mut lo = -50.0 * m.max(t).max(1.0);
    let mut hi = 50.0 * m.max(t).max(1.0) + 10.0 * n.abs().cbrt();
    for _ in 0..200 {
        let mid = 0.5 * (lo + hi);
        if gas_moments(m, mid, t, k_max, nodes).n < n {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    0.5 * (lo + hi)
}

/// Numerical check of the trace kernel and of the closed form: returns
/// (max |Tr[BC P_a(k) BC P_b(k')] - 4[1 + ab (M^2 - k.k')/(EE')]|,
///  |Tr(BC rho BC rho)_quadrature - (n^2 + S^2)/16| / ((n^2 + S^2)/16)).
/// The density matrix is built from the full 16x16 projectors at every
/// quadrature node pair with an explicit angular quadrature.
pub fn kernel_check(
    m: f64,
    mu: f64,
    t: f64,
    k_max: f64,
    nodes: usize,
    angles: usize,
) -> (f64, f64) {
    let ops = Operators::new();
    let g: Vec<C16> = crate::GAMMA.iter().map(C16::real).collect();
    let g4g1 = g[4].mul(&g[1]);
    let g4g2 = g[4].mul(&g[2]);
    let minus_i_g4 = g[4].scale(0.0, -1.0);
    let ident = C16::identity();
    let projector = |kx: f64, ky: f64, sign: f64| -> C16 {
        // h = -i M gamma^4 - gamma^4 (gamma^1 kx + gamma^2 ky)
        let h = minus_i_g4
            .scale(m, 0.0)
            .add(&g4g1.scale(-kx, 0.0))
            .add(&g4g2.scale(-ky, 0.0));
        let e = (m * m + kx * kx + ky * ky).sqrt();
        ident.add(&h.scale(sign / e, 0.0)).scale(0.5, 0.0)
    };
    let (x, w) = gauss_legendre(nodes);
    let (xa, wa) = gauss_legendre(angles);
    let mut kernel_defect: f64 = 0.0;
    let mut trace_quadrature = 0.0;
    let mut moments = [[0.0; 2]; 2]; // [a][b]: I0, I1 style sums
    let mut i0 = [0.0; 2];
    let mut i1 = [0.0; 2];
    let occupation = |energy: f64, a: usize| -> f64 {
        if a == 0 {
            fermi((energy - mu) / t)
        } else {
            fermi((energy + mu) / t)
        }
    };
    for (xi, wi) in x.iter().zip(w.iter()) {
        let k = 0.5 * k_max * (xi + 1.0);
        let dk = 0.5 * k_max * wi;
        let e = (m * m + k * k).sqrt();
        let measure = k * k * dk / (2.0 * PI * PI);
        for a in 0..2 {
            let f = occupation(e, a);
            i0[a] += f * measure;
            i1[a] += f * m / e * measure;
        }
        let pa = [projector(k, 0.0, 1.0), projector(k, 0.0, -1.0)];
        for (xj, wj) in x.iter().zip(w.iter()) {
            let kp = 0.5 * k_max * (xj + 1.0);
            let dkp = 0.5 * k_max * wj;
            let ep = (m * m + kp * kp).sqrt();
            let measure_p = kp * kp * dkp / (2.0 * PI * PI);
            for (ca, wc) in xa.iter().zip(wa.iter()) {
                let sa = (1.0 - ca * ca).max(0.0).sqrt();
                let pb = [
                    projector(kp * ca, kp * sa, 1.0),
                    projector(kp * ca, kp * sa, -1.0),
                ];
                for a in 0..2 {
                    for b in 0..2 {
                        let sign = if a == b { 1.0 } else { -1.0 };
                        let tr = ops.bc.mul(&pa[a]).mul(&ops.bc).mul(&pb[b]).trace_re();
                        let expected = 4.0 * (1.0 + sign * (m * m - k * kp * ca) / (e * ep));
                        kernel_defect = kernel_defect.max((tr - expected).abs());
                        let fa = occupation(e, a);
                        let fb = occupation(ep, b);
                        let weight =
                            (if a == 0 { 1.0 } else { -1.0 }) * (if b == 0 { 1.0 } else { -1.0 });
                        trace_quadrature += weight * fa * fb * tr * measure * measure_p * 0.5 * wc;
                        moments[a][b] += 0.0;
                    }
                }
            }
        }
    }
    let n = 8.0 * (i0[0] - i0[1]);
    let s = 8.0 * (i1[0] + i1[1]);
    let closed = (n * n + s * s) / 16.0;
    (kernel_defect, (trace_quadrature - closed).abs() / closed)
}

/// Single-k filled shell: Tr(BC P_+ BC P_+) = (Tr BC P_+)^2 / 8 (design probe).
pub fn filled_shell_check(m: f64, k: f64) -> f64 {
    let ops = Operators::new();
    let g: Vec<C16> = crate::GAMMA.iter().map(C16::real).collect();
    let h = g[4].scale(0.0, -m).add(&g[4].mul(&g[1]).scale(-k, 0.0));
    let e = (m * m + k * k).sqrt();
    let p = C16::identity().add(&h.scale(1.0 / e, 0.0)).scale(0.5, 0.0);
    let s = ops.bc.mul(&p).trace_re();
    let ex = ops.bc.mul(&p).mul(&ops.bc).mul(&p).trace_re();
    (ex - s * s / 8.0).abs()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn gauss_legendre_integrates_polynomials() {
        let (x, w) = gauss_legendre(12);
        let total: f64 = w.iter().sum();
        assert!((total - 2.0).abs() < 1e-14);
        let x4: f64 = x.iter().zip(w.iter()).map(|(x, w)| x.powi(4) * w).sum();
        assert!((x4 - 0.4).abs() < 1e-14);
    }

    #[test]
    fn filled_shell_exchange_is_one_eighth() {
        for k in [0.0, 0.5, 2.0] {
            assert!(filled_shell_check(1.0, k) < 1e-13);
        }
    }

    #[test]
    fn kernel_and_closed_form_hold_at_finite_temperature() {
        let (kernel, closed) = kernel_check(1.0, 1.3, 0.4, 12.0, 20, 8);
        assert!(kernel < 1e-12, "kernel defect {kernel}");
        assert!(closed < 1e-10, "closed-form relative defect {closed}");
    }

    #[test]
    fn potentials_are_derivatives() {
        let (lambda, n, s, h) = (0.7, 1.3, 0.9, 1e-6);
        let dn = (exchange_energy_density(lambda, n + h, s)
            - exchange_energy_density(lambda, n - h, s))
            / (2.0 * h);
        let ds = (exchange_energy_density(lambda, n, s + h)
            - exchange_energy_density(lambda, n, s - h))
            / (2.0 * h);
        assert!((dn - v_vector(lambda, n)).abs() < 1e-9);
        assert!((ds - v_scalar(lambda, s)).abs() < 1e-9);
        assert!((effective_mass(1.0, lambda, s) - (1.0 + 15.0 / 16.0 * lambda * s)).abs() < 1e-15);
    }

    #[test]
    fn gas_chemical_potential_inverts_density() {
        let mu = gas_chemical_potential(1.0, 0.05, 0.3, 40.0, 200);
        let moments = gas_moments(1.0, mu, 0.3, 40.0, 200);
        assert!((moments.n - 0.05).abs() < 1e-9, "{}", moments.n);
        assert!(moments.s > 0.0 && moments.energy > 0.0);
    }
}
