//! Energy-momentum tensor profiles, their identities, the adiabaticity
//! measure, particle-hole lists and the completeness of a label set.
//!
//! EMT (ks-theory.json emt; SPEC section 4 signs, rho = -T^x4_x4, p = T^mu_mu):
//!   rho = sum w g f eps n_o - e_int,
//!   p3  = sum w g f (kappa |k| / 3) t_o + e_int   (closed cubic shells),
//!   p_t = e_int,
//!   p8  = sum w g f [(eps - v) n_o - M s_o - kappa |k| t_o] + e_int
//! (exact-Fock variant: - w_Q q_o inside the bracket of p8, derived in the
//! solver README).  Identities checked: 2 Vol_7 int e^{6Hy} rho = E_KS;
//! (e^{6Hy} p8)' = 3H e^{6Hy} (p3 + p_t) (nabla_mu T^mu_y = 0) pointwise and
//! integrated; the derivative form of the y-kinetic term
//! j (a b' - b a') = (eps - v)(a^2+b^2) - M j 2ab - kappa k j (a^2-b^2) - w_Q (a^2-b^2)
//! with a', b' from finite differences of the stored orbitals (a pointwise
//! residual of the orbital equation, the non-trivial content of the trace
//! identity); T^x4_y = 0 holds identically in the real form chi = (a, i b).

use crate::model::*;
use crate::scf::*;
use crate::shoot::*;
use std::collections::BTreeMap;

pub struct Emt {
    pub eint: Vec<f64>,
    pub rho: Vec<f64>,
    pub p3: Vec<f64>,
    pub pt: Vec<f64>,
    pub p8: Vec<f64>,
}

pub fn emt(phys: &Physics, co: Coeffs, st: &State) -> Emt {
    let eint = e_int(phys, co, &st.dens);
    let nf = eint.len();
    let d = &st.dens;
    Emt {
        rho: (0..nf).map(|p| d.k4[p] - eint[p]).collect(),
        p3: (0..nf).map(|p| d.tk[p] / 3.0 + eint[p]).collect(),
        pt: eint.clone(),
        p8: (0..nf).map(|p| d.ky[p] + eint[p]).collect(),
        eint,
    }
}

/// 4th-order first derivative on a uniform grid (one-sided at the ends).
pub fn deriv4(f: &[f64], h: f64) -> Vec<f64> {
    let n = f.len();
    let mut d = vec![0.0; n];
    for i in 0..n {
        d[i] = if i >= 2 && i + 2 < n {
            (f[i - 2] - 8.0 * f[i - 1] + 8.0 * f[i + 1] - f[i + 2]) / (12.0 * h)
        } else if i == 0 {
            (-25.0 * f[0] + 48.0 * f[1] - 36.0 * f[2] + 16.0 * f[3] - 3.0 * f[4]) / (12.0 * h)
        } else if i == 1 {
            (-3.0 * f[0] - 10.0 * f[1] + 18.0 * f[2] - 6.0 * f[3] + f[4]) / (12.0 * h)
        } else if i == n - 1 {
            (25.0 * f[n - 1] - 48.0 * f[n - 2] + 36.0 * f[n - 3] - 16.0 * f[n - 4] + 3.0 * f[n - 5]) / (12.0 * h)
        } else {
            (3.0 * f[n - 1] + 10.0 * f[n - 2] - 18.0 * f[n - 3] + 6.0 * f[n - 4] - f[n - 5]) / (12.0 * h)
        };
    }
    d
}

pub struct EmtChecks {
    pub energy_integral: f64,
    pub ycons_integrated_rel: f64,
    pub ycons_pointwise_rel: f64,
    pub trace_derivative_rel: f64,
    pub int_rho: f64,
    pub int_p3: f64,
    pub int_pt: f64,
    pub int_p8: f64,
    pub int_n: f64,
    pub de_da_emt: f64,
    pub delta_ex_fock: f64,
}

