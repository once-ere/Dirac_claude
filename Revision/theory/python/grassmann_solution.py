"""Revision theory (sympy side): the exact nonlinear homogeneous solution of dirac16complex (Grassmann field,
U = (lambda/2) S^2) in an EXPLICIT Grassmann algebra with N = 2 generators theta_1, theta_2 and their conjugates
thetabar_1, thetabar_2, verified exactly (written anew; no code shared with the Wolfram side).

    Psi = sum_k [P(m) + lambda S0 dP/dm] chi_k theta_k,   P(m) = cosh(k x4) I + (sinh(k x4)/k) M_m,
    M_m = -m gamma^(x4) + 3 H gamma^(x4) gamma^(x8),   k^2 = 9 H^2 - m^2,
    S0 = sum_kl thetabar_k theta_l chi_k^dagger C chi_l   (even, nilpotent: S0^2 != 0, S0^2 Psi = 0),

with 16 generic complex constants per generator (chi_k components q_Bk; their conjugates qc_Bk).  It is the
expansion of exp(M_(m + lambda S0) x4) chi, which terminates because S0^2 Psi = 0.

Verified here:
  * S = Psibar Psi = S0 exactly (in the explicit algebra), S0 real, S0^2 != 0, S0^2 Psi = 0;
  * the field equation: the sympy jet expressions E_A = (gamma^mu D_mu Psi - (m + lambda S) Psi)_A of
    fields.Spinors (Grassmann, lambda general), evaluated at the solution in the explicit algebra, vanish for all
    16 A; control: without the correction lambda S0 dP/dm the equation fails;
  * the energy-momentum tensor of fields.Spinors.emt() at the solution: -T^x4_x4 = m S0 + (lambda/2) S0^2,
    T^mu_mu = (lambda/2) S0^2 for mu != x4, and nabla_mu T^mu_nu = 0 for all eight nu.  The kinetic part T_kin is
    a bilinear sum_AB N_AB chi_(A,d1) psi_(B,d2); at the solution Psi^(d) = U_d chi with real matrices
    U_d = U_d0 + sigma U_d1 (sigma = lambda S0 even, sigma^2 times any bilinear vanishes: degree 6 > 4), so
    T_kin = B[X0] + lambda S0 B[X1] with B[X] = sum_kl thetabar_k theta_l chi_k^dagger X chi_l and the 16 x 16
    matrices X0 = sum U_d1,0^T N U_d2,0, X1 = sum (U_d1,1^T N U_d2,0 + U_d1,0^T N U_d2,1); the statements follow from
    exact matrix identities (sufficient conditions), and this contraction is cross-checked against the direct
    evaluation in the explicit algebra for T_kin^x8_x8.  The potential part is -delta V, V = m S + (lambda/2) S^2,
    constant at the solution.

Coefficients: x4, Ch = cosh(k x4), Sh = sinh(k x4), k with d/dx4: Ch -> k Sh, Sh -> k Ch; the exact zero test
reduces Ch^2 -> 1 + Sh^2, k^2 -> 9 H^2 - m^2 and c^2 -> 1 - s^12 (author's ring) in the numerator."""

import sympy as sp

from superalg import Alg, gen, CHI, PSI
from geometry import X4, H, m, lam, s, c, cd_author, zero_author

NG = 2
GEN0 = 100  # generator keys (PSI, 100 + k) = theta_k, (CHI, 100 + k) = thetabar_k (conjugation maps PSI <-> CHI)
x4s, kk, Ch, Sh = sp.symbols("x4 k Ch Sh", real=True)
K2 = 9 * H**2 - m**2


def _theta(k):
    return Alg.g("grassmann", gen(PSI, GEN0 + k))


def _thetabar(k):
    return Alg.g("grassmann", gen(CHI, GEN0 + k))


def d4c(v):
    """d/dx4 of an explicit coefficient (x4, cosh(k x4), sinh(k x4))."""
    return sp.diff(v, x4s) + sp.diff(v, Ch) * kk * Sh + sp.diff(v, Sh) * kk * Ch


