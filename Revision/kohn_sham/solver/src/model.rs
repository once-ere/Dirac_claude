//! Parameters of a Kohn-Sham run and the lattice of 3-space momenta.
//!
//! Units: H = 1, m = 1 (canonical), so energies, momenta and temperatures are
//! in units of m = H.  The good sector has no extra-time momentum; 3-space is
//! a coordinate 3-torus of size ell = 2 pi / dk, k in dk Z^3; the extra-time
//! coordinate volume is v_t; Vol_7 = ell^3 v_t is the proper 7-volume per unit
//! e^{6Hy} (the same at every slice a4,0: the proper box is fixed).

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub enum Parity {
    Even,
    Odd,
}

impl Parity {
    pub fn tag(self) -> &'static str {
        match self {
            Parity::Even => "even",
            Parity::Odd => "odd",
        }
    }
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Functional {
    /// canonical: Hartree + exact local exchange of the uniform gas (SPEC section 7)
    Lda,
    /// variant: exact Fock exchange of the closed-shell slab determinant
    /// (ks-theory.json exchange.exactFockSlab: + w_Q sigma3, w_Q = lambda Q / 16)
    Exx,
}


#[derive(Clone, Debug)]
pub struct Physics {
    pub hh: f64,
    pub m: f64,
    pub l: f64,
    pub dk: f64,
    pub vt: f64,
    pub a4: f64,
    pub lambda: f64,
    pub n: f64,
    pub temp: f64,
    pub functional: Functional,
    /// weight of the exact-Fock term (1 = exact-Fock variant; < 1 only on a continuation path)
    pub exx_frac: f64,
    pub tip_theta: f64,
}

impl Physics {
    pub fn ell(&self) -> f64 {
        2.0 * std::f64::consts::PI / self.dk
    }
    pub fn vol7(&self) -> f64 {
        let l = self.ell();
        l * l * l * self.vt
    }
}

#[derive(Clone, Debug)]
pub struct Numerics {
    pub g: usize,
    pub root_tol: f64,
    pub scf_tol: f64,
    pub scf_max_iter: usize,
    pub anderson_depth: usize,
    pub anderson_beta: f64,
    pub f_cut: f64,
    pub fd_delta: f64,
    pub dt_rel: f64,
    pub deg_tol: f64,
    /// residual form of the Mermin root (mermin.rs): LogBalance (canonical) or LinearDeviation (refined
    /// run, an exactly equivalent form with a different rounding path)
    pub mermin_form: crate::mermin::MerminForm,
    pub tag: &'static str,
}

impl Numerics {
    pub fn canonical() -> Numerics {
        Numerics {
            g: 900,
            root_tol: 1e-13,
            scf_tol: 1e-11,
            scf_max_iter: 400,
            anderson_depth: 6,
            anderson_beta: 0.4,
            f_cut: 1e-12,
            fd_delta: 2e-3,
            dt_rel: 0.01,
            deg_tol: 1e-9,
            mermin_form: crate::mermin::MerminForm::LogBalance,
            tag: "canonical",
        }
    }
    pub fn refined() -> Numerics {
        Numerics { g: 1800, root_tol: 1e-14, scf_tol: 1e-12, f_cut: 1e-14, mermin_form: crate::mermin::MerminForm::LinearDeviation, tag: "refined", ..Numerics::canonical() }
    }
}

#[derive(Clone, Copy, Debug)]
pub struct Shell {
    pub n2: u32,
    pub r3: u32,
}

/// All shells n2 = |n|^2 <= n2max of Z^3 with their multiplicities r3(n2) > 0.
pub fn shells(n2max: u32) -> Vec<Shell> {
    let r = (n2max as f64).sqrt().floor() as i64 + 1;
    let mut cnt = vec![0u32; n2max as usize + 1];
    for x in -r..=r {
        for y in -r..=r {
            for z in -r..=r {
                let s = x * x + y * y + z * z;
                if s <= n2max as i64 {
                    cnt[s as usize] += 1;
                }
            }
        }
    }
    cnt.iter().enumerate().filter(|(_, &c)| c > 0).map(|(n2, &c)| Shell { n2: n2 as u32, r3: c }).collect()
}

/// Round to `d` significant digits (used to fix the calibrated couplings).
pub fn round_sig(x: f64, d: i32) -> f64 {
    if x == 0.0 {
        return 0.0;
    }
    let e = x.abs().log10().floor() as i32 - (d - 1);
    if e >= 0 {
        let p = 10f64.powi(e);
        (x / p).round() * p
    } else {
        let p = 10f64.powi(-e);
        (x * p).round() / p
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn r3_values() {
        let s = shells(9);
        let v: Vec<(u32, u32)> = s.iter().map(|s| (s.n2, s.r3)).collect();
        assert_eq!(v, vec![(0, 1), (1, 6), (2, 12), (3, 8), (4, 6), (5, 24), (6, 24), (8, 12), (9, 30)]);
    }
    #[test]
    fn rounding() {
        assert_eq!(round_sig(0.0123456, 4), 0.01235);
        assert_eq!(round_sig(12345.6, 4), 12350.0);
    }
}
