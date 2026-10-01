//! Exact rational numbers on i128 with overflow checks (every operation that
//! would overflow panics with a message instead of wrapping silently).

use std::cmp::Ordering;
use std::fmt;
use std::ops::{Add, Mul, Neg, Sub};

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub struct Rational {
    num: i128,
    den: i128, // always > 0, gcd(num, den) = 1
}

fn gcd(mut a: i128, mut b: i128) -> i128 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

impl Rational {
    pub const ZERO: Rational = Rational { num: 0, den: 1 };
    pub const ONE: Rational = Rational { num: 1, den: 1 };

    pub fn new(num: i128, den: i128) -> Rational {
        assert!(den != 0, "rational with zero denominator");
        let (mut n, mut d) = (num, den);
        if d < 0 {
            n = n.checked_neg().expect("rational overflow");
            d = d.checked_neg().expect("rational overflow");
        }
        let g = gcd(n, d);
        if g > 1 {
            n /= g;
            d /= g;
        }
        Rational { num: n, den: d }
    }

    pub fn int(n: i128) -> Rational {
        Rational { num: n, den: 1 }
    }

    pub fn num(&self) -> i128 {
        self.num
    }

    pub fn den(&self) -> i128 {
        self.den
    }

    pub fn is_zero(&self) -> bool {
        self.num == 0
    }

    pub fn to_f64(&self) -> f64 {
        self.num as f64 / self.den as f64
    }

    pub fn recip(&self) -> Rational {
        Rational::new(self.den, self.num)
    }
}

impl Add for Rational {
    type Output = Rational;
    fn add(self, o: Rational) -> Rational {
        let g = gcd(self.den, o.den);
        let l = (self.den / g).checked_mul(o.den).expect("rational overflow");
        let a = self.num.checked_mul(l / self.den).expect("rational overflow");
        let b = o.num.checked_mul(l / o.den).expect("rational overflow");
        Rational::new(a.checked_add(b).expect("rational overflow"), l)
    }
}

impl Sub for Rational {
    type Output = Rational;
    fn sub(self, o: Rational) -> Rational {
        self + (-o)
    }
}

impl Neg for Rational {
    type Output = Rational;
    fn neg(self) -> Rational {
        Rational { num: self.num.checked_neg().expect("rational overflow"), den: self.den }
    }
}

impl Mul for Rational {
    type Output = Rational;
    fn mul(self, o: Rational) -> Rational {
        let g1 = gcd(self.num, o.den).max(1);
        let g2 = gcd(o.num, self.den).max(1);
        let n = (self.num / g1).checked_mul(o.num / g2).expect("rational overflow");
        let d = (self.den / g2).checked_mul(o.den / g1).expect("rational overflow");
        Rational::new(n, d)
    }
}

impl PartialOrd for Rational {
    fn partial_cmp(&self, o: &Rational) -> Option<Ordering> {
        Some(self.cmp(o))
    }
}

impl Ord for Rational {
    fn cmp(&self, o: &Rational) -> Ordering {
        (self.num.checked_mul(o.den).expect("rational overflow"))
            .cmp(&o.num.checked_mul(self.den).expect("rational overflow"))
    }
}

impl fmt::Display for Rational {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        if self.den == 1 {
            write!(f, "{}", self.num)
        } else {
            write!(f, "{}/{}", self.num, self.den)
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn arithmetic() {
        let a = Rational::new(1, 3);
        let b = Rational::new(-1, 6);
        assert_eq!(a + b, Rational::new(1, 6));
        assert_eq!(a * b, Rational::new(-1, 18));
        assert_eq!(a - a, Rational::ZERO);
        assert_eq!(Rational::new(4, -8), Rational::new(-1, 2));
        assert_eq!(Rational::new(2, 3).recip(), Rational::new(3, 2));
    }
}
