#!/usr/bin/env python3
"""Revision Kohn-Sham theory: independent exact sympy derivation and verification (SPEC sections 1, 7).

This file is Revision code; it imports nothing from the old stages (no old module, no old fixture).
It is the independent second engine next to Revision/kohn_sham/theory/verify_ks_theory.wls (Wolfram).
Inputs (Revision outputs only):
  Revision/algebra/reports/python-gammas.json  the author's T16 rebuilt by the Revision Python algebra
                                               code (preferred input of this file)
  Revision/algebra/gammas.json                 the Wolfram fixture (only compared with the above)
  Revision/kohn_sham/ks-theory.json            the Wolfram export for the solver (cross-checked here
                                               against this file's own derivation when it exists)
Output (deterministic, LF): Revision/kohn_sham/reports/ks-theory-python.json

Coordinates (SPEC section 1): x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially
DEFLATING extra times (scale factor e^{-a4} sin^{1/6} z); x8 = the hidden direction, z = 6 H x8.
Arrays index x1..x8 as 0..7.  The proper hidden coordinate y = ln(sin z)/(6H) <= 0 replaces x8.

Usage: python Revision/kohn_sham/theory/check_ks_theory.py
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
KS = HERE.parent
REVISION = KS.parent
PY_GAMMAS = REVISION / "algebra" / "reports" / "python-gammas.json"
WL_GAMMAS = REVISION / "algebra" / "gammas.json"
KS_THEORY = KS / "ks-theory.json"
REPORT = KS / "reports" / "ks-theory-python.json"

CHECKS: list[dict] = []
T_START = time.time()


def check(name: str, ok, detail: str) -> bool:
    verdict = "PASS" if ok is True else ("FAIL" if ok is False else str(ok))
    CHECKS.append({"name": name, "verdict": verdict, "detail": detail})
    print(f"[{verdict}] {name}  t={time.time()-T_START:.1f}s", flush=True)
    return ok is True


def zero(m) -> bool:
    return sp.simplify(sp.Matrix(m)).is_zero_matrix


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------------------------
# A. The gamma matrices (Revision algebra outputs) and the Clifford relations
# ---------------------------------------------------------------------------------------------
src = PY_GAMMAS if PY_GAMMAS.exists() else WL_GAMMAS
fix = json.loads(src.read_text(encoding="utf-8"))
g = [sp.Matrix(m) for m in fix["gamma"]]          # g[a] = gamma^(x_{a+1})
eta = [int(v) for v in fix["eta"]]
I16, I2, Z16 = sp.eye(16), sp.eye(2), sp.zeros(16)
g1, g2, g3, g4, g5, g6, g7, g8 = g
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])

check("fixture_input", True,
      f"gammas read from {src.relative_to(REVISION.parent).as_posix()} (sha256 {sha256(src)})")
if PY_GAMMAS.exists() and WL_GAMMAS.exists():
    wl = json.loads(WL_GAMMAS.read_text(encoding="utf-8"))
    check("fixture_python_equals_wolfram", wl["gamma"] == fix["gamma"] and wl["eta"] == fix["eta"],
          "the Python-built and the Wolfram-built T16 (Revision/algebra) agree entry by entry")
else:
    check("fixture_python_equals_wolfram", "pending", "one of the two Revision gamma files is missing")

cliff = all(g[a] * g[b] + g[b] * g[a] == 2 * (eta[a] if a == b else 0) * I16
            for a in range(8) for b in range(8))
check("clifford_relation", cliff and eta == [1, 1, 1, -1, -1, -1, -1, 1],
      "{gamma^a, gamma^b} = 2 eta^ab, eta = diag(+1,+1,+1,-1,-1,-1,-1,+1) in x1..x8")
C = g8 * g1 * g2 * g3
B = -sp.I * C * g4
Gam = g8 * g1 * g2 * g3 * g4 * g5 * g6 * g7
check("C_B_Gamma", C.T == C and C * C == I16 and B.H == B and B * B == I16
      and Gam == sp.diag(*([-1] * 8 + [1] * 8)),
      "C = g8 g1 g2 g3 real symmetric, C^2 = 1; B = -i C g4 Hermitian, B^2 = 1; Gamma = g8 g1..g7 = diag(-I8, I8)")
check("BC_and_Cg4", B * C == -sp.I * g4 and C * g4 == sp.I * B and C * B * C == B,
      "BC = -i gamma^(x4), C gamma^(x4) = i B, C B C = B (used in the exchange and the EMT)")

# ---------------------------------------------------------------------------------------------
# B. Geometry: hidden coordinate y, warped form, sqrt|g|
# ---------------------------------------------------------------------------------------------
H = sp.symbols("H", positive=True)
yy = sp.symbols("y", negative=True)
x8, z = sp.symbols("x8 z", positive=True)
zy = sp.asin(sp.exp(6 * H * yy))                         # z(y), z in (0, pi/2)
dx8dy = sp.diff(zy / (6 * H), yy)
ok_g88 = sp.simplify((sp.cot(zy) ** 2) * dx8dy ** 2 - 1) == 0
ok_s13 = sp.simplify(sp.sin(zy) ** sp.Rational(1, 3) - sp.exp(2 * H * yy)) == 0
ok_dy = sp.simplify(sp.diff(sp.log(sp.sin(6 * H * x8)) / (6 * H), x8) - sp.cot(6 * H * x8)) == 0
check("geometry_hidden_coordinate", ok_g88 and ok_s13 and ok_dy,
      "y = ln(sin z)/(6H), sin z = e^{6Hy}: dy = cot z dx8, cot^2 z dx8^2 = dy^2, sin^{1/3} z = e^{2Hy}; "
      "z in (0, pi/2) <-> y in (-inf, 0); the patch end z = pi/2 is y = 0")
a0s = sp.symbols("a0", real=True)
detx8 = sp.simplify(sp.Abs(sp.prod([sp.exp(2 * a0s) * sp.sin(z) ** sp.Rational(1, 3)] * 3
                                   + [-1] + [-sp.exp(-2 * a0s) * sp.sin(z) ** sp.Rational(1, 3)] * 3
                                   + [sp.cot(z) ** 2])))
check("geometry_sqrt_det", sp.simplify(detx8 - sp.cos(z) ** 2) == 0,
      "|det g| = sin^2 z cot^2 z = cos^2 z in the author's x8 chart (independent of a4); in the y chart "
      "sqrt|g| = W^6 = e^{6Hy}, W = e^{Hy} (the 7-volume is a4-independent: e^{3a4} e^{-3a4} = 1)")

# metric in the y chart with time-dependent a4
X = sp.symbols("x1:8", real=True) + (sp.Symbol("y", real=True),)
Y = X[7]
x4 = X[3]
a4 = sp.Function("a4", real=True)(x4)
W = sp.exp(H * Y)
hv = [sp.exp(a4) * W] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * W] * 3 + [sp.Integer(1)]
gdiag = [eta[i] * hv[i] ** 2 for i in range(8)]
Gm = sp.diag(*gdiag)
Gmi = sp.diag(*[1 / v for v in gdiag])
check("geometry_warped_form", True,
      "ds^2 = e^{2Hy}[e^{2a4(x4)} dx_{1..3}^2 - e^{-2a4(x4)} dx_{5..7}^2] - dx4^2 + dy^2 "
      "(the author's metric with sin^{1/3} z = e^{2Hy} and cot^2 z dx8^2 = dy^2), "
      "vielbein h = (e^{a4}W x3, 1, e^{-a4}W x3, 1)")

Chr = [[[sp.simplify(sum(Gmi[n, l] * (sp.diff(Gm[l, m], X[k]) + sp.diff(Gm[l, k], X[m])
                                       - sp.diff(Gm[m, k], X[l])) for l in range(8)) / 2)
         for k in range(8)] for m in range(8)] for n in range(8)]
Sab = [[(g[a] * g[b] - g[b] * g[a]) / 4 for b in range(8)] for a in range(8)]


def spin_connection(hvec, Chris, coords):
    om = []
    for mu in range(8):
        O = sp.zeros(16)
        for A in range(8):
            for Bb in range(8):
                w = (hvec[A] * sp.diff(1 / hvec[Bb], coords[mu]) if A == Bb else 0) \
                    + hvec[A] * Chris[A][mu][Bb] / hvec[Bb]
                w = sp.simplify(w)
                if w != 0:
                    O += sp.Rational(1, 2) * eta[A] * w * Sab[A][Bb]
        om.append(sp.simplify(O))
    return om


Om = spin_connection(hv, Chr, X)
compat = all(zero(sp.diff(g[n] / hv[n], X[m]) + sum((Chr[n][m][l] * g[l] / hv[l] for l in range(8)), Z16)
                  + Om[m] * g[n] / hv[n] - g[n] / hv[n] * Om[m]) for m in range(8) for n in range(8))
check("spin_connection_compatibility", compat,
      "canonical omega_mu^a_b = e^a_nu nabla_mu e_b^nu, Omega_mu = (1/2) omega_mu ab S^ab: "
      "d_mu gamma^nu + Gamma^nu_{mu lam} gamma^lam + [Omega_mu, gamma^nu] = 0 for all 64 (mu, nu), a4 = a4(x4)")
a4p = sp.diff(a4, x4)
slash = sp.simplify(sum((g[m] / hv[m] * Om[m] for m in range(8)), Z16))
check("spin_connection_slash_3H", zero(slash - 3 * H * g8),
      "gamma^mu Omega_mu = 3H gamma^(x8) exactly for a4 = a4(x4): no a4' term survives")
s_infl = sp.simplify(sum((g[m] / hv[m] * Om[m] for m in range(3)), Z16).subs(H, 0))
s_defl = sp.simplify(sum((g[m] / hv[m] * Om[m] for m in range(4, 7)), Z16).subs(H, 0))
check("spin_connection_time_terms_cancel",
      (not s_infl.is_zero_matrix) and zero(s_infl + s_defl) and zero(Om[3]) and zero(Om[7]),
      "the a4' pieces of the 3 inflating directions (nonzero, see spin_connection_time_term_value) cancel those of the 3 deflating directions exactly; "
      "Omega_x4 = Omega_y = 0")
infl_coef = sp.simplify((s_infl * g4.inv())[0, 0])
check("spin_connection_time_term_value", sp.simplify(infl_coef - sp.Rational(3, 2) * a4p) == 0
      and zero(s_infl - sp.Rational(3, 2) * a4p * g4),
      f"sum over x1..x3 of gamma^i Omega_i at H = 0 equals ({infl_coef}) gamma^(x4); the x5..x7 sum is its negative")

# x8 chart check of gamma^mu Omega_mu
X8 = sp.symbols("x1:8") + (x8,)
zz = 6 * H * x8
hv8 = [sp.exp(a0s) * sp.sin(zz) ** sp.Rational(1, 6)] * 3 + [sp.Integer(1)] \
    + [sp.exp(-a0s) * sp.sin(zz) ** sp.Rational(1, 6)] * 3 + [sp.cot(zz)]
gd8 = [eta[i] * hv8[i] ** 2 for i in range(8)]
G8 = sp.diag(*gd8)
G8i = sp.diag(*[1 / v for v in gd8])
Chr8 = [[[sp.simplify(sum(G8i[n, l] * (sp.diff(G8[l, m], X8[k]) + sp.diff(G8[l, k], X8[m])
                                        - sp.diff(G8[m, k], X8[l])) for l in range(8)) / 2)
          for k in range(8)] for m in range(8)] for n in range(8)]
Om8 = spin_connection(hv8, Chr8, X8)
slash8 = sp.simplify(sum((g[m] / hv8[m] * Om8[m] for m in range(8)), Z16))
check("spin_connection_slash_3H_x8_chart", zero(slash8 - 3 * H * g8),
      "in the author's x8 chart (frame vector e_(x8) = tan z d_x8 = d_y): gamma^mu Omega_mu = 3H gamma^(x8) too")

# ---------------------------------------------------------------------------------------------
# C. The ansatz W^{-3}: removal of the spin connection; the exact time-dependent reduced equation
# ---------------------------------------------------------------------------------------------
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
chi = sp.Matrix([sp.Function(f"c{i}")(Y, x4) for i in range(16)])
phase = sp.exp(sp.I * (k1 * X[0] + k2 * X[1] + k3 * X[2]))


def dirac(Psi):
    out = sp.zeros(16, 1)
    for m in range(8):
        out += g[m] / hv[m] * (sp.diff(Psi, X[m]) + Om[m] * Psi)
    return out


kap = sp.exp(-H * Y - a4)
red = g8 * sp.diff(chi, Y) + g4 * sp.diff(chi, x4) + sp.I * kap * (k1 * g1 + k2 * g2 + k3 * g3) * chi
lhs = sp.simplify(dirac(phase * W ** -3 * chi) / (phase * W ** -3))
check("ansatz_removes_spin_connection", zero(lhs - red),
      "gamma^mu D_mu (e^{ik.x} W^{-3} chi(y, x4)) = e^{ik.x} W^{-3} [g8 d_y chi + g4 d_x4 chi + i kappa k_j g^j chi], "
      "kappa(y, x4) = e^{-Hy - a4(x4)}: exact, for time-dependent a4, good sector (no x5..x7 dependence)")
lhs0 = sp.simplify(dirac(phase * chi) / phase)
check("ansatz_without_W3_term_survives", zero(lhs0 - red - 3 * H * g8 * chi) and not zero(3 * H * g8 * chi),
      "without the factor W^{-3} the term 3H gamma^(x8) chi survives")

Ms, vs, eps = sp.symbols("M v epsilon", real=True)
hk = sp.Symbol("k", real=True)
# exact evolution: g4 d4 chi = (M - i v g4 - g8 d_y - i kappa k.g) chi  ->  i d4 chi = h chi
mat_dy = sp.I * g4 * g8
mat_k = [-g4 * gg for gg in (g1, g2, g3)]
mat_M = -sp.I * g4
herm = (g4 * g8).T == g4 * g8 and all(m.H == m for m in mat_k + [mat_M]) and mat_dy.H == -mat_dy
check("hamiltonian_16_hermitian", herm and (-sp.I * g4) * (-sp.I * g4) == I16,
      "i d_x4 chi = h chi, h = i g4 g8 d_y (g4 g8 real symmetric, so i g4 g8 d_y is Hermitian) - kappa k_j g4 g^j + M (-i g4) + v: i g4 g8, g4 g^j, -i g4 are Hermitian, "
      "(-i g4)^2 = 1; the KS covariant equation is gamma^mu D_mu Psi = (M_eff - i v_v g4) Psi; the Hilbert norm "
      "int chi^dagger chi dy (= int sqrt|g| Psi^dagger Psi over the hidden direction) is a4-independent and conserved "
      "when the boundary terms vanish")

# ---------------------------------------------------------------------------------------------
# D. Block diagonalisation
# ---------------------------------------------------------------------------------------------
A0, A1, A4 = g8, g8 * g1, g8 * g4
J, K1, K2 = g8 * g1 * g4, g2 * g3, g5 * g6
ok_comm = all((P * Q - Q * P).is_zero_matrix for P in (J, K1, K2) for Q in (A0, A1, A4, B, C, J, K1, K2))
check("blocks_commuting_set", ok_comm and J * J == I16 and K1 * K1 == -I16 and K2 * K2 == -I16,
      "J = g8 g1 g4 (J^2 = 1), K1 = g2 g3, K2 = g5 g6 (K^2 = -1) commute with each other and with "
      "gamma^(x8), gamma^(x8)gamma^(x1), gamma^(x8)gamma^(x4), B, C")
labels = [(j, a, b) for j in (1, -1) for a in (1, -1) for b in (1, -1)]
cols, seeds, projs = [], [], []
for (j, sa, sb) in labels:
    P = (I16 + j * J) / 2 * (I16 - sp.I * sa * K1) / 2 * (I16 - sp.I * sb * K2) / 2
    projs.append(P)
    Pp = P * (I16 + g8) / 2
    for c in range(16):
        v = Pp[:, c]
        if not v.is_zero_matrix:
            break
    seeds.append(c)
    v = 8 * v
    cols += [v, A1 * v]
U = sp.Matrix.hstack(*cols)          # unnormalised, entries in {0, +-1, +-i}
V = U / (2 * sp.sqrt(2))
check("blocks_projectors", all(p.rank() == 2 for p in projs) and sum(projs, Z16) == I16
      and all((p * p - p).is_zero_matrix for p in projs),
      "P(j,s2,s3) = (1+jJ)/2 (1-i s2 K1)/2 (1-i s3 K2)/2: eight rank-2 orthogonal projectors summing to 1")
entries_ok = all(e in (0, 1, -1, sp.I, -sp.I) for e in U)
check("blocks_basis_unitary", sp.simplify(V.H * V) == I16 and entries_ok,
      f"v+ = 8 P(j,s2,s3)(1+g8)/2 e_c, v- = g8 g1 v+, V = [v+ v- ...]/(2 sqrt 2) unitary; seeds c = {seeds}; "
      "entries of 2 sqrt2 V in {0, +-1, +-i}; block index beta = 0..7 for (j,s2,s3) = "
      + ", ".join(str(l) for l in labels))


def blockform(Xm):
    Yb = sp.simplify(V.H * Xm * V)
    bl = [Yb[2 * b:2 * b + 2, 2 * b:2 * b + 2] for b in range(8)]
    Zb = sp.zeros(16)
    for b in range(8):
        Zb[2 * b:2 * b + 2, 2 * b:2 * b + 2] = bl[b]
    return bl, Zb == Yb


expect = {
    "gamma^(x8)": (A0, lambda j, a, b: s3),
    "gamma^(x8)gamma^(x1)": (A1, lambda j, a, b: -sp.I * s2),
    "gamma^(x8)gamma^(x4)": (A4, lambda j, a, b: j * s1),
    "B": (B, lambda j, a, b: j * a * I2),
    "C": (C, lambda j, a, b: a * s2),
    "BC = -i gamma^(x4)": (B * C, lambda j, a, b: j * s2),
    "gamma^(x4)gamma^(x1)": (g4 * g1, lambda j, a, b: -j * s3),
    "B gamma^(x8)": (B * g8, lambda j, a, b: j * a * s3),
    "J": (J, lambda j, a, b: j * I2),
    "K1": (K1, lambda j, a, b: sp.I * a * I2),
    "K2": (K2, lambda j, a, b: sp.I * b * I2),
}
allok = True
for nm, (Xm, f) in expect.items():
    bl, diag = blockform(Xm)
    ok = diag and all(bl[i] == f(*labels[i]) for i in range(8))
    allok &= ok
check("blocks_forms", allok,
      "in block (j,s2,s3): g8 = s3(Pauli), g8g1 = -i sigma2, g8g4 = j sigma1, B = j s2, C = s2 sigma2, "
      "BC = j sigma2, g4g1 = -j sigma3, B g8 = j s2 sigma3, J = j, K1 = i s2, K2 = i s3 (all block diagonal)")
nb_ok = not blockform(g2)[1] and not blockform(g5)[1] and not blockform(g8 * g2)[1] and blockform(g1)[1]
check("blocks_not_everything_block_diagonal", nb_ok,
      "gamma^(x2), gamma^(x5), gamma^(x8)gamma^(x2) are not block diagonal (they anticommute with J), gamma^(x1) is; "
      "the reduction uses k along x1 "
      "(rotational invariance, check rotation_invariance)")
YG = sp.simplify(V.H * Gam * V)
pairs = [(a, b) for a in range(8) for b in range(8) if not YG[2 * a:2 * a + 2, 2 * b:2 * b + 2].is_zero_matrix]
gam_ok = pairs == [(0, 4), (1, 5), (2, 6), (3, 7), (4, 0), (5, 1), (6, 2), (7, 3)] and all(
    YG[2 * a:2 * a + 2, 2 * b:2 * b + 2] == labels[a][1] * s2 for (a, b) in pairs)
check("blocks_relation_to_Gamma", gam_ok and (Gam * J + J * Gam).is_zero_matrix
      and (Gam * K1 - K1 * Gam).is_zero_matrix and (Gam * K2 - K2 * Gam).is_zero_matrix,
      "Gamma anticommutes with J and commutes with K1, K2: it maps block (j,s2,s3) onto (-j,s2,s3); "
      "in the basis V its 2x2 entries between paired blocks are s2 sigma2: Gamma V_beta = s2 V_{beta'} sigma2")

# block Hamiltonian from the 16-component h (k along x1)
jj = sp.Symbol("j")
yv = sp.Symbol("y", real=True)
kp = sp.Symbol("kappa", positive=True)
ok_h = True
for i, (j, a, b) in enumerate(labels):
    Vb = V[:, 2 * i:2 * i + 2]
    for Mat, expct in [(mat_dy, -sp.I * j * s1), (mat_k[0], j * s3), (mat_M, j * s2)]:
        ok_h &= sp.simplify(Vb.H * Mat * Vb - expct).is_zero_matrix
check("block_hamiltonian", ok_h,
      "h_16 restricted to block (j,s2,s3), k = (k,0,0): h_j = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v; "
      "equivalently chi' = N chi, N = M sigma3 - kappa k sigma2 + i j (epsilon - v) sigma1")
Nmat = lambda j, M, k, e, v, kk: M * s3 - kk * k * s2 + sp.I * j * (e - v) * s1
hj = lambda j, M, k, v, kk: j * (M * s2 + kk * k * s3)          # algebraic part
ok_N = True
for j in (1, -1):
    # h chi = eps chi  <=>  chi' = N chi : -i j sigma1 chi' = (eps - v - j(M s2 + k kap s3)) chi
    lhs_ = -sp.I * j * s1 * Nmat(j, Ms, hk, eps, vs, kp)
    rhs_ = (eps - vs) * I2 - hj(j, Ms, hk, vs, kp)
    ok_N &= sp.simplify(lhs_ - rhs_).is_zero_matrix
check("block_ode_equivalent", ok_N, "h_j chi = epsilon chi is equivalent to chi' = N chi for j = +-1")
ok_sym = sp.simplify(-(hj(1, Ms, hk, 0, kp)) - hj(-1, Ms, hk, 0, kp)).is_zero_matrix and \
    sp.simplify(s3 * (-sp.I * s1) * s3 + (-sp.I * s1)).is_zero_matrix
check("block_type_relation", ok_sym and sp.simplify(s3 * hj(1, Ms, hk, 0, kp) * s3 - hj(-1, Ms, -hk, 0, kp)).is_zero_matrix,
      "h_{-1} - v = -(h_{+1} - v) (spectra mirrored); sigma3 h_j(k) sigma3 = h_{-j}(-k): the (j,k) and (-j,-k) "
      "orbitals are degenerate, chi_{-j,-k} = sigma3 chi_{j,k}")
ok_gam = sp.simplify(s2 * hj(1, Ms, hk, 0, kp) * s2 - hj(-1, -Ms, hk, 0, kp)).is_zero_matrix and \
    sp.simplify(s2 * (-sp.I * s1) * s2 - (sp.I * s1)).is_zero_matrix
check("block_Gamma_map", ok_gam,
      "sigma2 h_j(M, k) sigma2 = h_{-j}(-M, k) (the block form of Gamma): Gamma maps a solution of block type j "
      "with mass M onto block type -j with mass -M at the same k and epsilon (v fixed); it exchanges "
      "chi2(0) = 0 and chi1(0) = 0 (the two brane parities)")
# rotation invariance: spinor rotation by angle th in the x1-x2 plane
th = sp.Symbol("theta", real=True)
R12 = sp.cos(th / 2) * I16 + sp.sin(th / 2) * g1 * g2
kg = lambda k_: k_[0] * g1 + k_[1] * g2 + k_[2] * g3
rot_ok = sp.simplify(R12 * kg((hk, 0, 0)) * R12.inv() - kg((hk * sp.cos(th), -hk * sp.sin(th), 0))).is_zero_matrix \
    or sp.simplify(R12 * kg((hk, 0, 0)) * R12.inv() - kg((hk * sp.cos(th), hk * sp.sin(th), 0))).is_zero_matrix
rot_ok &= all((R12 * Mx - Mx * R12).is_zero_matrix for Mx in (g8, g4, B, C))
check("rotation_invariance", rot_ok,
      "the spinor rotation cos(th/2) + sin(th/2) g1 g2 commutes with g8, g4, B, C and rotates k.gamma: the "
      "spectrum depends on |k| only; every computation may take k = (k, 0, 0)")

# ---------------------------------------------------------------------------------------------
# E. Exchange: the uniform 8-fold gas (Hartree-Fock, U = lambda/2 S^2, angular averaging)
# ---------------------------------------------------------------------------------------------
lam, nn, SS, QQ, YY = sp.symbols("lambda n S Q Ycur", real=True)
E_ = sp.Symbol("E", positive=True)
p = sp.symbols("p1 p2 p3 p8", real=True)
hp = Ms * (-sp.I * g4) - (p[0] * g4 * g1 + p[1] * g4 * g2 + p[2] * g4 * g3 + p[3] * g4 * g8)
Esq = Ms ** 2 + sum(q ** 2 for q in p)
ok_sq = sp.simplify(hp * hp - Esq * I16).is_zero_matrix
Gp = (I16 + hp / E_) / 2
ok_proj = sp.simplify((Gp * Gp - Gp).subs(E_, sp.sqrt(Esq))).is_zero_matrix and Gp.H == Gp.subs(sp.I, sp.I) and \
    sp.simplify(Gp.trace().subs(E_, sp.sqrt(Esq))) == 8
check("gas_mode_projector", ok_sq and ok_proj,
      "flat good-sector plane waves e^{-i eps x4 + i p.x} (p in the four space-like directions x1,x2,x3,x8): "
      "h_p = M(-i g4) - p_a g4 g^a, h_p^2 = (M^2 + p^2) 1: eps = +-E, each 8-fold (the 8-fold gas); "
      "G_p = (1 + h_p/E)/2 is the Hermitian rank-8 projector on the positive-energy modes")
# angular average over S^2 (3-space) and over the y-momentum sign: explicit integrals
thv, phv = sp.symbols("vartheta varphi", real=True)
pr = sp.Symbol("prad", positive=True)
pdir = (pr * sp.sin(thv) * sp.cos(phv), pr * sp.sin(thv) * sp.sin(phv), pr * sp.cos(thv))
rho_p = Gp.subs({p[0]: pdir[0], p[1]: pdir[1], p[2]: pdir[2], p[3]: 0}) * B
avg = rho_p.applyfunc(lambda e: sp.integrate(sp.integrate(e * sp.sin(thv), (phv, 0, 2 * sp.pi)), (thv, 0, sp.pi))
                      / (4 * sp.pi))
check("gas_angular_average", sp.simplify(avg - (B + Ms / E_ * C) / 2).is_zero_matrix,
      "the angular average over S^2 of the one-body matrix G_p B of the 8 modes at momentum p is (B + (M/E) C)/2; "
      "the terms linear in p vanish (also for a y-momentum averaged over +-p8); only p -> -p symmetry is needed")
rho_m = ((I16 - hp.subs({q: 0 for q in p}) / E_) / 2) * B
check("gas_negative_energy_modes", sp.simplify(rho_m - (B - Ms / E_ * C) / 2).is_zero_matrix,
      "occupied negative-energy modes give (B - (M/E) C)/2: the local one-body matrix of ANY p -> -p symmetric "
      "occupation (any temperature, Mermin) has the form rho = (n B + S C)/16")
rho = (nn * B + SS * C) / 16
ok_ns = sp.simplify((B * rho).trace() - nn) == 0 and sp.simplify((C * rho).trace() - SS) == 0
check("gas_densities", ok_ns,
      "with <Psi^dagger M Psi> = Tr(M rho), rho = sum_occ f u u^dagger B (the expectation-value rule u^dagger B M u): "
      "number density n = <Psi^dagger B Psi> = Tr(B rho), scalar density S = <Psibar Psi> = Tr(C rho)")
# Wick: <:S^2:> = (Tr C rho)^2 - Tr(C rho C rho) -- verify with an explicit quasi-free 2-mode state
ok_wick = True
u1 = sp.Matrix([sp.Rational(1, 2), sp.I / 2, 0, 0, 0, 0, 0, 0, sp.Rational(1, 2), 0, 0, 0, 0, 0, -sp.I / 2, 0])
u2 = sp.Matrix([0, 0, sp.Rational(1, 2), 0, sp.Rational(-1, 2), 0, 0, 0, 0, 0, sp.I / 2, 0, 0, 0, 0, sp.I / 2])
# two-particle Slater determinant amplitude in the Krein rule: f_AB = <Psi_A^dag Psi_B> = rho_BA
rh = (u1 * u1.H + u2 * u2.H) * B
direct = (C * rh).trace() ** 2
exch = (C * rh * C * rh).trace()
# brute force: <:S S:> = sum C_AB C_CD (f_AB f_CD - f_AD f_CB)
f = rh.T
bf = sum(C[A, Bq] * C[Cq, D] * (f[A, Bq] * f[Cq, D] - f[A, D] * f[Cq, Bq])
         for A in range(16) for Bq in range(16) for Cq in range(16) for D in range(16)
         if C[A, Bq] != 0 and C[Cq, D] != 0)
ok_wick = sp.simplify(bf - (direct - exch)) == 0
check("hf_wick_contraction", ok_wick,
      "quasi-free state with one-body function f_AB = <Psi_A^dag Psi_B> = rho_BA: "
      "<:S^2:> = sum C_AB C_CD (f_AB f_CD - f_AD f_CB) = (Tr C rho)^2 - Tr(C rho C rho) (verified by brute force "
      "on an explicit two-mode state)")
ex = sp.factor(-lam / 2 * (C * rho * C * rho).trace())
check("exchange_uniform_gas", sp.simplify(ex + lam / 32 * (nn ** 2 + SS ** 2)) == 0,
      f"e_x = -(lambda/2) Tr(C rho C rho) = {ex} for rho = (nB + SC)/16 (C B C = B, Tr BC = 0): exactly local in "
      "(n, S) at every temperature; Hartree e_H = (lambda/2) S^2")
eH = lam / 2 * SS ** 2
eint = eH + ex
Meff = sp.diff(eint, SS)
vv = sp.diff(eint, nn)
ok_pot = sp.simplify(Meff - sp.Rational(15, 16) * lam * SS) == 0 and sp.simplify(vv + lam * nn / 16) == 0
check("ks_potentials", ok_pot,
      "e_int = e_H + e_x = (15/32) lambda S^2 - (1/32) lambda n^2; M_eff = m + d e_int/dS = m + (15/16) lambda S, "
      "v_v = d e_int/dn = -lambda n/16 (enters h as + v_v 1, the covariant equation as -i v_v gamma^(x4))")
ok_hom = sp.simplify(SS * Meff + nn * vv - eint - eint) == 0
check("ks_onshell_lagrangian", ok_hom,
      "on shell <L>/sqrt|g| = M_eff S + v_v n - m S - e_int = e_int (e_int homogeneous of degree 2), i.e. the "
      "operator identity <L> = <U> on shell evaluated in Hartree-Fock")
check("filled_shell_ratio", sp.simplify((-lam / 32 * (8 ** 2 + 8 ** 2)) / (lam / 2 * 8 ** 2) + sp.Rational(1, 8)) == 0,
      "one filled 8-fold level at rest (n = S = 8 per unit volume): E_x/E_H = -1/8")

# exact Fock exchange of the slab Kohn-Sham determinant (closed shells)
c0, c1, c2, c3 = sp.symbols("d0 d1 d2 d3", real=True)
Dm = (c0 * I2 + c1 * s1 + c2 * s2 + c3 * s3) / 2
Gsl = sp.zeros(16)
for b, (j, a, bb) in enumerate(labels):
    Vb = V[:, 2 * b:2 * b + 2]
    Gsl += Vb * (Dm if j == 1 else s3 * Dm * s3) * Vb.H
Xs = sp.Matrix(16, 16, sp.symbols("x0:256"))
eqs = []
for Lg in (g1 * g2, g1 * g3, g2 * g3):
    eqs += list(Lg * Xs - Xs * Lg)
sol = list(sp.linsolve(eqs, list(Xs)))[0]
Xsol = sp.Matrix(16, 16, list(sol))
free = sorted(Xsol.free_symbols, key=lambda s_: int(str(s_)[1:]))
basis = [Xsol.subs({fz: (1 if fz == ff else 0) for fz in free}) for ff in free]
Gram = sp.Matrix(len(basis), len(basis), lambda i, k_: (basis[i].H * basis[k_]).trace())
coef = Gram.LUsolve(sp.Matrix([(bb_.H * Gsl).trace() for bb_ in basis]))
Gavg = sp.simplify(sum((c_ * bb_ for c_, bb_ in zip(coef, basis)), Z16))
rs = Gavg * B
n_s = sp.simplify((B * rs).trace())
S_s = sp.simplify((C * rs).trace())
Q_s = sp.simplify((B * g8 * rs).trace())
exs = sp.expand(-lam / 2 * (C * rs * C * rs).trace())
ok_slab = len(basis) == 64 and n_s == 8 * c0 and S_s == 8 * c2 and Q_s == 8 * c3 and \
    sp.simplify(exs + lam / 32 * (n_s ** 2 + S_s ** 2 - Q_s ** 2 - (8 * c1) ** 2)) == 0
check("exchange_slab_exact_fock", ok_slab,
      "a level with 2x2 density D = (d0 + d1 s1 + d2 s2 + d3 s3)/2 in each of the 4 blocks of type j = +1 and "
      "sigma3 D sigma3 in the 4 blocks of type -1 (the degenerate (-j,-k) partners), averaged over a k -> -k closed "
      "shell (= the projection onto the 64-dim commutant of the 3-space rotations; End(16) carries only spin 0 and 1): "
      "n = 8 d0, S = 8 d2, Q = <Psi^dag B g8 Psi> = 8 d3; exact local Fock exchange -(lambda/32)(n^2 + S^2 - Q^2 - Y^2), "
      "Y = 8 d1 the y-current (zero for eigen-orbitals). The uniform-gas e_x omits +(lambda/32) Q^2.")

# ---------------------------------------------------------------------------------------------
# F. Boundary conditions
# ---------------------------------------------------------------------------------------------
Mf, vf, kf = sp.Function("M", real=True)(yv), sp.Function("v", real=True)(yv), sp.exp(-H * yv - a0s)
c1f, c2f = sp.Function("chi1")(yv), sp.Function("chi2")(yv)
ch = sp.Matrix([c1f, c2f])
ok_PA = True
for j in (1, -1):
    N_ = lambda yy_, M_, v_, kk_: M_ * s3 - kk_ * hk * s2 + sp.I * j * (eps - v_) * s1
    # chi~(y) = sigma3 chi(-y): chi~' = -sigma3 N(-y) sigma3 chi~
    Nt = -s3 * N_(-yv, Mf.subs(yv, -yv), vf.subs(yv, -yv), kf.subs(yv, -yv)) * s3
    ok_PA &= sp.simplify(Nt - N_(yv, -Mf.subs(yv, -yv), vf.subs(yv, -yv), kf.subs(yv, -yv))).is_zero_matrix
check("bc_mirror_map_PA", ok_PA,
      "the reflection P_A: chi(y) -> sigma3 chi(-y) = gamma^(x8) chi(-y) maps a solution with (M(y), v(y), kappa(y)) "
      "onto one with (-M(-y), v(-y), kappa(-y)); with the Z2 mirror warp W = e^{-H|y|}, kappa(-y) is the mirror's "
      "kappa: P_A is a symmetry of the doubled problem iff M_eff is odd across y = 0")
dens = {"n": I2, "s": s2, "Q": s3, "c": s1}
par = {nm: sp.simplify((s3 * Mx * s3 - Mx)).is_zero_matrix for nm, Mx in dens.items()}
check("bc_mirror_parities_of_densities", par == {"n": True, "s": False, "Q": True, "c": False},
      "under P_A: n and Q even, S and the y-current odd; hence M_eff = m + (15/16) lambda S odd requires the mirror "
      "copy to carry (-m, +lambda) (v_v = -lambda n/16 even, same lambda): the (+m, -m) mirror pair (SPEC T3)")
cur = sp.expand((ch.H * s1 * ch)[0])
ok_bc = sp.simplify(cur.subs(c2f, 0)) == 0 and sp.simplify(cur.subs(c1f, 0)) == 0
check("bc_brane_parity_conditions", ok_bc,
      "ASSUMED Z2 mirror (orbifold under P_A): continuity of Psi(-y) = +-gamma^(x8) Psi(y) at y = 0 gives "
      "(1 -+ gamma^(x8)) chi(0) = 0, in every block chi2(0) = 0 (even) or chi1(0) = 0 (odd); both kill the y-current "
      "chi^dag sigma1 chi; real form chi = (a, i b): b(0) = 0 or a(0) = 0")
phi = sp.Matrix([sp.Function("phi1")(yv), sp.Function("phi2")(yv)])
ok_bt = True
for j in (1, -1):
    hop = lambda w: j * (-sp.I * s1 * sp.diff(w, yv) + Mf * s2 * w + kf * hk * s3 * w) + vf * w
    lhs_b = (phi.H * hop(ch))[0] - (hop(phi).H * ch)[0]
    ok_bt &= sp.simplify(sp.expand(lhs_b - sp.diff(-sp.I * j * (phi.H * s1 * ch)[0], yv))) == 0
check("bc_self_adjoint_boundary_term", ok_bt,
      "phi^dag h_j chi - (h_j phi)^dag chi = d/dy[-i j phi^dag sigma1 chi] pointwise: with current-killing "
      "conditions at both ends h_j is self-adjoint in the flat measure int dy (levels real, orbitals orthogonal)")
thq = sp.Symbol("theta", real=True)
Qt = sp.cos(thq) * s3 + sp.sin(thq) * s2
ok_Q = sp.simplify(Qt * Qt - I2).is_zero_matrix and Qt.H == Qt and sp.simplify(Qt * s1 + s1 * Qt).is_zero_matrix
check("bc_tip_family", ok_Q,
      "tip family (1 - Q(theta)) chi(-L) = 0, Q = cos(theta) sigma3 + sin(theta) sigma2 (16-component: "
      "cos(theta) gamma^(x8) + i sin(theta) gamma^(x8) gamma^(x1)): Q^dag = Q, Q^2 = 1, {Q, sigma1} = 0, so the "
      "current vanishes; canonical theta = 0: chi2(-L) = 0 (b(-L) = 0)")
# current conservation along y on solutions, Hilbert density not conserved
ok_cc = True
for j in (1, -1):
    Nn = Ms * s3 - kp * hk * s2 + sp.I * j * (eps - vs) * s1
    ok_cc &= sp.simplify(Nn.H * s1 + s1 * Nn).is_zero_matrix
    nonc = sp.simplify(Nn.H + Nn)
check("bc_current_conserved_along_y", ok_cc and not nonc.is_zero_matrix,
      "N^dag sigma1 + sigma1 N = 0 for real (epsilon, M, v, kappa k): chi^dag sigma1 chi is constant in y on every "
      "solution (so zero everywhere for an eigen-orbital); N + N^dag = 2M sigma3 - 2 kappa k sigma2 != 0: "
      "the Hilbert density chi^dag chi is not")
# exact k = 0 spectra (constant M, v = 0)
Lc = sp.Symbol("L", positive=True)
nI = sp.Symbol("nI", integer=True, positive=True)
ok_k0 = True
for j in (1, -1):
    # real form a' = M a - (kap k + j e) b, b' = (j e - kap k) a - M b ; k = 0
    a_, b_ = sp.exp(Ms * yv), sp.Integer(0)
    ok_k0 &= sp.simplify(sp.diff(a_, yv) - Ms * a_) == 0
    pn = nI * sp.pi / Lc
    en = sp.sqrt(Ms ** 2 + pn ** 2)
    bsol = sp.sin(pn * yv)
    asol = (sp.diff(bsol, yv) + Ms * bsol) / (j * en)
    ok_k0 &= sp.simplify(sp.diff(asol, yv) - (Ms * asol - j * en * bsol)) == 0
    ok_k0 &= sp.simplify(bsol.subs(yv, 0)) == 0 and sp.simplify(bsol.subs(yv, -Lc)) == 0
pp = sp.Symbol("p", positive=True)
ao = sp.sin(pp * yv)
eo = sp.sqrt(Ms ** 2 + pp ** 2)
bo = (Ms * ao - sp.diff(ao, yv)) / eo        # j = +1
ok_odd = sp.simplify(sp.diff(bo, yv) - (eo * ao - Ms * bo)) == 0 and \
    sp.simplify(bo.subs(yv, -Lc) * eo - (-Ms * sp.sin(pp * Lc) - pp * sp.cos(pp * Lc))) == 0
check("bc_exact_k0_spectra", ok_k0 and ok_odd,
      "k = 0, constant M > 0, v = 0, tip theta = 0: even parity: chiral zero mode epsilon = 0, chi = (e^{My}, 0) "
      "(brane-localised, every L) and epsilon = +-sqrt(M^2 + (n pi/L)^2), chi2 ~ sin(n pi y/L); odd parity: "
      "epsilon^2 = M^2 + p^2 with M sin(pL) + p cos(pL) = 0, i.e. tan(pL) = -p/M; each level 4-fold per j")
# regular tip: asymptotic branches for k != 0
Nas = -kp * hk * s2
vdec = sp.Matrix([1, -sp.I])
ok_tip = sp.simplify(Nas * vdec - kp * hk * vdec).is_zero_matrix and sp.simplify(s2 * vdec + vdec).is_zero_matrix
check("bc_tip_asymptotics", ok_tip,
      "as y -> -inf, kappa(y) = e^{-Hy-a4} -> inf and N -> -kappa k sigma2: the branches are chi ~ exp(+- k kappa/H) "
      "times the sigma2 = -+1 eigenvectors; the regular (decaying toward the tip, k > 0) branch is sigma2 chi = -chi. "
      "An orbital with k != 0 is suppressed at the tip like exp(-|k|(kappa(-L) - kappa(y))/H), so for k != 0 any "
      "current-killing tip condition gives the same levels up to that factor; the tip condition matters for k = 0, "
      "where theta = 0 selects the regular brane-localised zero mode e^{My} and admits no tip-localised mode for M > 0")

# ---------------------------------------------------------------------------------------------
# G. Exact a4-rescaling identity between slices
# ---------------------------------------------------------------------------------------------
aa = sp.Symbol("a", real=True)
hfull = lambda j, k_, a_: j * (Ms * s2 + sp.exp(-H * yv - a_) * k_ * s3)
ok_resc = all(sp.simplify(hfull(j, hk, aa) - hfull(j, hk * sp.exp(-aa), 0)).is_zero_matrix for j in (1, -1))
ell, vt = sp.symbols("ell v_t", positive=True)
norm = lambda l_, v_: sp.exp(-6 * H * yv) / (l_ ** 3 * v_)
ok_norm = sp.simplify(norm(ell, vt) - norm(ell * sp.exp(aa), vt * sp.exp(-3 * aa))) == 0
ok_lam = sp.simplify(lam * norm(ell, vt) - lam * sp.exp(3 * aa) * norm(ell * sp.exp(aa), vt)) == 0
check("rescaling_identity", ok_resc and ok_norm and ok_lam,
      "a4,0 enters h only through kappa k = e^{-Hy}(k e^{-a4,0}); the lattice k = Delta k n at slice a4,0 is the "
      "lattice Delta k e^{-a4,0} at slice 0. The proper density factor e^{-6Hy}/(ell^3 v_t) is invariant under "
      "(ell, v_t) -> (ell e^{a}, v_t e^{-3a}) (same proper boxes). Hence EXACTLY (Hartree, exchange, any T): "
      "KS(a4,0; Delta k, v_t, lambda) = KS(0; Delta k e^{-a4,0}, v_t e^{-3 a4,0}, lambda), all levels, orbitals, "
      "densities and EMT profiles equal; equivalently KS(0; Delta k e^{-a4,0}, v_t, lambda e^{3 a4,0}) with every "
      "proper density multiplied by e^{-3 a4,0} and the same levels")

# ---------------------------------------------------------------------------------------------
# H. Energy-momentum tensor of a Kohn-Sham orbital (16-component derivation, reduced to blocks)
# ---------------------------------------------------------------------------------------------
Vol = sp.Symbol("Vol", positive=True)
fr = [sp.Function(f"f{i}", real=True)(Y) for i in range(4)]
chi_b = sp.Matrix([fr[0] + sp.I * fr[1], fr[2] + sp.I * fr[3]])
emt_ok = True
emt_details = []
for bi in (0, 5):
    j, sa, sb = labels[bi]
    Vb = V[:, 2 * bi:2 * bi + 2]
    u = sp.exp(-sp.I * eps * x4 + sp.I * hk * X[0]) * W ** -3 * Vb * chi_b / sp.sqrt(Vol)
    BC_ = B * C

    def Kdiag(mu):
        gm = g[mu] / hv[mu]
        Du = sp.diff(u, X[mu]) + Om[mu] * u
        du = sp.diff(u, X[mu])
        val = (u.H * BC_ * gm * Du)[0] - (du.H * BC_ * gm * u)[0] + (u.H * BC_ * Om[mu] * gm * u)[0]
        return sp.simplify(sp.expand(val / 2))

    def Koff(mu, nu):        # K_mu nu with lower indices, symmetrised
        gl = lambda m_: eta[m_] * hv[m_] * g[m_]          # gamma_mu = g_mu nu gamma^nu = eta h gamma^a
        Dm = lambda m_: sp.diff(u, X[m_]) + Om[m_] * u
        dm = lambda m_: sp.diff(u, X[m_])
        t = 0
        for (m_, n_) in ((mu, nu), (nu, mu)):
            t += (u.H * BC_ * gl(m_) * Dm(n_))[0] - (dm(n_).H * BC_ * gl(m_) * u)[0] + (u.H * BC_ * Om[n_] * gl(m_) * u)[0]
        return sp.simplify(sp.expand(t / 4))

    # ODE substitution: chi' = N chi with constant M, v (local values) -- derivatives of f's
    Nn = Ms * s3 - kap * hk * s2 + sp.I * j * (eps - vs) * s1
    dch = Nn * chi_b
    subsd = {sp.diff(fr[0], Y): sp.re(dch[0]), sp.diff(fr[1], Y): sp.im(dch[0]),
             sp.diff(fr[2], Y): sp.re(dch[1]), sp.diff(fr[3], Y): sp.im(dch[1])}
    nc = (chi_b.H * chi_b)[0]
    sc = (chi_b.H * (j * s2) * chi_b)[0]
    tc = (chi_b.H * (j * s3) * chi_b)[0]
    cc = (chi_b.H * (j * s1) * chi_b)[0]
    pref = sp.exp(-6 * H * Y) / Vol
    K11 = Kdiag(0)
    K44 = Kdiag(3)
    K55 = Kdiag(4)
    K22 = Kdiag(1)
    Kyy = Kdiag(7).subs(subsd)
    e1 = sp.simplify(sp.expand(-K11 - pref * kap * hk * tc))
    e4 = sp.simplify(sp.expand(K44 - pref * eps * nc))
    e5 = sp.simplify(K55) == 0 and sp.simplify(K22) == 0
    ey = sp.simplify(sp.expand(-Kyy - pref * ((eps - vs) * nc - Ms * sc - kap * hk * tc)))
    K4y = Koff(3, 7).subs(subsd)
    K4y_val = sp.simplify(sp.expand(K4y * Vol * sp.exp(6 * H * Y)))
    e4y = sp.simplify(sp.expand(K4y_val - (eps - vs / 2) * cc))
    ok_b = e1 == 0 and e4 == 0 and e5 and ey == 0 and e4y == 0
    emt_ok &= ok_b
    emt_details.append(f"block {bi} {labels[bi]}: K11 {e1 == 0}, K44 {e4 == 0}, K22=K55=0 {e5}, Kyy {ey == 0}, "
                       f"K_x4y = P (eps - v/2) c {e4y == 0}")
check("emt_orbital_components", emt_ok,
      "K^mu_mu(no sum) = (1/2)[Psibar g^mu D_mu Psi - (D_mu Psibar) g^mu Psi] in the expectation rule, for "
      "Psi = e^{-i eps x4 + i k x1} W^{-3} V_beta chi /sqrt(ell^3 v_t), a4 = a4(x4) general (the spin connection, "
      "including its a4' pieces, drops out of every diagonal component): -K^x1_x1 = P kappa k chi^dag j s3 chi, "
      "K^x4_x4 = P eps chi^dag chi, K^x2_x2 = K^x5_x5 = 0, -K^y_y = P[(eps - v) chi^dag chi - M chi^dag j s2 chi "
      "- kappa k chi^dag j s3 chi] (on shell), P = e^{-6Hy}/(ell^3 v_t); K_x4y = P (eps - v/2) chi^dag j s1 chi "
      "(zero for eigen-orbitals). " + "; ".join(emt_details))
# trace identity
tc_, nc_, sc_ = sp.symbols("t n_o s_o", real=True)
trace_ = (-kap * hk * tc_) + eps * nc_ + (Ms * sc_ + kap * hk * tc_ - (eps - vs) * nc_)
check("emt_trace_identity", sp.simplify(trace_ - (Ms * sc_ + vs * nc_)) == 0,
      "sum_mu K^mu_mu = M_eff s + v_v n per orbital (K^1+K^4+K^y), the on-shell trace; with <L> = e_int: "
      "T^mu_nu = -<K^mu_nu> + delta^mu_nu e_int (SPEC sign: rho = -T^x4_x4, p_mu = T^mu_mu; homogeneous classical "
      "limit rho = mS + U, p = S U' - U)")
# conservation along y (external M(y), v(y)) for one orbital, and self-consistent cancellation
Mx_, vx_ = sp.Function("M", real=True)(Y), sp.Function("v", real=True)(Y)
for j in (1,):
    Nn = Mx_ * s3 - kap * hk * s2 + sp.I * j * (eps - vx_) * s1
    dch = Nn * chi_b
    subsd = {sp.diff(fr[0], Y): sp.re(dch[0]), sp.diff(fr[1], Y): sp.im(dch[0]),
             sp.diff(fr[2], Y): sp.re(dch[1]), sp.diff(fr[3], Y): sp.im(dch[1])}
    nc = sp.expand((chi_b.H * chi_b)[0])
    sc = sp.expand((chi_b.H * (j * s2) * chi_b)[0])
    tc = sp.expand((chi_b.H * (j * s3) * chi_b)[0])
    p8c = (eps - vx_) * nc - Mx_ * sc - kap * hk * tc
    lhs_c = sp.diff(p8c, Y).subs(subsd)
    rhs_c = H * kap * hk * tc - sp.diff(vx_, Y) * nc - sp.diff(Mx_, Y) * sc
    ok_c = sp.simplify(sp.expand(lhs_c - rhs_c)) == 0
check("emt_y_conservation_orbital", ok_c,
      "for one orbital in external M(y), v(y) (coordinate densities, P without e^{-6Hy}): "
      "d/dy[(eps - v) n_c - M s_c - kappa k t_c] = H kappa k t_c - v' n_c - M' s_c")
p3f, ptf, p8f, rhof = [sp.Function(nm)(Y) for nm in ("p3", "pt", "p8", "rho")]
Tmix = sp.diag(p3f, p3f, p3f, -rhof, ptf, ptf, ptf, p8f)
divy = sum(sp.diff(Tmix[m, 7], X[m]) for m in range(8)) + sum(Chr[m][m][l] * Tmix[l, 7] for m in range(8) for l in range(8)) \
    - sum(Chr[l][m][7] * Tmix[m, l] for m in range(8) for l in range(8))
ok_dy = sp.simplify(divy - (sp.diff(p8f, Y) + 6 * H * p8f - 3 * H * (p3f + ptf))) == 0
nS, nN = sp.Function("S")(Y), sp.Function("n")(Y)
e_int_f = sp.Rational(15, 32) * lam * nS ** 2 - lam * nN ** 2 / 32
force = -sp.diff(sp.Rational(15, 16) * lam * nS, Y) * nS - sp.diff(-lam * nN / 16, Y) * nN + sp.diff(e_int_f, Y)
check("emt_y_conservation_selfconsistent", ok_dy and sp.simplify(force) == 0,
      "nabla_mu T^mu_y = p8' + 6H p8 - 3H (p3 + p_t) for diagonal T(y); summing the orbital identity over a closed "
      "shell (3 p3_kin = kappa |k| t) and adding e_int, the force terms -M' S - v' n + e_int' cancel exactly for the "
      "self-consistent M_eff, v_v: every self-consistent KS state with these potentials satisfies nabla_mu T^mu_y = 0")
div4 = sum(sp.diff(Tmix[m, 3], X[m]) for m in range(8)) + sum(Chr[m][m][l] * Tmix[l, 3] for m in range(8) for l in range(8)) \
    - sum(Chr[l][m][3] * Tmix[m, l] for m in range(8) for l in range(8))
check("emt_x4_component", sp.simplify(div4 - (-sp.diff(rhof, x4) - 3 * a4p * (p3f - ptf))) == 0,
      "with a4 = a4(x4): nabla_mu T^mu_x4 = -d_x4 rho - 3 a4' (p3 - p_t) (+ the y-flux divergence, zero for the "
      "instantaneous states): the energy of the 7-volume changes as dE/dx4 = -3 a4' int sqrt|g| (p3 - p_t)")
# Hellmann-Feynman / rescaling: d eps/da = <d_a h> = -k <j kappa sigma3> = -k d eps/dk
ef = sp.Function("eps0")
check("adiabatic_hellmann_feynman", sp.simplify(sp.diff(ef(hk * sp.exp(-aa)), aa)
                                                + hk * sp.diff(ef(hk * sp.exp(-aa)), hk)) == 0
      and sp.simplify(sp.diff(hfull(1, hk, aa), aa) + hk * sp.diff(hfull(1, hk, aa), hk)).is_zero_matrix,
      "d_a h_j = -j kappa k sigma3 = -k d_k h_j; for the free (frozen-potential) problem eps(k, a) = eps(k e^{-a}, 0) so "
      "d eps/da = -k d eps/dk = -k <j kappa sigma3>; summed with occupations: dE/da = -3 ell^3 v_t int e^{6Hy} "
      "(p3 - p_t) dy (Hellmann-Feynman, fixed occupations)")
# adiabaticity: off-diagonal identity on an explicit example
aS = sp.Symbol("a", real=True)
Hex = sp.Matrix([[sp.cos(aS), sp.sin(aS)], [sp.sin(aS), -sp.cos(aS)]]) * 2 + sp.Matrix([[1, 0], [0, 1]])
evs = Hex.eigenvects()
(e_a, _, [va]), (e_b, _, [vb]) = evs[0], evs[1]
va, vb = va / sp.sqrt((va.H * va)[0]), vb / sp.sqrt((vb.H * vb)[0])
lhs_ad = sp.simplify((va.H * Hex.diff(aS) * vb)[0])
rhs_ad = sp.simplify((e_b - e_a) * (va.H * vb.diff(aS))[0])
check("adiabatic_offdiagonal_identity", sp.simplify(lhs_ad - rhs_ad) == 0,
      "<n| d_a h |m> = (eps_m - eps_n) <n| d_a m> (differentiated eigen-equation; verified on an explicit family); "
      "measure along a4 = A H x4: Q_nm = A H |<n| d_a h_KS |m>| / (eps_n - eps_m)^2 for n occupied, m empty, "
      "same (k, block, parity); leading-order transition probability ~ Q_nm^2")

# brane-band slope c: exact formula and an independent numerical shooting check
Mn, Hn, Ln = 1.0, 1.0, 3.0
c_exact = lambda a_, M_, H_, L_: math.exp(-a_) * (2 * M_ / (2 * M_ - H_)) * (1 - math.exp(-(2 * M_ - H_) * L_)) / (1 - math.exp(-2 * M_ * L_))
c_formula_sym = sp.simplify(sp.integrate(sp.exp(-H * yv - aa) * sp.exp(2 * Ms * yv), (yv, -Lc, 0))
                            / sp.integrate(sp.exp(2 * Ms * yv), (yv, -Lc, 0)))
c_target = sp.exp(-aa) * 2 * Ms / (2 * Ms - H) * (1 - sp.exp(-(2 * Ms - H) * Lc)) / (1 - sp.exp(-2 * Ms * Lc))
ok_csym = sp.simplify(c_formula_sym.subs({Ms: 1, H: 1, Lc: 3}) - c_target.subs({Ms: 1, H: 1, Lc: 3})) == 0 and \
    sp.simplify(c_target.subs({Ms: 1, H: 1, Lc: 3, aa: 0}) - 2 / (1 + sp.exp(-3))) == 0


def shoot(e, k, a_, j=1, M_=Mn, H_=Hn, L_=Ln, steps=6000):
    # real form a' = M a - (kap k + j e) b, b' = (j e - kap k) a - M b, from y = 0 with b(0) = 0 (even), to y = -L
    def f(y_, s_):
        kk = math.exp(-H_ * y_ - a_) * k
        return np.array([M_ * s_[0] - (kk + j * e) * s_[1], (j * e - kk) * s_[0] - M_ * s_[1]])
    hstep = -L_ / steps
    s_ = np.array([1.0, 0.0])
    y_ = 0.0
    for _ in range(steps):
        k1_ = f(y_, s_)
        k2_ = f(y_ + hstep / 2, s_ + hstep / 2 * k1_)
        k3_ = f(y_ + hstep / 2, s_ + hstep / 2 * k2_)
        k4_ = f(y_ + hstep, s_ + hstep * k3_)
        s_ = s_ + hstep / 6 * (k1_ + 2 * k2_ + 2 * k3_ + k4_)
        y_ += hstep
    return s_[1]            # b(-L): tip condition theta = 0


def zero_mode(k, a_):
    lo, hi = -0.5, 0.5
    flo = shoot(lo, k, a_)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        fm = shoot(mid, k, a_)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


t0 = time.time()
slopes = {}
for a_ in (0.0, 0.5):
    sl = []
    for kk_small in (2e-3, 1e-3):
        sl.append((zero_mode(kk_small, a_) - zero_mode(-kk_small, a_)) / (2 * kk_small))
    slopes[a_] = (4 * sl[1] - sl[0]) / 3          # Richardson: eps is odd in k, error O(k^2) removed
num_ok = all(abs(slopes[a_] - c_exact(a_, Mn, Hn, Ln)) < 1e-6 for a_ in slopes)
check("brane_band_slope", ok_csym and num_ok,
      f"first-order Hellmann-Feynman at k = 0 (zero mode e^{{My}}, theta = 0): d eps/dk = j c, "
      f"c = e^{{-a4,0}} (2M/(2M-H)) (1 - e^{{-(2M-H)L}})/(1 - e^{{-2ML}}); M = H = 1, L = 3: c = 2/(1+e^{{-3}}) = "
      f"{c_exact(0, 1, 1, 3):.10f}; independent RK4 shooting (6000 steps, k = +-1e-3 and +-2e-3 with Richardson extrapolation, j = +1): "
      f"slope {slopes[0.0]:.10f} at a4,0 = 0 and {slopes[0.5]:.10f} at a4,0 = 0.5 (exact {c_exact(0.5, 1, 1, 3):.10f}), "
      "the e^{-a4,0} rescaling")
print(f"shooting time {time.time() - t0:.1f} s")

# ---------------------------------------------------------------------------------------------
# I. Cross-check of the Wolfram export ks-theory.json
# ---------------------------------------------------------------------------------------------
if KS_THEORY.exists():
    kt = json.loads(KS_THEORY.read_text(encoding="utf-8"))
    conv = {"0": 0, "1": 1, "-1": -1, "I": sp.I, "-I": -sp.I}
    try:
        Ujson = sp.Matrix([[conv[str(e)] for e in row] for row in kt["blockBasis"]["unnormalisedColumns2Sqrt2V"]])
        same_basis = Ujson == U
    except Exception as exc:  # noqa: BLE001
        same_basis = False
    check("ks_theory_json_basis", same_basis,
          "the exported basis 2 sqrt2 V of ks-theory.json equals this file's construction entry by entry")
    try:
        exj = kt["exchange"]["uniformGas"]
        same_ex = sp.Rational(exj["coefficient_n2"]) == sp.Rational(-1, 32) and \
            sp.Rational(exj["coefficient_S2"]) == sp.Rational(-1, 32) and \
            sp.Rational(kt["exchange"]["kohnShamPotentials"]["Meff_coefficient_of_lambda_S"]) == sp.Rational(15, 16) and \
            sp.Rational(kt["exchange"]["kohnShamPotentials"]["vv_coefficient_of_lambda_n"]) == sp.Rational(-1, 16)
    except Exception:  # noqa: BLE001
        same_ex = False
    check("ks_theory_json_exchange", same_ex, "exchange coefficients -1/32, -1/32 and potentials 15/16, -1/16 agree")
    try:
        cj = kt["checksNumeric"]["braneBandSlope_M1_H1_L3_a0"]
        same_c = abs(float(cj) - c_exact(0, 1, 1, 3)) < 1e-12
    except Exception:  # noqa: BLE001
        same_c = False
    check("ks_theory_json_slope", same_c, "the exported brane-band slope agrees with this file to 1e-12")
else:
    check("ks_theory_json_basis", "pending", "ks-theory.json not yet written by the Wolfram verifier")

# ---------------------------------------------------------------------------------------------
summary = {"passed": sum(c["verdict"] == "PASS" for c in CHECKS),
           "failed": sum(c["verdict"] == "FAIL" for c in CHECKS),
           "other": sum(c["verdict"] not in ("PASS", "FAIL") for c in CHECKS),
           "total": len(CHECKS)}
out = {
    "report": "Revision Kohn-Sham theory (SPEC sections 1, 7): independent exact sympy derivation and checks",
    "producer": "Revision/kohn_sham/theory/check_ks_theory.py",
    "coordinates": "x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; "
                   "x8 = the hidden direction (proper coordinate y = ln(sin 6Hx8)/(6H) <= 0)",
    "summary": summary,
    "checks": CHECKS,
}
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_bytes((json.dumps(out, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
print(json.dumps(summary))
sys.exit(0 if summary["failed"] == 0 else 1)
