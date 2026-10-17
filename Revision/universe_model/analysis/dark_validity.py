#!/usr/bin/env python3
"""Revision/universe_model/analysis/dark_validity.py - is it valid to associate dark matter, and dark energy, with the
dirac16complex field Psi of UM-1?  (ANALYSIS.md part B; run after x0_mass_analysis.py, whose outputs it reads.)

Dark matter: the criteria of a cold-dark-matter candidate (cold, dark, stable, the right abundance, compatible with the
portal that fixes N_eff, with direct detection, collisionless), each evaluated with the numbers of the UM-1 solution and of
the Revision dark-sector record.  The annihilation cross-section of a vector contact interaction is DERIVED here by an
explicit Dirac trace (numpy); the freeze-out relation and the unitarity limit are STANDARD formulas; the experimental
numbers are labelled with their sources (FROM MEMORY where they are not read from a document).

Dark energy: every Psi component on the static block of UM-1 (the late era) and on the record's history; the condensate
tuned to w0 < 0; the vacuum energy; and what UM-1 uses instead (delta Lambda).

Outputs: outputs/dark_validity.json, reports/dark-validity-checks.json, figures/figB*.png and the generated tables of
ANALYSIS.md (between its GENERATED markers).  Run time about 3 s."""
import json
import math
import re
import sys
from pathlib import Path

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = Path(__file__).resolve().parent
UM = HERE.parent
sys.path.insert(0, str(HERE))
import x0_mass_analysis as XA  # noqa: E402

OUT = HERE / "outputs"
REP = HERE / "reports"
FIG = HERE / "figures"
CHECKS = []
GEV2_TO_CM2 = 0.3893793721e-27          # (hbar c)^2 in GeV^2 cm^2 (CODATA)
C_CM_S = 2.99792458e10
GEV2_TO_CM3S = GEV2_TO_CM2 * C_CM_S       # a cross-section times v (c = 1) in GeV^-2 -> cm^3/s
G_F = 1.1663788e-5                        # GeV^-2 (PDG, from memory)
M_PL = 1.220890e19                        # GeV, the Planck mass (not reduced)
M_N = 0.93891875                          # GeV, the mean nucleon mass (PDG, from memory)
OMEGA_C_H2 = 0.1200                       # Planck 2018 (PROVENANCE.md section 3)
LZ_MIN = (2.2e-48, 40.0)                  # cm^2 at GeV: LZ 4.2 tonne-years, PRL 135, 011802 (2025); arXiv:2410.17036
GRAM_PER_GEV = 1.78266192e-24


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def load(rel):
    return json.loads((UM / rel).read_text(encoding="utf-8"))


# --------------------------------------------------------------------------------------------- the Dirac trace (B2)
def vector_contact_trace(M=1.0):
    """spin-summed |amplitude|^2 / G^2 of chi chibar -> f fbar (massless f) at threshold for L = G (chibar g^mu chi)(fbar g_mu f):
    Tr[(p2/ - M) g^mu (p1/ + M) g^nu] Tr[k1/ g_mu k2/ g_nu], explicit Dirac matrices (metric +,-,-,-); expected 128 M^4"""
    I2, Z2 = np.eye(2), np.zeros((2, 2))
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]], complex)
    sz = np.array([[1, 0], [0, -1]], complex)
    g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
    gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
    gam = [g0] + gs
    eta = np.diag([1.0, -1.0, -1.0, -1.0])

    def slash(p):
        return sum(eta[m, m] * p[m] * gam[m] for m in range(4))
    p1 = np.array([M, 0, 0, 0.0])
    p2 = np.array([M, 0, 0, 0.0])
    n = np.array([0.3, -0.5, 0.812403840463596])
    n = n / np.linalg.norm(n)
    k1 = np.concatenate([[M], M * n])
    k2 = np.concatenate([[M], -M * n])
    I4 = np.eye(4)
    A = np.array([[np.trace((slash(p2) - M * I4) @ gam[m] @ (slash(p1) + M * I4) @ gam[nn]) for nn in range(4)] for m in range(4)])
    B = np.array([[np.trace(slash(k1) @ gam[m] @ slash(k2) @ gam[nn]) for nn in range(4)] for m in range(4)])
    # contract A^{mu nu} B_{mu nu}: lower both indices of B with eta
    tot = sum(A[m, nn] * B[m, nn] * eta[m, m] * eta[nn, nn] for m in range(4) for nn in range(4))
    # sigma v_rel = (1/4 spins)(1/(4 M^2)) |M|^2 (1/(8 pi)) for two massless final particles
    sv = 0.25 * tot.real / (4 * M ** 2) / (8 * math.pi)
    return tot.real, sv


# ----------------------------------------------------------------------------------------- freeze-out (STANDARD) (B3)
def relic_sigma_v(M, gstar, g=2, target=OMEGA_C_H2):
    """the s-wave <sigma v> (GeV^-2) that gives Omega h^2 = target for a Dirac fermion (particle and antiparticle, g = 2
    each; Omega_total = 2 x the per-species value): x_f = ln(0.038 g M_Pl M sv / sqrt(g* x_f)), Omega h^2 = 1.07e9 x_f /
    (sqrt(g*) M_Pl sv) per species (Kolb and Turner; STANDARD, from memory, accuracy ~10 %)"""
    sv = 2e-9
    for _ in range(200):
        xf = 20.0
        for _ in range(50):
            xf = math.log(0.038 * g * M_PL * M * sv / math.sqrt(gstar * xf))
        om = 2 * 1.07e9 * xf / (math.sqrt(gstar) * M_PL * sv)
        sv *= om / target
    return sv, xf


