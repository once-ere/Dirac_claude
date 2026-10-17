"""W6 draft, part 2 of Revision/pairing/kohn_sham/numerics/t3_reference_demo.py (after patch_t3_reference_demo.py; applied
to the copy argv[1]): N_mid of the corrected record (read from parameters.json instead of the hard-coded 136), the fold
instead of the brane, the corrected metric in the texts, Vol_7 = ell^3 v_t e^{(5/3) a4,0}."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''    phi = j [phi_tip (1 - s) + phi_brane s],  s = (y + L)/L,  phi_tip = 0 (theta = 0) or pi/2 (theta = pi),
    phi_brane = 0 (even, b(0) = 0) or pi/2 (odd, a(0) = 0),''',
    '''    phi = j [phi_tip (1 - s) + phi_fold s],  s = (y + L)/L,  phi_tip = 0 (theta = 0) or pi/2 (theta = pi),
    phi_fold = 0 (fold condition theta = 0, "even", b(0) = 0) or pi/2 (theta = pi, "odd", a(0) = 0),''')
rep('''ground states N = 8 x lambda tags lam0, lamp2, lamm2 x a4,0 = 0, 1, 2 and N = 136 x lamp2, lamm2 x a4,0 = 0, 2; Mermin
states N = 8, lamp1 x a4,0 = 0, 2 x T = 0.01, 0.05 and N = 136, lamp1, a4,0 = 2, T = 0.05.  The slices belong to the
history a4 = A H x4, b4 = b4(0) e^{(4/3) A H x4} (A = 1) of the author's metric with b4(x4) (SPEC section 1; b4 is never
1), with x5, x6, x7 DEFLATING as e^{-a4} b4^{1/2} = b4(0)^{1/2} e^{-a4/3}; the coupling is the reference's lambda_hat,
held fixed while the cell volume Vol_7(a4,0) = ell^3 v_t e^{(3/2) beta a4,0} grows (ks_fd.Phys.vol7, beta from
ks-theory.json).''',
    '''ground states N = 8 x lambda tags lam0, lamp2, lamm2 x a4,0 = 0, 1, 2 and N = N_mid x lamp2, lamm2 x a4,0 = 0, 2; Mermin
states N = 8, lamp1 x a4,0 = 0, 2 x T = 0.01, 0.05 and N = N_mid, lamp1, a4,0 = 2, T = 0.05 (N_mid = 592 in the record of
the corrected metric, read from parameters.json).  The slices belong to the history a4 = A H x4,
b4 = b4(0) e^{(4/3) A H x4} (A = 1) of the corrected primordial metric of 2026-10-16 (version 2; SPEC section 1), with
x5, x6, x7 DEFLATING as e^{-a4} b4^{1/2} = b4(0)^{1/2} e^{-a4/3}; the hidden direction carries the same scale f, which
enters the block Hamiltonians as 1/f; the coupling is the reference's lambda_hat, held fixed while the cell volume
Vol_7(a4,0) = ell^3 v_t e^{(2 beta - 1) a4,0} = ell^3 v_t e^{(5/3) a4,0} grows (ks_fd.Phys.vol7, beta from
ks-theory.json).''')
rep('''The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0], z = 6 H x0''' + " " + '''
(brane y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra times.''',
    '''The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln|sin z|/(6 H) in [-L, 0], z = 6 H x0 real
(the fold cos z = 0 at y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra
times.''')
rep('''        # tip end phi = pi/2 (a(-L) = 0); even: pi/2 at the tip -> 0 at the brane; odd: pi/2 throughout''',
    '''        # tip end phi = pi/2 (a(-L) = 0); even: pi/2 at the tip -> 0 at the fold; odd: pi/2 throughout''')
rep('''    ce[-1], se[-1] = 1.0, 0.0            # brane (even): phi = 0 exactly''',
    '''    ce[-1], se[-1] = 1.0, 0.0            # fold (even): phi = 0 exactly''')
rep('''    # (-M, theta = pi) has, by the map, odd parity: eps = 0 and +-sqrt(M^2 + (n pi/L)^2); even: tan(pL) = -p/M''',
    '''    # (-M, theta = pi) has, by the map, odd parity: eps = 0 and +-sqrt(M^2 + (n pi/L)^2); even: tan(pL) = -p/M
    # (at a4,0 = 0, where the hidden scale f = 1; in general L -> f L)''')
rep('''          "(Richardson) the k = 0 levels equal the exact image spectra (odd parity: eps = 0 and sqrt(M^2 + (n pi/L)^2); "
          "even parity: tan(pL) = -p/M, the spectra of (M, theta = 0) with the parities exchanged) for (M, L) = (1, 3), "''',
    '''          "(Richardson) the k = 0 levels at a4,0 = 0 (f = 1) equal the exact image spectra (odd fold condition: eps = 0 "
          "and sqrt(M^2 + (n pi/L)^2); even: tan(pL) = -p/M, the spectra of (M, theta = 0) with the fold conditions "
          "exchanged) for (M, L) = (1, 3), "''')
rep('''    out = [(8, tag, a4, 0.0) for tag in ("lam0", "lamp2", "lamm2") for a4 in (0.0, 1.0, 2.0)]
    out += [(136, tag, a4, 0.0) for tag in ("lamp2", "lamm2") for a4 in (0.0, 2.0)]
    out += [(8, "lamp1", a4, t) for a4 in (0.0, 2.0) for t in (0.01, 0.05)]
    out += [(136, "lamp1", 2.0, 0.05)]''',
    '''    nmid = int(params["particleNumbers"]["N_mid"])
    out = [(8, tag, a4, 0.0) for tag in ("lam0", "lamp2", "lamm2") for a4 in (0.0, 1.0, 2.0)]
    out += [(nmid, tag, a4, 0.0) for tag in ("lamp2", "lamm2") for a4 in (0.0, 2.0)]
    out += [(8, "lamp1", a4, t) for a4 in (0.0, 2.0) for t in (0.01, 0.05)]
    out += [(nmid, "lamp1", 2.0, 0.05)]''')
rep('''          "and the key sets of plus and image equal after the map (n2, j, parity, rank) -> (n2, -j, other parity, rank)%s"''',
    '''          "and the key sets of plus and image equal after the map (n2, j, fold condition, rank) -> (n2, -j, other fold "
          "condition, rank)%s"''')
rep('''          "%d ground states (N = 8: lam0, lamp2, lamm2 x a4,0 = 0, 1, 2; N = 136: lamp2, lamm2 x a4,0 = 0, 2), Richardson values: "''',
    '''          "%d ground states (N = 8: lam0, lamp2, lamm2 x a4,0 = 0, 1, 2; N = %d: lamp2, lamm2 x a4,0 = 0, 2), Richardson values: "''')
rep('''          "values" % (ng, worst_g, wid_g, TOL, per_grid_worst))''',
    '''          "values" % (ng, NMID_TXT, worst_g, wid_g, TOL, per_grid_worst))''')
rep('''          "%d Mermin states (N = 8, lamp1 x a4,0 = 0, 2 x T = 0.01, 0.05; N = 136, lamp1, a4,0 = 2, T = 0.05): levels and occupations, mu, "''',
    '''          "%d Mermin states (N = 8, lamp1 x a4,0 = 0, 2 x T = 0.01, 0.05; N = %d, lamp1, a4,0 = 2, T = 0.05): levels and occupations, mu, "''')
rep('''          "(S, Q, M_eff with opposite sign): worst %.3e (%s), tolerance %.0e" % (nt, worst_t, wid_t, TOL))''',
    '''          "(S, Q, M_eff with opposite sign): worst %.3e (%s), tolerance %.0e" % (nt, NMID_TXT, worst_t, wid_t, TOL))''')
rep('''                      "deflating as e^{-a4} b4^{1/2} = b4(0)^{1/2} e^{-a4/3}); lambda_hat fixed per tag, Vol_7(a4,0) = ell^3 v_t "
                      "e^{2 a4,0}; the Kohn-Sham states violate the source conditions of the a4 and b4 equations "''',
    '''                      "deflating as e^{-a4} b4^{1/2} = b4(0)^{1/2} e^{-a4/3}); lambda_hat fixed per tag, Vol_7(a4,0) = ell^3 v_t "
                      "e^{(5/3) a4,0}; the Kohn-Sham states violate the source conditions of the a4 and b4 equations "''')
# NMID_TXT: defined where specs are built in main()
rep('''    specs = spec_list(co, params)''', '''    specs = spec_list(co, params)
    NMID_TXT = int(params["particleNumbers"]["N_mid"])''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
