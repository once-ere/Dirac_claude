#!/usr/bin/env python3
"""Revision/universe_model/solution/solve_model.py - step [4] of UM-1: assemble the approximate solution of the coupled
field equations from its parts, check it, draw the figures and write the generated tables of SOLUTION.md.

Parts (each a module of this folder):
  vacua.py       the Einstein-Lovelock background: static vacuum, effective Newton constant, block mode, slow deflation
  masses.py      the x0 mass spectrum (W, Z, photon, gluon, graviton, e, u, d, nu) and its fit
  ks_coupled.py  the Kohn-Sham solution of dirac16complex with the portal mean fields and the block feedback
                 (run first: python ks_coupled.py all; its outputs are read from outputs/ks/)
  cosmology.py   CMB (theta*, l_A, l_1), BAO (eBOSS DR16), CNB, N_eff

Outputs: outputs/{vacua,masses,cosmology,late_time,solution}.json, reports/solution-checks.json, figures/*.png and the
block between the GENERATED markers of ../SOLUTION.md.  Exit code 0 iff every check passes.
Usage: python solve_model.py"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt   # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import vacua as V          # noqa: E402
import masses as MS        # noqa: E402
import cosmology as CO     # noqa: E402

OUT, KSO, FIG, REP = HERE / "outputs", HERE / "outputs" / "ks", HERE / "figures", HERE / "reports"
DOC = HERE.parent / "SOLUTION.md"
HBAR_GEV_S = 6.582119569e-25
MPC_KM = 3.0856775814913673e19
KS_FILES = ("spectrum", "portal8_lam0", "portal8_lam1", "portal592_lam0", "portal592_lam1", "dm_lam0", "dm_lam1", "loop")


def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1, sort_keys=True, default=float) + "\n", encoding="utf-8", newline="\n")


def g(x, d=4):
    """a number for the tables: d significant digits"""
    if isinstance(x, str):
        return x
    if x == 0:
        return "0"
    if abs(x) >= 1e5 or abs(x) < 1e-3:
        m, e = ("%.*e" % (d - 1, x)).split("e")
        return "%s \\times 10^{%d}" % (m, int(e))
    t = "%.*g" % (d, x)
    return t if "e" not in t else "%.0f" % x


def null_hf(pr):
    return abs(pr["dE_de_hf"]) < 1e-18 and abs(pr["dE_de_fd"]) < 1e-18


def null_y(fi, rec):
    """every term of the identity at roundoff: below 1e-12 of the density scale of the state (rho, p3, n m)"""
    scale = max(abs(rec["sources"][k]) for k in ("rho_bar", "p3_bar", "n_bar"))
    return max(abs(fi["ycons_jump"]), abs(fi["ycons_integral"]), abs(fi["ycons_force"])) < 1e-12 * scale


class Checks:
    def __init__(self):
        self.rows = []

    def add(self, name, ok, detail):
        self.rows.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})


def main():
    ks = {}
    for nm in KS_FILES:
        p = KSO / (nm + ".json")
        if not p.exists():
            print("ERROR  missing %s: run python ks_coupled.py all first" % p)
            return 1
        ks[nm] = json.loads(p.read_text(encoding="utf-8"))
    vac = V.analyse()
    dump(OUT / "vacua.json", vac)
    ms = MS.fit()
    dump(OUT / "masses.json", ms)
    sp = ks["spectrum"]["vacuum"]
    Hg = ms["scales"]["H_GeV"]
    m_dm = sp["lowest_odd_bulk_k0"] * Hg                      # KS units m = H
    co = CO.analyse(g_F=sp["g_F"], m_dm_GeV=m_dm)
    dump(OUT / "cosmology.json", co)
    ch = Checks()

    # ---------------- vacua
    ch.add("V1_static_block_closed_forms", vac["part1_static_block_forms"]["closed_forms_hold"],
           "the three components on the static-block slicing equal the stated closed forms for general w2, w3")
    sv = vac["part2_static_vacuum"]
    ch.add("V2_unique_static_vacuum", sv["unique_nonzero"] and sv["solutions"][0]["k0"] == "1/(4*w2)",
           "k0 = %s, Lambda0 = %s, G(k0) = %s" % (sv["solutions"][0]["k0"], sv["solutions"][0]["Lambda0"], sv["G_k0"]))
    bm = vac["part3_block_mode_general"]
    ch.add("V3_block_mode_theorem", bm["lambda2_equals_k0_G_H2_over_4"] and bm["constraint_linearised"] == "0",
           "characteristic polynomial %s: lambda^2 = k0 G(k0) H^2/4 identically; the linearised constraint vanishes" % bm["charpoly"])
    au, be = vac["part4_author"], vac["part4_benchmark"]
    ch.add("V4_author_and_benchmark", au["G_k0"] == "-1" and be["G_k0"] == "1",
           "author's weights: G(k0) = %s (%s gravity, block %s); benchmark w3 = 1/768: G(k0) = %s (%s, block %s)"
           % (au["G_k0"], au["gravity"], au["block"], be["G_k0"], be["gravity"], be["block"]))

    # ---------------- masses
    ch.add("M1_neumann_exact", ms["neumann"]["max_rel_dev"] < 1e-10,
           "numerical Neumann levels vs 9 eta^2/4 + n^2 pi^2: %.2e" % ms["neumann"]["max_rel_dev"])
    dt = ms["dirichlet_tip"]
    ch.add("M2_dirichlet_tip_limit", abs(dt["Lambda_D_numeric_beta_1e7"] / dt["Lambda_D"] - 1) < 1e-5,
           "beta = 1e7 level %.8g vs tanh q = 2q/(3 eta): %.8g; m_W <= %.5f m_KK for every positive tip term"
           % (dt["Lambda_D_numeric_beta_1e7"], dt["Lambda_D"], dt["mW_max_over_mKK"]))
    ga = ms["gauge"]
    ch.add("M3_W_level_and_rayleigh", abs(ga["Lambda_W_back"] / ga["Lambda_W"] - 1) < 1e-9 and abs(ga["rayleigh_W"]["sum_rel_dev"]) < 1e-4
           and ga["beta_W"] > 0 and ga["beta_Z"] > 0,
           "beta_W = %.6g > 0 reproduces Lambda_W; Rayleigh quotient (bulk + tip) / Lambda_W - 1 = %.2e"
           % (ga["beta_W"], ga["rayleigh_W"]["sum_rel_dev"]))
    ch.add("M4_rho_fit", abs(ga["rho_minus_1"] - MS.OBS["rho0_minus_1"]) < 1e-8,
           "m_KK = %.6g GeV gives rho - 1 = %.6g (target %.5g)" % (ms["inputs"]["m_KK_GeV"], ga["rho_minus_1"], MS.OBS["rho0_minus_1"]))
    fe = ms["fermions"]
    ch.add("M5_fermion_zero_modes", all(abs(fe[s]["zeta2"] / fe[s]["ratio_to_mKK"] - 1) < 1e-10 and
                                        abs(fe[s]["width_t"] / fe[s]["width_t_exact"] - 1) < 1e-5 for s in fe),
           "zeta(c_f)^2 = m_f/m_KK and the width of e^{2ct} vs its closed form, for e, u, d, nu")
    ch.add("M6_x0_periodicity", ms["periodicity"]["max_abs_u(x0+pi/6H)-u(x0)"] < 1e-12,
           "the W profile at x0 + pi/(6H) equals that at x0: %.1e" % ms["periodicity"]["max_abs_u(x0+pi/6H)-u(x0)"])
    ch.add("M7_massless", ga["photon_gluon_graviton"]["massless"],
           "the photon, gluon and graviton zero modes (Neumann, beta = 0) have Lambda_0 = 0 exactly")

    # ---------------- Kohn-Sham
    s0 = ks["spectrum"]["a4_0"]
    ch.add("K1_record_bulk_edge", s0["bulk_edge_rel_dev_vs_record"] < 1e-10,
           "bulk edge at a4 = 0: %.13g vs the record's %.13g" % (s0["bulk_edge"], s0["record_bulkEdge"]))
    ch.add("K2_analytic_k0_levels", sp["analytic_max_rel_dev"] < 1e-10 and s0["analytic_max_rel_dev"] < 1e-10,
           "lowest odd and even bulk levels vs ks-theory.json exactK0Spectra: %.1e (vacuum), %.1e (a4 = 0)"
           % (sp["analytic_max_rel_dev"], s0["analytic_max_rel_dev"]))
    ch.add("K3_fold_band", sp["fold_band_slope_rel_dev"] < 1e-9 and sp["g_F"] == 8 and sp["N_zero_modes"] == 8,
           "massless fold band eps = kappa |k| (slope deviation %.1e), g_F = %d states per 3-momentum (4 particles, 4 antiparticles)"
           % (sp["fold_band_slope_rel_dev"], sp["g_F"]))
    hfmax, ymax, ydecr, nulls = 0.0, 0.0, True, []
    for nm in ("portal8_lam0", "portal8_lam1", "portal592_lam0", "portal592_lam1"):
        cs = ks[nm]["cases"]
        for lamtag, per in cs.items():
            res_by_G = {}
            for G, rec in per.items():
                for pn, pr in rec["portals"].items():
                    if null_hf(pr):
                        nulls.append("%s %s G=%s (HF)" % (nm, pn, G))
                    else:
                        hfmax = max(hfmax, pr["hf_rel_dev"])
                    fi = pr["finite"]
                    if null_y(fi, rec):
                        nulls.append("%s %s G=%s (exchange)" % (nm, pn, G))
                    else:
                        ymax = max(ymax, fi["ycons_residual_rel"])
                        res_by_G.setdefault(pn, {})[int(G)] = fi["ycons_residual_rel"]
            for pn, d in res_by_G.items():
                if len(d) >= 2:
                    Gs = sorted(d)
                    ydecr = ydecr and (d[Gs[-1]] <= d[Gs[0]] or d[Gs[-1]] < 1e-8)
    ch.add("K4_hellmann_feynman", hfmax < 1e-6,
           "dE_KS/de (Richardson differences, fixed occupations) = int (dM/de S + dv/de n) for every portal, N, lambda, grid: "
           "largest relative deviation %.2e; null cases (|dE/de| and the expectation both below 1e-18, the scalar portals on "
           "the chiral zero modes, whose scalar density vanishes): %d" % (hfmax, sum("(HF)" in x for x in nulls)))
    ch.add("K5_y_exchange_identity", ymax < 1e-3 and ydecr,
           "[e^{3Hy} p0] - 3H int e^{3Hy} p_t = -int e^{3Hy}(M_ext' S + v_ext' n) at e = 0.02: largest relative residual %.2e, "
           "falling with the grid: %s; null cases (every term below 1e-12 of the density scale of the state): %d" % (ymax, ydecr, sum("(exchange)" in x for x in nulls)))
    dm = dict(ks["dm_lam0"]["cases"], **ks["dm_lam1"]["cases"])
    # the dark-matter energy bookkeeping: the energy added by 8 odd quanta (fixed occupations, the EMT integrated over the
    # cell, three grids, Richardson) equals 8 times the analytic lowest odd level at lambda = 0 (w = 0 there holds by
    # construction, k = 0 and e_int = 0, and is a result, not a check)
    dE8 = dm["lam0"]["richardson"]["dE"][0]
    e_an = sp["lowest_odd_bulk_analytic"]
    ch.add("K6_dark_matter_energy", abs(dE8 / (8.0 * e_an) - 1.0) < 1e-9,
           "E(N = 8 + 8 odd quanta) - E(N = 8) = %.12g vs 8 x the analytic odd level %.12g (relative %.1e)"
           % (dE8, 8.0 * e_an, abs(dE8 / (8.0 * e_an) - 1.0)))
    lp = ks["loop"]["runs"]
    ch.add("K7_coupled_fixed_point", all(r["converged"] for r in lp),
           "Psi <-> Standard Model <-> block fixed point converged for sigma = %s in %s iterations"
           % ([r["sigma"] for r in lp], [r["iterations"] for r in lp]))

    # ---------------- cosmology
    lc = co["lcdm_planck"]
    ch.add("C1_calibration_LCDM", abs(lc["obs"]["theta_star_100"] - CO.PLANCK["theta_star_100"]) < 1e-9 and
           abs(lc["obs"]["r_drag_Mpc"] - CO.PLANCK["r_drag_Mpc"]) < 1e-9 and lc["bao_chi2"] < 2 * len(CO.BAO),
           "the calibrated formulae reproduce Planck LCDM (100 theta* = %.5f, r_drag = %.2f Mpc); its eBOSS chi^2 = %.2f for %d points"
           % (lc["obs"]["theta_star_100"], lc["obs"]["r_drag_Mpc"], lc["bao_chi2"], len(CO.BAO)))
    fit = co["um1"]["fit_to_Planck_Neff"]
    ch.add("C2_Neff_fit_scenario", abs(fit["N_eff"] - CO.PLANCK["N_eff_measured"]) < 1e-9,
           "g_*s at the Psi decoupling = %.4f gives N_eff = %.3f" % (fit["g_star_s_at_decoupling"], fit["N_eff"]))
    cn = fit["cnb"]
    ch.add("C3_CNB_temperature", abs(cn["T_nu_over_T_gamma"] - (4 / 11) ** (1 / 3)) < 1e-12,
           "T_nu/T_gamma = (4/11)^{1/3} = %.6f (T_nu = %.4f K)" % (cn["T_nu_over_T_gamma"], cn["T_nu_K"]))

    # ---------------- late time: deflation, drift, Lambda tuning
    H0_GeV = fit["H0"] / MPC_KM * HBAR_GEV_S
    AH2 = (H0_GeV / Hg) ** 2
    q0 = 0.5 * (CO.PLANCK["omega_b"] + CO.PLANCK["omega_c"]) / fit["h_fitted_to_theta_star"] ** 2 * 3 - 1      # q = (3/2) Om - 1
    late = {"H_GeV": Hg, "H0_GeV": H0_GeV, "A_over_H_squared": AH2,
            "h4_over_A_today": -4.0 * (1.0 + q0) / 8.0 * AH2,
            "mass_drift_per_hubble_time": 4.0 * (1.0 + q0) / 8.0 * AH2,
            "deltaLambda_over_H2": 3.0 * (1 - (CO.PLANCK["omega_b"] + CO.PLANCK["omega_c"]) / fit["h_fitted_to_theta_star"] ** 2) * AH2,
            "block_mode_lambda2_over_H2_benchmark": 8 * 1 / 4.0, "q0": q0, "m_dm_GeV": m_dm,
            "m_Psi_GeV": Hg, "fold_radiation_massless": True}
    dump(OUT / "late_time.json", late)
    dump(REP / "solution-checks.json", {"checks": ch.rows, "pass": sum(r["verdict"] == "PASS" for r in ch.rows),
                                        "total": len(ch.rows)})
    figures(vac, ms, ks, co)
    write_generated(vac, ms, ks, co, late, ch)
    npass = sum(r["verdict"] == "PASS" for r in ch.rows)
    for r in ch.rows:
        print(r["verdict"], r["name"], "-", r["detail"])
    print("%d/%d checks pass" % (npass, len(ch.rows)))
    return 0 if npass == len(ch.rows) else 1


def figures(vac, ms, ks, co):
    FIG.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 10, "figure.dpi": 130})
    # 1: the effective Newton factor and the block mode
    k = np.linspace(0, 14, 600)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for (w2, w3), lab in ((V.AUTHOR, "author: w = (1, 1/32, 1/1152)"), (V.BENCHMARK, "benchmark: w = (1, 1/32, 1/768)")):
        G = 1 - 24 * float(w2) * k + 72 * float(w3) * k ** 2
        ax.plot(k, G, label=lab)
    ax.axhline(0, color="k", lw=0.6)
    ax.axvline(8, color="gray", ls="--", lw=0.8)
    ax.text(8.15, 2.2, "static vacuum k0 = 1/(4 w2) = 8", fontsize=8)
    ax.set_xlabel("k = e^{2 a4}/b4")
    ax.set_ylabel("G(k) = G_Einstein/G_eff")
    ax.set_title("Effective 4D Newton factor; block mode lambda^2 = k0 G(k0) H^2/4")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "fig1_newton_factor.png")
    plt.close(fig)
    # 2: profiles over two x0 periods
    eta = ms["inputs"]["eta_HL"]
    z = np.linspace(1e-4, 2 * math.pi - 1e-4, 6000)
    y = np.log(np.abs(np.sin(z))) / 6.0
    t = np.clip(y / eta, -1, 0)
    _, _, uW = MS.shoot(ms["gauge"]["Lambda_W"], eta, profile=True)
    tg = np.linspace(0, -1, len(uW))
    W = np.interp(-t, -tg, uW)
    ce = ms["fermions"]["e"]["c_f"]
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    bend = (W - 1.0) / np.max(np.abs(W - 1.0))
    ax.plot(z / 6.0, 1.0 + 0.5 * bend, label="W profile: 1 + (u - 1)/(2 max|u - 1|), max|u - 1| = %.1e" % np.max(np.abs(W - 1.0)))
    ax.plot(z / 6.0, np.exp(2 * ce * t), label="electron zero-mode density e^{2 c_e y/L}")
    ax.plot(z / 6.0, np.ones_like(z), ls=":", label="photon / gluon / graviton (flat)")
    ax.axvline(math.pi / 6, color="gray", lw=0.6)
    ax.set_xlabel("H x0   (period pi/6 = pi/(6H))")
    ax.set_ylabel("profile")
    ax.set_title("x0 wave functions over two periods")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "fig2_x0_profiles.png")
    plt.close(fig)
    # 3: rho - 1 vs m_KK
    sc = ms["rho_scan"]
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.loglog([r["m_KK_GeV"] / 1e3 for r in sc], [r["rho_minus_1"] for r in sc], "o-", label="UM-1 tree level")
    ax.axhspan(MS.OBS["rho0_minus_1"] - MS.OBS["rho0_sigma"], MS.OBS["rho0_minus_1"] + MS.OBS["rho0_sigma"], color="C1", alpha=0.3,
               label="PDG rho0 - 1 (1 sigma)")
    ax.axvline(ms["inputs"]["m_KK_GeV"] / 1e3, color="gray", ls="--", lw=0.8)
    ax.set_xlabel("m_KK (TeV)")
    ax.set_ylabel("rho - 1")
    ax.legend(fontsize=8)
    ax.set_title("Custodial deviation of the Higgsless tip")
    fig.tight_layout()
    fig.savefig(FIG / "fig3_rho.png")
    plt.close(fig)
    # 4: N_eff vs g_*s at decoupling
    gF = ks["spectrum"]["vacuum"]["g_F"]
    gg = np.linspace(7.25, 60, 400)
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    for gf, ls_ in ((gF, "-"), (gF // 2, "--")):
        ne = CO.NEFF_PER_SPECIES + np.array([CO.delta_neff(gf, x) for x in gg])
        ax.plot(gg, ne, ls_, label="N_eff = 1.0147 + (g_F/2)(7.25/g_dec)^{4/3}, g_F = %d%s" % (gf, "" if gf == gF else " (one half of the cell)"))
    ax.axhspan(CO.PLANCK["N_eff_measured"] - CO.PLANCK["N_eff_sigma"], CO.PLANCK["N_eff_measured"] + CO.PLANCK["N_eff_sigma"],
               color="C1", alpha=0.3, label="Planck 2018 N_eff (1 sigma)")
    for nm, s in co["um1"].items():
        ax.plot([s["g_star_s_at_decoupling"]], [s["N_eff"]], "k.")
        ax.annotate(nm, (s["g_star_s_at_decoupling"], s["N_eff"]), fontsize=7, xytext=(4, 4), textcoords="offset points")
    ax.set_xlabel("g_*s of the Standard-Model plasma at the Psi decoupling")
    ax.set_ylabel("N_eff")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "fig4_neff.png")
    plt.close(fig)
    # 5: BAO pulls
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for lab, rows, off in (("Planck LCDM", co["lcdm_planck"]["bao"], -0.012), ("UM-1 (N_eff fit)", co["um1"]["fit_to_Planck_Neff"]["bao"], 0.012),
                           ("UM-1 (pion-gas decoupling)", co["um1"]["pion_gas"]["bao"], 0.036)):
        zz = [r["z"] + off for r in rows]
        ax.errorbar(zz, [r["pred"] / r["obs"] for r in rows], yerr=[r["sigma"] / r["obs"] for r in rows], fmt="o", ms=3, label=lab)
    ax.axhline(1, color="k", lw=0.6)
    ax.set_xlabel("z")
    ax.set_ylabel("prediction / eBOSS DR16")
    ax.set_title("BAO: D_M/r_d, D_H/r_d, D_V/r_d")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "fig5_bao.png")
    plt.close(fig)
    # 6: the Psi spectrum at the vacuum slice (k = 0 and |k| = dk levels by sector)
    lev = ks["spectrum"]["vacuum"]["levels"]
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    names = list(lev)
    for i, nm in enumerate(names):
        for r in ("rank-1", "rank0", "rank1", "rank2"):
            ax.plot([i], [lev[nm][r][0]], "_", ms=18, color="C0" if "0)" in nm[-3:] else "C3")
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=30, fontsize=7)
    ax.set_ylabel("eps / m")
    ax.set_title("Psi levels at the vacuum slice (n2, r3, j, odd): blue even, red odd")
    fig.tight_layout()
    fig.savefig(FIG / "fig6_psi_levels.png")
    plt.close(fig)


def write_generated(vac, ms, ks, co, late, ch):
    sp = ks["spectrum"]["vacuum"]
    ga, fe, sc = ms["gauge"], ms["fermions"], ms["scales"]
    L = []
    L.append("### 9.1 Generated tables (from `solution/solve_model.py`; every number below is from the run)")
    L.append("")
    L.append("**Vacuum and block (vacua.py).**")
    L.append("")
    L.append("| weights $w$ | $k_0$ | $\\Lambda_0/H^2$ | $G(k_0)$ | 4D gravity | block mode $\\lambda^2/H^2$ |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for tag in ("author", "benchmark"):
        r = vac["part4_" + tag]
        Gv = float(eval(r["G_k0"]))
        L.append("| (%s) | %s | %s | %s | %s | %s (%s) |" % (", ".join(r["w"]), r["k0"], r["Lambda0"].replace("*H**2", ""), r["G_k0"],
                                                            r["gravity"], g(8 * Gv / 4), r["block"]))
    L.append("")
    L.append("**Mass spectrum (masses.py; $\\eta = HL = 3$, $f = k_0^{-1/2}$).**")
    L.append("")
    L.append("| quantity | value |")
    L.append("| --- | --- |")
    L.append("| $m_{KK}$ (first photon/gluon/graviton KK level, fitted to $\\rho_0 - 1$) | $%s$ GeV |" % g(ms["inputs"]["m_KK_GeV"]))
    L.append("| $H$ | $%s$ GeV |" % g(sc["H_GeV"]))
    L.append("| proper half-cell $fL$ | $%s$ m |" % g(sc["fL_m"]))
    L.append("| period of $x_0$, $\\pi/(6H)$ | $%s$ GeV$^{-1}$ = $%s$ m |" % (g(sc["x0_period_pi_over_6H_GeV^-1"]), g(sc["x0_period_m"])))
    L.append("| largest $m_W$ of a positive tip term | $%s\\, m_{KK}$ (so $m_{KK} \\geq %s$ GeV) |" % (g(ms["dirichlet_tip"]["mW_max_over_mKK"]), g(ms["dirichlet_tip"]["m_KK_min_GeV"])))
    L.append("| $\\beta_W$, $\\beta_Z$ (tip Robin parameters) | $%s$, $%s$ |" % (g(ga["beta_W"]), g(ga["beta_Z"])))
    L.append("| $m_Z$ predicted (from $m_W$, on-shell $\\cos^2\\theta_W$) | $%s$ GeV (observed %s; difference $%s$ GeV) |" % (g(ga["m_Z_pred_GeV"], 7), ga["m_Z_obs_GeV"], g(ga["m_Z_pred_minus_obs_GeV"])))
    L.append("| $\\rho - 1$ (tree) | $%s$ |" % g(ga["rho_minus_1"]))
    L.append("| W: bulk hidden-momentum part / tip part of $m_W^2$ | $%s$ / $%s$ |" % (g(ga["rayleigh_W"]["bulk_hidden_momentum"] / ga["Lambda_W"]), g(ga["rayleigh_W"]["tip"] / ga["Lambda_W"])))
    L.append("| first W KK level | $%s$ GeV |" % g(ga["W_tower_GeV"][1] if len(ga["W_tower_GeV"]) > 1 else float("nan")))
    L.append("| photon, gluon, graviton | $\\Lambda_0 = 0$: massless |")
    L.append("")
    L.append("| fermion | $m_f$ (GeV) | $m_f/m_{KK} = \\zeta(c_f)^2$ | $c_f = f\\mu_f L$ | $\\mu_f/H$ |")
    L.append("| --- | --- | --- | --- | --- |")
    for s in ("nu", "e", "u", "d"):
        r = fe[s]
        L.append("| %s | $%s$ | $%s$ | %s | %s |" % (s, g(r["m_obs_GeV"]), g(r["zeta2"]), g(r["c_f"]), g(r["mu_f_over_H"])))
    L.append("")
    L.append("| fermion | width $\\Delta t$ | $\\Delta s$ (m) | $\\hbar c/(2\\Delta s)$ (GeV) | $m_f$ / Heisenberg estimate |")
    L.append("| --- | --- | --- | --- | --- |")
    for s in ("nu", "e", "u", "d"):
        r = fe[s]
        L.append("| %s | %s | $%s$ | $%s$ | $%s$ |" % (s, g(r["width_t"]), g(r["Delta_s_m"]), g(r["heisenberg_mass_GeV"]), g(r["m_over_heisenberg"])))
    L.append("")
    L.append("**dirac16complex, Kohn-Sham (ks_coupled.py; units $m = H$).**")
    L.append("")
    L.append("| quantity | value |")
    L.append("| --- | --- |")
    L.append("| vacuum slice $a_{4} = 3\\ln 8/2$, $f$, $\\kappa = e^{-a_4}$ | %s, %s, %s |" % (g(ks["spectrum"]["a4_vac"]), g(sp["f"]), g(sp["kappa"])))
    L.append("| fold zero modes; fold band | %d at $k = 0$; $\\varepsilon = \\kappa|k|$ exactly (massless), $g_F = %d$ |" % (sp["N_zero_modes"], sp["g_F"]))
    L.append("| lowest odd bulk level (dark matter) | $%s\\,m$ = $%s$ GeV |" % (g(sp["lowest_odd_bulk_k0"], 7), g(sp["lowest_odd_bulk_k0"] * sc["H_GeV"])))
    L.append("| lowest even bulk level | $%s\\,m$ |" % g(sp["lowest_even_bulk_k0"], 7))
    dmr = dict(ks["dm_lam0"]["cases"], **ks["dm_lam1"]["cases"])
    for tag in ("lam0", "lam157.7"):
        if tag in dmr and "richardson" in dmr[tag]:
            rr = dmr[tag]["richardson"]
            L.append("| dark matter (%s): energy per 8 quanta, $w = p_3/\\rho$, $p_0/\\rho$ | $%s$, $%s$, $%s$ |" % (tag.replace("lam", "$\\lambda$ = "), g(rr["dE"][0], 7), g(rr["w_dm"][0]), g(rr["p0_over_rho_dm"][0])))
    L.append("")
    tabA = ["| state (grid 600) | portal | $dE_{KS}/de$ | Hellmann-Feynman deviation | y-exchange residual ($e = 0.02$) |",
            "| --- | --- | --- | --- | --- |"]
    tabB = ["| state (grid 600) | portal | $d\\varepsilon_{DM}/de$ | $d(\\varepsilon_{n2=1} - \\varepsilon_0)/de$ | $d\\bar p_0/de$ |",
            "| --- | --- | --- | --- | --- |"]
    for nm in ("portal8_lam0", "portal8_lam1", "portal592_lam0", "portal592_lam1"):
        d = ks[nm]
        rec = d["cases"][list(d["cases"])[0]]
        Gm = str(max(int(x) for x in rec))
        for pn, pr in rec[Gm]["portals"].items():
            nh, ny = null_hf(pr), null_y(pr["finite"], rec[Gm])
            lab = "N = %d, $\\lambda$ = %s | %s" % (d["N"], g(d["lambda"]), pn)
            tabA.append("| %s | %s | %s | %s |" % (lab, "$%s$" % g(pr["dE_de_fd"]) if not nh else "0",
                                                   "$%s$" % g(pr["hf_rel_dev"]) if not nh else "null (both zero)",
                                                   "$%s$" % g(pr["finite"]["ycons_residual_rel"]) if not ny else "null (all terms zero)"))
            tabB.append("| %s | %s | %s | %s |" % (lab, "$%s$" % g(pr["d_dm_level_de"]),
                                                   "$%s$" % g(pr["d_fold_gap_n2_1_de"]) if abs(pr["d_fold_gap_n2_1_de"]) > 1e-14 else "below $10^{-14}$",
                                                   "$%s$" % g(pr["d_p0_bar_de"]) if not nh else "0"))
    L.extend(tabA)
    L.append("")
    L.extend(tabB)
    L.append("")
    L.append("| coupled fixed point | iterations | contraction | $\\delta k$ | $\\delta f/f$ | $\\delta m_e/m_e$ | $\\delta m_\\nu/m_\\nu$ |")
    L.append("| --- | --- | --- | --- | --- | --- | --- |")
    for r in ks["loop"]["runs"]:
        L.append("| $\\sigma$ = %s | %d | %s | $%s$ | $%s$ | $%s$ | $%s$ |" % (g(r["sigma"]), r["iterations"],
                                                                         "$%s$" % g(r["contraction"]) if r.get("contraction") is not None else "-",
                                                                         g(r["dk"]), g(r["df_over_f"]), g(r["dm_over_m"]["e"]), g(r["dm_over_m"]["nu"])))
    L.append("")
    L.append("**Cosmology (cosmology.py).**")
    L.append("")
    L.append("| model | $g_{*s}$ at decoupling | $N_{eff}$ | pull vs Planck | $H_0$ (km/s/Mpc) | BAO $\\chi^2$ (12 points) |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    lc = co["lcdm_planck"]
    L.append("| Planck LCDM (reference) | - | 3.046 | - | 67.36 | %s |" % g(lc["bao_chi2"]))
    for nm, s in co["um1"].items():
        L.append("| UM-1, %s | %s | %s | %s | %s | %s |" % (nm.replace("_", " "), g(s["g_star_s_at_decoupling"]), g(s["N_eff"]),
                                                          g(s["N_eff_pull_vs_Planck"], 3), g(s["H0"]), g(s["bao_chi2"])))
    L.append("")
    L.append("| model | $100\\theta_*$ | $z_*$ | $r_{drag}$ (Mpc) | $\\ell_A$ | $\\ell_1$ |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    L.append("| Planck LCDM (reference) | %s | %s | %s | %s | %s |" % (g(lc["obs"]["theta_star_100"], 6), g(lc["obs"]["z_star"], 6), g(lc["obs"]["r_drag_Mpc"], 5),
                                                                  g(lc["obs"]["l_A"], 5), g(lc["obs"]["l_1"], 4)))
    for nm, s in co["um1"].items():
        L.append("| UM-1, %s | %s | %s | %s | %s | %s |" % (nm.replace("_", " "), g(s["obs"]["theta_star_100"], 6), g(s["obs"]["z_star"], 6),
                                                          g(s["obs"]["r_drag_Mpc"], 5), g(s["obs"]["l_A"], 5), g(s["obs"]["l_1"], 4)))
    cn = co["um1"]["fit_to_Planck_Neff"]["cnb"]
    L.append("")
    L.append("| background today | value |")
    L.append("| --- | --- |")
    L.append("| $T_\\nu = (4/11)^{1/3}T_{CMB}$ | %s K |" % g(cn["T_nu_K"], 5))
    L.append("| $n_\\nu$ (one species, $\\nu + \\bar\\nu$) | %s cm$^{-3}$ |" % g(cn["n_nu_per_species_cm3"], 4))
    L.append("| $T_\\Psi$ of the fold band (N_eff fit) | %s K |" % g(cn["T_Psi_fold_K"], 4))
    L.append("| $n_\\Psi$ of the fold band ($g_F = %d$) | %s cm$^{-3}$ |" % (sp["g_F"], g(cn["n_Psi_fold_cm3"], 4)))
    L.append("| $(H_0/H)^2$ | $%s$ |" % g(late["A_over_H_squared"]))
    L.append("| deflation today $h_4/\\dot a_4$ | $%s$ |" % g(late["h4_over_A_today"]))
    L.append("| $\\delta\\Lambda/H^2$ (dark energy) | $%s$ |" % g(late["deltaLambda_over_H2"]))
    L.append("")
    L.append("**Checks** (`solution/reports/solution-checks.json`, %d of %d PASS): %s." % (sum(r["verdict"] == "PASS" for r in ch.rows), len(ch.rows),
                                                                                       ", ".join(r["name"].split("_")[0] for r in ch.rows if r["verdict"] == "PASS")))
    block = "\n".join(L)
    if DOC.exists():
        txt = DOC.read_text(encoding="utf-8")
        new = re.sub(r"<!-- BEGIN GENERATED -->.*<!-- END GENERATED -->",
                     lambda m: "<!-- BEGIN GENERATED -->\n\n" + block + "\n\n<!-- END GENERATED -->", txt, flags=re.S)
        DOC.write_text(new, encoding="utf-8", newline="\n")
    (OUT / "generated_tables.md").write_text(block + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    sys.exit(main())
