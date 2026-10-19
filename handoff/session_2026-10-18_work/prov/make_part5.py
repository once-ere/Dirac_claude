#!/usr/bin/env python3
"""Generate part5.md: the table of the origin of every field equation FE-1..FE-136 (inventory id, title, status)."""
import json
import sys

INV = '/home/claude/dirac_claude/universe_model_2/docs_src/equations.json'
OUT = sys.argv[1]

# n: (how it was obtained and solved, verified by)
I = {
 1: ("metric variation of IN-2 and of the matter action: the author's notebook equations with a source (section 4); solved at order 0 through FE-38 to FE-40 and at order $\\epsilon$ through FE-49", "geo 4-12, 16-18; res 1"),
 2: ("definition (for spinors the variation with respect to the vielbein)", "ks8 2; ks592 2"),
 3: ("sum of the energy-momentum tensors of the terms of IN-1", "cpl 14; res 9, 11"),
 4: ("metric variation of IN-4 with $\\rho_{\\mathrm{stab}} \\propto f^{-8}$", "bg 10, 13, 15; res 1"),
 5: ("symmetrised vielbein variation of IN-5; for Kohn-Sham states it is FE-67", "ks8 2, 3; ks592 2-4; ksdm 3; ana 20"),
 6: ("vielbein variation of IN-11; used through ideal and degenerate gases with the $x_0$ masses", "th 1; cpl 14"),
 7: ("metric variation of IN-8", "bg 19; ks592 4"),
 8: ("metric variation of IN-13 at $y = -L$; its effect is part of the rest energies of $W^\\pm$, $Z$ and the fermions", "(no separate check)"),
 9: ("metric variation of IN-16 and IN-18 (the frame currents do not depend on the vielbein)", "cpl 13"),
 10: ("metric variation of IN-17", "cpl 15; res 12"),
 11: ("diffeomorphism invariance: the Bianchi identities of the Lovelock tensors", "geo 6-8; ks8 2; ks592 2"),
 12: ("variation of IN-5 and IN-16 to IN-18 with respect to $\\bar\\Psi$; reduced exactly to FE-56", "fld 1; cpl 6; ksp 5"),
 13: ("IN-7 evaluated on FE-31 (sympy, both halves of a period)", "geo 22-25"),
 14: ("variation of IN-11, IN-13, IN-16, IN-18 with respect to $\\bar Q_i$; solved by FE-56 to FE-60", "fld 1, 8, 12, 13; mass 11-13; flav 3"),
 15: ("as FE-14, with respect to $\\bar u_{Ri}$", "fld 9, 12, 13; mass 11-13; flav 3"),
 16: ("as FE-14, with respect to $\\bar d_{Ri}$; the tip matrix of the sector is the CKM matrix", "fld 9, 12, 13; mass 11-13; flav 3"),
 17: ("variation of IN-11, IN-13, IN-16 with respect to $\\bar\\ell_i$ (no I13 term)", "fld 8, 12, 13; mass 11-13; flav 3, 7"),
 18: ("as FE-17, with respect to $\\bar e_{Ri}$", "fld 9, 12, 13; mass 11-13"),
 19: ("as FE-17, with respect to $\\bar\\nu_{Ri}$ (gauge singlets)", "mass 11, 13; flav 3; cpl 10"),
 20: ("variation of IN-11 with respect to the gauge fields", "ew 1-4"),
 21: ("IN-8 and IN-17 combined", "cpl 15, 16; res 12"),
 22: ("variation of IN-8, IN-11, IN-17 with respect to the gluon field", "fld 14; mass 1, 3"),
 23: ("variation of IN-8, IN-11, IN-13, IN-17 with respect to the SU(2) field, in the unitary gauge", "fld 14, 15; mass 6-8"),
 24: ("as FE-23, with respect to the hypercharge field", "fld 14, 15"),
 25: ("FE-23 and FE-24 at linear order with IN-10", "ew 2-4; mass 3, 7, 8"),
 26: ("variation of IN-13 with respect to $\\Sigma$ (the Noether identity of the gauge symmetry)", "fld 16"),
 27: ("boundary terms of the variation at the fold and at the tip", "fld 15"),
 28: ("the record's fold and tip conditions; self-adjoint", "fld 5, 7; kss 1"),
 29: ("selection projector chosen so that each doublet has one left-handed and each singlet one right-handed Weyl zero mode", "fld 3-5, 8-10; ew 12"),
 30: ("IN-13 on the zero modes; self-adjoint for every complex matrix (sympy, 42 real variables); the tip matrices ASSUMED", "fld 12, 13; flav 3, 4"),
 31: ("the record's corrected metric (section 5) in the author's coordinates", "geo 1-3"),
 32: ("change of chart to $y$ (section 5)", "geo 1-3, 22"),
 33: ("Riemann tensor of FE-31 in both charts (sympy)", "geo 1-3"),
 34: ("pairing formula, coefficients $2^pp!$ and $-2^{p-1}p!$ (sympy)", "geo 4-12; bg 4"),
 35: ("FE-34 with FE-33 (sympy, four routes)", "geo 4, 6, 10, 13; bg 1, 4"),
 36: ("as FE-35", "geo 5, 7, 11, 14; bg 2, 4"),
 37: ("as FE-35", "geo 8, 12, 15; bg 3, 4"),
 38: ("FE-1 with FE-35 to FE-37, the author's weights and $\\Lambda$", "geo 16, 19; prim 1; res 1, 3"),
 39: ("as FE-38; integrated through the primordial era (DOP853)", "geo 17, 20; bg 14; prim 1-5; res 1, 3"),
 40: ("as FE-38; the $x_0$ and the extra-time components have the same left side, and the order-0 metric (one block scale) obeys their average with $\\bar p$", "geo 18, 21; bg 1-3, 14; res 1, 3"),
 41: ("FE-11 on FE-31", "bg 15; prim 1"),
 42: ("FE-38 to FE-40 with $\\mathcal{H}_f = 0$, $\\dot{\\mathcal{H}} = 0$", "geo 19-21; bg 5-9; res 1"),
 43: ("closed form (sympy)", "bg 10-13, 15; res 1, 48"),
 44: ("Jacobian of FE-39 and FE-40 at the static block", "bg 16, 17; prim 2; ana 22; res 2, 47"),
 45: ("linearisation with block-averaged sources", "bg 18; res 2"),
 46: ("exact algebraic numbers (sympy)", "bg 18, 19; res 46"),
 47: ("FE-45 with the second time derivative of $\\Delta K$ neglected", "bg 19; ksfb 1; res 2, 9"),
 48: ("dimensional reduction on the static block (sympy)", "bg 20-22; ksfb 2; ana 21; res 4"),
 49: ("the reduced action and the zero modes of the gauge fields", "bg 21, 22; ana 23; res 4, 37"),
 50: ("reduction of FE-22 to FE-25 (and of FE-1 for the transverse-traceless graviton) on the static block", "fld 14; mass 1-4; ana 1-7; ser 2; res 5"),
 51: ("natural boundary conditions of IN-15", "fld 15; mass 6, 7; res 5"),
 52: ("exact solution of FE-50: mpmath roots (30 to 60 digits), finite elements as a check", "mass 1-5, 9; flav 5; ana 2; res 5"),
 53: ("exact eigenfunctions of FE-50 with $\\beta = 0$", "mass 1, 2; ser 2; res 15"),
 54: ("exchange of the tower between two static sources", "ser 2; res 15"),
 55: ("fit of $\\beta_{\\mathrm{W}}$ by bisection in $\\ln\\beta_{\\mathrm{W}}$ (80 steps)", "mass 7, 8, 10; res 5, 13, 29, 30"),
 56: ("the record's reduction, re-derived exactly for all eight blocks with the author's matrices (sympy)", "fld 1, 2; alg 19-29"),
 57: ("exact solutions of FE-56 at $k = 0$", "fld 6-11; kss 2"),
 58: ("exact solutions of the doublet and singlet systems", "mass 11-13"),
 59: ("FE-58 in FE-30; mpmath roots, shooting (DOP853) as a check", "mass 11-14; ana 8, 9; res 6"),
 60: ("FE-58 in the three-generation FE-30; mpmath at 50 digits", "flav 3, 4, 7; res 6"),
 61: ("NuFIT 6.0 and PDG values (section 7)", "flav 1, 2, 6; res 33"),
 62: ("exact solution of FE-56 with $M = m_\\Psi$", "kss 1-3; ew 13; ana 12; res 7"),
 63: ("the record's block Hamiltonian with the mean fields FE-64; Galerkin in the free basis, Anderson mixing, Richardson in the basis size", "ksv 1, 2; ks8 1; ks592 1; cpl 1, 7; res 8"),
 64: ("the record's Hartree-plus-exchange fields of the contact term and the portal mean fields of IN-16 to IN-18", "ksp 1-4; cpl 1, 7, 13; res 8, 10, 11"),
 65: ("the record's definitions", "ksv 1, 2"),
 66: ("the record's functional", "ks8 3; ks592 3; ksdm 1"),
 67: ("FE-5 for Kohn-Sham states", "ksdm 2, 3; ks592 4; ana 19; res 9, 28"),
 68: ("from FE-66, FE-67 and FE-11", "ks8 2, 3; ks592 2, 3; res 8"),
 69: ("block form of FE-28 ($\\gamma^{x_0} = \\sigma_3$ in every block)", "alg 20; fld 5; ew 13"),
 70: ("reduction of IN-16 and IN-18 with the zero-mode profiles", "cpl 1, 3, 5-7, 9; ksp 1-3; res 10, 40"),
 71: ("reduction of IN-17 with the dark-matter orbital", "ksp 4; ana 17; res 10, 41"),
 72: ("first order in the mean fields (Hellmann-Feynman)", "cpl 1, 2, 13; res 11"),
 73: ("FE-72 for protons, neutrons and electrons", "cpl 13; res 11"),
 74: ("trace anomaly (Shifman, Vainshtein, Zakharov)", "cpl 13; res 11"),
 75: ("lattice-like shape below 1 GeV, leading order above", "cpl 13"),
 76: ("free part; Feynman-Hellmann at order $\\alpha_{\\mathrm{G}}$", "cpl 13; res 11, 22"),
 77: ("one loop from the $\\overline{\\mathrm{MS}}$ values at $m_{\\mathrm{Z}}$", "cpl 13"),
 78: ("FE-76 with FE-77; thermal suppression below $m_{\\mathrm{W}}$", "cpl 13"),
 79: ("FE-21 and FE-50 with the dark-matter scalar density; first-order perturbation theory (version 4)", "cpl 15; res 12, 45"),
 80: ("FE-47 with all species, iterated with the masses", "cpl 14; res 11"),
 81: ("$\\bar p = \\frac14\\,\\mathrm{d}p/\\mathrm{d}\\ln f$ at fixed temperature", "cpl 14; res 11, 39"),
 82: ("$g_{\\mathrm{G}}^2 \\propto f^{-4}$, $m_{\\mathrm{KK}} \\propto 1/f$, one loop", "cpl 14"),
 83: ("one loop; nucleon sigma terms", "cpl 12; res 52"),
 84: ("one-loop matching at the quark thresholds", "cpl 12; res 52"),
 85: ("FE-59 with localisations proportional to $f$", "ana 11; cpl 12; res 52"),
 86: ("net baryons in weak equilibrium; dark matter in equilibrium below $x = 40$", "cpl 13; res 11"),
 87: ("magnitudes of the computed terms", "ser 1-4; res 16"),
 88: ("Newtonian gauge in eight dimensions", "ser 1, 3; res 16"),
 89: ("Newtonian gauge (Ma and Bertschinger)", "cos 3"),
 90: ("CAMB 2.0.5 (default accuracy, lensing)", "cos 1, 3, 4, 8; res 14"),
 91: ("CAMB; cold (a Kohn-Sham quantum at rest has zero pressure)", "cos 3; ksdm 2"),
 92: ("CAMB", "cos 3, 4"),
 93: ("CAMB", "cos 3"),
 94: ("CAMB", "cos 3"),
 95: ("CAMB", "cos 3"),
 96: ("CAMB, the three mass states separately (masses iterated)", "cos 2, 6, 7; res 32, 34"),
 97: ("Planck 2018 parameters; $N_{\\mathrm{eff}} = 3.0432 + 0.0010$", "cos 1, 4, 6; res 35, 38"),
 98: ("from the CAMB solution", "cos 8; ser 1; res 14"),
 99: ("from the CAMB matter power spectrum", "cos 8; res 50"),
 100: ("$m_1$ and the ordering chosen, the splittings of NuFIT 6.0; $x_0$ eigenvalues of FE-59", "nu 1, 16; mass 11; res 32"),
 101: ("exchange of $W^\\pm$ and $Z$ far below their masses", "nu 2-5; ew 6-11"),
 102: ("tree level; the measured $G_{\\mathrm{F}}$", "ew 4, 16, 18, 19; res 13, 30"),
 103: ("forward scattering in an unpolarised medium", "nu 3-5, 11"),
 104: ("exact matrix exponentials; ordered products of layers", "nu 2-5; res 17"),
 105: ("analytic", "nu 2; res 17"),
 106: ("two-flavour conditions; the exact three-flavour root as a check", "nu 3, 5; res 17"),
 107: ("adiabatic formula; numerical evolution as a check", "nu 5; res 17"),
 108: ("two-flavour conditions", "nu 11; res 17"),
 109: ("leading order in $T/m_{\\mathrm{W}}$; Brent roots", "nu 6; res 18"),
 110: ("linearised (FE-117) and momentum averaged (FE-111)", "nu 8, 9, 12-14"),
 111: ("Escudero's method; LSODA from 20 MeV to 5 keV", "nu 8, 9; res 19"),
 112: ("Escudero's kernels with the radiatively corrected couplings", "nu 8, 9"),
 113: ("Bennett et al.", "nu 7"),
 114: ("Gauss-Legendre panels", "nu 7"),
 115: ("from FE-111; the precision value 3.0432 is adopted", "nu 8, 9; res 19, 35, 49"),
 116: ("definitions; axially symmetric gas", "nu 12, 13; res 20"),
 117: ("vectorised Newton iterations", "nu 12, 13; res 20"),
 118: ("analytic", "nu 13"),
 119: ("300-node discretisation; analytic growth", "nu 12, 14, 15; res 20"),
 120: ("adaptive quadrature (to $3\\times10^{-16}$ since version 4)", "nu 10; res 21, 34"),
 121: ("Gauss-Legendre quadrature with the $x_0$ masses", "th 1; res 22, 31, 39"),
 122: ("sums of FE-121", "th 1; res 22, 37"),
 123: ("smooth switch; instantaneous neutrino decoupling at 2 MeV", "th 1; res 22, 38"),
 124: ("implicit Radau on $\\ln Y_{\\mathrm{DM}}$", "th 3, 4; cpl 8; res 23"),
 125: ("Gondolo and Gelmini; adaptive quadrature", "th 2; res 23"),
 126: ("from FE-124", "th 3, 4; cpl 8; res 23, 36"),
 127: ("spin traces and polarisation sums of FE-70 and FE-71", "ana 13-16; cpl 8; res 23"),
 128: ("partial waves $^3P_0$ and $^3S_1$", "th 5-7; ana 16; cpl 8"),
 129: ("FE-70 with Maxwell-Boltzmann statistics; trapezoid rule", "cpl 4; res 24"),
 130: ("from FE-129", "cpl 4; cos 6, 7; res 24, 35"),
 131: ("Radau in the shifted variable $x - 2$ (version 4)", "cpl 10; res 25"),
 132: ("a Weyl $\\nu_R$ on a heavy Dirac fermion", "cpl 10; res 25"),
 133: ("entropy conservation with the heating factor", "cpl 10, 11; cos 5; res 49"),
 134: ("ratio of the I11 and I13 rates", "cpl 10; res 25"),
 135: ("IN-5 on the dark matter and the fold bands; Fierz coefficients not computed", "cpl 11; res 10, 26"),
 136: ("trapezoid rule from $T_{\\mathrm{max}}$ to the freeze-out", "cpl 11; res 26"),
}

