#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Independent checker of the Stage-4 Kohn-Sham results (reference vs Rust).

Inputs (all optional except the reference; absent inputs are recorded as
comparisons that did not run, never as passing checks):

  --reference DIR   outputs of scripts/ks_reference_solver.py
                    (default artifacts/dirac16complex/kohn-sham/reference)
  --rust DIR        outputs of studies/dirac16complex_kohn_sham
                    (default artifacts/dirac16complex/kohn-sham/rust):
                    <sub>/summary.json (verdict, checks {name: bool}, files,
                    reference, runs[] records) and <sub>/<label>/{levels.csv,
                    profiles.csv, history.csv, run.json} for sub in scf,
                    thermo, emt; excited/<label>/{levels.csv,
                    levels-excited.csv, particle-hole.csv} with the numbers
                    in the summary records
  --theory PATH     artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json
  --repeat DIR      a second Rust output tree: byte identity of every file
                    listed in the summaries
  --refined DIR     a Rust output tree produced with --refined: tolerance
                    convergence of energies and eigenvalues

What is checked (each printed as check_<name>=true|false):

  reference   presence/completeness; self-tests (block reduction to 1e-12,
              exchange trace identity, gas thermodynamics, analytic k = 0
              spectra after extrapolation, discrete Hellmann-Feynman
              identities, doubler-free dispersion, a4 rescaling, geometry);
              every run converged; N conservation (sum of weights, integral
              of the density); Z2 parity purity (S_c(0) = 0, n_c(0) > 0); the
              y-current chi^dag sigma_x chi of every discrete eigenvector
              vanishes identically and the imposed boundary components vanish
              (computed here on a small grid); no particle/sea branch
              overlap; grid-order estimates near 2 (recomputed from the three
              eps_level columns of spectrum.csv); Chebyshev tail
              interpolation errors; energy from rho = E; EMT trace and
              y-conservation identities; entropy >= 0; C_V >= 0; the two C_V
              estimates of the central difference agree, the fixed-spectrum
              forms coincide at lambda = 0 and agree with the central
              difference there to O(delta^2); Delta-SCF = KS gap at
              lambda = 0; mu = eps_HOMO at T = 0; L-convergence trend of the
              first level; the per-configuration coupling rule;
              stationarity (Hellmann-Feynman) dF/dlambda = (E_H + E_x)/lambda
              and dF/dm = int S_p dV_p by finite differences of small
              self-consistent runs of the imported solver.
  rust        summaries present with verdict SUCCESS and every Rust check
              passed; internal identities of every Rust run (N conservation,
              energy from rho, EMT y-conservation recomputed from
              profiles.csv, HOMO profile boundary conditions = current-free
              ends, Z2 purity S_c(0) = 0, entropy >= 0, no particle/sea
              branch overlap, C_V >= 0, F(T) decreasing, L-convergence
              trend).
  canonical   reference vs Rust, run by run for every label both sides
              computed: the couplings lambda_hat (each side derives its own
              from its free ground state), eigenvalues per (q, parity, block
              type) with the particle/sea branch, E_0 (first-order
              lambda_hat correction by Hellmann-Feynman), mu, KS gap,
              Delta-SCF and the particle-hole list, density / M_eff / v_x /
              EMT profiles on the common nodes (every coarse reference node
              is a Rust node), EMT averages, brane and tip fractions, the E4.1
              sourcing record, thermodynamics (E, F, S, mu after the
              first-order correction for the Rust crate's f_cut = 1e-8 energy
              window, C_V as central difference and in both fixed-spectrum
              forms), the occupation-smearing fallback; tolerances in TOL.
  reproduce   a few Rust parameter sets re-solved by the reference with
              EXACTLY the Rust lambda_hat (no coupling correction needed).
  repeat /    --repeat byte identity; --refined convergence.
  refined
  theory      the exact theory JSON: block formulas map onto the reference
              reduction (their j = -s), the exchange closed form, geometry.

Writes --report (default artifacts/dirac16complex/kohn-sham/python-check-report.json)
with {schemaVersion, producer, checks, measurements, comparisons, sourceSha256}
and exits 1 if any check failed.

Usage: python scripts/check_dirac16complex_kohn_sham.py [options]
       [--max-reproductions N] [--quick] [--no-reproduce] [--no-stationarity]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import ks_reference_solver as KS  # noqa: E402

KOHN = os.path.join(REPO, "artifacts", "dirac16complex", "kohn-sham")
DEFAULT_REFERENCE = os.path.join(KOHN, "reference")
DEFAULT_RUST = os.path.join(KOHN, "rust")
DEFAULT_THEORY = os.path.join(KOHN, "kohn-sham-theory.json")
DEFAULT_REPORT = os.path.join(KOHN, "python-check-report.json")
PRODUCER = "scripts/check_dirac16complex_kohn_sham.py"

# Tolerances (stated once, applied everywhere).  Accuracy budget of the two
# methods: reference eigenvalues after the (h^2, h^3) elimination on N0 = 60,
# 120, 240 are good to ~1e-7 m at |eps| <~ 5 m (self-test at N0 = 100: 4e-8;
# error ~ h^4); Rust eigenvalues to ~1e-9 (CVODE rtol 1e-12) with the
# potentials on a 301-point spline; the reference END-NODE profile values
# are first-order quantities of the staggered scheme and carry O(h^3) after
# the (h, h^2) elimination (measured up to 3e-4 relative at m = 3).  Each
# side derives its own lambda_hat (maximum over the Rust grid nodes of the
# free-state pseudo-potential; measured agreement ~1e-7): the relative
# difference dl = |lh_rust/lh_ref - 1| enters every interacting comparison
# through the pseudo-potential (first order), added as dl * max|V|/m.
TOL = {
    "referenceAnalytic": 5e-7,          # extrapolated k = 0 spectra vs analytic (five levels, N0 = 100)
    "referenceHF": 1e-5,                # discrete Hellmann-Feynman identities in M and v (exact partners)
    "referenceHFk": 2e-3,               # d eps/d k vs -s int kappa z: O(h^2)-consistent only (kappa exact on half nodes)
    "referenceN": 1e-8,                 # N conservation from the state weights (exact discrete identity)
    "referenceNDensity": 1e-4,          # Simpson integral of the extrapolated coarse-grid n_c vs N (O(h_coarse^4))
    "referenceEnergyRho": 1e-8,         # |E from rho - E| / max(|E|, 1)
    "referenceTrace": 1e-10,            # EMT trace identity, relative to max(1, |rho|, |p_y|) of the run
    "referenceConservation": 5e-3,      # EMT y-conservation, finest level, normalised
    "referenceTail": 1e-9,              # Chebyshev tail interpolation error (eigenvalues and profiles)
    "referenceOrder": (1.5, 2.6),       # median order estimate window
    "referenceCV": 2e-2,                # |dE/dT - T dS/dT| / C_V (central differences, delta = 0.05)
    "referenceCVfixedFd": 1e-2,         # lambda = 0: |C_V(fd) - C_V^(0)| / C_V: O(delta^2 (m/T)^2 / 6) truncation
    "referenceGapDSCF": 1e-7,           # Delta-SCF vs KS gap at lambda = 0
    "stationarity": 1e-4,               # finite-difference Hellmann-Feynman of the Mermin functional (relative)
    "lambdaHat": 2e-6,                  # |lh_rust/lh_ref - 1|: both sides take the maximum over the Rust grid nodes;
                                        # the tip end-node densities agree to ~7e-7 (measured)
    "eps": 1e-6,                        # |d eps| <= eps max(1, |eps|/m) m + dl max|V|
    "energy": 1e-6,                     # E_0, F: |dE| <= energy max(|E|, N m) (+ dl |E_int| after correction)
    "scalar": 1e-6,                     # mu, gap, Delta-SCF: |d| <= scalar max(m, |value|) + dl max|V|
    "profileInterior": 2e-5,            # max |d profile| / max|profile| on interior common nodes (+ dl max|V|/m)
    "profileEnd": 2e-3,                 # the two end nodes: O(h^3) after the (h, h^2) elimination
    "emtAverage": 2e-5,                 # |d <X>| / max(|<rho>|, |<p_y>|, |<p_3>|)
    "fraction": 1e-5,                   # brane / tip fractions (absolute)
    "thermoEnergy": 1e-6,               # E, F after the f_cut correction: |d| <= thermoEnergy max(|E|, N m) + 5% |correction|
    "entropy": 1e-6,                    # |dS| <= entropy max(S, N) + 5% |correction|
    "cvFd": 1e-3,                       # central differences on both sides (same delta)
    "cvFixed": 1e-4,                    # fixed-spectrum C_V forms
    "rustConservation": 1e-2,           # recomputed from Rust profiles (301 points, fourth-order stencil)
    "refinedEnergy": 1e-7,
    "refinedEps": 1e-7,
}


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_csv(path):
    with open(path, "r", encoding="utf-8", newline="") as handle:
        header = handle.readline().rstrip("\n").split(",")
    data = np.loadtxt(path, delimiter=",", skiprows=1, ndmin=2)
    if data.size == 0:
        data = np.zeros((0, len(header)))
    return header, data


def column(header, data, name):
    return data[:, header.index(name)]


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def is_num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(float(x))


def integrate_uniform(y, values):
    """Composite Simpson rule on a uniform grid (O(h^4)); trapezoid (O(h^2))
    when the number of intervals is odd.  Returns (integral, rule)."""
    h = y[1] - y[0]
    n = len(y) - 1
    if n % 2 == 0 and n >= 2:
        w = np.full(n + 1, 2.0)
        w[1::2] = 4.0
        w[0] = w[-1] = 1.0
        return float(np.dot(w, values) * h / 3.0), "simpson"
    w = np.full(n + 1, h)
    w[0] = w[-1] = 0.5 * h
    return float(np.dot(w, values)), "trapezoid"


class Registry:
    def __init__(self):
        self.checks = {}
        self.measurements = {}
        self.comparisons = {}

    def check(self, name, ok, detail=""):
        self.checks[name] = bool(ok)
        if detail:
            self.measurements[name + "_detail"] = detail
        return bool(ok)

    def measure(self, name, value):
        self.measurements[name] = KS.jsonable(value)

    def comparison(self, name, status, detail=""):
        self.comparisons[name] = {"status": status, "detail": KS.jsonable(detail)}


def key_parse(text):
    parts = text.split(":")
    return tuple(int(p) for p in parts)


