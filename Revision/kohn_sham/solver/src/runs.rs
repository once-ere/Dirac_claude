//! The canonical matrix: instantaneous Kohn-Sham states along the deflating
//! history a4,0 in {0, 0.5, 1, 1.5, 2} (a4 = A H x4, A = 1), N in
//! {8, N_mid, N_large}, lambda in {0, +-lambda_1, +-lambda_2}; excited states,
//! adiabaticity, rescaling identity, exact-Fock variant, thermodynamics.

use crate::analysis::*;
use crate::analysis::rich;
use crate::json::{obj, to_pretty, Json};
use crate::model::*;
use crate::report::Report;
use crate::scf::*;
use crate::shoot::*;
use crate::spectrum::{closed_shells, f, free_checks, Csv};
use crate::theory::{inputs_json, TheoryInputs};
use std::collections::BTreeMap;
use std::path::PathBuf;
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Mutex;

pub const SLICES: [f64; 5] = [0.0, 0.5, 1.0, 1.5, 2.0];
pub const A_HIST: f64 = 1.0;
pub const SIGMAS: [f64; 2] = [0.1, 0.3];
pub const TEMPS: [f64; 3] = [0.01, 0.02, 0.05];

pub struct Cfg {
    pub out: PathBuf,
    pub report: PathBuf,
    pub num: Numerics,
    pub threads: usize,
    pub quick: bool,
    pub timing: Option<PathBuf>,
}

pub fn base_phys() -> Physics {
    Physics { hh: 1.0, m: 1.0, l: 3.0, dk: 0.25, vt: 1.0, a4: 0.0, lambda: 0.0, n: 8.0, temp: 0.0, functional: Functional::Lda, exx_frac: 1.0, tip_theta: 0.0 }
}

pub fn par_map<T: Sync, R: Send>(items: &[T], threads: usize, func: impl Fn(&T) -> R + Sync) -> Vec<R> {
    let n = items.len();
    let next = AtomicUsize::new(0);
    let slots: Vec<Mutex<Option<R>>> = (0..n).map(|_| Mutex::new(None)).collect();
    std::thread::scope(|s| {
        for _ in 0..threads.max(1).min(n.max(1)) {
            s.spawn(|| loop {
                let i = next.fetch_add(1, Ordering::SeqCst);
                if i >= n {
                    break;
                }
                let r = func(&items[i]);
                *slots[i].lock().unwrap() = Some(r);
            });
        }
    });
    slots.into_iter().map(|m| m.into_inner().unwrap().unwrap()).collect()
}

/// Aggregated checks over many runs.
#[derive(Default)]
pub struct Agg {
    map: BTreeMap<String, (String, f64, usize, Vec<String>, f64, String)>,
}

pub struct Item {
    pub name: &'static str,
    pub desc: &'static str,
    pub tol: f64,
    pub value: f64,
    pub pass: Option<bool>,
}

fn it(name: &'static str, desc: &'static str, tol: f64, value: f64) -> Item {
    Item { name, desc, tol, value, pass: None }
}

impl Agg {
    pub fn add(&mut self, id: &str, x: &Item) {
        let pass = x.pass.unwrap_or(x.value <= x.tol && x.value.is_finite());
        let e = self.map.entry(x.name.to_string()).or_insert((x.desc.to_string(), x.tol, 0, Vec::new(), f64::NEG_INFINITY, String::new()));
        e.2 += 1;
        if !pass {
            e.3.push(format!("{} ({:.3e})", id, x.value));
        }
        let v = if x.value.is_nan() { f64::INFINITY } else { x.value };
        if v > e.4 {
            e.4 = v;
            e.5 = id.to_string();
        }
    }
    pub fn into_report(self, rep: &mut Report) {
        for (name, (desc, tol, n, fails, worst, wid)) in self.map {
            let fl = if fails.is_empty() { "none".to_string() } else { fails.join(", ") };
            rep.check(&name, fails.is_empty(), format!("{}; {} cases; worst value {:.3e} ({}); tolerance {:.1e}; failures: {}", desc, n, worst, wid, tol, fl));
        }
    }
}

fn sigma_of(tag: &str) -> f64 {
    match tag {
        "lamp1" | "lamm1" => SIGMAS[0],
        "lamp2" | "lamm2" => SIGMAS[1],
        _ => 0.0,
    }
}

pub fn run_id(n: f64, tag: &str, a4: f64) -> String {
    format!("N{}_{}_a{:02}", n as i64, tag, (a4 * 10.0).round() as i64)
}

fn guesses_of(st: &State) -> BTreeMap<Key, f64> {
    st.levels.iter().map(|l| (l.key, l.eps)).collect()
}

fn occ_map(st: &State) -> BTreeMap<Key, f64> {
    st.levels.iter().zip(&st.occ).filter(|(_, &f)| f > 0.0).map(|(l, &f)| (l.key, f)).collect()
}

/// Ground state with a coupling-continuation fallback.
pub fn solve_ground(grid: &Grid, phys: &Physics, num: &Numerics, co: Coeffs, specs: &[SectorSpec], guesses: &BTreeMap<Key, f64>) -> Result<State, String> {
    let inp = RunInput { phys: phys.clone(), num, co, specs: specs.to_vec(), occ: Occ::Aufbau, start: None, guesses: guesses.clone() };
    match run_scf(grid, &inp) {
        Ok(mut s) => {
            s.path = "direct".into();
            Ok(s)
        }
        Err(e1) => {
            let num2 = Numerics { anderson_beta: num.anderson_beta / 2.0, scf_max_iter: 2 * num.scf_max_iter, ..num.clone() };
            let mut start: Option<Pots> = None;
            let mut g = guesses.clone();
            let mut last: Option<State> = None;
            for fr in [0.25, 0.5, 0.75, 1.0] {
                let mut ph = phys.clone();
                ph.lambda = phys.lambda * fr;
                let inp = RunInput { phys: ph, num: &num2, co, specs: specs.to_vec(), occ: Occ::Aufbau, start: start.clone(), guesses: g.clone() };
                let s = run_scf(grid, &inp).map_err(|e| format!("direct: {}; continuation at {}: {}", e1, fr, e))?;
                start = Some(s.pots.clone());
                g = guesses_of(&s);
                last = Some(s);
            }
            let mut s = last.unwrap();
            s.path = format!("continuation lambda x 1/4, 1/2, 3/4, 1 (beta/2) after: {}", e1);
            Ok(s)
        }
    }
}

fn fixed_run(grid: &Grid, phys: &Physics, num: &Numerics, co: Coeffs, base: &State, occ: BTreeMap<Key, f64>) -> Result<State, String> {
    let inp = RunInput { phys: phys.clone(), num, co, specs: base.specs.clone(), occ: Occ::Fixed(occ), start: Some(base.pots.clone()), guesses: guesses_of(base) };
    run_scf(grid, &inp)
}

pub struct Shared<'a> {
    pub grid: Grid,
    pub num: &'a Numerics,
    pub co: Coeffs,
    pub base: Physics,
}

fn profile_csv(grid: &Grid, st: &State, e: &Emt) -> String {
    let mut csv = Csv::new(vec!["y", "n", "S", "Q", "M_eff", "v_v", "w_Q", "e_int", "rho", "p3", "p_t", "p8"]);
    let stride = (grid.nf - 1) / 150;
    let mut p = 0;
    while p < grid.nf {
        csv.push(vec![
            f(grid.y[p]),
            f(st.dens.n[p]),
            f(st.dens.s[p]),
            f(st.dens.q[p]),
            f(st.pots.mass[p]),
            f(st.pots.v[p]),
            f(st.pots.wq[p]),
            f(e.eint[p]),
            f(e.rho[p]),
            f(e.p3[p]),
            f(e.pt[p]),
            f(e.p8[p]),
        ]);
        p += stride;
    }
    csv.text()
}

fn levels_csv(st: &State) -> String {
    let mut csv = Csv::new(vec!["n2", "r3", "k", "j", "parity", "label", "label_min", "eps", "deg", "f"]);
    let lmin: BTreeMap<(u32, i32, Parity), i64> = st.specs.iter().map(|s| ((s.shell.n2, s.j, s.parity), s.ell_min)).collect();
    for (l, &o) in st.levels.iter().zip(&st.occ) {
        csv.push(vec![
            l.key.0.to_string(),
            ((l.deg / 4.0).round() as i64).to_string(),
            f(l.k),
            l.key.1.to_string(),
            l.key.2.tag().into(),
            l.key.3.to_string(),
            lmin[&(l.key.0, l.key.1, l.key.2)].to_string(),
            f(l.eps),
            f(l.deg),
            f(o),
        ]);
    }
    csv.text()
}

pub struct GroundOut {
    pub id: String,
    pub n: f64,
    pub tag: String,
    pub ia: usize,
    pub items: Vec<Item>,
    pub files: Vec<(String, String)>,
    pub summary: Vec<String>,
    pub excited: Vec<String>,
    pub adiab: Vec<String>,
    pub emtrow: Vec<String>,
    pub rescale: Option<Vec<String>>,
    pub exx: Option<Vec<String>>,
    pub occ: BTreeMap<Key, f64>,
    pub state: Option<State>,
    pub record: Json,
    pub error: Option<String>,
    pub e_ks: f64,
}

