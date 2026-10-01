//! The Lovelock tensors of equation (4.38) (the author's In[68]), computed with GKD.
//!
//!   A^{lh} = sqrt(g) sum_{k=1}^{m-1} α_(k) g^{jl} δ^{h h1 ... h2k}_{j j1 ... j2k}
//!            R^{j1 j2}_{h1 h2} ... R^{j(2k-1) j2k}_{h(2k-1) h2k}  +  λ sqrt(g) g^{lh},
//!   m = n/2 for even n.  For n = 8: m = 4, k = 1, 2, 3: three non-zero tensors
//!
//!   A_(k)^{lh} = sqrt(g) g^{jl} P_(k)^h_j,
//!   P_(k)^h_j  = δ^{h h1 ... h2k}_{j j1 ... j2k} R^{j1 j2}_{h1 h2} ... R^{j(2k-1) j2k}_{h(2k-1) h2k}
//!              = sum GKD([j, j1, ..., j2k], [h, h1, ..., h2k]) prod_i R^{j(2i-1) j2i}_{h(2i-1) h2i}.
//!
//! The sum runs over the nonzero entries of R^{ab}_{cd} only (a vanishing factor gives a
//! vanishing term) and skips index lists with a repeated index (where GKD is 0 by the
//! determinant argument of gkd.rs); every term that remains is weighted by an explicit
//! call of GKD.  L_(k) = δ^{h1 ... h2k}_{j1 ... j2k} R ... R is the k-th Lovelock scalar.

use crate::geometry::{Geometry, DIM};
use crate::gkd::GKD;
use crate::poly::{Point, Poly};
use crate::rational::Rational;

pub struct Counters {
    pub gkd_calls: u64,
    pub gkd_nonzero: u64,
    pub leaves: u64,
}

/// P_(k)^h_j for all h, j (index [h][j]) and the counters of the GKD calls.
pub fn lovelock_mixed(geo: &Geometry, k: usize) -> (Vec<Vec<Poly>>, Counters) {
    let entries = geo.nonzero_mixed();
    let mut counters = Counters { gkd_calls: 0, gkd_nonzero: 0, leaves: 0 };
    let mut p = vec![vec![Poly::zero(); DIM]; DIM];
    for h in 0..DIM {
        for j in 0..DIM {
            let mut lower = vec![j];
            let mut upper = vec![h];
            let mut chosen: Vec<usize> = Vec::new();
            let mut acc = Poly::zero();
            dfs(&entries, k, 1 << j, 1 << h, &mut lower, &mut upper, &mut chosen, &mut acc, &mut counters);
            p[h][j] = acc;
        }
    }
    (p, counters)
}

/// L_(k) = δ^{h1..h2k}_{j1..j2k} R^{j1j2}_{h1h2} ... (the Lovelock scalar).
pub fn lovelock_scalar(geo: &Geometry, k: usize) -> (Poly, Counters) {
    let entries = geo.nonzero_mixed();
    let mut counters = Counters { gkd_calls: 0, gkd_nonzero: 0, leaves: 0 };
    let mut lower = Vec::new();
    let mut upper = Vec::new();
    let mut chosen = Vec::new();
    let mut acc = Poly::zero();
    dfs(&entries, k, 0, 0, &mut lower, &mut upper, &mut chosen, &mut acc, &mut counters);
    (acc, counters)
}

#[allow(clippy::too_many_arguments)]
fn dfs(
    entries: &[(usize, usize, usize, usize, Poly)],
    remaining: usize,
    lower_mask: u64,
    upper_mask: u64,
    lower: &mut Vec<usize>,
    upper: &mut Vec<usize>,
    chosen: &mut Vec<usize>,
    acc: &mut Poly,
    counters: &mut Counters,
) {
    if remaining == 0 {
        counters.leaves += 1;
        if lower_mask != upper_mask {
            return; // the two index sets differ: GKD = 0 (case c of gkd.rs)
        }
        counters.gkd_calls += 1;
        let s = GKD(lower, upper);
        if s == 0 {
            return;
        }
        counters.gkd_nonzero += 1;
        let mut prod = Poly::int(s as i128);
        for &e in chosen.iter() {
            prod = &prod * &entries[e].4;
        }
        *acc = &*acc + &prod;
        return;
    }
    for (idx, (a, b, c, d, _)) in entries.iter().enumerate() {
        let (a, b, c, d) = (*a, *b, *c, *d);
        // R^{ab}_{cd}: a, b join the lower row of δ, c, d the upper row
        let lb = (1u64 << a) | (1u64 << b);
        let ub = (1u64 << c) | (1u64 << d);
        if lower_mask & lb != 0 || upper_mask & ub != 0 {
            continue; // repeated index in a row: GKD = 0 (cases a, b)
        }
        lower.push(a);
        lower.push(b);
        upper.push(c);
        upper.push(d);
        chosen.push(idx);
        dfs(entries, remaining - 1, lower_mask | lb, upper_mask | ub, lower, upper, chosen, acc, counters);
        chosen.pop();
        upper.pop();
        upper.pop();
        lower.pop();
        lower.pop();
    }
}