pub fn emt_checks(grid: &Grid, phys: &Physics, st: &State, e: &Emt) -> EmtChecks {
    let nf = grid.nf;
    let vol2 = 2.0 * phys.vol7();
    let hh = phys.hh;
    let w = |f: &dyn Fn(usize) -> f64| -> f64 {
        let v: Vec<f64> = (0..nf).map(|p| grid.e6[p] * f(p)).collect();
        vol2 * grid.integrate(&v)
    };
    let int_rho = w(&|p| e.rho[p]);
    let int_p3 = w(&|p| e.p3[p]);
    let int_pt = w(&|p| e.pt[p]);
    let int_p8 = w(&|p| e.p8[p]);
    let int_n = w(&|p| st.dens.n[p]);
    let de_da_emt = -w(&|p| st.dens.tk[p]);
    let delta_ex_fock = phys.lambda / 32.0 * w(&|p| st.dens.q[p] * st.dens.q[p]);
    // y-conservation on the node grid
    let nodes: Vec<usize> = (0..=grid.g).map(|i| 2 * i).collect();
    let dcoord: Vec<f64> = nodes.iter().map(|&p| grid.e6[p] * e.p8[p]).collect();
    let rhs: Vec<f64> = nodes.iter().map(|&p| 3.0 * hh * grid.e6[p] * (e.p3[p] + e.pt[p])).collect();
    let dd = deriv4(&dcoord, grid.h);
    // scale: the derivatives themselves or the size of the cancelling terms of p8 (times m, an inverse length)
    let termscale = (0..nf).map(|p| grid.e6[p] * (st.dens.kyabs[p] + e.eint[p].abs())).fold(0.0f64, f64::max);
    let scale = dd.iter().chain(rhs.iter()).fold(0.0f64, |m, x| m.max(x.abs())).max(termscale * phys.m.abs()).max(1e-300);
    let pw = dd.iter().zip(&rhs).fold(0.0f64, |m, (a, b)| m.max((a - b).abs())) / scale;
    let rhs_f: Vec<f64> = (0..nf).map(|p| 3.0 * hh * grid.e6[p] * (e.p3[p] + e.pt[p])).collect();
    let integ = grid.integrate(&rhs_f);
    let jump = grid.e6[nf - 1] * e.p8[nf - 1] - grid.e6[0] * e.p8[0];
    let sc2 = integ.abs().max(jump.abs()).max((grid.e6[0] * e.p8[0]).abs()).max(termscale).max(1e-300);
    let yint = (jump - integ).abs() / sc2;
    if std::env::var("KS_DEBUG").is_ok() {
        eprintln!("  emt: functional {:?} jump {:e} integral {:e} e6p8(0) {:e} e6p8(-L) {:e} pointwise {:e} max|eint| {:e}", phys.functional, jump, integ, grid.e6[nf - 1] * e.p8[nf - 1], grid.e6[0] * e.p8[0], pw, e.eint.iter().fold(0.0f64, |m, x| m.max(x.abs())));
    }
    // derivative form of the y-kinetic term, occupied orbitals
    let kap0 = (-phys.a4).exp();
    let mut tr: f64 = 0.0;
    for (lv, &f) in st.levels.iter().zip(&st.occ) {
        if f == 0.0 {
            continue;
        }
        let j = lv.key.1 as f64;
        let a: Vec<f64> = nodes.iter().map(|&p| lv.prof[2 * p]).collect();
        let b: Vec<f64> = nodes.iter().map(|&p| lv.prof[2 * p + 1]).collect();
        let da = deriv4(&a, grid.h);
        let db = deriv4(&b, grid.h);
        let mut sc: f64 = 0.0;
        let mut dev: f64 = 0.0;
        for (i, &p) in nodes.iter().enumerate() {
            let kk = kap0 * grid.ew[p] * lv.k;
            let t1 = (lv.eps - st.pots.v[p]) * (a[i] * a[i] + b[i] * b[i]);
            let t2 = st.pots.mass[p] * j * 2.0 * a[i] * b[i];
            let t3 = (kk * j + st.pots.wq[p]) * (a[i] * a[i] - b[i] * b[i]);
            let lhs = j * (a[i] * db[i] - b[i] * da[i]);
            sc = sc.max(t1.abs() + t2.abs() + t3.abs());
            dev = dev.max((lhs - (t1 - t2 - t3)).abs());
        }
        tr = tr.max(dev / sc.max(1e-300));
    }
    EmtChecks {
        energy_integral: int_rho,
        ycons_integrated_rel: yint,
        ycons_pointwise_rel: pw,
        trace_derivative_rel: tr,
        int_rho,
        int_p3,
        int_pt,
        int_p8,
        int_n,
        de_da_emt,
        delta_ex_fock,
    }
}

/// Degenerate groups of levels (sorted by energy): (energy, member indices).
pub fn groups(st: &State, tol: f64) -> Vec<(f64, Vec<usize>)> {
    let mut idx: Vec<usize> = (0..st.levels.len()).collect();
    idx.sort_by(|&a, &b| st.levels[a].eps.partial_cmp(&st.levels[b].eps).unwrap().then(st.levels[a].key.cmp(&st.levels[b].key)));
    let mut out: Vec<(f64, Vec<usize>)> = Vec::new();
    for i in idx {
        let e = st.levels[i].eps;
        match out.last_mut() {
            Some((e0, m)) if e - *e0 <= tol => m.push(i),
            _ => out.push((e, vec![i])),
        }
    }
    out
}

