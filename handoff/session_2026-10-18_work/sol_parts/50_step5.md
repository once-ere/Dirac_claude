# Step 5: the flavour conversion of the three neutrinos, $N_{\mathrm{eff}}$ and the CNB

The three neutrino masses are $x_0$ eigenvalues of step 2 and the PMNS matrix is the neutrino tip matrix. Step 5 solves the
flavour evolution of the three neutrinos in vacuum, in matter (the MSW effect), in the Sun, at accelerators, in the early
Universe (where it accompanies neutrino decoupling and fixes $N_{\mathrm{eff}}$), in the cosmic neutrino background, and in
supernovae (the MSW resonances of the envelope and the fast flavour instability of the dense neutrino gas), and compares the
Dirac neutrinos of UM-2 with the Majorana alternative.

## The field equations of step 5

The masses and the mixing matrix (step 2):

@@nu_masses@@

@@pmns@@

The interactions at low energy, the matter potentials and the flavour evolution:

@@fourfermion@@

@@gf@@

@@potentials@@

@@flavour_ham@@

@@vacuum_prob@@

@@msw@@

@@pee@@

@@adiabaticity@@

The early Universe: the thermal potential, the kinetic equations and the decoupling of the neutrinos:

@@thermal_pot@@

@@qke@@

@@decoupling@@

@@transfer@@

@@qed_pressure@@

@@qed_integrals@@

@@neff@@

The dense neutrino gas near a supernova core:

@@ffi_eln@@

@@ffi_disp@@

@@ffi_branches@@

@@ffi_homog@@

The cosmic neutrino background:

@@cnb@@

## The approximation of step 5

*Ultra-relativistic, coherent flavour evolution.* Every neutrino of the sources considered has $E \ge 0.3$ MeV, so the
corrections of order $(m_i/E)^2$ to the evolution are negligible,

$$
\Big(\frac{m_3}{E}\Big)^2 \le 2.8\times10^{-14}\qquad (E \ge 0.3\ \text{MeV}),
$$

<!-- symbols: AUTO -->

and outside the early Universe the collisions are negligible against the forward scattering. The flavour-universal
neutral-current potential drops out exactly. The adiabatic solar formula leaves out the non-adiabatic and production-region
effects, $1.3\times10^{-3}$ at most against the numerical evolution (whose layer discretisation is converged to
$2.2\times10^{-6}$); the Landau-Zener jumps in the supernova envelope are at most $2.6\times10^{-77}$; the collective
evolution beyond the linear analysis is OPEN. The other approximations of step 5 are these.

* *The thermal potential* is taken at leading order in $T/m_{\mathrm{W}}$ (the next order is $(T/m_{\mathrm{W}})^2 \sim
  4\times10^{-9}$) in a CP-symmetric plasma; the CP-asymmetric potential of the electron excess is $1.1\times10^{-2}$ of the
  thermal one at the solar onset temperature and $2.2\times10^{-3}$ at the atmospheric one (ESTIMATE; it would move the
  onset temperatures by about a sixth of this).
* *Neutrino decoupling with one temperature per flavour* (momentum averaged): the electron mass in the rates and the momentum
  dependence, which this method does not resolve, make the computed $N_{\mathrm{eff}}$ larger than the precision value by
  $0.0044$; the treatment of the oscillations (separate or common temperature) changes it by $0.0009$; the neutrino masses
  enter as $(m_3/T)^2 = 6\times10^{-16}$ at decoupling.
* *The fast flavour instability* is analysed linearly in the flavour coherence; near the neutrinosphere the vacuum term is
  $9.0\times10^{-6}$ of the self-interaction term.
* *The CNB* is the Fermi-Dirac spectrum of instantaneous decoupling; the non-instantaneous heating raises its density today by
  $(N_{\mathrm{eff}}/3)^{3/4} - 1 = 1.08$ %, which the CMB computation of step 6 includes; gravitational clustering is not
  computed.

## The solution of step 5

