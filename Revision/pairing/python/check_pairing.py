#!/usr/bin/env python3
"""Revision pairing: independent exact sympy verification of the pairing theorems (SPEC section 9).

Revision code; it imports nothing from the old stages and shares no code with the Wolfram side
(Revision/pairing/wolfram/).  Everything is re-derived here:

* the author's real 16 x 16 gammas T16 are re-constructed from the author's formulas (tau matrices,
  notebook input cells In[45..372]) and mapped to x1..x8 (SPEC section 2); Revision/algebra/gammas.json
  is only READ at the end for an entry-by-entry comparison;
* the metric of SPEC section 1, its Christoffel symbols, the diagonal vielbein and the canonical spin
  connection are computed with sympy;
* the field is represented by its first jet (Psi, Psi^*, d_mu Psi, d_mu Psi^* at a point) in an
  exact polynomial algebra over sympy coefficients that is either COMMUTING (dirac16complex00) or
  GRASSMANN (dirac16complex, anticommuting generators with the sign of the reordering);
* L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m S - (lambda/2) S^2 ],
  Psibar = Psi^dagger C, S = Psibar Psi, D_mu Psi = d_mu Psi + Omega_mu Psi,
  D_mu Psibar = d_mu Psibar - Psibar Omega_mu, Omega_mu = (1/2) omega_mu ab S^ab (SPEC section 3).

Checked items (the pairing-wolfram task, every item):
  T1   chirality map Gamma: L_{m,lam}[Gamma Psi] = -L_{-m,-lam}[Psi]; Euler-Lagrange map;
       T_mu nu -> -T_mu nu; J -> -J; the pair has zero total T and J; for both statistics, in the
       metric of SPEC section 1 and in a general gravitational field (matrix-level proof for arbitrary
       vielbein and connection, plus a random exact instance in both statistics).
  T2   Gamma combined with the Pin(4,4) reflection of character -1 (Gamma gamma^(x8)), i.e. the spinor
       matrix gamma^(x8), with the mirror z -> pi - z across the Z2 brane at z = pi/2:
       (m, lam) -> (-m, lam), L -> +L; EL, T and J transformation; both statistics.
  Q    quantum reading: canonical anticommutator B/sqrt|g| extracted from L; the image field Gamma Psi
       carries the Krein metric -B, its own generators reproduce the same dynamics; no cancellation
       between two independently quantised universes.
  NOT  the exact list of what the theorems do not establish.
  Further: a general diagonal field e^a_mu = h_a(x1..x8) (T1 in full; T2 as frame reflections of every
  direction), a general cubic potential U(S) (T1), negative controls, and the flat one-particle
  generator (similarities, h^2, Krein inertia (4,4) of every energy eigenspace).

Output (deterministic, LF): Revision/pairing/reports/python-pairing.json.
At the end the results are compared with Revision/pairing/pairing-theory.json (the Wolfram side's
theory record) when that file exists; otherwise the comparison is recorded as "pending".

Usage: python Revision/pairing/python/check_pairing.py
"""

from __future__ import annotations

import itertools
import json
import random
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
PAIRING = HERE.parent
REVISION = PAIRING.parent
REPORT = PAIRING / "reports" / "python-pairing.json"
FIXTURE = REVISION / "algebra" / "gammas.json"
THEORY = PAIRING / "pairing-theory.json"

COORDS = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
ETA = [1, 1, 1, -1, -1, -1, -1, 1]
N = 16

CHECKS: list[dict] = []


def check(name: str, ok: bool, detail: str) -> bool:
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS " if ok else "FAIL ") + name, flush=True)
    return ok


# =========================================================================== gammas from the formulas
def signature(lst):
    if len(set(lst)) != len(lst):
        return 0
    inv = sum(1 for i in range(len(lst)) for j in range(i + 1, len(lst)) if lst[i] > lst[j])
    return -1 if inv % 2 else 1


def blk(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))


def author_T16():
    """T16[0..7] of the notebook, re-built from In[294..372] (sympy integer matrices)."""
    I4, Z4, I8, Z8 = sp.eye(4), sp.zeros(4), sp.eye(8), sp.zeros(8)
    kd = lambda i, j: 1 if i == j else 0  # noqa: E731
    Qa = lambda h, p, q: signature([h, p, q, 4])  # noqa: E731
    Qb = lambda h, p, q: kd(p, 4) * kd(q, h) - kd(p, h) * kd(q, 4)  # noqa: E731
    s4 = {h: sp.Matrix(4, 4, lambda p, q: Qa(h, p + 1, q + 1) - Qb(h, p + 1, q + 1)) for h in (1, 2, 3)}
    t4 = {h: sp.Matrix(4, 4, lambda p, q: Qa(h, p + 1, q + 1) + Qb(h, p + 1, q + 1)) for h in (1, 2, 3)}
    sigma = blk(Z4, I4, I4, Z4)
    tau = {0: I8}
    for h in (1, 2, 3):
        tau[7 - h] = blk(Z4, t4[h], -t4[h], Z4)
        tau[h] = blk(Z4, s4[h], s4[h], Z4)
    tau[7] = tau[1] * tau[2] * tau[3] * tau[4] * tau[5] * tau[6]
    taubar = {0: I8}
    for A in range(1, 8):
        taubar[A] = sigma * tau[A].T * sigma
    return {A: blk(Z8, taubar[A], tau[A], Z8) for A in range(8)}


T16 = author_T16()
# author's coordinate x_(a+1) -> notebook frame index: x1..x3 -> 1..3, x4 -> 4, x5..x7 -> 5..7, x8 -> 0
GAM = [T16[i] for i in [1, 2, 3, 4, 5, 6, 7, 0]]
I16 = sp.eye(N)
C = GAM[7] * GAM[0] * GAM[1] * GAM[2]
CHI = GAM[7] * GAM[0] * GAM[1] * GAM[2] * GAM[3] * GAM[4] * GAM[5] * GAM[6]   # Gamma
B = -sp.I * C * GAM[3]
SAB = [[(GAM[a] * GAM[b] - GAM[b] * GAM[a]) / 4 for b in range(8)] for a in range(8)]
G8 = GAM[7]
LAM8 = [1, 1, 1, 1, 1, 1, 1, -1]          # the reflection x8 -> -x8 (z -> pi - z) on vector indices


def matzero(M):
    return all(sp.simplify(x) == 0 for x in M)


def algebra_checks():
    ok = all((GAM[a] * GAM[b] + GAM[b] * GAM[a]) == (2 * ETA[a] if a == b else 0) * I16
             for a in range(8) for b in range(8))
    check("gammas.clifford", ok, "{gamma^a, gamma^b} = 2 eta^ab I16 exactly, eta = diag(+1,+1,+1,-1,-1,-1,-1,+1) in x1..x8, for the gammas re-built here from the author's tau formulas")
    check("gammas.C", C == C.T and C * C == I16 and all((C * g).T == -(C * g) for g in GAM),
          "C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3) is real symmetric, C^2 = 1, C gamma^a real antisymmetric (a = x1..x8)")
    d = [CHI[i, i] for i in range(N)]
    check("gammas.Gamma", CHI == sp.diag(*([-1] * 8 + [1] * 8)),
          "Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) = diag(-I8, I8) (diagonal %s)" % d)
    check("gammas.Gamma_anticommutes", all(CHI * g == -g * CHI for g in GAM) and CHI * CHI == I16,
          "Gamma^2 = 1 and Gamma gamma^a = -gamma^a Gamma for all eight a; hence [Gamma, S^ab] = 0 and Gamma C = C Gamma")
    check("gammas.B", B == B.H and B * B == I16 and sorted(B.eigenvals().items()) == [(-1, 8), (1, 8)],
          "B = -i C gamma^(x4) is Hermitian, B^2 = 1, eigenvalues +1 (8 times) and -1 (8 times): signature (8,8)")
    # comparison with the Wolfram fixture (read only)
    if FIXTURE.exists():
        fx = json.loads(FIXTURE.read_text(encoding="utf-8"))
        conv = lambda v: sp.Rational(v) if isinstance(v, str) else sp.Integer(v)  # noqa: E731
        mats = [sp.Matrix([[conv(v) for v in row] for row in m]) for m in fx["gamma"]]
        same = all(mats[a] == GAM[a] for a in range(8))
        cfx = sp.Matrix([[conv(v) for v in row] for row in fx["C"]])
        gfx = sp.Matrix([[conv(v) for v in row] for row in fx["Gamma"]])
        bfx = sp.Matrix([[conv(v) for v in row] for row in fx["B"]["re"]]) + sp.I * sp.Matrix(
            [[conv(v) for v in row] for row in fx["B"]["im"]])
        same = same and cfx == C and gfx == CHI and bfx == B
        check("gammas.equal_wolfram_fixture", same,
              "the eight gammas, C, Gamma and B built here equal Revision/algebra/gammas.json entry by entry")
    else:
        CHECKS.append({"name": "gammas.equal_wolfram_fixture", "verdict": "pending",
                       "detail": "Revision/algebra/gammas.json not present"})


