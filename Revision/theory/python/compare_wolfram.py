"""Revision theory (sympy side): compare the sympy results with the Wolfram side's
Revision/theory/field-theory.json (formulas) and Revision/theory/reports/wolfram-field-theory.json (checks).

These two files are READ here, at the end, and only as data: every Wolfram formula record is compared.  A record
in InputForm is parsed into sympy and compared with the sympy-side expression; the prose field equation and adjoint
equation are parsed (parse_dirac_prose); every other prose record must be exactly the statement quoted in STATED
(QUANTISATION_STATEMENTS for quantisation), which is re-derived here in the sympy jet algebra or, where it is the
statement of a sympy check, is backed by that passing check.  Every Wolfram check is paired with sympy checks
(CHECK_MAP); the sympy checks without a Wolfram counterpart carry a written justification (SYMPY_ONLY).
Reading Revision/algebra/reports/wolfram-algebra.json (data) for the algebra checks those justifications cite.
No Wolfram code is used."""

import json
import os
import re

import sympy as sp

from geometry import ETA, X0, X4, E, w, sv, c, sgn, Q, A1, A2, B1, B2, H, m, lam, cd_author, zero_author, canon_author
from superalg import Alg, gen, CHI, PSI

COORD = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # the author's coordinates; index k = xk
x0s = sp.Symbol("x0", real=True)
a4x = sp.Symbol("a4x", real=True)
b4x = sp.Symbol("b4x", positive=True)       # b4[x4] of the Wolfram strings
bd1, bd2 = sp.symbols("bd1 bd2", real=True)  # b4'[x4], b4''[x4]
Z = 6 * H * x0s
RFTSIG = sp.Symbol("rftSig", real=True)     # sign(Cot z) of the Wolfram strings (sqrt|g| = rftSig f0...f7)


def to_wl_vars(expr):
    """sympy ring expression -> the variables used for parsed Wolfram strings (Q = b4^(1/2), B1 = b4'/b4,
    B2 = b4''/b4 - (b4'/b4)^2, sv = sin z, c = cos z, w = (sin^2 z)^(1/12), sgn = rftSig)."""
    return sp.sympify(expr).subs({B2: bd2 / b4x - (bd1 / b4x) ** 2, B1: bd1 / b4x}).subs(
        {E: sp.exp(a4x), Q: sp.sqrt(b4x), w: (sp.sin(Z) ** 2) ** sp.Rational(1, 12), sv: sp.sin(Z), c: sp.cos(Z),
         sgn: RFTSIG})


def to_ring(expr):
    """Parsed Wolfram expression (or a ring expression) -> the sympy coefficient ring (every real z): |sin z|^p ->
    w^(6 p), (sin^2 z)^k -> w^(12 k), sin z -> sv, cos z -> c, e^a4 -> E, b4 -> Q^2, b4' -> B1 Q^2, b4'' -> (B2 + B1^2)
    Q^2, rftSig -> sgn.  Ring symbols are left unchanged, so the map is idempotent."""
    e = sp.sympify(expr)
    e = e.replace(lambda x: isinstance(x, sp.Abs) and x.args[0] == sp.sin(Z), lambda x: w**6)
    e = e.replace(lambda x: x.is_Pow and x.base == sp.sin(Z) ** 2, lambda x: w ** (12 * x.exp))
    s2, c2 = 2 * sv * c, c**2 - sv**2           # sin 2z, cos 2z (Wolfram's FullSimplify writes double angles)
    e = e.subs({sp.sin(2 * Z): s2, sp.cos(2 * Z): c2, sp.tan(2 * Z): s2 / c2, sp.cot(2 * Z): c2 / s2,
                sp.csc(2 * Z): 1 / s2, sp.sec(2 * Z): 1 / c2})
    e = e.subs({sp.cot(Z): c / sv, sp.tan(Z): sv / c, sp.csc(Z): 1 / sv, sp.sec(Z): 1 / c})
    e = e.subs({sp.sin(Z): sv, sp.cos(Z): c})
    e = e.subs({bd2: (B2 + B1**2) * Q**2, bd1: B1 * Q**2}).subs({b4x: Q**2}).subs({sp.exp(a4x): E})
    return e.subs(RFTSIG, sgn)


def wl_parse(src):
    """Parse a (simple) Wolfram InputForm expression into sympy."""
    t = src
    t = t.replace("Derivative[1][a4][x4]", "A1").replace("Derivative[2][a4][x4]", "A2")
    t = t.replace("Derivative[1][b4][x4]", "bd1").replace("Derivative[2][b4][x4]", "bd2")
    t = t.replace("a4[x4]", "a4x").replace("b4[x4]", "b4x")
    t = re.sub(r'dd\["x(\d)",\s*Psi\[(\d+)\]\]', r"dd_\1_\2", t)
    t = re.sub(r"Psi\[(\d+)\]", r"P_\1", t)
    t = re.sub(r'gamma\["x(\d)"\]', r"G_\1", t)
    for f in ("Sin", "Cos", "Tan", "Cot", "Sec", "Csc", "Sqrt", "Abs"):
        t = t.replace(f + "[", f.lower() + "(")
    t = t.replace("[", "(").replace("]", ")").replace("{", "[").replace("}", "]").replace("^", "**")
    names = {"sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot, "sec": sp.sec, "csc": sp.csc, "E": sp.E,
             "sqrt": sp.sqrt, "H": H, "x0": x0s, "rftSig": RFTSIG, "abs": sp.Abs,
             "a4x": a4x, "A1": A1, "A2": A2, "b4x": b4x, "bd1": bd1, "bd2": bd2, "V": sp.Symbol("V"), "m": m}
    for k in set(re.findall(r"\b(dd_\d_\d+|P_\d+|G_\d)\b", t)):
        names[k] = sp.Symbol(k)
    expr = sp.sympify(t, locals=names)

    def atoms(x):
        if isinstance(x, (list, tuple)):
            return set().union(*[atoms(y) for y in x]) if x else set()
        return {f for f in sp.sympify(x).atoms(sp.Function) if isinstance(f, sp.core.function.AppliedUndef)}

    undef = atoms(expr)
    if undef:
        raise ValueError(f"unparsed Wolfram functions in {src[:80]}: {undef}")
    return expr


FIELD_NAMES = ("rho", "p3", "pt", "p0")  # the entries of the diagonal T of the formula energy_exchange (p0: along x0)


def wl_top_split(src):
    """Top-level entries of a Wolfram InputForm list '{a, b, ...}' (commas inside brackets are kept)."""
    t = src.strip()
    if not (t.startswith("{") and t.endswith("}")):
        raise ValueError(f"not a Wolfram list: {src[:60]}")
    out, depth, cur = [], 0, []
    for ch in t[1:-1]:
        if ch in "[({":
            depth += 1
        elif ch in "])}":
            depth -= 1
        if ch == "," and depth == 0:
            out.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    out.append("".join(cur).strip())
    return out


def wl_parse_fields(src):
    """wl_parse for expressions in the functions rho, p3, pt, p0 of (x4, x0) or of x4 alone:
    Derivative[1, 0][f][x4, x0] and Derivative[1][f][x4] -> f_4, Derivative[0, 1][f][x4, x0] -> f_0, f[..] -> f."""
    t = re.sub(r"Derivative\[1, 0\]\[(rho|p3|pt|p0)\]\[x4, x0\]", r"\1_4", src)
    t = re.sub(r"Derivative\[0, 1\]\[(rho|p3|pt|p0)\]\[x4, x0\]", r"\1_0", t)
    t = re.sub(r"Derivative\[1\]\[(rho|p3|pt|p0)\]\[x4\]", r"\1_4", t)
    t = re.sub(r"\b(rho|p3|pt|p0)\[x4(?:, x0)?\]", r"\1", t)
    return wl_parse(t)


def energy_exchange_compare(ew, geo):
    """Recompute nabla_mu T^mu_nu (all eight nu) for T = diag(p0, p3, p3, p3, -rho, pt, pt, pt) (order x0..x7),
    entries functions of x4 and x0, from the sympy Christoffel symbols with the general mixed-tensor formula
    d_mu T^mu_nu + Gamma^mu_(mu l) T^l_nu - Gamma^l_(mu nu) T^mu_l, and compare it with the Wolfram record
    [complete identity, conservation equations, x0-independent case] (three InputForm strings)."""
    f = {n: sp.Symbol(n) for n in FIELD_NAMES}
    f4 = {n: sp.Symbol(f"{n}_4") for n in FIELD_NAMES}
    f0 = {n: sp.Symbol(f"{n}_0") for n in FIELD_NAMES}
    T = sp.diag(f["p0"], f["p3"], f["p3"], f["p3"], -f["rho"], f["pt"], f["pt"], f["pt"])

    def d(e, mu):  # coordinate derivative: the metric ring plus the jets of the four entries
        r = cd_author(e, mu)
        if mu in (X4, X0):
            jet = f4 if mu == X4 else f0
            r += sum(sp.diff(e, f[n]) * jet[n] for n in FIELD_NAMES)
        return r

    mine = []
    for nu in range(8):
        v = sum(d(T[mu, nu], mu) for mu in range(8))
        v += sum(geo.Gam[mu][mu][l] * T[l, nu] for mu in range(8) for l in range(8))
        v -= sum(geo.Gam[l][mu][nu] * T[mu, l] for mu in range(8) for l in range(8))
        mine.append(sp.factor(canon_author(v)))
    cot = c / sv
    shown = "; ".join(f"{COORD[nu]}: {sp.sstr(sp.expand(mine[nu]))}" for nu in range(8))
    if not isinstance(ew, list) or len(ew) != 3:
        return False, ("the Wolfram record energy_exchange is not the three-entry InputForm list [complete identity, "
                       "conservation equations, x0-independent case]; sympy recomputation: " + shown)
    # entry 1: the complete identity, component by component
    theirs = wl_parse_fields(ew[0])
    ok1 = len(theirs) == 8 and all(same(theirs[nu], to_wl_vars(mine[nu])) for nu in range(8))
    ok1 = ok1 and all(mine[nu] == 0 for nu in range(8) if nu not in (X4, X0))
    # entry 2: conservation <=> the two solved equations (each component linear in the solved derivative, -1 / +1)
    eqs = [tuple(wl_parse_fields(side) for side in e.split("==")) for e in wl_top_split(ew[1])]
    ok2 = len(eqs) == 2 and all(len(e) == 2 for e in eqs)
    ok2 = ok2 and eqs[0][0] == f4["rho"] and eqs[1][0] == f0["p0"]
    ok2 = ok2 and sp.expand(sp.diff(mine[X4], f4["rho"]) + 1) == 0 and zero_author(sp.diff(mine[X0], f0["p0"]) - 1)
    ok2 = ok2 and same(to_wl_vars(mine[X4]).subs(f4["rho"], eqs[0][1]), 0) and \
        same(to_wl_vars(mine[X0]).subs(f0["p0"], eqs[1][1]), 0)
    # entry 3: x0-independent entries; the x0 component is linear in p0 with coefficient 3 H cot z (!= 0 between the
    # degenerate points)
    eq3 = [tuple(wl_parse_fields(side) for side in e.split("==")) for e in wl_top_split(ew[2])]
    m0 = mine[X0].subs({f0[n]: 0 for n in FIELD_NAMES})
    ok3 = len(eq3) == 2 and all(len(e) == 2 for e in eq3) and eq3[0][0] == f4["rho"] and eq3[1][0] == f["p0"]
    # the stated rho equation of the x0-independent case already uses p0 = p_t (the second equation)
    ok3 = ok3 and same(to_wl_vars(mine[X4]).subs(f["p0"], eq3[1][1]).subs(f4["rho"], eq3[0][1]), 0) and \
        same(to_wl_vars(m0).subs(f["p0"], eq3[1][1]), 0) and zero_author(sp.diff(m0, f["p0"]) - 3 * H * cot)
    detail = ("the complete identity nabla_mu T^mu_nu, nu = x0..x7, for T = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) "
              "with entries functions of x4 and x0, recomputed here from the sympy Christoffel symbols with the general "
              "mixed-tensor formula (f_4 = d f/d x4, f_0 = d f/d x0; ring c/sv = cot z; every real z): " + shown +
              f". Wolfram entry 1 (the eight components) {'equals' if ok1 else 'DIFFERS from'} it component by "
              f"component; entry 2 (d rho/d x4 = -3 a4' (rho + p3) - 3 h4 (rho + p_t) - h4 (rho + p0), h4 = b4'/(2 b4) - "
              f"a4', d p0/d x0 = -3 H cot z (p0 - p_t)) {'is' if ok2 else 'is NOT'} equivalent to its vanishing; entry 3 "
              f"(x0-independent entries: d rho/d x4 = -3 a4' (rho + p3) - 4 h4 (rho + p_t), p0 = p_t) "
              f"{'is' if ok3 else 'is NOT'} equivalent to its vanishing (coefficient of p0 in the x0 component 3 H cot z, "
              "nonzero between the degenerate points). Same statement as the sympy check energy_exchange_equation")
    return ok1 and ok2 and ok3, detail


