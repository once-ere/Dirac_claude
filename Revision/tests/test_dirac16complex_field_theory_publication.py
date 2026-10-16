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

What is tested (fast, read-only):
  * the .tex is exactly the builder's output for the .md with the options the
    PDF command uses (--strip-heading-numbers, --developer-layout, default author and date);
  * the .md is UTF-8 with LF line endings only and has the title and subtitle;
  * the registry entry of the edition names the PDF file, its page count and its sha256; the
    PDF starts with %PDF-, ends with %%EOF and has only US-letter media boxes;
  * key statements are present (non-triviality [1], the Krein structure, the a4 equations, what is
    not claimed) and no placeholder text is left;
  * every check name the document cites (in a code span) exists, with a passing verdict, in one of
    the Revision reports the document is drawn from (REPORTS below); a list of essential checks is cited;
  * the check counts the document quotes equal the counts in the reports, and the statement about
    the comparison record of the theory branch matches the two theory reports;
  * the 16 component field equations, the Lovelock components E_(k) (in a4', a4'', u = b4'/b4,
    v = u', H), the factors Q_(k) of their x4-x0 components, the parts I_(k) of the identity
    x1 + x5 - 2 x0, the Einstein components and the factor Q(A, beta) of the author's weights in
    the document are the output of the renderers below applied to Revision/theory/field-theory.json
    and Revision/field_equations_a4/a4-equations.json, and the sums over k of the rendered parts
    equal the general formulas of a4-equations.json;
  * the 16 component equations agree with the independent sympy expressions of
    Revision/theory/reports/python-field-theory.json (formulas.dirac_equation_components);
  * the vielbein, sqrt|g|, the Christoffel symbols, the Ricci components, the spin connection and
    the per-direction contractions gamma^mu Omega_mu written in the document equal the entries of
    Revision/theory/field-theory.json (the metric with b4(x4), general a4 and b4);
  * the source that the history a4 = H x4, b4 = b4(0) e^((4/3) H x4) requires with the author's
    weights is the one quoted, and the required source of an exponential history is even in A.
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
    "offDiagonalFactor_Q", "identity_x1_plus_x5_minus_2x0", "secondOrderJacobianDet",
    "sourceRequiredByGivenHistory", "einstein", "exponentialHistory", "requiredSource",
    "authorWeights", "fields", "emtConvention", "comparison_with_wolfram", "dirac_equation_components",
    "not_established", "wolframscript", "pdflatex", "wolfram_checks_without_sympy_counterpart",
}

ESSENTIAL_CHECKS = [
    "Pin44_irreducible_commutant_dim_1", "pin_commutant_dimension_1",
    "chiral_halves_inequivalent_intertwiners_0", "spin_halves_inequivalent",
    "metric_is_the_authors", "sqrt_det_g", "sqrt_det_g_equals_b4_cos_z", "ricci_mixed_components",
    "vielbein_postulate", "Omega_components", "gammaOmega_total", "gammaOmega_per_direction",
    "gamma_mu_Omega_mu_equals_3H_gamma_x0_plus_b4_term", "a4_time_terms_cancel_b4_terms_add",
    "gravity_term_square", "nontriviality_1_dirac16complex",
    "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish", "never_flat_for_H_positive",
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
    "Q_one_particle_Krein_inertia_real_frequencies", "Q_one_particle_complex_and_zero_frequencies_Krein_neutral",
    "ks_profiles_violate_algebraic_condition", "ks_history_is_a_prescribed_background",
    "ks_offdiagonal_condition_on_history", "T3_energies_and_emt_profiles_equal",
    "lovelock_depends_on_b4_through_u_and_v", "offdiagonal_factorises",
    "algebraic_identity_x1_plus_x5_minus_2x0", "constraint_propagation_bianchi",
    "second_order_system_a4pp_vv", "einstein_null_energy_x0", "einstein_offdiagonal_forces_b4_constant",
    "author_weights_branch", "author_weights_history_source", "author_weights_no_vacuum_with_b4_not_constant",
    "condensate_source_with_b4_not_constant", "Q_Krein_metric_of_images",
    "A1_x1_x5_x0_combination_with_b4", "A2_offdiagonal_equation_needs_Q_zero",
    "B2_x0_conservation_on_every_profile", "C1_averaged_algebraic_condition_fails",
    "C3_record_history_not_a_solution_of_the_x4_moment", "D2_author_weights_start_on_the_record_history",
    "T3C_krein_rule_16_component", "T3C.krein_rule_16_component",
    "mode_hamiltonian_good_sector", "good_sector_positive_fock_realisation",
    "trace_identity_operator_identity_wick", "trace_identity_fails_for_every_other_combination",
    "homogeneous_rho_p_operator_identities_wick", "negative_control_free_dynamics",
]

