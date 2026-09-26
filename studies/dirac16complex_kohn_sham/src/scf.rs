//! Kohn-Sham self-consistency for the dirac16complex gas in the static
//! primordial field (STAGE4_SPEC sections 3-5).
//!
//! * 3-space: coordinate torus of size l, `k in (2 pi / l) Z^3`, shells
//!   `|k|^2 = (Delta k)^2 n2` with lattice multiplicity g(n2); the spectrum
//!   depends on |k| only (computed with k = (|k|, 0, 0)).
//! * Levels: for every shell and parity the s = +1 block problem of
//!   `shooting.rs` gives the states (eps, s = +1) with multiplicity 4 g; the
//!   s = -1 block problem (the s = +1 problem with the vector potential
//!   negated and eps -> -eps, identical profiles) gives the states
//!   (eps, s = -1), multiplicity 4 g.  For v_x = 0 the two are mirror images.
//! * Branches (normal ordering with respect to the FREE Dirac sea): a state
//!   is a particle state (branch +1) when its non-interacting partner -- the
//!   level with the same (shell, parity, block type, Pruefer index) at
//!   lambda = 0 -- has eps_free >= 0, and a sea state (branch -1) otherwise.
//!   The Pruefer index is a continuous label (Theta(eps) is monotone), so
//!   this is the identification by continuity from lambda = 0; the sign of
//!   the interacting eps itself is NOT used (the vector potential shifts
//!   whole bands: the k = 0 brane zero modes move to eps = <v_x> < 0 for
//!   lambda > 0 and stay particle states).  The exact k = 0 zero mode
//!   (eps_free = 0) is a particle state in both block types.
//! * Occupations (thermal antiparticles included): a particle state carries
//!   the weight `w = f(eps)`, a sea state `w = -(1 - f(eps))` (a hole in the
//!   sea = antiparticle), `f = 1/(e^{(eps - mu)/T} + 1)`; mu by bisection on
//!   N = sum mult w.  At T = 0 the particle states are filled in order of eps
//!   (ensemble/fractional occupation of the shell that straddles N) and the
//!   sea stays full; an overlap of the two branches (a sea level above the
//!   lowest occupied particle level) is recorded as a diagnostic.
//! * Densities: coordinate `n_c(y) = sum mult w (a^2 + b^2)/l^3`,
//!   `S_c(y) = sum mult w (-2 s a b)/l^3`; proper `n_p = e^{-6Hy} n_c`,
//!   `S_p = e^{-6Hy} S_c` (per unit coordinate extra-time volume).
//! * Potentials: `M_eff = m + lambda S_p + v_s(S_p) = m + (15/16) lambda S_p`,
//!   `v_x = v_v(n_p) = -lambda n_p / 16` (exchange.rs).
//! * Energies: `E = sum mult w eps - int [(lambda/2) S_p^2 + e_x] dV_p`,
//!   `dV_p = e^{6Hy} l^3 dy`; entropy `-sum mult [f ln f + (1-f) ln(1-f)]`
//!   over all states; `F = E - T S_ent`, `Omega = F - mu N`.
//! * Level crossings at the Fermi level (measured at N = 1016, attractive
//!   lambda_hat_2: the k = 0 bulk level is pulled to within 1e-4 of the
//!   192-fold brane band): the exact T = 0 aufbau occupations then flip
//!   between iterations (charge sloshing, no mixing parameter cures it) and
//!   the loop is stopped as stagnant; [`solve_ground`] retries with
//!   an annealed Fermi-Dirac occupation smearing (1e-2 m, 1e-3 m, 1e-4 m,
//!   then exact occupations again; damped mixing, beta x 1/4) and records
//!   the smearing
//!   in the solution's parameters (`run.json: parameters.occupationSmearing`,
//!   `exactZeroTemperatureOccupations = false`); F = E - T S_ent uses the
//!   physical T = 0, the smearing entropy is reported.
//! * Mixing: Anderson (Pulay) on the pair (n_c, S_c); convergence when
//!   `max|Delta n_c| / D < tol` and `max|Delta S_c| / D < tol` with
//!   `D = max(max|n_c|, max|S_c|)` (tol 1e-10).
//! * Delta-SCF: occupations fixed by level identity (shell, parity, s,
//!   Pruefer index) with one particle moved from the HOMO group to the LUMO
//!   group, re-converged; `E_1 - E_0`.

use std::collections::HashMap;
use std::sync::atomic::{AtomicUsize, Ordering as AtomicOrdering};
use std::sync::Arc;

use crate::exchange::{effective_mass, exchange_energy_density, v_vector};
use crate::geometry::density_factor;
use crate::math::{exp, fermi, log, PI};
use crate::shooting::{grid_points, simpson, Level, Potential, Shooter, Stats};
use crate::spline::Spline;
use crate::Tolerances;

/// Physical and numerical parameters of one Kohn-Sham problem.
#[derive(Clone, Debug, PartialEq)]
pub struct Params {
    pub h: f64,
    pub m: f64,
    pub a4: f64,
    pub length: f64,
    pub grid_n: usize,
    /// Delta k = 2 pi / l in units of m (0.25).
    pub delta_k_over_m: f64,
    /// lambda_hat = lambda m^6.
    pub lambda_hat: f64,
    /// Temperature (absolute, same units as m; T = 0 allowed).
    pub temperature: f64,
    /// Occupation smearing used ONLY by the fallback of [`solve_ground`]
    /// when the exact T = 0 aufbau occupations do not converge (a level
    /// crossing at the Fermi level): Fermi-Dirac weights at this
    /// temperature, entropy reported, F = E - T S_ent with the PHYSICAL T
    /// (0).  Zero in every other run.
    pub smearing: f64,
    pub n_particles: f64,
    /// Occupation cutoff defining the energy window at T > 0.
    pub f_cut: f64,
    /// Largest lattice n2 = n1^2 + n2^2 + n3^2 considered (safety cap).
    pub shell_cap: i64,
    pub mix_beta: f64,
    pub mix_history: usize,
    pub tol: f64,
    pub max_iter: usize,
    /// Iterations without a factor-2 improvement of the residual after
    /// which the loop stops as stagnant.
    pub stagnation_iterations: usize,
    /// T = 0 fallback of [`solve_ground`] that produced this solution: 0 none
    /// (exact occupations converged directly), 1 annealed smearing (the
    /// smallest converged rung, `smearing` > 0), 2 exact occupations
    /// re-converged after the annealing.
    pub fallback_stage: i32,
    pub tolerances: Tolerances,
}

impl Params {
    pub fn lambda(&self) -> f64 {
        self.lambda_hat / self.m.powi(6)
    }

    pub fn delta_k(&self) -> f64 {
        self.delta_k_over_m * self.m
    }

    pub fn ell(&self) -> f64 {
        2.0 * PI / self.delta_k()
    }

    pub fn volume(&self) -> f64 {
        self.ell().powi(3)
    }

    pub fn dy(&self) -> f64 {
        self.length / (self.grid_n as f64 - 1.0)
    }

    pub fn grid(&self) -> Vec<f64> {
        grid_points(self.length, self.grid_n)
    }

    /// Temperature of the Fermi-Dirac occupations: the physical T, or the
    /// smearing of the T = 0 fallback.
    pub fn occupation_temperature(&self) -> f64 {
        if self.temperature > 0.0 {
            self.temperature
        } else {
            self.smearing
        }
    }

    /// Lower edge of every energy window: all particle-branch states lie
    /// above it (the free particle branch starts at eps >= 0 and the
    /// potentials shift it by less than this margin).
    pub fn window_floor(&self) -> f64 {
        -(self.m + 1.5 * self.m + 2.0 * PI / self.length)
    }
}

/// One lattice shell.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Shell {
    pub n2: i64,
    pub multiplicity: i64,
    pub k: f64,
}

/// Shells n2 <= cap with their lattice multiplicities.
pub fn shells(delta_k: f64, cap: i64) -> Vec<Shell> {
    let r = (cap as f64).sqrt().ceil() as i64 + 1;
    let mut counts: HashMap<i64, i64> = HashMap::new();
    for n1 in -r..=r {
        for n2 in -r..=r {
            for n3 in -r..=r {
                let q = n1 * n1 + n2 * n2 + n3 * n3;
                if q <= cap {
                    *counts.entry(q).or_insert(0) += 1;
                }
            }
        }
    }
    let mut keys: Vec<i64> = counts.keys().copied().collect();
    keys.sort_unstable();
    keys.iter()
        .map(|q| Shell {
            n2: *q,
            multiplicity: counts[q],
            k: delta_k * (*q as f64).sqrt(),
        })
        .collect()
}

/// Level identity across iterations.
pub type Key = (usize, i32, i32, i64);

/// One single-particle state (a level of one block type).
#[derive(Clone, Debug)]
pub struct State {
    pub shell: usize,
    pub n2: i64,
    pub k: f64,
    pub parity: i32,
    pub s: i32,
    pub index: i64,
    pub eps: f64,
    /// 4 g(shell).
    pub mult: f64,
    pub level: Arc<Level>,
    /// +1 particle branch, -1 Dirac-sea branch (by continuity from lambda = 0).
    pub branch: i32,
    /// eps of the non-interacting partner level (same key, lambda = 0).
    pub eps_free: f64,
    /// Fermi-Dirac occupation f(eps).
    pub f: f64,
    /// Normal-ordered weight: f (particle branch) or -(1 - f) (sea branch).
    pub weight: f64,
}

impl State {
    pub fn key(&self) -> Key {
        (self.shell, self.parity, self.s, self.index)
    }
}