### Masses, mixing and the evolution

The neutrino masses are the $x_0$ eigenvalues of step 2 with the lightest mass chosen (ASSUMED) and the normal ordering (the
NuFIT 6.0 best fit; the inverted ordering has $\Delta\chi^2 = 6.1$): $\Delta m_{21}^2 = 7.49\times10^{-5}$ eV$^2$,
$\Delta m_{31}^2 = 2.513\times10^{-3}$ eV$^2$, and the sum of the masses $0.0599$ eV lies below the DESI DR2 bound $0.064$ eV
(DERIVED, 16 checks). The flavour amplitudes $\boldsymbol{\psi}$ of a neutrino of energy $E$ evolve with $H_{\mathrm{fl}}$; for
a constant density the evolution operator is the matrix exponential, otherwise the ordered product of the operators of thin
layers, and $\mathcal{P}(\nu_\alpha\to\nu_\beta) = \lvert\mathcal{U}_{\beta\alpha}\rvert^2$ (antineutrinos: $U \to U^*$,
$V \to -V$).

### Vacuum, matter and accelerators

Reactor $\bar\nu_e$ of 4 MeV survive with the probability $0.9183$ at 1.65 km, $0.2263$ at 52.5 km and $0.2674$ at 180 km; the
vacuum $\nu_\mu$ survival has its first minimum, $0.0060$, at $L_{\mathrm{b}}/E = 1516$ km/GeV. The 1-3 MSW resonance lies at
$11.135$ GeV in rock of the density 2.8 g/cm$^3$ with the electron fraction $0.5$; the exact three-flavour Hamiltonian has
$\lvert U^{\mathrm{m}}_{e3}\rvert^2 = 1/2$ (the electron content of the third matter eigenstate) at $11.133$ GeV (agreement
$1.6\times10^{-4}$; with $\Delta m_{31}^2$ alone the resonance formula gives $11.24$ GeV). The 1-2 resonance at the centre of
the Sun ($n_{\mathrm{e}} = 6.02\times10^{25}$ cm$^{-3}$) lies at $1.93$ MeV. Long-baseline appearance in matter of constant
density ($\delta_{\mathrm{CP}} = 212^\circ$, normal ordering; DERIVED):

| experiment | $L_{\mathrm{b}}$ (km) | $E$ (GeV) | density (g/cm$^3$) | $\mathcal{P}(\nu_\mu\to\nu_e)$ | $\mathcal{P}(\bar\nu_\mu\to\bar\nu_e)$ | vacuum $\mathcal{P}(\nu_\mu\to\nu_e)$ | $\mathcal{P}(\nu_\mu\to\nu_\mu)$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T2K | 295 | 0.6 | 2.6 | $0.0517$ | $0.0313$ | $0.0478$ | $0.0085$ |
| NOvA | 810 | 2.0 | 2.84 | $0.0481$ | $0.0236$ | $0.0404$ | $0.1010$ |
| DUNE | 1300 | 2.5 | 2.848 | $0.0701$ | $0.0195$ | $0.0491$ | $0.0098$ |

The matter effect raises the neutrino and lowers the antineutrino appearance for the normal ordering, and the phase
$\delta_{\mathrm{CP}} = 212^\circ$ adds to the asymmetry.

### The Sun

With the electron density $n_{\mathrm{e}}(r) = 6.02\times10^{23}\min(245\,\mathrm{e}^{-10.54\,r/R_\odot}, 100)$ cm$^{-3}$
(ASSUMED profile; $R_\odot$ the solar radius) and production at the radius $r_0$, the adiabatic survival probability is that of
the field equation written above, evaluated at $r_0$; the numerical three-flavour evolution through 20000 and 40000 layers
from $r_0$ to the surface, followed by the incoherent sum over the mass states, $\mathcal{P}_{ee} = \sum_i\lvert
U_{ei}\rvert^2\,\mathcal{P}(\nu_i\to\nu_e)$, gives (DERIVED):

