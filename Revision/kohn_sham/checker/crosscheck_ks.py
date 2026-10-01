#!/usr/bin/env python3
"""Cross-check of the Rust Kohn-Sham solver (Revision/kohn_sham/solver, results in Revision/kohn_sham/results)
against the independent Python reference (Revision/kohn_sham/reference, staggered finite differences with
Richardson extrapolation) on the reference subset of the canonical matrix (SPEC section 7).

TOLERANCE RULE (fixed in this file before any comparison; never adjusted to a result):
    |x_Rust - x_ref| <= 3 (U_ref + U_Rust) + 1e-12 * scale
  U_ref  = the reference's measured grid uncertainty (three-grid Richardson, |R - R2|; validated on a fourth
           grid, Revision/kohn_sham/reports/ks-reference.json check richardson_uncertainty_validated);
  U_Rust = (16/15) |canonical - refined| of the Rust solver (RK4: the refined error is 1/16 of the canonical
           one), measured per state and per quantity by checker/measure_rust_refinement.py where the Rust
           `single` command reports the quantity (energies, EMT integrals, levels, profiles, brane and tip
           values, mu, entropy); otherwise the maximum over the whole canonical matrix of
           Revision/kohn_sham/reports/ks-rust-determinism.json (stated in each check);
  scale  = max(1, |x|) for scalars, the profile maximum for profiles (roundoff floor).
Every comparison yields ratio = |x_Rust - x_ref| / tolerance; a check passes when every ratio <= 1.

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially
DEFLATING extra times (scale factor e^{-a4} sin^{1/6} z, a4 increasing); x8 = hidden direction,
y = ln(sin z)/(6H) in [-L, 0].

Usage (from the repository root):
  python Revision/kohn_sham/checker/crosscheck_ks.py [--reference-repeat DIR] [--report FILE] [--table FILE]
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KS = HERE.parent
K_SIGMA = 3.0
FLOOR = 1e-12
RK4_FACTOR = 16.0 / 15.0
PROFILES = ("n", "S", "Q", "M_eff", "v_v", "e_int", "rho", "p3", "p_t", "p8")


def read_csv(p: Path):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def num(x):
    return float("nan") if x in ("null", "", None) else float(x)


def load(p: Path):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def fe(x):
    return "nan" if x is None or not math.isfinite(x) else f"{x:.3e}"


class Check:
    """Aggregated comparison: worst ratio |diff| / tolerance, its case, and every failure."""

    def __init__(self, desc):
        self.desc = desc
        self.n = 0
        self.worst = -1.0
        self.wcase = ""
        self.fails = []
        self.extra = []

    def cmp(self, case, xr, xf, u_ref, u_rust, scale=None, table=None):
        scale = max(1.0, abs(xf)) if scale is None else scale
        tol = K_SIGMA * (u_ref + u_rust) + FLOOR * scale
        d = abs(xr - xf)
        ratio = d / tol if tol > 0 else (0.0 if d == 0 else math.inf)
        if not math.isfinite(xr) or not math.isfinite(xf):
            ratio = math.inf
        self.n += 1
        if ratio > self.worst:
            self.worst, self.wcase = ratio, f"{case}: Rust {xr:.15g}, reference {xf:.15g}, |diff| {fe(d)}, tolerance {fe(tol)}"
        if not ratio <= 1.0:
            self.fails.append(f"{case} (|diff| {fe(d)} > tolerance {fe(tol)}; U_ref {fe(u_ref)}, U_Rust {fe(u_rust)})")
        if table is not None:
            table.append([case, f"{xr:.15e}", f"{xf:.15e}", fe(u_ref), fe(u_rust), fe(tol), fe(d), f"{ratio:.4f}", "PASS" if ratio <= 1.0 else "FAIL"])
        return ratio <= 1.0

    def flag(self, case, ok, why):
        self.n += 1
        if not ok:
            self.fails.append(f"{case} ({why})")

    def detail(self):
        s = f"{self.desc}; {self.n} comparisons"
        if self.worst >= 0:
            s += f"; worst |diff|/tolerance {self.worst:.3f} ({self.wcase})"
        if self.extra:
            s += "; " + "; ".join(self.extra)
        s += f"; failures: {'; '.join(self.fails) if self.fails else 'none'}"
        return s

    def ok(self):
        return not self.fails


def parse_determinism(rep):
    """Matrix-wide canonical - refined maxima of the Rust determinism report (only PASS checks are used)."""
    pats = {
        "refined_ground_energies": r"max relative difference of E_KS ([0-9.eE+-]+)",
        "refined_ground_homo_lumo_gap": r"KS gap ([0-9.eE+-]+) m",
        "refined_eigenvalues": r"max \|difference\| ([0-9.eE+-]+) m",
        "refined_delta_scf": r"excitation energies ([0-9.eE+-]+) m",
        "refined_profiles": r"profile maximum ([0-9.eE+-]+)",
        "refined_adiabatic_derivatives": r"max relative difference ([0-9.eE+-]+)",
        "refined_thermodynamics": r"\): max ([0-9.eE+-]+)",
        "refined_heat_capacity": r"1e-6\)\) ([0-9.eE+-]+)",
    }
    by = {c["name"]: c for c in rep["checks"]}
    out = {}
    for name, pat in pats.items():
        c = by.get(name)
        if c is None or c["verdict"] != "PASS":
            raise SystemExit(f"determinism report: check {name} missing or not PASS")
        m = re.search(pat, c["detail"])
        if not m:
            raise SystemExit(f"determinism report: cannot read the value of {name}")
        out[name] = float(m.group(1).rstrip("."))
    return out


def key_from_label(s, lmin):
    """'n2:+1:even:label' (Rust label) -> 'n2:+1:even:rank' with rank = label - label_min."""
    n2, j, par, lab = s.split(":")
    jj = 1 if j in ("+1", "1") else -1
    return f"{int(n2)}:{'+1' if jj > 0 else '-1'}:{par}:{int(lab) - lmin[(int(n2), jj, par)]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rust", default=str(KS / "results"))
    ap.add_argument("--rust-solver-report", default=str(KS / "reports" / "ks-rust-solver.json"))
    ap.add_argument("--rust-determinism", default=str(KS / "reports" / "ks-rust-determinism.json"))
    ap.add_argument("--rust-refinement", default=str(HERE / "rust-refinement.json"))
    ap.add_argument("--reference", default=str(KS / "reference" / "results"))
    ap.add_argument("--reference-report", default=str(KS / "reports" / "ks-reference.json"))
    ap.add_argument("--reference-repeat", default=None)
    ap.add_argument("--report", default=str(KS / "reports" / "ks-crosscheck.json"))
    ap.add_argument("--table", default=str(KS / "reports" / "ks-crosscheck-table.csv"))
    args = ap.parse_args()
    rust, ref = Path(args.rust), Path(args.reference)
    checks = []
    table = []

    def emit(name, ok, detail):
        checks.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
        print(f"{'PASS' if ok else 'FAIL'} - {name}: {detail[:300]}", file=sys.stderr, flush=True)

    # ---------------------------------------------------------------- inputs
    rrep, srep, drep = load(args.reference_report), load(args.rust_solver_report), load(args.rust_determinism)
    refine = load(args.rust_refinement)
    rf = {s["id"]: s for s in refine["states"]}
    bad = {nm: [c["name"] for c in r["checks"] if c["verdict"] != "PASS"] for nm, r in
           (("ks-reference.json", rrep), ("ks-rust-solver.json", srep), ("ks-rust-determinism.json", drep))}
    runs_bad = [s["id"] for s in refine["states"] if not s["runs_ok"]]
    emit("inputs_all_pass", not any(bad.values()) and not runs_bad,
         f"reference report {rrep['summary']['pass']}/{rrep['summary']['checks']} PASS, Rust solver report {srep['summary']['pass']}/"
         f"{srep['summary']['checks']} PASS, Rust determinism report {drep['summary']['pass']}/{drep['summary']['checks']} PASS; "
         f"failing checks: {bad}; Rust refinement runs (single canonical and refined) failed: {runs_bad if runs_bad else 'none'}")
    G = parse_determinism(drep)
    U_EIG = RK4_FACTOR * G["refined_eigenvalues"]
    U_DSCF = RK4_FACTOR * G["refined_delta_scf"]
    U_ADIAB_REL = RK4_FACTOR * G["refined_adiabatic_derivatives"]
    U_CV_REL = RK4_FACTOR * G["refined_heat_capacity"]
    U_PROF_REL = RK4_FACTOR * G["refined_profiles"]

    # the measured single runs must reproduce the committed canonical matrix
    c_ok, worst = True, {}
    for s in refine["states"]:
        if not s["runs_ok"]:
            c_ok = False
            continue
        for k, v in s["canonical_single_vs_matrix"].items():
            if k == "levels_compared":
                continue
            worst[k] = max(worst.get(k, 0.0), v)
            if v > 1e-12:
                c_ok = False
    emit("rust_refinement_applies_to_matrix", c_ok,
         "the canonical `single` runs of checker/rust-refinement.json reproduce the committed canonical matrix (tolerance 1e-12 for every "
         "class): " + ", ".join(f"{k} {fe(v)}" for k, v in sorted(worst.items())) +
         "; hence |canonical - refined| of these runs measures the error of the committed Rust results")

    # ---------------------------------------------------------------- problem definition and derived inputs
    rp, fp = load(rust / "parameters.json"), load(ref / "parameters.json")
    phys_r, phys_f = rp["physics"], fp["physics"]
    pairs = [("H", "H"), ("m", "m"), ("L_tipCutoff", "L"), ("dk", "dk"), ("v_t", "vt"), ("tipTheta", "tipTheta"),
             ("historyA", "historyA"), ("slicesA4", "slicesA4"), ("temperatures", "temperatures")]
    diffs = [f"{a}: Rust {phys_r[a]} vs reference {phys_f[b]}" for a, b in pairs if phys_r[a] != phys_f[b]]
    same_theory = rp["theoryInputs"]["ksTheorySha256"] == fp["theoryInputs"]["ksTheorySha256"]
    emit("problem_definition_identical", not diffs and same_theory,
         f"H, m, L, dk, v_t, tip angle, history A, slices and temperatures identical: {not diffs} ({diffs if diffs else 'no differences'}); "
         f"both read the same ks-theory.json (sha256 {fp['theoryInputs']['ksTheorySha256'][:16]}): {same_theory}")
    der = fp["derived"]
    pn = rp["particleNumbers"]
    c = Check("particle numbers re-derived by the reference from the stated rules (free a4,0 = 0 aufbau, bulk edge, closed shells)")
    c.flag("N_large", der["N_large"] == pn["N_large"], f"Rust {pn['N_large']}, reference {der['N_large']}")
    c.flag("N_mid", der["N_mid"] == pn["N_mid"], f"Rust {pn['N_mid']}, reference {der['N_mid']}")
    c.flag("N values", sorted([8.0, der["N_mid"], der["N_large"]]) == sorted(pn["values"]), "N sets differ")
    c.cmp("bulk edge", pn["bulkEdge"], der["bulk_edge"]["value"], der["bulk_edge"]["U"], U_EIG, table=table)
    c.extra.append(f"N_large = {int(der['N_large'])}, N_mid = {int(der['N_mid'])} (U_Rust of the bulk edge: matrix-wide eigenvalue maximum {fe(U_EIG)})")
    emit("parameters_particle_numbers", c.ok(), c.detail())
    # couplings
    c = Check("couplings lambda_1, lambda_2 re-derived by the reference (4 significant digits) must be identical; strengths: the Rust value "
              "is the maximum over its fine-grid samples (spacing s = L/(2 x rk4Steps)), the reference value is the continuous maximum "
              "(quartic interpolation), so for an interior maximum 0 <= ref - Rust <= |f''| s^2/8 within 3 (U_ref + U_Rust), with f'' the "
              "reference curvature at the peak; for a maximum at the tip y = -L (a sample point of both) the values must agree; U_Rust = "
              "the matrix-wide profile maximum (16/15) x " + fe(G["refined_profiles"]) + " x strength")
    s_R = phys_r["L_tipCutoff"] / (2.0 * rp["numerics"]["rk4Steps"])
    rcal = {v["N"]: v for v in rp["couplingCalibration"]["values"]}
    for cal in der["calibration"]:
        r = rcal[cal["N"]]
        c.flag(f"N = {int(cal['N'])} lambda_1", cal["lambda1"] == r["lambda1"], f"Rust {r['lambda1']}, reference {cal['lambda1']}")
        c.flag(f"N = {int(cal['N'])} lambda_2", cal["lambda2"] == r["lambda2"], f"Rust {r['lambda2']}, reference {cal['lambda2']}")
        for i, ps in enumerate(cal["per_slice"]):
            xr, xf = r["strengthPerLambdaAtSlices"][i], ps["strength"]
            ur = U_PROF_REL * abs(xr)
            case = f"strength N = {int(cal['N'])} a4 = {ps['a4']}"
            if ps["peak_interior"]:
                bound = abs(ps["curvature_at_peak"]) * s_R ** 2 / 8.0
                slack = K_SIGMA * (ps["U"] + ur) + FLOOR * abs(xf)
                dd = xf - xr
                ok = -slack <= dd <= bound + slack
                c.flag(case, ok, f"ref - Rust = {fe(dd)} outside [-{fe(slack)}, {fe(bound + slack)}]")
                c.extra.append(f"{case}: ref - Rust = {fe(dd)}, sampling bound {fe(bound)}")
            else:
                c.cmp(case, xr, xf, ps["U"], ur, table=table)
    emit("parameters_couplings", c.ok(), c.detail())

    # ---------------------------------------------------------------- ground states
    summ = {r["id"]: r for r in read_csv(rust / "ground" / "summary.csv")}
    emt = {r["id"]: r for r in read_csv(rust / "ground" / "emt-integrals.csv")}
    exc = {r["id"]: r for r in read_csv(rust / "excited" / "summary.csv")}
    adi = {r["id"]: r for r in read_csv(rust / "adiabatic" / "adiabaticity.csv")}
    C = {
        "ground_occupations_and_groups": Check("the same occupied levels (Rust label - label_min = reference rank), occupations, HOMO group and LUMO group"),
        "ground_energies": Check("E_KS, E_band, E_int; U_Rust per state measured (single canonical vs refined)"),
        "ground_homo_lumo_gap": Check("HOMO, LUMO, KS gap; U_Rust = (16/15) x the largest |canonical - refined| over all levels of the state"),
        "ground_eigenvalues": Check("every level present in both label sets, label by label; U_Rust = (16/15) x the largest |canonical - refined| over all levels of the state"),
        "excited_delta_scf": Check(f"Delta-SCF excitation energy and E_excited; U_Rust(Delta-SCF) = matrix-wide maximum (16/15) x {fe(G['refined_delta_scf'])} m"),
        "emt_integrals": Check("2 Vol_7 int e^{6Hy} (rho, p3, p_t, p8, n) dy; U_Rust per state measured"),
        "emt_brane_tip_values": Check("rho, p3, p_t, p8 at the brane y = 0 and at the tip y = -L; U_Rust per state measured (profile end points)"),
        "ground_profiles": Check("proper profiles n, S, Q, M_eff, v_v, e_int, rho, p3, p_t, p8 at the 151 points y = -3 + 0.02 i, in units of the "
                                 "profile maximum; U_Rust = (16/15) x the largest |canonical - refined| of that profile of the state"),
        "exchange_delta_E_x": Check("Delta E_x = (lambda/32) 2 Vol_7 int e^{6Hy} Q^2 dy (exact-Fock minus uniform-gas exchange); U_Rust = "
                                    "(16/15) x 2 x (largest |canonical - refined| of Q / max |Q|) x |Delta E_x| (derived from the measured Q profile)"),
        "adiabatic_dE_da4": Check("dE/da4 = -6 Vol_7 int e^{6Hy}(p3 - p_t) dy (EMT form; U_Rust = 3 (U_Rust(int p3) + U_Rust(int p_t)) measured) and the "
                                  f"fixed-occupation finite difference (U_Rust = matrix-wide relative maximum (16/15) x {fe(G['refined_adiabatic_derivatives'])})"),
        "adiabatic_Q_max": Check(f"adiabaticity Q_max = A H |<n| d_a h |m>| / (eps_n - eps_m)^2 over the same pairs (n occupied, m empty, same sector, "
                                 f"rank <= 2) and the same maximising pair; U_Rust = matrix-wide relative maximum (16/15) x {fe(G['refined_adiabatic_derivatives'])}"),
    }
    gids = sorted(p.stem for p in (ref / "ground").glob("*.json"))
    for sid in gids:
        d = load(ref / "ground" / f"{sid}.json")
        r_s, r_e, r_x, r_a = summ[sid], emt[sid], exc[sid], adi[sid]
        m = rf[sid]
        ms = m["scalars"]
        U = lambda name: RK4_FACTOR * ms[name]["abs_diff"]
        sc = d["scalars"]
        # levels and occupations
        lv = read_csv(rust / "ground" / "levels" / f"{sid}.csv")
        lmin = {(int(x["n2"]), int(x["j"]), x["parity"]): int(x["label_min"]) for x in lv}
        rl = {f"{int(x['n2'])}:{'+1' if int(x['j']) > 0 else '-1'}:{x['parity']}:{int(x['label']) - int(x['label_min'])}": (float(x["eps"]), float(x["f"])) for x in lv}
        fl = {f"{k[0]}:{'+1' if k[1] > 0 else '-1'}:{k[2]}:{k[3]}": (e, u, f) for k, e, u, f in
              zip(d["levels"]["keys"], d["levels"]["eps"], d["levels"]["U"], d["levels"]["f"])}
        occ_r = sorted(k for k, v in rl.items() if v[1] > 0)
        occ_f = sorted(k for k, v in fl.items() if v[2] > 0)
        co = C["ground_occupations_and_groups"]
        co.flag(f"{sid} occupied set", occ_r == occ_f, f"Rust {len(occ_r)} levels, reference {len(occ_f)}, differ: {sorted(set(occ_r) ^ set(occ_f))[:6]}")
        co.flag(f"{sid} occupations", all(abs(rl[k][1] - fl[k][2]) <= 1e-12 for k in occ_r if k in fl), "occupation numbers differ")
        hg = sorted(key_from_label(s, lmin) for s in r_x["hole_levels"].split(";"))
        lg = sorted(key_from_label(s, lmin) for s in r_x["particle_levels"].split(";"))
        co.flag(f"{sid} HOMO group", hg == sorted(d["homo_group"]), f"Rust {hg}, reference {d['homo_group']}")
        co.flag(f"{sid} LUMO group", lg == sorted(d["lumo_group"]), f"Rust {lg}, reference {d['lumo_group']}")
        u_lev = RK4_FACTOR * m["levels"]["max_abs_diff"]
        # energies
        ce = C["ground_energies"]
        for k in ("E_KS", "E_band", "E_int"):
            ce.cmp(f"{sid} {k}", float(r_s[k]), sc[k]["value"], sc[k]["U"], U(k), table=table)
        ch = C["ground_homo_lumo_gap"]
        for k, ul in (("HOMO", u_lev), ("LUMO", u_lev), ("KS_gap", 2 * u_lev)):
            ch.cmp(f"{sid} {k}", float(r_s[k]), sc[k]["value"], sc[k]["U"], ul, table=table)
        cv = C["ground_eigenvalues"]
        common = sorted(set(rl) & set(fl))
        missing_r = [k for k in occ_f if k not in rl]
        missing_f = [k for k in rl if rl[k][1] > 0 and k not in fl]
        cv.flag(f"{sid} coverage", not missing_r and not missing_f and all(k in rl and k in fl for k in hg + lg),
                f"occupied or HOMO/LUMO levels missing in one label set: {missing_r + missing_f}")
        for k in common:
            cv.cmp(f"{sid} level {k}", rl[k][0], fl[k][0], fl[k][1], u_lev)
        cv.extra.append(f"{sid}: {len(common)} common levels (Rust {len(rl)}, reference {len(fl)})")
        # excited
        cx = C["excited_delta_scf"]
        cx.cmp(f"{sid} delta_SCF", float(r_x["delta_SCF"]), sc["delta_SCF"]["value"], sc["delta_SCF"]["U"], U_DSCF, table=table)
        cx.cmp(f"{sid} E_excited", float(r_x["E_excited"]), sc["E_excited"]["value"], sc["E_excited"]["U"], U("E_KS") + U_DSCF, table=table)
        # EMT
        ci = C["emt_integrals"]
        for k in ("rho", "p3", "p_t", "p8", "n"):
            ci.cmp(f"{sid} int_{k}", float(r_e["int_" + k]), sc["int_" + k]["value"], sc["int_" + k]["U"], U("int_" + k), table=table)
        cb = C["emt_brane_tip_values"]
        for k in ("rho", "p3", "p_t", "p8"):
            for end in ("brane", "tip"):
                nm = f"{k}_{end}"
                cb.cmp(f"{sid} {nm}", float(r_e[nm]), sc[nm]["value"], sc[nm]["U"], U(nm), table=table)
        # profiles
        cp = C["ground_profiles"]
        rpf = read_csv(rust / "ground" / "profiles" / f"{sid}.csv")
        ys = [float(x["y"]) for x in rpf]
        if max(abs(a - b) for a, b in zip(ys, d["profiles"]["y"])) > 1e-12:
            cp.flag(f"{sid} profile points", False, "the y points differ")
        for nm in PROFILES:
            xr = [num(x[nm]) for x in rpf]
            xf, uf = d["profiles"][nm]["value"], d["profiles"][nm]["U"]
            pmax = max(max(abs(v) for v in xr), 1e-300)
            ur = RK4_FACTOR * m["profiles"][nm]["max_abs_diff"]
            for i in range(len(xr)):
                cp.cmp(f"{sid} {nm}(y = {ys[i]:.2f})", xr[i], xf[i], uf[i], ur, scale=pmax)
        # exchange diagnostic
        cq = C["exchange_delta_E_x"]
        qrel = m["profiles"]["Q"]["max_abs_diff"] / max(m["profiles"]["Q"]["max_abs"], 1e-300)
        dex = float(r_e["deltaE_x_exact_fock"])
        cq.cmp(f"{sid} deltaE_x", dex, sc["deltaE_x_exact_fock"]["value"], sc["deltaE_x_exact_fock"]["U"], RK4_FACTOR * 2 * qrel * abs(dex), table=table)
        # adiabatic
        ca = C["adiabatic_dE_da4"]
        ca.cmp(f"{sid} dE_da4_emt", float(r_a["dE_da4_emt"]), sc["dE_da4_emt"]["value"], sc["dE_da4_emt"]["U"], 3 * (U("int_p3") + U("int_p_t")), table=table)
        xfd = float(r_a["dE_da4_finite_difference"])
        ca.cmp(f"{sid} dE_da4_finite_difference", xfd, sc["dE_da4_fd"]["value"], sc["dE_da4_fd"]["U"], U_ADIAB_REL * abs(xfd), table=table)
        cqm = C["adiabatic_Q_max"]
        qr = float(r_a["Q_max"])
        ad = d["adiabatic"]
        cqm.cmp(f"{sid} Q_max", qr, ad["Q_max"], ad["U_Q_max"], U_ADIAB_REL * abs(qr), table=table)
        if qr > 0 and ad["top"]:
            hole, part = [x.strip() for x in r_a["Q_max_pair"].split("->")]
            pr = (key_from_label(hole, lmin), key_from_label(part, lmin))
            pf = (ad["top"][0]["hole"], ad["top"][0]["particle"])
            cqm.flag(f"{sid} Q_max pair", pr == pf, f"Rust {pr}, reference {pf}")
            top = ad["top"][0]
            cqm.cmp(f"{sid} Q_max matrix element", float(r_a["Q_max_matrix_element"]), top["matrix_element"], top["U_matrix_element"],
                    U_ADIAB_REL * abs(float(r_a["Q_max_matrix_element"])), table=table)
            cqm.cmp(f"{sid} Q_max delta eps", float(r_a["Q_max_delta_eps"]), top["delta_eps"], top["U_delta_eps"],
                    RK4_FACTOR * 2 * m["levels"]["max_abs_diff"], table=table)
        elif qr == 0:
            cqm.extra.append(f"{sid}: Rust Q_max = 0 ({r_a['Q_max_pair']}), reference {fe(ad['Q_max'])}")
    for name, ch in C.items():
        emit(name, ch.ok(), ch.detail())

    # ---------------------------------------------------------------- thermal states
    th = {r["id"]: r for r in read_csv(rust / "thermo" / "thermodynamics.csv")}
    T = {
        "thermo_state_functions": Check("mu, E, entropy S, F = E - T S, Omega (both forms); U_Rust per state measured for mu, E, S (single canonical vs "
                                        "refined), U_Rust(F) = U(E) + T U(S), U_Rust(Omega) = U(F) + N U(mu)"),
        "thermo_derivatives": Check(f"C_V = T dS/dT, dE/dT and -dF/dT (Richardson differences in T); U_Rust = matrix-wide relative maximum (16/15) x "
                                    f"{fe(G['refined_heat_capacity'])} of max(|x|, 1e-6) (refined_heat_capacity); dE/dT and -dF/dT are difference "
                                    f"quotients of energies, so each solver's stated noise floor is added: eta_Rust = N x rootTolerance / dT "
                                    f"(Rust rootTolerance from its parameters.json, as in its thermo_CV_identity check), eta_ref = N x 1e-12 / dT "
                                    f"(the reference SCF tolerance, as in its own thermo_CV_identity check), dT = 0.01 T"),
    }
    root_tol_R = float(rp["numerics"]["rootTolerance"])
    tids = sorted(p.stem for p in (ref / "thermo").glob("*.json"))
    for sid in tids:
        d = load(ref / "thermo" / f"{sid}.json")
        r = th[sid]
        ms = rf[sid]["scalars"]
        uE, uS, uM = (RK4_FACTOR * ms[k]["abs_diff"] for k in ("E_KS", "entropy", "mu"))
        x = d["thermo"]
        Tt, N = d["T"], d["N"]
        uF = uE + Tt * uS
        ct = T["thermo_state_functions"]
        for k, ur in (("mu", uM), ("E", uE), ("entropy", uS), ("F", uF), ("Omega_direct", uF + N * uM), ("Omega_F_minus_muN", uF + N * uM)):
            ct.cmp(f"{sid} {k}", float(r[k]), x[k]["value"], x[k]["U"], ur, table=table)
        cd = T["thermo_derivatives"]
        dT = 0.01 * Tt
        for k in ("C_V", "C_V_from_dEdT", "minus_dFdT"):
            xr = float(r[k])
            quotient = k != "C_V"
            u_ref = x[k]["U"] + (N * 1e-12 / dT if quotient else 0.0)
            u_rust = U_CV_REL * max(abs(xr), 1e-6) + (N * root_tol_R / dT if quotient else 0.0)
            cd.cmp(f"{sid} {k}", xr, x[k]["value"], u_ref, u_rust, table=table)
    for name, ch in T.items():
        emit(name, ch.ok(), ch.detail())

    # ---------------------------------------------------------------- determinism of the reference outputs
    files = sorted(p for p in ref.rglob("*") if p.is_file())
    crlf = [p.relative_to(ref).as_posix() for p in files if b"\r\n" in p.read_bytes()]
    emit("reference_outputs_lf_only", not crlf, f"{len(files)} reference result files; files with CRLF: {crlf if crlf else 'none'}")
    if args.reference_repeat:
        rep = Path(args.reference_repeat)
        f2 = sorted(p for p in rep.rglob("*") if p.is_file())
        names1 = [p.relative_to(ref).as_posix() for p in files]
        names2 = [p.relative_to(rep).as_posix() for p in f2]
        differ = [n for n in names1 if n in names2 and (ref / n).read_bytes() != (rep / n).read_bytes()]
        same = names1 == names2 and not differ
        emit("reference_repeat_byte_identical", same,
             f"second reference run: {len(names2)} files, same file set: {names1 == names2}, differing files: {differ if differ else 'none'}")
    man = load(ref / "manifest.json")["files"]
    bad_hash = [n for n, h in man.items() if hashlib.sha256((ref / n).read_bytes()).hexdigest() != h]
    emit("reference_manifest", not bad_hash and len(man) == len(files) - 1,
         f"manifest.json lists {len(man)} files with SHA-256; mismatches: {bad_hash if bad_hash else 'none'}")

    npass = sum(c["verdict"] == "PASS" for c in checks)
    report = {
        "report": "Revision Kohn-Sham cross-check: Rust solver vs the independent Python reference (different discretisation) on the reference subset",
        "producer": "Revision/kohn_sham/checker/crosscheck_ks.py",
        "tolerance_rule": "|x_Rust - x_ref| <= 3 (U_ref + U_Rust) + 1e-12 scale; U_ref = the reference's three-grid Richardson uncertainty "
                          "(validated on a fourth grid); U_Rust = (16/15) |canonical - refined| measured per state (checker/rust-refinement.json) or, "
                          "where `single` does not report the quantity, the matrix-wide maximum of ks-rust-determinism.json; scale = max(1, |x|) "
                          "for scalars, the profile maximum for profiles. Fixed before the comparison.",
        "rust_matrix_wide_uncertainties": G,
        "subset": {"ground": gids, "thermal": tids},
        "summary": {"checks": len(checks), "pass": npass, "fail": len(checks) - npass},
        "checks": checks,
    }
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    with open(args.report, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(report, indent=1, ensure_ascii=True) + "\n")
    with open(args.table, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("case,rust,reference,U_ref,U_rust,tolerance,abs_diff,ratio,verdict\n")
        for row in table:
            fh.write(",".join(row) + "\n")
    print("SUCCESS" if npass == len(checks) else "FAILURE")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
