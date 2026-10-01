#!/usr/bin/env python3
"""Measure the grid uncertainty of the Rust Kohn-Sham solver for the reference subset, state by state.

For every state of the reference subset (Revision/kohn_sham/reference/results/{ground,thermo}/*.json) the
Rust solver is run in `single` mode twice, with the canonical numerics (RK4 G = 900, root tolerance
1e-13, SCF tolerance 1e-11) and with the refined numerics (G = 1800, 1e-14, 1e-12), with the same label-set
margin as the canonical matrix (0.25 + 2 sigma at T = 0, 0.2 + 2 sigma at T > 0).  The difference
|canonical - refined| measures the canonical error of every quantity that `single` reports (energies, EMT
integrals, all levels, the 151-point profiles incl. the brane and tip values, mu and the entropy).  The
canonical `single` run is also compared with the committed canonical matrix (Revision/kohn_sham/results),
which it must reproduce, so that the measured differences apply to the committed results.

Writes (deterministic, LF) Revision/kohn_sham/checker/rust-refinement.json; the raw Rust outputs go to
--work (scratch).  Revision code only; it runs the Revision Rust solver binary.

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
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
KS = HERE.parent
REPO = KS.parent.parent
BIN = KS / "solver" / "target" / "release" / ("revision_ks_solver.exe" if sys.platform == "win32" else "revision_ks_solver")
REF = KS / "reference" / "results"
RUST = KS / "results"
OUT = HERE / "rust-refinement.json"
SIGMA = {"lam0": 0.0, "lamp1": 0.1, "lamm1": 0.1, "lamp2": 0.3, "lamm2": 0.3}
PROFILES = ("n", "S", "Q", "M_eff", "v_v", "e_int", "rho", "p3", "p_t", "p8")


def read_csv(p: Path):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def num(x):
    return float("nan") if x in ("null", "") else float(x)


def run_single(spec, refined, work: Path):
    tag = "refined" if refined else "canonical"
    out = work / f"{spec['id']}_{tag}.json"
    prof = work / f"{spec['id']}_{tag}.csv"
    cmd = [str(BIN), "single", "--m", "1", "--lambda", repr(spec["lambda"]), "--a4", repr(spec["a4"]), "--N", repr(spec["N"]),
           "--margin", repr(spec["margin"]), "--out", str(out), "--profiles", str(prof)]
    if spec.get("T") is not None:
        cmd += ["--T", repr(spec["T"])]
    if refined:
        cmd.append("--refined")
    r = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True)
    ok = r.returncode == 0 and r.stdout.strip().endswith("SUCCESS")
    return {"cmd": " ".join(["revision_ks_solver"] + cmd[1:]).replace(str(work), "<work>"), "ok": ok,
            "json": json.loads(out.read_text(encoding="utf-8")) if ok else None,
            "profiles": read_csv(prof) if ok else None, "stderr": r.stderr[-2000:] if not ok else ""}


def compare(spec, c, r, rust_rows):
    rec = {"id": spec["id"], "kind": spec["kind"], "command_canonical": c["cmd"], "command_refined": r["cmd"],
           "runs_ok": bool(c["ok"] and r["ok"])}
    if not rec["runs_ok"]:
        rec["error"] = (c["stderr"] + r["stderr"])[-1000:]
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
    rec["scalars"] = sc
    rec["profiles"] = prof
    lc = {(l[0], l[1], l[2], l[3]): l[4] for l in cj["levels_n2_j_parity_label_eps_deg_f"]}
    lr = {(l[0], l[1], l[2], l[3]): l[4] for l in rj["levels_n2_j_parity_label_eps_deg_f"]}
    common = sorted(set(lc) & set(lr))
    worst = max(common, key=lambda k: abs(lc[k] - lr[k]))
    rec["levels"] = {"common": len(common), "max_abs_diff": abs(lc[worst] - lr[worst]),
                     "worst": f"{worst[0]}:{worst[1]}:{worst[2]}:{worst[3]}"}
    if spec["kind"] == "ground":
        occ_c = sorted(k for k in (tuple(l[:4]) for l in cj["levels_n2_j_parity_label_eps_deg_f"] if l[6] > 0))
        occ_r = sorted(k for k in (tuple(l[:4]) for l in rj["levels_n2_j_parity_label_eps_deg_f"] if l[6] > 0))
        rec["levels"]["same_occupied_labels"] = occ_c == occ_r
    else:
        # Mermin: every level of the thermal window is occupied; the window edge may differ between the two runs
        rec["levels"]["same_label_set"] = sorted(lc) == sorted(lr)
        rec["levels"]["labels_canonical_refined"] = [len(lc), len(lr)]
        # the final canonical levels (eps, degeneracy): the checker recomputes mu from them in high precision
        rec["canonical_levels_eps_deg"] = [[l[4], l[5]] for l in cj["levels_n2_j_parity_label_eps_deg_f"]]
        rec["canonical_T_N"] = [cj["parameters"]["T"], cj["parameters"]["N"]]
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
    else:
        trow = rust_rows["thermo"][spec["id"]]
        cm["E_rel"] = abs(cj["E_KS"] - float(trow["E"])) / max(1.0, abs(float(trow["E"])))
        cm["mu_abs"] = abs(cj["mu_or_fermi_level"] - float(trow["mu"]))
        cm["entropy_rel"] = abs(cj["entropy"] - float(trow["entropy"])) / max(1e-6, abs(float(trow["entropy"])))
    rec["canonical_single_vs_matrix"] = cm
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--jobs", type=int, default=12)
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()
    work = Path(args.work)
    work.mkdir(parents=True, exist_ok=True)
    if not BIN.exists():
        print(f"Rust solver binary missing: {BIN} (cargo build --release in Revision/kohn_sham/solver)", file=sys.stderr)
        return 2
    specs = []
    for p in sorted((REF / "ground").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        specs.append({"id": d["id"], "kind": "ground", "N": d["N"], "lambda": d["lambda"], "a4": d["a4"],
                      "margin": 0.25 + 2.0 * SIGMA[d["lambda_tag"]]})
    for p in sorted((REF / "thermo").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        specs.append({"id": d["id"], "kind": "thermo", "N": d["N"], "lambda": d["lambda"], "a4": d["a4"], "T": d["T"],
                      "margin": 0.2 + 2.0 * SIGMA[d["lambda_tag"]]})
    rust_rows = {"summary": {r["id"]: r for r in read_csv(RUST / "ground" / "summary.csv")},
                 "emt": {r["id"]: r for r in read_csv(RUST / "ground" / "emt-integrals.csv")},
                 "thermo": {r["id"]: r for r in read_csv(RUST / "thermo" / "thermodynamics.csv")}}
    tasks = [(s, refined) for s in specs for refined in (False, True)]
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        res = list(ex.map(lambda t: run_single(t[0], t[1], work), tasks))
    recs = [compare(s, res[2 * i], res[2 * i + 1], rust_rows) for i, s in enumerate(specs)]
    out = {"description": "Measured grid uncertainty of the Rust Kohn-Sham solver (Revision/kohn_sham/solver) for the states of the "
                          "reference subset: |canonical - refined| of `revision_ks_solver single` (canonical: RK4 G = 900, root tolerance "
                          "1e-13, SCF tolerance 1e-11; refined: G = 1800, 1e-14, 1e-12), with the label-set margin of the canonical matrix. "
                          "The canonical single run reproduces the committed canonical matrix (canonical_single_vs_matrix).",
           "producer": "Revision/kohn_sham/checker/measure_rust_refinement.py",
           "states": recs}
    txt = json.dumps(out, indent=1, ensure_ascii=True) + "\n"
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(txt)
    bad = [r["id"] for r in recs if not r["runs_ok"]]
    print(f"{len(recs)} states measured; failed runs: {bad if bad else 'none'}", file=sys.stderr)
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
