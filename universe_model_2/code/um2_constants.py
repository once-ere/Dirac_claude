"""UM-2 standard inputs (STANDARD) with their sources.  Every number here is used only as a target of a fit or as a
comparison, never as a derived result.  'verified' = read from the source on 2026-10-17; 'memory' = quoted from memory
(labelled FROM MEMORY in the documents)."""

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
    'm_e_MeV': (0.51099895, 0.00000000015, 'PDG (CODATA)', 'memory'),
    'm_u_MeV_2GeV': (2.16, 0.07, 'PDG, MS-bar at 2 GeV', 'memory'),
    'm_d_MeV_2GeV': (4.70, 0.07, 'PDG, MS-bar at 2 GeV', 'memory'),
    'm_nu_eV': (0.05, None, 'chosen at sqrt(|Delta m^2_31|) = 0.050 eV for the single neutrino of one generation (ASSUMED)', 'memory'),
    'v_GeV': (246.22, None, 'electroweak scale (G_F)', 'memory'),
    'alpha_inv_0': (137.035999, None, 'fine-structure constant at q = 0', 'memory'),
    'N_nu_LEP': (2.9840, 0.0082, 'LEP/SLD Z-pole combination, invisible width (Phys. Rept. 427 (2006) 257)', 'memory'),
    'm_p_MeV': (938.272, None, 'PDG', 'memory'),
    'm_n_MeV': (939.565, None, 'PDG', 'memory'),
    'hbar_c_GeV_m': (1.973269804e-16, None, 'hbar c in GeV m (CODATA)', 'memory'),
}


def val(key):
    return INPUTS[key][0]