def spectrum_order_estimate(hdr, spec, min_change=1e-9, min_weight=1e-6):
    """Median log2 of the ratio of successive level differences of the
    occupied eigenvalues over the three grids (2 for an h^2 scheme).  Levels
    that do not move between grids (the exact discrete zero mode, differences
    at round-off) carry no order information and are skipped."""
    cols = [c for c in hdr if c.startswith("eps_level")]
    if len(cols) < 3 or len(spec) == 0:
        return None
    e0, e1, e2 = (column(hdr, spec, c) for c in cols[:3])
    w = np.abs(column(hdr, spec, "w"))
    d1 = np.abs(e0 - e1)
    d2 = np.abs(e1 - e2)
    sel = (w > min_weight) & (d1 > min_change) & (d2 > min_change)
    if not np.any(sel):
        return None
    return float(np.median(np.log2(d1[sel] / d2[sel])))


def current_free_boundaries():
    """Computed on a small grid: for every eigenvector of the staggered
    scheme the y-current chi^dag sigma_x chi = 2 Re(f^* g) vanishes
    identically (f real, g = i g~ imaginary: the discrete counterpart of the
    conserved-and-zero current), and the boundary components imposed by the
    conditions vanish: f(0) = 0 for odd parity, f(-L) = 0 for the f-tip
    condition; the g-conditions (even parity at the brane, the canonical bag
    condition g(-L) = 0 at the tip) hold through the odd ghost extension."""
    grid = KS.Grid(3.0, 40)
    worst_current = 0.0
    worst_bc = 0.0
    m_eff = 1.0 + 0.2 * np.exp(grid.y)
    v = 0.1 * np.sin(grid.y)
    for tip in ("g0", "f0"):
        for parity in (1, -1):
            sh = KS.solve_shell(grid, m_eff, v, 0.6, 0.0, parity, tip, True, m=1.0)
            F = sh["F"]
            G = 1j * sh["G"]
            g_nodes = np.zeros_like(F, dtype=complex)
            g_nodes[:, :-1] += 0.5 * G
            g_nodes[:, 1:] += 0.5 * G
            current = 2.0 * np.real(np.conj(F) * g_nodes)
            worst_current = max(worst_current, float(np.max(np.abs(current))))
            scale = float(np.max(np.abs(F)))
            if parity < 0:
                worst_bc = max(worst_bc, float(np.max(np.abs(F[:, -1]))) / scale)
            if tip == "f0":
                worst_bc = max(worst_bc, float(np.max(np.abs(F[:, 0]))) / scale)
    return worst_current, worst_bc


# ---------------------------------------------------------------------------
# A. reference outputs
# ---------------------------------------------------------------------------

def check_reference_self_tests(reg: Registry, tests):
    red = tests.get("blockReduction", {})
    reg.check("reference_block_reduction_exact",
              red.get("maxDeviationFromClosedForm", 1) < 1e-12 and red.get("unitarityDeviation", 1) < 1e-12
              and red.get("algebraDimensionOverR") == 8 and all(red.get("facts", {}).values()),
              "deviation %s, algebra dim %s" % (red.get("maxDeviationFromClosedForm"), red.get("algebraDimensionOverR")))
    types = {b["s"] for b in red.get("blocks", [])}
    reg.check("reference_two_block_types", types == {1, -1} and len(red.get("blocks", [])) == 8
              and all(b["b_equals_J_times_iK1"] for b in red.get("blocks", [])),
              "8 blocks, s = J = +-1 (four of each), B = J iK1")
    reg.check("reference_exchange_trace_identity", tests.get("exchangeTraceIdentityDefect", 1) < 1e-12,
              "%s" % tests.get("exchangeTraceIdentityDefect"))
    gas = tests.get("gas", {})
    reg.check("reference_gas_thermodynamics",
              gas.get("T0_n_closed_form", 1) < 1e-12 and gas.get("dn_dmu_fd", 1) < 1e-6
              and gas.get("dS_dmu_fd", 1) < 1e-6 and gas.get("mu_of_n_roundtrip", 1) < 1e-10
              and gas.get("T0_vs_smallT_n", 1) < 1e-4, json.dumps(gas))
    reg.check("reference_analytic_spectra", tests.get("analyticMaxError", 1) < TOL["referenceAnalytic"],
              "max |eps_extrapolated - analytic| = %s over four BC pairs (lambda = 0, k = 0: the 1D Dirac box)"
              % tests.get("analyticMaxError"))
    reg.measure("referenceAnalyticMaxError", tests.get("analyticMaxError"))
    spectra = tests.get("analyticSpectra", {})
    reg.check("reference_zero_modes_where_expected",
              bool(spectra) and all(v["zeroMode"] == (abs(v["extrapolated"][0]) < 1e-9) for v in spectra.values()),
              "an exact zero mode iff both ends impose the same component")
    hf = tests.get("hellmannFeynman", {})
    reg.check("reference_hellmann_feynman_discrete",
              hf.get("dEps_dM_vs_scalarDensity", 1) < TOL["referenceHF"]
              and hf.get("dEps_dv_vs_number", 1) < TOL["referenceHF"]
              and hf.get("dEps_dk_vs_pressureBilinear", 1) < TOL["referenceHFk"] and abs(hf.get("norm", 0) - 1) < 1e-12,
              json.dumps(hf))
    disp = tests.get("freeDispersion", {})
    reg.check("reference_doubler_free", bool(disp.get("doublerFree")), json.dumps(disp))
    resc = tests.get("rescaling", {})
    reg.check("reference_a4_rescaling", resc.get("maxEigenvalueDifference", 1) < 1e-8
              and resc.get("E0Difference", 1) < 1e-8, json.dumps(resc))
    geo = tests.get("geometry", {})
    reg.check("reference_geometry_closed_forms",
              geo.get("curvatureFiniteDifferenceDefect", 1) < 1e-8 and geo.get("rhoRequired") == -21.0
              and geo.get("pRequired_transverse") == 15.0 and geo.get("braneEnergyDensity") == 12.0
              and geo.get("braneStress_x1_x2_x3_x4_x5_x6_x7") == [-10.0, -10.0, -10.0, -12.0, -10.0, -10.0, -10.0],
              "R = -42, G = diag(15,15,15,15,21,15,15,15), rho_req = -21/kappa, p_req = +15/kappa, "
              "S = -(10,10,10,12,10,10,10)/kappa")


