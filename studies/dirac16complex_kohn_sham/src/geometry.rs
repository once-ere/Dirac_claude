//! The static primordial field in the proper hidden coordinate, its
//! curvature, the two extensions beyond y = 0 and the Israel brane stress
//! (STAGE4_SPEC section 1; Stage-2 closed forms with a4 constant).
//!
//! Notebook patch: z = 6 H x0 in (0, pi/2), proper coordinate
//! `y = ln(sin z)/(6H) in (-inf, 0]`, z = pi/2 <-> y = 0.  Warped form
//! (a4 = a4_0 constant, the static member of the primordial family):
//!
//! ```text
//! ds^2 = dy^2 - dx4^2 + e^{2Hy} [ e^{2a4_0} (dx1^2+dx2^2+dx3^2) - e^{-2a4_0} (dx5^2+dx6^2+dx7^2) ]
//! ```
//!
//! Warp W = e^{Hy}; proper 7-volume per coordinate volume W^6 = e^{6Hy};
//! the transverse space pinches off at the tip y -> -inf (z -> 0).
//!
//! Curvature (order y, x1, x2, x3, x4, x5, x6, x7): R = -42 H^2,
//! G^mu_nu = diag(15, 15, 15, 15, 21, 15, 15, 15) H^2, so 8D Einstein gravity
//! `G^mu_nu = kappa T^mu_nu` needs `rho_req = -T^4_4 = -21 H^2/kappa < 0` and
//! transverse pressures `p_req = T^i_i = +15 H^2/kappa` (all seven).  These
//! are the Stage-2 closed forms at a4' = a4'' = 0 and are re-derived here
//! numerically ([`curvature_check`]) from the Christoffel symbols of the
//! diagonal warped metric with a 4th-order finite difference for the one
//! derivative that the closed-form Christoffels do not remove.
//!
//! Extrinsic curvature of y = const (unit normal d_y): K_ij = (1/2) d_y g_ij,
//! `K^i_j = H delta^i_j` on the six warped directions, 0 on x4, trace 6H.
//!
//! Extensions beyond y = 0:
//!  (E1) smooth: W = e^{Hy} for all real y (the Stage-2 zeta chart continued);
//!  (E2) Z2 mirror ("pair of universes"): W = e^{-H|y|}, a brane at y = 0.
//!      Israel junction with the convention `S^i_j = -(1/kappa)([K^i_j] -
//!      delta^i_j [K])`, `[X] = X(0+) - X(0-)`, normal pointing from the
//!      y < 0 side to the y > 0 side: [K^i_j] = -2H (warped), 0 (x4),
//!      [K] = -12H, hence `S^mu_nu = -(H/kappa) diag(10,10,10,12,10,10,10)` on
//!      (x1,x2,x3,x4,x5,x6,x7): brane energy density `rho_b = -S^4_4 =
//!      +12H/kappa` (positive tension) and brane pressures `-10H/kappa`.
//!      Structural remark (not physical): the gamma^8 map sends
//!      L_{m,U} -> -L_{-m,-U} (CONTRACT errata E2), so a mirror copy carrying
//!      gamma^8 Psi has mass -m: the notebook's "+-M pair".

use crate::math::{asin, exp, log};
use crate::output::Json;

/// Warp factor on the notebook patch and its smooth extension E1.
pub fn warp_e1(h: f64, y: f64) -> f64 {
    exp(h * y)
}

/// Warp factor of the Z2 extension E2.
pub fn warp_e2(h: f64, y: f64) -> f64 {
    exp(-h * y.abs())
}

/// kappa(y) = e^{-Hy - a4_0}: the factor multiplying the 3-momentum.
pub fn kappa(h: f64, a4: f64, y: f64) -> f64 {
    exp(-h * y - a4)
}

/// Proper 7-volume per coordinate volume, W^6 = e^{6Hy}.
pub fn volume_factor(h: f64, y: f64) -> f64 {
    exp(6.0 * h * y)
}