pub const SUMMARY_HEADER: [&str; 24] = [
    "id", "N", "lambda_tag", "lambda", "a4", "path", "iterations", "residual", "E_KS", "E_band", "E_int", "E_variational", "HOMO", "LUMO", "KS_gap", "open_shell", "max_abs_Meff_minus_m", "max_abs_v_v", "S_min", "S_max", "n_max", "levels", "shells", "E_complete",
];

pub fn ground_task(sh: &Shared, n: f64, tag: &str, lam: f64, ia: usize) -> GroundOut {
    let a4 = SLICES[ia];
    let id = run_id(n, tag, a4);
    let mut out = GroundOut {
        id: id.clone(),
        n,
        tag: tag.to_string(),
        ia,
        items: vec![],
        files: vec![],
        summary: vec![],
        excited: vec![],
        adiab: vec![],
        emtrow: vec![],
        rescale: None,
        exx: None,
        occ: BTreeMap::new(),
        state: None,
        record: Json::Null,
        error: None,
        e_ks: f64::NAN,
    };
    if let Err(e) = ground_inner(sh, n, tag, lam, a4, &mut out) {
        out.error = Some(e.clone());
        out.items.push(Item { name: "ground_runs_completed", desc: "every run of the canonical matrix completed (ground, a4 +- delta, Delta-SCF, rescaling partner, exact-Fock variant)", tol: 0.0, value: 1.0, pass: Some(false) });
        eprintln!("ERROR {}: {}", id, e);
    } else {
        out.items.push(Item { name: "ground_runs_completed", desc: "every run of the canonical matrix completed (ground, a4 +- delta, Delta-SCF, rescaling partner, exact-Fock variant)", tol: 0.0, value: 0.0, pass: Some(true) });
    }
    out
}

fn margin_for(tag: &str) -> f64 {
    0.25 + 2.0 * sigma_of(tag)
}

