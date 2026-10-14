"""check_b4_block.py - independent sympy check of the key "b4" of Revision/field_equations_a4/a4-equations.json.

The key "b4" (written by verify_field_equations_a4.wls) holds the field equations for a4[x4] and b4[x4] in the user's
metric of 2026-10-14 (g55 = g66 = g77 = -e^{-2 a4} b4 sin^{1/3} z).  This script recomputes, with sympy and code of
its own (no Wolfram output is used except the strings it checks):
  * the metric, Christoffel symbols, the mixed Riemann tensor and the Lovelock tensors E_(k) = -P_(k)/2^(k+1),
    k = 1, 2, 3 (P_(k) by the SIGN OF THE PERMUTATION over the nonzero R^{ab}_{cd}), and compares every component
    listed under b4.lovelockTensors;
  * the off-diagonal factor Q (sum_k alpha_k E_(k)^x4_x8 = cot z (b4'/b4) Q) and b4.generalSource.offDiagonalFactor_Q;
  * the identity sum_k alpha_k (E^x1_x1 + E^x5_x5 - 2 E^x8_x8) (b4.generalSource.identity_x1_plus_x5_minus_2x8);
  * nabla_mu T^mu_x4 and nabla_mu T^mu_x8 of a general source (b4.generalSource.conservation_x4/x8);
  * with the author's gamma matrices (Revision/algebra/gammas.json): gamma^mu Omega_mu = 3 H gamma^x8 + (3/4)(b4'/b4)
    gamma^x4, the condensate matrix A_b = -gamma^x4 (M - gamma^mu Omega_mu) = A_1 - (3/4)(b4'/b4) I16 and
    C A_b + A_b^T C = -(3/2)(b4'/b4) C.
Every equality is exact: functions are replaced by symbols and a difference is zero iff its numerator vanishes
modulo c^2 = 1 - S^6 (S = sin^{1/3} z, c = cos z).  Writes reports/python-b4-block.json; exit 0 iff all pass.
Usage (repository root): python Revision/field_equations_a4/python/check_b4_block.py
"""
import json
import re
import sys
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp

T0 = time.time()
REV = Path(__file__).resolve().parents[2]
EQ = REV / "field_equations_a4" / "a4-equations.json"
GAMMAS = REV / "algebra" / "gammas.json"
OUT = REV / "field_equations_a4" / "reports" / "python-b4-block.json"

H = sp.Symbol("H", positive=True)
x4, x8 = sp.symbols("x4 x8", real=True)
X = [sp.Symbol("x%d" % i, real=True) for i in (1, 2, 3)] + [x4] + [sp.Symbol("x%d" % i, real=True) for i in (5, 6, 7)] + [x8]
a4f, b4f = sp.Function("a4"), sp.Function("b4")
S = sp.Symbol("S", positive=True)
c, EA = sp.symbols("c EA", positive=True)
ad1, ad2, ad3, bb, bd1, bd2, bd3 = sp.symbols("ad1 ad2 ad3 bb bd1 bd2 bd3")
alpha1, alpha2, alpha3, Lam, kappa, uu, MM = sp.symbols("alpha1 alpha2 alpha3 Lam kappa uu MM")
z = 6 * H * x8
N = 8


def trig(e):
    e = e.subs({sp.sin(2 * z): 2 * S ** 3 * c, sp.cos(2 * z): 1 - 2 * S ** 6})
    e = e.subs({sp.cot(z): c / S ** 3, sp.tan(z): S ** 3 / c, sp.sec(z): 1 / c, sp.csc(z): 1 / S ** 3})
    return e.subs({sp.sin(z): S ** 3, sp.cos(z): c})


def sym(e):
    rep = {sp.Derivative(a4f(x4), (x4, 3)): ad3, sp.Derivative(a4f(x4), (x4, 2)): ad2, sp.Derivative(a4f(x4), x4): ad1,
           sp.Derivative(b4f(x4), (x4, 3)): bd3, sp.Derivative(b4f(x4), (x4, 2)): bd2, sp.Derivative(b4f(x4), x4): bd1}
    e = sp.sympify(e).subs(rep).subs({a4f(x4): sp.log(EA), b4f(x4): bb})
    return sp.powsimp(sp.expand_power_base(trig(e), force=True), force=True)


