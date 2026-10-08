"""Unit tests of the Stage-5 {+M, -M} pairs numerics (reference solver options,
the pairs runner and the pairs checker; numpy + stdlib).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_stage5_pairs.py" -v
Small grids only (the whole file runs in well under a minute); outputs go to
tempfile directories; negative controls (a wrong statistics sign, the
untransformed tip bag, a perturbed level) are detected.  The committed
Stage-4 couplings and pairing-theory.json are read where present.
"""

import contextlib
import io
import json
import math
import os
import sys
import tempfile
import unittest

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import ks_reference_solver as K  # noqa: E402
import ks_reference_pairs as RP  # noqa: E402
import check_dirac16complex_pairs as CP  # noqa: E402

THEORY = os.path.join(REPO, "artifacts", "dirac16complex", "pair-creation", "pairing-theory.json")


class ParamsDefaultsTests(unittest.TestCase):
    """Stage-4 defaults are unchanged and write nothing new; |m| sets every scale."""

    def test_default_writes_no_stage5_keys(self):
        d = K.Params(m=1.0, N=8.0).to_dict()
        self.assertNotIn("statistics", d)
        self.assertNotIn("statisticsSign", d)
        self.assertEqual(d["delta_k"], 0.25)
        self.assertEqual(d["delta_k_over_m"], 0.25)
        self.assertEqual(d["solverVersion"], 2)

    def test_commuting_is_recorded(self):
        d = K.Params(m=1.0, N=8.0, statistics="commuting").to_dict()
        self.assertEqual(d["statistics"], "commuting")
        self.assertEqual(d["statisticsSign"], 1)
        self.assertEqual(K.Params(statistics="commuting").to_dict_kwargs()["statistics"], "commuting")

    def test_negative_mass_scales(self):
        p = K.Params(m=-3.0, N=8.0)
        self.assertEqual(p.mass_scale, 3.0)
        self.assertEqual(p.delta_k, 0.75)
        self.assertGreater(p.ell, 0.0)
        self.assertGreater(p.volume, 0.0)
        self.assertEqual(p.to_dict()["delta_k_over_m"], 0.25)
        self.assertEqual(p.lam, K.Params(m=3.0, N=8.0).lam)   # lambda = lambda_hat/m^6 is even in m

    def test_invalid_options_rejected(self):
        with self.assertRaises(ValueError):
            K.Params(statistics="bosonic")
        with self.assertRaises(ValueError):
            K.Params(tip="x")
        with self.assertRaises(ValueError):
            K.coupling_rust_grid(-1.0, 3.0, 8.0)


