"""Revision theory (sympy side): compare the sympy results with the Wolfram side's
Revision/theory/field-theory.json (formulas) and Revision/theory/reports/wolfram-field-theory.json (checks).

These two files are READ here, at the end, and only as data: every Wolfram formula is either parsed from its
InputForm string into sympy and compared with the sympy-side expression, or (for formulas given in prose) the
stated formula is re-built in the sympy jet algebra and compared with the sympy-side object exactly.
No Wolfram code is used."""

import json
import os
import re

import sympy as sp

from geometry import ETA, X4, X8, E, s, c, A1, A2, H, m, lam, cd_author, zero_author, canon_author
from superalg import Alg, gen, CHI, PSI

COORD = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
x8s = sp.Symbol("x8", real=True)
a4x = sp.Symbol("a4x", real=True)
Z = 6 * H * x8s


def to_wl_vars(expr):
    """sympy ring expression -> the variables used for parsed Wolfram strings."""
    return sp.sympify(expr).subs({E: sp.exp(a4x), s: sp.sin(Z) ** sp.Rational(1, 6), c: sp.cos(Z)})


def wl_parse(src):
    """Parse a (simple) Wolfram InputForm expression into sympy."""
    t = src
    t = t.replace("Derivative[1][a4][x4]", "A1").replace("Derivative[2][a4][x4]", "A2")
    t = t.replace("a4[x4]", "a4x")
    t = re.sub(r'dd\["x(\d)",\s*Psi\[(\d+)\]\]', r"dd_\1_\2", t)
    t = re.sub(r"Psi\[(\d+)\]", r"P_\1", t)
    t = re.sub(r'gamma\["x(\d)"\]', r"G_\1", t)
    for f in ("Sin", "Cos", "Tan", "Cot", "Sec", "Csc"):
        t = t.replace(f + "[", f.lower() + "(")
    t = t.replace("[", "(").replace("]", ")").replace("{", "[").replace("}", "]").replace("^", "**")
    names = {"sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot, "sec": sp.sec, "csc": sp.csc, "E": sp.E,
             "H": H, "x8": x8s,
             "a4x": a4x, "A1": A1, "A2": A2, "V": sp.Symbol("V"), "m": m}
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


FIELD_NAMES = ("rho", "p3", "pt", "p8")  # the entries of the diagonal T of the formula energy_exchange


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
    """wl_parse for expressions in the functions rho, p3, pt, p8 of (x4, x8) or of x4 alone:
    Derivative[1, 0][f][x4, x8] and Derivative[1][f][x4] -> f_4, Derivative[0, 1][f][x4, x8] -> f_8, f[..] -> f."""
    t = re.sub(r"Derivative\[1, 0\]\[(rho|p3|pt|p8)\]\[x4, x8\]", r"\1_4", src)
    t = re.sub(r"Derivative\[0, 1\]\[(rho|p3|pt|p8)\]\[x4, x8\]", r"\1_8", t)
    t = re.sub(r"Derivative\[1\]\[(rho|p3|pt|p8)\]\[x4\]", r"\1_4", t)
    t = re.sub(r"\b(rho|p3|pt|p8)\[x4(?:, x8)?\]", r"\1", t)
    return wl_parse(t)


def energy_exchange_compare(ew, geo):
    """Recompute nabla_mu T^mu_nu (all eight nu) for T = diag(p3, p3, p3, -rho, pt, pt, pt, p8), entries functions of
    x4 and x8, from the sympy Christoffel symbols with the general mixed-tensor formula
    d_mu T^mu_nu + Gamma^mu_(mu l) T^l_nu - Gamma^l_(mu nu) T^mu_l, and compare it with the Wolfram record
    [complete identity, conservation equations, x8-independent case] (three InputForm strings)."""
    f = {n: sp.Symbol(n) for n in FIELD_NAMES}
    f4 = {n: sp.Symbol(f"{n}_4") for n in FIELD_NAMES}
    f8 = {n: sp.Symbol(f"{n}_8") for n in FIELD_NAMES}
    T = sp.diag(f["p3"], f["p3"], f["p3"], -f["rho"], f["pt"], f["pt"], f["pt"], f["p8"])

    def d(e, mu):  # coordinate derivative: the metric ring plus the jets of the four entries
        r = cd_author(e, mu)
        if mu in (X4, X8):
            jet = f4 if mu == X4 else f8
            r += sum(sp.diff(e, f[n]) * jet[n] for n in FIELD_NAMES)
        return r

    mine = []
    for nu in range(8):
        v = sum(d(T[mu, nu], mu) for mu in range(8))
        v += sum(geo.Gam[mu][mu][l] * T[l, nu] for mu in range(8) for l in range(8))
        v -= sum(geo.Gam[l][mu][nu] * T[mu, l] for mu in range(8) for l in range(8))
        mine.append(sp.factor(canon_author(v)))
    cot = c / s**6
    shown = "; ".join(f"{COORD[nu]}: {sp.sstr(sp.expand(mine[nu]))}" for nu in range(8))
    if not isinstance(ew, list) or len(ew) != 3:
        return False, ("the Wolfram record energy_exchange is not the three-entry InputForm list [complete identity, "
                       "conservation equations, x8-independent case]; sympy recomputation: " + shown)
    # entry 1: the complete identity, component by component
    theirs = wl_parse_fields(ew[0])
    ok1 = len(theirs) == 8 and all(same(theirs[nu], to_wl_vars(mine[nu])) for nu in range(8))
    ok1 = ok1 and all(mine[nu] == 0 for nu in range(8) if nu not in (X4, X8))
    # entry 2: conservation <=> the two solved equations (each component linear in the solved derivative, -1 / +1)
    eqs = [tuple(wl_parse_fields(side) for side in e.split("==")) for e in wl_top_split(ew[1])]
    ok2 = len(eqs) == 2 and all(len(e) == 2 for e in eqs)
    ok2 = ok2 and eqs[0][0] == f4["rho"] and eqs[1][0] == f8["p8"]
    ok2 = ok2 and sp.expand(sp.diff(mine[X4], f4["rho"]) + 1) == 0 and zero_author(sp.diff(mine[X8], f8["p8"]) - 1)
    ok2 = ok2 and same(to_wl_vars(mine[X4]).subs(f4["rho"], eqs[0][1]), 0) and \
        same(to_wl_vars(mine[X8]).subs(f8["p8"], eqs[1][1]), 0)
    # entry 3: x8-independent entries; the x8 component is linear in p8 with coefficient 6 H cot z > 0
    eq3 = [tuple(wl_parse_fields(side) for side in e.split("==")) for e in wl_top_split(ew[2])]
    m8 = mine[X8].subs({f8[n]: 0 for n in FIELD_NAMES})
    ok3 = len(eq3) == 2 and all(len(e) == 2 for e in eq3) and eq3[0][0] == f4["rho"] and eq3[1][0] == f["p8"]
    ok3 = ok3 and same(to_wl_vars(mine[X4]).subs(f4["rho"], eq3[0][1]), 0) and \
        same(to_wl_vars(m8).subs(f["p8"], eq3[1][1]), 0) and zero_author(sp.diff(m8, f["p8"]) - 6 * H * cot)
    detail = ("the complete identity nabla_mu T^mu_nu, nu = x1..x8, for T = diag(p3, p3, p3, -rho, p_t, p_t, p_t, p8) "
              "with entries functions of x4 and x8, recomputed here from the sympy Christoffel symbols with the general "
              "mixed-tensor formula (f_4 = d f/d x4, f_8 = d f/d x8; ring c/s^6 = cot z): " + shown + ". Wolfram entry 1 "
              f"(the eight components) {'equals' if ok1 else 'DIFFERS from'} it component by component; entry 2 "
              f"(d rho/d x4 = -3 a4' (p3 - p_t), d p8/d x8 = -3 H cot z (2 p8 - p3 - p_t)) "
              f"{'is' if ok2 else 'is NOT'} equivalent to its vanishing; entry 3 (x8-independent entries: d rho/d x4 = "
              f"-3 a4' (p3 - p_t), p8 = (p3 + p_t)/2) {'is' if ok3 else 'is NOT'} equivalent to its vanishing "
              "(coefficient of p8 in the x8 component 6 H cot z > 0). Same statement as the sympy check "
              "energy_exchange_equation")
    return ok1 and ok2 and ok3, detail


