"""Renderers of the generated blocks of DIRAC16COMPLEX_FIELD_THEORY.md for the corrected metric (version 2).

This module is the draft of the renderer part of Revision/tests/test_dirac16complex_field_theory_publication.py; the
test contains the same functions. Run it to print the blocks (python d16_renderers.py).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import sympy as sp

REVISION = Path(r"D:\Developer\github\Dirac_claude\Revision")
FIELD_THEORY = REVISION / "theory" / "field-theory.json"
A4_EQUATIONS = REVISION / "field_equations_a4" / "a4-equations.json"

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


def component_equation_rows() -> list[str]:
    """The 16 component field equations as LaTeX aligned rows, from field-theory.json.

    Every component has the derivative terms of the eight directions, the hidden-block term c_g psi_B with the same
    psi_B as the hidden-direction derivative, and the term v_g psi_C with the same psi_C and the same sign as d4: it is
    written with hat-d4 = d4 + v_g and epsilon_0 (tan z d0 + (3/2) H)."""
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


if __name__ == "__main__":
    for name, block in generated_blocks().items():
        print(f"% {name}")
        print(block)