/// Coordinate densities on the grid.
#[derive(Clone, Debug, PartialEq)]
pub struct Densities {
    pub n_c: Vec<f64>,
    pub s_c: Vec<f64>,
}

impl Densities {
    pub fn zero(n: usize) -> Self {
        Self {
            n_c: vec![0.0; n],
            s_c: vec![0.0; n],
        }
    }
}

/// Build the potentials from the coordinate densities.
pub fn build_potential(params: &Params, densities: &Densities) -> Arc<Potential> {
    let grid = params.grid();
    let lambda = params.lambda();
    let mut m_eff = Vec::with_capacity(grid.len());
    let mut v_x = Vec::with_capacity(grid.len());
    for (i, y) in grid.iter().enumerate() {
        let factor = density_factor(params.h, *y);
        let s_p = factor * densities.s_c[i];
        let n_p = factor * densities.n_c[i];
        m_eff.push(effective_mass(params.m, lambda, s_p));
        v_x.push(v_vector(lambda, n_p));
    }
    Arc::new(Potential {
        h: params.h,
        a4: params.a4,
        length: params.length,
        grid,
        m_eff: Spline::new(-params.length, params.dy(), m_eff),
        v_x: Spline::new(-params.length, params.dy(), v_x),
    })
}

/// Potential with the vector potential negated (the s = -1 block problem).
fn negated_vector(potential: &Potential) -> Arc<Potential> {
    let mut values = potential.v_x.values.clone();
    for v in values.iter_mut() {
        *v = -*v;
    }
    Arc::new(Potential {
        h: potential.h,
        a4: potential.a4,
        length: potential.length,
        grid: potential.grid.clone(),
        m_eff: potential.m_eff.clone(),
        v_x: Spline::new(potential.v_x.y0, potential.v_x.dy, values),
    })
}

/// Energy window of one spectrum computation.
#[derive(Clone, Copy, Debug, PartialEq)]
pub struct Window {
    pub eps_lo: f64,
    pub eps_hi: f64,
}

/// All states of all shells within the window.
#[derive(Clone, Debug, Default)]
pub struct Spectrum {
    pub states: Vec<State>,
    pub shells_used: usize,
    pub shells_total: usize,
    pub stats: Stats,
    pub max_theta_residual: f64,
    pub max_matching_residual: f64,
    pub max_winding_residual: f64,
}

/// Levels of one shell (both parities, both block types).
struct ShellResult {
    shell_index: usize,
    states: Vec<State>,
    stats: Stats,
    theta: f64,
    matching: f64,
    winding: f64,
}

#[allow(clippy::too_many_arguments)]
fn solve_shell(
    params: &Params,
    potential: &Arc<Potential>,
    negated: &Arc<Potential>,
    mirror: bool,
    window: Window,
    warm: &HashMap<Key, f64>,
    shell_index: usize,
    shell: &Shell,
) -> Result<ShellResult, String> {
    let mut plus = Shooter::new(Arc::clone(potential), params.tolerances);
    let mut minus = Shooter::new(Arc::clone(negated), params.tolerances);
    let mut result = ShellResult {
        shell_index,
        states: Vec::new(),
        stats: Stats::default(),
        theta: 0.0,
        matching: 0.0,
        winding: 0.0,
    };
    let absorb = |result: &mut ShellResult, level: &Level| {
        result.theta = result.theta.max(level.theta_residual.abs());
        result.matching = result.matching.max(level.matching_residual);
        result.winding = result.winding.max(level.winding_residual.abs());
    };
    for parity in [1i32, -1] {
        let warm_plus: Vec<(i64, f64)> = warm
            .iter()
            .filter(|(key, _)| key.0 == shell_index && key.1 == parity && key.2 == 1)
            .map(|(key, e)| (key.3, *e))
            .collect();
        // Mirror case (v_x = 0): the s = -1 states are the s = +1 levels
        // with eps -> -eps, so the s = +1 problem must be solved on the
        // UNION of the window and its mirror image; otherwise an
        // asymmetric window loses every s = -1 state whose s = +1 partner
        // lies outside [eps_lo, eps_hi] (measured: the brane band +ck of
        // the shells with ck > |eps_lo| was missing from the closed-shell
        // table computed on [-1, 3.2]).
        let plus_window = if mirror {
            Window {
                eps_lo: window.eps_lo.min(-window.eps_hi),
                eps_hi: window.eps_hi.max(-window.eps_lo),
            }
        } else {
            window
        };
        let levels_found = plus
            .levels(
                shell.k,
                parity,
                plus_window.eps_lo,
                plus_window.eps_hi,
                &warm_plus,
            )
            .map_err(|e| format!("shell n2 = {} (s = +1 block): {e}", shell.n2))?;
        for level in levels_found.iter() {
            absorb(&mut result, level);
        }
        let levels_minus: Vec<Level> = if mirror {
            levels_found
                .iter()
                .filter(|l| -l.eps >= window.eps_lo && -l.eps <= window.eps_hi)
                .cloned()
                .collect()
        } else {
            // warm values for s = -1 are stored as the negated problem's eigenvalues
            let warm_minus: Vec<(i64, f64)> = warm
                .iter()
                .filter(|(key, _)| key.0 == shell_index && key.1 == parity && key.2 == -1)
                .map(|(key, e)| (key.3, *e))
                .collect();
            let levels = minus
                .levels(shell.k, parity, -window.eps_hi, -window.eps_lo, &warm_minus)
                .map_err(|e| {
                    format!(
                        "shell n2 = {} (s = -1 block, negated vector potential): {e}",
                        shell.n2
                    )
                })?;
            for level in levels.iter() {
                absorb(&mut result, level);
            }
            levels
        };
        for level in levels_found
            .into_iter()
            .filter(|l| l.eps >= window.eps_lo && l.eps <= window.eps_hi)
        {
            result.states.push(State {
                shell: shell_index,
                n2: shell.n2,
                k: shell.k,
                parity,
                s: 1,
                index: level.index,
                eps: level.eps,
                mult: 4.0 * shell.multiplicity as f64,
                level: Arc::new(level),
                branch: 0,
                eps_free: f64::NAN,
                f: 0.0,
                weight: 0.0,
            });
        }
        for level in levels_minus.into_iter() {
            let eps = -level.eps;
            result.states.push(State {
                shell: shell_index,
                n2: shell.n2,
                k: shell.k,
                parity,
                s: -1,
                index: level.index,
                eps,
                mult: 4.0 * shell.multiplicity as f64,
                level: Arc::new(level),
                branch: 0,
                eps_free: f64::NAN,
                f: 0.0,
                weight: 0.0,
            });
        }
    }
    result.stats = plus.stats;
    result.stats.add(&minus.stats);
    Ok(result)
}

/// Shells per scheduling block, in units of the thread count.
pub const SHELL_BLOCK_FACTOR: usize = 4;

/// Number of worker threads (shells are independent; results are merged in
/// shell order, so the output does not depend on the thread count).
pub fn worker_threads() -> usize {
    std::thread::available_parallelism()
        .map(|n| n.get())
        .unwrap_or(1)
        .clamp(1, 32)
}

/// Compute the spectrum for the potentials; `warm` maps keys to previous
/// eigenvalues.  Shells are processed in blocks in parallel; the scan stops
/// after two consecutive shells without any level in the window (the lowest
/// |eps| of a shell grows with k).
pub fn compute_spectrum(
    params: &Params,
    potential: &Arc<Potential>,
    window: Window,
    warm: &HashMap<Key, f64>,
) -> Result<Spectrum, String> {
    let shell_list = shells(params.delta_k(), params.shell_cap);
    let mirror = potential.v_x.values.iter().all(|v| *v == 0.0);
    let negated = negated_vector(potential);
    let threads = worker_threads();
    let mut spectrum = Spectrum {
        shells_total: shell_list.len(),
        ..Spectrum::default()
    };
    let mut empty_in_a_row = 0;
    let mut start = 0;
    // blocks of SHELL_BLOCK_FACTOR x threads shells; inside a block the
    // workers pull shells from a shared counter (the work per shell is
    // uneven: many levels at small k, stiff integrations at large k), and
    // the results are put back into shell order, so the output does not
    // depend on the thread count or on the scheduling
    let block_size = SHELL_BLOCK_FACTOR * threads;
    'blocks: while start < shell_list.len() {
        let stop = (start + block_size).min(shell_list.len());
        let next = AtomicUsize::new(start);
        let results: Vec<Result<ShellResult, String>> = std::thread::scope(|scope| {
            let handles: Vec<_> = (0..threads.min(stop - start))
                .map(|_| {
                    let potential = Arc::clone(potential);
                    let negated = Arc::clone(&negated);
                    let next = &next;
                    let shell_list = &shell_list;
                    scope.spawn(move || {
                        let mut out: Vec<(usize, Result<ShellResult, String>)> = Vec::new();
                        loop {
                            let index = next.fetch_add(1, AtomicOrdering::SeqCst);
                            if index >= stop {
                                break;
                            }
                            let shell = shell_list[index];
                            out.push((
                                index,
                                solve_shell(
                                    params, &potential, &negated, mirror, window, warm, index,
                                    &shell,
                                ),
                            ));
                        }
                        out
                    })
                })
                .collect();
            let mut collected: Vec<(usize, Result<ShellResult, String>)> = Vec::new();
            for handle in handles {
                match handle.join() {
                    Ok(part) => collected.extend(part),
                    Err(_) => {
                        collected.push((usize::MAX, Err("shell thread panicked".to_string())))
                    }
                }
            }
            collected.sort_by_key(|(index, _)| *index);
            collected.into_iter().map(|(_, result)| result).collect()
        });
        for result in results {
            let result = result?;
            spectrum.stats.add(&result.stats);
            spectrum.max_theta_residual = spectrum.max_theta_residual.max(result.theta);
            spectrum.max_matching_residual = spectrum.max_matching_residual.max(result.matching);
            spectrum.max_winding_residual = spectrum.max_winding_residual.max(result.winding);
            spectrum.shells_used = result.shell_index + 1;
            if result.states.is_empty() {
                empty_in_a_row += 1;
            } else {
                empty_in_a_row = 0;
            }
            spectrum.states.extend(result.states);
            if empty_in_a_row >= 2 {
                break 'blocks;
            }
        }
        start = stop;
    }
    spectrum.states.sort_by(|a, b| {
        a.eps
            .partial_cmp(&b.eps)
            .unwrap_or(std::cmp::Ordering::Equal)
            .then(a.key().cmp(&b.key()))
    });
    Ok(spectrum)
}

