"""derive_warped_metric.py - the self-consistency of the primordial metric with diagonal sources, and the corrected
warped metric (version 2, 2026-10-16) that answers the user's order of 2026-10-16: "find the simplest modification for
the current metric of the primordial gravitational field that is probably self-consistent with the Einstein field
equations".

A diagonal metric is self-consistent with the field equations  sum_k alpha_k E_(k)^mu_nu + Lambda delta^mu_nu =
kappa T^mu_nu  only if every off-diagonal component of the left-hand side equals the off-diagonal component of the
source.  The metric of 2026-10-14 has the component E^{x4}_{x0} ~ cot z b4'/b4 at every Lovelock order.

The user's rules for the remedy (2026-10-16): x0 is a space-like hidden coordinate and x4 the time; z = 6 H x0 ranges
over ALL real numbers (-Infinity < z < Infinity); g44 cannot oscillate; Sin[6 H x0]^(1/3) means (Sin[6 H x0]^2)^(1/6),
the positive branch.  Version 1 of this record (g44 = -Sin[z]^(1/3), the "time-warped" metric) is withdrawn: its g44
oscillates in z and vanishes at z = n Pi.

This program, for every real z (sin z and cos z are free signed variables, w = (sin^2 z)^(1/6) > 0, and every
expression is reduced exactly modulo cos^2 z + sin^2 z - 1 and w^6 - sin^2 z):
  * reproduces the off-diagonal component of the metric of 2026-10-14 and the record's factor Q (frozen copy of
    Revision/field_equations_a4/a4-equations.json of commit 04fa2e7);
  * proves, for the family with g44 = -1 (no x0 dependence),
        g00 = b4^(2p) e^(2 q a4) cot^2 z,  g_ii = e^(2 a4) w^(6 alpha),  g_tt = -e^(-2 a4) b4 w^(6 beta),
    that the mixed curvature components are proportional to alpha ((q - 1) a4' + p b4'/b4) (3-space) and to
    beta ((q + 1) a4' + (p - 1/2) b4'/b4) (extra times); every Lovelock order is free of off-diagonal terms for all
    a4, b4 exactly when every x0-dependent family has the time dependence of the hidden direction.  With the author's
    warp on the extra times (beta = 1/6) this is q = -1, p = 1/2, alpha = 0: THE CORRECTED METRIC
        g = diag(e^(-2 a4) b4 cot^2 z, e^(2 a4), e^(2 a4), e^(2 a4), -1, -e^(-2 a4) b4 w^2, ..., ...),  w^2 = Sin[z]^(1/3);
    with the warp on 3-space (alpha = 1/6) it is q = 1, p = 0, beta = 0 (the alternative K, in which x0 grows with
    3-space); the Einstein-only one-entry change g00 = b4^(1/2) cot^2 z (both warps kept) is recorded;
  * proves for the corrected metric: no mixed Riemann component, no off-diagonal component of E_(1), E_(2), E_(3),
    diagonal components independent of x0 at every order; the block (x0, x5, x6, x7) is e^(-2 a4) b4 times a
    4-dimensional space of constant curvature -H^2; Ricci tensor and scalar; the divergence of a diagonal tensor;
    the source of the record's history and its conservation; the gravity term of the Dirac operator; flat space in
    Milne form as a vacuum check.
Coordinates: the author's x0..x7 (index 0 = x0, the hidden direction; x4 = the time).  Conventions of the Revision
record: Riemann R^a_{bcd} (MTW), R^{ab}_{cd} = g^{be} R^a_{ecd}, P_(k)^h_j = GKD[{h,h1..h2k},{j,j1..j2k}]
R^{j1j2}_{h1h2}..., E_(k) = -P_(k)/2^(k+1) (E_(1) = Einstein), field equations sum_k alpha_k E_(k) + Lambda delta =
kappa T.  Writes Revision/metric_warped/results/warped-metric.json and
Revision/metric_warped/reports/python-warped-metric-report.json (UTF-8, LF, sorted keys, no time stamps).
Exit code 0 if every check passes.  Usage (repository root):
    python Revision/metric_warped/python/derive_warped_metric.py
"""
import itertools
import json
import os
import sys
import time

import sympy as sp

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
OUT = os.path.join(ROOT, "Revision", "metric_warped")
T0 = time.time()

