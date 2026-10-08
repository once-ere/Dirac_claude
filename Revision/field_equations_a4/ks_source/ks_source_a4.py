#!/usr/bin/env python3
"""Revision/field_equations_a4/ks_source/ks_source_a4.py - the a4 field equations (SPEC section 5) specialised to
the Kohn-Sham states of dirac16complex (SPEC section 7, Revision/kohn_sham) as the source.

Coordinates as the author names them: x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time; x5, x6, x7 =
the three EXTRA TIMES, which DEFLATE EXPONENTIALLY when a4 increases (scale factor e^{-a4} sin^{1/6} z); x8 = the hidden
direction, z = 6 H x8, and the Kohn-Sham hidden coordinate y = ln(sin z)/(6 H) in [-L, 0] (sqrt|g| dx8 = e^{6Hy} dy).

What this script does (Revision code only; inputs are Revision files, read-only):
  A (exact, sympy, from Revision/field_equations_a4/a4-equations.json)
    the identities used below: E^x1_x1 + E^x5_x5 = 2 E^x8_x8 for every Lovelock order; E^x1_x1 - E^x5_x5 = a4'' F(a4');
    E^x4_x4 depends on a4'^2 only, P(X) := sum_k alpha_k E_(k)^x4_x4 at a4'^2 = X, and 3 F = 2 dP/dX (so the evolution
    equation is the x4-derivative of the constraint once the averaged energy relation holds); the x8 conservation
    identity in the y coordinate, p8_y + 6 H p8 = 3 H (p3 + p_t), hence p3 + p_t - 2 p8 = p8_y/(3H); its integral over
    the patch; the residual of the x8 equation after the constraint is used.
  B (numerical, the recorded Kohn-Sham ground-state profiles)
    the x8 conservation identity on every profile (4th-order finite differences on the output grid); the integrated
    identity against the solver's integrals; the hidden-direction mismatch of every component, measured in the
    L2 norm with the volume weight e^{6Hy} (the x8-independent part of a profile is its weighted average, the
    mismatch mu = ||X - Xbar|| / ||X|| is the fraction that no x8-independent source can carry).
  C (the hidden-direction moments of the field equations)
    multiplying the field equations by sqrt|g| and integrating over the patch gives EXACT necessary conditions with
    the weighted averages rho_bar, p3_bar, p_t_bar, p8_bar as the source; which of them are mutually consistent for
    the Kohn-Sham states along the history (the x4 moment and the x1 - x5 moment are, through the averaged energy
    relation d rho_bar/d a4 = -3 (p3_bar - p_t_bar); every set that contains the x8 moment is not).
  D (integration, an APPROXIMATION stated as such)
    the truncated system "x4 moment + x1 - x5 moment" (the x8 moment and the x1 + x5 - 2 x8 combination dropped, their
    residuals reported) has the first integral P(a4'^2) + Lambda = -kappa rho_bar(a4); it is integrated over the
    computed range a4 in [0, 2] for Einstein gravity and two stated Einstein-Lovelock couplings, with two methods
    (M1: the first integral and a quadrature for x4; M2: RK4 of the evolution equation with an independently
    interpolated source), and every case is classified (regular / turning point / branch point F = 0).

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
WAVE1 = A4DIR / "reports" / "ks-source-conditions.json"   # the wave-1 fixer's report, verified here (check B0)
OUT_MOMENTS = HERE / "results" / "ks-source-moments.csv"
OUT_CASES = HERE / "results" / "ks-source-a4-cases.csv"
OUT_REPORT = HERE / "reports" / "ks-source-a4.json"
OUT_SUMMARY = HERE / "reports" / "ks-source-a4-summary.md"

CHECKS: list[dict] = []

# tolerances (stated, with their reasons)
TOL_INTEGRAL = 1e-6      # Simpson on the 151-point output grid against the solver's own integrals (found ~1e-8)
TOL_CONS_FD = 1e-3       # 4th-order finite differences on the output grid dy = 0.02 (truncation ~ dy^4)
TOL_IDENTITY = 1e-6      # integrated x8 identity, from the solver's integrals and end values
TOL_ENERGY_SOLVER = 1e-6  # solver: dE/da4 by finite differences (step 2e-3) against the EMT formula
TOL_ENERGY_SLICES = 2e-2  # between slices (step 0.5): Simpson of -3 (p3_bar - p_t_bar) against the change of rho_bar
TOL_METHODS = 5e-3       # M1 (first integral) against M2 (RK4 of the evolution equation, independent interpolant)
TOL_ZERO = 1e-12

# the stated gravity theories (H = 1 units of the solver; alpha_k carry H^(2-2k))
GRAVITY = [
    ("einstein", Fraction(1), Fraction(0), Fraction(0),
     "Einstein gravity: alpha1 = 1, alpha2 = alpha3 = 0"),
    ("egb", Fraction(1), Fraction(1, 80), Fraction(0),
     "Einstein-Gauss-Bonnet: alpha1 = 1, alpha2 H^2 = 1/80 (inside 0 < alpha2 H^2 <= 1/40, where the vacuum admits the "
     "linear member, a4-equations.json linearMember.einsteinGaussBonnetVacuum), alpha3 = 0"),
    ("lovelock3", Fraction(1), Fraction(1, 80), Fraction(1, 4000),
     "Einstein-Lovelock (cubic): alpha1 = 1, alpha2 H^2 = 1/80, alpha3 H^4 = 1/4000"),
]
SERIES = ["N136_lam0", "N688_lam0", "N688_lamp2", "N688_lamm2", "N8_lamp2"]
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
ad1, ad2, H, X, Lam, kap = sp.symbols("ad1 ad2 H X Lam kappa")
al1, al2, al3 = sp.symbols("alpha1 alpha2 alpha3")
p3, pt, p8, rho, p8y, cc = sp.symbols("p3 pt p8 rho p8y cc")
LOC = {"ad1": ad1, "ad2": ad2, "H": H, "alpha1": al1, "alpha2": al2, "alpha3": al3, "Lam": Lam, "kappa": kap,
       "p3": p3, "pt": pt, "p8": p8, "rho": rho, "cc": cc}


def parse(s: str) -> sp.Expr:
    """an expression (or an equation lhs == rhs, returned as lhs - rhs) of a4-equations.json"""
    if s.count("==") == 1:
        lhs, rhs = s.split("==")
        return parse(lhs) - parse(rhs)
    s2 = s.replace("^", "**")
    if not re.fullmatch(r"[0-9A-Za-z_+\-*/(). ]+", s2):
        err("unexpected characters in an expression of a4-equations.json: %r" % s)
    return sp.sympify(s2, locals=LOC)


def part_a(a4: dict) -> dict:
    lt = a4["lovelockTensors"]
    E = {}
    for k in ("E1", "E2", "E3"):
        E[k] = {c: parse(lt[k][c]["input"]) for c in ("x1x1", "x4x4", "x5x5", "x8x8", "x4x8", "x8x4")}
    # A1: algebraic identity and off-diagonal zeros
    ok = all(sp.expand(E[k]["x1x1"] + E[k]["x5x5"] - 2 * E[k]["x8x8"]) == 0 for k in E)
    ok_off = all(E[k]["x4x8"] == 0 and E[k]["x8x4"] == 0 for k in E)
    check("A1_lovelock_identity_x1_plus_x5_equals_2x8", ok and ok_off,
          "for k = 1, 2, 3 (a4-equations.json lovelockTensors): E_(k)^x1_x1 + E_(k)^x5_x5 - 2 E_(k)^x8_x8 = 0 exactly and "
          "E_(k)^x4_x8 = E_(k)^x8_x4 = 0; hence the x1 + x5 - 2 x8 combination of the field equations reads "
          "0 = kappa (p3 + p_t - 2 p8) for EVERY a4(x4), Lambda and alpha_k")
    al = {"E1": al1, "E2": al2, "E3": al3}
    lhs = {c: sp.expand(sum(al[k] * E[k][c] for k in E)) for c in ("x1x1", "x4x4", "x5x5", "x8x8")}
    F_rec = parse(a4["generalSource"]["evolution_F"]["input"])
    diff15 = sp.expand(lhs["x1x1"] - lhs["x5x5"] - ad2 * F_rec)
    check("A2_evolution_is_x1_minus_x5", diff15 == 0 and not F_rec.has(ad2),
          "sum_k alpha_k (E_(k)^x1_x1 - E_(k)^x5_x5) = a4'' F(a4') exactly, F = generalSource.evolution_F = %s"
          % sp.sstr(F_rec))
    # P(X): x4x4 depends on ad1^2 only and not on ad2
    e4 = lhs["x4x4"]
    PX = sp.expand(e4.subs(ad1, sp.sqrt(X)))
    even = sp.expand(e4.subs(ad1, -ad1) - e4) == 0 and not e4.has(ad2) and not PX.has(sp.sqrt(X))
    dP = sp.diff(PX, X)
    f_even = sp.expand(F_rec.subs(ad1, -ad1) - F_rec) == 0
    ok3 = even and f_even and sp.expand(3 * F_rec.subs(ad1, sp.sqrt(X)) - 2 * dP) == 0
    check("A3_F_equals_two_thirds_dP_dX", ok3,
          "P(X) := sum_k alpha_k E_(k)^x4_x4 at a4'^2 = X is a polynomial in X (E^x4_x4 is even in a4' and free of "
          "a4''); F is even in a4' as well (so the equations are invariant under x4 -> -x4, which exchanges deflation and "
          "inflation of the extra times); 3 F(a4') = 2 dP/dX at X = a4'^2 exactly; P(X) = %s" % sp.sstr(sp.collect(PX, X)))
    # A4: constraint propagation with a source that depends on x4 only through a4(x4)
    x4 = sp.Symbol("x4")
    a = sp.Function("a4")(x4)
    rb = sp.Function("rhobar")
    Dsym = -sp.diff(rb(a), x4) / sp.diff(a, x4) / 3          # p3_bar - p_t_bar from the averaged energy relation
    constraint = PX.subs(X, sp.diff(a, x4) ** 2) + Lam + kap * rb(a)
    evolution = sp.diff(a, x4, 2) * F_rec.subs(ad1, sp.diff(a, x4)) - kap * Dsym
    prop = sp.simplify(sp.expand(sp.diff(constraint, x4) - 3 * sp.diff(a, x4) * evolution))
    check("A4_constraint_propagation_with_averaged_source", prop == 0,
          "for any source that depends on x4 only through a4(x4) and obeys d rho_bar/d a4 = -3 (p3_bar - p_t_bar): "
          "d/dx4 [P(a4'^2) + Lambda + kappa rho_bar(a4)] = 3 a4' [a4'' F(a4') - kappa (p3_bar - p_t_bar)] exactly; so the "
          "x4 moment (constraint) and the x1 - x5 moment (evolution) are mutually consistent, and for a4' != 0 the "
          "evolution follows from the first integral P(a4'^2) + Lambda + kappa rho_bar(a4) = 0")
    # A5: residual of the x8 equation once Lambda is eliminated with the constraint
    null_rec = parse(a4["generalSource"]["nullCombinations"]["kappa(rho+p8)"]["input"])
    r8 = sp.expand(lhs["x8x8"] - lhs["x4x4"] - null_rec)
    check("A5_x8_residual_after_constraint", r8 == 0,
          "with Lambda = -P(a4'^2) - kappa rho (constraint) the x8 equation sum_k alpha_k E^x8_x8 + Lambda = kappa p8 "
          "becomes R8 := N(a4') - kappa (rho + p8) = 0 with N = sum_k alpha_k (E^x8_x8 - E^x4_x4) = generalSource."
          "nullCombinations[kappa(rho+p8)] (equal exactly); Einstein: N = -6 (a4'^2 + H^2) < 0")
    # A6: the x8 conservation identity in the y coordinate and its integral
    x8s, ys = sp.symbols("x8 y", positive=True)
    z = 6 * H * x8s
    yfun = sp.log(sp.sin(z)) / (6 * H)
    dy_dx8 = sp.simplify(sp.diff(yfun, x8s) - sp.cot(z)) == 0
    vol = sp.simplify(sp.cos(z) / sp.cot(z) - sp.sin(z)) == 0          # sqrt|g| dx8 = cos z dx8 = sin z dy = e^{6Hy} dy
    cons = parse(a4["generalSource"]["conservation_x8"]["input"].replace("d4q48", "0").replace("d8p8", "(cc*p8y)"))
    in_y = sp.expand(cons / cc - (p8y + 6 * H * p8 - 3 * H * (p3 + pt)))
    alg = sp.expand((p3 + pt - 2 * p8) - p8y / (3 * H) - (-(p8y + 6 * H * p8 - 3 * H * (p3 + pt)) / (3 * H)))
    fy = sp.Function("p8f")(ys)
    integrand = sp.diff(sp.exp(6 * H * ys) * fy, ys) - sp.exp(6 * H * ys) * (sp.diff(fy, ys) + 6 * H * fy)
    ok6 = dy_dx8 and vol and in_y == 0 and alg == 0 and sp.simplify(integrand) == 0
    check("A6_x8_conservation_in_y", ok6,
          "y = ln(sin z)/(6H) gives dy/dx8 = cot z and sqrt|g| dx8 = cos z dx8 = e^{6Hy} dy; generalSource."
          "conservation_x8 with q48 = 0 is cot z [p8_y + 6 H p8 - 3 H (p3 + p_t)] = 0, so on shell p3 + p_t - 2 p8 = "
          "p8_y/(3H) EXACTLY (the algebraic condition fails exactly where p8 depends on x8) and d/dy(e^{6Hy} p8) = "
          "3 H e^{6Hy} (p3 + p_t), i.e. int_{-L}^{0} e^{6Hy} (p3 + p_t) dy = [e^{6Hy} p8]_{-L}^{0}/(3H)")
    polys = {}
    for gname, g1, g2, g3, _ in GRAVITY:
        sub = {al1: sp.Rational(g1.numerator, g1.denominator), al2: sp.Rational(g2.numerator, g2.denominator),
               al3: sp.Rational(g3.numerator, g3.denominator), H: 1}
        P = sp.Poly(sp.expand(PX.subs(sub)), X)
        N8 = sp.Poly(sp.expand(null_rec.subs(sub).subs(ad1, sp.sqrt(X))), X)
        polys[gname] = {"P": [Fraction(int(c.p), int(c.q)) for c in P.all_coeffs()],
                        "N": [Fraction(int(c.p), int(c.q)) for c in N8.all_coeffs()],
                        "Pstr": sp.sstr(P.as_expr()), "Nstr": sp.sstr(N8.as_expr())}
    return polys


# ---------------------------------------------------------------------------------------------------------------------
# helpers: polynomials, interpolation, quadrature
# ---------------------------------------------------------------------------------------------------------------------
def horner(coeffs: list, x: float) -> float:
    v = 0.0
    for c in coeffs:
        v = v * x + float(c)
    return v


def dcoeffs(coeffs: list) -> list:
    n = len(coeffs) - 1
    return [c * (n - i) for i, c in enumerate(coeffs[:-1])] or [Fraction(0)]


def real_roots_deriv(coeffs: list) -> list:
    """real roots of dP/dX (degree <= 2), exact discriminant sign, sorted"""
    d = dcoeffs(coeffs)
    while len(d) > 1 and d[0] == 0:
        d = d[1:]
    if len(d) == 1:
        return []
    if len(d) == 2:
        return [-float(d[1]) / float(d[0])]
    A_, B_, C_ = d
    disc = B_ * B_ - 4 * A_ * C_
    if disc < 0:
        return []
    s = math.sqrt(float(disc))
    r = sorted([(-float(B_) - s) / (2 * float(A_)), (-float(B_) + s) / (2 * float(A_))])
    return r


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
                p0, p1 = 1.0, x
                for k in range(2, n + 1):
                    p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
                dp = n * (x * p1 - p0) / (x * x - 1)
                dx = p1 / dp
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
    Hn = float(params["physics"]["H"])
    L = float(params["physics"]["L_tipCutoff"])
    vol7 = float(params["physics"]["Vol7"])
    slices = [float(s) for s in params["physics"]["slicesA4"]]
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
        comp = {c: [r[c] for r in rows] for c in ("rho", "p3", "p_t", "p8")}
        sid = p.stem
        it = integ[sid]
        st = {"id": sid, "N": int(float(it["N"])), "lambda_tag": it["lambda_tag"], "lambda": float(it["lambda"]),
              "a4": float(it["a4"]), "h": h, "ys": ys}
        scale = max(max(abs(v) for v in comp[c]) for c in comp)
        st["zero"] = scale == 0.0
        # B1: integrals against the solver
        worst_int = 0.0
        for c, ic in (("rho", "int_rho"), ("p3", "int_p3"), ("p_t", "int_p_t"), ("p8", "int_p8")):
            I = simpson([w[i] * comp[c][i] for i in range(len(ys))], h)
            st[c + "_bar"] = I / wvol
            ref = float(it[ic]) / (2 * vol7)
            den = max(abs(ref), max(abs(float(it[k])) for k in ("int_rho", "int_p3", "int_p_t", "int_p8")) / (2 * vol7))
            if den > 0:
                worst_int = max(worst_int, abs(I - ref) / den)
        st["int_rel"] = worst_int
        if st["zero"]:
            states[sid] = st
            continue
        # B2: pointwise x8 conservation by 4th-order central differences
        p8v, s = comp["p8"], [comp["p3"][i] + comp["p_t"][i] for i in range(len(ys))]
        worst = 0.0
        for i in range(2, len(ys) - 2):
            d = (-p8v[i + 2] + 8 * p8v[i + 1] - 8 * p8v[i - 1] + p8v[i - 2]) / (12 * h)
            res = d + 6 * Hn * p8v[i] - 3 * Hn * s[i]
            den = max(abs(d), abs(6 * Hn * p8v[i]), abs(3 * Hn * s[i]))
            if den > 0:
                worst = max(worst, abs(res) / den)
        st["cons_fd_rel"] = worst
        st["var_ratio"] = (max(comp["rho"]) - min(comp["rho"])) / scale
        st["int_ratio"] = ((float(it["int_p3"]) + float(it["int_p_t"])) / (2 * float(it["int_p8"]))
                           if float(it["int_p8"]) != 0.0 else None)
        st["alg_pointwise_rel"] = max(abs(s[i] - 2 * p8v[i]) for i in range(len(ys))) / scale
        # B3: integrated identity (solver integrals and end values): int (p3 + p_t) = 2 Vol7 [e^{6Hy} p8]/(3H)
        lhs = float(it["int_p3"]) + float(it["int_p_t"])
        rhs = 2 * vol7 * (float(it["p8_brane"]) - math.exp(-6 * Hn * L) * float(it["p8_tip"])) / (3 * Hn)
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
        a = [s[i] - 2 * p8v[i] for i in range(len(ys))]
        tn = simpson([w[i] * sum(comp[c][i] ** 2 for c in comp) for i in range(len(ys))], h)
        st["alg_L2_rel"] = math.sqrt(simpson([w[i] * a[i] ** 2 for i in range(len(ys))], h) / tn)
        st["alg_bar_rel"] = abs(st["p3_bar"] + st["p_t_bar"] - 2 * st["p8_bar"]) / (
            abs(st["p3_bar"]) + abs(st["p_t_bar"]) + 2 * abs(st["p8_bar"]))
        st["rho_brane"], st["rho_tip"] = float(it["rho_brane"]), float(it["rho_tip"])
        ad = adia[sid]
        st["dE_fd"], st["dE_emt"] = float(ad["dE_da4_finite_difference"]), float(ad["dE_da4_emt"])
        st["Q_max"] = float(ad["Q_max"])
        states[sid] = st
    return states, slices, {"H": Hn, "L": L, "Vol7": vol7, "wvol": wvol}


def series_of(states: dict, tag: str, slices: list) -> list:
    out = []
    for a in slices:
        sid = "%s_a%02d" % (tag, int(round(10 * a)))
        if sid not in states:
            err("missing Kohn-Sham state %s" % sid)
        out.append(states[sid])
    return out


# ---------------------------------------------------------------------------------------------------------------------
# D: integration of the truncated system
# ---------------------------------------------------------------------------------------------------------------------
def integrate_case(poly: dict, ser: list, slices: list, sigma0: float, A0f: float) -> dict:
    Pc, Nc = poly["P"], poly["N"]
    rb = [s["rho_bar"] for s in ser]
    D = [s["p3_bar"] - s["p_t_bar"] for s in ser]
    p8b = [s["p8_bar"] for s in ser]
    r0 = rb[0]
    kappa = sigma0 / r0                     # sigma0 = kappa rho_bar(a4 = 0) / H^2
    X0 = A0f * A0f
    P0 = horner(Pc, X0)
    Lam_ = -P0 - sigma0                     # constraint at a4 = 0
    dP = dcoeffs(Pc)
    crit = [c for c in real_roots_deriv(Pc) if c > 0]
    lo = max([0.0] + [c for c in crit if c < X0])
    his = [c for c in crit if c > X0]
    hi = min(his) if his else math.inf
    inc = horner(dP, X0) > 0                # P increasing on the branch

    def target(a):                          # P(X(a)) = -Lambda - kappa rho_bar(a)
        v, _ = hermite(slices, rb, [-3 * d for d in D], a)
        return -Lam_ - kappa * v

    Plo = horner(Pc, lo)
    Phi = horner(Pc, hi) if hi < math.inf else (math.inf if inc else -math.inf)

    def inside(T):
        a_, b_ = (Plo, Phi) if inc else (Phi, Plo)
        return a_ < T < b_

    def Xof(T):
        a_, b_ = lo, (hi if hi < math.inf else max(2 * X0 + 10, 10.0))
        if hi == math.inf:
            while (horner(Pc, b_) - T) * (1 if inc else -1) < 0:
                b_ *= 2
        for _ in range(200):
            m = 0.5 * (a_ + b_)
            if (horner(Pc, m) - T) * (1 if inc else -1) < 0:
                a_ = m
            else:
                b_ = m
        return 0.5 * (a_ + b_)

    # M1: scan for the first event on a fine grid, then bisection
    a_end, event = slices[-1], "regular"
    n = 4000
    prev = 0.0
    for i in range(1, n + 1):
        a = slices[-1] * i / n
        if not inside(target(a)):
            lo_a, hi_a = prev, a
            for _ in range(200):
                m = 0.5 * (lo_a + hi_a)
                if inside(target(m)):
                    lo_a = m
                else:
                    hi_a = m
            a_end = 0.5 * (lo_a + hi_a)
            Tend = target(a_end)
            at_lo = abs(Tend - Plo) <= abs(Tend - Phi)
            event = "turning_point" if (at_lo and lo == 0.0) else "branch_point"
            break
        prev = a
    # x4 elapsed: x4 = int_0^{a_end} da / sqrt(X(a)), substitution a = a_end (1 - t^2) (integrable 1/sqrt end)
    gx, gw = gauss_legendre()
    x4_end = 0.0
    for xi, wi in zip(gx, gw):
        t = 0.5 * (xi + 1)
        a = a_end * (1 - t * t)
        Xa = Xof(target(a)) if a > 0 else X0
        x4_end += 0.5 * wi * 2 * a_end * t / math.sqrt(Xa) if Xa > 0 else 0.0
    if event == "regular":
        X_end = Xof(target(a_end))
    elif event == "turning_point":
        X_end = 0.0
    else:
        X_end = lo if abs(target(a_end) - Plo) <= abs(target(a_end) - Phi) else hi
    X_sl = [Xof(target(a)) if a <= a_end + 1e-15 and inside(target(a)) else None for a in slices]
    # residual of the dropped x8 moment at the slices reached: R8 = N(X) - kappa (rho_bar + p8_bar)
    r8 = []
    for i, a in enumerate(slices):
        if X_sl[i] is None:
            continue
        Nx = horner(Nc, X_sl[i])
        e8 = horner(Pc, X_sl[i]) + Nx         # sum alpha E^x8_x8 = P + N
        R = Nx - kappa * (rb[i] + p8b[i])
        scale = max(abs(e8), abs(Lam_), abs(kappa * p8b[i]))
        r8.append(abs(R) / scale)
    alg = [abs(D_ + 2 * s["p_t_bar"] - 2 * s["p8_bar"]) / (abs(s["p3_bar"]) + abs(s["p_t_bar"]) + 2 * abs(s["p8_bar"]))
           for D_, s in zip(D, ser)]
    # adiabaticity along the solution: Q scales with a4' (Q_max recorded at a4' = H)
    q = [ser[i]["Q_max"] * math.sqrt(X_sl[i]) for i in range(len(slices)) if X_sl[i] is not None]
    # M2: RK4 of a4'' F(a4') = kappa (p3_bar - p_t_bar)(a4), source from a natural spline of the 5 values of D
    m2 = None
    if event != "branch_point":
        if all(d > 0 for d in D):           # D decays roughly exponentially: spline its logarithm
            lspl = natural_spline(slices, [math.log(d) for d in D])

            def Dspl(a):
                return math.exp(lspl(a))
        else:
            Dspl = natural_spline(slices, D)

        def Fv(v):
            return 2.0 / 3.0 * horner(dP, v * v)

        def rhs(a, v):
            return v, kappa * Dspl(min(max(a, 0.0), slices[-1])) / Fv(v)
        a, v, x = 0.0, A0f, 0.0
        hstep = 1e-3
        turned = None
        for _ in range(4_000_000):
            k1 = rhs(a, v)
            k2 = rhs(a + hstep / 2 * k1[0], v + hstep / 2 * k1[1])
            k3 = rhs(a + hstep / 2 * k2[0], v + hstep / 2 * k2[1])
            k4 = rhs(a + hstep * k3[0], v + hstep * k3[1])
            an = a + hstep / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
            vn = v + hstep / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            if an >= slices[-1]:
                f = (slices[-1] - a) / (an - a)
                m2 = {"a_end": slices[-1], "v_end": v + f * (vn - v), "x4_end": x + f * hstep}
                break
            if vn <= 0.0:
                f = v / (v - vn)
                turned = {"a_end": a + f * (an - a), "v_end": 0.0, "x4_end": x + f * hstep}
                m2 = turned
                break
            a, v, x = an, vn, x + hstep
    return {"kappa": kappa, "Lambda": Lam_, "event": event, "a_end": a_end, "x4_end": x4_end,
            "A_end": math.sqrt(X_end), "X_sl": X_sl, "r8_max": max(r8) if r8 else None, "alg_max": max(alg),
            "q_max": max(q) if q else None, "branch": (lo, hi), "m2": m2, "P0": P0}


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
    for p in (A4_JSON, KS_PARAMS, KS_INTEGRALS, KS_ADIABATIC, KS_HISTORY, KS_THEORY, WAVE1):
        if not p.is_file():
            err("missing input %s" % p)
    try:
        a4 = json.loads(A4_JSON.read_text(encoding="utf-8"))
        params = json.loads(KS_PARAMS.read_text(encoding="utf-8"))
        history = json.loads(KS_HISTORY.read_text(encoding="utf-8"))
        kst = json.loads(KS_THEORY.read_text(encoding="utf-8"))
    except (OSError, ValueError) as ex:
        err("cannot read an input: %s" % ex)
    if "p8' + 6H p8 = 3H (p3 + p_t)" not in kst["emt"]["conservationY"]:
        err("ks-theory.json emt.conservationY is not the expected identity")

    # ---------------- A
    polys = part_a(a4)

    # ---------------- B
    states, slices, geo = part_bc(params)
    nz = [s for s in states.values() if not s["zero"]]
    zero = sorted(s["id"] for s in states.values() if s["zero"])
    wi = max(states.values(), key=lambda s: s["int_rel"])
    check("B1_integrals_reproduced", wi["int_rel"] <= TOL_INTEGRAL,
          "Simpson's rule with the volume weight e^{6Hy} on the 151-point output grid (y = -L ... 0, L = %s) reproduces "
          "results/ground/emt-integrals.csv (int_X = 2 Vol_7 int e^{6Hy} X dy, Vol_7 = %s, the doubled system) for all "
          "%d states: largest relative difference %s (%s); hence the weighted average X_bar = int_X / (2 Vol_7 W), "
          "W = int_{-L}^{0} e^{6Hy} dy = %s" % (g6(geo["L"]), g6(geo["Vol7"]), len(states), g6(wi["int_rel"]), wi["id"],
                                               g6(geo["wvol"])))
    wc = max(nz, key=lambda s: s["cons_fd_rel"])
    check("B2_x8_conservation_on_every_profile", wc["cons_fd_rel"] <= TOL_CONS_FD,
          "p8_y + 6 H p8 - 3 H (p3 + p_t) = 0 (check A6) evaluated with 4th-order central differences on the output "
          "grid (dy = %s) of the %d nonzero profiles: largest residual relative to the largest term %s (%s; tolerance %s "
          "from the finite-difference truncation). The recorded states CONSERVE energy-momentum along x8; therefore their "
          "violation of p3 + p_t = 2 p8 is exactly p8_y/(3H): the source fails the field equations because p8 (and with "
          "it every component) depends on x8, not because conservation fails"
          % (g6(wc["h"]), len(nz), g6(wc["cons_fd_rel"]), wc["id"], g6(TOL_CONS_FD)))
    wid = max(nz, key=lambda s: s["identity_rel"])
    check("B3_integrated_x8_identity", wid["identity_rel"] <= TOL_IDENTITY,
          "int (p3 + p_t) = 2 Vol_7 [e^{6Hy} p8]_{-L}^{0}/(3H) with the solver's integrals and end values p8_brane, "
          "p8_tip (emt-integrals.csv) for the %d nonzero states: largest relative difference %s (%s). So "
          "p3_bar + p_t_bar - 2 p8_bar = ([e^{6Hy} p8]_{-L}^{0} - 6 H W p8_bar)/(3 H W): the averaged algebraic "
          "condition holds only if the boundary flux of p8 equals the value an x8-independent p8 would give"
          % (len(nz), g6(wid["identity_rel"]), wid["id"]))
    mus = {c: [s["mu_" + c] for s in nz if s["mu_" + c] is not None] for c in ("rho", "p3", "p_t", "p8")}
    mu1 = {c: [s["mu1_" + c] for s in nz if s["mu1_" + c] is not None] for c in ("rho", "p3", "p_t", "p8")}
    ptzero = [s["id"] for s in nz if s["mu_p_t"] is None]
    mu_rho_min = min(nz, key=lambda s: s["mu_rho"])
    mu1_rho_min = min(nz, key=lambda s: s["mu1_rho"])
    ok_mu = all(s["mu_rho"] > 1e-3 and s["mu_p8"] > 1e-3 and s["mu1_rho"] > 1e-3 and s["mu1_p8"] > 1e-3 for s in nz)

    def rng(v):
        return "[%s, %s]" % (g6(min(v)), g6(max(v))) if v else "-"
    tips = [s["tip_share_rho"] for s in nz]
    check("B4_hidden_direction_mismatch", ok_mu,
          "the field equations require every component to be independent of x8, the profiles are not. Two measures over "
          "the patch with the volume weight e^{6Hy}: (L1) mu1_X = int e^{6Hy} |X - X_bar| / int e^{6Hy} |X| (0 for an "
          "x8-independent X; above 1 where X changes sign along x8): over the %d nonzero states mu1_rho "
          "in %s (smallest %s), mu1_p3 in %s, mu1_p8 in %s, mu1_p_t in %s; (L2) mu_X = ||X - X_bar||/||X|| (X_bar is the "
          "orthogonal projection of X on the x8-independent functions): mu_rho in %s (smallest %s), mu_p3 in %s, mu_p8 in "
          "%s, mu_p_t in %s - the L2 norm is weighted towards the tip (the share of ||rho||^2 from the tip half y < -L/2 "
          "is %s), so the L1 measure is the less cut-off dependent one; p_t = e_int is identically zero (hence "
          "x8-independent) in the %d states with lambda = 0; the algebraic defect ||p3 + p_t - 2 p8||/||(rho, p3, p_t, "
          "p8)|| lies in %s. Every measure is O(1): the computed source is NOT close to an x8-independent one"
          % (len(nz), rng(mu1["rho"]), mu1_rho_min["id"], rng(mu1["p3"]), rng(mu1["p8"]), rng(mu1["p_t"]),
             rng(mus["rho"]), mu_rho_min["id"], rng(mus["p3"]), rng(mus["p8"]), rng(mus["p_t"]), rng(tips),
             len(ptzero), rng([s["alg_L2_rel"] for s in nz])))
    # B0: the wave-1 report ks-source-conditions.json, re-derived independently from the same Kohn-Sham files
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
    exp = [("ks_profiles_depend_on_x8", ["%d with a nonzero" % len(nz), ">= %s (smallest: %s)"
                                         % (g6(vmin_s["var_ratio"]), vmin_s["id"])]),
           ("ks_profiles_violate_algebraic_condition", ["between %s (%s) and %s (%s)" % (
               g6(amin_s["alg_pointwise_rel"]), amin_s["id"], g6(amax_s["alg_pointwise_rel"]), amax_s["id"])]),
           ("ks_integrals_violate_algebraic_condition", ["closest to 1: %s at %s" % (g6(rat[rbest]), rbest)]),
           ("ks_zero_source_states_listed", ["%d states have an identically vanishing" % len(zero)])]
    ok0 = w1["summary"]["fail"] == 0 and all(c["verdict"] == "PASS" for c in w1["checks"])
    missing = [n for n, subs in exp if n not in w1c or not all(x in w1c[n]["detail"] for x in subs)]
    check("B0_wave1_report_verified", ok0 and not missing and all(rat[k] < 1.0 for k in rat),
          "%s (all %d checks PASS) re-derived independently from the same Kohn-Sham files: %d nonzero states; the "
          "smallest x8 variation (max rho - min rho)/max|T| = %s (%s); the pointwise algebraic defect max|p3 + p_t - "
          "2 p8|/max|T| from %s (%s) to %s (%s); the integrated ratio (int p3 + int p_t)/(2 int p8) closest to 1 is %s "
          "(%s) and below 1 for every state - all equal to the numbers in that report%s. REFINEMENT: the recorded states "
          "do NOT violate the x8 conservation identity d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t) = 0; they satisfy it "
          "(check B2); what fails is p3 + p_t = 2 p8, which is that identity combined with x8-independence"
          % (rel(WAVE1), len(w1["checks"]), len(nz), g6(vmin_s["var_ratio"]), vmin_s["id"],
             g6(amin_s["alg_pointwise_rel"]), amin_s["id"], g6(amax_s["alg_pointwise_rel"]), amax_s["id"],
             g6(rat[rbest]), rbest, "" if not missing else " EXCEPT " + ", ".join(missing)))
    # ---------------- C
    walg = min(nz, key=lambda s: s["alg_bar_rel"])
    check("C1_averaged_algebraic_condition_fails", all(s["alg_bar_rel"] > 1e-3 for s in nz),
          "the x1 + x5 - 2 x8 moment reads 0 = kappa (p3_bar + p_t_bar - 2 p8_bar) whatever a4, Lambda, alpha_k (check A1); "
          "|p3_bar + p_t_bar - 2 p8_bar| / (|p3_bar| + |p_t_bar| + 2 |p8_bar|) lies in [%s (%s), %s] over the %d nonzero "
          "states: an O(1) violation, so no choice of kappa != 0 makes the hidden-direction averaged Kohn-Sham source "
          "satisfy all moments; dropping this combination (and with it the x8 moment) is an APPROXIMATION whose error "
          "is this defect" % (g6(walg["alg_bar_rel"]), walg["id"], g6(max(s["alg_bar_rel"] for s in nz)), len(nz)))
    wsolv = max(nz, key=lambda s: abs(s["dE_fd"] - s["dE_emt"]) / max(abs(s["dE_emt"]), 1e-300)
                if s["dE_emt"] != 0 else 0.0)
    solv_rel = (abs(wsolv["dE_fd"] - wsolv["dE_emt"]) / abs(wsolv["dE_emt"])) if wsolv["dE_emt"] != 0 else 0.0
    # energy relation between slices: rho_bar(a_{i+2}) - rho_bar(a_i) = -3 int (p3_bar - p_t_bar) da (Simpson, h = 0.5)
    tags = sorted({s["id"].rsplit("_a", 1)[0] for s in nz})
    worst_sl, worst_tag = 0.0, ""
    for tag in tags:
        ser = series_of(states, tag, slices)
        rb = [s["rho_bar"] for s in ser]
        D = [s["p3_bar"] - s["p_t_bar"] for s in ser]
        hs = slices[1] - slices[0]
        for i0 in (0, 2):
            ch = rb[i0 + 2] - rb[i0]
            pred = -3 * simpson(D[i0:i0 + 3], hs)
            den = max(abs(ch), abs(pred), 1e-300)
            if abs(ch) > 0 or abs(pred) > 0:
                if abs(ch - pred) / den > worst_sl:
                    worst_sl, worst_tag = abs(ch - pred) / den, "%s on [%s, %s]" % (tag, slices[i0], slices[i0 + 2])
    crossings = sum(len(s["fermiLevelCrossings"]) for s in history["series"])
    check("C2_averaged_energy_relation", solv_rel <= TOL_ENERGY_SOLVER and worst_sl <= TOL_ENERGY_SLICES
          and crossings == 0,
          "d rho_bar/d a4 = -3 (p3_bar - p_t_bar) (the x4 moment of nabla_mu T^mu_x4 = 0 for the instantaneous states; "
          "T^x4_y = 0): (i) the solver's finite-difference dE/da4 agrees with the energy-momentum formula to %s "
          "(largest relative difference, %s; adiabaticity.csv); (ii) between slices, Simpson's rule on the 5 slices "
          "(h = 0.5) reproduces the change of rho_bar to %s (worst: %s; tolerance %s for the step 0.5); (iii) "
          "history.json records %d Fermi-level crossings, so the instantaneous ground states form one adiabatic family "
          "along a4 in [0, 2]" % (g6(solv_rel), wsolv["id"], g6(worst_sl), worst_tag, g6(TOL_ENERGY_SLICES), crossings))
    # x4 + x8 moments (Einstein): kappa (p8_bar - rho_bar) = 36 H^2 + 2 Lambda must be constant along the history
    var = []
    for tag in tags:
        ser = series_of(states, tag, slices)
        q = [s["p8_bar"] - s["rho_bar"] for s in ser]
        var.append((abs(max(q) - min(q)) / max(abs(v) for v in q), tag))
    vmin = min(var)
    const_tags = sorted(t for v, t in var if v <= 1e-9)
    moving = [(v, t) for v, t in var if v > 1e-9]
    check("C3_x8_moment_inconsistent_with_history", all(t.startswith("N8_") for t in const_tags) and moving
          and all(v > 0.05 for v, _ in moving),
          "Einstein gravity: the x4 and x8 moments give kappa (p8_bar - rho_bar) = 36 H^2 + 2 Lambda (a constant), and "
          "the x8 moment with the evolution needs d p8_bar/d a4 = d rho_bar/d a4, the same condition; along the history "
          "p8_bar - rho_bar varies by a fraction %s ... %s of its largest value in the %d series with momentum, so every "
          "set of moments containing the x8 moment is inconsistent for them; it is constant (a4-independent source) "
          "only in the N = 8 interacting series %s, whose x1 + x5 - 2 x8 moment still fails (check C1)"
          % (g6(min(v for v, _ in moving)), g6(max(v for v, _ in moving)), len(moving), ", ".join(const_tags)))
    mom = [s for s in nz if s["N"] > 8]
    check("C4_source_signs", all(s["p3_bar"] - s["p_t_bar"] > 0 and s["rho_bar"] > 0 and s["rho_bar"] + s["p8_bar"] > 0
                                 for s in mom)
          and all(abs(s["p3_bar"] - s["p_t_bar"]) <= 1e-12 * max(abs(s["p3_bar"]), 1e-300) + 1e-18
                  for s in nz if s["N"] == 8),
          "for the %d nonzero states with N = 136, 688: rho_bar > 0, rho_bar + p8_bar > 0 and p3_bar - p_t_bar > 0 "
          "(range %s ... %s); for the N = 8 interacting states (k = 0 brane zero modes) p3_bar = p_t_bar (no 3-momentum) "
          "and the source does not depend on a4; so the evolution source kappa (p3_bar - p_t_bar) has the sign of kappa "
          "for N = 136, 688 and vanishes for N = 8"
          % (len(mom), g6(min(s["p3_bar"] - s["p_t_bar"] for s in mom)),
             g6(max(s["p3_bar"] - s["p_t_bar"] for s in mom))))

    # ---------------- D
    branches = {}
    for gname, g1, g2, g3, gdesc in GRAVITY:
        Pc = polys[gname]["P"]
        crit = [c for c in real_roots_deriv(Pc) if c > 0]
        branches[gname] = crit
    check("D0_gravity_branches", branches["einstein"] == [] and len(branches["egb"]) == 1
          and abs(branches["egb"][0] - 5.0 / 3.0) < 1e-12 and branches["lovelock3"] == [],
          "dP/dX (F = (2/3) dP/dX, check A3) has no positive root for Einstein (F = 2) and for the cubic Lovelock case "
          "(discriminant < 0: F > 0 for every a4'), and the single root X = a4'^2 = 5/3 H^2 for Einstein-Gauss-Bonnet "
          "(F = 1 - (3/5) a4'^2/H^2): there the evolution equation is singular (branch point); P(X): einstein %s; egb %s; lovelock3 %s"
          % (polys["einstein"]["Pstr"], polys["egb"]["Pstr"], polys["lovelock3"]["Pstr"]))
    cases = []
    for gname, g1, g2, g3, gdesc in GRAVITY:
        for tag in SERIES:
            ser = series_of(states, tag, slices)
            P1 = horner(polys[gname]["P"], float(A0) ** 2)
            sig_list = [(float(s_), "sigma0 = %s" % s_) for s_ in SIGMAS] + [(-P1, "Lambda = 0")]
            for sig, label in sig_list:
                res = integrate_case(polys[gname], ser, slices, sig, float(A0))
                res.update({"gravity": gname, "series": tag, "sigma0": sig, "label": label})
                cases.append(res)
    # D1: methods agree (regular and turning-point cases)
    worst_m, worst_case = 0.0, ""
    for c in cases:
        if c["m2"] is None:
            continue
        m2 = c["m2"]
        d1 = abs(m2["a_end"] - c["a_end"]) / max(c["a_end"], 1e-300)
        d2 = abs(m2["x4_end"] - c["x4_end"]) / c["x4_end"]
        d3 = abs(m2["v_end"] - c["A_end"]) / max(c["A_end"], 0.05) if c["event"] == "regular" else abs(m2["v_end"])
        d = max(d1, d2, d3)
        if d > worst_m:
            worst_m, worst_case = d, "%s %s %s" % (c["gravity"], c["series"], c["label"])
    n_m2 = sum(1 for c in cases if c["m2"] is not None)
    check("D1_two_integration_methods_agree", worst_m <= TOL_METHODS and n_m2 == sum(1 for c in cases
                                                                                         if c["event"] != "branch_point"),
          "M1 (first integral P(a4'^2) = -Lambda - kappa rho_bar(a4), rho_bar by the cubic Hermite interpolant with the "
          "exact slopes -3 (p3_bar - p_t_bar); x4 by Gauss-Legendre quadrature) against M2 (RK4 of a4'' F(a4') = kappa "
          "(p3_bar - p_t_bar)(a4), source by a natural cubic spline of ln(p3_bar - p_t_bar) through the 5 values (of the "
          "values themselves when they vanish), step 1e-3) for the %d regular "
          "and turning-point cases: end point, elapsed x4 and end rate agree to %s (worst: %s; tolerance %s for two different "
          "interpolations between slices 0.5 apart)" % (n_m2, g6(worst_m), worst_case, g6(TOL_METHODS)))
    # D2: Einstein, analytic content of the first integral, checked on the cases
    worst_e = 0.0
    for c in cases:
        if c["gravity"] != "einstein":
            continue
        ser = series_of(states, c["series"], slices)
        for i, s in enumerate(ser):
            if c["X_sl"][i] is None:
                continue
            pred = 1.0 + c["sigma0"] / 3 * (1 - s["rho_bar"] / ser[0]["rho_bar"])
            worst_e = max(worst_e, abs(c["X_sl"][i] - pred) / max(abs(pred), 1e-300))
    check("D2_einstein_first_integral", worst_e <= 1e-9,
          "Einstein gravity: a4'^2(a4) = a4'^2(0) - (kappa/3)(rho_bar(a4) - rho_bar(0)), i.e. a4'^2/H^2 = A0^2 + "
          "(sigma0/3)(1 - rho_bar(a4)/rho_bar(0)) with sigma0 = kappa rho_bar(0)/H^2 and Lambda = -3 A0^2 H^2 - 21 H^2 - "
          "sigma0 H^2; reproduced at every slice reached by every Einstein case to %s" % g6(worst_e))
    # D3: classification statements
    ein = [c for c in cases if c["gravity"] == "einstein"]
    lam0 = [c for c in cases if c["label"] == "Lambda = 0"]
    lam0_mom = [c for c in lam0 if not c["series"].startswith("N8_")]
    ok3 = all(c["event"] == "turning_point" and c["sigma0"] < 0 for c in lam0_mom)
    check("D3_lambda_zero_cases_halt", ok3,
          "with Lambda = 0 and the initial rate a4'(0) = H the constraint needs sigma0 = -P(H^2) < 0 (kappa rho_bar < 0) in "
          "all three theories; then for every series with momentum the deflation HALTS inside the computed range: "
          "turning point a4' = 0 at %s (gravity/series: a4*)" % "; ".join(
              "%s/%s: %s" % (c["gravity"], c["series"], g6(c["a_end"])) for c in lam0_mom))
    n8 = [c for c in cases if c["series"].startswith("N8_")]
    check("D4_constant_source_gives_linear_member", all(c["event"] == "regular" and abs(c["A_end"] - 1.0) < 1e-12
                                                        for c in n8),
          "for the N = 8 interacting source (a4-independent, p3_bar = p_t_bar) the truncated system gives exactly the "
          "linear member a4 = A0 H x4 + a0 for every sigma0 and theory (%d cases; the rate is the initial condition, "
          "Lambda absorbs kappa rho_bar); the dropped x8 moment fails by the C1 defect" % len(n8))
    ok5 = all((c["sigma0"] > 0 and c["A_end"] > 1.0) or (c["sigma0"] < 0 and (c["A_end"] < 1.0))
              for c in ein if not c["series"].startswith("N8_"))
    check("D5_einstein_sign_of_the_effect", ok5,
          "Einstein gravity, series with momentum: the Kohn-Sham source accelerates the deflation (a4' grows, extra times "
          "deflate faster) for sigma0 > 0 (kappa > 0, which needs Lambda < -21 H^2 - kappa rho_bar(0)) and decelerates it "
          "for sigma0 < 0; the total change of a4'^2 over a4 in [0, 2] is (sigma0/3)(1 - rho_bar(2)/rho_bar(0)) H^2, i.e. "
          "at most %s |sigma0| H^2 (bounded by the energy the gas loses)"
          % g6(max((1 - series_of(states, t, slices)[-1]["rho_bar"] / series_of(states, t, slices)[0]["rho_bar"]) / 3
                   for t in SERIES if not t.startswith("N8_"))))
    egb_branch = [c for c in cases if c["event"] == "branch_point"]
    check("D6_branch_points_only_for_egb", all(c["gravity"] == "egb" and c["sigma0"] > 0 for c in egb_branch)
          and len(egb_branch) > 0,
          "the evolution equation is not well defined where F(a4') = 0; this happens only for Einstein-Gauss-Bonnet "
          "with sigma0 > 0 (the first integral pushes a4'^2 up to the branch point 5/3 H^2): %d cases, e.g. %s"
          % (len(egb_branch), "; ".join("%s %s: a4* = %s" % (c["series"], c["label"], g6(c["a_end"]))
                                        for c in egb_branch[:4])))
    r8s = [c["r8_max"] for c in cases if c["r8_max"] is not None and not c["series"].startswith("N8_")]
    qs = [c["q_max"] for c in cases if c["q_max"] is not None]
    check("D7_dropped_x8_moment_residual_and_adiabaticity", min(r8s) > 1e-3 and max(qs) < 1.0,
          "the dropped x8 moment R8 = N(a4') - kappa (rho_bar + p8_bar) (check A5) relative to the largest term of the "
          "x8 equation, at the slices reached: %s ... %s over the cases with momentum (never small: the truncation is "
          "not a small perturbation of an exact solution); the adiabaticity measure along the solved histories, "
          "Q_max(a4') = Q_max(a4' = H) a4'/H, stays <= %s" % (g6(min(r8s)), g6(max(r8s)), g6(max(qs))))

    # ---------------- outputs
    OUT_MOMENTS.parent.mkdir(parents=True, exist_ok=True)
    OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO(newline="")
    wr = csv.writer(buf, lineterminator="\n")
    wr.writerow(["id", "N", "lambda_tag", "a4", "rho_bar", "p3_bar", "p_t_bar", "p8_bar", "mu1_rho", "mu1_p3", "mu1_p_t",
                 "mu1_p8", "mu_rho", "mu_p3", "mu_p_t", "mu_p8", "tip_share_rho", "alg_bar_rel", "alg_L2_rel",
                 "alg_pointwise_rel", "cons_fd_rel", "identity_rel", "Q_max"])
    for sid in sorted(states):
        s = states[sid]
        if s["zero"]:
            wr.writerow([sid, s["N"], s["lambda_tag"], e12(s["a4"]), "0", "0", "0", "0"] + ["zero source"] * 14 + [""])
            continue
        wr.writerow([sid, s["N"], s["lambda_tag"], e12(s["a4"]), e12(s["rho_bar"]), e12(s["p3_bar"]),
                     e12(s["p_t_bar"]), e12(s["p8_bar"]), e12(s["mu1_rho"]), e12(s["mu1_p3"]),
                     "identically zero" if s["mu1_p_t"] is None else e12(s["mu1_p_t"]), e12(s["mu1_p8"]),
                     e12(s["mu_rho"]), e12(s["mu_p3"]),
                     "identically zero" if s["mu_p_t"] is None else e12(s["mu_p_t"]), e12(s["mu_p8"]),
                     e12(s["tip_share_rho"]),
                     e12(s["alg_bar_rel"]), e12(s["alg_L2_rel"]), e12(s["alg_pointwise_rel"]), e12(s["cons_fd_rel"]),
                     e12(s["identity_rel"]), e12(s["Q_max"])])
    OUT_MOMENTS.write_bytes(buf.getvalue().encode("utf-8"))
    buf = io.StringIO(newline="")
    wr = csv.writer(buf, lineterminator="\n")
    wr.writerow(["gravity", "series", "case", "sigma0", "kappa", "Lambda", "event", "a4_end", "x4_end", "rate_end",
                 "rate_a00", "rate_a05", "rate_a10", "rate_a15", "rate_a20", "m2_a4_end", "m2_x4_end", "m2_rate_end",
                 "x8_moment_residual_max_rel", "algebraic_defect_max_rel", "adiabaticity_Q_max"])
    for c in cases:
        m2 = c["m2"]
        wr.writerow([c["gravity"], c["series"], c["label"], e12(c["sigma0"]), e12(c["kappa"]), e12(c["Lambda"]),
                     c["event"], e12(c["a_end"]), e12(c["x4_end"]), e12(c["A_end"])]
                    + [e12(math.sqrt(x)) if x is not None else "" for x in c["X_sl"]]
                    + ([e12(m2["a_end"]), e12(m2["x4_end"]), e12(m2["v_end"])] if m2 else ["", "", ""])
                    + [e12(c["r8_max"]) if c["r8_max"] is not None else "", e12(c["alg_max"]),
                       e12(c["q_max"]) if c["q_max"] is not None else ""])
    OUT_CASES.write_bytes(buf.getvalue().encode("utf-8"))

    n_pass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
    canon = {c["gravity"] + "/" + c["label"]: c for c in cases if c["series"] == "N136_lam0"}
    conclusions = [
        "EXACT: no recorded Kohn-Sham state is an admissible source of the author's metric. The states conserve "
        "energy-momentum along x8 (B2), so p3 + p_t - 2 p8 = p8_y/(3H) exactly (A6): the algebraic condition fails "
        "because every component depends on x8 (B4: at least a share %s of the energy density deviates from its "
        "hidden-direction average, L1 measure), and it fails also after averaging over the hidden direction (C1: O(1) "
        "defect). The coupled problem 'metric of SPEC section 1 + Kohn-Sham source' has no solution; nothing about a4 is "
        "DERIVED from it." % g6(min(mu1["rho"])),
        "APPROXIMATION (stated): keep the x4 moment and the x1 - x5 moment of the field equations (multiplied by "
        "sqrt|g| and integrated over the patch: exact necessary conditions), drop the x8 moment and the x1 + x5 - 2 x8 "
        "moment. This pair is the only consistent one (A4, C2, C3) and has the first integral P(a4'^2) + Lambda = "
        "-kappa rho_bar(a4) (Einstein: a4'^2 = a4'^2(0) - (kappa/3)(rho_bar(a4) - rho_bar(0))). Its error is the "
        "dropped residuals (C1, D7), which are O(1), not small.",
        "Within that approximation the Kohn-Sham source does NOT drive (start or select) exponential deflation of the "
        "extra times: the rate a4'(0) and its sign are initial data (the equations are invariant under x4 -> -x4, which "
        "turns deflation into inflation of the extra times, A3) and Lambda is fixed by them through the constraint. The "
        "gas modifies a deflation that is already there, by a bounded amount set by the energy it loses (D5): it "
        "accelerates it for kappa rho_bar > 0 (sigma0 > 0) and slows it for sigma0 < 0; for the canonical series "
        "N136_lam0 in Einstein gravity a4'(2)/a4'(0) = %s (sigma0 = 10), %s (sigma0 = 1), %s (sigma0 = -1). With "
        "Lambda = 0 (then sigma0 < 0 is forced) the deflation halts at a4* = %s (Einstein), %s (EGB), %s (cubic "
        "Lovelock), after which a4 decreases again (the extra times re-inflate, D3); in Einstein-Gauss-Bonnet with "
        "sigma0 > 0 the evolution reaches the branch point F = 0, where the evolution equation is not defined (D6). "
        "CONDITIONAL (not computed): if rho_bar tends to 0 as a4 grows beyond 2, Einstein gravity gives a4'^2 -> "
        "(-Lambda - 21 H^2)/3, i.e. late-time exponential deflation at a rate set by Lambda and H alone."
        % (g6(canon["einstein/sigma0 = 10"]["A_end"]), g6(canon["einstein/sigma0 = 1"]["A_end"]),
           g6(canon["einstein/sigma0 = -1"]["A_end"]), g6(canon["einstein/Lambda = 0"]["a_end"]),
           g6(canon["egb/Lambda = 0"]["a_end"]), g6(canon["lovelock3/Lambda = 0"]["a_end"])),
        "A source that does not change with a4 (the N = 8 interacting brane zero modes: p3_bar = p_t_bar) gives exactly "
        "the linear member a4 = A H x4 + a0 within the approximation (D4) - exponential deflation at the rate chosen "
        "initially, allowed but not selected; its x8 moment still fails (C1).",
        "Not computed (open): the source beyond a4 = 2 (no Kohn-Sham states there; any late-time statement is an "
        "extrapolation), thermal states (only the T = 0 ground states are used), the non-adiabatic problem, and a "
        "source with the hidden-direction profile the equations require (an x8-independent energy-momentum tensor, or "
        "a metric with x8-dependent warp functions that could carry the Kohn-Sham profile).",
    ]
    rep = {
        "report": rel(OUT_REPORT),
        "producer": rel(Path(__file__)),
        "spec": "Revision/SPEC.md sections 5 and 7: the a4 field equations with the Kohn-Sham energy-momentum tensor as "
                "the source; coordinates x1..x3 = 3-space, x4 = time, x5..x7 = the exponentially deflating extra times, "
                "x8 = hidden direction",
        "inputs": {rel(p): sha256(p) for p in (A4_JSON, KS_PARAMS, KS_INTEGRALS, KS_ADIABATIC, KS_HISTORY, KS_THEORY,
                                               WAVE1)},
        "inputProfiles": {"directory": rel(KS_PROFILES), "files": len(states),
                          "sha256OfSortedDigests": hashlib.sha256("".join(
                              sha256(p) for p in sorted(KS_PROFILES.glob("*.csv"))).encode()).hexdigest()},
        "units": "the solver's units H = m = 1; kappa in units m^-6 (H = m), Lambda in units H^2; sigma0 = kappa "
                 "rho_bar(a4 = 0)/H^2 is the dimensionless source strength",
        "assumptions": [
            "source = the T = 0 instantaneous Kohn-Sham ground states of Revision/kohn_sham (adiabatic family, no "
            "Fermi-level crossings) at the computed slices a4 = 0, 0.5, 1, 1.5, 2; rho_bar between slices by the cubic "
            "Hermite interpolant with the exact slopes -3 (p3_bar - p_t_bar)",
            "hidden-direction averages with the volume weight sqrt|g| = e^{6Hy} over the patch y in [-L, 0], L = 3 (the "
            "solver's tip cut-off)",
            "truncation: the x4 moment and the x1 - x5 moment are imposed, the x8 moment and the x1 + x5 - 2 x8 moment "
            "are not (their residuals are reported)",
            "sign convention sigmaT = +1 (a4-equations.json); kappa of either sign is examined (sigma0 > 0 and < 0)",
            "initial rate a4'(0) = H (the rate of the prescribed Kohn-Sham history, A = 1), a4(0) = 0; Lambda fixed by "
            "the constraint at a4 = 0 (or Lambda = 0 with sigma0 fixed instead)",
        ],
        "gravity": [{"name": g[0], "couplings": g[4], "P(X) at H = 1": polys[g[0]]["Pstr"],
                     "N(X) = sum alpha (E^x8_x8 - E^x4_x4) at H = 1": polys[g[0]]["Nstr"]} for g in GRAVITY],
        "conclusions": conclusions,
        "tolerances": {"integrals": TOL_INTEGRAL, "x8ConservationFD": TOL_CONS_FD, "integratedIdentity": TOL_IDENTITY,
                       "energyRelationSolver": TOL_ENERGY_SOLVER, "energyRelationSlices": TOL_ENERGY_SLICES,
                       "methods": TOL_METHODS},
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
    L = ["# The a4 field equations with the Kohn-Sham source (generated)", "",
         "Generated by `%s`; every number below is from this run (report `%s`, %d/%d checks pass)."
         % (rep["producer"], rep["report"], rep["summary"]["pass"], rep["summary"]["checks"]), "",
         "Coordinates: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra times (scale factor "
         "e^{-a4} sin^{1/6} z); x8 = hidden direction (Kohn-Sham coordinate y = ln(sin z)/(6H)).", "",
         "## Conclusions", ""]
    for c in rep["conclusions"]:
        L.append("* " + c)
    L += ["", "## Assumptions", ""] + ["* " + a for a in rep["assumptions"]]
    L += ["", "## Hidden-direction averages along the history (N = 136, lambda = 0)", "",
          "Proper densities in the solver's units (H = m = 1); mu1 = L1 and mu = L2 hidden-direction mismatch (check B4); "
          "defect = |p3_bar + p_t_bar - 2 p8_bar| / (|p3_bar| + |p_t_bar| + 2 |p8_bar|) (check C1).", "",
          "| a4 | rho_bar | p3_bar | p_t_bar | p8_bar | mu1_rho | mu1_p8 | mu_rho | mu_p8 | defect |", "| --- " * 10 + "|"]
    for a in slices:
        s = states["N136_lam0_a%02d" % int(round(10 * a))]
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            g6(a), g6(s["rho_bar"]), g6(s["p3_bar"]), g6(s["p_t_bar"]), g6(s["p8_bar"]), g6(s["mu1_rho"]),
            g6(s["mu1_p8"]), g6(s["mu_rho"]), g6(s["mu_p8"]), g6(s["alg_bar_rel"])))
    L += ["", "## Integrated cases (series N136_lam0, a4'(0) = H)", "",
          "sigma0 = kappa rho_bar(0)/H^2; Lambda from the constraint at a4 = 0; outcome: regular (through a4 = 2), "
          "turning_point (a4' = 0: the deflation halts, then the extra times re-inflate), branch_point (F(a4') = 0: the "
          "evolution equation is not defined there). Every series and case: `results/ks-source-a4-cases.csv`.", "",
          "| gravity | case | Lambda/H^2 | outcome | a4 reached | x4 elapsed (1/H) | a4'/H there |", "| --- " * 7 + "|"]
    for c in cases:
        if c["series"] != "N136_lam0":
            continue
        L.append("| %s | %s | %s | %s | %s | %s | %s |" % (c["gravity"], c["label"], g6(c["Lambda"]), c["event"],
                                                          g6(c["a_end"]), g6(c["x4_end"]), g6(c["A_end"])))
    L += ["", "## Checks", ""]
    for c in rep["checks"]:
        L.append("* **%s** %s: %s" % (c["verdict"], c["name"], c["detail"]))
    L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
