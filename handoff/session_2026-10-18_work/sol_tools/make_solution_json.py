#!/usr/bin/env python3
"""Write the SOLUTION registry file (version 4): the symbols that only SOLUTION uses.  Usage: python3 make_solution_json.py OUT"""
import json
import sys

E = {}


def R(key, tex, atoms, meaning, units, value=None, status=None):
    e = {'tex': tex, 'atoms': atoms, 'meaning': ' '.join(meaning.split()), 'units': units}
    if value:
        e['value'] = value
    if status:
        e['status'] = status
    E[key] = e


# step 2
R('sol_BR', r'\mathrm{BR}', [r'\mathrm{BR}'],
  r'The branching ratio of the lepton-flavour-violating decay of a charged lepton of the flavour $\alpha$ into one of the flavour '
  r'$\beta$ and a photon, the fraction of all its decays that end in this final state; in step 2 it is the decay '
  r'$\mu \to e\gamma$ ($\alpha = \mu$, $\beta = e$) through the neutrino masses alone.', 'dimensionless',
  r'$2.8\times10^{-55}$ for $\mu \to e\gamma$', 'DERIVED')
R('sol_alpha0', r'\alpha_{\mathrm{em},0}', [r'\alpha_{\mathrm{em},0}'],
  r'The electromagnetic fine-structure constant at zero momentum transfer, $e^2/(4\pi)$ measured at low energy (distinct from '
  r'its value at the $Z$ mass).', 'dimensionless', r'$1/137.036$', 'STANDARD')
# step 4
R('sol_gZ', r'g_{\mathrm{Z}}', [r'g_{\mathrm{Z}}'],
  r'The four-dimensional coupling of the $Z$ boson to the neutral current, $g_{\mathrm{Z}} = (g_2^2 + g_1^2)^{1/2}$ (canonically '
  r'normalised fields); the $Z$ couples to a fermion with $g_{\mathrm{Z}}(T_3P_L - Q_{\mathrm{em}}\sin^2\theta_{\mathrm{W}})$.',
  'dimensionless', status='DERIVED')
R('sol_anomaly', r'\mathcal{A}_{\mathrm{SU(3)^2U(1)}},\ \mathcal{A}_{\mathrm{SU(2)^2U(1)}},\ \mathcal{A}_{\mathrm{U(1)^3}}',
  [r'\mathcal{A}_{\mathrm{SU(3)^2U(1)}}', r'\mathcal{A}_{\mathrm{SU(2)^2U(1)}}', r'\mathcal{A}_{\mathrm{U(1)^3}}'],
  r'The gauge anomaly coefficients of one generation, with every zero mode written as a left-handed Weyl field (a right-handed one '
  r'with the hypercharge $-Y$): the sum over the colour triplets of $N_{\mathrm{dbl}}Y$ (mixed $SU(3)^2U(1)_Y$ anomaly), the sum '
  r'over the weak doublets of $N_{\mathrm{col}}Y$ (mixed $SU(2)^2U(1)_Y$ anomaly) and the sum over all components of '
  r'$N_{\mathrm{col}}N_{\mathrm{dbl}}Y^3$ (the $U(1)_Y^3$ anomaly); the theory is consistent only if they vanish.', 'dimensionless',
  '0 for each generation of UM-2', 'DERIVED')
R('sol_Ncol', r'N_{\mathrm{col}}', [r'N_{\mathrm{col}}'],
  'The number of colour components of a fermion multiplet: 3 for a quark, 1 for a lepton.', 'dimensionless', status='STANDARD')
R('sol_Ndbl', r'N_{\mathrm{dbl}}', [r'N_{\mathrm{dbl}}'],
  'The number of weak-isospin components of a fermion multiplet: 2 for an $SU(2)$ doublet, 1 for a singlet.', 'dimensionless',
  status='STANDARD')
R('sol_rZ', r'r_{\mathrm{Z}}', [r'r_{\mathrm{Z}}'],
  r'The coupling of the fold band of $\Psi_A$ to the $Z$ in units of the coupling of one neutrino flavour, in the chiral tip $Z$ '
  r'portal of version 1 (removed in UM-2, where it is zero).', 'dimensionless',
  r'bounded by $r_{\mathrm{Z}}^2 < 0.0056$ (two standard deviations)', 'DERIVED')
R('sol_Nnu', r'N_\nu', [r'N_{\nu}'],
  r'The number of light neutrino species seen by the $Z$: its invisible width in units of its width into one neutrino flavour.',
  'dimensionless', r'measured $2.9963 \pm 0.0074$ (PDG 2025); 3 in UM-2', 'STANDARD')
R('sol_GammaZ', r'\Gamma_{\mathrm{Z}}^{f}', [r'\Gamma_{\mathrm{Z}}'],
  r'The decay width of the $Z$ boson; with the fermion label $f$ it is the partial width into the pair of $f$ and its antiparticle '
  '(tree level, massless fermion).', 'GeV (quoted in MeV)',
  r'total $2485.2$ MeV with $1 + \alpha_3/\pi$ on the quarks (measured $2495.5$ MeV)', 'DERIVED')
