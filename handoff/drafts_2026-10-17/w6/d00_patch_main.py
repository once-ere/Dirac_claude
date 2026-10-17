"""W6 draft: dirac16complex00/python/derive_eos.py, the texts of main() and the remaining check names for the corrected
metric.  Applied to the scratch copy only."""
from pathlib import Path

p = Path(__file__).with_name("d00") / "python" / "derive_eos.py"
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('check("M2_tangent_exact_b4",', 'check("M2_tangent_exact",')
rep('check("M3_tangent_exact_b4",', 'check("M3_tangent_exact",')
rep('''        "metric": "the author's metric with b4(x4) (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[97]-In[102]): g = diag(cot^2 z, e^{2 a4} sin^{1/3} z (x3), -1, -e^{-2 a4} b4 sin^{1/3} z (x3)); b4 is a function of x4 (never 1); the history of the numbers is a4 = H x4, b4 = b4(0) e^{(4/3) H x4} (beta = 4/3, the branch of the author's weights for a source without T^x4_x0); the formulas hold for every a4(x4), b4(x4)",''',
    '''        "metric": "the corrected primordial metric of 2026-10-16 (version 2; Revision/SPEC.md section 1): g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real; b4 is a function of x4; the history of the numbers is the record's a4 = H x4, b4 = e^{(4/3) H x4} (beta = 4/3), a PRESCRIBED background (it needs the source exponentialHistory.authorWeights.historySource_kappaT_minus_Lam); the formulas hold for every a4(x4), b4(x4)",''')
# the ghost reading: the window of the condensate on the history, computed
a_in = (mp_382 := None)
rep('''    theory = {''', '''    win_in = mp.power(mp.mpf(382) / 441, mp.mpf(3) / 5)     # |u| = (382/441) a^(-5/3) reaches 1
    win_out = mp.power(mp.mpf(191) / 441, mp.mpf(3) / 5)    # |u| reaches 2: the condensate energy m S (1 + u/2) vanishes
    theory = {''')
rep('''With positive-energy components of real frequency only (for an extra-time mode: before its turning point a_*), w_eff(N1) >= 0 and w_eff(N2) >= -1/3 on the history b4 ~ a^(4/3) (theorem of section wkb): no dark-energy value under either normalisation from such components; reaching the Unite w0 with them needs a ghost-like sector larger than the positive energy. The exception is a condensate with lambda < 0 and m S > 0 (positive energy, attractive self-interaction; not a mode gas): its ratio w is below -1 exactly while lambda S/m lies in (-2, -1) (condensate_phantom_interval), and because w_eff(N2) = -1 + (beta/2)(1 + w) (condensate_observer_b4) the observer then reads w_eff(N2) < -1 as well; on the history lambda S/m ~ e^(-2 a4) drifts into that window toward the past (for lambda S/m = -382/441 today: from a = sqrt(382/441) = 0.9307 back to a = sqrt(191/441) = 0.6581, where its energy m S (1 + lambda S/(2 m)) vanishes). Its value -382/441 is CHOSEN, and no source of the history selects a condensate.",''',
    '''With positive-energy components of real frequency only (for an extra-time mode: before its turning point a_*), w_eff(N1) >= 0 and w_eff(N2) >= -4/9 on the record's history b4 ~ a^(4/3) (theorem of section wkb): no dark-energy value under either normalisation from such components; reaching the Unite w0 with them needs a ghost-like sector larger than the positive energy. The exception is a condensate with lambda < 0 and m S > 0 (positive energy, attractive self-interaction; not a mode gas): its ratio w is below -1 exactly while lambda S/m lies in (-2, -1) (condensate_phantom_interval), and because w_eff(N2) = (5/9)(1 + w) - 1 (condensate_observer) the observer then reads w_eff(N2) < -1 as well; on the history lambda S/m ~ e^(-(5/3) a4) drifts into that window toward the past (for lambda S/m = -382/441 today: from a = (382/441)^(3/5) = " + num(win_in) + " back to a = (191/441)^(3/5) = " + num(win_out) + ", where its energy m S (1 + lambda S/(2 m)) vanishes). Its value -382/441 is CHOSEN, and no source of the history selects a condensate (condensate_cannot_source_history).",''')
p.write_text(t.replace("a_in = (mp_382 := None)\n", ""), encoding="utf-8", newline="\n")
print("ok")
