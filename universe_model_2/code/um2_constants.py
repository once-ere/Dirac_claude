"""UM-2 standard inputs (STANDARD) with their sources.  Every number here is used only as a target of a fit or as a
comparison, never as a derived result.  'verified' = read from the source (2026-10-17 or, for the lepton and neutrino
inputs of the three-flavour version, 2026-10-18); 'memory' = quoted from memory (labelled FROM MEMORY in the documents)."""

# --- the author's parameters (from the author's notebooks; the record's sign convention for Lambda) ---
AUTHOR_W = (1.0, 1.0 / 32.0, 1.0 / 1152.0)     # Lovelock weights w_k, alpha_k = w_k H^{2-2k}
AUTHOR_LAMBDA_OVER_H2 = -10.0                  # Lambda = -10 H^2 (the author's Lambda = 10 in the notebook's convention)
ETA = 3.0                                      # H L, the regular-tip cutoff of the record (L = 3 in units H = 1); ASSUMED
M_PSI_OVER_H = 1.0                             # dirac16complex bulk mass m = 3 H M with the author's M = 1/3 (record units m = H)

# --- particle physics ---
INPUTS = {
    'm_W_GeV': (80.3625, 0.0077, 'PDG 2026 Review of Particle Physics, W mass OUR EVALUATION (pdglive S043M)', 'verified'),
    'm_Z_GeV': (91.1879, 0.0020, 'PDG 2026, Z mass OUR AVERAGE (pdglive S044M)', 'verified'),
    'sin2_theta_W_MSbar': (0.23122, 0.00004, 'PDG electroweak review (MS-bar at M_Z)', 'memory'),
    'rho0_minus_1': (0.00038, 0.00020, 'PDG electroweak review, global fit rho_0 = 1.00038 +- 0.00020', 'memory'),
    'm_e_MeV': (0.51099895000, 0.00000000015, 'PDG 2025 summary table (leptons)', 'verified'),
    'm_mu_MeV': (105.6583755, 0.0000023, 'PDG 2025 summary table (leptons)', 'verified'),
    'm_tau_MeV': (1776.93, 0.09, 'PDG 2025 summary table (leptons)', 'verified'),
    'm_u_MeV_2GeV': (2.16, 0.07, 'PDG 2025 summary table (quarks), MS-bar at 2 GeV', 'verified'),
    'm_d_MeV_2GeV': (4.70, 0.07, 'PDG 2025 summary table (quarks), MS-bar at 2 GeV', 'verified'),
    'm_s_MeV_2GeV': (93.5, 0.8, 'PDG 2025 summary table (quarks), MS-bar at 2 GeV', 'verified'),
    'm_c_GeV_mc': (1.2730, 0.0046, 'PDG 2025 summary table (quarks), MS-bar m_c(m_c)', 'verified'),
    'm_b_GeV_mb': (4.183, 0.007, 'PDG 2025 summary table (quarks), MS-bar m_b(m_b)', 'verified'),
    'm_t_GeV': (172.56, 0.31, 'PDG 2025 summary table (quarks), direct measurements', 'verified'),
    'alpha_s_mZ': (0.1180, 0.0009, 'PDG world average of the strong coupling at m_Z', 'memory'),
    'v_GeV': (246.22, None, 'electroweak scale (G_F)', 'memory'),
    'G_F_GeV-2': (1.1663788e-5, None, 'Fermi constant from the muon lifetime (PDG)', 'memory'),
    'alpha_inv_0': (137.035999, None, 'fine-structure constant at q = 0', 'memory'),
    # number of light neutrino types from the invisible Z width
    'N_nu': (2.9963, 0.0074, 'PDG 2025 listing "number of neutrino types": Janot and Jadach, Phys. Lett. B803 (2020) 135319 (LEP-SLC 2006 '
             'corrected with the updated Bhabha cross section and the correlated luminosity bias)', 'verified'),
    'N_nu_LEP2006': (2.9840, 0.0082, 'LEP/SLD Z-pole combination, Phys. Rept. 427 (2006) 257 (superseded; used by the one-generation '
                     'version of UM-2)', 'verified'),
    # Z widths (PDG 2025 Z listing, pdglive S044, read 2026-10-18)
    'Gamma_Z_MeV': (2495.5, 2.3, 'PDG 2025, Z full width 2.4955 +- 0.0023 GeV (pdglive S044W)', 'verified'),
    'B_Z_invisible': (0.20000, 0.00055, 'PDG 2025, Z branching fraction to invisible, (20.000 +- 0.055) %', 'verified'),
    'B_Z_hadrons': (0.69911, 0.00056, 'PDG 2025, Z branching fraction to hadrons, (69.911 +- 0.056) %', 'verified'),
    'B_Z_ll': (0.033658, 0.000023, 'PDG 2025, Z branching fraction to l+l- (lepton-universality average), (3.3658 +- 0.0023) %', 'verified'),
    # the CMB value of N_eff
    'N_eff_Planck2018': (2.99, 0.17, 'Planck 2018 VI, A&A 641 (2020) A6, abstract: N_eff = 2.99 +- 0.17 (Planck + BAO)', 'verified'),
    'N_eff_ACT_DR6': (2.86, 0.13, 'ACT DR6 extended models, Calabrese et al., arXiv:2503.14454, abstract: N_eff = 2.86 +- 0.13 (2.89 +- 0.11 '
                      'with BBN)', 'verified'),
    'm_p_MeV': (938.272, None, 'PDG', 'memory'),
    'm_n_MeV': (939.565, None, 'PDG', 'memory'),
    'hbar_c_GeV_m': (1.973269804e-16, None, 'hbar c in GeV m (CODATA)', 'memory'),
    'k_B_eV_per_K': (8.617333262e-5, None, 'Boltzmann constant (CODATA)', 'memory'),
    'T_CMB_K': (2.7255, None, 'CMB temperature today (Fixsen 2009)', 'memory'),
    'N_A': (6.02214076e23, None, 'Avogadro constant (SI, exact)', 'memory'),
    'M_Pl_GeV': (1.22091e19, None, 'Planck mass G_N^{-1/2}', 'memory'),
}