fn ground_inner(sh: &Shared, n: f64, tag: &str, lam: f64, a4: f64, out: &mut GroundOut) -> Result<(), String> {
    let grid = &sh.grid;
    let num = sh.num;
    let co = sh.co;
    let mut phys = sh.base.clone();
    phys.n = n;
    phys.lambda = lam;
    phys.a4 = a4;
    let specs = specs_t0(grid, &phys, margin_for(tag), 3, num.root_tol)?;
    let mut fp = phys.clone();
    fp.lambda = 0.0;
    let free = run_scf(grid, &RunInput { phys: fp, num, co, specs: specs.clone(), occ: Occ::Aufbau, start: None, guesses: BTreeMap::new() })?;
    let gs = if lam == 0.0 { free.clone() } else { solve_ground(grid, &phys, num, co, &specs, &guesses_of(&free))? };
    let mut gs = gs;
    if gs.path.is_empty() {
        gs.path = "direct".into();
    }
    let id = out.id.clone();
    let e = emt(&phys, co, &gs);
    let ec = emt_checks(grid, &phys, &gs, &e);
    // window completeness, HOMO/LUMO, gap
    let e_complete = lowest_excluded(grid, &phys, &gs, num.root_tol)?;
    let gr = groups(&gs, num.deg_tol);
    let homo = gr.iter().filter(|(_, m)| m.iter().any(|&i| gs.occ[i] > 1e-12)).map(|(e, _)| *e).fold(f64::NEG_INFINITY, f64::max);
    let lumo = gr.iter().filter(|(e, m)| *e > homo && m.iter().any(|&i| gs.occ[i] < 1.0 - 1e-12)).map(|(e, _)| *e).fold(f64::INFINITY, f64::min);
    let gap = lumo - homo;
    // conservation
    let ntot: f64 = gs.levels.iter().zip(&gs.occ).map(|(l, f)| l.deg * f).sum();
    out.items.push(it("ground_scf_converged", "Kohn-Sham SCF (Anderson mixing) converged: final max |potential residual| (units of m)", num.scf_tol, gs.resid));
    out.items.push(it("ground_N_conservation", "particle number: |sum g f - N| and |2 Vol_7 int e^{6Hy} n dy - N| / N (doubled system; the patch holds N/2)", 1e-9, (ntot - n).abs().max((ec.int_n - n).abs() / n)));
    out.items.push(it("ground_orbital_boundary_conditions", "max over orbitals of the brane-condition residual |b(0)| (even) or |a(0)| (odd) of the normalised orbital", 1e-8, gs.max_brane_residual));
    out.items.push(it("ground_energy_two_forms", "E_KS = sum g f eps - 2 Vol_7 int e^{6Hy} e_int equals the variational form (input potentials, output densities): relative difference", 1e-9, (gs.e_ks - gs.e_var).abs() / gs.e_ks.abs().max(1.0)));
    out.items.push(it("emt_energy_integral", "2 Vol_7 int e^{6Hy} rho dy = E_KS: relative difference", 1e-11, (ec.energy_integral - gs.e_ks).abs() / gs.e_ks.abs().max(1.0)));
    out.items.push(it("emt_y_conservation_integrated", "[e^{6Hy} p8]_{-L}^{0} = 3H int e^{6Hy} (p3 + p_t) dy (nabla_mu T^mu_y = 0): relative difference", 1e-7, ec.ycons_integrated_rel));
    out.items.push(it("emt_y_conservation_pointwise", "(e^{6Hy} p8)' = 3H e^{6Hy}(p3 + p_t) on the node grid (4th-order differences): max relative residual", 1e-5, ec.ycons_pointwise_rel));
    out.items.push(it("emt_trace_derivative_form", "derivative form of the y-kinetic term j(a b' - b a') = (eps - v)(a^2+b^2) - M j 2ab - kappa k j(a^2-b^2) (orbital equation residual from finite differences of the stored occupied orbitals): max relative deviation", 1e-5, ec.trace_derivative_rel));
    out.items.push(Item { name: "ground_window_complete", desc: "label set complete: the lowest level outside the label set lies above the LUMO (value: LUMO - lowest excluded, must be < 0)", tol: 0.0, value: lumo - e_complete, pass: Some(lumo < e_complete) });
    out.items.push(Item { name: "ground_closed_shell", desc: "the aufbau ground state is closed-shell (no fractionally occupied degenerate level; value 1 = open)", tol: 0.0, value: if gs.open_shell { 1.0 } else { 0.0 }, pass: Some(!gs.open_shell) });
    // a4 +- delta (fixed occupations) for d/da4
    let occ = occ_map(&gs);
    let dl = num.fd_delta;
    let mut nbs: Vec<State> = Vec::new();
    for s in [1.0, -1.0, 2.0, -2.0] {
        let mut pp = phys.clone();
        pp.a4 = a4 + s * dl;
        nbs.push(fixed_run(grid, &pp, num, co, &gs, occ.clone())?);
    }
    let de_fd = rich(nbs[0].e_ks, nbs[1].e_ks, nbs[2].e_ks, nbs[3].e_ks, dl);
    let de_scale = gs.levels.iter().zip(&gs.occ).map(|(l, f)| l.deg * f * l.eps.abs()).sum::<f64>().max(phys.m.abs());
    out.items.push(it("emt_energy_change_dE_da4", "dE/da4 at fixed occupations (self-consistent states at a4 +- delta, +- 2 delta, delta = 2e-3, Richardson) = -6 Vol_7 int e^{6Hy}(p3 - p_t) dy (nabla_mu T^mu_x4 = 0, Hellmann-Feynman): |difference| / max(sum g f |eps|, m)", 1e-8, (de_fd - ec.de_da_emt).abs() / de_scale));
    let ad = adiabatic(grid, &phys, A_HIST * phys.hh, &gs, [&nbs[0], &nbs[1], &nbs[2], &nbs[3]], dl);
    out.items.push(it("adiabatic_hellmann_feynman", "d eps_n/da4 (Richardson differences of the self-consistent levels) = <n| d_a h |n> with d_a h = -j kappa k sigma3 + j (d_a M_eff) sigma2 + d_a v_v (+ d_a w_Q sigma3): max absolute deviation (units of m)", 1e-7, ad.hf_maxdev));
    let (stp, stm) = (&nbs[0], &nbs[1]);
    // Delta-SCF (first excited state: one particle from the HOMO group to the LUMO group, uniform over each degenerate group)
    let hg = gr.iter().find(|(e, _)| *e == homo).unwrap();
    let lg = gr.iter().find(|(e, _)| *e == lumo).unwrap();
    let gh: f64 = hg.1.iter().map(|&i| gs.levels[i].deg).sum();
    let gl: f64 = lg.1.iter().map(|&i| gs.levels[i].deg).sum();
    let mut occx = occ.clone();
    for &i in &hg.1 {
        let k = gs.levels[i].key;
        let v = occx.get(&k).copied().unwrap_or(0.0) - 1.0 / gh;
        occx.insert(k, v);
    }
    for &i in &lg.1 {
        let k = gs.levels[i].key;
        let v = occx.get(&k).copied().unwrap_or(0.0) + 1.0 / gl;
        occx.insert(k, v);
    }
    let exc = fixed_run(grid, &phys, num, co, &gs, occx)?;
    let dscf = exc.e_ks - gs.e_ks;
    if lam == 0.0 {
        out.items.push(it("excited_delta_scf_free_equals_gap", "lambda = 0: Delta-SCF excitation energy equals the KS gap exactly (|difference|, units of m)", 1e-10, (dscf - gap).abs()));
    }
    out.items.push(it("excited_scf_converged", "Delta-SCF state (fixed ensemble occupations) converged: final residual", num.scf_tol, exc.resid));
    let hole_names: Vec<String> = hg.1.iter().map(|&i| key_str(&gs.levels[i].key)).collect();
    let part_names: Vec<String> = lg.1.iter().map(|&i| key_str(&gs.levels[i].key)).collect();
    out.excited = vec![id.clone(), (n as i64).to_string(), out.tag.clone(), f(lam), f(a4), f(homo), f(lumo), f(gap), f(gh), f(gl), hole_names.join(";"), part_names.join(";"), f(exc.e_ks), f(dscf), f(dscf - gap), exc.iters.to_string(), f(exc.resid)];
    // particle-hole list
    let ph = particle_hole(&gs, num.deg_tol, e_complete, 24);
    let mut csv = Csv::new(vec!["rank", "hole_levels", "particle_levels", "eps_hole", "eps_particle", "delta_eps", "multiplicity", "same_sector"]);
    for (r, p) in ph.iter().enumerate() {
        csv.push(vec![(r + 1).to_string(), p.hole.clone(), p.particle.clone(), f(p.e_hole), f(p.e_particle), f(p.de), f(p.mult), p.same_sector.to_string()]);
    }
    out.files.push((format!("excited/particle-hole/{}.csv", id), csv.text()));
    // adiabaticity row
    out.adiab = vec![id.clone(), (n as i64).to_string(), out.tag.clone(), f(lam), f(a4), f(ad.qmax), ad.pair.clone(), f(ad.pair_de), f(ad.pair_me), f(ad.qmax * ad.qmax), ad.n_pairs.to_string(), f(ad.hf_maxdev), f(ad.max_deps_da), f(de_fd), f(ec.de_da_emt)];
    // rescaling partner
    if a4 > 0.0 {
        let mut pr = phys.clone();
        pr.a4 = 0.0;
        pr.dk = phys.dk * (-a4).exp();
        pr.vt = phys.vt * (-3.0 * a4).exp();
        let specs_r = specs_t0(grid, &pr, margin_for(tag), 3, num.root_tol)?;
        let mut fpr = pr.clone();
        fpr.lambda = 0.0;
        let free_r = run_scf(grid, &RunInput { phys: fpr, num, co, specs: specs_r.clone(), occ: Occ::Aufbau, start: None, guesses: BTreeMap::new() })?;
        let gr_r = if lam == 0.0 { free_r } else { solve_ground(grid, &pr, num, co, &specs_r, &guesses_of(&free_r))? };
        let k1: Vec<Key> = gs.levels.iter().map(|l| l.key).collect();
        let k2: Vec<Key> = gr_r.levels.iter().map(|l| l.key).collect();
        let same_keys = k1 == k2;
        let m2: BTreeMap<Key, f64> = gr_r.levels.iter().map(|l| (l.key, l.eps)).collect();
        let de = gs.levels.iter().filter_map(|l| m2.get(&l.key).map(|x| (x - l.eps).abs())).fold(0.0f64, f64::max);
        let er = emt(&pr, co, &gr_r);
        let rel = |a: &[f64], b: &[f64]| -> f64 {
            let s = a.iter().fold(0.0f64, |m, x| m.max(x.abs())).max(1e-300);
            a.iter().zip(b).fold(0.0f64, |m, (x, y)| m.max((x - y).abs())) / s
        };
        let pd = rel(&gs.dens.n, &gr_r.dens.n).max(rel(&gs.dens.s, &gr_r.dens.s)).max(rel(&e.rho, &er.rho)).max(rel(&e.p3, &er.p3)).max(rel(&e.p8, &er.p8));
        let d_e = (gs.e_ks - gr_r.e_ks).abs() / gs.e_ks.abs().max(1.0);
        let occ_same = occ_map(&gs) == occ_map(&gr_r);
        out.items.push(Item {
            name: "rescaling_identity_between_slices",
            desc: "KS(a4,0; dk, v_t, lambda) = KS(0; dk e^{-a4,0}, v_t e^{-3 a4,0}, lambda), solved independently: same label set and occupations, max |delta eps| (units of m)",
            tol: 1e-9,
            value: de,
            pass: Some(same_keys && occ_same && de <= 1e-9),
        });
        out.items.push(it("rescaling_identity_energy_profiles", "rescaling partner: relative difference of E_KS and max relative difference of the proper profiles n, S, rho, p3, p8", 1e-8, d_e.max(pd)));
        out.rescale = Some(vec![id.clone(), (n as i64).to_string(), out.tag.clone(), f(lam), f(a4), f(pr.dk), f(pr.vt), same_keys.to_string(), occ_same.to_string(), f(de), f(d_e), f(pd), f(gr_r.e_ks)]);
    }
    // exact-Fock variant (lambda != 0)
    if lam != 0.0 {
        let mut px = phys.clone();
        px.functional = Functional::Exx;
        let inp = RunInput { phys: px.clone(), num, co, specs: gs.specs.clone(), occ: Occ::Aufbau, start: Some(gs.pots.clone()), guesses: guesses_of(&gs) };
        let sx = match run_scf(grid, &inp) {
            Ok(mut s) => {
                s.path = "direct".into();
                s
            }
            Err(e1) => {
                // continuation in the weight of the exact-Fock term
                let num2 = Numerics { anderson_beta: num.anderson_beta / 2.0, scf_max_iter: 2 * num.scf_max_iter, ..num.clone() };
                let mut start = gs.pots.clone();
                let mut g = guesses_of(&gs);
                let mut last = None;
                for fr in [0.25, 0.5, 0.75, 1.0] {
                    let mut pf = px.clone();
                    pf.exx_frac = fr;
                    let s = run_scf(grid, &RunInput { phys: pf, num: &num2, co, specs: gs.specs.clone(), occ: Occ::Aufbau, start: Some(start.clone()), guesses: g.clone() }).map_err(|e| format!("exact-Fock variant: direct: {}; continuation at {}: {}", e1, fr, e))?;
                    start = s.pots.clone();
                    g = guesses_of(&s);
                    last = Some(s);
                }
                let mut s = last.unwrap();
                s.path = "continuation in the exact-Fock weight 1/4, 1/2, 3/4, 1".into();
                s
            }
        };
        let ex = emt(&px, co, &sx);
        let cx = emt_checks(grid, &px, &sx, &ex);
        let grx = groups(&sx, num.deg_tol);
        let hx = grx.iter().filter(|(_, m)| m.iter().any(|&i| sx.occ[i] > 1e-12)).map(|(e, _)| *e).fold(f64::NEG_INFINITY, f64::max);
        let lx = grx.iter().filter(|(e, m)| *e > hx && m.iter().any(|&i| sx.occ[i] < 1.0 - 1e-12)).map(|(e, _)| *e).fold(f64::INFINITY, f64::min);
        out.items.push(it("exx_variant_scf_converged", "exact-Fock-exchange variant (w_Q = lambda Q/16 sigma3, + lambda Q^2/32) converged from the uniform-gas state", num.scf_tol, sx.resid));
        out.items.push(it("exx_variant_y_conservation", "exact-Fock variant: (e^{6Hy} p8)' = 3H e^{6Hy}(p3 + p_t) with p8 including -w_Q Q (derived): integrated relative residual", 1e-7, cx.ycons_integrated_rel));
        out.exx = Some(vec![
            id.clone(),
            (n as i64).to_string(),
            out.tag.clone(),
            f(lam),
            f(a4),
            f(gs.e_ks),
            f(ec.delta_ex_fock),
            f(gs.e_ks + ec.delta_ex_fock),
            f(sx.e_ks),
            f(sx.e_ks - gs.e_ks - ec.delta_ex_fock),
            f(gap),
            f(lx - hx),
            sx.iters.to_string(),
            f(cx.ycons_integrated_rel),
        ]);
    }
    // files and rows
    out.files.push((format!("ground/levels/{}.csv", id), levels_csv(&gs)));
    out.files.push((format!("ground/profiles/{}.csv", id), profile_csv(grid, &gs, &e)));
    let mx = |v: &[f64]| v.iter().fold(0.0f64, |m, x| m.max(x.abs()));
    let mmax = gs.pots.mass.iter().fold(0.0f64, |m, x| m.max((x - phys.m).abs()));
    let smin = gs.dens.s.iter().fold(f64::INFINITY, |m, &x| m.min(x));
    let smax = gs.dens.s.iter().fold(f64::NEG_INFINITY, |m, &x| m.max(x));
    let nshells = gs.specs.iter().map(|s| s.shell.n2).collect::<std::collections::BTreeSet<_>>().len();
    out.summary = vec![
        id.clone(),
        (n as i64).to_string(),
        out.tag.clone(),
        f(lam),
        f(a4),
        gs.path.split(" after:").next().unwrap().to_string(),
        gs.iters.to_string(),
        f(gs.resid),
        f(gs.e_ks),
        f(gs.e_band),
        f(gs.e_int),
        f(gs.e_var),
        f(homo),
        f(lumo),
        f(gap),
        gs.open_shell.to_string(),
        f(mmax),
        f(mx(&gs.pots.v)),
        f(smin),
        f(smax),
        f(mx(&gs.dens.n)),
        gs.levels.len().to_string(),
        nshells.to_string(),
        f(e_complete),
    ];
    let nf = grid.nf;
    out.emtrow = vec![
        id.clone(),
        (n as i64).to_string(),
        out.tag.clone(),
        f(lam),
        f(a4),
        f(ec.int_rho),
        f(ec.int_p3),
        f(ec.int_pt),
        f(ec.int_p8),
        f(ec.int_n),
        f(e.rho[nf - 1]),
        f(e.p3[nf - 1]),
        f(e.pt[nf - 1]),
        f(e.p8[nf - 1]),
        f(e.rho[0]),
        f(e.p3[0]),
        f(e.pt[0]),
        f(e.p8[0]),
        f(ec.delta_ex_fock),
        f(ec.ycons_integrated_rel),
        f(ec.ycons_pointwise_rel),
        f(ec.trace_derivative_rel),
    ];
    let hist: Vec<Json> = gs.history.iter().map(|(i, r, e)| Json::Arr(vec![(*i).into(), (*r).into(), (*e).into()])).collect();
    out.record = obj(vec![
        ("id", id.clone().into()),
        ("N", n.into()),
        ("lambdaTag", out.tag.clone().into()),
        ("lambda", lam.into()),
        ("a4", a4.into()),
        ("path", gs.path.clone().into()),
        ("iterations", gs.iters.into()),
        ("rootEvaluations", gs.evals.into()),
        ("scfHistory_iteration_residual_E", Json::Arr(hist)),
        ("deltaScfIterations", exc.iters.into()),
        ("fdPlusIterations", stp.iters.into()),
        ("fdMinusIterations", stm.iters.into()),
        ("fd2PlusIterations", nbs[2].iters.into()),
        ("fd2MinusIterations", nbs[3].iters.into()),
    ]);
    out.occ = occ;
    out.e_ks = gs.e_ks;
    out.state = Some(gs);
    Ok(())
}

