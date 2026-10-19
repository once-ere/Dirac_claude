# The verification record

Version 1 was rerun from fresh clones of the repository on 2026-10-17 at commit `b3c3c1a` (179 of 179 checks) and on
2026-10-18 at the commits `fa7305f`, `9285bb6` (180 of 180) and `5b73d16` (182 of 182; every computation as a separate step,
the longest 247 s); version 2 on 2026-10-18 at commit `4a6421d` (205 of 205; every computation as a separate step, 1027 s in
all); version 3 on 2026-10-18 at commit `726997f` (233 of 233; every computation as a separate step, 1100 s in all, the
longest the primordial integration with 269 s) and again, after the fixes of its independent review, at commit `815db9e`
(235 of 235; 1116 s in all, the primordial integration 269 s). In every run every check passed and every stored number was
reproduced to a relative $10^{-9}$ or better; in the runs from `9285bb6` on all numbers were identical except the run times,
the texts of check details and one Kohn-Sham integral, which differed by $1.1\times10^{-12}$ relative because the threaded
linear algebra did not sum in a fixed order (version 4 fixes the thread count, section 10); and the LaTeX sources, the PDF
documents and the figures were rebuilt byte-identical. Between the two runs of version 2, `um2_analysis.py` gained the
$^3P_0$ unitarity bound of item 22 (new stored numbers, the same 23 checks). After the run of version 3 at `726997f` the fixes of
its independent review (item 24) changed `um2_thermal.py`, `um2_coupled.py`, `um2_series.py`, `um2_cosmology.py` and the
`feedback` job of `um2_ks_jobs.py`, which were rerun in dependency order before the run at `815db9e`.

Version 4: the precision fixes of commit `cc2d514` changed `um2_coupled.py`, `um2_electroweak.py`, `um2_kohnsham.py`,
`um2_ks_jobs.py` and `um2_neutrino.py`; the affected computations (the seven Kohn-Sham jobs, `um2_neutrino.py`,
`um2_electroweak.py`, `um2_cosmology.py`, `um2_coupled.py`) and the new `um2_residuals.py` were rerun, and every script exits
with code 0 with all its checks: 287 of 287 (the reports in `universe_model_2/reports`). A rerun of version 4 from a fresh
clone is not part of this record.

# Corrections made during the work

1. The gauge-invariance test of the tip terms first used the wrong sign of the hypercharge phase; with
   $\psi \to \mathrm{e}^{\mathrm{i}Y\vartheta}\psi$ every term is invariant to $4\times10^{-15}$.
2. The finite-element cross-check of $\tilde m_{\mathrm{W}}^2$ was first limited by rounding; the Rayleigh quotient of the
   gradient form with Richardson extrapolation (observed order 4.01) agrees with the exact value to $3\times10^{-14}$.
3. The Kohn-Sham basis convergence and the conservation law were first checked without extrapolation; Richardson in the
   basis size (observed orders 4.95 for the energy, 2.97 for the hidden pressure; 4.96 for the energy since the
   deterministic thread count of version 4) was added.
4. The self-consistency loop did not converge for 592 particles at the record's coupling; a fixed labelling of the
   occupied set and a safeguarded Anderson mixing were introduced, the test coupling $\lambda_{\mathrm{test}}$ was adopted,
   and the record's coupling is kept as a stress test, which now converges.
5. A first statement that every primordial start above the unstable static block reaches the stable one was false in
   detail; the separatrix (the threshold of the initial $K$ as a function of the initial $\mathcal{H}_f$) was computed by
   bisection instead.
6. The primordial figure was first sampled too coarsely (aliasing of the radion oscillation) and is now densely sampled.
7. The sum rules of the uncertainty analysis were first imprecise for the sharp fermion zero modes; exact mpmath
   normalisation and the tip term fixed them ($10^{-8}$).
8. The radion quantity was stored under a wrong sign label; it is now stored as $\omega_{\mathrm{r}}^2$, the determinant of
   the Jacobian of the block equations.
9. Portal names of the first universe model (P1 to P6) in two check texts were replaced by I9, I11, I12.
10. The gauge-kinetic portal was first written with the scale to the power 5, which is dimensionally wrong in the geometric
    normalisation of the gauge fields; it is $\bar\Psi\Psi\,\mathcal{F}/\Lambda_\star^3$ (IN-17), and the symbol of the portal
    scale was changed so that it no longer clashes with the Dirichlet bound of the tip.
11. Before publication every number of the documents was compared with the computed outputs; four statements were
    corrected (the dark-matter wave number $\varpi = 1.89901$, the finite-element agreement $5\times10^{-10}$, the TT and EE
    agreements of version 1, and the restriction $\mathcal{H} = 0$ of the sourceless static block).
12. The kinetic term of the tip sigma field was first written with the sign of the signature $(+,-,-,-)$; in the
    signature $(+,+,+,-)$ of $x_1, \dots, x_4$ it is $-\frac{v_\Sigma^2}{4}\mathrm{tr}\big((D_\mu\Sigma)^\dagger D^\mu\Sigma\big)$,
    which gives mass terms $-\frac12$ times the squared mass times the square of the vector field with a positive squared
    mass (the computations always used positive squared masses).
