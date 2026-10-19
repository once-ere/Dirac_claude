#!/usr/bin/env python3
"""Write universe_model_2/docs_src/symbols/analysis.json (the ANALYSIS registry, version 4)."""
import json
from pathlib import Path

OUT = Path('/home/claude/dirac_claude/universe_model_2/docs_src/symbols/analysis.json')
R = {}


def add(key, tex, atoms, meaning, units, value=None, status=None):
    e = {'tex': tex, 'atoms': atoms, 'meaning': meaning, 'units': units}
    if value:
        e['value'] = value
    if status:
        e['status'] = status
    R[key] = e


add('ana_hbar', r'\hbar', [r'\hbar'],
    r'The reduced Planck constant, which sets the scale of the uncertainty relation; it equals 1 in the natural units of '
    r'this document, and $\hbar c = 1.973269804\times10^{-16}$ GeV m converts an inverse mass into a length.',
    r'GeV s (equal to 1 in natural units)', r'1 (natural units)', 'STANDARD')
add('ana_kx0', r'k_{x_0}', [r'k_{x_0}'],
    r'The component of the momentum along the hidden coordinate $x_0$, the momentum conjugate to $x_0$ (the author\'s '
    r'$(p)_{x_0}$); since $\hbar = 1$ it is also the wave number of the $x_0$ dependence.',
    'GeV', None, 'AUTHOR')
add('ana_meff', r'm_{\mathrm{eff}}', [r'm_{\mathrm{eff}}'],
    r'The effective mass of the author\'s argument: the mass that a particle receives from the $x_0$ dependence of its '
    r'wave function, estimated by taking the momentum $k_{x_0}$ proportional to the mass and the kinetic energy '
    r'proportional to the momentum squared over the mass.',
    'GeV', None, 'AUTHOR')
add('ana_Ekin', r'E_{\mathrm{kin}}', [r'E_{\mathrm{kin}}'],
    r'The kinetic energy of the motion along $x_0$ in the author\'s argument, proportional to $k_{x_0}^2/m_{\mathrm{eff}}$.',
    'GeV', None, 'AUTHOR')
add('ana_mHeis', r'm_{\mathrm{Heis}}', [r'm_{\mathrm{Heis}}'],
    r'The author\'s uncertainty (Heisenberg) estimate of the mass of a state, $m_{\mathrm{Heis}} = \hbar/(2\Delta(fy))$, '
    r'where $\Delta(fy) = fL\,\Delta\xi$ is the root-mean-square proper distance of the state from the fold '
    r'($\Delta\xi^2 = \int_{-1}^{0}\xi^2\varrho_\xi\,\mathrm{d}\xi$). It is the lower bound on the mass that the '
    r'uncertainty relation would give if the hidden kinetic energy were the whole mass and the state were negligible '
    r'at the tip. (The subscript stands for Heisenberg; UM-2 has no Higgs particle.)',
    'GeV',
    r'70.56 TeV (photon, gluons, graviton, $W^\pm$, $Z$); 53.80 TeV (quark-doublet zero mode); 93.08 TeV '
    r'(lepton-doublet zero mode); 22.90 TeV (fold band of dirac16complex); 19.39 TeV (dark matter); at least '
    r'$1/(2fL) = 11.05$ TeV for every profile on the cell', 'DERIVED')
add('ana_kxi', r'k_\xi', [r'k_{\xi}'],
    r'The wave number conjugate to $\xi$, i.e. the hidden momentum in units of $1/(fL)$. Its mean square in a state is the '
    r'hidden kinetic energy in units of $1/(fL)^2$: $\langle k_\xi^2\rangle = \int_{-1}^{0}(\mathrm{d}\tilde F/\mathrm{d}\xi)^2'
    r'\mathrm{d}\xi\big/\int_{-1}^{0}\tilde F^2\mathrm{d}\xi$ for a boson (flat-measure profile $\tilde F$) and '
    r'$\int_{-1}^{0}(\mathrm{d}\chi/\mathrm{d}\xi)^\dagger(\mathrm{d}\chi/\mathrm{d}\xi)\,\mathrm{d}\xi\big/\int_{-1}^{0}'
    r'\chi^\dagger\chi\,\mathrm{d}\xi$ for a fermion.',
    'dimensionless', None, 'DERIVED')
add('ana_varrhoxi', r'\varrho_\xi', [r'\varrho_{\xi}'],
    r'The probability density in $\xi$ of the $x_0$ profile of a mode on one half of the period, normalised as '
    r'$\int_{-1}^{0}\varrho_\xi\,\mathrm{d}\xi = 1$: $\varrho_\xi = \tilde F^2/\int_{-1}^{0}\tilde F^2\mathrm{d}\xi$ for a '
    r'boson ($\tilde F = \mathrm{e}^{3HL\xi/2}F$, the flat measure) and $\varrho_\xi = \chi^\dagger\chi/\int_{-1}^{0}'
    r'\chi^\dagger\chi\,\mathrm{d}\xi$ for a fermion. $\varrho_\xi(0)$ is its value at the fold, $\varrho_\xi(-1)$ its value '
    r'at the tip; over the full period the density is symmetric about the fold.',
    'dimensionless', None, 'DERIVED')
add('ana_wKS', r'w_{\mathrm{KS}}', [r'w_{\mathrm{KS}}'],
    r'The equation of state of a Kohn-Sham state of dirac16complex: the ratio of its integrated 3-space pressure to its '
    r'integrated energy density, each integrated over the cell as $2\,\mathrm{Vol}_7\int_{-L}^{0}\mathrm{e}^{3Hy}(\cdot)\,'
    r'\mathrm{d}y$.',
    'dimensionless',
    r'0 for dark-matter quanta at rest ($2.8\times10^{-5}$ with $\lambda_{\mathrm{test}}$); 1/3 for the free fold-band gas '
    r'(0.3312 with $+\lambda_{\mathrm{test}}$, 0.3354 with $-\lambda_{\mathrm{test}}$)', 'DERIVED')
