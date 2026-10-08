"""Unit tests for the Stage-4 reference solver and checker (numpy + stdlib).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_kohn_sham_reference.py" -v
The tests call the solver functions directly on small grids, include
negative controls (a wrong closed form is detected, a broken identity is
detected, a perturbed Rust eigenvalue is detected) and write only into
tempfile directories.  They do not need the committed artifacts.
"""

import contextlib
import io
import json
import math
import os
import re
import sys
import tempfile
import types
import unittest

# one BLAS thread (the reference solver's setting; small dense eigenproblems):
# must be set before numpy is imported
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import ks_reference_solver as K  # noqa: E402
import check_dirac16complex_kohn_sham as C  # noqa: E402


class ParticleHoleRuleTests(unittest.TestCase):
    """T = 0 particle-hole pairs (exact occupations, or a run converged with
    occupation smearing such as the N = 1016, -lambda_hat_2 level crossing):
    holes hold more than 1e-12 of a particle, particles more than 1e-12 of a
    vacancy, so the Fermi-Dirac tails of a smeared run (f ~ 1e-185) are
    neither; physical T > 0 keeps the thermal rule (holes f >= 1/2,
    particles f < 1/2).  The Rust crate uses the same floor
    (runs.rs PH_OCCUPATION_FLOOR)."""

    @staticmethod
    def _run(T, smearing, fs):
        # A: eps 0.5, mult 8; open-shell pair B1/B2: eps 0.7 and 0.7 + 1e-12,
        # mult 4 each (degenerate within DEGENERACY_TOL); C: eps 0.9, mult 4.
        # N = 12: A full, the 8-fold B group half filled (an open shell).
        specs = [(1, 2.0, 0.5, 1, 0), (0, 1.0, 0.7, 1, 1), (0, 1.0, 0.7 + 1e-12, -1, 1), (2, 1.0, 0.9, 1, 0)]
        states = []
        for (q, r3, eps, typ, idx), f in zip(specs, fs):
            st = K.State(q, r3, 0.25 * math.sqrt(q), typ, idx, eps, None, None, None, branch=1)
            st.f = f
            st.w = f
            states.append(st)
        run = types.SimpleNamespace()
        run.params = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=T, N=12.0, parity=1, N0=24, smearing=smearing)
        run.levels = [{"spectrum": types.SimpleNamespace(states=states)}]
        run.state_eps = {}
        return run, states

    def test_smeared_zero_temperature_run_uses_the_occupation_floor(self):
        smeared = [0.978, 0.526, 0.526, 1e-185]
        run, states = self._run(0.0, 1e-3, smeared)
        pairs = K.particle_hole_list(run)
        self.assertLess(pairs[0]["excitation"], 1e-9)          # inside the fractionally occupied level
        self.assertTrue(all(abs(p["epsHole"] - 0.9) > 1e-6 for p in pairs))   # f = 1e-185 is no hole
        self.assertEqual([st.f for st in states], smeared)     # the run's own occupations are untouched
        # negative control: the smeared f taken as thermal would give 0.2 (B -> C)
        run_t, _ = self._run(1e-3, 0.0, smeared)
        self.assertAlmostEqual(K.particle_hole_list(run_t)[0]["excitation"], 0.2, places=9)

    def test_exact_zero_temperature_run_is_unchanged(self):
        run, _ = self._run(0.0, 0.0, [1.0, 0.5, 0.5, 0.0])
        pairs = K.particle_hole_list(run)
        self.assertLess(pairs[0]["excitation"], 1e-9)
        self.assertTrue(all(abs(p["epsHole"] - 0.9) > 1e-6 for p in pairs))


class GridUncertaintyTests(unittest.TestCase):
    """The checker's Rust grid uncertainty (STAGE4_SPEC E4.14(a)): a _g<n> run and the run of its base label
    in the same subcommand form a refinement family; every member gets its OWN estimated grid error, the
    301-point member |X(601) - X(301)|, the 601-point member |X(601) - X(301)| / (2^p - 1) (p measured from
    three grids, else the design order 2); runs without a partner get nothing."""

    def test_refinement_pairs(self):
        runs = [
            {"sub": "excited", "label": "m1_L3_N1016_lamm2_T0", "run": None,
             "record": {"deltaScf": 0.0436184, "E0": 1126.858, "ksGap": 0.0412551}},
            {"sub": "excited", "label": "m1_L3_N1016_lamm2_T0_g601", "run": None,
             "record": {"deltaScf": 0.0436210, "E0": 1126.8581, "ksGap": 0.0412551}},
            {"sub": "scf", "label": "m1_L3_N1016_lamm2_T0_g601", "run": {"energy": 1.0}, "record": None},
            {"sub": "scf", "label": "m1_L3_N8_lam0_T0", "run": {"energy": 0.0}, "record": None},
        ]
        gu = C.rust_grid_uncertainties(runs)
        self.assertEqual(set(gu), {("excited", "m1_L3_N1016_lamm2_T0"),         # the scf _g601 run has no base
                                   ("excited", "m1_L3_N1016_lamm2_T0_g601")})
        coarse = gu[("excited", "m1_L3_N1016_lamm2_T0")]
        self.assertEqual(coarse["gridPoints"], 301)
        unc = coarse["values"]
        self.assertAlmostEqual(unc["deltaScf"], 2.6e-6, places=12)
        self.assertAlmostEqual(unc["E0"], 1e-4, places=9)
        self.assertEqual(unc["ksGap"], 0.0)
        self.assertNotIn("mu", unc)
        fine = gu[("excited", "m1_L3_N1016_lamm2_T0_g601")]
        self.assertEqual(fine["gridPoints"], 601)
        self.assertAlmostEqual(fine["values"]["deltaScf"], 2.6e-6 / 3.0, places=12)   # design order 2: / (2^2 - 1)
        self.assertAlmostEqual(fine["values"]["E0"], 1e-4 / 3.0, places=9)
        self.assertEqual(fine["orders"]["deltaScf"], C.RUST_GRID_DESIGN_ORDER)

    def test_member_errors_with_a_measured_order(self):
        # three grids converging with order 4: X = 1 + c h^4, h = 1/300, 1/600, 1/1200
        values = [(n, 1.0 + 1e3 * (1.0 / (n - 1)) ** 4) for n in (301, 601, 1201)]
        (u0, p0, how0), (u1, p1, how1), (u2, p2, how2) = C.member_grid_errors(values)
        self.assertEqual((p0, how0, how1, how2), (None, "coarsest", "measured", "measured"))
        self.assertAlmostEqual(p1, 4.0, places=6)
        self.assertAlmostEqual(p2, 4.0, places=6)
        self.assertAlmostEqual(u0, abs(values[1][1] - values[0][1]), delta=1e-18)
        exact601, exact1201 = values[1][1] - 1.0, values[2][1] - 1.0        # the true errors of the members
        self.assertAlmostEqual(u1, exact601, delta=1e-6 * exact601)
        self.assertAlmostEqual(u2, exact1201, delta=1e-6 * exact1201)
        # a non-converging triple (order 0): the finer member's term is capped at the coarser member's
        (u0, _, _), (u1, _, _), (u2, _, _) = C.member_grid_errors([(301, 1.0), (601, 1.0 + 1e-6), (1201, 1.0)])
        self.assertEqual(u1, u0)
        self.assertEqual(u2, u1)
        # two grids: the design order
        (u0, _, _), (u1, p1, how1) = C.member_grid_errors([(301, 1.0), (601, 1.0 + 3e-6)])
        self.assertEqual((p1, how1), (C.RUST_GRID_DESIGN_ORDER, "design"))
        self.assertAlmostEqual(u1, u0 / 3.0, delta=1e-18)


class AlgebraTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gam, cls.charge, cls.chirality = K.load_fixture()

    def test_clifford_and_block_reduction(self):
        self.assertTrue(K.clifford_ok(self.gam))
        red = K.block_reduction(self.gam, self.charge)
        self.assertLess(red["maxDeviationFromClosedForm"], 1e-12)
        self.assertLess(red["unitarityDeviation"], 1e-12)
        self.assertEqual(red["algebraDimensionOverR"], 8)
        self.assertEqual(sorted(b["s"] for b in red["blocks"]), [-1] * 4 + [1] * 4)
        self.assertTrue(all(b["b_equals_J_times_iK1"] for b in red["blocks"]))
        self.assertTrue(all(red["facts"].values()))

    def test_block_reduction_detects_wrong_gammas(self):
        gam = [g.copy() for g in self.gam]
        gam[1] = gam[1] * 2.0   # breaks the Clifford relation and the block forms
        self.assertFalse(K.clifford_ok(gam))

    def test_exchange_trace_identity_and_negative_control(self):
        self.assertLess(K.exchange_trace_identity(self.gam, self.charge), 1e-12)
        A = -1j * self.gam[4]
        h = -1j * 1.0 * self.gam[4] - 0.3 * (self.gam[4] @ self.gam[1])
        E = math.sqrt(1.0 + 0.09)
        P = (np.eye(16) + h / E) / 2
        tr = np.trace(A @ P @ A @ P).real
        self.assertAlmostEqual(tr, 4.0 * (1.0 + (1.0 - 0.09) / (E * E)), places=12)
        self.assertNotAlmostEqual(tr, 4.0 * (1.0 + (4.0 - 0.09) / (E * E)), places=3)


class GasTests(unittest.TestCase):

    def test_closed_forms_and_inversion(self):
        report = K.gas_selfcheck()
        self.assertLess(report["T0_n_closed_form"], 1e-12)
        self.assertLess(report["dn_dmu_fd"], 1e-6)
        self.assertLess(report["mu_of_n_roundtrip"], 1e-10)
        n, S, _, _ = K.gas_densities(1.5, 0.0, 1.0)
        self.assertGreater(S, 0.0)
        self.assertLess(S, n)   # S/n = <m/E> < 1
        self.assertLess(K.exchange_energy_density(0.3, 0.2, 1.0), 0.0)
        self.assertEqual(K.exchange_energy_density(0.3, 0.2, 1.0), K.exchange_energy_density(-0.3, -0.2, 1.0))

    def test_lda_n_potential_reduces_to_quadratic_slope(self):
        ex, vx = K.lda_n_potential(0.05, 0.2, 1.0, 2.0)
        self.assertLess(ex, 0.0)
        self.assertLess(vx, 0.0)


class DiscretisationTests(unittest.TestCase):

    def test_analytic_box_spectra_all_boundary_pairs(self):
        L, M = 3.0, 1.0
        for tip in ("g0", "f0"):
            for parity in (1, -1):
                brane = "g0" if parity > 0 else "f0"
                exact = K.analytic_box(M, L, brane, tip, count=3)
                levels = []
                for lvl in range(3):
                    grid = K.Grid(L, 50 * 2 ** lvl)
                    sh = K.solve_shell(grid, np.full(grid.N + 1, M), np.zeros(grid.N + 1), 0.0, 0.0, parity, tip, False)
                    e = sh["eps"][sh["type"] == 1]
                    levels.append(np.sort(e[e >= -K.ZERO_MODE_TOL])[:len(exact)])
                ext = K.extrapolate3(*levels)
                self.assertLess(float(np.max(np.abs(ext - np.array(exact)))), 5e-7, (tip, parity))
                self.assertEqual(brane == tip, abs(ext[0]) < 1e-9)

    def test_discrete_hellmann_feynman_and_norm(self):
        grid = K.Grid(3.0, 80)
        Mn = 1.0 + 0.2 * np.exp(grid.y)
        vn = 0.1 * np.sin(grid.y)
        sh = K.solve_shell(grid, Mn, vn, 0.7, 0.0, 1, "g0", True)
        i = int(np.argmin(np.abs(sh["eps"] - 2.0)))
        self.assertAlmostEqual(grid.integrate(sh["n"][i]), 1.0, places=12)
        d = 1e-6
        ep = K.solve_shell(grid, Mn + d, vn, 0.7, 0.0, 1, "g0", True)["eps"][i]
        em = K.solve_shell(grid, Mn - d, vn, 0.7, 0.0, 1, "g0", True)["eps"][i]
        self.assertAlmostEqual((ep - em) / (2 * d), grid.integrate(sh["s"][i]), places=4)
        direct = K.eigenpairs(grid, Mn, 0.7 * K.kappa_of(grid.y, 0.0), 0.7 * K.kappa_of(grid.yh, 0.0), -vn, 1, "g0")[0]
        minus = np.sort(sh["eps"][sh["type"] == -1])
        self.assertLess(float(np.max(np.abs(minus - np.sort(-direct)))), 1e-12)

    def test_no_doubler(self):
        grid = K.Grid(3.0, 40)
        hs, _, _ = K.build_hamiltonian(grid, np.zeros(41), np.zeros(41), np.zeros(40), np.zeros(41), 1, "g0")
        ev = np.abs(np.linalg.eigvalsh(hs))
        self.assertLessEqual(ev.max(), 2.0 / grid.h * (1 + 1e-9))

    def test_lattice_shells(self):
        shells = dict(K.lattice_shells(12))
        self.assertEqual(shells[0], 1)
        self.assertEqual(shells[1], 6)
        self.assertEqual(shells[2], 12)
        self.assertEqual(shells[3], 8)
        self.assertNotIn(7, shells)      # 7 is not a sum of three squares
        self.assertEqual(shells[9], 30)
        # brute force for q <= 50
        counts = {}
        for a in range(-8, 9):
            for b in range(-8, 9):
                for c in range(-8, 9):
                    q = a * a + b * b + c * c
                    if q <= 50:
                        counts[q] = counts.get(q, 0) + 1
        self.assertEqual(dict(K.lattice_shells(50)), counts)
        self.assertEqual([q for q, _ in K.shells_up_to_k(1.0, 0.25)], [q for q in sorted(counts) if q <= 17])