| source | $E$ (MeV) | $r_0/R_\odot$ | $\mathcal{P}_{ee}$ adiabatic | $\mathcal{P}_{ee}$ numerical |
| --- | --- | --- | --- | --- |
| pp | 0.30 | 0.10 | $0.5409$ | $0.5408$ |
| $^7$Be | 0.862 | 0.06 | $0.5197$ | $0.5196$ |
| pep | 1.44 | 0.07 | $0.4978$ | $0.4976$ |
| $^8$B | 5.0 | 0.05 | $0.3771$ | $0.3767$ |
| $^8$B | 10.0 | 0.05 | $0.3194$ | $0.3185$ |
| $^8$B | 15.0 | 0.05 | $0.3055$ | $0.3043$ |

The two agree to $1.3\times10^{-3}$: the conversion is adiabatic, vacuum dominated at low energy
($\mathcal{P}_{ee} \to c_{13}^4(1 - \frac12\sin^22\theta_{12}) + s_{13}^4$) and matter dominated for $^8$B
($\mathcal{P}_{ee} \to c_{13}^4\sin^2\theta_{12} + s_{13}^4$).

![Flavour conversion in UM-2. Left: the solar $\nu_e$ survival probability (adiabatic formula for two production radii, numerical evolution as points). Middle: $\nu_\mu\to\nu_e$ and $\bar\nu_\mu\to\bar\nu_e$ appearance over 1300 km of rock (normal ordering, $\delta_{\mathrm{CP}} = 212^\circ$). Right: the growth rate of the fast flavour instability against the wave number for the three angular distributions of the text.](figures/fig_neutrino_conversion.png)

### The early Universe and $N_{\mathrm{eff}}$

The thermal potential of the $e^\pm$ plasma falls below the vacuum term $\Delta m^2\cos2\theta/(2\lvert\vec k\rvert)$ at the
mean momentum $\lvert\vec k\rvert = 3.15\,T$ when $T = 4.99$ MeV for the atmospheric and $T = 2.39$ MeV for the solar
splitting (DERIVED; $m_{\mathrm{W}}$ of the UM-2 fit): the flavours mix while the neutrinos decouple. The decoupling is computed
from the temperature equations written above (Escudero's method; MeV units; the Planck mass $M_{\mathrm{Pl}} = 1.22091\times10^{19}$
GeV), with the radiatively corrected couplings $0.727$, $0.233$, $-0.273$, $0.233$ (or the UM-2 tree-level couplings with
$\sin^2\theta_{\mathrm{W}} = 0.22363$), the $e^\pm$ density and pressure with the electron mass, and the QED interaction pressure.
The integrals are evaluated with Gauss-Legendre panels, the logarithmic singularity of $\mathcal{Q}_2$ at $k_2 = k$ removed by a
substitution, and the massless limits $p_{\mathrm{QED}}^{(2)} = -5e^2T^4/288$, $p_{\mathrm{QED}}^{(3)} = e^3T^4/(36\sqrt3\pi)$,
$\rho_{\mathrm{e}} = 7\pi^2T^4/60$ are reproduced to $10^{-16}$. The equations run from $T = 20$ MeV to $5$ keV (LSODA, relative
tolerance $10^{-11}$); for instantaneous decoupling at 20 MeV the plasma entropy is conserved and $T_\nu$ falls as
$\mathrm{e}^{-a_4}$. Results (DERIVED):

| run | $N_{\mathrm{eff}}$ | published (Escudero 2020, same method, Table 1 there) |
| --- | --- | --- |
| instantaneous decoupling, no QED | $3.0002$ | $3.000$ |
| instantaneous, $O(e^2)$ QED | $3.0108$ | $3.011$ |
| instantaneous, $O(e^2) + O(e^3)$ | $3.0098$ | $3.010$ |
| Fermi-Dirac energy transfer, one neutrino temperature, no QED | $3.0393$ | $3.039$ |
| the same with $O(e^2)$ | $3.0495$ | |
| the same with $O(e^2) + O(e^3)$ | $3.0485$ | $3.049$ |
| UM-2, separate $\nu_e$ and $\nu_{\mu,\tau}$ temperatures (no oscillations), $O(e^3)$ | $3.0476$ | $3.048$ (separate temperatures) |
| UM-2, separate temperatures, UM-2 tree-level couplings | $3.0472$ | |
| UM-2, one common temperature (efficient oscillations) | $3.0485$ | |

