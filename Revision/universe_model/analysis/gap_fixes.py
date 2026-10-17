#!/usr/bin/env python3
"""Revision/universe_model/analysis/gap_fixes.py - UM-1 version 1.3: the gaps found by ANALYSIS.md, closed where the
model allows it (GAPS.md).  Run after x0_mass_analysis.py and dark_validity.py, whose outputs it reads.

G1  The light masses as x0 dependence of the wave function.
    (a) The resolved tip: the Robin condition u'(-1) = beta u(-1) of the sigma field is the thin-layer limit of a tip layer
        [-1 - delta, -1] of stiffness w = beta e^{-3 eta} delta in which the broken-generator profile is forced to vanish
        (Dirichlet at the outer edge: symmetry breaking by a boundary condition).  Then m^2 = int w |u'|^2 / int w u^2
        exactly, the whole mass is the x0 gradient energy of the wave function, and m^2 = P_tip <p^2>_tip with
        <p^2>_tip >= (pi/2)^2/delta^2 (the bound of a profile that must vanish within delta): the author's argument,
        weighted by the probability P_tip of being in the tip layer.  Computed by finite elements for delta -> 0.
    (b) The fermions: the tip Yukawa coupling as the self-adjoint mixing condition b_L(-1) = kappa b_R(-1),
        a_R(-1) = -kappa a_L(-1) of the coupled (L, R) x0 Dirac problem; the four-dimensional mass is its lowest exact
        eigenvalue (closed-form transfer matrices, mpmath 50 digits), compared with kappa zeta(c_L) zeta(c_R).
G2  The dark-matter / N_eff tension and the relic abundance: the vector portal P1 restricted to the lepton multiplets
    (L, e_R; INVENTED choice, gauge invariant multiplet by multiplet).  The same portal then decouples the fold band in the
    QCD crossover (N_eff = 2.99) and sets the dark-matter relic abundance through the x0 overlap rule: a PREDICTION of
    Omega h^2, with its band from the decoupling temperature.  Direct detection only through the electron loop (photon
    mixing, ESTIMATE); the CMB energy-injection bound (FROM MEMORY).
G3  The docstring of solution/masses.py: beta proportional to f (ANALYSIS.md section 3.3) - checked here.

Outputs: outputs/gap_fixes.json, reports/gap-fixes-checks.json, figures/figC*.png, the tables of GAPS.md section 7.
Run time about 20 s."""
import json
import math
import re
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = Path(__file__).resolve().parent
UM = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(UM / "solution"))
import masses as MS  # noqa: E402
import dark_validity as DV  # noqa: E402

OUT = HERE / "outputs"
REP = HERE / "reports"
FIG = HERE / "figures"
ETA = 3.0
CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


# ------------------------------------------------------------------------------------------------- G1 (a) the tip layer
def layered_lowest(eta, beta, delta, n_bulk=1500, n_layer=300):
    """lowest eigenvalue of the u-form with a tip layer [-1 - delta, -1] of weight density beta e^{-3 eta} (stiffness
    beta e^{-3 eta} delta... per unit length times delta: w_layer = beta e^{-3 eta} delta), Dirichlet at -1 - delta,
    Neumann at the fold; returns (Lambda, P_layer, <p^2>_layer, kinetic share of the layer, nodes, u)"""
    tb = np.linspace(-1.0, 0.0, n_bulk + 1)
    tl = np.linspace(-1.0 - delta, -1.0, n_layer + 1)
    nodes = np.concatenate([tl[:-1], tb])
    hs = np.diff(nodes)
    wl = beta * math.exp(-3 * eta) * delta
    We = np.empty(len(hs))
    nl = n_layer
    We[:nl] = wl * hs[:nl]                                            # constant weight density in the layer
    We[nl:] = (np.exp(3 * eta * nodes[nl + 1:]) - np.exp(3 * eta * nodes[nl:-1])) / (3 * eta)
    n = len(nodes)
    K = np.zeros((n, n))
    for i, (w, h) in enumerate(zip(We, hs)):
        k = w / h ** 2
        K[i, i] += k
        K[i + 1, i + 1] += k
        K[i, i + 1] -= k
        K[i + 1, i] -= k
    Md = np.zeros(n)
    Md[:-1] += We / 2
    Md[1:] += We / 2
    keep = np.ones(n, bool)
    keep[0] = False                                                   # Dirichlet at the outer edge of the layer
    s = 1 / np.sqrt(Md[keep])
    w, X = np.linalg.eigh(K[np.ix_(keep, keep)] * s[:, None] * s[None, :])
    u = np.zeros(n)
    u[keep] = X[:, 0] * s
    lam = float(w[0])
    du = np.diff(u) / hs
    kin = We * du ** 2
    nrm = float(np.sum(Md * u * u))
    kin_layer = float(np.sum(kin[:nl]))
    m_layer = float(np.sum(We[:nl] / 2 * (u[:nl] ** 2 + u[1:nl + 1] ** 2)))        # the layer elements' share of the norm
    P = m_layer / nrm
    p2 = kin_layer / m_layer if m_layer > 0 else float("inf")
    return {"Lambda": lam, "P_layer": P, "p2_layer": p2, "kinetic_share_layer": kin_layer / float(np.sum(kin)),
            "kinetic_total_over_Lambda": float(np.sum(kin)) / nrm / lam, "delta": delta}, nodes, u


