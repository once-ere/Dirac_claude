#!/usr/bin/env python3
"""UM-2 late cosmology: the CMB, the CNB and BAO from the order-epsilon (linear) metric of the four-dimensional
effective theory, solved with the Einstein-Boltzmann code CAMB.

The four-dimensional effective theory of the stabilised block is EXACT general relativity with Newton's constant
G_N = kappa/(8 pi V_perp G(k*)) and the cosmological term Lambda4 (the dimensional reduction of the Lovelock densities on
M4 x block gives G(k*) R4 + (topological GB4) + 0 x (cubic, vanishing in 4D) - 2 Lambda4: um2_background.py), so the
linear perturbations obey the standard Einstein-Boltzmann equations.  The model's particle content (three generations,
version of 2026-10-18) enters through:
  photons; the three neutrino mass eigenstates nu_1, nu_2, nu_3 (Dirac; masses 1.000, 8.712, 50.140 meV from um2_spectra.py:
  normal ordering, NuFIT 6.0 splittings, lightest mass 1 meV ASSUMED; the right-handed partners never thermalised), an
  incoherent mixture of mass eigenstates after decoupling, with N_eff = 3.0432 (the three-flavour Standard-Model value with
  non-instantaneous decoupling, QED corrections and oscillations; um2_neutrino.py reproduces it to 0.005), shared equally
  by the three eigenstates (CAMB degeneracy 3.0432/3 each; CAMB's mass of eigenstate i is m_i (3.0432/3)^{-1/4} so that the
  late-time density is m_i n_nu (3.0432/3)^{3/4});
  no dark radiation: the fold bands of dirac16complex are never thermalised (no tip Z portal, zero scalar density for I12,
  c_V = 0 for I11; um2_electroweak.py);
  variants with dark radiation: two Weyl species (a fold band) thermalised and decoupled with g_s = 105.75 (above the
  electroweak scale, Delta N_eff = 0.0958) or g_s = 61.75 (just above the QCD crossover, Delta N_eff = 0.1963);
  baryons (omega_b), dark matter (the odd quanta of Psi_A and Psi_B; omega_c), Lambda4 (flatness).
The comparison model is LCDM with the Planck 2018 parameters (CAMB defaults: one massive neutrino of 0.06 eV, N_eff = 3.044).
theta_* is held at the Planck value (H0 fitted), so the CMB peaks match and the BAO are a test.
Writes outputs/cosmology.json, figures/fig_cmb_spectra.png, fig_bao.png, reports/cosmology-checks.json.
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import FIG, OUT, Report, read_json, write_json  # noqa: E402
from um2_constants import INPUTS, NUFIT60_NO, SUM_MNU_BOUND_EV, val  # noqa: E402

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


KB_EV_PER_K = None     # set in main() from the constants


def nu_setup(pars, masses, neff_nu, dN):
    """Three distinct massive eigenstates, each with N_eff = neff_nu/3, plus dN massless species (dark radiation).  CAMB gives
    each massive eigenstate the density deg x rho_FD(m'; T_nu) with T_nu = (4/11)^{1/3} T_CMB; the physical heated spectrum has
    the number density n_nu deg^{3/4}, so m' = m deg^{-1/4} reproduces the late-time density m n_nu deg^{3/4}.  CAMB finds m'
    from omnuh2 x fraction by inverting the full (relativistic) density, so omnuh2 and the fractions are iterated until the
    three masses agree."""
    import camb
    deg = neff_nu / 3.0
    Tnu = pars.TCMB * (4.0 / 11.0) ** (1.0 / 3.0)
    target = np.array([m * deg ** -0.25 / (KB_EV_PER_K * Tnu) for m in masses])       # CAMB's m'/T_nu
    om = np.array([m * deg ** 0.75 for m in masses]) / camb.constants.neutrino_mass_fac
    pars.num_nu_massive = 3
    pars.nu_mass_eigenstates = 3
    pars.nu_mass_numbers = [1, 1, 1]
    pars.nu_mass_degeneracies = [deg] * 3
    pars.num_nu_massless = dN
    pars.share_delta_neff = False
    hist = []
    for it in range(60):
        pars.omnuh2 = float(np.sum(om))
        pars.nu_mass_fractions = list(om / np.sum(om))
        got = np.array(list(camb.get_background(pars, no_thermo=True).nu_masses)[:3])
        err = got / target - 1
        hist.append(float(np.max(np.abs(err))))
        if np.max(np.abs(err)) < 1e-11:
            break
        # d ln m'/d ln omega >= 1 (= 1 for a non-relativistic state): a damped Newton step in log space
        om = om * (target / got) ** 0.8
    return got * KB_EV_PER_K * Tnu, hist


def run(name, masses=None, neff_nu=3.044, dN=0.0, lmax=2600):
    """masses = None: LCDM with the CAMB defaults (one massive neutrino of 0.06 eV, N_eff = neff_nu, default 3.044)."""
    import camb
    pars = camb.CAMBparams()
    if masses is None:
        pars.set_cosmology(ombh2=PLANCK['ombh2'], omch2=PLANCK['omch2'], cosmomc_theta=PLANCK['cosmomc_theta'], tau=PLANCK['tau'],
                           mnu=0.06, num_massive_neutrinos=1, nnu=neff_nu, neutrino_hierarchy='degenerate')
        mcamb, hist = [0.06], []
    else:
        pars.set_cosmology(H0=67.0, ombh2=PLANCK['ombh2'], omch2=PLANCK['omch2'], tau=PLANCK['tau'], mnu=float(sum(masses)),
                           num_massive_neutrinos=3, nnu=neff_nu + dN, standard_neutrino_neff=neff_nu, neutrino_hierarchy='degenerate')
        mcamb, hist = nu_setup(pars, masses, neff_nu, dN)
        pars.set_H0_for_theta(PLANCK['cosmomc_theta'], cosmomc_approx=True)
    pars.InitPower.set_params(As=PLANCK['As'], ns=PLANCK['ns'])
    pars.set_for_lmax(lmax, lens_potential_accuracy=1)
    res = camb.get_results(pars)
    if masses is not None:          # the masses of the final run (after the H0 search), not those of the iteration
        mcamb = [float(x) * KB_EV_PER_K * pars.TCMB * (4.0 / 11.0) ** (1.0 / 3.0) for x in list(res.nu_masses)[:3]]
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
    nnu = pars.N_eff
    out = {'name': name, 'H0': pars.H0, 'omegam': (pars.ombh2 + pars.omch2 + pars.omnuh2) / (pars.H0 / 100) ** 2,
           'Neff': nnu, 'Neff_massive': float(sum(list(pars.nu_mass_degeneracies)[:pars.nu_mass_eigenstates])),
           'Neff_massless': pars.num_nu_massless, 'mnu_sum_eV': float(sum(masses)) if masses is not None else 0.06,
           'num_massive': pars.num_nu_massive, 'camb_masses_eV': [float(x) for x in mcamb], 'camb_mass_iteration': hist,
           'omnuh2': pars.omnuh2, 'omnuh2_camb_today': res.get_Omega('nu') * (pars.H0 / 100) ** 2,
           'theta_star_100': der['thetastar'], 'z_star': der['zstar'], 'r_star': der['rstar'], 'z_drag': der['zdrag'],
           'r_drag': rd, 'age_Gyr': der['age'], 'YHe': pars.YHe, 'bao': bao, 'bao_chi2': chi2, 'bao_npts': 13,
           'cl_TT_l': [[int(l), float(cls[l, 0])] for l in (2, 10, 30, 100, 220, 300, 540, 800, 1000, 1500, 2000, 2500)]}
    return out, cls


def main():
    global KB_EV_PER_K
    KB_EV_PER_K = val('k_B_eV_per_K')
    rep = Report('cosmology-checks', 'UM-2: CMB (TT, EE), CNB and BAO of the four-dimensional effective theory with the UM-2 particle '
                 'content of three generations (CAMB), compared with Planck 2018 LCDM and DESI DR2 BAO')
    nu = read_json(os.path.join(OUT, 'neutrino.json'))
    ew = read_json(os.path.join(OUT, 'electroweak.json'))
    masses = nu['masses_eV']
    Neff_nu = nu['N_eff_adopted']['value']
    dr = ew['Psi_A_thermalisation']['Delta_Neff_two_Weyl_species']
    dN_ew = dr['above the electroweak scale (Standard Model without a Higgs particle)']
    dN_qcd = dr['just above the QCD crossover (+ gluons, u, d, s, mu)']
    lcdm, cl0 = run('LCDM, Planck 2018 parameters (CAMB defaults: one massive neutrino 0.06 eV, N_eff = 3.044)')
    um2, cl1 = run('UM-2: nu_1, nu_2, nu_3 (1.000, 8.712, 50.140 meV), N_eff = 3.0432, no dark radiation', masses, Neff_nu, 0.0)
    um2e, cl2 = run('UM-2 + a fold band thermalised above the electroweak scale (Delta N_eff = %.4f)' % dN_ew, masses, Neff_nu, dN_ew)
    um2q, cl3 = run('UM-2 + a fold band thermalised above the QCD crossover (Delta N_eff = %.4f)' % dN_qcd, masses, Neff_nu, dN_qcd)
    # attribution of the small UM-2 - LCDM difference: each change separately
    _, cla = run('LCDM with N_eff = 3.0432', None, Neff_nu)
    _, clb = run('UM-2 neutrino masses with N_eff = 3.044', masses, 3.044, 0.0)
    out = {'models': [lcdm, um2, um2e, um2q], 'Delta_Neff_dark_radiation_EW': dN_ew, 'Delta_Neff_dark_radiation_QCD': dN_qcd}
    # comparisons
    l = np.arange(cl0.shape[0])
    sel = (l >= 30) & (l <= 2500)
    dTT = np.max(np.abs(cl1[sel, 0] / cl0[sel, 0] - 1))
    dEE = np.max(np.abs(cl1[sel, 1] / cl0[sel, 1] - 1))
    cv = np.sqrt(2.0 / (2 * l[sel] + 1))
    ratio = np.abs(cl1[sel, 0] / cl0[sel, 0] - 1) / cv

    def binned_chi2_cv(cla, clb):
        """binned (Delta l = 50) TT deviation of cla from clb in full-sky cosmic-variance units"""
        c2 = 0.0
        for lo_ in range(30, 2500, 50):
            mm = (l[sel] >= lo_) & (l[sel] < lo_ + 50)
            dev = np.mean(cla[sel, 0][mm] / clb[sel, 0][mm] - 1)
            err = np.sqrt(2.0 / np.sum(2 * l[sel][mm] + 1))
            c2 += (dev / err) ** 2
        return c2
    for key, cl in (('UM2', cl1), ('dark_radiation_EW', cl2), ('dark_radiation_QCD', cl3)):
        out[key + '_max_rel_dev_TT'] = float(np.max(np.abs(cl[sel, 0] / cl0[sel, 0] - 1)))
        out[key + '_max_dev_in_cosmic_variance_units'] = float(np.max(np.abs(cl[sel, 0] / cl0[sel, 0] - 1) / cv))
        out[key + '_TT_chi2_cosmic_variance_full_sky'] = binned_chi2_cv(cl, cl0)
    out['max_rel_dev_TT'] = float(dTT)
    out['max_rel_dev_EE'] = float(dEE)
    out['attribution_max_rel_dev'] = {
        'N_eff 3.0432 instead of 3.044 (one massive neutrino 0.06 eV)': [float(np.max(np.abs(cla[sel, k] / cl0[sel, k] - 1))) for k in (0, 1)],
        'three eigenstates 1.000, 8.712, 50.140 meV instead of one of 60 meV (N_eff 3.044)': [
            float(np.max(np.abs(clb[sel, k] / cl0[sel, k] - 1))) for k in (0, 1)]}
    att = list(out['attribution_max_rel_dev'].values())
    out['max_dev_in_cosmic_variance_units'] = float(np.max(ratio))
    rep.check('theta_star_matched', abs(um2['theta_star_100'] - lcdm['theta_star_100']) < 2e-4,
              '100 theta_* = %.5f (UM-2) and %.5f (LCDM); H0 = %.2f and %.2f km/s/Mpc' % (um2['theta_star_100'], lcdm['theta_star_100'],
                                                                                    um2['H0'], lcdm['H0']))
    # the three neutrino eigenstates in CAMB, the mass sum and its bound
    deg = Neff_nu / 3.0
    mphys = [m * deg ** 0.25 for m in um2['camb_masses_eV']]
    merr = max(abs(a / b - 1) for a, b in zip(mphys, masses))
    msum = float(sum(masses))
    bound = SUM_MNU_BOUND_EV[0]
    s21, s31 = NUFIT60_NO['dm2_21_eV2'][0], NUFIT60_NO['dm2_31_eV2'][0]
    from scipy.optimize import brentq
    m1max = brentq(lambda m1: m1 + math.sqrt(m1 * m1 + s21) + math.sqrt(m1 * m1 + s31) - bound, 0.0, bound)
    msum_min = math.sqrt(s21) + math.sqrt(s31)
    om_ratio = um2['omnuh2_camb_today'] / (nu['CNB']['Omega_nu_h2'] * deg ** 0.75)
    out['neutrinos'] = {'masses_eV': masses, 'camb_masses_eV': um2['camb_masses_eV'], 'camb_masses_times_deg_quarter_eV': mphys,
                        'sum_eV': msum, 'sum_bound_eV': bound, 'sum_min_normal_ordering_eV': msum_min,
                        'm1_max_from_bound_eV': m1max, 'Omega_nu_h2_camb': um2['omnuh2_camb_today'],
                        'Omega_nu_h2_um2_neutrino_times_deg34': nu['CNB']['Omega_nu_h2'] * deg ** 0.75,
                        'camb_mass_iterations': len(um2['camb_mass_iteration'])}
    rep.check('three_massive_neutrinos', merr < 1e-9 and msum < bound and abs(om_ratio - 1) < 2e-3,
              'CAMB evolves the three mass eigenstates separately (each with N_eff = %.4f; masses m_i deg^{-1/4} after %d iterations, '
              'reproducing m_i = %.4f, %.4f, %.4f meV to %.1e); sum m_nu = %.4f eV (normal-ordering minimum %.4f eV) below the DESI DR2 '
              'bound %.3f eV (95 %%, LCDM), which allows m_1 < %.1f meV; Omega_nu h^2 today = %.4e (CAMB), %.4e from um2_neutrino.py '
              '(instantaneous decoupling) times deg^{3/4} (ratio %.5f)' % (deg, len(um2['camb_mass_iteration']), 1e3 * masses[0], 1e3 * masses[1], 1e3 * masses[2], merr, msum,
                             msum_min, bound, 1e3 * m1max, um2['omnuh2_camb_today'], nu['CNB']['Omega_nu_h2'] * deg ** 0.75, om_ratio))
    rep.check('cmb_spectra_close_to_lcdm', dTT < 0.01 and dEE < 0.01,
              'UM-2 TT and EE spectra agree with Planck LCDM to %.2e and %.2e (relative, 30 <= l <= 2500), at most %.2f of the cosmic variance '
              'of a single multipole; binned full-sky cosmic-variance chi^2 of TT = %.3f; by themselves the three mass eigenstates (59.9 meV in '
              'three states instead of 60 meV in one) move TT, EE by %.1e, %.1e and N_eff = 3.0432 instead of 3.044 by %.1e, %.1e' % (
                  dTT, dEE, np.max(ratio), out['UM2_TT_chi2_cosmic_variance_full_sky'], att[1][0], att[1][1], att[0][0], att[0][1]))
    rep.check('bao_desi', um2['bao_chi2'] < 40,
              'DESI DR2 BAO chi^2 = %.2f for 13 measurements (LCDM with Planck parameters: %.2f; with dark radiation Delta N_eff = %.4f: '
              '%.2f; %.4f: %.2f)' % (um2['bao_chi2'], lcdm['bao_chi2'], dN_ew, um2e['bao_chi2'], dN_qcd, um2q['bao_chi2']))
    Neff_act, dNeff_act = val('N_eff_ACT_DR6'), INPUTS['N_eff_ACT_DR6'][1]
    rep.check('dark_radiation_variants', abs(um2e['Neff'] - (Neff_nu + dN_ew)) < 1e-9 and abs(um2q['Neff'] - (Neff_nu + dN_qcd)) < 1e-9
              and dN_ew < dN_qcd,
              'variants with a thermalised fold band of dirac16complex (two Weyl species, Delta N_eff = 2 (10.75/g_s)^{4/3} x 1.0095): '
              'N_eff = %.4f (g_s = 105.75) and %.4f (g_s = 61.75), %.1f and %.1f standard deviations above ACT DR6 (%.2f +- %.2f; '
              'UM-2: %.1f); at fixed Planck omega_b, omega_c, theta_* the TT spectrum moves by up to %.2e and %.2e (%.1f and %.1f '
              'cosmic-variance units per multipole; binned full-sky cosmic-variance chi^2 %.0f and %.0f): neither is a fit to the '
              'CMB; UM-2 contains no such thermalisation (um2_electroweak.py)' % (
                  um2e['Neff'], um2q['Neff'], (um2e['Neff'] - Neff_act) / dNeff_act, (um2q['Neff'] - Neff_act) / dNeff_act, Neff_act,
                  dNeff_act, (um2['Neff'] - Neff_act) / dNeff_act, out['dark_radiation_EW_max_rel_dev_TT'],
                  out['dark_radiation_QCD_max_rel_dev_TT'], out['dark_radiation_EW_max_dev_in_cosmic_variance_units'],
                  out['dark_radiation_QCD_max_dev_in_cosmic_variance_units'], out['dark_radiation_EW_TT_chi2_cosmic_variance_full_sky'],
                  out['dark_radiation_QCD_TT_chi2_cosmic_variance_full_sky']))
    rep.check('neff_and_helium', abs(um2['Neff'] - Neff_nu) < 1e-12 and abs(um2['Neff_massive'] - Neff_nu) < 1e-12 and um2['Neff_massless'] == 0,
              'N_eff = %.4f, all of it in the three massive eigenstates (BBN helium fraction Y_He = %.5f from the CAMB/BBN interpolation, '
              'LCDM %.5f)' % (um2['Neff'], um2['YHe'], lcdm['YHe']))
    out['CNB'] = nu['CNB']
    # figures
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(2, 2, figsize=(12, 7), gridspec_kw={'height_ratios': [3, 1]})
    ll = l[2:2501]
    for j, (lab, col) in enumerate([('TT', 0), ('EE', 1)]):
        axs[0, j].plot(ll, cl0[2:2501, col], 'k-', lw=1.2, label='Planck 2018 LCDM')
        axs[0, j].plot(ll, cl1[2:2501, col], 'C1--', lw=1.0, label='UM-2 (three massive neutrinos)')
        axs[0, j].plot(ll, cl3[2:2501, col], 'C2:', lw=1.0, label='UM-2 + fold band thermalised above QCD')
        axs[0, j].set_ylabel(r'$\ell(\ell+1)C_\ell/2\pi$ [$\mu$K$^2$] (%s)' % lab)
        axs[0, j].set_xscale('log')
        axs[0, j].legend(fontsize=8)
        axs[1, j].plot(ll, cl1[2:2501, col] / cl0[2:2501, col] - 1, 'C1-', lw=0.8)
        axs[1, j].plot(ll, cl3[2:2501, col] / cl0[2:2501, col] - 1, 'C2-', lw=0.8)
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
        for mdl, st, lab_m in [(lcdm, 'k-', 'Planck 2018 LCDM'), (um2, 'C1--', 'UM-2'),
                               (um2q, 'C2:', 'UM-2 + fold band thermalised above QCD')]:
            zz = [b['z'] for b in mdl['bao']]
            axs[qi].plot(zz, [b[q] / math.sqrt(b['z']) for b in mdl['bao']], st, lw=1, label=lab_m)
        labelled = False
        for (tr, z, dv, dm, dh, r) in DESI:
            dat = {'DV_rd': dv, 'DM_rd': dm, 'DH_rd': dh}[q]
            if dat is not None:
                axs[qi].errorbar([z], [dat[0] / math.sqrt(z)], yerr=[dat[1] / math.sqrt(z)], fmt='o', ms=4, color='C0',
                                 label=None if labelled else 'DESI DR2')
                labelled = True
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
