#!/usr/bin/env python3
"""Revision/dark_sector/dirac16complex/compute/run_ks_history.py - the Kohn-Sham gas of dirac16complex along the
history of the corrected primordial metric of 2026-10-16, on a DENSE grid of slices, computed by the Revision Rust
Kohn-Sham solver (Revision/kohn_sham/solver, command `single`; read-only use of that code, outputs written here).

The metric (Revision/SPEC.md section 1, version 2): g = diag(e^{-2a4} b4 cot^2 z, e^{2a4} (x3), -1,
-e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real, in the author's coordinates {x0, ..., x7}: x0 = hidden direction,
x1, x2, x3 = 3-space (scale factor e^{a4}), x4 = time, x5, x6, x7 = the three extra times (scale factor
e^{-a4} b4^{1/2} (sin^2 z)^{1/12}).  b4 is a FUNCTION of x4.  In the Kohn-Sham coordinate y = ln|sin z|/(6H) the hidden
direction carries the scale f = e^{-a4} b4^{1/2}, the extra times f e^{Hy}.

The history.  The record's history a4 = H x4, b4 = e^{(4/3) H x4} (beta = 4/3, b4(0) = 1; Revision/kohn_sham/ks-theory.json
adiabaticity.historyBeta), a PRESCRIBED background (test field, no back-reaction): with the author's weights it needs
the source of Revision/field_equations_a4/a4-equations.json (exponentialHistory.authorWeights), which the Kohn-Sham gas
does not supply (Revision/field_equations_a4/reports/ks-source-conditions.json).  On it f = e^{-a4/3} and the momentum
weight kappa = e^{-a4}.

The states.  The slice Hamiltonian is h_j = j[-(i/f) sigma1 d_y + M sigma2 + kappa k sigma3] + v (ks-theory.json
blockEquation): b4 enters through f, and through the proper 7-volume of the cell, Vol_7(a4) = ell^3 v_t e^{-a4} b4^2 =
ell^3 v_t e^{(5/3) a4}.  The record's coupling is lambda_hat = lambda b4(0)^{-2} (the calibrated couplings of
Revision/kohn_sham/results/parameters.json, the same at every slice).  This script runs `single --lambda lambda_hat
--a4 a4`.  Because a state depends on the coupling and the cell volume only through lambda/Vol (ks-theory.json
densities.couplingVolumeScaling), the same state is the one of the coordinate cell ell^3 v_t (same f and kappa) at
    lambda_eff(a4) = lambda_hat e^{-(5/3) a4};
the check lambda_eff_form_agrees solves that form too (`single --coordinate-cell --lambda lambda_eff`) at the committed
slices a4 > 0 and compares.  Same N (8, N_mid, N_large of the record), T = 0, canonical numerics, H = m = 1, L = 3,
tip theta = 0, a4 = 0, 0.05, ..., 2 (41 slices, the solver's validated range; it is not extended: outside it the
aufbau occupation can change, see the checks below).

Writes outputs/ks-history-dense.csv (one row per state; floats as shortest round-trip repr) and
reports/ks-history-run.json (checks: every run succeeded; at the five committed slices every one of the 15 series
equals the committed Kohn-Sham record; the lambda = 0 series are exact fold-band gases at every slice; the cell volume
of every run is ell^3 v_t e^{(5/3) a4}; the lambda_eff form agrees; the occupied label set is the same at every slice of
a series, so that the instantaneous ground states ARE the adiabatically continued state with fixed occupations, to
which the conservation identity dE/da4 = -3 P3 + P_t + P0/3 (beta = 4/3) applies; y-conservation residuals).
Deterministic (the work directory does not enter the outputs).

Usage (repository root): python Revision/dark_sector/dirac16complex/compute/run_ks_history.py [--solver PATH]
                         [--work DIR] [--jobs N] [--part i/n]
In parts, each within a time limit: --work DIR --part i/n for i = 1..n computes a fixed part of the 663 `single` runs
(615 of the history and 48 of the coordinate-cell form) into DIR (a run whose output is already in DIR is not repeated;
the runs are deterministic) and writes no outputs; then --work DIR without --part computes any run still missing and
writes the outputs.  The work directory must belong to the same solver binary (DIR/solver-sha256.txt).
"""

import argparse
import concurrent.futures as cf
import csv
import hashlib
import json
import math
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
BETA = 4.0 / 3.0                     # d ln b4/d a4 on the record's history (ks-theory.json adiabaticity.historyBeta)
CHECKS = []


