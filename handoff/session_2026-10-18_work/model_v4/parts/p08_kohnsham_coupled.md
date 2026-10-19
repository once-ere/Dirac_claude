# dirac16complex in the cell: the Kohn-Sham description and the coupled solution

$\Psi$ is quantised canonically with $x_4$ as the time; the anticommutator of the field and its adjoint on a slice carries the indefinite
operator $\mathcal{B}$, which is handled in the good sector by counting the positive branch of every block as particles (the record's
convention, ASSUMED). The interacting many-body state is described by Kohn-Sham theory, coupled to gravity and to all Standard-Model
fields: orbitals of the block Hamiltonian with the mean fields of the self-interaction and of the three portals (the I13 term acts on the
lower component only),

@@FE-63@@

with the mean fields

@@FE-64@@

($n_{\psi i}$ the proper eight-dimensional densities of the Standard-Model fermions of the three generations, $\langle\mathcal{F}\rangle$ the
condensate of the gauge invariant of I12; in the QCD vacuum the gluon condensate, a uniform mass shift), the densities, momentum shells, cell
volume and occupations

@@FE-65@@

($k_{\mathrm{lat}} = 0.25H$ in the computations; the proper seven-volume of a cell, with its hidden extent, is
$2\,\mathrm{Vol}_7(1 - \mathrm{e}^{-3HL})/(3H)$; the occupations are those of the aufbau or of the Mermin functional), the Kohn-Sham energy

@@FE-66@@

and the energy-momentum tensor of a Kohn-Sham state, the source of $\Psi$ in the gravitational equations (its block-averaged pressure
$\bar p = (p_0 + 3p_5)/4$ pushes on the block):

@@FE-67@@

Every self-consistent state satisfies the energy identity and the $y$-conservation law (DERIVED, to $4\times10^{-15}$ and $9\times10^{-8}$ with
Richardson extrapolation)

@@FE-68@@

and the orbitals obey the boundary conditions of dirac16complex (written out again)

@@FE-28@@

in their block form:

@@FE-69@@

The Kohn-Sham solver reproduces the record's reference states to $10^{-13}$; the dark matter at rest has $p_3 = 0$ and
$p_0/\rho = 0.772034 = -\mathrm{d}\ln\varepsilon_{\mathrm{DM}}/\mathrm{d}\ln f$ (two independent computations agree to $10^{-9}$).

## The coupled solution (DERIVED)

The coupled equations are solved by iterating the Kohn-Sham equations of $\Psi$ with the mean fields of the Standard-Model fields and the
response of the block until self-consistency (16 checks). The four-dimensional couplings of a state of $\Psi$ to the Standard-Model fermions
are the overlaps of the portals on the zero modes (written out again):

@@FE-70@@

| zero mode $f$ | $\tilde I_{of}$, dark matter | $\tilde I^{(b)}_{of}$, dark matter | $\tilde I_{of}$, fold band |
| -- | -- | -- | -- |
| quark doublet $Q$ | 8.272 | 2.613 | 6.685 |
| lepton doublet $\ell$ | 1.252 | 0.913 | 1.659 |
| up $u_R$ | 0.385 | 0.379 | 0.792 |
| charm $u_R$ | 0.606 | 0.557 | 1.060 |
| top $u_R$ | 8.272 | 2.613 | 6.685 |
| down $d_R$ | 0.396 | 0.389 | 0.807 |
| strange $d_R$ | 0.462 | 0.446 | 0.893 |
| bottom $d_R$ | 0.762 | 0.661 | 1.221 |
| electron $e_R$ | 0.397 | 0.390 | 0.808 |
| muon $e_R$ | 0.588 | 0.544 | 1.041 |
| tau $e_R$ | 1.252 | 0.913 | 1.659 |
| right-handed neutrinos $\nu_{Ri}$ | 0.302-0.308 | 0.301-0.308 | 0.668-0.678 |

($\nu_{Ri}$: the three right-handed neutrinos; the top and tau singlets share the profile of their doublets, $c_R = -c_L$;
$\tilde I^{(b)}_{of} = 0$ for the fold band.) Each overlap equals the derivative of the self-consistent Kohn-Sham level with respect to the
amplitude of the corresponding mean field to $3\times10^{-10}$ (I11) and $2\times10^{-10}$ (I13; Richardson in the amplitude); in the interacting
state (eight fold zero modes, eight dark-matter quanta, $\lambda_{\mathrm{test}}$) the response is screened by only $3.5\times10^{-4}$. The fold band
stays massless under every I11 mean field (its first-order change of the gap per unit amplitude, $7.9\times10^{-11}$ for the electron density,
$9.3\times10^{-11}$ for the neutrino density and $3.0\times10^{-9}$ for the up-quark density, is rounding; zero in exact arithmetic; the
dispersion stays linear), under the I12 gluon condensate ($1.4\times10^{-10}$, rounding) and under I13 (computed shifts at most
$1.2\times10^{-13}$, rounding; zero in exact arithmetic).

