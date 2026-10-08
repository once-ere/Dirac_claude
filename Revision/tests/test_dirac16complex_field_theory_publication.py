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
  * the 16 component field equations, the Lovelock components E_(k), F(a4'), the Einstein
    components and the linear-member formulas in the document are the output of the renderers
    below applied to Revision/theory/field-theory.json and
    Revision/field_equations_a4/a4-equations.json;
  * the 16 component equations agree with the independent sympy expressions of
    Revision/theory/reports/python-field-theory.json (formulas.dirac_equation_components);
  * the vielbein, sqrt|g|, the Christoffel symbols, the Ricci components, the spin connection and
    the per-direction contractions gamma^mu Omega_mu written in the document equal the entries of
    Revision/theory/field-theory.json.
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
            "operator, equations of state and the field equations for a4[x4] (Revision record)")

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
    "13. The field equations for a4[x4] with dirac16complex as the source",
    "14. Relation to the pairing theorems",
    "15. What this document does not claim",
    "16. Reproduction",
    "17. Index of formulas and checks",
]

# Code spans of the document that are not check names (formula keys, JSON keys, programs).
NON_CHECK_SPANS = {
    "_G", "grassmann_", "dirac16complex", "evolution_F", "field_equation",
    "field_equation_components", "christoffel_nonzero", "omega_nonzero",
    "gammaOmega_per_direction", "field_equation_blocks", "quantisation", "nontriviality",
    "majorana_negative_control", "exact_solutions", "EMT_diagonal", "EMT_kinetic_potential",
    "EMT_homogeneous_on_shell", "EMT_offdiagonal_x4_x8", "T_variation", "T_symmetric",
    "energy_exchange", "adjoint_equation", "equation_of_state_definitions",
    "hidden_direction_hermiticity", "lovelockTensors", "generalSource", "x8_dependence",
    "sourceRequiredByGivenA4", "einstein", "linearMember", "theoremLinear",
    "homogeneousSingleMode", "kohnSham", "emtConvention", "offDiagonalConditions",
    "einsteinConditions", "comparison_with_wolfram", "dirac_equation_components",
    "not_established", "wolframscript", "pdflatex", "wolfram_checks_without_sympy_counterpart",
}