def _rem(p):
    return sp.rem(sp.Poly(sp.expand(p), c), sp.Poly(c ** 2 - 1 + S ** 6, c)).as_expr()


def red(e):
    """exact normal form modulo c^2 = 1 - S^6 (denominator made free of c)"""
    e = sp.together(sp.expand(e))
    num, den = sp.fraction(e)
    num = _rem(num)
    if num == 0:
        return sp.Integer(0)
    den = _rem(den)
    dp = sp.Poly(den, c)
    if dp.degree() == 1:
        d1, d0 = dp.all_coeffs()
        num = _rem(sp.expand(num * (d0 - d1 * c)))
        den = sp.expand(d0 ** 2 - d1 ** 2 * (1 - S ** 6))
    return sp.cancel(sp.expand(num) / den)


def zero(e):
    return red(e) == 0


checks = []


def check(name, ok, detail):
    checks.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print("%s %s" % ("PASS" if ok else "FAIL", name), flush=True)


# ---- geometry from scratch ----
s13 = sp.sin(z) ** sp.Rational(1, 3)
gd = [sp.exp(2 * a4f(x4)) * s13] * 3 + [sp.Integer(-1)] + [-sp.exp(-2 * a4f(x4)) * b4f(x4) * s13] * 3 + [sp.cot(z) ** 2]
Gam = [[[sp.Integer(0)] * N for _ in range(N)] for _ in range(N)]
for a in range(N):
    for b in range(N):
        for cc_ in range(N):
            v = 0
            if a == cc_:
                v += sp.diff(gd[a], X[b])
            if a == b:
                v += sp.diff(gd[a], X[cc_])
            if b == cc_:
                v -= sp.diff(gd[b], X[a])
            if v != 0:
                Gam[a][b][cc_] = v / (2 * gd[a])
Rmix = {}
for a in range(N):
    for b in range(N):
        for cc_ in range(N):
            for d in range(cc_ + 1, N):
                v = sp.diff(Gam[a][d][b], X[cc_]) - sp.diff(Gam[a][cc_][b], X[d])
                v += sum(Gam[a][cc_][e] * Gam[e][d][b] - Gam[a][d][e] * Gam[e][cc_][b] for e in range(N))
                if v == 0:
                    continue
                m = red(sym(v / gd[b]))
                if m != 0:
                    Rmix[(a, b, cc_, d)] = m
                    Rmix[(a, b, d, cc_)] = -m
keys = sorted(Rmix)
vals = [Rmix[k] for k in keys]


def perm_sign(lower, upper):
    if len(set(lower)) != len(lower) or set(lower) != set(upper):
        return 0
    pos = {v: i for i, v in enumerate(lower)}
    p = [pos[u] for u in upper]
    sign, seen = 1, [False] * len(p)
    for i in range(len(p)):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                L += 1
            if L % 2 == 0:
                sign = -sign
    return sign


def lovelock(k):
    E = [[sp.Integer(0)] * N for _ in range(N)]
    for h in range(N):
        for j in range(N):
            coeff = {}

            def rec(depth, low, up, chosen):
                if depth == k:
                    s_ = perm_sign(low, up)
                    if s_:
                        t = tuple(sorted(chosen))
                        coeff[t] = coeff.get(t, 0) + s_
                    return
                for idx, (a, b, cc_, d) in enumerate(keys):
                    if a in low or b in low or cc_ in up or d in up:
                        continue
                    rec(depth + 1, low + [a, b], up + [cc_, d], chosen + [idx])
            rec(0, [j], [h], [])
            tot = sum(cf * sp.Mul(*[vals[i] for i in t]) for t, cf in coeff.items() if cf)
            E[h][j] = red(-tot / 2 ** (k + 1))
    return E


E = {k: lovelock(k) for k in (1, 2, 3)}
print("time_lovelock=%.1f" % (time.time() - T0), flush=True)


