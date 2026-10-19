
# The three neutrino flavours

The three flavours of left-handed neutrinos are the upper members of the lepton doublets $\ell_i$. Their masses come from the tip
mixing with the right-handed neutrinos (FE-59, FE-60), their mixing from the tip matrix $\mathcal{K}_\nu = U$, and their interactions from
the exchange of $W^+$, $W^-$ and $Z$. This section collects the equations of their masses, of their interactions at low energy and of
their flavour evolution in vacuum, in matter, in the early Universe and in dense neutrino gases, and the cosmic neutrino
background.

## The masses and the interactions at low energy

@FE-100

**The terms.** The masses of the three mass states $\nu_1$, $\nu_2$, $\nu_3$: the lightest mass $m_1$ is chosen and the ordering is normal
(ASSUMED), the two splittings $\Delta m_{21}^2 = 7.49\times10^{-5}$ eV$^2$ and $\Delta m_{31}^2 = 2.513\times10^{-3}$ eV$^2$ are the measured ones
(NuFIT 6.0). In UM-2 they are Dirac masses and $x_0$ eigenvalues of FE-59: the doublet localisation $c_L = 5.95288$ of the leptons and the
right-handed localisations $c_R = -35.0452$, $-32.8481$, $-31.0702$, with tip mixing of order one; the smallness of the masses comes from
the sharp localisation of the right-handed neutrinos at the fold. Status: ASSUMED ($m_1$, ordering), STANDARD (splittings), DERIVED (as
$x_0$ eigenvalues). The same masses enter the flavour evolution, the cosmic neutrino background and the CMB computation (they agree
across the three to $5.7\times10^{-12}$).

@FE-101

**The terms.** At momentum transfers far below $m_{\mathrm{W}}$ and $m_{\mathrm{Z}}$ the exchange of $W^\pm$ (FE-25) between the zero modes of the
lepton doublets gives the charged-current contact interaction $\mathcal{L}_{\mathrm{CC}}$ between the neutrino and the charged lepton of the
same flavour, and the exchange of the $Z$ the neutral-current interaction $\mathcal{L}_{\mathrm{NC}}$ of the neutrinos with every fermion $f$ of
the medium, with the chiral couplings $\tilde g^f_L$ and $\tilde g^f_R$. $P_L$ and $P_R$ project on the left-handed and right-handed zero
modes. The flavour states $\nu_\alpha$ ($\alpha = e, \mu, \tau$) are the combinations of the mass states with the mixing matrix $U$, the tip
matrix of the neutrino sector. Status: STANDARD.

@FE-102

**The terms.** The Fermi constant is fixed by the four-dimensional SU(2) coupling and the $W$ mass; the neutral-current couplings of a
fermion with the weak isospin $T_3^f$ and the charge $Q_{\mathrm{em}}^f$ contain the weak angle; $\tilde g^f_V$ is the vector coupling that acts
in an unpolarised medium. Status: STANDARD; UM-2 uses the measured $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$. The weak angle has two
values in UM-2: the tree-level angle of the $x_0$ masses ($\sin^2\theta_{\mathrm{W}} = 1 - 0.776368 = 0.22363$, FE-55) and the
$\overline{\mathrm{MS}}$ angle $\sin^2\theta_{\overline{\mathrm{MS}}} = 0.23122$ used in the couplings of the $Z$ widths; the difference changes the total
$Z$ width by $8.3\times10^{-3}$, the size of the electroweak loop corrections that UM-2 does not compute.

## Vacuum and matter

@FE-103

**The terms.** Coherent forward scattering on the medium gives each flavour the potential $V_\alpha$: the charged current acts on
$\nu_e$ only, with the net electron density; the neutral current acts on every flavour with the net densities $n_f - n_{\bar f}$ of the
fermions of the medium weighted by $\tilde g^f_V$. In neutral matter of electrons, protons and neutrons the neutral-current terms of
the electrons and the protons cancel ($\tilde g_V$ of the proton, two up quarks and one down quark, is minus that of the electron) and
the neutrons leave $V_{\mathrm{NC}} = -G_{\mathrm{F}}n_{\mathrm{n}}/\sqrt2$, common to all flavours. Status: STANDARD (an unpolarised medium at rest;
antineutrinos have $-V$).