class PotentialsTests(unittest.TestCase):
    """The statistics sign enters only the exchange term (15/16 vs 17/16, -1/16 vs +1/16)."""

    def setUp(self):
        self.grid = K.Grid(3.0, 12)
        rng = np.random.default_rng(3)
        self.n_c = np.abs(rng.normal(size=13)) * 1e-5
        self.s_c = rng.normal(size=13) * 1e-5

    def test_anticommuting_is_the_stage4_formula(self):
        p = K.Params(m=1.0, lambda_hat=0.3)
        m_eff, v, e_int, dc = K.potentials(p, self.grid, self.n_c, self.s_c)
        s_p, n_p, lam = self.grid.density_factor * self.s_c, self.grid.density_factor * self.n_c, p.lam
        self.assertTrue(np.array_equal(m_eff, p.m + lam * s_p - lam * s_p / 16.0))
        self.assertTrue(np.array_equal(v, -lam * n_p / 16.0))
        self.assertTrue(np.array_equal(e_int, 0.5 * lam * s_p * s_p - (lam / 32.0) * (n_p * n_p + s_p * s_p)))

    def test_commuting_formula(self):
        p = K.Params(m=-1.0, lambda_hat=0.3, statistics="commuting")
        m_eff, v, e_int, dc = K.potentials(p, self.grid, self.n_c, self.s_c)
        s_p, n_p, lam = self.grid.density_factor * self.s_c, self.grid.density_factor * self.n_c, p.lam
        # m_eff - m for m = -1 loses ~1e-16 absolutely to the cancellation of m
        np.testing.assert_allclose(m_eff - p.m, (17.0 / 16.0) * lam * s_p, rtol=1e-14, atol=1e-15)
        np.testing.assert_allclose(v, lam * n_p / 16.0, rtol=1e-14, atol=0)
        np.testing.assert_allclose(e_int, 0.5 * lam * s_p ** 2 + (lam / 32.0) * (n_p ** 2 + s_p ** 2), rtol=1e-14)
        # L_s = (M_eff - m) S_p + v n_p - e_int equals e_int for the quadratic functional (both signs)
        np.testing.assert_allclose(dc - e_int, e_int, rtol=1e-12, atol=1e-15 * float(np.max(np.abs(dc))))

    def test_map_of_the_potentials(self):
        """(m, n, S) -> (-m, n, -S) maps M_eff -> -M_eff and keeps v_x (the same lambda)."""
        for stat in ("anticommuting", "commuting"):
            a = K.potentials(K.Params(m=1.0, lambda_hat=0.3, statistics=stat), self.grid, self.n_c, self.s_c)
            b = K.potentials(K.Params(m=-1.0, lambda_hat=0.3, statistics=stat), self.grid, self.n_c, -self.s_c)
            np.testing.assert_allclose(a[0], -b[0], rtol=1e-15, atol=1e-18)
            np.testing.assert_allclose(a[1], b[1], rtol=0, atol=0)
            np.testing.assert_allclose(a[2], b[2], rtol=1e-15, atol=0)
        # with -lambda instead the vector potential changes sign: the ordinary -lambda problem does not map
        c = K.potentials(K.Params(m=-1.0, lambda_hat=-0.3), self.grid, self.n_c, -self.s_c)
        plus = K.potentials(K.Params(m=1.0, lambda_hat=0.3), self.grid, self.n_c, self.s_c)
        np.testing.assert_allclose(c[1], -plus[1], rtol=1e-15, atol=0)
        self.assertFalse(np.allclose(c[1], plus[1]))


class BlockMapTests(unittest.TestCase):
    """The swap f <-> g: h_s(M; p, g0) and h_{-s}(-M; -p, f0) have the same spectrum (to the
    discretisation error of the exchanged staggered grids), n is equal and S opposite."""

    def shells(self, N, k=0.5, v_amp=0.1):
        grid = K.Grid(3.0, N)
        m_eff = 1.0 + 0.3 * np.cos(grid.y)
        v = v_amp * np.exp(grid.y)
        a = K.solve_shell(grid, m_eff, v, k, 0.0, 1, "g0", True, m=1.0)
        b = K.solve_shell(grid, -m_eff, v, k, 0.0, -1, "f0", True, m=-1.0)
        return a, b

    def test_spectrum_maps_and_converges(self):
        defects = []
        for N in (20, 40, 80):
            a, b = self.shells(N)
            sel_a = np.abs(a["eps"]) < 4.0
            ea = np.sort(a["eps"][sel_a])
            eb = np.sort(b["eps"][np.abs(b["eps"]) < 4.0])
            self.assertEqual(len(ea), len(eb))
            defects.append(float(np.max(np.abs(ea - eb))))
        self.assertLess(defects[2], defects[1])
        self.assertLess(defects[1], defects[0])
        self.assertGreater(defects[0] / defects[1], 3.0)   # O(h^2)
        self.assertLess(defects[2], 2e-3)

    def test_types_parities_and_branches(self):
        a, b = self.shells(40)
        for typ in (1, -1):
            # the physical window (the levels near the grid cutoff 2/h depend on the discretisation)
            sa = (a["type"] == typ) & (np.abs(a["eps"]) < 4.0)
            sb = (b["type"] == -typ) & (np.abs(b["eps"]) < 4.0)
            np.testing.assert_allclose(np.sort(a["eps"][sa]), np.sort(b["eps"][sb]), atol=2e-2)
            np.testing.assert_array_equal(a["branch"][sa][np.argsort(a["eps"][sa])],
                                          b["branch"][sb][np.argsort(b["eps"][sb])])

    def test_densities(self):
        a, b = self.shells(80, v_amp=0.0)
        ia = int(np.argmin(np.abs(a["eps"][a["type"] == 1] - 1.6)))
        ib = int(np.argmin(np.abs(b["eps"][b["type"] == -1] - a["eps"][a["type"] == 1][ia])))
        na, nb = a["n"][a["type"] == 1][ia], b["n"][b["type"] == -1][ib]
        sa, sb = a["s"][a["type"] == 1][ia], b["s"][b["type"] == -1][ib]
        self.assertLess(float(np.max(np.abs(na - nb)[1:-1])) / float(np.max(na)), 5e-2)
        self.assertLess(float(np.max(np.abs(sa + sb)[1:-1])) / float(np.max(np.abs(sa))), 5e-2)

    def test_untransformed_control_differs(self):
        grid = K.Grid(3.0, 40)
        a = K.solve_shell(grid, np.full(41, 1.0), np.zeros(41), 0.0, 0.0, -1, "g0", False, m=1.0)
        c = K.solve_shell(grid, np.full(41, -1.0), np.zeros(41), 0.0, 0.0, -1, "g0", False, m=-1.0)
        ea = np.sort(a["eps"][(a["type"] == 1) & (np.abs(a["eps"]) < 1.0)])
        ec = np.sort(c["eps"][(c["type"] == 1) & (np.abs(c["eps"]) < 1.0)])
        self.assertEqual(len(ea), 0)                       # tan(pL) = -p/M: nothing below the gap
        self.assertEqual(len(ec), 2)                       # the control's bound-state pair
        eb = CP.bound_state_energy(1.0, 3.0)
        self.assertAlmostEqual(abs(ec[1]), eb, delta=5e-3)
        self.assertAlmostEqual(math.tanh(math.sqrt(1 - eb * eb) * 3.0), math.sqrt(1 - eb * eb), places=12)


