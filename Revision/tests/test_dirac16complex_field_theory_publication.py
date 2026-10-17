#!/usr/bin/env python3
"""Publication test of Revision/docs/DIRAC16COMPLEX_FIELD_THEORY (md, tex, pdf).

Run from the repository root:
    python -m unittest Revision/tests/test_dirac16complex_field_theory_publication.py -v
    (or: python -m unittest discover -s Revision/tests -p "test_dirac16complex_field_theory_publication.py" -v)

The document is built with
    python scripts/build_provenance_pdf.py Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md
        --developer-layout --specifications Revision/pdf-specifications.json [--register]
and its edition dirac16complex-field-theory is registered in Revision/pdf-specifications.json
(Revision's own registry; provenance/pdf-specifications.json is never touched).

What is tested (fast, read-only), for the corrected metric of 2026-10-16 (version 2):
  * the .tex is exactly the builder's output for the .md with the options the
    PDF command uses (--strip-heading-numbers, --developer-layout, default author and date);
  * the .md is UTF-8 with LF line endings only and has the title, the subtitle and the sections;
  * the registry entry of the edition names the PDF file, its page count and its sha256; the
    PDF starts with %PDF-, ends with %%EOF and has only US-letter media boxes;
  * key statements are present (non-triviality [1], the Krein structure, the a4 equations, what is
    not claimed), no placeholder text is left and no statement of the withdrawn metrics is left;
  * every check name the document cites (in a code span) exists, with a passing verdict, in one of
    the Revision reports the document is drawn from (REPORTS below); a list of essential checks is cited;
  * the check counts the document quotes equal the counts in the reports, and the statement about
    the comparison record of the theory branch matches the two theory reports; the CHOSEN values of
    sigma0 quoted in section 13 are those of the Kohn-Sham-source cases file;
  * the 16 component field equations, the Lovelock components E_(k) (in a4', a4'', u = b4'/b4,
    v = u', H, k = e^(2 a4)/b4), the Einstein components and the source of the background history
    with the author's weights in the document are the output of the renderers below applied to
    Revision/theory/field-theory.json and Revision/field_equations_a4/a4-equations.json, and the sums
    over k of the rendered components equal the general formulas of a4-equations.json;
  * the 16 component equations agree with the independent sympy expressions of
    Revision/theory/reports/python-field-theory.json (formulas.dirac_equation_components), at exact
    points in four quarters of z (every real z);
  * the vielbein, sqrt|g|, the Christoffel symbols, the Ricci components, the spin connection and
    the per-direction contractions gamma^mu Omega_mu written in the document equal the entries of
    Revision/theory/field-theory.json;
  * the source that the history a4 = H x4, b4 = b4(0) e^((4/3) H x4) requires with the author's
    weights is the one quoted, and the required source of an exponential history, written in k, is
    even in A.
Optional (REVISION_PDF_REBUILD=1, the switch shared by every Revision publication test): the PDF is rebuilt in verify mode by scripts/build_provenance_pdf.py
and must reproduce the registered edition (this rewrites the .tex and the .pdf with identical
bytes; it takes about a minute).

The renderers are the generators of the corresponding document blocks:
    python Revision/tests/test_dirac16complex_field_theory_publication.py --emit
prints them.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

import sympy as sp

REVISION = Path(__file__).resolve().parents[1]
ROOT = REVISION.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import build_dissertation_tex as builder  # noqa: E402
from scripts import check_dissertation_pdf  # noqa: E402

DOCS = REVISION / "docs"
STEM = "DIRAC16COMPLEX_FIELD_THEORY"
MARKDOWN = DOCS / f"{STEM}.md"
TEX = DOCS / f"{STEM}.tex"
PDF = DOCS / f"{STEM}.pdf"
REGISTRY = REVISION / "pdf-specifications.json"
EDITION = "dirac16complex-field-theory"
PDF_RELATIVE = f"Revision/docs/{STEM}.pdf"

FIELD_THEORY = REVISION / "theory" / "field-theory.json"
A4_EQUATIONS = REVISION / "field_equations_a4" / "a4-equations.json"
KS_SOURCE_CASES = REVISION / "field_equations_a4" / "ks_source" / "results" / "ks-source-a4-cases.csv"
REPORTS = {
    "algebra-wolfram": REVISION / "algebra" / "reports" / "wolfram-algebra.json",
    "algebra-python": REVISION / "algebra" / "reports" / "python-algebra.json",
    "theory-wolfram": REVISION / "theory" / "reports" / "wolfram-field-theory.json",
    "theory-python": REVISION / "theory" / "reports" / "python-field-theory.json",
    "a4-wolfram": REVISION / "field_equations_a4" / "reports" / "wolfram-a4-report.json",
    "a4-python": REVISION / "field_equations_a4" / "reports" / "python-a4-report.json",
    "pairing-wolfram": REVISION / "pairing" / "reports" / "wolfram-pairing.json",
    "pairing-python": REVISION / "pairing" / "reports" / "python-pairing.json",
    "scope-wolfram": REVISION / "theory" / "reports" / "wolfram-scope.json",
    "scope-python": REVISION / "theory" / "reports" / "python-scope.json",
    "t3-wolfram": REVISION / "pairing" / "kohn_sham" / "reports" / "wolfram-t3.json",
    "t3-python": REVISION / "pairing" / "kohn_sham" / "reports" / "python-t3.json",
    "ks-source": REVISION / "field_equations_a4" / "reports" / "ks-source-conditions.json",
    "ks-source-a4": REVISION / "field_equations_a4" / "ks_source" / "reports" / "ks-source-a4.json",
    "t3c-wolfram": REVISION / "pairing" / "kohn_sham" / "reports" / "wolfram-t3-completion.json",
    "t3c-python": REVISION / "pairing" / "kohn_sham" / "reports" / "python-t3-completion.json",
    "ks-crosscheck": REVISION / "kohn_sham" / "reports" / "ks-crosscheck.json",
    "ds-derivation": REVISION / "dark_sector" / "dirac16complex" / "reports" / "derivation-checks.json",
    "ds-ks-history": REVISION / "dark_sector" / "dirac16complex" / "reports" / "ks-history-run.json",
    "ds-eos": REVISION / "dark_sector" / "dirac16complex" / "reports" / "eos-checks.json",
    "ds-independent": REVISION / "dark_sector" / "dirac16complex" / "reports" / "independent-checks.json",
    # cited by the dirac16complex dark-sector README for the phantom window of the drifting condensate (verdict (iii))
    "ds00-derive-eos": REVISION / "dark_sector" / "dirac16complex00" / "reports" / "python-derive-eos.json",
    "lead-u1": REVISION / "lead_checks" / "reports" / "charge-conjugation-and-u1.json",
    "fock-quartic": REVISION / "theory" / "fock_quartic" / "reports" / "fock-quartic.json",
}

TITLE = "dirac16complex in the author's primordial gravitational field"
SUBTITLE = ("Lagrangian, covariant field equations, non-triviality [1], energy-momentum tensor "
            "operator, equations of state and the field equations for a4[x4] and b4[x4] (Revision record)")

SECTIONS = [
    "Abstract",
    "1. Scope, sources and status of the record",
    "2. The primordial gravitational field",
    "3. The field dirac16complex: Clifford algebra, Pin(4,4) and Spin(4,4)",
    "4. Coupling through the canonical spin connection",
    "5. The Lagrangian",
    "6. The exact covariant field equations (Euler-Lagrange)",
    "7. Non-triviality [1]",
    "8. Self-consistency",
    "9. The energy-momentum tensor",
    "10. Kinetic energy, potential energy, energy density, pressures and equations of state",
    "11. Canonical quantisation in 4 + 4 dimensions and the Krein structure",
    "12. The energy-momentum tensor operator",
    "13. The field equations for a4[x4] and b4[x4] with dirac16complex as the source",
    "14. Relation to the pairing theorems",
    "15. What this document does not claim",
    "16. Reproduction",
    "17. Index of formulas and checks",
]

# Code spans of the document that are not check names (formula keys, JSON keys, programs).
NON_CHECK_SPANS = {
    "_G", "grassmann_", "dirac16complex", "field_equation", "evolution_form",
    "field_equation_components", "christoffel_nonzero", "omega_nonzero", "ricci_mixed_nonzero",
    "field_equation_blocks", "quantisation", "nontriviality",
    "majorana_negative_control", "exact_solutions", "EMT_diagonal", "EMT_kinetic_potential",
    "EMT_homogeneous_on_shell", "EMT_offdiagonal_x4_x0", "T_variation", "T_symmetric",
    "energy_exchange", "adjoint_equation", "equation_of_state_definitions",
    "hidden_direction_hermiticity", "lovelockTensors", "generalSource", "x0_dependence",
    "secondOrderJacobianDet", "historySource_kappaT_minus_Lam",
    "sourceRequiredByGivenHistory", "einstein", "exponentialHistory", "requiredSource",
    "authorWeights", "fields", "emtConvention", "comparison_with_wolfram", "dirac_equation_components",
    "not_established", "wolframscript", "pdflatex", "wolfram_checks_without_sympy_counterpart",
}

ESSENTIAL_CHECKS = [
    "Pin44_irreducible_commutant_dim_1", "pin_commutant_dimension_1",
    "chiral_halves_inequivalent_intertwiners_0", "spin_halves_inequivalent",
    "metric_is_the_corrected_metric", "sqrt_det_g", "ricci_mixed_components", "flat_member_and_curvature",
    "curvature_and_flat_member", "vielbein_postulate", "Omega_components", "gammaOmega_total",
    "gammaOmega_per_direction", "gamma_mu_Omega_mu_equals_hidden_block_terms", "per_direction_terms",
    "gravity_term_square", "nontriviality_1_dirac16complex",
    "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish",
    "spin_curvature_equals_Riemann", "L_real_G", "EL_Psibar_G", "EL_Psi_G",
    "grassmann_euler_lagrange_psibar_variation", "Dirac_operator_explicit_G",
    "Majorana_Lg_total_derivative_grassmann", "Lichnerowicz_identity_G",
    "Noether_identity_diffeomorphisms_G", "Noether_identity_local_Lorentz_G",
    "grassmann_emt_conservation_on_shell", "T_vielbein_variation_closed_form_G",
    "grassmann_homogeneous_on_shell_rho_p", "first_order_form_and_anticommutator",
    "no_positive_inner_product", "Fock_space_good_sector_example", "expectation_value_rule",
    "extra_time_modes_grow", "good_sector_hermiticity_curved", "Krein_form_conserved_curved",
    "boosted_frame_gammaOmega_formula", "boosted_frame_removes_only_the_H_term",
    "boosted_frame_curvature_nonzero", "rescaling_removes_the_connection_term",
    "connection_free_lagrangian_same_equations", "good_sector_hermiticity_up_to_the_brane_flux",
    "good_sector_x0_independent_modes_without_boundary_condition", "extra_time_growth_rates_unbounded",
    "gammaOmega_sees_the_hidden_block",
    "Q_one_particle_Krein_inertia_real_frequencies", "Q_one_particle_complex_and_zero_frequencies_Krein_neutral",
    "T3_energies_and_emt_profiles_equal", "T3_fold_conditions_exchanged",
    "lovelock_variables", "independent_components", "constraint_propagation_bianchi",
    "second_order_system_a4pp_vv", "einstein_null_combinations", "einstein_flat_vacuum",
    "einstein_no_exponential_vacuum", "author_weights_history_source", "author_weights_no_exponential_vacuum",
    "condensate_source_equal_pressures", "Q_Krein_metric_of_images",
    "T3C_krein_rule_16_component", "T3C.krein_rule_16_component",
    "mode_hamiltonian_good_sector", "good_sector_positive_fock_realisation",
    "trace_identity_operator_identity_wick", "trace_identity_fails_for_every_other_combination",
    "homogeneous_rho_p_operator_identities_wick", "negative_control_free_dynamics",
    "einstein_second_order_system", "egb_exponential_vacuum_branches",
    # the Kohn-Sham source (section 13)
    "ks_profiles_depend_on_x0", "ks_hidden_pressure_condition", "ks_offdiagonal_condition",
    "ks_history_is_a_prescribed_background", "A1_hidden_equals_extra_times_and_no_offdiagonal",
    "B2_x0_conservation_on_every_profile", "B3_hidden_direction_mismatch", "C1_averaged_hidden_pressure_condition",
    "C3_record_history_not_sourced_by_the_gas", "D0_free_gas_average_exact",
    "D2_author_weights_from_the_record_history", "D4_outcomes",
    # the dark-sector verdict (section 15)
    "w_eff_A", "w_eff_C", "free_gas_exact_fold_band", "interacting_gas_ranges", "bulk_band_w_eff",
    "gas_cpl_far_from_unite", "phantom_condition", "condensate_phantom_interval", "condensate_drifts",
]

REQUIRED_PHRASES = [
    "16 complex anticommuting components",
    "irreducible under Pin(4,4)",
    "two inequivalent irreducible 8-dimensional representations",
    "Theorem 1 (non-triviality [1])",
    r"\gamma^\mu\Omega_\mu = c_g\gamma^{(0)} + v_g\gamma^{(4)}",
    r"c_g = \tfrac32He^{a_4}b_4^{-1/2}",
    r"\big(c_g^2 - v_g^2\big)\,I_{16} = \big(\tfrac94H^2k - (u - \tfrac12a_4')^2\big)\,I_{16}",
    r"H^2(\tfrac94e^{2Hx_4/3} - \tfrac{25}{36})I_{16} > 0",
    r"$b_4$ is never 1",
    r"a_4 = Hx_4,\quad b_4 = b_4(0)\,e^{(4/3)Hx_4}",
    "for $a_4 = 0$, $b_4 = H^2x_4^2$ all 4096 Riemann components vanish",
    "is a total derivative",
    "Theorem 2 (the canonical anticommutator forces a Krein structure)",
    "no positive inner product",
    "normal ordered",
    r"\hat T^\nu{}_\mu",
    "The field equations therefore require $p_0 = p_t$ and a source without off-diagonal components",
    "a_4 = AHx_4 + a_0",
    r"\sigma_T = +1",
    "no creation process",
    "is not claimed",
    "Numbers and formulas are taken only from",
    "belongs to the diagonal vielbein",
    "vanishes in no frame wherever the metric is curved",
    "no boost in this plane removes",
    "Krein-neutral",
    "not well posed in Hadamard's sense",
    "prescribed test-field background without back-reaction",
    "is a choice of sign",
    "That record establishes neither Hypothesis nor Hypothesis00.",
    "`Revision/docs/KOHN_SHAM_DEFLATING_FIELD`",
    "`Revision/docs/LOVELOCK_GKD`",
    "`Revision/docs/DARK_SECTOR_HYPOTHESES`",
    "`Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY`",
    "constructed and checked only for single good-sector momenta with frozen coefficients",
    "a positive-norm Hilbert space for the full field is not established",
    "the identity holds in this model if and only if the potential and the energy-momentum tensor are both Wick ordered",
    "Nothing is proved for the field on a whole slice",
    r"and in section 15 (the equation-of-state values $w_{\rm eff}$ of the Kohn-Sham gas",
    r"\kappa(p_3 - p_0) = -\tfrac{9}{16}k^2 + \tfrac{1069}{432}k + \tfrac{2015}{972}",
    "the corrected metric has no Z2 orbifold",
    # the honesty labels and verdicts of sections 13 and 15
    "no recorded Kohn-Sham state is an admissible source",
    "In a stated APPROXIMATION",
    "is CHOSEN at the six values",
    "These are statements of that approximation, not of the field equations",
    "is therefore a PRESCRIBED background for test fields, without back-reaction",
    "is a CHOSEN pure condensate",
    "a tuned value, NOT a prediction",
    r"far from the Unite pair $(w_0, w_a) = (-0.861, -0.60)$",
    "OPEN in that record",
    "The computed free Kohn-Sham gas ($\\lambda = 0$) is an exact fold-band gas",
    # the qualifications of the history values and of the constant-k histories
    r"I_{16} > 0$ for $x_4 \geq 0$",
    "so they do not deflate, and none of them is a history of this record",
]

# Numbers quoted from the second-wave reports: (report key, text in the report, text in the document).
# Filled from the regenerated Kohn-Sham source and dark-sector records (W5, W6).
QUOTED_NUMBERS: list[tuple[str, str, str]] = [
    ("ks-source", "(max rho - min rho)/max|T| >= 0.456213", r"$(\max\rho - \min\rho)/\max|T| \geq 0.456213$"),
    ("ks-source", "fails (> 1e-06) for every one of the 60 states with lambda != 0 (smallest: 0.080929",
     r"fails for every one of the 60 states with $\lambda \neq 0$ ($\max_y|p_0 - p_t|/\max|T| \geq 0.080929$"),
    ("ks-source", "a4,0 = 0 (kk = 1): kappa rho = 3.57407", r"$\kappa\rho = 3.57407$ at $a_{4,0} = 0$"),
    ("ks-source", "a4,0 = 2 (kk = 3.79367): kappa rho = -7.63383", r"$-7.63383$ at $a_{4,0} = 2$"),
    ("ks-source", "differ from the needed ones by at least 1.3733", "by at least 1.3733 at every recorded state"),
    ("ks-source-a4", "largest residual relative to the largest term 1.21233e-05",
     "largest residual 1.21233e-05 of the largest term"),
    ("ks-source-a4", "mu1_rho in [0.147738, 0.738255]", "lies between 0.147738 and 0.738255"),
    ("ks-source-a4", "relative to the largest averaged component >= 0.00613418",
     r"relative violation $\geq 0.00613418$"),
    ("ks-source-a4", "N = 592, 2352: C = 0.034125, 0.216249", "($C = 0.034125$ and 0.216249"),
    ("ks-source-a4", "rho_bar = 0.216249 at a4 = 0, 0.00104404 at a4 = 2",
     r"$\bar\rho = 0.216249$ and $0.00104404$ there"),
    ("ks-source-a4", "would have to run from 16.5276 to -7311.81", "run from 16.5276 to $-7311.81$"),
    ("ks-source-a4", "the constraint fixes kappa rho_bar(0) = 3.57407",
     r"the constraint fixes $\kappa\bar\rho(0) = 3.57407$"),
    ("ks-source-a4", "at x4 = 0.428813 (a4 = 0.361572, b4 = 0.862627, a4'/H = 0.978369, u/H = -2.60176)",
     r"$x_4 = 0.428813/H$ ($a_4 = 0.361572$, $b_4 = 0.862627$, $a_4'/H = 0.978369$, $u/H = -2.60176$"),
    ("ks-source-a4", "38 cases (2 free series", "Over 38 cases (the two free series"),
    ("ks-source-a4", "outcomes a4_turns 24, regular 6, runaway 4, singular_second_order_system 4",
     "$a_4$ turning 24 times ($a_4'$ reaches 0), regular 6 times (through $x_4 = 2/H$), runaway 4 times and singular 4 times"),
    ("ds-eos", "w_eff(A) = 1/3 exactly (radiation-like), w_eff(C) = 1/3 - 4/9 = -1/9, wa = 0",
     r"$w_{\rm eff}(A) = 1/3$ exactly (radiation-like), $w_{\rm eff}(C) = -1/9$, $w_a = 0$"),
    ("ds-eos", "w_eff(A) in [0.330585, 0.336132]", r"$w_{\rm eff}(A)$ between 0.330585 and 0.336132"),
    ("ds-eos", "w_eff(C) = w_eff(A) - 4/9 in [-0.113860, -0.108312]", "between $-0.113860$ and $-0.108312$ (interacting)"),
    ("ds-eos", "tangent wa in [-0.003892, 0.003904], least-squares fit wa in [-0.002392, 0.002261]",
     "tangent $w_a$ lies between $-0.003892$ and 0.003904 and its fitted $w_a$ between $-0.002392$ and 0.002261"),
    ("ds-eos", "w_eff(C) = (5/9) w_c - 4/9 = -0.868889, both with wa = -1.247867",
     r"$w_{\rm eff}(C) = -0.868889$ with $w_a = -1.247867$"),
    ("ds-eos", "w_eff(C) = P3_g/(E_g + E_c) - 4/9 >= -0.444111", r"$w_{\rm eff}(C) \geq -0.444111$"),
    ("ds-independent", "runs from 0.318721 (a4 = -3) to -0.081074 (a4 = 4), monotonically decreasing",
     "falls monotonically from 0.318721 ($a_4 = -3$) to $-0.081074$ ($a_4 = 4$)"),
    ("ds-independent", "it changes sign between a4 = -0.5 and -0.25",
     "changing sign between $a_4 = -0.5$ and $-0.25$"),
    ("ds-derivation", "= w_eff(A) - 4/9 at beta = 4/3", r"$w_{\rm eff}(C) = w_{\rm eff}(A) - 4/9$"),
    ("ds00-derive-eos", "lambda S/m in (-2, -1)", r"while $\lambda S/m$ lies in $(-2, -1)$"),
    # first-wave values quoted in section 13 (the tuned EGB vacuum couplings)
    ("a4-wolfram", "alpha2 = -1/(4 H^2 (A^2 - k0)) and Lambda = -E^x4_x4 at the history "
                   "((3*(AA^4*H^2 + 3*AA^2*H^2*kk + H^2*kk^2))/(AA^2 - kk))",
     r"$\alpha_2 = -1/(4H^2(A^2 - k_0))$ and $\Lambda = 3H^2(A^4 + 3A^2k_0 + k_0^2)/(A^2 - k_0)$"),
]

PLACEHOLDERS = ["TODO", "TBD", "FIXME", "lorem ipsum", "PLACEHOLDER", "XXX", "@@"]

# Statements of the withdrawn metrics (2026-10-14 and version 1 of 2026-10-16) that must not reappear as results.
STALE_PHRASES = ["planned and not yet written", "the conserved charge", "re-inflate",
                 "for every series with 3-momentum", "to be confirmed by the theory branch",
                 "the record of the case $b_4 = 1$", "Not recomputed for general", "F(a_4')",
                 r"\sqrt{|g|} = \cos z", "linear member", r"b_4^{3/2}\cos z", r"3H\gamma^{(0)} + \tfrac34u",
                 r"R^{x_0}{}_{x_0} = -6H^2", "never_flat_for_H_positive", "offDiagonalFactor_Q",
                 r"\big(-\tfrac{2}{27}, -\tfrac29, -\tfrac{22}{27}, -\tfrac{14}{27}\big)", r"e^{a_4}\sin^{1/6}z"]

# Hand-written formulas of the document that are compared with field-theory.json below.
DOCUMENT_FORMULAS = [
    r"f_0 = e^{-a_4}b_4^{1/2}\cot z,\quad f_1 = f_2 = f_3 = e^{a_4},\quad f_4 = 1,\quad f_5 = f_6 = f_7 = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}",
    r"\sqrt{|g|} = \sigma_z f_0 f_1\cdots f_7 = e^{-a_4}b_4^2\,|\cot z|\,(\sin^2 z)^{1/4}",
    r"\Gamma^{x_0}{}_{x_0 x_0} &= -12H\csc(12Hx_0), & \Gamma^{x_0}{}_{x_0 x_4} &= h_4,",
    r"\Gamma^{x_0}{}_{x_t x_t} &= H(\sin^2 z)^{1/6}\tan z, & \Gamma^{x_i}{}_{x_i x_4} &= a_4',",
    r"\Gamma^{x_4}{}_{x_0 x_0} &= e^{-2a_4}b_4\cot^2 z\,h_4, & \Gamma^{x_4}{}_{x_i x_i} &= e^{2a_4}a_4',",
    r"\Gamma^{x_4}{}_{x_t x_t} &= -e^{-2a_4}b_4(\sin^2 z)^{1/6}\,h_4, & \Gamma^{x_t}{}_{x_t x_0} &= H\cot z,",
    r"\Gamma^{x_t}{}_{x_t x_4} &= h_4 .",
    r"R^{x_0}{}_{x_0} = R^{x_t}{}_{x_t} &= -3H^2k + (a_4')^2 - a_4'' - \tfrac52a_4'u + \tfrac12\frac{b_4''}{b_4} + \tfrac12u^2, & R^{x_i}{}_{x_i} &= -(a_4')^2 + a_4'' + 2a_4'u,",
    r"R^{x_4}{}_{x_4} &= 7(a_4')^2 - a_4'' - 4a_4'u + 2\frac{b_4''}{b_4} - u^2,",
    r"R = -12H^2k + 8(a_4')^2 - 2a_4'' - 8a_4'u + 4\frac{b_4''}{b_4} + u^2 .",
    r"\omega_{x_0\,(0)(4)} &= h_4\,s_b\cot z, & \omega_{x_i\,(i)(4)} &= a_4'\,e^{a_4},",
    r"\omega_{x_t\,(4)(t)} &= h_4\,s_b\,(\sin^2 z)^{1/12}, & \omega_{x_t\,(0)(t)} &= H\,(\sin^2 z)^{1/12},",
    r"\gamma^{x_0}\Omega_{x_0} &= \tfrac12 h_4\,\gamma^{(4)}, \qquad \gamma^{x_i}\Omega_{x_i} = \tfrac12 a_4'\,\gamma^{(4)} \qquad (i = 1, 2, 3),",
    r"\gamma^{x_t}\Omega_{x_t} &= \tfrac12 h_4\,\gamma^{(4)} + \tfrac12He^{a_4}b_4^{-1/2}\,\gamma^{(0)} \qquad (t = 5, 6, 7), \qquad \gamma^{x_4}\Omega_{x_4} = 0,",
]


# ---------------------------------------------------------------------------------------------
# Renderers (they generate the document blocks; the tests compare the document with them)
# ---------------------------------------------------------------------------------------------

_a4, _z, _H = sp.symbols("a4 z H", real=True)
_A1, _A2 = sp.symbols("A1 A2", real=True)
_b4 = sp.symbols("b4", positive=True)
_B1, _B2 = sp.symbols("B1 B2", real=True)                 # b4' and b4''
EPS_S = sp.exp(-_a4)                                       # 1/f for x1, x2, x3
EPS_T = sp.exp(_a4) * _b4 ** sp.Rational(-1, 2) * (sp.sin(_z) ** 2) ** sp.Rational(-1, 12)  # 1/f for x5, x6, x7
EPS_0 = sp.exp(_a4) * _b4 ** sp.Rational(-1, 2) * sp.tan(_z)  # 1/f for x0 (signed)
C_G = sp.Rational(3, 2) * _H * sp.exp(_a4) / sp.sqrt(_b4)  # the gamma^(x0) coefficient of gamma^mu Omega_mu
V_G = _B1 / _b4 - _A1 / 2                                 # the gamma^(x4) coefficient


def _wl_metric_symbols(text: str) -> str:
    t = text.replace("Derivative[1][a4][x4]", "A1").replace("Derivative[2][a4][x4]", "A2")
    t = t.replace("Derivative[1][b4][x4]", "B1").replace("Derivative[2][b4][x4]", "B2")
    t = t.replace("Sqrt[b4[x4]]", "sqrt(b4)")
    return t.replace("a4[x4]", "a4").replace("b4[x4]", "b4").replace("12*H*x0", "(2*z)").replace("6*H*x0", "z")


def _parse_component(text: str) -> tuple[sp.Expr, int]:
    lhs, rhs = (part.strip() for part in text.split("=="))
    match = re.fullmatch(r"V\*Psi\[(\d+)\]", rhs)
    if match is None:
        raise ValueError(f"unexpected right-hand side {rhs!r}")
    t = re.sub(r'dd\["x(\d)",\s*Psi\[(\d+)\]\]', r"D_\1_\2", lhs)
    t = re.sub(r"Psi\[(\d+)\]", r"P_\1", t)
    t = _wl_metric_symbols(t)
    t = t.replace("Sin[z]", "sin(z)").replace("Tan[z]", "tan(z)").replace("Cos[z]", "cos(z)")
    t = t.replace("^", "**")
    if "[" in t or "]" in t:
        raise ValueError(f"unparsed Wolfram syntax in {t!r}")
    local = {"E": sp.E, "a4": _a4, "z": _z, "H": _H, "b4": _b4, "A1": _A1, "B1": _B1, "sqrt": sp.sqrt,
             "sin": sp.sin, "tan": sp.tan, "cos": sp.cos}
    return sp.sympify(t, locals=local), int(match.group(1))


def wolfram_component_lhs() -> list[sp.Expr]:
    formulas = {item["key"]: item["wl"] for item in json.loads(FIELD_THEORY.read_text("utf-8"))["formulas"]}
    out = []
    for number, text in enumerate(formulas["field_equation_components"], 1):
        expr, row = _parse_component(text)
        if row != number:
            raise ValueError(f"component {number} has right-hand side Psi[{row}]")
        out.append(expr)
    return out


def _sign(value: sp.Expr, base: sp.Expr) -> int:
    ratio = sp.simplify(value / base)
    if ratio not in (1, -1):
        raise ValueError(f"coefficient {value} is not +-{base}")
    return int(ratio)


def _signed(sign: int, body: str, first: bool) -> str:
    if first:
        return ("-" if sign < 0 else "") + body
    return (" - " if sign < 0 else " + ") + body


def component_equation_rows(exprs: list[sp.Expr] | None = None) -> list[str]:
    """The 16 component field equations as LaTeX aligned rows, from field-theory.json.

    Every component has the derivative terms of the eight directions, the hidden-block term c_g psi_B with the same
    psi_B as the hidden-direction derivative, and the term v_g psi_C with the same psi_C and the same sign as d4: it is
    written with hat-d4 = d4 + v_g and epsilon_0 (tan z d0 + (3/2) H)."""
    rows = []
    for number, expr in enumerate(wolfram_component_lhs() if exprs is None else exprs, 1):
        derivative = {}
        for symbol in expr.free_symbols:
            name = symbol.name
            if name.startswith("D_"):
                _, k, b = name.split("_")
                if int(k) in derivative:
                    raise ValueError(f"two x{k} derivatives in component {number}")
                derivative[int(k)] = (int(b), expr.coeff(symbol))
        field_terms = [s for s in expr.free_symbols if s.name.startswith("P_")]
        if len(field_terms) != 2 or sorted(derivative) != list(range(8)):
            raise ValueError(f"unexpected structure of component {number}")
        rest = sp.expand(expr - sum(c * sp.Symbol(f"D_{k}_{b}") for k, (b, c) in derivative.items())
                         - sum(expr.coeff(p) * p for p in field_terms))
        if rest != 0:
            raise ValueError(f"unexpected remainder {rest} in component {number}")
        bases = {0: EPS_0, 1: EPS_S, 2: EPS_S, 3: EPS_S, 4: sp.Integer(1), 5: EPS_T, 6: EPS_T, 7: EPS_T}
        signs = {k: _sign(c, bases[k]) for k, (b, c) in derivative.items()}
        hidden_b, time_b = derivative[0][0], derivative[4][0]
        coefficients = {int(p.name[2:]): expr.coeff(p) for p in field_terms}
        if sorted(coefficients) != sorted((hidden_b, time_b)) or hidden_b == time_b:
            raise ValueError(f"the non-derivative terms of component {number} are not on psi_{hidden_b}, psi_{time_b}")
        if signs[0] != 1 or _sign(coefficients[hidden_b], C_G) != 1:
            raise ValueError(f"the hidden-direction terms of component {number} are not epsilon_0 (tan z d0 + (3/2) H)")
        if _sign(coefficients[time_b], V_G) != signs[4]:
            raise ValueError(f"the v_g term of component {number} does not have the sign of d4")
        space = "".join(_signed(signs[k], rf"\partial_{k}\psi_{{{derivative[k][0]}}}", k == 1) for k in (1, 2, 3))
        time = "".join(_signed(signs[k], rf"\partial_{k}\psi_{{{derivative[k][0]}}}", k == 5) for k in (5, 6, 7))
        x4 = _signed(signs[4], rf"\hat\partial_4\psi_{{{time_b}}}", False)
        rows.append(rf"\epsilon_s({space}){x4} + \epsilon_t({time}) + \epsilon_0(\tan z\,\partial_0 + \tfrac32H)"
                    rf"\psi_{{{hidden_b}}} &= V\psi_{{{number}}}")
    return rows


def aligned(rows: list[str]) -> str:
    return "\\begin{aligned}\n" + " \\\\\n".join(rows) + "\n\\end{aligned}"


def component_equation_blocks() -> list[str]:
    rows = component_equation_rows()
    return [aligned(rows[:8]), aligned(rows[8:])]


_ad1, _ad2, _uu, _vv, _kk, _AA, _be = sp.symbols("ad1 ad2 uu vv kk AA be", real=True)
_alphas = sp.symbols("alpha1 alpha2 alpha3", real=True)
_lam, _kappa = sp.symbols("Lam kappa", real=True)
_A4_LOCALS = {"ad1": _ad1, "ad2": _ad2, "uu": _uu, "vv": _vv, "kk": _kk, "H": _H, "AA": _AA, "be": _be,
              "alpha1": _alphas[0], "alpha2": _alphas[1], "alpha3": _alphas[2], "Lam": _lam, "kappa": _kappa}
A4_GENS = (_ad1, _ad2, _uu, _vv, _H, _kk)
TERMS_PER_ROW = 4
FACTOR_TEX = {"ad1": "a_4'", "ad2": "a_4''", "uu": "u", "vv": "v", "H": "H", "kk": "k", "AA": "A", "be": r"\beta"}
AUTHOR_WEIGHTS = {_alphas[0]: 1, _alphas[1]: sp.Rational(1, 32), _alphas[2]: sp.Rational(1, 1152)}


def _wl_poly(text: str) -> sp.Expr:
    return sp.expand(sp.sympify(text.replace("^", "**"), locals=_A4_LOCALS))


def _factor_tex(symbol: sp.Symbol, power: int) -> str:
    name = FACTOR_TEX[symbol.name]
    if power == 1:
        return name
    if symbol.name in ("ad1", "ad2"):
        return f"({name})^{{{power}}}"
    return f"{name}^{{{power}}}"


def _number_tex(value: sp.Rational) -> str:
    return str(value.p) if value.q == 1 else rf"\tfrac{{{value.p}}}{{{value.q}}}"


def poly_terms(expr: sp.Expr, gens: tuple[sp.Symbol, ...]) -> list[tuple[int, str]]:
    poly = sp.Poly(sp.expand(expr), *gens)
    terms = sorted(poly.terms(), key=lambda term: tuple(-e for e in term[0]))
    out = []
    for exponents, coefficient in terms:
        if not coefficient.is_Rational:
            raise ValueError(f"non-rational coefficient {coefficient}")
        factors = " ".join(_factor_tex(g, e) for g, e in zip(gens, exponents) if e)
        magnitude = abs(coefficient)
        if factors:
            body = factors if magnitude == 1 else f"{_number_tex(magnitude)} {factors}"
        else:
            body = _number_tex(magnitude)
        out.append((-1 if coefficient < 0 else 1, body))
    return out


def poly_tex(expr: sp.Expr, gens: tuple[sp.Symbol, ...]) -> str:
    terms = poly_terms(expr, gens)
    return "".join(_signed(s, b, i == 0) for i, (s, b) in enumerate(terms)) if terms else "0"


def wrapped_rows(head: str, terms: list[tuple[int, str]], tail: str = "") -> list[str]:
    rows = []
    per_row = len(terms) if len(terms) <= TERMS_PER_ROW + 1 else TERMS_PER_ROW
    for start in range(0, len(terms), per_row):
        chunk = terms[start:start + per_row]
        text = "".join(_signed(s, b, start == 0 and i == 0) for i, (s, b) in enumerate(chunk))
        rows.append((head if start == 0 else r"&\quad") + text)
    rows[-1] += tail
    return rows


def lovelock_component(k: int, key: str) -> sp.Expr:
    data = json.loads(A4_EQUATIONS.read_text("utf-8"))
    return _wl_poly(data["lovelockTensors"][f"E{k}"][key]["input"])


A4_COMPONENT_LABELS = {"x0x0": "x_0", "x1x1": "x_1", "x4x4": "x_4"}


def lovelock_blocks() -> dict[str, str]:
    """The independent diagonal Lovelock components E_(k)^mu_mu (k = 1, 2, 3; mu = x0, x1, x4), one block each;
    E_(k)^x5_x5 = E_(k)^x0_x0 (tested separately)."""
    blocks = {}
    for k in (1, 2, 3):
        for key, label in A4_COMPONENT_LABELS.items():
            head = rf"E_{{({k})}}{{}}^{{{label}}}{{}}_{{{label}}} &= "
            blocks[f"lovelock_E{k}_{key}"] = aligned(wrapped_rows(head, poly_terms(lovelock_component(k, key), A4_GENS)))
    return blocks


def einstein_block() -> str:
    data = json.loads(A4_EQUATIONS.read_text("utf-8"))["einstein"]
    rows = []
    for key, right in (("constraint_x4", r"-\kappa\rho"), ("space_x1", r"\kappa p_3"),
                       ("hidden_x0", r"\kappa p_0 = \kappa p_t")):
        lhs, _ = data[key]["input"].split("==")
        rows.append(rf"{poly_tex(_wl_poly(lhs) - _lam, A4_GENS)} + \Lambda &= {right}")
    return aligned(rows)


def history_block() -> str:
    """kappa T - Lambda of the background history with the author's weights (H = 1), polynomials in k."""
    data = json.loads(A4_EQUATIONS.read_text("utf-8"))["exponentialHistory"]["authorWeights"]["historySource_kappaT_minus_Lam"]
    if _wl_poly(data["p0"]["input"]) != _wl_poly(data["pt"]["input"]):
        raise ValueError("p0 and p_t of the history source differ")
    gens = (_kk,)
    rows = [rf"-\kappa\rho - \Lambda &= {poly_tex(_wl_poly(data['minus_rho']['input']), gens)}",
            rf"\kappa p_3 - \Lambda &= {poly_tex(_wl_poly(data['p3']['input']), gens)}",
            rf"\kappa p_0 - \Lambda = \kappa p_t - \Lambda &= {poly_tex(_wl_poly(data['p0']['input']), gens)}"]
    return aligned(rows)


