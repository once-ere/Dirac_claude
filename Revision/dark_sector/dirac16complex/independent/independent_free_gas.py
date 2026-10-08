#!/usr/bin/env python3
"""Revision/dark_sector/dirac16complex/independent/independent_free_gas.py - INDEPENDENT second implementation of
the key numbers of the dark-sector analysis of dirac16complex for the free (lambda = 0) Kohn-Sham gas.

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the three exponentially
DEFLATING extra times (scale factor e^{-a4} sin^{1/6} z, a4 increasing); x8 = hidden direction, y = ln(sin z)/(6H).

Independent of the Rust solver (different method, different code, no solver output read except for the final
comparison): the 2 x 2 block Hamiltonian of Revision/kohn_sham/ks-theory.json (blockEquation; lambda = 0, so
M_eff = m, v_v = 0), h_j = j[-i sigma1 d_y + m sigma2 + kappa k sigma3], kappa = e^{-Hy - a4}, chi = (a, i b),
is discretised by CHEBYSHEV COLLOCATION on y in [-L, 0] (the Rust solver shoots with RK4 and a Pruefer count):
    eps a = j (b' + kappa k a + m b),  eps b = j (m a - kappa k b - a'),
with b(-L) = 0 (regular tip, theta = 0), b(0) = 0 (even brane parity) or a(0) = 0 (odd parity; the Z2 brane is
ASSUMED).  h_{-1} = -h_{+1}.  Filling (the CONVENTION of ks-theory.json): the positive levels of both block types
plus the k = 0 brane zero modes, degeneracy 4 r3(n2) (4 at k = 0) per level and block type, aufbau to N.
The derivative of each level along the history is the Hellmann-Feynman expectation
d eps/d a4 = <chi| -j kappa k sigma3 |chi> (Clenshaw-Curtis quadrature), so that X = P3 - Pt = -(1/3) dE/da4 is
obtained WITHOUT differencing E and without the solver's energy-momentum integrals.

Key numbers recomputed and compared with the primary chain (outputs/ks-history-dense.csv, outputs/eos-summary.json):
E(a4) and w_eff(A) = X/E for N = 136 and 688 at the 41 slices; d w_eff/d a4 (CPL wa) at a4_today = 0.5, 1, 1.5, 2
by central differences of the Hellmann-Feynman X; the exact k = 0 spectra; and (new here) the BULK band: the lowest
odd-parity level, whose quanta are massive, with w_eff(A) = -(1/3) d ln eps/d a4 along a4 in [-3, 4] (the
dark-matter-like 1/3 -> 0 law) versus the occupied brane band (-> 1/3).

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
OUT = OWN / "outputs" / "independent-free-gas.json"
REP = OWN / "reports" / "independent-checks.json"
Hc, M, L, DK = 1.0, 1.0, 3.0, 0.25            # Revision/kohn_sham/results/parameters.json physics (H = m = 1)
NCHEB = 96
N2MAX = 40
CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})


def r(v, n=12):
    return None if v is None or not math.isfinite(v) else float(f"{v:.{n}e}")


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
    """h_{+1} on y in [-L, 0] by collocation; index 0 = brane (y = 0), index n = tip (y = -L)"""

    def __init__(self, n=NCHEB):
        self.n = n
        xg, D = cheb(n)
        self.y = (xg - 1.0) * L / 2.0
        self.D = D * 2.0 / L
        self.w = ccw(n) * L / 2.0
        # values at the points cos(pi i/n) -> Chebyshev coefficients (for the resolution test of eigenvectors)
        th = np.pi * np.arange(n + 1) / n
        T = np.cos(np.outer(th, np.arange(n + 1)))
        self.Tinv = np.linalg.inv(T)

    def resolved(self, f):
        """an eigenfunction is accepted only if its last 6 Chebyshev coefficients are below 1e-7 of the largest;
        this removes the spurious (unresolved, polynomial) collocation modes"""
        c = np.abs(self.Tinv @ f)
        return float(np.max(c[-6:])) <= 1e-7 * float(np.max(c))

    def spectrum(self, kp, parity):
        """eigenvalues and Hellmann-Feynman derivatives d eps/d a4 of h_{+1} for physical momentum kp = k e^{-a4}"""
        n, D = self.n, self.D
        kap = np.exp(-Hc * self.y) * kp            # kappa k = e^{-Hy} k e^{-a4}
        I = np.eye(n + 1)
        A = np.zeros((2 * (n + 1), 2 * (n + 1)))
        A[:n + 1, :n + 1] = np.diag(kap)
        A[:n + 1, n + 1:] = D + M * I
        A[n + 1:, :n + 1] = M * I - D
        A[n + 1:, n + 1:] = -np.diag(kap)
        drop = [n + 1 + n]                          # b(tip) = 0
        drop += [n + 1] if parity == "even" else [0]   # b(0) = 0 (even) or a(0) = 0 (odd)
        keep = [i for i in range(2 * (n + 1)) if i not in drop]
        Ar = A[np.ix_(keep, keep)]
        vals, vecs = np.linalg.eig(Ar)
        out = []
        for lam_, vec in zip(vals, vecs.T):
            if abs(lam_.imag) > 1e-8 * max(1.0, abs(lam_.real)):
                continue
            full = np.zeros(2 * (n + 1), dtype=complex)
            full[keep] = vec
            a, b = full[:n + 1], full[n + 1:]
            ph = a[np.argmax(np.abs(a))] if np.max(np.abs(a)) > np.max(np.abs(b)) else b[np.argmax(np.abs(b))]
            a, b = (a / ph).real, (b / ph).real
            if not (self.resolved(a) and self.resolved(b)):
                continue
            norm = float(np.sum(self.w * (a * a + b * b)))
            dlev = -float(np.sum(self.w * np.exp(-Hc * self.y) * kp * (a * a - b * b))) / norm   # <-kappa k sigma3>
            out.append((float(lam_.real), dlev))
        out.sort()
        return out


def r3(n2):
    m = int(math.isqrt(n2)) + 1
    return sum(1 for i in range(-m, m + 1) for j in range(-m, m + 1) for k in range(-m, m + 1) if i * i + j * j + k * k == n2)


R3 = {n2: r3(n2) for n2 in range(N2MAX + 1)}
SHELLS = [n2 for n2 in range(N2MAX + 1) if R3[n2] > 0]


def particle_levels(blk, a4):
    """(eps, d eps/d a4, degeneracy, label) of the positive branch of both block types and the k = 0 zero modes"""
    levels = []
    for n2 in SHELLS:
        kp = DK * math.sqrt(n2) * math.exp(-a4)
        for parity in ("even", "odd"):
            spec = blk.spectrum(kp, parity)
            spec = [s for s in spec if abs(s[0]) < 30.0]          # far below the resolution limit of NCHEB
            g = 4 * R3[n2] if n2 > 0 else 4
            if n2 == 0 and parity == "even":
                # the brane zero mode (e^{my}, 0) at eps = 0 of both block types, inserted exactly; numerical
                # eigenvalues |eps| < 1e-8 of this sector (the zero mode and its degenerate spurious partner) dropped
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
    E = X = 0.0
    n = 0
    last = None
    for e, de, g, lab in levels:
        if n >= N:
            nxt = e
            break
        E += g * e
        X += -g * de / 3.0
        n += g
        last = e
    else:
        nxt = None
    return E, X, n, last, nxt


def main():
    blk = Block()
    # 1. exact k = 0 spectra (ks-theory.json boundaryConditions.exactK0Spectra)
    ev = [s[0] for s in blk.spectrum(0.0, "even")] + [0.0]          # zero mode: unresolved pair, inserted
    od = [s[0] for s in blk.spectrum(0.0, "odd")]
    ex_even = sorted([0.0] + [math.sqrt(M * M + (nn * math.pi / L) ** 2) * sg for nn in range(1, 4) for sg in (1, -1)])
    num_even = sorted(sorted(ev, key=abs)[:7])
    roots = []
    for nn in range(4):                                   # tan(pL) = -p/M: one root in ((2nn+1) pi/(2L), (nn+1) pi/L)
        lo, hi = (2 * nn + 1) * math.pi / (2 * L) + 1e-12, (nn + 1) * math.pi / L - 1e-12
        f = lambda p: math.sin(p * L) * M + p * math.cos(p * L)
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if f(lo) * f(mid) <= 0:
                hi = mid
            else:
                lo = mid
        roots.append(0.5 * (lo + hi))
    ex_odd = sorted([math.sqrt(M * M + p * p) * sg for p in roots[:3] for sg in (1, -1)])
    num_odd = sorted(sorted(od, key=abs)[:6])
    dev_k0 = max(max(abs(a - b) for a, b in zip(num_even, ex_even)), max(abs(a - b) for a, b in zip(num_odd, ex_odd)))
    check("exact_k0_spectra", dev_k0 < 1e-10,
          f"Chebyshev collocation (n = {NCHEB}) vs the exact k = 0 spectra: even {{0, +-sqrt(m^2 + (n pi/L)^2)}}, "
          f"odd +-sqrt(m^2 + p^2), tan(pL) = -p/m: max deviation {dev_k0:.3e}; bulk edge (lowest odd) "
          f"{math.sqrt(M * M + roots[0] ** 2):.12f}")
    # 2. brane-band slope at small k (ks-theory.json checksNumeric: c = 1.9051482536448664 at a4 = 0)
    kp = 1e-4
    sp_ = blk.spectrum(kp, "even")
    e0 = min((s for s in sp_ if s[0] > 0), key=lambda s: s[0])[0]
    c_num = e0 / kp
    c_th = (2 * M / (2 * M - Hc)) * (1 - math.exp(-(2 * M - Hc) * L)) / (1 - math.exp(-2 * M * L))
    check("brane_band_slope", abs(c_num - c_th) < 1e-6,
          f"eps_0(k)/k at k = 1e-4: {c_num:.10f}; formula (2M/(2M-H))(1 - e^-(2M-H)L)/(1 - e^-2ML) = {c_th:.10f}")
    # 3. convergence in the collocation order at one slice
    blk2 = Block(NCHEB + 32)
    lv1, lv2 = particle_levels(blk, 0.0), particle_levels(blk2, 0.0)
    E1, X1 = fill(lv1, 688)[:2]
    E2, X2 = fill(lv2, 688)[:2]
    check("collocation_converged", abs(E1 - E2) / E2 < 1e-11 and abs(X1 - X2) / X2 < 1e-10,
          f"N = 688, a4 = 0: n = {NCHEB} vs {NCHEB + 32}: |dE|/E = {abs(E1 - E2) / E2:.2e}, |dX|/X = {abs(X1 - X2) / X2:.2e}")

    # 4. the history: E, X (Hellmann-Feynman), w_eff(A) at the 41 slices, compared with the primary chain
    rust = {}
    for row in csv.DictReader(open(DENSE, encoding="utf-8")):
        if row["lambda_tag"] == "lam0":
            rust[(int(row["N"]), round(float(row["a4"]), 6))] = row
    slices = [round(0.05 * i, 10) for i in range(41)]
    hist = {136: [], 688: []}
    worstE = worstW = 0.0
    closed = True
    for a4 in slices:
        lv = particle_levels(blk, a4)
        for N in (136, 688):
            E, X, n, last, nxt = fill(lv, N)
            closed &= (n == N and nxt is not None and nxt - last > 1e-9)
            row = rust[(N, round(a4, 6))]
            Er = float(row["int_rho"])
            Xr = float(row["int_p3"]) - float(row["int_p_t"])
            worstE = max(worstE, abs(E - Er) / Er)
            worstW = max(worstW, abs(X / E - Xr / Er))
            hist[N].append((a4, E, X))
    check("aufbau_closed_shells", closed, "N = 136 and 688 fill closed degenerate groups with a gap above at every slice")
    check("energy_vs_rust_solver", worstE < 1e-8,
          f"E(a4) of the independent collocation vs the Rust solver (E = 2 Vol_7 int e^(6Hy) rho), 82 states: "
          f"max relative deviation {worstE:.3e}")
    check("w_eff_vs_primary", worstW < 1e-8,
          f"w_eff(A) = X/E with X from Hellmann-Feynman level derivatives vs X = P3 - Pt from the solver's "
          f"energy-momentum integrals, 82 states: max |difference| {worstW:.3e}")

    # 5. CPL tangent wa = -d w_eff/d a4 by central differences of the Hellmann-Feynman X (step 1e-3)
    prim = json.loads(SUMMARY.read_text(encoding="utf-8"))
    pt = {s["series"]: s for s in prim["series"]}
    tang = []
    worstT = 0.0
    dlt = 1e-3
    for N in (136, 688):
        for t in (0.5, 1.0, 1.5, 2.0):
            vals = {}
            for sgn in (-1, 0, 1):
                E, X = fill(particle_levels(blk, t + sgn * dlt), N)[:2]
                vals[sgn] = (E, X)
            E0, X0 = vals[0]
            dX = (vals[1][1] - vals[-1][1]) / (2 * dlt)
            dw = dX / E0 + 3 * (X0 / E0) ** 2
            p = next(q for q in pt[f"N{N}_lam0"]["cplTangent"] if q["a4_today"] == t)
            worstT = max(worstT, abs(-dw - p["w_eff_A_B"]["wa"]), abs(X0 / E0 - p["w_eff_A_B"]["w0"]))
            tang.append({"N": N, "a4_today": t, "w0_A_B": r(X0 / E0), "w0_C": r(X0 / E0 - 1), "wa": r(-dw),
                         "primary_w0_A_B": p["w_eff_A_B"]["w0"], "primary_wa": p["w_eff_A_B"]["wa"]})
    check("cpl_tangent_vs_primary", worstT < 5e-5,
          f"w0 and wa (a4_today = 0.5, 1, 1.5, 2; N = 136, 688; lambda = 0) independent vs primary (4th-order "
          f"differences of the solver's dense grid): max |difference| {worstT:.3e}")

    # 6. bulk (massive) band versus the occupied brane band: one n2 = 1 shell along a4 in [-3, 4]
    grid = [round(-3.0 + 0.25 * i, 10) for i in range(29)]
    bulk, brane = [], []
    for a4 in grid:
        kp = DK * math.exp(-a4)
        od_ = [s for s in blk.spectrum(kp, "odd") if s[0] > 0]
        ev_ = [s for s in blk.spectrum(kp, "even") if s[0] > 0]
        eb, deb = min(od_, key=lambda s: s[0])
        ebr, debr = min(ev_, key=lambda s: s[0])
        bulk.append({"a4": a4, "k_phys": r(kp), "eps": r(eb), "w_eff_A_B": r(-deb / eb / 3)})
        brane.append({"a4": a4, "k_phys": r(kp), "eps": r(ebr), "w_eff_A_B": r(-debr / ebr / 3)})
    wb = [q["w_eff_A_B"] for q in bulk]
    wr = [q["w_eff_A_B"] for q in brane]
    check("bulk_band_dark_matter_law", wb[0] > 0.2 and wb[-1] < 0.01 and all(x > y for x, y in zip(wb, wb[1:])),
          f"lowest odd-parity (massive, eps(0) = {math.sqrt(M * M + roots[0] ** 2):.6f}) level of the n2 = 1 shell: "
          f"w_eff(A) = -(1/3) d ln eps/d a4 falls monotonically from {wb[0]:.6f} (a4 = -3) to {wb[-1]:.3e} (a4 = 4); "
          f"w(4)/w(3.75) = {wb[-1] / wb[-2]:.6f} (e^-0.25 = {math.exp(-0.25):.6f}: w ~ k_phys ~ 1/a, a linear term "
          f"of eps(k) at small k; e^-0.5 would be the flat-space k^2 law): the dark-matter-like fall toward 0 "
          f"appears for quanta in the BULK band")
    check("brane_band_radiation_law", abs(wr[-1] - 1.0 / 3.0) < 1e-3 and min(wr) > 0.25,
          f"lowest even-parity (brane-band, massless at k = 0) level of the same shell: w_eff(A) in "
          f"[{min(wr):.6f}, {max(wr):.6f}], {wr[-1]:.6f} at a4 = 4 (-> 1/3: radiation, no 1/3 -> 0)")

    fails = [c for c in CHECKS if c["verdict"] != "PASS"]
    out = {"producer": "Revision/dark_sector/dirac16complex/independent/independent_free_gas.py",
           "method": f"Chebyshev collocation n = {NCHEB} on y in [-L, 0], Hellmann-Feynman level derivatives, "
                     f"Clenshaw-Curtis quadrature; H = m = 1, L = 3, dk = 0.25, lambda = 0, shells n2 <= {N2MAX}",
           "history": [{"N": N, "a4": r(a4), "E": r(E), "X": r(X), "w_eff_A_B": r(X / E), "w_eff_C": r(X / E - 1)}
                       for N in (136, 688) for (a4, E, X) in hist[N]],
           "cplTangent": tang, "bulkBand_n2_1": bulk, "braneBand_n2_1": brane,
           "label": "free (lambda = 0) gas on the PRESCRIBED history a4 = A H x4; instantaneous states; the Z2 brane "
                    "is ASSUMED; the filling rule is the stated CONVENTION of ks-theory.json"}
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(out, indent=1) + "\n")
    rep = {"producer": out["producer"], "checks": CHECKS,
           "summary": {"total": len(CHECKS), "pass": len(CHECKS) - len(fails), "fail": len(fails)}}
    with open(REP, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(rep, indent=1) + "\n")
    for c in CHECKS:
        print(f"{c['verdict']} - {c['name']}: {c['detail']}")
    print(f"{len(CHECKS) - len(fails)}/{len(CHECKS)} checks pass")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
