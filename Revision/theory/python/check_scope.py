#!/usr/bin/env python3
"""Revision/theory/python/check_scope.py - exact sympy checks of the SCOPE of the statements of the field-theory
record (Revision/SPEC.md sections 1-6) for the CORRECTED primordial metric of 2026-10-16 (version 2;
Revision/metric_warped/):
    g = diag(e^(-2 a4) b4 cot^2 z, e^(2 a4) (x3), -1, -e^(-2 a4) b4 (sin^2 z)^(1/6) (x3)),  z = 6 H x0 REAL,
general a4(x4) and b4(x4) > 0 and EVERY real z (the user's rules of 2026-10-16: -infinity < z < infinity,
sin^(1/3) z = (sin^2 z)^(1/6), the positive branch): what depends on the choice of frame and field variables, what
holds only up to boundary terms, and what the indefinite structures imply.  (Until 2026-10-16 this checker treated the
metric of 2026-10-14 on 0 < z < pi/2, withdrawn.)  Written anew for Revision (no code shared with
Revision/theory/wolfram/verify_scope.wls, nothing from the old stages).  Writes Revision/theory/reports/python-scope.json
(deterministic, LF).

Usage:  python Revision/theory/python/check_scope.py [--out PATH]

Coordinates as the author names them, in the author's order x0..x7 (arrays index them 0..7, index k = xk): x0 = the hidden,
space-like direction; x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the three extra times, which DEFLATE (scale factor
e^{-a4} b4^{1/2} (sin^2 z)^(1/12); the hidden direction shares the factor e^{-a4} b4^{1/2}).

Coefficient ring (exact, every real z): Ea = e^{a4(x4)}, A1, A2, A3, A4 = a4', ..., a4''''; Q = b4(x4)^(1/2), B1, B2, B3,
B4 = (ln b4)', ..., (ln b4)'''' (b4'/b4 = B1, b4''/b4 = B2 + B1^2); sv = sin z, c = cos z (signed); w = (sin^2 z)^(1/12)
> 0; sgn = sign(cot z) = +-1 (sqrt|g| = sgn f0...f7, constant between the degenerate points z = n pi/2); ch = cosh b,
sh = sinh b for a frame boost of rapidity b(x4) in the (x4, x0) plane.  Derivatives: d4 Ea = Ea A1, d4 A_k = A_(k+1),
d4 Q = Q B1/2, d4 B_k = B_(k+1), d4 ch = rate sh, d4 sh = rate ch (rate = b'); d0 sv = 6 H c, d0 c = -6 H sv,
d0 w = H (c/sv) w.  Zero test: numerator reduced modulo c^2 + sv^2 - 1, w^12 - sv^2, sgn^2 - 1 and ch^2 - 1 - sh^2
(the leading terms are coprime, so the successive remainders are canonical).
"""

import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
REV = os.path.normpath(os.path.join(HERE, "..", ".."))
GAMMAS = os.path.join(REV, "algebra", "gammas.json")
OUT = os.path.join(REV, "theory", "reports", "python-scope.json")
X0, X4 = 0, 4
ETA = [1, 1, 1, 1, -1, -1, -1, -1]
N = 16
T0 = time.time()
CHECKS = []

Ea, w, ch, sh, Q = sp.symbols("Ea w ch sh Q", positive=True)
sv, c, sgn = sp.symbols("sv c sgn", real=True)
A1, A2, A3, A4 = sp.symbols("A1 A2 A3 A4", real=True)
B1, B2, B3, B4 = sp.symbols("B1 B2 B3 B4", real=True)
H = sp.Symbol("H", positive=True)
beta = sp.Symbol("beta", real=True)
m, lam = sp.symbols("m lambda", real=True)
CG = sp.Rational(3, 2) * H * Ea / Q          # gamma^(x0) coefficient of gamma^mu Omega_mu (diagonal frame)
VG = B1 - A1 / 2                             # its gamma^(x4) coefficient


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(f"[{time.time() - T0:7.1f}s] {'PASS' if ok else 'FAIL'} {name}", flush=True)


# ------------------------------------------------------------------ gammas (fixture of Revision/algebra)
def _mat(rows):
    if isinstance(rows, dict):
        return _mat(rows["re"]) + sp.I * _mat(rows["im"])
    return sp.Matrix([[sp.Rational(x) if isinstance(x, str) else sp.Integer(x) for x in r] for r in rows])


with open(GAMMAS, encoding="utf-8") as fh:
    _gj = json.load(fh)
G = [_mat(g) for g in _gj["gamma"]]
C = _mat(_gj["C"])
B = _mat(_gj["B"])
I16, Z16 = sp.eye(N), sp.zeros(N, N)
SAB = [[(G[a] * G[b] - G[b] * G[a]) / 4 for b in range(8)] for a in range(8)]