def generated_blocks() -> dict[str, str]:
    blocks = {f"components_{i + 1}": block for i, block in enumerate(component_equation_blocks())}
    blocks.update(lovelock_blocks())
    blocks.update({"einstein": einstein_block(), "history": history_block()})
    return blocks


def emit() -> None:
    for name, block in generated_blocks().items():
        print(f"% {name}")
        print(block)


# ---------------------------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------------------------

def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def report_checks(key: str) -> dict[str, str]:
    data = load(REPORTS[key])
    return {item["name"]: str(item["verdict"]).upper() for item in data["checks"]}


def report_count(key: str) -> tuple[int, int]:
    """(passed, total) of a report, read from its own summary fields."""
    data = load(REPORTS[key])
    if key in ("algebra-wolfram", "theory-wolfram", "pairing-wolfram", "scope-wolfram", "t3-wolfram", "t3c-wolfram"):
        return data["summary"]["passed"], data["summary"]["total"]
    if key == "lead-u1":
        return data["summary"]["passed"], data["summary"]["total"]
    if key in ("algebra-python", "theory-python", "scope-python", "ks-source", "ks-source-a4", "ks-crosscheck",
               "fock-quartic"):
        return data["summary"]["pass"], data["summary"]["checks"]
    if key == "a4-wolfram":
        return data["checkCount"] - data["failedCount"], data["checkCount"]
    if key == "a4-python":
        return data["passCount"], data["checkCount"]
    if key in ("pairing-python", "t3-python", "t3c-python"):
        counts = data["counts"]
        return counts["pass"], counts["pass"] + counts["fail"] + counts["pending"]
    if key.startswith("ds-"):
        return data["summary"]["pass"], data["summary"]["total"]
    if key == "ds00-derive-eos":
        match = re.fullmatch(r"(\d+)/(\d+) checks pass", data["summary"])
        if match is None:
            raise ValueError(f"unexpected summary {data['summary']!r}")
        return int(match.group(1)), int(match.group(2))
    raise KeyError(key)


