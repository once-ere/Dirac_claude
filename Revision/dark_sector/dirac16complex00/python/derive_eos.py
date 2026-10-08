"""Revision dark sector, dirac16complex00 (Hypothesis00, SPEC sections 8 and 11): implementation A.

Exact derivations (sympy) first, then the key numbers of the models from the exact closed forms
(mpmath, 30 digits).  Writes
  <out>/eos-theory.json                 formulas, models, key numbers
  <out>/reports/python-derive-eos.json  every check with name, verdict and detail
Usage: python derive_eos.py [--out DIR]   (default: the folder Revision/dark_sector/dirac16complex00)
Deterministic: two runs give byte-identical files.

Inputs (Revision outputs only): Revision/algebra/gammas.json (the author's T16 in the author's
coordinate order) and Revision/field_equations_a4/a4-equations.json (the linear member).
"""

import argparse
import json
import os
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OWN = os.path.normpath(os.path.join(HERE, ".."))
REV = os.path.normpath(os.path.join(OWN, "..", ".."))
GAMMAS = os.path.join(REV, "algebra", "gammas.json")
A4EQ = os.path.join(REV, "field_equations_a4", "a4-equations.json")

mp.mp.dps = 30

# The Supernovae Unite values of the author's private PDF (SPEC section 8).
W_CONST = sp.Rational(-764, 1000)
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
    g = [_m(x) for x in d["gamma"]]  # g[0..7] = gamma^(x1..x8)
    eta = [int(x) for x in d["eta"]]
    return g, eta


# ----------------------------------------------------------------------------------------------
# A1. Conservation identities, re-derived from the author's metric
# ----------------------------------------------------------------------------------------------