pub struct ThermOut {
    pub row: Vec<String>,
    pub items: Vec<Item>,
    pub id: String,
    pub holes_over_n: f64,
}

pub fn thermal_task(sh: &Shared, n: f64, tag: &str, lam: f64, a4: f64, temp: f64) -> ThermOut {
    let id = format!("{}_T{}", run_id(n, tag, a4), (temp * 1000.0).round() as i64);
    match thermal_inner(sh, n, tag, lam, a4, temp, &id) {
        Ok(o) => o,
        Err(e) => {
            eprintln!("ERROR {}: {}", id, e);
            ThermOut { row: vec![], items: vec![Item { name: "thermo_runs_completed", desc: "every thermal run (T, T(1 +- dt)) completed", tol: 0.0, value: 1.0, pass: Some(false) }], id, holes_over_n: f64::NAN }
        }
    }
}

pub const THERMO_HEADER: [&str; 28] = [
    "id", "N", "lambda_tag", "lambda", "a4", "T", "mu", "E", "entropy", "F", "Omega_direct", "Omega_F_minus_muN", "C_V", "C_V_from_dEdT", "minus_dFdT", "levels", "shells", "window_cut", "f_at_window_cut", "sea_holes_excluded", "iterations", "residual", "E_T0", "max_abs_Meff_minus_m", "max_abs_v_v", "N_check", "sea_holes_over_N", "particle_only_convention_within_1pc",
];

fn thermal_inner(sh: &Shared, n: f64, tag: &str, lam: f64, a4: f64, temp: f64, id: &str) -> Result<ThermOut, String> {
    let grid = &sh.grid;
    let num = sh.num;
    let co = sh.co;
    let mut phys = sh.base.clone();
    phys.n = n;
    phys.lambda = lam;
    phys.a4 = a4;
    phys.temp = temp;
    let margin = 0.2 + 2.0 * sigma_of(tag);
    // T = 0 free Fermi level
    let mut f0 = phys.clone();
    f0.lambda = 0.0;
    f0.temp = 0.0;
    let specs0 = specs_t0(grid, &f0, 0.25, 1, num.root_tol)?;
    let free0 = run_scf(grid, &RunInput { phys: f0.clone(), num, co, specs: specs0, occ: Occ::Aufbau, start: None, guesses: BTreeMap::new() })?;
    let e_t0_free = free0.e_ks;
    let mut ecut = free0.mu + temp * (1.0 / num.f_cut).ln() + margin;
    let mut free_t;
    let mut specs;
    loop {
        specs = specs_thermal(grid, &phys, ecut, num.root_tol)?;
        let mut ft = phys.clone();
        ft.lambda = 0.0;
        free_t = run_scf(grid, &RunInput { phys: ft, num, co, specs: specs.clone(), occ: Occ::Mermin, start: None, guesses: BTreeMap::new() })?;
        let need = free_t.mu + temp * (1.0 / num.f_cut).ln() + margin;
        if need <= ecut + 1e-12 {
            break;
        }
        ecut = need + 0.05;
    }
    let run = |t: f64, start: Option<Pots>, g: BTreeMap<Key, f64>| -> Result<State, String> {
        let mut p = phys.clone();
        p.temp = t;
        run_scf(grid, &RunInput { phys: p, num, co, specs: specs.clone(), occ: Occ::Mermin, start, guesses: g })
    };
    let st = if lam == 0.0 { free_t.clone() } else { run(temp, None, guesses_of(&free_t))? };
    let dt = num.dt_rel * temp;
    let mut nb = Vec::new();
    for s in [1.0, -1.0, 2.0, -2.0] {
        nb.push(run(temp + s * dt, Some(st.pots.clone()), guesses_of(&st))?);
    }
    let e = st.e_ks;
    let s = st.entropy;
    let fr = e - temp * s;
    let om = fr - st.mu * n;
    let tv = [temp + dt, temp - dt, temp + 2.0 * dt, temp - 2.0 * dt];
    let fe: Vec<f64> = nb.iter().zip(&tv).map(|(x, t)| x.e_ks - t * x.entropy).collect();
    let cv = rich(nb[0].e_ks, nb[1].e_ks, nb[2].e_ks, nb[3].e_ks, dt);
    let tds = temp * rich(nb[0].entropy, nb[1].entropy, nb[2].entropy, nb[3].entropy, dt);
    let mdf = -rich(fe[0], fe[1], fe[2], fe[3], dt);
    let ntot: f64 = st.levels.iter().zip(&st.occ).map(|(l, f)| l.deg * f).sum();
    let fcut = fermi((ecut - st.mu) / temp);
    let maxn2w = specs.iter().map(|s| s.shell.n2).max().unwrap_or(0);
    let mut beyond = f64::INFINITY;
    for nx in shells(maxn2w + 200).into_iter().filter(|s| s.n2 > maxn2w).take(5) {
        for (j, par) in SECTORS {
            let (_, e) = free_sector_upto(grid, &phys, nx, j, par, f64::INFINITY, num.root_tol, 1)?;
            beyond = beyond.min(e[0]);
        }
    }
    // sea holes excluded by the convention: j = -1 even l = 0 (sea brane band) of every shell up to the window
    let ctx = ctx_for(grid, &phys, &st.pots);
    let maxn2 = specs.iter().map(|s| s.shell.n2).max().unwrap_or(0);
    let mut holes = 0.0;
    for shl in shells(maxn2) {
        if shl.n2 == 0 {
            continue;
        }
        let sec = Sector { k: kmag(&phys, shl), j: -1, parity: Parity::Even };
        let (es, _) = find_level(&ctx, sec, 0.0, -0.5 * kmag(&phys, shl) * (-a4).exp(), None, num.root_tol)?;
        holes += 4.0 * shl.r3 as f64 * fermi((st.mu - es) / temp);
    }
    let rel = |a: f64, b: f64| (a - b).abs() / a.abs().max(b.abs()).max(1e-300);
    let eta = n * num.root_tol / dt;
    let mut items = vec![
        it("thermo_scf_converged", "Mermin SCF converged at T, T +- dT, T +- 2 dT (dT = 0.01 T): max final residual", num.scf_tol, nb.iter().fold(st.resid, |m, x| m.max(x.resid))),
        it("thermo_N_conservation", "Mermin: |sum g f - N| at the converged mu", 1e-9, (ntot - n).abs()),
        it("thermo_grand_potential_two_forms", "Omega = -T sum g ln(1 + e^{-(eps-mu)/T}) - 2 Vol_7 int e^{6Hy} e_int equals F - mu N = E - T S - mu N: relative difference", 1e-10, rel(st.omega_direct, om)),
        it("thermo_CV_identity", "C_V = T dS/dT (reported; S is computed from the occupations and is well conditioned) equals dE/dT at fixed N (self-consistent Mermin states at T +- dT, T +- 2 dT, dT = 0.01 T, Richardson): |difference| / (1e-4 max(|dE/dT|, |T dS/dT|) + eta), eta = N x root tolerance / dT the noise floor of a difference quotient of energies (it dominates only where the thermal change of E over dT is below ~1e-11, i.e. deep in the activated regime)", 1.0, (cv - tds).abs() / (1e-4 * cv.abs().max(tds.abs()) + eta)),
        it("thermo_entropy_identity", "-dF/dT = S (Richardson differences): |difference| / (1e-4 S + eta), eta as for thermo_CV_identity", 1.0, (mdf - s).abs() / (1e-4 * s.abs() + eta)),
        it("thermo_window_cut", "occupation at the thermal window cut f(ecut) (levels above the cut are omitted)", 2.0 * num.f_cut, fcut),
        Item { name: "thermo_window_shells_beyond", desc: "the free levels of the five shells beyond the thermal label set lie above the cut (value: cut - lowest such level, must be < 0)", tol: 0.0, value: ecut - beyond, pass: Some(beyond > ecut) },
    ];
    items.push(Item { name: "thermo_runs_completed", desc: "every thermal run (T, T(1 +- dt)) completed", tol: 0.0, value: 0.0, pass: Some(true) });
    let mmax = st.pots.mass.iter().fold(0.0f64, |m, x| m.max((x - phys.m).abs()));
    let vmax = st.pots.v.iter().fold(0.0f64, |m, x| m.max(x.abs()));
    let nshells = specs.iter().map(|s| s.shell.n2).collect::<std::collections::BTreeSet<_>>().len();
    let row = vec![
        id.to_string(),
        (n as i64).to_string(),
        tag.to_string(),
        f(lam),
        f(a4),
        f(temp),
        f(st.mu),
        f(e),
        f(s),
        f(fr),
        f(st.omega_direct),
        f(om),
        f(tds),
        f(cv),
        f(mdf),
        st.levels.len().to_string(),
        nshells.to_string(),
        f(ecut),
        f(fcut),
        f(holes),
        st.iters.to_string(),
        f(st.resid),
        f(e_t0_free),
        f(mmax),
        f(vmax),
        f(ntot),
        f(holes / n),
        (holes / n <= 0.01).to_string(),
    ];
    Ok(ThermOut { row, items, id: id.to_string(), holes_over_n: holes / n })
}

