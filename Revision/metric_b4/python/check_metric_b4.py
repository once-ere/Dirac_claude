"""check_metric_b4.py - an independent sympy check of the primordial metric of 2026-10-14 (with b4[x4]).

Independent of the Wolfram computation (Revision/metric_b4/wolfram/verify_metric_b4.wls): it computes the
metric, Christoffel symbols, Riemann, Ricci, Einstein and the Lovelock tensors k = 1, 2, 3 from scratch
with sympy, contracts the generalized Kronecker delta by the SIGN OF THE PERMUTATION (not by a determinant,
as the Wolfram side does), and decides every equality exactly: after differentiation every quantity is a
rational function of the symbols

    H, S = Sin[6 H x0]^(1/3) (so Sin[6 H x0] = S^3), c = Cos[6 H x0], A0 = a4, A1 = a4', A2 = a4'', A3, B0 = b4,
    B1 = b4', B2 = b4'', B3, w1, w2, w3, Lambda (and E = e^{a4})

and a difference is zero exactly when its numerator vanishes modulo c^2 = 1 - S^6.  It then compares
  * with the Wolfram components Revision/metric_b4/results/metric-b4.json,
  * with the author's STORED outputs Revision/metric_b4/results/author-b4-outputs.json (Out[101], Out[119],
    Out[120], Out[124], Out[126], Out[127], Out[128], Out[129], Out[134], Out[135]),
  * at b4 = 1 with the earlier record (curvature.json and lovelock-tensors.json before 2026-10-14, frozen in
    Revision/metric_b4/reference_b4_1/ from commit e3e35fe),
and writes Revision/metric_b4/results/python-metric-b4-report.json (checks; UTF-8, LF, no time stamps).
Coordinates: the author's x0, x1, ..., x7 in his order (x0 = the hidden direction, index 0; xk = index k).  The frozen
b4 = 1 record is in the withdrawn labels x1..x8 (hidden x8 last) and is read through the map x8 -> x0, xk -> xk.
Exit code 0 if every check passes, 1 otherwise.  Usage (repository root):
    python Revision/metric_b4/python/check_metric_b4.py
"""
import itertools
import json
import os
import re
import sys
import time

import sympy as sp

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
RES = os.path.join(ROOT, "Revision", "metric_b4", "results")
T0 = time.time()

H = sp.Symbol("H", positive=True)
x0, x4 = sp.symbols("x0 x4", real=True)
a4 = sp.Function("a4")
b4 = sp.Function("b4")
X = [x0] + [sp.Symbol("x%d" % i, real=True) for i in (1, 2, 3)] + [x4] + [sp.Symbol("x%d" % i, real=True) for i in (5, 6, 7)]
S = sp.Symbol("S", positive=True)
c, A0, A1, A2, A3, B0, B1, B2, B3 = sp.symbols("c A0 A1 A2 A3 B0 B1 B2 B3")
w1, w2, w3, Lam = sp.symbols("w1 w2 w3 Lambda")
EA = sp.Symbol("EA", positive=True)  # e^{a4}
z = 6 * H * x0

# ---- the metric (the author's coordinates x0..x7, x0 = the hidden direction first) ---------------------------------
s13 = sp.sin(z) ** sp.Rational(1, 3)
gdiag = [sp.cot(z) ** 2] + [sp.exp(2 * a4(x4)) * s13] * 3 + [sp.Integer(-1)] + [-sp.exp(-2 * a4(x4)) * b4(x4) * s13] * 3
n = 8


def trig_subs(e):
    """Sin, Cos, Tan, Cot, Sec, Csc of z = 6 H x0 (and Sin, Cos of 2 z) -> S^3, c (exact)."""
    e = e.subs({sp.sin(2 * z): 2 * S ** 3 * c, sp.cos(2 * z): 1 - 2 * S ** 6})
    return e.subs({sp.cot(z): c / S ** 3, sp.tan(z): S ** 3 / c, sp.sec(z): 1 / c, sp.csc(z): 1 / S ** 3}).subs(
        {sp.sin(z): S ** 3, sp.cos(z): c})