REQUIRED_PHRASES = [
    "16 complex anticommuting components",
    "irreducible under Pin(4,4)",
    "two inequivalent irreducible 8-dimensional representations",
    "Theorem 1 (non-triviality [1])",
    "the $a_4'$ terms of the time direction of the three inflating and the three deflating directions cancel",
    r"\gamma^\mu\Omega_\mu = 3H\gamma^{(0)} + \tfrac34u\,\gamma^{(4)}",
    r"\big(9H^2 - \tfrac{9}{16}u^2\big)\,I_{16}",
    r"$b_4$ is never 1",
    r"a_4 = Hx_4,\quad b_4 = b_4(0)\,e^{(4/3)Hx_4}",
    "never flat for $H > 0$",
    "is a total derivative",
    "Theorem 2 (the canonical anticommutator forces a Krein structure)",
    "no positive inner product",
    "normal ordered",
    r"\hat T^\nu{}_\mu",
    "p_3 + p_t = 2p_0",
    "a_4 = AHx_4 + a_0",
    r"\sigma_T = +1",
    "no creation process",
    "is not claimed",
    "Numbers and formulas are taken only from",
    "belongs to the diagonal vielbein",
    "vanishes in no frame",
    "no boost in this plane removes",
    "Krein-neutral",
    "not well posed in Hadamard's sense",
    "prescribed test-field background without back-reaction",
    "is a choice of sign",
    "the Kohn-Sham source does not start or select exponential deflation of the extra times",
    "That record establishes neither Hypothesis nor Hypothesis00.",
    "no Kohn-Sham state comes near the Unite pair $(w_0, w_a) = (-0.861, -0.60)$",
    "`Revision/docs/KOHN_SHAM_DEFLATING_FIELD`",
    "`Revision/docs/LOVELOCK_GKD`",
    "`Revision/docs/DARK_SECTOR_HYPOTHESES`",
    "constructed and checked only for single good-sector momenta with frozen coefficients",
    "a positive-norm Hilbert space for the full field is not established",
    "the identity holds in this model if and only if the potential and the energy-momentum tensor are both Wick ordered",
    "Nothing is proved for the field on a whole slice",
    r"and in section 15 (the equation-of-state values $w_{\rm eff}$ of the Kohn-Sham gas",
    r"\kappa(\rho, p_3, p_t, p_0) = \big(-\tfrac{2}{27}, -\tfrac29, -\tfrac{22}{27}, -\tfrac{14}{27}\big)",
]

# Numbers quoted from the second-wave reports: (report key, text in the report, text in the document).
QUOTED_NUMBERS = [
    ("ks-source-a4", "[0.411101 (N688_lamm2_a00), 0.806379] over the 70 nonzero states",
     "between 0.411101 and 0.806379 over the 70 nonzero states"),
    ("ks-source-a4", "at least a share 0.582938 of the energy density deviates from its hidden-direction average",
     "at least a share 0.582938 of the energy density deviates from its hidden-direction average"),
    ("ks-source-a4", "fold at a4 = 0.024 with a4'/H = 0.870762, (b4'/b4)/H = 1.09136",
     r"at $a_4 = 0.024$, with $a_4'/H = 0.870762$ and $u/H = 1.09136$"),
    ("ks-source", "N136_lam0_a00: 0.339767, N136_lam0_a10: 0.25969, N136_lam0_a20: 0.239714",
     "0.339767, 0.25969 and 0.239714"),
    ("ds-eos", "w_eff(C) in [-0.040541, -0.006532]", "between -0.040541 and -0.006532"),
]

PLACEHOLDERS = ["TODO", "TBD", "FIXME", "lorem ipsum", "PLACEHOLDER", "XXX"]

# Stale or unqualified statements corrected after review (2026-10-08): the documents named exist,
# the charge is only locally conserved, and nothing past the Lambda = 0 turning point is computed.
# Since 2026-10-16 (the metric with b4(x4), b4 never 1) the statements of the withdrawn metric b4 = 1
# must not reappear as results.
STALE_PHRASES = ["planned and not yet written", "the conserved charge", "re-inflate",
                 "for every series with 3-momentum", "to be confirmed by the theory branch",
                 "the record of the case $b_4 = 1$", "Not recomputed for general", "F(a_4')",
                 r"\sqrt{|g|} = \cos z", "linear member", r"3H\gamma^{(0)}$ for every $a_4$"]

