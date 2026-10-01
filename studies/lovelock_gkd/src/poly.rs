//! Exact Laurent polynomials with rational coefficients in the eight symbols
//! of the test metric, with the two coordinate derivatives as derivations.
//!
//! Symbols (index in a monomial's exponent array):
//!   0 H            the notebook's constant H
//!   1 A1 = a4'[x4]     2 A2 = a4''[x4]     3 A3 = a4'''[x4]     4 A4 = a4''''[x4]
//!   5 E  = e^{a4[x4]}  (so the metric entry E^(2 a4) is E^2)
//!   6 S  = Sin[6 H x8]^(1/3)
//!   7 C  = Cot[6 H x8]
//! Every component of the metric is a monomial in these symbols:
//!   g_11 = g_22 = g_33 = E^2 S,  g_44 = -1,  g_55 = g_66 = g_77 = -E^-2 S,  g_88 = C^2,
//! and sqrt|det g| = S^3 C (= Sin * Cot = Cos[6 H x8] on 0 < 6 H x8 < pi/2).
//! Derivatives (exact):
//!   d/dx4:  A_n -> A_{n+1},  E -> A1 E,  everything else -> 0
//!   d/dx8:  S -> (1/3) Sin^(-2/3) Cos 6H = 2 H C S,  C -> -6 H (1 + C^2),  everything else -> 0
//! The representation is not canonical in general (S^6 (1 + C^2) = 1 holds), but S
//! cancels identically in every mixed tensor this program prints, and every zero test
//! is done on mixed tensors (plus independent numerical checks).

use crate::rational::Rational;
use std::collections::BTreeMap;
use std::fmt::Write as _;
use std::ops::{Add, Mul, Neg, Sub};

pub const NVAR: usize = 8;
pub const H: usize = 0;
pub const A1: usize = 1;
pub const A2: usize = 2;
pub const A3: usize = 3;
pub const A4: usize = 4;
pub const EV: usize = 5;
pub const SV: usize = 6;
pub const CV: usize = 7;

pub type Monomial = [i32; NVAR];

#[derive(Clone, Debug, PartialEq, Eq, Default)]
pub struct Poly {
    terms: BTreeMap<Monomial, Rational>,
}

impl Poly {
    pub fn zero() -> Poly {
        Poly { terms: BTreeMap::new() }
    }

    pub fn constant(c: Rational) -> Poly {
        let mut p = Poly::zero();
        if !c.is_zero() {
            p.terms.insert([0; NVAR], c);
        }
        p
    }

    pub fn int(n: i128) -> Poly {
        Poly::constant(Rational::int(n))
    }

    pub fn monomial(c: Rational, exps: Monomial) -> Poly {
        let mut p = Poly::zero();
        if !c.is_zero() {
            p.terms.insert(exps, c);
        }
        p
    }

    /// The symbol `var` to the power `e`.
    pub fn var(var: usize, e: i32) -> Poly {
        let mut m = [0; NVAR];
        m[var] = e;
        Poly::monomial(Rational::ONE, m)
    }

    pub fn is_zero(&self) -> bool {
        self.terms.is_empty()
    }

    pub fn terms(&self) -> &BTreeMap<Monomial, Rational> {
        &self.terms
    }

    pub fn len(&self) -> usize {
        self.terms.len()
    }

    pub fn is_empty(&self) -> bool {
        self.terms.is_empty()
    }

    fn add_term(&mut self, m: Monomial, c: Rational) {
        if c.is_zero() {
            return;
        }
        let entry = self.terms.entry(m).or_insert(Rational::ZERO);
        *entry = *entry + c;
        if entry.is_zero() {
            self.terms.remove(&m);
        }
    }

    pub fn scale(&self, c: Rational) -> Poly {
        if c.is_zero() {
            return Poly::zero();
        }
        Poly { terms: self.terms.iter().map(|(m, v)| (*m, *v * c)).collect() }
    }

    /// The inverse of a single monomial (the inverse metric of a diagonal metric).
    pub fn monomial_inverse(&self) -> Poly {
        assert_eq!(self.terms.len(), 1, "monomial_inverse of a non-monomial");
        let (m, c) = self.terms.iter().next().unwrap();
        let mut inv = [0; NVAR];
        for i in 0..NVAR {
            inv[i] = -m[i];
        }
        Poly::monomial(c.recip(), inv)
    }

    /// Exact derivative with respect to the coordinate x_{coord+1} (coord 0..7, i.e.
    /// x1..x8 of the test metric); only x4 (coord 3) and x8 (coord 7) appear.
    pub fn d(&self, coord: usize) -> Poly {
        match coord {
            3 => self.d4(),
            7 => self.d8(),
            _ => Poly::zero(),
        }
    }