# =========================================================================== exact (super)commutative algebra
class Alg:
    """Polynomials in generators (ints) with sympy coefficients; odd=True: Grassmann generators."""

    __slots__ = ("t", "odd")

    def __init__(self, t, odd):
        self.t = t
        self.odd = odd

    @staticmethod
    def gen(i, odd):
        return Alg({(i,): sp.Integer(1)}, odd)

    def __add__(self, o):
        t = dict(self.t)
        for k, c in o.t.items():
            t[k] = t[k] + c if k in t else c
        return Alg(t, self.odd)

    def __neg__(self):
        return Alg({k: -c for k, c in self.t.items()}, self.odd)

    def __sub__(self, o):
        return self + (-o)

    def scale(self, c):
        if c == 0:
            return Alg({}, self.odd)
        return Alg({k: c * v for k, v in self.t.items()}, self.odd)

    def __mul__(self, o):
        if not isinstance(o, Alg):
            return self.scale(o)
        t = {}
        for k1, c1 in self.t.items():
            for k2, c2 in o.t.items():
                if self.odd:
                    if set(k1) & set(k2):
                        continue
                    inv = sum(1 for a in k1 for b in k2 if a > b)
                    c = c1 * c2 if inv % 2 == 0 else -c1 * c2
                else:
                    c = c1 * c2
                k = tuple(sorted(k1 + k2))
                t[k] = t[k] + c if k in t else c
        return Alg(t, self.odd)

    def deriv(self, i):
        """Left derivative d/d(gen i)."""
        t = {}
        for k, c in self.t.items():
            if i not in k:
                continue
            if self.odd:
                p = k.index(i)
                kk = k[:p] + k[p + 1:]
                cc = c if p % 2 == 0 else -c
            else:
                n = k.count(i)
                p = k.index(i)
                kk = k[:p] + k[p + 1:]
                cc = n * c
            t[kk] = t[kk] + cc if kk in t else cc
        return Alg(t, self.odd)

    def subs(self, rule):
        return Alg({k: c.subs(rule) for k, c in self.t.items()}, self.odd)


def zero_alg(odd):
    return Alg({}, odd)


def is_zero_coeff(c):
    e = sp.expand(c)
    if e == 0:
        return True
    return sp.simplify(e) == 0


def alg_is_zero(x):
    """(True, n) or (False, offending key)."""
    for k in sorted(x.t):
        if not is_zero_coeff(x.t[k]):
            return False, k
    return True, len(x.t)


def matvec(M, v, odd):
    out = []
    for i in range(M.rows):
        acc = zero_alg(odd)
        for j in range(M.cols):
            if M[i, j] != 0:
                acc = acc + v[j].scale(M[i, j])
        out.append(acc)
    return out


def rowmat(v, M, odd):
    out = []
    for j in range(M.cols):
        acc = zero_alg(odd)
        for i in range(M.rows):
            if M[i, j] != 0:
                acc = acc + v[i].scale(M[i, j])
        out.append(acc)
    return out


def dot(u, v, odd):
    acc = zero_alg(odd)
    for a, b in zip(u, v):
        if a.t and b.t:
            acc = acc + a * b
    return acc


def vadd(u, v):
    return [a + b for a, b in zip(u, v)]


def vsub(u, v):
    return [a - b for a, b in zip(u, v)]


# generator ids of the first jet
def id_psc(A):
    return A


def id_ps(A):
    return 16 + A


def id_dpsc(mu, A):
    return 32 + 16 * mu + A


def id_dps(mu, A):
    return 160 + 16 * mu + A


def jets(odd):
    psc = [Alg.gen(id_psc(A), odd) for A in range(N)]
    ps = [Alg.gen(id_ps(A), odd) for A in range(N)]
    dpsc = [[Alg.gen(id_dpsc(mu, A), odd) for A in range(N)] for mu in range(8)]
    dps = [[Alg.gen(id_dps(mu, A), odd) for A in range(N)] for mu in range(8)]
    return psc, ps, dpsc, dps


def transform_jets(J, P, refl, odd):
    """Psi'(x) = P Psi(R x), R a reflection of coordinates with signs refl[mu] (jets at R x)."""
    psc, ps, dpsc, dps = J
    Pc = P.conjugate()
    return (matvec(Pc, psc, odd), matvec(P, ps, odd),
            [[x.scale(refl[mu]) for x in matvec(Pc, dpsc[mu], odd)] for mu in range(8)],
            [[x.scale(refl[mu]) for x in matvec(P, dps[mu], odd)] for mu in range(8)])


# =========================================================================== geometry of SPEC section 1
x4, z, H = sp.symbols("x4 z H", real=True)
m, lam = sp.symbols("m lambda", real=True)
a4 = sp.Function("a4")(x4)


def dcoord(expr, mu):
    """d/dx_mu of a coefficient (x8 enters through z = 6 H x8)."""
    if mu == 3:
        return sp.diff(expr, x4)
    if mu == 7:
        return 6 * H * sp.diff(expr, z)
    return sp.Integer(0)


class Geometry:
    """Diagonal vielbein e^a_mu = f_mu delta; s8 = +1 on the patch z in (0, pi/2) (f8 = cot z > 0),
    s8 = -1 on the mirror patch z in (pi/2, pi) (f8 = -cot z > 0): the positive frame sqrt|g_mu mu|."""

    def __init__(self, s8=None, f=None, dfun=None, sqrtg=None):
        if f is None:
            E, Em, S6 = sp.exp(a4), sp.exp(-a4), sp.sin(z) ** sp.Rational(1, 6)
            f = [E * S6] * 3 + [sp.Integer(1)] + [Em * S6] * 3 + [s8 * sp.cot(z)]
            dfun = dcoord
        self.f = f
        self.d = dfun
        dcoord_ = dfun
        self.g = [ETA[mu] * f[mu] ** 2 for mu in range(8)]
        g = self.g
        self.sqrtg = sp.simplify(sp.Mul(*f)) if sqrtg is None else sqrtg
        # Christoffel symbols of the diagonal metric
        Gm = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
        for nu in range(8):
            for mu in range(8):
                for la in range(8):
                    v = 0
                    if nu == la:
                        v += dcoord_(g[nu], mu)
                    if nu == mu:
                        v += dcoord_(g[nu], la)
                    if mu == la:
                        v -= dcoord_(g[mu], nu)
                    Gm[nu][mu][la] = sp.simplify(v / (2 * g[nu]))
        self.Gam = Gm
        # canonical spin connection omega_mu^a_b = e^a_nu (d_mu e^nu_b + Gamma^nu_mu lam e^lam_b)
        om = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]   # om[mu][a][b] = omega_mu ab
        for mu in range(8):
            for a in range(8):
                for b in range(8):
                    v = Gm[a][mu][b] / f[b]
                    if a == b:
                        v += dcoord_(1 / f[b], mu)
                    om[mu][a][b] = sp.simplify(ETA[a] * f[a] * v)
        self.om = om
        self.Om = [sp.Matrix(N, N, lambda i, j: 0) for _ in range(8)]
        for mu in range(8):
            M = sp.zeros(N)
            for a in range(8):
                for b in range(8):
                    if om[mu][a][b] != 0:
                        M += om[mu][a][b] * SAB[a][b] / 2
            self.Om[mu] = M.applyfunc(sp.simplify)
        self.gup = [GAM[mu] / f[mu] for mu in range(8)]            # gamma^mu = e^mu_a gamma^a
        self.glow = [ETA[mu] * f[mu] * GAM[mu] for mu in range(8)]  # gamma_mu = g_mu nu gamma^nu
        self.Cgup = [C * x for x in self.gup]
        self.COm = [(C * x).applyfunc(sp.simplify) for x in self.Om]

    def reflected(self):
        """The same coefficient functions evaluated at the mirror point z -> pi - z."""
        r = Geometry.__new__(Geometry)
        rule = {z: sp.pi - z}
        sub = lambda e: sp.expand(e.subs(rule))  # noqa: E731
        r.f = [sub(e) for e in self.f]
        r.d = None
        r.g = [sub(e) for e in self.g]
        r.sqrtg = sub(self.sqrtg)
        r.Gam = None
        r.om = [[[sub(self.om[mu][a][b]) for b in range(8)] for a in range(8)] for mu in range(8)]
        r.Om = [M.subs(rule).applyfunc(sp.expand) for M in self.Om]
        r.gup = [M.subs(rule).applyfunc(sp.expand) for M in self.gup]
        r.glow = [M.subs(rule).applyfunc(sp.expand) for M in self.glow]
        r.Cgup = [C * x for x in r.gup]
        r.COm = [C * x for x in r.Om]
        return r