class ScfTests(unittest.TestCase):

    def test_free_ground_state_zero_modes_and_gap(self):
        p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.0, N=8.0, parity=1, N0=40)
        grid = K.Grid(3.0, 40)
        res = K.scf(p, grid)
        self.assertTrue(res["converged"])
        self.assertAlmostEqual(res["energies"]["total"], 0.0, places=10)
        self.assertAlmostEqual(res["energies"]["nTotal"], 8.0, places=10)
        self.assertGreater(res["lumo"].eps, 0.4)
        n_c, s_c = res["n_c"], res["s_c"]
        self.assertAlmostEqual(p.volume * grid.integrate(n_c), 8.0, places=9)
        self.assertLess(float(np.max(np.abs(s_c))), 1e-12)   # the zero mode has no scalar density

    def test_interacting_scf_converges_and_energy_functional(self):
        p = K.Params(m=1.0, L=3.0, lambda_hat=0.008, T=0.0, N=32.0, parity=1, N0=32, tol=1e-11)
        grid = K.Grid(3.0, 32)
        res = K.scf(p, grid)
        self.assertTrue(res["converged"])
        en = res["energies"]
        self.assertAlmostEqual(en["total"], en["ksSum"] - en["hartree"] - en["exchange"], places=9)
        self.assertGreater(en["maxLambdaSOverM"], 0.0)

    def test_thermal_occupations_and_entropy(self):
        p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.2, N=8.0, parity=1, N0=24)
        grid = K.Grid(3.0, 24)
        res = K.scf(p, grid)
        self.assertAlmostEqual(res["energies"]["nTotal"], 8.0, places=8)
        self.assertGreater(res["energies"]["entropy"], 0.0)
        self.assertLess(res["energies"]["free"], res["energies"]["total"])

    def test_smearing_fallback_parameters(self):
        """Occupation smearing at T = 0: Fermi-Dirac weights at the smearing,
        entropy reported, F = E (physical T = 0)."""
        p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.0, N=32.0, parity=1, N0=24, smearing=1e-3)
        self.assertEqual(p.occupation_temperature(), 1e-3)
        res = K.scf(p, K.Grid(3.0, 24))
        self.assertEqual(res["mode"], "thermal")
        self.assertAlmostEqual(res["energies"]["nTotal"], 32.0, places=8)
        self.assertEqual(res["energies"]["free"], res["energies"]["total"])
        self.assertGreaterEqual(res["energies"]["entropy"], 0.0)

    def test_constrained_occupation_defaults(self):
        p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.0, N=8.0, parity=1, N0=24)
        grid = K.Grid(3.0, 24)
        res = K.scf(p, grid)
        states = res["spectrum"].states
        occ = {st.key(): st.f for st in states if st.branch > 0 and st.f > 0}
        mu, total = K.occupy_constrained(states, occ)
        self.assertAlmostEqual(total, 8.0, places=10)   # sea states default to filled (weight 0)

    def test_branch_classification_free_sea_convention(self):
        """lambda > 0 pushes the k = 0 zero-mode band below eps = 0; with the
        free-sea (continuity) convention it stays the occupied particle band
        (E0 < 0, mu < 0), with the sign convention it would be swallowed by
        the sea and N = 8 would jump to the next shell (E0 = 8 x 0.43)."""
        grid = K.Grid(3.0, 24)
        lam = 0.0162
        free = K.scf(K.Params(m=1.0, L=3.0, lambda_hat=lam, T=0.0, N=8.0, parity=0, N0=24, sea="free"), grid)
        sign = K.scf(K.Params(m=1.0, L=3.0, lambda_hat=lam, T=0.0, N=8.0, parity=0, N0=24, sea="sign"), grid)
        self.assertTrue(free["converged"] and sign["converged"])
        self.assertLess(free["mu"], 0.0)
        self.assertLess(free["energies"]["total"], 0.0)
        self.assertFalse(free["branchOverlap"])
        occupied = [st for st in free["spectrum"].states if st.w > 0]
        self.assertTrue(all(st.q == 0 and st.branch > 0 and st.eps < 0 for st in occupied))
        self.assertGreater(sign["energies"]["total"], 3.0)
        a = K.scf(K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.0, N=32.0, parity=1, N0=24, sea="free"), grid)
        b = K.scf(K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.0, N=32.0, parity=1, N0=24, sea="sign"), grid)
        self.assertEqual(a["energies"]["total"], b["energies"]["total"])
        ka = sorted((st.key(), st.branch) for st in a["spectrum"].states)
        kb = sorted((st.key(), st.branch) for st in b["spectrum"].states)
        self.assertEqual(ka, kb)

    def test_free_branch_counts_match_sign_of_free_spectrum(self):
        grid = K.Grid(3.0, 30)
        for k in (0.0, 0.7):
            for parity in (1, -1):
                sh = K.solve_shell(grid, np.full(31, 1.0), np.zeros(31), k, 0.0, parity, "g0", False)
                n_neg, n_pos, dim = K.free_branch_counts(grid, 1.0, k, 0.0, parity, "g0")
                plus = sh["eps"][sh["type"] == 1]
                self.assertEqual(dim, len(plus))
                self.assertEqual(n_neg, int(np.sum(plus < -K.ZERO_MODE_TOL)))
                self.assertEqual(n_pos, int(np.sum(plus > K.ZERO_MODE_TOL)))
        n_neg, n_pos, dim = K.free_branch_counts(grid, 1.0, 0.0, 0.0, 1, "g0")
        self.assertEqual(dim - n_neg - n_pos, 1)

    def test_union_parity_equals_lower_sector_for_free_n8(self):
        runs = {}
        for par in (1, 0):
            p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.0, N=8.0, parity=par, N0=24)
            runs[par] = K.scf(p, K.Grid(3.0, 24))
        self.assertAlmostEqual(runs[1]["energies"]["total"], runs[0]["energies"]["total"], places=12)
        self.assertTrue(any(st.parity == -1 for st in runs[0]["spectrum"].states))

    def test_compact_tail_sums_equal_explicit_sums(self):
        """Chebyshev-tail levels carry no profile arrays: the per-block sums of
        `densities` equal the explicit per-level sums of their profiles."""
        p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.3, N=8.0, parity=1, N0=16, exact_shells=4)
        grid = K.Grid(3.0, 16)
        res = K.scf(p, grid)
        states = res["spectrum"].states
        tail = [st for st in states if st.tail is not None]
        self.assertGreater(len(tail), 10)
        n_c, s_c = K.densities(states, p, grid)
        n_x = sum(st.mult * st.w * st.profile("n") for st in states) / p.volume
        s_x = sum(st.mult * st.w * st.profile("s") for st in states) / p.volume
        self.assertLess(float(np.max(np.abs(n_c - n_x))), 1e-13 * float(np.max(np.abs(n_x))))
        self.assertLess(float(np.max(np.abs(s_c - s_x))), 1e-12 * float(np.max(np.abs(s_x))))

    def test_parallel_shell_loop_equals_serial(self):
        """shell_workers changes the execution only: identical states and densities."""
        grid = K.Grid(3.0, 12)
        base = dict(m=1.0, L=3.0, lambda_hat=0.0, T=0.5, N=8.0, parity=0, N0=12, exact_shells=1000000)
        m_eff, v = np.full(13, 1.0), 0.01 * np.sin(grid.y)
        a = K.Spectrum(K.Params(**base), grid, m_eff, v, -6.0, 6.0)
        b = K.Spectrum(K.Params(shell_workers=2, **base), grid, m_eff, v, -6.0, 6.0)
        self.assertEqual([st.key() for st in a.states], [st.key() for st in b.states])
        self.assertEqual([st.eps for st in a.states], [st.eps for st in b.states])
        self.assertTrue(all(np.array_equal(x.n, y.n) and np.array_equal(x.s, y.s) for x, y in zip(a.states, b.states)))
        self.assertEqual(a.shells_exact, b.shells_exact)

    def test_fixed_spectrum_heat_capacity_and_truncation(self):
        """lambda = 0: C_V^(0) = C_V^(S) exactly and equal to the central
        difference to O(delta^2); a window that holds every level truncates
        nothing."""
        grid = K.Grid(3.0, 16)
        T = 0.3
        base = dict(m=1.0, L=3.0, lambda_hat=0.0, N=8.0, parity=1, N0=16)
        res = K.scf(K.Params(T=T, **base), grid)
        hc = K.heat_capacity_fixed_spectrum(res, K.Params(T=T, **base), grid)
        self.assertAlmostEqual(hc["C_V_fixedSpectrum"] / hc["C_V_fixedSpectrumEntropy"], 1.0, places=12)
        d = 0.01 * T
        ep = K.scf(K.Params(T=T + d, **base), grid)["energies"]["total"]
        em = K.scf(K.Params(T=T - d, **base), grid)["energies"]["total"]
        self.assertLess(abs((ep - em) / (2 * d) / hc["C_V_fixedSpectrum"] - 1.0), 2e-3)
        saved = K.RUST_F_CUT
        try:
            K.RUST_F_CUT = 1e-300
            tr = K.rust_window_truncation(res, K.Params(T=T, **base), grid)
        finally:
            K.RUST_F_CUT = saved
        self.assertEqual(tr["levelsOutside"], 0)
        self.assertLess(abs(tr["deltaE"]), 1e-9)
        tr = K.rust_window_truncation(res, K.Params(T=T, **base), grid)
        self.assertGreater(tr["levelsOutside"], 0)
        self.assertLess(tr["deltaE"], 0.0)   # the dropped tail carries positive energy (particles and antiparticles)


class SectorRunTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sector = K.SectorRun(K.Params(m=1.0, L=3.0, lambda_hat=0.005, T=0.0, N=8.0, parity=1, N0=24, levels=3))

    def test_extrapolation_and_emt_identities(self):
        run = self.sector
        self.assertTrue(run.converged)
        self.assertEqual(len(run.levels), 3)
        self.assertLess(abs(run.emt["energyFromRho"] - run.scalars["total"]), 1e-9)
        self.assertLess(run.emt["traceIdentityResidual"], 1e-10)
        cons = run.emt["conservationResidualMaxNormalised"]
        self.assertLess(cons[-1], cons[0])   # second-order decrease with refinement
        self.assertLess(cons[-1], 5e-3)
        self.assertEqual(run.emt["rhoRequired_kappa1"], -21.0)
        e41 = run.emt["E41_sourcingConditions"]
        self.assertFalse(e41["met"])
        self.assertEqual(e41["lambdaSOverMRequired"], -5.0 / 6.0)
        scale = run.coupling_scale
        self.assertAlmostEqual(scale["strengthPerUnitLambdaHat"],
                               max(15.0 / 16.0 * scale["sRef"], scale["nRef"] / 16.0), places=12)
        self.assertLessEqual(float(run.emt["braneLocalisedFraction"] + run.emt["tipLocalisedFraction"]), 1.0 + 1e-12)

    def test_write_run_and_checker_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = K.write_run(self.sector, os.path.join(tmp, "r"), {"excited": {"ksGap": self.sector.gap}})
            self.assertTrue(os.path.exists(os.path.join(tmp, "r", "spectrum.csv")))
            hdr, data = C.read_csv(os.path.join(tmp, "r", "spectrum.csv"))
            self.assertIn("parity", hdr)
            self.assertAlmostEqual(float(np.sum(C.column(hdr, data, "mult") * C.column(hdr, data, "w"))), 8.0, places=9)
            self.assertEqual(doc["params"]["N"], 8.0)
            self.assertEqual(doc["files"], sorted(set(doc["files"])))

    def test_extrapolate3_removes_h2_and_h3(self):
        h = 0.1
        f = lambda hh: 2.0 + 3.0 * hh ** 2 - 5.0 * hh ** 3
        self.assertAlmostEqual(float(K.extrapolate3(f(h), f(h / 2), f(h / 4))), 2.0, places=13)
        g = lambda hh: 1.0 + 0.7 * hh + 0.2 * hh ** 2
        self.assertAlmostEqual(float(K.extrapolate_profile([np.array([g(h)]), np.array([g(h / 2)]), np.array([g(h / 4)])])[0]),
                               1.0, places=13)

    def test_interval_integral_partial_cells(self):
        grid = K.Grid(3.0, 7)                      # -1 is not a node
        vals = 2.0 + 0.5 * grid.y                  # linear: the trapezoid with interpolated ends is exact
        exact = 2.0 * 1.0 + 0.25 * (0.0 - 1.0)
        self.assertAlmostEqual(K.interval_integral(grid, vals, -1.0, 0.0), exact, places=13)


