# Three neutrino flavours: masses, mixing and flavour conversion (DERIVED)

## Masses and mixing

The neutrinos are Dirac fermions whose masses are $x_0$ eigenvalues: the lepton doublet zero mode $c_L = 5.9529$ mixed at the tip with the
singlet zero modes $c_R = -35.0452$, $-32.8481$, $-31.0702$, through the exact mass condition (written out again; $\mathcal{K} = 1$ for each mass
state, because $\mathcal{K}_\nu = U$ is unitary and the three doublets share one bulk mass)

@@FE-59@@

with $\tilde\varepsilon = m_i\,fL$. The lightest mass is not measured; UM-2 takes
(ASSUMED) the normal ordering, the best fit of NuFIT 6.0 (the inverted ordering is disfavoured by $\Delta\chi^2 = 6.1$), and

@@FE-100@@

with $\Delta m_{21}^2 = 7.49\times10^{-5}$ eV$^2$ and $\Delta m_{31}^2 = 2.513\times10^{-3}$ eV$^2$ (NuFIT 6.0). The sum $\sum_im_i = 0.0599$ eV lies above the
minimum $0.0588$ eV of the normal ordering and below the DESI DR2 bound $0.064$ eV (95 %, $\Lambda$CDM), which allows $m_1 < 4.1$ meV. The mixing is
the neutrino tip matrix, $U = \mathcal{K}_e^\dagger\mathcal{K}_\nu = \mathcal{K}_\nu$, in the standard parametrisation (written out again)

@@FE-61@@

with the NuFIT 6.0 values $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{23} = 0.470$, $\sin^2\theta_{13} = 0.02215$, $\delta_{\mathrm{CP}} = 212^\circ$
($J_{\mathrm{CP}} = -0.01777$). A neutrino produced by the charged current with the charged lepton $\ell^-_\alpha$ is the flavour state
$\lvert\nu_\alpha\rangle = \sum_iU^*_{\alpha i}\lvert\nu_i\rangle$ ($\alpha = e, \mu, \tau$). The oscillation phases are differences of squared $x_0$
eigenvalues, so oscillation experiments measure the $x_0$ spectrum directly; they are the quantities of UM-2 most sensitive to the block scale
($\mathrm{d}\ln\Delta m_{21}^2/\mathrm{d}\ln f = -77.5$, $\mathrm{d}\ln\Delta m_{31}^2/\mathrm{d}\ln f = -74.0$; DERIVED). The light neutrino states also mix with
the Kaluza-Klein excitations of the lepton fields, which makes the $3\times3$ PMNS matrix non-unitary at relative order
$(m_i/m_{\mathrm{KK}})^2 \le 1.7\times10^{-31}$ (ESTIMATE): unobservable. The angles and the phase are inputs of UM-2 (NuFIT 6.0), not predictions.

## The flavour evolution

At energies far below $m_{\mathrm{W}}$ the charged and neutral currents act as four-fermion interactions (written out again)

@@FE-101@@

@@FE-102@@

with the measured $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$. Coherent forward scattering in matter then adds the potentials (written
out again)

@@FE-103@@

to the free propagation, and the flavour amplitudes of a neutrino of energy $E$ evolve as (STANDARD)

@@FE-104@@

($V_{\mathrm{NC}}$ is flavour universal and drops out of the probabilities; for antineutrinos $U \to U^*$ and $V \to -V$). In vacuum

@@FE-105@@

In a dense neutrino gas (the early Universe, a supernova core) the state of the neutrinos of momentum $\vec k$ is a $3\times3$ density matrix, which
obeys the quantum kinetic equation (STANDARD)

@@FE-110@@

## Vacuum, matter, the Sun and accelerators

The computed evolution (exact matrix exponentials, the ordered products of thin layers for varying densities) reproduces the vacuum formula
to $3.9\times10^{-15}$, unitarity, CPT and the T-odd difference (DERIVED). In matter the mixing is resonant (the MSW effect) where the potential
cancels the vacuum splitting of a sector:

@@FE-106@@