# Hand-written formulas of the document that are compared with field-theory.json below
# (u = b4'/b4, v = u' = b4''/b4 - u^2).
DOCUMENT_FORMULAS = [
    r"f_0 = \cot z,\quad f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z,\quad f_4 = 1,\quad f_5 = f_6 = f_7 = e^{-a_4}b_4^{1/2}\sin^{1/6}z",
    r"\sqrt{|g|} = f_0 f_1\cdots f_7 = b_4^{3/2}\sin z\cot z = b_4^{3/2}\cos z",
    r"\Gamma^{x_i}{}_{x_i x_4} &= a_4', & \Gamma^{x_i}{}_{x_i x_0} &= H\cot z,",
    r"\Gamma^{x_t}{}_{x_4 x_t} &= -\big(a_4' - \tfrac12u\big), & \Gamma^{x_t}{}_{x_t x_0} &= H\cot z,",
    r"\Gamma^{x_4}{}_{x_i x_i} &= e^{2a_4}\sin^{1/3}z\,a_4', & \Gamma^{x_4}{}_{x_t x_t} &= e^{-2a_4}b_4\sin^{1/3}z\,\big(a_4' - \tfrac12u\big),",
    r"\Gamma^{x_0}{}_{x_i x_i} &= -e^{2a_4}H\,\frac{\sin^{4/3}z}{\cos z}, & \Gamma^{x_0}{}_{x_t x_t} &= e^{-2a_4}b_4H\,\frac{\sin^{4/3}z}{\cos z},",
    r"\Gamma^{x_0}{}_{x_0 x_0} &= -\frac{6H}{\sin z\cos z}",
    r"R^{x_0}{}_{x_0} &= -6H^2, & R^{x_i}{}_{x_i} &= a_4'' - 6H^2 + \tfrac32a_4'u,",
    r"R^{x_4}{}_{x_4} &= 6(a_4')^2 - 3a_4'u + \tfrac34u^2 + \tfrac32v, & R^{x_t}{}_{x_t} &= -a_4'' - 6H^2 - \tfrac32a_4'u + \tfrac34u^2 + \tfrac12v,",
    r"R^{x_4}{}_{x_0} &= \tfrac32Hu\cot z, & R^{x_0}{}_{x_4} &= -\tfrac32Hu\tan z,",
    r"R = 6(a_4')^2 - 3a_4'u + 3u^2 + 3v - 42H^2",
    r"\omega_{x_i\,(i)(4)} &= a_4'\,e^{a_4}\sin^{1/6}z, & \omega_{x_i\,(i)(0)} &= H\,e^{a_4}\sin^{1/6}z,",
    r"\omega_{x_t\,(4)(t)} &= -\big(a_4' - \tfrac12u\big)\,e^{-a_4}b_4^{1/2}\sin^{1/6}z, & \omega_{x_t\,(t)(0)} &= -H\,e^{-a_4}b_4^{1/2}\sin^{1/6}z,",
    r"\gamma^{x_i}\Omega_{x_i} &= \tfrac12 a_4'\,\gamma^{(4)} + \tfrac12 H\,\gamma^{(0)} \qquad (i = 1, 2, 3),",
    r"\gamma^{x_t}\Omega_{x_t} &= \big(-\tfrac12 a_4' + \tfrac14u\big)\,\gamma^{(4)} + \tfrac12 H\,\gamma^{(0)} \qquad (t = 5, 6, 7),",
]


# ---------------------------------------------------------------------------------------------
# Renderers (they generate the document blocks; the tests compare the document with them)
# ---------------------------------------------------------------------------------------------

_a4, _z, _H = sp.symbols("a4 z H", real=True)
_A1, _A2 = sp.symbols("A1 A2", real=True)
_b4 = sp.symbols("b4", positive=True)
_B1, _B2 = sp.symbols("B1 B2", real=True)                 # b4' and b4''
EPS_S = sp.exp(-_a4) * sp.sin(_z) ** sp.Rational(-1, 6)   # 1/f for x1, x2, x3
EPS_T = sp.exp(_a4) * _b4 ** sp.Rational(-1, 2) * sp.sin(_z) ** sp.Rational(-1, 6)  # 1/f for x5, x6, x7
DELTA_4 = sp.Rational(3, 4) * _B1 / _b4                   # the b4 term (3/4)(b4'/b4) of gamma^mu Omega_mu


def _wl_metric_symbols(text: str) -> str:
    """Replace the metric functions of a Wolfram InputForm text by the symbols of this file."""
    t = text.replace("Derivative[1][a4][x4]", "A1").replace("Derivative[2][a4][x4]", "A2")
    t = t.replace("Derivative[1][b4][x4]", "B1").replace("Derivative[2][b4][x4]", "B2")
    t = t.replace("Sqrt[b4[x4]]", "sqrt(b4)")
    return t.replace("a4[x4]", "a4").replace("b4[x4]", "b4").replace("12*H*x0", "(2*z)").replace("6*H*x0", "z")


def wl_to_sympy(text: str) -> sp.Expr:
    """Parse a Wolfram InputForm expression of field-theory.json (no field symbols)."""
    t = _wl_metric_symbols(text)
    for name in ("Sin", "Cos", "Tan", "Cot", "Sec", "Csc"):
        t = t.replace(name + "[", name.lower() + "(")
    t = t.replace("[", "(").replace("]", ")").replace("^", "**")
    local = {"E": sp.E, "a4": _a4, "z": _z, "H": _H, "A1": _A1, "A2": _A2, "b4": _b4, "B1": _B1,
             "B2": _B2, "sqrt": sp.sqrt, "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot,
             "sec": sp.sec, "csc": sp.csc}
    return sp.sympify(t, locals=local)


