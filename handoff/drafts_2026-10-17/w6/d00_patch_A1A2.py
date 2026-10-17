"""W6 draft: dirac16complex00/python/derive_eos.py for the corrected metric, sections header, A1 (conservation) and A2
(observer normalisations).  Applied to the scratch copy scratchpad/w6/d00/python/derive_eos.py only."""
from pathlib import Path

p = Path(__file__).with_name("d00") / "python" / "derive_eos.py"
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''Inputs (Revision outputs only): Revision/algebra/gammas.json (the author's T16 in the author's
coordinate order) and Revision/field_equations_a4/a4-equations.json (key b4: the field equations of the
metric with b4 for a general source).

The metric is the author's of Dirac_Einstein-Lovelock_4+4_Nash.nb (In[48]: X = {x0[], ..., x7[]};
In[97]-In[102]): g = diag(cot^2 z, e^{2 a4} sin^{1/3} z (x3), -1, -e^{-2 a4} b4 sin^{1/3} z (x3)), z = 6 H x0.
b4 is a FUNCTION of x4 (never 1).  The history of the numbers: a4 = H x4 and b4(x4) = b4(0) e^{(4/3) H x4}
(beta = d ln b4/d a4 = 4/3), the branch that the author's weights allow for a source without T^x4_x0
(Revision/dark_sector/dirac16complex/derive/derive_effective.py, check author_weights_b4_branch).
"""''', '''Inputs (Revision outputs only): Revision/algebra/gammas.json (the author's T16 in the author's
coordinate order) and Revision/field_equations_a4/a4-equations.json (keys generalSource, exponentialHistory, fields:
the field equations of the corrected metric for a general source).

The metric is the corrected primordial metric of 2026-10-16 (version 2; Revision/SPEC.md section 1), in the author's
coordinates X = {x0, ..., x7}: g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)),
z = 6 H x0 real.  b4 is a FUNCTION of x4.  The history of the numbers: a4 = H x4 and b4 = e^{(4/3) H x4} (beta = d ln b4/d
a4 = 4/3), the record's history (Revision/kohn_sham/ks-theory.json adiabaticity.historyBeta), a PRESCRIBED background: with
the author's weights it needs the source exponentialHistory.authorWeights.historySource_kappaT_minus_Lam of
a4-equations.json.  Every real z: the x0 dependence enters through C = cot z (signed) and W = (sin^2 z)^{1/12} with
dC/dx0 = -6 H (1 + C^2), dW/dx0 = H C W.
"""''')
rep('''HERE = os.path.dirname(os.path.abspath(__file__))
OWN = os.path.normpath(os.path.join(HERE, ".."))
REV = os.path.normpath(os.path.join(OWN, "..", ".."))''', '''HERE = os.path.dirname(os.path.abspath(__file__))
OWN = os.path.normpath(os.path.join(HERE, ".."))
REV = os.environ.get("REVISION_DIR") or os.path.normpath(os.path.join(OWN, "..", ".."))''')
rep('''BETA = sp.Rational(4, 3)      # d ln b4/d a4 on the history (b4 ~ a^(4/3))
BETA_MP = mp.mpf(4) / 3''', '''BETA = sp.Rational(4, 3)      # d ln b4/d a4 on the history (b4 ~ a^(4/3))
BETA_MP = mp.mpf(4) / 3
SHIFT_N2 = -(4 - 2 * BETA) / 3          # w_eff(N2) - w_eff(N1) = -4/9 on the history
SHIFT_N2_MP = -(4 - 2 * BETA_MP) / 3''')
# ---- A1: conservation for the corrected metric (diagonal metric functions of x4 and of C, W)
old_a1_start = t.index("def christoffel_diag(gd, X):")
old_a1_end = t.index("# ----------------------------------------------------------------------------------------------\n# A2. Observer normalisations")
new_a1 = '''def christoffel_diag(gd, X, D):
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
    a4 = sp.Function("a4")(x4)
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


'''
t = t[:old_a1_start] + new_a1 + t[old_a1_end:]
# ---- A2: observer normalisations
old_a2_start = t.index("def section_observer():")
old_a2_end = t.index("# ----------------------------------------------------------------------------------------------\n# A3. The homogeneous condensate")
new_a2 = '''def section_observer():
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


'''
t = t[:old_a2_start] + new_a2 + t[old_a2_end:]
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