def unitarity_limit(M, xf):
    """the thermally averaged s-wave (J = 0 partial wave, inelastic) limit: sigma_ann v_rel <= 4 pi/(M^2 v_rel), with
    <1/v_rel> = sqrt(x/pi) for the Maxwell distribution of the relative velocity (reduced mass M/2) (STANDARD)"""
    return 4 * math.pi / M ** 2 * math.sqrt(xf / math.pi)


# ---------------------------------------------------------------------------------------------------------------- main
def overlaps(xa):
    """normalised overlaps of the Psi modes with the electron zero-mode density P(t) = 2c e^{2ct}/(1 - e^{-2c}) (the
    fold-localised Standard-Model fermions), on the half t in [-1, 0]"""
    c_e = xa["particles"]["fermion_e"]["c_f"]
    cps = xa["particles"]["Psi_dark_matter_odd"]["c"]
    t = np.linspace(-1.0, 0.0, 400001)
    P = 2 * c_e * np.exp(2 * c_e * t) / (-math.expm1(-2 * c_e))
    n_fold = 2 * cps * np.exp(2 * cps * t) / (-math.expm1(-2 * cps))
    q, efl = XA.odd_psi_level(cps)
    th = q * (t + 1)
    bb, aa = np.sin(th), (q * np.cos(th) + cps * np.sin(th)) / efl
    n_dm = (aa * aa + bb * bb) / np.trapezoid(aa * aa + bb * bb, t)
    O_fold = np.trapezoid(P * n_fold, t)
    O_dm = np.trapezoid(P * n_dm, t)
    return {"c_e": c_e, "c_Psi": cps, "overlap_fold_band": O_fold, "overlap_dark_matter": O_dm,
            "ratio_dm_over_fold": O_dm / O_fold, "n_fold_at_fold": float(n_fold[-1]), "n_dm_at_fold": float(n_dm[-1]),
            "profiles": {"t": t[::4000].tolist(), "P_e": P[::4000].tolist(), "n_fold": n_fold[::4000].tolist(), "n_dm": n_dm[::4000].tolist()}}