/// Non-interacting reference levels (lambda = 0) by (shell, parity, index):
/// they define the particle/sea branches.  The free spectrum is computed in
/// parallel over the shells ([`compute_spectrum`] on the free potential) for
/// the union of the windows requested so far, widened by the eigenvalue-shift
/// bound of the interacting problem; keys outside it fall back to a serial
/// level search.  (Measured before this design: at T = m the window holds
/// ~75000 levels and the serial per-state search cost as much as the whole
/// parallel spectrum multiplied by the thread count.)
pub struct FreeLevels {
    params: Params,
    /// The solve this cache serves is interacting (lambda != 0).
    interacting: bool,
    potential: Arc<Potential>,
    shooter: Shooter,
    shells: Vec<Shell>,
    cache: HashMap<(usize, i32, i64), f64>,
    covered: Option<Window>,
    prefetch_stats: Stats,
}

/// Cap of the window widening used by [`FreeLevels::classify`] (in units of
/// m); beyond it the serial fallback handles the misses.
pub const FREE_WINDOW_SHIFT_CAP: f64 = 3.0;
/// Quantum of the window widening (in units of m): the eigenvalue-shift
/// bound is rounded UP to a multiple of it (at least one quantum for an
/// interacting solve), so that the small iteration-to-iteration changes of
/// the bound do not trigger a new prefetch.  A prefetch that is not covered
/// recomputes the whole (mirror-symmetric) union window; measured at T = m
/// with lambda != 0 before this rule: ~1e6 free-level integrations in every
/// iteration, more than the interacting spectrum itself.
pub const FREE_WINDOW_QUANTUM: f64 = 0.25;

// The free levels are cached per solve only (no process-wide cache): a
// shared cache would change the warm starts of later solves and hence the
// 1e-12-level path of the root search, so that the same solve would no
// longer be byte-identical within one process (measured by the unit test
// `repeat_run_is_byte_identical`).

impl FreeLevels {
    pub fn new(params: &Params) -> Self {
        let potential = Arc::new(Potential::free(
            params.h,
            params.a4,
            params.length,
            params.m,
            params.grid_n,
        ));
        let mut free = params.clone();
        free.lambda_hat = 0.0;
        Self {
            params: free,
            interacting: params.lambda_hat != 0.0,
            potential: Arc::clone(&potential),
            shooter: Shooter::new(potential, params.tolerances),
            shells: shells(params.delta_k(), params.shell_cap),
            cache: HashMap::new(),
            covered: None,
            prefetch_stats: Stats::default(),
        }
    }

    /// Window widened by the eigenvalue-shift bound, rounded up to a
    /// multiple of [`FREE_WINDOW_QUANTUM`] m (at least one quantum for an
    /// interacting solve) and capped at [`FREE_WINDOW_SHIFT_CAP`] m.
    pub fn widened(&self, window: Window, shift_bound: f64) -> Window {
        let m = self.params.m;
        let quantum = FREE_WINDOW_QUANTUM * m;
        let minimum = if self.interacting { 1.0 } else { 0.0 };
        let steps = (shift_bound / quantum).ceil().max(minimum);
        let widen = (steps * quantum).min(FREE_WINDOW_SHIFT_CAP * m) + 1e-6 * m;
        Window {
            eps_lo: window.eps_lo - widen,
            eps_hi: window.eps_hi + widen,
        }
    }

    /// Insert the cached free levels as warm starts (both block types; the
    /// negated problem of the s = -1 block has the same free eigenvalues)
    /// for keys the map does not have yet.
    pub fn fill_warm(&self, warm: &mut HashMap<Key, f64>) {
        for ((shell, parity, index), eps) in &self.cache {
            for s in [1i32, -1] {
                warm.entry((*shell, *parity, s, *index)).or_insert(*eps);
            }
        }
    }

    /// Make sure the cache holds every s = +1 free level with eps in
    /// `window` (and every level whose mirror lies in it).  A no-op for a
    /// non-interacting solve: its own spectrum IS the free spectrum
    /// ([`FreeLevels::classify`]).
    pub fn prefetch(&mut self, window: Window) -> Result<(), String> {
        if !self.interacting {
            return Ok(());
        }
        let needed = match self.covered {
            Some(c) if c.eps_lo <= window.eps_lo && c.eps_hi >= window.eps_hi => return Ok(()),
            Some(c) => Window {
                eps_lo: c.eps_lo.min(window.eps_lo),
                eps_hi: c.eps_hi.max(window.eps_hi),
            },
            None => window,
        };
        let spectrum = compute_spectrum(&self.params, &self.potential, needed, &HashMap::new())?;
        self.prefetch_stats.add(&spectrum.stats);
        for st in &spectrum.states {
            // an s = -1 state of index n is the mirror of the s = +1 level n
            let eps_plus = if st.s == 1 { st.eps } else { -st.eps };
            self.cache
                .entry((st.shell, st.parity, st.index))
                .or_insert(eps_plus);
        }
        self.covered = Some(needed);
        Ok(())
    }

    /// eps at lambda = 0 of the s = +1 level (shell, parity, index).
    pub fn level(
        &mut self,
        shell: usize,
        parity: i32,
        index: i64,
        guess: f64,
    ) -> Result<f64, String> {
        if let Some(e) = self.cache.get(&(shell, parity, index)) {
            return Ok(*e);
        }
        let k = self.shells[shell].k;
        let (eps, _) = self.shooter.find_level(k, parity, index, guess, 0.25)?;
        let eps = if eps.abs() < crate::shooting::ZERO_SNAP {
            0.0
        } else {
            eps
        };
        self.cache.insert((shell, parity, index), eps);
        Ok(eps)
    }

    /// Assign branch and eps_free to every state of the spectrum computed on
    /// `window`; `shift_bound` is the largest possible distance between an
    /// interacting level and its free partner (max |M_eff - m| + max |v_x|,
    /// the norm of the perturbation of the self-adjoint block Hamiltonian),
    /// used to widen the prefetched free window (capped at
    /// [`FREE_WINDOW_SHIFT_CAP`] m; misses use the serial search).  For a
    /// non-interacting solve (lambda = 0: M_eff = m, v_x = 0 exactly) the
    /// spectrum is itself the free spectrum and every state is its own
    /// partner, `eps_free = eps` (measured before this shortcut: at T = m the
    /// free prefetch repeated the whole spectrum, 680000 integrations).
    pub fn classify(
        &mut self,
        spectrum: &mut Spectrum,
        window: Window,
        shift_bound: f64,
    ) -> Result<(), String> {
        if !self.interacting {
            for st in spectrum.states.iter_mut() {
                st.eps_free = st.eps;
                st.branch = if st.eps >= 0.0 { 1 } else { -1 };
            }
            return Ok(());
        }
        self.prefetch(self.widened(window, shift_bound))?;
        for st in spectrum.states.iter_mut() {
            let guess = if st.s == 1 { st.eps } else { -st.eps };
            let free_plus = self.level(st.shell, st.parity, st.index, guess)?;
            // the s = -1 state with index n is the mirror (eps -> -eps) of the
            // s = +1 level n of the free problem
            let eps_free = if st.s == 1 { free_plus } else { -free_plus };
            st.eps_free = eps_free;
            st.branch = if eps_free >= 0.0 { 1 } else { -1 };
        }
        Ok(())
    }

    /// Solver statistics of the prefetches and of the serial fallback.
    pub fn stats(&self) -> Stats {
        let mut total = self.prefetch_stats;
        total.add(&self.shooter.stats);
        total
    }

    /// Number of levels found by the serial fallback (diagnostic).
    pub fn fallback_integrations(&self) -> i64 {
        self.shooter.stats.integrations
    }
}

/// How the states are occupied.
#[derive(Clone, Debug, PartialEq)]
pub enum Occupation {
    /// Fill in order of eps at T = 0 (fractional straddling shell).
    Zero,
    /// Fermi-Dirac at T with mu from N.
    Thermal,
    /// Per-state occupations fixed by level identity (Delta-SCF).
    Constrained(Vec<(Key, f64)>),
}

/// Occupation result.
#[derive(Clone, Debug, Default)]
pub struct Filling {
    pub mu: f64,
    pub n_total: f64,
    pub homo: Option<(Key, f64)>,
    pub lumo: Option<(Key, f64)>,
    /// Highest sea-branch level in the window (diagnostic of branch overlap).
    pub sea_top: f64,
    /// Lowest occupied particle-branch level.
    pub particle_bottom: f64,
}

fn weight_of(branch: i32, f: f64) -> f64 {
    if branch > 0 {
        f
    } else {
        -(1.0 - f)
    }
}