# =========================================================================== Lagrangian, EL, T, J on jets
def covariant(geo, J, odd):
    psc, ps, dpsc, dps = J
    Dps = [vadd(dps[mu], matvec(geo.Om[mu], ps, odd)) for mu in range(8)]
    Dpsbar = [vsub(rowmat(dpsc[mu], C, odd), rowmat(psc, geo.COm[mu], odd)) for mu in range(8)]
    return Dps, Dpsbar


def scalar_S(J, odd):
    psc, ps = J[0], J[1]
    return dot(psc, matvec(C, ps, odd), odd)


def lagrangian(geo, J, odd, mass, coup, cov=None, upoly=None):
    psc, ps = J[0], J[1]
    Dps, Dpsbar = cov if cov is not None else covariant(geo, J, odd)
    kin = zero_alg(odd)
    for mu in range(8):
        kin = kin + dot(psc, matvec(geo.Cgup[mu], Dps[mu], odd), odd)
        kin = kin - dot(Dpsbar[mu], matvec(geo.gup[mu], ps, odd), odd)
    S = scalar_S(J, odd)
    if upoly is None:
        dens = kin.scale(sp.Rational(1, 2)) - S.scale(mass) - (S * S).scale(coup / 2)
    else:                                   # U(S) = sum_k upoly[k] S^k
        dens = kin.scale(sp.Rational(1, 2)) - S.scale(mass)
        Sk = S
        for k in range(2, max(upoly) + 1):
            Sk = Sk * S
            if k in upoly:
                dens = dens - Sk.scale(upoly[k])
        if 1 in upoly:
            dens = dens - S.scale(upoly[1])
    return dens.scale(geo.sqrtg), dens


def el_operator(geo, J, odd, mass, coup):
    """E = gamma^mu D_mu Psi - (m + lambda S) Psi (a vector of 16 algebra elements)."""
    ps = J[1]
    Dps, _ = covariant(geo, J, odd)
    S = scalar_S(J, odd)
    out = [zero_alg(odd) for _ in range(N)]
    for mu in range(8):
        out = vadd(out, matvec(geo.gup[mu], Dps[mu], odd))
    return [out[A] - ps[A].scale(mass) - (S * ps[A]).scale(coup) for A in range(N)]


def emt(geo, J, odd, mass, coup):
    """T_mu nu (coordinate components, mu <= nu): the symmetric (Belinfante) form
    (1/4)[Psibar gamma_mu D_nu Psi + Psibar gamma_nu D_mu Psi - (D_mu Psibar) gamma_nu Psi
    - (D_nu Psibar) gamma_mu Psi] - g_mu nu L/sqrt|g|."""
    psc, ps = J[0], J[1]
    cov = covariant(geo, J, odd)
    Dps, Dpsbar = cov
    _, dens = lagrangian(geo, J, odd, mass, coup, cov)
    T = {}
    for mu in range(8):
        for nu in range(mu, 8):
            t = (dot(psc, matvec(C * geo.glow[mu], Dps[nu], odd), odd)
                 + dot(psc, matvec(C * geo.glow[nu], Dps[mu], odd), odd)
                 - dot(Dpsbar[mu], matvec(geo.glow[nu], ps, odd), odd)
                 - dot(Dpsbar[nu], matvec(geo.glow[mu], ps, odd), odd)).scale(sp.Rational(1, 4))
            if mu == nu:
                t = t - dens.scale(geo.g[mu])
            T[(mu, nu)] = t
    return T


def current(geo, J, odd):
    """J^mu = i Psibar gamma^mu Psi (Hermitian; the U(1) Noether current)."""
    psc, ps = J[0], J[1]
    return [dot(psc, matvec(sp.I * geo.Cgup[mu], ps, odd), odd) for mu in range(8)]


def el_from_lagrangian(geo, J, odd, mass, coup):
    """dL/dPsi^*_A - d_mu (dL/d(d_mu Psi^*_A)) for the density L (left derivatives)."""
    Ld, _ = lagrangian(geo, J, odd, mass, coup)
    out = []
    for A in range(N):
        e = Ld.deriv(id_psc(A))
        for mu in range(8):
            q = Ld.deriv(id_dpsc(mu, A))      # linear in Psi
            for k, c in q.t.items():
                if len(k) != 1 or not (16 <= k[0] < 32):
                    raise RuntimeError("dL/d(d Psi^*) is not linear in Psi")
                Bi = k[0] - 16
                e = e - Alg({k: geo.d(c, mu)}, odd) - Alg({(id_dps(mu, Bi),): c}, odd)
        out.append(e)
    return out


# =========================================================================== the checks
def all_zero(items):
    for idx, x in items:
        ok, info = alg_is_zero(x)
        if not ok:
            return False, "nonzero at %s, monomial %s" % (idx, info)
    return True, "%d components identically zero" % len(items)


def stat_name(odd):
    return "grassmann" if odd else "commuting"


def field_name(odd):
    return "dirac16complex" if odd else "dirac16complex00"


def geometry_checks(geo):
    # antisymmetry of omega_mu ab and covariant constancy of gamma^mu (validates the connection)
    anti = all(sp.simplify(geo.om[mu][a][b] + geo.om[mu][b][a]) == 0
               for mu in range(8) for a in range(8) for b in range(8))
    check("geometry.omega_antisymmetric", anti,
          "the canonical spin connection omega_mu ab = eta_ac omega_mu^c_b of the metric of SPEC section 1 is antisymmetric in (a, b) for all mu")
    ok = True
    for mu in range(8):
        for nu in range(8):
            M = sp.diff(geo.gup[nu], x4) if mu == 3 else (6 * H * sp.diff(geo.gup[nu], z) if mu == 7 else sp.zeros(N))
            for la in range(8):
                if geo.Gam[nu][mu][la] != 0:
                    M = M + geo.Gam[nu][mu][la] * geo.gup[la]
            M = M + geo.Om[mu] * geo.gup[nu] - geo.gup[nu] * geo.Om[mu]
            if not matzero(M):
                ok = False
    check("geometry.gamma_covariantly_constant", ok,
          "d_mu gamma^nu + Gamma^nu_mu lam gamma^lam + [Omega_mu, gamma^nu] = 0 for all mu, nu (the vielbein postulate holds for Omega_mu = (1/2) omega_mu ab S^ab)")
    nz = sorted({(mu, a, b) for mu in range(8) for a in range(8) for b in range(a + 1, 8)
                 if sp.simplify(geo.om[mu][a][b]) != 0})
    det = "; ".join("omega_%s %s%s = %s" % (COORDS[mu], COORDS[a], COORDS[b], sp.simplify(geo.om[mu][a][b]).subs(sp.Derivative(a4, x4), sp.Symbol("a4p")).subs(a4, sp.Symbol("a4")))
                    for mu, a, b in nz)
    CHECKS.append({"name": "geometry.spin_connection_components", "verdict": "PASS", "detail": "nonzero components (a < b): " + det})
    rule = {z: sp.pi - z}
    iso = all(sp.simplify(gg.subs(rule) - gg) == 0 for gg in geo.g)
    deg = (sp.limit(geo.g[7], z, sp.pi / 2) == 0 and sp.limit(geo.sqrtg, z, sp.pi / 2) == 0
           and sp.simplify(geo.sqrtg - sp.cos(z)) == 0)
    check("geometry.brane_degenerate", deg,
          "sqrt|g| = %s on the patch; at the brane z = pi/2: g_88 -> 0 and sqrt|g| -> 0 (a degenerate surface of the metric)" % geo.sqrtg)
    check("geometry.mirror_isometry", iso,
          "g_mu mu(pi - z) = g_mu mu(z) for every component: z -> pi - z (x8 -> pi/(6H) - x8, the Z2 brane at z = pi/2) is an isometry of the metric of SPEC section 1")