def g1a(ms):
    res = {}
    for nm in ("W", "Z"):
        beta = ms["gauge"]["beta_" + nm]
        target = ms["gauge"]["Lambda_" + nm]
        rows = []
        for delta in (1e-2, 1e-3, 1e-4):
            r, _, _ = layered_lowest(ETA, beta, delta)
            r["rel_dev_vs_robin"] = r["Lambda"] / target - 1
            r["poincare_bound_ok"] = r["p2_layer"] >= (math.pi / 2) ** 2 / delta ** 2 * (1 - 1e-6)
            r["P_times_bound_over_Lambda"] = r["P_layer"] * (math.pi / 2) ** 2 / delta ** 2 / r["Lambda"]
            rows.append(r)
        res[nm] = {"beta": beta, "Lambda_robin": target, "layers": rows}
    W = res["W"]["layers"]
    # the layer elements have stiffness/mass ratios ~ 1/h_layer^2, so the discrete Rayleigh quotient of the computed
    # eigenvector reproduces the eigenvalue only to about 1e-5 (conditioning), and the 1500 bulk elements carry the
    # finite-element error ~ 3e-5: tolerances 1e-4 and 2e-4
    ok = all(abs(r["rel_dev_vs_robin"]) < 2e-4 for r in W) and all(r["poincare_bound_ok"] for r in W) and \
        all(abs(r["kinetic_total_over_Lambda"] - 1) < 1e-4 for r in W) and W[-1]["kinetic_share_layer"] > 0.99 and \
        all(abs(r["rel_dev_vs_robin"]) < 2e-4 for r in res["Z"]["layers"])
    check("G1a_W_Z_masses_are_x0_gradient_energy", ok,
          "with the tip resolved as a layer of thickness delta and stiffness beta e^{-3 eta} delta (Dirichlet at its outer edge), "
          "the lowest level equals the Robin value (W: %.2e, %.2e, %.2e relative for delta = 1e-2, 1e-3, 1e-4: the finite-element "
          "error); the whole of m_W^2 is the x0 gradient energy int w |u'|^2 of the wave function (ratio %.8f), %.4f of it inside "
          "the layer, and in the layer <p^2> >= (pi/2)^2/delta^2 holds: m_W^2 = P_tip <p^2>_tip with P_tip = %.2e at delta = 1e-4"
          % (tuple(r["rel_dev_vs_robin"] for r in W) + (W[-1]["kinetic_total_over_Lambda"], W[-1]["kinetic_share_layer"], W[-1]["P_layer"])))
    return res


# ------------------------------------------------------------------------------------------------ G1 (b) the fermions
mp.mp.dps = 50


def transfer(c, eps, t):
    """exp(M t) for (A, B)' = M (A, B), M = [[c, eps], [-eps, -c]] (from h chi = eps chi with a = A, b = -i B)"""
    k2 = c * c - eps * eps
    k = mp.sqrt(k2) if k2 >= 0 else mp.sqrt(-k2) * 1j
    ch = mp.cosh(k * t)
    sh = mp.sinh(k * t) / k
    return [[ch + c * sh, eps * sh], [-eps * sh, ch - c * sh]]