def same(a, b):
    """Exact equality, every real z: both sides are mapped into the coefficient ring (to_ring) and the difference is
    tested with the ring's exact zero test; expressions outside the ring fall back to sympy simplification."""
    d = sp.expand(to_ring(a) - to_ring(b))
    if d == 0:
        return True
    if not (d.free_symbols & {x0s, a4x, b4x, bd1, bd2}):
        return zero_author(d)
    d = sp.simplify(d)
    return d == 0 or sp.simplify(sp.expand_trig(sp.trigsimp(d))) == 0


def rec(out, name, ok, detail):
    out.append({"name": name, "verdict": "agree" if ok else "DISAGREE", "detail": detail})


# ------------------------------------------------------------------ prose records
# The Wolfram side states 19 of its 32 formula records in prose (field-theory.json; addFormulaText in
# verify_field_theory.wls).  Two of them, field_equation and adjoint_equation, are PARSED here (parse_dirac_prose).
# Sixteen are compared through the statement quoted verbatim below (STATED): the record agrees only if its text is
# exactly this statement AND the statement is re-derived here (or, where it is the statement of a sympy check, that
# check passes); a changed Wolfram text therefore shows up as a disagreement and has to be compared anew.  The
# nineteenth, quantisation, is compared statement by statement (QUANTISATION_STATEMENTS).
STATED = {
    'Omega_components': (
        "Omega_x0 = (1/2) h4 sb Cot[6 H x0] g[x0].g[x4]; Omega_xi = (1/2) a4'[x4] E^a4[x4] g[xi].g[x4] (i = 1"
        ', 2, 3); Omega_xt = (1/2) (Sin[6 H x0]^2)^(1/12) (h4 sb g[x4].g[xt] + H g[x0].g[xt]) (t = 5, 6, 7); '
        'Omega_x4 = 0; g[xa] = gamma^(xa) (frame gammas of the fixture)'
    ),
    'Lagrangian': (
        'L = sqrt g [ (1/2) sum_mu (Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m S - U(S) ] = s'
        'qrt g [ (1/2) sum_a (1/f_a) (Psibar gamma^(a) d_a Psi - d_a Psibar gamma^(a) Psi) - m S - U(S) ]; sq'
        'rt g = E^-a4[x4] b4[x4]^2 |Cot[z]| (Sin[z]^2)^(1/4); f_0 = E^-a4 b4^(1/2) Cot[z], f_(1,2,3) = E^a4, '
        'f_4 = 1, f_(5,6,7) = E^-a4 b4^(1/2) (Sin[z]^2)^(1/12)'
    ),
    'current': (
        'J^mu = -i Psibar gamma^mu Psi; d_mu (sqrt g J^mu) = -i sqrt g (Ebar Psi + Psibar E), sqrt g = E^-a4['
        'x4] b4[x4]^2 |Cot[z]| (Sin[z]^2)^(1/4); J^x4 = Psi^dagger B Psi; Q = Integral sqrt g Psi^dagger B Ps'
        'i dx0 dx1 dx2 dx3 dx5 dx6 dx7'
    ),
    'Lichnerowicz': (
        '(gamma^mu D_mu)^2 Psi = g^mu,nu (D_mu D_nu - Gamma^l_mu,nu D_l) Psi - (R/4) Psi, R = -12 H^2 E^(2 a4'
        "[x4])/b4[x4] + 8 a4'[x4]^2 - 2 a4''[x4] - 8 a4'[x4] b4'[x4]/b4[x4] + 4 b4''[x4]/b4[x4] + (b4'[x4]/b4"
        '[x4])^2'
    ),
    'evolution_form': (
        "d4 Psi = -g[x4] ((m + U'(S)) Psi - sum_(a != x4) (1/f_a) g[xa] d_a Psi - (3/2) H E^a4[x4] b4[x4]^(-1"
        "/2) g[x0] Psi) - (b4'[x4]/b4[x4] - a4'[x4]/2) Psi"
    ),
    'T_variation': (
        'T^nu_mu = delta^nu_mu L0 - (1/2) (Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi) - (1/4) g_mu,'
        'rho nabla_l (Psibar {gamma^l, Sigma^(nu rho)} Psi), Sigma^(nu rho) = (1/4) [gamma^nu, gamma^rho]'
    ),
    'T_symmetric': (
        'T^nu_mu = delta^nu_mu L0 - (1/4) (Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi + Psibar gamma'
        '_mu D^nu Psi - D^nu Psibar gamma_mu Psi)'
    ),
    'EMT_diagonal': (
        'K_mu = (1/(2 f_mu)) (Psibar gamma^(mu) d_mu Psi - d_mu Psibar gamma^(mu) Psi); L0 = sum_mu K_mu - m '
        'S - U(S); T^mu_mu = L0 - K_mu; rho = -T^x4_x4 = -sum_(mu != x4) K_mu + m S + U; p3 = T^x1_x1 (= T^x2'
        '_x2 = T^x3_x3 for isotropic states) = sum_(mu != x1) K_mu - m S - U; p_t = T^x5_x5 = sum_(mu != x5) '
        'K_mu - m S - U; p0 = T^x0_x0 = sum_(mu != x0) K_mu - m S - U'
    ),
    'EMT_kinetic_potential': (
        'T^nu_mu = T_kin^nu_mu + T_pot^nu_mu, T_pot^nu_mu = -delta^nu_mu (m S + U(S)), T_kin^nu_mu = delta^nu'
        '_mu sum_l K_l - (1/4)(Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi + Psibar gamma_mu D^nu Psi'
        ' - D^nu Psibar gamma_mu Psi); potential energy density rho_pot = m S + U, potential pressure p_pot ='
        ' -(m S + U) in every direction'
    ),
    'EMT_trace': (
        "T^mu_mu (sum) = 8 L0 - sum_mu K_mu = 7 sum_mu K_mu - 8 (m S + U); on shell = 7 (m + U') S - 8 (m S +"
        " U) = -m S + 7 S U' - 8 U"
    ),
    'EMT_homogeneous_on_shell': (
        "rho = m S + U(S); p3 = p_t = p0 = S U'(S) - U(S); w = (S U' - U)/(m S + U); for U = (lam/2) S^2: rho"
        ' = m S + lam S^2/2, p = lam S^2/2, w = lam S/(2 m + lam S); S = E^a4 b4^(-2) S_chi with S_chi consta'
        'nt on shell (check exact_solution_nonlinear_homogeneous_C)'
    ),
    'EMT_offdiagonal_x4_x0': (
        'T^x4_x0 = -(1/4) (B40 - E^-a4 b4^(1/2) Cot[z] B04), B40 = Psibar gamma^(x4) d0 Psi - d0 Psibar gamma'
        '^(x4) Psi, B04 = Psibar gamma^(x0) d4 Psi - d4 Psibar gamma^(x0) Psi; T^x0_x4 = -E^(2 a4) b4^(-1) Ta'
        'n[z]^2 T^x4_x0 (T_x4x0 = T_x0x4)'
    ),
    'nontriviality': (
        'gamma^mu D_mu Psi - gamma^mu d_mu Psi = gamma^mu Omega_mu Psi = ((3/2) H E^a4 b4^(-1/2) gamma^(x0) +'
        " (b4'/b4 - a4'/2) gamma^(x4)) Psi (nonzero for every H > 0, all a4 and b4; its square is (9/4) H^2 E"
        "^(2 a4)/b4 - (b4'/b4 - a4'/2)^2); per direction gamma^(x0) Omega_x0 = (h4/2) gamma^(x4), gamma^(xi) "
        "Omega_xi = (a4'/2) gamma^(x4) (i = 1, 2, 3) and gamma^(xt) Omega_xt = (h4/2) gamma^(x4) + (H/2) E^a4"
        " b4^(-1/2) gamma^(x0) (t = 5, 6, 7), h4 = b4'/(2 b4) - a4'; Omega_mu = 0 for all mu iff a4' = 0, b4'"
        ' = 0 and H = 0 (H = 0 is a degenerate limit of the metric); [D_mu, D_nu] = (1/2) R_ab,mu,nu S^ab: Om'
        'ega can be removed by a frame only where the metric is flat (the corrected metric is flat for a4 = 0'
        ", b4 = H^2 x4^2 and curved on the record's history)"
    ),
    'majorana_negative_control': (
        'anticommuting real Psi: sqrt g Psi^T C gamma^mu D_mu Psi = d_mu ((1/2) sqrt g Psi^T C gamma^mu Psi) '
        '(a total derivative; no field equation; Psi^T C Psi = 0); commuting real Phi: Euler-Lagrange express'
        'ion 2 sqrt g C gamma^mu D_mu Phi and Phi^T C gamma^mu Phi = 0'
    ),
    'exact_solutions': (
        "(i-a) U = 0, m = 0: Psi = Fsc (Sin[z]^2)^(al/2) (Cosh[I] + Sinh[I] K) chi, I' = muA; (i-b) U = 0, al"
        ' = -1/4: Psi = Fsc (Sin[z]^2)^(-1/8) (Cos[m x4] - Sin[m x4] g[x4]) chi; (ii) U = (lam/2) S^2, homoge'
        "neous, commuting: Psi = Fsc chi for every solution of chi' = (-(m + lam E^a4 b4^(-2) S0) g[x4] + (3/"
        '2) H E^a4 b4^(-1/2) K) chi, S0 = chi^dagger C chi constant, S = E^a4 b4^(-2) S0; (iii) Grassmann, m '
        "= 0: Psi = Fsc sum_k [P c_k + lam S0 eta_k] theta_k, P = Cosh[I0] + Sinh[I0] K, I0' = (3/2) H E^a4 b"
        "4^(-1/2), eta_k = -P g[x4] (Ic + Is K) c_k, Ic' = Fsc^2 Cosh[2 I0], Is' = Fsc^2 Sinh[2 I0], S0 = sum"
        '_kl thetabar_k theta_l c_k^dagger C c_l; at (ii) and (iii): rho = m S + lam S^2/2, p3 = p_t = p0 = l'
        'am S^2/2'
    ),
    'equation_of_state_definitions': (
        'rho = -T^x4_x4, p3 = T^x1_x1, p_t = T^x5_x5, p0 = T^x0_x0; w3 = p3/rho, w_t = p_t/rho, w0 = p0/rho; '
        "homogeneous on shell: w3 = w_t = w0 = (S U' - U)/(m S + U)"
    ),
    'hidden_direction_hermiticity': (
        '(Sin[z]^2)^(1/4) [p (d0 + (3/2) H Cot[z]) q + ((d0 + (3/2) H Cot[z]) p) q] = d0 ((Sin[z]^2)^(1/4) p '
        'q): the hidden-direction operator E^a4 b4^(-1/2) (Tan[z] d0 + (3/2) H) gamma^(x0) is antisymmetric f'
        'or the measure sqrt g/f0 dx0 = b4^(3/2) (Sin[z]^2)^(1/4) dx0 up to the boundary term (Sin[z]^2)^(1/4'
        ') p q, which vanishes where Sin z = 0 and not where Cos z = 0; without the spin-connection term (3/2'
        ') H the operator is not formally Hermitian for this measure and these variables'
    ),
}