pub fn write_files(out: &std::path::Path, files: &BTreeMap<String, String>) -> Result<(), String> {
    for (p, c) in files {
        let path = out.join(p);
        if let Some(d) = path.parent() {
            std::fs::create_dir_all(d).map_err(|e| e.to_string())?;
        }
        std::fs::write(&path, c.as_bytes()).map_err(|e| format!("{}: {}", path.display(), e))?;
    }
    Ok(())
}

pub fn run_all(cfg: &Cfg, th: &TheoryInputs, mut rep: Report) -> Result<bool, String> {
    let t_all = std::time::Instant::now();
    let mut timing: Vec<(String, f64)> = Vec::new();
    let num = &cfg.num;
    let base = base_phys();
    let co = Coeffs { meff: th.meff_coeff, vv: th.vv_coeff };
    let mut files: BTreeMap<String, String> = BTreeMap::new();
    // --- free spectra ----------------------------------------------------------
    let t0 = std::time::Instant::now();
    for (p, c) in free_checks(&base, num, th.slope_m1h1l3, &SLICES, &mut rep) {
        files.insert(p, c);
    }
    let grid = Grid::new(base.hh, base.l, num.g);
    // closed shells at every slice (free)
    let mut csv = Csv::new(vec!["a4", "N_closed", "eps_last_filled", "eps_next", "gap", "levels_of_the_last_group"]);
    let mut shells_a0 = Vec::new();
    for &a4 in &SLICES {
        let mut ph = base.clone();
        ph.a4 = a4;
        let cs = closed_shells(&grid, &ph, 1.6, num.root_tol);
        for (cum, e0, next, names) in &cs {
            csv.push(vec![f(a4), format!("{}", *cum as i64), f(*e0), f(*next), f(next - e0), names.clone()]);
        }
        if a4 == 0.0 {
            shells_a0 = cs;
        }
    }
    files.insert("spectrum/closed-shells.csv".into(), csv.text());
    // N choice (documented rule): bulk edge = lowest level that is not on the even j = +1 brane band
    let bulk_edge = {
        let pots = Pots::free(grid.nf, base.m);
        let odd = crate::spectrum::level_in(&grid, &base, &pots, 0.0, 1, Parity::Odd, 0, num.root_tol);
        let even1 = crate::spectrum::level_in(&grid, &base, &pots, 0.0, 1, Parity::Even, 1, num.root_tol);
        odd.min(even1)
    };
    let below: Vec<&(f64, f64, f64, String)> = shells_a0.iter().filter(|x| x.1 < bulk_edge && x.2 - x.1 > 1e-6).collect();
    let n_large = below.last().map(|x| x.0).ok_or("no closed shell below the bulk edge")?;
    let n_mid = below.iter().map(|x| x.0).filter(|&c| c >= 8.0).min_by(|a, b| ((a - (n_large / 4.0)).abs()).partial_cmp(&(b - n_large / 4.0).abs()).unwrap()).unwrap();
    let ns: Vec<f64> = if cfg.quick { vec![8.0, n_mid] } else { vec![8.0, n_mid, n_large] };
    timing.push(("free spectra and closed shells".into(), t0.elapsed().as_secs_f64()));
    // --- calibration -----------------------------------------------------------
    let t0 = std::time::Instant::now();
    let mut lambdas: BTreeMap<i64, (f64, f64, f64)> = BTreeMap::new();
    let mut calib = Vec::new();
    for &n in &ns {
        let mut per_slice = Vec::new();
        for &a4 in &SLICES {
            let mut ph = base.clone();
            ph.n = n;
            ph.a4 = a4;
            let specs = specs_t0(&grid, &ph, 0.25, 3, num.root_tol)?;
            let st = run_scf(&grid, &RunInput { phys: ph.clone(), num, co, specs, occ: Occ::Aufbau, start: None, guesses: BTreeMap::new() })?;
            per_slice.push((0..grid.nf).map(|p| (th.meff_coeff * st.dens.s[p]).abs().max((th.vv_coeff * st.dens.n[p]).abs())).fold(0.0f64, f64::max));
        }
        let strength = per_slice.iter().cloned().fold(0.0f64, f64::max);
        let l1 = round_sig(SIGMAS[0] / strength, 4);
        let l2 = round_sig(SIGMAS[1] / strength, 4);
        lambdas.insert(n as i64, (l1, l2, strength));
        calib.push(obj(vec![
            ("N", n.into()),
            ("strengthPerLambda", strength.into()),
            ("strengthPerLambdaAtSlices", per_slice.clone().into()),
            ("lambda1", l1.into()),
            ("lambda2", l2.into()),
            ("firstOrderPotential1", (l1 * strength).into()),
            ("firstOrderPotential2", (l2 * strength).into()),
            ("lambda1OverVol7", (l1 / base.vol7()).into()),
            ("lambda2OverVol7", (l2 / base.vol7()).into()),
        ]));
    }
    timing.push(("calibration".into(), t0.elapsed().as_secs_f64()));
    // --- ground matrix ------------------------------------------------------------
    let t0 = std::time::Instant::now();
    let tags = ["lam0", "lamp1", "lamm1", "lamp2", "lamm2"];
    let mut tasks: Vec<(f64, &str, f64, usize)> = Vec::new();
    for &n in &ns {
        let (l1, l2, _) = lambdas[&(n as i64)];
        for tag in tags {
            let lam = match tag {
                "lamp1" => l1,
                "lamm1" => -l1,
                "lamp2" => l2,
                "lamm2" => -l2,
                _ => 0.0,
            };
            if cfg.quick && (tag == "lamp2" || tag == "lamm2") {
                continue;
            }
            for ia in 0..SLICES.len() {
                if cfg.quick && ia % 2 == 1 {
                    continue;
                }
                tasks.push((n, tag, lam, ia));
            }
        }
    }
    let shared = Shared { grid: Grid::new(base.hh, base.l, num.g), num, co, base: base.clone() };
    let mut gouts = par_map(&tasks, cfg.threads, |t| {
        let tt = std::time::Instant::now();
        let o = ground_task(&shared, t.0, t.1, t.2, t.3);
        eprintln!("done {} in {:.1} s", o.id, tt.elapsed().as_secs_f64());
        o
    });
    timing.push(("ground matrix (ground, a4 +- delta, Delta-SCF, rescaling partner, exact-Fock variant)".into(), t0.elapsed().as_secs_f64()));
    let mut agg = Agg::default();
    let mut sum_csv = Csv::new(SUMMARY_HEADER.to_vec());
    let mut exc_csv = Csv::new(vec!["id", "N", "lambda_tag", "lambda", "a4", "HOMO", "LUMO", "KS_gap", "g_HOMO_group", "g_LUMO_group", "hole_levels", "particle_levels", "E_excited", "delta_SCF", "delta_SCF_minus_gap", "iterations", "residual"]);
    let mut ad_csv = Csv::new(vec!["id", "N", "lambda_tag", "lambda", "a4", "Q_max", "Q_max_pair", "Q_max_delta_eps", "Q_max_matrix_element", "transition_probability_estimate_Q2", "pairs", "HF_max_dev", "max_abs_deps_da4", "dE_da4_finite_difference", "dE_da4_emt"]);
    let mut emt_csv = Csv::new(vec!["id", "N", "lambda_tag", "lambda", "a4", "int_rho", "int_p3", "int_p_t", "int_p8", "int_n", "rho_brane", "p3_brane", "p_t_brane", "p8_brane", "rho_tip", "p3_tip", "p_t_tip", "p8_tip", "deltaE_x_exact_fock", "ycons_integrated_rel", "ycons_pointwise_rel", "trace_derivative_rel"]);
    let mut rs_csv = Csv::new(vec!["id", "N", "lambda_tag", "lambda", "a4", "partner_dk", "partner_v_t", "same_label_set", "same_occupations", "max_abs_delta_eps", "rel_delta_E", "max_rel_profile_diff", "partner_E_KS"]);
    let mut exx_csv = Csv::new(vec!["id", "N", "lambda_tag", "lambda", "a4", "E_uniform_gas", "deltaE_x_exact_fock_diag", "E_uniform_gas_plus_deltaE_x", "E_exact_fock_scf", "E_exx_minus_first_order", "gap_uniform_gas", "gap_exact_fock", "iterations", "ycons_integrated_rel"]);
    let mut records = Vec::new();
    for o in &gouts {
        for x in &o.items {
            agg.add(&o.id, x);
        }
        for (p, c) in &o.files {
            files.insert(p.clone(), c.clone());
        }
        if o.error.is_none() {
            sum_csv.push(o.summary.clone());
            exc_csv.push(o.excited.clone());
            ad_csv.push(o.adiab.clone());
            emt_csv.push(o.emtrow.clone());
            if let Some(r) = &o.rescale {
                rs_csv.push(r.clone());
            }
            if let Some(r) = &o.exx {
                exx_csv.push(r.clone());
            }
            records.push(o.record.clone());
        } else {
            records.push(obj(vec![("id", o.id.clone().into()), ("error", o.error.clone().unwrap().into())]));
        }
    }
    files.insert("ground/summary.csv".into(), sum_csv.text());
    files.insert("ground/emt-integrals.csv".into(), emt_csv.text());
    files.insert("ground/runs.json".into(), to_pretty(&Json::Arr(records)));
    files.insert("excited/summary.csv".into(), exc_csv.text());
    files.insert("adiabatic/adiabaticity.csv".into(), ad_csv.text());
    files.insert("rescaling/rescaling.csv".into(), rs_csv.text());
    files.insert("exx/exact-fock-variant.csv".into(), exx_csv.text());
    // --- history: crossings at the Fermi level and the adiabatically continued state
    let t0 = std::time::Instant::now();
    let mut series: BTreeMap<(i64, String), Vec<usize>> = BTreeMap::new();
    for (i, o) in gouts.iter().enumerate() {
        series.entry((o.n as i64, o.tag.clone())).or_default().push(i);
    }
    let mut cont_tasks: Vec<(usize, usize)> = Vec::new();
    let mut hist_json = Vec::new();
    let mut hist_csv = Csv::new(vec!["N", "lambda_tag", "a4_from", "a4_to", "occupied_set_changed", "labels_left", "labels_entered"]);
    for ((n, tag), idx) in &series {
        let ok = idx.iter().all(|&i| gouts[i].error.is_none());
        if !ok {
            continue;
        }
        let first = idx[0];
        let mut changes = Vec::new();
        for w in idx.windows(2) {
            let (a, b) = (&gouts[w[0]], &gouts[w[1]]);
            let left: Vec<String> = a.occ.keys().filter(|k| !b.occ.contains_key(k)).map(key_str).collect();
            let entered: Vec<String> = b.occ.keys().filter(|k| !a.occ.contains_key(k)).map(key_str).collect();
            let changed = a.occ != b.occ;
            hist_csv.push(vec![n.to_string(), tag.clone(), f(SLICES[a.ia]), f(SLICES[b.ia]), changed.to_string(), left.join(";"), entered.join(";")]);
            if changed {
                changes.push(format!("{} -> {}", SLICES[a.ia], SLICES[b.ia]));
            }
        }
        for &i in idx.iter().skip(1) {
            if gouts[i].occ != gouts[first].occ {
                cont_tasks.push((first, i));
            }
        }
        hist_json.push(obj(vec![("N", (*n).into()), ("lambdaTag", tag.clone().into()), ("fermiLevelCrossings", Json::Arr(changes.into_iter().map(Json::from).collect()))]));
    }
    let conts = par_map(&cont_tasks, cfg.threads, |&(i0, i)| {
        let g0 = &gouts[i0];
        let gi = &gouts[i];
        let st = gi.state.as_ref().unwrap();
        let r = fixed_run(&shared.grid, &st.phys, num, co, st, g0.occ.clone());
        (gi.id.clone(), gi.e_ks, r.map(|s| (s.e_ks, s.resid)))
    });
    let mut cont_csv = Csv::new(vec!["id", "E_aufbau_instantaneous_ground", "E_adiabatically_continued", "difference", "residual", "status"]);
    for (id, eg, r) in &conts {
        match r {
            Ok((e, res)) => {
                cont_csv.push(vec![id.clone(), f(*eg), f(*e), f(e - eg), f(*res), "converged".into()]);
                agg.add(id, &Item { name: "adiabatic_continued_state_not_lower", desc: "where the occupied label set changes along the history, the adiabatically continued state (a4,0 = 0 occupations) is not below the instantaneous aufbau ground state (value: E_aufbau - E_continued)", tol: 1e-9, value: eg - e, pass: None });
            }
            Err(e) => cont_csv.push(vec![id.clone(), f(*eg), "nan".into(), "nan".into(), "nan".into(), format!("failed: {}", e.replace(',', ";"))]),
        }
    }
    // crossing demonstration (not part of the canonical N): lambda = 0, N_demo
    let n_demo = shells_a0.iter().filter(|x| x.0 > 8.0).find(|x| x.3.split(';').any(|lv| !lv.contains(":+1:even:0"))).map(|x| x.0).unwrap_or(f64::NAN);
    let mut demo_csv = Csv::new(vec!["N", "a4", "occupied_set_equal_to_a4_0", "open_shell", "E_aufbau", "E_adiabatically_continued", "difference", "labels_left", "labels_entered"]);
    if n_demo.is_finite() && !cfg.quick {
        let mut demo_states: Vec<State> = Vec::new();
        for &a4 in &SLICES {
            let mut ph = base.clone();
            ph.n = n_demo;
            ph.a4 = a4;
            let specs = specs_t0(&grid, &ph, 0.25, 3, num.root_tol)?;
            demo_states.push(run_scf(&grid, &RunInput { phys: ph, num, co, specs, occ: Occ::Aufbau, start: None, guesses: BTreeMap::new() })?);
        }
        let occ0 = occ_map(&demo_states[0]);
        let mut flagged = false;
        let mut cont_ok = true;
        for st in &demo_states {
            let oc = occ_map(st);
            let left: Vec<String> = occ0.keys().filter(|k| !oc.contains_key(k)).map(key_str).collect();
            let entered: Vec<String> = oc.keys().filter(|k| !occ0.contains_key(k)).map(key_str).collect();
            let same = oc == occ0;
            let ec = if same { st.e_ks } else { fixed_run(&grid, &st.phys, num, co, st, occ0.clone())?.e_ks };
            if !same {
                flagged = true;
                cont_ok &= ec >= st.e_ks - 1e-12;
            }
            demo_csv.push(vec![format!("{}", n_demo as i64), f(st.phys.a4), same.to_string(), st.open_shell.to_string(), f(st.e_ks), f(ec), f(ec - st.e_ks), left.join(";"), entered.join(";")]);
        }
        rep.check(
            "adiabatic_crossing_flag_demonstration",
            flagged && cont_ok,
            format!("lambda = 0, N = {} (the smallest closed shell of the a4,0 = 0 aufbau that occupies a level off the even j = +1 brane band): the brane-band levels redshift below the k = 0 bulk level along the history, the instantaneous aufbau occupation changes (flagged: {}) and the adiabatically continued state (a4,0 = 0 labels) lies at or above the aufbau ground state at every flagged slice: {} (adiabatic/crossing-demo.csv)", n_demo as i64, flagged, cont_ok),
        );
    }
    files.insert("adiabatic/crossing-demo.csv".into(), demo_csv.text());
    files.insert("adiabatic/fermi-level-crossings.csv".into(), hist_csv.text());
    files.insert("adiabatic/continued-states.csv".into(), cont_csv.text());
    files.insert("adiabatic/history.json".into(), to_pretty(&obj(vec![("A", A_HIST.into()), ("slices", SLICES.to_vec().into()), ("series", Json::Arr(hist_json))])));
    for o in gouts.iter_mut() {
        o.state = None;
    }
    timing.push(("history (crossings, continued states)".into(), t0.elapsed().as_secs_f64()));
    // --- thermodynamics -------------------------------------------------------------
    let t0 = std::time::Instant::now();
    let mut ttasks: Vec<(f64, &str, f64, f64, f64)> = Vec::new();
    for &n in &ns {
        let (l1, _, _) = lambdas[&(n as i64)];
        for (tag, lam) in [("lam0", 0.0), ("lamp1", l1), ("lamm1", -l1)] {
            for &a4 in &SLICES {
                for &t in &TEMPS {
                    if cfg.quick && (a4 != 0.0 && a4 != 2.0 || t != TEMPS[1]) {
                        continue;
                    }
                    ttasks.push((n, tag, lam, a4, t));
                }
            }
        }
    }
    let touts = par_map(&ttasks, cfg.threads, |t| {
        let tt = std::time::Instant::now();
        let o = thermal_task(&shared, t.0, t.1, t.2, t.3, t.4);
        eprintln!("done {} in {:.1} s", o.id, tt.elapsed().as_secs_f64());
        o
    });
    let mut th_csv = Csv::new(THERMO_HEADER.to_vec());
    for o in &touts {
        for x in &o.items {
            agg.add(&o.id, x);
        }
        if !o.row.is_empty() {
            th_csv.push(o.row.clone());
        }
    }
    files.insert("thermo/thermodynamics.csv".into(), th_csv.text());
    {
        let bad: Vec<String> = touts.iter().filter(|o| o.holes_over_n > 0.01).map(|o| format!("{} ({:.3})", o.id, o.holes_over_n)).collect();
        let worst = touts.iter().map(|o| o.holes_over_n).fold(0.0f64, f64::max);
        rep.check(
            "thermo_sea_hole_diagnostic_computed",
            touts.iter().all(|o| o.holes_over_n.is_finite()),
            format!(
                "DIAGNOSTIC of the filling CONVENTION (not a validation): for every thermal state the number of thermal holes the excluded sea brane band (j = -1, even, l = 0, eps < 0) would carry at the same mu and T was computed; it exceeds 1% of N in {} of {} states (largest {:.3} N): there the particle-only Mermin ensemble is outside its range of validity and a thermal treatment of the sea (pairs) would be required; listed: {}",
                bad.len(),
                touts.len(),
                worst,
                if bad.is_empty() { "none".to_string() } else { bad.join(", ") }
            ),
        );
    }
    timing.push(("thermodynamics".into(), t0.elapsed().as_secs_f64()));
    // T3 solver self-test: the block form of Gamma maps (j, M) -> (-j, -M) and swaps the brane
    // parities and the tip condition b(-L) = 0 -> a(-L) = 0 (tip theta = pi): the instantaneous
    // problem with (m, lambda) and the one with (-m, lambda) and the transformed tip must have equal
    // spectra, energies and energy-momentum integrals, S -> -S.
    {
        let t0 = std::time::Instant::now();
        let mut lines = Vec::new();
        let mut ok = true;
        let mut worst: f64 = 0.0;
        for &n in ns.iter().take(2) {
            let lam = lambdas[&(n as i64)].0;
            let mut pa = base.clone();
            pa.n = n;
            pa.lambda = lam;
            pa.a4 = 1.0;
            let mut pb = pa.clone();
            pb.m = -base.m;
            pb.tip_theta = std::f64::consts::PI;
            let mut pc = pa.clone();
            pc.m = -base.m;
            let solve = |ph: &Physics| -> Result<State, String> {
                let specs = specs_t0(&grid, ph, margin_for("lamp1"), 3, num.root_tol)?;
                let mut fp = ph.clone();
                fp.lambda = 0.0;
                let free = run_scf(&grid, &RunInput { phys: fp, num, co, specs: specs.clone(), occ: Occ::Aufbau, start: None, guesses: BTreeMap::new() })?;
                solve_ground(&grid, ph, num, co, &specs, &guesses_of(&free))
            };
            let a = solve(&pa)?;
            let b = solve(&pb)?;
            let mut la: Vec<(f64, f64, f64)> = a.levels.iter().zip(&a.occ).map(|(l, f)| (l.eps, l.deg, *f)).collect();
            let mut lb: Vec<(f64, f64, f64)> = b.levels.iter().zip(&b.occ).map(|(l, f)| (l.eps, l.deg, *f)).collect();
            la.sort_by(|x, y| x.partial_cmp(y).unwrap());
            lb.sort_by(|x, y| x.partial_cmp(y).unwrap());
            let same_len = la.len() == lb.len();
            let de = la.iter().zip(&lb).fold(0.0f64, |m, (x, y)| m.max((x.0 - y.0).abs()).max((x.1 - y.1).abs()).max((x.2 - y.2).abs()));
            let ea = emt(&pa, co, &a);
            let eb = emt(&pb, co, &b);
            let ca = emt_checks(&grid, &pa, &a, &ea);
            let cb = emt_checks(&grid, &pb, &b, &eb);
            let dint = [(ca.int_rho, cb.int_rho), (ca.int_p3, cb.int_p3), (ca.int_pt, cb.int_pt), (ca.int_p8, cb.int_p8)].iter().fold(0.0f64, |m, (x, y)| m.max((x - y).abs() / x.abs().max(1.0)));
            let smax = a.dens.s.iter().fold(0.0f64, |m, x| m.max(x.abs())).max(1e-300);
            let ds = a.dens.s.iter().zip(&b.dens.s).fold(0.0f64, |m, (x, y)| m.max((x + y).abs())) / smax;
            let d_en = (a.e_ks - b.e_ks).abs() / a.e_ks.abs().max(1.0);
            let w = de.max(dint).max(ds).max(d_en);
            worst = worst.max(w);
            ok &= same_len && w < 1e-9;
            let ctrl = match solve(&pc) {
                Ok(c) => format!("negative control (-m, lambda, untransformed tip b(-L) = 0): E_KS = {:.10e} vs {:.10e} (difference {:.3e})", c.e_ks, a.e_ks, c.e_ks - a.e_ks),
                Err(e) => format!("negative control (-m, lambda, untransformed tip): no state ({})", e),
            };
            lines.push(format!("N = {}, lambda = {}, a4,0 = 1: E_KS {:.12e} vs {:.12e}; {} levels; max |delta| of sorted (eps, g, f) {:.2e}, EMT integrals {:.2e}, |S_a + S_b|/max|S| {:.2e}; {}", n as i64, lam, a.e_ks, b.e_ks, la.len(), de, dint, ds, ctrl));
        }
        rep.check(
            "t3_block_map_solver_selftest",
            ok,
            format!("numerical self-test of the solver for the Kohn-Sham-level block map of ks-theory.json blockForms.Gamma (NOT a proof of T3, which is owned by Revision/pairing/kohn_sham and not established here): (m, lambda, tip theta = 0) and (-m, lambda, tip theta = pi) solved independently give the same sorted levels, occupations, E_KS and EMT integrals and opposite S (worst {:.2e}, tolerance 1e-9): {}", worst, lines.join(" | ")),
        );
        timing.push(("T3 self-test".into(), t0.elapsed().as_secs_f64()));
    }
    agg.into_report(&mut rep);
    // --- parameters ------------------------------------------------------------------
    let params = obj(vec![
        ("description", "Revision Kohn-Sham solver (Revision/kohn_sham/solver): instantaneous Kohn-Sham states of dirac16complex in the author's primordial field along the deflating history (SPEC section 7, Revision/kohn_sham/ks-theory.json). x1..x3 = 3-space, x4 = time, x5..x7 = the exponentially deflating extra times (scale factor e^{-a4} sin^{1/6} z), x8 = hidden direction (y = ln(sin z)/(6H)).".into()),
        ("theoryInputs", inputs_json(th)),
        ("units", "H = 1, m = 1: energies, momenta, temperatures in units of m = H; lambda in units of m^-6 with Vol_7 in units of H^-7".into()),
        ("physics", obj(vec![("H", base.hh.into()), ("m", base.m.into()), ("L_tipCutoff", base.l.into()), ("dk", base.dk.into()), ("ell", base.ell().into()), ("v_t", base.vt.into()), ("Vol7", base.vol7().into()), ("tipTheta", base.tip_theta.into()), ("historyA", A_HIST.into()), ("slicesA4", SLICES.to_vec().into()), ("temperatures", TEMPS.to_vec().into())])),
        ("numerics", obj(vec![("tag", num.tag.into()), ("rk4Steps", num.g.into()), ("rootTolerance", num.root_tol.into()), ("scfTolerance", num.scf_tol.into()), ("scfMaxIterations", num.scf_max_iter.into()), ("andersonDepth", num.anderson_depth.into()), ("andersonBeta", num.anderson_beta.into()), ("thermalOccupationCut", num.f_cut.into()), ("a4FiniteDifferenceStep", num.fd_delta.into()), ("temperatureFiniteDifferenceRelative", num.dt_rel.into()), ("degeneracyTolerance", num.deg_tol.into())])),
        ("particleNumbers", obj(vec![("values", ns.clone().into()), ("rule", "N = 8 (the k = 0 brane zero modes, both block types); N_large = the largest closed shell of the free a4,0 = 0 aufbau whose last filled level lies below the bulk edge (the lowest level not on the even j = +1 brane band: min of the odd l = 0 and even l = 1 levels at k = 0); N_mid = the closed shell (>= 8, below the bulk edge) nearest N_large / 4".into()), ("bulkEdge", bulk_edge.into()), ("N_mid", n_mid.into()), ("N_large", n_large.into())])),
        ("couplingCalibration", obj(vec![("rule", "per N, from the free ground states of that N at every slice a4,0 of the history: strength = max over the slices and over y of max((15/16)|S(y)|, |n(y)|/16) (proper densities), the first-order mean-field potential per unit lambda; lambda_1 = 0.1/strength and lambda_2 = 0.3/strength rounded to 4 significant digits, so that the first-order mean-field potential stays below 0.1 m and 0.3 m along the whole history (for N > 8 it is largest at the last slice: the redshifted brane-band orbitals spread towards the tip, where the proper 7-volume e^{6Hy} is small); lambda is a constant of the theory, the same at every slice".into()), ("values", Json::Arr(calib))])),
        ("conventions", obj(vec![
            ("particleNumber", "N = sum g f over both brane parities = particle number of the doubled (universe + Z2 image) system; the patch holds N/2 (ks-theory.json densities.total). The thermodynamics line 'mu fixed by sum w_Z2 g f = N' of ks-theory.json is inconsistent with this and with its own Omega = -T sum g ln(...) + ..., F = Omega + mu N; the solver uses sum g f = N (noted as a discrepancy of the theory file)".into()),
            ("filling", "particles occupy the positive branch (labels whose lambda = 0 level at the same slice is positive) and the k = 0 brane zero modes (CONVENTION of ks-theory.json, justification OPEN); the negative branch is the normal-ordered sea and is not populated thermally (the excluded thermal sea holes are reported as a diagnostic)".into()),
            ("brane", "Z2 mirror at y = 0: ASSUMED (b(0) = 0 even, a(0) = 0 odd); tip: regular, theta = 0 (b(-L) = 0)".into()),
            ("instantaneous", "states at fixed a4,0 = a4(x4) are instantaneous (adiabatic) Kohn-Sham states; the non-adiabatic (time-dependent) problem is OPEN".into()),
            ("deltaScf", "first excited state: one particle moved from the highest occupied degenerate group to the lowest empty group, spread uniformly over each group (ensemble Delta-SCF, keeps the block and direction symmetry of the reduction)".into()),
            ("exactExchange", "canonical functional = Hartree + exact local exchange of the uniform 8-fold gas (exact at every temperature for p -> -p symmetric occupations); the exact Fock exchange of the closed-shell slab determinant differs by +lambda Q^2/32 (reported as deltaE_x and solved as a variant)".into()),
        ])),
    ]);
    files.insert("parameters.json".into(), to_pretty(&params));
    // --- manifest, report ---------------------------------------------------------------
    let mut man = Vec::new();
    for (p, c) in &files {
        man.push(obj(vec![("path", p.clone().into()), ("bytes", c.len().into()), ("sha256", crate::sha256::hex(c.as_bytes()).into())]));
    }
    files.insert("manifest.json".into(), to_pretty(&obj(vec![("files", Json::Arr(man))])));
    // fresh output directory
    if cfg.out.exists() {
        let ok = cfg.out.join("manifest.json").exists() || std::fs::read_dir(&cfg.out).map(|mut d| d.next().is_none()).unwrap_or(false);
        if !ok {
            return Err(format!("{} exists and is not an output directory of this solver", cfg.out.display()));
        }
        std::fs::remove_dir_all(&cfg.out).map_err(|e| e.to_string())?;
    }
    write_files(&cfg.out, &files)?;
    let npass = rep.checks.iter().filter(|c| c.pass).count();
    let rj = obj(vec![
        ("report", "Revision Kohn-Sham Rust solver: checks of the canonical matrix (SPEC section 7)".into()),
        ("producer", "Revision/kohn_sham/solver (cargo run --release -- all)".into()),
        ("numerics", num.tag.into()),
        ("summary", obj(vec![("checks", rep.checks.len().into()), ("pass", npass.into()), ("fail", rep.n_fail().into())])),
        ("checks", rep.to_json()),
    ]);
    if let Some(d) = cfg.report.parent() {
        std::fs::create_dir_all(d).map_err(|e| e.to_string())?;
    }
    std::fs::write(&cfg.report, to_pretty(&rj)).map_err(|e| e.to_string())?;
    timing.push(("total".into(), t_all.elapsed().as_secs_f64()));
    if let Some(tp) = &cfg.timing {
        let tj = obj(vec![("threads", cfg.threads.into()), ("numerics", num.tag.into()), ("groundRuns", tasks.len().into()), ("thermalRuns", ttasks.len().into()), ("seconds", obj(timing.iter().map(|(k, v)| (k.as_str(), Json::from(*v))).collect()))]);
        std::fs::write(tp, to_pretty(&tj)).map_err(|e| e.to_string())?;
    }
    for (k, v) in &timing {
        eprintln!("time {}: {:.1} s", k, v);
    }
    Ok(rep.n_fail() == 0)
}