ESSENTIAL_CHECKS = [
    "Pin44_irreducible_commutant_dim_1", "pin_commutant_dimension_1",
    "chiral_halves_inequivalent_intertwiners_0", "spin_halves_inequivalent",
    "vielbein_postulate", "Omega_components", "gammaOmega_equals_3H_gamma_x8",
    "gamma_mu_Omega_mu_equals_3H_gamma_x8", "gammaOmega_x4_terms_cancel",
    "time_terms_cancel_hidden_term_survives", "nontriviality_1_dirac16complex",
    "Omega_vanishes_iff_a4prime_and_H_vanish", "never_flat_for_H_positive",
    "spin_curvature_equals_Riemann", "L_real_G", "EL_Psibar_G", "EL_Psi_G",
    "grassmann_euler_lagrange_psibar_variation", "Dirac_operator_explicit_G",
    "Majorana_Lg_total_derivative_grassmann", "Lichnerowicz_identity_G",
    "Noether_identity_diffeomorphisms_G", "Noether_identity_local_Lorentz_G",
    "grassmann_emt_conservation_on_shell", "T_vielbein_variation_closed_form_G",
    "grassmann_homogeneous_on_shell_rho_p", "first_order_form_and_anticommutator",
    "no_positive_inner_product", "Fock_space_good_sector_example", "expectation_value_rule",
    "extra_time_modes_grow", "good_sector_hermiticity_curved", "evolution_factorises_a4pp_times_F",
    "boosted_frame_gammaOmega_vanishes", "boosted_frame_curvature_nonzero", "rescaling_removes_the_connection_term",
    "connection_free_lagrangian_same_equations", "good_sector_hermiticity_up_to_the_brane_flux",
    "good_sector_x8_independent_modes_without_boundary_condition", "extra_time_growth_rates_unbounded",
    "Q_one_particle_Krein_inertia_real_frequencies", "Q_one_particle_complex_and_zero_frequencies_Krein_neutral",
    "ks_profiles_violate_algebraic_condition", "ks_history_is_a_prescribed_background",
    "T3_energies_and_emt_profiles_equal",
    "algebraic_identity_x1_plus_x5_minus_2x8", "constraint_propagation_bianchi",
    "einstein_null_energy_x8", "linear_member_equal_pressures", "Q_Krein_metric_of_images",
    "A1_lovelock_identity_x1_plus_x5_equals_2x8", "B2_x8_conservation_on_every_profile",
    "C1_averaged_algebraic_condition_fails", "D4_constant_source_gives_linear_member",
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
    "the time-direction terms of the three inflating and the three deflating directions cancel",
    r"\gamma^\mu\Omega_\mu = 3H\gamma^{(8)}",
    "never flat for $H > 0$",
    "is a total derivative",
    "Theorem 2 (the canonical anticommutator forces a Krein structure)",
    "no positive inner product",
    "normal ordered",
    r"\hat T^\nu{}_\mu",
    "p_3 + p_t = 2p_8",
    "a_4 = AHx_4 + a_0",
    r"\sigma_T = +1",
    "no creation process",
    "is not claimed",
    "Numbers and formulas are taken only from",
    "belongs to the diagonal vielbein",
    "vanishes in no frame",
    "Krein-neutral",
    "not well posed in Hadamard's sense",
    "prescribed test-field background without back-reaction",
    "is a choice of sign",
    "the Kohn-Sham source does not start or select exponential deflation of the extra times",
    "That record establishes neither Hypothesis nor Hypothesis00.",
    "nothing computed comes near the Unite pair $(w_0, w_a) = (-0.861, -0.60)$",
    "`Revision/docs/KOHN_SHAM_DEFLATING_FIELD`",
    "`Revision/docs/LOVELOCK_GKD`",
    "`Revision/docs/DARK_SECTOR_HYPOTHESES`",
    "constructed and checked only for single good-sector momenta with frozen coefficients",
    "a positive-norm Hilbert space for the full field is not established",
    "the identity holds in this model if and only if the potential and the energy-momentum tensor are both Wick ordered",
    "Nothing is proved for the field on a whole slice",
    r"and in section 15 (the equation-of-state values $w_{\rm eff}$ of the Kohn-Sham gas",
]

# Numbers quoted from the second-wave reports: (report key, text in the report, text in the document).
QUOTED_NUMBERS = [
    ("ks-source-a4", "[0.414086 (N688_lamm2_a00), 0.806379] over the 70 nonzero states",
     "between 0.414086 and 0.806379 over the 70 nonzero states"),
    ("ks-source-a4", "a4'(2)/a4'(0) = 1.95362 (sigma0 = 10), 1.1321 (sigma0 = 1), 0.847549 (sigma0 = -1)",
     "$a_4'(2)/a_4'(0) = 1.95362$, 1.1321 and 0.847549"),
    ("ds-eos", "w_eff(C) in [-0.707107, -0.671895]", "between -0.707107 and -0.671895"),
]

PLACEHOLDERS = ["TODO", "TBD", "FIXME", "lorem ipsum", "PLACEHOLDER", "XXX"]

# Stale or unqualified statements corrected after review (2026-10-08): the documents named exist,
# the charge is only locally conserved, and nothing past the Lambda = 0 turning point is computed.
STALE_PHRASES = ["planned and not yet written", "the conserved charge", "re-inflate",
                 "for every series with 3-momentum"]

