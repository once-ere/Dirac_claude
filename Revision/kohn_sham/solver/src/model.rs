//! Parameters of a Kohn-Sham run and the lattice of 3-space momenta.
//!
//! Units: H = 1, m = 1 (canonical), so energies, momenta and temperatures are
//! in units of m = H.  The good sector has no extra-time momentum; 3-space is
//! a coordinate 3-torus of size ell = 2 pi / dk, k in dk Z^3; the extra-time
//! coordinate volume is v_t.  The metric is the corrected primordial metric of
//! 2026-10-16 (ks-theory.json geometry): ds^2 = e^{2a4} dx_{1..3}^2 - dx4^2
//! + f^2 [dy^2 - e^{2Hy} dx_{5..7}^2], f = e^{-a4} b4^{1/2}.  On the history
//! b4 = b4(0) e^{beta a4} with b4(0) = 1 (the record's value, SPEC section 1) the
//! hidden scale is f = e^{(beta/2 - 1) a4} (e^{-a4/3} for beta = 4/3) and the proper
//! 7-volume of the cell per unit e^{3Hy} is Vol_7(a4,0) = ell^3 v_t e^{-a4,0} b4,0^2
//! = ell^3 v_t e^{(2 beta - 1) a4,0}; lambda = lambda_hat = lambda b4(0)^{-2}
//! (ks-theory.json densities.perOrbital, densities.proper).

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
    /// beta = d ln b4 / d a4 of the history b4 = b4(0) e^{beta a4} (4/3, ks-theory.json adiabaticity.historyBeta);
    /// it fixes the hidden scale f = e^{(beta/2 - 1) a4} and Vol_7(a4) (b4(0) = 1)
    pub beta: f64,
    /// lambda_hat = lambda b4(0)^{-2}, the same at every slice
    pub lambda: f64,
    pub n: f64,
    pub temp: f64,
    pub functional: Functional,
    /// weight of the exact-Fock term (1 = exact-Fock variant; < 1 only on a continuation path)
    pub exx_frac: f64,
    pub tip_theta: f64,
    /// coordinate-cell form (`single --coordinate-cell`): Vol_7 = ell^3 v_t at every slice, so lambda is
    /// lambda_eff = lambda_hat e^{-(2 beta - 1) a4,0} (ks-theory.json densities.couplingVolumeScaling); f is unchanged
    pub coord_cell: bool,
}

impl Physics {
    pub fn ell(&self) -> f64 {
        2.0 * std::f64::consts::PI / self.dk
    }
    /// Vol_7(a4,0) = ell^3 v_t e^{-a4,0} b4,0^2 = ell^3 v_t e^{(2 beta - 1) a4,0}: the proper 7-volume of the cell per
    /// unit e^{3Hy} (sqrt|g| = e^{-a4} b4^2 e^{3Hy}, b4(0) = 1); it grows like e^{(5/3) a4} on the history (beta = 4/3).
    /// In the coordinate-cell form it is ell^3 v_t.
    pub fn vol7(&self) -> f64 {
        let l = self.ell();
        if self.coord_cell {
            return l * l * l * self.vt;
        }
        l * l * l * self.vt * ((2.0 * self.beta - 1.0) * self.a4).exp()
    }
    /// the hidden scale f = e^{-a4,0} b4,0^{1/2} = e^{(beta/2 - 1) a4,0} (b4(0) = 1): h_j = j[-(i/f) sigma1 d_y + ...],
    /// chi' = f N chi; the proper hidden length of the cell [-L, 0] is f L
    pub fn fh(&self) -> f64 {
        ((0.5 * self.beta - 1.0) * self.a4).exp()
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
    /// The refined run measures the error of the canonical one (U_Rust = (16/15) |canonical - refined|), so it must
    /// differ in every error source.  Its SCF tolerance is 1e-14, three orders below the canonical 1e-11: with 1e-12
    /// both runs could stop at the same iteration (the residual can drop from above 1e-11 to below 1e-12 in one
    /// Anderson step) and carry the same SCF stopping error, which enters E_band - E_int and p0 at first order
    /// (claude_failures.md H15); the tighter tolerance needs more iterations (up to about 350 for the slowest thermal
    /// state), hence the larger cap.
    pub fn refined() -> Numerics {
        Numerics { g: 1800, root_tol: 1e-14, scf_tol: 1e-14, scf_max_iter: 1000, f_cut: 1e-14, mermin_form: crate::mermin::MerminForm::LinearDeviation, tag: "refined", ..Numerics::canonical() }
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