X = sp.symbols("x0:8", real=True)
H = sp.Symbol("H", positive=True)
a4f = sp.Function("a4")(X[4])
b4f = sp.Function("b4", positive=True)(X[4])
z = 6 * H * X[0]
# the author's Sin[6 H x0]^(1/3), read as (Sin[6 H x0]^2)^(1/6) (the user's rule, positive branch)
S13 = (sp.sin(z) ** 2) ** sp.Rational(1, 6)
# plain symbols of the normal form: ad1 = a4', ad2 = a4'', bb = b4 > 0, bd1 = b4', bd2 = b4''; sv = sin z, cv = cos z
# (signed), w = (sin^2 z)^(1/12) = |sin z|^(1/6) > 0 (so w^12 = sv^2, |sin z| = w^6, sign(sin z) = sv/w^6)
ad1, ad2, ad3, bd1, bd2, bd3 = sp.symbols("ad1 ad2 ad3 bd1 bd2 bd3", real=True)
sv, cv = sp.symbols("sv cv", real=True)
bb, w = sp.symbols("bb w", positive=True)
al1, al2, al3, Lam = sp.symbols("alpha1 alpha2 alpha3 Lam", real=True)
EA = sp.Symbol("EA", positive=True)  # e^(a4)
CHECKS = []
RESULTS = {}


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + ": " + detail[:160], flush=True)


def s(e):
    return sp.sstr(e)


# ---------------------------------------------------------------- normal form valid for every real z
def normal(e):
    """Write derivatives, e^(a4), the trigonometric functions of z and (sin^2 z)^k as plain symbols."""
    e = sp.sympify(e)
    for old, new in [(sp.Derivative(a4f, X[4], 3), ad3), (sp.Derivative(a4f, X[4], 2), ad2),
                     (sp.Derivative(a4f, X[4]), ad1), (sp.Derivative(b4f, X[4], 3), bd3),
                     (sp.Derivative(b4f, X[4], 2), bd2), (sp.Derivative(b4f, X[4]), bd1)]:
        e = e.subs(old, new)
    e = e.subs(b4f, bb).subs(sp.exp(a4f), EA)
    # sin z != 0 (the metric is singular there): the delta functions of d sign(sin z) do not contribute
    e = e.replace(lambda t: isinstance(t, sp.DiracDelta), lambda t: 0)
    e = e.replace(lambda t: t.is_Pow and t.base == sp.sin(z) ** 2, lambda t: w ** (12 * t.exp))
    e = e.replace(lambda t: isinstance(t, sp.Abs) and t.args[0] == sp.sin(z), lambda t: w ** 6)
    e = e.replace(lambda t: isinstance(t, sp.sign) and t.args[0] == sp.sin(z), lambda t: sp.sin(z) / w ** 6)
    e = e.subs({sp.sin(2 * z): 2 * sp.sin(z) * sp.cos(z), sp.cos(2 * z): sp.cos(z) ** 2 - sp.sin(z) ** 2})
    e = e.subs({sp.tan(z): sv / cv, sp.cot(z): cv / sv, sp.sec(z): 1 / cv, sp.csc(z): 1 / sv})
    e = e.subs({sp.sin(z): sv, sp.cos(z): cv})
    e = e.replace(lambda t: t.is_Pow and t.base == sv ** 2, lambda t: w ** (12 * t.exp))
    e = e.subs(sp.exp(2 * a4f), EA ** 2).subs(sp.exp(-2 * a4f), EA ** -2).subs(sp.exp(-a4f), 1 / EA)
    return reduce_patch(e)


