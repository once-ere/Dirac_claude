//! Energy-momentum tensor of the Kohn-Sham state in the primordial field
//! (Stage-2 formulas, CONTRACT section 7, expectation-value rule).
//!
//! For one stationary mode `Psi = e^{-i eps x4} e^{i k x1} W^{-3} chi(y)` the
//! Stage-2 EMT gives, per unit proper volume (the factor `e^{-6Hy}/l^3`
//! converts the normalised profile into a proper density; below `n = a^2 +
//! b^2`, `S = -2 s a b`, `P1 = -s kappa k (a^2 - b^2)`):
//!
//! ```text
//! rho  = T_44        = eps n                            (per mode)
//! p_1  = T^1_1 - L_s = -(k/h_1) <Psibar gamma^1 Psi>   = P1
//! p_y  = T^y_y - L_s = -(1/2)[chi-bar gamma^0 chi' - c.c.] = (eps - v_x) n - P1 - M S
//! p_t  = T^5_5 - L_s = 0                                (q = 0)
//! ```
//!
//! (the last identity for p_y follows from the reduced equation; it is the
//! local virial relation `(eps - v_x) n = p_y + P1 + M S`).  Summing with
//! the normal-ordered weights and adding the on-shell interaction density
//! `L_s = (lambda/2) S_p^2 + e_x(n_p, S_p)` with the sign of CONTRACT
//! section 7 (`T_mu nu = ... + g_mu nu L_s`; `rho = -T^4_4`):
//!
//! ```text
//! rho(y) = e^{-6Hy}/l^3 sum mult w eps n      - L_s(y),
//! p_y(y) = e^{-6Hy}/l^3 sum mult w [(eps - v_x) n - P1 - M S] + L_s(y),
//! p_3(y) = e^{-6Hy}/l^3 (1/3) sum mult w P1   + L_s(y)   (shell-isotropic 3-space),
//! p_t(y) = L_s(y)                                        (extra-time directions).
//! ```
//!
//! `int rho dV_p = E` (the total Kohn-Sham energy) exactly, and the
//! y-conservation `nabla_mu T^mu_y = p_y' + 6H p_y - 3H p_3 - 3H p_t = 0`
//! holds for the self-consistent state (the LDA potentials are linear in
//! the densities, so the force terms cancel against `L_s'`); its residual is
//! reported as a check of the formulas and of self-consistency.
//!
//! Proper-volume averages `<X> = int X e^{6Hy} dy / int e^{6Hy} dy`, the
//! equation-of-state ratios `w_y = <p_y>/<rho>`, `w_3`, `w_t`, the
//! brane-localised fraction of N (within 1/H of the brane), and the
//! comparison with the source the field needs (`rho_req = -21 H^2/kappa`).
//!
//! STAGE4_SPEC erratum E4.1 (binding): for the static field the exact
//! homogeneous-state sourcing conditions are `m S = -36 H^2/kappa` and
//! `lambda S^2 = 30 H^2/kappa`, which together require `lambda S/m = -5/6`
//! and `m S < 0` (kappa > 0).  They are evaluated here on the proper-volume
//! average `<S_p>` of the Kohn-Sham state: `kappa_mass = -36 H^2/(m <S_p>)`,
//! `kappa_coupling = 30 H^2/(lambda <S_p>^2)`, the ratio `lambda <S_p>/m`,
//! the sign of `S_p` (min and max over the grid), the verdict "met" iff
//! both kappa's are finite, positive and equal (relative 1e-6), and the
//! first-order estimate `lambda_hat_needed = -(5/6) m^7 / <S_p>` of the
//! coupling at which the two conditions would coincide (first order: the
//! self-consistent <S_p> itself changes with lambda).
//!
//! Sign of S in the KS state (MEASURED, see the unit test): for m > 0 the
//! massive bulk levels have positive scalar charge (`M/eps` at k = 0), the
//! k = 0 brane zero modes have exactly 0, but the brane band `eps = +c k`
//! (k != 0, the mirror block type) has NEGATIVE scalar charge, because
//! `d eps/dM = k dc/dM < 0`: the exact `c(M) = (2M/(2M-H)) (1 -
//! e^{-(2M-H)L})/(1 - e^{-2ML})` decreases toward 1 as M grows (a larger
//! mass localises the mode more strongly).  Hence a ground state built from
//! the brane band has `<S_p> < 0`, `m <S_p> < 0` and a POSITIVE kappa from
//! the mass condition, while the coupling condition then needs
//! `lambda = -(5/6) m/<S_p> > 0`; a state dominated by bulk levels has
//! `<S_p> > 0` and needs kappa < 0.  The gamma^8 map m -> -m (with
//! lambda -> -lambda, CONTRACT E2) sends the KS state to a state with
//! `S -> -S`, which leaves `m S` and `lambda S^2` unchanged: the verdict is
//! the same in the mirror sector.  All numbers are reported as measured.