# ------------------------------------------------------------------ the coefficient ring
def cd(expr, mu, rate=beta):
    expr = sp.sympify(expr)
    if mu == X4:
        r = sp.diff(expr, Ea) * Ea * A1 + sp.diff(expr, A1) * A2 + sp.diff(expr, A2) * A3 + sp.diff(expr, A3) * A4
        r += sp.diff(expr, Q) * Q * B1 / 2 + sp.diff(expr, B1) * B2 + sp.diff(expr, B2) * B3 + sp.diff(expr, B3) * B4
        return r + sp.diff(expr, ch) * rate * sh + sp.diff(expr, sh) * rate * ch
    if mu == X0:
        return sp.diff(expr, sv) * 6 * H * c + sp.diff(expr, c) * (-6 * H * sv) + sp.diff(expr, w) * H * c * w / sv
    return sp.Integer(0)


def _rem(num, var, rel):
    if num.has(var):
        num = sp.expand(sp.rem(sp.Poly(num, var), sp.Poly(rel, var)).as_expr())
    return num


def reduce_poly(num):
    num = sp.expand(num)
    num = _rem(num, c, c**2 - 1 + sv**2)
    num = _rem(num, w, w**12 - sv**2)
    num = _rem(num, sgn, sgn**2 - 1)
    num = _rem(num, ch, ch**2 - 1 - sh**2)
    return num


def is0(expr):
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    num, _ = sp.fraction(sp.together(expr))
    return reduce_poly(num) == 0


def canon(expr):
    num, den = sp.fraction(sp.together(sp.sympify(expr)))
    return sp.factor(reduce_poly(num)) / sp.factor(den)


def mzero(M):
    return all(is0(x) for x in M)


# ------------------------------------------------------------------ a general vielbein e^a_mu (rows a, columns mu)
# e^a_mu = f_a delta^a_mu: f0 = e^-a4 b4^(1/2) cot z (signed), f_i = e^a4, f4 = 1, f_t = e^-a4 b4^(1/2) (sin^2 z)^(1/12)
DIAG = [Q * c / (Ea * sv), Ea, Ea, Ea, sp.Integer(1), Q * w / Ea, Q * w / Ea, Q * w / Ea]


def boost(chv, shv):
    """Lorentz boost of the frame in the (x4, x0) plane: e'^(4) = ch e^(4) + sh e^(0), e'^(0) = sh e^(4) + ch e^(0)."""
    L = sp.eye(8)
    L[X4, X4], L[X4, X0], L[X0, X4], L[X0, X0] = chv, shv, shv, chv
    return L


class Frame:
    def __init__(self, L, Linv, rate):
        self.rate = rate
        ed = sp.diag(*DIAG)
        self.e = L * ed                                          # e^a_mu
        self.E = sp.diag(*[1 / x for x in DIAG]) * Linv          # E[mu, a] = e_a^mu
        self.g = [[sp.expand(sum(ETA[a] * self.e[a, mu] * self.e[a, nu] for a in range(8))) for nu in range(8)]
                  for mu in range(8)]
        gd = [ETA[a] * DIAG[a] ** 2 for a in range(8)]          # the corrected metric (diagonal)
        self.gdiag = gd
        gi = [1 / x for x in gd]
        dg = [[cd(gd[l], mu, rate) for mu in range(8)] for l in range(8)]
        Gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
        for l in range(8):
            for a in range(8):
                for b in range(8):
                    v = 0
                    if l == b:
                        v += dg[l][a]
                    if l == a:
                        v += dg[l][b]
                    if a == b:
                        v -= dg[a][l]
                    if v != 0:
                        Gam[l][a][b] = sp.expand(gi[l] * v / 2)
        self.Gam = Gam
        # canonical spin connection omega_mu^a_b = e^a_nu (d_mu E_b^nu + Gam^nu_{mu lam} E_b^lam)
        om = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
        for mu in range(8):
            for a in range(8):
                for b in range(8):
                    v = 0
                    for nu in range(8):
                        if self.e[a, nu] == 0:
                            continue
                        t = cd(self.E[nu, b], mu, rate)
                        for l_ in range(8):
                            if Gam[nu][mu][l_] != 0 and self.E[l_, b] != 0:
                                t += Gam[nu][mu][l_] * self.E[l_, b]
                        v += self.e[a, nu] * t
                    om[mu][a][b] = canon(v) if v != 0 else sp.Integer(0)
        self.om_mixed = om
        self.om = [[[sp.expand(ETA[a] * om[mu][a][b]) for b in range(8)] for a in range(8)] for mu in range(8)]
        self.Om = []
        for mu in range(8):
            M = sp.zeros(N, N)
            for a in range(8):
                for b in range(a + 1, 8):
                    if not is0(self.om[mu][a][b]):
                        M += self.om[mu][a][b] * SAB[a][b]
            self.Om.append(M)
        self.gam = [sum((self.E[mu, a] * G[a] for a in range(8)), sp.zeros(N, N)) for mu in range(8)]

    def postulate_ok(self):
        bad = 0
        for a in range(8):
            for mu in range(8):
                for nu in range(8):
                    v = cd(self.e[a, nu], mu, self.rate) - sum(self.Gam[l_][mu][nu] * self.e[a, l_] for l_ in range(8)) \
                        + sum(self.om_mixed[mu][a][b] * self.e[b, nu] for b in range(8))
                    if not is0(v):
                        bad += 1
        return bad

    def antisym_ok(self):
        return all(is0(self.om[mu][a][b] + self.om[mu][b][a]) for mu in range(8) for a in range(8) for b in range(8))

    def gamma_Omega(self):
        tot = sp.zeros(N, N)
        for mu in range(8):
            tot += self.gam[mu] * self.Om[mu]
        return tot.applyfunc(canon)