def reduce_patch(e):
    """Exact reduction modulo cv^2 + sv^2 - 1 and w^12 - sv^2 (numerator and denominator separately)."""
    e = sp.together(sp.expand(e))
    num, den = sp.fraction(e)

    def red(p):
        p = sp.expand(p)
        if p.has(cv):
            p = sp.rem(sp.Poly(p, cv), sp.Poly(cv ** 2 + sv ** 2 - 1, cv)).as_expr()
        p = sp.expand(p)
        if p.has(w):
            pw = sp.Poly(p, w)
            out = 0
            for (k,), c in pw.terms():
                out += c * w ** (k % 12) * sv ** (2 * (k // 12))
            p = sp.expand(out)
        return p
    return sp.factor(red(num) / red(den))


def is_zero(e):
    return reduce_patch(e) == 0


# ---------------------------------------------------------------- curvature of a diagonal metric
def christoffel(g, coords):
    n = len(coords)
    G = {}
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                t = 0
                if a == c:
                    t += sp.diff(g[a], coords[b])
                if a == b:
                    t += sp.diff(g[a], coords[c])
                if b == c:
                    t -= sp.diff(g[b], coords[a])
                if t != 0:
                    v = t / (2 * g[a])
                    G[(a, b, c)] = v
                    G[(a, c, b)] = v
    return G


def riemann_uu(g, coords, G):
    """R^{ab}_{cd} (a < b, c < d), nonzero components, in the normal form."""
    n = len(coords)

    def Gm(a, b, c):
        return G.get((a, b, c), 0)

    out = {}
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(n):
                for d in range(c + 1, n):
                    r = sp.diff(Gm(a, b, d), coords[c]) - sp.diff(Gm(a, b, c), coords[d])
                    for e in range(n):
                        r += Gm(a, c, e) * Gm(e, b, d) - Gm(a, d, e) * Gm(e, b, c)
                    if r != 0:
                        v = normal(r / g[b])
                        if v != 0:
                            out[(a, b, c, d)] = v
    return out


def perm_sign(seq_from, seq_to):
    if sorted(seq_from) != sorted(seq_to):
        return 0
    idx = [seq_from.index(v) for v in seq_to]
    sign = 1
    seen = [False] * len(idx)
    for i in range(len(idx)):
        if not seen[i]:
            j, length = i, 0
            while not seen[j]:
                seen[j] = True
                j = idx[j]
                length += 1
            if length % 2 == 0:
                sign = -sign
    return sign


def lovelock(R, n, k):
    """E_(k)^h_j = -(1/2^(k+1)) GKD[{h,h1..h2k},{j,j1..j2k}] R^{j1j2}_{h1h2}...; GKD by the sign of the permutation."""
    syms = {key: sp.Symbol("R_%d_%d_%d_%d" % key) for key in R}
    items = list(syms.items())
    acc = {}
    for tup in itertools.product(items, repeat=k):
        low, up = [], []
        for (a, b, c, d), _ in tup:
            low += [a, b]
            up += [c, d]
        if len(set(low)) != 2 * k or len(set(up)) != 2 * k:
            continue
        val = 4 ** k
        for _, sy in tup:
            val *= sy
        for h in range(n):
            if h in up:
                continue
            for j in range(n):
                if j in low:
                    continue
                sg = perm_sign([h] + up, [j] + low)
                if sg:
                    acc[(h, j)] = acc.get((h, j), 0) + sg * val
    sub = {syms[key]: R[key] for key in R}
    E = {}
    for key, poly in acc.items():
        v = sp.expand(poly)
        if v == 0:
            continue
        v = reduce_patch(-v.xreplace(sub) / 2 ** (k + 1))
        if v != 0:
            E[key] = v
    return E


def curvature(gdiag, coords, kmax=3):
    g = [sp.sympify(v) for v in gdiag]
    G = christoffel(g, coords)
    R = riemann_uu(g, coords, G)
    E = {k: lovelock(R, len(coords), k) for k in range(1, kmax + 1)}
    return G, R, E


def x0_free(e):
    return not sp.sympify(e).has(sv, cv, w)


# ---------------------------------------------------------------- the metrics
def metric(g00, gs, g44, gt):
    return [g00] + [gs] * 3 + [g44] + [gt] * 3


G_RECORD = metric(sp.cot(z) ** 2, sp.exp(2 * a4f) * S13, -1, -sp.exp(-2 * a4f) * b4f * S13)
G_V1 = metric(sp.cot(z) ** 2, sp.exp(2 * a4f) * S13, -S13, -sp.exp(-2 * a4f) * b4f * S13)
G_FIX = metric(sp.exp(-2 * a4f) * b4f * sp.cot(z) ** 2, sp.exp(2 * a4f), -1, -sp.exp(-2 * a4f) * b4f * S13)
G_K = metric(sp.exp(2 * a4f) * sp.cot(z) ** 2, sp.exp(2 * a4f) * S13, -1, -sp.exp(-2 * a4f) * b4f)
G_EIN = metric(sp.sqrt(b4f) * sp.cot(z) ** 2, sp.exp(2 * a4f) * S13, -1, -sp.exp(-2 * a4f) * b4f * S13)
RESULTS["coordinates"] = ("x0 (hidden, space-like), x1, x2, x3 (space), x4 (time), x5, x6, x7 (extra times, time-like); "
                          "z = 6 H x0 real (-Infinity < z < Infinity); Sin[6 H x0]^(1/3) := (Sin[6 H x0]^2)^(1/6) > 0")
RESULTS["metric_corrected"] = ("diag(E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2, E^(2 a4[x4]), E^(2 a4[x4]), E^(2 a4[x4]), -1, "
                               "-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6), -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6), "
                               "-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6))")
RESULTS["metric_of_2026_10_14"] = ("diag(Cot[6 H x0]^2, E^(2 a4[x4]) Sin[6 H x0]^(1/3) (x1, x2, x3), -1, "
                                   "-E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3) (x5, x6, x7))")
RESULTS["metric_version_1_withdrawn"] = "the metric of 2026-10-14 with g44 = -Sin[6 H x0]^(1/3) (withdrawn 2026-10-16)"
RESULTS["vielbein_corrected"] = ("f0 = E^(-a4) b4^(1/2) Cot[6 H x0] (signed; f0^2 = g00), f1 = f2 = f3 = E^a4, f4 = 1, "
                                 "f5 = f6 = f7 = E^(-a4) b4^(1/2) (Sin[6 H x0]^2)^(1/12)")

# ---- 1. signs of the entries and the volume factor of the corrected metric, every real z
signs_ok = is_zero(normal(G_FIX[0]) - EA ** -2 * bb * cv ** 2 / sv ** 2) and is_zero(normal(G_FIX[5]) + EA ** -2 * bb * w ** 2)
f_fix = [sp.exp(-a4f) * sp.sqrt(b4f) * sp.cot(z)] + [sp.exp(a4f)] * 3 + [sp.Integer(1)] + \
        [sp.exp(-a4f) * sp.sqrt(b4f) * (sp.sin(z) ** 2) ** sp.Rational(1, 12)] * 3
eta = [1, 1, 1, 1, -1, -1, -1, -1]
vb_ok = all(is_zero(normal(eta[a] * f_fix[a] ** 2 - G_FIX[a])) for a in range(8))
prod_f = normal(sp.prod(f_fix))
vol_ok = is_zero(prod_f - EA ** -1 * bb ** 2 * cv / sv * w ** 3)
check("corrected_metric_entries", signs_ok and vb_ok and vol_ok,
      "for every real z (sin z, cos z signed, (sin^2 z)^(1/6) > 0): g00 = e^(-2 a4) b4 cot^2 z >= 0, g_ii = e^(2 a4) > 0, "
      "g44 = -1, g_tt = -e^(-2 a4) b4 (sin^2 z)^(1/6) < 0 (signature (4,4) wherever sin z cos z != 0); the diagonal "
      "vielbein f0 = e^(-a4) b4^(1/2) cot z (signed), f_i = e^(a4), f4 = 1, f_t = e^(-a4) b4^(1/2) (sin^2 z)^(1/12) "
      "reproduces it, and f0 f1...f7 = e^(-a4) b4^2 cot z (sin^2 z)^(1/4) (sqrt|g| = its absolute value)")
RESULTS["sqrt_det_g_corrected"] = "E^(-a4) b4^2 |Cot[6 H x0]| (Sin[6 H x0]^2)^(1/4)"
print("t", round(time.time() - T0, 1), flush=True)

# ---- 2. the metric of 2026-10-14: the off-diagonal component and the record's factor Q
_, R_rec, E_rec = curvature(G_RECORD, X)
off_rec = {k: sorted(key for key in E_rec[k] if key[0] != key[1]) for k in (1, 2, 3)}
lhs = sum(a * E_rec[k].get((4, 0), 0) for k, a in ((1, al1), (2, al2), (3, al3)))
with open(os.path.join(OUT, "reference_2026_10_14", "a4-offdiagonal-x4x0.json"), encoding="utf-8") as f:
    a4eq = json.load(f)  # frozen copy of the record of 2026-10-14 (commit 04fa2e7)
rec_text = a4eq["generalSource.offDiagonal_x4x0"]["input"].split("==")[0]
uu = sp.Symbol("uu")
rec_lhs = sp.sympify(rec_text, locals={"cc": cv / sv, "uu": uu, "ad1": ad1, "H": H, "alpha1": al1, "alpha2": al2,
                                       "alpha3": al3})
ok = all(off_rec[k] == [(0, 4), (4, 0)] for k in (1, 2, 3)) and is_zero(lhs - rec_lhs.subs(uu, bd1 / bb))
check("record_metric_offdiagonal_reproduced", ok,
      "metric of 2026-10-14 (every real z): E_(k) has exactly the off-diagonal pair (x4, x0), (x0, x4) for k = 1, 2, 3, "
      "and sum_k alpha_k E_(k)^x4_x0 equals the record's generalSource.offDiagonal_x4x0 (cot z u Q); E_(1)^x4_x0 = "
      "(3/2) H cot z b4'/b4")
RESULTS["metric_of_2026_10_14_offdiagonal"] = {"E%d^x4_x0" % k: s(E_rec[k][(4, 0)]) for k in (1, 2, 3)}
print("t", round(time.time() - T0, 1), flush=True)

# ---- 3. version 1 (g44 = -Sin[z]^(1/3)) is withdrawn: its g44 oscillates in z and vanishes at z = n Pi
g44v1 = G_V1[4]
per = sp.simplify(g44v1.subs(X[0], X[0] + sp.pi / (6 * H)) - g44v1) == 0
zero_at = sp.limit(g44v1.subs(X[0], sp.Symbol("t", positive=True) / (6 * H)), sp.Symbol("t", positive=True), 0) == 0
varies = sp.simplify(g44v1.subs(X[0], sp.pi / (12 * H)) - g44v1.subs(X[0], sp.pi / (36 * H))) != 0
check("version_1_g44_oscillates", per and zero_at and varies,
      "version 1 of this record (2026-10-16, withdrawn): g44 = -(sin^2 z)^(1/6) is periodic in z with period Pi, varies "
      "with x0 and vanishes at z = n Pi; with z real (-Infinity < z < Infinity) the time lapse oscillates, which the user "
      "excluded (\"g44 cannot oscillate\"); the remedy must keep g44 independent of x0")
print("t", round(time.time() - T0, 1), flush=True)

# ---- 4. the family with g44 = -1: the mixed curvature and the conditions
alp, bet, p, q = sp.symbols("alpha beta p q", real=True)
G_FAM = metric(b4f ** (2 * p) * sp.exp(2 * q * a4f) * sp.cot(z) ** 2, sp.exp(2 * a4f) * (sp.sin(z) ** 2) ** (3 * alp), -1,
               -sp.exp(-2 * a4f) * b4f * (sp.sin(z) ** 2) ** (3 * bet))
gF = [sp.sympify(v) for v in G_FAM]
RF = riemann_uu(gF, X, christoffel(gF, X))
mixedF = {key: sp.powsimp(sp.expand(v), force=True) for key, v in RF.items() if (key[0], key[1]) != (key[2], key[3])}
space_core = alp * ((q - 1) * ad1 * bb + p * bd1)
extra_core = bet * (2 * (q + 1) * ad1 * bb + (2 * p - 1) * bd1)
ok = sorted(mixedF) == sorted([(i, 4, 0, i) for i in (1, 2, 3)] + [(4, t, 0, t) for t in (5, 6, 7)] +
                              [(0, i, i, 4) for i in (1, 2, 3)] + [(0, t, 4, t) for t in (5, 6, 7)])
for key, v in mixedF.items():
    core = space_core if any(k in (1, 2, 3) for k in key) else extra_core
    r = sp.simplify(v / core)
    if r.has(ad1) or r.has(bd1) or sp.simplify(r.subs({bb: 2, EA: 3, sv: sp.Rational(1, 2), cv: sp.sqrt(3) / 2,
                                                      w: 2 ** sp.Rational(-1, 6), alp: 1, bet: 1, p: 1, q: 1})) == 0:
        ok = False
check("family_g44_fixed_conditions", ok,
      "family with g44 = -1: g00 = b4^(2p) e^(2 q a4) cot^2 z, g_ii = e^(2 a4) (sin^2 z)^(3 alpha), g_tt = -e^(-2 a4) b4 "
      "(sin^2 z)^(3 beta): the only mixed Riemann components are R^{x0 xi}_{xi x4}-type ones proportional to "
      "alpha ((q - 1) a4' + p b4'/b4) and R^{x0 xt}_{x4 xt}-type ones proportional to beta ((q + 1) a4' + (p - 1/2) b4'/b4); "
      "they vanish for all a4, b4 iff [alpha = 0 or (q, p) = (1, 0)] and [beta = 0 or (q, p) = (-1, 1/2)]. The author's "
      "two warps (alpha = beta = 1/6) cannot both be kept; keeping the warp of the extra times gives q = -1, p = 1/2, "
      "alpha = 0 (the corrected metric), keeping the warp of 3-space gives q = 1, p = 0, beta = 0 (the alternative K)")
EF1 = lovelock(RF, 8, 1)
e1 = sp.powsimp(sp.expand(EF1.get((4, 0), 0)), force=True)
ein_core = alp * ((q - 1) * ad1 * bb + p * bd1) + bet * ((q + 1) * ad1 * bb + (p - sp.Rational(1, 2)) * bd1)
r1 = sp.simplify(e1 / ein_core)
ok = not r1.has(ad1) and not r1.has(bd1) and not r1.has(alp) and not r1.has(p)
check("family_einstein_condition", ok,
      "in the same family E_(1)^x4_x0 is proportional to alpha ((q - 1) a4' + p b4'/b4) + beta ((q + 1) a4' + (p - 1/2) "
      "b4'/b4): with both warps (alpha = beta = 1/6) it vanishes for all a4, b4 iff q = 0, p = 1/4, i.e. the one-entry "
      "change g00 = b4^(1/2) cot^2 z, which satisfies the Einstein equations only (next check)")
RESULTS["family_mixed_curvature"] = {"space": "alpha ((q - 1) a4' + p b4'/b4)", "extra_times": "beta ((q + 1) a4' + (p - 1/2) b4'/b4)",
                                     "einstein_x4x0": "alpha ((q - 1) a4' + p b4'/b4) + beta ((q + 1) a4' + (p - 1/2) b4'/b4)"}
print("t", round(time.time() - T0, 1), flush=True)

# ---- 5. the corrected metric: no off-diagonal component at any order, diagonal free of x0
G_f, R_f, E_f = curvature(G_FIX, X)
mixed = [key for key in R_f if (key[0], key[1]) != (key[2], key[3])]
check("corrected_mixed_riemann_vanish", mixed == [],
      "corrected metric, every real z: R^{ab}_{cd} = 0 whenever {a, b} != {c, d} (%d nonzero components, all of the form "
      "R^{ab}_{ab})" % len(R_f))
offf = {k: [key for key in E_f[k] if key[0] != key[1]] for k in (1, 2, 3)}
diag_free = all(x0_free(E_f[k][(m, m)]) for k in (1, 2, 3) for m in range(8) if (m, m) in E_f[k])
check("corrected_offdiagonal_all_orders", all(offf[k] == [] for k in (1, 2, 3)) and diag_free,
      "corrected metric: all 56 off-diagonal components of E_(1) (Einstein), E_(2) (Gauss-Bonnet) and E_(3) (cubic "
      "Lovelock) vanish identically for all a4(x4), b4(x4) > 0, H and every real z, and every diagonal component is "
      "independent of x0: the field equations are ordinary differential equations in x4 for a diagonal source that "
      "depends on x4 only")
# the hidden block: e^(-2 a4) b4 times cot^2 z dx0^2 - (sin^2 z)^(1/6) (dx5^2 + dx6^2 + dx7^2)
XB = [X[0], X[5], X[6], X[7]]
gB = [sp.cot(z) ** 2, -S13, -S13, -S13]
RB = riemann_uu(gB, XB, christoffel(gB, XB))
blk_ok = sorted(RB) == sorted([(a, b, a, b) for a in range(4) for b in range(a + 1, 4)]) and \
    all(sp.simplify(v + H ** 2) == 0 for v in RB.values())
check("hidden_block_constant_curvature", blk_ok,
      "the 4-dimensional block cot^2 z dx0^2 - (sin^2 z)^(1/6) (dx5^2 + dx6^2 + dx7^2) of signature (1,3) has constant "
      "curvature: R^{ab}_{ab} = -H^2 for all six pairs, no other component (with y = Log|sin z|/(6 H): dy^2 - e^(2 H y) "
      "(dx5^2 + dx6^2 + dx7^2) wherever sin z != 0); the corrected metric is -dx4^2 + e^(2 a4) (dx1^2 + dx2^2 + dx3^2) + "
      "e^(-2 a4) b4 times this block, so x0 shrinks with the deflating extra times")
print("t", round(time.time() - T0, 1), flush=True)

# Ricci tensor, Ricci scalar and the Einstein tensor (diagonal), in the normal form and in Wolfram form
ricci = {}
for a in range(8):
    tot = 0
    for b in range(8):
        if b != a:
            key = (min(a, b), max(a, b), min(a, b), max(a, b))
            tot += R_f.get(key, 0)
    ricci[a] = reduce_patch(tot)
rs = reduce_patch(sum(ricci.values()))
ok = all(x0_free(v) for v in ricci.values()) and x0_free(rs)


def to_functions(e):
    return e.subs({ad2: sp.Derivative(a4f, X[4], 2), ad1: sp.Derivative(a4f, X[4]), bd2: sp.Derivative(b4f, X[4], 2),
                   bd1: sp.Derivative(b4f, X[4]), bb: b4f, EA: sp.exp(a4f)})


RESULTS["ricci_mixed_diagonal_mathematica"] = {"x%d" % a: sp.printing.mathematica.mathematica_code(to_functions(ricci[a]))
                                               for a in range(8)}
RESULTS["ricci_scalar_mathematica"] = sp.printing.mathematica.mathematica_code(to_functions(rs))
RESULTS["einstein_diagonal"] = {"x%d" % a: s(E_f[1][(a, a)]) for a in (0, 1, 4, 5)}
check("ricci_tensor", ok and all((a, b) not in E_f[1] for a in range(8) for b in range(8) if a != b),
      "corrected metric: the Ricci tensor R^mu_nu = sum_b R^{mu b}_{nu b} is diagonal and independent of x0; R = %s; "
      "recorded in Wolfram form for the field-theory record" % s(rs))
print("t", round(time.time() - T0, 1), flush=True)

# ---- 6. the divergence of a diagonal tensor in the corrected metric (entries functions of x0 and x4)
gfx = [sp.sympify(v) for v in G_FIX]
Gfx = christoffel(gfx, X)
Tf = {m: sp.Function("T%d" % m)(X[0], X[4]) for m in (0, 1, 4, 5)}
Tdiag = [Tf[0], Tf[1], Tf[1], Tf[1], Tf[4], Tf[5], Tf[5], Tf[5]]


def Gm(a, b, c):
    return Gfx.get((a, b, c), 0)


div = []
for nu in range(8):
    v = sp.diff(Tdiag[nu], X[nu])
    v += sum(Gm(m, m, nu) * Tdiag[nu] for m in range(8))
    v -= sum(Gm(m, m, nu) * Tdiag[m] for m in range(8))
    div.append(v)
rho, p3, pt, p0 = sp.symbols("rho p3 pt p0")
r4, p00 = sp.symbols("rho_4 p0_0")


def plain_T(e):
    e = e.subs({sp.Derivative(Tf[4], X[4]): -r4, sp.Derivative(Tf[0], X[0]): p00})
    e = e.subs({Tf[0]: p0, Tf[1]: p3, Tf[4]: -rho, Tf[5]: pt})
    return normal(e)


d4 = plain_T(div[4])
d0 = plain_T(div[0])
hc = bd1 / (2 * bb) - ad1  # the rate of the block x0, x5, x6, x7: d ln(e^(-a4) b4^(1/2))/dx4
exp4 = -r4 - 3 * ad1 * (rho + p3) - 3 * hc * (rho + pt) - hc * (rho + p0)
exp0 = p00 + 3 * H * (cv / sv) * (p0 - pt)
ctrl = not is_zero(d4 - (-r4 - 3 * ad1 * (p3 - pt) - sp.Rational(3, 2) * bd1 / bb * (rho + pt)))
ok = all(normal(div[nu]) == 0 for nu in (1, 2, 3, 5, 6, 7)) and is_zero(d4 - exp4) and is_zero(d0 - exp0) and ctrl
check("divergence_of_diagonal_tensor", ok,
      "corrected metric, T = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) with entries depending on x0 and x4: "
      "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (rho + p3) - 3 h (rho + p_t) - h (rho + p0) with h = b4'/(2 b4) - a4' the rate of "
      "the block x0, x5, x6, x7 (each expanding direction dilutes rho + its pressure), nabla_mu T^mu_x0 = d0 p0 + 3 H cot z "
      "(p0 - p_t) (the hidden direction balances against the extra times only), the six other components vanish "
      "identically; for x0-independent entries the x0 balance needs p0 = p_t. Control: the x4 identity of the metric of "
      "2026-10-14 differs")
RESULTS["divergence_of_diagonal_tensor"] = {"x4": "-d4 rho - 3 a4' (rho + p3) - 3 h (rho + p_t) - h (rho + p0), h = b4'/(2 b4) - a4'",
                                            "x0": "d0 p0 + 3 H Cot[z] (p0 - p_t)"}
print("t", round(time.time() - T0, 1), flush=True)

# ---- 7. the source of the record's history a4 = A H x4, b4 = b4(0) e^(beta A H x4), b4(0) = 1
A, be = sp.symbols("A beta", real=True)
hist = {ad1: A * H, ad2: 0, bb: sp.exp(be * A * H * X[4]), bd1: be * A * H * sp.exp(be * A * H * X[4]),
        bd2: (be * A * H) ** 2 * sp.exp(be * A * H * X[4]), EA: sp.exp(A * H * X[4])}
aw = {al1: 1 / H ** 2, al2: sp.Rational(1, 32) / H ** 4, al3: sp.Rational(1, 1152) / H ** 6}
names = {0: "p0", 1: "p3", 4: "-rho", 5: "p_t"}
srcE, srcA = {}, {}
for m in (0, 1, 4, 5):
    srcE[m] = sp.simplify(E_f[1][(m, m)].subs(hist))
    srcA[m] = sp.simplify(sum(aw[al] * E_f[k][(m, m)].subs(hist) for k, al in ((1, al1), (2, al2), (3, al3))))
h43 = {A: 1, be: sp.Rational(4, 3)}
RESULTS["history_source"] = {
    "history": "a4 = A H x4, b4 = b4(0) E^(beta A H x4) (b4(0) = 1); record values A = 1, beta = 4/3",
    "einstein_kappaT_minus_Lambda": {names[m]: s(sp.factor(srcE[m])) for m in (0, 1, 4, 5)},
    "einstein_A1_beta43": {names[m]: s(sp.simplify(srcE[m].subs(h43))) for m in (0, 1, 4, 5)},
    "author_weights_A1_beta43": {names[m]: s(sp.simplify(srcA[m].subs(h43))) for m in (0, 1, 4, 5)},
    "einstein_A1_beta43_mathematica": {names[m]: sp.printing.mathematica.mathematica_code(sp.simplify(srcE[m].subs(h43)))
                                       for m in (0, 1, 4, 5)},
    "author_weights_A1_beta43_mathematica": {names[m]: sp.printing.mathematica.mathematica_code(sp.simplify(srcA[m].subs(h43)))
                                             for m in (0, 1, 4, 5)}}
ok = all(x0_free(v) for v in list(srcE.values()) + list(srcA.values())) and \
    sp.simplify(srcE[0] - srcE[5]) == 0 and sp.simplify(srcA[0] - srcA[5]) == 0
# conservation of these x0-independent sources with the x4 identity (p0 = p_t holds)
cons = True
for src in (srcE, srcA):
    rho_h = -src[4]
    hch = be * A * H / 2 - A * H
    expr = -sp.diff(rho_h, X[4]) - 3 * A * H * (rho_h + src[1]) - 3 * hch * (rho_h + src[5]) - hch * (rho_h + src[0])
    if sp.simplify(expr) != 0:
        cons = False
check("history_source_conserved", ok and cons,
      "on the history a4 = A H x4, b4 = e^(beta A H x4) the source kappa T - Lambda delta = sum_k alpha_k E_(k) (Einstein "
      "and the author's weights) is diagonal, independent of x0, with p0 = p_t (the hidden direction and the extra times "
      "form one block), and depends on x4 through the curvature term H^2 e^(2 a4)/b4 = H^2 e^((2 - beta) A H x4) of the "
      "shrinking block; it satisfies nabla_mu T^mu_nu = 0 (the x4 identity above; the x0 identity holds because p0 = p_t). "
      "At A = 1, beta = 4/3 (Einstein): %s" % s(RESULTS["history_source"]["einstein_A1_beta43"]))
print("t", round(time.time() - T0, 1), flush=True)

# ---- 8. the gravity term of the Dirac operator: gamma^mu Omega_mu = (1/2) sum_a gamma^(a) (1/sqrt g) d_a (sqrt g/f_a)
volf = sp.prod(f_fix)
coef = [normal(sp.Rational(1, 2) * sp.diff(volf / f_fix[a], X[a]) / volf) for a in range(8)]
ok = all(coef[a] == 0 for a in (1, 2, 3, 5, 6, 7)) and is_zero(coef[0] - sp.Rational(3, 2) * H * EA / sp.sqrt(bb)) and \
    is_zero(coef[4] - (bd1 / bb - ad1 / 2))
check("dirac_gravity_term", ok,
      "corrected metric, vielbein f0 = e^(-a4) b4^(1/2) cot z, f_i = e^(a4), f4 = 1, f_t = e^(-a4) b4^(1/2) (sin^2 z)^(1/12): "
      "gamma^mu Omega_mu = (3/2) H e^(a4) b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4), independent of x0 for every "
      "real z (the metric of 2026-10-14: 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4)); on the history (b4'/b4 = (4/3) a4') "
      "the gamma^(x4) coefficient is (5/6) a4'")
RESULTS["dirac_gravity_term"] = "(3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4)"
print("t", round(time.time() - T0, 1), flush=True)

# ---- 9. flat space in Milne form: a4 = 0, b4 = H^2 x4^2 (all Lovelock tensors vanish)
mil = {ad1: 0, ad2: 0, bb: H ** 2 * X[4] ** 2, bd1: 2 * H ** 2 * X[4], bd2: 2 * H ** 2, EA: 1}
riem_flat = all(sp.simplify(v.subs(mil)) == 0 for v in R_f.values())
check("milne_flat_check", riem_flat,
      "a4 = 0, b4 = H^2 x4^2 makes every Riemann component of the corrected metric vanish (8-dimensional flat space in "
      "Milne form: the block x0, x5, x6, x7 of constant curvature -H^2 scaled by H x4), so all Lovelock tensors vanish: a "
      "consistency check of the formulas with b4 not constant, not a physical history (3-space does not expand)")
print("t", round(time.time() - T0, 1), flush=True)

# ---- 10. the alternatives: K (all orders, x0 grows with 3-space) and the Einstein-only g00 = b4^(1/2) cot^2 z
_, R_K, E_K = curvature(G_K, X)
okK = [key for key in R_K if (key[0], key[1]) != (key[2], key[3])] == [] and \
    all([key for key in E_K[k] if key[0] != key[1]] == [] for k in (1, 2, 3)) and \
    all(x0_free(E_K[k][(m, m)]) for k in (1, 2, 3) for m in range(8) if (m, m) in E_K[k])
_, R_E, E_E = curvature(G_EIN, X, kmax=2)
eE2 = sp.factor(E_E[2].get((4, 0), 0))
okE = [key for key in E_E[1] if key[0] != key[1]] == [] and eE2 != 0
check("alternatives", okK and okE,
      "alternative K = diag(e^(2 a4) cot^2 z, e^(2 a4) (sin^2 z)^(1/6) (x3), -1, -e^(-2 a4) b4 (x3)): no off-diagonal "
      "component at any order and diagonal free of x0, but the hidden direction grows with 3-space (the block x0, x1, x2, "
      "x3 carries the factor e^(2 a4)), while in the corrected metric it shrinks with the extra times; "
      "the Einstein-only change g00 = b4^(1/2) cot^2 z keeps both warps and makes the Einstein tensor diagonal, but "
      "E_(2)^x4_x0 = %s != 0" % s(eE2))
print("t", round(time.time() - T0, 1), flush=True)

# ---- report
RESULTS["checks_passed"] = "%d of %d" % (sum(c["verdict"] == "PASS" for c in CHECKS), len(CHECKS))
os.makedirs(os.path.join(OUT, "results"), exist_ok=True)
os.makedirs(os.path.join(OUT, "reports"), exist_ok=True)
with open(os.path.join(OUT, "results", "warped-metric.json"), "w", encoding="utf-8", newline="\n") as fh:
    json.dump(RESULTS, fh, indent=1, sort_keys=True, ensure_ascii=True)
    fh.write("\n")
with open(os.path.join(OUT, "reports", "python-warped-metric-report.json"), "w", encoding="utf-8", newline="\n") as fh:
    json.dump({"program": "Revision/metric_warped/python/derive_warped_metric.py", "checks": CHECKS}, fh, indent=1,
              ensure_ascii=True)
    fh.write("\n")
print("python_warped_metric=%s (%s) seconds=%.1f" % (
    "OK" if all(c["verdict"] == "PASS" for c in CHECKS) else "FAIL", RESULTS["checks_passed"], time.time() - T0))
sys.exit(0 if all(c["verdict"] == "PASS" for c in CHECKS) else 1)