def dark_matter(xa, late, cos, dm0, dm1, spec):
    res = {}
    M = late["m_dm_GeV"]
    H = late["H_GeV"]
    dmrow = xa["particles"]["Psi_dark_matter_odd"]
    res["M_DM_GeV"] = M
    # C1 cold
    w0 = dm0["cases"]["lam0"]["richardson"]["w_dm"][0]
    w1 = dm1["cases"]["lam157.7"]["richardson"]["w_dm"][0]
    p0r = dm0["cases"]["lam0"]["richardson"]["p0_over_rho_dm"][0]
    s = xa["sensitivity_dln_dlnf"]["Psi_dark_matter_odd"]
    beta_h = 4.0 / 3.0
    w_hist = 0.0 + (beta_h / 2 - 1) * p0r / 3.0              # w_eff(A) = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) with P3 = Pt = 0
    w_mass = -(1.0 / 3.0) * s * (beta_h / 2 - 1)             # -(1/3) d ln eps/d a4, d ln f/d a4 = beta/2 - 1 = -1/3
    res["cold"] = {"w_dm_lambda0": w0, "w_dm_lambda1": w1, "w_eff_static_block": w0, "w_eff_A_history": w_hist,
                   "w_eff_A_history_from_x0_mass": w_mass, "p0_over_rho": p0r}
    check("B1_cold_on_the_static_block", abs(w0) < 1e-9 and 0 < w1 < 0.01,
          "the k = 0 dark-matter quanta (eight in the lowest odd level, solved self-consistently on three grids) have w = p3/rho = "
          "%.1e (lambda = 0) and %.4f (lambda_1); on the static block of UM-1 (beta = 2) the record's shift (beta/2 - 1)(P0 + 3 Pt)/(3E) "
          "vanishes, so w_eff = w: COLD" % (w0, w1))
    check("B1_not_dust_while_the_block_deflates", abs(w_hist - w_mass) < 1e-8 and w_hist < -0.05,
          "on the record's primordial history (beta = 4/3, f = e^{-a4/3}) the same quanta have w_eff(A) = (beta/2 - 1) P0/(3E) = %.5f, "
          "equal to -(1/3) d ln eps/d a4 = %.5f from the x0-generated mass: the dark matter is dust only once the block is static "
          "(the record's finding that the bulk band falls through 0)" % (w_hist, w_mass))
    # C2 stability: a parity-violating amplitude eps_P gives Gamma ~ eps_P^2 M/(8 pi); tau > 1e26 s
    hbar = 6.582119569e-25
    tau_req = 1e26
    epsP = math.sqrt(8 * math.pi * hbar / (M * tau_req))
    res["stability"] = {"assumption": "exact fold-reflection parity z -> pi - z (ASSUMED in MODEL.md section 8)",
                        "lightest_odd_eps_over_m": dmrow["eps_over_m_record"],
                        "lightest_even_bulk_eps_over_m": spec["vacuum"]["lowest_even_bulk_analytic"],
                        "tau_required_s": tau_req, "max_parity_violation_amplitude": epsP}
    check("B1_stable_only_with_exact_parity", spec["vacuum"]["lowest_even_bulk_analytic"] > dmrow["eps_over_m_record"] and epsP < 1e-20,
          "the lightest odd level (%.6f m) lies below the lightest even bulk level (%.6f m) and has no odd state to decay into; with "
          "the fold parity broken by an amplitude eps_P the width eps_P^2 M/(8 pi) exceeds the age bound (tau > 1e26 s, the order "
          "of the indirect-detection limits) unless eps_P < %.1e: the parity must be exact (ASSUMED, not derived)"
          % (dmrow["eps_over_m_record"], spec["vacuum"]["lowest_even_bulk_analytic"], epsP))
    # B2 the trace
    tr, sv1 = vector_contact_trace(1.0)
    res["vector_contact_trace"] = {"spin_summed_over_G2_M4": tr, "sigma_v_over_G2_M2": sv1, "closed_form": "1/pi"}
    check("B2_vector_contact_annihilation", abs(tr - 128.0) < 1e-10 and abs(sv1 - 1 / math.pi) < 1e-12,
          "explicit Dirac trace: sum |M|^2 = %.10f G^2 M^4 (expected 128) at threshold, so sigma v_rel = G^2 M^2/pi per massless "
          "Dirac final state (1/2 for a chiral one) for L = G (chibar gamma^mu chi)(fbar gamma_mu f) (s-wave)" % tr)
    # B3 relic abundance
    gstar = 53.25 + 7.0 / 8.0 * 8                    # UM-1 above m_W (SOLUTION.md section 6) + the Psi fold band (g_F = 8 fermionic states)
    sv_need, xf = relic_sigma_v(M, gstar)
    sv_max = unitarity_limit(M, xf)
    G_need_1 = math.sqrt(math.pi * sv_need / M ** 2)
    res["relic"] = {"g_star_at_freeze_out": gstar, "x_f": xf, "sigma_v_needed_GeV-2": sv_need, "sigma_v_needed_cm3_s": sv_need * GEV2_TO_CM3S,
                    "unitarity_limit_cm3_s": sv_max * GEV2_TO_CM3S, "fraction_of_unitarity": sv_need / sv_max,
                    "M_at_unitarity_TeV": M * math.sqrt(sv_max / sv_need) / 1e3,
                    "G_needed_one_channel_inv_sqrt_TeV": G_need_1 ** -0.5 / 1e3, "H_TeV": H / 1e3,
                    "G_needed_times_H2": G_need_1 * H ** 2}
    # the familiar 4.4e-26 cm^3/s (Dirac) assumes the Standard-Model g* = 106.75 and x_f ~ 25; Omega ~ x_f/sqrt(g*) sigma v
    sv_scaled = 4.4e-26 * math.sqrt(106.75 / gstar) * xf / 25.0
    res["relic"]["sigma_v_familiar_rescaled_cm3_s"] = sv_scaled
    check("B3_relic_needs_near_unitary_cell_scale_coupling", abs(sv_need * GEV2_TO_CM3S / sv_scaled - 1) < 0.15 and sv_need < sv_max,
          "freeze-out (Kolb-Turner, g* = %.2f, x_f = %.2f): a Dirac relic of %.1f TeV needs <sigma v> = %.2e cm^3/s (the familiar "
          "4.4e-26 rescaled to the fewer light states of UM-1: %.2e), %.0f %% of the "
          "thermal s-wave unitarity limit %.2e cm^3/s (the limit is reached at %.0f TeV); as one vector contact channel that is "
          "G^{-1/2} = %.1f TeV, i.e. G = %.2f/H^2: the natural strength of an interaction of the cell, but its derivation from "
          "lambda (Psi Psi)^2 and the portals is OPEN" % (gstar, xf, M / 1e3, sv_need * GEV2_TO_CM3S, sv_scaled, 100 * sv_need / sv_max,
                                                          sv_max * GEV2_TO_CM3S, M * math.sqrt(sv_max / sv_need) / 1e3,
                                                          G_need_1 ** -0.5 / 1e3, G_need_1 * H ** 2))
    # B4 the portal of the fold band (N_eff) and the overlap rule
    ov = overlaps(xa)
    res["overlaps"] = {k: v for k, v in ov.items() if k != "profiles"}
    gdec = cos["um1"]["fit_to_Planck_Neff"]["g_star_s_at_decoupling"]
    T_dec = 0.150                                      # GeV: the QCD crossover where g*s = 12.31 (SOLUTION.md section 6)
    T_nu = 1.0e-3                                      # GeV: neutrino decoupling (STANDARD, approximate)
    G_fold = G_F * (T_nu / T_dec) ** 1.5 * (gdec / 10.75) ** 0.25
    G_dm = G_fold * ov["ratio_dm_over_fold"]
    N_ch = 1 + 0.5 + 3 + 3                             # e (Dirac), nu_L (chiral), u, d (3 colours each): the fields of P1
    sv_portal = G_dm ** 2 * M ** 2 * N_ch / math.pi
    om_portal = OMEGA_C_H2 * sv_need / sv_portal
    sig_SI = (M * M_N / (M + M_N)) ** 2 * (3 * G_dm) ** 2 / math.pi * GEV2_TO_CM2
    sig_lim = LZ_MIN[0] * M / LZ_MIN[1]
    G_relic = math.sqrt(math.pi * sv_need / (N_ch * M ** 2))
    sig_relic = (M * M_N / (M + M_N)) ** 2 * (3 * G_relic) ** 2 / math.pi * GEV2_TO_CM2
    res["portal"] = {"T_dec_GeV": T_dec, "g_star_s_dec": gdec, "G_fold_inv_sqrt_TeV": G_fold ** -0.5 / 1e3,
                     "G_dm_overlap_rule_inv_sqrt_TeV": G_dm ** -0.5 / 1e3, "N_channels": N_ch,
                     "sigma_v_portal_cm3_s": sv_portal * GEV2_TO_CM3S, "sigma_v_portal_over_needed": sv_portal / sv_need,
                     "Omega_h2_if_portal_dominates": om_portal, "sigma_SI_cm2": sig_SI,
                     "LZ_limit_linear_extrapolation_cm2": sig_lim, "sigma_SI_over_limit": sig_SI / sig_lim,
                     "G_relic_portal_inv_sqrt_TeV": G_relic ** -0.5 / 1e3, "sigma_SI_at_relic_cm2": sig_relic,
                     "sigma_SI_at_relic_over_limit": sig_relic / sig_lim,
                     "labels": "ESTIMATE: neutrino-like decoupling G = G_F (T_nu/T_dec)^{3/2} (g*/10.75)^{1/4}; universal c_V for "
                               "e, nu, u, d; 4D coupling proportional to the overlap with the fold-localised fermions; LZ limit "
                               "extrapolated linearly from its minimum (2.2e-48 cm^2 at 40 GeV), which is WEAKER than the published "
                               "curve at high mass"}
    check("B4_portal_consistency_with_N_eff", om_portal < 0.06 and 0.3 < sig_SI / sig_lim < 3.0,
          "if the vector portal that decouples the fold band in the QCD crossover (G^{-1/2} = %.1f TeV for N_eff = 2.99) acts on the "
          "dark matter with the overlap ratio %.3f of its x0 profile (G^{-1/2} = %.1f TeV), annihilation into e, nu, u, d gives "
          "<sigma v> = %.1f x the relic value, Omega h^2 = %.3f (UNDER-abundant), and sigma_SI = %.1e cm^2, %.1f x the LZ limit "
          "%.1e cm^2 (linear extrapolation, conservative): the dark-matter reading is in TENSION with the N_eff reading of the fold "
          "band unless the portal coefficients of the two modes differ" % (G_fold ** -0.5 / 1e3, ov["ratio_dm_over_fold"],
                                                                           G_dm ** -0.5 / 1e3, sv_portal / sv_need, om_portal,
                                                                           sig_SI, sig_SI / sig_lim, sig_lim))
    check("B4_relic_through_the_portal_is_testable", sig_relic < sig_lim,
          "a thermal relic that annihilates through the vector portal alone needs G^{-1/2} = %.1f TeV and then predicts sigma_SI = "
          "%.1e cm^2 (%.2f of the extrapolated LZ limit): consistent today, within reach of the next xenon experiments"
          % (G_relic ** -0.5 / 1e3, sig_relic, sig_relic / sig_lim))
    # B5 collisionless, Pauli
    G_self = 1.0 / H ** 2
    sig_self = G_self ** 2 * M ** 2 / (4 * math.pi) * GEV2_TO_CM2
    som = sig_self / (M * GRAM_PER_GEV)
    res["self_interaction"] = {"G_self": "1/H^2 (natural size, ESTIMATE)", "sigma_cm2": sig_self, "sigma_over_M_cm2_g": som,
                               "bound_cm2_g": 1.0, "tremaine_gunn_keV": 0.1}
    check("B5_collisionless", som < 1e-10,
          "a contact self-interaction of the natural size G = 1/H^2 gives sigma/M = %.1e cm^2/g, far below the cluster bound of about "
          "1 cm^2/g (FROM MEMORY); the Pauli (Tremaine-Gunn) bound of order 0.1-1 keV is irrelevant at %.0f TeV" % (som, M / 1e3))
    # B6 the record's computed states
    res["record_states"] = {"T0_gas": "exact fold-band gas, w_eff(A) = 1/3 (Revision/dark_sector/dirac16complex/README.md)",
                            "g_F": spec["vacuum"]["g_F"], "N_eff_fit_Delta": cos["um1"]["fit_to_Planck_Neff"]["Delta_N_eff"]}
    check("B6_the_computed_ground_states_are_radiation", spec["vacuum"]["g_F"] == 8 and spec["vacuum"]["fold_band_slope_rel_dev"] == 0.0,
          "the Kohn-Sham ground states of the record and of UM-1 fill the massless fold band (eps = kappa |k| exactly, g_F = 8): "
          "they are dark RADIATION (Delta N_eff = %.3f in the N_eff fit), not dark matter; the dark matter is a different, heavy "
          "sector of the same field that the T = 0 states do not populate" % cos["um1"]["fit_to_Planck_Neff"]["Delta_N_eff"])
    # B7 back-reaction of the hidden pressure today
    om_dm = 0.26
    dk = p0r * 3 * om_dm * late["A_over_H_squared"] / 3.0 / 8.0
    res["hidden_pressure_backreaction"] = {"delta_k_over_k0_today": dk}
    check("B7_hidden_pressure_negligible_today", dk < 1e-90,
          "the hidden pressure p0/rho = %.4f of the dark matter shifts the block by delta k/k0 = (p0/rho) 3 Omega_DM (A/H)^2/(3 k0) = "
          "%.1e today" % (p0r, dk))
    return res, ov