@FE-104

**The terms.** $\boldsymbol{\psi}$ is the vector of the three flavour amplitudes of a neutrino of energy $E$; the flavour Hamiltonian
$H_{\mathrm{fl}}$ contains the vacuum part (the squared masses rotated with $U$) and the matter potential $V$. For a constant density the
evolution over the baseline $L_{\mathrm{b}}$ is the matrix exponential $\mathcal{U}$, and $\mathcal{P}$ is the probability of the flavour change.
The common part $V_{\mathrm{NC}}\mathbf{1}$ is a phase and drops out. Status: STANDARD (solved exactly: matrix exponential for constant density,
ordered products of layers otherwise; the vacuum formula FE-105 is reproduced to $3.9\times10^{-15}$, unitarity to $1.8\times10^{-15}$).
Residual of the stored probabilities (unitarity, vacuum formula, CPT, the T2K, NOvA and DUNE probabilities, the solar survival
probability) $7.1\times10^{-12}$.

@FE-105

**The terms.** In vacuum the probability is the squared sum of three amplitudes with the phases $m_i^2L_{\mathrm{b}}/(2E)$; CPT symmetry
relates neutrinos and antineutrinos; the difference of the probabilities of a process and its time reverse is proportional to the
Jarlskog invariant $J_{\mathrm{CP}}$ (CP violation of the tip matrix) and to the three oscillation phases $\Delta_{ij}$. Status: STANDARD (CPT
checked to $2.8\times10^{-16}$, the T-odd difference to $5.9\times10^{-14}$).

In the two-flavour approximation of one sector (for example the 1-2 sector with $\theta_{13} = 0$) the flavour Hamiltonian of FE-104
is, up to a multiple of $\mathbf{1}$,

@@
H_{\mathrm{fl}} = \frac{\Delta m_{21}^2}{4E}\begin{pmatrix}-\cos2\theta_{12} & \sin2\theta_{12}\\ \sin2\theta_{12} &
 \cos2\theta_{12}\end{pmatrix} + \begin{pmatrix}V_{\mathrm{CC}} & 0\\ 0 & 0\end{pmatrix},
@@

whose two diagonal entries are equal, and the mixing in matter maximal, at $2EV_{\mathrm{CC}} = \Delta m_{21}^2\cos2\theta_{12}$; with the third
flavour the conditions become:

@FE-106

**The terms.** The resonance conditions of the 1-3 sector (with the effective splitting $\Delta m_{ee}^2$, the $\nu_e$-weighted average of
$\Delta m_{31}^2$ and $\Delta m_{32}^2$) and of the 1-2 sector (with the factor $c_{13}^2$, the $\nu_e$ content of the 1-2 subspace). Status:
STANDARD. The 1-3 resonance lies at 11.135 GeV in rock of 2.8 g/cm$^3$ (the exact three-flavour evolution gives 11.133 GeV); the 1-2
resonance at the centre of the Sun at 1.93 MeV.

@FE-107

**The terms.** The survival probability of solar electron neutrinos produced at a density where $A_{\mathrm{MSW}}$ is the ratio of the
matter term to the vacuum term: the mixing angle in matter $\theta^{\mathrm{m}}_{12}$ at the production point, adiabatic evolution to the
surface, and decoherence on the way to the Earth; the 1-3 sector enters through $c_{13}^4$ and $s_{13}^4$. Status: STANDARD (the numerical
three-flavour evolution through the solar density agrees to $1.3\times10^{-3}$, the size of the non-adiabatic and production-region
effects that the formula drops).

@FE-108

**The terms.** The electron density at the resonance, the adiabaticity parameter $\gamma_{\mathrm{ad}}$ (the ratio of the oscillation length at
the resonance to the width of the resonance region; the evolution is adiabatic for $\gamma_{\mathrm{ad}} \gg 1$), and the Landau-Zener
probability $\mathcal{P}_{\mathrm{LZ}}$ of a jump between the matter eigenstates. Status: STANDARD (two-flavour conditions; in a supernova
envelope both resonances are adiabatic, $\mathcal{P}_{\mathrm{LZ}} \le 2.6\times10^{-77}$).