def same(a, b):
    d = sp.simplify(sp.expand(a - b))
    if d == 0:
        return True
    return sp.simplify(sp.expand_trig(sp.trigsimp(d))) == 0


def rec(out, name, ok, detail):
    out.append({"name": name, "verdict": "agree" if ok else "DISAGREE", "detail": detail})


# ------------------------------------------------------------------ prose records
# The Wolfram side states 18 of its formula records in prose (field-theory.json).  Two of them, field_equation and
# adjoint_equation, are PARSED here (parse_dirac_prose).  The other sixteen are compared through the statement
# quoted verbatim below: the record agrees only if its text is exactly this statement AND the statement is
# re-derived here (or, where it is the statement of a sympy check, that check passes); a changed Wolfram text
# therefore shows up as a disagreement and has to be compared anew.  The record quantisation is in addition
# compared statement by statement (QUANTISATION_STATEMENTS).
STATED = {
    'Omega_components': (
        "Omega_xi = (1/2) E^a4[x4] Sin[6 H x8]^(1/6) (a4'[x4] g[xi].g[x4] + H g[xi].g[x8]) (i = 1, 2, 3); "
        "Omega_xt = -(1/2) E^-a4[x4] Sin[6 H x8]^(1/6) (a4'[x4] g[x4].g[xt] + H g[xt].g[x8]) (t = 5, 6, "
        '7); Omega_x4 = Omega_x8 = 0; g[xa] = gamma^(xa) (frame gammas of the fixture)'
    ),
    'Lagrangian': (
        'L = Cos[z] [ (1/2) sum_mu (Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m S - U(S) ] '
        '= Cos[z] [ (1/2) sum_a (1/f_a) (Psibar gamma^(a) d_a Psi - d_a Psibar gamma^(a) Psi) - m S - '
        'U(S) ]; f_(1,2,3) = E^a4 Sin[z]^(1/6), f_4 = 1, f_(5,6,7) = E^-a4 Sin[z]^(1/6), f_8 = Cot[z]'
    ),
    'current': (
        'J^mu = -i Psibar gamma^mu Psi; d_mu (Cos[z] J^mu) = -i Cos[z] (Ebar Psi + Psibar E); J^x4 = '
        'Psi^dagger B Psi; Q = Integral Cos[z] Psi^dagger B Psi dx1 dx2 dx3 dx5 dx6 dx7 dx8'
    ),
    'Lichnerowicz': (
        '(gamma^mu D_mu)^2 Psi = g^mu,nu (D_mu D_nu - Gamma^l_mu,nu D_l) Psi - (R/4) Psi, R = 6 '
        "(a4'[x4]^2 - 7 H^2)"
    ),
    'T_variation': (
        'T^nu_mu = delta^nu_mu L0 - (1/2) (Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi) - (1/4) '
        'g_mu,rho nabla_l (Psibar {gamma^l, Sigma^(nu rho)} Psi), Sigma^(nu rho) = (1/4) [gamma^nu, '
        'gamma^rho]'
    ),
    'T_symmetric': (
        'T^nu_mu = delta^nu_mu L0 - (1/4) (Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi + Psibar '
        'gamma_mu D^nu Psi - D^nu Psibar gamma_mu Psi)'
    ),
    'EMT_diagonal': (
        'K_mu = (1/(2 f_mu)) (Psibar gamma^(mu) d_mu Psi - d_mu Psibar gamma^(mu) Psi); L0 = sum_mu K_mu '
        '- m S - U(S); T^mu_mu = L0 - K_mu; rho = -T^x4_x4 = -sum_(mu != x4) K_mu + m S + U; p3 = T^x1_x1 '
        '(= T^x2_x2 = T^x3_x3 for isotropic states) = sum_(mu != x1) K_mu - m S - U; p_t = T^x5_x5 = '
        'sum_(mu != x5) K_mu - m S - U; p8 = T^x8_x8 = sum_(mu != x8) K_mu - m S - U'
    ),
    'EMT_kinetic_potential': (
        'T^nu_mu = T_kin^nu_mu + T_pot^nu_mu, T_pot^nu_mu = -delta^nu_mu (m S + U(S)), T_kin^nu_mu = '
        'delta^nu_mu sum_l K_l - (1/4)(Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi + Psibar '
        'gamma_mu D^nu Psi - D^nu Psibar gamma_mu Psi); potential energy density rho_pot = m S + U, '
        'potential pressure p_pot = -(m S + U) in every direction'
    ),
    'EMT_trace': (
        "T^mu_mu (sum) = 8 L0 - sum_mu K_mu = 7 sum_mu K_mu - 8 (m S + U); on shell = 7 (m + U') S - 8 (m "
        "S + U) = -m S + 7 S U' - 8 U"
    ),
    'EMT_homogeneous_on_shell': (
        "rho = m S + U(S); p3 = p_t = p8 = S U'(S) - U(S); w = (S U' - U)/(m S + U); for U = (lam/2) S^2: "
        'rho = m S + lam S^2/2, p = lam S^2/2, w = lam S/(2 m + lam S)'
    ),
    'EMT_offdiagonal_x4_x8': (
        'T^x4_x8 = -(1/4) (B48 - Cot[z] B84), B48 = Psibar gamma^(x4) d8 Psi - d8 Psibar gamma^(x4) Psi, '
        'B84 = Psibar gamma^(x8) d4 Psi - d4 Psibar gamma^(x8) Psi; T^x8_x4 = -Tan[z]^2 T^x4_x8 (T_x4x8 = '
        'T_x8x4)'
    ),
    'nontriviality': (
        'gamma^mu D_mu Psi - gamma^mu d_mu Psi = gamma^mu Omega_mu Psi = 3 H gamma^(x8) Psi (nonzero for '
        "every H > 0, every a4, every Psi != 0); per direction gamma^(xi) Omega_xi = (a4'/2) gamma^(x4) + "
        "(H/2) gamma^(x8) (i = 1, 2, 3, inflating) and gamma^(xt) Omega_xt = -(a4'/2) gamma^(x4) + (H/2) "
        "gamma^(x8) (t = 5, 6, 7, deflating): the time-direction terms cancel (3 a4'/2 - 3 a4'/2 = 0), "
        "the hidden-direction terms add (6 H/2 = 3 H); Omega_mu = 0 for all mu iff a4' = 0 and H = 0 (H = "
        '0 is a degenerate limit of the metric); [D_mu, D_nu] = (1/2) R_ab,mu,nu S^ab, and R^x8_x8 = -6 '
        'H^2 != 0: no frame removes Omega, the metric is never flat for H > 0'
    ),
    'majorana_negative_control': (
        'anticommuting real Psi: sqrt g Psi^T C gamma^mu D_mu Psi = d_mu ((1/2) sqrt g Psi^T C gamma^mu '
        'Psi) (a total derivative; no field equation; Psi^T C Psi = 0); commuting real Phi: '
        'Euler-Lagrange expression 2 sqrt g C gamma^mu D_mu Phi and Phi^T C gamma^mu Phi = 0'
    ),
    'exact_solutions': (
        '(i) U = 0: Psi = Sin[z]^al (Cosh[k x4] + Sinh[k x4]/k M) chi, M = -m g[x4] + 3 H (2 al + 1) '
        'g[x4].g[x8], k^2 = 9 H^2 (2 al + 1)^2 - m^2 (any a4); (ii) U = (lam/2) S^2, homogeneous: Psi = '
        '(Cosh[k x4] + Sinh[k x4]/k M) chi, M = -(m + lam S0) g[x4] + 3 H g[x4].g[x8], S0 = chi^dagger C '
        'chi, k^2 = 9 H^2 - (m + lam S0)^2 (commuting); Grassmann: Psi = sum_k [exp(M_m x4) + lam S0 d/dm '
        'exp(M_m x4)] chi_k theta_k, S0 = sum_kl thetabar_k theta_l chi_k^dagger C chi_l; at (ii): rho = '
        'm S0 + lam S0^2/2, p3 = p_t = p8 = lam S0^2/2'
    ),
    'equation_of_state_definitions': (
        'rho = -T^x4_x4, p3 = T^x1_x1, p_t = T^x5_x5, p8 = T^x8_x8; w3 = p3/rho, w_t = p_t/rho, w8 = '
        "p8/rho; homogeneous on shell: w3 = w_t = w8 = (S U' - U)/(m S + U)"
    ),
    'hidden_direction_hermiticity': (
        'Cos[z] [p (Tan[z] d8 + 3 H) q + ((Tan[z] d8 + 3 H) p) q] = d8 (Sin[z] p q): the operator Tan[z] '
        'd8 + 3 H is antisymmetric for the measure Cos[z] dx8 up to the boundary term Sin[z] p q, which '
        'does not vanish at z = Pi/2; without 3 H the mode operator is not formally Hermitian for this '
        'measure and these variables (Psi = Sin[z]^(-1/2) chi with the measure dy needs no such term)'
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
    """A prose expression with space-separated products, ' + ' sums and parenthesised groups -> sympy."""
    t = t.strip()
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
    (coefficients c_a of gamma^(a) d_a Psi (resp. d_a Psibar gamma^(a)), a = x1..x8, coefficient of the term
    without derivative (gamma^(x8) Psi resp. Psibar gamma^(x8)), right-hand side text, problems found)."""
    problems = []
    lhs, rhs = text.split(" = ")
    if adjoint:
        problems += [f"d{a} Psibar g[x{b}]" for a, b in re.findall(r"d(\d) Psibar g\[x(\d)\]", lhs) if a != b]
        t = re.sub(r"d(\d) Psibar g\[x\1\]", r"GD_\1", lhs).replace("Psibar g[x8]", "G_8")
    else:
        problems += [f"g[x{a}] d{b}" for a, b in re.findall(r"g\[x(\d)\] d(\d)", lhs) if a != b]
        t = re.sub(r"g\[x(\d)\] d\1", r"GD_\1", lhs).replace("g[x8] Psi", "G_8")
        t = re.sub(r"\bPsi\b", "", t)
    t = re.sub(r"\s+", " ", t).replace("( ", "(").replace(" )", ")").strip()
    t = re.sub(r"E\^-a4(\[x4\])?", "exp(-a4x)", t)
    t = re.sub(r"E\^a4(\[x4\])?", "exp(a4x)", t)
    t = t.replace("Sin[z]", "sin(Z)").replace("Tan[z]", "tan(Z)").replace("Cot[z]", "cot(Z)").replace("^", "**")
    gd = [sp.Symbol(f"GD_{a + 1}") for a in range(8)]
    g8 = sp.Symbol("G_8")
    loc = {"Z": Z, "a4x": a4x, "H": H, "G_8": g8}
    loc.update({str(x): x for x in gd})
    e = sp.expand(_prose_expr(t, loc))
    if not e.free_symbols <= set(gd) | {g8, H, x8s, a4x}:
        problems.append(f"unparsed symbols {sorted(map(str, e.free_symbols))}")
    coef = [e.coeff(x) for x in gd]
    rest = sp.expand(e - sum(cf * x for cf, x in zip(coef, gd)))
    const = rest.coeff(g8)
    if sp.expand(rest - const * g8) != 0 or any(cf.has(*gd, g8) for cf in coef) or const.has(*gd, g8):
        problems.append("terms of another form")
    return coef, const, rhs.strip(), problems


# the statements of the Wolfram record quantisation (separated by '; ') and their passing sympy counterparts
QUANTISATION_STATEMENTS = [
    ("pi_A = (i/2) Cos[z] (Psi^dagger B)_A", ["canonical_momentum"]),
    ("K = Cos[z] C gamma^(x4) = i Cos[z] B", ["canonical_momentum", "B_properties"]),
    ("{Psi_A(x), Psi^dagger_C(y)}_(x4 = y4) = B_AC delta^7(x - y)/Cos[z]", ["canonical_anticommutator_B"]),
    ("B = -i C gamma^(x4), B^dagger = B, B^2 = 1, signature (8,8)", ["B_properties"]),
    ("no positive inner product with Psi^dagger the adjoint (Krein space, fundamental symmetry B)",
     ["no_positive_inner_product"]),
    ("positive representation chi = Psi^dagger B, {Psi_A, chi_C} = delta_AC", ["good_sector_positive_fock_realisation"]),
    ("Heisenberg: d4 Psi = -i B (1/Cos[z]) dHd/dPsi^dagger = -gamma^(x4) [(m + U') Psi - sum_(a != 4) gamma^a D_a Psi]",
     ["hamiltonian_form_and_heisenberg_equation"]),
    ("good sector (no x5, x6, x7 dependence): h Hermitian for Cos[z] d^7x, positive Fock space, normal-ordered H = sum "
     "E (b^* b + d^* d) >= 0 per momentum", ["good_sector_spectrum_and_B_sectors", "good_sector_positive_fock_realisation"]),
    ("expectation-value rule <Psi^dagger M Psi> = u^dagger B M u (u^dagger u = 1, positive-energy good-sector u)",
     ["good_sector_positive_fock_realisation", "expectation_value_rule"]),
    ("EMT operator T^mu_nu = :T^mu_nu[Psi, Psi^dagger = chi B]: (normal ordered), <T> by the same rule",
     ["good_sector_positive_fock_realisation"]),
    ("extra-time modes: E^2 = m^2 + k_s^2 - k_t^2 < 0 for k_t^2 > m^2 + k_s^2, growing as exp(|E| x4)",
     ["mode_hamiltonian_B_selfadjoint_dispersion", "extra_time_modes_grow"]),
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
    ("metric_from_vielbein_equals_SPEC", ["metric_is_the_authors", "vielbein_inverse"]),
    ("sqrt_det_g_equals_cos_z", ["sqrt_det_g_is_cos_z"]),
    ("christoffel_symmetric_metric_compatible", ["christoffel_count"]),
    ("spin_connection_antisymmetric", ["omega_antisymmetric"]),
    ("vielbein_postulate", ["vielbein_postulate"]),
    ("Omega_x4_and_Omega_x8_vanish", ["Omega_components", "omega_components"]),
    ("covariant_constancy_D_mu_gamma_nu", ["gamma_covariantly_constant", "S_rotates_gamma_with_omega"]),
    ("gamma_mu_Omega_mu_equals_3H_gamma_x8", ["gammaOmega_equals_3H_gamma_x8"]),
    ("time_terms_cancel_hidden_term_survives", ["gammaOmega_x4_terms_cancel"]),
    ("anticommutator_gamma_Omega_vanishes", ["gammaOmega_divergence_form", "L_spin_connection_drops_out_G",
                                             "L_spin_connection_drops_out_C"]),
    ("divergence_of_sqrtg_gamma", ["gammaOmega_divergence_form"]),
    ("nontriviality_Omega_zero_iff_flat", ["Omega_vanishes_iff_a4prime_and_H_vanish", "nontriviality_1_dirac16complex",
                                           "nontriviality_2_dirac16complex00", "degenerate_at_H_0"]),
    ("curvature_nonzero_flat_only_formally", ["ricci_scalar", "ricci_mixed_components", "never_flat_for_H_positive"]),
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
    ("grassmann_T_x4x8_homogeneous", ["T_x4_x8_component_G"]),
    ("commuting_T_x4x8_homogeneous", ["T_x4_x8_component_C"]),
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
    ("exact_solution_family_x4_x8", ["solution_matrix_square", "exact_solution_x4_x8_G", "exact_solution_x4_x8_C"]),
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
    rec(out, "vielbein_diagonal", all(same(fw[a], to_wl_vars(geo.f[a])) for a in range(8)), "f_a, a = x1..x8")
    rec(out, "sqrt_det_g", same(wl_parse(F["sqrt_det_g"]), to_wl_vars(geo.sqrtg)), "sqrt|det g| = cos(6 H x8)")
    rec(out, "eta", [int(x) for x in wl_parse(F["eta"])] == ETA, "eta = diag(1,1,1,-1,-1,-1,-1,1)")
    # ---- Christoffel symbols
    lst = wl_parse(F["christoffel_nonzero"])
    theirs = {(int(l) - 1, int(a) - 1, int(b) - 1): v for l, a, b, v in lst}
    mine = {(l, a, b): geo.Gam[l][a][b] for l in range(8) for a in range(8) for b in range(a, 8)
            if geo.Gam[l][a][b] != 0}
    ok = set(theirs) == set(mine) and all(same(theirs[k], to_wl_vars(mine[k])) for k in mine)
    rec(out, "christoffel_nonzero", ok, f"{len(theirs)} Wolfram vs {len(mine)} sympy nonzero Gamma^l_mn (m <= n); "
        "same index set and equal values")
    # ---- Ricci
    rw = wl_parse(F["ricci_mixed_diagonal"])
    rm = [geo.ginv[a] * geo.ricci[a][a] for a in range(8)]
    offd = all(geo.ricci[a][b] == 0 for a in range(8) for b in range(8) if a != b)
    rec(out, "ricci_mixed_diagonal", offd and all(same(rw[a], to_wl_vars(rm[a])) for a in range(8)),
        "R^mu_mu (no sum) for mu = x1..x8 equal; off-diagonal Ricci components vanish on both sides "
        f"(sympy: {[sp.sstr(sp.expand(x)) for x in rm]})")
    rec(out, "ricci_scalar", same(wl_parse(F["ricci_scalar"]), to_wl_vars(geo.Rscalar)),
        f"R = 6 (a4'^2 - 7 H^2) on both sides (sympy: {sp.sstr(geo.Rscalar)})")
    # ---- spin connection
    lst = wl_parse(F["omega_nonzero"])
    theirs = {(int(mu) - 1, int(a) - 1, int(b) - 1): v for mu, a, b, v in lst}
    mine = {(mu, a, b): geo.om[mu][a][b] for mu in range(8) for a in range(8) for b in range(a + 1, 8)
            if geo.om[mu][a][b] != 0}
    ok = set(theirs) == set(mine) and all(same(theirs[k], to_wl_vars(mine[k])) for k in mine)
    rec(out, "omega_nonzero", ok, f"{len(theirs)} Wolfram vs {len(mine)} sympy nonzero omega_mu,ab (a < b), equal")
    ok = True
    for i in range(3):
        Mi = (E * s * (A1 * G[i] * G[3] + H * G[i] * G[7]) / 2)
        ok = ok and all(zero_author(x) for x in (Mi - geo.Om[i]))
    for t in range(4, 7):
        Mt = -(s / E) * (A1 * G[3] * G[t] + H * G[t] * G[7]) / 2
        ok = ok and all(zero_author(x) for x in (Mt - geo.Om[t]))
    ok = ok and geo.Om[3] == sp.zeros(16, 16) and geo.Om[7] == sp.zeros(16, 16)
    ok = ok and F["Omega_components"] == STATED["Omega_components"]
    rec(out, "Omega_components", ok, "(statement verbatim) the stated Omega_xi = (1/2) E^a4 Sin^(1/6) (a4' g[xi].g[x4] + H g[xi].g[x8]), "
        "Omega_xt = -(1/2) E^-a4 Sin^(1/6) (a4' g[x4].g[xt] + H g[xt].g[x8]), Omega_x4 = Omega_x8 = 0, rebuilt from "
        "the gammas, equal the sympy Omega_mu exactly")
    lst = wl_parse(F["gammaOmega_per_direction"])
    ok = True
    for mu, a, b in lst:
        mu = int(mu) - 1
        M = (geo.gam[mu] * geo.Om[mu]).applyfunc(sp.expand)
        ok = ok and all(zero_author(x) for x in (M - a * G[3] - b * G[7]))
    rec(out, "gammaOmega_per_direction", ok, "gamma^mu Omega_mu (no sum) = (stated coefficient) gamma^(x4) + "
        "(stated coefficient) gamma^(x8) for all 8 mu, checked against the sympy matrices")
    tot = sp.zeros(16, 16)
    for mu in range(8):
        tot += geo.gam[mu] * geo.Om[mu]
    gt = wl_parse(F["gammaOmega_total"])
    ok = sp.expand(gt - 3 * H * sp.Symbol("G_8")) == 0 and all(zero_author(x) for x in (tot - 3 * H * G[7]))
    rec(out, "gammaOmega_total", ok, "3 H gamma^(x8) on both sides")
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
    # the stated f_a: f_(1,2,3) = E^a4 Sin[z]^(1/6), f_4 = 1, f_(5,6,7) = E^-a4 Sin[z]^(1/6), f_8 = Cot[z]
    f_stated = [sp.exp(a4x) * sp.sin(Z) ** sp.Rational(1, 6)] * 3 + [sp.Integer(1)] + \
        [sp.exp(-a4x) * sp.sin(Z) ** sp.Rational(1, 6)] * 3 + [sp.cot(Z)]
    res_L = res_L and all(same(f_stated[a], to_wl_vars(geo.f[a])) for a in range(8))
    res_L = res_L and F["Lagrangian"] == STATED["Lagrangian"]
    rec(out, "Lagrangian", res_L, "(statement verbatim) the stated L = Cos[z][(1/2) sum_a (1/f_a)(Psibar gamma^(a) d_a "
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
            sym = sp.Symbol(f"dd_{d[0]+1}_{B+1}") if d else sp.Symbol(f"P_{B+1}")
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
    ok = ok and all(same(fe_coef[a], to_wl_vars(1 / geo.f[a])) for a in range(8))
    ok = ok and all(same(to_wl_vars(x), y) for x, y in zip(tot, fe_const * G[7]))
    rec(out, "field_equation", ok, "the prose equation parsed: the coefficient of gamma^(a) d_a Psi equals the sympy "
        f"1/f_a for all eight a ({', '.join(sp.sstr(x) for x in fe_coef)}), the term without derivative "
        f"{sp.sstr(fe_const)} gamma^(x8) Psi equals the sympy gamma^mu Omega_mu Psi, and the right-hand side is (m + "
        "U'(S)) Psi; the 16 components of this operator are compared in field_equation_components"
        + (f"; problems: {fe_prob}" if fe_prob else ""))
    blocks = F["field_equation_blocks"]
    ok = True
    for entry in blocks:
        a = int(re.search(r'"x(\d)"', entry).group(1)) - 1
        tb, tt = wl_parse(re.sub(r'"x\d",\s*', "", entry, count=1))
        Mb = sp.zeros(16, 16)
        Mb[0:8, 8:16] = sp.Matrix(tb)
        Mb[8:16, 0:8] = sp.Matrix(tt)
        ok = ok and Mb == G[a]
    rec(out, "field_equation_blocks", ok and len(blocks) == 8,
        "gamma^(xa) = {{0, tb}, {t, 0}} with the listed 8x8 blocks, all 8 a: equal to the fixture gammas")
    ok = True
    OmG = sp.zeros(16, 16)
    for mu in range(8):
        OmG += geo.Om[mu] * geo.gam[mu]
    ok = all(zero_author(x) for x in (OmG + 3 * H * G[7]))
    for stat in ("grassmann", "commuting"):
        sps = ctx["sps"][stat]
        pb = sps.psibar()
        lhs = sps.vecmat(pb, 3 * H * G[7])
        for a in range(8):
            lhs = sps.vadd(lhs, sps.vecmat(sps.psibar((a,)), G[a] / geo.f[a]))
        Mp = Alg.scalar(stat, m) + sps.S().scale(lam)
        Eb = sps.dirac_Ebar()
        ok = ok and all((lhs[B] + Mp * pb[B] + Eb[B]).expand().is_zero(zero_author)[0] for B in range(16))
    rec(out, "adjoint_equation", ok, "sum_mu Omega_mu gamma^mu = -3 H gamma^(x8), so the stated adjoint form "
        "(... + 3 H Psibar g[x8] = -(m + U') Psibar) equals the sympy D_mu Psibar gamma^mu = -(m + U') Psibar "
        "exactly, both statistics")
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
    rec(out, "current", ok, "d_mu(Cos z J^mu) = -i Cos z (Ebar Psi + Psibar E) with the Wolfram sign of Ebar "
        "(= minus the sympy Ebar) holds exactly; J^x4 = Psi^dagger B Psi; both statistics")
    rec(out, "Lichnerowicz", "6 (a4'[x4]^2 - 7 H^2)" in F["Lichnerowicz"] and "- (R/4) Psi" in F["Lichnerowicz"]
        and sp.expand(geo.Rscalar - 6 * (A1**2 - 7 * H**2)) == 0,
        "(gamma^mu D_mu)^2 = Box - R/4 with R = 6 (a4'^2 - 7 H^2): same statement as the sympy check "
        "lichnerowicz_identity_on_fields")
    # ---- energy-momentum tensor
    okv, oks, okd, okk, okx, okt = True, True, True, True, True, True
    for stat in ("grassmann", "commuting"):
        sps = ctx["sps"][stat]
        T, Tvar = ctx["T"][stat], ctx["Tvar"][stat]
        _, Tk, Tp, K, V = sps.emt()
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
        B48 = sps.dot(pb, sps.matvec(G[3], sps.psi((7,)))) - sps.dot(sps.vecmat(sps.psibar((7,)), G[3]), ps)
        B84 = sps.dot(pb, sps.matvec(G[7], sps.psi((3,)))) - sps.dot(sps.vecmat(sps.psibar((3,)), G[7]), ps)
        T48 = (B48 - B84.scale(c / s**6)).scale(-sp.Rational(1, 4))
        okx = okx and (T48 - T[3][7]).expand().is_zero(zero_author)[0]
        okx = okx and (T[7][3] + T[3][7].scale(s**12 / c**2)).expand().is_zero(zero_author)[0]
    rec(out, "T_variation", okv, "the stated closed form T^nu_mu = delta L0 - (1/2)(Psibar gamma^nu D_mu Psi - D_mu "
        "Psibar gamma^nu Psi) - (1/4) g_mu rho nabla_l (Psibar {gamma^l, Sigma^(nu rho)} Psi), rebuilt in the "
        "sympy algebra, equals the sympy first-order vielbein variation tensor OFF SHELL for all 64 components, "
        "both statistics (the sympy side had established equality with the Belinfante tensor on shell)")
    rec(out, "T_symmetric", oks, "the stated Belinfante T^nu_mu equals the sympy T^nu_mu off shell, 64 components, "
        "both statistics")
    rec(out, "EMT_kinetic_potential", okk, "T_kin = delta sum K - (1/4)(...), T_pot = -delta (m S + U) equal the "
        "sympy split, both statistics")
    rec(out, "EMT_diagonal", okd, "T^mu_mu (no sum) = L0 - K_mu, K_mu = (1/(2 f_mu))(Psibar gamma^(mu) d_mu Psi - "
        "d_mu Psibar gamma^(mu) Psi), sum_mu K_mu = K: equal off shell, both statistics")
    rec(out, "EMT_trace", okt and "-m S + 7 S U' - 8 U" in F["EMT_trace"],
        "T^mu_mu = 7 sum K - 8 (m S + U) off shell (sympy algebra) and the same on-shell value -m S + 7 S U' - 8 U")
    hw = F["EMT_homogeneous_on_shell"]
    rec(out, "EMT_homogeneous_on_shell", all(x in hw for x in ("rho = m S + U(S)", "p3 = p_t = p8 = S U'(S) - U(S)",
                                                                "w = lam S/(2 m + lam S)")) and
        {"grassmann_homogeneous_on_shell_rho_p", "commuting_homogeneous_on_shell_rho_p"} <= passed,
        "rho = m S + U, p3 = p_t = p8 = S U' - U, w = lambda S/(2 m + lambda S): the same statements as the passing "
        "sympy checks grassmann_homogeneous_on_shell_rho_p and commuting_homogeneous_on_shell_rho_p (verified there by "
        "on-shell substitution)")
    rec(out, "EMT_offdiagonal_x4_x8", okx and {"grassmann_T_x4x8_homogeneous", "commuting_T_x4x8_homogeneous"} <= passed,
        "T^x4_x8 = -(1/4)(B48 - Cot[z] B84) and T^x8_x4 = -Tan[z]^2 T^x4_x8 equal the sympy components off shell, both "
        "statistics; on homogeneous on-shell states the sympy side finds T^x4_x8 = T^x8_x4 = 0 (passing checks "
        "grassmann_T_x4x8_homogeneous, commuting_T_x4x8_homogeneous); the Wolfram side states T^x4_x8 = 0 at its "
        "exact solutions (exact_solution_x4_x8_*)")
    # ---- energy exchange: the complete identity nabla_mu T^mu_nu (all eight nu) for T = diag(p3, p3, p3, -rho, pt,
    # pt, pt, p8) with entries functions of x4 and x8, recomputed HERE from the sympy Christoffel symbols with the
    # general mixed-tensor formula d_mu T^mu_nu + Gamma^mu_(mu l) T^l_nu - Gamma^l_(mu nu) T^mu_l (the sympy check
    # uses the sqrt g form), and compared with the three InputForm entries of the Wolfram record
    okE, detE = energy_exchange_compare(F["energy_exchange"], geo)
    rec(out, "energy_exchange", okE and "energy_exchange_equation" in passed, detE)
    # ---- the five prose records (statements of checks), each re-derived here where it is a formula
    nt = F["nontriviality"]
    tot_nt = sp.zeros(16, 16)
    for mu in range(8):
        tot_nt += geo.gam[mu] * geo.Om[mu]
    r88 = sp.expand(geo.ginv[X8] * geo.ricci[X8][X8])
    ok_nt = all(x in nt for x in ("= 3 H gamma^(x8) Psi", "(a4'/2) gamma^(x4) + (H/2) gamma^(x8)",
                                  "-(a4'/2) gamma^(x4) + (H/2) gamma^(x8)", "iff a4' = 0 and H = 0",
                                  "R^x8_x8 = -6 H^2"))
    ok_nt = ok_nt and all(zero_author(x) for x in (tot_nt - 3 * H * G[7])) and zero_author(r88 + 6 * H**2)
    ok_nt = ok_nt and {"gamma_mu_Omega_mu_equals_3H_gamma_x8", "time_terms_cancel_hidden_term_survives",
                       "nontriviality_Omega_zero_iff_flat", "spinor_curvature_equals_riemann"} <= passed
    rec(out, "nontriviality", ok_nt, "the stated values gamma^mu Omega_mu = 3 H gamma^(x8) and R^x8_x8 = -6 H^2 are "
        "recomputed here (sympy matrices and Ricci tensor); the per-direction and iff statements are those of the "
        "passing sympy checks gamma_mu_Omega_mu_equals_3H_gamma_x8, time_terms_cancel_hidden_term_survives, "
        "nontriviality_Omega_zero_iff_flat, spinor_curvature_equals_riemann. Scope: the values belong to the "
        "diagonal vielbein (frame dependence: Revision/theory/reports/python-scope.json)")
    mj = F["majorana_negative_control"]
    ok_mj = all(x in mj for x in ("a total derivative", "no field equation", "Psi^T C Psi = 0",
                                  "2 sqrt g C gamma^mu D_mu Phi")) and \
        {"negative_control_majorana_grassmann_total_derivative", "negative_control_majorana_commuting_contrast"} <= passed
    rec(out, "majorana_negative_control", ok_mj, "the statement (total derivative and no field equation for "
        "anticommuting real components; Euler-Lagrange expression 2 sqrt g C gamma^mu D_mu Phi for commuting ones) is "
        "the content of the passing sympy checks negative_control_majorana_grassmann_total_derivative and "
        "negative_control_majorana_commuting_contrast")
    ex = F["exact_solutions"]
    al, S0 = sp.symbols("alpha S0", real=True)
    M1 = -m * G[3] + 3 * H * (2 * al + 1) * G[3] * G[7]
    M2 = -(m + lam * S0) * G[3] + 3 * H * G[3] * G[7]
    I16 = sp.eye(16)
    ok_ex = (M1 * M1 - (9 * H**2 * (2 * al + 1)**2 - m**2) * I16).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_ex = ok_ex and (M2 * M2 - (9 * H**2 - (m + lam * S0)**2) * I16).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_ex = ok_ex and (Cm * M1 + M1.T * Cm).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_ex = ok_ex and (Cm * M2 + M2.T * Cm).applyfunc(sp.expand) == sp.zeros(16, 16)
    Sx = sp.Symbol("S")
    Ux = lam * Sx**2 / 2
    ok_ex = ok_ex and sp.expand((m * Sx + Ux).subs(Sx, S0) - (m * S0 + lam * S0**2 / 2)) == 0 and \
        sp.expand((Sx * sp.diff(Ux, Sx) - Ux).subs(Sx, S0) - lam * S0**2 / 2) == 0
    ok_ex = ok_ex and all(x in ex for x in ("M = -m g[x4] + 3 H (2 al + 1) g[x4].g[x8]",
                                            "k^2 = 9 H^2 (2 al + 1)^2 - m^2",
                                            "M = -(m + lam S0) g[x4] + 3 H g[x4].g[x8]",
                                            "k^2 = 9 H^2 - (m + lam S0)^2", "rho = m S0 + lam S0^2/2",
                                            "p3 = p_t = p8 = lam S0^2/2"))
    ok_ex = ok_ex and {"exact_solution_family_x4_x8", "exact_nonlinear_homogeneous_solution"} <= passed
    rec(out, "exact_solutions", ok_ex, "with the sympy gammas: M^2 = (9 H^2 (2 alpha + 1)^2 - m^2) I16 and "
        "M^2 = (9 H^2 - (m + lambda S0)^2) I16 for the two stated M, C M + M^T C = 0 for both (S constant), and "
        "rho = m S0 + lambda S0^2/2, p = S U' - U = lambda S0^2/2 for U = lambda S^2/2; the solutions themselves are "
        "the passing sympy checks exact_solution_family_x4_x8 and exact_nonlinear_homogeneous_solution")
    eo = F["equation_of_state_definitions"]
    wq = sp.simplify((Sx * sp.diff(Ux, Sx) - Ux) / (m * Sx + Ux) - lam * Sx / (2 * m + lam * Sx))
    ok_eo = all(x in eo for x in ("rho = -T^x4_x4", "p3 = T^x1_x1", "p_t = T^x5_x5", "p8 = T^x8_x8",
                                  "w3 = p3/rho", "(S U' - U)/(m S + U)")) and wq == 0 and \
        {"grassmann_homogeneous_on_shell_rho_p", "commuting_homogeneous_on_shell_rho_p"} <= passed
    rec(out, "equation_of_state_definitions", ok_eo, "same definitions as SPEC section 4 and the sympy record; "
        "(S U' - U)/(m S + U) = lambda S/(2 m + lambda S) for U = lambda S^2/2 recomputed here; homogeneous values "
        "from the passing sympy checks *_homogeneous_on_shell_rho_p")
    hh = F["hidden_direction_hermiticity"]
    pf, qf = sp.Function("p")(x8s), sp.Function("q")(x8s)
    op = lambda f, k3: sp.tan(Z) * sp.diff(f, x8s) + k3 * f
    lhs3 = sp.cos(Z) * (pf * op(qf, 3 * H) + op(pf, 3 * H) * qf) - sp.diff(sp.sin(Z) * pf * qf, x8s)
    lhs0 = sp.cos(Z) * (pf * op(qf, 0) + op(pf, 0) * qf) - sp.diff(sp.sin(Z) * pf * qf, x8s)
    ok_hh = sp.simplify(lhs3) == 0 and sp.simplify(lhs0 + 6 * H * sp.cos(Z) * pf * qf) == 0 and \
        "Cos[z] [p (Tan[z] d8 + 3 H) q + ((Tan[z] d8 + 3 H) p) q] = d8 (Sin[z] p q)" in hh
    rec(out, "hidden_direction_hermiticity", ok_hh, "recomputed here: cos z [p (tan z d8 + 3H) q + ((tan z d8 + 3H) "
        "p) q] = d8(sin z p q) identically, and without the 3H term the same combination is d8(sin z p q) - 6 H cos z "
        "p q. Scope: this is antisymmetry for the measure cos z dx8 in the field variables Psi, up to the boundary "
        "term sin z p q, which does not vanish at z = pi/2 (Revision/theory/reports/python-scope.json)")
    q = F["quantisation"]
    items = [("pi_A = (i/2) Cos[z] (Psi^dagger B)_A", "canonical_momentum"),
             ("{Psi_A(x), Psi^dagger_C(y)}_(x4 = y4) = B_AC delta^7(x - y)/Cos[z]", "canonical_anticommutator_B"),
             ("signature (8,8)", "B_properties"),
             ("no positive inner product", "no_positive_inner_product"),
             ("positive representation chi = Psi^dagger B", "good_sector_positive_fock_realisation"),
             ("h Hermitian", "good_sector_spectrum_and_B_sectors"),
             ("<Psi^dagger M Psi> = u^dagger B M u", "good_sector_positive_fock_realisation"),
             ("E^2 = m^2 + k_s^2 - k_t^2", "mode_hamiltonian_B_selfadjoint_dispersion")]
    mine_pass = {x["name"]: x["verdict"] == "pass" for x in checks}
    okq = all(a in q and mine_pass.get(b, False) for a, b in items)
    rec(out, "quantisation", okq, "each statement of the Wolfram quantisation summary is present and has a passing "
        "sympy counterpart: " + "; ".join(f"'{a}' <-> {b}" for a, b in items) + ". Convention note: the sympy side "
        "states the rule in two realisations - (i) Psi^dagger the adjoint in a Krein-Fock space: <:Psi^dagger M "
        "Psi:> = eps u^dagger M u (= u^dagger B M u for B-eigenvector modes); (ii) the positive Fock space with "
        "Psi^dagger = chi B: u^dagger B M u for particles, -v^dagger B M v for antiparticles (the Wolfram form)")
    covered = {x["name"] for x in out}
    missing = [k for k in F if k not in covered and k not in ("field_equation",)]
    # the prose field_equation is the sum of the 16 components (compared above)
    rec(out, "field_equation", "3 H g[x8] Psi = (m + U'(S)) Psi" in F["field_equation"] and
        any(x["name"] == "field_equation_components" and x["verdict"] == "agree" for x in out),
        "prose form of the 16 compared component equations")
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
    nf = sum(1 for x in out if x["verdict"] == "agree")
    npair = sum(1 for p in pairs if p["agreement"] == "agree")
    status = "agree" if nf == len(out) and npair == len(pairs) and not missing else "DISAGREEMENTS"
    return {
        "status": status,
        "wolfram_summary": wr.get("summary"),
        "formulas": {"compared": len(out), "agree": nf, "not_compared": missing, "records": out},
        "checks": {"pairs": len(pairs), "agree": npair, "records": pairs,
                   "sympy_checks_without_wolfram_counterpart": mine_unmapped,
                   "wolfram_checks_without_sympy_counterpart": w_unmapped},
    }
