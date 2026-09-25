//! EXP-4 -- dirac16complex quanta as dark matter: Fermi-gas EoS and pair creation.
//!
//! # Background and mode equation
//!
//! 3-space FRW, hidden space and extra times static (b = c = 1), q = 0 good
//! sector: h_1 = h_2 = h_3 = a(t), V = a^3.  A mode
//! `Psi = V^{-1/2} e^{i k x1} u(t)` with comoving momentum k along x1 and
//! physical momentum K = k/a obeys (NUMERICS_CONTRACT, common physics)
//!
//! ```text
//! i du/dt = h(t) u,   h = -i m gamma^4 - K gamma^4 gamma^1,   h^2 = E^2 I,
//! E = sqrt(m^2 + K^2),   dh/dt = K H gamma^4 gamma^1   (dK/dt = -K H).
//! ```
//!
//! Every spinor is integrated as 32 real ODEs with CVODE (never by hand).
//! gamma^4 and gamma^4 gamma^1 are signed permutation matrices, so the RHS
//! is evaluated in that sparse form (bit-identical to the dense
//! `spinor::mode_rhs`, see the unit test).
//!
//! # Exact structure (used for the counting, verified numerically)
//!
//! * Direction: the Spin(3) generators S^{ij} (i, j in {1,2,3}) are unitary,
//!   commute with gamma^4 and B and rotate the gamma^4 gamma^j into each
//!   other, so a mode along any 3-space direction is unitarily equivalent to
//!   the one along x1.
//! * sigma_z := -i gamma^4 and sigma_x := -gamma^4 gamma^1 are Hermitian,
//!   square to I and anticommute: C^16 = C^2 (x) C^8 with
//!   h(t) = (m sigma_z + K sigma_x) (x) I_8.  Every positive-energy
//!   eigenvector is e_+ (x) chi, evolves as u_2(t) (x) chi, and all
//!   bilinears of h, gamma^4, gamma^4 gamma^1 are therefore independent of the
//!   "spin" chi (8-fold degeneracy): spin independence is exact.
//! * Charge conjugation: C h^* C = -h (C = gamma^0..gamma^3 real symmetric,
//!   C^2 = I, commutes with gamma^4, anticommutes with gamma^1), so
//!   u -> C u^* maps positive- to negative-energy solutions with
//!   eps(C u^*) = -eps(u), p_1(C u^*) = -p_1(u), s(C u^*) = -s(u): a hole
//!   (antiparticle) in a negative-energy mode v carries -eps(v) = eps(u).
//! * [B, h] = 0 in the good sector: u^dagger B u is conserved; the initial
//!   eigenvectors are chosen as joint eigenvectors with B = +1 (the second
//!   spin state of the spin-independence runs has B = -1).
//!
//! # Per-mode observables
//!
//! `eps = u^dag h u`, `p_1 = -K u^dag gamma^4 gamma^1 u`,
//! `s = u^dag (-i gamma^4) u`; identity `eps = m s + p_1` (h is that sum),
//! so KE_H per mode = p_1 (momentum energy) and PE_H per mode = m s (rest
//! mass; U = 0 for the free gas).  Lagrangian split: K_4 = eps, so
//! KE_L = PE_L = eps/2 (w_L = 0 for every free mode; p = KE - PE holds only
//! for homogeneous condensates, not for a gas -- reported, not used).
//! `beta2 = |P_- u|^2 / |u|^2` (weight on the instantaneous negative-energy
//! subspace; eps = E (1 - 2 beta2) for |u| = 1).  `beta2_adiabatic` is the
//! weight on the FIRST-ORDER adiabatic negative-frequency subspace,
//! `|P_- u + (i/(4E^2)) P_- hdot P_+ u|^2 / |u|^2`; it removes the adiabatic
//! dressing |beta_ad| = m K H/(4 E^3) of the instantaneous number.
//! (First-order adiabatic state: e + delta, delta = -(i/(4E^2)) Q hdot e,
//! Q the complementary spectral projector.)
//!
//! # (a) thermal Fermi gas, radiation era
//!
//! m = 1, comoving T_i = 10 at a_i = 1, H_i = 0.05, a = (t/t_i)^{1/2},
//! t_i = 1/(2 H_i) = 10, a from 1 to A_END.  k-grid: 48-node Gauss-Legendre
//! on [0, k_max = 12 T_i] (nodes computed here by Newton iteration and
//! written to thermal_grid.csv).  For each k: the positive-energy (B = +1)
//! eigenvector of h(t_i).  Fermi-Dirac f = 1/(exp(E_i/T_i) + 1),
//! E_i = sqrt(m^2 + k^2); 16 states per k (8 particles + 8 antiparticles,
//! the latter equal by charge conjugation).  With
//! `W_n = (16/(2 pi^2)) w_n k_n^2 f_n`:
//!
//! ```text
//! rho = sum W eps / a^3,  p = sum W p_1 / (3 a^3),  KE_H = sum W p_1 / a^3 = 3 p,
//! PE_H = m sum W s / a^3,  n a^3 = sum W u^dag u.
//! ```
//!
//! Isotropic pressure: the momentum-flux tensor of a mode with momentum
//! k n is n^i n^j K^2/E (on eigenmodes); for k along x1 its only nonzero
//! 3-space diagonal entry is T^1_1 = p_1 (p_2 = p_3 = 0 since k_2 = k_3 = 0);
//! the direction average <n^i n^j> = delta^{ij}/3 of the isotropic gas gives
//! p = (1/3) sum_i T^i_i = p_1/3 per mode.
//!
//! Extras: a second spin state (B = -1) for four k, a negative-energy mode
//! for one k (antiparticle symmetry), and the first-order adiabatic vacuum
//! for two trans-relativistic k (shows that the per-mode |beta|^2 of the
//! instantaneous-eigenvector start is the sudden-start free wave
//! |c|^2 = (m k H_i/(4 E_i^3))^2, not particle production).
//!
//! # (b) pair creation, de Sitter -> radiation
//!
//! a = exp(H_inf t) (t < 0, H_inf = 1) glued C^1 to a = (1 + 2 H_inf t)^{1/2}
//! (t > 0): a, H continuous at t = 0, dH/dt jumps from 0 to -2 H_inf^2.
//! The integration is restarted at t = 0 (two CVODE runs).  Vacuum initial
//! state: first-order adiabatic positive-frequency state at t0(k) with
//! k/a(t0) = K0 = 200 H_inf (t0 = ln(k/K0)/H_inf); its instantaneous
//! |beta|^2 is the dressing (m K0 H/(4 E0^3))^2 <= 1.6e-10.  End:
//! H(t_end) = 1e-4 m (a_end^2 = 1e4 H_inf/m; for m = 0 the m = 0.1 value),
//! where E >= m >> H.  Counting: the Dirac sea has 8 filled negative-energy
//! states per k; by the C^2 (x) C^8 structure each ends with weight |beta_k|^2
//! on the positive-energy subspace (= the positive mode's weight on the
//! negative subspace, by unitarity of the 2x2 block), i.e. 8 |beta_k|^2
//! particles + 8 |beta_k|^2 antiparticles per d^3k/(2 pi)^3:
//! `n a^3 = (16/(2 pi^2)) int k^2 |beta_k|^2 dk` (particles + antiparticles).
//! k-grid: 64-node Gauss-Legendre in ln k on [1e-3, 40].  The produced gas'
//! EoS uses the final (frozen) occupation:
//! `rho a^3 = (16/(2 pi^2)) int k^2 |beta_k|^2 E_k(a) dk`,
//! `p a^3 = (16/(2 pi^2)) int k^2 |beta_k|^2 K^2/(3E) dk`.
//! High-k tail (the C^1 kink): |beta_k|^2 -> (|Delta theta''|/(8 E^2))^2
//! = (m k/(4 E^4))^2 at a = 1 (theta = atan(K/m), Delta Hdot = -2 H_inf^2).

use std::f64::consts::PI;
use std::thread;

use crate::driver::{integrate, Integration, Method, RhsFn, SolverConfig};
use crate::math::{cos, exp, log};
use crate::output::{fmt17, standard_summary, write_csv, write_json, Json};
use crate::spinor::{
    energy_projector, energy_squared, involution_projector, mode_energy, mode_pressure,
    norm_hilbert, norm_krein, range_basis, scalar_density, Algebra, CMat16, CVec16, RMat16, N,
};
use crate::{ExperimentSummary, RunContext, Tolerances};

pub const EXPERIMENT: &str = "exp4";

// ---------------------------------------------------------------- (a) --
/// Particle mass (units m = 1).
pub const MASS: f64 = 1.0;
/// Initial comoving temperature T_i (a_i = 1).
pub const TEMPERATURE: f64 = 10.0;
/// Initial Hubble rate H_i (radiation era, H = 1/(2t)).
pub const HUBBLE_INITIAL: f64 = 0.05;
/// t_i = 1/(2 H_i).
pub const T_INITIAL: f64 = 1.0 / (2.0 * HUBBLE_INITIAL);
/// Final scale factor of the thermal run.
pub const A_END: f64 = 100.0;
/// k_max = 12 T_i.
pub const K_MAX: f64 = 12.0 * TEMPERATURE;
/// Gauss-Legendre nodes of the thermal momentum grid.
pub const N_K: usize = 48;
/// Output intervals, uniform in ln a.
pub const N_OUT: usize = 60;
/// States per comoving momentum: 8 particles + 8 antiparticles.
pub const DEGENERACY: f64 = 16.0;
/// Nodes that also get a second spin state (B = -1).
pub const SPIN_NODES: [usize; 4] = [2, 16, 32, 47];
/// Node that also gets a negative-energy (antiparticle) mode.
pub const ANTIPARTICLE_NODE: usize = 2;
/// Nodes that also start from the first-order adiabatic vacuum.
pub const ADIABATIC_VACUUM_NODES: [usize; 2] = [1, 2];
/// Nodes of the Adams-versus-BDF test and its window a in [1, A_METHOD_TEST].
pub const METHOD_TEST_NODES: [usize; 2] = [2, 47];
pub const A_METHOD_TEST: f64 = 2.0;
pub const METHOD_TEST_POINTS: usize = 8;

// ---------------------------------------------------------------- (b) --
pub const HUBBLE_INFLATION: f64 = 1.0;
/// k/a(t0) = K0 at the start of every pair-creation mode.
pub const K_OVER_A_START: f64 = 200.0;
pub const PAIR_MASSES: [f64; 5] = [0.0, 0.1, 0.5, 1.0, 2.0];
pub const PAIR_K_MIN: f64 = 1.0e-3;
pub const PAIR_K_MAX: f64 = 40.0;
pub const N_PAIR_K: usize = 64;
/// H(t_end) = HUBBLE_END_OVER_MASS * m.
pub const HUBBLE_END_OVER_MASS: f64 = 1.0e-4;
/// a_end^2 for m = 0 (the m = 0.1 value).
pub const MASSLESS_A2_END: f64 = 1.0e5;
/// Radiation-era samples, uniform in ln a on (1, a_end].
pub const N_PAIR_SAMPLES: usize = 6;
/// Points of the produced-gas EoS table (uniform in ln a on [1, a_end]).
pub const N_PAIR_EOS: usize = 60;
pub const PAIR_ANTIPARTICLE_MASS: f64 = 1.0;
pub const PAIR_ANTIPARTICLE_NODES: [usize; 3] = [20, 36, 48];
/// Tail comparison with the kink formula for k >= this value.
pub const PAIR_TAIL_K: f64 = 8.0;

