//! The test metric, in the author's coordinates x0..x7 stored at indices 0..7 (x0 = the hidden,
//! space-like direction first; x4 = the time), and its curvature, computed exactly.  Since 2026-10-16
//! it is the corrected primordial metric (version 2; Revision/SPEC.md section 1, Revision/metric_warped/):
//!
//!   g = diag( E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2              (x0),
//!             E^(2 a4[x4])                                   (x1, x2, x3),
//!             -1                                             (x4),
//!             -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6)    (x5, x6, x7) )
//!
//! for general a4(x4), b4(x4) > 0 and EVERY real z = 6 H x0 with Sin z Cos z != 0 (the positive
//! branch of (Sin^2)^(1/6)).  The metric of 2026-10-14 (g00 = Cot^2, g_ii = E^(2 a4) Sin^(1/3), g_tt =
//! -E^(-2 a4) b4 Sin^(1/3), on 0 < z < pi/2) is withdrawn; its results are frozen in
//! Revision/gkd_lovelock/reference_2026_10_14/.  (Until 2026-10-14 this program used the withdrawn labels
//! x1..x8 with the hidden direction x8 stored last.)  b4 is carried as Q = b4^(1/2), see poly.rs.
//!
//! Conventions (stated once, used everywhere):
//!   Christoffel  Γ^a_{bc} = (1/2) g^{ad} (∂_b g_dc + ∂_c g_db - ∂_d g_bc)
//!   Riemann      R^a_{bcd} = ∂_c Γ^a_{db} - ∂_d Γ^a_{cb} + Γ^a_{ce} Γ^e_{db} - Γ^a_{de} Γ^e_{cb}
//!                (Misner-Thorne-Wheeler; a 2-sphere of radius r has R^{12}_{12} = +1/r^2)
//!   R^{ab}_{cd} = g^{be} R^a_{ecd},  Ricci R_{bd} = R^a_{bad},  R = g^{bd} R_{bd} = R^{ab}_{ab}.

use crate::poly::{Poly, CV, EV, GV, NVAR, QV, WV};
use crate::rational::Rational;

pub const DIM: usize = 8;

/// Coordinate names of the test metric (the author's), index k = xk.
pub const COORD: [&str; DIM] = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"];

/// c E^e W^w C^cot Q^q G^sg
fn mono(c: i128, e: i32, w: i32, cot: i32, q: i32, sg: i32) -> Poly {
    let mut m = [0; NVAR];
    m[EV] = e;
    m[WV] = w;
    m[CV] = cot;
    m[QV] = q;
    m[GV] = sg;
    Poly::monomial(Rational::int(c), m)
}

/// The diagonal of the test metric.
pub fn metric_diagonal() -> Vec<Poly> {
    let mut g = Vec::with_capacity(DIM);
    g.push(mono(1, -2, 0, 2, 2, 0)); // x0: E^(-2 a4) b4 Cot^2, b4 = Q^2
    for _ in 0..3 {
        g.push(mono(1, 2, 0, 0, 0, 0)); // x1, x2, x3: E^(2 a4)
    }
    g.push(Poly::int(-1)); // x4
    for _ in 0..3 {
        g.push(mono(-1, -2, 2, 0, 2, 0)); // x5, x6, x7: -E^(-2 a4) b4 (Sin^2)^(1/6) = -E^-2 Q^2 W^2
    }
    g
}

pub struct Geometry {
    /// g_aa
    pub g: Vec<Poly>,
    /// g^aa
    pub ginv: Vec<Poly>,
    /// sqrt|det g| = E^-a4 b4^2 |Cot| (Sin^2)^(1/4) = G C E^-1 Q^4 W^3
    pub sqrt_g: Poly,
    /// Γ^a_{bc}, index [a][b][c]
    pub christoffel: Vec<Vec<Vec<Poly>>>,
    /// R^a_{bcd}, index [a][b][c][d]
    pub riemann: Vec<Vec<Vec<Vec<Poly>>>>,
    /// R^{ab}_{cd}, index [a][b][c][d]
    pub riemann_mixed: Vec<Vec<Vec<Vec<Poly>>>>,
    /// R^a_b (mixed Ricci), index [a][b]
    pub ricci_mixed: Vec<Vec<Poly>>,
    /// R
    pub ricci_scalar: Poly,
}