pub fn key_str(k: &Key) -> String {
    format!("{}:{}:{}:{}", k.0, if k.1 > 0 { "+1" } else { "-1" }, k.2.tag(), k.3)
}

pub struct PhRow {
    pub hole: String,
    pub particle: String,
    pub e_hole: f64,
    pub e_particle: f64,
    pub de: f64,
    pub mult: f64,
    pub same_sector: bool,
}

/// Lowest particle-hole excitations (groups), particles below `e_complete`.
pub fn particle_hole(st: &State, tol: f64, e_complete: f64, rows: usize) -> Vec<PhRow> {
    let gr = groups(st, tol);
    let mut out = Vec::new();
    for (eh, mh) in &gr {
        let fh: f64 = mh.iter().map(|&i| st.occ[i] * st.levels[i].deg).sum();
        if fh <= 1e-12 {
            continue;
        }
        for (ep, mp) in &gr {
            if *ep < e_complete && ep > eh {
                let gp: f64 = mp.iter().map(|&i| (1.0 - st.occ[i]) * st.levels[i].deg).sum();
                if gp <= 1e-12 {
                    continue;
                }
                let sect = |i: usize| (st.levels[i].key.0, st.levels[i].key.1, st.levels[i].key.2);
                let same = mh.iter().any(|&a| mp.iter().any(|&b| sect(a) == sect(b)));
                out.push(PhRow {
                    hole: mh.iter().map(|&i| key_str(&st.levels[i].key)).collect::<Vec<_>>().join(";"),
                    particle: mp.iter().map(|&i| key_str(&st.levels[i].key)).collect::<Vec<_>>().join(";"),
                    e_hole: *eh,
                    e_particle: *ep,
                    de: ep - eh,
                    mult: fh * gp,
                    same_sector: same,
                });
            }
        }
    }
    out.sort_by(|a, b| a.de.partial_cmp(&b.de).unwrap().then(a.hole.cmp(&b.hole)).then(a.particle.cmp(&b.particle)));
    out.truncate(rows);
    out
}

/// Lowest level NOT in the label set (the next label of every sector and the
/// lowest level of the first shell beyond the set), in the converged potentials.
pub fn lowest_excluded(grid: &Grid, phys: &Physics, st: &State, tol: f64) -> Result<f64, String> {
    let ctx = ctx_for(grid, phys, &st.pots);
    let mut emin = f64::INFINITY;
    let mut maxn2 = 0;
    for sp in &st.specs {
        maxn2 = maxn2.max(sp.shell.n2);
        let l = sp.ell_min + sp.nlev as i64;
        let last = st.levels.iter().filter(|lv| lv.key.0 == sp.shell.n2 && lv.key.1 == sp.j && lv.key.2 == sp.parity).map(|lv| lv.eps).fold(f64::NEG_INFINITY, f64::max);
        let sec = Sector { k: kmag(phys, sp.shell), j: sp.j, parity: sp.parity };
        let lower = if last.is_finite() { Some(last) } else { None };
        let (e, _) = find_level(&ctx, sec, target(sp.parity, l), last.max(0.0) + 0.5, lower, tol)?;
        emin = emin.min(e);
    }
    // the lowest levels of the next five shells beyond the set (guards against a non-monotone shell minimum)
    for next in shells(maxn2 + 200).into_iter().filter(|s| s.n2 > maxn2).take(5) {
        for (j, par) in SECTORS {
            let lm = ell_min(grid, phys, next, j, par)?;
            let sec = Sector { k: kmag(phys, next), j, parity: par };
            let (e, _) = find_level(&ctx, sec, target(par, lm), 0.0, None, tol)?;
            emin = emin.min(e);
        }
    }
    Ok(emin)
}

pub struct Adiab {
    pub qmax: f64,
    pub pair: String,
    pub pair_de: f64,
    pub pair_me: f64,
    pub hf_maxdev: f64,
    pub max_deps_da: f64,
    pub n_pairs: usize,
}

/// Adiabaticity measure Q_nm = A H |<n| d_a h |m>| / (eps_n - eps_m)^2 for n
/// occupied, m empty, same (shell, j, parity); d_a h = -j kappa k sigma3
/// + j (d_a M_eff) sigma2 + d_a v_v + (d_a w_Q) sigma3 with the self-consistent
/// derivatives from the a4 +- delta states (fixed occupations).
/// Richardson-extrapolated central difference from f(+-delta), f(+-2 delta).
pub fn rich(fp1: f64, fm1: f64, fp2: f64, fm2: f64, delta: f64) -> f64 {
    let d1 = (fp1 - fm1) / (2.0 * delta);
    let d2 = (fp2 - fm2) / (4.0 * delta);
    (4.0 * d1 - d2) / 3.0
}