# Hand-written formulas of the document that are compared with field-theory.json below.
DOCUMENT_FORMULAS = [
    r"f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z,\quad f_4 = 1,\quad f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z,\quad f_8 = \cot z",
    r"\sqrt{|g|} = f_1 f_2\cdots f_8 = \sin z\cot z = \cos z",
    r"\Gamma^{x_i}{}_{x_i x_4} &= a_4', & \Gamma^{x_i}{}_{x_i x_8} &= H\cot z,",
    r"\Gamma^{x_t}{}_{x_4 x_t} &= -a_4', & \Gamma^{x_t}{}_{x_t x_8} &= H\cot z,",
    r"\Gamma^{x_4}{}_{x_i x_i} &= e^{2a_4}\sin^{1/3}z\,a_4', & \Gamma^{x_4}{}_{x_t x_t} &= e^{-2a_4}\sin^{1/3}z\,a_4',",
    r"\Gamma^{x_8}{}_{x_i x_i} &= -e^{2a_4}H\,\frac{\sin^{4/3}z}{\cos z}, & \Gamma^{x_8}{}_{x_t x_t} &= e^{-2a_4}H\,\frac{\sin^{4/3}z}{\cos z},",
    r"\Gamma^{x_8}{}_{x_8 x_8} &= -\frac{6H}{\sin z\cos z}",
    r"R^{x_i}{}_{x_i} = a_4'' - 6H^2,\quad R^{x_4}{}_{x_4} = 6(a_4')^2,\quad R^{x_t}{}_{x_t} = -a_4'' - 6H^2,\quad R^{x_8}{}_{x_8} = -6H^2",
    r"R = 6\big((a_4')^2 - 7H^2\big)",
    r"\omega_{x_i\,(i)(4)} &= a_4'\,e^{a_4}\sin^{1/6}z, & \omega_{x_i\,(i)(8)} &= H\,e^{a_4}\sin^{1/6}z,",
    r"\omega_{x_t\,(4)(t)} &= -a_4'\,e^{-a_4}\sin^{1/6}z, & \omega_{x_t\,(t)(8)} &= -H\,e^{-a_4}\sin^{1/6}z,",
    r"\gamma^{x_i}\Omega_{x_i} &= \tfrac12 a_4'\,\gamma^{(4)} + \tfrac12 H\,\gamma^{(8)} \qquad (i = 1, 2, 3),",
    r"\gamma^{x_t}\Omega_{x_t} &= -\tfrac12 a_4'\,\gamma^{(4)} + \tfrac12 H\,\gamma^{(8)} \qquad (t = 5, 6, 7),",
]


# ---------------------------------------------------------------------------------------------
# Renderers (they generate the document blocks; the tests compare the document with them)
# ---------------------------------------------------------------------------------------------

_a4, _z, _H = sp.symbols("a4 z H", real=True)
_A1, _A2 = sp.symbols("A1 A2", real=True)
EPS_S = sp.exp(-_a4) * sp.sin(_z) ** sp.Rational(-1, 6)   # 1/f for x1, x2, x3
EPS_T = sp.exp(_a4) * sp.sin(_z) ** sp.Rational(-1, 6)    # 1/f for x5, x6, x7