QUOTED_COUNTS = {
    "algebra-wolfram": "Wolfram: {p} of {t} checks pass",
    "algebra-python": "sympy: {p} of {t} checks pass",
    "theory-wolfram": "Wolfram: {p} of {t} checks pass",
    "theory-python": "sympy: {p} of {t} checks pass",
    "a4-wolfram": "Wolfram: {p} of {t} checks pass",
    "a4-python": "sympy: {p} of {t} checks pass",
    "pairing-wolfram": "Wolfram: {p} of {t} checks pass",
    "pairing-python": "sympy: {p} of {t} checks pass",
    "scope-wolfram": "Wolfram: {p} of {t} checks pass",
    "scope-python": "sympy: {p} of {t} checks pass",
    "t3-wolfram": "Wolfram: {p} of {t} checks pass",
    "t3-python": "sympy: {p} of {t} checks pass",
    "ks-source": "Python: {p} of {t} checks pass",
    "ks-source-a4": "Python: {p} of {t} checks pass",
    "t3c-wolfram": "Wolfram: {p} of {t} checks pass",
    "t3c-python": "sympy: {p} of {t} checks pass",
    "ks-crosscheck": "`Revision/kohn_sham/reports/ks-crosscheck.json`: {p} of {t} checks pass",
    "ds-derivation": "derivation: {p} of {t} checks pass",
    "ds-ks-history": "Kohn-Sham history: {p} of {t} checks pass",
    "ds-eos": "equation of state: {p} of {t} checks pass",
    "ds-independent": "independent: {p} of {t} checks pass",
    "ds00-derive-eos": "dirac16complex00 derivation (cited for the phantom window of the drifting condensate): {p} of {t} checks pass",
    "fock-quartic": "no Wolfram counterpart): {p} of {t} checks pass",
    "lead-u1": "lead checks: {p} of {t} checks pass",
}


