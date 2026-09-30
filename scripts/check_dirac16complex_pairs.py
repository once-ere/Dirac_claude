#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Checker of the Stage-5 {+M, -M} Kohn-Sham pairs (STAGE5_SPEC T4).

Inputs (all optional; an absent input is recorded as a comparison that did
not run, never as a passing check):

  --reference DIR    outputs of scripts/ks_reference_pairs.py
                     (default artifacts/dirac16complex/pair-creation/reference)
  --rust DIR         outputs of the Rust `pairs` subcommand
                     (default artifacts/dirac16complex/pair-creation/rust): every
                     directory below DIR that holds a run.json with a
                     "parameters" block is one run; runs are identified by their
                     PARAMETERS (statistics, sign of m, tip bag, |m|, L, N,
                     lambda_hat, T), never by the label string
  --theory PATH      artifacts/dirac16complex/pair-creation/pairing-theory.json
  --repeat DIR       a second Rust pairs tree: byte identity of every file
  --refined DIR      a Rust pairs tree produced with tightened tolerances
  --stage4-rerun DIR Stage-4 reference runs re-executed with the Stage-5 solver
                     (ks_reference_solver.py --config ... --output DIR): byte
                     identity with artifacts/dirac16complex/kohn-sham/reference/<label>/
  --report PATH      default artifacts/dirac16complex/pair-creation/python-pairs-check-report.json

What is checked (each printed as check_<name>=true|false):

  reference  presence and completeness of the matrix; every plus and minus run
             converged; N conservation, no particle/sea branch overlap, energy
             from rho, EMT trace identity (Stage-4 internal identities).
  pairing    (both solvers) plus universe (m, g(-L) = 0) versus the minus universe
             of the exact map (-m, f(-L) = 0, the same lambda and statistics):
             every level (q, p, s, index) has the partner (q, -p, -s, index) with
             the same eigenvalue, branch and occupation; E, F, S, mu, KS gap,
             particle-hole excitations, Delta-SCF, nTotal equal; scalarCharge
             opposite; profiles n_c, n_p, v_x, rho, p_y, p_3, p_t, L_s equal,
             S_c, S_p, M_eff opposite; EMT averages equal, <S_p> opposite;
             brane/tip fractions equal; thermodynamics (E, F, S, mu, C_V) equal.
             Tolerances: the reference accuracy budget of the Stage-4 checker
             (TOL of check_dirac16complex_kohn_sham.py; the -M run is an
             independent discretisation, see below) resp. the Rust solver
             precision (RUST_PAIR_TOL, the measured Stage-4 tolerance-refinement
             level); plus the grid convergence of the reference pairing defect
             (the staggered grid is mapped onto the scheme with the two grids
             exchanged, so the defect is a discretisation error that falls like
             h^2 level by level and is removed by the extrapolation).
  lambdaSign the ordinary KS problem with -lambda does NOT pair: plus(+lambda)
             versus minus(-lambda) differ (pairing-theory T3 whatMustTransform).
  control    untransformed tip bag (-m, g(-L) = 0): the k = 0 spectra of plus,
             minus and control against the analytic box spectra (the control's
             mixed sector tan(pL) = +p/|m| with the sub-gap bound state
             tanh(kappa L) = kappa/|m|, plus/minus tan(pL) = -p/|m| without it);
             the tip-localised zero mode (brane/tip density ratio e^{-2|m|L}
             against e^{+2|m|L}); the KS gap, energies and levels differ from the
             plus universe; the first-order zero-mode splitting c_ctrl against
             c(M) (computed here with the imported solver at small k, compared
             with the closed forms of pairing-theory.json); the SCF status of
             the interacting controls is recorded.
  totals     (both solvers) the pair totals of pairing-theory.json: mirror pair
             (plus + minus: 2E, 2N, S = 0, 2<rho>, 2<p>) and Krein-image pair
             (plus - minus for every one-body density and energy: E = 0,
             charge 0, <rho> = <p> = 0, S = 2<S_p>).
  statistics lambda = 0 runs identical for both fields (bytes of the tables,
             numbers of run.json); exact potential identities M_eff - m =
             (1 + sg/16) lambda S_p, v_x = sg lambda n_p/16 on every profile;
             first-order (odd-in-lambda) parts: exchange energy
             E_x/lambda -> sg A_x and Hartree energy E_H/lambda -> A_H with
             A_H = (V/2) int S_p^2 dV_p, A_x = (V/32) int (n_p^2 + S_p^2) dV_p of
             the lambda = 0 state; dE/dlambda = A_H + sg A_x (so
             D_+ - D_- = 2 A_x, D_+ + D_- = 2 A_H: the -1/32 vs +1/32 exchange);
             the odd part of M_eff - m in the ratio 17/15 and of v_x in the
             ratio -1 (15/16 vs 17/16, -1/16 vs +1/16); N = 8: mu -> sg A_x/4
             lambda.  The O(lambda_hat_1^2) truncation is measured from the
             lambda_hat_2 runs.
  rust       Rust vs reference per run (Stage-4 tolerances and rules: the
             lambda_hat correction dl, the Rust f_cut window correction at
             T > 0, the measured Rust grid uncertainty |X(601) - X(301)| of runs
             with a finer-grid partner), --repeat byte identity, --refined
             convergence.
  stage4     byte identity of the re-executed Stage-4 reference runs; every
             dirac16complex plusM run whose parameters are a committed Stage-4
             reference run reproduces it byte for byte (the plus universe IS the
             Stage-4 problem).
  theory     pairing-theory.json: the T3 checks and the numerics prescription.