def _split_top(t, sep):
    """Split t at the separator sep outside brackets."""
    out, depth, cur, i = [], 0, "", 0
    while i < len(t):
        ch = t[i]
        if ch in "[({":
            depth += 1
        elif ch in "])}":
            depth -= 1
        if depth == 0 and t.startswith(sep, i):
            out.append(cur)
            cur = ""
            i += len(sep)
            continue
        cur += ch
        i += 1
    out.append(cur)
    return out


def _prose_expr(t, loc):
    """A prose expression with space-separated products, ' + ' and ' - ' sums and parenthesised groups -> sympy."""
    t = t.strip().replace(" - ", " + -1*")
    terms = _split_top(t, " + ")
    if len(terms) > 1:
        return sp.Add(*[_prose_expr(x, loc) for x in terms])
    factors = [x for x in _split_top(t, " ") if x]
    if len(factors) > 1:
        return sp.Mul(*[_prose_expr(x, loc) for x in factors])
    a = factors[0]
    if a.startswith("(") and a.endswith(")") and len(_split_top(a[1:-1], " ")) > 1:
        return _prose_expr(a[1:-1], loc)
    return sp.sympify(a, locals=loc)


def parse_dirac_prose(text, adjoint):
    """The prose field equation (adjoint=False) or adjoint equation (adjoint=True) of field-theory.json ->
    (coefficients c_a of gamma^(a) d_a Psi (resp. d_a Psibar gamma^(a)), a = x0..x7, coefficients of the terms
    without derivative (gamma^(x0) Psi and gamma^(x4) Psi, resp. Psibar gamma^(x0) and Psibar gamma^(x4)),
    right-hand side text, problems found)."""
    problems = []
    lhs, rhs = text.split(" = ")
    if adjoint:
        problems += [f"d{a} Psibar g[x{b}]" for a, b in re.findall(r"d(\d) Psibar g\[x(\d)\]", lhs) if a != b]
        t = re.sub(r"d(\d) Psibar g\[x\1\]", r"GD_\1", lhs).replace("Psibar g[x0]", "G_0")
        t = t.replace("Psibar g[x4]", "G_4")
    else:
        problems += [f"g[x{a}] d{b}" for a, b in re.findall(r"g\[x(\d)\] d(\d)", lhs) if a != b]
        t = re.sub(r"g\[x(\d)\] d\1", r"GD_\1", lhs).replace("g[x0] Psi", "G_0").replace("g[x4] Psi", "G_4")
        t = re.sub(r"\bPsi\b", "", t)
    t = re.sub(r"\s+", " ", t).replace("( ", "(").replace(" )", ")").strip()
    t = re.sub(r"a4'(\[x4\])?", "A1", t)
    t = re.sub(r"E\^-a4(\[x4\])?", "exp(-a4x)", t)
    t = re.sub(r"E\^a4(\[x4\])?", "exp(a4x)", t)
    t = re.sub(r"b4'(\[x4\])?", "bd1", t)
    t = re.sub(r"\bb4(\[x4\])?", "b4x", t)
    t = t.replace("Sin[z]", "sin(Z)").replace("Tan[z]", "tan(Z)").replace("Cot[z]", "cot(Z)").replace("^", "**")
    gd = [sp.Symbol(f"GD_{a}") for a in range(8)]  # GD_a: gamma^(xa) d_a, a = 0..7
    g0, g4 = sp.Symbol("G_0"), sp.Symbol("G_4")
    loc = {"Z": Z, "a4x": a4x, "b4x": b4x, "bd1": bd1, "A1": A1, "H": H, "G_0": g0, "G_4": g4}
    loc.update({str(x): x for x in gd})
    try:
        e = sp.expand(_prose_expr(t, loc))
    except (SyntaxError, TypeError, ValueError, sp.SympifyError) as exc:
        return ([sp.Integer(0)] * 8, (sp.Integer(0), sp.Integer(0)), rhs.strip(),
                problems + [f"not parsed: {type(exc).__name__}"])
    if not e.free_symbols <= set(gd) | {g0, g4, H, x0s, a4x, b4x, bd1, A1}:
        problems.append(f"unparsed symbols {sorted(map(str, e.free_symbols))}")
    coef = [e.coeff(x) for x in gd]
    rest = sp.expand(e - sum(cf * x for cf, x in zip(coef, gd)))
    const0, const4 = rest.coeff(g0), rest.coeff(g4)
    if sp.expand(rest - const0 * g0 - const4 * g4) != 0 or any(cf.has(*gd, g0, g4) for cf in coef) or \
            const0.has(*gd, g0, g4) or const4.has(*gd, g0, g4):
        problems.append("terms of another form")
    return coef, (const0, const4), rhs.strip(), problems


# the statements of the Wolfram record quantisation (separated by '; ') and their passing sympy counterparts
QUANTISATION_STATEMENTS = [
    ((
        'pi_A = (i/2) sqrt g (Psi^dagger B)_A'
    ), ['canonical_momentum', 'sqrt_det_g']),
    ((
        'K = sqrt g C gamma^(x4) = i sqrt g B'
    ), ['canonical_momentum', 'B_properties']),
    ((
        '{Psi_A(x), Psi^dagger_C(y)}_(x4 = y4) = B_AC delta^7(x - y)/sqrt g'
    ), ['canonical_anticommutator_B']),
    ((
        'B = -i C gamma^(x4), B^dagger = B, B^2 = 1, signature (8,8)'
    ), ['B_properties']),
    ((
        'no positive inner product with Psi^dagger the adjoint (Krein space, fundamental symmetry B)'
    ), ['no_positive_inner_product']),
    ((
        'positive representation chi = Psi^dagger B, {Psi_A, chi_C} = delta_AC'
    ), ['good_sector_positive_fock_realisation']),
    ((
        "Heisenberg: d4 Psi = -i B (1/sqrt g) dHd/dPsi^dagger = -gamma^(x4) [(m + U') Psi - sum_(a != x4) gam"
        'ma^a D_a Psi]'
    ), ['hamiltonian_form_and_heisenberg_equation']),
    ((
        'mode operator h = m (-i g[x4]) + sum_(a != x4) (1/f_a) i g[x4].g[xa] d_a + (3/2) i H E^a4 b4^(-1/2) '
        "g[x4].g[x0] - i (b4'/b4 - a4'/2)"
    ), ['hamiltonian_form_and_heisenberg_equation', 'per_direction_terms']),
    ((
        'good sector (no x5, x6, x7 dependence): integral sqrt g u^dagger v d^7x conserved up to boundary ter'
        "ms (the anti-Hermitian term compensates d_x4 sqrt g = (2 b4'/b4 - a4') sqrt g), positive Fock space,"
        ' normal-ordered H = sum E (b^* b + d^* d) >= 0 per momentum'
    ), ['good_sector_spectrum_and_B_sectors', 'good_sector_positive_fock_realisation']),
    ((
        'expectation-value rule <Psi^dagger M Psi> = u^dagger B M u (u^dagger u = 1, positive-energy good-sec'
        'tor u)'
    ), ['good_sector_positive_fock_realisation', 'expectation_value_rule']),
    ((
        'EMT operator T^mu_nu = :T^mu_nu[Psi, Psi^dagger = chi B]: (normal ordered), <T> by the same rule'
    ), ['good_sector_positive_fock_realisation']),
    ((
        'extra-time modes: E^2 = m^2 + k_s^2 - k_t^2 < 0 for k_t^2 > m^2 + k_s^2, growing as exp(|E| x4)'
    ), ['mode_hamiltonian_B_selfadjoint_dispersion', 'extra_time_modes_grow']),
]