13. With the real matrices $C\gamma^a$ antisymmetric, $\bar\Psi\gamma^a\Psi$ is anti-Hermitian; the portal currents are now
    written as the Hermitian currents $\mathrm{i}\bar\Psi\gamma^M\Psi$ and the Standard-Model currents as
    $\mathrm{i}\bar\psi\gamma^M\psi$.
14. The block response to the hidden pressure of a Kohn-Sham state first used $p_0$ alone; the common block scale is driven
    by the block-averaged pressure $\bar p = (p_0 + 3p_5)/4$, and $p_0 - p_5$ drives a block-shape mode outside the order-0
    metric (OPEN; quantified in version 4, section 10). The linearised sourced equations were added (`um2_background.py`,
    2 checks); they first omitted the density, which enters at first order through $3\mathcal{G}(K_*)\mathcal{H}^2 =
    \kappa\Delta\rho$; with it the adiabatic response reproduces the four-dimensional Friedmann acceleration equation exactly.
15. The statement that the numbers of quanta of $\Psi_A$ and $\Psi_B$ are separately conserved was first recorded as an
    asserted check; it is now computed with the author's matrices (commutators of $\mathcal{B}$ with $C$, $\gamma^a$,
    $C\gamma^a$, $\mathcal{S}^{ab}$), which also shows that extra-time momenta, outside the good sector, would mix the halves.
16. The radion lifetime was first quoted as an unverified estimate; it is now computed (ESTIMATE, with the coupling factor
    $C_{\mathrm{r}}$ explicit), as is the bound on the block rate today.
17. Figures: the BAO legend showed the data label twice and two labels of the uncertainty figure overlapped; the condensate
    figure no longer draws the vertical lines where its equation of state diverges.
18. An independent review of the five documents of version 1 against the outputs found, and the documents were corrected:
    the first-order fermion mass formula (it needs $\mathcal{Z}(-c_R)$ for the singlet, $c_R < 0$; the code always used the
    absolute value); the gap statement, which holds for the boson operators but not for $\Psi$ (the dark matter, 44.35 TeV,
    lies below the boson gap of 99.5 TeV); the sensitivity of $G_{\mathrm{N}}$ to the block, which is
    $\mathrm{d}\ln G_{\mathrm{N}}/\mathrm{d}\ln f = -4 + 2K_*(\mathrm{d}\mathcal{G}/\mathrm{d}K)/\mathcal{G}$ at $K_*$, $= +2.05$, and
    not $-4$ (recomputed; the lunar-ranging bound becomes $7.1\times10^{-4}\mathcal{H}_0$); $\Delta N_{\mathrm{eff}}$ of a
    thermalised fold band (recomputed); a level spacing (0.25000); a rounding (1.948); the definitions of $\bar M_{\mathrm{Pl}}$,
    $M_{\mathrm{Pl}}$, the radion formulas, the spread $\Delta(fy)$ of the proper hidden length, the unitarity estimate and the
    cosmic-variance measure; the statement on proper and coordinate localisation; and several notational clashes (a letter
    then used for $\mathrm{e}^{-a_4}$ is now written out).
19. A second review of version 1 found, and the documents were corrected: the electroweak parameter was written with the
    measured masses, $m_{\mathrm{W}}^2/(m_{\mathrm{Z}}^2\cos^2\theta_{\mathrm{W}})$, next to the on-shell definition
    $\cos^2\theta_{\mathrm{W}} = m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2$, which makes it identically 1; the computation always used
    $\rho_{\mathrm{EW}} = \tilde m_{\mathrm{W}}^2/(\tilde m_{\mathrm{Z}}^2\cos^2\theta_{\mathrm{W}})$. Checking the uncertainty relation
    for every state then showed that the bound $\langle k_\xi^2\rangle \ge 1/(4\Delta\xi^2)$ quoted for the hidden kinetic
    energy is not valid on the cell: the tip, where the cell ends, adds a boundary term, and the valid relation is
    $\langle k_\xi^2\rangle^{1/2}\Delta\xi \ge (1 - \varrho_\xi(-1))/2$ (the broad fold zero mode of $\Psi$ has
    $\langle k_\xi^2\rangle\Delta\xi^2 = 0.097$); a computed check of it was added. Further: the $\overline{\mathrm{MS}}$ angle in the
    $Z$ widths, the shooting accuracy, the normalisation volume $\mathrm{Vol}_7$ (not the proper seven-volume), the
    occupations $\phi_o$, the tip coupling matrices, and the notation (with a list of the symbols with more than one use in
    each document; version 4 replaces these lists by one meaning per symbol).
