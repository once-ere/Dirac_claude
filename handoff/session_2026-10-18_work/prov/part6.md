# The computations and their verification (DERIVED)

All computations are Python scripts in the folder `universe_model_2/code`; each writes its numbers to
`universe_model_2/outputs` and a report of named checks (name, verdict, detail) to `universe_model_2/reports`, and exits with
code 0 only if every check passes. Two modules are shared: `um2_common.py` (the output folders, the report class, reading and
writing the JSON files) and `um2_constants.py` (the measured inputs of section 7). In total 287 checks in version 4: the
235 of version 3 (233 before the fixes of its independent review, item 24; 205 in version 2; 179 to 182 in version 1) and the
52 of the new residual analysis; none failed. In the table the prefix `um2_` of every script name is omitted.

| script | what it computes | method | output | checks |
|:----------------|:-----------------------------------------|:-------------------------|:--------------------|:------|
| algebra.py | the author's gamma matrices rebuilt from the notebook formulas; $C$, $\Gamma_8$, $\mathcal{B}$; the irreducibility of the representation of Pin(4,4); the two inequivalent halves of Spin(4,4); the $2\times2$ block basis and the block forms of every matrix the reductions use | sympy, exact | algebra.json | 31 |
| geometry.py | the Riemann tensor of the order-0 metric in two charts; the Lovelock tensors by four routes (pairing formula, Ricci tensor, explicit Gauss-Bonnet tensor, minisuperspace variation with a lapse); the Bianchi identities; the record's equations; the static block; the canonical spin connection | sympy, exact | geometry.json | 25 |
| background.py | the background equations in class form; the static block; the stabiliser and its family; the radion; the linear response of the block to matter sources; the dimensional reduction | sympy, exact; eigenvalues numerically | background.json | 22 |
| fields.py | the exact $x_0$ reduction of the eight-dimensional Dirac equation (all blocks, general $a_4$, $b_4$, $M$, $v$); boundary conditions; zero modes; tip mixing for one and three generations (self-adjoint with an arbitrary complex $3\times3$ matrix); the gauge $x_0$ operator; gauge invariance of the tip terms of three generations | sympy and numpy | fields.json | 16 |
| spectra.py | the $x_0$ spectra of the gauge bosons and the graviton; the $W^\pm$, $Z$ fit to $\rho_{\mathrm{EW},0}$ with the angle of the couplings fixed by the measured masses (both masses reproduced); the twelve fermion masses as exact $x_0$ eigenvalues | mpmath root finding; quadratic finite elements with Richardson; shooting | masses.json | 14 |
| flavour.py | the PMNS and CKM matrices; the exact tip determinant of three generations and its null vectors; a general complex tip matrix; the flavour-changing couplings of the Kaluza-Klein gauge modes; $\mu \to e\gamma$; lepton universality | mpmath (50 digits), numpy | flavour.json | 7 |
| neutrino.py | vacuum and matter oscillations, the MSW resonances, long-baseline appearance, the Sun, the onset of oscillations in the early Universe, neutrino decoupling and $N_{\mathrm{eff}}$, the CNB, supernova resonances, the fast flavour instability, the heating behind the shock; (version 3) the Majorana alternative | exact matrix exponentials and layer products; LSODA; Gauss-Legendre panels; Newton iterations; adaptive quadrature | neutrino.json | 16 |
| kohnsham.py, ks_jobs.py | Kohn-Sham (the solver library and its seven jobs): validation against the record (2 checks), free spectrum (3), interacting ground states of 8 (3) and of 592 particles (4), dark-matter quanta (3), portal responses with the three-generation sources (5), block feedback with the full adiabatic response (2) | Galerkin in the free basis, safeguarded Anderson self-consistency, Richardson in the basis size; single-threaded linear algebra (version 4) | ks/*.json (seven files) | 22 |
| electroweak.py | charges ($W^+$: $+e$, $W^-$: $-e$), anomalies of three generations, couplings, the chirality projector, $\Gamma_4 = -\mathcal{B}\gamma^{x_0}$, the chiral tip charges of $\Psi_A$ and $\Psi_B$, the number of light neutrinos, the removal of the tip $Z$ portal, the $Z$ widths of three generations and their scheme dependence | sympy and numerics | electroweak.json | 19 |
| primordial.py | the nonlinear primordial evolution, the basin, the separatrix, the radion oscillation | DOP853, bisection | primordial.json | 5 |
| cosmology.py | TT and EE spectra with three massive neutrinos, the BAO $\chi_{\mathrm{BAO}}^2$, $N_{\mathrm{eff}}$, helium, the variants with a thermalised fold band; (version 3) the model with the freeze-in fold bands, $\sigma_8$, the growth rate, the potential spectrum | CAMB 2.0.5 | cosmology.json | 8 |
| analysis.py | the $x_0$ decompositions and the uncertainty relation on the cell; the gap theorem; sum rules; the twelve fermions against the uncertainty estimate; the conservation of the halves; the relic of two species with I12 alone; direct detection; the condensate; the vacuum energy; the sensitivities to the block size; the block rate today; the radion decay | mpmath, numpy, sympy | analysis.json | 23 |
| thermal.py | (version 3) the degrees of freedom with the $x_0$ masses; the relativistic thermal average; the Boltzmann solver and its validation; the relic of I12 alone; partial-wave unitarity; the unitarity-safe I12 benchmark | Gauss-Legendre ideal-gas integrals; adaptive quadrature with scaled Bessel functions; implicit Radau; Brent root finding | thermal.json | 7 |
| coupled.py | (version 3) the portal overlaps with every zero mode and their Kohn-Sham checks; the screened response; the fold band under the portals; the freeze-in of the fold bands; direct detection; I13 (the algebra of its bilinear, fold-band blindness, relic with the unitarity cap, detection, annihilation today); the $B - L$ alternative; the self-interaction channel; the mean fields in ten environments; the full adiabatic block response to every species; the proton sensitivity; the $W$ eigenvalue with the kinetic function; the domain of validity | exact sympy matrices; self-consistent Kohn-Sham solutions with Richardson in the amplitude; Boltzmann equations; first-order perturbation theory (version 4) | coupled.json | 16 |
| series.py | (version 3) the magnitudes of the terms of the metric series: potentials, Kaluza-Klein gravitons (levels, norms, Yukawa strengths, orthogonality), the radion, order 2, the tensor bound | analytic eigenfunctions, finite elements, quadrature | series.json | 4 |
| residuals.py | (version 4) the residuals of the stored solution in 26 field equations (afresh by substitution where cheap), the sizes of the neglected terms, and 26 links in concert (section 10) | substitution (sympy, mpmath at 40 digits), independent quadratures and re-integrations | residuals.json | 52 |

## The catalogue of the 287 checks

The checks are listed by report, numbered in the order of the report; the names are those of the reports, spelled as in
the code. The field-equation table of section 8 refers to them by the abbreviation of the report and the number.

```{=latex}
\begingroup\raggedright
```

@@CATALOGUE@@

```{=latex}
\par\endgroup
```

## The principal numbers and where they come from

| quantity | value | script (output) |
|:------------------|:-----------------------------------------------|:--------------------------|
| static block | $K_* = 12 + \frac43\sqrt{51} = 21.5219$, $f_* = 0.215556$, $\mathcal{G}(K_*) = \frac{20}{3} + \sqrt{51} = 13.8081$, $\kappa\rho_{\mathrm{stab}}(f_*) = (26 + 4\sqrt{51})H^2$ | background (background.json) |
| radion | $\omega_{\mathrm{r}}^2/H^2 = 31552/2249 - 2416\sqrt{51}/6747 = 11.4721$, $\omega_{\mathrm{r}} = 3.387H = 48.42$ TeV | background, spectra (background.json, masses.json) |
| unbroken $x_0$ spectrum ($HL = 3$) | $\tilde m = 0$ (flat profile); first even level $\tilde m_1^2 = 30.1196$; first odd level $\tilde m^2 = 27.0890$; gap $9H^2L^2/4 = 20.25$ | spectra (masses.json) |
| $W^\pm$, $Z$ | $\beta_{\mathrm{W}} = 0.011912$, $\beta_{\mathrm{Z}} = 0.015343$ ($\cos^2\theta_{\mathrm{W}} = 0.776368$), $\tilde m_{\mathrm{W}}^2 = 1.32149\times10^{-5}$, $\tilde m_{\mathrm{Z}}^2 = 1.70150\times10^{-5}$, $\rho_{\mathrm{EW}} - 1 = 0.00038$, model $m_{\mathrm{Z}} = 91.1879$ GeV; Dirichlet bound of the tip $\tilde m^2 = 0.010016$ | spectra (masses.json) |
| scales | $m_{\mathrm{KK}} = 121.32$ TeV, $H = 14.296$ TeV, proper half cell $fL = 8.926\times10^{-21}$ m, $x_0$ period $7.227\times10^{-21}$ m, gap $3H/(2f) = 99.48$ TeV | spectra (masses.json) |
| fermion localisations ($\mathcal{K} = 1$) | doublets $c_L = 5.9529$ (leptons), $3.3823$ (quarks); singlets $c_R$: $\nu_1$ $-35.0452$, $\nu_2$ $-32.8481$, $\nu_3$ $-31.0702$, electron $-14.5539$, muon $-8.9809$, tau $-5.9529$, up $-15.4300$, charm $-8.7683$, top $-3.3823$, down $-14.6258$, strange $-11.5158$, bottom $-7.5005$ | spectra (masses.json) |
| three generations | the roots of the tip determinant equal the one-generation roots to $3.0\times10^{-42}$, the null vectors the columns of $\mathcal{K}$ to $1.1\times10^{-16}$; a general complex tip matrix: singular values to $3.5\times10^{-5}$ | flavour (flavour.json) |
| mixing | PMNS ($\theta_{12} = 33.71^\circ$, $\theta_{13} = 8.56^\circ$, $\theta_{23} = 43.28^\circ$, $\delta_{\mathrm{CP}} = 212^\circ$) unitary to $1.1\times10^{-16}$, $J_{\mathrm{CP}} = -0.01777$; CKM $J_{\mathrm{CP}} = 3.117\times10^{-5}$; Kaluza-Klein gauge overlaps $0.14434$ (leptons), $-0.30066$ (quarks), off-diagonal $1.0\times10^{-17}$; branching ratio of $\mu \to e\gamma$ $2.8\times10^{-55}$ | flavour (flavour.json) |
| neutrino masses | $m_1 = 1.000$, $m_2 = 8.712$, $m_3 = 50.140$ meV; $\sum_im_i = 0.0599$ eV | spectra, neutrino (masses.json, neutrino.json) |
| flavour conversion | 1-3 MSW resonance 11.135 GeV (exact 11.133 GeV) at 2.8 g/cm$^3$; solar 1-2 resonance 1.93 MeV; $\mathcal{P}(\nu_\mu\to\nu_e)$: T2K 0.0517, NOvA 0.0481, DUNE 0.0701 (antineutrinos 0.0313, 0.0236, 0.0195); solar $\mathcal{P}_{ee}$ from 0.5408 (pp) to 0.3043 ($^8$B, 15 MeV) | neutrino (neutrino.json) |
| early Universe | oscillation onset $T = 4.99$ MeV (atmospheric), 2.39 MeV (solar); $N_{\mathrm{eff}} = 3.0476$ (separate temperatures), 3.0485 (common); adopted 3.0432 | neutrino (neutrino.json) |
| CNB | $T_\nu = 1.9454$ K, 112.0 cm$^{-3}$ per mass state, $\bar v_i = 0.435133$, $0.0604083$, $0.0105352$; $\Omega_\nu h_{100}^2 = 6.38217\times10^{-4}$ (version 4: quadrature to $3\times10^{-16}$) | neutrino (neutrino.json, copied in cosmology.json) |
| supernovae | H resonance (20 MeV) at 1573 g/cm$^3$, adiabaticity $\gamma_{\mathrm{ad}} = 178$; $\mathcal{P}_{ee} = 0.02215$, antineutrinos 0.677; fast instability growth 0.0877 and 0.0979 in units of $\sqrt2G_{\mathrm{F}}n_{\nu_e}$, e-folding in $5.9\times10^{-10}$ to $5.9\times10^{-11}$ s; heating factors 0.884, 0.760 | neutrino (neutrino.json) |
| dirac16complex at $f_*$ | $c_\Psi = 0.646667$; $\varepsilon_{\mathrm{DM}} = 3.102204\,m_\Psi$ ($\varpi = 1.89901$, an $x_0$ wave number of $2.93661\,m_\Psi$); lowest even bulk level $4.959981\,m_\Psi$; $x_0$-momentum fraction 0.896 | ks_jobs spectrum (ks/spectrum.json) |
| dark matter | $M_{\mathrm{DM}} = 44.35$ TeV (both halves); $p_3/\rho = 0$; $p_0/\rho = 0.772034343 = -\mathrm{d}\ln\varepsilon_{\mathrm{DM}}/\mathrm{d}\ln f$ | ks_jobs darkmatter (ks/darkmatter.json) |
| portal responses | the dark-matter level per unit amplitude of the mean field: I11 electron density 0.824779, up-quark density 4.328803, neutrino density 1.252406; I12 gluon condensate 0.707196 ($= \mathcal{O}_{\mathrm{DM}}$); the fold-band gap changes by $7.9\times10^{-11}$, $3.0\times10^{-9}$, $-9.3\times10^{-11}$, $-1.4\times10^{-10}$ (zero in exact arithmetic; version 4) | ks_jobs portals (ks/portals.json) |
| tip $Z$ portal (removed) | $N_\nu = 3 + 2r_{\mathrm{Z}}^2$, $r_{\mathrm{Z}}^2 < 0.0056$; at the bound decoupling at 14.7 MeV and $\Delta N_{\mathrm{eff}} = 2.02$; oriented part $\Delta N_{\mathrm{eff}} = 0.0958$ to 0.1257 | electroweak (electroweak.json) |
| $Z$ widths | invisible 497.7 MeV (measured 499.1), total 2422.3 MeV at tree level, 2485.2 MeV with $1 + \alpha_3/\pi$ (measured 2495.5); hadronic ratio $R_\ell = 20.83$ (measured 20.77) | electroweak (electroweak.json) |
| primordial era | separatrix at $K = 2.6983$, 2.5991, 2.5301 (for the initial $\mathcal{H}_f = -H/2$, $-H/3$, $-H/10$); deflation factor up to 2.9166; radion frequency $3.3868H$ measured | primordial (primordial.json) |
| cosmology | UM-2 (version 3, $N_{\mathrm{eff}} = 3.0442$): $\mathcal{H}_0 = 67.38$ km/s/Mpc, $\Omega_{\mathrm{m}} = 0.3150$, $r_{\mathrm{d}} = 147.104$ Mpc, $\chi_{\mathrm{BAO}}^2 = 31.49$ (13 points; $\Lambda$CDM 32.55), TT and EE within $2.5\times10^{-4}$ and $2.7\times10^{-4}$ of $\Lambda$CDM; without the freeze-in fold bands ($N_{\mathrm{eff}} = 3.0432$): 67.37, 0.3151, 147.109 Mpc, 31.72, $2.8\times10^{-4}$ | cosmology (cosmology.json) |
| relic with I12 alone (version 2) | two species, $x_{\mathrm{f}} = 30.38$, $g_\rho = 105.75$, required $\langle\sigma v_{\mathrm{rel}}\rangle = 2.01\times10^{-25}$ cm$^3$/s per species, $G_{\mathrm{I12}} = (15.5\ \text{TeV})^{-3}$; the $^3P_0$ bound $\sqrt{\pi x_{\mathrm{f}}}/M_{\mathrm{DM}}^2 = 5.79\times10^{-26}$ cm$^3$/s exceeded 3.47 times ($v_{\mathrm{c}} = 0.263$, 79 % of the pairs above it): OPEN in version 2, resolved in version 3 by I13 | analysis (analysis.json) |
| direct detection (gluons only) | $\sigma_{\mathrm{SI}} = 6.3\times10^{-53}$ cm$^2$ against $2.4\times10^{-45}$ cm$^2$ | analysis (analysis.json) |
| dark energy | condensate tuned to $w_{\mathrm{de},0} = -1$: $w_{\mathrm{de},a} = -6$, energy zero at $z_{\mathrm{red}} = 0.260$; natural vacuum energy $5.5\times10^{64}$ times the observed one; $(\mathcal{H}_0/H)^2 = 1.0\times10^{-92}$ | analysis (analysis.json) |
| uncertainty relation | $m/m_{\mathrm{Heis}}$: first Kaluza-Klein level 7.49, first odd level 6.47, dark matter 2.29, $W^\pm$ $1.14\times10^{-3}$, $Z$ $1.29\times10^{-3}$, top quark $3.2\times10^{-3}$, electron $5.5\times10^{-9}$, $\nu_1$ $1.1\times10^{-17}$; $\langle k_\xi^2\rangle\Delta\xi^2$: photon zero mode 0.497, fold zero mode of $\Psi$ 0.097 ($\varrho_\xi(-1) = 0.489$); $\langle k_\xi^2\rangle^{1/2}\Delta\xi \ge (1 - \varrho_\xi(-1))/2$ for every tabulated state | analysis (analysis.json) |
| block sensitivities | logarithmic derivatives with respect to $\ln f$: Kaluza-Klein masses $-1$, $m_{\mathrm{W}}$ $-0.501$, fermions from $-6.8$ (top) to $-41.0$ ($\nu_1$), $m_{\mathrm{e}}$ $-20.5$, $M_{\mathrm{DM}}$ $-0.772$, $\alpha_{\mathrm{em}}$ and the gauge couplings $-4$, $G_{\mathrm{N}}$ $+2.05$; splittings $\Delta m_{21}^2$ $-77.5$, $\Delta m_{31}^2$ $-74.0$ | analysis (analysis.json) |
| block rate today (ESTIMATE) | $\lvert\mathcal{H}_f\rvert < 3.6\times10^{-8}\mathcal{H}_0$ (atomic clocks, change of $\alpha_{\mathrm{em}}$ below $10^{-17}$ per year), $< 7.1\times10^{-4}\mathcal{H}_0$ (lunar ranging, change of $G_{\mathrm{N}}$ below $10^{-13}$ per year) | analysis (analysis.json) |
| radion decay (ESTIMATE) | $\Gamma_{\mathrm{r}} = C_{\mathrm{r}}\,\omega_{\mathrm{r}}^3/(4\pi\bar M_{\mathrm{Pl}}^2)$, $T_{\mathrm{RH}} = (90/(\pi^2g_\rho))^{1/4}(\Gamma_{\mathrm{r}}\bar M_{\mathrm{Pl}})^{1/2}$ ($g_\rho = 10.75$): lifetime $0.43\,\text{s}/C_{\mathrm{r}}$, $T_{\mathrm{RH}} = 1.85\,C_{\mathrm{r}}^{1/2}$ MeV (below 4.7 MeV unless $C_{\mathrm{r}} > 6.5$) | analysis (analysis.json) |
| first-order block response | $\Xi_{f3} = 0.028666$, $\Xi_{fp} = 0.037320$, $\Xi_{f\rho} = -0.009555$; adiabatic $\Delta K = (0.035852\,\kappa\Delta\rho - 0.107556\,\kappa\Delta p_3 - 0.140028\,\kappa\Delta\bar p)/H^2$ (radiation drops out: $0.107556 = 3\times0.035852$); for the Kohn-Sham states $\Delta K/\kappa = 2.27\times10^{-6}$ (8 particles, $+\lambda_{\mathrm{test}}$), 0.0125 (592 particles, $+\lambda_{\mathrm{test}}$), 0 (free gas), in units $H = 1$ | background, ks_jobs feedback (background.json, ks/feedback.json) |
| thermal history (version 3) | $g_\rho = 105.75$ (5 TeV), 105.73 (1.42 TeV), 104.95 (200 GeV), 86.22 (10 GeV), 10.74 (3 MeV); today $g_s = 3.9091$, $g_\rho = 3.3626$, $s_0 = 2891.3$ cm$^{-3}$; the relativistic thermal average exceeds the non-relativistic one by about $3/x$ | thermal (thermal.json) |
| I12 relic and unitarity (version 3) | $G_{\mathrm{I12}} = (15.855\ \text{TeV})^{-3}$, $x_{\mathrm{f}} = 31.70$, $\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}}) = 1.891\times10^{-25}$ cm$^3$/s; crossing of the $^3P_0$ bound at $E_{\mathrm{cm}} = 89510$ GeV, $v_{\mathrm{rel}} = 2\beta_{\mathrm{cm}} = 0.269$ (0.274 from the non-relativistic formula), 96 % of the rate and 75 % of the pairs above it; at the $^3P_0$ limit 0.0582 per species ($x_{\mathrm{f}} = 30.77$, $\langle\sigma v_{\mathrm{rel}}\rangle = 5.33\times10^{-26}$ against $\sqrt{\pi x}/M_{\mathrm{DM}}^2 = 5.84\times10^{-26}$ cm$^3$/s); benchmark fraction above its crossing $5.2\times10^{-4}$; capped: 0.1544, 0.1081, 0.0836, 0.0649, 0.0585; the benchmark $(38.2\ \text{TeV})^{-3}$ alone 8.0; $c_{\mathrm{I12}}/\Lambda_\star^3 = 1.106\times10^{-14}$ GeV$^{-3}$ | thermal (thermal.json) |
| I13 relic (version 3) | $\mathcal{S}_B = 16.351$; $G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$ (capped; $1.269\times10^{-9}$ without the cap); $x_{\mathrm{f}} = 31.23$; $\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}})$: I13 $9.50\times10^{-26}$, I12 $9.9\times10^{-28}$ cm$^3$/s; bound reached above $v_{\mathrm{rel}} = 0.51$ (22 % of the rate; the uncapped cross-section crosses it above 0.52, 25 %); $B - L$ alternative: $G_{\mathrm{A}}^{B-L} = 1.072\times10^{-9}$ GeV$^{-2}$, $\nu_R$ at 0.999698 of equilibrium at $x = 40$, kinetic decoupling at $x = 24.4$, $\Delta N_{\mathrm{eff}} = 0.144$; with $J^B$ the $\nu_R$ production through I11 is $r_{\nu_R} = 2.0\times10^{-17}$ | coupled (coupled.json) |
| self-interaction channel (version 3) | $\tilde I_\lambda = 14.38$; $\Delta N_{\mathrm{eff}} = 1.83\times10^{26}\,G_\lambda^2$ GeV$^4$; bound $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$ ($1.8\times10^{-6}G_{\mathrm{A}}$); $\lambda_{\mathrm{test}}$ with $v_{\mathrm{t}} = H^{-3}$: $G_\lambda = 1.14\times10^{-9}$ GeV$^{-2}$, fold bands thermalised to 2.6 TeV, $\Delta N_{\mathrm{eff}} = 0.19$ | coupled (coupled.json) |
| freeze-in and detection (version 3) | $\sum_fN_{\mathrm{c}}(q_f\tilde I_{of})^2 = 126.85$; $\Delta N_{\mathrm{eff}} = 5.21\times10^{29}G_{\mathrm{V}}^2$ GeV$^4$; $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$; production rate per fold quantum 0.012 of $\mathcal{H}$ at 10 TeV; xenon $\sigma_{\mathrm{SI}} = 4.01\times10^{-46}$ cm$^2$ (0.16 of LZ); $\langle\sigma v_{\mathrm{rel}}\rangle$ today $9.76\times10^{-26}$ cm$^3$/s | coupled (coupled.json) |
| coupled solution (version 3) | overlaps $\tilde I_Q = 8.2722$, $\tilde I^{(b)}_Q = 2.6135$ (dark matter); Kohn-Sham checks $3.1\times10^{-10}$, $2.3\times10^{-10}$; the I13 algebra exact; $\Delta\varepsilon_{\mathrm{DM}}/M_{\mathrm{DM}} \le 1.5\times10^{-6}$ (at the freeze-out, $T = 1.42$ TeV; thermal condensates $-8.1\times10^{12}$, $-5.0\times10^{11}$, $-2.6\times10^{10}$ GeV$^4$; Feynman-Hellmann against the trace anomaly $10^{-16}$); $\Delta\ln f \le 1.1\times10^{-34}$ (the hot plasma at the freeze-out; $7\times10^{-39}$ in the electroweak era, $9\times10^{-49}$ from nucleosynthesis on); loop gain $\le 1.1\times10^{-33}$; $\mathrm{d}\ln m_{\mathrm{p}}/\mathrm{d}\ln f = -46.1$; $A_{\mathrm{mf}} = 1.7\times10^{-16}$ at the freeze-out; $\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}} = -0.111253$ (version 4; version 3: $-0.1126$); validity up to $T = 27.4$ TeV | coupled (coupled.json) |
| metric series and $\sigma_8$ (version 3) | $\Phi_{\mathrm{rms}} = 2.42\times10^{-5}$ ($k = 10^{-4}$ Mpc$^{-1}$) to $5.03\times10^{-8}$ (1 Mpc$^{-1}$); order 2: $5.8\times10^{-10}$; $D_+\mathrm{e}^{-a_4} = 0.7878$ today; graviton levels $\tilde m_n^2 = 30.1196$, 59.7284, 109.0764; Yukawa strengths $\mathcal{A}_n = 0.0728$, 0.1469, 0.1809 (two masses at the fold); range $1.63\times10^{-21}$ m; radion $\le 1.1\times10^{-34}$; $\sigma_8 = 0.8118$ (UM-2), 0.8119 (without the freeze-in fold bands), 0.8109 ($\Lambda$CDM) | series, cosmology (series.json, cosmology.json) |
| Majorana alternative (version 3) | $\mathcal{K}_{\mathrm{M}}^{(i)} = 5.63\times10^{-13}$, $4.90\times10^{-12}$, $2.82\times10^{-11}$; $m_{\beta\beta}$ from 0.84 to 4.41 meV | neutrino (neutrino.json) |
| residuals (version 4) | 26 field equations: residuals from $7.4\times10^{-14}$ to $2.4\times10^{-5}$, each within its tolerance; 26 links: five not zero (section 10) | residuals (residuals.json) |

## Methods

* **Exact checks.** Symbolic identities are verified with sympy by simplifying the difference to zero; matrix identities
  entry by entry, with the author's matrices.
* **Roots.** The transcendental eigenvalue conditions (FE-52, FE-59, FE-60, FE-62) are solved with mpmath at 30 to 60
  digits; the residual analysis measures each stored root by its implied relative error, the value of the condition divided
  by the eigenvalue times the derivative of the condition.
* **Richardson extrapolation.** A number computed with the discretisation size $\mathsf{n}$, $2\mathsf{n}$ and $4\mathsf{n}$ is
  extrapolated and its observed order measured by

$$
\mathsf{X}_\infty \simeq \mathsf{X}_{2\mathsf{n}} + \frac{\mathsf{X}_{2\mathsf{n}} - \mathsf{X}_{\mathsf{n}}}{\mathrm{e}^{p_{\mathrm{obs}}\ln2} - 1},
\qquad p_{\mathrm{obs}} = \frac{1}{\ln2}\,\ln\frac{\mathsf{X}_{\mathsf{n}} - \mathsf{X}_{2\mathsf{n}}}{\mathsf{X}_{2\mathsf{n}} - \mathsf{X}_{4\mathsf{n}}}
$$

<!-- symbols: prov_RichX, prov_Richn, euler, prov_pobs -->

* **Finite elements.** As a cross-check of the boson eigenvalues, quadratic finite elements on 100, 200 and 400 elements
  solve the weak form of FE-50 with the tip condition of FE-51; the eigenvalue is the Rayleigh quotient of the gradient
  form,

$$
\int_{-1}^{0}\mathrm{e}^{3HL\xi}\Big(\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)^2\mathrm{d}\xi + \beta\,\mathrm{e}^{-3HL}F(-1)^2
 = \tilde m^2\int_{-1}^{0}\mathrm{e}^{3HL\xi}F^2\,\mathrm{d}\xi
$$

<!-- symbols: diff, euler, Hconst, Lcut, xi, Fprof, betaRobin, mtilde -->

  extrapolated by Richardson (observed order 4.01; $\tilde m_{\mathrm{W}}^2$ reproduced to $3.1\times10^{-14}$).
* **Kohn-Sham.** The orbitals of FE-63 are expanded in the exact eigenfunctions of the free problem of each sector (60, 120 or
  240 functions, quadrature with ten points per function); the mean fields FE-64 are iterated to self-consistency (tolerance
  $10^{-13}$) with a safeguarded Anderson mixing and a fixed labelling of the occupied set. Checks: the energy identity and
  the $y$-conservation law FE-68, Richardson in the basis size, the Hellmann-Feynman theorem for every portal mean field
  (the response of a level to a mean-field amplitude equals the expectation value of the perturbation), and the reproduction
  of the record's two reference states. Since version 4 the linear algebra runs single-threaded, so that the results do not
  depend on the number of cores (section 10).
* **Background and primordial era.** The 3-space and hidden components FE-39, FE-40 are solved for the two rates
  $\dot{\mathcal{H}}$ and $\dot{\mathcal{H}}_f$, with $\dot K = -2K\mathcal{H}_f$ and the stabiliser (plus radiation where
  stated); the constraint FE-38 fixes the initial $\mathcal{H}$ and is monitored (residual below $6\times10^{-10}$); DOP853
  integration, the separatrix by bisection in the initial $K$.
* **Neutrinos.** The flavour evolution FE-104 by exact matrix exponentials (constant density) and ordered products of 20000 and
  40000 layers (the Sun); the decoupling equations FE-111 to FE-114 with LSODA from 20 MeV to 5 keV (relative tolerance
  $10^{-11}$), validated against the published values of the method; the dispersion relation FE-117 by vectorised Newton
  iterations from a grid of complex starting points, checked against the analytic growth of FE-119 and the eigenvalues of
  the discretised homogeneous equation (300 nodes); the CNB FE-120 by adaptive quadrature.
* **Cosmology.** CAMB 2.0.5 solves FE-89 to FE-99 with the Planck 2018 parameters, the acoustic angle fixed (so $\mathcal{H}_0$
  is an output), multipoles to 2600, lensing included. UM-2 has three massive mass states, each with the degeneracy
  $N_{\mathrm{eff}}/3 = 1.0144$; CAMB gives each the density of a Fermi-Dirac gas times the degeneracy, so the masses passed to
  it are the masses divided by the fourth root of the degeneracy; because CAMB recovers them by inverting the relativistic
  density from the neutrino density and the mass fractions, these are iterated (damped exponent 0.8, 13 iterations) until
  the masses agree to $7.8\times10^{-12}$. The comparison model is CAMB's default (one neutrino of 0.06 eV,
  $N_{\mathrm{eff}} = 3.044$). The cosmic variance of one multipole is the relative error $\sqrt{2/(2l + 1)}$; the binned
  full-sky goodness of fit uses bins of 50 multipoles.
* **Thermal history and relic.** The ideal-gas integrals FE-121 by 160-point Gauss-Legendre quadrature on 360 temperatures from
  $10^{-4.5}$ to $10^{4.3}$ GeV; the Boltzmann equation FE-124 for $\ln Y_{\mathrm{DM}}$ with the implicit Radau method (relative
  tolerance $10^{-10}$) from $x = 5$ to 2000; the thermal average FE-125 by adaptive quadrature in the kinetic energy of the pair
  with exponentially scaled Bessel functions, tabulated on 200 to 260 points in $x$ and interpolated by a cubic spline; the
  strengths for $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ per species by Brent's method in the logarithm of the strength; the
  freeze-in FE-129 and the self-interaction channel FE-136 by the trapezoid rule on 600 and 800 logarithmic temperatures.
* **Determinism.** Every computation is deterministic: the Kohn-Sham scripts and the residual analysis fix the number of
  threads of the linear algebra to one (version 4); the document build writes no dates into the LaTeX sources, suppresses
  the PDF dates and trailer identifiers and fixes `SOURCE_DATE_EPOCH`.