def fake_rust_tree(root, ref_dir, label, perturb=0.0):
    """A Rust-format tree (scf/<label>) built from a reference run directory."""
    with open(os.path.join(ref_dir, label, "run.json"), encoding="utf-8") as handle:
        run = json.load(handle)
    shdr, spec = C.read_csv(os.path.join(ref_dir, label, "spectrum.csv"))
    phdr, prof = C.read_csv(os.path.join(ref_dir, label, "profiles.csv"))
    d = os.path.join(root, "scf", label)
    os.makedirs(d)
    eps = C.column(shdr, spec, "eps_extrapolated").copy()
    eps[len(eps) // 2] += perturb
    rows = np.stack([C.column(shdr, spec, "q"), C.column(shdr, spec, "parity"), C.column(shdr, spec, "type"),
                     C.column(shdr, spec, "index"), eps, C.column(shdr, spec, "branch"), C.column(shdr, spec, "f")],
                    axis=1)
    K.write_csv(os.path.join(d, "levels.csv"), ["n2", "parity", "s", "index", "eps", "branch", "f"], rows)
    names = ["y", "n_c", "S_c", "n_p", "S_p", "M_eff", "v_x", "rho", "p_y", "p_3", "p_t"]
    table = np.stack([C.column(phdr, prof, n) for n in names] + [C.column(phdr, prof, "W6")], axis=1)
    K.write_csv(os.path.join(d, "profiles.csv"), names + ["volume_factor"], table)
    p = run["params"]
    avg = run["emt"]["averages"]
    K.write_json(os.path.join(d, "run.json"), {
        "parameters": {"m": p["m"], "L": p["L"], "N": p["N"], "lambdaHat": p["lambda_hat"], "T": p["T"],
                       "a4_0": 0.0, "deltaKOverM": 0.25, "occupationSmearing": 0.0},
        "converged": True, "energy": run["extrapolated"]["total"], "mu": run["extrapolated"]["mu"],
        "ksGap": run["ksGap"], "nTotal": p["N"],
        "emt": {"rhoAvg": avg["rho"], "pYAvg": avg["p_y"], "p3Avg": avg["p_3"], "pTAvg": avg["p_t"],
                "sPAvg": avg["s_p"], "nPAvg": avg["n_p"], "energyFromRho": run["extrapolated"]["total"],
                "braneFraction_within_1_over_H": run["emt"]["braneLocalisedFraction"],
                "tipFraction_within_1_over_H_of_cutoff": run["emt"]["tipLocalisedFraction"]}})
    K.write_json(os.path.join(root, "scf", "summary.json"),
                 {"verdict": "SUCCESS", "checks": {"x": True}, "files": [label + "/levels.csv"], "runs": []})


class DeltaScfOccupationTests(unittest.TestCase):
    """STAGE4_SPEC E4.14: the constrained occupations of every grid level come from that level's
    own ground state (Rust scf.rs delta_scf: every Rust run is one grid)."""

    def test_level_E1_independent_of_the_finest_level(self):
        """Smearing 0.05 m: grid-dependent fractional occupations (N = 8, L = 3).  The E_1 of a
        grid level must not depend on how many finer levels the run has; the rule before E4.14
        (the finest level's occupations frozen on every level) fails this (6.2e-4)."""
        e1 = {}
        for levels in (2, 3):
            p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.0, N=8.0, N0=12, levels=levels, smearing=0.05,
                         label="t")
            run = K.SectorRun(p, mode="auto")
            fine = run.levels[-1]["spectrum"].states
            self.assertTrue(any(0.0 < st.f < 1.0 for st in fine if st.branch > 0))   # really smeared
            d = K.delta_scf(run)
            self.assertTrue(d["available"])
            self.assertEqual(d["constrainedOccupations"], K.DSCF_OCCUPATIONS)
            e1[levels] = d["levelsE1"]
        for i in range(2):
            self.assertAlmostEqual(e1[2][i], e1[3][i], delta=1e-10)

    def test_integer_occupations_unchanged(self):
        """Exact T = 0 occupations: the same constrained occupations on every level, and no new
        record in run.json (the Stage-4 integer runs stay byte-identical)."""
        p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.0, N=8.0, N0=12, levels=2, label="t")
        d = K.delta_scf(K.SectorRun(p, mode="auto"))
        self.assertTrue(d["available"])
        self.assertEqual((d["homoMultiplicity"], d["lumoMultiplicity"]), (8.0, 24.0))
        self.assertNotIn("constrainedOccupations", d)

    def test_resume_recomputes_a_smeared_run_written_before_the_rule(self):
        """--resume keeps a smeared excited run only if its Delta-SCF records the per-level rule."""
        spec = {"label": "t", "m": 1.0, "L": 3.0, "N": 8.0, "T": 0.0, "N0": 12, "levels": 2, "parity": 0,
                "tip": "g0", "xc": "quadratic", "tasks": ["excited"], "lambda": "lam0", "smearing": 0.05}
        q = K.params_of(spec, 0.0).to_dict()
        doc = {"params": dict(q), "converged": True,
               "excited": {"deltaSCF": {"available": True, "constrainedOccupations": K.DSCF_OCCUPATIONS}}}
        self.assertTrue(K.run_matches(doc, spec, 0.0))
        del doc["excited"]["deltaSCF"]["constrainedOccupations"]
        self.assertFalse(K.run_matches(doc, spec, 0.0))
        integer = dict(spec, smearing=0.0)
        doc["params"] = K.params_of(integer, 0.0).to_dict()
        self.assertTrue(K.run_matches(doc, integer, 0.0))


