"""Revision theory (sympy side): the exact nonlinear homogeneous solution of dirac16complex (Grassmann field,
U = (lambda/2) S^2) in the author's metric with b4(x4) (general a4 and b4 > 0), in an EXPLICIT Grassmann algebra with
N = 2 generators theta_1, theta_2 and their conjugates thetabar_1, thetabar_2, verified exactly (written anew; no code
shared with the Wolfram side).

    Psi = b4^(-3/4) sum_k [P chi_k + lambda S0 eta_k] theta_k,   P = cosh(k x4) I + (sinh(k x4)/k) M,
    M = -m gamma^(x4) + 3 H gamma^(x4) gamma^(x0),   k^2 = 9 H^2 - m^2,
    eta_k = -P (A0 I0 + Ac Ic + As Is) chi_k,   A0 = (gamma^(x4) + M gamma^(x4) M/k^2)/2,
    Ac = (gamma^(x4) - M gamma^(x4) M/k^2)/2,   As = [gamma^(x4), M]/(2 k),
    I0 = int_0^x4 b4^(-3/2) ds,  Ic = int_0^x4 b4^(-3/2) cosh(2 k s) ds,  Is = int_0^x4 b4^(-3/2) sinh(2 k s) ds,
    S0 = sum_kl thetabar_k theta_l chi_k^dagger C chi_l   (even, nilpotent: S0^2 != 0, S0^2 Psi = 0),

with 16 generic complex constants per generator (chi_k components q_Bk; their conjugates qc_Bk).  chi = b4^(3/4) Psi
solves the b4-free homogeneous equation with the effective coupling lambda b4^(-3/2); its degree-1 part is P chi_k,
and eta_k is the variation-of-constants solution of eta_k' = M eta_k - b4^(-3/2) gamma^(x4) P chi_k, eta_k(0) = 0
(P^-1 gamma^(x4) P = A0 + Ac cosh(2 k x4) + As sinh(2 k x4)).  The expansion terminates because S0^2 Psi = 0.
(Until 2026-10-15 this module verified the solution of the withdrawn metric b4 = 1, Psi = sum_k [P + lambda S0 dP/dm]
chi_k theta_k, which is the case b4 = 1 of the present one.)

Verified here:
  * S = Psibar Psi = b4^(-3/2) S0 exactly (in the explicit algebra), S0 real, S0^2 != 0, S0^2 Psi = 0;
  * the field equation: the sympy jet expressions E_A = (gamma^mu D_mu Psi - (m + lambda S) Psi)_A of
    fields.Spinors (Grassmann, lambda general), evaluated at the solution in the explicit algebra, vanish for all
    16 A; control: without the correction lambda S0 eta_k the equation fails;
  * the energy-momentum tensor of fields.Spinors.emt() at the solution: -T^x4_x4 = m S + (lambda/2) S^2,
    T^mu_mu = (lambda/2) S^2 for mu != x4 (S = b4^(-3/2) S0), and nabla_mu T^mu_nu = 0 for all eight nu.  The kinetic
    part T_kin is a bilinear sum_AB N_AB chi_(A,d1) psi_(B,d2); at the solution Psi^(d) = U_d chi with real matrices
    U_d = U_d0 + sigma U_d1 (sigma = lambda S0 even, sigma^2 times any bilinear vanishes: degree 6 > 4), so
    T_kin = B[Y0] + lambda S0 B[Y1] with B[Y] = sum_kl thetabar_k theta_l chi_k^dagger Y chi_l and the 16 x 16
    matrices Y0 = sum U_d1,0^T N U_d2,0, Y1 = sum (U_d1,1^T N U_d2,0 + U_d1,0^T N U_d2,1); the potential part is
    -delta V with V = m S + (lambda/2) S^2 = B[m b4^(-3/2) C] + lambda S0 B[(1/2) b4^(-3) C] at the solution (it
    depends on x4 through b4, so the divergence is taken of the total tensor); the statements follow from exact
    matrix identities (sufficient conditions), and this contraction is cross-checked against the direct evaluation
    in the explicit algebra for T_kin^x0_x0 (x0 = the hidden direction).

Coefficients: Ch = cosh(k x4), Sh = sinh(k x4), k, the integrals I0, Ic, Is and the metric ring of geometry.py
(Q = b4^(1/2), B1 = b4'/b4, ...), with d/dx4: Ch -> k Sh, Sh -> k Ch, I0 -> Q^-3, Ic -> Q^-3 (Ch^2 + Sh^2),
Is -> 2 Q^-3 Sh Ch, and the ring derivative cd_author; the exact zero test reduces Ch^2 -> 1 + Sh^2,
k^2 -> 9 H^2 - m^2 and c^2 -> 1 - s^12 (author's ring) in the numerator."""