# sympy checks without a Wolfram counterpart in wolfram-field-theory.json: the reason, and the Wolfram checks of
# Revision/algebra/reports/wolfram-algebra.json that state the same fact (where they exist; they must PASS)
SYMPY_ONLY = {
    "gammas_json_equals_python_construction": (
        "a cross-engine comparison by itself: the fixture Revision/algebra/gammas.json (Wolfram construction) equals "
        "the independent Python construction Revision/algebra/reports/python-gammas.json; the Wolfram construction is "
        "checked in Revision/algebra/reports/wolfram-algebra.json", ["coordinate_map", "fixture_round_trip"]),
    "gammas_real": ("a property of the fixture, stated on the Wolfram side in the algebra report", ["reality"]),
    "gamma_symmetry_pattern": ("a property of the fixture, stated on the Wolfram side in the algebra report",
                               ["symmetry_pattern"]),
    "grassmann_controls_not_vacuous": (
        "a negative control of the sympy checks themselves (the unsymmetrised Lagrangian is not real and differs "
        "from L), not a statement of the theory; the Wolfram side has its own controls (zero_test_sanity and the "
        "controls inside its checks)", []),
    "commuting_controls_not_vacuous": ("as grassmann_controls_not_vacuous, for the commuting field", []),
    "grassmann_emt_conservation_negative_control": (
        "a negative control of the sympy conservation test (a wrong potential sign is detected), not a statement of "
        "the theory", []),
    "commuting_emt_conservation_negative_control": (
        "as grassmann_emt_conservation_negative_control, for the commuting field", []),
}
# Wolfram checks without a sympy counterpart, with the reason (none at present)
WOLFRAM_ONLY = {}


# ------------------------------------------------------------------ check-by-check correspondence
CHECK_MAP = [
    ("gammas_coordinates_and_eta", ["fixture_Clifford_relation"]),
    ("clifford_relations", ["fixture_Clifford_relation"]),
    ("C_properties", ["fixture_C_B_S_consistent"]),
    ("S_definition_and_C_S_antisymmetric", ["fixture_C_B_S_consistent"]),
    ("chirality_Gamma", ["fixture_C_B_S_consistent", "block_form"]),
    ("B_properties", ["fixture_C_B_S_consistent"]),
    ("metric_from_vielbein_equals_SPEC", ["metric_is_the_corrected_metric", "vielbein_inverse"]),
    ("sqrt_det_g", ["sqrt_det_g"]),
    ("christoffel_symmetric_metric_compatible", ["christoffel_count"]),
    ("spin_connection_antisymmetric", ["omega_antisymmetric"]),
    ("vielbein_postulate", ["vielbein_postulate"]),
    ("Omega_x4_vanishes_Omega_x0_does_not", ["Omega_components", "omega_components"]),
    ("spinor_connection_real", ["Omega_components", "omega_components"]),
    ("covariant_constancy_D_mu_gamma_nu", ["gamma_covariantly_constant", "S_rotates_gamma_with_omega"]),
    ("gamma_mu_Omega_mu_equals_hidden_block_terms", ["gammaOmega_total"]),
    ("per_direction_terms", ["gammaOmega_per_direction"]),
    ("gravity_term_square", ["nontriviality_1_dirac16complex", "nontriviality_2_dirac16complex00"]),
    ("anticommutator_gamma_Omega_vanishes", ["gammaOmega_divergence_form", "L_spin_connection_drops_out_G",
                                             "L_spin_connection_drops_out_C"]),
    ("divergence_of_sqrtg_gamma", ["gammaOmega_divergence_form"]),
    ("nontriviality_Omega_zero_iff_flat", ["Omega_vanishes_iff_a4prime_b4prime_and_H_vanish", "nontriviality_1_dirac16complex",
                                           "nontriviality_2_dirac16complex00", "degenerate_at_H_0"]),
    ("curvature_and_flat_member", ["ricci_scalar", "ricci_mixed_components", "flat_member_and_curvature"]),
    ("spinor_curvature_equals_riemann", ["spin_curvature_equals_Riemann"]),
    ("lichnerowicz_contraction", ["Lichnerowicz_identity_G", "Lichnerowicz_identity_C"]),
    ("lichnerowicz_identity_on_fields", ["Lichnerowicz_identity_G", "Lichnerowicz_identity_C"]),
    ("superalgebra_axioms", ["grassmann_algebra_structure", "zero_test_sanity"]),
    ("grassmann_lagrangian_real", ["L_real_G"]),
    ("commuting_lagrangian_real", ["L_real_C"]),
    ("grassmann_total_divergence_relation", ["L_total_divergence_to_unsymmetrised_G"]),
    ("commuting_total_divergence_relation", ["L_total_divergence_to_unsymmetrised_C"]),
    ("grassmann_euler_lagrange_psibar_variation", ["EL_Psibar_G", "Dirac_operator_explicit_G"]),
    ("grassmann_euler_lagrange_psi_variation", ["EL_Psi_G"]),
    ("commuting_euler_lagrange_psibar_variation", ["EL_Psibar_C", "Dirac_operator_explicit_C"]),
    ("commuting_euler_lagrange_psi_variation", ["EL_Psi_C"]),
    ("grassmann_adjoint_equation_is_conjugate", ["adjoint_equation_is_Dirac_conjugate_G"]),
    ("commuting_adjoint_equation_is_conjugate", ["adjoint_equation_is_Dirac_conjugate_C"]),
    ("grassmann_current_conservation", ["current_real_G", "current_conservation_identity_G"]),
    ("commuting_current_conservation", ["current_real_C", "current_conservation_identity_C"]),
    ("grassmann_emt_symmetric", ["T_symmetric_part_Belinfante_G"]),
    ("commuting_emt_symmetric", ["T_symmetric_part_Belinfante_C"]),
    ("grassmann_emt_conservation_on_shell", ["Noether_identity_diffeomorphisms_G", "conservation_on_shell_general"]),
    ("commuting_emt_conservation_on_shell", ["Noether_identity_diffeomorphisms_C", "conservation_on_shell_general"]),
    ("grassmann_trace_on_shell", ["kinetic_sum_on_shell_G", "EMT_trace_G"]),
    ("commuting_trace_on_shell", ["kinetic_sum_on_shell_C", "EMT_trace_C"]),
    ("grassmann_homogeneous_on_shell_rho_p", ["T_diagonal_components_G", "kinetic_sum_on_shell_G"]),
    ("commuting_homogeneous_on_shell_rho_p", ["T_diagonal_components_C", "kinetic_sum_on_shell_C",
                                              "exact_solution_nonlinear_homogeneous_C"]),
    ("grassmann_T_x4x0_homogeneous", ["T_x4_x0_component_G"]),
    ("commuting_T_x4x0_homogeneous", ["T_x4_x0_component_C"]),
    ("grassmann_emt_equals_general_vielbein_variation_on_shell", ["T_vielbein_variation_closed_form_G",
                                                                  "Noether_identity_local_Lorentz_G"]),
    ("commuting_emt_equals_general_vielbein_variation_on_shell", ["T_vielbein_variation_closed_form_C",
                                                                  "Noether_identity_local_Lorentz_C"]),
    ("grassmann_emt_equals_vielbein_variation_diagonal", ["T_diagonal_components_G"]),
    ("commuting_emt_equals_vielbein_variation_diagonal", ["T_diagonal_components_C"]),
    ("negative_control_majorana_grassmann_total_derivative", ["Majorana_Lg_total_derivative_grassmann"]),
    ("negative_control_majorana_commuting_contrast", ["Majorana_Lg_commuting_control"]),
    ("canonical_momentum", ["canonical_momentum"]),
    ("canonical_anticommutator_B", ["first_order_form_and_anticommutator"]),
    ("no_positive_inner_product", ["no_positive_inner_product", "charge_density_is_Krein_form_G",
                                   "charge_density_is_Krein_form_C"]),
    ("mode_hamiltonian_B_selfadjoint_dispersion", ["mode_hamiltonian_good_sector", "mode_hamiltonian_Krein_selfadjoint",
                                                   "Krein_form_conserved_curved"]),
    ("good_sector_spectrum_and_B_sectors", ["mode_hamiltonian_good_sector", "good_sector_hermiticity_curved"]),
    ("good_sector_positive_fock_realisation", ["Fock_space_good_sector_example"]),
    ("extra_time_modes_grow", ["mode_hamiltonian_good_sector"]),
    ("expectation_value_rule", ["Fock_space_good_sector_example"]),
    ("hamiltonian_form_and_heisenberg_equation", ["Heisenberg_equation_reproduces_field_equation",
                                                  "evolution_form_G", "evolution_form_C"]),
    ("energy_exchange_equation", ["energy_exchange_equation"]),
    ("exact_solution_family_x4_x0", ["solution_matrix_square", "exact_solution_x4_x0_m0_G", "exact_solution_x4_x0_m0_C",
                                 "exact_solution_x4_x0_quarter_G", "exact_solution_x4_x0_quarter_C"]),
    ("exact_nonlinear_homogeneous_solution", ["exact_solution_nonlinear_homogeneous_C",
                                              "exact_solution_nonlinear_homogeneous_G"]),
]


