#!/usr/bin/env python3
"""Cross-check of the Rust Kohn-Sham solver (Revision/kohn_sham/solver, results in Revision/kohn_sham/results)
against the independent Python reference (Revision/kohn_sham/reference, staggered finite differences with
Richardson extrapolation) on the FULL canonical matrix (SPEC section 7): every ground state (75), every thermal
state (135, with every level label by label), the exact-Fock variant SCF energies and gaps (60), the rescaling
partners (60), the particle-hole lists (75), the sea-hole diagnostic (135) and the crossing demonstration (5 slices);
and the stated rounding bound of the repaired Rust Mermin root against 40-digit roots on the Rust levels.

TOLERANCE RULE (fixed in this file before any comparison; never adjusted to a result):
    |x_Rust - x_ref| <= 3 (U_ref + U_Rust) + 1e-12 * scale
  U_ref  = the reference's measured grid uncertainty (three-grid Richardson, |R - R2|; validated on a fourth
           grid, Revision/kohn_sham/reports/ks-reference.json check richardson_uncertainty_validated);
  U_Rust = (16/15) |canonical - refined| of the Rust solver (RK4: the refined error is 1/16 of the canonical
           one), measured per state and per quantity by checker/measure_rust_refinement.py where the Rust
           `single` command reports the quantity (energies, EMT integrals, levels, profiles, brane and tip
           values, mu, entropy; exact-Fock E_KS and gap; crossing-demonstration energies); otherwise the maximum
           over the whole canonical matrix of Revision/kohn_sham/reports/ks-rust-determinism.json, or a
           propagation of measured uncertainties stated in each check.  Where the matrix run and the `single`
           run take different SCF paths (exact-Fock variant: the matrix starts from the uniform-gas state,
           `single` from zero potentials), the measured |single - matrix| is added to U_Rust;
  scale  = max(1, |x|) for scalars, the profile maximum for profiles (roundoff floor).
Every comparison yields ratio = |x_Rust - x_ref| / tolerance; a check passes when every ratio <= 1.

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially
DEFLATING extra times (scale factor e^{-a4} sin^{1/6} z, a4 increasing); x8 = hidden direction,
y = ln(sin z)/(6H) in [-L, 0].

The reference repeat: the checker itself runs Revision/kohn_sham/reference/run_reference.py into a fresh
directory <work>/reference-repeat and compares every result file and the report byte for byte with the committed
ones.

Usage (from the repository root):
  python Revision/kohn_sham/checker/crosscheck_ks.py --work <scratch dir> [--jobs N] [--report FILE] [--table FILE]
"""

from __future__ import annotations

import argparse
import csv
import functools
import hashlib
import json
import math
import multiprocessing as mpc
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
KS = HERE.parent
REPO = KS.parent.parent
K_SIGMA = 3.0
FLOOR = 1e-12
RK4_FACTOR = 16.0 / 15.0
PROFILES = ("n", "S", "Q", "M_eff", "v_v", "e_int", "rho", "p3", "p_t", "p8")
EPS_MACH = 2.220446049250313e-16