import sympy as sp

from superalg import Alg, gen, CHI, PSI
from geometry import X0, X4, H, m, lam, s, c, Q, cd_author, zero_author

NG = 2
GEN0 = 100  # generator keys (PSI, 100 + k) = theta_k, (CHI, 100 + k) = thetabar_k (conjugation maps PSI <-> CHI)
kk, Ch, Sh = sp.symbols("k Ch Sh", real=True)
I0, Ic, Is = sp.symbols("I0 Ic Is", real=True)
K2 = 9 * H**2 - m**2
INTEGRAND = {I0: Q**-3, Ic: Q**-3 * (Ch**2 + Sh**2), Is: 2 * Q**-3 * Sh * Ch}


def _theta(k):
    return Alg.g("grassmann", gen(PSI, GEN0 + k))


def _thetabar(k):
    return Alg.g("grassmann", gen(CHI, GEN0 + k))


def d4c(v):
    """d/dx4 of an explicit coefficient (cosh(k x4), sinh(k x4), the integrals I0, Ic, Is and the metric ring)."""
    r = sp.diff(v, Ch) * kk * Sh + sp.diff(v, Sh) * kk * Ch + cd_author(v, X4)
    for sym, val in INTEGRAND.items():
        r += sp.diff(v, sym) * val
    return r


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

    Mm = -m * G[X4] + 3 * H * G[X4] * G[X0]
    ok_sq = (Mm * Mm - K2 * I16).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_c = (Mm.T * Cm + Cm * Mm).applyfunc(sp.expand) == sp.zeros(16, 16)
    P = Ch * I16 + (Sh / kk) * Mm
    A0 = (G[X4] + Mm * G[X4] * Mm / kk**2) / 2
    Ac = (G[X4] - Mm * G[X4] * Mm / kk**2) / 2
    As = (G[X4] * Mm - Mm * G[X4]) / (2 * kk)
    W = -P * (A0 * I0 + Ac * Ic + As * Is)
    bq = Q ** sp.Rational(-3, 2)  # b4^(-3/4)
    U0, U1 = (bq * P).applyfunc(sp.expand), (bq * W).applyfunc(sp.expand)
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
    ok_S = (Sx - S0.scale(Q**-3)).expand().is_zero(zt)[0]

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

    Ev = sps.dirac_E()
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
            N[A, B] = v
            Y0 += a0.T * N * b0
            Y1 += a1.T * N * b0 + a0.T * N * b1
        return Y0.applyfunc(sp.expand), Y1.applyfunc(sp.expand)

    def mzt(M):
        return all(zt(e) for e in M)

    # T_pot = -delta V with the jet V = m S + (lambda/2) S^2; at the solution S = b4^(-3/2) S0, so
    # V = B[m b4^(-3/2) C] + lambda S0 B[(1/2) b4^(-3) C] (it depends on x4 through b4)
    Sj = sps.S()
    ok_pot = all((Tp[a][b] + (V if a == b else Alg("grassmann"))).expand().is_zero(zero_author)[0]
                 for a in range(8) for b in range(8))
    ok_pot = ok_pot and (V - Sj.scale(m) - (Sj * Sj).scale(lam / 2)).expand().is_zero(zero_author)[0]
    Vy0, Vy1 = m * Q**-3 * Cm, Q**-6 * Cm / 2
    Xs = [[at_solution(Tk[a][b]) for b in range(8)] for a in range(8)]
    # -T^x4_x4 = -T_kin^x4_x4 + V and T^i_i = T_kin^i_i - V: -T_kin^x4_x4 = 0 and T_kin^i_i = (m + lambda S) S
    # = B[m b4^(-3/2) C] + lambda S0 B[b4^(-3) C]
    ok_rp = mzt(Xs[X4][X4][0]) and mzt(Xs[X4][X4][1])
    ok_rp = ok_rp and all(mzt(Xs[i][i][0] - m * Q**-3 * Cm) and mzt(Xs[i][i][1] - Q**-6 * Cm) for i in range(8) if i != X4)
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
    # control: the kinetic part alone is not conserved (V depends on x4 through b4)
    Yk = sp.zeros(16, 16)
    for mu in range(8):
        Yk += (Xs[mu][X4][0] * geo.sqrtg).applyfunc(lambda v: dtot(v, mu)) / geo.sqrtg
        for l in range(8):
            if geo.Gam[l][mu][X4] != 0:
                Yk -= geo.Gam[l][mu][X4] * Xs[mu][l][0]
    ctrl_cons = not mzt(Yk)
    # cross-check of the contraction against the direct evaluation in the explicit algebra (T_kin^x0_x0)
    Y0, Y1 = Xs[X0][X0]
    direct = Tk[X0][X0].subst(rule).expand()
    ok_lemma = (direct - contract(Y0) - (S0 * contract(Y1)).scale(lam)).expand().is_zero(zt)[0]
    ok = all((ok_sq, ok_c, ok_alg, ok_S, ok_E, ctrl_E, ok_pot, ok_rp, ctrl_rp, ok_cons, ctrl_cons, ok_lemma))
    detail = (f"Grassmann (dirac16complex, explicit algebra with N = 2 generators theta_k and their conjugates, 16 "
              "generic complex constants per generator), general a4 and b4: Psi = b4^(-3/4) sum_k [P chi_k + lambda S0 "
              "eta_k] theta_k, P = cosh(k x4) + sinh(k x4)/k M, M = -m gamma^(x4) + 3 H gamma^(x4) gamma^(x0), k^2 = "
              "9 H^2 - m^2, eta_k = -P (A0 I0 + Ac Ic + As Is) chi_k (A0 = (gamma^(x4) + M gamma^(x4) M/k^2)/2, Ac = "
              "(gamma^(x4) - M gamma^(x4) M/k^2)/2, As = [gamma^(x4), M]/(2 k); I0, Ic, Is = int_0^x4 b4^(-3/2) {1, "
              "cosh 2ks, sinh 2ks} ds), S0 = sum_kl thetabar_k theta_l chi_k^dagger C chi_l (the expansion terminates "
              f"since S0^2 Psi = 0): M^2 = k^2 I16 and M^T C + C M = 0 [{ok_sq and ok_c}]; S0 real, S0^2 != 0, S0^2 Psi "
              f"= 0 [{ok_alg}]; S = Psibar Psi = b4^(-3/2) S0 exactly [{ok_S}]; the 16 jet expressions E_A of the sympy "
              f"field equation vanish at Psi [{ok_E}] (control: without the lambda S0 eta_k term E_1 != 0 [{ctrl_E}]); "
              "for the sympy energy-momentum tensor (T_pot = -delta V, V = m S + (lambda/2) S^2 [" + str(ok_pot) + "]): "
              "-T^x4_x4 = m S + (lambda/2) S^2 and T^mu_mu = (lambda/2) S^2 for mu != x4, S = b4^(-3/2) S0 ["
              + str(ok_rp) + f"] (control: the lambda S^2 part of the pressure is nonzero [{ctrl_rp}]), nabla_mu T^mu_nu "
              f"= 0 for all 8 nu [{ok_cons}] (kinetic part evaluated as B[Y0] + lambda S0 B[Y1] with exact 16 x 16 "
              f"matrices; control: the kinetic part alone is not conserved, V depends on x4 [{ctrl_cons}]; this "
              f"contraction equals the direct explicit-algebra evaluation of T_kin^x0_x0 [{ok_lemma}]); the values are "
              "Grassmann-algebra elements (the classical Grassmann EMT; numbers come from the expectation values of "
              "the quantum theory)")
    return ok, detail
