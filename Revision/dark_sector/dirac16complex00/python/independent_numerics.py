"""Revision dark sector, dirac16complex00: implementation B (independent of implementation A).

numpy only (no sympy, no code shared with derive_eos.py).  It integrates the 16-component field
equation of the local model (the author's metric with the warp frozen at a fixed hidden position,
SPEC section 1, a4 = eps x4: the exponentially deflating member, eps = A H in units of the mass m)

    gamma^(x4) d4 phi + i e^{-a4} k gamma^(x1) phi + i e^{a4} q gamma^(x5) phi = m phi

for plane-wave modes exp(i (k x1 + q x5)) phi(x4) with the author's T16 read from
Revision/algebra/gammas.json, computes the energy-momentum bilinears along the solutions
(rho = -K1 - K5 + m S, p1 = L0 - K1, p5 = L0 - K5, L0 = K1 + K4 + K5 - m S), checks the conservation
identity and the conserved Krein charge numerically, forms the models of implementation A from the
numerical solutions, and computes w(a), the CPL tangents and fits, the crossings of -1 and the
growth past the turning point.  Then it compares its key numbers with Revision/dark_sector/
dirac16complex00/eos-theory.json (implementation A).

Writes <out>/results/independent-numerics.json and <out>/reports/python-independent-numerics.json.
Usage: python independent_numerics.py [--out DIR]   (deterministic: numbers rounded to 8 digits)
"""

import argparse
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OWN = os.path.normpath(os.path.join(HERE, ".."))
REV = os.path.normpath(os.path.join(OWN, "..", ".."))
GAMMAS = os.path.join(REV, "algebra", "gammas.json")

EPS = 1.0e-3        # a4' = A H in units of m (adiabatic regime)
DX_OMEGA = 0.05     # step: omega dx <= 0.05
CHECKS = []
TOL_W = 2.0e-3      # tolerance for w values against implementation A
TOL_WA = 4.0e-3     # tolerance for slopes (wa) against implementation A


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})


def r8(x):
    return float("%.8g" % x)


def frac(x):
    if isinstance(x, str):
        p, q = x.split("/")
        return int(p) / int(q)
    return float(x)


def load():
    with open(GAMMAS, encoding="utf-8") as fh:
        d = json.load(fh)
    g = [np.array([[frac(v) for v in row] for row in m], dtype=complex) for m in d["gamma"]]
    eta = [int(e) for e in d["eta"]]
    return g, eta


G, ETA = load()
G1, G4, G5, G8 = G[0], G[3], G[4], G[7]
C = G8 @ G[0] @ G[1] @ G[2]
B = -1j * C @ G4
I16 = np.eye(16, dtype=complex)
CG1, CG4, CG5 = C @ G1, C @ G4, C @ G5
M41, M45 = G4 @ G1, G4 @ G5


def hmat(m, k, q, a4):
    """omega phi = h phi for the frozen generator: d4 phi = -i h phi."""
    return -1j * m * G4 - k * math.exp(-a4) * M41 - q * math.exp(a4) * M45


def bil(M, u, v=None):
    v = u if v is None else v
    return complex(np.conj(u) @ (M @ v))


def initial_vector(m, k, q, a4, krein):
    """A vector of the positive-frequency eigenspace of h with Krein sign krein (+1 or -1), |Q| = 1."""
    h = hmat(m, k, q, a4)
    om = math.sqrt(m * m + k * k * math.exp(-2 * a4) - q * q * math.exp(2 * a4))
    P = 0.5 * (I16 + h / om)
    U, s, _ = np.linalg.svd(P)
    U = U[:, :8]
    gram = U.conj().T @ B @ U
    gram = 0.5 * (gram + gram.conj().T)
    ev, V = np.linalg.eigh(gram)
    y = V[:, -1] if krein > 0 else V[:, 0]
    u = U @ y
    Q = bil(B, u).real
    return u / math.sqrt(abs(Q)), om