/// Assign occupations; returns mu (T = 0: eps of the HOMO), the total N,
/// HOMO and LUMO keys.
pub fn occupy(
    spectrum: &mut Spectrum,
    params: &Params,
    mode: &Occupation,
) -> Result<Filling, String> {
    let n_target = params.n_particles;
    let zero = Occupation::Zero;
    let t_occ = params.occupation_temperature();
    let mode = if matches!(mode, Occupation::Thermal) && t_occ <= 0.0 {
        &zero
    } else {
        mode
    };
    let states = &mut spectrum.states;
    match mode {
        Occupation::Zero => {
            for st in states.iter_mut() {
                st.f = 0.0;
                st.weight = 0.0;
            }
            // particle branch in increasing order of eps
            let mut remaining = n_target;
            let mut homo: Option<(Key, f64)> = None;
            let mut lumo: Option<(Key, f64)> = None;
            let mut i = 0;
            let n = states.len();
            while i < n {
                if states[i].branch < 0 {
                    i += 1;
                    continue;
                }
                // degenerate group: same eps within 1e-9
                let e = states[i].eps;
                let mut j = i;
                let mut group_mult = 0.0;
                while j < n && (states[j].eps - e).abs() <= 1e-9 * e.abs().max(1.0) {
                    if states[j].branch > 0 {
                        group_mult += states[j].mult;
                    }
                    j += 1;
                }
                if remaining <= 0.0 {
                    if lumo.is_none() {
                        lumo = Some((states[i].key(), e));
                    }
                    break;
                }
                let fraction = (remaining / group_mult).min(1.0);
                for st in states[i..j].iter_mut().filter(|s| s.branch > 0) {
                    st.f = fraction;
                    st.weight = fraction;
                }
                remaining -= fraction * group_mult;
                homo = Some((states[i].key(), e));
                if fraction < 1.0 {
                    lumo = Some((states[i].key(), e));
                }
                i = j;
            }
            if remaining > 1e-9 {
                return Err(format!(
                    "occupy: window too small, {remaining} particles unplaced"
                ));
            }
            // the sea stays full: f = 1 for every sea state
            for st in states.iter_mut().filter(|s| s.branch < 0) {
                st.f = 1.0;
                st.weight = 0.0;
            }
            let n_total: f64 = states.iter().map(|s| s.mult * s.weight).sum();
            let (sea_top, particle_bottom) = branch_overlap(states);
            Ok(Filling {
                mu: homo.map(|h| h.1).unwrap_or(0.0),
                n_total,
                homo,
                lumo,
                sea_top,
                particle_bottom,
            })
        }
        Occupation::Thermal => {
            let t = t_occ;
            let count = |mu: f64, states: &[State]| -> f64 {
                states
                    .iter()
                    .map(|s| s.mult * weight_of(s.branch, fermi((s.eps - mu) / t)))
                    .sum()
            };
            let scale = states.iter().map(|s| s.eps.abs()).fold(1.0, f64::max) + 60.0 * t;
            let (mut lo, mut hi) = (-scale, scale);
            if count(lo, states) > n_target || count(hi, states) < n_target {
                return Err("occupy: N not bracketed by the window".to_string());
            }
            for _ in 0..200 {
                let mid = 0.5 * (lo + hi);
                if count(mid, states) < n_target {
                    lo = mid;
                } else {
                    hi = mid;
                }
                if hi - lo < 1e-15 * scale {
                    break;
                }
            }
            let mu = 0.5 * (lo + hi);
            for st in states.iter_mut() {
                st.f = fermi((st.eps - mu) / t);
                st.weight = weight_of(st.branch, st.f);
            }
            let n_total = count(mu, states);
            // HOMO/LUMO: highest / lowest particle level with f >= 1/2 and f < 1/2
            let homo = states
                .iter()
                .rev()
                .find(|s| s.branch > 0 && s.f >= 0.5)
                .map(|s| (s.key(), s.eps));
            let lumo = states
                .iter()
                .find(|s| s.branch > 0 && s.f < 0.5)
                .map(|s| (s.key(), s.eps));
            let (sea_top, particle_bottom) = branch_overlap(states);
            Ok(Filling {
                mu,
                n_total,
                homo,
                lumo,
                sea_top,
                particle_bottom,
            })
        }
        Occupation::Constrained(map) => {
            let lookup: HashMap<Key, f64> = map.iter().cloned().collect();
            for st in states.iter_mut() {
                let f = if st.branch > 0 {
                    lookup.get(&st.key()).copied().unwrap_or(0.0)
                } else {
                    1.0
                };
                st.f = f;
                st.weight = weight_of(st.branch, f);
            }
            let n_total: f64 = states.iter().map(|s| s.mult * s.weight).sum();
            let present = states
                .iter()
                .filter(|s| lookup.contains_key(&s.key()))
                .count();
            if present != lookup.len() {
                return Err(format!(
                    "occupy: {} of {} constrained levels missing from the window",
                    lookup.len() - present,
                    lookup.len()
                ));
            }
            let mu = states
                .iter()
                .filter(|s| s.branch > 0 && s.f > 0.0)
                .map(|s| s.eps)
                .fold(f64::NEG_INFINITY, f64::max);
            let (sea_top, particle_bottom) = branch_overlap(states);
            Ok(Filling {
                mu,
                n_total,
                homo: None,
                lumo: None,
                sea_top,
                particle_bottom,
            })
        }
    }
}

/// (highest sea level, lowest occupied particle level) in the window.
fn branch_overlap(states: &[State]) -> (f64, f64) {
    let sea_top = states
        .iter()
        .filter(|s| s.branch < 0)
        .map(|s| s.eps)
        .fold(f64::NEG_INFINITY, f64::max);
    let particle_bottom = states
        .iter()
        .filter(|s| s.branch > 0 && s.f > 0.0)
        .map(|s| s.eps)
        .fold(f64::INFINITY, f64::min);
    (sea_top, particle_bottom)
}

/// Coordinate densities from the occupied spectrum.
pub fn densities_from(spectrum: &Spectrum, params: &Params) -> Densities {
    let n = params.grid_n;
    let mut d = Densities::zero(n);
    let inv_v = 1.0 / params.volume();
    for st in &spectrum.states {
        if st.weight == 0.0 {
            continue;
        }
        let w = st.mult * st.weight * inv_v;
        let s = st.s as f64;
        for i in 0..n {
            let a = st.level.a[i];
            let b = st.level.b[i];
            d.n_c[i] += w * (a * a + b * b);
            d.s_c[i] += w * (-2.0 * s * a * b);
        }
    }
    d
}

/// Energies of an occupied spectrum with the densities it produced.
#[derive(Clone, Copy, Debug, Default, PartialEq)]
pub struct Energies {
    pub ks_sum: f64,
    pub hartree: f64,
    pub exchange: f64,
    pub double_counting: f64,
    pub total: f64,
    pub entropy: f64,
    pub free: f64,
    pub grand: f64,
    pub n_total: f64,
    pub scalar_total: f64,
    pub max_lambda_s_over_m: f64,
    /// max_y |v_x(y)| / m (the vector part of the pseudo-potential).
    pub max_v_x_over_m: f64,
}

pub fn energies(spectrum: &Spectrum, densities: &Densities, params: &Params, mu: f64) -> Energies {
    let lambda = params.lambda();
    let grid = params.grid();
    let mut hartree_int = Vec::with_capacity(grid.len());
    let mut exchange_int = Vec::with_capacity(grid.len());
    let mut scalar_int = Vec::with_capacity(grid.len());
    let mut max_ratio: f64 = 0.0;
    let mut max_ratio_v: f64 = 0.0;
    for (i, y) in grid.iter().enumerate() {
        let factor = density_factor(params.h, *y);
        let s_p = factor * densities.s_c[i];
        let n_p = factor * densities.n_c[i];
        max_ratio_v = max_ratio_v.max(v_vector(lambda, n_p).abs() / params.m);
        // dV_p = e^{6Hy} l^3 dy: e^{6Hy} (lambda/2) S_p^2 = e^{-6Hy} (lambda/2) S_c^2
        hartree_int
            .push(params.volume() * factor * 0.5 * lambda * densities.s_c[i] * densities.s_c[i]);
        exchange_int.push(params.volume() / factor * exchange_energy_density(lambda, n_p, s_p));
        scalar_int.push(params.volume() * densities.s_c[i]);
        max_ratio = max_ratio.max((lambda * s_p).abs() / params.m);
    }
    let dy = params.dy();
    let hartree = simpson(dy, &hartree_int);
    let exchange = simpson(dy, &exchange_int);
    let ks_sum: f64 = spectrum
        .states
        .iter()
        .map(|s| s.mult * s.weight * s.eps)
        .sum();
    let n_total: f64 = spectrum.states.iter().map(|s| s.mult * s.weight).sum();
    let mut entropy = 0.0;
    for st in &spectrum.states {
        let f = st.f;
        if f > 0.0 && f < 1.0 {
            entropy -= st.mult * (f * log(f) + (1.0 - f) * log(1.0 - f));
        }
    }
    let total = ks_sum - hartree - exchange;
    let free = total - params.temperature * entropy;
    Energies {
        ks_sum,
        hartree,
        exchange,
        double_counting: hartree + exchange,
        total,
        entropy,
        free,
        grand: free - mu * n_total,
        n_total,
        scalar_total: simpson(dy, &scalar_int),
        max_lambda_s_over_m: max_ratio,
        max_v_x_over_m: max_ratio_v,
    }
}