def wl_to_sympy(text: str) -> sp.Expr:
    """Parse a Wolfram InputForm expression of field-theory.json (no field symbols)."""
    t = text.replace("Derivative[1][a4][x4]", "A1").replace("Derivative[2][a4][x4]", "A2")
    t = t.replace("a4[x4]", "a4").replace("12*H*x8", "(2*z)").replace("6*H*x8", "z")
    for name in ("Sin", "Cos", "Tan", "Cot", "Sec", "Csc"):
        t = t.replace(name + "[", name.lower() + "(")
    t = t.replace("[", "(").replace("]", ")").replace("^", "**")
    local = {"E": sp.E, "a4": _a4, "z": _z, "H": _H, "A1": _A1, "A2": _A2,
             "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot, "sec": sp.sec, "csc": sp.csc}
    return sp.sympify(t, locals=local)


def is_zero(expr: sp.Expr) -> bool:
    expr = sp.simplify(sp.expand_trig(sp.sympify(expr).rewrite(sp.sin)))
    if expr == 0:
        return True
    # numeric confirmation at an exact rational point inside 0 < z < pi/2
    values = {_a4: sp.Rational(3, 7), _z: sp.Rational(5, 9), _H: sp.Rational(2, 3),
              _A1: sp.Rational(-4, 5), _A2: sp.Rational(7, 11)}
    return abs(sp.N(expr.subs(values), 50)) < sp.Float("1e-40")


def _parse_component(text: str) -> tuple[sp.Expr, int]:
    """Parse one Wolfram InputForm component equation 'lhs == V*Psi[A]'."""
    lhs, rhs = (part.strip() for part in text.split("=="))
    match = re.fullmatch(r"V\*Psi\[(\d+)\]", rhs)
    if match is None:
        raise ValueError(f"unexpected right-hand side {rhs!r}")
    t = re.sub(r'dd\["x(\d)",\s*Psi\[(\d+)\]\]', r"D_\1_\2", lhs)
    t = re.sub(r"Psi\[(\d+)\]", r"P_\1", t)
    t = t.replace("a4[x4]", "a4").replace("6*H*x8", "z")
    t = t.replace("Sin[z]", "sin(z)").replace("Tan[z]", "tan(z)").replace("Cos[z]", "cos(z)")
    t = t.replace("^", "**")
    if "[" in t or "]" in t:
        raise ValueError(f"unparsed Wolfram syntax in {t!r}")
    local = {"E": sp.E, "a4": _a4, "z": _z, "H": _H}
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
    """The 16 component field equations as LaTeX aligned rows, from field-theory.json."""
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
        mass_terms = [s for s in expr.free_symbols if s.name.startswith("P_")]
        if len(mass_terms) != 1 or sorted(derivative) != list(range(1, 9)):
            raise ValueError(f"unexpected structure of component {number}")
        p_symbol = mass_terms[0]
        rest = sp.expand(expr - sum(c * sp.Symbol(f"D_{k}_{b}") for k, (b, c) in derivative.items())
                         - expr.coeff(p_symbol) * p_symbol)
        if rest != 0:
            raise ValueError(f"unexpected remainder {rest} in component {number}")
        bases = {1: EPS_S, 2: EPS_S, 3: EPS_S, 4: sp.Integer(1), 5: EPS_T, 6: EPS_T, 7: EPS_T,
                 8: sp.tan(_z)}
        signs = {k: _sign(c, bases[k]) for k, (b, c) in derivative.items()}
        hidden_b = derivative[8][0]
        if int(p_symbol.name[2:]) != hidden_b or signs[8] != 1 or _sign(expr.coeff(p_symbol), 3 * _H) != 1:
            raise ValueError(f"the hidden-direction terms of component {number} are not (tan z d8 + 3H)")
        space = "".join(_signed(signs[k], rf"\partial_{k}\psi_{{{derivative[k][0]}}}", k == 1)
                        for k in (1, 2, 3))
        time = "".join(_signed(signs[k], rf"\partial_{k}\psi_{{{derivative[k][0]}}}", k == 5)
                       for k in (5, 6, 7))
        x4 = _signed(signs[4], rf"\partial_4\psi_{{{derivative[4][0]}}}", False)
        rows.append(rf"\epsilon_s({space}){x4} + \epsilon_t({time}) + (\tan z\,\partial_8 + 3H)"
                    rf"\psi_{{{hidden_b}}} &= V\psi_{{{number}}}")
    return rows


def aligned(rows: list[str]) -> str:
    return "\\begin{aligned}\n" + " \\\\\n".join(rows) + "\n\\end{aligned}"


def component_equation_blocks() -> list[str]:
    """Two aligned blocks: the equations of rows 1..8 (Gamma = -1) and of rows 9..16."""
    rows = component_equation_rows()
    return [aligned(rows[:8]), aligned(rows[8:])]


_ad1, _ad2, _AA = sp.symbols("ad1 ad2 AA", real=True)
_alphas = sp.symbols("alpha1 alpha2 alpha3", real=True)
_lam, _kappa = sp.symbols("Lam kappa", real=True)
_A4_LOCALS = {"ad1": _ad1, "ad2": _ad2, "H": _H, "AA": _AA, "alpha1": _alphas[0],
              "alpha2": _alphas[1], "alpha3": _alphas[2], "Lam": _lam, "kappa": _kappa}
MAX_TERMS_PER_ROW = 5


def _wl_poly(text: str) -> sp.Expr:
    return sp.expand(sp.sympify(text.replace("^", "**"), locals=_A4_LOCALS))


def _factor_tex(symbol: sp.Symbol, power: int) -> str:
    name = {"ad1": "a_4'", "ad2": "a_4''", "H": "H", "AA": "A"}[symbol.name]
    if power == 1:
        return name
    if symbol.name == "ad1":
        return f"(a_4')^{{{power}}}"
    if symbol.name == "ad2":
        return f"(a_4'')^{{{power}}}"
    return f"{name}^{{{power}}}"


def poly_terms(expr: sp.Expr, gens: tuple[sp.Symbol, ...]) -> list[tuple[int, str]]:
    """(sign, body) of the monomials of a polynomial with integer coefficients, in descending
    lexicographic order of the exponents of gens ((a_4')^4 before (a_4')^2 a_4'' before
    (a_4')^2 H^2)."""
    poly = sp.Poly(sp.expand(expr), *gens)
    terms = sorted(poly.terms(), key=lambda term: tuple(-e for e in term[0]))
    out = []
    for exponents, coefficient in terms:
        if not coefficient.is_Integer:
            raise ValueError(f"non-integer coefficient {coefficient}")
        factors = " ".join(_factor_tex(g, e) for g, e in zip(gens, exponents) if e)
        magnitude = abs(int(coefficient))
        if factors:
            body = factors if magnitude == 1 else f"{magnitude} {factors}"
        else:
            body = str(magnitude)
        out.append((-1 if coefficient < 0 else 1, body))
    return out


def poly_tex(expr: sp.Expr, gens: tuple[sp.Symbol, ...]) -> str:
    terms = poly_terms(expr, gens)
    return "".join(_signed(s, b, i == 0) for i, (s, b) in enumerate(terms)) if terms else "0"


def alpha_pieces(expr: sp.Expr, gens: tuple[sp.Symbol, ...]) -> list[tuple[int, str]]:
    """(sign, text) pieces alpha_k (polynomial) of an expression linear in alpha1..alpha3."""
    expr = sp.expand(expr)
    pieces = []
    for k, alpha in enumerate(_alphas, 1):
        coefficient = sp.expand(expr.coeff(alpha))
        if coefficient == 0:
            continue
        terms = poly_terms(coefficient, gens)
        if len(terms) == 1:
            sign, body = terms[0]
            text = rf"\alpha_{k}" if body == "1" else rf"{body}\,\alpha_{k}"
            pieces.append((sign, text))
        else:
            pieces.append((1, rf"\alpha_{k}\,({poly_tex(coefficient, gens)})"))
    remainder = sp.expand(expr - sum(a * expr.coeff(a) for a in _alphas))
    if remainder != 0:
        raise ValueError(f"expression not linear in the alphas: {remainder}")
    return pieces


def alpha_tex(expr: sp.Expr, gens: tuple[sp.Symbol, ...]) -> str:
    return "".join(_signed(s, t, i == 0) for i, (s, t) in enumerate(alpha_pieces(expr, gens)))


A4_COMPONENT_LABELS = {"x1x1": "x_1", "x4x4": "x_4", "x5x5": "x_5", "x8x8": "x_8"}


def lovelock_block() -> str:
    """The diagonal Lovelock components E_(k)^mu_mu (k = 1, 2, 3; mu = x1, x4, x5, x8)."""
    data = json.loads(A4_EQUATIONS.read_text("utf-8"))
    rows = []
    gens = (_ad1, _ad2, _H)
    for k in (1, 2, 3):
        for key, label in A4_COMPONENT_LABELS.items():
            terms = poly_terms(_wl_poly(data["lovelockTensors"][f"E{k}"][key]["input"]), gens)
            head = rf"E_{{({k})}}{{}}^{{{label}}}{{}}_{{{label}}} &= "
            first = terms[:4] if len(terms) > MAX_TERMS_PER_ROW else terms
            rows.append(head + "".join(_signed(s, b, i == 0) for i, (s, b) in enumerate(first)))
            if len(terms) > MAX_TERMS_PER_ROW:
                rows.append(r"&\quad" + "".join(_signed(s, b, False) for s, b in terms[4:]))
    return aligned(rows)


def evolution_f_block() -> str:
    data = json.loads(A4_EQUATIONS.read_text("utf-8"))
    expr = _wl_poly(data["generalSource"]["evolution_F"]["input"])
    return rf"F(a_4') = {alpha_tex(expr, (_ad1, _H))}"


def einstein_block() -> str:
    data = json.loads(A4_EQUATIONS.read_text("utf-8"))["einstein"]
    gens = (_ad1, _ad2, _H)
    rows = []
    for key, right in (("constraint_x4", r"-\kappa\rho"), ("space_x1", r"\kappa p_3"),
                       ("extraTime_x5", r"\kappa p_t"), ("hidden_x8", r"\kappa p_8")):
        lhs, _ = data[key]["input"].split("==")
        rows.append(rf"{poly_tex(_wl_poly(lhs) - _lam, gens)} + \Lambda &= {right}")
    return aligned(rows)


def linear_member_block() -> str:
    data = json.loads(A4_EQUATIONS.read_text("utf-8"))["linearMember"]
    gens = (_AA, _H)
    rows = []
    for key, label in (("rho", r"\kappa\rho"), ("p", r"\kappa p")):
        expr = sp.expand(_wl_poly(data[key]["input"]) * _kappa)
        lam_part = expr.coeff(_lam)
        if lam_part not in (1, -1):
            raise ValueError(f"Lambda coefficient {lam_part} in linearMember.{key}")
        pieces = alpha_pieces(sp.expand(expr - lam_part * _lam), gens)
        rows.append(rf"{label} &= " + "".join(_signed(s, t, i == 0) for i, (s, t) in enumerate(pieces[:2])))
        rows.append(r"&\quad" + "".join(_signed(s, t, False) for s, t in pieces[2:])
                    + _signed(int(lam_part), r"\Lambda", False))
    vacuum = _wl_poly(data["vacuumFactor"]["input"])
    rows.append(rf"\mathcal{{V}}(A) &= {alpha_tex(vacuum, gens)}")
    return aligned(rows)


def generated_blocks() -> dict[str, str]:
    blocks = {f"components_{i + 1}": block for i, block in enumerate(component_equation_blocks())}
    blocks.update({"lovelock": lovelock_block(), "evolution_F": evolution_f_block(),
                   "einstein": einstein_block(), "linear_member": linear_member_block()})
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
            or re.search(r"\.(json|md|py|wls|wl|tex|pdf|csv|rs|toml)$", span) is not None)


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
            t = t.replace("lambda", "lam").replace("6*H*x8", "z").replace("a4(x4)", "a4")
            expr = sp.sympify(t, locals={"lam": lam, "m": m, "a4": _a4, "z": _z, "H": _H,
                                          "exp": sp.exp, "sin": sp.sin, "cos": sp.cos})
            mass = sp.expand(expr).coeff(m)
            linear = sp.expand(expr).subs({lam: 0, m: 0})
            with self.subTest(component=number):
                self.assertEqual(mass, -sp.Symbol(f"P_{number}"))
                difference = sp.expand(linear - wolfram.subs(sp.tan(_z), sp.sin(_z) / sp.cos(_z)))
                self.assertEqual(sp.simplify(difference), 0)

    def test_connection_and_curvature_formulas_match_the_formula_file(self):
        text = markdown_text()
        for formula in DOCUMENT_FORMULAS:
            with self.subTest(formula=formula):
                self.assertIn(formula, text)
        formulas = {item["key"]: item["wl"] for item in load(FIELD_THEORY)["formulas"]}
        s6 = sp.sin(_z) ** sp.Rational(1, 6)
        e = sp.exp(_a4)
        # vielbein and sqrt|g|
        f = re.findall(r"[^{},]+", formulas["vielbein_diagonal"])
        expected_f = [e * s6] * 3 + [1] + [s6 / e] * 3 + [sp.cot(_z)]
        self.assertEqual(len(f), 8)
        for got, want in zip(f, expected_f):
            self.assertTrue(is_zero(wl_to_sympy(got) - want))
        self.assertTrue(is_zero(wl_to_sympy(formulas["sqrt_det_g"]) - sp.cos(_z)))
        # Christoffel symbols: 25 nonzero, as written in section 2
        entries = re.findall(r"\{(\d), (\d), (\d), ([^{}]+)\}", formulas["christoffel_nonzero"])
        expected = {}
        for i in (1, 2, 3):
            expected[(i, i, 4)] = _A1
            expected[(i, i, 8)] = _H * sp.cot(_z)
            expected[(4, i, i)] = sp.exp(2 * _a4) * sp.sin(_z) ** sp.Rational(1, 3) * _A1
            expected[(8, i, i)] = -sp.exp(2 * _a4) * _H * sp.sin(_z) ** sp.Rational(4, 3) / sp.cos(_z)
        for t in (5, 6, 7):
            expected[(t, 4, t)] = -_A1
            expected[(t, t, 8)] = _H * sp.cot(_z)
            expected[(4, t, t)] = sp.exp(-2 * _a4) * sp.sin(_z) ** sp.Rational(1, 3) * _A1
            expected[(8, t, t)] = sp.exp(-2 * _a4) * _H * sp.sin(_z) ** sp.Rational(4, 3) / sp.cos(_z)
        expected[(8, 8, 8)] = -6 * _H / (sp.sin(_z) * sp.cos(_z))
        got = {(int(a), int(b), int(c)): wl_to_sympy(v) for a, b, c, v in entries}
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(christoffel=key):
                self.assertTrue(is_zero(value - expected[key]))
        # Ricci components and scalar
        ricci = [wl_to_sympy(x) for x in re.findall(r"[^{},]+", formulas["ricci_mixed_diagonal"])]
        want = [_A2 - 6 * _H**2] * 3 + [6 * _A1**2] + [-_A2 - 6 * _H**2] * 3 + [-6 * _H**2]
        for got_r, want_r in zip(ricci, want):
            self.assertTrue(is_zero(got_r - want_r))
        self.assertTrue(is_zero(wl_to_sympy(formulas["ricci_scalar"]) - 6 * (_A1**2 - 7 * _H**2)))
        # spin connection: 12 nonzero omega_mu,ab (a < b)
        entries = re.findall(r"\{(\d), (\d), (\d), ([^{}]+)\}", formulas["omega_nonzero"])
        expected = {}
        for i in (1, 2, 3):
            expected[(i, i, 4)] = _A1 * e * s6
            expected[(i, i, 8)] = _H * e * s6
        for t in (5, 6, 7):
            expected[(t, 4, t)] = -_A1 * s6 / e
            expected[(t, t, 8)] = -_H * s6 / e
        got = {(int(a), int(b), int(c)): wl_to_sympy(v) for a, b, c, v in entries}
        self.assertEqual(set(got), set(expected))
        for key, value in got.items():
            with self.subTest(omega=key):
                self.assertTrue(is_zero(value - expected[key]))
        # gamma^mu Omega_mu per direction: coefficients of gamma^(x4) and gamma^(x8)
        entries = re.findall(r"\{(\d), ([^{},]+), ([^{},]+)\}", formulas["gammaOmega_per_direction"])
        want = {1: (_A1 / 2, _H / 2), 2: (_A1 / 2, _H / 2), 3: (_A1 / 2, _H / 2), 4: (0, 0),
                5: (-_A1 / 2, _H / 2), 6: (-_A1 / 2, _H / 2), 7: (-_A1 / 2, _H / 2), 8: (0, 0)}
        self.assertEqual(len(entries), 8)
        for mu, c4, c8 in entries:
            with self.subTest(direction=mu):
                self.assertTrue(is_zero(wl_to_sympy(c4) - want[int(mu)][0]))
                self.assertTrue(is_zero(wl_to_sympy(c8) - want[int(mu)][1]))
        self.assertEqual(formulas["gammaOmega_total"].replace(" ", ""), '3*H*gamma["x8"]')


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
