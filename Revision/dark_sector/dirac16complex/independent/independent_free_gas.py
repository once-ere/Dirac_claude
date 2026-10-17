#!/usr/bin/env python3
"""Revision/dark_sector/dirac16complex/independent/independent_free_gas.py - INDEPENDENT second implementation of
the key numbers of the dark-sector analysis of dirac16complex for the free (lambda = 0) Kohn-Sham gas.

The corrected primordial metric of 2026-10-16 (version 2; Revision/SPEC.md section 1), in the author's coordinates
{x0, x1, ..., x7}: x1, x2, x3 = 3-space (scale factor e^{a4}); x4 = time; x5, x6, x7 = the three exponentially DEFLATING
extra times (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}); x0 = hidden direction, z = 6 H x0 real, y = ln|sin z|/(6H);
the hidden direction carries the scale f = e^{-a4} b4^{1/2}.  The history: a4 = H x4, b4 = e^{(4/3) H x4} (beta = 4/3,
f = e^{-a4/3}), a PRESCRIBED background.

Independent of the Rust solver (different method, different code, no solver output read except for the final
comparison): the 2 x 2 block Hamiltonian of Revision/kohn_sham/ks-theory.json (blockEquation; lambda = 0, so
M_eff = m, v_v = 0), h_j = j[-(i/f) sigma1 d_y + m sigma2 + kappa k sigma3], kappa = e^{-a4} (constant in y), chi = (a, i b),
is discretised by CHEBYSHEV COLLOCATION on y in [-L, 0] (the Rust solver shoots with RK4 and a Pruefer count):
    eps a = j (b'/f + kappa k a + m b),  eps b = j (m a - kappa k b - a'/f),
with b(-L) = 0 (regular tip, theta = 0), b(0) = 0 (fold condition theta = 0, "even") or a(0) = 0 (theta = pi, "odd";
both filled: the ASSUMED convention of ks-theory.json boundaryConditions.fold).  h_{-1} = -h_{+1}.  Filling (the
CONVENTION of ks-theory.json): the positive levels of both block types plus the k = 0 fold zero modes, degeneracy
4 r3(n2) (4 at k = 0) per level and block type, aufbau to N.
The derivative of each level along the history is the Hellmann-Feynman expectation
d eps/d a4 = <chi| d h_{+1}/d a4 |chi>, d h_{+1}/d a4 = [[-kappa k, (1 - beta/2) d_y/f], [-(1 - beta/2) d_y/f, kappa k]]
(the kinetic term from f = e^{(beta/2 - 1) a4}, Clenshaw-Curtis quadrature), so that dE/da4 and w_eff(A) =
-(1/3) d ln E/d a4 are obtained WITHOUT differencing E and without the solver's energy-momentum integrals.

Key numbers recomputed and compared with the primary chain (outputs/ks-history-dense.csv, outputs/eos-summary.json):
E(a4) and w_eff(A) of the free series N_mid and N_large at every slice of the dense history; the CPL tangent wa at
a4_today = 0.5, 1, 1.5, 2; the exact k = 0 spectra (in the proper length f L); the fold-band dispersion eps = kappa |k|;
and (new here) the BULK band: the lowest odd-parity level of one shell, with w_eff(A) = -(1/3) d ln eps/d a4 along
a4 in [-3, 4], versus the occupied fold band.

Writes outputs/independent-free-gas.json and reports/independent-checks.json (deterministic, LF).
"""

import csv
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OWN = HERE.parent
DENSE = OWN / "outputs" / "ks-history-dense.csv"
SUMMARY = OWN / "outputs" / "eos-summary.json"
BETA = 4.0 / 3.0                     # d ln b4/d a4 on the history
CK = 1.0 - 0.5 * BETA                # d ln(1/f)/d a4 = 1 - beta/2 = 1/3
OUT = OWN / "outputs" / "independent-free-gas.json"
REP = OWN / "reports" / "independent-checks.json"
Hc, M, L, DK = 1.0, 1.0, 3.0, 0.25            # Revision/kohn_sham/results/parameters.json physics (H = m = 1)
NCHEB = 96
KCUT = 1.6                           # shells with coordinate momentum |k| <= KCUT (n2 <= 40); see particle_levels
N2MAX = int((KCUT / DK) ** 2)
CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})