/// Anderson (Pulay) mixer on a flat vector.
pub struct Anderson {
    beta: f64,
    history: usize,
    inputs: Vec<Vec<f64>>,
    residuals: Vec<Vec<f64>>,
}

impl Anderson {
    pub fn new(beta: f64, history: usize) -> Self {
        Self {
            beta,
            history,
            inputs: Vec::new(),
            residuals: Vec::new(),
        }
    }

    /// Next input from (input, output) of the current iteration.
    pub fn step(&mut self, input: &[f64], output: &[f64]) -> Vec<f64> {
        let residual: Vec<f64> = output
            .iter()
            .zip(input.iter())
            .map(|(o, i)| o - i)
            .collect();
        self.inputs.push(input.to_vec());
        self.residuals.push(residual.clone());
        if self.inputs.len() > self.history + 1 {
            self.inputs.remove(0);
            self.residuals.remove(0);
        }
        let m = self.inputs.len() - 1;
        let n = input.len();
        let mut next: Vec<f64> = input
            .iter()
            .zip(residual.iter())
            .map(|(x, r)| x + self.beta * r)
            .collect();
        if m == 0 {
            return next;
        }
        // differences relative to the latest
        let last = m;
        let dr: Vec<Vec<f64>> = (0..m)
            .map(|i| {
                (0..n)
                    .map(|j| self.residuals[i][j] - self.residuals[last][j])
                    .collect()
            })
            .collect();
        let dx: Vec<Vec<f64>> = (0..m)
            .map(|i| {
                (0..n)
                    .map(|j| self.inputs[i][j] - self.inputs[last][j])
                    .collect()
            })
            .collect();
        // normal equations (dr^T dr) gamma = dr^T r_last, regularised
        let mut a = vec![vec![0.0; m]; m];
        let mut rhs = vec![0.0; m];
        let mut trace = 0.0;
        for i in 0..m {
            for j in 0..m {
                a[i][j] = dr[i].iter().zip(dr[j].iter()).map(|(p, q)| p * q).sum();
            }
            trace += a[i][i];
            rhs[i] = dr[i].iter().zip(residual.iter()).map(|(p, q)| p * q).sum();
        }
        let reg = 1e-12 * trace.max(1e-300);
        for (i, row) in a.iter_mut().enumerate() {
            row[i] += reg;
        }
        // Gaussian elimination with partial pivoting
        let mut gamma = vec![0.0; m];
        let mut aug: Vec<Vec<f64>> = a
            .iter()
            .zip(rhs.iter())
            .map(|(row, r)| {
                let mut v = row.clone();
                v.push(*r);
                v
            })
            .collect();
        let mut singular = false;
        for c in 0..m {
            let mut pivot = c;
            for r in c + 1..m {
                if aug[r][c].abs() > aug[pivot][c].abs() {
                    pivot = r;
                }
            }
            aug.swap(c, pivot);
            if aug[c][c].abs() < 1e-300 {
                singular = true;
                break;
            }
            for r in c + 1..m {
                let factor = aug[r][c] / aug[c][c];
                let pivot_row = aug[c].clone();
                for (col, entry) in aug[r].iter_mut().enumerate().skip(c) {
                    *entry -= factor * pivot_row[col];
                }
            }
        }
        if singular {
            return next;
        }
        for c in (0..m).rev() {
            let mut value = aug[c][m];
            for col in c + 1..m {
                value -= aug[c][col] * gamma[col];
            }
            gamma[c] = value / aug[c][c];
        }
        for i in 0..m {
            for j in 0..n {
                next[j] -= gamma[i] * (dx[i][j] + self.beta * dr[i][j]);
            }
        }
        next
    }
}

/// One row of the SCF history.
#[derive(Clone, Copy, Debug, Default)]
pub struct HistoryRow {
    pub iteration: usize,
    pub residual_n: f64,
    pub residual_s: f64,
    pub mu: f64,
    pub energy: f64,
    pub free: f64,
    pub states: usize,
    pub integrations: i64,
}

/// A converged (or terminated) Kohn-Sham solution.
#[derive(Clone, Debug)]
pub struct Solution {
    pub params: Params,
    pub potential: Arc<Potential>,
    pub spectrum: Spectrum,
    /// Output densities of the last iteration (self-consistent when converged).
    pub densities: Densities,
    pub filling: Filling,
    pub energies: Energies,
    pub window: Window,
    pub history: Vec<HistoryRow>,
    pub converged: bool,
    pub iterations: usize,
    pub stats: Stats,
}

impl Solution {
    pub fn gap(&self) -> Option<f64> {
        match (self.filling.homo, self.filling.lumo) {
            (Some(h), Some(l)) => Some(l.1 - h.1),
            _ => None,
        }
    }
}

/// Energy window from a chemical-potential estimate.  Every window reaches
/// down to [`Params::window_floor`], so that all (fully occupied) particle
/// states are counted; at T > 0 it also contains the sea states with a hole
/// occupation above f_cut (eps > mu - T ln(1/f_cut)) and the particle states
/// with f > f_cut (eps < mu + T ln(1/f_cut)).  (Measured bug of an earlier
/// version: a window starting at mu - T ln(1/f_cut) dropped the occupied
/// states below it at small T and large N, and the particle number was then
/// placed into the few states inside the window.)
pub fn window_for(params: &Params, mu: f64, margin: f64) -> Window {
    let floor = params.window_floor();
    let t_occ = params.occupation_temperature();
    if t_occ > 0.0 {
        let thermal = t_occ * log(1.0 / params.f_cut);
        Window {
            eps_lo: (mu - thermal - margin).min(floor),
            eps_hi: mu + thermal + margin,
        }
    } else {
        Window {
            eps_lo: floor,
            eps_hi: mu.max(0.0) + margin,
        }
    }
}

/// Upper bound on the window enlargements of one SCF iteration.
pub const MAX_WINDOW_ENLARGEMENTS: usize = 40;
/// Iterations without a factor-2 improvement of the residual after which an
/// SCF loop is declared stagnant (returned as not converged).
pub const STAGNATION_ITERATIONS: usize = 20;
/// Smearing ladder (in units of m) of the T = 0 fallback of [`solve_ground`],
/// traversed from the LARGEST value down (annealing).
pub const SMEARING_LADDER: [f64; 3] = [1.0e-2, 1.0e-3, 1.0e-4];
/// The fallback attempts mix with `mix_beta` times this factor, allow
/// [`FALLBACK_MAX_ITER`] iterations and declare stagnation only after
/// [`FALLBACK_STAGNATION_ITERATIONS`].
pub const FALLBACK_MIX_FACTOR: f64 = 0.25;
pub const FALLBACK_MAX_ITER: usize = 200;
pub const FALLBACK_STAGNATION_ITERATIONS: usize = 40;

fn fallback_params(params: &Params, smearing: f64) -> Params {
    let mut p = params.clone();
    p.smearing = smearing * params.m;
    p.mix_beta = params.mix_beta * FALLBACK_MIX_FACTOR;
    p.max_iter = FALLBACK_MAX_ITER;
    p.stagnation_iterations = FALLBACK_STAGNATION_ITERATIONS;
    p
}

/// Ground state at the physical temperature of `params`.  T > 0: the
/// Fermi-Dirac loop.  T = 0: exact aufbau occupations; if they do not
/// converge (a level crossing at the Fermi level: the occupations flip
/// between iterations), an ANNEALED fallback with damped mixing:
///
/// 1. starting again from the original initial state, converge with
///    Fermi-Dirac occupation smearing at the largest rung of
///    [`SMEARING_LADDER`] (the smoothest fixed-point map);
/// 2. step the smearing down the ladder, each attempt starting from the
///    previous converged solution, and stop at the first rung that does not
///    converge;
/// 3. from the smallest converged smearing, retry the exact T = 0
///    occupations (at the fixed point the Kohn-Sham gap is open, so they are
///    usually stable there).
///
/// The result is the exact T = 0 solution when step 3 converges, else the
/// converged solution with the smallest smearing (recorded in the returned
/// parameters: `occupationSmearing`, `mixBeta`; F uses the physical T = 0),
/// else the last attempt (not converged).  MEASURED motivation: at N = 1016,
/// attractive lambda_hat_2, the k = 0 bulk level crosses the 192-fold brane
/// band during the iterations; a descending-from-small ladder that started
/// each attempt from the previous FAILED attempt converged or sloshed
/// depending on 1e-11-level differences of lambda_hat (default-tolerance
/// run converged at 1e-3 m, the refined one failed every rung).
pub fn solve_ground(
    params: &Params,
    initial: Option<&Densities>,
    mu_guess: f64,
) -> Result<Solution, String> {
    if params.temperature > 0.0 {
        return solve(params, &Occupation::Thermal, initial, mu_guess);
    }
    let exact = solve(params, &Occupation::Zero, initial, mu_guess)?;
    if exact.converged {
        return Ok(exact);
    }
    let mut start: Option<Densities> = initial.cloned();
    let mut start_mu = mu_guess;
    let mut best: Option<Solution> = None;
    let mut last = exact;
    for smearing in SMEARING_LADDER {
        let attempt = solve(
            &fallback_params(params, smearing),
            &Occupation::Thermal,
            start.as_ref(),
            start_mu,
        )?;
        if !attempt.converged {
            last = attempt;
            break;
        }
        start = Some(attempt.densities.clone());
        start_mu = attempt.filling.mu;
        best = Some(attempt);
    }
    let Some(best) = best else {
        return Ok(last);
    };
    let mut exact_params = fallback_params(params, 0.0);
    exact_params.smearing = 0.0;
    exact_params.fallback_stage = 2;
    let exact_again = solve(
        &exact_params,
        &Occupation::Zero,
        Some(&best.densities),
        best.filling.mu,
    )?;
    if exact_again.converged {
        return Ok(exact_again);
    }
    let mut best = best;
    best.params.fallback_stage = 1;
    Ok(best)
}