/// The inverse factor e^{-6Hy} that turns coordinate densities into proper ones.
pub fn density_factor(h: f64, y: f64) -> f64 {
    exp(-6.0 * h * y)
}

/// z(y) = arcsin(e^{6Hy}) on the notebook patch.
pub fn z_of_y(h: f64, y: f64) -> f64 {
    asin(exp(6.0 * h * y).min(1.0))
}

/// y(z) = ln(sin z)/(6H).
pub fn y_of_z(h: f64, z: f64) -> f64 {
    log(crate::math::sin(z)) / (6.0 * h)
}

/// Closed-form curvature numbers (H = h).
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Curvature {
    pub ricci_scalar: f64,
    /// G^mu_nu, order y, x1, x2, x3, x4, x5, x6, x7.
    pub einstein_mixed: [f64; 8],
    /// rho_req = -G^4_4 / kappa (kappa = 1).
    pub rho_required: f64,
    /// p_req,i = G^i_i / kappa for the seven transverse directions (order y,1,2,3,5,6,7).
    pub p_required: [f64; 7],
    /// Extrinsic curvature K^i_j of y = const (order x1,x2,x3,x4,x5,x6,x7).
    pub extrinsic: [f64; 7],
    /// Israel brane stress S^mu_nu of E2 (order x1,x2,x3,x4,x5,x6,x7), kappa = 1.
    pub brane_stress: [f64; 7],
}

pub fn curvature_closed_form(h: f64) -> Curvature {
    let h2 = h * h;
    let g = [15.0 * h2, 15.0 * h2, 15.0 * h2, 15.0 * h2, 21.0 * h2, 15.0 * h2, 15.0 * h2, 15.0 * h2];
    Curvature {
        ricci_scalar: -42.0 * h2,
        einstein_mixed: g,
        rho_required: -g[4],
        p_required: [g[0], g[1], g[2], g[3], g[5], g[6], g[7]],
        extrinsic: [h, h, h, 0.0, h, h, h],
        brane_stress: [-10.0 * h, -10.0 * h, -10.0 * h, -12.0 * h, -10.0 * h, -10.0 * h, -10.0 * h],
    }
}

/// Diagonal metric of the warped form, g_mu(y) for mu = 0..7 (0 = y).
fn metric_diag(h: f64, a4: f64, y: f64) -> [f64; 8] {
    let w2 = exp(2.0 * h * y);
    let s = w2 * exp(2.0 * a4);
    let t = -w2 * exp(-2.0 * a4);
    [1.0, s, s, s, -1.0, t, t, t]
}

/// Christoffel symbols Gamma^r_{mn} of a diagonal metric depending on y only,
/// with the exact derivative d_y g_mu = 2 H g_mu for the warped entries.
fn christoffel(h: f64, a4: f64, y: f64) -> [[[f64; 8]; 8]; 8] {
    let g = metric_diag(h, a4, y);
    let mut dg = [0.0; 8];
    for (mu, value) in dg.iter_mut().enumerate() {
        *value = if mu == 0 || mu == 4 { 0.0 } else { 2.0 * h * g[mu] };
    }
    let mut gamma = [[[0.0; 8]; 8]; 8];
    for i in 0..8 {
        // Gamma^0_{ii} = -(1/2) g^{00} d_y g_ii ; Gamma^i_{i0} = Gamma^i_{0i} = (1/2) g^{ii} d_y g_ii
        gamma[0][i][i] = -0.5 * dg[i] / g[0];
        if i != 0 {
            gamma[i][i][0] = 0.5 * dg[i] / g[i];
            gamma[i][0][i] = gamma[i][i][0];
        }
    }
    gamma
}