def lambda_eff(lam_hat, a4):
    """the coupling of the coordinate-cell form at slice a4: lambda_hat Vol_7(0)/Vol_7(a4) = lambda_hat e^{-(2 beta - 1) a4}
    = lambda_hat e^{-(5/3) a4}"""
    return lam_hat * math.exp(-(2.0 * BETA - 1.0) * a4)


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


def run_cost(t):
    """rough relative cost of a run (only the balance of the parts depends on it)"""
    n, tag, lam, a4 = t[:4]
    return (1.0 + n / 500.0) * (1.0 if lam == 0.0 else 4.0 if tag in ("lamp1", "lamm1") else 10.0) * (1.0 + a4)


def part_of(tasks, part):
    i, n = part
    order = sorted(range(len(tasks)), key=lambda k: (-run_cost(tasks[k]), k))
    load = [0.0] * n
    mine = []
    for k in order:
        b = min(range(n), key=lambda j: (load[j], j))
        load[b] += run_cost(tasks[k])
        if b == i - 1:
            mine.append(tasks[k])
    return mine


def run_one(solver, work, n, tag, lam, a4, form="hat"):
    """form "hat": the record's form (lambda_hat, Vol_7(a4) = ell^3 v_t e^{(5/3) a4}); form "eff": the coordinate cell at
    lambda_eff = lambda_hat e^{-(5/3) a4} (`--coordinate-cell`: Vol_7 = ell^3 v_t, the same f and kappa)"""
    rid = f"N{n}_{tag}_a{int(round(a4 * 100)):03d}"
    out = Path(work) / (f"{rid}.json" if form == "hat" else f"{rid}_eff.json")
    if out.exists():
        # a finished run of an earlier invocation (a part): written only after the solver ended with SUCCESS
        return rid, n, tag, lam, a4, json.loads(out.read_text(encoding="utf-8"))
    tmp = Path(work) / (out.name + ".tmp.json")
    if form == "hat":
        cmd = [str(solver), "single", "--m", "1", "--lambda", repr(lam), "--a4", repr(a4), "--N", str(n),
               "--out", str(out)]
    else:
        cmd = [str(solver), "single", "--m", "1", "--coordinate-cell", "--lambda", repr(lambda_eff(lam, a4)), "--a4", repr(a4),
               "--N", str(n), "--out", str(out)]
    cmd[cmd.index("--out") + 1] = str(tmp)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    ok = proc.returncode == 0 and tmp.exists() and proc.stdout.strip().endswith("SUCCESS")
    if not ok:
        return rid, n, tag, lam, a4, None
    os.replace(tmp, out)
    return rid, n, tag, lam, a4, json.loads(out.read_text(encoding="utf-8"))