Exit status 1 if any check failed.  Usage:
  python scripts/check_dirac16complex_pairs.py [--reference DIR] [--rust DIR]
         [--repeat DIR] [--refined DIR] [--stage4-rerun DIR] [--report PATH]
         [--no-solver] (skip the checker's own small solver computations)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import ks_reference_solver as KS  # noqa: E402
import check_dirac16complex_kohn_sham as C4  # noqa: E402  (tolerances and m-independent helpers only)

ART = os.path.join(REPO, "artifacts", "dirac16complex", "pair-creation")
DEFAULT_REFERENCE = os.path.join(ART, "reference")
DEFAULT_RUST = os.path.join(ART, "rust")
DEFAULT_THEORY = os.path.join(ART, "pairing-theory.json")
DEFAULT_REPORT = os.path.join(ART, "python-pairs-check-report.json")
STAGE4_REFERENCE = os.path.join(REPO, "artifacts", "dirac16complex", "kohn-sham", "reference")
PRODUCER = "scripts/check_dirac16complex_pairs.py"
SUMMARY_NAME = "reference-pairs-summary.json"

TOL = C4.TOL                  # the Stage-4 accuracy budget (reference vs Rust), used for the reference pairing
RUST_PAIR_TOL = {             # Rust pairing "to solver precision": the Stage-4 refined-tolerance level (6e-8 measured)
    "eps": 1e-7,              # |d eps| <= eps max(1, |eps|/|m|) |m|
    "energy": 1e-7,           # |dE| <= energy max(|E|, N |m|)
    "scalar": 1e-7,           # mu, gap, Delta-SCF, particle-hole: |d| <= scalar max(|m|, |x|)
    "profile": 1e-6,          # max |d profile| / profile scale (all nodes)
    "emtAverage": 1e-6,       # relative to max(|<rho>|, |<p_y>|, |<p_3>|)
    "fraction": 1e-7,         # brane / tip fractions (absolute)
    "entropy": 1e-7,          # |dS| <= entropy max(S, N)
}
POTENTIAL_IDENTITY_TOL = 1e-9   # M_eff - m = (1 + sg/16) lambda S_p, v_x = sg lambda n_p/16 (relative to the scale)
CONTROL_MIN_RATIO = 100.0       # the control must differ from the plus universe by > 100 x the pairing tolerance
WINDOW_EDGE_MARGIN = 0.02       # levels within 0.02 |m| of the common window edges are not compared (see match_levels)
FIELDS = ("d16c", "d16c00")
FIELD_SIGN = {"d16c": -1, "d16c00": 1}
STAT_OF = {"anticommuting": "d16c", "commuting": "d16c00", "dirac16complex": "d16c",
           "dirac16complex00": "d16c00"}
LAMBDA_NAMES = ("lam0", "lamp1", "lamm1", "lamp2", "lamm2")
# universe names of the outputs (Rust pairs.rs and ks_reference_pairs.py) -> the short internal names
UNIVERSE_SHORT = {"plusM": "plus", "minusM": "minus", "minusM_control": "control",
                  "plus": "plus", "minus": "minus", "control": "control"}
ODD_PAIRS = (("lamp1", "lamm1"), ("lamp2", "lamm2"))


def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


read_csv = C4.read_csv
column = C4.column
is_num = C4.is_num


def rel_path(path):
    return os.path.relpath(path, REPO).replace(os.sep, "/")


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

    def check_or_not_run(self, name, count, ok, detail):
        if count > 0:
            return self.check(name, ok, detail)
        self.comparison(name, "not run", detail)
        return None


class Worst:
    """Largest ratio deviation/tolerance per quantity, with location and failures."""

    def __init__(self):
        self.data = {}

    def add(self, quantity, where, deviation, tolerance, detail=""):
        if deviation is None or not math.isfinite(deviation):
            entry = self.data.setdefault(quantity, {"count": 0, "failures": [], "ratio": 0.0, "deviation": 0.0,
                                                    "tolerance": tolerance, "where": None, "detail": ""})
            entry["count"] += 1
            entry["failures"].append(where + " (non-finite)")
            entry["ratio"] = float("inf")
            return
        ratio = deviation / tolerance if tolerance > 0 else (0.0 if deviation == 0 else float("inf"))
        cur = self.data.get(quantity)
        entry = cur or {"count": 0, "failures": []}
        entry["count"] += 1
        if cur is None or ratio > cur["ratio"]:
            entry.update({"ratio": ratio, "deviation": deviation, "tolerance": tolerance, "where": where,
                          "detail": detail})
        if ratio > 1.0:
            entry["failures"].append(where)
        self.data[quantity] = entry

    def report(self, reg, prefix, descriptions):
        for quantity, entry in sorted(self.data.items()):
            reg.check(prefix + quantity, entry["ratio"] <= 1.0,
                      "%s; %d comparisons, worst %.3e (tolerance %.3e, ratio %.3g) at %s %s; failures: %s"
                      % (descriptions.get(quantity, quantity), entry["count"], entry["deviation"],
                         entry["tolerance"], entry["ratio"], entry["where"], entry.get("detail", ""),
                         entry["failures"][:8]))
            reg.measure("worstRatio_" + prefix + quantity, entry["ratio"])


# ---------------------------------------------------------------------------
# loading: reference pairs runs
# ---------------------------------------------------------------------------

def t_over_m_key(t, m_abs):
    return round(float(t) / float(m_abs), 9)


def ref_key(doc):
    """(field, universe, |m|, N, lambda name, T/|m|) of a reference pairs run.json."""
    pr = doc.get("pairs") or {}
    p = doc["params"]
    return (pr.get("field"), UNIVERSE_SHORT.get(pr.get("universe"), pr.get("universe")), abs(float(p["m"])),
            float(p["N"]), doc.get("lambdaName"), t_over_m_key(p["T"], abs(float(p["m"]))))


class RefRun:
    """A reference pairs run: run.json, its tables and derived quantities."""

    def __init__(self, directory):
        self.dir = directory
        self.doc = load_json(os.path.join(directory, "run.json"))
        self.params = self.doc["params"]
        self.label = self.params.get("label", os.path.basename(directory))
        self.m = float(self.params["m"])
        self.ms = abs(self.m)
        self.N = float(self.params["N"])
        self.T = float(self.params["T"])
        self.key = ref_key(self.doc)
        self.shdr, self.spec = read_csv(os.path.join(directory, "spectrum.csv"))
        self.phdr, self.prof = read_csv(os.path.join(directory, "profiles.csv"))
        self.sg = FIELD_SIGN.get(self.key[0], -1)
        self.lam = float(self.params["lambda"])
        self.lambda_hat = float(self.params["lambda_hat"])

    def p(self, name):
        return column(self.phdr, self.prof, name)

    def levels(self):
        """{(q, parity, type, index): row dict} of spectrum.csv."""
        idx = {h: i for i, h in enumerate(self.shdr)}
        out = {}
        for row in self.spec:
            key = (int(row[idx["q"]]), int(row[idx["parity"]]), int(row[idx["type"]]), int(row[idx["index"]]))
            out[key] = {h: row[i] for h, i in idx.items()}
        return out

    def converged(self):
        return bool(self.doc.get("converged"))

    def converged_by(self):
        return (self.doc.get("levels") or [{}])[-1].get("convergedBy")

    def ext(self, name):
        return (self.doc.get("extrapolated") or {}).get(name)


def load_reference(ref_dir):
    """(summary or None, {key: RefRun}, problems); run directories <config>/<universe>/."""
    runs = {}
    problems = []
    summary = None
    spath = os.path.join(ref_dir, SUMMARY_NAME)
    if os.path.exists(spath):
        summary = load_json(spath)
    if not os.path.isdir(ref_dir):
        return summary, runs, ["reference directory %s absent" % ref_dir]
    dirs = []
    for root, _subdirs, files in os.walk(ref_dir):
        if "run.json" in files:
            dirs.append(root)
    for d in sorted(dirs):
        entry = rel_path(d)
        try:
            run = RefRun(d)
        except Exception as error:  # noqa: BLE001
            problems.append("%s: %r" % (entry, error))
            continue
        if run.doc.get("failed"):
            problems.append("%s: failed %s" % (entry, run.doc.get("failed")))
            continue
        runs[run.key] = run
    return summary, runs, problems


# ---------------------------------------------------------------------------
# a common view of one run (reference or Rust) for the pairing comparisons
# ---------------------------------------------------------------------------

PROFILE_FLIP = {"n_c": 1, "n_p": 1, "v_x": 1, "rho": 1, "p_y": 1, "p_3": 1, "p_t": 1, "L_s": 1,
                "S_c": -1, "S_p": -1, "M_eff": -1}
PROFILE_GROUP = {"n_c": ("n_c", "S_c"), "S_c": ("n_c", "S_c"), "n_p": ("n_p", "S_p"), "S_p": ("n_p", "S_p"),
                 "M_eff": ("M_eff",), "v_x": ("v_x",), "rho": ("rho", "p_y", "p_3", "p_t"),
                 "p_y": ("rho", "p_y", "p_3", "p_t"), "p_3": ("rho", "p_y", "p_3", "p_t"),
                 "p_t": ("rho", "p_y", "p_3", "p_t"), "L_s": ("rho", "p_y", "p_3", "p_t", "L_s")}


class RefView:
    """Uniform accessors of a reference run (RefRun)."""
    solver = "reference"

    def __init__(self, run: RefRun):
        self.run = run
        self.label = run.label
        self.m, self.ms, self.N, self.T = run.m, run.ms, run.N, run.T
        self.lam, self.sg, self.key = run.lam, run.sg, run.key
        self._groups = None

    def converged(self):
        return self.run.converged()

    def smearing(self):
        return float(self.run.params.get("occupationSmearing") or 0.0)

    @property
    def dir(self):
        return self.run.dir

    def doc(self):
        return self.run.doc

    def table_files(self):
        return sorted(f for f in os.listdir(self.run.dir) if f.endswith(".csv"))

    def volume(self):
        return float(self.run.params["volume"])

    def converged_by(self):
        return self.run.converged_by()

    def level_groups(self):
        """{(q, parity, type): [level dicts sorted by eps]} with eps, branch, f, mult, index, epsLevels."""
        if self._groups is None:
            hdr, spec = self.run.shdr, self.run.spec
            idx = {h: i for i, h in enumerate(hdr)}
            lvl_cols = [c for c in hdr if c.startswith("eps_level")]
            groups = {}
            for row in spec:
                g = (int(row[idx["q"]]), int(row[idx["parity"]]), int(row[idx["type"]]))
                groups.setdefault(g, []).append({
                    "eps": float(row[idx["eps_extrapolated"]]), "branch": int(row[idx["branch"]]),
                    "f": float(row[idx["f"]]), "mult": float(row[idx["mult"]]), "index": int(row[idx["index"]]),
                    "epsLevels": [float(row[idx[c]]) for c in lvl_cols]})
            for g in groups.values():
                g.sort(key=lambda d: (d["eps"], d["index"]))
            self._groups = groups
        return self._groups

    def index_map(self, key):
        """Image of a level key (q, p, s, index) under the exact map (reference: rank index kept)."""
        q, p, s, i = key
        return (q, -p, -s, i)

    def scalar(self, name):
        d = self.run.doc
        ext = d.get("extrapolated") or {}
        th = d.get("thermo") or {}
        ex = d.get("excited") or {}
        if name in ("E", "F", "S", "mu") and th:
            return th.get({"E": "energy", "F": "free", "S": "entropy", "mu": "mu"}[name])
        table = {"E": "total", "F": "free", "S": "entropy", "mu": "mu", "nTotal": "nTotal",
                 "scalarCharge": "scalarCharge", "hartree": "hartree", "exchange": "exchange",
                 "interaction": "interaction"}
        if name in table:
            return ext.get(table[name])
        if name == "ksGap":
            return d.get("ksGap")
        if name == "deltaSCF":
            ds = ex.get("deltaSCF") or {}
            return ds.get("deltaSCF") if ds.get("available") else None
        if name == "lowestParticleHole":
            ph = self.particle_hole()
            return ph[0] if ph else None
        if name in ("C_V_fd", "C_V_fixedSpectrum", "C_V_fixedSpectrumEntropy"):
            return th.get(name)
        return None

    def particle_hole(self):
        d = self.run.doc
        if d.get("thermo"):
            # T > 0: the finite-T excitation list (holes f >= 1/2, particles f < 1/2; thermo_point, 8 entries)
            return [x["excitation"] for x in (d["thermo"].get("excitations") or [])]
        return [x["excitation"] for x in ((d.get("excited") or {}).get("particleHole") or [])]

    def y(self):
        return self.run.p("y")

    def profile(self, name):
        return self.run.p(name) if name in self.run.phdr else None

    def emt(self, name):
        e = self.run.doc.get("emt") or {}
        if name in ("rho", "p_y", "p_3", "p_t", "s_p", "n_p", "L_s"):
            return (e.get("averages") or {}).get(name)
        if name == "braneFraction":
            return e.get("braneLocalisedFraction")
        if name == "tipFraction":
            return e.get("tipLocalisedFraction")
        if name == "energyFromRho":
            return e.get("energyFromRho")
        if name == "lambdaSAvgOverM":
            return (e.get("E41_sourcingConditions") or {}).get("lambdaSAvgOverM")
        return None

    def grid_level_energies(self):
        return [lv["energies"]["total"] for lv in (self.run.doc.get("levels") or [])]


def fmax(values):
    values = [abs(float(v)) for v in values if v is not None and is_num(v)]
    return max(values) if values else 0.0


def pair_tolerances(kind):
    """Tolerance functions of the pairing comparison: kind 'reference' (Stage-4 budget) or 'rust'."""
    if kind == "reference":
        return {"eps": lambda e, ms: TOL["eps"] * max(1.0, abs(e) / ms) * ms,
                "energy": lambda x, N, ms: TOL["energy"] * max(abs(x), N * ms),
                "scalar": lambda x, ms: TOL["scalar"] * max(ms, abs(x)),
                "profileInterior": TOL["profileInterior"], "profileEnd": TOL["profileEnd"],
                "emtAverage": TOL["emtAverage"], "fraction": TOL["fraction"],
                "entropy": lambda x, N: TOL["entropy"] * max(abs(x), N),
                "cvFd": TOL["cvFd"], "cvFixed": TOL["cvFixed"]}
    return {"eps": lambda e, ms: RUST_PAIR_TOL["eps"] * max(1.0, abs(e) / ms) * ms,
            "energy": lambda x, N, ms: RUST_PAIR_TOL["energy"] * max(abs(x), N * ms),
            "scalar": lambda x, ms: RUST_PAIR_TOL["scalar"] * max(ms, abs(x)),
            "profileInterior": RUST_PAIR_TOL["profile"], "profileEnd": RUST_PAIR_TOL["profile"],
            "emtAverage": RUST_PAIR_TOL["emtAverage"], "fraction": RUST_PAIR_TOL["fraction"],
            "entropy": lambda x, N: RUST_PAIR_TOL["entropy"] * max(abs(x), N),
            "cvFd": 10 * RUST_PAIR_TOL["energy"], "cvFixed": 10 * RUST_PAIR_TOL["energy"]}


def match_levels(P, M, tol_eps, use_index):
    """Pair every level of P with its image in M: group (q, p, s) -> (q, -p, -s);
    with use_index the rank index is required to map as P.index_map says,
    otherwise the nearest eigenvalue in the image group.  Only levels inside
    the common window with a margin WINDOW_EDGE_MARGIN |m| are compared: each
    run's energy window follows its own mu on every grid level, so a level
    within a grid error of a window edge can be listed on one side only
    (such edge levels are deep sea levels of weight 0 or empty particle
    levels at T = 0, Fermi tails e^{-32} at T > 0).  Returns (pairs
    [(lp, lm)], unmatched count, compared count)."""
    gP, gM = P.level_groups(), M.level_groups()
    all_p = [d["eps"] for g in gP.values() for d in g]
    all_m = [d["eps"] for g in gM.values() for d in g]
    if not all_p or not all_m:
        return [], 0, 0
    lo = max(min(all_p), min(all_m)) + WINDOW_EDGE_MARGIN * P.ms
    hi = min(max(all_p), max(all_m)) - WINDOW_EDGE_MARGIN * P.ms
    pairs, unmatched, compared = [], 0, 0
    for (q, p, s), levels in gP.items():
        image = gM.get((q, -p, -s), [])
        by_index = {d["index"]: d for d in image}
        for lp in levels:
            if not lo <= lp["eps"] <= hi:
                continue
            compared += 1
            if use_index:
                lm = by_index.get(P.index_map((q, p, s, lp["index"]))[3])
            elif image:
                lm = min(image, key=lambda d: abs(d["eps"] - lp["eps"]))
                if abs(lm["eps"] - lp["eps"]) > max(1e-2 * max(1.0, abs(lp["eps"]) / P.ms) * P.ms,
                                                    100.0 * tol_eps(lp["eps"], P.ms)):
                    lm = None
            else:
                lm = None
            if lm is None:
                unmatched += 1
                continue
            pairs.append((lp, lm))
    return pairs, unmatched, compared


def profile_scale(view, names):
    vals = [view.profile(n) for n in names]
    vals = [v for v in vals if v is not None]
    return max((float(np.max(np.abs(v))) for v in vals), default=0.0)


def compare_pair(worst, where, P, M, kind, record):
    """The pairing identities between a plus run P and its minus image M."""
    tol = pair_tolerances(kind)
    ms, N, T = P.ms, P.N, P.T
    t_occ = max(T, P.smearing())
    pairs, unmatched, compared = match_levels(P, M, tol["eps"], use_index=(P.solver == "reference"))
    branch_bad = occ_bad = mult_bad = 0
    max_de = 0.0
    for lp, lm in pairs:
        de = abs(lp["eps"] - lm["eps"])
        te = tol["eps"](lp["eps"], ms)
        max_de = max(max_de, de)
        worst.add("eigenvalues", where, de, te, "eps %.10f" % lp["eps"])
        branch_bad += int(lp["branch"] != lm["branch"])
        mult_bad += int(lp["mult"] != lm["mult"])
        f_tol = 1e-9 if t_occ <= 0.0 else te / t_occ + 1e-9
        occ_bad += int(abs(lp["f"] - lm["f"]) > f_tol)
    worst.add("levelMatching", where, float(unmatched + branch_bad + occ_bad + mult_bad) + (0.0 if compared else 1.0),
              0.5, "compared %d, unmatched %d, branch %d, occupation %d, multiplicity %d"
              % (compared, unmatched, branch_bad, occ_bad, mult_bad))
    record["levels"] = {"compared": compared, "matched": len(pairs), "unmatched": unmatched,
                        "branchMismatches": branch_bad, "occupationMismatches": occ_bad,
                        "multiplicityMismatches": mult_bad, "maxAbsEpsDeviation": max_de,
                        "matching": ("rank index kept, (q, p, s) -> (q, -p, -s)" if P.solver == "reference"
                                     else "nearest eigenvalue in the image group (q, -p, -s)")}
    sc = {}
    for name in ("E", "F", "hartree", "exchange", "interaction"):
        a, b = P.scalar(name), M.scalar(name)
        if is_num(a) and is_num(b):
            t = tol["energy"](a, N, ms)
            worst.add("energies", where + ":" + name, abs(a - b), t)
            sc[name] = {"plus": a, "minus": b, "deviation": abs(a - b), "tolerance": t}
    a, b = P.scalar("S"), M.scalar("S")
    if is_num(a) and is_num(b):
        t = tol["entropy"](a, N)
        worst.add("entropy", where, abs(a - b), t)
        sc["S"] = {"plus": a, "minus": b, "deviation": abs(a - b), "tolerance": t}
    for name in ("mu", "ksGap", "deltaSCF", "lowestParticleHole"):
        a, b = P.scalar(name), M.scalar(name)
        if is_num(a) and is_num(b):
            t = tol["scalar"](a, ms)
            worst.add("muGapExcitations", where + ":" + name, abs(a - b), t)
            sc[name] = {"plus": a, "minus": b, "deviation": abs(a - b), "tolerance": t}
        elif is_num(a) != is_num(b):
            worst.add("muGapExcitations", where + ":" + name + " (present on one side only)", float("inf"), 1.0)
    pa, pb = P.particle_hole(), M.particle_hole()
    if pa or pb:
        n = min(len(pa), len(pb))
        dev = max((abs(x - y) for x, y in zip(pa[:n], pb[:n])), default=0.0)
        t = tol["scalar"](fmax(pa[:n]), ms)
        worst.add("particleHoleList", where, dev if len(pa) == len(pb) else float("inf"), t,
                  "%d / %d excitations" % (len(pa), len(pb)))
        sc["particleHoleList"] = {"count": [len(pa), len(pb)], "maxDeviation": dev, "tolerance": t}
    a, b = P.scalar("nTotal"), M.scalar("nTotal")
    if is_num(a) and is_num(b):
        worst.add("particleNumber", where, abs(a - b), 1e-9 * max(N, 1.0))
        sc["nTotal"] = {"plus": a, "minus": b}
    a, b = P.scalar("scalarCharge"), M.scalar("scalarCharge")
    if is_num(a) and is_num(b):
        t = tol["energy"](max(abs(a), abs(b)), N, 1.0)
        worst.add("scalarChargeOpposite", where, abs(a + b), t)
        sc["scalarCharge"] = {"plus": a, "minus": b, "sum": a + b, "tolerance": t}
    for name in ("C_V_fd", "C_V_fixedSpectrum", "C_V_fixedSpectrumEntropy"):
        a, b = P.scalar(name), M.scalar(name)
        if is_num(a) and is_num(b):
            t = tol["cvFd"] if name == "C_V_fd" else tol["cvFixed"]
            worst.add("heatCapacity", where + ":" + name, abs(a - b) / max(abs(a), 1e-300), t)
            sc[name] = {"plus": a, "minus": b}
    record["scalars"] = sc
    ya, yb = P.y(), M.y()
    prof = {}
    if ya is None or yb is None or len(ya) != len(yb) or float(np.max(np.abs(ya - yb))) > 1e-12:
        worst.add("profiles", where + " (grids differ)", float("inf"), 1.0)
    else:
        ends = np.zeros(len(ya), dtype=bool)
        ends[0] = ends[-1] = True
        m_eff = P.profile("M_eff")
        v_x = P.profile("v_x")
        pseudo = max(float(np.max(np.abs(m_eff - P.m))) if m_eff is not None else 0.0,
                     float(np.max(np.abs(v_x))) if v_x is not None else 0.0)
        for name, flip in PROFILE_FLIP.items():
            a, b = P.profile(name), M.profile(name)
            if a is None or b is None:
                continue
            if name == "M_eff":
                dev = np.abs((a - P.m) + (b - M.m))
                scale = pseudo
            elif name == "v_x":
                dev = np.abs(a - b)
                scale = pseudo
            else:
                dev = np.abs(a - flip * b)
                scale = profile_scale(P, PROFILE_GROUP[name])
            if scale <= 0.0:
                # identically vanishing profile (lambda = 0 potentials): must vanish on both sides
                worst.add("profilesInterior", where + ":" + name, float(np.max(dev)), 1e-15 * ms)
                prof[name] = {"scale": 0.0, "maxAbs": float(np.max(dev))}
                continue
            d_int = float(np.max(dev[~ends]) / scale)
            d_end = float(np.max(dev[ends]) / scale)
            worst.add("profilesInterior", where + ":" + name, d_int, tol["profileInterior"])
            worst.add("profilesEnds", where + ":" + name, d_end, tol["profileEnd"])
            prof[name] = {"flip": flip, "interior": d_int, "ends": d_end, "scale": scale}
    record["profiles"] = prof
    emt = {}
    scale = max(fmax([P.emt("rho"), P.emt("p_y"), P.emt("p_3")]), 1e-300)
    for name in ("rho", "p_y", "p_3", "p_t", "L_s"):
        a, b = P.emt(name), M.emt(name)
        if is_num(a) and is_num(b):
            worst.add("emtAverages", where + ":" + name, abs(a - b) / scale, tol["emtAverage"])
            emt[name] = {"plus": a, "minus": b}
    dscale = max(fmax([P.emt("n_p"), P.emt("s_p")]), 1e-300)
    for name, flip in (("n_p", 1), ("s_p", -1)):
        a, b = P.emt(name), M.emt(name)
        if is_num(a) and is_num(b):
            worst.add("emtAverages", where + ":" + name, abs(a - flip * b) / dscale, tol["emtAverage"])
            emt[name] = {"plus": a, "minus": b}
    for name in ("braneFraction", "tipFraction"):
        a, b = P.emt(name), M.emt(name)
        if is_num(a) and is_num(b):
            worst.add("fractions", where + ":" + name, abs(a - b), tol["fraction"])
            emt[name] = {"plus": a, "minus": b}
    a, b = P.emt("energyFromRho"), M.emt("energyFromRho")
    if is_num(a) and is_num(b):
        worst.add("energies", where + ":energyFromRho", abs(a - b), tol["energy"](a, N, ms))
    a, b = P.emt("lambdaSAvgOverM"), M.emt("lambdaSAvgOverM")
    if is_num(a) and is_num(b):
        worst.add("emtAverages", where + ":lambdaSAvgOverM", abs(a - b) / max(abs(a), abs(b), 1e-300),
                  tol["emtAverage"] + 1e-12)
        emt["lambdaSAvgOverM"] = {"plus": a, "minus": b}
    record["emt"] = emt
    return pairs


def defect_convergence(pairs, P, M):
    """Reference only: the pairing defect of the eigenvalues and of E on each grid
    level and after the extrapolation (a discretisation error of the staggered
    scheme mapped onto the exchanged scheme: it falls like h^2 per level)."""
    nlev = len(pairs[0][0]["epsLevels"]) if pairs else 0
    d = [max(abs(lp["epsLevels"][lv] - lm["epsLevels"][lv]) for lp, lm in pairs) for lv in range(nlev)]
    d_ext = max((abs(lp["eps"] - lm["eps"]) for lp, lm in pairs), default=0.0)
    e_p, e_m = P.grid_level_energies(), M.grid_level_energies()
    d_e = [abs(a - b) for a, b in zip(e_p, e_m)]
    orders = [math.log2(d[lv] / d[lv + 1]) for lv in range(nlev - 1) if d[lv + 1] > 0 and d[lv] > 0]
    ea, eb = P.scalar("E"), M.scalar("E")
    return {"epsDefectPerLevel": d, "epsDefectExtrapolated": d_ext, "epsDefectOrders": orders,
            "energyDefectPerLevel": d_e,
            "energyDefectExtrapolated": abs(ea - eb) if is_num(ea) and is_num(eb) else None}


PAIR_DESCRIPTIONS = {
    "eigenvalues": "every plus level and its image (q, -p, -s): the same eigenvalue",
    "levelMatching": "every plus level in the common window has an image with the same branch, occupation, multiplicity",
    "energies": "E, F, E_H, E_x, E_int and the energy from rho equal",
    "entropy": "S equal",
    "muGapExcitations": "mu, KS gap, Delta-SCF, lowest particle-hole excitation equal",
    "particleHoleList": "the particle-hole excitation lists equal",
    "particleNumber": "nTotal equal",
    "scalarChargeOpposite": "scalarCharge(minus) = -scalarCharge(plus)",
    "heatCapacity": "C_V (central difference and fixed-spectrum forms) equal",
    "profilesInterior": "profiles on the interior nodes: n, v_x, rho, p's, L_s equal; S, M_eff opposite",
    "profilesEnds": "profiles on the two end nodes",
    "profiles": "profiles on the same grid",
    "emtAverages": "EMT proper-volume averages equal, <S_p> opposite, lambda <S>/m equal",
    "fractions": "brane and tip fractions equal",
}


def group_views(runs):
    """{(field, |m|, N, lambda, T/|m|): {universe: view}}."""
    out = {}
    for key, view in runs.items():
        field, universe, m_abs, N, lam, t = key
        out.setdefault((field, m_abs, N, lam, t), {})[universe] = view
    return out


def where_of(base):
    field, m_abs, N, lam, t = base
    return "%s_m%s_N%d_%s_T%s" % (field, KS.trim_float(m_abs), int(N), lam, "0" if t == 0 else KS.trim_float(t))


def check_reference_runs(reg, summary, runs, problems, args):
    """Completeness and the Stage-4 internal identities of the reference pairs runs."""
    reg.measure("referenceRunCount", len(runs))
    reg.measure("referenceProblems", problems)
    if summary is None:
        reg.check("reference_summary_present", False, "no %s under %s" % (SUMMARY_NAME, args.reference))
        return
    expected = [r["label"] for r in summary.get("runs", [])] + list(summary.get("pending", []))
    failed = list(summary.get("failed", []))
    failed_control = list(summary.get("failedControl", []))
    other = [lab for lab in failed if lab not in failed_control]
    not_attempted = list(summary.get("notAttempted", []))
    reg.check("reference_summary_complete", bool(summary.get("complete")) and not other
              and not summary.get("pending"),
              "every run of the matrix attempted or recorded as not attempted (complete %s, pending %d); failed "
              "plusM/minusM runs: %s" % (summary.get("complete"), len(summary.get("pending", [])), other))
    reg.measure("referenceFailedControls", {r["label"]: r.get("failed") for r in summary.get("runs", [])
                                            if r.get("label") in failed_control})
    first = (summary.get("thermoFirstOrder") or {}).get("points") or {}
    estimates = {lab: (first.get(lab) or {}).get("firstOrderPseudoPotentialOverAbsM") for lab in not_attempted}
    reg.measure("referenceNotAttempted", estimates)
    bad = [lab for lab, est in estimates.items() if not (is_num(est) and est > KS.THERMO_FIRST_ORDER_LIMIT)]
    reg.check_or_not_run("reference_not_attempted_only_outside_window", len(not_attempted), not bad,
                         "%d interacting T > 0 points not attempted, each with a first-order pseudo-potential "
                         "|lambda_hat| strength_free(T) beyond the STAGE4_SPEC section 4 window edge %g |m| "
                         "(min %.4g |m|); without such an estimate: %s"
                         % (len(not_attempted), KS.THERMO_FIRST_ORDER_LIMIT,
                            min([e for e in estimates.values() if is_num(e)], default=float("nan")), bad))
    labels = {v.label for v in runs.values()}
    missing = sorted(set(expected) - labels - set(failed) - set(not_attempted))
    reg.check("reference_all_runs_present", not missing, "%d runs expected, %d present, missing %s"
              % (len(expected), len(labels), missing[:10]))
    bad = sorted(v.label for k, v in runs.items() if k[1] in ("plus", "minus") and not v.converged())
    reg.check("reference_plus_minus_converged", not bad and bool(runs),
              "plus and minus universes: every run converged; not converged: %s" % bad)
    ctrl = {v.label: v.run.converged_by() for k, v in runs.items() if k[1] == "control"}
    reg.measure("referenceControlConvergence", {lab: ctrl[lab] for lab in sorted(ctrl)})
    worst = {"N": 0.0, "Erho": 0.0, "trace": 0.0}
    overlap = []
    for key, v in runs.items():
        if key[1] == "control" and not v.converged():
            continue
        n_tot = v.scalar("nTotal")
        if is_num(n_tot):
            worst["N"] = max(worst["N"], abs(n_tot - v.N) / v.N)
        e, er = v.run.ext("total"), v.emt("energyFromRho")
        if is_num(e) and is_num(er):
            worst["Erho"] = max(worst["Erho"], abs(er - e) / max(abs(e), 1.0))
        tr = (v.run.doc.get("emt") or {}).get("traceIdentityResidual")
        if is_num(tr):
            scale = max(1.0, fmax([v.emt("rho"), v.emt("p_y")]))
            worst["trace"] = max(worst["trace"], tr / scale)
        if any(lv.get("branchOverlap") for lv in v.run.doc.get("levels", [])):
            overlap.append(v.label)
    reg.check("reference_N_conservation", worst["N"] < TOL["referenceN"],
              "max |sum of weights - N|/N = %.3e" % worst["N"])
    reg.check("reference_energy_from_rho", worst["Erho"] < TOL["referenceEnergyRho"],
              "max |E(rho) - E|/max(|E|, 1) = %.3e" % worst["Erho"])
    reg.check("reference_emt_trace_identity", worst["trace"] < TOL["referenceTrace"],
              "max EMT trace residual / max(1, |<rho>|, |<p_y>|) = %.3e" % worst["trace"])
    reg.check("reference_no_branch_overlap", not overlap, "runs with a sea level above an occupied particle "
              "level: %s" % overlap[:10])


def check_pairing(reg, groups, kind, record_prefix):
    """plus versus minus for every parameter set present in both universes."""
    worst = Worst()
    defects = {}
    compared = []
    skipped = []
    for base in sorted(groups):
        g = groups[base]
        if "plus" not in g or "minus" not in g:
            continue
        P, M = g["plus"], g["minus"]
        where = where_of(base)
        if not (P.converged() and M.converged()):
            skipped.append(where)
            continue
        record = {"plus": P.label, "minus": M.label}
        pairs = compare_pair(worst, where, P, M, kind, record)
        if kind == "reference" and pairs:
            record["defectConvergence"] = defect_convergence(pairs, P, M)
            defects[where] = record["defectConvergence"]
        reg.comparison("pairing_%s_%s" % (kind, where), "ran", record)
        compared.append(where)
    reg.measure("pairing_%s_compared" % kind, compared)
    reg.measure("pairing_%s_skippedNotConverged" % kind, skipped)
    if not compared:
        reg.comparison("pairing_" + kind, "not run", "no plus/minus pair of converged %s runs" % kind)
        return defects
    worst.report(reg, "pairing_%s_" % kind, PAIR_DESCRIPTIONS)
    if kind == "reference":
        check_defect_convergence(reg, defects)
    return defects


def check_defect_convergence(reg, defects):
    """The reference pairing defect is a discretisation error: it falls with h level by
    level (orders near 2) and the extrapolation removes most of it."""
    monotone, not_monotone, orders = 0, [], []
    reduced, not_reduced = 0, []
    for where, d in sorted(defects.items()):
        lv = d["epsDefectPerLevel"]
        if len(lv) < 2 or max(lv) < 1e-12:
            continue
        if all(lv[i + 1] < lv[i] for i in range(len(lv) - 1)):
            monotone += 1
        else:
            not_monotone.append(where)
        orders += d["epsDefectOrders"]
        if d["epsDefectExtrapolated"] < lv[-1]:
            reduced += 1
        else:
            not_reduced.append(where)
    total = monotone + len(not_monotone)
    med = float(np.median(orders)) if orders else float("nan")
    reg.measure("pairing_reference_defectOrders_median", med)
    reg.check_or_not_run("pairing_reference_defect_falls_with_h", total, not not_monotone and 1.5 <= med <= 2.6,
                         "eigenvalue pairing defect on the grids N0, 2N0, 4N0 decreasing in %d of %d pairs, median "
                         "order %.3f (not monotone: %s)" % (monotone, total, med, not_monotone[:8]))
    reg.check_or_not_run("pairing_reference_extrapolation_reduces_defect", total, not not_reduced,
                         "extrapolated defect below the finest-grid defect in %d of %d pairs (not: %s)"
                         % (reduced, total, not_reduced[:8]))


def check_lambda_sign(reg, groups, kind):
    """The ordinary -M problem with -lambda does not pair with +M at +lambda."""
    tol = pair_tolerances(kind)
    results = {}
    fails = []
    for base in sorted(groups):
        field, m_abs, N, lam, t = base
        if lam not in ("lamp1", "lamp2"):
            continue
        partner = (field, m_abs, N, lam.replace("lamp", "lamm"), t)
        P = groups[base].get("plus")
        M = (groups.get(partner) or {}).get("minus")
        if P is None or M is None or not (P.converged() and M.converged()):
            continue
        e_p, e_m = P.scalar("F") if t else P.scalar("E"), M.scalar("F") if t else M.scalar("E")
        te = tol["energy"](e_p, N, P.ms)
        ratio = abs(e_p - e_m) / te
        results[where_of(base)] = {"plusAtPlusLambda": e_p, "minusAtMinusLambda": e_m, "difference": e_p - e_m,
                                   "overPairingTolerance": ratio}
        if ratio <= CONTROL_MIN_RATIO:
            fails.append(where_of(base))
    reg.comparison("lambdaSign_%s" % kind, "ran" if results else "not run", results)
    reg.check_or_not_run("lambdaSign_%s_minusLambdaDoesNotPair" % kind, len(results), not fails,
                         "E (T > 0: F) of +M at +lambda vs -M (transformed bag) at -lambda differ by more than %g x "
                         "the pairing tolerance in %d of %d cases (pairing-theory T3.whatMustTransform.lambda); "
                         "not distinguished: %s" % (CONTROL_MIN_RATIO, len(results) - len(fails), len(results), fails))


def pair_totals(P, M):
    """Mirror pair (plus + minus) and Krein-image pair (plus - minus) of pairing-theory.json."""
    def s(view, name):
        v = view.scalar(name)
        return float(v) if is_num(v) else None

    def e(view, name):
        v = view.emt(name)
        return float(v) if is_num(v) else None
    out = {"mirror": {}, "kreinImage": {}}
    for name, getter in (("E", s), ("F", s), ("nTotal", s), ("scalarCharge", s), ("rho", e), ("p_y", e),
                         ("p_3", e), ("p_t", e), ("s_p", e), ("n_p", e)):
        a, b = getter(P, name), getter(M, name)
        if a is None or b is None:
            continue
        out["mirror"][name] = a + b
        out["kreinImage"][name] = a - b
        out.setdefault("plus", {})[name] = a
    return out


def check_totals(reg, groups, kind):
    tol = pair_tolerances(kind)
    totals = {}
    worst = Worst()
    for base in sorted(groups):
        g = groups[base]
        if "plus" not in g or "minus" not in g or not (g["plus"].converged() and g["minus"].converged()):
            continue
        P, M = g["plus"], g["minus"]
        t = pair_totals(P, M)
        totals[where_of(base)] = t
        N, ms = P.N, P.ms
        mir, kre, plus = t["mirror"], t["kreinImage"], t.get("plus", {})
        where = where_of(base)
        for name in ("E", "F"):
            if name in mir:
                worst.add("mirrorEnergyIsTwiceE", where + ":" + name, abs(mir[name] - 2 * plus[name]),
                          2 * tol["energy"](plus[name], N, ms))
                worst.add("kreinImageEnergyZero", where + ":" + name, abs(kre[name]), tol["energy"](plus[name], N, ms))
        if "nTotal" in mir:
            worst.add("mirrorChargeTwoN", where, abs(mir["nTotal"] - 2 * N), 1e-9 * N)
            worst.add("kreinImageChargeZero", where, abs(kre["nTotal"]), 1e-9 * N)
        if "scalarCharge" in mir:
            st = tol["energy"](plus["scalarCharge"], N, 1.0)
            worst.add("mirrorScalarZero", where, abs(mir["scalarCharge"]), st)
            worst.add("kreinImageScalarTwiceS", where, abs(kre["scalarCharge"] - 2 * plus["scalarCharge"]), 2 * st)
        scale = max(fmax([plus.get("rho"), plus.get("p_y"), plus.get("p_3")]), 1e-300)
        for name in ("rho", "p_y", "p_3", "p_t"):
            if name in kre:
                worst.add("kreinImageEmtZero", where + ":" + name, abs(kre[name]) / scale, tol["emtAverage"])
                worst.add("mirrorEmtTwice", where + ":" + name, abs(mir[name] - 2 * plus[name]) / scale,
                          2 * tol["emtAverage"])
    reg.comparison("totals_%s" % kind, "ran" if totals else "not run", totals)
    if not totals:
        return totals
    worst.report(reg, "totals_%s_" % kind, {
        "mirrorEnergyIsTwiceE": "mirror pair (plus + minus): E_pair = 2 E_+, F_pair = 2 F_+",
        "kreinImageEnergyZero": "Krein-image pair (plus - minus): E = F = 0",
        "mirrorChargeTwoN": "mirror pair: charge 2N", "kreinImageChargeZero": "Krein-image pair: charge 0",
        "mirrorScalarZero": "mirror pair: total scalar charge 0",
        "kreinImageScalarTwiceS": "Krein-image pair: total scalar charge 2 S_+",
        "kreinImageEmtZero": "Krein-image pair: <rho>, <p_y>, <p_3>, <p_t> = 0",
        "mirrorEmtTwice": "mirror pair: EMT averages doubled"})
    return totals


# ---------------------------------------------------------------------------
# the untransformed-BC control
# ---------------------------------------------------------------------------

def expected_box(universe, parity, M, L):
    """Analytic k = 0, lambda = 0 spectrum (eps >= 0) of one parity sector of a
    universe, in the reference's per-block basis (parity +1: g(0) = 0; -1: f(0) = 0).
    The -M problems are mapped onto +|m| problems by the swap f <-> g, which
    exchanges the roles of the f- and g-conditions at both ends."""
    brane = "g0" if parity > 0 else "f0"
    tip = {"plus": "g0", "minus": "f0", "control": "g0"}[universe]
    if universe != "plus":           # mass -M: swap the conditions, mass +M
        brane = "f0" if brane == "g0" else "g0"
        tip = "f0" if tip == "g0" else "g0"
    return KS.analytic_box(M, L, brane, tip, count=6)


def bound_state_energy(M, L):
    """sqrt(M^2 - kappa^2) with tanh(kappa L) = kappa/M (M L > 1), else None."""
    if M * L <= 1.0:
        return None
    a, b = 1e-12, M * (1 - 1e-15)
    g = lambda q: math.tanh(q * L) - q / M  # noqa: E731
    for _ in range(300):
        mid = 0.5 * (a + b)
        if g(a) * g(mid) <= 0:
            b = mid
        else:
            a = mid
    kappa = 0.5 * (a + b)
    return math.sqrt(max(M * M - kappa * kappa, 0.0))


def q0_levels(view, parity):
    """eps of the k = 0 (q = 0) levels of one parity sector, block type +1 (the k = 0
    spectrum of type -1 is the same), sorted."""
    g = view.level_groups().get((0, parity, 1), [])
    return sorted(d["eps"] for d in g)


def check_control(reg, groups, kind):
    tol = pair_tolerances(kind)
    worst = Worst()
    analytic = {}
    subgap = {}
    local = {}
    differs = {}
    status = {}
    for base in sorted(groups):
        field, m_abs, N, lam, t = base
        g = groups[base]
        where = where_of(base)
        if "control" in g:
            c = g["control"]
            status[where] = {"converged": c.converged(),
                             "convergedBy": c.run.converged_by() if hasattr(c, "run") else c.converged_by()}
        # (a) analytic k = 0 spectra and (b) the sub-gap band, lambda = 0 runs (constant M, v = 0)
        if lam == "lam0" and t == 0.0:
            for universe, view in sorted(g.items()):
                if not view.converged():
                    continue
                rec = {}
                for parity in (1, -1):
                    got = [e for e in q0_levels(view, parity) if e >= -1e-9]
                    exp = expected_box(universe, parity, m_abs, L_OF(view))
                    n = min(len(got), len(exp))
                    dev = max((abs(a - b) for a, b in zip(got[:n], exp[:n])), default=float("inf"))
                    te = tol["eps"](max(exp[:n], default=1.0), m_abs)
                    worst.add("analyticK0Spectra", "%s:%s:p%+d" % (where, universe, parity), dev if n else float("inf"),
                              te, "%d levels" % n)
                    rec["parity%+d" % parity] = {"levels": got[:n], "analytic": exp[:n], "maxDeviation": dev}
                analytic["%s:%s" % (where, universe)] = rec
                band = sorted(e for par in (1, -1) for e in q0_levels(view, par) if abs(e) < m_abs * (1 - 1e-9))
                eb = bound_state_energy(m_abs, L_OF(view))
                expected = [0.0] if universe != "control" else sorted([0.0] + ([-eb, eb] if eb is not None else []))
                ok = len(band) == len(expected) and all(abs(a - b) <= tol["eps"](b, m_abs) for a, b in
                                                        zip(band, expected))
                subgap["%s:%s" % (where, universe)] = {"subGapLevels": band, "expected": expected, "ok": ok,
                                                       "boundStateAnalytic": eb}
                worst.add("subGapBand", "%s:%s" % (where, universe), 0.0 if ok else 1.0, 0.5,
                          "levels %s expected %s" % (band, expected))
        # (c) zero-mode localisation of the N = 8 free ground state (|m| = 1)
        if lam == "lam0" and t == 0.0 and N == 8.0:
            for universe, view in sorted(g.items()):
                n_c = view.profile("n_c")
                if n_c is None or not view.converged():
                    continue
                ratio = float(n_c[-1] / n_c[0]) if n_c[0] > 0 else float("inf")
                expect = math.exp((1 if universe != "control" else -1) * 2 * m_abs * L_OF(view))
                local["%s:%s" % (where, universe)] = {"braneOverTip": ratio, "expected": expect}
                if m_abs == 1.0:
                    worst.add("zeroModeLocalisation", "%s:%s" % (where, universe),
                              abs(math.log(ratio / expect)) if ratio > 0 and math.isfinite(ratio) else float("inf"),
                              1e-3, "n_c(0)/n_c(-L) = %.8g, expected %.8g" % (ratio, expect))
        # (d) the control differs from the plus universe
        if "plus" in g and "control" in g and g["plus"].converged() and g["control"].converged():
            P, C = g["plus"], g["control"]
            pairs, unmatched, compared = match_levels(P, C, tol["eps"], use_index=False)
            eps_ratio = max((abs(a["eps"] - b["eps"]) / tol["eps"](a["eps"], P.ms) for a, b in pairs), default=0.0)
            if unmatched:
                eps_ratio = float("inf")
            gap_p, gap_c = P.scalar("ksGap"), C.scalar("ksGap")
            e_p, e_c = P.scalar("F" if t else "E"), C.scalar("F" if t else "E")
            n_p, n_cc = P.profile("n_c"), C.profile("n_c")
            dn = (float(np.max(np.abs(n_p - n_cc)) / max(float(np.max(np.abs(n_p))), 1e-300))
                  if n_p is not None and n_cc is not None and len(n_p) == len(n_cc) else None)
            rec = {"eigenvalueDeviationOverTolerance": eps_ratio, "unmatchedLevels": unmatched,
                   "gapPlus": gap_p, "gapControl": gap_c, "energyPlus": e_p, "energyControl": e_c,
                   "densityRelativeDifference": dn}
            ratios = [eps_ratio]
            if is_num(gap_p) and is_num(gap_c):
                ratios.append(abs(gap_p - gap_c) / tol["scalar"](gap_p, P.ms))
            if is_num(e_p) and is_num(e_c):
                ratios.append(abs(e_p - e_c) / tol["energy"](e_p, P.N, P.ms))
            if dn is not None:
                ratios.append(dn / tol["profileInterior"])
            rec["largestDifferenceOverTolerance"] = max(ratios)
            differs[where] = rec
            worst.add("controlDiffers", where, 1.0 if max(ratios) > CONTROL_MIN_RATIO else 2.0, 1.5,
                      "largest difference / pairing tolerance %.3g" % max(ratios))
    reg.comparison("control_%s_analyticK0" % kind, "ran" if analytic else "not run", analytic)
    reg.comparison("control_%s_subGapBand" % kind, "ran" if subgap else "not run", subgap)
    reg.comparison("control_%s_zeroModeLocalisation" % kind, "ran" if local else "not run", local)
    reg.comparison("control_%s_differs" % kind, "ran" if differs else "not run", differs)
    reg.measure("control_%s_status" % kind, status)
    worst.report(reg, "control_%s_" % kind, {
        "analyticK0Spectra": "lambda = 0 k = 0 levels of plus, minus, control against the analytic box spectra "
                             "(control mixed sector tan(pL) = +p/|m| + bound state; plus/minus tan(pL) = -p/|m|)",
        "subGapBand": "k = 0 levels in (-|m|, |m|): plus and minus only the zero mode, the control in addition the "
                      "bound-state pair +-sqrt(m^2 - kappa^2), tanh(kappa L) = kappa/|m|",
        "zeroModeLocalisation": "N = 8 free ground state (|m| = 1): n_c(0)/n_c(-L) = e^{+2|m|L} (plus, minus), "
                                "e^{-2|m|L} (control: tip-localised zero mode); |ln(ratio/expected)|",
        "controlDiffers": "the converged control differs from the plus universe by more than %g x the pairing "
                          "tolerance (eigenvalues, KS gap, E or F, density)" % CONTROL_MIN_RATIO})


def L_OF(view):
    return float(view.run.params["L"]) if hasattr(view, "run") else float(view.L)


def c_paired(M, L, H=1.0, a4=0.0):
    return math.exp(-a4) * (2 * M / (2 * M - H)) * (1 - math.exp(-(2 * M - H) * L)) / (1 - math.exp(-2 * M * L))


def c_control(M, L, H=1.0, a4=0.0):
    return math.exp(-a4) * (2 * M / (2 * M + H)) * (math.exp((2 * M + H) * L) - 1) / (math.exp(2 * M * L) - 1)


def zero_mode_splitting(m, parity, tip, L=3.0, k=1e-4, n0=60):
    """|eps_{+1}(k) - eps_{-1}(k)|/(2k) of the k = 0 zero-mode pair at small k,
    three grids (n0, 2 n0, 4 n0), (h^2, h^3) extrapolation."""
    vals = []
    for lv in range(3):
        grid = KS.Grid(L, n0 * 2 ** lv)
        sh = KS.solve_shell(grid, np.full(grid.N + 1, m), np.zeros(grid.N + 1), k, 0.0, parity, tip, False, m=m)
        e_plus = sh["eps"][sh["type"] == 1]
        e_minus = sh["eps"][sh["type"] == -1]
        ep = e_plus[int(np.argmin(np.abs(e_plus)))]
        em = e_minus[int(np.argmin(np.abs(e_minus)))]
        vals.append(abs(ep - em) / (2 * k))
    return float(KS.extrapolate3(*vals)), vals


def check_zero_mode_splitting(reg, theory):
    """The first-order splitting of the k = 0 zero-mode band (T3.untransformedBCControl)."""
    out = {}
    worst = Worst()
    for M, n0 in ((1.0, 60), (3.0, 120)):
        L = 3.0
        cp, cc = c_paired(M, L), c_control(M, L)
        rec = {"closedFormPaired": cp, "closedFormControl": cc}
        for universe, m, parity, tip, target in (("plus", M, 1, "g0", cp), ("minus", -M, -1, "f0", cp),
                                                 ("control", -M, 1, "g0", cc)):
            value, levels = zero_mode_splitting(m, parity, tip, L=L, n0=n0)
            rec[universe] = {"extrapolated": value, "levels": levels}
            worst.add("zeroModeSplitting", "M%g:%s" % (M, universe), abs(value - target) / target, 1e-6,
                      "%.12g vs %.12g" % (value, target))
        if M == 1.0:
            Y = math.exp(L)
            rec["differenceClosedForm"] = (2.0 / 3.0) * (Y - 1) ** 2 / (Y + 1)
            worst.add("zeroModeSplitting", "M1:c_ctrl - c(M) = (2/3)(Y-1)^2/(Y+1)",
                      abs((cc - cp) - rec["differenceClosedForm"]) / rec["differenceClosedForm"], 1e-12)
            text = (((theory or {}).get("T3") or {}).get("untransformedBCControl") or {}).get(
                "valuesM1H1L3a0_floatLabelled")
            if isinstance(text, str):
                nums = [float(x) for x in re.findall(r"([0-9]+\.[0-9]+)`", text)]
                rec["theoryFloatValues"] = nums
                if len(nums) == 2:
                    worst.add("zeroModeSplitting", "M1:theory float values",
                              max(abs(nums[0] - cp) / cp, abs(nums[1] - cc) / cc), 1e-12)
        out["M%g" % M] = rec
    reg.comparison("control_zeroModeSplitting", "ran", out)
    worst.report(reg, "control_", {"zeroModeSplitting": "first-order splitting eps = +-c k of the k = 0 zero-mode "
                                   "band: plus and minus c(M), control c_ctrl (closed forms of pairing-theory.json; "
                                   "computed here with the imported reference solver at k = 1e-4)"})


# ---------------------------------------------------------------------------
# statistics sign: dirac16complex (sg = -1) versus dirac16complex00 (sg = +1)
# ---------------------------------------------------------------------------

def strip_run_json(doc):
    """run.json without the entries that name the field (label, statistics, pairs record)."""
    doc = json.loads(json.dumps(doc))
    for key in ("label", "statistics", "statisticsSign", "exchangeSign"):
        (doc.get("params") or {}).pop(key, None)
        (doc.get("parameters") or {}).pop(key, None)
    doc.pop("pairs", None)
    doc.pop("pairRun", None)
    doc.pop("label", None)
    return doc


def check_lambda0_identity(reg, runs, kind):
    """lambda = 0: the two fields solve the same problem (the statistics enters only
    through lambda): tables byte-identical, run.json numbers identical."""
    compared, differing = 0, []
    for key, view in sorted(runs.items()):
        field, universe, m_abs, N, lam, t = key
        if field != "d16c" or lam != "lam0":
            continue
        other = runs.get(("d16c00",) + key[1:])
        if other is None:
            continue
        compared += 1
        files = view.table_files()
        bad = [f for f in files if not os.path.exists(os.path.join(other.dir, f))
               or sha256_file(os.path.join(view.dir, f)) != sha256_file(os.path.join(other.dir, f))]
        if strip_run_json(view.doc()) != strip_run_json(other.doc()):
            bad.append("run.json (numbers)")
        if bad:
            differing.append("%s: %s" % (view.label, bad))
    reg.check_or_not_run("statistics_%s_lambda0_identical" % kind, compared, not differing,
                         "%d lambda = 0 pairs (d16c, d16c00): tables byte-identical and run.json identical apart from "
                         "the field name; differing: %s" % (compared, differing[:6]))


def check_potential_identities(reg, runs, kind):
    """M_eff - m = (1 + sg/16) lambda S_p and v_x = sg lambda n_p/16 node by node."""
    worst = 0.0
    where = None
    count = 0
    for key, view in sorted(runs.items()):
        if not view.converged():
            continue
        m_eff, v_x, s_p, n_p = (view.profile(n) for n in ("M_eff", "v_x", "S_p", "n_p"))
        if any(a is None for a in (m_eff, v_x, s_p, n_p)):
            continue
        count += 1
        lam, sg = view.lam, view.sg
        scale = max(float(np.max(np.abs(m_eff - view.m))), float(np.max(np.abs(v_x))), 1e-300)
        d = max(float(np.max(np.abs((m_eff - view.m) - (1.0 + sg / 16.0) * lam * s_p))),
                float(np.max(np.abs(v_x - sg * lam * n_p / 16.0))))
        r = d / scale if scale > 1e-300 else d
        if r > worst:
            worst, where = r, view.label
    reg.check_or_not_run("statistics_%s_potential_identities" % kind, count, worst <= POTENTIAL_IDENTITY_TOL,
                         "M_eff - m = (1 + sg/16) lambda S_p (15/16 resp. 17/16) and v_x = sg lambda n_p/16 on every "
                         "profile node of %d runs: max deviation / pseudo-potential scale %.3e (at %s)"
                         % (count, worst, where))


def first_order_coefficients(view):
    """A_H = (V/2) int S_p^2 dV_p/V, A_x = (V/32) int (n_p^2 + S_p^2) dV_p/V of a lambda = 0
    run (dV_p = W^6 dy per coordinate volume), Simpson on the profile nodes; the
    Simpson - trapezoid difference is returned as the quadrature uncertainty."""
    y = view.y()
    w6 = view.profile("W6")
    n_p, s_p = view.profile("n_p"), view.profile("S_p")
    V = view.volume()
    out = {}
    for name, integrand in (("A_H", 0.5 * s_p * s_p * w6), ("A_x", (n_p * n_p + s_p * s_p) * w6 / 32.0)):
        simp, rule = C4.integrate_uniform(y, integrand)
        h = y[1] - y[0]
        trap = float(np.sum(0.5 * (integrand[1:] + integrand[:-1])) * h)
        out[name] = V * simp
        out[name + "_quadratureUncertainty"] = V * abs(simp - trap)
        out["rule"] = rule
    return out


def odd_part(fp, fm, lam):
    """[X(lambda) - X(-lambda)]/(2 lambda)."""
    return (fp - fm) / (2.0 * lam)


def even_over_lambda(fp, fm, lam):
    """[X(lambda)/lambda + X(-lambda)/(-lambda)]/2."""
    return 0.5 * (fp / lam - fm / lam)


def check_first_order(reg, runs, kind):
    """First-order (odd in lambda) statistics identities with the O(lambda_1^2)
    truncation measured from the lambda_2 runs (lambda_2 = 10 lambda_1)."""
    worst = Worst()
    records = {}
    bases = sorted({(k[0], k[1], k[2], k[3], k[5]) for k in runs})
    for field, universe, m_abs, N, t in bases:
        if universe not in ("plus", "minus"):
            continue
        get = {lam: runs.get((field, universe, m_abs, N, lam, t)) for lam in LAMBDA_NAMES}
        if any(v is None or not v.converged() for v in get.values()):
            continue
        v0 = get["lam0"]
        sg = v0.sg
        coef = first_order_coefficients(v0)
        A_H, A_x = coef["A_H"], coef["A_x"]
        qerr = coef["A_H_quadratureUncertainty"] + coef["A_x_quadratureUncertainty"]
        l1, l2 = get["lamp1"].lam, get["lamp2"].lam
        r2 = (l2 / l1) ** 2 - 1.0
        where = "%s_%s_m%s_N%d_T%s" % (field, universe, KS.trim_float(m_abs), int(N), "0" if t == 0 else KS.trim_float(t))
        rec = {"A_H": A_H, "A_x": A_x, "quadratureUncertainty": qerr, "lambda1": l1, "lambda2": l2}
        e_name = "F" if t else "E"
        for name, pred, func in (("exchange", sg * A_x, even_over_lambda), ("hartree", A_H, even_over_lambda),
                                 (e_name, A_H + sg * A_x, odd_part)):
            x1 = func(get["lamp1"].scalar(name), get["lamm1"].scalar(name), l1)
            x2 = func(get["lamp2"].scalar(name), get["lamm2"].scalar(name), l2)
            trunc = abs(x2 - x1) / r2
            tol = 3.0 * trunc + qerr + 1e-6 * max(abs(pred), abs(A_x), 1e-300)
            rec[name] = {"lambda1": x1, "lambda2": x2, "predicted": pred, "truncationEstimate": trunc,
                         "tolerance": tol, "deviation": abs(x1 - pred)}
            worst.add({"exchange": "exchangeFirstOrder", "hartree": "hartreeFirstOrder"}.get(name, "energyFirstOrder"),
                      where, abs(x1 - pred), tol, "%.10g vs %.10g" % (x1, pred))
        if N == 8.0 and t == 0.0:
            x1 = odd_part(get["lamp1"].scalar("mu"), get["lamm1"].scalar("mu"), l1)
            x2 = odd_part(get["lamp2"].scalar("mu"), get["lamm2"].scalar("mu"), l2)
            pred = sg * A_x / 4.0
            trunc = abs(x2 - x1) / r2
            tol = 3.0 * trunc + qerr / 4.0 + 1e-6 * abs(pred)
            rec["mu"] = {"lambda1": x1, "lambda2": x2, "predicted": pred, "truncationEstimate": trunc,
                         "tolerance": tol}
            worst.add("muFirstOrderN8", where, abs(x1 - pred), tol, "%.10g vs %.10g" % (x1, pred))
        records[where] = rec
    # the two fields side by side: exchange part of the linear energy shift -1 vs +1 (the -1/32 vs +1/32),
    # odd parts of M_eff - m in the ratio 17/15 and of v_x in the ratio -1
    for (field, universe, m_abs, N, t) in bases:
        if field != "d16c" or universe not in ("plus", "minus"):
            continue
        a = {lam: runs.get(("d16c", universe, m_abs, N, lam, t)) for lam in LAMBDA_NAMES}
        b = {lam: runs.get(("d16c00", universe, m_abs, N, lam, t)) for lam in LAMBDA_NAMES}
        if any(v is None or not v.converged() for v in list(a.values()) + list(b.values())):
            continue
        where = "%s_m%s_N%d_T%s" % (universe, KS.trim_float(m_abs), int(N), "0" if t == 0 else KS.trim_float(t))
        l1, l2 = a["lamp1"].lam, a["lamp2"].lam
        r2 = (l2 / l1) ** 2 - 1.0
        rec = records.setdefault("fields_" + where, {})
        for name, expected, weight_name in (("M_eff", 17.0 / 15.0, "S_p"), ("v_x", -1.0, "n_p")):
            def odd_profile(views, lam_p, lam_m, lam):
                pa, pm = views[lam_p].profile(name), views[lam_m].profile(name)
                if name == "M_eff":
                    pa, pm = pa - views[lam_p].m, pm - views[lam_m].m
                return (pa - pm) / (2.0 * lam)
            w0 = np.abs(a["lam0"].profile(weight_name))
            sel = w0 > 1e-2 * float(np.max(w0)) if float(np.max(w0)) > 0 else np.zeros(len(w0), dtype=bool)
            sel[0] = sel[-1] = False
            if not np.any(sel):
                rec[name] = {"note": "the lambda = 0 %s vanishes identically (N = 8: the zero modes carry no scalar "
                                     "density): no first-order ratio" % weight_name}
                continue
            r1 = odd_profile(b, "lamp1", "lamm1", l1)[sel] / odd_profile(a, "lamp1", "lamm1", l1)[sel]
            rr2 = odd_profile(b, "lamp2", "lamm2", l2)[sel] / odd_profile(a, "lamp2", "lamm2", l2)[sel]
            trunc = float(np.max(np.abs(rr2 - r1))) / r2
            dev = float(np.max(np.abs(r1 - expected)))
            tol = 3.0 * trunc + 1e-6
            rec[name] = {"expectedRatio": expected, "maxDeviation": dev, "truncationEstimate": trunc,
                         "tolerance": tol, "nodes": int(np.sum(sel))}
            worst.add("oddPartRatio_" + name, where, dev, tol, "ratio expected %.6f" % expected)
        e_name = "F" if t else "E"
        ra = records.get("d16c_%s_m%s_N%d_T%s" % (universe, KS.trim_float(m_abs), int(N),
                                                   "0" if t == 0 else KS.trim_float(t)), {})
        rb = records.get("d16c00_%s_m%s_N%d_T%s" % (universe, KS.trim_float(m_abs), int(N),
                                                     "0" if t == 0 else KS.trim_float(t)), {})
        if e_name in ra and e_name in rb and ra.get("A_x"):
            A_H, A_x = ra["A_H"], ra["A_x"]
            ratio = (rb[e_name]["lambda1"] - A_H) / (ra[e_name]["lambda1"] - A_H)
            tol = (ra[e_name]["tolerance"] + rb[e_name]["tolerance"]) / abs(A_x)
            rec["exchangePartRatio"] = {"value": ratio, "expected": -1.0, "tolerance": tol}
            worst.add("exchangePartRatio", where, abs(ratio + 1.0), tol,
                      "(D_00 - A_H)/(D_d16c - A_H) = %.10g (expected -1)" % ratio)
    reg.comparison("statistics_%s_firstOrder" % kind, "ran" if records else "not run", records)
    if not records:
        return
    worst.report(reg, "statistics_%s_" % kind, {
        "exchangeFirstOrder": "E_x/lambda (even part) -> sg A_x, A_x = (V/32) int (n_p^2 + S_p^2) dV_p of lambda = 0",
        "hartreeFirstOrder": "E_H/lambda (even part) -> A_H = (V/2) int S_p^2 dV_p of lambda = 0",
        "energyFirstOrder": "dE/dlambda (T > 0: dF/dlambda) at lambda = 0 = A_H + sg A_x (odd part of E)",
        "muFirstOrderN8": "N = 8: d mu/d lambda = sg A_x/4 (the zero modes carry no scalar density)",
        "oddPartRatio_M_eff": "odd part of M_eff - m: d16c00/d16c = 17/15 on the nodes where S_p(lambda = 0) != 0",
        "oddPartRatio_v_x": "odd part of v_x: d16c00/d16c = -1",
        "exchangePartRatio": "exchange part of the linear energy shift: (D_00 - A_H)/(D_d16c - A_H) = -1"})


# ---------------------------------------------------------------------------
# Rust pairs outputs (studies/dirac16complex_kohn_sham `pairs`: <root>/pairs/<config>/<universe>/)
# ---------------------------------------------------------------------------

RUST_TABLES = ("levels.csv", "profiles.csv", "history.csv", "particle-hole.csv", "levels-excited.csv")
RUST_PROFILE_NAMES = {"W6": "volume_factor"}


def num_or_none(value):
    return float(value) if is_num(value) else None


class RustView:
    """Uniform accessors of one Rust pairs universe directory."""
    solver = "rust"

    def __init__(self, directory):
        self.dir = directory
        self._doc = load_json(os.path.join(directory, "run.json"))
        d = self._doc
        self.label = d.get("label", rel_path(directory))
        self.error = d.get("error")
        pr = d.get("pairRun") or {}
        p = d.get("parameters") or pr.get("requestedParameters") or {}
        self.params = p
        stat = p.get("statistics") or pr.get("statistics")
        self.field = STAT_OF.get(stat, "d16c") if stat else "d16c"
        self.sg = FIELD_SIGN[self.field]
        self.m = float(p.get("m", pr.get("m", float("nan"))))
        self.ms = abs(self.m)
        self.N = float(p.get("N", pr.get("N", float("nan"))))
        self.T = float(p.get("T", pr.get("T", 0.0)))
        self.L = float(p.get("L", pr.get("L", 3.0)))
        self.lambda_hat = float(p.get("lambdaHat", pr.get("lambdaHat", float("nan"))))
        self.lam = float(p.get("lambda", pr.get("lambda", float("nan"))))
        self.grid_points = int(p.get("gridPoints", 301))
        universe = UNIVERSE_SHORT.get(d.get("universe") or pr.get("universe"))
        t = pr.get("TOverAbsM")
        t = float(t) if is_num(t) else (self.T / self.ms if self.ms else float("nan"))
        self.key = (self.field, universe, self.ms, self.N, pr.get("lambdaName"), round(t, 9))
        self._groups = None
        self._profiles = None

    def doc(self):
        return self._doc

    def converged(self):
        return not self.error and bool(self._doc.get("converged"))

    def converged_by(self):
        if self.error:
            return "error: " + str(self.error)[:160]
        return "converged" if self._doc.get("converged") else "not converged"

    def smearing(self):
        return float(self.params.get("occupationSmearing") or 0.0)

    def table_files(self):
        return [f for f in RUST_TABLES if os.path.exists(os.path.join(self.dir, f))]

    def volume(self):
        return float(self.params["ell"]) ** 3

    def level_groups(self):
        if self._groups is None:
            groups = {}
            path = os.path.join(self.dir, "levels.csv")
            if os.path.exists(path):
                hdr, lev = read_csv(path)
                idx = {h: i for i, h in enumerate(hdr)}
                for row in lev:
                    g = (int(row[idx["n2"]]), int(row[idx["parity"]]), int(row[idx["s"]]))
                    groups.setdefault(g, []).append({
                        "eps": float(row[idx["eps"]]), "branch": int(row[idx["branch"]]), "f": float(row[idx["f"]]),
                        "mult": float(row[idx["multiplicity"]]), "index": int(row[idx["index"]]), "epsLevels": []})
            for g in groups.values():
                g.sort(key=lambda d: (d["eps"], d["index"]))
            self._groups = groups
        return self._groups

    def index_map(self, key):
        """Rust level map (shooting.rs / pairs.rs image_key): (n2, p, s, n) -> (n2, -p, -s, -n)."""
        q, p, s, n = key
        return (q, -p, -s, -n)

    def _excited(self):
        return self._doc.get("firstExcitedState") or {}

    def scalar(self, name):
        d = self._doc
        table = {"E": "energy", "F": "freeEnergy", "S": "entropy", "mu": "mu", "nTotal": "nTotal",
                 "scalarCharge": "scalarTotal", "hartree": "hartreeEnergy", "exchange": "exchangeEnergy"}
        if name in table:
            return num_or_none(d.get(table[name]))
        if name == "interaction":
            h, x = num_or_none(d.get("hartreeEnergy")), num_or_none(d.get("exchangeEnergy"))
            return h + x if h is not None and x is not None else None
        ex = self._excited()
        if name == "ksGap":
            return num_or_none(ex.get("ksGap", d.get("ksGap")))
        if name == "deltaSCF":
            return num_or_none(ex.get("deltaScf"))
        if name == "lowestParticleHole":
            return num_or_none(ex.get("lowestParticleHole"))
        return None

    def particle_hole(self):
        return [float(x) for x in (self._excited().get("particleHoleExcitations") or []) if is_num(x)]

    def _load_profiles(self):
        if self._profiles is None:
            path = os.path.join(self.dir, "profiles.csv")
            self._profiles = read_csv(path) if os.path.exists(path) else (None, None)
        return self._profiles

    def y(self):
        hdr, prof = self._load_profiles()
        return column(hdr, prof, "y") if hdr else None

    def profile(self, name):
        hdr, prof = self._load_profiles()
        name = RUST_PROFILE_NAMES.get(name, name)
        return column(hdr, prof, name) if hdr and name in hdr else None

    def emt(self, name):
        e = self._doc.get("emt") or {}
        table = {"rho": "rhoAvg", "p_y": "pYAvg", "p_3": "p3Avg", "p_t": "pTAvg", "s_p": "sPAvg", "n_p": "nPAvg",
                 "braneFraction": "braneFraction_within_1_over_H",
                 "tipFraction": "tipFraction_within_1_over_H_of_cutoff", "energyFromRho": "energyFromRho"}
        if name in table:
            return num_or_none(e.get(table[name]))
        if name == "lambdaSAvgOverM":
            return num_or_none((e.get("E41_sourcingConditions") or {}).get("lambdaSAvgOverM"))
        return None

    def grid_level_energies(self):
        return []


def load_rust(rust_dir):
    """(pairs summary or None, {key: RustView}, errors, refinement partners)."""
    base = os.path.join(rust_dir, "pairs")
    if not os.path.isdir(base):
        base = rust_dir
    summary = None
    spath = os.path.join(base, "summary.json")
    if os.path.exists(spath):
        try:
            summary = load_json(spath)
        except (OSError, ValueError) as error:
            summary = {"unreadable": str(error), "verdict": "UNREADABLE"}
    runs, errors, partners = {}, [], {}
    if not os.path.isdir(base):
        return summary, runs, errors, partners
    for root, _subdirs, files in os.walk(base):
        if "run.json" not in files:
            continue
        try:
            view = RustView(root)
        except Exception as error:  # noqa: BLE001
            errors.append("%s: %r" % (rel_path(root), error))
            continue
        if view.key[1] is None:
            continue
        if view.error:
            errors.append("%s: %s" % (view.label, str(view.error)[:200]))
        if view.grid_points != 301:
            partners.setdefault(view.key, []).append(view)
            continue
        runs[view.key] = view
    return summary, runs, errors, partners


def check_rust_summary(reg, summary, runs, errors):
    if summary is None:
        reg.comparison("rust_pairs_summary", "not run", "no pairs/summary.json")
        return
    reg.check("rust_pairs_summary_success", summary.get("verdict") == "SUCCESS",
              "verdict %s" % summary.get("verdict"))
    checks = C4.summary_checks(summary)
    failed = sorted(n for n, ok in checks.items() if not ok)
    reg.measure("rustPairsOwnCheckCount", len(checks))
    reg.measure("rustPairsOwnChecksFailed", failed)
    reg.check("rust_pairs_own_checks_passed", bool(checks) and not failed,
              "%d Rust pairs checks, failed: %s" % (len(checks), failed[:20]))
    reg.measure("rustPairsRunCount", len(runs))
    reg.measure("rustPairsErrors", errors)


def rust_grid_uncertainty(view, partners):
    """|X(finer grid) - X(301)| of a Rust run with a finer-grid partner (Stage-4 rule E4.12)."""
    out = {}
    for other in partners.get(view.key, []):
        for name in ("E", "mu", "ksGap", "deltaSCF", "lowestParticleHole"):
            a, b = view.scalar(name), other.scalar(name)
            if is_num(a) and is_num(b):
                out[name] = max(out.get(name, 0.0), abs(a - b))
    return out


def reference_pot_scale(F):
    m_eff, v_x = F.profile("M_eff"), F.profile("v_x")
    return max(float(np.max(np.abs(m_eff - F.m))), float(np.max(np.abs(v_x))))


def compare_rust_reference(worst, where, R, F, gu, record):
    """One Rust universe against the reference universe of the same parameters
    (the rules of check_dirac16complex_kohn_sham.py compare_canonical, with |m|)."""
    ms, N, T = F.ms, F.N, F.T
    dl_s = (R.lambda_hat / F.run.lambda_hat - 1.0) if F.run.lambda_hat else 0.0
    dl = abs(dl_s)
    ratio_l = 1.0 + dl_s
    vmax = reference_pot_scale(F)
    trel = C4.truncation_relative(F.doc())
    record["lambdaHat"] = {"rust": R.lambda_hat, "reference": F.run.lambda_hat, "relativeDifference": dl}
    if F.run.lambda_hat or R.lambda_hat:
        worst.add("lambdaHat", where, dl if F.run.lambda_hat else float("inf"), TOL["lambdaHat"])
    # eigenvalues per (q, parity, block type) with branch and occupation
    gR, gF = R.level_groups(), F.level_groups()
    all_r = [d["eps"] for g in gR.values() for d in g]
    all_f = [d["eps"] for g in gF.values() for d in g]
    compared = unmatched = branch_bad = occ_bad = 0
    if all_r and all_f:
        lo, hi = max(min(all_r), min(all_f)) + 1e-6, min(max(all_r), max(all_f)) - 1e-6
        exact_t0 = T == 0.0 and not R.smearing() and not F.smearing()
        for g, levels in gR.items():
            cand = gF.get(g, [])
            for lr in levels:
                if not lo <= lr["eps"] <= hi:
                    continue
                compared += 1
                tol = TOL["eps"] * max(1.0, abs(lr["eps"]) / ms) * ms + (dl + trel) * vmax
                if not cand:
                    unmatched += 1
                    continue
                lf = min(cand, key=lambda d: abs(d["eps"] - lr["eps"]))
                dev = abs(lr["eps"] - lf["eps"])
                if dev > max(1e-2 * max(1.0, abs(lr["eps"]) / ms) * ms, 100.0 * tol):
                    unmatched += 1
                    continue
                worst.add("eigenvalues", where, dev, tol, "eps %.8f" % lr["eps"])
                branch_bad += int(lr["branch"] != lf["branch"])
                if exact_t0 and abs(lr["f"] - lf["f"]) > 1e-6:
                    occ_bad += 1
    worst.add("eigenvalueMatching", where, float(unmatched + branch_bad + occ_bad) + (0.0 if compared else 1.0), 0.5,
              "compared %d, unmatched %d, branch %d, occupation %d" % (compared, unmatched, branch_bad, occ_bad))
    record["eigenvalues"] = {"compared": compared, "unmatched": unmatched, "branchMismatches": branch_bad,
                             "occupationMismatches": occ_bad}
    e_int = F.scalar("interaction") or 0.0
    if T == 0.0:
        e_r, e_f = R.scalar("E"), F.scalar("E")
        if is_num(e_r) and is_num(e_f):
            e_f2 = e_f + e_int * dl_s
            tol = TOL["energy"] * max(abs(e_r), N * ms) + gu.get("E", 0.0)
            worst.add("E0", where, abs(e_r - e_f2), tol)
            record["E0"] = {"rust": e_r, "reference": e_f, "referenceLambdaCorrected": e_f2, "tolerance": tol}
        for name in ("mu", "ksGap", "deltaSCF", "lowestParticleHole"):
            a, b = R.scalar(name), F.scalar(name)
            if is_num(a) and is_num(b):
                tol = TOL["scalar"] * max(ms, abs(a)) + dl * vmax + gu.get(name, 0.0)
                worst.add({"mu": "muAndGap", "ksGap": "muAndGap", "deltaSCF": "deltaSCF",
                           "lowestParticleHole": "particleHole"}[name], where + ":" + name, abs(a - b), tol)
                record[name] = {"rust": a, "reference": b, "deviation": abs(a - b), "tolerance": tol}
            else:
                record[name] = {"rust": a, "reference": b, "compared": False}
    else:
        th = F.doc().get("thermo") or {}
        shdr, spec = F.run.shdr, F.run.spec
        lo_r, hi_r = R.doc().get("windowLo"), R.doc().get("windowHi")
        if is_num(lo_r) and is_num(hi_r) and is_num(th.get("mu")):
            tr = C4.truncation_from_spectrum(shdr, spec, T, N, th["mu"], lo_r, hi_r)
        else:
            tr = {k: v for k, v in (th.get("rustWindowTruncation") or {}).items() if k not in ("windowOnly", "edgeTable")}
        record["truncation"] = tr
        for name, dkey, kind in (("E", "deltaE", "E"), ("F", "deltaF", "E"), ("S", "deltaEntropy", "S"),
                                 ("mu", "deltaMu", "mu")):
            a, b = R.scalar(name), F.scalar(name)
            if not (is_num(a) and is_num(b)):
                continue
            corr = tr.get(dkey, 0.0) or 0.0
            b2 = b + corr + (e_int * dl_s if kind == "E" else 0.0)
            if kind == "E":
                tol = TOL["thermoEnergy"] * max(abs(a), N * ms) + 0.05 * abs(corr)
            elif kind == "S":
                tol = TOL["entropy"] * max(abs(a), N) + 0.05 * abs(corr)
            else:
                tol = TOL["scalar"] * max(ms, abs(a)) + 0.05 * abs(corr) + dl * vmax
            worst.add("thermodynamics", where + ":" + name, abs(a - b2), tol)
            record[name] = {"rust": a, "reference": b, "referenceCorrected": b2, "tolerance": tol}
    # profiles on the common nodes
    yr, yf = R.y(), F.y()
    if yr is not None and yf is not None:
        pairs = [(int(np.argmin(np.abs(yr - yv))), j) for j, yv in enumerate(yf)]
        pairs = [(i, j) for i, j in pairs if abs(yr[i] - yf[j]) < 1e-9]
        if len(pairs) >= 3:
            ir = np.array([a for a, _ in pairs])
            jf = np.array([b for _, b in pairs])
            ends = np.array([(j == 0 or j == len(yf) - 1) for j in jf])
            vrel = dl * vmax / ms + 2.0 * trel
            prof = {"commonNodes": len(pairs)}
            groups = {"density": ("n_c", "S_c", "n_p", "S_p"), "potential": ("M_eff", "v_x"),
                      "emt": ("rho", "p_y", "p_3", "p_t")}
            for group, names in groups.items():
                for name in names:
                    a = R.profile(name)
                    b = F.profile(name)
                    if a is None or b is None:
                        continue
                    a, b = a[ir], b[jf].copy()
                    if name == "M_eff":
                        a, b = a - R.m, (b - F.m) * ratio_l
                    elif name == "v_x":
                        b = b * ratio_l
                    if group == "density":
                        partner = {"n_c": "S_c", "S_c": "n_c", "n_p": "S_p", "S_p": "n_p"}[name]
                        scale = max(float(np.max(np.abs(b))), float(np.max(np.abs(F.profile(partner)[jf]))), 1e-300)
                    elif group == "potential":
                        scale = max(vmax * ratio_l, 1e-300)
                        if vmax < 1e-12 * ms:
                            continue
                    else:
                        scale = max(max(float(np.max(np.abs(F.profile(n)))) for n in names), 1e-300)
                    dev = np.abs(a - b) / scale
                    d_int = float(np.max(dev[~ends])) if np.any(~ends) else 0.0
                    d_end = float(np.max(dev[ends])) if np.any(ends) else 0.0
                    prof[name] = {"interior": d_int, "ends": d_end}
                    worst.add("profilesInterior", where + ":" + name, d_int, TOL["profileInterior"] + vrel)
                    worst.add("profilesEnds", where + ":" + name, d_end, TOL["profileEnd"] + vrel)
            record["profiles"] = prof
    # EMT averages and fractions
    scale = max(fmax([F.emt("rho"), F.emt("p_y"), F.emt("p_3")]), 1e-300)
    dscale = max(fmax([F.emt("n_p"), F.emt("s_p")]), 1e-300)
    vrel = dl * vmax / ms + 2.0 * trel
    emt = {}
    for name in ("rho", "p_y", "p_3", "p_t", "n_p", "s_p"):
        a, b = R.emt(name), F.emt(name)
        if is_num(a) and is_num(b):
            dev = abs(a - b) / (dscale if name in ("n_p", "s_p") else scale)
            worst.add("emtAverages", where + ":" + name, dev, TOL["emtAverage"] + vrel)
            emt[name] = {"rust": a, "reference": b, "relative": dev}
    for name in ("braneFraction", "tipFraction"):
        a, b = R.emt(name), F.emt(name)
        if is_num(a) and is_num(b):
            worst.add("fractions", where + ":" + name, abs(a - b), TOL["fraction"] + vrel)
            emt[name] = {"rust": a, "reference": b}
    record["emt"] = emt


def check_rust_vs_reference(reg, rust_runs, ref_runs, partners):
    worst = Worst()
    compared, missing_ref = [], []
    for key in sorted(rust_runs, key=str):
        R = rust_runs[key]
        F = ref_runs.get(key)
        if F is None:
            missing_ref.append(R.label)
            continue
        if not (R.converged() and F.converged()):
            reg.comparison("rust_vs_reference_%s" % R.label.replace("/", "_"), "not run",
                           "not converged: rust %s, reference %s" % (R.converged_by(), F.converged_by()))
            continue
        record = {"rust": R.label, "reference": F.label}
        gu = rust_grid_uncertainty(R, partners)
        if gu:
            record["rustGridUncertainty"] = gu
        compare_rust_reference(worst, R.label, R, F, gu, record)
        reg.comparison("rust_vs_reference_%s" % R.label.replace("/", "_"), "ran", record)
        compared.append(R.label)
    reg.measure("rustVsReferenceCompared", len(compared))
    reg.measure("rustRunsWithoutReference", missing_ref)
    reg.measure("referenceRunsWithoutRust", sorted(F.label for k, F in ref_runs.items() if k not in rust_runs))
    if not compared:
        reg.comparison("rust_vs_reference", "not run", "no Rust pairs run with a converged reference partner")
        return
    worst.report(reg, "rust_vs_reference_", {
        "lambdaHat": "lambda_hat of both sides (Stage-4 couplings of each solver)",
        "eigenvalues": "eigenvalues per (q, parity, block type): |d eps| <= %g max(1, |eps|/|m|) |m| + (dl + trel) "
                       "max|V|" % TOL["eps"],
        "eigenvalueMatching": "every level in the common window matched, same branch, same T = 0 occupation",
        "E0": "E_0 (lambda_hat-corrected): |dE| <= %g max(|E|, N |m|) (+ Rust grid uncertainty)" % TOL["energy"],
        "muAndGap": "mu and KS gap", "deltaSCF": "Delta-SCF", "particleHole": "lowest particle-hole excitation",
        "thermodynamics": "E, F, S, mu at T > 0 after the correction for the Rust level set (f_cut window)",
        "profilesInterior": "profiles on the interior common nodes", "profilesEnds": "profiles on the end nodes",
        "emtAverages": "EMT proper-volume averages", "fractions": "brane and tip fractions"})


def tree_files(root):
    out = []
    for base, _dirs, files in os.walk(root):
        for f in files:
            out.append(os.path.relpath(os.path.join(base, f), root).replace(os.sep, "/"))
    return sorted(out)


def check_repeat(reg, rust_dir, repeat_dir):
    if not repeat_dir or not os.path.isdir(repeat_dir):
        reg.comparison("rust_repeat_byte_identity", "not run", "no --repeat directory")
        return
    a_root = os.path.join(rust_dir, "pairs") if os.path.isdir(os.path.join(rust_dir, "pairs")) else rust_dir
    b_root = os.path.join(repeat_dir, "pairs") if os.path.isdir(os.path.join(repeat_dir, "pairs")) else repeat_dir
    files = tree_files(a_root)
    differing = [f for f in files if not os.path.exists(os.path.join(b_root, f))
                 or sha256_file(os.path.join(a_root, f)) != sha256_file(os.path.join(b_root, f))]
    extra = sorted(set(tree_files(b_root)) - set(files))
    reg.measure("rustRepeatFilesCompared", len(files))
    reg.check("rust_repeat_byte_identity", bool(files) and not differing and not extra,
              "%d files compared, differing %s, only in the repeat %s" % (len(files), differing[:10], extra[:10]))


def check_refined(reg, rust_runs, refined_dir):
    if not refined_dir or not os.path.isdir(refined_dir):
        reg.comparison("rust_refined_convergence", "not run", "no --refined directory")
        return
    _s, refined, _e, _p = load_rust(refined_dir)
    worst_e = worst_eps = 0.0
    count = 0
    for key, R in rust_runs.items():
        Q = refined.get(key)
        if Q is None or not (R.converged() and Q.converged()):
            continue
        a, b = R.scalar("E"), Q.scalar("E")
        if is_num(a) and is_num(b):
            worst_e = max(worst_e, abs(a - b) / max(abs(a), abs(b), 1.0))
            count += 1
        ga, gb = R.level_groups(), Q.level_groups()
        for g, levels in ga.items():
            other = gb.get(g, [])
            if len(other) == len(levels):
                worst_eps = max([worst_eps] + [abs(x["eps"] - y["eps"]) for x, y in zip(levels, other)])
    reg.measure("rustRefinedRunsCompared", count)
    reg.check("rust_refined_convergence", count > 0 and worst_e < TOL["refinedEnergy"] and worst_eps < TOL["refinedEps"],
              "%d runs: max relative energy difference %.3e, max eigenvalue difference %.3e"
              % (count, worst_e, worst_eps))


def check_stage4_rerun(reg, rerun_dir):
    """Byte identity of Stage-4 reference runs re-executed with the Stage-5 solver."""
    if not rerun_dir or not os.path.isdir(rerun_dir):
        reg.comparison("stage4_reference_byte_identity", "not run", "no --stage4-rerun directory")
        return
    compared, differing, labels = 0, [], []
    for label in sorted(os.listdir(rerun_dir)):
        new = os.path.join(rerun_dir, label)
        old = os.path.join(STAGE4_REFERENCE, label)
        if not os.path.isfile(os.path.join(new, "run.json")):
            continue
        labels.append(label)
        if not os.path.isdir(old):
            differing.append(label + " (no committed Stage-4 run)")
            continue
        names = sorted(set(os.listdir(old)) | set(os.listdir(new)))
        for f in names:
            compared += 1
            a, b = os.path.join(old, f), os.path.join(new, f)
            if not (os.path.isfile(a) and os.path.isfile(b)) or sha256_file(a) != sha256_file(b):
                differing.append(label + "/" + f)
    reg.measure("stage4RerunLabels", labels)
    reg.check("stage4_reference_byte_identity", len(labels) >= 2 and compared > 0 and not differing,
              "%d re-executed Stage-4 reference runs %s, %d files compared with %s: differing %s"
              % (len(labels), labels, compared, rel_path(STAGE4_REFERENCE), differing[:10]))


def check_theory(reg, theory):
    if theory is None:
        reg.comparison("theory", "not run", "pairing-theory.json absent")
        return
    t3 = theory.get("T3") or {}
    checks = dict(t3.get("checks") or {})
    for sub in ("untransformedBCControl", "pairTotalsKS"):
        checks.update((t3.get(sub) or {}).get("checks") or {})
    reg.check("theory_T3_checks_true", bool(checks) and all(checks.values()),
              "%d T3 checks of pairing-theory.json, false: %s" % (len(checks), [k for k, v in checks.items() if not v]))
    pres = t3.get("numericsPrescription") or {}
    text = json.dumps(pres)
    reg.check("theory_prescription_matches_runs",
              "lambda unchanged" in pres.get("minusMTransformed", "") and "a(-L) = 0" in pres.get("minusMTransformed", "")
              and "b(-L) = 0 kept" in pres.get("minusMUntransformedControl", "") and "15/16" in text and "17/16" in text,
              "minusMTransformed: %s | control: %s" % (pres.get("minusMTransformed", "")[:160],
                                                       pres.get("minusMUntransformedControl", "")[:120]))


def stage4_label_of(view):
    """The Stage-4 reference label of a dirac16complex plusM run (m1_L3_N8_lamp1_T0, ..._T0p1)."""
    field, universe, m_abs, N, lam, t = view.key
    if field != "d16c" or universe != "plus":
        return None
    return "m%s_L%s_N%d_%s_T%s" % (KS.trim_float(m_abs), KS.trim_float(L_OF(view)), int(N), lam,
                                   "0" if t == 0 else KS.trim_float(t))


def comparable_numbers(doc):
    """The numerical records of a reference run.json that do not name the run."""
    keep = ("extrapolated", "orderEstimates", "ksGap", "emt", "couplingScale", "heatCapacityFixedSpectrum",
            "rustWindowTruncation", "exactZeroTemperatureOccupations", "smearingAttempts", "levels", "excited",
            "thermo", "converged", "mode")
    out = {k: doc.get(k) for k in keep}
    p = dict(doc.get("params") or {})
    p.pop("label", None)
    out["params"] = p
    return json.loads(json.dumps(out))


def check_plus_reproduces_stage4(reg, runs):
    """dirac16complex plusM = the Stage-4 problem: every plusM run of the pairs matrix whose
    parameter set is a committed Stage-4 reference run reproduces it (tables byte for byte,
    run.json numbers identical apart from the label)."""
    compared, differing = [], []
    for key, view in sorted(runs.items()):
        label4 = stage4_label_of(view)
        if label4 is None:
            continue
        old = os.path.join(STAGE4_REFERENCE, label4)
        if not os.path.isfile(os.path.join(old, "run.json")):
            continue
        compared.append("%s = %s" % (view.label, label4))
        bad = []
        for f in view.table_files():
            a, b = os.path.join(view.dir, f), os.path.join(old, f)
            if not os.path.isfile(b) or sha256_file(a) != sha256_file(b):
                bad.append(f)
        if comparable_numbers(view.doc()) != comparable_numbers(load_json(os.path.join(old, "run.json"))):
            bad.append("run.json (numbers)")
        if bad:
            differing.append("%s: %s" % (view.label, bad))
    reg.measure("plusReproducesStage4Compared", compared)
    reg.check_or_not_run("reference_plusM_reproduces_stage4", len(compared), not differing,
                         "%d dirac16complex plusM runs with a committed Stage-4 reference run of the same parameters "
                         "(%s): tables byte-identical and run.json numbers identical; differing: %s"
                         % (len(compared), rel_path(STAGE4_REFERENCE), differing[:8]))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--reference", default=DEFAULT_REFERENCE)
    parser.add_argument("--rust", default=DEFAULT_RUST)
    parser.add_argument("--theory", default=DEFAULT_THEORY)
    parser.add_argument("--repeat", default=None)
    parser.add_argument("--refined", default=None)
    parser.add_argument("--stage4-rerun", default=None)
    parser.add_argument("--report", default=DEFAULT_REPORT)
    parser.add_argument("--no-solver", action="store_true", help="skip the checker's own small solver computations")
    args = parser.parse_args(argv)
    reg = Registry()
    sources = {"scripts/check_dirac16complex_pairs.py": sha256_file(os.path.abspath(__file__)),
               "scripts/ks_reference_solver.py": sha256_file(os.path.join(REPO, "scripts", "ks_reference_solver.py")),
               "scripts/ks_reference_pairs.py": sha256_file(os.path.join(REPO, "scripts", "ks_reference_pairs.py"))}
    theory = load_json(args.theory) if os.path.exists(args.theory) else None
    if theory is not None:
        sources[rel_path(args.theory)] = sha256_file(args.theory)
    check_theory(reg, theory)
    summary, ref_raw, problems = load_reference(args.reference)
    ref_runs = {k: RefView(v) for k, v in ref_raw.items()}
    if summary is not None:
        sources[rel_path(os.path.join(args.reference, SUMMARY_NAME))] = sha256_file(
            os.path.join(args.reference, SUMMARY_NAME))
    if ref_runs:
        check_reference_runs(reg, summary, ref_runs, problems, args)
        check_plus_reproduces_stage4(reg, ref_runs)
        groups = group_views(ref_runs)
        check_pairing(reg, groups, "reference", "reference")
        check_lambda_sign(reg, groups, "reference")
        check_totals(reg, groups, "reference")
        check_control(reg, groups, "reference")
        check_lambda0_identity(reg, ref_runs, "reference")
        check_potential_identities(reg, ref_runs, "reference")
        check_first_order(reg, ref_runs, "reference")
    else:
        reg.comparison("reference", "not run", "no reference pairs runs under %s (%s)" % (args.reference, problems[:3]))
    if not args.no_solver:
        check_zero_mode_splitting(reg, theory)
    else:
        reg.comparison("control_zeroModeSplitting", "not run", "--no-solver")
    rsum, rust_runs, rerrors, partners = load_rust(args.rust) if os.path.isdir(args.rust) else (None, {}, [], {})
    if rsum is not None and os.path.exists(os.path.join(args.rust, "pairs", "summary.json")):
        sources[rel_path(os.path.join(args.rust, "pairs", "summary.json"))] = sha256_file(
            os.path.join(args.rust, "pairs", "summary.json"))
    if rust_runs or rsum is not None:
        check_rust_summary(reg, rsum, rust_runs, rerrors)
        rgroups = group_views(rust_runs)
        check_pairing(reg, rgroups, "rust", "rust")
        check_lambda_sign(reg, rgroups, "rust")
        check_totals(reg, rgroups, "rust")
        check_control(reg, rgroups, "rust")
        check_lambda0_identity(reg, rust_runs, "rust")
        check_potential_identities(reg, rust_runs, "rust")
        check_first_order(reg, rust_runs, "rust")
        if ref_runs:
            check_rust_vs_reference(reg, rust_runs, ref_runs, partners)
        check_repeat(reg, args.rust, args.repeat)
        check_refined(reg, rust_runs, args.refined)
    else:
        reg.comparison("rust", "not run", "no Rust pairs outputs under %s" % args.rust)
    check_stage4_rerun(reg, args.stage4_rerun)
    failed = [n for n, ok in reg.checks.items() if not ok]
    for name, ok in reg.checks.items():
        print("check_%s=%s" % (name, "true" if ok else "false"))
    for name, value in reg.measurements.items():
        if not name.endswith("_detail"):
            print("measurement_%s=%s" % (name, json.dumps(value)[:300]))
    not_run = sorted(n for n, c in reg.comparisons.items() if c["status"] != "ran")
    print("comparisons_not_run=%s" % json.dumps(not_run))
    print("check_count=%d" % len(reg.checks))
    print("failed_check_count=%d" % len(failed))
    for name in failed:
        print("FAILED %s: %s" % (name, str(reg.measurements.get(name + "_detail", ""))[:600]))
    report = {"schemaVersion": 1, "producer": PRODUCER,
              "tolerances": {"reference": TOL, "rustPairing": RUST_PAIR_TOL,
                             "potentialIdentity": POTENTIAL_IDENTITY_TOL, "controlMinRatio": CONTROL_MIN_RATIO},
              "checks": reg.checks, "measurements": reg.measurements, "comparisons": reg.comparisons,
              "sourceSha256": sources, "checkCount": len(reg.checks), "failedCheckCount": len(failed),
              "failed": failed, "comparisonsNotRun": not_run}
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(KS.jsonable(report), indent=2) + "\n")
    print("report: %s" % args.report)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