def markdown_text() -> str:
    return MARKDOWN.read_text(encoding="utf-8")


def code_spans_outside_fences(text: str) -> list[str]:
    spans = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        spans.extend(re.findall(r"`([^`\n]+)`", line))
    return spans


def is_path_or_command(span: str) -> bool:
    return ("/" in span or " " in span or "\\" in span
            or re.search(r"\.(json|md|py|wls|wl|tex|pdf|csv|rs|toml|nb)$", span) is not None)


def wl_to_sympy(text: str) -> sp.Expr:
    """Parse a Wolfram InputForm expression of field-theory.json (no field symbols)."""
    t = _wl_metric_symbols(text)
    for name in ("Sin", "Cos", "Tan", "Cot", "Sec", "Csc", "Abs"):
        t = t.replace(name + "[", name.lower() + "(")
    t = t.replace("[", "(").replace("]", ")").replace("^", "**")
    local = {"E": sp.E, "a4": _a4, "z": _z, "H": _H, "A1": _A1, "A2": _A2, "b4": _b4, "B1": _B1,
             "B2": _B2, "sqrt": sp.sqrt, "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot,
             "sec": sp.sec, "csc": sp.csc, "abs": sp.Abs, "rftSig": sp.sign(sp.cot(_z))}
    return sp.sympify(t, locals=local)