def dark_energy(late, xa, dm0, dm1, spec):
    res = {}
    # E1 the condensate on the static block: S ~ e^{(1 - 2 beta) a4} = a^{-3}; w = x/(1 + x), x = lambda S/(2m) = x0 a^{-3}
    scan = []
    for w0 in (-1.2, -1.0, -0.9, -0.75, -0.5, -0.3, -0.1):
        x0 = w0 / (1 - w0)
        wa = 3 * x0 / (1 + x0) ** 2
        a_star = (-x0) ** (1.0 / 3.0)
        scan.append({"w0": w0, "x0": x0, "wa_tangent": wa, "z_energy_zero": 1 / a_star - 1})
    res["condensate_static_block"] = scan
    ok = all(r["z_energy_zero"] < 1.0 and r["wa_tangent"] < 0 for r in scan if r["w0"] <= -0.3)
    m1 = [r for r in scan if r["w0"] == -1.0][0]
    m075 = [r for r in scan if r["w0"] == -0.75][0]
    check("E1_condensate_cannot_be_dark_energy", ok and abs(m1["wa_tangent"] + 6) < 1e-12,
          "on the static block the condensate dilutes like dust (S ~ a^{-3}); with lambda < 0 tuned to w0 = -1 today it has wa = %.1f "
          "and its energy density m S (1 + x) vanishes at z = %.3f and is negative before; for w0 = -0.75, wa = %.2f, zero at z = %.3f; "
          "for every w0 <= -0.3 the zero lies below z = 1, where dark energy is measured positive"
          % (m1["wa_tangent"], m1["z_energy_zero"], m075["wa_tangent"], m075["z_energy_zero"]))
    # E2 positive-energy gas states
    res["gas"] = {"static_block": "w_eff = P3/E >= 0 for every real-frequency kinetic gas (P3 >= 0) once beta = 2",
                  "history": "w_eff(C) >= -4/9 for the computed positive-energy states (record: N2, mixtures); w_eff(A) of the "
                             "computed gas in [0.330585, 0.336132]",
                  "w_dm": xa["hidden_pressure_identity"]}
    w0 = dm0["cases"]["lam0"]["richardson"]["w_dm"][0]
    w1 = dm1["cases"]["lam157.7"]["richardson"]["w_dm"][0]
    e0 = dm0["cases"]["lam0"]["richardson"]["dE"][0]
    e1 = dm1["cases"]["lam157.7"]["richardson"]["dE"][0]
    check("E2_no_positive_energy_state_accelerates", w0 >= -1e-9 and w1 >= 0 and e0 > 0 and e1 > 0
          and spec["vacuum"]["fold_band_slope_rel_dev"] == 0.0,
          "the dark-matter quanta have positive energy (%.4f, %.4f in units of m) and w = %.1e, %.4f >= 0; the fold band is exactly "
          "massless (w = 1/3); the record's interacting gas has w_eff(A) in [0.3306, 0.3361] (TAKEN): on the static block, where the "
          "shift (beta/2 - 1)(P0 + 3 Pt)/(3E) vanishes, no Psi state of positive energy and pressure p3 >= 0 has w < 0, and none "
          "accelerates the expansion (w < -1/3)" % (e0, e1, w0, w1))
    # E3 vacuum energy
    mkk = 121186.28923690817
    rho_vac = mkk ** 4 / (16 * math.pi ** 2)
    H0 = late["H0_GeV"]
    Mbar = M_PL / math.sqrt(8 * math.pi)
    rho_L = 3 * H0 ** 2 * Mbar ** 2 * 0.685
    res["vacuum_energy"] = {"rho_vac_natural_GeV4": rho_vac, "rho_Lambda_GeV4": rho_L, "ratio": rho_vac / rho_L,
                            "deltaLambda_over_H2": late["deltaLambda_over_H2"]}
    check("E3_vacuum_energy_is_the_cosmological_constant_problem", rho_vac / rho_L > 1e60,
          "a natural Dirac-sea (Casimir) energy of Psi on the cell, m_KK^4/(16 pi^2) = %.1e GeV^4, exceeds the dark-energy density "
          "%.1e GeV^4 by %.0e: the record normal-orders the sea, and UM-1 puts the dark energy into delta Lambda/H^2 = %.1e, a tuned "
          "geometric cosmological constant (w = -1 exactly), not into Psi" % (rho_vac, rho_L, rho_vac / rho_L, late["deltaLambda_over_H2"]))
    return res


