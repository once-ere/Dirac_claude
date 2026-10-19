
# The coupled system

## Which fields appear in which equations

Every field of UM-2 obeys its own field equation and enters the equations of the other fields as a source, a mean field, a current
or a parameter. The table lists, for each field, its own equations and the other equations in which it appears.

| field | its own equations | it appears in |
| -------------------- | -------------------------------------- | ------------------------------------------ |
| Einstein-Lovelock gravity $g_{MN}$ (with the block scale $f$) | FE-1, FE-11; the background FE-31 to FE-49; the graviton tower FE-53, FE-54; the block response FE-80; the perturbations FE-87 to FE-90, FE-97 | every equation: the metric in every kinetic term, the spin connection FE-13, the block scale in every $x_0$ problem (FE-50 to FE-79), the expansion rate in FE-110 to FE-136 |
| dirac16complex $\Psi$ | FE-12, FE-13, FE-28; the reduction FE-56; the spectrum and the Kohn-Sham equations FE-62 to FE-69; its levels in matter FE-70 to FE-73; as dark matter FE-91, FE-124 to FE-128; the fold bands FE-129, FE-130, FE-135, FE-136 | the sources of gravity FE-2, FE-3, FE-5, FE-9, FE-10, FE-45 to FE-47, FE-67, FE-80, FE-81, FE-86; the fermion equations FE-14 to FE-19 (I11, I13); the gauge couplings FE-21 to FE-24 and FE-79 (I12); the neutrino hierarchy FE-96 (fold bands); FE-131, FE-132 |
| neutrinos: $\nu_e$, $\nu_\mu$, $\nu_\tau$ in $\ell_i$, and $\nu_{Ri}$ | FE-17, FE-19, FE-29, FE-30; the masses FE-57 to FE-60, FE-100; FE-96; the flavour evolution FE-101 to FE-120; FE-131 to FE-134 | FE-6; the I11 current in FE-12; the currents FE-20, FE-23 to FE-25; FE-26; the mean fields FE-64, FE-70; the plasma FE-121 to FE-123; $N_{\mathrm{eff}}$ in FE-97 |
| charged leptons: $\ell_i$ (lower members) and $e_{Ri}$ | FE-17, FE-18, FE-29, FE-30, FE-57 to FE-60 | FE-6; FE-12 (I11); FE-20, FE-23 to FE-25; FE-26; FE-64, FE-70, FE-73; the baryon fluid FE-92; the neutrino interactions FE-101 to FE-103, FE-109, FE-111 to FE-114; FE-121 |
| quarks: $Q_i$, $u_{Ri}$, $d_{Ri}$ | FE-14 to FE-16, FE-29, FE-30, FE-57 to FE-61 | FE-6; FE-12 (I11, I13); FE-20, FE-22 to FE-25; FE-26; FE-54; FE-64, FE-70, FE-73; the QCD plasma and the nucleon FE-75, FE-83 to FE-85; FE-92; FE-103; FE-121; FE-127 |
| gluons $G^A_M$ | FE-22, FE-27; the massless zero mode FE-50 to FE-52; the condensate FE-74, FE-75 | FE-7, FE-10; FE-12 (I12); FE-14 to FE-16; FE-21; FE-64, FE-71, FE-72, FE-79; the QCD scale FE-81 to FE-84; FE-121; FE-127 |
| photon $A_M$ | FE-25; the massless zero mode FE-50 to FE-52, FE-79; the CMB photons FE-93 to FE-95 | FE-7; FE-12 (I12, through $W^3$ and $B$); FE-20; FE-92; the photon temperature FE-111 to FE-115; FE-121, FE-122 |
| $W^+$, $W^-$, $Z$ | FE-23 to FE-25, FE-51, FE-52, FE-55; the condensates FE-76 to FE-78; FE-79 | FE-7, FE-8; FE-12 (I12); FE-14 to FE-19; FE-26; FE-71, FE-72; the Fermi interactions FE-101, FE-102, FE-109; FE-121; FE-127 |
| tip sigma field $\Sigma$ | FE-26 | the tip energy-momentum tensor FE-8; the tip Yukawa terms of FE-14 to FE-19; the tip currents of FE-23, FE-24; the tip mixing FE-30, FE-60; the Robin parameter of FE-51 |
| block stabiliser $\rho_{\mathrm{stab}}$ | FE-4, FE-41, FE-43 | FE-3; the static block FE-42; the radion and the block response FE-44 to FE-47; the reduction FE-48 |