use crate::exchange::interaction_energy_density;
use crate::geometry::{curvature_closed_form, density_factor, volume_factor, z_of_y};
use crate::scf::Solution;
use crate::shooting::simpson;

/// EMT profile row at one grid point.
#[derive(Clone, Copy, Debug, Default)]
pub struct Row {
    pub y: f64,
    pub z: f64,
    pub n_c: f64,
    pub n_p: f64,
    pub s_c: f64,
    pub s_p: f64,
    pub m_eff: f64,
    pub v_x: f64,
    pub l_s: f64,
    pub rho: f64,
    pub p_y: f64,
    pub p_3: f64,
    pub p_t: f64,
    pub conservation: f64,
}

/// Proper-volume averages and derived quantities.
#[derive(Clone, Copy, Debug, Default)]
pub struct Summary {
    pub energy_from_rho: f64,
    pub energy_total: f64,
    pub rho_avg: f64,
    pub p_y_avg: f64,
    pub p_3_avg: f64,
    pub p_t_avg: f64,
    pub w_y: f64,
    pub w_3: f64,
    pub w_t: f64,
    pub brane_fraction: f64,
    pub tip_fraction: f64,
    pub proper_volume: f64,
    pub rho_required: f64,
    pub kappa_needed: f64,
    pub conservation_max: f64,
    pub rho_scale: f64,
    pub rho_max: f64,
    pub rho_min: f64,
    /// Proper-volume averages of the proper densities.
    pub s_p_avg: f64,
    pub n_p_avg: f64,
    pub s_p_min: f64,
    pub s_p_max: f64,
    /// E4.1: lambda <S_p> / m (the sourcing conditions need -5/6).
    pub lambda_s_avg_over_m: f64,
    /// E4.1: kappa from m S = -36 H^2/kappa (NaN when m <S_p> = 0).
    pub kappa_mass_condition: f64,
    /// E4.1: kappa from lambda S^2 = 30 H^2/kappa (NaN when lambda <S_p>^2 = 0).
    pub kappa_coupling_condition: f64,
    /// E4.1 verdict: both kappa's finite, positive and equal to 1e-6.
    pub sourcing_conditions_met: bool,
    /// E4.1 first-order estimate: lambda_hat at which lambda <S_p>/m = -5/6
    /// with the present <S_p> (NaN when <S_p> = 0).
    pub lambda_hat_needed_first_order: f64,
}