def occupied_signature(levels):
    occ = sorted((int(l[0]), int(l[1]), str(l[2]), int(l[3]), repr(float(l[6]))) for l in levels if float(l[6]) > 0)
    return hashlib.sha256(json.dumps(occ).encode()).hexdigest()[:16], len(occ)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solver", default=str(default_solver()))
    ap.add_argument("--work", default=None)
    ap.add_argument("--jobs", type=int, default=max(1, min(12, (os.cpu_count() or 2) - 2)))
    ap.add_argument("--part", default=None, help="i/n (needs --work): only part i of n of the runs, no outputs")
    args = ap.parse_args()
    solver = Path(args.solver)
    if not solver.exists():
        print(f"ERROR  solver binary not found: {solver} (build: cargo build --release --manifest-path "
              f"Revision/kohn_sham/solver/Cargo.toml)")
        return 1
    if args.part and not args.work:
        print("ERROR  --part needs --work DIR")
        return 1
    work = args.work or tempfile.mkdtemp(prefix="ks-history-")
    Path(work).mkdir(parents=True, exist_ok=True)
    # the work directory belongs to one solver binary (its runs are reused)
    sha = hashlib.sha256(Path(solver).read_bytes()).hexdigest()
    stamp = Path(work) / "solver-sha256.txt"
    if stamp.exists() and stamp.read_text(encoding="utf-8").strip() != sha:
        print(f"ERROR  {work} holds runs of another solver binary; use a fresh work directory")
        return 1
    stamp.write_text(sha + "\n", encoding="utf-8")
    tasks = [(n, tag, lam, a4) for (n, tag, lam) in lambda_table() for a4 in SLICES]
    eff_tasks = [(n, tag, lam, a4) for (n, tag, lam) in lambda_table() if lam != 0.0 for a4 in COMMITTED if a4 > 0.0]
    if args.part:
        i_, n_ = (int(x) for x in args.part.split("/"))
        allt = [t + ("hat",) for t in tasks] + [t + ("eff",) for t in eff_tasks]
        mine = part_of(allt, (i_, n_))
        with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
            res = list(ex.map(lambda t: run_one(solver, work, *t[:4], form=t[4]), mine))
        bad = [r[0] for r in res if r[5] is None]
        print(f"part {i_}/{n_}: {len(mine)} runs, failed: {bad}")
        print("PART DONE" if not bad else "PART FAILED")
        return 0 if not bad else 1
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
    vol0 = (2.0 * math.pi / 0.25) ** 3 * 1.0          # ell^3 v_t of the record (dk = 0.25, v_t = 1)
    order = sorted(results, key=lambda r: (results[r][0], ["lam0", "lamp1", "lamm1", "lamp2", "lamm2"].index(results[r][1]),
                                           results[r][3]))
    for rid in order:
        n, tag, lam, a4, d = results[rid]
        emt = d["emtIntegrals_2Vol7_int_e3Hy"]
        sig, nocc = occupied_signature(d["levels_n2_j_parity_label_eps_deg_f"])
        rows.append({"id": rid, "N": n, "lambda_tag": tag, "lambda": lam, "a4": a4,
                     "b4_over_b4_0": math.exp(BETA * a4), "lambda_eff": lambda_eff(lam, a4),
                     "beta": d["parameters"]["beta"], "Vol7": d["parameters"]["Vol7"], "E_KS": d["E_KS"],
                     "int_rho": emt["rho"], "int_p3": emt["p3"], "int_p_t": emt["p_t"], "int_p0": emt["p0"],
                     "int_n": emt["n"], "iterations": d["iterations"], "residual": d["residual"],
                     "fermi_level": d["mu_or_fermi_level"], "ycons_integrated_rel": d["yConservationIntegratedRel"],
                     "ycons_pointwise_rel": d["yConservationPointwiseRel"], "occupied_signature": sig,
                     "occupied_labels": nocc})

    # comparison with the committed Kohn-Sham record (Revision/kohn_sham/results/ground/emt-integrals.csv): the
    # same history, so every series must equal it at the five committed slices
    committed = {}
    with open(KS / "results" / "ground" / "emt-integrals.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            committed[r["id"]] = r

    def compare(select):
        worst, compared = 0.0, 0
        for r in rows:
            if r["a4"] not in COMMITTED or not select(r):
                continue
            cid = f"N{r['N']}_{r['lambda_tag']}_a{int(round(r['a4'] * 10)):02d}"
            c = committed.get(cid)
            if c is None:
                return float("inf"), compared
            for mine in ("int_rho", "int_p3", "int_p_t", "int_p0"):
                a, b = float(r[mine]), float(c[mine])
                worst = max(worst, abs(a - b) / max(1.0, abs(b)))
                compared += 1
        return worst, compared

    wall, nall = compare(lambda r: True)
    check("committed_slices_equal_committed_record", nall == 15 * 5 * 4 and wall <= 1e-13,
          f"{nall} integrals (E, P3, Pt, P0) of the 15 series at the five committed slices a4 = 0, 0.5, ..., 2 compared "
          f"with Revision/kohn_sham/results/ground/emt-integrals.csv (the same history): max relative deviation "
          f"{wall:.3e}")
    # lambda = 0: every occupied orbital lies on the fold band chi = (e^{f M y}, 0), eps = e^{-a4} |k| (or is a k = 0
    # zero mode), so the series is exact at every slice: E(a4) = E(0) e^{-a4}, P3 = E/3, P0 = Pt = 0
    l0dev, l0n = 0.0, 0
    for (n_, tag_), _ in [((r["N"], r["lambda_tag"]), None) for r in rows if r["lambda_tag"] == "lam0" and r["a4"] == 0.0]:
        e0 = next(r for r in rows if r["N"] == n_ and r["lambda_tag"] == tag_ and r["a4"] == 0.0)["E_KS"]
        for r in rows:
            if r["N"] != n_ or r["lambda_tag"] != tag_:
                continue
            sc = max(1.0, abs(r["int_rho"]))
            l0dev = max(l0dev, abs(r["E_KS"] - e0 * math.exp(-r["a4"])) / max(1.0, abs(e0)),
                        abs(r["int_p3"] - r["int_rho"] / 3.0) / sc, abs(r["int_p0"]) / sc, abs(r["int_p_t"]) / sc,
                        abs(r["int_rho"] - r["E_KS"]) / sc)
            l0n += 1
    check("lambda0_series_exact_fold_band", l0n == 3 * 41 and l0dev <= 1e-12,
          f"lambda = 0, {l0n} states (three series x 41 slices): E_KS(a4) = E_KS(0) e^(-a4), int p3 = int rho/3, int p0 = "
          f"int p_t = 0 and int rho = E_KS to {l0dev:.3e} (relative to max(1, |x|)): every occupied orbital is the fold-band "
          f"orbital (e^(f M y), 0) with eps = e^(-a4) |k| or a k = 0 zero mode (ks-theory.json blockEquation; the hidden "
          f"kinetic pressure vanishes on it), so the free gas redshifts exactly like e^(-a4) with the pressure of radiation "
          f"in 3-space and no hidden or extra-time pressure")
    vol_dev = max(abs(r["Vol7"] / (vol0 * math.exp((2.0 * BETA - 1.0) * r["a4"])) - 1.0) for r in rows)
    check("cell_volume_follows_b4", vol_dev <= 1e-14,
          f"every run used Vol_7(a4) = ell^3 v_t e^(-a4) b4^2 = ell^3 v_t e^((2 beta - 1) a4) = ell^3 v_t e^((5/3) a4) (beta = "
          f"{rows[0]['beta']!r} from ks-theory.json, b4(0) = 1): max relative deviation {vol_dev:.3e}, so the effective "
          f"coupling lambda_hat/Vol_7 falls like e^(-(5/3) a4)")
    # the coordinate-cell form at lambda_eff (ks-theory.json densities.couplingVolumeScaling), every series with
    # lambda != 0 at the committed slices a4 > 0
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        eff = list(ex.map(lambda t: run_one(solver, work, *t, form="eff"), eff_tasks))
    byid = {r["id"]: r for r in rows}
    worst_eff, n_eff, bad_eff = 0.0, 0, []
    for rid, n, tag, lam, a4, d in eff:
        if d is None:
            bad_eff.append(rid)
            continue
        r = byid[rid]
        e2 = d["emtIntegrals_2Vol7_int_e3Hy"]
        for mine, k in (("int_rho", "rho"), ("int_p3", "p3"), ("int_p_t", "p_t"), ("int_p0", "p0")):
            worst_eff = max(worst_eff, abs(r[mine] - e2[k]) / max(1.0, abs(r[mine])))
            n_eff += 1
        worst_eff = max(worst_eff, abs(r["E_KS"] - d["E_KS"]) / max(1.0, abs(r["E_KS"])))
    check("lambda_eff_form_agrees", not bad_eff and n_eff == len(eff_tasks) * 4 and worst_eff <= 1e-12,
          f"{len(eff_tasks)} states (12 interacting series x 4 committed slices a4 > 0) solved again in the coordinate-cell "
          f"form `single --coordinate-cell --lambda lambda_eff`, lambda_eff = lambda_hat e^(-(5/3) a4) (the same f and kappa): "
          f"E_KS and the integrals E, P3, Pt, P0 agree with the record's form to {worst_eff:.3e} (relative to max(1, |x|)); "
          f"failed runs: {bad_eff}")

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
          f"p0_y + 3 H (p0 - p_t) = 0: max relative residual over {len(rows)} states {yc:.3e} (solver's own)")
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
           "slices": SLICES, "metric": "the corrected primordial metric of 2026-10-16 (version 2; SPEC section 1)",
           "history": "PRESCRIBED BACKGROUND a4 = H x4 and b4(x4) = e^((4/3) H x4) (b4(0) = 1; ks-theory.json "
           "adiabaticity.historyBeta): the Kohn-Sham gas is a test field without back-reaction",
           "coupling": "the solver runs at lambda_hat = lambda b4(0)^(-2) (the calibrated couplings of "
                       "Revision/kohn_sham/results/parameters.json) with the cell volume Vol_7(a4) = ell^3 v_t e^((5/3) a4) "
                       "and the hidden scale f = e^(-a4/3) (ks-theory.json densities, blockEquation); equivalently the "
                       "coordinate cell at lambda_eff = lambda_hat e^(-(5/3) a4) with the same f and kappa (check "
                       "lambda_eff_form_agrees)",
           "beta": "d ln b4/d a4 = 4/3",
           "checks": CHECKS, "summary": {"total": len(CHECKS), "pass": len(CHECKS) - len(fails), "fail": len(fails)}}
    with open(OUT_REPORT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(rep, indent=1) + "\n")
    for c in CHECKS:
        print(f"{c['verdict']} - {c['name']}: {c['detail']}")


if __name__ == "__main__":
    sys.exit(main())