impl Geometry {
    pub fn new() -> Geometry {
        let g = metric_diagonal();
        let ginv: Vec<Poly> = g.iter().map(|x| x.monomial_inverse()).collect();
        // det g = product of the diagonal = E^-2 Q^8 W^6 C^2 > 0 (four negative entries);
        // sqrt|det g| = G C E^-1 Q^4 W^3 (G C = |Cot|), and (G C E^-1 Q^4 W^3)^2 = det g because G^2 = 1
        let mut det = Poly::int(1);
        for x in &g {
            det = &det * x;
        }
        let sqrt_g = mono(1, -1, 3, 1, 4, 1);
        assert_eq!(&sqrt_g * &sqrt_g, det, "det g must equal (G C E^-1 Q^4 W^3)^2");

        // derivatives of the metric: dg[c][a] = ∂_c g_aa
        let dg: Vec<Vec<Poly>> = (0..DIM).map(|c| g.iter().map(|x| x.d(c)).collect()).collect();
        let mut chr = vec![vec![vec![Poly::zero(); DIM]; DIM]; DIM];
        for a in 0..DIM {
            for b in 0..DIM {
                for c in 0..DIM {
                    // Γ^a_{bc} = 1/2 g^{aa} (∂_b g_ac + ∂_c g_ab - ∂_a g_bc), diagonal g
                    let mut s = Poly::zero();
                    if a == c {
                        s = &s + &dg[b][a];
                    }
                    if a == b {
                        s = &s + &dg[c][a];
                    }
                    if b == c {
                        s = &s - &dg[a][b];
                    }
                    if !s.is_zero() {
                        chr[a][b][c] = (&ginv[a] * &s).scale(Rational::new(1, 2));
                    }
                }
            }
        }
        // R^a_{bcd} = ∂_c Γ^a_{db} - ∂_d Γ^a_{cb} + Γ^a_{ce} Γ^e_{db} - Γ^a_{de} Γ^e_{cb}
        let mut riem = vec![vec![vec![vec![Poly::zero(); DIM]; DIM]; DIM]; DIM];
        for a in 0..DIM {
            for b in 0..DIM {
                for c in 0..DIM {
                    for d in 0..DIM {
                        let mut s = &chr[a][d][b].d(c) - &chr[a][c][b].d(d);
                        for e in 0..DIM {
                            if !chr[a][c][e].is_zero() && !chr[e][d][b].is_zero() {
                                s = &s + &(&chr[a][c][e] * &chr[e][d][b]);
                            }
                            if !chr[a][d][e].is_zero() && !chr[e][c][b].is_zero() {
                                s = &s - &(&chr[a][d][e] * &chr[e][c][b]);
                            }
                        }
                        riem[a][b][c][d] = s;
                    }
                }
            }
        }
        // R^{ab}_{cd} = g^{bb} R^a_{bcd} (diagonal metric)
        let mut mixed = vec![vec![vec![vec![Poly::zero(); DIM]; DIM]; DIM]; DIM];
        for a in 0..DIM {
            for b in 0..DIM {
                for c in 0..DIM {
                    for d in 0..DIM {
                        if !riem[a][b][c][d].is_zero() {
                            mixed[a][b][c][d] = &ginv[b] * &riem[a][b][c][d];
                        }
                    }
                }
            }
        }
        // R^a_b = R^{ac}_{bc}
        let mut ricci_mixed = vec![vec![Poly::zero(); DIM]; DIM];
        for a in 0..DIM {
            for b in 0..DIM {
                let mut s = Poly::zero();
                for c in 0..DIM {
                    s = &s + &mixed[a][c][b][c];
                }
                ricci_mixed[a][b] = s;
            }
        }
        let mut ricci_scalar = Poly::zero();
        for a in 0..DIM {
            ricci_scalar = &ricci_scalar + &ricci_mixed[a][a];
        }
        Geometry { g, ginv, sqrt_g, christoffel: chr, riemann: riem, riemann_mixed: mixed, ricci_mixed, ricci_scalar }
    }

    /// Nonzero entries of R^{ab}_{cd}: (a, b, c, d) with the value.
    pub fn nonzero_mixed(&self) -> Vec<(usize, usize, usize, usize, Poly)> {
        let mut out = Vec::new();
        for a in 0..DIM {
            for b in 0..DIM {
                for c in 0..DIM {
                    for d in 0..DIM {
                        let v = &self.riemann_mixed[a][b][c][d];
                        if !v.is_zero() {
                            out.push((a, b, c, d, v.clone()));
                        }
                    }
                }
            }
        }
        out
    }