def check_reference(reg: Registry, ref_dir, args):
    summary_path = os.path.join(ref_dir, "reference-summary.json")
    if not os.path.exists(summary_path):
        reg.check("reference_present", False, "missing %s" % summary_path)
        return None
    summary = load_json(summary_path)
    reg.check("reference_present", True, summary_path)
    reg.check("reference_complete", bool(summary.get("complete")), "complete flag of reference-summary.json")
    reg.check("reference_fixture_hash", summary.get("fixtureSha256") == sha256_file(KS.DEFAULT_FIXTURE),
              "fixture sha256 recorded in the reference summary equals the committed fixture")
    tests = summary.get("selfTests", {})
    if tests:
        check_reference_self_tests(reg, tests)
    else:
        reg.comparison("reference_self_tests", "not run", "no selfTests in the summary")
    all_runs = summary.get("runs", [])
    reg.measure("referenceRunCount", len(all_runs))
    reg.check("reference_runs_present", len(all_runs) > 0, "%d runs" % len(all_runs))
    collapsed = [r["label"] for r in all_runs if r.get("convergedBy") == "collapse"]
    conv = [r["label"] for r in all_runs if not r.get("converged")]
    reg.check("reference_all_converged", not conv, "not converged: %s (tip collapses among them: %s)" % (conv, collapsed))
    failed_runs = [r["label"] for r in all_runs if r.get("failed")]
    reg.check("reference_no_failed_runs", not failed_runs, "failed: %s" % failed_runs)
    runs = [r for r in all_runs if not r.get("failed") and r.get("convergedBy") != "collapse"]
    smeared = [r["label"] for r in runs if r.get("exactZeroTemperatureOccupations") is False]
    reg.measure("referenceSmearedRuns", smeared)
    worst = {"N": 0.0, "Ndens": 0.0, "Erho": 0.0, "trace": 0.0, "cons": 0.0, "tail": 0.0, "Sc0": 0.0,
             "mu_vs_homo": 0.0, "cv": 0.0, "cvFixedEq": 0.0, "cvFixedFd": 0.0, "dscf": 0.0}
    orders = []
    n0_positive = True
    thermo_ok = True
    thermo_count = 0
    unreadable = []
    e41_missing = []
    signs = {}
    for r in runs:
        d = os.path.join(ref_dir, r["label"])
        try:
            run = load_json(os.path.join(d, "run.json"))
            hdr, spec = read_csv(os.path.join(d, "spectrum.csv"))
            phdr, prof = read_csv(os.path.join(d, "profiles.csv"))
        except (OSError, ValueError) as error:
            unreadable.append("%s (%s)" % (r["label"], error))
            continue
        p = run["params"]
        N = p["N"]
        worst["N"] = max(worst["N"], rel(run["extrapolated"]["nTotal"], N))
        for lv in run["levels"]:
            worst["N"] = max(worst["N"], rel(lv["energies"]["nTotal"], N))
        banded = (run.get("spectrumCsv") or {}).get("band") is not None
        if not banded:
            wsum = float(np.sum(column(hdr, spec, "mult") * column(hdr, spec, "w")))
            worst["N"] = max(worst["N"], rel(wsum, N))
        y = column(phdr, prof, "y")
        n_c = column(phdr, prof, "n_c")
        s_c = column(phdr, prof, "S_c")
        integral, _ = integrate_uniform(y, n_c)
        worst["Ndens"] = max(worst["Ndens"], rel(p["volume"] * integral, N))
        scale = max(float(np.max(np.abs(s_c))), float(np.max(np.abs(n_c))), 1e-300)
        worst["Sc0"] = max(worst["Sc0"], abs(s_c[-1]) / scale)
        if n_c[-1] <= 0:
            n0_positive = False
        rho_scale = max(1.0, float(np.max(np.abs(column(phdr, prof, "rho")))),
                        float(np.max(np.abs(column(phdr, prof, "p_y")))))
        emt = run["emt"]
        worst["Erho"] = max(worst["Erho"], abs(emt["energyFromRho"] - run["extrapolated"]["total"])
                            / max(abs(run["extrapolated"]["total"]), 1.0))
        worst["trace"] = max(worst["trace"], emt["traceIdentityResidual"] / rho_scale)
        cons = emt.get("conservationResidualMaxNormalised")
        if isinstance(cons, list) and cons and cons[-1] is not None:
            worst["cons"] = max(worst["cons"], cons[-1])
        if not isinstance(emt.get("E41_sourcingConditions"), dict):
            e41_missing.append(r["label"])
        else:
            signs[r["label"]] = emt["E41_sourcingConditions"].get("signOfAverageS")
        for lv in run["levels"]:
            tail = lv.get("tail")
            if tail and tail.get("levels", 0) > 0:
                worst["tail"] = max(worst["tail"], tail.get("maxEpsInterpolationError", 0.0),
                                    tail.get("maxDensityInterpolationError", 0.0))
        o = spectrum_order_estimate(hdr, spec)
        if o is not None and p["T"] <= 0:
            orders.append(o)
        if p["T"] > 0:
            th = run.get("thermo") or {}
            if th:
                thermo_count += 1
                if th["entropy"] < 0 or th["C_V"] < 0 or (th.get("C_V_fixedSpectrum") or 0.0) < 0:
                    thermo_ok = False
                if is_num(th.get("C_V_fd")):
                    worst["cv"] = max(worst["cv"], abs(th["C_V_fd"] - th["C_V_fromEntropy"]) / abs(th["C_V_fd"]))
                if p["lambda_hat"] == 0.0 and is_num(th.get("C_V_fixedSpectrum")):
                    worst["cvFixedEq"] = max(worst["cvFixedEq"], rel(th["C_V_fixedSpectrum"],
                                                                     th["C_V_fixedSpectrumEntropy"]))
                    if is_num(th.get("C_V_fd")):
                        worst["cvFixedFd"] = max(worst["cvFixedFd"], rel(th["C_V_fd"], th["C_V_fixedSpectrum"]))
        ex = run.get("excited")
        if ex and (ex.get("deltaSCF") or {}).get("available") and p["lambda_hat"] == 0.0:
            worst["dscf"] = max(worst["dscf"], abs(ex["deltaSCF"]["deltaSCF"] - ex["deltaSCF"]["ksGap"]))
        if p["T"] <= 0 and p.get("occupationSmearing", 0.0) == 0.0 and run.get("homo"):
            hk = key_parse(run["homo"])
            keys = list(zip(column(hdr, spec, "q").astype(int), column(hdr, spec, "parity").astype(int),
                            column(hdr, spec, "type").astype(int), column(hdr, spec, "index").astype(int)))
            if hk in keys:
                e_h = column(hdr, spec, "eps_extrapolated")[keys.index(hk)]
                worst["mu_vs_homo"] = max(worst["mu_vs_homo"], abs(e_h - run["extrapolated"]["mu"]))
    reg.check("reference_run_files_readable", not unreadable, "unreadable: %s" % unreadable[:5])
    reg.check("reference_N_conservation", worst["N"] < TOL["referenceN"],
              "max relative |sum mult w - N| over runs, grids and spectrum.csv = %.3e" % worst["N"])
    reg.check("reference_N_from_density", worst["Ndens"] < TOL["referenceNDensity"],
              "max relative |l^3 int n_c dy - N| = %.3e (Simpson rule on the extrapolated coarse-grid profiles)"
              % worst["Ndens"])
    reg.check("reference_Z2_parity_purity", worst["Sc0"] < 1e-12 and n0_positive,
              "S_c(0) = 0 for both parities: max |S_c(0)|/max(|S_c|, |n_c|) = %.3e; n_c(0) > 0" % worst["Sc0"])
    reg.check("reference_energy_from_rho", worst["Erho"] < TOL["referenceEnergyRho"], "max %.3e" % worst["Erho"])
    reg.check("reference_emt_trace_identity", worst["trace"] < TOL["referenceTrace"],
              "max residual / max(1, |rho|, |p_y|) = %.3e" % worst["trace"])
    reg.check("reference_emt_y_conservation", worst["cons"] < TOL["referenceConservation"],
              "max normalised residual of P_y' = 3H(P_3 + P_t) on the finest grid: %.3e" % worst["cons"])
    reg.check("reference_tail_interpolation", worst["tail"] < TOL["referenceTail"],
              "max Chebyshev tail error (eigenvalue, profile) %.3e" % worst["tail"])
    lo, hi = TOL["referenceOrder"]
    if orders:
        reg.check("reference_grid_order", all(lo <= o <= hi for o in orders),
                  "median order estimates of the occupied eigenvalues (T = 0 runs): min %.3f max %.3f over %d runs"
                  % (min(orders), max(orders), len(orders)))
    else:
        reg.comparison("reference_grid_order", "not run", "no T = 0 run with three grid levels")
    reg.check("reference_mu_equals_homo", worst["mu_vs_homo"] < 1e-9, "max |mu - eps_HOMO| = %.3e" % worst["mu_vs_homo"])
    cur, bc = current_free_boundaries()
    reg.check("reference_current_free_boundaries", cur < 1e-14 and bc < 1e-14,
              "computed here on a 40-interval grid: max |chi^dag sigma_x chi| over all eigenvectors and nodes = %.2e, "
              "max imposed boundary component = %.2e" % (cur, bc))
    if thermo_count:
        reg.check("reference_thermo_signs", thermo_ok, "entropy >= 0 and C_V >= 0 in %d finite-T runs" % thermo_count)
        reg.check("reference_CV_two_estimates", worst["cv"] < TOL["referenceCV"],
                  "max |dE/dT - T dS/dT| / C_V (central differences) = %.3e" % worst["cv"])
        reg.check("reference_CV_fixed_spectrum_lambda0", worst["cvFixedEq"] < 1e-9
                  and worst["cvFixedFd"] < TOL["referenceCVfixedFd"],
                  "lambda = 0: C_V^(0) = C_V^(S) to %.2e; central difference vs exact fixed-spectrum C_V %.2e "
                  "(O(delta^2) truncation of the central difference)" % (worst["cvFixedEq"], worst["cvFixedFd"]))
    else:
        reg.comparison("reference_thermo", "not run", "no finite-T runs")
    reg.check("reference_dscf_equals_gap_free", worst["dscf"] < TOL["referenceGapDSCF"],
              "max |Delta-SCF - KS gap| at lambda = 0: %.3e" % worst["dscf"])
    reg.check("reference_emt_sourcing_record", not e41_missing, "runs without the E4.1 record: %s" % e41_missing[:5])
    reg.measure("referenceSignOfAverageS", signs)
    firsts = {}
    for r in runs:
        mm = re.match(r"L(\d)-free-N8-p\+1$", r["label"])
        if mm:
            hdr, spec = read_csv(os.path.join(ref_dir, r["label"], "spectrum.csv"))
            e = column(hdr, spec, "eps_extrapolated")
            e = np.sort(e[e > 1e-6])
            if len(e):
                firsts[int(mm.group(1))] = float(e[0])
    if len(firsts) >= 3:
        d23 = abs(firsts[3] - firsts[2])
        d34 = abs(firsts[4] - firsts[3])
        reg.check("reference_L_convergence_trend", d34 < d23,
                  "first level above zero (parity +1, free N = 8): L=2 %.10f, L=3 %.10f, L=4 %.10f" %
                  (firsts[2], firsts[3], firsts[4]))
        reg.measure("referenceFirstLevelByL", firsts)
    else:
        reg.comparison("reference_L_convergence_trend", "not run", "L runs missing: %s" % sorted(firsts))
    couplings = summary.get("couplings") or []
    ok_coup = bool(couplings) and all(
        is_num(c.get("strengthPerUnitLambdaHat")) and c["strengthPerUnitLambdaHat"] > 0
        and abs(c["lambdaHat1"] * c["strengthPerUnitLambdaHat"] - 0.1) < 1e-12
        and abs(c["lambdaHat2"] * c["strengthPerUnitLambdaHat"] - 1.0) < 1e-12
        and abs(max(15.0 / 16.0 * c["sRef_maxProperScalarDensity_free"], c["nRef_maxProperNumberDensity_free"] / 16.0)
                / c["m"] ** 7 - c["strengthPerUnitLambdaHat"]) < 1e-12 * c["strengthPerUnitLambdaHat"]
        for c in couplings)
    reg.check("reference_couplings_rule", ok_coup,
              "%d configurations; lambda_hat_1 strength = 0.1, lambda_hat_2 strength = 1, strength = "
              "max((15/16) S_ref, n_ref/16)/m^7" % len(couplings))
    reg.measure("referenceCouplings", {"m%g_L%g_N%g" % (c["m"], c["L"], c["N"]): c.get("lambdaHat1")
                                       for c in couplings})
    reg.measure("referenceCouplingCoarseNodeBias",
                {"m%g_L%g_N%g" % (c["m"], c["L"], c["N"]):
                 (c["strengthCoarseNodes"] / c["strengthPerUnitLambdaHat"] - 1.0) if is_num(c.get("strengthCoarseNodes"))
                 else None for c in couplings})
    overlap = [r["label"] for r in runs if r.get("branchOverlap")]
    reg.check("reference_no_branch_overlap", not overlap,
              "runs with a sea level above an occupied particle level: %s" % overlap[:10])
    collapse = [r["label"] for r in runs if r.get("collapseSuspected")]
    reg.check("reference_no_tip_collapse", not collapse and not collapsed,
              "runs whose lowest occupied particle-branch level lies below -m (a tip-bound state of the attractive "
              "exchange well amplified by e^{6HL}): suspected %s, stopped %s" % (collapse, collapsed))
    return summary