def main():
    out = OUT
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]

    zt = [is0(c**2 + sv**2 - 1), not is0(w**6 - sv), not is0(w**6 + sv), is0(w**12 - sv**2), is0(sgn**2 - 1),
          not is0(sgn - 1), is0(cd(w**12 - sv**2, X0)), is0(ch**2 - sh**2 - 1)]
    check("zero_test_controls", all(zt),
          "the exact zero test of this checker (every real z): c^2 + sv^2 - 1, w^12 - sv^2, sgn^2 - 1 and ch^2 - sh^2 - 1 are "
          "zero; w^6 - sv and w^6 + sv (|sin z| -+ sin z) and sgn - 1 are not (no sign of sin z is assumed); the x0 "
          "derivatives of the ring respect w^12 = sv^2")

    # ================================================================ 1. frame dependence of gamma^mu Omega_mu
    fb = Frame(boost(ch, sh), boost(ch, -sh), beta)              # rapidity b = beta x4 + b0
    metric_ok = all(is0(fb.g[mu][nu] - (fb.gdiag[mu] if mu == nu else 0)) for mu in range(8) for nu in range(8))
    check("boosted_frame_reproduces_metric", metric_ok and mzero(fb.e * fb.E - sp.eye(8)),
          "the frame boosted in the (x4, x0) plane, e'^(x4) = cosh b e^(x4) + sinh b e^(x0), e'^(x0) = sinh b e^(x4) + "
          "cosh b e^(x0) (other e'^(a) = e^(a), b = b(x4) = beta x4 + b0), with e^(a) the diagonal vielbein "
          "(f = (e^-a4 b4^(1/2) cot z, e^a4 [x3], 1, e^-a4 b4^(1/2) (sin^2 z)^(1/12) [x3]), order x0..x7): "
          "eta_ab e'^a_mu e'^b_nu equals the corrected metric for all 64 (mu, nu) and every real z, and e' E' = 1")
    nbad = fb.postulate_ok()
    check("boosted_frame_canonical_connection", nbad == 0 and fb.antisym_ok(),
          "canonical spin connection of the boosted frame, omega_mu^a_b = e'^a_nu (d_mu e'_b^nu + Gamma^nu_mu,lam "
          f"e'_b^lam): the vielbein postulate holds for all 512 (a, mu, nu) ({nbad} failures) and omega_mu ab = "
          "eta_ac omega_mu^c_b is antisymmetric in a, b for every mu (exact, symbolic a4, b4, H, beta, every real z)")
    tot_b = fb.gamma_Omega()
    want = (CG - beta / 2) * (ch * G[X0] - sh * G[X4]) + VG * (ch * G[X4] - sh * G[X0])
    cf0 = sp.expand((tot_b * G[X0]).trace() / 16)
    cf4 = sp.expand(-(tot_b * G[X4]).trace() / 16)
    check("boosted_frame_gammaOmega_formula", mzero(tot_b - want) and is0(ch * cf4 + sh * cf0 - VG),
          "in the boosted frame gamma'^mu Omega'_mu = (cg - beta/2) (cosh b gamma^(x0) - sinh b gamma^(x4)) + vg "
          "(cosh b gamma^(x4) - sinh b gamma^(x0)), cg = (3/2) H e^a4 b4^(-1/2), vg = b4'/b4 - a4'/2, exactly for every "
          "a4(x4), b4(x4), H > 0, rapidity rate beta and every real z; at b = 0 this is the value cg gamma^(x0) + vg "
          "gamma^(x4) of the diagonal frame. Its coefficients satisfy cosh b c4 + sinh b c0 = vg for every beta, so no "
          "such boost makes gamma'^mu Omega'_mu vanish unless b4'/b4 = a4'/2")
    rate_z = 2 * CG                                              # b' = 2 cg = 3 H e^a4 b4^(-1/2)
    fz = Frame(boost(ch, sh), boost(ch, -sh), rate_z)
    tot_z = fz.gamma_Omega()
    nz_z = [mu for mu in range(8) if not mzero(fz.Om[mu])]
    check("boosted_frame_removes_only_the_H_term",
          mzero(tot_z - VG * (ch * G[X4] - sh * G[X0])) and not mzero(tot_z) and nz_z != [] and fz.postulate_ok() == 0,
          "with a rapidity b(x4) of rate b' = 2 cg = 3 H e^a4 b4^(-1/2) the term gamma'^mu D'_mu - gamma'^mu d_mu = "
          "gamma'^mu Omega'_mu is vg (cosh b gamma^(x4) - sinh b gamma^(x0)) for every H > 0, a4(x4), b4(x4) (exact): "
          "its cg part belongs to the diagonal vielbein and is not a frame-independent part of the field equation, "
          "while the vg part is not removed by any boost in this plane (previous check). Omega'_mu itself is nonzero "
          "for mu = " + ", ".join(f"x{mu}" for mu in nz_z) + ", as it must be where the metric is curved (next check)")
    # curvature of Omega' in the boosted frame, component (x5, x0): nonzero (frame-independent obstruction)
    F50 = sp.zeros(N, N)
    for i_ in range(N):
        for j_ in range(N):
            F50[i_, j_] = cd(fz.Om[X0][i_, j_], 5, rate_z) - cd(fz.Om[5][i_, j_], X0, rate_z)
    F50 = (F50 + fz.Om[5] * fz.Om[X0] - fz.Om[X0] * fz.Om[5]).applyfunc(canon)
    check("boosted_frame_curvature_nonzero", not mzero(F50) and nz_z != [],
          "in the boosted frame (b' = 2 cg) the spinor curvature F'_x5x0 = d_x5 Omega'_x0 - d_x0 Omega'_x5 + "
          "[Omega'_x5, Omega'_x0] is nonzero for general a4, b4: Omega' cannot vanish in this frame, and in no frame "
          "where the metric is curved, because its curvature is (1/2) R_ab,mu,nu S^ab; what vanishes in this frame is "
          "only the cg part of the contraction gamma'^mu Omega'_mu (the corrected metric is flat for special a4, b4)")

    # ================================================================ 2. the diagonal frame: rescaling and the hidden block
    fd = Frame(sp.eye(8), sp.eye(8), sp.Integer(0))
    tot_d = fd.gamma_Omega()
    wr = sp.sqrt(Ea) / Q**2 * w ** sp.Rational(-3, 2)            # e^(a4/2) b4^(-1) (sin^2 z)^(-1/8)
    Mres = sum((fd.gam[mu] * sp.expand(cd(wr, mu, 0) / wr) for mu in range(8)), sp.zeros(N, N)) + tot_d
    check("rescaling_removes_the_connection_term", mzero(tot_d - CG * G[X0] - VG * G[X4]) and mzero(Mres),
          "diagonal frame: gamma^mu Omega_mu = cg gamma^(x0) + vg gamma^(x4) (control), and for Psi = e^(a4/2) b4^(-1) "
          "(sin^2 z)^(-1/8) chi with any 16 component functions chi(x0, ..., x7): gamma^mu D_mu Psi - e^(a4/2) b4^(-1) "
          "(sin^2 z)^(-1/8) gamma^mu d_mu chi = (gamma^mu d_mu ln W + gamma^mu Omega_mu) W chi = 0 exactly, W the factor "
          "(the x0 terms: e^a4 b4^(-1/2) tan z (-(3/2) H cot z) + cg = 0; the x4 terms: a4'/2 - b4'/b4 + vg = 0; the "
          "operator is first order, so this matrix identity is the identity for every chi). In the variables chi the "
          "field equation has no spin-connection term: gamma^mu d_mu chi = (m + U'(S)) chi")
    Ssym, St = sp.symbols("S St", real=True)
    U = lam * Ssym**2 / 2
    upr = sp.diff(U, Ssym).subs(Ssym, wr**2 * St)                # S[Psi] = W^2 S[chi] (W real, positive)
    check("rescaled_equation_quadratic_potential", is0(upr - lam * St * Ea / (Q**4 * w**3)),
          "with U = (lambda/2) S^2 and Psi = e^(a4/2) b4^(-1) (sin^2 z)^(-1/8) chi: S[Psi] = Psi^dagger C Psi = e^a4 "
          "b4^(-2) |sin z|^(-1/2) S[chi], so the rescaled equation is gamma^mu d_mu chi = (m + lambda e^a4 S[chi]/(b4^2 "
          "|sin z|^(1/2))) chi exactly: for U = 0 the spin-connection term is removed completely, for U != 0 it becomes "
          "an x0- and x4-dependent coupling. The exact U = 0 family (i-b) of the theory record (al = -1/4) is the same "
          "statement: its coefficient (3/2) H (4 al + 1) e^a4 b4^(-1/2) of gamma^(x4) gamma^(x0) vanishes")
    Gd = fd.Gam

    def riem(r, sg_, mu, nu):
        v = cd(Gd[r][nu][sg_], mu, 0) - cd(Gd[r][mu][sg_], nu, 0)
        for l_ in range(8):
            v += Gd[r][mu][l_] * Gd[l_][nu][sg_] - Gd[r][nu][l_] * Gd[l_][mu][sg_]
        return v

    def ric_mixed(a):
        return canon(sum(riem(r, a, r, a) for r in range(8)) / fd.gdiag[a])

    R44, R11, R00, R55 = ric_mixed(X4), ric_mixed(1), ric_mixed(X0), ric_mixed(5)
    has_a4 = any(sp.diff(x, Ea) != 0 or sp.diff(x, A1) != 0 for x in tot_d)
    Cb = H**2 * Ea**2 / Q**2
    R44w = 7 * A1**2 - A2 - 4 * A1 * B1 + 2 * B2 + B1**2
    R00w = -3 * Cb + A1**2 - A2 - sp.Rational(5, 2) * A1 * B1 + B2 / 2 + B1**2
    check("gammaOmega_sees_the_hidden_block",
          has_a4 and is0(R44 - R44w) and is0(R11 - (-A1**2 + A2 + 2 * A1 * B1)) and is0(R00 - R00w) and is0(R55 - R00),
          "diagonal frame: gamma^mu Omega_mu = (3/2) H e^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) contains a4 "
          "(e^a4 and a4'): its gamma^(x0) coefficient is (3/2) H times the inverse scale factor of the hidden block "
          "(unlike the metric of 2026-10-14, whose term 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4) contained no a4); own "
          "Riemann computation from the Christoffel symbols, compared exactly (ring: b4''/b4 = B2 + B1^2): R^x4_x4 = "
          "7 a4'^2 - a4'' - 4 a4' b4'/b4 + 2 b4''/b4 - (b4'/b4)^2, R^x1_x1 = -a4'^2 + a4'' + 2 a4' b4'/b4, R^x0_x0 = "
          "R^x5_x5 = -3 Cb + a4'^2 - a4'' - (5/2) a4' b4'/b4 + (1/2) b4''/b4 + (1/2)(b4'/b4)^2, Cb = H^2 e^(2 a4)/b4")
    anti = all(mzero(fd.gam[mu] * fd.Om[mu] + fd.Om[mu] * fd.gam[mu]) for mu in range(8))
    sg = sgn * sp.prod(DIAG)
    divm = sum((sp.Matrix(N, N, lambda i_, j_: cd(sg * fd.gam[mu][i_, j_], mu, 0)) for mu in range(8)),
               sp.zeros(N, N)) / (2 * sg)
    check("connection_free_lagrangian_same_equations", anti and mzero(divm - tot_d),
          "diagonal frame: {gamma^mu, Omega_mu} = 0 for each mu separately, so Psibar {gamma^mu, Omega_mu} Psi = 0 and "
          "the canonical spin connection drops out of the symmetrised Lagrangian: L(Omega) = L(Omega = 0) "
          "identically, and its Euler-Lagrange equations equal those of the connection-free symmetric Lagrangian, "
          "gamma^mu d_mu Psi + (1/(2 sqrt|g|)) d_mu(sqrt|g| gamma^mu) Psi = (m + U') Psi; the matrix identity "
          "(1/(2 sqrt|g|)) d_mu(sqrt|g| gamma^mu) = gamma^mu Omega_mu = cg gamma^(x0) + vg gamma^(x4) is recomputed here "
          "(sqrt|g| = sgn e^-a4 b4^2 cot z (sin^2 z)^(1/4)): the surviving term is the half-density term")
    # the spin connection in the energy-momentum tensor (diagonal frame, homogeneous configuration)
    dK1 = (fd.gam[X4] * fd.Om[1] + fd.Om[1] * fd.gam[X4]) / 2       # Omega-part of K^x4_x1 for Phi = Phi(x4)
    dK5 = (fd.gam[X4] * fd.Om[5] + fd.Om[5] * fd.gam[X4]) / 2       # Omega-part of K^x4_x5
    target = w * H * G[X4] * G[X0] * G[5] / 2
    biln = C * G[X4] * G[X0] * G[5]
    check("spin_connection_in_the_energy_momentum_tensor", mzero(dK1) and mzero(dK5 - target) and biln != Z16,
          "diagonal frame, homogeneous configuration Phi = Phi(x4): the connection part of K^x4_x1 = (1/2)(Phibar "
          "gamma^x4 D_x1 Phi - D_x1 Phibar gamma^x4 Phi) is (1/2) Phibar {gamma^x4, Omega_x1} Phi = 0 (3-space does not "
          "depend on x0), while that of K^x4_x5 is (1/2) Phibar {gamma^x4, Omega_x5} Phi = (1/2) H (sin^2 z)^(1/12) Phibar "
          "gamma^(x4) gamma^(x0) gamma^(x5) Phi (the a4', b4' part cancels exactly); C gamma^(x4) gamma^(x0) gamma^(x5) != 0, "
          "so the canonical spin connection contributes to the off-diagonal energy-momentum tensor through the extra "
          "times although it drops out of the Lagrangian")

    # ================================================================ 3. Hermiticity only up to the boundary flux
    M0 = sp.I * G[X4] * G[X0]
    Aop = -sp.I * m * G[X4] + sp.I * CG * G[X4] * G[X0]           # algebraic part of h on x0-independent functions
    AopB = Aop - sp.I * VG * I16                                  # including the term -i vg
    Bop = sp.I * (1 / DIAG[X0]) * G[X4] * G[X0]                    # coefficient of d_x0 in h
    msr = sgn * sp.prod(DIAG)                                     # sqrt|g|
    Pw = sgn * Q**3 * w**3                                        # sqrt|g|/f0 = sgn b4^(3/2) (sin^2 z)^(1/4)
    ident = mzero(msr * Bop - Pw * M0) and mzero(msr * (AopB - AopB.H) - cd(Pw, X0, 0) * M0
                                                 + sp.I * cd(msr, X4, 0) * I16) and mzero(Bop + Bop.H) \
        and is0(cd(msr, X4, 0) - 2 * VG * msr)
    v_ = G[X4] * G[X0]
    evec = (v_ + I16).columnspace()[0]                             # gamma^(x4) gamma^(x0) u = u
    flux = sp.simplify((evec.H * M0 * evec)[0, 0])
    check("good_sector_hermiticity_up_to_the_brane_flux", ident and flux != 0,
          "curved good-sector mode operator at k = 0, h = -i m gamma^(x4) + i gamma^(x4) gamma^(x0) e^a4 b4^(-1/2) (tan z "
          "d_x0 + (3/2) H) - i vg (i d_x4 Psi = h Psi for U = 0): sqrt|g| [u^dagger (h v) - (h u)^dagger v] = d_x0(sgn "
          "b4^(3/2) (sin^2 z)^(1/4) u^dagger M0 v) - i (d_x4 sqrt|g|) u^dagger v, M0 = i gamma^(x4) gamma^(x0), for all "
          "u(x0), v(x0) and every real z (matrix identities: sqrt|g| (coefficient of d_x0) = sgn b4^(3/2) (sin^2 z)^(1/4) "
          "M0, sqrt|g| (A - A^dagger) = (d_x0 sgn b4^(3/2) (sin^2 z)^(1/4)) M0 - i (d_x4 sqrt|g|) for the algebraic part "
          "A, coefficient of d_x0 anti-Hermitian; d_x4 sqrt|g| = 2 vg sqrt|g|, so the anti-Hermitian term -i vg "
          "compensates the x4 dependence of the measure). The inner product int sqrt|g| u^dagger v dx0 is therefore "
          "conserved only up to the boundary term [b4^(3/2) (sin^2 z)^(1/4) u^dagger M0 v]: it vanishes where sin z = 0 but "
          "not at the degenerate points z = pi/2 + n pi of g00 (|sin z| = 1), e.g. u = v with gamma^(x4) gamma^(x0) u = u "
          f"gives u^dagger M0 u = {sp.sstr(flux)} (|u|^2 = {sp.sstr((evec.H * evec)[0, 0])}); conservation and Krein "
          "self-adjointness need boundary conditions there")
    A2op = (Aop * Aop).applyfunc(sp.expand)
    x0s = sp.Symbol("x0", positive=True)
    norm = sp.integrate(sp.cos(6 * H * x0s) / sp.sin(6 * H * x0s) * sp.sqrt(sp.sin(6 * H * x0s)), (x0s, 0, sp.pi / (12 * H)))
    # Psi = e^(a4/2) b4^(-1) chi with i d4 chi = A chi solves i d4 Psi = (A - i vg) Psi: the matrix identity
    # i d4(F) + F A = (A - i vg) F for F = e^(a4/2) b4^(-1)
    Fs = sp.sqrt(Ea) / Q**2
    resc_ok = mzero(sp.I * cd(Fs, X4, 0) * I16 + Fs * Aop - AopB * Fs)
    ok14 = mzero(A2op - (m**2 - CG**2) * I16) and Aop != Aop.H and resc_ok and sp.simplify(norm - 1 / (3 * H)) == 0
    check("good_sector_x0_independent_modes_without_boundary_condition", ok14,
          "on x0-independent good-sector functions (k = 0; finite norm on each interval between the degenerate points, "
          f"int_0^(pi/(12 H)) cot(6 H x0) sin(6 H x0)^(1/2) dx0 = {sp.sstr(norm)}) the curved mode operator acts on Psi "
          "as A - i vg, so Psi = e^(a4/2) b4^(-1) chi with i d4 chi = A chi (verified as a matrix identity), A = -i m "
          "gamma^(x4) + i cg gamma^(x4) gamma^(x0), which is not Hermitian, and A^2 = (m^2 - cg^2) I16 exactly, cg = "
          "(3/2) H e^a4 b4^(-1/2): wherever m^2 < cg^2 the instantaneous frequencies of chi are imaginary. On the record's "
          "history a4 = H x4, b4 = e^(4 H x4/3), cg = (3/2) H e^(H x4/3) grows, so every mass falls below it at late x4: "
          "without a boundary condition at the degenerate points the good sector contains growing x0-independent modes")

    # ================================================================ 4. extra-time modes: no bound on the growth
    ks = sp.symbols("k0 k1 k2 k3 k5 k6 k7", real=True)   # the momenta along x0, x1, x2, x3, x5, x6, x7
    idx = [0, 1, 2, 3, 5, 6, 7]
    hk = -sp.I * m * G[X4] - G[X4] * sum((ks[i] * G[j] for i, j in enumerate(idx)), sp.zeros(N, N))
    E2 = m**2 + ks[0]**2 + ks[1]**2 + ks[2]**2 + ks[3]**2 - ks[4]**2 - ks[5]**2 - ks[6]**2
    sq = (hk * hk - E2 * I16).applyfunc(sp.expand) == Z16
    K = sp.Symbol("K", positive=True)
    rate = sp.sqrt(-E2.subs({ks[4]: K, ks[5]: 0, ks[6]: 0}))
    unb = sp.limit(rate, K, sp.oo) == sp.oo
    check("extra_time_growth_rates_unbounded", sq and unb,
          "flat 4+4 space (or frozen coefficients), plane waves e^(i k.x - i E x4) with h_k = -i m gamma^(x4) - "
          f"gamma^(x4) sum_a k_a gamma^(a): h_k^2 = ({sp.sstr(E2)}) I16 exactly; for an extra-time momentum k5 = K "
          f"the growth rate is Im E = {sp.sstr(rate)} for K^2 > m^2 + k0^2 + k1^2 + k2^2 + k3^2, which has no upper "
          "bound as K grows: the first-order system is not well posed in Hadamard's sense (no continuous dependence "
          "on the data in any Sobolev norm) for data that depend on x5, x6, x7. The slices x4 = const are "
          "non-characteristic, but that does not make the Cauchy problem well posed")

    # ================================================================ 5. the classical energy of dirac16complex00
    sub = {m: 2, ks[0]: 4, ks[1]: 1, ks[2]: 2, ks[3]: 0, ks[4]: 0, ks[5]: 0, ks[6]: 0}   # (k0, k1, k2, k3) = (4, 1, 2, 0)
    hs = hk.subs(sub)
    ok_comm = (B * hs - hs * B).applyfunc(sp.expand) == Z16
    Vp = (hs - 5 * I16).nullspace()
    VB = sp.Matrix.hstack(*Vp)
    Kf = (VB.H * B * VB).applyfunc(sp.simplify)
    neg = [u for u in ((B - I16) * VB).columnspace()]              # B (B - 1) = -(B - 1): eigenvalue -1
    pos = [u for u in ((B + I16) * VB).columnspace()]              # eigenvalue +1
    uN, uP = neg[0], pos[0]
    uN, uP = uN / sp.sqrt((uN.H * uN)[0, 0]), uP / sp.sqrt((uP.H * uP)[0, 0])
    cc = sp.Symbol("cc", positive=True)                           # |c|
    xs = sp.symbols("y0:8", real=True)   # flat coordinates y0..y7; y4 = the time
    kvec = [4, 1, 2, 0, 0, 0, 0, 0]

    def energy_density(u):
        phase = sp.exp(sp.I * (sum(kvec[a] * xs[a] for a in range(8) if a != X4) - 5 * xs[X4]))
        Phi = cc * u * phase
        Phid = Phi.H
        Phib = Phid * C
        Kmu = []
        for a in range(8):
            dPhi = Phi.diff(xs[a])
            dPhib = dPhi.H * C
            Kmu.append(sp.simplify(((Phib * G[a] * dPhi - dPhib * G[a] * Phi) / 2)[0, 0]))
        S_ = sp.simplify((Phib * Phi)[0, 0])
        rho = sp.simplify(-sum(Kmu[a] for a in range(8) if a != X4) + 2 * S_)
        eq = (sum((G[a] * Phi.diff(xs[a]) for a in range(8)), sp.zeros(N, 1)) - 2 * Phi).applyfunc(sp.simplify)
        charge = sp.simplify((Phid * B * Phi)[0, 0])
        return rho, eq == sp.zeros(N, 1), charge

    rN, onN, qN = energy_density(uN)
    rP, onP, qP = energy_density(uP)
    inert = (sum(1 for e_, k_ in Kf.eigenvals().items() for _ in range(k_) if sp.N(e_) > 0),
             sum(1 for e_, k_ in Kf.eigenvals().items() for _ in range(k_) if sp.N(e_) < 0))
    ok16 = ok_comm and len(Vp) == 8 and inert == (4, 4) and onN and onP and sp.simplify(rN + 5 * cc**2) == 0 and \
        sp.simplify(rP - 5 * cc**2) == 0 and sp.simplify(qN + cc**2) == 0 and sp.simplify(qP - cc**2) == 0
    check("commuting_field_energy_unbounded_below", ok16,
          "dirac16complex00 (commuting), flat frame, good sector, U = 0, m = 2, k = (k0, k1, k2, k3) = (4, 1, 2, 0), "
          "E = 5: h_k commutes with B; the E = +5 eigenspace has dimension 8 and B restricted to it has inertia "
          f"{inert}; for the positive-frequency solutions Phi = c u e^(i(k.x - 5 x4)) (field equation verified) with "
          f"B u = -u and B u = +u (|u| = 1) the energy density rho = -T^x4_x4 = -sum_(mu != x4) K_mu + m S is "
          f"{sp.sstr(rN)} and {sp.sstr(rP)} (cc = |c|), and the charge density Phi^dagger B Phi is {sp.sstr(qN)} and "
          f"{sp.sstr(qP)}: the classical energy of dirac16complex00 is unbounded below already for U = 0 in the good "
          "sector (positive-frequency modes of negative energy), and its U(1) charge is indefinite (only the local "
          "law d_mu(sqrt|g| J^mu) = 0 is proved; the total charge is constant in x4 only if no charge flows through the "
          "boundary of the slice x4 = const, which at the degenerate points z = n pi/2 is an ASSUMED no-flux condition) - "
          "unlike Dirac's 1928 wave function, whose charge density psi^dagger psi is positive")

    npass = sum(1 for x in CHECKS if x["verdict"] == "PASS")
    rep = {
        "report": "Revision/theory/reports/python-scope.json",
        "producer": "Revision/theory/python/check_scope.py (sympy, exact)",
        "spec": "Revision/SPEC.md sections 1-6: scope of the non-triviality, quantisation and energy statements",
        "inputs": ["Revision/algebra/gammas.json"],
        "independence": "no code shared with Revision/theory/wolfram/verify_scope.wls or with the other Revision "
                        "verifiers; own coefficient ring, own vielbein, connection and Riemann computation",
        "metric": "the corrected metric of 2026-10-16: diag(e^(-2 a4) b4 cot^2 z, e^(2 a4) (x3), -1, -e^(-2 a4) b4 "
                  "(sin^2 z)^(1/6) (x3)), z = 6 H x0 real",
        "coordinates": "the author's coordinates x0..x7: x0 = the hidden, space-like direction, z = 6 H x0 real "
                       "(-infinity < z < infinity); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially "
                       "deflating extra times",
        "summary": {"checks": len(CHECKS), "pass": npass, "fail": len(CHECKS) - npass},
        "checks": CHECKS,
    }
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rep, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(f"wrote {out}: {npass}/{len(CHECKS)} pass; {time.time() - T0:.1f}s")
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
