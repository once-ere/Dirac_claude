#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Independent numpy reference solver for the Stage-4 Kohn-Sham problem of
dirac16complex in the static primordial (warped, Z2-mirrored) field.

This program is the *second, independent* implementation demanded by
STAGE4_SPEC section 5: the Rust crate integrates the 2x2 system in y with
CVODE shooting; this file discretises the same Hermitian 2x2 operator by a
matrix method and diagonalises it.  Nothing is shared with the Rust code
except the exact algebra fixture (artifacts/dirac16complex/arbitrary-field/
algebra-fixture.json) and the physics conventions of CONTRACT.md,
NUMERICS_CONTRACT.md and STAGE4_SPEC.md.

Physics (units H = 1, a4_0 given; y in (-L, 0], brane at y = 0)
------------------------------------------------------------------
Ansatz Psi = exp(-i eps x4) exp(i k x1) W(y)^-3 chi(y), W = exp(H y):
    gamma^0 chi' + i k kappa(y) gamma^1 chi - i eps gamma^4 chi = M_eff(y) chi,
    kappa(y) = exp(-H y - a4_0).
With A0 = gamma^0, A1 = gamma^0 gamma^1, A4 = gamma^0 gamma^4 this is
chi' = [M A0 - i k kappa A1 + i eps A4] chi.  The commuting operators
J = A0 A1 A4 (J^2 = 1), i gamma^2 gamma^3, i gamma^5 gamma^6 split C^16 into
eight 2-dimensional joint eigenspaces; in each one the basis
(e1 = the A0 = +1 vector, e2 = A4 e1) gives EXACTLY (derived numerically
from the fixture in `block_reduction`, tolerance 1e-12 on integer data)
    A0 = sigma_z,  A4 = sigma_x,  A1 = s i sigma_y (s = eigenvalue of J),
    B = b 1  (b = J * i gamma^2 gamma^3 = +-1),  C = b sigma_y,
    B C = -i gamma^4 = sigma_y  in every block.
Hence the KS equation is the 2x2 Hermitian eigenproblem (block type s = +-1,
four blocks of each type)
    h_s chi = eps chi,   h_s = -i sigma_x d/dy + M_eff(y) sigma_y
                                 - s k kappa(y) sigma_z + v_x(y),
    chi = (f, g),  number density chi^dag chi = |f|^2 + |g|^2,
    scalar density chi^dag (B C) chi = chi^dag sigma_y chi = 2 Im(f* g),
    y-current -i Psibar gamma^y Psi -> chi^dag sigma_x chi = 2 Re(f* g),
    x1-current (frame) -> -s chi^dag sigma_z chi.