def to_symbols(e):
    """Replace functions and trig by the polynomial symbols (exact)."""
    rep = {}
    for k, sym_ in ((3, A3), (2, A2), (1, A1)):
        rep[sp.Derivative(a4(x4), (x4, k))] = sym_
    for k, sym_ in ((3, B3), (2, B2), (1, B1)):
        rep[sp.Derivative(b4(x4), (x4, k))] = sym_
    e = e.subs(rep)
    e = e.subs({a4(x4): sp.log(EA), b4(x4): B0})
    e = trig_subs(e)
    return sp.powsimp(sp.expand_power_base(e, force=True), force=True)


def _rem(p):
    """remainder of a polynomial expression modulo c^2 - (1 - S^6), as a polynomial in c of degree <= 1"""
    return sp.rem(sp.Poly(sp.expand(p), c), sp.Poly(c ** 2 - 1 + S ** 6, c)).as_expr()


def reduce0(e):
    """Exact normal form: numerator and denominator reduced modulo c^2 = 1 - S^6, the denominator made free of
    c (multiplied through by its conjugate d0 - d1 c), then cancelled.  A quantity is zero iff this gives 0."""
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


def is_zero(e):
    return reduce0(e) == 0


checks = []


def check(name, ok, detail):
    checks.append({"name": name, "pass": bool(ok), "detail": detail})
    print("check_%s=%s" % (name, "PASS" if ok else "FAIL"), flush=True)


# ---- curvature from scratch ------------------------------------------------------------------------------------
g = [[gdiag[i] if i == j else sp.Integer(0) for j in range(n)] for i in range(n)]
gi = [[(1 / gdiag[i]) if i == j else sp.Integer(0) for j in range(n)] for i in range(n)]
# diagonal metric: Gamma^a_{bc} = 1/(2 g_aa) (d_b g_ac + d_c g_ab - d_a g_bc), only diagonal g
Gam = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for cc in range(n):
            v = 0
            if a == cc:
                v += sp.diff(gdiag[a], X[b])
            if a == b:
                v += sp.diff(gdiag[a], X[cc])
            if b == cc:
                v -= sp.diff(gdiag[b], X[a])
            if v != 0:
                Gam[a][b][cc] = v / (2 * gdiag[a])  # no simplify: it would introduce double angles
# R^a_{bcd} = d_c Gamma^a_{db} - d_d Gamma^a_{cb} + Gamma^a_{ce} Gamma^e_{db} - Gamma^a_{de} Gamma^e_{cb}
Rmix = {}
for a in range(n):
    for b in range(n):
        for cc in range(n):
            for d in range(cc + 1, n):
                v = sp.diff(Gam[a][d][b], X[cc]) - sp.diff(Gam[a][cc][b], X[d])
                v += sum(Gam[a][cc][e] * Gam[e][d][b] - Gam[a][d][e] * Gam[e][cc][b] for e in range(n))
                if v == 0:
                    continue
                vs = reduce0(to_symbols(v))
                if vs == 0:
                    continue
                # mixed R^{a e}_{cd} = g^{e e} R^a_{e cd} with e = b (diagonal inverse)
                m = reduce0(to_symbols(gi[b][b]) * vs)
                Rmix[(a, b, cc, d)] = m
                Rmix[(a, b, d, cc)] = -m
print("time_riemann=%.1f nonzero_mixed=%d" % (time.time() - T0, len(Rmix)), flush=True)
ricci = [[reduce0(sum(Rmix.get((a, cc, b, cc), 0) for cc in range(n))) for b in range(n)] for a in range(n)]
Rs = reduce0(sum(ricci[a][a] for a in range(n)))
G = [[reduce0(ricci[a][b] - (Rs / 2 if a == b else 0)) for b in range(n)] for a in range(n)]


