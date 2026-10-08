## 15. Solving the Kohn-Sham equations along the deflating history

Chapter 14 turned the Kohn-Sham problem of the field dirac16complex in the author's primordial universe into a problem a computer can solve: pairs of real functions of one variable, the hidden coordinate $y$, in eight independent blocks, with an effective mass and a potential made by the quanta themselves. This chapter solves that problem. It explains, line by line, the numerical method of the Revision Kohn-Sham solver (a Rust program of the repository), runs the solver over its whole list of states, and reads from the results what happens to the gas of quanta while the three extra times $x_5, x_6, x_7$ deflate exponentially and ordinary 3-space inflates: its levels, gaps, energies, densities, its energy-momentum tensor, how well it can follow the moving background, and its thermodynamics. Five complete notebooks, 15a to 15e, repeat every step and reproduce the numbers of the Revision record.

### 15.1 What this chapter does

**Why solving is a chapter of its own.** The Kohn-Sham equations of Chapter 14 are not solved by writing down a formula. Their orbitals make the potentials and the potentials make the orbitals, so the equations must be solved again and again until the two agree (self-consistency). Each orbital is itself the solution of a boundary-value problem: a pair of differential equations with one condition at each end of the hidden direction, which has solutions only for special energies, the levels. The gas has hundreds of occupied orbitals, and the whole computation must be repeated for three particle numbers, five couplings, five instants of the deflating history and three temperatures. A method is needed that finds every level without missing one, that labels each level so that it can be followed from one iteration, coupling or instant to the next, and that is accurate enough that two independent programs agree to many digits. This chapter teaches that method and what it finds.

**What is done, in order.**

- The equations the solver must solve, the parameters of the model and the list of states it computes, called the **canonical matrix** (Section 15.2).
- How one level is found: shooting from the tip to the brane, the Pruefer angle that turns the search for levels into counting, and Newton's method inside a bracket (Section 15.3).
- How the levels of the whole gas are organised: shells of 3-momenta, sectors, label sets, the brane band and its redshift along the history (Section 15.4).
- Self-consistency: the loop, Anderson mixing, the energy of the gas, an exact symmetry of the smallest state, and the first excited state (Section 15.5).
- Notebook 15e, which writes the whole method in plain Python and reproduces numbers of the solver (Sections 15.6 to 15.9).
- The Rust solver and its canonical matrix, and what the matrix shows (Sections 15.10 to 15.15, Notebook 15a).
- The energy-momentum tensor of the gas, its conservation along the hidden direction, the energy change along the history, and why the gas cannot be the source of the history (Sections 15.16 to 15.20, Notebook 15b).
- Adiabaticity: whether the gas follows its instantaneous states while the background moves (Sections 15.21 to 15.25, Notebook 15c).
- Thermodynamics: the gas at a temperature, the chemical potential and why it must be computed in a special way (Sections 15.26 to 15.30, Notebook 15d).
- What we proved, what we computed, what we assumed (Section 15.31), and seven exercises with complete worked answers (Section 15.32).

**The five notebooks.** The run times are the two measured executions of each notebook, the build run and the check run, that section 4.5 of its provenance file `Revision/textbook/notebooks/<name>.PROVENANCE.md` records; they were measured on the computer that built the book, where the solver used 22 threads, while other programs ran at the same time, which explains the spread. A laptop may need two or three times as long, and Notebook 15a, whose solver divides its work over all cores, up to about ten minutes.

| notebook | what it computes | Rust, PASS lines, figures, run time |
| --- | --- | --- |
| 15e | the solver's method by hand: shooting, Pruefer label, Newton, RK4 order, brane band, self-consistency for $N = 8$ | no Rust; 18 PASS lines; 6 figures; 11 to 12 s |
| 15a | the whole canonical matrix with the Rust solver, compared with the record | Rust; 25 PASS lines; 8 figures; 164 to 232 s |
| 15b | the energy-momentum profiles, the conservation law along $y$, the energy change along the history | Rust; 18 PASS lines; 7 figures; 23 to 29 s |
| 15c | the adiabaticity measure, Hellmann-Feynman, a Fermi-level crossing | no Rust; 12 PASS lines; 6 figures; 10 to 15 s |
| 15d | thermodynamics: chemical potential, free energy, entropy, heat capacity | Rust; 15 PASS lines; 7 figures; 36 s |

The notebooks are placed in the order in which the ideas are needed: 15e first, because it teaches the method that the Rust solver uses in the others.

**The status of every statement.** Every statement of this chapter carries one of the five labels of Chapter 0.

- PROVED: the exact reduction to blocks, the boundary conditions as conditions on the orbitals, the exact free levels at zero momentum, the slope of the brane band, the rescaling identity between the instants of the history, the formulas of the densities, potentials, energy and energy-momentum tensor, the conservation law along $y$, the energy-change law along the history, the Hellmann-Feynman relation and the adiabaticity measure. They are verified twice in the Revision record, by sympy in `Revision/kohn_sham/reports/ks-theory-python.json` and by WolframScript in `Revision/kohn_sham/reports/ks-theory-wolfram.json`; the check names are given with each statement. The mathematical facts of the method (the monotone Pruefer phase, the derivative formula of the phase, the Hermite midpoint, the Anderson weights, the double counting of the interaction energy, the symmetry $E(-\lambda) = -E(\lambda)$ of the zero-mode state, the adiabaticity estimate, the heat-capacity formula and the balance form of the chemical potential) are derived line by line in this chapter.
- COMPUTED: every level, energy, density, pressure, gap, adiabaticity number and thermodynamic function. They come from the Rust solver; its own checks are in `Revision/kohn_sham/reports/ks-rust-solver.json` (42 checks, all PASS), its repeat and refined runs in `Revision/kohn_sham/reports/ks-rust-determinism.json` (14 checks, all PASS), its chemical potentials against 40-digit roots in `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` (5 checks, all PASS), and the notebooks of this chapter reproduce them with the measured differences given with each number.
- ASSUMED: the good sector (no dependence on the extra times) and the Z2 mirror brane at $y = 0$. Three further assumptions are of a special kind and carry an extra word. CHOSEN: the regular tip condition at the cutoff $y = -L$ and the value $L = 3$ (the record calls them "chosen"); what the choice of $L$ changes is COMPUTED in the record (`Revision/kohn_sham/tip_convergence/tip-convergence.json`, 7 checks, all PASS): at most 1.4 per cent of the energy of the free gas, except $N = 688$ at the first slice, but much for the interaction (Section 15.2, the paragraph on the cutoff). CONVENTION: which levels count as particles (the positive branch and the zero modes) and that the negative branch, the sea, is never populated, not even thermally; its justification is OPEN. PRESCRIBED BACKGROUND: the history $a_4 = AHx_4$ with $A = 1$; it is given, not solved for, the gas does not act back on it, and Section 15.16 shows why it cannot (the record `Revision/field_equations_a4/reports/ks-source-conditions.json`).
- HYPOTHESIS: none. No statement of this chapter goes beyond the equations and their numerical solutions.
- OPEN: the time-dependent (non-adiabatic) problem, a thermal treatment of the sea, the justification of the filling convention, and the limit of a large cutoff $L$ wherever the record does not establish it.

**What this chapter does not touch.** No statement of this chapter concerns pairs of universes, their creation or matter and antimatter. One check of the solver's report, `t3_block_map_solver_selftest`, solves a state with the mass $m$ and a state with the mass $-m$ and finds equal energies; the report itself calls it a numerical self-test of the program and NOT a proof of the theorem T3, which belongs to Chapter 19. Nothing computed here says that any universe is created, in pairs or otherwise. Where Section 15.26 speaks of thermal holes in the sea, it means excitations inside one universe, not pairs of universes.

**Notation and units.** The author's coordinates are $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates with the scale factor $e^{a_4}\sin^{1/6}z$; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which deflate exponentially with the scale factor $e^{-a_4}\sin^{1/6}z$; $x_8$ is the hidden space direction, with $z = 6Hx_8$ between 0 and $\pi/2$. The hidden coordinate is $y = \ln(\sin z)/(6H)$ (Chapter 14); it runs from the **tip** $y = -L$ (where the model cuts the space) to the **brane** $y = 0$. A **slice** is one instant of the history, and $a_{4,0}$ is the value of $a_4$ there. In all numbers $H = 1$ and $m = 1$, so energies, momenta and temperatures are in units of $m$ (which equals $H$) and lengths in units of $1/H$; Boltzmann's constant is 1, so a temperature is an energy.

### 15.2 The equations the solver must solve

This section collects, without proofs, the results of Chapter 14 that the solver uses, and adds the parameters of the model. Chapter 14 proves each formula; here we only need to read them.

**One orbital.** At a slice $a_{4,0}$, an orbital of the gas has a 3-momentum $\mathbf k$ (a vector of three numbers), a block type $j = +1$ or $j = -1$, and a pair of real functions $a(y)$, $b(y)$ on the interval $-L \le y \le 0$. Its level $\varepsilon$ and the two functions obey the **block equation in real form** (`Revision/kohn_sham/ks-theory.json`, blockEquation.realForm; checks block_hamiltonian and block_ode_equivalent):

$$
a' = M a - \big(\kappa k + j(\varepsilon - v)\big)\,b, \qquad b' = \big(j(\varepsilon - v) - \kappa k\big)\,a - M b ,
$$

where the prime means $d/dy$, $k = |\mathbf k|$ is the length of the momentum, $\kappa = e^{-Hy - a_{4,0}}$ is the momentum weight of Chapter 14, $M(y)$ is the **effective mass** and $v(y)$ the **potential**. The 16-component field of the orbital is built from $\chi = (a, ib)$ and the block basis of Chapter 14. The slice enters only through $\kappa$.

**The boundary conditions.** At the tip the solver uses the regular tip condition $b(-L) = 0$ (CHOSEN; check bc_tip_family). At the brane the ASSUMED Z2 mirror allows two kinds of orbitals, called the two **parities**: even orbitals have $b(0) = 0$, odd orbitals have $a(0) = 0$ (check bc_brane_parity_conditions). Both conditions make the current along $y$ vanish, and with them the block Hamiltonian is self-adjoint, so the levels are real (check bc_self_adjoint_boundary_term).

**The lattice of 3-momenta.** 3-space is a torus of coordinate size $\ell$, so the allowed momenta are $\mathbf k = \Delta k\,(n_1, n_2, n_3)$ with whole numbers $n_1, n_2, n_3$ and $\Delta k = 2\pi/\ell = 0.25$. The numbers $n_1^2 + n_2^2 + n_3^2$ are written $n_2$ (a single symbol, read "n-two", not the second component), and all momenta with the same $n_2$ form a **shell**; they have the same length $k = \Delta k\sqrt{n_2}$, and their number is written $r_3(n_2)$. For example $r_3(0) = 1$ (only the zero vector), $r_3(1) = 6$ (the six vectors $(\pm1, 0, 0)$, $(0, \pm1, 0)$, $(0, 0, \pm1)$), $r_3(2) = 12$, $r_3(3) = 8$, $r_3(4) = 6$, $r_3(7) = 0$ (no three squares add up to 7). The levels depend only on $k$ (check rotation_invariance), and each level of block type $j$ in the shell $n_2$ belongs to $4r_3(n_2)$ orbitals: the four blocks of that type times the $r_3(n_2)$ directions (ks-theory.json, blockEquation.degeneracy). This number is the **degeneracy** $g$ of the level. A **sector** is a triple (shell $n_2$, block type $j$, parity).

**Densities.** The **proper** densities (per unit of proper 7-volume) of the number of quanta and of the scalar $S = \bar\Psi\Psi$ are sums over the levels (ks-theory.json, densities):

$$
n(y) = \sum w\,g\,f\,P\,(a^2 + b^2), \qquad S(y) = \sum w\,g\,f\,P\,j\,2ab, \qquad P = \frac{e^{-6Hy}}{\mathrm{Vol}_7} ,
$$

where $f$ is the occupation of the level (1 for full, 0 for empty, a number in between at a temperature), $w = \tfrac12$, and $\mathrm{Vol}_7 = \ell^3v_t$ is the coordinate volume of 3-space times the extra-time volume $v_t = 1$. With $\ell = 2\pi/\Delta k = 8\pi$, line by line:

$$
\mathrm{Vol}_7 = (8\pi)^3\cdot 1 = 512\,\pi^3 = 15875.2137 .
$$

Rule: $\ell^3 = 8^3\pi^3 = 512\pi^3$, and $\pi^3 = 31.00628$. The record has the same number (`Revision/kohn_sham/results/parameters.json`, physics.Vol7). The factor $e^{-6Hy}$ turns a density per unit $y$ into a density per unit proper volume, because the proper volume element is $\sqrt{|g|}\,dy = e^{6Hy}dy$ (Chapter 14). The weight $w = \tfrac12$ belongs to the **doubled system**: the Z2 mirror makes a copy of the patch, every orbital is normalised on the patch, $\int_{-L}^{0}(a^2 + b^2)\,dy = 1$, and the particle number $N = \sum g f$ counts the quanta of the patch and of its mirror copy together; one patch holds $N/2$.

**Potentials and energy.** The contact interaction $U = \tfrac{\lambda}{2}S^2$ with the exact local exchange of Chapters 13 and 14 gives (ks-theory.json, exchange.kohnShamPotentials; check ks_potentials)

$$
e_{int} = \lambda\Big(\tfrac{15}{32}S^2 - \tfrac{1}{32}n^2\Big), \qquad M = m + \frac{\partial e_{int}}{\partial S} = m + \tfrac{15}{16}\lambda S, \qquad v = \frac{\partial e_{int}}{\partial n} = -\tfrac{1}{16}\lambda n ,
$$

and the **Kohn-Sham energy** of the doubled system is

$$
E_{KS} = \sum g\,f\,\varepsilon - 2\,\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}e_{int}\,dy .
$$

Section 15.5 derives why the interaction energy is subtracted here. The term $\tfrac{15}{32}\lambda S^2$ is the Hartree energy $\tfrac{\lambda}{2}S^2$ plus the scalar part $-\tfrac{1}{32}\lambda S^2$ of the exchange energy, and $-\tfrac{1}{32}\lambda n^2$ is the rest of the exchange energy (Chapter 13); the potential $v$ therefore comes from the exchange alone, and the notebooks call it the exchange potential.

**Which levels are particles (CONVENTION).** The equations have levels of both signs. The convention of the record (ks-theory.json, thermodynamics.fillingConvention) is: particles occupy the **positive branch**, the levels whose value without interaction ($\lambda = 0$) at the same slice is positive, together with the **zero modes** at $k = 0$ (the levels $\varepsilon = 0$ of the free problem); the levels of the negative branch form the normal-ordered **sea** and are never occupied, not even at a temperature. The justification of this convention is OPEN; Section 15.26 measures where it stops being reasonable.

**The particle numbers.** The record uses three particle numbers (`Revision/kohn_sham/results/parameters.json`, particleNumbers). $N = 8$ fills exactly the eight zero modes at $k = 0$ (four blocks of each type). The next levels above the zero modes are the **brane band**, the lowest even level of block type $j = +1$ in each shell $n_2 \ge 1$ (Section 15.4); in the free gas at $a_{4,0} = 0$ the band levels increase with $n_2$, so filling them shell by shell gives **closed shells** (every level either full or empty). Line by line, with $g = 4r_3(n_2)$:

$$
8 + 4\big(r_3(1) + r_3(2) + r_3(3) + r_3(4)\big) = 8 + 4\,(6 + 12 + 8 + 6) = 8 + 128 = 136 .
$$

Rule: the eight zero modes plus four times the numbers of vectors in the shells 1 to 4. Continuing to $n_2 = 11$ with $r_3(5), \dots, r_3(11) = 24, 24, 0, 12, 30, 24, 24$:

$$
8 + 4\,(32 + 24 + 24 + 0 + 12 + 30 + 24 + 24) = 8 + 4\cdot170 = 688 .
$$

Rule: the sum $6 + 12 + 8 + 6 = 32$ of the first four shells plus the seven new shells. $N = 688$ is the largest closed shell whose highest level lies below the **bulk edge** $1.2922928$, the lowest level that is not on the brane band (the odd level at $k = 0$; parameters.json, particleNumbers.bulkEdge; a value at the cutoff $L = 3$, see the end of this section); $N = 136$ is the closed shell nearest to $688/4 = 172$ (Exercise 1 checks this). The record calls 688 $N_{large}$ and 136 $N_{mid}$ (parameters.json, particleNumbers.N_large and particleNumbers.N_mid, with the rule in particleNumbers.rule).

**The couplings.** The coupling $\lambda$ is a constant of the theory, the same at every slice. For each $N$ the record chooses two values so that the interaction is a moderate perturbation along the whole history (parameters.json, couplingCalibration). In the free ground states of that $N$ at all five slices it takes the largest value over $y$ of $\max\big(\tfrac{15}{16}|S|, \tfrac{1}{16}n\big)$, the size of the mean-field potentials per unit $\lambda$ (called the **strength**), and sets $\lambda_1 = 0.1/\text{strength}$ and $\lambda_2 = 0.3/\text{strength}$, rounded to four significant digits; then the first-order potentials stay below $0.1\,m$ and $0.3\,m$. For $N = 8$ the strength is $5.138804$, so $\lambda_1 = 0.1/5.138804 = 0.019460$, rounded $0.01946$, and $\lambda_2 = 0.05838$. For $N = 136$ and $688$ the strengths are $107.548$ and $541.713$, so $\lambda_1 = 0.0009298$ and $0.0001846$, $\lambda_2 = 0.002789$ and $0.0005538$. The strength of $N = 136$ grows from $5.226$ at the first slice to $107.548$ at the last, that of $N = 688$ from $5.226$ to $541.713$ (parameters.json, strengthPerLambdaAtSlices): along the history the brane-band orbitals spread toward the tip, where the factor $P = e^{-6Hy}/\mathrm{Vol}_7$ is large. A calibration at the first slice alone would make the late states strongly coupled; this is why the whole history is used. The calibration is made at the cutoff $L = 3$, and the strength grows with $L$ (the end of this section). The sign of $\lambda$ decides the kind of interaction: $\lambda > 0$ is repulsive, $\lambda < 0$ attractive. The run names use the tags `lam0`, `lamp1`, `lamm1`, `lamp2`, `lamm2` for $\lambda = 0, +\lambda_1, -\lambda_1, +\lambda_2, -\lambda_2$.

**The canonical matrix.** The solver computes a fixed list of states. **Ground states** ($T = 0$): three particle numbers $N = 8, 136, 688$, five couplings and five slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$, that is $3 \cdot 5 \cdot 5 = 75$ states. **Thermal states**: the same three $N$, the three couplings $0, \pm\lambda_1$, the five slices and three temperatures $T = 0.01, 0.02, 0.05$, that is $3\cdot3\cdot5\cdot3 = 135$ states. A state is named like `N136_lamp2_a20` ($N = 136$, $+\lambda_2$, $a_{4,0} = 2.0$; the last two digits are ten times the slice), and a thermal state carries in addition `_T10`, `_T20` or `_T50` (a thousand times the temperature).

**The numerical parameters** (parameters.json, numerics): $G = 900$ steps of the Runge-Kutta method on $[-L, 0]$, a root tolerance of $10^{-13}\,m$ for each level, a self-consistency tolerance of $10^{-11}\,m$ with at most 400 iterations, Anderson mixing with depth 6 and $\beta = 0.4$, the step $\delta = 0.002$ in $a_4$ for derivatives along the history, and levels closer than $10^{-9}\,m$ count as equal (one degenerate group).

**What the cutoff $L = 3$ changes (the choice is CHOSEN, its effect COMPUTED).** The regular tip and the value $L = 3$ are choices of the model, and the record measures what they change in the folder `Revision/kohn_sham/tip_convergence/`, summarised in sections 5 and 15 of the document `Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md`. It solves 29 recorded states, the 27 ground states with $N = 8, 136, 688$, $\lambda = 0, \pm\lambda_1$, $a_{4,0} = 0, 1, 2$ and two thermal states of $N = 136$, at $L = 3, 3.5, \dots, 6$ with the record's step $h = 1/300$, and every run again with the step $h/2$. A copy of the solver that reads $L$ from the environment reproduces the committed matrix byte for byte at $L = 3$, and the independent reference solver agrees at $L = 3$ and $L = 4$ (report `Revision/kohn_sham/tip_convergence/tip-convergence.json`, 7 of 7 checks PASS).

**How the study judges the limit $L \to \infty$.** The rules were fixed before the comparison (section 3 of the README of that folder). For each computed number $x$, for example $E_{KS}$, the study forms the **successive differences** $d = x(L + 0.5) - x(L)$ over the values of $L$, from 3 on, at which the self-consistent iteration converged, and the ratio $r$ of each difference to the one before it. If every difference from some $L$ on is no larger than the numerical noise of its two values (for each value the uncertainty measured with the step $h/2$, plus $10^{-11}$ relative), the number has converged within the noise, and its last value is its limit. If the last two ratios both lie between 0 and 0.5, the study takes the differences to go on shrinking like a geometric series, each one the fraction $r$ (the last ratio) of the one before; this is the **geometric-tail rule**, and the limit, which the record calls the extrapolated value and this chapter also the large-$L$ value, adds the differences still missing:

$$
x_\infty = x(L_{max}) + d_{last}\,(r + r^2 + r^3 + \dots) = x(L_{max}) + d_{last}\,\frac{r}{1 - r} .
$$

Rule: $L_{max}$ is the largest converged $L$ and $d_{last}$ the last difference, so the next differences would be $d_{last}r, d_{last}r^2, \dots$; the sum $s = r + r^2 + r^3 + \dots$ obeys $s = r + r\,s$ (take the factor $r$ out of every term after the first), so $s = r/(1 - r)$ for $0 < r < 1$. In every other case, and when fewer than three values of $L$ converged, the study takes no limit: the limit is not established. This rule follows the dependence on $L$; it is not the Richardson extrapolation of Chapter 2, which combines two values so that their leading error term cancels. What the study finds:

- The free results with $k \ne 0$ converge faster than exponentially, because an orbital with momentum $k$ is suppressed toward the tip like $\exp\big(-|k|(\kappa(-L) - \kappa(y))/H\big)$. The recorded $L = 3$ values are low by up to 1.4 per cent in $E_{KS}$ and 12 per cent in the integrated pressure along the hidden direction, $2\,\mathrm{Vol}_7\int e^{6Hy}p_8\,dy$ (the record's column `int_p8`, Section 15.16): for $N = 136$, $\lambda = 0$, $a_{4,0} = 2$ they are $12.44507$ against the extrapolated $12.62207$, and $8.47270$ against $9.63839$.
- The levels at $k = 0$ other than the zero mode approach $\pm m$ only slowly, like $(n\pi)^2/(2mL^2)$ (Section 15.3 derives this for the even levels from their exact formula; the record verifies the exact levels at every $L$ of the study, 84 levels, to $1.42 \times 10^{-10}\,m$). So the bulk edge $1.2922928$ that defines $N = 688$ is a value at $L = 3$: it is $1.0977$ at $L = 6$ and tends to $m$ as $L \to \infty$. From $L = 3.5$ on, the ground state of $N = 688$ at $a_{4,0} = 0$ occupies levels of the bulk at $k = 0$, its gap $0.0452$ closes, and its energy does not converge up to $L = 6$.
- The interacting results depend strongly on $L$. The proper density of the zero modes grows toward the tip like $e^{(6H - 2m)|y|} = e^{4|y|}$ (exact, and verified by the record; Figure 15e.6 shows the potential it makes). For $N = 8$ the record finds $E_{KS} = \mp9.868 \times 10^{-4}$ at $L = 3$ ($\lambda = \pm\lambda_1$, every slice) against $\mp3.0046 \times 10^{-3}$ at large $L$, extrapolated from $\lambda = -\lambda_1$ at $a_{4,0} = 2$, the only interacting $N = 8$ state solved up to $L = 6$ (the $\pm\lambda_1$ partners are negatives of each other to $1.1 \times 10^{-12}$ relative at every $L$ where both converge; the other interacting $N = 8$ states extrapolate to $\mp3.007 \times 10^{-3}$ from $L \le 4.5$, because their self-consistent iteration fails from $L = 5$): the recorded value is about one third of the large-$L$ value. For $N = 136$ at $a_{4,0} = 2$ the interaction shift $E_{KS}(\pm\lambda_1) - E_{KS}(0)$ is at large $L$ about 28 ($+\lambda_1$, value at $L = 5.5$) and 21 ($-\lambda_1$, extrapolated) times its value at $L = 3$.
- The self-consistent iteration fails at some larger $L$ for 13 of the 19 interacting states studied; this is a failure of the iteration, not a proof that no self-consistent state exists. For 7 of them the successive differences of $E_{KS}$ do not meet the geometric-tail rule of the study before the iteration fails, so their limit is not established; for the other 6 the values before the failure still end in a geometric tail.
- The calibration of the couplings is a statement at $L = 3$: the strength is the largest first-order mean-field potential per unit $\lambda$, and it grows with $L$ (for $N = 8$ it is the zero-mode potential at the tip, which grows like $e^{4L}$). The same rule applied at larger $L$ drives $\lambda_1$ to zero: at $L = 6$ it gives $1.2 \times 10^{-7}$ for $N = 8$ (falling like $e^{-4L}$ from $0.01946$ at $L = 3$), $1.2 \times 10^{-7}$ for $N = 136$ and $1.0 \times 10^{-11}$ for $N = 688$.

Not computed at $L \ne 3$: the couplings $\pm\lambda_2$, the slices $0.5$ and $1.5$, $T = 0.01$ and the other thermal states, the excited states and the adiabaticity measure; and nothing beyond $L = 6$. Every number printed by the notebooks of this chapter is a value at $L = 3$, and so is every number of the chapter except where this paragraph is cited.

### 15.3 Finding one level: shooting with the Pruefer angle

**The idea of shooting.** For a trial energy $\varepsilon$, start at the tip with values that satisfy the tip condition, $(a, b) = (1, 0)$, integrate the two first-order equations of Section 15.2 from $y = -L$ to $y = 0$ with a step rule (the Runge-Kutta rule RK4 of Chapter 2), and look at the end values. If the brane condition of the wanted parity holds there ($b(0) = 0$ or $a(0) = 0$), $\varepsilon$ is a level. If not, change $\varepsilon$ and shoot again. The start value 1 for $a$ is no restriction: the equations are linear in $(a, b)$, so any other start $(c, 0)$ gives $c$ times the same solution, and the solution is normalised at the end. Chapter 2 introduced this method for a quantum well. Two difficulties remain: how to find every level without missing one, and how to tell which level is which. The Pruefer angle solves both.

**The Pruefer angle.** Write the point $(a, b)$ in polar form, $a = r\cos\theta$, $b = r\sin\theta$, with the length $r = \sqrt{a^2 + b^2} > 0$ and the angle $\theta$, followed continuously along $y$ (it may grow beyond $2\pi$). We derive the equation for $\theta$, line by line.

$$
a b' - b a' = r\cos\theta\,(r'\sin\theta + r\cos\theta\,\theta') - r\sin\theta\,(r'\cos\theta - r\sin\theta\,\theta') = r^2\theta' .
$$

Rule: differentiate $a = r\cos\theta$ and $b = r\sin\theta$ with the product and chain rules; the terms with $r'$ cancel, and $\cos^2\theta + \sin^2\theta = 1$.

$$
a b' = \big(j(\varepsilon - v) - \kappa k\big)a^2 - M a b, \qquad b a' = M a b - \big(\kappa k + j(\varepsilon - v)\big)b^2 .
$$

Rule: multiply the second block equation by $a$ and the first by $b$.

$$
a b' - b a' = j(\varepsilon - v)(a^2 + b^2) - \kappa k\,(a^2 - b^2) - 2Mab .
$$

Rule: subtract; the terms with $j(\varepsilon - v)$ collect to $j(\varepsilon - v)(a^2 + b^2)$, the terms with $\kappa k$ to $-\kappa k a^2 + \kappa k b^2$, and the two terms $-Mab$ add.

$$
\theta' = j(\varepsilon - v) - \kappa k\cos2\theta - M\sin2\theta .
$$

Rule: divide by $r^2$ and use $a^2 + b^2 = r^2$, $a^2 - b^2 = r^2(\cos^2\theta - \sin^2\theta) = r^2\cos2\theta$ and $2ab = 2r^2\cos\theta\sin\theta = r^2\sin2\theta$ (the double-angle formulas). The angle obeys an equation of its own, without $r$. At the tip, $(a, b) = (1, 0)$ gives $\theta(-L) = 0$ for every $\varepsilon$.

**The phase function.** Define $\Phi(\varepsilon) = j\,\theta(0)$, $j$ times the angle at the brane. The brane conditions become conditions on $\Phi$: $b(0) = 0$ means $\sin\theta(0) = 0$, that is $\theta(0)$ is a whole multiple of $\pi$, so $\Phi = l\pi$ with a whole number $l$ (even parity); $a(0) = 0$ means $\cos\theta(0) = 0$, so $\Phi = \tfrac{\pi}{2} + l\pi$ (odd parity). (Multiplying by $j = \pm1$ maps the set of these values onto itself.) So every level is a solution of $\Phi(\varepsilon) = t_l$ for one of the **targets** $t_l = l\pi$ (even) or $t_l = \tfrac{\pi}{2} + l\pi$ (odd).

**$\Phi$ increases strictly.** We compute $u = \partial\theta/\partial\varepsilon$, line by line.

$$
u' = j + \big(2\kappa k\sin2\theta - 2M\cos2\theta\big)\,u, \qquad u(-L) = 0 .
$$

Rule: differentiate the angle equation with respect to $\varepsilon$ (chain rule: $\partial(\cos2\theta)/\partial\varepsilon = -2\sin2\theta\,u$ and $\partial(\sin2\theta)/\partial\varepsilon = 2\cos2\theta\,u$); $u(-L) = 0$ because $\theta(-L) = 0$ for every $\varepsilon$.

$$
(\ln r)' = \frac{a a' + b b'}{r^2} = M\cos2\theta - \kappa k\sin2\theta .
$$

Rule: $(\ln r)' = r'/r = (a a' + b b')/r^2$ (differentiate $r^2 = a^2 + b^2$); insert the block equations, where the terms with $j(\varepsilon - v)$ cancel: $aa' + bb' = M(a^2 - b^2) - 2\kappa k\,ab$; then the double-angle formulas.

$$
u' = j - 2(\ln r)'\,u .
$$

Rule: the bracket of the first line is $-2$ times the second line.

$$
(r^2u)' = 2rr'u + r^2u' = r^2\big(2(\ln r)'u + j - 2(\ln r)'u\big) = j\,r^2 .
$$

Rule: the product rule, $r' = r\,(\ln r)'$, and the previous line.

$$
r(0)^2\,u(0) = j\int_{-L}^{0}r^2\,dy, \qquad \frac{d\Phi}{d\varepsilon} = j\,u(0) = \frac{\int_{-L}^{0}r^2\,dy}{r(0)^2} > 0 .
$$

Rule: integrate from the tip to the brane, with $u(-L) = 0$; then multiply by $j$ and use $j^2 = 1$. The result is positive because $r^2 = a^2 + b^2 > 0$. So **$\Phi$ increases strictly with $\varepsilon$**, for both block types, any potentials and any slice. This formula is also the derivative that Newton's method needs, and the solver computes it at no extra cost while it integrates (its documentation in `Revision/kohn_sham/solver/README.md`, Method).

**$\Phi$ runs from $-\infty$ to $+\infty$.** On the interval the functions $|v|$, $\kappa k$ and $|M|$ are bounded, say by a number $C_0$ each. Then $j\theta' = (\varepsilon - v) - j\kappa k\cos2\theta - jM\sin2\theta$ lies between $\varepsilon - 3C_0$ and $\varepsilon + 3C_0$, and integrating over the length $L$ gives $(\varepsilon - 3C_0)L \le \Phi(\varepsilon) \le (\varepsilon + 3C_0)L$. So $\Phi(\varepsilon) \approx \varepsilon L$ for large $|\varepsilon|$, and it takes every real value.

**The oscillation theorem.** A continuous function that increases strictly from $-\infty$ to $+\infty$ takes every value exactly once. Hence each target $t_l$ is reached at exactly one energy: **every level has its own whole number $l$, its Pruefer label, and no level can be missed.** In a sector the levels are ordered by their labels. When the potentials change continuously (from one iteration of the self-consistent loop to the next, when the coupling is switched on, or from one slice to the next), a level moves continuously and keeps its label, because the target does not change. The label is therefore a name that follows a level everywhere. The particle levels of a sector are exactly the labels $l \ge l_{min}$, where $l_{min}$ is the first label whose level without interaction is positive; in the even sectors at $k = 0$, $l_{min} = 0$ is the zero mode, counted as a particle level by the convention of Section 15.2 (the solver checks this split in every sector up to $n_2 = 30$, check free_particle_branch_labels of `Revision/kohn_sham/reports/ks-rust-solver.json`).

**The test case: exact levels at $k = 0$.** With $k = 0$, $v = 0$ and a constant mass $M > 0$ the levels are known exactly (ks-theory.json, boundaryConditions.exactK0Spectra; check bc_exact_k0_spectra). Line by line:

$$
a'' = Ma' - j\varepsilon b' = Ma' - j\varepsilon(j\varepsilon a - Mb) = Ma' - \varepsilon^2 a + j\varepsilon M b .
$$

Rule: differentiate the first block equation (with $k = 0$, $v = 0$) and insert the second; $j^2 = 1$.

$$
a'' = Ma' - \varepsilon^2 a + M(Ma - a') = (M^2 - \varepsilon^2)\,a .
$$

Rule: the first block equation says $j\varepsilon b = Ma - a'$. The same two steps for $b$, line by line:

$$
b'' = j\varepsilon a' - Mb' = j\varepsilon(Ma - j\varepsilon b) - Mb' = j\varepsilon M a - \varepsilon^2 b - Mb' .
$$

Rule: differentiate the second block equation (with $k = 0$, $v = 0$) and insert the first; $j^2 = 1$.

$$
b'' = M(b' + Mb) - \varepsilon^2 b - Mb' = (M^2 - \varepsilon^2)\,b .
$$

Rule: the second block equation says $j\varepsilon a = b' + Mb$. For $\varepsilon \ne 0$ this relation gives $a$ from $b$, so an orbital that is not zero everywhere has a $b$ that is not zero everywhere; the cases $\varepsilon \ne 0$ are sorted by the sign of $M^2 - \varepsilon^2$. For $\varepsilon^2 > M^2$ put $p = \sqrt{\varepsilon^2 - M^2}$; then $b'' = -p^2b$, and the tip condition $b(-L) = 0$ leaves $b = B\sin\big(p(y + L)\big)$ with $B \ne 0$. Even parity, $b(0) = 0$: $\sin(pL) = 0$, so $p = n\pi/L$ and

$$
\varepsilon = \pm\sqrt{M^2 + (n\pi/L)^2}, \qquad n = 1, 2, \dots
$$

Odd parity, $a(0) = 0$: the second block equation gives $j\varepsilon a = b' + Mb$, so $a(0) = 0$ means $b'(0) + Mb(0) = 0$, that is $Bp\cos(pL) + MB\sin(pL) = 0$, or $\tan(pL) = -p/M$.

Inside the gap, $0 < \varepsilon^2 < M^2$, put $q = \sqrt{M^2 - \varepsilon^2} > 0$; then $b'' = q^2b$. The functions $\cosh x = (e^x + e^{-x})/2$ and $\sinh x = (e^x - e^{-x})/2$ are each the derivative of the other, so $\cosh\big(q(y + L)\big)$ and $\sinh\big(q(y + L)\big)$ solve $b'' = q^2b$, every solution is a combination of the two, and the tip condition $b(-L) = 0$ (where $\cosh 0 = 1$, $\sinh 0 = 0$) leaves $b = B\sinh\big(q(y + L)\big)$ with $B \ne 0$. Even parity needs $b(0) = B\sinh(qL) = 0$, impossible because $\sinh x > 0$ for $x > 0$. Odd parity needs $b'(0) + Mb(0) = B\big(q\cosh(qL) + M\sinh(qL)\big) = 0$, impossible because both terms in the bracket are positive. At the edge, $\varepsilon^2 = M^2$, the equation is $b'' = 0$ and the tip condition leaves $b = B(y + L)$; even parity needs $BL = 0$ and odd parity $b'(0) + Mb(0) = B(1 + ML) = 0$, both impossible for $B \ne 0$. So **no level lies in $0 < |\varepsilon| \le M$**: the only level inside the gap is the zero mode. Finally $\varepsilon = 0$: the equations become $a' = Ma$, $b' = -Mb$, so $b = 0$ (from $b(-L) = 0$) and $a = Ce^{My}$: the **zero mode**, which satisfies the even brane condition. Normalising, $\int_{-L}^{0}C^2e^{2My}dy = C^2(1 - e^{-2ML})/(2M) = 1$ gives $C = \sqrt{2M/(1 - e^{-2ML})}$. For $M = 1$, $L = 3$: the first even levels are $\pm\sqrt{1 + (\pi/3)^2} = \pm1.4479719$, and the first odd level is $\pm1.2922928$, the bulk edge of Section 15.2. Notebook 15e reproduces all of them by shooting (Out [6]).

**How these levels depend on the cutoff.** Every level other than the zero mode depends on $L$. For the even levels, line by line:

$$
\sqrt{M^2 + (n\pi/L)^2} - M = \frac{(n\pi/L)^2}{\sqrt{M^2 + (n\pi/L)^2} + M} \approx \frac{(n\pi)^2}{2ML^2} \quad (L \text{ large}) .
$$

Rule: multiply and divide by the sum $\sqrt{M^2 + (n\pi/L)^2} + M$ and use $(A - B)(A + B) = A^2 - B^2$; for large $L$ the denominator tends to $2M$. So the levels at $k = 0$ approach $\pm M$ only like $1/L^2$, slowly; the record finds the same $1/L^2$ approach for the odd levels (the bulk edge is $1.2923$ at $L = 3$ and $1.0977$ at $L = 6$; Section 15.2, the paragraph on the cutoff). The zero mode stays at $\varepsilon = 0$ for every $L$; only its normalisation $C$ depends on $L$.

**Newton's method inside a bracket.** To solve $\Phi(\varepsilon) = t_l$ the solver uses Newton's method, $\varepsilon \to \varepsilon - (\Phi(\varepsilon) - t_l)/\Phi'(\varepsilon)$, with the derivative from the formula above. Newton's method converges very fast near the root but can jump far away from a poor guess, so it is **safeguarded**: from a guess the solver first walks with doubling steps (up if $\Phi < t_l$, down otherwise) until $\Phi - t_l$ changes sign; the last two points form a **bracket** $[lo, hi]$ that contains the root, because $\Phi$ is continuous. Then it takes Newton steps, and replaces a Newton step by **bisection** (the midpoint of the bracket) whenever the Newton step would leave the bracket or the previous step did not halve $|\Phi - t_l|$; after each step the bracket shrinks to the side where the sign changes. It stops when the bracket is shorter than the tolerance $10^{-13}\,m$ or when a Newton step moved the energy by less than that (Newton's method approaches a root from one side, so the bracket itself need not shrink). The levels are therefore found to about $10^{-13}\,m$ for a given grid.

**The grid, RK4 and the order 4.** The solver makes $G = 900$ steps of length $h = L/G = 1/300$. One RK4 step needs the coefficients $M$, $v$ and $\kappa$ at the start, the middle and the end of the step, so the potentials are stored on the **fine grid** of the $2G + 1 = 1801$ step ends and midpoints, $y_i = -L + i\,h/2$. The error of RK4 falls like $h^4$ (Chapter 2): halving the step divides it by $2^4 = 16$. The record measured exactly this ratio, 16.00, between its canonical run ($G = 900$) and a refined run ($G = 1800$) (check refined_free_spectra_convergence_order of `Revision/kohn_sham/reports/ks-rust-determinism.json`).

**The orbital between the step ends: cubic Hermite interpolation.** RK4 gives $(a, b)$ at the step ends only, but the densities are needed on the whole fine grid. Each midpoint value is filled in from the values $u_0, u_1$ and the derivatives $u_0', u_1'$ at the two ends of a step (the derivatives come from the block equation itself). Take a cubic polynomial and measure from the midpoint, $p(s) = A + Bs + Cs^2 + Ds^3$, $-h/2 \le s \le h/2$, so that the wanted value is $p(0) = A$. Line by line:

$$
u_0 + u_1 = p(-h/2) + p(h/2) = 2A + \tfrac{h^2}{2}C .
$$

Rule: in the sum of the two end values the odd powers of $s$ cancel and the even powers double.

$$
u_1' - u_0' = p'(h/2) - p'(-h/2) = 2Ch .
$$

Rule: $p'(s) = B + 2Cs + 3Ds^2$; in the difference only the term $2Cs$ survives.

$$
A = \frac{u_0 + u_1}{2} - \frac{h^2}{4}C = \frac{u_0 + u_1}{2} - \frac{h^2}{4}\cdot\frac{u_1' - u_0'}{2h} = \frac{u_0 + u_1}{2} + \frac{h}{8}\,(u_0' - u_1') .
$$

Rule: solve the first line for $A$ and insert $C$ from the second. The formula is exact for every cubic polynomial, so its error is of the order $h^4$, like RK4 itself.

**Normalisation with Simpson's rule.** The integral $\int_{-L}^{0}(a^2 + b^2)\,dy$ is computed with Simpson's rule on the fine grid: the weights are $\tfrac{h}{6}$ times $1, 4, 2, 4, \dots, 2, 4, 1$ (Simpson's rule of Chapter 2 with the spacing $h/2$, whose weights are $\tfrac{h/2}{3}$ times the same numbers). Its error is also of the order $h^4$. The orbital is then divided by the square root of the integral.

**A detail that matters for Newton's method.** For the derivative $d\Phi/d\varepsilon = \int r^2dy/r(0)^2$ the solver integrates $r^2$ with the simpler **trapezoid rule** on the step ends while it shoots ($\tfrac{h}{2}(r_i^2 + r_{i+1}^2)$ per step). This derivative only steers Newton's method; an error in it changes how fast the root is found, not where it is.

### 15.4 From one level to the whole gas

**Label sets.** For a state of the gas the solver chooses the sectors and labels it will solve, its **label set**. It takes the shells $n_2 = 0, 1, 2, \dots$ in turn, with all four sectors (two block types, two parities) of each shell, fills the free levels found so far from the lowest upward, and stops adding shells when the lowest level of a new shell lies more than a margin above the lowest empty level (the LUMO) of that filling (in the canonical runs the margin is $0.25\,m$ plus twice the target size $0.1\,m$ or $0.3\,m$ of the coupling's first-order potential); in the occupied shells and the next one it solves three particle labels per sector, elsewhere the lowest only (`Revision/kohn_sham/solver/src/scf.rs`, the function `specs_t0`). The check ground_window_complete of the solver's report confirms for all 75 ground states that the lowest level outside the label set lies above the LUMO of the converged state, so no level that matters was left out.

**The brane band.** For $k > 0$ the lowest even level of block type $j = +1$ (label 0) grows out of the zero mode: it is bound to the brane, and its energy grows with $k$. This is the **brane band**. Its slope at $k = 0$ is known exactly (ks-theory.json, checksNumeric; check brane_band_slope):

$$
\frac{d\varepsilon}{dk}\Big|_{k = 0} = c\,e^{-a_{4,0}}, \qquad c = \frac{2M}{2M - H}\cdot\frac{1 - e^{-(2M - H)L}}{1 - e^{-2ML}} .
$$

For $M = H = 1$ and $L = 3$, line by line:

$$
c = \frac{2}{1}\cdot\frac{1 - e^{-3}}{1 - e^{-6}} = \frac{2\,(1 - e^{-3})}{(1 - e^{-3})(1 + e^{-3})} = \frac{2}{1 + e^{-3}} = 1.9051482536 .
$$

Rule: $2M - H = 1$; then $1 - e^{-6} = (1 - e^{-3})(1 + e^{-3})$ (the difference of two squares), and the common factor cancels; $e^{-3} = 0.0497871$.

**The two block types and the sea.** Without interaction the two block types mirror each other: $h_{-1} = -h_{+1}$ as operators with the same boundary conditions (check block_type_relation), so every orbital of $j = +1$ is also an orbital of $j = -1$, with the same $k$ and parity and the opposite level. The band of $j = -1$ therefore lies at $-\varepsilon_{band}(k)$, below zero: it belongs to the sea, and the positive band levels are those of $j = +1$ only, each $4r_3(n_2)$-fold. At $k = 0$ the zero mode ($\varepsilon = 0 = -0$) belongs to both types, so the zero-mode level is $4 + 4 = 8$-fold.

**The rescaling identity and the redshift.** The slice enters the block equation only through $\kappa k = e^{-Hy}(k\,e^{-a_{4,0}})$. Therefore (ks-theory.json, rescalingIdentity; check rescaling_identity), without interaction,

$$
\varepsilon(k;\ a_{4,0}) = \varepsilon(k\,e^{-a_{4,0}};\ 0)
$$

for every level: a later slice is the first slice with every 3-momentum **redshifted** by $e^{-a_{4,0}}$. With interaction the same holds for the whole self-consistent state when the extra-time volume is changed too (Chapter 14); the solver solved each partner problem independently and found the same levels to $1.5 \times 10^{-13}\,m$ (check rescaling_identity_between_slices of `Revision/kohn_sham/reports/ks-rust-solver.json`). Three consequences:

- The levels at $k = 0$ (the zero modes and the bulk levels at $k = 0$) do not depend on the slice at all.
- The brane band increases with $k$ (the solver checks this on $0 \le k \le 4$, check free_rescaling_relation_and_band_monotone). A level of the band at a fixed shell therefore decreases strictly along the history, because its redshifted momentum $k\,e^{-a_{4,0}}$ decreases.
- Every energy of the free gas that comes from band levels falls along the history.

**The gap of $N = 8$, exactly.** For $N = 8$ the highest occupied level is the zero mode ($\varepsilon = 0$) and the lowest empty one is the band level of the first shell, $k = \Delta k = 0.25$. So the Kohn-Sham gap is

$$
\Delta_{KS}(a_{4,0}) = \varepsilon_{band}(0.25\,e^{-a_{4,0}};\ 0) .
$$

The record gives $0.4307337$, $0.1703493$ and $0.0641594$ at $a_{4,0} = 0, 1, 2$ (Notebook 15a, Out [7]). The ratios to the first value are $0.39549$ and $0.14895$, larger than $e^{-1} = 0.36788$ and $e^{-2} = 0.13534$: the gap shrinks somewhat more slowly than $e^{-a_{4,0}}$. The reason is visible in Figure 15e.4: the band bends below its tangent line $c\,k$, so $\varepsilon_{band}(k)/k$ decreases with $k$; a redshifted momentum lies where the ratio is larger, closer to $c$. Exercise 2 makes this precise.

**Aufbau and closed shells.** At $T = 0$ the solver fills the levels from the lowest upward, with exact groups of equal levels (levels within $10^{-9}\,m$ count as equal); a group that would be filled only in part is flagged as an **open shell**. The particle numbers of Section 15.2 were chosen as closed shells, and the check ground_closed_shell confirms for all 75 ground states that no group is partly filled.

### 15.5 Self-consistency, the energy, and the first excited state

**The loop.** The unknowns of the self-consistent problem are the two functions $M(y) - m$ and $v(y)$ on the 1801 points of the fine grid, collected in one long list $x$ of $2 \times 1801$ numbers (the solver keeps a third function for a variant with the exact Fock exchange, zero in the canonical functional). One **iteration**: (1) from the input $x$, solve every level of the label set (Section 15.3); (2) fill them (aufbau at $T = 0$, Fermi-Dirac at $T > 0$); (3) build the densities $n$ and $S$ and from them the output potentials $x_{out} = \big(\tfrac{15}{16}\lambda S,\ -\tfrac{1}{16}\lambda n\big)$; (4) the **residual** is $r = x_{out} - x$, and its size is its largest entry in absolute value. The loop stops when this size is at most $10^{-11}\,m$. Without interaction $x_{out} = 0 = x$ after one iteration.

**Mixing.** Taking $x_{out}$ as the next input (plain iteration) can oscillate forever (charge sloshing, Chapter 13). **Linear mixing** takes $x + \beta r$ with $0 < \beta < 1$. **Anderson mixing** remembers the last few inputs $x_1, \dots, x_p$ and their residuals $r_1, \dots, r_p$ ($p \le 6$ in the solver), finds numbers $c_1, \dots, c_p$ with $\sum c_i = 1$ that make the combined residual $\sum c_ir_i$ as small as possible, and takes

$$
x_{next} = \sum_i c_i\,(x_i + \beta\,r_i), \qquad \beta = 0.4 .
$$

**The weights, line by line.** We minimise $F(c) = |\sum_i c_ir_i|^2 = \sum_{i,k}c_ic_k\,G_{ik}$, with the **Gram matrix** $G_{ik} = r_i\cdot r_k$ (the dot product of two lists, the sum of the products of their entries), under the condition $\sum_i c_i = 1$. With a Lagrange multiplier $\nu$ (Chapter 13) we make $F - 2\nu(\sum_i c_i - 1)$ stationary:

$$
\frac{\partial}{\partial c_i}\Big[\sum_{k,l}c_kc_lG_{kl} - 2\nu\Big(\sum_k c_k - 1\Big)\Big] = 2\sum_k G_{ik}c_k - 2\nu = 0 .
$$

Rule: each $c_i$ appears in the double sum once as $c_k$ and once as $c_l$, and $G$ is symmetric ($r_i\cdot r_k = r_k\cdot r_i$), so the two terms are equal.

$$
\begin{pmatrix} G & \mathbf 1 \\ \mathbf 1^T & 0 \end{pmatrix}\begin{pmatrix} c \\ -\nu \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} .
$$

Rule: divide by 2, move $\nu$ to the left as the last unknown (with the sign it carries), and add the condition $\sum_k c_k = 1$ as the last row; $\mathbf 1$ is the column of $p$ ones. This is a small linear system of $p + 1$ equations. The solver adds $10^{-12}$ times the largest diagonal entry of $G$ to the diagonal (which keeps the system solvable when two residuals are nearly equal), drops the oldest pair when it still cannot be solved, and forgets the whole history when a residual grows to more than ten times the smallest seen so far (`Revision/kohn_sham/solver/src/scf.rs`). Notebook 15e writes the same rule in Python (without the fallback for an unsolvable system, which its runs never need), and Figure 15e.5 shows how much faster it converges than linear mixing. Exercise 4 works the weights out for $p = 2$.

**The energy: why the interaction energy is subtracted.** The energy of the interacting gas is its kinetic and mass energy plus the interaction energy. Each level $\varepsilon$ already contains the potential energy of its orbital in the mean field, so the sum $\sum gf\varepsilon$ counts the interaction twice. Line by line, with $\langle\cdot\rangle$ meaning $2\,\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}(\cdot)\,dy$ (the amount in the whole doubled box):

$$
\sum g f\,\varepsilon = E_{kin} + \big\langle (M - m)S + v\,n\big\rangle .
$$

Rule: the level is the expectation value of the block Hamiltonian; the terms of $h$ with $M - m$ and $v$ give, summed with $wgfP$ over the occupied orbitals, the densities $S$ and $n$ times the potentials (the definitions of $S$ and $n$ in Section 15.2); everything else ($-i\sigma_1d/dy$, $m\sigma_2$, $\kappa k\sigma_3$) is collected in $E_{kin}$.

$$
(M - m)S + v\,n = S\frac{\partial e_{int}}{\partial S} + n\frac{\partial e_{int}}{\partial n} = \lambda\Big(\tfrac{15}{16}S^2 - \tfrac{1}{16}n^2\Big) = 2\,e_{int} .
$$

Rule: the potentials are the derivatives of $e_{int}$ (Section 15.2), and $e_{int}$ is a sum of squares, homogeneous of degree 2 (Euler's rule: $S\,\partial_Se + n\,\partial_ne = 2e$ for such a function); compare the coefficients $\tfrac{15}{16} = 2\cdot\tfrac{15}{32}$ and $\tfrac{1}{16} = 2\cdot\tfrac{1}{32}$.

$$
E = E_{kin} + \langle e_{int}\rangle = \sum gf\varepsilon - 2\langle e_{int}\rangle + \langle e_{int}\rangle = \sum gf\varepsilon - 2\,\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}e_{int}\,dy .
$$

Rule: insert the first two lines. This is $E_{KS}$ of Section 15.2 (ks-theory.json, thermodynamics.energy; check ks_onshell_lagrangian for the same degree-2 identity). The solver also computes the **variational form**, $\sum gf\varepsilon - \langle (M_{in} - m)S_{out} + v_{in}n_{out}\rangle + \langle e_{int}(S_{out}, n_{out})\rangle$, with the input potentials and output densities of the last iteration; the two agree to $2.2 \times 10^{-13}$ relative in all 75 ground states (check ground_energy_two_forms).

**An exact symmetry of the zero-mode state.** For $N = 8$ the eight occupied orbitals are the zero modes at $k = 0$. We show that changing the sign of $\lambda$ changes the sign of the energy, $E_{KS}(-\lambda) = -E_{KS}(\lambda)$. Line by line:

- At $k = 0$ the block equations of type $j$ are $a' = Ma - j(\varepsilon - v)b$ and $b' = j(\varepsilon - v)a - Mb$. Rule: Section 15.2 with $k = 0$.
- Put $\tilde a = a$, $\tilde b = -b$, $\tilde\varepsilon = -\varepsilon$, $\tilde v = -v$ and keep $M$ and $j$. Then $\tilde\varepsilon - \tilde v = -(\varepsilon - v)$, and $\tilde a' = M\tilde a - j(\tilde\varepsilon - \tilde v)\tilde b$, $\tilde b' = j(\tilde\varepsilon - \tilde v)\tilde a - M\tilde b$. Rule: in each equation the two sign changes ($b \to -b$ and $\varepsilon - v \to -(\varepsilon - v)$) cancel.
- So $(a, -b)$ is an orbital of the problem with $(M, -v)$ at the level $-\varepsilon$, with the same boundary conditions ($b = 0$ stays $b = 0$) and the same label (the angle $\theta$ becomes $-\theta$, so $\Phi \to -\Phi$, and the zero-mode label 0 stays 0). Rule: the previous line and the definition of the label.
- Its density $a^2 + b^2$ is unchanged and its scalar density $2jab$ changes sign: $n \to n$, $S \to -S$. Rule: the definitions of Section 15.2.
- With $-\lambda$ the potentials made by these densities are $\tfrac{15}{16}(-\lambda)(-S) = M - m$ and $-\tfrac{1}{16}(-\lambda)n = -v$: exactly the potentials assumed. So the mapped orbitals form a self-consistent state of $-\lambda$. Rule: the formulas of $M$ and $v$.
- Its energy: every level changes sign, so $\sum gf\varepsilon$ does; $e_{int} = \lambda(\tfrac{15}{32}S^2 - \tfrac{1}{32}n^2)$ changes sign with $\lambda$ while $S^2$ and $n^2$ stay. Hence $E_{KS}(-\lambda) = -E_{KS}(\lambda)$. Rule: the energy formula above.

This is PROVED for the mapped state; that the loop started from the free state finds exactly this state is COMPUTED (Notebook 15e finds $|E(+\lambda) + E(-\lambda)| = 0$ exactly, Out [13], and the record lists $E_{KS} = \mp9.8684262\times10^{-4}$ for $\pm\lambda_1$). These are values at the cutoff $L = 3$; the record's study of larger $L$ finds the partners negatives of each other at every $L$ where both converge, and the energy about three times larger at large $L$ (Section 15.2, the paragraph on the cutoff). The symmetry is special to the zero modes: for larger $N$ the band orbitals have $k \ne 0$, the momentum term spoils the map, and repulsion raises the energy while attraction lowers it.

**The first excited state: Delta-SCF.** Chapter 13 defined the Kohn-Sham gap $\Delta_{KS} = \varepsilon_{LUMO} - \varepsilon_{HOMO}$ and the Delta-SCF energy $\Delta_{SCF} = E_1 - E_0$, the difference of two self-consistent energies, the second with one particle moved from the highest occupied level to the lowest empty one. The solver uses an **ensemble** form: it removes one particle uniformly from the whole highest occupied group of equal levels and adds it uniformly to the whole lowest empty group, so that every orbital of a group keeps the same occupation and the block and direction symmetry of the reduction is kept (parameters.json, conventions.deltaScf). Without interaction the levels do not depend on the occupations, so $\Delta_{SCF} = \Delta_{KS}$ exactly (Janak's theorem of Chapter 13 with constant levels); the solver checks this in all 15 free states (check excited_delta_scf_free_equals_gap, largest difference $2.0 \times 10^{-11}\,m$). With interaction the orbitals relax and the two differ by the **orbital relaxation** $\Delta_{SCF} - \Delta_{KS}$; for example for `N8_lamp2_a00` the record has $\Delta_{KS} = 0.4312996$ and $\Delta_{SCF} = 0.4312929$ (`Revision/kohn_sham/results/excited/summary.csv`).

### 15.6 Example: the solver's method by hand (Notebook 15e)

Notebook 15e writes the method of Sections 15.3 to 15.5 in plain Python, exactly as the Rust solver does it (`Revision/kohn_sham/solver/src/shoot.rs` and `scf.rs`), and reproduces numbers of the record: the grid and Simpson's rule; one shooting integration with the Pruefer angle; the phase function and the levels it labels (Figure 15e.1); Newton's method inside a bracket, the exact levels at $k = 0$ and the solver's own levels; the orbitals with Hermite midpoints (Figure 15e.2); the order 4 of RK4 (Figure 15e.3); the brane band, its slope and the rescaling identity (Figure 15e.4); the self-consistent loop with Anderson mixing for $N = 8$, compared with linear mixing (Figure 15e.5); the four couplings and the symmetry $E(-\lambda) = -E(\lambda)$; and the self-consistent potentials (Figure 15e.6). It needs no Rust, runs in less than half a minute, and ends with ALL 18 CHECKS PASSED (notebook 15e).

What to look for: in Figure 15e.1 the steadily rising curve and the places where it crosses the horizontal lines (each crossing is one level, and none can be skipped); in Figure 15e.3 the straight lines of slope 4; in Figure 15e.4 the three band curves that are copies of each other with the momentum axis stretched; in Figure 15e.5 the blue dots, which fall on average about tenfold per iteration, and the black crosses of the Rust solver on top of them.

<!-- NOTEBOOK 15e -->

### 15.9 Line-by-line walk-through of Notebook 15e

The notebook has 15 code cells, In [1] to In [15]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted, then explained. Docstrings (the texts in triple quotes under a `def` line, which say what a function does) and some comment lines are left out of the quotations, and long caption strings in calls of `save_figure` are shortened: the quotation shows the first line of the call and the first line of the caption, and then a line `...)` that stands for the rest of the caption and the closing parenthesis; the complete cells are printed in Section 15.8. Every code cell is preceded in the notebook by a text cell that says what it does.

**In [1], the set-up cell.** Every line that starts with `#` is a **comment**, which Python skips. The first part of the cell, down to the lines of `-` and `=` signs, is the complete run instructions of Section 15.7 again, as comments, so that the notebook file carries its own instructions. The code starts after the heading THE SET-UP; it computes no physics and is the same in every notebook of the book, except for the line that names the notebook (the notebooks that run a Rust program add two imports and one function, explained in Section 15.14). The other walk-throughs of this chapter refer back to this paragraph.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module** (a part of Python or of a package) so that the code can use it. `json`, `os`, `textwrap` and `pathlib` come with Python. `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or a folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

These lines load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python code), which show a picture file below a cell.

```python
NOTEBOOK_ID = "15e"  # this notebook: chapter 15, example e
```

A **variable** is a name for a value; this line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"15e"`. The figure files are named after it.

```python
def find_repository_root():
    here = Path.cwd().resolve()  # the folder in which this notebook runs
    for folder in [here, *here.parents]:  # this folder, its parent, its grandparent ...
        if (folder / "Revision" / "textbook" / "requirements.txt").is_file():
            return folder
    raise FileNotFoundError(
        "The repository folder was not found: open this notebook inside the folder "
        "Revision/textbook/notebooks of the repository Dirac_claude")
```

`def` defines a **function**: a named piece of code that runs when it is called. `Path.cwd()` is the folder in which Jupyter runs the notebook (the folder that holds it), and `.resolve()` writes it as a complete address. `here.parents` lists the folders above it; `[here, *here.parents]` is the list that starts with `here` and continues with them (the star unpacks one list into another). The `for` loop visits these folders one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that contains the file `Revision/textbook/requirements.txt` (the list of the book's packages) is the repository, and `return` hands it back. If no folder qualifies, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
REPO = find_repository_root()
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first line calls the function and names its result `REPO`. It is never printed, because it differs from computer to computer, while the printed output of a notebook must not. The second line chooses where files are written. `os.environ` holds the **environment variables** of the program (named texts that it receives from the computer); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and the default `str(REPO)` (the repository folder as a string) otherwise. When you run the notebook the variable is not set, so the files go into the repository; the book's checking tool sets it to a scratch folder, so that a check never changes a file that git tracks. (Notebook 15e writes nothing else. The notebooks 15a, 15b and 15d, which run the Rust solver, also write the solver's raw output into the folders `Revision/kohn_sham/solver/target/textbook_15a`, `textbook_15b` and `textbook_15d` next to it, about 5.9 MB, 0.9 MB and 0.6 MB; git ignores these folders, and they are written during a check too.)

```python
def repository_file(relative):
    return REPO / relative


def output_file(relative):
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

Two small functions. `repository_file("Revision/...")` gives the full path of a repository file, for reading a Revision record. `output_file("Revision/...")` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the folder that will hold it, together with any missing folder above it, and does nothing if the folder exists.

```python
def say(text):
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters, the width of a page of the book; `textwrap.fill` breaks the text at blanks and starts every line after the first with four blanks. This is why some printed lines below continue on an indented second line.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

matplotlib reads personal settings from a file on your computer if you have one; `matplotlib.rcdefaults()` returns to the built-in settings, so that the figures are the same on every computer. `plt.rcParams.update({...})` then sets four settings for every figure: the size (7.0 by 4.2 inches), the size of the letters (10 points) and a faint grid of lines behind the curves (`grid.alpha` 0.3 means 30 per cent opaque). The braces make a **dictionary**: pairs of a key and a value, written `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/15e.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes the captions file with the empty dictionary `{}` and a line end; `encoding="utf-8"` and `newline="\n"` make the file the same bytes on every operating system.

```python
def save_figure(fig, name, caption):
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
    fig.savefig(output_file(relative), dpi=150, bbox_inches="tight",
                metadata={"Software": None})
    plt.close(fig)  # forget the figure, so that Jupyter does not draw it a second time
    CAPTIONS[file_name] = caption
    output_file(CAPTION_FILE).write_text(
        json.dumps(CAPTIONS, indent=1, sort_keys=True) + "\n", encoding="utf-8",
        newline="\n")
    display(Image(filename=str(output_file(relative))),
            metadata={"textbook_figure": file_name})  # the saved picture itself
    say(f"Figure {NOTEBOOK_ID}.{number} saved as {relative}")
```

`save_figure` is called once for every figure. `setdefault(name, default)` returns the number already given to this figure name, or gives it the next number (one more than the number of figures so far) and returns that; so the figures are numbered 1, 2, 3, ... in the order in which they are first saved. The file name is, for example, `15e_1_phase_function.png`. `fig.savefig` writes the picture: `dpi=150` is the resolution (150 dots per inch), `bbox_inches="tight"` cuts away the empty margin, and `metadata={"Software": None}` stores no program name in the file, so that every run writes exactly the same bytes. `plt.close(fig)` forgets the figure (otherwise Jupyter would draw it a second time). The caption is stored in `CAPTIONS`, and the whole dictionary is written again to the captions file (`json.dumps` turns it into text, `indent=1` puts one entry per line, `sort_keys=True` sorts them). `display(Image(...))` shows the saved picture below the cell, and the last line prints, for example, Figure 15e.1 saved as Revision/textbook/figures/15e_1_phase_function.png.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")
```

`PASSED` is an empty **list** (an ordered collection, in square brackets). `check` is the function behind every check: if the statement `condition` is false (`False`), `raise AssertionError(...)` stops the notebook with an error that names the check; if it is true, the name is appended to `PASSED` and the line PASS name is printed, followed by a line naming the Revision record and its check when the argument `record` is given. (Python's own `assert` statement is not used, because Python started with the option that optimises the code skips it.)

```python
def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a line that starts with RESULT; `(f" {unit}" if unit else "")` adds the unit when one is given. `all_checks_passed` prints the last line of the notebook; `len(PASSED)` is the number of checks that passed. The last statement prints the one output line of In [1], Set-up of notebook 15e complete.

**In [2], the grid.**

```python
import csv  # reads the tables (CSV files) of the Revision record
import math  # exp, sqrt, atan2, pi for single numbers

import numpy as np  # arrays of numbers
```

`csv` reads tables stored as comma-separated text, `math` holds the mathematical functions for single numbers, and numpy (under the short name `np`) works with **arrays**, lists of numbers on which arithmetic acts entry by entry.

```python
H, MASS, L = 1.0, 1.0, 3.0  # the units H = m = 1 and the tip cutoff L = 3
DK = 0.25  # the spacing of the 3-momenta
VOL7 = (2.0 * math.pi / DK) ** 3  # proper 7-volume per unit e^{6Hy} (v_t = 1)
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
```

The first line gives three names at once: $H = 1$, $m = 1$ (called `MASS`, because the letter m is used for other things below) and $L = 3$. `DK` is $\Delta k = 0.25$. `VOL7` is $\mathrm{Vol}_7 = (2\pi/\Delta k)^3 = 15875.2137$ (Section 15.2); `**` is the power. `PALETTE` is a list of eight colours, written as hexadecimal colour codes.

```python
def make_grid(steps):
    points = 2 * steps + 1  # step ends and step midpoints
    y = [-L * ((points - 1 - f) / (points - 1)) for f in range(points)]
    half = 0.5 * L / steps  # the distance between two fine points
    weights = [(4.0 if f % 2 == 1 else 2.0) * half / 3.0 for f in range(points)]
    weights[0] = weights[-1] = half / 3.0  # Simpson: 1, 4, 2, 4, ..., 4, 1 (x h/6)
    return {"steps": steps, "h": L / steps, "points": points, "y": y,
            "ew": [math.exp(-H * v) for v in y], "e6": [math.exp(6 * H * v) for v in y],
            "simpson": np.array(weights)}
```

`make_grid` builds the solver's grid for a given number of RK4 steps. The fine grid has `points` $= 2G + 1$ points (the step ends and the step midpoints). The second line is a **list comprehension** (a list built by a `for` inside square brackets): for $f = 0, 1, \dots, 2G$ it computes $y_f = -L\,(2G - f)/(2G)$, which is $-L$ for $f = 0$ and $0$ for $f = 2G$; this is the formula $y_f = -L + f\,h/2$ of Section 15.3 written so that the last point is exactly 0. `half` is the spacing $h/2$. The weights of Simpson's rule with spacing $h/2$ are $\tfrac{h/2}{3}$ times 4 at the odd points (`f % 2 == 1`: the remainder of $f$ divided by 2 is 1), 2 at the inner even points and 1 at the two ends; the next line sets the two ends (`weights[-1]` is the last entry). The function returns a dictionary with the number of steps, the step $h = L/G$, the number of points, the coordinates, the factors $e^{-Hy}$ (for $\kappa$; key `"ew"`) and $e^{6Hy}$ (the proper volume factor; key `"e6"`) at every fine point, and the Simpson weights as an array.

```python
GRID = make_grid(900)  # the canonical grid of the solver
Y = np.array(GRID["y"])
E6 = np.array(GRID["e6"])
simpson_test = float(np.sum(GRID["simpson"] * np.exp(Y)))
say(f"fine grid: {GRID['points']} points, step h = {GRID['h']:.6f}")
report("Simpson integral of e^y from -3 to 0", f"{simpson_test:.15f}")
check(abs(simpson_test - (1.0 - math.exp(-3.0))) < 1e-13,
      "Simpson's rule on the fine grid integrates e^y exactly to 1e-13")
```

`GRID` is the canonical grid ($G = 900$); `Y` and `E6` are its coordinates and volume factors as arrays. `simpson_test` is Simpson's rule applied to $e^y$: the sum of weight times value over the 1801 points (`np.sum` adds the entries of an array; `float` turns the result into an ordinary number). The exact integral is $\int_{-3}^{0}e^y\,dy = 1 - e^{-3} = 0.950212931632136$. The format `:.6f` prints six digits after the point, `:.15f` fifteen. Out [2] prints 1801 points, the step $0.003333$ and the integral $0.950212931632177$, which differs from the exact value by $4 \times 10^{-14}$, so the check passes.

**In [3], one shooting integration.**

```python
def rhs(m_y, kk, je, a, b):
    return m_y * a - (kk + je) * b, (je - kk) * a - m_y * b
```

`rhs` (right-hand side) returns the pair $(a', b')$ of the block equation for given values of $M$ (`m_y`), $\kappa k$ (`kk`), $j(\varepsilon - v)$ (`je`), $a$ and $b$: $a' = Ma - (\kappa k + j(\varepsilon - v))b$ and $b' = (j(\varepsilon - v) - \kappa k)a - Mb$, exactly Section 15.2.

```python
def shoot(eps, k, j, a4, mass, pot, grid=GRID, store=False):
    h = grid["h"]
    kk = k * math.exp(-a4)  # k e^{-a4,0}; kappa k = kk e^{-Hy}
    coef = [(mass[f], kk * grid["ew"][f], j * (eps - pot[f]))
            for f in range(grid["points"])]
```

`shoot` integrates from the tip to the brane for the trial energy `eps`, the momentum `k`, the block type `j`, the slice `a4` and the potentials `mass` ($M$) and `pot` ($v$), given as lists on the fine grid. The arguments `grid=GRID` and `store=False` have **default values**, used when the caller does not give them. `kk` is $k\,e^{-a_{4,0}}$, so that $\kappa k$ at a point is `kk` times $e^{-Hy}$. `coef` is a list with one triple $(M, \kappa k, j(\varepsilon - v))$ per fine point, computed once before the integration.

```python
    a, b = 1.0, 0.0  # the tip condition b(-L) = 0
    theta, raw = 0.0, 0.0  # the followed angle and the last angle from atan2
    area, r2_prev = 0.0, 1.0  # integral of r^2 (trapezoid) and r^2 at the last node
    nodes = [(a, b)] if store else None
```

The start values: $(a, b) = (1, 0)$ at the tip (the tip condition), the followed angle $\theta = 0$ and the last raw angle 0, the integral of $r^2$ so far 0, and $r^2 = 1$ at the tip. If `store` is true, the list `nodes` keeps the values at the step ends, starting with the tip; otherwise it is `None` (Python's word for "nothing").

```python
    for i in range(grid["steps"]):
        c0, c1, c2 = coef[2 * i], coef[2 * i + 1], coef[2 * i + 2]  # end, mid, end
        k1a, k1b = rhs(*c0, a, b)
        k2a, k2b = rhs(*c1, a + 0.5 * h * k1a, b + 0.5 * h * k1b)
        k3a, k3b = rhs(*c1, a + 0.5 * h * k2a, b + 0.5 * h * k2b)
        k4a, k4b = rhs(*c2, a + h * k3a, b + h * k3b)
        a += h / 6.0 * (k1a + 2.0 * k2a + 2.0 * k3a + k4a)
        b += h / 6.0 * (k1b + 2.0 * k2b + 2.0 * k3b + k4b)
```

The loop makes the $G$ RK4 steps. Step $i$ runs from the fine point $2i$ to the fine point $2i + 2$; its midpoint is the fine point $2i + 1$, so `c0`, `c1`, `c2` are the coefficients at the start, the middle and the end of the step. `rhs(*c0, a, b)` passes the three numbers of the triple `c0` as the first three arguments (the star unpacks it). The four lines compute the four slopes of the classical Runge-Kutta rule of Chapter 2: $k_1$ at the start, $k_2$ and $k_3$ at the midpoint (from the half-step predictions with $k_1$ and with $k_2$), $k_4$ at the end (from the full-step prediction with $k_3$). The last two lines advance $a$ and $b$ by $\tfrac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$; `a += x` means `a = a + x`.

```python
        new = math.atan2(b, a)
        change = new - raw
        if change > math.pi:  # bring the change of angle into (-pi, pi]
            change -= 2.0 * math.pi
        elif change <= -math.pi:
            change += 2.0 * math.pi
        theta += change
        raw = new
```

These lines follow the Pruefer angle. `math.atan2(b, a)` is the angle of the point $(a, b)$, a number between $-\pi$ and $\pi$; it jumps by $2\pi$ when the point crosses the negative $a$-axis. One step is so short that the true angle changes by much less than $\pi$; so the change `new - raw` is brought into the interval from $-\pi$ to $\pi$ by adding or subtracting $2\pi$, and that change is added to `theta`. In this way `theta` follows the angle continuously and may grow beyond $2\pi$ (Section 15.3).

```python
        r2 = a * a + b * b
        area += 0.5 * h * (r2_prev + r2)  # trapezoid rule over this step
        r2_prev = r2
        if store:
            nodes.append((a, b))
    return j * theta, area / r2_prev, nodes
```

`r2` is $r^2 = a^2 + b^2$ at the new step end; the trapezoid rule adds $\tfrac{h}{2}(r_i^2 + r_{i+1}^2)$ for the step. When `store` is true, the new values are appended to `nodes`. After the loop the function returns three things: $\Phi = j\,\theta(0)$, the derivative $d\Phi/d\varepsilon = \int r^2dy/r(0)^2$ (`r2_prev` now holds $r(0)^2$), and the stored values.

```python
FREE_MASS = [MASS] * GRID["points"]  # M = m everywhere (no interaction)
FREE_POT = [0.0] * GRID["points"]  # v = 0 everywhere
phi_zero, _, _ = shoot(0.0, 0.0, 1, 0.0, FREE_MASS, FREE_POT)
report("Phi(0) for k = 0, j = +1 (the zero mode: b stays 0)", phi_zero)
check(phi_zero == 0.0, "at eps = 0 and k = 0 the Pruefer angle stays exactly 0")
```

`[MASS] * n` is a list of $n$ copies of 1.0: the free potentials $M = m$ and $v = 0$ on the 1801 fine points. The shot at $\varepsilon = 0$, $k = 0$, $j = +1$, $a_{4,0} = 0$ is the zero mode; the underscores `_` receive the two results that are not needed. With $k = 0$ and $\varepsilon - v = 0$ the equation for $b$ is $b' = -Mb$, and $b = 0$ at the tip; so every RK4 stage gives exactly $b = 0$, `atan2(0, a)` is exactly 0 for $a > 0$, and $\Phi = 0$ without any rounding error. Out [3] prints the RESULT line with the value 0.0 and the PASS line. The text cell that follows the cell in the notebook repeats the derivation of $d\Phi/d\varepsilon$ of Section 15.3.

**In [4], the phase function.**

```python
energies = np.linspace(-4.0, 4.0, 401)  # 401 trial energies
phase = np.array([shoot(e, 0.0, 1, 0.0, FREE_MASS, FREE_POT)[0] for e in energies])
```

`np.linspace(-4.0, 4.0, 401)` makes 401 equally spaced numbers from $-4$ to $4$ (spacing 0.02). For each of them the cell shoots with $k = 0$, $j = +1$ and no interaction and keeps the first result, $\Phi$ (`[0]` takes the first entry of the returned triple).

```python
fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.plot(energies, phase / math.pi, color=PALETTE[0], lw=2.0,
        label="$\\Phi(\\varepsilon)/\\pi$, $k = 0$, $j = +1$")
for whole in range(-4, 5):
    ax.axhline(whole, color=PALETTE[1], lw=0.8, alpha=0.7)  # even targets l pi
    ax.axhline(whole + 0.5, color=PALETTE[2], lw=0.8, ls="--", alpha=0.7)  # odd
ax.plot([], [], color=PALETTE[1], lw=0.8, label="even targets $l$")
ax.plot([], [], color=PALETTE[2], lw=0.8, ls="--", label="odd targets $l + 1/2$")
```

`plt.subplots` makes a figure `fig` with one drawing area `ax` of 7.5 by 4.5 inches. `ax.plot` draws $\Phi/\pi$ against $\varepsilon$ as a blue line of width 2 (`lw`); the `label` is the text of the legend, written in the math notation of matplotlib (a doubled backslash in a Python string is one backslash). The loop draws horizontal lines (`axhline`) at the whole numbers $-4$ to $4$ (the even targets $l\pi$, divided by $\pi$) and dashed lines (the line style `ls` set to two hyphens) half-way between them (the odd targets); `alpha=0.7` makes them slightly transparent. The two `ax.plot([], [], ...)` lines draw nothing (empty lists) but put the two kinds of lines into the legend.

```python
ax.set_xlabel("trial energy $\\varepsilon$ (units of $m$)")
ax.set_ylabel("$\\Phi(\\varepsilon) / \\pi$")
ax.set_title("The phase function counts the levels")
ax.set_ylim(-3.2, 3.2)
ax.legend(fontsize=8, loc="upper left")
save_figure(fig, "phase_function",
            "The phase function $\\Phi(\\varepsilon)/\\pi$ (vertical axis) of the "
...)
check(bool(np.all(np.diff(phase) > 0.0)), "Phi increases strictly at all 400 steps")
```

These lines label the axes, set the title, show the vertical range from $-3.2$ to $3.2$ and draw the legend in the upper left corner. `save_figure` saves Figure 15e.1 with its caption (shortened here; the complete caption is printed under the figure in Section 15.8). `np.diff(phase)` is the array of the 400 differences between neighbouring values; `> 0.0` compares each with 0, and `np.all` is true when every comparison is true. Out [4] prints the figure line and PASS: $\Phi$ increases at all 400 steps, as Section 15.3 proved. In the figure the curve is nearly flat between the levels $\pm1.29$ around $\varepsilon = 0$ (there it passes the zero mode at $\Phi = 0$) and climbs steeply through each level; this is the gap of the free field.

**In [5], Newton's method inside a bracket.**

```python
def target(parity, label):
    return label * math.pi + (0.0 if parity == "even" else 0.5 * math.pi)
```

The target $t_l$ of a level: $l\pi$ for even parity, $\pi/2 + l\pi$ for odd parity. `a if condition else b` is Python's choice between two values.

```python
def find_level(k, j, parity, label, a4, mass, pot, guess, grid=GRID, tol=1e-13):
    t = target(parity, label)
    def g(e):  # Phi - target and its derivative at the energy e
        phi, dphi, _ = shoot(e, k, j, a4, mass, pot, grid)
        return phi - t, dphi
    ec = guess
    gc, dc = g(ec)
    if gc == 0.0:
        return ec
    step = min(max(abs(gc / dc) * 1.2, 1e-4), 2.0)  # the first trial step
```

`find_level` returns the energy of the level with the given momentum, block type, parity and label in the given potentials, starting from the energy `guess`. The inner function `g` shoots at the energy `e` and returns $\Phi - t_l$ and $d\Phi/d\varepsilon$. `ec`, `gc`, `dc` are the current energy, its value of $\Phi - t_l$ and its derivative. If the guess hits the target exactly, it is returned at once. The first trial step is 1.2 times the Newton estimate $|\Phi - t_l|/\Phi'$ of the distance to the root, but at least $10^{-4}$ and at most 2.

```python
    if gc < 0.0:  # Phi is too small: walk up until Phi - t >= 0
        lo = ec
        while True:
            e = lo + step
            ge, de = g(e)
            if ge >= 0.0:
                hi = e  # now [lo, hi] brackets the root
                if abs(ge) < abs(gc):
                    ec, gc, dc = e, ge, de  # keep the better end for Newton
                break
            lo, ec, gc, dc = e, e, ge, de
            step *= 2.0  # double the step
```

If $\Phi$ is below the target, the root lies higher (because $\Phi$ increases). The loop `while True` repeats until `break`: it tries the energy `lo + step`; if $\Phi - t_l$ is no longer negative there, the root lies between `lo` and this energy, which becomes `hi`, and the end with the smaller $|\Phi - t_l|$ becomes the start of Newton's method; otherwise the trial energy becomes the new `lo` and the step is doubled. Doubling reaches any distance in a few steps.

```python
    else:  # Phi is too large: walk down until Phi - t <= 0
        hi = ec
        while True:
            e = hi - step
            ge, de = g(e)
            if ge <= 0.0:
                lo = e
                if abs(ge) < abs(gc):
                    ec, gc, dc = e, ge, de
                break
            hi, ec, gc, dc = e, e, ge, de
            step *= 2.0
    if gc == 0.0:
        return ec
```

The mirror image: if $\Phi$ is above the target, the walk goes down until $\Phi - t_l \le 0$. Afterwards `[lo, hi]` brackets the root; if one end hit it exactly, it is returned.

```python
    previous = math.inf
    for _ in range(300):
        if hi - lo <= tol:
            break
        new = ec - gc / dc  # the Newton step
        bisect = not lo < new < hi or abs(gc) > 0.5 * previous
        if bisect:
            new = 0.5 * (lo + hi)  # bisection instead
        previous = abs(gc)
        moved = abs(new - ec)  # how far this step moved the energy
        ec = new
        gc, dc = g(ec)
        if gc == 0.0:
            break
        if gc < 0.0:
            lo = ec
        else:
            hi = ec
        if moved <= tol and not bisect:
            break  # a Newton step that moves less than tol: converged
    return ec
```

The refinement, at most 300 steps (`for _ in range(300)` repeats 300 times without using the counter). It stops when the bracket is shorter than the tolerance $10^{-13}$. Otherwise it computes the Newton step $\varepsilon - (\Phi - t_l)/\Phi'$. `bisect` is true when the Newton point is not strictly inside the bracket, or when the previous step did not halve $|\Phi - t_l|$ (`previous` holds the earlier value; it starts as infinity, `math.inf`, so the first step is never rejected for this reason); then the midpoint of the bracket is used instead. After the step the new energy is evaluated, the bracket end on the same side of the root is replaced (the sign of $\Phi - t_l$ tells the side), and the loop stops when a Newton step moved the energy by at most the tolerance. This is the solver's rule of Section 15.3. The cell defines functions only and prints nothing.

**In [6], the exact levels at $k = 0$ and the solver's levels.**

```python
def odd_momentum(n):
    lo, hi = (n - 0.5) * math.pi / L, n * math.pi / L
    f = lambda p: MASS * math.sin(p * L) + p * math.cos(p * L)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if f(lo) * f(mid) > 0.0 else (lo, mid)
    return 0.5 * (lo + hi)
```

The odd levels need the roots $p$ of $\tan(pL) = -p/M$ (Section 15.3). Multiplied by $M\cos(pL)$ this is $f(p) = M\sin(pL) + p\cos(pL) = 0$, which has no division. The $n$-th root lies between $(n - \tfrac12)\pi/L$ and $n\pi/L$: at the left end $\cos(pL) = 0$ and $f = \pm M$, at the right end $\sin(pL) = 0$ and $f = \pm p$ with the opposite sign, so $f$ changes sign in between. `lambda p: ...` defines a small function without a name. The loop is **bisection**: if $f$ has the same sign at `lo` and at the midpoint (their product is positive), the root lies in the right half, otherwise in the left half. After 200 halvings the interval is far below rounding size, and its midpoint is returned.

```python
def exact_level(parity, label):
    if parity == "even":
        n = abs(label)
        return math.copysign(math.sqrt(MASS ** 2 + (n * math.pi / L) ** 2), label) \
            if n else 0.0
    n = label + 1 if label >= 0 else -label  # labels 0, 1, ... and -1, -2, ...
    return math.copysign(math.sqrt(MASS ** 2 + odd_momentum(n) ** 2), label + 0.5)
```

The exact free level at $k = 0$ with a given parity and label. For even parity the label $l$ belongs to $n = |l|$ and the level is $\pm\sqrt{M^2 + (n\pi/L)^2}$ with the sign of $l$ (`math.copysign(x, s)` is $|x|$ with the sign of $s$); the label 0 is the zero mode, $\varepsilon = 0$ (`if n else 0.0`: a nonzero $n$ counts as true). The backslash at the end of a line continues the statement on the next line. For odd parity the labels $0, 1, 2, \dots$ are the positive levels with $n = l + 1$, and the labels $-1, -2, \dots$ the negative ones with $n = -l$; the sign is that of $l + \tfrac12$, which is positive for $l \ge 0$ and negative for $l \le -1$.

```python
RECORD_FREE = "Revision/kohn_sham/results/spectrum/free-k0-analytic.csv"
recorded = {}
for line in repository_file(RECORD_FREE).read_text(encoding="utf-8").split("\n")[1:]:
    if line:
        m_, l_, parity, label, eps_num, eps_exact, _ = line.split(",")
        if float(m_) == 1.0 and float(l_) == 3.0:
            recorded[(parity, int(label))] = (float(eps_num), float(eps_exact))
```

The record file of the solver's free spectra at $k = 0$ is read as text, split into lines, and the first line (the column names) is skipped (`[1:]` takes everything from the second entry on). Each nonempty line is split at the commas into seven fields: the mass, $L$, the parity, the label, the solver's numerical level, the exact level and one more column that is not needed. Only the rows with $M = 1$ and $L = 3$ are kept (the record also tests other masses and lengths), in a dictionary whose key is the pair (parity, label).

```python
worst_exact, worst_record = 0.0, 0.0
say("parity label   shooting           exact              difference")
for parity in ("even", "odd"):
    for label in range(-3, 6):
        exact = exact_level(parity, label)
        found = find_level(0.0, 1, parity, label, 0.0, FREE_MASS, FREE_POT, exact + 0.01)
        say(f"{parity:5} {label:3d}  {found:17.13f}  {exact:17.13f}"
            f"  {found - exact:10.2e}")
        if abs(exact) < 4.0:
            worst_exact = max(worst_exact, abs(found - exact))
        if (parity, label) in recorded:
            worst_record = max(worst_record, abs(found - recorded[(parity, label)][0]))
```

For both parities and the labels $-3$ to $5$ the cell computes the exact level, finds the level by shooting (with the guess 0.01 above the exact value), and prints a table row: the parity in 5 characters, the label in 3 digits, both levels with 13 digits after the point, and their difference in the exponent format `.2e` (two digits after the point and a power of ten). The largest difference is kept for $|\varepsilon| < 4$ (`worst_exact`; the record uses the same range for its tolerance), and the largest difference to the solver's recorded value for every row present in the record (`worst_record`).

```python
report("largest |shooting - exact| for |eps| < 4", f"{worst_exact:.2e}")
report("largest |this notebook - solver record|", f"{worst_record:.2e}")
check(worst_exact < 5e-9,
      "the shooting levels equal the exact levels within 5e-9 for |eps| < 4",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "free_k0_analytic_spectra")
check(worst_record < 1e-12, "the levels equal the solver's levels within 1e-12",
      record=f"{RECORD_FREE}, column eps_numeric")
```

Out [6] shows the table. The differences grow with the energy, from $10^{-13}$ near $\pm1.3$ to $6.7 \times 10^{-9}$ at the odd label 5 ($\varepsilon = 5.90$): the error of RK4 grows like $(h\varepsilon)^4$, because a higher level oscillates faster. The largest difference for $|\varepsilon| < 4$ is $7.23 \times 10^{-10}$, the value of the record's check free_k0_analytic_spectra. The first check therefore tests the tolerance $5 \times 10^{-9}$ only for $|\varepsilon| < 4$, as the record does, and its PASS line says so (the check name is written on its own line of the call because the call would otherwise be longer than a line of the page); for $4 \le |\varepsilon| < 7$ the record allows $3 \times 10^{-7}$, far above the $6.7 \times 10^{-9}$ of the table. The largest difference to the solver's own numbers is $7.99 \times 10^{-15}$: the Python code and the Rust program do the same arithmetic in a slightly different order. Both checks pass. The even label 0 is printed as $-0.0000000000000$, a difference of $-1.4 \times 10^{-19}$ from the exact zero, left by Newton's method.

**In [7], orbitals with Hermite midpoints.**

```python
def orbital(eps, k, j, a4, mass, pot, grid=GRID):
    _, _, nodes = shoot(eps, k, j, a4, mass, pot, grid, store=True)
    h = grid["h"]
    kk = k * math.exp(-a4)
    a = np.zeros(grid["points"])
    b = np.zeros(grid["points"])
    a[0::2] = [p[0] for p in nodes]  # the step ends
    b[0::2] = [p[1] for p in nodes]
```

`orbital` returns the normalised orbital of a level on the whole fine grid. It shoots once more at the level's energy and keeps the values at the $G + 1$ step ends. `np.zeros(n)` is an array of $n$ zeros. `a[0::2]` is every second entry starting with the first (the fine indices $0, 2, 4, \dots$, the step ends), and the step-end values are written there.

```python
    f = np.arange(0, grid["points"], 2)  # fine indices of the step ends
    m_y = np.array(mass)[f]
    kap = kk * np.array(grid["ew"])[f]
    je = j * (eps - np.array(pot)[f])
    da = m_y * a[f] - (kap + je) * b[f]  # derivatives from the equation
    db = (je - kap) * a[f] - m_y * b[f]
```

`np.arange(0, n, 2)` is the array $0, 2, 4, \dots$ of the step-end indices; indexing an array with it picks those entries. So `m_y`, `kap` and `je` are $M$, $\kappa k$ and $j(\varepsilon - v)$ at the step ends, and `da`, `db` are the derivatives $a'$, $b'$ there, computed from the block equation itself (this is where the Hermite formula gets its derivatives).

```python
    a[1::2] = 0.5 * (a[f][:-1] + a[f][1:]) + h / 8.0 * (da[:-1] - da[1:])
    b[1::2] = 0.5 * (b[f][:-1] + b[f][1:]) + h / 8.0 * (db[:-1] - db[1:])
    norm = math.sqrt(float(np.sum(grid["simpson"] * (a * a + b * b))))
    return a / norm, b / norm
```

`a[1::2]` are the midpoints. For each step, `a[f][:-1]` is the value at its start (all step ends but the last) and `a[f][1:]` the value at its end (all but the first); the line is the Hermite formula $\tfrac12(u_0 + u_1) + \tfrac{h}{8}(u_0' - u_1')$ of Section 15.3, for all steps at once. Then Simpson's rule gives $\int(a^2 + b^2)\,dy$, and both components are divided by its square root, so the returned orbital is normalised.

```python
zero_a, zero_b = orbital(0.0, 0.0, 1, 0.0, FREE_MASS, FREE_POT)
bulk_eps = find_level(0.0, 1, "even", 1, 0.0, FREE_MASS, FREE_POT, 1.4)
bulk_a, bulk_b = orbital(bulk_eps, 0.0, 1, 0.0, FREE_MASS, FREE_POT)
band_eps = find_level(0.5, 1, "even", 0, 0.0, FREE_MASS, FREE_POT, 0.8)
band_a, band_b = orbital(band_eps, 0.5, 1, 0.0, FREE_MASS, FREE_POT)
```

Three orbitals of the free block $j = +1$: the zero mode ($\varepsilon = 0$, $k = 0$); the first even bulk level at $k = 0$ (label 1, guess 1.4; its energy is $1.4479719$, Out [6]); and the brane-band level at $k = 0.5$ (the shell $n_2 = 4$; label 0, guess 0.8). Their energies appear in the panel titles of the figure.

```python
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6), sharey=True,
                         layout="constrained")
for ax, (a, b, title) in zip(axes, [
        (zero_a, zero_b, "zero mode, $k = 0$, $\\varepsilon = 0$"),
        (bulk_a, bulk_b, f"bulk, $k = 0$, $\\varepsilon = {bulk_eps:.4f}$"),
        (band_a, band_b, f"brane band, $k = 0.5$, $\\varepsilon = {band_eps:.4f}$")]):
    ax.plot(Y, a, color=PALETTE[0], lw=2.0, label="$a(y)$")
    ax.plot(Y, b, color=PALETTE[1], lw=2.0, ls="--", label="$b(y)$")
    ax.set_title(title, fontsize=9)
    ax.set_xlabel("hidden coordinate $y$")
axes[0].set_ylabel("orbital (normalised)")
axes[0].legend()
save_figure(fig, "orbitals",
            "Three normalised orbitals of the free block $j = +1$ (components $a$, "
...)
```

`plt.subplots(1, 3, ...)` makes one row of three drawing areas (`axes`), which share the vertical axis (`sharey=True`); `layout="constrained"` spaces them so that no labels overlap. `zip` pairs each drawing area with one triple (the two components and a title), and the loop draws $a$ solid and $b$ dashed against $y$. The first panel gets the vertical label and the legend, and `save_figure` saves Figure 15e.2. The student should see that the zero mode is $e^{y}$ and sits at the brane with $b = 0$ everywhere, that the bulk orbital fills the whole interval, and that the band orbital is again bound to the brane; every $b$ vanishes at both ends.

```python
exact_zero = math.sqrt(2.0 * MASS / (1.0 - math.exp(-2.0 * MASS * L))) * np.exp(MASS * Y)
zero_error = max(float(np.max(np.abs(zero_a - exact_zero))),
                 float(np.max(np.abs(zero_b))))
report("largest deviation of the zero mode from its exact form", f"{zero_error:.2e}")
check(zero_error < 1e-11, "the zero mode is (e^{My}, 0), normalised, to 1e-11",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "free_zero_mode_exact")
```

`exact_zero` is the normalised zero mode $\sqrt{2M/(1 - e^{-2ML})}\,e^{My}$ of Section 15.3 on the fine grid. `zero_error` is the larger of the largest deviation of $a$ from it and the largest $|b|$. Out [7] prints $1.35 \times 10^{-12}$, the value of the record's check free_zero_mode_exact, and PASS.

**In [8], the order 4 of RK4.**

```python
STEPS = [100, 200, 400, 800]
errors = {2: [], 3: []}
for steps in STEPS:
    grid = make_grid(steps)
    mass = [MASS] * grid["points"]
    pot = [0.0] * grid["points"]
    for label in errors:
        found = find_level(0.0, 1, "even", label, 0.0, mass, pot,
                           exact_level("even", label), grid=grid)
        errors[label].append(abs(found - exact_level("even", label)))
```

For the grids of 100, 200, 400 and 800 steps the cell finds the even levels with the labels 2 and 3 at $k = 0$ (exact values $\sqrt{1 + (2\pi/3)^2} = 2.3208815$ and $\sqrt{1 + \pi^2} = 3.2969083$) and appends the size of the error to a list for each label. Looping over a dictionary (`for label in errors`) visits its keys, 2 and 3.

```python
ratios = []
for label, errs in errors.items():
    steps_ratios = [errs[i] / errs[i + 1] for i in range(len(errs) - 1)]
    ratios += steps_ratios
    say(f"label {label}: errors " + ", ".join(f"{e:.2e}" for e in errs)
        + "; ratios " + ", ".join(f"{r:.2f}" for r in steps_ratios))
```

For each label the three ratios of the error on one grid to the error on the grid with twice as many steps are computed, collected in `ratios` and printed (`", ".join(...)` writes the numbers separated by commas). Out [8] shows the errors $2.45 \times 10^{-7}$, $1.53 \times 10^{-8}$, $9.59 \times 10^{-10}$, $5.99 \times 10^{-11}$ for the label 2 and ratios between 15.96 and 16.00.

```python
steps_h = [L / s for s in STEPS]
fig, ax = plt.subplots()
for colour, (label, errs) in zip(PALETTE, errors.items()):
    ax.loglog(steps_h, errs, "o-", color=colour, lw=2.0, ms=7,
              label=f"even level $l = {label}$")
ax.loglog(steps_h, [errors[3][0] * (s / steps_h[0]) ** 4 for s in steps_h], "--",
          color="0.4", lw=1.2, label="slope 4: error $\\propto h^4$")
```

`steps_h` are the steps $h = 3/G$. `ax.loglog` draws with logarithmic scales on both axes; the style `"o-"` draws dots joined by lines, `ms` is the size of the dots. On such axes a power law error $= C h^4$ is a straight line of slope 4; the dashed grey line (`color="0.4"` is a grey) is that law through the first error of the label 3.

```python
ax.set_xlabel("step $h$ (units of $1/m$)")
ax.set_ylabel("|shooting level - exact level| (units of $m$)")
ax.set_title("RK4: halving the step divides the error by 16")
ax.legend()
save_figure(fig, "rk4_convergence",
            "Error of two shooting levels (vertical axis, logarithmic, units of $m$) "
...)
middle = sorted(ratios)[len(ratios) // 2]
report("median error ratio for halving the step", f"{middle:.2f}")
check(15.0 < middle < 17.0, "the error ratio is 16 within 1 (fourth order)",
      record="Revision/kohn_sham/reports/ks-rust-determinism.json, check "
             "refined_free_spectra_convergence_order")
```

After the labels and the legend, `save_figure` saves Figure 15e.3. `sorted(ratios)` sorts the six ratios; the entry at the position `len(ratios) // 2` (`//` divides and drops the remainder; here position 3) is the **median**, the middle value. It is 16.00, the ratio $2^4$ of a fourth-order method, the same number as in the record's check refined_free_spectra_convergence_order. In the figure the dots lie on lines parallel to the dashed line of slope 4.

**In [9], the brane band and the redshift.**

```python
THEORY = json.loads(repository_file("Revision/kohn_sham/ks-theory.json").read_text(
    encoding="utf-8"))  # the theory file of the solver
C_RECORD = float(THEORY["checksNumeric"]["braneBandSlope_M1_H1_L3_a0"])
c_formula = (2 * MASS / (2 * MASS - H) * (1 - math.exp(-(2 * MASS - H) * L))
             / (1 - math.exp(-2 * MASS * L)))
```

`json.loads` turns the text of the theory file into Python dictionaries and lists. `C_RECORD` is the recorded slope $c = 1.9051482536448664$, and `c_formula` computes $c = \tfrac{2M}{2M - H}\cdot\tfrac{1 - e^{-(2M - H)L}}{1 - e^{-2ML}}$ of Section 15.4 again.

```python
def band(k, a4):
    return find_level(k, 1, "even", 0, a4, FREE_MASS, FREE_POT, 1.9 * k * math.exp(-a4))
```

`band(k, a4)` is the brane-band level: block type $+1$, even parity, label 0, free potentials, with the guess $1.9\,k\,e^{-a_{4,0}}$ from the small-$k$ law.

```python
momenta = np.linspace(0.0, 2.0, 41)
fig, ax = plt.subplots()
slopes = []
for shade, a4 in zip(("#86b6ef", "#2a78d6", "#104281"), (0.0, 1.0, 2.0)):
    curve = [band(k, a4) for k in momenta]
    ax.plot(momenta, curve, "o-", color=shade, ms=4, lw=1.8,
            label=f"$a_{{4,0}} = {a4:.0f}$")
    ax.plot(momenta, c_formula * momenta * math.exp(-a4), ":", color=shade, lw=1.2)
```

For the slices $a_{4,0} = 0, 1, 2$ (in light, middle and dark blue) the cell computes the band at 41 momenta from 0 to 2 and draws it, together with the dotted tangent $c\,k\,e^{-a_{4,0}}$. In an f-string a doubled brace `{{` prints one brace, so the label reads $a_{4,0} = 0$ and so on.

```python
    s1, s2 = band(1e-4, a4) / 1e-4, band(2e-4, a4) / 2e-4  # s(k) and s(2k)
    slopes.append((4.0 * s1 - s2) / 3.0 * math.exp(a4))  # slope times e^{a4,0}
    if a4 == 0.0:
        s4 = band(4e-4, a4) / 4e-4  # s(4k), to measure how the error grows
        growth = (s4 - s2) / (s2 - s1)  # 4 if the error of s is proportional to k^2
```

Still inside the loop: $s(k) = \varepsilon(k)/k$ at $k = 10^{-4}$ and $2 \times 10^{-4}$. The band is an odd function of $k$ (the text cell before In [9] derives this from the two block symmetries), so $\varepsilon = ck - dk^3 + \dots$ and $s(k) = c - dk^2 + \dots$; the **Richardson extrapolation** $\tfrac13(4s(k) - s(2k))$ removes the $k^2$ term: $4(c - dk^2) - (c - 4dk^2) = 3c$. Multiplied by $e^{a_{4,0}}$ it must be the slice-independent $c$. At the first slice the cell also computes $s(4k)$ and the ratio of the changes $(s(4k) - s(2k))/(s(2k) - s(k))$, which is $(16 - 4)/(4 - 1) = 4$ if the error of $s$ is proportional to $k^2$.

```python
ax.plot([], [], ":", color="0.4", label="$c\\,k\\,e^{-a_{4,0}}$")
ax.set_xlabel("3-momentum $k$ (units of $m$)")
ax.set_ylabel("brane-band level $\\varepsilon$ (units of $m$)")
ax.set_title("The brane band redshifts along the history")
ax.legend()
save_figure(fig, "brane_band",
            "The brane-band level $\\varepsilon(k)$ (vertical axis, units of $m$) "
...)
rescale = max(abs(band(k, a4) - band(k * math.exp(-a4), 0.0))
              for k in (0.25, 1.0, 2.5) for a4 in (0.5, 1.0, 2.0))
```

After the legend entry for the dotted tangents and the labels, `save_figure` saves Figure 15e.4. `rescale` is the largest violation of the rescaling identity $\varepsilon(k; a_{4,0}) = \varepsilon(k\,e^{-a_{4,0}}; 0)$ for three momenta and three slices; the two `for` clauses inside `max(...)` run over all nine pairs.

```python
report("growth of the error of eps(k)/k when k doubles", f"{growth:.4f}")
report("slope c times e^{a4,0} at a4,0 = 0, 1, 2",
       ", ".join(f"{s:.10f}" for s in slopes))
report("largest violation of the rescaling identity", f"{rescale:.1e}")
check(abs(c_formula - C_RECORD) < 1e-14 and
      max(abs(s - C_RECORD) for s in slopes) < 1e-9 * C_RECORD,
      "the brane-band slope is c e^{-a4,0} with c = 1.9051482536",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "free_brane_band_slope")
check(rescale < 1e-12, "eps(k, a4,0) = eps(k e^{-a4,0}, 0) within 1e-12",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "free_rescaling_relation_and_band_monotone")
```

Out [9] prints the growth factor $4.0000$, the three extrapolated slopes, each $1.9051482536$, and the violation 0.0, and both checks pass. The violation is exactly zero, not merely small, because the two calls do the same arithmetic: `shoot` uses $k$ only through the product $k\,e^{-a_{4,0}}$, and $k\,e^{-a_{4,0}}$ at the slice $a_{4,0}$ and $(k\,e^{-a_{4,0}})\,e^{0}$ at the slice 0 are the same number. In Figure 15e.4 each band curve is the previous one with the momentum axis stretched by $e = 2.718$, and every curve lies below its dotted tangent.

**In [10], the self-consistent loop.**

```python
POINTS = GRID["points"]
P_FACTOR = 1.0 / (E6 * VOL7)  # P = e^{-6Hy}/Vol_7 on the fine grid
```

`POINTS` is 1801, and `P_FACTOR` is the array of $P = e^{-6Hy}/\mathrm{Vol}_7$ at the fine points (Section 15.2).

```python
def iteration(x, lam, a4, guesses):
    mass = (MASS + x[:POINTS]).tolist()
    pot = x[POINTS:].tolist()
    n = np.zeros(POINTS)
    s = np.zeros(POINTS)
    levels = {}
```

`iteration` performs one Kohn-Sham iteration for $N = 8$. The input `x` is the array of the $2 \times 1801$ unknowns: its first half (`x[:POINTS]`) is $M - m$ and its second half (`x[POINTS:]`) is $v$; they become the lists `mass` and `pot` that `shoot` expects (`.tolist()`). The densities $n$ and $S$ start at zero, and `levels` will hold the two occupied levels.

```python
    for j in (1, -1):  # the two block types, each level four-fold (g = 4)
        eps = find_level(0.0, j, "even", 0, a4, mass, pot, guesses.get(j, 0.0))
        a, b = orbital(eps, 0.0, j, a4, mass, pot)
        weight = 0.5 * 4.0 * 1.0  # w g f with w = 1/2 (the Z2 doubling)
        n += weight * P_FACTOR * (a * a + b * b)
        s += weight * P_FACTOR * j * 2.0 * a * b
        levels[j] = eps
```

For each block type the occupied level is the zero mode: $k = 0$, even parity, label 0. Its energy is found starting from the previous iteration's energy (`guesses.get(j, 0.0)` gives 0 in the first iteration, when `guesses` is empty), and its orbital is computed. The weight $wgf = \tfrac12\cdot4\cdot1 = 2$ multiplies the orbital densities $P(a^2 + b^2)$ and $P\,j\,2ab$, which are added to $n$ and $S$ (the formulas of Section 15.2).

```python
    x_out = np.concatenate([lam * (15.0 / 16.0) * s, lam * (-1.0 / 16.0) * n])
    e_int = lam * (15.0 / 32.0 * s * s - 1.0 / 32.0 * n * n)
    energy = sum(4.0 * e for e in levels.values()) \
        - 2.0 * VOL7 * float(np.sum(GRID["simpson"] * E6 * e_int))
    return float(np.max(np.abs(x_out - x))), x_out, energy, levels
```

The output potentials are $\tfrac{15}{16}\lambda S$ and $-\tfrac{1}{16}\lambda n$, joined into one array (`np.concatenate`). `e_int` is the interaction energy density, and `energy` is $E_{KS} = \sum gf\varepsilon - 2\,\mathrm{Vol}_7\int e^{6Hy}e_{int}\,dy$ with $g f = 4$ for each of the two levels and Simpson's rule for the integral. The function returns the size of the residual (the largest $|x_{out} - x|$), the output potentials, the energy and the levels.

```python
class Anderson:
    def __init__(self, depth=6, beta=0.4):
        self.depth, self.beta = depth, beta
        self.xs, self.rs, self.best = [], [], math.inf
```

A **class** defines a new kind of object that keeps data between calls. An `Anderson` object stores the depth 6, the factor $\beta = 0.4$, the lists of the last inputs `xs` and residuals `rs`, and the smallest residual size seen so far, `best`. `__init__` runs when the object is made; `self` is the object itself.

```python
    def next(self, x, r):
        size = float(np.max(np.abs(r)))
        if size > 10.0 * self.best and self.xs:
            self.xs, self.rs = [], []  # the residual grew tenfold: start again
        self.best = min(self.best, size)
        self.xs = (self.xs + [x.copy()])[-self.depth:]
        self.rs = (self.rs + [r.copy()])[-self.depth:]
        count = len(self.xs)
```

`next` receives the current input and residual and returns the next input. If the residual is more than ten times the smallest one seen and there is a history, the history is forgotten (an empty list counts as false, a nonempty one as true). The new pair is appended, and `[-self.depth:]` keeps only the last six. `count` is the number $p$ of stored pairs.

```python
        system = np.zeros((count + 1, count + 1))
        gram = np.array([[float(np.dot(u, v)) for v in self.rs] for u in self.rs])
        system[:count, :count] = gram + 1e-12 * np.max(np.diag(gram)) * np.eye(count)
        system[:count, count] = 1.0
        system[count, :count] = 1.0
        right = np.zeros(count + 1)
        right[count] = 1.0
        weights = np.linalg.solve(system, right)[:count]
        return sum(c * (xi + self.beta * ri)
                   for c, xi, ri in zip(weights, self.xs, self.rs))
```

These lines build and solve the bordered system of Section 15.5. `gram` is the Gram matrix $G_{ik} = r_i\cdot r_k$ (`np.dot` is the dot product of two arrays). The upper left block of `system` is $G$ plus $10^{-12}$ times its largest diagonal entry on the diagonal (`np.eye(count)` is the unit matrix), the last column and the last row (without the corner) are ones, and the right side is $(0, \dots, 0, 1)$. `np.linalg.solve` solves the linear system; its first $p$ entries are the weights $c_i$ (the last one is $-\nu$). The function returns $\sum_i c_i(x_i + \beta r_i)$.

```python
def solve_n8(lam, a4=0.0, mixing="anderson", tol=1e-11, limit=200):
    x = np.zeros(2 * POINTS)
    mixer = Anderson()
    guesses, history = {}, []
    for it in range(1, limit + 1):
        residual, x_out, energy, levels = iteration(x, lam, a4, guesses)
        guesses = levels
        history.append((it, residual, energy))
        if residual <= tol:
            return energy, levels, history, x
        r = x_out - x
        x = mixer.next(x, r) if mixing == "anderson" else x + 0.4 * r
    raise RuntimeError("no convergence")
```

`solve_n8` runs the loop for the coupling `lam`. It starts from the free potentials ($x = 0$), makes a new `Anderson` object, and repeats at most 200 iterations: one iteration, its levels as the next guesses, its number, residual and energy appended to `history`; if the residual is at most $10^{-11}$, the energy, levels, history and potentials are returned; otherwise the next input is made by Anderson mixing or, if `mixing` is `"linear"`, by linear mixing $x + 0.4\,r$. If the loop never converges, a `RuntimeError` stops the notebook. The cell defines functions and the class only and prints nothing.

**In [11], the state $N = 8$ with $+\lambda_1$.**

```python
params = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                    .read_text(encoding="utf-8"))
calib = {int(c["N"]): c for c in params["couplingCalibration"]["values"]}
LAM1, LAM2 = calib[8]["lambda1"], calib[8]["lambda2"]
```

The parameters file of the record is read; `calib` is a **dictionary comprehension** that files the calibration entries under their particle number (8, 136, 688), and `LAM1`, `LAM2` are the couplings $\lambda_1 = 0.01946$ and $\lambda_2 = 0.05838$ of $N = 8$ (Section 15.2).

```python
energy, levels, history, x_final = solve_n8(LAM1)
say("iteration   residual        E_KS")
for it, residual, e in history:
    say(f"{it:9d}   {residual:9.3e}   {e:.13e}")
```

The loop is run with $+\lambda_1$ and its history is printed, one line per iteration: the iteration number, the residual and the energy. Out [11] shows the residual falling from $0.1$ in the first iteration to $7.5 \times 10^{-13}$ in the thirteenth, and the energy settling at $-9.8684261908764 \times 10^{-4}$.

```python
SUMMARY = "Revision/kohn_sham/results/ground/summary.csv"
with open(repository_file(SUMMARY), newline="", encoding="utf-8") as handle:
    ground = {row["id"]: row for row in csv.DictReader(handle)}
runs = {run["id"]: run for run in json.loads(repository_file(
    "Revision/kohn_sham/results/ground/runs.json").read_text(encoding="utf-8"))}
recorded_history = runs["N8_lamp1_a00"]["scfHistory_iteration_residual_E"]
early = max(abs(h[1] - r[1]) / r[1] for h, r in zip(history[:6], recorded_history[:6]))
```

`with open(...) as handle:` opens the record's table of ground states and closes it again after the indented block; `csv.DictReader` reads each row as a dictionary from the column names to the values, and the rows are filed under their state name. The file `runs.json` holds for every ground state the residual and energy of each iteration; `recorded_history` is that list for `N8_lamp1_a00`. `early` is the largest relative difference between this notebook's residuals and the recorded ones in the first six iterations.

```python
report("E_KS of N = 8 with lambda_1", f"{energy:.15e}")
report("iterations (this notebook / record)",
       f"{len(history)} / {len(recorded_history)}")
report("largest relative difference of the first six residuals", f"{early:.1e}")
check(abs(energy - float(ground["N8_lamp1_a00"]["E_KS"])) < 1e-14
      and abs(levels[1] - float(ground["N8_lamp1_a00"]["HOMO"])) < 1e-13,
      "E_KS and HOMO of N8_lamp1_a00 reproduced", record=f"{SUMMARY}, row N8_lamp1_a00")
check(early < 1e-5, "the first six residuals equal the recorded ones within 1e-5",
      record="Revision/kohn_sham/results/ground/runs.json, N8_lamp1_a00")
check(abs(levels[1] - levels[-1]) < 1e-13, "the levels of j = +1 and j = -1 are equal")
```

The cell reports $E_{KS} = -9.868426190876385 \times 10^{-4}$, 13 iterations here and in the record, and the relative difference $3.0 \times 10^{-7}$ of the first six residuals (the later residuals are differences of nearly equal numbers and depend on the order of the arithmetic, as the text cell explains). The three checks pass: the energy and the occupied level (HOMO) agree with the record within $10^{-14}$ and $10^{-13}$, the early residuals within $10^{-5}$, and the levels of the two block types are equal, as the symmetry $\sigma_3 h_j(k)\sigma_3 = h_{-j}(-k)$ demands at $k = 0$.

**In [12], Anderson against linear mixing.**

```python
energy_lin, _, history_lin, _ = solve_n8(LAM1, mixing="linear")
fig, ax = plt.subplots()
ax.semilogy([h[0] for h in history_lin], [h[1] for h in history_lin], "s-",
            color=PALETTE[1], ms=4, lw=1.5, label="linear mixing, $\\beta = 0.4$")
ax.semilogy([h[0] for h in history], [h[1] for h in history], "o-",
            color=PALETTE[0], ms=7, lw=2.0, label="Anderson mixing (this notebook)")
ax.semilogy([r[0] for r in recorded_history], [r[1] for r in recorded_history], "x",
            color="black", ms=9, label="Anderson mixing (Rust solver, record)")
ax.axhline(1e-11, color="0.4", ls=":", lw=1.2, label="tolerance $10^{-11}$")
```

The same state is solved with linear mixing. `ax.semilogy` draws with a logarithmic vertical axis: the residual against the iteration for linear mixing (orange squares, `"s-"`), for this notebook's Anderson run (blue dots) and for the solver's recorded run (black crosses, `"x"` without a line), and a dotted line at the tolerance.

```python
ax.set_xlabel("iteration")
ax.set_ylabel("residual (units of $m$)")
ax.set_title("Self-consistent loop for $N = 8$, $\\lambda = +\\lambda_1$")
ax.legend(fontsize=8)
save_figure(fig, "scf_mixing",
            "Residual of the self-consistent loop (vertical axis, logarithmic, units "
...)
report("iterations: Anderson / linear", f"{len(history)} / {len(history_lin)}")
report("|E(linear) - E(Anderson)|", f"{abs(energy_lin - energy):.1e}")
check(abs(energy_lin - energy) < 1e-12 and len(history_lin) > 2 * len(history),
      "linear mixing reaches the same energy, with more than twice the iterations")
```

`save_figure` saves Figure 15e.5. Out [12] reports 13 iterations for Anderson mixing and 47 for linear mixing, and an energy difference of $8.0 \times 10^{-15}$: both reach the same state, linear mixing with about four times the work. The check passes. In the figure the black crosses of the Rust solver sit on the blue dots.

**In [13], the four couplings and the symmetry.**

```python
tags = {"lamp1": LAM1, "lamm1": -LAM1, "lamp2": LAM2, "lamm2": -LAM2}
results = {}
worst_e, worst_homo = 0.0, 0.0
for tag, lam in tags.items():
    e, lv, hist, xf = solve_n8(lam)
    results[tag] = (e, lv[1], xf)
    row = ground[f"N8_{tag}_a00"]
    worst_e = max(worst_e, abs(e - float(row["E_KS"])))
    worst_homo = max(worst_homo, abs(lv[1] - float(row["HOMO"])))
    say(f"{tag}: lambda {lam:+.5f}, E_KS {e:+.12e}, HOMO {lv[1]:+.12e},"
        f" {len(hist)} it.")
```

The dictionary `tags` maps the four run tags to the couplings $\pm\lambda_1$, $\pm\lambda_2$. For each, the loop is solved, the energy, the level of $j = +1$ and the final potentials are kept in `results`, the differences to the record's row (for example `N8_lamm1_a00`) are tracked, and a line is printed; the format `+.5f` always prints the sign. Out [13] shows that $E_{KS}$ and the HOMO of $-\lambda$ are exactly the negatives of those of $+\lambda$, with 13 iterations for $\pm\lambda_1$ and 17 for $\pm\lambda_2$.

```python
xf = results["lamp1"][2]
lumo = find_level(0.25, 1, "even", 0, 0.0, (MASS + xf[:POINTS]).tolist(),
                  xf[POINTS:].tolist(), 0.43)
report("LUMO of N8_lamp1_a00 (brane band at k = 0.25)", f"{lumo:.13f}")
antisym = max(abs(results["lamp1"][0] + results["lamm1"][0]),
              abs(results["lamp2"][0] + results["lamm2"][0]))
report("largest |E(+lambda) + E(-lambda)|", f"{antisym:.1e}")
```

The lowest empty level of the state with $+\lambda_1$ is the brane-band level of the first shell, $k = 0.25$, in the converged potentials; it is found with the guess 0.43 (the free gap). `antisym` is the larger of $|E(+\lambda_1) + E(-\lambda_1)|$ and $|E(+\lambda_2) + E(-\lambda_2)|$. Out [13] prints the LUMO $0.4306983508491$ and the value 0.0.

```python
check(worst_e < 1e-14 and worst_homo < 1e-13,
      "E_KS and HOMO of all four couplings reproduced", record=f"{SUMMARY}, rows N8")
check(abs(lumo - float(ground["N8_lamp1_a00"]["LUMO"])) < 1e-12,
      "the LUMO of N8_lamp1_a00 reproduced", record=f"{SUMMARY}, column LUMO")
check(antisym < 1e-15, "E_KS(-lambda) = -E_KS(+lambda) for N = 8")
```

The three checks pass: the four energies and levels agree with the record, the LUMO too, and the energy is odd in $\lambda$, the exact symmetry derived in Section 15.5 (the text cell before the code cell repeats the derivation). The sum is exactly zero, not merely small, because the loop for $-\lambda$ performs exactly the arithmetic of the loop for $+\lambda$ with the signs of $\varepsilon$, $v$ and $b$ reversed, and a change of sign is exact in computer arithmetic.

**In [14], the self-consistent potentials.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
labels = {"lamp1": "$+\\lambda_1$", "lamm1": "$-\\lambda_1$",
          "lamp2": "$+\\lambda_2$", "lamm2": "$-\\lambda_2$"}
for colour, (tag, label) in zip(PALETTE, labels.items()):
    xf = results[tag][2]
    style = "-" if tag.startswith("lamp") else "--"
    left.plot(Y, xf[:POINTS], style, color=colour, lw=1.8, label=label)
    right.plot(Y, xf[POINTS:], style, color=colour, lw=1.8, label=label)
```

Two drawing areas side by side, named `left` and `right`. For each coupling the converged potentials are drawn: $M - m$ on the left and $v$ on the right, solid for positive couplings and dashed for negative ones (`tag.startswith("lamp")` is true for the tags of $+\lambda$).

```python
left.set_xlabel("hidden coordinate $y$")
left.set_ylabel("$M(y) - m$ (units of $m$)")
left.set_title("Mass shift")
right.set_xlabel("hidden coordinate $y$")
right.set_ylabel("$v(y)$ (units of $m$)")
right.set_title("Potential")
right.legend()
save_figure(fig, "n8_potentials",
            "The self-consistent mass shift $M(y) - m$ (left) and potential $v(y)$ "
...)
```

The axis labels and titles, and `save_figure` for Figure 15e.6. The student should see the potential $v = -\lambda n/16$ grow toward the tip roughly like $e^{-4y}$: the zero mode is $e^{y}$, so its coordinate density is $e^{2y}$, and dividing by the proper volume factor $e^{6y}$ gives $e^{-4y}$. This growth toward the tip is why the interacting $N = 8$ results depend strongly on the cutoff $L$ (Section 15.2, the paragraph on the cutoff). The mass shift is smaller, because the scalar density of the zero modes vanishes without interaction ($b = 0$) and is created only by the interaction itself.

```python
plus, minus = results["lamp1"][2], results["lamm1"][2]  # potentials x of +-lambda_1
mirror = max(float(np.max(np.abs(plus[:POINTS] - minus[:POINTS]))),
             float(np.max(np.abs(plus[POINTS:] + minus[POINTS:]))))
report("largest violation of the potential symmetry", f"{mirror:.1e}")
check(mirror < 1e-12, "M - m is even and v is odd under lambda -> -lambda")
```

The symmetry of Section 15.5 predicts that $M - m$ is the same for $\pm\lambda$ and $v$ changes sign. `mirror` is the larger of the largest $|(M - m)_+ - (M - m)_-|$ and the largest $|v_+ + v_-|$. Out [14] prints 0.0 and PASS; in the figure the dashed curves of the mass shift lie on the solid ones.

**In [15], the last check.**

```python
NAMES = ["phase_function", "orbitals", "rk4_convergence", "brane_band", "scf_mixing",
         "n8_potentials"]
missing = [name for number, name in enumerate(NAMES, start=1)
           if not output_file(f"{FIGURE_FOLDER}/15e_{number}_{name}.png").is_file()]
check(missing == [], "every figure file of this notebook exists")
all_checks_passed()
```

`NAMES` lists the six figure names in order. `enumerate(NAMES, start=1)` pairs each name with its number 1, 2, ...; the list comprehension with `if not ...` collects the names whose file does not exist. The check requires that list to be empty, and `all_checks_passed()` prints the last line, ALL 18 CHECKS PASSED (notebook 15e).

### 15.10 The Rust solver and its canonical matrix

Notebook 15e showed the method on the smallest state. The Revision record computes every state of the canonical matrix with a compiled program, the **Rust solver** `revision_ks_solver`, whose source is the folder `Revision/kohn_sham/solver` of the repository. Rust is a programming language whose programs are translated once into machine code by its tool cargo and then run much faster than Python; the solver needs no packages from outside the repository, so cargo downloads nothing.

**What is in the program.** The source is split into modules, one file each in `Revision/kohn_sham/solver/src`:

- `theory.rs` reads the theory file `Revision/kohn_sham/ks-theory.json` and the gamma matrices `Revision/algebra/gammas.json` and checks again, in floating point, that the block basis of Chapter 14 really makes every operator of the problem block diagonal (check block_reduction_numeric);
- `shoot.rs` holds the shooting with the Pruefer angle and the safeguarded Newton root of Section 15.3;
- `scf.rs` holds the label sets, the aufbau, the densities and the self-consistent loop with Anderson mixing of Sections 15.4 and 15.5;
- `mermin.rs` finds the chemical potential at a temperature (Section 15.26);
- `analysis.rs` computes the energy-momentum tensor, its identities, the adiabaticity measure and the particle-hole lists;
- `spectrum.rs` computes the free spectra and their exact checks;
- `runs.rs` runs the whole canonical matrix;
- `json.rs`, `sha256.rs`, `report.rs` and `model.rs` write the results deterministically, compute fingerprints, collect the checks and hold the parameters.

**The two ways to run it.** The command `revision_ks_solver all` computes the whole canonical matrix of Section 15.2 and writes it into a folder of results. For each of the 75 ground states it solves the state itself, the same state at the four neighbouring slices $a_{4,0} \pm \delta$ and $a_{4,0} \pm 2\delta$ with $\delta = 0.002$ (for the derivatives along the history), the first excited state (Delta-SCF), the partner state of the rescaling identity (for the 60 states with $a_{4,0} > 0$), and the variant with the exact Fock exchange (for the 60 states with $\lambda \ne 0$); for each of the 135 thermal states it solves the state and its four neighbours at the temperatures $T \pm 0.01T$ and $T \pm 0.02T$ (for the temperature derivatives). It then evaluates its 42 checks, prints each as a line PASS - name or FAIL - name on its error stream, writes them into a report, and prints SUCCESS or FAILURE as the last line of its output stream. The command `revision_ks_solver single` solves one state with chosen parameters ($m$, $\lambda$, $a_{4,0}$, $N$ and, if wanted, $T$) and writes its levels, energies and energy-momentum integrals as a JSON file and, if wanted, its profiles as a CSV file; Notebooks 15b and 15d use it.

**The results.** The folder `Revision/kohn_sham/results` holds the canonical matrix: `parameters.json` (all parameters and the calibration of Section 15.2), `manifest.json` (the list of every result file with its sha256 fingerprint, a 64-digit number computed from the bytes of a file, so that two files with the same fingerprint are identical), `spectrum/` (the free spectra), `ground/` (the 75 ground states: a summary table, the history of every self-consistent loop, the level tables, the profiles of the densities and the energy-momentum tensor at the 151 points $y = -3, -2.98, \dots, 0$, and the integrals of the tensor), `excited/` (Delta-SCF and the particle-hole excitations), `adiabatic/` (Section 15.21), `rescaling/`, `exx/` (the exact-Fock variant) and `thermo/` (the 135 thermal states). Every number is written with 16 significant digits and no time stamp or path, so that a second run writes the same bytes.

**How the record checks itself.** Three reports belong to the solver. `Revision/kohn_sham/reports/ks-rust-solver.json` holds the 42 checks of the run itself, all PASS: the theory input, the free spectra (exact levels, zero mode, band slope, block symmetries, labels, tip angle, rescaling), every state (convergence, particle number, boundary conditions, the two energy forms, the energy-momentum identities, closed shells, completeness of the label sets), the derivatives along the history, the excited states, the exact-Fock variant, the thermodynamics and the chemical potential. `Revision/kohn_sham/reports/ks-rust-determinism.json` (14 checks, all PASS) compares a second run with the canonical one (all 244 files, the 243 result files and the manifest, byte-identical; check repeat_byte_identical) and a **refined run** with twice the RK4 steps and ten times smaller tolerances, against tolerances fixed before the comparison ($10^{-8}$ for levels, energies and thermodynamics, $10^{-6}$ for profiles and derived quantities): for example $E_{KS}$ agrees to $1.9 \times 10^{-12}$ relative (check refined_ground_energies) and 23724 levels agree label by label to $2.1 \times 10^{-9}\,m$ (check refined_eigenvalues). `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` compares every chemical potential with a 40-digit root (Section 15.26). An independent cross-check by a second program written in Python is the subject of Chapter 16.

**Threads.** The solver distributes independent states over the processor cores (at most 22 threads) and merges the results in a fixed order, so the number of threads does not change any output byte. The record's run of the canonical matrix took 78.1 s on an idle machine with 22 threads (`Revision/kohn_sham/solver/README.md`, Timings); the whole Notebook 15a took 164 s and 232 s in its two recorded runs on the machine that built the book, while other programs were running (section 4.5 of `Revision/textbook/notebooks/15a_canonical_matrix.PROVENANCE.md`).

### 15.11 Example: running the canonical matrix (Notebook 15a)

Notebook 15a builds the solver with cargo on the student's computer, runs `revision_ks_solver all` into a folder that git ignores, and checks the new run against the committed record in three ways: the solver's own 42 checks must all pass and match the record's list; the new run must write the same 243 result files (and on the computer that built the book they are byte-identical); and the key numbers must agree within the tolerances that the record fixed in advance. Then it reads the new results and draws eight figures: the levels of $N = 136$ along the history (Figure 15a.1), the gaps (Figure 15a.2), the orbital relaxation of Delta-SCF (Figure 15a.3), the total energies and the interaction shifts (Figure 15a.4), the densities (Figure 15a.5), the self-consistent potentials (Figure 15a.6), the convergence of the self-consistent loop (Figure 15a.7) and the particle-hole excitations (Figure 15a.8). It needs Rust (the run instructions below explain how to install it), takes two to four minutes on a computer with many cores and up to about ten minutes on a laptop, and ends with ALL 25 CHECKS PASSED (notebook 15a).

What to look for: in Figure 15a.1 the blue brane-band levels that fall from slice to slice while the black levels at $k = 0$ stay flat; in Figure 15a.2 the gaps that fall almost, but not quite, like the dashed lines $e^{-a_{4,0}}$; in Figure 15a.5 that the particles sit near the brane although the proper density is largest at the tip.

<!-- NOTEBOOK 15a -->

### 15.14 Line-by-line walk-through of Notebook 15a

The notebook has 16 code cells, In [1] to In [16]. As in Section 15.9, docstrings are left out of the quotations, and long caption strings in calls of `save_figure` are shortened: the quotation shows the first line of the call and the first line of the caption, and then a line `...)` that stands for the rest of the caption and the closing parenthesis; the complete cells are printed in Section 15.13.

**In [1], the set-up cell.** It is the set-up cell of Notebook 15e (explained line by line in Section 15.9), with three differences: the comment lines at the top hold the run instructions of this notebook (Section 15.12), the line `NOTEBOOK_ID = "15a"` names it, and, because this notebook runs a Rust program, it has two more imports and one more function:

```python
import shutil  # finds the program cargo
import subprocess  # runs cargo and the Rust programs
```

`shutil` is a module of Python for files and programs; its function `shutil.which` finds a program on the computer, and `shutil.rmtree` deletes a folder with everything in it. `subprocess` runs another program from Python and collects what it prints.

```python
def rust_program(manifest, binary):
    if shutil.which("cargo") is None:
        raise FileNotFoundError(
            "cargo was not found: install Rust from https://rustup.rs, open a new "
            "terminal, activate the environment and start JupyterLab again")
    crate = (REPO / manifest).parent  # the folder that holds Cargo.toml
```

`rust_program` builds a Rust program and returns where it is. `manifest` is the repository path of the crate's file `Cargo.toml` (a **crate** is a Rust project; `Cargo.toml` describes it), and `binary` is the name of the program. If `shutil.which("cargo")` finds no program cargo, the function stops with a message that says how to install Rust. `crate` is the folder that holds `Cargo.toml` (`.parent` is the folder above a path).

```python
    completed = subprocess.run(
        ["cargo", "build", "--release", "--manifest-path", str(REPO / manifest),
         "--target-dir", str(crate / "target")],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if completed.returncode != 0:  # show the end of cargo's error message
        print(completed.stderr[-3000:])
        raise RuntimeError(f"cargo build failed for {manifest}")
```

`subprocess.run([...])` runs the command given as a list of words: cargo builds the crate in release mode (the fast, optimised translation) into the crate's own folder `target`. `capture_output=True` collects what cargo prints instead of showing it, `text=True` with `encoding="utf-8"` turns it into text, and `errors="replace"` replaces any byte that is not valid text. When cargo has nothing to do (the program is up to date) this takes about a second; the first build takes a minute or two. A program reports success with the **return code** 0; any other code means failure, and then the last 3000 characters of cargo's error stream (`stderr[-3000:]`) are printed and the notebook stops.

```python
    for file_name in (binary, binary + ".exe"):  # Linux and macOS; Windows
        path = crate / "target" / "release" / file_name
        if path.is_file():
            say(f"Rust program {binary} is built and ready.")
            return path
    raise FileNotFoundError(f"cargo built {manifest} but {binary} is missing")
```

The program lies in `target/release`; on Windows its file name ends with `.exe`, on Linux and macOS it has no ending, so both names are tried. The function prints that the program is ready and returns its path.

**In [2], building the solver.**

```python
import csv  # reads the tables (CSV files) that the solver writes
import math  # exp, sqrt and pi for single numbers

import numpy as np  # arrays of numbers

SOLVER_MANIFEST = "Revision/kohn_sham/solver/Cargo.toml"  # the crate of the solver
program = rust_program(SOLVER_MANIFEST, "revision_ks_solver")  # build it, get its path
```

After the imports (Section 15.9, In [2]) the cell builds the solver and keeps the path of the program in `program`.

```python
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # blue, orange, aqua, yellow, magenta, green, ...
SLICE_SHADES = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]  # light->dark
SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]  # the five slices a4,0 of the history
say("Packages imported; colours defined.")
```

`PALETTE` holds eight distinct colours, `SLICE_SHADES` five shades of blue for the five slices (light for the earliest, dark for the latest), and `SLICES` the slices $a_{4,0}$. Out [2] prints that the program is built and the line of the last statement.

**In [3], running the canonical matrix.**

```python
RUN_FOLDER = REPO / "Revision/kohn_sham/solver/target/textbook_15a"  # git ignores it
NEW_RESULTS = RUN_FOLDER / "results"  # the new canonical matrix
NEW_REPORT = RUN_FOLDER / "ks-rust-solver.json"  # the new check report
RUN_FOLDER.mkdir(parents=True, exist_ok=True)
if NEW_RESULTS.exists() and not (NEW_RESULTS / "manifest.json").exists():
    shutil.rmtree(NEW_RESULTS)  # remains of an interrupted run
```

The new run is written into the folder `textbook_15a` inside the solver's build folder `target`, which git ignores; the committed record is never touched. The folder is created if necessary. If a results folder exists without its `manifest.json`, an earlier run was interrupted, and the solver would refuse to write into it; `shutil.rmtree` removes it.

```python
completed = subprocess.run(
    [str(program), "all", "--root", str(REPO), "--out", str(NEW_RESULTS),
     "--report", str(NEW_REPORT)],
    capture_output=True, text=True, encoding="utf-8", errors="replace")
stdout_lines = completed.stdout.strip().split("\n")  # what it printed on stdout
stderr_lines = completed.stderr.split("\n")  # its check lines and timings
```

The solver runs the command `all`. Its option root (written, like every option, with two hyphens in front) tells it where the repository is (it reads the theory file, the gamma matrices and the fixture of 40-digit chemical potentials from there), and the options out and report name the folder of the results and the file of the check report. This is the longest step of the notebook. The printed text is split into lines: `.strip()` removes the blank space at the ends, `.split("\n")` cuts at the line ends.

```python
pass_count = sum(1 for line in stderr_lines if line.startswith("PASS - "))
fail_count = sum(1 for line in stderr_lines if line.startswith("FAIL - "))
say(f"exit code {completed.returncode}, last line {stdout_lines[-1]!r}, "
    f"{pass_count} PASS lines, {fail_count} FAIL lines")
check(completed.returncode == 0 and stdout_lines[-1] == "SUCCESS" and fail_count == 0,
      "the solver ran the whole canonical matrix and reported SUCCESS")
```

`sum(1 for line in ... if ...)` counts the lines that start with PASS - and with FAIL -. The format `!r` prints the last output line with quotes. Out [3] prints exit code 0, the last line SUCCESS, 42 PASS lines and 0 FAIL lines, and the check passes.

**In [4], the solver's check report.**

```python
RECORD_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
new_report = json.loads(NEW_REPORT.read_text(encoding="utf-8"))
old_report = json.loads(repository_file(RECORD_REPORT).read_text(encoding="utf-8"))
groups = {}  # first word of a check name -> [number of checks, number of PASS]
for item in new_report["checks"]:
    group = item["name"].split("_")[0]
    groups.setdefault(group, [0, 0])
    groups[group][0] += 1
    groups[group][1] += item["verdict"] == "PASS"  # True counts as 1
for group, (count, passed) in groups.items():
    say(f"  {group:10} {count:2d} checks, {passed:2d} PASS")
```

The new report and the committed one are read. Each check has a name, a verdict and a detail; the first word of the name (the text before the first underscore) is its group. For each group the cell counts the checks and the passed ones (a comparison gives `True` or `False`, which count as 1 and 0 when added). Out [4] lists the twelve groups, for example free with 7 checks and thermo with 11, all passed.

```python
new_names = [item["name"] for item in new_report["checks"]]
old_names = [item["name"] for item in old_report["checks"]]
summary = new_report["summary"]  # {"checks": ..., "pass": ..., "fail": ...}
report("checks in the new report / PASS / FAIL",
       f"{summary['checks']} / {summary['pass']} / {summary['fail']}")
check(summary == old_report["summary"] and summary["fail"] == 0
      and summary["pass"] == summary["checks"] == len(new_names),
      f"the new report holds the {summary['checks']} checks of the record, all PASS",
      record=f"{RECORD_REPORT}, summary")
check(new_names == old_names, "the new report has the same checks as the record")
report("new report byte-identical to the record",
       NEW_REPORT.read_bytes() == repository_file(RECORD_REPORT).read_bytes())
```

The lists of check names of the two reports and the summary of the new one are formed. The first check requires the same summary as the record, no failure, and as many passes as checks; the number 42 is not typed into the notebook but read from the report. The second requires the same check names in the same order. The last line compares the two report files byte for byte (`read_bytes` reads a file as raw bytes); Out [4] prints True: on the computer that built the book the new report is identical to the record. On another computer the last digits of some reported deviations may differ, which is why this is a RESULT and not a check.

**In [5], every result file.**

```python
RECORD_RESULTS = "Revision/kohn_sham/results"


def manifest_of(folder):
    data = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    return {entry["path"]: entry["sha256"] for entry in data["files"]}


old_manifest = manifest_of(repository_file(RECORD_RESULTS))
new_manifest = manifest_of(NEW_RESULTS)
check(sorted(old_manifest) == sorted(new_manifest),
      f"the new run wrote the same {len(old_manifest)} result files as the record",
      record=f"{RECORD_RESULTS}/manifest.json")
same = sum(1 for path in old_manifest if new_manifest[path] == old_manifest[path])
report("result files byte-identical to the record", f"{same} of {len(old_manifest)}")
```

`manifest_of` reads a manifest and returns a dictionary from each file path to its sha256 fingerprint. `sorted(old_manifest)` is the sorted list of the paths; the check requires the same set of files. `same` counts the files whose fingerprints agree. Out [5]: the same 243 result files, all 243 byte-identical to the record.

**In [6], the numerical comparison.**

```python
def read_table(folder, name):
    with open(folder / name, newline="", encoding="utf-8") as handle:
        return {row["id"]: row for row in csv.DictReader(handle)}
```

`read_table` reads a CSV table of the results and files its rows under the state name in the column `id`.

```python
def worst(table, columns, relative):
    new = read_table(NEW_RESULTS, table)
    old = read_table(repository_file(RECORD_RESULTS), table)
    assert sorted(new) == sorted(old), f"{table}: the state lists differ"
    largest = 0.0
    for key in old:
        for column in columns:
            a, b = float(new[key][column]), float(old[key][column])
            scale = max(abs(b), 1.0) if relative else 1.0
            largest = max(largest, abs(a - b) / scale)
    return largest
```

`worst` returns the largest difference between the new run and the record in the given columns of a table, over all states. The `assert` statement stops with the given message if the two tables do not list the same states (a safety net inside a helper, not one of the notebook's checks). For a relative comparison each difference is divided by the larger of $|b|$ and 1, so that numbers near zero are compared absolutely.

```python
COMPARISONS = [  # (table, columns, relative?, tolerance, what)
    ("ground/summary.csv", ["E_KS"], True, 1e-8, "ground-state energies"),
    ("ground/summary.csv", ["HOMO", "LUMO", "KS_gap"], False, 1e-8,
     "HOMO, LUMO and gaps"),
    ("excited/summary.csv", ["delta_SCF"], False, 1e-8, "Delta-SCF energies"),
    ("thermo/thermodynamics.csv", ["mu", "E", "entropy", "F"], True, 1e-8,
     "thermodynamics"),
    ("adiabatic/adiabaticity.csv", ["Q_max"], True, 1e-6, "adiabaticity Q_max"),
]
for table, columns, relative, tolerance, what in COMPARISONS:
    largest = worst(table, columns, relative)
    report(f"largest difference, {what}", f"{largest:.1e}")
    check(largest <= tolerance, f"{what} agree with the record within {tolerance:.0e}",
          record=f"{RECORD_RESULTS}/{table}")
```

`COMPARISONS` lists five comparisons, each a tuple (a fixed group of values in parentheses): the table, its columns, whether the comparison is relative, the tolerance (the values fixed in advance in `Revision/kohn_sham/reports/ks-rust-determinism.json`) and a description. The loop unpacks each tuple into five names, computes the largest difference, reports it and checks it. Out [6] reports 0.0 for all five and five PASS lines: on this computer the new numbers are exactly the recorded ones.

**In [7], the ground states along the history.**

```python
ground = read_table(NEW_RESULTS, "ground/summary.csv")  # the 75 ground states
excited = read_table(NEW_RESULTS, "excited/summary.csv")  # their Delta-SCF


def state_id(n, tag, a4):
    return f"N{n}_{tag}_a{round(10 * a4):02d}"
```

From here on the notebook reads the new results. `state_id` builds the solver's name of a state: `round(10 * a4)` is ten times the slice as a whole number, and the format `02d` writes it with two digits, so $N = 136$, `lam0`, $a_{4,0} = 1$ gives `N136_lam0_a10`.

```python
say("   N  a4,0        E_KS        HOMO        LUMO     KS gap")
for n in (8, 136, 688):
    for a4 in SLICES:
        row = ground[state_id(n, "lam0", a4)]
        say(f"{n:4d}  {a4:4.1f}  {float(row['E_KS']):10.5f}  {float(row['HOMO']):10.6f}"
            f"  {float(row['LUMO']):10.6f}  {float(row['KS_gap']):9.6f}")
report("KS gap of N = 8 at a4,0 = 0, 1, 2", ", ".join(
    f"{float(ground[state_id(8, 'lam0', a)]['KS_gap']):.7f}" for a in (0, 1, 2)))
```

For the three particle numbers without interaction and the five slices the cell prints a table of $E_{KS}$, the HOMO, the LUMO and the gap, and then the gap of $N = 8$ at $a_{4,0} = 0, 1, 2$ with seven digits. Out [7] is the table of Section 15.15. For $N = 8$ the energy is exactly 0 at every slice (the zero modes have $\varepsilon = 0$ and there is no interaction), and the gaps are $0.4307337$, $0.1703493$, $0.0641594$.

**In [8], the levels along the history.**

```python
def read_levels(n, tag, a4):
    path = NEW_RESULTS / "ground/levels" / f"{state_id(n, tag, a4)}.csv"
    with open(path, newline="", encoding="utf-8") as handle:
        return {(int(r["n2"]), int(r["j"]), r["parity"], int(r["label"])):
                (float(r["eps"]), float(r["f"])) for r in csv.DictReader(handle)}
```

`read_levels` reads the level table of one state and returns a dictionary whose key is the **key** of a level, the four numbers (shell $n_2$, block type $j$, parity, Pruefer label $l$), and whose value is the pair (level, occupation).

```python
levels = [read_levels(136, "lam0", a4) for a4 in SLICES]  # one dictionary per slice
THEORY = json.loads(repository_file("Revision/kohn_sham/ks-theory.json").read_text(
    encoding="utf-8"))  # the theory file of the solver
C_SLOPE = float(THEORY["checksNumeric"]["braneBandSlope_M1_H1_L3_a0"])  # c
fig, ax = plt.subplots(figsize=(7.5, 5.0))
all_keys = sorted(set().union(*levels))
```

`levels` holds the level tables of $N = 136$, $\lambda = 0$ at the five slices. `C_SLOPE` is the band slope $c$ from the theory file. `set().union(*levels)` is the set of all keys that occur at any slice (a **set** is a collection without repetitions), sorted into a list.

```python
for key in all_keys:
    points = [(a4, lv[key]) for a4, lv in zip(SLICES, levels) if key in lv]
    xs = [p[0] for p in points]
    es = [p[1][0] for p in points]
    if min(es) > 1.6:
        continue  # only the part of the spectrum near the Fermi level
    band = key[1] == 1 and key[2] == "even" and key[3] == 0 and key[0] >= 1
    colour = PALETTE[0] if band else ("black" if key[0] == 0 else "0.6")
    ax.plot(xs, es, "-", color=colour, lw=1.0, alpha=0.8)
    for x, (e, f) in points:
        ax.plot([x], [e], "o", ms=5, color=colour,
                markerfacecolor=colour if f > 0.5 else "white")
```

For each key the cell collects the slices at which the level exists (the label sets differ a little from slice to slice) with its level and occupation. Levels that stay above $1.6\,m$ are skipped (`continue` jumps to the next key). A key belongs to the brane band if it is $j = +1$, even, label 0 and $n_2 \ge 1$; band levels are drawn blue, levels at $k = 0$ black and all others grey. Each level is drawn as a thin line through its points, and each point as a dot that is filled when the level is occupied ($f > 0.5$) and open (white inside) when it is empty.

```python
a_fine = np.linspace(0.0, 2.0, 101)
ax.plot(a_fine, C_SLOPE * 0.25 * np.exp(-a_fine), "--", color=PALETTE[1], lw=1.5,
        label="$c\\,k\\,e^{-a_{4,0}}$ for $k = 0.25$")
ax.plot([], [], "o-", color=PALETTE[0], label="brane band ($j=+1$, even, $l=0$)")
ax.plot([], [], "o-", color="black", label="levels at $k = 0$")
ax.plot([], [], "o-", color="0.6", label="other levels")
ax.plot([], [], "o", color="0.3", markerfacecolor="white", label="open: empty")
ax.set_ylim(-0.05, 1.6)
ax.set_xlabel("slice $a_{4,0}$ of the history")
ax.set_ylabel("level $\\varepsilon$ (units of $m$)")
ax.set_title("Kohn-Sham levels of $N = 136$, $\\lambda = 0$, along the history")
ax.legend(fontsize=8, loc="center right")
save_figure(fig, "levels_history",
            "Kohn-Sham levels $\\varepsilon$ (vertical axis, units of $m$) of the "
...)
```

`a_fine` holds 101 slices from 0 to 2; the dashed orange curve is the small-$k$ law $c\,k\,e^{-a_{4,0}}$ for the first shell. The empty plots make the legend entries, and the remaining lines set the range, labels and title and save Figure 15a.1.

```python
k0_keys = [key for key in levels[0] if key[0] == 0]
k0_spread = max(abs(lv[key][0] - levels[0][key][0]) for lv in levels for key in k0_keys)
band_keys = [key for key in all_keys if all(key in lv for lv in levels)
             and key[1] == 1 and key[2] == "even" and key[3] == 0 and key[0] >= 1]
decreasing = all(levels[i + 1][key][0] < levels[i][key][0]
                 for key in band_keys for i in range(4))
report("number of brane-band levels followed through all five slices", len(band_keys))
check(k0_spread <= 1e-12, "the k = 0 levels are the same at every slice")
check(decreasing, "every brane-band level decreases strictly along the history")
```

`k0_spread` is the largest change of a level at $k = 0$ between the first slice and any other. `band_keys` are the band levels present at all five slices, and `decreasing` is true when each of them is lower at each slice than at the previous one (`all(...)` is true when every comparison is true). Out [8]: 8 band levels are followed through all slices, the $k = 0$ levels do not move, and every band level falls; both are consequences of the rescaling identity (Section 15.4). In Figure 15a.1 the lowest blue level (the first shell) lies below the dashed curve at $a_{4,0} = 0$, where the momentum $0.25$ is not yet small enough for the straight-line law, and approaches it along the history as the redshifted momentum shrinks.

**In [9], the gaps.**

```python
fig, ax = plt.subplots()
for colour, n in zip(PALETTE, (8, 136, 688)):
    gaps = [float(ground[state_id(n, "lam0", a4)]["KS_gap"]) for a4 in SLICES]
    ax.plot(SLICES, gaps, "o-", color=colour, lw=1.5, label=f"$N = {n}$")
    ax.plot(a_fine, gaps[0] * np.exp(-a_fine), "--", color=colour, lw=1.0)
ax.set_yscale("log")
ax.set_xlabel("slice $a_{4,0}$ of the history")
ax.set_ylabel("Kohn-Sham gap $\\Delta_{KS}$ (units of $m$)")
ax.set_title("The gap closes along the history (dashed: $\\propto e^{-a_{4,0}}$)")
ax.legend()
save_figure(fig, "gaps_history",
            "Kohn-Sham gap $\\Delta_{KS}$ (vertical axis, logarithmic, units of $m$) "
...)
```

For each particle number the gaps at the five slices are drawn as dots joined by lines, with a dashed curve $\Delta(0)\,e^{-a_{4,0}}$ through the first point; `set_yscale("log")` makes the vertical axis logarithmic, on which $e^{-a_{4,0}}$ is a straight line. This is Figure 15a.2.

```python
free_dscf = max(abs(float(excited[state_id(n, "lam0", a)]["delta_SCF_minus_gap"]))
                for n in (8, 136, 688) for a in SLICES)
report("largest |Delta-SCF - gap| without interaction", f"{free_dscf:.1e}")
check(free_dscf <= 1e-10, "Delta-SCF equals the gap without interaction",
      record=f"{RECORD_REPORT}, check excited_delta_scf_free_equals_gap")
shrinking = all(float(ground[state_id(n, "lam0", SLICES[i + 1])]["KS_gap"])
                < float(ground[state_id(n, "lam0", SLICES[i])]["KS_gap"])
                for n in (8, 136, 688) for i in range(4))
check(shrinking, "every gap shrinks from slice to slice")
```

`free_dscf` is the largest $|\Delta_{SCF} - \Delta_{KS}|$ of the 15 free states; Out [9] gives $2.0 \times 10^{-11}$, the value of the record's check, below its tolerance $10^{-10}$. The second check confirms that every gap shrinks from slice to slice.

**In [10], the orbital relaxation.**

```python
fig, axes = plt.subplots(1, 3, figsize=(10.0, 3.8), sharey=True,
                         layout="constrained")
for ax, n in zip(axes, (8, 136, 688)):
    for colour, tag, label in zip(PALETTE, ("lamp1", "lamm1", "lamp2", "lamm2"),
                                  ("$+\\lambda_1$", "$-\\lambda_1$", "$+\\lambda_2$",
                                   "$-\\lambda_2$")):
        diff = [float(excited[state_id(n, tag, a)]["delta_SCF_minus_gap"])
                for a in SLICES]
        ax.plot(SLICES, diff, "o-", color=colour, lw=1.5, label=label)
    ax.set_yscale("symlog", linthresh=1e-9)
    ax.set_title(f"$N = {n}$")
    ax.set_xlabel("slice $a_{4,0}$")
axes[0].set_ylabel("$\\Delta_{SCF} - \\Delta_{KS}$ (units of $m$)")
axes[0].legend(fontsize=8)
```

Three panels, one per particle number; in each, the relaxation $\Delta_{SCF} - \Delta_{KS}$ of the four interacting couplings at the five slices. The **symmetric logarithmic** axis (`"symlog"`) is logarithmic for large values of either sign and linear between $-10^{-9}$ and $10^{-9}$ (`linthresh`), so that small values of both signs fit on one axis.

```python
largest_id = max(excited, key=lambda i: abs(float(excited[i]["delta_SCF_minus_gap"])))
largest_relax = abs(float(excited[largest_id]["delta_SCF_minus_gap"]))
mantissa, power = f"{largest_relax:.1e}".split("e")  # e.g. "5.5", "-04"
save_figure(fig, "delta_scf",
            "Orbital relaxation: the Delta-SCF excitation energy minus the Kohn-Sham "
...)
report("largest |Delta-SCF - gap| over the 75 states",
       f"{largest_relax:.3e} ({largest_id})")
check(largest_id == "N688_lamp2_a00",
      "the largest relaxation belongs to N = 688, +lambda_2, a4,0 = 0 (the caption)")
check(largest_relax < 1e-3, "the orbital relaxation is below 0.001 m in every state")
```

`max(excited, key=...)` returns the state name whose relaxation has the largest size. The number is written in the format `.1e` and split at the letter e into the digits and the power of ten, which the caption of Figure 15a.3 prints as $5.5 \times 10^{-4}$ (so the caption's number is computed, not typed). Out [10]: the largest relaxation is $5.496 \times 10^{-4}\,m$, in `N688_lamp2_a00`, where the lowest empty level is the bulk level at $k = 0$, and every relaxation is below $0.001\,m$.

**In [11], the total energy.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
for colour, n in zip(PALETTE, (136, 688)):
    energies = [float(ground[state_id(n, "lam0", a)]["E_KS"]) for a in SLICES]
    left.plot(SLICES, energies, "o-", color=colour, lw=1.5, label=f"$N = {n}$")
left.set_yscale("log")
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("$E_{KS}$ (units of $m$)")
left.set_title("Energy without interaction")
left.legend()
```

The left panel draws $E_{KS}$ of the free states $N = 136$ and $688$ at the five slices on a logarithmic axis.

```python
tags = ("lamp2", "lamp1", "lamm1", "lamm2")
labels = ("$+\\lambda_2$", "$+\\lambda_1$", "$-\\lambda_1$", "$-\\lambda_2$")
largest_shift = 0.0  # the largest |E(lambda) - E(0)| of N = 136
for colour, tag, label in zip(PALETTE, tags, labels):
    shift = [float(ground[state_id(136, tag, a)]["E_KS"])
             - float(ground[state_id(136, "lam0", a)]["E_KS"]) for a in SLICES]
    largest_shift = max([largest_shift] + [abs(s) for s in shift])
    right.plot(SLICES, shift, "o-", color=colour, lw=1.5, label=label)
e136 = [float(ground[state_id(136, "lam0", a)]["E_KS"]) for a in SLICES]
right.axhline(0.0, color="0.4", lw=0.8)
right.set_xlabel("slice $a_{4,0}$")
right.set_ylabel("$E_{KS}(\\lambda) - E_{KS}(0)$ (units of $m$)")
right.set_title("Interaction energy shift, $N = 136$")
right.legend(fontsize=8)
save_figure(fig, "energy_history",
            "Left: the Kohn-Sham energy $E_{KS}$ (vertical axis, logarithmic, units "
...)
```

The right panel draws, for $N = 136$, the change $E_{KS}(\lambda) - E_{KS}(0)$ of the four couplings at the five slices, and keeps the largest size of these changes in `largest_shift` (the list `[largest_shift] + [...]` joins the old largest value with the new sizes). `e136` are the free energies of $N = 136$; the caption of Figure 15a.4 prints their smallest and largest value and `largest_shift`.

```python
report("largest |E(lambda) - E(0)| of N = 136", f"{largest_shift:.4f}")
ordered = all(
    float(ground[state_id(n, "lamp2", a)]["E_KS"])
    > float(ground[state_id(n, "lamp1", a)]["E_KS"])
    > float(ground[state_id(n, "lam0", a)]["E_KS"])
    > float(ground[state_id(n, "lamm1", a)]["E_KS"])
    > float(ground[state_id(n, "lamm2", a)]["E_KS"])
    for n in (136, 688) for a in SLICES)
check(ordered, "E(+lambda2) > E(+lambda1) > E(0) > E(-lambda1) > E(-lambda2), "
               "N = 136 and 688")
falling = all(float(ground[state_id(n, "lam0", SLICES[i + 1])]["E_KS"])
              < float(ground[state_id(n, "lam0", SLICES[i])]["E_KS"])
              for n in (136, 688) for i in range(4))
check(falling, "the energy of N = 136 and 688 falls from slice to slice")
```

Out [11]: the largest shift is $0.0318\,m$, out of energies from 12 to $80\,m$. Python allows a chain of comparisons, `a > b > c`, which is true when every neighbouring pair is ordered; the first check confirms that repulsion raises and attraction lowers the energy, more for the stronger coupling, at every slice for $N = 136$ and $688$. The second confirms that the free energies fall from slice to slice. For $N = 8$ the order is reversed (the text cell before the code cell explains why, and Section 15.5 gives the exact symmetry).

**In [12], the densities.**

```python
VOL7 = (2.0 * math.pi / 0.25) ** 3  # proper 7-volume per unit e^{6Hy} (v_t = 1)


def read_profile(n, tag, a4):
    path = NEW_RESULTS / "ground/profiles" / f"{state_id(n, tag, a4)}.csv"
    data = np.genfromtxt(path, delimiter=",", names=True)
    return {name: data[name] for name in data.dtype.names}
```

`read_profile` reads the profile table of a state with `np.genfromtxt`, which turns a CSV file into an array whose columns can be addressed by the names in the first line (`names=True`); the function returns a dictionary from each column name (`y`, `n`, `S`, `M_eff`, `v_v`, `rho`, `p3`, ...) to its array of 151 values.

```python
def simpson(values, step):
    weights = np.full(len(values), 2.0)
    weights[1::2] = 4.0
    weights[0] = weights[-1] = 1.0
    return step / 3.0 * float(np.sum(weights * values))
```

`simpson` is Simpson's rule for an odd number of equally spaced values: weights 1, 4, 2, 4, ..., 4, 1 times $h/3$ (`np.full(n, 2.0)` is an array of $n$ twos).

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
counts = []
for shade, a4 in zip((SLICE_SHADES[0], SLICE_SHADES[2], SLICE_SHADES[4]), (0, 1, 2)):
    prof = read_profile(136, "lam0", a4)
    y = prof["y"]
    per_y = 2.0 * VOL7 * np.exp(6.0 * y) * prof["n"]  # particles per unit y
    counts.append(simpson(per_y, y[1] - y[0]))
    left.plot(y, prof["n"], color=shade, lw=1.8, label=f"$a_{{4,0}} = {a4}$")
    right.plot(y, per_y, color=shade, lw=1.8, label=f"$a_{{4,0}} = {a4}$")
```

For $N = 136$, $\lambda = 0$ at the slices 0, 1, 2 the cell reads the profile, forms the number of particles per unit $y$ in the doubled box, $2\,\mathrm{Vol}_7\,e^{6Hy}n(y)$, integrates it with Simpson's rule (the spacing is `y[1] - y[0]` $= 0.02$), and draws the proper density on the left and the particles per unit $y$ on the right.

```python
left.set_yscale("log")
left.set_xlabel("hidden coordinate $y$ (tip at $-3$, brane at $0$)")
left.set_ylabel("proper density $n(y)$")
left.set_title("Proper number density")
right.set_xlabel("hidden coordinate $y$")
right.set_ylabel("particles per unit $y$")
right.set_title("$2\\,\\mathrm{Vol}_7\\, e^{6Hy} n(y)$, area $= N$")
right.legend()
save_figure(fig, "densities",
            "Left: the proper number density $n(y)$ (vertical axis, logarithmic, "
...)
report("particle number from the profiles at a4,0 = 0, 1, 2",
       ", ".join(f"{c:.6f}" for c in counts))
check(max(abs(c - 136.0) for c in counts) < 1e-5,
      "Simpson's rule on the profiles gives N = 136 at every slice",
      record=f"{RECORD_REPORT}, check ground_N_conservation")
```

After the labels, `save_figure` saves Figure 15a.5. Out [12] gives $136.000002$ at all three slices: the integral of the coarse 151-point profile reproduces $N$ to $2 \times 10^{-6}$ (the solver's own check ground_N_conservation, on its fine grid, gives $1.5 \times 10^{-15}$).

**In [13], the self-consistent potentials.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
ratios = []  # profile maximum / recorded maximum, one per slice
for shade, a4 in zip(SLICE_SHADES, SLICES):
    prof = read_profile(136, "lamp2", a4)
    left.plot(prof["y"], prof["M_eff"] - 1.0, color=shade, lw=1.8,
              label=f"$a_{{4,0}} = {a4}$")
    right.plot(prof["y"], prof["v_v"], color=shade, lw=1.8)
    recorded = float(ground[state_id(136, "lamp2", a4)]["max_abs_Meff_minus_m"])
    ratios.append(float(np.max(np.abs(prof["M_eff"] - 1.0))) / recorded)
```

For $N = 136$ with $+\lambda_2$ the cell draws $M - m$ (left) and $v$ (right) at the five slices, and for each slice divides the largest $|M - m|$ on the 151 profile points by the largest value that the solver recorded on its 1801 fine points.

```python
left.set_xlabel("hidden coordinate $y$")
left.set_ylabel("$M(y) - m$ (units of $m$)")
left.set_title("Mass shift, $N = 136$, $+\\lambda_2$")
left.legend(fontsize=8)
right.set_xlabel("hidden coordinate $y$")
right.set_ylabel("$v(y)$ (units of $m$)")
right.set_title("Exchange potential, $N = 136$, $+\\lambda_2$")
m_max = [float(ground[state_id(136, "lamp2", a4)]["max_abs_Meff_minus_m"])
         for a4 in SLICES]  # the solver's largest |M - m| at each slice
v_max = [float(ground[state_id(136, "lamp2", a4)]["max_abs_v_v"]) for a4 in SLICES]
peak = int(np.argmax(m_max))  # the slice where |M - m| is largest
save_figure(fig, "potentials",
            "The self-consistent mass shift $M(y) - m$ (left) and potential $v(y)$ "
...)
```

`m_max` and `v_max` are the recorded largest $|M - m|$ and $|v|$ at the five slices, and `np.argmax` gives the position of the largest entry of `m_max`. The caption of Figure 15a.6 prints these numbers.

```python
report("profile maximum / recorded maximum of |M - m|",
       ", ".join(f"{r:.5f}" for r in ratios))
check(all(0.998 <= r <= 1.0 + 1e-12 for r in ratios),
      "the profile maxima of |M - m| lie within 0.2 percent below the recorded ones",
      record=f"{RECORD_RESULTS}/ground/summary.csv, column max_abs_Meff_minus_m")
report("largest |M - m| at the five slices", ", ".join(f"{v:.3f}" for v in m_max))
report("largest |v| at the five slices", ", ".join(f"{v:.3f}" for v in v_max))
check(all(v_max[i + 1] > v_max[i] for i in range(4)) and SLICES[peak] == 1.5
      and max(m_max + v_max) < 0.4,
      "|v| grows at every slice, |M - m| peaks at a4,0 = 1.5, both stay below 0.4 m",
      record=f"{RECORD_RESULTS}/ground/summary.csv, columns max_abs_Meff_minus_m "
             "and max_abs_v_v")
```

Every profile point is also a point of the fine grid, so the profile maximum cannot exceed the recorded one; it is smaller when the true maximum lies between two profile points. Out [13]: the ratios lie between 0.99891 and 0.99997; the largest $|M - m|$ is $0.008$, $0.050$, $0.192$, $0.355$, $0.310\,m$ and the largest $|v|$ is $0.015$, $0.021$, $0.059$, $0.157$, $0.242\,m$ at the five slices. Both checks pass (`m_max + v_max` joins the two lists into one).

**In [14], the convergence of the loop.**

```python
runs = json.loads((NEW_RESULTS / "ground/runs.json").read_text(encoding="utf-8"))
by_id = {run["id"]: run for run in runs}
fig, ax = plt.subplots()
styles = {"lamp2": "-", "lamm2": "--"}
for colour, n in zip(PALETTE, (8, 136, 688)):
    for tag, style in styles.items():
        history = by_id[state_id(n, tag, 2.0)]["scfHistory_iteration_residual_E"]
        ax.plot([h[0] for h in history], [h[1] for h in history], style, marker="o",
                ms=4, color=colour, lw=1.5,
                label=f"$N = {n}$, {'+' if tag == 'lamp2' else '-'}$\\lambda_2$")
```

`runs.json` is a list with one entry per ground state; `by_id` files them under their names. For the strongest couplings $\pm\lambda_2$ at the last slice (the hardest cases) the residual of every iteration is drawn, solid for $+\lambda_2$ and dashed for $-\lambda_2$.

```python
ax.axhline(1e-11, color="0.3", ls=":", lw=1.2, label="tolerance $10^{-11}$")
ax.set_yscale("log")
ax.set_xlabel("iteration")
ax.set_ylabel("residual: largest change of the potential (units of $m$)")
ax.set_title("Anderson mixing, $a_{4,0} = 2$, couplings $\\pm\\lambda_2$")
ax.legend(fontsize=8, ncol=2)
save_figure(fig, "scf_convergence",
            "Convergence of the self-consistent loop with Anderson mixing: the "
...)
direct = all(run["path"] == "direct" for run in runs)
final = max(run["scfHistory_iteration_residual_E"][-1][1] for run in runs)
longest = max(run["iterations"] for run in runs)
report("largest final residual / largest number of iterations",
       f"{final:.2e} / {longest}")
check(len(runs) == 75 and direct and final <= 1e-11,
      "all 75 ground states converged directly below the tolerance 1e-11",
      record=f"{RECORD_REPORT}, check ground_scf_converged")
```

After the tolerance line and the labels (`ncol=2` puts the legend in two columns), `save_figure` saves Figure 15a.7. `direct` is true when every run took the path `direct` (no fallback was needed), `final` is the largest last residual and `longest` the largest number of iterations. Out [14]: $9.34 \times 10^{-12}$ and 17, and the check passes. In the figure the curves of $N = 8$ for $+\lambda_2$ and $-\lambda_2$ coincide, as the exact symmetry of Section 15.5 predicts.

**In [15], the particle-hole excitations.**

```python
TAGS = ("lam0", "lamp1", "lamm1", "lamp2", "lamm2")  # the five couplings


def read_pairs(n, tag, a4):
    path = NEW_RESULTS / "excited/particle-hole" / f"{state_id(n, tag, a4)}.csv"
    with open(path, newline="", encoding="utf-8") as handle:
        return {(r["hole_levels"], r["particle_levels"]):
                (float(r["delta_eps"]), float(r["multiplicity"]), r["same_sector"])
                for r in csv.DictReader(handle)}


lists = {(n, tag, a4): read_pairs(n, tag, a4)
         for n in (8, 136, 688) for tag in TAGS for a4 in SLICES}  # 75 states
```

`read_pairs` reads the list of the lowest particle-hole excitations of a state: the key is the pair (hole levels, particle levels), each written `n2:j:parity:label`, and the value is the excitation energy $\Delta\varepsilon = \varepsilon_{particle} - \varepsilon_{hole}$, the multiplicity $g_{hole}\,g_{particle}$ and the word `true` or `false` that says whether the two levels lie in the same sector. `lists` holds these lists for all 75 ground states.

```python
fig, ax = plt.subplots()
for a4 in SLICES:
    values = list(lists[(136, "lam0", a4)].values())
    ax.scatter([a4] * len(values), [v[0] for v in values],
               s=[v[1] / 40.0 for v in values],  # marker area ~ multiplicity
               color=PALETTE[0], alpha=0.3, edgecolors=PALETTE[0])
lowest = [min(v[0] for v in lists[(136, "lam0", a4)].values()) for a4 in SLICES]
ax.plot(SLICES, lowest, "o-", color=PALETTE[1], lw=1.8, ms=5,
        label="lowest excitation (the Kohn-Sham gap)")
ax.plot(a_fine, lowest[0] * np.exp(-a_fine), "--", color="0.4", lw=1.0,
        label="$\\propto e^{-a_{4,0}}$")
```

`ax.scatter` draws markers whose areas are given by `s`: here the multiplicity divided by 40, so a larger marker is a more degenerate excitation. For $N = 136$ without interaction all listed excitations are drawn at their slice, the lowest excitation of each slice is joined by an orange line, and a dashed curve falls like $e^{-a_{4,0}}$ from the first one.

```python
ax.scatter([], [], s=60, color=PALETTE[0], alpha=0.3, edgecolors=PALETTE[0],
           label="excitations (area: multiplicity)")
ax.set_yscale("log")
ax.set_xlabel("slice $a_{4,0}$ of the history")
ax.set_ylabel("excitation energy $\\Delta\\varepsilon$ (units of $m$)")
ax.set_title("Particle-hole excitations of $N = 136$, $\\lambda = 0$")
ax.legend(fontsize=8, loc="lower left")
save_figure(fig, "particle_hole",
            "The lowest particle-hole excitation energies (vertical axis, "
...)
```

A legend entry, the axes and `save_figure` for Figure 15a.8.

```python
lowest_is_gap = all(
    abs(min(v[0] for v in lists[key].values())
        - float(ground[state_id(*key)]["KS_gap"])) <= 1e-12 for key in lists)
cheaper = True
for n in (8, 136, 688):
    for tag in TAGS:
        series = [lists[(n, tag, a4)] for a4 in SLICES]
        common = set(series[0]).intersection(*series[1:])  # listed at every slice
        cheaper = cheaper and all(series[i + 1][key][0] < series[i][key][0]
                                  for key in common for i in range(4))
```

`lowest_is_gap` is true when in every state the lowest listed excitation equals the Kohn-Sham gap (`state_id(*key)` unpacks the triple $(N, \text{tag}, a_{4,0})$ into the three arguments). For each of the 15 series (particle number and coupling), `common` is the set of excitations listed at all five slices (`intersection` keeps what all sets share), and `cheaper` stays true only if each of them is cheaper at each slice than at the previous one.

```python
count = sum(len(pairs) for pairs in lists.values())
inside = sum(1 for pairs in lists.values() for v in pairs.values() if v[2] != "false")
jumps = [float(row["Q_max_delta_eps"]) for row in
         read_table(NEW_RESULTS, "adiabatic/adiabaticity.csv").values()
         if row["Q_max_delta_eps"] != "null"]  # null: no jump (N = 8)
report("particle-hole excitations listed / inside one sector", f"{count} / {inside}")
report("lowest excitation of N = 136 at a4,0 = 0 and 2",
       f"{lowest[0]:.5f}, {lowest[-1]:.5f}")
report("energy of the largest-Q jump inside a sector (smallest, largest)",
       f"{min(jumps):.3f}, {max(jumps):.3f}")
```

`count` is the number of listed excitations of all 75 states, and `inside` the number of those whose two levels lie in one sector. `jumps` collects, from the adiabaticity table, the energy of the jump with the largest adiabaticity number $Q$ in each state (Section 15.21); for $N = 8$ there is no such jump and the table says `null`. Out [15]: 1610 excitations, none inside one sector; the lowest excitation of $N = 136$ falls from $0.08267$ to $0.01446$; the in-sector jumps cost between $1.488$ and $2.253\,m$.

```python
check(lowest_is_gap, "in all 75 states the lowest particle-hole energy is the KS gap",
      record=f"{RECORD_RESULTS}/excited/particle-hole and ground/summary.csv")
check(cheaper, "every excitation listed at all five slices gets cheaper along the "
               "history")
check(count >= len(lists) and inside == 0,
      f"none of the {count} listed excitations stays inside one sector",
      record=f"{RECORD_RESULTS}/excited/particle-hole, column same_sector")
```

The three checks pass. The meaning of the third: the exact evolution along the history keeps the momentum, the block type and the parity of every orbital (Section 15.21), so the motion of the background alone cannot create any of the 1610 excitations; it can only cause jumps inside a sector, and the jump with the largest $Q$ costs between $1.488\,m$ and $2.253\,m$.

**In [16], the last check.**

```python
NAMES = ["levels_history", "gaps_history", "delta_scf", "energy_history",
         "densities", "potentials", "scf_convergence",
         "particle_hole"]  # the figures, in order
missing = [name for number, name in enumerate(NAMES, start=1)
           if not output_file(f"{FIGURE_FOLDER}/15a_{number}_{name}.png").is_file()]
check(missing == [], "every figure file of this notebook exists")
all_checks_passed()
```

The same as In [15] of Notebook 15e (Section 15.9), with the eight figure names of this notebook in order (the comment says so) and the file names `15a_<number>_<name>.png`: `enumerate(NAMES, start=1)` pairs each name with its number, the list comprehension collects the names whose file does not exist, the check requires that list to be empty, and `all_checks_passed()` prints the last line. The cell prints PASS every figure file of this notebook exists and ALL 25 CHECKS PASSED (notebook 15a).

### 15.15 What the canonical matrix shows

All numbers of this section are COMPUTED by the Rust solver and reproduced by Notebook 15a; the cell is named with each.

**The ground states without interaction** (Notebook 15a, Out [7]; `Revision/kohn_sham/results/ground/summary.csv`):

| $N$ | $a_{4,0}$ | $E_{KS}$ | HOMO | LUMO | $\Delta_{KS}$ |
| --- | --- | --- | --- | --- | --- |
| 8 | 0 | 0 | 0 | 0.430734 | 0.430734 |
| 8 | 1 | 0 | 0 | 0.170349 | 0.170349 |
| 8 | 2 | 0 | 0 | 0.064159 | 0.064159 |
| 136 | 0 | 80.28222 | 0.799646 | 0.882320 | 0.082674 |
| 136 | 1 | 32.38412 | 0.325768 | 0.360757 | 0.034989 |
| 136 | 2 | 12.44507 | 0.126766 | 0.141223 | 0.014457 |
| 688 | 0 | 680.44125 | 1.247113 | 1.292293 | 0.045180 |
| 688 | 1 | 279.42489 | 0.515229 | 0.535712 | 0.020484 |
| 688 | 2 | 110.38667 | 0.205760 | 0.214370 | 0.008610 |

How to read it. For $N = 8$ the eight particles sit in the zero modes at $\varepsilon = 0$, so $E_{KS} = 0$ at every slice, and the gap is the first band level (Section 15.4). For $N = 136$ the HOMO is the band level of the shell $n_2 = 4$ and the LUMO that of $n_2 = 5$; both redshift, and the energy, the sum of $g\varepsilon$ over the occupied band levels, falls from $80.28$ to $12.45$, by a factor $6.45$. For $N = 688$ at $a_{4,0} = 0$ the LUMO is $1.292293$, the bulk level at $k = 0$, which does not move; at later slices the band levels of the shells 12 and higher have come down below it, and the LUMO is again a band level. (Section 15.21 shows that a filling of $N = 696$ would cross the Fermi level for this reason.)

**The gaps close more slowly than $e^{-a_{4,0}}$.** Figure 15a.2 shows all gaps falling, each a little more slowly than its dashed line. The reason is the bending of the band (Section 15.4 and Exercise 2): a gap is the distance between two band levels, and a band level falls exactly like $e^{-a_{4,0}}$ only where it is a straight line, at small redshifted momenta.

**Delta-SCF and the orbital relaxation.** Without interaction $\Delta_{SCF} = \Delta_{KS}$ to $2.0 \times 10^{-11}\,m$ (Out [9]). With interaction the relaxation $\Delta_{SCF} - \Delta_{KS}$ is at most $5.5 \times 10^{-4}\,m$ (Out [10], `N688_lamp2_a00`), in every state far below the gap itself: the first excited state is well described by moving one particle between frozen orbitals.

**The interaction is a perturbation.** For $N = 136$ the couplings change the energy by at most $0.0318\,m$ (Out [11]), and the self-consistent potentials stay below $0.4\,m$ (Out [13]). The potentials grow along the history (the largest $|v|$ from $0.015$ to $0.242\,m$ for $+\lambda_2$), as the calibration of Section 15.2 anticipated, and they live near the tip, where the proper densities are large (Figure 15a.6). All this holds at the cutoff $L = 3$, where the couplings were calibrated; at larger $L$ the interaction effects grow: for $N = 136$ at $a_{4,0} = 2$ the shift of the energy by $\pm\lambda_1$ is at large $L$ about 21 to 28 times its size at $L = 3$ (Section 15.2, the paragraph on the cutoff). The self-consistent loop converged directly in all 75 states in at most 17 iterations (Out [14]).

**Where the particles are.** Figure 15a.5 makes the most important picture of the gas visible: the particles themselves sit near the brane (right panel), but the proper density, particles per proper 7-volume, is largest at the tip (left panel), because the proper volume factor $e^{6Hy}$ is tiny there ($e^{-18} = 1.5 \times 10^{-8}$ at $y = -3$). Along the history the redshifted band orbitals reach further toward the tip.

**Excitations.** In every state the cheapest way to excite the gas is the Kohn-Sham gap, all listed excitations get cheaper along the history, and none of them can be caused by the history alone (Out [15]); the next sections ask how much energy the history does put into the gas (Section 15.16) and how strongly it can disturb it (Section 15.21).

**What this does not show.** These are instantaneous states on a PRESCRIBED background, with the ASSUMED brane and the CONVENTION of filling. Whether a real gas follows them along the history is the question of adiabaticity (Section 15.21); whether the gas could make the history itself is answered in Section 15.16: it could not.

### 15.16 The energy-momentum tensor of the gas, and why the gas cannot drive the history

**What the tensor is.** Chapter 9 introduced the **energy-momentum tensor** $T^\mu{}_\nu$: at every point a table of $8 \times 8$ numbers that says how much energy and momentum there is and how it flows. For the Kohn-Sham states it is diagonal, and its diagonal holds the **energy density** $\rho = -T^{x_4}{}_{x_4}$ and the **pressures** $p_\mu = T^\mu{}_\mu$ (no sum over $\mu$; the sign convention of the Revision record). Because of the symmetries of the states only four different numbers occur at each $y$: $p_3$, the pressure along each of the three directions of 3-space; $p_t$, the pressure along each of the three extra times; $p_8$, the pressure along the hidden direction; and $\rho$. They are proper densities (per proper 7-volume) and depend on $y$.

**The formulas** (ks-theory.json, emt; checks emt_orbital_components and emt_trace_identity). With the orbital densities $n_o = P(a^2 + b^2)$, $s_o = P\,j\,2ab$ and $t_o = P\,j\,(a^2 - b^2)$ (the last one is the current along the momentum; $P = e^{-6Hy}/\mathrm{Vol}_7$ as in Section 15.2) and sums over the occupied levels with the weights $wgf$:

$$
\rho = \sum wgf\,\varepsilon\,n_o - e_{int}, \qquad p_3 = \sum wgf\,\tfrac{\kappa k}{3}\,t_o + e_{int}, \qquad p_t = e_{int},
$$

$$
p_8 = \sum wgf\,\big[(\varepsilon - v)\,n_o - M s_o - \kappa k\,t_o\big] + e_{int} .
$$

Three remarks make these formulas plausible. (1) The energy density is the level times the number density, summed, minus the interaction energy density (the same double counting as in Section 15.5). (2) A quantum moving along $x_1$ pushes on a wall across $x_1$ with $\kappa k\,t_o$; a closed shell of momenta contains every direction equally often (a cube has the same number of vectors along each axis), so the pressure along each of the three directions is one third of it. (3) The states belong to the **good sector**: they have no momentum along the extra times, so the extra-time pressure has no kinetic part at all, and only the interaction contributes, $p_t = e_{int}$. Without interaction $p_t = 0$.

**The conservation law along the hidden direction.** Energy and momentum are conserved: the covariant divergence of the tensor vanishes, $\nabla_\mu T^\mu{}_\nu = 0$ (Chapter 9). We write out its $y$ component for a diagonal tensor that depends only on $y$, line by line. The covariant divergence of a mixed tensor is

$$
\nabla_\mu T^\mu{}_\nu = \partial_\mu T^\mu{}_\nu + \Gamma^\mu{}_{\mu\sigma}T^\sigma{}_\nu - \Gamma^\sigma{}_{\mu\nu}T^\mu{}_\sigma ,
$$

with the Christoffel symbols $\Gamma$ (Chapters 3 and 9; summed over repeated indices). For a diagonal metric Chapter 9 gives $\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}(\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu})$ (no sum over $\lambda$).

$$
\nabla_\mu T^\mu{}_y = \partial_y T^y{}_y + \Gamma^\mu{}_{\mu y}\,T^y{}_y - \sum_\nu \Gamma^\nu{}_{\nu y}\,T^\nu{}_\nu .
$$

Rule: set $\nu = y$; for a diagonal tensor only $\sigma = y$ survives in the middle term and only $\sigma = \mu$ in the last, and only the $y$ derivative of $T^y{}_y$ is nonzero. (The index $\nu$ in the sum runs over the eight directions; the letter $\lambda$ is kept for the coupling.)

$$
\Gamma^\mu{}_{\mu y} = \partial_y \ln\sqrt{|g|} = \partial_y(6Hy) = 6H .
$$

Rule: for a diagonal metric $\Gamma^\mu{}_{\mu y} = \sum_\mu\frac{1}{2g_{\mu\mu}}\partial_y g_{\mu\mu} = \frac12\sum_\mu\partial_y\ln|g_{\mu\mu}| = \frac12\partial_y\ln|\det g| = \partial_y\ln\sqrt{|g|}$ (the formula above with $\lambda = \mu$ and $\nu = y$, where the first and the last term cancel; $\partial\ln Q = \partial Q/Q$; the logarithm of a product is the sum of the logarithms), and $\sqrt{|g|} = e^{6Hy}$ (Chapter 14).

$$
\Gamma^\nu{}_{\nu y} = \tfrac12 g^{\nu\nu}\partial_y g_{\nu\nu} = \tfrac12\partial_y\ln|g_{\nu\nu}| = H \quad (\nu = x_1, x_2, x_3, x_5, x_6, x_7), \qquad \Gamma^{x_4}{}_{x_4 y} = \Gamma^y{}_{yy} = 0 .
$$

Rule: the same formula for one value of $\nu$ (no sum) gives half the derivative of $\ln|g_{\nu\nu}|$; the six warped directions carry the factor $e^{2Hy}$ in the line element $ds^2 = e^{2Hy}[e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - e^{-2a_4}(dx_5^2 + dx_6^2 + dx_7^2)] - dx_4^2 + dy^2$, and $\tfrac12\partial_y\ln e^{2Hy} = H$; $g_{x_4x_4} = -1$ and $g_{yy} = 1$ are constant.

$$
p_8' + 6H\,p_8 - 3H\,p_3 - 3H\,p_t = 0 .
$$

Rule: $T^y{}_y = p_8$; the six warped terms give $H$ times $p_3$ three times and $H$ times $p_t$ three times.

$$
\big(e^{6Hy}p_8\big)' = 3H\,e^{6Hy}\,(p_3 + p_t) .
$$

Rule: $(e^{6Hy}p_8)' = e^{6Hy}(p_8' + 6Hp_8)$ (product and chain rule); multiply the previous line by $e^{6Hy}$. This is the **conservation law along $y$** (ks-theory.json, emt.conservationY). Integrated from the tip to the brane it reads $[e^{6Hy}p_8]_{-L}^{0} = 3H\int_{-L}^{0}e^{6Hy}(p_3 + p_t)\,dy$. It is PROVED for every self-consistent state (check emt_y_conservation_selfconsistent of `Revision/kohn_sham/reports/ks-theory-python.json`: the force terms $-M'S - v'n$ of the orbitals cancel exactly against the derivative of $e_{int}$ when the potentials are the self-consistent ones) and COMPUTED for all 75 ground states of the record (checks emt_y_conservation_pointwise, worst relative residual $1.95 \times 10^{-8}$, and emt_y_conservation_integrated, worst $1.42 \times 10^{-11}$, of `Revision/kohn_sham/reports/ks-rust-solver.json`).

**The energy change along the history.** Now the $x_4$ component. The metric depends on $x_4$ through $a_4(x_4)$, and the states are instantaneous states that follow it. Line by line:

$$
\nabla_\mu T^\mu{}_{x_4} = \partial_{x_4}T^{x_4}{}_{x_4} + \Gamma^\mu{}_{\mu x_4}T^{x_4}{}_{x_4} - \sum_\nu \Gamma^\nu{}_{\nu x_4}T^\nu{}_\nu .
$$

Rule: as before with $y$ replaced by $x_4$, now with the time derivative of $T^{x_4}{}_{x_4}$ (the flux $T^y{}_{x_4}$ along $y$ vanishes for the instantaneous states, ks-theory.json emt.offDiagonal).

$$
\Gamma^\mu{}_{\mu x_4} = \partial_{x_4}\ln\sqrt{|g|} = 0 .
$$

Rule: $\sqrt{|g|} = e^{6Hy}$ does not depend on $a_4$: 3-space grows like $e^{3a_4}$ and the three extra times shrink like $e^{-3a_4}$, so the proper 7-volume stays the same (check geometry_sqrt_det).

$$
\Gamma^\nu{}_{\nu x_4} = \tfrac12\partial_{x_4}\ln|g_{\nu\nu}| = +a_4' \ (\nu = x_1, x_2, x_3), \quad -a_4' \ (\nu = x_5, x_6, x_7), \quad 0 \ (\nu = x_4, y) .
$$

Rule: the inflating directions carry $e^{2a_4}$ and the deflating extra times $e^{-2a_4}$; $\tfrac12\partial_{x_4}\ln e^{\pm2a_4} = \pm a_4'$, with $a_4' = da_4/dx_4$.

$$
-\partial_{x_4}\rho - \big(3a_4'\,p_3 - 3a_4'\,p_t\big) = 0, \qquad \partial_{x_4}\rho = -3a_4'\,(p_3 - p_t) .
$$

Rule: $T^{x_4}{}_{x_4} = -\rho$; insert the symbols; then move the bracket to the right side.

$$
\frac{\partial\rho}{\partial a_4} = -3\,(p_3 - p_t), \qquad \frac{dE}{da_4} = -3\cdot2\,\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}\,(p_3 - p_t)\,dy .
$$

Rule: along the history $\partial_{x_4} = a_4'\,\partial/\partial a_4$ (chain rule), divide by $a_4'$; then multiply by $2\,\mathrm{Vol}_7e^{6Hy}$ and integrate over $y$, with $E = 2\,\mathrm{Vol}_7\int e^{6Hy}\rho\,dy = E_{KS}$ (check emt_energy_integral of the solver: relative difference at most $1.6 \times 10^{-15}$ in all 75 states). This is the **energy-change law** (ks-theory.json, emt.energyChange; PROVED, check emt_x4_component; COMPUTED for all 75 states against differences of the self-consistent energies at neighbouring slices with fixed occupations, check emt_energy_change_dE_da4, worst $1.5 \times 10^{-10}$).

**How to read it: work.** Write the law as $dE = -3\,P_3\,da_4 + 3\,P_t\,da_4$ with the integrated pressures $P_3 = 2\,\mathrm{Vol}_7\int e^{6Hy}p_3\,dy$ and $P_t$ likewise. When 3-space inflates by $da_4$, each of its three directions stretches by the factor $e^{da_4}$, and a gas that pushes outward with the pressure $p_3$ does work on the expanding space and loses that energy, as a gas in an expanding cylinder pushes a piston. When the three extra times deflate by the same amount, the gas gains $3p_t\,da_4$ per unit volume. Without interaction $p_t = 0$, so the free gas only loses energy, at the rate $3P_3$: this is why $E_{KS}$ falls along the history (Section 15.15). With interaction $p_t = e_{int}$ can have either sign, and the deflation of the extra times can give energy to the gas or take it away; Notebook 15b counts 29 interacting ground states with a positive and 31 with a negative integrated $p_t$ (Out [11]).

**Why the gas cannot be the source of the history.** In the author's theory the function $a_4(x_4)$ is not free: it must solve the field equations for $a_4$ (Chapter 12), whose right-hand side is the energy-momentum tensor of the matter. The record `Revision/field_equations_a4/reports/ks-source-conditions.json` lists, under its key conditions, what a source must satisfy:

- (C1) every component of the source is independent of $x_8$, that is, of $y$;
- (C2) $p_3 + p_t = 2p_8$ at every point (an algebraic identity of the left-hand side of the $a_4$ equations, which every source must share);
- (C3) for the linear history $a_4 = AHx_4 + a_0$ used here: $p_3 = p_t = p_8$ and a constant $\rho$.

The Kohn-Sham gas fails all three. C1: its densities vary strongly with $y$ (Figure 15a.5); the record finds $(\max\rho - \min\rho)/\max|T| \ge 0.0497$ in every state with a nonzero tensor (check ks_profiles_depend_on_x8). C2: $\max|p_3 + p_t - 2p_8|/\max|T|$ lies between 2.09 and 3.99 (check ks_profiles_violate_algebraic_condition), and even the integrated components violate it: $(\int p_3 + \int p_t)/(2\int p_8)$ is $0.339767$, $0.259690$, $0.239714$ for $N = 136$, $\lambda = 0$ at $a_{4,0} = 0, 1, 2$, never close to 1 (check ks_integrals_violate_algebraic_condition). C3: along the history $\rho$ falls (the integral from $80.28$ to $12.45$ for $N = 136$) and $p_3 \ne p_t$ (check ks_history_is_a_prescribed_background); indeed the energy-change law says that $\rho$ can only stay constant if $p_3 = p_t$. The five free states of $N = 8$ are not covered by these checks: their tensor vanishes identically (only the zero modes are filled), a zero source, for which Einstein gravity has no vacuum solution with $H > 0$ (check ks_zero_source_states_listed). Notebook 15b reproduces these numbers from its own computations (Out [12]). Hence the status: the history $a_4 = AHx_4$ is a **PRESCRIBED BACKGROUND**, and the gas is a **test field** on it, without back-reaction; quantities derived along the history, such as the ratios of integrated pressures below, are not consequences of the coupled field equations. Chapter 17 returns to this question with the full source conditions.

**Integrated pressures.** The ratio $\int p_3/\int\rho$ of the free gas is $0.2966$, $0.3100$, $0.3264$ for $N = 136$ at $a_{4,0} = 0, 1, 2$ (Notebook 15b, Out [9]; `Revision/kohn_sham/results/ground/emt-integrals.csv`). It rises toward $1/3$, the value for massless particles, because the band levels are nearly linear in the momentum ($\varepsilon \approx c\,k\,e^{-a_{4,0}}$), like massless particles, and become more so as the momenta redshift. These are integrated components on a prescribed background, not an equation of state that an observer in 3-space would measure.

### 15.17 Example: the energy-momentum profiles (Notebook 15b)

Notebook 15b runs the solver's command `single` for two states, $N = 136$ without interaction at $a_{4,0} = 1$ and $N = 136$ with $+\lambda_2$ at $a_{4,0} = 2$, and checks that their profiles equal the committed ones. It draws the four components as proper densities (Figure 15b.1) and as the densities that are integrated over $y$ (Figure 15b.2), checks the conservation law along $y$ point by point and integrated (Figure 15b.3), solves $N = 136$ at 17 slices and checks the energy-change law at every slice and integrated over the whole history (Figure 15b.4), draws the integrated pressure ratios (Figure 15b.5) and the spreading of the energy toward the tip (Figure 15b.6), shows the interaction terms (Figure 15b.7), and tests the three source conditions on its own numbers. It needs Rust, takes about half a minute, and ends with ALL 18 CHECKS PASSED (notebook 15b).

What to look for: in Figure 15b.1 that the proper densities are huge at the tip and that $p_8$ changes sign; in Figure 15b.2 that the same quantities times the volume factor sit near the brane; in Figure 15b.3 two curves that lie on top of each other; in Figure 15b.4 short orange lines, computed from the pressures alone, that touch the curve of the energies.

<!-- NOTEBOOK 15b -->

### 15.20 Line-by-line walk-through of Notebook 15b

The notebook has 13 code cells, In [1] to In [13]. As before, docstrings are left out of the quotations and long caption strings are shortened; the complete cells are printed in Section 15.19.

**In [1], the set-up cell.** It is the set-up cell of Notebook 15a (Section 15.14, which explains the two Rust lines and the function `rust_program`; the rest is explained in Section 15.9), with the run instructions of this notebook (Section 15.18) in its comments and `NOTEBOOK_ID = "15b"`.

**In [2], the solver and two profiles.**

```python
import csv  # reads the tables (CSV files)
import math  # exp and pi for single numbers

import numpy as np  # arrays of numbers

program = rust_program("Revision/kohn_sham/solver/Cargo.toml", "revision_ks_solver")
RUN_FOLDER = REPO / "Revision/kohn_sham/solver/target/textbook_15b"  # ignored by git
RUN_FOLDER.mkdir(parents=True, exist_ok=True)
```

The imports, the solver built (about a second when it is up to date), and the folder `textbook_15b` inside the solver's build folder, which git ignores, for the files of this notebook's runs.

```python
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
SLICE_SHADES = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]  # light->dark
VOL7 = (2.0 * math.pi / 0.25) ** 3  # proper 7-volume per unit e^{6Hy}
H = 1.0
```

The colours (as in Notebook 15a), $\mathrm{Vol}_7 = 15875.2137$ and $H = 1$.

```python
def solve_state(name, n, lam, a4, profiles=False):
    out = RUN_FOLDER / f"{name}.json"
    command = [str(program), "single", "--root", str(REPO), "--m", "1",
               "--lambda", repr(lam), "--a4", repr(a4), "--N", repr(float(n)),
               "--out", str(out)]
    if profiles:
        command += ["--profiles", str(RUN_FOLDER / f"{name}.csv")]
    done = subprocess.run(command, capture_output=True, text=True)
    if done.returncode != 0 or done.stdout.strip().split("\n")[-1] != "SUCCESS":
        raise RuntimeError(f"the solver failed for {name}: {done.stderr[-500:]}")
    return json.loads(out.read_text(encoding="utf-8"))
```

`solve_state` runs the solver's command `single` for one state and returns its JSON record as a dictionary. The command list holds the program, the word `single`, the repository, the mass 1, the coupling, the slice and the particle number; `repr(x)` writes a number with all the digits needed to read it back exactly. If profiles are wanted, the option that names a CSV file for them is appended (`+=` extends the list). If the program fails, or its last printed line is not SUCCESS, the notebook stops with the end of its error message.

```python
params = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                    .read_text(encoding="utf-8"))
LAMBDA2_136 = {int(c["N"]): c for c in params["couplingCalibration"]["values"]}[136][
    "lambda2"]  # the coupling lambda_2 of N = 136
free_state = solve_state("N136_lam0_a10", 136, 0.0, 1.0, profiles=True)
strong_state = solve_state("N136_lamp2_a20", 136, LAMBDA2_136, 2.0, profiles=True)
say(f"solved N136_lam0_a10 ({free_state['iterations']} iteration) and N136_lamp2_a20 "
    f"({strong_state['iterations']} iterations, lambda = {LAMBDA2_136})")
```

The coupling $\lambda_2 = 0.002789$ of $N = 136$ is read from the record. Two states are solved with profiles: the free state at $a_{4,0} = 1$ and the strongly interacting state at $a_{4,0} = 2$. Out [2] reports 1 iteration for the free state (without interaction one iteration is exact) and 17 for the other.

**In [3], comparison with the committed profiles.**

```python
RECORD_PROFILES = "Revision/kohn_sham/results/ground/profiles"


def read_profile(path):
    data = np.genfromtxt(path, delimiter=",", names=True)
    return {name: data[name] for name in data.dtype.names}
```

`read_profile` is the function of Notebook 15a (Section 15.14, In [12]), here with a path as its argument.

```python
worst = 0.0
identical = []
for name in ("N136_lam0_a10", "N136_lamp2_a20"):
    new = read_profile(RUN_FOLDER / f"{name}.csv")
    old = read_profile(repository_file(f"{RECORD_PROFILES}/{name}.csv"))
    for column in old:
        scale = max(float(np.max(np.abs(old[column]))), 1e-300)
        worst = max(worst, float(np.max(np.abs(new[column] - old[column]))) / scale)
    identical.append((RUN_FOLDER / f"{name}.csv").read_bytes()
                     == repository_file(f"{RECORD_PROFILES}/{name}.csv").read_bytes())
```

For both states and every column the largest difference between the new and the committed profile is divided by the largest value of the column (or by $10^{-300}$, so that a column of zeros does not cause a division by zero), and the largest such ratio is kept. The byte identity of each pair of files is recorded in the list `identical`.

```python
say("columns: " + ", ".join(old))
report("largest relative difference to the record", f"{worst:.1e}")
report("profile files byte-identical to the record", identical)
check(worst < 1e-9, "the new profiles equal the committed profiles within 1e-9",
      record=f"{RECORD_PROFILES}/N136_lam0_a10.csv and N136_lamp2_a20.csv")
```

Out [3] lists the twelve columns ($y$, $n$, $S$, $Q$, $M$, $v$, $w_Q$, $e_{int}$, $\rho$, $p_3$, $p_t$, $p_8$; $Q$ and $w_Q$ belong to the exact-Fock variant), a difference of 0.0, the files byte-identical, and PASS.

**In [4], the proper densities.**

```python
prof = read_profile(RUN_FOLDER / "N136_lam0_a10.csv")
y = prof["y"]
step = float(y[1] - y[0])  # 0.02
COMPONENTS = [("rho", "$\\rho$"), ("p3", "$p_3$"), ("p_t", "$p_t$"), ("p8", "$p_8$")]
fig, ax = plt.subplots()
for colour, (column, label) in zip(PALETTE, COMPONENTS):
    ax.plot(y, prof[column], color=colour, lw=2.0, label=label)
ax.set_yscale("symlog", linthresh=1e-3)
```

The free profile is read; `y` are its 151 coordinates with the spacing `step` $= 0.02$. `COMPONENTS` pairs the column names with their labels, and the four components are drawn on a symmetric logarithmic axis (linear between $-10^{-3}$ and $10^{-3}$), because they span six powers of ten and $p_8$ changes sign.

```python
ax.set_xlabel("hidden coordinate $y$ (tip at $-3$, brane at $0$)")
ax.set_ylabel("proper density (units of $m^8$)")
ax.set_title("Energy density and pressures, $N = 136$, $\\lambda = 0$, $a_{4,0} = 1$")
ax.legend()
save_figure(fig, "proper_emt",
            "The energy density $\\rho$ and the pressures $p_3$, $p_t$, $p_8$ of the "
...)
report("p_t without interaction: largest |p_t|", float(np.max(np.abs(prof["p_t"]))))
check(float(np.max(np.abs(prof["p_t"]))) == 0.0, "p_t = e_int = 0 when lambda = 0")
```

The labels (a proper energy density has the unit $m^8$ in eight dimensions), Figure 15b.1, and the check that $p_t$ is exactly zero without interaction (Out [4]). In the figure all components are largest at the tip, and $p_8$ is negative near the tip and changes sign near $y = -2.45$.

**In [5], the coordinate densities and their integrals.**

```python
def simpson(values, h):
    weights = np.full(len(values), 2.0)
    weights[1::2] = 4.0
    weights[0] = weights[-1] = 1.0
    return h / 3.0 * float(np.sum(weights * values))


def read_rows(relative):
    with open(repository_file(relative), newline="", encoding="utf-8") as handle:
        return {row["id"]: row for row in csv.DictReader(handle)}
```

`simpson` is Simpson's rule (Section 15.14, In [12]); `read_rows` reads a committed table of the record and files its rows by state name.

```python
EMT_TABLE = "Revision/kohn_sham/results/ground/emt-integrals.csv"
emt_rows = read_rows(EMT_TABLE)
summary_rows = read_rows("Revision/kohn_sham/results/ground/summary.csv")
weight = 2.0 * VOL7 * np.exp(6.0 * H * y)  # 2 Vol_7 e^{6Hy}
fig, ax = plt.subplots()
integrals = {}
for colour, (column, label) in zip(PALETTE, COMPONENTS):
    ax.plot(y, weight * prof[column], color=colour, lw=2.0, label=label)
    integrals[column] = simpson(weight * prof[column], step)
```

The record's table of the integrals $2\,\mathrm{Vol}_7\int e^{6Hy}(\cdot)\,dy$ and its summary table are read. `weight` is $2\,\mathrm{Vol}_7e^{6Hy}$, which turns a proper density into the amount per unit $y$ in the doubled box. Each component times the weight is drawn and integrated.

```python
ax.axhline(0.0, color="0.4", lw=0.8)
ax.set_xlabel("hidden coordinate $y$")
ax.set_ylabel("$2\\,\\mathrm{Vol}_7\\, e^{6Hy} \\times$ component (units of $m$)")
ax.set_title("The integrands: energy and pressures per unit $y$")
ax.legend()
save_figure(fig, "coordinate_emt",
            "The energy density and the pressures of the state $N = 136$, "
...)
row = emt_rows["N136_lam0_a10"]
rel = lambda a, b: abs(a - b) / max(abs(b), 1e-300)
worst_int = max(rel(integrals[c], float(row[f"int_{c}"])) for c in ("rho", "p3", "p8"))
```

A zero line, labels, Figure 15b.2. `rel` is the relative difference of two numbers, and `worst_int` the largest relative difference between this notebook's integrals of $\rho$, $p_3$, $p_8$ and the record's columns `int_rho`, `int_p3`, `int_p8`.

```python
report("E_KS from the profile / from the solver",
       f"{integrals['rho']:.8f} / {free_state['E_KS']:.8f}")
report("largest relative difference of the integrals to the record", f"{worst_int:.1e}")
check(rel(free_state["E_KS"], float(summary_rows["N136_lam0_a10"]["E_KS"])) < 1e-12,
      "the solver's E_KS equals the record",
      record="Revision/kohn_sham/results/ground/summary.csv, N136_lam0_a10")
check(rel(integrals["rho"], free_state["E_KS"]) < 1e-6 and worst_int < 1e-6,
      "Simpson's rule on the profile gives E_KS and the recorded integrals",
      record=f"{EMT_TABLE}, columns int_rho, int_p3, int_p8")
```

Out [5]: the integral of the energy density over the 151 profile points is $32.38411614$ against the solver's $E_{KS} = 32.38411569$ (a relative difference of $1.4 \times 10^{-8}$, the error of Simpson's rule on the coarse profile grid); both checks pass. In Figure 15b.2 the energy and the pressures sit near the brane.

**In [6], the conservation law along $y$.**

```python
def derivative4(f, h):
    d = np.zeros(len(f))
    d[2:-2] = (f[:-4] - 8.0 * f[1:-3] + 8.0 * f[3:-1] - f[4:]) / (12.0 * h)
    d[0] = (-25 * f[0] + 48 * f[1] - 36 * f[2] + 16 * f[3] - 3 * f[4]) / (12.0 * h)
    d[1] = (-3 * f[0] - 10 * f[1] + 18 * f[2] - 6 * f[3] + f[4]) / (12.0 * h)
    d[-1] = (25 * f[-1] - 48 * f[-2] + 36 * f[-3] - 16 * f[-4] + 3 * f[-5]) / (12.0 * h)
    d[-2] = (3 * f[-1] + 10 * f[-2] - 18 * f[-3] + 6 * f[-4] - f[-5]) / (12.0 * h)
    return d
```

`derivative4` computes the derivative of equally spaced values with error proportional to $h^4$. At the inner points it uses $f'(y_i) \approx [f_{i-2} - 8f_{i-1} + 8f_{i+1} - f_{i+2}]/(12h)$; `f[:-4]`, `f[1:-3]`, `f[3:-1]` and `f[4:]` are the arrays shifted so that position $i$ of each holds $f_{i-2}$, $f_{i-1}$, $f_{i+1}$, $f_{i+2}$ for the points 2 to 148. At the two first and two last points, where two neighbours on one side are missing, one-sided formulas of the same order use five points on one side. (Each of these formulas is the derivative of the polynomial of degree 4 through the five points.)

```python
def conservation(p):
    e6 = np.exp(6.0 * H * p["y"])
    left = derivative4(e6 * p["p8"], step)
    right = 3.0 * H * e6 * (p["p3"] + p["p_t"])
    scale = max(float(np.max(np.abs(left))), float(np.max(np.abs(right))))
    jump = e6[-1] * p["p8"][-1] - e6[0] * p["p8"][0]
    integral = simpson(right, step)
    return left, right, np.abs(left - right) / scale, abs(jump - integral) / abs(jump)
```

`conservation` returns, for a profile, the left side $(e^{6Hy}p_8)'$, the right side $3H\,e^{6Hy}(p_3 + p_t)$, their difference at every point divided by the largest value of the two sides, and the integrated residual: the jump $[e^{6Hy}p_8]_{-3}^{0}$ compared with the integral of the right side, relative to the jump.

```python
left, right, residual, integrated = conservation(prof)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
ax1.plot(y, left, color=PALETTE[0], lw=3.0, label="$(e^{6Hy}p_8)'$")
ax1.plot(y, right, color=PALETTE[1], lw=1.5, ls="--",
         label="$3H\\,e^{6Hy}(p_3 + p_t)$")
ax1.set_xlabel("hidden coordinate $y$")
ax1.set_ylabel("units of $m^9$")
ax1.set_title("The two sides of the law")
ax1.legend()
```

The left panel draws both sides, the left side as a thick line and the right side dashed on top of it.

```python
ax2.semilogy(y, np.maximum(residual, 1e-16), color=PALETTE[2], lw=1.5)
ax2.axhline(1e-4, color="0.4", ls=":", lw=1.2, label="tolerance $10^{-4}$")
ax2.set_xlabel("hidden coordinate $y$")
ax2.set_ylabel("|left - right| / largest value")
ax2.set_title("Relative residual on the 151 points")
ax2.legend()
save_figure(fig, "y_conservation",
            "Left: the two sides of the conservation law along the hidden "
...)
report("largest pointwise residual / integrated residual",
       f"{float(np.max(residual)):.1e} / {integrated:.1e}")
check(float(np.max(residual)) < 1e-4 and integrated < 1e-6,
      "(e^{6Hy} p8)' = 3H e^{6Hy} (p3 + p_t) holds for N136_lam0_a10",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, checks "
             "emt_y_conservation_pointwise and emt_y_conservation_integrated")
```

The right panel draws the relative residual on a logarithmic axis (`np.maximum(residual, 1e-16)` raises exact zeros to $10^{-16}$, because a logarithmic axis cannot show 0), with the tolerance $10^{-4}$ as a dotted line; then Figure 15b.3. Out [6]: the largest pointwise residual is $2.5 \times 10^{-8}$ and the integrated one $6.1 \times 10^{-10}$, far below the tolerances; the law holds.

**In [7], the energy at 17 slices and its slope.**

```python
DENSE = [i / 8.0 for i in range(17)]  # the slices 0, 0.125, ..., 2
history = []
for a4 in DENSE:
    record = solve_state(f"N136_lam0_dense_{round(1000 * a4):04d}", 136, 0.0, a4)
    ints = record["emtIntegrals_2Vol7_int_e6Hy"]  # 2 Vol_7 int e^{6Hy} (...) dy
    history.append({"a4": a4, "E": record["E_KS"], "rho": ints["rho"],
                    "p3": ints["p3"], "p_t": ints["p_t"], "p8": ints["p8"],
                    "slope": -3.0 * (ints["p3"] - ints["p_t"])})
```

The free state $N = 136$ is solved at the 17 slices $0, 0.125, \dots, 2$ (the names hold a thousand times the slice with four digits). From each JSON record the cell keeps the energy, the integrals of the four components that the solver computed on its fine grid, and the slope $-3(\int p_3 - \int p_t)$ that the energy-change law predicts for $dE/da_4$.

```python
adiabatic_rows = read_rows("Revision/kohn_sham/results/adiabatic/adiabaticity.csv")
worst_e, worst_slope = 0.0, 0.0
say("a4,0       E_KS     dE/da4 (EMT)   dE/da4 (record, finite differences)")
for item in history:
    if item["a4"] in (0.0, 0.5, 1.0, 1.5, 2.0):
        key = f"N136_lam0_a{round(10 * item['a4']):02d}"
        recorded_slope = float(adiabatic_rows[key]["dE_da4_finite_difference"])
        worst_e = max(worst_e, rel(item["E"], float(summary_rows[key]["E_KS"])),
                      rel(item["p3"], float(emt_rows[key]["int_p3"])))
        worst_slope = max(worst_slope, rel(item["slope"], recorded_slope))
        say(f"{item['a4']:4.2f}  {item['E']:10.5f}  {item['slope']:12.6f}"
            f"  {recorded_slope:12.6f}")
```

At the five slices of the canonical matrix the cell compares the energy and $\int p_3$ with the record, and the predicted slope with the derivative that the solver obtained from the energies at neighbouring slices (Richardson differences with the step $\delta = 0.002$, column `dE_da4_finite_difference`), and prints a table.

```python
report("largest relative difference of E and int p3 to the record", f"{worst_e:.1e}")
report("largest relative difference of the slopes", f"{worst_slope:.1e}")
check(worst_e < 1e-12, "E_KS and the integrals at the five slices equal the record",
      record="Revision/kohn_sham/results/ground/summary.csv and emt-integrals.csv")
check(worst_slope < 1e-8, "dE/da4 = -3 (int p3 - int p_t) at the five slices",
      record="Revision/kohn_sham/results/adiabatic/adiabaticity.csv, column "
             "dE_da4_finite_difference")
```

Out [7]: the energies and integrals equal the record exactly, and the slopes from the pressures agree with the finite differences to $3.7 \times 10^{-12}$; the slope is $-71.44$ at $a_{4,0} = 0$ and $-12.19$ at $a_{4,0} = 2$.

**In [8], the slopes integrated over the history.**

```python
slopes = np.array([item["slope"] for item in history])
energies = np.array([item["E"] for item in history])
work = simpson(slopes, 0.125)  # integral of dE/da4 over the history
change = energies[-1] - energies[0]
```

Simpson's rule on the 17 slopes (spacing 0.125) integrates $dE/da_4$ from 0 to 2; the result must equal the change $E(2) - E(0)$ of the energy.

```python
fig, ax = plt.subplots()
ax.plot(DENSE, energies, "o", color=PALETTE[0], ms=8, label="$E_{KS}$ (solver)")
for a4, e, s in zip(DENSE, energies, slopes):
    ax.plot([a4 - 0.05, a4 + 0.05], [e - 0.05 * s, e + 0.05 * s], color=PALETTE[1],
            lw=2.5)
ax.plot([], [], color=PALETTE[1], lw=2.0,
        label="slope $-3 \\cdot 2\\mathrm{Vol}_7 \\int e^{6Hy}(p_3 - p_t)$")
```

The energies are drawn as dots; through each dot a short line from $a_{4,0} - 0.05$ to $a_{4,0} + 0.05$ with the predicted slope $s$ (it rises by $0.05\,s$ on each side). An empty plot makes the legend entry.

```python
ax.set_xlabel("slice $a_{4,0}$ of the history")
ax.set_ylabel("$E_{KS}$ (units of $m$)")
ax.set_title("$N = 136$, $\\lambda = 0$: the pressures give the slope of the energy")
ax.legend()
save_figure(fig, "energy_slopes",
            "The Kohn-Sham energy $E_{KS}$ of $N = 136$ without interaction "
...)
report("E(2) - E(0) / integral of the slopes", f"{change:.6f} / {work:.6f}")
check(rel(work, change) < 1e-5,
      "the integrated slope equals E(2) - E(0) within 1e-5 (relative)",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "emt_energy_change_dE_da4")
```

Figure 15b.4; Out [8]: $E(2) - E(0) = -67.837152$ and the integral of the slopes $-67.837207$, a relative difference of $8 \times 10^{-7}$ (the error of Simpson's rule with the coarse spacing 0.125). The energy the gas loses along the history is the work of its pressures.

**In [9], the integrated pressure ratios.**

```python
ratio3 = np.array([item["p3"] / item["rho"] for item in history])
ratio8 = np.array([item["p8"] / item["rho"] for item in history])
fig, ax = plt.subplots()
ax.plot(DENSE, ratio3, color=PALETTE[0], lw=2.0,
        label="$\\int p_3 / \\int \\rho$, $N = 136$")
ax.plot(DENSE, ratio8, color=PALETTE[1], lw=2.0,
        label="$\\int p_8 / \\int \\rho$, $N = 136$")
```

The ratios $\int p_3/\int\rho$ and $\int p_8/\int\rho$ at the 17 slices, drawn as lines.

```python
worst_ratio = 0.0
for marker, n in (("o", 136), ("s", 688)):
    keys = [f"N{n}_lam0_a{round(10 * a):02d}" for a in (0.0, 0.5, 1.0, 1.5, 2.0)]
    r3 = [float(emt_rows[k]["int_p3"]) / float(emt_rows[k]["int_rho"]) for k in keys]
    r8 = [float(emt_rows[k]["int_p8"]) / float(emt_rows[k]["int_rho"]) for k in keys]
    ax.plot([0, 0.5, 1, 1.5, 2], r3, marker, color=PALETTE[0], ms=8,
            markerfacecolor="white", label=f"record, $N = {n}$")
    ax.plot([0, 0.5, 1, 1.5, 2], r8, marker, color=PALETTE[1], ms=8,
            markerfacecolor="white")
    if n == 136:
        worst_ratio = max(abs(r3[i] - ratio3[4 * i]) for i in range(5))
```

The same ratios from the record's table at the five canonical slices are drawn as open circles ($N = 136$) and squares ($N = 688$). For $N = 136$ they are compared with this notebook's values; `ratio3[4 * i]` is the slice $0.5\,i$, because the dense slices have the spacing 0.125.

```python
ax.axhline(1.0 / 3.0, color="0.4", ls=":", lw=1.2, label="$1/3$")
ax.set_xlabel("slice $a_{4,0}$ of the history")
ax.set_ylabel("ratio of integrals")
ax.set_title("Integrated pressures over integrated energy, $\\lambda = 0$")
ax.legend(fontsize=8)
save_figure(fig, "integrated_ratios",
            "The integrated 3-space pressure (blue) and hidden-direction pressure "
...)
report("int p3 / int rho of N = 136 at a4,0 = 0, 1, 2",
       ", ".join(f"{ratio3[i]:.4f}" for i in (0, 8, 16)))
report("int p8 / int rho of N = 136 at a4,0 = 0, 1, 2",
       ", ".join(f"{ratio8[i]:.4f}" for i in (0, 8, 16)))
check(worst_ratio < 1e-12, "the ratios at the five slices equal the record",
      record=f"{EMT_TABLE}, int_p3 / int_rho")
check(bool(np.all(np.diff(ratio3) > 0.0)) and ratio3[-1] < 1.0 / 3.0,
      "int p3 / int rho rises along the history and stays below 1/3")
```

A dotted line at $1/3$, Figure 15b.5, the ratios at $a_{4,0} = 0, 1, 2$ (the dense indices 0, 8, 16) and two checks. Out [9]: $\int p_3/\int\rho = 0.2966$, $0.3100$, $0.3264$ and $\int p_8/\int\rho = 0.4365$, $0.5969$, $0.6808$; the ratios equal the record, and the 3-space ratio rises at every slice but stays below $1/3$ (Section 15.16 explains why).

**In [10], where the energy sits.**

```python
fig, ax = plt.subplots()
means = []
for shade, a4 in zip(SLICE_SHADES, (0.0, 0.5, 1.0, 1.5, 2.0)):
    p = read_profile(repository_file(f"{RECORD_PROFILES}/N136_lam0_a"
                                     f"{round(10 * a4):02d}.csv"))
    density = 2.0 * VOL7 * np.exp(6.0 * H * p["y"]) * p["rho"]
    density = density / simpson(density, step)  # area 1
    means.append(simpson(p["y"] * density, step))
    ax.plot(p["y"], density, color=shade, lw=2.0, label=f"$a_{{4,0}} = {a4}$")
```

For the five committed profiles of $N = 136$ without interaction the energy per unit $y$, $2\,\mathrm{Vol}_7e^{6Hy}\rho$, is divided by its integral (so that the area under each curve is 1) and drawn; its mean position $\langle y\rangle = \int y\cdot(\text{density})\,dy$ is computed with Simpson's rule.

```python
ax.set_xlabel("hidden coordinate $y$")
ax.set_ylabel("$2\\,\\mathrm{Vol}_7 e^{6Hy}\\rho / E_{KS}$ (units of $m$)")
ax.set_title("The energy spreads toward the tip along the history")
ax.legend()
save_figure(fig, "energy_spreading",
            "The energy per unit $y$ divided by the total energy, "
...)
report("mean position <y> of the energy at the five slices",
       ", ".join(f"{m:.4f}" for m in means))
check(all(means[i + 1] < means[i] for i in range(4)),
      "the mean position of the energy moves toward the tip from slice to slice")
```

Figure 15b.6; Out [10]: $\langle y\rangle = -0.3873$, $-0.4263$, $-0.4556$, $-0.4746$, $-0.4849$, moving toward the tip from slice to slice, as the redshifted band orbitals spread.

**In [11], the interaction terms.**

```python
sp = read_profile(RUN_FOLDER / "N136_lamp2_a20.csv")
hartree = LAMBDA2_136 * 15.0 / 32.0 * sp["S"] ** 2  # (15/32) lambda S^2
exchange = -LAMBDA2_136 / 32.0 * sp["n"] ** 2  # -(1/32) lambda n^2
fig, ax = plt.subplots()
ax.plot(sp["y"], sp["e_int"], color=PALETTE[0], lw=3.0, label="$e_{int} = p_t$")
ax.plot(sp["y"], hartree, color=PALETTE[1], lw=1.5, ls="--",
        label="$\\frac{15}{32}\\lambda S^2$")
ax.plot(sp["y"], exchange, color=PALETTE[2], lw=1.5, ls="--",
        label="$-\\frac{1}{32}\\lambda n^2$")
ax.set_yscale("symlog", linthresh=1e-2)
```

For the strongly interacting profile the two parts of the interaction energy density are computed from the columns $S$ and $n$: the positive part $\tfrac{15}{32}\lambda S^2$ (named `hartree` in the code; it holds the Hartree term and the scalar part of the exchange, Section 15.2) and the negative part $-\tfrac{1}{32}\lambda n^2$. Both are drawn dashed, with the column $e_{int}$ as a thick line, on a symmetric logarithmic axis.

```python
ax.set_xlabel("hidden coordinate $y$")
ax.set_ylabel("proper energy density (units of $m^8$)")
ax.set_title("Interaction energy density, $N = 136$, $+\\lambda_2$, $a_{4,0} = 2$")
ax.legend()
save_figure(fig, "interaction_terms",
            "The interaction energy density $e_{int}$, which is also the extra-time "
...)
sum_error = float(np.max(np.abs(hartree + exchange - sp["e_int"]))) / float(
    np.max(np.abs(sp["e_int"])))
_, _, residual2, integrated2 = conservation(sp)
report("largest |e_int - (15/32 lambda S^2 - 1/32 lambda n^2)| / max|e_int|",
       f"{sum_error:.1e}")
report("conservation law with interaction: pointwise / integrated residual",
       f"{float(np.max(residual2)):.1e} / {integrated2:.1e}")
```

Figure 15b.7; `sum_error` compares the sum of the two parts with the column $e_{int}$, and the conservation law is evaluated again for this state, in which $p_t \ne 0$.

```python
check(sum_error < 1e-12 and bool(np.all(sp["p_t"] == sp["e_int"])),
      "e_int = lambda (15/32 S^2 - 1/32 n^2) and p_t = e_int")
check(float(np.max(residual2)) < 1e-4 and integrated2 < 1e-6,
      "the conservation law holds for the interacting state N136_lamp2_a20",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, checks "
             "emt_y_conservation_pointwise and emt_y_conservation_integrated")
int_pt = [float(row["int_p_t"]) for key, row in emt_rows.items()
          if "_lam0_" not in key]  # the 60 interacting ground states
positive = sum(1 for value in int_pt if value > 0.0)
negative = sum(1 for value in int_pt if value < 0.0)
report("interacting states with integrated p_t > 0 / < 0", f"{positive} / {negative}")
check(len(int_pt) == 60 and positive > 0 and negative > 0,
      "the integrated extra-time pressure takes both signs",
      record=f"{EMT_TABLE}, column int_p_t")
```

Out [11]: the sum matches to $6.8 \times 10^{-16}$ and $p_t = e_{int}$ exactly; the conservation law holds with residuals $5.0 \times 10^{-6}$ (pointwise) and $2.3 \times 10^{-8}$ (integrated). Among the 60 interacting ground states (every row whose name does not contain `_lam0_`) the integrated extra-time pressure is positive in 29 and negative in 31. In Figure 15b.7 the interaction lives near the tip.

**In [12], the three source conditions.**

```python
import re  # finds the numbers inside the record's text

SOURCE = "Revision/field_equations_a4/reports/ks-source-conditions.json"
source = json.loads(repository_file(SOURCE).read_text(encoding="utf-8"))
details = {item["name"]: item["detail"] for item in source["checks"]}
```

`re` is Python's module for **regular expressions**, patterns that find pieces of text. The source-conditions record is read, and `details` files the detail text of each of its checks under the check name.

```python
t_scale = max(float(np.max(np.abs(prof[c]))) for c in ("rho", "p3", "p_t", "p8"))
c1 = (float(np.max(prof["rho"])) - float(np.min(prof["rho"]))) / t_scale  # C1 test
c2 = prof["p3"] + prof["p_t"] - 2.0 * prof["p8"]  # zero everywhere if C2 held
```

For the free profile at $a_{4,0} = 1$: `t_scale` is the largest size of any component, `c1` the variation of $\rho$ along $y$ relative to it (zero if C1 held), and `c2` the array $p_3 + p_t - 2p_8$ (zero everywhere if C2 held).

```python
number = r"(-?[0-9.]+(?:e[-+]?[0-9]+)?)"  # a number as the record prints it
examples = re.findall(
    rf"y = {number}: rho = {number}, p3 = {number}, p_t = {number}, "
    rf"p8 = {number}, p3 \+ p_t - 2 p8 = {number}",
    details["ks_profiles_violate_algebraic_condition"])
```

`number` is a pattern for a number as the record prints it: an optional minus sign (`-?`), digits and points (`[0-9.]+`), and an optional exponent such as `e-05`; the parentheses mark the part to be returned. A string with the prefix `rf` is both raw (backslashes are kept) and an f-string, so `{number}` is replaced by the pattern; `\+` stands for a literal plus sign. `re.findall` returns, for every place in the detail text that matches, the six numbers: $y$, $\rho$, $p_3$, $p_t$, $p_8$ and $p_3 + p_t - 2p_8$. The record prints three such examples, at $y = -3$, $-1.5$ and $0$.

```python
say("    y         rho          p3      p_t          p8  p3 + p_t - 2 p8")
worst_example = 0.0
for example in examples:
    y0, values = float(example[0]), [float(v) for v in example[1:]]
    i = int(np.argmin(np.abs(y - y0)))  # the profile point at this y
    mine = [float(prof["rho"][i]), float(prof["p3"][i]), float(prof["p_t"][i]),
            float(prof["p8"][i]), float(c2[i])]
    say(f"{y[i] + 0.0:5.1f}  {mine[0]:10.6g}  {mine[1]:10.6g}"  # + 0.0 turns -0 into 0
        f"  {mine[2] + 0.0:7.3g}  {mine[3]:10.6g}  {mine[4]:15.6g}")
    for a, b in zip(mine, values):  # 6 significant digits: relative 5e-6
        worst_example = max(worst_example, abs(a - b) / max(abs(b), 1e-300)
                            if b != 0.0 else abs(a))
```

For each example the profile point nearest to its $y$ is found (`np.argmin` gives the position of the smallest distance), this notebook's five values there are printed (the format `g` chooses the shorter of the fixed and the exponent form; adding 0.0 turns a negative zero into 0), and the largest relative difference to the record's six-digit numbers is kept (an absolute difference where the record's value is 0).

```python
ratios_c2 = {item["a4"]: (item["p3"] + item["p_t"]) / (2.0 * item["p8"])
             for item in history}
recorded_c2 = {int(key[-2:]) / 10.0: float(value) for key, value in re.findall(
    r"(N136_lam0_a[0-9][0-9]): ([0-9.]+)",
    details["ks_integrals_violate_algebraic_condition"])}
worst_c2 = max(abs(ratios_c2[a4] / value - 1.0) for a4, value in recorded_c2.items())
```

`ratios_c2` holds $(\int p_3 + \int p_t)/(2\int p_8)$ at the 17 slices; C2 integrated would make it 1. The record prints this ratio for `N136_lam0_a00`, `a10` and `a20`; the pattern finds the three names and numbers, the slice is read from the last two digits of the name (`key[-2:]`), and `worst_c2` is the largest relative difference to this notebook's values.

```python
report("C1: (max rho - min rho) / max|T| for N136_lam0_a10", f"{c1:.4f}")
report("C2 integrated: (int p3 + int p_t)/(2 int p8) at a4,0 = 0, 1, 2",
       ", ".join(f"{ratios_c2[a]:.6f}" for a in (0.0, 1.0, 2.0)))
report("C3: int rho at a4,0 = 0 and 2; int p3 and int p_t at a4,0 = 1",
       f"{history[0]['rho']:.4f}, {history[-1]['rho']:.4f}; "
       f"{history[8]['p3']:.4f}, {history[8]['p_t']:.1f}")
```

Three RESULT lines: the C1 measure, the C2 ratios at three slices, and the numbers that violate C3 ($\int\rho$ at the first and last slice; $\int p_3$ and $\int p_t$ at $a_{4,0} = 1$).

```python
check(c1 > 0.01 and len(examples) == 3 and worst_example < 5e-6
      and float(np.min(np.abs(c2[[0, len(c2) // 2, -1]]))) > 0.0,
      "C1 and C2 fail for N136_lam0_a10; the record's example values reproduced",
      record=f"{SOURCE}, checks ks_profiles_depend_on_x8 and "
             "ks_profiles_violate_algebraic_condition")
check(len(recorded_c2) == 3 and worst_c2 < 5e-6
      and all(abs(r - 1.0) > 0.5 for r in ratios_c2.values()),
      "C2 fails after integration at all 17 slices; the record's ratios reproduced",
      record=f"{SOURCE}, check ks_integrals_violate_algebraic_condition")
check(history[-1]["rho"] < 0.2 * history[0]["rho"]
      and all(item["p3"] > 0.25 * item["rho"] and item["p_t"] == 0.0
              for item in history),
      "C3 fails: rho changes along the history and p3 differs from p_t",
      record=f"{SOURCE}, check ks_history_is_a_prescribed_background")
```

The three checks: C1 and C2 fail for this profile (the variation is more than 1 per cent, and $p_3 + p_t - 2p_8$ is nonzero at the tip, the middle point and the brane; `c2[[0, len(c2) // 2, -1]]` picks these three entries), and the record's three examples are reproduced to six digits; C2 fails after integration at all 17 slices (the ratio differs from 1 by more than 0.5) and the record's three ratios are reproduced; C3 fails ($\int\rho$ falls to less than a fifth, and $\int p_3$ is more than a quarter of $\int\rho$ while $\int p_t = 0$). Out [12] prints the table: at the tip $\rho = 43.07$, $p_3 = 158.3$, $p_8 = -431.7$ and $p_3 + p_t - 2p_8 = 1021.7$; the C1 measure $0.0998$; the C2 ratios $0.339767$, $0.259690$, $0.239714$; and $\int\rho = 80.2822$ and $12.4451$.

**In [13], the last check.**

```python
NAMES = ["proper_emt", "coordinate_emt", "y_conservation", "energy_slopes",
         "integrated_ratios", "energy_spreading", "interaction_terms"]
missing = [name for number, name in enumerate(NAMES, start=1)
           if not output_file(f"{FIGURE_FOLDER}/15b_{number}_{name}.png").is_file()]
check(missing == [], "every figure file of this notebook exists")
all_checks_passed()
```

As in Notebook 15e (Section 15.9, In [15]), with the seven figure names of this notebook in order and the file names `15b_<number>_<name>.png`: the names whose file does not exist are collected, the check requires that list to be empty, and `all_checks_passed()` prints the last line, ALL 18 CHECKS PASSED (notebook 15b).

### 15.21 Adiabaticity: does the gas follow the moving background?

**The question.** Every state computed so far is an **instantaneous** state: at the slice $a_{4,0}$ the solver finds the ground state of the Hamiltonian $h(a_{4,0})$ of that instant, as if the background stood still. But it does not stand still: along the history $a_4 = AHx_4$ grows with the time $x_4$, 3-space inflates and the extra times deflate. A system whose Hamiltonian changes slowly enough stays in the eigenstate that continues its initial one (the **adiabatic theorem** of quantum mechanics; Chapter 14 introduced this adiabatic picture); a system whose Hamiltonian changes too fast is kicked into higher levels. Which case applies here must be measured.

**The exact evolution keeps the sector.** In the mean field the orbitals obey exactly (ks-theory.json, adiabaticity.exactEvolution; check ansatz_removes_spin_connection, which holds for a time-dependent $a_4$)

$$
i\,\frac{\partial\chi}{\partial x_4} = h\big(a_4(x_4)\big)\,\chi, \qquad h_j = j\Big[-i\sigma_1\frac{d}{dy} + M\sigma_2 + \kappa k\sigma_3\Big] + v, \qquad \kappa = e^{-Hy - a_4(x_4)} .
$$

At every instant $h$ acts within one block, at one 3-momentum, and keeps the brane condition; so the evolution never moves a particle to another momentum, block type or parity. **Transitions are possible only inside a sector**, between the levels of one $(n_2, j, \text{parity})$. Notebook 15a showed that each of the lowest particle-hole excitations of the gas (up to 24 per state, 1610 in all) changes the sector (Section 15.15); the in-sector jumps are much more expensive: the one with the largest $Q$ costs between $1.488\,m$ and $2.253\,m$ in the 50 states that have one (all but the 25 states with $N = 8$).

**Where the measure $Q$ comes from, line by line.** Expand the evolving orbital in the instantaneous orbitals $\phi_m$, with $h\,\phi_m = \varepsilon_m\phi_m$ at every instant, as $\chi = \sum_m c_m(x_4)\,e^{-i\theta_m}\phi_m$ with the phases $\theta_m = \int^{x_4}\varepsilon_m\,dx_4$; a dot means $d/dx_4$.

$$
i\dot\chi = \sum_m\big(i\dot c_m + \varepsilon_m c_m\big)e^{-i\theta_m}\phi_m + i\sum_m c_m e^{-i\theta_m}\dot\phi_m .
$$

Rule: the product rule for the three factors; $\dot\theta_m = \varepsilon_m$.

$$
h\chi = \sum_m \varepsilon_m c_m e^{-i\theta_m}\phi_m .
$$

Rule: $h\phi_m = \varepsilon_m\phi_m$.

$$
\dot c_m = -\sum_n c_n\,e^{i(\theta_m - \theta_n)}\,\langle m|\dot\phi_n\rangle .
$$

Rule: set the two lines equal (the evolution equation), the terms $\varepsilon_m c_m$ cancel, take the inner product with $\phi_m$ (the orbitals are orthonormal, so $\langle m|\phi_n\rangle$ is 1 for $n = m$ and 0 otherwise; $\langle m|X\rangle$ means $\int\phi_m^\dagger X\,dy$), multiply by $-i\,e^{i\theta_m}$, and use $-i\cdot i = 1$.

$$
\langle m|\dot\phi_n\rangle = \frac{\langle m|\dot h|n\rangle}{\varepsilon_n - \varepsilon_m} = \dot a_4\,\frac{\langle m|\partial_a h|n\rangle}{\varepsilon_n - \varepsilon_m} \qquad (m \ne n) .
$$

Rule: differentiate $h\phi_n = \varepsilon_n\phi_n$: $\dot h\phi_n + h\dot\phi_n = \dot\varepsilon_n\phi_n + \varepsilon_n\dot\phi_n$; take the inner product with $\phi_m$, where $\langle m|h\dot\phi_n\rangle = \varepsilon_m\langle m|\dot\phi_n\rangle$ ($h$ is self-adjoint, Section 15.2) and $\langle m|\phi_n\rangle = 0$; solve for $\langle m|\dot\phi_n\rangle$; finally $\dot h = \dot a_4\,\partial h/\partial a_4$ (chain rule), written $\partial_a h$ (check adiabatic_offdiagonal_identity).

$$
|c_m| \approx \Big|\int \dot a_4\,\frac{\langle m|\partial_a h|n\rangle}{\varepsilon_n - \varepsilon_m}\,e^{i(\varepsilon_m - \varepsilon_n)x_4}\,dx_4\Big| \approx \dot a_4\,\frac{|\langle m|\partial_a h|n\rangle|}{(\varepsilon_n - \varepsilon_m)^2} .
$$

Rule: start with $c_n = 1$ and all other $c$ zero, and keep on the right of the third line only the term of the occupied orbital $n$ (first order); over a short stretch of time the factor in front of the exponential hardly changes, and $\int e^{i\omega x_4}dx_4 = e^{i\omega x_4}/(i\omega)$, whose size is $1/|\omega|$ with $\omega = \varepsilon_m - \varepsilon_n$.

With $\dot a_4 = AH$ this is the **adiabaticity measure** of the record (ks-theory.json, adiabaticity.measure):

$$
Q_{nm} = AH\,\frac{|\langle n|\partial_a h|m\rangle|}{(\varepsilon_n - \varepsilon_m)^2}, \qquad \text{transition probability} \approx Q_{nm}^2 ,
$$

for $n$ occupied and $m$ empty in the same sector. The evolution is adiabatic when every $Q_{nm} \ll 1$. This is an estimate of first order, not a solution of the time-dependent problem, which stays OPEN.

**The derivative of the Hamiltonian.** Without interaction only $\kappa$ depends on $a_4$, and $\partial\kappa/\partial a_4 = -\kappa$ (the derivative of $e^{-Hy - a_4}$). So

$$
\partial_a h_j = -j\,\kappa k\,\sigma_3, \qquad \langle n|\partial_a h|m\rangle = -j\,k\,e^{-a_{4,0}}\int_{-L}^{0}e^{-Hy}\,(a_na_m - b_nb_m)\,dy ,
$$

because for $\chi = (a, ib)$ the product $\chi_n^\dagger\sigma_3\chi_m$ is $a_na_m + (-ib_n)(-ib_m) = a_na_m - b_nb_m$. With interaction the self-consistent potentials change with $a_4$ too, and $\partial_a h$ gains $j(\partial_aM)\sigma_2 + \partial_av$, which the solver obtains from the states at $a_{4,0} \pm \delta$ and $\pm 2\delta$ (ks-theory.json, adiabaticity.derivative). At $k = 0$, $\partial_a h = 0$: the zero modes do not feel the history at all, and for $N = 8$ every $Q$ is exactly zero.

**Hellmann-Feynman.** For $m = n$ the same differentiation gives the **Hellmann-Feynman theorem** of Chapter 13, $d\varepsilon_n/da_4 = \langle n|\partial_a h|n\rangle$ (take the inner product of the differentiated eigen-equation with $\phi_n$ itself; the terms with $\dot\phi_n$ cancel because $h$ is self-adjoint and $\langle n|n\rangle = 1$). Summed over the occupied levels it gives $dE/da_4 = \sum gf\langle n|\partial_a h|n\rangle$ for the free gas, the same as the energy-change law of Section 15.16 (check adiabatic_hellmann_feynman of `Revision/kohn_sham/reports/ks-theory-python.json`; the solver checks it for all 75 states, worst deviation $2.6 \times 10^{-9}\,m$, check adiabatic_hellmann_feynman of `Revision/kohn_sham/reports/ks-rust-solver.json`).

**What the record finds** (COMPUTED; `Revision/kohn_sham/results/adiabatic/adiabaticity.csv`, reproduced by Notebook 15c). Over the whole canonical matrix $Q_{max} \le 0.0935$, so every transition probability is below $0.009$; the largest $Q$ belongs to the jump from the brane-band level of the highest occupied shell to the first bulk level of the same sector, at the start of the history ($N = 688$, $a_{4,0} = 0$), and $Q_{max}$ falls along the history because the matrix element carries the factor $k\,e^{-a_{4,0}}$. Within the sectors, the instantaneous states are followed adiabatically to a good approximation.

**Fermi-level crossings.** Adiabatic evolution keeps the occupation of every level. If along the history an empty level of one sector comes down below an occupied level of another sector, the instantaneous ground state (aufbau) would move particles from one to the other, but the evolution cannot: the two levels lie in different sectors. Such a **Fermi-level crossing** makes the instantaneous ground state the wrong state. The canonical matrix has none (the record file `adiabatic/fermi-level-crossings.csv`: no change of the occupied set in any of its 60 rows). The record demonstrates the effect with $N = 696 = 688 + 8$ (check adiabatic_crossing_flag_demonstration): at $a_{4,0} = 0$ the eight extra particles sit in the odd bulk level at $k = 0$ ($\varepsilon = 1.2923$, which does not move), while the band level of the shell $n_2 = 12$ lies just above it and comes down; after the crossing the adiabatically continued state lies above the instantaneous aufbau state by $3.66\,m$ at $a_{4,0} = 0.5$, growing to $8.62\,m$ at $a_{4,0} = 2$ (`adiabatic/crossing-demo.csv`). There the instantaneous picture fails.

### 15.22 Example: the adiabaticity measure (Notebook 15c)

Notebook 15c needs no Rust. It defines the solver's shooting method for the free problem in Python, solves again all 270 levels of the occupied sectors of the free states $N = 136$ and $N = 688$ at the five slices, and computes $Q_{nm}$ for every allowed pair. It draws the two orbitals of the pair with the largest $Q$ and the integrand of their matrix element (Figure 15c.1), every $Q$ against the shell (Figure 15c.2), $Q_{max}$ of the whole matrix along the history (Figure 15c.3), the Hellmann-Feynman theorem (Figure 15c.4), the Fermi-level crossing of $N = 696$ (Figure 15c.5) and a heat map of $Q_{max}$ (Figure 15c.6). It takes about 15 seconds and ends with ALL 12 CHECKS PASSED (notebook 15c).

What to look for: in Figure 15c.1 that the band orbital sits at the brane while the bulk orbital fills the interval, so that their overlap is small; in Figure 15c.2 that all points lie below 0.1; in Figure 15c.5 how quickly the band level crosses the fixed bulk level.

<!-- NOTEBOOK 15c -->

### 15.25 Line-by-line walk-through of Notebook 15c

The notebook has 11 code cells, In [1] to In [11]; the complete cells are printed in Section 15.24.

**In [1], the set-up cell.** It is the set-up cell of Notebook 15e, explained line by line in Section 15.9, with the run instructions of this notebook (Section 15.23) in its comments and `NOTEBOOK_ID = "15c"`.

**In [2], the solver's method for the free problem.**

```python
import csv  # reads the tables (CSV files) of the Revision record
import math  # exp, sqrt, atan2, pi for single numbers

import numpy as np  # arrays of numbers

L, STEPS = 3.0, 900  # tip cutoff and number of RK4 steps (the solver's values)
POINTS = 2 * STEPS + 1  # step ends and midpoints
STEP = L / STEPS
Y = np.array([-L * ((POINTS - 1 - f) / (POINTS - 1)) for f in range(POINTS)])
EW_LIST = [math.exp(-y) for y in Y.tolist()]  # e^{-Hy} with H = 1, as the solver
EW = np.array(EW_LIST)
```

The imports; $L = 3$ and $G = 900$ steps; the 1801 fine points `Y` (the formula of Notebook 15e, Section 15.9 In [2]); and the factor $e^{-Hy}$ at every fine point, once as a list (fast for single numbers in the loop) and once as an array.

```python
SIMPSON = np.full(POINTS, 2.0 * STEP / 6.0)  # Simpson weights on the fine grid
SIMPSON[1::2] = 4.0 * STEP / 6.0
SIMPSON[0] = SIMPSON[-1] = STEP / 6.0
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
```

The Simpson weights $\tfrac{h}{6}$ times $1, 4, 2, 4, \dots, 4, 1$ on the fine grid (Section 15.3), and the colours.

```python
def shoot(eps, k, j, a4, store=False):
    kk = k * math.exp(-a4)
    a, b, theta, raw, area, r2_prev = 1.0, 0.0, 0.0, 0.0, 0.0, 1.0
    je = j * eps  # j (eps - v) with v = 0
    nodes = [(a, b)] if store else None
```

The free version of `shoot` of Notebook 15e: the mass is 1 and $v = 0$ everywhere, so they need not be passed. The start values are those of Section 15.9 (In [3]), and `je` is $j\varepsilon$.

```python
    for i in range(STEPS):
        k0 = kk * EW_LIST[2 * i]  # kappa k at the start of the step
        k1 = kk * EW_LIST[2 * i + 1]  # at its midpoint
        k2 = kk * EW_LIST[2 * i + 2]  # at its end
        p1a, p1b = a - (k0 + je) * b, (je - k0) * a - b  # (a', b') with M = 1
        aa, bb = a + 0.5 * STEP * p1a, b + 0.5 * STEP * p1b
        p2a, p2b = aa - (k1 + je) * bb, (je - k1) * aa - bb
        aa, bb = a + 0.5 * STEP * p2a, b + 0.5 * STEP * p2b
        p3a, p3b = aa - (k1 + je) * bb, (je - k1) * aa - bb
        aa, bb = a + STEP * p3a, b + STEP * p3b
        p4a, p4b = aa - (k2 + je) * bb, (je - k2) * aa - bb
        a += STEP / 6.0 * (p1a + 2.0 * p2a + 2.0 * p3a + p4a)
        b += STEP / 6.0 * (p1b + 2.0 * p2b + 2.0 * p3b + p4b)
```

The RK4 step written out without the helper `rhs`: $\kappa k$ at the start, the middle and the end of the step; the four slopes $(a', b')$ of the block equation with $M = 1$, each at the prediction made with the previous slope (`aa`, `bb`); and the weighted average $\tfrac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$.

```python
        new = math.atan2(b, a)  # the Pruefer angle, followed continuously:
        change = new - raw  # bring the change of angle into (-pi, pi]
        if change > math.pi:
            change -= 2.0 * math.pi
        elif change <= -math.pi:
            change += 2.0 * math.pi
        theta, raw = theta + change, new
        r2 = a * a + b * b
        area, r2_prev = area + 0.5 * STEP * (r2_prev + r2), r2  # trapezoid rule
        if store:
            nodes.append((a, b))
    return j * theta, area / r2_prev, nodes  # Phi and dPhi/deps = int r^2 / r(0)^2
```

The Pruefer angle followed continuously, the trapezoid sum of $r^2$, the stored values, and the result $(\Phi, d\Phi/d\varepsilon, \text{nodes})$, as in Section 15.9.

```python
def find_level(k, j, parity, label, a4, guess, tol=1e-13):
    target = label * math.pi + (0.0 if parity == "even" else 0.5 * math.pi)
    e = guess
    g, d = shoot(e, k, j, a4)[:2]
    g -= target
    if g == 0.0:
        return e
    step = min(max(abs(g / d) * 1.2, 1e-4), 2.0)  # the first trial step
```

`find_level` is the safeguarded Newton method of Section 15.9 (In [5]) for the free problem: the target, the value $g = \Phi - t_l$ and the derivative $d$ at the guess (`[:2]` keeps the first two results of `shoot`), and the first trial step.

```python
    if g < 0:  # Phi too small: walk up with doubling steps until Phi >= target
        lo = e
        while True:
            trial = lo + step
            gt, dt = shoot(trial, k, j, a4)[:2]
            gt -= target
            if gt >= 0:
                hi = trial  # [lo, hi] brackets the level
                if abs(gt) < abs(g):
                    e, g, d = trial, gt, dt  # keep the better end for Newton
                break
            lo, e, g, d = trial, trial, gt, dt
            step *= 2.0
    else:  # Phi too large: walk down until Phi <= target
        hi = e
        while True:
            trial = hi - step
            gt, dt = shoot(trial, k, j, a4)[:2]
            gt -= target
            if gt <= 0:
                lo = trial
                if abs(gt) < abs(g):
                    e, g, d = trial, gt, dt
                break
            hi, e, g, d = trial, trial, gt, dt
            step *= 2.0
```

The walk with doubling steps up or down until the target is bracketed, exactly as in Notebook 15e.

```python
    previous = math.inf
    while hi - lo > tol and g != 0.0:
        new = e - g / d  # Newton step, or bisection if it leaves the bracket
        bisect = not lo < new < hi or abs(g) > 0.5 * previous
        if bisect:
            new = 0.5 * (lo + hi)
        previous = abs(g)
        moved = abs(new - e)
        e = new
        g, d = shoot(e, k, j, a4)[:2]
        g -= target
        if g < 0:
            lo = e
        elif g > 0:
            hi = e
        if moved <= tol and not bisect:
            break  # a Newton step that moves less than tol: converged
    return e
```

The refinement by Newton steps with bisection as the safeguard, written as a `while` loop that runs as long as the bracket is longer than the tolerance and the target is not hit exactly; otherwise as in Notebook 15e.

```python
def orbital(eps, k, j, a4):
    nodes = np.array(shoot(eps, k, j, a4, store=True)[2])
    kap = k * math.exp(-a4) * EW[0::2]
    a_n, b_n = nodes[:, 0], nodes[:, 1]
    da = a_n - (kap + j * eps) * b_n  # derivatives at the step ends
    db = (j * eps - kap) * a_n - b_n
    a = np.zeros(POINTS)
    b = np.zeros(POINTS)
    a[0::2], b[0::2] = a_n, b_n
    a[1::2] = 0.5 * (a_n[:-1] + a_n[1:]) + STEP / 8.0 * (da[:-1] - da[1:])
    b[1::2] = 0.5 * (b_n[:-1] + b_n[1:]) + STEP / 8.0 * (db[:-1] - db[1:])
    norm = math.sqrt(float(np.sum(SIMPSON * (a * a + b * b))))
    return a / norm, b / norm
```

The normalised orbital on the fine grid, as in Section 15.9 (In [7]): the stored step-end values become a two-column array (`nodes[:, 0]` is its first column, $a$; `nodes[:, 1]` the second, $b$), the derivatives come from the block equation, the midpoints from the Hermite formula, and Simpson's rule normalises.

```python
def da_h(k, j, a4, first, second):
    s3 = first[0] * second[0] - first[1] * second[1]
    return -j * k * math.exp(-a4) * float(np.sum(SIMPSON * EW * s3))
```

`da_h` is the matrix element $\langle n|\partial_a h|m\rangle = -j\,k\,e^{-a_{4,0}}\int e^{-Hy}(a_na_m - b_nb_m)\,dy$ of Section 15.21, with the integral by Simpson's rule; `first` and `second` are orbitals, each a pair $(a, b)$ of arrays. The cell defines functions only and prints nothing.

**In [3], the levels of the record solved again.**

```python
LEVELS = "Revision/kohn_sham/results/ground/levels"
SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]


def state_id(n, a4, tag="lam0"):
    return f"N{n}_{tag}_a{round(10 * a4):02d}"
```

The folder of the level tables, the five slices, and the state names as in Notebook 15a (here the coupling tag comes last, with the default `lam0`).

```python
def solve_state(n, a4):
    rows = list(csv.DictReader(open(repository_file(f"{LEVELS}/{state_id(n, a4)}.csv"),
                                    newline="", encoding="utf-8")))
    sectors = {}
    for row in rows:
        sector = (int(row["n2"]), int(row["j"]), row["parity"])
        sectors.setdefault(sector, []).append(row)
```

`solve_state` reads the level table of a free state into a list of rows and groups the rows by sector: `setdefault(sector, [])` returns the list of that sector, creating an empty one the first time, and the row is appended to it.

```python
    solved, worst = {}, 0.0
    for sector, members in sectors.items():
        if all(float(row["f"]) < 0.5 for row in members):
            continue  # no particle in this sector: no transition starts here
        solved[sector] = {}
        for row in members:
            k, eps_rec = float(row["k"]), float(row["eps"])
            eps = find_level(k, sector[1], sector[2], int(row["label"]), a4, eps_rec)
            worst = max(worst, abs(eps - eps_rec))
            solved[sector][int(row["label"])] = (
                eps, float(row["f"]), k, int(row["r3"]), orbital(eps, k, sector[1], a4))
    return solved, worst
```

Sectors without an occupied level are skipped: no transition can start there. For every level of the other sectors the energy is found again in Python, starting from the recorded value, and stored with its occupation, momentum, number of directions $r_3$ and orbital, under its sector and label; `worst` is the largest difference to the record.

```python
states = {}
worst_level = 0.0
for n in (136, 688):
    for a4 in SLICES:
        states[(n, a4)], worst = solve_state(n, a4)
        worst_level = max(worst_level, worst)
count = sum(len(levels) for state in states.values() for levels in state.values())
report("levels solved again (10 states)", count)
report("largest |eps(Python) - eps(solver)|", f"{worst_level:.1e}")
check(worst_level < 1e-12, "every level equals the solver's level within 1e-12",
      record=f"{LEVELS}/N136_lam0_a*.csv and N688_lam0_a*.csv, column eps")
```

The ten free states $N = 136, 688$ at the five slices are solved. Out [3]: 270 levels, the largest difference to the solver $9.3 \times 10^{-14}$, PASS.

**In [4], the pair with the largest $Q$.**

```python
sector = (4, 1, "even")
band = states[(136, 0.0)][sector][0]  # (eps, f, k, r3, (a, b)) of label 0
bulk = states[(136, 0.0)][sector][1]  # label 1
k = band[2]
integrand = k * EW * (band[4][0] * bulk[4][0] - band[4][1] * bulk[4][1])
```

For $N = 136$ at $a_{4,0} = 0$ the record names the pair `4:+1:even:0 -> 4:+1:even:1`: in the sector $n_2 = 4$ ($k = 0.5$), $j = +1$, even, the occupied band level (label 0) and the first empty bulk level (label 1). `band[4]` is the orbital $(a, b)$ of the band level; `integrand` is $\kappa k\,(a_na_m - b_nb_m)$ at $a_{4,0} = 0$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
left.plot(Y, band[4][0], color=PALETTE[0], lw=2.0, label="band: $a$")
left.plot(Y, band[4][1], color=PALETTE[0], lw=1.5, ls="--", label="band: $b$")
left.plot(Y, bulk[4][0], color=PALETTE[1], lw=2.0, label="bulk: $a$")
left.plot(Y, bulk[4][1], color=PALETTE[1], lw=1.5, ls="--", label="bulk: $b$")
left.set_xlabel("hidden coordinate $y$")
left.set_ylabel("orbital (normalised)")
left.set_title(f"$n_2 = 4$: band $\\varepsilon = {band[0]:.4f}$, "
               f"bulk $\\varepsilon = {bulk[0]:.4f}$", fontsize=10)
left.legend(fontsize=8)
```

The left panel draws both orbitals ($a$ solid, $b$ dashed), with their energies in the title.

```python
right.plot(Y, integrand, color=PALETTE[2], lw=2.0)
right.fill_between(Y, integrand, color=PALETTE[2], alpha=0.25)
right.set_xlabel("hidden coordinate $y$")
right.set_ylabel("$\\kappa k\\,(a_n a_m - b_n b_m)$ (units of $m^2$)")
right.set_title("Integrand of the matrix element")
save_figure(fig, "transition_orbitals",
            "Left: the orbitals (components $a$ solid, $b$ dashed; vertical axis, "
...)
element = abs(da_h(k, 1, 0.0, band[4], bulk[4]))
report("|<band| d_a h |bulk>| and Q for N = 136, a4,0 = 0",
       f"{element:.13f}, {element / (band[0] - bulk[0]) ** 2:.13f}")
```

The right panel draws the integrand and shades the area between it and zero (`fill_between`), whose signed size is the matrix element; then Figure 15c.1. Out [4]: $|\langle n|\partial_a h|m\rangle| = 0.3588612$ and $Q = 0.3588612/(2.052930)^2 = 0.0851488$. The band orbital sits at the brane and the bulk orbital oscillates, so the integrand changes sign and partly cancels; together with the large energy difference this keeps $Q$ small.

**In [5], $Q$ for every allowed pair.**

```python
ADIABATIC = "Revision/kohn_sham/results/adiabatic/adiabaticity.csv"
with open(repository_file(ADIABATIC), newline="", encoding="utf-8") as handle:
    adiabatic = {row["id"]: row for row in csv.DictReader(handle)}


def key_text(sector, label):
    return f"{sector[0]}:{sector[1]:+d}:{sector[2]}:{label}"
```

The record's adiabaticity table is read. `key_text` writes a level as the record writes it, `n2:j:parity:label`; the format `+d` prints the block type with its sign.

```python
pairs = {}  # (n, a4) -> list of (Q, n2, label m) for the figure
worst_q, same_pairs = 0.0, True
say("   N  a4,0   Q_max    pair                          delta eps   matrix el.")
for (n, a4), state in states.items():
    best = (0.0, "", 0.0, 0.0)
    pairs[(n, a4)] = []
    for sector, levels in state.items():
        for ln, (en, fn, k, _, on) in levels.items():
            if fn < 0.5:
                continue
            for lm, (em, fm, _, _, om) in levels.items():
                if fm > 0.5:
                    continue
                element = abs(da_h(k, sector[1], a4, on, om))
                q = element / (en - em) ** 2  # A H = 1
                pairs[(n, a4)].append((q, sector[0], lm))
                if q > best[0]:
                    best = (q, f"{key_text(sector, ln)} -> {key_text(sector, lm)}",
                            abs(en - em), element)
```

For each of the ten states and each occupied sector, the two inner loops run over every occupied level $n$ (`fn` its occupation; empty ones are skipped) and every empty level $m$ (occupied ones are skipped) of the same sector. For each pair the matrix element and $Q = |\langle n|\partial_a h|m\rangle|/(\varepsilon_n - \varepsilon_m)^2$ (with $AH = 1$) are computed and stored for the figure, and `best` keeps the largest $Q$ with its pair, energy difference and matrix element.

```python
    row = adiabatic[state_id(n, a4)]
    for value, column in ((best[0], "Q_max"), (best[2], "Q_max_delta_eps"),
                          (best[3], "Q_max_matrix_element")):
        worst_q = max(worst_q, abs(value / float(row[column]) - 1.0))
    same_pairs = same_pairs and best[1] == row["Q_max_pair"]
    say(f"{n:4d}  {a4:4.1f}  {best[0]:.5f}  {best[1]:28}  {best[2]:9.6f}"
        f"  {best[3]:9.6f}")
```

Still inside the loop over the states: the largest $Q$, its energy difference and its matrix element are compared with the record, the pair's name too, and a table row is printed.

```python
report("largest relative difference to the record", f"{worst_q:.1e}")
check(worst_q < 1e-9, "Q_max, its energy difference and matrix element reproduced",
      record=f"{ADIABATIC}, columns Q_max, Q_max_delta_eps, Q_max_matrix_element")
check(same_pairs, "the pair with the largest Q is the recorded pair",
      record=f"{ADIABATIC}, column Q_max_pair")
```

Out [5] shows the table: $Q_{max}$ falls from $0.08515$ to $0.03839$ for $N = 136$ and from $0.09345$ to $0.05289$ for $N = 688$ along the history, always for the jump from the band level of the highest occupied shell ($n_2 = 4$, respectively 11) to the bulk level above it in the same sector. The largest relative difference to the record is $6.8 \times 10^{-14}$, and the pairs are the recorded ones.

**In [6], every pair at the first slice.**

```python
fig, ax = plt.subplots()
for marker, n in (("o", 136), ("s", 688)):
    for colour, label in zip(PALETTE, (1, 2)):
        points = [(n2, q) for q, n2, lm in pairs[(n, 0.0)] if lm == label]
        ax.plot([p[0] for p in points], [max(p[1], 1e-6) for p in points], marker,
                color=colour, ms=8 if n == 136 else 6,
                markerfacecolor=colour if n == 136 else "white",
                label=f"$N = {n}$, to label {label}")
```

For $N = 136$ (filled circles) and $N = 688$ (open squares) at $a_{4,0} = 0$, the cell draws $Q$ of every pair against the shell of its sector, coloured by the label of the empty level (1 or 2). Values below $10^{-6}$ (the transitions at $k = 0$, which are exactly zero) are drawn at $10^{-6}$, because a logarithmic axis cannot show zero.

```python
ax.set_yscale("log")
ax.set_xlabel("shell $n_2$ of the sector ($k = 0.25\\sqrt{n_2}$)")
ax.set_ylabel("$Q_{nm}$ (pure number)")
ax.set_title("Every allowed transition at $a_{4,0} = 0$, $\\lambda = 0$")
ax.legend(fontsize=8)
save_figure(fig, "q_by_pair",
            "The adiabaticity measure $Q_{nm}$ (vertical axis, logarithmic, pure "
...)
largest = max(q for values in pairs.values() for q, _, _ in values)
report("largest Q of all free pairs (10 states)", f"{largest:.5f}")
check(largest < 0.1, "every Q of the free states is below 0.1")
```

Figure 15c.2, and the largest $Q$ over all pairs of the ten states: $0.09345$ (Out [6]), below 0.1. In the figure the jump to the label 1 dominates in every shell and grows with $n_2$, because the matrix element is proportional to $k$.

**In [7], $Q_{max}$ of the whole matrix.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
tags = [("lam0", "$0$"), ("lamp1", "$+\\lambda_1$"), ("lamm1", "$-\\lambda_1$"),
        ("lamp2", "$+\\lambda_2$"), ("lamm2", "$-\\lambda_2$")]
record_max = 0.0
for style, n in (("-", 136), ("--", 688)):
    for colour, (tag, label) in zip(PALETTE, tags):
        values = [float(adiabatic[state_id(n, a4, tag)]["Q_max"]) for a4 in SLICES]
        record_max = max(record_max, max(values))
        left.plot(SLICES, values, style, color=colour, lw=1.5, marker="o", ms=4,
                  label=f"$N = {n}$, $\\lambda = $ {label}")
        right.plot(SLICES, [v * v for v in values], style, color=colour, lw=1.5,
                   marker="o", ms=4)
```

For $N = 136$ (solid) and $688$ (dashed) and the five couplings the recorded $Q_{max}$ at the five slices is drawn on the left and its square, the transition probability, on the right; `record_max` keeps the largest value.

```python
    mine = [max(q for q, _, _ in pairs[(n, a4)]) for a4 in SLICES]
    left.plot(SLICES, mine, "x", color="black", ms=10, mew=2)
left.plot([], [], "x", color="black", ms=10, mew=2, label="this notebook")
left.set_yscale("log")
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("$Q_{max}$")
left.set_title("Largest $Q$ (record)")
left.legend(fontsize=7, ncol=2)
right.set_yscale("log")
right.set_xlabel("slice $a_{4,0}$")
right.set_ylabel("$Q_{max}^2$")
right.set_title("Transition probability estimate")
save_figure(fig, "q_history",
            "Left: the largest adiabaticity measure $Q_{max}$ (vertical axis, "
...)
```

The values recomputed in this notebook for $\lambda = 0$ are drawn as black crosses (`mew` is the width of the cross lines), then the legend, axes and Figure 15c.3.

```python
n8_zero = all(float(adiabatic[state_id(8, a4, tag)]["Q_max"]) == 0.0
              for a4 in SLICES for tag, _ in tags)
report("largest Q_max of the whole matrix (record)", f"{record_max:.4f}")
check(record_max <= 0.0935 and n8_zero,
      "Q_max <= 0.0935 over the matrix, and Q = 0 exactly for N = 8",
      record=f"{ADIABATIC}, column Q_max")
falling = all(max(q for q, _, _ in pairs[(n, SLICES[i + 1])])
              < max(q for q, _, _ in pairs[(n, SLICES[i])])
              for n in (136, 688) for i in range(4))
check(falling, "Q_max of the free states falls from slice to slice")
```

Out [7]: the largest $Q_{max}$ of the matrix is $0.0935$, every $Q$ of $N = 8$ is exactly zero (only $k = 0$ is occupied, where $\partial_a h = 0$), and $Q_{max}$ of the free states falls from slice to slice.

**In [8], the Hellmann-Feynman theorem.**

```python
DELTA = 2e-3
a0 = 1.0
state = states[(688, a0)]
shells, finite, element = [], [], []
for sector, levels in sorted(state.items()):
    if sector[0] == 0:
        continue  # the zero modes do not depend on a4,0
    eps, f, k, r3, orb = levels[0]  # the occupied brane-band level (label 0)
    near = {s: find_level(k, sector[1], sector[2], 0, a0 + s, eps)
            for s in (DELTA, -DELTA, 2 * DELTA, -2 * DELTA)}
```

For the free state $N = 688$ at $a_{4,0} = 1$ the cell visits the occupied sectors in sorted order, skips the shell $n_2 = 0$, and takes the occupied band level (label 0) of each shell; it solves this level again at the four slices $1 \pm 0.002$ and $1 \pm 0.004$.

```python
    d1 = (near[DELTA] - near[-DELTA]) / (2 * DELTA)
    d2 = (near[2 * DELTA] - near[-2 * DELTA]) / (4 * DELTA)
    shells.append(k)
    finite.append((4.0 * d1 - d2) / 3.0)
    element.append(da_h(k, sector[1], a0, orb, orb))
hf_dev = max(abs(a - b) for a, b in zip(finite, element))
```

`d1` and `d2` are the central differences $D(\delta)$ and $D(2\delta)$, $D(s) = [\varepsilon(a + s) - \varepsilon(a - s)]/(2s)$; their error is proportional to $s^2$, so the Richardson combination $\tfrac13(4D(\delta) - D(2\delta))$ removes it (as in Section 15.9, In [9]). `element` is the diagonal matrix element $\langle n|\partial_a h|n\rangle$, and `hf_dev` the largest difference between the two.

```python
de_da = sum(4.0 * levels[l][3] * levels[l][1] * da_h(levels[l][2], sector[1], a0,
                                                       levels[l][4], levels[l][4])
            for sector, levels in state.items() for l in levels)
recorded = float(adiabatic[state_id(688, a0)]["dE_da4_finite_difference"])
```

`de_da` is $\sum gf\langle n|\partial_a h|n\rangle$ over all levels of the occupied sectors, with $g = 4r_3$ (`levels[l][3]` is $r_3$, `levels[l][1]` the occupation, which is 0 for the empty levels); `recorded` is the derivative of $E$ that the solver obtained by finite differences.

```python
fig, ax = plt.subplots()
ax.plot(shells, finite, "o", color=PALETTE[0], ms=9, label="finite differences")
ax.plot(shells, element, "x", color=PALETTE[1], ms=10, mew=2,
        label="$\\langle n|\\partial_a h|n\\rangle$")
ax.set_xlabel("3-momentum $k$ of the shell (units of $m$)")
ax.set_ylabel("$d\\varepsilon/da_4$ (units of $m$)")
ax.set_title("Hellmann-Feynman: $N = 688$, $\\lambda = 0$, $a_{4,0} = 1$")
ax.legend()
save_figure(fig, "hellmann_feynman",
            "The derivative $d\\varepsilon/da_4$ of the eleven occupied brane-band "
...)
report("largest |finite difference - matrix element|", f"{hf_dev:.1e}")
report("dE/da4 of N688_lam0_a10: Hellmann-Feynman / record",
       f"{de_da:.10f} / {recorded:.10f}")
check(hf_dev < 1e-7, "d eps/da4 = <n| d_a h |n> for the eleven levels within 1e-7",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "adiabatic_hellmann_feynman")
check(abs(de_da / recorded - 1.0) < 1e-9, "dE/da4 = sum g f <n| d_a h |n>",
      record=f"{ADIABATIC}, N688_lam0_a10, column dE_da4_finite_difference")
```

Figure 15c.4 draws both derivatives of the eleven band levels against their momentum: circles and crosses coincide, and every level falls, faster for larger $k$. Out [8]: the largest difference is $1.7 \times 10^{-12}$, and $dE/da_4 = -253.0160345318$ against the record's $-253.0160345309$; both checks pass.

**In [9], the Fermi-level crossing of $N = 696$.**

```python
K12 = 0.25 * math.sqrt(12.0)
eps_odd = find_level(0.0, 1, "odd", 0, 0.0, 1.29)  # the k = 0 odd bulk level


def band12(a4):
    return find_level(K12, 1, "even", 0, a4, 1.9 * K12 * math.exp(-a4))
```

`K12` is the momentum $0.25\sqrt{12} = 0.866$ of the shell $n_2 = 12$; `eps_odd` the odd bulk level at $k = 0$ (it does not depend on the slice); `band12` the band level of the shell 12 at a given slice.

```python
lo, hi = 0.0, 0.5  # bisection for band12(a4) = eps_odd
for _ in range(45):
    mid = 0.5 * (lo + hi)
    lo, hi = (mid, hi) if band12(mid) > eps_odd else (lo, mid)
crossing = 0.5 * (lo + hi)
dense = np.linspace(0.0, 2.0, 41)
band_curve = [band12(a) for a in dense]
```

Bisection finds the slice at which the falling band level meets the bulk level: while the band level is still above, the crossing lies later. 45 halvings of the interval from 0 to 0.5 locate it far below the printed digits. `band_curve` is the band level at 41 slices for the figure.

```python
with open(repository_file("Revision/kohn_sham/results/adiabatic/crossing-demo.csv"),
          newline="", encoding="utf-8") as handle:
    demo = {float(row["a4"]): row for row in csv.DictReader(handle)}
mine = {a4: max(0.0, 8.0 * (eps_odd - band12(a4))) for a4 in SLICES}
worst_demo = max(abs(mine[a4] - float(demo[a4]["difference"])) for a4 in SLICES)
```

The record's demonstration table is read, filed by slice. Without interaction the adiabatically continued state keeps its eight particles in the bulk level, while the instantaneous aufbau state puts them into the lower band level; the energy difference is therefore $8(\varepsilon_{odd} - \varepsilon_{12})$ after the crossing and 0 before it (`max(0.0, ...)`). `worst_demo` compares this with the record's column `difference`.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
left.plot(dense, band_curve, color=PALETTE[0], lw=2.0,
          label="brane band $n_2 = 12$ (32 orbitals)")
left.axhline(eps_odd, color=PALETTE[1], lw=2.0, label="odd bulk level, $k = 0$ (8)")
left.axvline(crossing, color="0.4", ls=":", lw=1.2, label="crossing")
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("level (units of $m$)")
left.set_title("Two levels near the Fermi level, $N = 696$")
left.legend(fontsize=8)
```

The left panel: the band level of the shell 12 (degeneracy $4r_3(12) = 4\cdot8 = 32$), the fixed bulk level (8-fold) as a horizontal line, and the crossing as a dotted vertical line (`axvline`).

```python
right.plot(SLICES, [float(demo[a]["difference"]) for a in SLICES], "o", color="black",
           ms=9, label="record")
right.plot(SLICES, [mine[a] for a in SLICES], "x", color=PALETTE[0], ms=10, mew=2,
           label="$8(\\varepsilon_{odd} - \\varepsilon_{12})$, this notebook")
right.set_xlabel("slice $a_{4,0}$")
right.set_ylabel("$E_{continued} - E_{aufbau}$ (units of $m$)")
right.set_title("Energy above the instantaneous ground state")
right.legend(fontsize=8)
save_figure(fig, "fermi_crossing",
            "The Fermi-level crossing of the demonstration state $N = 696$ without "
...)
```

The right panel: the recorded energy differences (black dots) and this notebook's (blue crosses) at the five slices; then Figure 15c.5.

```python
report("band level n2 = 12 minus the odd level at a4,0 = 0",
       f"{band_curve[0] - eps_odd:.10f}")
report("crossing slice a4,0", f"{crossing:.6f}")
report("largest |8 (eps_odd - eps_12) - recorded difference|", f"{worst_demo:.1e}")
check(0.0 < crossing < 0.5, "the crossing lies between the slices 0 and 0.5",
      record="Revision/kohn_sham/results/adiabatic/crossing-demo.csv, flags at 0 "
             "and 0.5")
check(worst_demo < 1e-9, "the energy differences of the demonstration reproduced",
      record="Revision/kohn_sham/results/adiabatic/crossing-demo.csv, column "
             "difference")
```

Out [9]: at $a_{4,0} = 0$ the band level lies only $0.0032325\,m$ above the bulk level, so the crossing comes almost at once, at $a_{4,0} = 0.002854$; the energy differences agree with the record to $2.0 \times 10^{-11}$. Both checks pass.

**In [10], the heat map.**

```python
rows, names = [], []
for n in (8, 136, 688):
    for tag, label in tags:
        rows.append([float(adiabatic[state_id(n, a4, tag)]["Q_max"]) for a4 in SLICES])
        names.append(f"N = {n}, {tag}")
table = np.array(rows)
```

A table of $Q_{max}$ with one row per series (15 rows: three particle numbers times five couplings) and one column per slice, with a name for each row.

```python
fig, ax = plt.subplots(figsize=(6.5, 6.0))
image = ax.imshow(table, cmap="Blues", aspect="auto", vmin=0.0, vmax=0.1)
ax.grid(False)  # no grid lines across the coloured squares
ax.set_xticks(range(5), [f"{a:.1f}" for a in SLICES])
ax.set_yticks(range(len(names)), names, fontsize=8)
for i in range(table.shape[0]):
    for jj in range(table.shape[1]):
        ax.text(jj, i, f"{table[i, jj]:.3f}", ha="center", va="center", fontsize=7,
                color="white" if table[i, jj] > 0.06 else "black")
```

`ax.imshow` draws the table as coloured squares, from white (0) to dark blue (0.1); `aspect="auto"` lets the squares fill the drawing area. The ticks are labelled with the slices and the row names, and every square gets its value printed in its middle (`table.shape` is the pair (rows, columns); white letters on the dark squares).

```python
ax.set_xlabel("slice $a_{4,0}$")
ax.set_title("$Q_{max}$ of the 75 ground states (record)")
fig.colorbar(image, ax=ax, label="$Q_{max}$")
save_figure(fig, "q_map",
            "Heat map of the largest adiabaticity measure $Q_{max}$ of the 75 ground "
...)
with open(repository_file("Revision/kohn_sham/results/adiabatic/"
                          "fermi-level-crossings.csv"), newline="",
          encoding="utf-8") as handle:
    crossings = list(csv.DictReader(handle))
changed = sum(row["occupied_set_changed"] == "true" for row in crossings)
report("rows of the crossing record / rows with a changed occupied set",
       f"{len(crossings)} / {changed}")
check(len(crossings) == 60 and changed == 0,
      "no Fermi-level crossing in the canonical matrix",
      record="Revision/kohn_sham/results/adiabatic/fermi-level-crossings.csv")
```

A colour scale, Figure 15c.6, and the check that none of the 60 rows of the record's crossing table (15 series, four steps between neighbouring slices) reports a change of the occupied set (Out [10]: 60 / 0).

**In [11], the last check.**

```python
NAMES = ["transition_orbitals", "q_by_pair", "q_history", "hellmann_feynman",
         "fermi_crossing", "q_map"]
missing = [name for number, name in enumerate(NAMES, start=1)
           if not output_file(f"{FIGURE_FOLDER}/15c_{number}_{name}.png").is_file()]
check(missing == [], "every figure file of this notebook exists")
all_checks_passed()
```

As in Notebook 15e (Section 15.9, In [15]), with the six figure names of this notebook in order and the file names `15c_<number>_<name>.png`: the names whose file does not exist are collected, the check requires that list to be empty, and `all_checks_passed()` prints the last line, ALL 12 CHECKS PASSED (notebook 15c).

### 15.26 The gas at a temperature

**Mermin's functional.** At a temperature $T > 0$ the particles no longer fill exactly the lowest levels. Mermin's finite-temperature form of Kohn-Sham theory (Chapter 13) occupies each level with the **Fermi-Dirac** probability

$$
f(x) = \frac{1}{1 + e^{x}}, \qquad x = \frac{\varepsilon - \mu}{T},
$$

where the **chemical potential** $\mu$ is fixed by the particle number, $\sum gf = N$. The function $f$ is 1 far below $\mu$, 0 far above, and $\tfrac12$ at $\varepsilon = \mu$; it falls from nearly 1 to nearly 0 over a few $T$ (Figure 15d.5 shows it). A useful identity: $1 - f(x) = f(-x)$, because $1 - \frac{1}{1 + e^x} = \frac{e^x}{1 + e^x} = \frac{1}{e^{-x} + 1}$. The functions of state of the doubled system are (ks-theory.json, thermodynamics):

$$
E = \sum g f\varepsilon - 2\,\mathrm{Vol}_7\!\int e^{6Hy}e_{int}\,dy, \qquad S = -\sum g\big[f\ln f + (1 - f)\ln(1 - f)\big],
$$

$$
F = E - TS, \qquad \Omega = -T\sum g\ln\big(1 + e^{-(\varepsilon - \mu)/T}\big) - 2\,\mathrm{Vol}_7\!\int e^{6Hy}e_{int}\,dy = F - \mu N ,
$$

the energy, the **entropy** (a measure of how many arrangements of the particles the occupations allow), the **free energy** and the **grand potential**. The last equality is Exercise 5. The self-consistent loop is the one of Section 15.5 with the Fermi-Dirac occupations in place of the aufbau. A note on the record: the theory file writes the particle-number condition as $\sum w g f = N$ with $w = \tfrac12$, which contradicts its own densities, energy and grand potential; the solver uses $\sum gf = N$, the particle number of the doubled system, and records the discrepancy (`Revision/kohn_sham/results/parameters.json`, conventions.particleNumber).

**The record's thermal states.** 135 states: $N = 8, 136, 688$, the couplings $0, \pm\lambda_1$, the five slices and $T = 0.01, 0.02, 0.05$ (Section 15.2). Their label sets contain every particle level whose free occupation is above $10^{-12}$ (the thermal window; check thermo_window_cut), and the solver checks $\sum gf = N$ to $3.1 \times 10^{-12}$ (check thermo_N_conservation), the two forms of $\Omega$ (check thermo_grand_potential_two_forms) and the identities $C_V = T\,dS/dT = dE/dT$ and $-dF/dT = S$ with differences between neighbouring temperatures (checks thermo_CV_identity and thermo_entropy_identity).

**The heat capacity in closed form.** The **heat capacity** $C_V = dE/dT$ at fixed $N$ says how much energy one unit of temperature costs. Without interaction the levels do not depend on $T$, and $C_V$ has a closed form. With the shorthand $f_i = f(x_i)$, $d_i = \varepsilon_i - \mu$ and $w_i = g_if_i(1 - f_i)$, line by line:

$$
\frac{df}{dx} = -\frac{e^x}{(1 + e^x)^2} = -f(1 - f) .
$$

Rule: the derivative of $1/(1 + e^x)$ by the chain rule; then $\frac{e^x}{(1 + e^x)^2} = \frac{1}{1 + e^x}\cdot\frac{e^x}{1 + e^x} = f\,(1 - f)$.

$$
\frac{dx_i}{dT} = -\frac{d_i}{T^2} - \frac{1}{T}\frac{d\mu}{dT} .
$$

Rule: $x_i = (\varepsilon_i - \mu)/T$ with fixed $\varepsilon_i$; the quotient rule, and $\mu$ changes with $T$ because $N$ is fixed.

$$
0 = \frac{dN}{dT} = \sum_i g_i\frac{df}{dx}(x_i)\frac{dx_i}{dT} = -\sum_i w_i\frac{dx_i}{dT}, \qquad \frac{d\mu}{dT} = -\frac{\sum_i w_id_i}{T\sum_i w_i} .
$$

Rule: differentiate $\sum g_if_i = N$; insert the first line; then insert the second line and solve for $d\mu/dT$.

$$
C_V = \frac{dE}{dT} = -\sum_i w_i\varepsilon_i\frac{dx_i}{dT} = -\sum_i w_id_i\frac{dx_i}{dT} = \frac{1}{T^2}\Big[\sum_i w_id_i^2 - \frac{(\sum_i w_id_i)^2}{\sum_i w_i}\Big] .
$$

Rule: differentiate $E = \sum g_if_i\varepsilon_i$ in the same way; replacing $\varepsilon_i$ by $d_i = \varepsilon_i - \mu$ subtracts $\mu\sum w_i\,dx_i/dT$, which is zero by the previous line; then insert the second line and the value of $d\mu/dT$. In the same way $dN/d\mu = \sum_i g_i\frac{df}{dx}(x_i)\cdot(-\tfrac1T) = \tfrac1T\sum_i w_i$ at fixed $T$.

**$T\,dS/dT = dE/dT$ and $-dF/dT = S$.** The entropy of one level is $-g[f\ln f + (1 - f)\ln(1 - f)]$; its derivative with respect to $f$ is $-g[\ln f + 1 - \ln(1 - f) - 1] = g\ln\frac{1 - f}{f} = g\,x$, because $\frac{1 - f}{f} = e^x$. So, line by line,

$$
\frac{dS}{dT} = \sum_i g_ix_i\frac{df}{dx}(x_i)\frac{dx_i}{dT} = -\sum_i w_ix_i\frac{dx_i}{dT} = -\frac{1}{T}\sum_i w_id_i\frac{dx_i}{dT} = \frac{1}{T}\frac{dE}{dT} .
$$

Rule: the chain rule with the derivative just found; $df/dx = -f(1 - f)$; $x_i = d_i/T$; and the previous derivation of $dE/dT$. Hence $C_V = T\,dS/dT$, and $\frac{dF}{dT} = \frac{dE}{dT} - S - T\frac{dS}{dT} = -S$ (the product rule on $TS$). The solver reports $C_V$ as $T\,dS/dT$, because the entropy is computed from the occupations and is well conditioned, while $dE/dT$ is a difference of nearly equal energies.

**The two-level formula for $N = 8$.** At $a_{4,0} = 0$ and low temperature only two groups of levels matter for $N = 8$: the eight zero modes at $\varepsilon = 0$ and the 24 orbitals of the first band shell at $\varepsilon = \Delta = 0.4307$ (the gap). The particles that leave the zero modes must enter the band, line by line:

$$
8\,\big(1 - f(-\mu/T)\big) = 24\,f\big((\Delta - \mu)/T\big) .
$$

Rule: the holes in the zero modes equal the particles in the band, because $N$ is fixed.

$$
8\,e^{-\mu/T} = 24\,e^{-(\Delta - \mu)/T} .
$$

Rule: $1 - f(x) = f(-x)$, and $f(x) \approx e^{-x}$ for $x \gg 1$; here $\mu/T$ and $(\Delta - \mu)/T$ are about 21 and 22.

$$
\ln 8 - \frac{\mu}{T} = \ln 24 - \frac{\Delta - \mu}{T}, \qquad \mu = \frac{\Delta}{2} - \frac{T}{2}\ln 3 .
$$

Rule: take the logarithm of both sides; collect $\mu$ on one side ($-2\mu/T = \ln 3 - \Delta/T$, since $\ln 24 - \ln 8 = \ln 3$) and divide by $-2/T$. At $T \to 0$ the chemical potential sits in the middle of the gap; it falls linearly with the slope $-\tfrac12\ln 3$, the logarithm of the ratio of the degeneracies. At $T = 0.01$ the formula gives $0.209873777875$, the record $0.209873776387$ (Notebook 15d, Out [5]); the difference $1.5 \times 10^{-9}$ is the size of the neglected terms.

**Why $\mu$ must be computed with care.** Near a closed shell at low temperature almost every level is either full or empty. The direct count $\sum gf - N$ then adds numbers very close to 1 and subtracts $N$; in double precision (the computer's numbers, about 16 significant digits) the result is only known to about $\epsilon\,N$, where $\epsilon = 2^{-52} = 2.2 \times 10^{-16}$ is the rounding unit, while the count changes with $\mu$ only at the rate $dN/d\mu$. A root of the direct count is therefore uncertain by about $\epsilon N/(dN/d\mu)$. For $N = 8$ at $a_{4,0} = 0$, $T = 0.01$ the record has $dN/d\mu = 1.23 \times 10^{-6}$ (`Revision/kohn_sham/results/thermo/thermodynamics.csv`), so this uncertainty is $2.2 \times 10^{-16}\cdot8/(1.23 \times 10^{-6}) = 1.4 \times 10^{-9}\,m$, a million times worse than the rounding unit. An earlier version of the solver used the direct count, and the independent cross-check of Chapter 16 found its $\mu$ off by $8.3 \times 10^{-10}\,m$ in the state `N8_lamm1_a00_T10` (`Revision/kohn_sham/solver/README.md`, History).

**The balance form, line by line.** Let $\mathcal S$ be the set of the levels that are filled at $T = 0$ and $d = N - \sum_{\mathcal S}g$ (zero for a closed shell). Then

$$
\sum_i g_if(x_i) - N = \sum_{i \notin \mathcal S}g_if(x_i) + \sum_{i \in \mathcal S}g_i\big(1 - f(-x_i)\big) - N = P - H_l - d ,
$$

with the thermal particles above the filled levels $P = \sum_{i \notin \mathcal S}g_if(x_i)$ and the thermal holes below them $H_l = \sum_{i \in \mathcal S}g_if(-x_i)$. Rule: split the sum into the levels outside and inside $\mathcal S$; inside use $f(x) = 1 - f(-x)$; then $\sum_{\mathcal S}g_i - N = -d$. The condition $\sum gf = N$ becomes $P = H_l + d$, and for a closed shell simply $\ln P = \ln H_l$: the thermal particles balance the thermal holes. No numbers close to 1 are added and no large number is subtracted; each hole factor is computed as $f(-x)$ directly, never as $1 - f$. The solver solves $\ln(P + d_-) - \ln(H_l + d_+) = 0$ with $d_\pm = \max(\pm d, 0)$, adding each sum in the form $\ln\sum e^{t_i} = t_{max} + \ln\sum e^{t_i - t_{max}}$ (the **log-sum-exp**, which never overflows or underflows), by Newton's method in a bracket and then bisection down to neighbouring double-precision numbers (`Revision/kohn_sham/solver/src/mermin.rs`). The record checks every one of the 135 roots against a root computed with 40 significant digits by mpmath: all lie within their rounding bound, the largest difference is $2.4 \times 10^{-16}\,m$ (`Revision/kohn_sham/reports/ks-rust-mermin-roots.json`, check solver_mu_within_rounding_bound).

**The sea holes: where the filling convention stops being reasonable.** The CONVENTION of Section 15.2 never occupies the negative branch, not even thermally. How good is that? Without interaction the sea's brane band (block type $j = -1$, even parity, label 0) has the levels $-\varepsilon_{band}(n_2)$ (Section 15.4). If the sea were treated thermally, each of its orbitals would be empty with the probability $1 - f\big((-\varepsilon_{band} - \mu)/T\big) = f\big((\varepsilon_{band} + \mu)/T\big) = 1/(1 + e^{(\mu + \varepsilon_{band})/T})$; such an empty sea orbital is a **thermal hole**, which a full quantum treatment would count as an antiparticle of the same universe. The record computes the number of these holes for every thermal state as a DIAGNOSTIC (check thermo_sea_hole_diagnostic_computed): it exceeds 1 per cent of $N$ in 15 of the 135 states, all at $a_{4,0} \ge 1$, and reaches $30.98\,N$ in `N8_lamm1_a20_T50` ($N = 8$, $-\lambda_1$, $a_{4,0} = 2$, $T = 0.05$). There the band has been squeezed so close to $\varepsilon = 0$ that the temperature excites the sea as easily as the particles, $\mu$ itself is negative ($-0.0977$), and the particle-only ensemble is outside its range of validity; a thermal treatment of the sea is OPEN. These thermal holes are excitations inside one universe; they say nothing about pairs of universes or about the matter-antimatter asymmetry.

### 15.27 Example: thermodynamics (Notebook 15d)

Notebook 15d runs the solver's command `single` for 20 free thermal states ($N = 8$ and $136$) and reads their final levels exactly. From these levels alone it recomputes, in plain Python, the chemical potential (with mpmath at 40 digits), $E$, $S$, $F$, $\Omega$, $C_V$ and $dN/d\mu$, and compares them with the record. It shows why the direct count is too coarse (Figure 15d.1), draws $\mu(T)$ with the two-level formula (Figure 15d.2), $F$ and $S$ along the history (Figure 15d.3), the heat capacity (Figure 15d.4), the occupations (Figure 15d.5), the sea-hole diagnostic (Figure 15d.6) and the effect of the interaction on $F$ (Figure 15d.7). It needs Rust, takes about half a minute, and ends with ALL 15 CHECKS PASSED (notebook 15d).

What to look for: in Figure 15d.1 the orange staircase of the double-precision count against the smooth blue line of the exact count; in Figure 15d.2 the straight start of $\mu(T)$ from the middle of the gap; in Figure 15d.4 how the heat capacity of $N = 8$ wakes up at ever lower temperatures as the history closes the gap; in Figure 15d.6 the values above the 1 per cent line late in the history.

<!-- NOTEBOOK 15d -->

### 15.30 Line-by-line walk-through of Notebook 15d

The notebook has 11 code cells, In [1] to In [11]; the complete cells are printed in Section 15.29.

**In [1], the set-up cell.** It is the set-up cell of Notebook 15a (Section 15.14 for the Rust lines, Section 15.9 for the rest), with the run instructions of this notebook (Section 15.28) in its comments and `NOTEBOOK_ID = "15d"`.

**In [2], the solver and the free thermal states.**

```python
import csv  # reads the tables (CSV files)
import math  # exp, log for single numbers

import mpmath  # numbers with 40 digits
import numpy as np  # arrays of numbers

program = rust_program("Revision/kohn_sham/solver/Cargo.toml", "revision_ks_solver")
RUN_FOLDER = REPO / "Revision/kohn_sham/solver/target/textbook_15d"  # git ignores it
RUN_FOLDER.mkdir(parents=True, exist_ok=True)
```

The imports, among them mpmath, a package for numbers with as many digits as asked for; the solver is built, and the folder `textbook_15d` inside its build folder receives this notebook's runs.

```python
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
SHADES = {0.0: "#86b6ef", 0.5: "#5598e7", 1.0: "#2a78d6", 1.5: "#1c5cab",
          2.0: "#104281"}  # one shade of blue per slice, light to dark
TEMPS = (0.01, 0.02, 0.05)


def state_id(n, a4, t, tag="lam0"):
    return f"N{n}_{tag}_a{round(10 * a4):02d}_T{round(1000 * t)}"
```

The colours, one shade per slice in a dictionary, the three temperatures of the record, and the names of the thermal states, for example `N8_lam0_a00_T10` for $N = 8$, $\lambda = 0$, $a_{4,0} = 0$, $T = 0.01$.

```python
def thermal_state(n, a4, t):
    name = state_id(n, a4, t)
    out, lev = RUN_FOLDER / f"{name}.json", RUN_FOLDER / f"{name}-levels.json"
    done = subprocess.run(
        [str(program), "single", "--root", str(REPO), "--m", "1", "--lambda", "0",
         "--a4", repr(a4), "--N", repr(float(n)), "--T", repr(t), "--margin", "0.2",
         "--out", str(out), "--mermin-levels", str(lev)],
        capture_output=True, text=True)
    if done.returncode != 0:
        raise RuntimeError(f"the solver failed for {name}: {done.stderr[-500:]}")
```

`thermal_state` runs `single` for one free thermal state. Compared with Notebook 15b it adds the temperature, the margin 0.2 of the canonical thermal runs (so that the label set, and therefore the state, is exactly the recorded one), and the option that writes the final levels and $\mu$ into a second file as decimal numbers that read back into exactly the solver's double-precision numbers.

```python
    exact = json.loads(lev.read_text(encoding="utf-8"))
    full = json.loads(out.read_text(encoding="utf-8"))
    eps = [float(e) for e, _ in exact["levels_eps_deg"]]  # exactly the solver's
    deg = [float(g) for _, g in exact["levels_eps_deg"]]
    return float(exact["mu"]), eps, deg, full["levels_n2_j_parity_label_eps_deg_f"]
```

The two files are read; `eps` and `deg` are the levels and their degeneracies, and the function returns the solver's $\mu$, these two lists, and the full level list (shell, block type, parity, label, energy, degeneracy, occupation) from the main JSON file.

```python
THERMO = "Revision/kohn_sham/results/thermo/thermodynamics.csv"
with open(repository_file(THERMO), newline="", encoding="utf-8") as handle:
    record = {row["id"]: row for row in csv.DictReader(handle)}
states = {}
for n in (8, 136):
    for a4 in (0.0, 1.0, 2.0):
        for t in TEMPS:
            states[(n, a4, t)] = thermal_state(n, a4, t)
for a4 in (0.5, 1.5):
    states[(136, a4, 0.05)] = thermal_state(136, a4, 0.05)
```

The record's table of the 135 thermal states is read, and 20 free states are computed: $N = 8$ and $136$ at the slices 0, 1, 2 and the three temperatures (18 states), and $N = 136$ at $a_{4,0} = 0.5$ and $1.5$ with $T = 0.05$.

```python
worst_mu = max(abs(mu - float(record[state_id(n, a4, t)]["mu"]))
               for (n, a4, t), (mu, _, _, _) in states.items())
report("free thermal states computed", len(states))
report("largest |mu(solver now) - mu(record)|", f"{worst_mu:.1e}")
check(worst_mu < 1e-12, f"the solver reproduces the recorded mu of {len(states)} states",
      record=f"{THERMO}, column mu")
```

Out [2]: 20 states, and the new $\mu$ agrees with the record to $5.6 \times 10^{-17}$ (the record's column holds 16 significant digits).

**In [3], the 40-digit root and the functions of state.**

```python
def exact_root(eps, deg, n, t, guess):
    with mpmath.workdps(40):
        levels = [(mpmath.mpf(e), mpmath.mpf(g)) for e, g in zip(eps, deg)]
        temp, mu = mpmath.mpf(t), mpmath.mpf(guess)
        for _ in range(60):
            occ = [(g, 1 / (1 + mpmath.exp((e - mu) / temp))) for e, g in levels]
            count = sum(g * f for g, f in occ) - n
            slope = sum(g * f * (1 - f) for g, f in occ) / temp  # dN/dmu
            step = count / slope
            mu -= step
            if abs(step) < mpmath.mpf(10) ** -36:
                break
        return mu
```

`exact_root` solves $\sum gf = N$ with 40 significant digits: inside `with mpmath.workdps(40):` every mpmath number (`mpmath.mpf`) carries 40 digits. Starting at the solver's $\mu$, Newton's method takes the step $(\sum gf - N)/(dN/d\mu)$ with $dN/d\mu = \sum gf(1 - f)/T$ (Section 15.26), at most 60 times, until the step is below $10^{-36}$. With 40 digits the subtraction of $N$ loses nothing that matters.

```python
def functions_of_state(eps, deg, mu, t):
    e, g = np.array(eps), np.array(deg)
    x = (e - mu) / t
    small = np.exp(-np.abs(x))  # e^{-|x|}, never overflows
    f_abs = small / (1.0 + small)  # f(|x|)
    f = np.where(x > 0, f_abs, 1.0 - f_abs)  # f(x)
    energy = float(np.sum(g * f * e))
```

`functions_of_state` computes the functions of state of a free state in double precision, in forms that never overflow. `small` is $e^{-|x|}$, at most 1; `f_abs` is $f(|x|) = e^{-|x|}/(1 + e^{-|x|})$; `np.where(condition, a, b)` takes $a$ where the condition holds and $b$ elsewhere, so `f` is $f(x)$ ($f(|x|)$ for $x > 0$ and $1 - f(|x|)$ otherwise). The energy is $\sum gf\varepsilon$ (no interaction).

```python
    # -[f ln f + (1-f) ln(1-f)] = ln(1 + e^{-|x|}) + |x| f(|x|)
    entropy = float(np.sum(g * (np.log1p(small) + np.abs(x) * f_abs)))
    # ln(1 + e^{-x}) = max(-x, 0) + ln(1 + e^{-|x|})
    omega = -t * float(np.sum(g * (np.maximum(-x, 0.0) + np.log1p(small))))
```

The two comment lines state the formulas that the next lines use. The entropy of one level is $-[f\ln f + (1 - f)\ln(1 - f)] = \ln(1 + e^{-|x|}) + |x|\,f(|x|)$. (For $x \ge 0$: $\ln f = -x - \ln(1 + e^{-x})$ and $\ln(1 - f) = -\ln(1 + e^{-x})$; inserting, the two logarithms add to $\ln(1 + e^{-x})$ and the rest is $xf$; for $x < 0$ the roles of $f$ and $1 - f$ exchange.) `np.log1p(s)` is $\ln(1 + s)$, accurate also for tiny $s$. The grand potential uses $\ln(1 + e^{-x}) = \max(-x, 0) + \ln(1 + e^{-|x|})$.

```python
    w = g * f_abs * (1.0 - f_abs)  # g f (1 - f), the same for x and -x
    d = e - mu
    cv = float((np.sum(w * d * d) - np.sum(w * d) ** 2 / np.sum(w)) / t ** 2)
    return energy, entropy, energy - t * entropy, omega, cv, float(np.sum(w) / t)
```

`w` is $w_i = g_if_i(1 - f_i)$ (the product $f(1 - f)$ is the same for $x$ and $-x$), `cv` the closed form of $C_V$ derived in Section 15.26, and the function returns $E$, $S$, $F = E - TS$, $\Omega$, $C_V$ and $dN/d\mu = \sum w/T$.

```python
rel = lambda a, b: abs(a - b) / max(abs(b), 1.0)  # relative to max(|b|, 1)
worst = {"root": 0.0, "E S F Omega": 0.0, "C_V": 0.0, "dN/dmu": 0.0}
for (n, a4, t), (mu, eps, deg, _) in states.items():
    row = record[state_id(n, a4, t)]
    root = exact_root(eps, deg, n, t, mu)
    worst["root"] = max(worst["root"],
                        float(abs(mu - root)) / float(row["mu_rounding_bound"]))
    e_, s_, f_, o_, cv, dn = functions_of_state(eps, deg, mu, t)
    worst["E S F Omega"] = max(worst["E S F Omega"], rel(e_, float(row["E"])),
                               rel(s_, float(row["entropy"])), rel(f_, float(row["F"])),
                               rel(o_, float(row["Omega_direct"])))
    worst["C_V"] = max(worst["C_V"], abs(cv / float(row["C_V"]) - 1.0))
    worst["dN/dmu"] = max(worst["dN/dmu"], abs(dn / float(row["dN_dmu"]) - 1.0))
```

For each of the 20 states: the 40-digit root, the distance of the solver's $\mu$ from it measured in units of the recorded rounding bound (column `mu_rounding_bound`, the solver's first-order estimate of the rounding error of its root), and the functions of state compared with the record's columns (relative to the larger of the value and 1). The dictionary `worst` keeps the largest deviation of each kind.

```python
report("largest |mu - 40-digit root| / recorded rounding bound", f"{worst['root']:.2f}")
for key in ("E S F Omega", "C_V", "dN/dmu"):
    report(f"largest relative difference, {key}", f"{worst[key]:.1e}")
check(worst["root"] <= 1.0, "mu lies within its rounding bound of the 40-digit root",
      record="Revision/kohn_sham/reports/ks-rust-mermin-roots.json and "
             f"{THERMO}, column mu_rounding_bound")
check(worst["E S F Omega"] < 1e-12,
      f"E, S, F and Omega of {len(states)} states reproduced",
      record=f"{THERMO}, columns E, entropy, F, Omega_direct")
check(worst["C_V"] < 1e-4, "the closed-form C_V reproduces the recorded T dS/dT",
      record=f"{THERMO}, column C_V")
check(worst["dN/dmu"] < 1e-9, "dN/dmu reproduced", record=f"{THERMO}, column dN_dmu")
```

Out [3]: $\mu$ lies within $0.07$ of its rounding bound of the exact root; $E$, $S$, $F$, $\Omega$ agree to $3.6 \times 10^{-14}$; the closed-form $C_V$ agrees with the record's Richardson difference $T\,dS/dT$ to $1.6 \times 10^{-5}$ (the accuracy of the difference quotient); $dN/d\mu$ to $2.0 \times 10^{-15}$. All four checks pass.

**In [4], why the balance is needed.**

```python
def balance_root(eps, deg, n, t):
    order = np.argsort(eps, kind="stable")
    e, g = np.array(eps)[order], np.array(deg)[order]
    filled = int(np.searchsorted(np.cumsum(g), n - 1e-9)) + 1  # T = 0 filling
    below_e, below_g, above_e, above_g = e[:filled], g[:filled], e[filled:], g[filled:]
```

`balance_root` finds $\mu$ from the balance of Section 15.26 in double precision. The levels are sorted by energy (`np.argsort` gives the order; `kind="stable"` keeps equal levels in their original order). `np.cumsum(g)` is the running total of the degeneracies, and `np.searchsorted` finds the position where it reaches $N$; the first `filled` levels are the set $\mathcal S$ filled at $T = 0$ (the states here are closed shells, so $d = 0$).

```python
    def log_sum(log_terms):  # ln(sum e^{t}) without overflow or underflow
        top = float(np.max(log_terms))
        return top + math.log(float(np.sum(np.exp(log_terms - top))))

    def log_f(x):  # ln f(x) = -ln(1 + e^{x}), stable for every x
        return -(np.maximum(x, 0.0) + np.log1p(np.exp(-np.abs(x))))
```

`log_sum` is the log-sum-exp $\ln\sum e^{t_i} = t_{max} + \ln\sum e^{t_i - t_{max}}$, in which every exponential is at most 1. `log_f` is $\ln f(x) = -\ln(1 + e^x) = -[\max(x, 0) + \ln(1 + e^{-|x|})]$, which works for every $x$, however large.

```python
    def balance(mu):
        return (log_sum(np.log(above_g) + log_f((above_e - mu) / t))
                - log_sum(np.log(below_g) + log_f(-(below_e - mu) / t)))

    lo, hi = float(e[0]) - 1.0, float(e[-1]) + 1.0
    while lo < 0.5 * (lo + hi) < hi:  # bisection down to neighbouring numbers
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if balance(mid) < 0.0 else (lo, mid)
    return lo
```

`balance(mu)` is $\ln P - \ln H_l$: each term $g\,f$ is written as $e^{\ln g + \ln f}$, so that $\ln P = $ log-sum-exp of $\ln g + \ln f(x)$ over the levels above, and $\ln H_l$ the same with $f(-x)$ over the levels below. It increases with $\mu$ (more particles above, fewer holes below). Bisection between a value below all levels and one above them halves the interval until its midpoint is no longer strictly between its ends, that is, until `lo` and `hi` are neighbouring double-precision numbers.

```python
mu8, eps8, deg8, _ = states[(8, 0.0, 0.01)]
root8 = exact_root(eps8, deg8, 8, 0.01, mu8)
offsets = np.linspace(-3e-9, 3e-9, 61)
direct, exact = [], []
for off in offsets:
    x = (np.array(eps8) - (mu8 + off)) / 0.01
    direct.append(float(np.sum(np.array(deg8) / (1.0 + np.exp(x)))) - 8.0)
    with mpmath.workdps(40):
        m_ = mpmath.mpf(mu8) + mpmath.mpf(off)
        exact.append(float(sum(mpmath.mpf(g) / (1 + mpmath.exp((mpmath.mpf(e) - m_)
                                                                / mpmath.mpf(0.01)))
                               for e, g in zip(eps8, deg8)) - 8))
```

For the activated state $N = 8$, $a_{4,0} = 0$, $T = 0.01$ the cell evaluates the count $\sum gf - 8$ at 61 values of $\mu$ within $\pm 3 \times 10^{-9}$ of the solver's $\mu$: once directly in double precision (`direct`) and once with 40 digits (`exact`).

```python
fig, ax = plt.subplots()
ax.plot(offsets * 1e9, direct, "s-", color=PALETTE[1], ms=4, lw=1.2,
        label="direct count, double precision")
ax.plot(offsets * 1e9, exact, color=PALETTE[0], lw=2.0, label="exact count, 40 digits")
ax.axvline(float(root8 - mu8) * 1e9, color="0.3", ls=":", lw=1.2, label="exact root")
ax.axhline(0.0, color="0.6", lw=0.8)
ax.set_xlabel("$\\mu$ minus the solver's $\\mu$ (units of $10^{-9}\\,m$)")
ax.set_ylabel("$\\sum g f - N$")
ax.set_title("$N = 8$, $a_{4,0} = 0$, $T = 0.01$: the direct count is too coarse")
ax.legend(fontsize=8)
```

Both counts are drawn against the offset in units of $10^{-9}$, with the exact root as a dotted vertical line and a zero line.

```python
zero_at = [off for off, value in zip(offsets, direct) if value == 0.0]  # direct = 0
if zero_at:  # where the double-precision count says "exactly N particles"
    miss = min(abs(off - float(root8 - mu8)) for off in zero_at)  # nearest such point
    where = ("is zero only on a short interval that misses the true root by at "
             f"least ${miss * 1e10:.0f} \\times 10^{{-10}}\\,m$")
    report("distance of the zeros of the direct count from the true root",
           f"at least {miss:.1e} m")
else:  # (on another computer the rounding steps may fall differently)
    where = "is never exactly zero at the sampled points"
save_figure(fig, "root_conditioning",
            "The particle-number condition $\\sum g f - N$ (vertical axis, of size "
...)
```

`zero_at` collects the sampled values of $\mu$ at which the double-precision count is exactly zero; `miss` is the smallest distance of such a point from the true root. The caption of Figure 15d.1 is completed with a sentence that depends on what was found (on another computer the rounding steps may fall differently). Out [4] reports that these zeros miss the true root by at least $3.0 \times 10^{-10}\,m$.

```python
worst_balance = 0.0
for (n, a4, t), (mu, eps, deg, _) in states.items():
    root = exact_root(eps, deg, n, t, mu)
    worst_balance = max(worst_balance, float(abs(balance_root(eps, deg, n, t) - root)))
zero_width = (np.sum(np.array(direct) == 0.0)) * (offsets[1] - offsets[0])
report("width of the interval where the double-precision direct count is 0",
       f"{zero_width:.1e} m")
report(f"largest |balance root - 40-digit root| ({len(states)} states)",
       f"{worst_balance:.1e}")
check(worst_balance < 1e-15, "the double-precision balance finds mu to 1e-15",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "thermo_mu_well_conditioned_root")
```

For all 20 states the root of the balance is compared with the 40-digit root, and the width of the interval where the direct count is zero is estimated from the number of sampled zeros times the spacing. Out [4]: the width is $3.0 \times 10^{-10}\,m$, while the balance finds every root to $9.3 \times 10^{-17}\,m$, about three million times better. In Figure 15d.1 the orange squares jump in steps of the rounding unit of $N$ (size $10^{-15}$) while the blue line crosses zero at one point.

**In [5], the chemical potential against the temperature.**

```python
T_GRID = np.linspace(0.002, 0.05, 49)


def curves(n, a4):
    _, eps, deg, _ = states[(n, a4, 0.05)]
    rows = []
    for t in T_GRID:
        mu = balance_root(eps, deg, n, t)
        energy, entropy, free, _, cv, _ = functions_of_state(eps, deg, mu, t)
        rows.append((mu, energy, entropy, free, cv))
    return np.array(rows)  # columns: mu, E, S, F, C_V
```

`T_GRID` holds 49 temperatures from 0.002 to 0.05. `curves` takes the levels of the state at $T = 0.05$ (the largest thermal window; at lower temperatures the extra levels are empty far below the rounding) and computes $\mu$, $E$, $S$, $F$ and $C_V$ at every temperature of the grid, returned as an array with one row per temperature.

```python
GROUND = "Revision/kohn_sham/results/ground/summary.csv"
with open(repository_file(GROUND), newline="", encoding="utf-8") as handle:
    ground = {row["id"]: row for row in csv.DictReader(handle)}
gap8 = float(ground["N8_lam0_a00"]["KS_gap"])
two_level = gap8 / 2.0 - 0.5 * T_GRID * math.log(3.0)
curve8 = {a4: curves(8, a4) for a4 in (0.0, 1.0, 2.0)}
```

The gap $\Delta = 0.4307337$ of `N8_lam0_a00` is read from the record's ground-state table, the two-level formula $\Delta/2 - (T/2)\ln 3$ of Section 15.26 is evaluated on the grid, and the curves of $N = 8$ are computed at three slices.

```python
fig, ax = plt.subplots()
for a4 in (0.0, 1.0, 2.0):
    ax.plot(T_GRID, curve8[a4][:, 0], color=SHADES[a4], lw=2.0,
            label=f"$a_{{4,0}} = {a4:.0f}$")
    ax.plot(TEMPS, [float(record[state_id(8, a4, t)]["mu"]) for t in TEMPS], "o",
            color=SHADES[a4], ms=8, markerfacecolor="white")
ax.plot(T_GRID, two_level, "--", color=PALETTE[1], lw=1.5,
        label="$\\Delta/2 - (T/2)\\ln 3$, $a_{4,0} = 0$")
ax.plot([], [], "o", color="0.4", markerfacecolor="white", label="record")
ax.set_xlabel("temperature $T$ (units of $m$)")
ax.set_ylabel("chemical potential $\\mu$ (units of $m$)")
ax.set_title("$N = 8$, $\\lambda = 0$: the chemical potential")
ax.legend(fontsize=8)
save_figure(fig, "chemical_potential",
            "The chemical potential $\\mu$ (vertical axis, units of $m$) of the free "
...)
```

$\mu(T)$ at the three slices (`curve8[a4][:, 0]` is the first column of the array), the record's values as open circles, and the two-level formula dashed; then Figure 15d.2.

```python
formula = gap8 / 2.0 - 0.005 * math.log(3.0)
recorded = float(record[state_id(8, 0.0, 0.01)]["mu"])
report("mu of N8_lam0_a00_T10: two-level formula / record",
       f"{formula:.12f} / {recorded:.12f}")
check(abs(formula - recorded) < 1e-8, "the two-level formula gives mu to 1e-8",
      record=f"{THERMO}, N8_lam0_a00_T10")
```

The formula at $T = 0.01$ ($T/2 = 0.005$): $0.209873777875$ against the record's $0.209873776387$ (Out [5]); the check passes. In the figure, $\mu$ starts at $\Delta/2$ and falls along the dashed line; at the later slices the gap and with it $\mu$ are smaller.

**In [6], free energy and entropy.**

```python
curve136 = {a4: curves(136, a4) for a4 in (0.0, 0.5, 1.0, 1.5, 2.0)}
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
for a4, values in curve136.items():
    e0 = float(ground[f"N136_lam0_a{round(10 * a4):02d}"]["E_KS"])
    left.plot(T_GRID, values[:, 3] - e0, color=SHADES[a4], lw=2.0,
              label=f"$a_{{4,0}} = {a4}$")
    right.plot(T_GRID, values[:, 2], color=SHADES[a4], lw=2.0)
```

The curves of $N = 136$ at the five slices; on the left the free energy measured from the ground-state energy $E_0$ of the same slice (column 3 of the curves minus `e0`), on the right the entropy (column 2).

```python
    if a4 in (0.0, 1.0, 2.0):
        ids = [state_id(136, a4, t) for t in TEMPS]
        left.plot(TEMPS, [float(record[i]["F"]) - e0 for i in ids], "o",
                  color=SHADES[a4], ms=7, markerfacecolor="white")
        right.plot(TEMPS, [float(record[i]["entropy"]) for i in ids], "o",
                   color=SHADES[a4], ms=7, markerfacecolor="white")
left.set_xlabel("temperature $T$")
left.set_ylabel("$F - E_0$ (units of $m$)")
left.set_title("Free energy, $N = 136$, $\\lambda = 0$")
left.legend(fontsize=8)
right.set_xlabel("temperature $T$")
right.set_ylabel("entropy $S$")
right.set_title("Entropy (circles: record)")
save_figure(fig, "free_energy_entropy",
            "Left: the free energy measured from the ground-state energy, "
...)
```

Where the record has thermal states (slices 0, 1, 2), its values are drawn as open circles; then the labels and Figure 15d.3.

```python
_, eps, deg, _ = states[(136, 1.0, 0.05)]
worst_fs = 0.0
for t in T_GRID:
    h = 1e-3 * t
    f_plus = functions_of_state(eps, deg, balance_root(eps, deg, 136, t + h), t + h)[2]
    f_minus = functions_of_state(eps, deg, balance_root(eps, deg, 136, t - h), t - h)[2]
    s = functions_of_state(eps, deg, balance_root(eps, deg, 136, t), t)[1]
    worst_fs = max(worst_fs, abs(-(f_plus - f_minus) / (2 * h) - s) / s)
```

The identity $-dF/dT = S$ of Section 15.26 is tested for $N = 136$ at $a_{4,0} = 1$ at every temperature of the grid: the central difference $[F(T + h) - F(T - h)]/(2h)$ with $h = 10^{-3}T$ (each $F$ at its own $\mu$; index 2 of the returned tuple is $F$, index 1 is $S$) is compared with $S$.

```python
report("largest relative |-dF/dT - S|, N = 136, a4,0 = 1", f"{worst_fs:.1e}")
check(worst_fs < 1e-4, "-dF/dT = S along the whole temperature grid",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "thermo_entropy_identity")
rising = all(bool(np.all(np.diff(v[:, 2]) > 0)) and bool(np.all(np.diff(v[:, 3]) < 0))
             for v in curve136.values())
check(rising, "S rises and F falls with T at every slice")
```

Out [6]: the largest relative deviation is $7.5 \times 10^{-6}$; and at every slice $S$ rises and $F$ falls with $T$ at every step of the grid. In Figure 15d.3 the later slices (darker) have the larger entropy at the same temperature: the history crowds the levels together, so the same temperature excites more particles.

**In [7], the heat capacity.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
for a4, values in curve8.items():
    left.plot(T_GRID, values[:, 4], color=SHADES[a4], lw=2.0,
              label=f"$a_{{4,0}} = {a4:.0f}$")
    left.plot(TEMPS, [float(record[state_id(8, a4, t)]["C_V"]) for t in TEMPS], "o",
              color=SHADES[a4], ms=7, markerfacecolor="white")
for a4, values in curve136.items():
    right.plot(T_GRID, values[:, 4], color=SHADES[a4], lw=2.0,
               label=f"$a_{{4,0}} = {a4}$")
    if a4 in (0.0, 1.0, 2.0):
        right.plot(TEMPS, [float(record[state_id(136, a4, t)]["C_V"]) for t in TEMPS],
                   "o", color=SHADES[a4], ms=7, markerfacecolor="white")
```

The closed-form $C_V$ (column 4 of the curves) of $N = 8$ at three slices on the left and of $N = 136$ at five slices on the right, with the record's values as circles.

```python
for ax, n in ((left, 8), (right, 136)):
    ax.set_yscale("log")
    ax.set_xlabel("temperature $T$ (units of $m$)")
    ax.set_title(f"Heat capacity, $N = {n}$, $\\lambda = 0$")
    ax.legend(fontsize=8)
left.set_ylabel("$C_V$ (pure number)")
save_figure(fig, "heat_capacity",
            "The heat capacity $C_V = dE/dT$ (vertical axis, logarithmic, pure "
...)
positive = all(bool(np.all(v[:, 4] > 0)) for v in list(curve8.values())
               + list(curve136.values()))
check(positive, "C_V > 0 at every temperature and slice")
```

Both panels get a logarithmic axis, labels and a legend; Figure 15d.4; and the check that $C_V$ is positive everywhere (the closed form is a weighted variance of the $d_i$ divided by $T^2$, so it cannot be negative). In the figure the gas $N = 8$ at $a_{4,0} = 0$ is **activated**: its heat capacity is tiny below $T \approx 0.02$, because each excitation costs the gap $0.43\,m$ and is suppressed like $e^{-\Delta/(2T)}$; as the history closes the gap, the heat capacity wakes up at ever lower temperatures. $N = 136$, with its much smaller gap, has a large heat capacity already at $T = 0.01$.

**In [8], the occupations.**

```python
fig, ax = plt.subplots()
sums = []
for colour, t in zip(PALETTE, TEMPS):
    mu, eps, deg, levels = states[(136, 1.0, t)]
    e = np.array(eps)
    f = 1.0 / (1.0 + np.exp(np.minimum((e - mu) / t, 700.0)))
    sums.append(float(np.sum(np.array(deg) * f)))
    order = np.argsort(e)
    ax.plot(e[order], f[order], "o-", color=colour, ms=4, lw=1.0, label=f"$T = {t}$")
    ax.axvline(mu, color=colour, ls=":", lw=1.2)
```

For $N = 136$ at $a_{4,0} = 1$ and the three temperatures the occupation $f$ of every level is computed (`np.minimum(..., 700.0)` caps the exponent, because $e^{710}$ would overflow), the sum $\sum gf$ is kept, and $f$ is drawn against the level, sorted by energy, with $\mu$ as a dotted vertical line.

```python
ax.set_xlim(0.2, 0.5)
ax.set_xlabel("level $\\varepsilon$ (units of $m$)")
ax.set_ylabel("occupation $f$")
ax.set_title("$N = 136$, $a_{4,0} = 1$: Fermi-Dirac occupations (dotted: $\\mu$)")
ax.legend()
save_figure(fig, "occupations",
            "The occupation $f$ of the levels of the free state $N = 136$ at "
...)
report("sum g f at the three temperatures", ", ".join(f"{s:.12f}" for s in sums))
check(max(abs(s - 136.0) for s in sums) < 1e-9, "the occupations add up to N = 136",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "thermo_N_conservation")
```

The horizontal range is limited to the levels near the Fermi level ($0.2$ to $0.5$); Figure 15d.5; Out [8]: the sums are $136.000000000000$ at all three temperatures. In the figure the step from full to empty widens with $T$.

**In [9], the sea holes.**

```python
def shell_sizes(largest):
    reach = math.isqrt(largest) + 1
    sizes = {}
    for x in range(-reach, reach + 1):
        for y in range(-reach, reach + 1):
            for z in range(-reach, reach + 1):
                s = x * x + y * y + z * z
                if s <= largest:
                    sizes[s] = sizes.get(s, 0) + 1
    return sizes
```

`shell_sizes` counts $r_3(n_2)$ for all $n_2$ up to `largest` by brute force: it visits every vector of whole numbers in a cube large enough (`math.isqrt` is the whole-number square root) and adds one to the count of its $n_2 = x^2 + y^2 + z^2$.

```python
worst_sea, mine = 0.0, {}
for a4 in (0.0, 1.0, 2.0):
    mu, _, _, levels = states[(8, a4, 0.05)]
    band = {lv[0]: lv[4] for lv in levels
            if lv[1] == 1 and lv[2] == "even" and lv[3] == 0 and lv[0] >= 1}
    sizes = shell_sizes(max(lv[0] for lv in levels))
    holes = sum(4 * sizes[n2] / (1.0 + math.exp((mu + band[n2]) / 0.05))
                for n2 in sizes if n2 >= 1)
    mine[a4] = holes / 8.0
    recorded = float(record[state_id(8, a4, 0.05)]["sea_holes_excluded"])
    worst_sea = max(worst_sea, abs(holes / recorded - 1.0))
```

For $N = 8$ at $T = 0.05$ and three slices: `band` maps each shell $n_2 \ge 1$ to its band level ($j = +1$, even, label 0; `lv[4]` is the energy in the full level list), the shell sizes are counted up to the largest shell of the level set, and the number of sea holes is $\sum 4r_3(n_2)/(1 + e^{(\mu + \varepsilon_{band})/T})$ over these shells (Section 15.26). It is divided by 8 for the holes per particle and compared with the record's column `sea_holes_excluded`.

```python
fig, ax = plt.subplots()
plotted = []  # every value drawn, to measure their range
for marker, n in (("o", 8), ("s", 136)):
    for colour, t in zip(PALETTE, TEMPS):
        values = [float(record[state_id(n, a, t)]["sea_holes_over_N"])
                  for a in (0.0, 0.5, 1.0, 1.5, 2.0)]
        plotted += values
        ax.plot([0, 0.5, 1, 1.5, 2], np.maximum(values, 1e-60), marker + "-",
                color=colour, ms=6, lw=1.2,
                markerfacecolor=colour if n == 8 else "white",
                label=f"$N = {n}$, $T = {t}$")
```

The record's holes per particle for $N = 8$ (filled circles) and $N = 136$ (open squares), the three temperatures and the five slices, joined by lines; values below $10^{-60}$ would be drawn at $10^{-60}$ (the smallest recorded value is about $2 \times 10^{-56}$, so none is clipped).

```python
ax.plot(list(mine), list(mine.values()), "x", color="black", ms=11, mew=2,
        label="this notebook, $N = 8$, $T = 0.05$")
ax.axhline(0.01, color="0.3", ls=":", lw=1.2, label="1 percent")
ax.set_yscale("log")
ax.set_ylim(1e-60, 1e4)  # the smallest recorded value is about 2e-56
ax.set_xlabel("slice $a_{4,0}$")
ax.set_ylabel("sea holes per particle")
ax.set_title("Diagnostic of the filling convention ($\\lambda = 0$)")
ax.legend(fontsize=7, ncol=2, loc="lower right")
smallest = min(v for v in plotted if v > 0.0)  # the smallest nonzero value
powers = int(math.log10(max(plotted) / smallest))  # whole powers of ten spanned
save_figure(fig, "sea_holes",
            "The number of thermal holes that the excluded sea brane band would "
...)
```

This notebook's three values as black crosses (`list(mine)` is the list of the slices, the keys of the dictionary), the 1 per cent line, the axes, and the number of whole powers of ten between the smallest and the largest value, which the caption of Figure 15d.6 prints.

```python
report("smallest and largest sea holes per particle drawn",
       f"{smallest:.2e}, {max(plotted):.2e}")
report("sea holes per particle, N = 8, T = 0.05, a4,0 = 0, 1, 2",
       ", ".join(f"{v:.4g}" for v in mine.values()))
check(worst_sea < 1e-9, "the sea-hole diagnostic reproduced",
      record=f"{THERMO}, column sea_holes_excluded")
```

Out [9]: the values drawn span from $2.10 \times 10^{-56}$ to $30.8$ holes per particle (57 powers of ten); for $N = 8$ at $T = 0.05$ they are $1.464 \times 10^{-5}$, $0.09746$ and $30.8$ at the slices 0, 1, 2; the record is reproduced. At $a_{4,0} = 2$ the excluded sea would carry about 31 holes for each particle: there the CONVENTION is outside its range of validity.

**In [10], the interaction at a temperature.**

```python
fig, ax = plt.subplots()
shifts = []
by_series = {}  # (N, tag) -> the three values of F(lambda) - F(0)
for colour, n in zip(PALETTE, (8, 136, 688)):
    for tag, style in (("lamp1", "-"), ("lamm1", "--")):
        values = [float(record[state_id(n, 0.0, t, tag)]["F"])
                  - float(record[state_id(n, 0.0, t)]["F"]) for t in TEMPS]
        shifts += values
        by_series[(n, tag)] = values
        sign = "+" if tag == "lamp1" else "-"
        ax.plot(TEMPS, values, style, marker="o", color=colour, ms=6, lw=1.5,
                label=f"$N = {n}$, ${sign}\\lambda_1$")
```

From the record alone: the change $F(\lambda) - F(0)$ of the free energy for $\pm\lambda_1$, $N = 8, 136, 688$, at $a_{4,0} = 0$ and the three temperatures, drawn solid for $+\lambda_1$ and dashed for $-\lambda_1$, and kept in `shifts` and, by series, in `by_series`.

```python
ax.set_yscale("symlog", linthresh=1e-4)
ax.axhline(0.0, color="0.5", lw=0.8)
ax.set_xlabel("temperature $T$ (units of $m$)")
ax.set_ylabel("$F(\\lambda) - F(0)$ (units of $m$)")
ax.set_title("Effect of the interaction on the free energy, $a_{4,0} = 0$")
ax.legend(fontsize=8, ncol=2)
up = by_series[(688, "lamp1")]  # N = 688, +lambda_1, at T = 0.01, 0.02, 0.05
save_figure(fig, "interaction_free_energy",
            "The change of the free energy caused by the couplings $+\\lambda_1$ "
...)
```

A symmetric logarithmic axis (linear between $-10^{-4}$ and $10^{-4}$), the zero line, labels, and Figure 15d.7, whose caption prints the values of `up`, $0.0033$ and $0.0045\,m$ at $T = 0.01$ and $0.05$.

```python
report("largest |F(lambda) - F(0)| at a4,0 = 0", f"{max(abs(s) for s in shifts):.4f}")
check(max(abs(s) for s in shifts) < 0.005,
      "the interaction changes F by less than 0.005 at a4,0 = 0",
      record=f"{THERMO}, column F")
raises = all(v > 0.0 for n in (136, 688) for v in by_series[(n, "lamp1")]) and all(
    v < 0.0 for n in (136, 688) for v in by_series[(n, "lamm1")])
lowers8 = all(v < 0.0 for v in by_series[(8, "lamp1")]) and all(
    v > 0.0 for v in by_series[(8, "lamm1")])
check(raises and lowers8,
      "repulsion raises F for N = 136 and 688 and lowers it for N = 8",
      record=f"{THERMO}, column F")
```

Out [10]: the largest change is $0.0046\,m$; repulsion raises $F$ for $N = 136$ and $688$ and lowers it for $N = 8$, whose zero modes have no scalar density without interaction, so that to first order only the exchange term $-\tfrac{1}{32}\lambda n^2$ acts (Section 15.5 gives the exact symmetry at $T = 0$).

**In [11], the last check.**

```python
NAMES = ["root_conditioning", "chemical_potential", "free_energy_entropy",
         "heat_capacity", "occupations", "sea_holes", "interaction_free_energy"]
missing = [name for number, name in enumerate(NAMES, start=1)
           if not output_file(f"{FIGURE_FOLDER}/15d_{number}_{name}.png").is_file()]
check(missing == [], "every figure file of this notebook exists")
all_checks_passed()
```

As in Notebook 15e (Section 15.9, In [15]), with the seven figure names of this notebook in order and the file names `15d_<number>_<name>.png`: the names whose file does not exist are collected, the check requires that list to be empty, and `all_checks_passed()` prints the last line, ALL 15 CHECKS PASSED (notebook 15d).

### 15.31 What we proved, what we computed, what we assumed

**PROVED** (exact statements; derived line by line in this chapter or in Chapter 14, and verified by sympy in `Revision/kohn_sham/reports/ks-theory-python.json` and by WolframScript in `Revision/kohn_sham/reports/ks-theory-wolfram.json`):

| statement | where | record check |
| --- | --- | --- |
| the real block equation, its boundary conditions, self-adjointness, real levels | Section 15.2 | `block_hamiltonian`, `bc_brane_parity_conditions`, `bc_self_adjoint_boundary_term` |
| the Pruefer phase increases strictly and runs over all values: every level has its own label, none is missed | Section 15.3 | derived here; the solver's check `free_particle_branch_labels` |
| the exact levels at $k = 0$ and the zero mode $\sqrt{2M/(1 - e^{-2ML})}\,e^{My}$ | Section 15.3 | `bc_exact_k0_spectra` |
| the Hermite midpoint formula and the Anderson weights | Sections 15.3, 15.5 | derived here |
| the brane-band slope $c = 2/(1 + e^{-3}) = 1.9051482536$ (times $e^{-a_{4,0}}$) | Section 15.4 | `brane_band_slope` |
| the rescaling identity: a later slice is the first slice with redshifted momenta | Section 15.4 | `rescaling_identity` |
| $E_{KS} = \sum gf\varepsilon - 2\,\mathrm{Vol}_7\int e^{6Hy}e_{int}\,dy$ (double counting) | Section 15.5 | `ks_onshell_lagrangian` |
| $E_{KS}(-\lambda) = -E_{KS}(\lambda)$ for the mapped zero-mode state of $N = 8$ | Section 15.5 | derived here |
| the energy-momentum tensor of the states | Section 15.16 | `emt_orbital_components`, `emt_trace_identity` |
| the conservation law $(e^{6Hy}p_8)' = 3H\,e^{6Hy}(p_3 + p_t)$ | Section 15.16 | `emt_y_conservation_selfconsistent` |
| the energy-change law $dE/da_4 = -3\cdot2\,\mathrm{Vol}_7\int e^{6Hy}(p_3 - p_t)\,dy$ | Section 15.16 | `emt_x4_component` |
| the Hellmann-Feynman theorem and the first-order estimate $Q_{nm}$ | Section 15.21 | `adiabatic_hellmann_feynman`, `adiabatic_offdiagonal_identity` |
| the closed form of $C_V$, $C_V = T\,dS/dT$, $-dF/dT = S$, $\Omega = F - \mu N$, the balance form of $\sum gf = N$ | Section 15.26, Exercise 5 | derived here |

**COMPUTED** (numerical, with the record file and the measured agreement):

- The canonical matrix: 75 ground states and 135 thermal states, every one of the 42 checks of `Revision/kohn_sham/reports/ks-rust-solver.json` PASS; a repeat run byte-identical and a refined run within tolerances fixed in advance (`Revision/kohn_sham/reports/ks-rust-determinism.json`, 14 checks PASS); every chemical potential within its rounding bound of a 40-digit root (`Revision/kohn_sham/reports/ks-rust-mermin-roots.json`). Notebook 15a reran the matrix and found every compared number equal to the record (Out [5], Out [6]).
- The method by hand (Notebook 15e): the exact $k = 0$ levels to $7.2 \times 10^{-10}$, the solver's levels to $8 \times 10^{-15}$, the RK4 error ratio 16.00, the band slope at three slices, and the interacting $N = 8$ states to $10^{-14}$.
- Along the history: the $k = 0$ levels do not move, the band levels and all gaps fall (the gap of $N = 8$: $0.4307337$, $0.1703493$, $0.0641594$ at $a_{4,0} = 0, 1, 2$), the energy of the free gas falls ($N = 136$: $80.28$ to $12.45$), and the integrated ratio $\int p_3/\int\rho$ rises toward $1/3$ ($0.2966$ to $0.3264$).
- Delta-SCF equals the gap without interaction ($2.0 \times 10^{-11}$); the orbital relaxation is at most $5.5 \times 10^{-4}\,m$; the self-consistent loops converge in at most 17 iterations.
- The conservation law and the energy-change law hold numerically in every state (solver checks `emt_y_conservation_pointwise`, `emt_y_conservation_integrated` and `emt_energy_change_dE_da4`; Notebook 15b).
- $Q_{max} \le 0.0935$ over the matrix (transition probability below $0.009$), no Fermi-level crossing in the matrix, and the demonstration $N = 696$ where the instantaneous ground state is wrong by $3.66$ to $8.62\,m$ (Notebook 15c).
- The thermodynamics of the free states from the levels alone (Notebook 15d), and the sea-hole diagnostic: more than 1 per cent of $N$ in 15 of the 135 thermal states, at most $30.98\,N$.
- The dependence on the cutoff from $L = 3$ to $6$ of 29 recorded states (`Revision/kohn_sham/tip_convergence/tip-convergence.json`, 7 of 7 checks PASS; Section 15.2): the free results with $k \ne 0$ converge faster than exponentially, the levels at $k = 0$ only like $1/L^2$, and the interacting $N = 8$ energy ($\lambda = \pm\lambda_1$) goes from $\mp9.868 \times 10^{-4}$ at $L = 3$ to $\mp3.0046 \times 10^{-3}$ at large $L$. These are numbers of the record; the notebooks of this chapter compute at $L = 3$ only.
- The five notebooks print 88 PASS lines together (25, 18, 12, 15 and 18).

**ASSUMED**:

- the good sector (no dependence on the extra times) and the Z2 mirror brane at $y = 0$;
- CHOSEN: the regular tip $b(-L) = 0$ at the cutoff $L = 3$. Its effect is COMPUTED in the record (`Revision/kohn_sham/tip_convergence/`, $L = 3$ to $6$, 7 of 7 checks PASS; Section 15.2, the paragraph on the cutoff): the recorded free results, except $N = 688$ at $a_{4,0} = 0$, lie within 1.4 per cent ($E_{KS}$) and 12 per cent (the integral of $p_8$) of their large-$L$ values; the interaction effects do not, because the proper zero-mode density grows toward the tip like $e^{(6H - 2m)|y|}$: the recorded $N = 8$ interaction energy $\mp9.868 \times 10^{-4}$ ($\lambda = \pm\lambda_1$) is about one third of its large-$L$ value $\mp3.0046 \times 10^{-3}$, the interaction shift of $N = 136$ at $a_{4,0} = 2$ is at large $L$ about 21 to 28 times its $L = 3$ value, and the self-consistent iteration fails at some larger $L$ for 13 of the 19 interacting states studied. The couplings (calibrated at $L = 3$; the same rule at larger $L$ drives $\lambda_1$ to zero) and $N = 688$ (bulk edge at $L = 3$) are themselves choices at $L = 3$;
- CONVENTION: particles fill the positive branch and the zero modes, the sea is never occupied, not even thermally; its justification is OPEN, and the sea-hole diagnostic shows where it fails;
- PRESCRIBED BACKGROUND: the history $a_4 = AHx_4$ with $A = 1$; the gas is a test field on it and cannot be its source (it violates the conditions C1, C2, C3 of `Revision/field_equations_a4/reports/ks-source-conditions.json`);
- the functional: Hartree plus the exact local exchange of the uniform gas, no correlation; the instantaneous (adiabatic) states, supported but not proved by $Q_{max} \ll 1$.

**HYPOTHESIS**: none.

**OPEN**: the time-dependent (non-adiabatic) evolution of the gas; a thermal treatment of the sea; the justification of the filling convention; the limit $L \to \infty$ wherever the record does not establish it ($N = 688$ at $a_{4,0} = 0$, the 7 interacting states of Section 15.2 whose limit is not established, whether self-consistent states exist where the iteration fails, and every state not computed at $L \ne 3$); what drives the history, since this gas cannot (Chapter 22 lists these problems). Nothing in this chapter concerns the creation of universes, pairs of universes or the matter-antimatter asymmetry.

### 15.32 Exercises

**Exercise 1 (closed shells).** (a) Show that $r_3(3) = 8$ and $r_3(5) = 24$. (b) Starting with the eight zero modes and filling the brane band shell by shell, compute the closed shells up to $n_2 = 5$. (c) Which of them is nearest to $688/4$, and why is it the record's $N_{mid}$?

*Answer.* (a) $n_1^2 + n_2^2 + n_3^2 = 3$ only with three squares equal to 1, so $(\pm1, \pm1, \pm1)$: $2^3 = 8$ vectors. For 5 the squares must be $4 + 1 + 0$: the number 2 can stand in any of the 3 places, the number 1 in any of the 2 remaining places, and each has two signs, so $3\cdot2\cdot2\cdot2 = 24$ vectors. (b) With $g = 4r_3(n_2)$ and $r_3(1), \dots, r_3(5) = 6, 12, 8, 6, 24$: $8 + 24 = 32$; $32 + 48 = 80$; $80 + 32 = 112$; $112 + 24 = 136$; $136 + 96 = 232$. Rule: add $4r_3(n_2)$ for each new shell. (c) $688/4 = 172$; the distances are $|136 - 172| = 36$ and $|232 - 172| = 60$, so 136 is nearest, the rule of `Revision/kohn_sham/results/parameters.json` (particleNumbers.rule).

**Exercise 2 (why the gap shrinks more slowly than $e^{-a_{4,0}}$).** Let $s(k) = \varepsilon_{band}(k)/k$ and assume that $s$ decreases as $k$ grows. (a) Use the rescaling identity to show that $\Delta_{KS}(a_{4,0})/\Delta_{KS}(0) > e^{-a_{4,0}}$ for $N = 8$ and $a_{4,0} > 0$. (b) Compute $s$ at the momenta $0.25\,e^{-a_{4,0}}$, $a_{4,0} = 0, 1, 2$, from the gaps $0.4307337$, $0.1703493$, $0.0641594$ (Notebook 15a, Out [7]), and compare with $c = 1.9051482536$.

*Answer.* (a) Section 15.4: $\Delta_{KS}(a_{4,0}) = \varepsilon_{band}(k_a)$ with $k_a = 0.25\,e^{-a_{4,0}}$, so

$$
\frac{\Delta_{KS}(a_{4,0})}{\Delta_{KS}(0)} = \frac{k_a\,s(k_a)}{0.25\,s(0.25)} = e^{-a_{4,0}}\,\frac{s(k_a)}{s(0.25)} > e^{-a_{4,0}} .
$$

Rule: write each band level as $k\,s(k)$; $k_a/0.25 = e^{-a_{4,0}}$; and $s(k_a) > s(0.25)$ because $k_a < 0.25$ and $s$ decreases. (b) $s(0.25) = 0.4307337/0.25 = 1.722935$; $s(0.0919699) = 0.1703493/0.0919699 = 1.852229$; $s(0.0338338) = 0.0641594/0.0338338 = 1.896310$. Rule: divide each gap by its momentum ($0.25\,e^{-1} = 0.0919699$, $0.25\,e^{-2} = 0.0338338$). The values grow as $k$ shrinks and approach $c = 1.905148$, the slope at $k = 0$: the assumption holds on these points, and the ratios $1.852229/1.722935 = 1.0750$ and $1.896310/1.722935 = 1.1006$ are exactly the factors by which the measured ratios $0.39549$ and $0.14895$ exceed $e^{-1} = 0.36788$ and $e^{-2} = 0.13534$.

**Exercise 3 (counting levels with the phase).** For the free block $j = +1$ at $k = 0$ use the exact levels of Section 15.3 ($M = 1$, $L = 3$): the even levels $\sqrt{1 + (n\pi/3)^2}$ and the odd levels $1.2922928$, $2.0106286$ (Notebook 15e, Out [6]). (a) How many levels lie strictly between $\varepsilon = 0$ and $\varepsilon = 2$? (b) Between which two multiples of $\pi/2$ does $\Phi(2)$ lie? (c) Why is $\Phi(0) = 0$ exactly?

*Answer.* (a) Even: $n = 1$ gives $\sqrt{1 + 1.0966} = 1.4479719 < 2$, $n = 2$ gives $\sqrt{1 + 4.3865} = 2.3208815 > 2$. Odd: $1.2922928 < 2 < 2.0106286$. So two levels: the odd label 0 (target $\pi/2$) and the even label 1 (target $\pi$). (b) $\Phi$ increases strictly, has passed the targets $\pi/2$ (at $1.2923$) and $\pi$ (at $1.4480$), but not yet $3\pi/2$ (the odd label 1, at $2.0106$); so $\pi < \Phi(2) < 3\pi/2$, that is $1 < \Phi(2)/\pi < 1.5$, as Figure 15e.1 shows. (c) At $\varepsilon = 0$, $k = 0$, $v = 0$ the angle equation is $\theta' = -M\sin2\theta$ with $\theta(-L) = 0$; the constant $\theta = 0$ solves it, and a solution of such an equation is fixed by its start value, so $\theta(0) = 0$. (This is the zero mode, $b = 0$; Notebook 15e checks that the computed value is exactly 0.0, Out [3].)

**Exercise 4 (Anderson weights for two residuals).** (a) For $p = 2$ solve the bordered system of Section 15.5 and show $c_1 = (G_{22} - G_{12})/(G_{11} - 2G_{12} + G_{22})$, $c_2 = 1 - c_1$. (b) Evaluate it for the residuals $r_1 = (2, 1)$ and $r_2 = (1, -1)$, and compare $|c_1r_1 + c_2r_2|^2$ with $|r_1|^2$ and $|r_2|^2$.

*Answer.* (a) With $c_2 = 1 - c_1$, $F = |c_1r_1 + (1 - c_1)r_2|^2 = c_1^2G_{11} + 2c_1(1 - c_1)G_{12} + (1 - c_1)^2G_{22}$. Rule: expand the square with the dot products $G_{ik} = r_i\cdot r_k$. Then $dF/dc_1 = 2c_1G_{11} + 2(1 - 2c_1)G_{12} - 2(1 - c_1)G_{22} = 0$. Rule: differentiate each term. Collecting $c_1$: $c_1(G_{11} - 2G_{12} + G_{22}) = G_{22} - G_{12}$, which is the claim (the same as eliminating $\nu$ from the bordered system). (b) $G_{11} = 4 + 1 = 5$, $G_{22} = 1 + 1 = 2$, $G_{12} = 2 - 1 = 1$, so $c_1 = (2 - 1)/(5 - 2 + 2) = 0.2$ and $c_2 = 0.8$. The combined residual is $0.2\,(2, 1) + 0.8\,(1, -1) = (1.2, -0.6)$ with $|\cdot|^2 = 1.44 + 0.36 = 1.8$, smaller than $|r_2|^2 = 2$ and $|r_1|^2 = 5$; check: $F(c_1) = 5c_1^2 - 2c_1 + 2$ has its minimum $1.8$ at $c_1 = 0.2$.

**Exercise 5 (the grand potential).** For fixed levels and without interaction show that, level by level, $\varepsilon f - TS_1 - \mu f = -T\ln(1 + e^{-x})$, where $S_1 = -[f\ln f + (1 - f)\ln(1 - f)]$ and $x = (\varepsilon - \mu)/T$; conclude $\Omega = E - TS - \mu N$.

*Answer.* Line by line. $1 - f = f(-x) = 1/(1 + e^{-x})$, so $\ln(1 - f) = -\ln(1 + e^{-x})$. Rule: the identity $1 - f(x) = f(-x)$ of Section 15.26. Next, $\ln f - \ln(1 - f) = \ln\frac{f}{1 - f} = -x$. Rule: $\frac{1 - f}{f} = e^x$. Hence $S_1 = -f[\ln f - \ln(1 - f)] - \ln(1 - f) = fx - \ln(1 - f)$. Rule: write $f\ln f + (1 - f)\ln(1 - f) = f[\ln f - \ln(1 - f)] + \ln(1 - f)$. Then $TS_1 = (\varepsilon - \mu)f - T\ln(1 - f)$, because $Tx = \varepsilon - \mu$, and $\varepsilon f - TS_1 - \mu f = T\ln(1 - f) = -T\ln(1 + e^{-x})$. Summing with the degeneracies: $E - TS - \mu N = -T\sum g\ln(1 + e^{-x}) = \Omega$, with $E = \sum gf\varepsilon$ and $N = \sum gf$. With interaction both sides contain the same term $-2\,\mathrm{Vol}_7\int e^{6Hy}e_{int}\,dy$ (Section 15.26); the solver checks the equality in all 135 states (check thermo_grand_potential_two_forms, worst relative difference $1.7 \times 10^{-14}$).

**Exercise 6 (the energy along the history from its slope).** Notebook 15b, Out [7], gives for $N = 136$ without interaction $E(0) = 80.28222$, $E(0.5) = 51.24519$ and the slopes $dE/da_4 = -71.439756$ at $a_{4,0} = 0$ and $-46.470842$ at $a_{4,0} = 0.5$. (a) Estimate $E(0.5)$ from $E(0)$ with Euler's rule (one step with the slope at the start) and with the trapezoid rule (the mean of the two slopes). (b) Explain the signs of the errors.

*Answer.* (a) Euler: $80.28222 + 0.5\cdot(-71.439756) = 80.28222 - 35.71988 = 44.56234$, too low by $6.68$. Trapezoid: $80.28222 + 0.5\cdot\tfrac12(-71.439756 - 46.470842) = 80.28222 - 29.47765 = 50.80457$, too low by $0.44$. Rule: $E(a + h) \approx E(a) + h\,E'(a)$ (Euler) and $E(a + h) \approx E(a) + \tfrac{h}{2}[E'(a) + E'(a + h)]$ (trapezoid), Chapter 2. (b) The slope becomes less negative along the history (the curve of Figure 15b.4 is convex, it bends upward). Euler uses the steepest slope, that of the start, for the whole step and so overestimates the drop. The trapezoid rule averages the two end slopes; but the slope rises fast at first and then more slowly, so between the two ends it lies above the straight line that joins its end values, and the average of the two end slopes is more negative than the true average slope: the drop is again overestimated, by much less. Notebook 15b uses Simpson's rule on 17 slices instead and obtains $E(2) - E(0)$ to $8 \times 10^{-7}$ relative (Out [8]).

**Exercise 7 (adiabaticity).** (a) From Notebook 15c, Out [5], compute $Q$ and the transition probability for $N = 136$ at $a_{4,0} = 0$ (matrix element $0.358861$, energy difference $2.052930$) and at $a_{4,0} = 2$ (matrix element $0.089223$, energy difference $1.524416$). (b) Why is $Q = 0$ exactly for $N = 8$? (c) Use the two-level formula of Section 15.26 to estimate $\mu$ of $N = 8$ at $a_{4,0} = 0$ and $T = 0.02$; the record has $0.2043728$ (`Revision/kohn_sham/results/thermo/thermodynamics.csv`, `N8_lam0_a00_T20`). Why is the agreement worse than at $T = 0.01$?

*Answer.* (a) $Q = 0.358861/2.052930^2 = 0.358861/4.214522 = 0.085149$, probability $Q^2 = 0.00725$; at $a_{4,0} = 2$: $Q = 0.089223/2.323844 = 0.038395$, probability $0.00147$. Rule: $Q = AH|\langle n|\partial_ah|m\rangle|/(\varepsilon_n - \varepsilon_m)^2$ with $AH = 1$ (Section 15.21). Both are far below 1: the gas follows its instantaneous states within the sectors. (b) For $N = 8$ only the zero modes at $k = 0$ are occupied, so transitions could start only in the sectors with $k = 0$, where the free $\partial_a h = -j\kappa k\sigma_3$ vanishes. With interaction the occupied orbitals are still the $k = 0$ orbitals, which do not feel the slice at all (the slice enters only through $\kappa k$), so the self-consistent potentials do not change with $a_4$ either, and $\partial_a h = 0$ on these sectors: every matrix element vanishes. (c) $\mu = 0.4307337/2 - 0.01\ln 3 = 0.2153668 - 0.0109861 = 0.2043807$, against the record's $0.2043728$: a difference of $8 \times 10^{-6}$, against $1.5 \times 10^{-9}$ at $T = 0.01$. Rule: the formula keeps only the first band shell and uses $f(x) \approx e^{-x}$; at the higher temperature the next band shells (at $0.588$ and above) are less suppressed, and the neglected terms grow like $e^{-(\varepsilon - \mu)/T}$, so the estimate is less accurate.
