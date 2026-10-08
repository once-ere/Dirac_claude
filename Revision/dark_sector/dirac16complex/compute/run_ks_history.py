#!/usr/bin/env python3
"""Revision/dark_sector/dirac16complex/compute/run_ks_history.py - the Kohn-Sham gas of dirac16complex along the
deflating history on a DENSE grid of slices, computed by the Revision Rust Kohn-Sham solver
(Revision/kohn_sham/solver, command `single`; read-only use of that code, outputs written here).

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the three exponentially
DEFLATING extra times (scale factor e^{-a4} sin^{1/6} z, a4 increasing); x8 = hidden direction.

The committed Kohn-Sham record has five slices a4,0 in {0, 0.5, 1, 1.5, 2}; the CPL tangent needs d w/d a4, so
this driver solves the SAME states (same N, the same calibrated lambda values of
Revision/kohn_sham/results/parameters.json, T = 0, canonical numerics, H = m = 1, L = 3, tip theta = 0) at
a4,0 = 0, 0.05, ..., 2 (41 slices).  The range is the solver's validated range; it is not extended (outside it the
aufbau occupation can change, see the checks below).

Writes outputs/ks-history-dense.csv (one row per state; floats as shortest round-trip repr) and
reports/ks-history-run.json (checks: every run succeeded; the five committed slices are reproduced bit for bit;
the occupied label set is the same at every slice of a series, so that the instantaneous ground states ARE the
adiabatically continued state with fixed occupations, to which the conservation identity dE/da4 = -3 (P3 - Pt)
applies; y-conservation residuals).  Deterministic (the work directory does not enter the outputs).

Usage (repository root): python Revision/dark_sector/dirac16complex/compute/run_ks_history.py [--solver PATH]
                         [--work DIR] [--jobs N]
"""

import argparse
import concurrent.futures as cf
import csv
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
OWN = HERE.parent
REV = OWN.parent.parent
KS = REV / "kohn_sham"
OUT_CSV = OWN / "outputs" / "ks-history-dense.csv"
OUT_REPORT = OWN / "reports" / "ks-history-run.json"
SLICES = [round(0.05 * i, 10) for i in range(41)]
COMMITTED = [0.0, 0.5, 1.0, 1.5, 2.0]
CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})


def default_solver():
    exe = "revision_ks_solver.exe" if os.name == "nt" else "revision_ks_solver"
    return KS / "solver" / "target" / "release" / exe


def lambda_table():
    par = json.loads((KS / "results" / "parameters.json").read_text(encoding="utf-8"))
    table = []
    for entry in par["couplingCalibration"]["values"]:
        n = int(entry["N"])
        table.append((n, "lam0", 0.0))
        table.append((n, "lamp1", entry["lambda1"]))
        table.append((n, "lamm1", -entry["lambda1"]))
        table.append((n, "lamp2", entry["lambda2"]))
        table.append((n, "lamm2", -entry["lambda2"]))
    return table


