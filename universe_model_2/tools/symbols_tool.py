#!/usr/bin/env python3
r"""The symbol lists of the UM-2 documents (version 4): every display equation is followed by the complete list of the
symbols that appear in it, generated from one registry, and a check that no symbol of an equation is left undefined.

Registry: the JSON files universe_model_2/docs_src/symbols/*.json, each a JSON object  key -> entry  (keys unique over
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
listed key exists, and that no atom is defined by two registry entries (one symbol, one meaning).

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
    python universe_model_2/tools/symbols_tool.py expand [NAME ...]   # rewrite the generated lists in NAME.md
    python universe_model_2/tools/symbols_tool.py check  [NAME ...]   # report; exit 1 on any problem
    python universe_model_2/tools/symbols_tool.py atoms "LATEX"       # show the atoms of one formula
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent
REGISTRY = DOCS / 'docs_src' / 'symbols'   # every *.json file in this folder; together they are the registry
NAMES = ['MODEL', 'FIELD_EQUATIONS', 'SOLUTION', 'ANALYSIS', 'PROVENANCE']

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
INTEGRALS = {r'\int', r'\oint', r'\iint', r'\iiint'}


def tokenize(s):
    toks = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            m = re.match(r'\\([A-Za-z]+|.)', s[i:])
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


def check(name, reg, owner):
    path = doc_path(name)
    lines = path.read_text(encoding='utf-8').split('\n')
    problems = []
    n_disp = 0
    for start, end, latex in displays(lines):
        n_disp += 1
        j, keys = find_marker(lines, end)
        where = '%s line %d' % (name, start + 1)
        if keys is None:
            problems.append('%s: display equation without a symbol list: %s' % (where, latex.strip()[:90]))
            continue
        unknown = [k for k in keys if k not in reg]
        if unknown:
            problems.append('%s: unknown registry keys %s' % (where, unknown))
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
    if len(sys.argv) < 2 or sys.argv[1] not in ('expand', 'check', 'atoms'):
        print(__doc__)
        sys.exit(2)
    if sys.argv[1] == 'atoms':
        reg, owner, _ = load_registry()
        print('\n'.join(atoms_of(' '.join(sys.argv[2:]), frozenset(owner))))
        return
    reg, owner, problems = load_registry()
    names = sys.argv[2:] or [n for n in NAMES if (DOCS / (n + '.md')).exists()]
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