class NegativeMassSectorRunTests(unittest.TestCase):
    """The lead's warning (STAGE5_SPEC section 8): with |m| scales n_c(-M) = n_c(+M) and
    S_c(-M) = -S_c(+M) node by node at lambda = 0, and the energies pair at lambda != 0."""

    def run_pair(self, lam, stat):
        a = K.SectorRun(K.Params(m=1.0, N=8.0, parity=0, tip="g0", N0=12, levels=1, lambda_hat=lam, statistics=stat))
        b = K.SectorRun(K.Params(m=-1.0, N=8.0, parity=0, tip="f0", N0=12, levels=1, lambda_hat=lam, statistics=stat))
        return a, b

    def test_lambda0_densities(self):
        a, b = self.run_pair(0.0, "anticommuting")
        na, nb = a.levels[0]["n_c"], b.levels[0]["n_c"]
        self.assertGreater(float(np.min(nb[1:-1])), 0.0)              # the sign bug is gone
        self.assertLess(float(np.max(np.abs(na - nb))) / float(np.max(na)), 3e-2)
        self.assertEqual(a.scalars["nTotal"], 8.0)
        self.assertEqual(b.scalars["nTotal"], 8.0)

    def test_interacting_energies_pair(self):
        for stat in ("anticommuting", "commuting"):
            a, b = self.run_pair(0.0097, stat)
            self.assertTrue(a.converged and b.converged)
            ea, eb = float(a.scalars["total"]), float(b.scalars["total"])
            self.assertLess(abs(ea - eb), 5e-2 * abs(ea))
            self.assertGreater(ea * (1 if stat == "commuting" else -1), 0.0)   # the sign of the exchange energy
            self.assertAlmostEqual(float(a.scalars["scalarCharge"]), -float(b.scalars["scalarCharge"]),
                                   delta=5e-2 * abs(float(a.scalars["scalarCharge"])))