def read_csv(p: Path):
    with open(p, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def num(x):
    return float("nan") if x in ("null", "", None, "nan") else float(x)


def load(p: Path):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def fe(x):
    return "nan" if x is None or not math.isfinite(x) else f"{x:.3e}"


class Check:
    """Aggregated comparison: worst ratio |diff| / tolerance, its case, and every failure (with a diagnosis line)."""

    def __init__(self, desc):
        self.desc = desc
        self.n = 0
        self.worst = -1.0
        self.wcase = ""
        self.fails = []
        self.extra = []
        self.diag = []

    def cmp(self, case, xr, xf, u_ref, u_rust, scale=None, table=None, xr_refined=None):
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
            # data-driven diagnosis: which side carries the difference
            s = (f"{case}: |diff| = {d / max(u_ref, 1e-300):.3g} U_ref = {d / max(u_rust, 1e-300):.3g} U_Rust")
            if xr_refined is not None and math.isfinite(xr_refined):
                s += (f"; the refined Rust run gives {xr_refined:.15g}, |refined - reference| = {fe(abs(xr_refined - xf))} "
                      f"({'closer to the reference: the canonical Rust error exceeds its measured U_Rust' if abs(xr_refined - xf) < 0.5 * d else 'not closer: the difference is not a canonical-resolution error of Rust'})")
            self.diag.append(s)
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


@functools.lru_cache(maxsize=None)
def r3(n2):
    """Number of lattice points of Z^3 with |n|^2 = n2."""
    R = math.isqrt(n2) + 1
    return sum(1 for x in range(-R, R + 1) for y in range(-R, R + 1) for z in range(-R, R + 1) if x * x + y * y + z * z == n2)


def shell_table(count):
    """The first `count` values n2 >= 0 with r3(n2) > 0 (Legendre: n2 is a sum of three squares unless n2 = 4^a (8b + 7))."""
    out, n2 = [], 0
    while len(out) < count:
        m = n2
        while m > 0 and m % 4 == 0:
            m //= 4
        if n2 == 0 or m % 8 != 7:
            out.append(n2)
        n2 += 1
    return out


def mu_high_precision(eps, deg, N, T, mu0):
    """Root of sum g f(eps; mu, T) = N in 40-digit arithmetic (Newton from mu0); returns (mu, dN/dmu) as floats."""
    mu, ds = mu_root_mp(eps, deg, N, T, mu0)
    return float(mu), float(ds)


def mu_root_mp(eps, deg, N, T, mu0):
    """The same root, returned as 40-digit mpmath numbers (mu, dN/dmu)."""
    mp.mp.dps = 40
    E = [mp.mpf(e) for e in eps]
    Gd = [mp.mpf(g) for g in deg]
    Tm, Nm, mu = mp.mpf(T), mp.mpf(N), mp.mpf(mu0)
    ds = mp.mpf(0)
    for _ in range(100):
        s, ds = mp.mpf(0), mp.mpf(0)
        for e, g in zip(E, Gd):
            x = (e - mu) / Tm
            if x > 2000:
                continue
            f = 1 / (1 + mp.exp(x))
            s += g * f
            ds += g * f * (1 - f) / Tm
        step = (s - Nm) / ds
        mu -= step
        if abs(step) < mp.mpf(10) ** -32:
            break
    else:
        raise RuntimeError("mu_high_precision: no convergence")
    return mu, ds


def _mu_task(a):
    if a[0][0] == "X":
        # exact Rust levels and exact Rust mu: return mu_Rust - root to 40 digits (no rounding of the root to a double)
        root, ds = mu_root_mp(*a[1:])
        return a[0], (float(mp.mpf(a[5]) - root), float(ds))
    return a[0], mu_high_precision(*a[1:])


def key_from_label(s, lmin):
    """'n2:+1:even:label' (Rust label) -> 'n2:+1:even:rank' with rank = label - label_min."""
    n2, j, par, lab = s.split(":")
    jj = 1 if j in ("+1", "1") else -1
    return f"{int(n2)}:{'+1' if jj > 0 else '-1'}:{par}:{int(lab) - lmin[(int(n2), jj, par)]}"


def group_from_labels(s, lmin):
    return ";".join(sorted(key_from_label(x, lmin) for x in s.split(";") if x))


def run_reference_repeat(work: Path, jobs: int):
    """Run the reference into a fresh <work>/reference-repeat (results + report); returns (dir, report, seconds, ok)."""
    rep = work / "reference-repeat"
    if rep.exists():
        if not ((rep / "results" / "manifest.json").exists() or not any(rep.iterdir())):
            raise SystemExit(f"{rep} exists and is not a reference repeat directory")
        shutil.rmtree(rep)
    rep.mkdir(parents=True)
    t0 = time.time()
    cmd = [sys.executable, str(KS / "reference" / "run_reference.py"), "--out", str(rep / "results"), "--report", str(rep / "ks-reference.json"),
           "--jobs", str(jobs)]
    with open(rep / "stderr.txt", "w", encoding="utf-8") as fe_:
        r = subprocess.run(cmd, cwd=str(REPO), stdout=subprocess.PIPE, stderr=fe_, text=True)
    return rep, rep / "ks-reference.json", time.time() - t0, r.returncode == 0 and r.stdout.strip().endswith("SUCCESS")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rust", default=str(KS / "results"))
    ap.add_argument("--rust-solver-report", default=str(KS / "reports" / "ks-rust-solver.json"))
    ap.add_argument("--rust-determinism", default=str(KS / "reports" / "ks-rust-determinism.json"))
    ap.add_argument("--rust-refinement", default=str(HERE / "rust-refinement.json"))
    ap.add_argument("--reference", default=str(KS / "reference" / "results"))
    ap.add_argument("--reference-report", default=str(KS / "reports" / "ks-reference.json"))
    ap.add_argument("--work", required=True, help="scratch directory: the checker runs the reference repeat into <work>/reference-repeat")
    ap.add_argument("--jobs", type=int, default=20)
    ap.add_argument("--report", default=str(KS / "reports" / "ks-crosscheck.json"))
    ap.add_argument("--table", default=str(KS / "reports" / "ks-crosscheck-table.csv"))
    args = ap.parse_args()
    t_all = time.time()
    rust, ref = Path(args.rust), Path(args.reference)
    work = Path(args.work)
    work.mkdir(parents=True, exist_ok=True)
    checks = []
    table = []
    timing = {}

    def emit(name, ok, detail, diag=None):
        c = {"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail}
        if not ok and diag:
            c["diagnosis"] = diag
        checks.append(c)
        print(f"{'PASS' if ok else 'FAIL'} - {name}: {detail[:300]}", file=sys.stderr, flush=True)

    def emit_check(name, ch, extra_diag=None):
        d = list(ch.diag)
        if extra_diag:
            d.append(extra_diag)
        emit(name, ch.ok(), ch.detail(), "; ".join(d) if d else None)

    # ---------------------------------------------------------------- inputs
    rrep, srep, drep = load(args.reference_report), load(args.rust_solver_report), load(args.rust_determinism)
    refine = load(args.rust_refinement)
    rf = {(s["kind"], s["id"]): s for s in refine["states"]}
    bad = {nm: [c["name"] for c in r["checks"] if c["verdict"] != "PASS"] for nm, r in
           (("ks-reference.json", rrep), ("ks-rust-solver.json", srep), ("ks-rust-determinism.json", drep))}
    runs_bad = [f"{s['kind']}:{s['id']}" for s in refine["states"] if not s["runs_ok"]]
    summ = {r["id"]: r for r in read_csv(rust / "ground" / "summary.csv")}
    th = {r["id"]: r for r in read_csv(rust / "thermo" / "thermodynamics.csv")}
    exx = {r["id"]: r for r in read_csv(rust / "exx" / "exact-fock-variant.csv")}
    demo_rows = read_csv(rust / "adiabatic" / "crossing-demo.csv")
    want = {"ground": len(summ), "thermo": len(th), "exx": len(exx), "crossing": len(demo_rows)}
    have = {k: sum(1 for s in refine["states"] if s["kind"] == k) for k in want}
    emit("inputs_all_pass", not any(bad.values()) and not runs_bad and want == have,
         f"reference report {rrep['summary']['pass']}/{rrep['summary']['checks']} PASS, Rust solver report {srep['summary']['pass']}/"
         f"{srep['summary']['checks']} PASS, Rust determinism report {drep['summary']['pass']}/{drep['summary']['checks']} PASS; "
         f"failing checks: {bad}; Rust refinement runs (single canonical and refined) failed: {runs_bad if runs_bad else 'none'}; the refinement "
         f"covers every state of the Rust matrix: {want == have} (states per kind: Rust {want}, measured {have})")
    G = parse_determinism(drep)
    U_EIG = RK4_FACTOR * G["refined_eigenvalues"]
    U_DSCF = RK4_FACTOR * G["refined_delta_scf"]
    U_ADIAB_REL = RK4_FACTOR * G["refined_adiabatic_derivatives"]
    U_CV_REL = RK4_FACTOR * G["refined_heat_capacity"]
    U_PROF_REL = RK4_FACTOR * G["refined_profiles"]
    rp, fp = load(rust / "parameters.json"), load(ref / "parameters.json")
    scf_tol_R = float(rp["numerics"]["scfTolerance"])

    # the measured single runs must reproduce the committed canonical matrix
    c_ok, worst = True, {}
    for s in refine["states"]:
        if not s["runs_ok"]:
            c_ok = False
            continue
        if s["kind"] == "exx":
            continue
        for k, v in s["canonical_single_vs_matrix"].items():
            if k == "levels_compared":
                continue
            if s["kind"] == "crossing":
                # lambda = 0 energies sum g f eps: the checker re-sums the continued occupation, so rounding of the sum is allowed
                v = v / max(1.0, abs(s["scalars"]["E_KS"]["canonical"]))
                k = k + "_rel"
            worst[k] = max(worst.get(k, 0.0), v)
            if v > 1e-12:
                c_ok = False
    emit("rust_refinement_applies_to_matrix", c_ok,
         "the canonical `single` runs of checker/rust-refinement.json reproduce the committed canonical matrix (tolerance 1e-12 for every "
         "class; crossing demonstration relative to max(1, |E|)): " + ", ".join(f"{k} {fe(v)}" for k, v in sorted(worst.items())) +
         "; hence |canonical - refined| of these runs measures the error of the committed Rust results")
    x_ok, xw = True, {"E": (0.0, ""), "gap": (0.0, "")}
    for s in refine["states"]:
        if s["kind"] != "exx" or not s["runs_ok"]:
            continue
        cm = s["canonical_single_vs_matrix"]
        N = float(s["id"].split("_")[0][1:])
        rE, rg = cm["exx_E_abs"] / (N * scf_tol_R), cm["exx_gap_abs"] / (6 * scf_tol_R)
        x_ok &= rE <= 1.0 and rg <= 1.0
        if rE >= xw["E"][0]:
            xw["E"] = (rE, f"{s['id']} |dE| {fe(cm['exx_E_abs'])}")
        if rg >= xw["gap"][0]:
            xw["gap"] = (rg, f"{s['id']} |dgap| {fe(cm['exx_gap_abs'])}")
    emit("rust_refinement_applies_to_matrix_exx", x_ok,
         f"exact-Fock variant: the matrix starts the SCF from the converged uniform-gas state, `single --exx` from zero potentials; both stop "
         f"at max |residual| <= scfTolerance = {scf_tol_R:g}, so they agree only to the SCF stopping effect: |E_single - E_matrix| <= N x "
         f"scfTolerance and |gap_single - gap_matrix| <= 6 scfTolerance (two levels, three potentials) are required; worst ratios: E "
         f"{xw['E'][0]:.3f} ({xw['E'][1]}), gap {xw['gap'][0]:.3f} ({xw['gap'][1]}); the measured |single - matrix| is added to U_Rust of "
         "the exact-Fock comparisons")

    # ---------------------------------------------------------------- problem definition and derived inputs
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
    n_demo_R = float(demo_rows[0]["N"]) if demo_rows else float("nan")
    c.flag("N of the crossing demonstration", der["crossing_demo"]["N_demo"] == n_demo_R and der["crossing_demo"]["same_on_all_grids"],
           f"Rust {n_demo_R}, reference {der['crossing_demo']['N_demo']}")
    c.extra.append(f"N_large = {int(der['N_large'])}, N_mid = {int(der['N_mid'])}, N of the crossing demonstration = {int(der['crossing_demo']['N_demo'])} "
                   f"(U_Rust of the bulk edge: matrix-wide eigenvalue maximum {fe(U_EIG)})")
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

    # ---------------------------------------------------------------- ground states (all 75)
    emt = {r["id"]: r for r in read_csv(rust / "ground" / "emt-integrals.csv")}
    exc = {r["id"]: r for r in read_csv(rust / "excited" / "summary.csv")}
    adi = {r["id"]: r for r in read_csv(rust / "adiabatic" / "adiabaticity.csv")}
    C = {
        "ground_occupations_and_groups": Check("the same occupied levels (Rust label - label_min = reference rank), occupations, HOMO group and LUMO group"),
        "ground_energies": Check("E_KS, E_band, E_int; U_Rust per state measured (single canonical vs refined)"),
        "ground_homo_lumo_gap": Check("HOMO, LUMO, KS gap; U_Rust = (16/15) x the largest |canonical - refined| over all levels of the state"),
        "ground_eigenvalues": Check("every level present in both label sets, label by label; U_Rust = (16/15) x the largest |canonical - refined| over all levels of the state"),
        "excited_delta_scf": Check(f"Delta-SCF excitation energy and E_excited; U_Rust(Delta-SCF) = matrix-wide maximum (16/15) x {fe(G['refined_delta_scf'])} m"),
        "excited_particle_hole_lists": Check("the 24 lowest particle-hole excitations (excited/particle-hole/<id>.csv) against the reference list (48 rows): "
                                             "the same hole and particle groups (Rust labels converted to ranks), the same multiplicity and same-sector "
                                             "flag, delta_eps within the rule (U_Rust = 2 x (16/15) x the largest |canonical - refined| over the levels "
                                             "of the state); compared where the particle lies below both solvers' lowest excluded level; and no "
                                             "reference excitation below the Rust 24th (minus its tolerance) is missing from the Rust list"),
        "emt_integrals": Check("2 Vol_7 int e^{6Hy} (rho, p3, p_t, p8, n) dy; U_Rust per state measured"),
        "emt_brane_tip_values": Check("rho, p3, p_t, p8 at the brane y = 0 and at the tip y = -L; U_Rust per state measured (profile end points)"),
        "ground_profiles": Check("proper profiles n, S, Q, M_eff, v_v, e_int, rho, p3, p_t, p8 at the 151 points y = -3 + 0.02 i, in units of the "
                                 "profile maximum; U_Rust = (16/15) x the largest |canonical - refined| of that profile of the state"),
        "exchange_delta_E_x": Check("Delta E_x = (lambda/32) 2 Vol_7 int e^{6Hy} Q^2 dy (exact-Fock minus uniform-gas exchange, first order); U_Rust = "
                                    "(16/15) x 2 x (largest |canonical - refined| of Q / max |Q|) x |Delta E_x| (derived from the measured Q profile)"),
        "adiabatic_dE_da4": Check("dE/da4 = -6 Vol_7 int e^{6Hy}(p3 - p_t) dy (EMT form; U_Rust = 3 (U_Rust(int p3) + U_Rust(int p_t)) measured) and the "
                                  f"fixed-occupation finite difference (U_Rust = matrix-wide relative maximum (16/15) x {fe(G['refined_adiabatic_derivatives'])})"),
        "adiabatic_Q_max": Check(f"adiabaticity Q_max = A H |<n| d_a h |m>| / (eps_n - eps_m)^2 over the same pairs (n occupied, m empty, same sector, "
                                 f"rank <= 2) and the same maximising pair; U_Rust = matrix-wide relative maximum (16/15) x {fe(G['refined_adiabatic_derivatives'])}"),
    }
    gids = sorted(summ)
    ref_g = {sid: (load(ref / "ground" / f"{sid}.json") if (ref / "ground" / f"{sid}.json").exists() else None) for sid in gids}
    missing_ref = [sid for sid, d in ref_g.items() if d is None]
    # label_min of every sector at every slice from all Rust levels files (it depends only on the free problem at the slice):
    # used to convert the labels of the crossing demonstration; the files must agree with each other
    lmin_by_slice, lmin_conflicts = {}, []
    for sid in gids:
        a4 = float(summ[sid]["a4"])
        for x in read_csv(rust / "ground" / "levels" / f"{sid}.csv"):
            k, v = (int(x["n2"]), int(x["j"]), x["parity"]), int(x["label_min"])
            old = lmin_by_slice.setdefault(a4, {}).setdefault(k, v)
            if old != v:
                lmin_conflicts.append(f"{sid} {k}")
    u_lev_of, uE_of = {}, {}
    for sid in gids:
        d = ref_g[sid]
        if d is None:
            continue
        r_s, r_e, r_x, r_a = summ[sid], emt[sid], exc[sid], adi[sid]
        m = rf[("ground", sid)]
        ms = m["scalars"]
        U = lambda name: RK4_FACTOR * ms[name]["abs_diff"]
        REF = lambda name: ms[name]["refined"]
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
        u_lev_of[sid], uE_of[sid] = u_lev, U("E_KS")
        # energies
        ce = C["ground_energies"]
        for k in ("E_KS", "E_band", "E_int"):
            ce.cmp(f"{sid} {k}", float(r_s[k]), sc[k]["value"], sc[k]["U"], U(k), table=table, xr_refined=REF(k))
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
        # excited
        cx = C["excited_delta_scf"]
        cx.cmp(f"{sid} delta_SCF", float(r_x["delta_SCF"]), sc["delta_SCF"]["value"], sc["delta_SCF"]["U"], U_DSCF, table=table)
        cx.cmp(f"{sid} E_excited", float(r_x["E_excited"]), sc["E_excited"]["value"], sc["E_excited"]["U"], U("E_KS") + U_DSCF, table=table)
        # particle-hole list
        cph = C["excited_particle_hole_lists"]
        rph = read_csv(rust / "excited" / "particle-hole" / f"{sid}.csv")
        fph = d["particle_hole"]["list"]
        # the cut: both solvers' lowest level outside their label sets (reference: Richardson value), lowered by the comparison
        # tolerance, so that a level which is excluded by one solver and listed by the other is never compared
        ec_R, ec_F, u_ec = float(r_s["E_complete"]), sc["lowest_excluded"]["value"], sc["lowest_excluded"]["U"]
        ec = min(ec_R, ec_F) - (K_SIGMA * (u_ec + u_lev) + FLOOR * max(1.0, abs(ec_F)))
        fmap = {(x["hole"], x["particle"]): x for x in fph}
        f_full = len(fph) >= d["particle_hole"]["rows_kept"]
        f_last = fph[-1]["delta_eps"] if fph else -math.inf
        matched, skipped, notcov = 0, 0, 0
        last_de, last_tol = -math.inf, 0.0
        rust_keys = set()
        for row in rph:
            hk, pk = group_from_labels(row["hole_levels"], lmin), group_from_labels(row["particle_levels"], lmin)
            rust_keys.add((hk, pk))
            de = float(row["delta_eps"])
            if float(row["eps_particle"]) >= ec:
                skipped += 1
                continue
            x = fmap.get((hk, pk))
            if x is None:
                if f_full and de > f_last:
                    notcov += 1          # beyond the last kept reference row: not covered by the comparison
                else:
                    cph.flag(f"{sid} rank {row['rank']}", False, f"{hk} -> {pk} (delta_eps {de:.10g}) not in the reference list")
                continue
            matched += 1
            ok = cph.cmp(f"{sid} particle-hole rank {row['rank']} delta_eps", de, x["delta_eps"], x["U_delta_eps"], 2 * u_lev, table=table)
            cph.flag(f"{sid} rank {row['rank']} multiplicity", abs(float(row["multiplicity"]) - x["multiplicity"]) <= 1e-9,
                     f"Rust {row['multiplicity']}, reference {x['multiplicity']}")
            cph.flag(f"{sid} rank {row['rank']} same_sector", (row["same_sector"] == "true") == x["same_sector"],
                     f"Rust {row['same_sector']}, reference {x['same_sector']}")
            if de > last_de:
                last_de, last_tol = de, K_SIGMA * (x["U_delta_eps"] + 2 * u_lev) + FLOOR * max(1.0, abs(de))
        # completeness: no reference excitation (particle below both cuts) clearly below the last Rust row is missing from the Rust
        # list; if Rust lists fewer than 24 rows it lists every excitation below its cut, so then every reference row must be there
        bound_de = last_de - last_tol if len(rph) >= 24 else math.inf
        miss = [f"{x['hole']} -> {x['particle']} ({x['delta_eps']:.10g})" for x in fph
                if x["delta_eps"] < bound_de and x["eps_particle"] < ec and (x["hole"], x["particle"]) not in rust_keys]
        cph.flag(f"{sid} completeness", not miss, f"reference excitations below the last Rust row missing in Rust: {miss[:4]}")
        if skipped or notcov:
            cph.extra.append(f"{sid}: {skipped} Rust rows with the particle at or above the common cut {ec:.10g}, {notcov} beyond the "
                             f"last kept reference row (not compared)")
        cph.extra_rows = getattr(cph, "extra_rows", 0) + matched
        # EMT
        ci = C["emt_integrals"]
        for k in ("rho", "p3", "p_t", "p8", "n"):
            ci.cmp(f"{sid} int_{k}", float(r_e["int_" + k]), sc["int_" + k]["value"], sc["int_" + k]["U"], U("int_" + k), table=table,
                   xr_refined=REF("int_" + k))
        cb = C["emt_brane_tip_values"]
        for k in ("rho", "p3", "p_t", "p8"):
            for end in ("brane", "tip"):
                nm = f"{k}_{end}"
                cb.cmp(f"{sid} {nm}", float(r_e[nm]), sc[nm]["value"], sc[nm]["U"], U(nm), table=table, xr_refined=REF(nm))
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
    C["ground_eigenvalues"].extra.append(f"{len(gids) - len(missing_ref)} ground states; reference files missing: {missing_ref if missing_ref else 'none'}")
    C["excited_particle_hole_lists"].extra.append(f"{getattr(C['excited_particle_hole_lists'], 'extra_rows', 0)} Rust rows matched to reference rows")
    for name, ch in C.items():
        emit_check(name, ch)

    # ---------------------------------------------------------------- exact-Fock variant (all 60 lambda != 0 states)
    cX = Check("exact-Fock-exchange VARIANT (w_Q = lambda Q/16 sigma3, e_int + lambda Q^2/32), self-consistent in both solvers: E_exact_fock_scf, "
               "gap_exact_fock and E_exx - (E_uniform_gas + Delta E_x); U_Rust(E) = (16/15)|canonical - refined| of `single --exx` + "
               "|single - matrix| (different SCF start), likewise for the gap (from the `single` levels); U_Rust(E_exx - first order) = "
               "U_Rust(E_exx) + U_Rust(E_KS uniform gas) + U_Rust(Delta E_x as in exchange_delta_E_x)")
    for sid in sorted(exx):
        p = ref / "exx" / f"{sid}.json"
        if not p.exists():
            cX.flag(f"{sid} reference", False, "no reference exact-Fock result")
            continue
        d = load(p)
        sc = d["scalars"]
        r = exx[sid]
        m = rf[("exx", sid)]
        cm = m["canonical_single_vs_matrix"]
        uX = RK4_FACTOR * m["scalars"]["E_KS"]["abs_diff"] + cm["exx_E_abs"]
        uG = RK4_FACTOR * m["scalars"]["gap_exact_fock"]["abs_diff"] + cm["exx_gap_abs"]
        cX.cmp(f"{sid} E_exact_fock_scf", float(r["E_exact_fock_scf"]), sc["E_exact_fock_scf"]["value"], sc["E_exact_fock_scf"]["U"], uX, table=table,
               xr_refined=m["scalars"]["E_KS"]["refined"])
        cX.cmp(f"{sid} gap_exact_fock", float(r["gap_exact_fock"]), sc["gap_exact_fock"]["value"], sc["gap_exact_fock"]["U"], uG, table=table)
        mg = rf[("ground", sid)]
        qrel = mg["profiles"]["Q"]["max_abs_diff"] / max(mg["profiles"]["Q"]["max_abs"], 1e-300)
        u1 = uX + RK4_FACTOR * mg["scalars"]["E_KS"]["abs_diff"] + RK4_FACTOR * 2 * qrel * abs(float(r["deltaE_x_exact_fock_diag"]))
        cX.cmp(f"{sid} E_exx_minus_first_order", float(r["E_exx_minus_first_order"]), sc["E_exx_minus_first_order"]["value"],
               sc["E_exx_minus_first_order"]["U"], u1, table=table)
        same = all(x["same_occupations_as_uniform_gas"] for x in d["per_grid"])
        cX.flag(f"{sid} reference occupations", same, "the reference exact-Fock aufbau occupation differs from its uniform-gas one")
    emit_check("exx_variant_scf", cX)

    # ---------------------------------------------------------------- rescaling partners (all 60 a4,0 > 0 states)
    cR = Check("rescaling partners KS(0; dk e^{-a4,0}, v_t e^{-3 a4,0}, lambda), solved independently by each solver: partner_E_KS (Rust "
               "rescaling.csv) against the reference partner; partner dk and v_t identical (relative 1e-15); Rust same_label_set and "
               "same_occupations true; U_Rust = U_Rust(E_KS of the slice state, measured) + |partner_E_KS - E_KS(slice)| of Rust (the partner "
               "problem has the same coefficient functions up to rounding, so it carries the same discretisation error)")
    for r in read_csv(rust / "rescaling" / "rescaling.csv"):
        sid = r["id"]
        p = ref / "rescaling" / f"{sid}.json"
        if not p.exists():
            cR.flag(f"{sid} reference", False, "no reference partner")
            continue
        d = load(p)
        cR.flag(f"{sid} partner dk, v_t", abs(float(r["partner_dk"]) - d["partner_dk"]) <= 1e-15 * d["partner_dk"]
                and abs(float(r["partner_v_t"]) - d["partner_v_t"]) <= 1e-15 * d["partner_v_t"], f"Rust {r['partner_dk']}, {r['partner_v_t']}")
        cR.flag(f"{sid} Rust identity flags", r["same_label_set"] == "true" and r["same_occupations"] == "true", "Rust partner label set or occupations differ")
        eR = float(r["partner_E_KS"])
        u = uE_of.get(sid, math.nan) + abs(eR - float(summ[sid]["E_KS"]))
        cR.cmp(f"{sid} partner_E_KS", eR, d["E_KS"]["value"], d["E_KS"]["U"], u, table=table)
    emit_check("rescaling_partners", cR)

    # ---------------------------------------------------------------- crossing demonstration
    cC = Check("crossing demonstration (lambda = 0, N = N_demo): per slice the same flag occupied_set_equal_to_a4_0, the same open-shell flag, the "
               "same labels left and entered (Rust labels converted to ranks with the label_min of the Rust levels files at that slice), "
               "E_aufbau, E_adiabatically_continued and their difference; U_Rust = (16/15)|canonical - refined| of `single` (E_aufbau) and of the "
               "continued occupation summed over the `single` levels, plus |single - matrix| (summation order)")
    rcd = load(ref / "crossing" / "crossing-demo.json")
    rrows = {round(x["a4"], 6): x for x in rcd["rows"]}
    cC.flag("label_min consistent across the Rust levels files", not lmin_conflicts, f"conflicts: {lmin_conflicts[:5]}")
    for r in demo_rows:
        a4 = float(r["a4"])
        sid = f"N{int(float(r['N']))}_lam0_a{int(round(a4 * 10)):02d}"
        x = rrows.get(round(a4, 6))
        m = rf[("crossing", sid)]
        if x is None or not m["runs_ok"]:
            cC.flag(f"a4 = {a4}", False, "reference row or Rust refinement missing")
            continue
        lmin = lmin_by_slice.get(a4, {})
        cC.flag(f"a4 = {a4} occupied_set_equal_to_a4_0", (r["occupied_set_equal_to_a4_0"] == "true") == x["occupied_set_equal_to_a4_0"],
                f"Rust {r['occupied_set_equal_to_a4_0']}, reference {x['occupied_set_equal_to_a4_0']}")
        cC.flag(f"a4 = {a4} open_shell", (r["open_shell"] == "true") == x["open_shell"], f"Rust {r['open_shell']}, reference {x['open_shell']}")
        try:
            left = sorted(key_from_label(s, lmin) for s in r["labels_left"].split(";") if s)
            ent = sorted(key_from_label(s, lmin) for s in r["labels_entered"].split(";") if s)
            cC.flag(f"a4 = {a4} labels", left == x["labels_left"] and ent == x["labels_entered"],
                    f"Rust left {left} entered {ent}, reference left {x['labels_left']} entered {x['labels_entered']}")
        except KeyError as e:
            cC.flag(f"a4 = {a4} labels", False, f"no label_min for sector {e} at this slice in the Rust levels files")
        cm = m["canonical_single_vs_matrix"]
        uA = RK4_FACTOR * m["scalars"]["E_KS"]["abs_diff"] + cm["E_aufbau_abs"]
        uC = RK4_FACTOR * m["scalars"]["E_adiabatically_continued"]["abs_diff"] + cm["E_continued_abs"]
        cC.cmp(f"crossing a4 = {a4} E_aufbau", float(r["E_aufbau"]), x["E_aufbau"]["value"], x["E_aufbau"]["U"], uA, table=table)
        cC.cmp(f"crossing a4 = {a4} E_adiabatically_continued", float(r["E_adiabatically_continued"]), x["E_adiabatically_continued"]["value"],
               x["E_adiabatically_continued"]["U"], uC, table=table)
        cC.cmp(f"crossing a4 = {a4} difference", float(r["difference"]), x["difference"]["value"], x["difference"]["U"], uA + uC, table=table)
    emit_check("crossing_demonstration", cC)

    # ---------------------------------------------------------------- thermal states (all 135)
    T = {
        "thermo_state_functions": Check("mu, E, entropy S, F = E - T S, Omega (both forms); U_Rust per state measured for mu, E, S (single canonical vs "
                                        "refined), U_Rust(F) = U(E) + T U(S), U_Rust(Omega) = U(F) + N U(mu)"),
        "thermo_derivatives": Check(f"C_V = T dS/dT, dE/dT and -dF/dT (Richardson differences in T); U_Rust = matrix-wide relative maximum (16/15) x "
                                    f"{fe(G['refined_heat_capacity'])} of max(|x|, 1e-6) (refined_heat_capacity); dE/dT and -dF/dT are difference "
                                    f"quotients of energies, so each solver's stated noise floor is added: eta_Rust = N x rootTolerance / dT "
                                    f"(Rust rootTolerance from its parameters.json, as in its thermo_CV_identity check), eta_ref = N x 1e-12 / dT "
                                    f"(the reference SCF tolerance, as in its own thermo_CV_identity check), dT = 0.01 T"),
        "thermo_sea_hole_diagnostic": Check("sea-hole diagnostic of the filling CONVENTION: sea_holes_excluded = sum over the shells n2 >= 1 of the Rust "
                                            "thermal label set (the first `shells` shells) of 4 r3 f((mu - eps_sea)/T), eps_sea the highest sea level "
                                            "of the j = -1 even sector (Rust label 0 = rank -1), against the reference sum over the same shells; "
                                            "U_Rust = holes x (U_Rust(mu) + U_Rust(levels))/T (|d f| <= f (|d mu| + |d eps|)/T); and the same "
                                            "verdict on the 1% criterion sea_holes/N <= 0.01 where the reference value is decided (|holes/N - 0.01| "
                                            "> tolerance/N)"),
    }
    root_tol_R = float(rp["numerics"]["rootTolerance"])
    tids = sorted(th)
    ref_t = {sid: (load(ref / "thermo" / f"{sid}.json") if (ref / "thermo" / f"{sid}.json").exists() else None) for sid in tids}
    stab = shell_table(20000)
    for sid in tids:
        d = ref_t[sid]
        if d is None:
            T["thermo_state_functions"].flag(f"{sid} reference", False, "no reference thermal result")
            continue
        r = th[sid]
        m = rf[("thermo", sid)]
        ms = m["scalars"]
        uE, uS, uM = (RK4_FACTOR * ms[k]["abs_diff"] for k in ("E_KS", "entropy", "mu"))
        x = d["thermo"]
        Tt, N = d["T"], d["N"]
        uF = uE + Tt * uS
        ct = T["thermo_state_functions"]
        for k, ur, rk in (("mu", uM, "mu"), ("E", uE, "E_KS"), ("entropy", uS, "entropy"), ("F", uF, None), ("Omega_direct", uF + N * uM, None),
                          ("Omega_F_minus_muN", uF + N * uM, None)):
            ct.cmp(f"{sid} {k}", float(r[k]), x[k]["value"], x[k]["U"], ur, table=table, xr_refined=ms[rk]["refined"] if rk else None)
        cd = T["thermo_derivatives"]
        dT = 0.01 * Tt
        for k in ("C_V", "C_V_from_dEdT", "minus_dFdT"):
            xr = float(r[k])
            quotient = k != "C_V"
            u_ref = x[k]["U"] + (N * 1e-12 / dT if quotient else 0.0)
            u_rust = U_CV_REL * max(abs(xr), 1e-6) + (N * root_tol_R / dT if quotient else 0.0)
            cd.cmp(f"{sid} {k}", xr, x[k]["value"], u_ref, u_rust, table=table)
        # sea holes over the Rust shells
        cs = T["thermo_sea_hole_diagnostic"]
        sh = d["sea_holes"]
        nsh = int(r["shells"])
        maxn2 = stab[nsh - 1]
        idx = next((i for i, s in enumerate(sh["shells_n2_r3"]) if s[0] == maxn2), None)
        if idx is None:
            cs.flag(f"{sid} sea holes", False, f"the Rust shells (up to n2 = {maxn2}) exceed the reference list (up to n2 = {sh['shells_n2_r3'][-1][0]})")
            continue
        if not all(s[0] == stab[i + 1] for i, s in enumerate(sh["shells_n2_r3"][:idx + 1])):
            cs.flag(f"{sid} sea holes", False, "the reference shell list is not the shell sequence n2 >= 1")
            continue
        hr = float(r["sea_holes_excluded"])
        u_lev = RK4_FACTOR * m["levels"]["max_abs_diff"]
        uh = abs(hr) * (uM + u_lev) / Tt
        hf, uhf = sh["cumulative"][idx], sh["U_cumulative"][idx]
        cs.cmp(f"{sid} sea_holes_excluded", hr, hf, uhf, uh, table=table)
        tol = K_SIGMA * (uhf + uh) + FLOOR * max(1.0, abs(hf))
        if abs(hf / N - 0.01) > tol / N:
            cs.flag(f"{sid} 1% criterion", (r["particle_only_convention_within_1pc"] == "true") == (hf / N <= 0.01),
                    f"Rust {r['particle_only_convention_within_1pc']}, reference holes/N = {hf / N:.4g}")
        else:
            cs.extra.append(f"{sid}: 1% criterion undecided by the reference (holes/N = {hf / N:.6g})")
    big = sorted(((float(th[s]["sea_holes_over_N"]), s) for s in tids), reverse=True)
    T["thermo_sea_hole_diagnostic"].extra.append(f"Rust states with sea holes > 1% of N: {sum(1 for v, _ in big if v > 0.01)} of {len(tids)} "
                                                 f"(largest {big[0][1]}: {big[0][0]:.4g} N)")
    for name, ch in T.items():
        emit_check(name, ch)

    # ---------------------------------------------------------------- thermal levels, label by label (all 135 thermal states)
    # The Rust matrix writes no thermal levels file; the levels compared are those of the canonical `single` run of each thermal state
    # (checker/rust-refinement.json), which reproduces the committed mu, E and S of the matrix (rust_refinement_applies_to_matrix).
    # The Rust set of every sector starts at its label_min (solver/src/scf.rs solve_levels: label = ell_min + i, i = 0, 1, ...), so
    # rank = label - (lowest label of that sector in the set); this is checked against label_min of the Rust ground levels files at the
    # same slice wherever the sector occurs there, and the reference ranks of every sector must start at 0.
    TL = Check("every level of each thermal state that both label sets hold, label by label (Rust: the canonical `single` run, which "
               "reproduces the committed mu, E and S; rank = label - lowest label of the sector in the Rust set, checked against label_min "
               "of the Rust ground levels files at the same slice); U_Rust = (16/15) x the largest |canonical - refined| over all levels of "
               "the state; coverage: every level with f >= 1e-12 in one solver's set is in the other's")
    F_COVER = 1e-12
    tl_levels, tl_lmin_checked = 0, 0
    for sid in tids:
        d = ref_t[sid]
        if d is None:
            continue
        m = rf[("thermo", sid)]
        kf = m.get("canonical_level_keys_f")
        if kf is None or len(kf) != len(m["canonical_levels_eps_deg"]):
            TL.flag(f"{sid} Rust level keys", False, "checker/rust-refinement.json has no keys for the canonical thermal levels (re-run measure_rust_refinement.py)")
            continue
        a4 = float(th[sid]["a4"])
        parsed = []
        smin = {}
        for (key, f_), (eps, _) in zip(kf, m["canonical_levels_eps_deg"]):
            n2, j, par, lab = key.split(":")
            sec = (int(n2), 1 if j in ("+1", "1") else -1, par)
            parsed.append((sec, int(lab), eps, f_))
            smin[sec] = min(smin.get(sec, int(lab)), int(lab))
        lm_slice = lmin_by_slice.get(a4, {})
        bad_lmin = [f"{s}: lowest label {v}, label_min {lm_slice[s]}" for s, v in sorted(smin.items()) if s in lm_slice and lm_slice[s] != v]
        tl_lmin_checked += sum(1 for s in smin if s in lm_slice)
        TL.flag(f"{sid} Rust label_min", not bad_lmin, f"the lowest Rust label of a sector differs from label_min of the ground levels files: {bad_lmin[:4]}")
        rl = {f"{s[0]}:{'+1' if s[1] > 0 else '-1'}:{s[2]}:{lab - smin[s]}": (eps, f_) for s, lab, eps, f_ in parsed}
        fl = {f"{k[0]}:{'+1' if k[1] > 0 else '-1'}:{k[2]}:{k[3]}": (e, u, f_) for k, e, u, f_ in
              zip(d["levels"]["keys"], d["levels"]["eps"], d["levels"]["U"], d["levels"]["f"])}
        fmin = {}
        for k in d["levels"]["keys"]:
            fmin[(k[0], k[1], k[2])] = min(fmin.get((k[0], k[1], k[2]), k[3]), k[3])
        bad_rank = sorted(s for s, v in fmin.items() if v != 0)
        TL.flag(f"{sid} reference ranks", not bad_rank, f"reference sectors whose ranks do not start at 0: {bad_rank[:4]}")
        miss_f = sorted(k for k, v in rl.items() if v[1] >= F_COVER and k not in fl)
        miss_r = sorted(k for k, v in fl.items() if v[2] >= F_COVER and k not in rl)
        TL.flag(f"{sid} coverage", not miss_f and not miss_r,
                f"levels with f >= {F_COVER:g} missing in the reference set: {miss_f[:4]}, missing in the Rust set: {miss_r[:4]}")
        u_lev = RK4_FACTOR * m["levels"]["max_abs_diff"]
        for k in sorted(set(rl) & set(fl)):
            TL.cmp(f"{sid} level {k}", rl[k][0], fl[k][0], fl[k][1], u_lev)
            tl_levels += 1
    TL.extra.append(f"{tl_levels} levels compared in {len(tids)} thermal states; Rust sectors checked against label_min of the ground levels "
                    f"files: {tl_lmin_checked}")
    emit_check("thermo_levels", TL)

    # ---------------------------------------------------------------- mu recomputed in high precision from each solver's levels
    # mu is the root of sum g f(eps; mu, T) = N.  In floating point the direct count is known to ~eps_mach N, which fixes mu only to
    # ~eps_mach N / (dN/dmu); deep in the activated regime dN/dmu ~ e^{-gap/2T}/T is tiny.  Here mu is recomputed with 40 digits from
    # each solver's own final levels.  mu is a weighted mean of the levels (dmu/deps_i >= 0, sum 1), so its uncertainty is bounded by the
    # largest level uncertainty: U_Rust = (16/15) max |canonical - refined| of the levels, U_ref = max level U.
    hp = Check("mu recomputed in 40-digit arithmetic from each solver's final levels (the Mermin condition sum g f = N), and "
               "Omega = F - mu N with it; U from the level uncertainties (mu is a weighted mean of the levels)")
    diag = Check("DIAGNOSTIC (not a replacement of thermo_state_functions): each solver's floating-point mu minus the 40-digit root on "
                 "its own levels, against the floating-point conditioning bound B eps_mach N / (dN/dmu), dN/dmu = sum g f (1 - f)/T, "
                 "B = number of levels (plus 3 U(mu) for the reference, whose mu is a Richardson combination)")
    t0 = time.time()
    mtasks = []
    for sid in tids:
        d = ref_t[sid]
        if d is None:
            continue
        lr = rf[("thermo", sid)]["canonical_levels_eps_deg"]
        mtasks.append((("R", sid), [x[0] for x in lr], [x[1] for x in lr], d["N"], d["T"], float(th[sid]["mu"])))
        mtasks.append((("F", sid), d["levels"]["eps"], [4.0 * r3(k[0]) for k in d["levels"]["keys"]], d["N"], d["T"], d["thermo"]["mu"]["value"]))
        mx = rf[("thermo", sid)].get("canonical_mermin_exact")
        if mx is not None:
            mtasks.append((("X", sid), [x[0] for x in mx["levels_eps_deg"]], [x[1] for x in mx["levels_eps_deg"]], d["N"], d["T"], mx["mu"]))
    mtasks.sort(key=lambda t: -len(t[1]))
    with mpc.get_context("spawn").Pool(args.jobs) as pool:
        mres = dict(pool.imap_unordered(_mu_task, mtasks))
    timing["mu_40digit"] = time.time() - t0
    diag_rows = {}
    for sid in tids:
        d = ref_t[sid]
        if d is None:
            continue
        r = th[sid]
        m = rf[("thermo", sid)]
        Tt, N = d["T"], d["N"]
        lr = m["canonical_levels_eps_deg"]
        mu_r, dn_r = mres[("R", sid)]
        mu_f, dn_f = mres[("F", sid)]
        u_r = RK4_FACTOR * m["levels"]["max_abs_diff"]
        u_f = max(d["levels"]["U"])
        hp.cmp(f"{sid} mu_high_precision", mu_r, mu_f, u_f, u_r, table=table)
        uF_r = RK4_FACTOR * (m["scalars"]["E_KS"]["abs_diff"] + Tt * m["scalars"]["entropy"]["abs_diff"])
        hp.cmp(f"{sid} Omega_with_mu_high_precision", float(r["F"]) - mu_r * N, d["thermo"]["F"]["value"] - mu_f * N,
               d["thermo"]["F"]["U"] + N * u_f, uF_r + N * u_r, table=table)
        dev_r = float(r["mu"]) - mu_r
        dev_f = d["thermo"]["mu"]["value"] - mu_f
        b_r = len(lr) * EPS_MACH * N / dn_r
        b_f = len(d["levels"]["keys"]) * EPS_MACH * N / dn_f + 3 * d["thermo"]["mu"]["U"]
        diag.flag(f"{sid} Rust", abs(dev_r) <= b_r, f"|mu_float - mu_hp| = {fe(abs(dev_r))} > bound {fe(b_r)}")
        diag.flag(f"{sid} reference", abs(dev_f) <= b_f, f"|mu_float - mu_hp| = {fe(abs(dev_f))} > bound {fe(b_f)}")
        diag_rows[sid] = {"rust_mu_minus_hp": dev_r, "rust_bound": b_r, "rust_U_mu_measured": RK4_FACTOR * m["scalars"]["mu"]["abs_diff"],
                          "ref_mu_minus_hp": dev_f, "ref_bound": b_f, "ref_U_mu": d["thermo"]["mu"]["U"],
                          "hp_rust_minus_hp_ref": mu_r - mu_f, "dN_dmu": dn_f}
    top = sorted(diag_rows.items(), key=lambda kv: -abs(kv[1]["rust_mu_minus_hp"]))[:3]
    diag.extra.append("largest |Rust mu - 40-digit root on its levels|: " + ", ".join(f"{s} {fe(v['rust_mu_minus_hp'])} (bound {fe(v['rust_bound'])})" for s, v in top))
    topf = sorted(diag_rows.items(), key=lambda kv: -abs(kv[1]["ref_mu_minus_hp"]))[:3]
    diag.extra.append("largest |reference mu - 40-digit root on its levels|: " + ", ".join(f"{s} {fe(v['ref_mu_minus_hp'])} (bound {fe(v['ref_bound'])})" for s, v in topf))
    emit_check("thermo_mu_high_precision", hp)
    emit_check("thermo_mu_rounding_diagnostic", diag)
    # The repaired Rust Mermin root states a first-order rounding bound for its mu (thermodynamics.csv mu_rounding_bound,
    # solver/src/mermin.rs). It is tested here on the EXACT doubles of the canonical `single` run (`--mermin-levels`: shortest
    # round-trip levels and mu; the main outputs carry 16 significant digits, whose rounding, up to ~6e-16 m, is of the size of the
    # bound itself): |mu_Rust - root| with the root of sum g f = N on those levels computed by this checker in 40 digits and the
    # difference taken in 40 digits.  The exact values must round to the committed 16-digit mu and levels.
    sb = Check("the Rust solver's stated first-order rounding bound of mu (thermodynamics.csv mu_rounding_bound, solver/src/mermin.rs), "
               "tested on the exact doubles of the canonical `single` run (`--mermin-levels`, shortest round-trip; they round to the "
               "committed 16-digit mu and levels): |mu_Rust - root| <= mu_rounding_bound, the root of sum g f = N on those levels and the "
               "difference in 40-digit arithmetic, in every thermal state")
    sb_worst, sb_rows = (-1.0, ""), {}
    for sid in tids:
        mx = rf[("thermo", sid)].get("canonical_mermin_exact")
        if mx is None or ("X", sid) not in mres:
            sb.flag(f"{sid}", False, "no exact Rust levels in checker/rust-refinement.json (re-run measure_rust_refinement.py) or reference missing")
            continue
        sb.flag(f"{sid} exact values round to the committed ones", mx["mu_rounds_to_16_digit_value"] and mx["levels_round_to_16_digit_values"]
                and float(f"{mx['mu']:.15e}") == float(th[sid]["mu"]), "the exact mu or levels do not round to the committed 16-digit values")
        dev, _ = mres[("X", sid)]
        bnd = num(th[sid].get("mu_rounding_bound"))
        ok = math.isfinite(bnd) and bnd > 0 and abs(dev) <= bnd
        sb.flag(f"{sid} bound", ok, f"|mu_Rust - root| = {fe(abs(dev))} > stated bound {fe(bnd)}")
        sb_rows[sid] = (dev, bnd)
        if math.isfinite(bnd) and bnd > 0 and abs(dev) / bnd > sb_worst[0]:
            sb_worst = (abs(dev) / bnd, f"{sid}: |mu_Rust - root| {fe(abs(dev))}, bound {fe(bnd)}")
    if sb_rows:
        big_d = max(sb_rows, key=lambda s: abs(sb_rows[s][0]))
        big_b = max(sb_rows, key=lambda s: sb_rows[s][1])
        forms = sorted({rf[("thermo", s)]["canonical_mermin_exact"]["root_form"] for s in sb_rows})
        sb.extra.append(f"root form of the canonical runs: {', '.join(forms)}; largest |mu_Rust - root| / bound {sb_worst[0]:.3f} ({sb_worst[1]}); "
                        f"largest |mu_Rust - root| {fe(abs(sb_rows[big_d][0]))} ({big_d}); largest stated bound {fe(sb_rows[big_b][1])} ({big_b})")
        if "N8_lamm1_a00_T10" in sb_rows:
            v = sb_rows["N8_lamm1_a00_T10"]
            sb.extra.append(f"N8_lamm1_a00_T10 (the state of the former 8.3e-10 m error): |mu_Rust - root| {fe(abs(v[0]))}, bound {fe(v[1])}")
    emit_check("thermo_mu_rust_stated_bound", sb)
    # data-driven diagnosis of failing mu / Omega comparisons
    for c in checks:
        if c["name"] == "thermo_state_functions" and c["verdict"] == "FAIL":
            notes = []
            failed = c["detail"][c["detail"].find("failures:"):]
            for sid, v in diag_rows.items():
                if f"{sid} mu " in failed or f"{sid} Omega" in failed:
                    notes.append(f"{sid}: the 40-digit roots of the Mermin condition on the Rust levels and on the reference levels agree to "
                                 f"{fe(abs(v['hp_rust_minus_hp_ref']))} (thermo_mu_high_precision); the Rust floating-point mu differs from "
                                 f"the root on its own levels by {fe(v['rust_mu_minus_hp'])} (conditioning bound {fe(v['rust_bound'])}, dN/dmu = "
                                 f"{fe(v['dN_dmu'])}); measured U_Rust(mu) = {fe(v['rust_U_mu_measured'])}; the reference mu differs from its "
                                 f"40-digit root by {fe(v['ref_mu_minus_hp'])}.")
            if notes:
                c["diagnosis"] = (c.get("diagnosis", "") + " " + " ".join(notes)).strip()

    # ---------------------------------------------------------------- determinism of the reference outputs (the checker runs the repeat)
    files = sorted(p for p in ref.rglob("*") if p.is_file())
    crlf = [p.relative_to(ref).as_posix() for p in files if b"\r\n" in p.read_bytes()]
    emit("reference_outputs_lf_only", not crlf, f"{len(files)} reference result files; files with CRLF: {crlf if crlf else 'none'}")
    man = load(ref / "manifest.json")["files"]
    bad_hash = [n for n, h in man.items() if not (ref / n).exists() or hashlib.sha256((ref / n).read_bytes()).hexdigest() != h]
    emit("reference_manifest", not bad_hash and len(man) == len(files) - 1,
         f"manifest.json lists {len(man)} files with SHA-256 ({len(files) - 1} result files besides it); mismatches: {bad_hash if bad_hash else 'none'}")
    print(f"running the reference repeat into {work / 'reference-repeat'} ({args.jobs} processes) ...", file=sys.stderr, flush=True)
    rep_dir, rep_report, secs, rep_ok = run_reference_repeat(work, args.jobs)
    timing["reference_repeat"] = secs
    f2 = sorted(p for p in (rep_dir / "results").rglob("*") if p.is_file())
    names1 = [p.relative_to(ref).as_posix() for p in files]
    names2 = [p.relative_to(rep_dir / "results").as_posix() for p in f2]
    differ = [n for n in names1 if n in names2 and (ref / n).read_bytes() != (rep_dir / "results" / n).read_bytes()]
    same_report = rep_report.exists() and rep_report.read_bytes() == Path(args.reference_report).read_bytes()
    emit("reference_repeat_byte_identical", rep_ok and names1 == names2 and not differ and same_report,
         f"this checker ran run_reference.py again into a fresh directory (<work>/reference-repeat; exit SUCCESS: {rep_ok}): {len(names2)} result "
         f"files, same file set: {names1 == names2}, differing files: {differ if differ else 'none'}; report ks-reference.json byte-identical: "
         f"{same_report}")

    npass = sum(c["verdict"] == "PASS" for c in checks)
    report = {
        "report": "Revision Kohn-Sham cross-check: Rust solver vs the independent Python reference (different discretisation) on the FULL canonical matrix",
        "producer": "Revision/kohn_sham/checker/crosscheck_ks.py",
        "tolerance_rule": "|x_Rust - x_ref| <= 3 (U_ref + U_Rust) + 1e-12 scale; U_ref = the reference's three-grid Richardson uncertainty "
                          "(validated on a fourth grid); U_Rust = (16/15) |canonical - refined| measured per state (checker/rust-refinement.json) or, "
                          "where `single` does not report the quantity, the matrix-wide maximum of ks-rust-determinism.json or a stated propagation "
                          "of measured uncertainties; |single - matrix| is added where the two take different SCF paths (exact-Fock variant); "
                          "scale = max(1, |x|) for scalars, the profile maximum for profiles. Fixed before the comparison.",
        "rust_matrix_wide_uncertainties": G,
        "matrix": {"ground": len(gids), "thermal": len(tids), "exact_fock_variant": len(exx), "rescaling_partners": sum(1 for _ in read_csv(rust / "rescaling" / "rescaling.csv")),
                   "particle_hole_lists": len(gids), "crossing_demo_slices": len(demo_rows)},
        "comparisons": sum(1 for _ in table) + C["ground_eigenvalues"].n + C["ground_profiles"].n + TL.n,
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
    timing["total"] = time.time() - t_all
    print("timing: " + ", ".join(f"{k} {v:.1f} s" for k, v in timing.items()), file=sys.stderr)
    print("SUCCESS" if npass == len(checks) else "FAILURE")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
