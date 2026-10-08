#!/usr/bin/env python3
"""Revision/theory/fock_quartic/check_fock_quartic.py

dirac16complex with U = (lam/2) S^2 (lam != 0) in a finite fermionic Fock space: is the operator form of the
on-shell identity sum_mu <:K_mu:> = <:(m + U'(S)) S:> (and of rho = m S + U, p = S U' - U) true, and in which sense?

Construction (exact; Gaussian rationals, the parameters m and lam kept as symbols where stated):
* the author's T16 gammas from Revision/algebra/gammas.json, C, B = -i C gamma^(x4), beta = B C = -i gamma^(x4);
* ONE good-sector plane-wave mode set with frozen coefficients (flat frame, V = 1): Psi(x) = e^{i k.x} psi(x4),
  psi = U a, U unitary with the 16 orthonormal eigenvectors of h_k = m beta + sum_a k_a alpha^a as columns
  (8 with energy +E, 8 with -E), a_j = b_j (j < 8), a_j = d_(j-8)^dagger (j >= 8): the positive realisation of the
  record, Psi^dagger = chi B, chi the Hilbert adjoint, {psi_A, Psi^dagger_C} = B_AC (the canonical relation, delta
  replaced by its projection 1/V onto the mode set, V = 1);
* the CAR algebra of the 16 modes b, d in the normal-ordered monomial basis (faithful on the 2^16-dimensional
  positive Fock space): an operator is zero iff it vanishes on every state;
* mode sets: M0 = rest frame k = 0 with symbolic m > 0 (homogeneous: S, K_mu x-independent, K_(a != x4) = 0);
  M1 = m = 3, k = (4, 0, 0, 0) along x1, E = 5 (the record's Wolfram example Fock_space_good_sector_example).

Output: Revision/theory/fock_quartic/reports/fock-quartic.json (deterministic, LF)."""

import json
import os
import sys
from fractions import Fraction as Fr
from functools import lru_cache

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
REV = os.path.normpath(os.path.join(HERE, "..", ".."))
GAMMAS = os.path.join(REV, "algebra", "gammas.json")
REPORT = os.path.join(HERE, "reports", "fock-quartic.json")
NMODE = 16
CHECKS = []


