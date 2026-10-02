#!/usr/bin/env python3
"""Revision/field_equations_a4/python/check_ks_source_conditions.py - do the Kohn-Sham states computed in
Revision/kohn_sham satisfy the conditions that the field equations for a4[x4] (SPEC section 5) impose on a source?

The a4 record (Revision/field_equations_a4/a4-equations.json, checks algebraic_identity_x1_plus_x5_minus_2x8,
x8-dependence, linear_member_equal_pressures) requires of every source of the author's metric:
  (C1) every component independent of x8 (the left-hand sides do not depend on x8),
  (C2) p3 + p_t = 2 p8 (algebraic identity of the Lovelock tensors),
  (C3) for the linear member a4 = A H x4 + a0: p3 = p_t = p8 and rho constant along x4.
This script reads the Kohn-Sham outputs (results of the Rust solver: ground-state profiles in the hidden
coordinate y = ln(sin z)/(6 H), a function of x8 alone, and their integrals) and records, for every state, whether
these conditions hold.  It derives nothing new about the Kohn-Sham states; it only evaluates the stated conditions
on the recorded numbers.  Writes Revision/field_equations_a4/reports/ks-source-conditions.json (deterministic, LF).

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING
extra times; x8 = hidden direction.
"""

import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
A4 = HERE.parent
REV = A4.parent
KS = REV / "kohn_sham" / "results" / "ground"
OUT = A4 / "reports" / "ks-source-conditions.json"
TOL = 1e-6           # relative; the recorded profiles are converged to about 1e-9 of their maxima
CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS " if ok else "FAIL ") + name, flush=True)


def f(x):
    return float(x)


def g6(x):
    return format(x, ".6g")


