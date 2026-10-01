//! The test metric (exactly as given by the author, coordinates x1..x8 stored at
//! indices 0..7) and its curvature, computed exactly.
//!
//!   g = diag( E^(2 a4[x4]) Sin[6 H x8]^(1/3)  (x1, x2, x3),
//!             -1                              (x4),
//!             -E^(-2 a4[x4]) Sin[6 H x8]^(1/3) (x5, x6, x7),
//!             Cot[6 H x8]^2                   (x8) )
//!
//! Conventions (stated once, used everywhere):
//!   Christoffel  Γ^a_{bc} = (1/2) g^{ad} (∂_b g_dc + ∂_c g_db - ∂_d g_bc)
//!   Riemann      R^a_{bcd} = ∂_c Γ^a_{db} - ∂_d Γ^a_{cb} + Γ^a_{ce} Γ^e_{db} - Γ^a_{de} Γ^e_{cb}
//!                (Misner-Thorne-Wheeler; a 2-sphere of radius r has R^{12}_{12} = +1/r^2)
//!   R^{ab}_{cd} = g^{be} R^a_{ecd},  Ricci R_{bd} = R^a_{bad},  R = g^{bd} R_{bd} = R^{ab}_{ab}.

use crate::poly::{Poly, CV, EV, NVAR, SV};
use crate::rational::Rational;

pub const DIM: usize = 8;

/// Coordinate names of the test metric, index 0..7.
pub const COORD: [&str; DIM] = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"];

fn mono(c: i128, e: i32, s: i32, cot: i32) -> Poly {
    let mut m = [0; NVAR];
    m[EV] = e;
    m[SV] = s;
    m[CV] = cot;
    Poly::monomial(Rational::int(c), m)
}

/// The diagonal of the test metric.
pub fn metric_diagonal() -> Vec<Poly> {
    let mut g = Vec::with_capacity(DIM);
    for _ in 0..3 {
        g.push(mono(1, 2, 1, 0)); // E^(2 a4) Sin^(1/3)
    }
    g.push(Poly::int(-1)); // x4
    for _ in 0..3 {
        g.push(mono(-1, -2, 1, 0)); // -E^(-2 a4) Sin^(1/3)
    }
    g.push(mono(1, 0, 0, 2)); // Cot^2
    g
}

pub struct Geometry {
    /// g_aa
    pub g: Vec<Poly>,
    /// g^aa
    pub ginv: Vec<Poly>,
    /// sqrt|det g| = Sin * Cot = S^3 C
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
        // det g = product of the diagonal; |det g| = S^6 C^2, sqrt = S^3 C
        let mut det = Poly::int(1);
        for x in &g {
            det = &det * x;
        }
        let sqrt_g = mono(1, 0, 3, 1);
        assert_eq!(&sqrt_g * &sqrt_g, det, "det g must equal (S^3 C)^2");

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

    /// Christoffel symbols agree with finite differences of the metric.
    #[test]
    fn christoffel_numerical() {
        let geo = Geometry::new();
        let q = Point { h: 0.4, a4: 0.3, a1: 0.7, a2: -0.2, a3: 0.1, a4d4: 0.0, x8: 0.31 };
        // Γ^8_{88} = (1/2) g^88 ∂_8 g_88 by hand: g_88 = cot^2 z, z = 6 H x8
        let z = 6.0 * q.h * q.x8;
        let expect = 0.5 * (z.sin() / z.cos()).powi(2) * (2.0 * (z.cos() / z.sin()) * (-1.0 / z.sin().powi(2)) * 6.0 * q.h);
        assert!((geo.christoffel[7][7][7].eval(&q) - expect).abs() < 1e-12 * expect.abs().max(1.0));
    }
}