/// `nb` = the states at a4 + delta, a4 - delta, a4 + 2 delta, a4 - 2 delta (fixed occupations).
pub fn adiabatic(grid: &Grid, phys: &Physics, a_h: f64, st0: &State, nb: [&State; 4], delta: f64) -> Adiab {
    let nf = grid.nf;
    let kap0 = (-phys.a4).exp();
    let [sp1, sm1, sp2, sm2] = nb;
    let dm: Vec<f64> = (0..nf).map(|p| rich(sp1.pots.mass[p], sm1.pots.mass[p], sp2.pots.mass[p], sm2.pots.mass[p], delta)).collect();
    let dv: Vec<f64> = (0..nf).map(|p| rich(sp1.pots.v[p], sm1.pots.v[p], sp2.pots.v[p], sm2.pots.v[p], delta)).collect();
    let dw: Vec<f64> = (0..nf).map(|p| rich(sp1.pots.wq[p], sm1.pots.wq[p], sp2.pots.wq[p], sm2.pots.wq[p], delta)).collect();
    let me = |n: &Level, m: &Level| -> f64 {
        let j = n.key.1 as f64;
        let mut s = 0.0;
        for p in 0..nf {
            let (an, bn, am, bm) = (n.prof[2 * p], n.prof[2 * p + 1], m.prof[2 * p], m.prof[2 * p + 1]);
            let s3 = an * am - bn * bm;
            let s2 = an * bm + bn * am;
            let s0 = an * am + bn * bm;
            let kk = kap0 * grid.ew[p] * n.k;
            s += grid.simpson[p] * (-j * kk * s3 + j * dm[p] * s2 + dv[p] * s0 + dw[p] * s3);
        }
        s
    };
    let mut by_sector: BTreeMap<(u32, i32, Parity), Vec<usize>> = BTreeMap::new();
    for (i, lv) in st0.levels.iter().enumerate() {
        by_sector.entry((lv.key.0, lv.key.1, lv.key.2)).or_default().push(i);
    }
    let mut qmax = 0.0;
    let mut pair = String::from("none");
    let mut pair_de = f64::NAN;
    let mut pair_me = f64::NAN;
    let mut n_pairs = 0;
    for idx in by_sector.values() {
        for &a in idx {
            if st0.occ[a] <= 1e-12 {
                continue;
            }
            for &b in idx {
                if b == a || st0.occ[b] >= 1.0 - 1e-12 {
                    continue;
                }
                let x = me(&st0.levels[a], &st0.levels[b]);
                let de = st0.levels[a].eps - st0.levels[b].eps;
                let q = a_h * x.abs() / (de * de);
                n_pairs += 1;
                if q > qmax {
                    qmax = q;
                    pair = format!("{} -> {}", key_str(&st0.levels[a].key), key_str(&st0.levels[b].key));
                    pair_de = de.abs();
                    pair_me = x.abs();
                }
            }
        }
    }
    // Hellmann-Feynman: d eps/da (finite differences) vs <n| d_a h |n>
    let mut hf: f64 = 0.0;
    let mut mx: f64 = 0.0;
    let ep1: BTreeMap<Key, f64> = sp1.levels.iter().map(|l| (l.key, l.eps)).collect();
    let em1: BTreeMap<Key, f64> = sm1.levels.iter().map(|l| (l.key, l.eps)).collect();
    let ep2: BTreeMap<Key, f64> = sp2.levels.iter().map(|l| (l.key, l.eps)).collect();
    let em2: BTreeMap<Key, f64> = sm2.levels.iter().map(|l| (l.key, l.eps)).collect();
    for lv in &st0.levels {
        if let (Some(a), Some(b), Some(c), Some(d)) = (ep1.get(&lv.key), em1.get(&lv.key), ep2.get(&lv.key), em2.get(&lv.key)) {
            let fd = rich(*a, *b, *c, *d, delta);
            let d = me(lv, lv);
            hf = hf.max((fd - d).abs());
            mx = mx.max(fd.abs());
        }
    }
    if n_pairs > 0 && qmax == 0.0 {
        pair = "all matrix elements vanish".into();
    }
    Adiab { qmax, pair, pair_de, pair_me, hf_maxdev: hf, max_deps_da: mx, n_pairs }
}
