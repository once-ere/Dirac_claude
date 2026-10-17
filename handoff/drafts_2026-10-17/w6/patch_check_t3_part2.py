"""W6 draft, part 2 of check_t3.py for the corrected metric (applied to the copy given as argv[1])."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''          "chi' = N chi, N = M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1 (ks-theory.json blockEquation.ode): "
          "sigma2 N_j(M) sigma2 = N_(-j)(-M) exactly")''',
    '''          "chi' = f N chi, N = M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1 (ks-theory.json blockEquation.ode; f > 0 "
          "the hidden scale): sigma2 N_j(M) sigma2 = N_(-j)(-M) exactly, so sigma2 (f N_j(M)) sigma2 = f N_(-j)(-M)")''')
rep('''    # 4. brane parities, current, norm''', '''    # 4. the fold conditions, current, norm''')
rep('''    check("T3.brane_parities_exchanged", par and curok and normok,
          "brane (ASSUMED Z2 orbifold of ks-theory.json): even chi2(0) = 0, odd chi1(0) = 0, i.e. (1 -+ sigma3) "
          "chi(0) = 0; sigma2 (1 - sigma3) sigma2 = 1 + sigma3: the map exchanges the parities (both are part of the "
          "problem); the boundary current -i j phi^dagger sigma1 chi and the norm are invariant under (chi, j) -> "
          "(sigma2 chi, -j), so self-adjointness and the orbital normalisation carry over")''',
    '''    fold = ks["boundaryConditions"]["fold"]
    fold_ok = "same chi(y) on both halves" in fold["statement"] and "w = 1/2" in fold["statement"] and "ASSUMED" in fold["status"]
    check("T3.fold_conditions_exchanged", par and curok and normok and fold_ok,
          "the fold (ks-theory.json boundaryConditions.fold: the fold cos z = 0 joins the two halves of a cell, a spinor "
          "continuous across it has the same chi(y) on both halves, so there is no mirror copy; self-adjointness gives "
          "(1 - Q(theta)) chi(0) = 0, and the record fills theta = 0 (chi2(0) = 0) and theta = pi (chi1(0) = 0) together, "
          "w = 1/2, ASSUMED): sigma2 (1 - sigma3) sigma2 = 1 + sigma3, so the map exchanges the two fold conditions (both are "
          "part of the problem); the boundary current -i j phi^dagger sigma1 chi and the norm are invariant under (chi, j) "
          "-> (sigma2 chi, -j), so self-adjointness and the orbital normalisation carry over")''')
# remove the Z2 mirror check (a statement of the withdrawn orbifold)
start = t.index("    # 10. the ASSUMED Z2 mirror P_A")
end = t.index("    # 11. numerical confirmation (data, not a proof)")
t = t[:start] + t[end:]
rep('''                 ("T3_brane_parities_exchanged", "T3.brane_parities_exchanged"),''',
    '''                 ("T3_fold_conditions_exchanged", "T3.fold_conditions_exchanged"),''')
rep('''                 ("T3_exact_k0_spectra", "T3.exact_k0_spectra"), ("T3_Gamma_is_the_block_map", "T3.Gamma_is_the_block_map"),
                 ("T3_z2_mirror_copy_carries_minus_m_plus_lambda", "T3.z2_mirror_copy_carries_minus_m_plus_lambda")]''',
    '''                 ("T3_exact_k0_spectra", "T3.exact_k0_spectra"), ("T3_Gamma_is_the_block_map", "T3.Gamma_is_the_block_map")]''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok (part 2)")
