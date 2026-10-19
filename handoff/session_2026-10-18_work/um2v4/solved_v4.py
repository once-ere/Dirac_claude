"""The `solved_in` notes of the inventory in the notation of version 4 (inline math in $...$), keyed by the equation id.
Equations not listed keep the note written with them in the eq_*.py modules."""
SOLVED = {
 'IN-5': r"Gives FE-5 and FE-12; solved by the exact $x_0$ spectrum (FE-62) and by Kohn-Sham theory (FE-63 to FE-69); the "
         r"self-coupling $\lambda$ is bounded by the fold-band radiation (FE-135).",
 'IN-6': r"The author's real $16 \times 16$ matrices satisfy the algebra exactly (31 checks); $\mathcal{B}$ commutes with every "
         r"interaction of the good sector, so the two halves are conserved separately.",
 'IN-7': r"Evaluated exactly for the order-0 metric (FE-13); it makes $\gamma^N$ covariantly constant (verified symbolically).",
 'IN-8': r"Gives FE-7 and the Yang-Mills equations FE-22 to FE-25; their $x_0$ reduction gives the massless photon and gluons and "
         r"the $W^\pm$ and $Z$ masses (FE-50 to FE-55).",
 'IN-9': r"Exact definitions; the non-abelian terms are kept in FE-22 to FE-24 and neglected in the linearised $W^\pm$, $Z$ and "
         r"photon equations FE-25.",
 'IN-10': r"$W^+$ carries the electric charge $+e$ and $W^-$ the charge $-e$ (DERIVED); $Z$ and $A$ are the neutral combinations; "
          r"the angle of the couplings is fixed by the measured masses (FE-55).",
 'IN-13': r"Gives FE-8, the tip terms of FE-14 to FE-19 and of FE-23, FE-24, and the sigma-field equation FE-26; on the static "
          r"block it becomes the Robin condition of the $W^\pm$ and $Z$ profiles (FE-51) and the tip mixing of the fermions (FE-30).",
 'IN-15': r"Exact; the photon receives no tip term, so it stays massless; $W^+$ and $W^-$ share one mass (particle and antiparticle).",
 'IN-18': r"Enters FE-9, FE-12 and FE-14 to FE-16; the bilinear is Hermitian for $M \ne x_0$ only (DERIVED); on the zero modes it "
          r"is FE-70, its strength fixed by the dark-matter relic (FE-126).",
 'FE-1': r"Solved exactly at order 0 (the background equations FE-38 to FE-40, integrated numerically through the primordial era "
         r"and solved in closed form for the static block); at order $\epsilon$ through the four-dimensional reduction FE-49.",
 'FE-4': r"Exact; conserved because $\rho_{\mathrm{stab}} \propto f^{-8}$; it sets the static block FE-43.",
 'FE-5': r"Evaluated for Kohn-Sham states in the form FE-67 (verified: energy identity and $y$-conservation law FE-68).",
 'FE-6': r"Used through the block averages of the plasma and of cold matter (ideal and degenerate gases with the $x_0$ masses) "
         r"in the block response FE-45 and the hidden pressure FE-81.",
 'FE-7': r"Used through the radiation and order-$\alpha_{\mathrm{G}}$ plasma pressures in the block response; radiation drops out "
         r"of it exactly.",
 'FE-8': r"Zero for the hidden component; its gravitational effect is part of the $W^\pm$, $Z$ and fermion rest energies counted "
         r"in the plasma.",
 'FE-9': r"Exact (the frame currents do not depend on the vielbein); negligible against the stabiliser in every environment (the "
         r"level shifts of FE-72 are below $10^{-9}$ GeV).",
 'FE-10': r"Exact; I12 acts as a field-dependent gauge coupling FE-21; its effect is computed in the coupled solution (at most "
          r"$1.7\times10^{-16}$).",
 'FE-11': r"The Bianchi identities were verified for the order-0 metric ($p = 1, 2, 3$); the conservation holds on the matter "
          r"field equations; at order 0 it is FE-41.",
 'FE-12': r"Reduced exactly to the block Hamiltonian FE-56 (all eight blocks, general $a_4$, $b_4$); solved exactly for the free "
          r"spectrum FE-62 and by Kohn-Sham theory with the portal mean fields FE-63.",
 'FE-13': r"Exact for every $a_4$, $b_4$ and on both halves of a period; removed by the factors of the reduction ansatz FE-56; it "
          r"vanishes only in flat 4+4 space.",
 'FE-14': r"Solved on the static block by the zero mode and the tip mixing FE-56 to FE-60 (exact roots; the portal terms are mean "
          r"fields of relative size $10^{-17}$ at most).",
 'FE-15': r"As FE-14: singlet zero modes mixed at the tip with the doublet (exact roots for the up, charm and top quarks).",
 'FE-16': r"As FE-14 (exact roots for the down, strange and bottom quarks; the tip matrix of the sector is the CKM matrix).",
 'FE-18': r"As FE-17 (exact roots for the electron, muon and tau with the tip matrix $\mathbf{1}$).",
 'FE-19': r"Gauge singlets: sharply localised singlet zero modes ($c_R = -31$ to $-35$) mixed at the tip with the lepton doublet "
          r"give the Dirac neutrino masses; never thermalised (their I11 production is computed in FE-134).",
 'FE-21': r"Exact; in four dimensions it is the coupling shift FE-79 (at most $1.7\times10^{-16}$ at the dark-matter freeze-out).",
 'FE-22': r"Solved on the static block by the $x_0$ reduction FE-50 with no tip term: the gluon zero mode is exactly massless "
          r"(flat profile); QCD below the confinement scale enters through the nucleon masses and the condensates FE-74.",
 'FE-23': r"The tip term (in the unitary gauge; $N$ runs over the tip directions) is a mass term for the charged components and "
          r"for $W^3 - B$ only; solved on the static block by FE-50 with the Robin condition FE-51.",
 'FE-25': r"Obtained exactly from FE-23 and FE-24 at linear order; the photon has no tip term and stays massless; the $W^\pm$ and "
          r"$Z$ tip terms become the Robin conditions FE-51.",
 'FE-26': r"Not independent: it is the divergence of the tip part of FE-23 (the fermion currents are conserved up to the same tip "
          r"terms); in the unitary gauge the three modes of $\Sigma$ are the longitudinal $W^+$, $W^-$ and $Z$.",
 'FE-27': r"Lagrangian boundary conditions of the variational principle; for an $x_0$ profile they are FE-51.",
 'FE-29': r"Self-adjoint (DERIVED); each doublet has one Weyl zero mode with $\Gamma_4 = +1$ and each singlet one with "
          r"$\Gamma_4 = -1$, in the two selected blocks of the half $\mathcal{B} = -1$; at the tip modified by the mixing "
          r"conditions FE-30.",
 'FE-31': r"The corrected primordial metric of the record (author's coordinates, $x_0$ first); its curvature is computed exactly "
          r"(sympy, identical in both charts) and does not depend on $x_0$.",
 'FE-32': r"Exact change of chart; one period of $x_0$ (length $\pi/(6H)$) is two halves joined at the fold $y = 0$, each closed "
          r"by the regular tip at $y = -L$ ($HL = 3$, ASSUMED).",
 'FE-33': r"Exact (sympy, both charts, 25 checks); $x_1$, $x_2$, $x_3$ are equivalent, and $x_0$, $x_5$, $x_6$, $x_7$ are "
          r"equivalent.",
 'FE-34': r"Exact (the coefficients are $2^pp!$ and $-2^{p-1}p!$ for the order $p$); checked against the Ricci route ($p = 1$), "
          r"the explicit Gauss-Bonnet tensor ($p = 2$), the Bianchi identities and the minisuperspace variation with a lapse "
          r"($p = 1, 2, 3$).",
 'FE-35': r"Exact; every off-diagonal component vanishes and the $x_0$ component equals the $x_5$, $x_6$, $x_7$ components.",
 'FE-39': r"Exact; solved together with the $x_0$ component for the two rates and integrated numerically (LSODA) from the "
          r"primordial block to the static block.",
 'FE-40': r"Exact. The $x_0$ component and the extra-time components $x_5$, $x_6$, $x_7$ have the same left side ($\mathcal{E}_{(p)}{}^{x_0}{}_{x_0} = \mathcal{E}_{(p)}{}^{x_5}{}_{x_5}$), so the order-0 metric solves both only if $p_0 = p_5$; for $p_0 \ne p_5$ the common block scale $f$ obeys their average with $\bar p$ (the variation of the action with respect to $f$), and $p_0 - p_5$ drives a block-shape mode outside the order-0 metric (OPEN).",
 'FE-41': r"Exact consequence of FE-11; for the stabiliser it gives $\rho_{\mathrm{stab}} \propto f^{-8}$.",
 'FE-42': r"Exact for $\mathcal{H}_f = 0$ and $\dot{\mathcal{H}} = 0$; the $x_0$ and extra-time components agree for a block-isotropic source ($p_0 = p_5 = \bar p$); without sources and with $\mathcal{H} = 0$ the only static block is $K = 1/(4w_{(2)}) = 8$, which needs $\Lambda = -24H^2$ and has $\mathcal{G} = -1$ (repulsive gravity).",
 'FE-43': r"Exact (closed form); the stabiliser is block-isotropic ($p_0 = p_5 = \rho_{\mathrm{stab}}$, so the $x_0$ and the extra-time equations coincide); the upper root is the vacuum of UM-2 with attractive four-dimensional gravity; the lower root $K_- = 2.4781$ has $\mathcal{G} = -0.4748$.",
 'FE-44': r"Exact; eigenvalues 0 and $\pm\mathrm{i}\omega_{\mathrm{r}}$: the block is stable and oscillates (the radion, mass "
          r"48.42 TeV); stable for every stabiliser law of the family tried.",
 'FE-45': r"Exact to first order ($\mathcal{H}^2$ counted as first order); the coefficients are FE-46.",
 'FE-46': r"Exact (sympy); numerically $0.272956\,H^2$, $0.266522\,H^2$, $-0.006853$, $0.038221$, $-0.045997$, $0.028666$, "
          r"$0.037320$, $-0.009555$.",
 'FE-47': r"Exact for a slowly varying source (second time derivative of $\Delta K$ neglected); radiation drops out exactly; "
          r"used in every environment of the coupled solution FE-80.",
 'FE-48': r"Exact (the four-dimensional quadratic density is topological, the cubic one vanishes); $\Lambda_4 = 0$ at the static "
          r"point; the observed dark energy is a tuned residual, $\Lambda_4/H^2 \sim 10^{-92}$ (OPEN).",
 'FE-50': r"Exact reduction on the static block (in the gauge where the $y$ component of the gauge field vanishes; the same "
          r"operator for the transverse-traceless graviton in Einstein gravity); solved exactly by FE-52 (mpmath) and checked with "
          r"finite elements to $5\times10^{-10}$.",
 'FE-51': r"The tip condition is the natural boundary condition of the tip mass term (IN-15); one value for $W^+$ and $W^-$ "
          r"(particle and antiparticle); $\beta_{\mathrm{W}}$ is fitted to the measured masses (FE-55).",
 'FE-52': r"Exact; graviton, photon and gluons are exactly massless; the first even Kaluza-Klein level $\tilde m_1^2 = 30.1196$ ($\tilde m_1 = 5.48813$), "
          r"the first odd level $\tilde m^2 = 27.0890$, the gap $\tilde m^2 = 9H^2L^2/4 = 20.25$ ($HL = 3$); $\tilde m_{\mathrm{W}}^2 = 1.32149\times10^{-5}$, "
          r"$\tilde m_{\mathrm{Z}}^2 = 1.70150\times10^{-5}$ (mpmath; finite elements $3\times10^{-14}$).",
 'FE-53': r"Exact; $\tilde m_n^2 = 30.1196$, 59.7284, 109.0764 for $n = 1, 2, 3$ (finite elements agree to $3.9\times10^{-9}$); "
          r"$m^{\mathrm{KK}}_1 = m_{\mathrm{KK}} = 121.32$ TeV.",
 'FE-55': r"Fit (DERIVED): $\beta_{\mathrm{W}} = 0.011912$ reproduces $\rho_{\mathrm{EW},0} - 1 = 0.00038$ and both measured "
          r"masses; $m_{\mathrm{KK}} = 121.32$ TeV, $H = 14.296$ TeV.",
 'FE-56': r"Exact (all eight blocks, general $a_4(x_4)$, $b_4(x_4)$, $M(y)$, $v(y)$; checked with the author's matrices); the "
          r"basis of the reduction for every fermion of UM-2.",
 'FE-57': r"Exact: the zero modes are massless four-dimensional particles with the energy $\mathrm{e}^{-a_4}\lvert k\rvert$; "
          r"localised at the fold for $c_L > 0$ and $c_R < 0$.",
 'FE-58': r"Exact solutions (block $\varsigma = +1$) that satisfy the fold conditions $b(0) = 0$ (doublet, $c_L > 0$) and "
          r"$a(0) = 0$ (singlet, $c_R < 0$).",
 'FE-59': r"Exact roots (shooting agrees to $6\times10^{-10}$); the first-order formula agrees to $1.1\times10^{-3}$ (top quark) "
          r"and better than $3\times10^{-4}$ otherwise.",
 'FE-62': r"Exact; at the stabilised block $c_\Psi = 0.646667$, the lowest odd level (the dark matter) is "
          r"$\varepsilon = 3.102204\,m_\Psi = 44.35$ TeV ($\varpi = 1.89901$) and the lowest even bulk level $4.959981\,m_\Psi$.",
 'FE-65': r"Exact definitions (the factor $\frac12$ is the weight of each fold parity); $k_{\mathrm{lat}} = 0.25\,H$ in the "
          r"computations.",
 'FE-67': r"Evaluated for every state; its block averages enter the block response FE-47 (dark matter at rest: $p_3 = 0$ and "
          r"$p_0/\rho = 0.772034343 = -\mathrm{d}\ln\varepsilon_{\mathrm{DM}}/\mathrm{d}\ln f$).",
 'FE-69': r"The block form of FE-28 ($\gamma^{x_0} = \sigma_3$ in every block); self-adjoint.",
 'FE-70': r"The overlaps are computed with the Kohn-Sham orbitals ($\tilde I_Q = 8.2722$, $\tilde I_\ell = 1.2524$ for the dark "
          r"matter) and equal the derivatives of self-consistent levels with respect to the mean-field amplitudes to "
          r"$3\times10^{-10}$ (Hellmann-Feynman); I13 vanishes on the fold bands (to $7\times10^{-14}$).",
 'FE-71': r"$\mathcal{O}_{\mathrm{DM}} = 0.7072$ (Hellmann-Feynman, checked to $10^{-8}$); the field strengths are in the "
          r"geometric normalisation of the action (flat zero modes), and $G_{\mathrm{g}}$, $G_{\mathrm{W}}$, $G_{\mathrm{B}}$ are "
          r"the couplings to the canonically normalised fields (field divided by its four-dimensional coupling) used in the "
          r"cross-section FE-127; the benchmark strength is unitarity safe.",
 'FE-72': r"First order in the mean fields (Hellmann-Feynman; the response is screened by only $3.5\times10^{-4}$ in the "
          r"interacting state); universal I12 coefficients $c_{\mathrm{G}} = c_{\mathrm{W}} = c_{\mathrm{B}} = c_{\mathrm{I12}}$.",
 'FE-73': r"Evaluated in ten environments (unpolarised fermions, each chirality half of the density); at most "
          r"$8.2\times10^{-10}$ GeV (I13, at the freeze-out).",
 'FE-74': r"Geometric normalisation (the canonical field times $g_3$): the vacuum value is $4\pi^2$ times the standard condensate "
          r"$0.012$ GeV$^4$ of $(\alpha_3/\pi)$ times the squared canonical field strength (STANDARD); the relation does not "
          r"depend on the signature convention.",
 'FE-75': r"A lattice-like shape below 1 GeV (ESTIMATE) and leading-order perturbation theory above ($\alpha_3$ at the scale "
          r"$2\pi T$).",
 'FE-76': r"The first relation is the free part (on shell the Proca Lagrangian is a total derivative); the second "
          r"(Feynman-Hellmann) reproduces the trace-anomaly gluon condensate to $10^{-16}$; SU(2): $d_{\mathrm{adj}} = 3$, "
          r"$C_{\mathrm{adj}} = 2$, $T_{\mathrm{F}}N_{\mathrm{f}} = 3$; U(1)$_Y$: $d_{\mathrm{adj}} = 1$, $C_{\mathrm{adj}} = 0$, "
          r"$\frac52T_{\mathrm{F}}N_{\mathrm{f}} \to \frac{25}{2}$; no scalar term (ESTIMATE).",
 'FE-77': r"One loop from the $\overline{\mathrm{MS}}$ values at $m_{\mathrm{Z}}$; the couplings of the condensates are taken at "
          r"$\mu_{\mathrm{ren}} = 2\pi T$.",
 'FE-78': r"Below $m_{\mathrm{W}}$ the order-$\alpha_{\mathrm{G}}$ part is multiplied by the thermal suppression of a massive "
          r"vector (ESTIMATE); at the freeze-out the $W$ condensate is $-5.0\times10^{11}$ GeV$^4$, almost all from the "
          r"interaction part.",
 'FE-79': r"First-order perturbation theory with the exact $W$ eigenfunction (shooting and the stored value agree to "
          r"$3\times10^{-12}$): $\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}} = -0.111253$ (version 3 quoted $-0.1126$ "
          r"from finite elements) while the photon and gluon zero mode stays "
          r"massless; the physical shifts are at most $1.7\times10^{-16}$.",
 'FE-80': r"Iterated with the masses until self-consistency (the loop gain is at most $1.1\times10^{-33}$, so one step suffices); "
          r"the block moves by at most $\Delta\ln f = 1.1\times10^{-34}$ (at the freeze-out).",
 'FE-81': r"The response of the pressure to the block scale at fixed temperature ($\bar p = \frac14\,\mathrm{d}p/\mathrm{d}\ln f$); "
          r"the plasma species as ideal gases with their $x_0$ masses, nucleons and electrons as degenerate Fermi gases in the "
          r"cold environments.",
 'FE-82': r"The bulk couplings scale as $f^{-4}$ ($g_{\mathrm{G}}^2 = \hat g^2/V_\perp$) and $m_{\mathrm{KK}}$ as $1/f$; "
          r"leading-order trace anomaly.",
 'FE-83': r"One loop; $\alpha_3(m_{\mathrm{KK}}) = 0.0606$ and $\mathrm{d}\ln m_{\mathrm{p}}/\mathrm{d}\ln f = -46.1$: the most "
          r"block-sensitive mass of UM-2.",
 'FE-85': r"From $m = \tilde\varepsilon/(fL)$ with the first-order root of FE-59 and localisations $c \propto f$: $-18.82$, "
          r"$-18.01$, $-14.90$, $-12.15$, $-10.89$, $-6.77$ for the up, down, strange, charm, bottom and top quarks.",
 'FE-86': r"The hot environments (the cold ones use measured densities); the dark matter in equilibrium for both species while "
          r"$M_{\mathrm{DM}}/T < 40$, its relic density afterwards.",
 'FE-87': r"Order 0 exact; order 1, $n = 0$ by the linear Einstein-Boltzmann equations (FE-90 to FE-96; potentials "
          r"$2.4\times10^{-5}$ and smaller); $n \ge 1$ by the graviton tower FE-53 (range below $1.6\times10^{-21}$ m); order 2 "
          r"estimated ($5.8\times10^{-10}$).",
 'FE-88': r"The potentials, the tensor and the radion are of order $\epsilon$; the radion is massive (48.42 TeV) and its static "
          r"response is at most $1.1\times10^{-34}$; the tensor amplitude is an input (bounded: tensor-to-scalar ratio below 0.036).",
 'FE-89': r"Newtonian gauge (Ma and Bertschinger); the prime denotes $\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$ and $a_4'$ is the "
          r"conformal expansion rate.",
 'FE-90': r"Solved numerically with CAMB 2.0.5 (default accuracy, lensing) at the Planck 2018 parameters, summed over the species "
          r"of UM-2; TT and EE agree with Planck $\Lambda$CDM to $2.5\times10^{-4}$ and $2.7\times10^{-4}$.",
 'FE-91': r"Solved with CAMB; the dark matter is cold (pressure zero for quanta at rest, Kohn-Sham).",
 'FE-94': r"Solved with CAMB (the $l = 2$ equation equals the separate quadrupole equation of Ma and Bertschinger).",
 'FE-96': r"Solved with CAMB, each mass state separately with the degeneracy $N_{\mathrm{eff}}/3 = 1.0144$ (masses iterated to "
          r"$7.8\times10^{-12}$); the fold bands produced by freeze-in obey the massless limit $E^{\mathrm{c}}_i = k_\nu$.",
 'FE-97': r"Inputs: the Planck 2018 primordial parameters; $N_{\mathrm{eff}} = 3.0432$ (neutrinos) + 0.0010 (freeze-in fold "
          r"bands) = 3.0442; $\mathcal{H}_0 = 67.38$ km/s/Mpc, sound horizon at the drag epoch 147.10 Mpc, BAO $\chi_{\mathrm{fit}}^2 = 31.5$ "
          r"for 13 DESI DR2 points.",
 'FE-98': r"From the CAMB solution: $\Phi_{\mathrm{rms}} = 2.42\times10^{-5}$ at $k = 10^{-4}$ Mpc$^{-1}$ down to "
          r"$5.03\times10^{-8}$ at 1 Mpc$^{-1}$; the Poisson form agrees to $1.5\times10^{-6}$ for $k \ge 0.01$ Mpc$^{-1}$ and the "
          r"large-scale form to $4.4\times10^{-5}$ ($D_+\mathrm{e}^{-a_4} = 0.7878$ today); inside the integral $\mathcal{H}$ is "
          r"evaluated at $a_4 = \tilde a_4$.",
 'FE-99': r"Computed from the CAMB linear matter power spectrum: $\sigma_8 = 0.8118$ for UM-2 against 0.8109 for $\Lambda$CDM.",
 'FE-100': r"$m_1$ and the normal ordering ASSUMED, the splittings STANDARD (NuFIT 6.0); they are $x_0$ eigenvalues of FE-59 "
           r"with $c_R = -35.0452$, $-32.8481$, $-31.0702$.",
 'FE-101': r"The exchange of $W^+$, $W^-$ and $Z$ between zero modes far below $m_{\mathrm{W}}$, $m_{\mathrm{Z}}$; summed over the "
           r"flavours $\alpha$, $\beta$ and the fermions $f$ of the medium.",
 'FE-102': r"UM-2 uses the measured $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$.",
 'FE-103': r"For an unpolarised medium at rest; in neutral matter of electrons, protons and neutrons; antineutrinos have $-V$.",
 'FE-104': r"Solved exactly (matrix exponential for constant density, ordered products of layers otherwise); vacuum formula "
           r"reproduced to $3.9\times10^{-15}$, unitarity $1.8\times10^{-15}$; antineutrinos: $U \to U^*$, $V \to -V$.",
 'FE-105': r"Checked against the exact evolution (CPT to $2.8\times10^{-16}$, T-odd difference to $5.9\times10^{-14}$).",
 'FE-106': r"The 1-3 resonance at 11.135 GeV in rock of 2.8 g/cm$^3$ (exact three-flavour 11.133 GeV); the 1-2 resonance at "
           r"the centre of the Sun at 1.93 MeV.",
 'FE-107': r"Evaluated at the production point; the numerical three-flavour evolution through the solar density agrees to "
           r"$1.3\times10^{-3}$.",
 'FE-108': r"Two-flavour conditions; in the supernova envelope both resonances are adiabatic "
           r"($\mathcal{P}_{\mathrm{LZ}} \le 2.6\times10^{-77}$).",
 'FE-109': r"Leading order in $T/m_{\mathrm{W}}$; it falls below the vacuum term at $T = 4.99$ MeV (atmospheric) and 2.39 MeV "
           r"(solar) for $\lvert\vec k\rvert = 3.15\,T$.",
 'FE-111': r"Integrated from 20 MeV to 5 keV (LSODA, relative tolerance $10^{-11}$); the method reproduces the published values "
           r"(Escudero 2020) to $10^{-3}$; $\nu_\tau$ follows $\nu_\mu$.",
 'FE-112': r"$f_{\mathrm{a}} = 0.884$, $f_{\mathrm{s}} = 0.829$; the radiatively corrected couplings "
           r"$\tilde g^{\nu_e e}_L = 0.727$, $\tilde g^{\nu_e e}_R = 0.233$, $\tilde g^{\nu_\mu e}_L = -0.273$, "
           r"$\tilde g^{\nu_\mu e}_R = 0.233$ are used (the tree-level ones change $N_{\mathrm{eff}}$ by $4\times10^{-4}$).",
 'FE-113': r"Massless limits $-5e^2T^4/288$ and $e^3T^4/(36\sqrt3\,\pi)$ reproduced to $10^{-16}$ (Bennett et al. 2020).",
 'FE-114': r"Gauss-Legendre panels; the logarithmic singularity at $k_2 = k$ removed by a substitution.",
 'FE-115': r"UM-2 computes 3.0476 (separate temperatures) and 3.0485 (one common temperature, efficient oscillations) and adopts "
           r"the precision value 3.0432 (Cielo et al. 2023); for instantaneous decoupling the plasma entropy per comoving volume "
           r"is conserved and $T_\nu$ falls as $\mathrm{e}^{-a_4}$.",
 'FE-116': r"Homogeneous, axially symmetric gas of electron neutrinos and antineutrinos (symmetry axis $x_3$).",
 'FE-117': r"Roots found for real $k_{\mathrm{f}}$ on a grid by vectorised Newton iterations; three independent evaluations "
           r"agree to $1.2\times10^{-14}$.",
 'FE-118': r"A root with $\mathrm{Im}\,\bar\omega > 0$ for real $\bar k$ is an instability; with a crossing of the "
           r"electron-lepton-number distribution the largest growth rate is $0.088\sqrt2\,G_{\mathrm{F}}n_{\nu_e}$, without one "
           r"no mode grows (Morinaga 2022).",
 'FE-119': r"Eigenvalues of the discretised homogeneous equation (300 nodes) agree with the dispersion relation; growth by a "
           r"factor $\mathrm{e}$ in $6\times10^{-10}$ to $6\times10^{-11}$ s near the neutrinosphere (scale "
           r"$\sqrt2\,G_{\mathrm{F}}n_{\nu_e}$).",
 'FE-120': r"Exact integrals: $T_\nu = 1.9454$ K, 112.0 per cm$^3$ per mass state, mean velocities 0.435, 0.0604, 0.0105 today, "
           r"$\Omega_\nu h_{100}^2 = 6.382\times10^{-4}$.",
 'FE-121': r"Exact integrals with the $x_0$ masses (upper sign for fermions); no Higgs particle; right-handed neutrinos, fold "
           r"bands, radion and Kaluza-Klein modes not in equilibrium.",
 'FE-122': r"Checked against the exact limits 105.75, 86.25, 10.75 and 43/11.",
 'FE-123': r"$T_{\mathrm{c}} = 155$ MeV, $T_{\mathrm{w}} = 15$ MeV with a gas of the twelve lightest hadron multiplets below "
           r"(ASSUMED model of the crossover); neutrinos decoupled instantaneously at 2 MeV.",
 'FE-124': r"Integrated implicitly (Radau, $\ln Y_{\mathrm{DM}}$ from $x = 5$ to 2000, relative tolerance $10^{-10}$) with the "
           r"degrees of freedom of UM-2; the late-time integral holds to $1.3\times10^{-8}$; each of the two species freezes out "
           r"separately.",
 'FE-126': r"Each species gives 0.060 (0.120 together) for $G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$ (freeze-out at "
           r"$x = 31.23$).",
 'FE-127': r"Spin averaged; I12 p-wave (from $^3P_0$ only, polarisation sum and spin trace checked numerically), I13 s-wave "
           r"(from $^3S_1$), summed over the quark multiplets ($o$ the dark-matter orbital; the sum of "
           r"$N_{\mathrm{c}}(q^B_f\tilde I^{(b)}_{of})^2$ is 16.351); I12 at the unitarity-safe benchmark "
           r"$G_{\mathrm{I12}} = \pi/(2M_{\mathrm{DM}}^3)$.",
 'FE-128': r"Where an effective cross-section exceeds its bound it is replaced by the bound; I13 reaches it only above "
           r"$v_{\mathrm{rel}} = 0.51$ (22 % of the freeze-out rate); I12 alone would need a strongly coupled $^3P_0$ channel.",
 'FE-129': r"Maxwell-Boltzmann, massless ($o$ the fold band; the sum is 126.85 over the fifteen multiplets of three "
           r"generations); integrated from the highest temperature 10 TeV (ASSUMED): "
           r"$\Delta N_{\mathrm{eff}} = 5.21\times10^{29}\,G_{\mathrm{V}}^2$ GeV$^4$, so the benchmark "
           r"$G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$ gives 0.001.",
 'FE-130': r"The production rate per fold quantum is 0.012 of the Hubble rate at the highest temperature 10 TeV: never in "
           r"equilibrium.",
 'FE-131': r"The counterfactual that motivates the baryon current: the three $\nu_R$ would reach 0.9997 of equilibrium by "
           r"$x = 40$ and add $\Delta N_{\mathrm{eff}} = 0.144$ (the factor 2 counts the two dark-matter species).",
 'FE-132': r"For a Weyl $\nu_R$ on a heavy Dirac fermion (two species); kinetic decoupling at $x = 24.4$.",
 'FE-133': r"$T_\nu/T_\gamma = 0.71664$ and $h_\nu = 0.00165$ from the common-temperature decoupling of FE-115; used for the "
           r"$B - L$ variant (0.144) and the self-interaction channel.",
 'FE-134': r"Evaluated: $r_{\nu_R} = 2.0\times10^{-17}$, so the right-handed neutrinos are never thermalised.",
 'FE-135': r"$\tilde I_\lambda = 14.38$ (DERIVED); the cross-section is an ESTIMATE (Fierz coefficients not computed).",
 'FE-136': r"Integrated from the highest temperature to the freeze-out: "
           r"$\Delta N_{\mathrm{eff}} = 1.83\times10^{26}\,G_\lambda^2$ GeV$^4$, so $\Delta N_{\mathrm{eff}} \le 0.001$ requires "
           r"$G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$ (ASSUMED bound on $\lambda$); otherwise the fold bands decouple as four "
           r"Weyl species (FE-133).",
}