/// Default tolerances.  Adams' norm leakage grows with the ~1e5 radians of
/// phase per thermal mode: max |u^dag u - 1| = 2.4e-4 (rtol 1e-10),
/// 2.3e-6 (1e-12), 2.4e-7 (1e-13), measured on this study; the a priori
/// unitarity limit 1e-6 therefore requires rtol = 1e-13 (limit not relaxed).
/// atol = 1e-14: with atol <= 1e-16 CVODE's initial-step heuristic sees
/// roundoff in initially-zero components and warns "t + h = t".
pub const DEFAULT_TOLERANCES: Tolerances = Tolerances {
    rtol: 1.0e-13,
    atol: 1.0e-14,
    max_step: 2.0,
};
/// CVodeSetMaxNumSteps per output interval.  At the refined tolerances
/// (rtol 1e-14) the long m = 0.1 radiation segment is roundoff limited and
/// needs ~1.2e6 steps in one interval (driver default 1e6).
pub const MAX_NUM_STEPS: i64 = 50_000_000;
/// Upper bound on worker threads (results do not depend on it).
pub const MAX_THREADS: usize = 8;

// ------------------------------------------------------------ limits --
pub const EIGEN_LIMIT: f64 = 1.0e-12;
pub const UNITARITY_LIMIT: f64 = 1.0e-6;
pub const KREIN_LIMIT: f64 = 1.0e-6;
pub const IDENTITY_LIMIT: f64 = 1.0e-12;
pub const KINETIC_LIMIT: f64 = 1.0e-6;
pub const SPIN_LIMIT: f64 = 1.0e-6;
pub const ANTIPARTICLE_LIMIT: f64 = 1.0e-6;
pub const BETA_LIMIT: f64 = 1.0e-6;
pub const MASSLESS_BETA_LIMIT: f64 = 1.0e-10;
/// Relative tolerance of the sudden-start prediction |c|^2 (second-order
/// adiabatic corrections O(H_i/E_i) to the amplitude).
pub const SUDDEN_START_LIMIT: f64 = 0.1;
/// Below this |c|^2 the late |beta|^2 is only bounded, not compared.
pub const SUDDEN_START_FLOOR: f64 = 1.0e-10;
/// Absolute allowance (numerical floor) in the |beta|^2 bounds.
pub const BETA_FLOOR: f64 = 1.0e-12;
/// Relative tolerance of the kink tail formula (next order O(H/E)).
pub const TAIL_LIMIT: f64 = 0.35;
pub const W_EARLY_LIMIT: f64 = 5.0e-3;
pub const W_LATE_MAX: f64 = 0.05;
pub const PAIR_W_LATE_MAX: f64 = 1.0e-3;

// ================================================================ math ==

/// Gauss-Legendre nodes (ascending) and weights on [-1, 1], by Newton
/// iteration on the three-term recurrence (exactly symmetric).
pub fn gauss_legendre(n: usize) -> (Vec<f64>, Vec<f64>) {
    let mut nodes = vec![0.0; n];
    let mut weights = vec![0.0; n];
    for i in 0..n.div_ceil(2) {
        let mut z = cos(PI * (i as f64 + 0.75) / (n as f64 + 0.5));
        for _ in 0..100 {
            let (p, dp) = legendre(n, z);
            let dz = p / dp;
            z -= dz;
            if dz.abs() <= 1.0e-16 {
                break;
            }
        }
        if n % 2 == 1 && i == n / 2 {
            z = 0.0;
        }
        let (_, dp) = legendre(n, z);
        let w = 2.0 / ((1.0 - z * z) * dp * dp);
        nodes[n - 1 - i] = z;
        nodes[i] = -z;
        weights[n - 1 - i] = w;
        weights[i] = w;
    }
    (nodes, weights)
}

/// (P_n(x), P_n'(x)).
fn legendre(n: usize, x: f64) -> (f64, f64) {
    let (mut p0, mut p1) = (1.0, x);
    for j in 2..=n {
        let jf = j as f64;
        let p2 = ((2.0 * jf - 1.0) * x * p1 - (jf - 1.0) * p0) / jf;
        p0 = p1;
        p1 = p2;
    }
    let dp = n as f64 * (x * p1 - p0) / (x * x - 1.0);
    (p1, dp)
}

/// Row i of a signed permutation matrix has its only nonzero entry
/// sign[i] = +-1 in column col[i].
#[derive(Clone, Copy, Debug)]
struct SignedPermutation {
    col: [usize; N],
    sign: [f64; N],
}

impl SignedPermutation {
    fn from_matrix(matrix: &RMat16, name: &str) -> Result<Self, String> {
        let mut col = [0usize; N];
        let mut sign = [0.0; N];
        for (i, row) in matrix.iter().enumerate() {
            let nonzero: Vec<usize> = (0..N).filter(|&j| row[j] != 0.0).collect();
            if nonzero.len() != 1 || row[nonzero[0]].abs() != 1.0 {
                return Err(format!("{name} is not a signed permutation (row {i})"));
            }
            col[i] = nonzero[0];
            sign[i] = row[nonzero[0]];
        }
        Ok(Self { col, sign })
    }
}

/// `i du/dt = h u`, `h = -i m gamma^4 - K gamma^4 gamma^1`, in the 32-real
/// layout (re0..re15, im0..im15).
#[derive(Clone, Copy, Debug)]
struct ModeOperator {
    g4: SignedPermutation,
    g41: SignedPermutation,
}

impl ModeOperator {
    fn new(alg: &Algebra) -> Result<Self, String> {
        Ok(Self {
            g4: SignedPermutation::from_matrix(&alg.gamma[4], "gamma^4")?,
            g41: SignedPermutation::from_matrix(&alg.g4g[1], "gamma^4 gamma^1")?,
        })
    }

    /// With h = hr + i hi, hr = -K gamma^4 gamma^1, hi = -m gamma^4:
    /// d(re)/dt = hr im + hi re, d(im)/dt = hi im - hr re.
    fn rhs(&self, mass: f64, kk: f64, y: &[f64], ydot: &mut [f64]) {
        for i in 0..N {
            let (c4, s4) = (self.g4.col[i], self.g4.sign[i]);
            let (c1, s1) = (self.g41.col[i], self.g41.sign[i]);
            ydot[i] = -kk * s1 * y[N + c1] - mass * s4 * y[c4];
            ydot[N + i] = -mass * s4 * y[N + c4] + kk * s1 * y[c1];
        }
    }
}