/// Options of the `single` subcommand.
pub struct SingleOpts {
    pub m: f64,
    pub lambda: f64,
    pub a4: f64,
    pub n: f64,
    pub tip_theta: f64,
    pub temp: f64,
    pub exx: bool,
    pub margin: f64,
    pub out: PathBuf,
    pub profiles: Option<PathBuf>,
}

/// One instantaneous Kohn-Sham state with user-chosen parameters (e.g. for the
/// T3 demonstration: m < 0 with the transformed tip condition, theta = pi).
/// Writes a JSON record (levels, energies, EMT integrals, identities).
pub fn run_single(num: &Numerics, th: &TheoryInputs, o: &SingleOpts) -> Result<bool, String> {
    let mut phys = base_phys();
    phys.m = o.m;
    phys.lambda = o.lambda;
    phys.a4 = o.a4;
    phys.n = o.n;
    phys.tip_theta = o.tip_theta;
    phys.temp = o.temp;
    if o.exx {
        phys.functional = Functional::Exx;
    }
    let co = Coeffs { meff: th.meff_coeff, vv: th.vv_coeff };
    let grid = Grid::new(phys.hh, phys.l, num.g);
    let (specs, occ) = if o.temp > 0.0 {
        let mut f0 = phys.clone();
        f0.lambda = 0.0;
        f0.temp = 0.0;
        let s0 = specs_t0(&grid, &f0, 0.25, 1, num.root_tol)?;
        let fr = run_scf(&grid, &RunInput { phys: f0, num, co, specs: s0, occ: Occ::Aufbau, start: None, guesses: BTreeMap::new() })?;
        let mut ecut = fr.mu + o.temp * (1.0 / num.f_cut).ln() + o.margin;
        loop {
            let sp = specs_thermal(&grid, &phys, ecut, num.root_tol)?;
            let mut ft = phys.clone();
            ft.lambda = 0.0;
            let st = run_scf(&grid, &RunInput { phys: ft, num, co, specs: sp.clone(), occ: Occ::Mermin, start: None, guesses: BTreeMap::new() })?;
            let need = st.mu + o.temp * (1.0 / num.f_cut).ln() + o.margin;
            if need <= ecut + 1e-12 {
                break (sp, Occ::Mermin);
            }
            ecut = need + 0.05;
        }
    } else {
        (specs_t0(&grid, &phys, o.margin, 3, num.root_tol)?, Occ::Aufbau)
    };
    let mut fp = phys.clone();
    fp.lambda = 0.0;
    let free = run_scf(&grid, &RunInput { phys: fp, num, co, specs: specs.clone(), occ: occ.clone(), start: None, guesses: BTreeMap::new() })?;
    let st = if o.lambda == 0.0 {
        free
    } else if o.temp > 0.0 || o.exx {
        run_scf(&grid, &RunInput { phys: phys.clone(), num, co, specs: specs.clone(), occ, start: None, guesses: guesses_of(&free) })?
    } else {
        solve_ground(&grid, &phys, num, co, &specs, &guesses_of(&free))?
    };
    let e = emt(&phys, co, &st);
    let c = emt_checks(&grid, &phys, &st, &e);
    let ntot: f64 = st.levels.iter().zip(&st.occ).map(|(l, f)| l.deg * f).sum();
    let levels: Vec<Json> = st
        .levels
        .iter()
        .zip(&st.occ)
        .map(|(l, f)| Json::Arr(vec![l.key.0.into(), l.key.1.into(), l.key.2.tag().into(), Json::Int(l.key.3), l.eps.into(), l.deg.into(), (*f).into()]))
        .collect();
    let rec = obj(vec![
        ("producer", "Revision/kohn_sham/solver single".into()),
        ("numerics", num.tag.into()),
        ("parameters", obj(vec![("H", phys.hh.into()), ("m", phys.m.into()), ("L", phys.l.into()), ("dk", phys.dk.into()), ("v_t", phys.vt.into()), ("a4", phys.a4.into()), ("lambda", phys.lambda.into()), ("N", phys.n.into()), ("T", phys.temp.into()), ("tipTheta", phys.tip_theta.into()), ("exactFockVariant", o.exx.into())])),
        ("iterations", st.iters.into()),
        ("residual", st.resid.into()),
        ("E_KS", st.e_ks.into()),
        ("E_band", st.e_band.into()),
        ("E_int", st.e_int.into()),
        ("mu_or_fermi_level", st.mu.into()),
        ("entropy", st.entropy.into()),
        ("particleNumber", ntot.into()),
        ("emtIntegrals_2Vol7_int_e6Hy", obj(vec![("rho", c.int_rho.into()), ("p3", c.int_p3.into()), ("p_t", c.int_pt.into()), ("p8", c.int_p8.into()), ("n", c.int_n.into())])),
        ("yConservationIntegratedRel", c.ycons_integrated_rel.into()),
        ("yConservationPointwiseRel", c.ycons_pointwise_rel.into()),
        ("levels_n2_j_parity_label_eps_deg_f", Json::Arr(levels)),
    ]);
    std::fs::write(&o.out, to_pretty(&rec)).map_err(|e| e.to_string())?;
    if let Some(p) = &o.profiles {
        std::fs::write(p, profile_csv(&grid, &st, &e)).map_err(|e| e.to_string())?;
    }
    Ok(st.resid <= num.scf_tol || o.lambda == 0.0)
}