# step 5: the Majorana alternative
R('sol_SM', r'S_{\mathrm{M}}', [r'S_{\mathrm{M}}'],
  r'The action of the gauge-invariant Majorana mass operator on the tip, the alternative to the Dirac neutrinos of UM-2 without '
  r'right-handed neutrinos (not part of UM-2).', r'dimensionless (an action, $\hbar = 1$)', status='INVENTED')
R('sol_mM', r'm^{\mathrm{M}}_{ij}', [r'm^{\mathrm{M}}'],
  r'The complex symmetric $3\times3$ matrix of the Majorana tip masses of the alternative operator $S_{\mathrm{M}}$ (generation '
  r'indices $i$, $j$).', 'GeV', status='INVENTED')
R('sol_nutilde', r'\tilde\nu_i', [r'\tilde{\nu}'],
  r'The neutral upper component $(\Sigma^\dagger\ell_i)_1$ of the lepton doublet of generation $i$ dressed with the tip sigma '
  r'field: a left-handed field that is neutral under $SU(2)_L\times U(1)_Y$; $\tilde\nu_i\tilde\nu_j$ is the Lorentz-invariant '
  '(Majorana) product of two such fields.', r'$\mathrm{GeV}^{7/2}$ (an eight-dimensional spinor field at the tip)',
  status='INVENTED')
R('sol_KM', r'\mathcal{K}_{\mathrm{M}}^{(i)}', [r'\mathcal{K}_{\mathrm{M}}'],
  r'The dimensionless Majorana tip coefficient that the alternative would need for the mass state $i$ (written with the index '
  r'$i$ in brackets): $m_i = \mathcal{K}_{\mathrm{M}}^{(i)}\,\mathcal{Z}(c_L)^2/(fL)$ to first order in the tip value of the doublet '
  'zero mode.',
  'dimensionless', r'$5.63\times10^{-13}$, $4.90\times10^{-12}$, $2.82\times10^{-11}$ for $i = 1, 2, 3$', 'DERIVED')
R('sol_phiM', r'\varphi^{\mathrm{M}}_i', [r'\varphi^{\mathrm{M}}'],
  r'The Majorana phase of the neutrino mass state $i$ in the Majorana alternative (a free parameter; all values are scanned).',
  'dimensionless (radians)', status='ASSUMED')
R('sol_mbb', r'm_{\beta\beta}', [r'm_{\beta \beta}'],
  r'The effective Majorana mass of neutrinoless double-beta decay, $\lvert\sum_iU_{ei}^2m_i\mathrm{e}^{\mathrm{i}\varphi^{\mathrm{M}}_i}\rvert$.',
  'eV', r'$0.84$ to $4.41$ meV over all Majorana phases', 'DERIVED')
R('sol_Omeganu', r'\Omega_\nu', [r'\Omega_{\nu}'],
  r'The density parameter of the three neutrino mass states today: their energy density divided by the critical density '
  r'$\rho_{\mathrm{crit}}$ (with $h_{100}^2$: $\Omega_\nu h_{100}^2$).', 'dimensionless',
  r'$\Omega_\nu h_{100}^2 = 6.382\times10^{-4}$ (instantaneous decoupling), $6.4511\times10^{-4}$ (heated spectrum, CAMB)',
  'DERIVED')
# step 6: BAO
R('sol_Dist', r'd_{\mathrm{M}},\ d_{\mathrm{H}},\ d_{\mathrm{V}}', [r'd_{\mathrm{M}}', r'd_{\mathrm{H}}', r'd_{\mathrm{V}}'],
  r'The distances of the BAO analysis at the redshift $z_{\mathrm{red}}$ (flat space, $c = 1$): the comoving transverse distance '
  r'$d_{\mathrm{M}}$, the Hubble distance $d_{\mathrm{H}} = 1/\mathcal{H}$ at that redshift, and the volume-averaged distance '
  r'$d_{\mathrm{V}} = (z_{\mathrm{red}}d_{\mathrm{M}}^2d_{\mathrm{H}})^{1/3}$ (written with a lower-case $d$ because $D_M$ is the '
  'covariant derivative).', 'length (Mpc)', status='STANDARD')
R('sol_rd', r'r_{\mathrm{d}}', [r'r_{\mathrm{d}}'],
  'The comoving sound horizon at the drag epoch, the standard ruler of the BAO.', 'length (Mpc)',
  r'$147.104$ Mpc (UM-2)', 'DERIVED')
R('sol_zred', r'z_{\mathrm{red}},\ \tilde z_{\mathrm{red}}', [r'z_{\mathrm{red}}', r'\tilde{z}_{\mathrm{red}}'],
  r'The cosmological redshift, $1 + z_{\mathrm{red}} = \mathrm{e}^{-a_4}$ with $a_4 = 0$ today (not $z = 6Hx_0$, the angle variable '
  r'of the hidden direction); $\tilde z_{\mathrm{red}}$ is the redshift as the variable of an integral.',
  'dimensionless', status='STANDARD')
