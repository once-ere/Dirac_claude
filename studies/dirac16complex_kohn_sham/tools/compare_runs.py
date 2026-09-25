#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Determinism and tolerance-convergence comparison of dirac16complex_kohn_sham
output trees (standard library only).

    python tools/compare_runs.py --canonical DIR --repeat DIR [--refined DIR]
                                 [--report PATH]

* repeat: every file listed in the `files` array of every `<sub>/summary.json`
  of the canonical tree must exist in the repeat tree with the same SHA-256
  (byte identity of a second run of the same binary with the same flags).
* refined: for every run directory `<sub>/<label>/run.json` present in both
  trees, the relative difference of `energy` (and of `freeEnergy`, `mu`) and
  the largest absolute difference of the `eps` column of `levels.csv` are
  measured; the check passes when they are below the stated tolerances
  (energies relative 1e-7, eigenvalues absolute 1e-7: the shooting tolerance
  is rtol 1e-12 / atol 1e-14, the regula falsi stops at |Theta - target| <
  1e-11, and the refined run divides both tolerances by 10).

Prints `check_<name>=true|false`, `measurement_<name>=...`, `check_count`,
`failed_check_count`; writes the JSON report {schemaVersion, producer,
checks, measurements, sourceSha256}; exits 1 when any check fails.
"""

import argparse
import csv
import hashlib
import json
import os
import sys

SUBCOMMANDS = ["spectrum", "scf", "excited", "thermo", "emt"]
ENERGY_TOLERANCE = 1.0e-7
EPS_TOLERANCE = 1.0e-7
PRODUCER = "studies/dirac16complex_kohn_sham/tools/compare_runs.py"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def summaries(root):
    out = {}
    for sub in SUBCOMMANDS:
        path = os.path.join(root, sub, "summary.json")
        if os.path.exists(path):
            out[sub] = load_json(path)
    return out


def run_dirs(root, subs):
    runs = []
    for sub in subs:
        base = os.path.join(root, sub)
        if not os.path.isdir(base):
            continue
        for entry in sorted(os.listdir(base)):
            d = os.path.join(base, entry)
            if os.path.isdir(d) and os.path.exists(os.path.join(d, "run.json")):
                runs.append((sub, entry, d))
    return runs


def eps_column(path):
    with open(path, "r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    header = rows[0]
    index = header.index("eps")
    keys = [header.index(name) for name in ("n2", "parity", "s", "index")]
    table = {}
    for row in rows[1:]:
        key = tuple(row[k] for k in keys)
        table[key] = float(row[index])
    return table


def relative(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--canonical", required=True)
    parser.add_argument("--repeat", default=None)
    parser.add_argument("--refined", default=None)
    parser.add_argument("--report", default=None)
    args = parser.parse_args()

    checks = {}
    measurements = {}
    canonical = summaries(args.canonical)
    checks["canonical_summaries_present"] = sorted(canonical) == sorted(SUBCOMMANDS)
    measurements["canonicalSubcommands"] = sorted(canonical)
    verdicts = {sub: s.get("verdict") for sub, s in canonical.items()}
    checks["canonical_verdicts_success"] = bool(verdicts) and all(v == "SUCCESS" for v in verdicts.values())
    measurements["canonicalVerdicts"] = verdicts

    # repeat: byte identity
    if args.repeat and os.path.isdir(args.repeat):
        compared = 0
        differing = []
        for sub, summary in canonical.items():
            for name in summary.get("files", []):
                a = os.path.join(args.canonical, sub, name)
                b = os.path.join(args.repeat, sub, name)
                if not os.path.exists(a) or not os.path.exists(b):
                    differing.append(sub + "/" + name + " (missing)")
                    continue
                compared += 1
                if sha256_file(a) != sha256_file(b):
                    differing.append(sub + "/" + name)
        checks["repeat_byte_identity"] = compared > 0 and not differing
        measurements["repeatFilesCompared"] = compared
        measurements["repeatDifferingFiles"] = differing[:20]
    else:
        checks["repeat_byte_identity"] = False
        measurements["repeatFilesCompared"] = 0
        measurements["repeatDifferingFiles"] = ["no --repeat tree"]

    # refined: tolerance convergence
    if args.refined and os.path.isdir(args.refined):
        worst_energy = 0.0
        worst_free = 0.0
        worst_mu = 0.0
        worst_eps = 0.0
        count = 0
        levels_compared = 0
        details = []
        for sub, label, d in run_dirs(args.canonical, canonical):
            d2 = os.path.join(args.refined, sub, label)
            if not os.path.exists(os.path.join(d2, "run.json")):
                continue
            r1 = load_json(os.path.join(d, "run.json"))
            r2 = load_json(os.path.join(d2, "run.json"))
            count += 1
            e = relative(r1["energy"], r2["energy"])
            f = relative(r1["freeEnergy"], r2["freeEnergy"])
            mu = abs(r1["mu"] - r2["mu"])
            worst_energy = max(worst_energy, e)
            worst_free = max(worst_free, f)
            worst_mu = max(worst_mu, mu)
            worst_level = 0.0
            l1 = os.path.join(d, "levels.csv")
            l2 = os.path.join(d2, "levels.csv")
            if os.path.exists(l1) and os.path.exists(l2):
                t1 = eps_column(l1)
                t2 = eps_column(l2)
                common = set(t1) & set(t2)
                if common:
                    levels_compared += len(common)
                    worst_level = max(abs(t1[k] - t2[k]) for k in common)
                    worst_eps = max(worst_eps, worst_level)
            details.append({"run": sub + "/" + label, "relativeEnergy": e, "relativeFree": f,
                            "absMu": mu, "maxAbsEps": worst_level})
        checks["refined_convergence"] = (count > 0 and worst_energy < ENERGY_TOLERANCE
                                         and worst_free < ENERGY_TOLERANCE
                                         and worst_eps < EPS_TOLERANCE)
        measurements["refinedRunsCompared"] = count
        measurements["refinedLevelsCompared"] = levels_compared
        measurements["refinedMaxRelativeEnergy"] = worst_energy
        measurements["refinedMaxRelativeFreeEnergy"] = worst_free
        measurements["refinedMaxAbsMu"] = worst_mu
        measurements["refinedMaxAbsEps"] = worst_eps
        measurements["refinedEnergyTolerance"] = ENERGY_TOLERANCE
        measurements["refinedEpsTolerance"] = EPS_TOLERANCE
        measurements["refinedDetails"] = details
    else:
        checks["refined_convergence"] = False
        measurements["refinedRunsCompared"] = 0
        measurements["refinedDetails"] = ["no --refined tree"]

    for name, passed in checks.items():
        print("check_%s=%s" % (name, "true" if passed else "false"))
    for name, value in measurements.items():
        if not isinstance(value, list) or len(value) <= 6:
            print("measurement_%s=%s" % (name, json.dumps(value)))
    failed = [name for name, passed in checks.items() if not passed]
    print("check_count=%d" % len(checks))
    print("failed_check_count=%d" % len(failed))
    if args.report:
        source = {}
        for sub, summary in canonical.items():
            source[sub + "/summary.json"] = sha256_file(os.path.join(args.canonical, sub, "summary.json"))
        source["tools/compare_runs.py"] = sha256_file(os.path.abspath(__file__))
        report = {"schemaVersion": 1, "producer": PRODUCER, "checks": checks,
                  "measurements": measurements, "sourceSha256": source}
        os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
        with open(args.report, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(report, indent=2) + "\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
