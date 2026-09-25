#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Independent checker of the Stage-4 Kohn-Sham results (reference vs Rust).

Inputs (all optional except the reference; absent inputs are recorded as
comparisons that did not run, never as passing checks):

  --reference DIR   outputs of scripts/ks_reference_solver.py
                    (default artifacts/dirac16complex/kohn-sham/reference)
  --rust DIR        outputs of studies/dirac16complex_kohn_sham
                    (default artifacts/dirac16complex/kohn-sham/rust):
                    <sub>/summary.json and <sub>/<label>/{run.json,levels.csv,
                    profiles.csv,history.csv} for sub in spectrum, scf,
                    excited, thermo, emt
  --theory PATH     artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json
  --repeat DIR      a second Rust output tree: byte identity of every file
                    listed in the summaries
  --refined DIR     a Rust output tree produced with --refined: tolerance
                    convergence of energies and eigenvalues

What is checked (each printed as check_<name>=true|false):

  reference   presence/completeness; self-tests (block reduction to 1e-12,
              exchange trace identity, gas thermodynamics, analytic k = 0
              spectra after extrapolation, discrete Hellmann-Feynman
              identities, doubler-free dispersion, a4 rescaling); every run
              converged; N conservation (sum of weights, integral of the
              density); Z2 parity purity (S_c(0) = 0, n_c(0) > 0, scalar
              density odd/vector density even structure through the brane
              value); grid-order estimates near 2; Chebyshev tail
              interpolation errors; energy from rho = E; EMT trace and
              y-conservation identities; entropy >= 0; C_V >= 0 with the two
              finite-difference estimates dE/dT and T dS/dT agreeing;
              Delta-SCF = KS gap at lambda = 0; L-convergence trend of the
              first level; stationarity (Hellmann-Feynman) dE/dlambda =
              (E_H + E_x)/lambda and dE/dm = int S_p dV_p re-computed here by
              finite differences of small self-consistent runs of the
              imported solver.
  rust        summaries present with verdict SUCCESS; internal identities of
              every Rust run (N conservation, energy from rho, EMT
              y-conservation recomputed from profiles.csv, HOMO profile
              boundary conditions = current-free ends and Z2 purity,
              S_c(0) = 0, entropy >= 0, C_V >= 0, free energy decreasing in
              T, L-convergence trend); reproduction of a subset of the Rust
              parameter sets with the reference solver (both parities filled
              together, as the Rust crate does) and agreement of eigenvalues
              per (n2, parity, s, level), E_0, mu, gaps, entropy, free
              energy, density/M_eff/v_x profiles, EMT averages, Delta-SCF and
              thermodynamics within the stated tolerances; --repeat byte
              identity; --refined convergence.
  theory      the exact theory JSON: block formulas map onto the reference
              reduction (their j = -s), the exchange closed form, the
              geometry numbers.

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