inv = json.load(open(INV))
fe = [e for e in inv if e['id'].startswith('FE-')]
assert len(fe) == 136 and set(I) == set(range(1, 137))
lines = []
lines.append('# The field equations and their origin')
lines.append('')
lines.append(
 'The 136 field equations of UM-2 are the variations of the action of section 6 (FE-1 to FE-30), their exact reductions on '
 'the order-0 metric and the static block (FE-31 to FE-86), and the equations of the four-dimensional effective theory: '
 'the metric series and the linear perturbations (FE-87 to FE-99), the neutrinos (FE-100 to FE-120) and the thermal history '
 '(FE-121 to FE-136). The table gives, for each, its title and status (as in the inventory of the field equations), how it '
 'was obtained and solved, and the checks that verify it. The checks are named by the report and their number in the '
 'catalogue of section 9: alg (`um2_algebra.py`), geo (`um2_geometry.py`), bg (`um2_background.py`), fld (`um2_fields.py`), '
 'mass (`um2_spectra.py`), flav (`um2_flavour.py`), nu (`um2_neutrino.py`), ksv, kss, ks8, ks592, ksdm, ksp, ksfb '
 '(`um2_ks_jobs.py` validate, spectrum, ground8, ground592, darkmatter, portals, feedback), ew (`um2_electroweak.py`), '
 'prim (`um2_primordial.py`), cos (`um2_cosmology.py`), ana (`um2_analysis.py`), th (`um2_thermal.py`), cpl '
 '(`um2_coupled.py`), ser (`um2_series.py`) and res (`um2_residuals.py`, version 4: res 1 to 26 are the residuals of the '
 'solution in its equations, res 27 to 52 the links in concert). The field equations that this document uses are written '
 'out where they are used (FE-1, FE-31, FE-32, FE-56, FE-64 to FE-66 in sections 4 and 5; FE-2, FE-47, FE-55, FE-67, FE-75, '
 'FE-76, FE-79, FE-102, FE-115, FE-120 to FE-123 and FE-131 in section 10).')
lines.append('')
lines.append('| FE | field equation (status) | how it was obtained and solved | verified by |')
lines.append('|:------|:-------------------------|:----------------------------------------|:------------------------|')
for e in fe:
    n = int(e['id'][3:])
    how, chk = I[n]
    lines.append('| %s | %s (%s) | %s | %s |' % (e['id'], e['title'], e['status'], how, chk))
lines.append('')
open(OUT, 'w').write('\n'.join(lines) + '\n')
print('written', OUT, len(lines))