With separate temperatures $T_{\nu_e}/T_\gamma = 0.71732$ and $T_{\nu_\mu}/T_\gamma = 0.71621$; $e^+e^-$ annihilation raises the
comoving neutrino temperatures by $0.265$ % ($\nu_e$, which also has charged-current interactions with the electrons) and $0.109$ %
($\nu_{\mu,\tau}$). The plasma of UM-2 at MeV temperatures is that of the three-flavour Standard Model (the fold bands made by
freeze-in, $\Delta N_{\mathrm{eff}} = 0.001$ in step 9, are decoupled free-streaming radiation, which takes no part in the neutrino
decoupling and is added to $N_{\mathrm{eff}}$ separately), so the precision Standard-Model value with oscillations and the
electron mass in the rates is adopted,

$$
N_{\mathrm{eff}} = 3.0432 \pm 0.0002\qquad \text{(Cielo, Escudero, Mangano and Pisanti 2023)},
$$

<!-- symbols: AUTO -->

from which the computed range $3.0476$ to $3.0485$ differs by $0.0044$ to $0.0053$ (the electron mass in the rates and the
momentum dependence, which the method of temperatures does not resolve).

![Neutrino decoupling in UM-2 (three flavours, separate $\nu_e$ and $\nu_{\mu,\tau}$ temperatures, QED to $O(e^3)$). Left: the neutrino temperatures relative to the photon temperature; right: the comoving heating of the neutrinos by $e^+e^-$ annihilation.](figures/fig_neutrino_decoupling.png)

### The cosmic neutrino background

After decoupling the flavour coherence is lost: the CNB of UM-2 is an incoherent mixture of the three mass eigenstates with
the Fermi-Dirac spectrum at $T_\nu = (4/11)^{1/3}T_\gamma = 1.9454$ K $= 1.676\times10^{-4}$ eV ($T_\gamma = 2.7255$ K today,
STANDARD): $n_i = 112.0$ cm$^{-3}$ ($\nu_i$ and $\bar\nu_i$) for each mass state, and the density parameter of the three states
is (DERIVED)

$$
\Omega_\nu h_{100}^2 = \frac{\sum_{i=1}^{3}\rho_i}{\rho_{\mathrm{crit}}/h_{100}^2} = 6.382\times10^{-4},\qquad
\frac{\rho_{\mathrm{crit}}}{h_{100}^2} = 1.05368\times10^{4}\ \text{eV}/\text{cm}^3,
$$

<!-- symbols: AUTO -->

compared with the non-relativistic value $\sum_im_i/(94.06\ \text{eV}) = 6.363\times10^{-4}$ at this temperature (the
semi-relativistic $\nu_1$, whose energy density exceeds $m_1n_1$ by 16 %, adds $0.3$ %), with the conventional
$\sum_im_i/(93.14\ \text{eV}) = 6.426\times10^{-4}$ (which includes the heating of the non-instantaneous decoupling) and with
$6.451\times10^{-4}$ for the heated spectrum of $N_{\mathrm{eff}} = 3.0432$ (step 6: the degeneracy $N_{\mathrm{eff}}/3$ of each
state corresponds to a Fermi-Dirac spectrum of the temperature $(N_{\mathrm{eff}}/3)^{1/4}T_\nu$, so the non-relativistic
density is multiplied by $(N_{\mathrm{eff}}/3)^{3/4}$). The states (DERIVED):

