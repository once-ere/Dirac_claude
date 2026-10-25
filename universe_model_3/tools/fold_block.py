#!/usr/bin/env python3
"""fold_block.py - put the one definition of the fold, with its examples, into every UM-3 file that uses the word, and
check that every such file carries it word for word.

BEGIN FOLD DEFINITION
THE FOLD (the definition used in every UM-3 file)

Definition. The fold is the seven-dimensional surface of the author's eight-dimensional spacetime on which the cosine of
the angle z = 6 H x0 of the hidden direction vanishes:
    (FD-1)  F = { X = (x0, x1, ..., x7) : cos(6 H x0) = 0 };  in one period 0 < z < pi of the metric: z = pi/2, x0 = pi/(12 H).
X = {x0, ..., x7} are the author's coordinates: x0 the hidden space-like direction, x1, x2, x3 ordinary space, x4 the
time, x5, x6, x7 the three extra times; H is the author's constant (an inverse length). The author's metric depends on x0
only through cot(z)^2 and (sin(z)^2)^(1/6), so it repeats with the period pi/(6 H) of x0, and every period 0 < z < pi
contains exactly one surface of F, at z = pi/2: F is the union of these copies, one per period (example 2), and "the
fold" without a qualifier is the copy in the period that contains our world. A point of the fold is labelled by the seven
coordinates x1, ..., x7, and the metric restricted to the fold (dx0 = 0, z = pi/2) is
    (FD-2)  ds^2 on F = e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2),
with three space-like and four time-like directions; a4 and b4 are the author's two functions of the time x4.
Notation: ln is the natural logarithm, e Euler's number, exp(y) = e^y, sin, cos and cot = cos/sin the trigonometric
functions, tanh the hyperbolic tangent, |y| the absolute value; f(0+) and f(0-) are the limits of f(sigma) as sigma
approaches 0 from above and from below.

Why this surface is called a fold. Measured by the proper distance along the hidden direction,
    (FD-3)  sigma = sgn(pi/2 - z) ln(sin z)/(6 H),   d sigma = |cot z| dx0,   sin z = e^(-6 H |sigma|)
(the fold is sigma = 0; the half-period 0 < z < pi/2 is sigma < 0, the half-period pi/2 < z < pi is sigma > 0; the two ends
of the period, the tips z -> 0 and z -> pi, lie at sigma -> -infinity and sigma -> +infinity), the author's metric is
    (FD-4)  ds^2 = d sigma^2 + e^(-2 H |sigma|) [ e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2) ] - dx4^2.
It depends on sigma only through |sigma|. The function W(sigma) = e^(-2 H |sigma|), which multiplies the squared steps of
ordinary space and of the extra times, is the warp factor of the metric (its square root e^(-H |sigma|) multiplies the
lengths); the time x4 is not warped. Four properties make the surface sigma = 0 a fold, and together they single it out
within the period:
  1. It is a mirror. The reflection sigma -> -sigma (that is z -> pi - z, or x0 -> pi/(6 H) - x0) maps the metric to
     itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
     period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are
     joined along the crease.
  2. The warp factor is largest on it. The warp factor (sin(z)^2)^(1/6) = e^(-2 H |sigma|) equals 1 on the fold and
     decreases on both sides.
  3. The metric has a kink on it. The metric is continuous across the fold, but its first derivative along sigma jumps.
     The extrinsic curvature of the surfaces sigma = const changes sign across the fold,
        (FD-5)  K^a_b = (1/2) g^ac d_sigma g_cb:  K^1_1 = K^2_2 = K^3_3 = K^5_5 = K^6_6 = K^7_7 = -H sgn(sigma),  K^4_4 = 0
     (g_ab the metric components along the fold, g^ab their inverse, d_sigma the derivative with respect to sigma, sgn the
     sign function, a, b frame indices along the fold); it jumps by -2 H along ordinary space and along the extra times.
     The Einstein-Lovelock equations of UM-3, sum_p alpha_(p) E_(p)^a_b + Lambda delta^a_b = kappa T^a_b (E_(p) the
     Lovelock tensor of order p = 1, 2, 3, alpha_(p) = w_(p) H^(2-2p) its coupling with the weights w = (1, 1/20, 1/360),
     Lambda = -7 H^2 the cosmological constant, kappa = 8 pi G_8 the gravitational coupling of eight dimensions, T^a_b the
     energy-momentum tensor, delta^a_b the Kronecker delta), are linear in the second sigma-derivatives of the metric, so
     the jump puts a Dirac delta function delta_D(sigma) into them: the metric solves them only if the fold carries a thin
     source S^a_b, an energy-momentum tensor concentrated on sigma = 0, given by the integral of the equations across the
     fold (the junction conditions),
        (FD-11) kappa S^a_b = integral from sigma = 0- to 0+ of d sigma sum_p alpha_(p) E_(p)^a_b,
     with S^4_4 = -(its energy density), S^1_1 = S^2_2 = S^3_3 its pressure along ordinary space and S^5_5 = S^6_6 = S^7_7
     its pressure along the extra times; S is T integrated across the fold, an energy per unit volume of the six other
     directions of the fold (unit GeV^7). On the static block (a4 and b4 constant) and on an expanding fold whose extra
     times are frozen (b4 proportional to e^(a4), A = a4'/H, A1 = a4''/H^2)
        (FD-12) static block:      kappa S^a_b = -(32/5) H delta^a_b  (a pure tension),
                frozen extra times: kappa S^1_1 = -(16/15)(6 + 3 A^2 + 2 A1) H,  kappa S^4_4 = -(16/5)(2 + A^2) H,
                                    kappa S^5_5 = -(4/5)(8 + 8 A^2 + A^4 + 4 A1 + A^2 A1) H:
     the tension plus matter that obeys the Friedmann equations of general relativity. The fold is therefore not only a
     place but a physical object: a thin layer that carries energy and momentum (a brane).
  4. The author's coordinate x0 degenerates on it. The metric component g_x0x0 = cot(6 H x0)^2 vanishes on the fold and
     nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,
        (FD-6)  |sigma| = 3 H (x0 - pi/(12 H))^2 [1 + 6 H^2 (x0 - pi/(12 H))^2 + ...],
     so the two coordinate values on either side of x0 = pi/(12 H) at the same coordinate distance lie at the same proper
     distance from the fold: the coordinate line of x0 is folded onto the line of proper distances (a fold map, example 5).

What lives on the fold. In UM-3 the Standard Model (the Higgs doublet with the author's ad hoc vacuum, a time-dependent
choice of its vacuum value; the gauge fields of SU(3)_C x SU(2)_L x U(1)_Y; three generations of quarks and leptons and
three right-handed neutrinos) and the fold fluid (its tension and the pressure along the extra times that keeps their
volume fixed) live on the fold: they are fields at sigma = 0, functions of x1, ..., x4 (no field depends on the extra
times). Integrated over the extra times, the fold is the four-dimensional universe that we observe, with the metric
diag(e^(2 a4), e^(2 a4), e^(2 a4), -1) in x1, ..., x4. dirac16complex (the author's spinor field of eight dimensions) and
gravity live in the bulk sigma != 0 as well as on the fold; the bound states chi of dirac16complex are the part of it that
the fold holds, and the portals (couplings between dirac16complex and Standard-Model fields) act at sigma = 0. In UM-3
files "the fold" means this surface; the examples below use the word for other surfaces with the same properties. The
word is not used in its other senses: a set of equal energy levels is called degenerate, and a growth by the factor e is
called an e-folding.

Examples of folds that are meaningful for UM-3.
  1. Our fold. The fold z = pi/2 of the period that contains our world (FD-1): the seven-dimensional world-volume of the
     Standard Model, and after the integration over the extra times the four-dimensional universe that we observe.
  2. The copies of the fold. Because the metric repeats with the period pi/(6 H), every surface
     x0 = pi/(12 H) + (an integer multiple of pi/(6 H)) is a copy of the fold, one per period. Neighbouring copies are
     separated by a tip (z a multiple of pi), where the warp factor (sin(z)^2)^(1/6) vanishes and g_x0x0 = cot(z)^2
     diverges, and which lies at an infinite proper distance from both: in proper distance every copy has its own complete
     line -infinity < sigma < infinity. A compact direction of length L would give every field a tower of particles with
     the masses 2 pi n/L, n = 1, 2, ... (a Kaluza-Klein tower); because the copies are infinitely far apart, the period
     pi/(6 H) of x0 produces no such tower with the spacing 12 H, and the x0 mass of the bound states is their binding to
     the fold.
  3. A folded sheet of paper. The crease of a folded sheet is a fold in this sense: the two halves are mirror images
     (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
     In UM-3 the direction across the crease is the hidden direction sigma, the seven directions along the crease are
     x1, ..., x7, and the crease is the fold.
  4. A folded function. The warp factor e^(-2 H |sigma|) is the simplest folded function: continuous, mirror symmetric,
     largest at sigma = 0, with a jump of its derivative,
        (FD-7)  d/d sigma e^(-2 H |sigma|) = -2 H sgn(sigma) e^(-2 H |sigma|),
                d^2/d sigma^2 e^(-2 H |sigma|) = 4 H^2 e^(-2 H |sigma|) - 4 H delta_D(sigma),
     whose delta function is the origin of the thin source of property 3. Every metric function of FD-4 depends on sigma
     through |sigma| and is folded at sigma = 0 in this sense.
  5. A fold map. In the mathematics of smooth maps the fold (Whitney's fold singularity) is the map u -> u^2 of a line onto
     a half-line: it folds the line at u = 0, two points +u and -u land on the same point, and the derivative of the map
     vanishes on the fold. Near the fold the map from the author's coordinate x0 to the distance |sigma| from the fold is
     of this kind (FD-6), and g_x0x0 = cot(z)^2, the square of the derivative d sigma/d x0, vanishes there.
  6. The brane of Randall and Sundrum. The five-dimensional metric
        (FD-8)  dy_RS^2 + e^(-2 k_RS |y_RS|) (dx1^2 + dx2^2 + dx3^2 - dx4^2),
                lambda_RS = 6 k_RS/kappa_5,   Lambda_RS = -6 k_RS^2/kappa_5
     (y_RS the proper coordinate across the brane, k_RS the inverse curvature length of the bulk, kappa_5 = 8 pi G_5) has a
     fold at y_RS = 0 with the properties 1 to 3 (its coordinate y_RS is already the proper distance, so property 4 does
     not arise); Einstein's equations require there a brane of the tension lambda_RS (Israel's junction condition) and in
     the bulk the vacuum energy Lambda_RS, and the bulk is otherwise empty. The fold of UM-3 is of the same kind: its static
     block is a vacuum of the bulk with a fold of pure tension (FD-12). It differs in that the time x4 is not warped,
     three extra times are warped together with ordinary space, the Lovelock terms add to the junction conditions, and
     the space is not cut at the brane: Randall and Sundrum identify the two sides of their brane (one physical side),
     while the fold of UM-3 has two distinct sides (example 7).
  7. A particle bound to a thin layer. A particle held by an attractive thin layer has a wave function that falls off
     exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order Dirac
     equation, the wave function itself). In UM-3 the particles chi of dark matter are the states of dirac16complex bound
     to the fold; at rest and without their self-interaction (the field is Psi = e^(3 H |sigma|) chi(sigma) e^(-i omega_b x4))
        (FD-9)  chi(sigma) = e^(-q_b |sigma|) chi(0+) (sigma > 0),   chi(sigma) = e^(-q_b |sigma|) chi(0-) (sigma < 0),
                chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-),   omega_b = sqrt(m_Psi^2 - q_b^2),
     where mu_L, mu_R are the strengths of the fold for the left- and right-handed halves of dirac16complex (set by the
     Standard-Model fields on the fold), gamma^(0) = T^0 the Dirac matrix along sigma, P_L, P_R the chiral projectors,
     m_Psi the bulk mass, and q_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), s = sqrt(mu_L mu_R) (q_b = -m_Psi mu_L/2 for
     mu_R = 0). The profile is not a function of |sigma|: it jumps at the fold, chi(0+) != chi(0-).
  8. The fold as a mirror for dirac16complex. The reflection across the fold acts on the profiles chi(sigma) in two ways,
        (FD-10)  (R_1 chi)(sigma) = T_0 T_1 T_2 T_3 chi(-sigma),   (R_2 chi)(sigma) = T_0 T_5 T_6 T_7 chi(-sigma)
     (T_a the author's Dirac matrices; for states at rest R_1 is the reflection across the fold combined with the
     reflection of ordinary space, R_2 the reflection across the fold combined with the reflection of the extra times).
     The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a state can
     carry the charge -1 or +1. R_1 is a symmetry of dirac16complex, of gravity and of the mean field of a gas of the
     particles chi (the average field that the particles of the gas create and feel): the four bound states of Krein
     charge -1 (the particles chi) are even under it and the four of Krein charge +1 are odd, so the mean field of the gas
     cannot mix the two signs of the indefinite charge. R_2 maps the bound states of one Krein charge onto those of the
     other and makes the two sets degenerate without the self-interaction.
  9. The planes of Horava and Witten. In M-theory (the eleven-dimensional theory whose limits include the superstring
     theories) on an interval (a circle whose points are identified with their mirror images), the two ten-dimensional
     planes left in place by the reflection are mirror surfaces (property 1); each carries one E8 gauge group while gravity
     fills the bulk. As in UM-3, the gauge fields live on the mirror surface and gravity in the bulk; unlike UM-3, the two
     sides of each plane are identified (one physical side).

What is not a fold.
  * The tips z = 0 and z = pi (mod pi): the mirror exchanges them within a period, but there the warp factor vanishes,
    g_x0x0 diverges, and they lie at an infinite proper distance; they carry no thin source.
  * A smooth maximum of a warp factor, such as 1/cosh(H sigma)^2: mirror symmetric and largest at sigma = 0, but without a
    kink and without a thin source.
END FOLD DEFINITION

The two versions of the definition:
  docs_src/fold_definition.md   Markdown with LaTeX (FD-1 to FD-10, each display followed by its symbol list, generated
                                from the registry): the documents MODEL, FIELD_EQUATIONS, SOLUTION, ANALYSIS, PROVENANCE
                                (and so their .tex and .pdf), universe_model_3/README.md and the repository files
                                README.md, HANDOFF.md and claude_failures.md, between the lines
                                <!-- begin fold definition --> and <!-- end fold definition -->;
  docs_src/fold_definition.txt  plain text, the same definition and examples: the docstring of every Python file of
                                universe_model_3 that uses the word (between the lines BEGIN FOLD DEFINITION and
                                END FOLD DEFINITION, as above), and from there the field "definition_of_the_fold" of every
                                JSON file that such a module writes.
Not touched: the author's notebooks (author_inputs/4+4.nb uses Mathematica's function Fold, not this word) and the
git-ignored external data.

Usage (repository root):
    python universe_model_3/tools/fold_block.py insert   # write the blocks (then the symbol lists are expanded)
    python universe_model_3/tools/fold_block.py check    # exit 1 unless every file that uses the word carries the block
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
ROOT = UM3.parent
sys.path.insert(0, str(HERE))
import symbols_tool as ST  # noqa: E402

MD_SRC = UM3 / 'docs_src' / 'fold_definition.md'
TXT_SRC = UM3 / 'docs_src' / 'fold_definition.txt'
MD_BEGIN, MD_END = '<!-- begin fold definition -->', '<!-- end fold definition -->'
PY_BEGIN, PY_END = 'BEGIN FOLD DEFINITION', 'END FOLD DEFINITION'
DOCS = ['MODEL', 'FIELD_EQUATIONS', 'SOLUTION', 'ANALYSIS', 'PROVENANCE', 'STABILISER']
MD_FILES = [UM3 / (n + '.md') for n in DOCS] + [UM3 / 'README.md', ROOT / 'README.md', ROOT / 'HANDOFF.md',
                                                ROOT / 'claude_failures.md']
EXCLUDED = {'universe_model_3/author_inputs/4+4.nb'}
WORD = re.compile(r'(?<![A-Za-z])folds?(?![A-Za-z])', re.IGNORECASE)


def txt_block():
    return TXT_SRC.read_text(encoding='utf-8').rstrip('\n')


def md_block_raw():
    return MD_SRC.read_text(encoding='utf-8').rstrip('\n')


def region(text, begin, end):
    a = text.find(begin)
    b = text.find(end)
    if a < 0 or b < 0 or b < a:
        return None
    return text[a + len(begin):b]


def insert_md(path, block):
    text = path.read_text(encoding='utf-8')
    if MD_BEGIN not in text:
        raise SystemExit('%s has no line %s: place the markers first' % (path, MD_BEGIN))
    a = text.index(MD_BEGIN) + len(MD_BEGIN)
    b = text.index(MD_END)
    new = text[:a] + '\n' + block + '\n' + text[b:]
    if new != text:
        path.write_text(new, encoding='utf-8')


def insert_py(path, block):
    text = path.read_text(encoding='utf-8')
    if PY_BEGIN not in text:
        raise SystemExit('%s has no line %s in its docstring: place the markers first' % (path, PY_BEGIN))
    a = text.index(PY_BEGIN) + len(PY_BEGIN)
    b = text.index(PY_END)
    new = text[:a] + '\n' + block + '\n' + text[b:]
    if new != text:
        path.write_text(new, encoding='utf-8')


def tracked_and_new(base):
    """The files of base (tracked or new, not ignored), as paths relative to the repository root."""
    out = subprocess.run(['git', 'ls-files', '--cached', '--others', '--exclude-standard', base], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout.split('\n')
    return [x for x in out if x and (ROOT / x).is_file()]


def uses_word(rel):
    p = ROOT / rel
    try:
        text = p.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        return False
    return bool(WORD.search(text))


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('insert', 'check'):
        print(__doc__)
        return 2
    txt = txt_block()
    if sys.argv[1] == 'insert':
        raw = md_block_raw()
        for p in MD_FILES:
            insert_md(p, raw)
        reg, owner, problems = ST.load_registry()
        for p in MD_FILES:
            problems += ST.expand(str(p), reg)
        for rel in tracked_and_new('universe_model_3'):
            if rel.endswith('.py') and uses_word(rel):
                insert_py(ROOT / rel, txt)
        for x in problems:
            print('problem:', x)
        return 1 if problems else 0
    # check
    problems = []
    ref = region(UM3.joinpath('FIELD_EQUATIONS.md').read_text(encoding='utf-8'), MD_BEGIN, MD_END)
    if ref is None:
        problems.append('FIELD_EQUATIONS.md carries no definition of the fold')
    else:
        # the reference block is the source with its generated symbol lists
        body = ref.strip('\n')
        stripped = re.sub(r'\n<!-- begin generated symbol list -->.*?<!-- end generated symbol list -->', '', body,
                          flags=re.DOTALL)
        if stripped.strip() != md_block_raw().strip():
            problems.append('the block in FIELD_EQUATIONS.md differs from docs_src/fold_definition.md')
    n_md = n_py = n_json = 0
    for p in MD_FILES:
        r = region(p.read_text(encoding='utf-8'), MD_BEGIN, MD_END)
        if r is None or ref is None or r != ref:
            problems.append('%s: the definition of the fold is missing or differs' % p.relative_to(ROOT))
        n_md += 1
    md_set = {str(p.relative_to(ROOT)) for p in MD_FILES}
    files = tracked_and_new('universe_model_3') + [x for x in ('README.md', 'HANDOFF.md', 'claude_failures.md')]
    for rel in files:
        if rel in EXCLUDED or not uses_word(rel):
            continue
        p = ROOT / rel
        text = p.read_text(encoding='utf-8')
        if rel in md_set:
            continue
        if rel.endswith('.py'):
            r = region(text, PY_BEGIN, PY_END)
            if r is None or r.strip('\n') != txt:
                problems.append('%s: the docstring lacks the definition of the fold' % rel)
            n_py += 1
        elif rel.endswith('.json'):
            try:
                data = json.loads(text)
            except json.JSONDecodeError:
                problems.append('%s: not JSON' % rel)
                continue
            if isinstance(data, dict):
                val = data.get('definition_of_the_fold', data.get('_definition_of_the_fold', {}))
                if isinstance(val, dict):
                    val = val.get('text')
            elif isinstance(data, list):
                val = next((e.get('text') for e in data if isinstance(e, dict) and e.get('id') == '_definition_of_the_fold'),
                           None)
            else:
                val = None
            if val != txt:
                problems.append('%s: the field definition_of_the_fold is missing or differs' % rel)
            n_json += 1
        elif rel.endswith(('.md', '.tex', '.pdf', '.txt')):
            if rel.endswith('.tex') and rel[:-4] + '.md' in md_set:
                # built from its Markdown source; the block must be there as well
                if 'Definition.' not in text or 'What is not a fold' not in text:
                    problems.append('%s: the definition of the fold is missing (rebuild from the .md)' % rel)
                continue
            if rel.endswith('fold_definition.md') or rel.endswith('fold_definition.txt'):
                continue
            problems.append('%s uses the word fold but carries no definition' % rel)
        else:
            problems.append('%s uses the word fold but carries no definition' % rel)
    for x in problems:
        print('problem:', x)
    print('fold_check=%s (%d Markdown files, %d Python files, %d JSON files; %d problems)'
          % ('OK' if not problems else 'FAILED', n_md, n_py, n_json, len(problems)))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