class RunnerTests(unittest.TestCase):
    """The pairs matrix (the matrix and labels of the Rust pairs subcommand)."""

    def test_matrix(self):
        specs = RP.pair_specs()
        self.assertEqual(len(specs), 2 * 4 * 5 * 3 + 2 * 2 * 5 * 3)   # T = 0 everywhere, T = 0.1|m| at N = 112
        labels = {s["label"] for s in specs}
        self.assertEqual(len(labels), len(specs))
        self.assertIn("d16c00_m3_L3_N112_lamp2_T0p1/minusM", labels)
        self.assertIn("d16c_m1_L3_N8_lam0_T0/minusM_control", labels)
        self.assertFalse(any("N8" in s["label"] and s["T"] > 0 for s in specs))
        for s in specs:
            sign, tip, _ = RP.UNIVERSES[s["universe"]]
            self.assertEqual(s["m"], sign * abs(s["m"]))
            self.assertEqual(s["tip"], tip)
            self.assertEqual(s["N0"], 120 if abs(s["m"]) > 2 else 60)
            self.assertEqual(s["tasks"], ["excited"] if s["T"] == 0 else ["thermo"])
            self.assertEqual(s["partner"], s["configLabel"] + "/plusM")

    def test_config_label_is_the_rust_label(self):
        # pairs.rs Config::label: {stat}_m{|m|}_L{L}_N{N}_{lambda}_T{T/|m|}
        self.assertEqual(RP.config_label("d16c00", 3.0, 3.0, 112.0, "lamm2", 0.1), "d16c00_m3_L3_N112_lamm2_T0p1")
        self.assertEqual(RP.config_label("d16c", 1.0, 3.0, 8.0, "lam0", 0.0), "d16c_m1_L3_N8_lam0_T0")

    def test_params_of(self):
        spec = [s for s in RP.pair_specs() if s["label"] == "d16c00_m1_L3_N8_lamp1_T0/minusM"][0]
        p = RP.params_of(spec, 0.01)
        self.assertEqual((p.m, p.tip, p.statistics, p.parity, p.N0, p.levels), (-1.0, "f0", "commuting", 0, 60, 3))
        self.assertEqual(p.delta_k, 0.25)

    def test_couplings_are_the_stage4_ones(self):
        path = os.path.join(RP.STAGE4_COUPLINGS, "coupling-m1_L3_N8.json")
        if not os.path.exists(path):
            self.skipTest("Stage-4 reference couplings absent")
        c = RP.coupling_record(1.0, 3.0, 8.0)
        self.assertAlmostEqual(c["lambdaHat2"] / c["lambdaHat1"], 10.0, places=12)
        self.assertEqual(RP.lambda_hat_of("lamm1", c), -c["lambdaHat1"])
        self.assertEqual(RP.lambda_hat_of("lam0", c), 0.0)

    def test_first_order_record(self):
        specs = [s for s in RP.pair_specs() if s["configLabel"].startswith("d16c_m1_L3_N112")]
        couplings = {(1.0, 3.0, 112.0): {"lambdaHat1": 0.01, "lambdaHat2": 0.1}}
        free = "d16c_m1_L3_N112_lam0_T0p1/plusM"
        docs = {free: {"couplingScale": {"strengthPerUnitLambdaHat": 11.0}}}
        rec = RP.thermo_first_order(specs, docs, couplings)
        self.assertAlmostEqual(rec["d16c_m1_L3_N112_lamp1_T0p1/minusM"]["firstOrderPseudoPotentialOverAbsM"], 0.11)
        self.assertFalse(rec["d16c_m1_L3_N112_lamp1_T0p1/minusM"]["outsideWindow"])
        self.assertTrue(rec["d16c_m1_L3_N112_lamm2_T0p1/plusM"]["outsideWindow"])
        self.assertNotIn("d16c_m1_L3_N112_lamp1_T0/plusM", rec)

    def test_readiness(self):
        specs = {s["label"]: s for s in RP.pair_specs()}
        couplings = {(1.0, 3.0, 112.0): {"lambdaHat1": 0.01, "lambdaHat2": 0.1},
                     (3.0, 3.0, 112.0): {"lambdaHat1": 852.6, "lambdaHat2": 8526.0}}
        hot = specs["d16c_m1_L3_N112_lamp2_T0p1/minusM"]
        self.assertEqual(RP.readiness(specs["d16c_m1_L3_N112_lamp2_T0/minusM"], {}, couplings), ("run", None))
        self.assertEqual(RP.readiness(specs["d16c_m1_L3_N112_lam0_T0p1/minusM"], {}, couplings), ("run", None))
        self.assertEqual(RP.readiness(hot, {}, couplings), ("wait", None))      # its free source is not done
        docs = {"d16c_m1_L3_N112_lam0_T0p1/plusM": {"couplingScale": {"strengthPerUnitLambdaHat": 11.2}}}
        self.assertEqual(RP.readiness(hot, docs, couplings)[0], "run")          # 1.12 |m| <= ATTEMPT_LIMIT
        m3 = specs["d16c_m3_L3_N112_lamp1_T0p1/plusM"]
        docs3 = {"d16c_m3_L3_N112_lam0_T0p1/plusM": {"couplingScale": {"strengthPerUnitLambdaHat": 0.0987}}}
        state, rec = RP.readiness(m3, docs3, couplings)
        self.assertEqual(state, "skip")                                         # 84 |m|: not attempted
        self.assertAlmostEqual(rec["firstOrderPseudoPotentialOverAbsM"], 852.6 * 0.0987)
        failed = {"d16c_m3_L3_N112_lam0_T0p1/plusM": {"failed": "x"}}
        self.assertEqual(RP.readiness(m3, failed, couplings)[0], "skip")         # source unavailable

    def test_window_cap_is_an_abort_only_guard(self):
        p = K.Params(m=-1.0, window_cap=5.0)
        K.check_window_cap(p, -4.9, 4.9)
        with self.assertRaises(RuntimeError):
            K.check_window_cap(p, -1.0, 5.1)
        self.assertNotIn("windowCap", p.to_dict())
        self.assertNotIn("window_cap", p.to_dict())
        K.check_window_cap(K.Params(m=1.0), -1e9, 1e9)                          # default: no cap