def is_zero(expr: sp.Expr) -> bool:
    expr = sp.simplify(sp.expand_trig(sp.sympify(expr).rewrite(sp.sin)))
    if expr == 0:
        return True
    # numeric confirmation at an exact rational point inside 0 < z < pi/2 (b4 > 0)
    values = {_a4: sp.Rational(3, 7), _z: sp.Rational(5, 9), _H: sp.Rational(2, 3),
              _A1: sp.Rational(-4, 5), _A2: sp.Rational(7, 11), _b4: sp.Rational(5, 3),
              _B1: sp.Rational(-2, 7), _B2: sp.Rational(3, 5)}
    return abs(sp.N(expr.subs(values), 50)) < sp.Float("1e-40")


def _parse_component(text: str) -> tuple[sp.Expr, int]:
    """Parse one Wolfram InputForm component equation 'lhs == V*Psi[A]'."""
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
    local = {"E": sp.E, "a4": _a4, "z": _z, "H": _H, "b4": _b4, "B1": _B1, "sqrt": sp.sqrt}
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


def component_equation_rows() -> list[str]:
    """The 16 component field equations as LaTeX aligned rows, from field-theory.json.

    Every component has the derivative terms of the eight directions, the hidden-direction term
    3 H psi_B with the same psi_B as tan z d0, and the b4 term (3/4)(b4'/b4) psi_C with the same
    psi_C and the same sign as d4: it is written with hat-d4 = d4 + (3/4)(b4'/b4)."""
    rows = []
    for number, expr in enumerate(wolfram_component_lhs(), 1):
        derivative = {}
        for symbol in expr.free_symbols:
            name = symbol.name
            if name.startswith("D_"):
                _, k, b = name.split("_")
                if int(k) in derivative:
                    raise ValueError(f"two x{k} derivatives in component {number}")
                derivative[int(k)] = (int(b), expr.coeff(symbol))
        field_terms = [s for s in expr.free_symbols if s.name.startswith("P_")]
        if len(field_terms) != 2 or sorted(derivative) != list(range(8)):  # x0..x7, x0 the hidden direction
            raise ValueError(f"unexpected structure of component {number}")
        rest = sp.expand(expr - sum(c * sp.Symbol(f"D_{k}_{b}") for k, (b, c) in derivative.items())
                         - sum(expr.coeff(p) * p for p in field_terms))
        if rest != 0:
            raise ValueError(f"unexpected remainder {rest} in component {number}")
        bases = {0: sp.tan(_z), 1: EPS_S, 2: EPS_S, 3: EPS_S, 4: sp.Integer(1), 5: EPS_T, 6: EPS_T, 7: EPS_T}
        signs = {k: _sign(c, bases[k]) for k, (b, c) in derivative.items()}
        hidden_b, time_b = derivative[0][0], derivative[4][0]
        coefficients = {int(p.name[2:]): expr.coeff(p) for p in field_terms}
        if sorted(coefficients) != sorted((hidden_b, time_b)) or hidden_b == time_b:
            raise ValueError(f"the non-derivative terms of component {number} are not on psi_{hidden_b}, psi_{time_b}")
        if signs[0] != 1 or _sign(coefficients[hidden_b], 3 * _H) != 1:
            raise ValueError(f"the hidden-direction terms of component {number} are not (tan z d0 + 3H)")
        if _sign(coefficients[time_b], DELTA_4) != signs[4]:
            raise ValueError(f"the b4 term of component {number} is not (3/4)(b4'/b4) with the sign of d4")
        space = "".join(_signed(signs[k], rf"\partial_{k}\psi_{{{derivative[k][0]}}}", k == 1)
                        for k in (1, 2, 3))
        time = "".join(_signed(signs[k], rf"\partial_{k}\psi_{{{derivative[k][0]}}}", k == 5)
                       for k in (5, 6, 7))
        x4 = _signed(signs[4], rf"\hat\partial_4\psi_{{{time_b}}}", False)
        rows.append(rf"\epsilon_s({space}){x4} + \epsilon_t({time}) + (\tan z\,\partial_0 + 3H)"
                    rf"\psi_{{{hidden_b}}} &= V\psi_{{{number}}}")
    return rows


def aligned(rows: list[str]) -> str:
    return "\\begin{aligned}\n" + " \\\\\n".join(rows) + "\n\\end{aligned}"


def component_equation_blocks() -> list[str]:
    """Two aligned blocks: the equations of rows 1..8 (Gamma = -1) and of rows 9..16."""
    rows = component_equation_rows()
    return [aligned(rows[:8]), aligned(rows[8:])]