R('sol_chiBAO', r'\chi^2_{\mathrm{BAO}}', [r'\chi_{\mathrm{BAO}}'],
  'The chi-squared of the model distances against the 13 DESI DR2 BAO measurements (the pairs of the anisotropic tracers with '
  'their correlations, and one point for BGS).', 'dimensionless', r'$31.49$ for UM-2 ($32.55$ for $\Lambda$CDM)', 'DERIVED')
R('sol_dvec', r'\mathbf{d},\ \mathbf{d}^{\mathrm{th}}', [r'\mathbf{d}', r'\mathbf{d}^{\mathrm{th}}'],
  r'The measured pair $(d_{\mathrm{M}}/r_{\mathrm{d}}, d_{\mathrm{H}}/r_{\mathrm{d}})$ of an anisotropic BAO tracer, and the pair '
  r'$\mathbf{d}^{\mathrm{th}}$ computed in the model.', 'dimensionless', status='STANDARD')
R('sol_Cmat', r'\mathbf{C}', [r'\mathbf{C}'],
  r'The covariance matrix of the measured pair of one BAO tracer, built from the published errors and the published '
  r'correlation coefficient of the pair.', 'dimensionless', status='STANDARD')
# step 7 and 9: relic and detection
R('sol_xf', r'x_{\mathrm{f}}', [r'x_{\mathrm{f}}'],
  r'The freeze-out point $x_{\mathrm{f}} = M_{\mathrm{DM}}/T$ at which the dark matter leaves chemical equilibrium.',
  'dimensionless', r'$30.38$ (freeze-out formula, I12), $31.23$ (Boltzmann equation, I12 + I13)', 'DERIVED')
R('sol_vc', r'v_{\mathrm{c}}', [r'v_{\mathrm{c}}'],
  r'The relative velocity above which the effective I12 cross-section at the relic strength exceeds the $^3P_0$ unitarity bound '
  '(non-relativistic formula).', 'dimensionless (units of c)', r'$0.263$', 'DERIVED')
R('sol_fN', r'f_{\mathrm{N}},\ f_{\mathrm{p}},\ f_{\mathrm{n}}', [r'f_{\mathrm{N}}', r'f_{\mathrm{p}}', r'f_{\mathrm{n}}'],
  r'The spin-independent effective couplings of the dark matter to a nucleon: $f_{\mathrm{p}}$ to the proton, $f_{\mathrm{n}}$ to the '
  r'neutron, and $f_{\mathrm{N}}$ the average per nucleon of the target (or, in step 7, the coupling through the gluon content of '
  r'a nucleon).', r'$\mathrm{GeV}^{-2}$', r'$f_{\mathrm{p}} = 1.915\times10^{-9}$, $f_{\mathrm{n}} = 1.917\times10^{-9}$ GeV$^{-2}$ '
  '(I13 and I11)', 'ESTIMATE')
R('sol_mN', r'm_{\mathrm{N}}', [r'm_{\mathrm{N}}'], 'The mass of a nucleon.', 'GeV', '0.939 GeV', 'STANDARD')
R('sol_fTG', r'f_{\mathrm{TG}}', [r'f_{\mathrm{TG}}'],
  'The fraction of the nucleon mass carried by the gluons through the trace anomaly of QCD.', 'dimensionless',
  '0.92 (the value used in the computation; approximate)', 'STANDARD')
R('sol_sigmaSI', r'\sigma_{\mathrm{SI}}', [r'\sigma_{\mathrm{SI}}'],
  'The spin-independent elastic scattering cross-section of a dark-matter particle on one nucleon.', r'$\mathrm{cm}^2$',
  r'$4.01\times10^{-46}$ cm$^2$ (xenon, I13 and I11); $6.3\times10^{-53}$ cm$^2$ through I12 alone', 'ESTIMATE')
R('sol_mured', r'\mu_{\mathrm{red}}', [r'\mu_{\mathrm{red}}'],
  r'The reduced mass of the dark-matter particle and a nucleon, $M_{\mathrm{DM}}m_{\mathrm{N}}/(M_{\mathrm{DM}} + m_{\mathrm{N}})$.',
  'GeV', status='STANDARD')
R('sol_Gud', r'G_{\mathrm{u}},\ G_{\mathrm{d}}', [r'G_{\mathrm{u}}', r'G_{\mathrm{d}}'],
  r'The four-dimensional vector couplings of the dark matter to the up and to the down quark (I13 and I11, unpolarised quarks with '
  'each chirality carrying half of the density).', r'$\mathrm{GeV}^{-2}$', status='DERIVED')
R('sol_ZAXe', r'Z_{\mathrm{Xe}},\ A_{\mathrm{Xe}}', [r'Z_{\mathrm{Xe}}', r'A_{\mathrm{Xe}}'],
  'The atomic number and the mass number of the xenon target.', 'dimensionless', '54 and 131', 'STANDARD')

if __name__ == '__main__':
    with open(sys.argv[1], 'w', encoding='utf-8') as f:
        json.dump(E, f, indent=1, ensure_ascii=False)
        f.write('\n')
    print(len(E), 'entries')
