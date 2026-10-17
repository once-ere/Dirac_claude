#!/usr/bin/env python3
"""Revision/field_equations_a4/python/check_ks_source_conditions.py - do the Kohn-Sham states computed in
Revision/kohn_sham satisfy the conditions that the field equations for a4[x4] and b4[x4] (SPEC section 5) impose on
a source?

The metric is the corrected primordial metric of 2026-10-16 (version 2; SPEC section 1): g = diag(e^{-2a4} b4 cot^2 z,
e^{2a4} (x3), -1, -e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real; the Kohn-Sham record is that of the PRESCRIBED
history a4 = H x4, b4 = e^{(4/3) H x4} (b4(0) = 1; Revision/kohn_sham, ks-theory.json adiabaticity).  The a4 record
(Revision/field_equations_a4/a4-equations.json, keys generalSource and exponentialHistory) requires of every source:
  (C1) every component independent of x0 (generalSource.x0_dependence: the left-hand sides are free of x0 for every
       a4 and b4);
  (C2) p0 = p_t (generalSource.hiddenEqualsExtraTimes: the hidden and the extra-time components of the left-hand side
       are equal identically);
  (C3) no off-diagonal component, in particular T^x4_x0 = 0 (generalSource.offDiagonal);
  (C4) on the record's history with the author's weights (alpha_k = w_k/H^(2k), w = (1, 1/32, 1/1152), Lambda = -10)
       the source kappa T - Lambda of exponentialHistory.authorWeights.historySource_kappaT_minus_Lam, a function of
       kk = e^{(2/3) H x4} alone.
This script reads the Kohn-Sham outputs (ground-state profiles in the hidden coordinate y = ln|sin z|/(6 H), a function
of x0 alone, and their integrals; proper densities, b4(0) = 1) and records, for every state, whether these conditions
hold.  It derives nothing new about the Kohn-Sham states; it evaluates the stated conditions on the recorded numbers
and the recorded formulas.  Writes Revision/field_equations_a4/reports/ks-source-conditions.json (deterministic, LF).

The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction; x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the
extra times.  p0 = T^x0_x0 is the hidden-direction pressure, p_t = T^x5_x5 the extra-time pressure.
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
EXACT = 1e-12        # relative: an identity of the recorded numbers up to rounding
CHECKS = []
METRIC = ("the corrected metric of 2026-10-16 (version 2; SPEC section 1): g = diag(e^{-2a4} b4 cot^2 z, e^{2a4} (x3), -1, "
          "-e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real")


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
    beta = sp.Rational(kst["adiabaticity"]["historyBeta"])
    gs, eh = eqs["generalSource"], eqs["exponentialHistory"]
    H = float(params["physics"]["H"])
    L = float(params["physics"]["L_tipCutoff"])
    vol0 = float(params["physics"]["Vol7AtA4Zero"])

    profiles = sorted((KS / "profiles").glob("*.csv"))
    rows = {}
    for p in profiles:
        with p.open(encoding="utf-8", newline="") as fh:
            rows[p.stem] = [{k: f(v) for k, v in r.items()} for r in csv.DictReader(fh)]
    with (KS / "emt-integrals.csv").open(encoding="utf-8", newline="") as fh:
        integ = {r["id"]: r for r in csv.DictReader(fh)}

    trivial, nontrivial = [], []
    var_ratio, c2_ratio = {}, {}
    for sid, rs in rows.items():
        scale = max(max(abs(r[c]) for c in ("rho", "p3", "p_t", "p0")) for r in rs)
        if scale == 0.0:
            trivial.append(sid)
            continue
        nontrivial.append(sid)
        rho = [r["rho"] for r in rs]
        var_ratio[sid] = (max(rho) - min(rho)) / scale
        c2_ratio[sid] = max(abs(r["p0"] - r["p_t"]) for r in rs) / scale

    # C1: x0 dependence of every nonzero profile; the left-hand sides are free of x0 for every a4, b4
    comp_keys = ("constraint_x4", "space_x1_eq_x2_eq_x3", "hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7")
    lhs_free = all(not any(s in gs[k]["input"] for s in ("cc", "tt", "x0")) for k in comp_keys)
    stated = gs["x0_dependence"].startswith("the left-hand sides are free of x0")
    worst1 = min(var_ratio, key=var_ratio.get)
    check("ks_profiles_depend_on_x0", bool(nontrivial) and all(v > TOL for v in var_ratio.values()) and lhs_free and stated,
          "%d ground-state profiles of Revision/kohn_sham/results/ground/profiles (%d with a nonzero energy-momentum tensor): "
          "for every nonzero one the energy density rho(y) varies along the hidden coordinate y (a function of x0 alone), "
          "(max rho - min rho)/max|T| >= %s (smallest: %s); the left-hand sides of the a4 and b4 equations "
          "(a4-equations.json generalSource: x4, x1..x3 and x0 = x5..x7 components) contain no x0, cot z or tan z: %s "
          "(generalSource.x0_dependence: '%s'), so every component of an admissible source is independent of x0 (C1) and "
          "none of these states is an admissible source, for any history"
          % (len(rows), len(nontrivial), g6(var_ratio[worst1]), worst1, lhs_free, gs["x0_dependence"][:60]))

    # C2: p0 = p_t
    holds = sorted(sid for sid, v in c2_ratio.items() if v <= EXACT)
    fails = sorted(sid for sid, v in c2_ratio.items() if v > TOL)
    between = sorted(sid for sid, v in c2_ratio.items() if EXACT < v <= TOL)
    lam0 = sorted(sid for sid in nontrivial if "_lam0_" in sid)
    lamx = sorted(sid for sid in nontrivial if "_lam0_" not in sid)
    stated2 = gs["hiddenEqualsExtraTimes"].endswith("p0 = p_t")
    worst_hold = max((c2_ratio[s] for s in holds), default=0.0)
    least_fail = min(fails, key=c2_ratio.get) if fails else None
    check("ks_hidden_pressure_condition", stated2 and holds == lam0 and fails == lamx and not between,
          "C2: the hidden and the extra-time components of every left-hand side are equal (a4-equations.json "
          "generalSource.hiddenEqualsExtraTimes: '%s'), so a source needs p0 = p_t; a Kohn-Sham state has p0 - p_t = "
          "sum w g f [(eps - v_v) n_o - M_eff s_o - kappa |k| t_o], the kinetic pressure along the hidden direction "
          "(ks-theory.json emt.fieldEquationCondition). It holds to rounding (max_y |p0 - p_t|/max|T| <= %s; largest "
          "%s) for exactly the %d nonzero states with lambda = 0: their occupied orbitals are the fold-band orbitals "
          "(e^{f M y}, 0) with eps = kappa k (and the k = 0 zero modes), whose hidden kinetic pressure vanishes "
          "identically, and e_int = 0; it fails (> %s) for every one of the %d states with lambda != 0 (smallest: %s at "
          "%s): the interaction bends the orbitals; states in between: %s"
          % (gs["hiddenEqualsExtraTimes"][-40:], EXACT, g6(worst_hold), len(lam0), TOL, len(lamx),
             g6(c2_ratio[least_fail]) if least_fail else "none", least_fail, between if between else "none"))

    # C3: no off-diagonal component; the Kohn-Sham states have T^x4_y = 0
    off_ks = kst["emt"]["offDiagonal"]
    check("ks_offdiagonal_condition",
          gs["offDiagonal"].startswith("0 = kappa T^mu_nu for every mu != nu") and off_ks.startswith("T^x4_y = 0 for eigen-orbitals"),
          "C3: the left-hand sides have no off-diagonal component (a4-equations.json generalSource.offDiagonal: '%s...'), so "
          "a source needs T^x4_x0 = 0; the Kohn-Sham eigen-orbitals have it (ks-theory.json emt.offDiagonal: '%s'): C3 "
          "holds for every recorded state; it is C1 (and C2 for lambda != 0) that excludes them"
          % (gs["offDiagonal"][:60], off_ks[:70]))

    # C4: the record's history needs the source of exponentialHistory.authorWeights; compare kappa-independent ratios
    aw = eh["authorWeights"]
    kk = sp.Symbol("kk")
    hsrc = {k: sp.sympify(aw["historySource_kappaT_minus_Lam"][k]["input"], locals={"kk": kk})
            for k in ("minus_rho", "p3", "p0", "pt")}
    lam_c = sp.Integer(-10)
    # kappa T = (kappa T - Lambda) + Lambda: kappa rho = -(minus_rho + Lambda) ... in the convention T^4_4 = -rho
    krho = -(hsrc["minus_rho"] + lam_c)
    kp3, kp0, kpt = hsrc["p3"] + lam_c, hsrc["p0"] + lam_c, hsrc["pt"] + lam_c
    p0_eq_pt = sp.simplify(kp0 - kpt) == 0
    a4s = sorted({f(r["a4"]) for r in integ.values()})
    need = {}
    for a in a4s:
        kv = math.exp((2.0 - float(beta)) * a)          # kk = e^{2 a4}/b4 = e^{(2 - beta) a4}
        need[a] = {"kk": kv, "rho": float(krho.subs(kk, kv)), "p3/rho": float((kp3 / krho).subs(kk, kv)),
                   "p0/rho": float((kp0 / krho).subs(kk, kv)), "pt/rho": float((kpt / krho).subs(kk, kv))}
    # the Kohn-Sham x0 averages per proper volume: int sqrt|g| T / int sqrt|g| = (2 Vol_7 int e^{3Hy} T dy) / cell
    vals = {}
    for sid in sorted(nontrivial):
        r = integ[sid]
        a = f(r["a4"])
        cell = 2.0 * vol0 * math.exp((2.0 * float(beta) - 1.0) * a) * (1.0 - math.exp(-3.0 * H * L)) / (3.0 * H)
        ir = f(r["int_rho"])
        if ir == 0.0:
            continue
        vals[sid] = {"a4": a, "rho_bar": ir / cell, "p3/rho": f(r["int_p3"]) / ir, "p0/rho": f(r["int_p0"]) / ir,
                     "pt/rho": f(r["int_p_t"]) / ir}
    dev = {sid: max(abs(v[k] - need[v["a4"]][k]) for k in ("p3/rho", "p0/rho", "pt/rho")) for sid, v in vals.items()}
    closest = min(dev, key=dev.get)
    signs = all(need[a]["rho"] > 0 for a in a4s)
    hist_ok = ("be = 4/3" in aw["recordHistory"] and p0_eq_pt and bool(vals) and min(dev.values()) > 0.1)
    need_s = "; ".join("a4,0 = %s (kk = %s): kappa rho = %s, p3/rho = %s, p0/rho = p_t/rho = %s" % (
        g6(a), g6(need[a]["kk"]), g6(need[a]["rho"]), g6(need[a]["p3/rho"]), g6(need[a]["p0/rho"])) for a in a4s)
    ex = ["N%s_%s_a%02d" % (int(n), t, int(round(10 * a))) for n in params["particleNumbers"]["values"][1:]
          for t in ("lam0",) for a in (0.0, 1.0, 2.0)]
    ks_s = "; ".join("%s: rho_bar = %s, p3/rho = %s, p0/rho = %s, p_t/rho = %s" % (
        sid, g6(vals[sid]["rho_bar"]), g6(vals[sid]["p3/rho"]), g6(vals[sid]["p0/rho"]), g6(vals[sid]["pt/rho"]))
        for sid in ex if sid in vals)
    check("ks_history_is_a_prescribed_background", hist_ok,
          "the Kohn-Sham history (ks-theory.json adiabaticity.history: a4 = H x4, b4 = e^((4/3) H x4), historyBeta = %s; "
          "a4-equations.json exponentialHistory.authorWeights.recordHistory: '%s') needs, with the author's weights and "
          "Lambda = -10, the x0-independent source kappa T - Lambda of authorWeights.historySource_kappaT_minus_Lam, a "
          "function of kk = e^{(2/3) H x4} with p0 = p_t: %s; kappa rho > 0 at every slice: %s; %s. Its ratios do "
          "not depend on the unknown kappa. The Kohn-Sham source, averaged over x0 per proper volume (the most an "
          "x0-independent source could be), has %s; at every recorded state with a nonzero energy density the ratios "
          "(p3/rho, p0/rho, p_t/rho) differ from the needed ones by at least %s (closest: %s). The history is therefore a "
          "PRESCRIBED test-field background without back-reaction, not a solution of the a4 and b4 equations with the "
          "Kohn-Sham source; equations of state derived from it are not consequences of the coupled field equations"
          % (kst["adiabaticity"]["historyBeta"], aw["recordHistory"], p0_eq_pt, signs, need_s, ks_s,
             g6(min(dev.values())), closest))

    check("ks_zero_source_states_listed", True,
          "%d states have an identically vanishing energy-momentum tensor (zero source): %s (the k = 0 zero modes at "
          "lambda = 0 carry eps = 0, no 3-momentum and no hidden kinetic pressure). A zero source is not admissible on the "
          "history either: the history needs the nonzero source of C4 (a4-equations.json exponentialHistory.authorWeights."
          "vacuum: '%s')"
          % (len(trivial), ", ".join(trivial) if trivial else "none", aw.get("vacuum", "")))

    n_pass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
    rep = {
        "report": "Revision/field_equations_a4/reports/ks-source-conditions.json",
        "producer": "Revision/field_equations_a4/python/check_ks_source_conditions.py",
        "metric": METRIC,
        "spec": "Revision/SPEC.md sections 1, 5 and 7: the Kohn-Sham energy-momentum tensor as a source of the a4 and b4 "
                "equations, on the history a4 = H x4, b4 = e^((4/3) H x4)",
        "inputs": ["Revision/kohn_sham/results/ground/profiles/*.csv", "Revision/kohn_sham/results/ground/emt-integrals.csv",
                   "Revision/kohn_sham/results/parameters.json", "Revision/kohn_sham/ks-theory.json",
                   "Revision/field_equations_a4/a4-equations.json"],
        "conditions": ["C1: every component of the source independent of x0 (for every a4 and b4)",
                       "C2: p0 = p_t (the hidden and the extra-time components of the left-hand sides are equal)",
                       "C3: no off-diagonal component (T^x4_x0 = 0)",
                       "C4 (the history a4 = H x4, b4 = e^((4/3) H x4), the author's weights, Lambda = -10): the source "
                       "kappa T - Lambda of exponentialHistory.authorWeights.historySource_kappaT_minus_Lam (a function of "
                       "kk = e^{(2/3) H x4}, p0 = p_t)"],
        "conclusion": "No Kohn-Sham state recorded in Revision/kohn_sham is an admissible source of the corrected metric: C1 "
                      "fails for every nonzero state, for every a4(x4) and b4(x4); C2 (p0 = p_t) holds exactly for the "
                      "lambda = 0 states and fails for lambda != 0; C3 holds; the states are not the source C4 that the "
                      "history needs (no constant kappa reproduces its ratios).  The Kohn-Sham history a4 = H x4, b4 = "
                      "e^((4/3) H x4) is a prescribed background without back-reaction.",
        "tolerance": "relative %s (failures), %s (identities)" % (TOL, EXACT),
        "summary": {"checks": len(CHECKS), "pass": n_pass, "fail": len(CHECKS) - n_pass},
        "checks": CHECKS,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes((json.dumps(rep, indent=1, ensure_ascii=False) + "\n").encode("utf-8"))
    print("pass %d/%d; wrote %s" % (n_pass, len(CHECKS), OUT))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
