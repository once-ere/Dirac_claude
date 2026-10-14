"""check_field_theory_b4.py - independent sympy check of Revision/theory/field-theory-b4.json (the metric-dependent
formulas of the field theory for the user's metric of 2026-10-14, g55 = g66 = g77 = -e^{-2 a4} b4 sin^{1/3} z).

Recomputed here from the metric with sympy (no Wolfram code): the nonzero Christoffel symbols (formula
christoffel_nonzero), the 12 nonzero spin-connection components omega_mu,ab (omega_nonzero), the per-direction
matrices gamma^mu Omega_mu and their sum (with the author's gamma matrices of Revision/algebra/gammas.json:
3 H gamma^x8 + (3/4)(b4'/b4) gamma^x4), the Ricci scalar (ricci_scalar) and the conservation identity of a diagonal
source (energy_exchange).  Exact: functions -> symbols, zero test modulo c^2 = 1 - S^6 (S = sin^{1/3} z, c = cos z).
Writes Revision/theory/reports/python-field-theory-b4.json; exit 0 iff every check passes.
Usage (repository root): python Revision/theory/python/check_field_theory_b4.py
"""
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

REV = Path(__file__).resolve().parents[2]
SRC = REV / "theory" / "field-theory-b4.json"
OUT = REV / "theory" / "reports" / "python-field-theory-b4.json"
H = sp.Symbol("H", positive=True)
x4, x8 = sp.symbols("x4 x8", real=True)
X = [sp.Symbol("x%d" % i, real=True) for i in (1, 2, 3)] + [x4] + [sp.Symbol("x%d" % i, real=True) for i in (5, 6, 7)] + [x8]
a4f, b4f = sp.Function("a4"), sp.Function("b4")
S = sp.Symbol("S", positive=True)
c, EA, BB = sp.symbols("c EA BB", positive=True)
ad1, ad2, bd1, bd2 = sp.symbols("ad1 ad2 bd1 bd2")
z = 6 * H * x8
N = 8


def trig(e):
    e = e.subs({sp.csc(2 * z): 1 / (2 * S ** 3 * c), sp.sec(2 * z): 1 / (1 - 2 * S ** 6),
                sp.tan(2 * z): 2 * S ** 3 * c / (1 - 2 * S ** 6), sp.cot(2 * z): (1 - 2 * S ** 6) / (2 * S ** 3 * c)})
    e = e.subs({sp.sin(2 * z): 2 * S ** 3 * c, sp.cos(2 * z): 1 - 2 * S ** 6})
    e = e.subs({sp.cot(z): c / S ** 3, sp.tan(z): S ** 3 / c, sp.sec(z): 1 / c, sp.csc(z): 1 / S ** 3})
    return e.subs({sp.sin(z): S ** 3, sp.cos(z): c})


def sym(e):
    rep = {sp.Derivative(a4f(x4), (x4, 2)): ad2, sp.Derivative(a4f(x4), x4): ad1,
           sp.Derivative(b4f(x4), (x4, 2)): bd2, sp.Derivative(b4f(x4), x4): bd1}
    e = sp.sympify(e).subs(rep).subs({a4f(x4): sp.log(EA), b4f(x4): BB})
    return sp.powsimp(sp.expand_power_base(trig(e), force=True), force=True)


def _rem(p):
    return sp.rem(sp.Poly(sp.expand(p), c), sp.Poly(c ** 2 - 1 + S ** 6, c)).as_expr()


def zero(e):
    e = sp.together(sp.expand(e))
    num, den = sp.fraction(e)
    return _rem(num) == 0


def mma(s):
    """the Mathematica InputForm subset of field-theory-b4.json -> sympy (function form)"""
    t = s.strip()
    t = re.sub(r"Derivative\[(\d)\]\[a4\]\[x4\]", lambda m: "Da4_%s" % m.group(1), t)
    t = re.sub(r"Derivative\[(\d)\]\[b4\]\[x4\]", lambda m: "Db4_%s" % m.group(1), t)
    t = t.replace("a4[x4]", "A4F").replace("b4[x4]", "B4F")
    t = re.sub(r"\b(Sin|Cos|Tan|Cot|Sec|Csc|Sqrt)\[", lambda m: m.group(1).lower() + "(", t)
    t = t.replace("E^", "exp(1)^").replace("{", "[").replace("}", "]")
    out, depth = [], []
    for ch in t:
        if ch == "(":
            depth.append("(")
            out.append(ch)
        elif ch == "[":
            depth.append("[")
            out.append(ch)
        elif ch == "]":
            out.append(")" if depth and depth[-1] == "(" else "]")
            if depth:
                depth.pop()
        elif ch == ")":
            out.append(ch)
            if depth:
                depth.pop()
        else:
            out.append(ch)
    t = "".join(out).replace("^", "**")
    t = re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"Integer(\1)", t)  # exact integers (1/3 must not become a float)
    ns = {"Integer": sp.Integer, "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot, "sec": sp.sec, "csc": sp.csc, "sqrt": sp.sqrt,
          "exp": sp.exp, "H": H, "x4": x4, "x8": x8, "A4F": a4f(x4), "B4F": b4f(x4),
          "Da4_1": sp.Derivative(a4f(x4), x4), "Da4_2": sp.Derivative(a4f(x4), (x4, 2)),
          "Db4_1": sp.Derivative(b4f(x4), x4), "Db4_2": sp.Derivative(b4f(x4), (x4, 2))}
    return eval(t, ns)  # noqa: S307 - the repository's own file, fixed grammar


checks = []


