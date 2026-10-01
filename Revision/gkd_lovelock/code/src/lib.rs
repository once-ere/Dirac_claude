//! lovelock_gkd: the generalized Kronecker delta GKD (a pure-Rust refactoring of the
//! author's Wolfram Language kδ) and the exact Lovelock tensors of equation (4.38)
//! for the author's 8-dimensional test metric. No dependencies, no external algebra
//! system: exact rational Laurent polynomials (poly.rs), exact derivatives, exact
//! curvature (geometry.rs), GKD (gkd.rs), the Lovelock sums (lovelock.rs).

// Tensor formulas read best with explicit index loops (a, b, c, d over the 8 coordinates).
#![allow(clippy::needless_range_loop)]

pub mod geometry;
pub mod gkd;
pub mod lovelock;
pub mod output;
pub mod poly;
pub mod rational;