def t1_metric(geo, odd):
    sn, fn = stat_name(odd), field_name(odd)
    J = jets(odd)
    JG = transform_jets(J, CHI, [1] * 8, odd)
    # S invariant
    ok, info = all_zero([("S", scalar_S(JG, odd) - scalar_S(J, odd))])
    check("T1.metric.%s.S_invariant" % sn, ok, "%s: S[Gamma Psi] - S[Psi] = 0 (%s)" % (fn, info))
    # Lagrangian
    L1, _ = lagrangian(geo, JG, odd, m, lam)
    L2, _ = lagrangian(geo, J, odd, -m, -lam)
    ok, info = all_zero([("L", L1 + L2)])
    check("T1.metric.%s.lagrangian" % sn, ok,
          "%s, metric of SPEC section 1 with the canonical spin connection: L_{m,lambda}[Gamma Psi] + L_{-m,-lambda}[Psi] = 0 on the full first jet (%s)" % (fn, info))
    # negative controls: the wrong mass map, and the identity without the map
    bad1 = alg_is_zero(L1 + lagrangian(geo, J, odd, m, lam)[0])[0]
    bad2 = alg_is_zero(L1 + lagrangian(geo, J, odd, -m, lam)[0])[0]
    check("T1.metric.%s.negative_controls" % sn, not bad1 and not bad2,
          "%s: L_{m,lambda}[Gamma Psi] + L_{m,lambda}[Psi] != 0 and L_{m,lambda}[Gamma Psi] + L_{-m,lambda}[Psi] != 0 (the checker detects a wrong mass/coupling map)" % fn)
    # EL derived from L equals sqrt|g| C E
    E = el_operator(geo, J, odd, m, lam)
    CE = matvec(C, E, odd)
    EL = el_from_lagrangian(geo, J, odd, m, lam)
    ok, info = all_zero([(A, EL[A] - CE[A].scale(geo.sqrtg)) for A in range(N)])
    check("T1.metric.%s.euler_lagrange_derived" % sn, ok,
          "%s: dL/dPsi^*_A - d_mu dL/d(d_mu Psi^*_A) = sqrt|g| [C (gamma^mu D_mu Psi - (m + lambda S) Psi)]_A for all 16 A, i.e. the EL equation gamma^mu D_mu Psi = (m + U'(S)) Psi (%s)" % (fn, info))
    # EL map
    E1 = el_operator(geo, JG, odd, m, lam)
    E2 = matvec(CHI, el_operator(geo, J, odd, -m, -lam), odd)
    ok, info = all_zero([(A, E1[A] + E2[A]) for A in range(N)])
    check("T1.metric.%s.euler_lagrange_map" % sn, ok,
          "%s: E_{m,lambda}[Gamma Psi] = -Gamma E_{-m,-lambda}[Psi]; so Psi solves the (-m,-lambda) equations iff Gamma Psi solves the (m,lambda) equations (%s)" % (fn, info))
    # EMT and current
    T1 = emt(geo, JG, odd, m, lam)
    T2 = emt(geo, J, odd, -m, -lam)
    ok, info = all_zero([(k, T1[k] + T2[k]) for k in sorted(T1)])
    check("T1.metric.%s.emt" % sn, ok,
          "%s: T_mu nu[Gamma Psi; m, lambda] = -T_mu nu[Psi; -m, -lambda] for all 36 components mu <= nu (%s)" % (fn, info))
    Tp = emt(geo, J, odd, m, lam)
    Tq = emt(geo, JG, odd, -m, -lam)
    ok, info = all_zero([(k, Tp[k] + Tq[k]) for k in sorted(Tp)])
    check("T1.metric.%s.pair_total_emt_zero" % sn, ok,
          "%s: the pair (Psi with (m, lambda), Gamma Psi with (-m, -lambda)) has T_mu nu[Psi; m, lambda] + T_mu nu[Gamma Psi; -m, -lambda] = 0 identically (all 36 components) (%s)" % (fn, info))
    J1, J2 = current(geo, JG, odd), current(geo, J, odd)
    ok, info = all_zero([(mu, J1[mu] + J2[mu]) for mu in range(8)])
    check("T1.metric.%s.current" % sn, ok,
          "%s: J^mu[Gamma Psi] = -J^mu[Psi] (J^mu = i Psibar gamma^mu Psi); the pair's total charge current vanishes identically (%s)" % (fn, info))


def p_name(P):
    for nm, M in (("1", I16), ("Gamma", CHI), ("gamma^(x8)", G8), ("Gamma gamma^(x8)", CHI * G8)):
        if P == M:
            return nm
    return "?"


def t2_metric(patch, mirror, odd):
    """Psi~(x) = P Psi(R x) on the mirror patch, R: z -> pi - z; compare with the patch at R x."""
    sn, fn = stat_name(odd), field_name(odd)
    J = jets(odd)
    refl = patch.reflected()
    table = []
    found = {}
    for P in (I16, CHI, G8, CHI * G8):
        JP = transform_jets(J, P, LAM8, odd)
        Lm, _ = lagrangian(mirror, JP, odd, m, lam)
        hit = None
        for sg, sm, sl in itertools.product((1, -1), (1, -1), (1, -1)):
            Lp, _ = lagrangian(refl, J, odd, sm * m, sl * lam)
            if alg_is_zero(Lm - Lp.scale(sg))[0]:
                hit = (sg, sm, sl)
                break
        found[p_name(P)] = hit
        if hit is None:
            table.append("P = %s: no relation L_mirror = sigma L_patch(R x) with (m, lambda) -> (+-m, +-lambda)" % p_name(P))
        else:
            table.append("P = %s: L_{m,lambda}[P Psi(Rx)] = %s L_{%sm,%slambda}[Psi](Rx)"
                         % (p_name(P), "+" if hit[0] > 0 else "-", "" if hit[1] > 0 else "-", "" if hit[2] > 0 else "-"))
    check("T2.metric.%s.reflection_table" % sn,
          found["gamma^(x8)"] == (1, -1, 1) and found["Gamma gamma^(x8)"] == (-1, 1, -1),
          "%s, mirror across the Z2 brane z -> pi - z with the positive frame on both sides: " % fn + "; ".join(table)
          + ". So the reflection Gamma gamma^(x8) (spinor action P^-1 gamma^a P = Lambda^a_b gamma^b, character -1 on S) gives L -> -L_{m,-lambda}; combined with Gamma (Gamma Gamma gamma^(x8) = gamma^(x8)) it gives T2: (m, lambda) -> (-m, lambda), L -> +L")
    # T2 in detail for P = gamma^(x8)
    JP = transform_jets(J, G8, LAM8, odd)
    E1 = el_operator(mirror, JP, odd, m, lam)
    E2 = matvec(G8, el_operator(refl, J, odd, -m, lam), odd)
    ok, info = all_zero([(A, E1[A] + E2[A]) for A in range(N)])
    check("T2.metric.%s.euler_lagrange_map" % sn, ok,
          "%s: E_{m,lambda}[gamma^(x8) Psi(Rx)](x) = -gamma^(x8) E_{-m,lambda}[Psi](Rx): Psi solves the (-m, lambda) equations on the patch iff its mirror image solves the (m, lambda) equations on the mirror patch (%s)" % (fn, info))
    T1 = emt(mirror, JP, odd, m, lam)
    T2 = emt(refl, J, odd, -m, lam)
    ok, info = all_zero([(k, T1[k] - T2[k].scale(LAM8[k[0]] * LAM8[k[1]])) for k in sorted(T1)])
    check("T2.metric.%s.emt" % sn, ok,
          "%s: T_mu nu[gamma^(x8) Psi(Rx); m, lambda](x) = Lambda_mu Lambda_nu T_mu nu[Psi; -m, lambda](Rx) (the pull-back by R; no sign change of the energy density) (%s)" % (fn, info))
    J1, J2 = current(mirror, JP, odd), current(refl, J, odd)
    ok, info = all_zero([(mu, J1[mu] - J2[mu].scale(LAM8[mu])) for mu in range(8)])
    check("T2.metric.%s.current" % sn, ok,
          "%s: J^mu[mirror image](x) = Lambda^mu J^mu[Psi](Rx): the charge density J^(x4) is unchanged (%s)" % (fn, info))
    S1, S2 = scalar_S(JP, odd), scalar_S(J, odd)
    ok, info = all_zero([("S", S1 + S2)])
    check("T2.metric.%s.S_odd" % sn, ok, "%s: S[gamma^(x8) Psi] = -S[Psi] (S is a pseudo-scalar under the hidden-direction reflection because C contains gamma^(x8)) (%s)" % (fn, info))