class ClosedFormTests(unittest.TestCase):
    def test_splitting_constants(self):
        cp, cc = CP.c_paired(1.0, 3.0), CP.c_control(1.0, 3.0)
        Y = math.exp(3.0)
        self.assertAlmostEqual(cc - cp, (2.0 / 3.0) * (Y - 1) ** 2 / (Y + 1), places=12)
        self.assertGreater(cc, cp)
        if os.path.exists(THEORY):
            with open(THEORY, encoding="utf-8") as handle:
                text = json.load(handle)["T3"]["untransformedBCControl"]["valuesM1H1L3a0_floatLabelled"]
            self.assertIn("1.905148253644866", text)
            self.assertAlmostEqual(cp, 1.905148253644866, places=12)
            self.assertAlmostEqual(cc, 13.421975197576823, places=11)

    def test_zero_mode_splitting_numerics(self):
        value, _levels = CP.zero_mode_splitting(1.0, 1, "g0", n0=20)
        self.assertAlmostEqual(value, CP.c_paired(1.0, 3.0), delta=1e-4)
        value, _ = CP.zero_mode_splitting(-1.0, -1, "f0", n0=20)
        self.assertAlmostEqual(value, CP.c_paired(1.0, 3.0), delta=1e-4)
        value, _ = CP.zero_mode_splitting(-1.0, 1, "g0", n0=20)
        self.assertAlmostEqual(value, CP.c_control(1.0, 3.0), delta=2e-3)

    def test_expected_box_spectra(self):
        # plus mixed sector (brane f0, tip g0): tan(pL) = -p/M, no level below M; control: bound state
        plus = CP.expected_box("plus", -1, 1.0, 3.0)
        ctrl = CP.expected_box("control", -1, 1.0, 3.0)
        self.assertGreater(min(plus), 1.0)
        self.assertAlmostEqual(min(ctrl), CP.bound_state_energy(1.0, 3.0), places=9)
        self.assertEqual(CP.expected_box("minus", 1, 1.0, 3.0), plus)     # the swap exchanges the parities
        self.assertEqual(CP.expected_box("minus", -1, 1.0, 3.0), CP.expected_box("plus", 1, 1.0, 3.0))
        self.assertEqual(CP.expected_box("plus", 1, 1.0, 3.0)[0], 0.0)    # the zero mode


class _View:
    """A synthetic view for the matching and totals helpers."""
    solver = "rust"

    def __init__(self, levels, m=1.0, N=8.0, scalars=None, emt=None):
        self.m, self.ms, self.N, self.T = m, abs(m), N, 0.0
        self._levels = levels
        self._scalars = scalars or {}
        self._emt = emt or {}

    def level_groups(self):
        out = {}
        for (q, p, s, n), eps in self._levels.items():
            out.setdefault((q, p, s), []).append({"eps": eps, "branch": 1, "f": 0.0, "mult": 4.0, "index": n,
                                                  "epsLevels": []})
        return out

    def index_map(self, key):
        return (key[0], -key[1], -key[2], -key[3])

    def scalar(self, name):
        return self._scalars.get(name)

    def emt(self, name):
        return self._emt.get(name)


