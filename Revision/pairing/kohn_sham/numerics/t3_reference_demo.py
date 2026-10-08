#!/usr/bin/env python3
"""Revision/pairing/kohn_sham/numerics/t3_reference_demo.py - numerical demonstration of theorem T3 (SPEC section 9,
the Kohn-Sham level) with the independent Revision REFERENCE solver (Revision/kohn_sham/reference/ks_fd.py:
staggered finite differences, Sturm counts, Richardson extrapolation over G = 300, 600, 1200).

A demonstration, NOT a proof (the proof is exact: Revision/pairing/kohn_sham/t3-theory.json).

The reference is used read only, unchanged, for the plus member (m, lambda, tip theta = 0) and for the negative
control (-m, +lambda, tip theta = 0, the UNtransformed boundary condition).  Its rotated frame chi = e^{i phi sigma1} psi,
psi = (u, i w), turns the boundary conditions into w = 0 at both ends; it is written for the regular tip theta = 0
(phi(-L) = 0).  For the T3 image (-m, +lambda, tip theta = pi: a(-L) = 0) this script supplies the same frame with the
tip end rotated by pi/2 (phi(-L) = j pi/2), in two functions that replace ks_fd.sector_arrays and ks_fd.orbitals_ext
for the image runs only:
    phi = j [phi_tip (1 - s) + phi_brane s],  s = (y + L)/L,  phi_tip = 0 (theta = 0) or pi/2 (theta = pi),
    phi_brane = 0 (even, b(0) = 0) or pi/2 (odd, a(0) = 0),
with the transformed operator of ks_fd (mass M cos 2phi - K sin 2phi, momentum term M sin 2phi + K cos 2phi, scalar
phi').  For theta = 0 the formula is the reference's own frame (checked to the last bit); for theta = pi it is checked
against the exact k = 0 spectra of the image problem.  Everything else (grids, eigen-solver, densities, functional,
SCF, Mermin root, observables, Richardson) is the reference's code.

States (a subset of the canonical matrix of Revision/kohn_sham, for run time; the Rust demonstration covers all of it):
ground states N = 8 x lambda tags lam0, lamp2, lamm2 x a4,0 = 0, 1, 2 and N = 136 x lamp2, lamm2 x a4,0 = 0, 2; Mermin
states N = 8, lamp1 x a4,0 = 0, 2 x T = 0.01, 0.05 and N = 136, lamp1, a4,0 = 2, T = 0.05.  The slices belong to the history a4 = A H x4 (A = 1; x5, x6, x7 DEFLATING as
e^{-a4}), a PRESCRIBED BACKGROUND (ks-theory.json adiabaticity.historyStatus; the states violate the a4 source
conditions, Revision/field_equations_a4/reports/ks-source-conditions.json).

Usage (from the repository root; after numerics/t3_rust_demo.py, whose table it compares with):
  python Revision/pairing/kohn_sham/numerics/t3_reference_demo.py [--jobs 8]
Writes (deterministic, LF): Revision/pairing/kohn_sham/numerics/results/t3-reference-states.csv and
Revision/pairing/kohn_sham/reports/t3-reference-demo.json.  Exit 0 iff every check passes.
Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra
times; x8 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0] (brane y = 0, tip y = -L).
"""

import argparse
import csv
import hashlib
import io
import json
import math
import multiprocessing as mp
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
T3DIR = HERE.parent
REV = T3DIR.parent.parent
KS = REV / "kohn_sham"
REFDIR = KS / "reference"
sys.path.insert(0, str(REFDIR))
import run_reference as R  # noqa: E402  (read only: helpers rich3, make_phys, theory_coefficients)
import ks_fd as K  # noqa: E402

OUT_CSV = HERE / "results" / "t3-reference-states.csv"
OUT_REPORT = T3DIR / "reports" / "t3-reference-demo.json"
RUST_CSV = HERE / "results" / "t3-rust-states.csv"
GRIDS = (300, 600, 1200)
TOL = 1e-9            # T3 equality (relative, floor 1; profiles relative to their maximum)
CTRL_MIN = 1e-6
XSOLVER_TOL = 1e-8    # reference image vs Rust image (E_KS, mu: relative, floor 1)
PROFILE_NAMES = ("n", "S", "Q", "M_eff", "v_v", "e_int", "rho", "p3", "p_t", "p8")
ODD = ("S", "Q", "M_eff")
STATE = {"tip_pi": False}
ORIG_SA = K.sector_arrays
ORIG_OE = K.orbitals_ext