def general_field_matrix_checks():
    """T1 and T2 for an arbitrary vielbein e^mu_a(x), connection omega_mu ab(x), density sqrt|g|(x):
    L is a linear combination, with these arbitrary coefficient functions, of the bilinears with the
    matrices C gamma^a (d Psi), C gamma^a S^bc and S^bc C gamma^a type (connection), C (mass), and
    the quartic S^2; the identities below for every basis matrix prove the statements for any field."""
    basis_kin = [C * g for g in GAM]
    basis_con = [C * GAM[a] * SAB[b][c] for a in range(8) for b in range(8) for c in range(b + 1, 8)]
    basis_con += [C * SAB[b][c] * GAM[a] for a in range(8) for b in range(8) for c in range(b + 1, 8)]
    ok = all(CHI.T * M * CHI == -M for M in basis_kin + basis_con) and CHI.T * C * CHI == C
    ok = ok and all(CHI.T * g * CHI == -g for g in GAM) and all(CHI.T * (C * GAM[a]) * CHI == -(C * GAM[a]) for a in range(8))
    check("T1.general_field.matrix_identities", ok,
          "Gamma^T M Gamma = -M for all %d kinetic and connection basis matrices M (C gamma^a; C gamma^a S^bc; C S^bc gamma^a) and Gamma^T C Gamma = +C; since Gamma is constant and real, for ANY vielbein, spin connection and sqrt|g|: L_{m,lambda}[Gamma Psi] = -L_{-m,-lambda}[Psi], the EL map, J -> -J, and (the identity holding for every vielbein) T_mu nu -> -T_mu nu, for both statistics" % (len(basis_kin) + len(basis_con)))
    Lam = sp.diag(*LAM8)
    ok = G8.T * C * G8 == -C
    ok = ok and all(G8.T * C * GAM[a] * G8 == C * sum((Lam[a, b] * GAM[b] for b in range(8)), sp.zeros(N)) for a in range(8))
    ok = ok and all(G8.inv() * SAB[a][b] * G8 == LAM8[a] * LAM8[b] * SAB[a][b] for a in range(8) for b in range(8))
    P2 = CHI * G8
    ok2 = all(P2.inv() * GAM[a] * P2 == LAM8[a] * GAM[a] for a in range(8)) and P2.T * C * P2 == -C
    ok3 = all(G8.inv() * GAM[a] * G8 == -LAM8[a] * GAM[a] for a in range(8))
    check("T2.general_field.matrix_identities", ok and ok2 and ok3,
          "gamma^(x8)^T C gamma^(x8) = -C; gamma^(x8)^T C gamma^a gamma^(x8) = C Lambda^a_b gamma^b; gamma^(x8)^-1 S^ab gamma^(x8) = Lambda^a Lambda^b S^ab (Lambda = diag(1,1,1,1,1,1,1,-1)); (Gamma gamma^(x8))^-1 gamma^a (Gamma gamma^(x8)) = Lambda^a_b gamma^b and (Gamma gamma^(x8))^T C (Gamma gamma^(x8)) = -C; gamma^(x8)^-1 gamma^a gamma^(x8) = -Lambda^a_b gamma^b. Hence in ANY field with an isometry reflecting the x8 frame direction the hidden-direction reflection with gamma^(x8) maps (m, lambda) -> (-m, lambda), L -> +L")
    # table of all single reflections
    rows = []
    for b in range(8):
        sS = 1 if GAM[b].T * C * GAM[b] == C else (-1 if GAM[b].T * C * GAM[b] == -C else 0)
        Lb = [(-1 if a == b else 1) for a in range(8)]
        kin_inv = all(GAM[b].T * C * GAM[a] * GAM[b] == Lb[a] * C * GAM[a] for a in range(8))
        kin_flip = all(GAM[b].T * C * GAM[a] * GAM[b] == -Lb[a] * C * GAM[a] for a in range(8))
        rows.append("%s: S -> %sS, kinetic %s" % (COORDS[b], "+" if sS > 0 else "-", "invariant" if kin_inv else ("-1" if kin_flip else "?")))
    expect = all(("S -> -S, kinetic invariant" in r) for r in rows[:3] + rows[7:]) and all(("S -> +S, kinetic -1" in r) for r in rows[3:7])
    check("T2.general_field.reflection_table", expect,
          "spinor matrix gamma^(b) with the frame reflection of direction b: " + "; ".join(rows)
          + ". The space-like reflections (x1, x2, x3, x8) give (m, lambda) -> (-m, lambda), L -> +L; the time-like ones (x4..x7) give L -> -L_{-m,-lambda}")


def random_instance_general_field():
    rng = random.Random(20261001)
    rq = lambda: sp.Rational(rng.randint(-9, 9), rng.randint(1, 5))  # noqa: E731

    class G:
        pass
    geo = G()
    E = sp.Matrix(8, 8, lambda i, j: rq())      # e^mu_a (arbitrary, not diagonal)
    geo.gup = [sum((E[mu, a] * GAM[a] for a in range(8)), sp.zeros(N)) for mu in range(8)]
    geo.Cgup = [C * x for x in geo.gup]
    geo.Om = []
    for mu in range(8):
        M = sp.zeros(N)
        for a in range(8):
            for b in range(a + 1, 8):
                M += rq() * SAB[a][b]           # Omega_mu = (1/2) omega_mu ab S^ab, omega antisymmetric
        geo.Om.append(M)
    geo.COm = [C * x for x in geo.Om]
    geo.sqrtg = abs(rq()) + 1
    for odd in (False, True):
        J = jets(odd)
        JG = transform_jets(J, CHI, [1] * 8, odd)
        L1, _ = lagrangian(geo, JG, odd, m, lam)
        L2, _ = lagrangian(geo, J, odd, -m, -lam)
        E1 = el_operator(geo, JG, odd, m, lam)
        E2 = matvec(CHI, el_operator(geo, J, odd, -m, -lam), odd)
        ok, info = all_zero([("L", L1 + L2)] + [(A, E1[A] + E2[A]) for A in range(N)])
        check("T1.general_field.random_instance.%s" % stat_name(odd), ok,
              "%s, a random exact non-diagonal vielbein and connection (seed 20261001): L_{m,lambda}[Gamma Psi] + L_{-m,-lambda}[Psi] = 0 and E_{m,lambda}[Gamma Psi] + Gamma E_{-m,-lambda}[Psi] = 0 (%s)" % (field_name(odd), info))


def quantum_checks(geo):
    # canonical structure from the x4-velocity terms of the Grassmann L
    J = jets(True)
    Ld, _ = lagrangian(geo, J, True, m, lam)
    K = sp.zeros(N)
    for A in range(N):
        for Bi in range(N):
            c1 = Ld.t.get((id_psc(A), id_dps(3, Bi)), 0)
            c2 = Ld.t.get(tuple(sorted((id_dpsc(3, A), id_ps(Bi)))), 0)
            # psi^*_A dpsi_B (coefficient c1) and dpsi^*_A psi_B: sorted order puts psi_B (16+B) before dpsi^*_4A
            # (32+48+A), so the stored monomial is psi_B dpsi^*_A = -dpsi^*_A psi_B
            K[A, Bi] = sp.simplify(c1 + c2)       # = coefficient after moving d_4 onto Psi (up to a total derivative)
    # L ~ i Psi^dagger M d_4 Psi  =>  {Psi_A, Psi^dagger_B} = (M^-1)_AB
    M = (-sp.I * K).applyfunc(sp.simplify)
    X = M.inv().applyfunc(sp.simplify)
    ok = matzero(X - B / geo.sqrtg)
    check("Q.canonical_anticommutator", ok,
          "from the x4-velocity terms of L (dirac16complex): L = i Psi^dagger M d_4 Psi + ... with M = sqrt|g| B, hence {Psi_A(x), Psi^dagger_B(y)} = B_AB delta^7(x - y)/sqrt|g| (sqrt|g| = %s)" % geo.sqrtg)
    ok = CHI * B * CHI == -B and sorted((-B).eigenvals().items()) == [(-1, 8), (1, 8)]
    check("Q.image_krein_metric", ok,
          "Gamma B Gamma^dagger = -B: if Psi is canonically quantised ({Psi, Psi^dagger} = B/sqrt|g|), the image field Gamma Psi has {Gamma Psi, (Gamma Psi)^dagger} = -B/sqrt|g|, the Krein metric -B (also of signature (8,8))")
    # the image's own canonical quantisation: L' = L_{-m,-lambda}[Psi] = -L_{m,lambda}[Psi'] gives M' = -M
    JG = transform_jets(J, CHI, [1] * 8, True)
    Lg, _ = lagrangian(geo, JG, True, m, lam)
    # L' as a function of the image jets is -L_{m,lambda}: its velocity matrix is -K
    ok = alg_is_zero(Lg + lagrangian(geo, J, True, -m, -lam)[0])[0]
    Xp = ((-sp.I * (-K)).inv()).applyfunc(sp.simplify)
    ok = ok and matzero(Xp + B / geo.sqrtg) and matzero(CHI * X * CHI - Xp)
    check("Q.image_own_quantisation", ok,
          "the image Psi' = Gamma Psi obeys the (m, lambda) equations but its dynamics comes from L' = -L_{m,lambda}[Psi']: canonical quantisation of L' gives {Psi', Psi'^dagger} = -B/sqrt|g| = Gamma (B/sqrt|g|) Gamma, consistent with the map")
    # one-particle generators: i d_4 Psi = G Psi with G = X h (flat 4+4 slice, plane wave k_j in x1..x3, x5..x8)
    ks = sp.symbols("k1 k2 k3 k5 k6 k7 k8", real=True)
    kv = dict(zip([0, 1, 2, 4, 5, 6, 7], ks))
    def h_of(mass):
        # H density = -(L - velocity terms) for L = Psibar gamma^a d_a Psi - m S in flat space, d_j -> i k_j
        return mass * C - sum((sp.I * kv[j] * C * GAM[j] for j in kv), sp.zeros(N))
    G1 = B * h_of(m)                 # universe 1: field Psi, (m, lambda), anticommutator B
    G_image_by_map = CHI * (B * h_of(-m)) * CHI      # image of a (-m) field's dynamics
    G_image_own = (-B) * (-h_of(m))  # image's own canonical data: metric -B, generator -h_m
    ok = (G_image_own - G_image_by_map).applyfunc(sp.expand) == sp.zeros(N) and (G_image_own - G1).applyfunc(sp.expand) == sp.zeros(N)
    check("Q.image_generators_same_dynamics", ok,
          "with metric -B and its own generator density -h_m the image field has the one-particle generator (-B)(-h_m) = B h_m = Gamma (B h_{-m}) Gamma: the Krein sign and the generator sign compensate, the image evolves exactly by the (m, lambda) dynamics")
    # no cancellation between two independently quantised universes
    Gk0 = (B * h_of(m)).subs({k: 0 for k in ks})
    Gk0m = (B * h_of(-m)).subs({k: 0 for k in ks})
    ev1 = Gk0.eigenvals()
    ev2 = Gk0m.eigenvals()
    Gtot = sp.diag(Gk0, Gk0m)
    evt = Gtot.eigenvals()
    rank_cross = (CHI * B).rank()
    ok = (rank_cross == 16 and all(sp.simplify(e) != 0 for e in evt) and sum(evt.values()) == 32)
    check("Q.no_cancellation_independent_universes", ok,
          "two independently quantised universes (Psi1 with (m, lambda), Psi2 with (-m, -lambda), each with its own anticommutator B/sqrt|g|, {Psi1, Psi2^dagger} = 0) have the block one-particle generator diag(B h_m, B h_{-m}) with eigenvalues %s (zero momentum, all nonzero for m != 0): the total generators do not cancel as operators. Psi2 = Gamma Psi1 is impossible for independent universes because {Gamma Psi1, Psi1^dagger} = Gamma B/sqrt|g| has rank %d != 0; T[Psi] + T[Gamma Psi] = 0 is an identity for ONE field and its image, not a cancellation between two independent quantum systems"
          % (sorted(((str(k), v) for k, v in evt.items())), rank_cross))
    _ = (ev1, ev2)



