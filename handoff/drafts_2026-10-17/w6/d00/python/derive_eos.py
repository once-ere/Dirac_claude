"""Revision dark sector, dirac16complex00 (Hypothesis00, SPEC sections 8 and 11): implementation A.

Exact derivations (sympy) first, then the key numbers of the models from the exact closed forms
(mpmath, 30 digits).  Writes
  <out>/eos-theory.json                 formulas, models, key numbers
  <out>/reports/python-derive-eos.json  every check with name, verdict and detail
Usage: python derive_eos.py [--out DIR]   (default: the folder Revision/dark_sector/dirac16complex00)
Deterministic: two runs give byte-identical files.

Inputs (Revision outputs only): Revision/algebra/gammas.json (the author's T16 in the author's
coordinate order) and Revision/field_equations_a4/a4-equations.json (keys generalSource, exponentialHistory, fields:
the field equations of the corrected metric for a general source).

The metric is the corrected primordial metric of 2026-10-16 (version 2; Revision/SPEC.md section 1), in the author's
coordinates X = {x0, ..., x7}: g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)),
z = 6 H x0 real.  b4 is a FUNCTION of x4.  The history of the numbers: a4 = H x4 and b4 = e^{(4/3) H x4} (beta = d ln b4/d
a4 = 4/3), the record's history (Revision/kohn_sham/ks-theory.json adiabaticity.historyBeta), a PRESCRIBED background: with
the author's weights it needs the source exponentialHistory.authorWeights.historySource_kappaT_minus_Lam of
a4-equations.json.  Every real z: the x0 dependence enters through C = cot z (signed) and W = (sin^2 z)^{1/12} with
dC/dx0 = -6 H (1 + C^2), dW/dx0 = H C W.
"""

import argparse
import json
import os
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OWN = os.path.normpath(os.path.join(HERE, ".."))
REV = os.environ.get("REVISION_DIR") or os.path.normpath(os.path.join(OWN, "..", ".."))
GAMMAS = os.path.join(REV, "algebra", "gammas.json")
A4EQ = os.path.join(REV, "field_equations_a4", "a4-equations.json")

mp.mp.dps = 30

BETA = sp.Rational(4, 3)      # d ln b4/d a4 on the history (b4 ~ a^(4/3))
BETA_MP = mp.mpf(4) / 3
SHIFT_N2 = -(4 - 2 * BETA) / 3          # w_eff(N2) - w_eff(N1) = -4/9 on the history
SHIFT_N2_MP = -(4 - 2 * BETA_MP) / 3

# The Supernovae Unite values of the author's private PDF (SPEC section 8).
W_CONST = sp.Rational(-764, 1000)
UNITE_W0_MP = mp.mpf("-0.861")
W0_U = sp.Rational(-861, 1000)
WA_U = sp.Rational(-60, 100)

CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})


def num(x, digits=12):
    """Deterministic decimal string of a number."""
    return mp.nstr(mp.mpf(x) if not isinstance(x, mp.mpf) else x, digits)


def sstr(e):
    return sp.sstr(e)


def q2mp(r):
    r = sp.Rational(r)
    return mp.mpf(int(r.p)) / int(r.q)


def inertia(Hm):
    """Exact inertia (n+, n-, n0) of a Hermitian matrix: its characteristic polynomial has real roots
    only, so Descartes' rule of signs counts the positive and the negative roots exactly."""
    lam = sp.Symbol("lam")
    cp = sp.Poly(sp.expand(Hm.charpoly(lam).as_expr()), lam)
    coeffs = [sp.nsimplify(c) for c in cp.all_coeffs()]
    assert all(sp.im(c) == 0 for c in coeffs)

    def changes(cs):
        cs = [c for c in cs if c != 0]
        return sum(1 for u, v in zip(cs, cs[1:]) if (u > 0) != (v > 0))

    n = len(coeffs) - 1
    n0 = 0
    while n0 < n and coeffs[n - n0] == 0:
        n0 += 1
    npos = changes(coeffs)
    neg = [c * (-1) ** (n - i) for i, c in enumerate(coeffs)]
    nneg = changes(neg)
    return npos, nneg, n0


# ----------------------------------------------------------------------------------------------
# gammas (own loader; exact)
# ----------------------------------------------------------------------------------------------

def _q(x):
    return sp.Rational(x) if isinstance(x, str) else sp.Integer(x)


def _m(rows):
    if isinstance(rows, dict):
        return _m(rows["re"]) + sp.I * _m(rows["im"])
    return sp.Matrix([[_q(x) for x in r] for r in rows])


def load_gammas():
    with open(GAMMAS, encoding="utf-8") as fh:
        d = json.load(fh)
    g = [_m(x) for x in d["gamma"]]  # g[k] = gamma^(xk), k = 0..7 (the author's order; x0 the hidden direction)
    eta = [int(x) for x in d["eta"]]
    return g, eta


# ----------------------------------------------------------------------------------------------
# A1. Conservation identities, re-derived from the author's metric
# ----------------------------------------------------------------------------------------------