    /// Mixed Einstein tensor G^a_b = R^a_b - 1/2 δ^a_b R.
    pub fn einstein_mixed(&self) -> Vec<Vec<Poly>> {
        let mut gm = vec![vec![Poly::zero(); DIM]; DIM];
        for a in 0..DIM {
            for b in 0..DIM {
                let mut v = self.ricci_mixed[a][b].clone();
                if a == b {
                    v = &v - &self.ricci_scalar.scale(Rational::new(1, 2));
                }
                gm[a][b] = v;
            }
        }
        gm
    }
}

impl Default for Geometry {
    fn default() -> Self {
        Geometry::new()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::poly::Point;

    /// The symmetries of the Riemann tensor hold exactly.
    #[test]
    fn riemann_symmetries() {
        let geo = Geometry::new();
        for a in 0..DIM {
            for b in 0..DIM {
                for c in 0..DIM {
                    for d in 0..DIM {
                        let r = &geo.riemann_mixed[a][b][c][d];
                        assert_eq!(*r, -&geo.riemann_mixed[b][a][c][d]);
                        assert_eq!(*r, -&geo.riemann_mixed[a][b][d][c]);
                        // first Bianchi identity R^a_{[bcd]} = 0
                        let s = &(&geo.riemann[a][b][c][d] + &geo.riemann[a][c][d][b]) + &geo.riemann[a][d][b][c];
                        assert!(s.is_zero());
                    }
                }
            }
        }
    }

    /// Christoffel symbols agree with the metric written out by hand and with finite differences,
    /// and sqrt_g is the positive root of |det g|, in all four quarters of the period of z = 6 H x0.
    #[test]
    fn christoffel_numerical() {
        let geo = Geometry::new();
        // H = 0.4: z = 0.744, 2.64, 3.84, 5.76 (Sin, Cot) = (+, +), (+, -), (-, +), (-, -)
        for x0 in [0.31, 1.1, 1.6, 2.4] {
            let q = Point { h: 0.4, a4: 0.3, a1: 0.7, a2: -0.2, a3: 0.1, a4d4: 0.0, b4: 1.3, b1: 0.25, b2: -0.15, b3: 0.0, b4d4: 0.0, x0 };
            let z = 6.0 * q.h * q.x0;
            let pre = (-2.0 * q.a4).exp() * q.b4;
            // the metric written out by hand: g_00 = e^(-2 a4) b4 cot^2 z, g_55 = -e^(-2 a4) b4 (sin^2 z)^(1/6)
            let g00 = |x: f64| pre * ((6.0 * q.h * x).cos() / (6.0 * q.h * x).sin()).powi(2);
            let g55 = |x: f64| -pre * ((6.0 * q.h * x).sin().powi(2)).powf(1.0 / 6.0);
            assert!((geo.g[0].eval(&q) - g00(x0)).abs() < 1e-12 * g00(x0).abs());
            assert!((geo.g[5].eval(&q) - g55(x0)).abs() < 1e-12 * g55(x0).abs());
            // Γ^0_{00} = (1/2) g^00 ∂_0 g_00 = -6 H / (sin z cos z), by hand
            let expect = -6.0 * q.h / (z.sin() * z.cos());
            assert!((geo.christoffel[0][0][0].eval(&q) - expect).abs() < 1e-12 * expect.abs().max(1.0));
            // Γ^0_{55} = -(1/2) g^00 ∂_0 g_55, ∂_0 by central finite differences of the hand-written metric
            let e = 1e-6;
            let fd = -0.5 / g00(x0) * (g55(x0 + e) - g55(x0 - e)) / (2.0 * e);
            assert!((geo.christoffel[0][5][5].eval(&q) - fd).abs() < 1e-6 * fd.abs().max(1.0));
            // sqrt_g > 0 and sqrt_g^2 = |det g|
            let det: f64 = geo.g.iter().map(|x| x.eval(&q)).product();
            let s = geo.sqrt_g.eval(&q);
            assert!(s > 0.0 && (s - det.abs().sqrt()).abs() < 1e-12 * s);
        }
    }
}
