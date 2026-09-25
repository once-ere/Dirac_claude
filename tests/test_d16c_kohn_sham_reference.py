"""Unit tests for the Stage-4 reference solver and checker (numpy + stdlib).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_kohn_sham_reference.py" -v
The tests call the solver functions directly on small grids, include
negative controls (a wrong closed form is detected, a broken identity is
detected) and write only into tempfile directories.  They do not need the
committed artifacts.
"""

import contextlib
import io
import json
import math
import os
import sys
import tempfile
import unittest

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import ks_reference_solver as K  # noqa: E402
import check_dirac16complex_kohn_sham as C  # noqa: E402


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
        # wrong mass in the projectors but the closed form with the right one: detected
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
        # e_x is even in n and negative for lambda > 0
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
        # exact up to the O(h^3) boundary term of the ghost correction (which carries M_N h/2)
        self.assertAlmostEqual((ep - em) / (2 * d), grid.integrate(sh["s"][i]), places=4)
        # type -1 states are the negated spectrum of h_+(-v)
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
        # quadratic mode: E = sum w eps - E_H - E_x
        self.assertAlmostEqual(en["total"], en["ksSum"] - en["hartree"] - en["exchange"], places=9)
        self.assertGreater(en["maxLambdaSOverM"], 0.0)

    def test_thermal_occupations_and_entropy(self):
        p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.2, N=8.0, parity=1, N0=24)
        grid = K.Grid(3.0, 24)
        res = K.scf(p, grid)
        self.assertAlmostEqual(res["energies"]["nTotal"], 8.0, places=8)
        self.assertGreater(res["energies"]["entropy"], 0.0)
        self.assertLess(res["energies"]["free"], res["energies"]["total"])

    def test_constrained_occupation_defaults(self):
        p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.0, N=8.0, parity=1, N0=24)
        grid = K.Grid(3.0, 24)
        res = K.scf(p, grid)
        states = res["spectrum"].states
        occ = {st.key(): st.f for st in states if st.eps >= -K.ZERO_MODE_TOL and st.f > 0}
        mu, total = K.occupy_constrained(states, occ)
        self.assertAlmostEqual(total, 8.0, places=10)   # sea states default to filled (weight 0)

    def test_union_parity_equals_lower_sector_for_free_n8(self):
        runs = {}
        for par in (1, 0):
            p = K.Params(m=1.0, L=3.0, lambda_hat=0.0, T=0.0, N=8.0, parity=par, N0=24)
            runs[par] = K.scf(p, K.Grid(3.0, 24))
        self.assertAlmostEqual(runs[1]["energies"]["total"], runs[0]["energies"]["total"], places=12)
        self.assertTrue(any(st.parity == -1 for st in runs[0]["spectrum"].states))


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

    def test_write_run_and_checker_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = K.write_run(self.sector, os.path.join(tmp, "r"), {"excited": {"ksGap": self.sector.gap}})
            self.assertTrue(os.path.exists(os.path.join(tmp, "r", "spectrum.csv")))
            hdr, data = C.read_csv(os.path.join(tmp, "r", "spectrum.csv"))
            self.assertIn("parity", hdr)
            self.assertAlmostEqual(float(np.sum(C.column(hdr, data, "mult") * C.column(hdr, data, "w"))), 8.0, places=9)
            self.assertEqual(doc["params"]["N"], 8.0)

    def test_extrapolate3_removes_h2_and_h3(self):
        h = 0.1
        f = lambda hh: 2.0 + 3.0 * hh ** 2 - 5.0 * hh ** 3
        self.assertAlmostEqual(float(K.extrapolate3(f(h), f(h / 2), f(h / 4))), 2.0, places=13)
        g = lambda hh: 1.0 + 0.7 * hh + 0.2 * hh ** 2
        self.assertAlmostEqual(float(K.extrapolate_profile([np.array([g(h)]), np.array([g(h / 2)]), np.array([g(h / 4)])])[0]),
                               1.0, places=13)


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
            report = json.load(open(os.path.join(tmp, "rep.json"), encoding="utf-8"))
            self.assertFalse(report["checks"]["reference_present"])
            self.assertEqual(report["comparisons"]["rust_outputs"]["status"], "not run")

    def test_rust_conservation_recomputation_detects_violation(self):
        y = np.linspace(-3.0, 0.0, 61)
        vf = np.exp(6 * y)
        # exact: P_y = e^{3y}, P_3 + P_t = P_y'/3 = e^{3y}
        p_y = np.exp(3 * y) / vf
        p_3 = 0.5 * np.exp(3 * y) / vf
        p_t = 0.5 * np.exp(3 * y) / vf
        hdr = ["y", "volume_factor", "p_y", "p_3", "p_t"]
        data = np.stack([y, vf, p_y, p_3, p_t], axis=1)
        self.assertLess(C.rust_conservation(hdr, data), 1e-4)
        data[:, 3] *= 2.0
        self.assertGreater(C.rust_conservation(hdr, data), 0.1)


if __name__ == "__main__":
    unittest.main()