def general_potential(geo, odd):
    sn, fn = stat_name(odd), field_name(odd)
    u1, u2, u3 = sp.symbols("u1 u2 u3", real=True)
    J = jets(odd)
    JG = transform_jets(J, CHI, [1] * 8, odd)
    U = {1: u1, 2: u2, 3: u3}
    Um = {k: -v for k, v in U.items()}
    L1, _ = lagrangian(geo, JG, odd, m, 0, upoly=U)
    L2, _ = lagrangian(geo, J, odd, -m, 0, upoly=Um)
    ok, info = all_zero([("L", L1 + L2)])
    check("T1.metric.%s.general_potential" % sn, ok,
          "%s: with U(S) = u1 S + u2 S^2 + u3 S^3 (a general cubic, Grassmann powers of S computed in the exterior algebra): L_{m,U}[Gamma Psi] = -L_{-m,-U}[Psi] (%s)" % (fn, info))


def diagonal8_checks(odd):
    """A general diagonal (4,4) field: e^a_mu = h_a(x1..x8) delta^a_mu, eight arbitrary functions."""
    sn, fn = stat_name(odd), field_name(odd)
    X = sp.symbols("x1:9", real=True)
    h = [sp.Function("h%d" % (a + 1))(*X) for a in range(8)]
    dfun = lambda e, mu: sp.diff(e, X[mu])  # noqa: E731
    geo = Geometry(f=h, dfun=dfun)
    J = jets(odd)
    JG = transform_jets(J, CHI, [1] * 8, odd)
    L1, _ = lagrangian(geo, JG, odd, m, lam)
    L2, _ = lagrangian(geo, J, odd, -m, -lam)
    E = el_operator(geo, J, odd, m, lam)
    CE = matvec(C, E, odd)
    EL = el_from_lagrangian(geo, J, odd, m, lam)
    E1 = el_operator(geo, JG, odd, m, lam)
    E2 = matvec(CHI, el_operator(geo, J, odd, -m, -lam), odd)
    T1 = emt(geo, JG, odd, m, lam)
    T2 = emt(geo, J, odd, -m, -lam)
    J1, J2 = current(geo, JG, odd), current(geo, J, odd)
    items = ([("L", L1 + L2)] + [("EL%d" % A, EL[A] - CE[A].scale(geo.sqrtg)) for A in range(N)]
             + [("E%d" % A, E1[A] + E2[A]) for A in range(N)] + [(k, T1[k] + T2[k]) for k in sorted(T1)]
             + [("J%d" % mu, J1[mu] + J2[mu]) for mu in range(8)])
    ok, info = all_zero(items)
    check("T1.diagonal8.%s" % sn, ok,
          "%s, general diagonal field e^a_mu = h_a(x1..x8) delta^a_mu with its canonical spin connection: L_{m,lambda}[Gamma Psi] = -L_{-m,-lambda}[Psi]; EL derived from L = sqrt|g| C E; E_{m,lambda}[Gamma Psi] = -Gamma E_{-m,-lambda}[Psi]; T -> -T (36 components); J -> -J (%s)" % (fn, info))
    # T2 as a frame reflection at the same point: e' = R_n e, Psi' = gamma^n Psi
    rows, good = [], True
    for n in range(8):
        fr = [(-h[a] if a == n else h[a]) for a in range(8)]
        geo_r = Geometry(f=fr, dfun=dfun, sqrtg=geo.sqrtg)
        JP = transform_jets(J, GAM[n], [1] * 8, odd)
        Lr, _ = lagrangian(geo_r, JP, odd, m, lam)
        if ETA[n] > 0:
            ok_n = alg_is_zero(Lr - lagrangian(geo, J, odd, -m, lam)[0])[0]
            rows.append("%s: L_{m,lambda}[gamma^n Psi; R_n e] = +L_{-m,lambda}[Psi; e] %s" % (COORDS[n], "holds" if ok_n else "FAILS"))
        else:
            ok_n = alg_is_zero(Lr + lagrangian(geo, J, odd, -m, -lam)[0])[0]
            rows.append("%s: L_{m,lambda}[gamma^n Psi; R_n e] = -L_{-m,-lambda}[Psi; e] %s" % (COORDS[n], "holds" if ok_n else "FAILS"))
        good = good and ok_n
    check("T2.diagonal8.frame_reflections.%s" % sn, good,
          "%s, general diagonal field, frame reflection of direction n (e'^n = -e^n, same metric, same sqrt|g|) with Psi' = gamma^n Psi = Gamma (Gamma gamma^n) Psi: " % fn + "; ".join(rows))