def add_grid_partner(root, label, shifts):
    """scf/<label>_g601: a copy of scf/<label> whose levels.csv row i carries eps + shifts[i]."""
    import shutil
    src = os.path.join(root, "scf", label)
    dst = src + "_g601"
    shutil.copytree(src, dst)
    hdr, rows = C.read_csv(os.path.join(dst, "levels.csv"))
    arr = np.array(rows, dtype=float)
    col = hdr.index("eps")
    for i, d in shifts.items():
        arr[i, col] += d
    K.write_csv(os.path.join(dst, "levels.csv"), hdr, arr)
    with open(os.path.join(root, "scf", "summary.json"), encoding="utf-8") as handle:
        summary = json.load(handle)
    summary["files"].append(label + "_g601/levels.csv")
    K.write_json(os.path.join(root, "scf", "summary.json"), summary)


class CheckerLevelUncertaintyTests(unittest.TestCase):
    """STAGE4_SPEC E4.14: the OWN estimated Rust y-grid error of a level enters that level's eigenvalue
    tolerance, and only that level's, of that member only (rust_level_grid_uncertainties): the 301-point
    member |eps(601) - eps(301)|, the 601-point member |eps(601) - eps(301)| / (2^p - 1)."""
    LABEL = "m1_L3_N8_lamp1_T0"

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        cls.ref_dir = os.path.join(cls.tmp, "ref")
        spec = {"label": cls.LABEL, "m": 1.0, "L": 3.0, "N": 8.0, "T": 0.0, "N0": 12, "levels": 2,
                "parity": 0, "tip": "g0", "xc": "quadratic", "tasks": [], "lambda": "lamp1"}
        with contextlib.redirect_stdout(io.StringIO()):
            K.execute_run(spec, 0.01, cls.ref_dir, lambda msg: None)

    @classmethod
    def tearDownClass(cls):
        import shutil
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def check(self, name, perturb, shifts=None):
        """The level in the middle of levels.csv is perturbed by perturb (fake_rust_tree); shifts
        ({"mid" | "other": d}) build a _g601 partner, None = no partner."""
        rust = os.path.join(self.tmp, name)
        fake_rust_tree(rust, self.ref_dir, self.LABEL, perturb)
        if shifts is not None:
            hdr, rows = C.read_csv(os.path.join(rust, "scf", self.LABEL, "levels.csv"))
            mid = len(rows) // 2
            add_grid_partner(rust, self.LABEL, {(mid if k == "mid" else mid + 1): v for k, v in shifts.items()})
        reg = C.Registry()
        runs = C.rust_runs(rust, C.rust_summaries(rust))
        C.compare_canonical(reg, self.ref_dir, runs)
        return reg

    def test_no_partner_fixed_tolerance(self):
        # 3e-6 on a level near eps = 2.2 m exceeds the fixed tolerance 1e-6 |eps|
        reg = self.check("nopartner", 3e-6)
        self.assertFalse(reg.checks["canonical_eigenvalues"], reg.measurements["canonical_eigenvalues_detail"])

    def test_measured_grid_uncertainty_of_the_level(self):
        # the partner moves the same level back by 3e-6: |eps(601) - eps(301)| = 3e-6 enters its tolerance
        reg = self.check("same", 3e-6, {"mid": -3e-6})
        self.assertTrue(reg.checks["canonical_eigenvalues"], reg.measurements["canonical_eigenvalues_detail"])
        rec = reg.comparisons["canonical_scf_" + self.LABEL]["detail"]["rustLevelGridUncertainty"]
        self.assertAlmostEqual(rec["max"], 3e-6, delta=1e-12)

    def test_uncertainty_is_per_level(self):
        # a 3e-6 change of ANOTHER level does not widen the tolerance of the perturbed one
        reg = self.check("other", 3e-6, {"other": -3e-6})
        self.assertFalse(reg.checks["canonical_eigenvalues"], reg.measurements["canonical_eigenvalues_detail"])

    def test_negative_control_large_error(self):
        # an error of 1e-4 with a measured grid change of 2e-6 is still detected
        reg = self.check("large", 1e-4, {"mid": -2e-6})
        self.assertFalse(reg.checks["canonical_eigenvalues"], reg.measurements["canonical_eigenvalues_detail"])

    def record(self, reg, suffix=""):
        return reg.comparisons["canonical_scf_" + self.LABEL + suffix]["detail"]

    def test_fine_member_gets_its_own_scaled_term(self):
        # |eps(601) - eps(301)| = 3e-6: the 301-point member gets 3e-6, the 601-point member its own
        # (design order 2) 3e-6 / 3 = 1e-6, never the 301-point member's term
        reg = self.check("scaled", 3e-6, {"mid": -3e-6})
        self.assertTrue(reg.checks["canonical_eigenvalues"], reg.measurements["canonical_eigenvalues_detail"])
        coarse = self.record(reg)["rustLevelGridUncertainty"]
        fine = self.record(reg, "_g601")["rustLevelGridUncertainty"]
        self.assertEqual((coarse["gridPoints"], fine["gridPoints"]), (301, 601))
        self.assertAlmostEqual(coarse["max"], 3e-6, delta=1e-12)
        self.assertAlmostEqual(fine["max"], 1e-6, delta=1e-12)
        self.assertEqual(fine["orders"]["design"], fine["levels"])
        self.assertEqual(fine["orders"]["designOrder"], C.RUST_GRID_DESIGN_ORDER)

    def test_negative_control_fine_member_beyond_its_own_tolerance(self):
        # the 301-point member agrees with the reference, the 601-point member is off by 4.5e-6: its own
        # term is 1.5e-6, so the deviation exceeds its tolerance (it would have passed with the 301-point
        # member's term 4.5e-6, the rule before this test)
        shift = 4.5e-6
        reg = self.check("finebad", 0.0, {"mid": shift})
        self.assertFalse(reg.checks["canonical_eigenvalues"], reg.measurements["canonical_eigenvalues_detail"])
        coarse, fine = self.record(reg)["eigenvalues"], self.record(reg, "_g601")["eigenvalues"]
        self.assertLess(coarse["maxDeviationOverTolerance"], 1e-3)
        self.assertGreater(fine["maxDeviationOverTolerance"], 1.0)
        dev = fine["maxAbsDeviation"]
        self.assertAlmostEqual(dev, shift, delta=1e-12)
        tol_own = dev / fine["maxDeviationOverTolerance"]
        self.assertLess(tol_own, dev)
        self.assertGreater(tol_own - shift / 3.0 + shift, dev)    # the old (coarse-term) tolerance missed it
        self.assertIn("scf/%s_g601" % self.LABEL, reg.measurements["canonical_eigenvalues_detail"])