## The early Universe

@FE-109

**The terms.** In the hot plasma the net electron density is tiny (of the order of $\eta_{\mathrm{b}} = 6.1\times10^{-10}$ times the photon
density), and the leading potential is the thermal one: the
$W$ propagator expanded to the next order in $\lvert\vec k\rvert T/m_{\mathrm{W}}^2$, proportional to the energy density $\rho_{\mathrm{e}}$ of the
electrons and positrons. It suppresses the flavour mixing at high temperature. Status: STANDARD (leading order in $T/m_{\mathrm{W}}$; it falls
below the vacuum term at $T = 4.99$ MeV for the atmospheric splitting and 2.39 MeV for the solar one, at $\lvert\vec k\rvert = 3.15\,T$).
Residual $8.7\times10^{-12}$; the neglected CP-asymmetric potential of the net electron density is $1.1\times10^{-2}$ of the thermal one at the
onset (ESTIMATE).

@FE-110

**The terms.** The density matrix $\boldsymbol{\rho}_{\vec k}$ of the neutrinos of momentum $\vec k$ (its diagonal the occupation numbers of the
flavours, its off-diagonal entries the flavour coherence; $\bar{\boldsymbol{\rho}}$ that of the antineutrinos) evolves by the commutator with
the vacuum Hamiltonian $H^{\mathrm{vac}}$, the matter potential and the neutrino-neutrino potential $V_{\nu\nu}$ (forward scattering on the
other neutrinos, with the angular factor of the current-current interaction), and by the collision term $C_{\mathrm{coll}}$; in the
expanding Universe the momenta redshift. Status: STANDARD. It is used linearised for the fast flavour instability (FE-117) and
momentum-averaged for the decoupling (FE-111).

@FE-111

**The terms.** The momentum-averaged form of FE-110 for the temperatures of the photons and of the neutrino flavours: the photon
temperature falls by the expansion (the dilution of the photons, of the electron-positron plasma and of the QED interaction pressure
$p_{\mathrm{QED}}$) and rises by the energy that the collisions $C_{\nu_\alpha}$ take from the neutrinos; each neutrino temperature falls with the
expansion and changes by its collisions. The Hubble rate follows from the total energy density. Status: STANDARD (integrated from 20 MeV
to 5 keV with LSODA, relative tolerance $10^{-11}$; the method reproduces the published values of Escudero (2020) to $5\times10^{-4}$; $\nu_\tau$
follows $\nu_\mu$). Residual $2.7\times10^{-12}$.

@FE-112

**The terms.** The rates of energy transfer between the electron-positron plasma and the neutrinos (annihilation and scattering, with
the couplings $\tilde g^{\nu_e e}$ and $\tilde g^{\nu_\mu e}$; the electron neutrinos also have the charged current) and between the neutrino
flavours; $\mathcal{F}_{\mathrm{tr}}$ is the transfer function between two thermal baths of temperatures $T_{\mathrm{A}}$ and $T_{\mathrm{B}}$, with the
factors $f_{\mathrm{a}} = 0.884$ and $f_{\mathrm{s}} = 0.829$ of the Fermi-Dirac statistics. Status: STANDARD (the radiatively corrected couplings
0.727, 0.233, $-0.273$, 0.233 are used; the tree-level ones change $N_{\mathrm{eff}}$ by $4\times10^{-4}$).

@FE-113

**The terms.** The finite-temperature QED correction to the pressure of the electron-photon plasma at order $e^2$ and $e^3$, from the
integrals of FE-114; $\rho_{\mathrm{QED}}$ follows by the thermodynamic relation. It raises $N_{\mathrm{eff}}$ by 0.009 (the decoupling computed
with and without it). Status: STANDARD (the massless limits $-5e^2T^4/288$ and $e^3T^4/(36\sqrt3\,\pi)$ reproduced to $10^{-16}$).

@FE-114

**The terms.** The momentum integrals over the electron and positron distribution $n_{\mathrm{D}}$ (two spin states, energy $E$ with the electron
mass $m_{\mathrm{e}}$). Status: STANDARD (Gauss-Legendre panels; the logarithmic singularity at $k_2 = k$ removed by a substitution).

