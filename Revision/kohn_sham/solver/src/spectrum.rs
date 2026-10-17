//! Free-field (lambda = 0) spectra and their exact checks (corrected metric of
//! 2026-10-16: h_j = j[-(i/f) sigma1 d_y + M sigma2 + kappa k sigma3] + v with
//! kappa = e^{-a4,0} and f = e^{-a4,0} b4,0^{1/2} constant in y; ks-theory.json).
//! Identifiers that contain "brane" (file names, CSV columns, check names) are
//! kept from the earlier record for continuity; they denote the fold y = 0.

use crate::json::fmt_f;
use crate::model::*;
use crate::report::Report;
use crate::scf::*;
use crate::shoot::*;
use std::f64::consts::PI;

pub struct Csv {
    pub header: Vec<&'static str>,
    pub rows: Vec<Vec<String>>,
}

impl Csv {
    pub fn new(header: Vec<&'static str>) -> Csv {
        Csv { header, rows: Vec::new() }
    }
    pub fn push(&mut self, r: Vec<String>) {
        assert_eq!(r.len(), self.header.len());
        self.rows.push(r);
    }
    pub fn text(&self) -> String {
        let mut s = self.header.join(",");
        s.push('\n');
        for r in &self.rows {
            s.push_str(&r.join(","));
            s.push('\n');
        }
        s
    }
}

pub fn f(x: f64) -> String {
    fmt_f(x)
}

fn odd_p_roots(m: f64, l: f64, count: usize) -> Vec<f64> {
    (0..count)
        .map(|n| {
            let mut lo = (n as f64 + 0.5) * PI / l;
            let mut hi = (n as f64 + 1.0) * PI / l;
            let g = |p: f64| m * (p * l).sin() + p * (p * l).cos();
            let glo = g(lo);
            for _ in 0..200 {
                let mid = 0.5 * (lo + hi);
                if mid <= lo || mid >= hi {
                    break;
                }
                if (g(mid) > 0.0) == (glo > 0.0) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }
            0.5 * (lo + hi)
        })
        .collect()
}

pub fn level_in(grid: &Grid, phys: &Physics, pots: &Pots, k: f64, j: i32, par: Parity, l: i64, tol: f64) -> f64 {
    let ctx = ctx_for(grid, phys, pots);
    let sec = Sector { k, j, parity: par };
    // bracket from below by stepping down from 0 if needed
    find_level(&ctx, sec, target(par, l), 0.0, None, tol).map(|x| x.0).unwrap_or(f64::NAN)
}