def r(v, n=12):
    return None if v is None or not math.isfinite(v) else float(f"{v:.{n}e}")


def fh(a4):
    return math.exp((0.5 * BETA - 1.0) * a4)


def cheb(n):
    """Chebyshev points x_i = cos(pi i/n) and differentiation matrix (Trefethen, Spectral Methods in MATLAB)"""
    xg = np.cos(np.pi * np.arange(n + 1) / n)
    c = np.hstack([2.0, np.ones(n - 1), 2.0]) * (-1.0) ** np.arange(n + 1)
    X = np.tile(xg, (n + 1, 1)).T
    dX = X - X.T
    D = np.outer(c, 1.0 / c) / (dX + np.eye(n + 1))
    D = D - np.diag(D.sum(axis=1))
    return xg, D


def ccw(n):
    """Clenshaw-Curtis weights on [-1, 1] for the points cos(pi i/n)"""
    theta = np.pi * np.arange(n + 1) / n
    w = np.zeros(n + 1)
    v = np.ones(n - 1)
    if n % 2 == 0:
        w[0] = w[n] = 1.0 / (n ** 2 - 1)
        for k in range(1, n // 2):
            v -= 2 * np.cos(2 * k * theta[1:-1]) / (4 * k * k - 1)
        v -= np.cos(n * theta[1:-1]) / (n ** 2 - 1)
    else:
        w[0] = w[n] = 1.0 / n ** 2
        for k in range(1, (n - 1) // 2 + 1):
            v -= 2 * np.cos(2 * k * theta[1:-1]) / (4 * k * k - 1)
    w[1:-1] = 2 * v / n
    return w


class Block:
    """h_{+1} on y in [-L, 0] by collocation; index 0 = fold (y = 0), index n = tip (y = -L)"""

    def __init__(self, n=NCHEB):
        self.n = n
        xg, D = cheb(n)
        self.y = (xg - 1.0) * L / 2.0
        self.D = D * 2.0 / L
        self.w = ccw(n) * L / 2.0
        th = np.pi * np.arange(n + 1) / n
        T = np.cos(np.outer(th, np.arange(n + 1)))
        self.Tinv = np.linalg.inv(T)

    def resolved(self, f):
        """an eigenfunction is accepted only if its last 6 Chebyshev coefficients are below 1e-7 of the largest;
        this removes the spurious (unresolved, polynomial) collocation modes"""
        c = np.abs(self.Tinv @ f)
        return float(np.max(c[-6:])) <= 1e-7 * float(np.max(c))

    def spectrum(self, a4, k, parity):
        """eigenvalues and Hellmann-Feynman derivatives d eps/d a4 of h_{+1} for the coordinate momentum k at slice a4"""
        n, D = self.n, self.D
        f = fh(a4)
        K = math.exp(-a4) * k                        # kappa k, constant in y
        I = np.eye(n + 1)
        A = np.zeros((2 * (n + 1), 2 * (n + 1)))
        A[:n + 1, :n + 1] = K * I
        A[:n + 1, n + 1:] = D / f + M * I
        A[n + 1:, :n + 1] = M * I - D / f
        A[n + 1:, n + 1:] = -K * I
        drop = [n + 1 + n]                          # b(tip) = 0
        drop += [n + 1] if parity == "even" else [0]   # b(0) = 0 (even, theta = 0) or a(0) = 0 (odd, theta = pi)
        keep = [i for i in range(2 * (n + 1)) if i not in drop]
        Ar = A[np.ix_(keep, keep)]
        vals, vecs = np.linalg.eig(Ar)
        real = sorted((i for i in range(len(vals)) if abs(vals[i].imag) <= 1e-8 * max(1.0, abs(vals[i].real))),
                      key=lambda i: vals[i].real)
        clusters = []
        for i in real:
            if clusters and abs(vals[i].real - vals[clusters[-1][-1]].real) <= 1e-9 * max(1.0, abs(vals[i].real)):
                clusters[-1].append(i)
            else:
                clusters.append([i])
        cand = []
        for cl in clusters:
            V = np.zeros((2 * (n + 1), len(cl)), dtype=complex)
            V[keep, :] = vecs[:, cl]
            if len(cl) == 1:
                cand.append((vals[cl[0]], V[:, 0]))
                continue
            # a degenerate eigenspace: the collocation leaves the fold-band orbital (e^{f m y}, 0) at eps = kappa k with
            # a spurious polynomial partner (b = 0, a constrained only at the interior points), and eig returns
            # mixtures; the right singular vectors of the Chebyshev tails of the basis separate them, and the
            # resolution test below keeps the resolved combinations only
            V = V / np.max(np.abs(V), axis=0)
            tail = np.vstack([(self.Tinv @ V[:n + 1])[-6:], (self.Tinv @ V[n + 1:])[-6:]])
            _, _, wh = np.linalg.svd(tail)
            for row in wh:
                cand.append((complex(np.mean([vals[i] for i in cl])), V @ row.conj()))
        out = []
        for lam_, full in cand:
            a, b = full[:n + 1], full[n + 1:]
            ph = a[np.argmax(np.abs(a))] if np.max(np.abs(a)) > np.max(np.abs(b)) else b[np.argmax(np.abs(b))]
            a, b = (a / ph).real, (b / ph).real
            # a component that vanishes (the fold-band orbital (e^{f m y}, 0) has b = 0 identically) is round-off:
            # its Chebyshev tail does not decay, so it is tested only when it is not negligible against the other
            amax = max(float(np.max(np.abs(a))), float(np.max(np.abs(b))))
            if not all(float(np.max(np.abs(c_))) <= 1e-12 * amax or self.resolved(c_) for c_ in (a, b)):
                continue
            norm = float(np.sum(self.w * (a * a + b * b)))
            # <chi| dh/da4 |chi>: dK/da4 = -K; d(1/f)/da4 = CK/f
            dlev = (float(np.sum(self.w * (-K * a * a + K * b * b)))
                    + CK / f * float(np.sum(self.w * (a * (D @ b) - b * (D @ a))))) / norm
            out.append((float(lam_.real), dlev))
        out.sort()
        return out


def r3(n2):
    m = int(math.isqrt(n2)) + 1
    return sum(1 for i in range(-m, m + 1) for j in range(-m, m + 1) for k in range(-m, m + 1) if i * i + j * j + k * k == n2)


R3 = {n2: r3(n2) for n2 in range(N2MAX + 1)}
SHELLS = [n2 for n2 in range(N2MAX + 1) if R3[n2] > 0]


def particle_levels(blk, a4):
    """(eps, d eps/d a4, degeneracy, label) of the positive branch of both block types and the k = 0 zero modes, for
    every shell with |k| <= KCUT.  Every level of a shell lies at or above kappa |k| (the fold band is the lowest), and
    kappa = e^{-a4} scales every fold-band level alike, so a level of an excluded shell lies above e^{-a4} KCUT at every
    slice: the aufbau below that value is exact (checked: the HOMO and the next level lie below it)"""
    levels = []
    for n2 in SHELLS:
        k = DK * math.sqrt(n2)
        for parity in ("even", "odd"):
            spec = blk.spectrum(a4, k, parity)
            spec = [s for s in spec if abs(s[0]) < 30.0]          # far below the resolution limit of NCHEB
            g = 4 * R3[n2] if n2 > 0 else 4
            if n2 == 0 and parity == "even":
                # the fold zero mode (e^{f m y}, 0) at eps = 0 of both block types, inserted exactly; the numerical
                # eigenvalue |eps| < 1e-8 of this sector (the same zero mode, the resolved member of its pair) dropped
                levels.append((0.0, 0.0, g, (n2, +1, parity, "zero")))
                levels.append((0.0, 0.0, g, (n2, -1, parity, "zero")))
                spec = [s for s in spec if abs(s[0]) >= 1e-8]
            for e, de in spec:
                if e > 0:
                    levels.append((e, de, g, (n2, +1, parity)))
                elif e < 0:                                       # h_{-1} = -h_{+1}
                    levels.append((-e, -de, g, (n2, -1, parity)))
    levels.sort(key=lambda t: (t[0], str(t[3])))
    return levels


def fill(levels, N):
    E = dE = 0.0
    n = 0
    last = None
    nxt = None
    for e, de, g, lab in levels:
        if n >= N:
            nxt = e
            break
        E += g * e
        dE += g * de
        n += g
        last = e
    return E, dE, n, last, nxt


def main():
    blk = Block()
    dense = list(csv.DictReader(open(DENSE, encoding="utf-8")))
    ns = sorted({int(row["N"]) for row in dense if row["lambda_tag"] == "lam0" and int(row["N"]) != 8})
    slices = sorted({round(float(row["a4"]), 10) for row in dense})
    # 1. exact k = 0 spectra (ks-theory.json: even {0, +-sqrt(m^2 + (n pi/(f L))^2)}, odd +-sqrt(m^2 + p^2), tan(p f L) = -p/m)
    dev_k0 = 0.0
    for a4 in (0.0, 1.0, 2.0):
        fl = fh(a4) * L
        ev = [s[0] for s in blk.spectrum(a4, 0.0, "even")]       # the zero mode is the resolved member of its pair
        od = [s[0] for s in blk.spectrum(a4, 0.0, "odd")]
        ex_even = sorted([0.0] + [math.sqrt(M * M + (nn * math.pi / fl) ** 2) * sg for nn in range(1, 4) for sg in (1, -1)])
        num_even = sorted(sorted(ev, key=abs)[:7])
        roots = []
        for nn in range(4):                                   # tan(p fL) = -p/M: one root in ((2nn+1) pi/(2fL), (nn+1) pi/fL)
            lo, hi = (2 * nn + 1) * math.pi / (2 * fl) + 1e-12, (nn + 1) * math.pi / fl - 1e-12
            fn = lambda p: math.sin(p * fl) * M + p * math.cos(p * fl)  # noqa: E731
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if fn(lo) * fn(mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            roots.append(0.5 * (lo + hi))
        ex_odd = sorted([math.sqrt(M * M + p * p) * sg for p in roots[:3] for sg in (1, -1)])
        num_odd = sorted(sorted(od, key=abs)[:6])
        dev_k0 = max(dev_k0, max(abs(a - b) for a, b in zip(num_even, ex_even)),
                     max(abs(a - b) for a, b in zip(num_odd, ex_odd)))
        if a4 == 0.0:
            bulk_edge0 = math.sqrt(M * M + roots[0] ** 2)
    check("exact_k0_spectra", dev_k0 < 1e-10,
          f"Chebyshev collocation (n = {NCHEB}) vs the exact k = 0 spectra at a4 = 0, 1, 2 (proper length f L, f = e^(-a4/3)): "
          f"even {{0, +-sqrt(m^2 + (n pi/(f L))^2)}}, odd +-sqrt(m^2 + p^2), tan(p f L) = -p/m: max deviation {dev_k0:.3e}; "
          f"bulk edge (lowest odd) at a4 = 0: {bulk_edge0:.12f}")
    # 2. the fold band: eps = kappa |k| exactly, d eps/d a4 = -eps (ks-theory.json: slope c = e^{-a4,0})
    dev_fb, dev_dfb = 0.0, 0.0
    for a4 in (0.0, 1.0, 2.0):
        for n2 in (1, 4, 9):
            k = DK * math.sqrt(n2)
            sp_ = blk.spectrum(a4, k, "even")
            K = math.exp(-a4) * k
            e0, de0 = min((s for s in sp_ if s[0] > 0), key=lambda s: abs(s[0] - K))
            dev_fb = max(dev_fb, abs(e0 - K))
            dev_dfb = max(dev_dfb, abs(de0 + K))
    check("fold_band_dispersion", dev_fb < 1e-11 and dev_dfb < 1e-9,
          f"even sector of h_(+1) at a4 = 0, 1, 2 and |k| = 0.25, 0.5, 0.75: the level eps = e^(-a4) |k| (the fold-band "
          f"orbital (e^(f m y), 0)) to {dev_fb:.2e}, and its Hellmann-Feynman derivative (with the kinetic term) d eps/d a4 = "
          f"-eps to {dev_dfb:.2e}")
    # 3. convergence in the collocation order at one slice
    blk2 = Block(NCHEB + 32)
    nl = max(ns)
    lv1, lv2 = particle_levels(blk, 0.0), particle_levels(blk2, 0.0)
    E1, d1 = fill(lv1, nl)[:2]
    E2, d2 = fill(lv2, nl)[:2]
    check("collocation_converged", abs(E1 - E2) / E2 < 1e-11 and abs(d1 - d2) / abs(d2) < 1e-10,
          f"N = {nl}, a4 = 0: n = {NCHEB} vs {NCHEB + 32}: |dE|/E = {abs(E1 - E2) / E2:.2e}, "
          f"|d(dE/da4)|/|dE/da4| = {abs(d1 - d2) / abs(d2):.2e}")

    # 4. the history: E, dE/da4 (Hellmann-Feynman), w_eff(A) at every dense slice, compared with the primary chain
    rust = {}
    for row in dense:
        if row["lambda_tag"] == "lam0":
            rust[(int(row["N"]), round(float(row["a4"]), 6))] = row
    hist = {N: [] for N in ns}
    worstE = worstW = 0.0
    closed = True
    for a4 in slices:
        lv = particle_levels(blk, a4)
        for N in ns:
            E, dE, n, last, nxt = fill(lv, N)
            closed &= (n == N and nxt is not None and nxt - last > 1e-9 and nxt < math.exp(-a4) * KCUT)
            row = rust[(N, round(a4, 6))]
            Er = float(row["int_rho"])
            wr = (float(row["int_p3"]) - (float(row["int_p0"]) + 3 * float(row["int_p_t"])) / 9.0) / Er
            wA = -dE / (3 * E)
            worstE = max(worstE, abs(E - Er) / Er)
            worstW = max(worstW, abs(wA - wr))
            hist[N].append((a4, E, dE, wA))
    check("aufbau_closed_shells", closed,
          f"N = {', '.join(map(str, ns))} fill closed degenerate groups with a gap above at every slice, and the next level "
          f"lies below e^(-a4) |k|_cut ({KCUT} = the shells n2 <= {N2MAX}), so no excluded shell can hold a lower level")
    check("energy_vs_rust_solver", worstE < 1e-8,
          f"E(a4) of the independent collocation vs the Rust solver (E = 2 Vol_7 int e^(3Hy) rho), {len(ns) * len(slices)} "
          f"states: max relative deviation {worstE:.3e}")
    check("w_eff_vs_primary", worstW < 1e-8,
          f"w_eff(A) = -(1/3) d ln E/d a4 with dE/da4 from Hellmann-Feynman level derivatives vs w_eff(A) = P3/E - (P0 + 3 Pt)/(9E) "
          f"from the solver's energy-momentum integrals, {len(ns) * len(slices)} states: max |difference| {worstW:.3e}")
    wmax = max(abs(q[3] - 1.0 / 3.0) for N in ns for q in hist[N])
    check("free_gas_w_eff_one_third", wmax < 1e-10,
          f"independently: w_eff(A) = 1/3 at every slice for N = {', '.join(map(str, ns))} (max |w_eff(A) - 1/3| = {wmax:.2e}): "
          f"every occupied level is a fold-band level with d eps/d a4 = -eps")

    # 5. CPL tangent wa = -d w_eff/d a4 by central differences of the Hellmann-Feynman w (step 1e-3)
    prim = json.loads(SUMMARY.read_text(encoding="utf-8"))
    pt = {s["series"]: s for s in prim["series"]}
    tang = []
    worstT = 0.0
    dlt = 1e-3
    for N in ns:
        for t in (0.5, 1.0, 1.5, 2.0):
            vals = {}
            for sgn in (-1, 0, 1):
                E, dE = fill(particle_levels(blk, t + sgn * dlt), N)[:2]
                vals[sgn] = -dE / (3 * E)
            dw = (vals[1] - vals[-1]) / (2 * dlt)
            p = next(q for q in pt[f"N{N}_lam0"]["cplTangent"] if q["a4_today"] == t)
            worstT = max(worstT, abs(-dw - p["w_eff_A_B"]["wa"]), abs(vals[0] - p["w_eff_A_B"]["w0"]))
            tang.append({"N": N, "a4_today": t, "w0_A_B": r(vals[0]), "w0_C": r(vals[0] - (4 - 2 * BETA) / 3), "wa": r(-dw),
                         "primary_w0_A_B": p["w_eff_A_B"]["w0"], "primary_wa": p["w_eff_A_B"]["wa"]})
    check("cpl_tangent_vs_primary", worstT < 5e-5,
          f"w0 and wa (a4_today = 0.5, 1, 1.5, 2; N = {', '.join(map(str, ns))}; lambda = 0) independent vs primary (4th-order "
          f"differences of the solver's dense grid): max |difference| {worstT:.3e}")

    # 6. bulk band versus the occupied fold band: one n2 = 1 shell along a4 in [-3, 4]
    grid = [round(-3.0 + 0.25 * i, 10) for i in range(29)]
    bulk, fold = [], []
    for a4 in grid:
        k = DK
        od_ = [s for s in blk.spectrum(a4, k, "odd") if s[0] > 0]
        ev_ = [s for s in blk.spectrum(a4, k, "even") if s[0] > 0]
        eb, deb = min(od_, key=lambda s: s[0])
        ebr, debr = min(ev_, key=lambda s: s[0])
        bulk.append({"a4": a4, "f": r(fh(a4)), "kappa_k": r(math.exp(-a4) * k), "eps": r(eb), "w_eff_A_B": r(-deb / eb / 3)})
        fold.append({"a4": a4, "kappa_k": r(math.exp(-a4) * k), "eps": r(ebr), "w_eff_A_B": r(-debr / ebr / 3)})
    wb = [q["w_eff_A_B"] for q in bulk]
    wr = [q["w_eff_A_B"] for q in fold]
    mono = all(x > y for x, y in zip(wb, wb[1:]))
    sign_change = next((q["a4"] for q, q2 in zip(bulk, bulk[1:]) if q["w_eff_A_B"] > 0 >= q2["w_eff_A_B"]), None)
    check("bulk_band_w_eff", all(math.isfinite(x) for x in wb) and mono and sign_change is not None,
          f"lowest odd-parity (bulk) level of the n2 = 1 shell along a4 in [-3, 4] (f = e^(-a4/3) from {fh(-3):.4f} to "
          f"{fh(4):.4f}): w_eff(A) = -(1/3) d ln eps/d a4 runs from {wb[0]:.6f} (a4 = -3) to {wb[-1]:.6f} (a4 = 4), "
          f"monotonically decreasing: {mono}; " +
          (f"it changes sign between a4 = {sign_change:g} and {sign_change + 0.25:g} (the shrinking hidden direction raises "
           f"the bulk level like 1/f = e^(a4/3), so w_eff(A) -> -1/9 when the hidden momentum dominates)"
           if sign_change is not None else "it does not change sign") +
          ": the bulk-band quanta do NOT follow the dust-like 1/3 -> 0 law of a massive flat-space quantum")
    check("fold_band_radiation_law", max(abs(x - 1.0 / 3.0) for x in wr) < 1e-9,
          f"lowest even-parity (fold-band) level of the same shell: w_eff(A) = 1/3 at every a4 (max deviation "
          f"{max(abs(x - 1.0 / 3.0) for x in wr):.2e}): radiation, exactly")

    fails = [c for c in CHECKS if c["verdict"] != "PASS"]
    out = {"producer": "Revision/dark_sector/dirac16complex/independent/independent_free_gas.py",
           "method": f"Chebyshev collocation n = {NCHEB} on y in [-L, 0] with d_y/f, Hellmann-Feynman level derivatives with "
                     f"the kinetic term (1 - beta/2) d_y/f, Clenshaw-Curtis quadrature; H = m = 1, L = 3, dk = 0.25, lambda = 0, "
                     f"shells |k| <= {KCUT}",
           "history": [{"N": N, "a4": r(a4), "E": r(E), "dE_da4": r(dE), "w_eff_A_B": r(wA),
                        "w_eff_C": r(wA - (4 - 2 * BETA) / 3)}
                       for N in ns for (a4, E, dE, wA) in hist[N]],
           "cplTangent": tang, "bulkBand_n2_1": bulk, "foldBand_n2_1": fold,
           "label": "free (lambda = 0) gas on the PRESCRIBED history a4 = H x4, b4 = e^((4/3) H x4) (beta = 4/3, f = e^(-a4/3)); "
                    "instantaneous states; both fold conditions filled (ASSUMED); the filling rule is the stated CONVENTION "
                    "of ks-theory.json"}
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh_:
        fh_.write(json.dumps(out, indent=1) + "\n")
    rep = {"producer": out["producer"], "checks": CHECKS,
           "summary": {"total": len(CHECKS), "pass": len(CHECKS) - len(fails), "fail": len(fails)}}
    with open(REP, "w", encoding="utf-8", newline="\n") as fh_:
        fh_.write(json.dumps(rep, indent=1) + "\n")
    for c in CHECKS:
        print(f"{c['verdict']} - {c['name']}: {c['detail']}")
    print(f"{len(CHECKS) - len(fails)}/{len(CHECKS)} checks pass")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