# Exact test points in four quarters of z (every real z; no sign of sin z or cos z is assumed).
TEST_POINTS = [
    {_a4: sp.Rational(3, 7), _z: sp.Rational(5, 9), _H: sp.Rational(2, 3), _A1: sp.Rational(-4, 5),
     _A2: sp.Rational(7, 11), _b4: sp.Rational(5, 3), _B1: sp.Rational(-2, 7), _B2: sp.Rational(3, 5)},
    {_a4: sp.Rational(-1, 3), _z: sp.Rational(11, 5), _H: sp.Rational(3, 2), _A1: sp.Rational(5, 4),
     _A2: sp.Rational(-2, 9), _b4: sp.Rational(7, 2), _B1: sp.Rational(9, 4), _B2: sp.Rational(-1, 6)},
    {_a4: sp.Rational(1, 2), _z: sp.Rational(-13, 4), _H: sp.Rational(1, 3), _A1: sp.Rational(2, 3),
     _A2: sp.Rational(1, 8), _b4: sp.Rational(2, 9), _B1: sp.Rational(-5, 3), _B2: sp.Rational(4, 7)},
    {_a4: sp.Rational(-2, 5), _z: sp.Rational(-7, 5), _H: sp.Rational(5, 4), _A1: sp.Rational(-1, 6),
     _A2: sp.Rational(3, 4), _b4: sp.Rational(11, 6), _B1: sp.Rational(1, 9), _B2: sp.Rational(-7, 8)},
]


