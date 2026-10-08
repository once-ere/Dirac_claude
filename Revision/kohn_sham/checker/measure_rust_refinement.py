#!/usr/bin/env python3
"""Measure the grid uncertainty of the Rust Kohn-Sham solver for EVERY state of the canonical matrix.

The states are read from the committed canonical Rust results (Revision/kohn_sham/results): the 75 ground states
(ground/summary.csv), the 135 thermal states (thermo/thermodynamics.csv), the 60 exact-Fock-variant states
(exx/exact-fock-variant.csv) and the 5 slices of the crossing demonstration (adiabatic/crossing-demo.csv).  Each is
run with the Rust `single` command twice, with the canonical numerics (RK4 G = 900, root tolerance 1e-13, SCF
tolerance 1e-11) and with the refined numerics (G = 1800, 1e-14, 1e-12, thermal cut / 100), with the label-set
margin of the canonical matrix (0.25 + 2 sigma at T = 0, 0.2 + 2 sigma at T > 0).  The difference
|canonical - refined| measures the canonical error of every quantity that `single` reports (energies, EMT
integrals, all levels, the 151-point profiles incl. the brane and tip values, mu and the entropy, and for the thermal
states the canonical levels with their keys and occupations, which the cross-check compares label by label; for the
exact-Fock variant its E_KS and, from its levels, its HOMO/LUMO gap; for the crossing demonstration the aufbau
energy and, from the levels, the energy of the adiabatically continued a4,0 = 0 occupation).  The canonical
`single` run is also compared with the committed canonical matrix, which it must reproduce, so that the measured
differences apply to the committed results.  (The exact-Fock variant of the matrix starts from the converged
uniform-gas state, `single --exx` from zero potentials: both stop at the SCF tolerance, so their difference is
recorded and is part of the stated uncertainty in the cross-check.)

Writes (deterministic, LF) Revision/kohn_sham/checker/rust-refinement.json; the raw Rust outputs go to --work
(scratch).  Revision code only; it runs the Revision Rust solver binary.

Usage (from the repository root, after `cargo build --release` of Revision/kohn_sham/solver):
  python Revision/kohn_sham/checker/measure_rust_refinement.py --work <scratch dir> [--jobs N]
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
KS = HERE.parent
REPO = KS.parent.parent
BIN = KS / "solver" / "target" / "release" / ("revision_ks_solver.exe" if sys.platform == "win32" else "revision_ks_solver")
RUST = KS / "results"
OUT = HERE / "rust-refinement.json"
SIGMA = {"lam0": 0.0, "lamp1": 0.1, "lamm1": 0.1, "lamp2": 0.3, "lamm2": 0.3}
PROFILES = ("n", "S", "Q", "M_eff", "v_v", "e_int", "rho", "p3", "p_t", "p8")
DEG_TOL = 1e-9           # the degeneracy tolerance of the Rust solver (parameters.json numerics.degeneracyTolerance)
KIND_ORDER = {"ground": 0, "thermo": 1, "exx": 2, "crossing": 3}


def read_csv(p: Path):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def num(x):
    return float("nan") if x in ("null", "", "nan") else float(x)


def key_of(level):
    return f"{level[0]}:{'+1' if level[1] > 0 else '-1'}:{level[2]}:{level[3]}"


def run_single(spec, refined, work: Path):
    tag = "refined" if refined else "canonical"
    stem = f"{spec['kind']}_{spec['id']}_{tag}"
    out = work / f"{stem}.json"
    prof = work / f"{stem}.csv"
    cmd = [str(BIN), "single", "--m", "1", "--lambda", repr(spec["lambda"]), "--a4", repr(spec["a4"]), "--N", repr(spec["N"]),
           "--margin", repr(spec["margin"]), "--out", str(out), "--profiles", str(prof)]
    if spec.get("T") is not None:
        cmd += ["--T", repr(spec["T"])]
    if spec["kind"] == "exx":
        cmd.append("--exx")
    if refined:
        cmd.append("--refined")
    # canonical thermal runs also write their exact final levels and mu (shortest round-trip decimals; the main output has 16
    # significant digits): the checker tests the solver's stated rounding bound of mu on them
    mlv = work / f"{stem}.mermin.json" if spec["kind"] == "thermo" and not refined else None
    if mlv is not None:
        cmd += ["--mermin-levels", str(mlv)]
    t0 = time.time()
    r = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True)
    ok = r.returncode == 0 and r.stdout.strip().endswith("SUCCESS")
    return {"cmd": " ".join(["revision_ks_solver"] + cmd[1:]).replace(str(work), "<work>"), "ok": ok,
            "json": json.loads(out.read_text(encoding="utf-8")) if ok else None,
            "mermin": json.loads(mlv.read_text(encoding="utf-8")) if ok and mlv is not None else None,
            "profiles": read_csv(prof) if ok else None, "stderr": r.stderr[-2000:] if not ok else "", "seconds": time.time() - t0}


def homo_lumo(levels):
    """HOMO and LUMO of a T = 0 state from its levels [n2, j, parity, label, eps, deg, f] (the grouping of the Rust
    solver: sorted by (eps, key), a group = levels within DEG_TOL of its first member)."""
    order = sorted(levels, key=lambda l: (l[4], l[0], l[1], 0 if l[2] == "even" else 1, l[3]))
    groups = []
    for l in order:
        if groups and l[4] - groups[-1][0] <= DEG_TOL:
            groups[-1][1].append(l)
        else:
            groups.append((l[4], [l]))
    homo = max((e for e, m in groups if any(x[6] > 1e-12 for x in m)), default=-math.inf)
    lumo = min((e for e, m in groups if e > homo and any(x[6] < 1.0 - 1e-12 for x in m)), default=math.inf)
    return homo, lumo


def compare(spec, c, r, rust_rows, occ0=None):
    rec = {"id": spec["id"], "kind": spec["kind"], "command_canonical": c["cmd"], "command_refined": r["cmd"],
           "runs_ok": bool(c["ok"] and r["ok"])}
    if spec["kind"] == "crossing" and occ0 is None:
        rec["runs_ok"] = False
    if not rec["runs_ok"]:
        rec["error"] = (c["stderr"] + r["stderr"])[-1000:] or "the a4,0 = 0 run of the crossing demonstration failed"
        return rec
    cj, rj = c["json"], r["json"]
    sc = {}

    def put(name, cv, rv):
        sc[name] = {"canonical": cv, "refined": rv, "abs_diff": abs(cv - rv)}

    put("E_KS", cj["E_KS"], rj["E_KS"])
    put("E_band", cj["E_band"], rj["E_band"])
    put("E_int", cj["E_int"], rj["E_int"])
    for k in ("rho", "p3", "p_t", "p8", "n"):
        put("int_" + k, cj["emtIntegrals_2Vol7_int_e6Hy"][k], rj["emtIntegrals_2Vol7_int_e6Hy"][k])
    if spec["kind"] == "thermo":
        put("mu", cj["mu_or_fermi_level"], rj["mu_or_fermi_level"])
        put("entropy", cj["entropy"], rj["entropy"])
    pc, pr = c["profiles"], r["profiles"]
    prof = {}
    for nm in PROFILES:
        xc = [num(row[nm]) for row in pc]
        xr = [num(row[nm]) for row in pr]
        d = [abs(a - b) for a, b in zip(xc, xr)]
        prof[nm] = {"max_abs_diff": max(d), "max_abs": max(abs(a) for a in xc), "points": len(d)}
    for k in ("rho", "p3", "p_t", "p8"):
        put(k + "_brane", num(pc[-1][k]), num(pr[-1][k]))
        put(k + "_tip", num(pc[0][k]), num(pr[0][k]))
    lcl = cj["levels_n2_j_parity_label_eps_deg_f"]
    lrl = rj["levels_n2_j_parity_label_eps_deg_f"]
    lc = {tuple(l[:4]): l[4] for l in lcl}
    lr = {tuple(l[:4]): l[4] for l in lrl}
    common = sorted(set(lc) & set(lr))
    worst = max(common, key=lambda k: abs(lc[k] - lr[k]))
    rec["levels"] = {"common": len(common), "max_abs_diff": abs(lc[worst] - lr[worst]), "worst": f"{worst[0]}:{worst[1]}:{worst[2]}:{worst[3]}"}
    if spec["kind"] in ("ground", "exx", "crossing"):
        occ_c = sorted(tuple(l[:4]) for l in lcl if l[6] > 0)
        occ_r = sorted(tuple(l[:4]) for l in lrl if l[6] > 0)
        rec["levels"]["same_occupied_labels"] = occ_c == occ_r
    else:
        # Mermin: every level of the thermal window is occupied; the window edge may differ between the two runs
        rec["levels"]["same_label_set"] = sorted(lc) == sorted(lr)
        rec["levels"]["labels_canonical_refined"] = [len(lc), len(lr)]
        # the final canonical levels (eps, degeneracy): the checker recomputes mu from them in high precision
        rec["canonical_levels_eps_deg"] = [[l[4], l[5]] for l in lcl]
        # their keys (Rust labels, n2:j:parity:label) and occupations, in the same order: the checker compares the thermal levels
        # label by label with the reference (the Rust matrix writes no thermal levels file)
        rec["canonical_level_keys_f"] = [[key_of(l), l[6]] for l in lcl]
        rec["canonical_T_N"] = [cj["parameters"]["T"], cj["parameters"]["N"]]
        # the exact doubles (shortest round-trip) of the final levels and of mu, from `single --mermin-levels` of the same run; they
        # must round to the 16-digit values of the main output
        mj = c["mermin"]
        ex = [[float(e), float(g)] for e, g in mj["levels_eps_deg"]]
        rec["canonical_mermin_exact"] = {
            "root_form": mj["merminRoot"], "mu": float(mj["mu"]), "levels_eps_deg": ex,
            "mu_rounds_to_16_digit_value": float(f"{float(mj['mu']):.15e}") == cj["mu_or_fermi_level"],
            "levels_round_to_16_digit_values": len(ex) == len(lcl) and all(float(f"{e:.15e}") == l[4] and g == l[5] for (e, g), l in zip(ex, lcl)),
        }
    if spec["kind"] == "exx":
        hc, uc = homo_lumo(lcl)
        hr, ur = homo_lumo(lrl)
        put("gap_exact_fock", uc - hc, ur - hr)
    if spec["kind"] == "crossing":
        # the adiabatically continued state: the a4,0 = 0 occupation (by label) with the levels of this slice (lambda = 0)
        def e_cont(levels, occ):
            have = {key_of(l): l for l in levels}
            missing = [k for k in occ if k not in have]
            return (sum(have[k][5] * f * have[k][4] for k, f in occ.items()) if not missing else math.nan), missing
        ecc, mc = e_cont(lcl, occ0["canonical"])
        ecr, mr = e_cont(lrl, occ0["refined"])
        put("E_adiabatically_continued", ecc, ecr)
        rec["continued_labels_missing"] = sorted(set(mc) | set(mr))
        rec["occupied_set_equal_to_a4_0"] = {key_of(l): l[6] for l in lcl if l[6] > 0} == occ0["canonical"]
    rec["scalars"] = sc
    rec["profiles"] = prof
    # the canonical single run must reproduce the committed canonical matrix
    cm = {}
    if spec["kind"] == "ground":
        srow = rust_rows["summary"][spec["id"]]
        erow = rust_rows["emt"][spec["id"]]
        cm["E_KS_rel"] = abs(cj["E_KS"] - float(srow["E_KS"])) / max(1.0, abs(float(srow["E_KS"])))
        cm["emt_integrals_rel"] = max(abs(cj["emtIntegrals_2Vol7_int_e6Hy"][k] - float(erow["int_" + k])) / max(1.0, abs(float(erow["int_" + k])))
                                      for k in ("rho", "p3", "p_t", "p8", "n"))
        lv = {(int(x["n2"]), int(x["j"]), x["parity"], int(x["label"])): float(x["eps"]) for x in read_csv(RUST / "ground" / "levels" / f"{spec['id']}.csv")}
        cmm = [abs(lc[k] - lv[k]) for k in lc if k in lv]
        cm["levels_max_abs"] = max(cmm)
        cm["levels_compared"] = len(cmm)
        mp_ = read_csv(RUST / "ground" / "profiles" / f"{spec['id']}.csv")
        cm["profiles_max_rel"] = max(max(abs(num(a[nm]) - num(b[nm])) for a, b in zip(pc, mp_)) / max(1e-300, max(abs(num(b[nm])) for b in mp_))
                                     for nm in PROFILES)
    elif spec["kind"] == "thermo":
        trow = rust_rows["thermo"][spec["id"]]
        cm["E_rel"] = abs(cj["E_KS"] - float(trow["E"])) / max(1.0, abs(float(trow["E"])))
        cm["mu_abs"] = abs(cj["mu_or_fermi_level"] - float(trow["mu"]))
        cm["entropy_rel"] = abs(cj["entropy"] - float(trow["entropy"])) / max(1e-6, abs(float(trow["entropy"])))
    elif spec["kind"] == "exx":
        xrow = rust_rows["exx"][spec["id"]]
        hc, uc = homo_lumo(lcl)
        cm["exx_E_abs"] = abs(cj["E_KS"] - float(xrow["E_exact_fock_scf"]))
        cm["exx_gap_abs"] = abs((uc - hc) - float(xrow["gap_exact_fock"]))
        cm["exx_matrix_iterations"] = int(xrow["iterations"])
        cm["exx_single_iterations"] = int(cj["iterations"])
    else:
        drow = rust_rows["crossing"][spec["id"]]
        cm["E_aufbau_abs"] = abs(cj["E_KS"] - float(drow["E_aufbau"]))
        cm["E_continued_abs"] = abs(sc["E_adiabatically_continued"]["canonical"] - float(drow["E_adiabatically_continued"]))
    rec["canonical_single_vs_matrix"] = cm
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--jobs", type=int, default=20)
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()
    work = Path(args.work)
    work.mkdir(parents=True, exist_ok=True)
    if not BIN.exists():
        print(f"Rust solver binary missing: {BIN} (cargo build --release in Revision/kohn_sham/solver)", file=sys.stderr)
        return 2
    t_all = time.time()
    rust_rows = {"summary": {r["id"]: r for r in read_csv(RUST / "ground" / "summary.csv")},
                 "emt": {r["id"]: r for r in read_csv(RUST / "ground" / "emt-integrals.csv")},
                 "thermo": {r["id"]: r for r in read_csv(RUST / "thermo" / "thermodynamics.csv")},
                 "exx": {r["id"]: r for r in read_csv(RUST / "exx" / "exact-fock-variant.csv")}}
    specs = []
    for r in rust_rows["summary"].values():
        specs.append({"id": r["id"], "kind": "ground", "N": float(r["N"]), "lambda": float(r["lambda"]), "a4": float(r["a4"]),
                      "margin": 0.25 + 2.0 * SIGMA[r["lambda_tag"]]})
    for r in rust_rows["thermo"].values():
        specs.append({"id": r["id"], "kind": "thermo", "N": float(r["N"]), "lambda": float(r["lambda"]), "a4": float(r["a4"]),
                      "T": float(r["T"]), "margin": 0.2 + 2.0 * SIGMA[r["lambda_tag"]]})
    for r in rust_rows["exx"].values():
        specs.append({"id": r["id"], "kind": "exx", "N": float(r["N"]), "lambda": float(r["lambda"]), "a4": float(r["a4"]),
                      "margin": 0.25 + 2.0 * SIGMA[r["lambda_tag"]]})
    rust_rows["crossing"] = {}
    for r in read_csv(RUST / "adiabatic" / "crossing-demo.csv"):
        sid = f"N{int(r['N'])}_lam0_a{int(round(float(r['a4']) * 10)):02d}"
        rust_rows["crossing"][sid] = r
        specs.append({"id": sid, "kind": "crossing", "N": float(r["N"]), "lambda": 0.0, "a4": float(r["a4"]), "margin": 0.25})
    specs.sort(key=lambda s: (KIND_ORDER[s["kind"]], s["id"]))
    tasks = [(i, s, refined) for i, s in enumerate(specs) for refined in (False, True)]
    # longest first (thermal at the highest T, refined); the order changes no output
    cost = lambda t: (t[1].get("T") or 0.0) * 100.0 + (1.0 if t[2] else 0.0) + t[1]["a4"] * 0.1
    res = {}
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(run_single, s, refined, work): (i, refined) for (i, s, refined) in sorted(tasks, key=lambda t: -cost(t))}
        for f in futs:
            res[futs[f]] = f.result()
    # occupation of the crossing demonstration at a4,0 = 0 (by label), per numerics
    occ0 = None
    c0 = [i for i, s in enumerate(specs) if s["kind"] == "crossing" and s["a4"] == 0.0]
    if c0 and res[(c0[0], False)]["ok"] and res[(c0[0], True)]["ok"]:
        occ0 = {tag: {key_of(l): l[6] for l in res[(c0[0], rf)]["json"]["levels_n2_j_parity_label_eps_deg_f"] if l[6] > 0}
                for tag, rf in (("canonical", False), ("refined", True))}
    recs = [compare(s, res[(i, False)], res[(i, True)], rust_rows, occ0) for i, s in enumerate(specs)]
    out = {"description": "Measured grid uncertainty of the Rust Kohn-Sham solver (Revision/kohn_sham/solver) for EVERY state of the canonical "
                          "matrix (75 ground, 135 thermal, 60 exact-Fock-variant states and the 5 slices of the crossing demonstration): "
                          "|canonical - refined| of `revision_ks_solver single` (canonical: RK4 G = 900, root tolerance 1e-13, SCF tolerance "
                          "1e-11; refined: G = 1800, 1e-14, 1e-12, thermal cut 1e-14), with the label-set margin of the canonical matrix. "
                          "The canonical single run reproduces the committed canonical matrix (canonical_single_vs_matrix).",
           "producer": "Revision/kohn_sham/checker/measure_rust_refinement.py",
           "counts": {k: sum(1 for s in specs if s["kind"] == k) for k in KIND_ORDER},
           "states": recs}
    txt = json.dumps(out, indent=1, ensure_ascii=True) + "\n"
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(txt)
    bad = [f"{r['kind']}:{r['id']}" for r in recs if not r["runs_ok"]]
    slow = sorted(((v["seconds"], f"{specs[k[0]]['kind']}:{specs[k[0]]['id']}{' refined' if k[1] else ''}") for k, v in res.items()), reverse=True)[:3]
    print(f"{len(recs)} states measured ({len(tasks)} single runs on {args.jobs} threads) in {time.time() - t_all:.1f} s; slowest runs: "
          + ", ".join(f"{n} {s:.1f} s" for s, n in slow) + f"; failed runs: {bad if bad else 'none'}", file=sys.stderr)
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