fn momenta(kk: f64) -> [f64; 8] {
    [0.0, kk, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
}

fn hamiltonian(alg: &Algebra, mass: f64, kk: f64) -> (CMat16, f64) {
    let kh = momenta(kk);
    (
        alg.mode_hamiltonian(mass, &kh),
        energy_squared(mass, &kh).sqrt(),
    )
}

/// dh/dt = K H gamma^4 gamma^1.
fn hamiltonian_rate(alg: &Algebra, kk: f64, hubble: f64) -> CMat16 {
    CMat16::from_real(&alg.g4g[1]).scale(kk * hubble, 0.0)
}

/// Unit joint eigenvector of h (energy sign) and B (b_sign).
fn eigen_state(
    alg: &Algebra,
    h: &CMat16,
    energy: f64,
    energy_sign: f64,
    b_sign: f64,
) -> Result<CVec16, String> {
    let projector =
        energy_projector(h, energy, energy_sign).mul(&involution_projector(&alg.b, b_sign));
    range_basis(&projector, 1.0e-8)
        .first()
        .copied()
        .ok_or_else(|| "empty joint (energy, B) eigenspace".to_string())
}

/// First-order adiabatic state e + delta, delta = -(i/(4E^2)) Q hdot e
/// (Q the complementary spectral projector), normalised.
fn adiabatic_state(h: &CMat16, hdot: &CMat16, energy: f64, energy_sign: f64, e: &CVec16) -> CVec16 {
    let delta = adiabatic_correction(h, hdot, energy, energy_sign, e);
    let u = e.axpy(1.0, 0.0, &delta);
    u.scale(1.0 / u.norm2().sqrt(), 0.0)
}

fn adiabatic_correction(
    h: &CMat16,
    hdot: &CMat16,
    energy: f64,
    energy_sign: f64,
    e: &CVec16,
) -> CVec16 {
    energy_projector(h, energy, -energy_sign)
        .apply(&hdot.apply(e))
        .scale(0.0, -1.0 / (4.0 * energy * energy))
}

/// Per-state observables (see the module header).
#[derive(Clone, Copy, Debug, Default)]
struct Diagnostics {
    energy: f64,
    eps: f64,
    p1: f64,
    s: f64,
    norm: f64,
    krein: f64,
    beta2: f64,
    beta2_adiabatic: f64,
}

/// `energy_sign = +1`: particle mode, beta2 = weight on the negative-energy
/// subspace; `-1`: negative-energy mode, beta2 = weight on the positive one.
fn diagnostics(
    alg: &Algebra,
    mass: f64,
    kk: f64,
    hubble: f64,
    u: &CVec16,
    energy_sign: f64,
) -> Diagnostics {
    let (h, energy) = hamiltonian(alg, mass, kk);
    let hdot = hamiltonian_rate(alg, kk, hubble);
    let norm = norm_hilbert(u);
    let hu = h.apply(u);
    let other = u.axpy(-energy_sign / energy, 0.0, &hu).scale(0.5, 0.0);
    let own = u.axpy(energy_sign / energy, 0.0, &hu).scale(0.5, 0.0);
    let rate_own = hdot.apply(&own);
    let h_rate_own = h.apply(&rate_own);
    let projected = rate_own
        .axpy(-energy_sign / energy, 0.0, &h_rate_own)
        .scale(0.5, 0.0);
    let adiabatic = other.axpy(0.0, 1.0 / (4.0 * energy * energy), &projected);
    Diagnostics {
        energy,
        eps: mode_energy(&h, u),
        p1: mode_pressure(alg, u, kk, 1),
        s: scalar_density(alg, u),
        norm,
        krein: norm_krein(alg, u),
        beta2: other.norm2() / norm,
        beta2_adiabatic: adiabatic.norm2() / norm,
    }
}

/// Map `f` over `items` on scoped worker threads (static interleaved
/// partition); results are returned in item order, so the outcome does not
/// depend on the number of threads.
fn parallel_map<T, R, F>(items: &[T], f: F) -> Result<Vec<R>, String>
where
    T: Sync,
    R: Send,
    F: Fn(&T) -> Result<R, String> + Sync,
{
    let workers = thread::available_parallelism()
        .map(|n| n.get())
        .unwrap_or(1)
        .clamp(1, MAX_THREADS)
        .min(items.len().max(1));
    let f = &f;
    let mut slots: Vec<Option<Result<R, String>>> = (0..items.len()).map(|_| None).collect();
    thread::scope(|scope| {
        let handles: Vec<_> = (0..workers)
            .map(|worker| {
                scope.spawn(move || {
                    let mut out = Vec::new();
                    let mut index = worker;
                    while index < items.len() {
                        out.push((index, f(&items[index])));
                        index += workers;
                    }
                    out
                })
            })
            .collect();
        for handle in handles {
            if let Ok(list) = handle.join() {
                for (index, result) in list {
                    slots[index] = Some(result);
                }
            }
        }
    });
    slots
        .into_iter()
        .enumerate()
        .map(|(index, slot)| {
            slot.unwrap_or_else(|| Err(format!("worker for item {index} panicked")))
        })
        .collect()
}

fn state_columns() -> Vec<String> {
    let mut columns: Vec<String> = (0..16).map(|i| format!("u_re_{i}")).collect();
    columns.extend((0..16).map(|i| format!("u_im_{i}")));
    columns
}

fn strings(names: &[&str]) -> Vec<String> {
    names.iter().map(|s| s.to_string()).collect()
}

fn cube(x: f64) -> f64 {
    x * x * x
}

fn max_of(values: impl Iterator<Item = f64>) -> f64 {
    values.fold(0.0f64, f64::max)
}

// ========================================================= (a) thermal ==

/// Radiation era a(t) = (t/t_i)^{1/2}.
fn thermal_scale_factor(t: f64) -> f64 {
    (t / T_INITIAL).sqrt()
}

/// Output targets t_j = t_i a_j^2, a_j = A_END^{j/N_OUT}, j = 1..N_OUT.
fn thermal_targets(a_end: f64, count: usize) -> Vec<f64> {
    let ln_a = log(a_end);
    (1..=count)
        .map(|j| {
            if j == count {
                T_INITIAL * a_end * a_end
            } else {
                T_INITIAL * exp(2.0 * ln_a * j as f64 / count as f64)
            }
        })
        .collect()
}

#[derive(Clone, Debug)]
struct ThermalGrid {
    x: Vec<f64>,
    gl_weight: Vec<f64>,
    k: Vec<f64>,
    weight: Vec<f64>,
    energy: Vec<f64>,
    occupation: Vec<f64>,
    /// W_n = (16/(2 pi^2)) w_n k_n^2 f_n.
    mode_weight: Vec<f64>,
    /// |c_n|^2 = (m k H_i/(4 E_i^3))^2 (sudden-start free-wave prediction).
    sudden_start: Vec<f64>,
}

fn thermal_grid() -> ThermalGrid {
    let (x, gl_weight) = gauss_legendre(N_K);
    let k: Vec<f64> = x.iter().map(|xi| 0.5 * K_MAX * (xi + 1.0)).collect();
    let weight: Vec<f64> = gl_weight.iter().map(|w| 0.5 * K_MAX * w).collect();
    let energy: Vec<f64> = k.iter().map(|ki| (MASS * MASS + ki * ki).sqrt()).collect();
    let occupation: Vec<f64> = energy
        .iter()
        .map(|e| 1.0 / (exp(e / TEMPERATURE) + 1.0))
        .collect();
    let mode_weight = (0..N_K)
        .map(|n| DEGENERACY / (2.0 * PI * PI) * weight[n] * k[n] * k[n] * occupation[n])
        .collect();
    let sudden_start = (0..N_K)
        .map(|n| {
            let c = MASS * k[n] * HUBBLE_INITIAL / (4.0 * energy[n] * energy[n] * energy[n]);
            c * c
        })
        .collect();
    ThermalGrid {
        x,
        gl_weight,
        k,
        weight,
        energy,
        occupation,
        mode_weight,
        sudden_start,
    }
}

#[derive(Clone, Debug)]
struct ThermalSpec {
    node: usize,
    k: f64,
    energy_sign: f64,
    b_sign: f64,
    adiabatic: bool,
}

struct ThermalRun {
    spec: ThermalSpec,
    residual: f64,
    integration: Integration,
    diags: Vec<Diagnostics>,
}

fn thermal_rhs(ops: ModeOperator, mass: f64, k: f64) -> RhsFn {
    Box::new(move |t, y, ydot| {
        ops.rhs(mass, k / thermal_scale_factor(t), y, ydot);
        Ok(())
    })
}

fn thermal_initial(alg: &Algebra, spec: &ThermalSpec) -> Result<(CVec16, f64), String> {
    let (h0, e0) = hamiltonian(alg, MASS, spec.k);
    let e = eigen_state(alg, &h0, e0, spec.energy_sign, spec.b_sign)?;
    let residual = h0
        .apply(&e)
        .max_abs_diff(&e.scale(spec.energy_sign * e0, 0.0));
    if spec.adiabatic {
        let hdot = hamiltonian_rate(alg, spec.k, HUBBLE_INITIAL);
        Ok((
            adiabatic_state(&h0, &hdot, e0, spec.energy_sign, &e),
            residual,
        ))
    } else {
        Ok((e, residual))
    }
}

fn run_thermal(
    alg: &Algebra,
    ops: ModeOperator,
    spec: &ThermalSpec,
    targets: &[f64],
    cfg: &SolverConfig,
) -> Result<ThermalRun, String> {
    let (u0, residual) = thermal_initial(alg, spec)?;
    let integration = integrate(
        u0.to_state(),
        T_INITIAL,
        targets,
        thermal_rhs(ops, MASS, spec.k),
        cfg,
    )
    .map_err(|error| format!("thermal node {} (k = {}): {error}", spec.node, spec.k))?;
    let diags = integration
        .times
        .iter()
        .zip(&integration.states)
        .map(|(t, state)| {
            let kk = spec.k / thermal_scale_factor(*t);
            diagnostics(
                alg,
                MASS,
                kk,
                0.5 / t,
                &CVec16::from_state(state),
                spec.energy_sign,
            )
        })
        .collect();
    Ok(ThermalRun {
        spec: spec.clone(),
        residual,
        integration,
        diags,
    })
}

fn thermal_mode_header() -> Vec<String> {
    let mut header = strings(&["node", "k", "t", "a", "H", "K"]);
    header.extend(state_columns());
    header.extend(strings(&[
        "E",
        "eps",
        "p1",
        "s",
        "norm_hilbert",
        "norm_krein",
        "beta2",
        "beta2_adiabatic",
    ]));
    header
}

fn thermal_mode_rows(runs: &[&ThermalRun]) -> Vec<Vec<f64>> {
    let mut rows = Vec::new();
    for run in runs {
        for ((t, state), d) in run
            .integration
            .times
            .iter()
            .zip(&run.integration.states)
            .zip(&run.diags)
        {
            let a = thermal_scale_factor(*t);
            let mut row = vec![
                run.spec.node as f64,
                run.spec.k,
                *t,
                a,
                0.5 / t,
                run.spec.k / a,
            ];
            row.extend_from_slice(state);
            row.extend([
                d.energy,
                d.eps,
                d.p1,
                d.s,
                d.norm,
                d.krein,
                d.beta2,
                d.beta2_adiabatic,
            ]);
            rows.push(row);
        }
    }
    rows
}

/// Adams versus BDF on two thermal modes over a in [1, A_METHOD_TEST].
#[derive(Clone, Debug)]
struct MethodTrial {
    node: usize,
    method: Method,
    steps: i64,
    rhs_evals: i64,
    lin_rhs_evals: i64,
    error: f64,
    norm_drift: f64,
}

fn method_selection(
    alg: &Algebra,
    ops: ModeOperator,
    grid: &ThermalGrid,
    tolerances: &Tolerances,
) -> Result<(Method, Vec<MethodTrial>), String> {
    let t_end = T_INITIAL * A_METHOD_TEST * A_METHOD_TEST;
    let targets = crate::driver::uniform_targets(T_INITIAL, t_end, METHOD_TEST_POINTS);
    let reference_cfg = solver_for(
        Method::Adams,
        &Tolerances {
            rtol: tolerances.rtol / 10.0,
            atol: tolerances.atol / 10.0,
            max_step: tolerances.max_step,
        },
    )
    .with_stop_time(t_end);
    let mut jobs = Vec::new();
    for &node in &METHOD_TEST_NODES {
        for method in [None, Some(Method::Adams), Some(Method::Bdf)] {
            jobs.push((node, method));
        }
    }
    let results = parallel_map(&jobs, |(node, method)| {
        let spec = ThermalSpec {
            node: *node,
            k: grid.k[*node],
            energy_sign: 1.0,
            b_sign: 1.0,
            adiabatic: false,
        };
        let cfg = match method {
            None => reference_cfg.clone(),
            Some(method) => solver_for(*method, tolerances).with_stop_time(t_end),
        };
        run_thermal(alg, ops, &spec, &targets, &cfg)
    })?;
    let mut trials = Vec::new();
    for (index, (node, method)) in jobs.iter().enumerate() {
        let Some(method) = method else { continue };
        let reference = &results[index - index % 3];
        let run = &results[index];
        let error = max_of(
            run.integration
                .states
                .iter()
                .zip(&reference.integration.states)
                .map(|(a, b)| CVec16::from_state(a).distance(&CVec16::from_state(b))),
        );
        let norm_drift = max_of(run.diags.iter().map(|d| (d.norm - 1.0).abs()));
        trials.push(MethodTrial {
            node: *node,
            method: *method,
            steps: run.integration.steps,
            rhs_evals: run.integration.rhs_evals,
            lin_rhs_evals: run.integration.lin_rhs_evals,
            error,
            norm_drift,
        });
    }
    let total = |method: Method| -> (f64, i64) {
        let selected: Vec<&MethodTrial> = trials.iter().filter(|t| t.method == method).collect();
        (
            max_of(selected.iter().map(|t| t.error)),
            selected.iter().map(|t| t.rhs_evals + t.lin_rhs_evals).sum(),
        )
    };
    let (error_adams, cost_adams) = total(Method::Adams);
    let (error_bdf, cost_bdf) = total(Method::Bdf);
    // The clearly (factor 2) more accurate method wins; otherwise the cheaper.
    let selected = if error_adams <= 0.5 * error_bdf {
        Method::Adams
    } else if error_bdf <= 0.5 * error_adams {
        Method::Bdf
    } else if cost_adams <= cost_bdf {
        Method::Adams
    } else {
        Method::Bdf
    };
    Ok((selected, trials))
}

fn solver_for(method: Method, tolerances: &Tolerances) -> SolverConfig {
    let mut cfg = match method {
        Method::Adams => SolverConfig::adams(tolerances.rtol, tolerances.atol, tolerances.max_step),
        Method::Bdf => SolverConfig::bdf(tolerances.rtol, tolerances.atol, tolerances.max_step),
    };
    cfg.max_num_steps = MAX_NUM_STEPS;
    cfg
}

fn method_name(method: Method) -> &'static str {
    match method {
        Method::Adams => "adams",
        Method::Bdf => "bdf",
    }
}

// ============================================================ (b) pair ==

/// (a, H) of the de Sitter -> radiation background.
fn pair_background(t: f64) -> (f64, f64) {
    if t < 0.0 {
        (exp(HUBBLE_INFLATION * t), HUBBLE_INFLATION)
    } else {
        let a2 = 1.0 + 2.0 * HUBBLE_INFLATION * t;
        (a2.sqrt(), HUBBLE_INFLATION / a2)
    }
}

/// a_end^2 with H(t_end) = HUBBLE_END_OVER_MASS m.
fn pair_a2_end(mass: f64) -> f64 {
    if mass > 0.0 {
        HUBBLE_INFLATION / (HUBBLE_END_OVER_MASS * mass)
    } else {
        MASSLESS_A2_END
    }
}

/// Radiation samples t_j = (a_j^2 - 1)/(2 H_inf), a_j^2 = (a_end^2)^{j/N}.
fn pair_targets(a2_end: f64) -> Vec<f64> {
    let ln_a2 = log(a2_end);
    (1..=N_PAIR_SAMPLES)
        .map(|j| {
            let a2 = if j == N_PAIR_SAMPLES {
                a2_end
            } else {
                exp(ln_a2 * j as f64 / N_PAIR_SAMPLES as f64)
            };
            (a2 - 1.0) / (2.0 * HUBBLE_INFLATION)
        })
        .collect()
}

#[derive(Clone, Debug)]
struct PairGrid {
    x: Vec<f64>,
    gl_weight: Vec<f64>,
    k: Vec<f64>,
    /// Weight in ln k: int g(k) dk = sum w_ln k g(k).
    ln_weight: Vec<f64>,
}

fn pair_grid() -> PairGrid {
    let (x, gl_weight) = gauss_legendre(N_PAIR_K);
    let (l0, l1) = (log(PAIR_K_MIN), log(PAIR_K_MAX));
    let k = x
        .iter()
        .map(|xi| exp(l0 + 0.5 * (l1 - l0) * (xi + 1.0)))
        .collect();
    let ln_weight = gl_weight.iter().map(|w| 0.5 * (l1 - l0) * w).collect();
    PairGrid {
        x,
        gl_weight,
        k,
        ln_weight,
    }
}