_ad1, _ad2, _uu, _vv, _AA, _be = sp.symbols("ad1 ad2 uu vv AA be", real=True)
_cc = sp.symbols("cc", positive=True)
_alphas = sp.symbols("alpha1 alpha2 alpha3", real=True)
_lam, _kappa = sp.symbols("Lam kappa", real=True)
_A4_LOCALS = {"ad1": _ad1, "ad2": _ad2, "uu": _uu, "vv": _vv, "H": _H, "AA": _AA, "be": _be, "cc": _cc,
              "alpha1": _alphas[0], "alpha2": _alphas[1], "alpha3": _alphas[2], "Lam": _lam, "kappa": _kappa}
A4_GENS = (_ad1, _ad2, _uu, _vv, _H)        # the order of the factors in every rendered monomial
TERMS_PER_ROW = 4
FACTOR_TEX = {"ad1": "a_4'", "ad2": "a_4''", "uu": "u", "vv": "v", "H": "H", "AA": "A", "be": r"\beta"}
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
    """(sign, body) of the monomials of a polynomial with rational coefficients, in descending
    lexicographic order of the exponents of gens ((a_4')^4 before (a_4')^2 a_4'' before
    (a_4')^2 u before (a_4')^2 H^2)."""
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
    """Rows of an aligned block: head and the first TERMS_PER_ROW terms, then continuation rows
    (a polynomial of at most TERMS_PER_ROW + 1 terms stays on one row)."""
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


A4_COMPONENT_LABELS = {"x0x0": "x_0", "x1x1": "x_1", "x4x4": "x_4", "x5x5": "x_5"}


def lovelock_blocks() -> dict[str, str]:
    """The diagonal Lovelock components E_(k)^mu_mu (k = 1, 2, 3; mu = x0, x1, x4, x5), one block each."""
    blocks = {}
    for k in (1, 2, 3):
        for key, label in A4_COMPONENT_LABELS.items():
            head = rf"E_{{({k})}}{{}}^{{{label}}}{{}}_{{{label}}} &= "
            blocks[f"lovelock_E{k}_{key}"] = aligned(wrapped_rows(head, poly_terms(lovelock_component(k, key), A4_GENS)))
    return blocks


def offdiagonal_factor(k: int) -> sp.Expr:
    """Q_(k) with E_(k)^x4_x0 = cot z u Q_(k) (a polynomial in a4', u, H)."""
    factor = sp.cancel(lovelock_component(k, "x4x0") / (_cc * _uu))
    if factor.free_symbols - {_ad1, _uu, _H}:
        raise ValueError(f"E_({k})^x4_x0 is not cot z u times a polynomial in a4', u, H")
    return sp.expand(factor)


def offdiagonal_block() -> str:
    rows = []
    for k in (1, 2, 3):
        rows += wrapped_rows(rf"Q_{{({k})}} &= ", poly_terms(offdiagonal_factor(k), A4_GENS))
    return aligned(rows)


def identity_part(k: int) -> sp.Expr:
    """I_(k) = E_(k)^x1_x1 + E_(k)^x5_x5 - 2 E_(k)^x0_x0."""
    return sp.expand(lovelock_component(k, "x1x1") + lovelock_component(k, "x5x5")
                     - 2 * lovelock_component(k, "x0x0"))


def identity_block() -> str:
    rows = []
    for k in (1, 2, 3):
        rows += wrapped_rows(rf"I_{{({k})}} &= ", poly_terms(identity_part(k), A4_GENS))
    return aligned(rows)


def einstein_block() -> str:
    data = json.loads(A4_EQUATIONS.read_text("utf-8"))["einstein"]
    rows = []
    for key, right in (("constraint_x4", r"-\kappa\rho"), ("space_x1", r"\kappa p_3"),
                       ("extraTime_x5", r"\kappa p_t"), ("hidden_x0", r"\kappa p_0")):
        lhs, _ = data[key]["input"].split("==")
        rows.append(rf"{poly_tex(_wl_poly(lhs) - _lam, A4_GENS)} + \Lambda &= {right}")
    lhs, rhs = data["offDiagonal_x4x0"]["input"].split("==")
    if sp.expand(_wl_poly(rhs) - _kappa * sp.Symbol("q40")) != 0:
        raise ValueError("unexpected right-hand side of einstein.offDiagonal_x4x0")
    rows.append(rf"\cot z\,({poly_tex(sp.cancel(_wl_poly(lhs) / _cc), A4_GENS)}) &= \kappa q_{{40}}")
    return aligned(rows)


def author_weights_q() -> sp.Expr:
    data = json.loads(A4_EQUATIONS.read_text("utf-8"))["exponentialHistory"]["authorWeights"]
    return sp.sympify(data["Q"]["input"].replace("^", "**"), locals=_A4_LOCALS)


def author_weights_q_block() -> str:
    inner = sp.expand(sp.cancel(author_weights_q() * 128 * _H / 3))
    if inner.free_symbols - {_AA, _be}:
        raise ValueError("Q(A, beta) of the author's weights is not 3/(128 H) times a polynomial in A, beta")
    return rf"Q(A, \beta) = \frac{{3}}{{128H}}\,\big({poly_tex(inner, (_AA, _be))}\big)"