def check(name, ok, detail, section):
    CHECKS.append({"name": name, "section": section, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS " if ok else "FAIL ") + name, flush=True)


# ====================================================================================== exact CAR algebra
class Q:
    """Gaussian rational r + i im (Fraction parts)."""
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r = r if isinstance(r, Fr) else Fr(r)
        self.i = i if isinstance(i, Fr) else Fr(i)

    def __add__(a, b):
        return Q(a.r + b.r, a.i + b.i)

    def __sub__(a, b):
        return Q(a.r - b.r, a.i - b.i)

    def __mul__(a, b):
        if isinstance(b, int):
            return Q(a.r * b, a.i * b)
        return Q(a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r)

    __rmul__ = __mul__

    def __neg__(a):
        return Q(-a.r, -a.i)

    def conj(a):
        return Q(a.r, -a.i)

    def __bool__(a):
        return a.r != 0 or a.i != 0

    def __eq__(a, b):
        return a.r == b.r and a.i == b.i

    def sym(a):
        return sp.Rational(a.r.numerator, a.r.denominator) + sp.I * sp.Rational(a.i.numerator, a.i.denominator)


ONE, IU, HALF = Q(1), Q(0, 1), Q(Fr(1, 2))
P0, PM, PL = (0, 0), (1, 0), (0, 1)  # exponents of (m, lam)


def sort_sign(t):
    if len(set(t)) < len(t):
        return None
    lst, s = list(t), 1
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                s = -s
    return s, tuple(lst)


@lru_cache(maxsize=None)
def order_ac(a, c):
    """f_a1 .. f_ap f^+_c1 .. f^+_cq normal ordered with {f_i, f^+_j} = delta_ij: {(cre, ann): int}."""
    if not a or not c:
        return {(c, a): 1}
    x, ap, q = a[-1], a[:-1], len(c)
    out = {}
    for k, ck in enumerate(c):
        if ck == x:
            for key, s in order_ac(ap, c[:k] + c[k + 1:]).items():
                out[key] = out.get(key, 0) + s * (-1) ** k
    for (cc, aa), s in order_ac(ap, c).items():
        key = (cc, aa + (x,))
        out[key] = out.get(key, 0) + s * (-1) ** q
    return {k: v for k, v in out.items() if v}


@lru_cache(maxsize=None)
def mono_mul(c1, a1, c2, a2):
    """operator product of two normal-ordered monomials (all contractions)."""
    out = {}
    for (cc, aa), s in order_ac(a1, c2).items():
        sc, sa = sort_sign(c1 + cc), sort_sign(aa + a2)
        if sc is None or sa is None:
            continue
        key = (sc[1], sa[1])
        out[key] = out.get(key, 0) + s * sc[0] * sa[0]
    return tuple((k, v) for k, v in out.items() if v)


@lru_cache(maxsize=None)
def mono_wick(c1, a1, c2, a2):
    """Wick (normal-ordered) product: the same juxtaposition with NO contractions."""
    sc, sa = sort_sign(c1 + c2), sort_sign(a1 + a2)
    if sc is None or sa is None:
        return ()
    return (((sc[1], sa[1]), sc[0] * sa[0] * (-1) ** (len(a1) * len(c2))),)


class Op:
    """sum coef m^em lam^el f^+_cre f_ann; keys ((em, el), cre, ann), cre and ann ascending."""
    __slots__ = ("t",)

    def __init__(self, t=None):
        self.t = {k: v for k, v in (t or {}).items() if v}

    def __add__(A, B):
        t = dict(A.t)
        for k, v in B.t.items():
            t[k] = t[k] + v if k in t else v
        return Op(t)

    def __neg__(A):
        return Op({k: -v for k, v in A.t.items()})

    def __sub__(A, B):
        return A + (-B)

    def scale(A, z, pe=P0):
        z = Q(z) if isinstance(z, int) else z
        return Op({((k[0][0] + pe[0], k[0][1] + pe[1]), k[1], k[2]): v * z for k, v in A.t.items()})

    def _prod(A, B, rule):
        t = {}
        for (p1, c1, a1), v1 in A.t.items():
            for (p2, c2, a2), v2 in B.t.items():
                pe, v = (p1[0] + p2[0], p1[1] + p2[1]), v1 * v2
                for (c, a), s in rule(c1, a1, c2, a2):
                    k, w = (pe, c, a), v * s
                    t[k] = t[k] + w if k in t else w
        return Op(t)

    def __mul__(A, B):
        return A._prod(B, mono_mul)

    def wick(A, B):
        return A._prod(B, mono_wick)

    def adj(A):  # m, lam real
        t = {}
        for (pe, c, a), v in A.t.items():
            p, q = len(c), len(a)
            t[(pe, a, c)] = v.conj() * ((-1) ** (p * (p - 1) // 2 + q * (q - 1) // 2))
        return Op(t)

    def vev(A):
        return Op({k: v for k, v in A.t.items() if not k[1] and not k[2]})

    def novac(A):
        return Op({k: v for k, v in A.t.items() if k[1] or k[2]})

    def zero(A):
        return not A.t

    def degrees(A):
        return sorted({len(c) + len(a) for (_, c, a) in A.t})

    def lam_powers(A):
        return sorted({pe[1] for (pe, _, _) in A.t})


def comm(A, B):
    return A * B - B * A


def acomm(A, B):
    return A * B + B * A


def mode_name(j):
    return f"b{j}" if j < 8 else f"d{j - 8}"


def op_str(A):
    if A.zero():
        return "0"
    terms = []
    for (pe, c, a), v in sorted(A.t.items(), key=lambda kv: (kv[0][1], kv[0][2], kv[0][0])):
        coef = v.sym() * sp.Symbol("m") ** pe[0] * sp.Symbol("lam") ** pe[1]
        mon = " ".join([mode_name(j) + "^+" for j in c] + [mode_name(j) for j in a])
        terms.append(f"({sp.sstr(coef)})" + (f" {mon}" if mon else ""))
    return " + ".join(terms)


def apply_mono(c, a, state):
    out = {}
    for s, z in state.items():
        sign, ok = 1, True
        for j in reversed(a):
            if not (s >> j) & 1:
                ok = False
                break
            sign *= (-1) ** bin(s & ((1 << j) - 1)).count("1")
            s ^= 1 << j
        if ok:
            for j in reversed(c):
                if (s >> j) & 1:
                    ok = False
                    break
                sign *= (-1) ** bin(s & ((1 << j) - 1)).count("1")
                s ^= 1 << j
        if ok:
            out[s] = out.get(s, Q()) + z * sign
    return {k: v for k, v in out.items() if v}


def apply_op(A, state):  # parameters must be absent
    out = {}
    for (pe, c, a), v in A.t.items():
        assert pe == P0
        for s, z in apply_mono(c, a, state).items():
            out[s] = out.get(s, Q()) + z * v
    return {k: v for k, v in out.items() if v}


def expect(A, state):
    """<state|A|state>/<state|state> as a sympy expression in m, lam."""
    norm = sum((z.conj() * z for z in state.values()), Q())
    tot = sp.Integer(0)
    for (pe, c, a), v in A.t.items():
        amp = Q()
        for s, z in apply_mono(c, a, state).items():
            if s in state:
                amp = amp + state[s].conj() * z
        if amp:
            tot += (v * amp).sym() * sp.Symbol("m") ** pe[0] * sp.Symbol("lam") ** pe[1]
    return sp.simplify(tot / norm.sym())


def occ(*modes):
    s = 0
    for j in modes:
        s |= 1 << j
    return s


# fields in the mode basis: a_j = b_j (j < 8), a_j = d_(j-8)^+ (j >= 8)
A_ = [Op({(P0, (), (j,)): ONE}) if j < 8 else Op({(P0, (j,), ()): ONE}) for j in range(NMODE)]
AD = [x.adj() for x in A_]


# ====================================================================================== gammas and mode sets
def load_gammas():
    with open(GAMMAS, encoding="utf-8") as fh:
        d = json.load(fh)

    def num(x):
        return sp.Rational(x) if isinstance(x, str) else sp.Integer(x)

    def mat(r):
        if isinstance(r, dict):
            return mat(r["re"]) + sp.I * mat(r["im"])
        return sp.Matrix([[num(x) for x in row] for row in r])

    return [mat(g) for g in d["gamma"]], mat(d["C"]), mat(d["B"]), list(d["eta"])


G, CM, BM, ETA = load_gammas()
I16 = sp.eye(16)
X4 = 3
BETA = -sp.I * G[X4]
ALPHA = {a: -G[X4] * G[a] for a in range(8) if a != X4}


def toQ(x):
    re_, im_ = sp.expand(x).as_real_imag()
    assert re_.is_Rational and im_.is_Rational, x
    return Q(Fr(int(re_.p), int(re_.q)), Fr(int(im_.p), int(im_.q)))


class ModeSet:
    def __init__(self, label, m, k, msym):
        self.label, self.k, self.msym, self.mval = label, k, msym, m
        mm = sp.Symbol("m", positive=True) if msym else m
        self.h = mm * BETA + sum((kv * ALPHA[a] for a, kv in k.items()), sp.zeros(16, 16))
        self.E = sp.sqrt(mm ** 2 + sum(kv ** 2 for kv in k.values()))
        J = (self.h / self.E).applyfunc(sp.simplify)
        reps, seen = [], set()
        for A in range(16):  # one representative per pair {A, pi(A)} of the signed permutation beta
            if A not in seen:
                partner = [i for i in range(16) if BETA[i, A] != 0][0]
                seen |= {A, partner}
                reps.append(A)
        cols = []
        for sgn in (1, -1):
            for A in reps:
                e = sp.zeros(16, 1)
                e[A] = 1
                cols.append(((I16 + sgn * J) * (I16 + sgn * BETA) * e).applyfunc(sp.expand))
        self.V = sp.Matrix.hstack(*cols)
        gram = (self.V.H * self.V).applyfunc(sp.expand)
        self.nsq = gram[0, 0]
        self.unitary = (len(reps) == 8 and gram == self.nsq * I16
                        and (self.V * self.V.H).applyfunc(sp.expand) == self.nsq * I16)
        self.energies = [self.E] * 8 + [-self.E] * 8
        self.diag = self.Nt(self.h) == sp.diag(*self.energies)

    def Nt(self, M):  # U^dagger M U with U = V / sqrt(nsq): rational, no square roots
        return (self.V.H * M * self.V / self.nsq).applyfunc(sp.simplify)

    def bil(self, M, wick=False, mfactor=False):
        """chi M psi = sum_ij (U^+ M U)_ij a_i^+ a_j (operator product, or Wick product if wick)."""
        Nt = self.Nt(M)
        out = Op()
        for i in range(16):
            for j in range(16):
                x = Nt[i, j]
                if x == 0:
                    continue
                pe = P0
                if mfactor:  # x = m * rational
                    x = sp.simplify(x / sp.Symbol("m", positive=True))
                    pe = PM
                out = out + (AD[i].wick(A_[j]) if wick else AD[i] * A_[j]).scale(toQ(x), pe)
        return out


# ====================================================================================== the computation
def section_setup():
    sec = "A. construction"
    ok = (BM == -sp.I * CM * G[X4] and BM * BM == I16 and BM.H == BM and CM * G[X4] * CM == G[X4]
          and BM * CM == BETA and BETA.H == BETA and BETA * BETA == I16 and ETA[X4] == -1
          and all((G[a] * G[b] + G[b] * G[a]) == 2 * (ETA[a] if a == b else 0) * I16 for a in range(8) for b in range(8)))
    check("fixture_B_C_beta", ok,
          "Revision/algebra/gammas.json: {gamma^a, gamma^b} = 2 eta^ab, B = -i C gamma^(x4), B^dagger = B, B^2 = 1, "
          "C gamma^(x4) C = gamma^(x4), B C = beta = -i gamma^(x4) Hermitian with beta^2 = 1; hence Psibar = Psi^dagger C "
          "= chi B C = chi beta, S = Psibar Psi = chi beta psi, Psibar gamma^(x4) = i chi", sec)
    # engine self-test: CAR relations, product vs Jordan-Wigner action on states, associativity, adjoint
    F = [Op({(P0, (), (j,)): ONE}) for j in range(NMODE)]
    FD = [x.adj() for x in F]
    ok_car = all((acomm(F[i], FD[j]) - (Op({(P0, (), ()): ONE}) if i == j else Op())).zero()
                 and acomm(F[i], F[j]).zero() for i in range(NMODE) for j in range(NMODE))
    X = (FD[0] * F[9] + FD[9] * FD[3].scale(Q(2, 1)) + F[3] * F[0] + FD[5]) * (FD[9] * F[0] + F[3].scale(IU))
    Y = FD[3] * F[9] + FD[0]
    states = [{occ(): ONE}, {occ(0, 3): ONE, occ(9): Q(1, -2)}, {occ(0, 5, 9): ONE, occ(3): Q(Fr(1, 3))}]
    ok_jw = True
    for st in states:
        lhs = apply_op(X * Y, st)
        rhs = apply_op((FD[0] * F[9] + FD[9] * FD[3].scale(Q(2, 1)) + F[3] * F[0] + FD[5]),
                       apply_op(FD[9] * F[0] + F[3].scale(IU), apply_op(Y, st)))
        ok_jw = ok_jw and lhs == rhs
    ok_assoc = ((X * Y) * X - X * (Y * X)).zero() and ((X * Y).adj() - Y.adj() * X.adj()).zero()
    check("car_engine_selftest", ok_car and ok_jw and ok_assoc,
          "own exact CAR engine (normal-ordered monomials f^+..f^+ f..f of 16 modes, Gaussian-rational coefficients, "
          "the parameters m and lam as exponents): {f_i, f_j^+} = delta_ij and {f_i, f_j} = 0 for all 16 x 16 pairs; "
          "products agree with the independent Jordan-Wigner action on occupation states; associativity and "
          "(XY)^+ = Y^+ X^+ on test elements. The normal-ordered basis is faithful on the 2^16-dimensional Fock "
          "space: an operator is zero iff it vanishes on every state", sec)
    M0 = ModeSet("M0", None, {}, True)
    M1 = ModeSet("M1", sp.Integer(3), {0: sp.Integer(4)}, False)
    for M, txt in ((M0, "M0: rest frame k = 0, symbolic m > 0, h = m beta, energies +-m"),
                   (M1, "M1: m = 3, k = (4, 0, 0, 0) along x1, h = 3 beta + 4 alpha^(x1), energies +-5 (the record's Wolfram example)")):
        okA = all(acomm(A_[i], AD[j]).t == ({(P0, (), ()): ONE} if i == j else {}) and acomm(A_[i], A_[j]).zero()
                  for i in range(NMODE) for j in range(NMODE))
        Bt = M.Nt(BM)  # U^+ B U; {psi_A, Psi^+_C} = (U U^+ B)_AC = B_AC since U U^+ = 1
        check(f"mode_set_{M.label}", M.unitary and M.diag and okA and (M.V * M.V.H / M.nsq) * BM == BM and Bt.H == Bt,
              f"{txt}: columns u_j = (1 + sgn h/E)(1 + sgn beta) e_A / sqrt(nsq), nsq = {sp.sstr(M.nsq)} (one A per pair of "
              "beta's signed permutation; sgn = + for 8 modes, - for 8): U^dagger U = U U^dagger = 1 exactly, U^dagger h U = "
              "diag(E x8, -E x8); with psi = U a, a_j = b_j (j < 8), d_(j-8)^+ (j >= 8): {a_i, a_j^+} = delta_ij, {a_i, a_j} = 0 "
              "(engine), hence {psi_A, chi_C} = delta_AC and {psi_A, Psi^dagger_C} = (U U^dagger B)_AC = B_AC with "
              "Psi^dagger = chi B: the canonical anticommutator of the record (delta^7 replaced by its projection on the "
              "mode set, V = 1). Only Gaussian-rational matrices U^dagger M U enter (no square roots)", sec)
        okg = M.Nt(BM * CM * G[X4]) == sp.I * I16
        check(f"psibar_gamma4_is_i_chi_{M.label}", okg,
              "U^dagger (B C gamma^(x4)) U = i 1 exactly, i.e. Psibar gamma^(x4) = i chi, so K_4 = (1/2)(Psibar gamma^(x4) "
              "d4 Psi - d4 Psibar gamma^(x4) Psi) = (i/2)(chi d4 psi - d4 chi psi) (computed below from the matrices, not "
              "from this simplification)", sec)
    return M0, M1


def build(M):
    """the operators of one mode set."""
    o = {}
    o["S"] = M.bil(BM * CM)                  # Psibar Psi (operator product of the fields)
    o["Sw"] = M.bil(BM * CM, wick=True)      # :S:
    o["Q"] = M.bil(I16)                      # Psi^+ B Psi = chi psi
    if M.msym:
        o["H0"] = o["S"].scale(1, PM)        # chi h psi = m S
        o["mS"] = o["H0"]
    else:
        o["H0"] = M.bil(M.h)
        o["mS"] = o["S"].scale(int(M.mval))
    o["H0n"] = o["H0"].novac()               # :chi h psi:
    o["spatial"] = Op()
    for a, kv in M.k.items():                # K_a = i k_a Psibar gamma^a psi (d_a -> i k_a on e^{ik.x})
        o["spatial"] = o["spatial"] + M.bil(BM * CM * G[a]).scale(Q(0, int(kv)))
    S, Sw = o["S"], o["Sw"]
    o["W"] = {
        "plain": S * S,                       # S.S, operator square of the un-normal-ordered S
        "nsq": Sw * Sw,                       # :S:.:S:, operator square of the normal-ordered S
        "wick": Sw.wick(Sw),                  # :S S:, Wick (normal) ordering of the classical S^2
    }
    Nb = M.Nt(BM * CM)
    nz = [(i, j, toQ(Nb[i, j])) for i in range(16) for j in range(16) if Nb[i, j] != 0]
    WF = Op()
    for (i, j, z1) in nz:                     # field ordering Psi^+ Psi^+ Psi Psi: beta_AB beta_CD chi_A chi_C psi_D psi_B
        for (kk, l, z2) in nz:
            WF = WF + (AD[i] * AD[kk] * A_[l] * A_[j]).scale(z1 * z2)
    o["W"]["field"] = WF
    o["G4m"] = M.Nt(G[X4])
    o["N4"] = M.Nt(BM * CM * G[X4])
    o["R1"] = o["mS"].novac() + Sw.wick(Sw).scale(1, PL)       # :(m + U') S: = m :S: + lam :S S:
    o["R2"] = o["mS"].novac() + (Sw * Sw).scale(1, PL)         # m :S: + lam :S:^2
    return o


def heisenberg(o, H):
    ad = [comm(H, A_[j]).scale(IU) for j in range(16)]           # d4 a_j = i [H, a_j]
    add = [comm(H, AD[j]).scale(IU) for j in range(16)]          # d4 a_j^+ = i [H, a_j^+]
    return ad, add


def kinetic(o, ad, add):
    """K_4 from the matrices: (1/2)(Psibar g4 d4psi - d4Psibar g4 psi); operator product and Wick product."""
    K4, K4w = Op(), Op()
    for i in range(16):
        for j in range(16):
            x = o["N4"][i, j]
            if x == 0:
                continue
            z = toQ(x) * HALF
            K4 = K4 + (AD[i] * ad[j] - add[i] * A_[j]).scale(z)
            K4w = K4w + (AD[i].wick(ad[j]) - add[i].wick(A_[j])).scale(z)
    return K4 + o["spatial"], K4w + o["spatial"].novac(), K4, K4w


ORDER_NAMES = {"plain": "U = (lam/2) S.S (operator square of S = Psibar Psi, the classical expression with the field operators)",
               "nsq": "U = (lam/2) :S:.:S: (square of the normal-ordered density)",
               "wick": "U = (lam/2) :S S: (Wick/normal ordering of the classical S^2)",
               "field": "U = (lam/2) beta_AB beta_CD Psi^+_A Psi^+_C Psi_D Psi_B (all Psi^+ left of all Psi)"}


def analyse(M, o, results):
    sec = "C. lam != 0"
    lab = M.label
    S, Sw, Qc = o["S"], o["Sw"], o["Q"]
    SS = o["W"]["plain"]
    res = {"mode_set": lab, "orderings": {}}
    # ordering relations among the four U
    rel = {
        "field = S.S - Q": (o["W"]["field"] - (SS - Qc)).zero(),
        "nsq - wick (one-body + const)": op_str(o["W"]["nsq"] - o["W"]["wick"]),
        "plain - wick (one-body + const)": op_str(SS - o["W"]["wick"]),
    }
    res["ordering_relations"] = rel
    ok_rel = rel["field = S.S - Q"] and all(set((x - o["W"]["wick"]).degrees()) <= {0, 2} for x in (SS, o["W"]["nsq"], o["W"]["field"]))
    check(f"orderings_of_S2_{lab}", ok_rel,
          f"{lab}: the four operator orderings of S^2 differ by one-body operators and constants only: field-ordered "
          f"Psi^+Psi^+PsiPsi = S.S - Q exactly (Q = chi psi); :S:.:S: - :SS: = {rel['nsq - wick (one-body + const)']}; "
          f"S.S - :SS: = {rel['plain - wick (one-body + const)']}", sec)
    cands = {}
    G4 = o["G4m"]
    def cand(kind):
        out = []
        for l in range(16):
            if kind == "S psi":
                out.append(S * A_[l])
            elif kind == "psi S":
                out.append(A_[l] * S)
            elif kind == "(1/2){S, psi}":
                out.append((S * A_[l] + A_[l] * S).scale(HALF))
            elif kind == ":S psi: (Wick)":
                out.append(Sw.wick(A_[l]))
            elif kind == ":S: psi":
                out.append(Sw * A_[l])
            elif kind == "psi :S:":
                out.append(A_[l] * Sw)
            elif kind == "(1/2){:S:, psi}":
                out.append((Sw * A_[l] + A_[l] * Sw).scale(HALF))
        return out
    kinds = ["S psi", "psi S", "(1/2){S, psi}", ":S psi: (Wick)", ":S: psi", "psi :S:", "(1/2){:S:, psi}"]
    for kd in kinds:
        c = cand(kd)
        cands[kd] = []
        for j in range(16):
            acc = Op()
            for l in range(16):
                if G4[j, l] != 0:
                    acc = acc + c[l].scale(toQ(G4[j, l]))
            cands[kd].append(acc)
    # free part
    ad0, _ = heisenberg(o, o["H0n"])
    free_ok = all((ad0[j] - A_[j].scale(Q(0, -1) * toQ(M.energies[j] / (sp.Symbol("m", positive=True) if M.msym else 1)),
                                        PM if M.msym else P0)).zero() for j in range(16))
    res["free_heisenberg_equation"] = free_ok
    for wn, W in o["W"].items():
        H = o["H0n"] + W.scale(HALF, PL)
        ad, add = heisenberg(o, H)
        okadj = all((add[j] - ad[j].adj()).zero() for j in range(16)) and (H - H.adj()).zero()
        inter = [ad[j] - ad0[j] for j in range(16)]
        match = [kd for kd in kinds if all((inter[j] + cands[kd][j].scale(1, PL)).zero() for j in range(16))]
        SK, SKw, K4, K4w = kinetic(o, ad, add)
        D = H - o["H0n"] - SS.scale(HALF, PL)
        th = SK - (o["mS"] + SS.scale(1, PL) - Qc.scale(HALF, PL) + D)
        cmp = {}
        for nm, L in (("N1 vacuum-subtracted operator", SK.novac()), ("N2 Wick product", SKw)):
            for rn, R in (("R1 m:S: + lam:SS:", o["R1"]), ("R2 m:S: + lam:S:^2", o["R2"])):
                Dl = L - R
                cmp[f"{nm} | {rn}"] = {"zero": Dl.zero(), "difference": op_str(Dl), "_op": Dl}
        res["orderings"][wn] = {"U": ORDER_NAMES[wn], "H_selfadjoint_and_d4chi_is_adjoint": okadj,
                                "operator_field_equation_ordering": match,
                                "theorem_residual_constant": op_str(th), "theorem_holds": th.novac().zero(),
                                "comparisons": cmp, "_H": H, "_K4w": K4w, "_K4": K4, "_SK": SK, "_SKw": SKw}
    results[lab] = res
    return res


def strip(d):
    if isinstance(d, dict):
        return {k: strip(v) for k, v in d.items() if not k.startswith("_")}
    return d


def main():
    M0, M1 = section_setup()
    sp_m, sp_l = sp.Symbol("m"), sp.Symbol("lam")
    ops = {M.label: build(M) for M in (M0, M1)}
    # ------------------------------------------------------------------ B. control lam = 0 (the record)
    sec = "B. control lam = 0"
    o, M = ops["M1"], M1
    vac, b0, d0 = {occ(): ONE}, {occ(0): ONE}, {occ(8): ONE}
    Hv = expect(o["H0"], vac)
    eb, ed = expect(o["H0n"], b0), expect(o["H0n"], d0)
    qb, qd = expect(o["Q"].novac(), b0), expect(o["Q"].novac(), d0)
    dense = sp.Matrix(16, 16, lambda A, Bv: ((3 * (A + 1) + 5 * (Bv + 1)) % 7 - 3) if A <= Bv else ((3 * (Bv + 1) + 5 * (A + 1)) % 7 - 3))
    Ms = [CM, -sp.I * CM * G[X4], -sp.I * CM * G[0], CM * G[1] * G[2], dense]
    ok_rule = True
    for Mx in Ms:
        Nt = M.Nt(BM * Mx)
        X = M.bil(BM * Mx).novac()
        ok_rule = ok_rule and sp.simplify(expect(X, b0) - Nt[0, 0]) == 0 and sp.simplify(expect(X, d0) + Nt[8, 8]) == 0
    check("control_record_Fock_example", Hv == -40 and eb == 5 and ed == 5 and qb == 1 and qd == -1 and ok_rule,
          "reproduces Fock_space_good_sector_example (Wolfram) / good_sector_positive_fock_realisation (sympy) exactly on "
          "M1 (m = 3, k1 = 4, E = 5): vacuum value of chi h psi = -40 = -8E (the filled sea); normal-ordered energy +5 for "
          "b_0^+|0> AND for d_0^+|0>; charge :chi psi: = +1 and -1; expectation-value rule <:Psi^dagger M Psi:> = "
          "u^dagger B M u (particle) and -v^dagger B M v (antiparticle) for M = C, -i C gamma^(x4), -i C gamma^(x1), "
          "C gamma^(x2) gamma^(x3) and the record's dense integer matrix", sec)
    ok0, txt0 = True, []
    for M in (M0, M1):
        o = ops[M.label]
        ad, add = heisenberg(o, o["H0n"])
        okf = all((ad[j] - A_[j].scale(Q(0, -1) * toQ(M.energies[j] / (sp.Symbol("m", positive=True) if M.msym else 1)),
                                       PM if M.msym else P0)).zero() for j in range(16))
        SK, SKw, _, _ = kinetic(o, ad, add)
        okt = (SK - o["mS"]).zero() and (SK.novac() - o["mS"].novac()).zero() and (SKw - o["mS"].novac()).zero()
        ok0 = ok0 and okf and okt
        txt0.append(f"{M.label}: d4 a_j = i[:H0:, a_j] = -i e_j a_j (free field equation), sum_mu K_mu = m S exactly "
                    f"(including the constant), :sum K_mu: = m :S: (vacuum subtraction and Wick product agree)")
    check("control_trace_identity_lam0", ok0,
          "lam = 0 (the record's case): with H = :chi h psi: the Heisenberg field solves the free field equation and the "
          "kinetic-sum identity holds as an OPERATOR identity on the whole Fock space: " + "; ".join(txt0), sec)
    o = ops["M0"]
    rho0 = o["H0n"]  # k = 0, lam = 0: rho = m :S:
    ad, add = heisenberg(o, o["H0n"])
    _, SKw, _, K4w = kinetic(o, ad, add)
    check("control_homogeneous_lam0", o["spatial"].zero() and (rho0 - o["mS"].novac()).zero() and (K4w - rho0).zero(),
          "M0 (homogeneous), lam = 0: K_(a != x4) = 0, rho = :H: = m :S:, p = :K_4: - m :S: = 0 = S U' - U: operator identities", sec)
    # ------------------------------------------------------------------ C. lam != 0
    results = {}
    for M in (M0, M1):
        analyse(M, ops[M.label], results)
    sec = "C. lam != 0"
    expected = {"plain": ["(1/2){S, psi}"], "nsq": ["(1/2){:S:, psi}"], "wick": [":S psi: (Wick)"], "field": ["S psi"]}
    okH = all(results[l]["orderings"][w]["operator_field_equation_ordering"] == expected[w]
              and results[l]["orderings"][w]["H_selfadjoint_and_d4chi_is_adjoint"] and results[l]["free_heisenberg_equation"]
              for l in results for w in expected)
    check("heisenberg_field_equation_ordering", okH,
          "for H = :chi h psi: + U_W (W one of the four orderings; H self-adjoint, d4 chi = i[H, chi] = (d4 psi)^+), the "
          "Heisenberg field d4 psi = i[H, psi] satisfies EXACTLY ONE of seven tested orderings of the operator field "
          "equation d4 psi = -i h psi - lam gamma^(x4) O(S, psi) [i.e. gamma^mu d_mu Psi = m Psi + lam O(S, Psi)], on both "
          "mode sets: U = (lam/2) S.S -> O = (1/2){S, psi}; U = (lam/2):S:.:S: -> O = (1/2){:S:, psi}; U = (lam/2):SS: -> "
          "O = :S psi: (the Wick-ordered classical U'(S) Psi); field ordering -> O = S psi (candidates: S psi, psi S, "
          "(1/2){S,psi}, :S psi:, :S: psi, psi :S:, (1/2){:S:,psi})", sec)
    okT = all(results[l]["orderings"][w]["theorem_holds"] for l in results for w in expected)
    consts = "; ".join(f"{l}/{w}: {results[l]['orderings'][w]['theorem_residual_constant']}" for l in results for w in expected)
    check("kinetic_sum_operator_theorem", okT,
          "for every ordering W and both mode sets, with K_mu from the Heisenberg field (operator products, no ordering "
          "prescription): sum_mu K_mu = m S + lam S.S - (lam/2) Q + D_W + c_W 1 EXACTLY, where D_W = U_W - (lam/2) S.S is "
          "the one-body-plus-constant difference of the chosen potential from the operator square and c_W a c-number "
          f"(c_W = {consts}; '0' means none). So the plain operator sum_mu K_mu equals (m + U'(S)) S = m S + lam S.S only "
          "up to the one-body operator D_W - (lam/2) Q; for the field ordering D_W = -(lam/2) Q and sum K = m S + 2 U_W", sec)
    okW = all(results[l]["orderings"]["wick"]["comparisons"]["N2 Wick product | R1 m:S: + lam:SS:"]["zero"] for l in results)
    for M in (M0, M1):  # H_wick is the integrated normal-ordered energy density :(-sum_(a != 4) K_a + m S + U):
        o = ops[M.label]
        rho_op = (o["mS"] - o["spatial"]).novac() + o["Sw"].wick(o["Sw"]).scale(HALF, PL)
        okW = okW and (results[M.label]["orderings"]["wick"]["_H"] - rho_op).zero()
    check("trace_identity_operator_identity_wick", okW,
          "THE POSITIVE RESULT: with the Wick-ordered potential U = (lam/2):S S: in the Hamiltonian H = :chi h psi: + "
          "(lam/2) :S S: (which is the integrated normal-ordered energy density, V = 1) and with K_mu defined as the Wick "
          "(normal-ordered) product of Psibar and the Heisenberg derivative d4 Psi = i[H, Psi], "
          ":sum_mu K_mu: = :(m + U'(S)) S: = m :S: + lam :S S: holds EXACTLY as an operator identity on the whole Fock "
          "space (every state, both mode sets, symbolic lam; M0 also symbolic m); verified also: H = :(-sum_(a != x4) K_a + "
          "m S + U):, the generator of x4-translations is the integrated normal-ordered energy density. Stated on the "
          "slice x4 = 0 where the canonical relations and the normal ordering are defined (conjugation by e^{iH x4} "
          "transports it to other x4 with the normal ordering transported accordingly)", sec)
    fails, okF = [], True
    for l in results:
        for w in expected:
            for key, c in results[l]["orderings"][w]["comparisons"].items():
                if w == "wick" and key.startswith("N2") and "R1" in key:
                    continue
                Dl = c["_op"]
                good = (not c["zero"]) and set(Dl.degrees()) <= {0, 2} and Dl.lam_powers() == [1]
                okF = okF and good
                fails.append(f"{l}/{w}/{key.split()[0]}-{key.split('| ')[1].split()[0]}")
    check("trace_identity_fails_for_every_other_combination", okF and len(fails) == 30,
          f"all {len(fails)} other combinations (2 mode sets x 4 orderings x LHS {{N1 = Heisenberg operator minus its vacuum "
          "value, N2 = Wick product}} x RHS {R1 = m:S: + lam:SS:, R2 = m:S: + lam:S:^2}, minus the Wick/N2/R1 case) violate "
          "the identity by a NONZERO operator that is one-body (plus possibly a constant) and linear in lam; the exact "
          "differences are listed in results", sec)
    # expectation-value classes on M0: differences diagonal, same sign -> vanish only in the vacuum
    cls, okC = {}, True
    for w in expected:
        for key, c in results["M0"]["orderings"][w]["comparisons"].items():
            Dl = c["_op"]
            if c["zero"]:
                continue
            diag = all(cc == aa and len(cc) == 1 for (_, cc, aa) in Dl.t)
            coefs = sorted({(cc[0] >= 8, v.r) for (_, cc, aa), v in Dl.t.items()}) if diag else []
            bco = {v for (isd, v) in coefs if not isd}
            dco = {v for (isd, v) in coefs if isd}
            same = diag and len(bco) == 1 and len(dco) == 1 and all(x.i == 0 for x in Dl.t.values())
            if same:
                bb, dd = bco.pop(), dco.pop()
                same = bb != 0 and dd != 0 and (bb > 0) == (dd > 0)
                cls[f"{w}/{key.split()[0]}-{key.split('| ')[1].split()[0]}"] = f"lam*({bb}*N_b + {dd}*N_d)"
            okC = okC and same
    check("expectation_classes_M0", okC and len(cls) == 15,
          "M0 (homogeneous): every failing difference is lam (alpha N_b + beta N_d) with N_b = sum b^+b, N_d = sum d^+d and "
          "alpha, beta nonzero of the SAME sign, so <Delta> = 0 for lam != 0 only in the vacuum of the mode set (where both "
          "sides vanish): outside the Wick/N2 definition the identity does not even hold in expectation values for any "
          f"state with a quantum present; differences: {json.dumps(cls, sort_keys=True)}", sec)
    st = {"vacuum": {occ(): ONE}, "b0": {occ(0): ONE}, "d0": {occ(8): ONE}}
    m1tab, okM1 = {}, True
    for w in expected:
        for key, c in results["M1"]["orderings"][w]["comparisons"].items():
            if c["zero"]:
                continue
            ev = {n: sp.sstr(expect(c["_op"], s_)) for n, s_ in st.items()}
            m1tab[f"{w}/{key.split()[0]}-{key.split('| ')[1].split()[0]}"] = ev
            okM1 = okM1 and (ev["b0"] != "0" or ev["d0"] != "0")
    check("expectation_values_M1", okM1,
          "M1 (k1 = 4): every failing difference has a nonzero expectation value in b_0^+|0> or d_0^+|0> (it also contains "
          f"pair terms b^+ d^+, b d); expectation values (vacuum, b0, d0): {json.dumps(m1tab, sort_keys=True)}", sec)
    # ------------------------------------------------------------------ D. homogeneous rho, p (M0)
    sec = "D. homogeneous rho and p (M0, k = 0)"
    o = ops["M0"]
    rW = results["M0"]["orderings"]["wick"]
    H = rW["_H"]
    rho = H.novac()                                   # rho = -T^x4_x4 = :(- sum_(a != 4) K_a + m S + U): with K_a = 0
    SSw = o["Sw"].wick(o["Sw"])
    p_N2 = rW["_K4w"] - rho                           # p_mu = sum_(nu != mu) K_nu - m S - U = K_4 - (m S + U) at k = 0
    p_N1 = rW["_K4"].novac() - rho
    n_op = o["Sw"]
    ok_rho = o["spatial"].zero() and (rho - (o["mS"].novac() + SSw.scale(HALF, PL))).zero()
    ok_p = (p_N2 - SSw.scale(HALF, PL)).zero()
    ok_cons = comm(H, o["S"]).zero()
    ok_n = (SSw - (n_op * n_op - n_op)).zero()
    Nb_ = sum((AD[j] * A_[j] for j in range(8)), Op())
    Nd_ = sum((A_[j] * AD[j] for j in range(8, 16)), Op())
    ok_nbd = (n_op - (Nb_ + Nd_)).zero()
    ok_pN1 = (p_N1 - SSw.scale(HALF, PL) - (Nb_.scale(-8) + Nd_.scale(-7)).scale(1, PL)).zero()
    tests = {"vacuum": {occ(): ONE}, "b0": {occ(0): ONE}, "b0 d0": {occ(0, 8): ONE}, "b0 b1 d0": {occ(0, 1, 8): ONE},
             "(|0> + b0^+ d0^+|0>)/sqrt2": {occ(): ONE, occ(0, 8): ONE}}
    tab, ok_tab = {}, True
    for nme, s_ in tests.items():
        r_, p_, S_ = expect(rho, s_), expect(p_N2, s_), expect(n_op, s_)
        U_S2 = expect(SSw, s_)
        naive_p = sp.simplify(sp_l / 2 * S_ ** 2)
        tab[nme] = {"<:S:>": sp.sstr(S_), "<:SS:>": sp.sstr(U_S2), "rho": sp.sstr(r_), "p": sp.sstr(p_),
                    "rho - (m<:S:> + (lam/2)<:S:>^2)": sp.sstr(sp.simplify(r_ - sp_m * S_ - sp_l / 2 * S_ ** 2)),
                    "p - (lam/2)<:S:>^2": sp.sstr(sp.simplify(p_ - naive_p))}
    ok_tab = (tab["b0"]["p"] == "0" and tab["b0 d0"]["p"] == "lam" and tab["b0 b1 d0"]["p"] == "3*lam"
              and tab["b0"]["rho"] == "m" and tab["b0"]["p - (lam/2)<:S:>^2"] == "-lam/2")
    check("homogeneous_rho_p_operator_identities_wick", ok_rho and ok_p and ok_cons and ok_n and ok_nbd,
          "M0 (k = 0, the homogeneous sector), Wick ordering, K_mu as Wick products with the Heisenberg derivative: "
          "K_(a != x4) = 0 identically; rho = -T^x4_x4 = :H: = m :S: + (lam/2) :S S: = :m S + U(S): and p_mu = T^mu_mu = "
          ":K_4: - :m S + U: = (lam/2) :S S: = :S U'(S) - U(S): for every mu != x4 (p3 = p_t = p8): EXACT operator "
          "identities on the whole Fock space; [H, S] = 0 (S is conserved, the analogue of the classical S = S0); "
          ":S: = N_b + N_d =: n and :S S: = n^2 - n (operator identities)", sec)
    check("homogeneous_expectation_values_are_not_U_of_expectation", ok_tab,
          "M0, Wick: on occupation states with n quanta rho = m n + (lam/2) n(n - 1), p = (lam/2) n(n - 1), so "
          "<:U(S):> = (lam/2) n(n - 1) != U(<:S:>) = (lam/2) n^2 (one quantum: p = 0, w = 0, not lam/(2m + lam)); the "
          "classical formulas hold for the normal-ordered OPERATORS, not with S replaced by its expectation value: "
          f"{json.dumps(tab, sort_keys=True)}", sec)
    check("homogeneous_p_vacuum_subtraction_fails", ok_pN1,
          "M0, Wick potential but p defined from the Heisenberg K_4 by vacuum subtraction only (N1): p = (lam/2):S S: - "
          "lam (8 N_b + 7 N_d), i.e. p != S U' - U on every state with a quantum present; the extra term is the "
          "contraction of Psibar with the sea in Psibar gamma^(x4) d4 Psi (8 = the number of negative-energy modes of the "
          "mode set)", sec)
    # ------------------------------------------------------------------ E. negative control
    sec = "E. negative control"
    okN = True
    for l in ("M0", "M1"):
        o = ops[l]
        ad, add = heisenberg(o, o["H0n"])               # free dynamics, interacting right-hand side
        _, SKw, _, _ = kinetic(o, ad, add)
        Dl = SKw - o["R1"]
        okN = okN and (not Dl.zero()) and (Dl + o["Sw"].wick(o["Sw"]).scale(1, PL)).zero()
    check("negative_control_free_dynamics", okN,
          "if d4 Psi is NOT the solution of the interacting operator field equation (free Heisenberg dynamics H = :chi h "
          "psi:, while the right-hand side keeps U' = lam S), the checker finds :sum K: - :(m + U')S: = -lam :S S: != 0 on "
          "both mode sets: the identity is a statement about solutions of the operator field equation, not an algebraic "
          "identity for arbitrary d4 Psi", sec)
    # ------------------------------------------------------------------ report
    npass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
    rep = {
        "report": "Revision/theory/fock_quartic/reports/fock-quartic.json",
        "producer": "Revision/theory/fock_quartic/check_fock_quartic.py (sympy + own exact CAR engine, Gaussian rationals)",
        "spec": "Revision/SPEC.md sections 3, 4, 6, 7 (dirac16complex, V = m + lam S, U = (lam/2) S^2; normal-ordered "
                "energy-momentum tensor operator; homogeneous rho = m S + U, p = S U' - U)",
        "inputs": ["Revision/algebra/gammas.json"],
        "question": "lam != 0: does <:sum_mu K_mu:> = <:(m + U'(S)) S:> (and rho = m S + U, p = S U' - U) hold as an "
                    "operator identity, only on solutions of the operator field equation, or only in expectation values?",
        "construction": {
            "field": "Psi(x) = e^{i k.x} U a (V = 1), U unitary from the eigenvectors of h_k, a_j = b_j (j < 8), d_(j-8)^+ "
                     "(j >= 8); Psi^dagger = chi B (positive realisation of the record); {psi_A, Psi^dagger_C} = B_AC",
            "mode_sets": {"M0": "k = 0, symbolic m > 0 (homogeneous)", "M1": "m = 3, k = (4,0,0,0), E = 5"},
            "hamiltonian": "H = :chi h psi: + U_W (the x4-generator; for W = wick it equals the integrated normal-ordered "
                           "energy density)",
            "kinetic_terms": "K_4 = (1/2)(Psibar gamma^(x4) d4 Psi - d4 Psibar gamma^(x4) Psi) with d4 Psi = i[H, Psi], "
                             "K_a = i k_a Psibar gamma^a Psi (a != x4)",
            "lhs_definitions": {"N1": "the operator sum K_mu minus its vacuum value",
                                "N2": "Wick (normal-ordered) product of Psibar (resp. d4 Psibar) and the normal-ordered "
                                      "operator d4 Psi (resp. Psi): no contractions between the two factors"},
            "rhs_definitions": {"R1": ":(m + U'(S)) S: = m :S: + lam :S S: (Wick ordering of the classical expression)",
                                "R2": "m :S: + lam :S:^2"},
            "orderings": ORDER_NAMES,
        },
        "summary": {"checks": len(CHECKS), "pass": npass, "fail": len(CHECKS) - npass},
        "checks": CHECKS,
        "results": strip(results),
        "conclusion": {
            "proved_in_the_model": [
                "Wick ordering: with H = :chi h psi: + (lam/2):S S: the Heisenberg field obeys the Wick-ordered operator "
                "field equation gamma^mu d_mu Psi = :(m + lam S) Psi: exactly, and with K_mu defined as Wick products "
                ":sum_mu K_mu: = :(m + U'(S)) S: is an operator identity on the whole Fock space (all states; slice x4 = 0)",
                "homogeneous (k = 0): rho = :m S + U(S): and p3 = p_t = p8 = :S U' - U: = (lam/2):S S: as operator identities "
                "in the same (Wick) sense",
                "for every ordering: sum_mu K_mu = m S + lam S.S - (lam/2) Q + (U_W - (lam/2) S.S) + const (exact operator "
                "theorem with the plain operator products)"],
            "fails": [
                "the same identity with K_mu taken as the plain Heisenberg operator minus its vacuum value (N1), for every "
                "ordering of U: off by a nonzero one-body operator (k = 0, Wick U: -lam (8 N_b + 7 N_d))",
                "with U ordered as S.S, :S:.:S: or Psi^+Psi^+PsiPsi and K_mu as Wick products, and with the right-hand "
                "side m:S: + lam :S:^2: off by nonzero one-body operators; at k = 0 the expectation value vanishes only in "
                "the vacuum",
                "<:U(S):> = U(<:S:>): false (one quantum at k = 0: p = 0 versus lam/2)",
                "the identity for arbitrary d4 Psi (negative control): it needs the interacting operator field equation"],
            "scope": "one good-sector plane-wave mode set with frozen coefficients (flat frame, V = 1, 16 modes, 2^16 "
                     "states); not the field on a whole slice, not the curved x8 dependence, not the extra-time sector; "
                     "the one-body discrepancies scale with the number of sea modes (8 here) and would diverge in the "
                     "continuum (remark, not computed)"},
    }
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with open(REPORT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rep, fh, indent=1, ensure_ascii=False, sort_keys=False)
        fh.write("\n")
    print(f"{npass}/{len(CHECKS)} checks passed; report {os.path.relpath(REPORT, REV).replace(os.sep, '/')}")
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
