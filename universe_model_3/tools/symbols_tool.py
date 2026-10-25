#!/usr/bin/env python3
r"""The symbol lists of the UM-3 documents: every display equation is followed by the complete list of the
symbols that appear in it, generated from one registry, and a check that no symbol of an equation is left undefined.

Registry: the JSON files universe_model_3/docs_src/symbols/*.json, each a JSON object  key -> entry  (keys unique over
all files) with
    "tex":     how the symbol is printed in the list (LaTeX without dollars), e.g. "g_{MN}"
    "atoms":   the atoms of an equation that this entry defines (see below), e.g. ["g"]
    "meaning": one or more plain sentences: what the symbol is (and, for a derived quantity, its defining formula)
    "units":   its unit or dimension (e.g. "GeV", "1/length", "dimensionless"); "" if not applicable (operators, indices)
    "value":   optional: its numerical value or the place in the same document where it is computed
    "status":  optional: AUTHOR, RECORD, STANDARD, ASSUMED, INVENTED, DERIVED, ESTIMATE or OPEN
In a document, a display equation ($$ ... $$) is followed (after at most one blank line) by a marker line
    <!-- symbols: key1, key2, ... -->
and the generated block
    <!-- begin generated symbol list -->  ...  <!-- end generated symbol list -->
which `expand` (re)writes from the registry.  `check` extracts the atoms of every display equation and requires that
every atom is defined by one of the listed keys (or is pure typography), that every display has a marker, that every
listed key exists, that no atom is defined by two registry entries (one symbol, one meaning), that a display
tagged FE-n or IN-n is written exactly as in the inventory docs_src/equations.json, with the same keys, and that a
document is self-contained: every equation tag (FE-n, IN-n, FD-n, S-n, A-n, SB-n) that its text or one of its symbol lists cites
is displayed in that document.

Atoms.  A symbol of an equation is reduced to an atom: a LaTeX command with its decoration (\Psi, \bar\Psi, \partial,
\mathcal{L}, \hat{g}), a letter (g, R), a letter or command with a NAME subscript (a_4, x_0, G_F, m_\nu, M_{Pl}: the
subscript is a number, a single non-Greek command such as \star or \pm, contains \mathrm or \text, or is a combination
registered as an atom, such as m_\nu, G_F, M_{Pl}; plain letters in a subscript are otherwise indices), an index letter in an index position
(written "index:M": a single letter in a subscript or superscript that is not a name), or a special mark ("prime" for
the prime ', "dagger" for ^\dagger, "transpose" for ^T, "star" for ^* or ^\ast).  A superscript on Euler's number
\mathrm{e} or on a closing bracket is an exponent, a subscript on a vertical bar an evaluation point and a script on an
integral sign a limit: these are expressions, whose letters are symbols, not indices.  Typography is not an atom: digits,
+ - = < > ( ) [ ] | , ; : . !, \frac, \sqrt, \left, \right, \big..., spacing commands, \cdot, \dots, \le, \ge, \ne,
\approx, \sim, \simeq, \equiv, \to, \pm, \mp, \times, \lvert, \rvert, \langle, \rangle and the like.

Usage (repository root):
    python universe_model_3/tools/symbols_tool.py expand [NAME ...]   # rewrite the generated lists in NAME.md
    python universe_model_3/tools/symbols_tool.py check  [NAME ...]   # report; exit 1 on any problem
    python universe_model_3/tools/symbols_tool.py atoms "LATEX"       # show the atoms of one formula
    python universe_model_3/tools/symbols_tool.py sync   [NAME ...]   # rewrite FE-n/IN-n displays from the inventory

BEGIN FOLD DEFINITION
THE FOLD (the definition used in every UM-3 file)

Definition. The fold is the seven-dimensional surface of the author's eight-dimensional spacetime on which the cosine of
the angle z = 6 H x0 of the hidden direction vanishes:
    (FD-1)  F = { X = (x0, x1, ..., x7) : cos(6 H x0) = 0 };  in one period 0 < z < pi of the metric: z = pi/2, x0 = pi/(12 H).
X = {x0, ..., x7} are the author's coordinates: x0 the hidden space-like direction, x1, x2, x3 ordinary space, x4 the
time, x5, x6, x7 the three extra times; H is the author's constant (an inverse length). The author's metric depends on x0
only through cot(z)^2 and (sin(z)^2)^(1/6), so it repeats with the period pi/(6 H) of x0, and every period 0 < z < pi
contains exactly one fold, at z = pi/2. A point of the fold is labelled by the seven coordinates x1, ..., x7, and the
metric restricted to the fold (dx0 = 0, z = pi/2) is
    (FD-2)  ds^2 on F = e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2),
with three space-like and four time-like directions; a4 and b4 are the author's two functions of the time x4.

Why this surface is called a fold. Measured by the proper distance along the hidden direction,
    (FD-3)  sigma = sgn(pi/2 - z) ln(sin z)/(6 H),   d sigma = |cot z| dx0,   sin z = e^(-6 H |sigma|)
(the fold is sigma = 0; the half-period 0 < z < pi/2 is sigma < 0, the half-period pi/2 < z < pi is sigma > 0; the two ends
of the period, the tips z -> 0 and z -> pi, lie at sigma -> -infinity and sigma -> +infinity), the author's metric is
    (FD-4)  ds^2 = d sigma^2 + e^(-2 H |sigma|) [ e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2) ] - dx4^2.
It depends on sigma only through |sigma|. Four properties make the surface sigma = 0 a fold, and together they single it
out within the period:
  1. It is a mirror. The reflection sigma -> -sigma (that is z -> pi - z, or x0 -> pi/(6 H) - x0) maps the metric to
     itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
     period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are
     joined along the crease.
  2. The warp is largest on it. The warp factor (sin(z)^2)^(1/6) = e^(-2 H |sigma|), which multiplies ordinary space and
     the extra times, equals 1 on the fold and decreases on both sides.
  3. The metric has a kink on it. The metric is continuous across the fold, but its first derivative along sigma jumps.
     The extrinsic curvature of the surfaces sigma = const changes sign across the fold,
        (FD-5)  K^a_b = (1/2) g^ac d_sigma g_cb:  K^1_1 = K^2_2 = K^3_3 = K^5_5 = K^6_6 = K^7_7 = -H sgn(sigma),  K^4_4 = 0;
     (g_ab the metric components along the fold, g^ab their inverse, d_sigma the derivative with respect to sigma, sgn the
     sign function); it jumps by -2 H along ordinary space and along the extra times. The Einstein-Lovelock equations are
     linear in the second sigma-derivatives of the metric, so the jump puts a Dirac delta function delta_D(sigma) into
     them: the metric solves them only if the fold carries a thin source S^a_b, an energy-momentum tensor concentrated on
     sigma = 0 (the junction conditions). At the author's vacuum (a4' = H, b4 constant) its frame components along (ordinary space, the
     time, the extra times) are kappa S = (-10 H, -6 H, -10 H), at the static late-time state (a4 and b4 constant)
     kappa S = (-61 H/8, -31 H/4, -61 H/8), with kappa = 8 pi G_8 the gravitational coupling of eight dimensions. The fold
     is therefore not only a place but a physical object: a thin layer that carries energy and momentum (a brane).
  4. The author's coordinate x0 degenerates on it. The metric component g_x0x0 = cot(6 H x0)^2 vanishes on the fold and
     nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,
        (FD-6)  |sigma| = 3 H (x0 - pi/(12 H))^2 [1 + 6 H^2 (x0 - pi/(12 H))^2 + ...],
     so the two coordinate values on either side of x0 = pi/(12 H) at the same coordinate distance lie at the same proper
     distance from the fold: the coordinate line of x0 is folded onto the line of proper distances (a fold map, example 5).

What lives on the fold. In UM-3 the Standard Model (the Higgs doublet with the ad hoc vacuum, the gauge fields of
SU(3)_C x SU(2)_L x U(1)_Y, three generations of quarks and leptons and three right-handed neutrinos), the fold fluid and
the induced Einstein-Hilbert term of the fold live on the fold: they are fields at sigma = 0, functions of x1, ..., x4 (no
field depends on the extra times). Integrated over the extra times, the fold is the four-dimensional universe that we
observe, with the metric diag(e^(2 a4), e^(2 a4), e^(2 a4), -1) in x1, ..., x4. dirac16complex and gravity live in the
bulk sigma != 0 as well as on the fold; the bound states chi of dirac16complex are the part of it that the fold holds,
and the portals couple dirac16complex to the Standard Model at sigma = 0. In UM-3 files the word fold means this surface
and nothing else: a number of equal energy levels is written as a number of degenerate states, and a growth by powers of
Euler's number as a logarithm.

Examples of folds that are meaningful for UM-3.
  1. Our fold. The fold z = pi/2 of the period that contains our world (FD-1): the seven-dimensional world-volume of the
     Standard Model, and after the integration over the extra times the four-dimensional universe that we observe.
  2. The copies of the fold. Because the metric repeats with the period pi/(6 H), every surface
     x0 = pi/(12 H) + (an integer multiple of pi/(6 H)) is a copy of the fold, one per period. Neighbouring copies are
     separated by a tip (z a multiple of pi), where the warp (sin(z)^2)^(1/6) vanishes and g_x0x0 = cot(z)^2 diverges, and
     which lies at an infinite proper distance from both: in proper distance every copy has its own complete line
     -infinity < sigma < infinity. This is why the period pi/(6 H) of x0 produces no Kaluza-Klein tower with the spacing
     12 H; the x0 mass of the bound states is their binding to the fold.
  3. A folded sheet of paper. The crease of a folded sheet is a fold in this sense: the two halves are mirror images
     (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
     In UM-3 the direction across the crease is the hidden direction sigma, the seven directions along the crease are
     x1, ..., x7, and the crease is the fold.
  4. A folded function. The warp factor e^(-2 H |sigma|) is the simplest folded function: continuous, mirror symmetric,
     largest at sigma = 0, with a jump of its derivative,
        (FD-7)  d/d sigma e^(-2 H |sigma|) = -2 H sgn(sigma) e^(-2 H |sigma|),
                d^2/d sigma^2 e^(-2 H |sigma|) = 4 H^2 e^(-2 H |sigma|) - 4 H delta_D(sigma),
     whose delta function is the origin of the thin source of property 3. Every function of UM-3 that depends on sigma
     through |sigma| is folded at sigma = 0: the metric functions of FD-4 and the profiles of the bound states of
     dirac16complex (example 7).
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
     the bulk the vacuum energy Lambda_RS. The fold of UM-3 is of the same kind; it differs in that the time x4 is not
     warped, three extra times are warped together with ordinary space, and the Lovelock terms add to the junction
     conditions.
  7. A particle bound to a thin layer. A particle held by an attractive thin layer has a folded wave function: it falls
     off exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order
     Dirac equation, the wave function itself). In UM-3 the particles chi of dark matter are the states of dirac16complex
     bound to the fold; at rest and without their self-interaction (the field is
     Psi = e^(3 H |sigma|) chi(sigma) e^(-i omega_b x4))
        (FD-9)  chi(sigma) = e^(-q_b |sigma|) chi(0+) (sigma > 0),   chi(sigma) = e^(-q_b |sigma|) chi(0-) (sigma < 0),
                chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-),   omega_b = sqrt(m_Psi^2 - q_b^2),
     where mu_L, mu_R are the strengths of the fold for the left- and right-handed halves of dirac16complex (set by the
     Standard-Model fields on the fold), gamma^(0) = T^0 the Dirac matrix along sigma, P_L, P_R the chiral projectors,
     m_Psi the bulk mass, and q_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), s = sqrt(mu_L mu_R) (q_b = -m_Psi mu_L/2 for
     mu_R = 0).
  8. The fold as a mirror for dirac16complex. The reflection across the fold acts on the profiles chi(sigma) in two ways,
        (FD-10)  (R_1 chi)(sigma) = T_0 T_1 T_2 T_3 chi(-sigma),   (R_2 chi)(sigma) = T_0 T_5 T_6 T_7 chi(-sigma)
     (T_a the author's Dirac matrices; for states at rest R_1 is the reflection across the fold combined with the
     reflection of ordinary space, R_2 the reflection across the fold combined with the reflection of the extra times).
     The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a state can
     carry the charge -1 or +1. R_1 is a symmetry of dirac16complex, of gravity and of the mean field of a gas of the
     particles chi: the four bound states of Krein charge -1 (the particles chi) are even under it and the four of Krein
     charge +1 are odd, so the mean field of the gas cannot mix the two signs of the indefinite charge. R_2 maps the bound
     states of one Krein charge onto those of the other and makes the two sets degenerate without the self-interaction.
  9. The planes of Horava and Witten. In M-theory on an interval (a circle whose points are identified with their mirror
     images), the two ten-dimensional planes left in place by the reflection are mirror surfaces (property 1); the gauge
     fields E8 x E8 live on them while gravity fills the bulk. This is the arrangement of UM-3, where the Standard Model
     lives on the fold and gravity and dirac16complex fill the bulk.

What is not a fold.
  * The tips z = 0 and z = pi (mod pi): the mirror exchanges them within a period, but there the warp vanishes, g_x0x0
    diverges, and they lie at an infinite proper distance; they carry no thin source.
  * A smooth maximum of a warp, such as 1/cosh(H sigma)^2: mirror symmetric and largest at sigma = 0, but without a kink
    and without a thin source.
END FOLD DEFINITION
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent
REGISTRY = DOCS / 'docs_src' / 'symbols'   # every *.json file in this folder; together they are the registry
NAMES = ['MODEL', 'FIELD_EQUATIONS', 'SOLUTION', 'ANALYSIS', 'PROVENANCE', 'STABILISER']
# (adapted from the UM-2 tool of the same name; the rules are unchanged)

MARK = re.compile(r'^<!-- symbols: (.*?) -->\s*$')
BEGIN = '<!-- begin generated symbol list -->'
END = '<!-- end generated symbol list -->'

# typography: commands that are not symbols
TYPO = set(r'''
\frac \dfrac \tfrac \sqrt \left \right \big \Big \bigg \Bigg \bigl \bigr \Bigl \Bigr \biggl \biggr \Biggl \Biggr \middle
\quad \qquad \, \; \: \! \  \cdot \cdots \dots \ldots \vdots \ddots \le \leq \ge \geq \ne \neq \approx \sim \simeq \equiv
\to \rightarrow \leftarrow \Rightarrow \Leftrightarrow \mapsto \pm \mp \times \lvert \rvert \lVert \rVert \langle \rangle
\vert \Vert \{ \} \lbrace \rbrace \lbrack \rbrack \displaystyle \textstyle \scriptstyle \nonumber \notag \limits \nolimits
\begin \end \hline \\ \& \% \# \mid \parallel \colon \ll \gg \propto \lesssim \gtrsim \in \notin \subset \cup \cap
\land \lor \neg \forall \exists \circ \phantom \hphantom \vphantom \underbrace \overbrace \mathstrut \strut \ast
\sin \cos \tan \cot \sec \csc \sinh \cosh \tanh \coth \exp \ln \log \arcsin \arccos \arctan \min \max \lim \sup \inf
\det \arg \sum \int \prod \oint \iint
'''.split())
STANDARD_DOC = 'standard functions (sin, cos, tan, cot, sinh, cosh, tanh, exp, ln, log, det, min, max, lim) and the signs of sums, products and integrals'
# commands that decorate the next symbol (part of the atom)
DECOR = {r'\bar', r'\hat', r'\tilde', r'\dot', r'\ddot', r'\vec', r'\overline', r'\widehat', r'\widetilde', r'\check',
         r'\breve', r'\mathring'}
# commands whose argument is one name (the whole command with its argument is one atom)
NAMEFONTS = {r'\mathcal', r'\mathbb', r'\mathfrak', r'\mathscr', r'\mathbf', r'\boldsymbol', r'\mathsf', r'\mathrm',
             r'\operatorname', r'\mathit'}
# commands whose argument is ignored entirely
IGNORE_ARG = {r'\tag', r'\label', r'\text', r'\textrm', r'\textit', r'\textbf', r'\mbox', r'\hspace', r'\vspace',
              r'\textnormal'}
ENV_ARG = {r'\begin', r'\end'}
# closing delimiters: a superscript after one of them is an exponent of the bracketed expression
CLOSERS = {')', ']', '|', r'\rvert', r'\rVert', r'\Vert', r'\vert', r'\rbrace', r'\}', r'\rangle'}
# vertical bars: a subscript after one of them is an evaluation point (an expression), e.g. F\vert_{\xi=0}
EVALBARS = {'|', r'\vert', r'\rvert', r'\Vert', r'\rVert'}
# integral signs: their subscript and superscript are the limits of integration (expressions), e.g. \int_{-L}^{0}
INTEGRALS = {r'\int', r'\oint', r'\iint', r'\iiint', r'\lim'}   # (UM-3: the subscript of \lim is a limit, an expression)


def tokenize(s):
    toks = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            m = re.match(r'\\([A-Za-z]+|.)', s[i:], re.DOTALL)
            toks.append('\\' + m.group(1))
            i += len(m.group(0))
        elif c.isspace():
            i += 1
        else:
            toks.append(c)
            i += 1
    return toks


def group(toks, i):
    """Return (list of tokens of the group starting at i, next index).  A group is {...} or one token (a command with
    its own argument for name fonts and decorations)."""
    if i >= len(toks):
        return [], i
    if toks[i] == '{':
        depth = 0
        j = i
        while j < len(toks):
            if toks[j] == '{':
                depth += 1
            elif toks[j] == '}':
                depth -= 1
                if depth == 0:
                    return toks[i + 1:j], j + 1
            j += 1
        return toks[i + 1:], len(toks)
    if toks[i] in NAMEFONTS or toks[i] in DECOR:
        g, j = group(toks, i + 1)
        return [toks[i], '{'] + g + ['}'], j
    return [toks[i]], i + 1


def flat(toks):
    return ''.join(t if not (t.startswith('\\') and t[1:].isalpha()) else t + ' ' for t in toks).replace(' }', '}').strip()


def is_name(g):
    r"""A subscript or superscript that names (a_4, M_{Pl}, x_0, \Lambda_\star, f_*) rather than indexes.  A single
    letter or Greek letter is an index unless the registry knows the combination as a name (see atoms_of)."""
    text = [t for t in g if t not in ('{', '}')]
    if not text:
        return False
    if any(t in (r'\mathrm', r'\text', r'\operatorname', r'\textrm') for t in text):
        return True
    if all(t.isdigit() for t in text):
        return True
    if len(text) == 1 and (text[0] in ('*', '+', '-', '0') or (text[0].startswith('\\') and text[0][1:].isalpha()
                                                              and text[0][1:] not in GREEK)):
        return True  # \star, \pm, \perp, \parallel, \infty, *, +, -
    return False


def normalise(base_toks):
    s = flat(base_toks)
    s = re.sub(r'\s+', ' ', s)
    s = s.replace('{ ', '{').replace(' }', '}')
    s = re.sub(r'(\\[A-Za-z]+) \{', r'\1{', s)
    return s


def atoms_of(latex, names=frozenset()):
    r"""The atoms of a formula (see the module docstring).  `names` are the registered atoms; a base followed by a
    one-symbol subscript (or superscript) is read as one name atom when that combination is registered (m_\nu, G_F,
    c_V, \nu_e, J^B), otherwise the subscript is an index."""
    toks = tokenize(latex)
    out = []

    def walk(ts, in_index=False):
        i = 0
        last = (None, -1)   # (last symbol atom, index just after it): to recognise exponents of e
        lim = -1            # position of a limit of an integral sign (an expression, not an index)
        while i < len(ts):
            t = ts[i]
            if t in INTEGRALS:
                lim = i + 1
                i += 1
                continue
            if t in IGNORE_ARG or t in ENV_ARG:
                _, i = group(ts, i + 1)
                continue
            if t in ('{', '}', '&'):
                i += 1
                continue
            if t in ('^', '_'):
                # a superscript on Euler's number or on a closing bracket is an exponent, and a subscript on a vertical bar an
                # evaluation point: both are expressions, not indices
                expr = ((t == '^' and ((last[0] == r'\mathrm{e}' and last[1] == i) or (i > 0 and ts[i - 1] in CLOSERS)))
                        or (t == '_' and i > 0 and ts[i - 1] in EVALBARS)   # f\vert_{x=0}: the evaluation point
                        or i == lim)                                        # \int_{-L}^{0}: the limits
                at_limit = i == lim
                g, i = group(ts, i + 1)
                handle_script(t, g, expr)
                if at_limit:
                    lim = i   # the other limit may follow
                continue
            if t in ("'", r'\prime'):
                out.append('prime')
                i += 1
                continue
            if t in TYPO or (len(t) == 1 and not t.isalpha()) or (t.startswith('\\') and len(t) == 2 and not t[1].isalpha()):
                i += 1
                continue
            # a symbol: command, decorated command, name font, or letter
            if t in DECOR or t in NAMEFONTS:
                g, j = group(ts, i)
                base = g
                i = j
            else:
                base = [t]
                i += 1
            atom = normalise(base)
            single_letter = len(base) == 1 and ((len(base[0]) == 1 and base[0].isalpha())
                                                or (base[0].startswith('\\') and base[0][1:] in GREEK))
            if in_index and single_letter:
                # inside an index group a letter is an index, also with a numbered copy (A_1, B_2); x with a number
                # is the coordinate it names (gamma^{x_0}: the matrix along x_0)
                if i < len(ts) and ts[i] == '_':
                    g, j = group(ts, i + 1)
                    if all(x.isdigit() or x in ('{', '}') for x in g):
                        i = j
                        if base[0] == 'x':
                            out.append('x_{' + normalise(g) + '}')
                            continue
                out.append('index:' + base[0])
                continue
            # glued name scripts (one subscript and/or one superscript that are names)
            for _ in range(2):
                if i < len(ts) and ts[i] in ('_', '^'):
                    kind = ts[i]
                    g, j = group(ts, i + 1)
                    cand = atom + kind + '{' + normalise(g) + '}'
                    if cand in names or (kind == '_' and is_name(g)):
                        atom = cand
                        i = j
                        continue
                break
            out.append(atom)
            last = (atom, i)

    def handle_script(kind, g, expr=False):
        text = [x for x in g if x not in ('{', '}')]
        if not text:
            return
        if kind == '^':
            if text == [r'\dagger']:
                out.append('dagger')
                return
            if text == ['T']:
                out.append('transpose')
                return
            if text in (['*'], [r'\ast'], [r'\star']):
                out.append('star')
                return
            if all(x.isdigit() or x in ('-', '+', '/', '.', '(', ')') for x in text):
                return  # a power
            if all(x in ("'", r'\prime') for x in text):
                out.append('prime')
                return
        walk(g, in_index=not expr)

    walk(toks)
    return out


GREEK = set('alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi pi varpi rho '
            'varrho sigma varsigma tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi '
            'Psi Omega'.split())


def load_registry():
    reg = {}
    problems = []
    for f in sorted(REGISTRY.glob('*.json')):
        part = json.loads(f.read_text(encoding='utf-8'))
        for key, e in part.items():
            if key.startswith('_'):          # not a symbol (the definition of the fold carried by the file)
                continue
            if key in reg:
                problems.append('registry key %s is defined twice (second time in %s)' % (key, f.name))
            reg[key] = e
    owner = {}
    for key, e in reg.items():
        for f in ('tex', 'atoms', 'meaning', 'units'):
            if f not in e:
                problems.append('registry entry %s lacks %s' % (key, f))
        for a in e.get('atoms', []):
            if a in owner and owner[a] != key and not (e.get('shares') and owner[a] in e.get('shares')):
                problems.append('atom %s is defined by two entries: %s and %s (one symbol, one meaning)'
                                % (a, owner[a], key))
            owner.setdefault(a, key)
    return reg, owner, problems


def displays(lines):
    """Yield (start, end, latex) of every display equation: a line '$$' opening and closing, or '$$ ... $$' on lines."""
    i = 0
    in_code = False
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith('```'):
            in_code = not in_code
            i += 1
            continue
        if not in_code and s.startswith('$$'):
            start = i
            body = s[2:]
            if body.rstrip().endswith('$$') and len(body.strip()) >= 2:
                yield start, i, body.rstrip()[:-2]
                i += 1
                continue
            parts = [body]
            i += 1
            while i < len(lines) and not lines[i].rstrip().endswith('$$'):
                parts.append(lines[i])
                i += 1
            if i < len(lines):
                parts.append(lines[i].rstrip()[:-2])
            yield start, i, '\n'.join(parts)
        i += 1


def find_marker(lines, end):
    j = end + 1
    while j < len(lines) and lines[j].strip() == '':
        j += 1
        if j - end > 2:
            return None, None
    if j < len(lines):
        m = MARK.match(lines[j].strip())
        if m:
            return j, [k.strip() for k in m.group(1).split(',') if k.strip()]
    return None, None


def tag_of(latex):
    m = re.search(r'\\tag\{([^}]*)\}', latex)
    return m.group(1) if m else None


def render(keys, reg, tag):
    head = '**Symbols in (%s).**' % tag if tag else '**Symbols in this equation.**'
    out = [BEGIN, head, '']
    for k in keys:
        e = reg[k]
        line = '- $%s$: %s' % (e['tex'], e['meaning'].strip())
        extras = []
        if e.get('units'):
            extras.append('Unit: %s.' % e['units'].rstrip('.'))
        if e.get('value'):
            extras.append('Value: %s.' % e['value'].rstrip('.'))
        if e.get('status'):
            extras.append('Status: %s.' % e['status'])
        if extras:
            line += ' ' + ' '.join(extras)
        out.append(line)
    out += ['', END]
    return out


def doc_path(name):
    return Path(name) if name.endswith('.md') else DOCS / (name + '.md')


def expand(name, reg):
    path = doc_path(name)
    lines = path.read_text(encoding='utf-8').split('\n')
    out = []
    i = 0
    problems = []
    disp = {end: (start, latex) for start, end, latex in displays(lines)}
    last_tag = None
    while i < len(lines):
        line = lines[i]
        m = MARK.match(line.strip())
        if m:
            keys = [k.strip() for k in m.group(1).split(',') if k.strip()]
            missing = [k for k in keys if k not in reg]
            if missing:
                problems.append('%s line %d: unknown keys %s' % (name, i + 1, missing))
                keys = [k for k in keys if k in reg]
            out.append(line)
            # skip an existing generated block
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines) and lines[j].strip() == BEGIN:
                k = j
                while k < len(lines) and lines[k].strip() != END:
                    k += 1
                i = k + 1
            else:
                i += 1
            out += render(keys, reg, last_tag)
            continue
        out.append(line)
        if i in disp:
            last_tag = tag_of(disp[i][1])
        i += 1
    text = '\n'.join(out)
    if text != path.read_text(encoding='utf-8'):
        path.write_text(text, encoding='utf-8')
    return problems


INVENTORY = DOCS / 'docs_src' / 'equations.json'


def load_inventory():
    if not INVENTORY.exists():
        return {}
    return {e['id']: e for e in json.loads(INVENTORY.read_text(encoding='utf-8')) if not e['id'].startswith('_')}


def squeeze(s):
    return re.sub(r'\s+', '', s)


def sync(name, inventory):
    """Rewrite every display tagged FE-n or IN-n, and the key list of its marker, from the inventory (run expand
    afterwards).  The display is written as '$$', the inventory LaTeX, '$$' on separate lines."""
    path = doc_path(name)
    lines = path.read_text(encoding='utf-8').split('\n')
    problems = []
    edits = []
    for start, end, latex in displays(lines):
        tag = tag_of(latex)
        if not (tag and re.fullmatch(r'(FE|IN)-\d+', tag)):
            continue
        inv = inventory.get(tag)
        if inv is None:
            problems.append('%s line %d: tag %s is not in the inventory' % (name, start + 1, tag))
            continue
        j, keys = find_marker(lines, end)
        same = squeeze(inv['latex']) == squeeze(latex) and keys is not None and set(keys) == set(inv['keys'])
        if not same:
            edits.append((start, end, j, inv))
    for start, end, j, inv in reversed(edits):
        marker = '<!-- symbols: %s -->' % ', '.join(inv['keys'])
        block = ['$$'] + inv['latex'].split('\n') + ['$$']
        if j is not None:
            lines[j] = marker
            lines[start:end + 1] = block
        else:
            lines[start:end + 1] = block + [marker]
    if edits:
        path.write_text('\n'.join(lines), encoding='utf-8')
        print('%s: %d tagged displays rewritten from the inventory' % (name, len(edits)))
    return problems


TAGREF = re.compile(r'(?<![A-Za-z0-9])((?:FE|IN|FD|SB|S|A)-\d+)\b')


def prose_tag_problems(name, lines, shown):
    """Every equation tag that the prose of a document cites (outside display equations, generated symbol lists, code
    blocks and HTML comments) must be displayed in the document itself: each document is self-contained."""
    problems = []
    skip = set()
    for start, end, _ in displays(lines):
        skip.update(range(start, end + 1))
    in_list = in_code = False
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith('```'):
            in_code = not in_code
            continue
        if s == BEGIN:
            in_list = True
        if in_list or in_code or i in skip or s.startswith('<!--'):
            if s == END:
                in_list = False
            continue
        for t in TAGREF.findall(line):
            if t not in shown:
                problems.append('%s line %d: the text cites %s, which this document does not display' % (name, i + 1, t))
    return problems


def check(name, reg, owner, inventory=None):
    path = doc_path(name)
    lines = path.read_text(encoding='utf-8').split('\n')
    problems = []
    n_disp = 0
    inventory = inventory if inventory is not None else load_inventory()
    shown = {tag_of(latex) for _, _, latex in displays(lines)} - {None}
    problems += prose_tag_problems(name, lines, shown)
    for start, end, latex in displays(lines):
        n_disp += 1
        j, keys = find_marker(lines, end)
        where = '%s line %d' % (name, start + 1)
        if keys is None:
            problems.append('%s: display equation without a symbol list: %s' % (where, latex.strip()[:90]))
            continue
        # a display tagged FE-n or IN-n is the inventory's equation, written out identically with the same keys
        tag = tag_of(latex)
        if tag and re.fullmatch(r'(FE|IN)-\d+', tag):
            inv = inventory.get(tag)
            if inv is None:
                problems.append('%s: tag %s is not in the inventory' % (where, tag))
            else:
                if squeeze(inv['latex']) != squeeze(latex):
                    problems.append('%s: (%s) differs from the inventory equation' % (where, tag))
                if set(inv['keys']) != set(keys):
                    problems.append('%s: the keys of (%s) differ from the inventory keys' % (where, tag))
        unknown = [k for k in keys if k not in reg]
        if unknown:
            problems.append('%s: unknown registry keys %s' % (where, unknown))
        # a display may cite (in its text) only equations that this document displays
        for t in TAGREF.findall(re.sub(r'\\tag\{[^}]*\}', '', latex)):
            if t not in shown:
                problems.append('%s: the display cites %s, which this document does not display' % (where, t))
        # the symbol list may cite only equations that this document displays
        for k in keys:
            if k in reg:
                for t in TAGREF.findall(reg[k]['meaning'] + ' ' + reg[k].get('value', '') + ' ' + reg[k].get('units', '')):
                    if t not in shown:
                        problems.append('%s: the entry %s of the symbol list cites %s, which this document does not display'
                                        % (where, k, t))
        covered = set()
        for k in keys:
            if k in reg:
                covered.update(reg[k]['atoms'])
        need = []
        for a in atoms_of(latex, frozenset(owner)):
            if a not in covered and a not in need:
                need.append(a)
        if need:
            hint = ['%s (%s)' % (a, owner[a]) if a in owner else a for a in need]
            problems.append('%s: atoms not defined by the listed keys: %s' % (where, ', '.join(hint)))
        # the generated block must be current
        k = j + 1
        while k < len(lines) and lines[k].strip() == '':
            k += 1
        if k >= len(lines) or lines[k].strip() != BEGIN:
            problems.append('%s: the generated symbol list is missing (run expand)' % where)
        else:
            e = k
            while e < len(lines) and lines[e].strip() != END:
                e += 1
            block = lines[k:e + 1]
            if block != render([x for x in keys if x in reg], reg, tag_of(latex)):
                problems.append('%s: the generated symbol list is out of date (run expand)' % where)
    return n_disp, problems


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('expand', 'check', 'atoms', 'sync'):
        print(__doc__)
        sys.exit(2)
    if sys.argv[1] == 'atoms':
        reg, owner, _ = load_registry()
        print('\n'.join(atoms_of(' '.join(sys.argv[2:]), frozenset(owner))))
        return
    reg, owner, problems = load_registry()
    names = sys.argv[2:] or [n for n in NAMES if (DOCS / (n + '.md')).exists()]
    if sys.argv[1] == 'sync':
        inventory = load_inventory()
        for n in names:
            problems += sync(n, inventory)
        for p in problems:
            print('problem:', p)
        sys.exit(1 if problems else 0)
    if sys.argv[1] == 'expand':
        for n in names:
            problems += expand(n, reg)
        for p in problems:
            print('problem:', p)
        sys.exit(1 if problems else 0)
    total = 0
    for n in names:
        nd, ps = check(n, reg, owner)
        total += nd
        problems += ps
        print('%s: %d display equations, %d problems' % (n, nd, len(ps)))
    for p in problems:
        print('problem:', p)
    print('symbols_check=%s (%d display equations, %d registry entries, %d problems)'
          % ('OK' if not problems else 'FAILED', total, len(reg), len(problems)))
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