def figures(dm, ov, de):
    FIG.mkdir(parents=True, exist_ok=True)
    # B1: the condensate tuned to w0 = -1 and -0.75 against a cosmological constant
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    zz = np.linspace(0, 2.5, 600)
    for w0 in (-1.0, -0.75):
        x0 = w0 / (1 - w0)
        x = x0 * (1 + zz) ** 3
        w = x / (1 + x)
        rho = (1 + zz) ** 3 * (1 + x) / (1 + x0)
        ax[0].plot(zz, np.where(np.abs(w) < 10, w, np.nan), label="condensate, w0 = %.2f" % w0)
        ax[1].plot(zz, rho, label="condensate, w0 = %.2f" % w0)
    ax[0].axhline(-1, color="k", ls="--", label="cosmological constant")
    ax[1].axhline(1, color="k", ls="--", label="cosmological constant")
    ax[1].axhline(0, color="grey", lw=0.8)
    ax[0].set_ylim(-10, 1)
    ax[1].set_ylim(-5, 3)
    for a in ax:
        a.set_xlabel("redshift z")
        a.legend(fontsize=8)
    ax[0].set_ylabel("w(z)")
    ax[1].set_ylabel("rho(z)/rho(0)")
    ax[0].set_title("lambda < 0 condensate on the static block: w runs away")
    ax[1].set_title("its energy density turns negative at z < 0.4")
    fig.tight_layout()
    fig.savefig(FIG / "figB1_condensate_is_not_dark_energy.png", dpi=130)
    plt.close(fig)
    # B2: the profiles on the full cell
    p = ov["profiles"]
    t = np.array(p["t"])
    s = np.concatenate([t, -t[::-1]])

    def mir(a):
        a = np.array(a)
        return np.concatenate([a, a[::-1]]) / 2
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(s, mir(p["n_fold"]), label="Psi fold band (massless, dark radiation)")
    ax.plot(s, mir(p["n_dm"]), label="Psi lowest odd level (dark matter, %.1f TeV)" % (dm["M_DM_GeV"] / 1e3))
    ax.plot(s, mir(p["P_e"]), label="electron zero mode (c = %.1f)" % ov["c_e"])
    ax.set_yscale("log")
    ax.set_ylim(1e-3, 30)
    ax.set_xlabel("proper hidden coordinate s/(fL) on one period (fold at 0)")
    ax.set_ylabel("probability density")
    ax.set_title("x0 profiles: the portal couplings follow the overlaps at the fold")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "figB2_profiles_and_overlaps.png", dpi=130)
    plt.close(fig)
    # B3: the portal plane
    M = dm["M_DM_GeV"]
    pr = dm["portal"]
    gs = np.logspace(math.log10(5e3), math.log10(2e5), 300)
    G = gs ** -2.0
    sv = G ** 2 * M ** 2 * pr["N_channels"] / math.pi
    sig = (M * M_N / (M + M_N)) ** 2 * (3 * G) ** 2 / math.pi * GEV2_TO_CM2
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.loglog(gs / 1e3, sv / dm["relic"]["sigma_v_needed_GeV-2"], label="<sigma v> / relic value (Omega h^2 = 0.12 / this)")
    ax.loglog(gs / 1e3, sig / pr["LZ_limit_linear_extrapolation_cm2"], label="sigma_SI / LZ limit (extrapolated)")
    ax.axhline(1, color="k", lw=0.8)
    ax.axvline(pr["G_dm_overlap_rule_inv_sqrt_TeV"], color="C3", ls="--", label="overlap rule from the N_eff portal")
    ax.axvline(pr["G_relic_portal_inv_sqrt_TeV"], color="C2", ls=":", label="thermal relic through the portal")
    ax.axvline(pr["G_fold_inv_sqrt_TeV"], color="grey", ls="-.", label="fold-band portal (N_eff)")
    ax.set_xlabel("dark-matter vector portal scale G^{-1/2} [TeV]")
    ax.set_ylabel("ratio")
    ax.set_title("dark matter of %.0f TeV through the vector portal P1" % (M / 1e3))
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIG / "figB3_portal_plane.png", dpi=130)
    plt.close(fig)


