#!/usr/bin/env python3
"""Revision/field_equations_a4/ks_source/ks_source_a4.py - the field equations for a4[x4] and b4[x4] (SPEC section 5)
specialised to the Kohn-Sham states of dirac16complex (SPEC section 7, Revision/kohn_sham) as the source.

The metric is the author's metric with b4(x4) in the three extra-time components (b4 a function of x4, never 1;
SPEC section 1).  Coordinates as the author names them: x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z);
x4 = time; x5, x6, x7 = the three EXTRA TIMES, which DEFLATE EXPONENTIALLY (scale factor e^{-a4} b4^{1/2} sin^{1/6} z);
x0 = the hidden direction, z = 6 H x0, and the Kohn-Sham hidden coordinate y = ln(sin z)/(6 H) in [-L, 0]
(sqrt|g| dx0 = b4^{3/2} cos z dx0 = b4^{3/2} e^{6Hy} dy).  u = b4'/b4, v = u'.

What this script does (Revision code only; inputs are Revision files, read-only):
  A (exact, sympy, from Revision/field_equations_a4/a4-equations.json, key generalSource)
    the x1 + x5 - 2 x0 combination for general b4 (no longer an identity; it vanishes for b4' = 0 and on the history
    with the author's weights); the off-diagonal equation kappa q40 = cot z u Q(a4', u): a source without T^x4_x0 and
    b4 not constant needs Q = 0, which Einstein gravity (Q = 3H/2) never allows; the x4 constraint is first order;
    the constraint propagation (Bianchi) identity with u; the x0 conservation identity in the y coordinate; the real
    branches of Q(H, u) = 0 of the stated theories.
  B (numerical, the recorded Kohn-Sham ground-state profiles; densities per Vol_7(a4,0) = ell^3 v_t e^{(3/2) beta a4,0},
    the proper ones times b4(0)^{3/2})
    the x0 conservation identity on every profile; the integrated identity; the hidden-direction mismatch of every
    component (the x0-independent part of a profile is its weighted average); the source-condition report verified.
  C (the hidden-direction moments along the record's history a4 = H x4, b4 = b4(0) e^{(4/3) H x4})
    the averaged algebraic condition; the averaged energy relation with the b4 term; the x4 moment of the author's
    equations needs the constant source kappa rho = -2/27 (H = 1), which no Kohn-Sham series supplies; source signs.
  D (integration, an APPROXIMATION stated as such)
    the truncated system "x4 moment + off-diagonal equation" (both exact necessary conditions; together algebraic in
    (a4', u) for a given source) for the free gas series (lambda = 0), whose averaged source is known for ANY b4
    (rho_bar = E(a4)/(cell volume b4^{3/2}), E independent of b4), integrated over a4 in [0, 2] from a4'(0) = H on
    every real branch of Q(H, u) = 0, with two methods; the residuals of the dropped second-order moments are
    reported; the outcomes are classified (regular / turning point / branch point / no real solution / u = 0).

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
KS_ADIABATIC = KS / "results" / "adiabatic" / "adiabaticity.csv"
KS_HISTORY = KS / "results" / "adiabatic" / "history.json"
KS_THEORY = KS / "ks-theory.json"
WAVE1 = A4DIR / "reports" / "ks-source-conditions.json"   # the source-condition report, verified here (check B0)
# the dense free-gas history (41 slices a4 = 0, 0.05, ..., 2; the same solver and history, written by
# Revision/dark_sector/dirac16complex/compute/run_ks_history.py): the source of the integration (part D)
DENSE = REV / "dark_sector" / "dirac16complex" / "outputs" / "ks-history-dense.csv"
OUT_MOMENTS = HERE / "results" / "ks-source-moments.csv"
OUT_CASES = HERE / "results" / "ks-source-a4-cases.csv"
OUT_REPORT = HERE / "reports" / "ks-source-a4.json"
OUT_SUMMARY = HERE / "reports" / "ks-source-a4-summary.md"

CHECKS: list[dict] = []

# tolerances (stated, with their reasons)
TOL_INTEGRAL = 1e-6      # Simpson on the 151-point output grid against the solver's own integrals (found ~1e-8)
TOL_CONS_FD = 1e-3       # 4th-order finite differences on the output grid dy = 0.02 (truncation ~ dy^4)
TOL_IDENTITY = 1e-6      # integrated x0 identity, from the solver's integrals and end values
TOL_ENERGY_SOLVER = 1e-6  # solver: dE/da4 by finite differences (step 2e-3) against the EMT formula
TOL_ENERGY_SLICES = 2e-2  # between slices (step 0.5): Simpson of the energy relation against the change of E
TOL_METHODS = 5e-3       # M1 (Hermite source, step 1e-3) against M2 (spline of ln E, step 2e-3)
TOL_BIANCHI = 1e-8       # the propagation identity of the dropped moments along the solutions, relative
NEWTON_TOL = 1e-14

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
SERIES = ["N136_lam0", "N688_lam0"]     # the free gas: its averaged source is known for any b4
SIGMAS = [Fraction(-10), Fraction(-1), Fraction(-1, 10), Fraction(1, 10), Fraction(1), Fraction(10)]
A0 = Fraction(1)        # initial rate a4'(0) = A0 H (the rate of the prescribed Kohn-Sham history, A = 1)


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
    global KS_PARAMS, KS_PROFILES, KS_INTEGRALS, KS_ADIABATIC, KS_HISTORY, OUT_MOMENTS, OUT_CASES, OUT_REPORT, OUT_SUMMARY
    KS_PARAMS = ks_results / "parameters.json"
    KS_PROFILES = ks_results / "ground" / "profiles"
    KS_INTEGRALS = ks_results / "ground" / "emt-integrals.csv"
    KS_ADIABATIC = ks_results / "adiabatic" / "adiabaticity.csv"
    KS_HISTORY = ks_results / "adiabatic" / "history.json"
    OUT_MOMENTS = out / "results" / "ks-source-moments.csv"
    OUT_CASES = out / "results" / "ks-source-a4-cases.csv"
    OUT_REPORT = out / "reports" / "ks-source-a4.json"
    OUT_SUMMARY = out / "reports" / "ks-source-a4-summary.md"


# ---------------------------------------------------------------------------------------------------------------------
# A: exact identities (sympy) from a4-equations.json
# ---------------------------------------------------------------------------------------------------------------------
ad1, ad2, uu, vv, H, Lam, kap = sp.symbols("ad1 ad2 uu vv H Lam kappa")
al1, al2, al3 = sp.symbols("alpha1 alpha2 alpha3")
p3, pt, p0, rho, p0y, cc, q40, q04 = sp.symbols("p3 pt p0 rho p0y cc q40 q04")
d0p0, d4q40, bd1, bb = sp.symbols("d0p0 d4q40 bd1 bb")
LOC = {"ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "H": H, "alpha1": al1, "alpha2": al2, "alpha3": al3, "Lam": Lam,
       "kappa": kap, "p3": p3, "pt": pt, "p0": p0, "rho": rho, "cc": cc, "q40": q40, "q04": q04, "d0p0": d0p0,
       "d4q40": d4q40, "bd1": bd1, "bb": bb}


def parse(s: str) -> sp.Expr:
    """an expression (or an equation lhs == rhs, returned as lhs - rhs) of a4-equations.json"""
    if s.count("==") == 1:
        lhs, rhs = s.split("==")
        return parse(lhs) - parse(rhs)
    s2 = s.replace("^", "**")
    if not re.fullmatch(r"[0-9A-Za-z_+\-*/(). ]+", s2):
        err("unexpected characters in an expression of a4-equations.json: %r" % s)
    return sp.sympify(s2, locals=LOC)


def lhs_of(s: str) -> sp.Expr:
    if s.count("==") != 1:
        err("expected an equation 'lhs == rhs' in a4-equations.json: %r" % s[:80])
    return parse(s.split("==")[0])


def weights_of(g) -> dict:
    return {al1: sp.Rational(g[1].numerator, g[1].denominator), al2: sp.Rational(g[2].numerator, g[2].denominator),
            al3: sp.Rational(g[3].numerator, g[3].denominator)}


def part_a(a4: dict) -> dict:
    gs = a4["generalSource"]
    S4 = lhs_of(gs["constraint_x4"]["input"]) - Lam           # sum_k alpha_k E^x4_x4 (the constraint: S4 + Lam = -kappa rho)
    S1 = lhs_of(gs["space_x1_eq_x2_eq_x3"]["input"]) - Lam
    S5 = lhs_of(gs["extraTime_x5_eq_x6_eq_x7"]["input"]) - Lam
    S0 = lhs_of(gs["hidden_x0"]["input"]) - Lam
    lam_lin = all(not sp.expand(S).has(Lam) for S in (S4, S1, S5, S0))
    Q = parse(gs["offDiagonalFactor_Q"]["input"])
    ident_rec = lhs_of(gs["identity_x1_plus_x5_minus_2x0"]["input"])
    I = sp.expand(S1 + S5 - 2 * S0)
    hist = {ad1: H, ad2: 0, uu: sp.Rational(4, 3) * H, vv: 0}
    wa = weights_of(GRAVITY[1])
    wa = {k: v / H ** (2 * i) for i, (k, v) in enumerate(wa.items())}
    I_b4const = sp.expand(I.subs({uu: 0, vv: 0}))
    I_hist = sp.simplify(I.subs(hist).subs(wa))
    I_ein = sp.factor(sp.expand(I.subs({al1: 1, al2: 0, al3: 0})))
    check("A1_x1_x5_x0_combination_with_b4", lam_lin and sp.expand(I - ident_rec) == 0 and I_b4const == 0 and I_hist == 0
          and I_ein != 0,
          "with S_mu = sum_k alpha_k E_(k)^mu_mu (a4-equations.json generalSource, each component linear in Lambda with "
          "coefficient 1: %s): S1 + S5 - 2 S0 equals generalSource.identity_x1_plus_x5_minus_2x0 exactly, so the "
          "x1 + x5 - 2 x0 combination reads kappa (p3 + p_t - 2 p0) = I(a4', a4'', u, v); I = 0 for u = v = 0 (b4 "
          "constant: the identity of the withdrawn metric b4 = 1), I = %s on the history a4 = H x4, b4 ~ e^{(4/3) H x4} "
          "with the author's weights, but I is not an identity for general b4 (Einstein: I = %s)"
          % (lam_lin, I_hist, sp.sstr(I_ein)))
    off = lhs_of(gs["offDiagonal_x4x0"]["input"])
    off_ok = sp.expand(off - cc * uu * Q) == 0
    Q_ein = sp.simplify(Q.subs({al1: 1, al2: 0, al3: 0}))
    check("A2_offdiagonal_equation_needs_Q_zero", off_ok and Q_ein == sp.Rational(3, 2) * H,
          "generalSource.offDiagonal_x4x0: sum_k alpha_k E_(k)^x4_x0 = cot z u Q(a4', u) exactly (Q = generalSource."
          "offDiagonalFactor_Q); a source without T^x4_x0 (q40 = 0: every Kohn-Sham state, ks-theory.json emt."
          "offDiagonal) and b4 not constant (u != 0) therefore needs Q(a4', u) = 0 at every instant. Einstein gravity: "
          "Q = %s, never zero: with such a source b4' = 0 is forced, so in Einstein gravity NO history with b4 not "
          "constant has a Kohn-Sham source (and none with the record's history)" % sp.sstr(Q_ein))
    first = not S4.has(ad2) and not S4.has(vv)
    lin = all(sp.degree(sp.expand(S), ad2) <= 1 and sp.degree(sp.expand(S), vv) <= 1 for S in (S1, S5, S0))
    check("A3_constraint_first_order", first and lin,
          "the x4 component S4(a4', u) + Lambda = -kappa rho contains no a4'' and no v (a constraint, first order in "
          "a4 and ln b4); the x1, x5 and x0 components are linear in (a4'', v): the second-order equations")
    prop = sp.expand(sp.diff(S4, ad1) * ad2 + sp.diff(S4, uu) * vv
                     - (3 * ad1 * (S1 - S5) + sp.Rational(3, 2) * uu * (S5 - S4) + 6 * H * uu * Q))
    check("A4_constraint_propagation_with_b4", prop == 0,
          "d/dx4 S4 = 3 a4' (S1 - S5) + (3/2) u (S5 - S4) + 6 H u Q identically (the x4 component of the Bianchi "
          "identity; a4-equations.json generalSource.constraint_propagation); with Q = 0 and a source obeying the "
          "averaged conservation d rho/dx4 = -3 a4' (p3 - p_t) - (3/2) u (rho + p_t), the constraint therefore propagates "
          "exactly into the combination 3 a4' (R1 - R5) + (3/2) u (R5 - R4) = 0 of the residuals R_mu of the "
          "second-order equations: one combination of them holds automatically, the other two are independent")
    cons = parse(gs["conservation_x0"]["input"]).subs({q40: 0, d4q40: 0}).subs(d0p0, cc * p0y)
    in_y = sp.expand(cons / cc - (p0y + 6 * H * p0 - 3 * H * (p3 + pt)))
    x0s, ys = sp.symbols("x0 y", positive=True)
    z = 6 * H * x0s
    dy_dx0 = sp.simplify(sp.diff(sp.log(sp.sin(z)) / (6 * H), x0s) - sp.cot(z)) == 0
    vol = sp.simplify(sp.cos(z) / sp.cot(z) - sp.sin(z)) == 0
    check("A5_x0_conservation_in_y", in_y == 0 and dy_dx0 and vol,
          "y = ln(sin z)/(6H): dy/dx0 = cot z and sqrt|g| dx0 = b4^{3/2} cos z dx0 = b4^{3/2} e^{6Hy} dy; generalSource."
          "conservation_x0 with q40 = 0 is cot z [p0_y + 6 H p0 - 3 H (p3 + p_t)] = 0 for every b4, so on shell "
          "p3 + p_t - 2 p0 = p0_y/(3H) EXACTLY and int_{-L}^{0} e^{6Hy} (p3 + p_t) dy = [e^{6Hy} p0]_{-L}^{0}/(3H)")
    theories, branches_txt = {}, []
    for g in GRAVITY:
        w = weights_of(g)
        sub = {al1: w[al1], al2: w[al2], al3: w[al3], H: 1}
        Qn, S4n = sp.expand(Q.subs(sub)), sp.expand(S4.subs(sub))
        S1n, S5n, S0n = (sp.expand(S.subs(sub)) for S in (S1, S5, S0))
        Qu0 = sp.Poly(sp.expand(Qn.subs(ad1, sp.Rational(A0.numerator, A0.denominator))), uu)
        if Qu0.degree() <= 0:
            roots = []
        else:
            roots = sorted([r for r in sp.Poly(Qu0, uu).nroots(n=30) if abs(sp.im(r)) < 1e-25], key=lambda r: float(sp.re(r)))
            roots = [float(sp.re(r)) for r in roots]
        exact = [sp.nsimplify(r) for r in sp.solve(Qu0.as_expr(), uu)] if Qu0.degree() > 0 else []
        real_exact = [r for r in exact if r.is_real]
        theories[g[0]] = {
            "Q": sp.lambdify((ad1, uu), Qn, "math"), "Qa": sp.lambdify((ad1, uu), sp.diff(Qn, ad1), "math"),
            "Qu": sp.lambdify((ad1, uu), sp.diff(Qn, uu), "math"),
            "S4": sp.lambdify((ad1, uu), S4n, "math"), "S4a": sp.lambdify((ad1, uu), sp.diff(S4n, ad1), "math"),
            "S4u": sp.lambdify((ad1, uu), sp.diff(S4n, uu), "math"),
            "S1": sp.lambdify((ad1, ad2, uu, vv), S1n, "math"), "S5": sp.lambdify((ad1, ad2, uu, vv), S5n, "math"),
            "S0": sp.lambdify((ad1, ad2, uu, vv), S0n, "math"),
            "roots": [r for r in roots if abs(r) > 1e-12], "root_zero": any(abs(r) <= 1e-12 for r in roots),
            "Qstr": sp.sstr(Qn), "S4str": sp.sstr(S4n), "exact_roots": [sp.sstr(r) for r in real_exact],
        }
        branches_txt.append("%s: Q(H, u) = %s, real roots u/H = %s" % (
            g[0], sp.sstr(sp.expand(Qn.subs(ad1, 1))), [sp.sstr(r) for r in real_exact] or "none"))
    ok6 = (theories["einstein"]["roots"] == [] and not theories["einstein"]["root_zero"]
           and theories["author"]["root_zero"] and len(theories["author"]["roots"]) == 1
           and abs(theories["author"]["roots"][0] - 4 / 3) < 1e-14
           and len(theories["egb"]["roots"]) == 2 and all(r < 0 for r in theories["egb"]["roots"])
           and theories["lovelock3"]["roots"] == [])
    check("A6_branches_at_the_initial_rate", ok6,
          "Q(a4' = H, u) = 0 (H = 1) for the stated theories: %s. So a history that starts with a4'(0) = H and has a "
          "source without T^x4_x0 has u(0) = 4/3 H for the author's weights (u = 0 is the excluded constant b4: the "
          "record's history is this branch), u(0) in the two negative roots for the stated Gauss-Bonnet case, and does "
          "not exist in Einstein gravity and in the stated cubic Lovelock case (no real root)" % "; ".join(branches_txt))
    return theories


# ---------------------------------------------------------------------------------------------------------------------
# helpers: polynomials, interpolation, quadrature
# ---------------------------------------------------------------------------------------------------------------------
def hermite(xs, fs, ds, x):
    """piecewise cubic Hermite interpolant (values fs, derivatives ds at nodes xs) and its derivative"""
    i = 0
    while i < len(xs) - 2 and x > xs[i + 1]:
        i += 1
    h = xs[i + 1] - xs[i]
    t = (x - xs[i]) / h
    h00, h10, h01, h11 = 2 * t**3 - 3 * t**2 + 1, t**3 - 2 * t**2 + t, -2 * t**3 + 3 * t**2, t**3 - t**2
    v = h00 * fs[i] + h10 * h * ds[i] + h01 * fs[i + 1] + h11 * h * ds[i + 1]
    dh00, dh10, dh01, dh11 = 6 * t**2 - 6 * t, 3 * t**2 - 4 * t + 1, -6 * t**2 + 6 * t, 3 * t**2 - 2 * t
    dv = (dh00 * fs[i] + dh01 * fs[i + 1]) / h + dh10 * ds[i] + dh11 * ds[i + 1]
    return v, dv


def natural_spline(xs, fs):
    n = len(xs)
    h = [xs[i + 1] - xs[i] for i in range(n - 1)]
    al = [0.0] * n
    for i in range(1, n - 1):
        al[i] = 3 / h[i] * (fs[i + 1] - fs[i]) - 3 / h[i - 1] * (fs[i] - fs[i - 1])
    l, mu, zz = [1.0] * n, [0.0] * n, [0.0] * n
    for i in range(1, n - 1):
        l[i] = 2 * (xs[i + 1] - xs[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        zz[i] = (al[i] - h[i - 1] * zz[i - 1]) / l[i]
    c, b, d = [0.0] * n, [0.0] * (n - 1), [0.0] * (n - 1)
    for j in range(n - 2, -1, -1):
        c[j] = zz[j] - mu[j] * c[j + 1]
        b[j] = (fs[j + 1] - fs[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    def ev(x):
        j = 0
        while j < n - 2 and x > xs[j + 1]:
            j += 1
        dx = x - xs[j]
        return fs[j] + b[j] * dx + c[j] * dx * dx + d[j] * dx ** 3
    return ev


def simpson(vals, h):
    n = len(vals) - 1
    if n % 2:
        raise ValueError("Simpson needs an even number of intervals")
    return h / 3 * (vals[0] + vals[-1] + 4 * sum(vals[1:-1:2]) + 2 * sum(vals[2:-1:2]))


GL = None


def gauss_legendre(n=48):
    global GL
    if GL is None:
        xs, ws = [], []
        for i in range(1, n + 1):
            x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
            for _ in range(100):
                L0, L1 = 1.0, x
                for k in range(2, n + 1):
                    L0, L1 = L1, ((2 * k - 1) * x * L1 - (k - 1) * L0) / k
                dp = n * (x * L1 - L0) / (x * x - 1)
                dx = L1 / dp
                x -= dx
                if abs(dx) < 1e-16:
                    break
            xs.append(x)
            ws.append(2 / ((1 - x * x) * dp * dp))
        GL = (xs, ws)
    return GL


# ---------------------------------------------------------------------------------------------------------------------
# B, C: the Kohn-Sham states
# ---------------------------------------------------------------------------------------------------------------------
def read_csv(p: Path) -> list:
    with p.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def part_bc(params: dict) -> tuple:
    phys = params["physics"]
    Hn = float(phys["H"])
    L = float(phys["L_tipCutoff"])
    vol0 = float(phys["Vol7AtA4Zero"])
    beta = float(phys["historyBeta"])
    slices = [float(s) for s in phys["slicesA4"]]
    if Hn != 1.0:
        err("the analysis assumes the solver units H = 1 (parameters.json physics.H = %s)" % Hn)
    wvol = (1 - math.exp(-6 * Hn * L)) / (6 * Hn)          # int_{-L}^{0} e^{6Hy} dy
    integ = {r["id"]: r for r in read_csv(KS_INTEGRALS)}
    adia = {r["id"]: r for r in read_csv(KS_ADIABATIC)}
    files = sorted(KS_PROFILES.glob("*.csv"))
    if len(files) != len(integ):
        err("profiles (%d) and emt-integrals rows (%d) differ" % (len(files), len(integ)))
    states = {}
    for p in files:
        rows = [{k: float(v) for k, v in r.items()} for r in read_csv(p)]
        ys = [r["y"] for r in rows]
        h = ys[1] - ys[0]
        if abs(ys[0] + L) > 1e-12 or abs(ys[-1]) > 1e-12 or any(abs(ys[i + 1] - ys[i] - h) > 1e-12
                                                                 for i in range(len(ys) - 1)):
            err("profile %s is not on a uniform grid from -L to 0" % p.name)
        w = [math.exp(6 * Hn * y) for y in ys]
        comp = {c: [r[c] for r in rows] for c in ("rho", "p3", "p_t", "p0")}
        sid = p.stem
        it = integ[sid]
        a4v = float(it["a4"])
        vol7 = vol0 * math.exp(1.5 * beta * a4v)            # Vol_7(a4,0) of the record (units of b4(0)^{3/2})
        st = {"id": sid, "N": int(float(it["N"])), "lambda_tag": it["lambda_tag"], "lambda": float(it["lambda"]),
              "a4": a4v, "h": h, "ys": ys, "vol7": vol7,
              "E": float(it["int_rho"]), "P3": float(it["int_p3"]), "Pt": float(it["int_p_t"]), "P0": float(it["int_p0"])}
        scale = max(max(abs(v) for v in comp[c]) for c in comp)
        st["zero"] = scale == 0.0
        # B1: integrals against the solver
        worst_int = 0.0
        for c, ic in (("rho", "int_rho"), ("p3", "int_p3"), ("p_t", "int_p_t"), ("p0", "int_p0")):
            I = simpson([w[i] * comp[c][i] for i in range(len(ys))], h)
            st[c + "_bar"] = I / wvol
            ref = float(it[ic]) / (2 * vol7)
            den = max(abs(ref), max(abs(float(it[k])) for k in ("int_rho", "int_p3", "int_p_t", "int_p0")) / (2 * vol7))
            if den > 0:
                worst_int = max(worst_int, abs(I - ref) / den)
        st["int_rel"] = worst_int
        if st["zero"]:
            states[sid] = st
            continue
        # B2: pointwise x0 conservation by 4th-order central differences
        p0v, s = comp["p0"], [comp["p3"][i] + comp["p_t"][i] for i in range(len(ys))]
        worst = 0.0
        for i in range(2, len(ys) - 2):
            d = (-p0v[i + 2] + 8 * p0v[i + 1] - 8 * p0v[i - 1] + p0v[i - 2]) / (12 * h)
            res = d + 6 * Hn * p0v[i] - 3 * Hn * s[i]
            den = max(abs(d), abs(6 * Hn * p0v[i]), abs(3 * Hn * s[i]))
            if den > 0:
                worst = max(worst, abs(res) / den)
        st["cons_fd_rel"] = worst
        st["var_ratio"] = (max(comp["rho"]) - min(comp["rho"])) / scale
        st["int_ratio"] = ((float(it["int_p3"]) + float(it["int_p_t"])) / (2 * float(it["int_p0"]))
                           if float(it["int_p0"]) != 0.0 else None)
        st["alg_pointwise_rel"] = max(abs(s[i] - 2 * p0v[i]) for i in range(len(ys))) / scale
        # B3: integrated identity (solver integrals and end values): int (p3 + p_t) = 2 Vol7 [e^{6Hy} p0]/(3H)
        lhs = float(it["int_p3"]) + float(it["int_p_t"])
        rhs = 2 * vol7 * (float(it["p0_brane"]) - math.exp(-6 * Hn * L) * float(it["p0_tip"])) / (3 * Hn)
        st["identity_rel"] = abs(lhs - rhs) / max(abs(lhs), abs(rhs), 1e-300)
        # B4: L2(e^{6Hy}) mismatch of every component
        half = (len(ys) - 1) // 2              # index of y = -L/2; y in [-L, -L/2] is the tip half of the patch
        if abs(ys[half] + L / 2) > 1e-12:
            err("y = -L/2 is not a grid point of %s" % p.name)
        for c in comp:
            mean = st[c + "_bar"]
            num = simpson([w[i] * (comp[c][i] - mean) ** 2 for i in range(len(ys))], h)
            den = simpson([w[i] * comp[c][i] ** 2 for i in range(len(ys))], h)
            st["mu_" + c] = math.sqrt(max(num, 0.0) / den) if den > 0 else None
            n1 = simpson([w[i] * abs(comp[c][i] - mean) for i in range(len(ys))], h)
            d1 = simpson([w[i] * abs(comp[c][i]) for i in range(len(ys))], h)
            st["mu1_" + c] = n1 / d1 if d1 > 0 else None
            if c == "rho":
                sq = [w[i] * comp[c][i] ** 2 for i in range(len(ys))]      # trapezoid: y = -L/2 is a grid point
                st["tip_share_rho"] = (sum(sq[:half + 1]) - 0.5 * (sq[0] + sq[half])) / (sum(sq) - 0.5 * (sq[0] + sq[-1]))
        a = [s[i] - 2 * p0v[i] for i in range(len(ys))]
        tn = simpson([w[i] * sum(comp[c][i] ** 2 for c in comp) for i in range(len(ys))], h)
        st["alg_L2_rel"] = math.sqrt(simpson([w[i] * a[i] ** 2 for i in range(len(ys))], h) / tn)
        st["alg_bar_rel"] = abs(st["p3_bar"] + st["p_t_bar"] - 2 * st["p0_bar"]) / (
            abs(st["p3_bar"]) + abs(st["p_t_bar"]) + 2 * abs(st["p0_bar"]))
        ad = adia[sid]
        st["dE_fd"], st["dE_emt"] = float(ad["dE_da4_finite_difference"]), float(ad["dE_da4_emt"])
        st["Q_max"] = float(ad["Q_max"])
        states[sid] = st
    return states, slices, {"H": Hn, "L": L, "Vol7_0": vol0, "beta": beta, "wvol": wvol}


def series_of(states: dict, tag: str, slices: list) -> list:
    out = []
    for a in slices:
        sid = "%s_a%02d" % (tag, int(round(10 * a)))
        if sid not in states:
            err("missing Kohn-Sham state %s" % sid)
        out.append(states[sid])
    return out


# ---------------------------------------------------------------------------------------------------------------------
# D: integration of the truncated system {x4 moment, off-diagonal equation} for the free gas
# ---------------------------------------------------------------------------------------------------------------------
def solve_rates(th: dict, a_guess: float, u_guess: float, target: float) -> tuple:
    """Newton for Q(a', u) = 0, S4(a', u) = target (= -Lambda - kappa rho_bar); returns (a', u, det J) or None"""
    a_, u_ = a_guess, u_guess
    scale = 1.0 + abs(target)
    for _ in range(100):
        f1, f2 = th["Q"](a_, u_), th["S4"](a_, u_) - target
        j11, j12, j21, j22 = th["Qa"](a_, u_), th["Qu"](a_, u_), th["S4a"](a_, u_), th["S4u"](a_, u_)
        det = j11 * j22 - j12 * j21
        if det == 0.0:
            return None
        da = (f1 * j22 - f2 * j12) / det
        du = (j11 * f2 - j21 * f1) / det
        a_, u_ = a_ - da, u_ - du
        step = abs(da) + abs(du)
        # converged: a step at the stated tolerance, or (near a fold, where det is small and the step cannot fall below
        # the rounding level eps/|det|) a step below 1e-11 with the residual at the rounding level
        if step <= NEWTON_TOL * (1 + abs(a_) + abs(u_)) or (
                step <= 1e-11 * (1 + abs(a_) + abs(u_))
                and abs(th["Q"](a_, u_)) + abs(th["S4"](a_, u_) - target) <= 1e-14 * scale):
            j11, j12, j21, j22 = th["Qa"](a_, u_), th["Qu"](a_, u_), th["S4a"](a_, u_), th["S4u"](a_, u_)
            return a_, u_, j11 * j22 - j12 * j21
        if not (math.isfinite(a_) and math.isfinite(u_)) or abs(a_) > 1e6 or abs(u_) > 1e6:
            return None
    return None


def integrate_case(th: dict, src: dict, slices: list, u0: float, Lam_: float, sigma0: float, method: str) -> dict:
    """a4 as the independent variable: d ln(b4/b4(0))/da4 = u/a', dx4/da4 = 1/a', with (a', u) from the two algebraic
    equations at each a4; kappa rho_bar(a4, b) = sigma0 E(a4)/E(0) (b4/b4(0))^{-3/2} (free gas)"""
    Efun = src["E_h"] if method == "M1" else src["E_s"]
    hstep = 1e-3 if method == "M1" else 2e-3
    E0 = src["E"][0]
    Qm = src["Q_max"]

    def qfun(a):                    # Q_max at a4' = H, linear between the slices (the free gas: only the frozen part)
        i = min(int(a / (slices[1] - slices[0])), len(slices) - 2)
        t = (a - slices[i]) / (slices[1] - slices[0])
        return (1 - t) * Qm[i] + t * Qm[i + 1]

    def target(a, lb):
        return -Lam_ - sigma0 * Efun(a) / E0 * math.exp(-1.5 * lb)

    state = {"a": 0.0, "lb": 0.0, "x4": 0.0, "ap": float(A0), "u": u0}
    det0 = th["Qa"](float(A0), u0) * th["S4u"](float(A0), u0) - th["Qu"](float(A0), u0) * th["S4a"](float(A0), u0)
    rates = {0.0: (float(A0), u0)}
    event, a_end = "regular", slices[-1]

    def rhs(a, lb, guess):
        sol = solve_rates(th, guess[0], guess[1], target(a, lb))
        if sol is None:
            return None
        ap, u_, det = sol
        return ap, u_, det

    a, lb, x4, guess = 0.0, 0.0, 0.0, (float(A0), u0)
    nsteps = int(round(slices[-1] / hstep))
    for n in range(nsteps):
        k = []
        ok = True
        for (da_, dl_) in ((0.0, None), (0.5, 0), (0.5, 1), (1.0, 2)):
            if dl_ is None:
                r = rhs(a, lb, guess)
                lbs = lb
            else:
                lbs = lb + da_ * hstep * k[dl_][0]
                r = rhs(a + da_ * hstep, lbs, guess)
            if r is None:
                ok = False
                break
            ap, u_, det = r
            if ap <= 1e-6:
                ok = False
                event = "turning_point"
                break
            if abs(u_) <= 1e-9:
                ok = False
                event = "u_zero"
                break
            if det * det0 <= 0:
                ok = False
                event = "fold"
                break
            k.append((u_ / ap, 1.0 / ap))
        if not ok:
            if event == "regular":
                # the real solution of the two algebraic equations ends: by the implicit-function theorem only at a
                # fold (det J = 0) or by running off to infinity
                event = "runaway" if max(abs(guess[0]), abs(guess[1])) > 1e3 else "fold"
            a_end = a
            break
        lb_n = lb + hstep / 6 * (k[0][0] + 2 * k[1][0] + 2 * k[2][0] + k[3][0])
        x4 += hstep / 6 * (k[0][1] + 2 * k[1][1] + 2 * k[2][1] + k[3][1])
        a = (n + 1) * hstep
        lb = lb_n
        r = rhs(a, lb, guess)
        if r is None:
            event, a_end = ("runaway" if max(abs(guess[0]), abs(guess[1])) > 1e3 else "fold"), a
            break
        if qfun(a) * r[0] > 1.0:
            # the instantaneous (adiabatic) Kohn-Sham states are no longer a valid source beyond this point
            event, a_end = "adiabaticity_lost", a
            guess = (r[0], r[1])
            break
        guess = (r[0], r[1])
        for s_ in slices:
            if abs(a - s_) < 1e-9:
                rates[s_] = (r[0], r[1], lb, x4)
    rates[0.0] = (float(A0), u0, 0.0, 0.0)
    end = rates.get(a_end) or ((guess[0], guess[1], lb, x4) if event == "regular" else (guess[0], guess[1], lb, x4))
    return {"event": event, "a_end": a_end, "x4_end": x4 if event == "regular" else end[3] if a_end in rates else x4,
            "rate_end": guess[0], "u_end": guess[1], "lb_end": lb, "rates": rates}


def residuals_at_slices(th: dict, src: dict, res: dict, Lam_: float, sigma0: float, slices: list) -> list:
    """residuals of the dropped second-order moments at the slices reached (a'' and v from the implicit derivatives)"""
    out = []
    E0 = src["E"][0]
    for i, a in enumerate(slices):
        if a not in res["rates"] or a > res["a_end"] + 1e-12:
            continue
        ap, u_, lb = res["rates"][a][0], res["rates"][a][1], res["rates"][a][2]
        f = math.exp(-1.5 * lb)
        E, P3, P0 = src["E"][i], src["P3"][i], src["P0"][i]
        dE = -3.0 * P3                                       # free gas: dE/da4 = -3 P3 (P_t = 0) at fixed b4
        dsig = sigma0 / E0 * f * (dE * ap - 1.5 * E * u_)     # d(kappa rho_bar)/dx4
        j11, j12, j21, j22 = th["Qa"](ap, u_), th["Qu"](ap, u_), th["S4a"](ap, u_), th["S4u"](ap, u_)
        det = j11 * j22 - j12 * j21
        app = (0.0 * j22 - (-dsig) * j12) / det
        v_ = (j11 * (-dsig) - j21 * 0.0) / det
        kp3, kp0 = sigma0 * P3 / E0 * f, sigma0 * P0 / E0 * f
        S1, S5, S0 = th["S1"](ap, app, u_, v_), th["S5"](ap, app, u_, v_), th["S0"](ap, app, u_, v_)
        R1, R5, R0 = S1 + Lam_ - kp3, S5 + Lam_, S0 + Lam_ - kp0
        scale = max(abs(S1), abs(S5), abs(S0), abs(Lam_), abs(kp3), abs(kp0), 1e-300)
        bian = 3 * ap * (R1 - R5) + 1.5 * u_ * R5
        out.append({"a4": a, "R1": R1 / scale, "R5": R5 / scale, "R0": R0 / scale,
                    "bianchi": abs(bian) / (scale * max(3 * abs(ap), 1.5 * abs(u_))), "a2": app, "v": v_})
    return out


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
    for p in (A4_JSON, KS_PARAMS, KS_INTEGRALS, KS_ADIABATIC, KS_HISTORY, KS_THEORY, WAVE1, DENSE):
        if not p.is_file():
            err("missing input %s" % p)
    try:
        a4 = json.loads(A4_JSON.read_text(encoding="utf-8"))
        params = json.loads(KS_PARAMS.read_text(encoding="utf-8"))
        history = json.loads(KS_HISTORY.read_text(encoding="utf-8"))
        kst = json.loads(KS_THEORY.read_text(encoding="utf-8"))
    except (OSError, ValueError) as ex:
        err("cannot read an input: %s" % ex)
    if "p0' + 6H p0 = 3H (p3 + p_t)" not in kst["emt"]["conservationY"]:
        err("ks-theory.json emt.conservationY is not the expected identity")
    if kst["adiabaticity"]["historyBeta"] != "4/3" or not kst["emt"]["offDiagonal"].startswith("T^x4_y = 0"):
        err("ks-theory.json: expected historyBeta 4/3 and T^x4_y = 0 for eigen-orbitals")

    # ---------------- A
    theories = part_a(a4)

    # ---------------- B
    states, slices, geo = part_bc(params)
    nz = [s for s in states.values() if not s["zero"]]
    zero = sorted(s["id"] for s in states.values() if s["zero"])
    wi = max(states.values(), key=lambda s: s["int_rel"])
    check("B1_integrals_reproduced", wi["int_rel"] <= TOL_INTEGRAL,
          "Simpson's rule with the volume weight e^{6Hy} on the 151-point output grid (y = -L ... 0, L = %s) reproduces "
          "results/ground/emt-integrals.csv (int_X = 2 Vol_7(a4,0) int e^{6Hy} X dy, Vol_7(a4,0) = %s e^{(3/2) beta a4,0}, "
          "beta = %s, the doubled system) for all %d states: largest relative difference %s (%s); hence the weighted "
          "average X_bar = int_X / (2 Vol_7(a4,0) W) (per proper cell volume, in units of b4(0)^{-3/2}), "
          "W = int_{-L}^{0} e^{6Hy} dy = %s" % (g6(geo["L"]), g6(geo["Vol7_0"]), g6(geo["beta"]), len(states),
                                               g6(wi["int_rel"]), wi["id"], g6(geo["wvol"])))
    wc = max(nz, key=lambda s: s["cons_fd_rel"])
    check("B2_x0_conservation_on_every_profile", wc["cons_fd_rel"] <= TOL_CONS_FD,
          "p0_y + 6 H p0 - 3 H (p3 + p_t) = 0 (check A5) evaluated with 4th-order central differences on the output "
          "grid (dy = %s) of the %d nonzero profiles: largest residual relative to the largest term %s (%s; tolerance %s "
          "from the finite-difference truncation). The recorded states CONSERVE energy-momentum along x0; therefore their "
          "violation of p3 + p_t = 2 p0 is exactly p0_y/(3H): the source fails the field equations because p0 (and with "
          "it every component) depends on x0, not because conservation fails"
          % (g6(wc["h"]), len(nz), g6(wc["cons_fd_rel"]), wc["id"], g6(TOL_CONS_FD)))
    wid = max(nz, key=lambda s: s["identity_rel"])
    check("B3_integrated_x0_identity", wid["identity_rel"] <= TOL_IDENTITY,
          "int (p3 + p_t) = 2 Vol_7(a4,0) [e^{6Hy} p0]_{-L}^{0}/(3H) with the solver's integrals and end values p0_brane, "
          "p0_tip (emt-integrals.csv) for the %d nonzero states: largest relative difference %s (%s). So "
          "p3_bar + p_t_bar - 2 p0_bar = ([e^{6Hy} p0]_{-L}^{0} - 6 H W p0_bar)/(3 H W): the averaged algebraic "
          "condition holds only if the boundary flux of p0 equals the value an x0-independent p0 would give"
          % (len(nz), g6(wid["identity_rel"]), wid["id"]))
    mus = {c: [s["mu_" + c] for s in nz if s["mu_" + c] is not None] for c in ("rho", "p3", "p_t", "p0")}
    mu1 = {c: [s["mu1_" + c] for s in nz if s["mu1_" + c] is not None] for c in ("rho", "p3", "p_t", "p0")}
    ptzero = [s["id"] for s in nz if s["mu_p_t"] is None]
    mu_rho_min = min(nz, key=lambda s: s["mu_rho"])
    mu1_rho_min = min(nz, key=lambda s: s["mu1_rho"])
    ok_mu = all(s["mu_rho"] > 1e-3 and s["mu_p0"] > 1e-3 and s["mu1_rho"] > 1e-3 and s["mu1_p0"] > 1e-3 for s in nz)

    def rng(v):
        return "[%s, %s]" % (g6(min(v)), g6(max(v))) if v else "-"
    tips = [s["tip_share_rho"] for s in nz]
    check("B4_hidden_direction_mismatch", ok_mu,
          "the field equations require every diagonal component to be independent of x0 (for every a4 and b4), the "
          "profiles are not. Two measures over the patch with the volume weight e^{6Hy}: (L1) mu1_X = int e^{6Hy} "
          "|X - X_bar| / int e^{6Hy} |X| (0 for an x0-independent X; above 1 where X changes sign along x0): over the %d "
          "nonzero states mu1_rho in %s (smallest %s), mu1_p3 in %s, mu1_p0 in %s, mu1_p_t in %s; (L2) mu_X = "
          "||X - X_bar||/||X|| (X_bar is the orthogonal projection of X on the x0-independent functions): mu_rho in %s "
          "(smallest %s), mu_p3 in %s, mu_p0 in %s, mu_p_t in %s - the L2 norm is weighted towards the tip (the share of "
          "||rho||^2 from the tip half y < -L/2 is %s), so the L1 measure is the less cut-off dependent one; p_t = e_int "
          "is identically zero (hence x0-independent) in the %d states with lambda = 0; the algebraic defect "
          "||p3 + p_t - 2 p0||/||(rho, p3, p_t, p0)|| lies in %s. Every measure is O(1): the computed source is NOT close "
          "to an x0-independent one"
          % (len(nz), rng(mu1["rho"]), mu1_rho_min["id"], rng(mu1["p3"]), rng(mu1["p0"]), rng(mu1["p_t"]),
             rng(mus["rho"]), mu_rho_min["id"], rng(mus["p3"]), rng(mus["p0"]), rng(mus["p_t"]), rng(tips),
             len(ptzero), rng([s["alg_L2_rel"] for s in nz])))
    # B0: the source-condition report, re-derived independently from the same Kohn-Sham files
    try:
        w1 = json.loads(WAVE1.read_text(encoding="utf-8"))
        w1c = {c["name"]: c for c in w1["checks"]}
    except (OSError, ValueError, KeyError) as ex:
        err("cannot read %s: %s" % (rel(WAVE1), ex))
    vmin_s = min(nz, key=lambda s: s["var_ratio"])
    amin_s = min(nz, key=lambda s: s["alg_pointwise_rel"])
    amax_s = max(nz, key=lambda s: s["alg_pointwise_rel"])
    rat = {s["id"]: s["int_ratio"] for s in nz if s["int_ratio"] is not None}
    rbest = min(rat, key=lambda k: abs(rat[k] - 1.0))
    exp = [("ks_profiles_depend_on_x0", ["%d with a nonzero" % len(nz), ">= %s (smallest: %s)"
                                         % (g6(vmin_s["var_ratio"]), vmin_s["id"])]),
           ("ks_profiles_violate_algebraic_condition", ["between %s (%s) and %s (%s)" % (
               g6(amin_s["alg_pointwise_rel"]), amin_s["id"], g6(amax_s["alg_pointwise_rel"]), amax_s["id"])]),
           ("ks_integrals_violate_algebraic_condition", ["closest to 1: %s at %s" % (g6(rat[rbest]), rbest)]),
           ("ks_offdiagonal_condition_on_history", ["Q = 0 on the history"]),
           ("ks_zero_source_states_listed", ["%d states have an identically vanishing" % len(zero)])]
    ok0 = w1["summary"]["fail"] == 0 and all(c["verdict"] == "PASS" for c in w1["checks"])
    missing = [n for n, subs in exp if n not in w1c or not all(x in w1c[n]["detail"] for x in subs)]
    check("B0_source_condition_report_verified", ok0 and not missing and all(rat[k] < 1.0 for k in rat),
          "%s (all %d checks PASS) re-derived independently from the same Kohn-Sham files: %d nonzero states; the "
          "smallest x0 variation (max rho - min rho)/max|T| = %s (%s); the pointwise algebraic defect max|p3 + p_t - "
          "2 p0|/max|T| from %s (%s) to %s (%s); the integrated ratio (int p3 + int p_t)/(2 int p0) closest to 1 is %s "
          "(%s) and below 1 for every state; Q = 0 on the history (check A6) - all equal to the numbers in that report%s. "
          "REFINEMENT: the recorded states do NOT violate the x0 conservation identity d p0/d x0 + 3 H cot z (2 p0 - p3 - "
          "p_t) = 0; they satisfy it (check B2); what fails is p3 + p_t = 2 p0, which is that identity combined with "
          "x0-independence"
          % (rel(WAVE1), len(w1["checks"]), len(nz), g6(vmin_s["var_ratio"]), vmin_s["id"],
             g6(amin_s["alg_pointwise_rel"]), amin_s["id"], g6(amax_s["alg_pointwise_rel"]), amax_s["id"],
             g6(rat[rbest]), rbest, "" if not missing else " EXCEPT " + ", ".join(missing)))
    # ---------------- C
    walg = min(nz, key=lambda s: s["alg_bar_rel"])
    check("C1_averaged_algebraic_condition_fails", all(s["alg_bar_rel"] > 1e-3 for s in nz),
          "on the history with the author's weights the x1 + x5 - 2 x0 moment reads 0 = kappa (p3_bar + p_t_bar - "
          "2 p0_bar) (I = 0 there, check A1); |p3_bar + p_t_bar - 2 p0_bar| / (|p3_bar| + |p_t_bar| + 2 |p0_bar|) lies in "
          "[%s (%s), %s] over the %d nonzero states: an O(1) violation, so no kappa != 0 makes the hidden-direction "
          "averaged Kohn-Sham source satisfy this moment on the history"
          % (g6(walg["alg_bar_rel"]), walg["id"], g6(max(s["alg_bar_rel"] for s in nz)), len(nz)))
    beta = geo["beta"]
    wsolv = max(nz, key=lambda s: abs(s["dE_fd"] - s["dE_emt"]) / max(abs(s["dE_emt"]), 1e-300)
                if s["dE_emt"] != 0 else 0.0)
    solv_rel = (abs(wsolv["dE_fd"] - wsolv["dE_emt"]) / abs(wsolv["dE_emt"])) if wsolv["dE_emt"] != 0 else 0.0
    tags = sorted({s["id"].rsplit("_a", 1)[0] for s in nz})
    worst_sl, worst_tag = 0.0, ""
    for tag in tags:
        ser = series_of(states, tag, slices)
        E = [s["E"] for s in ser]
        G = [-3 * (s["P3"] - s["Pt"]) - 1.5 * beta * s["Pt"] for s in ser]
        hs = slices[1] - slices[0]
        for i0 in (0, 2):
            ch = E[i0 + 2] - E[i0]
            pred = simpson(G[i0:i0 + 3], hs)
            den = max(abs(ch), abs(pred), 1e-300)
            if abs(ch) > 0 or abs(pred) > 0:
                if abs(ch - pred) / den > worst_sl:
                    worst_sl, worst_tag = abs(ch - pred) / den, "%s on [%s, %s]" % (tag, slices[i0], slices[i0 + 2])
    crossings = sum(len(s["fermiLevelCrossings"]) for s in history["series"])
    check("C2_averaged_energy_relation_with_b4", solv_rel <= TOL_ENERGY_SOLVER and worst_sl <= TOL_ENERGY_SLICES
          and crossings == 0,
          "the x4 moment of nabla_mu T^mu_x4 = 0 (T^x4_y = 0) on the record's history: d(b4^{3/2} rho_bar)/da4 = "
          "b4^{3/2} (-3 (p3_bar - p_t_bar) - (3/2) beta p_t_bar), i.e. dE/da4 = -3 (P3 - P_t) - (3/2) beta P_t, beta = %s: "
          "(i) the solver's finite-difference dE/da4 agrees with this formula to %s (largest relative difference, %s; "
          "adiabaticity.csv); (ii) between slices, Simpson's rule on the 5 slices (h = 0.5) reproduces the change of E "
          "to %s (worst: %s; tolerance %s for the step 0.5); (iii) history.json records %d Fermi-level crossings, so the "
          "instantaneous ground states form one adiabatic family along a4 in [0, 2]"
          % (g6(beta), g6(solv_rel), wsolv["id"], g6(worst_sl), worst_tag, g6(TOL_ENERGY_SLICES), crossings))
    # C3: on the record's history the x4 moment of the author's equations needs the constant kappa rho = -2/27 (H = 1)
    th_a = theories["author"]
    lam_auth = float(GRAVITY[1][4])
    krho_req = -lam_auth - th_a["S4"](1.0, 4.0 / 3.0)
    var = []
    for tag in tags:
        ser = series_of(states, tag, slices)
        rb = [s["rho_bar"] for s in ser]
        var.append((max(rb) / min(rb) if min(rb) > 0 else (min(rb) / max(rb) if max(rb) < 0 else float("inf")), tag))
    check("C3_record_history_not_a_solution_of_the_x4_moment",
          abs(krho_req + 2.0 / 27.0) < 1e-14 and all(v > 1.0 + 1e-6 for v, _ in var),
          "with the author's weights and Lambda = -10 the x4 moment on the record's history (a4' = H, u = 4/3 H) needs "
          "kappa rho_bar = -Lambda - S4(H, 4/3 H) = %s (= -2/27, H = 1) at EVERY slice; along the history the Kohn-Sham "
          "rho_bar (per proper cell volume) of every series with a nonzero source changes, by the factor max/min = %s ... "
          "%s over the %d series, so no constant kappa satisfies the x4 moment at more than one slice: the record's "
          "history is a prescribed background, not a solution even of the x4 moment with the Kohn-Sham source"
          % (g6(krho_req), g6(min(v for v, _ in var)), g6(max(v for v, _ in var)), len(var)))
    mom = [s for s in nz if s["N"] > 8]
    n8 = [s for s in nz if s["N"] == 8]
    check("C4_source_signs", all(s["p3_bar"] - s["p_t_bar"] > 0 and s["rho_bar"] > 0 and s["rho_bar"] + s["p0_bar"] > 0
                                 for s in mom)
          and all(abs(s["p3_bar"] - s["p_t_bar"]) <= 1e-12 * max(abs(s["p3_bar"]), 1e-300) + 1e-18 for s in n8),
          "for the %d nonzero states with N = 136, 688: rho_bar > 0, rho_bar + p0_bar > 0 and p3_bar - p_t_bar > 0 "
          "(range %s ... %s); for the %d N = 8 interacting states (k = 0 brane zero modes) p3_bar = p_t_bar (no "
          "3-momentum), and their source still changes along the history because the effective coupling falls like "
          "e^{-2 a4}; the required source of the history has rho < 0 for kappa > 0 (check C3)"
          % (len(mom), g6(min(s["p3_bar"] - s["p_t_bar"] for s in mom)),
             g6(max(s["p3_bar"] - s["p_t_bar"] for s in mom)), len(n8)))

    # ---------------- D
    dense = {}
    for r in read_csv(DENSE):
        dense.setdefault(r["id"].rsplit("_a", 1)[0], []).append(r)
    srcs, dev_dense = {}, 0.0
    for tag in SERIES:
        ser = series_of(states, tag, slices)
        if any(s["Pt"] != 0.0 or s["lambda"] != 0.0 for s in ser):
            err("series %s is not a free gas (lambda = 0, P_t = 0)" % tag)
        rows = sorted(dense.get(tag, []), key=lambda r: float(r["a4"]))
        xs = [float(r["a4"]) for r in rows]
        if len(rows) != 41 or any(abs(x - 0.05 * i) > 1e-12 for i, x in enumerate(xs)):
            err("%s: the dense history of %s needs the 41 slices a4 = 0, 0.05, ..., 2" % (rel(DENSE), tag))
        Ed = [float(r["int_rho"]) for r in rows]
        P3d = [float(r["int_p3"]) for r in rows]
        if any(float(r["int_p_t"]) != 0.0 for r in rows):
            err("%s: %s is not a free gas" % (rel(DENSE), tag))
        for s_ in ser:                       # the dense history at the record's five slices equals the record
            r = rows[int(round(s_["a4"] / 0.05))]
            for k_, kk in (("E", "int_rho"), ("P3", "int_p3"), ("P0", "int_p0")):
                dev_dense = max(dev_dense, abs(float(r[kk]) - s_[k_]) / max(abs(s_[k_]), 1e-300))
        dEd = [-3.0 * x for x in P3d]        # free gas at fixed b4: dE/da4 = -3 P3
        lspl = natural_spline(xs, [math.log(x) for x in Ed])
        srcs[tag] = {"E": [s_["E"] for s_ in ser], "P3": [s_["P3"] for s_ in ser], "P0": [s_["P0"] for s_ in ser],
                     "Q_max": [s_["Q_max"] for s_ in ser],
                     "E_h": (lambda a, x=xs, E=Ed, dE=dEd: hermite(x, E, dE, a)[0]),
                     "E_s": (lambda a, l=lspl: math.exp(l(a)))}
    check("D0_dense_free_gas_source", dev_dense <= 1e-13,
          "the source of the integration is the dense free-gas history of the record (%s: N136_lam0 and N688_lam0 at the "
          "41 slices a4 = 0, 0.05, ..., 2, written by the same Rust solver on the same history); at the five slices of "
          "the Kohn-Sham record its E, P3, P0 equal results/ground/emt-integrals.csv to %s relative; for lambda = 0 E(a4) "
          "does not depend on b4, so the averaged source on any (a4, b4) path is rho_bar = E(a4)/(cell volume b4^{3/2})"
          % (rel(DENSE), g6(dev_dense)))
    cases = []
    for g in GRAVITY:
        name = g[0]
        th = theories[name]
        if name in ("einstein", "lovelock3"):
            continue                                   # no history with a4'(0) = H (checks A2, A6)
        for tag in SERIES:
            for ib, u0 in enumerate(th["roots"]):
                if g[4] is not None:
                    Lam_ = float(g[4])
                    sig_list = [(-Lam_ - th["S4"](float(A0), u0), "Lambda = %s" % g[4])]
                else:
                    sig_list = [(float(s_), "sigma0 = %s" % s_) for s_ in SIGMAS] + [(-th["S4"](float(A0), u0), "Lambda = 0")]
                for sig, label in sig_list:
                    Lam_ = float(g[4]) if g[4] is not None else -th["S4"](float(A0), u0) - sig
                    r1 = integrate_case(th, srcs[tag], slices, u0, Lam_, sig, "M1")
                    r2 = integrate_case(th, srcs[tag], slices, u0, Lam_, sig, "M2")
                    resid = residuals_at_slices(th, srcs[tag], r1, Lam_, sig, slices)
                    q = [srcs[tag]["Q_max"][i] * r1["rates"][a][0] for i, a in enumerate(slices) if a in r1["rates"]]
                    cases.append({"gravity": name, "series": tag, "branch": ib, "u0": u0, "label": label, "sigma0": sig,
                                  "Lambda": Lam_, "m1": r1, "m2": r2, "resid": resid, "q_max": max(q) if q else None})
    # D1: methods agree
    worst_m, worst_case, n_cmp = 0.0, "", 0
    same_events = all(c["m1"]["event"] == c["m2"]["event"] for c in cases)
    for c in cases:
        m1, m2 = c["m1"], c["m2"]
        if m1["event"] != m2["event"]:
            continue
        n_cmp += 1
        d1 = abs(m1["a_end"] - m2["a_end"]) / max(m1["a_end"], 1e-300) if m1["a_end"] > 0 else abs(m2["a_end"])
        d2 = abs(m1["rate_end"] - m2["rate_end"]) / max(abs(m1["rate_end"]), 0.05)
        d3 = abs(m1["u_end"] - m2["u_end"]) / max(abs(m1["u_end"]), 0.05)
        d4 = abs(m1["lb_end"] - m2["lb_end"]) / max(abs(m1["lb_end"]), 0.05)
        if m1["event"] == "regular":
            d = max(d1, d2, d3, d4)
        else:                       # an event is resolved only to the larger step (M2: 2e-3); its position is compared
            d = max(abs(m1["a_end"] - m2["a_end"]) - 2e-3, 0.0) / max(m1["a_end"], 1e-300)
        if d > worst_m:
            worst_m, worst_case = d, "%s %s branch %d %s" % (c["gravity"], c["series"], c["branch"], c["label"])
    check("D1_two_integration_methods_agree", same_events and worst_m <= TOL_METHODS and n_cmp == len(cases),
          "M1 (the free-gas energy E(a4) by the cubic Hermite interpolant through the 41 dense slices with the exact slopes "
          "dE/da4 = -3 P3, RK4 in a4 with step 1e-3) against M2 (a natural cubic spline of ln E through the same 41 "
          "slices, step 2e-3); at every step "
          "(a4', u) solve Q(a4', u) = 0 and S4(a4', u) + Lambda = -kappa rho_bar(a4, b4) by Newton (tolerance %s): the "
          "%d cases have the same outcome in both methods (%s), and for the regular cases the rates a4'/H, u/H and "
          "ln(b4/b4(0)) at a4 = 2, for the others the position of the event (resolved to the larger step 2e-3), agree "
          "to %s (worst: %s; tolerance %s for two different interpolations between slices 0.05 "
          "apart)"
          % (g6(NEWTON_TOL), len(cases), same_events, g6(worst_m), worst_case, g6(TOL_METHODS)))
    auth = [c for c in cases if c["gravity"] == "author"]
    ok2 = all(abs(c["u0"] - 4.0 / 3.0) < 1e-14 and abs(c["sigma0"] + 2.0 / 27.0) < 1e-14 and abs(c["Lambda"] + 10) < 1e-14
              for c in auth) and len(auth) == len(SERIES)
    check("D2_author_weights_start_on_the_record_history", ok2,
          "with the author's weights and Lambda = -10 the integration starts on the record's history: a4'(0) = H, "
          "u(0) = 4/3 H (the nonzero root of Q(H, u)) and kappa rho_bar(0) = -2/27 H^2 forced by the x4 constraint (so "
          "kappa < 0 for the free gas, rho_bar > 0); then the gas dilutes and the solution leaves that history: %s"
          % "; ".join("%s: outcome %s at a4 = %s, there a4'/H = %s, u/H = %s, b4/b4(0) = %s (record history: a4'/H = 1, "
                      "u/H = 4/3, b4/b4(0) = %s)" % (c["series"], c["m1"]["event"], g6(c["m1"]["a_end"]),
                                                     g6(c["m1"]["rate_end"]), g6(c["m1"]["u_end"]),
                                                     g6(math.exp(c["m1"]["lb_end"])),
                                                     g6(math.exp(4.0 / 3.0 * c["m1"]["a_end"]))) for c in auth))
    bian = [r["bianchi"] for c in cases for r in c["resid"]]
    check("D3_propagation_identity_along_the_solutions", bool(bian) and max(bian) <= TOL_BIANCHI,
          "at the slices reached, with a4'' and v from the implicit derivatives of the two algebraic equations and the "
          "free-gas conservation d(kappa rho_bar)/dx4 = kappa (dE/da4 a4' - (3/2) E u)/(cell volume b4^{3/2}): "
          "3 a4' (R1 - R5) + (3/2) u R5 = 0 (check A4 with R4 = 0, Q = 0) to %s relative over %d slice evaluations: the "
          "implementation reproduces the exact propagation identity" % (g6(max(bian)) if bian else "-", len(bian)))
    r1s = [abs(r["R1"]) for c in cases for r in c["resid"] if r["a4"] > 0]
    r0s = [abs(r["R0"]) for c in cases for r in c["resid"] if r["a4"] > 0]
    check("D4_dropped_moments_residuals", bool(r1s) and min(max(a, b) for a, b in zip(r1s, r0s)) > 1e-3,
          "the dropped second-order moments (x1: R1 = S1 + Lambda - kappa p3_bar, x0: R0 = S0 + Lambda - kappa p0_bar), "
          "relative to the largest term, at the slices a4 > 0 reached: |R1| in %s, |R0| in %s: never small together - the "
          "truncation is not a small perturbation of an exact solution" % (rng(r1s), rng(r0s)))
    from collections import Counter
    outc = Counter((c["gravity"], c["m1"]["event"]) for c in cases)
    egb = [c for c in cases if c["gravity"] == "egb"]
    check("D5_outcomes", len(cases) == len(SERIES) * (1 + 2 * (len(SIGMAS) + 1)),
          "%d integrated cases (the author's weights: %d; Einstein-Gauss-Bonnet: %d = 2 series x 2 branches x %d "
          "parameter choices); outcomes (gravity, outcome: count): %s. Einstein gravity and the stated cubic Lovelock "
          "case have no history with a4'(0) = H and a source without T^x4_x0 (checks A2, A6) and are not integrated"
          % (len(cases), len(auth), len(egb), len(SIGMAS) + 1,
             ", ".join("%s %s: %d" % (k[0], k[1], v) for k, v in sorted(outc.items()))))
    qs = [c["q_max"] for c in cases if c["q_max"] is not None]
    lost = [c for c in cases if c["m1"]["event"] == "adiabaticity_lost"]
    check("D6_adiabaticity_along_the_solutions", bool(qs) and max(qs) <= 1.0 + 1e-12,
          "the adiabaticity measure of the free gas, Q_max(a4') = Q_max(a4' = H) a4'/H (only the frozen part of d_a h for "
          "lambda = 0; Q_max(H) linear between the slices), is evaluated after every step; the integration stops where "
          "it reaches 1, because there the instantaneous Kohn-Sham states are no longer a valid source (outcome "
          "adiabaticity_lost): %d cases (%s); along every integrated part it stays <= %s at the slices"
          % (len(lost), "; ".join("%s %s u0/H = %s %s at a4 = %s, a4'/H = %s" % (c["gravity"], c["series"], g6(c["u0"]),
                                                                                c["label"], g6(c["m1"]["a_end"]),
                                                                                g6(c["m1"]["rate_end"]))
                                  for c in lost[:6]) + (" ..." if len(lost) > 6 else ""), g6(max(qs))))

    # ---------------- outputs
    OUT_MOMENTS.parent.mkdir(parents=True, exist_ok=True)
    OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO(newline="")
    wr = csv.writer(buf, lineterminator="\n")
    wr.writerow(["id", "N", "lambda_tag", "a4", "rho_bar", "p3_bar", "p_t_bar", "p0_bar", "mu1_rho", "mu1_p3", "mu1_p_t",
                 "mu1_p0", "mu_rho", "mu_p3", "mu_p_t", "mu_p0", "tip_share_rho", "alg_bar_rel", "alg_L2_rel",
                 "alg_pointwise_rel", "cons_fd_rel", "identity_rel", "Q_max"])
    for sid in sorted(states):
        s = states[sid]
        if s["zero"]:
            wr.writerow([sid, s["N"], s["lambda_tag"], e12(s["a4"]), "0", "0", "0", "0"] + ["zero source"] * 14 + [""])
            continue
        wr.writerow([sid, s["N"], s["lambda_tag"], e12(s["a4"]), e12(s["rho_bar"]), e12(s["p3_bar"]),
                     e12(s["p_t_bar"]), e12(s["p0_bar"]), e12(s["mu1_rho"]), e12(s["mu1_p3"]),
                     "identically zero" if s["mu1_p_t"] is None else e12(s["mu1_p_t"]), e12(s["mu1_p0"]),
                     e12(s["mu_rho"]), e12(s["mu_p3"]),
                     "identically zero" if s["mu_p_t"] is None else e12(s["mu_p_t"]), e12(s["mu_p0"]),
                     e12(s["tip_share_rho"]),
                     e12(s["alg_bar_rel"]), e12(s["alg_L2_rel"]), e12(s["alg_pointwise_rel"]), e12(s["cons_fd_rel"]),
                     e12(s["identity_rel"]), e12(s["Q_max"])])
    OUT_MOMENTS.write_bytes(buf.getvalue().encode("utf-8"))
    buf = io.StringIO(newline="")
    wr = csv.writer(buf, lineterminator="\n")
    wr.writerow(["gravity", "series", "branch", "u0_over_H", "case", "sigma0", "Lambda", "event", "a4_end", "x4_end",
                 "rate_end", "u_end", "b4_ratio_end"]
                + ["rate_a%02d" % int(round(10 * a)) for a in slices] + ["u_a%02d" % int(round(10 * a)) for a in slices]
                + ["m2_event", "m2_a4_end", "m2_rate_end", "m2_u_end", "m2_b4_ratio_end",
                   "x1_moment_residual_max_rel", "x0_moment_residual_max_rel", "propagation_identity_max_rel",
                   "adiabaticity_Q_max"])
    for c in cases:
        m1, m2 = c["m1"], c["m2"]
        r1max = max((abs(r["R1"]) for r in c["resid"] if r["a4"] > 0), default=None)
        r0max = max((abs(r["R0"]) for r in c["resid"] if r["a4"] > 0), default=None)
        bmax = max((r["bianchi"] for r in c["resid"]), default=None)
        wr.writerow([c["gravity"], c["series"], c["branch"], e12(c["u0"]), c["label"], e12(c["sigma0"]), e12(c["Lambda"]),
                     m1["event"], e12(m1["a_end"]), e12(m1["x4_end"]), e12(m1["rate_end"]), e12(m1["u_end"]),
                     e12(math.exp(m1["lb_end"]))]
                    + [e12(m1["rates"][a][0]) if a in m1["rates"] else "" for a in slices]
                    + [e12(m1["rates"][a][1]) if a in m1["rates"] else "" for a in slices]
                    + [m2["event"], e12(m2["a_end"]), e12(m2["rate_end"]), e12(m2["u_end"]), e12(math.exp(m2["lb_end"])),
                       e12(r1max) if r1max is not None else "", e12(r0max) if r0max is not None else "",
                       e12(bmax) if bmax is not None else "", e12(c["q_max"]) if c["q_max"] is not None else ""])
    OUT_CASES.write_bytes(buf.getvalue().encode("utf-8"))

    n_pass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
    a136 = [c for c in auth if c["series"] == "N136_lam0"][0]
    e136 = {(c["branch"], c["label"]): c for c in egb if c["series"] == "N136_lam0"}
    conclusions = [
        "EXACT: no recorded Kohn-Sham state is an admissible source of the author's metric with b4(x4). The states conserve "
        "energy-momentum along x0 (B2), so p3 + p_t - 2 p0 = p0_y/(3H) exactly (A5): the diagonal components depend on x0, "
        "which the field equations exclude for every a4 and b4 (B4: at least a share %s of the energy density deviates "
        "from its hidden-direction average, L1 measure); on the history the x1 + x5 - 2 x0 moment fails also after "
        "averaging (C1), and the x4 moment of the author's equations would need the constant source kappa rho = -2/27, "
        "which the gas, whose rho_bar changes along the history, cannot supply (C3). Nothing about a4 or b4 is DERIVED "
        "from the coupled problem." % g6(min(mu1["rho"])),
        "EXACT (new with b4): the off-diagonal equation kappa q40 = cot z (b4'/b4) Q(a4', b4'/b4) (A2). Every Kohn-Sham "
        "state has q40 = 0, so a history with b4 not constant needs Q = 0 at every instant. In Einstein gravity Q = 3H/2: "
        "there is NO history with b4 not constant and a Kohn-Sham source (b4' = 0 is forced, which the author's metric "
        "excludes). With the author's weights Q = 0 ties b4'/b4 to a4' (at a4' = H: b4'/b4 = 4/3 H, the record's "
        "history; A6); the stated cubic Lovelock case has no real branch at a4' = H; the stated Gauss-Bonnet case has two "
        "(b4 decreasing).",
        "APPROXIMATION (stated): keep the x4 moment and the off-diagonal equation (exact necessary conditions; for a "
        "given source two algebraic equations for (a4', b4'/b4)), drop the remaining second-order moments. One combination "
        "of the dropped equations then holds by the propagation identity (A4, D3); the other two are not small (D4). "
        "Integrated for the free gas (N136_lam0, N688_lam0), whose averaged source is known for any b4, from a4'(0) = H "
        "over a4 in [0, 2].",
        "Within that approximation, with the author's weights and Lambda = -10 the start is the record's history with "
        "kappa rho_bar(0) = -2/27 H^2 (kappa < 0 for the gas); as the gas dilutes the rates leave that history: for "
        "N136_lam0 the outcome is %s at a4 = %s with a4'/H = %s, (b4'/b4)/H = %s there (record: 1 and 4/3). The source "
        "does not select the deflation: the initial rate and the branch of Q = 0 are initial data and Lambda (or the "
        "source strength) is fixed by the constraint. Gauss-Bonnet (alpha2 H^2 = 1/80), N136_lam0: %s."
        % (a136["m1"]["event"], g6(a136["m1"]["a_end"]), g6(a136["m1"]["rate_end"]), g6(a136["m1"]["u_end"]),
           "; ".join("branch u0/H = %s, %s: %s at a4 = %s" % (g6(c["u0"]), lbl, c["m1"]["event"], g6(c["m1"]["a_end"]))
                     for (b, lbl), c in sorted(e136.items(), key=lambda kv: (kv[0][0], kv[1]["sigma0"]))
                     if lbl in ("sigma0 = -1", "sigma0 = 1", "Lambda = 0"))),
        "Not computed (open): the interacting series (their averaged source along a history other than the record's "
        "would need new Kohn-Sham solves at the effective coupling of that b4), the source beyond a4 = 2, thermal states, "
        "the non-adiabatic problem, and a source with the hidden-direction profile the equations require.",
    ]
    rep = {
        "report": rel(OUT_REPORT),
        "producer": rel(Path(__file__)),
        "spec": "Revision/SPEC.md sections 1, 5 and 7: the field equations for a4 and b4 with the Kohn-Sham energy-momentum "
                "tensor as the source; coordinates x1..x3 = 3-space, x4 = time, x5..x7 = the exponentially deflating extra "
                "times, x0 = hidden direction; the author's metric with b4(x4) (b4 a function of x4, never 1)",
        "inputs": {rel(p): sha256(p) for p in (A4_JSON, KS_PARAMS, KS_INTEGRALS, KS_ADIABATIC, KS_HISTORY, KS_THEORY,
                                               WAVE1, DENSE)},
        "inputProfiles": {"directory": rel(KS_PROFILES), "files": len(states),
                          "sha256OfSortedDigests": hashlib.sha256("".join(
                              sha256(p) for p in sorted(KS_PROFILES.glob("*.csv"))).encode()).hexdigest()},
        "units": "the solver's units H = m = 1; densities per proper cell volume in units of b4(0)^{-3/2}; kappa in units "
                 "m^-6 times b4(0)^{3/2}; Lambda in units H^2; sigma0 = kappa rho_bar(a4 = 0)/H^2 is the dimensionless "
                 "source strength (b4(0) cancels in it)",
        "assumptions": [
            "source = the T = 0 instantaneous Kohn-Sham ground states of Revision/kohn_sham (adiabatic family, no "
            "Fermi-level crossings) at the computed slices a4 = 0, 0.5, 1, 1.5, 2 of the history a4 = H x4, "
            "b4 = b4(0) e^{(4/3) H x4}",
            "integration only for the free gas (lambda = 0): its energy E(a4) does not depend on b4, so its averaged source "
            "on any (a4, b4) path is rho_bar = E(a4)/(cell volume b4^{3/2}); E from the dense history of the record (41 "
            "slices, Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv), between them by the cubic Hermite "
            "interpolant with the exact slopes -3 P3 (M1) or a spline of ln E (M2)",
            "hidden-direction averages with the volume weight sqrt|g| ~ e^{6Hy} over the patch y in [-L, 0], L = 3 (the "
            "solver's tip cut-off)",
            "truncation: the x4 moment and the off-diagonal equation are imposed, the x1, x5 and x0 moments are not (one "
            "combination holds by the propagation identity; the residuals are reported)",
            "sign convention sigmaT = +1 (a4-equations.json); kappa of either sign is examined for Gauss-Bonnet",
            "initial rate a4'(0) = H (the rate of the prescribed Kohn-Sham history), a4(0) = 0, b4(0) as the unit; "
            "b4'(0)/b4(0) a real root of Q(H, u) = 0; Lambda fixed by the constraint at a4 = 0 (or the author's "
            "Lambda = -10 with sigma0 fixed instead)",
        ],
        "gravity": [{"name": g[0], "couplings": g[5], "Q(a4', u) at H = 1": theories[g[0]]["Qstr"],
                     "real roots of Q(H, u) = 0, u/H": theories[g[0]]["exact_roots"]} for g in GRAVITY],
        "conclusions": conclusions,
        "tolerances": {"integrals": TOL_INTEGRAL, "x0ConservationFD": TOL_CONS_FD, "integratedIdentity": TOL_IDENTITY,
                       "energyRelationSolver": TOL_ENERGY_SOLVER, "energyRelationSlices": TOL_ENERGY_SLICES,
                       "methods": TOL_METHODS, "propagationIdentity": TOL_BIANCHI, "newton": NEWTON_TOL},
        "outputs": [rel(OUT_MOMENTS), rel(OUT_CASES), rel(OUT_SUMMARY)],
        "zeroSourceStates": zero,
        "summary": {"checks": len(CHECKS), "pass": n_pass, "fail": len(CHECKS) - n_pass},
        "checks": CHECKS,
    }
    OUT_REPORT.write_bytes((json.dumps(rep, indent=1, ensure_ascii=False) + "\n").encode("utf-8"))
    OUT_SUMMARY.write_bytes(summary_md(rep, cases, states, slices).encode("utf-8"))
    print("pass %d/%d; wrote %s" % (n_pass, len(CHECKS), rel(OUT_REPORT)))
    return 0 if n_pass == len(CHECKS) else 1


def summary_md(rep: dict, cases: list, states: dict, slices: list) -> str:
    L = ["# The field equations for a4 and b4 with the Kohn-Sham source (generated)", "",
         "Generated by `%s`; every number below is from this run (report `%s`, %d/%d checks pass)."
         % (rep["producer"], rep["report"], rep["summary"]["pass"], rep["summary"]["checks"]), "",
         "Coordinates: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra times (scale factor "
         "e^{-a4} b4^{1/2} sin^{1/6} z; the author's metric with b4(x4), b4 a function of x4, never 1); x0 = hidden "
         "direction (Kohn-Sham coordinate y = ln(sin z)/(6H)).", "",
         "## Conclusions", ""]
    for c in rep["conclusions"]:
        L.append("* " + c)
    L += ["", "## Assumptions", ""] + ["* " + a for a in rep["assumptions"]]
    L += ["", "## Hidden-direction averages along the history (N = 136, lambda = 0)", "",
          "Proper densities per cell volume in units of b4(0)^{-3/2} (H = m = 1); mu1 = L1 and mu = L2 hidden-direction "
          "mismatch (check B4); defect = |p3_bar + p_t_bar - 2 p0_bar| / (|p3_bar| + |p_t_bar| + 2 |p0_bar|) (check C1).", "",
          "| a4 | rho_bar | p3_bar | p_t_bar | p0_bar | mu1_rho | mu1_p0 | mu_rho | mu_p0 | defect |", "| --- " * 10 + "|"]
    for a in slices:
        s = states["N136_lam0_a%02d" % int(round(10 * a))]
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            g6(a), g6(s["rho_bar"]), g6(s["p3_bar"]), g6(s["p_t_bar"]), g6(s["p0_bar"]), g6(s["mu1_rho"]),
            g6(s["mu1_p0"]), g6(s["mu_rho"]), g6(s["mu_p0"]), g6(s["alg_bar_rel"])))
    L += ["", "## Integrated cases (series N136_lam0, a4'(0) = H)", "",
          "u0 = b4'(0)/b4(0), a real root of Q(H, u) = 0; sigma0 = kappa rho_bar(0)/H^2; Lambda from the constraint at "
          "a4 = 0 (the author's weights: Lambda = -10 and sigma0 from the constraint); outcome: regular (through a4 = 2), "
          "turning_point (a4' = 0), branch_point (the Jacobian of the two algebraic equations vanishes), no_real_solution, "
          "u_zero (b4'/b4 reaches 0). Every integrated series (" + ", ".join(SERIES) + ") and case: "
          "`results/ks-source-a4-cases.csv`.", "",
          "| gravity | u0/H | case | Lambda/H^2 | outcome | a4 reached | a4'/H there | (b4'/b4)/H there | b4/b4(0) there |",
          "| --- " * 9 + "|"]
    for c in cases:
        if c["series"] != "N136_lam0":
            continue
        m1 = c["m1"]
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            c["gravity"], g6(c["u0"]), c["label"], g6(c["Lambda"]), m1["event"], g6(m1["a_end"]), g6(m1["rate_end"]),
            g6(m1["u_end"]), g6(math.exp(m1["lb_end"]))))
    L += ["", "## Gravity theories", ""]
    for g in rep["gravity"]:
        L.append("* **%s** (%s): Q(a4', u) = %s; real roots of Q(H, u) = 0: %s" % (
            g["name"], g["couplings"], g["Q(a4', u) at H = 1"], ", ".join(g["real roots of Q(H, u) = 0, u/H"]) or "none"))
    L += ["", "## Checks", ""]
    for c in rep["checks"]:
        L.append("* **%s** %s: %s" % (c["verdict"], c["name"], c["detail"]))
    L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