| state | mass (meV) | $n_i$ (cm$^{-3}$) | $\bar v_i/c$ today | $\lvert U_{ei}\rvert^2$ | $\lvert U_{\mu i}\rvert^2$ | $\lvert U_{\tau i}\rvert^2$ |
| -- | --- | --- | --- | --- | --- | --- |
| $\nu_1$ | $1.000$ | $112.0$ | $0.435$ | $0.677$ | $0.112$ | $0.211$ |
| $\nu_2$ | $8.712$ | $112.0$ | $0.0604$ | $0.301$ | $0.428$ | $0.271$ |
| $\nu_3$ | $50.140$ | $112.0$ | $0.0105$ | $0.022$ | $0.460$ | $0.518$ |

The fold bands of dirac16complex are not part of the CNB (they are never thermalised, step 4; their freeze-in radiation is
counted separately, step 9).

### Supernovae

**The MSW resonances of the envelope.** With the density profile $10^4\,(10^9\,\text{cm}/r)^3$ g/cm$^3$ and the electron fraction
$0.5$ (ASSUMED), a resonance lies at the density $n_{\mathrm{e}}^{\mathrm{res}}$, i.e. at the radius with
$\mathrm{d}\ln n_{\mathrm{e}}/\mathrm{d}r = -3/r$, with the adiabaticity $\gamma_{\mathrm{ad}}$ and the jump probability
$\mathcal{P}_{\mathrm{LZ}}$ of the field equation written above (DERIVED; two-flavour conditions: $\Delta m_{31}^2$ and $\theta_{13}$
for the H resonance, $\Delta m_{21}^2$ and $\theta_{12}$ for the L resonance, without the factor $c_{13}^2$ of the solar condition,
which would move the L densities by 2 %, and without $\Delta m_{ee}^2$, which would move the H densities by 1 %):

| $E$ (MeV) | H (1-3): density (g/cm$^3$) | radius (km) | $\gamma_{\mathrm{ad}}$ | L (1-2): density (g/cm$^3$) | radius (km) | $\gamma_{\mathrm{ad}}$ |
| -- | ---- | --- | -- | ---- | --- | -- |
| 10 | $3147$ | $1.47\times10^4$ | $283$ | $37.7$ | $6.43\times10^4$ | $903$ |
| 20 | $1573$ | $1.85\times10^4$ | $178$ | $18.8$ | $8.10\times10^4$ | $569$ |
| 40 | $787$ | $2.33\times10^4$ | $112$ | $9.42$ | $1.02\times10^5$ | $358$ |

Both resonances are adiabatic ($\mathcal{P}_{\mathrm{LZ}} \le 2.6\times10^{-77}$). For the normal ordering a $\nu_e$ produced in the
core leaves the star as $\nu_3$, $\mathcal{P}(\nu_e\to\nu_e) = \lvert U_{e3}\rvert^2 = 0.02215$, and a $\bar\nu_e$ as $\bar\nu_1$,
$\mathcal{P}(\bar\nu_e\to\bar\nu_e) = \lvert U_{e1}\rvert^2 = 0.677$ (without collective effects and Earth matter). For
representative accretion-phase neutrinospheres (luminosities $6$, $6$, $4\times10^{52}$ erg/s and mean energies $11$, $14$, $15.5$
MeV for $\nu_e$, $\bar\nu_e$ and each heavy-lepton flavour; ASSUMED), number fluxes proportional to the luminosity over the mean
energy and the survival probabilities above, the mean energy observed at the Earth, the flux-weighted mean of the surviving and
the converted spectra, becomes $15.29$ MeV ($\nu_e$) and $14.34$ MeV ($\bar\nu_e$).

**The fast flavour instability.** The electron-lepton-number distribution, the frequencies, the wavenumbers and the growth rates
are measured in units of the self-interaction strength $\sqrt2G_{\mathrm{F}}n_{\nu_e}$ of the $\nu_e$ gas. The roots of the dispersion relation with $\mathrm{Im}\,\bar\omega > 0$ were found
for real $\bar k$ on a grid ($-1.2 \le \bar k \le 1.2$, step $0.1$) by vectorised Newton iterations with the analytic derivative
from a grid of complex starting points (DERIVED):