def reduce_form(v):
    """Normal form of the numerator: Ch^2 -> 1 + Sh^2, k^2 -> 9 H^2 - m^2, c^2 -> 1 - s^12 (unique representation
    with Ch, k, c of degree <= 1), so the expression is zero iff the result is 0."""
    v = sp.sympify(v)
    if v == 0:
        return sp.Integer(0)
    num, _ = sp.fraction(sp.together(v))
    num = sp.expand(num)
    if num == 0:
        return num
    out = 0
    for (a, b, e), cf in sp.Poly(num, Ch, kk, c).terms():
        out += cf * Ch**(a % 2) * (1 + Sh**2)**(a // 2) * kk**(b % 2) * K2**(b // 2) * c**(e % 2) * (1 - s**12)**(e // 2)
    return sp.expand(out)


def zt(v):
    return reduce_form(v) == 0


def verify(gm, geo, sps, Tk, Tp, V):
    """sps: fields.Spinors('grassmann', geo, ..., m, lam); Tk, Tp, V from sps.emt().  Returns (ok, detail)."""
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

    Mm = -m * G[3] + 3 * H * G[3] * G[7]
    ok_sq = (Mm * Mm - K2 * I16).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_c = (Mm.T * Cm + Cm * Mm).applyfunc(sp.expand) == sp.zeros(16, 16)
    P = Ch * I16 + (Sh / kk) * Mm
    kp = -m / kk  # dk/dm
    dP = kp * x4s * Sh * I16 + kp * (x4s * Ch / kk - Sh / kk**2) * Mm - (Sh / kk) * G[3]  # d P / d m
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
        Pc = [P * chi[k] for k in range(NG)]
        dPc = [dP * chi[k] for k in range(NG)]
        out = []
        for A in range(16):
            e = Alg("grassmann")
            for k in range(NG):
                e = e + _theta(k).scale(sp.expand(Pc[k][A]))
                if with_correction:
                    e = e + (S0 * _theta(k)).scale(sp.expand(lam * dPc[k][A]))
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
    ok_S = (Sx - S0).expand().is_zero(zt)[0]

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
            return Alg("grassmann")  # homogeneous: no dependence on x1..x3, x5..x8
        return rule

    Ev = sps.dirac_E()
    rule = rule_for(Psi)
    ok_E = all(Ev[A].subst(rule).expand().is_zero(zt)[0] for A in range(16))
    rule_bad = rule_for(solution(False))
    ctrl_E = not Ev[0].subst(rule_bad).expand().is_zero(zt)[0]
    # energy-momentum tensor at the solution through the contraction B[.]
    U = {(): (P, dP), (X4,): (P.applyfunc(d4c), dP.applyfunc(d4c))}

    def at_solution(x):
        X0, X1 = sp.zeros(16, 16), sp.zeros(16, 16)
        for mono, v in x.t.items():
            if len(mono) != 2 or mono[0][0] != CHI or mono[1][0] != PSI:
                raise ValueError(f"T_kin is not a Psibar-Psi bilinear: {mono}")
            (_, A, d1), (_, B, d2) = mono
            if d1 not in U or d2 not in U:
                continue  # derivatives other than d4 vanish at a homogeneous solution
            a0, a1 = U[d1]
            b0, b1 = U[d2]
            N = sp.zeros(16, 16)
            N[A, B] = v
            X0 += a0.T * N * b0
            X1 += a1.T * N * b0 + a0.T * N * b1
        return X0.applyfunc(sp.expand), X1.applyfunc(sp.expand)

    def mzt(M):
        return all(zt(e) for e in M)

    ok_pot = all((Tp[a][b] + (V if a == b else Alg("grassmann"))).expand().is_zero(zero_author)[0]
                 for a in range(8) for b in range(8))
    ok_pot = ok_pot and (V - S0.scale(0)).t is not None  # V is the jet m S + (lambda/2) S^2 (fields.Spinors)
    Xs = [[at_solution(Tk[a][b]) for b in range(8)] for a in range(8)]
    # -T^x4_x4 = -T_kin^x4_x4 + V and T^i_i = T_kin^i_i - V, V(solution) = m S0 + (lambda/2) S0^2:
    # -T_kin^x4_x4 = 0 and T_kin^i_i = m S0 + lambda S0^2 = B[m C] + lambda S0 B[C]
    ok_rp = mzt(Xs[X4][X4][0]) and mzt(Xs[X4][X4][1])
    ok_rp = ok_rp and all(mzt(Xs[i][i][0] - m * Cm) and mzt(Xs[i][i][1] - Cm) for i in range(8) if i != X4)
    ctrl_rp = not mzt(Xs[0][0][1])  # the lambda S0^2 part of the pressure is not zero

    def dtot(v, mu):
        return cd_author(v, mu) + (d4c(v) if mu == X4 else 0)

    ok_cons = True
    for nu in range(8):
        for j in (0, 1):
            Y = sp.zeros(16, 16)
            for mu in range(8):
                Y += (Xs[mu][nu][j] * geo.sqrtg).applyfunc(lambda v: dtot(v, mu)) / geo.sqrtg
                for l in range(8):
                    if geo.Gam[l][mu][nu] != 0:
                        Y -= geo.Gam[l][mu][nu] * Xs[mu][l][j]
            ok_cons = ok_cons and mzt(Y)
    # the potential part -delta V (V constant at the solution) contributes d_nu V + V (d_nu ln sqrt g - Gamma^mu_mu nu) = 0
    ok_cons = ok_cons and all(zero_author(cd_author(geo.sqrtg, nu) / geo.sqrtg - sum(geo.Gam[mu][mu][nu] for mu in range(8)))
                              for nu in range(8))
    # cross-check of the contraction against the direct evaluation in the explicit algebra (T_kin^x8_x8)
    X0, X1 = Xs[7][7]
    direct = Tk[7][7].subst(rule).expand()
    ok_lemma = (direct - contract(X0) - (S0 * contract(X1)).scale(lam)).expand().is_zero(zt)[0]
    ok = all((ok_sq, ok_c, ok_alg, ok_S, ok_E, ctrl_E, ok_pot, ok_rp, ctrl_rp, ok_cons, ok_lemma))
    detail = (f"Grassmann (dirac16complex, explicit algebra with N = 2 generators theta_k and their conjugates, 16 "
              "generic complex constants per generator): Psi = sum_k [P(m) + lambda S0 dP/dm] chi_k theta_k, P(m) = "
              "cosh(k x4) + sinh(k x4)/k M_m, M_m = -m gamma^(x4) + 3 H gamma^(x4) gamma^(x8), k^2 = 9 H^2 - m^2, "
              "S0 = sum_kl thetabar_k theta_l chi_k^dagger C chi_l (the expansion of exp(M_(m + lambda S0) x4) chi, "
              "which terminates since S0^2 Psi = 0): "
              f"M_m^2 = k^2 I16 and M^T C + C M = 0 [{ok_sq and ok_c}]; S0 real, S0^2 != 0, S0^2 Psi = 0 [{ok_alg}]; "
              f"S = Psibar Psi = S0 exactly [{ok_S}]; the 16 jet expressions E_A of the sympy field equation vanish at "
              f"Psi [{ok_E}] (control: without the lambda S0 dP/dm term E_1 != 0 [{ctrl_E}]); for the sympy "
              "energy-momentum tensor (T_pot = -delta V, V = m S + (lambda/2) S^2 [" + str(ok_pot) + "]): -T^x4_x4 = "
              "m S0 + (lambda/2) S0^2 and T^mu_mu = (lambda/2) S0^2 for mu != x4 [" + str(ok_rp) + "] (control: the "
              f"lambda S0^2 part of the pressure is nonzero [{ctrl_rp}]), nabla_mu T^mu_nu = 0 for all 8 nu "
              f"[{ok_cons}] (kinetic part evaluated as B[X0] + lambda S0 B[X1] with exact 16 x 16 matrices; this "
              f"contraction equals the direct explicit-algebra evaluation of T_kin^x8_x8 [{ok_lemma}]); the values are "
              "Grassmann-algebra elements (the classical Grassmann EMT; numbers come from the expectation values of "
              "the quantum theory)")
    return ok, detail
