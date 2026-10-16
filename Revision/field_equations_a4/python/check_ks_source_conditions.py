#!/usr/bin/env python3
"""Revision/field_equations_a4/python/check_ks_source_conditions.py - do the Kohn-Sham states computed in
Revision/kohn_sham satisfy the conditions that the field equations for a4[x4] and b4[x4] (SPEC section 5) impose on
a source?

The metric is the author's metric with b4(x4) in the extra-time components (b4 a function of x4, never 1), and the
Kohn-Sham record is that of the history a4 = H x4, b4 = b4(0) e^{(4/3) H x4} (SPEC section 1; Revision/kohn_sham,
moved to this history on 2026-10-16).  The a4 record (Revision/field_equations_a4/a4-equations.json, keys
generalSource and exponentialHistory) requires of every source of the author's metric:
  (C1) every diagonal component independent of x0 (the diagonal left-hand sides do not depend on x0, for every a4
       and b4: generalSource.x0_dependence);
  (C2) kappa (p3 + p_t - 2 p0) = sum_k alpha_k (E^x1_x1 + E^x5_x5 - 2 E^x0_x0) (generalSource.
       identity_x1_plus_x5_minus_2x0); evaluated here on the history with the author's weights, where the right-hand
       side vanishes, so the condition is p3 + p_t = 2 p0;
  (C3) on the history with the author's weights (alpha_k = w_k/H^(2k), w = (1, 1/32, 1/1152), Lambda = -10) the
       constant source kappa (rho, p3, p_t, p0) = 2 (135 - 136 H^2, 3 (44 H^2 - 45), 124 H^2 - 135, 128 H^2 - 135)/27,
       i.e. (-2/27, -2/9, -22/27, -14/27) at H = 1 (exponentialHistory.requiredSource);
  (C4) the off-diagonal pair kappa q40 = cot z (b4'/b4) Q, kappa q04 = -tan z (b4'/b4) Q (generalSource.
       offDiagonal_*); on the history with the author's weights Q = 0, so q40 = q04 = 0 is required.
This script reads the Kohn-Sham outputs (ground-state profiles in the hidden coordinate y = ln(sin z)/(6 H), a
function of x0 alone, and their integrals; the profiles are per Vol_7(a4,0), i.e. the proper densities times
b4(0)^(3/2), which changes no ratio and no x0 dependence) and records, for every state, whether these conditions
hold.  It derives nothing new about the Kohn-Sham states; it evaluates the stated conditions on the recorded numbers
and the recorded formulas.  Writes Revision/field_equations_a4/reports/ks-source-conditions.json (deterministic, LF).

The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction; x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the
exponentially DEFLATING extra times.  p0 = T^x0_x0 is the hidden-direction pressure.
"""