20. A third review of version 1 found, and the computations and documents were corrected: (a) the $W^\pm$, $Z$ fit set the
    angle of the gauge couplings equal to the on-shell angle of the measured masses and fitted the tree-level
    $\rho_{\mathrm{EW}} - 1$ to $\rho_{\mathrm{EW},0} - 1$, which put the model's $m_{\mathrm{Z}} = 91.1706$ GeV 17 MeV below the
    measured value; since $\rho_{\mathrm{EW},0}$ measures the custodial violation beyond the Standard-Model loops, the angle of the
    couplings is now fixed by the measured masses, $\cos^2\theta_{\mathrm{W}} = (m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2)/\rho_{\mathrm{EW},0}
    = 0.776368$, and the model reproduces both masses (check `mZ_reproduced`); $\beta_{\mathrm{W}} = 0.011912$ and every scale in GeV
    moved by $+8.50\times10^{-4}$ ($m_{\mathrm{KK}} = 121.32$ TeV, $H = 14.296$ TeV, gap 99.48 TeV, radion 48.42 TeV,
    $M_{\mathrm{DM}} = 44.35$ TeV). The tree-level $Z$ widths with the angle of the couplings were added (check
    `Z_width_scheme`). (b) The familiar bound $\langle k_\xi^2\rangle \ge 1/(4\Delta\xi^2)$ is guaranteed only for profiles
    negligible at the tip. (c) Symbol lists and wording.
21. **Version 2 (2026-10-18): three generations and three neutrino flavours.** By the author's orders of 2026-10-18 (option
    A): (a) three generations of quarks and leptons with one doublet bulk mass per sector, the twelve masses as exact $x_0$
    eigenvalues and the PMNS and CKM matrices as the tip matrices, proved exact for three generations (`um2_flavour.py`, new;
    `um2_spectra.py`, `um2_fields.py` extended); (b) the flavour conversion of the three neutrinos (`um2_neutrino.py`, new):
    vacuum, matter, accelerators, the Sun, the early Universe and $N_{\mathrm{eff}}$, the CNB of three mass states,
    supernovae; (c) the chiral tip $Z$ portal I9 is removed: with three neutrinos it has no role left, its even part is
    bounded by the invisible width ($N_\nu = 3 + 2r_{\mathrm{Z}}^2$, $r_{\mathrm{Z}}^2 < 0.0056$) and would still keep the fold band in
    equilibrium to 14.7 MeV ($\Delta N_{\mathrm{eff}} = 2.02$), and its oriented part would thermalise the fold band through the
    decays of the odd $\Psi_A$ states ($\Delta N_{\mathrm{eff}} = 0.0958$ to 0.1257, 2.1 to 2.4 standard deviations above ACT DR6);
    consequently both halves of $\Psi$ keep an exact fold parity and the dark matter consists of the lightest odd states of
    both halves (two species, relic recomputed: $x_{\mathrm{f}} = 30.38$, $G_{\mathrm{I12}} = (15.5\ \text{TeV})^{-3}$); (d) the
    invisible width uses the PDG 2025 value $N_\nu = 2.9963 \pm 0.0074$ instead of the LEP 2006 value; (e) $N_{\mathrm{eff}}$ is
    computed for three flavours (3.0476 to 3.0485) and the precision value 3.0432 (Cielo et al.) replaces 3.044; (f) the
    cosmology has three massive neutrinos ($\sum_im_i = 0.0599$ eV) instead of one of 0.05 eV and no dark radiation; (g) the
    $Z$ widths of three generations (2485.2 MeV with the QCD factor) remove the one-generation conflict (1232 MeV); (h) the
    Kohn-Sham portal sources use the three-generation localisations. Errors found and corrected during the version-2 work:
    the 1-3 MSW resonance energy was first evaluated with a spurious factor $1/c_{13}^2$ (11.49 GeV); it is
    $E = \Delta m_{ee}^2\cos2\theta_{13}/(2V_{\mathrm{CC}}) = 11.135$ GeV with $\Delta m_{ee}^2 = c_{12}^2\Delta m_{31}^2 +
    s_{12}^2\Delta m_{32}^2$, confirmed by the exact three-flavour root 11.133 GeV (now a check); CAMB's built-in
    normal-hierarchy option put the mass in one mass state, so the three mass states are now set up explicitly with the
    iteration of section 9; a check of the analysis (fermions below the uncertainty estimate) first used a threshold that the
    muon and the strange quark exceed and now tests the documented statement ($m/m_{\mathrm{Heis}} < 0.01$ for every fermion);
    in the documents the muon eigenvalue ($\tilde\varepsilon = 4.7795\times10^{-6}$), the Landau-Zener bound
    ($\mathcal{P}_{\mathrm{LZ}} \le 2.6\times10^{-77}$) and the explanation of $\Omega_\nu h_{100}^2$ (the non-relativistic coefficient
    94.06 eV at the instantaneous-decoupling temperature, 93.14 eV with the heating) were corrected; the published values of
    the decoupling method were read from the source (Escudero 2020, Table 1) and the separate-temperature value 3.048 added
    to the validation.