    fn d4(&self) -> Poly {
        let mut out = Poly::zero();
        for (m, c) in &self.terms {
            // A_n -> A_{n+1}
            for (n, next) in [(A1, A2), (A2, A3), (A3, A4)] {
                if m[n] != 0 {
                    let mut mm = *m;
                    mm[n] -= 1;
                    mm[next] += 1;
                    out.add_term(mm, *c * Rational::int(m[n] as i128));
                }
            }
            assert!(m[A4] == 0, "derivative of a4'''' requested (order 5 not supported)");
            // E^k -> k A1 E^k
            if m[EV] != 0 {
                let mut mm = *m;
                mm[A1] += 1;
                out.add_term(mm, *c * Rational::int(m[EV] as i128));
            }
        }
        out
    }

    fn d8(&self) -> Poly {
        let mut out = Poly::zero();
        for (m, c) in &self.terms {
            // S^k -> k S^(k-1) * 2 H C S = 2 k H C S^k
            if m[SV] != 0 {
                let mut mm = *m;
                mm[H] += 1;
                mm[CV] += 1;
                out.add_term(mm, *c * Rational::int(2 * m[SV] as i128));
            }
            // C^k -> k C^(k-1) * (-6 H (1 + C^2)) = -6 k H (C^(k-1) + C^(k+1))
            if m[CV] != 0 {
                let k = m[CV] as i128;
                let mut m1 = *m;
                m1[H] += 1;
                m1[CV] -= 1;
                out.add_term(m1, *c * Rational::int(-6 * k));
                let mut m2 = *m;
                m2[H] += 1;
                m2[CV] += 1;
                out.add_term(m2, *c * Rational::int(-6 * k));
            }
        }
        out
    }

    /// Does the polynomial contain the symbol `var` (with a nonzero exponent)?
    pub fn contains(&self, var: usize) -> bool {
        self.terms.keys().any(|m| m[var] != 0)
    }

    /// Numerical value at a point: values of H, a4, a4', a4'', a4''', a4'''' and x8.
    pub fn eval(&self, p: &Point) -> f64 {
        let z = 6.0 * p.h * p.x8;
        let vals = [p.h, p.a1, p.a2, p.a3, p.a4d4, p.a4.exp(), z.sin().cbrt(), z.cos() / z.sin()];
        let mut s = 0.0;
        for (m, c) in &self.terms {
            let mut t = c.to_f64();
            for i in 0..NVAR {
                if m[i] != 0 {
                    t *= vals[i].powi(m[i]);
                }
            }
            s += t;
        }
        s
    }

    /// Mathematica InputForm (so that the author can paste it into a notebook).
    pub fn to_mathematica(&self) -> String {
        if self.terms.is_empty() {
            return "0".to_string();
        }
        let mut out = String::new();
        for (i, (m, c)) in self.terms.iter().enumerate() {
            let neg = c.num() < 0;
            let a = Rational::new(c.num().abs(), c.den());
            if i == 0 {
                if neg {
                    out.push('-');
                }
            } else {
                out.push_str(if neg { " - " } else { " + " });
            }
            let factors = mathematica_factors(m);
            let coeff_one = a == Rational::ONE;
            if factors.is_empty() {
                write!(out, "{}", a).unwrap();
            } else if coeff_one {
                out.push_str(&factors.join("*"));
            } else {
                write!(out, "({})*{}", a, factors.join("*")).unwrap();
            }
        }
        out
    }

    /// LaTeX (for the provenance document).
    pub fn to_latex(&self) -> String {
        if self.terms.is_empty() {
            return "0".to_string();
        }
        let mut out = String::new();
        for (i, (m, c)) in self.terms.iter().enumerate() {
            let neg = c.num() < 0;
            let a = Rational::new(c.num().abs(), c.den());
            if i == 0 {
                if neg {
                    out.push('-');
                }
            } else {
                out.push_str(if neg { " - " } else { " + " });
            }
            let factors = latex_factors(m);
            let coeff = if a.den() == 1 {
                format!("{}", a.num())
            } else {
                format!("\\tfrac{{{}}}{{{}}}", a.num(), a.den())
            };
            if factors.is_empty() {
                out.push_str(&coeff);
            } else if a == Rational::ONE {
                out.push_str(&factors);
            } else {
                write!(out, "{}\\,{}", coeff, factors).unwrap();
            }
        }
        out
    }
}

/// Values at which a polynomial is evaluated numerically.
#[derive(Clone, Copy, Debug)]
pub struct Point {
    pub h: f64,
    pub a4: f64,
    pub a1: f64,
    pub a2: f64,
    pub a3: f64,
    pub a4d4: f64,
    pub x8: f64,
}

/// The exponent k/3 of Sin[6 H x8] for S^k, as a reduced fraction (numerator, denominator).
fn third_exponent(k: i32) -> (i32, i32) {
    if k % 3 == 0 {
        (k / 3, 1)
    } else {
        (k, 3)
    }
}

