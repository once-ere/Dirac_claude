"""Revision theory (sympy side): the exact nonlinear homogeneous solution of dirac16complex (Grassmann field,
U = (lambda/2) S^2, MASS m = 0) in the CORRECTED metric of 2026-10-16 (general a4 and b4 > 0, every real z), in an
EXPLICIT Grassmann algebra with N = 2 generators theta_1, theta_2 and their conjugates thetabar_1, thetabar_2, verified
exactly (written anew; no code shared with the Wolfram side).

    Psi = F sum_k [P chi_k + lambda S0 eta_k] theta_k,   F = e^(a4/2) b4^(-1),   K = gamma^(x4) gamma^(x0),
    P = cosh(I0) I + sinh(I0) K,   I0' = cg = (3/2) H e^a4 b4^(-1/2),
    eta_k = -P gamma^(x4) (Ic I + Is K) chi_k,   Ic' = F^2 cosh(2 I0),   Is' = F^2 sinh(2 I0),
    S0 = sum_kl thetabar_k theta_l chi_k^dagger C chi_l   (even, nilpotent: S0^2 != 0, S0^2 Psi = 0),

with 16 generic complex constants per generator (chi_k components q_Bk; their conjugates qc_Bk).  chi = Psi/F solves
the homogeneous equation chi' = (-lambda F^2 S0 gamma^(x4) + cg K) chi; its degree-1 part is P chi_k (K^2 = 1), and
eta_k is the variation-of-constants solution of eta_k' = cg K eta_k - F^2 gamma^(x4) P chi_k, eta_k(0) = 0
(P^-1 gamma^(x4) P = gamma^(x4) (cosh 2 I0 + sinh 2 I0 K) because {K, gamma^(x4)} = 0).  The expansion terminates
because S0^2 Psi = 0.  For m != 0 the linear system chi' = (-m gamma^(x4) + cg K) chi has no closed-form fundamental
matrix for general a4, b4 (cg depends on x4); the commuting nonlinear case of check_field_theory.py covers every m.
(Until 2026-10-16 this module verified the solution for the metric of 2026-10-14, with the constant coefficient 3 H
and a closed form for every m.)

Verified here:
  * S = Psibar Psi = F^2 S0 exactly (in the explicit algebra), S0 real, S0^2 != 0, S0^2 Psi = 0;
  * the field equation: the sympy jet expressions E_A = (gamma^mu D_mu Psi - (m + lambda S) Psi)_A of
    fields.Spinors (Grassmann, lambda general, m = 0), evaluated at the solution in the explicit algebra, vanish for
    all 16 A; control: without the correction lambda S0 eta_k the equation fails;
  * the energy-momentum tensor of fields.Spinors.emt() at the solution (m = 0): -T^x4_x4 = (lambda/2) S^2,
    T^mu_mu = (lambda/2) S^2 for mu != x4 (S = F^2 S0), and nabla_mu T^mu_nu = 0 for all eight nu, through the
    exact contraction T_kin = B[Y0] + lambda S0 B[Y1] (B[Y] = sum_kl thetabar_k theta_l chi_k^dagger Y chi_l; the
    potential part is -delta V, V = (lambda/2) S^2 = lambda S0 B[(1/2) F^4 C]); the contraction is cross-checked
    against the direct evaluation in the explicit algebra for T_kin^x0_x0 (x0 = the hidden direction).

Coefficients: Ch = cosh(I0), Sh = sinh(I0), the integrals Ic, Is and the metric ring of geometry.py (E = e^a4,
Q = b4^(1/2), B1 = b4'/b4, sv, c, w, sgn), with d/dx4: Ch -> cg Sh, Sh -> cg Ch, Ic -> F^2 (Ch^2 + Sh^2),
Is -> 2 F^2 Sh Ch, and the ring derivative cd_author; the exact zero test reduces Ch^2 -> 1 + Sh^2 and the ring
relations of geometry.reduce_author in the numerator."""

import sympy as sp

from superalg import Alg, gen, CHI, PSI
from geometry import X0, X4, H, m, lam, E, Q, cd_author, zero_author, reduce_author