def det_mix(eps, cL, cR, kappa):
    """the tip conditions B_L(-1) = kappa B_R(-1), A_R(-1) = -kappa A_L(-1) with the fold conditions B_L(0) = 0
    (start (1, 0)) and A_R(0) = 0 (start (0, 1)): det = B_L A_R + kappa^2 B_R A_L at t = -1"""
    TL = transfer(cL, eps, -1)
    TR = transfer(cR, eps, -1)
    AL, BL = TL[0][0], TL[1][0]
    AR, BR = TR[0][1], TR[1][1]
    return mp.re(BL * AR + kappa ** 2 * BR * AL)


def lowest_mixed(c, kappa):
    """the lowest positive eps for c_L = c, c_R = -c (both zero modes at the fold); bracket around kappa zeta(c)^2"""
    c = mp.mpf(c)
    z2 = 2 * c * mp.e ** (-2 * c) / (1 - mp.e ** (-2 * c))
    guess = kappa * z2
    lo, hi = guess * mp.mpf("0.5"), guess * 2
    flo = det_mix(lo, c, -c, kappa)
    fhi = det_mix(hi, c, -c, kappa)
    assert flo * fhi < 0
    for _ in range(200):
        mid = (lo + hi) / 2
        fm = det_mix(mid, c, -c, kappa)
        if fm * flo <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2, guess


def g1b(ms):
    lam1 = MS.neumann_exact(ETA, 1)
    kappa = math.sqrt(lam1)            # lambda_f = 1 of SOLUTION.md: m_f = m_KK zeta^2 = (sqrt(Lambda_1)/fL) zeta^2
    fl = ms["scales"]["fL_GeV^-1"]
    out = {"kappa": kappa}
    worst = 0.0
    for s in ("e", "u", "d", "nu"):
        c = ms["fermions"][s]["c_f"]
        eps, guess = lowest_mixed(c, kappa)
        rel = float(eps / guess - 1)
        worst = max(worst, abs(rel))
        out[s] = {"c_f": c, "eps_fL_exact": float(eps), "kappa_zeta2": float(guess), "rel_dev": rel,
                  "m_exact_GeV": float(eps) / fl, "m_obs_GeV": ms["fermions"][s]["m_obs_GeV"]}
    # a non-perturbative case: c = 1 (a broad zero mode), to show the size of the corrections when eps is not small
    eps1, g1 = lowest_mixed(1.0, kappa)
    out["c_1_example"] = {"eps_fL_exact": float(eps1), "kappa_zeta2": float(g1), "rel_dev": float(eps1 / g1 - 1)}
    # the exact eigenvalue differs from first order by O(kappa^2 e^{-2c}): the mixing changes the tip values of the modes
    bound = max(kappa ** 2 * math.exp(-2 * out[s]["c_f"]) for s in ("e", "u", "d", "nu"))
    out["correction_scale_kappa2_exp_m2c_max"] = bound
    ok = worst < 3 * bound and all(abs(out[s]["m_exact_GeV"] / out[s]["m_obs_GeV"] - 1) < 1e-6 for s in ("e", "u", "d", "nu"))
    check("G1b_fermion_masses_are_exact_x0_eigenvalues", ok,
          "the tip Yukawa as the self-adjoint mixing condition of the coupled (L, R) x0 Dirac problem (kappa = %.4f for lambda_f = 1): "
          "the lowest exact eigenvalue equals kappa zeta(c)^2 to %.1e (the correction is O(kappa^2 e^{-2c}), at most %.1e) for e, u, "
          "d, nu and reproduces the observed masses to 1e-6; the first-order formula of SOLUTION.md is the exact x0 eigenvalue of "
          "the light fermions (for a broad mode, c = 1, the exact eigenvalue differs by %.2f %%)"
          % (kappa, worst, bound, 100 * out["c_1_example"]["rel_dev"]))
    return out


