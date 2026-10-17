"""W6 draft: Revision/pairing/wolfram/verify_pairing.wls and RevisionPairing.wl for the corrected metric (applied to the
copies in argv[1], a folder holding both): the corrected vielbein, sqrt|g| = e^-a4 b4^2 cot z sin^(1/2) z, the fold
instead of the Z2 brane, the not-established list with the tokens of check_pairing.py ('across the fold',
'degenerate'), and REVISION_DIR for a copy outside the repository."""
import sys
from pathlib import Path

d = Path(sys.argv[1])
p = d / "verify_pairing.wls"
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''         (m, lambda) -> (-m, lambda), L -> +L; in the metric of SPEC section 1 the Z2 mirror across the
         patch end z = 6 H x0 = pi/2 of the hidden coordinate;''',
    '''         (m, lambda) -> (-m, lambda), L -> +L; in the corrected metric of SPEC section 1 the reflection
         z -> pi - z across the fold z = 6 H x0 = pi/2 of the hidden coordinate (an isometry between the two
         halves of a cell);''')
rep('''   in four gravitational fields: the metric of SPEC section 1 with b4(x4) ("primordial"), its mirror patch, a''',
    '''   in four gravitational fields: the corrected metric of SPEC section 1 ("primordial"), its mirror patch, a''')
rep('''$revisionDir = ExpandFileName[FileNameJoin[{$pairingDir, ".."}]];''',
    '''$revisionDir = If[StringQ[Environment["REVISION_DIR"]], Environment["REVISION_DIR"], ExpandFileName[FileNameJoin[{$pairingDir, ".."}]]];''')
rep('''(* the author's metric with b4[x4] in the three extra-time components (SPEC section 1; b4 > 0, never 1) *)
sb = Sqrt[RPb4[x4]]; sqrtgPrim = Cos[zz] RPb4[x4]^(3/2);
EPrim = DiagonalMatrix[{Cot[zz], E^RPa4[x4] sx, E^RPa4[x4] sx, E^RPa4[x4] sx, 1, E^-RPa4[x4] sb sx, E^-RPa4[x4] sb sx, E^-RPa4[x4] sb sx}];
gAuthor = DiagonalMatrix[{Cot[zz]^2, E^(2 RPa4[x4]) Sin[zz]^(1/3), E^(2 RPa4[x4]) Sin[zz]^(1/3), E^(2 RPa4[x4]) Sin[zz]^(1/3), -1,
  -E^(-2 RPa4[x4]) RPb4[x4] Sin[zz]^(1/3), -E^(-2 RPa4[x4]) RPb4[x4] Sin[zz]^(1/3), -E^(-2 RPa4[x4]) RPb4[x4] Sin[zz]^(1/3)}];''',
    '''(* the corrected primordial metric of SPEC section 1 (version 2 of 2026-10-16), written as the author writes it, with
   (Sin[z]^2)^(1/6) in the extra times; on the patches sin z > 0, so (Sin[z]^2)^(1/6) = Sin[z]^(1/3) = sx^2 *)
sb = Sqrt[RPb4[x4]]; ea = E^-RPa4[x4]; sqrtgPrim = E^-RPa4[x4] RPb4[x4]^2 Cot[zz] Sin[zz]^(1/2);
EPrim = DiagonalMatrix[{ea sb Cot[zz], E^RPa4[x4], E^RPa4[x4], E^RPa4[x4], 1, ea sb sx, ea sb sx, ea sb sx}];
gAuthor = DiagonalMatrix[{E^(-2 RPa4[x4]) RPb4[x4] Cot[zz]^2, E^(2 RPa4[x4]), E^(2 RPa4[x4]), E^(2 RPa4[x4]), -1,
  -E^(-2 RPa4[x4]) RPb4[x4] (Sin[zz]^2)^(1/6), -E^(-2 RPa4[x4]) RPb4[x4] (Sin[zz]^2)^(1/6), -E^(-2 RPa4[x4]) RPb4[x4] (Sin[zz]^2)^(1/6)}];''')
rep('''  "the diagonal vielbein e^a_mu = sqrt|g_mumu| (cot z for x0, e^a4 sin^(1/6) z for x1..x3, 1 for x4, e^-a4 b4^(1/2) sin^(1/6) z for x5..x7; z = 6 H x0 in (0, pi/2); a4 = a4(x4) real, b4 = b4(x4) > 0 arbitrary functions) gives E^T eta E = the author's metric of SPEC section 1 with b4(x4) exactly and sqrt|g| = det E = b4^(3/2) cos z"];''',
    '''  "the diagonal vielbein e^a_mu = sqrt|g_mumu| (e^-a4 b4^(1/2) cot z for x0, e^a4 for x1..x3, 1 for x4, e^-a4 b4^(1/2) sin^(1/6) z for x5..x7; z = 6 H x0 in (0, pi/2), where (sin^2 z)^(1/12) = sin^(1/6) z; a4 = a4(x4) real, b4 = b4(x4) > 0 arbitrary functions) gives E^T eta E = the corrected metric of SPEC section 1 exactly and sqrt|g| = det E = e^-a4 b4^2 cot z sin^(1/2) z"];''')
rep('''EMir = DiagonalMatrix[{-Cot[zz], E^RPa4[x4] sx, E^RPa4[x4] sx, E^RPa4[x4] sx, 1, E^-RPa4[x4] sb sx, E^-RPa4[x4] sb sx, E^-RPa4[x4] sb sx}];''',
    '''EMir = DiagonalMatrix[{-ea sb Cot[zz], E^RPa4[x4], E^RPa4[x4], E^RPa4[x4], 1, ea sb sx, ea sb sx, ea sb sx}];''')
rep('''(* F2. the Z2 mirror of the primordial field across z = pi/2 *)''',
    '''(* F2. the reflection of the primordial field across the fold z = pi/2 (the other half of the cell) *)''')
rep('''  "phi: x0 -> pi/(6H) - x0 (z -> pi - z) maps the patch z in (0, pi/2) onto the mirror patch (pi/2, pi) and is an isometry of the author's metric with b4(x4) (sin z and cot^2 z are invariant; a4 and b4 depend on x4 only); with the positive vielbein on both patches (e^0 = |cot z| dx0: cot z on the patch, -cot z on the mirror) the pulled-back mirror vielbein is R_0 e (the hidden frame direction reflected), and sqrt|g| = b4^(3/2) |cos z| is invariant. The brane z = pi/2 itself is degenerate (g_00 = cot^2 z = 0, sqrt|g| = 0); the mirror construction across it is the ASSUMED Z2 construction of SPEC section 7"];''',
    '''  "phi: x0 -> pi/(6H) - x0 (z -> pi - z) maps the patch z in (0, pi/2) onto the other half (pi/2, pi) of the cell and is an isometry of the corrected metric (sin z and cot^2 z are invariant; a4 and b4 depend on x4 only); with the positive vielbein on both patches (e^0 = e^-a4 b4^(1/2) |cot z| dx0: + cot z on the patch, - cot z on the mirror patch) the pulled-back mirror vielbein is R_0 e (the hidden frame direction reflected), and sqrt|g| = e^-a4 b4^2 |cot z| sin^(1/2) z is invariant. The fold z = pi/2 itself is degenerate (g_00 = e^-2a4 b4 cot^2 z = 0, sqrt|g| = 0); the two patches are the two halves of a cell (no Z2 orbifold), and no matching of the field across the fold is derived"];''')
rep('''    "primordial: the author's metric of SPEC section 1 with b4(x4) (a4(x4) real and b4(x4) > 0 arbitrary functions of x4; b4 is never 1) on the patch z in (0, pi/2), canonical spin connection from the diagonal vielbein",
    "mirror_patch: the same metric (with b4(x4)) on z in (pi/2, pi) with its own positive vielbein (e^0 = -cot z dx0)",''',
    '''    "primordial: the corrected primordial metric of SPEC section 1 (version 2 of 2026-10-16; a4(x4) real and b4(x4) > 0 arbitrary functions of x4) on the patch z in (0, pi/2), canonical spin connection from the diagonal vielbein",
    "mirror_patch: the same metric on the other half z in (pi/2, pi) of the cell with its own positive vielbein (e^0 = -e^-a4 b4^(1/2) cot z dx0)",''')
rep('''        "primordial field: the reflection is realised by the isometry phi: x0 -> pi/(6H) - x0 (z -> pi - z), the Z2 mirror across the patch end z = pi/2, with Psi'(phi(x)) = gamma^(x0) Psi(x); the brane z = pi/2 is a degenerate surface of the metric (g_00 = 0, sqrt|g| = 0) and the extension of the field to the mirror patch is the ASSUMED Z2 construction of SPEC section 7",''',
    '''        "primordial field: the reflection is realised by the isometry phi: x0 -> pi/(6H) - x0 (z -> pi - z) across the fold z = pi/2 between the two halves of a cell, with Psi'(phi(x)) = gamma^(x0) Psi(x); the fold is a degenerate surface of the metric (g_00 = 0, sqrt|g| = 0); the corrected metric has no Z2 orbifold, and no matching of the field across the fold is derived",''')
rep('''    "The Z2 brane: the mirror across z = pi/2 uses the ASSUMED Z2 construction of SPEC section 7; the metric is degenerate at z = pi/2 (g_00 = 0, sqrt|g| = 0), and no junction condition, brane tension or matching of the field across the brane is derived here.",''',
    '''    "The fold: T2 relates the two halves of a cell through the isometry z -> pi - z across the fold z = pi/2; the corrected metric has no Z2 orbifold (the Kohn-Sham record of SPEC section 7 fills both fold conditions, an ASSUMED convention), the metric is degenerate at z = pi/2 (g_00 = 0, sqrt|g| = 0), and no junction condition or matching of the field across the fold is derived here.",''')
rep('''    "The Kohn-Sham level (T3) is not established by this file; it is proved separately, with its own hypotheses (ASSUMED Z2 brane, instantaneous mean-field Kohn-Sham states), in Revision/pairing/kohn_sham/."}|>;''',
    '''    "The Kohn-Sham level (T3) is not established by this file; it is proved separately, with its own hypotheses (both fold conditions filled, ASSUMED; instantaneous mean-field Kohn-Sham states), in Revision/pairing/kohn_sham/."}|>;''')
p.write_text(t, encoding="utf-8", newline="\n")

q = d / "RevisionPairing.wl"
u = q.read_text(encoding="utf-8")
a = '''   Z2 mirror across the patch end z = pi/2 of the hidden coordinate) and the quantum-level reading.'''
assert u.count(a) == 1
u = u.replace(a, '''   reflection z -> pi - z across the fold z = pi/2 of the hidden coordinate) and the quantum-level reading.''')
a = '''RPb4::usage = "RPb4: the metric function b4[x4] > 0 of the three extra-time components (never 1; SPEC section 1).";'''
assert u.count(a) == 1
u = u.replace(a, '''RPb4::usage = "RPb4: the metric function b4[x4] > 0 of the corrected metric (SPEC section 1).";''')
q.write_text(u, encoding="utf-8", newline="\n")
print("ok")