def check_stationarity(reg: Registry, quick):
    """Finite-difference Hellmann-Feynman identities of the Mermin functional
    on small self-consistent runs of the imported solver (one grid, T = 0.05 so
    that the occupations are smooth): dF/dlambda = (E_H + E_x)/lambda and
    dF/dm = int S_p dV_p at fixed lambda, Delta k and l (five-point stencils)."""
    N0 = 24 if quick else 40
    base = dict(m=1.0, L=3.0, T=0.05, N=32.0, parity=1, N0=N0, levels=1, tol=1e-12)
    lam = 0.006

    def free(**kw):
        p = KS.Params(**{**base, **kw})
        return KS.SectorRun(p).levels[-1]["energies"]
    en0 = free(lambda_hat=lam)
    d = 0.05 * lam
    vals = [free(lambda_hat=lam + f * d)["free"] for f in (-2.0, -1.0, 1.0, 2.0)]
    fd = (vals[0] - 8.0 * vals[1] + 8.0 * vals[2] - vals[3]) / (12.0 * d)
    hf = en0["interaction"] / lam
    dev_l = abs(fd - hf) / max(abs(hf), 1e-300)
    reg.check("stationarity_dF_dlambda", dev_l < TOL["stationarity"],
              "finite difference %.10g vs (E_H + E_x)/lambda = %.10g (relative %.2e; N=32, T=0.05, lambda_hat=%g, N0=%d)"
              % (fd, hf, dev_l, lam, N0))
    dm = 1e-3
    p0 = KS.Params(**{**base, "lambda_hat": lam})

    def with_mass(mm):
        return {"m": mm, "lambda_hat": p0.lam * mm ** 6, "delta_k": p0.delta_k, "ell": p0.ell}
    vals = [free(**with_mass(1.0 + f * dm))["free"] for f in (-2.0, -1.0, 1.0, 2.0)]
    fd_m = (vals[0] - 8.0 * vals[1] + 8.0 * vals[2] - vals[3]) / (12.0 * dm)
    hf_m = en0["scalarCharge"]
    dev_m = abs(fd_m - hf_m) / max(abs(hf_m), 1e-300)
    reg.check("stationarity_dF_dm", dev_m < TOL["stationarity"],
              "finite difference %.10g vs int S_p dV_p = %.10g (relative %.2e)" % (fd_m, hf_m, dev_m))
    reg.measure("stationarity_dF_dlambda_relative", dev_l)
    reg.measure("stationarity_dF_dm_relative", dev_m)


# ---------------------------------------------------------------------------
# B. Rust outputs: reading and internal identities
# ---------------------------------------------------------------------------

SUBCOMMANDS = ("spectrum", "scf", "excited", "thermo", "emt")
LABEL_RE = re.compile(r"^m(?P<m>[0-9p]+)_L(?P<L>[0-9p]+)_N(?P<N>\d+)_(?P<lam>lam[a-z0-9]+)_T(?P<T>[0-9p]+)"
                      r"(?:_a4(?P<a4>[0-9pm]+))?(?:_g(?P<g>\d+))?(?:_dk(?P<dk>[0-9pm]+))?$")
LAMBDA_KEYS = {"lam0": (0.0, None), "lamp1": (1.0, "lambdaHat1"), "lamm1": (-1.0, "lambdaHat1"),
               "lamp2": (1.0, "lambdaHat2"), "lamm2": (-1.0, "lambdaHat2")}


def rust_number(text):
    """Rust label numbers: 'p' is the decimal point, a leading 'm' the sign."""
    return float(text.replace("p", ".").replace("m", "-"))


def parse_label(label):
    """Parameters encoded in a Rust run label m1_L3_N8_lamp1_T0p1[_a40p5][_g601][_dk0p125]."""
    m = LABEL_RE.match(label)
    if not m:
        return None
    d = m.groupdict()
    return {"m": rust_number(d["m"]), "L": rust_number(d["L"]), "N": float(d["N"]), "lambdaName": d["lam"],
            "T_over_m": rust_number(d["T"]), "a4_0": rust_number(d["a4"]) if d["a4"] else 0.0,
            "gridPoints": int(d["g"]) if d["g"] else 301,
            "deltaKOverM": rust_number(d["dk"]) if d["dk"] else 0.25}


def rust_summaries(rust_dir):
    out = {}
    for sub in SUBCOMMANDS:
        path = os.path.join(rust_dir, sub, "summary.json")
        if os.path.exists(path):
            try:
                out[sub] = load_json(path)
            except (OSError, ValueError) as error:
                out[sub] = {"unreadable": str(error), "verdict": "UNREADABLE", "runs": [], "files": []}
    return out


def summary_checks(summary):
    """{name: passed} of a Rust summary: the dict form {name: bool} of the
    crate, or a list of {name, passed} records."""
    checks = summary.get("checks", {})
    if isinstance(checks, dict):
        return {str(k): bool(v) for k, v in checks.items()}
    out = {}
    for c in checks or []:
        if isinstance(c, dict):
            out[str(c.get("name"))] = bool(c.get("passed"))
    return out


def rust_coupling(reference_block, m, L, N):
    """(lambdaHat1, lambdaHat2) of a configuration from a Rust summary's reference block."""
    for c in (reference_block or {}).get("couplings", []) or []:
        if (is_num(c.get("m")) and abs(c["m"] - m) < 1e-12 and abs(c["L"] - L) < 1e-12
                and abs(c["N"] - N) < 1e-9):
            return c
    return None


def rust_runs(rust_dir, summaries):
    """One entry per Rust run directory: {sub, label, dir, run (run.json or
    None), record (the summary's runs[] entry or None), params}.  The
    parameters come from run.json, the record, or the label (lambda_hat then
    from the summary's per-configuration couplings)."""
    runs = []
    for sub, summary in summaries.items():
        base = os.path.join(rust_dir, sub)
        if not os.path.isdir(base):
            continue
        records = {r.get("label"): r for r in summary.get("runs", []) if isinstance(r, dict)}
        reference = summary.get("reference", {}) if isinstance(summary.get("reference"), dict) else {}
        for entry in sorted(os.listdir(base)):
            d = os.path.join(base, entry)
            if not os.path.isdir(d):
                continue
            run = None
            rpath = os.path.join(d, "run.json")
            if os.path.exists(rpath):
                try:
                    run = load_json(rpath)
                except (OSError, ValueError):
                    run = None
            record = records.get(entry)
            if run is None and record is None:
                continue
            params = (run or {}).get("parameters") or (record or {}).get("parameters")
            if not isinstance(params, dict):
                parsed = parse_label(entry)
                if parsed is None:
                    continue
                sign, key = LAMBDA_KEYS.get(parsed["lambdaName"], (None, None))
                lam = None
                if record is not None and is_num(record.get("lambdaHat")):
                    lam = float(record["lambdaHat"])
                elif sign is not None:
                    if key is None:
                        lam = 0.0
                    else:
                        c = rust_coupling(reference, parsed["m"], parsed["L"], parsed["N"])
                        if c is None and is_num(reference.get(key)):
                            lam = sign * reference[key]
                        elif c is not None:
                            lam = sign * c[key]
                params = {"m": parsed["m"], "L": parsed["L"], "N": parsed["N"], "lambdaHat": lam,
                          "T": parsed["T_over_m"] * parsed["m"], "a4_0": parsed["a4_0"],
                          "gridPoints": parsed["gridPoints"], "deltaKOverM": parsed["deltaKOverM"],
                          "ell": 2.0 * math.pi / (parsed["deltaKOverM"] * parsed["m"]), "fromLabel": True}
            runs.append({"sub": sub, "label": entry, "dir": d, "run": run, "record": record, "params": params})
    return runs


def field(item, name):
    """A value of a Rust run from run.json or, failing that, its summary record."""
    for src in (item.get("run"), item.get("record")):
        if isinstance(src, dict) and name in src:
            return src[name]
    return None


def rust_energy(item):
    e = field(item, "energy")
    return e if is_num(e) else field(item, "E0")


def rust_conservation(phdr, prof):
    """P_y' = 3H(P_3 + P_t) recomputed from a Rust profiles.csv (uniform grid)."""
    y = column(phdr, prof, "y")
    vf = column(phdr, prof, "volume_factor")
    Py = vf * column(phdr, prof, "p_y")
    P3 = vf * column(phdr, prof, "p_3")
    Pt = vf * column(phdr, prof, "p_t")
    if len(y) < 8:
        return float("nan")
    h = y[1] - y[0]
    dPy = (-Py[4:] + 8 * Py[3:-1] - 8 * Py[1:-3] + Py[:-4]) / (12 * h)
    res = dPy - 3.0 * (P3 + Pt)[2:-2]
    inner = slice(1, -1)
    # normalised by the largest term of p_y' + 6H p_y = 3H (p_3 + p_t) on the
    # inner nodes (the 6H|P_y| term keeps a free k = 0 state, whose right-hand
    # side vanishes and whose P_y is constant, from dividing round-off by itself)
    scale = max(float(np.max(np.abs(dPy[inner]))), float(np.max(np.abs(3.0 * (P3 + Pt)[2:-2][inner]))),
                6.0 * float(np.max(np.abs(Py[2:-2][inner]))), 1e-300)
    if scale <= 1e-300 or scale < 1e-14 * max(float(np.max(np.abs(Py))), 1e-300):
        return 0.0
    return float(np.max(np.abs(res[inner])) / scale)