def quantum_one_particle_checks():
    ks = sp.symbols("k1 k2 k3 k5 k6 k7 k8", real=True)
    idx = [0, 1, 2, 4, 5, 6, 7]
    def G_of(mass, kk):
        h = mass * C - sum((sp.I * kk[i] * C * GAM[j] for i, j in enumerate(idx)), sp.zeros(N))
        return B * h
    kR = list(ks[:-1]) + [-ks[-1]]
    ok1 = (CHI * G_of(m, ks) * CHI - G_of(-m, ks)).applyfunc(sp.expand) == sp.zeros(N)
    ok2 = (G8 * G_of(m, ks) * G8 - G_of(-m, kR)).applyfunc(sp.expand) == sp.zeros(N)
    E2 = m ** 2 + ks[0] ** 2 + ks[1] ** 2 + ks[2] ** 2 - ks[3] ** 2 - ks[4] ** 2 - ks[5] ** 2 + ks[6] ** 2
    sq1 = (G_of(m, ks) ** 2 - E2 * I16).applyfunc(sp.expand) == sp.zeros(N)
    sq2 = (G_of(-m, ks) ** 2 - E2 * I16).applyfunc(sp.expand) == sp.zeros(N)
    tr0 = sp.expand(G_of(m, ks).trace()) == 0 and sp.expand(G_of(-m, ks).trace()) == 0
    check("Q.one_particle_maps", ok1 and ok2 and sq1 and sq2 and tr0,
          "flat 4+4 one-particle generator G_m(k) = B (m C - i k_j C gamma^j) (i d_4 Psi = G Psi, k in x1..x3, x5..x8): Gamma G_m(k) Gamma = G_(-m)(k) and gamma^(x8) G_m(k) gamma^(x8) = G_(-m)(R_8 k) (similarities, so equal spectra); G_(+-m)(k)^2 = (%s) I16 and tr G = 0: both universes have the eigenvalues +-sqrt(%s), each 8-fold (the extra-time momenta k5, k6, k7 enter with the opposite sign)" % (E2, E2))
    # Krein inertia of B on each eigenspace at an exact sample point with E = 3
    sub = {m: 1, ks[0]: 2, ks[1]: 0, ks[2]: 0, ks[3]: 0, ks[4]: 0, ks[5]: 0, ks[6]: 2}
    Gs = G_of(m, ks).subs(sub)
    res, good = [], True
    for ev in (3, -3):
        Pr = ((Gs + ev * I16) / (2 * ev))           # projector onto the eigenspace G = ev
        V = sp.Matrix.hstack(*Pr.columnspace())
        ok_ev = (Gs * V - ev * V).applyfunc(sp.simplify) == sp.zeros(N, V.cols)
        K = (V.H * B * V).applyfunc(sp.simplify)
        evs = K.eigenvals()
        pos = sum(v for e, v in evs.items() if sp.N(e) > 0)
        neg = sum(v for e, v in evs.items() if sp.N(e) < 0)
        res.append("w = %s: dim %d, Krein inertia (%d,%d)" % (ev, V.cols, pos, neg))
        good = good and ok_ev and V.cols == 8 and (pos, neg) == (4, 4)
    check("Q.one_particle_Krein_inertia", good,
          "at the exact sample m = 1, k1 = 2, k8 = 2, other k = 0 (E = 3): " + "; ".join(res) + " - every energy eigenspace of the canonically quantised field is Krein-indefinite (B restricted to it has inertia (4,4))")
    check("Q.T2_image_keeps_B", G8 * B * G8.H == B,
          "gamma^(x8) B gamma^(x8)^dagger = +B: the T2 (mirror) image keeps the canonical anticommutator +B/sqrt|g|, it is an ordinary independently quantisable copy with equal energies (unlike the T1 image, which carries -B)")

NOT_ESTABLISHED = [
    "No creation process: nothing in these equations produces a universe, a pair of universes or a change of the number of universes; no transition between 'no universe' and 'two universes' is described.",
    "No rate, probability or amplitude for creating a pair is derived; no wave function of the universe, path integral or tunnelling computation is part of these theorems.",
    "No conservation law forces pairing: the theorems are symmetries (maps between solutions); a single universe with mass +m is an equally valid solution of the field equations without its partner.",
    "The vanishing total energy-momentum and charge of a pair (T1) is an identity for a field configuration and its image (classical bilinears, or one operator and its image); it is not a cancellation between two independently quantised universes (Q.no_cancellation_independent_universes).",
    "T2 does not reverse the sign of the energy-momentum tensor: the mirror universe of mass -m has the pulled-back T of the original, not -T.",
    "The Z2 brane at z = pi/2 and the mirror construction are ASSUMED (a boundary/orbifold choice), not derived from the field equations.",
    "The gravitational back-reaction (the a4 equations of SPEC section 5) is not part of the pairing theorems; T1 maps T -> -T, so a pair sourcing ONE common geometry would have zero total source, which is a statement about sources, not a derivation that such a geometry is created.",
    "No dynamical necessity: nothing forces the partner configuration to exist; the theorems are correspondences between solutions of two parameter sets, not a mechanism.",
    "T1 pairs (m, lambda) with (-m, -lambda): for lambda != 0 it is not a pure +m / -m pairing; the pure pairing (m, lambda) -> (-m, lambda) is T2, at EQUAL (not opposite) energy-momentum.",
    "Quantum positivity: in flat 4+4 space every energy eigenspace of the one-particle generator has Krein inertia (4,4) (Q.one_particle_Krein_inertia); a positive-norm Fock space for either universe is not established by these theorems.",
    "The brane z = pi/2 is a degenerate surface of the metric (g_88 = cot^2 z = 0, sqrt|g| = cos z = 0 there, geometry.brane_degenerate); no junction condition, brane tension or matching of the field across it is derived.",
    "The Kohn-Sham level (T3) is not covered by this checker (owned by Revision/pairing/kohn_sham/).",
]


