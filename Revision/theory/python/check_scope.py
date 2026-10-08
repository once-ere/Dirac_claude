#!/usr/bin/env python3
"""Revision/theory/python/check_scope.py - exact sympy checks of the SCOPE of the statements of the field-theory
record (Revision/SPEC.md sections 1-6) for the author's primordial metric: what depends on the choice of frame and
field variables, what holds only up to boundary terms, and what the indefinite structures imply.  Written anew for
Revision (no code shared with Revision/theory/wolfram/verify_scope.wls, nothing from the old stages).  Writes
Revision/theory/reports/python-scope.json (deterministic, LF).

Usage:  python Revision/theory/python/check_scope.py [--out PATH]

Coordinates as the author names them (arrays index them 0..7): x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the
three extra times, which DEFLATE exponentially (scale factor e^{-a4} sin^{1/6} z, a4 increasing); x8 = the hidden
direction, z = 6 H x8 in (0, pi/2).

Coefficient ring (exact): Ea = e^{a4(x4)}, A1, A2, A3 = a4', a4'', a4'''; s = sin(z)^(1/6), c = cos z; ch = cosh b,
sh = sinh b for a frame boost of rapidity b(x4) = beta x4 + b0 in the (x4, x8) plane.  Derivatives:
d4 Ea = Ea A1, d4 A1 = A2, d4 A2 = A3, d4 ch = beta sh, d4 sh = beta ch; d8 s = H c/s^5, d8 c = -6 H s^6.
Zero test: numerator reduced with c^2 = 1 - s^12 and ch^2 = 1 + sh^2.
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
X4, X8 = 3, 7
ETA = [1, 1, 1, -1, -1, -1, -1, 1]
N = 16
T0 = time.time()
CHECKS = []

Ea, s, c, ch, sh = sp.symbols("Ea s c ch sh", positive=True)
A1, A2, A3, A4 = sp.symbols("A1 A2 A3 A4", real=True)
H = sp.Symbol("H", positive=True)
beta = sp.Symbol("beta", real=True)
m, lam = sp.symbols("m lambda", real=True)


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
        return r + sp.diff(expr, ch) * rate * sh + sp.diff(expr, sh) * rate * ch
    if mu == X8:
        return sp.diff(expr, s) * H * c / s**5 + sp.diff(expr, c) * (-6 * H * s**6)
    return sp.Integer(0)


def reduce_poly(num):
    num = sp.expand(num)
    if num.has(c):
        num = sp.expand(sp.rem(sp.Poly(num, c), sp.Poly(c**2 - 1 + s**12, c)).as_expr())
    if num.has(ch):
        num = sp.expand(sp.rem(sp.Poly(num, ch), sp.Poly(ch**2 - 1 - sh**2, ch)).as_expr())
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
DIAG = [Ea * s, Ea * s, Ea * s, sp.Integer(1), s / Ea, s / Ea, s / Ea, c / s**6]   # e^a_mu = f_a delta^a_mu


def boost(chv, shv):
    """Lorentz boost of the frame in the (x4, x8) plane: e'^(4) = ch e^(4) + sh e^(8), e'^(8) = sh e^(4) + ch e^(8)."""
    L = sp.eye(8)
    L[X4, X4], L[X4, X8], L[X8, X4], L[X8, X8] = chv, shv, shv, chv
    return L


class Frame:
    def __init__(self, L, Linv, rate):
        self.rate = rate
        ed = sp.diag(*DIAG)
        self.e = L * ed                                          # e^a_mu
        self.E = sp.diag(*[1 / x for x in DIAG]) * Linv          # E[mu, a] = e_a^mu
        self.g = [[sp.expand(sum(ETA[a] * self.e[a, mu] * self.e[a, nu] for a in range(8))) for nu in range(8)]
                  for mu in range(8)]
        gd = [ETA[a] * DIAG[a] ** 2 for a in range(8)]          # the author's metric (diagonal)
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

    # ================================================================ 1. frame dependence of gamma^mu Omega_mu
    fb = Frame(boost(ch, sh), boost(ch, -sh), beta)              # rapidity b = beta x4 + b0
    metric_ok = all(is0(fb.g[mu][nu] - (fb.gdiag[mu] if mu == nu else 0)) for mu in range(8) for nu in range(8))
    check("boosted_frame_reproduces_metric", metric_ok and mzero(fb.e * fb.E - sp.eye(8)),
          "the frame boosted in the (x4, x8) plane, e'^(x4) = cosh b e^(x4) + sinh b e^(x8), e'^(x8) = sinh b e^(x4) + "
          "cosh b e^(x8) (other e'^(a) = e^(a), b = b(x4) = beta x4 + b0), with e^(a) the diagonal vielbein "
          "(e^a_mu = f_a delta^a_mu, f = (e^a4 sin^(1/6) z [x3], 1, e^-a4 sin^(1/6) z [x3], cot z)): "
          "eta_ab e'^a_mu e'^b_nu equals the author's metric for all 64 (mu, nu), and e' E' = 1 for its inverse")
    nbad = fb.postulate_ok()
    check("boosted_frame_canonical_connection", nbad == 0 and fb.antisym_ok(),
          "canonical spin connection of the boosted frame, omega_mu^a_b = e'^a_nu (d_mu e'_b^nu + Gamma^nu_mu,lam "
          f"e'_b^lam): the vielbein postulate holds for all 512 (a, mu, nu) ({nbad} failures) and omega_mu ab = "
          "eta_ac omega_mu^c_b is antisymmetric in a, b for every mu (exact, symbolic a4, H, beta)")
    tot_b = fb.gamma_Omega()
    want = (6 * H - beta) / 2 * (ch * G[X8] - sh * G[X4])
    nz = [mu for mu in range(8) if not mzero(fb.Om[mu])]
    check("boosted_frame_gammaOmega_formula", mzero(tot_b - want),
          "in the boosted frame gamma'^mu Omega'_mu = ((6 H - beta)/2) (cosh b gamma^(x8) - sinh b gamma^(x4)) "
          "exactly for every a4(x4), H > 0 and rapidity rate beta; at b = 0 (cosh b = 1, sinh b = 0, beta = 0) this is "
          "the value 3 H gamma^(x8) of the diagonal frame (control: the same code reproduces the diagonal-frame "
          "value). Equivalently gamma'^mu Omega'_mu = (1/2) div(e'_(a)) gamma^(a): div e'_(x4) = sinh b (beta - 6 H), "
          "div e'_(x8) = cosh b (6 H - beta), all other frame divergences vanish, and the totally antisymmetric part "
          "of omega' vanishes")
    fz = Frame(boost(ch, sh), boost(ch, -sh), 6 * H)              # rapidity b = 6 H x4 + b0
    tot_z = fz.gamma_Omega()
    nz_z = [mu for mu in range(8) if not mzero(fz.Om[mu])]
    check("boosted_frame_gammaOmega_vanishes", mzero(tot_z) and nz_z == [0, 1, 2, 3, 4, 5, 6] and fz.postulate_ok() == 0,
          "with rapidity b = 6 H x4 + b0 the term of the Euler-Lagrange operator gamma'^mu D'_mu - gamma'^mu d_mu = "
          "gamma'^mu Omega'_mu is IDENTICALLY ZERO for every H > 0 and every a4(x4) (exact), although the metric is "
          "the author's and curved (R^x8_x8 = -6 H^2): the value 3 H gamma^(x8) belongs to the diagonal vielbein, it "
          "is not a frame-independent part of the field equation. Omega'_mu itself is nonzero for mu = "
          + ", ".join(f"x{mu + 1}" for mu in nz_z) + " (zero only for x8), as it must be in every frame (its "
          "curvature is the Riemann tensor, next check)")
    # curvature of Omega' in the boosted frame, component (x1, x8): nonzero (frame-independent obstruction)
    F18 = sp.zeros(N, N)
    for i_ in range(N):
        for j_ in range(N):
            F18[i_, j_] = cd(fz.Om[X8][i_, j_], 0, 6 * H) - cd(fz.Om[0][i_, j_], X8, 6 * H)
    F18 = (F18 + fz.Om[0] * fz.Om[X8] - fz.Om[X8] * fz.Om[0]).applyfunc(canon)
    check("boosted_frame_curvature_nonzero", not mzero(F18) and nz_z != [],
          "in the boosted frame (b = 6 H x4 + b0) the spinor curvature F'_x1x8 = d_x1 Omega'_x8 - d_x8 Omega'_x1 + "
          "[Omega'_x1, Omega'_x8] is nonzero: Omega' cannot vanish in this frame, and in no frame, because its "
          "curvature is (1/2) R_ab,mu,nu S^ab and the metric is curved for H > 0; what vanishes in this frame is only "
          "the contraction gamma'^mu Omega'_mu")

    # ================================================================ 2. the diagonal frame: rescaling and a4
    fd = Frame(sp.eye(8), sp.eye(8), sp.Integer(0))
    tot_d = fd.gamma_Omega()
    w = s**-3                                                      # sin(z)^(-1/2)
    Mres = sum((fd.gam[mu] * cd(w, mu, 0) for mu in range(8)), sp.zeros(N, N)) + w * tot_d
    check("rescaling_removes_the_connection_term", mzero(tot_d - 3 * H * G[X8]) and mzero(Mres),
          "diagonal frame: gamma^mu Omega_mu = 3 H gamma^(x8) (control), and for Psi = sin^(-1/2)(z) chi with any 16 "
          "component functions chi(x1, ..., x8): gamma^mu D_mu Psi - sin^(-1/2)(z) gamma^mu d_mu chi = "
          "(gamma^mu d_mu sin^(-1/2) z + sin^(-1/2) z gamma^mu Omega_mu) chi = (tan z (-3 H sin^(-1/2) z) + 3 H "
          "sin^(-1/2) z) gamma^(x8) chi = 0 exactly (the operator is first order, so this matrix identity is the "
          "identity for every chi). In the variables chi the field equation has no spin-connection term: "
          "gamma^mu d_mu chi = (m + U'(S)) chi")
    Ssym, St = sp.symbols("S St", real=True)
    U = lam * Ssym**2 / 2
    upr = sp.diff(U, Ssym).subs(Ssym, w**2 * St)                  # S[Psi] = sin^-1(z) S[chi] (w real)
    check("rescaled_equation_quadratic_potential", is0(upr - lam * St / s**6),
          "with U = (lambda/2) S^2 and Psi = sin^(-1/2)(z) chi: S[Psi] = Psi^dagger C Psi = sin^(-1)(z) S[chi], so the "
          "rescaled equation is gamma^mu d_mu chi = (m + lambda S[chi]/sin z) chi exactly: for U = 0 the 3 H term is "
          "removed completely, for U != 0 it becomes the x8-dependent coupling lambda S[chi]/sin z. The exact U = 0 "
          "family of the theory record at alpha = -1/2 is the same statement: M = -m gamma^(x4) + 3 H (2 alpha + 1) "
          "gamma^(x4) gamma^(x8) = -m gamma^(x4) and k^2 = -m^2 (no H)")
    # a4 does not enter gamma^mu Omega_mu, although the a4 sector is curved
    Ric4 = 0
    Gd = fd.Gam
    # R^x4_x4 and R^x1_x1 from the Christoffel symbols of the diagonal metric (own computation)

    def riem(r, sg, mu, nu):
        v = cd(Gd[r][nu][sg], mu, 0) - cd(Gd[r][mu][sg], nu, 0)
        for l_ in range(8):
            v += Gd[r][mu][l_] * Gd[l_][nu][sg] - Gd[r][nu][l_] * Gd[l_][mu][sg]
        return v

    def ric_mixed(a):
        return canon(sum(riem(r, a, r, a) for r in range(8)) / fd.gdiag[a])

    R44, R11, R88 = ric_mixed(X4), ric_mixed(0), ric_mixed(X8)
    noa4 = all(sp.diff(x, v) == 0 for x in tot_d for v in (Ea, A1, A2))
    check("gammaOmega_blind_to_the_deflation", noa4 and is0(R44 - 6 * A1**2) and is0(R11 - (A2 - 6 * H**2))
          and is0(R88 + 6 * H**2),
          "diagonal frame: gamma^mu Omega_mu = 3 H gamma^(x8) contains neither e^a4 nor a4' nor a4'' (the "
          "time-direction terms of the 3 inflating and the 3 deflating directions cancel), while the a4 sector is "
          "curved: R^x4_x4 = 6 a4'^2, R^x1_x1 = a4'' - 6 H^2, R^x8_x8 = -6 H^2 (own Riemann computation from the "
          "Christoffel symbols, compared exactly). The deflation enters the field equation only through the frame "
          "factors e^(-+a4) sin^(-1/6) z of the derivative terms; in the formal limit H -> 0 gamma^mu Omega_mu = 0 "
          "although R^x4_x4 = 6 a4'^2 != 0")
    anti = all(mzero(fd.gam[mu] * fd.Om[mu] + fd.Om[mu] * fd.gam[mu]) for mu in range(8))
    sg = sp.prod(DIAG)
    divm = sum((sp.Matrix(N, N, lambda i_, j_: cd(sg * fd.gam[mu][i_, j_], mu, 0)) for mu in range(8)),
               sp.zeros(N, N)) / (2 * sg)
    check("connection_free_lagrangian_same_equations", anti and mzero(divm - tot_d),
          "diagonal frame: {gamma^mu, Omega_mu} = 0 for each mu separately, so Psibar {gamma^mu, Omega_mu} Psi = 0 and "
          "the canonical spin connection drops out of the symmetrised Lagrangian: L(Omega) = L(Omega = 0) "
          "identically, and its Euler-Lagrange equations equal those of the connection-free symmetric Lagrangian, "
          "gamma^mu d_mu Psi + (1/(2 sqrt|g|)) d_mu(sqrt|g| gamma^mu) Psi = (m + U') Psi; the matrix identity "
          "(1/(2 sqrt|g|)) d_mu(sqrt|g| gamma^mu) = gamma^mu Omega_mu = 3 H gamma^(x8) is recomputed here: the "
          "surviving term is the half-density (volume and vielbein divergence) term")
    # the spin connection is visible in the energy-momentum tensor (diagonal frame, homogeneous configuration)
    dK = (fd.gam[X4] * fd.Om[0] + fd.Om[0] * fd.gam[X4]) / 2       # Omega-part of K^x4_x1 for Phi = Phi(x4)
    target = Ea * s * H * G[X4] * G[0] * G[X8] / 2
    biln = C * G[X4] * G[0] * G[X8]
    check("spin_connection_in_the_energy_momentum_tensor", mzero(dK - target) and biln != Z16,
          "diagonal frame, homogeneous configuration Phi = Phi(x4): in K^x4_x1 = (1/2)(Phibar gamma^x4 D_x1 Phi - "
          "D_x1 Phibar gamma^x4 Phi) the derivative part vanishes and the connection part is (1/2) Phibar "
          "{gamma^x4, Omega_x1} Phi = (1/2) e^a4 sin^(1/6) z H Phibar gamma^(x4) gamma^(x1) gamma^(x8) Phi (the a4' "
          "part cancels exactly); C gamma^(x4) gamma^(x1) gamma^(x8) != 0, so the canonical spin connection "
          "contributes to the off-diagonal energy-momentum tensor although it drops out of the Lagrangian")

    # ================================================================ 3. Hermiticity only up to the brane flux
    tz = s**6 / c
    M8 = sp.I * G[X4] * G[X8]
    Aop = -sp.I * m * G[X4] + 3 * sp.I * H * G[X4] * G[X8]          # h on x8-independent functions (k = 0)
    Bop = sp.I * tz * G[X4] * G[X8]                                # coefficient of d_x8 in h
    ident = mzero(c * Bop - s**6 * M8) and mzero(c * (Aop - Aop.H) - cd(s**6, X8, 0) * M8) and mzero(Bop + Bop.H)
    v_ = G[X4] * G[X8]
    evec = (v_ + I16).columnspace()[0]                             # gamma^(x4) gamma^(x8) u = u, M8 u = i u
    flux = sp.simplify((evec.H * M8 * evec)[0, 0])
    check("good_sector_hermiticity_up_to_the_brane_flux", ident and flux != 0,
          "curved good-sector mode operator at k = 0, h = -i m gamma^(x4) + i gamma^(x4) gamma^(x8) (tan z d_x8 + 3 H) "
          "(i d_x4 Psi = h Psi for U = 0): cos z [u^dagger (h v) - (h u)^dagger v] = d_x8(sin z u^dagger M8 v), M8 = "
          "i gamma^(x4) gamma^(x8), for all u(x8), v(x8) (matrix identities: cos z * (coefficient of d_x8) = sin z M8, "
          "cos z (A - A^dagger) = (d_x8 sin z) M8 for the algebraic part A, coefficient of d_x8 anti-Hermitian). So h "
          "is symmetric for int cos z u^dagger v dx8 only up to the boundary term [sin z u^dagger M8 v]: it vanishes "
          "at the tip z -> 0 but not at the patch end z = pi/2 (finite proper distance, sin z = 1), e.g. "
          f"u = v with gamma^(x4) gamma^(x8) u = u gives u^dagger M8 u = {sp.sstr(flux)} (|u|^2 = "
          f"{sp.sstr((evec.H * evec)[0, 0])}); Hermiticity and Krein self-adjointness need boundary conditions there")
    A2op = (Aop * Aop).applyfunc(sp.expand)
    Anum = Aop.subs({m: 1, H: 1})
    # A^2 = -8 I and tr A = 0 fix the spectrum: eigenvalues +-2 sqrt(2) i with multiplicities (8, 8)
    a2n = (Anum * Anum).applyfunc(sp.expand)
    trn = sp.expand(Anum.trace())
    evs = {2 * sp.sqrt(2) * sp.I: 8, -2 * sp.sqrt(2) * sp.I: 8} if (a2n == -8 * I16 and trn == 0) else {}
    x8 = sp.Symbol("x8", positive=True)
    norm = sp.integrate(sp.cos(6 * H * x8), (x8, 0, sp.pi / (12 * H)))
    ok14 = A2op == ((m**2 - 9 * H**2) * I16).applyfunc(sp.expand) and Aop != Aop.H and \
        evs == {2 * sp.sqrt(2) * sp.I: 8, -2 * sp.sqrt(2) * sp.I: 8} and sp.simplify(norm - 1 / (6 * H)) == 0
    check("good_sector_x8_independent_modes_without_boundary_condition", ok14,
          "on x8-independent good-sector functions (k = 0; finite norm, int_0^(pi/(12 H)) cos(6 H x8) dx8 = "
          f"{sp.sstr(norm)}) the curved mode operator acts as the matrix A = -i m gamma^(x4) + 3 i H gamma^(x4) "
          "gamma^(x8), which is not Hermitian, and A^2 = (m^2 - 9 H^2) I16 exactly: for m^2 < 9 H^2 the frequencies are "
          "imaginary; at m = H = 1 the eigenvalues are +-2 sqrt(2) i (8 each), modes growing like e^(2 sqrt(2) x4). "
          "Without a boundary condition at z = pi/2 the good sector of the author's metric therefore contains growing "
          "x8-independent modes for |m + U'| < 3 H (for U != 0: the exact homogeneous solutions with k^2 = 9 H^2 - "
          "(m + lambda S0)^2 of the theory record)")

    # ================================================================ 4. extra-time modes: no bound on the growth
    ks = sp.symbols("k1 k2 k3 k5 k6 k7 k8", real=True)
    idx = [0, 1, 2, 4, 5, 6, 7]
    hk = -sp.I * m * G[X4] - G[X4] * sum((ks[i] * G[j] for i, j in enumerate(idx)), sp.zeros(N, N))
    E2 = m**2 + ks[0]**2 + ks[1]**2 + ks[2]**2 + ks[6]**2 - ks[3]**2 - ks[4]**2 - ks[5]**2
    sq = (hk * hk - E2 * I16).applyfunc(sp.expand) == Z16
    K = sp.Symbol("K", positive=True)
    rate = sp.sqrt(-E2.subs({ks[3]: K, ks[4]: 0, ks[5]: 0}))
    unb = sp.limit(rate, K, sp.oo) == sp.oo
    check("extra_time_growth_rates_unbounded", sq and unb,
          "flat 4+4 space (or frozen coefficients), plane waves e^(i k.x - i E x4) with h_k = -i m gamma^(x4) - "
          f"gamma^(x4) sum_a k_a gamma^(a): h_k^2 = ({sp.sstr(E2)}) I16 exactly; for an extra-time momentum k5 = K "
          f"the growth rate is Im E = {sp.sstr(rate)} for K^2 > m^2 + k1^2 + k2^2 + k3^2 + k8^2, which has no upper "
          "bound as K grows: the first-order system is not well posed in Hadamard's sense (no continuous dependence "
          "on the data in any Sobolev norm) for data that depend on x5, x6, x7. The slices x4 = const are "
          "non-characteristic, but that does not make the Cauchy problem well posed")

    # ================================================================ 5. the classical energy of dirac16complex00
    sub = {m: 2, ks[0]: 1, ks[1]: 2, ks[2]: 0, ks[3]: 0, ks[4]: 0, ks[5]: 0, ks[6]: 4}
    hs = hk.subs(sub)
    ok_comm = (B * hs - hs * B).applyfunc(sp.expand) == Z16
    Vp = (hs - 5 * I16).nullspace()
    VB = sp.Matrix.hstack(*Vp)
    Kf = (VB.H * B * VB).applyfunc(sp.simplify)
    # B-eigenvectors inside the E = 5 eigenspace (B commutes with h_k in the good sector)
    neg = [u for u in ((B - I16) * VB).columnspace()]              # B (B - 1) = -(B - 1): eigenvalue -1
    pos = [u for u in ((B + I16) * VB).columnspace()]              # eigenvalue +1
    uN, uP = neg[0], pos[0]
    uN, uP = uN / sp.sqrt((uN.H * uN)[0, 0]), uP / sp.sqrt((uP.H * uP)[0, 0])
    cc = sp.Symbol("cc", positive=True)                           # |c|
    xs = sp.symbols("y1:9", real=True)
    kvec = [1, 2, 0, 0, 0, 0, 0, 4]

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
          "dirac16complex00 (commuting), flat frame, good sector, U = 0, m = 2, k = (k1, k2, k3, k8) = (1, 2, 0, 4), "
          "E = 5: h_k commutes with B; the E = +5 eigenspace has dimension 8 and B restricted to it has inertia "
          f"{inert}; for the positive-frequency solutions Phi = c u e^(i(k.x - 5 x4)) (field equation verified) with "
          f"B u = -u and B u = +u (|u| = 1) the energy density rho = -T^x4_x4 = -sum_(mu != x4) K_mu + m S is "
          f"{sp.sstr(rN)} and {sp.sstr(rP)} (cc = |c|), and the charge density Phi^dagger B Phi is {sp.sstr(qN)} and "
          f"{sp.sstr(qP)}: the classical energy of dirac16complex00 is unbounded below already for U = 0 in the good "
          "sector (positive-frequency modes of negative energy), and its U(1) charge is indefinite (only the local "
          "law d_mu(cos z J^mu) = 0 is proved; the total charge is constant in x4 only if no charge flows through "
          "the boundary of the slice x4 = const, which at the brane z = pi/2 is an ASSUMED no-flux condition) - "
          "unlike Dirac's 1928 wave function, whose charge density psi^dagger psi is positive")

    npass = sum(1 for x in CHECKS if x["verdict"] == "PASS")
    rep = {
        "report": "Revision/theory/reports/python-scope.json",
        "producer": "Revision/theory/python/check_scope.py (sympy, exact)",
        "spec": "Revision/SPEC.md sections 1-6: scope of the non-triviality, quantisation and energy statements",
        "inputs": ["Revision/algebra/gammas.json"],
        "independence": "no code shared with Revision/theory/wolfram/verify_scope.wls or with the other Revision "
                        "verifiers; own coefficient ring, own vielbein, connection and Riemann computation",
        "coordinates": "x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; "
                       "x8 = the hidden direction, z = 6 H x8 in (0, pi/2)",
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