# ------------------------------------------------------------------------------------------------
# the rotated frame with a general tip end (theta = 0 or pi)
# ------------------------------------------------------------------------------------------------
def frame(y, L, odd, j, tip_pi):
    """phi_g(y) per sector (without the factor j) and phi' (with the factor j).  lin = (pi/2)(y + L)/L is evaluated as
    ks_fd.Grid.phi0 is, so that theta = 0 reproduces the reference's frame bit for bit."""
    lin = 0.5 * math.pi * (y + L) / L
    if tip_pi:
        # tip end phi = pi/2 (a(-L) = 0); even: pi/2 at the tip -> 0 at the brane; odd: pi/2 throughout
        phig = np.where(odd[None, :], 0.5 * math.pi, (0.5 * math.pi - lin)[:, None])
        dphi = np.where(odd, 0.0, -j * math.pi / (2.0 * L))[None, :]
    else:
        # the reference's frame: even 0; odd (pi/2)(y + L)/L
        phig = np.where(odd[None, :], lin[:, None], 0.0)
        dphi = np.where(odd, j * math.pi / (2.0 * L), 0.0)[None, :]
    return phig, dphi


def sector_arrays_general(grid, phys, sec, M, v, a4=None, wq=None, tip_pi=None):
    tip_pi = STATE["tip_pi"] if tip_pi is None else tip_pi
    a4 = phys.a4 if a4 is None else a4
    kap = np.exp(-phys.H * grid.y - a4)
    Kk = kap[:, None] * sec.kmag(phys.dk)[None, :]
    j = sec.j[None, :]
    if wq is not None:
        Kk = Kk + j * wq[:, None]
    phig, dphi = frame(grid.y, phys.L, sec.odd, sec.j, tip_pi)
    phi = j * phig
    c2, s2 = np.cos(2.0 * phi), np.sin(2.0 * phi)
    if not tip_pi:
        # the reference's own frame: exact 1 and 0 where phi = 0 (even sectors)
        c2 = np.where(sec.odd[None, :], c2, 1.0)
        s2 = np.where(sec.odd[None, :], s2, 0.0)
    else:
        # odd sectors: phi = j pi/2 exactly, cos 2phi = -1, sin 2phi = 0
        c2 = np.where(sec.odd[None, :], -1.0, c2)
        s2 = np.where(sec.odd[None, :], 0.0, s2)
    m2 = M[:, None] * c2 - Kk * s2
    k2 = M[:, None] * s2 + Kk * c2
    alpha = np.where(grid.is_u[:, None], j * (dphi + k2), j * (dphi - k2)) + v[:, None]
    beta = j * (grid.bs[:, None] + 0.5 * m2[grid.bu, :])
    return alpha, beta


def sector_arrays_patched(grid, phys, sec, M, v, a4=None, wq=None):
    if not STATE["tip_pi"]:
        return ORIG_SA(grid, phys, sec, M, v, a4=a4, wq=wq)
    return sector_arrays_general(grid, phys, sec, M, v, a4=a4, wq=wq, tip_pi=True)


def orbitals_ext_patched(grid, Z, j, odd):
    if not STATE["tip_pi"]:
        return ORIG_OE(grid, Z, j, odd)
    n = grid.n
    zp = Z / math.sqrt(grid.h)
    B = Z.shape[1]
    U = np.empty((n + 2, B))
    W = np.zeros((n + 2, B))
    U[1:n + 1:2] = zp[0::2]
    U[2:n + 1:2] = 0.5 * (zp[0:n - 1:2] + zp[2::2])
    U[0] = K.EXTRAP @ zp[0:11:2]
    U[n + 1] = K.EXTRAP @ zp[n - 1:n - 12:-2]
    W[2:n + 1:2] = zp[1::2]
    zpad = np.zeros((n + 2, B))
    zpad[1:n + 1] = zp
    W[1:n + 1:2] = 0.5 * (zpad[0:n:2] + zpad[2:n + 2:2])
    L = -grid.yext[0]
    s = (grid.yext + L) / L
    ce = np.cos(0.5 * math.pi * (1.0 - s))
    se = np.sin(0.5 * math.pi * (1.0 - s))
    ce[0], se[0] = 0.0, 1.0              # tip: phi = j pi/2 exactly
    ce[-1], se[-1] = 1.0, 0.0            # brane (even): phi = 0 exactly
    c = np.where(odd[None, :], 0.0, ce[:, None])
    sn = j[None, :] * np.where(odd[None, :], 1.0, se[:, None])
    a = c * U - sn * W
    b = sn * U + c * W
    return a, b


