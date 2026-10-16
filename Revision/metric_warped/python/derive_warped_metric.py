"""derive_warped_metric.py - the self-consistency of the primordial metric with diagonal sources, and the
warped metric of 2026-10-16 (the user's order of 2026-10-16: "find the simplest modification for the current
metric of the primordial gravitational field that is probably self-consistent with the Einstein field equations").

A diagonal metric is self-consistent with the field equations  sum_k alpha_k E_(k)^mu_nu + Lambda delta^mu_nu =
kappa T^mu_nu  only if every off-diagonal component of the left-hand side equals the off-diagonal component of the
source.  For the metric of 2026-10-14 (SPEC section 1 until 2026-10-16) the left-hand side has the component
E^{x4}_{x0} ~ cot z b4'/b4 at every Lovelock order, so a diagonal source forces b4' = 0 (Einstein) or a special
history (the author's weights).  This program
  * reproduces that component and the record's factor Q (Revision/field_equations_a4/a4-equations.json of commit
    04fa2e7, frozen in Revision/metric_warped/reference_2026_10_14/a4-offdiagonal-x4x0.json);
  * scans the two-parameter family g00 = b4^(2p) e^(2 q a4) cot^2 z, g44 = -sin^(2 gamma) z (all other entries as
    in the metric of 2026-10-14) and proves: the Einstein component vanishes for all a4, b4 exactly when q = 0 and
    6 gamma + 4 p = 1; on that line the Gauss-Bonnet component is proportional to (6 gamma - 1) b4' (4 a4' b4 - b4')^2,
    so the ONLY member for which every Lovelock order is free of off-diagonal terms is gamma = 1/6, p = 0:
        the warped metric  g44 = -Sin[6 H x0]^(1/3)  (every one of x1, ..., x7 carries the factor Sin[6 H x0]^(1/3));
  * proves for the warped metric: every off-diagonal component of E_(1), E_(2), E_(3) and every mixed Riemann
    component vanishes identically; the Lovelock tensors split into layers Sin[z]^(-j/3) times the Lovelock tensors
    of the 7-dimensional metric of x1..x7; the Einstein equations reduce to 7-dimensional Einstein equations on each
    slice of constant x0; exact vacuum solutions with b4 not constant (Kasner) exist for Einstein gravity with
    Lambda = -21 H^2; the source required by the record's history and its conservation; the gravity term of the
    Dirac operator;
  * records the rejected one-entry alternative g00 = b4^(1/2) cot^2 z (Einstein only).
Coordinates: the author's x0..x7 (index 0 = x0, the hidden direction; x4 = the time).  Conventions of the Revision
record: Riemann R^a_{bcd} (MTW), R^{ab}_{cd} = g^{be} R^a_{ecd}, P_(k)^h_j = GKD[{h,h1..h2k},{j,j1..j2k}]
R^{j1j2}_{h1h2}..., E_(k) = -P_(k)/2^(k+1) (E_(1) = Einstein), field equations sum_k alpha_k E_(k) + Lambda delta =
kappa T (Revision/field_equations_a4/a4-equations.json, conventions).
Writes Revision/metric_warped/results/warped-metric.json and Revision/metric_warped/reports/python-warped-metric-report.json
(UTF-8, LF, sorted keys, no time stamps).  Exit code 0 if every check passes.  Usage (repository root):
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
SIN13 = sp.sin(z) ** sp.Rational(1, 3)
# plain symbols of the normal form: ad1 = a4', ad2 = a4'', bb = b4 > 0, bd1 = b4', bd2 = b4'', cc = cot z > 0,
# W = Sin[z]^(-1/3) = (1 + cc^2)^(1/6) > 0 (the inverse square of the warp factor w = Sin[z]^(1/6))
ad1, ad2, ad3, bd1, bd2, bd3 = sp.symbols("ad1 ad2 ad3 bd1 bd2 bd3", real=True)
bb, cc, W = sp.symbols("bb cc W", positive=True)
al1, al2, al3, Lam, kap = sp.symbols("alpha1 alpha2 alpha3 Lam kappa", real=True)
CHECKS = []
RESULTS = {}


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + ": " + detail, flush=True)


def s(e):
    return sp.sstr(e)


# ---------------------------------------------------------------- normal form
def normal(e):
    """Write derivatives and trigonometric functions of z as plain symbols; cot z = cc, Sin[z]^(1/3) = 1/W^2."""
    e = sp.sympify(e)
    for old, new in [(sp.Derivative(a4f, X[4], 3), ad3), (sp.Derivative(a4f, X[4], 2), ad2),
                     (sp.Derivative(a4f, X[4]), ad1), (sp.Derivative(b4f, X[4], 3), bd3),
                     (sp.Derivative(b4f, X[4], 2), bd2), (sp.Derivative(b4f, X[4]), bd1)]:
        e = e.subs(old, new)
    e = e.subs(b4f, bb)
    # double angles first (sympy's simplify writes Sin[2 z] etc.)
    e = e.subs({sp.sin(2 * z): 2 * sp.sin(z) * sp.cos(z), sp.cos(2 * z): sp.cos(z) ** 2 - sp.sin(z) ** 2,
                sp.tan(2 * z): 2 * sp.tan(z) / (1 - sp.tan(z) ** 2), sp.cot(2 * z): (sp.cot(z) ** 2 - 1) / (2 * sp.cot(z)),
                sp.csc(2 * z): 1 / (2 * sp.sin(z) * sp.cos(z)), sp.sec(2 * z): 1 / (sp.cos(z) ** 2 - sp.sin(z) ** 2)})
    sinz = W ** -3
    e = e.subs({sp.sin(z): sinz, sp.cos(z): cc * sinz, sp.tan(z): 1 / cc, sp.cot(z): cc,
                sp.sec(z): 1 / (cc * sinz), sp.csc(z): 1 / sinz})
    e = sp.powsimp(sp.powdenest(sp.expand(e), force=True), force=True)
    # on the patch 1 + cc^2 = W^6
    e = sp.together(sp.expand(e))
    num, den = sp.fraction(e)
    return sp.factor(num / den)


def reduce_patch(e):
    """Exact reduction modulo the patch relation cc^2 = W^6 - 1 (W = Sin^(-1/3) z, cc = cot z)."""
    e = sp.together(sp.expand(e))
    num, den = sp.fraction(e)
    num = sp.expand(num)
    num = sp.rem(sp.Poly(num, cc), sp.Poly(cc ** 2 - W ** 6 + 1, cc)).as_expr() if num.has(cc) else num
    den = sp.expand(den)
    den = sp.rem(sp.Poly(den, cc), sp.Poly(cc ** 2 - W ** 6 + 1, cc)).as_expr() if den.has(cc) else den
    return sp.factor(sp.expand(num) / sp.expand(den))


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
                    v = sp.cancel(t / (2 * g[a]))
                    if v != 0:
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
    """Sign of the permutation that maps the list seq_from onto seq_to (same elements), else 0."""
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
    """E_(k)^h_j = -(1/2^(k+1)) GKD[{h,h1..h2k},{j,j1..j2k}] R^{j1j2}_{h1h2}...; GKD by permutation sign.
    Also returns the scalar E_(k)^(0) := -(1/2^(k+1)) GKD[{h1..h2k},{j1..j2k}] R^{j1j2}_{h1h2}..."""
    syms = {key: sp.Symbol("R_%d_%d_%d_%d" % key) for key in R}
    items = list(syms.items())
    acc = {}
    scal = 0
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
        if sorted(low) == sorted(up):
            scal += perm_sign(up, low) * val
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
        v = normal(-v.xreplace(sub) / 2 ** (k + 1))
        if v != 0:
            E[key] = v
    scal = normal(-sp.expand(scal).xreplace(sub) / 2 ** (k + 1))
    return E, scal


def curvature(gdiag, coords, kmax=3):
    g = [sp.sympify(v) for v in gdiag]
    G = christoffel(g, coords)
    R = riemann_uu(g, coords, G)
    E = {}
    Es = {}
    for k in range(1, kmax + 1):
        E[k], Es[k] = lovelock(R, len(coords), k)
    return G, R, E, Es


def levels(e):
    """Split a normal-form expression into powers of W = Sin^(-1/3) z (layer j = W^j = w^(-2j))."""
    e = reduce_patch(e)
    e = sp.expand(e)
    if e.has(cc):
        return None
    out = {}
    for term in sp.Add.make_args(e):
        pw = sp.degree(term, W) if term.has(W) else 0
        out[pw] = out.get(pw, 0) + term / W ** pw
    return {kk: sp.factor(v) for kk, v in out.items()}


# ---------------------------------------------------------------- the metrics
def metric(g00_factor=1, g44=-1):
    return [g00_factor * sp.cot(z) ** 2] + [sp.exp(2 * a4f) * SIN13] * 3 + [g44] + \
           [-sp.exp(-2 * a4f) * b4f * SIN13] * 3


G_RECORD = metric()
G_WARPED = metric(1, -SIN13)
G_HIDDEN = metric(sp.sqrt(b4f), -1)

RESULTS["metric_warped"] = [s(v) for v in G_WARPED]
RESULTS["metric_of_2026_10_14"] = [s(v) for v in G_RECORD]
RESULTS["coordinates"] = "x0 (hidden, z = 6 H x0 in (0, pi/2)), x1, x2, x3 (space), x4 (time), x5, x6, x7 (extra times)"

# ---- 1. the metric and its volume factor
sqrtg = sp.sqrt(sp.Abs(sp.prod(G_WARPED)))
sqrtg_n = normal(sp.sqrt(sp.prod([sp.Abs(v) for v in G_WARPED]).subs(sp.Abs(sp.cot(z)), sp.cot(z))))
target = normal(b4f ** sp.Rational(3, 2) * sp.cos(z) * sp.sin(z) ** sp.Rational(1, 6))
ok = is_zero(sqrtg_n - target)
check("sqrt_det_g", ok, "sqrt|det g| = b4^(3/2) Cos[z] Sin[z]^(1/6) for the warped metric (the metric of 2026-10-14: "
      "b4^(3/2) Cos[z]); the extra factor Sin[z]^(1/6) is the warp of g44")
RESULTS["sqrt_det_g"] = "b4^(3/2) Cos[6 H x0] Sin[6 H x0]^(1/6)"

y = sp.Symbol("y", real=True)
ycoord = sp.log(sp.sin(z)) / (6 * H)
ok1 = sp.simplify(sp.diff(ycoord, X[0]) - sp.cot(z)) == 0
ok2 = sp.simplify(sp.exp(2 * H * ycoord) - SIN13) == 0
check("proper_hidden_coordinate", ok1 and ok2,
      "y = Log[Sin[z]]/(6 H): dy = Cot[z] dx0 and Sin[z]^(1/3) = E^(2 H y), so the warped metric is "
      "ds^2 = dy^2 + E^(2 H y) (E^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - E^(-2 a4) b4 (dx5^2 + dx6^2 + dx7^2)), "
      "y in (-Infinity, 0): a warped product of the hidden line and the 7-dimensional metric of x1..x7")
RESULTS["warped_product_form"] = ("ds^2 = dy^2 + E^(2 H y) ghat7, y = Log[Sin[6 H x0]]/(6 H), ghat7 = E^(2 a4) "
                                  "(dx1^2 + dx2^2 + dx3^2) - dx4^2 - E^(-2 a4) b4 (dx5^2 + dx6^2 + dx7^2)")
print("t", round(time.time() - T0, 1), flush=True)

# ---- 2. the metric of 2026-10-14: the off-diagonal component at every order, and the record's factor Q
_, R_rec, E_rec, _ = curvature(G_RECORD, X)
off_rec = {k: sorted(key for key in E_rec[k] if key[0] != key[1]) for k in (1, 2, 3)}
lhs = sum(a * E_rec[k].get((4, 0), 0) for k, a in ((1, al1), (2, al2), (3, al3)))
with open(os.path.join(OUT, "reference_2026_10_14", "a4-offdiagonal-x4x0.json"), encoding="utf-8") as f:
    a4eq = json.load(f)  # frozen copy of the record of 2026-10-14 (commit 04fa2e7)
rec_text = a4eq["generalSource.offDiagonal_x4x0"]["input"].split("==")[0]
uu = sp.Symbol("uu")
rec_lhs = sp.sympify(rec_text, locals={"cc": cc, "uu": uu, "ad1": ad1, "H": H, "alpha1": al1, "alpha2": al2,
                                       "alpha3": al3})
ok = all(off_rec[k] == [(0, 4), (4, 0)] for k in (1, 2, 3)) and is_zero(lhs - rec_lhs.subs(uu, bd1 / bb))
check("record_metric_offdiagonal_reproduced", ok,
      "metric of 2026-10-14: E_(k) has exactly the off-diagonal pair (x4, x0), (x0, x4) for k = 1, 2, 3, and "
      "sum_k alpha_k E_(k)^x4_x0 equals the record's generalSource.offDiagonal_x4x0 (cot z u Q)")
RESULTS["metric_of_2026_10_14_offdiagonal"] = {"E1^x4_x0": s(E_rec[1][(4, 0)]), "E2^x4_x0": s(E_rec[2][(4, 0)]),
                                               "E3^x4_x0": s(E_rec[3][(4, 0)])}
print("t", round(time.time() - T0, 1), flush=True)

# ---- 3. the two-parameter family
gam, p, q = sp.symbols("gamma p q", real=True)
G_FAM = metric(b4f ** (2 * p) * sp.exp(2 * q * a4f), -sp.sin(z) ** (2 * gam))
gF = [sp.sympify(v) for v in G_FAM]
GF = christoffel(gF, X)
RF = riemann_uu(gF, X, GF)
EF1, _ = lovelock(RF, 8, 1)
e1 = EF1.get((4, 0), 0)
e1 = sp.factor(sp.powsimp(sp.expand(e1), force=True))
expected1 = -3 * H * cc * (4 * q * ad1 * bb + (6 * gam + 4 * p - 1) * bd1) / (2 * bb)
ratio1 = sp.simplify(e1 / expected1)
ok = sp.simplify(ratio1.subs({ad1: 1, bd1: 1, bb: 1})) != 0 and not sp.simplify(ratio1).has(ad1, bd1) \
    and sorted(key for key in EF1 if key[0] != key[1]) == [(0, 4), (4, 0)]
check("family_einstein_condition", ok,
      "family g00 = b4^(2p) E^(2 q a4) Cot[z]^2, g44 = -Sin[z]^(2 gamma): the only off-diagonal Einstein component is "
      "E1^x4_x0 = -(3 H cot z/(2 b4)) (4 q a4' b4 + (6 gamma + 4 p - 1) b4') times a positive factor; it vanishes for "
      "all a4, b4 exactly when q = 0 and 6 gamma + 4 p = 1")
RESULTS["family_E1_x4x0"] = s(e1)
print("t", round(time.time() - T0, 1), flush=True)

# Gauss-Bonnet on the Einstein line q = 0, p = (1 - 6 gamma)/4
G_LINE = metric(b4f ** ((1 - 6 * gam) / 2), -sp.sin(z) ** (2 * gam))
gL = [sp.sympify(v) for v in G_LINE]
GL_ = christoffel(gL, X)
RL_ = riemann_uu(gL, X, GL_)
EL2, _ = lovelock(RL_, 8, 2)
e2 = sp.factor(sp.powsimp(sp.expand(EL2.get((4, 0), 0)), force=True))
core = (6 * gam - 1) * bd1 * (4 * ad1 * bb - bd1) ** 2
ratio2 = sp.simplify(e2 / core)
ok = not ratio2.has(ad1) and not ratio2.has(bd1) and sp.simplify(ratio2.subs({bb: 1, cc: 1, W: 1})) != 0
check("family_gauss_bonnet_condition", ok,
      "on the Einstein line (q = 0, p = (1 - 6 gamma)/4) the Gauss-Bonnet component E2^x4_x0 is (6 gamma - 1) b4' "
      "(4 a4' b4 - b4')^2 times a nonzero factor: it vanishes for all a4, b4 exactly when gamma = 1/6, p = 0 (the "
      "warped metric); every other member needs an off-diagonal source as soon as b4' != 0 and b4' != 4 a4' b4")
RESULTS["family_E2_x4x0_on_einstein_line"] = s(e2)
print("t", round(time.time() - T0, 1), flush=True)

# ---- 4. the warped metric: every off-diagonal component vanishes
G_w, R_w, E_w, Es_w = curvature(G_WARPED, X)
mixed = [key for key in R_w if (key[0], key[1]) != (key[2], key[3])]
check("warped_mixed_riemann_vanish", mixed == [],
      "warped metric: R^{ab}_{cd} = 0 whenever {a, b} != {c, d} (%d nonzero components, all of the form R^{ab}_{ab}); "
      "the metric of 2026-10-14 has %d mixed components R^{x0 c}_{x4 c}" % (
          len(R_w), len([key for key in R_rec if (key[0], key[1]) != (key[2], key[3])])))
offw = {k: [key for key in E_w[k] if key[0] != key[1]] for k in (1, 2, 3)}
check("warped_offdiagonal_all_orders", all(offw[k] == [] for k in (1, 2, 3)),
      "warped metric: all 56 off-diagonal components of E_(1) (Einstein), E_(2) (Gauss-Bonnet) and E_(3) (cubic "
      "Lovelock) vanish identically, for all functions a4(x4), b4(x4) > 0 and every H")
print("t", round(time.time() - T0, 1), flush=True)

# ---- 5. the rejected alternative g00 = b4^(1/2) cot^2 z
_, R_h, E_h, _ = curvature(G_HIDDEN, X)
offh = {k: sorted(key for key in E_h[k] if key[0] != key[1]) for k in (1, 2, 3)}
eh2 = sp.factor(E_h[2].get((4, 0), 0))
ok = offh[1] == [] and offh[2] == [(0, 4), (4, 0)] and offh[3] == [(0, 4), (4, 0)] and \
    sp.simplify(eh2 / (bd1 * (4 * ad1 * bb - bd1) ** 2)).has(ad1) is False
check("alternative_hidden_breathing_einstein_only", ok,
      "g00 = b4^(1/2) Cot[z]^2 (g44 = -1): the Einstein tensor is diagonal, but E2^x4_x0 = %s and E3^x4_x0 != 0: "
      "Einstein-Lovelock gravity still needs an off-diagonal source; also b4 itself (not only b4'/b4) enters" % s(eh2))
RESULTS["alternative_hidden_breathing"] = {"metric_g00": "b4^(1/2) Cot[6 H x0]^2", "E2^x4_x0": s(eh2),
                                           "E3^x4_x0": s(sp.factor(E_h[3].get((4, 0), 0)))}
print("t", round(time.time() - T0, 1), flush=True)

# ---- 6. layers: E_(k) = sum_j c_kj H^(2(k-j)) W^(2j) Ehat_(j) (the Lovelock tensors of the 7-dimensional metric)
X7 = X[1:8]
G7 = [sp.exp(2 * a4f)] * 3 + [sp.Integer(-1)] + [-sp.exp(-2 * a4f) * b4f] * 3
_, R7, E7, Es7 = curvature(G7, X7)
C = {(1, 0): 21, (1, 1): 1, (2, 0): -420, (2, 1): -40, (2, 2): 1, (3, 0): 2520, (3, 1): 360, (3, 2): -18, (3, 3): 1}
ok = True
bad = []
for k in (1, 2, 3):
    for mu in range(8):
        lv = levels(E_w[k][(mu, mu)])
        if lv is None:
            ok = False
            bad.append((k, mu, "cc"))
            continue
        for j in range(0, k + 1):
            if j == 0:
                fib = 1
            elif mu == 0:
                fib = Es7[j]
            else:
                fib = E7[j].get((mu - 1, mu - 1), 0)
            want = C[(k, j)] * H ** (2 * (k - j)) * fib if j > 0 else C[(k, 0)] * H ** (2 * k)
            have = lv.get(j, 0)
            if sp.simplify(have - want) != 0:
                ok = False
                bad.append((k, mu, j))
        if set(lv) - set(range(k + 1)):
            ok = False
            bad.append((k, mu, "extra"))
check("warped_layer_decomposition", ok,
      "E_(k)^mu_mu = sum_{j=0..k} c_kj H^(2(k-j)) Sin[z]^(-j/3) Ehat_(j)^mu_mu, where Ehat_(j) is the Lovelock tensor "
      "of order j of the 7-dimensional metric of x1..x7 (computed separately) for mu = x1..x7, and its scalar "
      "Ehat_(j)^(0) = -(1/2^(j+1)) GKD R..R for mu = x0; Ehat_(0) = 1; c = %s%s" % (
          s({"%d%d" % kj: v for kj, v in C.items()}), "" if ok else "; failures " + s(bad)))
RESULTS["layer_coefficients_c_kj"] = {"%d%d" % kj: v for kj, v in C.items()}
RESULTS["fiber_lovelock_tensors"] = {"Ehat%d" % j: {"x%d" % (m + 1): s(E7[j].get((m, m), 0)) for m in range(7)}
                                     for j in (1, 2, 3)}
RESULTS["fiber_lovelock_scalars"] = {"Ehat%d^(0)" % j: s(Es7[j]) for j in (1, 2, 3)}
print("t", round(time.time() - T0, 1), flush=True)

# effective couplings beta_j = sum_k alpha_k c_kj H^(2(k-j)); the author's weights alpha_k = w_k/H^(2k)
alpha = {1: al1, 2: al2, 3: al3}
beta = {0: sum(alpha[k] * C[(k, 0)] * H ** (2 * k) for k in (1, 2, 3)) + Lam}
for j in (1, 2, 3):
    beta[j] = sum(alpha[k] * C[(k, j)] * H ** (2 * (k - j)) for k in range(j, 4))
aw = {al1: 1 / H ** 2, al2: sp.Rational(1, 32) / H ** 4, al3: sp.Rational(1, 1152) / H ** 6}
betaA = {j: sp.simplify(beta[j].subs(aw)) for j in beta}
ok = betaA[0] == sp.Rational(161, 16) + Lam and betaA[1] == sp.Rational(1, 16) / H ** 2 and \
    betaA[2] == sp.Rational(1, 64) / H ** 4 and betaA[3] == sp.Rational(1, 1152) / H ** 6
check("warped_field_equations_layers", ok,
      "sum_k alpha_k E_(k) + Lambda = beta_0 + sum_j beta_j Sin[z]^(-j/3) Ehat_(j) with beta_0 = 21 alpha1 H^2 - 420 "
      "alpha2 H^4 + 2520 alpha3 H^6 + Lambda, beta_1 = alpha1 - 40 alpha2 H^2 + 360 alpha3 H^4, beta_2 = alpha2 - "
      "18 alpha3 H^2, beta_3 = alpha3; the author's weights (alpha_k = w_k/H^(2k), w = 1, 1/32, 1/1152) give beta_0 = "
      "161/16 + Lambda, beta_1 = 1/(16 H^2), beta_2 = 1/(64 H^4), beta_3 = 1/(1152 H^6)")
RESULTS["effective_couplings"] = {"beta%d" % j: s(beta[j]) for j in beta}
RESULTS["effective_couplings_author_weights"] = {"beta%d" % j: s(betaA[j]) for j in betaA}
print("t", round(time.time() - T0, 1), flush=True)

# ---- 7. exact vacuum solutions of Einstein gravity: Kasner fibers
x4 = X[4]
ok = True
kas_list = []
for sign in (1, -1):
    ps = (1 + sign * sp.sqrt(5)) / 6
    pt = (1 - sign * sp.sqrt(5)) / 6
    sub = {ad1: ps / x4, ad2: -ps / x4 ** 2, bb: x4 ** sp.Rational(2, 3), bd1: sp.Rational(2, 3) * x4 ** sp.Rational(-1, 3),
           bd2: -sp.Rational(2, 9) * x4 ** sp.Rational(-4, 3)}
    for mu in range(8):
        if sp.simplify(reduce_patch(E_w[1][(mu, mu)]).subs(sub) - 21 * H ** 2) != 0:
            ok = False
    # the extra-time scale factor E^(-a4) b4^(1/2) = x4^pt
    if sp.simplify(sp.exp(-ps * sp.log(x4)) * x4 ** sp.Rational(1, 3) - x4 ** pt) != 0:
        ok = False
    kas_list.append({"a4": s(ps * sp.log(x4)), "b4": "x4^(2/3)", "space_scale": "x4^(%s)" % s(ps),
                     "extra_time_scale": "x4^(%s)" % s(pt)})
check("einstein_vacuum_kasner", ok,
      "Einstein gravity (alpha1 = 1, alpha2 = alpha3 = 0) with Lambda = -21 H^2: for E^(a4) = x4^ps, b4 = x4^(2/3) "
      "(ps = (1 +- Sqrt[5])/6) all 64 components of E_(1) + Lambda vanish at every x0: exact vacuum solutions with "
      "b4 not constant; for ps = (1 + Sqrt[5])/6 = 0.539 space expands and the extra times deflate as x4^((1 - Sqrt[5])/6) "
      "= x4^(-0.206) (the fiber is a 7-dimensional Kasner metric, sum p = sum p^2 = 1)")
RESULTS["einstein_vacuum_kasner"] = {"Lambda": "-21 H^2", "solutions": kas_list}

# the author's weights: the Kasner fibers are not vacuum (Ehat_2 != 0), and no exponential fiber is Ricci-flat
A, be = sp.symbols("A beta", real=True)
sub_k = {ad1: (1 + sp.sqrt(5)) / 6 / x4, ad2: -(1 + sp.sqrt(5)) / 6 / x4 ** 2, bb: x4 ** sp.Rational(2, 3),
         bd1: sp.Rational(2, 3) * x4 ** sp.Rational(-1, 3), bd2: -sp.Rational(2, 9) * x4 ** sp.Rational(-4, 3)}
e2k = sp.simplify(E7[2][(0, 0)].subs(sub_k))
hist = {ad1: A * H, ad2: 0, bb: sp.exp(be * A * H * x4), bd1: be * A * H * sp.exp(be * A * H * x4),
        bd2: (be * A * H) ** 2 * sp.exp(be * A * H * x4)}
r00 = sp.factor(sp.simplify(Es7[1].subs(hist)))
ok = e2k != 0 and sp.factor(sp.simplify(E7[1][(0, 0)].subs(hist) - E7[1][(4, 4)].subs(hist))) != 0
check("author_weights_vacuum_conditions", ok,
      "with the author's weights the field equations hold at every x0 only if beta_0 = 0 and Ehat_(1) = Ehat_(2) = "
      "Ehat_(3) = 0 separately; the Kasner fibers have Ehat_(2)^x1_x1 = %s != 0, and an exponential fiber a4 = A H x4, "
      "b4 = E^(beta A H x4) is never Ricci-flat (Ehat_(1)^(0) = %s); so the warped metric has no vacuum history of the "
      "author's theory with b4 not constant: a history needs a source (section 9)" % (s(e2k), s(r00)))
print("t", round(time.time() - T0, 1), flush=True)

# ---- 8. the source of the record's history a4 = A H x4, b4 = b4(0) E^(beta A H x4)
srcE = {}
srcA = {}
for mu in range(8):
    e = reduce_patch(E_w[1][(mu, mu)]).subs(hist)
    srcE[mu] = sp.factor(sp.simplify(e))
    tot = sum(aw[al] * reduce_patch(E_w[k][(mu, mu)]).subs(hist) for k, al in ((1, al1), (2, al2), (3, al3)))
    srcA[mu] = sp.factor(sp.expand(sp.simplify(tot)))
hist43 = {A: 1, be: sp.Rational(4, 3)}
names = {0: "p0", 1: "p3", 4: "-rho", 5: "p_t"}
RESULTS["history_source"] = {
    "history": "a4 = A H x4, b4 = b4(0) E^(beta A H x4); record values A = 1, beta = 4/3",
    "einstein_kappaT_minus_Lambda": {names[m]: s(srcE[m]) for m in (0, 1, 4, 5)},
    "einstein_A1_beta43": {names[m]: s(sp.expand(srcE[m].subs(hist43))) for m in (0, 1, 4, 5)},
    "author_weights_kappaT_minus_Lambda": {names[m]: s(srcA[m]) for m in (0, 1, 4, 5)},
    "author_weights_A1_beta43": {names[m]: s(sp.expand(srcA[m].subs(hist43))) for m in (0, 1, 4, 5)}}
ok = all(srcE[m] == srcE[mm] for m, mm in ((1, 2), (1, 3), (5, 6), (5, 7))) and \
    all(not srcE[m].has(x4) for m in range(8))
check("history_source_einstein", ok,
      "Einstein gravity on the history: kappa T^mu_nu - Lambda delta = 21 H^2 delta + Sin[z]^(-1/3) Ghat^mu_nu, constant "
      "in x4, diagonal, isotropic in 3-space and in the extra times; at A = 1, beta = 4/3: %s" % s(
          RESULTS["history_source"]["einstein_A1_beta43"]))
print("t", round(time.time() - T0, 1), flush=True)

# conservation of the diagonal source with x0-dependent entries, from the warped Christoffel symbols
g_w = [sp.sympify(v) for v in G_WARPED]
Gw = christoffel(g_w, X)
f = {m: sp.Function("T%d" % m)(X[0], X[4]) for m in (0, 1, 4, 5)}
Tdiag = [f[0], f[1], f[1], f[1], f[4], f[5], f[5], f[5]]


def Gm(a, b, c):
    return Gw.get((a, b, c), 0)


div = []
for nu in range(8):
    v = sp.diff(Tdiag[nu], X[nu])
    v += sum(Gm(m, m, nu) * Tdiag[nu] for m in range(8))
    v -= sum(Gm(m, m, nu) * Tdiag[m] for m in range(8))
    div.append(sp.simplify(v))
nonzero = [nu for nu in range(8) if div[nu] != 0]
ok = nonzero == [0, 4]
# the history source satisfies both
for which, src in (("einstein", srcE), ("author", srcA)):
    sub = {}
    for m in (0, 1, 4, 5):
        e = src[m].subs(hist43)
        e = e.subs(W, sp.sin(z) ** sp.Rational(-1, 3)).subs(cc, sp.cot(z))
        sub[f[m]] = e
    on_history = {a4f: H * X[4], b4f: sp.exp(sp.Rational(4, 3) * H * X[4])}
    for nu in (0, 4):
        val = div[nu].subs(sub).subs(on_history).doit()
        val = sp.simplify(normal(val))
        if val != 0:
            ok = False
            print("divergence", which, nu, val)
check("history_source_conserved", ok,
      "for a diagonal T = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) with entries depending on x0 and x4 the warped "
      "metric gives nabla_mu T^mu_nu = 0 identically for nu != x0, x4; nabla_mu T^mu_x4 = 0 and nabla_mu T^mu_x0 = 0 "
      "hold for the history's source (Einstein and the author's weights, A = 1, beta = 4/3), as the Bianchi identity "
      "requires")
RESULTS["divergence_of_diagonal_tensor"] = {"x4": s(div[4]), "x0": s(div[0])}
print("t", round(time.time() - T0, 1), flush=True)

# ---- 9. the gravity term of the Dirac operator: gamma^mu Omega_mu = (1/2) sum_a gamma^(a) (1/sqrt g) d_a(sqrt g/f_a)
fw = [sp.cot(z), sp.exp(a4f) * sp.sin(z) ** sp.Rational(1, 6), sp.exp(a4f) * sp.sin(z) ** sp.Rational(1, 6),
      sp.exp(a4f) * sp.sin(z) ** sp.Rational(1, 6), sp.sin(z) ** sp.Rational(1, 6),
      sp.exp(-a4f) * sp.sqrt(b4f) * sp.sin(z) ** sp.Rational(1, 6), sp.exp(-a4f) * sp.sqrt(b4f) * sp.sin(z) ** sp.Rational(1, 6),
      sp.exp(-a4f) * sp.sqrt(b4f) * sp.sin(z) ** sp.Rational(1, 6)]
vol = sp.prod(fw)
coef = [sp.simplify(sp.Rational(1, 2) * sp.diff(vol / fw[a], X[a]) / vol) for a in range(8)]
c0 = normal(coef[0])
c4 = normal(coef[4])
ok = all(coef[a] == 0 for a in (1, 2, 3, 5, 6, 7)) and sp.simplify(c0 - sp.Rational(7, 2) * H) == 0 and \
    is_zero(c4 - sp.Rational(3, 4) * bd1 / bb * sp.sqrt(W))
check("dirac_gravity_term", ok,
      "warped metric, diagonal vielbein f = (Cot[z], E^a4 Sin[z]^(1/6) (x3), Sin[z]^(1/6), E^-a4 b4^(1/2) Sin[z]^(1/6) "
      "(x3)): gamma^mu Omega_mu = (7/2) H gamma^(x0) + (3/4) (b4'/b4) Sin[z]^(-1/6) gamma^(x4) (the metric of 2026-10-14: "
      "3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4))")
RESULTS["dirac_gravity_term"] = "(7/2) H gamma^(x0) + (3/4) (b4'/b4) Sin[6 H x0]^(-1/6) gamma^(x4)"
RESULTS["vielbein_diagonal"] = [s(v) for v in fw]
print("t", round(time.time() - T0, 1), flush=True)

# ---- 10. the earlier vacuum of the author (b4 = 1, a4 = H x4) is not a solution of the warped metric
sub_old = {ad1: H, ad2: 0, bb: 1, bd1: 0, bd2: 0}
lay = levels(sum(aw[al] * E_w[k][(4, 4)] for k, al in ((1, al1), (2, al2), (3, al3))))
lay = {kk: sp.simplify(v.subs(sub_old)) for kk, v in lay.items()}
ok = any(v != 0 for kk, v in lay.items() if kk > 0)
check("earlier_vacuum_not_warped_solution", ok,
      "the author's earlier vacuum (b4 = 1, a4 = H x4, weights 1, 1/32, 1/1152) has in the warped metric the x4x4 "
      "layers %s (powers of W = Sin[z]^(-1/3)): the layers with W do not vanish, so it is not a vacuum solution of the "
      "warped metric (that solution was a solution of the earlier metric, b4 = 1, which the user withdrew)" % s(lay))

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