/// Numerical Ricci tensor (mixed R^mu_nu), Ricci scalar and mixed Einstein
/// tensor at y for the warped metric; the y-derivative of the Christoffel
/// symbols is a 4th-order central difference with step `dy`.
pub fn curvature_numerical(h: f64, a4: f64, y: f64, dy: f64) -> (f64, [f64; 8]) {
    let g = metric_diag(h, a4, y);
    let gam = christoffel(h, a4, y);
    let gp = christoffel(h, a4, y + dy);
    let gm = christoffel(h, a4, y - dy);
    let gp2 = christoffel(h, a4, y + 2.0 * dy);
    let gm2 = christoffel(h, a4, y - 2.0 * dy);
    let d = |r: usize, m: usize, n: usize| {
        (-gp2[r][m][n] + 8.0 * gp[r][m][n] - 8.0 * gm[r][m][n] + gm2[r][m][n]) / (12.0 * dy)
    };
    // R_{mn} = d_r Gamma^r_{mn} - d_n Gamma^r_{mr} + Gamma^r_{rl} Gamma^l_{mn} - Gamma^r_{nl} Gamma^l_{mr}
    let mut ricci = [[0.0; 8]; 8];
    for m in 0..8 {
        for n in 0..8 {
            let mut value = 0.0;
            // only d_y (index 0) derivatives are nonzero
            value += d(0, m, n);
            if n == 0 {
                for r in 0..8 {
                    value -= d(r, m, r);
                }
            }
            for r in 0..8 {
                for l in 0..8 {
                    value += gam[r][r][l] * gam[l][m][n] - gam[r][n][l] * gam[l][m][r];
                }
            }
            ricci[m][n] = value;
        }
    }
    let mut mixed = [0.0; 8];
    for (m, value) in mixed.iter_mut().enumerate() {
        *value = ricci[m][m] / g[m];
    }
    let scalar: f64 = mixed.iter().sum();
    let mut einstein = [0.0; 8];
    for (m, value) in einstein.iter_mut().enumerate() {
        *value = mixed[m] - 0.5 * scalar;
    }
    (scalar, einstein)
}

/// Max deviation between the numerical curvature at a few y and the closed form.
pub fn curvature_check(h: f64, a4: f64) -> f64 {
    let closed = curvature_closed_form(h);
    let mut worst: f64 = 0.0;
    for y in [-3.0, -1.5, -0.25, 0.0] {
        let (scalar, einstein) = curvature_numerical(h, a4, y, 1.0e-3);
        worst = worst.max((scalar - closed.ricci_scalar).abs());
        for (a, b) in einstein.iter().zip(closed.einstein_mixed.iter()) {
            worst = worst.max((a - b).abs());
        }
    }
    worst
}

/// Extrinsic curvature K^i_j = (1/2) g^{ii} d_y g_ii of y = const, numerically.
pub fn extrinsic_numerical(h: f64, a4: f64, y: f64, dy: f64) -> [f64; 7] {
    let gp = metric_diag(h, a4, y + dy);
    let gm = metric_diag(h, a4, y - dy);
    let g = metric_diag(h, a4, y);
    let mut out = [0.0; 7];
    for (slot, mu) in [1usize, 2, 3, 4, 5, 6, 7].iter().enumerate() {
        out[slot] = 0.5 * (gp[*mu] - gm[*mu]) / (2.0 * dy) / g[*mu];
    }
    out
}

/// Israel stress from the jump of K across the Z2 brane (E2), kappa = 1.
pub fn brane_stress_from_jump(k_minus: &[f64; 7]) -> [f64; 7] {
    // K(0+) = -K(0-) for the mirror W = e^{-H|y|}: [K^i_j] = -2 K^i_j(0-).
    let jump: Vec<f64> = k_minus.iter().map(|k| -2.0 * k).collect();
    let trace: f64 = jump.iter().sum();
    let mut s = [0.0; 7];
    for i in 0..7 {
        s[i] = -(jump[i] - trace);
    }
    s
}