import csv
import json
import math
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
A4 = HERE.parent
REV = A4.parent
KSDIR = REV / "kohn_sham"
KS = KSDIR / "results" / "ground"
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
    eqs = json.loads((A4 / "a4-equations.json").read_text(encoding="utf-8"))
    kst = json.loads((KSDIR / "ks-theory.json").read_text(encoding="utf-8"))
    params = json.loads((KSDIR / "results" / "parameters.json").read_text(encoding="utf-8"))
    beta = float(sp.Rational(kst["adiabaticity"]["historyBeta"]))
    gs, eh = eqs["generalSource"], eqs["exponentialHistory"]
    names = ("ad1", "ad2", "uu", "vv", "alpha1", "alpha2", "alpha3", "Lam", "kappa", "cc", "H", "AA", "be")
    loc = {s: sp.Symbol(s) for s in names}
    Hs = loc["H"]
    weights = {loc["alpha1"]: 1, loc["alpha2"]: sp.Rational(1, 32) / Hs ** 2, loc["alpha3"]: sp.Rational(1, 1152) / Hs ** 4}
    history = {loc["ad1"]: Hs, loc["ad2"]: 0, loc["uu"]: sp.Rational(4, 3) * Hs, loc["vv"]: 0}

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
        scale = max(max(abs(r[c]) for c in ("rho", "p3", "p_t", "p0")) for r in rs)
        if scale == 0.0:
            trivial.append(sid)
            continue
        nontrivial.append(sid)
        rho = [r["rho"] for r in rs]
        var_ratio[sid] = (max(rho) - min(rho)) / scale
        alg_ratio[sid] = max(abs(r["p3"] + r["p_t"] - 2 * r["p0"]) for r in rs) / scale

    # C1: x0 dependence of every nontrivial profile; the diagonal left-hand sides are free of x0 for every a4, b4
    diag_keys = ("constraint_x4", "space_x1_eq_x2_eq_x3", "extraTime_x5_eq_x6_eq_x7", "hidden_x0")
    diag_free = all("cc" not in gs[k]["input"].split("==")[0] for k in diag_keys)
    worst1 = min(var_ratio, key=var_ratio.get)
    check("ks_profiles_depend_on_x0", bool(nontrivial) and all(v > TOL for v in var_ratio.values()) and diag_free,
          "%d ground-state profiles of Revision/kohn_sham/results/ground/profiles (%d with a nonzero energy-momentum "
          "tensor): for every nonzero one the energy density rho(y) varies along the hidden coordinate y (a function of "
          "x0 alone), (max rho - min rho)/max|T| >= %s (smallest: %s); the diagonal left-hand sides of the a4 and b4 "
          "equations (a4-equations.json generalSource, x4, x1..x3, x5..x7 and x0 components) contain no x0 for every "
          "a4(x4) and b4(x4): %s, so every component of an admissible diagonal source is independent of x0 (C1) and none "
          "of these states is an admissible source of the author's metric, for any history"
          % (len(rows), len(nontrivial), g6(var_ratio[worst1]), worst1, diag_free))

    # C2 on the history: the general identity with the author's weights
    ident = sp.sympify(gs["identity_x1_plus_x5_minus_2x0"]["input"].split("==")[0], locals=loc)
    ident_hist = sp.simplify(ident.subs(history).subs(weights))
    worst2 = min(alg_ratio, key=alg_ratio.get)
    best2 = max(alg_ratio, key=alg_ratio.get)
    ex = rows.get("N136_lam0_a10")
    exs = ""
    if ex:
        def at(yv):
            r = min(ex, key=lambda q: abs(q["y"] - yv))
            return "y = %s: rho = %s, p3 = %s, p_t = %s, p0 = %s, p3 + p_t - 2 p0 = %s" % (
                g6(r["y"]), g6(r["rho"]), g6(r["p3"]), g6(r["p_t"]), g6(r["p0"]), g6(r["p3"] + r["p_t"] - 2 * r["p0"]))
        exs = ("; example N136_lam0_a10 (N = 136, lambda = 0, a4,0 = 1; densities per Vol_7(a4,0)): "
               + " | ".join(at(v) for v in (-3.0, -1.5, 0.0)))
    check("ks_profiles_violate_algebraic_condition", ident_hist == 0 and all(v > TOL for v in alg_ratio.values()),
          "C2 for general b4: kappa (p3 + p_t - 2 p0) = sum_k alpha_k (E^x1_x1 + E^x5_x5 - 2 E^x0_x0) (a4-equations.json "
          "generalSource.identity_x1_plus_x5_minus_2x0); on the history a4 = H x4, b4 = b4(0) e^((4/3) H x4) with the "
          "author's weights the right-hand side is %s, so the condition is p3 + p_t = 2 p0; for every nonzero profile "
          "max_y |p3 + p_t - 2 p0| / max|T| lies between %s (%s) and %s (%s): it fails pointwise%s"
          % (ident_hist, g6(alg_ratio[worst2]), worst2, g6(alg_ratio[best2]), best2, exs))
    # C2 integrated (an averaging over x0 does not rescue it)
    ratios = {}
    for sid in nontrivial:
        r = integ[sid]
        if f(r["int_p0"]) != 0.0:
            ratios[sid] = (f(r["int_p3"]) + f(r["int_p_t"])) / (2 * f(r["int_p0"]))
    dev = {sid: abs(v - 1.0) for sid, v in ratios.items()}
    hist = ", ".join("%s: %s" % (sid, g6(ratios[sid])) for sid in ("N136_lam0_a00", "N136_lam0_a10", "N136_lam0_a20")
                     if sid in ratios)
    check("ks_integrals_violate_algebraic_condition", bool(ratios) and len(ratios) == len(nontrivial) and min(dev.values()) > TOL,
          "integrated over the patch (results/ground/emt-integrals.csv: 2 Vol_7 int e^(6Hy) T dy), (int p3 + int p_t)/"
          "(2 int p0) differs from 1 for every nonzero state (closest to 1: %s at %s); for the history N = 136, lambda = "
          "0: %s - even an x0-averaged (dimensionally reduced) source would violate p3 + p_t = 2 p0"
          % (g6(ratios[min(dev, key=dev.get)]), min(dev, key=dev.get), hist))

    # C3: the history needs the constant source; the Kohn-Sham states along it are not that source
    req = {}
    for k in ("rho", "p3", "pt", "p0"):
        e = sp.sympify(eh["requiredSource"][k]["input"], locals=loc)
        req[k] = sp.simplify(e.subs({loc["AA"]: 1, loc["be"]: sp.Rational(4, 3), loc["Lam"]: -10}).subs(weights)
                             * loc["kappa"])
    req1 = {k: v.subs(Hs, 1) for k, v in req.items()}
    expected = {"rho": sp.Rational(-2, 27), "p3": sp.Rational(-2, 9), "pt": sp.Rational(-22, 27), "p0": sp.Rational(-14, 27)}
    req_ok = all(sp.simplify(req1[k] - expected[k]) == 0 for k in expected)
    vol0 = params["physics"]["Vol7AtA4Zero"]
    hist_ids = [sid for sid in ("N136_lam0_a00", "N136_lam0_a10", "N136_lam0_a20", "N688_lam0_a00", "N688_lam0_a10",
                                "N688_lam0_a20") if sid in integ]
    vals = {}
    for sid in hist_ids:
        r = integ[sid]
        a4v = f(r["a4"])
        # x0 average of the proper densities in units of b4(0)^(-3/2): the integral over the cell divided by the
        # cell volume 2 Vol_7(a4,0) int_{-L}^0 e^{6Hy} dy, Vol_7(a4,0) = Vol_7(0) e^{(3/2) beta a4,0}
        cell = 2.0 * vol0 * math.exp(1.5 * beta * a4v) * (1.0 - math.exp(-6.0 * 3.0)) / 6.0
        vals[sid] = {"a4": a4v, "rho_bar": f(r["int_rho"]) / cell, "p3/rho": f(r["int_p3"]) / f(r["int_rho"]),
                     "pt/rho": f(r["int_p_t"]) / f(r["int_rho"]), "p0/rho": f(r["int_p0"]) / f(r["int_rho"])}
    positive = all(v["rho_bar"] > 0 for v in vals.values())
    ratios_off = all(abs(v["p3/rho"] - 3) > 1 and abs(v["pt/rho"] - 11) > 1 and abs(v["p0/rho"] - 7) > 1 for v in vals.values())
    changes = all(abs(vals[a]["rho_bar"] - vals[b]["rho_bar"]) > TOL * abs(vals[a]["rho_bar"])
                  for a, b in (("N136_lam0_a00", "N136_lam0_a10"), ("N688_lam0_a00", "N688_lam0_a10")))
    desc = "; ".join("%s: rho_bar = %s, p3/rho = %s, p_t/rho = %s, p0/rho = %s" % (
        sid, g6(v["rho_bar"]), g6(v["p3/rho"]), g6(v["pt/rho"]), g6(v["p0/rho"])) for sid, v in vals.items())
    check("ks_history_is_a_prescribed_background", req_ok and len(vals) == 6 and positive and ratios_off and changes,
          "the Kohn-Sham history of Revision/kohn_sham (ks-theory.json adiabaticity.history: a4 = H x4, b4 = b4(0) "
          "e^((4/3) H x4), historyBeta = %s) needs, with the author's weights and Lambda = -10 (a4-equations.json "
          "exponentialHistory.requiredSource at AA = 1, be = 4/3), the constant source kappa (rho, p3, p_t, p0) = (%s, %s, "
          "%s, %s) (H = 1; for general H: %s, %s, %s, %s): a negative energy density, constant in x4 and x0, with "
          "p3/rho = 3, p_t/rho = 11, p0/rho = 7 (C3, reproduced: %s). Along the history the Kohn-Sham source has (x0 "
          "averages per proper cell volume, in units of b4(0)^(-3/2)) %s: rho_bar > 0, it changes with a4,0 and its "
          "ratios are far from (3, 11, 7). The history is therefore a PRESCRIBED test-field background without "
          "back-reaction, not a solution of the a4 and b4 equations with the Kohn-Sham source; equations of state "
          "derived from it are not consequences of the coupled field equations"
          % (kst["adiabaticity"]["historyBeta"], req1["rho"], req1["p3"], req1["pt"], req1["p0"], req["rho"], req["p3"],
             req["pt"], req["p0"], req_ok, desc))

    # C4: the off-diagonal condition on the history
    Q = sp.sympify(eh["authorWeights"]["Q"]["input"], locals=loc)
    Q_hist = sp.simplify(Q.subs({loc["AA"]: 1, loc["be"]: sp.Rational(4, 3)}))
    q_einstein = eqs["einstein"]["offDiagonal_x4x0"]["input"]
    off_ks = kst["emt"]["offDiagonal"]
    check("ks_offdiagonal_condition_on_history",
          Q_hist == 0 and "cc" in gs["offDiagonal_x4x0"]["input"] and off_ks.startswith("T^x4_y = 0 for eigen-orbitals"),
          "C4: kappa q40 = cot z (b4'/b4) Q (a4-equations.json generalSource.offDiagonal_x4x0); with the author's weights "
          "Q = %s on the history (exponentialHistory.authorWeights.Q at AA = 1, be = 4/3: the reason why beta = 4/3), so "
          "q40 = q04 = 0 is required, and the Kohn-Sham states have it (ks-theory.json emt.offDiagonal: '%s'): the "
          "off-diagonal condition holds on the history; it is the diagonal conditions C1 to C3 that exclude the states. "
          "In Einstein gravity (%s) a source with q40 = 0 forces b4' = 0, which the history excludes"
          % (Q_hist, off_ks[:60], q_einstein))

    check("ks_zero_source_states_listed", True,
          "%d states have an identically vanishing energy-momentum tensor (zero source): %s. A zero source is not "
          "admissible on the history either: with the author's weights every vacuum solution has b4 constant "
          "(a4-equations.json key b4.background; b4 is never constant here), and in Einstein gravity the equations have "
          "no vacuum solution for H > 0 (einstein.noVacuum)"
          % (len(trivial), ", ".join(trivial) if trivial else "none"))

    n_pass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
    rep = {
        "report": "Revision/field_equations_a4/reports/ks-source-conditions.json",
        "producer": "Revision/field_equations_a4/python/check_ks_source_conditions.py",
        "spec": "Revision/SPEC.md sections 1, 5 and 7: the Kohn-Sham energy-momentum tensor as a source of the a4 and b4 "
                "equations, on the history a4 = H x4, b4 = b4(0) e^((4/3) H x4)",
        "inputs": ["Revision/kohn_sham/results/ground/profiles/*.csv", "Revision/kohn_sham/results/ground/emt-integrals.csv",
                   "Revision/kohn_sham/results/parameters.json", "Revision/kohn_sham/ks-theory.json",
                   "Revision/field_equations_a4/a4-equations.json"],
        "conditions": ["C1: every diagonal component of the source independent of x0 (for every a4 and b4)",
                       "C2: kappa (p3 + p_t - 2 p0) = sum_k alpha_k (E^x1_x1 + E^x5_x5 - 2 E^x0_x0); on the history with "
                       "the author's weights: p3 + p_t = 2 p0",
                       "C3 (the history a4 = H x4, b4 = b4(0) e^((4/3) H x4), the author's weights, Lambda = -10): the "
                       "constant source kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27) at H = 1",
                       "C4 (off-diagonal): kappa q40 = cot z (b4'/b4) Q; on the history Q = 0, so q40 = q04 = 0"],
        "conclusion": "No Kohn-Sham state recorded in Revision/kohn_sham is an admissible source of the author's metric: "
                      "C1 fails for every nonzero state, for every a4(x4) and b4(x4); on the history C2 fails pointwise and "
                      "after integration over x0, and the states are not the constant source C3 that the history needs "
                      "(they have positive energy density changing with a4); the off-diagonal condition C4 holds.  The "
                      "Kohn-Sham history a4 = H x4, b4 = b4(0) e^((4/3) H x4) is a prescribed background without "
                      "back-reaction.",
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
