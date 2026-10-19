#!/usr/bin/env python3
"""Generate the LaTeX of the order-0 Lovelock tensors and background field equations in version-4 notation from
outputs/background.json (sympy), check them, and write bg_latex.py.  v3 -> v4: A -> \\mathcal{H}, h -> \\mathcal{H}_f,
k -> K, Adot -> \\dot{\\mathcal{H}}, hdot -> \\dot{\\mathcal{H}}_f."""
import json
from pathlib import Path

import sympy as sp

SCR = Path(__file__).resolve().parent
BG = json.load(open('/home/claude/dirac_claude/universe_model_2/outputs/background.json'))
A, h, k, Ad, hd, H, Lam, kap, w2, w3, rho, p3, pb = sp.symbols('A h k Adot hdot H Lambda kappa w2 w3 rho p3 pbar')
loc = dict(A=A, h=h, k=k, Adot=Ad, hdot=hd, H=H, Lambda=Lam, Lam=Lam, kappa=kap, w2=w2, w3=w3)
NAMES = {A: r'\mathcal{H}', h: r'\mathcal{H}_f', k: 'K', Ad: r'\dot{\mathcal{H}}', hd: r'\dot{\mathcal{H}}_f', H: 'H'}
ORDER = [Ad, hd, k, A, h, H]


def term_tex(c, mon):
    """c a rational, mon a dict symbol->power."""
    num, den = [], []
    for s in ORDER:
        e = mon.get(s, 0)
        if e == 0:
            continue
        t = NAMES[s] + ('^{%d}' % abs(e) if abs(e) != 1 else '')
        if s in (A, h) and abs(e) != 1:
            t = NAMES[s] if s == A else r'\mathcal{H}_f'
            t = t + '^{%d}' % abs(e)
        (num if e > 0 else den).append(t)
    c = sp.Rational(c)
    sign = '-' if c < 0 else '+'
    c = abs(c)
    p, q = c.p, c.q
    numtex = ''.join(num)
    # \mathcal{H}_f^{2} must be written {\mathcal{H}_f}^{2}?  No: \mathcal{H}_f^{2} is fine in LaTeX.
    if den or q != 1:
        top = (str(p) if p != 1 or not numtex else '') + (r'\,' if p != 1 and numtex else '') + numtex
        if not top:
            top = '1'
        bot = (str(q) if q != 1 else '') + ''.join(den)
        body = r'\frac{%s}{%s}' % (top, bot)
    else:
        body = (str(p) if p != 1 or not numtex else '') + (r'\,' if p != 1 and numtex else '') + numtex
    return sign, body


def poly_tex(expr, width=96):
    expr = sp.expand(expr)
    terms = []
    for t in sp.Add.make_args(expr):
        c, rest = t.as_coeff_Mul()
        mon = {}
        for b, e in rest.as_powers_dict().items():
            if b == 1:
                continue
            mon[b] = int(e)
        terms.append((mon, c))
    terms.sort(key=lambda mc: (mc[0].get(H, 0), -sum(v for s_, v in mc[0].items() if s_ != H),
                               [-mc[0].get(s_, 0) for s_ in ORDER]))
    lines, cur = [], ''
    for mon, c in terms:
        sign, body = term_tex(c, mon)
        piece = ('-' + body if sign == '-' else body) if not cur and not lines else ' %s %s' % (sign, body)
        if cur and len(cur) + len(piece) > width:
            lines.append(cur)
            cur = '%s %s' % (sign, body)
        else:
            cur += piece
    lines.append(cur)
    return lines


def P(s):
    return sp.sympify(s, locals=loc)


E = {}
for p in ('1', '2', '3'):
    d = BG['E_class_form'][p]
    E[p] = {'x4': P(d['x4']), 'x1': P(d['x1 (= x2 = x3)']), 'x0': P(d['x0 (= x5 = x6 = x7)'])}
fe = BG['field_equations_class_form']
F = {'x4': P(fe['x4 (constraint)'].split('=')[0]), 'x1': P(fe['x1 = x2 = x3'].split('=')[0]),
     'x0': P(fe['x0 = x5 = x6 = x7'].split('=')[0])}
# check: field equation lhs = E1 + (w2/H^2) E2 + (w3/H^4) E3 + Lambda
for c in ('x4', 'x1', 'x0'):
    lhs = E['1'][c] + w2 / H ** 2 * E['2'][c] + w3 / H ** 4 * E['3'][c] + Lam
    assert sp.simplify(lhs - F[c]) == 0, c
print('field equations = sum_p alpha_p E_(p) + Lambda: OK')
sub = {w2: sp.Rational(1, 32), w3: sp.Rational(1, 1152), Lam: -10 * H ** 2}
out = {}
for p in ('1', '2', '3'):
    for c in ('x4', 'x1', 'x0'):
        out['E%s_%s' % (p, c)] = poly_tex(E[p][c])
for c in ('x4', 'x1', 'x0'):
    ex = sp.expand(F[c].subs(sub))
    cA = sp.expand(ex.coeff(Ad))
    ch = sp.expand(ex.coeff(hd))
    rest = sp.expand(ex - cA * Ad - ch * hd)
    out['F_%s_Adot' % c] = poly_tex(cA, 80) if cA != 0 else []
    out['F_%s_hdot' % c] = poly_tex(ch, 80) if ch != 0 else []
    out['F_%s_rest' % c] = poly_tex(rest, 92)
# v3 printed x4 constraint (FIELD_EQUATIONS) for comparison of one equation
v3x4 = (-sp.Rational(15, 16) * A**2 * h**4 / H**4 - sp.Rational(5, 4) * A**3 * h**3 / H**4 - sp.Rational(3, 8) * h**4 / H**2
        - sp.Rational(9, 2) * A * h**3 / H**2 - sp.Rational(27, 4) * A**2 * h**2 / H**2 + sp.Rational(9, 8) * k * A**2 * h**2 / H**2
        - sp.Rational(3, 2) * h * A**3 / H**2 + sp.Rational(3, 4) * h * k * A**3 / H**2 - 6 * h**2 + sp.Rational(3, 4) * k * h**2
        - 12 * A * h + sp.Rational(9, 2) * A * h * k - 3 * A**2 + sp.Rational(9, 4) * k * A**2 - sp.Rational(3, 16) * A**2 * k**2
        - 10 * H**2 + 6 * k * H**2 - sp.Rational(3, 8) * H**2 * k**2)
assert sp.expand(F['x4'].subs(sub) - v3x4) == 0
print('x4 constraint equals the version-3 printed form: OK')
(SCR / 'bg_latex.py').write_text('BG = ' + json.dumps(out, indent=1) + '\n', encoding='utf-8')
for kk, v in out.items():
    print(kk, len(v), max((len(x) for x in v), default=0))
