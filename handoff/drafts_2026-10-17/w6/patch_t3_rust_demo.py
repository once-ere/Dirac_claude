"""W6 draft: Revision/pairing/kohn_sham/numerics/t3_rust_demo.py for the corrected metric (applied to the copy argv[1]):
the key emtIntegrals_2Vol7_int_e3Hy of the corrected solver, the fold instead of the brane, Vol_7 = ell^3 v_t e^{(5/3) a4,0},
the hidden scale f in the block Hamiltonians and the zero modes."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''  image    the -M universe:  (-m, +lambda), tip theta = pi        (the T3 image: transformed tip, brane parities
                                                                    exchanged by the map, solved independently)''',
    '''  image    the -M universe:  (-m, +lambda), tip theta = pi        (the T3 image: transformed tip, the two fold
                                                                    conditions exchanged by the map, solved independently)''')
rep('''and compares them: T3 predicts EQUAL levels (sector (n2, j, parity) of plus <-> sector (n2, -j, other parity) of''',
    '''and compares them: T3 predicts EQUAL levels (sector (n2, j, fold condition) of plus <-> sector (n2, -j, other fold
condition) of''')
rep('''States: the slices a4,0 in {0, 0.5, 1, 1.5, 2} of the history a4 = A H x4 (A = 1), b4 = b4(0) e^{(4/3) A H x4} of the
author's metric with b4(x4) (SPEC section 1; b4 is never 1), with the extra times x5, x6, x7 DEFLATING exponentially
(scale factor e^{-a4} b4^{1/2} sin^{1/6} z = b4(0)^{1/2} e^{-a4/3} sin^{1/6} z on the history).  This history is a''',
    '''States: the slices a4,0 in {0, 0.5, 1, 1.5, 2} of the history a4 = A H x4 (A = 1), b4 = b4(0) e^{(4/3) A H x4} of the
corrected primordial metric of 2026-10-16 (version 2; SPEC section 1), with the extra times x5, x6, x7 DEFLATING
exponentially (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12} = b4(0)^{1/2} e^{-a4/3} (sin^2 z)^{1/12} on the history).
This history is a''')
rep('''without back-reaction.  T3 holds slice by slice; it does not use the history (b4 does not enter the block
Hamiltonians h_j).  N and lambda_hat (the solver's coupling, held fixed along the history while the cell volume
Vol_7(a4,0) = ell^3 v_t e^{(3/2) beta a4,0} grows; `single --lambda`) are those of the canonical matrix''',
    '''without back-reaction.  T3 holds slice by slice; it does not use the history (a4 and b4 enter the block
Hamiltonians h_j only through the positive constants f = e^{-a4} b4^{1/2} and kappa = e^{-a4} of the slice).  N and
lambda_hat (the solver's coupling, held fixed along the history while the cell volume
Vol_7(a4,0) = ell^3 v_t e^{(2 beta - 1) a4,0} = ell^3 v_t e^{(5/3) a4,0} grows; `single --lambda`) are those of the
canonical matrix''')
rep('''The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0], z = 6 H x0''' + " " + '''
(brane y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra times.''',
    '''The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln|sin z|/(6 H) in [-L, 0], z = 6 H x0 real
(the fold cos z = 0 at y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra
times.''')
rep('''emtIntegrals_2Vol7_int_e6Hy''', '''emtIntegrals_2Vol7_int_e3Hy''', n=12)
rep('''              "by label with the sector map (n2, j, parity) -> (n2, -j, other parity) (eps, degeneracy, occupation), "
              "E_KS, E_band, E_int, mu, entropy, N, the EMT integrals 2 Vol_7 int e^(6Hy)(rho, p3, p_t, p0, n) dy, "''',
    '''              "by label with the sector map (n2, j, fold condition) -> (n2, -j, other fold condition) (eps, degeneracy, "
              "occupation), E_KS, E_band, E_int, mu, entropy, N, the EMT integrals 2 Vol_7 int e^(3Hy)(rho, p3, p_t, p0, n) dy, "''')
rep('''          "state with a control state (with -m and the untransformed tip the k = 0 zero modes (e^(-m y), 0) are localised at "
          "the tip instead of the brane); the combined "''',
    '''          "state with a control state (with -m and the untransformed tip the k = 0 zero modes (e^(-f m y), 0) are localised "
          "at the tip instead of the fold); the combined "''')
rep('''                    "image": "(-m, +lambda), tip theta = pi (the T3 image, transformed tip; brane parities exchanged by the map)",''',
    '''                    "image": "(-m, +lambda), tip theta = pi (the T3 image, transformed tip; the two fold conditions exchanged by the map)",''')
rep('''                      "coupling lambda_hat of each tag is held fixed while Vol_7(a4,0) = ell^3 v_t e^{2 a4,0} grows; the "''',
    '''                      "coupling lambda_hat of each tag is held fixed while Vol_7(a4,0) = ell^3 v_t e^{(5/3) a4,0} grows; the "''')
rep('''                           "t3-theory.json). Instantaneous (adiabatic) states on a prescribed background; ASSUMED Z2 brane; "''',
    '''                           "t3-theory.json). Instantaneous (adiabatic) states on a prescribed background; both fold "
                           "conditions filled (ASSUMED); "''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