def is_zero(expr: sp.Expr) -> bool:
    """Exact simplification first, then a 50-digit check at the four test points (a nonzero
    expression is detected at a generic point; the points lie in four different quarters of z)."""
    expr = sp.sympify(expr)
    if sp.simplify(expr) == 0:
        return True
    return all(abs(sp.N(expr.subs(point), 50)) < sp.Float("1e-40") for point in TEST_POINTS)


# ---------------------------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------------------------

class DocumentFilesTest(unittest.TestCase):
    def test_markdown_is_lf_only_utf8(self):
        data = MARKDOWN.read_bytes()
        self.assertNotIn(b"\r", data)
        data.decode("utf-8")
        self.assertTrue(data.endswith(b"\n"))

    def test_title_subtitle_and_sections(self):
        lines = markdown_text().splitlines()
        self.assertEqual(lines[0], "# " + TITLE)
        self.assertIn("## " + SUBTITLE, lines)
        headings = [line[3:] for line in lines if line.startswith("## ")][1:]
        self.assertEqual(headings, SECTIONS)

    def test_tex_is_the_builder_output_of_the_markdown(self):
        latex = builder.convert(
            markdown_text(),
            strip_heading_numbers=True,
            developer_layout=True,
            author=builder.DEFAULT_AUTHOR,
            date=builder.DEFAULT_DATE,
            image_root=ROOT,
        )
        self.assertEqual(TEX.read_bytes(), latex.encode("utf-8"))

    def test_registered_edition_matches_the_pdf_file(self):
        registry = load(REGISTRY)
        self.assertIn(EDITION, registry)
        entry = registry[EDITION]
        pdf_bytes = PDF.read_bytes()
        self.assertEqual(entry["path"], PDF_RELATIVE)
        self.assertEqual(entry["sha256"], hashlib.sha256(pdf_bytes).hexdigest())
        self.assertEqual(entry["pages"], len(check_dissertation_pdf.PAGE_PATTERN.findall(pdf_bytes)))
        self.assertTrue(pdf_bytes.startswith(b"%PDF-"))
        self.assertTrue(pdf_bytes.rstrip().endswith(b"%%EOF"))
        self.assertEqual(check_dissertation_pdf.parse_media_boxes(pdf_bytes), [(0.0, 0.0, 612.0, 792.0)])

    def test_required_phrases_present_and_no_placeholders(self):
        text = markdown_text()
        for phrase in REQUIRED_PHRASES:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)
        for placeholder in PLACEHOLDERS:
            with self.subTest(placeholder=placeholder):
                self.assertNotIn(placeholder, text)
        for phrase in STALE_PHRASES:
            with self.subTest(stale=phrase):
                self.assertNotIn(phrase, text)

    def test_no_old_stage_paths_are_cited(self):
        text = markdown_text()
        for old in ("artifacts/", "provenance/", "studies/", "notebooks/", "dirac-main", "vendor/"):
            with self.subTest(old=old):
                self.assertNotIn(old, text)


