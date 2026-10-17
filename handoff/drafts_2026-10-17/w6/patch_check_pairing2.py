"""W6 draft, part 2 of Revision/pairing/python/check_pairing.py for the corrected metric (applied to the copy argv[1]):
the fold instead of the Z2 brane in every remaining text, the not-established list and its comparison topics (the
Wolfram side, verify_pairing.wls, must carry the same tokens: 'across the fold', 'degenerate')."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''# =========================================================================== geometry of SPEC section 1''',
    '''# =========================================================================== geometry of SPEC section 1 (corrected metric)''')
rep('''b4 = sp.Function("b4", positive=True)(x4)   # the extra-time function of SPEC section 1 (b4 > 0, never 1)''',
    '''b4 = sp.Function("b4", positive=True)(x4)   # the function b4(x4) > 0 of SPEC section 1''')
rep('''          "the canonical spin connection omega_mu ab = eta_ac omega_mu^c_b of the metric of SPEC section 1 is antisymmetric in (a, b) for all mu")''',
    '''          "the canonical spin connection omega_mu ab = eta_ac omega_mu^c_b of the corrected metric of SPEC section 1 is antisymmetric in (a, b) for all mu")''')
rep('''          "%s, metric of SPEC section 1 with the canonical spin connection: L_{m,lambda}[Gamma Psi] + L_{-m,-lambda}[Psi] = 0 on the full first jet (%s)" % (fn, info))''',
    '''          "%s, corrected metric of SPEC section 1 with the canonical spin connection: L_{m,lambda}[Gamma Psi] + L_{-m,-lambda}[Psi] = 0 on the full first jet (%s)" % (fn, info))''')
rep('''          "%s, mirror across the Z2 brane z -> pi - z with the positive frame on both sides: " % fn + "; ".join(table)''',
    '''          "%s, reflection z -> pi - z across the fold z = pi/2 (an isometry of the corrected metric; the other half of the "
          "cell) with the positive frame on both sides: " % fn + "; ".join(table)''')
rep('''    "The Z2 brane at z = pi/2 and the mirror construction are ASSUMED (a boundary/orbifold choice), not derived from the field equations.",''',
    '''    "The continuation across the fold z = pi/2 is not derived: T2 maps a configuration on the half z in (0, pi/2) of a cell to one on the other half (pi/2, pi) through the isometry z -> pi - z; the corrected metric has no Z2 orbifold (the two halves are not identified), and no matching condition of the field between the halves is part of the theorems.",''')
rep('''    "The brane z = pi/2 is a degenerate surface of the metric (g_00 = cot^2 z = 0, sqrt|g| = b4^{3/2} cos z = 0 there, geometry.brane_degenerate); no junction condition, brane tension or matching of the field across it is derived.",''',
    '''    "The fold z = pi/2 is a degenerate surface of the metric (g_00 = e^{-2a4} b4 cot^2 z = 0, sqrt|g| = e^{-a4} b4^2 |cot z| sin^{1/2} z = 0 there, geometry.fold_degenerate); no junction condition or matching of the field at it is derived.",''')
rep('''    "The Kohn-Sham level (T3) is not covered by this checker; it is proved separately in Revision/pairing/kohn_sham/ (check_t3.py, with its own hypotheses: ASSUMED Z2 brane, instantaneous mean-field Kohn-Sham states).",''',
    '''    "The Kohn-Sham level (T3) is not covered by this checker; it is proved separately in Revision/pairing/kohn_sham/ (check_t3.py, with its own hypotheses: both fold conditions filled (ASSUMED), instantaneous mean-field Kohn-Sham states).",''')
rep('''              ("independent universes do not cancel", "independently quantised"), ("Z2 brane assumed", "assumed"),''',
    '''              ("independent universes do not cancel", "independently quantised"),
              ("continuation across the fold not derived", "across the fold"),''')
rep('''              ("T1 not a pure +-m pairing for lambda != 0", "pure"), ("degenerate brane", "degenerate"),''',
    '''              ("T1 not a pure +-m pairing for lambda != 0", "pure"), ("degenerate fold", "degenerate"),''')
rep('''            "mirror": "R: z -> pi - z (x0 -> pi/(6H) - x0), Z2 brane at z = pi/2 (ASSUMED boundary construction); positive frame e^(x0)_(x0) = |cot z| on both sides; Lambda = diag(-1,1,1,1,1,1,1,1)",''',
    '''            "mirror": "R: z -> pi - z (x0 -> pi/(6H) - x0), the reflection across the fold z = pi/2, an isometry of the corrected metric between the two halves of a cell (not an orbifold); positive frame e^(x0)_(x0) = e^{-a4} b4^{1/2} |cot z| on both sides; Lambda = diag(-1,1,1,1,1,1,1,1)",''')
rep('''both statistics; the metric of SPEC section 1 and any gravitational field",''',
    '''both statistics; the corrected metric of SPEC section 1 and any gravitational field",''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