# ---- Lovelock tensors by the sign of the permutation --------------------------------------------------------------
def perm_sign(lower, upper):
    """delta^{upper}_{lower} for index lists of distinct labels: sign of the permutation taking lower to upper,
    0 if they are not the same set (or have repeats)."""
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


entries = sorted(Rmix.items())
keys = [k for k, _ in entries]
vals = [v for _, v in entries]


def lovelock(k):
    E = [[sp.Integer(0)] * n for _ in range(n)]
    for h in range(n):
        for j in range(n):
            coeff = {}
            # choose k entries (ordered k-tuples), the upper pair (a, b) of R joins the LOWER row (j, j1, j2, ...)
            def rec(depth, low, up, chosen):
                if depth == k:
                    s = perm_sign(low, up)
                    if s:
                        t = tuple(sorted(chosen))
                        coeff[t] = coeff.get(t, 0) + s
                    return
                for idx, (a, b, cc, d) in enumerate(keys):
                    if a in low or b in low or cc in up or d in up:
                        continue
                    rec(depth + 1, low + [a, b], up + [cc, d], chosen + [idx])
            rec(0, [j], [h], [])
            tot = 0
            for t, cf in coeff.items():
                if cf:
                    tot += cf * sp.Mul(*[vals[i] for i in t])
            E[h][j] = reduce0(-tot / 2 ** (k + 1))
    return E


Ek = {}
for k in (1, 2, 3):
    Ek[k] = lovelock(k)
    print("time_lovelock%d=%.1f" % (k, time.time() - T0), flush=True)


# ---- parse Mathematica InputForm strings (the limited grammar of the outputs) --------------------------------------
def mma(s, author=False, withdrawn=False):
    """Evaluate a Mathematica list/expression string; lists become nested Python lists.  author: the notebook's
    names X0..X7 are the author's x0..x7; withdrawn: a string of the record in the withdrawn labels (x8 -> x0)."""
    t = s.strip()
    t = re.sub(r"^HoldComplete\[(.*)\]$", r"\1", t, flags=re.S)
    if author:
        for i in range(0, 8):
            t = t.replace("X%d" % i, "x%d" % i)
    if withdrawn:
        t = re.sub(r"x8(?![0-9])", "x0", t)
    t = re.sub(r"Derivative\[(\d)\]\[a4\]\[x4\]", lambda m: "A%s" % m.group(1), t)
    t = re.sub(r"Derivative\[(\d)\]\[b4\]\[x4\]", lambda m: "B%s" % m.group(1), t)
    t = t.replace("a4[x4]", "log(EA)").replace("b4[x4]", "B0")
    t = re.sub(r"Rational\[(-?\d+), (\d+)\]", r"(sp.Rational(\1,\2))", t)
    t = re.sub(r"\b(Sin|Cos|Tan|Cot|Sec|Csc)\[", lambda m: m.group(1).lower() + "(", t)
    t = t.replace("E^", "sp.E**")
    out, depth_stack = [], []
    for ch in t:  # '[' only remains as function-call bracket of sin(...) etc. closed by ']'
        if ch == "{":
            out.append("[")
        elif ch == "}":
            out.append("]")
        elif ch == "]":
            out.append(")")
        else:
            out.append(ch)
    t = "".join(out).replace("^", "**")
    t = re.sub(r"(?<![\w.])(\d+)(?![\w.])", r"sp.Integer(\1)", t)
    ns = {"sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot, "sec": sp.sec, "csc": sp.csc,
          "log": sp.log, "H": H, "x0": x0, "x4": x4, "EA": EA, "Lambda": Lam, "w1": w1, "w2": w2, "w3": w3,
          "A1": A1, "A2": A2, "A3": A3, "B0": B0, "B1": B1, "B2": B2, "B3": B3, "sp": sp}
    return eval(t, ns)  # noqa: S307 - our own files of a fixed grammar


def sym(e):
    return reduce0(to_symbols_plain(e))


def to_symbols_plain(e):
    e = trig_subs(sp.sympify(e))
    return sp.powsimp(sp.expand_power_base(e, force=True), force=True)