class CitedChecksTest(unittest.TestCase):
    def test_every_cited_check_exists_and_passes(self):
        verdicts: dict[str, set[str]] = {}
        for key in REPORTS:
            for name, verdict in report_checks(key).items():
                verdicts.setdefault(name, set()).add(verdict)
        cited = set()
        for span in code_spans_outside_fences(markdown_text()):
            if is_path_or_command(span) or span in NON_CHECK_SPANS:
                continue
            cited.add(span)
            with self.subTest(check=span):
                self.assertTrue(span in verdicts, f"cited check {span!r} is in no report")
                self.assertEqual(verdicts.get(span), {"PASS"})
        for name in ESSENTIAL_CHECKS:
            with self.subTest(essential=name):
                self.assertIn(name, cited)

    def test_quoted_counts_match_the_reports(self):
        text = markdown_text()
        for key, pattern in QUOTED_COUNTS.items():
            passed, total = report_count(key)
            with self.subTest(report=key):
                self.assertEqual(passed, total, f"{key}: not every check passes")
                self.assertIn(pattern.format(p=passed, t=total), text)

    def test_quoted_numbers_of_the_second_wave(self):
        text = markdown_text()
        self.assertGreater(len(QUOTED_NUMBERS), 3)
        for key, in_report, in_document in QUOTED_NUMBERS:
            with self.subTest(report=key, number=in_report):
                self.assertIn(in_report, REPORTS[key].read_text(encoding="utf-8"))
                self.assertIn(in_document, text)

    def test_chosen_sigma0_values_match_the_cases_file(self):
        """Section 13: for the three theories other than the author's weights sigma0 is CHOSEN at six values."""
        import csv
        with KS_SOURCE_CASES.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        chosen = {row["case"] for row in rows if row["gravity"] != "author"}
        self.assertEqual(chosen, {f"sigma0 = {v}" for v in ("-10", "-1", "-1/10", "1/10", "1", "10")})
        self.assertEqual({row["gravity"] for row in rows}, {"author", "einstein", "egb", "lovelock3"})
        self.assertEqual({row["case"] for row in rows if row["gravity"] == "author"}, {"Lambda = -10"})
        self.assertIn(r"is CHOSEN at the six values $-10, -1, -1/10, 1/10, 1, 10$", markdown_text())

    def test_comparison_record_statement_matches_the_theory_reports(self):
        text = markdown_text()
        python_report = load(REPORTS["theory-python"])
        comparison = python_report["comparison_with_wolfram"]
        wolfram_names = list(report_checks("theory-wolfram"))
        referenced = set(comparison["checks"]["wolfram_checks_without_sympy_counterpart"])
        for record in comparison["checks"]["records"]:
            referenced |= set(record["wolfram_checks"])
        uncovered = [name for name in wolfram_names if name not in referenced]
        self.assertEqual(comparison["status"], "agree")
        self.assertEqual(comparison["formulas"]["not_compared"], [])
        self.assertEqual(comparison["formulas"]["agree"], comparison["formulas"]["compared"])
        self.assertEqual(comparison["checks"]["agree"], comparison["checks"]["pairs"])
        wolfram = load(REPORTS["theory-wolfram"])
        self.assertEqual(comparison["wolfram_summary"], wolfram["summary"])
        self.assertIn(f"a Wolfram run of {comparison['wolfram_summary']['total']} checks", text)
        self.assertIn(f"{comparison['formulas']['agree']} of {comparison['formulas']['compared']} formula records", text)
        self.assertIn(f"{comparison['checks']['agree']} of {comparison['checks']['pairs']} check pairs", text)
        self.assertEqual(uncovered, [])
        for name in comparison["checks"]["wolfram_checks_without_sympy_counterpart"]:
            self.assertIn(f"`{name}`", text)
        if not comparison["checks"]["wolfram_checks_without_sympy_counterpart"]:
            total = comparison["wolfram_summary"]["total"]
            self.assertIn(f"every one of the {total} Wolfram checks is paired with a sympy check", text)
            self.assertNotIn("paired with a sympy check except", text)


class GeneratedBlocksTest(unittest.TestCase):
    def test_generated_blocks_are_in_the_document(self):
        text = markdown_text()
        for name, block in generated_blocks().items():
            with self.subTest(block=name):
                self.assertIn("$$\n" + block + "\n$$", text)

    def test_renderer_detects_a_changed_coefficient(self):
        # negative controls: the extra-time factor or the hidden-block term of the withdrawn metric is refused
        formulas = {item["key"]: item["wl"] for item in load(FIELD_THEORY)["formulas"]}
        for old, new in (("(Sin[6*H*x0]^2)^(1/12)", "Sin[6*H*x0]^(1/6)*E^a4[x4]"),
                         ("(3*E^a4[x4]*H*Psi[", "(6*E^a4[x4]*H*Psi[")):
            texts = [t.replace(old, new) for t in formulas["field_equation_components"]]
            self.assertNotEqual(texts, formulas["field_equation_components"])
            exprs = [_parse_component(t)[0] for t in texts]
            with self.subTest(change=new), self.assertRaises(ValueError):
                component_equation_rows(exprs)

    def test_component_equations_agree_with_the_sympy_report(self):
        sympy_components = load(REPORTS["theory-python"])["formulas"]["dirac_equation_components"]["components"]
        lam, m, x4, x0 = sp.symbols("lam m x4 x0")
        a4f, b4f = sp.Function("a4"), sp.Function("b4")
        for number, wolfram in enumerate(wolfram_component_lhs(), 1):
            text = sympy_components[f"E{number}"]
            t = re.sub(r"psi(\d+)_x(\d)", r"D_\2_\1", text)
            t = re.sub(r"psi(\d+)", r"P_\1", t)
            t = re.sub(r"chi(\d+)", r"C_\1", t)
            t = t.replace("lambda", "lam")
            expr = sp.sympify(t, locals={"lam": lam, "m": m, "H": _H, "x4": x4, "x0": x0, "a4": a4f, "b4": b4f,
                                          "exp": sp.exp, "sin": sp.sin, "cos": sp.cos, "sqrt": sp.sqrt,
                                          "Abs": sp.Abs, "Derivative": sp.Derivative})
            expr = expr.subs(sp.Derivative(b4f(x4), x4), _B1).subs(sp.Derivative(a4f(x4), x4), _A1)
            expr = expr.subs({a4f(x4): _a4, b4f(x4): _b4}).subs(x0, _z / (6 * _H))
            mass = sp.expand(expr).coeff(m)
            linear = sp.expand(expr).subs({lam: 0, m: 0})
            with self.subTest(component=number):
                self.assertEqual(mass, -sp.Symbol(f"P_{number}"))
                self.assertIn(_B1, linear.free_symbols)  # the v_g term is part of every component
                symbols = sorted((linear.free_symbols | wolfram.free_symbols) - {_a4, _z, _H, _b4, _A1, _B1},
                                 key=lambda s: s.name)
                for symbol in symbols:
                    self.assertTrue(is_zero(linear.coeff(symbol) - wolfram.coeff(symbol)), (number, symbol))

    def test_connection_and_curvature_formulas_match_the_formula_file(self):
        """The hand-written formulas of sections 2 and 4 (corrected metric, u = b4'/b4, v = u')."""
        text = markdown_text()
        for formula in DOCUMENT_FORMULAS:
            with self.subTest(formula=formula):
                self.assertIn(formula, text)
        formulas = {item["key"]: item["wl"] for item in load(FIELD_THEORY)["formulas"]}
        e = sp.exp(_a4)
        sb = sp.sqrt(_b4) / e                    # e^{-a4} b4^{1/2}
        w = (sp.sin(_z) ** 2) ** sp.Rational(1, 12)
        u = _B1 / _b4
        h4 = u / 2 - _A1                         # the rate of the block (x0, x5, x6, x7)
        kk = sp.exp(2 * _a4) / _b4
        # vielbein and sqrt|g| (list position k + 1 holds x_k)
        f = re.findall(r"[^{},]+(?:\[[^\]]*\][^{},]*)*", formulas["vielbein_diagonal"])
        expected_f = [sb * sp.cot(_z)] + [e] * 3 + [1] + [sb * w] * 3
        self.assertEqual(len(f), 8)
        for got, want in zip(f, expected_f):
            self.assertTrue(is_zero(wl_to_sympy(got) - want), got)
        sqrt_g = wl_to_sympy(formulas["sqrt_det_g"])
        self.assertTrue(is_zero(sqrt_g - sp.exp(-_a4) * _b4**2 * sp.Abs(sp.cot(_z)) * (sp.sin(_z) ** 2) ** sp.Rational(1, 4)))
        # Christoffel symbols: 21 nonzero
        entries = re.findall(r"\{(\d), (\d), (\d), ([^{}]+)\}", formulas["christoffel_nonzero"])
        P = {k: k + 1 for k in range(8)}
        s3 = (sp.sin(_z) ** 2) ** sp.Rational(1, 6)
        expected = {(P[0], P[0], P[0]): -12 * _H * sp.csc(2 * _z), (P[0], P[0], P[4]): h4,
                    (P[4], P[0], P[0]): sp.exp(-2 * _a4) * _b4 * sp.cot(_z) ** 2 * h4}
        for i in (1, 2, 3):
            expected[(P[i], P[i], P[4])] = _A1
            expected[(P[4], P[i], P[i])] = sp.exp(2 * _a4) * _A1
        for t in (5, 6, 7):
            expected[(P[0], P[t], P[t])] = _H * s3 * sp.tan(_z)
            expected[(P[4], P[t], P[t])] = -sp.exp(-2 * _a4) * _b4 * s3 * h4
            expected[(P[t], P[0], P[t])] = _H * sp.cot(_z)
            expected[(P[t], P[4], P[t])] = h4
        got = {(int(a), int(b), int(c)): wl_to_sympy(v_) for a, b, c, v_ in entries}
        self.assertEqual(len(got), 21)
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(christoffel=key):
                self.assertTrue(is_zero(value - expected[key]))
        # Ricci tensor (diagonal) and scalar, with b4''/b4 = B2/b4
        entries = re.findall(r"\{(\d), (\d), ([^{}]+)\}", formulas["ricci_mixed_nonzero"])
        hidden = -3 * _H**2 * kk + _A1**2 - _A2 - sp.Rational(5, 2) * _A1 * u + _B2 / (2 * _b4) + u**2 / 2
        expected = {(P[0], P[0]): hidden, (P[4], P[4]): 7 * _A1**2 - _A2 - 4 * _A1 * u + 2 * _B2 / _b4 - u**2}
        for i in (1, 2, 3):
            expected[(P[i], P[i])] = -_A1**2 + _A2 + 2 * _A1 * u
        for t in (5, 6, 7):
            expected[(P[t], P[t])] = hidden
        got = {(int(a), int(b)): wl_to_sympy(v_) for a, b, v_ in entries}
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(ricci=key):
                self.assertTrue(is_zero(value - expected[key]))
        self.assertTrue(is_zero(wl_to_sympy(formulas["ricci_scalar"])
                                - (-12 * _H**2 * kk + 8 * _A1**2 - 2 * _A2 - 8 * _A1 * u + 4 * _B2 / _b4 + u**2)))
        # spin connection: 10 nonzero omega_mu,ab (a < b)
        entries = re.findall(r"\{(\d), (\d), (\d), ([^{}]+)\}", formulas["omega_nonzero"])
        expected = {(P[0], P[0], P[4]): h4 * sb * sp.cot(_z)}
        for i in (1, 2, 3):
            expected[(P[i], P[i], P[4])] = _A1 * e
        for t in (5, 6, 7):
            expected[(P[t], P[4], P[t])] = h4 * sb * w
            expected[(P[t], P[0], P[t])] = _H * w
        got = {(int(a), int(b), int(c)): wl_to_sympy(v_) for a, b, c, v_ in entries}
        self.assertEqual(len(got), 10)
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(omega=key):
                self.assertTrue(is_zero(value - expected[key]))
        # gamma^mu Omega_mu per direction: coefficients of gamma^(x4) and gamma^(x0)
        entries = re.findall(r"\{(\d), ([^{},]+), ([^{},]+)\}", formulas["gammaOmega_per_direction"])
        extra = (h4 / 2, _H * e / (2 * sp.sqrt(_b4)))
        want = {P[0]: (h4 / 2, 0), P[1]: (_A1 / 2, 0), P[2]: (_A1 / 2, 0), P[3]: (_A1 / 2, 0),
                P[4]: (0, 0), P[5]: extra, P[6]: extra, P[7]: extra}
        self.assertEqual(len(entries), 8)
        for mu, c4, c0 in entries:
            with self.subTest(direction=mu):
                self.assertTrue(is_zero(wl_to_sympy(c4) - want[int(mu)][0]))
                self.assertTrue(is_zero(wl_to_sympy(c0) - want[int(mu)][1]))
        total = formulas["gammaOmega_total"].replace('gamma["x0"]', "G0").replace('gamma["x4"]', "G4")
        g0, g4 = sp.symbols("G0 G4")
        total = sp.sympify(_wl_metric_symbols(total).replace("^", "**"),
                           locals={"G0": g0, "G4": g4, "H": _H, "b4": _b4, "B1": _B1, "A1": _A1, "a4": _a4,
                                   "E": sp.E, "sqrt": sp.sqrt})
        self.assertEqual(sp.simplify(total - (C_G * g0 + V_G * g4)), 0)