22. **Independent review of version 2 (2026-10-18).** A review of the five documents of version 2 against the outputs found
    every computed number in agreement except three roundings, and found the following, all corrected in the documents: (a)
    the dark-matter relic: the operator $\bar\Psi_{\mathrm{DM}}\Psi_{\mathrm{DM}}$ times a squared field strength annihilates a
    pair only from the state $^3P_0$, so the unitarity bound on the spin-averaged cross-section is
    $\sigma \le \pi/(4k_{\mathrm{cm}}^2)$ and $\langle\sigma v_{\mathrm{rel}}\rangle \le \sqrt{\pi x_{\mathrm{f}}}/M_{\mathrm{DM}}^2 =
    5.79\times10^{-26}$ cm$^3$/s; the freeze-out requirement $2.01\times10^{-25}$ cm$^3$/s exceeds it 3.47 times (the documents had
    compared it with $(4\pi/M_{\mathrm{DM}}^2)\sqrt{x_{\mathrm{f}}/\pi} = 2.32\times10^{-25}$ cm$^3$/s, the bound of one helicity
    channel without the spin average, and called the requirement 87 % of it); the relic abundance of the dark matter is
    therefore OPEN in version 2, and the check `B3_relic_requirement_and_unitarity` of `um2_analysis.py` now computes the
    bound, its numerical thermal average, the crossing velocity $v_{\mathrm{c}} = 0.263$ and the fraction (79 %) of pairs
    above it; (b) "no tip operator reaches $\Psi_B$" holds only for chiral tip currents with $P_L$ and for operators built on
    $\bar\Psi\Psi$ (a non-chiral tip current would reach $\Psi_B$); (c) the fast-flavour dispersion relation is written with
    the shifts by the moments of the electron-lepton-number distribution (now $\mathcal{I}_0$, $\mathcal{I}_1$) and the stated
    metric $\mathrm{diag}(1, -1)$ on $(x_4, x_3)$; (d) $c_{\mathrm{Z}} = \tilde c_{\mathrm{Z}} = 0$ is a modelling choice (ASSUMED):
    the invisible width bounds the even part and $N_{\mathrm{eff}}$ disfavours, but does not exclude, the oriented part; (e)
    the coordinate rule: the flavour, decoupling and fast-flavour equations had written a letter $t$ for $x_4$ and $z$ for the
    symmetry axis $x_3$; (f) roundings: the adiabatic solar $\mathcal{P}_{ee}$ at 15 MeV (0.306), the bulk mass of the tau
    singlet ($-9.205H$), the Kohn-Sham accuracy ($2.2\times10^{-9}$ relative); (g) minor items: the largest possible
    $J_{\mathrm{CP}}$ computed from the best-fit angles (0.0335) against NuFIT's marginalised value ($0.0333 \pm 0.0007$); the
    conventions of the supernova resonances (two-flavour conditions); the tip matrices equal the mixing matrices only with
    $\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}$ (ASSUMED); the three roles of the measured values; the sum rules of the
    uncertainty analysis (absolute $1.0\times10^{-8}$, relative $7.8\times10^{-4}$ and $6.0\times10^{-4}$ for $W^\pm$ and $Z$); the
    50-digit roots against the stored masses ($4.5\times10^{-11}$); the labels ESTIMATE and STANDARD; the strength required for a
    single species ($(17.6\ \text{TeV})^{-3}$ with $g_\rho = 105.75$, not a version-1 value); further notational clashes added
    to the symbol lists; (h) self-containment: equations and inputs used but not written in a document (the relic and
    $\Delta N_{\mathrm{eff}}$ formulas, the Einstein-Boltzmann equations, the BAO goodness of fit and data, the nonlinear background
    equations, the fermion equations with their boundary conditions, the decoupling equations, the CNB, Landau-Zener, adiabatic
    solar, condensate and pairing formulas, the Kohn-Sham equations behind the quoted equations of state) are now written out
    in every document that uses them.