/// Free-field checks; returns the CSV files.
pub fn free_checks(base: &Physics, num: &Numerics, slope_theory: f64, slices: &[f64], rep: &mut Report) -> Vec<(String, String)> {
    let mut files = Vec::new();
    let tol = num.root_tol;
    // (a) k = 0 analytic spectra
    let mut csv = Csv::new(vec!["m", "L", "a4", "f", "parity", "label", "eps_numeric", "eps_analytic", "difference"]);
    let mut worst: f64 = 0.0;
    let mut worst_hi: f64 = 0.0;
    for &(m, l, a4) in &[(1.0, 3.0, 0.0), (1.0, 2.0, 0.0), (2.0, 3.0, 0.0), (1.0, 3.0, 1.5)] {
        let mut ph = base.clone();
        ph.m = m;
        ph.l = l;
        ph.a4 = a4;
        let fl = ph.fh() * l;
        let grid = Grid::new(ph.hh, l, ((num.g as f64) * l / 3.0).round() as usize);
        let pots = Pots::free(grid.nf, m);
        let pr = odd_p_roots(m, fl, 6);
        for lab in -3i64..=5 {
            // even
            let ex = if lab == 0 { 0.0 } else { (lab.signum() as f64) * (m * m + (lab as f64 * PI / fl).powi(2)).sqrt() };
            let e = level_in(&grid, &ph, &pots, 0.0, 1, Parity::Even, lab, tol);
            csv.push(vec![f(m), f(l), f(a4), f(ph.fh()), "even".into(), lab.to_string(), f(e), f(ex), f(e - ex)]);
            // odd: labels l >= 0 positive (p_l), l <= -1 negative (p_{-l-1})
            let exo = if lab >= 0 { (m * m + pr[lab as usize].powi(2)).sqrt() } else { -(m * m + pr[(-lab - 1) as usize].powi(2)).sqrt() };
            let eo = level_in(&grid, &ph, &pots, 0.0, 1, Parity::Odd, lab, tol);
            csv.push(vec![f(m), f(l), f(a4), f(ph.fh()), "odd".into(), lab.to_string(), f(eo), f(exo), f(eo - exo)]);
            for (x, y) in [(e, ex), (eo, exo)] {
                if y.abs() < 4.0 {
                    worst = worst.max((x - y).abs());
                } else {
                    worst_hi = worst_hi.max((x - y).abs());
                }
            }
        }
    }
    let tol_k0 = if num.g >= 1800 { 5e-10 } else { 5e-9 };
    rep.check(
        "free_k0_analytic_spectra",
        worst < tol_k0 && worst_hi < 64.0 * tol_k0,
        format!(
            "k = 0, constant M, v = 0, theta_tip = 0 (ks-theory.json boundaryConditions.exactK0Spectra) for (m, L, a4,0) = (1, 3, 0), (1, 2, 0), (2, 3, 0) (f = 1) and (1, 3, 1.5) (f = e^(-1/2) on the history), labels -3..5 of both fold conditions: even eps = 0 and +-sqrt(M^2 + (n pi/(f L))^2), odd eps = +-sqrt(M^2 + p^2) with tan(p f L) = -p/M; max |difference| {:.2e} for |eps| < 4 m (tolerance {:.0e}, RK4 error ~ (f h eps)^4), {:.2e} for |eps| >= 4 m (tolerance {:.0e})",
            worst, tol_k0, worst_hi, 64.0 * tol_k0
        ),
    );
    files.push(("spectrum/free-k0-analytic.csv".to_string(), csv.text()));

    let grid = Grid::new(base.hh, base.l, num.g);
    let pots = Pots::free(grid.nf, base.m);
    // (b) zero mode exact, at a4,0 = 0 (f = 1) and a4,0 = 2 (f = e^(-2/3) on the history)
    {
        let mut emax: f64 = 0.0;
        let mut dev: f64 = 0.0;
        let mut bmax: f64 = 0.0;
        for a4 in [0.0, 2.0] {
            let mut ph = base.clone();
            ph.a4 = a4;
            let ctx = ctx_for(&grid, &ph, &pots);
            let sec = Sector { k: 0.0, j: 1, parity: Parity::Even };
            let (e, _) = find_level(&ctx, sec, 0.0, 0.0, None, tol).unwrap();
            let prof = profile(&ctx, sec, e);
            let fm = ph.fh() * ph.m;
            let c = (2.0 * fm / (1.0 - (-2.0 * fm * ph.l).exp())).sqrt();
            emax = emax.max(e.abs());
            for p in 0..grid.nf {
                dev = dev.max((prof[2 * p] - c * (fm * grid.y[p]).exp()).abs());
                bmax = bmax.max(prof[2 * p + 1].abs());
            }
        }
        rep.check(
            "free_zero_mode_exact",
            emax == 0.0 && bmax == 0.0 && dev < 1e-9,
            format!("k = 0 fold zero mode (both j) at a4,0 = 0 (f = 1) and a4,0 = 2 (f = e^(-2/3)): eps = 0 exactly (max |eps| = {:e}), chi = (a, 0) with b = 0 identically (max |b| = {:e}); a = sqrt(2fM/(1 - e^(-2fML))) e^(fMy) to {:.2e} (normalised in int dy, Simpson)", emax, bmax, dev),
        );
    }
    // (c) fold-band slope c = e^{-a4,0} at every slice (Richardson from k = 1e-4, 2e-4)
    let mut csv = Csv::new(vec!["a4", "c_numeric", "c_theory", "difference"]);
    let mut wslope: f64 = 0.0;
    for &a4 in slices {
        let mut ph = base.clone();
        ph.a4 = a4;
        let e1 = level_in(&grid, &ph, &pots, 1e-4, 1, Parity::Even, 0, 1e-16);
        let e2 = level_in(&grid, &ph, &pots, 2e-4, 1, Parity::Even, 0, 1e-16);
        let c = (4.0 * e1 / 1e-4 - e2 / 2e-4) / 3.0;
        let ct = slope_theory * (-a4).exp();
        wslope = wslope.max(((c - ct) / ct).abs());
        csv.push(vec![f(a4), f(c), f(ct), f(c - ct)]);
    }
    rep.check(
        "free_brane_band_slope",
        wslope < 1e-9,
        format!(
            "d eps/dk at k = 0 of the even j = +1 fold band (Richardson extrapolation of eps(k)/k from k = 1e-4, 2e-4) equals ks-theory.json c = {} (braneBandSlope_a0) times e^(-a4,0) at a4,0 = {:?} (M = H = 1, L = 3; f = e^(-a4,0/3) on the history: the slope does not depend on f) to {:.2e} relative",
            slope_theory, slices, wslope
        ),
    );
    files.push(("spectrum/brane-band-slope.csv".to_string(), csv.text()));
    // (d) symmetries at lambda = 0 (j mirror and (j,k) -> (-j,-k))
    {
        let mut dev1: f64 = 0.0;
        let mut dev2: f64 = 0.0;
        for &n2 in &[0u32, 1, 2, 5, 9] {
            let k = base.dk * (n2 as f64).sqrt();
            for lab in -3i64..=3 {
                let ep = level_in(&grid, base, &pots, k, 1, Parity::Even, lab, tol);
                let em = level_in(&grid, base, &pots, k, -1, Parity::Even, -lab, tol);
                dev1 = dev1.max((ep + em).abs());
                let op = level_in(&grid, base, &pots, k, 1, Parity::Odd, lab, tol);
                let om = level_in(&grid, base, &pots, k, -1, Parity::Odd, -lab - 1, tol);
                dev1 = dev1.max((op + om).abs());
                let sm = level_in(&grid, base, &pots, -k, -1, Parity::Even, lab, tol);
                dev2 = dev2.max((sm - ep).abs());
                let so = level_in(&grid, base, &pots, -k, -1, Parity::Odd, lab, tol);
                dev2 = dev2.max((so - op).abs());
            }
        }
        rep.check(
            "free_block_type_symmetries",
            dev1 < 1e-12 && dev2 < 1e-12,
            format!(
                "lambda = 0, n2 in {{0,1,2,5,9}}, labels -3..3: spec h_(-1) = -spec h_(+1) (label l <-> -l even, -l-1 odd) to {:.1e}; sigma3 h_j(k) sigma3 = h_(-j)(-k): eps_(-1)(-k) = eps_(+1)(k) label by label to {:.1e}",
                dev1, dev2
            ),
        );
    }
    // (e) particle labels: eps(l_min) > 0 > eps(l_min - 1) (k > 0); zero mode at k = 0
    {
        let mut ok = true;
        let mut mingap = f64::INFINITY;
        for sh in shells(30) {
            for (j, par) in SECTORS {
                let lm = ell_min(&grid, base, sh, j, par).unwrap();
                let e0 = level_in(&grid, base, &pots, base.dk * (sh.n2 as f64).sqrt(), j, par, lm, tol);
                let em = level_in(&grid, base, &pots, base.dk * (sh.n2 as f64).sqrt(), j, par, lm - 1, tol);
                if sh.n2 == 0 && par == Parity::Even {
                    ok &= e0 == 0.0 && em < 0.0;
                } else {
                    ok &= e0 > 0.0 && em < 0.0;
                    mingap = mingap.min(e0.min(-em));
                }
            }
        }
        rep.check(
            "free_particle_branch_labels",
            ok,
            format!("for every shell n2 <= 30 and sector (j, fold condition): the lowest particle label l_min (first target above Phi(eps = 0)) has eps > 0 and l_min - 1 has eps < 0 (the branch split by the sign of the lambda = 0 level is a split of the Pruefer labels; closest level to zero away from the k = 0 zero modes: {:.4} m); k = 0 even l_min = 0 is the zero mode (convention)", mingap),
        );
    }
    // (f) tip angle: the exact boundary identity and the size of the shifts (no tip suppression: kappa is constant in y)
    {
        let mut csv = Csv::new(vec!["a4", "f", "k", "label", "theta_tip", "eps", "shift_from_theta0", "overlap", "boundary_term", "identity_residual", "fold_band_tail_2fM_exp"]);
        let mut wres: f64 = 0.0;
        let mut est_ratio: f64 = 0.0;
        let mut bulk_min: f64 = f64::INFINITY;
        let mut band_max: f64 = 0.0;
        for a4 in [0.0f64, 1.5] {
            let mut p0 = base.clone();
            p0.a4 = a4;
            let fh = p0.fh();
            let fm = fh * p0.m;
            let tail = 2.0 * fm * (-2.0 * fm * p0.l).exp() / (1.0 - (-2.0 * fm * p0.l).exp());
            for &k in &[0.25f64, 0.5, 1.0] {
                for lab in [0i64, 1] {
                    let sec = Sector { k, j: 1, parity: Parity::Even };
                    let ctx0 = ctx_for(&grid, &p0, &pots);
                    let (e0, _) = find_level(&ctx0, sec, target(Parity::Even, lab), 0.4 * k + lab as f64, None, tol).unwrap();
                    let pr0 = profile(&ctx0, sec, e0);
                    for &th in &[0.5f64, 1.0] {
                        let mut ph = p0.clone();
                        ph.tip_theta = th;
                        let ctx = ctx_for(&grid, &ph, &pots);
                        let (e, _) = find_level(&ctx, sec, target(Parity::Even, lab), e0, None, tol).unwrap();
                        let pr = profile(&ctx, sec, e);
                        let ov: Vec<f64> = (0..grid.nf).map(|q| pr0[2 * q] * pr[2 * q] + pr0[2 * q + 1] * pr[2 * q + 1]).collect();
                        let overlap = grid.integrate(&ov);
                        // (eps_theta - eps_0) int chi_0^dag chi_theta dy = -j a_0(-L) b_theta(-L) / f (j = +1; b_0(-L) = 0)
                        let bterm = -pr0[0] * pr[1] / fh;
                        let res = ((e - e0) * overlap - bterm).abs();
                        wres = wres.max(res);
                        let sh = e - e0;
                        if lab == 0 {
                            // the fold band: first-order estimate |shift| ~ tan(theta/2) |a_0(-L)|^2/f (INFORMATION)
                            est_ratio = est_ratio.max(sh.abs() / ((0.5 * th).tan() * tail / fh));
                            band_max = band_max.max(sh.abs());
                        } else {
                            bulk_min = bulk_min.min(sh.abs());
                        }
                        csv.push(vec![f(a4), f(fh), f(k), lab.to_string(), f(th), f(e), f(sh), f(overlap), f(bterm), f(res), f(tail)]);
                    }
                }
            }
        }
        rep.check(
            "free_tip_angle_boundary_identity",
            wres < 1e-9,
            format!(
                "tip family (1 - Q(theta)) chi(-L) = 0, theta = 0.5, 1 against theta = 0, j = +1 even, k = 0.25, 0.5, 1, a4,0 = 0 (f = 1) and 1.5 (f = e^(-1/2)): the exact boundary identity (eps_theta - eps_0) int chi_0^dag chi_theta dy = -j a_0(-L) b_theta(-L)/f (from phi^dag h chi - (h phi)^dag chi = d/dy[-(i j/f) phi^dag sigma1 chi], ks-theory.json boundaryConditions.selfAdjointness) holds to {:.2e} (tolerance 1e-9); INFORMATION: the fold band (label 0, chi_0 = (e^(f M y), 0) exactly) shifts by at most {:.2e}, at most {:.3} times the first-order estimate tan(theta/2) |a_0(-L)|^2/f, |a_0(-L)|^2 = 2fM e^(-2fML)/(1 - e^(-2fML)) (the tail of the fold band at the tip, e^(-2fML) = e^(-6) at a4,0 = 0 and e^(-3.64) at a4,0 = 1.5); the extended level (label 1) shifts by at least {:.3e}: kappa = e^(-a4) is constant in y, so nothing suppresses an extended orbital toward the tip and its level depends on the tip condition (spectrum/tip-angle.csv)",
                wres, band_max, est_ratio, bulk_min
            ),
        );
        files.push(("spectrum/tip-angle.csv".to_string(), csv.text()));
    }
    // (g) the fold band eps = kappa k exactly, and the rescaling relation eps(k, a4,0; L) = eps(k e^{-a4,0}, 0; f0 L)
    {
        let mut csv = Csv::new(vec!["k", "eps_band_a0", "eps_band_bulk_even_l1", "eps_odd_l0", "eps_jm1_even_l1"]);
        let mut kk = 0.0;
        while kk <= 4.0 + 1e-12 {
            let b = level_in(&grid, base, &pots, kk, 1, Parity::Even, 0, tol);
            let b1 = level_in(&grid, base, &pots, kk, 1, Parity::Even, 1, tol);
            let o = level_in(&grid, base, &pots, kk, 1, Parity::Odd, 0, tol);
            let m1 = level_in(&grid, base, &pots, kk, -1, Parity::Even, 1, tol);
            csv.push(vec![f(kk), f(b), f(b1), f(o), f(m1)]);
            kk += 0.05;
        }
        files.push(("spectrum/brane-band.csv".to_string(), csv.text()));
        let mut dev: f64 = 0.0;
        let mut mono = true;
        let mut prev = -1.0;
        let mut band_dev: f64 = 0.0;
        for i in 0..=80 {
            let k = 0.05 * i as f64;
            let b = level_in(&grid, base, &pots, k, 1, Parity::Even, 0, tol);
            mono &= b > prev;
            prev = b;
            band_dev = band_dev.max((b - k).abs());
        }
        for &a4 in slices {
            let mut ph = base.clone();
            ph.a4 = a4;
            // the partner slice a4 = 0 (f = 1) with the proper hidden length f0 L on the same number of steps
            let mut pr = base.clone();
            pr.l = ph.fh() * base.l;
            let grid_r = Grid::new(pr.hh, pr.l, num.g);
            let pots_r = Pots::free(grid_r.nf, base.m);
            for &k in &[0.25, 1.0, 2.5] {
                for (j, par, l) in [(1, Parity::Even, 0i64), (1, Parity::Odd, 0), (-1, Parity::Even, 1), (1, Parity::Even, 1)] {
                    let x = level_in(&grid, &ph, &pots, k, j, par, l, tol);
                    let y = level_in(&grid_r, &pr, &pots_r, k * (-a4).exp(), j, par, l, tol);
                    dev = dev.max((x - y).abs());
                }
            }
        }
        rep.check(
            "free_rescaling_relation_and_band_monotone",
            dev < 1e-12 && mono && band_dev < 1e-12,
            format!("lambda = 0: eps(k, a4,0; L) = eps(k e^(-a4,0), 0; f0 L), f0 = e^(-a4,0/3) (the rescaling identity of ks-theory.json without interaction: H does not enter the free levels), for k in {{0.25, 1, 2.5}}, a4,0 in {:?}, four sectors, on the same number of RK4 steps, to {:.1e}; the even j = +1 fold band is eps = kappa k exactly (chi = (e^(f M y), 0) for every k at theta = 0; max |eps - k| at a4,0 = 0 on [0, 4]: {:.1e}) and strictly increasing (spectrum/brane-band.csv): {}", slices, dev, band_dev, mono),
        );
    }
    files
}