/// Progress trace on stderr when the environment variable
/// `DIRAC16_KS_VERBOSE` is set (diagnostics only; no file content depends on it).
pub fn verbose_trace() -> bool {
    std::env::var_os("DIRAC16_KS_VERBOSE").is_some()
}

/// Run the self-consistency loop.
pub fn solve(
    params: &Params,
    mode: &Occupation,
    initial: Option<&Densities>,
    mu_guess: f64,
) -> Result<Solution, String> {
    let verbose = verbose_trace();
    let n = params.grid_n;
    let mut densities = initial.cloned().unwrap_or_else(|| Densities::zero(n));
    let mut mixer = Anderson::new(params.mix_beta, params.mix_history);
    let mut warm: HashMap<Key, f64> = HashMap::new();
    let mut history = Vec::new();
    let mut mu_estimate = mu_guess;
    let t_occ = params.occupation_temperature();
    // T = 0: room for the LUMO and the gap; T > 0: the thermal term sets the window
    let margin = if t_occ > 0.0 {
        0.5 * params.m
    } else {
        1.5 * params.m + 2.0 * PI / params.length
    };
    // stagnation stop: the exact T = 0 occupations cannot converge through a
    // level crossing at the Fermi level (charge sloshing); give up when the
    // running minimum of the residual has not improved for STAGNATION_ITERATIONS
    let mut best_residual = f64::INFINITY;
    let mut best_iteration = 0usize;
    let mut stats = Stats::default();
    let mut free_levels = FreeLevels::new(params);
    let mut converged = false;
    let mut last: Option<(
        Arc<Potential>,
        Spectrum,
        Densities,
        Filling,
        Energies,
        Window,
    )> = None;
    // The window is chosen in the first iteration and then FROZEN (enlarged
    // only when the edge check fails): a window that followed the running mu
    // estimate moved its edge by tiny amounts every iteration, and at T > 0
    // the edge states (occupation ~ f_cut, multiplicity ~ 200) entering or
    // leaving changed the densities at the 1e-6 level, so the loop could not
    // reach the 1e-10 tolerance (measured at T = m: stagnation, and a full
    // free-level prefetch per iteration because the covered window grew).
    let mut frozen: Option<Window> = None;
    for iteration in 0..params.max_iter {
        let potential = build_potential(params, &densities);
        let mut window = frozen.unwrap_or_else(|| window_for(params, mu_estimate, margin));
        // enlarge the window until the occupation succeeds and the edge is unoccupied
        let mut enlargements = 0usize;
        let (mut spectrum, filling) = loop {
            if enlargements > MAX_WINDOW_ENLARGEMENTS {
                return Err(format!(
                    "solve: window enlarged {enlargements} times without a usable edge (iteration {iteration}, window [{}, {}])",
                    window.eps_lo, window.eps_hi
                ));
            }
            // free levels first (parallel): they classify the branches and
            // warm-start the interacting levels not seen in the previous iteration
            let shift_bound = potential
                .m_eff
                .values
                .iter()
                .map(|m| (m - params.m).abs())
                .fold(0.0, f64::max)
                + potential
                    .v_x
                    .values
                    .iter()
                    .map(|v| v.abs())
                    .fold(0.0, f64::max);
            let before = free_levels.stats();
            free_levels.prefetch(free_levels.widened(window, shift_bound))?;
            let mut warm_now = warm.clone();
            free_levels.fill_warm(&mut warm_now);
            let mut spectrum = compute_spectrum(params, &potential, window, &warm_now)?;
            if verbose {
                eprintln!(
                    "[scf] iteration {iteration} window [{:.6}, {:.6}] shells {} states {} integrations {}",
                    window.eps_lo,
                    window.eps_hi,
                    spectrum.shells_used,
                    spectrum.states.len(),
                    spectrum.stats.integrations
                );
            }
            stats.add(&spectrum.stats);
            free_levels.classify(&mut spectrum, window, shift_bound)?;
            let after = free_levels.stats();
            if verbose {
                eprintln!(
                    "[scf]   classification: shift bound {shift_bound:.3e}, free-level integrations {} (serial fallback {})",
                    after.integrations - before.integrations,
                    free_levels.fallback_integrations()
                );
            }
            stats.add(&after.since(&before));
            match occupy(&mut spectrum, params, mode) {
                Ok(filling) => {
                    let edge_ok = if matches!(mode, Occupation::Constrained(_)) {
                        true
                    } else if t_occ > 0.0 {
                        let thermal = t_occ * log(1.0 / params.f_cut);
                        window.eps_hi >= filling.mu + thermal
                            && window.eps_lo <= filling.mu - thermal
                    } else {
                        // at least one unoccupied particle level above the HOMO inside the window
                        filling.lumo.is_some()
                            && spectrum.states.iter().any(|s| s.branch > 0 && s.f == 0.0)
                    };
                    if edge_ok {
                        break (spectrum, filling);
                    }
                    mu_estimate = filling.mu;
                    let wider = window_for(params, mu_estimate, margin);
                    window = Window {
                        eps_lo: wider.eps_lo.min(window.eps_lo) - 0.5 * params.m,
                        eps_hi: wider.eps_hi.max(window.eps_hi) + 0.5 * params.m,
                    };
                    enlargements += 1;
                    if verbose {
                        eprintln!(
                            "[scf]   edge not usable (mu {}, lumo {:?}, sea_top {}, particle_bottom {}): enlarging to [{:.6}, {:.6}]",
                            filling.mu, filling.lumo, filling.sea_top, filling.particle_bottom, window.eps_lo, window.eps_hi
                        );
                    }
                }
                Err(message) => {
                    if window.eps_hi > 200.0 * params.m.max(1.0) {
                        return Err(format!("solve: window exhausted ({message})"));
                    }
                    window = Window {
                        eps_lo: window.eps_lo * 1.5,
                        eps_hi: window.eps_hi * 1.5,
                    };
                    enlargements += 1;
                    if verbose {
                        eprintln!(
                            "[scf]   occupation failed ({message}): enlarging to [{:.6}, {:.6}]",
                            window.eps_lo, window.eps_hi
                        );
                    }
                }
            }
        };
        frozen = Some(window);
        warm = spectrum
            .states
            .iter()
            .map(|s| (s.key(), if s.s == 1 { s.eps } else { -s.eps }))
            .collect();
        // warm start keys for s = -1 store the eigenvalue of the negated problem (-eps): handled above
        let output = densities_from(&spectrum, params);
        let energy = energies(&spectrum, &output, params, filling.mu);
        mu_estimate = filling.mu;
        // both residuals are relative to the LARGER of the two density scales:
        // in a T = 0 brane-band state S_c << n_c and the scale is max|n_c|; in
        // the hot pair plasma the net n_c is tiny while S_c (particles and
        // antiparticles both count positively) is large, and dividing the
        // eigenvalue-noise floor of S_c (~1e-12 per level, ~75000 levels) by
        // max|n_c| would put it above the tolerance for ever (measured: the
        // S residual stalled at 4e-10 with max|S_c| = 57 max|n_c|)
        let scale_n = output.n_c.iter().map(|v| v.abs()).fold(1e-300, f64::max);
        let scale_s = output.s_c.iter().map(|v| v.abs()).fold(1e-300, f64::max);
        let scale = scale_n.max(scale_s);
        let residual_n = output
            .n_c
            .iter()
            .zip(densities.n_c.iter())
            .map(|(o, i)| (o - i).abs())
            .fold(0.0, f64::max)
            / scale;
        let residual_s = output
            .s_c
            .iter()
            .zip(densities.s_c.iter())
            .map(|(o, i)| (o - i).abs())
            .fold(0.0, f64::max)
            / scale;
        history.push(HistoryRow {
            iteration,
            residual_n,
            residual_s,
            mu: filling.mu,
            energy: energy.total,
            free: energy.free,
            states: spectrum.states.len(),
            integrations: stats.integrations,
        });
        spectrum.stats = stats;
        if verbose {
            eprintln!(
                "[scf] iteration {iteration}: residual_n {residual_n:.3e} residual_S {residual_s:.3e} mu {} E {} N {} max|lambda S|/m {}",
                filling.mu, energy.total, energy.n_total, energy.max_lambda_s_over_m
            );
        }
        let done = residual_n < params.tol && residual_s < params.tol;
        last = Some((
            Arc::clone(&potential),
            spectrum,
            output.clone(),
            filling,
            energy,
            window,
        ));
        if done {
            converged = true;
            break;
        }
        let residual = residual_n.max(residual_s);
        if residual < 0.5 * best_residual {
            best_residual = residual;
            best_iteration = iteration;
        }
        if iteration >= best_iteration + params.stagnation_iterations {
            if verbose {
                eprintln!("[scf] stagnation: no residual improvement by a factor 2 since iteration {best_iteration}; stopping");
            }
            break;
        }
        // mix
        let flat_in: Vec<f64> = densities
            .n_c
            .iter()
            .chain(densities.s_c.iter())
            .copied()
            .collect();
        let flat_out: Vec<f64> = output
            .n_c
            .iter()
            .chain(output.s_c.iter())
            .copied()
            .collect();
        let next = mixer.step(&flat_in, &flat_out);
        densities = Densities {
            n_c: next[..n].to_vec(),
            s_c: next[n..].to_vec(),
        };
    }
    let (potential, spectrum, output, filling, energy, window) =
        last.ok_or_else(|| "solve: no iteration ran".to_string())?;
    let iterations = history.len();
    Ok(Solution {
        params: params.clone(),
        potential,
        spectrum,
        densities: output,
        filling,
        energies: energy,
        window,
        history,
        converged,
        iterations,
        stats,
    })
}

