"""W6 draft: Revision/pairing/kohn_sham/wolfram/verify_t3.wls for the corrected metric, applied to the COPY argv[1]."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''$revDir = ExpandFileName[FileNameJoin[{$t3Dir, "..", ".."}]];''',
    '''$revDir = If[StringQ[Environment["REVISION_DIR"]], Environment["REVISION_DIR"], ExpandFileName[FileNameJoin[{$t3Dir, "..", ".."}]]];''')
rep('''(* the block Hamiltonian of ks-theory.json blockEquation: h_j = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v *)
hBlock[j_, M_, k_, chi_] := j (-I s1 . D[chi, y] + M[y] s2 . chi + kap[y] k s3 . chi) + vv[y] chi;''',
    '''(* the block Hamiltonian of ks-theory.json blockEquation: h_j = j[-(i/f) sigma1 d_y + M sigma2 + kappa k sigma3] + v, f > 0 the
   hidden scale (a constant on a slice) *)
hBlock[j_, M_, k_, chi_] := j (-I s1 . D[chi, y]/fh + M[y] s2 . chi + kap[y] k s3 . chi) + vv[y] chi;''')
rep('''  "for arbitrary functions M(y), kappa(y), v(y), any k and both block types j = +-1: h_(-j)(-M, k, v) (sigma2 chi) = sigma2 h_j(M, k, v) chi as differential operators''',
    '''  "for arbitrary functions M(y), kappa(y), v(y), any k, any hidden scale f > 0 and both block types j = +-1: h_(-j)(-M, k, v) (sigma2 chi) = sigma2 h_j(M, k, v) chi as differential operators''')
rep('''  "the shooting form chi' = N chi with N = M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1 (ks-theory.json blockEquation.ode): sigma2 N_j(M, k, eps) sigma2 = N_(-j)(-M, k, eps) exactly''',
    '''  "the shooting form chi' = f N chi with N = M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1 (ks-theory.json blockEquation.ode): sigma2 N_j(M, k, eps) sigma2 = N_(-j)(-M, k, eps) exactly''')
rep('''addCheck["T3_brane_parities_exchanged",''', '''foldSt = Lookup[Lookup[Lookup[ks, "boundaryConditions", <||>], "fold", <||>], "statement", ""];
foldOk = StringContainsQ[foldSt, "same chi(y) on both halves"] && StringContainsQ[foldSt, "w = 1/2"];
addCheck["T3_fold_conditions_exchanged",''')
rep('''  zeroQ[jCur[-j, s2 . ph, s2 . ch] - jCur[j, ph, ch]] && zeroQ[Conjugate[s2 . ch] . (s2 . ch) - Conjugate[ch] . ch],
  "brane (ASSUMED Z2 orbifold, ks-theory.json boundaryConditions.brane): even parity chi2(0) = 0 and odd parity chi1(0) = 0, i.e. (1 -+ gamma^(x0)) chi(0) = 0 with gamma^(x0) = sigma3 in every block; sigma2 (1 - sigma3) sigma2 = 1 + sigma3, so the map exchanges the two parities (both are solved and filled together in the Kohn-Sham record, so the set of boundary problems is mapped onto itself)''',
    '''  zeroQ[jCur[-j, s2 . ph, s2 . ch] - jCur[j, ph, ch]] && zeroQ[Conjugate[s2 . ch] . (s2 . ch) - Conjugate[ch] . ch] && foldOk,
  "the fold (ks-theory.json boundaryConditions.fold: the fold cos z = 0 joins the two halves of a cell, a spinor continuous across it has the same chi(y) on both halves, so there is no mirror copy; the record fills both fold conditions, theta = 0: chi2(0) = 0 and theta = Pi: chi1(0) = 0, w = 1/2, ASSUMED), i.e. (1 -+ gamma^(x0)) chi(0) = 0 with gamma^(x0) = sigma3 in every block; sigma2 (1 - sigma3) sigma2 = 1 + sigma3, so the map exchanges the two fold conditions (both are solved and filled together, so the set of boundary problems is mapped onto itself)''')
rep('''(* per-orbital densities of ks-theory.json densities.perOrbital (P = e^(-6 H y)/(ell^3 v_t) cancels) *)''',
    '''(* per-orbital densities of ks-theory.json densities.perOrbital (P = e^(-3 H y)/Vol_7 cancels) *)''')
rep('''(general complex chi, eps, occupation f, degeneracy g, momentum k, weight w = w_Z2)''',
    '''(general complex chi, eps, occupation f, degeneracy g, momentum k, weight w of the two fold conditions)''')
rep('''the integrand of E_KS = sum g f eps - 2 Vol_7 int e^(6Hy) e_int''', '''the integrand of E_KS = sum g f eps - 2 Vol_7 int e^(3Hy) e_int''')
rep('''Omega = -T sum g ln(1 + e^(-(eps - mu)/T)) - 2 Vol_7 int e^(6Hy) e_int''', '''Omega = -T sum g ln(1 + e^(-(eps - mu)/T)) - 2 Vol_7 int e^(3Hy) e_int''')
rep('''Psi_16 = e^(-i eps x4) e^(i k x1) e^(-3 H y) b4^(-3/4) V_beta chi(y)/sqrt(ell^3 v_t) (ks-theory.json sectorAndAnsatz.orbital16; up to the phase s2), applied at the same point; Gamma is constant, so the map commutes with the factors e^(-3 H y) b4^(-3/4) of the author's metric with b4(x4)"];''',
    '''Psi_16 = e^(-i eps x4) e^(i k x1) e^(-(3/2) H y) e^(a4/2) b4^(-1) V_beta chi(y)/sqrt(ell^3 v_t) (ks-theory.json sectorAndAnsatz.orbital16; up to the phase s2), applied at the same point; Gamma is constant, so the map commutes with the half-density factor e^(-(3/2) H y) e^(a4/2) b4^(-1) of the corrected metric"];''')
start = t.index('(* the ASSUMED Z2 orbifold: P_A chi(y) = sigma3 chi(-y) *)')
end = t.index('(* ------------------------------------------------------------------ theorem record *)')
t = t[:start] + t[end:]
rep('''  "coordinates" -> "the author's coordinates {x0, ..., x7}: x0 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0] (brane y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times",''',
    '''  "coordinates" -> "the author's coordinates {x0, ..., x7}: x0 = hidden direction, y = ln|sin z|/(6 H) in [-L, 0], z = 6 H x0 real (the fold cos z = 0 at y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times",''')
rep('''    "H1 (the problem): the instantaneous Kohn-Sham problem of Revision/kohn_sham/ks-theory.json at a fixed slice a4,0 = a4(x4), b4,0 = b4(x4) of the author's metric with b4(x4) (SPEC section 1; b4 is never 1; b4 does not enter h_j and enters the proper densities only through the cell volume Vol_7, ks-theory.json sectorAndAnsatz.instantaneousProblem): good sector (no extra-time momentum), 3-torus lattice of momenta k, block Hamiltonians h_j = j[-i sigma1 d_y + M_eff(y) sigma2 + kappa(y) k sigma3] + v_v(y) on y in [-L, 0], j = +-1, four blocks (s2, s3) per j",''',
    '''    "H1 (the problem): the instantaneous Kohn-Sham problem of Revision/kohn_sham/ks-theory.json at a fixed slice a4,0 = a4(x4), b4,0 = b4(x4) of the corrected primordial metric of 2026-10-16 (SPEC section 1; a4 and b4 enter h_j through the hidden scale f = e^(-a4) b4^(1/2) and kappa = e^(-a4), positive constants on a slice, and the proper densities through the cell volume Vol_7): good sector (no extra-time momentum), 3-torus lattice of momenta k, block Hamiltonians h_j = j[-(i/f) sigma1 d_y + M_eff(y) sigma2 + kappa k sigma3] + v_v(y) on y in [-L, 0], j = +-1, four blocks (s2, s3) per j",''')
rep('''    "H3 (the brane, ASSUMED): the Z2 mirror (orbifold) construction at y = 0 of ks-theory.json boundaryConditions.brane; both brane parities (chi2(0) = 0 and chi1(0) = 0) are solved and filled together with the weight w_Z2 = 1/2",''',
    '''    "H3 (the fold, ASSUMED): the fold cos z = 0 joins the two halves of a cell (ks-theory.json boundaryConditions.fold; the same chi(y) on both halves, no mirror copy); both fold conditions (chi2(0) = 0 and chi1(0) = 0) are solved and filled together with the weight w = 1/2",''')
rep('''    "S1: (chi, j) -> (sigma2 chi, -j) at the same k, i.e. Psi_16 -> Gamma Psi_16 (the chirality, up to the phase s2 per block), maps every eigen-orbital of h_j with (M_eff, v_v) onto an eigen-orbital of h_(-j) with (-M_eff, v_v) at the SAME level eps, and exchanges the brane parities",''',
    '''    "S1: (chi, j) -> (sigma2 chi, -j) at the same k, i.e. Psi_16 -> Gamma Psi_16 (the chirality, up to the phase s2 per block), maps every eigen-orbital of h_j with (M_eff, v_v) onto an eigen-orbital of h_(-j) with (-M_eff, v_v) at the SAME level eps, and exchanges the two fold conditions",''')
rep('''    "S4: EQUAL Kohn-Sham levels with their degeneracies, occupations, chemical potential, particle number, entropy, Kohn-Sham energy E_KS, grand potential Omega and free energy F, and equal energy-momentum profiles rho(y), p3(y), p_t(y), p0(y) (also for the exact-Fock diagnostic); S(y) and Q(y) change sign",
    "S5: inside the ASSUMED Z2 orbifold the mirror copy of a self-consistent state carries (-m, +lambda) (P_A symmetry of the doubled problem), consistent with S3"},''',
    '''    "S4: EQUAL Kohn-Sham levels with their degeneracies, occupations, chemical potential, particle number, entropy, Kohn-Sham energy E_KS, grand potential Omega and free energy F, and equal energy-momentum profiles rho(y), p3(y), p_t(y), p0(y) (also for the exact-Fock diagnostic); S(y) and Q(y) change sign"},''')
rep('''    "sigma2 Q(theta) sigma2 = Q(Pi - theta), sigma2 (1 - sigma3) sigma2 = 1 + sigma3; the boundary current and the norm are invariant (T3_tip_condition_map, T3_brane_parities_exchanged)",''',
    '''    "sigma2 Q(theta) sigma2 = Q(Pi - theta), sigma2 (1 - sigma3) sigma2 = 1 + sigma3; the boundary current and the norm are invariant (T3_tip_condition_map, T3_fold_conditions_exchanged)",''')
rep('''    "the map is a bijection between the eigen-orbitals of the two problems with equal eps (both j and both parities are part of each problem)''',
    '''    "the map is a bijection between the eigen-orbitals of the two problems with equal eps (both j and both fold conditions are part of each problem)''')
rep('''    "independent confirmation on exactly solvable data: equal k = 0 spectra level by level, and a different spectrum for the untransformed tip (T3_exact_k0_spectra); the 2 x 2 map is the 16-component chirality Gamma in the block basis (T3_Gamma_is_the_block_map); the Z2 mirror copy (T3_z2_mirror_copy_carries_minus_m_plus_lambda)"},''',
    '''    "independent confirmation on exactly solvable data: equal k = 0 spectra level by level, and a different spectrum for the untransformed tip (T3_exact_k0_spectra); the 2 x 2 map is the 16-component chirality Gamma in the block basis (T3_Gamma_is_the_block_map)"},''')
rep('''    "The brane: the Z2 mirror construction at y = 0 is ASSUMED (ks-theory.json); the tip condition is a choice, and T3 needs the transformed tip angle Pi - theta.",''',
    '''    "The fold: filling both fold conditions is ASSUMED (ks-theory.json); the corrected metric has no mirror copy (both halves of a cell carry the same state), so T3 relates two Kohn-Sham problems, not a universe and its mirror image; the tip condition is a choice, and T3 needs the transformed tip angle Pi - theta.",''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