class CheckerHelperTests(unittest.TestCase):
    def test_match_levels_and_negative_control(self):
        P = _View({(0, 1, 1, 0): 0.0, (1, 1, 1, 1): 1.5, (1, -1, -1, 2): 2.0})
        M = _View({(0, -1, -1, 0): 0.0, (1, -1, -1, -1): 1.5, (1, 1, 1, -2): 2.0}, m=-1.0)
        tol = CP.pair_tolerances("rust")["eps"]
        pairs, unmatched, compared = CP.match_levels(P, M, tol, use_index=True)
        self.assertEqual((len(pairs), unmatched), (compared, 0))
        self.assertGreater(compared, 0)
        # a perturbed image level is detected
        M2 = _View({(0, -1, -1, 0): 0.0, (1, -1, -1, -1): 1.5 + 1e-5, (1, 1, 1, -2): 2.0}, m=-1.0)
        pairs2, _, _ = CP.match_levels(P, M2, tol, use_index=True)
        self.assertGreater(max(abs(a["eps"] - b["eps"]) / tol(a["eps"], 1.0) for a, b in pairs2), 1.0)

    def test_pair_totals(self):
        P = _View({}, scalars={"E": 2.0, "F": 2.0, "nTotal": 8.0, "scalarCharge": 0.3},
                  emt={"rho": 1e-3, "p_y": 2e-3, "p_3": 1e-4, "p_t": 1e-4, "s_p": 5e-6, "n_p": 3e-3})
        M = _View({}, m=-1.0, scalars={"E": 2.0, "F": 2.0, "nTotal": 8.0, "scalarCharge": -0.3},
                  emt={"rho": 1e-3, "p_y": 2e-3, "p_3": 1e-4, "p_t": 1e-4, "s_p": -5e-6, "n_p": 3e-3})
        t = CP.pair_totals(P, M)
        self.assertEqual(t["mirror"]["E"], 4.0)
        self.assertEqual(t["mirror"]["nTotal"], 16.0)
        self.assertEqual(t["mirror"]["scalarCharge"], 0.0)
        self.assertEqual(t["kreinImage"]["E"], 0.0)
        self.assertEqual(t["kreinImage"]["nTotal"], 0.0)
        self.assertEqual(t["kreinImage"]["scalarCharge"], 0.6)
        self.assertEqual(t["kreinImage"]["rho"], 0.0)

    def test_strip_and_universe_names(self):
        a = {"params": {"label": "d16c_x/plusM", "m": 1.0}, "pairs": {"field": "d16c"}, "extrapolated": {"total": 0.0}}
        b = {"params": {"label": "d16c00_x/plusM", "m": 1.0, "statistics": "commuting", "statisticsSign": 1},
             "pairs": {"field": "d16c00"}, "extrapolated": {"total": 0.0}}
        self.assertEqual(CP.strip_run_json(a), CP.strip_run_json(b))
        b["extrapolated"]["total"] = 1e-16
        self.assertNotEqual(CP.strip_run_json(a), CP.strip_run_json(b))
        self.assertEqual(CP.UNIVERSE_SHORT["minusM_control"], "control")


class _GridView:
    """A synthetic Rust or reference universe for the Rust-vs-reference comparison: one level, T = 0, the
    given scalars (no profiles, no EMT averages)."""
    solver = "rust"
    KEY = ("d16c", "plus", 1.0, 8.0, "lamp1", 0.0)

    def __init__(self, scalars, grid_points=301, label="d16c_m1_L3_N8_lamp1_T0/plusM"):
        self.key, self.label, self.grid_points = self.KEY, label, grid_points
        self.dir = "%s@%d" % (label, grid_points)
        self.m, self.ms, self.N, self.T = 1.0, 1.0, 8.0, 0.0
        self.lambda_hat = 0.01
        self.run = type("Run", (), {"lambda_hat": 0.01})()
        self._scalars = scalars

    def converged(self):
        return True

    def converged_by(self):
        return "tolerance"

    def scalar(self, name):
        return self._scalars.get(name)

    def profile(self, name):
        return np.full(3, self.m) if name == "M_eff" else np.zeros(3)

    def doc(self):
        return {}

    def level_groups(self):
        return {(0, 1, 1): [{"eps": 0.5, "branch": 1, "f": 1.0}]}

    def smearing(self):
        return False

    def y(self):
        return None

    def emt(self, name):
        return None