/// Delta-SCF: promote one particle from the HOMO group to the LUMO group of
/// a converged T = 0 solution and re-converge with fixed occupations.
pub fn delta_scf(ground: &Solution) -> Result<Solution, String> {
    let homo = ground
        .filling
        .homo
        .ok_or_else(|| "delta_scf: no HOMO".to_string())?;
    let lumo = ground
        .filling
        .lumo
        .ok_or_else(|| "delta_scf: no LUMO".to_string())?;
    if homo.0 == lumo.0 {
        return Err("delta_scf: HOMO and LUMO coincide (fractional shell)".to_string());
    }
    // occupations by key; groups: all states with eps equal to HOMO / LUMO eps
    let mut map: Vec<(Key, f64)> = Vec::new();
    let homo_group: Vec<&State> = ground
        .spectrum
        .states
        .iter()
        .filter(|s| (s.eps - homo.1).abs() <= 1e-9 * homo.1.abs().max(1.0) && s.branch > 0)
        .collect();
    let lumo_group: Vec<&State> = ground
        .spectrum
        .states
        .iter()
        .filter(|s| (s.eps - lumo.1).abs() <= 1e-9 * lumo.1.abs().max(1.0) && s.branch > 0)
        .collect();
    let homo_mult: f64 = homo_group.iter().map(|s| s.mult).sum();
    let lumo_mult: f64 = lumo_group.iter().map(|s| s.mult).sum();
    let homo_keys: Vec<Key> = homo_group.iter().map(|s| s.key()).collect();
    let lumo_keys: Vec<Key> = lumo_group.iter().map(|s| s.key()).collect();
    for st in ground
        .spectrum
        .states
        .iter()
        .filter(|s| s.branch > 0 && (s.f > 0.0 || lumo_keys.contains(&s.key())))
    {
        let key = st.key();
        let f = if homo_keys.contains(&key) {
            st.f - 1.0 / homo_mult
        } else if lumo_keys.contains(&key) {
            st.f + 1.0 / lumo_mult
        } else {
            st.f
        };
        map.push((key, f));
    }
    let mode = Occupation::Constrained(map);
    let mut params = ground.params.clone();
    params.temperature = 0.0;
    solve(&params, &mode, Some(&ground.densities), ground.filling.mu)
}

/// Heat capacity at constant N with the Kohn-Sham spectrum and potentials
/// held fixed (the exact derivative of the Fermi-Dirac occupations):
///
/// ```text
/// df_i/dT|_N = f_i (1 - f_i) [ (eps_i - mu)/T^2 + mu'/T ],
/// mu' = -(1/T) sum mult f(1-f)(eps - mu) / sum mult f(1-f),
/// C_V^(0) = sum mult (df_i/dT) <h_0>_i,   <h_0>_i = eps_i - <Delta H>_i,
/// <Delta H>_i = int [ (M_eff - m)(-2 s a b) + v_x (a^2 + b^2) ] dy,
/// C_V^(S) = T dS_ent/dT = sum mult (df_i/dT) (eps_i - mu).
/// ```
///
/// (`dw/dT = df/dT` on both branches; the double-counting term changes by
/// `sum mult dw <Delta H>` at fixed potentials.)  For lambda = 0 the
/// potentials do not depend on T, so `C_V^(0)` is the EXACT heat capacity
/// and `C_V^(0) = C_V^(S)` (N conservation); for lambda != 0 it neglects the
/// self-consistent response of the potentials, which the finite-difference
/// `C_V` of `runs.rs` includes where it is computed.
#[derive(Clone, Copy, Debug, Default, PartialEq)]
pub struct HeatCapacity {
    pub from_energy: f64,
    pub from_entropy: f64,
    pub dmu_dt: f64,
}

pub fn heat_capacity_fixed_spectrum(solution: &Solution) -> Option<HeatCapacity> {
    let params = &solution.params;
    let t = params.occupation_temperature();
    if t <= 0.0 {
        return None;
    }
    let mu = solution.filling.mu;
    let dy = params.dy();
    let m_eff = &solution.potential.m_eff.values;
    let v_x = &solution.potential.v_x.values;
    let mut a_sum = 0.0;
    let mut b_sum = 0.0;
    for st in &solution.spectrum.states {
        let g = st.f * (1.0 - st.f);
        a_sum += st.mult * g;
        b_sum += st.mult * g * (st.eps - mu);
    }
    let dmu_dt = if a_sum > 0.0 {
        -b_sum / (a_sum * t)
    } else {
        0.0
    };
    let mut from_energy = 0.0;
    let mut from_entropy = 0.0;
    for st in &solution.spectrum.states {
        let g = st.f * (1.0 - st.f);
        if g == 0.0 {
            continue;
        }
        let dfdt = g * ((st.eps - mu) / (t * t) + dmu_dt / t);
        let s = st.s as f64;
        let integrand: Vec<f64> = st
            .level
            .a
            .iter()
            .zip(st.level.b.iter())
            .zip(m_eff.iter().zip(v_x.iter()))
            .map(|((a, b), (m, v))| (m - params.m) * (-2.0 * s * a * b) + v * (a * a + b * b))
            .collect();
        let delta_h = simpson(dy, &integrand);
        from_energy += st.mult * dfdt * (st.eps - delta_h);
        from_entropy += st.mult * dfdt * (st.eps - mu);
    }
    Some(HeatCapacity {
        from_energy,
        from_entropy,
        dmu_dt,
    })
}

/// Total density integral (N from the profiles, Simpson) as a consistency check.
pub fn particle_number_from_density(params: &Params, densities: &Densities) -> f64 {
    params.volume() * simpson(params.dy(), &densities.n_c)
}

/// Standard parameter set (H = 1).
pub fn standard_params(
    m: f64,
    length: f64,
    lambda_hat: f64,
    temperature: f64,
    n_particles: f64,
) -> Params {
    Params {
        h: 1.0,
        m,
        a4: 0.0,
        length,
        grid_n: 301,
        delta_k_over_m: 0.25,
        lambda_hat,
        temperature,
        smearing: 0.0,
        n_particles,
        f_cut: 1.0e-8,
        shell_cap: 4096,
        mix_beta: 0.4,
        mix_history: 6,
        tol: 1.0e-10,
        max_iter: 80,
        stagnation_iterations: STAGNATION_ITERATIONS,
        fallback_stage: 0,
        tolerances: crate::shooting::DEFAULT_TOLERANCES,
    }
}

/// Closed-shell particle numbers of a non-interacting spectrum (cumulative
/// multiplicities at the ends of degenerate groups of eps >= 0 states).
pub fn closed_shell_numbers(spectrum: &Spectrum, limit: f64) -> Vec<(f64, f64)> {
    // a non-interacting spectrum: the branch is the sign of eps
    let spectrum = {
        let mut s = spectrum.clone();
        for st in s.states.iter_mut() {
            st.branch = if st.eps >= 0.0 { 1 } else { -1 };
        }
        s
    };
    let spectrum = &spectrum;
    let mut out = Vec::new();
    let mut total = 0.0;
    let states: Vec<&State> = spectrum.states.iter().filter(|s| s.branch > 0).collect();
    let mut i = 0;
    while i < states.len() {
        let e = states[i].eps;
        let mut j = i;
        while j < states.len() && (states[j].eps - e).abs() <= 1e-9 * e.abs().max(1.0) {
            total += states[j].mult;
            j += 1;
        }
        out.push((total, e));
        if total > limit {
            break;
        }
        i = j;
    }
    out
}