def christoffel_diag(gd, X, D):
    """Christoffel symbols of a diagonal metric gd; D(e, mu) is the partial derivative along X[mu]"""
    n = len(gd)
    G = [[[0] * n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for m_ in range(n):
            for k in range(n):
                val = 0
                if l == k:
                    val += D(gd[l], m_)
                if l == m_:
                    val += D(gd[l], k)
                if m_ == k:
                    val -= D(gd[m_], l)
                G[l][m_][k] = sp.simplify(val / (2 * gd[l])) if val != 0 else 0
    return G


def divergence_diag(G, P, D):
    n = len(P)
    out = []
    for nu in range(n):
        e = D(P[nu], nu)
        for mu in range(n):  # diagonal T: Gamma^mu_{mu nu} (P_nu - P_mu)
            e += G[mu][mu][nu] * (P[nu] - P[mu])
        out.append(sp.simplify(e))
    return out


def section_conservation():
    xs = sp.symbols("x0:8", real=True)          # the author's coordinates x0, x1, ..., x7 (index k = xk)
    x4, x0 = xs[4], xs[0]
    H = sp.Symbol("H", positive=True)
    a4 = sp.Function("a4", real=True)(x4)
    b4 = sp.Function("b4", positive=True)(x4)
    u = sp.diff(b4, x4) / b4
    Cc = sp.Symbol("C", real=True)              # cot z, signed (every real z)
    Ww = sp.Symbol("W", positive=True)          # (sin^2 z)^(1/12)

    def D(e, mu):
        if mu == 0:
            return sp.diff(e, x0) + sp.diff(e, Cc) * (-6 * H * (1 + Cc ** 2)) + sp.diff(e, Ww) * (H * Cc * Ww)
        if mu == 4:
            return sp.diff(e, x4)
        return sp.Integer(0)
    gd = ([sp.exp(-2 * a4) * b4 * Cc ** 2] + [sp.exp(2 * a4)] * 3 + [-1] + [-sp.exp(-2 * a4) * b4 * Ww ** 2] * 3)
    G = christoffel_diag(gd, xs, D)
    P = [sp.Function("P%d" % i)(x4, x0) for i in range(8)]  # P[k] = T^xk_xk, P4 = -rho
    div = divergence_diag(G, P, D)
    rho = -P[4]
    h4 = u / 2 - sp.diff(a4, x4)
    exp4 = (-sp.diff(rho, x4) - sp.diff(a4, x4) * (3 * rho + P[1] + P[2] + P[3])
            - h4 * (4 * rho + P[0] + P[5] + P[6] + P[7]))
    exp0 = sp.diff(P[0], x0) + H * Cc * sum(P[0] - P[i] for i in (5, 6, 7))
    ok4 = sp.simplify(div[4] - exp4) == 0
    ok0 = sp.simplify(div[0] - exp0) == 0 and not div[0].has(b4) and not div[0].has(a4)
    okrest = all(sp.simplify(div[i]) == 0 for i in (1, 2, 3, 5, 6, 7))
    wrong4 = -sp.diff(rho, x4) - sp.diff(a4, x4) * (3 * rho + P[1] + P[2] + P[3])
    check("conservation_negative_control", sp.simplify(div[4] - wrong4) != 0,
          "control: the x4 identity WITHOUT the expansion of the hidden direction and the extra times (rate h4 = b4'/(2 b4) - "
          "a4') is NOT satisfied (the comparison is not vacuous)")
    check("conservation_x4_corrected_metric", ok4,
          "nabla_mu T^mu_x4 = -d4 rho - a4' (3 rho + p1 + p2 + p3) - h4 (4 rho + p0 + p5 + p6 + p7), h4 = b4'/(2 b4) - a4', "
          "for a diagonal T(x4, x0), Christoffel symbols computed here from the corrected metric (every real z)")
    check("conservation_x0_corrected_metric", ok0,
          "nabla_mu T^mu_x0 = d0 p0 + H cot z sum_(t = x5, x6, x7) (p0 - p_t), free of a4 and b4 (3-space carries no warp); "
          "isotropic: d0 p0 + 3 H cot z (p0 - p_t)")
    check("conservation_other_components_vanish", okrest,
          "nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7 (every b4)")
    # the local model: the warp of the extra times and the cot of the hidden direction frozen
    gl = [sp.exp(-2 * a4) * b4] + [sp.exp(2 * a4)] * 3 + [-1] + [-sp.exp(-2 * a4) * b4] * 3
    Dl = lambda e, mu: sp.diff(e, xs[mu])  # noqa: E731
    Gl = christoffel_diag(gl, xs, Dl)
    divl = divergence_diag(Gl, P, Dl)
    okl = sp.simplify(divl[4] - exp4) == 0 and sp.simplify(divl[0] - sp.diff(P[0], x0)) == 0
    check("conservation_x4_local_model", okl,
          "local model (warp and cot z frozen at a fixed hidden position): the same x4 identity; nabla_mu T^mu_x0 = d0 p0")
    sqrtg_l = sp.sqrt(sp.Abs(sp.prod(gl)))
    check("local_model_volume", sp.simplify(sqrtg_l - sp.exp(-a4) * b4 ** 2) == 0,
          "local model: sqrt|g| = e^(-a4) b4^2: the proper 7-volume of a comoving cell changes with x4 like e^(-a4) b4^2 "
          "(e^((5/3) a4) on the history beta = 4/3)")
    return {
        "x4": "nabla_mu T^mu_x4 = -d4 rho - a4' (3 rho + p1 + p2 + p3) - h4 (4 rho + p0 + p5 + p6 + p7), h4 = b4'/(2 b4) - a4'  (isotropic: -d4 rho - 3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t))",
        "x0": "nabla_mu T^mu_x0 = d0 p0 + H cot z sum_{t in x5,x6,x7} (p0 - p_t)  (isotropic: d0 p0 + 3 H cot z (p0 - p_t)); no a4, b4",
        "others": "nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7 (diagonal T depending on x4, x0)",
        "homogeneous": "d rho / d x4 = -3 a4' (rho + p3) - 4 h4 (rho + p0) and p0 = p_t (x0-independent source)",
        "localModelVolume": "sqrt|g| = e^(-a4) b4^2",
    }


# ----------------------------------------------------------------------------------------------
# A2. Observer normalisations
# ----------------------------------------------------------------------------------------------

def section_observer():
    x4 = sp.Symbol("x4", real=True)
    a4 = sp.Function("a4")(x4)
    b4 = sp.Function("b4", positive=True)(x4)
    rho = sp.Function("rho")(x4)
    P3 = sp.Function("P3")(x4)   # P3 = p1 + p2 + p3
    Pt = sp.Function("Pt")(x4)   # Pt = p5 + p6 + p7
    P0 = sp.Function("P0")(x4)   # p0
    ad = sp.diff(a4, x4)
    bt = sp.Symbol("beta", real=True)   # beta = b4'/(a4' b4) = d ln b4/d a4
    h4 = sp.diff(b4, x4) / (2 * b4) - ad

    def weff(rho4):
        return -1 - sp.diff(rho4, x4) / (3 * rho4 * ad)

    sub = {sp.Derivative(rho, x4): -ad * (3 * rho + P3) - h4 * (4 * rho + P0 + Pt)}
    tob = {sp.Derivative(b4, x4): bt * ad * b4}
    wN1 = sp.simplify(sp.expand(weff(sp.exp(-4 * a4) * b4 ** 2 * rho).subs(sub)).subs(tob))
    wN2 = sp.simplify(sp.expand(weff(rho).subs(sub)).subs(tob))
    want1 = (P3 + (bt / 2 - 1) * (P0 + Pt)) / (3 * rho)
    ok1 = sp.simplify(wN1 - want1) == 0
    ok2 = sp.simplify(wN2 - (want1 - (4 - 2 * bt) / 3)) == 0
    check("observer_N1_weff_identity", ok1,
          "N1 (per unit coordinate volume of the extra times and the hidden direction, rho_4 = e^{-4 a4} b4^2 <rho>): w_eff = "
          "(p1+p2+p3 + (beta/2 - 1)(p0 + p5 + p6 + p7))/(3 rho) = w3 + (beta/2 - 1)(w0 + 3 w_t)/3 (isotropic), beta = d ln b4/d a4, "
          "using the exact x4 identity")
    check("observer_N2_weff_identity", ok2,
          "N2 (per unit proper 7-volume, rho_4 = <rho>): w_eff = w_eff(N1) - (4 - 2 beta)/3 (= w_eff(N1) - 4/9 on the history "
          "beta = 4/3)")
    # the weighted x0 average commutes with d/dx4 (the weight |cot z| |sin z|^(1/2) does not depend on x4)
    x0, H = sp.symbols("x0 H", positive=True)
    f = sp.Function("f")(x4, x0)
    wgt = sp.cot(6 * H * x0) * sp.sin(6 * H * x0) ** sp.Rational(1, 2)
    avg = sp.Integral(wgt * f, (x0, 0, sp.pi / (12 * H)))
    ok3 = sp.simplify(sp.diff(avg, x4) - sp.Integral(wgt * sp.diff(f, x4), (x0, 0, sp.pi / (12 * H)))) == 0
    check("observer_hidden_average_commutes", ok3,
          "<f> = int |cot z| |sin z|^(1/2) f dx0 over a quarter of the period: d<f>/dx4 = <d4 f> (the weight does not depend on "
          "x4), so the identities hold for the hidden-direction averages")
    return {
        "a": "a = e^{a4}: the 3-space scale factor (no warp); c = e^{-a4} b4^{1/2} the scale factor of the extra times and of the hidden direction (b4 ~ a^(4/3) on the history: c ~ a^(-1/3))",
        "average": "<f>(x4) = int |cot z| |sin z|^(1/2) f dx0 (the proper-volume weight is sqrt|g| = e^{-a4} b4^2 |cot z| |sin z|^(1/2); its a4, b4 factor is written out in rho_4 below)",
        "N1": "per unit COORDINATE volume of the extra times and the hidden direction: rho_4 = e^{-4 a4} b4^2 <rho> (integrate over their proper volume e^{-4 a4} b4^2 |cot z| |sin z|^(1/2) per unit coordinate volume)",
        "N2": "per unit PROPER 7-volume: rho_4 = <rho>/<1>",
        "compactness": "a compact coordinate range of the time-like x5, x6, x7 means closed time-like directions; a non-compact range needs a normalisation per unit extra-time volume (N1 or N2). Both are ASSUMPTIONS about the 3-space observer, not consequences of the field equations",
        "w_eff": "w_eff = -1 - (1/3) d ln rho_4 / d ln a, d/d ln a = (1/a4') d/dx4",
        "N1_result": "w_eff(N1) = (p1+p2+p3 + (beta/2 - 1)(p0 + p5 + p6 + p7))/(3 rho) = w3 + (beta/2 - 1)(w0 + 3 w_t)/3 (isotropic)",
        "N2_result": "w_eff(N2) = w_eff(N1) - (4 - 2 beta)/3 (beta = 4/3 on the history: w_eff(N1) - 4/9)",
        "ratio": "w = p3/rho (the 3-space pressure over the energy density; independent of the normalisation)",
        "reading": "INTERPRETATION: a 3-space observer who uses the 4-dimensional Friedmann equations infers w_eff from the dilution of rho_4 (this is what supernova distances measure); w = p3/rho is the 3-space pressure ratio. They agree only if no energy is exchanged with the extra times and the hidden direction (p0 = p_t = 0 under N1)",
    }


# ----------------------------------------------------------------------------------------------
# A3. The homogeneous condensate
# ----------------------------------------------------------------------------------------------

def section_condensate(g):
    M, H, m, lam, S = sp.symbols("M H m lambda S", real=True)
    g4, g0 = g[4], g[0]
    C = g[0] * g[1] * g[2] * g[3]
    I16 = sp.eye(16)
    ub, ad = sp.symbols("u a4p", real=True)       # u = b4'/b4, a4p = a4'
    cg = sp.Symbol("c_g", positive=True)            # (3/2) H e^{a4} b4^{-1/2}, a positive scalar on a slice
    B = -M * g4 + cg * g4 * g0
    A = B - (ub - ad / 2) * I16
    ok_S = (C * A + A.T * C + 2 * (ub - ad / 2) * C).expand() == sp.zeros(16)
    K4mat = ((C * g4 * A - A.T * C * g4) / 2).expand()
    ok_K4 = (K4mat - M * C).expand() == sp.zeros(16)
    rec = json.load(open(A4EQ, encoding="utf-8"))
    hc = rec["fields"]["dirac16complex00"]["homogeneousCondensate"]
    stated = ("A = B - (b4'/b4 - a4'/2) I16" in hc and "(3/2) H e^{a4} b4^{-1/2} gamma^x4 gamma^x0" in hc
              and "S = e^{a4} b4^{-2} S0 (exact)" in hc)
    check("condensate_S_T16", ok_S and stated,
          "Phi(x4) on shell in the corrected metric (a4-equations.json fields.dirac16complex00.homogeneousCondensate): d4 Phi = A "
          "Phi, A = B - (b4'/b4 - a4'/2) I16, B = -M gamma^(x4) + (3/2) H e^(a4) b4^(-1/2) gamma^(x4) gamma^(x0), M = m + U'(S); "
          "C A + A^T C = -2 (b4'/b4 - a4'/2) C (author's T16, for every value of the coefficient of gamma^(x4) gamma^(x0)), so "
          "d S/dx4 = -2 (b4'/b4 - a4'/2) S: S = S0 e^(a4) b4^(-2) (S Vol_7 constant); the record states the same: %s" % stated)
    check("condensate_negative_control", (K4mat + M * C).expand() != sp.zeros(16) and (C * A + A.T * C).expand() != sp.zeros(16),
          "controls: K_x4 is not -M S, and C A + A^T C is not zero for b4'/b4 != a4'/2 (S is not constant)")
    check("condensate_K4_equals_MS_T16", ok_K4,
          "K_x4 = (1/2)(Phibar gamma^(x4) d4 Phi - d4 Phibar gamma^(x4) Phi) = M S exactly (matrix identity (C g4 A - A^T C g4)/2 = "
          "M C, for every coefficient of the gravity term); all other K_mu = 0")
    U = lam * S ** 2 / 2
    rho = m * S + U
    p = (m + lam * S) * S - m * S - U
    ok_p = sp.simplify(p - lam * S ** 2 / 2) == 0
    w = sp.simplify(p / rho)
    check("condensate_rho_p_w", ok_p and sp.simplify(w - lam * S / (2 * m + lam * S)) == 0,
          "rho = m S + lambda S^2/2, p3 = p_t = p0 = lambda S^2/2 with S = S0 e^(a4) b4^(-2), w = p/rho = lambda S/(2 m + lambda S) "
          "at each instant")
    # observer: N1 rho_4 = e^{-4 a4} b4^2 rho, N2 rho_4 = rho; on b4 ~ e^{beta a4}: S = S0 e^{(1 - 2 beta) a4}
    bt = sp.Symbol("beta", real=True)
    S0, A4v = sp.symbols("S0 a4", real=True)
    Sa = S0 * sp.exp((1 - 2 * bt) * A4v)
    rho_a = (m * S + U).subs(S, Sa)
    p_a = (lam * S ** 2 / 2).subs(S, Sa)
    rho4_N1 = sp.exp((2 * bt - 4) * A4v) * rho_a
    wN1 = sp.simplify(-1 - sp.diff(sp.log(rho4_N1), A4v) / 3)
    wN2 = sp.simplify(-1 - sp.diff(sp.log(rho_a), A4v) / 3)
    w_a = sp.simplify(p_a / rho_a)
    ok_obs = sp.simplify(wN1 - (2 * bt - 1) / 3 * w_a) == 0 and sp.simplify(wN2 - ((2 * bt - 1) / 3 * w_a - (4 - 2 * bt) / 3)) == 0
    dw = sp.simplify(sp.diff(w_a, A4v))
    ok_dw = sp.simplify(dw - ((1 - 2 * bt) * 2 * m * lam * Sa / (2 * m + lam * Sa) ** 2)) == 0
    check("condensate_observer", ok_obs and ok_dw,
          "with S = S0 e^(a4) b4^(-2) and b4 ~ e^(beta a4): w_eff(N1) = ((2 beta - 1)/3) w, w_eff(N2) = ((2 beta - 1)/3) w - "
          "(4 - 2 beta)/3, and the ratio drifts, d w/d a4 = (1 - 2 beta) 2 m lambda S/(2 m + lambda S)^2 (beta = 4/3: "
          "lambda S/m ~ e^(-(5/3) a4); w_eff(N1) = (5/9) w, w_eff(N2) = (5/9) w - 4/9)")
    x = sp.Symbol("x", real=True)  # x = lambda S/(2 m)
    wx = x / (1 + x)
    phantom_set = sp.solve_univariate_inequality(wx < -1, x, relational=False)
    ok_ph = phantom_set == sp.Interval.open(-1, sp.Rational(-1, 2))
    check("condensate_phantom_interval", ok_ph,
          "w = x/(1+x) with x = lambda S/(2 m): w < -1 exactly for x in (-1, -1/2), i.e. lambda S/m in (-2, -1); there rho = m S "
          "(1 + x) has the sign of m S and p = m S x the opposite sign; since w_eff(N2) = (5/9)(w + 1) - 1 at beta = 4/3, the "
          "observer reads w_eff(N2) < -1 exactly in the same window")
    xU = sp.solve(sp.Eq(wx, W_CONST), x)[0]
    check("condensate_ratio_equals_unite_constant_w", xU == sp.Rational(-191, 441),
          "w = -0.764 at x = -191/441, i.e. lambda S/m = -382/441 = -0.866213... at that instant; rho > 0 then needs m S > 0 and "
          "lambda < 0 (U = lambda S^2/2 < 0); the ratio then drifts (condensate_observer)")
    xs_ = -sp.Rational(382, 441)
    wa_ratio = sp.nsimplify(-(1 - 2 * BETA) * 2 * xs_ / (2 + xs_) ** 2)
    wa_general = sp.simplify(-((1 - 2 * BETA) * 2 * m * lam * S / (2 * m + lam * S) ** 2).subs(lam, xs_ * m / S))
    check("condensate_ratio_drift_at_unite_value", sp.simplify(wa_ratio - wa_general) == 0 and wa_ratio < 0,
          "beta = 4/3: lambda S/m = u ~ e^(-(5/3) a4), so the ratio u/(2 + u) has wa = -dw/da4 = (10/3) u/(2 + u)^2 = %s = %s at "
          "u = -382/441 (thawing sign); w_eff(N1) = (5/9) w and w_eff(N2) = (5/9) w - 4/9 then have wa = %s"
          % (sstr(wa_ratio), num(q2mp(wa_ratio)), num(q2mp(sp.Rational(5, 9) * wa_ratio))))
    # the source the record's history needs with the author's weights (a4-equations.json exponentialHistory.authorWeights,
    # historySource_kappaT_minus_Lam: the left-hand sides with Lambda removed, functions of kk = e^{(2/3) H x4})
    aw = rec["exponentialHistory"]["authorWeights"]
    kk = sp.Symbol("kk", positive=True)
    src = {k: sp.sympify(aw["historySource_kappaT_minus_Lam"][k]["input"].replace("^", "**"), locals={"kk": kk})
           for k in ("minus_rho", "p3", "p0", "pt")}
    aniso = sp.expand(src["p3"] - src["p0"])
    poly_nonzero = sp.Poly(aniso, kk).is_zero is False
    hist_ok = "be = 4/3" in aw["recordHistory"] and src["p0"] == src["pt"]
    check("history_required_source", hist_ok and poly_nonzero,
          "the record's history a4 = H x4, b4 = e^((4/3) H x4) with the author's weights needs the diagonal, x0-independent source of "
          "a4-equations.json exponentialHistory.authorWeights.historySource_kappaT_minus_Lam (kappa T - Lambda delta, kk = "
          "e^((2/3) H x4)): -kappa rho - Lambda = %s, kappa p3 - Lambda = %s, kappa p0 - Lambda = kappa p_t - Lambda = %s; it is "
          "anisotropic: kappa (p3 - p0) = %s" % (sstr(src["minus_rho"]), sstr(src["p3"]), sstr(src["p0"]), sstr(aniso)))
    check("condensate_cannot_source_history", poly_nonzero,
          "every homogeneous condensate (any m, lambda, S0) has p3 = p_t = p0 = lambda S^2/2, while the history needs kappa (p3 - p0) "
          "= %s, a nonzero polynomial in kk: no condensate is the source of the record's history (exact); in addition its S ~ "
          "e^(-(5/3) a4) = kk^(-5/2) decays while the required source grows with kk" % sstr(aniso))
    return {
        "solution": "Phi = e^{a4/2} b4^{-1} chi, chi' = B chi, B = -M gamma^(x4) + (3/2) H e^{a4} b4^{-1/2} gamma^(x4) gamma^(x0), M = m + lambda S, S = S0 e^{a4} b4^{-2} (S Vol_7 constant; re-verified here: C A + A^T C = -2 (b4'/b4 - a4'/2) C, K_x4 = M S)",
        "rho": "m S + lambda S^2/2, S = S0 e^{a4} b4^{-2}", "p": "p3 = p_t = p0 = lambda S^2/2",
        "w_ratio": "lambda S/(2 m + lambda S) at each instant; w < -1 iff lambda S/m in (-2, -1); lambda S/m ~ e^(-(5/3) a4) on the history",
        "w_eff_N1": "((2 beta - 1)/3) w = (5/9) w", "w_eff_N2": "((2 beta - 1)/3) w - (4 - 2 beta)/3 = (5/9) w - 4/9",
        "CPL": "the ratio has wa = (10/3) u/(2 + u)^2, u = lambda S/m (beta = 4/3); w_eff(N1), w_eff(N2): (5/9) of it",
        "unite_constant_w_by_ratio": "lambda S/m = -382/441 at one instant (rho > 0: m S > 0, lambda < 0); then wa = %s" % num(q2mp(wa_ratio)),
        "historyRequiredSource": {k: sstr(v) for k, v in src.items()} | {
            "meaning": "kappa T - Lambda delta (Lambda = -10), the author's weights w1 = 1, w2 = 1/32, w3 = 1/1152, history a4 = H x4, b4 = e^((4/3) H x4), kk = e^((2/3) H x4)"},
        "selfConsistency": "no condensate is the source of the record's history: it is isotropic (p3 = p0) and decays, the required source is anisotropic and grows",
        "expansion_inferred_w": "the observer reads a = e^{a4}: w_exp = -1 - (2/3) a4''/a4'^2 = -1 exactly on a4 = H x4, for every b4(x4)",
    }


# ----------------------------------------------------------------------------------------------
# A4. Plane waves in the frozen (local) frame: Krein-signed energies, growing modes
# ----------------------------------------------------------------------------------------------

def mode_matrices(g, m, k, q):
    g1, g4, g5 = g[1], g[4], g[5]
    C = g[0] * g[1] * g[2] * g[3]
    B = -sp.I * C * g4
    h = -sp.I * m * g4 - k * g4 * g1 - q * g4 * g5
    return C, B, h


def section_modes(g):
    out = {"generator": "plane wave Phi = u exp(i (k x1 + q x5 - omega x4)) with physical (frozen-frame) momenta k (3-space) and q (extra time): omega u = h u, h = -i m gamma^(x4) - k gamma^(x4) gamma^(x1) - q gamma^(x4) gamma^(x5); h^2 = (m^2 + k^2 - q^2) I16; B h is Hermitian (h is B-self-adjoint)", "cases": []}
    m, k, q = sp.symbols("m k q", real=True)
    C, B, h = mode_matrices(g, m, k, q)
    okh2 = (h * h - (m ** 2 + k ** 2 - q ** 2) * sp.eye(16)).expand() == sp.zeros(16)
    okB = ((B * h) - (B * h).H).expand() == sp.zeros(16)
    check("mode_dispersion_h_squared", okh2, "h^2 = (m^2 + k^2 - q^2) I16: omega^2 = m^2 + k_phys^2 - q_phys^2 (the extra times are time-like: q enters with the opposite sign)")
    check("mode_generator_B_selfadjoint", okB, "B h = (B h)^dagger: the charge density Q = Phi^dagger B Phi is the Krein form of the frozen-frame evolution and is conserved by it (in the field theory the charge obeys a local conservation law; its total is constant only without flux through z = pi/2, an ASSUMED condition)")
    g1, g5 = g[1], g[5]
    for (mv, kv, qv) in [(3, 4, 0), (5, 0, 3), (4, 4, 4)]:
        Cm, Bm, hm = mode_matrices(g, sp.Integer(mv), sp.Integer(kv), sp.Integer(qv))
        om = sp.sqrt(mv ** 2 + kv ** 2 - qv ** 2)
        rec = {"m": mv, "k": kv, "q": qv, "omega": str(om)}
        for sgn in (1, -1):
            w_ = sgn * om
            P = sp.Matrix.hstack(*(hm - w_ * sp.eye(16)).nullspace())
            gram = (P.H * Bm * P).expand()
            pos, neg, _ = inertia(gram)
            # energy-momentum on the eigenspace: rho = -K1 - K5 + m S, p1 = L0 - K1, p5 = L0 - K5, L0 = K1 + K4 + K5 - m S
            K1 = sp.I * kv * Cm * g1
            K5 = sp.I * qv * Cm * g5
            K4 = w_ * Bm
            L0 = K1 + K4 + K5 - mv * Cm
            rhoM = -K1 - K5 + mv * Cm
            p1M = L0 - K1
            p5M = L0 - K5
            z16 = sp.zeros(P.shape[1])
            ok_rho = (P.H * (rhoM - w_ * Bm) * P).expand() == z16
            ok_L0 = (P.H * L0 * P).expand() == z16
            ok_p1 = (P.H * (p1M - sp.Rational(kv ** 2) / w_ * Bm) * P).applyfunc(sp.simplify) == z16
            ok_p5 = (P.H * (p5M + sp.Rational(qv ** 2) / w_ * Bm) * P).applyfunc(sp.simplify) == z16
            tag = "m%d_k%d_q%d_%s" % (mv, kv, qv, "pos" if sgn > 0 else "neg")
            if (mv, kv, qv, sgn) == (3, 4, 0, 1):
                check("mode_emt_negative_control", (P.H * (rhoM + w_ * Bm) * P).expand() != z16 and (P.H * Bm * P).expand() != z16,
                      "controls on the omega = 5 eigenspace: rho is not -omega Q, and the Krein form is not zero there")
            check("mode_krein_inertia_" + tag, P.shape[1] == 8 and pos == 4 and neg == 4,
                  "eigenspace omega = %s: dimension %d, Krein form u^dagger B u of signature (%d, %d)" % (w_, P.shape[1], pos, neg))
            check("mode_emt_" + tag, ok_rho and ok_L0 and ok_p1 and ok_p5,
                  "on the eigenspace exactly: rho = omega Q, L0 = 0, p1 = k^2 Q/omega, p5 = -q^2 Q/omega, Q = u^dagger B u (T^mu_nu = k^mu k_nu Q/omega); "
                  "energy sign = sign(omega) sign(Q): both signs at every real frequency")
            rec["omega_%s" % ("pos" if sgn > 0 else "neg")] = {"dimension": P.shape[1], "krein_signature": [pos, neg]}
        out["cases"].append(rec)
    # growing mode: q^2 > m^2 + k^2
    mv, kv, qv = 3, 0, 5
    Cm, Bm, hm = mode_matrices(g, sp.Integer(mv), sp.Integer(kv), sp.Integer(qv))
    w_ = 4 * sp.I  # omega = 4 i: Phi ~ exp(4 x4), growing
    P = sp.Matrix.hstack(*(hm - w_ * sp.eye(16)).nullspace())
    z8 = sp.zeros(P.shape[1])
    gram = (P.H * Bm * P).expand()
    # complex omega: K4 = Re(omega) u^dagger B u = 0
    K5 = sp.I * qv * Cm * g5
    Sform = (P.H * Cm * P).expand()
    ok_neutral = gram == z8
    ok_K5 = (P.H * (K5 - mv * Cm) * P).expand() == z8  # on shell sum K = m S, K1 = K4 = 0
    ok_S_nonzero = Sform != z8
    check("growing_mode_krein_neutral", P.shape[1] == 8 and ok_neutral,
          "m = 3, k = 0, q = 5: omega = 4 i (growth exp(4 x4)); the growing eigenspace has dimension 8 and is Krein-neutral (Q = 0), so K_x4 = Re(omega) Q = 0 and rho = 0")
    check("growing_mode_extra_time_pressure", ok_K5 and ok_S_nonzero,
          "on the growing eigenspace K_x5 = m S exactly (on shell), so rho = 0, p1 = p0 = L0 = 0 and p5 = -m S, which grows as exp(8 x4) and is not identically zero: w = p/rho is undefined; the energy of a growing mode sits in cross terms with decaying modes")
    out["growing"] = {"m": mv, "k": kv, "q": qv, "omega": "4 i", "result": "Krein-neutral 8-dimensional eigenspace; rho = 0, p5 = -m S (growing), p1 = p0 = 0"}
    out["rate"] = "frozen frame: growth rate sqrt(q_phys^2 - m^2 - k_phys^2) for q_phys^2 > m^2 + k_phys^2; in the deflating field q_phys = q e^{a4} b4^(-1/2) grows (as a^(1/3) on the history b4 ~ a^(4/3)), so every q != 0 mode reaches a turning point a_* and then grows"
    return out


# ----------------------------------------------------------------------------------------------
# A5. Adiabatic (WKB) mode gases in the deflating local model
# ----------------------------------------------------------------------------------------------

def section_wkb():
    x4 = sp.Symbol("x4", real=True)
    a4 = sp.Function("a4")(x4)
    b4 = sp.Function("b4", positive=True)(x4)
    m, k, q, Q = sp.symbols("m k q Q", real=True)
    a = sp.exp(a4)
    om = sp.sqrt(m ** 2 + k ** 2 / a ** 2 - q ** 2 * a ** 2 / b4)
    nb = sp.exp(a4) * b4 ** -2           # per proper volume: the proper 7-volume of a comoving cell grows like e^{-a4} b4^2
    rho = om * Q * nb
    p3 = k ** 2 / (3 * a ** 2 * om) * Q * nb
    pt = -q ** 2 * a ** 2 / (3 * b4 * om) * Q * nb
    h4 = sp.diff(b4, x4) / (2 * b4) - sp.diff(a4, x4)
    ok = sp.simplify(sp.diff(rho, x4) + 3 * sp.diff(a4, x4) * (rho + p3) + h4 * rho + 3 * h4 * (rho + pt)) == 0
    check("wkb_mode_gas_conservation", ok,
          "rho = omega Q n, p3 = k^2 Q n/(3 a^2 omega), p_t = -q^2 a^2 Q n/(3 b4 omega), p0 = 0, n = e^(a4) b4^(-2), omega^2 = m^2 + "
          "k^2/a^2 - q^2 a^2/b4 (comoving k, q, no hidden momentum; Q the Krein charge per comoving coordinate volume, constant as "
          "an adiabatic invariant) satisfy d rho/dx4 = -3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t) exactly")
    bt = sp.Symbol("beta", real=True)
    eps = sp.simplify((3 * p3 + (bt / 2 - 1) * (0 + 3 * pt)) / (3 * rho))
    ok2 = sp.simplify(eps - (k ** 2 / a ** 2 + (1 - bt / 2) * q ** 2 * a ** 2 / b4) / (3 * om ** 2)) == 0
    check("wkb_epsilon_sign_free", ok2,
          "w_eff(N1) of one component = eps = (k_p^2 + (1 - beta/2) q_p^2)/(3 omega^2), k_p = k/a, q_p = q a b4^(-1/2): independent of the Krein charge Q, and eps >= 0 for real omega when beta < 2 (beta = 4/3 on the history: eps = (k_p^2 + q_p^2/3)/(3 omega^2))")
    # mixture identity
    n = 3
    rs = sp.symbols("r1:%d" % (n + 1), real=True)
    es = sp.symbols("e1:%d" % (n + 1), real=True)
    # from rho_4(N1) of each component: d ln(e^{-4 a4} b4^2 rho_i)/d a4 = -3 (1 + eps_i), so
    # d ln rho_i/d a4 = 1 - 2 beta - 3 eps_i
    wN2 = -1 - sp.Rational(1, 3) * sum((1 - 2 * bt - 3 * e) * r for e, r in zip(es, rs)) / sum(rs)
    ok3 = sp.simplify(wN2 - (-(4 - 2 * bt) / 3 + sum(e * r for e, r in zip(es, rs)) / sum(rs))) == 0
    check("mixture_weighted_average", ok3,
          "mixture: w_eff(N1) = sum eps_i rho_i / sum rho_i, w_eff(N2) = -(4 - 2 beta)/3 + sum eps_i rho_i / sum rho_i (condensates "
          "with lambda = 0 have eps = 0)")
    return {
        "approximation": "ADIABATIC (WKB) local plane-wave modes at a fixed hidden position, with no hidden momentum: the warp (sin^2 z)^{1/12} and cot z frozen (wavelengths short compared with the warp scale 1/H; the gravity terms are absent in the half-density variables), the Krein charge of each mode an adiabatic invariant (|d omega/dx4| << omega^2); incoherent superposition (cross terms between different momenta average to zero over 3-space and the extra times; cross terms between frequencies average to zero in time)",
        "component": "rho = omega Q n, p3 = k^2 Q n/(3 a^2 omega), p_t = -q^2 a^2 Q n/(3 b4 omega), p0 = 0, n = e^{a4} b4^{-2}, omega^2 = m^2 + k^2/a^2 - q^2 a^2/b4 (isotropic averages)",
        "eps": "eps = w_eff(N1) = (k_p^2 + (1 - beta/2) q_p^2)/(3 omega^2) >= 0 for real omega and beta < 2",
        "mixture": "w_eff(N1) = sum eps_i rho_i / sum rho_i, w_eff(N2) = w_eff(N1) - (4 - 2 beta)/3, w = p3/rho = sum p3_i / sum rho_i",
        "theorem": "if every component has rho_i >= 0 (Krein charge of the sign of omega), real frequencies, and total rho > 0, then w_eff(N1) >= 0 and w_eff(N2) >= -(4 - 2 beta)/3 (= -4/9 on the history b4 ~ a^(4/3)) at every a at which these conditions hold (weighted averages of eps_i >= 0 with weights rho_i >= 0): no phantom, no crossing of -1, and no w_eff(N2) below -4/9 there. A mode with extra-time momentum q != 0 loses its real frequency past its turning point a_* (q_phys = q a b4^(-1/2) grows), where the theorem does not apply. Going below -(4 - 2 beta)/3 needs a component with rho_i < 0 (negative classical energy: a ghost-like sector)",
    }


# ----------------------------------------------------------------------------------------------
# A6. Models and key numbers
# ----------------------------------------------------------------------------------------------

AFIT = [mp.mpf(1) / 2, mp.mpf(1) / 3]
NFIT = 101


def lsq_cpl(f, amin):
    xs = [amin + (1 - amin) * mp.mpf(j) / (NFIT - 1) for j in range(NFIT)]
    ys = [f(x) for x in xs]
    us = [1 - x for x in xs]
    n = NFIT
    Su, Suu, Sy = mp.fsum(us), mp.fsum(u * u for u in us), mp.fsum(ys)
    Suy = mp.fsum(u * y for u, y in zip(us, ys))
    det = n * Suu - Su * Su
    w0 = (Suu * Sy - Su * Suy) / det
    wa = (n * Suy - Su * Sy) / det
    return w0, wa, Sy / n


def crossings(f, amin=mp.mpf(1) / 3, amax=mp.mpf(1), steps=400):
    out = []
    xs = [amin + (amax - amin) * mp.mpf(j) / steps for j in range(steps + 1)]
    vals = [f(x) + 1 for x in xs]
    for x0, x1, v0, v1 in zip(xs, xs[1:], vals, vals[1:]):
        if v0 * v1 < 0:
            out.append(mp.findroot(lambda t: f(t) + 1, (x0, x1), solver="bisect"))
    return out


class Model:
    """components: list of (kind, weight, params); rho per comoving coordinate cell, normalised so that the total is 1
    at a = 1.  On the history b4 ~ a^beta (beta = 4/3) every component's proper density carries the common factor
    e^{a4} b4^(-2), which cancels in w_eff(N1) and in the ratio; w_eff(N2) = w_eff(N1) - (4 - 2 beta)/3
    (mixture_weighted_average).
    The extra-time momentum is blueshifted as q_p = q a b4^(-1/2) ~ q a^(1 - beta/2), so a q-mode has
    omega^2 = m^2 (1 - s a^(2 - beta)), s = q_p^2/m^2 at a = 1."""

    def __init__(self, comps):
        self.comps = comps

    def parts(self, a):
        R = E = P3 = mp.mpf(0)
        ex = 2 - BETA_MP
        for kind, wgt, par in self.comps:
            if kind == "condensate":  # lambda = 0: E = m S0 per coordinate cell constant, P3 = Pt = P0 = 0
                r, e, p3 = wgt, mp.mpf(0), mp.mpf(0)
            elif kind == "kmode":  # q = 0, r_k = k^2/(k^2 + m^2) at a = 1 (does not feel b4)
                rk = par["r"]
                om2 = (rk / (1 - rk)) / a ** 2 + 1  # in units m = 1
                om2_1 = (rk / (1 - rk)) + 1
                r = wgt * mp.sqrt(om2 / om2_1)
                e = ((rk / (1 - rk)) / a ** 2) / (3 * om2)
                p3 = r * e
            elif kind == "qmode":  # k = 0, s = q_p^2/m^2 at a = 1; eps = (1 - beta/2) q_p^2/(3 omega^2)
                s = par["s"]
                r = wgt * mp.sqrt((1 - s * a ** ex) / (1 - s))
                e = (1 - BETA_MP / 2) * s * a ** ex / (3 * (1 - s * a ** ex))
                p3 = mp.mpf(0)
            elif kind == "ghost_radiation":  # massless k-mode of negative energy: rho = -G/a, eps = 1/3
                r = -wgt / a
                e = mp.mpf(1) / 3
                p3 = r / 3
            else:
                raise ValueError(kind)
            R += r
            E += e * r
            P3 += p3
        return R, E, P3

    def wN2(self, a):
        R, E, _ = self.parts(a)
        return SHIFT_N2_MP + E / R

    def wN1(self, a):
        R, E, _ = self.parts(a)
        return E / R

    def wratio(self, a):
        R, _, P3 = self.parts(a)
        return P3 / R


def tangent(f):
    return f(mp.mpf(1)), -mp.diff(f, mp.mpf(1))


def summarize(model, extra=None):
    res = {}
    for name, f in (("N2", model.wN2), ("N1", model.wN1), ("ratio_p3_over_rho", model.wratio)):
        w0, wa = tangent(f)
        r = {"w(a=1)": num(w0), "CPL_tangent": {"w0": num(w0), "wa": num(wa), "w0_plus_wa": num(w0 + wa)}}
        for amin in AFIT:
            fw0, fwa, cw = lsq_cpl(f, amin)
            key = "fit_a_%s_to_1" % ("1/2" if amin == mp.mpf(1) / 2 else "1/3")
            r[key] = {"w0": num(fw0), "wa": num(fwa), "constant_w": num(cw)}
        r["w_at"] = {lab: num(f(mp.mpf(av))) for lab, av in (("1/3", mp.mpf(1) / 3), ("1/2", mp.mpf(1) / 2), ("3/4", mp.mpf(3) / 4), ("1", 1))}
        cr = crossings(f)
        r["crossings_of_minus_1_in_[1/3,1]"] = [num(c) for c in cr]
        res[name] = r
    R13 = model.parts(mp.mpf(1) / 3)[0]
    res["rho_total_at_a_1/3"] = num(R13)
    if extra:
        res.update(extra)
    return res


def section_models():
    out = {}
    unite = {
        "constant_w": str(W_CONST), "w0": str(W0_U), "wa": str(WA_U),
        "deep_past_w0_plus_wa": str(W0_U + WA_U),
        "crossing_of_minus_1": {"a": str(1 + (1 + W0_U) / WA_U), "a_decimal": num(mp.mpf(461) / 600), "z": str(1 / (1 + (1 + W0_U) / WA_U) - 1)},
        "reading": "CPL w(a) = w0 + wa (1 - a); thawing means wa < 0 in this convention (w rises from below); the Unite line is phantom (w < -1) for a < 461/600",
    }
    ok_u = (1 + (1 + W0_U) / WA_U) == sp.Rational(461, 600)
    uline = lambda a: mp.mpf("-0.861") + mp.mpf("-0.60") * (1 - a)
    proxy = {}
    okp = True
    for amin, lab, exact in ((mp.mpf(1) / 2, "1/2", sp.Rational(-1011, 1000)), (mp.mpf(1) / 3, "1/3", sp.Rational(-1061, 1000))):
        fw0, fwa, cw = lsq_cpl(uline, amin)
        okp = okp and abs(fw0 + mp.mpf("0.861")) < mp.mpf("1e-25") and abs(fwa + mp.mpf("0.60")) < mp.mpf("1e-25") and abs(cw - q2mp(exact)) < mp.mpf("1e-25")
        proxy["fit_a_%s_to_1" % lab] = {"w0": num(fw0), "wa": num(fwa), "constant_w": num(cw)}
    check("unite_line_fit_proxy", okp,
          "the fit procedure applied to the Unite CPL line itself returns (w0, wa) = (-0.861, -0.60) and the constant w = -1.011 ([1/2, 1]) and -1.061 ([1/3, 1]): the constant-w proxy (mean of w(a)) is NOT the supernova constant-w fit -0.764, which weights the data")
    unite["fit_proxy_applied_to_the_unite_line"] = proxy
    check("unite_crossing_point", ok_u, "the Unite CPL line crosses w = -1 at a = 461/600 (z = 139/461 = 0.3015)")
    out["unite"] = unite
    # the models keep the physical parameters of the withdrawn b4 = 1 record (so that the effect of the metric is seen
    # directly); on the record's history of the corrected metric they give the numbers below
    third = sp.Rational(1, 3)
    # M1 condensate
    out["M1_condensate"] = {
        "content": "homogeneous condensate (exact solution for every a4, b4): S = S0 e^(a4) b4^(-2), u = lambda S/m ~ e^(-(5/3) a4) on the history",
        "N2": {"w": "-4/9 + (5/9) u/(2 + u)", "lambda_0": {"w0": "-4/9", "wa": "0"}},
        "N1": {"w": "(5/9) u/(2 + u)", "lambda_0": {"w0": "0", "wa": "0"}},
        "ratio": {"w": "u/(2 + u)", "CPL": {"w0": "u/(2 + u)", "wa": "(10/3) u/(2 + u)^2"}, "unite_constant_w": "u = -382/441 at one instant"},
    }
    # M2 positive good-sector k-mode gas (q = 0: does not feel b4), r = 417/1000 as in the withdrawn record
    r = sp.Rational(417, 1000)
    w0_2 = SHIFT_N2 + r / 3
    wa_exact = sp.Rational(2, 3) * r * (1 - r)
    m2 = Model([("kmode", mp.mpf(1), {"r": mp.mpf(417) / 1000})])
    w0n, wan = tangent(m2.wN2)
    check("M2_tangent_exact", abs(w0n - q2mp(w0_2)) < mp.mpf("1e-25") and abs(wan - q2mp(wa_exact)) < mp.mpf("1e-20"),
          "positive-energy good-sector gas (q = 0), k^2/(k^2+m^2) = 417/1000 at a = 1: N2 tangent (w0, wa) = (%s, %s) = (-4/9 + r/3, (2/3) r (1 - r)): FREEZING (wa > 0)" % (sstr(w0_2), sstr(wa_exact)))
    out["M2_positive_good_sector_gas"] = summarize(m2, {
        "content": "one isotropic shell of good-sector modes (q = 0) of positive energy, k^2/(k^2+m^2) = 417/1000 at a = 1",
        "N2_tangent_exact": {"w0": sstr(w0_2), "wa": sstr(wa_exact)},
        "N1_range": "w_eff(N1) = (1/3) k^2/(k^2 + m^2 a^2): from 1/3 (a -> 0) to 0 (a -> infinity): a time-varying DARK-MATTER-like equation of state, independent of b4",
    })
    # M3 positive q-mode alone, s = 417/1417 as in the withdrawn record
    s3 = sp.Rational(417, 1417)
    av = sp.Symbol("a", positive=True)
    eps3 = (1 - BETA / 2) * s3 * av ** (2 - BETA) / (3 * (1 - s3 * av ** (2 - BETA)))
    wN2_3 = SHIFT_N2 + eps3
    w0_3 = sp.nsimplify(wN2_3.subs(av, 1))
    wa3 = sp.nsimplify(-sp.diff(wN2_3, av).subs(av, 1))
    a_star3 = s3 ** (-sp.Rational(1, 1) / (2 - BETA))
    m3 = Model([("qmode", mp.mpf(1), {"s": mp.mpf(417) / 1417})])
    w0n, wan = tangent(m3.wN2)
    check("M3_tangent_exact", abs(w0n - q2mp(w0_3)) < mp.mpf("1e-25") and abs(wan - q2mp(wa3)) < mp.mpf("1e-20"),
          "positive-energy extra-time-momentum mode (k = 0), s = q_p^2/m^2 = 417/1417 at a = 1, omega^2 = m^2 (1 - s a^(2/3)): N2 tangent (w0, wa) = (%s, %s) = (%s, %s): w_eff(N2) = -4/9 + (1/9) s a^(2/3)/(1 - s a^(2/3)) >= -4/9; turning point a_* = s^(-3/2) = %s" % (sstr(w0_3), sstr(wa3), num(q2mp(w0_3)), num(q2mp(wa3)), num(mp.mpf(1417 / 417) ** mp.mpf(1.5))))
    out["M3_positive_extra_time_mode"] = summarize(m3, {
        "content": "one positive-energy mode with extra-time momentum q and k = 0, s = q_p^2/m^2 = 417/1417 at a = 1",
        "N2_tangent_exact": {"w0": sstr(w0_3), "wa": sstr(wa3), "wa_decimal": num(q2mp(wa3))},
        "turning_point_a_star": {"exact": "(1417/417)^(3/2)", "decimal": num((mp.mpf(1417) / 417) ** (mp.mpf(3) / 2))},
        "N2_formula": "w_eff(N2) = -4/9 + (1/9) s a^(2/3)/(1 - s a^(2/3)) >= -4/9 for a < a_* = s^(-3/2) (real frequency); past a_* the frequency is imaginary and the formula does not apply",
    })
    # M4 condensate + q-mode with the parameters of the withdrawn tuning (s = 264037/403037, Omega_q = 57963/264037)
    m4 = Model([("condensate", 1 - mp.mpf(57963) / 264037, {}), ("qmode", mp.mpf(57963) / 264037, {"s": mp.mpf(264037) / 403037})])
    w0n, wan = tangent(m4.wN2)
    a_star4 = (mp.mpf(403037) / 264037) ** (mp.mpf(3) / 2)
    minw = min(m4.wN2(mp.mpf(j) / 300) for j in range(1, 301))
    check("M4_former_tuning_on_the_history", minw >= SHIFT_N2_MP and w0n > UNITE_W0_MP,
          "condensate + positive q-mode with the parameters that gave the Unite tangent on the withdrawn b4 = 1 record (s = 264037/403037, Omega_q = 57963/264037): on the record's history its N2 tangent is (%s, %s), min of w_eff(N2) over a = 1/300 ... 1 is %s >= -4/9 (above the Unite w0 = -0.861); turning point a_* = s^(-3/2) = %s" % (num(w0n), num(wan), num(minw), num(a_star4)))
    out["M4_condensate_plus_extra_time_mode"] = summarize(m4, {
        "content": "positive condensate (lambda = 0) + positive extra-time-momentum mode (k = 0); fractions at a = 1: Omega_c = 1 - Omega_q, Omega_q = 57963/264037; s = q_p^2/m^2 = 264037/403037 (the parameters of the withdrawn b4 = 1 tuning to the Unite tangent)",
        "parameters": {"s": "264037/403037", "s_decimal": num(mp.mpf(264037) / 403037), "Omega_q": "57963/264037", "Omega_q_decimal": num(mp.mpf(57963) / 264037)},
        "turning_point_a_star": num(a_star4),
        "min_w_N2_on_(0,1]": num(minw),
    })
    # positive models are bounded below by -(4 - 2 beta)/3 = -4/9 under N2 (theorem of the section wkb)
    mins = [min(mod.wN2(mp.mpf(j) / 300) for j in range(1, 301)) for mod in (m2, m3, m4)]
    check("positive_models_bounded_by_minus_four_ninths", all(v >= SHIFT_N2_MP for v in mins),
          "M2, M3, M4 (positive components, real frequencies on a in (0, 1]): min of w_eff(N2) over a = 1/300 ... 1 = %s, all >= -(4 - 2 beta)/3 = -4/9: on the record's history no positive-energy model reaches the Unite w0 = -0.861 or crosses -1" % ", ".join(num(v) for v in mins))
    # the Unite w0 under N2 needs a ghost component: w_eff(N2)(1) >= -4/9 - G/3 (G = ghost fraction at a = 1)
    Gmin = 3 * (sp.Rational(861, 1000) + SHIFT_N2)
    a0 = Gmin / (1 + Gmin)
    check("unite_w0_requires_dominant_ghost", Gmin == sp.Rational(3749, 3000) and sp.Rational(1, 2) < a0 < 1,
          "a ghost component (massless good-sector modes of negative energy, rho_g = -G/a at a = 1, eps = 1/3) lowers w_eff(N2)(1) by G/3 at most and positive components raise it, so w_eff(N2)(1) = -0.861 needs G >= %s (the ghost energy exceeds the total); for condensate + ghost (Omega_c = 1 + G) the total energy (1 + G) - G/a vanishes at a = G/(1 + G) = %s inside [1/2, 1], where w_eff diverges: the Unite fit over [1/2, 1] is not reachable by such a model" % (sstr(Gmin), sstr(a0)))
    # M5: the composition of the withdrawn record (condensate + q-mode + ghost G = 3/10, its s and Omega_q)
    G = mp.mpf(3) / 10
    s5, Oq5 = mp.mpf("0.567762680825"), mp.mpf("0.594675195377")
    m5 = Model([("condensate", 1 - Oq5 + G, {}), ("qmode", Oq5, {"s": s5}), ("ghost_radiation", G, {})])
    fw0, fwa, _ = lsq_cpl(m5.wN2, mp.mpf(1) / 2)
    cr = crossings(m5.wN2)
    check("M5_former_composition_on_the_history", fw0 > UNITE_W0_MP,
          "condensate + positive q-mode + ghost radiation with the parameters of the withdrawn record (G = 3/10, s = 0.567762680825, Omega_q = 0.594675195377): on the record's history its N2 least-squares CPL fit over a in [1/2, 1] is (%s, %s) (w0 above the Unite -0.861); crossings of -1 in [1/3, 1]: %s" % (num(fw0), num(fwa), ", ".join(num(c) for c in cr) if cr else "none"))
    out["M5_with_ghost_component"] = summarize(m5, {
        "content": "positive condensate + positive extra-time mode + a GHOST component (massless good-sector modes of NEGATIVE classical energy, rho_g = -G/a, eps = 1/3), G = 3/10 of the total at a = 1, s = 0.567762680825, Omega_q = 0.594675195377 (the composition and parameters of the withdrawn b4 = 1 record)",
        "parameters": {"G": "3/10", "s": num(s5), "Omega_q": num(Oq5), "Omega_c": num(1 - Oq5 + G)},
        "turning_point_a_star": num(s5 ** (-mp.mpf(3) / 2)),
        "unite": "on the record's history the Unite w0 under N2 needs a ghost fraction G >= 3749/3000 (unite_w0_requires_dominant_ghost)",
    })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OWN)
    args = ap.parse_args()
    g, eta = load_gammas()
    ok_cl = all(((g[i] * g[j] + g[j] * g[i]) == (2 * eta[i] * sp.eye(16) if i == j else sp.zeros(16))) for i in range(8) for j in range(8))
    check("gammas_clifford_author_T16", ok_cl, "{gamma^a, gamma^b} = 2 eta^ab for the fixture Revision/algebra/gammas.json (eta = diag(+,+,+,+,-,-,-,-) in the author's order x0..x7)")
    win_in = mp.power(mp.mpf(382) / 441, mp.mpf(3) / 5)     # |u| = (382/441) a^(-5/3) reaches 1
    win_out = mp.power(mp.mpf(191) / 441, mp.mpf(3) / 5)    # |u| reaches 2: the condensate energy m S (1 + u/2) vanishes
    theory = {
        "title": "dirac16complex00 (classical commuting Pin(4,4) spinor): the 3-space observer's equation of state in the deflating primordial field (Hypothesis00; Revision/SPEC.md sections 8 and 11)",
        "producer": "Revision/dark_sector/dirac16complex00/python/derive_eos.py (implementation A: sympy exact, mpmath 30 digits)",
        "labels": "EXACT = verified by exact symbolic computation in the named checks; APPROXIMATION = stated approximation; ASSUMPTION = observer or model assumption; INTERPRETATION = reading, not a computed statement",
        "metric": "the corrected primordial metric of 2026-10-16 (version 2; Revision/SPEC.md section 1): g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real; b4 is a function of x4; the history of the numbers is the record's a4 = H x4, b4 = e^{(4/3) H x4} (beta = 4/3), a PRESCRIBED background (it needs the source exponentialHistory.authorWeights.historySource_kappaT_minus_Lam); the formulas hold for every a4(x4), b4(x4)",
        "beta": "d ln b4/d a4 = 4/3",
        "conservation": section_conservation(),
        "observer": section_observer(),
        "condensate": section_condensate(g),
        "modes": section_modes(g),
        "wkb": section_wkb(),
        "models": section_models(),
        "ghost": "INTERPRETATION (with the exact basis above): dirac16complex00 is a commuting field with a first-order Lagrangian; at every real frequency half of its modes (Krein charge of the opposite sign) carry negative classical energy, and its energy is unbounded below. Components of negative classical energy are a ghost-like sector. With positive-energy components of real frequency only (for an extra-time mode: before its turning point a_*), w_eff(N1) >= 0 and w_eff(N2) >= -4/9 on the record's history b4 ~ a^(4/3) (theorem of section wkb): no dark-energy value under either normalisation from such components; reaching the Unite w0 with them needs a ghost-like sector larger than the positive energy. The exception is a condensate with lambda < 0 and m S > 0 (positive energy, attractive self-interaction; not a mode gas): its ratio w is below -1 exactly while lambda S/m lies in (-2, -1) (condensate_phantom_interval), and because w_eff(N2) = (5/9)(1 + w) - 1 (condensate_observer) the observer then reads w_eff(N2) < -1 as well; on the history lambda S/m ~ e^(-(5/3) a4) drifts into that window toward the past (for lambda S/m = -382/441 today: from a = (382/441)^(3/5) = " + num(win_in) + " back to a = (191/441)^(3/5) = " + num(win_out) + ", where its energy m S (1 + lambda S/(2 m)) vanishes). Its value -382/441 is CHOSEN, and no source of the history selects a condensate (condensate_cannot_source_history).",
    }
    os.makedirs(os.path.join(args.out, "reports"), exist_ok=True)
    with open(os.path.join(args.out, "eos-theory.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(theory, fh, indent=2, sort_keys=True)
        fh.write("\n")
    npass = sum(c["verdict"] == "PASS" for c in CHECKS)
    report = {"producer": "Revision/dark_sector/dirac16complex00/python/derive_eos.py", "summary": "%d/%d checks pass" % (npass, len(CHECKS)), "checks": CHECKS}
    with open(os.path.join(args.out, "reports", "python-derive-eos.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(report, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print("derive_eos: %d/%d checks pass" % (npass, len(CHECKS)))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