def christoffel_diag(gd, X):
    n = len(gd)
    G = [[[0] * n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for m_ in range(n):
            for k in range(n):
                val = 0
                if l == k:
                    val += sp.diff(gd[l], X[m_])
                if l == m_:
                    val += sp.diff(gd[l], X[k])
                if m_ == k:
                    val -= sp.diff(gd[m_], X[l])
                G[l][m_][k] = sp.simplify(val / (2 * gd[l])) if val != 0 else 0
    return G


def divergence_diag(G, P, X):
    n = len(P)
    out = []
    for nu in range(n):
        e = sp.diff(P[nu], X[nu])
        for mu in range(n):  # diagonal T: Gamma^mu_{mu nu} (P_nu - P_mu)
            e += G[mu][mu][nu] * (P[nu] - P[mu])
        out.append(sp.simplify(e))
    return out


def section_conservation():
    xs = sp.symbols("x1:9", real=True)
    x4, x8 = xs[3], xs[7]
    H = sp.Symbol("H", positive=True)
    a4 = sp.Function("a4")(x4)
    z = 6 * H * x8
    w6 = sp.sin(z) ** sp.Rational(1, 3)
    gd = [sp.exp(2 * a4) * w6] * 3 + [-1] + [-sp.exp(-2 * a4) * w6] * 3 + [sp.cot(z) ** 2]
    G = christoffel_diag(gd, xs)
    P = [sp.Function("P%d" % (i + 1))(x4, x8) for i in range(8)]  # T^mu_mu, P4 = -rho
    div = divergence_diag(G, P, xs)
    rho = -P[3]
    exp4 = -sp.diff(rho, x4) - sp.diff(a4, x4) * (P[0] + P[1] + P[2] - P[4] - P[5] - P[6])
    exp8 = sp.diff(P[7], x8) + H * sp.cot(z) * sum(P[7] - P[i] for i in (0, 1, 2, 4, 5, 6))
    ok4 = sp.simplify(div[3] - exp4) == 0
    ok8 = sp.simplify(sp.expand_trig(div[7] - exp8)) == 0
    okrest = all(sp.simplify(div[i]) == 0 for i in (0, 1, 2, 4, 5, 6))
    wrong4 = -sp.diff(rho, x4) + sp.diff(a4, x4) * (P[0] + P[1] + P[2] - P[4] - P[5] - P[6])
    check("conservation_negative_control", sp.simplify(div[3] - wrong4) != 0,
          "control: the x4 identity with the opposite sign of the exchange term is NOT satisfied (the comparison is not vacuous)")
    check("conservation_x4_author_metric", ok4,
          "nabla_mu T^mu_x4 = -d4 rho - a4' (p1 + p2 + p3 - p5 - p6 - p7) for a diagonal T(x4, x8), "
          "Christoffel symbols computed here from the author's metric")
    check("conservation_x8_author_metric", ok8,
          "nabla_mu T^mu_x8 = d8 p8 + H cot z sum_{6 directions} (p8 - p_dir); isotropic: d8 p8 + 3 H cot z (2 p8 - p3 - p_t)")
    check("conservation_other_components_vanish", okrest,
          "nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7")
    # the local model: the same metric with the warp sin^(1/6) z frozen (absorbed in the coordinates)
    gl = [sp.exp(2 * a4)] * 3 + [-1] + [-sp.exp(-2 * a4)] * 3 + [1]
    Gl = christoffel_diag(gl, xs)
    divl = divergence_diag(Gl, P, xs)
    okl = sp.simplify(divl[3] - exp4) == 0 and sp.simplify(divl[7] - sp.diff(P[7], x8)) == 0
    check("conservation_x4_local_model", okl,
          "local model (warp frozen at a fixed hidden position): the same x4 identity; nabla_mu T^mu_x8 = d8 p8")
    sqrtg_l = sp.sqrt(sp.Abs(sp.prod(gl)))
    check("local_model_volume_constant", sp.simplify(sqrtg_l - 1) == 0,
          "local model: sqrt|g| = 1, independent of x4 (3-space inflation e^{3 a4} compensated by the deflation e^{-3 a4})")
    return {
        "x4": "nabla_mu T^mu_x4 = -d4 rho - a4' (p1 + p2 + p3 - p5 - p6 - p7)  (isotropic: -d4 rho - 3 a4' (p3 - p_t))",
        "x8": "nabla_mu T^mu_x8 = d8 p8 + H cot z sum_{dir in x1,x2,x3,x5,x6,x7} (p8 - p_dir)  (isotropic: d8 p8 + 3 H cot z (2 p8 - p3 - p_t))",
        "others": "nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7 (diagonal T depending on x4, x8)",
        "homogeneous": "d rho / d x4 = -3 a4' (p3 - p_t) and p3 + p_t = 2 p8 (x8-independent source)",
    }


# ----------------------------------------------------------------------------------------------
# A2. Observer normalisations
# ----------------------------------------------------------------------------------------------

def section_observer():
    x4 = sp.Symbol("x4", real=True)
    a4 = sp.Function("a4")(x4)
    rho = sp.Function("rho")(x4)
    D = sp.Function("D")(x4)  # D = p1 + p2 + p3 - p5 - p6 - p7
    ad = sp.diff(a4, x4)

    def weff(rho4):
        return -1 - sp.diff(rho4, x4) / (3 * rho4 * ad)

    sub = {sp.Derivative(rho, x4): -ad * D}
    wN1 = sp.simplify(weff(sp.exp(-3 * a4) * rho).subs(sub))
    wN2 = sp.simplify(weff(rho).subs(sub))
    ok1 = sp.simplify(wN1 - D / (3 * rho)) == 0
    ok2 = sp.simplify(wN2 - (D / (3 * rho) - 1)) == 0
    check("observer_N1_weff_identity", ok1,
          "N1 (per unit extra-time coordinate volume, rho_4 = e^{-3 a4} <rho>): w_eff = (p1+p2+p3-p5-p6-p7)/(3 rho) = w3 - w_t (isotropic), "
          "using the exact conservation identity d rho/d x4 = -a4' (p1+p2+p3-p5-p6-p7)")
    check("observer_N2_weff_identity", ok2,
          "N2 (per unit proper 7-volume, rho_4 = <rho>): w_eff = -1 + (p1+p2+p3-p5-p6-p7)/(3 rho) = w_eff(N1) - 1")
    # the weighted x8 average commutes with d/dx4 (the weight cos z does not depend on x4)
    x8, H = sp.symbols("x8 H", positive=True)
    f = sp.Function("f")(x4, x8)
    avg = sp.Integral(sp.cos(6 * H * x8) * f, (x8, 0, sp.pi / (12 * H)))
    ok3 = sp.simplify(sp.diff(avg, x4) - sp.Integral(sp.cos(6 * H * x8) * sp.diff(f, x4), (x8, 0, sp.pi / (12 * H)))) == 0
    check("observer_hidden_average_commutes", ok3,
          "<f> = int cos z f dx8 over the patch: d<f>/dx4 = <d4 f>, so the identities hold for the hidden-direction averages")
    return {
        "a": "a = e^{a4}: the 3-space scale factor (up to the constant factor sin^{1/6} z at a fixed hidden position); c = e^{-a4} = 1/a the extra-time scale factor",
        "average": "<f>(x4) = int_0^{pi/(12 H)} cos z f dx8 (the proper-volume weight sqrt|g| = cos z; constant in x4)",
        "N1": "per unit extra-time COORDINATE volume: rho_4 = e^{-3 a4} <rho> (integrate over the proper extra-time volume e^{-3 a4} sin^{1/2} z d^3x_t per unit coordinate volume, divide by the 3-space volume); the SPEC section 11 choice rho_4 ~ rho_8 c^3",
        "N2": "per unit PROPER 7-volume: rho_4 = <rho>/<1> (equivalently: integrate over a FIXED proper extra-time volume, whose coordinate extent grows as e^{a4})",
        "compactness": "a compact coordinate range of the time-like x5, x6, x7 means closed time-like directions; a non-compact range needs a normalisation per unit extra-time volume (N1 or N2). Both are ASSUMPTIONS about the 3-space observer, not consequences of the field equations",
        "w_eff": "w_eff = -1 - (1/3) d ln rho_4 / d ln a, d/d ln a = (1/a4') d/dx4",
        "N1_result": "w_eff(N1) = (p1+p2+p3-p5-p6-p7)/(3 rho) = w3 - w_t (isotropic)",
        "N2_result": "w_eff(N2) = w_eff(N1) - 1 = -1 + w3 - w_t (isotropic)",
        "ratio": "w = p3/rho (the 3-space pressure over the energy density; independent of the normalisation, both being densities of the same volume)",
        "reading": "INTERPRETATION: a 3-space observer who uses the 4-dimensional Friedmann equations infers w_eff from the dilution of rho_4 (this is what supernova distances measure); w = p3/rho is the 3-space pressure ratio. They agree only if no energy is exchanged with the extra times (p_t = 0 under N1)",
    }


# ----------------------------------------------------------------------------------------------
# A3. The homogeneous condensate
# ----------------------------------------------------------------------------------------------

def section_condensate(g):
    M, H, m, lam, S = sp.symbols("M H m lambda S", real=True)
    g4, g8 = g[3], g[7]
    C = g[7] * g[0] * g[1] * g[2]
    I16 = sp.eye(16)
    A = -g4 * (M * I16 - 3 * H * g8)
    ok_S = (C * A + A.T * C).expand() == sp.zeros(16)
    K4mat = ((C * g4 * A - A.T * C * g4) / 2).expand()
    ok_K4 = (K4mat - M * C).expand() == sp.zeros(16)
    check("condensate_S_constant_T16", ok_S,
          "Phi(x4) on shell: d4 Phi = A Phi, A = -gamma^(x4) (M - 3 H gamma^(x8)), M = m + U'(S); C A + A^T C = 0 (author's T16), so S = Phibar Phi is constant")
    check("condensate_negative_control", (K4mat + M * C).expand() != sp.zeros(16) and (C * A - A.T * C).expand() != sp.zeros(16),
          "controls: K_x4 is not -M S, and C A - A^T C is not zero")
    check("condensate_K4_equals_MS_T16", ok_K4,
          "K_x4 = (1/2)(Phibar gamma^(x4) d4 Phi - d4 Phibar gamma^(x4) Phi) = M S exactly (matrix identity (C g4 A - A^T C g4)/2 = M C); all other K_mu = 0")
    U = lam * S ** 2 / 2
    rho = m * S + U
    p = (m + lam * S) * S - m * S - U
    ok_p = sp.simplify(p - lam * S ** 2 / 2) == 0
    w = sp.simplify(p / rho)
    check("condensate_rho_p_w", ok_p and sp.simplify(w - lam * S / (2 * m + lam * S)) == 0,
          "rho = m S + lambda S^2/2, p3 = p_t = p8 = lambda S^2/2 (constant), w = p/rho = lambda S/(2 m + lambda S)")
    # observer: constant rho -> N1: rho_4 ~ a^-3 -> w_eff = 0; N2: w_eff = -1
    x = sp.Symbol("x", real=True)  # x = lambda S/(2 m)
    wx = x / (1 + x)
    phantom_set = sp.solve_univariate_inequality(wx < -1, x, relational=False)
    ok_ph = phantom_set == sp.Interval.open(-1, sp.Rational(-1, 2))
    check("condensate_phantom_interval", ok_ph,
          "w = x/(1+x) with x = lambda S/(2 m): w < -1 exactly for x in (-1, -1/2), i.e. lambda S/m in (-2, -1); there rho = m S (1 + x) has the sign of m S and p = m S x the opposite sign")
    xU = sp.solve(sp.Eq(wx, W_CONST), x)[0]
    check("condensate_ratio_equals_unite_constant_w", xU == sp.Rational(-191, 441),
          "w = -0.764 at x = -191/441, i.e. lambda S/m = -382/441 = -0.866213...; rho > 0 then needs m S > 0 and lambda < 0 (U = lambda S^2/2 < 0); constant in time (wa = 0)")
    # linear member: kappa (rho + p) factorises; Einstein: rho + p = -6 (1 + A^2) H^2/kappa
    with open(A4EQ, encoding="utf-8") as fh:
        a4eq = json.load(fh)
    lm = a4eq["linearMember"]
    syms = {k: sp.Symbol(k, real=True) for k in ("AA", "H", "kappa", "Lam", "alpha1", "alpha2", "alpha3")}

    def parse(s):
        return sp.sympify(s.replace("^", "**"), locals=syms)

    AA, Hs, kap = syms["AA"], syms["H"], syms["kappa"]
    al1, al2, al3 = syms["alpha1"], syms["alpha2"], syms["alpha3"]
    rhoL, pL = parse(lm["rho"]["input"]), parse(lm["p"]["input"])
    ad = AA * Hs
    bracket = 6 * al1 - 48 * al2 * (ad ** 2 + 5 * Hs ** 2) + 432 * al3 * (ad ** 4 + 2 * ad ** 2 * Hs ** 2 + 5 * Hs ** 4)
    ok_fac = sp.expand(kap * (rhoL + pL) + (ad ** 2 + Hs ** 2) * bracket) == 0
    check("linear_member_rho_plus_p_factorises", ok_fac,
          "from a4-equations.json (linearMember): kappa (rho + p) = -(a4'^2 + H^2) [6 alpha1 - 48 alpha2 (a4'^2 + 5 H^2) + 432 alpha3 (a4'^4 + 2 a4'^2 H^2 + 5 H^4)] at a4' = A H")
    rhoE, pE = parse(lm["rhoEinstein"]["input"]), parse(lm["pEinstein"]["input"])
    okE = sp.simplify(rhoE + pE + 6 * (1 + AA ** 2) * Hs ** 2 / kap) == 0
    check("linear_member_einstein_phantom_ratio", okE,
          "Einstein: rho + p = -6 (1 + A^2) H^2/kappa < 0 (kappa > 0); a self-consistent condensate source with rho > 0 therefore has w = p/rho = -1 - 6 (1 + A^2) H^2/(kappa rho) < -1 (phantom in the RATIO sense), constant in x4")
    # expansion-inferred w of the 3-space observer for the backreacted homogeneous Einstein case
    x4 = sp.Symbol("x4", real=True)
    a4 = sp.Function("a4")(x4)
    rho_f = sp.Function("rho")(x4)
    Df = sp.Function("Dp")(x4)  # p3 - p_t
    Lam = syms["Lam"]
    h2 = -(kap * rho_f + Lam + 21 * Hs ** 2) / 3  # constraint: 3 a4'^2 + 21 H^2 + Lambda = -kappa rho
    dh2 = sp.diff(h2, x4).subs(sp.Derivative(rho_f, x4), -3 * sp.Symbol("ad1") * Df)
    wtot = sp.simplify(-1 - dh2 / (3 * h2 * sp.Symbol("ad1")))
    ok_wt = sp.simplify(wtot - (-1 - kap * Df / (3 * h2))) == 0
    check("expansion_inferred_w_einstein", ok_wt,
          "backreacted homogeneous source, Einstein gravity: a4'^2 = -(kappa rho + Lambda + 21 H^2)/3, so the observer's Hubble rate gives w_tot = -1 - (1/3) d ln a4'^2/d ln a = -1 - kappa (p3 - p_t)/(3 a4'^2); the linear member (a4'' = 0) gives w_tot = -1 exactly")
    return {
        "solution": "Phi = exp(A x4) chi, A = -gamma^(x4) (M - 3 H gamma^(x8)), M = m + lambda S, S = chi^dagger C chi constant (Revision/field_equations_a4 record; re-verified here: C A + A^T C = 0, K_x4 = M S)",
        "rho": "m S + lambda S^2/2 (constant)", "p": "p3 = p_t = p8 = lambda S^2/2 (constant)",
        "w_ratio": "lambda S/(2 m + lambda S) (constant; any value; w < -1 iff lambda S/m in (-2, -1))",
        "w_eff_N1": "0 (rho_4 ~ a^-3: dust-like dilution)", "w_eff_N2": "-1 (rho_4 constant: Lambda-like)",
        "CPL": "wa = 0 in all three definitions (no time dependence)",
        "unite_constant_w_by_ratio": "lambda S/m = -382/441 (rho > 0: m S > 0, lambda < 0)",
        "linear_member_rho_plus_p": "kappa (rho + p) = -(a4'^2 + H^2) [6 alpha1 - 48 alpha2 (a4'^2 + 5 H^2) + 432 alpha3 (a4'^4 + 2 a4'^2 H^2 + 5 H^4)], a4' = A H",
        "einstein": "rho + p = -6 (1 + A^2) H^2/kappa: rho > 0 gives w = -1 - 6 (1 + A^2) H^2/(kappa rho) < -1 (constant); with alpha2, alpha3 the bracket can change sign",
        "expansion_inferred_w": "Einstein, backreacted homogeneous source: w_tot = -1 - kappa (p3 - p_t)/(3 a4'^2); for the condensate p3 = p_t: a4 linear, w_tot = -1 exactly (constant 3-space Hubble rate A H)",
    }


# ----------------------------------------------------------------------------------------------
# A4. Plane waves in the frozen (local) frame: Krein-signed energies, growing modes
# ----------------------------------------------------------------------------------------------

def mode_matrices(g, m, k, q):
    g1, g4, g5 = g[0], g[3], g[4]
    C = g[7] * g[0] * g[1] * g[2]
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
    check("mode_generator_B_selfadjoint", okB, "B h = (B h)^dagger: the conserved charge Q = Phi^dagger B Phi is the Krein form of the evolution")
    g1, g5 = g[0], g[4]
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
          "on the growing eigenspace K_x5 = m S exactly (on shell), so rho = 0, p1 = p8 = L0 = 0 and p5 = -m S, which grows as exp(8 x4) and is not identically zero: w = p/rho is undefined; the energy of a growing mode sits in cross terms with decaying modes")
    out["growing"] = {"m": mv, "k": kv, "q": qv, "omega": "4 i", "result": "Krein-neutral 8-dimensional eigenspace; rho = 0, p5 = -m S (growing), p1 = p8 = 0"}
    out["rate"] = "frozen frame: growth rate sqrt(q_phys^2 - m^2 - k_phys^2) for q_phys^2 > m^2 + k_phys^2; in the deflating field q_phys = e^{a4} q grows, so every q != 0 mode reaches the turning point a_* = sqrt((m^2 + ...)/q^2) and then grows (rate proportional to a, double-exponential amplitude for a4 linear in x4)"
    return out


# ----------------------------------------------------------------------------------------------
# A5. Adiabatic (WKB) mode gases in the deflating local model
# ----------------------------------------------------------------------------------------------

def section_wkb():
    x4 = sp.Symbol("x4", real=True)
    a4 = sp.Function("a4")(x4)
    m, k, q, Q = sp.symbols("m k q Q", real=True)
    a = sp.exp(a4)
    om = sp.sqrt(m ** 2 + k ** 2 / a ** 2 - q ** 2 * a ** 2)
    rho = om * Q
    p3 = k ** 2 / (3 * a ** 2 * om) * Q
    pt = -q ** 2 * a ** 2 / (3 * om) * Q
    ok = sp.simplify(sp.diff(rho, x4) + 3 * sp.diff(a4, x4) * (p3 - pt)) == 0
    check("wkb_mode_gas_conservation", ok,
          "rho = omega Q, p3 = k^2 Q/(3 a^2 omega), p_t = -q^2 a^2 Q/(3 omega), omega^2 = m^2 + k^2/a^2 - q^2 a^2 (comoving k, q; Q the conserved Krein charge per comoving volume) satisfy d rho/dx4 = -3 a4' (p3 - p_t) exactly")
    eps = sp.simplify((p3 - pt) / rho)
    ok2 = sp.simplify(eps - (k ** 2 / a ** 2 + q ** 2 * a ** 2) / (3 * om ** 2)) == 0
    check("wkb_epsilon_sign_free", ok2,
          "w_eff(N1) of one component = eps = (k^2/a^2 + q^2 a^2)/(3 omega^2): independent of the Krein charge Q, and eps >= 0 for real omega")
    # mixture identity
    n = 3
    rs = sp.symbols("r1:%d" % (n + 1), real=True)
    es = sp.symbols("e1:%d" % (n + 1), real=True)
    # with d rho_i/d ln a = -3 e_i rho_i:
    wN2 = -1 - sp.Rational(1, 3) * sum(-3 * e * r for e, r in zip(es, rs)) / sum(rs)
    ok3 = sp.simplify(wN2 - (-1 + sum(e * r for e, r in zip(es, rs)) / sum(rs))) == 0
    check("mixture_weighted_average", ok3,
          "mixture: w_eff(N2) = -1 + sum eps_i rho_i / sum rho_i, w_eff(N1) = sum eps_i rho_i / sum rho_i (condensates have eps = 0)")
    return {
        "approximation": "ADIABATIC (WKB) local plane-wave modes at a fixed hidden position: the warp sin^{1/6} z and tan z frozen (wavelengths short compared with the warp scale 1/H; in the variables chi = sin^{1/2} z Phi the term 3 H gamma^(x8) is absent exactly), the Krein charge of each mode an adiabatic invariant (|d omega/dx4| << omega^2); incoherent superposition (cross terms between different momenta average to zero over 3-space and the extra times; cross terms between frequencies average to zero in time)",
        "component": "rho = omega Q, p3 = k^2 Q/(3 a^2 omega), p_t = -q^2 a^2 Q/(3 omega), p8 = 0, omega^2 = m^2 + k^2/a^2 - q^2 a^2 (isotropic averages)",
        "eps": "eps = w_eff(N1) = (k^2/a^2 + q^2 a^2)/(3 omega^2) >= 0 for real omega",
        "mixture": "w_eff(N1) = sum eps_i rho_i / sum rho_i, w_eff(N2) = w_eff(N1) - 1, w = p3/rho = sum p3_i / sum rho_i",
        "theorem": "if every component has rho_i >= 0 (Krein charge of the sign of omega), real frequencies, and total rho > 0, then w_eff(N1) >= 0 and w_eff(N2) >= -1 at every a (weighted averages of eps_i >= 0 with weights rho_i >= 0): no phantom and no crossing of -1. A crossing needs sum eps_i rho_i to change sign, i.e. a component with rho_i < 0 (negative classical energy: a ghost-like sector)",
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
    """components: list of (kind, weight, params); rho normalised so that rho_tot(1) = 1."""

    def __init__(self, comps):
        self.comps = comps

    def parts(self, a):
        R = E = P3 = mp.mpf(0)
        for kind, wgt, par in self.comps:
            if kind == "condensate":  # rho constant, eps = 0, p3 = 0 (lambda = 0)
                r, e, p3 = wgt, mp.mpf(0), mp.mpf(0)
            elif kind == "kmode":  # q = 0, r_k = k^2/(k^2 + m^2) at a = 1
                rk = par["r"]
                om2 = (rk / (1 - rk)) / a ** 2 + 1  # in units m = 1
                om2_1 = (rk / (1 - rk)) + 1
                r = wgt * mp.sqrt(om2 / om2_1)
                e = ((rk / (1 - rk)) / a ** 2) / (3 * om2)
                p3 = r * e
            elif kind == "qmode":  # k = 0, s = q^2/m^2 at a = 1
                s = par["s"]
                r = wgt * mp.sqrt((1 - s * a * a) / (1 - s))
                e = s * a * a / (3 * (1 - s * a * a))
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
        return -1 + E / R

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
    # M1 condensate
    out["M1_condensate"] = {
        "content": "homogeneous condensate (exact solution for every a4); lambda S/m free",
        "N2": {"w": "-1", "CPL": {"w0": "-1", "wa": "0"}},
        "N1": {"w": "0", "CPL": {"w0": "0", "wa": "0"}},
        "ratio": {"w": "lambda S/(2 m + lambda S) (constant)", "CPL": {"w0": "lambda S/(2 m + lambda S)", "wa": "0"}, "unite_constant_w": "lambda S/m = -382/441"},
    }
    # M2 positive good-sector k-mode gas, N2 w0 matched
    r = sp.Rational(417, 1000)  # k^2/(k^2+m^2) at a = 1 gives 1 + w0(N2) = r/3 = 0.139
    wa_exact = sp.Rational(2, 3) * r * (1 - r)
    m2 = Model([("kmode", mp.mpf(1), {"r": mp.mpf(417) / 1000})])
    w0n, wan = tangent(m2.wN2)
    check("M2_tangent_exact", abs(w0n - mp.mpf("-0.861")) < mp.mpf("1e-25") and abs(wan - q2mp(wa_exact)) < mp.mpf("1e-20"),
          "positive-energy good-sector gas (q = 0), k^2/(k^2+m^2) = 417/1000 at a = 1: N2 tangent (w0, wa) = (-0.861, %s) = (-0.861, (2/3) r (1 - r)): FREEZING (wa > 0)" % sstr(wa_exact))
    out["M2_positive_good_sector_gas"] = summarize(m2, {
        "content": "one isotropic shell of good-sector modes (q = 0) of positive energy, k^2/(k^2+m^2) = 417/1000 at a = 1 (chosen so that w_eff(N2)(1) = -0.861)",
        "N2_tangent_exact": {"w0": "-861/1000", "wa": sstr(wa_exact)},
        "N1_range": "w_eff(N1) = (1/3) k^2/(k^2 + m^2 a^2): from 1/3 (a -> 0) to 0 (a -> infinity): a time-varying DARK-MATTER-like equation of state",
    })
    # M3 positive q-mode alone, N2 w0 matched
    s3 = sp.Rational(417, 1417)
    wa3 = -sp.Rational(2, 3) * s3 / (1 - s3) ** 2
    m3 = Model([("qmode", mp.mpf(1), {"s": mp.mpf(417) / 1417})])
    w0n, wan = tangent(m3.wN2)
    check("M3_tangent_exact", abs(w0n - mp.mpf("-0.861")) < mp.mpf("1e-25") and abs(wan - q2mp(wa3)) < mp.mpf("1e-20"),
          "positive-energy extra-time-momentum mode (k = 0), s = q^2/m^2 = 417/1417 at a = 1: N2 tangent (w0, wa) = (-0.861, %s): THAWING (wa < 0), w -> -1 from above as a -> 0" % sstr(wa3))
    out["M3_positive_extra_time_mode"] = summarize(m3, {
        "content": "one positive-energy mode with extra-time momentum q and k = 0, s = q^2/m^2 = 417/1417 at a = 1 (w_eff(N2)(1) = -0.861)",
        "N2_tangent_exact": {"w0": "-861/1000", "wa": sstr(wa3), "wa_decimal": num(q2mp(wa3))},
        "turning_point_a_star": {"exact": "sqrt(1417/417)", "decimal": num(mp.sqrt(mp.mpf(1417) / 417))},
        "N2_formula": "w_eff(N2) = -1 + (1/3) s a^2/(1 - s a^2) >= -1",
    })
    # M4 condensate + q-mode, N2 tangent = Unite
    c = sp.Rational(600, 139) - sp.Rational(417, 1000)
    s4 = sp.nsimplify((c - 2) / (c - 1))
    Oq4 = sp.Rational(417, 1000) * (1 - s4) / s4
    check("M4_parameters_exact", s4 == sp.Rational(264037, 403037) and Oq4 == sp.Rational(57963, 264037),
          "condensate + positive q-mode with N2 tangent equal to Unite: s = 264037/403037, Omega_q = 57963/264037 (exact solution of the two tangent conditions)")
    m4 = Model([("condensate", 1 - mp.mpf(57963) / 264037, {}), ("qmode", mp.mpf(57963) / 264037, {"s": mp.mpf(264037) / 403037})])
    w0n, wan = tangent(m4.wN2)
    check("M4_tangent_equals_unite", abs(w0n - mp.mpf("-0.861")) < mp.mpf("1e-25") and abs(wan - mp.mpf("-0.60")) < mp.mpf("1e-20"),
          "N2 tangent of M4 = (-0.861, -0.600) = the Unite CPL values; yet w_eff(N2) >= -1 at every a (theorem: positive components), no crossing: the phantom past of the CPL line is not reproduced")
    minw = min(m4.wN2(mp.mpf(j) / 300) for j in range(1, 301))
    check("M4_never_phantom", minw >= -1, "min of w_eff(N2) over a = 1/300 ... 1 is %s >= -1" % num(minw))
    out["M4_condensate_plus_extra_time_mode"] = summarize(m4, {
        "content": "positive condensate (lambda = 0, rho constant) + positive extra-time-momentum mode (k = 0); fractions at a = 1: Omega_c = 1 - Omega_q, Omega_q = 57963/264037; s = q^2/m^2 = 264037/403037; the two parameters solve N2 tangent = (-0.861, -0.60) exactly",
        "parameters": {"s": "264037/403037", "s_decimal": num(mp.mpf(264037) / 403037), "Omega_q": "57963/264037", "Omega_q_decimal": num(mp.mpf(57963) / 264037)},
        "turning_point_a_star": num(1 / mp.sqrt(mp.mpf(264037) / 403037)),
        "min_w_N2_on_(0,1]": num(minw),
    })
    # M5 ghost: condensate + positive q-mode + ghost radiation (G = 3/10); CPL fit over [1/2, 1] = Unite
    G = mp.mpf(3) / 10

    def F(s, Oq):
        mod = Model([("condensate", 1 - Oq + G, {}), ("qmode", Oq, {"s": s}), ("ghost_radiation", G, {})])
        fw0, fwa, _ = lsq_cpl(mod.wN2, mp.mpf(1) / 2)
        return [fw0 - mp.mpf("-0.861"), fwa - mp.mpf("-0.60")]

    s5, Oq5 = mp.findroot(F, (mp.mpf("0.5678"), mp.mpf("0.5947")))
    m5 = Model([("condensate", 1 - Oq5 + G, {}), ("qmode", Oq5, {"s": s5}), ("ghost_radiation", G, {})])
    fw0, fwa, _ = lsq_cpl(m5.wN2, mp.mpf(1) / 2)
    check("M5_fit_equals_unite", abs(fw0 + mp.mpf("0.861")) < mp.mpf("1e-20") and abs(fwa + mp.mpf("0.60")) < mp.mpf("1e-20"),
          "condensate + positive q-mode + ghost radiation (|rho_ghost| = 0.3 of the total at a = 1): N2 least-squares CPL fit over a in [1/2, 1] (101 points) = (-0.861, -0.60); s = %s, Omega_q = %s" % (num(s5), num(Oq5)))
    cr = crossings(m5.wN2)
    check("M5_crosses_minus_1", len(cr) == 1, "w_eff(N2) of M5 crosses -1 once in [1/3, 1], at a = %s (Unite line: 461/600 = 0.768333)" % (num(cr[0]) if cr else "none"))
    m5_no_ghost = Model([("condensate", 1 - Oq5, {}), ("qmode", Oq5, {"s": s5})])
    check("M5_without_ghost_no_crossing", len(crossings(m5_no_ghost.wN2)) == 0,
          "the same model with the ghost component removed (Omega_c = 1 - Omega_q) has no crossing: the crossing is due to the negative-energy component")
    out["M5_with_ghost_component"] = summarize(m5, {
        "content": "positive condensate + positive extra-time mode + a GHOST component (massless good-sector modes of NEGATIVE classical energy, rho_g = -G/a, eps = 1/3), G = 3/10 of the total at a = 1 (a stated choice); s and Omega_q solve: N2 least-squares CPL fit over a in [1/2, 1] = (-0.861, -0.60)",
        "parameters": {"G": "3/10", "s": num(s5), "Omega_q": num(Oq5), "Omega_c": num(1 - Oq5 + G)},
        "turning_point_a_star": num(1 / mp.sqrt(s5)),
        "family": "smaller G moves the q-mode turning point towards a = 1 (G = 0.28: s = 0.726; G = 0.24: s = 0.921; exploration, not a check); for G = 0 no crossing is possible (theorem)",
    })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OWN)
    args = ap.parse_args()
    g, eta = load_gammas()
    ok_cl = all(((g[i] * g[j] + g[j] * g[i]) == (2 * eta[i] * sp.eye(16) if i == j else sp.zeros(16))) for i in range(8) for j in range(8))
    check("gammas_clifford_author_T16", ok_cl, "{gamma^a, gamma^b} = 2 eta^ab for the fixture Revision/algebra/gammas.json (eta = diag(+,+,+,-,-,-,-,+) in the order x1..x8)")
    theory = {
        "title": "dirac16complex00 (classical commuting Pin(4,4) spinor): the 3-space observer's equation of state in the deflating primordial field (Hypothesis00; Revision/SPEC.md sections 8 and 11)",
        "producer": "Revision/dark_sector/dirac16complex00/python/derive_eos.py (implementation A: sympy exact, mpmath 30 digits)",
        "labels": "EXACT = verified by exact symbolic computation in the named checks; APPROXIMATION = stated approximation; ASSUMPTION = observer or model assumption; INTERPRETATION = reading, not a computed statement",
        "metric": "author's metric (SPEC section 1); a4 linear in x4 (a4 = A H x4 + a0, the exponentially deflating member, the only one a homogeneous dirac16complex00 condensate allows) is the reference background; test-field statements hold for every a4(x4)",
        "conservation": section_conservation(),
        "observer": section_observer(),
        "condensate": section_condensate(g),
        "modes": section_modes(g),
        "wkb": section_wkb(),
        "models": section_models(),
        "ghost": "INTERPRETATION (with the exact basis above): dirac16complex00 is a commuting field with a first-order Lagrangian; at every real frequency half of its modes (Krein charge of the opposite sign) carry negative classical energy, and its energy is unbounded below. Components of negative classical energy are a ghost-like sector. With positive-energy components only, no phantom w and no crossing of -1 occur (theorem of section wkb); every phantom or crossing found here needs the ghost-like sector, or (ratio definition only) a constant condensate with lambda < 0.",
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