add('ana_wde', r'w_{\mathrm{de}},\ w_{\mathrm{de},0},\ w_{\mathrm{de},a}',
    [r'w_{\mathrm{de}}', r'w_{\mathrm{de},0}', r'w_{\mathrm{de},a}'],
    r'The equation of state of a candidate dark energy, the ratio of its pressure to its energy density. In the '
    r'parametrisation $w_{\mathrm{de}} = w_{\mathrm{de},0} + w_{\mathrm{de},a}(1 - \mathrm{e}^{a_4})$ used by supernova fits, '
    r'$w_{\mathrm{de},0}$ is the value today ($a_4 = 0$) and $w_{\mathrm{de},a} = -\mathrm{d}w_{\mathrm{de}}/\mathrm{d}'
    r'\mathrm{e}^{a_4}$ at $a_4 = 0$ (the tangent at today).',
    'dimensionless', None, 'STANDARD')
add('ana_calX', r'\mathcal{X},\ \mathcal{X}_0', [r'\mathcal{X}', r'\mathcal{X}_{0}'],
    r'The ratio of the self-interaction energy density to the rest-energy density of a homogeneous scalar condensate of '
    r'dirac16complex, $\mathcal{X} = \lambda n^{\mathrm{sc}}/(2m_\Psi)$; it scales as $\mathrm{e}^{-3a_4}$, and '
    r'$\mathcal{X}_0$ is its value today ($a_4 = 0$).',
    'dimensionless', None, 'DERIVED')
add('ana_Ucond', r'U_{\mathrm{cond}}', [r'U_{\mathrm{cond}}'],
    r'The self-interaction energy density of a homogeneous scalar condensate of dirac16complex, $U_{\mathrm{cond}} = '
    r'\frac{\lambda}{2}(n^{\mathrm{sc}})^2$ (the contact term of the action evaluated on the condensate).',
    r'GeV$^8$ (an eight-dimensional energy density)', None, 'DERIVED')
add('ana_rhovac', r'\rho_{\mathrm{vac}}', [r'\rho_{\mathrm{vac}}'],
    r'A natural vacuum energy density of the cell, the fourth power of the Kaluza-Klein scale over $16\pi^2$.',
    r'GeV$^4$', r'$1.4\times10^{18}$ GeV$^4$', 'ESTIMATE')
add('ana_rhode', r'\rho_{\mathrm{de}}', [r'\rho_{\mathrm{de}}'],
    r'The observed energy density of the dark energy today.',
    r'GeV$^4$', r'$2.5\times10^{-47}$ GeV$^4$', 'STANDARD')
add('ana_Gammar', r'\Gamma_{\mathrm{r}}', [r'\Gamma_{\mathrm{r}}'],
    r'The decay rate of the radion (the quantum of the block-size oscillation) into lighter particles, a '
    r'Planck-suppressed estimate.',
    'GeV', r'$1.52\times10^{-24}\,C_{\mathrm{r}}$ GeV (lifetime $0.43\,\text{s}/C_{\mathrm{r}}$)', 'ESTIMATE')
add('ana_Cr', r'C_{\mathrm{r}}', [r'C_{\mathrm{r}}'],
    r'The order-one factor of the radion decay rate that collects its unknown couplings to the decay products.',
    'dimensionless', r'not computed (of order one)', 'ESTIMATE')
add('ana_MPlbar', r'\bar M_{\mathrm{Pl}}', [r'\bar{M}_{\mathrm{Pl}}'],
    r'The reduced Planck mass, $\bar M_{\mathrm{Pl}} = (8\pi G_{\mathrm{N}})^{-1/2} = M_{\mathrm{Pl}}/\sqrt{8\pi}$.',
    'GeV', r'$2.435\times10^{18}$ GeV', 'STANDARD')
add('ana_TRH', r'T_{\mathrm{RH}}', [r'T_{\mathrm{RH}}'],
    r'The reheating temperature: the temperature of the plasma produced when the radion oscillation left over from the '
    r'primordial deflation decays.',
    'GeV', r'$1.85\sqrt{C_{\mathrm{r}}}$ MeV', 'ESTIMATE')
add('ana_swpw', r'a_{\mathrm{sw}},\ b_{\mathrm{pw}}', [r'a_{\mathrm{sw}}', r'b_{\mathrm{pw}}'],
    r'The s-wave and p-wave coefficients of the non-relativistic expansion of the thermally averaged annihilation '
    r'cross-section, $\langle\sigma v_{\mathrm{rel}}\rangle = a_{\mathrm{sw}} + 6b_{\mathrm{pw}}/x$.',
    r'GeV$^{-2}$ (quoted in cm$^3$/s)', r'for I12 alone at the relic strength $a_{\mathrm{sw}} = 0$, '
    r'$b_{\mathrm{pw}} = 8.741\times10^{-8}$ GeV$^{-2}$', 'STANDARD')
add('ana_Nstate', r'\lvert\mathrm{N}\rangle', [r'\mathrm{N}'],
    r'A nucleon state at rest (proton or neutron); $\langle\mathrm{N}\rvert\cdots\lvert\mathrm{N}\rangle$ is a matrix '
    r'element between nucleon states, normalised so that the trace of the energy-momentum tensor of QCD has the matrix '
    r'element $m_{\mathrm{N}}$.',
    'dimensionless (state)', None, 'STANDARD')
OUT.write_text(json.dumps(R, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('wrote', len(R), 'entries to', OUT)