def author_to_revision(A):
    """A[p][q] = T_{a(p)}^{a(q)} (lower index first) -> M[h][j] = T^h_j (upper index first); both in the author's
    order x0..x7, so M[q][p] = A[p][q]."""
    M = [[sp.Integer(0)] * n for _ in range(n)]
    for p in range(n):
        for q in range(n):
            M[q][p] = A[p][q]
    return M


def same(M, N, label=""):
    bad = [(h, j) for h in range(n) for j in range(n) if not is_zero(M[h][j] - sym(N[h][j]))]
    if bad:
        print("  differing components %s: %s" % (label, bad[:10]), flush=True)
    return not bad


# ---- (1) against the Wolfram components ---------------------------------------------------------------------------
wol = json.load(open(os.path.join(RES, "metric-b4.json"), encoding="utf-8"))
lab = ["x%d" % i for i in range(0, 8)]  # the author's x0..x7
OLDLAB = ["x8"] + ["x%d" % i for i in range(1, 8)]  # their names in the withdrawn labels (the frozen b4 = 1 record)


def wmixed(key):
    d = wol[key]
    return [[mma(d.get(lab[h] + "," + lab[j], "0")) for j in range(n)] for h in range(n)]


check("ricci_scalar_equals_wolfram", is_zero(Rs - sym(mma(wol["ricciScalar"]))), "R (sympy) = R (Wolfram, metric-b4.json)")
check("einstein_equals_wolfram", same(G, wmixed("einsteinMixed")), "G^h_j (sympy) = Wolfram, 64 components")
for k in (1, 2, 3):
    check("lovelock%d_equals_wolfram" % k, same(Ek[k], wmixed("E%dMixed" % k)), "E_(%d) (sympy, permutation signs) = Wolfram (determinant)" % k)
check("riemann_nonzero_count_equals_wolfram", len(Rmix) == wol["riemannMixedNonzeroCount"],
      "nonzero R^{ab}_{cd}: sympy %d, Wolfram %d" % (len(Rmix), wol["riemannMixedNonzeroCount"]))

# ---- (2) against the author's stored outputs ----------------------------------------------------------------------
au = json.load(open(os.path.join(RES, "author-b4-outputs.json"), encoding="utf-8"))["cells"]
A101 = mma(au["Out[101]"], author=True)
check("metric_equals_author_Out101", all(is_zero(to_symbols(gdiag[p]) - sym(A101[p][p])) for p in range(8))
      and all(A101[p][q] == 0 for p in range(8) for q in range(8) if p != q),
      "the metric = the author's Out[101], component by component in his coordinates x0..x7")
check("ricci_scalar_equals_author_Out119", is_zero(Rs - sym(mma(au["Out[119]"], author=True))), "R = Out[119]")
check("einstein_equals_author_Out120", same(G, author_to_revision(mma(au["Out[120]"], author=True)), "Out120"), "G = Out[120]")
check("ricci_equals_author_Out124", same(ricci, author_to_revision(mma(au["Out[124]"], author=True)), "Out124"), "R^h_j = Out[124]")
for k, cell in ((1, "Out[126]"), (2, "Out[127]"), (3, "Out[128]")):
    check("lovelock%d_equals_author_%s" % (k, cell.replace("[", "").replace("]", "")),
          same(Ek[k], author_to_revision(mma(au[cell], author=True))), "E_(%d) = the author's allLovelock%d (%s)" % (k, k, cell))
vac = [[(-Lam if h == j else 0) + w1 * Ek[1][h][j] / H ** 2 + w2 * Ek[2][h][j] / H ** 4 + w3 * Ek[3][h][j] / H ** 6
        for j in range(n)] for h in range(n)]