/// Closed shells of the free aufbau at a slice (all particle levels below emax).
pub fn closed_shells(grid: &Grid, phys: &Physics, emax: f64, tol: f64) -> Vec<(f64, f64, f64, String)> {
    let mut lev: Vec<(f64, f64, String)> = Vec::new();
    for sh in shells(4000) {
        let mut any = false;
        for (j, par) in SECTORS {
            let (sp, e) = free_sector_upto(grid, phys, sh, j, par, emax, tol, 50).unwrap();
            for (i, x) in e.iter().enumerate() {
                any = true;
                lev.push((*x, 4.0 * sh.r3 as f64, format!("{}:{}:{}:{}", sh.n2, if j > 0 { "+1" } else { "-1" }, par.tag(), sp.ell_min + i as i64)));
            }
        }
        if !any && sh.n2 > 0 {
            break;
        }
    }
    lev.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap().then(a.2.cmp(&b.2)));
    // groups
    let mut out = Vec::new();
    let mut cum = 0.0;
    let mut i = 0;
    while i < lev.len() {
        let e0 = lev[i].0;
        let mut k = i;
        let mut g = 0.0;
        let mut names = Vec::new();
        while k < lev.len() && lev[k].0 - e0 <= 1e-9 {
            g += lev[k].1;
            names.push(lev[k].2.clone());
            k += 1;
        }
        cum += g;
        let next = if k < lev.len() { lev[k].0 } else { f64::NAN };
        out.push((cum, e0, next, names.join(";")));
        i = k;
    }
    out
}