No Higgs field and no Higgs particle appear in any equation: the masses of $W^\pm$ and $Z$ come from the tip sigma field (FE-51), those of
the fermions from their localisation in $x_0$ and the tip mixing (FE-59, FE-60).

## How the system is solved

The coupled system is solved in eight steps. Each step solves a group of equations exactly or with a controlled approximation, uses
the results of the earlier steps, and is checked by the residual of its solution in the equations it uses (section "What was
verified").

**Step 1: the background.** The background equations FE-38 to FE-40 (with the tensors FE-35 to FE-37 and the conservation law FE-41)
are solved in closed form for a static block with the stabiliser FE-4: FE-42 and FE-43 give $K_* = 12 + \frac43\sqrt{51}$, $f_* = 0.215556$
and $\mathcal{G}(K_*) = 13.8081$. Linearised (FE-44 to FE-46) they give the stable radion ($\omega_{\mathrm{r}} = 3.38705\,H$) and the adiabatic
response of the block to matter (FE-47), and integrated numerically from a deflating primordial block they show how the block reaches
the static point within $x_4 < 1/H$ (deflation rates up to $\lvert\mathcal{H}_f\rvert = 2.63\,H$, the largest deflation of the block scale
$f/f_* = 2.917$, then radion oscillations at $3.3868\,H$ and a dust-like expansion). The reduction FE-48, FE-49 gives four-dimensional
general relativity with $8\pi G_{\mathrm{N}} = \kappa/(\mathcal{G}(K_*)V_\perp)$ and $\Lambda_4 = 0$ at the static point. The block-averaged sources
of matter are included at first order only, with the hidden pressure $\bar p$; the block-shape source $p_0 - p_5$ is not (OPEN).

**Step 2: the masses.** On the static block every mass is an $x_0$ eigenvalue. For the bosons FE-50 to FE-52 give the massless
graviton, photon and gluons, the tower FE-53 (with the potential FE-54) and the $W^\pm$, $Z$ eigenvalues from the tip condition FE-51;
FE-55 fixes $\beta_{\mathrm{W}}$ by the measured electroweak parameter, reproduces $m_{\mathrm{Z}}$ from $m_{\mathrm{W}}$, and fixes the Kaluza-Klein scale
$m_{\mathrm{KK}} = 121.32$ TeV and with it $H = 14.296$ TeV. For the fermions the exact reduction FE-56 gives the zero modes FE-57 and the tip
values FE-58; the mass conditions FE-59 (one generation) and FE-60 (three generations, with the tip matrices of FE-61) reproduce the
twelve measured masses with the right-handed localisations and the measured mixing matrices $U$ and $V_{\mathrm{CKM}}$; the neutrino masses
FE-100 are among them. FE-62 gives the spectrum of dirac16complex: the massless fold bands and the dark matter at $44.35$ TeV.

**Step 3: dirac16complex in Kohn-Sham theory and its back-reaction on the block.** The Kohn-Sham equations FE-63 with the mean
fields FE-64 (densities FE-65, energy FE-66, boundary conditions FE-69) are solved to self-consistency for many-body states of
dirac16complex on the block. Their energy-momentum tensor FE-67 (checked by the identities FE-68) is the source of the background
equations: its block averages $\rho$, $p_3$ and $\bar p = \frac14(p_0 + 3p_5)$ enter the block response FE-45 to FE-47, which changes $f$ and
with it every mass of step 2. The block-shape source $p_0 - p_5$ of these states is up to 4 times $\bar p$ (OPEN).

**Step 4: the portals and the condensates.** On the zero modes the portals become the contact interactions FE-70 (I11, I13) and
FE-71 (I12), with overlaps computed from the Kohn-Sham orbitals. In an environment the levels of dirac16complex shift by the
mean fields of the Standard-Model densities and condensates (FE-72, FE-73), with the condensates of the plasma from FE-74 to FE-78
(QCD trace anomaly, massive vectors, order-$\alpha$ pressure, running couplings without a Higgs particle). Conversely the dark matter
weakens the gauge couplings and changes the $x_0$ problem of $W^\pm$ and $Z$ (FE-79), while the photon and the gluons stay massless.

**Step 5: gravity closes the loop.** In ten environments, from the cosmic mean today to a neutron-star core and the dark-matter
freeze-out (densities FE-86), the block responds to every species through FE-80, with the hidden pressure FE-81 of matter and of the
hot plasma, the block dependence of the gauge couplings FE-82, of the QCD scale and the nucleon mass FE-83, FE-84, and of the fermion
masses FE-85. The loop mass, source, block, mass is iterated to self-consistency; its gain is at most $1.05\times10^{-33}$, so the block
moves by at most $\Delta\ln f = 1.1\times10^{-34}$ (at the freeze-out) and by $7\times10^{-94}$ today.

**Step 6: the neutrino flavours.** With the masses and the tip matrix of step 2, the four-fermion interactions FE-101, FE-102 and the
matter potentials FE-103, the flavour evolution FE-104 is solved exactly in vacuum and in matter (FE-105 to FE-108: accelerator
baselines, the Sun, the Earth, supernova envelopes). In the early Universe the thermal potential FE-109 delays the onset of
oscillations, and the decoupling equations FE-110 to FE-114 give $N_{\mathrm{eff}}$ (FE-115). In dense neutrino gases the linearised kinetic
equations give the fast flavour instability (FE-116 to FE-119). Today the neutrinos form the cosmic neutrino background FE-120.

**Step 7: the thermal history.** With the $x_0$ masses of step 2 the degrees of freedom FE-121 to FE-123 give the expansion of the hot
Universe. The Boltzmann equation FE-124 with the thermal average FE-125, the cross-sections FE-127 and the unitarity bounds FE-128 fixes
the I13 coupling $G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$ by the measured relic density FE-126. The freeze-in FE-129, FE-130 bounds the
I11 coupling by the extra radiation (benchmark $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$ for $\Delta N_{\mathrm{eff}} = 0.001$), the self-interaction
channel FE-135, FE-136 bounds $\lambda$, and FE-131 to FE-134 show that the right-handed neutrinos are never thermalised with the baryon
current in I13 (with a $B - L$ current they would add $\Delta N_{\mathrm{eff}} = 0.144$).

**Step 8: the linear perturbations.** The metric series FE-87 is evaluated term by term: order 1 with $n = 0$ is the four-dimensional
cosmological perturbation theory FE-88 to FE-90, with the species of UM-2 (the dark matter of step 7, FE-91; baryons FE-92; photons
FE-93 to FE-95; the three neutrino mass states of step 2 and the fold bands of step 7, FE-96), the background and primordial spectrum
FE-97; it gives the CMB, CNB and BAO, the potentials FE-98 and $\sigma_8$ (FE-99). The terms $n \ge 1$ are the graviton tower of step 2, the
radion term is the block response of step 5, and order 2 is estimated.

## The solution in concert

The steps share quantities: the same mass, coupling or density enters equations of different steps. UM-2 checks 26 such links, each
the difference between the values of one quantity in two or more equations. 21 of them agree to between $5\times10^{-16}$ and
$1.9\times10^{-5}$, the precision of the stored numbers and of the numerical methods. Five differ by design, each by an amount that the results tolerate: the weak angle of the $x_0$ masses and
of the $Z$ widths (relative change of the total width $8.3\times10^{-3}$, the size of the electroweak loop corrections); the Hubble rate of
the thermal history and of four-dimensional gravity at the freeze-out ($1.7\times10^{-4}$: the thermal history leaves out the fold bands);
the radiation density after neutrino decoupling in the thermal history and in the CMB computation ($5.9\times10^{-3}$: instantaneous
decoupling in the thermal history); the plasma energy density at the freeze-out in the thermal history and in the block sources
($1.3\times10^{-3}$: the trace anomaly of the interacting plasma is in the block sources only); and the radion frequency of the linear and
of the nonlinear evolution ($7.9\times10^{-5}$: measured from the zero crossings of a finite oscillation).