def run_one(solver, work, n, tag, lam, a4):
    rid = f"N{n}_{tag}_a{int(round(a4 * 100)):03d}"
    out = Path(work) / f"{rid}.json"
    cmd = [str(solver), "single", "--m", "1", "--lambda", repr(lam), "--a4", repr(a4), "--N", str(n),
           "--out", str(out)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    ok = proc.returncode == 0 and out.exists() and proc.stdout.strip().endswith("SUCCESS")
    if not ok:
        return rid, n, tag, lam, a4, None
    return rid, n, tag, lam, a4, json.loads(out.read_text(encoding="utf-8"))


def occupied_signature(levels):
    occ = sorted((int(l[0]), int(l[1]), str(l[2]), int(l[3]), repr(float(l[6]))) for l in levels if float(l[6]) > 0)
    return hashlib.sha256(json.dumps(occ).encode()).hexdigest()[:16], len(occ)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solver", default=str(default_solver()))
    ap.add_argument("--work", default=None)
    ap.add_argument("--jobs", type=int, default=max(1, min(12, (os.cpu_count() or 2) - 2)))
    args = ap.parse_args()
    solver = Path(args.solver)
    if not solver.exists():
        print(f"ERROR  solver binary not found: {solver} (build: cargo build --release --manifest-path "
              f"Revision/kohn_sham/solver/Cargo.toml)")
        return 1
    work = args.work or tempfile.mkdtemp(prefix="ks-history-")
    Path(work).mkdir(parents=True, exist_ok=True)
    tasks = [(n, tag, lam, a4) for (n, tag, lam) in lambda_table() for a4 in SLICES]
    results = {}
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = [ex.submit(run_one, solver, work, *t) for t in tasks]
        for f in cf.as_completed(futs):
            rid, n, tag, lam, a4, d = f.result()
            results[rid] = (n, tag, lam, a4, d)
    failed = sorted(r for r, v in results.items() if v[4] is None)
    check("all_runs_succeeded", not failed and len(results) == len(tasks),
          f"{len(tasks)} runs (15 series x 41 slices), failed: {failed[:10]}")
    if failed:
        write(results, [])
        return 1

    rows = []
    order = sorted(results, key=lambda r: (results[r][0], ["lam0", "lamp1", "lamm1", "lamp2", "lamm2"].index(results[r][1]),
                                           results[r][3]))
    for rid in order:
        n, tag, lam, a4, d = results[rid]
        emt = d["emtIntegrals_2Vol7_int_e6Hy"]
        sig, nocc = occupied_signature(d["levels_n2_j_parity_label_eps_deg_f"])
        rows.append({"id": rid, "N": n, "lambda_tag": tag, "lambda": lam, "a4": a4, "E_KS": d["E_KS"],
                     "int_rho": emt["rho"], "int_p3": emt["p3"], "int_p_t": emt["p_t"], "int_p8": emt["p8"],
                     "int_n": emt["n"], "iterations": d["iterations"], "residual": d["residual"],
                     "fermi_level": d["mu_or_fermi_level"], "ycons_integrated_rel": d["yConservationIntegratedRel"],
                     "ycons_pointwise_rel": d["yConservationPointwiseRel"], "occupied_signature": sig,
                     "occupied_labels": nocc})

    # reproduction of the committed five slices (Revision/kohn_sham/results/ground/emt-integrals.csv)
    committed = {}
    with open(KS / "results" / "ground" / "emt-integrals.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            committed[r["id"]] = r
    worst, compared = 0.0, 0
    for r in rows:
        if r["a4"] not in COMMITTED:
            continue
        cid = f"N{r['N']}_{r['lambda_tag']}_a{int(round(r['a4'] * 10)):02d}"
        c = committed.get(cid)
        if c is None:
            worst = float("inf")
            continue
        for mine, theirs in (("int_rho", "int_rho"), ("int_p3", "int_p3"), ("int_p_t", "int_p_t"), ("int_p8", "int_p8")):
            a, b = float(r[mine]), float(c[theirs])
            worst = max(worst, abs(a - b) / max(1.0, abs(b)))
            compared += 1
    check("committed_slices_reproduced", compared == 15 * 5 * 4 and worst <= 1e-13,
          f"{compared} integrals of the 75 committed states compared with Revision/kohn_sham/results/ground/"
          f"emt-integrals.csv: max relative deviation {worst:.3e}")

    # fixed occupations along every series
    series = {}
    for r in rows:
        series.setdefault((r["N"], r["lambda_tag"]), []).append(r)
    changed = [f"N{k[0]}_{k[1]}" for k, v in series.items() if len({x["occupied_signature"] for x in v}) != 1]
    check("occupied_labels_fixed_along_history", not changed,
          f"occupied (n2, j, parity, level, f) set identical at all 41 slices for {len(series) - len(changed)} of "
          f"{len(series)} series; changed: {changed}")
    yc = max(max(r["ycons_integrated_rel"], r["ycons_pointwise_rel"]) for r in rows)
    check("y_conservation_every_state", yc <= 1e-6,
          f"p8_y + 6 H p8 = 3 H (p3 + p_t): max relative residual over {len(rows)} states {yc:.3e} (solver's own)")
    nmax = max(abs(r["int_n"] - r["N"]) / r["N"] for r in rows)
    check("particle_number_every_state", nmax <= 1e-12, f"max |int n - N|/N = {nmax:.3e}")
    write(results, rows)
    return 0 if all(c["verdict"] == "PASS" for c in CHECKS) else 1


def write(results, rows):
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    if rows:
        cols = list(rows[0].keys())
        with open(OUT_CSV, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(",".join(cols) + "\n")
            for r in rows:
                fh.write(",".join(repr(r[c]) if isinstance(r[c], float) else str(r[c]) for c in cols) + "\n")
    fails = [c for c in CHECKS if c["verdict"] != "PASS"]
    rep = {"producer": "Revision/dark_sector/dirac16complex/compute/run_ks_history.py",
           "solver": "Revision/kohn_sham/solver (command single), canonical numerics, T = 0, H = m = 1, L = 3, theta = 0",
           "slices": SLICES, "history": "PRESCRIBED BACKGROUND a4 = A H x4 (Revision/kohn_sham/results/parameters.json "
           "conventions.history): the Kohn-Sham gas is a test field without back-reaction",
           "checks": CHECKS, "summary": {"total": len(CHECKS), "pass": len(CHECKS) - len(fails), "fail": len(fails)}}
    with open(OUT_REPORT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(rep, indent=1) + "\n")
    for c in CHECKS:
        print(f"{c['verdict']} - {c['name']}: {c['detail']}")


if __name__ == "__main__":
    sys.exit(main())