def generated_blocks() -> dict[str, str]:
    blocks = {f"components_{i + 1}": block for i, block in enumerate(component_equation_blocks())}
    blocks.update(lovelock_blocks())
    blocks.update({"offdiagonal": offdiagonal_block(), "identity": identity_block(),
                   "einstein": einstein_block(), "author_weights_q": author_weights_q_block()})
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
    if key in ("algebra-wolfram", "theory-wolfram", "pairing-wolfram"):
        return data["summary"]["passed"], data["summary"]["total"]
    if key in ("algebra-python",):
        return data["summary"]["pass"], data["summary"]["checks"]
    if key == "theory-python":
        return data["summary"]["pass"], data["summary"]["checks"]
    if key == "a4-wolfram":
        return data["checkCount"] - data["failedCount"], data["checkCount"]
    if key == "a4-python":
        return data["passCount"], data["checkCount"]
    if key in ("pairing-python", "t3-python"):
        counts = data["counts"]
        return counts["pass"], counts["pass"] + counts["fail"] + counts["pending"]
    if key in ("scope-wolfram", "t3-wolfram"):
        return data["summary"]["passed"], data["summary"]["total"]
    if key in ("scope-python", "ks-source", "ks-source-a4", "ks-crosscheck", "fock-quartic"):
        return data["summary"]["pass"], data["summary"]["checks"]
    if key == "t3c-wolfram":
        return data["summary"]["passed"], data["summary"]["total"]
    if key == "t3c-python":
        counts = data["counts"]
        return counts["pass"], counts["pass"] + counts["fail"] + counts["pending"]
    if key.startswith("ds-"):
        return data["summary"]["pass"], data["summary"]["total"]
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
    "fock-quartic": "no Wolfram counterpart): {p} of {t} checks pass",
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
        for key, in_report, in_document in QUOTED_NUMBERS:
            with self.subTest(report=key, number=in_report):
                self.assertIn(in_report, REPORTS[key].read_text(encoding="utf-8"))
                self.assertIn(in_document, text)

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

    def test_component_equations_agree_with_the_sympy_report(self):
        sympy_components = load(REPORTS["theory-python"])["formulas"]["dirac_equation_components"]["components"]
        lam, m = sp.symbols("lam m")
        for number, wolfram in enumerate(wolfram_component_lhs(), 1):
            text = sympy_components[f"E{number}"]
            t = re.sub(r"psi(\d+)_x(\d)", r"D_\2_\1", text)
            t = re.sub(r"psi(\d+)", r"P_\1", t)
            t = re.sub(r"chi(\d+)", r"C_\1", t)
            t = t.replace("Derivative(b4(x4), x4)", "B1").replace("b4(x4)", "b4")
            t = t.replace("lambda", "lam").replace("6*H*x0", "z").replace("a4(x4)", "a4")
            expr = sp.sympify(t, locals={"lam": lam, "m": m, "a4": _a4, "z": _z, "H": _H, "b4": _b4,
                                          "B1": _B1, "exp": sp.exp, "sin": sp.sin, "cos": sp.cos,
                                          "sqrt": sp.sqrt})
            mass = sp.expand(expr).coeff(m)
            linear = sp.expand(expr).subs({lam: 0, m: 0})
            with self.subTest(component=number):
                self.assertEqual(mass, -sp.Symbol(f"P_{number}"))
                self.assertIn(_B1, linear.free_symbols)  # the b4 term is part of every component
                difference = sp.expand(linear - wolfram.subs(sp.tan(_z), sp.sin(_z) / sp.cos(_z)))
                self.assertEqual(sp.simplify(difference), 0)

    def test_connection_and_curvature_formulas_match_the_formula_file(self):
        """The hand-written formulas of sections 2 and 4 (metric with b4, u = b4'/b4, v = u')."""
        text = markdown_text()
        for formula in DOCUMENT_FORMULAS:
            with self.subTest(formula=formula):
                self.assertIn(formula, text)
        formulas = {item["key"]: item["wl"] for item in load(FIELD_THEORY)["formulas"]}
        s6 = sp.sin(_z) ** sp.Rational(1, 6)
        s3 = sp.sin(_z) ** sp.Rational(1, 3)
        e = sp.exp(_a4)
        u = _B1 / _b4                      # u = b4'/b4
        v = _B2 / _b4 - u**2               # v = u' = b4''/b4 - u^2
        rate = _A1 - u / 2                 # the time-direction rate of the extra times
        # vielbein and sqrt|g|
        # list position k + 1 holds x_k (the author's coordinates x0..x7; x0 the hidden direction, first)
        f = re.findall(r"[^{},]+(?:\[[^\]]*\][^{},]*)*", formulas["vielbein_diagonal"])
        expected_f = [sp.cot(_z)] + [e * s6] * 3 + [1] + [sp.sqrt(_b4) * s6 / e] * 3
        self.assertEqual(len(f), 8)
        for got, want in zip(f, expected_f):
            self.assertTrue(is_zero(wl_to_sympy(got) - want), got)
        self.assertTrue(is_zero(wl_to_sympy(formulas["sqrt_det_g"]) - _b4 ** sp.Rational(3, 2) * sp.cos(_z)))
        # Christoffel symbols: 25 nonzero, as written in section 2
        entries = re.findall(r"\{(\d), (\d), (\d), ([^{}]+)\}", formulas["christoffel_nonzero"])
        P = {k: k + 1 for k in range(8)}  # the list position of x_k
        expected = {}
        for i in (1, 2, 3):
            expected[(P[i], P[i], P[4])] = _A1
            expected[(P[i], P[0], P[i])] = _H * sp.cot(_z)
            expected[(P[4], P[i], P[i])] = sp.exp(2 * _a4) * s3 * _A1
            expected[(P[0], P[i], P[i])] = -sp.exp(2 * _a4) * _H * sp.sin(_z) ** sp.Rational(4, 3) / sp.cos(_z)
        for t in (5, 6, 7):
            expected[(P[t], P[4], P[t])] = -rate
            expected[(P[t], P[0], P[t])] = _H * sp.cot(_z)
            expected[(P[4], P[t], P[t])] = sp.exp(-2 * _a4) * _b4 * s3 * rate
            expected[(P[0], P[t], P[t])] = sp.exp(-2 * _a4) * _b4 * _H * sp.sin(_z) ** sp.Rational(4, 3) / sp.cos(_z)
        expected[(P[0], P[0], P[0])] = -6 * _H / (sp.sin(_z) * sp.cos(_z))
        got = {(int(a), int(b), int(c)): wl_to_sympy(v_) for a, b, c, v_ in entries}
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(christoffel=key):
                self.assertTrue(is_zero(value - expected[key]))
        # Ricci tensor (diagonal and the pair x4-x0) and scalar
        entries = re.findall(r"\{(\d), (\d), ([^{}]+)\}", formulas["ricci_mixed_nonzero"])
        expected = {(P[0], P[0]): -6 * _H**2,
                    (P[4], P[4]): 6 * _A1**2 - 3 * _A1 * u + sp.Rational(3, 4) * u**2 + sp.Rational(3, 2) * v,
                    (P[4], P[0]): sp.Rational(3, 2) * _H * u * sp.cot(_z),
                    (P[0], P[4]): -sp.Rational(3, 2) * _H * u * sp.tan(_z)}
        for i in (1, 2, 3):
            expected[(P[i], P[i])] = _A2 - 6 * _H**2 + sp.Rational(3, 2) * _A1 * u
        for t in (5, 6, 7):
            expected[(P[t], P[t])] = (-_A2 - 6 * _H**2 - sp.Rational(3, 2) * _A1 * u
                                      + sp.Rational(3, 4) * u**2 + v / 2)
        got = {(int(a), int(b)): wl_to_sympy(v_) for a, b, v_ in entries}
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(ricci=key):
                self.assertTrue(is_zero(value - expected[key]))
        self.assertTrue(is_zero(wl_to_sympy(formulas["ricci_scalar"])
                                - (6 * _A1**2 - 3 * _A1 * u + 3 * u**2 + 3 * v - 42 * _H**2)))
        # spin connection: 12 nonzero omega_mu,ab (a < b)
        entries = re.findall(r"\{(\d), (\d), (\d), ([^{}]+)\}", formulas["omega_nonzero"])
        # omega_mu,ab with a < b in the list positions: the pair (x0, x_i) is written (0)(i) = -(i)(0)
        expected = {}
        for i in (1, 2, 3):
            expected[(P[i], P[i], P[4])] = _A1 * e * s6
            expected[(P[i], P[0], P[i])] = -_H * e * s6
        for t in (5, 6, 7):
            expected[(P[t], P[4], P[t])] = -rate * sp.sqrt(_b4) * s6 / e
            expected[(P[t], P[0], P[t])] = _H * sp.sqrt(_b4) * s6 / e
        got = {(int(a), int(b), int(c)): wl_to_sympy(v_) for a, b, c, v_ in entries}
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(omega=key):
                self.assertTrue(is_zero(value - expected[key]))
        # gamma^mu Omega_mu per direction (list position): coefficients of gamma^(x4) and gamma^(x0)
        entries = re.findall(r"\{(\d), ([^{},]+), ([^{},]+)\}", formulas["gammaOmega_per_direction"])
        deflating = (-_A1 / 2 + u / 4, _H / 2)
        want = {P[0]: (0, 0), P[1]: (_A1 / 2, _H / 2), P[2]: (_A1 / 2, _H / 2), P[3]: (_A1 / 2, _H / 2),
                P[4]: (0, 0), P[5]: deflating, P[6]: deflating, P[7]: deflating}
        self.assertEqual(len(entries), 8)
        for mu, c4, c0 in entries:
            with self.subTest(direction=mu):
                self.assertTrue(is_zero(wl_to_sympy(c4) - want[int(mu)][0]))
                self.assertTrue(is_zero(wl_to_sympy(c0) - want[int(mu)][1]))
        total = formulas["gammaOmega_total"].replace('gamma["x0"]', "G0").replace('gamma["x4"]', "G4")
        g0, g4 = sp.symbols("G0 G4")
        total = sp.sympify(_wl_metric_symbols(total).replace("^", "**"),
                           locals={"G0": g0, "G4": g4, "H": _H, "b4": _b4, "B1": _B1})
        self.assertEqual(sp.simplify(total - (3 * _H * g0 + sp.Rational(3, 4) * u * g4)), 0)


