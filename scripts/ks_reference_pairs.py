#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Stage-5 reference runs of the {+M, -M} pairs (STAGE5_SPEC T4).

The independent numpy reference solver (scripts/ks_reference_solver.py, with
its Stage-5 options: negative bare mass, statistics sign, the transformed tip
bag) computes, for both fields, the Kohn-Sham ground and first excited states
of three universes per parameter set:

  plusM    the Stage-4 problem: mass +m, tip bag theta = 0 (g(-L) = 0; the Rust
           crate's b(-L) = 0), both Z2 parity sectors (parity 0), coupling lambda;
  minusM   the -M universe of the exact map T3 (pairing-theory.json,
           T3.numericsPrescription.minusMTransformed): bare mass -m, the SAME
           lambda and statistics, the transformed tip bag theta = pi
           (f(-L) = 0; Rust a(-L) = 0), both parity sectors (the parity
           sectors are exchanged by the map, so "both" is mapped onto "both");
  minusM_control  the -M universe with the UNTRANSFORMED tip bag (bare mass -m,
           g(-L) = 0; T3.untransformedBCControl): expected NOT to pair.
(the universe names of the Rust pairs subcommand, studies/dirac16complex_kohn_sham/src/pairs.rs)

Fields: "d16c" = dirac16complex (anticommuting; the Stage-4 functional,
e_x = -(lambda/32)(n^2 + S^2), M_eff = m + (15/16) lambda S_p, v_x = -lambda
n_p/16) and "d16c00" = dirac16complex00 (commuting, statistics sign +1:
e_x = +(lambda/32)(n^2 + S^2), M_eff = m + (17/16) lambda S_p, v_x = +lambda
n_p/16; the same numerical lambda_hat as dirac16complex).

Run matrix (the matrix of the Rust pairs subcommand, pairs.rs `matrix`; the
checker matches Rust and reference runs by their PARAMETERS (field, universe,
|m|, L, N, lambda, T/|m|), the labels are in addition the same):
  (|m|, N) in {(1, 8), (1, 112), (3, 8), (3, 112)} (the closed shells of the
  Stage-4 reference: N_mid = N_mid(m = 3) = 112), L = 3, a4_0 = 0,
  Delta k = 0.25 |m|, xc "quadratic";
  lambda in {lam0, lamp1, lamm1, lamp2, lamm2} = {0, +-lambda_hat_1,
  +-lambda_hat_2} with the Stage-4 reference couplings of (|m|, 3, N)
  (artifacts/dirac16complex/kohn-sham/reference/couplings/*.json, read only;
  lambda = lambda_hat/m^6 is even in m, so the minus and control universes
  carry the same lambda as the plus universe);
  T = 0 (tasks "excited": KS gap, particle-hole list with the occupation floor
  1e-12, Delta-SCF) for every configuration, and T = 0.1 |m| (task "thermo":
  E, F, S, mu, C_V as in Stage 4) for the configurations with N in
  THERMO_N (default N = N_mid = 112, "one N", as the Rust THERMAL_N);
  grids as in Stage 4: N0 = 60 (m = 1) and 120 (m = 3), levels N0, 2 N0,
  4 N0, (h^2, h^3) extrapolation.
Labels (the Rust pairs labels): <field>_m<|m|>_L<L>_N<N>_<lambda>_T<T/|m|>/<universe>
('p' = decimal point), e.g. d16c00_m3_L3_N112_lamp2_T0/minusM or
d16c_m1_L3_N112_lam0_T0p1/plusM; the run directory is <output>/<label>.

Outputs (deterministic, LF): artifacts/dirac16complex/pair-creation/reference/
<config>/<universe>/{spectrum.csv, profiles.csv, scf-history-level*.csv, run.json} in the
Stage-4 reference formats (run.json carries in addition a "pairs" record:
field, universe, statistics, bag angle, partner label, coupling source) and
reference-pairs-summary.json.  The pairing identities, the control and the
pair totals are evaluated by scripts/check_dirac16complex_pairs.py.

Usage: python scripts/ks_reference_pairs.py [--output DIR] [--workers W]
       [--resume] [--runs LABEL,...] [--thermo-n 112] [--quick]
       [--only-fields d16c,d16c00] [--only-universes plusM,minusM,minusM_control]
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import math
import os
import sys
import time
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ks_reference_solver as KS  # noqa: E402  (sets the BLAS thread variables before numpy loads)

REPO = KS.REPO
ART = os.path.join(REPO, "artifacts", "dirac16complex", "pair-creation")
DEFAULT_OUTPUT = os.path.join(ART, "reference")
STAGE4_COUPLINGS = os.path.join(REPO, "artifacts", "dirac16complex", "kohn-sham", "reference", "couplings")
PAIRING_THEORY = os.path.join(ART, "pairing-theory.json")
PRODUCER = "scripts/ks_reference_pairs.py"
SCHEMA_VERSION = 1
SUMMARY_NAME = "reference-pairs-summary.json"

FIELDS = {"d16c": "anticommuting", "d16c00": "commuting"}
FIELD_NAMES = {"d16c": "dirac16complex", "d16c00": "dirac16complex00"}
# universe -> (sign of the bare mass, tip condition of the reference solver, bag angle theta)
UNIVERSES = {"plusM": (1.0, "g0", 0.0), "minusM": (-1.0, "f0", math.pi), "minusM_control": (-1.0, "g0", 0.0)}
UNIVERSE_TEXT = {
    "plusM": "+M universe: the Stage-4 problem (mass +m, tip bag theta = 0: g(-L) = 0, Rust b(-L) = 0)",
    "minusM": "-M universe with the transformed boundary conditions (mass -m, the same lambda and statistics, "
             "tip bag theta = pi: f(-L) = 0, Rust a(-L) = 0, both parity sectors)",
    "minusM_control": "-M universe with the untransformed boundary conditions (mass -m, tip bag theta = 0: g(-L) = 0); "
               "the control of T3.untransformedBCControl",
}
CONFIGS = ((1.0, 8.0), (1.0, 112.0), (3.0, 8.0), (3.0, 112.0))
L_PAIRS = 3.0
LAMBDAS = ("lam0", "lamp1", "lamm1", "lamp2", "lamm2")
LAMBDA_OF = {"lam0": None, "lamp1": (1.0, "lambdaHat1"), "lamm1": (-1.0, "lambdaHat1"),
             "lamp2": (1.0, "lambdaHat2"), "lamm2": (-1.0, "lambdaHat2")}
THERMO_T_OVER_M = 0.1
THERMO_N = (112.0,)
# Stage-4 first-order rule (ks_reference_solver.THERMO_FIRST_ORDER_LIMIT, the Rust runs.rs rule): the
# pseudo-potential |lambda_hat| strength_free(T) of an interacting T > 0 point in units of |m|, with
# strength_free(T) of the lambda = 0 plusM run of the same field at the same T.  STAGE4_SPEC section 4 window
# edge: 1 |m| (lambda_hat_2 is calibrated to it at T = 0).  Measured (2026-09-30): |m| = 1, N = 112, T = 0.1:
# 0.107 (lambda_hat_1) and 1.07 (lambda_hat_2); |m| = 3, N = 112, T = 0.3: 84.1 and 841.  The m = 3 points were
# attempted first: their SCF widened the energy window to +-137 |m| and a single attempt committed 167 GB of
# memory before failing (the free thermal state at T = 0.1 |m| carries a tip density e^{6HL} times larger than
# the brane-localised T = 0 state that calibrates lambda_hat).  Interacting T > 0 points with an estimate above
# ATTEMPT_LIMIT are therefore NOT attempted and are recorded with their estimates; every limit between 1.08 and
# 84 |m| selects the same points
THERMO_FIRST_ORDER_LIMIT = KS.THERMO_FIRST_ORDER_LIMIT
ATTEMPT_LIMIT = 10.0
# execution guard of every pairs run (ks_reference_solver.Params.window_cap): an SCF whose energy window would
# reach beyond WINDOW_CAP |m| aborts instead of widening further (it cannot change the numbers of a run)
WINDOW_CAP = 20.0
QUICK = {"configs": ((1.0, 8.0),), "lambdas": ("lam0", "lamp1"), "thermoN": (), "N0": KS.QUICK_N0,
         "levels": KS.QUICK_LEVELS}


def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def rel_path(path):
    return os.path.relpath(path, REPO).replace(os.sep, "/")


def config_label(field, m_abs, L, N, lam_name, t_over_m):
    """<field>_m<|m|>_L<L>_N<N>_<lambda>_T<T/|m|>: the Rust pairs configuration label (pairs.rs Config::label)."""
    return "%s_m%s_L%s_N%d_%s_T%s" % (field, KS.trim_float(m_abs), KS.trim_float(L), int(N), lam_name,
                                      "0" if t_over_m == 0 else KS.trim_float(t_over_m))


def pair_label(field, universe, m_abs, L, N, lam_name, t_over_m):
    """<config>/<universe>: the relative run label of the Rust pairs outputs."""
    return config_label(field, m_abs, L, N, lam_name, t_over_m) + "/" + universe


def coupling_record(m_abs, L, N):
    """The Stage-4 reference coupling of the configuration (|m|, L, N) (read only)."""
    path = os.path.join(STAGE4_COUPLINGS, KS.coupling_label(m_abs, L, N) + ".json")
    with open(path, "r", encoding="utf-8") as handle:
        rec = json.load(handle)
    if rec.get("failed") or not (rec.get("m") == m_abs and rec.get("L") == L and rec.get("N") == N):
        raise RuntimeError("Stage-4 coupling record %s unusable" % path)
    return {"configuration": [m_abs, L, N], "lambdaHat1": rec["lambdaHat1"], "lambdaHat2": rec["lambdaHat2"],
            "strengthPerUnitLambdaHat": rec["strengthPerUnitLambdaHat"], "source": rel_path(path),
            "sha256": sha256_file(path), "solverVersion": rec.get("solverVersion")}


def lambda_hat_of(lam_name, coupling):
    sym = LAMBDA_OF[lam_name]
    if sym is None:
        return 0.0
    sign, key = sym
    return sign * coupling[key]


def pair_specs(quick=False, thermo_n=THERMO_N, fields=None, universes=None):
    """The run specifications of the pairs matrix (plain dicts, deterministic order)."""
    configs = QUICK["configs"] if quick else CONFIGS
    lambdas = QUICK["lambdas"] if quick else LAMBDAS
    thermo = QUICK["thermoN"] if quick else tuple(thermo_n)
    specs = []
    for field in (fields or tuple(FIELDS)):
        for m_abs, N in configs:
            temps = [0.0] + ([THERMO_T_OVER_M] if N in thermo else [])
            for t_over_m in temps:
                for lam_name in lambdas:
                    plus_label = pair_label(field, "plusM", m_abs, L_PAIRS, N, lam_name, t_over_m)
                    for universe in (universes or tuple(UNIVERSES)):
                        sign, tip, theta = UNIVERSES[universe]
                        m = sign * m_abs
                        n0 = (QUICK["N0"] if quick else KS.CANONICAL_N0) * (2 if m_abs > 2.0 else 1)
                        specs.append({
                            "label": pair_label(field, universe, m_abs, L_PAIRS, N, lam_name, t_over_m),
                            "configLabel": config_label(field, m_abs, L_PAIRS, N, lam_name, t_over_m),
                            "field": field, "universe": universe, "statistics": FIELDS[field],
                            "m": m, "L": L_PAIRS, "N": N, "T": t_over_m * m_abs, "tOverM": t_over_m, "tip": tip,
                            "bagAngleTheta": theta, "lambda": lam_name, "coupling": [m_abs, L_PAIRS, N],
                            "tasks": ["excited"] if t_over_m == 0.0 else ["thermo"],
                            "N0": n0, "levels": QUICK["levels"] if quick else KS.CANONICAL_LEVELS,
                            "partner": plus_label})
    return specs


def params_of(spec, lambda_hat):
    """Solver parameters of a pairs specification (Stage-4 defaults otherwise)."""
    return KS.Params(m=spec["m"], a4=0.0, L=spec["L"], lambda_hat=lambda_hat, T=spec["T"], N=spec["N"],
                     parity=0, tip=spec["tip"], xc="quadratic", N0=spec["N0"], levels=spec["levels"],
                     label=spec["label"], statistics=spec["statistics"], window_cap=WINDOW_CAP)


def pairs_record(spec, coupling):
    return {"field": spec["field"], "fieldName": FIELD_NAMES[spec["field"]], "universe": spec["universe"],
            "universeDescription": UNIVERSE_TEXT[spec["universe"]], "statistics": spec["statistics"],
            "statisticsSign": KS.STATISTICS_SIGNS[spec["statistics"]], "massSign": 1 if spec["m"] > 0 else -1,
            "massScale": abs(spec["m"]), "tip": spec["tip"], "bagAngleTheta": spec["bagAngleTheta"],
            "tOverM": spec["tOverM"], "partnerLabel": spec["partner"], "configLabel": spec["configLabel"],
            "couplingSource": {k: coupling[k] for k in ("configuration", "source", "sha256")}}


def execute_pair_run(spec, coupling, output_root, log):
    """One pairs run: SectorRun (T = 0, with the excited tasks) or thermo_point
    (T > 0), written with KS.write_run in the Stage-4 reference formats."""
    lambda_hat = lambda_hat_of(spec["lambda"], coupling)
    params = params_of(spec, lambda_hat)
    tasks = spec["tasks"]
    log("run %s: %s" % (spec["label"], json.dumps(KS.jsonable(params.to_dict()))))
    t0 = time.time()
    extra = {}
    if params.T > 0 and "thermo" in tasks:
        point = KS.thermo_point(params, params.T, log=log)
        run = point.pop("run")
        extra["thermo"] = point
    else:
        run = KS.SectorRun(params, log=log)
    if "excited" in tasks and params.T <= 0:
        fine = run.levels[-1]
        if not run.converged or fine.get("convergedBy") == "collapse":
            extra["excited"] = {"ksGap": run.gap, "particleHole": [],
                                "deltaSCF": {"available": False,
                                             "reason": "ground state not converged (%s): no excited state computed"
                                                       % fine.get("convergedBy")}}
        else:
            try:
                ph = KS.particle_hole_list(run)
            except Exception as error:  # noqa: BLE001
                ph = []
                log("  particle-hole list failed: %r" % (error,))
            try:
                ds = KS.delta_scf(run, log=log)
            except Exception as error:  # noqa: BLE001
                ds = {"available": False, "reason": "Delta-SCF failed: %r" % (error,)}
                log("  Delta-SCF failed: %r" % (error,))
            extra["excited"] = {"ksGap": run.gap, "particleHole": ph, "deltaSCF": ds}
    extra["tasks"] = tasks
    extra["lambdaName"] = spec["lambda"]
    extra["couplingConfiguration"] = spec["coupling"]
    extra["pairs"] = pairs_record(spec, coupling)
    doc = KS.write_run(run, os.path.join(output_root, spec["label"]), extra)
    log("  -> %s: E0 = %.12f  mu = %.10f  converged = %s  gap = %s  (%.0f s)"
        % (spec["label"], run.scalars["total"], run.scalars["mu"], run.converged, run.gap, time.time() - t0))
    return doc


def execute_pair_worker(spec, coupling, output_root):
    label = spec["label"]

    def log(msg):
        print("[%s] %s" % (label, msg), flush=True)
    try:
        return execute_pair_run(spec, coupling, output_root, log)
    except Exception as error:  # noqa: BLE001
        log("FAILED: %r\n%s" % (error, traceback.format_exc()))
        return {"params": {"label": label}, "failed": repr(error), "converged": False,
                "pairs": pairs_record(spec, coupling)}


MATCH_KEYS = ("m", "a4_0", "L", "lambda_hat", "T", "N", "parity", "tip", "xc", "sea", "delta_k", "ell", "N0",
              "levels", "tol", "solverVersion")


def run_matches(doc, spec, coupling):
    """Does an existing run.json reproduce the specification (--resume)?"""
    try:
        p = doc["params"]
        q = params_of(spec, lambda_hat_of(spec["lambda"], coupling)).to_dict()
        same = all(p.get(k) == q[k] for k in MATCH_KEYS)
        same = same and p.get("statistics", KS.DEFAULT_STATISTICS) == q.get("statistics", KS.DEFAULT_STATISTICS)
        if "excited" in spec["tasks"] and "excited" not in doc:
            return False
        if "thermo" in spec["tasks"] and "thermo" not in doc:
            return False
        if (doc.get("pairs") or {}).get("universe") != spec["universe"]:
            return False
        collapsed = (doc.get("levels") or [{}])[-1].get("convergedBy") == "collapse"
        return bool(same and (doc.get("converged") or collapsed))
    except Exception:  # noqa: BLE001
        return False


def summary_record(doc, spec):
    if doc.get("notAttempted"):
        rec = {"label": spec["label"], "converged": False, "notAttempted": doc["notAttempted"],
               "firstOrder": doc.get("firstOrder")}
    elif doc.get("failed"):
        rec = {"label": spec["label"], "converged": False, "failed": doc.get("failed")}
    else:
        rec = KS.summary_record(doc)
    rec["pairs"] = doc.get("pairs")
    rec["field"] = spec["field"]
    rec["universe"] = spec["universe"]
    return rec


def thermo_first_order(specs, docs, couplings):
    """{label: record} of the first-order pseudo-potential of every interacting T > 0 point:
    |lambda_hat| strength_free(T), strength_free(T) = couplingScale.strengthPerUnitLambdaHat of the
    lambda = 0 run of the plusM universe at the same (field, |m|, N, T) (per |m|^7, in units of |m|)."""
    out = {}
    for s in specs:
        if s["T"] <= 0.0 or s["lambda"] == "lam0":
            continue
        src = pair_label(s["field"], "plusM", abs(s["m"]), s["L"], s["N"], "lam0", s["tOverM"])
        doc = docs.get(src) or {}
        strength = (doc.get("couplingScale") or {}).get("strengthPerUnitLambdaHat")
        lh = lambda_hat_of(s["lambda"], couplings[tuple(s["coupling"])])
        est = abs(lh) * strength if isinstance(strength, float) else None
        out[s["label"]] = {"freeSource": src, "strengthFree": strength, "lambdaHat": lh,
                           "firstOrderPseudoPotentialOverAbsM": est, "windowEdge": THERMO_FIRST_ORDER_LIMIT,
                           "outsideWindow": bool(est is not None and est > THERMO_FIRST_ORDER_LIMIT),
                           "attemptLimit": ATTEMPT_LIMIT,
                           "attempted": bool(est is not None and est <= ATTEMPT_LIMIT)}
    return out


def readiness(spec, docs, couplings):
    """("run", None) | ("wait", None) | ("skip", record): an interacting T > 0 point waits for the
    lambda = 0 plusM run of its field at the same T and is attempted only if its first-order
    pseudo-potential is <= ATTEMPT_LIMIT |m|."""
    if spec["T"] <= 0.0 or spec["lambda"] == "lam0":
        return "run", None
    rec = thermo_first_order([spec], docs, couplings)[spec["label"]]
    src = docs.get(rec["freeSource"])
    if src is None:
        return "wait", None
    if rec["firstOrderPseudoPotentialOverAbsM"] is None:
        return "skip", dict(rec, reason="free thermal source run %s unavailable (%s)"
                                        % (rec["freeSource"], src.get("failed") or src.get("notAttempted")))
    if not rec["attempted"]:
        return "skip", dict(rec, reason="not attempted: first-order pseudo-potential |lambda_hat| strength_free(T) "
                                        "= %.6g |m| exceeds the attempt limit %g |m| (STAGE4_SPEC section 4 window "
                                        "edge %g |m|)" % (rec["firstOrderPseudoPotentialOverAbsM"], ATTEMPT_LIMIT,
                                                          THERMO_FIRST_ORDER_LIMIT))
    return "run", None


def priority(spec):
    """Longest runs first: m = 3 (grids 120/240/480), the thermo points (three
    SCF solutions each), N = 112, then the rest."""
    return (0 if spec["m"] ** 2 > 4.0 else 1, 0 if spec["T"] > 0.0 else 1, -spec["N"])


def matrix_description(quick, thermo_n, fields, universes):
    return {"fields": {f: FIELD_NAMES[f] + " (" + FIELDS[f] + ")" for f in (fields or tuple(FIELDS))},
            "universes": {u: UNIVERSE_TEXT[u] for u in (universes or tuple(UNIVERSES))},
            "configurations_absM_N": [list(c) for c in (QUICK["configs"] if quick else CONFIGS)],
            "L": L_PAIRS, "a4_0": 0.0, "deltaKOverAbsM": 0.25, "parity": "0 (both Z2 sectors)", "xc": "quadratic",
            "lambdas": list(QUICK["lambdas"] if quick else LAMBDAS),
            "temperatures": {"T0": "tasks excited (KS gap, particle-hole list, Delta-SCF)",
                             "T_over_absM": THERMO_T_OVER_M,
                             "thermoN": list(QUICK["thermoN"] if quick else thermo_n)},
            "grids": ("N0 = %d (|m| = 1), %d (|m| = 3), levels N0, 2 N0, 4 N0" %
                      ((QUICK["N0"] if quick else KS.CANONICAL_N0), 2 * (QUICK["N0"] if quick else KS.CANONICAL_N0))
                      if not quick else "quick: N0 = %d, %d levels" % (QUICK["N0"], QUICK["levels"])),
            "labelScheme": "<field>_m<|m|>_L<L>_N<N>_<lambda>_T<T/|m|>/<universe> (the Rust pairs labels, "
                           "pairs.rs Config::label and write_universe; 'p' = decimal point)",
            "couplingRule": "lambda_hat of the Stage-4 reference coupling of (|m|, L, N) (" + rel_path(STAGE4_COUPLINGS)
                            + "); the same lambda_hat (and lambda = lambda_hat/m^6) in all three universes and for "
                              "both fields",
            "prescription": "pairing-theory.json T3.numericsPrescription (minusMTransformed, "
                            "minusMUntransformedControl)"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--workers", type=int, default=None,
                        help="parallel worker processes (default min(10, cpu/2))")
    parser.add_argument("--resume", action="store_true",
                        help="keep run directories whose run.json already matches the specification")
    parser.add_argument("--runs", default=None, help="comma-separated labels to execute")
    parser.add_argument("--thermo-n", default=None, help="comma-separated N of the T = 0.1 |m| points (default 112)")
    parser.add_argument("--only-fields", default=None, help="comma-separated subset of d16c,d16c00")
    parser.add_argument("--only-universes", default=None,
                        help="comma-separated subset of plusM,minusM,minusM_control")
    parser.add_argument("--quick", action="store_true", help="reduced matrix on coarse grids (smoke test)")
    parser.add_argument("--list", action="store_true", help="print the labels of the matrix and exit")
    parser.add_argument("--keep-failed", action="store_true",
                        help="with --resume: keep the failure records of the previous summary instead of retrying")
    args = parser.parse_args(argv)
    t_start = time.time()

    def log(msg):
        print(msg, flush=True)
    thermo_n = tuple(float(x) for x in args.thermo_n.split(",")) if args.thermo_n else THERMO_N
    fields = tuple(args.only_fields.split(",")) if args.only_fields else None
    universes = tuple(args.only_universes.split(",")) if args.only_universes else None
    for f in fields or ():
        if f not in FIELDS:
            parser.error("unknown field %r" % f)
    for u in universes or ():
        if u not in UNIVERSES:
            parser.error("unknown universe %r" % u)
    specs = pair_specs(args.quick, thermo_n, fields, universes)
    if args.runs:
        wanted = set(args.runs.split(","))
        unknown = sorted(wanted - {s["label"] for s in specs})
        if unknown:
            parser.error("labels not in the matrix: %s" % unknown)
        specs = [s for s in specs if s["label"] in wanted]
    if args.list:
        for s in specs:
            print(s["label"])
        return 0
    couplings = {}
    for s in specs:
        key = tuple(s["coupling"])
        if key not in couplings:
            couplings[key] = coupling_record(*key)
    workers = args.workers if args.workers is not None else max(1, min(10, (os.cpu_count() or 2) // 2))
    os.makedirs(args.output, exist_ok=True)
    summary = {"schemaVersion": SCHEMA_VERSION, "producer": PRODUCER, "solver": "scripts/ks_reference_solver.py",
               "solverVersion": KS.SOLVER_VERSION,
               "sourceSha256": {"scripts/ks_reference_solver.py": sha256_file(os.path.join(HERE, "ks_reference_solver.py")),
                                "scripts/ks_reference_pairs.py": sha256_file(os.path.abspath(__file__)),
                                rel_path(KS.DEFAULT_FIXTURE): sha256_file(KS.DEFAULT_FIXTURE),
                                rel_path(PAIRING_THEORY): (sha256_file(PAIRING_THEORY)
                                                           if os.path.exists(PAIRING_THEORY) else None)},
               "matrix": matrix_description(args.quick, thermo_n, fields, universes),
               "couplings": [couplings[k] for k in sorted(couplings)], "quick": bool(args.quick)}
    docs = {}
    pending = list(specs)
    kept = 0
    if args.resume:
        for spec in list(pending):
            path = os.path.join(args.output, spec["label"], "run.json")
            if not os.path.exists(path):
                continue
            with open(path, "r", encoding="utf-8") as handle:
                doc = json.load(handle)
            if run_matches(doc, spec, couplings[tuple(spec["coupling"])]):
                docs[spec["label"]] = doc
                pending.remove(spec)
                kept += 1
    if args.resume and args.keep_failed and os.path.exists(os.path.join(args.output, SUMMARY_NAME)):
        with open(os.path.join(args.output, SUMMARY_NAME), "r", encoding="utf-8") as handle:
            previous = json.load(handle)
        records = {r.get("label"): r for r in previous.get("runs", [])}
        for spec in list(pending):
            rec = records.get(spec["label"])
            if rec and rec.get("failed") and rec.get("pairs"):
                docs[spec["label"]] = {"params": {"label": spec["label"]}, "failed": rec["failed"],
                                       "converged": False, "pairs": rec["pairs"]}
                pending.remove(spec)
                kept += 1
    log("%d pairs runs (%d kept from a previous run), %d workers" % (len(specs), kept, workers))
    by_label = {s["label"]: s for s in specs}

    def flush(complete):
        summary["runs"] = [summary_record(docs[s["label"]], s) for s in specs if s["label"] in docs]
        summary["failed"] = sorted(lab for lab, d in docs.items() if d.get("failed"))
        first = thermo_first_order(specs, docs, couplings)
        summary["thermoFirstOrder"] = {"rule": "first-order pseudo-potential |lambda_hat| strength_free(T) of an "
                                               "interacting T > 0 point, in units of |m| (strength_free of the "
                                               "lambda = 0 plusM run of the field at that T); STAGE4_SPEC section 4 "
                                               "window edge %g |m|; points above %g |m| are not attempted (see "
                                               "ks_reference_pairs.py ATTEMPT_LIMIT)" % (THERMO_FIRST_ORDER_LIMIT,
                                                                                       ATTEMPT_LIMIT),
                                       "points": first}
        summary["windowCap"] = WINDOW_CAP
        summary["notAttempted"] = sorted(lab for lab, d in docs.items() if d.get("notAttempted"))
        summary["failedControl"] = [lab for lab in summary["failed"] if by_label[lab]["universe"] == "minusM_control"]
        summary["failedOther"] = [lab for lab in summary["failed"] if lab not in summary["failedControl"]]
        summary["notConverged"] = sorted(lab for lab, d in docs.items() if not d.get("failed")
                                         and not d.get("converged"))
        summary["pending"] = sorted(s["label"] for s in specs if s["label"] not in docs)
        summary["complete"] = bool(complete)
        KS.write_json(os.path.join(args.output, SUMMARY_NAME), summary)
    flush(False)
    pending.sort(key=lambda sp: (priority(sp), specs.index(sp)))
    if pending:
        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
            futures = {}

            def submit_ready():
                # at most `workers` runs in flight; an interacting T > 0 point waits for its free source
                while len(futures) < workers:
                    chosen = None
                    for sp in list(pending):
                        state, rec = readiness(sp, docs, couplings)
                        if state == "skip":
                            pending.remove(sp)
                            docs[sp["label"]] = {"params": {"label": sp["label"]}, "notAttempted": rec["reason"],
                                                 "firstOrder": rec, "converged": False,
                                                 "pairs": pairs_record(sp, couplings[tuple(sp["coupling"])])}
                            log("[%s] %s" % (sp["label"], rec["reason"]))
                        elif state == "run" and chosen is None:
                            chosen = sp
                    if chosen is None:
                        return
                    pending.remove(chosen)
                    fut = pool.submit(execute_pair_worker, chosen, couplings[tuple(chosen["coupling"])], args.output)
                    futures[fut] = chosen["label"]
            submit_ready()
            while futures:
                done, _ = concurrent.futures.wait(list(futures), return_when=concurrent.futures.FIRST_COMPLETED)
                for fut in done:
                    docs[futures.pop(fut)] = fut.result()
                submit_ready()
                flush(False)
    for sp in pending:   # a free source never became available
        docs[sp["label"]] = {"params": {"label": sp["label"]}, "failed": "dependency unavailable",
                             "converged": False, "pairs": pairs_record(sp, couplings[tuple(sp["coupling"])])}
    failed = sorted(lab for lab, d in docs.items() if d.get("failed"))
    flush(all(s["label"] in docs for s in specs))
    log("wrote %s in %.1f s (%d runs; failed %s; not attempted %s)"
        % (os.path.join(args.output, SUMMARY_NAME), time.time() - t_start, len(by_label), failed,
           summary["notAttempted"]))
    return 1 if summary["failedOther"] else 0


if __name__ == "__main__":
    sys.exit(main())