def main():
    profiles = sorted((KS / "profiles").glob("*.csv"))
    rows = {}
    for p in profiles:
        with p.open(encoding="utf-8", newline="") as fh:
            rows[p.stem] = [{k: f(v) for k, v in r.items()} for r in csv.DictReader(fh)]
    with (KS / "emt-integrals.csv").open(encoding="utf-8", newline="") as fh:
        integ = {r["id"]: r for r in csv.DictReader(fh)}

    trivial, nontrivial = [], []
    var_ratio, alg_ratio = {}, {}
    for sid, rs in rows.items():
        scale = max(max(abs(r[c]) for c in ("rho", "p3", "p_t", "p8")) for r in rs)
        if scale == 0.0:
            trivial.append(sid)
            continue
        nontrivial.append(sid)
        rho = [r["rho"] for r in rs]
        var_ratio[sid] = (max(rho) - min(rho)) / scale
        alg_ratio[sid] = max(abs(r["p3"] + r["p_t"] - 2 * r["p8"]) for r in rs) / scale

    # C1: x8 dependence of every nontrivial profile
    worst1 = min(var_ratio, key=var_ratio.get)
    check("ks_profiles_depend_on_x8", nontrivial and all(v > TOL for v in var_ratio.values()),
          "%d ground-state profiles of Revision/kohn_sham/results/ground/profiles (%d with a nonzero energy-momentum "
          "tensor): for every nonzero one the energy density rho(y) varies along the hidden coordinate y (a function of "
          "x8 alone), (max rho - min rho)/max|T| >= %s (smallest: %s); the a4 equations require every component of the "
          "source to be independent of x8, so none of these states is an admissible source of the author's metric"
          % (len(rows), len(nontrivial), g6(var_ratio[worst1]), worst1))
    # C2: algebraic condition pointwise
    worst2 = min(alg_ratio, key=alg_ratio.get)
    best2 = max(alg_ratio, key=alg_ratio.get)
    ex = rows.get("N136_lam0_a10")
    exs = ""
    if ex:
        def at(yv):
            r = min(ex, key=lambda q: abs(q["y"] - yv))
            return "y = %s: rho = %s, p3 = %s, p_t = %s, p8 = %s, p3 + p_t - 2 p8 = %s" % (
                g6(r["y"]), g6(r["rho"]), g6(r["p3"]), g6(r["p_t"]), g6(r["p8"]), g6(r["p3"] + r["p_t"] - 2 * r["p8"]))
        exs = "; example N136_lam0_a10 (N = 136, lambda = 0, a4,0 = 1): " + " | ".join(at(v) for v in (-3.0, -1.5, 0.0))
    check("ks_profiles_violate_algebraic_condition", all(v > TOL for v in alg_ratio.values()),
          "for every nonzero profile max_y |p3 + p_t - 2 p8| / max|T| lies between %s (%s) and %s (%s): the condition "
          "p3 + p_t = 2 p8 of the a4 equations (algebraic identity E^x1_x1 + E^x5_x5 = 2 E^x8_x8 of the Lovelock "
          "tensors) fails pointwise%s" % (g6(alg_ratio[worst2]), worst2, g6(alg_ratio[best2]), best2, exs))
    # C2 integrated (an averaging over x8 does not rescue it)
    ratios = {}
    for sid in nontrivial:
        r = integ[sid]
        if f(r["int_p8"]) != 0.0:
            ratios[sid] = (f(r["int_p3"]) + f(r["int_p_t"])) / (2 * f(r["int_p8"]))
    dev = {sid: abs(v - 1.0) for sid, v in ratios.items()}
    hist = ", ".join("%s: %s" % (sid, g6(ratios[sid])) for sid in ("N136_lam0_a00", "N136_lam0_a10", "N136_lam0_a20")
                     if sid in ratios)
    check("ks_integrals_violate_algebraic_condition", ratios and len(ratios) == len(nontrivial) and min(dev.values()) > TOL,
          "integrated over the patch (results/ground/emt-integrals.csv: 2 Vol_7 int e^(6Hy) T dy), (int p3 + int p_t)/"
          "(2 int p8) differs from 1 for every nonzero state (closest to 1: %s at %s); for the history N = 136, lambda = "
          "0: %s - even an x8-averaged (dimensionally reduced) source would violate p3 + p_t = 2 p8"
          % (g6(ratios[min(dev, key=dev.get)]), min(dev, key=dev.get), hist))
    # C3: the history a4 = A H x4 is not a solution with the Kohn-Sham source
    hist_ids = [sid for sid in ("N136_lam0_a00", "N136_lam0_a10", "N136_lam0_a20", "N688_lam0_a00", "N688_lam0_a10",
                                "N688_lam0_a20") if sid in integ]
    vals = {sid: (f(integ[sid]["int_rho"]), f(integ[sid]["int_p3"]), f(integ[sid]["int_p_t"])) for sid in hist_ids}
    rho_const = all(abs(vals[a][0] - vals[b][0]) <= TOL * abs(vals[a][0])
                    for a, b in (("N136_lam0_a00", "N136_lam0_a10"), ("N688_lam0_a00", "N688_lam0_a10")))
    p_equal = all(abs(v[1] - v[2]) <= TOL * max(abs(v[1]), 1.0) for v in vals.values())
    desc = "; ".join("%s: int rho = %s, int p3 = %s, int p_t = %s" % (sid, g6(v[0]), g6(v[1]), g6(v[2]))
                     for sid, v in vals.items())
    check("ks_history_is_a_prescribed_background", len(vals) == 6 and not rho_const and not p_equal,
          "the Kohn-Sham history of Revision/kohn_sham (ks-theory.json adiabaticity.history: a4 = A H x4, A = 1) uses "
          "the linear member, which the a4 equations allow only with p3 = p_t = p8 and constant rho "
          "(linear_member_equal_pressures); along it the Kohn-Sham source has %s: rho changes with a4,0 and p3 != p_t "
          "(dE/da4 = -3 (2 Vol_7) int e^(6Hy) (p3 - p_t) dy, ks-theory.json emt.energyChange). The history is therefore a "
          "PRESCRIBED test-field background without back-reaction, not a solution of the a4 equations with the "
          "Kohn-Sham source; equations of state derived from it are not consequences of the coupled field equations"
          % desc)
    check("ks_zero_source_states_listed", True,
          "%d states have an identically vanishing energy-momentum tensor (zero source; in Einstein gravity the a4 "
          "equations have no vacuum solution for H > 0, check einstein_no_vacuum_solution): %s"
          % (len(trivial), ", ".join(trivial) if trivial else "none"))

    n_pass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
    rep = {
        "report": "Revision/field_equations_a4/reports/ks-source-conditions.json",
        "producer": "Revision/field_equations_a4/python/check_ks_source_conditions.py",
        "spec": "Revision/SPEC.md sections 5 and 7: the Kohn-Sham energy-momentum tensor as a source of the a4 equations",
        "inputs": ["Revision/kohn_sham/results/ground/profiles/*.csv", "Revision/kohn_sham/results/ground/emt-integrals.csv"],
        "conditions": ["C1: every component of the source independent of x8",
                       "C2: p3 + p_t = 2 p8",
                       "C3 (linear member a4 = A H x4 + a0): p3 = p_t = p8 and rho constant"],
        "conclusion": "No Kohn-Sham state recorded in Revision/kohn_sham is an admissible source of the author's metric: "
                      "C1 and C2 fail for every nonzero state (C2 also after integration over x8), and the Kohn-Sham "
                      "history uses the linear member as a prescribed background, without back-reaction.",
        "tolerance": "relative %s" % TOL,
        "summary": {"checks": len(CHECKS), "pass": n_pass, "fail": len(CHECKS) - n_pass},
        "checks": CHECKS,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes((json.dumps(rep, indent=1, ensure_ascii=False) + "\n").encode("utf-8"))
    print("pass %d/%d; wrote %s" % (n_pass, len(CHECKS), OUT))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
