#!/usr/bin/env python3
"""40-digit roots of the Mermin condition for the Revision Kohn-Sham solver (mpmath).

Revision code only (Python standard library and mpmath; nothing of the old stages).

For every thermal state of the canonical matrix (N, the couplings lambda in {0, +-lambda_1}, the slices
a4,0 and the temperatures T of Revision/kohn_sham/results/parameters.json) the Rust binary is run as

    revision_ks_solver single --m 1 --lambda L --a4 A --N N --T T --margin 0.2+2sigma --mermin-levels FILE

with the canonical numerics and the label-set margin of the canonical matrix.  `--mermin-levels` writes the
final Kohn-Sham levels and mu of the state as shortest round-trip decimals, so the doubles read here are
exactly the solver's doubles.  On these levels the root of

    sum_i g_i / (1 + exp((eps_i - mu)/T)) = N

is computed with mpmath at 40 significant digits (bracketed Newton started at the solver's mu) and checked at
50 digits.  The direct sum is harmless at 40 digits: its rounding fixes mu to 1e-40 N/(dN/dmu) <= 1e-33 here.

For each state the tool records |mu_solver - root| against the rounding bound of the solver's well-conditioned
residual (solver/src/mermin.rs), eps_mach [(n + 2 + L) (P + Hl + |d|)/(dN/dmu) + 3 <|eps - mu|> +
T (ln g_max + 3) + 2 |mu|] (n levels, split S = {eps < root}, <.> the mean weighted with g f (1 - f), g_max the
largest degeneracy, L = max(|ln(P + d-)|, |ln(Hl + d+)|)), and the conditioning bound of the former direct count,
eps_mach [(n + 2) N/(dN/dmu) + 3 <|eps - mu|> + T (ln g_max + 3) + 2 |mu|].  The bounds are evaluated here at the
40-digit root, independently of the solver's own evaluation.

Outputs (deterministic, LF):
  Revision/kohn_sham/solver/tools/mermin-roots-40digit.json   fixture: the --fixture-count states with the
        largest direct-count bound (exact levels, mu of the run, 40-digit root); read by the Rust unit test
        mermin::tests::forty_digit_roots and by the solver check thermo_mu_vs_40digit_roots
  Revision/kohn_sham/reports/ks-rust-mermin-roots.json         every state and every check (name, verdict, detail)

Usage (from the repository root, after `cargo build --release` in Revision/kohn_sham/solver):
  python Revision/kohn_sham/solver/tools/mermin_roots_mp.py --work <scratch>/mermin-roots [--jobs N]
The check `single_reproduces_committed_matrix` compares the solver's mu with the committed
results/thermo/thermodynamics.csv, so the tool is run after the canonical matrix.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
SOLVER = HERE.parent
KS = SOLVER.parent
ROOT = KS.parent.parent
BIN = SOLVER / "target" / "release" / ("revision_ks_solver.exe" if os.name == "nt" else "revision_ks_solver")
PARAMS = KS / "results" / "parameters.json"
THERMO = KS / "results" / "thermo" / "thermodynamics.csv"
FIXTURE = HERE / "mermin-roots-40digit.json"
REPORT = KS / "reports" / "ks-rust-mermin-roots.json"

EPS_MACH = 2.0 ** -52
DIGITS = 40
CHECK_DIGITS = 50
SIGMA = {"lam0": 0.0, "lamp1": 0.1, "lamm1": 0.1}


def states_from_parameters():
    p = json.loads(PARAMS.read_text(encoding="utf-8"))
    slices = p["physics"]["slicesA4"]
    temps = p["physics"]["temperatures"]
    out = []
    for c in p["couplingCalibration"]["values"]:
        n, l1 = c["N"], c["lambda1"]
        for tag, lam in (("lam0", 0.0), ("lamp1", l1), ("lamm1", -l1)):
            for a4 in slices:
                for t in temps:
                    sid = "N%d_%s_a%02d_T%d" % (int(n), tag, int(round(a4 * 10)), int(round(t * 1000)))
                    out.append({"id": sid, "N": n, "tag": tag, "lambda": lam, "a4": a4, "T": t,
                                "margin": 0.2 + 2.0 * SIGMA[tag]})
    out.sort(key=lambda s: s["id"])
    return out


def run_single(spec, work: Path):
    lv = work / (spec["id"] + "-levels.json")
    out = work / (spec["id"] + ".json")
    cmd = [str(BIN), "single", "--m", "1", "--lambda", repr(spec["lambda"]), "--a4", repr(spec["a4"]),
           "--N", repr(spec["N"]), "--T", repr(spec["T"]), "--margin", repr(spec["margin"]),
           "--out", str(out), "--mermin-levels", str(lv)]
    r = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    if r.returncode != 0 or not lv.exists():
        return spec["id"], None, (r.stderr or "")[-400:]
    return spec["id"], json.loads(lv.read_text(encoding="utf-8")), ""


def mermin_root(eps, deg, n, t, mu0, dps):
    """Root of sum g f = N at `dps` digits (bracketed Newton from mu0) and dN/dmu there."""
    with mp.workdps(dps):
        E = [mp.mpf(e) for e in eps]
        G = [mp.mpf(g) for g in deg]
        N = mp.mpf(n)
        T = mp.mpf(t)

        def F(mu):
            s = mp.mpf(0)
            ds = mp.mpf(0)
            for e, g in zip(E, G):
                f = 1 / (1 + mp.exp((e - mu) / T))
                s += g * f
                ds += g * f * (1 - f)
            return s - N, ds / T

        mu = mp.mpf(mu0)
        w = mp.mpf("1e-9")
        while True:
            lo, hi = mu - w, mu + w
            if F(lo)[0] < 0 < F(hi)[0]:
                break
            w *= 10
            if w > 100:
                raise RuntimeError("no bracket")
        tol = mp.mpf(10) ** (-(dps + 3))
        for _ in range(200):
            f, df = F(mu)
            if f == 0:
                break
            if f < 0:
                lo = mu
            else:
                hi = mu
            nxt = mu - f / df
            if not (lo < nxt < hi):
                nxt = (lo + hi) / 2
            if abs(nxt - mu) <= tol * max(1, abs(mu)):
                mu = nxt
                break
            mu = nxt
        return mu, F(mu)[1]


def analyse(job):
    sid, lv = job
    n = float(lv["N"])
    t = float(lv["T"])
    mu_run = float(lv["mu"])
    eps = [float(e) for e, _ in lv["levels_eps_deg"]]
    deg = [float(g) for _, g in lv["levels_eps_deg"]]
    root, dn = mermin_root(eps, deg, n, t, mu_run, DIGITS)
    root_chk, _ = mermin_root(eps, deg, n, t, mu_run, CHECK_DIGITS)
    with mp.workdps(CHECK_DIGITS):
        prec_dev = abs(root_chk - root) / max(1, abs(root_chk))
    with mp.workdps(DIGITS):
        # magnitude of the well-conditioned residual's terms for S = {eps < root}
        T = mp.mpf(t)
        P = Hl = mp.mpf(0)
        gs = mp.mpf(0)
        w = wx = mp.mpf(0)
        gmax = max(mp.mpf(g) for g in deg)
        for e, g in zip(eps, deg):
            x = (mp.mpf(e) - root) / T
            f = 1 / (1 + mp.exp(x))
            wi = g * f * (1 - f)
            w += wi
            wx += wi * abs(mp.mpf(e) - root)
            if mp.mpf(e) < root:
                Hl += g / (1 + mp.exp(-x))
                gs += g
            else:
                P += g / (1 + mp.exp(x))
        d = mp.mpf(n) - gs
        mag = P + Hl + abs(d)
        # the two sides of the balance, A = P + d- and B = Hl + d+ (equal at the root)
        big_l = max(abs(mp.log(P + max(-d, 0))), abs(mp.log(Hl + max(d, 0))))
        dev = mp.mpf(mu_run) - root
        nl = len(eps)
        # rounded arguments and log domain: 3 eps_mach <|eps - mu|> (weights g f (1 - f)); ln g and constants:
        # eps_mach T (ln g_max + 3); adjacent doubles: 2 eps_mach |mu|
        common = EPS_MACH * (3 * wx / w + T * (mp.log(gmax) + 3) + 2 * abs(root))
        b_wc = EPS_MACH * (nl + 2 + big_l) * mag / dn + common
        b_dc = EPS_MACH * (nl + 2) * mp.mpf(n) / dn + common
        rec = {
            "id": sid,
            "N": lv["N"],
            "T": lv["T"],
            "levels": len(eps),
            "muRun": lv["mu"],
            "root40": mp.nstr(root, DIGITS, strip_zeros=False),
            "muRun_minus_root": "%.3e" % float(dev),
            "dN_dmu": "%.6e" % float(dn),
            "boundWellConditioned": "%.3e" % float(b_wc),
            "boundDirectCount": "%.3e" % float(b_dc),
            "withinBound": bool(abs(dev) <= b_wc),
        }
        return rec, float(prec_dev), float(b_dc), float(abs(dev) / b_wc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True, help="scratch directory for the `single` outputs")
    ap.add_argument("--jobs", type=int, default=min(os.cpu_count() or 4, 20))
    ap.add_argument("--fixture-count", type=int, default=8)
    a = ap.parse_args()
    work = Path(a.work)
    work.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
        print(("PASS" if ok else "FAIL") + " - " + name + ": " + detail, file=sys.stderr)

    specs = states_from_parameters()
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        runs = list(ex.map(lambda s: run_single(s, work), specs))
    failed = [(sid, err) for sid, lv, err in runs if lv is None]
    check("solver_runs_completed", not failed,
          f"{len(specs)} thermal states of the canonical matrix (N, lambda in {{0, +-lambda_1}}, a4,0, T of "
          f"results/parameters.json) run with `single --mermin-levels` (canonical numerics, margin 0.2 + 2 sigma); "
          f"failed: {failed if failed else 'none'}")
    good = [(sid, lv) for sid, lv, _ in runs if lv is not None]
    forms = sorted({lv["merminRoot"] for _, lv in good})
    t1 = time.time()
    with cf.ProcessPoolExecutor(max_workers=a.jobs) as ex:
        res = list(ex.map(analyse, good, chunksize=1))
    t2 = time.time()
    recs = [r[0] for r in res]
    prec = max(r[1] for r in res)
    check("root_precision_self_check", prec < 1e-33,
          f"roots at {DIGITS} and at {CHECK_DIGITS} significant digits agree to {prec:.1e} (relative, max over "
          f"{len(res)} states): the {DIGITS}-digit roots are exact far below double precision")
    ratios = [(r[3], r[0]["id"]) for r in res]
    worst = max(ratios)
    absdev = max((abs(float(r["muRun_minus_root"])), r["id"]) for r in recs)
    target = next((r for r in recs if r["id"] == "N8_lamm1_a00_T10"), None)
    check("solver_mu_within_rounding_bound", all(r["withinBound"] for r in recs),
          f"the solver's mu (form {', '.join(forms)}) minus the {DIGITS}-digit root on its own final levels lies "
          f"within the rounding bound eps_mach [(n + 2 + L) (P + Hl + |d|)/(dN/dmu) + 3 <|eps - mu|> + "
          f"T (ln g_max + 3) + 2 |mu|] in "
          f"{sum(r['withinBound'] for r in recs)} of {len(recs)} states; largest |mu - root| {absdev[0]:.3e} "
          f"({absdev[1]}); largest ratio to the bound {worst[0]:.3f} ({worst[1]})"
          + (f"; N8_lamm1_a00_T10 (the cross-check failure, 8.27e-10 with the former direct count): "
             f"{target['muRun_minus_root']} (bound {target['boundWellConditioned']})" if target else ""))
    # the committed canonical matrix holds the same mu (printed with 16 significant digits)
    if THERMO.exists():
        with open(THERMO, newline="") as f:
            mat = {row["id"]: row for row in csv.DictReader(f)}
        diff = []
        for r in recs:
            row = mat.get(r["id"])
            if row is None or float(row["mu"]) != float("%.15e" % float(r["muRun"])):
                diff.append(r["id"])
        check("single_reproduces_committed_matrix", not diff and len(mat) == len(recs),
              f"the mu of every `single` run equals the mu of the committed results/thermo/thermodynamics.csv "
              f"(16 significant digits) in {len(recs) - len(diff)} of {len(recs)} states ({len(mat)} rows); "
              f"differing: {diff if diff else 'none'}: the comparison above applies to the committed matrix")
    else:
        check("single_reproduces_committed_matrix", False, "results/thermo/thermodynamics.csv not found")
    # fixture: the states with the largest conditioning bound of the direct count
    order = sorted(res, key=lambda r: (-r[2], r[0]["id"]))[: a.fixture_count]
    lvmap = dict(good)
    fixture = []
    for r in order:
        rec = r[0]
        lv = lvmap[rec["id"]]
        fixture.append({"id": rec["id"], "N": lv["N"], "T": lv["T"], "muRun": lv["mu"], "root40": rec["root40"],
                        "dN_dmu": rec["dN_dmu"], "boundDirectCount": rec["boundDirectCount"],
                        "boundWellConditioned": rec["boundWellConditioned"],
                        "levels": [[e, g] for e, g in lv["levels_eps_deg"]]})
    check("fixture_written", len(fixture) == a.fixture_count,
          f"fixture solver/tools/mermin-roots-40digit.json: the {len(fixture)} states with the largest conditioning "
          f"bound of the direct count: " + ", ".join(f"{x['id']} ({x['boundDirectCount']})" for x in fixture))
    fx = {
        "producer": "Revision/kohn_sham/solver/tools/mermin_roots_mp.py",
        "description": "Exact final Kohn-Sham levels (shortest round-trip decimals of `revision_ks_solver single "
                       "--mermin-levels`, canonical numerics) and the root of sum g/(1 + exp((eps - mu)/T)) = N computed "
                       f"with mpmath at {DIGITS} significant digits (checked at {CHECK_DIGITS}), for the thermal states "
                       "with the largest conditioning bound eps_mach [(n + 2) N/(dN/dmu) + 3 <|eps - mu|> + T (ln g_max + 3) + "
                       "2 |mu|] of the former direct count. "
                       "Test input of the Rust unit test mermin::tests::forty_digit_roots and of the solver check "
                       "thermo_mu_vs_40digit_roots. All numbers are strings.",
        "digits": DIGITS,
        "fixture": fixture,
    }
    FIXTURE.write_bytes((json.dumps(fx, indent=1) + "\n").encode("utf-8"))
    nfail = sum(c["verdict"] == "FAIL" for c in checks)
    rep = {
        "report": "Revision Kohn-Sham Rust solver: the Mermin chemical potential of every thermal state against "
                  f"{DIGITS}-digit roots on its own final levels",
        "producer": "Revision/kohn_sham/solver/tools/mermin_roots_mp.py",
        "method": f"mpmath {DIGITS} significant digits (bracketed Newton from the solver's mu; self-check at "
                  f"{CHECK_DIGITS} digits) on the exact doubles of `single --mermin-levels`; bounds as in "
                  "solver/src/mermin.rs with the split S = {eps < root}",
        "summary": {"checks": len(checks), "pass": len(checks) - nfail, "fail": nfail},
        "checks": checks,
        "states": recs,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_bytes((json.dumps(rep, indent=2) + "\n").encode("utf-8"))
    print(f"time: solver runs {t1 - t0:.1f} s, roots {t2 - t1:.1f} s, total {time.time() - t0:.1f} s", file=sys.stderr)
    print("SUCCESS" if nfail == 0 else "FAILURE")
    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