Representative results (DERIVED; normal ordering, $\delta_{\mathrm{CP}} = 212^\circ$): reactor electron antineutrinos of 4 MeV survive with the
probability $0.918$ at 1.65 km, $0.226$ at 52.5 km and $0.267$ at 180 km; atmospheric muon neutrinos have their first survival minimum, $0.006$, at
$L_{\mathrm{b}}/E = 1516$ km/GeV; the MSW resonance of the 1-3 sector lies at $11.135$ GeV in rock of $2.8$ g/cm$^3$ (equal numbers of protons and
neutrons; the exact three-flavour resonance $\lvert U^{\mathrm{m}}_{e3}\rvert^2 = 1/2$, with the mixing matrix in matter, is at $11.133$ GeV), and that of
the 1-2 sector at the centre of the Sun at $1.93$ MeV. The $\nu_\mu \to \nu_e$ appearance at the long-baseline experiments (matter of constant
density):

| experiment | $L_{\mathrm{b}}$ | $E$ | density (g/cm$^3$) | $\mathcal{P}(\nu_\mu\to\nu_e)$ | $\mathcal{P}(\bar\nu_\mu\to\bar\nu_e)$ | vacuum $\mathcal{P}(\nu_\mu\to\nu_e)$ |
| --- | -- | -- | --- | ---- | ---- | --- |
| T2K | 295 km | 0.6 GeV | 2.6 | $0.0517$ | $0.0313$ | $0.0478$ |
| NOvA | 810 km | 2.0 GeV | 2.84 | $0.0481$ | $0.0236$ | $0.0404$ |
| DUNE | 1300 km | 2.5 GeV | 2.848 | $0.0701$ | $0.0195$ | $0.0491$ |

Solar electron neutrinos arrive at the Earth as an incoherent mixture of mass states, with the adiabatic survival probability

@@FE-107@@