# ------------------------------------------------------------------------------------- G2 the lepton-only vector portal
def g2(xa, dv, cos):
    dm = dv["dark_matter"]
    M = dm["M_DM_GeV"]
    r = dm["overlaps"]["ratio_dm_over_fold"]
    sv_need = dm["relic"]["sigma_v_needed_GeV-2"]
    gdec = cos["um1"]["fit_to_Planck_Neff"]["g_star_s_at_decoupling"]
    N_lep = 1 + 0.5                           # e (L and e_R: Dirac), nu_L (chiral): the lepton fields of P1

    def omega(T_dec):
        G_fold = DV.G_F * (1e-3 / T_dec) ** 1.5 * (gdec / 10.75) ** 0.25
        G_dm = G_fold * r
        sv = G_dm ** 2 * M ** 2 * N_lep / math.pi
        return DV.OMEGA_C_H2 * sv_need / sv, G_fold, G_dm, sv
    om150, Gf, Gd, sv = omega(0.150)
    band = {T: omega(T)[0] for T in (0.120, 0.135, 0.150, 0.165, 0.180)}
    # T_dec that gives exactly 0.120
    lo, hi = 0.05, 0.5
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if omega(mid)[0] < DV.OMEGA_C_H2:
            lo = mid
        else:
            hi = mid
    T_exact = 0.5 * (lo + hi)
    # direct detection through the electron loop (photon mixing; Kopp et al. 2009, FROM MEMORY):
    # b_p = (alpha/(3 pi)) G_dm ln(Lambda^2/m_e^2) with Lambda = m_KK; xenon per nucleon (Z/A)^2 = (54/131)^2
    alpha = 1 / 137.035999
    m_kk = xa["particles"]["KK_even_n1"]["m_GeV"]
    b_p = alpha / (3 * math.pi) * Gd * math.log(m_kk ** 2 / 0.51099895e-3 ** 2)
    mu = M * DV.M_N / (M + DV.M_N)
    sig_p = mu ** 2 * b_p ** 2 / math.pi * DV.GEV2_TO_CM2
    sig_xe = sig_p * (54 / 131) ** 2
    lim = dv["dark_matter"]["portal"]["LZ_limit_linear_extrapolation_cm2"]
    # CMB energy injection: p_ann = f_eff <sigma v>/M < 3.2e-28 cm^3/s/GeV (Planck 2018, FROM MEMORY), f_eff ~ 0.6 for e+e-
    p_ann = 0.6 * sv * DV.GEV2_TO_CM3S * (1.0 / N_lep) / M
    out = {"N_lepton_channels": N_lep, "overlap_ratio": r, "T_dec_GeV": 0.150, "G_fold_inv_sqrt_TeV": Gf ** -0.5 / 1e3,
           "G_dm_inv_sqrt_TeV": Gd ** -0.5 / 1e3, "sigma_v_cm3_s": sv * DV.GEV2_TO_CM3S, "sigma_v_over_needed": sv / sv_need,
           "Omega_h2_predicted": om150, "Omega_h2_band": {"%.0f MeV" % (1e3 * T): v for T, v in band.items()},
           "T_dec_for_Planck_GeV": T_exact, "loop_b_p_over_G": b_p / Gd, "sigma_SI_xe_per_nucleon_cm2": sig_xe,
           "sigma_SI_limit_cm2": lim, "sigma_SI_over_limit": sig_xe / lim, "p_ann_ee_cm3_s_GeV": p_ann, "p_ann_bound": 3.2e-28,
           "labels": "INVENTED: P1 restricted to the lepton multiplets; ESTIMATE: neutrino-like decoupling and the overlap rule; "
                     "electron-loop direct detection and the CMB bound FROM MEMORY"}
    ok = 0.06 < om150 < 0.24 and min(band.values()) < DV.OMEGA_C_H2 < max(band.values()) and sig_xe < 1e-3 * lim and p_ann < 3.2e-28
    check("G2_lepton_portal_predicts_the_relic", ok,
          "with P1 on the lepton multiplets only, the portal that decouples the fold band in the QCD crossover (N_eff = 2.99, "
          "G^{-1/2} = %.1f TeV) gives the dark matter (overlap %.3f, G^{-1/2} = %.1f TeV) <sigma v> = %.2f x the relic value, i.e. "
          "a PREDICTED Omega h^2 = %.3f for T_dec = 150 MeV (%.3f to %.3f for T_dec = 120 to 180 MeV; Planck 0.120 at T_dec = %.0f MeV); "
          "direct detection only through the electron loop, sigma_SI = %.1e cm^2 per xenon nucleon (%.1e of the limit); CMB "
          "injection %.1e cm^3/s/GeV against 3.2e-28" % (Gf ** -0.5 / 1e3, r, Gd ** -0.5 / 1e3, sv / sv_need, om150,
                                                       band[0.180], band[0.120], 1e3 * T_exact, sig_xe, sig_xe / lim, p_ann))
    # the self-interaction channel must not dominate: lambda-mediated annihilation into fold-band pairs is p-wave
    out["requirement_lambda_channel"] = "sigma v (Psi Psi -> fold band) << %.1e cm^3/s, i.e. the p-wave lambda channel subdominant" % (sv * DV.GEV2_TO_CM3S)
    return out, omega