| angular distributions | ELN crossing | largest growth $\mathrm{Im}\,\bar\omega$ (branch, $\bar k$) | homogeneous mode | mode $k_{\mathrm{f}} = \mathcal{I}_1$ |
| --- | --- | --- | --- | --- |
| $g_{\nu_e} \propto \mathrm{e}^{-(1-u)^2/(2\cdot0.6^2)}$, $g_{\bar\nu_e} \propto \mathrm{e}^{-(1-u)^2/(2\cdot0.4^2)}$, $n_{\bar\nu_e}/n_{\nu_e} = 0.8$ | yes | $0.0877$ (axisymmetric, $\bar k = -0.30$) | $0.0185$ | stable |
| $g_{\nu_e} = 1 + 0.2u$, $g_{\bar\nu_e} = 1 + 0.6u$, $n_{\bar\nu_e}/n_{\nu_e} = 0.9$ | yes | $0.0979$ (axisymmetric, $\bar k = -0.10$) | stable | $0.0917$ |
| as the first, $n_{\bar\nu_e}/n_{\nu_e} = 0.3$ | no | none | stable | stable |

(the largest azimuthal growth rates are $0.0200$ and $0.0050$ for the first two cases). Three
independent evaluations agree to $1.2\times10^{-14}$: the analytic growth of the mode $k_{\mathrm{f}} = \mathcal{I}_1$ against the
root of the dispersion relation at $\bar k = 0$, and the eigenvalues of the discretised homogeneous equation (300 nodes) against
the root at $\bar k = -\mathcal{I}_1$. With an ELN crossing the gas is unstable, without one it is not, as Morinaga's theorem (2022)
states; the second case shows that a stable homogeneous mode does not exclude growing inhomogeneous modes. Near the
neutrinosphere, $n_{\nu_e} = 10^{32}$ to $10^{33}$ cm$^{-3}$ ($\sqrt2G_{\mathrm{F}}n_{\nu_e} = 1.27\times10^{-5}$ to $1.27\times10^{-4}$ eV), the
first case grows by the factor $\mathrm{e}$ in $5.9\times10^{-10}$ to $5.9\times10^{-11}$ s over $17.8$ to $1.78$ cm: a million times
faster than the hydrodynamics, which is why explosion models treat the conversion as instantaneous.

**Flavour conversion and the explosions.** The charged-current heating behind the shock is, schematically, proportional to the sum
over $\nu_e$ and $\bar\nu_e$ of the number flux times the mean squared energy, with the mean squared energy $\frac54$ times the
squared mean energy (spectra with the pinching parameter 3). Full three-flavour equipartition reduces it to $0.884$ of its value,
and pair conversion $\nu_e\bar\nu_e \to \nu_x\bar\nu_x$, which conserves the electron lepton number until $\bar\nu_e$ is
equipartitioned, to $0.760$ (DERIVED, schematic): the heavy-lepton neutrinos are more energetic but fewer and do not heat through
charged currents. Gogilashvili and Tamborra (2026, arXiv:2605.16504) simulated 195 progenitors of 9 to 120 solar masses (GR1D, M1
transport of $\nu_e$, $\bar\nu_e$, $\nu_x$ in 18 energy bins, SFHo equation of state) with instantaneous flavour equipartition,
conserving the electron lepton number and the number and momentum of the neutrinos in each energy bin, imposed at 0.02 s after
bounce where the baryon density is below a threshold (STANDARD, cited):

| threshold density (g/cm$^3$) | no conversion | $10^9$ | $10^{10}$ | $10^{11}$ | $10^{13}$ |
| --- | --- | --- | --- | --- | --- |
| failed explosions | $25.6$ % | $50.8$ % | $77.4$ % | $93.3$ % | $96.4$ % |
| weighted with the Salpeter mass function | $27.0$ % | $47.6$ % | $61.9$ % | $73.9$ % | $88.3$ % |