**The Standard-Model fields acting on $\Psi$** in ten environments. To first order in the mean fields (Hellmann-Feynman; universal I12
coefficients) a Kohn-Sham level moves by

@@FE-72@@

and with unpolarised fermions (each chirality carries half of the density) and the net quark densities of protons and neutrons the
dark-matter level moves by

@@FE-73@@

The gluon condensate follows from the trace anomaly of QCD,

@@FE-74@@

with the QCD interaction measure (a lattice-like shape below 1 GeV, an ESTIMATE, and leading-order perturbation theory above, with $\alpha_3$
at the scale $2\pi T$)

@@FE-75@@

For the massive vector bosons the free part of the thermal condensate follows from the on-shell Proca Lagrangian, and above $m_{\mathrm{W}}$ the
interaction pressure of the electroweak plasma dominates (Feynman-Hellmann; for QCD it reproduces the trace-anomaly condensate exactly,
DERIVED to $10^{-16}$; for $SU(2)$ $d_{\mathrm{adj}} = 3$, $C_{\mathrm{adj}} = 2$ and twelve Weyl doublets, $T_{\mathrm{F}}N_{\mathrm{f}} = 3$; for $U(1)_Y$
$d_{\mathrm{adj}} = 1$, $C_{\mathrm{adj}} = 0$ and $\frac52T_{\mathrm{F}}N_{\mathrm{f}} \to \frac{25}{2}$; no scalar term, ESTIMATE; below $m_{\mathrm{W}}$ the
order-$\alpha$ part is multiplied by the thermal suppression of a massive vector, ESTIMATE):

@@FE-76@@

with the couplings taken at $\mu_{\mathrm{ren}} = 2\pi T$, one loop from the $\overline{\mathrm{MS}}$ values at $m_{\mathrm{Z}}$ without a Higgs particle
($\alpha_{\mathrm{em}} = 1/127.95$, $\sin^2\theta_{\overline{\mathrm{MS}}} = 0.23122$),

@@FE-77@@

Hence the electroweak condensates of the hot plasma

@@FE-78@@

At the freeze-out $\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle = -8.1\times10^{12}$ GeV$^4$, $\langle W^I_{\mu\nu}W^{I\mu\nu}\rangle = -5.0\times10^{11}$ GeV$^4$ (almost all from
the interaction part) and $\langle B_{\mu\nu}B^{\mu\nu}\rangle = -2.6\times10^{10}$ GeV$^4$ (geometric normalisation). The densities of the hot
environments are

@@FE-86@@

($\eta_{\mathrm{b}} = 6.1\times10^{-10}$, $m_{\mathrm{n}} - m_{\mathrm{p}} = 1.293$ MeV; the dark matter in thermal equilibrium for both species while
$M_{\mathrm{DM}}/T < 40$, its relic density afterwards). The cold environments are given by their matter: the cosmic mean today (the Planck
baryon density with the helium fraction $0.2457$ and $\Omega_{\mathrm{DM}}h_{100}^2 = 0.120$); the Galaxy at the Sun (one proton and one electron
per cm$^3$, dark matter $0.4$ GeV/cm$^3$); the Earth (mean density $5.51$ g/cm$^3$ with 48 % protons); the centre of the Sun (150 g/cm$^3$, 66 %
protons, 32 % neutrons); a white dwarf ($10^6$ g/cm$^3$ of carbon and oxygen, equal numbers of protons and neutrons); a neutron-star core
($0.3$ fm$^{-3}$ with 10 % protons, as many electrons as protons); the local dark-matter density $0.4$ GeV/cm$^3$ in all bound objects.
Results (DERIVED):

| environment | $\Delta\varepsilon_{\mathrm{DM}}/M_{\mathrm{DM}}$ | $\Delta\ln f$ |
| --- | --- | --- |
| cosmic mean today; the Galaxy at the Sun; the Earth; the centre of the Sun; a white dwarf | $8.4\times10^{-20}$ (the QCD vacuum condensate) | $7\times10^{-94}$ to $2\times10^{-57}$ |
| neutron-star core ($0.3$ fm$^{-3}$) | $1.0\times10^{-16}$ | $9\times10^{-49}$ |
| nucleosynthesis ($T = 1$ MeV) | $8.4\times10^{-20}$ | $7\times10^{-60}$ |
| QCD crossover ($T = 200$ MeV) | $4.4\times10^{-20}$ | $3\times10^{-48}$ |
| electroweak era ($T = 100$ GeV) | $-5.5\times10^{-11}$ | $7\times10^{-39}$ |
| dark-matter freeze-out ($T = 1.42$ TeV, $x_{\mathrm{f}} = 31.23$) | $-1.5\times10^{-6}$ | $1.1\times10^{-34}$ |