def check_rust_internal(reg: Registry, rust_dir, summaries, runs):
    verdicts = {sub: s.get("verdict") for sub, s in summaries.items()}
    reg.measure("rustSubcommandsPresent", sorted(summaries))
    missing = [sub for sub in SUBCOMMANDS if sub not in summaries]
    if missing:
        reg.comparison("rust_subcommands_missing", "not run", "no summary.json for %s" % missing)
    reg.check("rust_summaries_success", bool(summaries) and all(v == "SUCCESS" for v in verdicts.values()),
              json.dumps(verdicts))
    failed = []
    total = 0
    for sub, s in summaries.items():
        for cname, ok in summary_checks(s).items():
            total += 1
            if not ok:
                failed.append("%s:%s" % (sub, cname))
    reg.measure("rustOwnCheckCount", total)
    reg.check("rust_own_checks_passed", total > 0 and not failed, "%d Rust checks, failed: %s" % (total, failed[:20]))
    reg.measure("rustRunCount", len(runs))
    reg.measure("rustRunLabels", ["%s/%s" % (r["sub"], r["label"]) for r in runs])
    worst = {"N": 0.0, "Ndens": 0.0, "Erho": 0.0, "cons": 0.0, "Sc0": 0.0, "bc": 0.0}
    counted = {"N": 0, "Erho": 0, "profiles": 0, "bc": 0}
    entropy_ok = True
    overlap = []
    smeared = []
    for item in runs:
        N = item["params"].get("N") if item["params"] else None
        n_total = field(item, "nTotal")
        n_dens = field(item, "nFromDensity")
        if is_num(N) and is_num(n_total):
            worst["N"] = max(worst["N"], rel(n_total, N))
            counted["N"] += 1
        if is_num(N) and is_num(n_dens):
            worst["Ndens"] = max(worst["Ndens"], rel(n_dens, N))
        emt = field(item, "emt")
        energy = field(item, "energy")
        if isinstance(emt, dict) and is_num(energy) and is_num(emt.get("energyFromRho")):
            worst["Erho"] = max(worst["Erho"], abs(emt["energyFromRho"] - energy) / max(abs(energy), 1.0))
            counted["Erho"] += 1
        ent = field(item, "entropy")
        if is_num(ent) and ent < -1e-12:
            entropy_ok = False
        if field(item, "branchOverlap") is True:
            overlap.append(item["label"])
        if field(item, "exactZeroTemperatureOccupations") is False and item["params"].get("T", 0.0) == 0.0:
            smeared.append("%s/%s" % (item["sub"], item["label"]))
        ppath = os.path.join(item["dir"], "profiles.csv")
        lpath = os.path.join(item["dir"], "levels.csv")
        if os.path.exists(ppath):
            phdr, prof = read_csv(ppath)
            counted["profiles"] += 1
            if all(c in phdr for c in ("y", "volume_factor", "p_y", "p_3", "p_t")):
                c = rust_conservation(phdr, prof)
                if math.isfinite(c):
                    worst["cons"] = max(worst["cons"], c)
            if "S_c" in phdr and "n_c" in phdr:
                s_c = column(phdr, prof, "S_c")
                n_c = column(phdr, prof, "n_c")
                scale = max(float(np.max(np.abs(s_c))), float(np.max(np.abs(n_c))), 1e-300)
                worst["Sc0"] = max(worst["Sc0"], abs(s_c[-1]) / scale)
            eps_homo = field(item, "epsHomo")
            if ("homo_a" in phdr and "homo_b" in phdr and os.path.exists(lpath) and is_num(eps_homo)):
                a = column(phdr, prof, "homo_a")
                b = column(phdr, prof, "homo_b")
                scale = max(float(np.max(np.abs(a))), float(np.max(np.abs(b))), 1e-300)
                lhdr, lev = read_csv(lpath)
                if scale > 1e-300 and "eps" in lhdr and "parity" in lhdr and len(lev):
                    eps = column(lhdr, lev, "eps")
                    par = column(lhdr, lev, "parity")
                    i = int(np.argmin(np.abs(eps - eps_homo)))
                    brane = abs(b[-1]) if par[i] > 0 else abs(a[-1])
                    worst["bc"] = max(worst["bc"], abs(b[0]) / scale, brane / scale)
                    counted["bc"] += 1

    def check_or_not_run(name, count, ok, detail):
        if count > 0:
            reg.check(name, ok, detail)
        else:
            reg.comparison(name, "not run", "no Rust run with the required records/files (" + detail + ")")
    check_or_not_run("rust_N_conservation", counted["N"], worst["N"] < 1e-8 and worst["Ndens"] < 1e-6,
                     "%d runs: max relative |sum weights - N| = %.3e, |N(density) - N| = %.3e"
                     % (counted["N"], worst["N"], worst["Ndens"]))
    check_or_not_run("rust_energy_from_rho", counted["Erho"], worst["Erho"] < 1e-6,
                     "%d runs, max %.3e" % (counted["Erho"], worst["Erho"]))
    check_or_not_run("rust_emt_y_conservation_recomputed", counted["profiles"], worst["cons"] < TOL["rustConservation"],
                     "P_y' = 3H(P_3 + P_t) from %d profiles.csv, max normalised residual %.3e"
                     % (counted["profiles"], worst["cons"]))
    check_or_not_run("rust_Z2_parity_purity", counted["profiles"], worst["Sc0"] < 1e-10,
                     "max |S_c(0)|/max(|S_c|, |n_c|) = %.3e (the scalar density vanishes on the brane for both parities)"
                     % worst["Sc0"])
    check_or_not_run("rust_homo_boundary_conditions", counted["bc"], worst["bc"] < 1e-6,
                     "HOMO profile of %d runs: |b(-L)| and the parity component at y = 0, relative %.3e (current-free ends)"
                     % (counted["bc"], worst["bc"]))
    check_or_not_run("rust_entropy_nonnegative", len(runs), entropy_ok, "entropy >= 0 in every run (%d runs)" % len(runs))
    check_or_not_run("rust_no_branch_overlap", len(runs), not overlap,
                     "runs with a sea level above an occupied particle level: %s" % overlap[:10])
    reg.measure("rustSmearedRuns", smeared)
    tpath = os.path.join(rust_dir, "thermo", "thermodynamics.csv")
    if os.path.exists(tpath):
        thdr, tab = read_csv(tpath)
        needed = ("C_V", "T", "S_entropy", "F", "N", "lambda_hat")
        if all(c in thdr for c in needed) and len(tab):
            cv = column(thdr, tab, "C_V")
            T = column(thdr, tab, "T")
            S = column(thdr, tab, "S_entropy")
            F = column(thdr, tab, "F")
            Nc = column(thdr, tab, "N")
            lam = column(thdr, tab, "lambda_hat")
            ok_cv = bool(np.all(cv[T > 0] > 0))
            if "C_V_fixed_spectrum" in thdr:
                ok_cv = ok_cv and bool(np.all(column(thdr, tab, "C_V_fixed_spectrum")[T > 0] > 0))
            ok_s = bool(np.all(S[T > 0] > 0))
            ok_f = True
            for n_, l_ in sorted({(float(a), float(b)) for a, b in zip(Nc, lam)}):
                sel = (Nc == n_) & (lam == l_)
                Fs = F[sel][np.argsort(T[sel])]
                ok_f = ok_f and bool(np.all(np.diff(Fs) <= 1e-9 * np.maximum(np.abs(Fs[:-1]), 1.0)))
            reg.check("rust_CV_positive", ok_cv, "C_V > 0 at every T > 0 in thermodynamics.csv (%d rows)" % len(tab))
            reg.check("rust_entropy_positive_finiteT", ok_s, "S > 0 at every T > 0")
            reg.check("rust_free_energy_decreasing", ok_f, "F(T) non-increasing along each (N, lambda) series")
        else:
            reg.comparison("rust_thermodynamics_table", "not run", "thermodynamics.csv lacks columns %s" % (needed,))
    else:
        reg.comparison("rust_thermodynamics_table", "not run", "thermo/thermodynamics.csv absent")
    gaps = {}
    for item in runs:
        m = re.match(r"m1_L(\d)_N8_lam0_T0$", item["label"])
        if m and item["sub"] == "scf" and is_num(field(item, "ksGap")):
            gaps[int(m.group(1))] = field(item, "ksGap")
    if all(k in gaps for k in (2, 3, 4)):
        reg.check("rust_L_convergence_trend", abs(gaps[4] - gaps[3]) < abs(gaps[3] - gaps[2]),
                  "KS gap of the free N = 8 state: L=2 %.10f, L=3 %.10f, L=4 %.10f" % (gaps[2], gaps[3], gaps[4]))
        reg.measure("rustFreeN8GapByL", gaps)
    else:
        reg.comparison("rust_L_convergence_trend", "not run",
                       "free N = 8 scf runs at L = 2, 3, 4 not all present: %s" % sorted(gaps))


# ---------------------------------------------------------------------------
# C. canonical comparison: reference run <-> Rust run of the same label
# ---------------------------------------------------------------------------

class Worst:
    """Largest ratio deviation/tolerance per quantity with its location."""

    def __init__(self):
        self.data = {}

    def add(self, quantity, where, deviation, tolerance, detail=""):
        if deviation is None or not math.isfinite(deviation):
            return
        ratio = deviation / tolerance if tolerance > 0 else float("inf")
        cur = self.data.get(quantity)
        entry = cur or {"count": 0, "failures": []}
        entry["count"] += 1
        if cur is None or ratio > cur["ratio"]:
            entry.update({"ratio": ratio, "deviation": deviation, "tolerance": tolerance, "where": where,
                          "detail": detail})
        if ratio > 1.0:
            entry["failures"].append(where)
        self.data[quantity] = entry


def reference_label_for(item):
    """Reference run label for a Rust run: the same label; the Rust grid
    refinement runs (_g601) are compared with the reference run of the base
    label (both approximate the same continuum problem)."""
    return re.sub(r"_g\d+$", "", item["label"])


def load_reference_run(ref_dir, label):
    d = os.path.join(ref_dir, label)
    path = os.path.join(d, "run.json")
    if not os.path.exists(path):
        return None
    run = load_json(path)
    phdr, prof = read_csv(os.path.join(d, "profiles.csv"))
    shdr, spec = read_csv(os.path.join(d, "spectrum.csv"))
    m = run["params"]["m"]
    run["_profiles"] = (phdr, prof)
    run["_spectrum"] = (shdr, spec)
    run["_potScale"] = float(max(np.max(np.abs(column(phdr, prof, "M_eff") - m)),
                                 np.max(np.abs(column(phdr, prof, "v_x")))))
    return run


def compare_levels(worst, where, item, ref, dl, record):
    """Eigenvalues per (q, parity, block type) in the common window, with the
    particle/sea branch and (T = 0) the occupation of every matched level."""
    lpath = os.path.join(item["dir"], "levels.csv")
    if not os.path.exists(lpath):
        record["eigenvalues"] = {"compared": 0, "note": "levels.csv absent"}
        return
    lhdr, lev = read_csv(lpath)
    shdr, spec = ref["_spectrum"]
    if len(lev) == 0 or len(spec) == 0:
        record["eigenvalues"] = {"compared": 0, "note": "empty level table"}
        return
    m = ref["params"]["m"]
    vmax = ref["_potScale"]
    mine = {}
    e_ref = column(shdr, spec, "eps_extrapolated")
    for q, par, typ, br, e, f in zip(column(shdr, spec, "q").astype(int), column(shdr, spec, "parity").astype(int),
                                     column(shdr, spec, "type").astype(int), column(shdr, spec, "branch").astype(int),
                                     e_ref, column(shdr, spec, "f")):
        mine.setdefault((q, par, typ), []).append((float(e), int(br), float(f)))
    e_rust = column(lhdr, lev, "eps")
    lo = max(float(np.min(e_rust)), float(np.min(e_ref))) + 1e-6
    hi = min(float(np.max(e_rust)), float(np.max(e_ref))) - 1e-6
    compared = unmatched = branch_bad = occ_bad = 0
    max_dev = 0.0
    max_ratio = 0.0
    T0 = item["params"].get("T", 0.0) == 0.0 and not item["params"].get("occupationSmearing")
    for row in lev:
        rec = dict(zip(lhdr, row))
        eps = rec["eps"]
        if not lo <= eps <= hi:
            continue
        compared += 1
        cand = mine.get((int(rec["n2"]), int(rec["parity"]), int(rec["s"])), [])
        tol = TOL["eps"] * max(1.0, abs(eps) / m) * m + dl * vmax
        if not cand:
            unmatched += 1
            continue
        j = int(np.argmin([abs(eps - c[0]) for c in cand]))
        dev = abs(eps - cand[j][0])
        if dev > max(1e-2 * max(1.0, abs(eps) / m) * m, 100.0 * tol):
            unmatched += 1      # no partner within a small fraction of a level spacing
            continue
        max_dev = max(max_dev, dev)
        max_ratio = max(max_ratio, dev / tol)
        worst.add("eigenvalues", where, dev, tol, "eps %.8f" % eps)
        if "branch" in rec and int(rec["branch"]) != cand[j][1]:
            branch_bad += 1
        if T0 and "f" in rec and abs(rec["f"] - cand[j][2]) > 1e-6:
            occ_bad += 1
    record["eigenvalues"] = {"compared": compared, "unmatched": unmatched, "maxAbsDeviation": max_dev,
                             "maxDeviationOverTolerance": max_ratio, "branchMismatches": branch_bad,
                             "occupationMismatches": occ_bad if T0 else None, "window": [lo, hi],
                             "blockSignMapping": "Rust s == reference type"}
    worst.add("eigenvalueMatching", where, float(unmatched + branch_bad + occ_bad) + (0.0 if compared else 1.0), 0.5,
              "unmatched %d, branch mismatches %d, occupation mismatches %d, compared %d"
              % (unmatched, branch_bad, occ_bad, compared))