The effect is strongest between 16 and 30 solar masses (easing the red-supergiant and supernova-rate problems), and the successful
explosions leave lighter neutron stars (gravitational masses around 1.2 to 1.4 solar masses); the authors caution that the large
fractions for deep conversion are in tension with observations and call for dynamical, multi-dimensional treatments.

### Dirac or Majorana

UM-2 gives the neutrinos Dirac masses (the lepton-doublet zero mode mixed at the tip with three right-handed singlets localised at
$\lvert c_R\rvert = 31$ to $35$, tip couplings of order one). The alternative without right-handed neutrinos is a Majorana mass from
the gauge-invariant tip operator

$$
S_{\mathrm{M}} = -\frac12\int_{y=-L}\mathrm{d}^7X_{\mathrm{tip}}\sqrt{\lvert g_{\mathrm{tip}}\rvert}\,\sum_{i,j=1}^{3}
m^{\mathrm{M}}_{ij}\,\tilde\nu_i\tilde\nu_j + \text{h.c.},\qquad \tilde\nu_i = \big(\Sigma^\dagger\ell_i\big)_1
$$

<!-- symbols: AUTO -->

(the upper component $\tilde\nu_i$ of $\Sigma^\dagger\ell_i$ is a left-handed field neutral under $SU(2)_L\times U(1)_Y$, because
$\Sigma \to U_L\Sigma U_Y^\dagger$, and $\tilde\nu_i\tilde\nu_j$ is the Lorentz-invariant Majorana product of two such fields),
whose four-dimensional mass is, to first order in the tip value of the doublet zero mode,

$$
m_i = \mathcal{K}_{\mathrm{M}}^{(i)}\,\frac{\mathcal{Z}(c_L)^2}{fL},\qquad \mathcal{Z}(c_L)^2 = \frac{c_L\,\mathrm{e}^{-c_L}}{\sinh c_L}
 = 8.038\times10^{-5},\qquad \frac{1}{fL} = 22.1\ \text{TeV}
$$

<!-- symbols: AUTO -->

(DERIVED): the measured masses need $\mathcal{K}_{\mathrm{M}}^{(i)} = 5.63\times10^{-13}$, $4.90\times10^{-12}$, $2.82\times10^{-11}$, a
hierarchy that the $x_0$ mechanism does not explain, whereas the Dirac masses come from the localisation with couplings of order
one: the mechanism favours Dirac neutrinos. Neutrinoless double-beta decay would have

$$
m_{\beta\beta} = \Big\lvert\sum_{i=1}^{3}U_{ei}^2\,m_i\,\mathrm{e}^{\mathrm{i}\varphi^{\mathrm{M}}_i}\Big\rvert,\qquad
0.84\ \text{meV} \le m_{\beta\beta} \le 4.41\ \text{meV}
$$

<!-- symbols: AUTO -->

for all Majorana phases $\varphi^{\mathrm{M}}_i$ ($\lvert U_{ei}\rvert^2m_i = 0.677$, $2.624$, $1.111$ meV; the extremes $\sum_i\lvert
U_{ei}\rvert^2m_i$ and twice the largest term minus the sum agree with a scan of the phases), below the reach of present
experiments; the non-relativistic CNB would be captured twice as often as for Dirac neutrinos (both helicities active); the flavour
conversion is the same.

## The check of step 5

**In its own equations.**

* *The flavour evolution.* With the $x_0$ masses and the stored PMNS matrix the evolution operators are unitary to
  $1.3\times10^{-15}$; the exact vacuum evolution reproduces the analytic sum formula to $7.1\times10^{-12}$ (with the masses of the
  roots, which differ from the stored ones by the fit residual; $3.9\times10^{-15}$ with the same masses), CPT holds to
  $2.2\times10^{-16}$ and the T-odd difference to $5.9\times10^{-14}$; the stored T2K, NOvA and DUNE probabilities and the adiabatic
  solar probabilities are reproduced to $4.9\times10^{-13}$ and $4.4\times10^{-13}$ (DERIVED).