Complex conjugation maps h_{-s}(k) to -h_s(k): spec(-s, k) = -spec(s, k) and
the eigenvectors are complex conjugates, so ONE diagonalisation per
(k-shell, parity) gives both block types (`solve_shell`).  The 16-component
spectrum at k is therefore {eps_i} (x4) U {-eps_i} (x4); at k = 0 the two
types coincide and every level is 8-fold degenerate.
Boundary conditions.  Brane y = 0 (Z2): Psi(-y) = +- gamma^0 Psi(y), i.e.
(1 -+ sigma_z) chi(0) = 0: parity +1 <=> g(0) = 0, parity -1 <=> f(0) = 0
(parity 0: both sectors are solved and filled together as one system, the
convention of the Rust crate; the canonical reference runs use one sector).
Tip y = -L: the bag condition (1 + gamma^0) chi(-L) = 0 <=> f(-L) = 0
(the (4,4)-signature analogue of the MIT condition with outward normal
-e_y; gamma^0 squares to +1 so no factor i appears), option `tip = "g0"`
for g(-L) = 0.  Every one of these conditions makes the y-current
2 Re(f* g) vanish at the end.  NOTE (measured, section "spectrum" of the
JSON output): with tip f(-L) = 0 the parity -1 sector has an exact zero
mode f = 0, g = exp(-M (y + L)) at k = 0 (localised at the cutoff for
M > 0); with tip g(-L) = 0 the parity +1 sector has the exact zero mode
f = exp(M (y + L)), g = 0 (localised at the brane).  A pair of unlike
conditions (f at one end, g at the other) has no zero mode and the
analytic k = 0, lambda = 0 spectrum tan(pL) = p/M (p^2 = eps^2 - M^2,
plus the bound state tanh(qL) = q/M for ML > 1); like conditions give
p = n pi / L.  Both are used as self-tests.
Discretisation (doubler-free).  Staggered (Yee) grid: f on the nodes
y_j = -L + j h, g on the half nodes y_{j+1/2}, j = 0..N-1, h = L/N.  The
Hermitian quadratic form Q[chi] = 2 Re Int -i f* (g' + M g) dy
+ Int (v - s k kappa)|f|^2 + (v + s k kappa)|g|^2 dy is discretised with
the trapezoid rule on the nodes, the midpoint rule on the half nodes,
central differences and averages between the two grids, and a boundary
condition on g imposed by the odd ghost extension g_{N+1/2} = -g_{N-1/2}.
With g = i g~ the matrix is real symmetric; the generalised problem
H c = eps W c (W = quadrature weights) is symmetrised by W^-1/2.  The free
dispersion of the scheme, eps(p) = +-sqrt(M^2 + (2/h)^2 sin^2(p h / 2)),
is monotonic on the Brillouin zone, so there is no fermion doubler and no
Wilson term is needed.  The eigenvalue error is c2 h^2 + c3 h^3 + O(h^4)
(the h^3 term comes from the ghost node); every quantity is computed on
the three grids N, 2N, 4N and extrapolated by eliminating h^2 and h^3,
with the order estimates and level values recorded.  The two END-NODE
values of a profile are only first-order accurate (they are tied to the
half-node value g~ = O(h) through a division by h) and are extrapolated
with the (h, h^2) elimination instead (`extrapolate_profile`).
Kohn-Sham functional (Mermin, finite T, normal ordered).  Proper densities
n_p = e^{-6Hy} n_c, S_p = e^{-6Hy} S_c with the coordinate densities
n_c(y) = (1/l^3) sum_i g_i o_i |chi_i|^2, S_c(y) = (1/l^3) sum_i g_i o_i
chi_i^dag sigma_y chi_i, o_i = f(eps_i) for a particle state and
-(1 - f(eps_i)) for a Dirac-sea state (a hole in the sea is an
antiparticle: it counts negatively in n and positively in S), g_i = 4 r3(q)
(block multiplicity times the number of lattice vectors with |n|^2 = q,
k = Delta_k sqrt(q)).  Particle/sea branches (normal ordering with respect
to the FREE Dirac sea, the convention of the exact theory and of the Rust
crate; option sea = "free", default): a level is a particle state iff its
lambda = 0 partner has eps >= 0, the partner being the level of the same
rank in the ascending spectrum at the same (k, parity, block type); in one
dimension the levels of a self-adjoint sector do not cross, so the rank is
a continuous label (the Rust crate's Pruefer index) and the identification
is the continuation from lambda = 0.  Only the numbers of negative and
positive free eigenvalues are needed (`free_branch_counts`, one extra
eigvalsh per shell and grid, cached).  The interacting sign of eps is NOT
used: the k = 0 brane zero modes move to eps = <v_x> < 0 for lambda > 0
and stay particle states (with the sign convention, option sea = "sign",
they would be swallowed by the sea and N = 8 would jump to the next shell:
a convention-driven discontinuity, recorded for comparison only).
Coupling rule (the Rust crate's): S_ref = max_y |S_p(y)| of the free
N_mid ground state at m = 1, L = 3 (both parities filled together),
lambda_hat_1 = 0.1/S_ref, lambda_hat_2 = 1.0/S_ref (so that |lambda S_p|/m
reaches 0.1 and 1.0 there); the same numbers are used at m = 3 and the
achieved max |lambda S_p|/m is reported per run.  Hartree: E_H = (lambda/2)
Int S_p^2 W^6 dy, M_H = lambda S_p.  Exchange: for the uniform 8-fold
degenerate gas with the contact interaction the Fock term is exactly
e_x = -(lambda/32) (n^2 + S^2) (derived in `exchange_trace_identity`
from Tr[(-i gamma^4) P_+(k) (-i gamma^4) P_+(k')] = 4 [1 + (M^2 - k.k')/
(E E')] and its P_- partners; it reproduces E_x = -E_H/8 for one filled
shell).  Three pseudo-potential modes are implemented (`--xc`):
    hartree    M_eff = m + lambda S_p, v_x = 0;
    lda-n      (STAGE4_SPEC recommendation, default) M_eff = m + lambda
               S_p and v_x = d e_x / d n at (n_p(y), T) with the gas
               relation S = S_gas(n, T; m) of the free gas of mass m,
               entering as eps -> eps - v_x(y);
    quadratic  the exact functional derivative of E_x[n_p, S_p]:
               v_v = -lambda n_p / 16 (vector) and v_s = -lambda S_p / 16
               (added to M_eff).
Parity sectors.  The Z2 conditions are boundary conditions, not symmetries
(STAGE4_SPEC E4.6): parity = +1 / -1 solves one sector, parity = 0 solves
both and fills them together as one system (the convention of the Rust
crate: on the doubled interval the two sectors are the symmetric and
antisymmetric solutions).  The canonical set uses parity = 0 for the runs
that mirror the Rust matrix (labels m1_L3_N8_lam0_T0, ... as in the crate)
and the single sectors for the L series (labels L2-free-N8-p+1, ...).
Outputs (deterministic, LF, json.dumps(indent=2) + newline) under
artifacts/dirac16complex/kohn-sham/reference/: reference-summary.json and
one directory per run with spectrum.csv, profiles.csv,
scf-history-level*.csv and run.json (thermo/excited/emt records inside).

Usage: python scripts/ks_reference_solver.py [--output DIR] [--quick]
       [--runs NAME,...] [--workers W] [--resume] [--skip-self-tests]
       [--config JSON] (a single run from a JSON parameter set)
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import math
import os
import sys
import time

# small dense matrices: BLAS threading only costs (the run-level parallelism
# is by processes, see --workers); must be set before numpy is imported
if "OPENBLAS_NUM_THREADS" not in os.environ:
    os.environ["OPENBLAS_NUM_THREADS"] = "2"
if "OMP_NUM_THREADS" not in os.environ:
    os.environ["OMP_NUM_THREADS"] = "2"

import numpy as np  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_FIXTURE = os.path.join(REPO, "artifacts", "dirac16complex", "arbitrary-field",
                               "algebra-fixture.json")
DEFAULT_OUTPUT = os.path.join(REPO, "artifacts", "dirac16complex", "kohn-sham", "reference")
PRODUCER = "scripts/ks_reference_solver.py"
SCHEMA_VERSION = 1

SX = np.array([[0.0, 1.0], [1.0, 0.0]])
SY = np.array([[0.0, -1.0j], [1.0j, 0.0]])
SZ = np.array([[1.0, 0.0], [0.0, -1.0]])
I2 = np.eye(2)
ETA = np.array([1, 1, 1, 1, -1, -1, -1, -1], dtype=float)


# ---------------------------------------------------------------------------
# 1. Algebra fixture and the exact block reduction
# ---------------------------------------------------------------------------

def sha256_file(path: str) -> str:
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def load_fixture(path: str = DEFAULT_FIXTURE):
    with open(path, "r", encoding="utf-8") as handle:
        doc = json.load(handle)
    gam = [np.array(g, dtype=float) for g in doc["gamma"]]
    charge = np.array(doc["C"], dtype=float)
    chirality = np.array(doc["chirality"], dtype=float)
    return gam, charge, chirality


def clifford_ok(gam) -> bool:
    ident = np.eye(16)
    for a in range(8):
        for b in range(8):
            target = 2.0 * ETA[a] * ident if a == b else np.zeros((16, 16))
            if not np.array_equal(gam[a] @ gam[b] + gam[b] @ gam[a], target):
                return False
    return True


def block_reduction(gam, charge):
    """Derive the eight 2x2 blocks of (A0, A1, A4, B, C) from the fixture.

    Returns a dict with the unitary U (columns = block basis, 16x16 complex,
    listed as [re, im]), the labels (J, iK1, iK2, s, b) of the eight blocks,
    the maximal deviation of every block from its claimed closed form and
    the dimension of the algebra generated by A0, A1, A4 (8 over R).
    """
    A0, A1, A4 = gam[0], gam[0] @ gam[1], gam[0] @ gam[4]
    B = -1j * charge @ gam[4]
    J = A0 @ A1 @ A4
    K1, K2 = 1j * gam[2] @ gam[3], 1j * gam[5] @ gam[6]
    ident = np.eye(16)
    facts = {
        "J_symmetric": bool(np.array_equal(J, J.T)),
        "J_squares_to_one": bool(np.array_equal(J @ J, ident)),
        "iK1_hermitian": bool(np.allclose(K1, K1.conj().T, atol=0, rtol=0)),
        "iK2_hermitian": bool(np.allclose(K2, K2.conj().T, atol=0, rtol=0)),
        "J_K1_K2_commute": bool(np.allclose(J @ K1, K1 @ J) and np.allclose(J @ K2, K2 @ J)
                                and np.allclose(K1 @ K2, K2 @ K1)),
        "A0_A1_A4_commute_with_J_K1_K2": bool(all(
            np.allclose(X @ Y, Y @ X) for X in (A0, A1, A4) for Y in (J, K1, K2))),
        "B_commutes_with_A0_A1_A4": bool(all(np.allclose(B @ X, X @ B) for X in (A0, A1, A4))),
        "C_anticommutes_A0_A4_commutes_A1": bool(
            np.allclose(charge @ A0, -A0 @ charge) and np.allclose(charge @ A4, -A4 @ charge)
            and np.allclose(charge @ A1, A1 @ charge)),
    }
    columns = []
    labels = []
    deviation = 0.0
    for j in (1, -1):
        for k1 in (1, -1):
            for k2 in (1, -1):
                proj = ((ident + j * J) / 2) @ ((ident + k1 * K1) / 2) @ ((ident + k2 * K2) / 2)
                u, sv, _ = np.linalg.svd(proj)
                rank = int(np.sum(sv > 1e-9))
                if rank != 2:
                    raise RuntimeError("joint eigenspace of dimension %d" % rank)
                V = u[:, :2]
                a0 = V.conj().T @ A0 @ V
                w, vec = np.linalg.eigh((a0 + a0.conj().T) / 2)
                e1 = V @ vec[:, int(np.argmax(w))]
                idx = int(np.argmax(np.abs(e1)))
                e1 = e1 * np.exp(-1j * np.angle(e1[idx]))
                e2 = A4 @ e1
                E = np.stack([e1, e2], axis=1)
                blk = {name: E.conj().T @ X @ E for name, X in
                       (("A0", A0), ("A1", A1), ("A4", A4), ("B", B), ("C", charge), ("J", J),
                        ("BC", B @ charge), ("mig4", -1j * gam[4]))}
                dev = max(np.max(np.abs(blk["A0"] - SZ)), np.max(np.abs(blk["A4"] - SX)))
                s = 1 if np.max(np.abs(blk["A1"] - 1j * SY)) < 1e-9 else -1
                dev = max(dev, np.max(np.abs(blk["A1"] - s * 1j * SY)))
                b = 1 if np.max(np.abs(blk["B"] - I2)) < 1e-9 else -1
                dev = max(dev, np.max(np.abs(blk["B"] - b * I2)),
                          np.max(np.abs(blk["C"] - b * SY)),
                          np.max(np.abs(blk["J"] - j * I2)),
                          np.max(np.abs(blk["BC"] - SY)),
                          np.max(np.abs(blk["mig4"] - SY)))
                deviation = max(deviation, float(dev))
                columns.append(E)
                labels.append({"J": j, "iK1": k1, "iK2": k2, "s": s, "b": b,
                               "b_equals_J_times_iK1": bool(b == j * k1)})
    U = np.concatenate(columns, axis=1)
    unitary_dev = float(np.max(np.abs(U.conj().T @ U - ident)))
    return {
        "facts": facts,
        "blocks": labels,
        "maxDeviationFromClosedForm": deviation,
        "unitarityDeviation": unitary_dev,
        "algebraDimensionOverR": algebra_dimension([A0, A1, A4]),
        "unitary_re": U.real.tolist(),
        "unitary_im": U.imag.tolist(),
        "closedForm": "A0 = sigma_z, A4 = sigma_x, A1 = s i sigma_y (s = J), B = b 1 "
                      "(b = J iK1), C = b sigma_y, B C = -i gamma^4 = sigma_y",
        "ksOperator2x2": "h_s = -i sigma_x d/dy + M_eff sigma_y - s k kappa sigma_z + v_x",
    }


def algebra_dimension(generators) -> int:
    basis = [np.eye(16, dtype=complex)]
    frontier = [np.eye(16, dtype=complex)]
    while frontier:
        new = []
        for Bm in frontier:
            for G in generators:
                Mx = Bm @ G
                V = np.array([b.flatten() for b in basis + [Mx]])
                if np.linalg.matrix_rank(V, tol=1e-9) > len(basis):
                    basis.append(Mx)
                    new.append(Mx)
        frontier = new
    return len(basis)


def exchange_trace_identity(gam, charge, M=1.0, samples=((0.3, 0.1, -0.2), (1.1, -0.4, 0.5))):
    """Tr[A P_a(k) A P_b(k')], A = -i gamma^4, P_+- spectral projectors of
    h_k = -i M gamma^4 - gamma^4 gamma^j k_j, against the closed form
    4 [1 +- (M^2 - k.k') / (E E')] (+ for like, - for unlike signs)."""
    A = -1j * gam[4]
    dev = 0.0
    B = -1j * charge @ gam[4]
    assert np.allclose(B @ charge, A)
    for kk in samples:
        for kp in samples:
            def ham(k):
                hm = -1j * M * gam[4]
                for j in range(3):
                    hm = hm - k[j] * (gam[4] @ gam[1 + j])
                return hm
            Ek = math.sqrt(M * M + sum(x * x for x in kk))
            Ep = math.sqrt(M * M + sum(x * x for x in kp))
            Pk = {1: (np.eye(16) + ham(kk) / Ek) / 2, -1: (np.eye(16) - ham(kk) / Ek) / 2}
            Pp = {1: (np.eye(16) + ham(kp) / Ep) / 2, -1: (np.eye(16) - ham(kp) / Ep) / 2}
            dot = sum(a * b for a, b in zip(kk, kp))
            for sa in (1, -1):
                for sb in (1, -1):
                    tr = np.trace(A @ Pk[sa] @ A @ Pp[sb]).real
                    closed = 4.0 * (1.0 + sa * sb * (M * M - dot) / (Ek * Ep))
                    dev = max(dev, abs(tr - closed))
    return float(dev)


# ---------------------------------------------------------------------------
# 2. Uniform-gas thermodynamics (8-fold degenerate relativistic gas, mass m)
# ---------------------------------------------------------------------------

GAUSS_N = 160


def _fermi(x):
    """1/(e^x + 1) without overflow."""
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    pos = x > 0
    out[pos] = np.exp(-x[pos]) / (1.0 + np.exp(-x[pos]))
    out[~pos] = 1.0 / (1.0 + np.exp(x[~pos]))
    return out


def gas_densities(mu: float, T: float, m: float):
    """(n, S, dn/dmu, dS/dmu) of the free 8-fold gas of mass m at (mu, T),
    normal ordered: n = 8 Int d3k/(2pi)^3 [f(E-mu) - f(E+mu)],
    S = 8 Int d3k/(2pi)^3 (m/E) [f(E-mu) + f(E+mu)]."""
    if T <= 0.0:
        if abs(mu) <= m:
            return 0.0, 0.0, 0.0, 0.0
        kf = math.sqrt(mu * mu - m * m)
        ef = abs(mu)
        n = 4.0 * kf ** 3 / (3.0 * math.pi ** 2)
        S = (2.0 * m / math.pi ** 2) * (kf * ef - m * m * math.log((kf + ef) / m))
        dn = 4.0 * kf * ef / math.pi ** 2
        dS = 4.0 * m * kf / math.pi ** 2
        sign = 1.0 if mu > 0 else -1.0
        return sign * n, S, dn, sign * dS
    # finite T: k in [0, kmax], kmax such that f < 1e-18
    kmax = math.sqrt(max((abs(mu) + 45.0 * T) ** 2 - m * m, 0.0)) + 1.0
    x, w = np.polynomial.legendre.leggauss(GAUSS_N)
    # split the interval in two ranges for accuracy near the Fermi surface
    pieces = []
    kf = math.sqrt(max(mu * mu - m * m, 0.0)) if abs(mu) > m else 0.0
    edges = sorted({0.0, kmax, min(max(kf, 0.0), kmax), min(kf + 8 * T, kmax), min(max(kf - 8 * T, 0.0), kmax)})
    for a, b in zip(edges[:-1], edges[1:]):
        if b - a < 1e-14:
            continue
        pieces.append(((b - a) / 2 * x + (b + a) / 2, (b - a) / 2 * w))
    kk = np.concatenate([p[0] for p in pieces])
    ww = np.concatenate([p[1] for p in pieces])
    E = np.sqrt(kk * kk + m * m)
    fp = _fermi((E - mu) / T)
    fm = _fermi((E + mu) / T)
    pref = 8.0 / (2.0 * math.pi ** 2)
    n = pref * float(np.sum(ww * kk * kk * (fp - fm)))
    S = pref * float(np.sum(ww * kk * kk * (m / E) * (fp + fm)))
    dfp = fp * (1 - fp) / T
    dfm = fm * (1 - fm) / T
    dn = pref * float(np.sum(ww * kk * kk * (dfp + dfm)))
    dS = pref * float(np.sum(ww * kk * kk * (m / E) * (dfp - dfm)))
    return n, S, dn, dS


def gas_mu_of_n(n: float, T: float, m: float) -> float:
    """Chemical potential of the free gas with net density n (bisection)."""
    if n == 0.0:
        return 0.0
    sign = 1.0 if n > 0 else -1.0
    target = abs(n)
    lo, hi = 0.0, m + 1.0
    while gas_densities(hi, T, m)[0] < target:
        hi *= 2.0
        if hi > 1e6:
            raise RuntimeError("gas_mu_of_n: density out of range")
    for _ in range(200):
        mid = (lo + hi) / 2
        if gas_densities(mid, T, m)[0] < target:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-15 * max(1.0, hi):
            break
    return sign * (lo + hi) / 2


def exchange_energy_density(n: float, S: float, lam: float) -> float:
    """e_x = -(lambda/32)(n^2 + S^2): exact HF exchange of the 8-fold gas."""
    return -(lam / 32.0) * (n * n + S * S)


def lda_n_potential(n: float, T: float, m: float, lam: float):
    """(e_x, v_x) of mode lda-n: e_x(n,T) = -(lam/32)(n^2 + S_gas(n,T)^2),
    v_x = d e_x/d n = -(lam/16)(n + S dS/dn), S_gas even in n."""
    mu = gas_mu_of_n(n, T, m)
    ng, Sg, dn, dS = gas_densities(mu, T, m)
    if dn > 0:
        dSdn = dS / dn
    else:
        dSdn = 0.0
    ex = -(lam / 32.0) * (n * n + Sg * Sg)
    vx = -(lam / 16.0) * (n + Sg * dSdn)
    return ex, vx


def gas_selfcheck():
    """Closed form T = 0 vs quadrature at tiny T, derivative consistency."""
    m = 1.0
    report = {}
    mu = 1.7
    n0, S0, dn0, dS0 = gas_densities(mu, 0.0, m)
    n1, S1, dn1, dS1 = gas_densities(mu, 1e-3, m)
    report["T0_vs_smallT_n"] = abs(n0 - n1) / n0
    report["T0_vs_smallT_S"] = abs(S0 - S1) / S0
    # derivative check at T = 0.4 by central differences
    T = 0.4
    d = 1e-4
    na, Sa = gas_densities(mu + d, T, m)[:2]
    nb, Sb = gas_densities(mu - d, T, m)[:2]
    _, _, dn, dS = gas_densities(mu, T, m)
    report["dn_dmu_fd"] = abs((na - nb) / (2 * d) - dn) / dn
    report["dS_dmu_fd"] = abs((Sa - Sb) / (2 * d) - dS) / max(abs(dS), 1e-30)
    # inversion
    n, S = gas_densities(1.3, 0.3, m)[:2]
    report["mu_of_n_roundtrip"] = abs(gas_mu_of_n(n, 0.3, m) - 1.3)
    # T=0 closed form: n = 4 kf^3 / 3 pi^2 for kf = sqrt(mu^2 - m^2)
    kf = math.sqrt(mu * mu - 1)
    report["T0_n_closed_form"] = abs(n0 - 4 * kf ** 3 / (3 * math.pi ** 2))
    return report


# ---------------------------------------------------------------------------
# 3. Geometry of the static primordial field (H = 1 unless stated)
# ---------------------------------------------------------------------------

def geometry_record(H: float = 1.0, kappa8: float = 1.0):
    """Closed forms of STAGE4_SPEC section 1 re-derived numerically from the
    warped metric (finite-difference Ricci tensor) and the Israel junction."""
    def metric(y, a4=0.0):
        w2 = math.exp(2 * H * y)
        return np.array([1.0, w2 * math.exp(2 * a4), w2 * math.exp(2 * a4), w2 * math.exp(2 * a4),
                         -1.0, -w2 * math.exp(-2 * a4), -w2 * math.exp(-2 * a4), -w2 * math.exp(-2 * a4)])

    def christoffel(y):
        g = metric(y)
        dg = np.array([0.0 if mu in (0, 4) else 2 * H * g[mu] for mu in range(8)])
        gam = np.zeros((8, 8, 8))
        for i in range(8):
            gam[0, i, i] = -0.5 * dg[i] / g[0]
            if i != 0:
                gam[i, i, 0] = gam[i, 0, i] = 0.5 * dg[i] / g[i]
        return gam

    def einstein(y, dy=1e-3):
        g = metric(y)
        gam = christoffel(y)
        d = (-christoffel(y + 2 * dy) + 8 * christoffel(y + dy) - 8 * christoffel(y - dy)
             + christoffel(y - 2 * dy)) / (12 * dy)
        ric = np.zeros((8, 8))
        for m in range(8):
            for n in range(8):
                val = d[0, m, n]
                if n == 0:
                    val -= sum(d[r, m, r] for r in range(8))
                val += sum(gam[r, r, l] * gam[l, m, n] - gam[r, n, l] * gam[l, m, r]
                           for r in range(8) for l in range(8))
                ric[m, n] = val
        mixed = np.array([ric[m, m] / g[m] for m in range(8)])
        R = mixed.sum()
        return R, mixed - 0.5 * R

    worst = 0.0
    for y in (-3.0, -1.5, -0.25, 0.0):
        R, G = einstein(y)
        worst = max(worst, abs(R + 42 * H * H),
                    float(np.max(np.abs(G - H * H * np.array([15, 15, 15, 15, 21, 15, 15, 15])))))
    K_minus = np.array([H, H, H, 0.0, H, H, H])          # y = const, normal +d_y, order x1..x7
    jump = -2.0 * K_minus                                # Z2 mirror: K(0+) = -K(0-)
    trace = jump.sum()
    S = -(jump - trace) / kappa8
    return {
        "H": H,
        "ricciScalar": -42.0 * H * H,
        "einsteinMixed_y_x1_x2_x3_x4_x5_x6_x7": [15.0 * H * H] * 4 + [21.0 * H * H] + [15.0 * H * H] * 3,
        "rhoRequired": -21.0 * H * H / kappa8,
        "pRequired_transverse": 15.0 * H * H / kappa8,
        "wRequired": -15.0 / 21.0,
        "curvatureFiniteDifferenceDefect": worst,
        "extrinsicK_x1_x2_x3_x4_x5_x6_x7": K_minus.tolist(),
        "israelConvention": "S^i_j = -(1/kappa)([K^i_j] - delta^i_j [K]), [X] = X(0+) - X(0-), normal from y<0 to y>0, W = e^{-H|y|}",
        "braneStress_x1_x2_x3_x4_x5_x6_x7": S.tolist(),
        "braneEnergyDensity": float(-S[3]),
        "branePressure": float(S[0]),
        "specNote": "STAGE4_SPEC writes p_req = -15H^2/kappa; the mixed components give T^i_i = G^i_i/kappa = +15H^2/kappa (all seven transverse directions) and rho_req = -T^4_4 = -21H^2/kappa < 0.",
    }


# ---------------------------------------------------------------------------
# 4. Staggered-grid discretisation of the 2x2 operator and its eigenpairs
# ---------------------------------------------------------------------------

class Grid:
    """Uniform grid on [-L, 0]: nodes y_j (j = 0..N), half nodes y_{j+1/2}."""

    def __init__(self, L: float, N: int):
        self.L = float(L)
        self.N = int(N)
        self.h = self.L / self.N
        y = -self.L + self.h * np.arange(self.N + 1)
        y[-1] = 0.0
        self.y = y
        self.yh = 0.5 * (y[:-1] + y[1:])
        w = np.full(self.N + 1, self.h)
        w[0] = w[-1] = 0.5 * self.h
        self.w = w
        self.volume_factor = np.exp(6.0 * y)        # W^6 (H = 1)
        self.density_factor = np.exp(-6.0 * y)      # e^{-6Hy}

    def integrate(self, values):
        """Trapezoid integral over [-L, 0] of node values."""
        return float(np.dot(self.w, values))


def half_values(node_values):
    """Linear interpolation of node values to the half nodes."""
    return 0.5 * (node_values[:-1] + node_values[1:])


def kappa_of(y, a4: float):
    return np.exp(-y - a4)


def build_hamiltonian(grid: Grid, m_eff_node, kk_node, kk_half, v_node, parity: int, tip: str):
    """Real symmetric matrix of the staggered discretisation.

    kk = s k kappa (already multiplied by the block sign s and by k) on nodes
    and half nodes; v on nodes (half-node values by linear interpolation).
    Returns (Hs, inv_sqrt_weights, f_nodes) with Hs = W^-1/2 H W^-1/2.  The
    unknown vector is (f at f_nodes, g~ at the N half nodes), g = i g~.
    """
    N, h = grid.N, grid.h
    j0 = 1 if tip == "f0" else 0
    j1 = N if parity > 0 else N - 1
    f_nodes = np.arange(j0, j1 + 1)
    nf = len(f_nodes)
    wf = grid.w[f_nodes]
    v_half = half_values(v_node)
    dim = nf + N
    H = np.zeros((dim, dim))
    H[np.arange(nf), np.arange(nf)] = wf * (v_node[f_nodes] - kk_node[f_nodes])
    H[nf + np.arange(N), nf + np.arange(N)] = h * (v_half + kk_half)
    Mj = m_eff_node[f_nodes]
    a_idx = np.arange(nf)
    right = f_nodes <= N - 1
    H[a_idx[right], nf + f_nodes[right]] += wf[right] * (1.0 / h + 0.5 * Mj[right])
    if not right.all():            # j = N present: ghost g~_{N+1/2} = -g~_{N-1/2}
        a = a_idx[~right][0]
        H[a, nf + N - 1] += -wf[a] * (1.0 / h + 0.5 * Mj[a])
    left = f_nodes >= 1
    H[a_idx[left], nf + f_nodes[left] - 1] += wf[left] * (-1.0 / h + 0.5 * Mj[left])
    if not left.all():             # j = 0 present: ghost g~_{-1/2} = -g~_{1/2}
        a = a_idx[~left][0]
        H[a, nf + 0] += -wf[a] * (-1.0 / h + 0.5 * Mj[a])
    # Note on the ghost: the odd extension g~(-y) = -g~(y) about a g-boundary
    # neglects g~''(0) = (s k kappa' - v') f(0); the corresponding local error
    # enters the form with the end-node weight h/2 and shifts eigenvalues only
    # at O(h^2) (measured), so no correction term is added: the matrix depends
    # on the potentials exactly through sum_j w_j (v_j |f_j|^2 + M_j ...), which
    # keeps the discrete Hellmann-Feynman identities d eps/d v_j = w_j n_j and
    # d eps/d M_j = w_j s_j exact (used by the energy functional).  The end-node
    # VALUES of the eigenvectors are first-order accurate (see
    # extrapolate_profile), the eigenvalues, integrals and interior second order.
    H[nf:, :nf] = H[:nf, nf:].T
    w_all = np.concatenate([wf, np.full(N, h)])
    inv_sqrt = 1.0 / np.sqrt(w_all)
    Hs = inv_sqrt[:, None] * H * inv_sqrt[None, :]
    Hs = 0.5 * (Hs + Hs.T)
    return Hs, inv_sqrt, f_nodes


def eigenpairs(grid: Grid, m_eff_node, kk_node, kk_half, v_node, parity: int, tip: str):
    """All eigenpairs of the discrete h_+ operator.

    Returns eps (ascending) and the node densities n (|chi|^2), s (scalar,
    chi^dag sigma_y chi), z (chi^dag sigma_z chi) as arrays (n_states, N+1),
    plus f on the nodes and g~ on the half nodes (for checks).  Discrete
    definitions (exact Hellmann-Feynman partners of the quadratic form, so
    that sum_j w_j n_j = 1 and d eps / d M_j = w_j s_j):
      n_j = |f_j|^2 + (h/2w_j) sum_{half neighbours b} |g~_b|^2,
      s_j = f_j (g~_{j+1/2} + g~_{j-1/2})  (ghost images with sign -1),
      z_j = |f_j|^2 - (h/2w_j) sum_{half neighbours b} |g~_b|^2.
    """
    Hs, inv_sqrt, f_nodes = build_hamiltonian(grid, m_eff_node, kk_node, kk_half, v_node, parity, tip)
    eps, vec = np.linalg.eigh(Hs)
    c = inv_sqrt[:, None] * vec
    nf = len(f_nodes)
    N = grid.N
    nstates = len(eps)
    F = np.zeros((N + 1, nstates))
    F[f_nodes, :] = c[:nf, :]
    Gt = c[nf:, :]
    G2 = Gt * Gt
    spread = np.zeros((N + 1, nstates))
    spread[:-1, :] += 0.5 * grid.h * G2
    spread[1:, :] += 0.5 * grid.h * G2
    inv_w = 1.0 / grid.w
    n = F * F + inv_w[:, None] * spread
    z = F * F - inv_w[:, None] * spread
    gsum = np.zeros((N + 1, nstates))
    gsum[:-1, :] += Gt
    gsum[1:, :] += Gt
    if parity > 0:
        gsum[N, :] += -Gt[N - 1, :]
    if tip == "g0":
        gsum[0, :] += -Gt[0, :]
    s = F * gsum
    return eps, n.T, s.T, z.T, F.T, Gt.T


_FREE_COUNT_CACHE = {}


def free_branch_counts(grid: Grid, m: float, k: float, a4: float, parity: int, tip: str):
    """(n_neg, n_pos, dim) of the FREE discrete operator h_+ (M = m, v = 0)
    at momentum k: the numbers of eigenvalues below -ZERO_MODE_TOL and
    above +ZERO_MODE_TOL and the matrix dimension.  They define the
    particle/sea branches by continuity from lambda = 0 (see the module
    docstring); cached per (grid, m, k, a4, parity, tip)."""
    key = (grid.N, grid.L, float(m), float(k), float(a4), int(parity), tip)
    hit = _FREE_COUNT_CACHE.get(key)
    if hit is not None:
        return hit
    kap_n = kappa_of(grid.y, a4)
    kap_h = kappa_of(grid.yh, a4)
    Hs, _, _ = build_hamiltonian(grid, np.full(grid.N + 1, float(m)), k * kap_n, k * kap_h,
                                 np.zeros(grid.N + 1), parity, tip)
    ev = np.linalg.eigvalsh(Hs)
    out = (int(np.sum(ev < -ZERO_MODE_TOL)), int(np.sum(ev > ZERO_MODE_TOL)), int(len(ev)))
    if len(_FREE_COUNT_CACHE) > 100000:
        _FREE_COUNT_CACHE.clear()
    _FREE_COUNT_CACHE[key] = out
    return out


def solve_shell(grid: Grid, m_eff_node, v_node, k: float, a4: float, parity: int, tip: str,
                need_minus: bool, m=None, sea="free"):
    """States of both block types at momentum k for one parity.

    Returns a dict with arrays over states (sorted by eps): eps, type
    (+1/-1), branch (+1 particle / -1 Dirac sea), n, s, z, F, G.  Type +1
    states come from h_+(v); type -1 states from h_+(-v) through the
    conjugation map (eps -> -eps, s -> -s, n and z unchanged).  With
    need_minus=False (v = 0) the same diagonalisation serves both types.
    Branches: sea = "free" with the bare mass m given classifies by the
    rank of the level against the free spectrum (a type +1 level of rank r
    is a particle iff r >= n_neg; a type -1 level, whose free partner is
    -free_plus[r], iff r < dim - n_pos); otherwise by the sign of eps.
    """
    kap_n = kappa_of(grid.y, a4)
    kap_h = kappa_of(grid.yh, a4)
    kk_n = k * kap_n
    kk_h = k * kap_h
    eps_p, n_p, s_p, z_p, F_p, G_p = eigenpairs(grid, m_eff_node, kk_n, kk_h, v_node, parity, tip)
    if need_minus:
        eps_m, n_m, s_m, z_m, F_m, G_m = eigenpairs(grid, m_eff_node, kk_n, kk_h, -v_node, parity, tip)
    else:
        eps_m, n_m, s_m, z_m, F_m, G_m = eps_p, n_p, s_p, z_p, F_p, G_p
    if sea == "free" and m is not None:
        n_neg, n_pos, dim = free_branch_counts(grid, m, k, a4, parity, tip)
        br_p = np.where(np.arange(len(eps_p)) >= n_neg, 1, -1)
        br_m = np.where(np.arange(len(eps_m)) < dim - n_pos, 1, -1)
    else:
        br_p = np.where(eps_p >= -ZERO_MODE_TOL, 1, -1)
        br_m = np.where(-eps_m >= -ZERO_MODE_TOL, 1, -1)
    eps = np.concatenate([eps_p, -eps_m])
    typ = np.concatenate([np.ones(len(eps_p), dtype=int), -np.ones(len(eps_m), dtype=int)])
    branch = np.concatenate([br_p, br_m])
    n = np.concatenate([n_p, n_m])
    s = np.concatenate([s_p, -s_m])
    z = np.concatenate([z_p, z_m])
    F = np.concatenate([F_p, F_m])
    G = np.concatenate([G_p, G_m])
    order = np.argsort(eps, kind="stable")
    return {"eps": eps[order], "type": typ[order], "branch": branch[order], "n": n[order],
            "s": s[order], "z": z[order], "F": F[order], "G": G[order]}


# ---------------------------------------------------------------------------
# 5. Lattice shells and the three-level extrapolation
# ---------------------------------------------------------------------------

def lattice_shells(qmax: int):
    """[(q, r3(q))] for 0 <= q <= qmax with r3(q) > 0 (sums of three squares)."""
    r = int(math.isqrt(qmax))
    counts = {}
    for n1 in range(-r, r + 1):
        for n2 in range(-r, r + 1):
            rem = qmax - n1 * n1 - n2 * n2
            if rem < 0:
                continue
            n3max = math.isqrt(rem)
            for n3 in range(-n3max, n3max + 1):
                q = n1 * n1 + n2 * n2 + n3 * n3
                counts[q] = counts.get(q, 0) + 1
    return [(q, counts[q]) for q in sorted(counts)]


def extrapolate3(q1, q2, q4):
    """Eliminate h^2 and h^3 from values on the grids h, h/2, h/4."""
    q1 = np.asarray(q1, dtype=float)
    q2 = np.asarray(q2, dtype=float)
    q4 = np.asarray(q4, dtype=float)
    r12 = (4.0 * q2 - q1) / 3.0
    r24 = (4.0 * q4 - q2) / 3.0
    return (8.0 * r24 - r12) / 7.0


def order_estimate(q1, q2, q4):
    """log2 of the ratio of successive differences (2 for an h^2 scheme)."""
    d1 = float(np.max(np.abs(np.asarray(q1, dtype=float) - np.asarray(q2, dtype=float))))
    d2 = float(np.max(np.abs(np.asarray(q2, dtype=float) - np.asarray(q4, dtype=float))))
    if d2 <= 0.0 or d1 <= 0.0:
        return float("nan")
    return math.log2(d1 / d2)


# ---------------------------------------------------------------------------
# 6. The Kohn-Sham problem: parameters, spectrum in a window, occupations
# ---------------------------------------------------------------------------

WINDOW_FACTOR = 32.0        # f(32) = 1.3e-14: states beyond mu +- 32 T are dropped
ZERO_MODE_TOL = 1e-9        # |eps| below this counts as a particle state (eps >= 0)
DEGENERACY_TOL = 1e-9       # relative grouping tolerance of degenerate levels at T = 0
EXACT_SHELLS_MAX = 300      # lattice shells diagonalised exactly before the Chebyshev tail
CHEBYSHEV_NODES = 32
TAIL_TEST_SHELLS = 6


class Params:
    """Physical and numerical parameters of one Kohn-Sham sector."""

    def __init__(self, m=1.0, a4=0.0, L=3.0, lambda_hat=0.0, T=0.0, N=8.0, parity=1,
                 tip="g0", xc="quadratic", delta_k_over_m=0.25, ell=None, delta_k=None,
                 N0=100, levels=3, mix_beta=0.4, mix_history=6, tol=1e-10, max_iter=200,
                 label="run", f_cut=None, sea="free"):
        if sea not in ("free", "sign"):
            raise ValueError("sea must be 'free' or 'sign'")
        self.sea = sea
        self.m = float(m)
        self.a4 = float(a4)
        self.L = float(L)
        self.lambda_hat = float(lambda_hat)
        self.lam = self.lambda_hat / self.m ** 6
        self.T = float(T)
        self.N = float(N)
        self.parity = int(parity)
        self.tip = tip
        self.xc = xc
        self.delta_k = float(delta_k) if delta_k is not None else float(delta_k_over_m) * self.m
        self.ell = float(ell) if ell is not None else 2.0 * math.pi / self.delta_k
        self.volume = self.ell ** 3
        self.N0 = int(N0)
        self.levels = int(levels)
        self.mix_beta = float(mix_beta)
        self.mix_history = int(mix_history)
        self.tol = float(tol)
        self.max_iter = int(max_iter)
        self.label = label
        self.f_cut = f_cut

    def to_dict_kwargs(self):
        """Constructor keyword arguments reproducing this parameter set."""
        return {"m": self.m, "a4": self.a4, "L": self.L, "lambda_hat": self.lambda_hat, "T": self.T,
                "N": self.N, "parity": self.parity, "tip": self.tip, "xc": self.xc,
                "delta_k": self.delta_k, "ell": self.ell, "N0": self.N0, "levels": self.levels,
                "mix_beta": self.mix_beta, "mix_history": self.mix_history, "tol": self.tol,
                "max_iter": self.max_iter, "label": self.label, "f_cut": self.f_cut, "sea": self.sea}

    def to_dict(self):
        return {"label": self.label, "m": self.m, "a4_0": self.a4, "L": self.L,
                "lambda_hat": self.lambda_hat, "lambda": self.lam, "T": self.T, "N": self.N,
                "parity": self.parity, "tip": self.tip, "xc": self.xc, "sea": self.sea,
                "delta_k": self.delta_k, "ell": self.ell, "volume": self.volume, "N0": self.N0,
                "levels": self.levels, "mix_beta": self.mix_beta, "mix_history": self.mix_history,
                "tol": self.tol, "max_iter": self.max_iter, "H": 1.0}


class State:
    """One single-particle level (both branches, both block types)."""
    __slots__ = ("q", "r3", "k", "type", "index", "eps", "n", "s", "z", "mult", "f", "w",
                 "interpolated", "parity", "branch")

    def __init__(self, q, r3, k, typ, index, eps, n, s, z, interpolated=False, parity=1, branch=None):
        self.parity = parity
        self.branch = int(branch) if branch is not None else (1 if index >= 0 else -1)
        self.q = q
        self.r3 = r3
        self.k = k
        self.type = typ
        self.index = index
        self.eps = eps
        self.n = n
        self.s = s
        self.z = z
        self.mult = 4.0 * r3
        self.f = 0.0
        self.w = 0.0
        self.interpolated = interpolated

    def key(self):
        return (self.q, self.parity, self.type, self.index)


def index_states(shell, eps_lo, eps_hi):
    """Rank indices within (type, branch): 0, 1, ... for the particle
    branch ascending in eps, -1, -2, ... for the sea branch descending;
    returns the states in the window as (type, index, position)."""
    out = []
    for typ in (1, -1):
        sel = np.where(shell["type"] == typ)[0]
        br = shell["branch"][sel]
        pos = sel[br > 0]
        neg = sel[br < 0]
        for rank, i in enumerate(pos):
            if eps_lo <= shell["eps"][i] <= eps_hi:
                out.append((typ, rank, i))
        for rank, i in enumerate(neg[::-1]):
            if eps_lo <= shell["eps"][i] <= eps_hi:
                out.append((typ, -1 - rank, i))
    return out


def chebyshev_nodes(a, b, n):
    j = np.arange(n)
    x = np.cos(math.pi * (2 * j + 1) / (2 * n))      # Chebyshev points of the first kind
    return 0.5 * (a + b) + 0.5 * (b - a) * x, x


def barycentric_weights_first_kind(n):
    j = np.arange(n)
    return (-1.0) ** j * np.sin(math.pi * (2 * j + 1) / (2 * n))


def barycentric_eval(xnodes, wts, values, x):
    """Barycentric interpolation; values has shape (n, ...)."""
    diff = x - xnodes
    exact = np.where(np.abs(diff) < 1e-15)[0]
    if len(exact):
        return values[exact[0]]
    c = wts / diff
    return np.tensordot(c, values, axes=(0, 0)) / c.sum()


class Spectrum:
    """All states of one sector within an energy window, at fixed potentials."""

    def __init__(self, params: Params, grid: Grid, m_eff, v, eps_lo, eps_hi):
        self.params = params
        self.grid = grid
        self.m_eff = m_eff
        self.v = v
        self.eps_lo = eps_lo
        self.eps_hi = eps_hi
        self.states = []
        self.shells_exact = 0
        self.shells_interpolated = 0
        self.tail = None
        self.compute()

    def parities(self):
        """Sectors solved: one Z2 parity, or both filled together (parity = 0)."""
        return [1, -1] if self.params.parity == 0 else [self.params.parity]

    def compute(self):
        p = self.params
        need_minus = bool(np.any(self.v != 0.0))
        shells = lattice_shells(4 * int((max(abs(self.eps_hi), abs(self.eps_lo)) * math.exp(p.a4) / p.delta_k) ** 2) + 64)
        empty_run = 0
        exact_done = 0
        last_exact_q = 0
        exhausted = False
        for q, r3 in shells:
            if exact_done >= EXACT_SHELLS_MAX:
                break
            k = p.delta_k * math.sqrt(q)
            found = []
            for parity in self.parities():
                shell = solve_shell(self.grid, self.m_eff, self.v, k, p.a4, parity, p.tip, need_minus,
                                    m=p.m, sea=p.sea)
                here = index_states(shell, self.eps_lo, self.eps_hi)
                found.extend(here)
                for typ, index, i in here:
                    self.states.append(State(q, r3, k, typ, index, float(shell["eps"][i]),
                                             shell["n"][i], shell["s"][i], shell["z"][i], parity=parity,
                                             branch=shell["branch"][i]))
            exact_done += 1
            last_exact_q = q
            if found:
                empty_run = 0
            else:
                empty_run += 1
                if empty_run >= 3 and k > 0.5 * max(abs(self.eps_hi), abs(self.eps_lo)) * math.exp(p.a4):
                    exhausted = True
                    break
        self.shells_exact = exact_done
        if not exhausted:
            self.compute_tail(shells, last_exact_q, need_minus)

    def compute_tail(self, shells, last_exact_q, need_minus):
        """Chebyshev interpolation in |k| of the levels and profiles for the
        lattice shells beyond the exactly diagonalised ones."""
        p = self.params
        top = max(abs(self.eps_hi), abs(self.eps_lo))
        k_a = p.delta_k * math.sqrt(last_exact_q)
        # find k_max: smallest sampled k whose lowest |eps| exceeds the window
        k_b = k_a
        parities = self.parities()
        def shell_at(kv, par):
            return solve_shell(self.grid, self.m_eff, self.v, kv, p.a4, par, p.tip, need_minus,
                               m=p.m, sea=p.sea)

        while True:
            k_b = k_b * 1.25 + 0.5
            if not any(index_states(shell_at(k_b, par), self.eps_lo, self.eps_hi) for par in parities):
                break
            if k_b > 1e4 * max(top, 1.0):
                raise RuntimeError("tail: window never exhausted")
        nodes, _ = chebyshev_nodes(k_a, k_b, CHEBYSHEV_NODES)
        wts = barycentric_weights_first_kind(CHEBYSHEV_NODES)
        # levels kept per (parity, type, branch): those in the window at k_a (the widest set)
        keep = {}
        for par in parities:
            ref = shell_at(k_a, par)
            for typ, index, i in index_states(ref, self.eps_lo, self.eps_hi):
                kk = (par, typ, index >= 0)
                keep[kk] = max(keep.get(kk, 0), abs(index) + (1 if index >= 0 else 0))
        if not keep:
            self.tail = {"kMin": k_a, "kMax": k_b, "levels": 0}
            return
        samples = {}   # (parity, typ, index) -> list over nodes of (eps, n, s, z)
        for kn in nodes:
            for par in parities:
                shell = shell_at(kn, par)
                for typ in (1, -1):
                    sel = np.where(shell["type"] == typ)[0]
                    br = shell["branch"][sel]
                    pos = sel[br > 0]
                    neg = sel[br < 0][::-1]
                    for rank in range(keep.get((par, typ, True), 0)):
                        i = pos[rank]
                        samples.setdefault((par, typ, rank), []).append(
                            (shell["eps"][i], shell["n"][i], shell["s"][i], shell["z"][i]))
                    for rank in range(keep.get((par, typ, False), 0)):
                        i = neg[rank]
                        samples.setdefault((par, typ, -1 - rank), []).append(
                            (shell["eps"][i], shell["n"][i], shell["s"][i], shell["z"][i]))
        packed = {}
        for key, lst in samples.items():
            packed[key] = (np.array([x[0] for x in lst]), np.array([x[1] for x in lst]),
                           np.array([x[2] for x in lst]), np.array([x[3] for x in lst]))
        tail_shells = [(q, r3) for q, r3 in shells if q > last_exact_q and p.delta_k * math.sqrt(q) <= k_b]
        count = 0
        for q, r3 in tail_shells:
            k = p.delta_k * math.sqrt(q)
            any_state = False
            for key, (eps_s, n_s, s_s, z_s) in packed.items():
                eps = float(barycentric_eval(nodes, wts, eps_s, k))
                if self.eps_lo <= eps <= self.eps_hi:
                    any_state = True
                    n = barycentric_eval(nodes, wts, n_s, k)
                    s = barycentric_eval(nodes, wts, s_s, k)
                    z = barycentric_eval(nodes, wts, z_s, k)
                    self.states.append(State(q, r3, k, key[1], key[2], eps, n, s, z, interpolated=True,
                                             parity=key[0]))
            if any_state:
                count += 1
        self.shells_interpolated = count
        # verification at TAIL_TEST_SHELLS lattice shells spread over the range
        test_err_eps = 0.0
        test_err_n = 0.0
        if tail_shells:
            picks = sorted({tail_shells[int(i * (len(tail_shells) - 1) / max(TAIL_TEST_SHELLS - 1, 1))][0]
                            for i in range(TAIL_TEST_SHELLS)})
            for q in picks:
                k = p.delta_k * math.sqrt(q)
                for par in parities:
                    shell = shell_at(k, par)
                    for typ, index, i in index_states(shell, self.eps_lo, self.eps_hi):
                        if (par, typ, index) not in packed:
                            continue
                        eps_s, n_s, s_s, z_s = packed[(par, typ, index)]
                        eps_i = float(barycentric_eval(nodes, wts, eps_s, k))
                        n_i = barycentric_eval(nodes, wts, n_s, k)
                        test_err_eps = max(test_err_eps, abs(eps_i - shell["eps"][i]))
                        test_err_n = max(test_err_n, float(np.max(np.abs(n_i - shell["n"][i]))))
        self.tail = {"kMin": k_a, "kMax": k_b, "levels": len(packed), "nodes": CHEBYSHEV_NODES,
                     "shellsInterpolated": count, "testShells": TAIL_TEST_SHELLS,
                     "maxEpsInterpolationError": test_err_eps, "maxDensityInterpolationError": test_err_n}


def fermi_weight(branch, f):
    """Normal-ordered weight: f on the particle branch, -(1 - f) on the sea."""
    return f if branch > 0 else -(1.0 - f)


def branch_overlap(states):
    """(highest sea level, lowest occupied particle level): a diagnostic of
    the branch classification (a sea level above an occupied particle level
    would signal a band crossing)."""
    sea = [st.eps for st in states if st.branch < 0]
    occ = [st.eps for st in states if st.branch > 0 and st.f > 0.0]
    return (max(sea) if sea else float("-inf")), (min(occ) if occ else float("inf"))


def occupy_zero(states, N):
    """T = 0 filling by eps along the particle branch, fractional straddling
    group; the sea stays full (f = 1, weight 0)."""
    for st in states:
        st.f = 1.0 if st.branch < 0 else 0.0
        st.w = 0.0
    particles = sorted((st for st in states if st.branch > 0), key=lambda st: (st.eps, st.key()))
    remaining = N
    homo = None
    lumo = None
    i = 0
    while i < len(particles):
        e = particles[i].eps
        j = i
        group_mult = 0.0
        while j < len(particles) and abs(particles[j].eps - e) <= DEGENERACY_TOL * max(abs(e), 1.0):
            group_mult += particles[j].mult
            j += 1
        if remaining <= 1e-12:
            if lumo is None:
                lumo = particles[i]
            break
        fraction = min(remaining / group_mult, 1.0)
        for st in particles[i:j]:
            st.f = fraction
            st.w = fraction
        remaining -= fraction * group_mult
        homo = particles[i]
        if fraction < 1.0:
            lumo = particles[i]
        i = j
    if remaining > 1e-9:
        raise RuntimeError("occupy_zero: %g particles unplaced (window too small)" % remaining)
    mu = homo.eps if homo is not None else 0.0
    return mu, homo, lumo


def occupy_thermal(states, N, T):
    eps = np.array([st.eps for st in states])
    mult = np.array([st.mult for st in states])
    sign = np.array([1.0 if st.branch > 0 else -1.0 for st in states])

    def count(mu):
        f = _fermi((eps - mu) / T)
        w = np.where(sign > 0, f, -(1.0 - f))
        return float(np.dot(mult, w))

    scale = float(np.max(np.abs(eps))) + 60.0 * T if len(eps) else 60.0 * T
    lo, hi = -scale, scale
    if count(lo) > N or count(hi) < N:
        raise RuntimeError("occupy_thermal: N not bracketed")
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if count(mid) < N:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-15 * scale:
            break
    mu = 0.5 * (lo + hi)
    f = _fermi((eps - mu) / T)
    for st, fi, sg in zip(states, f, sign):
        st.f = float(fi)
        st.w = float(fi) if sg > 0 else -(1.0 - float(fi))
    homo = None
    lumo = None
    for st in sorted(states, key=lambda st: st.eps):
        if st.branch > 0:
            if st.f >= 0.5:
                homo = st
            elif lumo is None:
                lumo = st
    return mu, homo, lumo


def occupy_constrained(states, occupations):
    """occupations: dict key -> f for the particle states; sea untouched."""
    total = 0.0
    for st in states:
        # particle states default to empty, sea states to filled (weight 0)
        default = 0.0 if st.branch > 0 else 1.0
        f = occupations.get(st.key(), default)
        st.f = f
        st.w = fermi_weight(st.branch, f)
        total += st.mult * st.w
    present = sum(1 for st in states if st.key() in occupations)
    if present != len(occupations):
        raise RuntimeError("occupy_constrained: %d constrained levels missing" % (len(occupations) - present))
    mu = max((st.eps for st in states if st.f > 0), default=0.0)
    return mu, total


# ---------------------------------------------------------------------------
# 7. Densities, potentials, energies, mixing, the SCF loop
# ---------------------------------------------------------------------------

def densities(states, params: Params, grid: Grid):
    n_c = np.zeros(grid.N + 1)
    s_c = np.zeros(grid.N + 1)
    inv_v = 1.0 / params.volume
    for st in states:
        if st.w == 0.0:
            continue
        wgt = st.mult * st.w * inv_v
        n_c += wgt * st.n
        s_c += wgt * st.s
    return n_c, s_c


class LdaTable:
    """S_gas(n, T; m) and dS/dn by tabulation in mu (mode lda-n)."""

    def __init__(self, T, m, n_max):
        self.T = T
        self.m = m
        if T <= 0.0:
            self.mu = None
            return
        mu_hi = m + 1.0
        while gas_densities(mu_hi, T, m)[0] < 1.2 * n_max + 1e-12:
            mu_hi *= 1.5
        self.mu = np.linspace(0.0, mu_hi, 4001)
        vals = np.array([gas_densities(mu, T, m) for mu in self.mu])
        self.n = vals[:, 0]
        self.S = vals[:, 1]
        self.dSdn = np.where(vals[:, 2] > 0, vals[:, 3] / np.maximum(vals[:, 2], 1e-300), 0.0)

    def lookup(self, n):
        a = abs(n)
        if self.T <= 0.0:
            mu = gas_mu_of_n(a, 0.0, self.m)
            ng, Sg, dn, dS = gas_densities(mu, 0.0, self.m)
            return Sg, (dS / dn if dn > 0 else 0.0)
        return float(np.interp(a, self.n, self.S)), float(np.interp(a, self.n, self.dSdn))


def potentials(params: Params, grid: Grid, n_c, s_c, lda: LdaTable = None):
    """(M_eff, v_x, e_int, dc) on the nodes: the KS potentials, the
    interaction energy density and the double-counting density
    (M_eff - m) S_p + v_x n_p, all per proper volume."""
    lam = params.lam
    s_p = grid.density_factor * s_c
    n_p = grid.density_factor * n_c
    if params.xc == "hartree":
        m_eff = params.m + lam * s_p
        v = np.zeros_like(n_p)
        e_int = 0.5 * lam * s_p * s_p
    elif params.xc == "quadratic":
        m_eff = params.m + lam * s_p - lam * s_p / 16.0
        v = -lam * n_p / 16.0
        e_int = 0.5 * lam * s_p * s_p - (lam / 32.0) * (n_p * n_p + s_p * s_p)
    elif params.xc == "lda-n":
        m_eff = params.m + lam * s_p
        v = np.zeros_like(n_p)
        e_int = 0.5 * lam * s_p * s_p
        for j in range(len(n_p)):
            Sg, dSdn = lda.lookup(n_p[j])
            v[j] = -(lam / 16.0) * (n_p[j] + Sg * dSdn)
            e_int[j] += -(lam / 32.0) * (n_p[j] ** 2 + Sg ** 2)
    else:
        raise ValueError("unknown xc mode %r" % params.xc)
    dc = (m_eff - params.m) * s_p + v * n_p
    return m_eff, v, e_int, dc


def energies(states, params: Params, grid: Grid, n_c, s_c, e_int, dc, mu):
    """Total energy and thermodynamic potentials of an occupied spectrum."""
    ks_sum = sum(st.mult * st.w * st.eps for st in states)
    n_total = sum(st.mult * st.w for st in states)
    vol = params.volume
    e_int_total = vol * grid.integrate(e_int * grid.volume_factor)
    dc_total = vol * grid.integrate(dc * grid.volume_factor)
    hartree = vol * 0.5 * params.lam * grid.integrate(grid.density_factor * s_c * s_c)
    entropy = 0.0
    for st in states:
        f = st.f
        if 0.0 < f < 1.0:
            entropy -= st.mult * (f * math.log(f) + (1.0 - f) * math.log(1.0 - f))
    total = ks_sum - dc_total + e_int_total
    free = total - params.T * entropy
    scalar_total = vol * grid.integrate(s_c)
    lam_s_over_m = np.abs(params.lam * grid.density_factor * s_c) / params.m
    return {"ksSum": ks_sum, "nTotal": n_total, "interaction": e_int_total, "hartree": hartree,
            "exchange": e_int_total - hartree, "doubleCounting": dc_total, "total": total,
            "entropy": entropy, "free": free, "grand": free - mu * n_total,
            "scalarCharge": scalar_total, "maxLambdaSOverM": float(np.max(lam_s_over_m)),
            "meanLambdaSOverM": float(grid.integrate(lam_s_over_m * grid.volume_factor)
                                      / grid.integrate(grid.volume_factor))}


class Anderson:
    """Anderson (Pulay) mixing on a flat vector; same algorithm family as the
    Rust crate (normal equations of the residual differences)."""

    def __init__(self, beta, history):
        self.beta = beta
        self.history = history
        self.inputs = []
        self.residuals = []

    def step(self, x_in, x_out):
        r = x_out - x_in
        self.inputs.append(x_in.copy())
        self.residuals.append(r.copy())
        if len(self.inputs) > self.history + 1:
            self.inputs.pop(0)
            self.residuals.pop(0)
        m = len(self.inputs) - 1
        nxt = x_in + self.beta * r
        if m == 0:
            return nxt
        dr = np.array([self.residuals[i] - self.residuals[-1] for i in range(m)])
        dx = np.array([self.inputs[i] - self.inputs[-1] for i in range(m)])
        A = dr @ dr.T
        A += 1e-12 * max(np.trace(A), 1e-300) * np.eye(m)
        rhs = dr @ r
        try:
            gamma = np.linalg.solve(A, rhs)
        except np.linalg.LinAlgError:
            return nxt
        return nxt - gamma @ (dx + self.beta * dr)


def free_window(params: Params, grid: Grid):
    """Initial energy window from the free spectrum (lambda = 0)."""
    m_eff = np.full(grid.N + 1, params.m)
    v = np.zeros(grid.N + 1)
    top = params.m + 4.0 + 3.0 * (params.N / 8.0) ** (1.0 / 3.0) * params.delta_k + 2.0 * math.pi / params.L
    spec = Spectrum(params, grid, m_eff, v, -top, top)
    mu, homo, lumo = occupy_zero(spec.states, params.N)
    return mu, spec


def window_for(params: Params, mu):
    """Energy window around mu: T = 0 needs a small margin above the HOMO
    (LUMO and gap), T > 0 the 32 T band on both sides."""
    if params.T <= 0.0:
        margin = 2.0 + math.pi / params.L
        return -params.m - 1.0, mu + margin
    return mu - WINDOW_FACTOR * params.T, mu + WINDOW_FACTOR * params.T


def occupy(spec: Spectrum, params: Params, mode, constrained=None):
    if mode == "zero":
        mu, homo, lumo = occupy_zero(spec.states, params.N)
        return mu, homo, lumo
    if mode == "thermal":
        return occupy_thermal(spec.states, params.N, params.T)
    if mode == "constrained":
        mu, total = occupy_constrained(spec.states, constrained)
        return mu, None, None
    raise ValueError(mode)


def scf(params: Params, grid: Grid, mode="auto", constrained=None, initial=None, log=None):
    """Self-consistent solution of one sector on one grid.

    mode: "zero" (T = 0 filling), "thermal", "constrained" (Delta-SCF) or
    "auto" (zero if T == 0 else thermal).  initial: optional (n_c, s_c)
    starting densities on this grid (from a coarser level).  Returns a dict
    with the converged spectrum, densities, potentials, energies, history.
    """
    if mode == "auto":
        mode = "zero" if params.T <= 0.0 else "thermal"
    lda = None
    if params.xc == "lda-n":
        n_est = params.N / (params.volume * (1 - math.exp(-6 * params.L)) / 6.0) * math.exp(6 * params.L)
        lda = LdaTable(params.T, params.m, n_est)
    mu, spec = free_window(params, grid)
    if initial is None:
        if mode == "thermal":
            lo, hi = window_for(params, mu)
            spec = Spectrum(params, grid, np.full(grid.N + 1, params.m), np.zeros(grid.N + 1), lo, hi)
            mu, _, _ = occupy(spec, params, mode, constrained)
        elif mode == "constrained":
            mu, _, _ = occupy(spec, params, mode, constrained)
        n_c, s_c = densities(spec.states, params, grid)
    else:
        n_c, s_c = initial
    mixer = Anderson(params.mix_beta, params.mix_history)
    history = []
    x_in = np.concatenate([n_c, s_c])
    converged = False
    result = None
    for it in range(1, params.max_iter + 1):
        n_in, s_in = x_in[:grid.N + 1], x_in[grid.N + 1:]
        m_eff, v, e_int, dc = potentials(params, grid, n_in, s_in, lda)
        lo, hi = window_for(params, mu)
        spec = Spectrum(params, grid, m_eff, v, lo, hi)
        mu, homo, lumo = occupy(spec, params, mode, constrained)
        # enlarge the window if mu moved too close to its edge
        lo2, hi2 = window_for(params, mu)
        if lo2 < lo or hi2 > hi:
            spec = Spectrum(params, grid, m_eff, v, min(lo, lo2), max(hi, hi2))
            mu, homo, lumo = occupy(spec, params, mode, constrained)
        n_out, s_out = densities(spec.states, params, grid)
        x_out = np.concatenate([n_out, s_out])
        res_n = float(np.max(np.abs(n_out - n_in)) / max(np.max(np.abs(n_out)), 1e-300))
        res_s = float(np.max(np.abs(s_out - s_in)) / max(np.max(np.abs(s_out)), 1e-300))
        en = energies(spec.states, params, grid, n_out, s_out, e_int, dc, mu)
        history.append({"iteration": it, "residualN": res_n, "residualS": res_s, "mu": mu,
                        "energy": en["total"], "free": en["free"], "states": len(spec.states),
                        "shellsExact": spec.shells_exact, "shellsInterpolated": spec.shells_interpolated})
        if log:
            log("    it %3d  resN %.3e resS %.3e  mu %.10f  E %.12f  states %d" %
                (it, res_n, res_s, mu, en["total"], len(spec.states)))
        sea_top, particle_bottom = branch_overlap(spec.states)
        result = {"spectrum": spec, "n_c": n_out, "s_c": s_out, "m_eff": m_eff, "v": v, "e_int": e_int,
                  "dc": dc, "mu": mu, "homo": homo, "lumo": lumo, "energies": en, "history": history,
                  "iterations": it, "residualN": res_n, "residualS": res_s, "mode": mode,
                  "seaTop": sea_top, "particleBottom": particle_bottom,
                  "branchOverlap": bool(sea_top > particle_bottom)}
        if res_n < params.tol and res_s < params.tol:
            converged = True
            break
        x_in = mixer.step(x_in, x_out)
        # keep the input densities physically sane (no NaN)
        if not np.all(np.isfinite(x_in)):
            raise RuntimeError("scf: non-finite densities at iteration %d" % it)
    result["converged"] = converged
    # the potentials of the converged output densities (what the observables use)
    m_eff, v, e_int, dc = potentials(params, grid, result["n_c"], result["s_c"], lda)
    result["m_eff_out"] = m_eff
    result["v_out"] = v
    result["e_int_out"] = e_int
    result["dc_out"] = dc
    return result


# ---------------------------------------------------------------------------
# 8. Observables of a converged sector: profiles, EMT, spectrum tables
# ---------------------------------------------------------------------------

def emt_profiles(result, params: Params, grid: Grid):
    """Energy-momentum profiles of the KS state (proper densities) from the
    per-state bilinears (Stage-2 EMT reduced to the ansatz):
      rho  = K_4 - L_s,   K_4 = e^{-6Hy} sum mult w eps |chi|^2 / l^3
      p_y  = -K_y + L_s,  K_y = e^{-6Hy} sum mult w [-(eps - v) n + M_eff s - s_type k kappa z] / l^3
      p_3  = -K_1 + L_s,  K_1 = e^{-6Hy} (1/3) sum mult w s_type k kappa z / l^3  (shell average)
      p_t  = L_s          (no extra-time momentum)
      L_s  = (M_eff - m) S_p + v_x n_p - e_int  (= (lambda/2) S_p^2 + e_x in mode quadratic).
    Also returns the finite-difference check of K_y from the eigenvectors
    (the identity K_y + K_1 + K_4 = M_eff S_p + v_x n_p per state is exact
    for the discrete eigenvectors only up to the derivative approximation).
    """
    kap = kappa_of(grid.y, params.a4)
    inv_v = 1.0 / params.volume
    K4 = np.zeros(grid.N + 1)
    Ky = np.zeros(grid.N + 1)
    K1 = np.zeros(grid.N + 1)
    m_eff = result["m_eff_out"]
    v = result["v_out"]
    for st in result["spectrum"].states:
        if st.w == 0.0:
            continue
        wgt = st.mult * st.w * inv_v
        K4 += wgt * st.eps * st.n
        Ky += wgt * (-(st.eps - v) * st.n + m_eff * st.s - st.type * st.k * kap * st.z)
        K1 += wgt * (st.type * st.k * kap * st.z) / 3.0
    df = grid.density_factor
    n_p = df * result["n_c"]
    s_p = df * result["s_c"]
    L_s = result["dc_out"] - result["e_int_out"]
    rho = df * K4 - L_s
    p_y = -df * Ky + L_s
    p_3 = -df * K1 + L_s
    p_t = L_s.copy()
    trace_residual = (-rho + p_y + 3 * p_3 + 3 * p_t) - (-(m_eff * s_p + v * n_p) + 8 * L_s)
    # y-conservation nabla_mu T^mu_y = p_y' + 6H p_y - 3H p_3 - 3H p_t = 0.  Written
    # for the coordinate-volume quantities P = e^{6Hy} p (smooth in y, no e^{-6Hy}
    # amplification of the difference error): P_y' = 3H (P_3 + P_t).  Fourth-order
    # central differences on the interior nodes.
    P_y = grid.volume_factor * p_y
    P_3 = grid.volume_factor * p_3
    P_t = grid.volume_factor * p_t
    h = grid.h
    dPy = np.full_like(P_y, np.nan)
    if grid.N >= 4:
        dPy[2:-2] = (-P_y[4:] + 8.0 * P_y[3:-1] - 8.0 * P_y[1:-3] + P_y[:-4]) / (12.0 * h)
    conservation = dPy - 3.0 * (P_3 + P_t)
    # stencils touching the end nodes are excluded: the end-node values are only
    # first-order accurate (they are derived through g~/h, see extrapolate_profile)
    inner = slice(3, grid.N - 2)
    scale = max(float(np.max(np.abs(dPy[inner]))), float(np.max(np.abs(3.0 * (P_3 + P_t)[inner]))), 1e-300)
    if scale < 1e-14 * max(float(np.max(np.abs(P_y))), 1e-300) or scale <= 1e-300:
        normalised = 0.0
    else:
        normalised = float(np.max(np.abs(conservation[inner])) / scale)
    return {"rho": rho, "p_y": p_y, "p_3": p_3, "p_t": p_t, "L_s": L_s, "n_p": n_p, "s_p": s_p,
            "K4": df * K4, "Ky": df * Ky, "K1": df * K1,
            "traceIdentityResidual": float(np.max(np.abs(trace_residual))),
            "conservationResidual": conservation,
            "conservationResidualMaxNormalised": normalised}


def proper_average(grid: Grid, values):
    return grid.integrate(values * grid.volume_factor) / grid.integrate(grid.volume_factor)


def emt_summary(prof, params: Params, grid: Grid, result):
    avg = {name: proper_average(grid, prof[name]) for name in ("rho", "p_y", "p_3", "p_t", "L_s")}
    rho = avg["rho"]
    energy_check = params.volume * grid.integrate(prof["rho"] * grid.volume_factor)
    # brane-localised fraction: particles within one warp length |y| < 1/H of the brane
    mask = grid.y >= -1.0
    w_brane = grid.w.copy()
    w_brane[~mask] = 0.0
    if mask.any():
        first = int(np.argmax(mask))
        if first > 0:   # partial cell at y = -1 handled by the trapezoid weights of the nodes >= -1
            w_brane[first] = 0.5 * grid.h
    frac = params.volume * float(np.dot(w_brane, result["n_c"])) / params.N if params.N else float("nan")
    out = {"averages": avg,
           "conservationResidualMaxNormalised": prof["conservationResidualMaxNormalised"],
           "w_y": avg["p_y"] / rho if rho else float("nan"),
           "w_3": avg["p_3"] / rho if rho else float("nan"),
           "w_t": avg["p_t"] / rho if rho else float("nan"),
           "w_mean": (avg["p_y"] + 3 * avg["p_3"] + 3 * avg["p_t"]) / (7 * rho) if rho else float("nan"),
           "energyFromRho": energy_check,
           "braneLocalisedFraction": frac,
           "traceIdentityResidual": prof["traceIdentityResidual"],
           "rhoRequired_kappa1": -21.0,
           "pRequired_kappa1": 15.0,
           "kappaNeededForRho": (-21.0 / rho) if rho else float("nan"),
           "mismatch": "the KS energy density is positive; the field requires rho_req = -21 H^2/kappa < 0 "
                       "(and p_req = +15 H^2/kappa, w_req = -5/7): no positive kappa can source it"}
    return out


def key_str(key):
    """q:parity:type:index"""
    return "%d:%+d:%+d:%d" % key


class SectorRun:
    """Three-level solution of one sector with Richardson extrapolation."""

    def __init__(self, params: Params, mode="auto", constrained=None, log=None, initial=None):
        self.params = params
        self.mode = mode
        self.levels = []
        self.grids = []
        prev = None
        for lvl in range(params.levels):
            N = params.N0 * 2 ** lvl
            grid = Grid(params.L, N)
            init = None
            if prev is not None:
                init = (np.interp(grid.y, prev[0].y, prev[1]["n_c"]), np.interp(grid.y, prev[0].y, prev[1]["s_c"]))
            elif initial is not None:
                init = initial
            if log:
                log("  level %d (N = %d)" % (lvl, N))
            res = scf(params, grid, mode=mode, constrained=constrained, initial=init, log=log)
            self.grids.append(grid)
            self.levels.append(res)
            prev = (grid, res)
        self.extrapolate()

    def extrapolate(self):
        p = self.params
        fine = self.levels[-1]
        # scalars
        names = ["total", "free", "entropy", "ksSum", "interaction", "hartree", "exchange", "grand",
                 "scalarCharge", "nTotal"]
        self.scalars = {}
        self.orders = {}
        for name in names:
            vals = [lv["energies"][name] for lv in self.levels]
            self.scalars[name] = extrapolate_values(vals)
            self.orders[name] = order_estimate(*vals) if len(vals) == 3 else float("nan")
        mus = [lv["mu"] for lv in self.levels]
        self.scalars["mu"] = extrapolate_values(mus)
        self.orders["mu"] = order_estimate(*mus) if len(mus) == 3 else float("nan")
        # states matched by key
        keyed = [{st.key(): st for st in lv["spectrum"].states} for lv in self.levels]
        common = [k for k in keyed[-1] if all(k in d for d in keyed)]
        common.sort(key=lambda k: (keyed[-1][k].eps, k))
        self.state_keys = common
        self.state_eps = {}
        for k in common:
            vals = [d[k].eps for d in keyed]
            self.state_eps[k] = (vals, extrapolate_values(vals))
        eps_orders = [order_estimate(*self.state_eps[k][0]) for k in common
                      if len(self.state_eps[k][0]) == 3 and abs(keyed[-1][k].w) > 1e-6]
        eps_orders = [o for o in eps_orders if math.isfinite(o)]
        self.orders["occupiedEigenvalues_median"] = float(np.median(eps_orders)) if eps_orders else float("nan")
        # profiles on the coarse nodes
        coarse = self.grids[0]
        step = [2 ** (len(self.levels) - 1 - l) for l in range(len(self.levels))]
        # per level: node subsets that coincide with the coarse nodes
        sub = [np.arange(0, self.grids[l].N + 1, 2 ** l) for l in range(len(self.levels))]
        self.profiles = {}
        prof_names = ["n_c", "s_c", "m_eff_out", "v_out"]
        emts = [emt_profiles(lv, p, g) for lv, g in zip(self.levels, self.grids)]
        for name in prof_names:
            vals = [lv[name][s] for lv, s in zip(self.levels, sub)]
            self.profiles[name] = extrapolate_profile(vals)
            self.orders["profile_" + name] = (order_estimate(*[v[1:-1] for v in vals])
                                              if len(vals) == 3 else float("nan"))
        for name in ("rho", "p_y", "p_3", "p_t", "L_s", "n_p", "s_p"):
            vals = [e[name][s] for e, s in zip(emts, sub)]
            self.profiles[name] = extrapolate_profile(vals)
        self.emt_levels = [emt_summary(e, p, g, lv) for e, g, lv in zip(emts, self.grids, self.levels)]
        self.emt = {}
        for name in ("w_y", "w_3", "w_t", "w_mean", "energyFromRho", "braneLocalisedFraction"):
            vals = [e[name] for e in self.emt_levels]
            self.emt[name] = extrapolate_values(vals)
        self.emt["averages"] = {name: extrapolate_values([e["averages"][name] for e in self.emt_levels])
                                for name in ("rho", "p_y", "p_3", "p_t", "L_s")}
        self.emt["traceIdentityResidual"] = max(e["traceIdentityResidual"] for e in self.emt_levels)
        self.emt["conservationResidualMaxNormalised"] = [e["conservationResidualMaxNormalised"] for e in self.emt_levels]
        self.emt["rhoRequired_kappa1"] = -21.0
        self.emt["pRequired_kappa1"] = 15.0
        self.emt["wRequired"] = -5.0 / 7.0
        rho = self.emt["averages"]["rho"]
        self.emt["kappaNeededForRho"] = (-21.0 / rho) if rho else float("nan")
        self.emt["mismatch"] = self.emt_levels[-1]["mismatch"]
        self.coarse_grid = coarse
        # HOMO / LUMO / gap from the finest level, extrapolated where matched
        homo, lumo = fine["homo"], fine["lumo"]
        self.homo = homo.key() if homo is not None else None
        self.lumo = lumo.key() if lumo is not None else None
        self.gap = None
        if homo is not None and lumo is not None and homo.key() in self.state_eps and lumo.key() in self.state_eps:
            self.gap = self.state_eps[lumo.key()][1] - self.state_eps[homo.key()][1]
        self.converged = all(lv["converged"] for lv in self.levels)

    def summary(self):
        p = self.params
        fine = self.levels[-1]
        return {
            "params": p.to_dict(),
            "mode": fine["mode"],
            "converged": self.converged,
            "levels": [{"N": g.N, "h": g.h, "iterations": lv["iterations"], "converged": lv["converged"],
                        "residualN": lv["residualN"], "residualS": lv["residualS"], "mu": lv["mu"],
                        "seaTop": lv["seaTop"], "particleBottom": lv["particleBottom"],
                        "branchOverlap": lv["branchOverlap"],
                        "energies": lv["energies"], "states": len(lv["spectrum"].states),
                        "shellsExact": lv["spectrum"].shells_exact,
                        "shellsInterpolated": lv["spectrum"].shells_interpolated,
                        "tail": lv["spectrum"].tail}
                       for g, lv in zip(self.grids, self.levels)],
            "extrapolated": dict(self.scalars),
            "orderEstimates": self.orders,
            "homo": key_str(self.homo) if self.homo else None,
            "lumo": key_str(self.lumo) if self.lumo else None,
            "ksGap": self.gap,
            "emt": self.emt,
        }


def extrapolate_profile(vals):
    """Node profiles: (h^2, h^3) elimination in the interior, (h, h^2)
    elimination at the two end nodes.  The end-node values of the staggered
    scheme (f_N at a g-boundary, |g~_{N-1/2}|^2 at an f-boundary) carry a
    first-order error because they are tied to the half-node value g~ ~ h
    through a division by h; eigenvalues, integrals and interior nodes are
    second order.  The (h, h^2) formula also leaves O(h^3) when no h term is
    present, so it is safe at every end node."""
    out = extrapolate_values(vals)
    if len(vals) == 3:
        q1, q2, q4 = (np.asarray(v, dtype=float) for v in vals)
        for j in (0, -1):
            r12 = 2.0 * q2[j] - q1[j]
            r24 = 2.0 * q4[j] - q2[j]
            out[j] = (4.0 * r24 - r12) / 3.0
    return out


def extrapolate_values(vals):
    if len(vals) == 3:
        return extrapolate3(vals[0], vals[1], vals[2])
    if len(vals) == 2:
        return (4.0 * np.asarray(vals[1], dtype=float) - np.asarray(vals[0], dtype=float)) / 3.0
    return np.asarray(vals[-1], dtype=float)


# ---------------------------------------------------------------------------
# 9. Excited states (KS gap, particle-hole list, Delta-SCF) and thermodynamics
# ---------------------------------------------------------------------------

def particle_hole_list(run: SectorRun, count=12):
    fine = run.levels[-1]
    states = fine["spectrum"].states
    occ = [st for st in states if st.branch > 0 and st.f > 1e-12]
    emp = [st for st in states if st.branch > 0 and st.f < 1.0 - 1e-12]
    pairs = []
    for i in occ:
        for a in emp:
            if a.key() == i.key():
                continue
            de = a.eps - i.eps
            if de <= 0:
                continue
            ei = run.state_eps.get(i.key(), ([], i.eps))[1]
            ea = run.state_eps.get(a.key(), ([], a.eps))[1]
            pairs.append({"hole": key_str(i.key()), "particle": key_str(a.key()),
                          "epsHole": float(ei), "epsParticle": float(ea),
                          "excitation": float(ea - ei), "weight": float(i.mult * i.f * a.mult * (1.0 - a.f))})
    pairs.sort(key=lambda d: (d["excitation"], d["hole"], d["particle"]))
    return pairs[:count]


def delta_scf(run: SectorRun, log=None):
    """Constrained-occupation SCF with one particle moved from the HOMO
    group to the LUMO group (symmetric fractional occupation within each
    degenerate group); returns E_1 - E_0 (extrapolated) and details."""
    p = run.params
    fine = run.levels[-1]
    homo, lumo = fine["homo"], fine["lumo"]
    if homo is None or lumo is None or homo.key() == lumo.key():
        return {"available": False, "reason": "no HOMO/LUMO pair (open shell or empty window)"}
    states = fine["spectrum"].states
    def group(ref):
        return [st for st in states if st.branch > 0
                and abs(st.eps - ref.eps) <= DEGENERACY_TOL * max(abs(ref.eps), 1.0)]
    gh = group(homo)
    gl = group(lumo)
    occ = {st.key(): st.f for st in states if st.branch > 0 and st.f > 0}
    mh = sum(st.mult for st in gh)
    ml = sum(st.mult for st in gl)
    for st in gh:
        occ[st.key()] = st.f - 1.0 / mh
    for st in gl:
        occ[st.key()] = occ.get(st.key(), 0.0) + 1.0 / ml
    q = Params(**{**p.to_dict_kwargs(), "label": p.label + "-dscf"})
    if log:
        log("  Delta-SCF: HOMO %s -> LUMO %s" % (key_str(homo.key()), key_str(lumo.key())))
    excited = SectorRun(q, mode="constrained", constrained=occ, log=log,
                        initial=None)
    e1 = excited.scalars["total"]
    e0 = run.scalars["total"]
    return {"available": True, "homo": key_str(homo.key()), "lumo": key_str(lumo.key()),
            "homoMultiplicity": mh, "lumoMultiplicity": ml,
            "E0": float(e0), "E1": float(e1), "deltaSCF": float(e1 - e0),
            "ksGap": run.gap, "nTotalExcited": excited.scalars["nTotal"],
            "converged": excited.converged,
            "levelsE1": [lv["energies"]["total"] for lv in excited.levels],
            "orderEstimateE1": excited.orders["total"]}


def thermo_point(params: Params, T: float, delta=0.05, log=None):
    """E, F, S, mu at T and C_V = dE/dT|_N by central differences (T (1 +- delta))."""
    runs = {}
    for tag, Tv in (("center", T), ("plus", T * (1 + delta)), ("minus", T * (1 - delta))):
        label = params.label if tag == "center" else "%s-T%s" % (params.label, tag)
        q = Params(**{**params.to_dict_kwargs(), "T": Tv, "label": label})
        if log:
            log("  thermo T = %.6f (%s)" % (Tv, tag))
        runs[tag] = SectorRun(q, mode="thermal", log=log)
    c = runs["center"]
    dT = 2 * delta * T
    cv = (runs["plus"].scalars["total"] - runs["minus"].scalars["total"]) / dT
    cv_entropy = T * (runs["plus"].scalars["entropy"] - runs["minus"].scalars["entropy"]) / dT
    return {"T": T, "energy": float(c.scalars["total"]), "free": float(c.scalars["free"]),
            "entropy": float(c.scalars["entropy"]), "mu": float(c.scalars["mu"]),
            "grand": float(c.scalars["grand"]), "C_V": float(cv), "C_V_fromEntropy": float(cv_entropy),
            "delta": delta, "converged": all(r.converged for r in runs.values()),
            "excitations": particle_hole_list(c, 8), "run": c}


# ---------------------------------------------------------------------------
# 10. Deterministic output helpers
# ---------------------------------------------------------------------------

def jsonable(obj):
    """Convert numpy scalars/arrays and non-finite floats for json.dumps."""
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [jsonable(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return [jsonable(v) for v in obj.tolist()]
    if isinstance(obj, (np.floating,)):
        obj = float(obj)
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.bool_,)):
        return bool(obj)
    if isinstance(obj, float):
        return obj if math.isfinite(obj) else None
    if isinstance(obj, (State,)):
        return key_str(obj.key())
    return obj


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(jsonable(obj), indent=2) + "\n")


def fmt(value):
    value = float(value)
    if not math.isfinite(value):
        return "nan"
    return "%.17e" % (value + 0.0)


def write_csv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(",".join(header) + "\n")
        for row in rows:
            handle.write(",".join(fmt(v) for v in row) + "\n")


# ---------------------------------------------------------------------------
# 11. Run outputs
# ---------------------------------------------------------------------------

def write_run(run: SectorRun, directory, extra=None):
    os.makedirs(directory, exist_ok=True)
    fine = run.levels[-1]
    states = {st.key(): st for st in fine["spectrum"].states}
    rows = []
    for key in run.state_keys:
        st = states[key]
        vals, ext = run.state_eps[key]
        row = [st.q, st.r3, st.k, st.parity, st.type, st.index, st.branch, st.mult, st.f, st.w]
        row += list(vals) + [float(ext), 1.0 if st.interpolated else 0.0]
        rows.append(row)
    header = ["q", "r3", "k", "parity", "type", "index", "branch", "mult", "f", "w"]
    header += ["eps_level%d" % l for l in range(len(run.levels))] + ["eps_extrapolated", "interpolated"]
    write_csv(os.path.join(directory, "spectrum.csv"), header, rows)
    g = run.coarse_grid
    prof = run.profiles
    z = np.arcsin(np.minimum(np.exp(6.0 * g.y), 1.0))
    prows = []
    for j in range(g.N + 1):
        prows.append([g.y[j], z[j], g.volume_factor[j], prof["n_c"][j], prof["s_c"][j], prof["n_p"][j],
                      prof["s_p"][j], prof["m_eff_out"][j], prof["v_out"][j], prof["rho"][j],
                      prof["p_y"][j], prof["p_3"][j], prof["p_t"][j], prof["L_s"][j]])
    write_csv(os.path.join(directory, "profiles.csv"),
              ["y", "z", "W6", "n_c", "S_c", "n_p", "S_p", "M_eff", "v_x", "rho", "p_y", "p_3", "p_t", "L_s"],
              prows)
    for l, lv in enumerate(run.levels):
        hrows = [[h["iteration"], h["residualN"], h["residualS"], h["mu"], h["energy"], h["free"],
                  h["states"], h["shellsExact"], h["shellsInterpolated"]] for h in lv["history"]]
        write_csv(os.path.join(directory, "scf-history-level%d.csv" % l),
                  ["iteration", "residualN", "residualS", "mu", "energy", "free", "states",
                   "shellsExact", "shellsInterpolated"], hrows)
    doc = run.summary()
    doc["files"] = sorted(os.listdir(directory)) + ["run.json"]
    if extra:
        doc.update(extra)
    write_json(os.path.join(directory, "run.json"), doc)
    return doc


# ---------------------------------------------------------------------------
# 12. Self-tests (analytic spectra, identities, rescaling)
# ---------------------------------------------------------------------------

def analytic_box(M, L, brane, tip, count=5):
    """Exact k = 0, constant-M spectrum (eps >= 0) for the BC pair.
    like conditions (f,f) or (g,g): p = n pi/L (n >= 1) plus one zero mode
    unlike: tan(pL) = +p/M for (tip f, brane g) and (tip g, brane f) with
    the sign fixed below, plus the bound state tanh(qL) = q/M if ML > 1."""
    eps = []
    like = (brane == tip)
    if like:
        eps.append(0.0)
        for n in range(1, count + 1):
            eps.append(math.sqrt(M * M + (n * math.pi / L) ** 2))
        return sorted(eps)[:count + 1]
    # unlike: (tip f0, brane g0): f = sin(p(y+L)), g(0)=0 -> tan(pL) = p/M ; bound state tanh(qL)=q/M
    #         (tip g0, brane f0): f = sin(py), g(-L)=0 -> tan(pL) = -p/M ; no bound state
    sign = 1.0 if tip == "f0" else -1.0
    fn = lambda p: math.tan(p * L) - sign * p / M
    roots = []
    n = 0
    while len(roots) < count + 2 and n < 200:
        lo = max((n - 0.5) * math.pi / L + 1e-9, 1e-9)
        hi = (n + 0.5) * math.pi / L - 1e-9
        if fn(lo) * fn(hi) < 0:
            a, b = lo, hi
            for _ in range(200):
                mid = 0.5 * (a + b)
                if fn(a) * fn(mid) <= 0:
                    b = mid
                else:
                    a = mid
            pr = 0.5 * (a + b)
            if pr > 1e-6:
                roots.append(pr)
        n += 1
    if sign > 0 and M * L > 1:
        gq = lambda q: math.tanh(q * L) - q / M
        a, b = 1e-9, M - 1e-12
        for _ in range(200):
            mid = 0.5 * (a + b)
            if gq(a) * gq(mid) <= 0:
                b = mid
            else:
                a = mid
        eps.append(math.sqrt(M * M - (0.5 * (a + b)) ** 2))
    for pr in roots:
        eps.append(math.sqrt(M * M + pr * pr))
    return sorted(eps)[:count + 1]


def self_tests(N0=100, L=3.0, M=1.0):
    gam, charge, chirality = load_fixture()
    tests = {"fixtureSha256": sha256_file(DEFAULT_FIXTURE), "clifford": clifford_ok(gam)}
    red = block_reduction(gam, charge)
    tests["blockReduction"] = {k: v for k, v in red.items() if k not in ("unitary_re", "unitary_im")}
    tests["exchangeTraceIdentityDefect"] = exchange_trace_identity(gam, charge)
    tests["gas"] = gas_selfcheck()
    tests["geometry"] = geometry_record()
    # analytic spectra for the four BC combinations, three grids, extrapolated
    spectra = {}
    for tip in ("g0", "f0"):
        for parity in (1, -1):
            brane = "g0" if parity > 0 else "f0"
            exact = analytic_box(M, L, brane, tip, count=4)
            per_level = []
            for lvl in range(3):
                grid = Grid(L, N0 * 2 ** lvl)
                sh = solve_shell(grid, np.full(grid.N + 1, M), np.zeros(grid.N + 1), 0.0, 0.0, parity, tip, False)
                e = sh["eps"][sh["type"] == 1]
                e = np.sort(e[e >= -ZERO_MODE_TOL])[:len(exact)]
                per_level.append(e)
            ext = extrapolate3(*per_level)
            spectra["tip_%s_parity_%+d" % (tip, parity)] = {
                "analytic": exact, "levels": [x.tolist() for x in per_level], "extrapolated": ext.tolist(),
                "maxAbsError": float(np.max(np.abs(ext - np.array(exact)))),
                "maxAbsErrorFinest": float(np.max(np.abs(per_level[-1] - np.array(exact)))),
                "orderEstimate": order_estimate(*per_level),
                "zeroMode": bool(brane == tip)}
    tests["analyticSpectra"] = spectra
    tests["analyticMaxError"] = max(v["maxAbsError"] for v in spectra.values())
    # discrete Hellmann-Feynman identities at k = 0.7 with a smooth potential
    grid = Grid(L, N0)
    Mn = M + 0.2 * np.exp(grid.y)
    vn = 0.1 * np.sin(grid.y)
    k = 0.7
    sh = solve_shell(grid, Mn, vn, k, 0.0, 1, "g0", True)
    i = int(np.argmin(np.abs(sh["eps"] - 2.0)))
    d = 1e-6
    ep = solve_shell(grid, Mn + d, vn, k, 0.0, 1, "g0", True)["eps"][i]
    em = solve_shell(grid, Mn - d, vn, k, 0.0, 1, "g0", True)["eps"][i]
    hf_m = abs((ep - em) / (2 * d) - grid.integrate(sh["s"][i]))
    ep = solve_shell(grid, Mn, vn + d, k, 0.0, 1, "g0", True)["eps"][i]
    em = solve_shell(grid, Mn, vn - d, k, 0.0, 1, "g0", True)["eps"][i]
    hf_v = abs((ep - em) / (2 * d) - sh["type"][i] * grid.integrate(sh["n"][i]))
    ep = solve_shell(grid, Mn, vn, k + d, 0.0, 1, "g0", True)["eps"][i]
    em = solve_shell(grid, Mn, vn, k - d, 0.0, 1, "g0", True)["eps"][i]
    hf_k = abs((ep - em) / (2 * d) + sh["type"][i] * grid.integrate(kappa_of(grid.y, 0.0) * sh["z"][i]))
    tests["hellmannFeynman"] = {"dEps_dM_vs_scalarDensity": hf_m, "dEps_dv_vs_number": hf_v,
                               "dEps_dk_vs_pressureBilinear": hf_k, "norm": grid.integrate(sh["n"][i])}
    # the free dispersion of the staggered scheme has no doubler
    grid2 = Grid(L, 40)
    hs, _, _ = build_hamiltonian(grid2, np.zeros(41), np.zeros(41), np.zeros(40), np.zeros(41), 1, "g0")
    ev = np.sort(np.abs(np.linalg.eigvalsh(hs)))
    tests["freeDispersion"] = {"maxEigenvalue": float(ev[-1]), "twoOverH": 2.0 / grid2.h,
                               "doublerFree": bool(ev[-1] <= 2.0 / grid2.h * (1 + 1e-9))}
    return tests


def rescaling_test(lambda_hat, N=8.0, L=3.0, N0=64, levels=2):
    """a4_0 = 0.5 equals a4_0 = 0 with every lattice momentum rescaled by
    e^{-a4_0} (same l^3 in the density normalisation)."""
    a = Params(m=1.0, a4=0.5, L=L, lambda_hat=lambda_hat, N=N, parity=1, N0=N0, levels=levels, label="a4-0.5")
    b = Params(m=1.0, a4=0.0, L=L, lambda_hat=lambda_hat, N=N, parity=1, N0=N0, levels=levels,
               delta_k=0.25 * math.exp(-0.5), ell=2.0 * math.pi / 0.25, label="a4-0-rescaled")
    ra = SectorRun(a)
    rb = SectorRun(b)
    common = [k for k in ra.state_keys if k in rb.state_eps]
    de = max(abs(ra.state_eps[k][1] - rb.state_eps[k][1]) for k in common) if common else float("nan")
    return {"lambda_hat": lambda_hat, "E0_a4_0.5": float(ra.scalars["total"]), "E0_rescaled": float(rb.scalars["total"]),
            "maxEigenvalueDifference": float(de), "statesCompared": len(common),
            "E0Difference": float(abs(ra.scalars["total"] - rb.scalars["total"]))}


# ---------------------------------------------------------------------------
# 13. Canonical parameter set and the command line
# ---------------------------------------------------------------------------

def closed_shells(m=1.0, L=3.0, N0=64, upto=1300, parity=0):
    """Cumulative degeneracies of the free spectrum (both parities filled
    together for parity = 0, the Rust convention): closed-shell N."""
    p = Params(m=m, L=L, lambda_hat=0.0, T=0.0, N=upto, parity=parity, N0=N0)
    grid = Grid(L, N0)
    res = scf(p, grid)
    parts = sorted((st for st in res["spectrum"].states if st.branch > 0), key=lambda st: st.eps)
    shells = []
    total = 0.0
    i = 0
    while i < len(parts):
        e = parts[i].eps
        j = i
        mult = 0.0
        while j < len(parts) and abs(parts[j].eps - e) <= DEGENERACY_TOL * max(abs(e), 1.0):
            mult += parts[j].mult
            j += 1
        total += mult
        shells.append({"eps": e, "multiplicity": mult, "cumulative": total,
                       "levels": [key_str(st.key()) for st in parts[i:j]]})
        i = j
        if total >= upto:
            break
    return shells


def reference_scale(N_mid, m=1.0, L=3.0, N0=64, levels=3, log=None):
    """S_ref = max_y |S_p(y)| of the free N_mid ground state (both parities
    filled together), from the three-level extrapolated proper scalar
    density; lambda_hat_1 = 0.1/S_ref, lambda_hat_2 = 1/S_ref (the Rust
    crate's rule, so that |lambda S_p|/m reaches 0.1 and 1.0 in that state)."""
    p = Params(m=m, L=L, lambda_hat=0.0, T=0.0, N=N_mid, parity=0, N0=N0, levels=levels, label="reference-scale")
    run = SectorRun(p, log=log)
    s_p = np.abs(np.asarray(run.profiles["s_p"], dtype=float))
    j = int(np.argmax(s_p))
    S_ref = float(s_p[j])
    if not S_ref > 0.0:
        raise RuntimeError("reference_scale: S_ref vanishes")
    return {"S_ref": S_ref, "argmax_y": float(run.coarse_grid.y[j]), "N_mid": float(N_mid), "m": m, "L": L,
            "lambda_hat_1": 0.1 / S_ref, "lambda_hat_2": 1.0 / S_ref, "E0_free_N_mid": float(run.scalars["total"]),
            "levels": [float(np.max(np.abs(np.asarray(lv["s_c"]) * g.density_factor)))
                       for lv, g in zip(run.levels, run.grids)]}


LAMBDA_NAMES = {"lam0": 0.0, "lamp1": "l1", "lamm1": "-l1", "lamp2": "l2", "lamm2": "-l2"}


def rust_label(m, L, N, lam_name, T, a4=0.0, delta_k_over_m=0.25):
    """Labels in the form of the Rust crate: m1_L3_N8_lamp1_T0[_a40p5][_dk0p125]."""
    def trim(v):
        return ("%g" % v).replace(".", "p").replace("-", "m")
    lab = "m%s_L%s_N%s_%s_T%s" % (trim(m), trim(L), N if isinstance(N, str) else int(N), lam_name,
                                   "0" if T == 0 else trim(T / m))
    if a4 != 0.0:
        lab += "_a4" + trim(a4)
    if delta_k_over_m != 0.25:
        lab += "_dk" + trim(delta_k_over_m)
    return lab


def canonical_runs(quick=False):
    """The list of run specifications (dicts of Params kwargs + tasks).
    Symbolic N ("mid", "big") and lambda_hat ("l1", "-l1", "l2", "-l2")
    are resolved by `resolve_run` from the closed shells and S_ref."""
    N0 = 48 if quick else 64
    levels = 2 if quick else 3
    runs = []
    base = {"L": 3.0, "N0": N0, "levels": levels, "tip": "g0", "xc": "quadratic", "parity": 0}
    if quick:
        runs.append({"label": rust_label(1, 3, 8, "lam0", 0), "m": 1.0, "lambda_hat": 0.0, "N": 8, "T": 0.0,
                     "tasks": ["excited", "emt"], **base})
        runs.append({"label": rust_label(1, 3, 8, "lamp1", 0), "m": 1.0, "lambda_hat": "l1", "N": 8, "T": 0.0,
                     "tasks": ["excited"], **base})
        runs.append({"label": rust_label(1, 3, 8, "lam0", 0.3), "m": 1.0, "lambda_hat": 0.0, "N": 8, "T": 0.3,
                     "tasks": ["thermo"], **base})
        runs.append({"label": "L2-free-N8-p-1", "m": 1.0, "lambda_hat": 0.0, "N": 8, "T": 0.0,
                     "tasks": ["excited"], **{**base, "L": 2.0, "parity": -1}})
        return runs
    # A. L-dependence of the two parity sectors (free, N = 8)
    for L in (2.0, 3.0, 4.0):
        for parity in (1, -1):
            runs.append({"label": "L%.0f-free-N8-p%+d" % (L, parity), "m": 1.0, "lambda_hat": 0.0, "N": 8,
                         "T": 0.0, "tasks": ["excited"], **{**base, "L": L, "parity": parity}})
    # B. ground states at T = 0, m = 1, L = 3 (the Rust matrix; both parities together)
    for Nname in ("8", "mid", "big"):
        for lam_name, lam in LAMBDA_NAMES.items():
            tasks = ["excited"] if (Nname != "big" or lam_name in ("lam0", "lamp1")) else []
            runs.append({"label": rust_label(1, 3, Nname, lam_name, 0), "m": 1.0, "lambda_hat": lam,
                         "N": Nname, "T": 0.0, "tasks": tasks, **base})
    # C. m = 3
    for Nname in ("8", "mid"):
        for lam_name in ("lam0", "lamp1", "lamm1"):
            runs.append({"label": rust_label(3, 3, Nname, lam_name, 0), "m": 3.0,
                         "lambda_hat": LAMBDA_NAMES[lam_name], "N": Nname, "T": 0.0, "tasks": [], **base})
    # D. L = 2, 4 (N_mid, lambda_hat 0 and lambda_hat_1)
    for L in (2.0, 4.0):
        for lam_name in ("lam0", "lamp1"):
            runs.append({"label": rust_label(1, L, "mid", lam_name, 0), "m": 1.0, "lambda_hat": LAMBDA_NAMES[lam_name],
                         "N": "mid", "T": 0.0, "tasks": [], **{**base, "L": L}})
    # E. Delta k halved at the same density (N x 8)
    runs.append({"label": rust_label(1, 3, "8mid", "lamp1", 0, delta_k_over_m=0.125), "m": 1.0, "lambda_hat": "l1",
                 "N": "8mid", "T": 0.0, "tasks": [], "delta_k_over_m": 0.125, **base})
    # F. thermodynamics (C_V by central differences, see thermo_point)
    for Nname in ("8", "mid"):
        for lam_name in ("lam0", "lamp1"):
            for T in (0.1, 0.3, 1.0):
                runs.append({"label": rust_label(1, 3, Nname, lam_name, T), "m": 1.0,
                             "lambda_hat": LAMBDA_NAMES[lam_name], "N": Nname, "T": T, "tasks": ["thermo"],
                             **{**base, "N0": 48}})
    return runs


def resolve_run(spec, shells_info, couplings):
    """Replace symbolic N ("8", "mid", "big", "8mid") and lambda ("l1",
    "-l1", "l2", "-l2") by numbers and the symbolic label parts by them."""
    spec = dict(spec)
    Nsym = spec["N"]
    if isinstance(Nsym, str):
        Nval = 8.0 * shells_info["N_mid"] if Nsym == "8mid" else shells_info["N_" + Nsym]
        spec["N"] = float(Nval)
        spec["label"] = spec["label"].replace("_N" + Nsym + "_", "_N%d_" % int(Nval))
    lam = spec["lambda_hat"]
    if isinstance(lam, str):
        sign = -1.0 if lam.startswith("-") else 1.0
        name = lam.lstrip("-")
        spec["lambda_hat"] = sign * couplings["lambda_hat_" + name[1:]]
    return spec


def run_matches(doc, spec):
    """Does an existing run.json reproduce the parameter set of spec (--resume)?"""
    try:
        p = doc["params"]
        q = Params(**{k: v for k, v in spec.items() if k != "tasks"}).to_dict()
        keys = ("m", "a4_0", "L", "lambda_hat", "T", "N", "parity", "tip", "xc", "sea", "delta_k", "ell",
                "N0", "levels", "tol")
        same = all(p.get(k) == q[k] for k in keys)
        tasks = spec.get("tasks", [])
        if "excited" in tasks and spec.get("T", 0.0) <= 0 and "excited" not in doc:
            return False
        if "thermo" in tasks and spec.get("T", 0.0) > 0 and "thermo" not in doc:
            return False
        return bool(same and doc.get("converged"))
    except Exception:  # noqa: BLE001
        return False


def execute_run(spec, output_root, log):
    spec = dict(spec)
    tasks = spec.pop("tasks", [])
    label = spec["label"]
    params = Params(**spec)
    log("run %s: %s" % (label, json.dumps(jsonable(params.to_dict()))))
    directory = os.path.join(output_root, label)
    extra = {}
    t0 = time.time()
    if params.T > 0 and "thermo" in tasks:
        point = thermo_point(params, params.T, log=log)
        run = point.pop("run")
        extra["thermo"] = point
    else:
        run = SectorRun(params, log=log)
    if "excited" in tasks and params.T <= 0:
        extra["excited"] = {"ksGap": run.gap, "particleHole": particle_hole_list(run),
                            "deltaSCF": delta_scf(run, log=log)}
    extra["tasks"] = tasks
    doc = write_run(run, directory, extra)
    log("  -> %s: E0 = %.12f  mu = %.10f  converged = %s  gap = %s  (%.0f s)" %
        (label, run.scalars["total"], run.scalars["mu"], run.converged, run.gap, time.time() - t0))
    return doc


def execute_run_worker(spec, output_root):
    """Process-pool entry: run one specification, log with the label prefix."""
    label = spec["label"]

    def log(msg):
        print("[%s] %s" % (label, msg), flush=True)

    try:
        return execute_run(spec, output_root, log)
    except Exception as error:  # noqa: BLE001
        log("FAILED: %r" % (error,))
        return {"params": {"label": label}, "failed": repr(error), "converged": False}


def summary_record(doc):
    return {"label": doc["params"]["label"], "params": doc["params"], "converged": doc.get("converged", False),
            "failed": doc.get("failed"), "extrapolated": doc.get("extrapolated"), "ksGap": doc.get("ksGap"),
            "homo": doc.get("homo"), "lumo": doc.get("lumo"), "emt": doc.get("emt"),
            "orderEstimates": doc.get("orderEstimates"),
            "branchOverlap": any(lv.get("branchOverlap") for lv in doc.get("levels", [])),
            "thermo": {k: v for k, v in (doc.get("thermo") or {}).items() if k != "excitations"},
            "excited": doc.get("excited")}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--quick", action="store_true", help="reduced parameter set (tests)")
    parser.add_argument("--runs", default=None, help="comma-separated run labels to execute (symbolic labels "
                        "such as m1_L3_Nmid_lamp1_T0 or resolved ones such as m1_L3_N112_lamp1_T0)")
    parser.add_argument("--config", default=None, help="JSON file with one run specification (Params kwargs + tasks)")
    parser.add_argument("--skip-self-tests", action="store_true")
    parser.add_argument("--workers", type=int, default=None,
                        help="parallel worker processes for the runs (default min(4, cpu/2))")
    parser.add_argument("--resume", action="store_true",
                        help="keep run directories whose run.json already matches the parameter set")
    args = parser.parse_args(argv)
    t_start = time.time()

    def log(msg):
        print(msg, flush=True)

    os.makedirs(args.output, exist_ok=True)
    if args.config:
        with open(args.config, "r", encoding="utf-8") as handle:
            spec = json.load(handle)
        execute_run(spec, args.output, log)
        log("done in %.1f s" % (time.time() - t_start))
        return 0
    workers = args.workers if args.workers is not None else max(1, min(4, (os.cpu_count() or 2) // 2))
    summary = {"schemaVersion": SCHEMA_VERSION, "producer": PRODUCER,
               "fixtureSha256": sha256_file(DEFAULT_FIXTURE),
               "method": "staggered-grid (Yee) real-symmetric matrix eigensolver, three grids N0, 2N0, 4N0, "
                         "extrapolation eliminating h^2 and h^3; Anderson-mixed SCF on (n_c, S_c); "
                         "particle/sea branches by continuity from lambda = 0 (rank against the free spectrum)",
               "conventions": {"sea": "free", "parity": "0 = both Z2 sectors filled together (Rust convention); "
                               "+1/-1 = one sector", "xc": "quadratic: M_eff = m + (15/16) lambda S_p, "
                               "v_x = -lambda n_p/16, e_x = -(lambda/32)(n_p^2 + S_p^2)"},
               "quick": bool(args.quick)}
    if not args.skip_self_tests:
        log("self-tests")
        summary["selfTests"] = self_tests(N0=64 if args.quick else 100)
        summary["selfTests"]["rescaling"] = rescaling_test(0.0 if args.quick else 0.009, N0=48 if args.quick else 64,
                                                            levels=2)
        log("  analytic k = 0 spectra: max error %.3e" % summary["selfTests"]["analyticMaxError"])
    runs = canonical_runs(args.quick)
    N0_ref = 48 if args.quick else 64
    log("closed shells (free, both parities, m = 1, L = 3)")
    shells = closed_shells(N0=N0_ref)
    cum = [s["cumulative"] for s in shells if s["cumulative"] > 8.0]
    def nearest(target):
        return float(min(cum, key=lambda c: abs(c - target)))
    shells_info = {"N_8": 8.0, "N_mid": nearest(100.0), "N_big": nearest(1000.0), "closedShells": shells[:40]}
    summary["closedShells"] = shells_info
    log("  N_mid = %g, N_big = %g" % (shells_info["N_mid"], shells_info["N_big"]))
    log("reference scale S_ref (free N_mid ground state)")
    couplings = reference_scale(shells_info["N_mid"], N0=N0_ref, levels=2 if args.quick else 3)
    log("  S_ref = %.10g at y = %.4f -> lambda_hat_1 = %.10g, lambda_hat_2 = %.10g"
        % (couplings["S_ref"], couplings["argmax_y"], couplings["lambda_hat_1"], couplings["lambda_hat_2"]))
    summary["couplings"] = couplings
    summary["couplingRule"] = ("lambda_hat_1 = 0.1/S_ref, lambda_hat_2 = 1.0/S_ref, S_ref = max_y |S_p(y)| of the free "
                               "N_mid ground state at m = 1, L = 3 with both parities filled together (the Rust "
                               "crate's rule; |lambda S_p|/m reaches 0.1 and 1 there); the same values are used "
                               "at m = 3 and the achieved max |lambda S_p|/m is recorded per run")
    specs = [resolve_run(r, shells_info, couplings) for r in runs]
    if args.runs:
        wanted = set(args.runs.split(","))
        specs = [s for s, r in zip(specs, runs) if s["label"] in wanted or r["label"] in wanted]
    labels = [s["label"] for s in specs]
    docs = {}
    todo = []
    for spec in specs:
        path = os.path.join(args.output, spec["label"], "run.json")
        if args.resume and os.path.exists(path):
            with open(path, "r", encoding="utf-8") as handle:
                doc = json.load(handle)
            if run_matches(doc, spec):
                docs[spec["label"]] = doc
                log("resume: keeping %s" % spec["label"])
                continue
        todo.append(spec)
    log("%d runs (%d kept from a previous run), %d workers" % (len(specs), len(docs), workers))

    def flush(complete):
        summary["runs"] = [summary_record(docs[lab]) for lab in labels if lab in docs]
        summary["complete"] = bool(complete)
        write_json(os.path.join(args.output, "reference-summary.json"), summary)

    flush(False)
    if workers <= 1 or len(todo) <= 1:
        for spec in todo:
            docs[spec["label"]] = execute_run_worker(spec, args.output)
            flush(False)
    else:
        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(execute_run_worker, spec, args.output): spec["label"] for spec in todo}
            for future in concurrent.futures.as_completed(futures):
                docs[futures[future]] = future.result()
                flush(False)
    failed = [lab for lab in labels if docs.get(lab, {}).get("failed")]
    flush(not failed)
    log("wrote %s in %.1f s (%d runs, failed: %s)" % (os.path.join(args.output, "reference-summary.json"),
                                                        time.time() - t_start, len(labels), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