def compare_profiles(worst, where, item, ref, dl, ratio_l, record):
    ppath = os.path.join(item["dir"], "profiles.csv")
    if not os.path.exists(ppath):
        return
    rhdr, rprof = read_csv(ppath)
    fhdr, fprof = ref["_profiles"]
    y_r = column(rhdr, rprof, "y")
    y_f = column(fhdr, fprof, "y")
    pairs = []
    for j, yv in enumerate(y_f):
        i = int(np.argmin(np.abs(y_r - yv)))
        if abs(y_r[i] - yv) < 1e-9:
            pairs.append((i, j))
    if len(pairs) < 3:
        record["profiles"] = {"commonNodes": len(pairs), "note": "grids do not nest"}
        return
    ir = np.array([a for a, _ in pairs])
    jf = np.array([b for _, b in pairs])
    ends = np.array([(j == 0 or j == len(y_f) - 1) for j in jf])
    m = ref["params"]["m"]
    vrel = dl * ref["_potScale"] / m
    out = {"commonNodes": len(pairs)}
    groups = {"density": ("n_c", "S_c", "n_p", "S_p"), "potential": ("M_eff", "v_x"),
              "emt": ("rho", "p_y", "p_3", "p_t")}
    ref_names = {"n_c": "n_c", "S_c": "S_c", "n_p": "n_p", "S_p": "S_p", "M_eff": "M_eff", "v_x": "v_x",
                 "rho": "rho", "p_y": "p_y", "p_3": "p_3", "p_t": "p_t"}
    for group, names in groups.items():
        if group == "emt":
            scale_all = max(max(float(np.max(np.abs(column(fhdr, fprof, n)))) for n in names), 1e-300)
        for name in names:
            if name not in rhdr:
                continue
            a = column(rhdr, rprof, name)[ir]
            b = column(fhdr, fprof, ref_names[name])[jf].copy()
            if name == "M_eff":
                b = m + (b - m) * ratio_l
                a = a - m
                b = b - m
            elif name == "v_x":
                b = b * ratio_l
            if group == "density":
                partner = {"n_c": "S_c", "S_c": "n_c", "n_p": "S_p", "S_p": "n_p"}[name]
                scale = max(float(np.max(np.abs(b))), float(np.max(np.abs(column(fhdr, fprof, partner)[jf]))), 1e-300)
            elif group == "potential":
                scale = max(float(np.max(np.abs(b))), float(np.max(np.abs(a))), 1e-300)
            else:
                scale = scale_all
            dev = np.abs(a - b) / scale
            d_int = float(np.max(dev[~ends])) if np.any(~ends) else 0.0
            d_end = float(np.max(dev[ends])) if np.any(ends) else 0.0
            out[name] = {"interior": d_int, "ends": d_end}
            if group == "potential" and scale < 1e-12 * m:
                continue   # lambda = 0: both vanish identically
            worst.add("profilesInterior", where + ":" + name, d_int, TOL["profileInterior"] + vrel)
            worst.add("profilesEnds", where + ":" + name, d_end, TOL["profileEnd"] + vrel)
    record["profiles"] = out


def compare_emt(worst, where, item, ref, dl, record):
    e_r = field(item, "emt")
    if not isinstance(e_r, dict):
        return
    e_f = ref["emt"]
    avg = e_f["averages"]
    pairs = {"rhoAvg": avg["rho"], "pYAvg": avg["p_y"], "p3Avg": avg["p_3"], "pTAvg": avg["p_t"],
             "sPAvg": avg.get("s_p"), "nPAvg": avg.get("n_p")}
    scale = max(abs(avg["rho"]), abs(avg["p_y"]), abs(avg["p_3"]), 1e-300)
    vrel = dl * ref["_potScale"] / ref["params"]["m"]
    out = {}
    for k, v in pairs.items():
        if is_num(e_r.get(k)) and is_num(v):
            sc = scale if k in ("rhoAvg", "pYAvg", "p3Avg", "pTAvg") else max(abs(avg.get("n_p") or 0.0),
                                                                              abs(avg.get("s_p") or 0.0), 1e-300)
            dev = abs(e_r[k] - v) / sc
            out[k] = {"rust": e_r[k], "reference": v, "relative": dev}
            worst.add("emtAverages", where + ":" + k, dev, TOL["emtAverage"] + vrel)
    for k, kr in (("braneFraction_within_1_over_H", "braneLocalisedFraction"),
                  ("tipFraction_within_1_over_H_of_cutoff", "tipLocalisedFraction")):
        if is_num(e_r.get(k)) and is_num(e_f.get(kr)):
            dev = abs(e_r[k] - e_f[kr])
            out[k] = {"rust": e_r[k], "reference": e_f[kr], "absolute": dev}
            worst.add("fractions", where + ":" + k, dev, TOL["fraction"] + vrel)
    s_r = e_r.get("E41_sourcingConditions") or {}
    s_f = e_f.get("E41_sourcingConditions") or {}
    if s_r and s_f:
        same = (bool(s_r.get("met")) == bool(s_f.get("met")))
        sign_r = np.sign(e_r.get("sPAvg", 0.0)) if is_num(e_r.get("sPAvg")) else None
        if sign_r is not None and abs(e_r["sPAvg"]) > 1e-12 * max(abs(e_r.get("nPAvg", 0.0)), 1e-300):
            same = same and int(sign_r) == int(s_f.get("signOfAverageS", 0))
        out["E41"] = {"rustMet": s_r.get("met"), "referenceMet": s_f.get("met"),
                      "rustLambdaSAvgOverM": s_r.get("lambdaSAvgOverM"),
                      "referenceLambdaSAvgOverM": s_f.get("lambdaSAvgOverM"), "agree": same}
        worst.add("sourcingConditions", where, 0.0 if same else 1.0, 0.5)
    record["emt"] = out


def compare_thermo(worst, where, item, ref, dl, record):
    th = ref.get("thermo") or {}
    if not th:
        record["thermo"] = {"note": "reference run has no thermo record"}
        return
    tr = th.get("rustWindowTruncation") or {}
    N = ref["params"]["N"]
    m = ref["params"]["m"]
    vmax = ref["_potScale"]
    e_int = ref["extrapolated"].get("interaction", 0.0) or 0.0
    corr_l = e_int * dl_signed(item, ref)
    out = {"truncation": tr}
    for key_r, key_f, dkey, kind in (("energy", "energy", "deltaE", "E"), ("freeEnergy", "free", "deltaF", "E"),
                                     ("entropy", "entropy", "deltaEntropy", "S"), ("mu", "mu", "deltaMu", "mu")):
        vr = field(item, key_r)
        vf = th.get(key_f)
        if not (is_num(vr) and is_num(vf)):
            continue
        corr = tr.get(dkey, 0.0) or 0.0
        vf2 = vf + corr + (corr_l if kind == "E" else 0.0)
        dev = abs(vr - vf2)
        if kind == "E":
            tol = TOL["thermoEnergy"] * max(abs(vr), N * m) + 0.05 * abs(corr)
        elif kind == "S":
            tol = TOL["entropy"] * max(abs(vr), N) + 0.05 * abs(corr)
        else:
            tol = TOL["scalar"] * max(m, abs(vr)) + 0.05 * abs(corr) + dl * vmax
        out[key_r] = {"rust": vr, "reference": vf, "truncationCorrection": corr, "referenceCorrected": vf2,
                      "deviation": dev, "tolerance": tol, "uncorrectedDeviation": abs(vr - vf)}
        worst.add("thermodynamics", where + ":" + key_r, dev, tol)
    # heat capacities
    rec = item.get("record") or {}
    cv_fd_r = field(item, "heatCapacityFiniteDifference")
    cv0_r = field(item, "heatCapacityFixedSpectrum")
    cvs_r = field(item, "heatCapacityFixedSpectrumFromEntropy")
    if not is_num(cv0_r) and is_num(rec.get("heatCapacityFixedSpectrum")):
        cv0_r = rec["heatCapacityFixedSpectrum"]
    for name, vr, vf, dkey, tol in (
            ("C_V_fd", cv_fd_r, th.get("C_V_fd"), None, TOL["cvFd"]),
            ("C_V_fixedSpectrum", cv0_r, th.get("C_V_fixedSpectrum"), "deltaCVfixedSpectrum", TOL["cvFixed"]),
            ("C_V_fixedSpectrumEntropy", cvs_r, th.get("C_V_fixedSpectrumEntropy"), "deltaCVfixedSpectrumEntropy",
             TOL["cvFixed"])):
        if not (is_num(vr) and is_num(vf)):
            out[name] = {"rust": vr, "reference": vf, "compared": False}
            continue
        corr = tr.get(dkey, 0.0) if dkey else 0.0
        corr = corr or 0.0
        dev = abs(vr - (vf + corr)) / max(abs(vr), 1e-300)
        tl = tol + 0.05 * abs(corr) / max(abs(vr), 1e-300) + dl * vmax / m
        out[name] = {"rust": vr, "reference": vf, "truncationCorrection": corr, "relative": dev, "tolerance": tl}
        worst.add("heatCapacity", where + ":" + name, dev, tl)
    record["thermo"] = out


def dl_signed(item, ref):
    """lambda_hat_rust/lambda_hat_ref - 1 (0 when either vanishes)."""
    lr = item["params"].get("lambdaHat")
    lf = ref["params"].get("lambda_hat")
    if is_num(lr) and is_num(lf) and lf != 0.0:
        return float(lr) / float(lf) - 1.0
    return 0.0