/// JSON summary of the geometry (closed forms, checks).
pub fn geometry_json(h: f64, a4: f64) -> Json {
    let closed = curvature_closed_form(h);
    let defect = curvature_check(h, a4);
    let k_num = extrinsic_numerical(h, a4, -0.7, 1.0e-4);
    let s_num = brane_stress_from_jump(&closed.extrinsic);
    let k_defect = k_num
        .iter()
        .zip(closed.extrinsic.iter())
        .map(|(a, b)| (a - b).abs())
        .fold(0.0, f64::max);
    let s_defect = s_num
        .iter()
        .zip(closed.brane_stress.iter())
        .map(|(a, b)| (a - b).abs())
        .fold(0.0, f64::max);
    Json::object(vec![
        ("coordinate", Json::str("y = ln(sin z)/(6H) in (-inf, 0]; z = 6 H x0; y = 0 is the brane (z = pi/2)")),
        ("metric", Json::str("ds^2 = dy^2 - dx4^2 + e^{2Hy}[e^{2a4_0}(dx1^2+dx2^2+dx3^2) - e^{-2a4_0}(dx5^2+dx6^2+dx7^2)]")),
        ("warp", Json::str("W = e^{Hy}; proper 7-volume per coordinate volume W^6 = e^{6Hy}; kappa(y) = e^{-Hy-a4_0}")),
        ("H", Json::Float(h)),
        ("a4_0", Json::Float(a4)),
        ("ricciScalar", Json::Float(closed.ricci_scalar)),
        ("einsteinMixed_y_x1_x2_x3_x4_x5_x6_x7", Json::floats(&closed.einstein_mixed)),
        ("rhoRequired_kappa1", Json::Float(closed.rho_required)),
        ("pRequired_kappa1_y_x1_x2_x3_x5_x6_x7", Json::floats(&closed.p_required)),
        ("curvatureNumericalDefect", Json::Float(defect)),
        ("extrinsicK_x1_x2_x3_x4_x5_x6_x7", Json::floats(&closed.extrinsic)),
        ("extrinsicNumericalDefect", Json::Float(k_defect)),
        ("extensionE1", Json::str("smooth: W = e^{Hy} for all y")),
        ("extensionE2", Json::str("Z2 mirror: W = e^{-H|y|}, brane at y = 0; Israel S^i_j = -(1/kappa)([K^i_j] - delta^i_j [K]), [X] = X(0+) - X(0-), normal from y<0 to y>0")),
        ("braneStress_kappa1_x1_x2_x3_x4_x5_x6_x7", Json::floats(&closed.brane_stress)),
        ("braneStressFromJumpDefect", Json::Float(s_defect)),
        ("braneEnergyDensity_kappa1", Json::Float(-closed.brane_stress[3])),
        ("gamma8Remark", Json::str("structural, not physical: Psi -> gamma^8 Psi maps L_{m,U} to -L_{-m,-U}; a mirror copy carrying gamma^8 Psi has mass -m (the notebook's +-M pair)")),
    ])
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn curvature_matches_closed_forms() {
        for a4 in [0.0, 0.5] {
            assert!(curvature_check(1.0, a4) < 1e-7, "{}", curvature_check(1.0, a4));
        }
        let c = curvature_closed_form(1.0);
        assert_eq!(c.rho_required, -21.0);
        assert!(c.p_required.iter().all(|p| *p == 15.0));
        let k = extrinsic_numerical(1.0, 0.3, -1.0, 1e-4);
        for (a, b) in k.iter().zip(c.extrinsic.iter()) {
            assert!((a - b).abs() < 1e-7);
        }
        let s = brane_stress_from_jump(&c.extrinsic);
        assert_eq!(s, c.brane_stress);
        assert_eq!(-s[3], 12.0);
    }

    #[test]
    fn coordinate_maps_are_inverse() {
        for y in [-3.0, -1.0, -0.1, 0.0] {
            let z = z_of_y(1.0, y);
            assert!((y_of_z(1.0, z) - y).abs() < 1e-12);
        }
        assert!((z_of_y(1.0, 0.0) - std::f64::consts::FRAC_PI_2).abs() < 1e-15);
        assert_eq!(warp_e2(1.0, 0.5), warp_e2(1.0, -0.5));
        assert_eq!(warp_e1(1.0, -0.5), warp_e2(1.0, -0.5));
    }
}