def compare(formulas, checks, ft_path, wrep_path, ctx=None):
    if not os.path.exists(ft_path) or not os.path.exists(wrep_path) or ctx is None:
        return {"status": "not available",
                "detail": "Revision/theory/field-theory.json or wolfram-field-theory.json does not exist yet"}
    with open(ft_path, encoding="utf-8") as fh:
        ft = json.load(fh)
    with open(wrep_path, encoding="utf-8") as fh:
        wr = json.load(fh)
    F = {x["key"]: x["wl"] for x in ft["formulas"]}
    gm, geo = ctx["gm"], ctx["geo"]
    G, Cm, Smat = gm["gamma"], gm["C"], gm["S"]
    out = []
    passed = {x["name"] for x in checks if x["verdict"] == "pass"}

    # ---- metric, vielbein, sqrt g, eta
    gw = wl_parse(F["metric"])
    ok = all(same(gw[i][j], to_wl_vars(geo.g[i]) if i == j else 0) for i in range(8) for j in range(8))
    rec(out, "metric", ok, "the 8x8 metric of field-theory.json equals g = eta f^2 of the sympy side entry by entry")
    fw = wl_parse(F["vielbein_diagonal"])
    rec(out, "vielbein_diagonal", all(same(fw[a], to_wl_vars(geo.f[a])) for a in range(8)), "f_a, a = x0..x7")
    rec(out, "sqrt_det_g", same(wl_parse(F["sqrt_det_g"]), geo.sqrtg),
        "sqrt|det g| = rftSig e^-a4 b4^2 cot z (sin^2 z)^(1/4) = sgn f0...f7 (sgn = sign(cot z)) on both sides")
    rec(out, "eta", [int(x) for x in wl_parse(F["eta"])] == ETA, "eta = diag(1,1,1,1,-1,-1,-1,-1)")
    # ---- Christoffel symbols
    lst = wl_parse(F["christoffel_nonzero"])
    theirs = {(int(l) - 1, int(a) - 1, int(b) - 1): v for l, a, b, v in lst}
    mine = {(l, a, b): geo.Gam[l][a][b] for l in range(8) for a in range(8) for b in range(a, 8)
            if geo.Gam[l][a][b] != 0}
    ok = set(theirs) == set(mine) and all(same(theirs[k], to_wl_vars(mine[k])) for k in mine)
    rec(out, "christoffel_nonzero", ok, f"{len(theirs)} Wolfram vs {len(mine)} sympy nonzero Gamma^l_mn (m <= n); "
        "same index set and equal values")
    # ---- Ricci
    lst = wl_parse(F["ricci_mixed_nonzero"])
    theirs = {(int(a) - 1, int(b) - 1): v for a, b, v in lst}
    mine = {(a, b): sp.expand(geo.ginv[a] * geo.ricci[a][b]) for a in range(8) for b in range(8)
            if not zero_author(geo.ginv[a] * geo.ricci[a][b])}
    ok = set(theirs) == set(mine) and all(same(theirs[k], to_wl_vars(mine[k])) for k in mine)
    rec(out, "ricci_mixed_nonzero", ok,
        f"the nonzero R^mu_nu: {len(theirs)} Wolfram vs {len(mine)} sympy entries, same index set (the diagonal only: "
        "no off-diagonal Ricci component in the corrected metric) and equal values (sympy, ring B1 = b4'/b4: "
        + "; ".join(f"R^{COORD[a]}_{COORD[b]} = {sp.sstr(v)}" for (a, b), v in sorted(mine.items())) + ")")
    rec(out, "ricci_scalar", same(wl_parse(F["ricci_scalar"]), to_wl_vars(geo.Rscalar)),
        "R = -12 H^2 e^(2 a4)/b4 + 8 a4'^2 - 2 a4'' - 8 a4' b4'/b4 + 4 b4''/b4 + (b4'/b4)^2 on both sides (sympy, ring "
        "B2 = b4''/b4 - (b4'/b4)^2: "
        f"{sp.sstr(geo.Rscalar)})")
    # ---- spin connection
    lst = wl_parse(F["omega_nonzero"])
    theirs = {(int(mu) - 1, int(a) - 1, int(b) - 1): v for mu, a, b, v in lst}
    mine = {(mu, a, b): geo.om[mu][a][b] for mu in range(8) for a in range(8) for b in range(a + 1, 8)
            if geo.om[mu][a][b] != 0}
    ok = set(theirs) == set(mine) and all(same(theirs[k], to_wl_vars(mine[k])) for k in mine)
    rec(out, "omega_nonzero", ok, f"{len(theirs)} Wolfram vs {len(mine)} sympy nonzero omega_mu,ab (a < b), equal")
    ok = True
    h4 = B1 / 2 - A1          # the rate of the hidden block
    sb = Q / E                # e^-a4 b4^(1/2), its scale factor
    M0 = h4 * sb * (c / sv) * G[X0] * G[X4] / 2
    ok = ok and all(zero_author(x) for x in (M0 - geo.Om[X0]))
    for i in range(1, 4):  # x1, x2, x3
        Mi = A1 * E * G[i] * G[X4] / 2
        ok = ok and all(zero_author(x) for x in (Mi - geo.Om[i]))
    for t in range(5, 8):  # x5, x6, x7
        Mt = w * (h4 * sb * G[X4] * G[t] + H * G[X0] * G[t]) / 2
        ok = ok and all(zero_author(x) for x in (Mt - geo.Om[t]))
    ok = ok and geo.Om[X4] == sp.zeros(16, 16)
    ok = ok and F["Omega_components"] == STATED["Omega_components"]
    rec(out, "Omega_components", ok, "(statement verbatim) the stated Omega_x0 = (1/2) h4 sb Cot z g[x0].g[x4], Omega_xi = "
        "(1/2) a4' E^a4 g[xi].g[x4], Omega_xt = (1/2) (Sin^2)^(1/12) (h4 sb g[x4].g[xt] + H g[x0].g[xt]), Omega_x4 = 0 "
        "(h4 = b4'/(2 b4) - a4', sb = E^-a4 b4^(1/2)), rebuilt from the gammas, equal the sympy Omega_mu exactly")
    lst = wl_parse(F["gammaOmega_per_direction"])
    ok = True
    for mu, a, b in lst:
        mu = int(mu) - 1
        M = (geo.gam[mu] * geo.Om[mu]).applyfunc(lambda v: to_wl_vars(sp.expand(v)))  # the variables of the parsed record
        ok = ok and all(same(x, 0) for x in (M - a * G[X4] - b * G[X0]))
    rec(out, "gammaOmega_per_direction", ok, "gamma^mu Omega_mu (no sum) = (stated coefficient) gamma^(x4) + "
        "(stated coefficient) gamma^(x0) for all 8 mu, checked against the sympy matrices")
    tot = sp.zeros(16, 16)
    for mu in range(8):
        tot += geo.gam[mu] * geo.Om[mu]
    gt = wl_parse(F["gammaOmega_total"])
    CG = sp.Rational(3, 2) * H * E / Q
    VG = B1 - A1 / 2
    ok = same(gt.coeff(sp.Symbol("G_0")), CG) and same(gt.coeff(sp.Symbol("G_4")), VG)
    ok = ok and same(gt - gt.coeff(sp.Symbol("G_0")) * sp.Symbol("G_0") - gt.coeff(sp.Symbol("G_4")) * sp.Symbol("G_4"), 0)
    ok = ok and all(zero_author(x) for x in (tot - CG * G[X0] - VG * G[X4]))
    rec(out, "gammaOmega_total", ok, "(3/2) H e^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) on both sides")
    # ---- Lagrangian, field equations
    res_L = True
    for stat in ("grassmann", "commuting"):
        sps = ctx["sps"][stat]
        pb, ps = sps.psibar(), sps.psi()
        K = sps.zero()
        for a in range(8):
            K = K + sps.dot(pb, sps.matvec(G[a] / geo.f[a], sps.psi((a,))))
            K = K - sps.dot(sps.vecmat(sps.psibar((a,)), G[a] / geo.f[a]), ps)
        Sx = sps.S()
        Lw = (K.scale(sp.Rational(1, 2)) - Sx.scale(m) - (Sx * Sx).scale(lam / 2)).scale(geo.sqrtg)
        res_L = res_L and (Lw - sps.lagrangian()).expand().is_zero(zero_author)[0]
    # the stated f_a: f_0 = E^-a4 b4^(1/2) Cot[z], f_(1,2,3) = E^a4, f_4 = 1, f_(5,6,7) = E^-a4 b4^(1/2) (Sin[z]^2)^(1/12)
    f_stated = [sp.exp(-a4x) * sp.sqrt(b4x) * sp.cot(Z)] + [sp.exp(a4x)] * 3 + [sp.Integer(1)] + \
        [sp.exp(-a4x) * sp.sqrt(b4x) * (sp.sin(Z) ** 2) ** sp.Rational(1, 12)] * 3
    res_L = res_L and all(same(f_stated[a], geo.f[a]) for a in range(8))
    # the stated sqrt g = E^-a4 b4^2 |Cot z| (Sin^2)^(1/4) is sgn f0...f7 (|Cot z| = sgn Cot z)
    res_L = res_L and zero_author(geo.sqrtg - sgn * Q**4 * (c / sv) * w**3 / E)
    res_L = res_L and F["Lagrangian"] == STATED["Lagrangian"]
    rec(out, "Lagrangian", res_L, "(statement verbatim) the stated L = sqrt g [(1/2) sum_a (1/f_a)(Psibar gamma^(a) d_a "
        "Psi - d_a Psibar gamma^(a) Psi) - m S - U] (spin connection dropped) equals the sympy L (with Omega_mu) "
        "exactly, both statistics, U = (lambda/2) S^2; the stated f_a equal the sympy vielbein factors")
    comps = F["field_equation_components"]
    sps = ctx["sps"]["grassmann"]
    Ev = sps.dirac_E()
    ok = len(comps) == 16
    for A in range(16):
        lhs, rhs = comps[A].split("==")
        lw = wl_parse(lhs)
        mine = 0
        for key, v in Ev[A].t.items():
            if len(key) != 1:
                continue  # the lambda S Psi terms belong to V on the Wolfram side
            kind, B, d = key[0]
            sym = sp.Symbol(f"dd_{d[0]}_{B+1}") if d else sp.Symbol(f"P_{B+1}")  # dd_k_B: d Psi_B / d xk
            mine += to_wl_vars(v) * sym
        mine += m * sp.Symbol(f"P_{A+1}")  # move the mass term back to the right-hand side V
        ok = ok and same(lw, mine) and sp.expand(wl_parse(rhs) - sp.Symbol("V") * sp.Symbol(f"P_{A+1}")) == 0
    rec(out, "field_equation_components", ok, "all 16 component equations (gamma^mu D_mu Psi)_A = V Psi_A parsed "
        "from field-theory.json equal the sympy E_A + (m + lambda S) Psi_A term by term")
    ok_fec = ok
    # the prose field equation, parsed: coefficient of gamma^(a) d_a Psi and the term without derivative
    tot = sp.zeros(16, 16)
    for mu in range(8):
        tot += geo.gam[mu] * geo.Om[mu]
    fe_coef, fe_const, fe_rhs, fe_prob = parse_dirac_prose(F["field_equation"], adjoint=False)
    ok = not fe_prob and fe_rhs == "(m + U'(S)) Psi" and ok_fec
    ok = ok and all(same(fe_coef[a], 1 / geo.f[a]) for a in range(8))
    ok = ok and all(same(to_wl_vars(x), y) for x, y in zip(tot, fe_const[0] * G[X0] + fe_const[1] * G[X4]))
    rec(out, "field_equation", ok, "the prose equation parsed: the coefficient of gamma^(a) d_a Psi equals the sympy "
        f"1/f_a for all eight a ({', '.join(sp.sstr(x) for x in fe_coef)}), the terms without derivative "
        f"{sp.sstr(fe_const[0])} gamma^(x0) Psi + {sp.sstr(fe_const[1])} gamma^(x4) Psi equal the sympy gamma^mu "
        "Omega_mu Psi, and the right-hand side is (m + U'(S)) Psi; the 16 components of this operator are compared in "
        "field_equation_components" + (f"; problems: {fe_prob}" if fe_prob else ""))
    blocks = F["field_equation_blocks"]
    ok = True
    for entry in blocks:
        a = int(re.search(r'"x(\d)"', entry).group(1))  # xa has index a
        tb, tt = wl_parse(re.sub(r'"x\d",\s*', "", entry, count=1))
        Mb = sp.zeros(16, 16)
        Mb[0:8, 8:16] = sp.Matrix(tb)
        Mb[8:16, 0:8] = sp.Matrix(tt)
        ok = ok and Mb == G[a]
    rec(out, "field_equation_blocks", ok and len(blocks) == 8,
        "gamma^(xa) = {{0, tb}, {t, 0}} with the listed 8x8 blocks, all 8 a: equal to the fixture gammas")
    # the prose adjoint equation, parsed; then the parsed operator is rebuilt in the jet algebra
    OmG = sp.zeros(16, 16)
    for mu in range(8):
        OmG += geo.Om[mu] * geo.gam[mu]
    ad_coef, ad_const, ad_rhs, ad_prob = parse_dirac_prose(F["adjoint_equation"], adjoint=True)
    ok = not ad_prob and ad_rhs == "-(m + U'(S)) Psibar"
    ok = ok and all(same(ad_coef[a], 1 / geo.f[a]) for a in range(8))
    # the stated non-derivative terms Psibar (ad_const[0] gamma^(x0) + ad_const[1] gamma^(x4)) must be
    # -Psibar Omega_mu gamma^mu
    ad_M = ad_const[0] * G[X0] + ad_const[1] * G[X4]
    ok = ok and all(same(to_wl_vars(x), y) for x, y in zip(-OmG, ad_M))
    ok = ok and not ad_const[0].free_symbols - {H, a4x, b4x} and not ad_const[1].free_symbols - {b4x, bd1, A1}
    ad_ring = to_ring(ad_const[0]) * G[X0] + to_ring(ad_const[1]) * G[X4]  # back in the ring
    for stat in ("grassmann", "commuting"):
        sps = ctx["sps"][stat]
        pb = sps.psibar()
        lhs = sps.vecmat(pb, ad_ring)
        for a in range(8):
            lhs = sps.vadd(lhs, sps.vecmat(sps.psibar((a,)), G[a] / geo.f[a]))
        Mp = Alg.scalar(stat, m) + sps.S().scale(lam)
        Eb = sps.dirac_Ebar()
        ok = ok and all((lhs[B] + Mp * pb[B] + Eb[B]).expand().is_zero(zero_author)[0] for B in range(16))
    rec(out, "adjoint_equation", ok, "the prose equation parsed: the coefficient of d_a Psibar gamma^(a) equals the "
        "sympy 1/f_a for all eight a, the terms without derivative " + sp.sstr(ad_const[0]) + " Psibar gamma^(x0) + "
        + sp.sstr(ad_const[1]) + " Psibar gamma^(x4) equal -Psibar Omega_mu gamma^mu (sympy: sum_mu Omega_mu gamma^mu = "
        "-(3/2) H e^a4 b4^(-1/2) gamma^(x0) - (b4'/b4 - a4'/2) gamma^(x4)), and the stated equation "
        "(... = -(m + U'(S)) Psibar), rebuilt in the jet algebra, equals the sympy D_mu Psibar gamma^mu = -(m + U') "
        "Psibar exactly, both statistics" + (f"; problems: {ad_prob}" if ad_prob else ""))
    # ---- current
    ok = True
    for stat in ("grassmann", "commuting"):
        sps = ctx["sps"][stat]
        pb, ps = sps.psibar(), sps.psi()
        J = sps.current()
        Ev, Eb = sps.dirac_E(), sps.dirac_Ebar()
        div = sps.zero()
        for mu in range(8):
            div = div + J[mu].scale(geo.sqrtg).total(mu, cd_author)
        Ebw = [-x for x in Eb]  # Wolfram's Ebar = D Psibar gamma + (m + U') Psibar = -(sympy Ebar)
        ident = div + (sps.dot(Ebw, ps) + sps.dot(pb, Ev)).scale(sp.I * geo.sqrtg)
        ok = ok and ident.expand().is_zero(zero_author)[0]
        chiB = sps.zero()
        for A in range(16):
            for Bb in range(16):
                if gm["B"][A, Bb] != 0:
                    chiB = chiB + (Alg.g(stat, gen(CHI, A)) * Alg.g(stat, gen(PSI, Bb))).scale(gm["B"][A, Bb])
        ok = ok and (J[X4] - chiB).expand().is_zero(zero_author)[0]
    ok = ok and F["current"] == STATED["current"]
    ok = ok and zero_author(geo.sqrtg - sgn * Q**4 * (c / sv) * w**3 / E)
    rec(out, "current", ok, "(statement verbatim) J^mu = -i Psibar gamma^mu Psi (the sympy current); d_mu(sqrt g J^mu) "
        "= -i sqrt g (Ebar Psi + Psibar E) with the Wolfram sign of Ebar (= minus the sympy Ebar) holds exactly (sqrt|g| "
        "= e^-a4 b4^2 |cot z| (sin^2 z)^(1/4)); J^x4 = Psi^dagger B Psi; both statistics; Q is the integral of "
        "sqrt|g| J^x4 over a slice x4 = const (conserved for fields that vanish at the boundary of the slice)")
    Rring = -12 * H**2 * E**2 / Q**2 + 8 * A1**2 - 2 * A2 - 8 * A1 * B1 + 4 * (B2 + B1**2) + B1**2  # b4''/b4 = B2 + B1^2
    ok = F["Lichnerowicz"] == STATED["Lichnerowicz"] and zero_author(geo.Rscalar - Rring)
    ok = ok and {"lichnerowicz_identity_on_fields", "lichnerowicz_contraction"} <= passed
    rec(out, "Lichnerowicz", ok, "(statement verbatim) (gamma^mu D_mu)^2 Psi = g^mu nu (D_mu D_nu - Gamma^l_mu nu "
        "D_l) Psi - (R/4) Psi is the identity proved on the jet space by the passing sympy check "
        "lichnerowicz_identity_on_fields (with gamma^mu gamma^nu F_mu nu = -(R/2) I16, lichnerowicz_contraction); "
        f"R = -12 H^2 e^(2 a4)/b4 + 8 a4'^2 - 2 a4'' - 8 a4' b4'/b4 + 4 b4''/b4 + (b4'/b4)^2 recomputed here (sympy: "
        f"{sp.sstr(geo.Rscalar)})")
    # ---- evolution form: d4 Psi = -g[x4] ((m + U') Psi - sum_(a != x4) (1/f_a) g[xa] d_a Psi - 3 H g[x0] Psi)
    #      - (3/4)(b4'/b4) Psi, rebuilt in the jet algebra and compared with the field equation solved for d4 Psi
    ok_ev = F["evolution_form"] == STATED["evolution_form"] and "hamiltonian_form_and_heisenberg_equation" in passed
    for stat in ("grassmann", "commuting"):
        sps = ctx["sps"][stat]
        ps = sps.psi()
        Mp = Alg.scalar(stat, m) + sps.S().scale(lam)
        inner_s = [Mp * ps[A] for A in range(16)]
        inner_w = [Mp * ps[A] for A in range(16)]
        for mu in range(8):
            if mu != X4:
                inner_s = [a - b for a, b in zip(inner_s, sps.matvec(geo.gam[mu], sps.Dpsi(mu)))]
                inner_w = [a - b for a, b in zip(inner_w, sps.matvec(G[mu] / geo.f[mu], sps.psi((mu,))))]
        inner_w = [a - b for a, b in zip(inner_w, sps.matvec(CG * G[X0], ps))]
        d4_s = sps.matvec(-G[X4], inner_s)
        d4_w = [a - b.scale(VG) for a, b in zip(sps.matvec(-G[X4], inner_w), ps)]
        ok_ev = ok_ev and all((x - y).expand().is_zero(zero_author)[0] for x, y in zip(d4_s, d4_w))
    rec(out, "evolution_form", ok_ev, "(statement verbatim) the stated d4 Psi = -g[x4]((m + U') Psi - sum_(a != x4) "
        "(1/f_a) g[xa] d_a Psi - (3/2) H e^a4 b4^(-1/2) g[x0] Psi) - (b4'/b4 - a4'/2) Psi, rebuilt in the jet algebra (U = "
        "(lambda/2) S^2), "
        "equals -gamma^(x4)[(m + U') Psi - sum_(mu != x4) gamma^mu D_mu Psi] (the sympy field equation solved for d4 "
        "Psi, with the sympy spin connection) exactly, both statistics; the Heisenberg form of the same equation is "
        "the passing sympy check hamiltonian_form_and_heisenberg_equation")
    # ---- energy-momentum tensor
    okv, oks, okd, okk, okx, okt = True, True, True, True, True, True
    for stat in ("grassmann", "commuting"):
        sps = ctx["sps"][stat]
        T, Tvar = ctx["T"][stat], ctx["Tvar"][stat]
        Tk, Tp, K, V = ctx["emt_parts"][stat]  # fields.Spinors.emt() of the sympy checks
        pb, ps = sps.psibar(), sps.psi()
        L0 = K - V
        Xm = [[sps.dot(pb, sps.matvec(geo.gam[nu], sps.Dpsi(mu))) -
               sps.dot(sps.vecmat(sps.Dpsibar(mu), geo.gam[nu]), ps) for mu in range(8)] for nu in range(8)]
        # W^{l nu rho} = Psibar {gamma^l, Sigma^{nu rho}} Psi, Sigma = (1/4)[gamma^nu, gamma^rho]
        Wt = {}
        for l in range(8):
            for nu in range(8):
                for r in range(8):
                    if nu == r:
                        Wt[(l, nu, r)] = sps.zero()
                        continue
                    Sig = (geo.gam[nu] * geo.gam[r] - geo.gam[r] * geo.gam[nu]) / 4
                    Mx = (geo.gam[l] * Sig + Sig * geo.gam[l]).applyfunc(sp.expand)
                    Wt[(l, nu, r)] = sps.dot(pb, sps.matvec(Mx, ps))
        for nu in range(8):
            for mu in range(8):
                # nabla_l W^{l nu rho} with rho = mu (g_mu rho diagonal)
                r = mu
                dW = sps.zero()
                for l in range(8):
                    dW = dW + Wt[(l, nu, r)].scale(geo.sqrtg).total(l, cd_author).scale(1 / geo.sqrtg)
                    for k in range(8):
                        if geo.Gam[nu][l][k] != 0:
                            dW = dW + Wt[(l, k, r)].scale(geo.Gam[nu][l][k])
                        if geo.Gam[r][l][k] != 0:
                            dW = dW + Wt[(l, nu, k)].scale(geo.Gam[r][l][k])
                Tw = (L0 if nu == mu else sps.zero()) - Xm[nu][mu].scale(sp.Rational(1, 2)) \
                    - dW.scale(geo.g[mu] / 4)
                okv = okv and (Tw - Tvar[nu][mu]).expand().is_zero(zero_author)[0]
                Ts = (L0 if nu == mu else sps.zero()) - (Xm[nu][mu] + Xm[mu][nu].scale(geo.g[mu] * geo.ginv[nu])) \
                    .scale(sp.Rational(1, 4))
                oks = oks and (Ts - T[nu][mu]).expand().is_zero(zero_author)[0]
                Tkw = (K if nu == mu else sps.zero()) - (Xm[nu][mu] + Xm[mu][nu].scale(geo.g[mu] * geo.ginv[nu])) \
                    .scale(sp.Rational(1, 4))
                okk = okk and (Tkw - Tk[nu][mu]).expand().is_zero(zero_author)[0]
                okk = okk and (Tp[nu][mu] - ((-V) if nu == mu else sps.zero())).expand().is_zero(zero_author)[0]
        Km = []
        for a in range(8):
            Ka = (sps.dot(pb, sps.matvec(G[a], sps.psi((a,)))) -
                  sps.dot(sps.vecmat(sps.psibar((a,)), G[a]), ps)).scale(1 / (2 * geo.f[a]))
            Km.append(Ka)
            okd = okd and (L0 - Ka - T[a][a]).expand().is_zero(zero_author)[0]
        sumK = sps.zero()
        for Ka in Km:
            sumK = sumK + Ka
        okd = okd and (sumK - K).expand().is_zero(zero_author)[0]
        tr = sps.zero()
        for a in range(8):
            tr = tr + T[a][a]
        okt = okt and (tr - sumK.scale(7) + V.scale(8)).expand().is_zero(zero_author)[0]
        B40 = sps.dot(pb, sps.matvec(G[X4], sps.psi((X0,)))) - sps.dot(sps.vecmat(sps.psibar((X0,)), G[X4]), ps)
        B04 = sps.dot(pb, sps.matvec(G[X0], sps.psi((X4,)))) - sps.dot(sps.vecmat(sps.psibar((X4,)), G[X0]), ps)
        f0 = geo.f[X0]
        T40 = (B40 - B04.scale(f0)).scale(-sp.Rational(1, 4))
        okx = okx and (T40 - T[X4][X0]).expand().is_zero(zero_author)[0]
        okx = okx and (T[X0][X4] + T[X4][X0].scale(1 / f0**2)).expand().is_zero(zero_author)[0]
    rec(out, "T_variation", okv and F["T_variation"] == STATED["T_variation"],
        "(statement verbatim) the stated closed form T^nu_mu = delta L0 - (1/2)(Psibar gamma^nu D_mu Psi - D_mu "
        "Psibar gamma^nu Psi) - (1/4) g_mu rho nabla_l (Psibar {gamma^l, Sigma^(nu rho)} Psi), rebuilt in the "
        "sympy algebra, equals the sympy first-order vielbein variation tensor OFF SHELL for all 64 components, "
        "both statistics (the sympy side had established equality with the Belinfante tensor on shell)")
    rec(out, "T_symmetric", oks and F["T_symmetric"] == STATED["T_symmetric"],
        "(statement verbatim) the stated Belinfante T^nu_mu, rebuilt in the sympy algebra, equals the sympy T^nu_mu off "
        "shell, 64 components, both statistics")
    rec(out, "EMT_kinetic_potential", okk and F["EMT_kinetic_potential"] == STATED["EMT_kinetic_potential"],
        "(statement verbatim) T_kin = delta sum K - (1/4)(...) and T_pot = -delta (m S + U), rebuilt in the sympy "
        "algebra, equal the sympy split, both statistics; hence rho_pot = -T_pot^x4_x4 = m S + U and p_pot = -(m S + U) "
        "in every direction")
    rec(out, "EMT_diagonal", okd and F["EMT_diagonal"] == STATED["EMT_diagonal"],
        "(statement verbatim) T^mu_mu (no sum) = L0 - K_mu with K_mu = (1/(2 f_mu))(Psibar gamma^(mu) d_mu Psi - d_mu "
        "Psibar gamma^(mu) Psi) and sum_mu K_mu = K: equal off shell, both statistics; with L0 = sum K - m S - U these "
        "are the stated rho = -sum_(mu != x4) K_mu + m S + U and p_mu = sum_(l != mu) K_l - m S - U")
    # trace: off shell in the sympy algebra (okt); on shell for a general U from sum_mu K_mu = (m + U') S
    Sg = sp.Symbol("S", real=True)
    Uf = sp.Function("U")
    dU = sp.diff(Uf(Sg), Sg)
    ok_tr = okt and sp.expand(7 * (m + dU) * Sg - 8 * (m * Sg + Uf(Sg)) - (-m * Sg + 7 * Sg * dU - 8 * Uf(Sg))) == 0
    Uq = lam * Sg**2 / 2
    ok_tr = ok_tr and sp.expand(-m * Sg + 7 * Sg * sp.diff(Uq, Sg) - 8 * Uq - (-m * Sg + 3 * lam * Sg**2)) == 0
    ok_tr = ok_tr and {"grassmann_trace_on_shell", "commuting_trace_on_shell"} <= passed
    ok_tr = ok_tr and F["EMT_trace"] == STATED["EMT_trace"]
    rec(out, "EMT_trace", ok_tr, "(statement verbatim) T^mu_mu = 8 L0 - sum K = 7 sum K - 8 (m S + U) off shell "
        "(rebuilt in the sympy algebra, both statistics); on shell the sympy checks grassmann_trace_on_shell and "
        "commuting_trace_on_shell (passing) verify -m S + 3 lambda S^2 for U = (lambda/2) S^2 by the prolonged on-shell "
        "substitution; recomputed here: 7 (m + U') S - 8 (m S + U) = -m S + 7 S U' - 8 U for a general U, and = -m S + "
        "3 lambda S^2 for U = (lambda/2) S^2. Counterparts of the Wolfram checks EMT_trace_G and EMT_trace_C")
    ok_h = F["EMT_homogeneous_on_shell"] == STATED["EMT_homogeneous_on_shell"]
    ok_h = ok_h and sp.expand(m * Sg + Uq - (m * Sg + lam * Sg**2 / 2)) == 0
    ok_h = ok_h and sp.expand(Sg * sp.diff(Uq, Sg) - Uq - lam * Sg**2 / 2) == 0
    ok_h = ok_h and sp.simplify((Sg * sp.diff(Uq, Sg) - Uq) / (m * Sg + Uq) - lam * Sg / (2 * m + lam * Sg)) == 0
    ok_h = ok_h and {"grassmann_homogeneous_on_shell_rho_p", "commuting_homogeneous_on_shell_rho_p"} <= passed
    rec(out, "EMT_homogeneous_on_shell", ok_h, "(statement verbatim) rho = m S + U and p3 = p_t = p0 = S U' - U are the "
        "statements of the passing sympy checks grassmann_homogeneous_on_shell_rho_p and "
        "commuting_homogeneous_on_shell_rho_p (verified there for U = (lambda/2) S^2 by the prolonged on-shell "
        "substitution, with T_kin^x4_x4 = 0 and T_kin^mu_mu = (m + U') S for mu != x4); the specialisations rho = m S + "
        "lambda S^2/2, p = lambda S^2/2 and w = lambda S/(2 m + lambda S) are recomputed here")
    rec(out, "EMT_offdiagonal_x4_x0", okx and {"grassmann_T_x4x0_homogeneous", "commuting_T_x4x0_homogeneous"} <= passed
        and F["EMT_offdiagonal_x4_x0"] == STATED["EMT_offdiagonal_x4_x0"],
        "(statement verbatim) T^x4_x0 = -(1/4)(B40 - f0 B04) and T^x0_x4 = -T^x4_x0/f0^2, f0 = e^-a4 b4^(1/2) cot z, equal "
        "the sympy "
        "components off shell, both statistics; on homogeneous on-shell states the sympy side finds T^x4_x0 = T^x0_x4 = "
        "0 (passing checks grassmann_T_x4x0_homogeneous, commuting_T_x4x0_homogeneous); the Wolfram side states "
        "T^x4_x0 = 0 at its exact solutions (exact_solution_x4_x0_*)")
    # ---- energy exchange: the complete identity nabla_mu T^mu_nu (all eight nu) for T = diag(p0, p3, p3, p3, -rho,
    # pt, pt, pt) with entries functions of x4 and x0, recomputed HERE from the sympy Christoffel symbols with the
    # general mixed-tensor formula d_mu T^mu_nu + Gamma^mu_(mu l) T^l_nu - Gamma^l_(mu nu) T^mu_l (the sympy check
    # uses the sqrt g form), and compared with the three InputForm entries of the Wolfram record
    okE, detE = energy_exchange_compare(F["energy_exchange"], geo)
    rec(out, "energy_exchange", okE and "energy_exchange_equation" in passed, detE)
    # ---- the remaining prose records, each re-derived here where it is a formula
    ok_nt = F["nontriviality"] == STATED["nontriviality"]
    tot_nt = sp.zeros(16, 16)
    for mu in range(8):
        M = (geo.gam[mu] * geo.Om[mu]).applyfunc(sp.expand)
        tot_nt += M
        if mu == X0:
            want = h4 / 2 * G[X4]
        elif mu in (1, 2, 3):
            want = A1 / 2 * G[X4]
        elif mu in (5, 6, 7):
            want = h4 / 2 * G[X4] + H * E / (2 * Q) * G[X0]
        else:
            want = sp.zeros(16, 16)
        ok_nt = ok_nt and all(zero_author(x) for x in (M - want))
    gOm = CG * G[X0] + VG * G[X4]
    ok_nt = ok_nt and all(zero_author(x) for x in (tot_nt - gOm))
    ok_nt = ok_nt and all(zero_author(x) for x in (gOm * gOm - (CG**2 - VG**2) * sp.eye(16)))
    ok_nt = ok_nt and {"gamma_mu_Omega_mu_equals_hidden_block_terms", "per_direction_terms",
                       "nontriviality_Omega_zero_iff_flat", "spinor_curvature_equals_riemann",
                       "gravity_term_square", "curvature_and_flat_member"} <= passed
    rec(out, "nontriviality", ok_nt, "(statement verbatim) recomputed here from the sympy matrices: gamma^(x0) Omega_x0 = "
        "(h4/2) gamma^(x4), gamma^(xi) Omega_xi = (a4'/2) gamma^(x4) (i = 1, 2, 3), gamma^(xt) Omega_xt = (h4/2) "
        "gamma^(x4) + (H/2) e^a4 b4^(-1/2) gamma^(x0) (t = 5, 6, 7), gamma^(x4) Omega_x4 = 0 (h4 = b4'/(2 b4) - a4'), the "
        "sum (3/2) H e^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) with square ((9/4) H^2 e^(2 a4)/b4 - (b4'/b4 "
        "- a4'/2)^2) I16 (sympy check gravity_term_square); the iff statement, [D_mu, D_nu] = curvature and the flat member "
        "a4 = 0, b4 = H^2 x4^2 are the passing sympy checks nontriviality_Omega_zero_iff_flat, "
        "spinor_curvature_equals_riemann and curvature_and_flat_member. Scope: the values belong to the diagonal vielbein "
        "(frame dependence: Revision/theory/reports/python-scope.json)")
    ok_mj = F["majorana_negative_control"] == STATED["majorana_negative_control"]
    ok_mj = ok_mj and {"negative_control_majorana_grassmann_total_derivative",
                       "negative_control_majorana_commuting_contrast"} <= passed
    spg, spc = ctx["sps"]["grassmann"], ctx["sps"]["commuting"]
    thg, thc = spg.theta(), spc.theta()
    ok_mj = ok_mj and len(spg.dot(spg.vecmat(thg, Cm), thg).expand()) == 0  # Psi^T C Psi = 0 (anticommuting)
    ok_mj = ok_mj and all(len(spc.dot(spc.vecmat(thc, Cm), spc.matvec(G[a], thc)).expand()) == 0 for a in range(8))
    rec(out, "majorana_negative_control", ok_mj, "(statement verbatim) the total derivative and the absence of field "
        "equations for anticommuting real components, and the Euler-Lagrange expression for commuting ones, are the "
        "passing sympy checks negative_control_majorana_grassmann_total_derivative and "
        "negative_control_majorana_commuting_contrast; recomputed here: Psi^T C Psi = 0 for 16 real anticommuting "
        "components and Phi^T C gamma^(a) Phi = 0 for 16 real commuting components, all a")
    al, S0 = sp.symbols("alpha S0", real=True)
    Kx = G[X4] * G[X0]
    M2 = -(m + lam * S0 * E / Q**4) * G[X4] + CG * Kx
    I16 = sp.eye(16)
    ok_ex = (Kx * Kx - I16).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_ex = ok_ex and (Kx * G[X4] + G[X4] * Kx).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_ex = ok_ex and (Cm * Kx + Kx.T * Cm).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_ex = ok_ex and all(zero_author(x) for x in (Cm * M2 + M2.T * Cm))
    Sb = S0 * E / Q**4  # S = e^a4 b4^(-2) S0
    ok_ex = ok_ex and sp.expand((m * Sg + Uq).subs(Sg, Sb) - (m * Sb + lam * Sb**2 / 2)) == 0 and \
        sp.expand((Sg * sp.diff(Uq, Sg) - Uq).subs(Sg, Sb) - lam * Sb**2 / 2) == 0
    ok_ex = ok_ex and F["exact_solutions"] == STATED["exact_solutions"]
    ok_ex = ok_ex and {"exact_solution_family_x4_x0", "exact_nonlinear_homogeneous_solution"} <= passed
    rec(out, "exact_solutions", ok_ex, "(statement verbatim) with the sympy gammas: K = gamma^(x4) gamma^(x0) has K^2 = "
        "I16, {K, gamma^(x4)} = 0 and C K + K^T C = 0 (the matrices of (i-a), (i-b) and (iii)), C M + M^T C = 0 for the "
        "x4-dependent M = -(m + lambda e^a4 b4^(-2) S0) gamma^(x4) + (3/2) H e^a4 b4^(-1/2) K of (ii) (so chi^dagger C chi "
        "is constant), and rho = m S + lambda S^2/2, p = S U' - U = lambda S^2/2 for U = lambda S^2/2 with S = e^a4 "
        "b4^(-2) S0; the solutions themselves - (i-a), (i-b), (ii) and the Grassmann solution (iii) in an explicit "
        "Grassmann algebra with N = 2 - are the passing sympy checks exact_solution_family_x4_x0 and "
        "exact_nonlinear_homogeneous_solution")
    wq = sp.simplify((Sg * sp.diff(Uq, Sg) - Uq) / (m * Sg + Uq) - lam * Sg / (2 * m + lam * Sg))
    ok_eo = F["equation_of_state_definitions"] == STATED["equation_of_state_definitions"] and wq == 0 and \
        {"grassmann_homogeneous_on_shell_rho_p", "commuting_homogeneous_on_shell_rho_p"} <= passed
    rec(out, "equation_of_state_definitions", ok_eo, "(statement verbatim) the same definitions as SPEC section 4 and "
        "the sympy record (rho = -T^x4_x4, p_mu = T^mu_mu); (S U' - U)/(m S + U) = lambda S/(2 m + lambda S) for U = "
        "lambda S^2/2 recomputed here; the homogeneous values from the passing sympy checks "
        "*_homogeneous_on_shell_rho_p")
    pp, qq, p1, q1 = sp.symbols("p q p1 q1", real=True)    # p, q functions of x0 with the jets p1 = d0 p, q1 = d0 q

    def d0j(e):
        return cd_author(e, X0) + sp.diff(e, pp) * p1 + sp.diff(e, qq) * q1

    cotr = c / sv
    lhs3 = w**3 * (pp * (q1 + sp.Rational(3, 2) * H * cotr * qq) + (p1 + sp.Rational(3, 2) * H * cotr * pp) * qq) \
        - d0j(w**3 * pp * qq)
    lhs0 = w**3 * (pp * q1 + p1 * qq) - d0j(w**3 * pp * qq)
    ok_hh = zero_author(lhs3) and zero_author(lhs0 + 3 * H * cotr * w**3 * pp * qq) and \
        F["hidden_direction_hermiticity"] == STATED["hidden_direction_hermiticity"]
    rec(out, "hidden_direction_hermiticity", ok_hh, "(statement verbatim) recomputed here in the ring (every real z): "
        "(sin^2 z)^(1/4) [p (d0 + (3/2) H cot z) q + ((d0 + (3/2) H cot z) p) q] = d0((sin^2 z)^(1/4) p q) identically, and "
        "without the (3/2) H term the same combination is d0((sin^2 z)^(1/4) p q) - 3 H cot z (sin^2 z)^(1/4) p q. Scope: "
        "antisymmetry for the measure sqrt g/f0 dx0 in the field variables Psi, up to the boundary term (sin^2 z)^(1/4) p "
        "q, which vanishes where sin z = 0 and not at the degenerate points cos z = 0 "
        "(Revision/theory/reports/python-scope.json)")
    segs = F["quantisation"].split("; ")
    mine_pass = {x["name"]: x["verdict"] == "pass" for x in checks}
    okq = segs == [a for a, _ in QUANTISATION_STATEMENTS]
    okq = okq and all(mine_pass.get(b, False) for _, bs in QUANTISATION_STATEMENTS for b in bs)
    okq = okq and (Cm * G[X4] - sp.I * gm["B"]).applyfunc(sp.expand) == sp.zeros(16, 16)
    rec(out, "quantisation", okq, f"the record consists of exactly these {len(QUANTISATION_STATEMENTS)} statements, "
        "each with passing sympy counterparts: " + "; ".join(f"'{a}' <-> {', '.join(bs)}"
                                                           for a, bs in QUANTISATION_STATEMENTS)
        + "; C gamma^(x4) = i B recomputed here. Convention note: the sympy side states the rule in two realisations - "
        "(i) Psi^dagger the adjoint in a Krein-Fock space: <:Psi^dagger M Psi:> = eps u^dagger M u (= u^dagger B M u "
        "for B-eigenvector modes); (ii) the positive Fock space with Psi^dagger = chi B: u^dagger B M u for particles, "
        "-v^dagger B M v for antiparticles (the Wolfram form). Scope: the conservation of integral sqrt g "
        "u^dagger v d^7x in the good sector holds up to the boundary terms at the degenerate points (record "
        "hidden_direction_hermiticity; Revision/theory/reports/python-scope.json); "
        "the EMT operator is a definition (normal ordering of the classical tensor), the same as the sympy record "
        "quantisation.emt_operator")
    covered = [x["name"] for x in out]
    missing = [k for k in F if k not in covered]
    extra = [k for k in covered if k not in F]
    duplicates = len(covered) != len(set(covered)) or len(ft["formulas"]) != len(F)
    # ---- check-by-check
    wv = {x["name"]: x["verdict"] for x in wr["checks"]}
    pairs = []
    used = set()
    for mine_name, wnames in CHECK_MAP:
        mv = next((x["verdict"] for x in checks if x["name"] == mine_name), "absent")
        ws = {w: wv.get(w, "absent") for w in wnames}
        used.update(wnames)
        agree = mv == "pass" and all(v == "PASS" for v in ws.values())
        pairs.append({"sympy_check": mine_name, "sympy_verdict": mv, "wolfram_checks": ws,
                      "agreement": "agree" if agree else "DISAGREE"})
    mine_unmapped = [x["name"] for x in checks if x["name"] not in {p[0] for p in CHECK_MAP}]
    w_unmapped = [n for n in wv if n not in used]
    # the unpaired checks need a written justification (and the algebra-report checks they cite must pass)
    alg_path = os.path.join(os.path.dirname(ft_path), "..", "algebra", "reports", "wolfram-algebra.json")
    av = {}
    if os.path.exists(alg_path):
        with open(alg_path, encoding="utf-8") as fh:
            av = {x["name"]: x["verdict"] for x in json.load(fh)["checks"]}
    just_sympy = []
    for n in mine_unmapped:
        reason, refs = SYMPY_ONLY.get(n, ("MISSING", []))
        just_sympy.append({"sympy_check": n, "justification": reason,
                           "wolfram_algebra_checks": {r: av.get(r, "absent") for r in refs}})
    just_wolfram = [{"wolfram_check": n, "justification": WOLFRAM_ONLY.get(n, "MISSING")} for n in w_unmapped]
    ok_just = all(j["justification"] != "MISSING" and all(v == "PASS" for v in j["wolfram_algebra_checks"].values())
                  for j in just_sympy) and all(j["justification"] != "MISSING" for j in just_wolfram)
    nf = sum(1 for x in out if x["verdict"] == "agree")
    npair = sum(1 for p in pairs if p["agreement"] == "agree")
    status = "agree" if (nf == len(out) and npair == len(pairs) and not missing and not extra and not duplicates
                         and ok_just) else "DISAGREEMENTS"
    return {
        "status": status,
        "wolfram_summary": wr.get("summary"),
        "formulas": {"compared": len(out), "agree": nf, "not_compared": missing, "records": out},
        "checks": {"pairs": len(pairs), "agree": npair, "records": pairs,
                   "sympy_checks_without_wolfram_counterpart": mine_unmapped,
                   "wolfram_checks_without_sympy_counterpart": w_unmapped,
                   "justifications": {"sympy_only": just_sympy, "wolfram_only": just_wolfram}},
    }