/// A_(k)^{lh} = sqrt(g) g^{ll} P_(k)^h_l (index [l][h]).
pub fn lovelock_contravariant(geo: &Geometry, p: &[Vec<Poly>]) -> Vec<Vec<Poly>> {
    let mut a = vec![vec![Poly::zero(); DIM]; DIM];
    for l in 0..DIM {
        for h in 0..DIM {
            if !p[h][l].is_zero() {
                a[l][h] = &(&geo.sqrt_g * &geo.ginv[l]) * &p[h][l];
            }
        }
    }
    a
}

/// Covariant divergence ∇_h P^h_j = ∂_h P^h_j + Γ^h_{hm} P^m_j - Γ^m_{hj} P^h_m (index j).
pub fn divergence(geo: &Geometry, p: &[Vec<Poly>]) -> Vec<Poly> {
    let mut out = vec![Poly::zero(); DIM];
    for j in 0..DIM {
        let mut s = Poly::zero();
        for h in 0..DIM {
            s = &s + &p[h][j].d(h);
            for m in 0..DIM {
                if !geo.christoffel[h][h][m].is_zero() && !p[m][j].is_zero() {
                    s = &s + &(&geo.christoffel[h][h][m] * &p[m][j]);
                }
                if !geo.christoffel[m][h][j].is_zero() && !p[h][m].is_zero() {
                    s = &s - &(&geo.christoffel[m][h][j] * &p[h][m]);
                }
            }
        }
        out[j] = s;
    }
    out
}

/// Brute force at a numerical point: the literal sum over ALL index lists
/// (h1..h2k, j1..j2k in 0..7, 8^(4k) terms per component) with GKD as the weight,
/// without any pruning. Used to check the pruned exact sum for k = 1 and k = 2.
pub fn brute_force_numeric(geo: &Geometry, k: usize, q: &Point) -> (Vec<Vec<f64>>, u64) {
    let r: Vec<f64> = {
        let mut v = vec![0.0; DIM * DIM * DIM * DIM];
        for a in 0..DIM {
            for b in 0..DIM {
                for c in 0..DIM {
                    for d in 0..DIM {
                        v[((a * DIM + b) * DIM + c) * DIM + d] = geo.riemann_mixed[a][b][c][d].eval(q);
                    }
                }
            }
        }
        v
    };
    let nfree = 2 * k; // j1..j2k and h1..h2k
    let total = (DIM as u64).pow(2 * nfree as u32);
    let mut out = vec![vec![0.0; DIM]; DIM];
    let mut calls = 0u64;
    let mut lower = vec![0usize; 1 + nfree];
    let mut upper = vec![0usize; 1 + nfree];
    for h in 0..DIM {
        for j in 0..DIM {
            let mut sum = 0.0;
            for code in 0..total {
                let mut c = code;
                lower[0] = j;
                upper[0] = h;
                for x in 1..=nfree {
                    lower[x] = (c % DIM as u64) as usize;
                    c /= DIM as u64;
                }
                for x in 1..=nfree {
                    upper[x] = (c % DIM as u64) as usize;
                    c /= DIM as u64;
                }
                calls += 1;
                let s = GKD(&lower, &upper);
                if s == 0 {
                    continue;
                }
                let mut prod = s as f64;
                for i in 0..k {
                    let (a, b) = (lower[1 + 2 * i], lower[2 + 2 * i]);
                    let (cc, d) = (upper[1 + 2 * i], upper[2 + 2 * i]);
                    prod *= r[((a * DIM + b) * DIM + cc) * DIM + d];
                }
                sum += prod;
            }
            out[h][j] = sum;
        }
    }
    (out, calls)
}

/// The value of the prefactor -1/2^(k+1) relating P_(k) to the usual normalisation
/// E_(k)^h_j = -1/2^(k+1) P_(k)^h_j (E_(1) = G, the Einstein tensor).
pub fn usual_normalisation(k: usize) -> Rational {
    Rational::new(-1, 1i128 << (k + 1))
}
