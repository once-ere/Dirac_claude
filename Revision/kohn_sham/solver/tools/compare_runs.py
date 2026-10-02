#!/usr/bin/env python3
"""Compare runs of the Revision Kohn-Sham solver (standard library only).

* --repeat DIR: a second run with the canonical options; every file of the
  canonical output tree (and the canonical report, if --repeat-report is given)
  must be byte-identical.
* --refined DIR: a run with --refined (RK4 steps x 2, root tolerance / 10, SCF
  tolerance / 10, thermal occupation cut / 100, and the Mermin root solved with
  the exactly equivalent LinearDeviation form instead of LogBalance, a
  different rounding path); the canonical numbers must agree within
  tolerances that bound the canonical discretisation error: eigenvalues 1e-8 m
  (absolute), energies 1e-8 (relative), proper profiles 1e-6 (relative to the
  profile maximum), thermodynamic quantities (mu, E, F, both forms of Omega,
  S) 1e-8 (relative), derived derivatives (Q_max, dE/da4, C_V = T dS/dT) 1e-6
  (relative).

Why the refined run changes the root form: the former direct count
sum g f - N fixed mu only to eps_mach N/(dN/dmu), and the canonical and the
refined run carried the same rounding (their levels differ too little to move
it), so |canonical - refined| did not see an error of 8.3e-10 m.  With two
different rounding paths, |canonical - refined| of mu and of Omega = F - mu N
contains the rounding error of the root.

Writes a JSON report with every check (name, verdict, detail); exit 1 on failure.
"""
import argparse
import csv
import glob
import hashlib
import json
import os
import sys

TOL = {"eig": 1e-8, "energy": 1e-8, "profile": 1e-6, "thermo": 1e-8, "derived": 1e-6}


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def tree(root):
    out = {}
    for dp, _, fs in os.walk(root):
        for fn in fs:
            p = os.path.join(dp, fn)
            out[os.path.relpath(p, root).replace(os.sep, "/")] = p
    return out


def rows(path, key):
    with open(path, newline="") as f:
        r = list(csv.DictReader(f))
    return {tuple(x[k] for k in key): x for x in r}


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return float("nan")