def compare_canonical(reg: Registry, ref_dir, runs):
    """Every Rust run with a reference run of the same label (see
    reference_label_for), quantity by quantity; one aggregated check per
    quantity, per-run records under comparisons."""
    worst = Worst()
    compared = []
    missing = []
    for item in runs:
        if item["sub"] == "spectrum":
            continue
        label = reference_label_for(item)
        ref = load_reference_run(ref_dir, label)
        where = "%s/%s" % (item["sub"], item["label"])
        if ref is None:
            missing.append(where)
            continue
        compared.append(where)
        p = item["params"] or {}
        record = {"referenceLabel": label}
        lr, lf = p.get("lambdaHat"), ref["params"].get("lambda_hat")
        dl = abs(dl_signed(item, ref))
        ratio_l = 1.0 + dl_signed(item, ref)
        record["lambdaHat"] = {"rust": lr, "reference": lf, "relativeDifference": dl}
        if is_num(lr) and is_num(lf) and (lr != 0.0 or lf != 0.0):
            worst.add("lambdaHat", where, dl if lf != 0.0 else float("inf"), TOL["lambdaHat"])
        elif is_num(lr) and is_num(lf):
            worst.add("lambdaHat", where, 0.0, TOL["lambdaHat"])
        # smearing protocol
        sm_r = p.get("occupationSmearing") or 0.0
        sm_f = ref["params"].get("occupationSmearing") or 0.0
        record["occupationSmearing"] = {"rust": sm_r, "reference": sm_f}
        m = ref["params"]["m"]
        N = ref["params"]["N"]
        vmax = ref["_potScale"]
        T = ref["params"]["T"]
        compare_levels(worst, where, item, ref, dl, record)
        if T == 0.0:
            e_r = rust_energy(item)
            e_f = ref["extrapolated"]["total"]
            if is_num(e_r) and is_num(e_f):
                e_f2 = e_f + (ref["extrapolated"].get("interaction") or 0.0) * dl_signed(item, ref)
                dev = abs(e_r - e_f2)
                tol = TOL["energy"] * max(abs(e_r), N * m)
                record["E0"] = {"rust": e_r, "reference": e_f, "referenceLambdaCorrected": e_f2, "deviation": dev,
                                "tolerance": tol}
                worst.add("E0", where, dev, tol)
            for key_r, value_f in (("mu", ref["extrapolated"].get("mu")), ("ksGap", ref.get("ksGap"))):
                vr = field(item, key_r)
                if is_num(vr) and is_num(value_f):
                    dev = abs(vr - value_f)
                    tol = TOL["scalar"] * max(m, abs(vr)) + dl * vmax
                    record[key_r] = {"rust": vr, "reference": value_f, "deviation": dev, "tolerance": tol}
                    worst.add("muAndGap", where + ":" + key_r, dev, tol)
        if item["sub"] == "excited":
            rec = item.get("record") or {}
            ex = ref.get("excited") or {}
            ds = ex.get("deltaSCF") or {}
            if is_num(rec.get("deltaScf")) and ds.get("available") and is_num(ds.get("deltaSCF")):
                dev = abs(rec["deltaScf"] - ds["deltaSCF"])
                tol = TOL["scalar"] * max(m, abs(rec["deltaScf"])) + dl * vmax
                record["deltaSCF"] = {"rust": rec["deltaScf"], "reference": ds["deltaSCF"], "deviation": dev,
                                      "tolerance": tol}
                worst.add("deltaSCF", where, dev, tol)
            else:
                record["deltaSCF"] = {"rust": rec.get("deltaScf"), "reference": ds.get("deltaSCF"),
                                      "compared": False, "referenceAvailable": ds.get("available")}
            ph = ex.get("particleHole") or []
            if is_num(rec.get("lowestParticleHole")) and ph:
                dev = abs(rec["lowestParticleHole"] - ph[0]["excitation"])
                tol = TOL["scalar"] * max(m, abs(rec["lowestParticleHole"])) + dl * vmax
                record["lowestParticleHole"] = {"rust": rec["lowestParticleHole"], "reference": ph[0]["excitation"],
                                                "deviation": dev}
                worst.add("particleHole", where, dev, tol)
            for key_r, value_f in (("E0", ref["extrapolated"]["total"]), ("mu", ref["extrapolated"].get("mu")),
                                   ("ksGap", ref.get("ksGap"))):
                vr = rec.get(key_r)
                if is_num(vr) and is_num(value_f):
                    if key_r == "E0":
                        value_f = value_f + (ref["extrapolated"].get("interaction") or 0.0) * dl_signed(item, ref)
                        tol = TOL["energy"] * max(abs(vr), N * m)
                        worst.add("E0", where, abs(vr - value_f), tol)
                    else:
                        tol = TOL["scalar"] * max(m, abs(vr)) + dl * vmax
                        worst.add("muAndGap", where + ":" + key_r, abs(vr - value_f), tol)
                    record[key_r] = {"rust": vr, "reference": value_f, "deviation": abs(vr - value_f)}
        compare_profiles(worst, where, item, ref, dl, ratio_l, record)
        compare_emt(worst, where, item, ref, dl, record)
        if T > 0.0:
            compare_thermo(worst, where, item, ref, dl, record)
        reg.comparison("canonical_" + where.replace("/", "_"), "ran", record)
    reg.measure("canonicalCompared", compared)
    reg.measure("canonicalWithoutReferenceRun", missing)
    if not compared:
        reg.comparison("canonical", "not run", "no Rust run has a reference run of the same label")
        return
    descriptions = {
        "lambdaHat": "couplings derived independently on both sides",
        "eigenvalues": "eigenvalues per (q, parity, block type): |d eps| <= %g max(1, |eps|/m) m + dl max|V|" % TOL["eps"],
        "eigenvalueMatching": "every level in the common window matched, same branch, same T = 0 occupation",
        "E0": "E_0 (lambda_hat-corrected): |dE| <= %g max(|E|, N m)" % TOL["energy"],
        "muAndGap": "mu, eps_HOMO-based KS gap: |d| <= %g max(m, |x|) + dl max|V|" % TOL["scalar"],
        "deltaSCF": "Delta-SCF E_1 - E_0",
        "particleHole": "lowest particle-hole excitation",
        "profilesInterior": "profiles on the interior common nodes (relative to the profile scale)",
        "profilesEnds": "profiles on the two end nodes (O(h^3) reference end values)",
        "emtAverages": "proper-volume EMT averages",
        "fractions": "brane and tip fractions",
        "sourcingConditions": "E4.1 verdict and sign of <S_p> agree",
        "thermodynamics": "E, F, S, mu at T > 0 after the f_cut window correction",
        "heatCapacity": "C_V central difference and fixed-spectrum forms",
    }
    for quantity, entry in sorted(worst.data.items()):
        ok = entry["ratio"] <= 1.0
        reg.check("canonical_" + quantity, ok,
                  "%s; %d comparisons, worst %.3e (tolerance %.3e, ratio %.3g) at %s %s; failures: %s"
                  % (descriptions.get(quantity, quantity), entry["count"], entry["deviation"], entry["tolerance"],
                     entry["ratio"], entry["where"], entry.get("detail", ""), entry["failures"][:8]))
        reg.measure("canonicalWorstRatio_" + quantity, entry["ratio"])
    for quantity in descriptions:
        if quantity not in worst.data:
            reg.comparison("canonical_" + quantity, "not run", "no run pair with this quantity")


# ---------------------------------------------------------------------------
# D. reproductions with the exact Rust lambda_hat, repeat and refined runs
# ---------------------------------------------------------------------------

REPRODUCTION_PRIORITY = (r"^m1_L2_N8_lamp1_T0$", r"^m1_L3_N8_lamp2_T0$", r"^m1_L3_N8_lamm2_T0$",
                         r"^m3_L3_N8_lamp1_T0$", r"^m1_L3_N112_lamp2_T0$", r"^m1_L4_N8_lamp1_T0$")


def select_reproductions(runs, max_count):
    """Rust scf runs to re-solve with exactly their lambda_hat (strong couplings first)."""
    chosen = []
    for pattern in REPRODUCTION_PRIORITY:
        for item in runs:
            if item["sub"] == "scf" and re.match(pattern, item["label"]) and item not in chosen:
                chosen.append(item)
    return chosen[:max_count]


def reproduce_rust_run(reg: Registry, item, quick):
    """Re-solve a Rust T = 0 parameter set with the reference solver at the
    Rust lambda_hat (canonical grids unless --quick) and compare E_0, mu,
    the gap and the eigenvalues without any coupling correction."""
    label = item["label"]
    p = item["params"]
    name = "reproduce_%s" % label
    if not p or not is_num(p.get("lambdaHat")) or not is_num(p.get("N")):
        reg.comparison(name, "not run", "parameters unavailable")
        return None
    N0 = KS.QUICK_N0 if quick else KS.CANONICAL_N0
    levels = KS.QUICK_LEVELS if quick else KS.CANONICAL_LEVELS
    delta_k = p.get("deltaKOverM", 0.25) * p["m"]
    params = KS.Params(m=p["m"], a4=p.get("a4_0", 0.0), L=p["L"], lambda_hat=p["lambdaHat"], T=p.get("T", 0.0),
                       N=p["N"], parity=0, tip="g0", xc="quadratic", delta_k=delta_k,
                       ell=p.get("ell", 2.0 * math.pi / delta_k), N0=N0, levels=levels, label="reproduce-" + label)
    try:
        ref = KS.SectorRun(params)
    except Exception as error:  # noqa: BLE001
        reg.comparison(name, "failed", "reference solver failed: %r" % (error,))
        reg.check(name, False, "reference solver failed: %r" % (error,))
        return None
    m, N = p["m"], p["N"]
    problems = []
    res = {"lambdaHat": p["lambdaHat"], "N0": N0, "levels": levels, "converged": ref.converged}
    e_r, e_f = rust_energy(item), float(ref.scalars["total"])
    tol_e = TOL["energy"] * max(abs(e_r), N * m)
    res["E0"] = {"rust": e_r, "reference": e_f, "deviation": abs(e_r - e_f), "tolerance": tol_e}
    if abs(e_r - e_f) > tol_e:
        problems.append("E0")
    for key, vf in (("mu", float(ref.scalars["mu"])), ("ksGap", ref.gap)):
        vr = field(item, key)
        if is_num(vr) and is_num(vf):
            tol = TOL["scalar"] * max(m, abs(vr))
            res[key] = {"rust": vr, "reference": vf, "deviation": abs(vr - vf), "tolerance": tol}
            if abs(vr - vf) > tol:
                problems.append(key)
    lpath = os.path.join(item["dir"], "levels.csv")
    if os.path.exists(lpath):
        lhdr, lev = read_csv(lpath)
        fine = {st.key(): st for st in ref.levels[-1]["spectrum"].states}
        mine = {}
        for key in ref.state_keys:
            q, par, typ, _ = key
            mine.setdefault((q, par, typ), []).append((float(ref.state_eps[key][1]), fine[key].branch))
        lo, hi = ref.levels[-1]["spectrum"].eps_lo, ref.levels[-1]["spectrum"].eps_hi
        worst_ratio, count, bad = 0.0, 0, 0
        for row in lev:
            rec = dict(zip(lhdr, row))
            if not lo + 1e-6 <= rec["eps"] <= hi - 1e-6:
                continue
            cand = mine.get((int(rec["n2"]), int(rec["parity"]), int(rec["s"])), [])
            if not cand:
                bad += 1
                continue
            j = int(np.argmin([abs(rec["eps"] - c[0]) for c in cand]))
            tol = TOL["eps"] * max(1.0, abs(rec["eps"]) / m) * m
            worst_ratio = max(worst_ratio, abs(rec["eps"] - cand[j][0]) / tol)
            count += 1
            if int(rec.get("branch", cand[j][1])) != cand[j][1]:
                bad += 1
        res["eigenvalues"] = {"compared": count, "worstDeviationOverTolerance": worst_ratio, "mismatches": bad}
        if count == 0 or worst_ratio > 1.0 or bad:
            problems.append("eigenvalues")
    res["problems"] = problems
    reg.check(name, not problems and ref.converged,
              "reference re-solved at the Rust lambda_hat %.10g: %s" % (p["lambdaHat"], json.dumps(KS.jsonable(res))[:1500]))
    reg.comparison(name, "ran", res)
    return res