/// Compute the EMT profiles and their summary.
pub fn compute(solution: &Solution) -> (Vec<Row>, Summary) {
    let params = &solution.params;
    let grid = params.grid();
    let n = grid.len();
    let inv_v = 1.0 / params.volume();
    let lambda = params.lambda();
    let h = params.h;
    let mut rows: Vec<Row> = grid
        .iter()
        .map(|y| Row {
            y: *y,
            z: z_of_y(h, *y),
            ..Row::default()
        })
        .collect();
    for (i, row) in rows.iter_mut().enumerate() {
        let factor = density_factor(h, row.y);
        row.n_c = solution.densities.n_c[i];
        row.s_c = solution.densities.s_c[i];
        row.n_p = factor * row.n_c;
        row.s_p = factor * row.s_c;
        row.m_eff = solution.potential.m_eff.values[i];
        row.v_x = solution.potential.v_x.values[i];
        row.l_s = interaction_energy_density(lambda, row.n_p, row.s_p);
    }
    for st in &solution.spectrum.states {
        if st.weight == 0.0 {
            continue;
        }
        let w = st.mult * st.weight * inv_v;
        let s = st.s as f64;
        for (i, row) in rows.iter_mut().enumerate() {
            let a = st.level.a[i];
            let b = st.level.b[i];
            let kappa = solution.potential.kappa(row.y);
            let n_mode = a * a + b * b;
            let s_mode = -2.0 * s * a * b;
            let p1 = -s * kappa * st.k * (a * a - b * b);
            let factor = density_factor(h, row.y);
            row.rho += w * factor * st.eps * n_mode;
            row.p_y += w * factor * ((st.eps - row.v_x) * n_mode - p1 - row.m_eff * s_mode);
            row.p_3 += w * factor * p1 / 3.0;
        }
    }
    for row in rows.iter_mut() {
        row.rho -= row.l_s;
        row.p_y += row.l_s;
        row.p_3 += row.l_s;
        row.p_t = row.l_s;
    }
    // conservation residual p_y' + 6H p_y - 3H p_3 - 3H p_t (4th-order differences)
    let dy = params.dy();
    for i in 0..n {
        let p = |j: usize| rows[j].p_y;
        let d = if i >= 2 && i + 2 < n {
            (-p(i + 2) + 8.0 * p(i + 1) - 8.0 * p(i - 1) + p(i - 2)) / (12.0 * dy)
        } else if i < 2 {
            // one-sided 5-point forward difference (4th order)
            (-25.0 * p(i) + 48.0 * p(i + 1) - 36.0 * p(i + 2) + 16.0 * p(i + 3) - 3.0 * p(i + 4))
                / (12.0 * dy)
        } else {
            (25.0 * p(i) - 48.0 * p(i - 1) + 36.0 * p(i - 2) - 16.0 * p(i - 3) + 3.0 * p(i - 4))
                / (12.0 * dy)
        };
        rows[i].conservation =
            d + 6.0 * h * rows[i].p_y - 3.0 * h * rows[i].p_3 - 3.0 * h * rows[i].p_t;
    }
    // averages
    let weight: Vec<f64> = grid.iter().map(|y| volume_factor(h, *y)).collect();
    let volume = simpson(dy, &weight);
    let avg = |f: &dyn Fn(&Row) -> f64| -> f64 {
        let values: Vec<f64> = rows
            .iter()
            .zip(weight.iter())
            .map(|(r, w)| f(r) * w)
            .collect();
        simpson(dy, &values) / volume
    };
    let rho_avg = avg(&|r| r.rho);
    let p_y_avg = avg(&|r| r.p_y);
    let p_3_avg = avg(&|r| r.p_3);
    let p_t_avg = avg(&|r| r.p_t);
    let energy_from_rho = rho_avg * volume * params.volume();
    let n_total: f64 = params.volume() * simpson(dy, &solution.densities.n_c);
    let brane_index = ((params.length - 1.0 / h) / dy).round().max(0.0) as usize;
    let brane_fraction = if brane_index < n && n_total != 0.0 {
        params.volume() * simpson(dy, &solution.densities.n_c[brane_index..]) / n_total
    } else {
        0.0
    };
    let tip_index = ((1.0 / h) / dy).round().min((n - 1) as f64) as usize;
    let tip_fraction = if n_total != 0.0 {
        params.volume() * simpson(dy, &solution.densities.n_c[..=tip_index]) / n_total
    } else {
        0.0
    };
    let rho_scale = rows
        .iter()
        .map(|r| r.rho.abs())
        .fold(0.0, f64::max)
        .max(1e-300);
    // interior points only: the one-sided end differences resolve the
    // tip-side structure (scale 1/(kappa k)) less well than the interior stencil
    let conservation_max = rows
        .iter()
        .skip(2)
        .take(n.saturating_sub(4))
        .map(|r| r.conservation.abs())
        .fold(0.0, f64::max)
        / (6.0 * h * rho_scale);
    let curvature = curvature_closed_form(h);
    // E4.1 sourcing conditions on the proper-volume average of S_p
    let s_p_avg = avg(&|r| r.s_p);
    let n_p_avg = avg(&|r| r.n_p);
    let s_p_min = rows.iter().map(|r| r.s_p).fold(f64::INFINITY, f64::min);
    let s_p_max = rows.iter().map(|r| r.s_p).fold(f64::NEG_INFINITY, f64::max);
    let h2 = h * h;
    let kappa_mass_condition = if params.m * s_p_avg != 0.0 {
        -36.0 * h2 / (params.m * s_p_avg)
    } else {
        f64::NAN
    };
    let kappa_coupling_condition = if lambda * s_p_avg * s_p_avg != 0.0 {
        30.0 * h2 / (lambda * s_p_avg * s_p_avg)
    } else {
        f64::NAN
    };
    let sourcing_conditions_met = kappa_mass_condition.is_finite()
        && kappa_coupling_condition.is_finite()
        && kappa_mass_condition > 0.0
        && kappa_coupling_condition > 0.0
        && (kappa_mass_condition - kappa_coupling_condition).abs()
            <= 1e-6
                * kappa_mass_condition
                    .abs()
                    .max(kappa_coupling_condition.abs());
    let summary = Summary {
        energy_from_rho,
        energy_total: solution.energies.total,
        rho_avg,
        p_y_avg,
        p_3_avg,
        p_t_avg,
        w_y: if rho_avg != 0.0 {
            p_y_avg / rho_avg
        } else {
            0.0
        },
        w_3: if rho_avg != 0.0 {
            p_3_avg / rho_avg
        } else {
            0.0
        },
        w_t: if rho_avg != 0.0 {
            p_t_avg / rho_avg
        } else {
            0.0
        },
        brane_fraction,
        tip_fraction,
        proper_volume: volume * params.volume(),
        rho_required: curvature.rho_required,
        kappa_needed: if rho_avg != 0.0 {
            curvature.rho_required / rho_avg
        } else {
            0.0
        },
        conservation_max,
        rho_scale,
        rho_max: rows.iter().map(|r| r.rho).fold(f64::NEG_INFINITY, f64::max),
        rho_min: rows.iter().map(|r| r.rho).fold(f64::INFINITY, f64::min),
        s_p_avg,
        n_p_avg,
        s_p_min,
        s_p_max,
        lambda_s_avg_over_m: lambda * s_p_avg / params.m,
        kappa_mass_condition,
        kappa_coupling_condition,
        sourcing_conditions_met,
        lambda_hat_needed_first_order: if s_p_avg != 0.0 {
            -(5.0 / 6.0) * params.m.powi(7) / s_p_avg
        } else {
            f64::NAN
        },
    };
    (rows, summary)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::scf::{solve, standard_params, Occupation};

    #[test]
    fn free_gas_emt_is_consistent_and_conserved() {
        // N = 32 non-interacting at L = 2: brane zero modes plus the first shell
        let params = standard_params(1.0, 2.0, 0.0, 0.0, 32.0);
        let solution = solve(&params, &Occupation::Zero, None, 0.0).unwrap();
        let (rows, summary) = compute(&solution);
        assert_eq!(rows.len(), params.grid_n);
        assert!(
            (summary.energy_from_rho - summary.energy_total).abs()
                < 1e-6 * summary.energy_total.abs().max(1.0),
            "{} vs {}",
            summary.energy_from_rho,
            summary.energy_total
        );
        assert!(
            summary.conservation_max < 1e-4,
            "conservation {}",
            summary.conservation_max
        );
        assert!(summary.rho_avg > 0.0);
        assert!(summary.brane_fraction > 0.0 && summary.brane_fraction < 1.0);
        assert!(summary.p_t_avg == 0.0);
        assert!(summary.kappa_needed < 0.0);
        // E4.1 on the free N = 32 gas (brane zero modes + the brane band of
        // the first shell): the brane band eps = +ck carries NEGATIVE
        // scalar charge, so S_p <= 0 on the grid, <S_p> < 0, m <S_p> < 0 and
        // the mass condition gives kappa > 0; lambda = 0: the coupling
        // condition has no finite kappa; the conditions are not met.
        let band = solution
            .spectrum
            .states
            .iter()
            .find(|s| s.weight > 0.0 && s.n2 == 1)
            .expect("occupied first-shell state");
        assert!(band.eps > 0.0 && (band.s as f64) * band.level.scalar_charge < 0.0);
        assert!(
            summary.s_p_max <= 1e-12 && summary.s_p_avg < 0.0,
            "{summary:?}"
        );
        assert!(summary.kappa_mass_condition > 0.0);
        assert!(summary.kappa_coupling_condition.is_nan());
        assert!(!summary.sourcing_conditions_met);
        assert_eq!(summary.lambda_s_avg_over_m, 0.0);
        assert!(summary.lambda_hat_needed_first_order > 0.0);
    }
}