def compare_with_theory():
    """Entry-by-entry comparison with the Wolfram theory record (read only, at the very end)."""
    if not THEORY.exists():
        CHECKS.append({"name": "compare.pairing_theory_json", "verdict": "pending",
                       "detail": "Revision/pairing/pairing-theory.json does not exist yet; re-run this checker after the Wolfram side has written it"})
        return
    th = json.loads(THEORY.read_text(encoding="utf-8"))
    check("compare.theory.status", "all checks" in th.get("status", "") and "passed" in th.get("status", ""),
          "the Wolfram theory record states: %s" % th.get("status"))
    data = th["data"]
    # 1. reflection table
    rows_ok, notes = True, []
    for row in data["reflections"]:
        n = COORDS.index(row["direction"])
        Pn = CHI * GAM[n]
        prod = I16
        for a in [7, 0, 1, 2, 3, 4, 5, 6]:          # Gamma's product order x8, x1, ..., x7
            if a != n:
                prod = prod * GAM[a]
        sgn = 1 if Pn == prod else (-1 if Pn == -prod else 0)
        char = 1 if Pn.H * C * Pn == C else (-1 if Pn.H * C * Pn == -C else 0)
        sS = 1 if GAM[n].H * C * GAM[n] == C else -1
        Ln = [(-1 if a == n else 1) for a in range(8)]
        kin = 1 if all(GAM[n].H * C * GAM[a] * GAM[n] == Ln[a] * C * GAM[a] for a in range(8)) else -1
        mine = (ETA[n], sgn, char, sS, kin)
        theirs = (row["eta_nn"], row["P_n_equals_sign_times_product_of_other_seven"], row["character_of_P_n"],
                  row["S_sign_under_gamma_n"], row["kinetic_sign_under_gamma_n_with_frame_reflection"])
        mp = "(m, lambda) -> (-m, lambda), L -> +L" if (sS, kin) == (-1, 1) else "(m, lambda) -> (-m, -lambda), L -> -L"
        same = mine == theirs and row["mass_coupling_map"].startswith(mp)
        rows_ok = rows_ok and same
        notes.append("%s %s%s" % (row["direction"], mine, "" if same else " != Wolfram %s" % (theirs,)))
    check("compare.theory.reflection_table", rows_ok,
          "(eta_nn, sign of P_n = Gamma gamma^n against the product of the other seven gammas in Gamma's order, character chi of P_n^dagger C P_n = chi C, S sign under gamma^n, kinetic sign) recomputed here for every direction and equal to the Wolfram record: " + "; ".join(notes))
    # 2. Krein signs M B M^dagger = s B
    ks_ok, notes = True, []
    for row in data["Krein_signs_M_B_Mdagger"]:
        nm = row["map"]
        if nm == "Gamma":
            M = CHI
        elif nm.startswith("gamma^"):
            M = GAM[COORDS.index(nm[6:])]
        else:
            M = CHI * GAM[COORDS.index(nm[2:])]
        sg = 1 if M * B * M.H == B else (-1 if M * B * M.H == -B else 0)
        ks_ok = ks_ok and sg == row["sign"]
        notes.append("%s: %+d" % (nm, sg))
    check("compare.theory.krein_signs", ks_ok,
          "M B M^dagger = s B recomputed here, equal to the Wolfram record: " + ", ".join(notes))
    # 3. one-particle Hamiltonian and samples
    op = data["one_particle_flat"]
    kk = sp.symbols("q1:9", real=True)
    h_theirs = -sp.I * m * GAM[3] - GAM[3] * sum((kk[a] * GAM[a] for a in range(8) if a != 3), sp.zeros(N))
    h_mine = B * (m * C - sum((sp.I * kk[a] * C * GAM[a] for a in range(8) if a != 3), sp.zeros(N)))
    same_h = (h_theirs - h_mine).applyfunc(sp.expand) == sp.zeros(N)
    E2 = m ** 2 + kk[0] ** 2 + kk[1] ** 2 + kk[2] ** 2 + kk[7] ** 2 - kk[4] ** 2 - kk[5] ** 2 - kk[6] ** 2
    same_sq = (h_mine ** 2 - E2 * I16).applyfunc(sp.expand) == sp.zeros(N)
    smp_ok, notes = True, []
    for smp in op["samples"]:
        sub = {m: smp["m"]}
        sub.update({kk[a]: smp["k"][a] for a in range(8)})
        Hs = h_mine.subs(sub)
        w = sp.sqrt(E2.subs(sub))
        res = []
        for ev in (w, -w):
            V = sp.Matrix.hstack(*((Hs + ev * I16) / (2 * ev)).applyfunc(sp.radsimp).columnspace())
            K = (V.H * B * V).applyfunc(sp.simplify)
            evs = K.eigenvals()
            res.append((V.cols, (sum(v for e, v in evs.items() if sp.N(e) > 0),
                                 sum(v for e, v in evs.items() if sp.N(e) < 0))))
        theirs = ((smp["dim_plus_w"], tuple(smp["B_inertia_plus_w"])), (smp["dim_minus_w"], tuple(smp["B_inertia_minus_w"])))
        wt = sp.sympify(smp["w"].replace("Sqrt[", "sqrt(").replace("]", ")"))
        ok = tuple(res) == theirs and sp.simplify(wt - w) == 0 and smp["k"][3] == 0
        smp_ok = smp_ok and ok
        notes.append("m=%s k=%s: w=%s %s" % (smp["m"], smp["k"], w, "agrees" if ok else "DIFFERS (%s)" % (res,)))
    check("compare.theory.one_particle", same_h and same_sq and smp_ok,
          "the Wolfram h_m(k) = -i m gamma^(x4) - gamma^(x4) sum k_a gamma^a equals the generator B (m C - i k_a C gamma^a) derived here from L (%s); h^2 = (%s) I16 (%s); samples (eigenvalue w, eigenspace dimensions, Krein inertia of B on each): %s"
          % (same_h, E2, same_sq, "; ".join(notes)))
    # 4. the theorems -> the checks of this file that establish them independently
    by = {c["name"]: c["verdict"] for c in CHECKS}
    support = {
        "T1": ["T1.general_field.matrix_identities", "T1.general_field.random_instance.commuting",
               "T1.general_field.random_instance.grassmann", "T1.diagonal8.commuting", "T1.diagonal8.grassmann",
               "T1.metric.commuting.lagrangian", "T1.metric.grassmann.lagrangian",
               "T1.metric.commuting.euler_lagrange_map", "T1.metric.grassmann.euler_lagrange_map",
               "T1.metric.commuting.emt", "T1.metric.grassmann.emt", "T1.metric.commuting.pair_total_emt_zero",
               "T1.metric.grassmann.pair_total_emt_zero", "T1.metric.commuting.current", "T1.metric.grassmann.current",
               "T1.metric.commuting.general_potential", "T1.metric.grassmann.general_potential"],
        "T2": ["T2.general_field.matrix_identities", "T2.general_field.reflection_table",
               "T2.diagonal8.frame_reflections.commuting", "T2.diagonal8.frame_reflections.grassmann",
               "geometry.mirror_isometry", "T2.metric.commuting.reflection_table", "T2.metric.grassmann.reflection_table",
               "T2.metric.commuting.euler_lagrange_map", "T2.metric.grassmann.euler_lagrange_map",
               "T2.metric.commuting.emt", "T2.metric.grassmann.emt", "T2.metric.commuting.current", "T2.metric.grassmann.current"],
        "Q": ["Q.canonical_anticommutator", "Q.image_krein_metric", "Q.image_own_quantisation",
              "Q.image_generators_same_dynamics", "Q.no_cancellation_independent_universes", "Q.one_particle_maps",
              "Q.one_particle_Krein_inertia", "Q.T2_image_keeps_B"],
    }
    for t in th["theorems"]:
        names = support.get(t["id"], [])
        ok = bool(names) and all(by.get(nm) == "PASS" for nm in names)
        check("compare.theory.theorem_%s" % t["id"], ok,
              "Wolfram theorem %s (%s; %d statements, %d Wolfram verifications) is independently confirmed by %d sympy checks of this file, all PASS: %s"
              % (t["id"], t["name"], len(t["statement"]), len(t["verification"]), len(names), ", ".join(names)))
    # 5. the not-established lists
    theirs = th.get("not_established", [])
    topics = [("creation process", "process"), ("rate / amplitude", "amplitude"), ("no necessity", "forces"),
              ("independent universes do not cancel", "independently quantised"), ("Z2 brane assumed", "assumed"),
              ("back-reaction", "back-reaction"), ("Krein positivity", "krein"),
              ("T1 not a pure +-m pairing for lambda != 0", "pure"), ("degenerate brane", "degenerate"),
              ("T3 not covered", "kohn-sham")]
    rows, good = [], True
    for label, tok in topics:
        a_ = any(tok in x.lower() for x in theirs)
        b_ = any(tok in x.lower() for x in NOT_ESTABLISHED)
        rows.append("%s: Wolfram %s, sympy %s" % (label, "yes" if a_ else "no", "yes" if b_ else "no"))
        good = good and a_ and b_
    check("compare.theory.not_established", good,
          "the two independently written lists of what the theorems do NOT establish cover the same topics: " + "; ".join(rows))


def main():
    t0 = time.time()
    algebra_checks()
    patch = Geometry(1)
    mirror = Geometry(-1)
    print("geometry %.1fs" % (time.time() - t0), flush=True)
    geometry_checks(patch)
    general_field_matrix_checks()
    random_instance_general_field()
    print("general field %.1fs" % (time.time() - t0), flush=True)
    for odd in (False, True):
        t1_metric(patch, odd)
        print("T1 %s %.1fs" % (stat_name(odd), time.time() - t0), flush=True)
    for odd in (False, True):
        t2_metric(patch, mirror, odd)
        print("T2 %s %.1fs" % (stat_name(odd), time.time() - t0), flush=True)
    for odd in (False, True):
        general_potential(patch, odd)
    print("general potential %.1fs" % (time.time() - t0), flush=True)
    for odd in (False, True):
        diagonal8_checks(odd)
        print("diagonal8 %s %.1fs" % (stat_name(odd), time.time() - t0), flush=True)
    quantum_checks(patch)
    quantum_one_particle_checks()
    compare_with_theory()
    n_fail = sum(1 for c in CHECKS if c["verdict"] == "FAIL")
    n_pass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
    report = {
        "producer": "Revision/pairing/python/check_pairing.py",
        "spec": "Revision/SPEC.md section 9 (pairing of universes of masses {+m, -m}, both fields)",
        "independence": "sympy only; gammas re-built from the author's tau formulas; no code shared with Revision/pairing/wolfram",
        "conventions": {
            "coordinates": "x1..x3 3-space, x4 time, x5..x7 the exponentially deflating extra times, x8 hidden (z = 6 H x8)",
            "lagrangian": "L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m S - (lambda/2) S^2 ], Psibar = Psi^dagger C, S = Psibar Psi",
            "emt": "T_mu nu = (1/4)[Psibar gamma_mu D_nu Psi + Psibar gamma_nu D_mu Psi - (D_mu Psibar) gamma_nu Psi - (D_nu Psibar) gamma_mu Psi] - g_mu nu L/sqrt|g|",
            "current": "J^mu = i Psibar gamma^mu Psi",
            "mirror": "R: z -> pi - z (x8 -> pi/(6H) - x8), Z2 brane at z = pi/2 (ASSUMED boundary construction); positive frame e^(x8)_(x8) = |cot z| on both sides; Lambda = diag(1,1,1,1,1,1,1,-1)",
            "statistics": "commuting jets = dirac16complex00 (classical); Grassmann jets = dirac16complex (anticommuting, the same identities hold as operator identities before normal ordering)",
        },
        "theorems_verified": {
            "T1": "L_{m,lambda}[Gamma Psi] = -L_{-m,-lambda}[Psi]; E_{m,lambda}[Gamma Psi] = -Gamma E_{-m,-lambda}[Psi]; T[Gamma Psi; m, lambda] = -T[Psi; -m, -lambda]; J[Gamma Psi] = -J[Psi]; for the pair (Psi, m, lambda) and (Gamma Psi, -m, -lambda): T + T = 0 and J + J = 0 identically; both statistics; the metric of SPEC section 1 and any gravitational field",
            "T2": "with P = gamma^(x8) = Gamma (Gamma gamma^(x8)) and the mirror z -> pi - z: L_{m,lambda}[P Psi(Rx)](x) = +L_{-m,lambda}[Psi](Rx); EL map; T pulled back (no sign change); J pulled back; S -> -S; both statistics",
            "quantum": "{Psi, Psi^dagger} = B/sqrt|g|; the image Gamma Psi carries -B; its own generators (-h) reproduce the same dynamics; no operator cancellation between two independently quantised universes",
        },
        "not_established": NOT_ESTABLISHED,
        "counts": {"pass": n_pass, "fail": n_fail,
                   "pending": sum(1 for c in CHECKS if c["verdict"] == "pending")},
        "checks": CHECKS,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_bytes((json.dumps(report, indent=2, ensure_ascii=True) + "\n").encode("utf-8"))
    print("pass %d fail %d; %.1fs; wrote %s" % (n_pass, n_fail, time.time() - t0, REPORT), flush=True)
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