class FieldEquationFormulasTest(unittest.TestCase):
    """The rendered parts of section 13 add up to the general formulas of a4-equations.json."""

    def setUp(self):
        self.data = load(A4_EQUATIONS)

    def general(self, key: str) -> sp.Expr:
        return _wl_poly(self.data["generalSource"][key]["input"].split("==")[0])

    def test_diagonal_equations_are_the_sums_of_the_rendered_components(self):
        for key, label in (("constraint_x4", "x4x4"), ("space_x1_eq_x2_eq_x3", "x1x1"),
                           ("extraTime_x5_eq_x6_eq_x7", "x5x5"), ("hidden_x0", "x0x0")):
            rendered = sum(a * lovelock_component(k, label) for k, a in zip((1, 2, 3), _alphas)) + _lam
            with self.subTest(component=key):
                self.assertEqual(sp.expand(rendered - self.general(key)), 0)

    def test_offdiagonal_factor_and_pair(self):
        rendered_q = sum(a * offdiagonal_factor(k) for k, a in zip((1, 2, 3), _alphas))
        self.assertEqual(sp.expand(rendered_q - _wl_poly(self.data["generalSource"]["offDiagonalFactor_Q"]["input"])), 0)
        self.assertEqual(sp.simplify(self.general("offDiagonal_x4x0") - _cc * _uu * rendered_q), 0)
        self.assertEqual(sp.simplify(self.general("offDiagonal_x0x4") + _uu * rendered_q / _cc), 0)
        for k in (1, 2, 3):
            with self.subTest(order=k):  # E^x0_x4 = -tan^2 z E^x4_x0
                self.assertEqual(sp.simplify(lovelock_component(k, "x0x4")
                                             + lovelock_component(k, "x4x0") / _cc**2), 0)

    def test_identity_is_the_sum_of_the_rendered_parts(self):
        lhs = self.general("identity_x1_plus_x5_minus_2x0")
        rendered = sum(a * identity_part(k) for k, a in zip((1, 2, 3), _alphas))
        self.assertEqual(sp.expand(rendered - lhs), 0)
        for k in (1, 2, 3):
            with self.subTest(order=k):  # every term contains u or v
                self.assertEqual(sp.expand(identity_part(k).subs({_uu: 0, _vv: 0})), 0)

    def test_background_history_with_the_author_weights(self):
        history = self.data["exponentialHistory"]
        source = history["requiredSource"]
        point = {_AA: 1, _be: sp.Rational(4, 3), _H: 1, _lam: -10, **AUTHOR_WEIGHTS}
        expected = {"rho": sp.Rational(-2, 27), "p3": sp.Rational(-2, 9), "pt": sp.Rational(-22, 27),
                    "p0": sp.Rational(-14, 27)}
        for key, value in expected.items():
            expr = sp.sympify(source[key]["input"].replace("^", "**"), locals=_A4_LOCALS) * _kappa
            with self.subTest(entry=key):
                self.assertEqual(sp.simplify(expr.subs(point)), value)
                # the required diagonal source of an exponential history is even in A
                self.assertEqual(sp.simplify(expr - expr.subs(_AA, -_AA)), 0)
        q40 = sp.sympify(source["q40"]["input"].replace("^", "**"), locals=_A4_LOCALS)
        self.assertEqual(sp.simplify(q40 + q40.subs(_AA, -_AA)), 0)  # odd in A
        self.assertEqual(sp.simplify(q40.subs(point)), 0)
        q = author_weights_q()
        self.assertEqual(sp.factor(q.subs(_AA, 1)), sp.factor(3 * _be * (3 * _be - 4) / (64 * _H)))
        self.assertEqual(sp.simplify(sp.sympify(history["authorWeights"]["Q"]["input"].replace("^", "**"),
                                                locals=_A4_LOCALS) - q), 0)
        self.assertIn(r"at $A = 1$, $Q = 3\beta(3\beta - 4)/(64H)$", markdown_text())


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