#[derive(Clone, Debug)]
struct PairSpec {
    mass: f64,
    node: usize,
    k: f64,
    energy_sign: f64,
}

struct PairRun {
    spec: PairSpec,
    t0: f64,
    a2_end: f64,
    /// |delta| of the initial first-order adiabatic state and the
    /// eigenvector residual of its zeroth-order part.
    delta_norm: f64,
    residual: f64,
    times: Vec<f64>,
    states: Vec<Vec<f64>>,
    diags: Vec<Diagnostics>,
    steps: i64,
    rhs_evals: i64,
}

fn run_pair(
    alg: &Algebra,
    ops: ModeOperator,
    spec: &PairSpec,
    cfg: &SolverConfig,
) -> Result<PairRun, String> {
    let (mass, k) = (spec.mass, spec.k);
    let t0 = log(k / K_OVER_A_START) / HUBBLE_INFLATION;
    let (a0, hubble0) = pair_background(t0);
    let kk0 = k / a0;
    let (h0, e0) = hamiltonian(alg, mass, kk0);
    let e = eigen_state(alg, &h0, e0, spec.energy_sign, 1.0)?;
    let residual = h0
        .apply(&e)
        .max_abs_diff(&e.scale(spec.energy_sign * e0, 0.0));
    let hdot0 = hamiltonian_rate(alg, kk0, hubble0);
    let delta_norm = adiabatic_correction(&h0, &hdot0, e0, spec.energy_sign, &e)
        .norm2()
        .sqrt();
    let u0 = adiabatic_state(&h0, &hdot0, e0, spec.energy_sign, &e);
    let label = |error: String| format!("pair m = {mass} k = {k}: {error}");
    let de_sitter: RhsFn = Box::new(move |t, y, ydot| {
        ops.rhs(mass, k * exp(-HUBBLE_INFLATION * t), y, ydot);
        Ok(())
    });
    let first = integrate(
        u0.to_state(),
        t0,
        &[0.0],
        de_sitter,
        &cfg.clone().with_stop_time(0.0),
    )
    .map_err(label)?;
    let a2_end = pair_a2_end(mass);
    let targets = pair_targets(a2_end);
    let t_end = targets[targets.len() - 1];
    let radiation: RhsFn = Box::new(move |t, y, ydot| {
        ops.rhs(mass, k / pair_background(t).0, y, ydot);
        Ok(())
    });
    let second = integrate(
        first.states[1].clone(),
        0.0,
        &targets,
        radiation,
        &cfg.clone().with_stop_time(t_end),
    )
    .map_err(label)?;
    let mut times = vec![t0, 0.0];
    times.extend_from_slice(&second.times[1..]);
    let mut states = vec![first.states[0].clone(), first.states[1].clone()];
    states.extend(second.states[1..].iter().cloned());
    let diags = times
        .iter()
        .zip(&states)
        .map(|(t, state)| {
            let (a, hubble) = pair_background(*t);
            diagnostics(
                alg,
                mass,
                k / a,
                hubble,
                &CVec16::from_state(state),
                spec.energy_sign,
            )
        })
        .collect();
    Ok(PairRun {
        spec: spec.clone(),
        t0,
        a2_end,
        delta_norm,
        residual,
        times,
        states,
        diags,
        steps: first.steps + second.steps,
        rhs_evals: first.rhs_evals + second.rhs_evals,
    })
}

fn pair_mode_header() -> Vec<String> {
    let mut header = strings(&["m", "node", "k", "t", "a", "H", "K"]);
    header.extend(state_columns());
    header.extend(strings(&[
        "E",
        "eps",
        "p1",
        "norm_hilbert",
        "norm_krein",
        "beta2",
        "beta2_adiabatic",
    ]));
    header
}

fn pair_mode_rows(runs: &[&PairRun]) -> Vec<Vec<f64>> {
    let mut rows = Vec::new();
    for run in runs {
        for ((t, state), d) in run.times.iter().zip(&run.states).zip(&run.diags) {
            let (a, hubble) = pair_background(*t);
            let mut row = vec![
                run.spec.mass,
                run.spec.node as f64,
                run.spec.k,
                *t,
                a,
                hubble,
                run.spec.k / a,
            ];
            row.extend_from_slice(state);
            row.extend([
                d.energy,
                d.eps,
                d.p1,
                d.norm,
                d.krein,
                d.beta2,
                d.beta2_adiabatic,
            ]);
            rows.push(row);
        }
    }
    rows
}

/// (m k/(4 E^4))^2 with E = sqrt(m^2 + k^2) (a = 1 at the kink).
fn kink_tail(mass: f64, k: f64) -> f64 {
    let e2 = mass * mass + k * k;
    let b = mass * k / (4.0 * e2 * e2);
    b * b
}

struct PairMassResult {
    mass: f64,
    a2_end: f64,
    t_end: f64,
    n_a3: f64,
    n_a3_adiabatic: f64,
    n_a3_kink: f64,
    rho_a3_end: f64,
    w_at_1: f64,
    w_end: f64,
    w_monotone: bool,
    max_beta2: f64,
    max_beta2_adiabatic: f64,
    k_peak: f64,
    tail_max_dev: f64,
    tail_nodes: usize,
    initial_beta2_max: f64,
    delta_prediction_dev: f64,
}

// =============================================================== run ===

/// Configuration lines for `print-config`.
pub fn config_lines() -> Vec<String> {
    vec![
        format!(
            "exp4 (a): m = {}, T_i = {}, H_i = {}, t_i = {}, a in [1, {}], k in [0, {}] ({} GL nodes)",
            fmt17(MASS),
            fmt17(TEMPERATURE),
            fmt17(HUBBLE_INITIAL),
            fmt17(T_INITIAL),
            fmt17(A_END),
            fmt17(K_MAX),
            N_K
        ),
        format!(
            "exp4 (b): H_inf = {}, K0 = {}, m = {:?}, k in [{}, {}] ({} GL nodes in ln k)",
            fmt17(HUBBLE_INFLATION),
            fmt17(K_OVER_A_START),
            PAIR_MASSES,
            fmt17(PAIR_K_MIN),
            fmt17(PAIR_K_MAX),
            N_PAIR_K
        ),
        format!(
            "exp4: default rtol = {}, atol = {}, max_step = {}, max_num_steps = {}, \
             method Adams or BDF chosen at run time by the method-selection test",
            fmt17(DEFAULT_TOLERANCES.rtol),
            fmt17(DEFAULT_TOLERANCES.atol),
            fmt17(DEFAULT_TOLERANCES.max_step),
            MAX_NUM_STEPS
        ),
    ]
}