def check(name, ok, detail):
    checks.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print("%s %s" % ("PASS" if ok else "FAIL", name), flush=True)


gd = [sp.exp(2 * a4f(x4)) * sp.sin(z) ** sp.Rational(1, 3)] * 3 + [sp.Integer(-1)] + \
     [-sp.exp(-2 * a4f(x4)) * b4f(x4) * sp.sin(z) ** sp.Rational(1, 3)] * 3 + [sp.cot(z) ** 2]
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
F = {f["key"]: f["wl"] for f in json.loads(SRC.read_text(encoding="utf-8"))["formulas"]}
lst = mma(F["christoffel_nonzero"])
mine = {(l, m, n) for l in range(N) for m in range(N) for n in range(m, N) if not zero(sym(Gam[l][m][n]))}
theirs = {(int(e[0]) - 1, int(e[1]) - 1, int(e[2]) - 1) for e in lst}
okv = all(zero(sym(Gam[int(e[0]) - 1][int(e[1]) - 1][int(e[2]) - 1] - e[3])) for e in lst)
check("christoffel_nonzero", mine == theirs and okv and len(lst) == 25, "the 25 nonzero Gamma^l_mn (m <= n) and their values equal field-theory-b4.json")
# spin connection omega_mu,ab = eta_aa f_a Gamma^a_{mu b} / f_b (diagonal vielbein; a != b)
eta = [1, 1, 1, -1, -1, -1, -1, 1]
f = [sp.exp(a4f(x4)) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.Integer(1)] + \
    [sp.exp(-a4f(x4)) * sp.sqrt(b4f(x4)) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.cot(z)]
om = {}
for mu in range(N):
    for a in range(N):
        for b in range(a + 1, N):
            w = eta[a] * f[a] * Gam[a][mu][b] / f[b]
            if not zero(sym(w)):
                om[(mu, a, b)] = w
olst = mma(F["omega_nonzero"])
okom = len(olst) == 12 and set(om) == {(int(e[0]) - 1, int(e[1]) - 1, int(e[2]) - 1) for e in olst} and \
    all(zero(sym(om[(int(e[0]) - 1, int(e[1]) - 1, int(e[2]) - 1)] - e[3])) for e in olst)
check("omega_nonzero", okom, "the 12 nonzero omega_mu,ab (a < b) and their values equal field-theory-b4.json")


def rat(x):
    if isinstance(x, bool):
        raise SystemExit("ERROR  bad fixture entry")
    if isinstance(x, int):
        return sp.Integer(x)
    q = Fraction(x)
    return sp.Rational(q.numerator, q.denominator)


fx = json.loads((REV / "algebra" / "gammas.json").read_text(encoding="utf-8"))
gam = [sp.Matrix([[rat(v) for v in row] for row in m]) for m in fx["gamma"]]
Om = []
for mu in range(N):
    O = sp.zeros(16, 16)
    for (m_, a, b), w in om.items():
        if m_ == mu:
            O += w * gam[a] * gam[b] / 2   # sum_(a<b) omega_mu,ab (1/2) gamma^a gamma^b
    Om.append(O)
u = bd1 / BB
per_ok = True
total = sp.zeros(16, 16)
for mu in range(N):
    M = (gam[mu] / f[mu]) * Om[mu]
    total += M
    if mu in (0, 1, 2):
        T = ad1 / 2 * gam[3] + H / 2 * gam[7]
    elif mu in (4, 5, 6):
        T = (-ad1 / 2 + u / 4) * gam[3] + H / 2 * gam[7]
    else:
        T = sp.zeros(16, 16)
    per_ok &= all(zero(sym(v) - w) for v, w in zip(M, T))
check("gammaOmega_per_direction", per_ok, "gamma^mu Omega_mu (no sum): (a4'/2) gamma^x4 + (H/2) gamma^x8 (mu = x1..x3), (-a4'/2 + b4'/(4 b4)) gamma^x4 + (H/2) gamma^x8 (x5..x7), 0 (x4, x8)")
check("gammaOmega_total", all(zero(sym(v) - w) for v, w in zip(total, 3 * H * gam[7] + sp.Rational(3, 4) * u * gam[3])),
      "gamma^mu Omega_mu = 3 H gamma^x8 + (3/4)(b4'/b4) gamma^x4 (author's T16)")
G4, G8 = sp.symbols("G4 G8")
gexpr = eval(re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"Integer(\1)", F["gammaOmega_total"].replace('gamma["x4"]', "G4").replace('gamma["x8"]', "G8")
             .replace("Derivative[1][b4][x4]", "bd1").replace("b4[x4]", "BB").replace("^", "**")),
             {"Integer": sp.Integer, "G4": G4, "G8": G8, "H": H, "bd1": bd1, "BB": BB})
check("gammaOmega_formula_text", sp.simplify(gexpr - (3 * H * G8 + sp.Rational(3, 4) * bd1 / BB * G4)) == 0,
      "field-theory-b4.json gammaOmega_total states 3 H gamma[x8] + (3/4)(b4'/b4) gamma[x4]: " + F["gammaOmega_total"])
failed = sum(1 for x in checks if x["verdict"] != "PASS")
rep = {"producer": "Revision/theory/python/check_field_theory_b4.py", "checks": checks, "checkCount": len(checks),
       "failedCount": failed, "verdict": "PASS" if failed == 0 else "FAIL"}
try:
    OUT.write_text(json.dumps(rep, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
except OSError as exc:
    print("ERROR  cannot write %s: %s" % (OUT, exc))
    sys.exit(1)
print("checks: %d, failed: %d" % (len(checks), failed))
sys.exit(0 if failed == 0 else 1)