23. **Version 3 (2026-10-18).** By the author's order for the coupled solution: (a) the computations `um2_thermal.py`,
    `um2_coupled.py` and `um2_series.py` (new), the matter power spectrum and the version-3 model in `um2_cosmology.py`, the
    Majorana alternative in `um2_neutrino.py`, and an optional potential on the lower component in the Kohn-Sham solver
    `um2_kohnsham.py` (the record's reference states reproduced again to $10^{-12}$); (b) the portal I13 was first coupled to
    the $B - L$ current; the computation C9 then showed that the annihilation of the dark matter into right-handed neutrinos
    and its inverse would thermalise them and add $\Delta N_{\mathrm{eff}} = 0.144$ (2.5 standard deviations above ACT DR6), so
    I13 couples to the baryon-number current ($G_{\mathrm{A}}$: $1.072 \to 1.278\times10^{-9}$ GeV$^{-2}$; xenon: 0.12 to 0.16 of
    LZ); (c) the first version of the C9 rates compared the production rate of three flavours with the equilibrium density of
    one; corrected (per flavour) before the result was recorded; (d) `um2_thermal.py` read a key of the analysis output that
    item 22 had renamed; corrected; (e) the early-Universe environments first put the whole net baryon density into protons;
    it is now shared by weak equilibrium, $n_{\mathrm{n}}/n_{\mathrm{p}} = \mathrm{e}^{-(m_{\mathrm{n}} - m_{\mathrm{p}})/T}$, and the
    QCD interaction measure had the wrong flavour thresholds in its perturbative branch and a special case at exactly 200 MeV
    (neither affected a stored number); (f) the text of the validity check C7 now refers to the benchmark strengths; (g) the
    thermal numerical result refines the version-2 statement on I12: a cross-section at the $^3P_0$ limit at every energy
    leaves $\Omega_{\mathrm{DM}}h_{100}^2 = 0.058$ per species, so I12 alone could give the relic only as a strongly coupled
    channel at the unitarity limit; (h) in MODEL a cross-reference to the neutrino decoupling pointed to section 9.4 instead
    of 10.4 (since version 2).
24. **Independent review of version 3 (2026-10-18).** A review of the five documents of version 3 at commit `726997f` against
    the outputs (2055 s, 74 tool calls) found every version-3 number in agreement with the stored outputs except the items
    below, and the following errors and omissions, all corrected in the computations and the documents (the affected scripts
    rerun; 235 checks, all passing): (a) the I13 bilinear $\mathrm{i}\bar\Psi\gamma^MP_b\Psi$ is Hermitian only for $M \ne x_0$,
    since the Hermitian conjugate of $\mathrm{i}C\gamma^{x_0}P_b$ is $\mathrm{i}C\gamma^{x_0}P_a$; the action now sums over
    $M = x_1, \dots, x_7$, and the new check `C8_I13_algebra` verifies with the author's matrices the Hermiticity, its failure for
    $x_0$, $CP_bC^{-1} = P_a$, the Lorentz property and the structure under $\mathcal{B}$ ($C\gamma^MP_b$ commutes with $\mathcal{B}$
    for $x_1, \dots, x_4$ and anticommutes with it for $x_5$, $x_6$, $x_7$, whose currents vanish for spinors in one half, so the
    Standard-Model zero modes, all in the half $\mathcal{B} = -1$, are not mixed); no number changes, since the zero-mode
    reduction uses the four-dimensional components only; (b) the block response of the coupled solution kept only the hidden
    pressure of non-relativistic matter and only the $\Delta\bar p$ term of the adiabatic response; it now uses the full
    response ($c_\rho$, $c_3 = -3c_\rho$, $c_p$) and the hidden pressure $\bar p = \frac14\,\partial p/\partial\ln f$ of every
    species, the hot plasma included (ideal gases with the $x_0$ masses, the QCD interaction measure with the block dependence
    of the QCD scale, the order-$\alpha$ electroweak pressure with the block dependence of the couplings): $\Delta\ln f$ at the
    freeze-out $5.6\times10^{-45} \to 1.1\times10^{-34}$ ($7\times10^{-39}$ in the electroweak era, at most $9\times10^{-49}$ from
    nucleosynthesis on), the loop gain $1.3\times10^{-44} \to 1.1\times10^{-33}$, the radion term of the metric series accordingly;
    the Kohn-Sham block feedback also reports the full response; the conclusion, a negligible back-reaction, is unchanged; (c)
    the thermal $W$, $Z$ condensates had only the free massive-vector part; the order-$\alpha$ interaction part (FE-76;
    Feynman-Hellmann; for QCD it reproduces the trace-anomaly condensate to $10^{-16}$, now part of check C4) dominates above
    $m_{\mathrm{W}}$: the $W$ condensate at the freeze-out is $-5.0\times10^{11}$ GeV$^4$; (d) the freeze-out environment used the
    version-2 $x_{\mathrm{f}} = 30.38$ ($T = 1.46$ TeV); it uses the version-3 $x_{\mathrm{f}} = 31.23$ ($T = 1.42$ TeV), and
    $\Delta\varepsilon_{\mathrm{DM}}/M_{\mathrm{DM}}$ there is $-1.5\times10^{-6}$ (was $-1.6\times10^{-6}$); the degrees-of-freedom
    table lists 1.42 TeV instead of 1.46 TeV; (e) the thermal history did not state $\lambda$: the self-interaction contains the
    channel in which two dark-matter particles become two fold quanta through the transition scalar density
    $n^{\mathrm{sc}}_{\mathrm{DF}} = a_{\mathrm{DM}}b_{\mathrm{fold}} + b_{\mathrm{DM}}a_{\mathrm{fold}}$; the new computation C10 gives
    $\Delta N_{\mathrm{eff}} = 1.83\times10^{26}G_\lambda^2$ GeV$^4$ and the bound $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$, now
    ASSUMED (the Kohn-Sham test value $\lambda_{\mathrm{test}}$ with $v_{\mathrm{t}} = H^{-3}$ would thermalise the fold bands and add
    0.19); (f) the elastic $\nu_R$ rate of the $B - L$ alternative used $\sigma_{\mathrm{el}} = G_\nu^2E^2/\pi$ instead of
    $G_\nu^2E^2/(2\pi)$ for a Weyl $\nu_R$ on a heavy Dirac fermion: kinetic decoupling at $x = 25.1 \to 24.4$
    ($T = 1769 \to 1816$ GeV), $\Delta N_{\mathrm{eff}} = 0.144$ unchanged; (g) the I11 production of $\nu_R$, quoted as $10^{-14}$ of
    the I13 rate without a source, is now computed: $2.0\times10^{-17}$; (h) the fractions of the annihilation rate above the
    unitarity crossings were integrated inaccurately (one of them exceeded 1): they are now computed by adaptive quadrature
    with the break points of the thermal weight (I12 at the relic strength: 96 %; the I12 benchmark $5.3 \to 5.2\times10^{-4}$;
    I13 uncapped $24.5 \to 24.8$ %, capped $19.0 \to 21.7$ %); the exact I12 crossing at $E_{\mathrm{cm}} = 89510$ GeV is quoted
    with its relative velocity $v_{\mathrm{rel}} = 2\beta_{\mathrm{cm}} = 0.269$ (0.274 is the non-relativistic formula); the
    relic at the $^3P_0$ limit compares the thermal average and $\sqrt{\pi x}/M_{\mathrm{DM}}^2$ at the same $x$ (5.33 against
    $5.84\times10^{-26}$ cm$^3$/s); (i) stale or mixed statements: "$c_{\mathrm{V}} = 0$" and "no dark radiation" or "no extra
    radiation" of version 2; the cosmology labels (UM-2 version 3 is the model with the freeze-in fold bands:
    $N_{\mathrm{eff}} = 3.0442$, $\sigma_8 = 0.8118$, $\chi_{\mathrm{BAO}}^2 = 31.49$, $\mathcal{H}_0 = 67.38$ km/s/Mpc; the model
    without them is the neutrino content of version 2); "relic OPEN" qualified as the result of version 2; the check counts of
    `um2_neutrino.py` (16) and `um2_cosmology.py` (8); the amplitude of the kinetic-function shift at the freeze-out
    ($1.7\times10^{-16}$, not below $10^{-50}$); "perturbative" made precise (22 % of the freeze-out rate at the bound of total
    angular momentum 1; $G_f^{-1/2} = 30$ TeV for the quark doublet, below $E_{\mathrm{cm}} \approx 89$ TeV); the $\nu_R$ couplings
    (the I11 coupling as well as the tip mixing); the dark matter is not counted in $g_\rho$, $g_s$ (as in the code); roundings
    ($\tilde I^{(b)}_{\nu_R} = 0.301$ to 0.308, $g_\rho = 104.95$ at 200 GeV, $D_+\mathrm{e}^{-a_4} = 0.7878$ today,
    $\Phi_{\mathrm{rms}} = 5.03\times10^{-8}$ at 1 Mpc$^{-1}$, the Poisson agreement $1.5\times10^{-6}$); the signature convention of
    the trace anomaly and of the Proca Lagrangian, written for $(+,-,-,-)$; the $\overline{\mathrm{MS}}$ angle in the running
    couplings; the Yukawa strengths $\mathcal{A}_n$ for two different profiles; the order-2 magnitude
    $(2.4\times10^{-5})^2 = 5.8\times10^{-10}$; a heading labelled DERIVED over estimates; (j) self-containment: the quark
    sensitivities to the block scale, the scale $2\pi T$ of $\alpha_3$, the densities of the environments, the hadron list,
    $\Omega_{\mathrm{m}}$, the symbols $N_{\mathrm{c}}$, $N_{\mathrm{fold}}$, $G_{\mathrm{A}}^{B-L}$, the factor 2 of the two dark-matter
    species, $g_{s,e\gamma}$, $K_1$, $K_2$, the squared centre-of-mass energy, $\beta_{\mathrm{cm}}$, the total angular momentum of a
    partial wave and the version-3 symbols are now stated in every document that uses them, and the variable
    $E_{\mathrm{cm}}^2/(4M_{\mathrm{DM}}^2) - 1$ is no longer written with the letter $z$ (in version 4 $z$ is only $6Hx_0$ and the
    redshift is $z_{\mathrm{red}}$).