class CheckerGridUncertaintyTests(unittest.TestCase):
    """STAGE4_SPEC E4.12/E4.14 in the pairs checker (rust_grid_uncertainty): every member of a Rust y-grid
    refinement family is compared with the reference with its OWN grid-error term: the 301-point member
    |X(601) - X(301)|, the finer member only |X(601) - X(301)| / (2^p - 1) (p measured from three grids,
    otherwise the scheme's smallest order 2)."""

    @staticmethod
    def family(values):
        views = [_GridView({"E": -1e-3, "mu": mu}, grid_points=n) for n, mu in values]
        return views, [(v.grid_points, v) for v in views]

    def test_two_grids_design_order(self):
        (coarse, fine), fam = self.family([(301, 0.5), (601, 0.5 + 3e-6)])
        gc, gf = CP.rust_grid_uncertainty(coarse, fam), CP.rust_grid_uncertainty(fine, fam)
        self.assertEqual((gc["gridPoints"], gf["gridPoints"]), (301, 601))
        self.assertAlmostEqual(gc["values"]["mu"], 3e-6, delta=1e-15)
        self.assertAlmostEqual(gf["values"]["mu"], 1e-6, delta=1e-15)
        self.assertEqual(gc["orderSource"]["mu"], "coarsest")
        self.assertEqual(gf["orderSource"]["mu"], "design")
        self.assertEqual(gf["orders"]["mu"], CP.C4.RUST_GRID_DESIGN_ORDER)
        self.assertEqual(gf["designOrder"], 2.0)
        self.assertIn("smallest order", gf["designOrderReason"])
        self.assertNotIn("designOrder", gc)
        self.assertEqual(CP.rust_grid_uncertainty(coarse, fam[:1]), {})      # no partner: no term

    def test_three_grids_measured_order(self):
        # differences 8e-6 and 1e-6 at ratio 2: p = 3 measured, finer members get diff / 7
        (g0, g1, g2), fam = self.family([(301, 0.5), (601, 0.5 + 8e-6), (1201, 0.5 + 9e-6)])
        u = [CP.rust_grid_uncertainty(v, fam) for v in (g0, g1, g2)]
        self.assertAlmostEqual(u[0]["values"]["mu"], 8e-6, delta=1e-15)
        self.assertAlmostEqual(u[1]["values"]["mu"], 8e-6 / 7.0, delta=1e-12)
        self.assertAlmostEqual(u[2]["values"]["mu"], 1e-6 / 7.0, delta=1e-12)
        for k in (1, 2):
            self.assertEqual(u[k]["orderSource"]["mu"], "measured")
            self.assertAlmostEqual(u[k]["orders"]["mu"], 3.0, delta=1e-9)
            # E is the same on all grids (vanishing difference): its order falls back to the design order,
            # with the reason recorded
            self.assertEqual(u[k]["orderSource"]["E"], "design")
            self.assertEqual(u[k]["values"]["E"], 0.0)
            self.assertIn("vanishing difference", u[k]["designOrderReason"])

    def compare(self, mu_301, mu_601, mu_ref=0.5):
        coarse = _GridView({"E": -1e-3, "mu": mu_301})
        fine = _GridView({"E": -1e-3, "mu": mu_601}, grid_points=601)
        ref = _GridView({"E": -1e-3, "mu": mu_ref})
        reg = CP.Registry()
        CP.check_rust_vs_reference(reg, {coarse.key: coarse}, {ref.key: ref}, {coarse.key: [fine]})
        return reg

    def test_both_members_compared_with_their_own_terms(self):
        # the 301-point member is off by 3e-6, the 601-point member agrees: the coarse member's own term
        # |mu(601) - mu(301)| = 3e-6 covers it
        reg = self.compare(0.5 + 3e-6, 0.5)
        self.assertTrue(reg.checks["rust_vs_reference_muAndGap"], reg.measurements)
        self.assertEqual(reg.measurements["rustVsReferenceCompared"], 2)
        fine = reg.comparisons["rust_vs_reference_d16c_m1_L3_N8_lamp1_T0_plusM_g601"]["detail"]
        coarse = reg.comparisons["rust_vs_reference_d16c_m1_L3_N8_lamp1_T0_plusM"]["detail"]
        self.assertAlmostEqual(coarse["rustGridUncertainty"]["values"]["mu"], 3e-6, delta=1e-15)
        self.assertAlmostEqual(fine["rustGridUncertainty"]["values"]["mu"], 1e-6, delta=1e-15)

    def test_negative_control_planted_deviation_of_the_finer_member(self):
        # the 301-point member agrees with the reference, the 601-point member is off by 4.5e-6: its own term
        # is 4.5e-6 / 3 = 1.5e-6, its tolerance 1e-6 + 1.5e-6 = 2.5e-6 < 4.5e-6, so it is detected; the old rule
        # (the full difference for every member: 1e-6 + 4.5e-6) would have accepted it, and the old checker did
        # not compare the finer member at all
        shift = 4.5e-6
        reg = self.compare(0.5, 0.5 + shift)
        self.assertFalse(reg.checks["rust_vs_reference_muAndGap"])
        detail = reg.measurements["rust_vs_reference_muAndGap_detail"]
        self.assertIn("plusM_g601:mu", detail)
        fine = reg.comparisons["rust_vs_reference_d16c_m1_L3_N8_lamp1_T0_plusM_g601"]["detail"]
        self.assertAlmostEqual(fine["mu"]["deviation"], shift, delta=1e-12)
        self.assertLess(fine["mu"]["tolerance"], shift)
        self.assertGreater(1e-6 + shift, shift)                                     # the old tolerance
        coarse = reg.comparisons["rust_vs_reference_d16c_m1_L3_N8_lamp1_T0_plusM"]["detail"]
        self.assertLess(coarse["mu"]["deviation"], 1e-15)

    def test_no_partner_fixed_tolerance(self):
        coarse = _GridView({"E": -1e-3, "mu": 0.5 + 3e-6})
        ref = _GridView({"E": -1e-3, "mu": 0.5})
        reg = CP.Registry()
        CP.check_rust_vs_reference(reg, {coarse.key: coarse}, {ref.key: ref}, {})
        self.assertFalse(reg.checks["rust_vs_reference_muAndGap"])


