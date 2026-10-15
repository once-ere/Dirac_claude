"""12a builder: the Rust Lovelock record (Revision/gkd_lovelock/results/lovelock-tensors.json)
was recomputed for the metric with b4 (13 exponents per monomial since 2026-10-14). This
notebook works at b4 = 1, so the record is evaluated at b4 = 1 before the comparison."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/12a_a4_field_equations.py"
s = p.read_text(encoding="utf-8")
pairs = [
    ('''        text = lovelock_json[f"L{k}"].replace("Derivative[1][a4][x4]", "ad1")''',
     '''        text = lovelock_json[f"L{k}"].replace("Derivative[1][a4][x4]", "ad1")
        for b4_text, value in (("Derivative[2][b4][x4]", "0"),
                               ("Derivative[1][b4][x4]", "0"), ("b4[x4]", "1")):
            text = text.replace(b4_text, value)  # the record at b4 = 1'''),
    (r"""    The Rust program `lovelock_gkd` of the GKD record stored every component of
    $P_{(k)}{}^h{}_j$ as a list of monomials: a fraction and the exponents of $H$,
    $a_4', a_4'', a_4''', a_4''''$, $e^{a_4}$, $\sin^{1/3} z$ and $\cot z$.""",
     r"""    The Rust program `lovelock_gkd` of the GKD record stored every component of
    $P_{(k)}{}^h{}_j$ as a list of monomials: a fraction and the 13 exponents of $H$,
    $a_4', a_4'', a_4''', a_4''''$, $e^{a_4}$, $\sin^{1/3} z$, $\cot z$, $b_4^{1/2}$ and
    $b_4', b_4'', b_4''', b_4''''$. The program computes the author's metric with the
    second function $b_4(x_4)$ of 2026-10-14; this notebook works at $b_4 = 1$, so
    `from_monomials` keeps only the monomials without a derivative of $b_4$ (the others
    vanish at $b_4 = 1$) and sets $b_4^{1/2} = 1$. The same is done with the scalars
    $L_{(k)}$ in the cell before (`b4[x4]` becomes 1, its derivatives 0)."""),
    ('''        for numerator, denominator, exponents in monomials:
            term = sp.Rational(numerator, denominator)
            for symbol, power in zip(symbols_of_monomial, exponents):''',
     '''        for numerator, denominator, exponents in monomials:
            if any(exponents[9:13]):  # a derivative of b4: zero at b4 = 1
                continue
            term = sp.Rational(numerator, denominator)  # b4^(1/2) = 1 (exponent 8)
            for symbol, power in zip(symbols_of_monomial, exponents[:8]):'''),
]
s = strict_replace(s, pairs, "12a_b4")
p.write_bytes(s.encode("utf-8"))
print("ok")