25. **Version 4 (2026-10-18): the organisation and presentation ordered on 2026-10-18 at 15:42.** (a) *The presentation
    rules* S1 to S6 (section 2) for MODEL, FIELD_EQUATIONS, SOLUTION, ANALYSIS and PROVENANCE: every document starts with "How
    to read this document"; every display equation is followed by the complete list of its symbols; every field equation or
    interaction term that a document uses is written out there with its tag FE-$n$ or IN-$n$ and its symbols; a solution is
    presented as the field equation, the approximation (the small parameter and the size of what is neglected), the
    solution, its check in its own equation and in concert with the other field equations, and the status labels; the reader
    is never sent to another file; every change of a claim is stated here (commit `9dbc424`). (b) *The notation.* Version 3
    used many letters for several things ($k$, $s$, $M$, $H$, $p$, $a$, $\kappa$, $\Lambda$, $\delta$, $n$, $\mu$, $e$, $J$, $u$,
    $G$, $\beta$, $w$, $f$, $c$ and others); version 4 gives every meaning its own symbol, among them the block variable
    $K = 1/f^2$ (was $k$, now only a wave number); the Hubble rate $\mathcal{H}$ and the rate $\mathcal{H}_f$ of the block scale
    (were $H$ or $A$, and $h$; $H$ is only the author's constant); the Lovelock order as the index $p$ in brackets,
    $\alpha_{(p)}$, $w_{(p)}$, $\mathcal{L}_{(p)}$, $\mathcal{E}_{(p)}$; the energy-momentum tensor $\mathcal{T}^M{}_N$ (was $T$, now
    only the temperature); the pressure $p_5$ of the extra times and the stabiliser density $\rho_{\mathrm{stab}}$; the gauge
    couplings $g_3$, $g_2$, $g_1$ and $\hat g_3$, $\hat g_2$, $\hat g_1$ (were $g_s$, $g$, $g'$), so that $g$ is only the metric;
    the tip mixing matrices $\mathcal{K}$ and the tip Yukawa matrices $\mathcal{Y}_\nu$, $\mathcal{Y}_e$, $\mathcal{Y}_u$,
    $\mathcal{Y}_d$; the scalar density $n^{\mathrm{sc}}$ of dirac16complex; the mass parameter $m_\Psi$ and the record's
    parameter $\mathcal{M}$; the four-dimensional dark-matter and fold-band fields $\Psi_{\mathrm{DM}}$, $\Psi_{\mathrm{fold}}$
    ($\chi$ is now only the block spinor); the dimensionless boson eigenvalue $\tilde m^2$, its wave number $\varpi$ and the
    profiles $F$; the Newtonian-gauge potentials $\Phi$ and $\Psi_{\mathrm{N}}$; the gauge fields in the geometric normalisation
    ($G$, $W$, $B$) distinguished from the canonically normalised $W^\pm$, $Z$, $A$; the overlaps $\tilde I_{of}$ made
    dimensionless by an explicit factor $1/H$; Euler's number, the imaginary unit and the differential upright. The table of the
    decisions (the version-3 symbol and meaning, the version-4 symbol) is `docs_src/NOTATION.md` (commit `fd749e8`); this
    document applies it in every display, inline formula and sentence. (c) *The symbol registry and its check.* Every symbol
    of the documents has one entry (meaning in complete sentences, unit, value and status) in the registry
    `docs_src/symbols/*.json`: the core file with the symbols of the field equations (488 entries when the inventory was made,
    commit `fd749e8`) and one file per document (`provenance.json` for this document). `tools/symbols_tool.py` (commit
    `9dbc424`; extended in `fd749e8`: exponents of $\mathrm{e}$ and of brackets, evaluation bars and integral limits are
    expressions, not indices) writes the symbol list under every display equation from the registry and checks that every
    atom of every display (symbols, name subscripts, index letters, primes and daggers) is defined by a listed key, that every
    display has its list, and that no atom has two entries; since commit `1e264d0` it also checks that every display tagged
    FE-$n$ or IN-$n$ is written exactly as in the inventory, with the same keys. (d) *The inventory.*
    `docs_src/equations.json` lists the 136 field equations FE-1 to FE-136 and the 18 interaction terms IN-1 to IN-18 in the
    version-4 notation, each with its title, status, fields, the place where it is solved and the registry keys of all its
    symbols; a test document of all 154 equations passed the check and built with 0 overfull boxes (commit `fd749e8`). Commit
    `1e264d0` aligned it with the documents: FE-40, FE-42 and FE-43 now write the $x_0$ component (with $p_0$) and the
    extra-time components $x_5$, $x_6$, $x_7$ (with $p_5$) separately, next to the block-isotropic form with $\bar p$; FE-52 and
    FE-53 quote the squared eigenvalues $\tilde m_1^2$, $\tilde m_n^2$; FE-79 records the first-order result of fix 1 of
    section 10. (e) *The residual analysis.* The new
    computation `um2_residuals.py` (52 checks; 287 in all) measures the residual of the stored solution in 26 field equations
    and 26 links in concert; its findings are section 10 (commit `cc2d514`). (f) *The precision fixes:* the first-order
    perturbation theory for $\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}}$, the robust integration of the right-handed
    neutrinos, the CNB quadrature, the deterministic thread counts in the Kohn-Sham scripts, and a stale check text (section
    10; commit `cc2d514`). (g) *Claims.* No claim of version 3 changes; the changed numbers and the statements made precise are
    listed at the end of section 10. (h) The documents of version 4: SOLUTION and ANALYSIS (commit `1e264d0`), MODEL,
    FIELD_EQUATIONS and PROVENANCE (this version).