evaluated at the production point in the electron density $n_{\mathrm{e}} = N_{\mathrm{A}}\min(245\,\mathrm{e}^{-10.54\,r/R_\odot}, 100)$ cm$^{-3}$ ($N_{\mathrm{A}}$
Avogadro's number, $R_\odot$ the solar radius; ASSUMED profile): $\mathcal{P}_{ee} = 0.541$ (pp, 0.3 MeV), $0.520$ ($^7$Be), $0.498$ (pep), $0.377$, $0.319$,
$0.306$ ($^8$B at 5, 10, 15 MeV); the numerical three-flavour evolution through the solar density agrees with the adiabatic formula to
$1.3\times10^{-3}$: the conversion is vacuum dominated at low energy and matter dominated (MSW) for $^8$B.

## The early Universe and $N_{\mathrm{eff}}$

The electron-positron plasma gives the electron neutrinos a thermal potential (STANDARD)

@@FE-109@@

which suppresses the mixing until it falls below the vacuum term; at the mean momentum $\lvert\vec k\rvert = 3.15T$ the atmospheric oscillations start
at $T = 4.99$ MeV and the solar ones at $T = 2.39$ MeV (DERIVED): flavour conversion is active while the neutrinos decouple. Decoupling is computed
from the temperature equations (STANDARD form, Escudero 2020; MeV units)

@@FE-111@@

with the energy transfer by collisions (the radiatively corrected couplings $0.727$, $0.233$, $-0.273$, $0.233$ are used; the tree-level ones change
$N_{\mathrm{eff}}$ by $4\times10^{-4}$)

@@FE-112@@

and the finite-temperature QED pressure of the electron-photon plasma (STANDARD; Bennett et al. 2020)

@@FE-113@@

@@FE-114@@

Then

@@FE-115@@

The method reproduces the published values of the same method (DERIVED: instantaneous decoupling $3.0002$, with the QED corrections $3.0108$ and
$3.0098$; Fermi-Dirac energy transfer $3.0393$, with QED $3.0495$ and $3.0485$; published $3.000$, $3.011$, $3.010$, $3.039$, $3.049$). For UM-2 it
gives $N_{\mathrm{eff}} = 3.0476$ with separate $\nu_e$ and $\nu_{\mu,\tau}$ temperatures (published with separate temperatures: $3.048$) and $3.0485$ with one
common temperature; $T_{\nu_e}/T_\gamma = 0.71732$, $T_{\nu_\mu}/T_\gamma = 0.71621$, the comoving neutrino temperatures being raised by $0.265$ % ($\nu_e$) and
$0.109$ % ($\nu_{\mu,\tau}$) by electron-positron annihilation. The plasma at MeV temperatures is that of the three-flavour Standard Model; the only
extra radiation is that of the fold bands produced by freeze-in through I11, $\Delta N_{\mathrm{eff}} = 0.001$ (neither fold band is ever thermalised;
the dark sector), so UM-2 adopts for the neutrinos the precision Standard-Model value with oscillations and the electron mass in the rates,
$N_{\mathrm{eff}} = 3.0432 \pm 0.0002$ (Cielo, Escudero, Mangano and Pisanti 2023), and $N_{\mathrm{eff}} = 3.0442$ with the fold bands.

## The cosmic neutrino background

After decoupling the flavour states lose their coherence: the CNB of UM-2 is an incoherent mixture of the three MASS eigenstates (DERIVED;
instantaneous decoupling; the CMB temperature $T_\gamma = 2.7255$ K today, STANDARD) with the temperature $T_\nu = (4/11)^{1/3}T_\gamma = 1.9454$ K and

@@FE-120@@

$n_i = 112.0$ cm$^{-3}$ per mass state (neutrinos and antineutrinos), $336$ cm$^{-3}$ in all, and the density parameter

$$
\Omega_\nu h_{100}^2 = \frac{\sum_{i=1}^{3}\rho_i}{\rho_{\mathrm{crit}}/h_{100}^2} = 6.382\times10^{-4},\qquad
\frac{\rho_{\mathrm{crit}}}{h_{100}^2} = 1.05368\times10^{4}\ \text{eV/cm}^3
$$
<!-- symbols: AUTO -->

($6.451\times10^{-4}$ with the heated spectrum of $N_{\mathrm{eff}} = 3.0432$: the degeneracy $N_{\mathrm{eff}}/3$ of each state corresponds to a Fermi-Dirac
spectrum of temperature $(N_{\mathrm{eff}}/3)^{1/4}T_\nu$, so the non-relativistic density is multiplied by $(N_{\mathrm{eff}}/3)^{3/4}$). The mean velocities
today and the flavour contents are

| state | mass | mean velocity today | $\nu_e$ content $\lvert U_{ei}\rvert^2$ | $\nu_\mu$ content | $\nu_\tau$ content |
| --- | --- | --- | --- | --- | --- |
| $\nu_1$ | $1.000$ meV | $0.435\,c$ | $0.677$ | $0.112$ | $0.211$ |
| $\nu_2$ | $8.712$ meV | $0.0604\,c$ | $0.301$ | $0.428$ | $0.271$ |
| $\nu_3$ | $50.140$ meV | $0.0105\,c$ | $0.022$ | $0.460$ | $0.518$ |

## Supernovae and the dense neutrino gas

**MSW in the envelope.** In the envelope, with the density profile $10^4\,(10^9\,\text{cm}/r)^3$ g/cm$^3$ and equal numbers of protons and neutrons
(ASSUMED), a resonance lies at the electron density of FE-108 and is crossed adiabatically when the adiabaticity is large (two-flavour
conditions: $\Delta m_{31}^2$ and $\theta_{13}$ for the H resonance, $\Delta m_{21}^2$ and $\theta_{12}$ for the L resonance, without the factor $c_{13}^2$ of the
solar condition):

@@FE-108@@

For 20 MeV the 1-3 (H) resonance lies at $1573$ g/cm$^3$ ($r = 1.85\times10^4$ km) with $\gamma_{\mathrm{ad}} = 178$ ($\mathcal{P}_{\mathrm{LZ}} = 2.7\times10^{-122}$):
adiabatic. For the normal ordering an electron neutrino from the core leaves the star as $\nu_3$ and an electron antineutrino as $\bar\nu_1$:
$\mathcal{P}(\nu_e\to\nu_e) = \lvert U_{e3}\rvert^2 = 0.022$ and $\mathcal{P}(\bar\nu_e\to\bar\nu_e) = \lvert U_{e1}\rvert^2 = 0.677$ (without collective effects and Earth
matter; DERIVED). For neutrinospheres with the luminosities $6$, $6$ and $4\times10^{52}$ erg/s and the mean energies $\bar E_{\mathrm{e}} = 11$ MeV,
$\bar E_{\bar{\mathrm{e}}} = 14$ MeV, $\bar E_{\mathrm{x}} = 15.5$ MeV of the electron neutrinos, electron antineutrinos and each heavy-lepton flavour
(ASSUMED), with the number emission rates proportional to the luminosity over the mean energy, the mean energies at the Earth are

$$
\bar E_{\mathrm{e}}^{\mathrm{Earth}} = \frac{\mathcal{P}\,\dot N_{\mathrm{e}}\bar E_{\mathrm{e}} + (1 - \mathcal{P})\,\dot N_{\mathrm{x}}\bar E_{\mathrm{x}}}{\mathcal{P}\,\dot N_{\mathrm{e}} + (1 - \mathcal{P})\,\dot N_{\mathrm{x}}}
 = 15.29\ \text{MeV}\qquad \big(\mathcal{P} = \mathcal{P}(\nu_e\to\nu_e)\big)
$$
<!-- symbols: AUTO -->

and, with $\mathcal{P}(\bar\nu_e\to\bar\nu_e)$, $\dot N_{\bar{\mathrm{e}}}$ and $\bar E_{\bar{\mathrm{e}}}$, $\bar E_{\bar{\mathrm{e}}}^{\mathrm{Earth}} = 14.34$ MeV for the electron
antineutrinos.

**The fast flavour instability.** Near the neutrinosphere the neutrino gas is dense enough for the neutrino-neutrino potential to dominate. For an
axially symmetric gas the electron-lepton-number angular distribution and its moments are

@@FE-116@@

the linearised equations for the flavour coherence give plane-wave modes along the symmetry axis $x_3$ with the dispersion relation (STANDARD)

@@FE-117@@

whose axisymmetric and azimuthal branches are

@@FE-118@@

and the homogeneous mode and the mode with $k_{\mathrm{f}} = \mathcal{I}_1$ obey

@@FE-119@@

A root with $\mathrm{Im}\,\bar\omega > 0$ is an instability. In units of $\sqrt2\,G_{\mathrm{F}}n_{\nu_e}$ (DERIVED): with an ELN crossing (forward-peaked
antineutrinos, $n_{\bar\nu_e}/n_{\nu_e} = 0.8$) the largest growth rate is $0.088$ (homogeneous mode $0.018$); with linear distributions
($g_{\nu_e} = 1 + 0.2u$, $g_{\bar\nu_e} = 1 + 0.6u$, $n_{\bar\nu_e}/n_{\nu_e} = 0.9$) it is $0.098$ although the homogeneous mode is stable; without a crossing
no mode grows, as the general theorem (Morinaga 2022) states. At $n_{\nu_e} = 10^{32}$ to $10^{33}$ cm$^{-3}$ the instability grows by the factor
$\mathrm{e}$ in $6\times10^{-10}$ to $6\times10^{-11}$ s over $18$ to $1.8$ cm, a million times faster than the hydrodynamics.

**Flavour conversion and the explosions.** Conversion moves energy from the electron-flavour neutrinos, which heat the matter behind the shock
through charged-current absorption, to the heavy-lepton neutrinos, which do not. A schematic estimate of the heating rate (Fermi-Dirac-like
spectra with the pinching parameter 3, so that the mean squared energy is $\frac54$ of the squared mean energy, a common factor) compares full
flavour equipartition and lepton-number-conserving pair conversion of $\dot N_{\mathrm{pair}}$ pairs with no conversion:

$$
\begin{aligned}
&\dot E_{\mathrm{h}} \propto \dot N_{\mathrm{e}}\bar E_{\mathrm{e}}^2 + \dot N_{\bar{\mathrm{e}}}\bar E_{\bar{\mathrm{e}}}^2,\qquad
 \dot E_{\mathrm{h}}^{\mathrm{eq}} \propto \tfrac13\big(\dot N_{\mathrm{e}}\bar E_{\mathrm{e}}^2 + 2\dot N_{\mathrm{x}}\bar E_{\mathrm{x}}^2\big)
 + \tfrac13\big(\dot N_{\bar{\mathrm{e}}}\bar E_{\bar{\mathrm{e}}}^2 + 2\dot N_{\mathrm{x}}\bar E_{\mathrm{x}}^2\big),\\
&\dot E_{\mathrm{h}}^{\mathrm{pair}} \propto \big(\dot N_{\mathrm{e}} - \dot N_{\mathrm{pair}}\big)\bar E_{\mathrm{e}}^2 + \big(\dot N_{\bar{\mathrm{e}}} - \dot N_{\mathrm{pair}}\big)\bar E_{\bar{\mathrm{e}}}^2,\qquad
 \dot N_{\mathrm{pair}} = \tfrac23\big(\dot N_{\bar{\mathrm{e}}} - \dot N_{\mathrm{x}}\big):
\end{aligned}
$$
<!-- symbols: AUTO -->

$\dot E_{\mathrm{h}}^{\mathrm{eq}}/\dot E_{\mathrm{h}} = 0.884$ and $\dot E_{\mathrm{h}}^{\mathrm{pair}}/\dot E_{\mathrm{h}} = 0.760$ for the neutrinospheres above (DERIVED,
schematic). In 195 collapse simulations (9 to 120 solar masses) with instantaneous flavour equipartition below a baryon density, Gogilashvili and
Tamborra (2026) find the fraction of failed explosions $25.6$ % without conversion and $50.8$, $77.4$, $93.3$, $96.4$ % for the threshold densities
$10^9$, $10^{10}$, $10^{11}$, $10^{13}$ g/cm$^3$ ($27.0$ % and $47.6$, $61.9$, $73.9$, $88.3$ % weighted with the Salpeter mass function), most strongly
between 16 and 30 solar masses, with lighter neutron stars from the successful explosions (STANDARD, cited).

## The $Z$ boson: invisible width and the widths of the three generations

With three neutrinos and no tip $Z$ portal the invisible width of the $Z$ counts $N_\nu = 3$ neutrino species, against the measured
$2.9963 \pm 0.0074$ (PDG 2025; 0.5 standard deviations); a fold band of $Z$ coupling $r_{\mathrm{Z}}$ times a neutrino's would add $2r_{\mathrm{Z}}^2$,
bounded by $r_{\mathrm{Z}}^2 < 0.0056$ (the section on the interactions). The tree-level partial widths (STANDARD)

$$
\Gamma_{\mathrm{Z}}^f = \frac{N_{\mathrm{col}}\,G_{\mathrm{F}}m_{\mathrm{Z}}^3}{6\sqrt2\,\pi}\Big(\big(\tilde g^f_V\big)^2 + \big(T_3^f\big)^2\Big),\qquad
\tilde g^f_V = T_3^f - 2Q_{\mathrm{em}}^f\sin^2\theta_{\overline{\mathrm{MS}}},
$$
<!-- symbols: AUTO -->

with the $\overline{\mathrm{MS}}$ value $\sin^2\theta_{\overline{\mathrm{MS}}} = 0.23122$ give (DERIVED) $165.9$ MeV per neutrino ($497.7$ MeV invisible; measured
$499.1$ MeV), $83.4$ MeV per charged lepton, $285.4$ MeV for each of the up and charm quarks and $367.9$ MeV for each of the down, strange and bottom
quarks (the top quark is too heavy), a hadronic width of $1674.4$ MeV ($1737.3$ MeV with the QCD factor $1 + \alpha_3/\pi$, $\alpha_3 = 0.1180$) and a
total of $2422.3$ MeV ($2485.2$ MeV with the QCD factor) against the measured $2495.5$ MeV; the ratio of the hadronic to the leptonic width is
$20.83$ against $20.77$. The remaining difference ($0.41$ % of the total) is the size of the electroweak loop corrections, which UM-2 does not
compute; the angle of the couplings of the $x_0$ mass fit, $\sin^2\theta_{\mathrm{W}} = 0.223632$, would change the total by $+0.82$ % ($0.83$ % with
the QCD factor; residual analysis).

## Dirac or Majorana (DERIVED)

UM-2 gives the neutrinos Dirac masses: the overlap at the tip of the lepton-doublet zero mode with three sharply localised right-handed
singlets ($\lvert c_R\rvert = 31$ to $35$) with tip couplings of order one. The alternative without right-handed neutrinos is a Majorana mass from the
gauge-invariant tip operator (the tip form of the Weinberg operator; the upper component of $\Sigma^\dagger\ell_i$ is neutral, since
$\Sigma \to U_L\Sigma U_Y^\dagger$ absorbs both the $SU(2)_L$ and the hypercharge transformations of $\ell_i$)

$$
S_{\mathrm{M}} = -\frac12\int_{y=-L}\mathrm{d}^7X_{\mathrm{tip}}\sqrt{\lvert g_{\mathrm{tip}}\rvert}\,\sum_{i,j=1}^{3}m^{\mathrm{M}}_{ij}\,\tilde\nu_i\tilde\nu_j + \text{h.c.},\qquad
\tilde\nu_i = \big(\Sigma^\dagger\ell_i\big)_1 .
$$
<!-- symbols: AUTO -->

On the zero modes it gives, to first order in the tip value of the doublet zero mode,

$$
m_i = \mathcal{K}_{\mathrm{M}}^{(i)}\,\frac{\mathcal{Z}(c_L)^2}{fL},\qquad \mathcal{Z}(c_L)^2 = 8.04\times10^{-5},\qquad \frac{1}{fL} = 22.1\ \text{TeV},
$$
<!-- symbols: AUTO -->

so the measured masses need the tip couplings $\mathcal{K}_{\mathrm{M}}^{(i)} = 5.6\times10^{-13}$, $4.9\times10^{-12}$, $2.8\times10^{-11}$: an unexplained hierarchy,
whereas the Dirac masses follow from the localisation with couplings of order one; the $x_0$ mechanism favours Dirac neutrinos. Observable
differences: neutrinoless double-beta decay, with

$$
m_{\beta\beta} = \Big\lvert\sum_{i=1}^{3}U_{ei}^2\,m_i\,\mathrm{e}^{\mathrm{i}\varphi^{\mathrm{M}}_i}\Big\rvert
$$
<!-- symbols: AUTO -->

between $0.84$ and $4.41$ meV for all Majorana phases ($\lvert U_{ei}\rvert^2m_i = 0.677$, $2.624$, $1.111$ meV; a numerical scan of the phases agrees),
below the reach of present experiments; and the capture of the non-relativistic CNB, twice as frequent for Majorana as for Dirac neutrinos (both
helicities active). The flavour conversion is the same in both cases (the Majorana phases cancel in the oscillation probabilities).

![Neutrino flavour conversion in UM-2. Left: the survival probability of solar electron neutrinos at the Earth against the energy (adiabatic formula FE-107 for two production radii, and the numerical three-flavour evolution through the solar density). Middle: the appearance probabilities $\mathcal{P}(\nu_\mu\to\nu_e)$ and $\mathcal{P}(\bar\nu_\mu\to\bar\nu_e)$ at the DUNE baseline of 1300 km (normal ordering, $\delta_{\mathrm{CP}} = 212^\circ$). Right: the growth rate $\mathrm{Im}\,\bar\omega$ of the axisymmetric fast-flavour modes against the wavenumber, in units of $\sqrt2\,G_{\mathrm{F}}n_{\nu_e}$ (labelled mu in the figure), for the three angular distributions of the text.](figures/fig_neutrino_conversion.png)