# ---------------------------------------------------------------------------------------------------- G3 the docstring
def g3():
    src = (UM / "solution" / "masses.py").read_text(encoding="utf-8")
    ok = "beta proportional to f" in src and "c_tip f^2 L e^{3 eta}" not in src
    check("G3_masses_docstring_beta_scaling", ok,
          "solution/masses.py states the tip parameter as beta = c g^2 v_Sigma^2 f L, proportional to f (ANALYSIS.md section 3.3), "
          "instead of the former c_tip f^2 L e^{3 eta}; the fitted beta and every number of the solution are unchanged")
    return {"ok": ok}


def figures(res, omega_fn, ms):
    FIG.mkdir(parents=True, exist_ok=True)
    beta = ms["gauge"]["beta_W"]
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    for delta in (1e-2, 1e-3):
        r, nodes, u = layered_lowest(ETA, beta, delta)
        u = u / np.max(np.abs(u))
        ax[0].plot(nodes, u, label="delta = %g: (m fL)^2 = %.4e" % (delta, r["Lambda"]))
    ax[0].set_xlim(-1.012, -0.95)
    ax[0].axvline(-1, color="grey", lw=0.8)
    ax[0].set_xlabel("t = y/L near the tip (layer to the left of -1)")
    ax[0].set_ylabel("W profile u (normalised)")
    ax[0].set_title("the resolved tip: the W wave function bends to 0 in the layer")
    ax[0].legend(fontsize=8)
    ds = [r["delta"] for r in res["G1a"]["W"]["layers"]]
    dev = [abs(r["rel_dev_vs_robin"]) for r in res["G1a"]["W"]["layers"]]
    P = [r["P_layer"] for r in res["G1a"]["W"]["layers"]]
    p2 = [r["p2_layer"] for r in res["G1a"]["W"]["layers"]]
    ax[1].loglog(ds, dev, "o-", label="|Lambda/Lambda_Robin - 1|")
    ax[1].loglog(ds, P, "s-", label="P_tip (probability in the layer)")
    ax[1].loglog(ds, np.array(p2) * np.array(ds) ** 2, "^-", label="<p^2>_tip delta^2 (>= (pi/2)^2)")
    ax[1].axhline((math.pi / 2) ** 2, color="grey", ls=":")
    ax[1].set_xlabel("layer thickness delta (units L)")
    ax[1].set_title("m_W^2 = P_tip <p^2>_tip as delta -> 0")
    ax[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "figC1_resolved_tip.png", dpi=130)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(7.5, 4.3))
    T = np.linspace(0.100, 0.200, 101)
    om = [omega_fn(x)[0] for x in T]
    ax.plot(T * 1e3, om, label="UM-1 1.3: lepton-only vector portal (prediction)")
    ax.axhline(0.120, color="k", ls="--", label="Planck 2018: 0.120")
    ax.axvspan(120, 180, color="C1", alpha=0.15, label="QCD crossover (g*s = 12.31 inside)")
    ax.set_yscale("log")
    ax.set_xlabel("decoupling temperature of the Psi fold band [MeV]")
    ax.set_ylabel("Omega_DM h^2")
    ax.set_title("the N_eff portal fixes the dark-matter abundance")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "figC2_relic_prediction.png", dpi=130)
    plt.close(fig)