class CheckerRobustnessTests(unittest.TestCase):
    """End to end on a tiny synthetic reference tree (coarse grids), with the Rust outputs absent:
    the pairing and control comparisons run, the Rust comparisons are recorded as not run."""

    def test_end_to_end_without_rust(self):
        with tempfile.TemporaryDirectory() as tmp:
            ref = os.path.join(tmp, "reference")
            c = {"configuration": [1.0, 3.0, 8.0], "lambdaHat1": 0.0097, "lambdaHat2": 0.097,
                 "source": "synthetic", "sha256": "0"}
            specs = [s for s in RP.pair_specs(quick=True) if s["lambda"] == "lam0" and s["field"] == "d16c"]
            docs = {}
            with contextlib.redirect_stdout(io.StringIO()):
                for s in specs:
                    s = dict(s, N0=12, levels=2)
                    docs[s["label"]] = RP.execute_pair_run(s, c, ref, lambda msg: None)
            summary = {"runs": [RP.summary_record(docs[s["label"]], s) for s in specs], "failed": [],
                       "failedOutsideWindow": [], "pending": [], "complete": True}
            K.write_json(os.path.join(ref, RP.SUMMARY_NAME), summary)
            report = os.path.join(tmp, "report.json")
            with contextlib.redirect_stdout(io.StringIO()):
                code = CP.main(["--reference", ref, "--rust", os.path.join(tmp, "absent"), "--report", report,
                                "--no-solver"])
            with open(report, encoding="utf-8") as handle:
                doc = json.load(handle)
            self.assertIn(code, (0, 1))
            self.assertIn("rust", doc["comparisonsNotRun"])
            self.assertTrue(doc["checks"]["reference_plus_minus_converged"])
            self.assertTrue(doc["checks"]["pairing_reference_levelMatching"])
            self.assertTrue(doc["checks"]["pairing_reference_particleNumber"])
            self.assertTrue(doc["checks"]["control_reference_controlDiffers"])
            self.assertIn("pairing_reference_eigenvalues", doc["checks"])


if __name__ == "__main__":
    unittest.main()