def fmt(x, d=4):
    if x is None:
        return "-"
    if isinstance(x, str):
        return x
    if x == 0:
        return "0"
    a = abs(x)
    if a >= 1e4 or a < 1e-3:
        m, e = ("%.*e" % (d - 1, x)).split("e")
        return "$%s\\times10^{%d}$" % (m, int(e))
    return "%.*g" % (d, x)


def tables(xa, dm, de):
    P = xa["particles"]
    L = ["### 12.1 The mass decomposition and the Heisenberg comparison (`analysis/outputs/x0_mass.json`)", "",
         "Units $(fL)^{-2}$ for the terms; $\\Delta s$ on one full period of $x_0$ (both halves); $m_H = \\hbar c/(2\\Delta s)$.", "",
         "| particle | $(mfL)^2$ | $\\langle p^2\\rangle$ | warp or $c^2$ | fold | tip |",
         "| --- | --- | --- | --- | --- | --- |"]
    order = [("photon_gluon_graviton_zero_mode", "photon, gluon, graviton"), ("W", "$W$"), ("Z", "$Z$"),
             ("KK_even_n1", "first even KK mode"), ("KK_odd_n1", "first odd mode"), ("fermion_e", "$e$ (zero mode)"),
             ("fermion_u", "$u$ (zero mode)"), ("fermion_d", "$d$ (zero mode)"), ("fermion_nu", "$\\nu$ (zero mode)"),
             ("Psi_fold_band", "$\\Psi$ fold band"), ("Psi_dark_matter_odd", "$\\Psi$ dark matter (odd)"), ("Psi_even_bulk", "$\\Psi$ even bulk")]
    for k, lab in order:
        r = P[k]
        lam = r.get("Lambda", 0.0)
        tip = r.get("tip_warp", 0.0) + r.get("tip_sigma", 0.0) + r.get("tip", 0.0)
        L.append("| %s | %s | %s | %s | %s | %s |" % (
            lab, fmt(lam), fmt(r["K"]), fmt(r.get("warp", r.get("bulk_mass"))), fmt(r["fold"]), fmt(tip)))
    L += ["", "| particle | $\\Delta s$ [m] | $m$ [GeV] | $m_H$ [GeV] | $m/m_H$ | $\\langle p^2\\rangle\\Delta s^2$ |",
          "| --- | --- | --- | --- | --- | --- |"]
    for k, lab in order:
        r = P[k]
        L.append("| %s | %s | %s | %s | %s | %s |" % (
            lab, fmt(r["Delta_s_m"], 3), fmt(r["m_GeV"]), fmt(r["heisenberg_GeV"]), fmt(r["m_over_heisenberg"], 3),
            fmt(r["uncertainty_product_full_cell"], 3)))
    L += ["", "The fermion rows of the first table give the decomposition of the zero mode itself ($(mfL)^2 = 0$); the masses in "
          "the $m$ column of the second come from the tip Yukawa coupling, $m_f = m_{KK}\\zeta(c_f)^2$.", ""]
    S = xa["sensitivity_dln_dlnf"]
    L += ["### 12.2 Sensitivity to the block size, $d\\ln X/d\\ln f$", "", "| $X$ | $d\\ln X/d\\ln f$ |", "| --- | --- |"]
    for k, lab in (("KK_tower", "Kaluza-Klein masses, the gap $3H/(2f)$"), ("W", "$m_W$"), ("Z", "$m_Z$"), ("fermion_e", "$m_e$"),
                   ("fermion_u", "$m_u$"), ("fermion_d", "$m_d$"), ("fermion_nu", "$m_\\nu$"), ("Psi_dark_matter_odd", "$M_{DM}$"),
                   ("alpha_em", "$\\alpha$"), ("G_Newton", "$G_N$"), ("Lambda_QCD_proton", "$\\Lambda_{QCD}$, $m_p$ (one-loop ESTIMATE)"),
                   ("mp_over_me", "$m_p/m_e$")):
        L.append("| %s | %s |" % (lab, fmt(S[k])))
    B = xa["deflation_bound_today"]
    L += ["", "Bound today (atomic clocks, FROM MEMORY): $|h_4|/H_0 <$ %s; UM-1: $h_4/A =$ %s." % (fmt(B["h4_over_H0_bound"], 2), fmt(B["h4_over_A_model_today"], 3)), ""]
    R, Pq = dm["relic"], dm["portal"]
    L += ["### 12.3 Dark matter: the numbers (`analysis/outputs/dark_validity.json`)", "", "| quantity | value |", "| --- | --- |",
          "| $M_{DM}$ | %s TeV |" % fmt(dm["M_DM_GeV"] / 1e3),
          "| $w$ of the $k = 0$ quanta, $\\lambda = 0$ / $\\lambda_1$ | %s / %s |" % (fmt(dm["cold"]["w_dm_lambda0"]), fmt(dm["cold"]["w_dm_lambda1"])),
          "| $w_{eff}(A)$ on the primordial history | %s |" % fmt(dm["cold"]["w_eff_A_history"]),
          "| hidden pressure $p_0/\\rho$ | %s |" % fmt(dm["cold"]["p0_over_rho"]),
          "| largest allowed parity-violating amplitude | %s |" % fmt(dm["stability"]["max_parity_violation_amplitude"], 2),
          "| freeze-out $x_f$, $g_*$ | %s, %s |" % (fmt(R["x_f"]), fmt(R["g_star_at_freeze_out"])),
          "| needed $\\langle\\sigma v\\rangle$ | %s cm$^3$/s |" % fmt(R["sigma_v_needed_cm3_s"], 3),
          "| thermal s-wave unitarity limit | %s cm$^3$/s (fraction used %s) |" % (fmt(R["unitarity_limit_cm3_s"], 3), fmt(R["fraction_of_unitarity"], 3)),
          "| one-channel contact scale needed, $G^{-1/2}$ | %s TeV ($G =$ %s $/H^2$) |" % (fmt(R["G_needed_one_channel_inv_sqrt_TeV"], 3), fmt(R["G_needed_times_H2"], 3)),
          "| fold-band portal for $N_{eff} = 2.99$, $G^{-1/2}$ | %s TeV |" % fmt(Pq["G_fold_inv_sqrt_TeV"], 3),
          "| overlap ratio dark matter / fold band | %s |" % fmt(dm["overlaps"]["ratio_dm_over_fold"], 3),
          "| dark-matter portal by the overlap rule, $G^{-1/2}$ | %s TeV |" % fmt(Pq["G_dm_overlap_rule_inv_sqrt_TeV"], 3),
          "| $\\langle\\sigma v\\rangle$ through the portal / needed | %s ($\\Omega h^2 =$ %s) |" % (fmt(Pq["sigma_v_portal_over_needed"], 3), fmt(Pq["Omega_h2_if_portal_dominates"], 3)),
          "| $\\sigma_{SI}$ (overlap rule) | %s cm$^2$ (%s of the limit) |" % (fmt(Pq["sigma_SI_cm2"], 3), fmt(Pq["sigma_SI_over_limit"], 3)),
          "| LZ limit at $M_{DM}$, linear extrapolation | %s cm$^2$ |" % fmt(Pq["LZ_limit_linear_extrapolation_cm2"], 3),
          "| relic through the portal alone: $G^{-1/2}$, $\\sigma_{SI}$ | %s TeV, %s cm$^2$ |" % (fmt(Pq["G_relic_portal_inv_sqrt_TeV"], 3), fmt(Pq["sigma_SI_at_relic_cm2"], 3)),
          "| self-interaction $\\sigma/M$ for $G = 1/H^2$ | %s cm$^2$/g |" % fmt(dm["self_interaction"]["sigma_over_M_cm2_g"], 2), ""]
    L += ["### 12.4 Dark energy: the $\\lambda < 0$ condensate on the static block", "",
          "| $w_0$ | $w_a$ (tangent) | energy density zero at $z$ |", "| --- | --- | --- |"]
    for r in de["condensate_static_block"]:
        L.append("| %s | %s | %s |" % (fmt(r["w0"]), fmt(r["wa_tangent"]), fmt(r["z_energy_zero"])))
    V = de["vacuum_energy"]
    L += ["", "Natural vacuum energy of $\\Psi$ on the cell $m_{KK}^4/(16\\pi^2) =$ %s GeV$^4$; dark-energy density %s GeV$^4$; ratio %s."
          % (fmt(V["rho_vac_natural_GeV4"], 3), fmt(V["rho_Lambda_GeV4"], 3), fmt(V["ratio"], 2)), ""]
    return "\n".join(L)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    REP.mkdir(parents=True, exist_ok=True)
    xa = json.loads((OUT / "x0_mass.json").read_text(encoding="utf-8"))
    late = load("solution/outputs/late_time.json")
    cos = load("solution/outputs/cosmology.json")
    dm0 = load("solution/outputs/ks/dm_lam0.json")
    dm1 = load("solution/outputs/ks/dm_lam1.json")
    spec = load("solution/outputs/ks/spectrum.json")
    dm, ov = dark_matter(xa, late, cos, dm0, dm1, spec)
    de = dark_energy(late, xa, dm0, dm1, spec)
    figures(dm, ov, de)
    verdict = {"dark_matter": "CONDITIONAL: the heavy odd quanta of Psi are a valid cold-dark-matter candidate only if the fold "
                              "parity is exact and the relic annihilation is supplied (OPEN); the computed ground states are dark "
                              "radiation; the N_eff and dark-matter readings of the portal are in tension",
               "dark_energy": "NOT SUPPORTED: no Psi state of positive energy accelerates the late universe; the lambda < 0 "
                              "condensate fails; the dark energy of UM-1 is delta Lambda"}
    res = {"dark_matter": dm, "dark_energy": de, "verdict": verdict}
    (OUT / "dark_validity.json").write_text(json.dumps(res, indent=1, default=float, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    rep = {"checks": CHECKS, "pass": sum(c["verdict"] == "PASS" for c in CHECKS), "total": len(CHECKS)}
    (REP / "dark-validity-checks.json").write_text(json.dumps(rep, indent=1) + "\n", encoding="utf-8", newline="\n")
    gen = tables(xa, dm, de)
    (OUT / "generated_tables.md").write_text(gen + "\n", encoding="utf-8", newline="\n")
    doc = UM / "ANALYSIS.md"
    if doc.exists():
        text = doc.read_text(encoding="utf-8")
        new = re.sub(r"(<!-- BEGIN GENERATED -->\n).*?(<!-- END GENERATED -->)", lambda m: m.group(1) + gen + "\n" + m.group(2), text, flags=re.S)
        if new != text:
            doc.write_text(new, encoding="utf-8", newline="\n")
    print("%d of %d checks PASS" % (rep["pass"], rep["total"]))
    return 0 if rep["pass"] == rep["total"] else 1


if __name__ == "__main__":
    sys.exit(main())