fn mathematica_factors(m: &Monomial) -> Vec<String> {
    let mut f = Vec::new();
    let pw = |base: &str, e: i32| if e == 1 { base.to_string() } else { format!("{}^{}", base, if e < 0 { format!("({})", e) } else { e.to_string() }) };
    if m[H] != 0 {
        f.push(pw("H", m[H]));
    }
    for (i, d) in [(A1, 1), (A2, 2), (A3, 3), (A4, 4)] {
        if m[i] != 0 {
            f.push(pw(&format!("Derivative[{}][a4][x4]", d), m[i]));
        }
    }
    if m[EV] != 0 {
        f.push(format!("E^({}*a4[x4])", m[EV]));
    }
    if m[SV] != 0 {
        f.push(match third_exponent(m[SV]) {
            (1, 1) => "Sin[6*H*x8]".to_string(),
            (n, 1) => format!("Sin[6*H*x8]^{}", if n < 0 { format!("({})", n) } else { n.to_string() }),
            (n, d) => format!("Sin[6*H*x8]^({}/{})", n, d),
        });
    }
    if m[CV] != 0 {
        f.push(pw("Cot[6*H*x8]", m[CV]));
    }
    f
}

fn latex_factors(m: &Monomial) -> String {
    let mut f = String::new();
    let pw = |base: &str, e: i32| if e == 1 { base.to_string() } else { format!("{}^{{{}}}", base, e) };
    if m[H] != 0 {
        f.push_str(&pw("H", m[H]));
    }
    for (i, primes) in [(A1, "'"), (A2, "''"), (A3, "'''"), (A4, "''''")] {
        if m[i] != 0 {
            if m[i] == 1 {
                write!(f, "\\,a_4{}", primes).unwrap();
            } else {
                write!(f, "\\,(a_4{})^{{{}}}", primes, m[i]).unwrap();
            }
        }
    }
    if m[EV] != 0 {
        write!(f, "\\,e^{{{} a_4}}", m[EV]).unwrap();
    }
    if m[SV] != 0 {
        match third_exponent(m[SV]) {
            (1, 1) => f.push_str("\\,\\sin(6Hx_8)"),
            (n, 1) => write!(f, "\\,\\sin^{{{}}}(6Hx_8)", n).unwrap(),
            (n, d) => write!(f, "\\,\\sin^{{{}/{}}}(6Hx_8)", n, d).unwrap(),
        }
    }
    if m[CV] != 0 {
        if m[CV] == 1 {
            f.push_str("\\,\\cot(6Hx_8)");
        } else {
            write!(f, "\\,\\cot^{{{}}}(6Hx_8)", m[CV]).unwrap();
        }
    }
    f.trim_start_matches("\\,").to_string()
}

impl Add for &Poly {
    type Output = Poly;
    fn add(self, o: &Poly) -> Poly {
        let mut out = self.clone();
        for (m, c) in &o.terms {
            out.add_term(*m, *c);
        }
        out
    }
}

impl Sub for &Poly {
    type Output = Poly;
    fn sub(self, o: &Poly) -> Poly {
        let mut out = self.clone();
        for (m, c) in &o.terms {
            out.add_term(*m, -*c);
        }
        out
    }
}

impl Neg for &Poly {
    type Output = Poly;
    fn neg(self) -> Poly {
        self.scale(-Rational::ONE)
    }
}

impl Mul for &Poly {
    type Output = Poly;
    fn mul(self, o: &Poly) -> Poly {
        let mut out = Poly::zero();
        for (m1, c1) in &self.terms {
            for (m2, c2) in &o.terms {
                let mut m = [0; NVAR];
                for i in 0..NVAR {
                    m[i] = m1[i] + m2[i];
                }
                out.add_term(m, *c1 * *c2);
            }
        }
        out
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn pt() -> Point {
        Point { h: 0.37, a4: 0.21, a1: 0.8, a2: -0.3, a3: 0.11, a4d4: 0.05, x8: 0.29 }
    }

    /// The exact derivatives agree with central finite differences.
    #[test]
    fn derivatives_match_finite_differences() {
        let p = &(&Poly::var(EV, 2) * &Poly::var(SV, 1)) * &(&Poly::var(CV, -3) + &Poly::var(A1, 2));
        let q = pt();
        // d/dx8 by finite differences in x8
        let e = 1e-6;
        let mut qp = q;
        qp.x8 += e;
        let mut qm = q;
        qm.x8 -= e;
        let fd = (p.eval(&qp) - p.eval(&qm)) / (2.0 * e);
        assert!((p.d(7).eval(&q) - fd).abs() < 1e-6 * fd.abs().max(1.0));
        // d/dx4: a4 -> a4 + e a1, a1 -> a1 + e a2, ... (a Taylor step of the function a4)
        let step = |s: f64| Point { a4: q.a4 + s * q.a1, a1: q.a1 + s * q.a2, a2: q.a2 + s * q.a3, a3: q.a3 + s * q.a4d4, ..q };
        let fd4 = (p.eval(&step(e)) - p.eval(&step(-e))) / (2.0 * e);
        assert!((p.d(3).eval(&q) - fd4).abs() < 1e-5 * fd4.abs().max(1.0));
    }

    #[test]
    fn product_and_inverse() {
        let g = Poly::monomial(Rational::int(-1), { let mut m = [0; NVAR]; m[EV] = -2; m[SV] = 1; m });
        let one = &g * &g.monomial_inverse();
        assert_eq!(one, Poly::int(1));
    }
}