* *The onset of the mixing.* The thermal potential equals the vacuum term at the stored temperatures to $8.7\times10^{-12}$
  (DERIVED).
* *The decoupling.* $N_{\mathrm{eff}}$ of instantaneous decoupling without QED, recomputed independently from the separate
  entropy conservation of the $e^\pm\gamma$ plasma with exact Fermi-Dirac integrals, equals the stored $3.00018038904$ to
  $2.7\times10^{-12}$, and the method reproduces the six published values of the same method to $4.6\times10^{-4}$ (DERIVED).
* *The fast flavour instability.* The moments of the distributions, the analytic growth and the eigenvalues of the discretised
  homogeneous equation, recomputed, agree with the stored values to $3.3\times10^{-13}$ (in units of $\sqrt2G_{\mathrm{F}}n_{\nu_e}$) (DERIVED).
* *The CNB.* The number densities, energy densities, mean velocities, flavour contents and $\Omega_\nu h_{100}^2$, recomputed with
  the $x_0$ masses by an independent adaptive quadrature, agree with the stored values to $2.9\times10^{-12}$ (DERIVED).

**In concert with the other field equations.**

* *The masses and the mixing of step 2.* The neutrino masses of the tip conditions and their splittings are those of the flavour
  evolution, the CNB and the CMB computation to $5.7\times10^{-12}$; the PMNS matrix of the flavour evolution and of the flavour
  content of the CNB is the neutrino tip matrix to $8.2\times10^{-13}$ (DERIVED).
* *$N_{\mathrm{eff}}$ and $\Omega_\nu h_{100}^2$ in the CMB.* The CMB computation of step 6 uses $N_{\mathrm{eff}} = 3.0432$ plus the
  freeze-in radiation $0.0010$ of step 9 exactly ($5\times10^{-16}$), and its neutrino density today, $6.4511\times10^{-4}$, equals
  the CNB density times $(N_{\mathrm{eff}}/3)^{3/4}$, $6.4510\times10^{-4}$, to $1.9\times10^{-5}$ (the scaling is exact only for
  non-relativistic states; the semi-relativistic $\nu_1$ leaves this) (DERIVED).
* *The heating factor and the radiation today.* The heating factor $F_{\mathrm{h}}$ of the decoupling is the one used in steps 4
  and 9 to $5.8\times10^{-7}$; the radiation density after decoupling in the thermal history of step 9, which decouples the
  neutrinos instantaneously at 2 MeV ($g_\rho = 3.3626$ today), differs from that of the CMB computation with $N_{\mathrm{eff}} =
  3.0442$ ($3.3827$) by $0.59$ %, a documented approximation of step 9 that enters only the entropy today (taken as the standard
  $g_s = 43/11$) and the nucleosynthesis environment of step 8 (effects below $10^{-58}$) (DERIVED).
* *The $Z$ width of step 4.* $N_\nu = 3$, the number of neutrinos of the decoupling, is the measured invisible width of the $Z$.

## The status of step 5

DERIVED: the flavour evolution in vacuum, matter, the Sun, at accelerators and in the supernova envelope, the onset of the mixing,
the decoupling and the computed $N_{\mathrm{eff}}$, the CNB, the fast-flavour growth rates, the schematic heating ratios, the
Majorana alternative. ASSUMED: the lightest mass and the ordering, the solar and supernova profiles, the neutrinospheres.
STANDARD: the splittings, the mixing angles and the phase (NuFIT 6.0), the adopted precision $N_{\mathrm{eff}} = 3.0432$, the cited
supernova simulations. OPEN: the absolute mass scale and the ordering (chosen here); the collective flavour evolution beyond the
linear analysis.