# What is not in the repository, and why

By the author's instruction the following private inputs are never committed (they are git-ignored): the prompt files, the
author's private PDF with the supernova dark-energy fits, the folders `dirac-main/` and `vendor/`, the archive
`dirac-main_2.zip`, the files `Generalized_Kronecker_Delta.*`, and the notebook `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb`
with its `.mx` files. The paper "Neutrino Flavor Conversion.pdf" (Gogilashvili and Tamborra, arXiv:2605.16504) is a
third-party publication and is not committed either; UM-2 cites its results. UM-2 uses from these inputs only what is written
out in this document (the notebook formulas of the metric and of the gamma matrices, the two supernova fits, the explosion
statistics).

# Reproduction

From the repository root, with Python 3 and the packages sympy, numpy, scipy, mpmath, matplotlib and camb installed
(`pip install sympy numpy scipy mpmath matplotlib camb`), the commands

```text
python universe_model_2/code/um2_algebra.py
python universe_model_2/code/um2_geometry.py
python universe_model_2/code/um2_background.py
python universe_model_2/code/um2_fields.py
python universe_model_2/code/um2_spectra.py
python universe_model_2/code/um2_flavour.py
python universe_model_2/code/um2_neutrino.py
python universe_model_2/code/um2_ks_jobs.py validate
python universe_model_2/code/um2_ks_jobs.py spectrum
python universe_model_2/code/um2_ks_jobs.py ground8
python universe_model_2/code/um2_ks_jobs.py ground592
python universe_model_2/code/um2_ks_jobs.py darkmatter
python universe_model_2/code/um2_ks_jobs.py portals
python universe_model_2/code/um2_ks_jobs.py feedback
python universe_model_2/code/um2_electroweak.py
python universe_model_2/code/um2_primordial.py
python universe_model_2/code/um2_cosmology.py
python universe_model_2/code/um2_analysis.py
python universe_model_2/code/um2_thermal.py
python universe_model_2/code/um2_coupled.py
python universe_model_2/code/um2_series.py
python universe_model_2/code/um2_residuals.py
python universe_model_2/tools/symbols_tool.py check
python universe_model_2/tools/build_docs.py
python universe_model_2/tools/compare_outputs.py
```