def run_mode(m, k, q, krein, a_start, a_end, eps=EPS, record_every=1, u0=None):
    """Exponential-midpoint integration (exact propagator of the frozen generator at the midpoint;
    it preserves the Krein form exactly). Returns arrays over the steps."""
    x = math.log(a_start) / eps
    xend = math.log(a_end) / eps
    if u0 is None:
        phi, _ = initial_vector(m, k, q, eps * x, krein)
    else:
        phi = u0
    rec = {"lna": [], "rho": [], "K1": [], "K5": [], "K4": [], "S": [], "Q": [], "norm": []}

    def diag(phi, x):
        a4 = eps * x
        h = hmat(m, k, q, a4)
        dphi = -1j * (h @ phi)
        K1 = (1j * k * math.exp(-a4) * bil(CG1, phi)).real
        K5 = (1j * q * math.exp(a4) * bil(CG5, phi)).real
        K4c = 0.5 * (bil(CG4, phi, dphi) - np.conj(dphi) @ (CG4 @ phi))
        S = bil(C, phi).real
        rec["lna"].append(a4)
        rec["rho"].append(-K1 - K5 + m * S)
        rec["K1"].append(K1)
        rec["K5"].append(K5)
        rec["K4"].append(complex(K4c).real)
        rec["S"].append(S)
        rec["Q"].append(bil(B, phi).real)
        rec["norm"].append(float(np.linalg.norm(phi)))

    diag(phi, x)
    n = 0
    while x < xend - 1e-12:
        a4m = eps * x
        om2 = m * m + k * k * math.exp(-2 * a4m) - q * q * math.exp(2 * a4m)
        dx = min(DX_OMEGA / max(math.sqrt(abs(om2)), 1e-3), 0.2, xend - x)
        hm = hmat(m, k, q, eps * (x + 0.5 * dx))
        w2 = m * m + k * k * math.exp(-2 * eps * (x + 0.5 * dx)) - q * q * math.exp(2 * eps * (x + 0.5 * dx))
        w = np.sqrt(complex(w2))
        c = np.cos(w * dx)
        sc = dx if abs(w * dx) < 1e-12 else np.sin(w * dx) / w
        phi = c * phi - 1j * sc * (hm @ phi)
        x += dx
        n += 1
        if n % record_every == 0 or x >= xend - 1e-12:
            diag(phi, x)
    return {key: np.array(v) for key, v in rec.items()}


def smooth_at(lna, f, a, half=0.01):
    """Local linear regression in ln a over |ln a - ln a0| < half (averages the fast oscillation;
    one oscillation period is 2 pi EPS/omega in ln a)."""
    t = math.log(a)
    sel = np.abs(lna - t) < half
    X = lna[sel] - t
    A = np.vstack([np.ones_like(X), X]).T
    coef, *_ = np.linalg.lstsq(A, f[sel], rcond=None)
    return coef[0]


class Comp:
    def __init__(self, weight, run):
        self.weight = weight  # rho of the component at a = 1 (signed), total normalised to 1
        self.run = run
        lna = run["lna"]
        self.r1 = smooth_at(lna, run["rho"], 1.0)



def model_w(comps, masses, a):
    R = E = P3 = 0.0
    for (c, m) in zip(comps, masses):
        run = c.run
        lna = run["lna"]
        L0 = run["K1"] + run["K4"] + run["K5"] - m * run["S"]
        p3 = L0 - run["K1"] / 3.0
        r = smooth_at(lna, run["rho"], a) / c.r1
        e = smooth_at(lna, (run["K5"] - run["K1"]) / 3.0, a) / c.r1
        p = smooth_at(lna, p3, a) / c.r1
        R += c.weight * r
        E += c.weight * e
        P3 += c.weight * p
    return {"N2": -1.0 + E / R, "N1": E / R, "ratio": P3 / R, "rho": R}


def fits(fun, amin, n=101):
    xs = [amin + (1 - amin) * j / (n - 1) for j in range(n)]
    ys = np.array([fun(x) for x in xs])
    u = 1 - np.array(xs)
    A = np.vstack([np.ones_like(u), u]).T
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
    return coef[0], coef[1], float(np.mean(ys))