# --- three-flavour oscillation data: NuFIT 6.0 (Esteban, Gonzalez-Garcia, Maltoni, Martinez-Soler, Pinheiro, Schwetz,
#     JHEP 12 (2024) 216, arXiv:2410.05380), Table 1, analysis IC24 WITH Super-Kamiokande atmospheric data, NORMAL ordering
#     (the best fit; the inverted ordering has Delta chi^2 = 6.1).  Value, (+1 sigma, -1 sigma), 3 sigma range.  verified 2026-10-18
NUFIT60_NO = {
    'sin2_theta12': (0.308, (0.012, -0.011), (0.275, 0.345)),
    'sin2_theta23': (0.470, (0.017, -0.013), (0.435, 0.585)),
    'sin2_theta13': (0.02215, (0.00056, -0.00058), (0.02030, 0.02388)),
    'delta_CP_deg': (212.0, (26.0, -41.0), (124.0, 364.0)),
    'dm2_21_eV2': (7.49e-5, (0.19e-5, -0.19e-5), (6.92e-5, 8.05e-5)),
    'dm2_31_eV2': (2.513e-3, (0.021e-3, -0.019e-3), (2.451e-3, 2.578e-3)),
}
NUFIT60_SOURCE = ('NuFIT 6.0, arXiv:2410.05380 (JHEP 12 (2024) 216), Table 1, IC24 with SK atmospheric data, normal ordering '
                  '(best fit; inverted ordering Delta chi^2 = 6.1); J_CP^max = 0.0333 +- 0.0007')
# --- quark mixing: PDG 2024 review "CKM quark-mixing matrix" (global fit, CKMfitter), standard parametrisation, Eq. (12.28);
#     J = 3.12 (+0.13 -0.12) x 10^-5.  verified 2026-10-18
CKM_PDG2024 = {
    's12': (0.22501, 0.00068),
    's13': (0.003732, 0.000090),
    's23': (0.04183, 0.00079),
    'delta_rad': (1.147, 0.026),
    'J': (3.12e-5, 0.13e-5),
}
CKM_SOURCE = 'PDG 2024 review "CKM quark-mixing matrix", global fit (CKMfitter), Eq. (12.28); Jarlskog J = 3.12e-5'
# the lightest neutrino mass is not measured; UM-2 chooses it (ASSUMED)
M_NU_LIGHTEST_EV = 1.0e-3
SUM_MNU_BOUND_EV = (0.064, 'DESI DR2 Results II, arXiv:2503.14738: sum m_nu < 0.064 eV (95 %, LCDM, DESI BAO + CMB)', 'verified')
# precision Standard-Model values of N_eff (three flavours, non-instantaneous decoupling, QED corrections, oscillations)
NEFF_SM = (3.0432, 0.0002, 'Cielo, Escudero, Mangano, Pisanti, arXiv:2306.05460 ("Neff in the Standard Model at NLO is 3.043"); '
                           'oscillations contribute +0.0007 there', 'verified')
NEFF_SM_BENNETT2021 = (3.0440, 0.0002, 'Bennett et al., JCAP 04 (2021) 073 (used by the one-generation version of UM-2)', 'memory')


def val(key):
    return INPUTS[key][0]