def check_repeat(reg: Registry, rust_dir, repeat_dir, summaries):
    if not repeat_dir or not os.path.isdir(repeat_dir):
        reg.comparison("rust_repeat_byte_identity", "not run", "no --repeat directory")
        return
    differing = []
    compared = 0
    for sub, summary in summaries.items():
        for f in summary.get("files", []):
            a = os.path.join(rust_dir, sub, f)
            b = os.path.join(repeat_dir, sub, f)
            if not os.path.exists(a) or not os.path.exists(b):
                differing.append(sub + "/" + f + " (missing)")
                continue
            compared += 1
            if sha256_file(a) != sha256_file(b):
                differing.append(sub + "/" + f)
        for extra in ("summary.json",):
            a = os.path.join(rust_dir, sub, extra)
            b = os.path.join(repeat_dir, sub, extra)
            if os.path.exists(a) and os.path.exists(b):
                compared += 1
                if sha256_file(a) != sha256_file(b):
                    differing.append(sub + "/" + extra)
    reg.measure("rustRepeatFilesCompared", compared)
    reg.check("rust_repeat_byte_identity", compared > 0 and not differing,
              "%d files compared, differing: %s" % (compared, differing[:10]))


def check_refined(reg: Registry, rust_dir, refined_dir, runs):
    if not refined_dir or not os.path.isdir(refined_dir):
        reg.comparison("rust_refined_convergence", "not run", "no --refined directory")
        return
    refined = {(r["sub"], r["label"]): r for r in rust_runs(refined_dir, rust_summaries(refined_dir))}
    worst_e = 0.0
    worst_eps = 0.0
    count = 0
    for item in runs:
        other = refined.get((item["sub"], item["label"]))
        if other is None:
            continue
        e1, e2 = rust_energy(item), rust_energy(other)
        if is_num(e1) and is_num(e2):
            worst_e = max(worst_e, abs(e1 - e2) / max(abs(e1), abs(e2), 1.0))
            count += 1
        l1 = os.path.join(item["dir"], "levels.csv")
        l2 = os.path.join(other["dir"], "levels.csv")
        if os.path.exists(l1) and os.path.exists(l2):
            h1, a = read_csv(l1)
            h2, b = read_csv(l2)
            if a.shape == b.shape and "eps" in h1 and "eps" in h2:
                worst_eps = max(worst_eps, float(np.max(np.abs(column(h1, a, "eps") - column(h2, b, "eps")))))
    reg.measure("rustRefinedRunsCompared", count)
    reg.check("rust_refined_convergence", count > 0 and worst_e < TOL["refinedEnergy"] and worst_eps < TOL["refinedEps"],
              "%d runs: max relative energy difference %.3e, max eigenvalue difference %.3e" % (count, worst_e, worst_eps))


# ---------------------------------------------------------------------------
# E. exact theory JSON
# ---------------------------------------------------------------------------

def check_theory(reg: Registry, theory_path):
    if not os.path.exists(theory_path):
        reg.comparison("theory_json", "not run", "missing %s" % theory_path)
        return None
    th = load_json(theory_path)
    forms = th.get("reduction", {}).get("blockDiagonalisation", {}).get("blockFormulas", {})
    # their j = -s (J_theory = gamma^0 gamma^1 gamma^4 = -A0 A1 A4); their basis v- = A1 v+
    ok = ("sigma3" in forms.get("A0", "") and "sigma2" in forms.get("A1", "") and "j sigma1" in forms.get("A4", "")
          and "j sigma2" in forms.get("BC", "") and "j s2" in forms.get("B", "") and "-j sigma3" in forms.get("gamma4gamma1", ""))
    reg.check("theory_block_forms_consistent", ok,
              "theory: A0 = sigma3, A1 = -i sigma2, A4 = j sigma1, BC = j sigma2, B = j s2, gamma4 gamma1 = -j sigma3 with "
              "j = -s and their second basis vector A1 v+ = -s x (reference e2 = A4 e1): the reference forms "
              "A0 = sigma_z, A4 = sigma_x, A1 = s i sigma_y, BC = sigma_y, gamma4 gamma1 = s sigma_z map onto them")
    ex = th.get("exchange", {}).get("uniformGas", {})
    reg.check("theory_exchange_closed_form", "lambda/32" in ex.get("closedForm", "") and "n^2 + S^2" in ex.get("closedForm", ""),
              ex.get("closedForm", "")[:200])
    geo = th.get("geometry", {})
    req = geo.get("requiredSource", {})
    reg.check("theory_geometry_numbers", req.get("rhoValue") == "-21" and req.get("pValue") == "15"
              and geo.get("extensions", {}).get("E2_Z2mirror", {}).get("braneStressValues") == ["-10", "-10", "-10", "-12", "-10", "-10", "-10"],
              "rho_req = -21 H^2/kappa, p_req = 15 H^2/kappa, brane stress -(10,10,10,12,10,10,10) H/kappa")
    return th


# ---------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--reference", default=DEFAULT_REFERENCE)
    parser.add_argument("--rust", default=DEFAULT_RUST)
    parser.add_argument("--theory", default=DEFAULT_THEORY)
    parser.add_argument("--repeat", default=None)
    parser.add_argument("--refined", default=None)
    parser.add_argument("--report", default=DEFAULT_REPORT)
    parser.add_argument("--max-reproductions", type=int, default=1)
    parser.add_argument("--quick", action="store_true", help="quick grids for the stationarity and reproduction runs")
    parser.add_argument("--no-reproduce", action="store_true")
    parser.add_argument("--no-stationarity", action="store_true")
    args = parser.parse_args(argv)
    reg = Registry()
    sources = {}

    summary = check_reference(reg, args.reference, args)
    if summary is not None:
        sources["referenceSummary"] = sha256_file(os.path.join(args.reference, "reference-summary.json"))
    sources["referenceSolver"] = sha256_file(os.path.join(REPO, "scripts", "ks_reference_solver.py"))
    sources["checker"] = sha256_file(os.path.abspath(__file__))
    if not args.no_stationarity:
        check_stationarity(reg, args.quick)
    else:
        reg.comparison("stationarity", "not run", "--no-stationarity")

    theory = check_theory(reg, args.theory)
    if theory is not None:
        sources["theoryJson"] = sha256_file(args.theory)

    summaries = rust_summaries(args.rust) if os.path.isdir(args.rust) else {}
    if summaries:
        for sub in summaries:
            sources["rust_" + sub] = sha256_file(os.path.join(args.rust, sub, "summary.json"))
        runs = rust_runs(args.rust, summaries)
        check_rust_internal(reg, args.rust, summaries, runs)
        if summary is not None:
            compare_canonical(reg, args.reference, runs)
        if args.no_reproduce or args.max_reproductions <= 0:
            reg.comparison("rust_reproduction", "not run", "--no-reproduce")
        else:
            chosen = select_reproductions(runs, args.max_reproductions)
            reg.measure("rustReproductions", ["%s/%s" % (it["sub"], it["label"]) for it in chosen])
            if not chosen:
                reg.comparison("rust_reproduction", "not run", "none of the preferred Rust runs present")
            for item in chosen:
                print("reproducing %s/%s" % (item["sub"], item["label"]), flush=True)
                reproduce_rust_run(reg, item, args.quick)
        check_repeat(reg, args.rust, args.repeat, summaries)
        check_refined(reg, args.rust, args.refined, runs)
    else:
        reg.comparison("rust_outputs", "not run", "no Rust summaries under %s" % args.rust)

    failed = [n for n, ok in reg.checks.items() if not ok]
    for name, ok in reg.checks.items():
        print("check_%s=%s" % (name, "true" if ok else "false"))
    for name, value in reg.measurements.items():
        if not name.endswith("_detail"):
            print("measurement_%s=%s" % (name, json.dumps(value)[:400]))
    not_run = sorted(n for n, c in reg.comparisons.items() if c["status"] != "ran")
    print("comparisons_not_run=%s" % json.dumps(not_run))
    print("check_count=%d" % len(reg.checks))
    print("failed_check_count=%d" % len(failed))
    for name in failed:
        print("FAILED %s: %s" % (name, reg.measurements.get(name + "_detail", "")))
    report = {"schemaVersion": 2, "producer": PRODUCER, "tolerances": TOL, "checks": reg.checks,
              "measurements": reg.measurements, "comparisons": reg.comparisons, "sourceSha256": sources,
              "checkCount": len(reg.checks), "failedCheckCount": len(failed), "failed": failed,
              "comparisonsNotRun": not_run}
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(KS.jsonable(report), indent=2) + "\n")
    print("report: %s" % args.report)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