def rel(a, b, floor=1e-300):
    return abs(a - b) / max(abs(a), abs(b), floor)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--canonical", required=True)
    ap.add_argument("--canonical-report", default=None)
    ap.add_argument("--repeat", default=None)
    ap.add_argument("--repeat-report", default=None)
    ap.add_argument("--refined", default=None)
    ap.add_argument("--report", required=True)
    a = ap.parse_args()
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
        print(("PASS" if ok else "FAIL") + " - " + name + ": " + detail)

    can = tree(a.canonical)
    if a.repeat:
        rep = tree(a.repeat)
        same_set = sorted(can) == sorted(rep)
        diff = [p for p in sorted(can) if p in rep and sha(can[p]) != sha(rep[p])]
        nbytes = sum(os.path.getsize(p) for p in can.values())
        check("repeat_byte_identical", same_set and not diff,
              f"second run with the canonical options: {len(can)} files ({nbytes} bytes) compared, same file set: {same_set}, differing files: {diff if diff else 'none'}")
        if a.canonical_report and a.repeat_report:
            ok = sha(a.canonical_report) == sha(a.repeat_report)
            check("repeat_report_byte_identical", ok, "the solver check report of the repeat run is byte-identical to the canonical report")
        crlf = [p for p, q in can.items() if b"\r\n" in open(q, "rb").read()]
        check("outputs_lf_only", not crlf, f"no CRLF line endings in the canonical outputs (offending: {crlf if crlf else 'none'})")

    if a.refined:
        ref = a.refined
        pc = json.load(open(os.path.join(a.canonical, "parameters.json")))
        pr = json.load(open(os.path.join(ref, "parameters.json")))
        same_n = pc["particleNumbers"]["values"] == pr["particleNumbers"]["values"]
        lc = [(c["N"], c["lambda1"], c["lambda2"]) for c in pc["couplingCalibration"]["values"]]
        lr = [(c["N"], c["lambda1"], c["lambda2"]) for c in pr["couplingCalibration"]["values"]]
        check("refined_same_inputs", same_n and lc == lr,
              f"the refined run selects the same N {pc['particleNumbers']['values']} and the same calibrated couplings (rounded to 4 significant digits) {lc}: N {same_n}, couplings {lc == lr}")
        # free analytic spectra: canonical and refined errors
        fa = rows(os.path.join(a.canonical, "spectrum/free-k0-analytic.csv"), ["m", "L", "parity", "label"])
        fr = rows(os.path.join(ref, "spectrum/free-k0-analytic.csv"), ["m", "L", "parity", "label"])
        ratios = []
        worst_c = worst_r = 0.0
        for k, x in fa.items():
            dc = abs(num(x["difference"]))
            dr = abs(num(fr[k]["difference"]))
            worst_c, worst_r = max(worst_c, dc), max(worst_r, dr)
            if dc > 1e-11 and dr > 0:
                ratios.append(dc / dr)
        ratios.sort()
        med = ratios[len(ratios) // 2] if ratios else float("nan")
        check("refined_free_spectra_convergence_order", 12.0 < med < 20.0,
              f"analytic k = 0 spectra: max error canonical {worst_c:.3e}, refined {worst_r:.3e}; median error ratio {med:.2f} over {len(ratios)} levels (RK4 order 4 predicts 16)")
        # ground summary
        gc = rows(os.path.join(a.canonical, "ground/summary.csv"), ["id"])
        gr = rows(os.path.join(ref, "ground/summary.csv"), ["id"])
        we = wg = 0.0
        wid = gid = ""
        for k, x in gc.items():
            y = gr.get(k)
            if y is None:
                continue
            e = rel(num(x["E_KS"]), num(y["E_KS"]), 1.0)
            if e > we:
                we, wid = e, k[0]
            g = max(abs(num(x[c]) - num(y[c])) for c in ("HOMO", "LUMO", "KS_gap"))
            if g > wg:
                wg, gid = g, k[0]
        check("refined_ground_energies", we <= TOL["energy"] and set(gc) == set(gr),
              f"{len(gc)} ground states, same run set: {set(gc) == set(gr)}; max relative difference of E_KS {we:.3e} ({wid}); tolerance {TOL['energy']:.0e}")
        check("refined_ground_homo_lumo_gap", wg <= TOL["eig"],
              f"max |difference| of HOMO, LUMO, KS gap {wg:.3e} m ({gid}); tolerance {TOL['eig']:.0e}")
        # levels
        wl = 0.0
        wlid = ""
        nlev = 0
        mism = []
        for p in sorted(glob.glob(os.path.join(a.canonical, "ground/levels/*.csv"))):
            name = os.path.basename(p)
            q = os.path.join(ref, "ground/levels", name)
            if not os.path.exists(q):
                mism.append(name)
                continue
            lc_ = rows(p, ["n2", "j", "parity", "label"])
            lr_ = rows(q, ["n2", "j", "parity", "label"])
            if set(lc_) != set(lr_):
                mism.append(name)
            for k, x in lc_.items():
                if k in lr_:
                    nlev += 1
                    d = abs(num(x["eps"]) - num(lr_[k]["eps"]))
                    if d > wl:
                        wl, wlid = d, f"{name[:-4]} level {':'.join(k)}"
                    if num(x["f"]) != num(lr_[k]["f"]):
                        mism.append(name + " occupation")
        check("refined_eigenvalues", wl <= TOL["eig"] and not mism,
              f"{nlev} Kohn-Sham levels compared label by label: max |difference| {wl:.3e} m ({wlid}); label sets and occupations identical: {not mism} {mism if mism else ''}; tolerance {TOL['eig']:.0e}")
        # excited
        ec = rows(os.path.join(a.canonical, "excited/summary.csv"), ["id"])
        er = rows(os.path.join(ref, "excited/summary.csv"), ["id"])
        wd = max(abs(num(x["delta_SCF"]) - num(er[k]["delta_SCF"])) for k, x in ec.items() if k in er)
        check("refined_delta_scf", wd <= TOL["eig"], f"max |difference| of the Delta-SCF excitation energies {wd:.3e} m; tolerance {TOL['eig']:.0e}")
        # profiles
        wp = 0.0
        wpid = ""
        for p in sorted(glob.glob(os.path.join(a.canonical, "ground/profiles/*.csv"))):
            name = os.path.basename(p)
            q = os.path.join(ref, "ground/profiles", name)
            with open(p) as f:
                A = list(csv.DictReader(f))
            with open(q) as f:
                B = list(csv.DictReader(f))
            if len(A) != len(B) or any(abs(num(x["y"]) - num(y["y"])) > 1e-12 for x, y in zip(A, B)):
                wp, wpid = float("inf"), name + " (grids differ)"
                continue
            for col in ("n", "S", "rho", "p3", "p_t", "p8"):
                mx = max(abs(num(x[col])) for x in A)
                if mx == 0.0:
                    continue
                d = max(abs(num(x[col]) - num(y[col])) for x, y in zip(A, B)) / mx
                if d > wp:
                    wp, wpid = d, f"{name[:-4]} {col}"
        check("refined_profiles", wp <= TOL["profile"], f"proper profiles n, S, rho, p3, p_t, p8 at the 151 common y points: max difference / profile maximum {wp:.3e} ({wpid}); tolerance {TOL['profile']:.0e}")
        # derived
        ac = rows(os.path.join(a.canonical, "adiabatic/adiabaticity.csv"), ["id"])
        ar = rows(os.path.join(ref, "adiabatic/adiabaticity.csv"), ["id"])
        wq = 0.0
        wqid = ""
        for k, x in ac.items():
            for col in ("Q_max", "dE_da4_emt", "dE_da4_finite_difference"):
                d = rel(num(x[col]), num(ar[k][col]), 1e-6)
                if d > wq:
                    wq, wqid = d, f"{k[0]} {col}"
        check("refined_adiabatic_derivatives", wq <= TOL["derived"], f"Q_max, dE/da4 (EMT and finite differences): max relative difference {wq:.3e} ({wqid}); tolerance {TOL['derived']:.0e}")
        # thermodynamics
        tc = rows(os.path.join(a.canonical, "thermo/thermodynamics.csv"), ["id"])
        tr = rows(os.path.join(ref, "thermo/thermodynamics.csv"), ["id"])
        wt = wcv = 0.0
        wtid = wcid = ""
        for k, x in tc.items():
            y = tr.get(k)
            if y is None:
                continue
            for col in ("mu", "E", "F", "Omega_direct", "Omega_F_minus_muN"):
                d = rel(num(x[col]), num(y[col]), 1.0)
                if d > wt:
                    wt, wtid = d, f"{k[0]} {col}"
            d = rel(num(x["entropy"]), num(y["entropy"]), 1e-6)
            if d > wt:
                wt, wtid = d, f"{k[0]} entropy"
            d = rel(num(x["C_V"]), num(y["C_V"]), 1e-6)
            if d > wcv:
                wcv, wcid = d, k[0]
        check("refined_thermodynamics", wt <= TOL["thermo"] and set(tc) == set(tr),
              f"{len(tc)} thermal states, same set: {set(tc) == set(tr)}; mu, E, F, Omega (both forms; relative to max(|x|, 1)) and S (relative to max(|S|, 1e-6)): max {wt:.3e} ({wtid}); tolerance {TOL['thermo']:.0e}")
        # the Mermin root: two rounding paths, so that |canonical - refined| sees the rounding of mu
        fc = pc["numerics"].get("merminRoot")
        fr_ = pr["numerics"].get("merminRoot")
        wm = wo = wb = 0.0
        wmid = woid = wbid = ""
        for k, x in tc.items():
            y = tr.get(k)
            if y is None:
                continue
            d = abs(num(x["mu"]) - num(y["mu"]))
            if d > wm:
                wm, wmid = d, k[0]
            d = max(abs(num(x[c]) - num(y[c])) for c in ("Omega_direct", "Omega_F_minus_muN"))
            if d > wo:
                wo, woid = d, k[0]
            b = num(x.get("mu_rounding_bound"))
            if b > wb:
                wb, wbid = b, k[0]
        check("refined_mermin_root_path", fc is not None and fr_ is not None and fc != fr_,
              f"the canonical run solves sum g f = N with the form {fc}, the refined run with {fr_} (exactly equivalent "
              f"well-conditioned residuals of solver/src/mermin.rs with different rounding paths), so |canonical - refined| "
              f"of mu and Omega contains the rounding error of the root instead of sharing it (the former direct count, the "
              f"same in both runs, hid an error of 8.3e-10 m in N8_lamm1_a00_T10); max |mu_c - mu_r| {wm:.3e} m ({wmid}), "
              f"max |Omega_c - Omega_r| {wo:.3e} ({woid}); largest canonical rounding bound of mu (thermodynamics.csv "
              f"mu_rounding_bound) {wb:.3e} ({wbid})")
        check("refined_heat_capacity", wcv <= TOL["derived"], f"C_V = T dS/dT (Richardson): max relative difference (relative to max(|C_V|, 1e-6)) {wcv:.3e} ({wcid}); tolerance {TOL['derived']:.0e}")

    nfail = sum(1 for c in checks if c["verdict"] == "FAIL")
    rep = {
        "report": "Revision Kohn-Sham Rust solver: repeat (byte identity) and refined-tolerance comparison",
        "producer": "Revision/kohn_sham/solver/tools/compare_runs.py",
        "tolerances": TOL,
        "summary": {"checks": len(checks), "pass": len(checks) - nfail, "fail": nfail},
        "checks": checks,
    }
    os.makedirs(os.path.dirname(os.path.abspath(a.report)), exist_ok=True)
    with open(a.report, "w", newline="\n") as f:
        f.write(json.dumps(rep, indent=2) + "\n")
    print("SUCCESS" if nfail == 0 else "FAILURE")
    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
