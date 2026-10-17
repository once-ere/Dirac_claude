#!/usr/bin/env python3
"""Revision/field_equations_a4/ks_source/ks_source_a4.py - the field equations for a4[x4] and b4[x4] (SPEC section 5)
specialised to the Kohn-Sham states of dirac16complex (SPEC section 7, Revision/kohn_sham) as the source.

The metric is the corrected primordial metric of 2026-10-16 (version 2; SPEC section 1): g = diag(e^{-2a4} b4 cot^2 z,
e^{2a4} (x3), -1, -e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real.  Coordinates as the author names them: x1, x2, x3 =
3-space (scale factor e^{a4}); x4 = time; x5, x6, x7 = the three extra times (scale factor e^{-a4} b4^{1/2}
(sin^2 z)^{1/12}); x0 = the hidden direction, z = 6 H x0, and the Kohn-Sham hidden coordinate y = ln|sin z|/(6 H) in
[-L, 0] (sqrt|g| d^8x = e^{-a4} b4^2 e^{3Hy} dy d^3x dx4 d^3x_t).  u = b4'/b4, v = u', kk = e^{2a4}/b4, h4 = u/2 - a4'.

What this script does (Revision code only; inputs are Revision files, read-only):
  A (exact, sympy, from Revision/field_equations_a4/a4-equations.json)
    the hidden and the extra-time components of the left-hand side are one and the same expression (a source needs
    p0 = p_t); the off-diagonal components vanish identically (a source needs T^x4_x0 = 0); the x4 component is a
    first-order constraint and the x1 and x0 components are linear in (a4'', v) with the recorded Jacobian; the
    constraint propagates (the x4 component of the Bianchi identity, with the u terms); the x0 conservation identity
    in the Kohn-Sham coordinate is p0_y + 3 H (p0 - p_t) = 0; the x0-averaged free fold-band gas (rho ~ b4^{-2},
    p3 = rho/3, p0 = p_t = 0) satisfies the energy exchange identically, for every a4 and b4; the history source of the
    record reproduces the recorded one.
  B (numerical, the recorded Kohn-Sham ground-state profiles; proper densities, b4(0) = 1)
    the integrals from the profiles; the x0 conservation identity on every profile; the hidden-direction mismatch of
    every component (the x0-independent part of a profile is its weighted average); the source-condition report
    verified.
  C (the hidden-direction moments along the record's history a4 = H x4, b4 = e^{(4/3) H x4})
    the averaged condition p0 = p_t; the energy relation dE/da4 = -3 P3 + P_t + P0/3 along the dense history of every
    series; the record's history needs a source that no constant kappa makes of the Kohn-Sham gas; source signs.
  D (integration, an APPROXIMATION stated as such)
    the x0-averaged equations (the x4 constraint and the x1 and x0 components, the second-order system) with the
    x0-averaged free fold-band gas as the source, kappa rho_bar = sigma0 (b4/b4(0))^{-2}, kappa p3_bar = kappa rho_bar/3,
    kappa p0_bar = kappa p_t_bar = 0 (exact for every a4 and b4 while the gas stays on the fold band, check D0), started
    on the record's history (a4'(0) = H, u(0) = (4/3) H) and integrated in x4 with RK4 at two base step sizes (every
    step covered by substeps with step-doubling error control), for the stated gravity theories; the constraint is kept
    by the Bianchi identity (check D3); the outcomes are classified.

Outputs (deterministic, LF; two runs byte-identical):
  Revision/field_equations_a4/ks_source/results/ks-source-moments.csv   per Kohn-Sham state
  Revision/field_equations_a4/ks_source/results/ks-source-a4-cases.csv  per integration case
  Revision/field_equations_a4/ks_source/reports/ks-source-a4.json       every check (name, verdict, detail), conclusions
  Revision/field_equations_a4/ks_source/reports/ks-source-a4-summary.md the results in words, from this run

Usage (from anywhere): python Revision/field_equations_a4/ks_source/ks_source_a4.py [--ks-results DIR] [--out DIR]
(defaults: Revision/kohn_sham/results and this folder; the options exist for the negative control of the tests)
Exit code 0 iff every check passes; exit code 1 with a line "ERROR  ..." if an input is missing or malformed.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
A4DIR = HERE.parent
REV = A4DIR.parent
ROOT = REV.parent
KS = REV / "kohn_sham"
A4_JSON = A4DIR / "a4-equations.json"
KS_PARAMS = KS / "results" / "parameters.json"
KS_PROFILES = KS / "results" / "ground" / "profiles"
KS_INTEGRALS = KS / "results" / "ground" / "emt-integrals.csv"
KS_LEVELS = KS / "results" / "ground" / "levels"
KS_ADIABATIC = KS / "results" / "adiabatic" / "adiabaticity.csv"
KS_HISTORY = KS / "results" / "adiabatic" / "history.json"
KS_THEORY = KS / "ks-theory.json"
CONDITIONS = A4DIR / "reports" / "ks-source-conditions.json"   # the source-condition report, verified here (check B0)
# the dense history (41 slices a4 = 0, 0.05, ..., 2; the same solver and history, written by
# Revision/dark_sector/dirac16complex/compute/run_ks_history.py): parts C and D
DENSE = REV / "dark_sector" / "dirac16complex" / "outputs" / "ks-history-dense.csv"
OUT_MOMENTS = HERE / "results" / "ks-source-moments.csv"
OUT_CASES = HERE / "results" / "ks-source-a4-cases.csv"
OUT_REPORT = HERE / "reports" / "ks-source-a4.json"
OUT_SUMMARY = HERE / "reports" / "ks-source-a4-summary.md"

CHECKS: list[dict] = []

# tolerances (stated, with their reasons)
TOL_INTEGRAL = 1e-6      # Simpson on the 151-point output grid against the solver's own integrals (found ~1e-8)
TOL_CONS_FD = 1e-3       # 4th-order finite differences on the output grid dy = 0.02 (truncation ~ dy^4)
TOL_ENERGY = 1e-5        # Simpson of the energy relation over two dense steps (0.05) against the change of E
TOL_EXACT = 1e-12        # identities of the recorded numbers up to rounding
TOL_METHODS = 1e-6       # RK4 with the base steps h = 1e-3 and h = 2e-3 (substeps controlled by TOL_STEP in both)
TOL_CONSTRAINT = 1e-8    # the constraint along the integrated solutions (kept by the Bianchi identity), relative
TOL_STEP = 1e-12         # local error of an RK4 substep (step doubling: one step s against two steps s/2), rel. max(1, |y|)
SUB_LEVELS = 40          # the smallest substep is h 2^-40; a solution that needs less cannot be followed (an event)
DET_SINGULAR = 1e-6      # |det J| <= DET_SINGULAR |det J(0)|: the second-order system is singular there (a4'' ~ 1/det J)

# the stated gravity theories (H = 1 units of the solver; alpha_k carry H^(2-2k)); Lambda fixed only for the author's
GRAVITY = [
    ("einstein", Fraction(1), Fraction(0), Fraction(0), None,
     "Einstein gravity: alpha1 = 1, alpha2 = alpha3 = 0"),
    ("author", Fraction(1), Fraction(1, 32), Fraction(1, 1152), Fraction(-10),
     "the author's Lovelock weights: alpha_k = w_k/H^(2k), w = (1, 1/32, 1/1152), Lambda = -10 H^2 in the convention of "
     "a4-equations.json (the author's Lambda = 10; Dirac_Einstein-Lovelock_4+4_Nash.nb, Out[134]/Out[135])"),
    ("egb", Fraction(1), Fraction(1, 80), Fraction(0), None,
     "Einstein-Gauss-Bonnet: alpha1 = 1, alpha2 H^2 = 1/80, alpha3 = 0"),
    ("lovelock3", Fraction(1), Fraction(1, 80), Fraction(1, 4000), None,
     "Einstein-Lovelock (cubic): alpha1 = 1, alpha2 H^2 = 1/80, alpha3 H^4 = 1/4000"),
]
SERIES = ["lam0"]                        # the free gas of N_mid and N_large: its averaged source is known for any b4
SIGMAS = [Fraction(-10), Fraction(-1), Fraction(-1, 10), Fraction(1, 10), Fraction(1), Fraction(10)]
A0, BE = Fraction(1), Fraction(4, 3)     # the record's history: a4'(0) = A0 H, u(0) = BE A0 H
X4_OUT = [0.5, 1.0, 1.5, 2.0]            # output times (units 1/H); both base step sizes hit them exactly
X4_END = 2.0
H_M1, H_M2 = 1e-3, 2e-3


def err(msg: str) -> None:
    print("ERROR  " + msg, flush=True)
    sys.exit(1)


def check(name: str, ok: bool, detail: str) -> bool:
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS " if ok else "FAIL ") + name, flush=True)
    return ok


def g6(x: float) -> str:
    return format(x, ".6g")


def e12(x: float) -> str:
    if x == 0.0:
        return "0"
    return format(x, ".12e")


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rel(p: Path) -> str:
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except ValueError:                      # a file outside the repository (only with --ks-results / --out)
        return p.resolve().as_posix()


def set_paths(ks_results: Path, out: Path) -> None:
    """--ks-results / --out (used by the tests for a negative control; the defaults are the committed locations)"""
    global KS_PARAMS, KS_PROFILES, KS_INTEGRALS, KS_LEVELS, KS_ADIABATIC, KS_HISTORY, OUT_MOMENTS, OUT_CASES, OUT_REPORT, OUT_SUMMARY
    KS_PARAMS = ks_results / "parameters.json"
    KS_PROFILES = ks_results / "ground" / "profiles"
    KS_INTEGRALS = ks_results / "ground" / "emt-integrals.csv"
    KS_LEVELS = ks_results / "ground" / "levels"
    KS_ADIABATIC = ks_results / "adiabatic" / "adiabaticity.csv"
    KS_HISTORY = ks_results / "adiabatic" / "history.json"
    OUT_MOMENTS = out / "results" / "ks-source-moments.csv"
    OUT_CASES = out / "results" / "ks-source-a4-cases.csv"
    OUT_REPORT = out / "reports" / "ks-source-a4.json"
    OUT_SUMMARY = out / "reports" / "ks-source-a4-summary.md"


def simpson(vals, h):
    n = len(vals) - 1
    if n % 2:
        raise ValueError("Simpson needs an even number of intervals")
    return h / 3 * (vals[0] + vals[-1] + 4 * sum(vals[1:-1:2]) + 2 * sum(vals[2:-1:2]))


def deriv4(f, h):
    """4th-order first derivative on a uniform grid (one-sided 5-point formulas at the two ends on each side)"""
    n = len(f)
    d = [0.0] * n
    for i in range(n):
        if 2 <= i < n - 2:
            d[i] = (f[i - 2] - 8 * f[i - 1] + 8 * f[i + 1] - f[i + 2]) / (12 * h)
        elif i == 0:
            d[i] = (-25 * f[0] + 48 * f[1] - 36 * f[2] + 16 * f[3] - 3 * f[4]) / (12 * h)
        elif i == 1:
            d[i] = (-3 * f[0] - 10 * f[1] + 18 * f[2] - 6 * f[3] + f[4]) / (12 * h)
        elif i == n - 1:
            d[i] = (25 * f[n - 1] - 48 * f[n - 2] + 36 * f[n - 3] - 16 * f[n - 4] + 3 * f[n - 5]) / (12 * h)
        else:
            d[i] = (3 * f[n - 1] + 10 * f[n - 2] - 18 * f[n - 3] + 6 * f[n - 4] - f[n - 5]) / (12 * h)
    return d


# ---------------------------------------------------------------------------------------------------------------------
# A: exact identities (sympy) from a4-equations.json
# ---------------------------------------------------------------------------------------------------------------------
SYM = {s: sp.Symbol(s) for s in ("ad1", "ad2", "uu", "vv", "kk", "hh", "alpha1", "alpha2", "alpha3", "Lam", "kappa", "H",
                                 "rho", "p3", "p0", "pt", "cc", "tt", "d0p0", "d4q40", "q40", "q04", "d0q04", "d4rho",
                                 "AA", "be", "bb", "dyp0")}


def parse(s: str) -> sp.Expr:
    return sp.sympify(s, locals=SYM)


def lhs_of(s: str) -> sp.Expr:
    return parse(s.split("==")[0])


def rhs_of(s: str) -> sp.Expr:
    return parse(s.split("==")[1])


def weights_of(g) -> dict:
    H = SYM["H"]
    return {SYM["alpha1"]: sp.Rational(g[1]), SYM["alpha2"]: sp.Rational(g[2]) / H ** 2, SYM["alpha3"]: sp.Rational(g[3]) / H ** 4}


def part_a(a4: dict) -> dict:
    gs, ein = a4["generalSource"], a4["einstein"]
    ad1, ad2, uu, vv, kk, Lam, H = (SYM[k] for k in ("ad1", "ad2", "uu", "vv", "kk", "Lam", "H"))
    F4 = lhs_of(gs["constraint_x4"]["input"])
    F1 = lhs_of(gs["space_x1_eq_x2_eq_x3"]["input"])
    F0 = lhs_of(gs["hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7"]["input"])
    rhs_ok = (rhs_of(gs["constraint_x4"]["input"]) == -SYM["kappa"] * SYM["rho"]
              and rhs_of(gs["space_x1_eq_x2_eq_x3"]["input"]) == SYM["kappa"] * SYM["p3"]
              and rhs_of(gs["hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7"]["input"]) == SYM["kappa"] * SYM["p0"])
    stated = (gs["hiddenEqualsExtraTimes"].endswith("p0 = p_t") and gs["offDiagonal"].startswith("0 = kappa T^mu_nu for every mu != nu")
              and "the left-hand sides are free of x0" in gs["x0_dependence"])
    # the Einstein members of the record are the general components at alpha2 = alpha3 = 0
    e_sub = {SYM["alpha1"]: 1, SYM["alpha2"]: 0, SYM["alpha3"]: 0}
    ein_ok = (sp.expand(F4.subs(e_sub) - lhs_of(ein["constraint_x4"]["input"])) == 0
              and sp.expand(F1.subs(e_sub) - lhs_of(ein["space_x1"]["input"])) == 0
              and sp.expand(F0.subs(e_sub) - lhs_of(ein["hidden_x0"]["input"])) == 0)
    check("A1_hidden_equals_extra_times_and_no_offdiagonal", rhs_ok and stated and ein_ok,
          "a4-equations.json has one component for x0 = x5 = x6 = x7 (generalSource.hiddenEqualsExtraTimes: '%s'), so a "
          "source needs p0 = p_t; the off-diagonal left-hand sides vanish identically (generalSource.offDiagonal), so it "
          "needs T^x4_x0 = 0; the left-hand sides are free of x0 (generalSource.x0_dependence), so every component of the "
          "source must be independent of x0; the right-hand sides are -kappa rho, kappa p3, kappa p0: %s; the Einstein "
          "entries of the record equal the general components at alpha2 = alpha3 = 0: %s"
          % (gs["hiddenEqualsExtraTimes"][-30:], rhs_ok, ein_ok))
    # the constraint is first order; the x1 and x0 components are linear in (ad2, vv) with the recorded Jacobian
    first = not (F4.has(ad2) or F4.has(vv))
    lin = all(sp.degree(sp.expand(F), gen) <= 1 for F in (F1, F0) for gen in (ad2, vv))
    J = sp.Matrix([[sp.diff(F1, ad2), sp.diff(F1, vv)], [sp.diff(F0, ad2), sp.diff(F0, vv)]])
    Jrec = parse(gs["secondOrderJacobian"]["input"].replace("{", "[").replace("}", "]"))
    Jrec = sp.Matrix(Jrec)
    jac_ok = sp.simplify(J - Jrec) == sp.zeros(2, 2)
    check("A2_constraint_first_order_second_order_system", first and lin and jac_ok,
          "the x4 component contains neither a4'' nor v = u' (a first-order constraint): %s; the x1 and x0 components are "
          "linear in (a4'', v): %s, with the Jacobian of generalSource.secondOrderJacobian: %s (where det J != 0 they give "
          "a4'' and v from the sources)" % (first, lin, jac_ok))
    # propagation of the constraint: d/dx4 F4 = 3 ad1 (F1 - F4) + 4 hh (F0 - F4), hh = uu/2 - ad1, kk' = kk (2 ad1 - uu)
    dF4 = sp.diff(F4, ad1) * ad2 + sp.diff(F4, uu) * vv + sp.diff(F4, kk) * kk * (2 * ad1 - uu)
    prop = sp.expand(dF4 - (3 * ad1 * (F1 - F4) + 4 * (uu / 2 - ad1) * (F0 - F4)))
    check("A3_constraint_propagation", prop == 0,
          "d/dx4 [x4 component] = 3 a4' (x1 - x4) + 4 h4 (x0 - x4) identically for every alpha_k, Lambda (h4 = u/2 - a4', "
          "kk' = kk (2 a4' - u); generalSource.constraint_propagation): the constraint is preserved by the second-order "
          "system whenever the source satisfies the energy exchange (A5)")
    # the x0 conservation identity in the Kohn-Sham coordinate (no off-diagonal source)
    cons0 = lhs_of(gs["conservation_x0"]["input"]).subs({SYM["q40"]: 0, SYM["q04"]: 0, SYM["d4q40"]: 0})
    in_y = sp.expand(cons0.subs(SYM["d0p0"], SYM["cc"] * SYM["dyp0"]) / SYM["cc"])
    y_ok = sp.expand(in_y - (SYM["dyp0"] + 3 * H * (SYM["p0"] - SYM["pt"]))) == 0
    check("A4_x0_conservation_in_y", y_ok,
          "generalSource.conservation_x0 without an off-diagonal source is d0 p0 + 3 H cot z (p0 - p_t) = 0; with "
          "dy = cot z dx0 (y = ln|sin z|/(6H)) it is p0_y + 3 H (p0 - p_t) = 0, the identity of ks-theory.json "
          "emt.conservationY that every self-consistent Kohn-Sham state satisfies")
    # the x0-averaged free fold-band gas satisfies the energy exchange for every a4, b4
    rho = SYM["rho"]
    ex = lhs_of(gs["energyExchange"]["input"]).subs({SYM["d4rho"]: -2 * uu * rho, SYM["p3"]: rho / 3, SYM["p0"]: 0})
    exch_ok = sp.expand(ex) == 0
    check("A5_free_fold_band_gas_conserves_energy", exch_ok,
          "generalSource.energyExchange (-d4 rho - 3 a4' (p3 + rho) - 4 h4 (p0 + rho) = 0 for an x0-independent source with "
          "p0 = p_t) holds identically for rho ~ b4^{-2} (d4 rho = -2 u rho), p3 = rho/3, p0 = p_t = 0, for every a4(x4) and "
          "b4(x4): the x0-averaged free fold-band gas (check D0) is a source that keeps the constraint (A3)")
    # the history source of the record
    aw = a4["exponentialHistory"]["authorWeights"]
    w_author = weights_of(GRAVITY[1])
    hist = {ad1: H, ad2: 0, uu: sp.Rational(4, 3) * H, vv: 0}
    kv = sp.Symbol("kk")
    srcs = {"minus_rho": F4, "p3": F1, "p0": F0}
    hs_ok = True
    for k, F in srcs.items():
        val = sp.expand((F.subs(hist).subs(w_author).subs(Lam, 0)).subs(H, 1))
        want = sp.expand(parse(aw["historySource_kappaT_minus_Lam"][k]["input"]).subs(kv, kk))
        hs_ok &= sp.simplify(val - want) == 0
    hs_ok &= aw["historySource_kappaT_minus_Lam"]["p0"]["input"] == aw["historySource_kappaT_minus_Lam"]["pt"]["input"]
    check("A6_history_source_reproduced", hs_ok and "be = 4/3" in aw["recordHistory"],
          "on the record's history a4 = H x4, b4 = e^((4/3) H x4) (a4' = H, a4'' = 0, u = (4/3) H, v = 0) the left-hand sides "
          "with the author's weights (Lambda removed) equal exponentialHistory.authorWeights.historySource_kappaT_minus_Lam "
          "(minus_rho, p3, p0 = pt; H = 1): %s" % hs_ok)
    theories = {}
    for g in GRAVITY:
        w = weights_of(g)
        args = (ad1, ad2, uu, vv, kk, Lam)
        F4g, F1g, F0g = (sp.expand(F.subs(w).subs(H, 1)) for F in (F4, F1, F0))
        theories[g[0]] = {
            "F4": sp.lambdify((ad1, uu, kk, Lam), F4g, "math"),
            "F1": sp.lambdify(args, F1g, "math"), "F0": sp.lambdify(args, F0g, "math"),
            "J": [[sp.lambdify((ad1, uu, kk), sp.diff(F, gen), "math") for gen in (ad2, vv)] for F in (F1g, F0g)],
            "couplings": g[5], "Lambda": g[4]}
    return theories


# ---------------------------------------------------------------------------------------------------------------------
# B, C: the Kohn-Sham states
# ---------------------------------------------------------------------------------------------------------------------
def read_csv(p: Path) -> list:
    with p.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def part_bc(params: dict) -> tuple:
    H = float(params["physics"]["H"])
    L = float(params["physics"]["L_tipCutoff"])
    vol0 = float(params["physics"]["Vol7AtA4Zero"])
    beta = float(params["physics"]["historyBeta"])
    W = (1.0 - math.exp(-3.0 * H * L)) / (3.0 * H)       # int_{-L}^{0} e^{3Hy} dy
    integ = {r["id"]: r for r in read_csv(KS_INTEGRALS)}
    states = {}
    for p in sorted(KS_PROFILES.glob("*.csv")):
        rows = read_csv(p)
        y = [float(r["y"]) for r in rows]
        X = {c: [float(r[c]) for r in rows] for c in ("n", "rho", "p3", "p_t", "p0")}
        sid = p.stem
        ir = integ[sid]
        a4 = float(ir["a4"])
        vol7 = vol0 * math.exp((2.0 * beta - 1.0) * a4)
        hy = y[1] - y[0]
        w3 = [math.exp(3.0 * H * t) for t in y]
        ints = {c: 2.0 * vol7 * simpson([w * x for w, x in zip(w3, X[c])], hy) for c in X}
        int_rel = max(abs(ints[c] - float(ir["int_" + c])) / max(1.0, abs(float(ir["int_" + c]))) for c in X)
        scale = max(max(abs(v) for v in X[c]) for c in ("rho", "p3", "p_t", "p0"))
        zero = scale == 0.0
        s = {"id": sid, "N": int(ir["N"]), "lambda_tag": ir["lambda_tag"], "a4": a4, "zero": zero, "int_rel": int_rel,
             "h": hy}
        bars = {c: float(ir["int_" + c]) / (2.0 * vol7 * W) for c in ("rho", "p3", "p_t", "p0", "n")}
        s.update({c + "_bar": bars[c] for c in bars})
        if not zero:
            # x0 conservation p0_y + 3H (p0 - p_t) = 0 with 4th-order differences
            d0 = deriv4(X["p0"], hy)
            res = [d0[i] + 3 * H * (X["p0"][i] - X["p_t"][i]) for i in range(len(y))]
            terms = max(max(abs(v) for v in d0), 3 * H * max(abs(a - b) for a, b in zip(X["p0"], X["p_t"])), 1e-300)
            s["cons_fd_rel"] = max(abs(v) for v in res) / max(terms, 3 * H * scale)
            # hidden-direction mismatch (L1 with the volume weight): mu1_X = int e^{3Hy} |X - X_bar| / int e^{3Hy} |X|
            for c in ("rho", "p3", "p_t", "p0"):
                den = simpson([w * abs(x) for w, x in zip(w3, X[c])], hy)
                s["mu1_" + c] = (simpson([w * abs(x - bars[c]) for w, x in zip(w3, X[c])], hy) / den) if den > 0 else None
            s["var_ratio"] = (max(X["rho"]) - min(X["rho"])) / scale
            s["c2_ratio"] = max(abs(a - b) for a, b in zip(X["p0"], X["p_t"])) / scale
            s["c2_bar_rel"] = abs(bars["p0"] - bars["p_t"]) / max(abs(bars["rho"]), abs(bars["p3"]), abs(bars["p0"]), abs(bars["p_t"]))
        states[sid] = s
    slices = sorted({s["a4"] for s in states.values()})
    geo = {"H": H, "L": L, "Vol7_0": vol0, "beta": beta, "W": W}
    return states, slices, geo


def read_dense() -> list:
    rows = read_csv(DENSE)
    out = []
    for r in rows:
        out.append({k: (r[k] if k in ("id", "lambda_tag", "occupied_signature") else float(r[k])) for k in r})
    return out


# ---------------------------------------------------------------------------------------------------------------------
# D: integration of the x0-averaged equations with the averaged free fold-band gas
# ---------------------------------------------------------------------------------------------------------------------
def bulk_edge(f: float, L: float) -> float:
    """the lowest positive k = 0 level that is not on the fold band (M = 1, v = 0, theta_tip = 0): the odd l = 0 level
    sqrt(1 + p^2), tan(p f L) = -p, p in (pi/(2 f L), pi/(f L)) (below the even l = 1 level sqrt(1 + (pi/(f L))^2))"""
    fl = f * L
    lo, hi = 0.5 * math.pi / fl, math.pi / fl
    g = lambda p: math.sin(p * fl) + p * math.cos(p * fl)  # noqa: E731
    glo = g(lo)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if (g(mid) > 0) == (glo > 0):
            lo, glo = mid, g(mid)
        else:
            hi = mid
    return min(math.sqrt(1.0 + (0.5 * (lo + hi)) ** 2), math.sqrt(1.0 + (math.pi / fl) ** 2))


def integrate_case(th: dict, Lam_: float, sigma0: float, h: float, kF: float, L: float) -> dict:
    """RK4 in x4 for y = (a4, ln b4, a4', u): (a4'', v) from the x1 and x0 components with kappa p3_bar = kappa rho_bar/3,
    kappa p0_bar = 0, kappa rho_bar = sigma0 b4^{-2} (b4(0) = 1). Every base step h is covered by substeps s = h 2^-l with
    step-doubling error control (one RK4 step s against two steps s/2, the latter kept, local error <= TOL_STEP
    max(1, |y|)), so the solution stays resolved where it steepens before an event; the substeps are counted in units
    of h 2^-SUB_LEVELS, so every base step and output time is hit exactly. Events: the second-order system singular
    (det J changes sign inside a substep or falls to DET_SINGULAR |det J(0)|), runaway (|a4'| or |u| > 1e3 H), step_underflow (a substep below
    h 2^-SUB_LEVELS would be needed), a4' <= 0 (3-space stops expanding) and the free gas leaving the fold band (the
    Fermi level e^{-a4} kF reaches the bulk edge at f = e^{-a4} b4^{1/2}), the last two at the base steps."""
    def rates(y):
        a, lb, ap, u_ = y
        kk_ = math.exp(2.0 * a - lb)
        sig = sigma0 * math.exp(-2.0 * lb)
        J = th["J"]
        j11, j12 = float(J[0][0](ap, u_, kk_)), float(J[0][1](ap, u_, kk_))
        j21, j22 = float(J[1][0](ap, u_, kk_)), float(J[1][1](ap, u_, kk_))
        det = j11 * j22 - j12 * j21
        r1 = sig / 3.0 - th["F1"](ap, 0.0, u_, 0.0, kk_, Lam_)
        r0 = 0.0 - th["F0"](ap, 0.0, u_, 0.0, kk_, Lam_)
        if det == 0.0:
            return None, det
        app = (r1 * j22 - j12 * r0) / det
        v_ = (j11 * r0 - j21 * r1) / det
        return (ap, u_, app, v_), det

    def rk4(y, s):
        """one RK4 step of size s, or None if det J changes sign or vanishes at a stage"""
        ks = []
        for (c, prev) in ((0.0, None), (0.5, 0), (0.5, 1), (1.0, 2)):
            ys = y if prev is None else [y[j] + c * s * ks[prev][j] for j in range(4)]
            r, det = rates(ys)
            if r is None or det * det0 <= 0.0:
                return None
            ks.append(r)
        yn = [y[j] + s / 6.0 * (ks[0][j] + 2 * ks[1][j] + 2 * ks[2][j] + ks[3][j]) for j in range(4)]
        return yn if all(math.isfinite(v) for v in yn) else None

    y = [0.0, 0.0, float(A0), float(BE * A0)]
    _, det0 = rates(y)
    out = {0.0: list(y)}
    cres = 0.0
    scale0 = abs(sigma0) + abs(Lam_) + 1.0
    event, x_end = "regular", X4_END
    n = int(round(X4_END / h))
    full_units = 1 << SUB_LEVELS
    lev = 0                                    # the current substep is h 2^-lev
    for i in range(n):
        done = 0                               # progress inside the base step, in units of h 2^-SUB_LEVELS
        while done < full_units:
            while (1 << (SUB_LEVELS - lev)) > full_units - done:
                lev += 1
            s = h * 2.0 ** -lev
            one = rk4(y, s)
            half = rk4(y, 0.5 * s)
            two = rk4(half, 0.5 * s) if half is not None else None
            sing = one is None or two is None
            e = 0.0 if sing else max(abs(a - b) / max(1.0, abs(b)) for a, b in zip(one, two))
            if sing or e > TOL_STEP:
                if lev >= SUB_LEVELS - 1:
                    event = "singular_second_order_system" if sing else "step_underflow"
                    break
                lev += 1
                continue
            y = two
            done += 1 << (SUB_LEVELS - lev)
            if e < TOL_STEP / 64.0 and lev > 0:
                lev -= 1
            a, lb, ap, u_ = y
            kk_ = math.exp(2.0 * a - lb)
            cres = max(cres, abs(th["F4"](ap, u_, kk_, Lam_) + sigma0 * math.exp(-2.0 * lb)) / (scale0 + abs(th["F4"](ap, u_, kk_, 0.0))))
            if abs(rates(y)[1]) <= DET_SINGULAR * abs(det0):
                event = "singular_second_order_system"
                break
            if abs(ap) > 1e3 or abs(u_) > 1e3:
                event = "runaway"
                break
        if event != "regular":
            x_end = (i + done / full_units) * h
            break
        x = (i + 1) * h
        a, lb, ap, u_ = y
        if ap <= 0.0:
            event, x_end = "a4_turns", x
            out[round(x, 9)] = list(y)
            break
        if kF > 0.0 and math.exp(-a) * kF >= bulk_edge(math.exp(-a + 0.5 * lb), L):
            event, x_end = "leaves_fold_band", x
            out[round(x, 9)] = list(y)
            break
        for xo in X4_OUT:
            if abs(x - xo) < 1e-9:
                out[xo] = list(y)
    return {"event": event, "x_end": x_end, "y_end": y, "out": out, "det0": det0, "constraint": cres}


# ---------------------------------------------------------------------------------------------------------------------
def main(argv: list) -> int:
    args = list(argv)
    ks_results, out = KS / "results", HERE
    while args:
        a = args.pop(0)
        if a in ("--ks-results", "--out") and args:
            v = Path(args.pop(0))
            if a == "--ks-results":
                ks_results = v
            else:
                out = v
        else:
            err("unknown argument %r (usage: ks_source_a4.py [--ks-results DIR] [--out DIR])" % a)
    set_paths(ks_results, out)
    for p in (A4_JSON, KS_PARAMS, KS_INTEGRALS, KS_ADIABATIC, KS_HISTORY, KS_THEORY, CONDITIONS, DENSE):
        if not p.is_file():
            err("missing input %s" % p)
    try:
        a4 = json.loads(A4_JSON.read_text(encoding="utf-8"))
        params = json.loads(KS_PARAMS.read_text(encoding="utf-8"))
        kst = json.loads(KS_THEORY.read_text(encoding="utf-8"))
    except (OSError, ValueError) as ex:
        err("cannot read an input: %s" % ex)
    if not kst["emt"]["conservationY"].startswith("p0' + 3H (p0 - p_t) = 0"):
        err("ks-theory.json emt.conservationY is not the identity of the corrected metric")
    if kst["adiabaticity"]["historyBeta"] != "4/3" or not kst["emt"]["offDiagonal"].startswith("T^x4_y = 0"):
        err("ks-theory.json: expected historyBeta 4/3 and T^x4_y = 0 for eigen-orbitals")
    if "corrected primordial metric of 2026-10-16" not in a4["title"]:
        err("a4-equations.json is not the record of the corrected metric")

    # ---------------- A
    theories = part_a(a4)

    # ---------------- B
    states, slices, geo = part_bc(params)
    nz = [s for s in states.values() if not s["zero"]]
    zero = sorted(s["id"] for s in states.values() if s["zero"])
    wi = max(states.values(), key=lambda s: s["int_rel"])
    check("B1_integrals_reproduced", wi["int_rel"] <= TOL_INTEGRAL,
          "Simpson's rule with the volume weight e^{3Hy} on the 151-point output grid (y = -L ... 0, L = %s) reproduces "
          "results/ground/emt-integrals.csv (int_X = 2 Vol_7(a4,0) int e^{3Hy} X dy, Vol_7(a4,0) = %s e^{(2 beta - 1) a4,0}, "
          "beta = %s, the whole cell) for all %d states: largest relative difference %s (%s); hence the weighted average "
          "X_bar = int_X / (2 Vol_7(a4,0) W) (per proper cell volume), W = int_{-L}^{0} e^{3Hy} dy = %s"
          % (g6(geo["L"]), g6(geo["Vol7_0"]), g6(geo["beta"]), len(states), g6(wi["int_rel"]), wi["id"], g6(geo["W"])))
    wc = max(nz, key=lambda s: s["cons_fd_rel"])
    check("B2_x0_conservation_on_every_profile", wc["cons_fd_rel"] <= TOL_CONS_FD,
          "p0_y + 3 H (p0 - p_t) = 0 (check A4) evaluated with 4th-order differences on the output grid (dy = %s) of the %d "
          "nonzero profiles: largest residual relative to the largest term %s (%s; tolerance %s from the truncation). The "
          "recorded states CONSERVE energy-momentum along x0; the source fails the field equations because its components "
          "depend on x0 (B3) and, for lambda != 0, because p0 != p_t (C1), not because conservation fails"
          % (g6(wc["h"]), len(nz), g6(wc["cons_fd_rel"]), wc["id"], g6(TOL_CONS_FD)))
    mu1 = {c: [s["mu1_" + c] for s in nz if s["mu1_" + c] is not None] for c in ("rho", "p3", "p_t", "p0")}
    mrho = min(nz, key=lambda s: s["mu1_rho"])

    def rng(v):
        return "[%s, %s]" % (g6(min(v)), g6(max(v))) if v else "-"
    ok_mu = all(s["mu1_rho"] > 1e-2 and s["mu1_p3"] > 1e-2 for s in nz)
    check("B3_hidden_direction_mismatch", ok_mu,
          "the field equations require every component of the source to be independent of x0 (A1); the profiles are not. "
          "The L1 measure with the volume weight, mu1_X = int e^{3Hy} |X - X_bar| / int e^{3Hy} |X| (0 for an x0-independent "
          "X), over the %d nonzero states: mu1_rho in %s (smallest %s), mu1_p3 in %s, mu1_p0 in %s, mu1_p_t in %s (p0 = p_t = 0 "
          "identically for lambda = 0, where these two are undefined): the computed source is NOT close to an x0-independent "
          "one" % (len(nz), rng(mu1["rho"]), mrho["id"], rng(mu1["p3"]), rng(mu1["p0"]), rng(mu1["p_t"])))
    # B0: the source-condition report, re-derived independently from the same Kohn-Sham files
    try:
        cond = json.loads(CONDITIONS.read_text(encoding="utf-8"))
        cc_ = {c["name"]: c for c in cond["checks"]}
    except (OSError, ValueError, KeyError) as ex:
        err("cannot read %s: %s" % (rel(CONDITIONS), ex))
    vmin = min(nz, key=lambda s: s["var_ratio"])
    holds = sorted(s["id"] for s in nz if s["c2_ratio"] <= TOL_EXACT)
    fails = sorted(s["id"] for s in nz if s["c2_ratio"] > 1e-6)
    lam0 = sorted(s["id"] for s in nz if s["lambda_tag"] == "lam0")
    fmin = min((s for s in nz if s["id"] in fails), key=lambda s: s["c2_ratio"])
    d1 = cc_["ks_profiles_depend_on_x0"]["detail"]
    d2 = cc_["ks_hidden_pressure_condition"]["detail"]
    ok0 = (all(c["verdict"] == "PASS" for c in cond["checks"]) and "corrected metric of 2026-10-16" in cond.get("metric", "")
           and (">= %s (smallest: %s)" % (g6(vmin["var_ratio"]), vmin["id"])) in d1
           and ("for exactly the %d nonzero states with lambda = 0" % len(holds)) in d2 and holds == lam0
           and ("(smallest: %s at %s)" % (g6(fmin["c2_ratio"]), fmin["id"])) in d2 and len(fails) == len(nz) - len(lam0))
    check("B0_source_condition_report_verified", ok0,
          "the numbers of Revision/field_equations_a4/reports/ks-source-conditions.json (corrected metric, every check PASS), "
          "re-derived from the same profiles: smallest (max rho - min rho)/max|T| %s (%s); p0 = p_t to rounding in exactly the "
          "%d lambda = 0 states with a nonzero tensor, violated in the other %d (smallest max_y |p0 - p_t|/max|T| %s, %s): "
          "the report states the same numbers: %s" % (g6(vmin["var_ratio"]), vmin["id"], len(holds), len(fails),
                                                       g6(fmin["c2_ratio"]), fmin["id"], ok0))

    # ---------------- C
    c1_zero = [s for s in nz if s["lambda_tag"] == "lam0"]
    c1_int = [s for s in nz if s["lambda_tag"] != "lam0"]
    c1_ok = all(s["c2_bar_rel"] <= TOL_EXACT for s in c1_zero) and all(s["c2_bar_rel"] > 1e-3 for s in c1_int)
    wmin = min(c1_int, key=lambda s: s["c2_bar_rel"])
    check("C1_averaged_hidden_pressure_condition", c1_ok,
          "averaged over x0 (per proper volume), p0_bar = p_t_bar holds to rounding for the %d lambda = 0 states with a "
          "nonzero tensor (both vanish) and fails for every one of the %d states with lambda != 0 (|p0_bar - p_t_bar| relative "
          "to the largest averaged component >= %s, %s): even an x0-averaged (dimensionally reduced) interacting source would "
          "violate p0 = p_t" % (len(c1_zero), len(c1_int), g6(wmin["c2_bar_rel"]), wmin["id"]))
    dense = read_dense()
    series = {}
    for r in dense:
        series.setdefault((int(r["N"]), r["lambda_tag"]), []).append(r)
    worst_e, n_e, worst_id = 0.0, 0, ""
    n_slices, steps = set(), set()
    for key, rs in series.items():
        rs.sort(key=lambda r: r["a4"])
        da = rs[1]["a4"] - rs[0]["a4"]
        n_slices.add(len(rs))
        steps.add(g6(2.0 * da))
        g = [-3.0 * r["int_p3"] + r["int_p_t"] + r["int_p0"] / 3.0 for r in rs]
        for i in range(0, len(rs) - 2, 2):
            lhs = rs[i + 2]["E_KS"] - rs[i]["E_KS"]
            rhs = simpson(g[i:i + 3], da)
            sc = max(1.0, abs(rs[i]["E_KS"]))
            dev = abs(lhs - rhs) / sc
            n_e += 1
            if dev > worst_e:
                worst_e, worst_id = dev, "N%d_%s a4 = %s" % (key[0], key[1], g6(rs[i]["a4"]))
    check("C2_energy_relation_along_the_dense_history", n_e > 0 and worst_e <= TOL_ENERGY,
          "dE/da4 = -3 P3 + P_t + P0/3 (beta = 4/3; ks-theory.json emt.energyChange; P = 2 Vol_7 int e^{3Hy} p dy) along the "
          "dense history (%s slices, every one of the %d series; the occupations stay fixed along each, ks-history-run.json): "
          "Simpson of the right-hand side over two steps (%s in a4) against the change of E_KS, %d intervals, largest "
          "|difference|/max(1, |E|) %s (%s; tolerance %s from the quadrature)"
          % ("/".join(str(n) for n in sorted(n_slices)), len(series), "/".join(sorted(steps)), n_e, g6(worst_e), worst_id,
             g6(TOL_ENERGY)))
    # C3: the record's history needs a source; the Kohn-Sham gas would need a kappa that changes along the history
    aw = a4["exponentialHistory"]["authorWeights"]
    kk = sp.Symbol("kk")
    need_krho = sp.lambdify(kk, -(parse(aw["historySource_kappaT_minus_Lam"]["minus_rho"]["input"]).subs(SYM["kk"], kk) - 10), "math")
    big = max(n for n, _ in series)
    fr = sorted(series[(big, "lam0")], key=lambda r: r["a4"])
    kap = []
    for r in fr:
        rho_bar = r["int_rho"] / (2.0 * r["Vol7"] * geo["W"])
        kap.append((r["a4"], need_krho(math.exp((2.0 - float(BE)) * r["a4"])) / rho_bar))
    kmax, kmin = max(k for _, k in kap), min(k for _, k in kap)
    sign_change = kmax > 0 > kmin
    c3_sign_change = sign_change
    gas_positive = all(r["int_rho"] > 0 for r in fr)
    crossing = next(((a, a2) for (a, k), (a2, k2) in zip(kap, kap[1:]) if k * k2 <= 0), None)
    check("C3_record_history_not_sourced_by_the_gas",
          gas_positive and (sign_change or kmax / max(kmin, 1e-300) > 2.0),
          "with the author's weights (Lambda = -10) the record's history needs kappa rho = %s at a4 = 0 and %s at a4 = 2 "
          "(exponentialHistory.authorWeights.historySource_kappaT_minus_Lam; %s), while the x0-averaged Kohn-Sham energy "
          "density of the free gas N = %d is %s (rho_bar = %s at a4 = 0, %s at a4 = 2): kappa = (needed kappa rho)/rho_bar "
          "would have to run from %s to %s along the history, no constant kappa makes the gas the source (with lambda != 0, "
          "C1 excludes it already)"
          % (g6(need_krho(1.0)), g6(need_krho(math.exp((2.0 - float(BE)) * 2.0))),
             ("it changes sign between the dense slices a4 = %s and %s" % (g6(crossing[0]), g6(crossing[1])))
             if crossing is not None else "it keeps its sign",
             big, "positive at every slice" if gas_positive else "NOT positive at every slice",
             g6(fr[0]["int_rho"] / (2.0 * fr[0]["Vol7"] * geo["W"])), g6(fr[-1]["int_rho"] / (2.0 * fr[-1]["Vol7"] * geo["W"])),
             g6(kap[0][1]), g6(kap[-1][1])))
    zm = [s for s in nz if s["N"] == 8]
    gas = [s for s in nz if s["N"] != 8]
    lam_of = {r["id"]: float(r["lambda"]) for r in read_csv(KS_INTEGRALS)}
    ratios = [s["p3_bar"] / s["rho_bar"] for s in zm]
    zm_ok = all((s["rho_bar"] > 0) == (lam_of[s["id"]] < 0) for s in zm) and all(0.0 < q < 1.0 for q in ratios)
    gas_ok = all(s["rho_bar"] > 0 and s["rho_bar"] + s["p3_bar"] > 0 for s in gas)
    viol = sorted(s["id"] for s in zm if s["rho_bar"] + s["p3_bar"] < 0)
    check("C4_source_signs", zm_ok and gas_ok and bool(zm) and bool(gas),
          "the gas of N = %s (the fold band and the zero modes) has rho_bar > 0 and rho_bar + p3_bar > 0 in all %d nonzero "
          "states. The %d nonzero N = 8 states fill only k = 0 levels (no 3-momentum, so p3 = e_int, the interaction energy "
          "density; to first order in lambda, where S = 0, rho_bar and p3_bar both equal -lambda <n^2>/32): rho_bar has the "
          "sign of -lambda and the self-consistent p3_bar/rho_bar lies in [%s, %s], "
          "so for lambda > 0 the averaged null energy condition along 3-space is VIOLATED (rho_bar + p3_bar < 0) in %d states "
          "(%s); for lambda = 0, p3_bar = rho_bar/3 exactly and p0_bar = p_t_bar = 0 (D0)"
          % (", ".join(sorted({str(s["N"]) for s in gas}, key=int)), len(gas), len(zm), g6(min(ratios)), g6(max(ratios)), len(viol),
             ", ".join(viol)))

    # ---------------- D
    W = geo["W"]
    d0dev, d0n = 0.0, 0
    Cs = {}
    for (n, tag), rs in series.items():
        if tag != "lam0" or n == 8:
            continue
        c0 = None
        for r in rs:
            rho_bar = r["int_rho"] / (2.0 * r["Vol7"] * W)
            b4 = r["b4_over_b4_0"]
            c = rho_bar * b4 ** 2
            c0 = c if c0 is None else c0
            sc = max(abs(r["int_rho"]), 1e-300)
            d0dev = max(d0dev, abs(c / c0 - 1.0), abs(r["int_p3"] - r["int_rho"] / 3.0) / sc, abs(r["int_p0"]) / sc,
                        abs(r["int_p_t"]) / sc)
            d0n += 1
        Cs[n] = c0
    check("D0_free_gas_average_exact", d0n > 0 and d0dev <= TOL_EXACT,
          "the x0-averaged free gas (lambda = 0, N = %s) along the dense history (%d states): rho_bar b4^2 is constant, "
          "p3_bar = rho_bar/3 and p0_bar = p_t_bar = 0, to %s. Reason (ks-theory.json blockEquation): every occupied orbital is "
          "the fold-band orbital (e^{f M y}, 0) with eps = e^{-a4} |k|, so E = e^{-a4} E(0) for EVERY (a4, b4) (f does not "
          "enter), and the proper cell volume is ell^3 v_t e^{-a4} b4^2 2W: rho_bar = C b4^{-2} with C = E(0)/(2 ell^3 v_t W) "
          "(N = %s: C = %s) as long as the gas stays on the fold band (the Fermi level e^{-a4} k_F below the bulk edge, which "
          "depends on f = e^{-a4} b4^{1/2}). So the averaged free gas is a source of the x0-averaged equations for any history"
          % (", ".join(str(n) for n in sorted(Cs)), d0n, g6(d0dev), ", ".join(str(n) for n in sorted(Cs)),
             ", ".join(g6(Cs[n]) for n in sorted(Cs))))
    # Fermi wave numbers of the free series (the occupied fold-band shell with the largest |k| at a4,0 = 0)
    kF = {}
    dk = float(params["physics"]["dk"])
    for n in sorted(Cs):
        lv = read_csv(KS_LEVELS / ("N%d_lam0_a00.csv" % n))
        kF[n] = max(float(r["k"]) for r in lv if float(r["f"]) > 0)
    L = geo["L"]
    cases = []
    for g in GRAVITY:
        th = theories[g[0]]
        F4h = th["F4"](float(A0), float(BE * A0), 1.0, 0.0)       # the x4 component at the start, without Lambda
        if g[4] is not None:
            choices = [("Lambda = %s" % g[4], float(g[4]), -(F4h + float(g[4])))]
        else:
            choices = [("sigma0 = %s" % s, -float(s) - F4h, float(s)) for s in SIGMAS]
        for n in sorted(Cs):
            for (label, Lam_, sig0) in choices:
                r1 = integrate_case(th, Lam_, sig0, H_M1, kF[n], L)
                r2 = integrate_case(th, Lam_, sig0, H_M2, kF[n], L)
                cases.append({"gravity": g[0], "series": "N%d_lam0" % n, "label": label, "Lambda": Lam_, "sigma0": sig0,
                              "m1": r1, "m2": r2})
    same_ev = all(c["m1"]["event"] == c["m2"]["event"] for c in cases)
    worst_m = 0.0
    for c in cases:
        for xo, y1 in c["m1"]["out"].items():
            y2 = c["m2"]["out"].get(xo)
            if y2 is None:
                continue
            worst_m = max(worst_m, max(abs(a - b) / max(1.0, abs(a)) for a, b in zip(y1, y2)))
    check("D1_two_step_sizes_agree", same_ev and worst_m <= TOL_METHODS,
          "%d cases integrated with RK4 at the base steps h = %s and h = %s (units 1/H; substeps with step-doubling "
          "error control, local error <= %s): the same outcome in every case: %s; (a4, ln b4, "
          "a4', u) at the common output times agree to %s (relative to max(1, |x|); tolerance %s)"
          % (len(cases), g6(H_M1), g6(H_M2), g6(TOL_STEP), same_ev, g6(worst_m), g6(TOL_METHODS)))
    worst_c = max(c["m1"]["constraint"] for c in cases)
    check("D3_constraint_kept_along_the_solutions", worst_c <= TOL_CONSTRAINT,
          "the x4 constraint F4(a4', u, kk) + kappa rho_bar = 0 imposed at x4 = 0 (it fixes sigma0 for the author's weights, "
          "Lambda for the others) stays satisfied along every integrated solution (A3 with A5): largest residual relative to "
          "the scale of its terms %s (tolerance %s)" % (g6(worst_c), g6(TOL_CONSTRAINT)))
    auth = [c for c in cases if c["gravity"] == "author"]
    auth_s = "; ".join("%s: sigma0 = kappa rho_bar(0) = %s, outcome %s at x4 = %s (a4 = %s, b4 = %s, a4'/H = %s, u/H = %s)" % (
        c["series"], g6(c["sigma0"]), c["m1"]["event"], g6(c["m1"]["x_end"]), g6(c["m1"]["y_end"][0]),
        g6(math.exp(c["m1"]["y_end"][1])), g6(c["m1"]["y_end"][2]), g6(c["m1"]["y_end"][3])) for c in auth)
    hist_dev = []
    for c in auth:
        y = c["m1"]["out"].get(0.5)
        if y is not None:
            hist_dev.append(max(abs(y[2] - 1.0), abs(y[3] - 4.0 / 3.0)))
    check("D2_author_weights_from_the_record_history", len(auth) == len(Cs) and all(math.isfinite(c["sigma0"]) for c in auth),
          "the author's weights (Lambda = -10): started on the record's history (a4'(0) = H, u(0) = (4/3) H, b4(0) = 1) the "
          "constraint fixes kappa rho_bar(0) = %s for both series (%s, since rho_bar > 0 for the free gas); the "
          "second-order system then evolves the rates: %s. Deviation of (a4'/H, u/H) from the record's (1, 4/3) at "
          "x4 = 0.5/H: %s. The record's history needs the source of A6, the averaged free gas gives a different evolution"
          % (g6(auth[0]["sigma0"]) if auth else "-",
             ("kappa > 0" if auth[0]["sigma0"] > 0 else "kappa < 0" if auth[0]["sigma0"] < 0 else "kappa = 0") if auth else "-",
             auth_s, ", ".join(g6(v) for v in hist_dev) or "the solution ended before"))
    events = sorted({c["m1"]["event"] for c in cases})
    counts = {e: sum(1 for c in cases if c["m1"]["event"] == e) for e in events}
    check("D4_outcomes", len(cases) == len(Cs) * (1 + 3 * len(SIGMAS)),
          "%d cases (%d free series x (the author's weights + 3 theories x %d values of sigma0 = kappa rho_bar(0)/H^2, Lambda "
          "from the constraint)): outcomes %s (regular: through x4 = %s/H; a4_turns: a4' reaches 0; leaves_fold_band: the "
          "Fermi level of the gas reaches the bulk edge, beyond which the averaged source is no longer C b4^{-2}; "
          "singular_second_order_system: det J changes sign inside a substep or falls to %s |det J(0)|; runaway: |a4'| "
          "or |u| > 1e3 H; step_underflow: a substep below h 2^-%d would be needed); every case: "
          "results/ks-source-a4-cases.csv"
          % (len(cases), len(Cs), len(SIGMAS), ", ".join("%s %d" % (e, counts[e]) for e in events), g6(X4_END),
             g6(DET_SINGULAR), SUB_LEVELS))

    # ---------------- outputs
    mom_cols = ["id", "N", "lambda_tag", "a4", "zero_source", "rho_bar", "p3_bar", "p_t_bar", "p0_bar", "n_bar",
                "int_rel", "cons_fd_rel", "var_ratio", "c2_ratio", "c2_bar_rel", "mu1_rho", "mu1_p3", "mu1_p_t", "mu1_p0"]
    buf = io.StringIO()
    buf.write(",".join(mom_cols) + "\n")
    for sid in sorted(states):
        s = states[sid]
        vals = []
        for c in mom_cols:
            if c == "zero_source":
                vals.append("true" if s["zero"] else "false")
            elif c in ("id", "lambda_tag"):
                vals.append(s[c])
            elif c == "N":
                vals.append(str(s["N"]))
            else:
                v = s.get(c)
                vals.append("" if v is None else e12(float(v)))
        buf.write(",".join(vals) + "\n")
    OUT_MOMENTS.parent.mkdir(parents=True, exist_ok=True)
    OUT_MOMENTS.write_bytes(buf.getvalue().encode("utf-8"))
    case_cols = ["gravity", "series", "case", "Lambda", "sigma0", "outcome", "x4_end", "a4_end", "b4_end", "a4p_end", "u_end"]
    for xo in X4_OUT:
        case_cols += ["a4_x%s" % g6(xo), "b4_x%s" % g6(xo), "a4p_x%s" % g6(xo), "u_x%s" % g6(xo)]
    case_cols += ["constraint_residual", "m2_outcome"]
    buf = io.StringIO()
    buf.write(",".join(case_cols) + "\n")
    for c in cases:
        m1 = c["m1"]
        row = [c["gravity"], c["series"], c["label"], e12(c["Lambda"]), e12(c["sigma0"]), m1["event"], e12(m1["x_end"]),
               e12(m1["y_end"][0]), e12(math.exp(m1["y_end"][1])), e12(m1["y_end"][2]), e12(m1["y_end"][3])]
        for xo in X4_OUT:
            y = m1["out"].get(xo)
            row += ([e12(y[0]), e12(math.exp(y[1])), e12(y[2]), e12(y[3])] if y is not None else ["", "", "", ""])
        row += [e12(m1["constraint"]), c["m2"]["event"]]
        buf.write(",".join(row) + "\n")
    OUT_CASES.parent.mkdir(parents=True, exist_ok=True)
    OUT_CASES.write_bytes(buf.getvalue().encode("utf-8"))
    inputs = [A4_JSON, KS_PARAMS, KS_INTEGRALS, KS_ADIABATIC, KS_HISTORY, KS_THEORY, CONDITIONS, DENSE]
    prof = sorted(KS_PROFILES.glob("*.csv"))
    n_pass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
    rep = {
        "report": rel(OUT_REPORT),
        "producer": "Revision/field_equations_a4/ks_source/ks_source_a4.py",
        "metric": "the corrected primordial metric of 2026-10-16 (version 2; SPEC section 1)",
        "inputs": {rel(p): sha256(p) for p in inputs},
        "inputProfiles": {"directory": rel(KS_PROFILES), "files": len(prof),
                          "sha256OfSortedDigests": hashlib.sha256("".join(sha256(p) for p in prof).encode()).hexdigest()},
        "assumptions": [
            "The Kohn-Sham states are the instantaneous (adiabatic) states of the record on the PRESCRIBED history a4 = H x4, "
            "b4 = e^{(4/3) H x4}; the cutoff L = 3, the fold convention and the filling convention of Revision/kohn_sham.",
            "Part D replaces the x0-dependent source by its x0 average per proper volume (a dimensional reduction, an "
            "APPROXIMATION: C1 and B3 show that the true source is not x0-independent) and uses the free gas (lambda = 0), "
            "whose average is exact for every (a4, b4) while it stays on the fold band (D0).",
            "The gravity theories and their couplings are the stated ones; kappa and, except for the author's weights, "
            "Lambda are fixed by the constraint at x4 = 0."],
        "conclusions": [
            "No recorded Kohn-Sham state is an admissible source of the corrected metric: every nonzero state depends on x0 "
            "(B3), and the interacting states violate p0 = p_t also after averaging (C1); the off-diagonal condition holds.",
            "The free (lambda = 0) gas is an exact fold-band gas: averaged over x0 it is rho_bar = C b4^{-2}, p3 = rho/3, "
            "p0 = p_t = 0, a source that conserves energy for every a4, b4 (A5, D0).",
            ("The record's history a4 = H x4, b4 = e^{(4/3) H x4} needs a source that changes sign along it (A6, C3); the "
             if c3_sign_change else
             "The record's history a4 = H x4, b4 = e^{(4/3) H x4} needs a source that no constant kappa makes of the gas (A6, "
             "C3); the ") +
            "Kohn-Sham gas does not supply it: the history is a prescribed background without back-reaction.",
            "With the averaged free gas as the source, the x0-averaged equations started on the record's history evolve "
            "differently (D2, D4; outcomes in results/ks-source-a4-cases.csv)."],
        "summary": {"checks": len(CHECKS), "pass": n_pass, "fail": len(CHECKS) - n_pass},
        "checks": CHECKS,
    }
    OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    OUT_REPORT.write_bytes((json.dumps(rep, indent=1, ensure_ascii=False) + "\n").encode("utf-8"))
    OUT_SUMMARY.write_bytes(summary_md(rep, cases, states, slices, sorted(Cs)).encode("utf-8"))
    print("pass %d/%d" % (n_pass, len(CHECKS)))
    return 0 if n_pass == len(CHECKS) else 1


def summary_md(rep: dict, cases: list, states: dict, slices: list, ns: list) -> str:
    L = ["# The field equations for a4 and b4 with the Kohn-Sham source (generated)", "",
         "Generated by `%s`; every number below is from this run (report `%s`, %d/%d checks pass)."
         % (rep["producer"], rep["report"], rep["summary"]["pass"], rep["summary"]["checks"]), "",
         "The corrected primordial metric of 2026-10-16 (version 2). Coordinates: x1, x2, x3 = 3-space (scale factor "
         "e^{a4}); x4 = time; x5, x6, x7 = the extra times (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}); x0 = hidden "
         "direction (Kohn-Sham coordinate y = ln|sin z|/(6H)).", "",
         "## Conclusions", ""]
    for c in rep["conclusions"]:
        L.append("* " + c)
    L += ["", "## Assumptions", ""] + ["* " + a for a in rep["assumptions"]]
    big = ns[-1]
    L += ["", "## Hidden-direction averages along the history (N = %d, lambda = 0 and lambda_1)" % big, "",
          "Proper densities per cell volume (H = m = 1); mu1 = L1 hidden-direction mismatch (check B3); c2 = "
          "|p0_bar - p_t_bar| relative to the largest averaged component (check C1).", "",
          "| state | rho_bar | p3_bar | p_t_bar | p0_bar | mu1_rho | mu1_p3 | c2 |", "| --- " * 8 + "|"]
    for tag in ("lam0", "lamp1"):
        for a in slices:
            s = states.get("N%d_%s_a%02d" % (big, tag, int(round(10 * a))))
            if s is None:
                continue
            L.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
                s["id"], g6(s["rho_bar"]), g6(s["p3_bar"]), g6(s["p_t_bar"]), g6(s["p0_bar"]), g6(s["mu1_rho"]),
                g6(s["mu1_p3"]), g6(s["c2_bar_rel"])))
    L += ["", "## Integrated cases (series N%d_lam0; a4'(0) = H, u(0) = (4/3) H, b4(0) = 1)" % big, "",
          "sigma0 = kappa rho_bar(0)/H^2; Lambda from the constraint at x4 = 0 (the author's weights: Lambda = -10 and sigma0 "
          "from the constraint). Every series and case: `results/ks-source-a4-cases.csv`.", "",
          "| gravity | case | Lambda/H^2 | sigma0 | outcome | x4 reached | a4 there | b4 there | a4'/H there | u/H there |",
          "| --- " * 10 + "|"]
    for c in cases:
        if c["series"] != "N%d_lam0" % big:
            continue
        m1 = c["m1"]
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            c["gravity"], c["label"], g6(c["Lambda"]), g6(c["sigma0"]), m1["event"], g6(m1["x_end"]), g6(m1["y_end"][0]),
            g6(math.exp(m1["y_end"][1])), g6(m1["y_end"][2]), g6(m1["y_end"][3])))
    L += ["", "## Checks", ""]
    for c in rep["checks"]:
        L.append("* **%s** %s: %s" % (c["verdict"], c["name"], c["detail"]))
    L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
