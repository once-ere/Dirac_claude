#!/usr/bin/env python3
"""UM-2 late cosmology: the CMB, the CNB and BAO from the order-epsilon (linear) metric of the four-dimensional
effective theory, solved with the Einstein-Boltzmann code CAMB.

The four-dimensional effective theory of the stabilised block is EXACT general relativity with Newton's constant
G_N = kappa/(8 pi V_perp G(k*)) and the cosmological term Lambda4 (the dimensional reduction of the Lovelock densities on
M4 x block gives G(k*) R4 + (topological GB4) + 0 x (cubic, vanishing in 4D) - 2 Lambda4: um2_background.py), so the
linear perturbations obey the standard Einstein-Boltzmann equations.  The model's particle content enters through:
  photons; one neutrino species nu_e (Dirac, m_nu = 0.05 eV, its right-handed partner never thermalised);
  the Psi_A fold band: two massless Weyl species with the neutrino's Z coupling (r^2 = 0.992), decoupled with the
  neutrinos (T = T_nu): N_eff = 3.044 in total;
  optionally the Psi_B fold band (two sterile Weyl species) if it was thermalised above the QCD crossover:
  Delta N_eff = 2 (7.25/g_s)^{4/3} (0.18 for g_s = 44.25, 0.14 for g_s = 53.25);
  baryons (u, d confined in p, n; omega_b), dark matter (the Psi_B odd quanta; omega_c), Lambda4 (flatness).
The comparison model is Planck 2018 LCDM (three neutrinos, sum m_nu = 0.06 eV).  theta_* is held at the Planck value
(H0 fitted), so the CMB peaks match and the BAO are a test.
Writes outputs/cosmology.json, figures/fig_cmb_*.png, fig_bao.png, reports/cosmology-checks.json.
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import FIG, OUT, Report, read_json, write_json  # noqa: E402

PLANCK = {'ombh2': 0.02237, 'omch2': 0.1200, 'cosmomc_theta': 1.04092e-2, 'tau': 0.0544, 'As': math.exp(3.044) * 1e-10,
          'ns': 0.9649}
# DESI DR2 BAO (DESI collaboration, arXiv:2503.14738, Table IV): z, DV/rd, DM/rd, DH/rd (value, error), r_MH
DESI = [
    ('BGS', 0.295, (7.942, 0.075), None, None, None),
    ('LRG1', 0.510, (12.720, 0.099), (13.588, 0.167), (21.863, 0.425), -0.459),
    ('LRG2', 0.706, (16.050, 0.110), (17.351, 0.177), (19.455, 0.330), -0.404),
    ('LRG3+ELG1', 0.934, (19.721, 0.091), (21.576, 0.152), (17.641, 0.193), -0.416),
    ('ELG2', 1.321, (24.252, 0.174), (27.601, 0.318), (14.176, 0.221), -0.434),
    ('QSO', 1.484, (26.055, 0.398), (30.512, 0.760), (12.817, 0.516), -0.500),
    ('Lya', 2.330, (31.267, 0.256), (38.988, 0.531), (8.632, 0.101), -0.431),
]


def run(name, num_massive, mnu, nnu, lmax=2600):
    import camb
    pars = camb.CAMBparams()
    pars.set_cosmology(ombh2=PLANCK['ombh2'], omch2=PLANCK['omch2'], cosmomc_theta=PLANCK['cosmomc_theta'], tau=PLANCK['tau'],
                       mnu=mnu, num_massive_neutrinos=num_massive, nnu=nnu, neutrino_hierarchy='degenerate')
    pars.InitPower.set_params(As=PLANCK['As'], ns=PLANCK['ns'])
    pars.set_for_lmax(lmax, lens_potential_accuracy=1)
    res = camb.get_results(pars)
    der = res.get_derived_params()
    cls = res.get_cmb_power_spectra(pars, CMB_unit='muK', raw_cl=False)['total']
    rd = der['rdrag']
    bao = []
    chi2 = 0.0
    for (tr, z, dv, dm, dh, r) in DESI:
        DM = res.angular_diameter_distance(z) * (1 + z)
        DH = 299792.458 / res.hubble_parameter(z)
        DV = (z * DM ** 2 * DH) ** (1.0 / 3.0)
        row = {'tracer': tr, 'z': z, 'DV_rd': DV / rd, 'DM_rd': DM / rd, 'DH_rd': DH / rd}
        if dm is None:
            chi2 += ((DV / rd - dv[0]) / dv[1]) ** 2
        else:
            d = np.array([DM / rd - dm[0], DH / rd - dh[0]])
            Cm = np.array([[dm[1] ** 2, r * dm[1] * dh[1]], [r * dm[1] * dh[1], dh[1] ** 2]])
            chi2 += float(d @ np.linalg.solve(Cm, d))
        bao.append(row)
    out = {'name': name, 'H0': pars.H0, 'omegam': (pars.ombh2 + pars.omch2 + pars.omnuh2) / (pars.H0 / 100) ** 2,
           'Neff': nnu, 'mnu_sum_eV': mnu, 'num_massive': num_massive,
           'theta_star_100': der['thetastar'], 'z_star': der['zstar'], 'r_star': der['rstar'], 'z_drag': der['zdrag'],
           'r_drag': rd, 'age_Gyr': der['age'], 'YHe': pars.YHe, 'bao': bao, 'bao_chi2': chi2, 'bao_npts': 13,
           'cl_TT_l': [[int(l), float(cls[l, 0])] for l in (2, 10, 30, 100, 220, 300, 540, 800, 1000, 1500, 2000, 2500)]}
    return out, cls


def main():
    rep = Report('cosmology-checks', 'UM-2: CMB (TT, EE), CNB and BAO of the four-dimensional effective theory with the UM-2 particle '
                 'content (CAMB), compared with Planck 2018 LCDM and DESI DR2 BAO')
    ew = read_json(os.path.join(OUT, 'electroweak.json'))
    Neff = ew['N_eff']
    lcdm, cl0 = run('Planck 2018 LCDM (3 nu, sum 0.06 eV)', 1, 0.06, 3.044)
    um2, cl1 = run('UM-2: nu_e (0.05 eV) + 2 Psi_A (massless), Psi_B not thermalised', 1, 0.05, Neff)
    dB = 2 * (7.25 / 44.25) ** (4.0 / 3.0)
    um2b, cl2 = run('UM-2 with the Psi_B fold band thermalised above the QCD crossover', 1, 0.05, Neff + dB)
    out = {'models': [lcdm, um2, um2b], 'Delta_Neff_PsiB_QCD': dB}
    # comparisons
    l = np.arange(cl0.shape[0])
    sel = (l >= 30) & (l <= 2500)
    dTT = np.max(np.abs(cl1[sel, 0] / cl0[sel, 0] - 1))
    dEE = np.max(np.abs(cl1[sel, 1] / cl0[sel, 1] - 1))
    # cosmic-variance-limited relative error of a single multipole: sqrt(2/(2l+1)); compare the rms deviation in bins of 50
    cv = np.sqrt(2.0 / (2 * l[sel] + 1))
    ratio = np.abs(cl1[sel, 0] / cl0[sel, 0] - 1) / cv
    ratio_b = np.abs(cl2[sel, 0] / cl0[sel, 0] - 1) / cv
    out['PsiB_variant_max_rel_dev_TT'] = float(np.max(np.abs(cl2[sel, 0] / cl0[sel, 0] - 1)))
    out['PsiB_variant_max_dev_in_cosmic_variance_units'] = float(np.max(ratio_b))
    # binned (Delta l = 50) significance of the Psi_B variant relative to LCDM in cosmic-variance units (full sky, TT only)
    chi2_cv = 0.0
    for lo_ in range(30, 2500, 50):
        mm = (l[sel] >= lo_) & (l[sel] < lo_ + 50)
        dev = np.mean(cl2[sel, 0][mm] / cl0[sel, 0][mm] - 1)
        err = np.sqrt(2.0 / np.sum(2 * l[sel][mm] + 1))
        chi2_cv += (dev / err) ** 2
    out['PsiB_variant_TT_chi2_cosmic_variance_full_sky'] = chi2_cv
    out['max_rel_dev_TT'] = float(dTT)
    out['max_rel_dev_EE'] = float(dEE)
    out['max_dev_in_cosmic_variance_units'] = float(np.max(ratio))
    rep.check('theta_star_matched', abs(um2['theta_star_100'] - lcdm['theta_star_100']) < 2e-4,
              '100 theta_* = %.5f (UM-2) and %.5f (LCDM); H0 = %.2f and %.2f km/s/Mpc' % (um2['theta_star_100'], lcdm['theta_star_100'],
                                                                                    um2['H0'], lcdm['H0']))
    rep.check('cmb_spectra_close_to_lcdm', dTT < 0.01 and dEE < 0.01,
              'UM-2 TT and EE spectra agree with Planck LCDM to %.2e and %.2e (relative, 30 <= l <= 2500), at most %.2f of the cosmic variance '
              'of a single multipole' % (dTT, dEE, np.max(ratio)))
    rep.check('bao_desi', um2['bao_chi2'] < 40,
              'DESI DR2 BAO chi^2 = %.2f for 13 measurements (LCDM with Planck parameters: %.2f; with thermalised Psi_B: %.2f)' % (
                  um2['bao_chi2'], lcdm['bao_chi2'], um2b['bao_chi2']))
    rep.check('psiB_variant_cmb_shift', True,
              'variant with the Psi_B fold band thermalised (N_eff = %.3f) at fixed Planck omega_b, omega_c, theta_*: TT changes by up to %.2e '
              '(%.1f cosmic-variance units per multipole; binned full-sky cosmic-variance chi^2 = %.0f): it is NOT a fit to the CMB; a joint '
              'CMB + BAO fit of this variant is OPEN' % (Neff + dB, out['PsiB_variant_max_rel_dev_TT'], out['PsiB_variant_max_dev_in_cosmic_variance_units'],
                                                         out['PsiB_variant_TT_chi2_cosmic_variance_full_sky']))
    rep.check('neff_and_helium', abs(um2['Neff'] - 3.044) < 1e-6,
              'N_eff = %.4f (BBN helium fraction Y_He = %.5f from the CAMB/BBN interpolation, LCDM %.5f)' % (um2['Neff'], um2['YHe'], lcdm['YHe']))
    out['CNB'] = ew['CNB']
    # figures
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(2, 2, figsize=(12, 7), gridspec_kw={'height_ratios': [3, 1]})
    ll = l[2:2501]
    for j, (lab, col) in enumerate([('TT', 0), ('EE', 1)]):
        axs[0, j].plot(ll, cl0[2:2501, col], 'k-', lw=1.2, label='Planck 2018 LCDM')
        axs[0, j].plot(ll, cl1[2:2501, col], 'C1--', lw=1.0, label='UM-2')
        axs[0, j].plot(ll, cl2[2:2501, col], 'C2:', lw=1.0, label='UM-2, Psi_B thermalised')
        axs[0, j].set_ylabel(r'$\ell(\ell+1)C_\ell/2\pi$ [$\mu$K$^2$] (%s)' % lab)
        axs[0, j].set_xscale('log')
        axs[0, j].legend(fontsize=8)
        axs[1, j].plot(ll, cl1[2:2501, col] / cl0[2:2501, col] - 1, 'C1-', lw=0.8)
        axs[1, j].plot(ll, cl2[2:2501, col] / cl0[2:2501, col] - 1, 'C2-', lw=0.8)
        axs[1, j].plot(ll, np.sqrt(2.0 / (2 * ll + 1)), 'k:', lw=0.6)
        axs[1, j].plot(ll, -np.sqrt(2.0 / (2 * ll + 1)), 'k:', lw=0.6)
        axs[1, j].set_xscale('log')
        axs[1, j].set_ylim(-0.05, 0.05)
        axs[1, j].set_xlabel(r'$\ell$')
        axs[1, j].set_ylabel('relative to LCDM')
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'fig_cmb_spectra.png'), dpi=130)
    plt.close(fig)
    fig, axs = plt.subplots(1, 3, figsize=(13, 3.6))
    for qi, (q, lab) in enumerate([('DV_rd', r'$D_V/r_d$'), ('DM_rd', r'$D_M/r_d$'), ('DH_rd', r'$D_H/r_d$')]):
        for mdl, st, lab_m in [(lcdm, 'k-', 'Planck 2018 LCDM'), (um2, 'C1--', 'UM-2'), (um2b, 'C2:', 'UM-2, Psi_B thermalised')]:
            zz = [b['z'] for b in mdl['bao']]
            axs[qi].plot(zz, [b[q] / math.sqrt(b['z']) for b in mdl['bao']], st, lw=1, label=lab_m)
        for (tr, z, dv, dm, dh, r) in DESI:
            dat = {'DV_rd': dv, 'DM_rd': dm, 'DH_rd': dh}[q]
            if dat is not None:
                axs[qi].errorbar([z], [dat[0] / math.sqrt(z)], yerr=[dat[1] / math.sqrt(z)], fmt='o', ms=4, color='C0',
                                 label='DESI DR2' if tr == 'LRG1' or (q == 'DV_rd' and tr == 'BGS') else None)
        axs[qi].set_xlabel('z')
        axs[qi].set_ylabel(lab + r'$/\sqrt{z}$')
    axs[0].legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'fig_bao.png'), dpi=130)
    plt.close(fig)
    write_json(os.path.join(OUT, 'cosmology.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
