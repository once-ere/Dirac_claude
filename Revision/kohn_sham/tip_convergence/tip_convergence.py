#!/usr/bin/env python3
"""Tip-cutoff convergence of the Revision Kohn-Sham record (Revision/kohn_sham).

The record replaces the tip z -> 0 (y -> -infinity) of the author's hidden coordinate
y = ln(sin z)/(6H) by a CHOSEN regular-tip boundary condition b(-L) = 0 at the cutoff y = -L, L = 3.
This script measures how the recorded results depend on L.

How L enters the committed solver: it does NOT read L from results/parameters.json (that file is an
OUTPUT of the solver); `--root` only locates the theory inputs. L = 3 is a literal in
`base_phys()` (solver/src/runs.rs) and the RK4 step count G = 900 a literal in
`Numerics::canonical()` (solver/src/model.rs). The committed source is NOT changed: this script copies
the crate into a work directory, applies two one-line patches that read L and G from the environment
(KS_TIP_L, KS_RK4_STEPS; defaults 3 and 900), builds the copy, and verifies at L = 3, G = 900 that the
copy reproduces the committed results byte for byte (the whole canonical matrix, and every `single` run
used here against the committed binary).

Steps (all outputs in this folder, deterministic: no timings, no paths):
  1. build the patched copy; control (full matrix + singles) at L = 3;
  2. the state set at L = 3, 3.5, ..., 6 with G = 300 L (step h = 1/300 as in the record) and the
     h-check G = 600 L; two coupling protocols: FIXED lambda (the recorded constants) and RECALIBRATED
     lambda_1(L) (the record's calibration rule applied at each L);
  3. analysis: successive differences, resolution against the h-error, exponential vs double-exponential
     fits, extrapolated L -> infinity values with uncertainties where convergence is reached;
  4. independent check with the reference solver (reference/ks_fd.py) at L = 3 and L = 4.

Usage (from the repository root):
  python Revision/kohn_sham/tip_convergence/tip_convergence.py --work <scratch dir> [--jobs 8]
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import multiprocessing as mp
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
KS = HERE.parent
REPO = KS.parent.parent
SOLVER = KS / "solver"
RESULTS = KS / "results"
EXE = ".exe" if os.name == "nt" else ""
BIN_COMMITTED = SOLVER / "target" / "release" / ("revision_ks_solver" + EXE)

L_VALUES = (3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0)
STEPS_PER_UNIT_L = 300          # G = 300 L: h = L/G = 1/300, the record's step (900 steps on L = 3)
REFINE = 2                      # h-check: G = 600 L
SLICES_RUN = (0.0, 1.0, 2.0)
SLICES_CAL = (0.0, 0.5, 1.0, 1.5, 2.0)
N_VALUES = (8, 136, 688)
TAGS_FIXED = ("lam0", "lamp1", "lamm1")
THERMAL = ((136, "lam0", 2.0, 0.05), (136, "lamp1", 1.0, 0.02))
SIGMA = {"lam0": 0.0, "lamp1": 0.1, "lamm1": 0.1}
K0_MARGIN = 1.2                 # label-set margin of the free k = 0 spectrum run (N = 8, lambda = 0, a4 = 0)
REF_STATES = ((8, "lamp1", 0.0), (136, "lam0", 2.0))
REF_L = (3.0, 4.0)
REF_GRIDS_L3 = (300, 600, 1200)

# Criteria, fixed before any comparison (see README.md "Checks").
CRIT = {
    "control_single_vs_matrix_rel": 1e-12,
    "k0_analytic_abs": 5e-9,
    "zero_mode_density_rel": 1e-8,
    "noise_floor_rel": 1e-11,
    "reference_factor": 10.0,
    "reference_floor_rel": 1e-9,
    # geometric extrapolation only if the LAST TWO ratios of successive differences (step 0.5 in L) lie in (0, 0.5):
    # an algebraic tail d ~ L^-p gives ratios (L/(L + 0.5))^p > 0.5 at L >= 5 for every p < 8, so it is rejected
    # (revised from 0.9 after the first run, see README.md History)
    "ratio_max_geometric": 0.5,
    "exp_fit_max_log_residual": math.log(2.0),
}

PATCHES = (
    ("src/runs.rs",
     "Physics { hh: 1.0, m: 1.0, l: 3.0, dk: 0.25,",
     'Physics { hh: 1.0, m: 1.0, l: std::env::var("KS_TIP_L").ok().map(|s| s.parse::<f64>().expect("KS_TIP_L")).unwrap_or(3.0), dk: 0.25,'),
    ("src/model.rs",
     "            g: 900,\n",
     '            g: std::env::var("KS_RK4_STEPS").ok().map(|s| s.parse::<usize>().expect("KS_RK4_STEPS")).unwrap_or(900),\n'),
)

Q_T0 = ("E_KS", "E_int", "HOMO", "LUMO", "KS_gap", "eps_zero_mode", "int_rho", "int_p3", "int_p_t", "int_p8",
        "int_n", "rho_brane", "p3_brane", "p_t_brane", "p8_brane", "n_brane")
Q_THERMAL = ("E_KS", "mu", "entropy", "int_rho", "int_p3", "int_p_t", "int_p8", "int_n", "rho_brane",
             "p3_brane", "p_t_brane", "p8_brane", "n_brane")
DIAG = ("n_tip", "max_abs_v_v", "max_abs_Meff_minus_m", "iterations", "residual")
CSV_COLS = ("protocol", "id", "N", "lambda_tag", "lambda", "a4", "T", "L", "G", "status") + \
    tuple(dict.fromkeys(Q_T0 + Q_THERMAL + DIAG))


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def f16(x):
    if x is None:
        return ""
    if isinstance(x, (int, np.integer)) and not isinstance(x, bool):
        return str(int(x))
    return f"{float(x):.15e}"


def jclean(o):
    if isinstance(o, dict):
        return {k: jclean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jclean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        x = float(o)
        return x if math.isfinite(x) else None
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


def write_text(p: Path, s: str):
    p.write_bytes(s.encode("utf-8"))


def round_sig(x, d=4):
    if x == 0.0:
        return 0.0
    e = math.floor(math.log10(abs(x))) - (d - 1)
    if e >= 0:
        p = 10.0 ** e
        return round(x / p) * p
    p = 10.0 ** (-e)
    return round(x * p) / p


def grid_steps(L, refine=1):
    return int(round(STEPS_PER_UNIT_L * L * refine))


def lstr(L):
    return f"{L:.1f}".replace(".", "p")


# --------------------------------------------------------------------------------------------------
# 1. patched copy of the solver
# --------------------------------------------------------------------------------------------------
def build_patched(work: Path):
    src_files = sorted(p for p in (SOLVER / "src").glob("*.rs"))
    committed = {f"src/{p.name}": sha256(p) for p in src_files}
    committed["Cargo.toml"] = sha256(SOLVER / "Cargo.toml")
    committed["Cargo.lock"] = sha256(SOLVER / "Cargo.lock")
    dst = work / "solver_tipL"
    if dst.exists():
        shutil.rmtree(dst)
    (dst / "src").mkdir(parents=True)
    for p in src_files:
        shutil.copyfile(p, dst / "src" / p.name)
    shutil.copyfile(SOLVER / "Cargo.toml", dst / "Cargo.toml")
    shutil.copyfile(SOLVER / "Cargo.lock", dst / "Cargo.lock")
    applied = []
    for rel, old, new in PATCHES:
        p = dst / rel
        s = p.read_bytes().decode("utf-8")
        cnt = s.count(old)
        if cnt != 1:
            raise SystemExit(f"patch target in {rel} found {cnt} times (expected exactly 1)")
        write_text(p, s.replace(old, new))
        applied.append({"file": rel, "old": old.strip(), "new": new.strip(), "matches": cnt,
                        "patchedSha256": sha256(p)})
    env = dict(os.environ, CARGO_TARGET_DIR=str(dst / "target"))
    r = subprocess.run(["cargo", "build", "--release", "--manifest-path", str(dst / "Cargo.toml")],
                       env=env, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("cargo build of the patched copy failed:\n" + r.stderr[-3000:])
    return dst / "target" / "release" / ("revision_ks_solver" + EXE), committed, applied


# --------------------------------------------------------------------------------------------------
# solver runs
# --------------------------------------------------------------------------------------------------
def run_single(spec, binary: Path, outdir: Path):
    """spec: dict with id, N, lam, a4, T, L, G, margin. Returns the parsed record (or the failure)."""
    tag = f"{spec['id']}_L{lstr(spec['L'])}_G{spec['G']}"
    js, pr = outdir / f"{tag}.json", outdir / f"{tag}.csv"
    for p in (js, pr):
        if p.exists():
            p.unlink()
    cmd = [str(binary), "single", "--m", "1", "--lambda", repr(spec["lam"]), "--a4", repr(spec["a4"]),
           "--N", repr(float(spec["N"])), "--margin", repr(spec["margin"]), "--out", str(js), "--profiles", str(pr)]
    if spec["T"] > 0:
        cmd += ["--T", repr(spec["T"])]
    env = dict(os.environ, KS_TIP_L=repr(spec["L"]), KS_RK4_STEPS=str(spec["G"]))
    r = subprocess.run(cmd, cwd=str(REPO), env=env, capture_output=True, text=True)
    rec = {"rc": r.returncode, "json_path": js, "profiles_path": pr}
    if not js.exists():
        err = [ln for ln in r.stderr.splitlines() if ln.startswith("error")]
        rec["status"] = "scf_failed"
        rec["error"] = (err[-1] if err else r.stderr.strip().splitlines()[-1])[:400]
        return rec
    rec["status"] = "ok" if r.returncode == 0 else "not_converged"
    rec.update(parse_single(js, pr, spec))
    return rec


def parse_single(js: Path, pr: Path, spec):
    d = json.loads(js.read_text(encoding="utf-8"))
    o = {"E_KS": d["E_KS"], "E_band": d["E_band"], "E_int": d["E_int"], "iterations": d["iterations"],
         "residual": d["residual"]}
    em = d["emtIntegrals_2Vol7_int_e6Hy"]
    for k, v in (("int_rho", "rho"), ("int_p3", "p3"), ("int_p_t", "p_t"), ("int_p8", "p8"), ("int_n", "n")):
        o[k] = em[v]
    lv = d["levels_n2_j_parity_label_eps_deg_f"]
    o["levels"] = lv
    if spec["T"] > 0:
        o["mu"] = d["mu_or_fermi_level"]
        o["entropy"] = d["entropy"]
    else:
        occ = [x[4] for x in lv if x[6] > 0.0]
        emp = [x[4] for x in lv if x[6] < 1.0]
        o["HOMO"] = max(occ)
        o["LUMO"] = min(emp)
        o["KS_gap"] = o["LUMO"] - o["HOMO"]
        zm = [x[4] for x in lv if x[0] == 0 and x[1] == 1 and x[2] == "even" and x[3] == 0]
        o["eps_zero_mode"] = zm[0] if zm else None
    rows = list(csv.reader(io.StringIO(pr.read_text(encoding="utf-8"))))
    hdr = rows[0]
    data = np.array([[float(v) for v in r] for r in rows[1:]])
    col = {h: data[:, i] for i, h in enumerate(hdr)}
    o["y"] = col["y"]
    o["profiles"] = col
    for nm in ("rho", "p3", "p_t", "p8", "n"):
        o[f"{nm}_brane"] = float(col[nm][-1])
    o["n_tip"] = float(col["n"][0])
    o["max_abs_v_v"] = float(np.max(np.abs(col["v_v"])))
    o["max_abs_Meff_minus_m"] = float(np.max(np.abs(col["M_eff"] - 1.0)))
    o["strength_sampled"] = float(np.max(np.maximum(15.0 / 16.0 * np.abs(col["S"]), np.abs(col["n"]) / 16.0)))
    o["strength"] = max(continuous_max(col["y"], 15.0 / 16.0 * np.abs(col["S"])), continuous_max(col["y"], np.abs(col["n"]) / 16.0))
    return o


def continuous_max(y, f):
    """maximum of a smooth profile sampled on the 151 report points: the largest sample, refined by the
    quartic through the 5 nearest samples (maximised on the two adjacent intervals); an end-point maximum is
    taken as it is (as the reference solver does for the coupling strength)"""
    i = int(np.argmax(f))
    if i == 0 or i == len(f) - 1:
        return float(f[i])
    lo = min(max(i - 2, 0), len(f) - 5)
    c = np.polyfit(y[lo:lo + 5] - y[i], f[lo:lo + 5], 4)
    t = np.linspace(y[i - 1] - y[i], y[i + 1] - y[i], 2001)
    return float(max(f[i], np.max(np.polyval(c, t))))


def run_pool(specs, binary, outdir, jobs):
    outdir.mkdir(parents=True, exist_ok=True)
    order = sorted(range(len(specs)), key=lambda i: (-specs[i]["N"] * specs[i]["L"], i))  # long first
    res = [None] * len(specs)
    with ThreadPoolExecutor(max_workers=jobs) as ex:
        futs = {i: ex.submit(run_single, specs[i], binary, outdir) for i in order}
        for i, f in futs.items():
            res[i] = f.result()
    return res


def state_id(N, tag, a4, T=0.0):
    s = f"N{N}_{tag}_a{int(round(10 * a4)):02d}"
    return s + (f"_T{int(round(1000 * T))}" if T > 0 else "")


def committed_couplings():
    par = json.loads((RESULTS / "parameters.json").read_text(encoding="utf-8"))
    out = {}
    for v in par["couplingCalibration"]["values"]:
        out[int(v["N"])] = {"lambda1": v["lambda1"], "strength": v["strengthPerLambda"],
                            "atSlices": v["strengthPerLambdaAtSlices"]}
    return par, out


def fixed_specs(lam1):
    specs = []
    for N in N_VALUES:
        for tag in TAGS_FIXED:
            lam = {"lam0": 0.0, "lamp1": lam1[N], "lamm1": -lam1[N]}[tag]
            for a4 in SLICES_RUN:
                specs.append({"id": state_id(N, tag, a4), "N": N, "tag": tag, "lam": lam, "a4": a4, "T": 0.0,
                              "margin": 0.25 + 2 * SIGMA[tag]})
    for (N, tag, a4, T) in THERMAL:
        lam = {"lam0": 0.0, "lamp1": lam1[N], "lamm1": -lam1[N]}[tag]
        specs.append({"id": state_id(N, tag, a4, T), "N": N, "tag": tag, "lam": lam, "a4": a4, "T": T,
                      "margin": 0.2 + 2 * SIGMA[tag]})
    return specs


def with_L(specs, L, refine=1):
    return [dict(s, L=L, G=grid_steps(L, refine)) for s in specs]


# --------------------------------------------------------------------------------------------------
# reference solver (independent discretisation)
# --------------------------------------------------------------------------------------------------
def ref_job(args):
    N, tag, lam, a4, L = args
    sys.path.insert(0, str(KS / "reference"))
    import run_reference as R  # noqa: E402
    K = R.K
    co = R.theory_coefficients()
    grids = tuple(int(round(G * L / 3.0)) for G in REF_GRIDS_L3)
    ph = R.make_phys(co, a4=a4, lam=lam, N=float(N), L=L)
    g0 = K.Grid(ph, grids[0])
    ls0, _ = K.build_window(g0, ph, R.SIGMA[tag], pad_ranks=R.PAD_RANKS)
    vals = []
    for G in grids:
        g = K.Grid(ph, G)
        ls = K.relabel(g, ph, ls0)
        free = K.solve_state(g, ph.copy(lam=0.0), ls)
        gs = free if lam == 0.0 else K.solve_state(g, ph, ls, guess=free.eps)
        o, _ = K.observables(gs)
        homo, lumo, _, _ = K.homo_lumo(gs)
        vals.append({"E_KS": o["E_KS"], "E_int": o["E_int"], "HOMO": homo, "LUMO": lumo, "int_p8": o["int_p8"],
                     "int_n": o["int_n"], "int_rho": o["int_rho"]})
    out = {"grids": list(grids)}
    for k in vals[0]:
        Rv, U = R.rich3(*[v[k] for v in vals])
        out[k] = {"value": float(Rv), "U": float(U)}
    return out


# --------------------------------------------------------------------------------------------------
# analysis
# --------------------------------------------------------------------------------------------------
def odd_roots(m, L, nr):
    out = []
    for l in range(nr):
        lo, hi = (l + 0.5) * math.pi / L, (l + 1) * math.pi / L
        f = lambda p: m * math.sin(p * L) + p * math.cos(p * L)  # noqa: E731
        flo = f(lo)
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            fm = f(mid)
            if (fm > 0) == (flo > 0):
                lo, flo = mid, fm
            else:
                hi = mid
        out.append(0.5 * (lo + hi))
    return out


def analytic_k0(L, parity, label, m=1.0):
    if parity == "even":
        return 0.0 if label == 0 else math.copysign(math.sqrt(m * m + (abs(label) * math.pi / L) ** 2), label)
    p = odd_roots(m, L, 12)
    return math.sqrt(m * m + p[label] ** 2) if label >= 0 else -math.sqrt(m * m + p[-label - 1] ** 2)


def fit_log(xs, ys):
    """least squares ln|d| = a + b x; returns b, max |residual|, rss"""
    A = np.vstack([np.ones(len(xs)), np.asarray(xs)]).T
    y = np.log(np.abs(np.asarray(ys)))
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    r = y - A @ c
    return float(c[1]), float(np.max(np.abs(r))), float(np.sum(r * r))


def analyse_series(Ls, x, xh):
    """x[L] (G = 300 L) and xh[L] (G = 600 L) or None. Returns the convergence record of one quantity."""
    out = {"L": list(Ls), "value": [x.get(L) for L in Ls]}
    eh = {}
    for L in Ls:
        if x.get(L) is not None and xh.get(L) is not None:
            eh[L] = 16.0 / 15.0 * abs(xh[L] - x[L])
        else:
            eh[L] = None
    out["h_error"] = [eh[L] for L in Ls]
    # contiguous successes from L = 3
    ok = []
    for L in Ls:
        if x.get(L) is None:
            break
        ok.append(L)
    failed_at = None if len(ok) == len(Ls) else Ls[len(ok)]
    out["first_failed_L"] = failed_at

    def noise(L):
        return (eh[L] or 0.0) + CRIT["noise_floor_rel"] * max(1.0, abs(x[L]))
    diffs = []
    for a, b in zip(ok[:-1], ok[1:]):
        d = x[b] - x[a]
        diffs.append({"from": a, "to": b, "diff": d, "noise": noise(a) + noise(b), "resolved": abs(d) > noise(a) + noise(b)})
    out["differences"] = diffs
    res = {"verdict": None, "extrapolated": None, "U": None, "rate_per_unit_L": None, "fits": None}
    if len(ok) < 3:
        res["verdict"] = "NOT ESTABLISHED: fewer than 3 converged L values" + (f" (SCF fails at L = {failed_at})" if failed_at else "")
        out["convergence"] = res
        return out
    # trailing unresolved differences = converged within noise
    k = len(diffs)
    while k > 0 and not diffs[k - 1]["resolved"]:
        k -= 1
    xl = x[ok[-1]]
    if k < len(diffs):
        Lc = diffs[k]["from"]
        res["verdict"] = f"converged within the numerical noise from L = {Lc}"
        res["extrapolated"] = xl
        res["U"] = abs(diffs[-1]["diff"]) + noise(ok[-1])
        res["converged_from_L"] = Lc
    else:
        d1, d2 = diffs[-2]["diff"], diffs[-1]["diff"]
        r = d2 / d1 if d1 != 0 else float("inf")
        rs = [diffs[i + 1]["diff"] / diffs[i]["diff"] if diffs[i]["diff"] != 0 else float("inf")
              for i in range(max(0, len(diffs) - 3), len(diffs) - 1)]
        res["last_ratio"] = r
        res["last_ratios"] = rs
        if not all(0.0 < q < CRIT["ratio_max_geometric"] for q in rs):
            res["verdict"] = (f"NOT CONVERGED: last ratios of successive differences {', '.join(f'{q:.3g}' for q in rs)} "
                              f"(|d| at L = {ok[-2]}..{ok[-1]}: {abs(d2):.3e})")
        else:
            tail = d2 * r / (1.0 - r)
            res["extrapolated"] = xl + tail
            res["U"] = abs(tail) + noise(ok[-1])
            res["rate_per_unit_L"] = -math.log(r) / (ok[-1] - ok[-2])
            res["verdict"] = "converging (geometric tail from the last two differences)"
    # exponential vs double-exponential test on the resolved differences
    rd = [d for d in diffs if d["resolved"]]
    if len(rd) >= 3:
        mids = [0.5 * (d["from"] + d["to"]) for d in rd]
        vals = [d["diff"] for d in rd]
        b1, m1, s1 = fit_log(mids, vals)
        b2, m2, s2 = fit_log([math.exp(t) for t in mids], vals)
        rat = [vals[i + 1] / vals[i] for i in range(len(vals) - 1)]
        lr = [math.log(abs(q)) for q in rat]
        if all(q > 0 for q in rat) and all(lr[i + 1] < lr[i] for i in range(len(lr) - 1)) and m1 > CRIT["exp_fit_max_log_residual"]:
            kind = "faster than exponential (ratios of successive differences decrease; exponential fit rejected)"
        elif m1 <= CRIT["exp_fit_max_log_residual"] and all(abs(q) < 1 for q in rat):
            kind = "consistent with exponential convergence"
        elif any(abs(q) >= 1 for q in rat):
            kind = "differences grow: not converging"
        else:
            kind = "neither a clean exponential nor a monotone faster-than-exponential law"
        res["fits"] = {"n_resolved": len(rd), "exp_rate_per_unit_L": -b1, "exp_max_log_residual": m1, "exp_rss": s1,
                       "doubleexp_coefficient_of_e^L": -b2, "doubleexp_max_log_residual": m2, "doubleexp_rss": s2,
                       "ratios": rat, "classification": kind}
    out["convergence"] = res
    return out


# --------------------------------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--work", required=True, help="scratch directory (patched copy, raw runs)")
    ap.add_argument("--jobs", type=int, default=8, help="worker processes (default 8)")
    ap.add_argument("--debug-skip-control-matrix", action="store_true",
                    help="development only: skip the full-matrix control (its check then FAILS as not run)")
    a = ap.parse_args()
    work = Path(a.work).resolve()
    work.mkdir(parents=True, exist_ok=True)
    jobs = max(1, min(a.jobs, 8))
    t0 = time.time()
    tlog = lambda s: print(f"[{time.time() - t0:7.1f} s] {s}", file=sys.stderr, flush=True)  # noqa: E731
    checks = []

    def check(name, crit, ok, detail):
        checks.append({"name": name, "criterion": crit, "result": "PASS" if ok else "FAIL", "detail": detail})
        print(f"{'PASS' if ok else 'FAIL'} - {name}: {detail}", file=sys.stderr, flush=True)

    # ---- 1. build and control -------------------------------------------------------------------
    binp, committed_src, applied = build_patched(work)
    tlog("patched copy built")
    ctl = work / "control_all"
    if ctl.exists():
        shutil.rmtree(ctl)
    env = dict(os.environ, KS_TIP_L="3", KS_RK4_STEPS="900")
    if a.debug_skip_control_matrix:
        ctl.mkdir(parents=True)
    r = subprocess.CompletedProcess([], 99, "", "") if a.debug_skip_control_matrix else subprocess.run([str(binp), "all", "--root", str(REPO), "--out", str(ctl), "--report",
                        str(work / "control_all-report.json"), "--threads", str(jobs)],
                       cwd=str(REPO), env=env, capture_output=True, text=True)
    man = json.loads((RESULTS / "manifest.json").read_text(encoding="utf-8"))
    want = {f["path"]: f["sha256"] for f in man["files"]}
    want["manifest.json"] = sha256(RESULTS / "manifest.json")
    got = {p.relative_to(ctl).as_posix(): sha256(p) for p in ctl.rglob("*") if p.is_file()}
    diff = sorted(k for k in set(want) | set(got) if want.get(k) != got.get(k))
    check("control_full_matrix_byte_identical",
          "the patched copy with KS_TIP_L = 3, KS_RK4_STEPS = 900 runs `all` (exit SUCCESS) and writes every file of "
          "Revision/kohn_sham/results byte for byte (SHA-256 of results/manifest.json, and manifest.json itself)",
          r.returncode == 0 and not diff,
          f"exit {r.returncode} ({r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ''}); {len(got)} files written, "
          f"{len(want)} committed; differing or missing: {diff[:10] if diff else 'none'}")
    tlog("control matrix done")

    par, cal = committed_couplings()
    lam1 = {N: cal[N]["lambda1"] for N in N_VALUES}
    assert par["physics"]["L_tipCutoff"] == 3.0 and par["numerics"]["rk4Steps"] == 900
    base = fixed_specs(lam1)
    k0spec = {"id": "N8_lam0_a00_k0spectrum", "N": 8, "tag": "lam0", "lam": 0.0, "a4": 0.0, "T": 0.0, "margin": K0_MARGIN}
    raw = work / "runs"
    if raw.exists():
        shutil.rmtree(raw)

    # control singles: committed binary vs patched copy at L = 3, G = 900
    s3 = with_L(base + [k0spec], 3.0)
    rc = run_pool(s3, BIN_COMMITTED, raw / "control_committed", jobs)
    rp = run_pool(s3, binp, raw / "control_patched", jobs)
    nbad = [s["id"] for s, x, y in zip(s3, rc, rp)
            if x["status"] != y["status"] or x["json_path"].read_bytes() != y["json_path"].read_bytes()
            or x["profiles_path"].read_bytes() != y["profiles_path"].read_bytes()]
    check("control_single_byte_identical",
          "every `single` run of this study at L = 3 (G = 900): the committed binary and the patched copy write "
          "byte-identical JSON records and profiles", not nbad,
          f"{len(s3)} states; differing: {nbad if nbad else 'none'}")
    # control against the committed matrix (CSV values)
    summ = {r_["id"]: r_ for r_ in csv.DictReader(io.StringIO((RESULTS / "ground/summary.csv").read_text(encoding="utf-8")))}
    emt = {r_["id"]: r_ for r_ in csv.DictReader(io.StringIO((RESULTS / "ground/emt-integrals.csv").read_text(encoding="utf-8")))}
    thm = {r_["id"]: r_ for r_ in csv.DictReader(io.StringIO((RESULTS / "thermo/thermodynamics.csv").read_text(encoding="utf-8")))}
    worst, nexact, ncmp, fails = 0.0, 0, 0, []
    for s, x in zip(s3, rp):
        if s["id"] == k0spec["id"]:
            continue
        pairs = []
        if s["T"] == 0:
            for k in ("E_KS", "HOMO", "LUMO", "KS_gap"):
                pairs.append((k, x[k], float(summ[s["id"]][k])))
            for k in ("int_rho", "int_p3", "int_p_t", "int_p8", "int_n", "rho_brane", "p3_brane", "p_t_brane", "p8_brane"):
                pairs.append((k, x[k], float(emt[s["id"]][k])))
        else:
            for k, kk in (("E_KS", "E"), ("mu", "mu"), ("entropy", "entropy")):
                pairs.append((k, x[k], float(thm[s["id"]][kk])))
        for k, v, w in pairs:
            ncmp += 1
            rel = abs(v - w) / max(1.0, abs(w))
            nexact += (v == w)
            if rel > worst:
                worst = rel
            if rel > CRIT["control_single_vs_matrix_rel"]:
                fails.append(f"{s['id']}:{k}")
    check("control_single_vs_committed_matrix",
          f"the `single` values at L = 3 equal the committed matrix (ground/summary.csv, ground/emt-integrals.csv, "
          f"thermo/thermodynamics.csv) within {CRIT['control_single_vs_matrix_rel']:.0e} x max(1, |x|)",
          not fails, f"{ncmp} comparisons, {nexact} bit-identical, worst relative difference {worst:.2e}; failures: {fails if fails else 'none'}")
    tlog("control singles done")

    # ---- 2. the L scan --------------------------------------------------------------------------
    # protocol FIXED: the recorded couplings
    allspecs = []
    for L in L_VALUES:
        for rf in (1, REFINE):
            for s in base + [k0spec]:
                allspecs.append(dict(s, L=L, G=grid_steps(L, rf), protocol="fixed", refine=rf))
    # protocol RECAL: calibration runs (free ground states at every slice of the history)
    calspecs = []
    for L in L_VALUES:
        for N in N_VALUES:
            for a4 in SLICES_CAL:
                calspecs.append({"id": f"cal_N{N}_a{int(round(10 * a4)):02d}", "N": N, "tag": "lam0", "lam": 0.0, "a4": a4,
                                 "T": 0.0, "margin": 0.25, "L": L, "G": grid_steps(L), "protocol": "calibration", "refine": 1})
    res_fixed = run_pool(allspecs, binp, raw / "fixed", jobs)
    tlog("fixed-lambda scan done")
    res_cal = run_pool(calspecs, binp, raw / "calibration", jobs)
    strength = {}
    for s, x in zip(calspecs, res_cal):
        strength.setdefault((s["L"], s["N"]), []).append(x["strength"])
    lam1_L = {k: round_sig(0.1 / max(v), 4) for k, v in strength.items()}
    badcal = [N for N in N_VALUES if lam1_L[(3.0, N)] != lam1[N]]
    rels = {N: abs(max(strength[(3.0, N)]) - cal[N]["strength"]) / cal[N]["strength"] for N in N_VALUES}
    check("calibration_rule_reproduced_at_L3",
          "the record's calibration rule evaluated on the free ground states (5 slices; the maximum over y of the 151-point "
          "profiles refined by local quartic interpolation, see continuous_max) gives, "
          "at L = 3, exactly the recorded lambda_1 (4 significant digits) for N = 8, 136, 688",
          not badcal, f"lambda_1(L=3) = {[lam1_L[(3.0, N)] for N in N_VALUES]}, recorded {[lam1[N] for N in N_VALUES]}; "
          f"relative difference of the strengths {', '.join(f'N={N}: {rels[N]:.1e}' for N in N_VALUES)}")
    recspecs = []
    for L in L_VALUES:
        for rf in (1, REFINE):
            for N in N_VALUES:
                for tag, sg in (("lamp1", 1.0), ("lamm1", -1.0)):
                    for a4 in SLICES_RUN:
                        recspecs.append({"id": state_id(N, tag, a4), "N": N, "tag": tag, "lam": sg * lam1_L[(L, N)],
                                         "a4": a4, "T": 0.0, "margin": 0.25 + 2 * SIGMA[tag], "L": L,
                                         "G": grid_steps(L, rf), "protocol": "recalibrated", "refine": rf})
    res_rec = run_pool(recspecs, binp, raw / "recalibrated", jobs)
    tlog("recalibrated scan done")

    # ---- table ----------------------------------------------------------------------------------
    rows = []
    for s, x in list(zip(allspecs, res_fixed)) + list(zip(recspecs, res_rec)):
        row = {"protocol": s["protocol"], "id": s["id"], "N": s["N"], "lambda_tag": s["tag"], "lambda": f16(s["lam"]),
               "a4": f16(s["a4"]), "T": f16(s["T"]), "L": f16(s["L"]), "G": s["G"], "status": x["status"]}
        for c in CSV_COLS[10:]:
            row[c] = f16(x.get(c)) if x["status"] != "scf_failed" else ""
        rows.append(row)
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=CSV_COLS, lineterminator="\n")
    w.writeheader()
    for row in rows:
        w.writerow(row)
    write_text(HERE / "tip-convergence-table.csv", buf.getvalue())

    # ---- 3. analysis ----------------------------------------------------------------------------
    def series(specs, results, sid, q):
        x, xh = {}, {}
        for s, r_ in zip(specs, results):
            if s["id"] != sid or r_["status"] == "scf_failed" or r_.get(q) is None:
                continue
            (x if s["refine"] == 1 else xh)[s["L"]] = r_[q]
        return x, xh

    def fails_of(specs, results, sid):
        return [{"L": s["L"], "G": s["G"], "status": r_["status"], "error": r_.get("error")}
                for s, r_ in zip(specs, results) if s["id"] == sid and r_["status"] != "ok"]

    analysis = {"fixed": {}, "recalibrated": {}}
    ext_rows = []
    for proto, specs, results, idl in (("fixed", allspecs, res_fixed, [s["id"] for s in base]),
                                       ("recalibrated", recspecs, res_rec, sorted({s["id"] for s in recspecs}))):
        for sid in idl:
            sp = next(s for s in specs if s["id"] == sid)
            qs = Q_THERMAL if sp["T"] > 0 else Q_T0
            ent = {"N": sp["N"], "lambda_tag": sp["tag"], "a4": sp["a4"], "T": sp["T"],
                   "failures": fails_of(specs, results, sid), "quantities": {}}
            if proto == "recalibrated":
                ent["lambda_of_L"] = {f16(L): lam1_L[(L, sp["N"])] * (1 if sp["tag"] == "lamp1" else -1) for L in L_VALUES}
            for q in qs:
                x, xh = series(specs, results, sid, q)
                a_ = analyse_series(L_VALUES, x, xh)
                ent["quantities"][q] = a_
                c = a_["convergence"]
                ext_rows.append({"protocol": proto, "id": sid, "quantity": q,
                                 "value_L3": f16(x.get(3.0)), "value_Lmax_converged": f16(x[max(x)]) if x else "",
                                 "Lmax_converged": f16(max(x)) if x else "",
                                 "first_failed_L": f16(a_["first_failed_L"]),
                                 "extrapolated_Linf": f16(c["extrapolated"]), "U": f16(c["U"]),
                                 "L3_minus_Linf": f16(x[3.0] - c["extrapolated"]) if (c["extrapolated"] is not None and 3.0 in x) else "",
                                 "verdict": c["verdict"],
                                 "fit_classification": c["fits"]["classification"] if c["fits"] else ""})
            analysis[proto][sid] = ent
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(ext_rows[0].keys()), lineterminator="\n")
    w.writeheader()
    for row in ext_rows:
        w.writerow(row)
    write_text(HERE / "tip-convergence-extrapolation.csv", buf.getvalue())

    # free k = 0 spectrum: exact L dependence
    k0 = []
    worst_k0 = 0.0
    for s, x in zip(allspecs, res_fixed):
        if s["id"] != k0spec["id"] or s["refine"] != 1:
            continue
        for lv in x["levels"]:
            if lv[0] != 0:
                continue
            ex = analytic_k0(s["L"], lv[2], lv[3])
            k0.append({"L": s["L"], "j": lv[1], "parity": lv[2], "label": lv[3], "eps": lv[4], "analytic": ex, "diff": lv[4] - ex})
            worst_k0 = max(worst_k0, abs(lv[4] - ex))
    check("k0_spectrum_exact_L_dependence",
          f"free k = 0 levels of the scan (both block types, both parities, every L) equal the exact spectrum "
          f"(even: 0 and sqrt(m^2 + (l pi/L)^2); odd: sqrt(m^2 + p^2), tan(pL) = -p/m) within {CRIT['k0_analytic_abs']:.0e} m",
          worst_k0 <= CRIT["k0_analytic_abs"], f"{len(k0)} levels, max |difference| {worst_k0:.2e} m")
    bulk_edge = {f16(L): analytic_k0(L, "odd", 0) for L in L_VALUES}
    # zero-mode density: exact brane and tip values of the free N = 8 state
    vol7 = par["physics"]["Vol7"]
    zm_rows, worst_zm = [], 0.0
    for s, x in zip(allspecs, res_fixed):
        if s["id"] == "N8_lam0_a00" and s["refine"] == 1:
            L = s["L"]
            nb = 8.0 / (vol7 * (1.0 - math.exp(-2.0 * L)))
            nt = nb * math.exp(4.0 * L)
            e1 = abs(x["n_brane"] / nb - 1)
            e2 = abs(x["n_tip"] / nt - 1)
            worst_zm = max(worst_zm, e1, e2)
            zm_rows.append({"L": L, "n_brane": x["n_brane"], "n_brane_exact": nb, "n_tip": x["n_tip"], "n_tip_exact": nt})
    check("zero_mode_density_exact",
          f"free N = 8 (the 8 brane zero modes chi ~ e^{{my}}): proper density n(0) = 8/(Vol_7 (1 - e^{{-2mL}})) and "
          f"n(-L) = n(0) e^{{(6H - 2m)L}} at every L, within {CRIT['zero_mode_density_rel']:.0e} relative",
          worst_zm <= CRIT["zero_mode_density_rel"], f"{len(zm_rows)} L values, worst relative deviation {worst_zm:.2e}")
    # first-order interaction energy of the zero modes with a fixed lambda (diagnostic)
    fo = []
    for s, x in zip(allspecs, res_fixed):
        if s["N"] == 8 and s["tag"] in ("lamp1", "lamm1") and s["a4"] == 0.0 and s["refine"] == 1:
            L = s["L"]
            e1 = -(2.0 * s["lam"] / vol7) * math.exp(2.0 * L) / (1.0 - math.exp(-2.0 * L))
            v1 = abs(s["lam"]) / 16.0 * 8.0 / (vol7 * (1.0 - math.exp(-2.0 * L))) * math.exp(4.0 * L)
            fo.append({"id": s["id"], "L": L, "lambda": s["lam"], "E_int_first_order": e1, "tip_potential_first_order": v1,
                       "status": x["status"], "E_KS": x.get("E_KS"), "E_int": x.get("E_int"),
                       "max_abs_v_v": x.get("max_abs_v_v"), "E_KS_over_first_order": (x["E_KS"] / e1) if x.get("E_KS") is not None else None,
                       "error": x.get("error")})
    tlog("analysis done")

    # ---- 4. reference ---------------------------------------------------------------------------
    rjobs = []
    for (N, tag, a4) in REF_STATES:
        lam = {"lam0": 0.0, "lamp1": lam1[N], "lamm1": -lam1[N]}[tag]
        for L in REF_L:
            rjobs.append((N, tag, lam, a4, L))
    with mp.get_context("spawn").Pool(min(jobs, len(rjobs))) as pool:
        rref = pool.map(ref_job, rjobs)
    tlog("reference done")
    refcmp, rfail, rworst = [], [], 0.0
    for (N, tag, lam, a4, L), rr in zip(rjobs, rref):
        sid = state_id(N, tag, a4)
        for q in ("E_KS", "E_int", "HOMO", "LUMO", "int_p8", "int_n", "int_rho"):
            x, xh = series(allspecs, res_fixed, sid, q)
            if q == "E_int":
                x = {}
                xh = {}
                for s, r_ in zip(allspecs, res_fixed):
                    if s["id"] == sid and r_["status"] != "scf_failed":
                        (x if s["refine"] == 1 else xh)[s["L"]] = r_["E_int"]
            ur = 16.0 / 15.0 * abs(xh[L] - x[L])
            v, vr, Ur = x[L], rr[q]["value"], rr[q]["U"]
            tol = CRIT["reference_factor"] * (Ur + ur) + CRIT["reference_floor_rel"] * max(1.0, abs(vr))
            ok = abs(v - vr) <= tol
            rworst = max(rworst, abs(v - vr) / tol)
            refcmp.append({"id": sid, "L": L, "quantity": q, "rust": v, "reference": vr, "U_reference": Ur, "U_rust": ur,
                           "tolerance": tol, "pass": ok})
            if not ok:
                rfail.append(f"{sid}:L={L}:{q}")
    # the L differences themselves
    dcmp = []
    for (N, tag, a4) in REF_STATES:
        sid = state_id(N, tag, a4)
        for q in ("E_KS", "HOMO", "LUMO", "int_p8", "int_n"):
            c3 = next(c for c in refcmp if c["id"] == sid and c["L"] == 3.0 and c["quantity"] == q)
            c4 = next(c for c in refcmp if c["id"] == sid and c["L"] == 4.0 and c["quantity"] == q)
            dcmp.append({"id": sid, "quantity": q, "rust_L4_minus_L3": c4["rust"] - c3["rust"],
                         "reference_L4_minus_L3": c4["reference"] - c3["reference"]})
    check("reference_solver_at_two_L",
          f"independent reference solver (reference/ks_fd.py, staggered finite differences, Richardson over 3 grids with the "
          f"step of the record) at L = 3 and L = 4 for {[state_id(*s) for s in REF_STATES]}: |Rust - reference| <= "
          f"{CRIT['reference_factor']:.0f} (U_reference + U_Rust) + {CRIT['reference_floor_rel']:.0e} max(1, |x|), "
          f"U_Rust = (16/15)|x(G = 600 L) - x(G = 300 L)|",
          not rfail, f"{len(refcmp)} comparisons, worst |diff|/tolerance {rworst:.3f}; failures: {rfail if rfail else 'none'}")

    # ---- report ---------------------------------------------------------------------------------
    rep = {
        "report": "Revision/kohn_sham/tip_convergence/tip-convergence.json",
        "producer": "Revision/kohn_sham/tip_convergence/tip_convergence.py",
        "question": "dependence of the recorded Kohn-Sham results on the chosen tip cutoff L (regular tip b(-L) = 0); "
                    "convergence as L grows",
        "howTheSolverGetsL": "L = 3 is a literal in base_phys() (solver/src/runs.rs) and G = 900 in Numerics::canonical() "
                             "(solver/src/model.rs); results/parameters.json is written by the solver, not read; --root only "
                             "locates ks-theory.json, gammas.json and the Mermin fixture. A scratch root with a modified "
                             "parameters.json is therefore ignored. This study builds a patched COPY (two one-line patches, "
                             "L and G from the environment) and verifies it at L = 3 against the committed record.",
        "committedSolverSourceSha256": committed_src,
        "patches": applied,
        "stepSizeRule": "G = 300 L (h = 1/300, the record's step); h-check G = 600 L at every L; U_h = (16/15)|x(600 L) - x(300 L)| (RK4 order 4)",
        "Lvalues": list(L_VALUES),
        "criteria": CRIT,
        "states": {"fixed": [s["id"] for s in base], "k0spectrum": k0spec,
                   "recalibrated": sorted({s["id"] for s in recspecs})},
        "couplings": {"recorded_lambda1": {str(N): lam1[N] for N in N_VALUES},
                      "recalibrated_lambda1_of_L": {str(N): {f16(L): lam1_L[(L, N)] for L in L_VALUES} for N in N_VALUES},
                      "strength_of_L": {str(N): {f16(L): max(strength[(L, N)]) for L in L_VALUES} for N in N_VALUES}},
        "k0Spectrum": {"rows": k0, "bulkEdge_odd_l0_of_L": bulk_edge,
                       "law": "even: eps = 0 (zero mode) and +-sqrt(m^2 + (l pi/L)^2); odd: +-sqrt(m^2 + p^2), tan(pL) = -p/m; "
                              "every non-zero level tends to +-m like (l pi)^2/(2 m L^2): algebraic, not exponential"},
        "zeroModeDensity": zm_rows,
        "firstOrderZeroModeEnergy": {
            "law": "free zero modes chi ~ e^{my}, proper density n = n(0) e^{(2m - 6H)y}; first-order interaction energy "
                   "E_int1 = 2 Vol_7 int e^{6Hy} lambda (-1/32) n^2 dy = -(2 lambda/Vol_7) e^{2L}/(1 - e^{-2L}) for m = H = 1 "
                   "(in general proportional to e^{(6H - 4m)L}: finite as L -> infinity only for m > 3H/2); tip potential "
                   "|v_v(-L)| = (lambda/16) n(-L) proportional to e^{(6H - 2m)L} = e^{4L}",
            "rows": fo},
        "analysis": analysis,
        "reference": {"jobs": [{"id": state_id(N, tag, a4), "L": L, "result": rr} for (N, tag, lam, a4, L), rr in zip(rjobs, rref)],
                      "comparisons": refcmp, "LDifferences": dcmp},
        "checks": checks,
        "summary": {"checks": len(checks), "pass": sum(c["result"] == "PASS" for c in checks)},
    }
    write_text(HERE / "tip-convergence.json", json.dumps(jclean(rep), indent=1, sort_keys=False) + "\n")
    make_figures(rep, allspecs, res_fixed, recspecs, res_rec)
    tlog("report and figures written")
    ok = all(c["result"] == "PASS" for c in checks)
    print("SUCCESS" if ok else "FAILURE")
    sys.exit(0 if ok else 1)


def make_figures(rep, allspecs, res_fixed, recspecs, res_rec):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    meta = {"Software": None}
    an = rep["analysis"]
    cols = {"lam0": "#2b6cb0", "lamp1": "#c05621", "lamm1": "#2f855a"}
    mk = {0.0: "o", 1.0: "s", 2.0: "^"}
    # Figure 1: |successive differences of E_KS| (fixed lambda)
    fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2), sharey=True)
    for ax, N in zip(axs, N_VALUES):
        for sid, ent in an["fixed"].items():
            if ent["N"] != N or ent["T"] > 0:
                continue
            q = ent["quantities"]["E_KS"]
            xs = [0.5 * (d["from"] + d["to"]) for d in q["differences"]]
            ys = [max(abs(d["diff"]), 1e-16) for d in q["differences"]]
            ax.semilogy(xs, ys, marker=mk[ent["a4"]], color=cols[ent["lambda_tag"]], lw=1.2,
                        label=f"{ent['lambda_tag']} a4={ent['a4']:g}")
            if q["first_failed_L"] is not None:
                ax.axvline(q["first_failed_L"], color=cols[ent["lambda_tag"]], ls=":", lw=0.8)
        ax.set_title(f"N = {N}: |E_KS(L+0.5) - E_KS(L)| (fixed lambda)", fontsize=9)
        ax.set_xlabel("midpoint of (L, L+0.5)")
        ax.grid(alpha=0.3)
    axs[0].set_ylabel("|difference| [m]")
    axs[-1].legend(fontsize=7, ncol=1, loc="lower left")
    fig.text(0.5, -0.02, "dotted vertical lines: first L at which the self-consistent iteration fails (fixed lambda)", ha="center", fontsize=8)
    fig.tight_layout()
    fig.savefig(HERE / "fig-differences-EKS.png", dpi=110, metadata=meta, bbox_inches="tight")
    plt.close(fig)
    # Figure 2: zero modes with a fixed lambda: E_KS vs first-order law, tip potential
    fo = rep["firstOrderZeroModeEnergy"]["rows"]
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
    Lf = np.linspace(3, 6, 61)
    for tag, sg in (("lamp1", 1), ("lamm1", -1)):
        rows = [r for r in fo if r["id"].startswith(f"N8_{tag}")]
        lam = rows[0]["lambda"]
        law = [abs(-(2.0 * lam / rep_vol7(rep)) * math.exp(2 * L) / (1 - math.exp(-2 * L))) for L in Lf]
        axs[0].semilogy(Lf, law, color=cols[tag], lw=1, ls="--", label=f"|first-order law| {tag}")
        tp = [abs(lam) / 16.0 * 8.0 / (rep_vol7(rep) * (1 - math.exp(-2 * L))) * math.exp(4 * L) for L in Lf]
        axs[1].semilogy(Lf, tp, color=cols[tag], lw=1, ls="--", label=f"first-order |v_v(-L)| {tag}")
        for a4 in SLICES_RUN:
            sid = state_id(8, tag, a4)
            sel = [(s["L"], x_) for s, x_ in zip(allspecs, res_fixed) if s["id"] == sid and s["refine"] == 1]
            ok_ = [(L, x_) for L, x_ in sel if x_["status"] == "ok"]
            off = {0.0: -0.06, 1.0: 0.0, 2.0: 0.06}[a4] * (1 if tag == "lamp1" else -1) * 0.5
            axs[0].semilogy([L + off for L, _ in ok_], [abs(x_["E_KS"]) for _, x_ in ok_], mk[a4], color=cols[tag], ms=5,
                            label=f"|E_KS| solved {tag} a4={a4:g}")
            axs[1].semilogy([L + off for L, _ in ok_], [x_["max_abs_v_v"] for _, x_ in ok_], mk[a4], color=cols[tag], ms=5,
                            label=f"self-consistent max|v_v| {tag} a4={a4:g}")
            for L, x_ in sel:
                if x_["status"] != "ok":
                    axs[0].plot([L + off], [2e-4], "x", color=cols[tag], ms=6)
    axs[0].set_title("N = 8 (brane zero modes), fixed lambda_1: |E_KS| vs tip cutoff" + chr(10) + "(x at the bottom: SCF fails at that L)", fontsize=9)
    axs[0].set_xlabel("L (points shifted slightly per slice)")
    axs[0].set_ylabel("|E_KS| [m]")
    axs[1].set_title("tip potential: first order grows like e^{4L}, self-consistent saturates", fontsize=9)
    axs[1].set_xlabel("L")
    axs[1].set_ylabel("[m]")
    for ax in axs:
        ax.grid(alpha=0.3)
        ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(HERE / "fig-zero-modes-fixed-lambda.png", dpi=110, metadata=meta, bbox_inches="tight")
    plt.close(fig)
    # Figure 3: free k = 0 spectrum vs L
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    for par_, lab, c in (("even", 1, "#2b6cb0"), ("even", 2, "#2b6cb0"), ("odd", 0, "#c05621"), ("odd", 1, "#c05621")):
        ax.plot(Lf, [analytic_k0(L, par_, lab) for L in Lf], color=c, lw=1, ls="-" if par_ == "even" else "--")
        pts = [(r["L"], r["eps"]) for r in rep["k0Spectrum"]["rows"] if r["parity"] == par_ and r["label"] == lab and r["j"] == 1]
        ax.plot([p[0] for p in pts], [p[1] for p in pts], "o", color=c, ms=4, label=f"{par_} l={lab}")
    ax.axhline(1.0, color="k", lw=0.6)
    hom = an["fixed"]["N688_lam0_a00"]["quantities"]["HOMO"]
    hp = [(L, v) for L, v in zip(hom["L"], hom["value"]) if v is not None]
    ax.plot([p[0] for p in hp], [p[1] for p in hp], "k^", ms=5, label="HOMO of N = 688, a4 = 0 (free)")
    ax.set_xlabel("L")
    ax.set_ylabel("eps [m]")
    ax.set_title("free k = 0 levels: exact law (lines) and solver (points)", fontsize=9)
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(HERE / "fig-k0-spectrum.png", dpi=110, metadata=meta, bbox_inches="tight")
    plt.close(fig)
    # Figure 4: recalibrated protocol: E_int vs L
    fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2))
    for ax, N in zip(axs, N_VALUES):
        for sid, ent in an["recalibrated"].items():
            if ent["N"] != N:
                continue
            q = ent["quantities"]["E_KS"]
            free = an["fixed"][f"N{N}_lam0_a{int(round(10 * ent['a4'])):02d}"]["quantities"]["E_KS"]
            xs = [L for L, v, f in zip(q["L"], q["value"], free["value"]) if v is not None and f is not None]
            ys = [abs(v - f) for v, f in zip(q["value"], free["value"]) if v is not None and f is not None]
            ax.semilogy(xs, [max(y, 1e-16) for y in ys], marker=mk[ent["a4"]], color=cols[ent["lambda_tag"]], lw=1.2,
                        label=f"{ent['lambda_tag']} a4={ent['a4']:g}")
        ax.set_title(f"N = {N}: |E_KS(lambda_1(L)) - E_KS(0)|, recalibrated lambda_1(L)", fontsize=9)
        ax.set_xlabel("L")
        ax.grid(alpha=0.3)
    axs[0].set_ylabel("[m]")
    axs[-1].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(HERE / "fig-recalibrated-interaction.png", dpi=110, metadata=meta, bbox_inches="tight")
    plt.close(fig)


def rep_vol7(rep):
    return json.loads((RESULTS / "parameters.json").read_text(encoding="utf-8"))["physics"]["Vol7"]


if __name__ == "__main__":
    main()