rerun every computation in dependency order (each exits with code 0 if and only if all its checks pass; the residual
analysis reads the outputs of all the others and must run last), check the symbol lists of the five documents against the
registry (the check must end with `symbols_check=OK`), rebuild the LaTeX and PDF documents from the Markdown sources (pandoc
and a TeX Live installation with the `lmodern` package are needed; every document must build with 0 overfull boxes), and
compare the regenerated files with the committed ones (numbers to a relative $10^{-9}$, run times and check texts listed
separately). The document build is deterministic: no dates in the LaTeX sources, PDF dates and trailer identifiers suppressed,
a fixed `SOURCE_DATE_EPOCH`.

Software used: Python 3.13.16, sympy 1.14.0, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, matplotlib 3.11.2, camb 2.0.5, pandoc
3.1.3, pdfTeX 1.40.25 (TeX Live 2023).

# History in the repository

UM-2 was started on top of commit `0cb4916`. Version 1: its computations were committed in the order algebra and geometry
(`ca523d9`), background gravity (`0b3e10d`), field reductions (`6fc35a0`), mass spectra (`dcfd528`), Kohn-Sham (`2f3018e`),
electroweak sector (`2e4c48d`), primordial era (`a502e62`), cosmology (`717b46e`), analysis (`a06b55e`), followed by the
corrections listed above and the documents MODEL, PROVENANCE, FIELD_EQUATIONS, SOLUTION and ANALYSIS (Markdown, LaTeX and PDF
each); the fixes of the three independent reviews are in `b386446`, `fa7305f`, `b0e686e`, `9285bb6`, `d92a61b`, `c98de95`,
`1561566`, `df358db` and `5b73d16`; a checklist for manual reruns and the comparison tool are in `7b86239`. Version 2: three
generations and the masses and mixing (`94621af`), the neutrino flavour conversion (`a0d750a`), the electroweak sector of three
generations (`cf824d5`), the removal of the tip $Z$ portal and the cosmology with three massive neutrinos (`53c5139`), the dark
matter of both halves, the twelve-fermion tables and the three-generation tip and gauge checks (`b755990`), the corrected 1-3
resonance (`b999f57`), the documents MODEL (`9a5b92b`), FIELD_EQUATIONS (`79d9d31`), SOLUTION (`a3dcc6a`), ANALYSIS (`df6d94a`)
and PROVENANCE (`4a6421d`), and the fixes of the independent review of version 2 (item 22; `ecca926`). Version 3: the thermal
history, the coupled solution, I13, the metric series and $\sigma_8$ (`15c2aab`), I13 on the baryon-number current (`3fa1b49`),
the documents MODEL (`765f0b8`), FIELD_EQUATIONS (`41e921a`), SOLUTION (`df23013`), ANALYSIS (`19d2c06`) and PROVENANCE
(`726997f`), the fixes of the independent review of version 3 with the record of the fresh-clone verification of `726997f`
(item 24; `815db9e`), and the record of the fresh-clone verification of `815db9e` (`93e5c03`). Version 4: the presentation
rules and the symbol tool (`9dbc424`), the residual analysis and the precision fixes (`cc2d514`), the notation, the inventory
and the core registry (`fd749e8`), the documents SOLUTION and ANALYSIS of version 4 with the inventory aligned and the
extended symbol check (`1e264d0`), and the documents MODEL, FIELD_EQUATIONS and PROVENANCE of version 4 (this version).