# ---- the strings of a4-equations.json ----
def parse(s):
    t = s.replace("^", "**")
    loc = {"ad1": ad1, "ad2": ad2, "bb": bb, "bd1": bd1, "bd2": bd2, "cc": c / S ** 3, "H": H, "alpha1": alpha1,
           "alpha2": alpha2, "alpha3": alpha3, "Lam": Lam, "kappa": kappa, "uu": uu}
    for nm in ("rho", "p3", "pt", "p8", "q48", "q84"):
        loc[nm] = sp.Symbol(nm)
        loc["d4" + nm] = sp.Symbol("d4" + nm)
        loc["d8" + nm] = sp.Symbol("d8" + nm)
    return sp.sympify(t, locals=loc)


def lhs_rhs(s):
    l, r = s.split(" == ")
    return parse(l), parse(r)


data = json.loads(EQ.read_text(encoding="utf-8"))["b4"]
lab = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
idx = {"x1x1": (0, 0), "x4x4": (3, 3), "x5x5": (4, 4), "x8x8": (7, 7), "x4x8": (3, 7), "x8x4": (7, 3)}
ok = True
for k in (1, 2, 3):
    for key, (h, j) in idx.items():
        ok &= zero(E[k][h][j] - parse(data["lovelockTensors"]["E%d" % k][key]["input"]))
check("b4_lovelock_components", ok, "E_(1), E_(2), E_(3) (components x1x1, x4x4, x5x5, x8x8, x4x8, x8x4) of b4.lovelockTensors equal the sympy tensors (permutation signs)")
sumE = lambda h, j: alpha1 * E[1][h][j] + alpha2 * E[2][h][j] + alpha3 * E[3][h][j]  # noqa: E731
Qjson = parse(data["generalSource"]["offDiagonalFactor_Q"]["input"])
Qmine = red(sumE(3, 7) * bb / ((c / S ** 3) * bd1))
check("b4_offdiagonal_factor_Q", zero(Qmine.subs(bd1, uu * bb) - Qjson) and zero(sumE(7, 3) + (S ** 3 / c) * bd1 * Qmine / bb),
      "sum_k alpha_k E^x4_x8 = cot z (b4'/b4) Q and E^x8_x4 = -tan z (b4'/b4) Q with Q of the JSON")
check("b4_einstein_Q", zero(Qmine.subs({alpha1: 1, alpha2: 0, alpha3: 0}) - sp.Rational(3, 2) * H), "Einstein: Q = 3 H / 2")
idj = parse(data["generalSource"]["identity_x1_plus_x5_minus_2x8"]["input"])
idm = sumE(0, 0) + sumE(4, 4) - 2 * sumE(7, 7)
check("b4_identity", zero(idm - idj) and zero(idm.subs({alpha1: 1, alpha2: 0, alpha3: 0}) - (bd1 ** 2 / (4 * bb ** 2) + bd2 / (2 * bb))),
      "sum_k alpha_k (E^x1_x1 + E^x5_x5 - 2 E^x8_x8) equals the JSON and, for Einstein, (b4'/b4)^2/4 + b4''/(2 b4)")
for ky, nm in (("constraint_x4", (3, 3)), ("space_x1_eq_x2_eq_x3", (0, 0)), ("extraTime_x5_eq_x6_eq_x7", (4, 4)), ("hidden_x8", (7, 7))):
    l, r = lhs_rhs(data["generalSource"][ky]["input"])
    check("b4_equation_" + ky, zero(l - sumE(*nm) - Lam), ky + ": the left-hand side equals sum_k alpha_k E^mu_mu + Lambda")

# ---- conservation of a general source (sympy covariant divergence) ----
fs = {nm: sp.Function(nm)(x4, x8) for nm in ("rho", "p3", "pt", "p8", "q48", "q84")}
T = [[sp.Integer(0)] * N for _ in range(N)]
for i, nm in ((0, "p3"), (1, "p3"), (2, "p3"), (4, "pt"), (5, "pt"), (6, "pt"), (7, "p8")):
    T[i][i] = fs[nm]
T[3][3] = -fs["rho"]
T[3][7] = fs["q48"]
T[7][3] = fs["q84"]
div = []
for n_ in range(N):
    v = sum(sp.diff(T[m][n_], X[m]) for m in range(N))
    v += sum(Gam[m][m][l] * T[l][n_] for m in range(N) for l in range(N))
    v -= sum(Gam[l][m][n_] * T[m][l] for m in range(N) for l in range(N))
    div.append(v)