K.sector_arrays = sector_arrays_patched
K.orbitals_ext = orbitals_ext_patched


# ------------------------------------------------------------------------------------------------
# one member of one state
# ------------------------------------------------------------------------------------------------
def member(task):
    try:
        return _member(task)
    except Exception as e:  # a member without a self-consistent state is recorded, not hidden
        return {"id": task[1]["id"], "member": task[2], "error": "%s: %s" % (type(e).__name__, e)}


def _member(task):
    co, spec, mem = task
    STATE["tip_pi"] = (mem == "image")
    m = 1.0 if mem == "plus" else -1.0
    T = spec["T"]
    ph = R.make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"], T=T, m=m)
    g0 = K.Grid(ph, GRIDS[0])
    ls0, winfo = K.build_window(g0, ph, spec["sigma"])
    mode = "mermin" if T > 0.0 else "aufbau"
    runs = []
    for G in GRIDS:
        g = K.Grid(ph, G)
        ls = K.relabel(g, ph, ls0)
        free = K.solve_state(g, ph.copy(lam=0.0), ls, mode=mode)
        st = free if ph.lam == 0.0 else K.solve_state(g, ph, ls, mode=mode, guess=free.eps)
        o, prof = K.observables(st)
        sc = {k: o[k] for k in ("E_KS", "E_band", "E_int", "int_rho", "int_p3", "int_p_t", "int_p8", "int_n", "N_sum")}
        if T > 0.0:
            ent, lg = K.mermin_sums(st.eps, ls.deg, st.mu, T)
            sc["mu"], sc["entropy"] = st.mu, ent
            sc["Omega"] = -T * lg - o["E_int"]
            sc["F"] = sc["Omega"] + st.mu * ph.N
        else:
            homo, lumo, _, _ = K.homo_lumo(st)
            sc["HOMO"], sc["LUMO"], sc["KS_gap"] = homo, lumo, lumo - homo
        ri = g.report_indices()
        runs.append({"sc": sc, "eps": st.eps, "f": st.f, "keys": ls.keys(), "deg": ls.deg, "res": st.res,
                     "prof": {k: prof[k][ri] for k in PROFILE_NAMES}})
    out = {"id": spec["id"], "member": mem, "keys": runs[0]["keys"], "deg": runs[0]["deg"].tolist(),
           "same_keys_all_grids": all(r["keys"] == runs[0]["keys"] for r in runs),
           "f": runs[-1]["f"].tolist(), "residual_max": max(r["res"] for r in runs), "window": winfo}
    out["sc"] = {}
    for k in runs[0]["sc"]:
        Rv, U = R.rich3(*[r["sc"][k] for r in runs])
        out["sc"][k] = (float(Rv), float(U))
    Re, Ue = R.rich3(*[r["eps"] for r in runs])
    out["eps"], out["U_eps"] = Re.tolist(), Ue.tolist()
    out["eps_per_grid"] = [r["eps"].tolist() for r in runs]
    out["prof"] = {}
    for k in PROFILE_NAMES:
        Rv, U = R.rich3(*[r["prof"][k] for r in runs])
        out["prof"][k] = (Rv.tolist(), U.tolist())
    return out


def spec_list(co, params):
    calib = params["couplingCalibration"]["values"]
    sig = {"lam0": 0.0, "lamp1": 0.1, "lamm1": 0.1, "lamp2": 0.3, "lamm2": 0.3}

    def lam(n, tag):
        if tag == "lam0":
            return 0.0
        c = next(x for x in calib if int(x["N"]) == n)
        v = c["lambda1"] if tag[-1] == "1" else c["lambda2"]
        return v if tag[3] == "p" else -v

    out = [(8, tag, a4, 0.0) for tag in ("lam0", "lamp2", "lamm2") for a4 in (0.0, 1.0, 2.0)]
    out += [(136, tag, a4, 0.0) for tag in ("lamp2", "lamm2") for a4 in (0.0, 2.0)]
    out += [(8, "lamp1", a4, t) for a4 in (0.0, 2.0) for t in (0.01, 0.05)]
    out += [(136, "lamp1", 2.0, 0.05)]
    specs = []
    for n, tag, a4, t in out:
        sid = "N%d_%s_a%02d" % (n, tag, int(round(10 * a4))) + ("_T%d" % int(round(1000 * t)) if t else "")
        specs.append({"id": sid, "N": float(n), "tag": tag, "lam": lam(n, tag), "a4": a4, "T": t, "sigma": sig[tag]})
    return specs