**$\Psi$ acting on the Standard Model.** Through I12 the scalar density of the dark matter shifts the gauge couplings, and through the kinetic
function of the gauge fields along $x_0$ it changes the $x_0$ eigenvalue of the $W$:

@@FE-79@@

The coupling shifts are at most $1.7\times10^{-16}$ (at the freeze-out), $10^{-36}$ from nucleosynthesis on and $2\times10^{-60}$ today in the
Galaxy; the eigenvalue of the $W$ changes by $\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}} = -0.11125$ per unit amplitude (first-order
perturbation theory, confirmed by shooting to $3\times10^{-11}$; version 3 quoted $-0.1126$ from finite elements, limited by rounding), while
the photon and the gluons stay exactly massless (their zero mode has no slope, so the shift vanishes identically); at the physical amplitude
of the freeze-out the shift of $\tilde m_{\mathrm{W}}^2$ is $1.9\times10^{-17}$.

**Gravity closes the loop.** The block responds to the block-averaged sources of all species with the adiabatic response of the gravity section:

@@FE-80@@

in which radiation drops out exactly ($c_3 = -3c_\rho$), so only the trace $\rho - 3p_3$ and the hidden pressure act. The hidden pressure is the
response of the pressure to the block scale at fixed temperature, $\bar p = \frac14\,\partial p/\partial\ln f$:

@@FE-81@@

(the plasma species as ideal gases with their $x_0$ masses, the nucleons and electrons of the cold environments as degenerate Fermi gases,
the QCD plasma through its scale, the electroweak plasma through its couplings), with the block dependence of a gauge coupling and the trace
of an electroweak plasma (the bulk couplings scale as $f^{-4}$ and $m_{\mathrm{KK}}$ as $1/f$; leading-order trace anomaly)

@@FE-82@@

The nucleon pushes through the QCD scale (one loop, ESTIMATE; $\sigma_{\pi N} = 45$ MeV and $\sigma_{\mathrm{s}} = 40$ MeV from memory):

@@FE-83@@

@@FE-84@@

with the quark sensitivities of the block dependence of a fermion mass (written out again)

@@FE-85@@

$\mathrm{d}\ln m/\mathrm{d}\ln f = -18.82$, $-18.01$, $-14.90$, $-12.15$, $-10.89$, $-6.77$ for the up, down, strange, charm, bottom and top quarks, so
that $\alpha_3(m_{\mathrm{KK}}) = 0.0606$, $\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(6)}/\mathrm{d}\ln f = -60.2$, $\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(3)}/\mathrm{d}\ln f = -49.0$ and
$\mathrm{d}\ln m_{\mathrm{p}}/\mathrm{d}\ln f = -46.1$: the nucleon mass is the most block-sensitive mass of UM-2, more than the lightest neutrino ($-41.0$).
The result: $\Delta\ln f \le 1.1\times10^{-34}$, at the freeze-out, where the hot plasma has $\bar p = 3.1\times10^{12}$ GeV$^4$ (mostly the QCD
interaction measure with $\mathrm{d}\ln\Lambda_{\mathrm{QCD}}/\mathrm{d}\ln f = -60$) and $\rho - 3p_3 = 2.2\times10^{11}$ GeV$^4$; at most $9\times10^{-49}$ from
nucleosynthesis to today; the gain of the loop mass $\to$ source $\to$ block $\to$ mass is at most $1.1\times10^{-33}$, so the iteration converges at
once. (The plasma energy density at the freeze-out in these block sources, $1.4161\times10^{14}$ GeV$^4$, exceeds that of the ideal-gas thermal
history by 0.13 %, by design: the block sources contain the trace anomaly of the interacting plasma; residual analysis.)

**Domain of validity.** The I12 benchmark changes the strong coupling by 10 % through the thermal dark-matter density only at $T = 27$ TeV
($M_{\mathrm{DM}}/T = 1.6$): the coupled effective description holds through the freeze-out and everything later.

![The coupled solution. Left: the $x_0$ profiles that enter the overlaps of FE-70 against $Hy$ (fold at 0, tip at $-3$): the dark-matter orbital $a^2 + b^2$, the fold band and, scaled, the zero modes of the quark doublets, the lepton doublets (labelled L in the figure) and two singlets. Right: the shift of the dark-matter level by the Standard-Model mean fields in the ten environments, the decimal logarithm of its ratio to $M_{\mathrm{DM}}$ (labelled M in the figure).](figures/fig_coupled.png)

