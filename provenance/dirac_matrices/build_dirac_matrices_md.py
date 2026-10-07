#!/usr/bin/env python3
"""Build and verify `provenance/dirac matrices.md`: the eight real 16 x 16 Dirac matrices of the author.

Source of truth: the author's notebook
  Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb (read only).
`extract_from_author_notebook.wls` evaluates the author's own input cells in a fresh Wolfram kernel and
writes `author_notebook_T16.json`; this script reads that file and proves, in exact arithmetic,

  1. the eight matrices Gamma_A = T16A[A] (A = 0..7) are real (integer entries -1, 0, 1);
  2. {Gamma_A, Gamma_B} = 2 eta_AB I16 with eta = eta4488 = diag(+1,+1,+1,+1,-1,-1,-1,-1)  (Cl(4,4));
  3. the scaled commutators S^AB = (1/4)[Gamma_A, Gamma_B] close on so(4,4), act on the Gamma_C as
     so(4,4) acts on vectors, exponentiate (closed forms, checked with sympy) to products of two unit
     vectors, i.e. to elements of Pin(4,4), and generate its identity component Spin_0(4,4); together
     with Gamma_0 and Gamma_4 they generate all of Pin(4,4) (the four components are separated exactly);
  4. the products (sigma16, T16A[8], all 256 ordered basis products) and the projectors P_L, P_R
     have the stated properties;
  5. the matrices used by the repository's calculations (Revision/algebra/gammas.json, the Revision
     construction in Revision/algebra/python/check_algebra.py, scripts/d16c_exact.py) equal these.

Every check is exact (Python integers / fractions.Fraction); the Clifford relation and the so(4,4)
closure are re-evaluated with sympy as a second engine, and the exponentials are verified
symbolically with sympy.  The run stops with exit code 1 if any check fails; the Markdown file is
written only when every check passes.  Output is deterministic (LF line endings, no time stamps).

Usage (from the repository root):
  wolframscript -file provenance/dirac_matrices/extract_from_author_notebook.wls
  python provenance/dirac_matrices/build_dirac_matrices_md.py            # check and write
  python provenance/dirac_matrices/build_dirac_matrices_md.py --check    # check and compare, write nothing
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NB_JSON = HERE / "author_notebook_T16.json"
OUT = ROOT / "provenance" / "dirac matrices.md"
NOTEBOOK = "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb"

N = 16
IDX = range(8)
# author's coordinate x_k (k = 1..8) -> notebook index A (Revision/SPEC.md section 2)
COORD_OF_A = {0: "x8", 1: "x1", 2: "x2", 3: "x3", 4: "x4", 5: "x5", 6: "x6", 7: "x7"}
ROLE_OF_A = {0: "hidden space-like direction", 1: "space", 2: "space", 3: "space",
             4: "time", 5: "extra time", 6: "extra time", 7: "extra time"}


# --------------------------------------------------------------------------- exact helpers
def zeros(n=N):
    return [[0] * n for _ in range(n)]


def ident(n=N):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    out = [[0] * m for _ in range(n)]
    for i in range(n):
        for t in range(k):
            x = a[i][t]
            if x:
                bt = b[t]
                oi = out[i]
                for j in range(m):
                    if bt[j]:
                        oi[j] += x * bt[j]
    return out


def mulall(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = mul(out, m)
    return out


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scal(c, a):
    return [[c * x for x in r] for r in a]


def tr(a):
    return [list(r) for r in zip(*a)]


def eq(a, b):
    return all(x == y for r, s in zip(a, b) for x, y in zip(r, s))


def is_zero(a):
    return all(x == 0 for r in a for x in r)


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def comm(a, b):
    return sub(mul(a, b), mul(b, a))


def anti(a, b):
    return add(mul(a, b), mul(b, a))


def lin_comb(coeffs, mats):
    out = zeros(len(mats[0]))
    for c, m in zip(coeffs, mats):
        if c:
            out = add(out, scal(c, m))
    return out


def rank(rows):
    """Exact rank of a list of equal-length rows (Fraction Gaussian elimination)."""
    m = [[Fraction(x) for x in r] for r in rows]
    rk, col, ncol = 0, 0, len(m[0]) if m else 0
    while rk < len(m) and col < ncol:
        piv = next((i for i in range(rk, len(m)) if m[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        m[rk], m[piv] = m[piv], m[rk]
        p = m[rk][col]
        m[rk] = [x / p for x in m[rk]]
        for i in range(len(m)):
            if i != rk and m[i][col] != 0:
                f = m[i][col]
                m[i] = [x - f * y for x, y in zip(m[i], m[rk])]
        rk += 1
        col += 1
    return rk


def det(a):
    return sympy.Matrix(a).det()


# --------------------------------------------------------------------------- check registry
CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    CHECKS.append((name, bool(ok), detail))
    if not ok:
        print(f"FAIL {name}: {detail}")
    return ok


# --------------------------------------------------------------------------- display helpers
def fmt_matrix(m):
    def cell(x):
        x = Fraction(x)
        s = str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
        return s.rjust(2)
    return "\n".join("[" + " ".join(cell(x) for x in r) + " ]" for r in m)


def signed_perm(m):
    """One-line form of a signed permutation matrix: entry i is +-j (row i has +-1 in column j)."""
    out = []
    for r in m:
        nz = [(j, x) for j, x in enumerate(r) if x]
        assert len(nz) == 1 and nz[0][1] in (1, -1)
        j, x = nz[0]
        out.append(("+" if x > 0 else "-") + str(j + 1))
    return " ".join(s.rjust(3) for s in out)


def gname(A):
    return f"Gamma_{A}"


# --------------------------------------------------------------------------- main
def main():
    if not NB_JSON.exists():
        print(f"ERROR: {NB_JSON.relative_to(ROOT)} not found; run extract_from_author_notebook.wls first")
        return 1
    nbd = json.loads(NB_JSON.read_text(encoding="utf-8"))
    G = [[[int(x) for x in r] for r in m] for m in nbd["T16A"]]
    eta8 = [[int(x) for x in r] for r in nbd["eta4488"]]
    eta = [eta8[A][A] for A in IDX]
    sigma16 = nbd["sigma16"]
    T8 = nbd["T16A_8"]
    PL = [[Fraction(x, 2) for x in r] for r in nbd["twice_PL"]]
    PR = [[Fraction(x, 2) for x in r] for r in nbd["twice_PR"]]
    I = ident()

    # ---- 0. the notebook's metric
    check("eta4488_diagonal_4_4",
          eta == [1, 1, 1, 1, -1, -1, -1, -1] and all(eta8[A][B] == 0 for A in IDX for B in IDX if A != B),
          f"eta4488 from author input cell 41 = diag{tuple(eta)}: signature (4,4)")

    # ---- 1. reality
    entries = sorted({x for m in G for r in m for x in r})
    check("eight_16x16", len(G) == 8 and all(len(m) == 16 and all(len(r) == 16 for r in m) for m in G),
          "exactly eight matrices, each 16 x 16")
    check("real_integer_entries", entries == [-1, 0, 1],
          f"the set of all entries of the eight matrices is {entries}: every entry is a real integer")
    check("signed_permutation", all(sum(1 for x in r if x) == 1 for m in G for r in m)
          and all(sum(1 for r in m if r[j]) == 1 for m in G for j in range(N)),
          "each Gamma_A has exactly one nonzero entry (+1 or -1) in every row and every column")
    check("orthogonal", all(eq(mul(tr(m), m), I) for m in G), "Gamma_A^T Gamma_A = I16 for every A")
    sym = [A for A in IDX if eq(tr(G[A]), G[A])]
    asym = [A for A in IDX if eq(tr(G[A]), scal(-1, G[A]))]
    check("transpose_pattern", sym == [0, 1, 2, 3] and asym == [4, 5, 6, 7],
          f"symmetric: A = {sym} (eta = +1); antisymmetric: A = {asym} (eta = -1); so Gamma_A^T = eta_AA Gamma_A")

    # ---- 2. anticommutation (own integers + sympy)
    bad = [(A, B) for A in IDX for B in IDX if not eq(anti(G[A], G[B]), scal(2 * eta8[A][B], I))]
    check("clifford_anticommutation", not bad,
          "{Gamma_A, Gamma_B} = Gamma_A Gamma_B + Gamma_B Gamma_A = 2 eta_AB I16 for all 64 ordered pairs "
          f"(integer arithmetic){'' if not bad else f'; failures {bad}'}")
    sG = [sympy.Matrix(m) for m in G]
    bad_s = [(A, B) for A in IDX for B in IDX if sG[A] * sG[B] + sG[B] * sG[A] != 2 * eta8[A][B] * sympy.eye(N)]
    check("clifford_anticommutation_sympy", not bad_s, "the same 64 relations re-evaluated with sympy.Matrix")
    squares = ["+I16" if eq(mul(G[A], G[A]), I) else "-I16" if eq(mul(G[A], G[A]), scal(-1, I)) else "?"
               for A in IDX]
    check("squares", squares == ["+I16"] * 4 + ["-I16"] * 4,
          f"Gamma_A^2 for A = 0..7: {squares}")

    # ---- 3. products: all 256 ordered basis products
    subsets = [s for k in range(9) for s in itertools.combinations(IDX, k)]
    prods = {s: (mulall(*[G[A] for A in s]) if s else I) for s in subsets}
    gram_ok = all(trace(mul(tr(prods[s]), prods[t])) == (16 if s == t else 0) for s in subsets for t in subsets)
    check("256_products_orthonormal", len(subsets) == 256 and gram_ok,
          "the 256 products Gamma_{A1}...Gamma_{Ak} (A1 < ... < Ak, k = 0..8) are signed permutation matrices "
          "with tr(P_s^T P_t) = 16 delta_st: they are linearly independent, so they form a basis of the "
          "256-dimensional space of real 16 x 16 matrices: Cl(4,4) = M16(R)")
    check("irreducible", gram_ok,
          "consequence: a matrix commuting with all eight Gamma_A commutes with every product, hence with "
          "all of M16(R), hence is a multiple of I16 (Schur): the 16-dimensional representation is irreducible")
    check("sigma16_product", eq(sigma16, mulall(G[0], G[1], G[2], G[3])),
          "sigma16 (author input cell 285) = Gamma_0 Gamma_1 Gamma_2 Gamma_3")
    check("T16A8_product", eq(T8, mulall(*G)),
          "T16A[8] (author input cell 287) = Gamma_0 Gamma_1 ... Gamma_7")
    check("T16A8_chirality", eq(mul(T8, T8), I) and all(is_zero(anti(T8, g)) for g in G)
          and eq(T8, [[(-1 if i < 8 else 1) if i == j else 0 for j in range(N)] for i in range(N)]),
          "T16A[8]^2 = I16, T16A[8] anticommutes with every Gamma_A, and T16A[8] = diag(-I8, I8)")
    check("sigma16_properties", eq(tr(sigma16), sigma16) and eq(mul(sigma16, sigma16), I)
          and all(eq(tr(mul(sigma16, g)), scal(-1, mul(sigma16, g))) for g in G),
          "sigma16 is symmetric, sigma16^2 = I16, and sigma16 Gamma_A is antisymmetric for every A")

    # ---- 4. scaled commutators S^AB and Pin(4,4)
    pairs = [(A, B) for A in IDX for B in IDX if A < B]
    S = {}
    for A in IDX:
        for B in IDX:
            S[(A, B)] = [[Fraction(x, 4) for x in r] for r in comm(G[A], G[B])]
    ok = all(eq(S[(A, B)], [[Fraction(x, 2) for x in r] for r in mul(G[A], G[B])]) for A, B in pairs)
    ok = ok and all(eq(S[(A, B)], scal(-1, S[(B, A)])) for A in IDX for B in IDX)
    check("S_definition", ok, "S^AB = (1/4)[Gamma_A, Gamma_B] = (1/2) Gamma_A Gamma_B for A != B, S^BA = -S^AB: "
          "28 independent pairs A < B")
    check("S_linearly_independent", rank([[x for r in S[p] for x in r] for p in pairs]) == 28,
          "the 28 matrices S^AB (A < B) have exact rank 28: dim = 28 = dim so(4,4)")

    def eta_(a, b):
        return eta8[a][b]

    bad = 0
    bad_s = 0
    sS = {p: sympy.Matrix(S[p]) for p in S}
    for (a, b), (c, d) in itertools.product(pairs, pairs):
        lhs = comm(S[(a, b)], S[(c, d)])
        rhs = zeros()
        for coef, key in ((eta_(b, c), (a, d)), (-eta_(a, c), (b, d)), (-eta_(b, d), (a, c)), (eta_(a, d), (b, c))):
            if coef:
                rhs = add(rhs, scal(coef, S[key]))
        bad += not eq(lhs, rhs)
        rs = (eta_(b, c) * sS[(a, d)] - eta_(a, c) * sS[(b, d)] - eta_(b, d) * sS[(a, c)] + eta_(a, d) * sS[(b, c)])
        bad_s += (sS[(a, b)] * sS[(c, d)] - sS[(c, d)] * sS[(a, b)]) != rs
    check("so44_closure", bad == 0 and bad_s == 0,
          "[S^AB, S^CD] = eta_BC S^AD - eta_AC S^BD - eta_BD S^AC + eta_AD S^BC for all 28 x 28 pairs "
          f"(integer/Fraction arithmetic: {bad} failures; sympy: {bad_s} failures): the S^AB span the Lie "
          "algebra so(4,4)")

    # vector action: [S^AB, Gamma_C] = eta_BC Gamma_A - eta_AC Gamma_B  ->  8 x 8 matrices M^AB
    M = {}
    bad = []
    for p in pairs:
        A, B = p
        m8 = [[0] * 8 for _ in IDX]  # column C holds the coefficients of [S^AB, Gamma_C] on Gamma_D
        for C in IDX:
            lhs = comm(S[p], G[C])
            coeffs = [Fraction(0)] * 8
            coeffs[A] += eta_(B, C)
            coeffs[B] -= eta_(A, C)
            if not eq(lhs, lin_comb(coeffs, G)):
                bad.append((p, C))
            for D in IDX:
                m8[D][C] = coeffs[D]
        M[p] = m8
    check("S_vector_action", not bad,
          "[S^AB, Gamma_C] = eta_BC Gamma_A - eta_AC Gamma_B for all 28 pairs and all 8 C: the commutator "
          "with S^AB maps the span of the Gamma's to itself by the 8 x 8 matrix M^AB")
    eta_m = [[eta_(i, j) for j in IDX] for i in IDX]
    check("M_in_so44", all(is_zero(add(mul(tr(M[p]), eta_m), mul(eta_m, M[p]))) for p in pairs),
          "(M^AB)^T eta + eta M^AB = 0 for every pair: every M^AB lies in so(4,4) = {X : X^T eta + eta X = 0}")
    # dimension of so(4,4): the linear conditions on the 64 entries of X
    rows = []
    for i in IDX:
        for j in IDX:
            row = [0] * 64
            row[j * 8 + i] += eta_(j, j)   # (X^T eta)_ij = X_ji eta_jj
            row[i * 8 + j] += eta_(i, i)   # (eta X)_ij = eta_ii X_ij
            rows.append(row)
    dim_so = 64 - rank(rows)
    check("M_basis_of_so44", dim_so == 28 and rank([[x for r in M[p] for x in r] for p in pairs]) == 28,
          f"so(4,4) has dimension {dim_so} (exact rank of its 64 linear conditions) and the 28 M^AB are "
          "linearly independent: they form a basis of so(4,4)")
    hom_bad = 0
    for (a, b), (c, d) in itertools.product(pairs, pairs):
        lhs = sub(mul(M[(a, b)], M[(c, d)]), mul(M[(c, d)], M[(a, b)]))

        def Mk(x, y):
            return M[(x, y)] if x < y else scal(-1, M[(y, x)]) if x > y else [[0] * 8 for _ in IDX]
        rhs = [[0] * 8 for _ in IDX]
        for coef, (x, y) in ((eta_(b, c), (a, d)), (-eta_(a, c), (b, d)), (-eta_(b, d), (a, c)), (eta_(a, d), (b, c))):
            if coef:
                rhs = add(rhs, scal(coef, Mk(x, y)))
        hom_bad += not eq(lhs, rhs)
    check("spin_to_so_isomorphism", hom_bad == 0,
          "the M^AB satisfy the same commutation relations as the S^AB (28 x 28 pairs, "
          f"{hom_bad} failures): S^AB -> M^AB is a Lie-algebra isomorphism spin(4,4) -> so(4,4)")

    # invariant bilinear and chirality
    check("S_preserves_sigma16", all(is_zero(add(mul(tr(S[p]), sigma16), mul(sigma16, S[p]))) for p in pairs),
          "(S^AB)^T sigma16 + sigma16 S^AB = 0: the author's bilinear Psi^T sigma16 Psi is invariant under the "
          "group generated by the S^AB")
    check("S_commute_with_T16A8", all(is_zero(comm(T8, S[p])) for p in pairs),
          "[T16A[8], S^AB] = 0: the chiral halves are invariant under the group generated by the S^AB")

    # exponentials: closed forms, symbolic proof with sympy
    th, ph = sympy.symbols("theta phi", real=True)
    n_rot = n_boost = 0
    exp_ok = True
    vec_ok = True
    pin_ok = True
    cover_ok = True
    for p in pairs:
        A, B = p
        K = mul(G[A], G[B])          # = 2 S^AB
        s = eta[A] * eta[B]          # K^2 = -s I
        if not eq(mul(K, K), scal(-s, I)):
            exp_ok = False
            continue
        if s == 1:
            n_rot += 1
            c, sn = sympy.cos(th / 2), sympy.sin(th / 2)
        else:
            n_boost += 1
            c, sn = sympy.cosh(th / 2), sympy.sinh(th / 2)
        # g(theta) = c I + sn K.  (i) g(0) = I; (ii) dg/dtheta = S^AB g  <=>  c' = -s sn / 2, sn' = c / 2
        exp_ok &= c.subs(th, 0) == 1 and sn.subs(th, 0) == 0
        exp_ok &= sympy.simplify(sympy.diff(c, th) + s * sn / 2) == 0 and sympy.simplify(sympy.diff(sn, th) - c / 2) == 0
        # (iii) g(theta) g(phi) = g(theta + phi): coefficient identities using K^2 = -s I
        c2, s2 = c.subs(th, ph), sn.subs(th, ph)
        c3, s3 = c.subs(th, th + ph), sn.subs(th, th + ph)
        exp_ok &= sympy.simplify(sympy.expand_trig(c * c2 - s * sn * s2 - c3)) == 0
        exp_ok &= sympy.simplify(sympy.expand_trig(c * s2 + sn * c2 - s3)) == 0
        # vector action at group level: g Gamma_C g^-1 = sum_D Lambda_DC Gamma_D, g^-1 = c I - sn K
        KC_comm = {C: comm(K, G[C]) for C in IDX}
        KCK = {C: mulall(K, G[C], K) for C in IDX}
        Lam = sympy.zeros(8, 8)
        for C in IDX:
            # g G_C g^-1 = c^2 G_C + c sn [K, G_C] - sn^2 K G_C K ; decompose each on the Gamma's
            for D in IDX:
                cD_comm = Fraction(trace(mul(tr(G[D]), KC_comm[C])), 16)
                cD_kck = Fraction(trace(mul(tr(G[D]), KCK[C])), 16)
                Lam[D, C] = (c ** 2 * int(D == C) + c * sn * sympy.Rational(cD_comm.numerator, cD_comm.denominator)
                             - sn ** 2 * sympy.Rational(cD_kck.numerator, cD_kck.denominator))
            recon = sum(([sympy.Matrix(G[D]) * Lam[D, C] for D in IDX]), sympy.zeros(N, N))
            direct = (c * sympy.eye(N) + sn * sympy.Matrix(K)) * sympy.Matrix(G[C]) * (c * sympy.eye(N) - sn * sympy.Matrix(K))
            vec_ok &= sympy.expand(recon - direct) == sympy.zeros(N, N)
        Lam = Lam.applyfunc(sympy.simplify)
        Mm = sympy.Matrix(M[p])
        vec_ok &= sympy.simplify(Lam.diff(th) - Mm * Lam) == sympy.zeros(8, 8)          # Lambda = exp(theta M^AB)
        vec_ok &= Lam.subs(th, 0) == sympy.eye(8)
        vec_ok &= sympy.simplify(Lam.T * sympy.Matrix(eta_m) * Lam - sympy.Matrix(eta_m)) == sympy.zeros(8, 8)
        # exp(theta S^AB) is a product of two unit vectors: g = Gamma_A Gamma(u), u = eta_A c e_A + sn e_B
        u = [0] * 8
        u[A], u[B] = eta[A] * c, sn
        norm_u = sympy.simplify(sum(eta[D] * u[D] ** 2 for D in IDX))
        Gu = sum((sympy.Matrix(G[D]) * u[D] for D in IDX), sympy.zeros(N, N))
        g = c * sympy.eye(N) + sn * sympy.Matrix(K)
        pin_ok &= sympy.simplify(norm_u - eta[A]) == 0
        pin_ok &= sympy.simplify(sympy.Matrix(G[A]) * Gu - g) == sympy.zeros(N, N)
        # double cover for rotations: g(2 pi) = -I16 while Lambda(2 pi) = I8
        if s == 1:
            cover_ok &= g.subs(th, 2 * sympy.pi) == -sympy.eye(N) and Lam.subs(th, 2 * sympy.pi) == sympy.eye(8)
    check("exp_closed_forms", exp_ok and n_rot == 12 and n_boost == 16,
          f"(2 S^AB)^2 = (Gamma_A Gamma_B)^2 = -eta_AA eta_BB I16, so exp(theta S^AB) = cos(theta/2) I16 + "
          f"sin(theta/2) Gamma_A Gamma_B for the {n_rot} rotation generators (eta_AA = eta_BB) and "
          f"cosh(theta/2) I16 + sinh(theta/2) Gamma_A Gamma_B for the {n_boost} boost generators "
          "(eta_AA = -eta_BB); verified symbolically (sympy): g(0) = I16, dg/dtheta = S^AB g, g(theta) g(phi) = g(theta + phi)")
    check("exp_vector_action", vec_ok,
          "for every generator, exp(theta S^AB) Gamma_C exp(-theta S^AB) = sum_D Lambda(theta)_DC Gamma_D with "
          "Lambda(theta) = exp(theta M^AB) (checked as Lambda(0) = I8 and dLambda/dtheta = M^AB Lambda) and "
          "Lambda^T eta Lambda = eta: each exp(theta S^AB) acts on the Gamma's as an element of SO_0(4,4) (sympy, symbolic theta)")
    check("exp_is_product_of_two_unit_vectors", pin_ok,
          "exp(theta S^AB) = Gamma_A Gamma(u) with Gamma(u) = sum_D u^D Gamma_D, u = eta_AA cos(theta/2) e_A + "
          "sin(theta/2) e_B (rotation) or cosh(theta/2) e_A + sinh(theta/2) e_B (boost), eta(u,u) = eta_AA = +-1: "
          "every exponential of a scaled commutator is a product of two unit vectors, i.e. an element of "
          "Spin(4,4) inside Pin(4,4) (sympy, symbolic theta)")
    check("double_cover", cover_ok,
          "for the 12 rotation generators exp(2 pi S^AB) = -I16 while Lambda(2 pi) = I8: the kernel of "
          "Spin_0(4,4) -> SO_0(4,4) contains -I16 (double cover)")

    # the four components of Pin(4,4): Lambda of Gamma_0, Gamma_4, Gamma_0 Gamma_4 (twisted adjoint)
    def twisted_lambda(x, odd):
        """Matrix L with sign * x Gamma_C x^-1 = sum_D L_DC Gamma_D, sign = -1 for odd x (twisted adjoint)."""
        xinv = [[Fraction(v) for v in r] for r in sympy.Matrix(x).inv().tolist()]
        L = [[0] * 8 for _ in IDX]
        for C in IDX:
            y = scal(-1 if odd else 1, mulall(x, G[C], xinv))
            for D in IDX:
                L[D][C] = Fraction(trace(mul(tr(G[D]), y)), 16)
            if not eq(y, lin_comb([L[D][C] for D in IDX], G)):
                return None
        return L

    comps = []
    for label, x, odd in (("I16", I, False), ("Gamma_0", G[0], True), ("Gamma_4", G[4], True),
                          ("Gamma_0 Gamma_4", mul(G[0], G[4]), False)):
        L = twisted_lambda(x, odd)
        dL = det(L)
        dspace = det([r[:4] for r in L[:4]])
        dtime = det([r[4:] for r in L[4:]])
        comps.append((label, L is not None and eq(mul(mul(tr(L), eta_m), L), eta_m), dL, dspace, dtime))
    comp_ok = (all(c[1] for c in comps)
               and [(c[2], sympy.sign(c[3]), sympy.sign(c[4])) for c in comps]
               == [(1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)])
    check("pin44_four_components", comp_ok,
          "twisted adjoint action x Gamma_C x^-1 (times -1 for odd x) of I16, Gamma_0, Gamma_4, Gamma_0 Gamma_4: "
          + "; ".join(f"{c[0]}: det {c[2]}, sign det(space block) {sympy.sign(c[3])}, sign det(time block) {sympy.sign(c[4])}"
                      for c in comps)
          + ". The four (det, space, time) sign patterns are different, so these four elements lie in the four "
          "different components of Pin(4,4); every product of exponentials exp(theta S^AB) acts with pattern "
          "(+1, +1, +1) (it is connected to I16), so the scaled commutators alone generate only the identity "
          "component Spin_0(4,4)")

    # ---- 5. projectors
    def fmul(a, b):
        return mul(a, b)
    IF = [[Fraction(x) for x in r] for r in I]
    proj_ok = (eq(add(PL, PR), IF) and eq(fmul(PL, PL), PL) and eq(fmul(PR, PR), PR)
               and is_zero(fmul(PL, PR)) and is_zero(fmul(PR, PL))
               and eq(tr(PL), PL) and eq(tr(PR), PR) and trace(PL) == 8 and trace(PR) == 8)
    check("projectors_PL_PR", proj_ok,
          "P_L = (I16 - T16A[8])/2 and P_R = (I16 + T16A[8])/2 (author input cells 323, 324): P_L + P_R = I16, "
          "P_L^2 = P_L, P_R^2 = P_R, P_L P_R = P_R P_L = 0, both symmetric, tr P_L = tr P_R = 8")
    check("projectors_vs_gammas", all(eq(mul(G[A], PL), mul(PR, G[A])) and eq(mul(G[A], PR), mul(PL, G[A])) for A in IDX)
          and all(is_zero(comm(PL, S[p])) and is_zero(comm(PR, S[p])) for p in pairs),
          "Gamma_A P_L = P_R Gamma_A and Gamma_A P_R = P_L Gamma_A (each Dirac matrix exchanges the halves) and "
          "[P_L, S^AB] = [P_R, S^AB] = 0 (each half is invariant under Spin_0(4,4))")
    check("projectors_vs_sigma16", is_zero(comm(PL, sigma16)) and is_zero(comm(PR, sigma16)),
          "[P_L, sigma16] = [P_R, sigma16] = 0: sigma16 = diag(-sigma, sigma) is block diagonal")

    # ---- 6. the matrices used by the repository's calculations
    fx = json.loads((ROOT / "Revision/algebra/gammas.json").read_text(encoding="utf-8"))
    coord_to_A = [1, 2, 3, 4, 5, 6, 7, 0]  # x1..x8 -> notebook index
    ok = (fx["coordinates"] == ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
          and all(eq([[int(v) for v in r] for r in fx["gamma"][k]], G[coord_to_A[k]]) for k in range(8))
          and eq([[int(v) for v in r] for r in fx["C"]], sigma16)
          and eq([[int(v) for v in r] for r in fx["Gamma"]], T8))
    check("fixture_Revision_algebra_gammas_json", ok,
          "Revision/algebra/gammas.json (the fixture read by the Revision code and the textbook notebooks): "
          "gamma^(x1..x3) = Gamma_1..3, gamma^(x4) = Gamma_4, gamma^(x5..x7) = Gamma_5..7, gamma^(x8) = Gamma_0, "
          "C = sigma16, Gamma = T16A[8], entry by entry")

    def load(path, name):
        spec = importlib.util.spec_from_file_location(name, ROOT / path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    rev = load("Revision/algebra/python/check_algebra.py", "check_algebra").construct()
    check("Revision_construction", all(eq(rev["T16"][A], G[A]) for A in IDX) and eq(rev["sigma16"], sigma16)
          and eq(rev["T16_8"], T8),
          "construct() of Revision/algebra/python/check_algebra.py gives the same T16[0..7], sigma16, T16A[8]")
    old = load("scripts/d16c_exact.py", "d16c_exact").notebook_gammas()
    check("old_stage_construction", all(eq([[int(v) for v in r] for r in old[A]], G[A]) for A in IDX),
          "notebook_gammas() of scripts/d16c_exact.py (the earlier stages) gives the same eight matrices")
    consumers = sorted(str(p.relative_to(ROOT)).replace("\\", "/")
                       for base in ("Revision", "tests", "scripts")
                       for p in (ROOT / base).rglob("*")
                       if p.suffix in (".py", ".wl", ".wls") and p.is_file()
                       and "gammas.json" in p.read_text(encoding="utf-8", errors="ignore")
                       and p.name != Path(__file__).name)

    failed = [c for c in CHECKS if not c[1]]
    if failed:
        print(f"{len(failed)} of {len(CHECKS)} checks FAILED; {OUT.name} not written")
        return 1

    # ------------------------------------------------------------------- write the Markdown
    L = []
    w = L.append
    w("# Dirac matrices: the eight real 16 x 16 Dirac matrices of the author's notebook")
    w("")
    w(f"Provenance file.  Generated by `provenance/dirac_matrices/build_dirac_matrices_md.py` from the author's "
      f"notebook `{NOTEBOOK}` (read only, never modified).  Do not edit by hand: re-run the two commands below.")
    w("")
    w("## Answer in one paragraph")
    w("")
    w("Yes: the calculations use eight real-valued 16 x 16 Dirac matrices, and they are the author's own. "
      "They come from the author's input cells, evaluated directly from the `.nb` file, not re-typed. "
      "All entries are -1, 0 or +1. The matrices satisfy {Gamma_A, Gamma_B} = 2 eta_AB I16 with "
      "eta = diag(+1,+1,+1,+1,-1,-1,-1,-1), which is the Clifford algebra Cl(4,4) = M16(R). "
      "The 28 scaled commutators S^AB = (1/4)[Gamma_A, Gamma_B] form a basis of spin(4,4), which is isomorphic to so(4,4). "
      "Their exponentials are products of two unit vectors, and they generate the identity component Spin_0(4,4) of Pin(4,4). "
      "Pin(4,4) itself has four components. The commutators alone cannot reach the other three; the check "
      "`pin44_four_components` proves this exactly. Adding one space-like and one time-like Dirac matrix "
      "(Gamma_0 and Gamma_4) generates all of Pin(4,4). "
      "Every matrix file used by the repository's calculations equals these matrices entry by entry. "
      "The *field* Psi16 has complex (Grassmann) components, as Revision/SPEC.md requires; the *matrices* are real. "
      f"All {len(CHECKS)} exact checks pass.")
    w("")
    w("## How to reproduce (complete, self-contained)")
    w("")
    w("Requirements: Wolfram Engine or Mathematica with `wolframscript` on the PATH; Python 3.10+ with `sympy`. "
      "From the repository root:")
    w("")
    w("```bash")
    w("wolframscript -file provenance/dirac_matrices/extract_from_author_notebook.wls")
    w("python provenance/dirac_matrices/build_dirac_matrices_md.py")
    w("```")
    w("")
    w("Expected output: the first command prints `author notebook: 996 input cells`, then one line "
      "`evaluated author input cell N: ...` for each of the 14 cells listed below, then `wrote .../author_notebook_T16.json`. "
      f"The second command prints `{len(CHECKS)} of {len(CHECKS)} checks pass` and `wrote provenance/dirac matrices.md`. "
      "Run time: about 1 minute (Wolfram) and about 10 seconds (Python). "
      "Side effects: the two commands write only `provenance/dirac_matrices/author_notebook_T16.json` and "
      "`provenance/dirac matrices.md`. The notebook is only read. "
      "If any check fails, the second command prints `FAIL <name>: <detail>`, does not write this file and exits with code 1. "
      "`python provenance/dirac_matrices/build_dirac_matrices_md.py --check` runs every check and confirms that this file is up to date without writing anything; the test `tests/test_dirac_matrices_provenance.py` does the same.")
    w("")
    w("## Source: the author's input cells that were evaluated")
    w("")
    w("| input cell (index among the notebook's Input cells) | defines |")
    w("|---|---|")
    for c in nbd["cells"]:
        w(f"| {c['input_cell']} | `{c['defines']}` |")
    w("")
    w("The construction, in the author's words: `Qa[h,p,q] = Signature[{h,p,q,4}]`, "
      "`Qb[h,p,q] = ID4[[p,4]] ID4[[q,h]] - ID4[[p,h]] ID4[[q,4]]`; `s4by4[h] = Qa - Qb`, `t4by4[h] = Qa + Qb` "
      "(self-dual and anti-self-dual 4 x 4 blocks); `tau[0] = ID8`, `tau[h] = {{0, s4by4[h]}, {s4by4[h], 0}}`, "
      "`tau[7-h] = {{0, t4by4[h]}, {-t4by4[h], 0}}` (h = 1..3), `tau[7] = tau[1]...tau[6]`; "
      "`taubar[A] = sigma . Transpose[tau[A]] . sigma` with `sigma = {{0, I4}, {I4, 0}}`; "
      "and finally **`T16A[A] = {{0, taubar[A]}, {tau[A], 0}}`, A = 0..7**. Below, Gamma_A = T16A[A].")
    w("")
    w("Coordinates (Revision/SPEC.md section 2): " + ", ".join(
        f"Gamma_{A} = gamma^({COORD_OF_A[A]}) ({ROLE_OF_A[A]}, eta = {eta[A]:+d})" for A in IDX) + ".")
    w("")
    w("## The proofs (every check, exact)")
    w("")
    w("| # | check | result | what is proved |")
    w("|---|---|---|---|")
    for i, (name, ok, detail) in enumerate(CHECKS, 1):
        w(f"| {i} | `{name}` | {'PASS' if ok else 'FAIL'} | {detail.replace('|', '/')} |")
    w("")
    w("### Why the scaled commutators generate Pin(4,4) (argument)")
    w("")
    w("1. **Lie algebra.** The 28 matrices S^AB are linearly independent (`S_linearly_independent`). They close under commutators "
      "with the structure constants of so(4,4) (`so44_closure`). The map S^AB -> M^AB, given by the action on the Gamma's, is an "
      "isomorphism onto the 28-dimensional so(4,4) (`S_vector_action`, `M_in_so44`, `M_basis_of_so44`, `spin_to_so_isomorphism`). "
      "So the S^AB span spin(4,4), which is isomorphic to so(4,4).")
    w("2. **Group.** Each exp(theta S^AB) is a product of two unit vectors Gamma_A Gamma(u) (`exp_is_product_of_two_unit_vectors`). "
      "Pin(4,4) is by definition the group generated by the unit vectors Gamma(v) with eta(v,v) = +-1, so each exp(theta S^AB) lies in "
      "Pin(4,4), in fact in its even part Spin(4,4). Each exp(theta S^AB) acts on the Gamma's as exp(theta M^AB), "
      "which is in SO_0(4,4) (`exp_vector_action`). The rotation generators give exp(2 pi S^AB) = -I16 (`double_cover`). "
      "A connected Lie group is generated by the exponentials of its Lie algebra. "
      "Therefore the exponentials of the S^AB generate the identity component Spin_0(4,4), a double cover of SO_0(4,4).")
    w("3. **All of Pin(4,4).** Pin(4,4) has four components. `pin44_four_components` shows exactly that I16, Gamma_0, Gamma_4 and "
      "Gamma_0 Gamma_4 lie in four different components. Every unit vector Gamma(v) is g Gamma_0 g^-1 (if eta(v,v) = +1) or "
      "g Gamma_4 g^-1 (if eta(v,v) = -1) for some g in Spin_0(4,4). This holds because SO_0(4,4) acts transitively on each "
      "connected quadric eta(v,v) = +-1 in R^(4,4), and g Gamma_C g^-1 = Gamma(Lambda e_C). "
      "Hence **Pin(4,4) = the group generated by the exp(theta S^AB) together with Gamma_0 and Gamma_4**, which is also the group "
      "generated by the eight Dirac matrices and their unit-vector combinations. "
      "The scaled commutators alone generate exactly the identity component Spin_0(4,4). We state this restriction plainly "
      "rather than claim more than is proved.")
    w("4. **Invariants.** (S^AB)^T sigma16 + sigma16 S^AB = 0, so the author's bilinear Psi^T sigma16 Psi is invariant under "
      "Spin_0(4,4). [T16A[8], S^AB] = 0, so the two chiral halves P_L Psi and P_R Psi are invariant. "
      "The 256 products form a basis of M16(R), so the representation is irreducible under Pin(4,4).")
    w("")
    w("## The eight real 16 x 16 Dirac matrices")
    w("")
    for A in IDX:
        w(f"### Gamma_{A} = T16A[{A}] = gamma^({COORD_OF_A[A]}) - {ROLE_OF_A[A]}, Gamma_{A}^2 = {'+' if eta[A] > 0 else '-'}I16")
        w("")
        w("```text")
        w(fmt_matrix(G[A]))
        w("```")
        w("")
    w("## Products")
    w("")
    w("### sigma16 = Gamma_0 Gamma_1 Gamma_2 Gamma_3 (the author's bilinear form, = diag(-sigma, sigma))")
    w("")
    w("```text")
    w(fmt_matrix(sigma16))
    w("```")
    w("")
    w("### T16A[8] = Gamma_0 Gamma_1 ... Gamma_7 (chirality, = diag(-I8, I8))")
    w("")
    w("```text")
    w(fmt_matrix(T8))
    w("```")
    w("")
    w("### The 28 pairwise products Gamma_A Gamma_B = 2 S^AB (A < B): the scaled commutators")
    w("")
    for A, B in pairs:
        kind = "rotation, (Gamma_A Gamma_B)^2 = -I16" if eta[A] == eta[B] else "boost, (Gamma_A Gamma_B)^2 = +I16"
        w(f"#### Gamma_{A} Gamma_{B} = 2 S^{A}{B} ({kind})")
        w("")
        w("```text")
        w(fmt_matrix(mul(G[A], G[B])))
        w("```")
        w("")
    w("### All 256 ordered basis products (compact form)")
    w("")
    w("Each product Gamma_{A1}...Gamma_{Ak} (A1 < ... < Ak) is a signed permutation matrix. It is written on one line as 16 entries: "
      "entry i is +j or -j, meaning row i has its single nonzero entry, +1 or -1, in column j. "
      "Example: `I16` is `+1 +2 ... +16`. These 256 matrices are a basis of M16(R) (`256_products_orthonormal`).")
    w("")
    w("```text")
    for s in subsets:
        label = ("I16" if not s else "G" + ".".join(str(a) for a in s)).ljust(17)
        w(f"{label} {signed_perm(prods[s])}")
    w("```")
    w("")
    w("## Projection matrices")
    w("")
    w("### P_L = (I16 - T16A[8]) / 2 (author input cell 323) = diag(I8, 0)")
    w("")
    w("```text")
    w(fmt_matrix(PL))
    w("```")
    w("")
    w("### P_R = (I16 + T16A[8]) / 2 (author input cell 324) = diag(0, I8)")
    w("")
    w("```text")
    w(fmt_matrix(PR))
    w("```")
    w("")
    w("## Calculations that use these matrices")
    w("")
    w("Every Revision calculation and every textbook notebook reads its gamma matrices from `Revision/algebra/gammas.json`. "
      "That file equals the author's matrices entry by entry (`fixture_Revision_algebra_gammas_json`). "
      "Both independent constructions in the code give the same matrices (`Revision_construction`, `old_stage_construction`). "
      f"Files that read `gammas.json` ({len(consumers)}):")
    w("")
    for c in consumers:
        w(f"- `{c}`")
    w("")
    text = "\n".join(L) + "\n"
    print(f"{len(CHECKS)} of {len(CHECKS)} checks pass")
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
        if current != text:
            print(f"OUT OF DATE: {OUT.relative_to(ROOT).as_posix()} differs from the regenerated text")
            return 1
        print(f"{OUT.relative_to(ROOT).as_posix()} is up to date")
        return 0
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {OUT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