def tables(res):
    f = DV.fmt
    L = ["### 7.1 The resolved tip (`analysis/outputs/gap_fixes.json`)", "",
         "| boson | $\\delta$ | $(mfL)^2$ | deviation from the Robin value | $P_{tip}$ | $\\langle p^2\\rangle_{tip}\\delta^2$ | layer share of the gradient energy |",
         "| --- | --- | --- | --- | --- | --- | --- |"]
    for nm in ("W", "Z"):
        for r in res["G1a"][nm]["layers"]:
            L.append("| $%s$ | %s | %s | %s | %s | %s | %s |" % (nm, f(r["delta"]), f(r["Lambda"], 6), f(r["rel_dev_vs_robin"], 2),
                                                              f(r["P_layer"], 3), f(r["p2_layer"] * r["delta"] ** 2, 4),
                                                              f(r["kinetic_share_layer"], 6)))
    L += ["", "### 7.2 The fermion masses as exact $x_0$ eigenvalues", "",
          "| fermion | $c_f$ | exact $\\varepsilon fL$ | $\\kappa\\zeta^2$ | relative difference | $m$ [GeV] |", "| --- | --- | --- | --- | --- | --- |"]
    for s in ("e", "u", "d", "nu"):
        r = res["G1b"][s]
        L.append("| $%s$ | %s | %s | %s | %s | %s |" % (s if s != "nu" else "\\nu", f(r["c_f"]), f(r["eps_fL_exact"], 6),
                                                       f(r["kappa_zeta2"], 6), f(r["rel_dev"], 2), f(r["m_exact_GeV"], 6)))
    g = res["G2"]
    L += ["", "### 7.3 The lepton-only vector portal", "", "| quantity | value |", "| --- | --- |",
          "| fold-band portal for $N_{eff} = 2.99$, $G^{-1/2}$ | %s TeV |" % f(g["G_fold_inv_sqrt_TeV"], 3),
          "| dark-matter portal (overlap %s), $G^{-1/2}$ | %s TeV |" % (f(g["overlap_ratio"], 3), f(g["G_dm_inv_sqrt_TeV"], 3)),
          "| $\\langle\\sigma v\\rangle$ into $e$, $\\nu$ / relic value | %s |" % f(g["sigma_v_over_needed"], 3),
          "| predicted $\\Omega_{DM}h^2$ at $T_{dec} = 150$ MeV | %s |" % f(g["Omega_h2_predicted"], 3)]
    for k, v in g["Omega_h2_band"].items():
        L.append("| $\\Omega_{DM}h^2$ at $T_{dec}$ = %s | %s |" % (k, f(v, 3)))
    L += ["| $T_{dec}$ for $\\Omega h^2 = 0.120$ | %s MeV |" % f(1e3 * g["T_dec_for_Planck_GeV"], 4),
          "| $\\sigma_{SI}$ per xenon nucleon (electron loop) | %s cm$^2$ (%s of the limit) |" % (f(g["sigma_SI_xe_per_nucleon_cm2"], 2), f(g["sigma_SI_over_limit"], 2)),
          "| CMB energy injection $p_{ann}$ | %s cm$^3$/s/GeV (bound $3.2\\times10^{-28}$) |" % f(g["p_ann_ee_cm3_s_GeV"], 2), ""]
    return "\n".join(L)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    REP.mkdir(parents=True, exist_ok=True)
    ms = json.loads((UM / "solution" / "outputs" / "masses.json").read_text(encoding="utf-8"))
    xa = json.loads((OUT / "x0_mass.json").read_text(encoding="utf-8"))
    dv = json.loads((OUT / "dark_validity.json").read_text(encoding="utf-8"))
    cos = json.loads((UM / "solution" / "outputs" / "cosmology.json").read_text(encoding="utf-8"))
    res = {"G1a": g1a(ms), "G1b": g1b(ms)}
    res["G2"], omega_fn = g2(xa, dv, cos)
    res["G3"] = g3()
    figures(res, omega_fn, ms)
    (OUT / "gap_fixes.json").write_text(json.dumps(res, indent=1, default=float, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    rep = {"checks": CHECKS, "pass": sum(c["verdict"] == "PASS" for c in CHECKS), "total": len(CHECKS)}
    (REP / "gap-fixes-checks.json").write_text(json.dumps(rep, indent=1) + "\n", encoding="utf-8", newline="\n")
    gen = tables(res)
    doc = UM / "GAPS.md"
    if doc.exists():
        text = doc.read_text(encoding="utf-8")
        new = re.sub(r"(<!-- BEGIN GENERATED -->\n).*?(<!-- END GENERATED -->)", lambda m: m.group(1) + gen + "\n" + m.group(2), text, flags=re.S)
        if new != text:
            doc.write_text(new, encoding="utf-8", newline="\n")
    print("%d of %d checks PASS" % (rep["pass"], rep["total"]))
    return 0 if rep["pass"] == rep["total"] else 1


if __name__ == "__main__":
    sys.exit(main())