pub fn exp_factor(h: f64, y: f64) -> f64 {
    exp(6.0 * h * y)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn shell_multiplicities_are_lattice_counts() {
        let list = shells(0.25, 6);
        let expected = [(0, 1), (1, 6), (2, 12), (3, 8), (4, 6), (5, 24), (6, 24)];
        assert_eq!(list.len(), expected.len());
        for (shell, (n2, g)) in list.iter().zip(expected.iter()) {
            assert_eq!(shell.n2, *n2);
            assert_eq!(shell.multiplicity, *g);
            assert!((shell.k - 0.25 * (*n2 as f64).sqrt()).abs() < 1e-15);
        }
    }

    #[test]
    fn anderson_solves_a_linear_fixed_point() {
        // x = A x + c with spectral radius < 1: Anderson converges fast
        let a = [[0.5, 0.2], [0.1, 0.4]];
        let c = [1.0, 2.0];
        let f = |x: &[f64]| {
            vec![
                a[0][0] * x[0] + a[0][1] * x[1] + c[0],
                a[1][0] * x[0] + a[1][1] * x[1] + c[1],
            ]
        };
        let mut mixer = Anderson::new(0.5, 4);
        let mut x = vec![0.0, 0.0];
        for _ in 0..12 {
            let out = f(&x);
            x = mixer.step(&x, &out);
        }
        let out = f(&x);
        assert!(
            (out[0] - x[0]).abs() < 1e-10 && (out[1] - x[1]).abs() < 1e-10,
            "{x:?}"
        );
    }

    #[test]
    fn noninteracting_scf_reproduces_the_free_fill() {
        // lambda = 0, N = 8: the eight brane zero modes, E = 0, converged in 2 iterations
        let params = standard_params(1.0, 3.0, 0.0, 0.0, 8.0);
        let solution = solve(&params, &Occupation::Zero, None, 0.0).unwrap();
        assert!(solution.converged);
        assert!(solution.iterations <= 3, "{}", solution.iterations);
        assert!(
            solution.energies.total.abs() < 1e-8,
            "{}",
            solution.energies.total
        );
        assert!((solution.energies.n_total - 8.0).abs() < 1e-12);
        assert!((particle_number_from_density(&params, &solution.densities) - 8.0).abs() < 1e-6);
        // occupied: exactly the k = 0, parity +, index 0 states of both block types
        let occupied: Vec<&State> = solution
            .spectrum
            .states
            .iter()
            .filter(|s| s.weight > 0.0)
            .collect();
        assert_eq!(occupied.len(), 2);
        assert!(occupied
            .iter()
            .all(|s| s.n2 == 0 && s.parity == 1 && s.index == 0 && s.eps.abs() < 1e-9));
        // gap to the next level is positive
        assert!(solution.gap().unwrap() > 0.1);
        assert!(solution
            .spectrum
            .states
            .iter()
            .all(|s| s.branch == if s.eps_free >= 0.0 { 1 } else { -1 }));
        // scalar density of the zero modes vanishes
        assert!(solution.densities.s_c.iter().all(|s| s.abs() < 1e-12));
    }

    #[test]
    fn asymmetric_window_keeps_the_mirror_states() {
        // Regression: with v_x = 0 the s = -1 states are mirrored from the
        // s = +1 levels; a narrow asymmetric window [-1, 3.2] must still
        // contain every state that the symmetric window [-3.2, 3.2] finds
        // inside [-1, 3.2], in particular the brane band eps = +ck of the
        // shells with ck > 1 (n2 = 8: eps = 1.0847 at L = 3).
        let mut params = standard_params(1.0, 3.0, 0.0, 0.0, 8.0);
        params.shell_cap = 9;
        let potential = build_potential(&params, &Densities::zero(params.grid_n));
        let narrow = compute_spectrum(
            &params,
            &potential,
            Window {
                eps_lo: -1.0,
                eps_hi: 3.2,
            },
            &Default::default(),
        )
        .unwrap();
        let wide = compute_spectrum(
            &params,
            &potential,
            Window {
                eps_lo: -3.2,
                eps_hi: 3.2,
            },
            &Default::default(),
        )
        .unwrap();
        let inside: Vec<&State> = wide
            .states
            .iter()
            .filter(|s| s.eps >= -1.0 && s.eps <= 3.2)
            .collect();
        assert_eq!(narrow.states.len(), inside.len());
        for (a, b) in narrow.states.iter().zip(inside.iter()) {
            assert_eq!(a.key(), b.key());
            assert!((a.eps - b.eps).abs() < 1e-9, "{} vs {}", a.eps, b.eps);
        }
        let band = narrow
            .states
            .iter()
            .find(|s| s.n2 == 8 && s.parity == 1 && s.s == -1 && s.index == 0)
            .expect("n2 = 8 brane-band state present");
        assert!((band.eps - 1.0847).abs() < 1e-3, "{}", band.eps);
        // the closed shells of the free spectrum continue through the brane bands
        let shells = closed_shell_numbers(&narrow, 1300.0);
        let numbers: Vec<f64> = shells.iter().map(|(n, _)| *n).collect();
        assert!(
            numbers.contains(&376.0) && numbers.contains(&496.0),
            "{numbers:?}"
        );
    }

    #[test]
    fn free_window_widening_is_quantised_and_capped() {
        let window = Window {
            eps_lo: -2.0,
            eps_hi: 5.0,
        };
        let width = |w: Window| (w.eps_hi - window.eps_hi, window.eps_lo - w.eps_lo);
        let close = |a: (f64, f64), b: f64| (a.0 - b).abs() < 1e-5 && (a.1 - b).abs() < 1e-5;
        // non-interacting solve: no widening beyond the 1e-6 m guard
        let free = FreeLevels::new(&standard_params(2.0, 3.0, 0.0, 0.0, 8.0));
        assert!(close(width(free.widened(window, 0.0)), 0.0));
        // interacting: at least one quantum (0.25 m = 0.5 here), rounded up, capped at 3 m
        let lev = FreeLevels::new(&standard_params(2.0, 3.0, 0.01, 0.0, 8.0));
        assert!(close(width(lev.widened(window, 0.0)), 0.5));
        assert!(close(width(lev.widened(window, 0.3)), 0.5));
        assert!(close(width(lev.widened(window, 0.51)), 1.0));
        assert!(close(width(lev.widened(window, 0.7)), 1.0));
        assert!(close(width(lev.widened(window, 100.0)), 6.0));
    }

    #[test]
    #[ignore]
    fn probe_methods() {
        let mut reference: Vec<Vec<f64>> = Vec::new();
        for (label, tol, adams) in [
            (
                "bdf 1e-12",
                Tolerances {
                    rtol: 1e-12,
                    atol: 1e-14,
                    max_step: 0.05,
                },
                false,
            ),
            (
                "adams 1e-12",
                Tolerances {
                    rtol: 1e-12,
                    atol: 1e-14,
                    max_step: 0.05,
                },
                true,
            ),
            (
                "adams 1e-12 maxstep 0.5",
                Tolerances {
                    rtol: 1e-12,
                    atol: 1e-14,
                    max_step: 0.5,
                },
                true,
            ),
            (
                "adams 1e-11",
                Tolerances {
                    rtol: 1e-11,
                    atol: 1e-13,
                    max_step: 0.05,
                },
                true,
            ),
        ] {
            for (i, k) in [0.5, 3.0, 8.0].iter().enumerate() {
                let start = std::time::Instant::now();
                let pot = Arc::new(Potential::free(1.0, 0.0, 3.0, 1.0, 301));
                let mut sh = Shooter::new(pot, tol);
                sh.adams_theta = adams;
                let levels = sh.levels(*k, 1, -12.0, 12.0, &[]).unwrap();
                let eps: Vec<f64> = levels.iter().map(|l| l.eps).collect();
                let worst = if reference.len() > i {
                    eps.iter()
                        .zip(reference[i].iter())
                        .map(|(a, b)| (a - b).abs())
                        .fold(0.0, f64::max)
                } else {
                    reference.push(eps.clone());
                    0.0
                };
                println!("{label} k={k}: levels={} integrations={} steps={} time={:?} max|deps| vs first={worst:e} matching={:e}", levels.len(), sh.stats.integrations, sh.stats.steps, start.elapsed(), levels.iter().map(|l| l.matching_residual).fold(0.0, f64::max));
            }
        }
    }

    #[test]
    #[ignore]
    fn probe_timing() {
        let start = std::time::Instant::now();
        let mut params = standard_params(1.0, 3.0, 0.0, 1.0, 8.0);
        params.max_iter = 1;
        let solution = solve(&params, &Occupation::Thermal, None, 0.0).unwrap();
        println!(
            "T=1.0 L=3 N=8: shells_used={} states={} integrations={} steps={} window=({}, {}) mu={} time={:?}",
            solution.spectrum.shells_used,
            solution.spectrum.states.len(),
            solution.stats.integrations,
            solution.stats.steps,
            solution.window.eps_lo,
            solution.window.eps_hi,
            solution.filling.mu,
            start.elapsed()
        );
        let by_shell: Vec<(i64, usize)> = {
            let mut v: Vec<(i64, usize)> = Vec::new();
            for s in &solution.spectrum.states {
                if let Some(last) = v.last_mut() {
                    if last.0 == s.n2 {
                        last.1 += 1;
                        continue;
                    }
                }
                v.push((s.n2, 1));
            }
            v
        };
        println!("states per shell (n2, count): {by_shell:?}");
    }

    #[test]
    fn repeat_run_is_byte_identical() {
        // two independent solves (parallel shells) give identical bytes
        let params = standard_params(1.0, 2.0, 0.05, 0.0, 32.0);
        let render = |s: &Solution| -> String {
            let mut text = String::new();
            for st in &s.spectrum.states {
                text.push_str(&format!(
                    "{} {} {} {} {} {}
",
                    st.n2,
                    st.parity,
                    st.s,
                    st.index,
                    crate::output::fmt17(st.eps),
                    crate::output::fmt17(st.weight)
                ));
            }
            for (a, b) in s.densities.n_c.iter().zip(s.densities.s_c.iter()) {
                text.push_str(&format!(
                    "{} {}
",
                    crate::output::fmt17(*a),
                    crate::output::fmt17(*b)
                ));
            }
            text.push_str(&crate::output::fmt17(s.energies.total));
            text
        };
        let first = solve(&params, &Occupation::Zero, None, 0.0).unwrap();
        let second = solve(&params, &Occupation::Zero, None, 0.0).unwrap();
        assert!(first.converged && second.converged);
        assert_eq!(render(&first), render(&second));
        assert_eq!(first.iterations, second.iterations);
    }

    #[test]
    fn noninteracting_thermal_fill_conserves_n() {
        let params = standard_params(1.0, 2.0, 0.0, 0.3, 8.0);
        let solution = solve(&params, &Occupation::Thermal, None, 0.0).unwrap();
        assert!(solution.converged);
        assert!(
            (solution.energies.n_total - 8.0).abs() < 1e-9,
            "{}",
            solution.energies.n_total
        );
        assert!(solution.energies.entropy > 0.0);
        assert!(solution.energies.free < solution.energies.total);
    }
}