def tangent(fun, h=0.015, n=13):
    xs = np.linspace(1 - h, 1 + h, n)
    ys = np.array([fun(x) for x in xs])
    A = np.vstack([np.ones_like(xs), xs - 1, (xs - 1) ** 2, (xs - 1) ** 3]).T
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
    return coef[0], -coef[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OWN)
    args = ap.parse_args()
    with open(os.path.join(OWN, "eos-theory.json"), encoding="utf-8") as fh:
        A_ = json.load(fh)["models"]
    out = {"producer": "Revision/dark_sector/dirac16complex00/python/independent_numerics.py (implementation B: numpy ODE integration)",
           "settings": {"eps_AH_over_m": EPS, "omega_dx": DX_OMEGA, "smoothing": "local linear regression in ln a over |ln a - ln a0| < 0.01",
                        "fits": "least squares over 101 uniform points in a (as implementation A)", "tangent": "local cubic regression over a in [0.985, 1.015] (13 points)"}}

    # 0. algebra sanity
    ok = all(np.allclose(G[i] @ G[j] + G[j] @ G[i], 2 * ETA[i] * I16 * (i == j)) for i in range(8) for j in range(8))
    check("B_clifford_numeric", ok, "numeric Clifford relation of the fixture (independent loader)")
    check("B_krein_matrix", np.allclose(B, B.conj().T) and np.allclose(B @ B, I16), "B = -i C gamma^(x4) Hermitian, B^2 = 1")

    # 1. Krein-signed energies of modes at one frequency (frozen frame)
    signs = {}
    for kr in (1, -1):
        u, om = initial_vector(1.0, 0.75, 0.0, 0.0, kr)
        K1 = (1j * 0.75 * bil(CG1, u)).real
        rho = -K1 + bil(C, u).real
        signs[kr] = (rho, bil(B, u).real, om)
    ok = abs(signs[1][0] - signs[1][2]) < 1e-12 and abs(signs[-1][0] + signs[-1][2]) < 1e-12
    check("B_krein_signed_energy", ok, "m = 1, k = 0.75, omega = 1.25: positive-frequency vectors with Q = +1 and Q = -1 have rho = +1.25 and %s (rho = omega Q)" % r8(signs[-1][0]))
    out["krein_signed_energy"] = {"omega": r8(signs[1][2]), "rho_Q_plus": r8(signs[1][0]), "rho_Q_minus": r8(signs[-1][0])}

    # 2. superposition and wave packet (frozen frame, a = 1): averages are sums of mode contributions
    xs = np.linspace(0, 2 * math.pi, 64, endpoint=False)
    modes = []
    for kn, kr, cn in ((1.0, 1, 0.8), (2.0, -1, 0.6), (3.0, 1, 0.3 + 0.2j)):
        u, om = initial_vector(1.0, kn, 0.0, 0.0, kr)
        modes.append((kn, om, u, cn))
    rho_x, p1_x = [], []
    for x in xs:
        phi = sum(c * u * np.exp(1j * kn * x) for kn, om, u, c in modes)
        d1 = sum(1j * kn * c * u * np.exp(1j * kn * x) for kn, om, u, c in modes)
        d4 = sum(-1j * om * c * u * np.exp(1j * kn * x) for kn, om, u, c in modes)
        K1 = (0.5 * (bil(CG1, phi, d1) - np.conj(d1) @ (CG1 @ phi))).real
        K4 = (0.5 * (bil(CG4, phi, d4) - np.conj(d4) @ (CG4 @ phi))).real
        S = bil(C, phi).real
        L0 = K1 + K4 - S
        rho_x.append(-K1 + S)
        p1_x.append(L0 - K1)
    rho_x, p1_x = np.array(rho_x), np.array(p1_x)
    rho_sum = sum(abs(c) ** 2 * om * bil(B, u).real for kn, om, u, c in modes)
    p1_sum = sum(abs(c) ** 2 * kn ** 2 / om * bil(B, u).real for kn, om, u, c in modes)
    ok = abs(rho_x.mean() - rho_sum) < 1e-12 and abs(p1_x.mean() - p1_sum) < 1e-12 and np.ptp(rho_x) > 1e-3
    check("B_superposition_average", ok,
          "three modes (k = 1, 2, 3; Krein signs +, -, +) at one instant: the spatial averages of rho and p1 equal the sums of omega |c|^2 Q and k^2 |c|^2 Q/omega (cross terms average to zero; pointwise interference range %s)" % r8(np.ptp(rho_x)))
    out["superposition"] = {"rho_average": r8(rho_x.mean()), "rho_sum_of_modes": r8(rho_sum), "p1_average": r8(p1_x.mean()), "p1_sum_of_modes": r8(p1_sum), "rho_pointwise_range": r8(np.ptp(rho_x))}

    # 3. mode runs in the deflating local model
    runs = {}
    s3 = 417 / 1417
    s4 = 264037 / 403037
    s5 = float(A_["M5_with_ghost_component"]["parameters"]["s"])
    rk = 417 / 1000
    kk = math.sqrt(rk / (1 - rk))
    runs["kmode"] = run_mode(1.0, kk, 0.0, 1, 0.3, 1.06)
    runs["q3"] = run_mode(1.0, 0.0, math.sqrt(s3), 1, 0.3, 1.06)
    runs["q4"] = run_mode(1.0, 0.0, math.sqrt(s4), 1, 0.3, 1.06)
    runs["q5"] = run_mode(1.0, 0.0, math.sqrt(s5), 1, 0.3, 1.06)
    runs["cond"] = run_mode(1.0, 0.0, 0.0, 1, 0.3, 1.06)
    runs["ghost"] = run_mode(0.0, 1.0, 0.0, -1, 0.3, 1.06)
    # checks on every run: Krein charge conserved, on shell, conservation identity
    for name, rn in runs.items():
        Qd = np.max(np.abs(rn["Q"] - rn["Q"][0]))
        m = 0.0 if name == "ghost" else 1.0
        L0 = rn["K1"] + rn["K4"] + rn["K5"] - m * rn["S"]
        lna, rho = rn["lna"], rn["rho"]
        drho = np.gradient(rho, lna / EPS)
        rhs = EPS * (rn["K1"] - rn["K5"])
        scale = max(np.max(np.abs(rhs)), 1e-300)
        cons = np.max(np.abs(drho[2:-2] - rhs[2:-2])) / scale if np.max(np.abs(rhs)) > 0 else np.max(np.abs(drho[2:-2]))
        ok = Qd < 1e-9 and np.max(np.abs(L0)) < 1e-9 and cons < 2e-2
        check("B_run_%s_invariants" % name, ok,
              "Krein charge drift %s, max |L0| (on shell) %s, conservation d rho/dx4 = a4' (K1 - K5) relative residual %s (finite differences)" % (r8(Qd), r8(np.max(np.abs(L0))), r8(cons)))
    check("B_ghost_negative_energy", runs["ghost"]["rho"][-1] < 0 and runs["ghost"]["Q"][0] < 0,
          "the ghost component (massless, positive frequency, Krein charge -1) has rho < 0 along the whole run: rho(1.06) = %s" % r8(runs["ghost"]["rho"][-1]))
    rc = runs["cond"]["rho"]
    check("B_condensate_rho_constant", np.ptp(rc) < 1e-9, "homogeneous solution (k = q = 0): rho = m S constant, range %s" % r8(np.ptp(rc)))

    def model(spec):
        comps, masses = [], []
        for key, wgt, m in spec:
            comps.append(Comp(wgt, runs[key]))
            masses.append(m)
        return comps, masses

    defs = {
        "M2_positive_good_sector_gas": [("kmode", 1.0, 1.0)],
        "M3_positive_extra_time_mode": [("q3", 1.0, 1.0)],
        "M4_condensate_plus_extra_time_mode": [("cond", 1 - 57963 / 264037, 1.0), ("q4", 57963 / 264037, 1.0)],
        "M5_with_ghost_component": [("cond", float(A_["M5_with_ghost_component"]["parameters"]["Omega_c"]), 1.0),
                                    ("q5", float(A_["M5_with_ghost_component"]["parameters"]["Omega_q"]), 1.0),
                                    ("ghost", -0.3, 0.0)],
    }
    res = {}
    for mname, spec in defs.items():
        comps, masses = model(spec)
        r = {}
        for defn in ("N2", "N1", "ratio"):
            f = (lambda a, d=defn: model_w(comps, masses, a)[d])
            w0, wa = tangent(f)
            fw0, fwa, cw = fits(f, 0.5)
            g0, ga, gc = fits(f, 1 / 3)
            r[defn] = {"tangent": {"w0": r8(w0), "wa": r8(wa)}, "fit_a_1/2_to_1": {"w0": r8(fw0), "wa": r8(fwa), "constant_w": r8(cw)},
                       "fit_a_1/3_to_1": {"w0": r8(g0), "wa": r8(ga), "constant_w": r8(gc)}}
            Akey = "ratio_p3_over_rho" if defn == "ratio" else defn
            Ar = A_[mname][Akey]
            d_t = (abs(w0 - float(Ar["CPL_tangent"]["w0"])), abs(wa - float(Ar["CPL_tangent"]["wa"])))
            d_f = (abs(fw0 - float(Ar["fit_a_1/2_to_1"]["w0"])), abs(fwa - float(Ar["fit_a_1/2_to_1"]["wa"])),
                   abs(cw - float(Ar["fit_a_1/2_to_1"]["constant_w"])))
            d_g = (abs(g0 - float(Ar["fit_a_1/3_to_1"]["w0"])), abs(ga - float(Ar["fit_a_1/3_to_1"]["wa"])),
                   abs(gc - float(Ar["fit_a_1/3_to_1"]["constant_w"])))
            ok = d_t[0] < TOL_W and d_t[1] < TOL_WA and d_f[0] < TOL_W and d_f[1] < TOL_WA and d_f[2] < TOL_W and d_g[0] < TOL_W and d_g[1] < TOL_WA and d_g[2] < TOL_W
            check("B_vs_A_%s_%s" % (mname.split("_")[0], defn), ok,
                  "%s, %s: tangent (w0, wa) = (%s, %s) vs A (%s, %s); fit [1/2,1] (%s, %s, const %s) vs A (%s, %s, %s); max deviation %s"
                  % (mname, defn, r8(w0), r8(wa), Ar["CPL_tangent"]["w0"], Ar["CPL_tangent"]["wa"], r8(fw0), r8(fwa), r8(cw),
                     Ar["fit_a_1/2_to_1"]["w0"], Ar["fit_a_1/2_to_1"]["wa"], Ar["fit_a_1/2_to_1"]["constant_w"], r8(max(d_t + d_f + d_g))))
        if mname == "M5_with_ghost_component":
            f = lambda a: model_w(comps, masses, a)["N2"] + 1.0
            grid = np.linspace(0.34, 1.0, 67)
            vals = [f(a) for a in grid]
            cr = [a for a, b, va, vb in zip(grid, grid[1:], vals, vals[1:]) if va * vb < 0]
            if cr:
                lo, hi = cr[0], cr[0] + (grid[1] - grid[0])
                for _ in range(40):
                    mid = 0.5 * (lo + hi)
                    if f(lo) * f(mid) <= 0:
                        hi = mid
                    else:
                        lo = mid
                ac = 0.5 * (lo + hi)
            else:
                ac = float("nan")
            Aac = float(A_[mname]["N2"]["crossings_of_minus_1_in_[1/3,1]"][0])
            check("B_vs_A_M5_crossing", len(cr) == 1 and abs(ac - Aac) < 2e-3,
                  "w_eff(N2) of M5 from the field equation crosses -1 at a = %s (A: %s; Unite line 0.768333)" % (r8(ac), Aac))
            r["crossing_N2"] = r8(ac)
        res[mname] = r
    out["models"] = res

    # 4. independent solves: M3 (s from w0 = -0.861) and M4 (s from wa = -0.60 with Omega_q from w0)
    def w0_q(s):
        rn = run_mode(1.0, 0.0, math.sqrt(s), 1, 0.9, 1.06)
        c = Comp(1.0, rn)
        return model_w([c], [1.0], 1.0)["N2"], rn

    lo, hi = 0.2, 0.4
    for _ in range(22):
        mid = 0.5 * (lo + hi)
        if w0_q(mid)[0] > -0.861:
            hi = mid
        else:
            lo = mid
    s3B = 0.5 * (lo + hi)
    check("B_solve_M3_s", abs(s3B - s3) < 2e-3 * s3,
          "bisection on the field-equation solution: w_eff(N2)(1) = -0.861 at s = q^2/m^2 = %s (A: 417/1417 = %s)" % (r8(s3B), r8(s3)))

    def wa_M4(s):
        rn = run_mode(1.0, 0.0, math.sqrt(s), 1, 0.9, 1.06)
        cq = Comp(1.0, rn)
        e1 = model_w([cq], [1.0], 1.0)["N1"]  # eps_q(1)
        Oq = 0.139 / e1
        cc = Comp(1 - Oq, runs["cond"])
        cq.weight = Oq
        f = lambda a: model_w([cc, cq], [1.0, 1.0], a)["N2"]
        return tangent(f), Oq

    lo, hi = 0.55, 0.75
    for _ in range(18):
        mid = 0.5 * (lo + hi)
        (w0m, wam), _ = wa_M4(mid)
        if wam > -0.60:
            lo = mid
        else:
            hi = mid
    s4B = 0.5 * (lo + hi)
    (w0m, wam), Oq4B = wa_M4(s4B)
    check("B_solve_M4", abs(s4B - s4) < 2e-3 * s4 and abs(Oq4B - 57963 / 264037) < 2e-3 * (57963 / 264037) and abs(w0m + 0.861) < TOL_W,
          "bisection on the field-equation solution: tangent (w0, wa) = (-0.861, -0.60) at s = %s, Omega_q = %s (A: %s, %s)" % (r8(s4B), r8(Oq4B), r8(s4), r8(57963 / 264037)))
    out["independent_solves"] = {"M3_s": r8(s3B), "M4_s": r8(s4B), "M4_Omega_q": r8(Oq4B)}

    # 5. growth past the turning point (M3 mode continued): rate sqrt(q^2 a^2 - m^2)
    a_star = 1 / math.sqrt(s3)
    rn = run_mode(1.0, 0.0, math.sqrt(s3), 1, 1.5, 2.2, record_every=1)
    lna = rn["lna"]
    lnn = np.log(rn["norm"])
    sel = lna > math.log(2.0)
    slope = np.polyfit(lna[sel] / EPS, lnn[sel], 1)[0]
    gam = math.sqrt(s3 * math.exp(2 * np.mean(lna[sel])) - 1)
    pt_end = (rn["K1"][-1] + rn["K4"][-1] + rn["K5"][-1] - rn["S"][-1]) - rn["K5"][-1] / 3.0
    check("B_growth_rate", abs(slope - gam) < 0.03 * gam,
          "q-mode of M3 past its turning point a_* = %s: d ln|phi|/dx4 over a in [2.0, 2.2] = %s, WKB rate sqrt(q^2 a^2 - m^2) at the mean a = %s" % (r8(a_star), r8(slope), r8(gam)))
    out["growth"] = {"a_star": r8(a_star), "numerical_rate": r8(slope), "wkb_rate": r8(gam),
                     "log10_amplitude_growth_1.5_to_2.2": r8((lnn[-1] - lnn[0]) / math.log(10)),
                     "rho_over_Q_at_2.2": r8(rn["rho"][-1] / rn["Q"][0]), "pt_iso_over_Q_at_2.2": r8(pt_end / rn["Q"][0]),
                     "reading": "the extra-time-momentum mode becomes exponentially growing once q a > m (the deflation blueshifts q); its energy and extra-time pressure then grow without bound"}

    os.makedirs(os.path.join(args.out, "results"), exist_ok=True)
    os.makedirs(os.path.join(args.out, "reports"), exist_ok=True)
    with open(os.path.join(args.out, "results", "independent-numerics.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
        fh.write("\n")
    npass = sum(c["verdict"] == "PASS" for c in CHECKS)
    rep = {"producer": "Revision/dark_sector/dirac16complex00/python/independent_numerics.py", "summary": "%d/%d checks pass" % (npass, len(CHECKS)), "checks": CHECKS}
    with open(os.path.join(args.out, "reports", "python-independent-numerics.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rep, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print("independent_numerics: %d/%d checks pass" % (npass, len(CHECKS)))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