NG = 2
GEN0 = 100  # generator keys (PSI, 100 + k) = theta_k, (CHI, 100 + k) = thetabar_k (conjugation maps PSI <-> CHI)
Ch, Sh = sp.symbols("Ch Sh", real=True)
Ic, Is = sp.symbols("Ic Is", real=True)
CG = sp.Rational(3, 2) * H * E / Q               # cg = (3/2) H e^a4 b4^(-1/2)
F = sp.sqrt(E) / Q**2                            # e^(a4/2) b4^(-1)
F2 = E / Q**4                                    # F^2
INTEGRAND = {Ic: F2 * (Ch**2 + Sh**2), Is: 2 * F2 * Sh * Ch}


def _theta(k):
    return Alg.g("grassmann", gen(PSI, GEN0 + k))


def _thetabar(k):
    return Alg.g("grassmann", gen(CHI, GEN0 + k))


def d4c(v):
    """d/dx4 of an explicit coefficient (cosh(I0), sinh(I0), the integrals Ic, Is and the metric ring)."""
    r = sp.diff(v, Ch) * CG * Sh + sp.diff(v, Sh) * CG * Ch + cd_author(v, X4)
    for sym, val in INTEGRAND.items():
        r += sp.diff(v, sym) * val
    return r


def reduce_form(v):
    """Normal form of the numerator: Ch^2 -> 1 + Sh^2, then the ring relations (c^2 + sv^2 = 1, w^12 = sv^2,
    sgn^2 = 1), so the expression is zero iff the result is 0."""
    v = sp.sympify(v)
    if v == 0:
        return sp.Integer(0)
    num, _ = sp.fraction(sp.together(v))
    num = sp.expand(num)
    if num == 0:
        return num
    if num.has(Ch):
        num = sp.expand(sp.rem(sp.Poly(num, Ch), sp.Poly(Ch**2 - 1 - Sh**2, Ch)).as_expr())
    return reduce_author(num)


def zt(v):
    return reduce_form(v) == 0