class FieldEquationFormulasTest(unittest.TestCase):
    """The rendered components of section 13 add up to the general formulas of a4-equations.json."""

    def setUp(self):
        self.data = load(A4_EQUATIONS)

    def general(self, key: str) -> sp.Expr:
        return _wl_poly(self.data["generalSource"][key]["input"].split("==")[0])

    def test_diagonal_equations_are_the_sums_of_the_rendered_components(self):
        for key, label in (("constraint_x4", "x4x4"), ("space_x1_eq_x2_eq_x3", "x1x1"),
                           ("hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7", "x0x0")):
            rendered = sum(a * lovelock_component(k, label) for k, a in zip((1, 2, 3), _alphas)) + _lam
            with self.subTest(component=key):
                self.assertEqual(sp.expand(rendered - self.general(key)), 0)

    def test_hidden_component_equals_the_extra_time_component(self):
        for k in (1, 2, 3):
            with self.subTest(order=k):
                self.assertEqual(sp.expand(lovelock_component(k, "x0x0") - lovelock_component(k, "x5x5")), 0)
        self.assertIn("p0 = p_t", self.data["generalSource"]["hiddenEqualsExtraTimes"])
        self.assertIn("T^x4_x0 = T^x0_x4 = 0", self.data["generalSource"]["offDiagonal"])

    def test_einstein_is_the_first_order_of_the_general_equations(self):
        einstein = self.data["einstein"]
        for key, label in (("constraint_x4", "x4x4"), ("space_x1", "x1x1"), ("hidden_x0", "x0x0")):
            lhs = _wl_poly(einstein[key]["input"].split("==")[0])
            with self.subTest(component=key):
                self.assertEqual(sp.expand(lhs - lovelock_component(1, label) - _lam), 0)

    def test_background_history_with_the_author_weights(self):
        history = self.data["exponentialHistory"]
        source = history["requiredSource"]
        point = {_AA: 1, _be: sp.Rational(4, 3), _H: 1, _lam: -10, **AUTHOR_WEIGHTS}
        hs = history["authorWeights"]["historySource_kappaT_minus_Lam"]
        expected = {"rho": -_wl_poly(hs["minus_rho"]["input"]) - _lam, "p3": _wl_poly(hs["p3"]["input"]) + _lam,
                    "p0": _wl_poly(hs["p0"]["input"]) + _lam, "pt": _wl_poly(hs["pt"]["input"]) + _lam}
        for key, value in expected.items():
            expr = sp.sympify(source[key]["input"].replace("^", "**"), locals=_A4_LOCALS) * _kappa
            with self.subTest(entry=key):
                self.assertEqual(sp.simplify(expr.subs(point) - value.subs(_lam, -10)), 0)
                # the required source of an exponential history, written in k, is even in A
                self.assertEqual(sp.simplify(expr - expr.subs(_AA, -_AA)), 0)
        anisotropy = sp.expand(_wl_poly(hs["p3"]["input"]) - _wl_poly(hs["p0"]["input"]))
        self.assertEqual(anisotropy, sp.expand(-sp.Rational(9, 16) * _kk**2 + sp.Rational(1069, 432) * _kk
                                               + sp.Rational(2015, 972)))


@unittest.skipUnless(os.environ.get("REVISION_PDF_REBUILD") == "1", "set REVISION_PDF_REBUILD=1 to rebuild the PDF in verify mode")
class PdfRebuildTest(unittest.TestCase):
    def test_verify_mode_reproduces_the_registered_edition(self):
        completed = subprocess.run(
            [sys.executable, "scripts/build_provenance_pdf.py", f"Revision/docs/{STEM}.md",
             "--developer-layout", "--specifications", "Revision/pdf-specifications.json"],
            cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, timeout=1800,
        )
        output = completed.stdout.decode("utf-8", "replace")
        self.assertEqual(completed.returncode, 0, output[-4000:])
        self.assertIn("provenance_pdf=OK", output)
        self.assertIn("measurement_warningLineCount=0", output)


if __name__ == "__main__":
    if "--emit" in sys.argv:
        emit()
        raise SystemExit(0)
    unittest.main()