/// Run EXP-4.
pub fn run(ctx: &RunContext) -> Result<ExperimentSummary, String> {
    let directory = ctx.experiment_dir(EXPERIMENT)?;
    let tolerances = ctx.tolerances(DEFAULT_TOLERANCES);
    let alg = Algebra::new();
    let ops = ModeOperator::new(&alg)?;
    let mut summary = ExperimentSummary::new(EXPERIMENT);

    // ---------------------------------------------- method selection --
    // The method test runs at the DEFAULT tolerances (a property of the
    // problem, identical for canonical, --rtol/--atol and --refined runs).
    let grid = thermal_grid();
    let (method, trials) = method_selection(&alg, ops, &grid, &DEFAULT_TOLERANCES)?;
    for trial in &trials {
        summary.add_stats(trial.steps, trial.rhs_evals + trial.lin_rhs_evals);
    }
    let base_cfg = solver_for(method, &tolerances);
    let solver_description = base_cfg.describe();

    // ------------------------------------------------ (a) thermal gas --
    let targets = thermal_targets(A_END, N_OUT);
    let t_end = targets[targets.len() - 1];
    let thermal_cfg = base_cfg.clone().with_stop_time(t_end);
    let mut specs: Vec<ThermalSpec> = (0..N_K)
        .map(|node| ThermalSpec {
            node,
            k: grid.k[node],
            energy_sign: 1.0,
            b_sign: 1.0,
            adiabatic: false,
        })
        .collect();
    for &node in &SPIN_NODES {
        specs.push(ThermalSpec {
            node,
            k: grid.k[node],
            energy_sign: 1.0,
            b_sign: -1.0,
            adiabatic: false,
        });
    }
    specs.push(ThermalSpec {
        node: ANTIPARTICLE_NODE,
        k: grid.k[ANTIPARTICLE_NODE],
        energy_sign: -1.0,
        b_sign: 1.0,
        adiabatic: false,
    });
    for &node in &ADIABATIC_VACUUM_NODES {
        specs.push(ThermalSpec {
            node,
            k: grid.k[node],
            energy_sign: 1.0,
            b_sign: 1.0,
            adiabatic: true,
        });
    }
    let thermal = parallel_map(&specs, |spec| {
        run_thermal(&alg, ops, spec, &targets, &thermal_cfg)
    })?;
    for run in &thermal {
        summary.add_stats(run.integration.steps, run.integration.rhs_evals);
    }
    let main_runs: Vec<&ThermalRun> = thermal[..N_K].iter().collect();
    let spin_runs: Vec<&ThermalRun> = thermal[N_K..N_K + SPIN_NODES.len()].iter().collect();
    let anti_run = &thermal[N_K + SPIN_NODES.len()];
    let adiabatic_runs: Vec<&ThermalRun> = thermal[N_K + SPIN_NODES.len() + 1..].iter().collect();

    // grid file
    let grid_rows: Vec<Vec<f64>> = (0..N_K)
        .map(|n| {
            vec![
                n as f64,
                grid.x[n],
                grid.gl_weight[n],
                grid.k[n],
                grid.weight[n],
                grid.energy[n],
                grid.occupation[n],
                grid.mode_weight[n],
                grid.sudden_start[n],
            ]
        })
        .collect();
    write_csv(
        &directory.join("thermal_grid.csv"),
        &strings(&[
            "node",
            "x",
            "gl_weight",
            "k",
            "weight",
            "E_i",
            "f",
            "mode_weight",
            "beta2_sudden_start",
        ]),
        &grid_rows,
    )?;
    summary.add_file("thermal_grid.csv");
    for (name, runs) in [
        ("thermal_modes.csv", main_runs.clone()),
        ("thermal_spin.csv", spin_runs.clone()),
        ("thermal_antiparticle.csv", vec![anti_run]),
        ("thermal_adiabatic_vacuum.csv", adiabatic_runs.clone()),
    ] {
        write_csv(
            &directory.join(name),
            &thermal_mode_header(),
            &thermal_mode_rows(&runs),
        )?;
        summary.add_file(name);
    }

    // equation of state
    let times = &main_runs[0].integration.times;
    let fd_norm: f64 = (0..N_K)
        .map(|n| grid.weight[n] * grid.k[n] * grid.k[n] * grid.occupation[n])
        .sum();
    let mut eos_rows = Vec::new();
    let mut w_values = Vec::new();
    let (mut max_dev_rho, mut max_dev_p) = (0.0f64, 0.0f64);
    let (mut max_beta_weighted, mut max_identity) = (0.0f64, 0.0f64);
    let (mut pressure_envelope_ok, mut pressure_envelope_ratio) = (true, 0.0f64);
    for (j, t) in times.iter().enumerate() {
        let a = thermal_scale_factor(*t);
        let a3 = a * a * a;
        let (mut rho, mut p1, mut pe, mut number) = (0.0, 0.0, 0.0, 0.0);
        let (mut rho_kin, mut p_kin, mut beta_w, mut envelope) = (0.0, 0.0, 0.0, 0.0);
        let (mut beta_max, mut beta_ad_max, mut norm_dev) = (0.0f64, 0.0f64, 0.0f64);
        for (n, run) in main_runs.iter().enumerate() {
            let d = &run.diags[j];
            let wn = grid.mode_weight[n];
            rho += wn * d.eps;
            p1 += wn * d.p1;
            pe += wn * MASS * d.s;
            number += wn * d.norm;
            let kk = grid.k[n] / a;
            let e = (MASS * MASS + kk * kk).sqrt();
            rho_kin += wn * e;
            p_kin += wn * kk * kk / (3.0 * e);
            // free-wave interference: p_1 = (1 - 2|b|^2) K^2/E + 2 Re(alpha^* b) m K/E
            // with |b| <= |c| (1 + tol) + beta_ad(t) (checked per mode below)
            let beta_ad = MASS * kk * (0.5 / t) / (4.0 * e * e * e);
            let b = grid.sudden_start[n].sqrt() * (1.0 + SUDDEN_START_LIMIT) + beta_ad;
            envelope += wn * (2.0 * b * MASS * kk / e + 2.0 * b * b * kk * kk / e);
            beta_w += grid.weight[n] * grid.k[n] * grid.k[n] * grid.occupation[n] * d.beta2;
            beta_max = beta_max.max(d.beta2);
            beta_ad_max = beta_ad_max.max(d.beta2_adiabatic);
            norm_dev = norm_dev.max((d.norm - 1.0).abs());
            max_identity =
                max_identity.max((d.eps - (MASS * d.s + d.p1)).abs() / d.energy.max(1.0));
        }
        let (rho, p, ke_h, pe_h) = (rho / a3, p1 / (3.0 * a3), p1 / a3, pe / a3);
        let (rho_kin, p_kin) = (rho_kin / a3, p_kin / a3);
        let w = p / rho;
        let dev_rho = (rho - rho_kin) / rho_kin;
        let dev_p = (p - p_kin) / p_kin;
        max_dev_rho = max_dev_rho.max(dev_rho.abs());
        max_dev_p = max_dev_p.max(dev_p.abs());
        let allowed = envelope / (3.0 * a3) + KINETIC_LIMIT * p_kin;
        pressure_envelope_ratio = pressure_envelope_ratio.max((p - p_kin).abs() / allowed);
        if (p - p_kin).abs() > allowed {
            pressure_envelope_ok = false;
        }
        max_identity = max_identity.max((ke_h + pe_h - rho).abs() / rho);
        let beta_weighted = beta_w / fd_norm;
        max_beta_weighted = max_beta_weighted.max(beta_weighted);
        w_values.push(w);
        eos_rows.push(vec![
            a,
            *t,
            0.5 / t,
            rho,
            p,
            w,
            ke_h,
            pe_h,
            0.5 * rho,
            rho - 0.5 * rho,
            number,
            rho_kin,
            p_kin,
            p_kin / rho_kin,
            dev_rho,
            dev_p,
            beta_weighted,
            beta_max,
            beta_ad_max,
            norm_dev,
        ]);
    }
    write_csv(
        &directory.join("thermal_eos.csv"),
        &strings(&[
            "a",
            "t",
            "H",
            "rho",
            "p",
            "w",
            "KE_H",
            "PE_H",
            "KE_L",
            "PE_L",
            "n_a3",
            "rho_kinetic",
            "p_kinetic",
            "w_kinetic",
            "rel_dev_rho",
            "rel_dev_p",
            "beta2_weighted",
            "beta2_max",
            "beta2_adiabatic_max",
            "norm_dev_max",
        ]),
        &eos_rows,
    )?;
    summary.add_file("thermal_eos.csv");

    // thermal measurements
    let all_thermal: Vec<&ThermalRun> = thermal.iter().collect();
    let eigen_residual = max_of(all_thermal.iter().map(|r| r.residual));
    let unitarity = max_of(
        all_thermal
            .iter()
            .flat_map(|r| r.diags.iter().map(|d| (d.norm - 1.0).abs())),
    );
    let krein_drift = max_of(all_thermal.iter().flat_map(|r| {
        let k0 = r.diags[0].krein;
        r.diags.iter().map(move |d| (d.krein - k0).abs())
    }));
    let krein_initial_ok = all_thermal
        .iter()
        .all(|r| (r.diags[0].krein - r.spec.b_sign).abs() <= 1.0e-12);
    let beta_max_instantaneous = max_of(
        main_runs
            .iter()
            .flat_map(|r| r.diags.iter().map(|d| d.beta2)),
    );
    let (beta_max_node, _) = main_runs
        .iter()
        .enumerate()
        .map(|(n, r)| (n, max_of(r.diags.iter().map(|d| d.beta2))))
        .fold(
            (0usize, -1.0f64),
            |best, item| {
                if item.1 > best.1 {
                    item
                } else {
                    best
                }
            },
        );
    // sudden-start theory: late adiabatic-basis |beta|^2 -> |c|^2, and
    // instantaneous |beta(t)| <= |c| (1 + tol) + beta_ad(t)
    let (mut sudden_dev, mut sudden_compared, mut sudden_bound_ok) = (0.0f64, 0usize, true);
    let mut sudden_bound_ratio = 0.0f64;
    for (n, run) in main_runs.iter().enumerate() {
        let c2 = grid.sudden_start[n];
        let late = run.diags[run.diags.len() - 1].beta2_adiabatic;
        if c2 >= SUDDEN_START_FLOOR {
            sudden_dev = sudden_dev.max((late / c2 - 1.0).abs());
            sudden_compared += 1;
        } else if late > c2 * (1.0 + SUDDEN_START_LIMIT) * (1.0 + SUDDEN_START_LIMIT) + BETA_FLOOR {
            sudden_bound_ok = false;
        }
        for (t, d) in run.integration.times.iter().zip(&run.diags) {
            let kk = run.spec.k / thermal_scale_factor(*t);
            let hubble = 0.5 / t;
            let e = (MASS * MASS + kk * kk).sqrt();
            let beta_ad = MASS * kk * hubble / (4.0 * e * e * e);
            let bound = c2.sqrt() * (1.0 + SUDDEN_START_LIMIT) + beta_ad;
            let bound2 = bound * bound + BETA_FLOOR;
            sudden_bound_ratio = sudden_bound_ratio.max(d.beta2 / bound2);
            if d.beta2 > bound2 {
                sudden_bound_ok = false;
            }
        }
    }
    let adiabatic_vacuum_late = max_of(
        adiabatic_runs
            .iter()
            .map(|r| r.diags[r.diags.len() - 1].beta2),
    );
    let adiabatic_vacuum_max = max_of(
        adiabatic_runs
            .iter()
            .flat_map(|r| r.diags.iter().map(|d| d.beta2_adiabatic)),
    );
    // pressure of a single mode relative to K^2/E: instantaneous start versus
    // first-order adiabatic vacuum at the same node
    let pressure_dev = |run: &ThermalRun| -> f64 {
        max_of(run.integration.times.iter().zip(&run.diags).map(|(t, d)| {
            let kk = run.spec.k / thermal_scale_factor(*t);
            let kinetic = kk * kk / d.energy;
            (d.p1 - kinetic).abs() / kinetic
        }))
    };
    let pressure_dev_adiabatic = max_of(adiabatic_runs.iter().map(|r| pressure_dev(r)));
    let pressure_dev_instantaneous = max_of(
        adiabatic_runs
            .iter()
            .map(|r| pressure_dev(main_runs[r.spec.node])),
    );
    let mode_stats: Vec<Json> = main_runs
        .iter()
        .map(|r| {
            Json::object(vec![
                ("node", Json::Int(r.spec.node as i64)),
                ("k", Json::Float(r.spec.k)),
                ("steps", Json::Int(r.integration.steps)),
                ("rhsEvals", Json::Int(r.integration.rhs_evals)),
                ("lastOrder", Json::Int(r.integration.last_order as i64)),
                (
                    "maxNormDrift",
                    Json::Float(max_of(r.diags.iter().map(|d| (d.norm - 1.0).abs()))),
                ),
            ])
        })
        .collect();
    let spin_dev = max_of(spin_runs.iter().flat_map(|spin| {
        let main = main_runs[spin.spec.node];
        spin.diags.iter().zip(&main.diags).map(|(a, b)| {
            ((a.eps - b.eps).abs() / b.energy)
                .max((a.p1 - b.p1).abs() / b.energy)
                .max((a.s - b.s).abs())
                .max((a.beta2 - b.beta2).abs())
        })
    }));
    let spin_krein_ok = spin_runs
        .iter()
        .all(|r| (r.diags[0].krein + 1.0).abs() <= 1.0e-12);
    let anti_main = main_runs[ANTIPARTICLE_NODE];
    let anti_dev = max_of(anti_run.diags.iter().zip(&anti_main.diags).map(|(v, u)| {
        ((v.eps + u.eps).abs() / u.energy)
            .max((v.p1 + u.p1).abs() / u.energy)
            .max((v.s + u.s).abs())
            .max((v.beta2 - u.beta2).abs())
    }));
    let anti_initial_energy = anti_run.diags[0].eps / anti_run.diags[0].energy;
    let w_first = w_values[0];
    let w_last = w_values[w_values.len() - 1];
    let w_monotone = w_values.windows(2).all(|pair| pair[1] < pair[0]);
    let w_kin_first = eos_rows[0][13];
    let w_kin_last = eos_rows[eos_rows.len() - 1][13];

    summary.check(
        "thermal_grid_gauss_legendre",
        {
            let sum: f64 = grid.weight.iter().sum();
            let second: f64 = (0..N_K)
                .map(|n| grid.weight[n] * grid.k[n] * grid.k[n])
                .sum();
            (sum / K_MAX - 1.0).abs() <= 1e-14
                && (second / (K_MAX * K_MAX * K_MAX / 3.0) - 1.0).abs() <= 1e-14
                && grid.x.iter().all(|x| legendre(N_K, *x).0.abs() <= 1e-13)
        },
        "weights sum to k_max, exact for k^2, |P_48(x_n)| <= 1e-13",
    );
    summary.check(
        "thermal_initial_eigenvectors",
        eigen_residual <= EIGEN_LIMIT && krein_initial_ok && anti_initial_energy < -0.999_999,
        &format!(
            "max |h u0 -+ E u0| = {}, u0^dag B u0 = b_sign, antiparticle eps/E = {}",
            fmt17(eigen_residual),
            fmt17(anti_initial_energy)
        ),
    );
    summary.check(
        "thermal_unitarity",
        unitarity <= UNITARITY_LIMIT,
        &format!(
            "max |u^dag u - 1| = {} (limit {})",
            fmt17(unitarity),
            fmt17(UNITARITY_LIMIT)
        ),
    );
    summary.check(
        "thermal_krein_conserved",
        krein_drift <= KREIN_LIMIT,
        &format!("max |d(u^dag B u)| = {}", fmt17(krein_drift)),
    );
    summary.check(
        "thermal_energy_split_identities",
        max_identity <= IDENTITY_LIMIT,
        &format!(
            "eps = m s + p_1 per mode and KE_H + PE_H = rho: max rel residual {}",
            fmt17(max_identity)
        ),
    );
    summary.check(
        "thermal_rho_matches_kinetic_theory",
        max_dev_rho <= KINETIC_LIMIT,
        &format!(
            "max |rho_modes/rho_kinetic - 1| = {} (same GL nodes; limit {})",
            fmt17(max_dev_rho),
            fmt17(KINETIC_LIMIT)
        ),
    );
    summary.check(
        "thermal_pressure_matches_kinetic_theory_plus_free_wave",
        pressure_envelope_ok,
        &format!(
            "max |p_modes/p_kinetic - 1| = {} (literal 1e-6 not met: first-order interference \
             2 Re(alpha^* beta) m K/E of the sudden-start free wave); |p - p_kin| / (free-wave \
             envelope + 1e-6 p_kin) max = {}",
            fmt17(max_dev_p),
            fmt17(pressure_envelope_ratio)
        ),
    );
    summary.check(
        "thermal_w_early_radiation",
        (w_first - 1.0 / 3.0).abs() <= W_EARLY_LIMIT && w_first < 1.0 / 3.0,
        &format!(
            "w(a=1) = {} (kinetic {}), 1/3 - w = {}",
            fmt17(w_first),
            fmt17(w_kin_first),
            fmt17(1.0 / 3.0 - w_first)
        ),
    );
    summary.check(
        "thermal_w_decreases_to_dust",
        w_monotone && w_last <= W_LATE_MAX && w_last > 0.0,
        &format!(
            "w strictly decreasing on the grid, w(a={}) = {} (kinetic {})",
            fmt17(A_END),
            fmt17(w_last),
            fmt17(w_kin_last)
        ),
    );
    summary.check(
        "thermal_beta2_gas_weighted_below_1e-6",
        max_beta_weighted <= BETA_LIMIT,
        &format!(
            "max_t sum w k^2 f |beta|^2 / sum w k^2 f = {} (limit {})",
            fmt17(max_beta_weighted),
            fmt17(BETA_LIMIT)
        ),
    );
    summary.check(
        "thermal_beta2_per_mode_is_sudden_start_wave",
        sudden_dev <= SUDDEN_START_LIMIT && sudden_bound_ok && sudden_compared > 0,
        &format!(
            "late adiabatic |beta|^2 vs (m k H_i/(4E_i^3))^2: max rel dev {} over {} modes; \
             |beta(t)|^2 / bound max {}; per-mode max |beta|^2 = {} at k = {}",
            fmt17(sudden_dev),
            sudden_compared,
            fmt17(sudden_bound_ratio),
            fmt17(beta_max_instantaneous),
            fmt17(grid.k[beta_max_node])
        ),
    );
    summary.check(
        "thermal_beta2_adiabatic_vacuum_below_1e-6",
        adiabatic_vacuum_late <= BETA_LIMIT && adiabatic_vacuum_max <= BETA_LIMIT,
        &format!(
            "adiabatic-vacuum start: late instantaneous |beta|^2 = {}, max adiabatic-basis \
             |beta|^2 = {}",
            fmt17(adiabatic_vacuum_late),
            fmt17(adiabatic_vacuum_max)
        ),
    );
    summary.check(
        "thermal_spin_independence",
        spin_dev <= SPIN_LIMIT && spin_krein_ok,
        &format!(
            "B = -1 spin state vs B = +1 at {} nodes: max dev {}",
            SPIN_NODES.len(),
            fmt17(spin_dev)
        ),
    );
    summary.check(
        "thermal_antiparticle_symmetry",
        anti_dev <= ANTIPARTICLE_LIMIT,
        &format!(
            "negative-energy mode: max |eps(v)+eps(u)|/E, |p1(v)+p1(u)|/E, |s(v)+s(u)|, \
             |beta dev| = {}",
            fmt17(anti_dev)
        ),
    );
    let adams_error = max_of(
        trials
            .iter()
            .filter(|t| t.method == Method::Adams)
            .map(|t| t.error),
    );
    let bdf_error = max_of(
        trials
            .iter()
            .filter(|t| t.method == Method::Bdf)
            .map(|t| t.error),
    );
    let (selected_error, other_error) = match method {
        Method::Adams => (adams_error, bdf_error),
        Method::Bdf => (bdf_error, adams_error),
    };
    summary.check(
        "method_selected_by_test",
        trials.len() == 2 * METHOD_TEST_NODES.len()
            && selected_error <= 2.0 * other_error
            && selected_error <= UNITARITY_LIMIT,
        &format!(
            "selected {} (max error vs reference: adams {}, bdf {}; selected <= 2 x other and \
             <= {})",
            method_name(method),
            fmt17(adams_error),
            fmt17(bdf_error),
            fmt17(UNITARITY_LIMIT)
        ),
    );

    // ------------------------------------------------- (b) pair creation --
    let pgrid = pair_grid();
    let mut pair_specs = Vec::new();
    for &mass in &PAIR_MASSES {
        for node in 0..N_PAIR_K {
            pair_specs.push(PairSpec {
                mass,
                node,
                k: pgrid.k[node],
                energy_sign: 1.0,
            });
        }
    }
    for &node in &PAIR_ANTIPARTICLE_NODES {
        pair_specs.push(PairSpec {
            mass: PAIR_ANTIPARTICLE_MASS,
            node,
            k: pgrid.k[node],
            energy_sign: -1.0,
        });
    }
    let pair = parallel_map(&pair_specs, |spec| run_pair(&alg, ops, spec, &base_cfg))?;
    for run in &pair {
        summary.add_stats(run.steps, run.rhs_evals);
    }
    let n_main = PAIR_MASSES.len() * N_PAIR_K;
    let pair_main: Vec<&PairRun> = pair[..n_main].iter().collect();
    let pair_anti: Vec<&PairRun> = pair[n_main..].iter().collect();

    let pgrid_rows: Vec<Vec<f64>> = (0..N_PAIR_K)
        .map(|n| {
            vec![
                n as f64,
                pgrid.x[n],
                pgrid.gl_weight[n],
                pgrid.k[n],
                pgrid.ln_weight[n],
                log(pgrid.k[n] / K_OVER_A_START) / HUBBLE_INFLATION,
            ]
        })
        .collect();
    write_csv(
        &directory.join("pair_grid.csv"),
        &strings(&["node", "x", "gl_weight", "k", "ln_k_weight", "t0"]),
        &pgrid_rows,
    )?;
    summary.add_file("pair_grid.csv");
    write_csv(
        &directory.join("pair_modes.csv"),
        &pair_mode_header(),
        &pair_mode_rows(&pair_main),
    )?;
    summary.add_file("pair_modes.csv");
    write_csv(
        &directory.join("pair_antiparticle.csv"),
        &pair_mode_header(),
        &pair_mode_rows(&pair_anti),
    )?;
    summary.add_file("pair_antiparticle.csv");

    let prefactor = DEGENERACY / (2.0 * PI * PI);
    let mut spectrum_rows = Vec::new();
    let mut eos_pair_rows = Vec::new();
    let mut history_rows = Vec::new();
    let mut mass_results = Vec::new();
    for (index, &mass) in PAIR_MASSES.iter().enumerate() {
        let runs = &pair_main[index * N_PAIR_K..(index + 1) * N_PAIR_K];
        let a2_end = runs[0].a2_end;
        let a_end = a2_end.sqrt();
        let last = runs[0].diags.len() - 1;
        let final_beta: Vec<f64> = runs.iter().map(|r| r.diags[last].beta2).collect();
        let final_beta_ad: Vec<f64> = runs.iter().map(|r| r.diags[last].beta2_adiabatic).collect();
        let integral = |values: &[f64]| -> f64 {
            prefactor
                * (0..N_PAIR_K)
                    .map(|n| pgrid.ln_weight[n] * cube(pgrid.k[n]) * values[n])
                    .sum::<f64>()
        };
        let mut tail_dev = 0.0f64;
        let mut tail_nodes = 0usize;
        for (n, run) in runs.iter().enumerate() {
            let k = pgrid.k[n];
            let tail = kink_tail(mass, k);
            if mass > 0.0 && k >= PAIR_TAIL_K {
                tail_dev = tail_dev.max((final_beta_ad[n] / tail - 1.0).abs());
                tail_nodes += 1;
            }
            spectrum_rows.push(vec![
                mass,
                n as f64,
                k,
                run.t0,
                a_end,
                run.diags[0].beta2,
                run.diags[1].beta2,
                run.diags[1].beta2_adiabatic,
                final_beta[n],
                final_beta_ad[n],
                tail,
            ]);
        }
        // produced-gas EoS from the frozen final spectrum
        let ln_a_end = log(a_end);
        let mut w_list = Vec::new();
        let mut rho_end = 0.0;
        let n_a3 = integral(&final_beta);
        // (16/(2 pi^2)) w_ln k^3 |beta_k|^2 (frozen final occupation)
        let occupation_weight: Vec<f64> = (0..N_PAIR_K)
            .map(|n| prefactor * pgrid.ln_weight[n] * cube(pgrid.k[n]) * final_beta[n])
            .collect();
        for i in 0..=N_PAIR_EOS {
            let a = if i == N_PAIR_EOS {
                a_end
            } else {
                exp(ln_a_end * i as f64 / N_PAIR_EOS as f64)
            };
            let (mut rho, mut p) = (0.0, 0.0);
            for (k, weight) in pgrid.k.iter().zip(&occupation_weight) {
                let kk = k / a;
                let e = (mass * mass + kk * kk).sqrt();
                rho += weight * e;
                p += weight * kk * kk / (3.0 * e);
            }
            let w = if rho > 0.0 { p / rho } else { 0.0 };
            w_list.push(w);
            rho_end = rho;
            eos_pair_rows.push(vec![mass, a, n_a3, rho, p, w]);
        }
        // production history on the common times (sample 0 = t0(k) differs
        // per k and is summarised as initialBeta2Max instead)
        for sample in 1..runs[0].times.len() {
            let values: Vec<f64> = runs.iter().map(|r| r.diags[sample].beta2).collect();
            let values_ad: Vec<f64> = runs
                .iter()
                .map(|r| r.diags[sample].beta2_adiabatic)
                .collect();
            let t = runs[0].times[sample];
            history_rows.push(vec![
                mass,
                sample as f64,
                t,
                pair_background(t).0,
                integral(&values),
                integral(&values_ad),
            ]);
        }
        let (peak_node, _) = (0..N_PAIR_K)
            .map(|n| (n, cube(pgrid.k[n]) * final_beta[n]))
            .fold(
                (0usize, -1.0f64),
                |best, item| {
                    if item.1 > best.1 {
                        item
                    } else {
                        best
                    }
                },
            );
        let kink_values: Vec<f64> = runs.iter().map(|r| r.diags[1].beta2).collect();
        // |delta| = |Q hdot e|/(4E^2) = m K0 H_inf/(4 E0^3) (|Q gamma^4 gamma^1 e| = m/E)
        let delta_expected = {
            let kk = K_OVER_A_START;
            let e = (mass * mass + kk * kk).sqrt();
            mass * kk * HUBBLE_INFLATION / (4.0 * e * e * e)
        };
        let delta_dev = max_of(runs.iter().map(|r| (r.delta_norm - delta_expected).abs()));
        mass_results.push(PairMassResult {
            mass,
            a2_end,
            t_end: runs[0].times[last],
            n_a3,
            n_a3_adiabatic: integral(&final_beta_ad),
            n_a3_kink: integral(&kink_values),
            rho_a3_end: rho_end,
            w_at_1: w_list[0],
            w_end: w_list[w_list.len() - 1],
            w_monotone: w_list.windows(2).all(|pair| pair[1] <= pair[0]),
            max_beta2: max_of(runs.iter().flat_map(|r| r.diags.iter().map(|d| d.beta2))),
            max_beta2_adiabatic: max_of(
                runs.iter()
                    .flat_map(|r| r.diags.iter().map(|d| d.beta2_adiabatic)),
            ),
            k_peak: pgrid.k[peak_node],
            tail_max_dev: tail_dev,
            tail_nodes,
            initial_beta2_max: max_of(runs.iter().map(|r| r.diags[0].beta2)),
            delta_prediction_dev: delta_dev,
        });
    }
    write_csv(
        &directory.join("pair_spectrum.csv"),
        &strings(&[
            "m",
            "node",
            "k",
            "t0",
            "a_end",
            "beta2_initial",
            "beta2_kink",
            "beta2_adiabatic_kink",
            "beta2_end",
            "beta2_adiabatic_end",
            "beta2_kink_tail_theory",
        ]),
        &spectrum_rows,
    )?;
    summary.add_file("pair_spectrum.csv");
    write_csv(
        &directory.join("pair_eos.csv"),
        &strings(&["m", "a", "n_a3", "rho_a3", "p_a3", "w"]),
        &eos_pair_rows,
    )?;
    summary.add_file("pair_eos.csv");
    write_csv(
        &directory.join("pair_history.csv"),
        &strings(&["m", "sample", "t", "a", "n_a3", "n_a3_adiabatic"]),
        &history_rows,
    )?;
    summary.add_file("pair_history.csv");

    // pair measurements
    let pair_all: Vec<&PairRun> = pair.iter().collect();
    let pair_residual = max_of(pair_all.iter().map(|r| r.residual));
    let pair_unitarity = max_of(
        pair_all
            .iter()
            .flat_map(|r| r.diags.iter().map(|d| (d.norm - 1.0).abs())),
    );
    let pair_krein = max_of(pair_all.iter().flat_map(|r| {
        let k0 = r.diags[0].krein;
        r.diags.iter().map(move |d| (d.krein - k0).abs())
    }));
    let massless = &mass_results[0];
    let initial_beta = max_of(mass_results.iter().map(|m| m.initial_beta2_max));
    let initial_bound = {
        let mmax = PAIR_MASSES.iter().fold(0.0f64, |a, b| a.max(*b));
        let c = mmax * HUBBLE_INFLATION / (4.0 * K_OVER_A_START * K_OVER_A_START);
        c * c
    };
    let delta_dev = max_of(mass_results.iter().map(|m| m.delta_prediction_dev));
    let tail_dev = max_of(mass_results.iter().map(|m| m.tail_max_dev));
    let pauli_ok = pair_main
        .iter()
        .all(|r| r.diags.iter().all(|d| d.beta2 <= 1.0 && d.beta2 >= 0.0));
    let produced_ok = mass_results[1..].iter().all(|m| m.n_a3 > 0.0);
    let pair_eos_ok = mass_results[1..]
        .iter()
        .all(|m| m.w_monotone && m.w_end <= PAIR_W_LATE_MAX && m.w_at_1 > m.w_end);
    let pair_anti_dev = max_of(pair_anti.iter().map(|v| {
        pair_main
            .iter()
            .find(|u| u.spec.mass == v.spec.mass && u.spec.node == v.spec.node)
            .map(|u| {
                max_of(v.diags.iter().zip(&u.diags).map(|(dv, du)| {
                    (dv.beta2 - du.beta2)
                        .abs()
                        .max((dv.eps + du.eps).abs() / du.energy)
                }))
            })
            .unwrap_or(f64::INFINITY)
    }));
    summary.check(
        "pair_initial_adiabatic_vacuum",
        pair_residual <= EIGEN_LIMIT
            && initial_beta <= initial_bound * 1.001 + 1e-20
            && delta_dev <= 1e-12,
        &format!(
            "K(t0) = {}: eigen residual {}, |delta| vs m K0 H/(4E0^3) dev {}, max |beta(t0)|^2 = {} \
             (bound {})",
            fmt17(K_OVER_A_START),
            fmt17(pair_residual),
            fmt17(delta_dev),
            fmt17(initial_beta),
            fmt17(initial_bound)
        ),
    );
    summary.check(
        "pair_unitarity",
        pair_unitarity <= UNITARITY_LIMIT,
        &format!("max |u^dag u - 1| = {}", fmt17(pair_unitarity)),
    );
    summary.check(
        "pair_krein_conserved",
        pair_krein <= KREIN_LIMIT,
        &format!("max |d(u^dag B u)| = {}", fmt17(pair_krein)),
    );
    summary.check(
        "pair_massless_no_production",
        massless.max_beta2 <= MASSLESS_BETA_LIMIT
            && massless.max_beta2_adiabatic <= MASSLESS_BETA_LIMIT,
        &format!(
            "m = 0: max |beta|^2 = {} (instantaneous), {} (adiabatic) over all k and samples \
             (limit {})",
            fmt17(massless.max_beta2),
            fmt17(massless.max_beta2_adiabatic),
            fmt17(MASSLESS_BETA_LIMIT)
        ),
    );
    summary.check(
        "pair_massive_production_pauli",
        produced_ok && pauli_ok,
        &format!(
            "n a^3 > 0 for m > 0 and 0 <= |beta|^2 <= 1; n a^3 = {:?}",
            mass_results
                .iter()
                .map(|m| fmt17(m.n_a3))
                .collect::<Vec<_>>()
        ),
    );
    summary.check(
        "pair_tail_matches_kink_theory",
        tail_dev <= TAIL_LIMIT,
        &format!(
            "k >= {}: adiabatic |beta|^2 vs (m k/(4E^4))^2, max rel dev {} (limit {})",
            fmt17(PAIR_TAIL_K),
            fmt17(tail_dev),
            fmt17(TAIL_LIMIT)
        ),
    );
    summary.check(
        "pair_antiparticle_symmetry",
        pair_anti_dev <= ANTIPARTICLE_LIMIT,
        &format!(
            "negative-energy modes (m = {}): weight on positive subspace vs |beta|^2 and \
             eps(v) = -eps(u): max dev {}",
            fmt17(PAIR_ANTIPARTICLE_MASS),
            fmt17(pair_anti_dev)
        ),
    );
    summary.check(
        "pair_eos_relativistic_to_dust",
        pair_eos_ok,
        &format!(
            "w of the produced gas decreasing, w(a_end) <= {}: w(1) = {:?}, w(a_end) = {:?}",
            fmt17(PAIR_W_LATE_MAX),
            mass_results[1..]
                .iter()
                .map(|m| fmt17(m.w_at_1))
                .collect::<Vec<_>>(),
            mass_results[1..]
                .iter()
                .map(|m| fmt17(m.w_end))
                .collect::<Vec<_>>()
        ),
    );

    // ------------------------------------------------------- summary --
    let trial_json: Vec<Json> = trials
        .iter()
        .map(|t| {
            Json::object(vec![
                ("node", Json::Int(t.node as i64)),
                ("k", Json::Float(grid.k[t.node])),
                ("method", Json::str(method_name(t.method))),
                ("steps", Json::Int(t.steps)),
                ("rhsEvals", Json::Int(t.rhs_evals)),
                ("linRhsEvals", Json::Int(t.lin_rhs_evals)),
                ("maxErrorVsReference", Json::Float(t.error)),
                ("maxNormDrift", Json::Float(t.norm_drift)),
            ])
        })
        .collect();
    let mass_json: Vec<Json> = mass_results
        .iter()
        .map(|m| {
            Json::object(vec![
                ("m", Json::Float(m.mass)),
                ("a2End", Json::Float(m.a2_end)),
                ("tEnd", Json::Float(m.t_end)),
                ("nA3", Json::Float(m.n_a3)),
                ("nA3Adiabatic", Json::Float(m.n_a3_adiabatic)),
                ("nA3AtKink", Json::Float(m.n_a3_kink)),
                ("rhoA3End", Json::Float(m.rho_a3_end)),
                ("wFrozenSpectrumAtA1", Json::Float(m.w_at_1)),
                ("wEnd", Json::Float(m.w_end)),
                ("maxBeta2", Json::Float(m.max_beta2)),
                ("maxBeta2Adiabatic", Json::Float(m.max_beta2_adiabatic)),
                ("kPeakK3Beta2", Json::Float(m.k_peak)),
                ("tailNodes", Json::Int(m.tail_nodes as i64)),
                ("tailMaxRelDev", Json::Float(m.tail_max_dev)),
                ("initialBeta2Max", Json::Float(m.initial_beta2_max)),
            ])
        })
        .collect();
    let extra = vec![
        (
            "parameters",
            Json::object(vec![
                (
                    "thermal",
                    Json::object(vec![
                        ("m", Json::Float(MASS)),
                        ("temperature", Json::Float(TEMPERATURE)),
                        ("hubbleInitial", Json::Float(HUBBLE_INITIAL)),
                        ("tInitial", Json::Float(T_INITIAL)),
                        ("aEnd", Json::Float(A_END)),
                        ("tEnd", Json::Float(t_end)),
                        ("kMax", Json::Float(K_MAX)),
                        ("nodes", Json::Int(N_K as i64)),
                        ("outputIntervals", Json::Int(N_OUT as i64)),
                        ("degeneracy", Json::Float(DEGENERACY)),
                        ("momentumDirection", Json::Int(1)),
                        (
                            "spinNodes",
                            Json::Array(SPIN_NODES.iter().map(|n| Json::Int(*n as i64)).collect()),
                        ),
                        ("antiparticleNode", Json::Int(ANTIPARTICLE_NODE as i64)),
                        (
                            "adiabaticVacuumNodes",
                            Json::Array(
                                ADIABATIC_VACUUM_NODES
                                    .iter()
                                    .map(|n| Json::Int(*n as i64))
                                    .collect(),
                            ),
                        ),
                    ]),
                ),
                (
                    "pair",
                    Json::object(vec![
                        ("hubbleInflation", Json::Float(HUBBLE_INFLATION)),
                        ("kOverAStart", Json::Float(K_OVER_A_START)),
                        ("masses", Json::floats(&PAIR_MASSES)),
                        ("kMin", Json::Float(PAIR_K_MIN)),
                        ("kMax", Json::Float(PAIR_K_MAX)),
                        ("nodes", Json::Int(N_PAIR_K as i64)),
                        ("hubbleEndOverMass", Json::Float(HUBBLE_END_OVER_MASS)),
                        ("masslessA2End", Json::Float(MASSLESS_A2_END)),
                        ("samples", Json::Int(N_PAIR_SAMPLES as i64)),
                        ("eosPoints", Json::Int(N_PAIR_EOS as i64)),
                        ("antiparticleMass", Json::Float(PAIR_ANTIPARTICLE_MASS)),
                        (
                            "antiparticleNodes",
                            Json::Array(
                                PAIR_ANTIPARTICLE_NODES
                                    .iter()
                                    .map(|n| Json::Int(*n as i64))
                                    .collect(),
                            ),
                        ),
                        ("tailKMin", Json::Float(PAIR_TAIL_K)),
                    ]),
                ),
            ]),
        ),
        (
            "stateLayout",
            Json::str("u_re_0..u_re_15, u_im_0..u_im_15 (u = re + i im in C^16)"),
        ),
        (
            "counting",
            Json::object(vec![
                (
                    "thermal",
                    Json::str(
                        "16 states per comoving k (8 particles + 8 antiparticles), Fermi-Dirac \
                         f = 1/(exp(E_i/T_i)+1); rho = (16/(2 pi^2 a^3)) sum w k^2 f eps(u_k), \
                         p = (16/(2 pi^2 a^3)) sum w k^2 f p_1(u_k)/3 (direction average of the \
                         momentum flux, k along x1)",
                    ),
                ),
                (
                    "pair",
                    Json::str(
                        "Dirac sea: 8 filled negative-energy states per k, each ends with weight \
                         |beta_k|^2 on the positive-energy subspace -> 8|beta|^2 particles + \
                         8|beta|^2 antiparticles: n a^3 = (16/(2 pi^2)) int k^2 |beta_k|^2 dk",
                    ),
                ),
            ]),
        ),
        (
            "methodSelection",
            Json::object(vec![
                ("selected", Json::str(method_name(method))),
                ("window", Json::floats(&[1.0, A_METHOD_TEST])),
                ("testRtol", Json::Float(DEFAULT_TOLERANCES.rtol)),
                ("testAtol", Json::Float(DEFAULT_TOLERANCES.atol)),
                (
                    "rule",
                    Json::str(
                        "at the default tolerances, the method with a factor-2 smaller max error \
                         vs an Adams reference at rtol/10, atol/10 wins; otherwise the one with \
                         fewer RHS evaluations (incl. difference-quotient Jacobian evaluations)",
                    ),
                ),
                ("trials", Json::Array(trial_json)),
            ]),
        ),
        (
            "limits",
            Json::object(vec![
                ("eigen", Json::Float(EIGEN_LIMIT)),
                ("unitarity", Json::Float(UNITARITY_LIMIT)),
                ("krein", Json::Float(KREIN_LIMIT)),
                ("identity", Json::Float(IDENTITY_LIMIT)),
                ("kinetic", Json::Float(KINETIC_LIMIT)),
                ("spin", Json::Float(SPIN_LIMIT)),
                ("antiparticle", Json::Float(ANTIPARTICLE_LIMIT)),
                ("beta", Json::Float(BETA_LIMIT)),
                ("masslessBeta", Json::Float(MASSLESS_BETA_LIMIT)),
                ("suddenStart", Json::Float(SUDDEN_START_LIMIT)),
                ("suddenStartFloor", Json::Float(SUDDEN_START_FLOOR)),
                ("betaFloor", Json::Float(BETA_FLOOR)),
                ("tail", Json::Float(TAIL_LIMIT)),
                ("wEarly", Json::Float(W_EARLY_LIMIT)),
                ("wLateMax", Json::Float(W_LATE_MAX)),
                ("pairWLateMax", Json::Float(PAIR_W_LATE_MAX)),
            ]),
        ),
        (
            "thermal",
            Json::object(vec![
                ("wAtA1", Json::Float(w_first)),
                ("wAtAEnd", Json::Float(w_last)),
                ("wKineticAtA1", Json::Float(w_kin_first)),
                ("wKineticAtAEnd", Json::Float(w_kin_last)),
                ("maxRelDevRho", Json::Float(max_dev_rho)),
                ("maxRelDevP", Json::Float(max_dev_p)),
                ("maxUnitarityDev", Json::Float(unitarity)),
                ("maxKreinDrift", Json::Float(krein_drift)),
                ("maxIdentityResidual", Json::Float(max_identity)),
                ("maxBeta2GasWeighted", Json::Float(max_beta_weighted)),
                ("maxBeta2PerMode", Json::Float(beta_max_instantaneous)),
                ("maxBeta2PerModeK", Json::Float(grid.k[beta_max_node])),
                ("suddenStartMaxRelDev", Json::Float(sudden_dev)),
                ("suddenStartComparedModes", Json::Int(sudden_compared as i64)),
                ("suddenStartBoundMaxRatio", Json::Float(sudden_bound_ratio)),
                ("adiabaticVacuumLateBeta2", Json::Float(adiabatic_vacuum_late)),
                ("adiabaticVacuumMaxAdiabaticBeta2", Json::Float(adiabatic_vacuum_max)),
                (
                    "adiabaticVacuumMaxRelPressureDev",
                    Json::Float(pressure_dev_adiabatic),
                ),
                (
                    "instantaneousStartMaxRelPressureDevSameNodes",
                    Json::Float(pressure_dev_instantaneous),
                ),
                ("pressureEnvelopeMaxRatio", Json::Float(pressure_envelope_ratio)),
                ("spinMaxDev", Json::Float(spin_dev)),
                ("antiparticleMaxDev", Json::Float(anti_dev)),
                ("modeSolverStats", Json::Array(mode_stats)),
            ]),
        ),
        (
            "pair",
            Json::object(vec![
                ("maxEigenResidual", Json::Float(pair_residual)),
                ("maxUnitarityDev", Json::Float(pair_unitarity)),
                ("maxKreinDrift", Json::Float(pair_krein)),
                ("maxInitialBeta2", Json::Float(initial_beta)),
                ("tailMaxRelDev", Json::Float(tail_dev)),
                ("antiparticleMaxDev", Json::Float(pair_anti_dev)),
                ("masses", Json::Array(mass_json)),
            ]),
        ),
        (
            "findings",
            Json::Array(vec![
                Json::str(
                    "Per-mode |beta_k|^2 <= 1e-6 (NUMERICS_CONTRACT) is not attainable at \
                     H_i/m = 0.05: the instantaneous-eigenvector start leaves a free wave \
                     |c|^2 = (m k H_i/(4 E_i^3))^2 (max (H_i/(10.4 m))^2 = 2.3e-5 at k = m/sqrt 2), \
                     and its first half-oscillation reaches 4|c|^2. Measured maximum and the \
                     comparison with |c|^2 are in 'thermal'. The gas-weighted |beta|^2, the \
                     adiabatic-vacuum runs and all bulk (k >> m) modes stay below 1e-6.",
                ),
                Json::str(
                    "The same free wave beta enters p_1 and s at FIRST order, \
                     p_1 = (1 - 2|beta|^2) K^2/E + 2 Re(alpha^* beta) m K/E (eps has no \
                     interference term), so the mode-sum pressure deviates from kinetic theory \
                     by ~2e-5 (independent of the solver tolerance) while rho agrees to ~1e-7; \
                     the check compares |p - p_kin| with the predicted interference envelope. \
                     The adiabatic-vacuum runs show the deviation is removed by an adiabatic start.",
                ),
                Json::str(
                    "Lagrangian split for the gas: KE_L = PE_L = rho/2 exactly (w_L = 0); the \
                     scalar-field relation p = KE - PE holds only for homogeneous condensates. \
                     Hamiltonian split: KE_H = 3p (momentum energy), PE_H = rho - 3p (rest mass).",
                ),
                Json::str(
                    "Spin independence and antiparticle symmetry are exact consequences of \
                     h(t) = (m sigma_z + K sigma_x) (x) I_8 and C h^* C = -h; the runs verify \
                     them to solver accuracy.",
                ),
                Json::str(
                    "m = 0: h = K(t) sigma_x (x) I_8 has time-independent eigenvectors, so no \
                     pairs are created (conformal invariance); measured |beta|^2 is roundoff.",
                ),
            ]),
        ),
    ];
    let doc = standard_summary(ctx, &summary, &tolerances, solver_description, extra);
    write_json(&directory.join("summary.json"), &doc)?;
    summary.add_file("summary.json");
    Ok(summary)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::spinor::mode_rhs;

    #[test]
    fn gauss_legendre_small_orders_and_exactness() {
        let (x, w) = gauss_legendre(2);
        assert!((x[1] - (1.0f64 / 3.0).sqrt()).abs() < 1e-16 && x[0] == -x[1]);
        assert!((w[0] - 1.0).abs() < 1e-15 && (w[1] - 1.0).abs() < 1e-15);
        let (x, w) = gauss_legendre(5);
        assert_eq!(x[2], 0.0);
        assert!((w[2] - 128.0 / 225.0).abs() < 1e-15);
        for n in [5usize, 48, 64] {
            let (x, w) = gauss_legendre(n);
            for degree in 0..(2 * n) {
                let exact = if degree % 2 == 1 {
                    0.0
                } else {
                    2.0 / (degree as f64 + 1.0)
                };
                let sum: f64 = x
                    .iter()
                    .zip(&w)
                    .map(|(xi, wi)| wi * xi.powi(degree as i32))
                    .sum();
                assert!((sum - exact).abs() < 1e-13, "n={n} degree={degree}");
            }
            assert!(x.windows(2).all(|p| p[0] < p[1]));
        }
    }

    #[test]
    fn sparse_rhs_equals_dense_rhs() {
        let alg = Algebra::new();
        let ops = ModeOperator::new(&alg).unwrap();
        let mut y = vec![0.0; 32];
        for (i, value) in y.iter_mut().enumerate() {
            *value = 0.3 + 0.17 * i as f64 - 0.01 * (i * i) as f64;
        }
        for (mass, kk) in [(1.0, 0.7), (0.0, 3.0), (2.0, 1.0e-3)] {
            let (h, _) = hamiltonian(&alg, mass, kk);
            let mut dense = vec![0.0; 32];
            let mut sparse = vec![0.0; 32];
            mode_rhs(&h, &y, &mut dense);
            ops.rhs(mass, kk, &y, &mut sparse);
            for i in 0..32 {
                assert!((dense[i] - sparse[i]).abs() <= 1e-15, "{mass} {kk} {i}");
            }
        }
    }

    #[test]
    fn two_level_structure_and_charge_conjugation() {
        let alg = Algebra::new();
        // sigma_z = -i gamma^4 and sigma_x = -gamma^4 gamma^1 anticommute and square to I
        let sz = CMat16::from_real(&alg.gamma[4]).scale(0.0, -1.0);
        let sx = CMat16::from_real(&alg.g4g[1]).scale(-1.0, 0.0);
        assert_eq!(sz.mul(&sz), CMat16::identity());
        assert_eq!(sx.mul(&sx), CMat16::identity());
        assert_eq!(sz.mul(&sx).add(&sx.mul(&sz)).max_abs(), 0.0);
        // C h^* C = -h
        let (h, _) = hamiltonian(&alg, 0.8, 1.7);
        let c = CMat16::from_real(&alg.charge);
        let h_conj = CMat16 {
            re: h.re,
            im: h.im.map(|row| row.map(|v| -v)),
        };
        assert!(c.mul(&h_conj).mul(&c).add(&h).max_abs() < 1e-15);
    }

    #[test]
    fn adiabatic_state_and_beta_diagnostics() {
        let alg = Algebra::new();
        let (mass, kk, hubble) = (1.0, 0.9, 0.05);
        let (h, e) = hamiltonian(&alg, mass, kk);
        let hdot = hamiltonian_rate(&alg, kk, hubble);
        let e_plus = eigen_state(&alg, &h, e, 1.0, 1.0).unwrap();
        let d0 = diagnostics(&alg, mass, kk, hubble, &e_plus, 1.0);
        assert!(d0.beta2 < 1e-28);
        let c = mass * kk * hubble / (4.0 * e * e * e);
        // the eigenvector's adiabatic-basis weight is the dressing |c|^2
        assert!((d0.beta2_adiabatic / (c * c) - 1.0).abs() < 1e-12);
        // the first-order adiabatic state has instantaneous weight ~|c|^2 and
        // (to second order) no weight on the adiabatic negative subspace
        let u = adiabatic_state(&h, &hdot, e, 1.0, &e_plus);
        let d1 = diagnostics(&alg, mass, kk, hubble, &u, 1.0);
        assert!((d1.beta2 / (c * c) - 1.0).abs() < 1e-3);
        assert!(d1.beta2_adiabatic < 1e-6 * c * c);
        assert!((d1.eps - e * (1.0 - 2.0 * d1.beta2)).abs() < 1e-14);
        // negative-energy counterpart
        let e_minus = eigen_state(&alg, &h, e, -1.0, 1.0).unwrap();
        let v = adiabatic_state(&h, &hdot, e, -1.0, &e_minus);
        let dv = diagnostics(&alg, mass, kk, hubble, &v, -1.0);
        assert!((dv.beta2 - d1.beta2).abs() < 1e-15);
        assert!(dv.beta2_adiabatic < 1e-6 * c * c);
        assert!((d1.krein - 1.0).abs() < 1e-14 && (dv.krein - 1.0).abs() < 1e-14);
    }

    #[test]
    fn parallel_map_keeps_order() {
        let items: Vec<usize> = (0..37).collect();
        let out = parallel_map(&items, |i| Ok(i * i)).unwrap();
        assert_eq!(out, items.iter().map(|i| i * i).collect::<Vec<_>>());
        let failed = parallel_map(&items, |i| {
            if *i == 5 {
                Err("x".to_string())
            } else {
                Ok(*i)
            }
        });
        assert!(failed.is_err());
    }
}