dsub = {}
for nm, f in fs.items():
    dsub[sp.Derivative(f, x4)] = sp.Symbol("d4" + nm)
    dsub[sp.Derivative(f, x8)] = sp.Symbol("d8" + nm)
    dsub[f] = sp.Symbol(nm)


def symT(e):
    return sym(sp.sympify(e).subs(dsub))


ok4 = zero(symT(div[3]) - parse(data["generalSource"]["conservation_x4"]["input"].split(" == ")[0]))
ok8 = zero(symT(div[7]) - parse(data["generalSource"]["conservation_x8"]["input"].split(" == ")[0]))
okz = all(zero(symT(div[i])) for i in (0, 1, 2, 4, 5, 6))
check("b4_conservation", ok4 and ok8 and okz, "nabla_mu T^mu_x4, nabla_mu T^mu_x8 equal the JSON; the other components vanish")


# ---- spinors with the author's T16 ----
def rat(x):
    if isinstance(x, bool):
        raise SystemExit("ERROR  bad fixture entry")
    if isinstance(x, int):
        return sp.Integer(x)
    f = Fraction(x)
    return sp.Rational(f.numerator, f.denominator)


fx = json.loads(GAMMAS.read_text(encoding="utf-8"))
gam = [sp.Matrix([[rat(v) for v in row] for row in m]) for m in fx["gamma"]]
Cm = sp.Matrix([[rat(v) for v in row] for row in fx["C"]])
eta = [1, 1, 1, -1, -1, -1, -1, 1]
vb = [sp.exp(a4f(x4)) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.Integer(1)] + [sp.exp(-a4f(x4)) * sp.sqrt(b4f(x4)) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.cot(z)]
# diagonal vielbein e^a_mu = vb[mu] delta; omega_mu ab = eta_aa e^a_nu (d_mu e_b^nu + Gamma^nu_{mu l} e_b^l)
Om = []
for mu in range(N):
    O = sp.zeros(16, 16)
    for a in range(N):
        for b in range(N):
            if a == b:
                continue
            w = vb[a] * (sp.diff(1 / vb[b], X[mu]) * (1 if a == b else 0) + Gam[a][mu][b] / vb[b])
            w = eta[a] * w
            if w != 0:
                Sab = (gam[a] * gam[b] - gam[b] * gam[a]) / 4
                O += sp.Rational(1, 2) * w * Sab
    Om.append(O)
gco = [gam[m] / vb[m] for m in range(N)]
G = sp.zeros(16, 16)
for mu in range(N):
    G += gco[mu] * Om[mu]
Gs = G.applyfunc(sym)
target = (3 * H * gam[7] + sp.Rational(3, 4) * (bd1 / bb) * gam[3])
check("b4_gravity_term", all(zero(v) for v in (Gs - target)), "gamma^mu Omega_mu = 3 H gamma^x8 + (3/4)(b4'/b4) gamma^x4 (author's T16)")
A_b = (-gco[3] * (MM * sp.eye(16) - G)).applyfunc(sym)
A_1 = A_b.subs({bd1: 0, bb: 1})
okA = all(zero(v) for v in (A_b - A_1 + sp.Rational(3, 4) * (bd1 / bb) * sp.eye(16)))
okC = all(zero(v) for v in (Cm * A_b + A_b.T * Cm + sp.Rational(3, 2) * (bd1 / bb) * Cm))
check("b4_condensate_matrix", okA and okC, "A_b = A_1 - (3/4)(b4'/b4) I16 and C A_b + A_b^T C = -(3/2)(b4'/b4) C")

failed = sum(1 for x in checks if x["verdict"] != "PASS")
rep = {"producer": "Revision/field_equations_a4/python/check_b4_block.py", "checks": checks, "checkCount": len(checks),
       "failedCount": failed, "verdict": "PASS" if failed == 0 else "FAIL", "sympyVersion": sp.__version__}
try:
    OUT.write_text(json.dumps(rep, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
except OSError as exc:
    print("ERROR  cannot write %s: %s" % (OUT, exc))
    sys.exit(1)
print("checks: %d, failed: %d, time %.1f s" % (len(checks), failed, time.time() - T0))
sys.exit(0 if failed == 0 else 1)