check("vacuum_equations_equal_author_Out129", same(vac, author_to_revision(mma(au["Out[129]"], author=True))), "vacuum equations = Out[129]")
# the author's solution
subs_sol = {B0: 1, B1: 0, B2: 0, B3: 0, A1: H, A2: 0, A3: 0, w1: 1, w2: sp.Rational(1, 32)}
reduced = []
for h in range(n):
    for j in range(n):
        r_ = reduce0(reduce0(vac[h][j]).subs(subs_sol))
        if r_ != 0 and all(reduce0(r_ - q) != 0 for q in reduced):
            reduced.append(r_)
sol = sp.solve(reduced, [w3, Lam], dict=True)
check("author_solution_Out135", sol == [{w3: sp.Rational(1, 1152), Lam: 10}],
      "b4 = 1, a4 = H x4, w1 = 1, w2 = 1/32: reduced %s, solve %s (the author's Out[135]: w3 = 1/1152, Lambda = 10)" % (reduced, sol))

# ---- (3) b4 = 1 against the earlier record -------------------------------------------------------------------------
# the record before 2026-10-14 (metric without b4), frozen from commit e3e35fe (Revision/gkd_lovelock/results now has b4)
REF = os.path.join(ROOT, "Revision", "metric_b4", "reference_b4_1")
import hashlib  # noqa: E402
ref_sha = {n: hashlib.sha256(open(os.path.join(REF, n), "rb").read()).hexdigest() for n in ("curvature.json", "lovelock-tensors.json")}
check("reference_b4_1_files_are_the_earlier_record",
      ref_sha == {"curvature.json": "d5beb73a32244ea938ca61eac3573f72061c0e329b78f7506dd983881638763e",
                  "lovelock-tensors.json": "9278a0bf0da9ac7b2b22be5bb39e44073e821efb741514f42a43fa9cbc978567"},
      "reference_b4_1/curvature.json and lovelock-tensors.json are the gkd_lovelock results of commit e3e35fe (before b4)")
cur = json.load(open(os.path.join(REF, "curvature.json"), encoding="utf-8"))
lov = json.load(open(os.path.join(REF, "lovelock-tensors.json"), encoding="utf-8"))
one = {B0: 1, B1: 0, B2: 0, B3: 0}


def rec_mixed(d):
    return [[mma(d[OLDLAB[h] + "," + OLDLAB[j]]["mathematica"], withdrawn=True) for j in range(n)] for h in range(n)]


check("b4_one_ricci_scalar_equals_record", is_zero(Rs.subs(one) - sym(mma(cur["ricciScalar"], withdrawn=True))), "R at b4 = 1 = curvature.json")
check("b4_one_einstein_equals_record", all(is_zero(G[h][j].subs(one) - sym(x)) for h, row in enumerate(rec_mixed(cur["einsteinMixed"])) for j, x in enumerate(row)),
      "G at b4 = 1 = curvature.json einsteinMixed")
for k in (1, 2, 3):
    P = rec_mixed(lov["P%d_mixed_up_h_down_j" % k])
    check("b4_one_lovelock%d_equals_record" % k,
          all(is_zero(Ek[k][h][j].subs(one) + sym(P[h][j]) / 2 ** (k + 1)) for h in range(n) for j in range(n)),
          "E_(%d) at b4 = 1 = -P_(%d)/2^%d of lovelock-tensors.json" % (k, k, k + 1))

report = {"program": "Revision/metric_b4/python/check_metric_b4.py", "checks": checks, "checkCount": len(checks),
          "failedCount": sum(1 for x in checks if not x["pass"]), "sympyVersion": sp.__version__,
          "riemannMixedNonzero": len(Rmix)}
try:
    with open(os.path.join(RES, "python-metric-b4-report.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
except OSError as exc:
    print("ERROR: cannot write the report: %s" % exc)
    sys.exit(1)
print("time_total=%.1f" % (time.time() - T0))
print("checks=%d failed=%d" % (len(checks), report["failedCount"]))
print("metric_b4_python=%s" % ("OK" if report["failedCount"] == 0 else "FAILED"))
sys.exit(0 if report["failedCount"] == 0 else 1)