def verify(gm, geo, sps, Tk, Tp, V):
    """sps: fields.Spinors('grassmann', geo, ..., m, lam); Tk, Tp, V from sps.emt().  The solution has m = 0; the
    jet expressions are evaluated at m = 0.  Returns (ok, detail)."""
    G, Cm = gm["gamma"], gm["C"]
    I16 = sp.eye(16)
    q = [[sp.Symbol(f"q{B+1}_{k+1}") for k in range(NG)] for B in range(16)]
    qc = [[sp.Symbol(f"qc{B+1}_{k+1}") for k in range(NG)] for B in range(16)]
    swap = {}
    for B in range(16):
        for k in range(NG):
            swap[q[B][k]], swap[qc[B][k]] = qc[B][k], q[B][k]

    def cconj(x):  # complex conjugation in the explicit algebra (q <-> qc; Alg.conj reverses products, I -> -I)
        return x.conj().map_coeffs(lambda v: v.xreplace(swap))

    def m0(x):  # evaluate a jet expression at m = 0
        return x.map_coeffs(lambda v: v.subs(m, 0))

    K = G[X4] * G[X0]
    ok_sq = (K * K - I16).applyfunc(sp.expand) == sp.zeros(16, 16) and \
        (K * G[X4] + G[X4] * K).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_c = (K.T * Cm + Cm * K).applyfunc(sp.expand) == sp.zeros(16, 16) and \
        (G[X4].T * Cm + Cm * G[X4]).applyfunc(sp.expand) == sp.zeros(16, 16)
    P = Ch * I16 + Sh * K
    W = -P * G[X4] * (Ic * I16 + Is * K)
    U0, U1 = (F * P).applyfunc(sp.expand), (F * W).applyfunc(sp.expand)
    chi = [sp.Matrix([q[B][k] for B in range(16)]) for k in range(NG)]
    chic = [sp.Matrix([qc[B][k] for B in range(16)]) for k in range(NG)]

    def contract(X):  # B[X] = sum_kl thetabar_k theta_l chi_k^dagger X chi_l
        e = Alg("grassmann")
        for k1 in range(NG):
            for k2 in range(NG):
                e = e + (_thetabar(k1) * _theta(k2)).scale(sp.expand((chic[k1].T * X * chi[k2])[0]))
        return e

    S0 = contract(Cm)

    def solution(with_correction):
        Pc = [U0 * chi[k] for k in range(NG)]
        Wc = [U1 * chi[k] for k in range(NG)]
        out = []
        for A in range(16):
            e = Alg("grassmann")
            for k in range(NG):
                e = e + _theta(k).scale(sp.expand(Pc[k][A]))
                if with_correction:
                    e = e + (S0 * _theta(k)).scale(sp.expand(lam * Wc[k][A]))
            out.append(e)
        return out

    Psi = solution(True)
    Psic = [cconj(x) for x in Psi]
    S02 = (S0 * S0).expand()
    ok_alg = (cconj(S0) - S0).is_zero(zt)[0] and len(S02) > 0 and all(len((S02 * x).expand()) == 0 for x in Psi)
    Sx = Alg("grassmann")
    for A in range(16):
        for B in range(16):
            if Cm[A, B] != 0:
                Sx = Sx + (Psic[A] * Psi[B]).scale(Cm[A, B])
    ok_S = (Sx - S0.scale(F2)).expand().is_zero(zt)[0]

    def rule_for(Pv):
        Pvc = [cconj(x) for x in Pv]
        dPv, dPvc = [x.map_coeffs(d4c) for x in Pv], [x.map_coeffs(d4c) for x in Pvc]

        def rule(key):
            kind, A, d = key
            if A >= GEN0:
                return None
            if d == ():
                return Pv[A] if kind == PSI else Pvc[A]
            if d == (X4,):
                return dPv[A] if kind == PSI else dPvc[A]
            return Alg("grassmann")  # homogeneous: no dependence on x0..x3, x5..x7
        return rule

    Ev = [m0(x) for x in sps.dirac_E()]
    rule = rule_for(Psi)
    ok_E = all(Ev[A].subst(rule).expand().is_zero(zt)[0] for A in range(16))
    rule_bad = rule_for(solution(False))
    ctrl_E = not Ev[0].subst(rule_bad).expand().is_zero(zt)[0]
    # energy-momentum tensor at the solution through the contraction B[.]
    Ud = {(): (U0, U1), (X4,): (U0.applyfunc(d4c), U1.applyfunc(d4c))}

    def at_solution(x):
        Y0, Y1 = sp.zeros(16, 16), sp.zeros(16, 16)
        for mono, v in x.t.items():
            if len(mono) != 2 or mono[0][0] != CHI or mono[1][0] != PSI:
                raise ValueError(f"T_kin is not a Psibar-Psi bilinear: {mono}")
            (_, A, d1), (_, B, d2) = mono
            if d1 not in Ud or d2 not in Ud:
                continue  # derivatives other than d4 vanish at a homogeneous solution
            a0, a1 = Ud[d1]
            b0, b1 = Ud[d2]
            N = sp.zeros(16, 16)
            N[A, B] = v.subs(m, 0)
            Y0 += a0.T * N * b0
            Y1 += a1.T * N * b0 + a0.T * N * b1
        return Y0.applyfunc(sp.expand), Y1.applyfunc(sp.expand)

    def mzt(M):
        return all(zt(e) for e in M)

    # T_pot = -delta V with the jet V = m S + (lambda/2) S^2; at the solution (m = 0) S = F^2 S0, so
    # V = lambda S0 B[(1/2) F^4 C] (it depends on x4 through F)
    Sj = sps.S()
    ok_pot = all((Tp[a][b] + (V if a == b else Alg("grassmann"))).expand().is_zero(zero_author)[0]
                 for a in range(8) for b in range(8))
    ok_pot = ok_pot and (V - Sj.scale(m) - (Sj * Sj).scale(lam / 2)).expand().is_zero(zero_author)[0]
    Vy0, Vy1 = sp.zeros(16, 16), F2**2 * Cm / 2
    Xs = [[at_solution(Tk[a][b]) for b in range(8)] for a in range(8)]
    # -T^x4_x4 = -T_kin^x4_x4 + V and T^i_i = T_kin^i_i - V: -T_kin^x4_x4 = 0 and T_kin^i_i = lambda S^2
    # = lambda S0 B[F^4 C]
    ok_rp = mzt(Xs[X4][X4][0]) and mzt(Xs[X4][X4][1])
    ok_rp = ok_rp and all(mzt(Xs[i][i][0]) and mzt(Xs[i][i][1] - F2**2 * Cm) for i in range(8) if i != X4)
    ctrl_rp = not mzt(Xs[1][1][1])  # the lambda S^2 part of the pressure (T^x1_x1) is not zero
    # the total tensor T = T_kin - delta V at the solution
    Xt = [[(Xs[a][b][0] - (Vy0 if a == b else sp.zeros(16, 16)), Xs[a][b][1] - (Vy1 if a == b else sp.zeros(16, 16)))
           for b in range(8)] for a in range(8)]

    def dtot(v, mu):
        return d4c(v) if mu == X4 else cd_author(v, mu)

    ok_cons = True
    for nu in range(8):
        for j in (0, 1):
            Y = sp.zeros(16, 16)
            for mu in range(8):
                Y += (Xt[mu][nu][j] * geo.sqrtg).applyfunc(lambda v: dtot(v, mu)) / geo.sqrtg
                for l in range(8):
                    if geo.Gam[l][mu][nu] != 0:
                        Y -= geo.Gam[l][mu][nu] * Xt[mu][l][j]
            ok_cons = ok_cons and mzt(Y)
    # control: the kinetic part alone is not conserved at order lambda S0 (V depends on x4 through F)
    Yk = sp.zeros(16, 16)
    for mu in range(8):
        Yk += (Xs[mu][X4][1] * geo.sqrtg).applyfunc(lambda v: dtot(v, mu)) / geo.sqrtg
        for l in range(8):
            if geo.Gam[l][mu][X4] != 0:
                Yk -= geo.Gam[l][mu][X4] * Xs[mu][l][1]
    ctrl_cons = not mzt(Yk)
    # cross-check of the contraction against the direct evaluation in the explicit algebra (T_kin^x0_x0)
    Y0, Y1 = Xs[X0][X0]
    direct = m0(Tk[X0][X0]).subst(rule).expand()
    ok_lemma = (direct - contract(Y0) - (S0 * contract(Y1)).scale(lam)).expand().is_zero(zt)[0]
    ok = all((ok_sq, ok_c, ok_alg, ok_S, ok_E, ctrl_E, ok_pot, ok_rp, ctrl_rp, ok_cons, ctrl_cons, ok_lemma))
    detail = (f"Grassmann (dirac16complex, explicit algebra with N = 2 generators theta_k and their conjugates, 16 "
              "generic complex constants per generator), MASS m = 0, general a4 and b4, every real z: Psi = F sum_k "
              "[P chi_k + lambda S0 eta_k] theta_k, F = e^(a4/2) b4^(-1), P = cosh(I0) + sinh(I0) K, K = gamma^(x4) "
              "gamma^(x0), I0' = (3/2) H e^a4 b4^(-1/2), eta_k = -P gamma^(x4) (Ic + Is K) chi_k with Ic' = F^2 cosh(2 I0), "
              "Is' = F^2 sinh(2 I0), S0 = sum_kl thetabar_k theta_l chi_k^dagger C chi_l (the expansion terminates since "
              f"S0^2 Psi = 0): K^2 = I16, {{K, gamma^(x4)}} = 0, K^T C + C K = 0 [{ok_sq and ok_c}]; S0 real, S0^2 != 0, "
              f"S0^2 Psi = 0 [{ok_alg}]; S = Psibar Psi = F^2 S0 exactly [{ok_S}]; the 16 jet expressions E_A of the sympy "
              f"field equation (m = 0) vanish at Psi [{ok_E}] (control: without the lambda S0 eta_k term E_1 != 0 "
              f"[{ctrl_E}]); for the sympy energy-momentum tensor (T_pot = -delta V, V = m S + (lambda/2) S^2 [{ok_pot}]): "
              "-T^x4_x4 = (lambda/2) S^2 and T^mu_mu = (lambda/2) S^2 for mu != x4, S = F^2 S0 [" + str(ok_rp) +
              f"] (control: the lambda S^2 part of the pressure is nonzero [{ctrl_rp}]), nabla_mu T^mu_nu = 0 for all 8 "
              f"nu [{ok_cons}] (kinetic part evaluated as B[Y0] + lambda S0 B[Y1] with exact 16 x 16 matrices; control: "
              f"the kinetic part alone is not conserved at order lambda S0 [{ctrl_cons}]; this contraction equals the "
              f"direct explicit-algebra evaluation of T_kin^x0_x0 [{ok_lemma}]). Scope: m = 0; for m != 0 the linear "
              "system has no closed-form fundamental matrix for general a4, b4")
    return ok, detail
