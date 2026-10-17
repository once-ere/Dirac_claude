"""W6 draft: Revision/pairing/python/check_pairing.py for the corrected metric (copy argv[1]): the vielbein, the fold
degeneracy check, the texts."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''* the metric of SPEC section 1 with b4(x4) (a4(x4) real, b4(x4) > 0 arbitrary; b4 is never 1), its Christoffel
  symbols, the diagonal vielbein and the canonical spin connection are computed with sympy;''',
    '''* the corrected primordial metric of SPEC section 1 (version 2 of 2026-10-16; a4(x4) real, b4(x4) > 0 arbitrary), on the
  patches 0 < z < pi/2 and pi/2 < z < pi of a cell (sin z > 0 there, so (sin^2 z)^(1/12) = sin^(1/6) z), its Christoffel
  symbols, the diagonal vielbein and the canonical spin connection are computed with sympy;''')
rep('''       matrix gamma^(x0), with the mirror z -> pi - z across the Z2 brane at z = pi/2:''',
    '''       matrix gamma^(x0), with the mirror z -> pi - z across the fold z = pi/2 (an isometry of the corrected metric):''')
rep('''    """Diagonal vielbein e^a_mu = f_mu delta (order x0, x1, ..., x7); s0 = +1 on the patch z in (0, pi/2)
    (f0 = cot z > 0), s0 = -1 on the mirror patch z in (pi/2, pi) (f0 = -cot z > 0): the positive frame sqrt|g_mu mu|."""''',
    '''    """Diagonal vielbein e^a_mu = f_mu delta (order x0, x1, ..., x7) of the corrected metric; s0 = +1 on the patch z in
    (0, pi/2) (f0 = e^{-a4} b4^{1/2} cot z > 0), s0 = -1 on the mirror patch z in (pi/2, pi) (f0 = -e^{-a4} b4^{1/2} cot z > 0):
    the positive frame sqrt|g_mu mu|."""''')
rep('''            f = [s0 * sp.cot(z)] + [E * S6] * 3 + [sp.Integer(1)] + [Em * sp.sqrt(b4) * S6] * 3''',
    '''            f = [s0 * Em * sp.sqrt(b4) * sp.cot(z)] + [E] * 3 + [sp.Integer(1)] + [Em * sp.sqrt(b4) * S6] * 3''')
rep('''          "extra-time vielbein e^-a4 b4^(1/2) sin^(1/6) z: the T1, T2 and Q checks in the metric of SPEC section 1 are made "
          "with b4(x4) not constant (b4 is never 1)" % sp.simplify(dw).subs(b4, sp.Symbol("b4")).subs(a4, sp.Symbol("a4")))''',
    '''          "extra-time vielbein e^-a4 b4^(1/2) sin^(1/6) z: the T1, T2 and Q checks in the corrected metric of SPEC section 1 are "
          "made with b4(x4) not constant" % sp.simplify(dw).subs(b4, sp.Symbol("b4")).subs(a4, sp.Symbol("a4")))''')
rep('''           and sp.simplify(geo.sqrtg - b4 ** sp.Rational(3, 2) * sp.cos(z)) == 0)
    check("geometry.brane_degenerate", deg,
          "sqrt|g| = %s on the patch; at the brane z = pi/2: g_00 -> 0 and sqrt|g| -> 0 (a degenerate surface of the metric)" % geo.sqrtg)
    check("geometry.mirror_isometry", iso,
          "g_mu mu(pi - z) = g_mu mu(z) for every component: z -> pi - z (x0 -> pi/(6H) - x0, the Z2 brane at z = pi/2) is an isometry of the metric of SPEC section 1")''',
    '''           and sp.simplify(geo.sqrtg - sp.exp(-a4) * b4 ** 2 * sp.cot(z) * sp.sin(z) ** sp.Rational(1, 2)) == 0)
    check("geometry.fold_degenerate", deg,
          "sqrt|g| = %s on the patch; at the fold z = pi/2: g_00 -> 0 and sqrt|g| -> 0 (a degenerate surface of the metric, "
          "where the two halves of a cell meet)" % geo.sqrtg)
    check("geometry.mirror_isometry", iso,
          "g_mu mu(pi - z) = g_mu mu(z) for every component: z -> pi - z (x0 -> pi/(6H) - x0, the reflection across the fold "
          "z = pi/2) is an isometry of the corrected metric of SPEC section 1")''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
