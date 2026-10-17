"""W6 draft: Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls for the corrected metric (copy argv[1])."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''   The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0], z = 6 H x0
   (brane y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra times.''',
    '''   The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln|sin z|/(6 H) in [-L, 0], z = 6 H x0 real
   (the fold cos z = 0 at y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra
   times.  The metric is the corrected primordial metric of 2026-10-16 (version 2; SPEC section 1).''')
rep('''$revDir = ExpandFileName[FileNameJoin[{$t3Dir, "..", ".."}]];''',
    '''$revDir = If[StringQ[Environment["REVISION_DIR"]], Environment["REVISION_DIR"], ExpandFileName[FileNameJoin[{$t3Dir, "..", ".."}]]];''')
rep('''hk0[jj_, M_, c_] := jj (-I s1 . D[c, y] + M s2 . c);''', '''hk0[jj_, M_, c_] := jj (-I s1 . D[c, y]/fh + M s2 . c);''')
rep('''hB[j_, M_, chi_] := j (-I s1 . D[chi, y] + M s2 . chi + kap[y] k s3 . chi) + vv[y] chi;''',
    '''hB[j_, M_, chi_] := j (-I s1 . D[chi, y]/fh + M s2 . chi + kap[y] k s3 . chi) + vv[y] chi;''')
rep('''the levels with eps > 0 of the lambda = 0 problem plus the k = 0 brane zero modes''',
    '''the levels with eps > 0 of the lambda = 0 problem plus the k = 0 fold zero modes''')
rep('''  "coordinates" -> "the author's coordinates {x0, ..., x7}: x0 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0] (brane y = 0, tip y = -L);''',
    '''  "coordinates" -> "the author's coordinates {x0, ..., x7}: x0 = hidden direction, y = ln|sin z|/(6 H) in [-L, 0], z = 6 H x0 real (the fold cos z = 0 at y = 0, tip y = -L);''')
rep('''  "background" -> "T3 holds at every fixed slice a4,0 = a4(x4), b4,0 = b4(x4) of the author's metric with b4(x4) (b4 is never 1; it does not enter the block Hamiltonians) and uses no history.''',
    '''  "background" -> "T3 holds at every fixed slice a4,0 = a4(x4), b4,0 = b4(x4) of the corrected primordial metric (a4 and b4 enter the block Hamiltonians only through the positive constants f = e^(-a4) b4^(1/2) and kappa = e^(-a4) of the slice) and uses no history.''')
rep('''the proof uses it for the image through 'both j and both parities are part of each problem' without showing''',
    '''the proof uses it for the image through 'both j and both fold conditions are part of each problem' without showing''')
rep('''and the brane zero mode goes to the brane zero mode of the image in its boundary conditions.",''',
    '''and the fold zero mode goes to the fold zero mode of the image in its boundary conditions.",''')
rep('''    "The Z2 brane is ASSUMED; the tip condition is a choice and T3 needs the transformed tip Pi - theta; the filling convention is a CONVENTION whose justification is OPEN.",''',
    '''    "Filling both fold conditions is ASSUMED (the corrected metric has no mirror copy); the tip condition is a choice and T3 needs the transformed tip Pi - theta; the filling convention is a CONVENTION whose justification is OPEN.",''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