For instantaneous decoupling the entropy of the electron-positron plasma goes to the photons alone, and

@@
T_{\nu_e} = T_{\nu_\mu} = \Big(\frac{4}{11}\Big)^{1/3}T_\gamma\quad\Rightarrow\quad
N_{\mathrm{eff}} = \Big(\frac{11}{4}\Big)^{4/3}\cdot3\Big(\frac{4}{11}\Big)^{4/3} = 3.
@@

@FE-115

**The terms.** The effective number of neutrino species measures the energy density of the neutrinos relative to that of three
species decoupled instantaneously; the second relation is the common-temperature form (efficient oscillations). Status: STANDARD.
UM-2 computes 3.0476 (separate temperatures) and 3.0485 (common temperature) and adopts the precision value 3.0432 (Cielo et al. 2023);
the difference, $4\times10^{-3}$, is the electron-mass and momentum dependence that the temperature method omits. The fold bands add 0.0010
(FE-129, FE-130); the sum agrees with the value in the CMB computation to $5\times10^{-16}$.

## Dense neutrino gases

@FE-116

**The terms.** In a dense, homogeneous and axially symmetric gas of electron neutrinos and antineutrinos (near the neutrinosphere of
a supernova), $G_{\mathrm{ELN}}$ is the electron-lepton-number distribution over the cosine $u$ of the angle to the symmetry axis $x_3$, with
the normalised angular distributions $g_{\nu_e}$, $g_{\bar\nu_e}$ and the densities $n_{\nu_e}$, $n_{\bar\nu_e}$; $\mathcal{I}_l$ are its moments.
Status: STANDARD.

@FE-117

**The terms.** The linearised FE-110 for a small flavour coherence $\mathcal{C}(u)$ with the frequency $\omega_{\mathrm{f}}$ and the wave number
$k_{\mathrm{f}}$ along the axis (shifted by the moments, $\bar\omega$, $\bar k$): non-trivial solutions need $\det\Pi = 0$, the dispersion relation
of fast flavour waves. Status: STANDARD (roots for real $k_{\mathrm{f}}$ by vectorised Newton iterations; three independent evaluations agree
to $1.2\times10^{-14}$).

@FE-118

**The terms.** The dispersion relation splits into the axisymmetric branch (the first equation, with the moments $\mathcal{J}_l$) and the
azimuthal branch (the second). A root with $\mathrm{Im}\,\bar\omega > 0$ for real $\bar k$ grows exponentially: the fast flavour instability.
Status: STANDARD (with a crossing of the electron-lepton-number distribution the largest growth rate is $0.088\sqrt2\,G_{\mathrm{F}}n_{\nu_e}$; without
one no mode grows).

@FE-119

**The terms.** The homogeneous equation for $\mathcal{C}(u)$ and the quadratic equation of the mode $k_{\mathrm{f}} = \mathcal{I}_1$, whose imaginary
part gives the growth rate in closed form. Status: STANDARD (the eigenvalues of the discretised equation, 300 nodes, agree with the
dispersion relation; near the neutrinosphere the coherence grows by a factor $\mathrm{e}$ in $6\times10^{-10}$ to $6\times10^{-11}$ s). Residual
of the stored moments, growth rates and eigenvalues $3.3\times10^{-13}$.

## The cosmic neutrino background

@FE-120

**The terms.** Today the relic neutrinos are three mass states (decoherent), each with the Fermi-Dirac distribution of the
temperature $T_\nu$ (the momenta redshift, so the massless form is kept), the number density $n_i$, the energy density $\rho_i$ with the
mass $m_i$, and the mean velocity $\bar v_i$; the flavour content of $\nu_i$ is $\lvert U_{\alpha i}\rvert^2$. Status: STANDARD (exact integrals):
$T_\nu = 1.9454$ K, 112.0 per cm$^3$ per mass state, mean velocities 0.435, 0.0604 and 0.0105 (in units of the speed of light), and
$\Omega_\nu h_{100}^2 = 6.382\times10^{-4}$ (the value in the CMB computation agrees to $1.9\times10^{-5}$). Residual $2.9\times10^{-12}$.