def rel(a, b):
    return abs(a - b) / max(1.0, abs(a))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=8)
    args = ap.parse_args()
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
        print("%s %s" % ("PASS" if ok else "FAIL", name), flush=True)

    co = R.theory_coefficients()
    params = json.loads((KS / "results" / "parameters.json").read_text(encoding="utf-8"))
    ks = json.loads((KS / "ks-theory.json").read_text(encoding="utf-8"))
    hist = ks["adiabaticity"]["historyStatus"]

    # 1. the frame: theta = 0 reproduces the reference bit for bit; theta = pi gives the exact k = 0 image spectra
    ph = R.make_phys(co, a4=1.0, lam=0.0, N=8.0)
    g = K.Grid(ph, 600)
    sec = K.shell_sectors(K.shells(20))
    rng_M = 1.0 + 0.3 * np.sin(3.0 * g.y)
    rng_v = 0.05 * np.cos(2.0 * g.y)
    a0, b0 = ORIG_SA(g, ph, sec, rng_M, rng_v)
    a1, b1 = sector_arrays_general(g, ph, sec, rng_M, rng_v, tip_pi=False)
    same0 = bool(np.array_equal(a0, a1) and np.array_equal(b0, b1))
    # exact k = 0 spectra (ks-theory.json boundaryConditions.exactK0Spectra for (M, theta = 0)); the image problem
    # (-M, theta = pi) has, by the map, odd parity: eps = 0 and +-sqrt(M^2 + (n pi/L)^2); even: tan(pL) = -p/M
    worst = 0.0
    for (Mv, Lv) in ((1.0, 3.0), (2.0, 3.0)):
        phx = R.make_phys(co, m=-Mv, L=Lv, a4=0.0, lam=0.0, N=8.0)
        vals = []
        for G in GRIDS:
            gg = K.Grid(phx, G)
            s0 = K.Sectors([(0, 1, 1.0, True), (0, 1, 1.0, False)])
            al, be = sector_arrays_general(gg, phx, s0, np.full(gg.n, phx.m), np.zeros(gg.n), tip_pi=True)
            cnt = K.sturm_count(al, be * be, np.zeros(2) - 1e-9)
            idx = np.concatenate([cnt[0] + np.arange(4), cnt[1] + np.arange(3)])
            col = np.array([0] * 4 + [1] * 3)
            e, _ = K.eigen(al[:, col], be[:, col], idx)
            vals.append(e)
        Rv, _ = R.rich3(*vals)
        odd_exact = [0.0] + [math.sqrt(Mv * Mv + (k * math.pi / Lv) ** 2) for k in (1, 2, 3)]
        roots = []
        k = 0
        while len(roots) < 3:
            lo, hi = (k + 0.5) * math.pi / Lv + 1e-12, (k + 1) * math.pi / Lv - 1e-12
            fn = lambda p: math.tan(p * Lv) + p / Mv
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if fn(lo) * fn(mid) <= 0.0:
                    hi = mid
                else:
                    lo = mid
            roots.append(0.5 * (lo + hi))
            k += 1
        even_exact = [math.sqrt(Mv * Mv + p * p) for p in roots]
        worst = max(worst, float(np.max(np.abs(Rv - np.array(odd_exact + even_exact)))))
    check("image_frame_theta_pi", same0 and worst < 1e-9,
          "the rotated frame with a general tip end: for theta = 0 it gives the reference's sector matrices bit for bit "
          "(%s, 340 sectors, non-constant M(y), v(y)); for the image problem (-M, tip theta = pi) on G = 300, 600, 1200 "
          "(Richardson) the k = 0 levels equal the exact image spectra (odd parity: eps = 0 and sqrt(M^2 + (n pi/L)^2); "
          "even parity: tan(pL) = -p/M, the spectra of (M, theta = 0) with the parities exchanged) for (M, L) = (1, 3), "
          "(2, 3): max |difference| %.2e (tolerance 1e-9)" % ("identical" if same0 else "DIFFERENT", worst))

    specs = spec_list(co, params)
    tasks = [(co, s, mem) for s in specs for mem in ("plus", "image", "control")]
    tasks.sort(key=lambda t: -(t[1]["N"] * (3.0 if t[1]["T"] > 0 else 1.0)))
    with mp.Pool(args.jobs) as pool:
        outs = pool.map(member, tasks, chunksize=1)
    byk = {(o["id"], o["member"]): o for o in outs}
    probs = []
    errors = sorted("%s %s: %s" % (o["id"], o["member"], o["error"]) for o in outs if "error" in o)
    bad = [e for e in errors if " control:" not in e]
    if bad:
        probs.extend(bad[:10])
        specs = [s for s in specs if "error" not in byk[(s["id"], "plus")] and "error" not in byk[(s["id"], "image")]]

    rust = {}
    if RUST_CSV.exists():
        with RUST_CSV.open(encoding="utf-8", newline="") as fh:
            rust = {r["id"]: r for r in csv.DictReader(fh)}

    rows = []
    worst_g = worst_t = 0.0
    wid_g = wid_t = ""
    ctrl_min, ctrl_id, ctrl_none = math.inf, "", []
    nmin = (math.inf, "")
    xs_worst, xs_id, xs_n = 0.0, "", 0
    per_grid_worst = 0.0
    for s in specs:
        a, b, c = byk[(s["id"], "plus")], byk[(s["id"], "image")], byk[(s["id"], "control")]
        if not (a["same_keys_all_grids"] and b["same_keys_all_grids"]):
            probs.append("%s: label set differs between grids" % s["id"])
        ia = {tuple(k): i for i, k in enumerate(a["keys"])}
        ib = {}
        for i, k in enumerate(b["keys"]):
            n2, j, par, r = k
            ib[(n2, -j, "odd" if par == "even" else "even", r)] = i
        if set(ia) != set(ib):
            probs.append("%s: key sets differ after the map (%d vs %d)" % (s["id"], len(ia), len(ib)))
        dl = 0.0
        for k in set(ia) & set(ib):
            i, i2 = ia[k], ib[k]
            dl = max(dl, abs(a["eps"][i] - b["eps"][i2]), abs(a["f"][i] - b["f"][i2]), abs(a["deg"][i] - b["deg"][i2]))
            for G in range(len(GRIDS)):
                per_grid_worst = max(per_grid_worst, abs(a["eps_per_grid"][G][i] - b["eps_per_grid"][G][i2]))
        dsc = max(rel(a["sc"][k][0], b["sc"][k][0]) for k in a["sc"])
        dpe = dpo = 0.0
        for k in PROFILE_NAMES:
            xa, xb = np.array(a["prof"][k][0]), np.array(b["prof"][k][0])
            sg = -1.0 if k in ODD else 1.0
            dv = float(np.max(np.abs(xa - sg * xb)) / max(float(np.max(np.abs(xa))), 1e-300))
            if k in ODD:
                dpo = max(dpo, dv)
            else:
                dpe = max(dpe, dv)
        w = max(dl, dsc, dpe, dpo)
        if s["T"] > 0.0:
            if w > worst_t:
                worst_t, wid_t = w, s["id"]
        elif w > worst_g:
            worst_g, wid_g = w, s["id"]
        # control: sorted levels, scalars, n(y); a control without a self-consistent state is recorded as such
        if "error" in c:
            cd = math.inf
            ctrl_none.append(s["id"])
        else:
            la, lc = sorted(zip(a["eps"], a["deg"])), sorted(zip(c["eps"], c["deg"]))
            cd = max((max(abs(x[0] - y[0]), abs(x[1] - y[1])) for x, y in zip(la, lc)), default=0.0)
            cd = max(cd, max(rel(a["sc"][k][0], c["sc"][k][0]) for k in ("E_KS", "int_rho", "int_p3", "int_p_t", "int_p8")))
            na, nc = np.array(a["prof"]["n"][0]), np.array(c["prof"]["n"][0])
            dn = float(np.max(np.abs(na - nc)) / max(float(np.max(np.abs(na))), 1e-300))
            cd = max(cd, dn)
            if dn < nmin[0]:
                nmin = (dn, s["id"])
        if cd < ctrl_min:
            ctrl_min, ctrl_id = cd, s["id"]
        # cross-solver: the reference image against the Rust image
        xs = ""
        if s["id"] in rust:
            r = rust[s["id"]]
            xs_n += 1
            dx = rel(b["sc"]["E_KS"][0], float(r["E_KS_image"]))
            if s["T"] > 0.0:
                dx = max(dx, abs(b["sc"]["mu"][0] - float(r["mu_image"])), rel(b["sc"]["Omega"][0], float(r["Omega_image"])))
            for nm in ("rho", "p3", "p_t", "p8"):
                dx = max(dx, rel(b["sc"]["int_" + nm][0], float(r["int_%s_image" % nm])))
            xs = "%.3e" % dx
            if dx > xs_worst:
                xs_worst, xs_id = dx, s["id"]
        rows.append([s["id"], int(s["N"]), s["tag"], repr(s["lam"]), repr(s["a4"]), repr(s["T"]),
                     repr(a["sc"]["E_KS"][0]), "%.2e" % a["sc"]["E_KS"][1], repr(b["sc"]["E_KS"][0]), "%.2e" % b["sc"]["E_KS"][1],
                     repr(a["sc"]["mu"][0]) if s["T"] else repr(a["sc"]["HOMO"][0]),
                     repr(b["sc"]["mu"][0]) if s["T"] else repr(b["sc"]["HOMO"][0]),
                     repr(a["sc"]["int_p8"][0]), repr(b["sc"]["int_p8"][0]), len(a["keys"]),
                     "%.3e" % w, "%.3e" % dl, "%.3e" % dsc, "%.3e" % dpe, "%.3e" % dpo,
                     "no state" if "error" in c else repr(c["sc"]["E_KS"][0]), "no state" if "error" in c else "%.3e" % cd, xs])
    ng = sum(1 for s in specs if s["T"] == 0.0)
    nt = len(specs) - ng
    resmax = max(o["residual_max"] for o in outs if "error" not in o)
    check("all_members_converged", resmax <= 1e-12 and not probs and not bad,
          "%d states x 3 members (plus, image, control), each on G = 300, 600, 1200: SCF residual <= %.2e (tolerance "
          "1e-12 of the reference), the same label set on every grid, and the key sets of plus and image equal after the "
          "map (n2, j, parity, rank) -> (n2, -j, other parity, rank)%s" % (len(specs), resmax, "" if not probs else "; problems: " + "; ".join(probs[:8])))
    check("t3_equal_ground_states", worst_g <= TOL,
          "%d ground states (N = 8: lam0, lamp2, lamm2 x a4,0 = 0, 1, 2; N = 136: lamp2, lamm2 x a4,0 = 0, 2), Richardson values: "
          "levels by key (eps, occupation, degeneracy), E_KS, E_band, E_int, the EMT integrals (rho, p3, p_t, p8, n), N, "
          "HOMO, LUMO, KS gap, the profiles n, v_v, e_int, rho, p3, p_t, p8 (equal) and S, Q, M_eff (opposite sign) of the "
          "image (-m, +lambda, tip pi) equal those of the plus state: worst %.3e (%s), tolerance %.0e. On a single grid the "
          "levels of the two members differ by up to %.2e: the image's rotated frame is not the discrete image of the plus "
          "frame, so the two discretisations differ at O(h^2), and the equality appears in the extrapolated (continuum) "
          "values" % (ng, worst_g, wid_g, TOL, per_grid_worst))
    check("t3_equal_thermal_states", worst_t <= TOL,
          "%d Mermin states (N = 8, lamp1 x a4,0 = 0, 2 x T = 0.01, 0.05; N = 136, lamp1, a4,0 = 2, T = 0.05): levels and occupations, mu, "
          "entropy, E_KS, Omega = -T sum g ln(1 + e^(-(eps - mu)/T)) - E_int, F = Omega + mu N, EMT integrals and profiles "
          "(S, Q, M_eff with opposite sign): worst %.3e (%s), tolerance %.0e" % (nt, worst_t, wid_t, TOL))
    check("negative_control_untransformed_tip", ctrl_min > CTRL_MIN and nmin[0] > CTRL_MIN,
          "control (-m, +lambda) with the UNtransformed tip theta = 0, solved by the unchanged reference, in all %d states: "
          "the density profile alone, max_y |n_control - n_plus| / max_y |n_plus|, is at least %.3e (%s); the combined measure "
          "(that, the sorted (eps, degeneracy) list, E_KS, EMT integrals) at least %.3e (%s); required > %.0e, where the "
          "reference found a self-consistent control state; states where it found none (SCF not converging, which separates "
          "them from the converged image as well; it does not show that no such state exists): %s"
          % (len(specs), nmin[0], nmin[1], ctrl_min, ctrl_id, CTRL_MIN, ", ".join(ctrl_none) if ctrl_none else "none"))
    check("reference_image_equals_rust_image", xs_n == len(specs) and xs_worst <= XSOLVER_TOL,
          "the -M universe (-m, +lambda, tip pi) solved by the two independent solvers: reference (finite differences, "
          "Richardson) against the Rust solver (shooting, RK4; numerics/results/t3-rust-states.csv) in %d of %d states: "
          "E_KS, the EMT integrals and (thermal) mu and Omega agree to %.3e (%s), tolerance %.0e"
          % (xs_n, len(specs), xs_worst, xs_id or "-", XSOLVER_TOL))
    check("history_is_a_prescribed_background", hist.startswith("PRESCRIBED BACKGROUND"),
          "the slices belong to the history a4 = A H x4 (extra times deflating as e^{-a4}); ks-theory.json "
          "adiabaticity.historyStatus: '%s...' (Revision/field_equations_a4/reports/ks-source-conditions.json: the "
          "Kohn-Sham states are not admissible sources); T3 holds slice by slice" % hist[:120])

    head = ["id", "N", "lambda_tag", "lambda", "a4", "T", "E_KS_plus", "U_E_KS_plus", "E_KS_image", "U_E_KS_image",
            "mu_or_HOMO_plus", "mu_or_HOMO_image", "int_p8_plus", "int_p8_image", "levels", "t3_worst_dev",
            "t3_levels_dev", "t3_scalars_dev", "t3_profiles_even_dev", "t3_profiles_odd_dev",
            "E_KS_control_untransformed_tip", "control_tip_dev", "reference_vs_rust_image_dev"]
    buf = io.StringIO()
    wr = csv.writer(buf, lineterminator="\n")
    wr.writerow(head)
    wr.writerows(rows)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    OUT_CSV.write_bytes(buf.getvalue().encode("utf-8"))
    npass = sum(1 for c in checks if c["verdict"] == "PASS")
    sh = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    rep = {
        "report": "Revision/pairing/kohn_sham/reports/t3-reference-demo.json",
        "producer": "Revision/pairing/kohn_sham/numerics/t3_reference_demo.py",
        "spec": "Revision/SPEC.md section 9, theorem T3 (the Kohn-Sham level): numerical demonstration with the independent "
                "Revision reference solver (a demonstration, not part of the proof)",
        "method": "Revision/kohn_sham/reference/ks_fd.py (read only) for plus (m, lambda, tip 0) and control (-m, +lambda, tip 0); "
                  "for the image (-m, +lambda, tip pi) the reference's rotated frame with the tip end rotated by pi/2 "
                  "(phi(-L) = j pi/2), supplied here; Richardson over G = 300, 600, 1200 (run_reference.rich3)",
        "background": "slices of the PRESCRIBED BACKGROUND history a4 = A H x4 (A = 1; x5, x6, x7 deflating as e^{-a4}); the "
                      "Kohn-Sham states violate the a4 source conditions (Revision/field_equations_a4/reports/ks-source-conditions.json)",
        "inputs": {"Revision/kohn_sham/ks-theory.json": sh(KS / "ks-theory.json"),
                   "Revision/kohn_sham/reference/ks_fd.py": sh(REFDIR / "ks_fd.py"),
                   "Revision/kohn_sham/reference/run_reference.py": sh(REFDIR / "run_reference.py"),
                   "Revision/kohn_sham/results/parameters.json": sh(KS / "results" / "parameters.json"),
                   "Revision/pairing/kohn_sham/numerics/results/t3-rust-states.csv": sh(RUST_CSV) if RUST_CSV.exists() else "missing"},
        "tolerances": {"t3_equality": TOL, "control_minimum_deviation": CTRL_MIN, "reference_vs_rust": XSOLVER_TOL},
        "states": len(specs),
        "table": "Revision/pairing/kohn_sham/numerics/results/t3-reference-states.csv",
        "summary": {"checks": len(checks), "pass": npass, "fail": len(checks) - npass},
        "checks": checks,
    }
    OUT_REPORT.write_bytes((json.dumps(rep, indent=2, ensure_ascii=True) + "\n").encode("utf-8"))
    print("pass %d fail %d; wrote %s and %s" % (npass, len(checks) - npass, OUT_REPORT, OUT_CSV), flush=True)
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