class CheckerTests(unittest.TestCase):

    def test_registry_and_missing_inputs(self):
        reg = C.Registry()
        self.assertFalse(reg.check("x", False, "d"))
        self.assertTrue(reg.check("y", 1 > 0))
        reg.comparison("z", "not run", "absent")
        self.assertEqual(reg.comparisons["z"]["status"], "not run")
        with tempfile.TemporaryDirectory() as tmp:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = C.main(["--reference", os.path.join(tmp, "none"), "--rust", os.path.join(tmp, "none"),
                               "--theory", os.path.join(tmp, "none.json"), "--report", os.path.join(tmp, "rep.json"),
                               "--no-stationarity", "--no-reproduce"])
            self.assertEqual(code, 1)   # the reference is required
            with open(os.path.join(tmp, "rep.json"), encoding="utf-8") as handle:
                report = json.load(handle)
            self.assertFalse(report["checks"]["reference_present"])
            self.assertEqual(report["comparisons"]["rust_outputs"]["status"], "not run")
            self.assertIn("check_count=", out.getvalue())

    def test_report_names_no_folder_of_the_computer(self):
        """The report records repository-relative paths (repo_path): no absolute path of the computer, so
        a re-run from another folder writes the same bytes.  The temporary folder stands in for the
        repository (the reference inside it, the Rust and theory inputs outside it)."""
        from unittest import mock
        self.assertEqual(C.repo_path(os.path.join(C.REPO, "artifacts", "x", "y.json")), "artifacts/x/y.json")
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            repo = os.path.join(tmp, "repo")
            ref = os.path.join(repo, "artifacts", "reference")
            os.makedirs(ref)
            with open(os.path.join(ref, "reference-summary.json"), "w", encoding="utf-8") as handle:
                json.dump({"complete": True, "runs": [{"label": "absent_run", "converged": True}]}, handle)
            report_path = os.path.join(outside, "report.json")
            with mock.patch.object(C, "REPO", repo), contextlib.redirect_stdout(io.StringIO()):
                C.main(["--reference", ref, "--rust", os.path.join(outside, "rust"),
                        "--theory", os.path.join(outside, "theory.json"), "--report", report_path,
                        "--no-stationarity", "--no-reproduce"])
            with open(report_path, encoding="utf-8") as handle:
                text = handle.read()
            report = json.loads(text)
            self.assertEqual(report["measurements"]["reference_present_detail"],
                             "artifacts/reference/reference-summary.json")
            self.assertIn("absent_run", report["measurements"]["reference_run_files_readable_detail"])
            self.assertEqual(report["comparisons"]["theory_json"]["detail"],
                             "missing <outside the repository>/theory.json")
            for folder in (tmp, outside, C.REPO, os.path.expanduser("~")):
                for form in {folder, folder.replace("\\", "/"), json.dumps(folder)[1:-1]}:
                    self.assertNotIn(form, text)
            # nothing that looks like an absolute path: a drive letter with a separator (the backslash
            # JSON-escaped), or a POSIX root folder
            self.assertIsNone(re.search(r'(?<![A-Za-z0-9_])[A-Za-z]:(?:\\\\|/)|(?<![A-Za-z0-9_.])/(?:home|Users|tmp|var|mnt)/',
                                        text))

    def test_rust_labels_and_couplings(self):
        self.assertEqual(K.rust_label(1, 3, 8, "lamp1", 0), "m1_L3_N8_lamp1_T0")
        self.assertEqual(K.rust_label(1, 3, 112, "lam0", 0.1), "m1_L3_N112_lam0_T0p1")
        self.assertEqual(K.rust_label(1, 3, 896, "lamp1", 0, delta_k_over_m=0.125), "m1_L3_N896_lamp1_T0_dk0p125")
        self.assertEqual(K.rust_label(1, 3, 112, "lamp1", 0, delta_k_over_m=0.25 * math.exp(-0.5)),
                         "m1_L3_N112_lamp1_T0_dk0p15163266492815836")
        self.assertEqual(K.rust_label(1, 3, 112, "lamp1", 0, a4=0.5), "m1_L3_N112_lamp1_T0_a40p5")
        self.assertEqual(K.trim_float(3.0), "3")
        specs = K.canonical_runs(False)
        labels = [r["label"] for r in specs]
        self.assertEqual(len(labels), len(set(labels)))
        self.assertIn("L3-free-N8-p-1", labels)
        self.assertIn("m1_L3_N8_lamp1_T1", labels)
        self.assertIn("m1_L3_N112_lamh_T1", labels)
        self.assertIn("m1_L3_N112_lamp1_T1", labels)         # skipped at run time by the first-order rule
        self.assertEqual([r["parity"] for r in specs[:2]], [1, -1])
        couplings = {(1.0, 3.0, 8.0): {"lambdaHat1": 0.01, "lambdaHat2": 0.1}}
        spec = next(s for s in specs if s["label"] == "m1_L3_N8_lamm2_T0")
        self.assertAlmostEqual(K.resolve_lambda(spec, couplings), -0.1)
        spec = next(s for s in specs if s["label"] == "m1_L3_N112_lamp1_T0")
        self.assertIsNone(K.resolve_lambda(spec, couplings))  # its configuration is not known yet
        parsed = C.parse_label("m1_L3_N112_lamp1_T0p3_a40p5_g601_dk0p125")
        self.assertEqual(parsed, {"m": 1.0, "L": 3.0, "N": 112.0, "lambdaName": "lamp1", "T_over_m": 0.3,
                                  "a4_0": 0.5, "gridPoints": 601, "deltaKOverM": 0.125})
        self.assertIsNone(C.parse_label("L3-free-N8-p+1"))

    def test_coupling_rule_on_the_rust_grid(self):
        """The per-configuration coupling of the free N = 8 state: the brane
        zero modes carry no scalar density, n_p peaks at the tip (end node)."""
        with contextlib.redirect_stdout(io.StringIO()):
            rec = K.coupling_rust_grid(1.0, 3.0, 8.0, quick=True)
        self.assertEqual(rec["nRefY"], -3.0)
        self.assertLess(rec["sRef_maxProperScalarDensity_free"], 1e-10)
        self.assertAlmostEqual(rec["strengthPerUnitLambdaHat"], rec["nRef_maxProperNumberDensity_free"] / 16.0, places=12)
        self.assertAlmostEqual(rec["lambdaHat1"] * rec["strengthPerUnitLambdaHat"], 0.1, places=14)
        self.assertEqual(rec["label"], "coupling-m1_L3_N8")

    def test_rust_summary_records_and_checks_forms(self):
        self.assertEqual(C.summary_checks({"checks": {"a": True, "b": False}}), {"a": True, "b": False})
        self.assertEqual(C.summary_checks({"checks": [{"name": "a", "passed": True}]}), {"a": True})
        with tempfile.TemporaryDirectory() as tmp:
            sub = os.path.join(tmp, "thermo")
            os.makedirs(os.path.join(sub, "m1_L3_N8_lamp1_T0p1"))
            summary = {"verdict": "SUCCESS", "checks": {"x": True}, "files": [],
                       "reference": {"couplings": [{"m": 1.0, "L": 3.0, "N": 8.0, "lambdaHat1": 0.01,
                                                    "lambdaHat2": 0.1}]},
                       "runs": [{"label": "m1_L3_N8_lamp1_T0p1", "energy": 1.5, "nTotal": 8.0,
                                 "heatCapacity": 2.0}]}
            with open(os.path.join(sub, "summary.json"), "w", encoding="utf-8") as handle:
                json.dump(summary, handle)
            runs = C.rust_runs(tmp, C.rust_summaries(tmp))
            self.assertEqual(len(runs), 1)
            item = runs[0]
            self.assertIsNone(item["run"])
            self.assertEqual(item["params"]["N"], 8.0)
            self.assertEqual(item["params"]["lambdaHat"], 0.01)   # from the per-configuration couplings
            self.assertAlmostEqual(item["params"]["T"], 0.1)
            self.assertTrue(item["params"]["fromLabel"])
            self.assertEqual(C.rust_energy(item), 1.5)
            self.assertEqual(C.field(item, "heatCapacity"), 2.0)
            reg = C.Registry()
            C.check_rust_internal(reg, tmp, C.rust_summaries(tmp), runs)
            self.assertTrue(reg.checks["rust_summaries_success"])
            self.assertTrue(reg.checks["rust_own_checks_passed"])
            # nothing computed -> recorded as not run, never as a passing check
            self.assertNotIn("rust_energy_from_rho", reg.checks)
            self.assertEqual(reg.comparisons["rust_energy_from_rho"]["status"], "not run")

    def test_rust_conservation_recomputation_detects_violation(self):
        y = np.linspace(-3.0, 0.0, 61)
        vf = np.exp(6 * y)
        p_y = np.exp(3 * y) / vf
        p_3 = 0.5 * np.exp(3 * y) / vf
        p_t = 0.5 * np.exp(3 * y) / vf
        hdr = ["y", "volume_factor", "p_y", "p_3", "p_t"]
        data = np.stack([y, vf, p_y, p_3, p_t], axis=1)
        self.assertLess(C.rust_conservation(hdr, data), 1e-4)
        data[:, 3] *= 2.0
        self.assertGreater(C.rust_conservation(hdr, data), 0.1)

    def test_reference_outputs_are_deterministic(self):
        """Two executions of the same specification write byte-identical files."""
        spec = {"label": "m1_L3_N8_lamp1_T0", "m": 1.0, "L": 3.0, "N": 8.0, "T": 0.0, "N0": 10, "levels": 2,
                "parity": 0, "tip": "g0", "xc": "quadratic", "tasks": ["excited"], "lambda": "lamp1"}
        with tempfile.TemporaryDirectory() as tmp:
            for tag in ("a", "b"):
                with contextlib.redirect_stdout(io.StringIO()):
                    K.execute_run(spec, 0.01, os.path.join(tmp, tag), lambda msg: None)
            names = sorted(os.listdir(os.path.join(tmp, "a", spec["label"])))
            self.assertEqual(names, sorted(os.listdir(os.path.join(tmp, "b", spec["label"]))))
            for name in names:
                with open(os.path.join(tmp, "a", spec["label"], name), "rb") as fa, \
                        open(os.path.join(tmp, "b", spec["label"], name), "rb") as fb:
                    self.assertEqual(fa.read(), fb.read(), name)

    def test_edge_table_reproduces_the_exact_cut(self):
        """The first-order edge table of a hot run evaluated at the solver's own
        window agrees with the exact (re-solved mu) cut, and a narrower window
        drops more."""
        p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.6, N=8.0, parity=1, N0=8, levels=1, exact_shells=100000)
        grid = K.Grid(3.0, 8)
        res = K.scf(p, grid)
        tr = K.rust_window_truncation(res, p, grid)
        table = tr["edgeTable"]
        est = C.truncation_from_table(table, *tr["window"])
        self.assertLess(abs(est["deltaE"] - tr["deltaE"]), 0.02 * abs(tr["deltaE"]) + 1e-12)
        self.assertLess(abs(est["deltaEntropy"] - tr["deltaEntropy"]), 0.02 * abs(tr["deltaEntropy"]) + 1e-12)
        self.assertLess(abs(est["deltaCVfixedSpectrumEntropy"] - tr["deltaCVfixedSpectrumEntropy"]),
                        0.05 * abs(tr["deltaCVfixedSpectrumEntropy"]) + 1e-12)
        narrow = C.truncation_from_table(table, tr["window"][0] + 1.0, tr["window"][1] - 1.0)
        self.assertLess(narrow["deltaE"], est["deltaE"])

    def test_canonical_comparison_and_negative_control(self):
        """A Rust-format copy of a reference run agrees in every compared
        quantity; a perturbed eigenvalue is detected."""
        with tempfile.TemporaryDirectory() as tmp:
            ref_dir = os.path.join(tmp, "ref")
            spec = {"label": "m1_L3_N8_lamp1_T0", "m": 1.0, "L": 3.0, "N": 8.0, "T": 0.0, "N0": 12, "levels": 2,
                    "parity": 0, "tip": "g0", "xc": "quadratic", "tasks": [], "lambda": "lamp1"}
            with contextlib.redirect_stdout(io.StringIO()):
                K.execute_run(spec, 0.01, ref_dir, lambda msg: None)
            for perturb, expect in ((0.0, True), (1e-4, False)):
                rust = os.path.join(tmp, "rust%g" % perturb)
                fake_rust_tree(rust, ref_dir, "m1_L3_N8_lamp1_T0", perturb)
                reg = C.Registry()
                runs = C.rust_runs(rust, C.rust_summaries(rust))
                C.compare_canonical(reg, ref_dir, runs)
                self.assertEqual(reg.checks["canonical_eigenvalues"], expect, reg.measurements)
                self.assertTrue(reg.checks["canonical_eigenvalueMatching"])
                self.assertTrue(reg.checks["canonical_E0"])
                self.assertTrue(reg.checks["canonical_profilesInterior"])
                self.assertTrue(reg.checks["canonical_emtAverages"])
                self.assertTrue(reg.checks["canonical_lambdaHat"])


if __name__ == "__main__":
    unittest.main()