# tolerances (stated once, applied everywhere)
TOL = {
    "referenceAnalytic": 5e-7,          # extrapolated k = 0 spectra vs analytic (five levels, N0 >= 64)
    "referenceHF": 1e-5,                # discrete Hellmann-Feynman identities in M and v (exact partners)
    "referenceHFk": 2e-3,               # d eps/d k vs -s int kappa z: O(h^2)-consistent only (kappa exact on half nodes)
    "referenceN": 1e-8,                 # N conservation from the state weights (exact discrete identity)
    "referenceNDensity": 1e-4,          # trapezoid integral of the extrapolated coarse-grid n_c vs N (O(h_coarse^2))
    "referenceEnergyRho": 1e-8,         # |E from rho - E| / max(|E|, 1)
    "referenceTrace": 1e-10,            # EMT trace identity
    "referenceConservation": 5e-3,      # EMT y-conservation, finest level, normalised
    "referenceTail": 1e-9,              # Chebyshev tail interpolation error
    "referenceOrder": (1.5, 2.6),       # median order estimate window
    "referenceCV": 2e-2,                # |dE/dT - T dS/dT| / max(C_V)
    "referenceGapDSCF": 1e-7,           # Delta-SCF vs KS gap at lambda = 0
    "stationarity": 1e-4,               # finite-difference Hellmann-Feynman of the Mermin functional (relative)
    "rustEps": 2e-6,                    # |eps_rust - eps_ref| (absolute + 1e-6 relative)
    "rustEnergy": 2e-6,                 # relative, E_0, F, mu, gap
    "rustEntropy": 1e-5,
    "rustProfile": 2e-4,                # relative to max|profile|
    "rustEMT": 5e-4,
    "rustDeltaSCF": 1e-5,
    "rustCV": 2e-2,
    "rustConservation": 1e-2,           # recomputed from Rust profiles (301 points, 2nd order)
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


class Registry:
    def __init__(self):
        self.checks = {}
        self.measurements = {}
        self.comparisons = {}
        self.notes = []

    def check(self, name, ok, detail=""):
        self.checks[name] = bool(ok)
        if detail:
            self.measurements[name + "_detail"] = detail
        return bool(ok)

    def measure(self, name, value):
        if isinstance(value, (np.floating, np.integer)):
            value = value.item()
        if isinstance(value, float) and not math.isfinite(value):
            value = None
        self.measurements[name] = value

    def comparison(self, name, status, detail=""):
        self.comparisons[name] = {"status": status, "detail": detail}


def key_parse(text):
    parts = text.split(":")
    return tuple(int(p) for p in parts)


# ---------------------------------------------------------------------------
# A. reference outputs
# ---------------------------------------------------------------------------

def check_reference(reg: Registry, ref_dir, args):
    summary_path = os.path.join(ref_dir, "reference-summary.json")
    if not os.path.exists(summary_path):
        reg.check("reference_present", False, "missing %s" % summary_path)
        return None
    summary = load_json(summary_path)
    reg.check("reference_present", True, summary_path)
    reg.check("reference_complete", bool(summary.get("complete")), "complete flag")
    reg.check("reference_fixture_hash", summary.get("fixtureSha256") == sha256_file(KS.DEFAULT_FIXTURE),
              "fixture sha256 recorded in the reference summary equals the committed fixture")
    tests = summary.get("selfTests", {})
    if tests:
        red = tests.get("blockReduction", {})
        reg.check("reference_block_reduction_exact",
                  red.get("maxDeviationFromClosedForm", 1) < 1e-12 and red.get("unitarityDeviation", 1) < 1e-12
                  and red.get("algebraDimensionOverR") == 8 and all(red.get("facts", {}).values()),
                  "deviation %s, algebra dim %s" % (red.get("maxDeviationFromClosedForm"), red.get("algebraDimensionOverR")))
        types = {b["s"] for b in red.get("blocks", [])}
        reg.check("reference_two_block_types", types == {1, -1} and len(red.get("blocks", [])) == 8
                  and all(b["b_equals_J_times_iK1"] for b in red.get("blocks", [])),
                  "8 blocks, s = J = +-1, B = J iK1")
        reg.check("reference_exchange_trace_identity", tests.get("exchangeTraceIdentityDefect", 1) < 1e-12,
                  "%s" % tests.get("exchangeTraceIdentityDefect"))
        gas = tests.get("gas", {})
        reg.check("reference_gas_thermodynamics",
                  gas.get("T0_n_closed_form", 1) < 1e-12 and gas.get("dn_dmu_fd", 1) < 1e-6
                  and gas.get("dS_dmu_fd", 1) < 1e-6 and gas.get("mu_of_n_roundtrip", 1) < 1e-10
                  and gas.get("T0_vs_smallT_n", 1) < 1e-4,
                  json.dumps(gas))
        reg.check("reference_analytic_spectra", tests.get("analyticMaxError", 1) < TOL["referenceAnalytic"],
                  "max |eps_extrapolated - analytic| = %s over four BC pairs" % tests.get("analyticMaxError"))
        reg.measure("referenceAnalyticMaxError", tests.get("analyticMaxError"))
        spectra = tests.get("analyticSpectra", {})
        reg.check("reference_zero_modes_where_expected",
                  all(v["zeroMode"] == (abs(v["extrapolated"][0]) < 1e-9) for v in spectra.values()),
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
                  "R = -42, G = diag(15,15,15,15,21,15,15,15), rho_req = -21/kappa, S = -(10,10,10,12,10,10,10)/kappa")
    runs = summary.get("runs", [])
    reg.measure("referenceRunCount", len(runs))
    reg.check("reference_runs_present", len(runs) > 0, "%d runs" % len(runs))
    conv = [r["label"] for r in runs if not r["converged"]]
    reg.check("reference_all_converged", not conv, "not converged: %s" % conv)
    # per-run identities from the run directories
    worst = {"N": 0.0, "Ndens": 0.0, "Erho": 0.0, "trace": 0.0, "cons": 0.0, "tail": 0.0, "Sc0": 0.0,
             "mu_vs_homo": 0.0}
    orders = []
    n0_zero = True
    thermo_ok = True
    cv_dev = 0.0
    dscf_dev = 0.0
    for r in runs:
        d = os.path.join(ref_dir, r["label"])
        run = load_json(os.path.join(d, "run.json"))
        N = run["params"]["N"]
        worst["N"] = max(worst["N"], rel(run["extrapolated"]["nTotal"], N))
        hdr, spec = read_csv(os.path.join(d, "spectrum.csv"))
        wsum = float(np.sum(column(hdr, spec, "mult") * column(hdr, spec, "w")))
        worst["N"] = max(worst["N"], rel(wsum, N))
        phdr, prof = read_csv(os.path.join(d, "profiles.csv"))
        y = column(phdr, prof, "y")
        n_c = column(phdr, prof, "n_c")
        s_c = column(phdr, prof, "S_c")
        h = y[1] - y[0]
        w = np.full(len(y), h)
        w[0] = w[-1] = 0.5 * h
        vol = run["params"]["volume"]
        worst["Ndens"] = max(worst["Ndens"], rel(vol * float(np.dot(w, n_c)), N))
        worst["Sc0"] = max(worst["Sc0"], abs(s_c[-1]) / max(np.max(np.abs(s_c)), 1e-300))
        if n_c[-1] <= 0:
            n0_zero = False
        emt = run["emt"]
        worst["Erho"] = max(worst["Erho"], abs(emt["energyFromRho"] - run["extrapolated"]["total"])
                            / max(abs(run["extrapolated"]["total"]), 1.0))
        worst["trace"] = max(worst["trace"], emt["traceIdentityResidual"])
        cons = emt.get("conservationResidualMaxNormalised")
        if isinstance(cons, list) and cons:
            worst["cons"] = max(worst["cons"], cons[-1] if cons[-1] is not None else 0.0)
        for lv in run["levels"]:
            tail = lv.get("tail")
            if tail and tail.get("levels", 0) > 0:
                worst["tail"] = max(worst["tail"], tail.get("maxEpsInterpolationError", 0.0),
                                    tail.get("maxDensityInterpolationError", 0.0))
        o = run["orderEstimates"].get("occupiedEigenvalues_median")
        if o is not None and math.isfinite(o):
            orders.append(o)
        if run["params"]["T"] > 0:
            th = run.get("thermo", {})
            if th:
                if th["entropy"] < 0 or th["C_V"] < 0:
                    thermo_ok = False
                cv_dev = max(cv_dev, abs(th["C_V"] - th["C_V_fromEntropy"]) / max(abs(th["C_V"]), 1e-300))
        ex = run.get("excited")
        if ex and ex.get("deltaSCF", {}).get("available") and run["params"]["lambda_hat"] == 0.0:
            dscf_dev = max(dscf_dev, abs(ex["deltaSCF"]["deltaSCF"] - ex["deltaSCF"]["ksGap"]))
        # mu equals the HOMO eigenvalue at T = 0
        if run["params"]["T"] <= 0 and run.get("homo"):
            hk = key_parse(run["homo"])
            keys = list(zip(column(hdr, spec, "q").astype(int), column(hdr, spec, "parity").astype(int),
                            column(hdr, spec, "type").astype(int), column(hdr, spec, "index").astype(int)))
            if hk in keys:
                e_h = column(hdr, spec, "eps_extrapolated")[keys.index(hk)]
                worst["mu_vs_homo"] = max(worst["mu_vs_homo"], abs(e_h - run["extrapolated"]["mu"]))
    reg.check("reference_N_conservation", worst["N"] < TOL["referenceN"], "max relative |sum mult w - N| = %.3e" % worst["N"])
    reg.check("reference_N_from_density", worst["Ndens"] < TOL["referenceNDensity"],
              "max relative |l^3 int n_c dy - N| = %.3e (extrapolated coarse-grid profiles)" % worst["Ndens"])
    reg.check("reference_Z2_parity_purity", worst["Sc0"] < 1e-12 and n0_zero,
              "scalar density vanishes on the brane for either parity (max |S_c(0)|/max|S_c| = %.3e), n_c(0) > 0" % worst["Sc0"])
    reg.check("reference_energy_from_rho", worst["Erho"] < TOL["referenceEnergyRho"], "max %.3e" % worst["Erho"])
    reg.check("reference_emt_trace_identity", worst["trace"] < TOL["referenceTrace"], "max %.3e" % worst["trace"])
    reg.check("reference_emt_y_conservation", worst["cons"] < TOL["referenceConservation"],
              "max normalised residual of P_y' = 3H(P_3 + P_t) on the finest grid: %.3e" % worst["cons"])
    reg.check("reference_tail_interpolation", worst["tail"] < TOL["referenceTail"], "max Chebyshev error %.3e" % worst["tail"])
    lo, hi = TOL["referenceOrder"]
    if orders:
        reg.check("reference_grid_order", all(lo <= o <= hi for o in orders),
                  "median order estimates of the occupied eigenvalues: %s" % [round(o, 3) for o in orders])
    else:
        reg.comparison("reference_grid_order", "not run", "no run with three grid levels (order estimates need three)")
    reg.check("reference_mu_equals_homo", worst["mu_vs_homo"] < 1e-9, "max |mu - eps_HOMO| = %.3e" % worst["mu_vs_homo"])
    reg.check("reference_thermo_signs", thermo_ok, "entropy >= 0 and C_V >= 0 for every finite-T run")
    reg.check("reference_CV_two_estimates", cv_dev < TOL["referenceCV"],
              "max |dE/dT - T dS/dT| / C_V = %.3e" % cv_dev)
    reg.check("reference_dscf_equals_gap_free", dscf_dev < TOL["referenceGapDSCF"],
              "max |Delta-SCF - KS gap| at lambda = 0: %.3e" % dscf_dev)
    # L-convergence trend of the first level above the zero modes (free N = 8, parity +)
    firsts = {}
    for r in runs:
        lab = r["label"]
        m = re.match(r"L(\d)-free-N8-p\+1", lab)
        if m:
            d = os.path.join(ref_dir, lab)
            hdr, spec = read_csv(os.path.join(d, "spectrum.csv"))
            e = column(hdr, spec, "eps_extrapolated")
            e = np.sort(e[e > 1e-6])
            if len(e):
                firsts[int(m.group(1))] = float(e[0])
    if len(firsts) >= 3:
        d23 = abs(firsts[3] - firsts[2])
        d34 = abs(firsts[4] - firsts[3])
        reg.check("reference_L_convergence_trend", d34 < d23,
                  "first level above zero: L=2 %.8f, L=3 %.8f, L=4 %.8f" % (firsts[2], firsts[3], firsts[4]))
        reg.measure("referenceFirstLevelByL", firsts)
    else:
        reg.comparison("reference_L_convergence_trend", "not run", "L runs missing: %s" % sorted(firsts))
    # coupling rule recorded
    reg.check("reference_couplings_recorded", bool(summary.get("couplings")), json.dumps(summary.get("couplings", []))[:400])
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
# B. Rust outputs
# ---------------------------------------------------------------------------

SUBCOMMANDS = ("spectrum", "scf", "excited", "thermo", "emt")


def rust_summaries(rust_dir):
    out = {}
    for sub in SUBCOMMANDS:
        path = os.path.join(rust_dir, sub, "summary.json")
        if os.path.exists(path):
            out[sub] = load_json(path)
    return out


def rust_run_dirs(rust_dir, summaries):
    """(sub, label, dir) for every Rust run that has run.json."""
    runs = []
    for sub, summary in summaries.items():
        base = os.path.join(rust_dir, sub)
        for entry in sorted(os.listdir(base)):
            d = os.path.join(base, entry)
            if os.path.isdir(d) and os.path.exists(os.path.join(d, "run.json")):
                runs.append((sub, entry, d))
    return runs


def rust_conservation(phdr, prof):
    """P_y' = 3H(P_3 + P_t) recomputed from a Rust profiles.csv (uniform grid)."""
    y = column(phdr, prof, "y")
    vf = column(phdr, prof, "volume_factor")
    Py = vf * column(phdr, prof, "p_y")
    P3 = vf * column(phdr, prof, "p_3")
    Pt = vf * column(phdr, prof, "p_t")
    h = y[1] - y[0]
    if len(y) < 8:
        return float("nan")
    dPy = (-Py[4:] + 8 * Py[3:-1] - 8 * Py[1:-3] + Py[:-4]) / (12 * h)
    res = dPy - 3.0 * (P3 + Pt)[2:-2]
    inner = slice(1, -1)
    scale = max(float(np.max(np.abs(dPy[inner]))), float(np.max(np.abs(3.0 * (P3 + Pt)[2:-2][inner]))), 1e-300)
    if scale < 1e-14 * max(float(np.max(np.abs(Py))), 1e-300):
        return 0.0
    return float(np.max(np.abs(res[inner])) / scale)


def check_rust_internal(reg: Registry, rust_dir, summaries, runs):
    verdicts = {sub: s.get("verdict") for sub, s in summaries.items()}
    reg.measure("rustSubcommandsPresent", sorted(summaries))
    reg.check("rust_summaries_success", bool(summaries) and all(v == "SUCCESS" for v in verdicts.values()),
              json.dumps(verdicts))
    failed = []
    for sub, s in summaries.items():
        for c in s.get("checks", []):
            if not c.get("passed"):
                failed.append("%s:%s" % (sub, c.get("name")))
    reg.check("rust_own_checks_passed", not failed, "failed Rust checks: %s" % failed[:20])
    reg.measure("rustRunCount", len(runs))
    worst = {"N": 0.0, "Ndens": 0.0, "Erho": 0.0, "cons": 0.0, "Sc0": 0.0, "bc": 0.0}
    entropy_ok = True
    for sub, label, d in runs:
        run = load_json(os.path.join(d, "run.json"))
        p = run["parameters"]
        N = p["N"]
        worst["N"] = max(worst["N"], rel(run["nTotal"], N))
        worst["Ndens"] = max(worst["Ndens"], rel(run["nFromDensity"], N))
        worst["Erho"] = max(worst["Erho"], abs(run["emt"]["energyFromRho"] - run["energy"]) / max(abs(run["energy"]), 1.0))
        if run["entropy"] < -1e-12:
            entropy_ok = False
        ppath = os.path.join(d, "profiles.csv")
        lpath = os.path.join(d, "levels.csv")
        if os.path.exists(ppath):
            phdr, prof = read_csv(ppath)
            worst["cons"] = max(worst["cons"], rust_conservation(phdr, prof))
            s_c = column(phdr, prof, "S_c")
            worst["Sc0"] = max(worst["Sc0"], abs(s_c[-1]) / max(float(np.max(np.abs(s_c))), 1e-300))
            # HOMO profile: current-free ends and Z2 purity: b(-L) = 0 (bag), b(0) = 0 or a(0) = 0
            a = column(phdr, prof, "homo_a")
            b = column(phdr, prof, "homo_b")
            scale = max(float(np.max(np.abs(a))), float(np.max(np.abs(b))), 1e-300)
            if scale > 1e-300 and os.path.exists(lpath):
                lhdr, lev = read_csv(lpath)
                eps = column(lhdr, lev, "eps")
                par = column(lhdr, lev, "parity")
                if len(eps):
                    i = int(np.argmin(np.abs(eps - run["epsHomo"]))) if math.isfinite(run["epsHomo"]) else None
                    if i is not None:
                        brane = abs(b[-1]) if par[i] > 0 else abs(a[-1])
                        worst["bc"] = max(worst["bc"], abs(b[0]) / scale, brane / scale)
    reg.check("rust_N_conservation", worst["N"] < 1e-8 and worst["Ndens"] < 1e-6,
              "max relative |sum weights - N| = %.3e, |N(density) - N| = %.3e" % (worst["N"], worst["Ndens"]))
    reg.check("rust_energy_from_rho", worst["Erho"] < 1e-6, "max %.3e" % worst["Erho"])
    reg.check("rust_emt_y_conservation_recomputed", worst["cons"] < TOL["rustConservation"],
              "P_y' = 3H(P_3 + P_t) from profiles.csv, max normalised residual %.3e" % worst["cons"])
    reg.check("rust_Z2_parity_purity", worst["Sc0"] < 1e-10,
              "max |S_c(0)|/max|S_c| = %.3e (scalar density vanishes on the brane)" % worst["Sc0"])
    reg.check("rust_homo_boundary_conditions", worst["bc"] < 1e-6,
              "HOMO profile: |b(-L)| and the parity component at y = 0, relative %.3e (current-free ends)" % worst["bc"])
    reg.check("rust_entropy_nonnegative", entropy_ok, "entropy >= 0 in every run")
    # thermodynamics table
    tpath = os.path.join(rust_dir, "thermo", "thermodynamics.csv")
    if os.path.exists(tpath):
        thdr, tab = read_csv(tpath)
        cv = column(thdr, tab, "C_V")
        T = column(thdr, tab, "T")
        S = column(thdr, tab, "S_entropy")
        F = column(thdr, tab, "F")
        Nc = column(thdr, tab, "N")
        lam = column(thdr, tab, "lambda_hat")
        ok_cv = bool(np.all(cv[T > 0] > 0))
        ok_s = bool(np.all(S[T > 0] > 0))
        ok_f = True
        for n_, l_ in {(float(a), float(b)) for a, b in zip(Nc, lam)}:
            sel = (Nc == n_) & (lam == l_)
            Ts = T[sel]
            Fs = F[sel][np.argsort(Ts)]
            ok_f = ok_f and bool(np.all(np.diff(Fs) <= 1e-9 * np.maximum(np.abs(Fs[:-1]), 1.0)))
        reg.check("rust_CV_nonnegative", ok_cv, "C_V > 0 at every T > 0 in thermodynamics.csv")
        reg.check("rust_entropy_positive_finiteT", ok_s, "S > 0 at every T > 0")
        reg.check("rust_free_energy_decreasing", ok_f, "F(T) non-increasing along each (N, lambda) series")
    else:
        reg.comparison("rust_thermodynamics_table", "not run", "thermo/thermodynamics.csv absent")
    # L-convergence trend from scf runs (free N = 8: labels m1_L{2,3,4}_N8_lam0_T0)
    gaps = {}
    for sub, label, d in runs:
        m = re.match(r"m1_L(\d)_N8_lam0_T0$", label)
        if m and sub == "scf":
            run = load_json(os.path.join(d, "run.json"))
            gaps[int(m.group(1))] = run["ksGap"]
    if len(gaps) >= 3 and all(isinstance(gaps.get(k), float) for k in (2, 3, 4)):
        reg.check("rust_L_convergence_trend", abs(gaps[4] - gaps[3]) < abs(gaps[3] - gaps[2]),
                  "KS gap of the free N = 8 state: L=2 %.8f, L=3 %.8f, L=4 %.8f" % (gaps[2], gaps[3], gaps[4]))
    else:
        reg.comparison("rust_L_convergence_trend", "not run", "free N = 8 runs at L = 2, 3, 4 not all present: %s" % sorted(gaps))


def select_reproductions(runs, max_count, quick):
    """Pick a representative subset of Rust runs to reproduce."""
    wanted = []
    def add(pred):
        for item in runs:
            sub, label, d = item
            if pred(sub, label) and item not in wanted:
                wanted.append(item)
    add(lambda s, l: s == "scf" and re.match(r"m1_L3_N8_lam(0|p1|m1)_T0$", l))
    add(lambda s, l: s == "excited" and re.match(r"m1_L3_N8_lam0_T0$", l))
    add(lambda s, l: s == "thermo" and re.match(r"m1_L3_N8_lam0_T0p1$", l))
    add(lambda s, l: s == "scf" and re.match(r"m1_L3_N\d+_lam0_T0$", l) and "N8_" not in l)
    add(lambda s, l: s == "scf" and re.match(r"m1_L3_N8_lam(p2|m2)_T0$", l))
    add(lambda s, l: s == "thermo" and re.match(r"m1_L3_N8_lamp1_T0p3$", l))
    add(lambda s, l: s == "scf" and re.match(r"m3_L3_N8_lam0_T0$", l))
    add(lambda s, l: s == "scf" and re.match(r"m1_L[24]_N8_lam0_T0$", l))
    add(lambda s, l: s == "scf" and "a4" in l)
    add(lambda s, l: s == "scf" and re.match(r"m1_L3_N\d+_lamp1_T0$", l) and "N8_" not in l)
    add(lambda s, l: s == "emt")
    add(lambda s, l: True)
    if quick:
        max_count = min(max_count, 3)
    return wanted[:max_count]


def reproduce_rust_run(reg: Registry, sub, label, d, quick):
    run = load_json(os.path.join(d, "run.json"))
    p = run["parameters"]
    N0 = 32 if quick else 50
    levels = 2 if quick else 3
    delta_k = p["deltaKOverM"] * p["m"]
    params = KS.Params(m=p["m"], a4=p["a4_0"], L=p["L"], lambda_hat=p["lambdaHat"], T=p["T"], N=p["N"],
                       parity=0, tip="g0", xc="quadratic", delta_k=delta_k, ell=p["ell"], N0=N0, levels=levels,
                       label="repro-" + label)
    name = "rust_%s_%s" % (sub, label)
    try:
        ref = KS.SectorRun(params)
    except Exception as error:  # noqa: BLE001
        reg.comparison(name, "failed", "reference solver failed: %s" % error)
        return
    res = {"label": label, "sub": sub, "parameters": p, "referenceN0": N0, "referenceLevels": levels,
           "referenceConverged": ref.converged}
    # scalars
    e_ref = float(ref.scalars["total"])
    res["E0"] = {"rust": run["energy"], "reference": e_ref, "relative": rel(run["energy"], e_ref)}
    res["mu"] = {"rust": run["mu"], "reference": float(ref.scalars["mu"]),
                 "difference": abs(run["mu"] - float(ref.scalars["mu"]))}
    res["entropy"] = {"rust": run["entropy"], "reference": float(ref.scalars["entropy"]),
                      "difference": abs(run["entropy"] - float(ref.scalars["entropy"]))}
    res["free"] = {"rust": run["freeEnergy"], "reference": float(ref.scalars["free"]),
                   "relative": rel(run["freeEnergy"], float(ref.scalars["free"]))}
    gap_rust = run.get("ksGap")
    res["ksGap"] = {"rust": gap_rust, "reference": ref.gap,
                    "difference": (abs(gap_rust - ref.gap) if isinstance(gap_rust, float) and ref.gap is not None else None)}
    # eigenvalues by (n2, parity, s)
    lhdr, lev = read_csv(os.path.join(d, "levels.csv"))
    fine = ref.levels[-1]["spectrum"]
    lo, hi = fine.eps_lo, fine.eps_hi
    mine = {}
    for key in ref.state_keys:
        q, par, typ, idx = key
        mine.setdefault((q, par, typ), []).append(float(ref.state_eps[key][1]))
    max_dev = 0.0
    unmatched = 0
    compared = 0
    flip_dev = 0.0
    for row in lev:
        rec = dict(zip(lhdr, row))
        eps = rec["eps"]
        if not (lo + 1e-9 <= eps <= hi - 1e-9):
            continue
        cand = mine.get((int(rec["n2"]), int(rec["parity"]), int(rec["s"])), [])
        cand_flip = mine.get((int(rec["n2"]), int(rec["parity"]), -int(rec["s"])), [])
        compared += 1
        best = min((abs(eps - e) for e in cand), default=float("inf"))
        best_flip = min((abs(eps - e) for e in cand_flip), default=float("inf"))
        flip_dev = max(flip_dev, min(best_flip, 1.0))
        if best > 0.05 * max(1.0, abs(eps)):
            unmatched += 1
        else:
            max_dev = max(max_dev, best)
    res["eigenvalues"] = {"compared": compared, "unmatched": unmatched, "maxAbsDeviation": max_dev,
                          "maxDeviationWithFlippedBlockSign": flip_dev,
                          "window": [lo, hi], "blockSignMapping": "rust s == reference type"}
    # profiles at common y (Rust uniform grid vs reference coarse grid)
    ppath = os.path.join(d, "profiles.csv")
    prof_dev = {}
    if os.path.exists(ppath):
        phdr, prof = read_csv(ppath)
        y_r = column(phdr, prof, "y")
        y_m = ref.coarse_grid.y
        idx = []
        for j, ym in enumerate(y_m):
            i = int(np.argmin(np.abs(y_r - ym)))
            if abs(y_r[i] - ym) < 1e-9:
                idx.append((i, j))
        if idx:
            ir = [a for a, _ in idx]
            im = [b for _, b in idx]
            for rname, mname in (("n_c", "n_c"), ("S_c", "s_c"), ("M_eff", "m_eff_out"), ("v_x", "v_out"),
                                 ("rho", "rho"), ("p_y", "p_y"), ("p_3", "p_3"), ("p_t", "p_t")):
                a = column(phdr, prof, rname)[ir]
                b = np.asarray(ref.profiles[mname])[im]
                scale = max(float(np.max(np.abs(a))), float(np.max(np.abs(b))), 1e-300)
                prof_dev[rname] = float(np.max(np.abs(a - b)) / scale) if scale > 1e-300 else 0.0
            prof_dev["commonPoints"] = len(idx)
    res["profiles"] = prof_dev
    # EMT averages
    e_r = run["emt"]
    res["emt"] = {"rhoAvg": {"rust": e_r["rhoAvg"], "reference": float(ref.emt["averages"]["rho"])},
                  "pYAvg": {"rust": e_r["pYAvg"], "reference": float(ref.emt["averages"]["p_y"])},
                  "p3Avg": {"rust": e_r["p3Avg"], "reference": float(ref.emt["averages"]["p_3"])},
                  "pTAvg": {"rust": e_r["pTAvg"], "reference": float(ref.emt["averages"]["p_t"])},
                  "braneFraction": {"rust": e_r["braneFraction_within_1_over_H"],
                                    "reference": float(ref.emt["braneLocalisedFraction"])}}
    emt_dev = 0.0
    scale = max(abs(e_r["rhoAvg"]), abs(float(ref.emt["averages"]["rho"])), 1e-300)
    for k, v in res["emt"].items():
        if k == "braneFraction":
            emt_dev = max(emt_dev, abs(v["rust"] - v["reference"]))
        else:
            emt_dev = max(emt_dev, abs(v["rust"] - v["reference"]) / scale)
    res["emtMaxDeviation"] = emt_dev
    # verdicts
    ok = (res["E0"]["relative"] < TOL["rustEnergy"] and res["mu"]["difference"] < TOL["rustEnergy"] * max(1.0, abs(run["mu"]))
          and res["free"]["relative"] < TOL["rustEnergy"] and res["entropy"]["difference"] < TOL["rustEntropy"] * max(1.0, abs(run["entropy"]))
          and unmatched == 0 and max_dev < TOL["rustEps"] * (1.0 + abs(hi))
          and all(v < TOL["rustProfile"] for k, v in prof_dev.items() if k != "commonPoints")
          and emt_dev < TOL["rustEMT"])
    if isinstance(gap_rust, float) and ref.gap is not None:
        ok = ok and abs(gap_rust - ref.gap) < TOL["rustEnergy"] * max(1.0, abs(gap_rust))
    reg.check(name + "_agreement", ok,
              "E0 rel %.2e, mu %.2e, eps max %.2e (%d compared, %d unmatched), profiles %s, emt %.2e"
              % (res["E0"]["relative"], res["mu"]["difference"], max_dev, compared, unmatched,
                 {k: ("%.1e" % v if isinstance(v, float) else v) for k, v in prof_dev.items()}, emt_dev))
    # excited: Delta-SCF
    if sub == "excited":
        ex_summary = load_json(os.path.join(os.path.dirname(d), "summary.json"))
        rec = next((r for r in ex_summary.get("runs", []) if r.get("label") == label), None)
        if rec is not None and params.T <= 0:
            try:
                ds = KS.delta_scf(ref)
            except Exception as error:  # noqa: BLE001
                ds = {"available": False, "reason": str(error)}
            res["deltaSCF"] = {"rust": rec.get("deltaScf"), "reference": ds.get("deltaSCF"), "available": ds.get("available")}
            if ds.get("available") and isinstance(rec.get("deltaScf"), float):
                dev = abs(rec["deltaScf"] - ds["deltaSCF"]) / max(abs(rec["deltaScf"]), 1e-300)
                reg.check(name + "_deltaSCF", dev < TOL["rustDeltaSCF"],
                          "rust %.10g vs reference %.10g (relative %.2e)" % (rec["deltaScf"], ds["deltaSCF"], dev))
            else:
                reg.comparison(name + "_deltaSCF", "not run", "Delta-SCF unavailable: %s" % ds.get("reason"))
    # thermo: C_V
    if sub == "thermo" and params.T > 0:
        th_summary = load_json(os.path.join(os.path.dirname(d), "summary.json"))
        rec = next((r for r in th_summary.get("runs", []) if r.get("label") == label), None)
        if rec is not None and isinstance(rec.get("heatCapacity"), float):
            try:
                point = KS.thermo_point(params, params.T)
                cv_ref = point["C_V"]
                dev = abs(rec["heatCapacity"] - cv_ref) / max(abs(cv_ref), 1e-300)
                res["C_V"] = {"rust": rec["heatCapacity"], "reference": cv_ref, "relative": dev}
                reg.check(name + "_CV", dev < TOL["rustCV"], "rust %.8g vs reference %.8g (relative %.2e)"
                          % (rec["heatCapacity"], cv_ref, dev))
            except Exception as error:  # noqa: BLE001
                reg.comparison(name + "_CV", "failed", str(error))
    reg.comparison(name, "ran", json.dumps(KS.jsonable(res))[:2000])
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
                differing.append(f + " (missing)")
                continue
            compared += 1
            if sha256_file(a) != sha256_file(b):
                differing.append(sub + "/" + f)
    reg.check("rust_repeat_byte_identity", compared > 0 and not differing,
              "%d files compared, differing: %s" % (compared, differing[:10]))


def check_refined(reg: Registry, rust_dir, refined_dir, runs):
    if not refined_dir or not os.path.isdir(refined_dir):
        reg.comparison("rust_refined_convergence", "not run", "no --refined directory")
        return
    worst_e = 0.0
    worst_eps = 0.0
    count = 0
    for sub, label, d in runs:
        d2 = os.path.join(refined_dir, sub, label)
        if not os.path.exists(os.path.join(d2, "run.json")):
            continue
        r1 = load_json(os.path.join(d, "run.json"))
        r2 = load_json(os.path.join(d2, "run.json"))
        worst_e = max(worst_e, rel(r1["energy"], r2["energy"]))
        count += 1
        l1 = os.path.join(d, "levels.csv")
        l2 = os.path.join(d2, "levels.csv")
        if os.path.exists(l1) and os.path.exists(l2):
            h1, a = read_csv(l1)
            h2, b = read_csv(l2)
            if a.shape == b.shape:
                worst_eps = max(worst_eps, float(np.max(np.abs(column(h1, a, "eps") - column(h2, b, "eps")))))
    reg.check("rust_refined_convergence", count > 0 and worst_e < TOL["refinedEnergy"] and worst_eps < TOL["refinedEps"],
              "%d runs: max relative energy difference %.3e, max eigenvalue difference %.3e" % (count, worst_e, worst_eps))


# ---------------------------------------------------------------------------
# C. exact theory JSON
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
    parser.add_argument("--max-reproductions", type=int, default=10)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--no-reproduce", action="store_true")
    parser.add_argument("--no-stationarity", action="store_true")
    args = parser.parse_args(argv)
    reg = Registry()
    sources = {}

    summary = check_reference(reg, args.reference, args)
    if summary is not None:
        sources["referenceSummary"] = sha256_file(os.path.join(args.reference, "reference-summary.json"))
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
        runs = rust_run_dirs(args.rust, summaries)
        check_rust_internal(reg, args.rust, summaries, runs)
        if args.no_reproduce:
            reg.comparison("rust_reproduction", "not run", "--no-reproduce")
        else:
            chosen = select_reproductions(runs, args.max_reproductions, args.quick)
            reg.measure("rustReproductions", ["%s/%s" % (s, l) for s, l, _ in chosen])
            for sub, label, d in chosen:
                print("reproducing %s/%s" % (sub, label), flush=True)
                reproduce_rust_run(reg, sub, label, d, args.quick)
        check_repeat(reg, args.rust, args.repeat, summaries)
        check_refined(reg, args.rust, args.refined, runs)
    else:
        reg.comparison("rust_outputs", "not run", "no Rust summaries under %s" % args.rust)

    failed = [n for n, ok in reg.checks.items() if not ok]
    for name, ok in reg.checks.items():
        print("check_%s=%s" % (name, "true" if ok else "false"))
    for name, value in reg.measurements.items():
        if not name.endswith("_detail"):
            print("measurement_%s=%r" % (name, value))
    print("check_count=%d" % len(reg.checks))
    print("failed_check_count=%d" % len(failed))
    for name in failed:
        print("FAILED %s: %s" % (name, reg.measurements.get(name + "_detail", "")))
    report = {"schemaVersion": 1, "producer": PRODUCER, "tolerances": TOL, "checks": reg.checks,
              "measurements": reg.measurements, "comparisons": reg.comparisons, "sourceSha256": sources,
              "checkCount": len(reg.checks), "failedCheckCount": len(failed), "failed": failed}
    os.makedirs(os.path.dirname(args.report), exist_ok=True)
    with open(args.report, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(KS.jsonable(report), indent=2) + "\n")
    print("report: %s" % args.report)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
