## 15. Solving the Kohn-Sham equations along the deflating history

Chapter 14 turned the Kohn-Sham problem of the field dirac16complex in the author's primordial universe, in the corrected metric of 2026-10-16, into a problem a computer can solve: pairs of real functions of one variable, the hidden coordinate $y$, in eight independent blocks, with an effective mass and a potential made by the quanta themselves. This chapter solves that problem. It explains, line by line, the numerical method of the Revision Kohn-Sham solver (a Rust program of the repository), runs the solver over its list of states, and reads from the results what happens to the gas of quanta while ordinary 3-space inflates and the three extra times $x_5, x_6, x_7$ deflate exponentially, with the hidden direction shrinking together with them: its levels, gaps, energies, densities, its energy-momentum tensor, how well it can follow the moving background, and its thermodynamics. Five complete notebooks, 15a to 15e, repeat every step and reproduce the numbers of the Revision record.

### 15.1 What this chapter does

**Why solving is a chapter of its own.** The Kohn-Sham equations of Chapter 14 are not solved by writing down a formula. Their orbitals make the potentials and the potentials make the orbitals, so the equations must be solved again and again until the two agree (self-consistency). Each orbital is itself the solution of a boundary-value problem: a pair of differential equations with one condition at each end of the hidden coordinate, which has solutions only for special energies, the levels. The gas has hundreds of occupied orbitals, and the whole computation must be repeated for three particle numbers, five couplings, five instants of the deflating history and three temperatures. A method is needed that finds every level without missing one, that labels each level so that it can be followed from one iteration, coupling or instant to the next, and that is accurate enough that two independent programs agree to many digits. This chapter teaches that method and what it finds.

**What is done, in order.**

- The equations the solver must solve, the parameters of the model and the list of states it computes, called the **canonical matrix** (Section 15.2).
- How one level is found: shooting from the tip to the fold, the Pruefer angle that turns the search for levels into counting, and Newton's method inside a bracket (Section 15.3).
- How the levels of the whole gas are organised: shells of 3-momenta, sectors, label sets, the fold band and its redshift along the history, and the levels at zero momentum, which rise (Section 15.4).
- Self-consistency: the loop, Anderson mixing, the energy of the gas, an exact symmetry of the smallest state, and the first excited state (Section 15.5).
- Notebook 15e, which writes the whole method in plain Python and reproduces numbers of the solver (Sections 15.6 to 15.9).
- The Rust solver and its canonical matrix, and what the matrix shows (Sections 15.10 to 15.15, Notebook 15a).
- The energy-momentum tensor of the gas, its conservation along the hidden direction, the energy change along the history, and why the gas cannot be the source of the history (Sections 15.16 to 15.20, Notebook 15b).
- Adiabaticity: whether the gas follows its instantaneous states while the background moves (Sections 15.21 to 15.25, Notebook 15c).
- Thermodynamics: the gas at a temperature, the chemical potential and why it must be computed in a special way (Sections 15.26 to 15.30, Notebook 15d).
- What we proved, what we computed, what we assumed (Section 15.31), and seven exercises with complete worked answers (Section 15.32).

**The five notebooks.** The run times are the two measured executions of each notebook, the build run and the check run, that section 4.5 of its provenance file `Revision/textbook/notebooks/<name>.PROVENANCE.md` records; they were measured on a computer with two processor cores while other programs ran at the same time, which explains the spread. Notebook 15a runs the solver's quick matrix, whose work the solver divides over all cores; on a computer with many cores it is much faster.

| notebook | what it computes | Rust, PASS lines, figures, run time |
| --- | --- | --- |
| 15e | the solver's method by hand: shooting, Pruefer label, Newton, RK4 order, the fold band, the rescaling identity, self-consistency for $N = 8$ | no Rust; 19 PASS lines; 6 figures; 26 to 27 s |
| 15a | the quick matrix with the Rust solver, compared with the record, and the canonical matrix along the history | Rust; 28 PASS lines; 8 figures; 292 to 298 s |
| 15b | the energy-momentum profiles, the conservation law along $y$, the energy change along the history, the source conditions | Rust; 20 PASS lines; 7 figures; 76 to 79 s |
| 15c | the adiabaticity measure, Hellmann-Feynman, a Fermi-level crossing | no Rust; 12 PASS lines; 6 figures; 15 to 17 s |
| 15d | thermodynamics: chemical potential, free energy, entropy, heat capacity, sea holes | Rust; 16 PASS lines; 7 figures; 66 to 67 s |

The notebooks are placed in the order in which the ideas are needed: 15e first, because it teaches the method that the Rust solver uses in the others.

**The status of every statement.** Every statement of this chapter carries one of the five labels of Chapter 0.

- PROVED: the exact reduction to blocks, the boundary conditions as conditions on the orbitals, the exact free levels at zero momentum, the exact fold band $\varepsilon = \kappa k$ and its slope, the rescaling identity between the instants of the history, the formulas of the densities, potentials, energy and energy-momentum tensor, the conservation law along $y$, the energy-change law along the history, the Hellmann-Feynman relation and the adiabaticity measure. They are verified twice in the Revision record, by sympy in `Revision/kohn_sham/reports/ks-theory-python.json` (61 checks) and by WolframScript in `Revision/kohn_sham/reports/ks-theory-wolfram.json` (51 checks), all PASS; the check names are given with each statement. The mathematical facts of the method (the monotone Pruefer phase, the derivative formula of the phase, the Hermite midpoint, the Anderson weights, the double counting of the interaction energy, the symmetry $E(-\lambda) = -E(\lambda)$ of the zero-mode state, the adiabaticity estimate, the heat-capacity formula and the balance form of the chemical potential) are derived line by line in this chapter.
- COMPUTED: every level, energy, density, pressure, gap, adiabaticity number and thermodynamic function. They come from the Rust solver; its own checks are in `Revision/kohn_sham/reports/ks-rust-solver.json` (45 checks, all PASS), its repeat and refined runs in `Revision/kohn_sham/reports/ks-rust-determinism.json` (14 checks, all PASS), its chemical potentials against 40-digit roots in `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` (5 checks, all PASS), and the notebooks of this chapter reproduce them with the measured differences given with each number. (An independent Python reference solver and the cross-check of the whole matrix belong to Chapter 16.)
- ASSUMED: the good sector (no dependence on the extra times) and the boundary construction at the fold $y = 0$, where the two halves of a cell of the hidden direction meet: both fold conditions are solved and filled. Three further assumptions are of a special kind and carry an extra word. CHOSEN: the regular tip condition at the cutoff $y = -L$ and the value $L = 3$ (the record calls them "chosen"); what the choice of $L$ changes is COMPUTED in the record (`Revision/kohn_sham/tip_convergence/tip-convergence.json`, 7 checks, all PASS): nothing for the free fold-band gases except their values at the fold and the state $N = 2352$ at the first slice, but much for the interaction (Section 15.2, the paragraph on the cutoff). CONVENTION: which levels count as particles (the positive branch and the zero modes) and that the negative branch, the sea, is never populated, not even thermally; its justification is OPEN. PRESCRIBED BACKGROUND: the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = 1$ and $b_4(0) = 1$; it is given, not solved for, the gas does not act back on it, and Section 15.16 shows why it cannot (the record `Revision/field_equations_a4/reports/ks-source-conditions.json`).
- HYPOTHESIS: none. No statement of this chapter goes beyond the equations and their numerical solutions.
- OPEN: the time-dependent (non-adiabatic) problem, a thermal treatment of the sea, the justification of the filling convention, and the limit of a large cutoff $L$ wherever the record does not establish it.

**What this chapter does not touch.** No statement of this chapter concerns pairs of universes, their creation or matter and antimatter. One check of the solver's report, `t3_block_map_solver_selftest`, solves a state with the mass $m$ and a state with the mass $-m$ (with the two fold conditions exchanged by the tip angle) and finds equal energies; the report itself calls it a numerical self-test of the program and NOT a proof of the theorem T3, which belongs to Chapter 19. Nothing computed here says that any universe is created, in pairs or otherwise. Where Section 15.26 speaks of thermal holes in the sea, it means excitations inside one universe, not pairs of universes.

**Notation and units.** The author's coordinates are $x_0, x_1, \dots, x_7$, with the corrected metric of Chapter 3: $x_0$ is the hidden space-like direction, with $z = 6Hx_0$ taking every real value and the scale factor $e^{-a_4}b_4^{1/2}|\cot z|$; $x_1, x_2, x_3$ are ordinary 3-space, which inflates with the scale factor $e^{a_4}$ (no warp); $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which deflate exponentially with the scale factor $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$. The hidden coordinate is $y = \ln|\sin z|/(6H)$ (Chapter 14); on each half of a cell it runs from the **tip** $y = -L$ (where the model cuts the space; the true tip $\sin z = 0$ is at $y \to -\infty$) to the **fold** $y = 0$ ($\cos z = 0$), where the two halves $z < \pi/2$ and $z > \pi/2$ meet. A **slice** is one instant of the history, and $a_{4,0}$ is the value of $a_4$ there; at that slice the **hidden scale** is $f = e^{-a_{4,0}}b_{4,0}^{1/2}$, which on the record's history ($b_4 = e^{(4/3)a_4}$) is $f = e^{-a_{4,0}/3}$, and the **momentum weight** is $\kappa = e^{-a_{4,0}}$, the same at every $y$. In all numbers $H = 1$ and $m = 1$, so energies, momenta and temperatures are in units of $m$ (which equals $H$) and lengths in units of $1/H$; Boltzmann's constant is 1, so a temperature is an energy.

### 15.2 The equations the solver must solve

This section collects, without proofs, the results of Chapter 14 that the solver uses, and adds the parameters of the model. Chapter 14 proves each formula; here we only need to read them.

**One orbital.** At a slice $a_{4,0}$, an orbital of the gas has a 3-momentum $\mathbf k$ (a vector of three numbers), a block type $j = +1$ or $j = -1$, and a pair of real functions $a(y)$, $b(y)$ on the interval $-L \le y \le 0$. Its level $\varepsilon$ and the two functions obey the **block equation in real form** (Section 14.12; `Revision/kohn_sham/ks-theory.json`, blockEquation.realForm; checks block_hamiltonian and block_ode_equivalent):

$$
a' = f\big[M a - \big(\kappa k + j(\varepsilon - v)\big)\,b\big], \qquad b' = f\big[\big(j(\varepsilon - v) - \kappa k\big)\,a - M b\big] ,
$$

where the prime means $d/dy$, $k = |\mathbf k|$ is the length of the momentum, $\kappa = e^{-a_{4,0}}$ is the momentum weight (the same at every $y$), $f = e^{-a_{4,0}/3}$ is the hidden scale of the slice, $M(y)$ is the **effective mass** and $v(y)$ the **potential**. The 16-component field of the orbital is built from $\chi = (a, ib)$ and the block basis of Chapter 14. The slice enters through three things: $\kappa$ (every 3-momentum is redshifted, $k \to ke^{-a_{4,0}}$), $f$ (the hidden direction has shrunk by the factor $f$) and the proper volume of the cell, which divides the densities below.

**The boundary conditions.** At the tip the solver uses the regular tip condition $b(-L) = 0$ (CHOSEN; check bc_tip_family). At the fold two conditions are possible (Section 14.12): the **even fold condition** $b(0) = 0$ and the **odd fold condition** $a(0) = 0$ (check bc_fold_conditions). Both make the current along $y$ vanish, and with them the block Hamiltonian is self-adjoint, so the levels are real (check bc_self_adjoint_boundary_term). The record solves both and fills both together (ASSUMED). The files of the record name the fold condition in a column `parity` with the values `even` and `odd`, a name kept from an earlier construction; in this chapter the word is only that column name.

**The lattice of 3-momenta.** 3-space is a torus of coordinate size $\ell$, so the allowed momenta are $\mathbf k = \Delta k\,(n_1, n_2, n_3)$ with whole numbers $n_1, n_2, n_3$ and $\Delta k = 2\pi/\ell = 0.25$. The numbers $n_1^2 + n_2^2 + n_3^2$ are written $n_2$ (a single symbol, read "n-two", not the second component), and all momenta with the same $n_2$ form a **shell**; they have the same length $k = \Delta k\sqrt{n_2}$, and their number is written $r_3(n_2)$. For example $r_3(0) = 1$ (only the zero vector), $r_3(1) = 6$ (the six vectors $(\pm1, 0, 0)$, $(0, \pm1, 0)$, $(0, 0, \pm1)$), $r_3(2) = 12$, $r_3(3) = 8$, $r_3(4) = 6$, $r_3(7) = 0$ (no three squares add up to 7). The levels depend only on $k$ (check rotation_invariance), and each level of block type $j$ in the shell $n_2$ belongs to $4r_3(n_2)$ orbitals: the four blocks of that type times the $r_3(n_2)$ directions (ks-theory.json, blockEquation.degeneracy). This number is the **degeneracy** $g$ of the level. A **sector** is a triple (shell $n_2$, block type $j$, fold condition).

**Densities.** The **proper** densities (per unit of proper 7-volume) of the number of quanta and of the scalar $S = \bar\Psi\Psi$ are sums over the levels (ks-theory.json, densities):

$$
n(y) = \sum w\,g\,f_o\,P\,(a^2 + b^2), \qquad S(y) = \sum w\,g\,f_o\,P\,j\,2ab, \qquad P = \frac{e^{-3Hy}}{\mathrm{Vol}_7(a_{4,0})} ,
$$

where $f_o$ is the occupation of the level (1 for full, 0 for empty, a number in between at a temperature; the index $o$ keeps it apart from the hidden scale $f$), $w = \tfrac12$, and $\mathrm{Vol}_7(a_{4,0}) = \ell^3v_t\,e^{-a_{4,0}}b_{4,0}^2$ is the proper 7-volume of the coordinate cell per unit of $e^{3Hy}$, with the extra-time coordinate volume $v_t = 1$. On the history, line by line:

$$
\mathrm{Vol}_7(a_{4,0}) = \ell^3v_t\,e^{-a_{4,0}}\big(e^{(4/3)a_{4,0}}\big)^2 = \ell^3v_t\,e^{(-1 + 8/3)a_{4,0}} = \ell^3v_t\,e^{(5/3)a_{4,0}} .
$$

Rule: insert $b_{4,0} = e^{(4/3)a_{4,0}}$ and add the exponents. With $\ell = 2\pi/\Delta k = 8\pi$:

$$
\mathrm{Vol}_7(0) = (8\pi)^3\cdot 1 = 512\,\pi^3 = 15875.2137 .
$$

Rule: $\ell^3 = 8^3\pi^3 = 512\pi^3$, and $\pi^3 = 31.00628$. The record has the same number (`Revision/kohn_sham/results/parameters.json`, physics.Vol7AtA4Zero); at the last slice the cell is $e^{10/3} = 28.03$ times larger, $\mathrm{Vol}_7(2) = 445008.0$. The factor $e^{-3Hy}$ turns a density per unit $y$ into a density per unit proper volume, because the proper volume element is $\sqrt{|g|}\,dx_0 = e^{-a_4}b_4^2|\sin z|^{1/2}\,dy = e^{-a_4}b_4^2e^{3Hy}\,dy$ (Chapter 14: $dy = \cot z\,dx_0$ removes the factor $|\cot z|$ of $\sqrt{|g|}$, and $|\sin z| = e^{6Hy}$). The weight $w = \tfrac12$ belongs to the **whole cell**: every orbital is normalised on one half, $\int_{-L}^{0}(a^2 + b^2)\,dy = 1$, the same $\chi(y)$ describes both halves (Section 14.12), and the particle number $N = \sum g f_o$ counts the quanta of both halves together; one half holds $N/2$. The Rust solver fixes the particle number by exactly this count, $\sum g f_o = N$ (`Revision/kohn_sham/solver/src/scf.rs` and `mermin.rs`; the check ground_N_conservation compares both $\sum g f_o$ and $2\,\mathrm{Vol}_7\int e^{3Hy}n\,dy$ with $N$). The theory file states the same count in its densities (ks-theory.json, densities.total) but writes "mu fixed by sum w g f = N" in its line on the occupations at a temperature (thermodynamics.occupation); that line is inconsistent with the rest of the file, the solver does not follow it, and `Revision/kohn_sham/results/parameters.json` records the discrepancy (conventions.particleNumber). Section 15.26 comes back to it.

**Potentials and energy.** The contact interaction $U = \tfrac{\lambda}{2}S^2$ with the exact local exchange of Chapters 13 and 14 gives (ks-theory.json, exchange.kohnShamPotentials; check ks_potentials)

$$
e_{int} = \lambda\Big(\tfrac{15}{32}S^2 - \tfrac{1}{32}n^2\Big), \qquad M = m + \frac{\partial e_{int}}{\partial S} = m + \tfrac{15}{16}\lambda S, \qquad v = \frac{\partial e_{int}}{\partial n} = -\tfrac{1}{16}\lambda n ,
$$

and the **Kohn-Sham energy** of the whole cell is

$$
E_{KS} = \sum g\,f_o\,\varepsilon - 2\,\mathrm{Vol}_7\int_{-L}^{0}e^{3Hy}e_{int}\,dy .
$$

Section 15.5 derives why the interaction energy is subtracted here. The term $\tfrac{15}{32}\lambda S^2$ is the Hartree energy $\tfrac{\lambda}{2}S^2$ plus the scalar part $-\tfrac{1}{32}\lambda S^2$ of the exchange energy, and $-\tfrac{1}{32}\lambda n^2$ is the rest of the exchange energy (Chapter 13); the potential $v$ therefore comes from the exchange alone, and the notebooks call it the exchange potential. The coupling of the record is $\hat\lambda = \lambda\,b_4(0)^{-2}$, the same number for $b_4(0) = 1$; it is held fixed while the cell grows, so the strength of the mean field, which goes with $\hat\lambda/\mathrm{Vol}_7(a_{4,0})$, falls like $e^{-(5/3)a_{4,0}}$ along the history (ks-theory.json, densities.couplingVolumeScaling; check ks_coupling_volume_scaling).

**Which levels are particles (CONVENTION).** The equations have levels of both signs. The convention of the record (ks-theory.json, thermodynamics.fillingConvention) is: particles occupy the **positive branch**, the levels whose value without interaction ($\lambda = 0$) at the same slice is positive, together with the **zero modes** at $k = 0$ (the levels $\varepsilon = 0$ of the free problem); the levels of the negative branch form the normal-ordered **sea** and are never occupied, not even at a temperature. The justification of this convention is OPEN; Section 15.26 measures where it stops being reasonable.

**The particle numbers.** The record uses three particle numbers (`Revision/kohn_sham/results/parameters.json`, particleNumbers). $N = 8$ fills exactly the eight zero modes at $k = 0$ (four blocks of each type). The next levels above the zero modes are the **fold band**, the even level of label 0 of block type $j = +1$ in each shell $n_2 \ge 1$, exactly $\varepsilon = \kappa k$ (Section 14.19 and Section 15.4); at $a_{4,0} = 0$ it increases with $n_2$, so filling it shell by shell gives **closed shells** (every level either full or empty). Line by line, with $g = 4r_3(n_2)$ and $r_3(1), \dots, r_3(10) = 6, 12, 8, 6, 24, 24, 0, 12, 30, 24$:

$$
8 + 4\,(6 + 12 + 8 + 6 + 24 + 24 + 0 + 12 + 30 + 24) = 8 + 4\cdot146 = 592 .
$$

Rule: the eight zero modes plus four times the numbers of vectors in the shells 1 to 10. Continuing to $n_2 = 26$ with $r_3(11), \dots, r_3(26) = 24, 8, 24, 48, 0, 6, 48, 36, 24, 24, 48, 24, 0, 24, 30, 72$, whose sum is $440$:

$$
8 + 4\,(146 + 440) = 8 + 4\cdot586 = 2352 .
$$

Rule: the sum of the first ten shells plus the sixteen new ones. $N = 2352$ is the largest closed shell whose highest level, the fold band at $k = 0.25\sqrt{26} = 1.2747549$, lies below the **bulk edge** $1.2922928$, the lowest level that is not on the fold band (the odd level of label 0 at $k = 0$; parameters.json, particleNumbers.bulkEdge; a value at the cutoff $L = 3$, see the end of this section); the next fold-band shell, $0.25\sqrt{27} = 1.2990$, lies above it. $N = 592$ is the closed shell nearest to $2352/4 = 588$ (Exercise 1 checks this). The record calls 2352 $N_{large}$ and 592 $N_{mid}$ (parameters.json, particleNumbers.N_large and particleNumbers.N_mid, with the rule in particleNumbers.rule). Chapter 14 (Section 14.21) lists the closed shells in between.

**The couplings.** The coupling $\hat\lambda$ is a constant of the theory, the same at every slice. For each $N$ the record chooses two values so that the interaction is a moderate perturbation along the whole history (parameters.json, couplingCalibration). In the free ground states of that $N$ at all five slices it takes the largest value over $y$ of $\max\big(\tfrac{15}{16}|S|, \tfrac{1}{16}n\big)$ per unit $\hat\lambda$, the size of the first-order mean-field potentials (called the **strength**), with the densities per $\mathrm{Vol}_7(a_{4,0})$, and sets $\lambda_1 = 0.1/\text{strength}$ and $\lambda_2 = 0.3/\text{strength}$, rounded to four significant digits; then the first-order potentials stay below $0.1\,m$ and $0.3\,m$. For $N = 8$ the strength is $0.0006341788$, so $\lambda_1 = 0.1/0.0006341788 = 157.68$, rounded $157.7$, and $\lambda_2 = 473.1$. For $N = 592$ and $2352$ the strengths are $0.04692923$ and $0.1864486$, so $\lambda_1 = 2.131$ and $0.5363$, $\lambda_2 = 6.393$ and $1.609$. The strength is largest at the first slice and falls along the history (for $N = 592$ from $0.04693$ to $0.01665$; parameters.json, strengthPerLambdaAtSlices): the cell grows like $e^{(5/3)a_{4,0}}$ and the proper densities fall with it, while the orbitals spread toward the tip, where the factor $P = e^{-3Hy}/\mathrm{Vol}_7$ is larger; the growth of the cell wins. The calibration is made at the cutoff $L = 3$, and the strength grows with $L$ (the end of this section). The sign of $\hat\lambda$ decides the kind of interaction: $\hat\lambda > 0$ is repulsive, $\hat\lambda < 0$ attractive. The run names use the tags `lam0`, `lamp1`, `lamm1`, `lamp2`, `lamm2` for $\hat\lambda = 0, +\lambda_1, -\lambda_1, +\lambda_2, -\lambda_2$.

**The canonical matrix.** The solver computes a fixed list of states. **Ground states** ($T = 0$): three particle numbers $N = 8, 592, 2352$, five couplings and five slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$, that is $3 \cdot 5 \cdot 5 = 75$ states. **Thermal states**: the same three $N$, the three couplings $0, \pm\lambda_1$, the five slices and three temperatures $T = 0.01, 0.02, 0.05$, that is $3\cdot3\cdot5\cdot3 = 135$ states. A state is named like `N592_lamp2_a20` ($N = 592$, $+\lambda_2$, $a_{4,0} = 2.0$; the last two digits are ten times the slice), and a thermal state carries in addition `_T10`, `_T20` or `_T50` (a thousand times the temperature).

**The numerical parameters** (parameters.json, numerics): $G = 900$ steps of the Runge-Kutta method on $[-L, 0]$, a root tolerance of $10^{-13}\,m$ for each level, a self-consistency tolerance of $10^{-11}\,m$ with at most 400 iterations, Anderson mixing with depth 6 and $\beta = 0.4$, the step $\delta = 0.002$ in $a_4$ for derivatives along the history, and levels closer than $10^{-9}\,m$ count as equal (one degenerate group).

**What the cutoff $L = 3$ changes (the choice is CHOSEN, its effect COMPUTED).** The regular tip and the value $L = 3$ are choices of the model, and the record measures what they change in the folder `Revision/kohn_sham/tip_convergence/`, summarised in sections 5 and 15 of the document `Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md` and in Section 14.20. It solves 29 recorded states, the 27 ground states with $N = 8, 592, 2352$, $\hat\lambda = 0, \pm\lambda_1$, $a_{4,0} = 0, 1, 2$ and two thermal states of $N = 592$, at $L = 3, 3.5, \dots, 6$ with the record's step $h = 1/300$, and every run again with the step $h/2$. A copy of the solver that reads $L$ from the environment reproduces the committed quick matrix byte for byte at $L = 3$, and the independent reference solver agrees at $L = 3$ and $L = 4$ (report `Revision/kohn_sham/tip_convergence/tip-convergence.json`, 7 of 7 checks PASS, rerun for the corrected metric on 2026-10-17).

**How the study judges the limit $L \to \infty$.** The rules were fixed before the comparison (section 3 of the README of that folder). For each computed number $x$, for example $E_{KS}$, the study forms the **successive differences** $d = x(L + 0.5) - x(L)$ over the unbroken run $L = 3, 3.5, 4, \dots$ of values at which the self-consistent iteration converged (the run ends just before the first $L$ at which the iteration fails, and values at larger $L$ after a failure are not used), and the ratio $r$ of each difference to the one before it. If every difference from some $L$ on is no larger than the numerical noise of its two values, the number has converged within the noise, and its last value is its limit. The noise of a value $x_h$ computed with the step $h$ is $\tfrac{16}{15}|x_{h/2} - x_h|$, measured with the run at the step $h/2$, plus $10^{-11}$ times the larger of 1 and $|x|$: the error of the Runge-Kutta rule, which is of fourth order, falls by the factor $2^4 = 16$ when the step is halved, so $x_h - x_{h/2}$ is $\tfrac{15}{16}$ of the error of $x_h$. If the last two ratios both lie between 0 and 0.5, the study takes the differences to go on shrinking like a geometric series, each one the fraction $r$ (the last ratio) of the one before; this is the **geometric-tail rule**, and the limit, which the record calls the extrapolated value and this chapter also the large-$L$ value, adds the differences still missing:

$$
x_\infty = x(L_{max}) + d_{last}\,(r + r^2 + r^3 + \dots) = x(L_{max}) + d_{last}\,\frac{r}{1 - r} .
$$

Rule: $L_{max}$ is the last $L$ of this run and $d_{last}$ the last difference, so the next differences would be $d_{last}r, d_{last}r^2, \dots$; the sum $s = r + r^2 + r^3 + \dots$ obeys $s = r + r\,s$ (take the factor $r$ out of every term after the first), so $s = r/(1 - r)$ for $0 < r < 1$. In every other case, and when this run holds fewer than three values of $L$ (as for $N = 2352$, $+\lambda_1$, $a_{4,0} = 0$, which converges at $L = 3$ and fails from $L = 3.5$ on), the study takes no limit: the limit is not established. The condition on the last two ratios is stricter than the one of the study's first analysis, which, in a run for an earlier form of the metric, accepted a last ratio below 0.9 and so extrapolated a tail that fell like a power of $L$; the change only removed extrapolations (section 9 of the README). An algebraic tail $d \sim L^{-p}$ has ratios $(L/(L + 0.5))^p$, larger than 0.5 for $p < 8$ at $L \ge 5$, and is rejected. This rule follows the dependence on $L$; it is not the Richardson extrapolation of Chapter 2, which combines two values so that their leading error term cancels. What the study finds:

- The free states are exact fold-band gases (Section 15.4): every occupied orbital of the free states $N = 8$ and $592$ (all slices) and $N = 2352$ at $a_{4,0} = 1, 2$ is the fold-band orbital $(e^{fmy}, 0)$ with $\varepsilon = \kappa|\mathbf k|$, and its level does not depend on $L$. So their $E_{KS}$, highest occupied and lowest empty levels and gap are the same at every $L$ (largest relative change $1.4 \times 10^{-17}$). Only the values at the fold depend on $L$, through the normalisation of the band orbital: $\rho(0; L) = \rho(0; \infty)/(1 - e^{-2fmL})$ exactly, so the recorded $L = 3$ fold values are high by 0.25, 1.38 and 4.8 per cent at $a_{4,0} = 0, 1, 2$.
- The levels at $k = 0$ other than the zero mode approach $\pm m$ only slowly, like the levels of a box of proper length $fL$: $\varepsilon - m \approx (n\pi)^2/(2m(fL)^2)$ (Section 15.3 derives this for the even levels from their exact formula; the record verifies its 84 levels at $k = 0$ against the exact formulas at every $L$ of the study, to $1.42 \times 10^{-10}\,m$). So the bulk edge $1.2922928$ that defines $N = 2352$ is a value at $L = 3$: it is $1.0977$ at $L = 6$ and tends to $m$ as $L \to \infty$. From $L = 3.5$ on, the ground state of $N = 2352$ at $a_{4,0} = 0$ occupies levels of the bulk at $k = 0$, its gap $0.01754$ closes, and its energy does not converge up to $L = 6$ ($2288.388$ at $L = 3$, $2245.486$ at $L = 6$).
- The interacting results depend on $L$, the more the later the slice. The proper density of the zero modes grows toward the tip like $e^{(3H - 2fm)|y|}$ (exact, and verified by the record; Figure 15e.6 shows the potential it makes). For $N = 8$ the record finds $E_{KS} = \mp3.7787 \times 10^{-2}$ at $L = 3$ ($\hat\lambda = \pm\lambda_1$, $a_{4,0} = 0$) against $\mp3.8688 \times 10^{-2}$ at large $L$, $\mp1.4571 \times 10^{-2}$ against $\mp2.1622 \times 10^{-2}$ at $a_{4,0} = 1$, and $\mp6.980 \times 10^{-3}$ against $\mp3.239 \times 10^{-2}$ at $a_{4,0} = 2$: the recorded values are 0.977, 0.674 and 0.215 of the large-$L$ values. For $N = 592$ and $2352$ at $a_{4,0} = 2$ the interaction shift $E_{KS}(\pm\lambda_1) - E_{KS}(0)$ is 4.6 to 4.7 times larger at large $L$ than at $L = 3$.
- The self-consistent iteration converges at every $L$ for 17 of the 19 interacting states studied (geometric tails); it fails only for $N = 2352$ at $a_{4,0} = 0$, from $L = 3.5$ for $+\lambda_1$ and from $L = 4.5$ for $-\lambda_1$, where levels of the bulk at $k = 0$ are occupied. This is a failure of the iteration, not a proof that no self-consistent state exists.
- The calibration of the couplings is a statement at $L = 3$: the strength is the largest first-order mean-field potential per unit $\hat\lambda$, and it grows with $L$. The same rule applied at larger $L$ drives $\lambda_1$ toward zero: $157.7$, $2.131$ and $0.5363$ at $L = 3$ ($N = 8$, $592$, $2352$), $1.249$, $0.01687$ and $1.03 \times 10^{-5}$ at $L = 6$.

Not computed at $L \ne 3$: the couplings $\pm\lambda_2$, the slices $0.5$ and $1.5$, $T = 0.01$ and the other thermal states, the excited states and the adiabaticity measure; and nothing beyond $L = 6$. Every number printed by the notebooks of this chapter is a value at $L = 3$, and so is every number of the chapter except where this paragraph is cited.

### 15.3 Finding one level: shooting with the Pruefer angle

**The idea of shooting.** For a trial energy $\varepsilon$, start at the tip with values that satisfy the tip condition, $(a, b) = (1, 0)$, integrate the two first-order equations of Section 15.2 from $y = -L$ to $y = 0$ with a step rule (the Runge-Kutta rule RK4 of Chapter 2), and look at the end values. If the fold condition wanted holds there ($b(0) = 0$ or $a(0) = 0$), $\varepsilon$ is a level. If not, change $\varepsilon$ and shoot again. The start value 1 for $a$ is no restriction: the equations are linear in $(a, b)$, so any other start $(c, 0)$ gives $c$ times the same solution, and the solution is normalised at the end. Chapter 2 introduced this method for a quantum well and Chapter 14 (Section 14.14) applied it to the free blocks. Two difficulties remain: how to find every level without missing one, and how to tell which level is which. The Pruefer angle solves both.

**The Pruefer angle.** Write the point $(a, b)$ in polar form, $a = r\cos\theta$, $b = r\sin\theta$, with the length $r = \sqrt{a^2 + b^2} > 0$ and the angle $\theta$, followed continuously along $y$ (it may grow beyond $2\pi$). We derive the equation for $\theta$, line by line.

$$
a b' - b a' = r\cos\theta\,(r'\sin\theta + r\cos\theta\,\theta') - r\sin\theta\,(r'\cos\theta - r\sin\theta\,\theta') = r^2\theta' .
$$

Rule: differentiate $a = r\cos\theta$ and $b = r\sin\theta$ with the product and chain rules; the terms with $r'$ cancel, and $\cos^2\theta + \sin^2\theta = 1$.

$$
a b' = f\big[\big(j(\varepsilon - v) - \kappa k\big)a^2 - M a b\big], \qquad b a' = f\big[M a b - \big(\kappa k + j(\varepsilon - v)\big)b^2\big] .
$$

Rule: multiply the second block equation by $a$ and the first by $b$.

$$
a b' - b a' = f\big[j(\varepsilon - v)(a^2 + b^2) - \kappa k\,(a^2 - b^2) - 2Mab\big] .
$$

Rule: subtract; the terms with $j(\varepsilon - v)$ collect to $j(\varepsilon - v)(a^2 + b^2)$, the terms with $\kappa k$ to $-\kappa k a^2 + \kappa k b^2$, and the two terms $-Mab$ add; the common factor $f$ stays in front.

$$
\theta' = f\big[j(\varepsilon - v) - \kappa k\cos2\theta - M\sin2\theta\big] .
$$

Rule: divide by $r^2$ and use $a^2 + b^2 = r^2$, $a^2 - b^2 = r^2(\cos^2\theta - \sin^2\theta) = r^2\cos2\theta$ and $2ab = 2r^2\cos\theta\sin\theta = r^2\sin2\theta$ (the double-angle formulas). The angle obeys an equation of its own, without $r$. At the tip, $(a, b) = (1, 0)$ gives $\theta(-L) = 0$ for every $\varepsilon$. (Section 14.14 derives the same equation; Notebook 14b checks it with sympy.)

**The phase function.** Define $\Phi(\varepsilon) = j\,\theta(0)$, $j$ times the angle at the fold. The fold conditions become conditions on $\Phi$: $b(0) = 0$ means $\sin\theta(0) = 0$, that is $\theta(0)$ is a whole multiple of $\pi$, so $\Phi = l\pi$ with a whole number $l$ (even fold condition); $a(0) = 0$ means $\cos\theta(0) = 0$, so $\Phi = \tfrac{\pi}{2} + l\pi$ (odd fold condition). (Multiplying by $j = \pm1$ maps the set of these values onto itself.) So every level is a solution of $\Phi(\varepsilon) = t_l$ for one of the **targets** $t_l = l\pi$ (even) or $t_l = \tfrac{\pi}{2} + l\pi$ (odd).

**$\Phi$ increases strictly.** We compute $u = \partial\theta/\partial\varepsilon$, line by line.

$$
u' = f\big[j + \big(2\kappa k\sin2\theta - 2M\cos2\theta\big)\,u\big], \qquad u(-L) = 0 .
$$

Rule: differentiate the angle equation with respect to $\varepsilon$ (chain rule: $\partial(\cos2\theta)/\partial\varepsilon = -2\sin2\theta\,u$ and $\partial(\sin2\theta)/\partial\varepsilon = 2\cos2\theta\,u$); $f$ does not depend on $\varepsilon$; $u(-L) = 0$ because $\theta(-L) = 0$ for every $\varepsilon$.

$$
(\ln r)' = \frac{a a' + b b'}{r^2} = f\big[M\cos2\theta - \kappa k\sin2\theta\big] .
$$

Rule: $(\ln r)' = r'/r = (a a' + b b')/r^2$ (differentiate $r^2 = a^2 + b^2$); insert the block equations, where the terms with $j(\varepsilon - v)$ cancel: $aa' + bb' = f[M(a^2 - b^2) - 2\kappa k\,ab]$; then the double-angle formulas.

$$
u' = fj - 2(\ln r)'\,u .
$$

Rule: the bracket of the first line, times $f$, is $fj$ plus $-2$ times the second line times $u$.

$$
(r^2u)' = 2rr'u + r^2u' = r^2\big(2(\ln r)'u + fj - 2(\ln r)'u\big) = fj\,r^2 .
$$

Rule: the product rule, $r' = r\,(\ln r)'$, and the previous line.

$$
r(0)^2\,u(0) = fj\int_{-L}^{0}r^2\,dy, \qquad \frac{d\Phi}{d\varepsilon} = j\,u(0) = \frac{f\int_{-L}^{0}r^2\,dy}{r(0)^2} > 0 .
$$

Rule: integrate from the tip to the fold, with $u(-L) = 0$; then multiply by $j$ and use $j^2 = 1$. The result is positive because $f > 0$ and $r^2 = a^2 + b^2 > 0$. So **$\Phi$ increases strictly with $\varepsilon$**, for both block types, any potentials and any slice. This formula is also the derivative that Newton's method needs, and the solver computes it at no extra cost while it integrates (its documentation in `Revision/kohn_sham/solver/README.md`, Method).

**$\Phi$ runs from $-\infty$ to $+\infty$.** On the interval the functions $|v|$, $\kappa k$ and $|M|$ are bounded, say by a number $C_0$ each. Then $j\theta' = f[(\varepsilon - v) - j\kappa k\cos2\theta - jM\sin2\theta]$ lies between $f(\varepsilon - 3C_0)$ and $f(\varepsilon + 3C_0)$, and integrating over the length $L$ gives $f(\varepsilon - 3C_0)L \le \Phi(\varepsilon) \le f(\varepsilon + 3C_0)L$. So $\Phi(\varepsilon) \approx \varepsilon fL$ for large $|\varepsilon|$, and it takes every real value. The product $fL$, the proper length of the cut-off half, sets the scale.

**The oscillation theorem.** A continuous function that increases strictly from $-\infty$ to $+\infty$ takes every value exactly once. Hence each target $t_l$ is reached at exactly one energy: **every level has its own whole number $l$, its Pruefer label, and no level can be missed.** In a sector the levels are ordered by their labels. When the potentials change continuously (from one iteration of the self-consistent loop to the next, when the coupling is switched on, or from one slice to the next), a level moves continuously and keeps its label, because the target does not change. The label is therefore a name that follows a level everywhere. The particle levels of a sector are exactly the labels $l \ge l_{min}$, where $l_{min}$ is the first label whose level without interaction is positive; in the even sectors at $k = 0$, $l_{min} = 0$ is the zero mode, counted as a particle level by the convention of Section 15.2 (the solver checks this split in every sector up to $n_2 = 30$ and finds the level closest to zero, apart from the zero modes, at $0.2500\,m$, the fold band of the first shell; check free_particle_branch_labels of `Revision/kohn_sham/reports/ks-rust-solver.json`).

**The test case: exact levels at $k = 0$.** With $k = 0$, $v = 0$ and a constant mass $M > 0$ the levels are known exactly (Section 14.13; ks-theory.json, boundaryConditions.exactK0Spectra; check bc_exact_k0_spectra). Line by line:

$$
\frac{a''}{f} = Ma' - j\varepsilon b' = Ma' - j\varepsilon f(j\varepsilon a - Mb) = Ma' - f\varepsilon^2 a + j\varepsilon fM b .
$$

Rule: differentiate the first block equation (with $k = 0$, $v = 0$), divide by $f$, and insert the second; $j^2 = 1$.

$$
\frac{a''}{f} = Ma' - f\varepsilon^2 a + M(fMa - a') = f(M^2 - \varepsilon^2)\,a, \qquad a'' = f^2(M^2 - \varepsilon^2)\,a .
$$

Rule: the first block equation says $j\varepsilon f b = fMa - a'$; then multiply by $f$. The same two steps for $b$, line by line:

$$
\frac{b''}{f} = j\varepsilon a' - Mb' = j\varepsilon f(Ma - j\varepsilon b) - Mb' = j\varepsilon fM a - f\varepsilon^2 b - Mb' .
$$

Rule: differentiate the second block equation (with $k = 0$, $v = 0$), divide by $f$, and insert the first; $j^2 = 1$.

$$
\frac{b''}{f} = M(b' + fMb) - f\varepsilon^2 b - Mb' = f(M^2 - \varepsilon^2)\,b, \qquad b'' = f^2(M^2 - \varepsilon^2)\,b .
$$

Rule: the second block equation says $j\varepsilon f a = b' + fMb$; then multiply by $f$. For $\varepsilon \ne 0$ this relation gives $a$ from $b$, so an orbital that is not zero everywhere has a $b$ that is not zero everywhere; the cases $\varepsilon \ne 0$ are sorted by the sign of $M^2 - \varepsilon^2$. For $\varepsilon^2 > M^2$ put $p = \sqrt{\varepsilon^2 - M^2}$; then $b'' = -(fp)^2b$, and the tip condition $b(-L) = 0$ leaves $b = B\sin\big(fp(y + L)\big)$ with $B \ne 0$. Even fold condition, $b(0) = 0$: $\sin(pfL) = 0$, so $p = n\pi/(fL)$ and

$$
\varepsilon = \pm\sqrt{M^2 + \big(n\pi/(fL)\big)^2}, \qquad n = 1, 2, \dots
$$

Odd fold condition, $a(0) = 0$: the relation $j\varepsilon f a = b' + fMb$ gives $a(0) = 0$ exactly when $b'(0) + fMb(0) = 0$, that is $Bfp\cos(pfL) + fMB\sin(pfL) = 0$, or $\tan(pfL) = -p/M$.

Inside the gap, $0 < \varepsilon^2 < M^2$, put $q = \sqrt{M^2 - \varepsilon^2} > 0$; then $b'' = (fq)^2b$. The functions $\cosh x = (e^x + e^{-x})/2$ and $\sinh x = (e^x - e^{-x})/2$ are each the derivative of the other, so $\cosh\big(fq(y + L)\big)$ and $\sinh\big(fq(y + L)\big)$ solve $b'' = (fq)^2b$, every solution is a combination of the two, and the tip condition $b(-L) = 0$ (where $\cosh 0 = 1$, $\sinh 0 = 0$) leaves $b = B\sinh\big(fq(y + L)\big)$ with $B \ne 0$. The even condition needs $b(0) = B\sinh(fqL) = 0$, impossible because $\sinh x > 0$ for $x > 0$. The odd condition needs $b'(0) + fMb(0) = Bf\big(q\cosh(fqL) + M\sinh(fqL)\big) = 0$, impossible because both terms in the bracket are positive. At the edge, $\varepsilon^2 = M^2$, the equation is $b'' = 0$ and the tip condition leaves $b = B(y + L)$; the even condition needs $BL = 0$ and the odd one $b'(0) + fMb(0) = B(1 + fML) = 0$, both impossible for $B \ne 0$. So **no level lies in $0 < |\varepsilon| \le M$**: the only level inside the gap is the zero mode. Finally $\varepsilon = 0$: the equations become $a' = fMa$, $b' = -fMb$, so $b = 0$ (from $b(-L) = 0$) and $a = Ce^{fMy}$: the **zero mode**, which satisfies the even fold condition. Normalising, $\int_{-L}^{0}C^2e^{2fMy}dy = C^2(1 - e^{-2fML})/(2fM) = 1$ gives $C = \sqrt{2fM/(1 - e^{-2fML})}$. For $M = 1$, $L = 3$ at the first slice ($f = 1$): the first even levels are $\pm\sqrt{1 + (\pi/3)^2} = \pm1.4479719$, and the first odd level is $\pm1.2922928$, the bulk edge of Section 15.2. At the slice $a_{4,0} = 1.5$ ($f = e^{-1/2}$, $fL = 1.819592$) the same two levels are $1.9952267$ and $1.5905829$: the hidden direction is shorter and the levels are higher. Notebook 15e reproduces all of them by shooting (Out [6]).

**How these levels depend on the cutoff and on the slice.** Every level other than the zero mode depends on $fL$. For the even levels, line by line:

$$
\sqrt{M^2 + \big(n\pi/(fL)\big)^2} - M = \frac{\big(n\pi/(fL)\big)^2}{\sqrt{M^2 + \big(n\pi/(fL)\big)^2} + M} \approx \frac{(n\pi)^2}{2M(fL)^2} \quad (fL \text{ large}) .
$$

Rule: multiply and divide by the sum $\sqrt{M^2 + (n\pi/(fL))^2} + M$ and use $(A - B)(A + B) = A^2 - B^2$; for large $fL$ the denominator tends to $2M$. So the levels at $k = 0$ approach $\pm M$ only like $1/L^2$, slowly; the record finds the same approach for the odd levels (the bulk edge is $1.2923$ at $L = 3$ and $1.0977$ at $L = 6$; Section 15.2, the paragraph on the cutoff). Along the history $f$ shrinks, so these levels rise: the lowest odd level at $k = 0$ goes from $1.2923$ at the first slice to $1.7356$ at $a_{4,0} = 2$ (Section 14.20). The zero mode stays at $\varepsilon = 0$ for every $L$ and every slice; only its normalisation $C$ depends on them.

**Newton's method inside a bracket.** To solve $\Phi(\varepsilon) = t_l$ the solver uses Newton's method, $\varepsilon \to \varepsilon - (\Phi(\varepsilon) - t_l)/\Phi'(\varepsilon)$, with the derivative from the formula above. Newton's method converges very fast near the root but can jump far away from a poor guess, so it is **safeguarded**: from a guess the solver first walks with doubling steps (up if $\Phi < t_l$, down otherwise) until $\Phi - t_l$ changes sign; the last two points form a **bracket** $[lo, hi]$ that contains the root, because $\Phi$ is continuous. Then it takes Newton steps, and replaces a Newton step by **bisection** (the midpoint of the bracket) whenever the Newton step would leave the bracket or the previous step did not halve $|\Phi - t_l|$; after each step the bracket shrinks to the side where the sign changes. It stops when the bracket is shorter than the tolerance $10^{-13}\,m$ or when a Newton step moved the energy by less than that (Newton's method approaches a root from one side, so the bracket itself need not shrink). The levels are therefore found to about $10^{-13}\,m$ for a given grid.

**The grid, RK4 and the order 4.** The solver makes $G = 900$ steps of length $h = L/G = 1/300$. One RK4 step needs the coefficients $M$, $v$ (and $\kappa$, $f$, which are constants of the slice) at the start, the middle and the end of the step, so the potentials are stored on the **fine grid** of the $2G + 1 = 1801$ step ends and midpoints, $y_i = -L + i\,h/2$. The error of RK4 falls like $h^4$ (Chapter 2): halving the step divides it by $2^4 = 16$. The record measured exactly this ratio, 16.00, between its canonical run ($G = 900$) and a refined run ($G = 1800$) (check refined_free_spectra_convergence_order of `Revision/kohn_sham/reports/ks-rust-determinism.json`; Section 14.14).

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

**A detail that matters for Newton's method.** For the derivative $d\Phi/d\varepsilon = f\int r^2dy/r(0)^2$ the solver integrates $r^2$ with the simpler **trapezoid rule** on the step ends while it shoots ($\tfrac{h}{2}(r_i^2 + r_{i+1}^2)$ per step). This derivative only steers Newton's method; an error in it changes how fast the root is found, not where it is.

### 15.4 From one level to the whole gas

**Label sets.** For a state of the gas the solver chooses the sectors and labels it will solve, its **label set**. It takes the shells $n_2 = 0, 1, 2, \dots$ in turn, with all four sectors (two block types, two fold conditions) of each shell, fills the free levels found so far from the lowest upward, and stops adding shells when the lowest level of a new shell lies more than a margin above the lowest empty level (the LUMO) of that filling (in the canonical runs the margin is $0.25\,m$ plus twice the target size $0.1\,m$ or $0.3\,m$ of the coupling's first-order potential); in the occupied shells and the next one it solves three particle labels per sector, elsewhere the lowest only (`Revision/kohn_sham/solver/src/scf.rs`, the function `specs_t0`). The check ground_window_complete of the solver's report confirms for all 75 ground states that the lowest level outside the label set lies above the LUMO of the converged state, so no level that matters was left out.

**The fold band.** For $k > 0$ the even level of label 0 of block type $j = +1$ grows out of the zero mode. Section 14.19 showed that it is known exactly: the zero-mode orbital $(e^{fMy}, 0)$ solves the block equation with $b = 0$ for every $k$ at the level

$$
\varepsilon_{band}(k) = \kappa k = k\,e^{-a_{4,0}} ,
$$

because with $b = 0$ the first equation is $a' = fMa$ and the second needs $j(\varepsilon - v) - \kappa k = 0$, that is $\varepsilon = \kappa k$ for $j = +1$ and $v = 0$; $b = 0$ holds at the tip and at the fold. The orbital stays at the fold, which gives the band its name: the **fold band**. Its slope is $\kappa = e^{-a_{4,0}}$ for every mass, cutoff and hidden scale (ks-theory.json, checksNumeric; check brane_band_slope, a name kept from an earlier construction; the solver measured the slope at the five slices to $2.05 \times 10^{-16}$ relative, check free_brane_band_slope). The mass term only holds the orbital at the fold and drops out of the level: the band is exactly linear, like the energy of a massless particle.

**The two block types and the sea.** Without interaction the two block types mirror each other: $h_{-1} = -h_{+1}$ as operators with the same boundary conditions (check block_type_relation), so every orbital of $j = +1$ is also an orbital of $j = -1$, with the same $k$ and fold condition and the opposite level. The band of $j = -1$ therefore lies at $-\kappa k$, below zero: it belongs to the sea, and the positive band levels are those of $j = +1$ only, each $4r_3(n_2)$-fold. At $k = 0$ the zero mode ($\varepsilon = 0 = -0$) belongs to both types, so the zero-mode level is $4 + 4 = 8$-fold.

**The rescaling identity and the redshift.** The slice enters the block equation through $\kappa k$ and $f$, and the densities through $\mathrm{Vol}_7$. Writing the equation in the proper hidden coordinate $Y = fy$ removes $f$ from it and moves it into the constants: the state at the slice $a_{4,0}$ is the state at the slice 0 with the 3-momenta redshifted, $\Delta k \to \Delta k\,e^{-a_{4,0}}$, a shorter hidden interval, $L \to fL$, a larger warp rate, $H \to H/f$, and a smaller extra-time volume, $v_t \to v_t\,e^{-a_{4,0}}$ on the history (ks-theory.json, rescalingIdentity; check rescaling_identity; Section 14.7). Without interaction it reads

$$
\varepsilon(k,\ a_{4,0};\ L) = \varepsilon(k\,e^{-a_{4,0}},\ 0;\ fL)
$$

for every level (the constant $H$ does not enter the free levels); with interaction the whole self-consistent state obeys it, and the solver solved each of 60 partner problems independently and found the same levels to $1.643 \times 10^{-13}\,m$ (check rescaling_identity_between_slices of `Revision/kohn_sham/reports/ks-rust-solver.json`). Three consequences:

- The fold band redshifts exactly: a band level of a fixed shell decreases like $e^{-a_{4,0}}$ along the history.
- The levels at $k = 0$ other than the zero modes rise, because the proper length $fL$ of the cut-off half shrinks (Section 15.3); the zero modes stay at 0.
- Every energy of the free gas that comes from band levels falls exactly like $e^{-a_{4,0}}$.

**The gap of $N = 8$, exactly.** For $N = 8$ the highest occupied level is the zero mode ($\varepsilon = 0$) and the lowest empty one is the band level of the first shell, $k = \Delta k = 0.25$. So the Kohn-Sham gap is

$$
\Delta_{KS}(a_{4,0}) = \kappa\,\Delta k = 0.25\,e^{-a_{4,0}} ,
$$

$0.25$, $0.1516327$, $0.0919699$, $0.0557825$ and $0.0338338$ at the five slices (Notebook 15a, Out [7]; the column KS_gap of `Revision/kohn_sham/results/ground/summary.csv`). As 3-space inflates, the lattice momenta are redshifted and the empty band levels come down toward the filled zero modes, exactly like $e^{-a_{4,0}}$.

**Aufbau and closed shells.** At $T = 0$ the solver fills the levels from the lowest upward, with exact groups of equal levels (levels within $10^{-9}\,m$ count as equal); a group that would be filled only in part is flagged as an **open shell**. The particle numbers of Section 15.2 were chosen as closed shells, and the check ground_closed_shell confirms for all 75 ground states that no group is partly filled.

### 15.5 Self-consistency, the energy, and the first excited state

**The loop.** The unknowns of the self-consistent problem are the two functions $M(y) - m$ and $v(y)$ on the 1801 points of the fine grid, collected in one long list $x$ of $2 \times 1801$ numbers (the solver keeps a third function for a variant with the exact Fock exchange, zero in the canonical functional). One **iteration**: (1) from the input $x$, solve every level of the label set (Section 15.3); (2) fill them (aufbau at $T = 0$, Fermi-Dirac at $T > 0$); (3) build the densities $n$ and $S$ and from them the output potentials $x_{out} = \big(\tfrac{15}{16}\hat\lambda S,\ -\tfrac{1}{16}\hat\lambda n\big)$; (4) the **residual** is $r = x_{out} - x$, and its size is its largest entry in absolute value. The loop stops when this size is at most $10^{-11}\,m$. Without interaction $x_{out} = 0 = x$ after one iteration.

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

**The energy: why the interaction energy is subtracted.** The energy of the interacting gas is its kinetic and mass energy plus the interaction energy. Each level $\varepsilon$ already contains the potential energy of its orbital in the mean field, so the sum $\sum gf_o\varepsilon$ counts the interaction twice. Line by line, with $\langle\cdot\rangle$ meaning $2\,\mathrm{Vol}_7\int_{-L}^{0}e^{3Hy}(\cdot)\,dy$ (the amount in the whole cell, both halves):

$$
\sum g f_o\,\varepsilon = E_{kin} + \big\langle (M - m)S + v\,n\big\rangle .
$$

Rule: the level is the expectation value of the block Hamiltonian; the terms of $h$ with $M - m$ and $v$ give, summed with $wgf_oP$ over the occupied orbitals, the densities $S$ and $n$ times the potentials (the definitions of $S$ and $n$ in Section 15.2; the factor 2 of $\langle\cdot\rangle$ and the weight $w = \tfrac12$ cancel); everything else ($-(i/f)\sigma_1d/dy$, $m\sigma_2$, $\kappa k\sigma_3$) is collected in $E_{kin}$.

$$
(M - m)S + v\,n = S\frac{\partial e_{int}}{\partial S} + n\frac{\partial e_{int}}{\partial n} = \hat\lambda\Big(\tfrac{15}{16}S^2 - \tfrac{1}{16}n^2\Big) = 2\,e_{int} .
$$

Rule: the potentials are the derivatives of $e_{int}$ (Section 15.2), and $e_{int}$ is a sum of squares, homogeneous of degree 2 (Euler's rule: $S\,\partial_Se + n\,\partial_ne = 2e$ for such a function); compare the coefficients $\tfrac{15}{16} = 2\cdot\tfrac{15}{32}$ and $\tfrac{1}{16} = 2\cdot\tfrac{1}{32}$.

$$
E = E_{kin} + \langle e_{int}\rangle = \sum gf_o\varepsilon - 2\langle e_{int}\rangle + \langle e_{int}\rangle = \sum gf_o\varepsilon - 2\,\mathrm{Vol}_7\int_{-L}^{0}e^{3Hy}e_{int}\,dy .
$$

Rule: insert the first two lines. This is $E_{KS}$ of Section 15.2 (ks-theory.json, thermodynamics.energy; check ks_onshell_lagrangian for the same degree-2 identity). The solver also computes the **variational form**, $\sum gf_o\varepsilon - \langle (M_{in} - m)S_{out} + v_{in}n_{out}\rangle + \langle e_{int}(S_{out}, n_{out})\rangle$, with the input potentials and output densities of the last iteration; the two agree to $1.764 \times 10^{-11}$ relative in all 75 ground states (check ground_energy_two_forms).

**An exact symmetry of the zero-mode state.** For $N = 8$ the eight occupied orbitals are the zero modes at $k = 0$. We show that changing the sign of $\hat\lambda$ changes the sign of the energy, $E_{KS}(-\hat\lambda) = -E_{KS}(\hat\lambda)$. Line by line:

- At $k = 0$ the block equations of type $j$ are $a' = f[Ma - j(\varepsilon - v)b]$ and $b' = f[j(\varepsilon - v)a - Mb]$. Rule: Section 15.2 with $k = 0$.
- Put $\tilde a = a$, $\tilde b = -b$, $\tilde\varepsilon = -\varepsilon$, $\tilde v = -v$ and keep $M$, $f$ and $j$. Then $\tilde\varepsilon - \tilde v = -(\varepsilon - v)$, and $\tilde a' = f[M\tilde a - j(\tilde\varepsilon - \tilde v)\tilde b]$, $\tilde b' = f[j(\tilde\varepsilon - \tilde v)\tilde a - M\tilde b]$. Rule: in each equation the two sign changes ($b \to -b$ and $\varepsilon - v \to -(\varepsilon - v)$) cancel.
- So $(a, -b)$ is an orbital of the problem with $(M, -v)$ at the level $-\varepsilon$, with the same boundary conditions ($b = 0$ stays $b = 0$) and the same label (the angle $\theta$ becomes $-\theta$, so $\Phi \to -\Phi$, and the zero-mode label 0 stays 0). Rule: the previous line and the definition of the label.
- Its density $a^2 + b^2$ is unchanged and its scalar density $2jab$ changes sign: $n \to n$, $S \to -S$. Rule: the definitions of Section 15.2.
- With $-\hat\lambda$ the potentials made by these densities are $\tfrac{15}{16}(-\hat\lambda)(-S) = M - m$ and $-\tfrac{1}{16}(-\hat\lambda)n = -v$: exactly the potentials assumed. So the mapped orbitals form a self-consistent state of $-\hat\lambda$. Rule: the formulas of $M$ and $v$.
- Its energy: every level changes sign, so $\sum gf_o\varepsilon$ does; $e_{int} = \hat\lambda(\tfrac{15}{32}S^2 - \tfrac{1}{32}n^2)$ changes sign with $\hat\lambda$ while $S^2$ and $n^2$ stay. Hence $E_{KS}(-\hat\lambda) = -E_{KS}(\hat\lambda)$. Rule: the energy formula above.

This is PROVED for the mapped state; that the loop started from the free state finds exactly this state is COMPUTED (Notebook 15e finds $|E(+\lambda) + E(-\lambda)| = 0$ exactly, Out [13], and the record lists $E_{KS} = \mp3.7786683\times10^{-2}$ for $\pm\lambda_1$ at $a_{4,0} = 0$). These are values at the cutoff $L = 3$; the record's study of larger $L$ finds the partners negatives of each other at every $L$ (Section 15.2, the paragraph on the cutoff). The symmetry is special to the zero modes: for larger $N$ the band orbitals have $k \ne 0$, and the map would need $k \to -k$, which turns a level of block type $j$ into one of type $-j$, a sea level. There the record shows a different regularity: repulsion lowers the energy and attraction raises it (for $N = 592$ at $a_{4,0} = 0$, $E_{KS}(\pm\lambda_1) - E_{KS}(0) = -2.8151$ and $+2.7794$), because the occupied fold-band orbitals $(e^{fMy}, 0)$ have $b = 0$ and so no scalar density, and to first order the only interaction energy is the exchange term $-\tfrac{1}{32}\hat\lambda n^2$ (Section 15.15).

**The first excited state: Delta-SCF.** Chapter 13 defined the Kohn-Sham gap $\Delta_{KS} = \varepsilon_{LUMO} - \varepsilon_{HOMO}$ and the Delta-SCF energy $\Delta_{SCF} = E_1 - E_0$, the difference of two self-consistent energies, the second with one particle moved from the highest occupied level to the lowest empty one. The solver uses an **ensemble** form: it removes one particle uniformly from the whole highest occupied group of equal levels and adds it uniformly to the whole lowest empty group, so that every orbital of a group keeps the same occupation and the block and direction symmetry of the reduction is kept (parameters.json, conventions.deltaScf). Without interaction the levels do not depend on the occupations, so $\Delta_{SCF} = \Delta_{KS}$ exactly (Janak's theorem of Chapter 13 with constant levels); the solver checks this in all 15 free states (check excited_delta_scf_free_equals_gap, largest difference $3.1 \times 10^{-13}\,m$). With interaction the orbitals relax and the two differ by the **orbital relaxation** $\Delta_{SCF} - \Delta_{KS}$; for example for `N8_lamp2_a00` the record has $\Delta_{KS} = 0.24993310$ and $\Delta_{SCF} = 0.24993289$, a relaxation of $-2.1 \times 10^{-7}\,m$, and the largest relaxation of the matrix, $6.3 \times 10^{-4}\,m$, belongs to `N2352_lamp1_a00`, whose excited particle goes into the bulk edge (`Revision/kohn_sham/results/excited/summary.csv`).

### 15.6 Example: the solver's method by hand (Notebook 15e)

Notebook 15e writes the method of Sections 15.3 to 15.5 in plain Python, exactly as the Rust solver does it (`Revision/kohn_sham/solver/src/shoot.rs` and `scf.rs`), for the corrected metric, and reproduces numbers of the record: the grid, the hidden scale $f$ of the five slices, the cell volume and Simpson's rule; one shooting integration with the Pruefer angle; the phase function and the levels it labels (Figure 15e.1); Newton's method inside a bracket, the exact levels at $k = 0$ at the first slice and at $a_{4,0} = 1.5$, and the solver's own levels; the orbitals with Hermite midpoints and the exact fold-band orbital (Figure 15e.2); the order 4 of RK4 (Figure 15e.3); the exact fold band $\varepsilon = \kappa k$, its slope, the rising bulk levels and the rescaling identity (Figure 15e.4); the self-consistent loop with Anderson mixing for $N = 8$, compared with linear mixing (Figure 15e.5); the four couplings and the symmetry $E(-\lambda) = -E(\lambda)$; and the self-consistent potentials (Figure 15e.6). It needs no Rust, runs in less than a minute, and ends with ALL 19 CHECKS PASSED (notebook 15e).

What to look for: in Figure 15e.1 the steadily rising curve and the places where it crosses the horizontal lines (each crossing is one level, and none can be skipped); in Figure 15e.2 the fold-band orbital of the last slice, flatter than the zero mode of the first; in Figure 15e.3 the straight lines of slope 4; in Figure 15e.4 the dots exactly on the three lines $k\,e^{-a_{4,0}}$, and the dashed bulk levels that move up; in Figure 15e.5 the blue dots, which fall on average about fourfold per iteration, and the black crosses of the Rust solver on top of them.

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

The first line calls the function and names its result `REPO`. It is never printed, because it differs from computer to computer, while the printed output of a notebook must not. The second line chooses where files are written. `os.environ` holds the **environment variables** of the program (named texts that it receives from the computer); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and the default `str(REPO)` (the repository folder as a string) otherwise. When you run the notebook the variable is not set, so the files go into the repository; the book's checking tool sets it to a scratch folder, so that a check never changes a file that git tracks. (Notebook 15e writes nothing else. The notebooks 15a, 15b and 15d, which run the Rust solver, also write the solver's raw output into the folders `Revision/kohn_sham/solver/target/textbook_15a`, `textbook_15b` and `textbook_15d` next to it, about 2 MB, 1.8 MB and 1.2 MB; git ignores these folders, and they are written during a check too.)

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

**In [2], the grid, the hidden scale and the cell volume.**

```python
import csv  # reads the tables (CSV files) of the Revision record
import math  # exp, sqrt, atan2, pi for single numbers

import numpy as np  # arrays of numbers
```

`csv` reads tables stored as comma-separated text, `math` holds the mathematical functions for single numbers, and numpy (under the short name `np`) works with **arrays**, lists of numbers on which arithmetic acts entry by entry.

```python
H, MASS, L = 1.0, 1.0, 3.0  # the units H = m = 1 and the tip cutoff L = 3
DK = 0.25  # the spacing of the 3-momenta
BETA = 4.0 / 3.0  # the history b4 = e^{beta a4} of the record (beta = 4/3)
ELL = 2.0 * math.pi / DK  # the side of the coordinate 3-torus
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
```

The first line gives three names at once: $H = 1$, $m = 1$ (called `MASS`, because the letter m is used for other things below) and $L = 3$. `DK` is $\Delta k = 0.25$. `BETA` is the exponent $\beta = \tfrac43$ of the record's history $b_4 = e^{\beta a_4}$ (with $b_4(0) = 1$). `ELL` is the side $\ell = 2\pi/\Delta k = 8\pi$ of the coordinate 3-torus. `PALETTE` is a list of eight colours, written as hexadecimal colour codes.

```python
def hidden_scale(a4):
    return math.exp((0.5 * BETA - 1.0) * a4)


def vol7(a4):
    return ELL * ELL * ELL * math.exp((2.0 * BETA - 1.0) * a4)
```

Two small functions of the slice. `hidden_scale(a4)` is $f = e^{-a_4}b_4^{1/2} = e^{-a_4}e^{(\beta/2)a_4} = e^{(\beta/2 - 1)a_4}$, which for $\beta = \tfrac43$ is $e^{-a_4/3}$ (Section 15.1). `vol7(a4)` is the proper 7-volume of the cell per unit $e^{3Hy}$, $\mathrm{Vol}_7 = \ell^3v_t\,e^{-a_4}b_4^2 = \ell^3\,e^{(2\beta - 1)a_4}$ with $v_t = 1$, which for $\beta = \tfrac43$ is $\ell^3e^{(5/3)a_4}$ (Section 15.2). Writing the exponents with `BETA` instead of the numbers $-\tfrac13$ and $\tfrac53$ shows where they come from.

```python
def make_grid(steps, length=L):
    points = 2 * steps + 1  # step ends and step midpoints
    y = [-length * ((points - 1 - f) / (points - 1)) for f in range(points)]
    half = 0.5 * length / steps  # the distance between two fine points
    weights = [(4.0 if f % 2 == 1 else 2.0) * half / 3.0 for f in range(points)]
    weights[0] = weights[-1] = half / 3.0  # Simpson: 1, 4, 2, 4, ..., 4, 1 (x h/6)
    return {"steps": steps, "h": length / steps, "points": points, "y": y,
            "e3": [math.exp(3 * H * v) for v in y], "simpson": np.array(weights)}
```

`make_grid` builds the solver's grid for a given number of RK4 steps on the interval from $-$`length` to 0; `length=L` is a **default value**, used when the caller gives no length (In [9] uses a shorter interval). The fine grid has `points` $= 2G + 1$ points (the step ends and the step midpoints). The second line is a **list comprehension** (a list built by a `for` inside square brackets): for $f = 0, 1, \dots, 2G$ it computes $y_f = -L\,(2G - f)/(2G)$, which is $-L$ for $f = 0$ and $0$ for $f = 2G$; this is the formula $y_f = -L + f\,h/2$ of Section 15.3 written so that the last point is exactly 0. (Here the letter `f` is only the counter of the list comprehension, not the hidden scale.) `half` is the spacing $h/2$. The weights of Simpson's rule with spacing $h/2$ are $\tfrac{h/2}{3}$ times 4 at the odd points (`f % 2 == 1`: the remainder of $f$ divided by 2 is 1), 2 at the inner even points and 1 at the two ends; the next line sets the two ends (`weights[-1]` is the last entry). The function returns a dictionary with the number of steps, the step $h = L/G$, the number of points, the coordinates, the volume factor $e^{3Hy}$ at every fine point (key `"e3"`) and the Simpson weights as an array.

```python
GRID = make_grid(900)  # the canonical grid of the solver
Y = np.array(GRID["y"])
E3 = np.array(GRID["e3"])
simpson_test = float(np.sum(GRID["simpson"] * np.exp(Y)))
say(f"fine grid: {GRID['points']} points, step h = {GRID['h']:.6f}")
report("hidden scale f at a4,0 = 0, 0.5, 1, 1.5, 2",
       ", ".join(f"{hidden_scale(a):.6f}" for a in (0.0, 0.5, 1.0, 1.5, 2.0)))
report("Vol_7 at a4,0 = 0 and 2", f"{vol7(0.0):.6f} and {vol7(2.0):.3f}")
report("Simpson integral of e^y from -3 to 0", f"{simpson_test:.15f}")
check(abs(simpson_test - (1.0 - math.exp(-3.0))) < 1e-13,
      "Simpson's rule on the fine grid integrates e^y exactly to 1e-13")
```

`GRID` is the canonical grid ($G = 900$); `Y` and `E3` are its coordinates and volume factors as arrays. `simpson_test` is Simpson's rule applied to $e^y$: the sum of weight times value over the 1801 points (`np.sum` adds the entries of an array; `float` turns the result into an ordinary number). The exact integral is $\int_{-3}^{0}e^y\,dy = 1 - e^{-3} = 0.950212931632136$. The format `:.6f` prints six digits after the point, `:.15f` fifteen; `", ".join(...)` writes the five hidden scales separated by commas. Out [2] prints 1801 points and the step $0.003333$; the hidden scales $1$, $0.846482$, $0.716531$, $0.606531$, $0.513417$ at the five slices (at the last slice the hidden direction has shrunk to about half); the volumes $\mathrm{Vol}_7(0) = 15875.213660$ and $\mathrm{Vol}_7(2) = 445008.034$ (the factor $e^{10/3} = 28.03$); and the integral $0.950212931632177$, which differs from the exact value by $4 \times 10^{-14}$, so the check passes.

**In [3], one shooting integration.**

```python
def rhs(m_y, kk, je, a, b):
    return m_y * a - (kk + je) * b, (je - kk) * a - m_y * b
```

`rhs` (right-hand side) returns the pair $(a', b')$ of the block equation for given values of $fM$ (`m_y`), $f\kappa k$ (`kk`), $fj(\varepsilon - v)$ (`je`), $a$ and $b$: $a' = fMa - (f\kappa k + fj(\varepsilon - v))b$ and $b' = (fj(\varepsilon - v) - f\kappa k)a - fMb$, which is Section 15.2 with the factor $f$ multiplied into the three coefficients.

```python
def shoot(eps, k, j, a4, mass, pot, grid=GRID, store=False):
    h = grid["h"]
    fh = hidden_scale(a4)  # the hidden scale f of the slice
    kk = k * math.exp(-a4)  # kappa k = k e^{-a4,0}, the same at every y
    coef = [(fh * mass[f], fh * kk, fh * j * (eps - pot[f]))
            for f in range(grid["points"])]
```

`shoot` integrates from the tip to the fold for the trial energy `eps`, the momentum `k`, the block type `j`, the slice `a4` and the potentials `mass` ($M$) and `pot` ($v$), given as lists on the fine grid. The arguments `grid=GRID` and `store=False` have default values. `fh` is the hidden scale $f$ of the slice (named `fh` so that it does not clash with the counter `f`). `kk` is $\kappa k = k\,e^{-a_{4,0}}$, the same number at every point. `coef` is a list with one triple $(fM, f\kappa k, fj(\varepsilon - v))$ per fine point, computed once before the integration; this is how the solver does it, so that the arithmetic is the same.

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
    return j * theta, fh * area / r2_prev, nodes
```

`r2` is $r^2 = a^2 + b^2$ at the new step end; the trapezoid rule adds $\tfrac{h}{2}(r_i^2 + r_{i+1}^2)$ for the step. When `store` is true, the new values are appended to `nodes`. After the loop the function returns three things: $\Phi = j\,\theta(0)$, the derivative $d\Phi/d\varepsilon = f\int r^2dy/r(0)^2$ of Section 15.3 (`r2_prev` now holds $r(0)^2$, and the factor `fh` is the $f$ of the formula), and the stored values.

```python
FREE_MASS = [MASS] * GRID["points"]  # M = m everywhere (no interaction)
FREE_POT = [0.0] * GRID["points"]  # v = 0 everywhere
phi_zero, _, _ = shoot(0.0, 0.0, 1, 0.0, FREE_MASS, FREE_POT)
report("Phi(0) for k = 0, j = +1 (the zero mode: b stays 0)", phi_zero)
check(phi_zero == 0.0, "at eps = 0 and k = 0 the Pruefer angle stays exactly 0")
```

`[MASS] * n` is a list of $n$ copies of 1.0: the free potentials $M = m$ and $v = 0$ on the 1801 fine points. The shot at $\varepsilon = 0$, $k = 0$, $j = +1$, $a_{4,0} = 0$ is the zero mode; the underscores `_` receive the two results that are not needed. With $k = 0$ and $\varepsilon - v = 0$ the equation for $b$ is $b' = -fMb$, and $b = 0$ at the tip; so every RK4 stage gives exactly $b = 0$, `atan2(0, a)` is exactly 0 for $a > 0$, and $\Phi = 0$ without any rounding error. Out [3] prints the RESULT line with the value 0.0 and the PASS line. The text cell that follows the cell in the notebook repeats the derivation of $d\Phi/d\varepsilon$ of Section 15.3.

**In [4], the phase function.**

```python
energies = np.linspace(-4.0, 4.0, 401)  # 401 trial energies
phase = np.array([shoot(e, 0.0, 1, 0.0, FREE_MASS, FREE_POT)[0] for e in energies])
```

`np.linspace(-4.0, 4.0, 401)` makes 401 equally spaced numbers from $-4$ to $4$ (spacing 0.02). For each of them the cell shoots with $k = 0$, $j = +1$, no interaction and the first slice ($f = 1$) and keeps the first result, $\Phi$ (`[0]` takes the first entry of the returned triple).

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

The target $t_l$ of a level: $l\pi$ for the even fold condition, $\pi/2 + l\pi$ for the odd one. The argument is called `parity`, like the column of the record that holds the fold condition, and takes the values `"even"` and `"odd"`. `a if condition else b` is Python's choice between two values.

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

`find_level` returns the energy of the level with the given momentum, block type, fold condition and label in the given potentials at the slice `a4`, starting from the energy `guess`. The inner function `g` shoots at the energy `e` and returns $\Phi - t_l$ and $d\Phi/d\varepsilon$. `ec`, `gc`, `dc` are the current energy, its value of $\Phi - t_l$ and its derivative. If the guess hits the target exactly, it is returned at once. The first trial step is 1.2 times the Newton estimate $|\Phi - t_l|/\Phi'$ of the distance to the root, but at least $10^{-4}$ and at most 2.

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

The same walk downward: if $\Phi$ is above the target, the walk goes down until $\Phi - t_l \le 0$. Afterwards `[lo, hi]` brackets the root; if one end hit it exactly, it is returned.

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
def odd_momentum(n, fh):
    lo, hi = (n - 0.5) * math.pi / (fh * L), n * math.pi / (fh * L)
    g = lambda p: MASS * math.sin(p * fh * L) + p * math.cos(p * fh * L)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if g(lo) * g(mid) > 0.0 else (lo, mid)
    return 0.5 * (lo + hi)
```

The odd levels need the roots $p$ of $\tan(pfL) = -p/M$ (Section 15.3), now with the hidden scale `fh`. Multiplied by $M\cos(pfL)$ this is $g(p) = M\sin(pfL) + p\cos(pfL) = 0$, which has no division. The $n$-th root lies between $(n - \tfrac12)\pi/(fL)$ and $n\pi/(fL)$: at the left end $\cos(pfL) = 0$ and $g = \pm M$, at the right end $\sin(pfL) = 0$ and $g = \pm p$ with the opposite sign, so $g$ changes sign in between (Section 14.13). `lambda p: ...` defines a small function without a name. The loop is **bisection**: if $g$ has the same sign at `lo` and at the midpoint (their product is positive), the root lies in the right half, otherwise in the left half. After 200 halvings the interval is far below rounding size, and its midpoint is returned.

```python
def exact_level(parity, label, fh=1.0):
    if parity == "even":
        n = abs(label)
        return math.copysign(math.sqrt(MASS ** 2 + (n * math.pi / (fh * L)) ** 2),
                             label) if n else 0.0
    n = label + 1 if label >= 0 else -label  # labels 0, 1, ... and -1, -2, ...
    return math.copysign(math.sqrt(MASS ** 2 + odd_momentum(n, fh) ** 2), label + 0.5)
```

The exact free level at $k = 0$ with a given fold condition, label and hidden scale (the default `fh=1.0` is the first slice). For the even condition the label $l$ belongs to $n = |l|$ and the level is $\pm\sqrt{M^2 + (n\pi/(fL))^2}$ with the sign of $l$ (`math.copysign(x, s)` is $|x|$ with the sign of $s$); the label 0 is the zero mode, $\varepsilon = 0$ (`if n else 0.0`: a nonzero $n$ counts as true). For the odd condition the labels $0, 1, 2, \dots$ are the positive levels with $n = l + 1$, and the labels $-1, -2, \dots$ the negative ones with $n = -l$; the sign is that of $l + \tfrac12$, which is positive for $l \ge 0$ and negative for $l \le -1$.

```python
RECORD_FREE = "Revision/kohn_sham/results/spectrum/free-k0-analytic.csv"
recorded = {}
for line in repository_file(RECORD_FREE).read_text(encoding="utf-8").split("\n")[1:]:
    if line:
        m_, l_, a4_, f_, parity, label, eps_num, eps_exact, _ = line.split(",")
        if float(m_) == 1.0 and float(l_) == 3.0:
            recorded[(float(a4_), parity, int(label))] = (float(eps_num),
                                                          float(eps_exact))
```

The record file of the solver's free spectra at $k = 0$ is read as text, split into lines, and the first line (the column names) is skipped (`[1:]` takes everything from the second entry on). Each nonempty line is split at the commas into nine fields: the mass, $L$, the slice, the hidden scale, the fold condition, the label, the solver's numerical level, the exact level and one more column that is not needed. Only the rows with $M = 1$ and $L = 3$ are kept (the record also tests $L = 2$ and $M = 2$), in a dictionary whose key is the triple (slice, fold condition, label); with $M = 1$, $L = 3$ the record has the slices 0 and 1.5.

```python
worst_exact, worst_record = 0.0, 0.0
say("a4,0  parity label   shooting           exact              difference")
for a4 in (0.0, 1.5):
    fh = hidden_scale(a4)
    for parity in ("even", "odd"):
        for label in range(-3, 6):
            exact = exact_level(parity, label, fh)
            found = find_level(0.0, 1, parity, label, a4, FREE_MASS, FREE_POT,
                               exact + 0.01)
            say(f"{a4:4.1f}  {parity:5} {label:3d}  {found:17.13f}  {exact:17.13f}"
                f"  {found - exact:10.2e}")
            if abs(exact) < 4.0:
                worst_exact = max(worst_exact, abs(found - exact))
            if (a4, parity, label) in recorded:
                worst_record = max(worst_record,
                                   abs(found - recorded[(a4, parity, label)][0]))
```

For the slices 0 and 1.5 (the hidden scales 1 and $e^{-1/2}$), both fold conditions and the labels $-3$ to $5$ the cell computes the exact level, finds the level by shooting (with the guess 0.01 above the exact value), and prints a table row: the slice, the fold condition in 5 characters, the label in 3 digits, both levels with 13 digits after the point, and their difference in the exponent format `.2e` (two digits after the point and a power of ten). The largest difference is kept for $|\varepsilon| < 4$ (`worst_exact`; the record uses the same range for its tolerance), and the largest difference to the solver's recorded value for every row present in the record (`worst_record`).

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

Out [6] shows the table. At the first slice the lowest levels are $\pm1.4479719304$ (even) and $\pm1.2922928281$ (odd, the bulk edge); at the slice 1.5 they are $\pm1.9952267011$ and $\pm1.5905829045$: with the shorter hidden direction every level away from zero is higher (Section 15.3). The differences grow with the energy, from $10^{-13}$ near the lowest levels to $1.10 \times 10^{-8}$ at the odd label 5 of the slice 1.5 ($\varepsilon = 9.61$): the error of RK4 grows like $(fh\varepsilon)^4$, because a higher level oscillates faster. The largest difference for $|\varepsilon| < 4$ is $7.23 \times 10^{-10}$, the value of the record's check free_k0_analytic_spectra. The first check therefore tests the tolerance $5 \times 10^{-9}$ only for $|\varepsilon| < 4$, as the record does; for $|\varepsilon| \ge 4$ the record allows $3 \times 10^{-7}$, far above the $1.10 \times 10^{-8}$ of the table. The largest difference to the solver's own numbers is $9.77 \times 10^{-15}$: the Python code and the Rust program do the same arithmetic in a slightly different order. Both checks pass. The even label 0 is printed as $-0.0000000000000$, a difference of about $-10^{-19}$ from the exact zero, left by Newton's method.

**In [7], orbitals with Hermite midpoints.**

```python
def orbital(eps, k, j, a4, mass, pot, grid=GRID):
    _, _, nodes = shoot(eps, k, j, a4, mass, pot, grid, store=True)
    h = grid["h"]
    fh = hidden_scale(a4)
    kk = fh * k * math.exp(-a4)  # f kappa k
    a = np.zeros(grid["points"])
    b = np.zeros(grid["points"])
    a[0::2] = [p[0] for p in nodes]  # the step ends
    b[0::2] = [p[1] for p in nodes]
```

`orbital` returns the normalised orbital of a level on the whole fine grid. It shoots once more at the level's energy and keeps the values at the $G + 1$ step ends. `kk` is now the coefficient $f\kappa k$ of the equation. `np.zeros(n)` is an array of $n$ zeros. `a[0::2]` is every second entry starting with the first (the fine indices $0, 2, 4, \dots$, the step ends), and the step-end values are written there.

```python
    f = np.arange(0, grid["points"], 2)  # fine indices of the step ends
    m_y = fh * np.array(mass)[f]  # f M at the step ends
    je = fh * j * (eps - np.array(pot)[f])  # f j (eps - v)
    da = m_y * a[f] - (kk + je) * b[f]  # derivatives from the equation
    db = (je - kk) * a[f] - m_y * b[f]
```

`np.arange(0, n, 2)` is the array $0, 2, 4, \dots$ of the step-end indices (here `f` is again an index array, not the hidden scale); indexing an array with it picks those entries. So `m_y` and `je` are $fM$ and $fj(\varepsilon - v)$ at the step ends, and `da`, `db` are the derivatives $a'$, $b'$ there, computed from the block equation itself (this is where the Hermite formula gets its derivatives).

```python
    a[1::2] = 0.5 * (a[f][:-1] + a[f][1:]) + h / 8.0 * (da[:-1] - da[1:])
    b[1::2] = 0.5 * (b[f][:-1] + b[f][1:]) + h / 8.0 * (db[:-1] - db[1:])
    norm = math.sqrt(float(np.sum(grid["simpson"] * (a * a + b * b))))
    return a / norm, b / norm
```

`a[1::2]` are the midpoints. For each step, `a[f][:-1]` is the value at its start (all step ends but the last) and `a[f][1:]` the value at its end (all but the first); the line is the Hermite formula $\tfrac12(u_0 + u_1) + \tfrac{h}{8}(u_0' - u_1')$ of Section 15.3, for all steps at once. Then Simpson's rule gives $\int(a^2 + b^2)\,dy$, and both components are divided by its square root, so the returned orbital is normalised on one half of the cell.

```python
def exact_fold_orbital(a4):
    fm = hidden_scale(a4) * MASS
    return math.sqrt(2.0 * fm / (1.0 - math.exp(-2.0 * fm * L))) * np.exp(fm * Y)
```

`exact_fold_orbital(a4)` is the exact normalised component $a = \sqrt{2fM/(1 - e^{-2fML})}\,e^{fMy}$ of the zero mode and of the fold band at the slice (Section 15.3; $b = 0$), on the fine grid. `fm` is the product $fM$.

```python
zero_a, zero_b = orbital(0.0, 0.0, 1, 0.0, FREE_MASS, FREE_POT)
bulk_eps = find_level(0.0, 1, "even", 1, 0.0, FREE_MASS, FREE_POT, 1.4)
bulk_a, bulk_b = orbital(bulk_eps, 0.0, 1, 0.0, FREE_MASS, FREE_POT)
band_eps = find_level(0.5, 1, "even", 0, 2.0, FREE_MASS, FREE_POT, 0.06)
band_a, band_b = orbital(band_eps, 0.5, 1, 2.0, FREE_MASS, FREE_POT)
```

Three orbitals of the free block $j = +1$: the zero mode ($\varepsilon = 0$, $k = 0$, first slice); the first even bulk level at $k = 0$ and the first slice (label 1, guess 1.4; its energy is $1.4479719$, Out [6]); and the fold-band level at $k = 0.5$ (the shell $n_2 = 4$; label 0) at the last slice $a_{4,0} = 2$, with the guess 0.06, a little below $\kappa k = 0.5\,e^{-2} = 0.0677$.

```python
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6), sharey=True,
                         layout="constrained")
for ax, (a, b, title) in zip(axes, [
        (zero_a, zero_b, "zero mode, $k = 0$, $a_{4,0} = 0$"),
        (bulk_a, bulk_b, f"bulk, $k = 0$, $\\varepsilon = {bulk_eps:.4f}$"),
        (band_a, band_b, f"fold band, $k = 0.5$, $a_{{4,0}} = 2$")]):
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

`plt.subplots(1, 3, ...)` makes one row of three drawing areas (`axes`), which share the vertical axis (`sharey=True`); `layout="constrained"` spaces them so that no labels overlap. `zip` pairs each drawing area with one triple (the two components and a title; in an f-string a doubled brace `{{` prints one brace), and the loop draws $a$ solid and $b$ dashed against $y$. The first panel gets the vertical label and the legend, and `save_figure` saves Figure 15e.2. The student should see that the zero mode is $e^{y}$ and sits at the fold with $b = 0$ everywhere, that the bulk orbital fills the whole interval, and that the fold-band orbital at the last slice is again $(e^{fy}, 0)$, now with the smaller $f = e^{-2/3}$ and therefore flatter, spread toward the tip; every $b$ vanishes at both ends.

```python
fold_error = max(float(np.max(np.abs(zero_a - exact_fold_orbital(0.0)))),
                 float(np.max(np.abs(band_a - exact_fold_orbital(2.0)))),
                 float(np.max(np.abs(zero_b))), float(np.max(np.abs(band_b))))
report("fold-band level at k = 0.5, a4,0 = 2, and kappa k", f"{band_eps:.15f}, "
       f"{0.5 * math.exp(-2.0):.15f}")
report("largest deviation of the two orbitals from (e^{f M y}, 0)", f"{fold_error:.2e}")
check(fold_error < 1e-11 and abs(band_eps - 0.5 * math.exp(-2.0)) < 1e-13,
      "the zero mode and the fold band are (e^{f M y}, 0) at eps = kappa k, to 1e-11",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "free_zero_mode_exact")
```

`fold_error` is the largest of four numbers: the largest deviation of the computed $a$ of the zero mode and of the band orbital from their exact forms, and the largest $|b|$ of each. Out [7] prints the band level $0.067667641618306$ and $\kappa k = 0.5\,e^{-2} = 0.067667641618306$, equal to all printed digits, and the deviation $1.35 \times 10^{-12}$, the value of the record's check free_zero_mode_exact, and PASS: the exact fold band of Section 15.4, found by shooting.

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

For the grids of 100, 200, 400 and 800 steps the cell finds the even levels with the labels 2 and 3 at $k = 0$ and the first slice (exact values $\sqrt{1 + (2\pi/3)^2} = 2.3208815$ and $\sqrt{1 + \pi^2} = 3.2969083$) and appends the size of the error to a list for each label. Looping over a dictionary (`for label in errors`) visits its keys, 2 and 3.

```python
ratios = []
for label, errs in errors.items():
    steps_ratios = [errs[i] / errs[i + 1] for i in range(len(errs) - 1)]
    ratios += steps_ratios
    say(f"label {label}: errors " + ", ".join(f"{e:.2e}" for e in errs)
        + "; ratios " + ", ".join(f"{r:.2f}" for r in steps_ratios))
```

For each label the three ratios of the error on one grid to the error on the grid with twice as many steps are computed, collected in `ratios` and printed. Out [8] shows the errors $2.45 \times 10^{-7}$, $1.53 \times 10^{-8}$, $9.59 \times 10^{-10}$, $5.99 \times 10^{-11}$ for the label 2 and ratios between 15.96 and 16.00.

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

**In [9], the fold band, the redshift and the rescaling identity.**

```python
THEORY = json.loads(repository_file("Revision/kohn_sham/ks-theory.json").read_text(
    encoding="utf-8"))  # the theory file of the solver
C_RECORD = float(THEORY["checksNumeric"]["braneBandSlope_a0"])  # c at a4,0 = 0
```

`json.loads` turns the text of the theory file into Python dictionaries and lists. `C_RECORD` is the recorded slope of the fold band at the first slice, $c = 1$ (the key keeps the earlier name "brane band").

```python
def band(k, a4, tol=1e-13):
    return find_level(k, 1, "even", 0, a4, FREE_MASS, FREE_POT,
                      0.9 * k * math.exp(-a4), tol=tol)


def bulk(k, a4):
    guess = math.hypot(exact_level("even", 1, hidden_scale(a4)), k * math.exp(-a4))
    return find_level(k, 1, "even", 1, a4, FREE_MASS, FREE_POT, guess)
```

`band(k, a4)` is the fold-band level: block type $+1$, even fold condition, label 0, free potentials, with the guess $0.9\,\kappa k$ just below the exact value; the tolerance can be chosen (the slope below needs a smaller one). `bulk(k, a4)` is the first bulk level of the same sector (label 1); its guess is $\sqrt{\varepsilon(0)^2 + \kappa^2k^2}$ (`math.hypot(x, y)` is $\sqrt{x^2 + y^2}$), the relativistic dispersion of Section 14.19 with the exact level $\varepsilon(0)$ at $k = 0$ of this slice.

```python
momenta = np.linspace(0.0, 2.0, 41)
fig, ax = plt.subplots()
worst_band, slopes = 0.0, []
for shade, a4 in zip(("#86b6ef", "#2a78d6", "#104281"), (0.0, 1.0, 2.0)):
    curve = [band(k, a4) for k in momenta]
    worst_band = max([worst_band] + [abs(e - k * math.exp(-a4))
                                     for e, k in zip(curve, momenta)])
    ax.plot(momenta, curve, "o", color=shade, ms=4, label=f"$a_{{4,0}} = {a4:.0f}$")
    ax.plot(momenta, momenta * math.exp(-a4), "-", color=shade, lw=1.2)
    ax.plot(momenta[::2], [bulk(k, a4) for k in momenta[::2]], "--", color=shade,
            lw=1.5)
    slopes.append(band(1e-4, a4, tol=1e-17) / 1e-4 * math.exp(a4))  # c e^{a4,0}
```

For the slices $a_{4,0} = 0, 1, 2$ (in light, middle and dark blue) the cell computes the band at 41 momenta from 0 to 2, keeps the largest deviation from the exact $\kappa k = k\,e^{-a_{4,0}}$ in `worst_band` (the list `[worst_band] + [...]` puts the old value in front of the new deviations), and draws the computed band as dots on the exact line. It also draws the first bulk level at every second momentum (`momenta[::2]`) as a dashed line. The last line measures the slope: $\varepsilon(k)/k$ at $k = 10^{-4}$, with the tolerance $10^{-17}$ (smaller than any difference of two numbers near $10^{-4}$, so Newton's method runs until its steps vanish), times $e^{a_{4,0}}$; for the exact band this is 1 at every slice. (The record measured the slope with a Richardson extrapolation from two small momenta, Section 14.19; for the exactly linear band one momentum is enough.)

```python
ax.plot([], [], "-", color="0.4", label="$\\kappa k = k\\,e^{-a_{4,0}}$")
ax.plot([], [], "--", color="0.4", label="first bulk level, same sector")
ax.set_xlabel("3-momentum $k$ (units of $m$)")
ax.set_ylabel("level $\\varepsilon$ (units of $m$)")
ax.set_title("The fold band redshifts, the bulk levels rise")
ax.legend(fontsize=8)
save_figure(fig, "fold_band",
            "The fold-band level $\\varepsilon(k)$ (dots, by shooting; vertical axis, "
...)
```

Two legend entries for the line styles, the labels and the title, and `save_figure` saves Figure 15e.4. In the figure every dot lies on its line, each line is the previous one with the momentum axis stretched by $e = 2.718$, and the dashed bulk levels move up along the history at small $k$.

```python
rescale = 0.0
for a4 in (0.5, 1.0, 2.0):
    partner_grid = make_grid(900, hidden_scale(a4) * L)  # slice 0, length f0 L
    for k in (0.25, 1.0, 2.5):
        for parity, label in (("even", 1), ("odd", 0)):
            guess = math.hypot(exact_level(parity, label, hidden_scale(a4)),
                               k * math.exp(-a4))
            level = find_level(k, 1, parity, label, a4, FREE_MASS, FREE_POT, guess)
            partner = find_level(k * math.exp(-a4), 1, parity, label, 0.0, FREE_MASS,
                                 FREE_POT, level, grid=partner_grid)
            rescale = max(rescale, abs(level - partner))
```

The rescaling identity of Section 15.4 without interaction, $\varepsilon(k, a_{4,0}; L) = \varepsilon(k\,e^{-a_{4,0}}, 0; fL)$, for three slices, three momenta and two levels off the band (the even level of label 1 and the odd level of label 0). `partner_grid` is a grid of 900 steps on the shorter interval $[-fL, 0]$ at the slice 0. For each case the level at the slice $a_{4,0}$ on the canonical grid and the partner level at the slice 0 with the redshifted momentum on the short grid are found, and the largest difference is kept. (The fold band itself obeys the identity trivially, because it is $\kappa k$ on both sides.)

```python
report("largest |fold-band level - kappa k| (123 levels)", f"{worst_band:.1e}")
report("slope c times e^{a4,0} at a4,0 = 0, 1, 2",
       ", ".join(f"{s:.12f}" for s in slopes))
report("bulk level at k = 0 for a4,0 = 0, 1, 2",
       ", ".join(f"{bulk(0.0, a4):.6f}" for a4 in (0.0, 1.0, 2.0)))
report("largest violation of the rescaling identity", f"{rescale:.1e}")
check(worst_band < 1e-12, "the fold band is eps = kappa k = k e^{-a4,0} within 1e-12",
      record="Revision/kohn_sham/ks-theory.json, boundaryConditions.tip")
check(max(abs(s - C_RECORD) for s in slopes) < 1e-9 * C_RECORD,
      "the fold-band slope is c e^{-a4,0} with c = 1",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "free_brane_band_slope")
check(rescale < 1e-12, "eps(k, a4,0; L) = eps(k e^{-a4,0}, 0; f0 L) within 1e-12",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "free_rescaling_relation_and_band_monotone")
```

Out [9] prints the largest deviation of the 123 band levels (three slices times 41 momenta) from $\kappa k$, $1.1 \times 10^{-16}$, a rounding error; the three slopes times $e^{a_{4,0}}$, each $1.000000000000$; the first even bulk level at $k = 0$, $1.447972$, $1.770856$ and $2.271612$ at the slices 0, 1, 2, which rises because $fL$ shrinks; and the largest violation of the rescaling identity, $7.5 \times 10^{-14}$, the difference of two integrations on different grids of the same length in units of the proper hidden coordinate. All three checks pass.

**In [10], the self-consistent loop.**

```python
POINTS = GRID["points"]
```

`POINTS` is 1801, the number of fine points.

```python
def iteration(x, lam, a4, guesses):
    mass = (MASS + x[:POINTS]).tolist()
    pot = x[POINTS:].tolist()
    p_factor = 1.0 / (E3 * vol7(a4))  # P = e^{-3Hy}/Vol_7 on the fine grid
    n = np.zeros(POINTS)
    s = np.zeros(POINTS)
    levels = {}
```

`iteration` performs one Kohn-Sham iteration for $N = 8$ at the slice `a4`. The input `x` is the array of the $2 \times 1801$ unknowns: its first half (`x[:POINTS]`) is $M - m$ and its second half (`x[POINTS:]`) is $v$; they become the lists `mass` and `pot` that `shoot` expects (`.tolist()`). `p_factor` is the array of $P = e^{-3Hy}/\mathrm{Vol}_7(a_{4,0})$ at the fine points (Section 15.2). The densities $n$ and $S$ start at zero, and `levels` will hold the two occupied levels.

```python
    for j in (1, -1):  # the two block types, each level four-fold (g = 4)
        eps = find_level(0.0, j, "even", 0, a4, mass, pot, guesses.get(j, 0.0))
        a, b = orbital(eps, 0.0, j, a4, mass, pot)
        weight = 0.5 * 4.0 * 1.0  # w g f with w = 1/2 (each half holds N/2)
        n += weight * p_factor * (a * a + b * b)
        s += weight * p_factor * j * 2.0 * a * b
        levels[j] = eps
```

For each block type the occupied level is the zero mode: $k = 0$, even fold condition, label 0. Its energy is found starting from the previous iteration's energy (`guesses.get(j, 0.0)` gives 0 in the first iteration, when `guesses` is empty), and its orbital is computed. The weight $wgf_o = \tfrac12\cdot4\cdot1 = 2$ multiplies the orbital densities $P(a^2 + b^2)$ and $P\,j\,2ab$, which are added to $n$ and $S$ (the formulas of Section 15.2; $w = \tfrac12$ because each orbital is normalised on one half of the cell and $N$ counts both halves).

```python
    x_out = np.concatenate([lam * (15.0 / 16.0) * s, lam * (-1.0 / 16.0) * n])
    e_int = lam * (15.0 / 32.0 * s * s - 1.0 / 32.0 * n * n)
    energy = sum(4.0 * e for e in levels.values()) \
        - 2.0 * vol7(a4) * float(np.sum(GRID["simpson"] * E3 * e_int))
    return float(np.max(np.abs(x_out - x))), x_out, energy, levels
```

The output potentials are $\tfrac{15}{16}\lambda S$ and $-\tfrac{1}{16}\lambda n$, joined into one array (`np.concatenate`). `e_int` is the interaction energy density, and `energy` is $E_{KS} = \sum gf_o\varepsilon - 2\,\mathrm{Vol}_7\int e^{3Hy}e_{int}\,dy$ with $g f_o = 4$ for each of the two levels and Simpson's rule for the integral; the backslash at the end of a line continues the statement on the next line. The function returns the size of the residual (the largest $|x_{out} - x|$), the output potentials, the energy and the levels.

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

`solve_n8` runs the loop for the coupling `lam` at the slice `a4` (the first slice when not given). It starts from the free potentials ($x = 0$), makes a new `Anderson` object, and repeats at most 200 iterations: one iteration, its levels as the next guesses, its number, residual and energy appended to `history`; if the residual is at most $10^{-11}$, the energy, levels, history and potentials are returned; otherwise the next input is made by Anderson mixing or, if `mixing` is `"linear"`, by linear mixing $x + 0.4\,r$. If the loop never converges, a `RuntimeError` stops the notebook. The cell defines functions and the class only and prints nothing.

**In [11], the state $N = 8$ with $+\lambda_1$.**

```python
params = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                    .read_text(encoding="utf-8"))
calib = {int(c["N"]): c for c in params["couplingCalibration"]["values"]}
LAM1, LAM2 = calib[8]["lambda1"], calib[8]["lambda2"]
```

The parameters file of the record is read; `calib` is a **dictionary comprehension** that files the calibration entries under their particle number (8, 592, 2352), and `LAM1`, `LAM2` are the couplings $\lambda_1 = 157.7$ and $\lambda_2 = 473.1$ of $N = 8$ (Section 15.2).

```python
energy, levels, history, x_final = solve_n8(LAM1)
say("iteration   residual        E_KS")
for it, residual, e in history:
    say(f"{it:9d}   {residual:9.3e}   {e:.13e}")
```

The loop is run with $+\lambda_1$ at the first slice and its history is printed, one line per iteration: the iteration number, the residual and the energy. Out [11] shows the residual falling from $0.1$ in the first iteration (the first-order potential, as calibrated) to $9.2 \times 10^{-12}$ in the seventeenth, and the energy settling at $-3.7786682917046 \times 10^{-2}$.

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
report("lambda_1 and lambda_2 of N = 8", f"{LAM1} and {LAM2}")
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

The cell reports the couplings $157.7$ and $473.1$, $E_{KS} = -3.778668291704577 \times 10^{-2}$, 17 iterations here and in the record, and the relative difference $4.7 \times 10^{-10}$ of the first six residuals (the later residuals are differences of nearly equal numbers and depend on the order of the arithmetic, as the text cell explains). The three checks pass: the energy and the occupied level (HOMO) agree with the record within $10^{-14}$ and $10^{-13}$, the early residuals within $10^{-5}$, and the levels of the two block types are equal, as the symmetry $\sigma_3 h_j(k)\sigma_3 = h_{-j}(-k)$ demands at $k = 0$.

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
ratio = len(history_lin) / len(history)  # how many times more iterations
save_figure(fig, "scf_mixing",
            "Residual of the self-consistent loop (vertical axis, logarithmic, units "
...)
report("iterations: Anderson / linear", f"{len(history)} / {len(history_lin)}")
report("|E(linear) - E(Anderson)|", f"{abs(energy_lin - energy):.1e}")
check(abs(energy_lin - energy) < 1e-10 and len(history_lin) > 2 * len(history),
      "linear mixing reaches the same energy within 1e-10, with more than twice the "
      "iterations")
```

`ratio` is the number of linear iterations divided by the number of Anderson iterations; the caption prints it with one decimal (2.9). `save_figure` saves Figure 15e.5. Out [12] reports 17 iterations for Anderson mixing and 49 for linear mixing, and an energy difference of $4.7 \times 10^{-12}$: both reach the same state, linear mixing with about three times the work. The check passes. In the figure the black crosses of the Rust solver sit on the blue dots.

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
    say(f"{tag}: lambda {lam:+.1f}, E_KS {e:+.12e}, HOMO {lv[1]:+.12e},"
        f" {len(hist)} it.")
```

The dictionary `tags` maps the four run tags to the couplings $\pm\lambda_1$, $\pm\lambda_2$. For each, the loop is solved, the energy, the level of $j = +1$ and the final potentials are kept in `results`, the differences to the record's row (for example `N8_lamm1_a00`) are tracked, and a line is printed; the format `+.1f` always prints the sign. Out [13] shows that $E_{KS}$ and the HOMO of $-\lambda$ are exactly the negatives of those of $+\lambda$: $\mp3.778668291705 \times 10^{-2}$ and $\mp9.410183270701 \times 10^{-3}$ for $\pm\lambda_1$ (17 iterations), $\mp1.109816005304 \times 10^{-1}$ and $\mp2.726254801520 \times 10^{-2}$ for $\pm\lambda_2$ (23 iterations).

```python
xf = results["lamp1"][2]
lumo = find_level(0.25, 1, "even", 0, 0.0, (MASS + xf[:POINTS]).tolist(),
                  xf[POINTS:].tolist(), 0.24)
report("LUMO of N8_lamp1_a00 (fold band at k = 0.25)", f"{lumo:.13f}")
antisym = max(abs(results["lamp1"][0] + results["lamm1"][0]),
              abs(results["lamp2"][0] + results["lamm2"][0]))
report("largest |E(+lambda) + E(-lambda)|", f"{antisym:.1e}")
```

The lowest empty level of the state with $+\lambda_1$ is the fold-band level of the first shell, $k = 0.25$, in the converged potentials; it is found with the guess 0.24 (just below the free gap 0.25). `antisym` is the larger of $|E(+\lambda_1) + E(-\lambda_1)|$ and $|E(+\lambda_2) + E(-\lambda_2)|$. Out [13] prints the LUMO $0.2405774163373$ (the repulsive potential $v < 0$ lowers the band level from 0.25) and the value 0.0.

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

The axis labels and titles, and `save_figure` for Figure 15e.6. The student should see the potential $v = -\lambda n/16$ grow toward the tip roughly like $e^{-y}$: the zero mode is $e^{fMy} = e^{y}$ at the first slice, so its density per unit $y$ is $e^{2y}$, and dividing by the proper volume factor $e^{3Hy} = e^{3y}$ gives $e^{-y}$, the growth $e^{(3H - 2fm)|y|}$ of Section 15.2. This growth toward the tip, stronger at the later slices where $f$ is smaller, is why the interacting $N = 8$ results depend on the cutoff $L$ (Section 15.2, the paragraph on the cutoff). The mass shift is smaller, because the scalar densities of the zero modes of the two block types cancel without interaction ($b = 0$) and are created only by the interaction itself.

```python
plus, minus = results["lamp1"][2], results["lamm1"][2]  # potentials x of +-lambda_1
mirror = max(float(np.max(np.abs(plus[:POINTS] - minus[:POINTS]))),
             float(np.max(np.abs(plus[POINTS:] + minus[POINTS:]))))
report("largest violation of the potential symmetry", f"{mirror:.1e}")
check(mirror < 1e-12, "M - m is even and v is odd under lambda -> -lambda")
```

The symmetry of Section 15.5 predicts that $M - m$ is the same for $\pm\lambda$ and $v$ changes sign. The variable `mirror` (a name for this reflection $\lambda \to -\lambda$ of the coupling, nothing else) is the larger of the largest $|(M - m)_+ - (M - m)_-|$ and the largest $|v_+ + v_-|$. Out [14] prints 0.0 and PASS; in the figure the dashed curves of the mass shift lie on the solid ones.

**In [15], the last check.**

```python
NAMES = ["phase_function", "orbitals", "rk4_convergence", "fold_band", "scf_mixing",
         "n8_potentials"]
missing = [name for number, name in enumerate(NAMES, start=1)
           if not output_file(f"{FIGURE_FOLDER}/15e_{number}_{name}.png").is_file()]
check(missing == [], "every figure file of this notebook exists")
all_checks_passed()
```

`NAMES` lists the six figure names in order. `enumerate(NAMES, start=1)` pairs each name with its number 1, 2, ...; the list comprehension with `if not ...` collects the names whose file does not exist. The check requires that list to be empty, and `all_checks_passed()` prints the last line, ALL 19 CHECKS PASSED (notebook 15e).

### 15.10 The Rust solver and its canonical matrix

Notebook 15e showed the method on the smallest state. The Revision record computes every state of the canonical matrix with a compiled program, the **Rust solver** `revision_ks_solver`, whose source is the folder `Revision/kohn_sham/solver` of the repository. Rust is a programming language whose programs are translated once into machine code by its tool cargo and then run much faster than Python; the solver needs no packages from outside the repository, so cargo downloads nothing.

**What is in the program.** The source is split into modules, one file each in `Revision/kohn_sham/solver/src`:

- `theory.rs` reads the theory file `Revision/kohn_sham/ks-theory.json` and the gamma matrices `Revision/algebra/gammas.json` and checks again, in floating point, that the block basis of Chapter 14 really makes every operator of the problem block diagonal (check block_reduction_numeric) and that the metric forms of the theory file are those of the corrected metric (check theory_input_metric_forms);
- `shoot.rs` holds the shooting with the Pruefer angle and the safeguarded Newton root of Section 15.3, with the hidden scale $f$ and the momentum weight $\kappa$ of the slice;
- `scf.rs` holds the label sets, the aufbau, the densities and the self-consistent loop with Anderson mixing of Sections 15.4 and 15.5;
- `mermin.rs` finds the chemical potential at a temperature (Section 15.26);
- `analysis.rs` computes the energy-momentum tensor, its identities, the adiabaticity measure and the particle-hole lists;
- `spectrum.rs` computes the free spectra and their exact checks;
- `runs.rs` runs the canonical matrix, `cache.rs` lets it run in parts;
- `json.rs`, `sha256.rs`, `report.rs` and `model.rs` write the results deterministically, compute fingerprints, collect the checks and hold the parameters.

**The ways to run it.** The command `revision_ks_solver all` computes the whole canonical matrix of Section 15.2 and writes it into a folder of results. For each of the 75 ground states it solves the state itself, the same state at the four neighbouring slices $a_{4,0} \pm \delta$ and $a_{4,0} \pm 2\delta$ with $\delta = 0.002$ (for the derivatives along the history; there $\kappa$, $f$ and $\mathrm{Vol}_7$ all change), the first excited state (Delta-SCF), the partner state of the rescaling identity (for the 60 states with $a_{4,0} > 0$), and the variant with the exact Fock exchange (for the 60 states with $\hat\lambda \ne 0$); for each of the 135 thermal states it solves the state and its four neighbours at the temperatures $T \pm 0.01T$ and $T \pm 0.02T$ (for the temperature derivatives). It then evaluates its 45 checks, prints each as a line PASS - name or FAIL - name on its error stream, writes them into a report, and prints SUCCESS or FAILURE as the last line of its output stream. The whole matrix took 284.5 s with 22 threads on the computer of the record (`Revision/kohn_sham/solver/README.md`, Timings), so the record computes it in parts with a cache of finished states; the parts give byte for byte the same files. The option `quick` (written in a command, like every option, with two hyphens in front of its name) selects the **quick matrix**: $N = 8$ and $592$, the couplings $0, \pm\lambda_1$, the slices $0, 1, 2$ (18 ground states, each with its neighbours, excited state, partner and variant) and the thermal states of these $N$ and couplings at the slices 0 and 2 and $T = 0.02$ (12 states), chosen so that every part of the program runs; it has the checks of the whole matrix except the one of the crossing demonstration (Section 15.21). The command `revision_ks_solver single` solves one state with chosen parameters ($m$, $\hat\lambda$, $a_{4,0}$, $N$ and, if wanted, $T$) and writes its levels, energies and energy-momentum integrals as a JSON file and, if wanted, its profiles as a CSV file; Notebooks 15b and 15d use it.

**The results.** The folder `Revision/kohn_sham/results` holds the canonical matrix: `parameters.json` (all parameters, the conventions and the calibration of Section 15.2), `manifest.json` (the list of every result file with its sha256 fingerprint, a 64-digit number computed from the bytes of a file, so that two files with the same fingerprint are identical; 243 files), `spectrum/` (the free spectra), `ground/` (the 75 ground states: a summary table, the history of every self-consistent loop, the level tables, the profiles of the densities and the energy-momentum tensor at the 151 points $y = -3, -2.98, \dots, 0$, and the integrals of the tensor), `excited/` (Delta-SCF and the particle-hole excitations), `adiabatic/` (Section 15.21), `rescaling/`, `exx/` (the exact-Fock variant) and `thermo/` (the 135 thermal states). Every number is written with 16 significant digits and no time stamp or path, so that a second run writes the same bytes. (Some file and key names still say "brane", from an earlier construction of the record: `spectrum/brane-band.csv` is the fold band, and the check brane_band_slope its slope.)

**How the record checks itself.** Three reports belong to the solver. `Revision/kohn_sham/reports/ks-rust-solver.json` holds the 45 checks of the run itself, all PASS: the theory input, the free spectra (exact levels, zero mode, fold-band slope, block symmetries, labels, tip angle, rescaling), every state (convergence, particle number, boundary conditions, the two energy forms, the energy-momentum identities, closed shells, completeness of the label sets), the derivatives along the history, the excited states, the exact-Fock variant, the thermodynamics and the chemical potential. `Revision/kohn_sham/reports/ks-rust-determinism.json` (14 checks, all PASS) compares a second run with the canonical one (all 244 files, the 243 result files and the manifest, byte-identical; check repeat_byte_identical) and a **refined run** with twice the RK4 steps and smaller tolerances (root tolerance $10^{-14}$, self-consistency tolerance $10^{-14}$), against tolerances fixed before the comparison ($10^{-8}$ for levels, energies and thermodynamics, $10^{-6}$ for profiles and derived quantities): $E_{KS}$ agrees to $1.73 \times 10^{-11}$ relative (check refined_ground_energies) and 50420 levels agree label by label to $5.7 \times 10^{-10}\,m$ (check refined_eigenvalues). `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` compares every chemical potential with a 40-digit root (Section 15.26). An independent cross-check by a second program written in Python is the subject of Chapter 16.

**Threads.** The solver distributes independent states over the processor cores (at most 22 threads) and the sectors of one state over a few more, and merges the results in a fixed order, so the number of threads does not change any output byte.

### 15.11 Example: running the quick matrix (Notebook 15a)

Notebook 15a builds the solver with cargo on the student's computer, runs `revision_ks_solver all` with the option quick into a folder that git ignores, and checks the new run against the committed record in three ways: the solver's own checks of the quick matrix (44 of the 45 of the record) must all pass and come in the record's order; every result file of the quick run must be a file of the record (on the computer that built the book 14 of the 72 are byte-identical; the tables of the whole matrix cannot be, because they list fewer states); and the key numbers must agree within the tolerances that the record fixed in advance. Then it reads the committed canonical matrix and draws eight figures: the levels of $N = 592$ along the history (Figure 15a.1), the gaps (Figure 15a.2), the orbital relaxation of Delta-SCF (Figure 15a.3), the total energies and the interaction shifts (Figure 15a.4), the densities (Figure 15a.5), the self-consistent potentials (Figure 15a.6), the convergence of the self-consistent loop (Figure 15a.7) and the particle-hole excitations (Figure 15a.8). It needs Rust (the run instructions below explain how to install it), takes a few minutes (about five on the computer with two cores that built this book, Section 15.1), and ends with ALL 28 CHECKS PASSED (notebook 15a).

What to look for: in Figure 15a.1 the blue fold-band levels that fall from slice to slice exactly along the dashed line, while the black levels at $k = 0$ rise; in Figure 15a.2 the gaps of $N = 8$ and $592$ exactly on their dashed lines $e^{-a_{4,0}}$, and the gap of $N = 2352$ that joins its line from the second slice on; in Figure 15a.5 that the particles sit near the fold although the proper density is largest at the tip.

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

**In [3], running the quick matrix.**

```python
RUN_FOLDER = REPO / "Revision/kohn_sham/solver/target/textbook_15a"  # git ignores it
NEW_RESULTS = RUN_FOLDER / "results"  # the new quick matrix
NEW_REPORT = RUN_FOLDER / "ks-rust-solver-quick.json"  # its check report
RUN_FOLDER.mkdir(parents=True, exist_ok=True)
if NEW_RESULTS.exists() and not (NEW_RESULTS / "manifest.json").exists():
    shutil.rmtree(NEW_RESULTS)  # remains of an interrupted run
```

The new run is written into the folder `textbook_15a` inside the solver's build folder `target`, which git ignores; the committed record is never touched. The folder is created if necessary. If a results folder exists without its `manifest.json`, an earlier run was interrupted, and the solver would refuse to write into it; `shutil.rmtree` removes it.

```python
completed = subprocess.run(
    [str(program), "all", "--quick", "--root", str(REPO), "--out", str(NEW_RESULTS),
     "--report", str(NEW_REPORT)],
    capture_output=True, text=True, encoding="utf-8", errors="replace")
stdout_lines = completed.stdout.strip().split("\n")  # what it printed on stdout
stderr_lines = completed.stderr.split("\n")  # its check lines and progress lines
```

The solver runs the command `all` with the option quick (Section 15.10: 18 ground states and 12 thermal states). The option root tells it where the repository is (it reads the theory file, the gamma matrices and the fixture of 40-digit chemical potentials from there), and the options out and report name the folder of the results and the file of the check report. This is the longest step of the notebook. The printed text is split into lines: `.strip()` removes the blank space at the ends, `.split("\n")` cuts at the line ends.

```python
pass_count = sum(1 for line in stderr_lines if line.startswith("PASS - "))
fail_count = sum(1 for line in stderr_lines if line.startswith("FAIL - "))
say(f"exit code {completed.returncode}, last line {stdout_lines[-1]!r}, "
    f"{pass_count} PASS lines, {fail_count} FAIL lines")
check(completed.returncode == 0 and stdout_lines[-1] == "SUCCESS" and fail_count == 0,
      "the solver ran the quick matrix and reported SUCCESS")
```

`sum(1 for line in ... if ...)` counts the lines that start with PASS - and with FAIL -. The format `!r` prints the last output line with quotes. Out [3] prints exit code 0, the last line SUCCESS, 44 PASS lines and 0 FAIL lines, and the check passes.

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

The new report and the committed one are read. Each check has a name, a verdict and a detail; the first word of the name (the text before the first underscore) is its group. For each group the cell counts the checks and the passed ones (a comparison gives `True` or `False`, which count as 1 and 0 when added). Out [4] lists the twelve groups, for example free with 7 checks and thermo with 12, all passed.

```python
new_names = [item["name"] for item in new_report["checks"]]
old_names = [item["name"] for item in old_report["checks"]]
left_out = [name for name in old_names if name not in new_names]
summary = new_report["summary"]  # {"checks": ..., "pass": ..., "fail": ...}
report("checks in the new report / PASS / FAIL",
       f"{summary['checks']} / {summary['pass']} / {summary['fail']}")
report("checks in the record / PASS", f"{old_report['summary']['checks']} / "
       f"{old_report['summary']['pass']}")
report("checks of the record that the quick matrix leaves out", ", ".join(left_out))
```

The lists of check names of the two reports are formed, and `left_out` collects the names of the record that the new report does not have. Out [4] reports 44 checks in the new report, 44 PASS and 0 FAIL; 45 checks in the record, all PASS; and the one check left out, adiabatic_crossing_flag_demonstration, which belongs to the crossing demonstration (Section 15.21) that the quick matrix does not compute.

```python
check(summary["fail"] == 0 and summary["pass"] == summary["checks"] == len(new_names)
      and old_report["summary"]["fail"] == 0,
      f"the new report holds {summary['checks']} checks, all PASS",
      record=f"{RECORD_REPORT}, summary")
check(left_out == ["adiabatic_crossing_flag_demonstration"]
      and new_names == [name for name in old_names if name != left_out[0]],
      "the new report has the checks of the record except the crossing demonstration")
```

The first check requires no failure in either report and as many passes as checks; the number 44 is not typed into the notebook but read from the report. The second requires that exactly the crossing demonstration is left out and that the other names come in the same order as in the record. Both pass.

**In [5], every result file.**

```python
RECORD_RESULTS = "Revision/kohn_sham/results"


def manifest_of(folder):
    data = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    return {entry["path"]: entry["sha256"] for entry in data["files"]}


old_manifest = manifest_of(repository_file(RECORD_RESULTS))
new_manifest = manifest_of(NEW_RESULTS)
check(set(new_manifest) <= set(old_manifest),
      f"each of the {len(new_manifest)} result files of the quick run is a file of the "
      f"record ({len(old_manifest)} files)", record=f"{RECORD_RESULTS}/manifest.json")
same = sum(1 for path in new_manifest if new_manifest[path] == old_manifest[path])
report("result files byte-identical to the record", f"{same} of {len(new_manifest)}")
```

`manifest_of` reads a manifest and returns a dictionary from each file path to its sha256 fingerprint. `set(...)` makes the set of the paths, and `<=` between two sets asks whether the first is contained in the second: every file of the quick run must be a file of the record. `same` counts the files whose fingerprints agree. Out [5]: each of the 72 result files of the quick run is one of the 243 files of the record, and 14 of the 72 are byte-identical to the record on the computer that built the book. The others cannot be: the tables of the whole matrix (such as `ground/summary.csv`) list fewer states in a quick run, and a few single-state files differ in the last digit of some numbers on a computer whose mathematical library rounds differently from the one that made the record (the text cell before In [6] explains this).

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
    assert set(new) <= set(old), f"{table}: a state of the quick run is not recorded"
    largest = 0.0
    for key in new:
        for column in columns:
            a, b = float(new[key][column]), float(old[key][column])
            scale = max(abs(b), 1.0) if relative else 1.0
            largest = max(largest, abs(a - b) / scale)
    return largest, len(new)
```

`worst` returns the largest difference between the new run and the record in the given columns of a table, over the states of the quick run, and the number of these states. The `assert` statement stops with the given message if the quick run has a state that the record does not have (a safety net inside a helper, not one of the notebook's checks). For a relative comparison each difference is divided by the larger of $|b|$ and 1, so that numbers near zero are compared absolutely.

```python
COMPARISONS = [  # (table, columns, relative?, tolerance, what)
    ("ground/summary.csv", ["E_KS"], True, 1e-8, "ground-state energies"),
    ("ground/summary.csv", ["HOMO", "LUMO", "KS_gap"], False, 1e-8,
     "HOMO, LUMO and gaps"),
    ("excited/summary.csv", ["delta_SCF"], False, 1e-8, "Delta-SCF energies"),
    ("ground/emt-integrals.csv", ["int_rho", "int_p3", "int_p_t", "int_p0"], True,
     1e-6, "integrated energy-momentum tensor"),
    ("thermo/thermodynamics.csv", ["mu", "E", "entropy", "F"], True, 1e-8,
     "thermodynamics"),
    ("adiabatic/adiabaticity.csv", ["Q_max"], True, 1e-6, "adiabaticity Q_max"),
]
for table, columns, relative, tolerance, what in COMPARISONS:
    largest, states = worst(table, columns, relative)
    report(f"largest difference, {what} ({states} states)", f"{largest:.1e}")
    check(largest <= tolerance, f"{what} agree with the record within {tolerance:.0e}",
          record=f"{RECORD_RESULTS}/{table}")
```

`COMPARISONS` lists six comparisons, each a tuple (a fixed group of values in parentheses): the table, its columns, whether the comparison is relative, the tolerance (the values fixed in advance in `Revision/kohn_sham/reports/ks-rust-determinism.json`) and a description. The loop unpacks each tuple into five names, computes the largest difference, reports it and checks it. Out [6] reports, for the 18 ground states and the 12 thermal states, $1.6 \times 10^{-13}$ (energies), $7.3 \times 10^{-14}$ (HOMO, LUMO, gaps), $2.9 \times 10^{-11}$ (Delta-SCF), $6.2 \times 10^{-13}$ (integrated tensor), $7.5 \times 10^{-13}$ (thermodynamics) and $3.5 \times 10^{-12}$ ($Q_{max}$), and six PASS lines: the new numbers agree with the record far inside the tolerances. These are the differences of the mathematical libraries of two computers, amplified by the self-consistent loop; the record's own refined run (Section 15.10) measures the far larger error of the method itself.

**In [7], the ground states along the history.**

```python
RECORD = repository_file(RECORD_RESULTS)  # the folder of the committed matrix
ground = read_table(RECORD, "ground/summary.csv")  # the 75 ground states
excited = read_table(RECORD, "excited/summary.csv")  # their Delta-SCF


def state_id(n, tag, a4):
    return f"N{n}_{tag}_a{round(10 * a4):02d}"
```

From here on the notebook reads the committed canonical matrix (the quick run reproduced the part of it that it computed). `state_id` builds the solver's name of a state: `round(10 * a4)` is ten times the slice as a whole number, and the format `02d` writes it with two digits, so $N = 592$, `lam0`, $a_{4,0} = 1$ gives `N592_lam0_a10`.

```python
say("   N  a4,0        E_KS        HOMO        LUMO      KS gap")
for n in (8, 592, 2352):
    for a4 in SLICES:
        row = ground[state_id(n, "lam0", a4)]
        say(f"{n:4d}  {a4:4.1f}  {float(row['E_KS']):10.4f}  {float(row['HOMO']):10.6f}"
            f"  {float(row['LUMO']):10.6f}  {float(row['KS_gap']):10.7f}")
```

For the three particle numbers without interaction and the five slices the cell prints a table of $E_{KS}$, the HOMO, the LUMO and the gap. Out [7] is the table of Section 15.15. For $N = 8$ the energy is exactly 0 at every slice (the zero modes have $\varepsilon = 0$ and there is no interaction).

```python
gap8 = [float(ground[state_id(8, "lam0", a)]["KS_gap"]) for a in SLICES]
report("KS gap of N = 8 at a4,0 = 0, 1, 2",
       ", ".join(f"{gap8[i]:.7f}" for i in (0, 2, 4)))
redshift = max(abs(float(ground[state_id(n, "lam0", a)]["E_KS"]) * math.exp(a)
                   / float(ground[state_id(n, "lam0", 0.0)]["E_KS"]) - 1.0)
               for n in (592, 2352) for a in SLICES)
report("largest |E_KS(a4,0) e^{a4,0} / E_KS(0) - 1|, N = 592 and 2352",
       f"{redshift:.1e}")
```

`gap8` holds the gaps of $N = 8$ at the five slices, and the report prints those at $a_{4,0} = 0, 1, 2$ (the list positions 0, 2, 4). `redshift` measures how exactly the free energies of $N = 592$ and $2352$ fall like $e^{-a_{4,0}}$: if $E_{KS}(a_{4,0}) = E_{KS}(0)\,e^{-a_{4,0}}$, then $E_{KS}(a_{4,0})\,e^{a_{4,0}}/E_{KS}(0) - 1 = 0$. Out [7] reports the gaps $0.2500000$, $0.0919699$, $0.0338338$ and the largest deviation $2.2 \times 10^{-16}$, a rounding error.

```python
check(max(abs(g - 0.25 * math.exp(-a)) for g, a in zip(gap8, SLICES)) < 1e-12,
      "the gap of N = 8 is 0.25 e^{-a4,0} at every slice",
      record=f"{RECORD_RESULTS}/ground/summary.csv, column KS_gap")
check(redshift < 1e-12, "the free energies of N = 592 and 2352 fall like e^{-a4,0}",
      record=f"{RECORD_RESULTS}/ground/summary.csv, column E_KS")
```

The two exact consequences of the fold band (Section 15.4): the gap of $N = 8$ is $\kappa\Delta k = 0.25\,e^{-a_{4,0}}$, and the free energies of $N = 592$ and $2352$, sums of fold-band levels $\kappa k$ only, scale with $\kappa = e^{-a_{4,0}}$. Both checks pass.

**In [8], the levels along the history.**

```python
def read_levels(n, tag, a4):
    path = RECORD / "ground/levels" / f"{state_id(n, tag, a4)}.csv"
    with open(path, newline="", encoding="utf-8") as handle:
        return {(int(r["n2"]), int(r["j"]), r["parity"], int(r["label"])):
                (float(r["eps"]), float(r["f"]), float(r["k"]))
                for r in csv.DictReader(handle)}
```

`read_levels` reads the level table of one state and returns a dictionary whose key is the **key** of a level, the four entries (shell $n_2$, block type $j$, fold condition, Pruefer label $l$; the fold condition is the column `parity`), and whose value is the triple (level, occupation, momentum $k$).

```python
levels = [read_levels(592, "lam0", a4) for a4 in SLICES]  # one dictionary per slice
fig, ax = plt.subplots(figsize=(7.5, 5.0))
all_keys = sorted(set().union(*levels))
```

`levels` holds the level tables of $N = 592$, $\lambda = 0$ at the five slices. `set().union(*levels)` is the set of all keys that occur at any slice (a **set** is a collection without repetitions), sorted into a list.

```python
for key in all_keys:
    points = [(a4, lv[key]) for a4, lv in zip(SLICES, levels) if key in lv]
    xs = [p[0] for p in points]
    es = [p[1][0] for p in points]
    if min(es) > 2.4:
        continue  # only the part of the spectrum near the Fermi level
    band = key[1] == 1 and key[2] == "even" and key[3] == 0 and key[0] >= 1
    colour = PALETTE[0] if band else ("black" if key[0] == 0 else "0.6")
    ax.plot(xs, es, "-", color=colour, lw=1.0, alpha=0.8)
    for x, (e, f, _) in points:
        ax.plot([x], [e], "o", ms=5, color=colour,
                markerfacecolor=colour if f > 0.5 else "white")
```

For each key the cell collects the slices at which the level exists (the label sets differ from slice to slice) with its triple. Levels that stay above $2.4\,m$ are skipped (`continue` jumps to the next key). A key belongs to the fold band if it is $j = +1$, even fold condition, label 0 and $n_2 \ge 1$; band levels are drawn blue, levels at $k = 0$ black and all others grey. Each level is drawn as a thin line through its points, and each point as a dot that is filled when the level is occupied ($f > 0.5$) and open (white inside) when it is empty; the underscore receives the momentum, which is not needed here.

```python
a_fine = np.linspace(0.0, 2.0, 101)
ax.plot(a_fine, 0.25 * np.exp(-a_fine), "--", color=PALETTE[1], lw=1.5,
        label="$\\kappa k = k\\,e^{-a_{4,0}}$ for $k = 0.25$")
ax.plot([], [], "o-", color=PALETTE[0], label="fold band ($j=+1$, even, $l=0$)")
ax.plot([], [], "o-", color="black", label="levels at $k = 0$")
ax.plot([], [], "o-", color="0.6", label="other levels")
ax.plot([], [], "o", color="0.3", markerfacecolor="white", label="open: empty")
ax.set_ylim(-0.05, 2.4)
ax.set_xlabel("slice $a_{4,0}$ of the history")
ax.set_ylabel("level $\\varepsilon$ (units of $m$)")
ax.set_title("Kohn-Sham levels of $N = 592$, $\\lambda = 0$, along the history")
ax.legend(fontsize=8, loc="upper right")
save_figure(fig, "levels_history",
            "Kohn-Sham levels $\\varepsilon$ (vertical axis, units of $m$) of the "
...)
```

`a_fine` holds 101 slices from 0 to 2; the dashed orange curve is the exact band level $\kappa k = 0.25\,e^{-a_{4,0}}$ of the first shell. The empty plots make the legend entries, and the remaining lines set the range, labels and title and save Figure 15a.1.

```python
band_keys = [key for key in all_keys
             if key[1] == 1 and key[2] == "even" and key[3] == 0 and key[0] >= 1]
band_dev = max(abs(lv[key][0] - lv[key][2] * math.exp(-a4))
               for a4, lv in zip(SLICES, levels) for key in band_keys if key in lv)
k0_keys = [key for key in levels[0] if key[0] == 0 and levels[0][key][0] > 0.0]
rising = all(levels[i + 1][key][0] > levels[i][key][0]
             for key in k0_keys for i in range(4) if key in levels[i + 1])
report("fold-band levels followed / largest |eps - k e^{-a4,0}|",
       f"{len(band_keys)} / {band_dev:.1e}")
report("levels at k = 0 above the zero modes, at a4,0 = 0", len(k0_keys))
check(band_dev <= 1e-12, "every fold-band level is k e^{-a4,0}",
      record=f"{RECORD_RESULTS}/ground/levels/N592_lam0_a*.csv")
check(rising, "every level at k = 0 above the zero modes rises along the history")
```

`band_keys` are the fold-band keys, and `band_dev` is the largest difference between a recorded band level and $k\,e^{-a_{4,0}}$, with the recorded momentum $k$ of the level (the third entry of the triple), over every slice at which the key occurs. `k0_keys` are the positive levels at $k = 0$ of the first slice (the zero modes, at exactly 0, are left out), and `rising` is true when each of them is higher at each slice than at the previous one, wherever it is in the label set (`all(...)` is true when every comparison is true). Out [8]: 97 band keys, largest deviation $2.2 \times 10^{-16}$; 10 levels at $k = 0$ above the zero modes; both checks pass. In Figure 15a.1 the blue levels come down exactly along the dashed line of the first shell and its copies, while the black levels move up: the hidden direction shrinks (Section 15.3).

**In [9], the gaps.**

```python
fig, ax = plt.subplots()
for colour, n in zip(PALETTE, (8, 592, 2352)):
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

For each particle number the gaps at the five slices are drawn as dots joined by lines, with a dashed curve $\Delta(0)\,e^{-a_{4,0}}$ through the first point; `set_yscale("log")` makes the vertical axis logarithmic, on which $e^{-a_{4,0}}$ is a straight line. This is Figure 15a.2: the gaps of $N = 8$ and $592$ lie on their lines; the gap of $N = 2352$ lies on a parallel line from the second slice on, above its dashed line: there it is the distance $(0.25\sqrt{27} - 0.25\sqrt{26})\,e^{-a_{4,0}} = 0.024283\,e^{-a_{4,0}}$ of two band levels, larger than the first gap $0.017538$ to the bulk edge.

```python
free_dscf = max(abs(float(excited[state_id(n, "lam0", a)]["delta_SCF_minus_gap"]))
                for n in (8, 592, 2352) for a in SLICES)
report("largest |Delta-SCF - gap| without interaction", f"{free_dscf:.1e}")
check(free_dscf <= 1e-10, "Delta-SCF equals the gap without interaction",
      record=f"{RECORD_REPORT}, check excited_delta_scf_free_equals_gap")
shrinking = all(float(ground[state_id(n, "lam0", SLICES[i + 1])]["KS_gap"])
                < float(ground[state_id(n, "lam0", SLICES[i])]["KS_gap"])
                for n in (8, 592, 2352) for i in range(4))
check(shrinking, "every gap shrinks from slice to slice")
```

`free_dscf` is the largest $|\Delta_{SCF} - \Delta_{KS}|$ of the 15 free states; Out [9] gives $3.1 \times 10^{-13}$, the value of the record's check, below its tolerance $10^{-10}$. The second check confirms that every gap shrinks from slice to slice.

**In [10], the orbital relaxation.**

```python
fig, axes = plt.subplots(1, 3, figsize=(10.0, 3.8), sharey=True,
                         layout="constrained")
for ax, n in zip(axes, (8, 592, 2352)):
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
second = sorted(abs(float(row["delta_SCF_minus_gap"])) for row in excited.values())[-2]
mantissa, power = f"{largest_relax:.1e}".split("e")  # e.g. "6.3", "-04"
save_figure(fig, "delta_scf",
            "Orbital relaxation: the Delta-SCF excitation energy minus the Kohn-Sham "
...)
```

`max(excited, key=...)` returns the state name whose relaxation has the largest size, and `second` is the second largest size (`sorted(...)[-2]`, the last but one of the sorted sizes). The largest number is written in the format `.1e` and split at the letter e into the digits and the power of ten, which the caption of Figure 15a.3 prints as $6.3 \times 10^{-4}$ (so the caption's number is computed, not typed).

```python
report("largest |Delta-SCF - gap| over the 75 states",
       f"{largest_relax:.3e} ({largest_id})")
report("second largest |Delta-SCF - gap|", f"{second:.1e}")
check(largest_id == "N2352_lamp1_a00"
      and excited[largest_id]["particle_levels"] == "0:-1:odd:0;0:+1:odd:0",
      "the largest relaxation belongs to N = 2352, +lambda_1, a4,0 = 0 (the caption)")
check(largest_relax < 1e-3, "the orbital relaxation is below 0.001 m in every state")
```

Out [10]: the largest relaxation is $6.286 \times 10^{-4}\,m$, in `N2352_lamp1_a00`, and the second largest only $2.1 \times 10^{-7}\,m$. The first check confirms what the caption says: in that state the excited particle goes into the odd levels of label 0 at $k = 0$ of both block types (the bulk edge, written `0:-1:odd:0;0:+1:odd:0`), whose orbital fills the whole interval and changes the mean field more than a fold-band orbital does. Every relaxation is below $0.001\,m$.

**In [11], the total energy.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
for colour, n in zip(PALETTE, (592, 2352)):
    energies = [float(ground[state_id(n, "lam0", a)]["E_KS"]) for a in SLICES]
    left.plot(SLICES, energies, "o-", color=colour, lw=1.5, label=f"$N = {n}$")
left.set_yscale("log")
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("$E_{KS}$ (units of $m$)")
left.set_title("Energy without interaction")
left.legend()
```

The left panel draws $E_{KS}$ of the free states $N = 592$ and $2352$ at the five slices on a logarithmic axis, where the exact fall $e^{-a_{4,0}}$ is a straight line.

```python
tags = ("lamp2", "lamp1", "lamm1", "lamm2")
labels = ("$+\\lambda_2$", "$+\\lambda_1$", "$-\\lambda_1$", "$-\\lambda_2$")
largest_shift = 0.0  # the largest |E(lambda) - E(0)| of N = 592
for colour, tag, label in zip(PALETTE, tags, labels):
    shift = [float(ground[state_id(592, tag, a)]["E_KS"])
             - float(ground[state_id(592, "lam0", a)]["E_KS"]) for a in SLICES]
    largest_shift = max([largest_shift] + [abs(s) for s in shift])
    right.plot(SLICES, shift, "o-", color=colour, lw=1.5, label=label)
e592 = [float(ground[state_id(592, "lam0", a)]["E_KS"]) for a in SLICES]
right.axhline(0.0, color="0.4", lw=0.8)
right.set_xlabel("slice $a_{4,0}$")
right.set_ylabel("$E_{KS}(\\lambda) - E_{KS}(0)$ (units of $m$)")
right.set_title("Interaction energy shift, $N = 592$")
right.legend(fontsize=8)
save_figure(fig, "energy_history",
            "Left: the Kohn-Sham energy $E_{KS}$ (vertical axis, logarithmic, units "
...)
```

The right panel draws, for $N = 592$, the change $E_{KS}(\lambda) - E_{KS}(0)$ of the four couplings at the five slices, and keeps the largest size of these changes in `largest_shift`. `e592` are the free energies of $N = 592$; the caption of Figure 15a.4 prints their smallest and largest value and `largest_shift`.

```python
report("largest |E(lambda) - E(0)| of N = 592", f"{largest_shift:.4f}")
ordered = all(
    float(ground[state_id(n, "lamm2", a)]["E_KS"])
    > float(ground[state_id(n, "lamm1", a)]["E_KS"])
    > float(ground[state_id(n, "lam0", a)]["E_KS"])
    > float(ground[state_id(n, "lamp1", a)]["E_KS"])
    > float(ground[state_id(n, "lamp2", a)]["E_KS"])
    for n in (8, 592, 2352) for a in SLICES)
check(ordered, "E(-lambda2) > E(-lambda1) > E(0) > E(+lambda1) > E(+lambda2), "
               "N = 8, 592, 2352")
falling = all(float(ground[state_id(n, "lam0", SLICES[i + 1])]["E_KS"])
              < float(ground[state_id(n, "lam0", SLICES[i])]["E_KS"])
              for n in (592, 2352) for i in range(4))
check(falling, "the energy of N = 592 and 2352 falls from slice to slice")
```

Out [11]: the largest shift is $8.3182\,m$, out of energies from 49 to $361\,m$. Python allows a chain of comparisons, `a > b > c`, which is true when every neighbouring pair is ordered; the first check confirms that repulsion lowers and attraction raises the energy, more for the stronger coupling, at every slice and for all three particle numbers. The reason (the text cell before the code cell, and Section 15.5): the occupied fold-band orbitals have $b = 0$ and no scalar density, so to first order the interaction energy is the exchange term $-\tfrac{1}{32}\hat\lambda n^2$, negative for $\hat\lambda > 0$. The second check confirms that the free energies fall from slice to slice.

**In [12], the densities.**

```python
def vol7(a4):
    return (2.0 * math.pi / 0.25) ** 3 * math.exp((2.0 * 4.0 / 3.0 - 1.0) * a4)
```

`vol7` is the proper 7-volume of the cell per unit $e^{3Hy}$ at a slice, $\mathrm{Vol}_7 = \ell^3e^{(2\beta - 1)a_{4,0}}$ with $\ell = 2\pi/0.25$ and $\beta = \tfrac43$ (Section 15.2).

```python
def read_profile(n, tag, a4):
    path = RECORD / "ground/profiles" / f"{state_id(n, tag, a4)}.csv"
    data = np.genfromtxt(path, delimiter=",", names=True)
    return {name: data[name] for name in data.dtype.names}
```

`read_profile` reads the profile table of a state with `np.genfromtxt`, which turns a CSV file into an array whose columns can be addressed by the names in the first line (`names=True`); the function returns a dictionary from each column name (`y`, `n`, `S`, `M_eff`, `v_v`, `rho`, `p3`, ...) to its array of 151 values. The profiles are densities per $\mathrm{Vol}_7(a_{4,0})$, the proper densities (with $b_4(0) = 1$).

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
    prof = read_profile(592, "lam0", a4)
    y = prof["y"]
    per_y = 2.0 * vol7(a4) * np.exp(3.0 * y) * prof["n"]  # particles per unit y
    counts.append(simpson(per_y, y[1] - y[0]))
    left.plot(y, prof["n"], color=shade, lw=1.8, label=f"$a_{{4,0}} = {a4}$")
    right.plot(y, per_y, color=shade, lw=1.8, label=f"$a_{{4,0}} = {a4}$")
```

For $N = 592$, $\lambda = 0$ at the slices 0, 1, 2 the cell reads the profile, forms the number of particles per unit $y$ in the whole cell, $2\,\mathrm{Vol}_7(a_{4,0})\,e^{3Hy}n(y)$, integrates it with Simpson's rule (the spacing is `y[1] - y[0]` $= 0.02$), and draws the proper density on the left and the particles per unit $y$ on the right.

```python
left.set_yscale("log")
left.set_xlabel("hidden coordinate $y$ (tip at $-3$, fold at $0$)")
left.set_ylabel("proper density $n(y)$")
left.set_title("Proper number density")
right.set_xlabel("hidden coordinate $y$")
right.set_ylabel("particles per unit $y$")
right.set_title("$2\\,\\mathrm{Vol}_7\\, e^{3Hy} n(y)$, area $= N$")
right.legend()
save_figure(fig, "densities",
            "Left: the proper number density $n(y)$ (vertical axis, logarithmic, "
...)
report("particle number from the profiles at a4,0 = 0, 1, 2",
       ", ".join(f"{c:.6f}" for c in counts))
check(max(abs(c - 592.0) for c in counts) < 1e-5,
      "Simpson's rule on the profiles gives N = 592 at every slice",
      record=f"{RECORD_REPORT}, check ground_N_conservation")
```

After the labels, `save_figure` saves Figure 15a.5. Out [12] gives $592.000008$, $592.000002$ and $592.000001$: the integral of the coarse 151-point profile reproduces $N$ to $8 \times 10^{-6}$ (the solver's own check ground_N_conservation, on its fine grid, gives $2.4 \times 10^{-15}$). In the figure the particles per unit $y$ follow $e^{2fy}$ (every occupied orbital is a fold-band orbital $e^{fMy}$ with $M = 1$): they sit at the fold and spread toward the tip as $f$ shrinks; the proper density follows $e^{(2f - 3)y}$ and is largest at the tip.

**In [13], the self-consistent potentials.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
ratios = []  # profile maximum / recorded maximum, one per slice
for shade, a4 in zip(SLICE_SHADES, SLICES):
    prof = read_profile(592, "lamp2", a4)
    left.plot(prof["y"], prof["M_eff"] - 1.0, color=shade, lw=1.8,
              label=f"$a_{{4,0}} = {a4}$")
    right.plot(prof["y"], prof["v_v"], color=shade, lw=1.8)
    recorded = float(ground[state_id(592, "lamp2", a4)]["max_abs_Meff_minus_m"])
    ratios.append(float(np.max(np.abs(prof["M_eff"] - 1.0))) / recorded)
```

For $N = 592$ with $+\lambda_2$ the cell draws $M - m$ (left) and $v$ (right) at the five slices, and for each slice divides the largest $|M - m|$ on the 151 profile points by the largest value that the solver recorded on its 1801 fine points.

```python
left.set_xlabel("hidden coordinate $y$")
left.set_ylabel("$M(y) - m$ (units of $m$)")
left.set_title("Mass shift, $N = 592$, $+\\lambda_2$")
left.legend(fontsize=8)
right.set_xlabel("hidden coordinate $y$")
right.set_ylabel("$v(y)$ (units of $m$)")
right.set_title("Exchange potential, $N = 592$, $+\\lambda_2$")
m_max = [float(ground[state_id(592, "lamp2", a4)]["max_abs_Meff_minus_m"])
         for a4 in SLICES]  # the solver's largest |M - m| at each slice
v_max = [float(ground[state_id(592, "lamp2", a4)]["max_abs_v_v"]) for a4 in SLICES]
peak = int(np.argmax(v_max))  # the slice where |v| is largest
save_figure(fig, "potentials",
            "The self-consistent mass shift $M(y) - m$ (left) and potential $v(y)$ "
...)
```

`m_max` and `v_max` are the recorded largest $|M - m|$ and $|v|$ at the five slices, and `np.argmax` gives the position of the largest entry of `v_max`. The caption of Figure 15a.6 prints these numbers.

```python
report("profile maximum / recorded maximum of |M - m|",
       ", ".join(f"{r:.5f}" for r in ratios))
check(all(0.998 <= r <= 1.0 + 1e-12 for r in ratios),
      "the profile maxima of |M - m| lie within 0.2 percent below the recorded ones",
      record=f"{RECORD_RESULTS}/ground/summary.csv, column max_abs_Meff_minus_m")
report("largest |M - m| at the five slices", ", ".join(f"{v:.3f}" for v in m_max))
report("largest |v| at the five slices", ", ".join(f"{v:.3f}" for v in v_max))
check(all(m_max[i + 1] < m_max[i] for i in range(4)) and SLICES[peak] == 0.5
      and all(v_max[i + 1] < v_max[i] for i in range(1, 4))
      and max(m_max + v_max) < 0.25,
      "|M - m| falls at every slice, |v| peaks at a4,0 = 0.5, both stay below 0.25 m",
      record=f"{RECORD_RESULTS}/ground/summary.csv, columns max_abs_Meff_minus_m "
             "and max_abs_v_v")
```

Every profile point is also a point of the fine grid, so the profile maximum cannot exceed the recorded one; it is smaller when the true maximum lies between two profile points. Out [13]: the ratios lie between 0.99968 and 0.99996; the largest $|M - m|$ is $0.208$, $0.169$, $0.103$, $0.047$, $0.017\,m$ and the largest $|v|$ is $0.226$, $0.230$, $0.205$, $0.157$, $0.105\,m$ at the five slices. Both checks pass (`m_max + v_max` joins the two lists into one). The coupling is the same at every slice, but the cell grows like $e^{(5/3)a_{4,0}}$ and the densities with it fall, so the potentials shrink along the history; only $|v|$ grows a little from the first to the second slice, because the orbitals spread toward the tip, where the factor $P$ is large. This is why the calibration of Section 15.2 found its largest potential at the first slice.

**In [14], the convergence of the loop.**

```python
runs = json.loads((RECORD / "ground/runs.json").read_text(encoding="utf-8"))
by_id = {run["id"]: run for run in runs}
fig, ax = plt.subplots()
styles = {"lamp2": "-", "lamm2": "--"}
for colour, n in zip(PALETTE, (8, 592, 2352)):
    for tag, style in styles.items():
        history = by_id[state_id(n, tag, 0.0)]["scfHistory_iteration_residual_E"]
        ax.plot([h[0] for h in history], [h[1] for h in history], style, marker="o",
                ms=4, color=colour, lw=1.5,
                label=f"$N = {n}$, {'+' if tag == 'lamp2' else '-'}$\\lambda_2$")
```

`runs.json` is a list with one entry per ground state; `by_id` files them under their names. For the strongest couplings $\pm\lambda_2$ at the first slice (the hardest cases, because the effective coupling $\hat\lambda/\mathrm{Vol}_7$ is largest there) the residual of every iteration is drawn, solid for $+\lambda_2$ and dashed for $-\lambda_2$.

```python
ax.axhline(1e-11, color="0.3", ls=":", lw=1.2, label="tolerance $10^{-11}$")
ax.set_yscale("log")
ax.set_xlabel("iteration")
ax.set_ylabel("residual: largest change of the potential (units of $m$)")
ax.set_title("Anderson mixing, $a_{4,0} = 0$, couplings $\\pm\\lambda_2$")
ax.legend(fontsize=8, ncol=2)
direct = all(run["path"] == "direct" for run in runs)
final = max(run["scfHistory_iteration_residual_E"][-1][1] for run in runs)
longest = max(run["iterations"] for run in runs)
save_figure(fig, "scf_convergence",
            "Convergence of the self-consistent loop with Anderson mixing: the "
...)
report("largest final residual / largest number of iterations",
       f"{final:.2e} / {longest}")
check(len(runs) == 75 and direct and final <= 1e-11,
      "all 75 ground states converged directly below the tolerance 1e-11",
      record=f"{RECORD_REPORT}, check ground_scf_converged")
```

After the tolerance line and the labels (`ncol=2` puts the legend in two columns), `direct` is true when every run took the path `direct` (no fallback to the continuation in the coupling was needed), `final` is the largest last residual and `longest` the largest number of iterations; `save_figure` saves Figure 15a.7, whose caption prints `longest`. Out [14]: $9.96 \times 10^{-12}$ and 29, and the check passes. In the figure the curves of $N = 8$ for $+\lambda_2$ and $-\lambda_2$ coincide, as the exact symmetry of Section 15.5 predicts.

**In [15], the particle-hole excitations.**

```python
TAGS = ("lam0", "lamp1", "lamm1", "lamp2", "lamm2")  # the five couplings


def read_pairs(n, tag, a4):
    path = RECORD / "excited/particle-hole" / f"{state_id(n, tag, a4)}.csv"
    with open(path, newline="", encoding="utf-8") as handle:
        return {(r["hole_levels"], r["particle_levels"]):
                (float(r["delta_eps"]), float(r["multiplicity"]), r["same_sector"])
                for r in csv.DictReader(handle)}


lists = {(n, tag, a4): read_pairs(n, tag, a4)
         for n in (8, 592, 2352) for tag in TAGS for a4 in SLICES}  # 75 states
```

`read_pairs` reads the list of the lowest particle-hole excitations of a state: the key is the pair (hole levels, particle levels), each written `n2:j:parity:label`, and the value is the excitation energy $\Delta\varepsilon = \varepsilon_{particle} - \varepsilon_{hole}$, the multiplicity $g_{hole}\,g_{particle}$ and the word `true` or `false` that says whether the two levels lie in the same sector. `lists` holds these lists for all 75 ground states.

```python
fig, ax = plt.subplots()
for a4 in SLICES:
    values = list(lists[(592, "lam0", a4)].values())
    ax.scatter([a4] * len(values), [v[0] for v in values],
               s=[v[1] / 200.0 for v in values],  # marker area ~ multiplicity
               color=PALETTE[0], alpha=0.3, edgecolors=PALETTE[0])
lowest = [min(v[0] for v in lists[(592, "lam0", a4)].values()) for a4 in SLICES]
ax.plot(SLICES, lowest, "o-", color=PALETTE[1], lw=1.8, ms=5,
        label="lowest excitation (the Kohn-Sham gap)")
ax.plot(a_fine, lowest[0] * np.exp(-a_fine), "--", color="0.4", lw=1.0,
        label="$\\propto e^{-a_{4,0}}$")
```

`ax.scatter` draws markers whose areas are given by `s`: here the multiplicity divided by 200, so a larger marker is a more degenerate excitation. For $N = 592$ without interaction all listed excitations are drawn at their slice, the lowest excitation of each slice is joined by an orange line, and a dashed curve falls like $e^{-a_{4,0}}$ from the first one.

```python
ax.scatter([], [], s=60, color=PALETTE[0], alpha=0.3, edgecolors=PALETTE[0],
           label="excitations (area: multiplicity)")
ax.set_yscale("log")
ax.set_xlabel("slice $a_{4,0}$ of the history")
ax.set_ylabel("excitation energy $\\Delta\\varepsilon$ (units of $m$)")
ax.set_title("Particle-hole excitations of $N = 592$, $\\lambda = 0$")
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
for n in (8, 592, 2352):
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
         read_table(RECORD, "adiabatic/adiabaticity.csv").values()]
report("particle-hole excitations listed / inside one sector", f"{count} / {inside}")
report("lowest excitation of N = 592 at a4,0 = 0 and 2",
       f"{lowest[0]:.6f}, {lowest[-1]:.6f}")
report("energy of the largest-Q jump inside a sector (smallest, largest)",
       f"{min(jumps):.3f}, {max(jumps):.3f}")
```

`count` is the number of listed excitations of all 75 states, and `inside` the number of those whose two levels lie in one sector. `jumps` collects, from the adiabaticity table, the energy of the jump with the largest adiabaticity number $Q$ in each state (Section 15.21); in the corrected metric every state has such a jump, even $N = 8$, whose zero modes can jump through the kinetic term of the shrinking hidden direction. Out [15]: 1687 excitations, none inside one sector; the lowest excitation of $N = 592$ falls from $0.038587$ to $0.005222$, exactly by $e^{-2}$; the in-sector jumps cost between $0.633$ and $2.290\,m$.

```python
check(lowest_is_gap, "in all 75 states the lowest particle-hole energy is the KS gap",
      record=f"{RECORD_RESULTS}/excited/particle-hole and ground/summary.csv")
check(cheaper, "every excitation listed at all five slices gets cheaper along the "
               "history")
check(count >= len(lists) and inside == 0,
      f"none of the {count} listed excitations stays inside one sector",
      record=f"{RECORD_RESULTS}/excited/particle-hole, column same_sector")
```

The three checks pass. The meaning of the third: the exact evolution along the history keeps the momentum, the block type and the fold condition of every orbital (Section 15.21), so the motion of the background alone cannot create any of the 1687 excitations; it can only cause jumps inside a sector, and the jump with the largest $Q$ costs between $0.633\,m$ and $2.290\,m$, far more than the gap.

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

The same as In [15] of Notebook 15e (Section 15.9), with the eight figure names of this notebook in order (the comment says so) and the file names `15a_<number>_<name>.png`: `enumerate(NAMES, start=1)` pairs each name with its number, the list comprehension collects the names whose file does not exist, the check requires that list to be empty, and `all_checks_passed()` prints the last line. The cell prints PASS every figure file of this notebook exists and ALL 28 CHECKS PASSED (notebook 15a).

### 15.15 What the canonical matrix shows

All numbers of this section are COMPUTED by the Rust solver and reproduced or read by Notebook 15a; the cell is named with each.

**The ground states without interaction** (Notebook 15a, Out [7]; `Revision/kohn_sham/results/ground/summary.csv`):

| $N$ | $a_{4,0}$ | $E_{KS}$ | HOMO | LUMO | $\Delta_{KS}$ |
| --- | --- | --- | --- | --- | --- |
| 8 | 0 | 0 | 0 | 0.250000 | 0.250000 |
| 8 | 1 | 0 | 0 | 0.091970 | 0.091970 |
| 8 | 2 | 0 | 0 | 0.033834 | 0.033834 |
| 592 | 0 | 361.1161 | 0.790569 | 0.829156 | 0.038587 |
| 592 | 1 | 132.8472 | 0.290834 | 0.305030 | 0.014195 |
| 592 | 2 | 48.8718 | 0.106992 | 0.112214 | 0.005222 |
| 2352 | 0 | 2288.3882 | 1.274755 | 1.292293 | 0.017538 |
| 2352 | 1 | 841.8510 | 0.468956 | 0.477889 | 0.008933 |
| 2352 | 2 | 309.6997 | 0.172519 | 0.175806 | 0.003286 |

How to read it. For $N = 8$ the eight particles sit in the zero modes at $\varepsilon = 0$, so $E_{KS} = 0$ at every slice, and the gap is the first band level, exactly $0.25\,e^{-a_{4,0}}$ (Section 15.4). For $N = 592$ the HOMO is the band level of the shell $n_2 = 10$, $0.25\sqrt{10}\,e^{-a_{4,0}}$, and the LUMO that of $n_2 = 11$; both redshift exactly, and the energy, the sum of $g\varepsilon$ over the occupied band levels, falls exactly like $e^{-a_{4,0}}$, from $361.12$ to $48.87$, by the factor $e^{2} = 7.389$. For $N = 2352$ at $a_{4,0} = 0$ the LUMO is $1.292293$, the bulk edge at $k = 0$ (the choice of this $N$); from $a_{4,0} = 0.5$ on the bulk levels have risen above the next band shell ($n_2 = 27$), the LUMO is again a band level, and the gap falls like $e^{-a_{4,0}}$ from there. (Section 15.21 shows that a filling of $N = 2360$ would cross the Fermi level for this reason.) Reading (labelled interpretation of these numbers): as the extra times deflate and 3-space inflates, the 3-momenta of the gas redshift, and the free gas, which lives entirely on the fold band, loses its energy like a gas of massless particles in an expanding box.

**The gaps close exactly like $e^{-a_{4,0}}$.** Figure 15a.2 shows the gaps of $N = 8$ and $592$ exactly on their dashed lines: each is the distance of two fold-band levels, $\kappa(k_{LUMO} - k_{HOMO})$. In the metric of 2026-10-14, withdrawn on 2026-10-16, the band bent below its tangent and the gaps closed more slowly; in the corrected metric the band is exactly straight (Section 15.4).

**Delta-SCF and the orbital relaxation.** Without interaction $\Delta_{SCF} = \Delta_{KS}$ to $3.1 \times 10^{-13}\,m$ (Out [9]). With interaction the relaxation $\Delta_{SCF} - \Delta_{KS}$ is at most $6.3 \times 10^{-4}\,m$ (Out [10], `N2352_lamp1_a00`, the state whose excited particle enters the bulk edge), and at most $2.1 \times 10^{-7}\,m$ in every other state, far below the gap itself: the first excited state is well described by moving one particle between frozen orbitals.

**The interaction is a perturbation.** For $N = 592$ the couplings change the energy by at most $8.32\,m$ out of $361\,m$ (Out [11]), and the self-consistent potentials stay below $0.25\,m$ (Out [13]). The potentials are largest at the first slices (the largest $|v|$ is $0.230\,m$ at $a_{4,0} = 0.5$ for $+\lambda_2$ and falls to $0.105\,m$ at $a_{4,0} = 2$), because the cell grows and the effective coupling $\hat\lambda/\mathrm{Vol}_7$ falls like $e^{-(5/3)a_{4,0}}$, as the calibration of Section 15.2 anticipated; they live near the tip, where the proper densities are large (Figure 15a.6). Repulsion lowers the energy and attraction raises it, for every particle number (Out [11]; Section 15.5). All this holds at the cutoff $L = 3$, where the couplings were calibrated; at larger $L$ the interaction effects of the later slices grow: for $N = 592$ and $2352$ at $a_{4,0} = 2$ the shift of the energy by $\pm\lambda_1$ is 4.6 to 4.7 times larger at large $L$ (Section 15.2, the paragraph on the cutoff). The self-consistent loop converged directly in all 75 states in at most 29 iterations (Out [14]).

**Where the particles are.** Figure 15a.5 makes the most important picture of the gas visible: the particles themselves sit near the fold (right panel), but the proper density, particles per proper 7-volume, is largest at the tip (left panel), because the proper volume factor $e^{3Hy}$ is small there ($e^{-9} = 1.2 \times 10^{-4}$ at $y = -3$). Along the history the band orbitals $e^{fy}$ become flatter, as the hidden scale $f$ shrinks, and reach further toward the tip.

**Excitations.** In every state the cheapest way to excite the gas is the Kohn-Sham gap, all listed excitations get cheaper along the history, and none of them can be caused by the history alone (Out [15]); the next sections ask how much energy the history does put into the gas (Section 15.16) and how strongly it can disturb it (Section 15.21).

**What this does not show.** These are instantaneous states on a PRESCRIBED background, with both fold conditions filled (ASSUMED) and the CONVENTION of filling. Whether a real gas follows them along the history is the question of adiabaticity (Section 15.21); whether the gas could make the history itself is answered in Section 15.16: it could not.

### 15.16 The energy-momentum tensor of the gas, and why the gas cannot drive the history

**What the tensor is.** Chapter 9 introduced the **energy-momentum tensor** $T^\mu{}_\nu$: at every point a table of $8 \times 8$ numbers that says how much energy and momentum there is and how it flows. For the Kohn-Sham states it is diagonal, and its diagonal holds the **energy density** $\rho = -T^{x_4}{}_{x_4}$ and the **pressures** $p_\mu = T^\mu{}_\mu$ (no sum over $\mu$; the sign convention of the Revision record). Because of the symmetries of the states only four different numbers occur at each $y$: $p_3$, the pressure along each of the three directions of 3-space; $p_t$, the pressure along each of the three extra times; $p_0$, the pressure along the hidden direction; and $\rho$. They are proper densities (per proper 7-volume) and depend on $y$.

**The formulas** (ks-theory.json, emt; checks emt_orbital_components and emt_trace_identity). With the orbital densities $n_o = P(a^2 + b^2)$, $s_o = P\,j\,2ab$ and $t_o = P\,j\,(a^2 - b^2)$ (the last one is the current along the momentum; $P = e^{-3Hy}/\mathrm{Vol}_7$ as in Section 15.2) and sums over the occupied levels with the weights $wgf_o$:

$$
\rho = \sum wgf_o\,\varepsilon\,n_o - e_{int}, \qquad p_3 = \sum wgf_o\,\tfrac{\kappa k}{3}\,t_o + e_{int}, \qquad p_t = e_{int},
$$

$$
p_0 = \sum wgf_o\,\big[(\varepsilon - v)\,n_o - M s_o - \kappa k\,t_o\big] + e_{int} .
$$

Three remarks make these formulas plausible. (1) The energy density is the level times the number density, summed, minus the interaction energy density (the same double counting as in Section 15.5). (2) A quantum moving along $x_1$ pushes on a wall across $x_1$ with $\kappa k\,t_o$; a closed shell of momenta contains every direction equally often (a cube has the same number of vectors along each axis), so the pressure along each of the three directions is one third of it. (3) The states belong to the **good sector**: they have no momentum along the extra times, so the extra-time pressure has no kinetic part at all, and only the interaction contributes, $p_t = e_{int}$. Without interaction $p_t = 0$.

**The free gas, exactly.** For a fold-band orbital $(a, b) = (Ae^{fMy}, 0)$ with $\varepsilon = \kappa k$ and no interaction, line by line:

$$
n_o = PA^2e^{2fMy}, \qquad s_o = 0, \qquad t_o = j\,PA^2e^{2fMy} = n_o .
$$

Rule: the definitions with $b = 0$ and $j = +1$ for the band (the zero modes have $j = \pm1$, but $k = 0$ and $\varepsilon = 0$, so their terms vanish below).

$$
\varepsilon\,n_o = \kappa k\,n_o = \kappa k\,t_o, \qquad (\varepsilon - v)\,n_o - Ms_o - \kappa k\,t_o = \kappa k\,n_o - 0 - \kappa k\,n_o = 0 .
$$

Rule: insert $\varepsilon = \kappa k$, $v = 0$, $s_o = 0$ and $t_o = n_o$. So every occupied orbital of the free gas contributes $\kappa k\,n_o$ to $\rho$, a third of it to $p_3$, and nothing to $p_0$ and $p_t$:

$$
p_3 = \tfrac13\rho, \qquad p_0 = p_t = 0 \qquad (\lambda = 0,\ \text{at every } y) .
$$

The free gas is a **radiation-like gas**: the pressure of massless particles moving in 3-space, although the quanta have the mass $m$; the mass only holds the orbitals at the fold. Status: PROVED (this derivation, from the formulas of the record), and COMPUTED to rounding in the record (`Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md`, section 9) and in Notebook 15b (Out [4]).

**The conservation law along the hidden direction.** The conservation law of the tensor states that its covariant divergence vanishes, $\nabla_\mu T^\mu{}_\nu = 0$ (Chapter 9). In flat spacetime it says that energy and momentum are neither created nor destroyed, they only flow. In the author's metric, which depends on the time $x_4$ through $a_4$ and $b_4$, it is a local balance law: the energy of the gas is not conserved, it changes along the history (the energy-change law below; for a universe, Section 20.22 (d)). We write out its $y$ component for a diagonal tensor that depends only on $y$, line by line, in the hidden-coordinate form of the metric (Chapter 14),

$$
ds^2 = e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 + f^2\big[dy^2 - e^{2Hy}(dx_5^2 + dx_6^2 + dx_7^2)\big], \qquad f = e^{-a_4}b_4^{1/2} .
$$

The covariant divergence of a mixed tensor is

$$
\nabla_\mu T^\mu{}_\nu = \partial_\mu T^\mu{}_\nu + \Gamma^\mu{}_{\mu\sigma}T^\sigma{}_\nu - \Gamma^\sigma{}_{\mu\nu}T^\mu{}_\sigma ,
$$

with the Christoffel symbols $\Gamma$ (Chapters 3 and 9; summed over repeated indices). For a diagonal metric Chapter 9 gives $\Gamma^\kappa{}_{\mu\nu} = \frac{1}{2g_{\kappa\kappa}}(\partial_\mu g_{\kappa\nu} + \partial_\nu g_{\kappa\mu} - \partial_\kappa g_{\mu\nu})$ (no sum over $\kappa$; here $\kappa$ is only an index name).

$$
\nabla_\mu T^\mu{}_y = \partial_y T^y{}_y + \Gamma^\mu{}_{\mu y}\,T^y{}_y - \sum_\nu \Gamma^\nu{}_{\nu y}\,T^\nu{}_\nu .
$$

Rule: set $\nu = y$; for a diagonal tensor only $\sigma = y$ survives in the middle term and only $\sigma = \mu$ in the last, and only the $y$ derivative of $T^y{}_y$ is nonzero. (The index $\nu$ in the sum runs over the eight directions; the letter $\lambda$ is kept for the coupling.)

$$
\Gamma^\mu{}_{\mu y} = \partial_y \ln\sqrt{|g|} = \partial_y\big(\ln(e^{3a_4}f^4) + 3Hy\big) = 3H .
$$

Rule: for a diagonal metric $\Gamma^\mu{}_{\mu y} = \sum_\mu\frac{1}{2g_{\mu\mu}}\partial_y g_{\mu\mu} = \frac12\sum_\mu\partial_y\ln|g_{\mu\mu}| = \frac12\partial_y\ln|\det g| = \partial_y\ln\sqrt{|g|}$ (the formula above with $\kappa = \mu$ and $\nu = y$, where the first and the last term cancel; $\partial\ln Q = \partial Q/Q$; the logarithm of a product is the sum of the logarithms); in this form of the metric $\sqrt{|g|} = e^{3a_4}\cdot1\cdot f\cdot(fe^{Hy})^3 = e^{3a_4}f^4e^{3Hy}$, and only $e^{3Hy}$ depends on $y$.

$$
\Gamma^\nu{}_{\nu y} = \tfrac12 g^{\nu\nu}\partial_y g_{\nu\nu} = \tfrac12\partial_y\ln|g_{\nu\nu}| = H \quad (\nu = x_5, x_6, x_7), \qquad 0 \quad (\nu = x_1, x_2, x_3, x_4, y) .
$$

Rule: the same formula for one value of $\nu$ (no sum) gives half the derivative of $\ln|g_{\nu\nu}|$; only the three extra times carry the factor $e^{2Hy}$, and $\tfrac12\partial_y\ln e^{2Hy} = H$; 3-space has no warp ($g_{11} = e^{2a_4}$), and $g_{x_4x_4} = -1$ and $g_{yy} = f^2$ do not depend on $y$.

$$
p_0' + 3H\,p_0 - 3H\,p_t = 0 .
$$

Rule: $T^y{}_y = p_0$; the three warped terms give $H$ times $p_t$ three times.

$$
\big(e^{3Hy}p_0\big)' = 3H\,e^{3Hy}\,p_t .
$$

Rule: $(e^{3Hy}p_0)' = e^{3Hy}(p_0' + 3Hp_0)$ (product and chain rule); multiply the previous line by $e^{3Hy}$. This is the **conservation law along $y$** (ks-theory.json, emt.conservationY). The 3-space pressure does not enter, because 3-space has no warp. Integrated from the tip to the fold it reads $[e^{3Hy}p_0]_{-L}^{0} = 3H\int_{-L}^{0}e^{3Hy}p_t\,dy$. For the free gas both sides vanish ($p_0 = p_t = 0$); with interaction it is a real test. It is PROVED for every self-consistent state (check emt_y_conservation_selfconsistent of `Revision/kohn_sham/reports/ks-theory-python.json`: the force terms $-M'S - v'n$ of the orbitals cancel exactly against the derivative of $e_{int}$ when the potentials are the self-consistent ones) and COMPUTED for all 75 ground states of the record (checks emt_y_conservation_pointwise, worst relative residual $5.2 \times 10^{-10}$, and emt_y_conservation_integrated, worst $3.6 \times 10^{-11}$, of `Revision/kohn_sham/reports/ks-rust-solver.json`).

**The energy change along the history.** Now the $x_4$ component. The metric depends on $x_4$ through $a_4(x_4)$ and $b_4(x_4)$, and the states are instantaneous states that follow it. Line by line:

$$
\nabla_\mu T^\mu{}_{x_4} = \partial_{x_4}T^{x_4}{}_{x_4} + \Gamma^\mu{}_{\mu x_4}T^{x_4}{}_{x_4} - \sum_\nu \Gamma^\nu{}_{\nu x_4}T^\nu{}_\nu .
$$

Rule: as before with $y$ replaced by $x_4$, now with the time derivative of $T^{x_4}{}_{x_4}$ (the flux $T^y{}_{x_4}$ along $y$ vanishes for the instantaneous states, ks-theory.json emt.offDiagonal).

$$
\Gamma^\mu{}_{\mu x_4} = \partial_{x_4}\ln\big(e^{3a_4}f^4e^{3Hy}\big) = 3a_4' + 4\,\frac{f'}{f} = 3a_4' + 4h_4, \qquad h_4 = \frac{f'}{f} = \frac{b_4'}{2b_4} - a_4' .
$$

Rule: the same formula with $x_4$; the logarithm of a product is a sum; $\ln f = -a_4 + \tfrac12\ln b_4$, whose derivative is $h_4$ (Section 14.2 uses the same $h_4$). This is $-a_4' + 2b_4'/b_4$, the rate of change of the proper volume element $e^{-a_4}b_4^2$ (check geometry_sqrt_det).

$$
\Gamma^\nu{}_{\nu x_4} = \tfrac12\partial_{x_4}\ln|g_{\nu\nu}| = a_4' \ (\nu = x_1, x_2, x_3), \quad h_4 \ (\nu = x_5, x_6, x_7, y), \quad 0 \ (\nu = x_4) .
$$

Rule: 3-space carries $e^{2a_4}$, the extra times and the hidden direction carry $f^2$, and $\tfrac12\partial_{x_4}\ln f^2 = f'/f$; $g_{x_4x_4} = -1$.

$$
-\partial_{x_4}\rho - (3a_4' + 4h_4)\,\rho - 3a_4'\,p_3 - 3h_4\,p_t - h_4\,p_0 = 0 .
$$

Rule: $T^{x_4}{}_{x_4} = -\rho$ and $T^\nu{}_\nu = p_3, p_t, p_0$; insert the symbols.

$$
\partial_{x_4}\rho = -3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0) .
$$

Rule: move everything but $\partial_{x_4}\rho$ to the right and split $(3a_4' + 4h_4)\rho$ into $3a_4'\rho + 3h_4\rho + h_4\rho$. In words: 3-space (three directions with the rate $a_4'$), the extra times (three with $h_4$) and the hidden direction (one with $h_4$) each change the energy density by their rate times $\rho$ plus their pressure (ks-theory.json, emt.energyChange; PROVED, check emt_x4_component). On the record's history $a_4' = AH$ and $b_4'/b_4 = \tfrac43AH$, so $h_4 = \tfrac23AH - AH = -\tfrac13AH$: the extra times and the hidden direction shrink at one third of the rate at which 3-space grows.

$$
\frac{\partial\rho}{\partial a_4} = -3(\rho + p_3) + (\rho + p_t) + \tfrac13(\rho + p_0) = -\tfrac53\rho - 3p_3 + p_t + \tfrac13p_0 .
$$

Rule: along the history $\partial_{x_4} = a_4'\,\partial/\partial a_4$ (chain rule); divide by $a_4' = AH$ and insert $h_4/a_4' = -\tfrac13$; collect the terms with $\rho$: $-3 + 1 + \tfrac13 = -\tfrac53$.

$$
\frac{dE}{da_4} = \tfrac53E + 2\,\mathrm{Vol}_7\int_{-L}^{0}e^{3Hy}\,\frac{\partial\rho}{\partial a_4}\,dy = -3P_3 + P_t + \tfrac13P_0, \qquad P = 2\,\mathrm{Vol}_7\int_{-L}^{0}e^{3Hy}p\,dy .
$$

Rule: $E = 2\,\mathrm{Vol}_7\int e^{3Hy}\rho\,dy$ with $\mathrm{Vol}_7 \propto e^{(5/3)a_4}$ (Section 15.2), so the product rule gives $\tfrac53E$ from the volume and the integral of $\partial\rho/\partial a_4$; the term $-\tfrac53\rho$ integrates to $-\tfrac53E$ and cancels it. This is the **energy-change law** (ks-theory.json, emt.energyChange; check emt_energy_change_history of the theory record), with $E = E_{KS}$ (check emt_energy_integral of the solver: relative difference at most $2.3 \times 10^{-15}$ in all 75 states); COMPUTED for all 75 states against differences of the self-consistent energies at neighbouring slices with fixed occupations (check emt_energy_change_dE_da4, worst $9.2 \times 10^{-10}$).

**How to read it: work.** Write the law as $dE = (-3P_3 + P_t + \tfrac13P_0)\,da_4$. When 3-space inflates by $da_4$, each of its three directions stretches by the factor $e^{da_4}$, and a gas that pushes outward with the pressure $p_3$ does work on the expanding space and loses that energy, as a gas in an expanding cylinder pushes a piston: $-3P_3\,da_4$. The three extra times and the hidden direction shrink by the factor $e^{-da_4/3}$ each, and a gas that pushes on them has work done on it: $+3\cdot\tfrac13P_t\,da_4$ and $+\tfrac13P_0\,da_4$. For the free gas $P_t = P_0 = 0$ and $P_3 = E/3$, so

$$
\frac{dE}{da_4} = -E, \qquad E(a_{4,0}) = E(0)\,e^{-a_{4,0}} ,
$$

exactly the redshift of the fold band of Section 15.4 (rule: the solution of $E' = -E$ is $E(0)e^{-a}$). With interaction $p_t = e_{int}$ is dominated by the exchange term $-\tfrac{1}{32}\hat\lambda n^2$ and has the sign of $-\hat\lambda$ (Notebook 15b finds this for the integrated $P_t$ of all 60 interacting ground states, Out [11]): the deflation of the extra times then takes energy from a repulsive gas and gives energy to an attractive one.

**Why the gas cannot be the source of the history.** In the author's theory the functions $a_4(x_4)$ and $b_4(x_4)$ are not free: they must solve the field equations (Chapter 12), whose right-hand side is the energy-momentum tensor of the matter. The record `Revision/field_equations_a4/reports/ks-source-conditions.json` (5 checks, all PASS) lists, under its key conditions, what a source must satisfy in the corrected metric:

- (C1) every component of the source is independent of $x_0$, that is, of $y$ (the left-hand sides contain no $x_0$, for every $a_4$ and $b_4$);
- (C2) $p_0 = p_t$ (the hidden and the extra-time components of every left-hand side are equal);
- (C3) no off-diagonal component, $T^{x_4}{}_{x_0} = 0$;
- (C4) on the history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ with the author's Lovelock weights, exactly the source that this history needs: an $x_0$-independent tensor with $p_0 = p_t$, recorded in `Revision/field_equations_a4/a4-equations.json`.

The Kohn-Sham gas fails them. C1: its densities vary strongly with $y$ (Figure 15a.5); the record finds $(\max\rho - \min\rho)/\max|T| \ge 0.456213$ in every one of the 70 states with a nonzero tensor (check ks_profiles_depend_on_x0). C2: it holds, to rounding, for exactly the 10 nonzero free states (their fold-band orbitals have no hidden kinetic pressure, as derived above) and fails for every one of the 60 interacting states, $\max_y|p_0 - p_t|/\max|T| \ge 0.080929$ (check ks_hidden_pressure_condition): the interaction bends the orbitals. C3 holds for every eigen-orbital (check ks_offdiagonal_condition). C4: the needed source has the energy density $\kappa\rho = 3.57407$ at $a_{4,0} = 0$ and $-7.63383$ at $a_{4,0} = 2$ (it changes sign along the history; $\kappa$ here is the gravitational coupling constant of the field equations, not the momentum weight), with $p_3/\rho = -1.26713$ and $p_0/\rho = p_t/\rho = -2.38212$ at $a_{4,0} = 0$, while the free gas has $p_3/\rho = \tfrac13$ and $p_0 = p_t = 0$ (check ks_history_is_a_prescribed_background). The five free states of $N = 8$ are not covered by C1 and C2: their tensor vanishes identically (only the zero modes are filled, with $\varepsilon = 0$ and no momentum), a zero source, and no exponential history is a vacuum solution for the author's weights (check ks_zero_source_states_listed). Notebook 15b reproduces these numbers from the committed profiles and its own states (Out [12]). A fuller analysis of the record (`Revision/field_equations_a4/ks_source/reports/ks-source-a4.json`, 19 checks, all PASS; Chapter 17) adds that the states do satisfy the conservation identity along $y$ above, so they fail the field equations because of their dependence on $x_0$ and, with interaction, $p_0 \ne p_t$, not because conservation fails. Hence the status: the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ is a **PRESCRIBED BACKGROUND**, and the gas is a **test field** on it, without back-reaction; quantities derived along the history, such as the ratios of integrated pressures below, are not consequences of the coupled field equations. Chapter 17 returns to this question with the full source analysis.

**Integrated pressures.** For the free gas $P_3/E = \tfrac13$ and $P_0 = P_t = 0$ at every slice (Notebook 15b, Out [9]; `Revision/kohn_sham/results/ground/emt-integrals.csv`), the integrated pressures of a gas of massless particles in 3-space; with interaction the ratios move away from these values, $P_t/E$ and $P_0/E$ with the sign of $-\hat\lambda$ (Figure 15b.5). These are integrated components on a prescribed background, not an equation of state that an observer in 3-space would measure (that question belongs to the dark-sector work of the record, Chapter 22).

### 15.17 Example: the energy-momentum profiles (Notebook 15b)

Notebook 15b runs the solver's command `single` for two states, $N = 592$ without interaction at $a_{4,0} = 1$ and $N = 592$ with $+\lambda_2$ at $a_{4,0} = 2$, and checks that their profiles equal the committed ones. It draws the energy density and the 3-space pressure of the free state as proper densities, with $p_3 = \rho/3$ (Figure 15b.1), and the four components as the densities that are integrated over $y$ (Figure 15b.2); it checks the conservation law along $y$ point by point and integrated on the interacting state (Figure 15b.3); it solves the free state $N = 592$ at 17 slices and checks the energy-change law at every slice, integrated over the whole history and on all 75 recorded states (Figure 15b.4); it draws the integrated pressure ratios (Figure 15b.5) and the spreading of the energy toward the tip (Figure 15b.6), shows the interaction terms (Figure 15b.7), and tests the source conditions on the record's profiles and on its own states. It needs Rust, takes about a minute, and ends with ALL 20 CHECKS PASSED (notebook 15b).

What to look for: in Figure 15b.1 that the proper densities are largest at the tip and that $p_3$ lies on the dotted line $\rho/3$; in Figure 15b.2 that the same quantities times the volume factor sit near the fold; in Figure 15b.3 two curves that lie on top of each other; in Figure 15b.4 short orange lines, computed from the pressures alone, that touch the curve of the energies.

<!-- NOTEBOOK 15b -->

### 15.20 Line-by-line walk-through of Notebook 15b

The notebook has 13 code cells, In [1] to In [13]. As in Section 15.9, docstrings are left out of the quotations, and long caption strings in calls of `save_figure` are shortened: the quotation shows the first line of the call and the first line of the caption, and then a line `...)` that stands for the rest of the caption and the closing parenthesis; the complete cells are printed in Section 15.19.

**In [1], the set-up cell.** It is the set-up cell of Notebook 15a (Section 15.14, which explains the two Rust lines and the function `rust_program`; the rest is explained in Section 15.9), with the run instructions of this notebook (Section 15.18) in its comments and `NOTEBOOK_ID = "15b"`.

**In [2], the solver and two profiles.**

```python
import csv  # reads the tables (CSV files)
import math  # exp and pi for single numbers

import numpy as np  # arrays of numbers

program = rust_program("Revision/kohn_sham/solver/Cargo.toml", "revision_ks_solver")
RUN_FOLDER = REPO / "Revision/kohn_sham/solver/target/textbook_15b"  # ignored by git
RUN_FOLDER.mkdir(parents=True, exist_ok=True)
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
SLICE_SHADES = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]  # light->dark
H = 1.0
```

The imports, the build of the solver (Section 15.14), the folder for the solver's output files inside the build folder `target`, the colours and the constant $H = 1$.

```python
def vol7(a4):
    return (2.0 * math.pi / 0.25) ** 3 * math.exp((2.0 * 4.0 / 3.0 - 1.0) * a4)
```

`vol7` is the proper 7-volume of the cell per unit $e^{3Hy}$ at a slice, $\mathrm{Vol}_7 = \ell^3e^{(2\beta - 1)a_{4,0}} = \ell^3e^{(5/3)a_{4,0}}$ with $\ell = 2\pi/0.25$ and $\beta = \tfrac43$ (Section 15.2).

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

`solve_state` runs the solver's command `single` for one state. The list `command` holds the program, the command and its options (each written with two hyphens): the repository folder, the mass $m = 1$, the coupling, the slice and the particle number (`repr` writes a number with all its digits, so the solver receives exactly the value in the notebook), and the name of the JSON file of the results. If the profiles are wanted, the option profiles and the name of a CSV file are added (`+=` appends to the list). The function runs the command, stops with the end of the solver's error message if the return code is not 0 or the last printed line is not SUCCESS, and returns the JSON record read back into Python.

```python
params = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                    .read_text(encoding="utf-8"))
LAMBDA2_592 = {int(c["N"]): c for c in params["couplingCalibration"]["values"]}[592][
    "lambda2"]  # the coupling lambda_2 of N = 592
free_state = solve_state("N592_lam0_a10", 592, 0.0, 1.0, profiles=True)
strong_state = solve_state("N592_lamp2_a20", 592, LAMBDA2_592, 2.0, profiles=True)
say(f"solved N592_lam0_a10 ({free_state['iterations']} iteration) and N592_lamp2_a20 "
    f"({strong_state['iterations']} iterations, lambda = {LAMBDA2_592})")
```

The coupling $\lambda_2 = 6.393$ of $N = 592$ is read from the parameters of the record (the calibration entries are filed under their particle number and the entry of 592 is taken). Then the two states are solved with their profiles: the free state at $a_{4,0} = 1$ and the strongly interacting state at $a_{4,0} = 2$. Out [2]: the free state needs 1 iteration (no interaction), the interacting one 13 iterations.

**In [3], comparison with the committed profiles.**

```python
RECORD_PROFILES = "Revision/kohn_sham/results/ground/profiles"
FAMILIES = [["y"], ["n", "S", "Q"], ["M_eff", "v_v", "w_Q"],
            ["e_int", "rho", "p3", "p_t", "p0"]]  # columns compared together


def read_profile(path):
    data = np.genfromtxt(path, delimiter=",", names=True)
    return {name: data[name] for name in data.dtype.names}
```

`FAMILIES` groups the columns of a profile table whose sizes belong together: the coordinate; the three densities $n$, $S$, $Q$; the three potentials $M_{eff}$, $v_v$ and $w_Q$ (the last one belongs to the exact-Fock variant and is zero in the canonical functional); and the five components $e_{int}$, $\rho$, $p_3$, $p_t$, $p_0$. `read_profile` reads a profile table into a dictionary of arrays (Section 15.14, In [12]).

```python
worst = 0.0
identical = []
for name in ("N592_lam0_a10", "N592_lamp2_a20"):
    new = read_profile(RUN_FOLDER / f"{name}.csv")
    old = read_profile(repository_file(f"{RECORD_PROFILES}/{name}.csv"))
    for family in FAMILIES:
        scale = max(max(float(np.max(np.abs(old[c]))) for c in family), 1e-300)
        for column in family:
            worst = max(worst, float(np.max(np.abs(new[column] - old[column]))) / scale)
    identical.append((RUN_FOLDER / f"{name}.csv").read_bytes()
                     == repository_file(f"{RECORD_PROFILES}/{name}.csv").read_bytes())
```

For both states and every column the largest difference between the new and the committed profile is divided by the largest value of the column's family (`1e-300` keeps the division defined for a family that is zero), and the largest of these relative differences is kept in `worst`. A column that vanishes up to rounding, such as $p_0$ of the free state, is thereby measured against the size of the components of its family, not against its own rounding values. `identical` records whether the two files are equal byte for byte.

```python
say("columns: " + ", ".join(old))
report("largest difference to the record, relative to the family", f"{worst:.1e}")
report("profile files byte-identical to the record", identical)
check(worst < 1e-9, "the new profiles equal the committed profiles within 1e-9",
      record=f"{RECORD_PROFILES}/N592_lam0_a10.csv and N592_lamp2_a20.csv")
```

Out [3] lists the twelve columns, reports the largest relative difference $1.7 \times 10^{-14}$ and `[False, False]`: on the computer that built the book the files differ in the last digits of some numbers (a different mathematical library from the one of the record), far below the tolerance $10^{-9}$, which is far below the accuracy of the profiles themselves. The check passes.

**In [4], the proper densities.**

```python
prof = read_profile(RUN_FOLDER / "N592_lam0_a10.csv")
y = prof["y"]
step = float(y[1] - y[0])  # 0.02
COMPONENTS = [("rho", "$\\rho$"), ("p3", "$p_3$"), ("p_t", "$p_t$"), ("p0", "$p_0$")]
t_scale = max(float(np.max(np.abs(prof[c]))) for c, _ in COMPONENTS)  # max |T|
```

`prof` is the new profile of the free state; `y` holds the 151 points and `step` their spacing 0.02. `COMPONENTS` pairs each column name with its label for the figures, and `t_scale` is $\max|T|$, the largest absolute value of the four components over $y$.

```python
fig, ax = plt.subplots()
ax.semilogy(y, prof["rho"], color=PALETTE[0], lw=2.5, label="$\\rho$")
ax.semilogy(y, prof["p3"], color=PALETTE[1], lw=2.5, label="$p_3$")
ax.semilogy(y, prof["rho"] / 3.0, color="black", lw=1.0, ls=":", label="$\\rho/3$")
ax.set_xlabel("hidden coordinate $y$ (tip at $-3$, fold at $0$)")
ax.set_ylabel("proper density (units of $m^8$)")
ax.set_title("Energy density and pressure, $N = 592$, $\\lambda = 0$, $a_{4,0} = 1$")
ax.legend()
p0_size = float(np.max(np.abs(prof["p0"]))) / t_scale  # p0 relative to max |T|
eos_dev = float(np.max(np.abs(prof["p3"] - prof["rho"] / 3.0))) / t_scale
save_figure(fig, "proper_emt",
            "The energy density $\\rho$ and the 3-space pressure $p_3$ of the free "
...)
```

The cell draws $\rho$ and $p_3$ on a logarithmic axis (`semilogy`), and $\rho/3$ as a thin dotted black line. A proper energy density is an energy per proper 7-volume, so its unit is $m \cdot m^7 = m^8$ in units where $H = m = 1$. `p0_size` is the largest $|p_0|$ relative to $\max|T|$, and `eos_dev` the largest deviation of $p_3$ from $\rho/3$, relative too. `save_figure` saves Figure 15b.1: both curves are largest at the tip, where the proper volume factor $e^{3Hy}$ is small, and $p_3$ lies on the dotted line.

```python
report("largest |p_t| and largest |p0| / max|T|",
       f"{float(np.max(np.abs(prof['p_t'])))}, {p0_size:.1e}")
report("largest |p3 - rho/3| / max|T|", f"{eos_dev:.1e}")
check(float(np.max(np.abs(prof["p_t"]))) == 0.0, "p_t = e_int = 0 when lambda = 0")
check(p0_size < 1e-12 and eos_dev < 1e-12,
      "the free gas has p0 = 0 and p3 = rho/3 at every point, to 1e-12",
      record="Revision/field_equations_a4/reports/ks-source-conditions.json, check "
             "ks_hidden_pressure_condition")
```

Out [4]: $p_t$ is exactly 0.0 (without interaction $e_{int} = 0$), $|p_0|/\max|T| = 1.8 \times 10^{-17}$ and $|p_3 - \rho/3|/\max|T| = 1.6 \times 10^{-16}$, rounding values: the exact result $p_3 = \rho/3$, $p_0 = p_t = 0$ of Section 15.16. Both checks pass.

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

`simpson` is Simpson's rule on equally spaced points (Section 15.14, In [12]); `read_rows` reads a committed table of the record and files its rows under the state name.

```python
EMT_TABLE = "Revision/kohn_sham/results/ground/emt-integrals.csv"
emt_rows = read_rows(EMT_TABLE)
summary_rows = read_rows("Revision/kohn_sham/results/ground/summary.csv")
weight = 2.0 * vol7(1.0) * np.exp(3.0 * H * y)  # 2 Vol_7 e^{3Hy} at a4,0 = 1
fig, ax = plt.subplots()
integrals = {}
for colour, (column, label) in zip(PALETTE, COMPONENTS):
    ax.plot(y, weight * prof[column], color=colour, lw=2.0, label=label)
    integrals[column] = simpson(weight * prof[column], step)
```

`emt_rows` and `summary_rows` are the committed tables of the integrated tensor and of the ground states. `weight` is $2\,\mathrm{Vol}_7(1)\,e^{3Hy}$, which turns a proper density at the slice 1 into the amount per unit $y$ in the whole cell. For each component the cell draws the product and integrates it with Simpson's rule.

```python
ax.axhline(0.0, color="0.4", lw=0.8)
ax.set_xlabel("hidden coordinate $y$")
ax.set_ylabel("$2\\,\\mathrm{Vol}_7\\, e^{3Hy} \\times$ component (units of $m$)")
ax.set_title("The integrands: energy and pressures per unit $y$")
ax.legend()
save_figure(fig, "coordinate_emt",
            "The energy density and the pressures of the free state $N = 592$, "
...)
```

The zero line, the labels, and `save_figure` for Figure 15b.2; its caption prints $E_{KS}$ from the solver's JSON record. In this form the energy and the 3-space pressure sit near the fold, like the particles in Figure 15a.5, and $p_t$ and $p_0$ lie on the zero line.

```python
row = emt_rows["N592_lam0_a10"]
rel = lambda a, b: abs(a - b) / max(abs(b), 1e-300)
worst_int = max(rel(integrals[c], float(row[f"int_{c}"])) for c in ("rho", "p3"))
report("E_KS from the profile / from the solver",
       f"{integrals['rho']:.8f} / {free_state['E_KS']:.8f}")
report("largest relative difference of the integrals to the record", f"{worst_int:.1e}")
check(rel(free_state["E_KS"], float(summary_rows["N592_lam0_a10"]["E_KS"])) < 1e-12,
      "the solver's E_KS equals the record",
      record="Revision/kohn_sham/results/ground/summary.csv, N592_lam0_a10")
check(rel(integrals["rho"], free_state["E_KS"]) < 1e-6 and worst_int < 1e-6,
      "Simpson's rule on the profile gives E_KS and the recorded integrals",
      record=f"{EMT_TABLE}, columns int_rho, int_p3")
```

`rel` is a small function (a `lambda`) for the relative difference. `worst_int` compares the integrals of $\rho$ and $p_3$ with the record's columns `int_rho` and `int_p3`. Out [5]: $E_{KS} = 132.84720569$ from the 151-point profile against $132.84720519$ from the solver's fine grid, and a largest relative difference of $3.7 \times 10^{-9}$ to the record. Both checks pass.

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

`derivative4` computes the derivative of a list of equally spaced values with fourth-order accuracy (an error proportional to $h^4$): inside, the centred formula $[f_{i-2} - 8f_{i-1} + 8f_{i+1} - f_{i+2}]/(12h)$ for all points at once (`f[:-4]` are the values two places to the left of the points `2:-2`, `f[4:]` two places to the right, and so on); at the two first and the two last points, where two neighbours on one side are missing, one-sided formulas of the same order, as in the solver. (Here `f` is a list of values, not the hidden scale.)

```python
def conservation(p):
    e3 = np.exp(3.0 * H * p["y"])
    left = derivative4(e3 * p["p0"], step)
    right = 3.0 * H * e3 * p["p_t"]
    scale = max(float(np.max(np.abs(left))), float(np.max(np.abs(right))))
    jump = e3[-1] * p["p0"][-1] - e3[0] * p["p0"][0]
    integral = simpson(right, step)
    return left, right, np.abs(left - right) / scale, abs(jump - integral) / abs(jump)
```

`conservation` evaluates both sides of $(e^{3Hy}p_0)' = 3H\,e^{3Hy}p_t$ on a profile: the left side by the finite difference, the right side directly. It returns both sides, their difference at every point relative to the larger of the two, and the integrated form: the jump $[e^{3Hy}p_0]_{-3}^{0}$ (`e3[-1]` is the value at the fold, `e3[0]` at the tip) against the Simpson integral of the right side, relative to the jump.

```python
sp = read_profile(RUN_FOLDER / "N592_lamp2_a20.csv")
left, right, residual, integrated = conservation(sp)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
ax1.plot(sp["y"], left, color=PALETTE[0], lw=3.0, label="$(e^{3Hy}p_0)'$")
ax1.plot(sp["y"], right, color=PALETTE[1], lw=1.5, ls="--",
         label="$3H\\,e^{3Hy}p_t$")
ax1.set_xlabel("hidden coordinate $y$")
ax1.set_ylabel("units of $m^9$")
ax1.set_title("The two sides of the law")
ax1.legend()
ax2.semilogy(sp["y"], np.maximum(residual, 1e-16), color=PALETTE[2], lw=1.5)
ax2.axhline(1e-4, color="0.4", ls=":", lw=1.2, label="tolerance $10^{-4}$")
ax2.set_xlabel("hidden coordinate $y$")
ax2.set_ylabel("|left - right| / largest value")
ax2.set_title("Relative residual on the 151 points")
ax2.legend()
save_figure(fig, "y_conservation",
            "Left: the two sides of the conservation law along the hidden "
...)
```

`sp` is the profile of the interacting state $N = 592$, $+\lambda_2$, $a_{4,0} = 2$. The left panel draws the two sides (thick solid and thin dashed, so that both are visible when they coincide); the right panel draws the relative residual on a logarithmic axis (`np.maximum(residual, 1e-16)` replaces exact zeros, which a logarithmic axis cannot show) with the tolerance $10^{-4}$ as a dotted line. This is Figure 15b.3.

```python
free_e3 = np.exp(3.0 * H * y)
free_sides = max(float(np.max(np.abs(derivative4(free_e3 * prof["p0"], step)))),
                 float(np.max(np.abs(3.0 * H * free_e3 * prof["p_t"])))) / t_scale
report("largest pointwise residual / integrated residual",
       f"{float(np.max(residual)):.1e} / {integrated:.1e}")
report("free state: largest side of the law / max|T|", f"{free_sides:.1e}")
check(float(np.max(residual)) < 1e-4 and integrated < 1e-6,
      "(e^{3Hy} p0)' = 3H e^{3Hy} p_t holds for N592_lamp2_a20",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, checks "
             "emt_y_conservation_pointwise and emt_y_conservation_integrated")
check(free_sides < 1e-10, "both sides of the law vanish for the free state")
```

For the free state the two sides are computed too, relative to $\max|T|$. Out [6]: the largest pointwise residual of the interacting state is $1.7 \times 10^{-7}$ (the error of the finite difference on the coarse grid) and the integrated one $1.2 \times 10^{-10}$; for the free state both sides are of size $9.1 \times 10^{-18}$, zero to rounding. Both checks pass.

**In [7], the energy at 17 slices and its slope.**

```python
DENSE = [i / 8.0 for i in range(17)]  # the slices 0, 0.125, ..., 2
history = []
for a4 in DENSE:
    record = solve_state(f"N592_lam0_dense_{round(1000 * a4):04d}", 592, 0.0, a4)
    ints = record["emtIntegrals_2Vol7_int_e3Hy"]  # 2 Vol_7 int e^{3Hy} (...) dy
    history.append({"a4": a4, "E": record["E_KS"], "rho": ints["rho"],
                    "p3": ints["p3"], "p_t": ints["p_t"], "p0": ints["p0"],
                    "slope": -3.0 * ints["p3"] + ints["p_t"] + ints["p0"] / 3.0})
```

`DENSE` holds the 17 slices $0, 0.125, \dots, 2$. For each, the free state $N = 592$ is solved (the file name carries a thousand times the slice, with four digits), and from its JSON record the cell keeps the energy and the integrals $P = 2\,\mathrm{Vol}_7\int e^{3Hy}p\,dy$ that the solver computed on its fine grid (the key `emtIntegrals_2Vol7_int_e3Hy`), together with the slope $-3P_3 + P_t + \tfrac13P_0$ of the energy-change law.

```python
adiabatic_rows = read_rows("Revision/kohn_sham/results/adiabatic/adiabaticity.csv")
worst_e, worst_slope = 0.0, 0.0
say("a4,0       E_KS     dE/da4 (EMT)   dE/da4 (record, finite differences)")
for item in history:
    if item["a4"] in (0.0, 0.5, 1.0, 1.5, 2.0):
        key = f"N592_lam0_a{round(10 * item['a4']):02d}"
        recorded_slope = float(adiabatic_rows[key]["dE_da4_finite_difference"])
        worst_e = max(worst_e, rel(item["E"], float(summary_rows[key]["E_KS"])),
                      rel(item["p3"], float(emt_rows[key]["int_p3"])))
        worst_slope = max(worst_slope, rel(item["slope"], recorded_slope))
        say(f"{item['a4']:4.2f}  {item['E']:10.5f}  {item['slope']:12.6f}"
            f"  {recorded_slope:12.6f}")
```

At the five slices of the canonical matrix the cell compares the energy and the integrated $p_3$ with the committed tables, and the slope from the pressures with the derivative that the solver obtained by finite differences of $E$ between neighbouring slices (column `dE_da4_finite_difference` of the adiabaticity table), and prints a row for each.

```python
report("largest relative difference of E and int p3 to the record", f"{worst_e:.1e}")
report("largest relative difference of the slopes", f"{worst_slope:.1e}")
check(worst_e < 1e-12, "E_KS and the integrals at the five slices equal the record",
      record="Revision/kohn_sham/results/ground/summary.csv and emt-integrals.csv")
check(worst_slope < 1e-8, "dE/da4 = -3 P3 + P_t + P0/3 at the five slices",
      record="Revision/kohn_sham/results/adiabatic/adiabaticity.csv, column "
             "dE_da4_finite_difference")
```

Out [7] is the table of Section 15.21 for $N = 592$: the energies $361.11614$, $219.02801$, $132.84721$, $80.57590$, $48.87176$, and slopes equal to $-E_{KS}$ to all printed digits, from the pressures and from the finite differences alike; the energies and integrals equal the record exactly ($0.0$), the slopes to $6.0 \times 10^{-13}$. Both checks pass.

**In [8], the slopes integrated over the history.**

```python
slopes = np.array([item["slope"] for item in history])
energies = np.array([item["E"] for item in history])
work = simpson(slopes, 0.125)  # integral of dE/da4 over the history
change = energies[-1] - energies[0]
```

`work` is the integral of the slope over the whole history, by Simpson's rule on the 17 slices with the spacing 0.125; `change` is $E(2) - E(0)$. If the law holds, the two are equal: the energy lost along the history is the work done by the pressures.

```python
fig, ax = plt.subplots()
ax.plot(DENSE, energies, "o", color=PALETTE[0], ms=8, label="$E_{KS}$ (solver)")
for a4, e, s in zip(DENSE, energies, slopes):
    ax.plot([a4 - 0.05, a4 + 0.05], [e - 0.05 * s, e + 0.05 * s], color=PALETTE[1],
            lw=2.5)
ax.plot([], [], color=PALETTE[1], lw=2.0,
        label="slope $-3P_3 + P_t + P_0/3$ from the pressures")
ax.set_xlabel("slice $a_{4,0}$ of the history")
ax.set_ylabel("$E_{KS}$ (units of $m$)")
ax.set_title("$N = 592$, $\\lambda = 0$: the pressures give the slope of the energy")
ax.legend()
save_figure(fig, "energy_slopes",
            "The Kohn-Sham energy $E_{KS}$ of $N = 592$ without interaction "
...)
```

The energies are drawn as blue dots, and at each slice a short orange line from $a_{4,0} - 0.05$ to $a_{4,0} + 0.05$ with the slope from the pressures: the line through $(a, E)$ with slope $s$ has the end values $E \mp 0.05\,s$. This is Figure 15b.4; its caption prints the first and the last energy.

```python
worst_law = 0.0  # the identity on the 75 recorded ground states
for key, row in emt_rows.items():
    emt_slope = (-3.0 * float(row["int_p3"]) + float(row["int_p_t"])
                 + float(row["int_p0"]) / 3.0)
    recorded = float(adiabatic_rows[key]["dE_da4_finite_difference"])
    scale = max(abs(float(row["int_rho"])), 1.0)  # the energy scale of the state
    worst_law = max(worst_law, abs(emt_slope - recorded) / scale)
```

The free gas tests only the term $-3P_3$. So the cell also evaluates $-3P_3 + P_t + \tfrac13P_0$ from the committed integrals of all 75 ground states, the 60 interacting ones included, and compares it with the recorded finite differences, relative to the larger of the energy and 1 (for the free $N = 8$ states the energy is 0).

```python
report("E(2) - E(0) / integral of the slopes", f"{change:.6f} / {work:.6f}")
report("largest |(-3 P3 + P_t + P0/3) - dE/da4| / max(E, 1), 75 recorded states",
       f"{worst_law:.1e}")
check(rel(work, change) < 1e-5,
      "the integrated slope equals E(2) - E(0) within 1e-5 (relative)",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "emt_energy_change_dE_da4")
check(worst_law < 1e-8, "dE/da4 = -3 P3 + P_t + P0/3 in all 75 recorded ground states",
      record=f"{EMT_TABLE} and adiabatic/adiabaticity.csv")
```

Out [8]: $E(2) - E(0) = -312.244388$ and the integral of the slopes $-312.244811$, a relative difference of $1.4 \times 10^{-6}$, the error of Simpson's rule with the step 0.125 on the function $-E(0)e^{-a}$ (Exercise 3 computes it); and the law holds on all 75 recorded states to $9.2 \times 10^{-10}$, the value of the solver's check. Both checks pass.

**In [9], the integrated pressure ratios.**

```python
ratio3 = np.array([item["p3"] / item["rho"] for item in history])
free_dev = max(float(np.max(np.abs(ratio3 - 1.0 / 3.0))),
               max(abs(item["p0"]) + abs(item["p_t"]) for item in history)
               / min(item["rho"] for item in history))
```

`ratio3` holds $P_3/E$ at the 17 slices, and `free_dev` is the larger of the largest $|P_3/E - \tfrac13|$ and the largest $(|P_0| + |P_t|)/E$ (divided by the smallest energy, which makes it larger, not smaller).

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
tags = [("lam0", "$0$"), ("lamp1", "$+\\lambda_1$"), ("lamm1", "$-\\lambda_1$"),
        ("lamp2", "$+\\lambda_2$"), ("lamm2", "$-\\lambda_2$")]
signs_ok = True  # with interaction P_t/E and P_0/E have the sign of -lambda
for colour, (tag, label) in zip(PALETTE, tags):
    keys = [f"N592_{tag}_a{round(10 * a):02d}" for a in (0.0, 0.5, 1.0, 1.5, 2.0)]
    e = [float(emt_rows[k]["int_rho"]) for k in keys]
    r3 = [float(emt_rows[k]["int_p3"]) / x for k, x in zip(keys, e)]
    rt = [float(emt_rows[k]["int_p_t"]) / x for k, x in zip(keys, e)]
    r0 = [float(emt_rows[k]["int_p0"]) / x for k, x in zip(keys, e)]
    left.plot([0, 0.5, 1, 1.5, 2], r3, "o-", color=colour, ms=6, lw=1.5, label=label)
    right.plot([0, 0.5, 1, 1.5, 2], rt, "s--", color=colour, ms=6, lw=1.2)
    right.plot([0, 0.5, 1, 1.5, 2], r0, "o-", color=colour, ms=6, lw=1.5)
    if tag != "lam0":
        sign = -1.0 if tag.startswith("lamp") else 1.0
        signs_ok = signs_ok and all(sign * v > 0.0 for v in rt + r0)
```

For $N = 592$ and the five couplings the cell reads the committed integrals at the five slices and draws $P_3/E$ on the left, $P_t/E$ (squares, dashed) and $P_0/E$ (circles) on the right. For the interacting couplings it checks the sign: `sign` is $-1$ for $+\lambda$ and $+1$ for $-\lambda$, and every ratio times `sign` must be positive (`rt + r0` joins the two lists).

```python
left.axhline(1.0 / 3.0, color="0.4", ls=":", lw=1.2)
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("$P_3 / E$")
left.set_title("3-space pressure, $N = 592$ (dotted: $1/3$)")
left.legend(fontsize=8)
right.axhline(0.0, color="0.4", lw=0.8)
right.plot([], [], "s--", color="0.4", label="$P_t / E$")
right.plot([], [], "o-", color="0.4", label="$P_0 / E$")
right.set_xlabel("slice $a_{4,0}$")
right.set_ylabel("ratio of integrals")
right.set_title("Extra-time and hidden pressures, $N = 592$")
right.legend(fontsize=8)
save_figure(fig, "integrated_ratios",
            "Left: the integrated 3-space pressure divided by the energy, "
...)
report("free gas: largest |P3/E - 1/3| and (|P_0| + |P_t|)/E at 17 slices",
       f"{free_dev:.1e}")
check(free_dev < 1e-12, "the free gas has P3 = E/3 and P0 = P_t = 0 at all 17 slices",
      record=f"{EMT_TABLE}, columns int_rho, int_p3, int_p_t, int_p0")
check(signs_ok, "with interaction P_t/E and P0/E have the sign of -lambda, N = 592")
```

The value $\tfrac13$ as a dotted line, the zero line, the legend entries for the two line styles, and `save_figure` for Figure 15b.5. Out [9]: the free gas deviates from $P_3 = E/3$, $P_0 = P_t = 0$ by $5.0 \times 10^{-16}$ at the 17 slices; both checks pass.

**In [10], where the energy sits.**

```python
fig, ax = plt.subplots()
means, worst_shape = [], 0.0
for shade, a4 in zip(SLICE_SHADES, (0.0, 0.5, 1.0, 1.5, 2.0)):
    p = read_profile(repository_file(f"{RECORD_PROFILES}/N592_lam0_a"
                                     f"{round(10 * a4):02d}.csv"))
    density = 2.0 * vol7(a4) * np.exp(3.0 * H * p["y"]) * p["rho"]
    density = density / simpson(density, step)  # area 1
    fm = math.exp(-a4 / 3.0)  # f M with M = m = 1
    exact = 2.0 * fm * np.exp(2.0 * fm * p["y"]) / (1.0 - math.exp(-2.0 * fm * 3.0))
    worst_shape = max(worst_shape, float(np.max(np.abs(density - exact)))
                      / float(np.max(exact)))
    means.append(simpson(p["y"] * density, step))
    ax.plot(p["y"], density, color=shade, lw=2.0, label=f"$a_{{4,0}} = {a4}$")
```

For the free state $N = 592$ at the five slices the cell reads the committed profile and forms the energy per unit $y$, $2\,\mathrm{Vol}_7e^{3Hy}\rho$, divided by its integral, so that its area is 1. Every occupied orbital of the free gas is a fold-band orbital $(Ae^{fMy}, 0)$, so its energy per unit $y$ is $\kappa k$ times $A^2e^{2fMy}$, the same shape for every shell; normalised, it is `exact` $= 2fM\,e^{2fMy}/(1 - e^{-2fML})$ with $fM = e^{-a_{4,0}/3}$ (`fm`) and $L = 3$. `worst_shape` is the largest deviation from it, relative to its maximum, and `means` collects the mean position $\langle y\rangle = \int y\,(\text{density})\,dy$.

```python
ax.set_xlabel("hidden coordinate $y$")
ax.set_ylabel("$2\\,\\mathrm{Vol}_7 e^{3Hy}\\rho / E_{KS}$ (units of $m$)")
ax.set_title("The energy spreads toward the tip along the history")
ax.legend()
save_figure(fig, "energy_spreading",
            "The energy per unit $y$ divided by the total energy, "
...)
report("largest deviation from 2fM e^{2fMy}/(1 - e^{-2fML}), relative",
       f"{worst_shape:.1e}")
report("mean position <y> of the energy at the five slices",
       ", ".join(f"{m:.4f}" for m in means))
check(worst_shape < 1e-6 and all(means[i + 1] < means[i] for i in range(4)),
      "the energy follows e^{2fMy} and moves toward the tip from slice to slice")
```

`save_figure` saves Figure 15b.6. Out [10]: the largest relative deviation from the exact shape is $1.4 \times 10^{-8}$ (the rounding of the profile file and Simpson's rule on 151 points), and the mean position moves from $-0.4925$ at the first slice to $-0.8294$ at the last: the energy spreads toward the tip as the hidden scale $f$ shrinks. The check passes.

**In [11], the interaction terms.**

```python
hartree = LAMBDA2_592 * 15.0 / 32.0 * sp["S"] ** 2  # (15/32) lambda S^2
exchange = -LAMBDA2_592 / 32.0 * sp["n"] ** 2  # -(1/32) lambda n^2
fig, ax = plt.subplots()
ax.plot(sp["y"], sp["e_int"], color=PALETTE[0], lw=3.0, label="$e_{int} = p_t$")
ax.plot(sp["y"], hartree, color=PALETTE[1], lw=1.5, ls="--",
        label="$\\frac{15}{32}\\lambda S^2$")
ax.plot(sp["y"], exchange, color=PALETTE[2], lw=1.5, ls="--",
        label="$-\\frac{1}{32}\\lambda n^2$")
ax.set_yscale("symlog", linthresh=1e-5)
ax.set_xlabel("hidden coordinate $y$")
ax.set_ylabel("proper energy density (units of $m^8$)")
ax.set_title("Interaction energy density, $N = 592$, $+\\lambda_2$, $a_{4,0} = 2$")
ax.legend()
save_figure(fig, "interaction_terms",
            "The interaction energy density $e_{int}$, which is also the extra-time "
...)
```

From the profile of the interacting state the cell computes the two parts of $e_{int}$ (Section 15.2): the term $\tfrac{15}{32}\lambda S^2$ (named `hartree`, although it contains the scalar part of the exchange, Section 15.2) and the exchange term $-\tfrac{1}{32}\lambda n^2$, and draws them with $e_{int}$ on a symmetric logarithmic axis (linear between $-10^{-5}$ and $10^{-5}$). This is Figure 15b.7.

```python
sum_error = float(np.max(np.abs(hartree + exchange - sp["e_int"]))) / float(
    np.max(np.abs(sp["e_int"])))
report("largest |e_int - (15/32 lambda S^2 - 1/32 lambda n^2)| / max|e_int|",
       f"{sum_error:.1e}")
check(sum_error < 1e-12 and bool(np.all(sp["p_t"] == sp["e_int"])),
      "e_int = lambda (15/32 S^2 - 1/32 n^2) and p_t = e_int")
```

`sum_error` compares the column $e_{int}$ with the sum of the two parts. Out [11]: $3.7 \times 10^{-16}$, and $p_t$ equals $e_{int}$ exactly at every point (`np.all(... == ...)` compares every pair of numbers). The check passes.

```python
signs = [(float(row["lambda"]), float(row["int_p_t"])) for key, row in emt_rows.items()
         if "_lam0_" not in key]  # the 60 interacting ground states
opposite = sum(1 for lam, value in signs if lam * value < 0.0)
report("interacting states / states with P_t of the sign of -lambda",
       f"{len(signs)} / {opposite}")
check(len(signs) == 60 and opposite == 60,
      "the integrated extra-time pressure has the sign of -lambda in all 60 states",
      record=f"{EMT_TABLE}, column int_p_t")
```

For the 60 interacting ground states of the record the cell pairs the coupling with the integrated extra-time pressure and counts the states where the product is negative, that is, where $P_t$ has the sign of $-\lambda$. Out [11]: 60 of 60. The scalar density of the fold-band orbitals is zero, and the interaction creates only a small one, so the exchange term $-\tfrac{1}{32}\lambda n^2$ dominates $e_{int}$ everywhere: by the energy-change law the deflation of the extra times takes energy from every repulsive gas and gives energy to every attractive one. The check passes.

**In [12], the source conditions.**

```python
import re  # finds the numbers inside the record's text

SOURCE = "Revision/field_equations_a4/reports/ks-source-conditions.json"
source = json.loads(repository_file(SOURCE).read_text(encoding="utf-8"))
details = {item["name"]: item["detail"] for item in source["checks"]}
```

`re` is Python's module for **regular expressions**, patterns that find pieces of text; the cell uses it to read the numbers that the record prints inside the details of its checks. `details` maps each check name of the source-conditions record to its detail text.

```python
def condition_ratios(p):
    scale = max(float(np.max(np.abs(p[c]))) for c in ("rho", "p3", "p_t", "p0"))
    if scale == 0.0:
        return None
    return ((float(np.max(p["rho"])) - float(np.min(p["rho"]))) / scale,
            float(np.max(np.abs(p["p0"] - p["p_t"]))) / scale)
```

`condition_ratios` returns, for one profile, the two measures of the record: $(\max\rho - \min\rho)/\max|T|$ for C1 (zero if $\rho$ does not depend on $y$) and $\max_y|p_0 - p_t|/\max|T|$ for C2; for a vanishing tensor it returns `None` (nothing).

```python
ratios = {}
for path in sorted(repository_file(RECORD_PROFILES).glob("*.csv")):
    values = condition_ratios(read_profile(path))
    if values is not None:
        ratios[path.stem] = values
c1_min = min(ratios, key=lambda k: ratios[k][0])
free_c2 = max(v[1] for k, v in ratios.items() if "_lam0_" in k)
lam_c2 = min((k for k in ratios if "_lam0_" not in k), key=lambda k: ratios[k][1])
mine = {name: condition_ratios(p) for name, p in (("N592_lam0_a10", prof),
                                                   ("N592_lamp2_a20", sp))}
```

The loop runs over the 75 committed profile files (`glob("*.csv")` lists them, `sorted` fixes their order) and keeps the two measures of every nonzero one under its state name (`path.stem` is the file name without `.csv`). `c1_min` is the state with the smallest C1 measure, `free_c2` the largest C2 measure among the free states, `lam_c2` the interacting state with the smallest C2 measure, and `mine` the two measures of this notebook's own states.

```python
number = r"(-?[0-9.]+(?:e[-+]?[0-9]+)?)"  # a number as the record prints it
rec_c1 = re.search(rf"max\|T\| >= {number} \(smallest: (\w+)\)",
                   details["ks_profiles_depend_on_x0"])
rec_c2 = re.search(rf"largest {number}\).*smallest: {number} at (\w+)\)",
                   details["ks_hidden_pressure_condition"])
need = re.search(rf"a4,0 = 0 \(kk = 1\): kappa rho = {number}, p3/rho = {number}, "
                 rf"p0/rho = p_t/rho = {number}", details["ks_history_is_a_prescribed_"
                                                          "background"])
late = re.search(rf"a4,0 = 2 \(kk = [0-9.]+\): kappa rho = {number}",
                 details["ks_history_is_a_prescribed_background"])
same6 = lambda a, b: abs(a - float(b)) <= 5e-6 * abs(float(b))  # 6 digits
```

`number` is a pattern for a number as the record prints it: an optional minus sign, digits and points, and an optional exponent (the parentheses capture the number so that it can be read back with `group`). `re.search` finds the first place where a pattern occurs in a text; the patterns are written as **raw f-strings** (`rf"..."`), in which a backslash is kept as typed and the braces insert `number`; `\|` is a literal bar, `\(` a literal parenthesis, `\w+` a word (the state name) and `.*` any text in between. `rec_c1` reads the smallest C1 ratio and its state, `rec_c2` the largest free and the smallest interacting C2 ratio and its state, `need` the energy density $\kappa\rho$ and the ratios $p_3/\rho$, $p_0/\rho = p_t/\rho$ that the history needs at $a_{4,0} = 0$, and `late` the needed $\kappa\rho$ at $a_{4,0} = 2$. `same6` asks whether a computed number agrees with a printed one to six significant digits.

```python
report("nonzero profiles / with lambda = 0", f"{len(ratios)} / "
       f"{sum(1 for k in ratios if '_lam0_' in k)}")
report("C1: smallest (max rho - min rho)/max|T| (state)",
       f"{ratios[c1_min][0]:.6g} ({c1_min})")
report("C2: largest ratio with lambda = 0 / smallest with lambda != 0 (state)",
       f"{free_c2:.4e} / {ratios[lam_c2][1]:.6g} ({lam_c2})")
report("this notebook's states: C1 and C2 ratios", "; ".join(
    f"{k}: {v[0]:.4f}, {v[1]:.2e}" for k, v in mine.items()))
report("C4: the history needs at a4,0 = 0 kappa rho, p3/rho, p0/rho = p_t/rho",
       f"{need.group(1)}, {need.group(2)}, {need.group(3)}; kappa rho at 2: "
       f"{late.group(1)}")
```

Out [12] reports 70 nonzero profiles, 10 of them free; the smallest C1 ratio $0.456213$ (`N592_lamm2_a20`); the largest free C2 ratio $4.7533 \times 10^{-17}$ (rounding) and the smallest interacting one $0.080929$ (`N2352_lamm1_a00`); this notebook's states with C1 ratios $0.9909$ and $0.9984$ and C2 ratios $1.79 \times 10^{-17}$ and $0.771$; and the source that the history needs: $\kappa\rho = 3.57407$, $p_3/\rho = -1.26713$, $p_0/\rho = p_t/\rho = -2.38212$ at $a_{4,0} = 0$, and $\kappa\rho = -7.63383$ at $a_{4,0} = 2$.

```python
check(same6(ratios[c1_min][0], rec_c1.group(1)) and c1_min == rec_c1.group(2)
      and mine["N592_lam0_a10"][0] > 0.4 and mine["N592_lamp2_a20"][0] > 0.4,
      "C1 fails for every nonzero profile; the record's smallest ratio reproduced",
      record=f"{SOURCE}, check ks_profiles_depend_on_x0")
check(free_c2 <= 1e-12 and same6(ratios[lam_c2][1], rec_c2.group(2))
      and lam_c2 == rec_c2.group(3) and mine["N592_lamp2_a20"][1] > 0.08,
      "C2 holds for lambda = 0 and fails for lambda != 0; the record reproduced",
      record=f"{SOURCE}, check ks_hidden_pressure_condition")
check(float(need.group(1)) > 0.0 > float(late.group(1))
      and abs(float(need.group(2)) - 1.0 / 3.0) > 1.0 and free_dev < 1e-12,
      "C4 fails: the free gas has P3/E = 1/3, P0 = P_t = 0, the history needs others",
      record=f"{SOURCE}, check ks_history_is_a_prescribed_background")
```

The three checks pass: C1 fails for every nonzero profile (the record's smallest ratio and its state are reproduced, and both states of this notebook vary strongly with $y$); C2 holds for the free states and fails for every interacting one (reproduced, with this notebook's interacting state far above the threshold); and the source of C4 changes sign along the history and has $p_3/\rho$ more than 1 away from the free gas's $\tfrac13$ (with `free_dev` from In [9]). This is the reason, computed on the notebook's own numbers and on the record, why the history is a PRESCRIBED BACKGROUND (Section 15.16).

**In [13], the last check.**

```python
NAMES = ["proper_emt", "coordinate_emt", "y_conservation", "energy_slopes",
         "integrated_ratios", "energy_spreading", "interaction_terms"]
missing = [name for number, name in enumerate(NAMES, start=1)
           if not output_file(f"{FIGURE_FOLDER}/15b_{number}_{name}.png").is_file()]
check(missing == [], "every figure file of this notebook exists")
all_checks_passed()
```

The same as the last cell of Notebook 15e (Section 15.9), with the seven figure names of this notebook. The cell prints PASS every figure file of this notebook exists and ALL 20 CHECKS PASSED (notebook 15b).

### 15.21 Adiabaticity: does the gas follow the moving background?

**The question.** Every state computed so far is an **instantaneous** state: at the slice $a_{4,0}$ the solver finds the ground state of the Hamiltonian $h(a_{4,0})$ of that instant, as if the background stood still. But it does not stand still: along the history $a_4 = AHx_4$ grows with the time $x_4$, 3-space inflates, and the extra times and the hidden direction shrink. A system whose Hamiltonian changes slowly enough stays in the eigenstate that continues its initial one (the **adiabatic theorem** of quantum mechanics; Chapter 14 introduced this adiabatic picture); a system whose Hamiltonian changes too fast is kicked into higher levels. Which case applies here must be measured.

**The exact evolution keeps the sector.** In the mean field the orbitals obey exactly (ks-theory.json, adiabaticity.exactEvolution; check ansatz_removes_spin_connection, which holds for time-dependent $a_4$ and $b_4$; Chapter 14)

$$
i\,\frac{\partial\chi}{\partial x_4} = h\big(a_4(x_4)\big)\,\chi, \qquad h_j = j\Big[-\frac{i}{f}\sigma_1\frac{d}{dy} + M\sigma_2 + \kappa k\sigma_3\Big] + v, \qquad \kappa = e^{-a_4(x_4)},\quad f = e^{-a_4(x_4)/3} .
$$

At every instant $h$ acts within one block, at one 3-momentum, and keeps the fold condition; so the evolution never moves a particle to another momentum, block type or fold condition. **Transitions are possible only inside a sector**, between the levels of one $(n_2, j, \text{fold condition})$. Notebook 15a showed that each of the lowest particle-hole excitations of the gas (up to 24 per state, 1687 in all) changes the sector (Section 15.15); the in-sector jumps are much more expensive: the one with the largest $Q$ (below) costs between $0.633\,m$ and $2.290\,m$.

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

Rule: differentiate $h\phi_n = \varepsilon_n\phi_n$: $\dot h\phi_n + h\dot\phi_n = \dot\varepsilon_n\phi_n + \varepsilon_n\dot\phi_n$; take the inner product with $\phi_m$, where $\langle m|h\dot\phi_n\rangle = \varepsilon_m\langle m|\dot\phi_n\rangle$ ($h$ is self-adjoint, Section 15.2) and $\langle m|\phi_n\rangle = 0$; solve for $\langle m|\dot\phi_n\rangle$; finally $\dot h = \dot a_4\,\partial h/\partial a_4$ (chain rule; on the history $b_4$ is a function of $a_4$), written $\partial_a h$ (check adiabatic_offdiagonal_identity).

$$
|c_m| \approx \Big|\int \dot a_4\,\frac{\langle m|\partial_a h|n\rangle}{\varepsilon_n - \varepsilon_m}\,e^{i(\varepsilon_m - \varepsilon_n)x_4}\,dx_4\Big| \approx \dot a_4\,\frac{|\langle m|\partial_a h|n\rangle|}{(\varepsilon_n - \varepsilon_m)^2} .
$$

Rule: start with $c_n = 1$ and all other $c$ zero, and keep on the right of the third line only the term of the occupied orbital $n$ (first order); over a short stretch of time the factor in front of the exponential hardly changes, and $\int e^{i\omega x_4}dx_4 = e^{i\omega x_4}/(i\omega)$, whose size is $1/|\omega|$ with $\omega = \varepsilon_m - \varepsilon_n$.

With $\dot a_4 = AH$ this is the **adiabaticity measure** of the record (ks-theory.json, adiabaticity.measure):

$$
Q_{nm} = AH\,\frac{|\langle n|\partial_a h|m\rangle|}{(\varepsilon_n - \varepsilon_m)^2}, \qquad \text{transition probability} \approx Q_{nm}^2 ,
$$

for $n$ occupied and $m$ empty in the same sector. The evolution is adiabatic when every $Q_{nm} \ll 1$. This is an estimate of first order, not a solution of the time-dependent problem, which stays OPEN.

**The derivative of the Hamiltonian.** Without interaction two things in $h_j$ depend on $a_4$: the momentum weight and the hidden scale. Line by line:

$$
\frac{\partial\kappa}{\partial a_4} = -\kappa, \qquad \frac{\partial}{\partial a_4}\frac1f = \frac{\partial}{\partial a_4}e^{(1 - \beta/2)a_4} = \Big(1 - \frac\beta2\Big)\frac1f = \frac13\cdot\frac1f .
$$

Rule: the derivative of $e^{ca}$ is $ce^{ca}$; $f = e^{(\beta/2 - 1)a_4}$ on the history (Section 15.1), so $1/f = e^{(1 - \beta/2)a_4}$, and $1 - \beta/2 = \tfrac13$ for $\beta = \tfrac43$.

$$
\partial_a h_j = -j\kappa k\,\sigma_3 + \tfrac13\,T_j, \qquad T_j = j\Big(-\frac{i}{f}\sigma_1\frac{d}{dy}\Big) .
$$

Rule: differentiate $h_j$ term by term; $M = m$ and $v = 0$ do not depend on $a_4$ without interaction. The second term, one third of the kinetic term, comes from the shrinking hidden direction (ks-theory.json, adiabaticity.derivative). The kinetic term needs no derivative of an orbital, because the eigen-equation gives it:

$$
T_j\phi_m = \big(\varepsilon_m - v - jM\sigma_2 - j\kappa k\sigma_3\big)\,\phi_m .
$$

Rule: $h_j\phi_m = \varepsilon_m\phi_m$ with $h_j = T_j + j(M\sigma_2 + \kappa k\sigma_3) + v$; move the other terms to the right. For real orbitals $\chi = (a, ib)$ the three products are, with $s_0 = a_na_m + b_nb_m$, $s_2 = a_nb_m + b_na_m$, $s_3 = a_na_m - b_nb_m$ (rule: multiply as in Section 14.12),

$$
\chi_n^\dagger\chi_m = s_0, \qquad \chi_n^\dagger\sigma_2\chi_m = s_2, \qquad \chi_n^\dagger\sigma_3\chi_m = s_3 ,
$$

and therefore, for $v = 0$,

$$
\langle n|\partial_a h|m\rangle = \int_{-L}^{0}\Big[-j\kappa k\,s_3 + \tfrac13\big(\varepsilon_m s_0 - jM s_2 - j\kappa k\,s_3\big)\Big]dy .
$$

Rule: insert the previous lines into $\int\chi_n^\dagger\,\partial_a h\,\chi_m\,dy$. The kinetic part acts even at $k = 0$: unlike in the metric of 2026-10-14 (withdrawn on 2026-10-16), where only $\kappa$ depended on $a_4$, the zero modes now feel the history, because the hidden direction they live in shrinks. With interaction the self-consistent potentials change with $a_4$ too, and $\partial_a h$ gains $j(\partial_aM)\sigma_2 + \partial_av$, which the solver obtains from the states at $a_{4,0} \pm \delta$ and $\pm 2\delta$ (they contain the change of the effective coupling $\hat\lambda/\mathrm{Vol}_7$ along the history).

**Hellmann-Feynman.** For $m = n$ the same differentiation gives the **Hellmann-Feynman theorem** of Chapter 13 (and Section 14.19), $d\varepsilon_n/da_4 = \langle n|\partial_a h|n\rangle$ (take the inner product of the differentiated eigen-equation with $\phi_n$ itself; the terms with $\dot\phi_n$ cancel because $h$ is self-adjoint and $\langle n|n\rangle = 1$). For a fold-band orbital $(Ae^{fMy}, 0)$ with $\varepsilon = \kappa k$: $s_0 = s_3 = a^2$, $s_2 = 0$, so $\langle n|\partial_a h|n\rangle = -\kappa k + \tfrac13(\kappa k - \kappa k) = -\kappa k$, the derivative of $\kappa k = ke^{-a_4}$, as it must be. Summed over the occupied levels it gives $dE/da_4 = \sum gf_o\langle n|\partial_a h|n\rangle = -E_{KS}$ for the free gas, the same as the energy-change law of Section 15.16 (check adiabatic_hellmann_feynman of `Revision/kohn_sham/reports/ks-theory-python.json`; the solver checks the self-consistent version for all 75 states, worst deviation $6.444 \times 10^{-11}\,m$, check adiabatic_hellmann_feynman of `Revision/kohn_sham/reports/ks-rust-solver.json`).

**What the record finds** (COMPUTED; `Revision/kohn_sham/results/adiabatic/adiabaticity.csv`, reproduced by Notebook 15c). Over the whole canonical matrix $Q_{max} \le 0.1982205$ (state N2352_lamm1_a00), so every transition probability is below $0.04$. In every free state the largest $Q$ belongs to the jump from the fold-band level of the highest occupied shell to the first bulk level of the same sector (for $N = 592$ at $a_{4,0} = 0$: $Q = 0.1396883$, with the energy difference $0.8591647\,m$), and for $N = 8$ to the jump of a zero mode to the first even bulk level at $k = 0$ ($Q = 0.06814928$ at $a_{4,0} = 0$): the shrinking hidden direction acts on the zero modes too. $Q_{max}$ falls along the history: the energy differences of the jumps grow, because the bulk levels rise as the hidden direction shrinks, faster than the matrix elements grow. Reading (labelled interpretation): within the sectors, the instantaneous states are followed adiabatically only in the weak sense $Q_{max} < 1$; the largest values approach 0.2 at the start of the history for $N = 2352$.

**Fermi-level crossings.** Adiabatic evolution keeps the occupation of every level. If along the history an empty level of one sector comes down below an occupied level of another sector, the instantaneous ground state (aufbau) would move particles from one to the other, but the evolution cannot: the two levels lie in different sectors. Such a **Fermi-level crossing** makes the instantaneous ground state the wrong state. The canonical matrix has none (the record file `adiabatic/fermi-level-crossings.csv`: no change of the occupied set in any of its 60 rows). The record demonstrates the effect with $N = 2360 = 2352 + 8$, the smallest closed shell of the first slice that occupies a level off the fold band (check adiabatic_crossing_flag_demonstration): at $a_{4,0} = 0$ the eight extra particles sit in the odd bulk level at $k = 0$ ($\varepsilon = 1.2923$), while the fold-band level of the shell $n_2 = 27$ ($k = 1.2990$, 128 orbitals) lies only $0.0067\,m$ above it. Along the history the band level comes down like $ke^{-a_{4,0}}$ and the bulk level goes up (the hidden direction shrinks), so they cross almost at once, near $a_{4,0} = 0.0047$; after the crossing the adiabatically continued state lies above the instantaneous aufbau state by $4.68\,m$ at $a_{4,0} = 0.5$, growing to $12.48\,m$ at $a_{4,0} = 2$ (`adiabatic/crossing-demo.csv`). There the instantaneous picture fails.

### 15.22 Example: the adiabaticity measure (Notebook 15c)

Notebook 15c needs no Rust. It defines the solver's shooting method for the free problem in Python, with the hidden scale of the slice, solves again all 570 levels of the occupied sectors of the free states $N = 8$, $592$ and $2352$ at the five slices, and computes $Q_{nm}$ for every allowed pair. It draws the two orbitals of the pair with the largest $Q$ of $N = 592$ and the momentum and kinetic parts of the integrand of their matrix element (Figure 15c.1), every $Q$ against the shell (Figure 15c.2), $Q_{max}$ of the whole matrix along the history (Figure 15c.3), the Hellmann-Feynman theorem (Figure 15c.4), the Fermi-level crossing of $N = 2360$ (Figure 15c.5) and a heat map of $Q_{max}$ (Figure 15c.6). It takes less than half a minute and ends with ALL 12 CHECKS PASSED (notebook 15c).

What to look for: in Figure 15c.1 that the band orbital sits at the fold while the bulk orbital fills the interval, and that the kinetic part of the integrand is not small; in Figure 15c.2 the triangles of the zero modes at $n_2 = 0$, which are there only because the hidden direction shrinks, and that all points lie below 0.2; in Figure 15c.5 how quickly the band level crosses the rising bulk level.

<!-- NOTEBOOK 15c -->

### 15.25 Line-by-line walk-through of Notebook 15c

The notebook has 11 code cells, In [1] to In [11]. As in Section 15.9, docstrings are left out of the quotations, and long caption strings in calls of `save_figure` are shortened: the quotation shows the first line of the call and the first line of the caption, and then a line `...)` that stands for the rest of the caption and the closing parenthesis; the complete cells are printed in Section 15.24.

**In [1], the set-up cell.** It is the set-up cell of Notebook 15e, explained line by line in Section 15.9, with the run instructions of this notebook (Section 15.23) in its comments and `NOTEBOOK_ID = "15c"`.

**In [2], the solver's method for the free problem.**

```python
import csv  # reads the tables (CSV files) of the Revision record
import math  # exp, sqrt, atan2, pi for single numbers

import numpy as np  # arrays of numbers

L, STEPS = 3.0, 900  # tip cutoff and number of RK4 steps (the solver's values)
BETA = 4.0 / 3.0  # the history b4 = e^{beta a4} of the record
CKIN = 1.0 - 0.5 * BETA  # the weight 1/3 of the kinetic term in d_a h
POINTS = 2 * STEPS + 1  # step ends and midpoints
STEP = L / STEPS
```

The imports and the grid of the solver: $L = 3$, $G = 900$ steps of length $h = 1/300$, $2G + 1 = 1801$ fine points. `BETA` is $\beta = \tfrac43$ of the history, and `CKIN` is the weight $1 - \beta/2 = \tfrac13$ of the kinetic term in $\partial_a h$ (Section 15.21).

```python
Y = np.array([-L * ((POINTS - 1 - f) / (POINTS - 1)) for f in range(POINTS)])
SIMPSON = np.full(POINTS, 2.0 * STEP / 6.0)  # Simpson weights on the fine grid
SIMPSON[1::2] = 4.0 * STEP / 6.0
SIMPSON[0] = SIMPSON[-1] = STEP / 6.0
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
```

`Y` holds the fine points from $-3$ to $0$ (the same formula as in Notebook 15e, Section 15.9), and `SIMPSON` the Simpson weights $\tfrac{h}{6}(1, 4, 2, 4, \dots, 4, 1)$: all entries first $\tfrac{2h}{6}$, then every odd entry $\tfrac{4h}{6}$, then the two ends $\tfrac{h}{6}$.

```python
def coefficients(eps, k, j, a4):
    fh = math.exp((0.5 * BETA - 1.0) * a4)  # the hidden scale f = e^{-a4/3}
    return fh * 1.0, fh * (k * math.exp(-a4)), fh * j * eps, fh
```

`coefficients` returns the three coefficients $fM$, $f\kappa k$ and $fj\varepsilon$ of the free block ($M = m = 1$, $v = 0$) at the slice, and the hidden scale $f$ itself. In the free problem the three coefficients are the same at every point, so every RK4 stage uses the same three numbers.

```python
def shoot(eps, k, j, a4, store=False):
    m_y, kk, je, fh = coefficients(eps, k, j, a4)
    a, b, theta, raw, area, r2_prev = 1.0, 0.0, 0.0, 0.0, 0.0, 1.0
    nodes = [(a, b)] if store else None
    for i in range(STEPS):
        p1a, p1b = m_y * a - (kk + je) * b, (je - kk) * a - m_y * b  # (a', b')
        aa, bb = a + 0.5 * STEP * p1a, b + 0.5 * STEP * p1b
        p2a, p2b = m_y * aa - (kk + je) * bb, (je - kk) * aa - m_y * bb
        aa, bb = a + 0.5 * STEP * p2a, b + 0.5 * STEP * p2b
        p3a, p3b = m_y * aa - (kk + je) * bb, (je - kk) * aa - m_y * bb
        aa, bb = a + STEP * p3a, b + STEP * p3b
        p4a, p4b = m_y * aa - (kk + je) * bb, (je - kk) * aa - m_y * bb
        a += STEP / 6.0 * (p1a + 2.0 * p2a + 2.0 * p3a + p4a)
        b += STEP / 6.0 * (p1b + 2.0 * p2b + 2.0 * p3b + p4b)
```

`shoot` is the shooting of Notebook 15e (Section 15.9, In [3]) for constant coefficients, written out: the start values at the tip, $(a, b) = (1, 0)$, the angles, the integral of $r^2$ and $r^2 = 1$ are set in one line; each step computes the four RK4 slopes `p1` to `p4` from the block equation $a' = fMa - (f\kappa k + fj\varepsilon)b$, $b' = (fj\varepsilon - f\kappa k)a - fMb$ at the start, twice at the midpoint and at the end (`aa`, `bb` are the predicted intermediate points), and advances $a$ and $b$.

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
    return j * theta, fh * area / r2_prev, nodes  # Phi and f int r^2 / r(0)^2
```

The Pruefer angle is followed continuously and $\int r^2dy$ is added up with the trapezoid rule, as in Notebook 15e. The function returns $\Phi = j\,\theta(0)$, the derivative $d\Phi/d\varepsilon = f\int r^2dy/r(0)^2$ and, if asked, the values at the step ends.

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

`find_level` is the solver's safeguarded Newton method (Section 15.3; Notebook 15e, In [5]) in a compact form: the target of the label ($l\pi$ for the even, $\pi/2 + l\pi$ for the odd fold condition), the value $g = \Phi - t_l$ and its derivative $d$ at the guess (`[:2]` keeps the first two results of `shoot`), and the first trial step.

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

The walk with doubling steps until the target is bracketed, upward or downward, keeping the better end for Newton's method, exactly as in Notebook 15e.

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

The refinement: Newton steps, replaced by bisection when they would leave the bracket or did not halve the mismatch, until the bracket is shorter than $10^{-13}$, the mismatch is exactly zero, or a Newton step moved the energy by less than the tolerance (Section 15.3).

```python
def orbital(eps, k, j, a4):
    nodes = np.array(shoot(eps, k, j, a4, store=True)[2])
    m_y, kk, je, _ = coefficients(eps, k, j, a4)
    a_n, b_n = nodes[:, 0], nodes[:, 1]
    da = m_y * a_n - (kk + je) * b_n  # derivatives at the step ends
    db = (je - kk) * a_n - m_y * b_n
    a = np.zeros(POINTS)
    b = np.zeros(POINTS)
    a[0::2], b[0::2] = a_n, b_n
    a[1::2] = 0.5 * (a_n[:-1] + a_n[1:]) + STEP / 8.0 * (da[:-1] - da[1:])
    b[1::2] = 0.5 * (b_n[:-1] + b_n[1:]) + STEP / 8.0 * (db[:-1] - db[1:])
    norm = math.sqrt(float(np.sum(SIMPSON * (a * a + b * b))))
    return a / norm, b / norm
```

`orbital` returns the normalised orbital on the fine grid: the values at the step ends from `shoot` (`nodes[:, 0]` is the first column of the array of pairs, the values of $a$), the derivatives there from the block equation, the cubic Hermite midpoints of Section 15.3 and the Simpson normalisation, as in Notebook 15e (In [7]); the underscore receives $f$, which is not needed here.

```python
def da_h(k, j, a4, first, second, eps_second, parts=False):
    kk = k * math.exp(-a4)  # kappa k
    s3 = first[0] * second[0] - first[1] * second[1]
    s2 = first[0] * second[1] + first[1] * second[0]
    s0 = first[0] * second[0] + first[1] * second[1]
    momentum = -j * kk * s3  # from d kappa / d a4 = -kappa
    kinetic = CKIN * (eps_second * s0 - j * 1.0 * s2 - j * kk * s3)  # (1/3) T_j
    if parts:
        return momentum, kinetic  # the two integrands on the fine grid
    return float(np.sum(SIMPSON * (momentum + kinetic)))
```

`da_h` computes the matrix element $\langle n|\partial_a h|m\rangle$ of Section 15.21 between two orbitals `first` $= (a_n, b_n)$ and `second` $= (a_m, b_m)$, with `eps_second` $= \varepsilon_m$: the products $s_3$, $s_2$, $s_0$ on the fine grid, the momentum part $-j\kappa k\,s_3$ and the kinetic part $\tfrac13(\varepsilon_ms_0 - jMs_2 - j\kappa k\,s_3)$ with $M = 1$. With `parts=True` it returns the two integrands (for Figure 15c.1), otherwise their integral by Simpson's rule. Out [2] is empty: the cell defines functions only.

**In [3], the levels of the record solved again.**

```python
LEVELS = "Revision/kohn_sham/results/ground/levels"
SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]


def state_id(n, a4, tag="lam0"):
    return f"N{n}_{tag}_a{round(10 * a4):02d}"
```

The folder of the level tables, the five slices, and the state names (Section 15.14, with the coupling tag last and `lam0` by default).

```python
def solve_state(n, a4):
    rows = list(csv.DictReader(open(repository_file(f"{LEVELS}/{state_id(n, a4)}.csv"),
                                    newline="", encoding="utf-8")))
    sectors = {}
    for row in rows:
        sector = (int(row["n2"]), int(row["j"]), row["parity"])
        sectors.setdefault(sector, []).append(row)
```

`solve_state` reads the level table of a free state (one row per level: its shell, number $r_3$ of momentum vectors, $k$, $j$, fold condition in the column `parity`, label, energy and occupation) and groups the rows by sector, $(n_2, j, \text{fold condition})$.

```python
    solved, worst = {}, 0.0
    for sector in sorted(sectors):  # the solver's order: n2, then j, then parity
        members = sectors[sector]
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

Only the sectors that hold a particle matter (a transition starts at an occupied level); in each of them every level of the record is solved again, starting from the recorded energy, and kept with its occupation, momentum, $r_3$ and orbital under its label. `sorted(sectors)` visits the sectors in the solver's order (shell, then block type with $j = -1$ first, then the fold condition with `even` first, the order of the sorted tuples). The function returns the solved sectors and the largest difference to the record.

```python
states = {}
worst_level = 0.0
for n in (8, 592, 2352):
    for a4 in SLICES:
        states[(n, a4)], worst = solve_state(n, a4)
        worst_level = max(worst_level, worst)
count = sum(len(levels) for state in states.values() for levels in state.values())
report("levels solved again (15 states)", count)
report("largest |eps(Python) - eps(solver)|", f"{worst_level:.1e}")
check(worst_level < 1e-12, "every level equals the solver's level within 1e-12",
      record=f"{LEVELS}/N8_lam0_a*.csv, N592_lam0_a*.csv and N2352_lam0_a*.csv, "
             "column eps")
```

The fifteen free states are solved. Out [3]: 570 levels, the largest difference to the solver's levels $7.1 \times 10^{-15}$; the check passes.

**In [4], the pair with the largest $Q$.**

```python
sector = (10, 1, "even")
band = states[(592, 0.0)][sector][0]  # (eps, f, k, r3, (a, b)) of label 0
bulk = states[(592, 0.0)][sector][1]  # label 1
k = band[2]
momentum, kinetic = da_h(k, 1, 0.0, band[4], bulk[4], bulk[0], parts=True)
```

The sector of the largest $Q$ of $N = 592$ at the first slice: the shell $n_2 = 10$ ($k = 0.25\sqrt{10} = 0.79$), $j = +1$, even. `band` is the occupied fold-band level (label 0) and `bulk` the empty first bulk level (label 1); the two integrands of their matrix element are computed.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
left.plot(Y, band[4][0], color=PALETTE[0], lw=2.0, label="band: $a$")
left.plot(Y, band[4][1], color=PALETTE[0], lw=1.5, ls="--", label="band: $b$")
left.plot(Y, bulk[4][0], color=PALETTE[1], lw=2.0, label="bulk: $a$")
left.plot(Y, bulk[4][1], color=PALETTE[1], lw=1.5, ls="--", label="bulk: $b$")
left.set_xlabel("hidden coordinate $y$")
left.set_ylabel("orbital (normalised)")
left.set_title(f"$n_2 = 10$: band $\\varepsilon = {band[0]:.4f}$, "
               f"bulk $\\varepsilon = {bulk[0]:.4f}$", fontsize=10)
left.legend(fontsize=8)
```

The left panel draws the two components of both orbitals (band blue, bulk orange; $a$ solid, $b$ dashed), with their energies in the title.

```python
right.plot(Y, momentum, color=PALETTE[2], lw=1.5, ls="--", label="momentum part")
right.plot(Y, kinetic, color=PALETTE[3], lw=1.5, ls=":", label="kinetic part")
right.plot(Y, momentum + kinetic, color=PALETTE[6], lw=2.0, label="sum")
right.fill_between(Y, momentum + kinetic, color=PALETTE[6], alpha=0.2)
right.set_xlabel("hidden coordinate $y$")
right.set_ylabel("integrand (units of $m$)")
right.set_title("Integrand of the matrix element")
right.legend(fontsize=8)
element = abs(da_h(k, 1, 0.0, band[4], bulk[4], bulk[0]))
save_figure(fig, "transition_orbitals",
            "Left: the orbitals (components $a$ solid, $b$ dashed; vertical axis, "
...)
report("|<band| d_a h |bulk>| and Q for N = 592, a4,0 = 0",
       f"{element:.13f}, {element / (band[0] - bulk[0]) ** 2:.13f}")
```

The right panel draws the momentum part, the kinetic part and their sum, and shades the area under the sum (`fill_between`), whose integral is the matrix element. `element` is its size; with $AH = 1$, $Q = $ `element` divided by the squared energy difference. `save_figure` saves Figure 15c.1. Out [4]: $|\langle n|\partial_a h|m\rangle| = 0.1031128583791$ and $Q = 0.1396882759133$ (the record's $0.1396883$; Section 15.21). The fold-band orbital sits at the fold, the bulk orbital fills the interval with one node, and the kinetic part, which exists only because the hidden direction shrinks, contributes a large share of the area.

**In [5], $Q$ for every allowed pair.**

```python
ADIABATIC = "Revision/kohn_sham/results/adiabatic/adiabaticity.csv"
with open(repository_file(ADIABATIC), newline="", encoding="utf-8") as handle:
    adiabatic = {row["id"]: row for row in csv.DictReader(handle)}


def key_text(sector, label):
    return f"{sector[0]}:{sector[1]:+d}:{sector[2]}:{label}"
```

The adiabaticity table of the record is read; `key_text` writes a level as the record does, `n2:j:parity:label`, with the sign of $j$ always printed (`+d`).

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
                element = abs(da_h(k, sector[1], a4, on, om, em))
                q = element / (en - em) ** 2  # A H = 1
                pairs[(n, a4)].append((q, sector[0], lm))
                if q > best[0] * (1.0 + 1e-12):
                    best = (q, f"{key_text(sector, ln)} -> {key_text(sector, lm)}",
                            abs(en - em), element)
```

For each of the fifteen states and each solved sector the cell takes every occupied level $n$ ($f > 0.5$) and every empty level $m$ of the same sector, computes the matrix element and $Q_{nm}$, and keeps the triple $(Q, n_2, l_m)$ for the next figure. `best` holds the largest $Q$ so far with its pair, energy difference and matrix element; a new pair replaces it only if its $Q$ is larger by more than a relative $10^{-12}$, so that of two equal values (at $k = 0$ the sectors $j = +1$ and $j = -1$ have the same levels and orbitals up to the sign of $b$, by $\sigma_3 h_j(0)\sigma_3 = h_{-j}(0)$, Chapter 14) the first in the solver's order is kept, as the solver does.

```python
    row = adiabatic[state_id(n, a4)]
    for value, column in ((best[0], "Q_max"), (best[2], "Q_max_delta_eps"),
                          (best[3], "Q_max_matrix_element")):
        worst_q = max(worst_q, abs(value / float(row[column]) - 1.0))
    same_pairs = same_pairs and best[1] == row["Q_max_pair"]
    say(f"{n:4d}  {a4:4.1f}  {best[0]:.5f}  {best[1]:28}  {best[2]:9.6f}"
        f"  {best[3]:9.6f}")
report("largest relative difference to the record", f"{worst_q:.1e}")
check(worst_q < 1e-9, "Q_max, its energy difference and matrix element reproduced",
      record=f"{ADIABATIC}, columns Q_max, Q_max_delta_eps, Q_max_matrix_element")
check(same_pairs, "the pair with the largest Q is the recorded pair",
      record=f"{ADIABATIC}, column Q_max_pair")
```

For each state the largest $Q$, its energy difference and matrix element are compared with the record's columns (relative differences), the pair with the record's column `Q_max_pair`, and a table row is printed (`:28` pads the pair to 28 characters). Out [5] is the table: for $N = 8$ the pair is `0:-1:even:0 -> 0:-1:even:1` (a zero mode of $j = -1$ and the first even bulk level at $k = 0$), with $Q$ from $0.06815$ to $0.03617$; for $N = 592$ the pair `10:+1:even:0 -> 10:+1:even:1`, with $Q$ from $0.13969$ to $0.03880$; for $N = 2352$ the pair `26:+1:even:0 -> 26:+1:even:1`, with $Q$ from $0.19433$ to $0.04047$. Along the history the energy differences grow (from $0.859$ to $2.167\,m$ for $N = 592$) faster than the matrix elements (from $0.103$ to $0.182\,m$). The largest relative difference to the record is $6.7 \times 10^{-14}$; both checks pass.

**In [6], every pair at the first slice.**

```python
fig, ax = plt.subplots()
for marker, n in (("^", 8), ("o", 592), ("s", 2352)):
    for colour, label in zip(PALETTE, (1, 2)):
        points = [(n2, q) for q, n2, lm in pairs[(n, 0.0)] if lm == label]
        ax.plot([p[0] for p in points], [p[1] for p in points], marker,
                color=colour, ms=8 if n != 2352 else 6,
                markerfacecolor=colour if n != 2352 else "white",
                label=f"$N = {n}$, to label {label}")
```

For the three free states at $a_{4,0} = 0$ the cell draws every $Q$ against the shell of its sector, with a marker per particle number (triangles, circles, open squares for $N = 2352$) and a colour per label of the empty level (1 or 2).

```python
ax.set_yscale("log")
ax.set_xlabel("shell $n_2$ of the sector ($k = 0.25\\sqrt{n_2}$)")
ax.set_ylabel("$Q_{nm}$ (pure number)")
ax.set_title("Every allowed transition at $a_{4,0} = 0$, $\\lambda = 0$")
ax.legend(fontsize=8)
largest = max(q for values in pairs.values() for q, _, _ in values)
save_figure(fig, "q_by_pair",
            "The adiabaticity measure $Q_{nm}$ (vertical axis, logarithmic, pure "
...)
report("largest Q of all free pairs (15 states)", f"{largest:.5f}")
check(largest < 0.2, "every Q of the free states is below 0.2")
```

A logarithmic axis, the labels, and `largest`, the largest $Q$ of all pairs of all fifteen states, printed in the caption of Figure 15c.2. Out [6]: $0.19433$, and the check passes. In the figure the jumps to label 1 dominate in every shell and grow with $n_2$ (the momentum part of the matrix element is proportional to $k$), and the zero modes at $n_2 = 0$ can jump too, through the kinetic part.

**In [7], $Q_{max}$ of the whole matrix.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
tags = [("lam0", "$0$"), ("lamp1", "$+\\lambda_1$"), ("lamm1", "$-\\lambda_1$"),
        ("lamp2", "$+\\lambda_2$"), ("lamm2", "$-\\lambda_2$")]
record_max, record_state = 0.0, ""
for style, n in ((":", 8), ("-", 592), ("--", 2352)):
    for colour, (tag, label) in zip(PALETTE, tags):
        values = [float(adiabatic[state_id(n, a4, tag)]["Q_max"]) for a4 in SLICES]
        if max(values) > record_max:
            record_max = max(values)
            record_state = state_id(n, SLICES[values.index(record_max)], tag)
        left.plot(SLICES, values, style, color=colour, lw=1.5, marker="o", ms=3,
                  label=f"$N = {n}$, $\\lambda = $ {label}" if n == 592 else None)
        right.plot(SLICES, [v * v for v in values], style, color=colour, lw=1.5,
                   marker="o", ms=3)
```

For the 15 series (three particle numbers, five couplings) the recorded $Q_{max}$ at the five slices is drawn on the left (dotted for $N = 8$, solid for $592$, dashed for $2352$; a colour per coupling; only the series of $N = 592$ get legend entries, `None` gives none) and its square on the right; the largest value of the whole matrix and its state are tracked (`values.index(record_max)` is the position of the largest value in the list).

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

Still inside the loop over $N$: the values computed here for $\lambda = 0$ are drawn as black crosses over the record's free curves. Then the legend, the logarithmic axes and `save_figure` for Figure 15c.3, whose caption prints the largest $Q_{max}^2$.

```python
report("largest Q_max of the whole matrix (record) and its state",
       f"{record_max:.7f} ({record_state})")
check(f"{record_max:.7f}" == "0.1982205" and record_state == "N2352_lamm1_a00",
      "Q_max <= 0.1982205 over the matrix, at N2352_lamm1_a00",
      record=f"{ADIABATIC}, column Q_max")
falling = all(max(q for q, _, _ in pairs[(n, SLICES[i + 1])])
              < max(q for q, _, _ in pairs[(n, SLICES[i])])
              for n in (8, 592, 2352) for i in range(4))
check(falling, "Q_max of the free states falls from slice to slice")
```

Out [7]: the largest $Q_{max}$ of the matrix is $0.1982205$, in the state `N2352_lamm1_a00`, the value of the record (there the derivatives of the self-consistent potentials, which change with $a_4$ because the effective coupling does, add to the matrix element: $0.0944$ against $0.0832$ without interaction, while the energy difference is $0.690\,m$ against $0.654\,m$; the record's columns `Q_max_matrix_element` and `Q_max_delta_eps`); and $Q_{max}$ of every free state falls from slice to slice. Both checks pass.

**In [8], the Hellmann-Feynman theorem.**

```python
DELTA = 2e-3
a0 = 1.0
state = states[(2352, a0)]
shells, finite, element, kinds = [], [], [], []
for sector, levels in state.items():
    if sector[0] == 0:
        continue  # the zero modes stay at 0
    for label in (0, 1):  # the fold-band level and the first bulk level
        eps, f, k, r3, orb = levels[label]
        near = {s: find_level(k, sector[1], sector[2], label, a0 + s, eps)
                for s in (DELTA, -DELTA, 2 * DELTA, -2 * DELTA)}
        d1 = (near[DELTA] - near[-DELTA]) / (2 * DELTA)
        d2 = (near[2 * DELTA] - near[-2 * DELTA]) / (4 * DELTA)
        shells.append(k)
        kinds.append(label)
        finite.append((4.0 * d1 - d2) / 3.0)
        element.append(da_h(k, sector[1], a0, orb, orb, eps))
```

For the free state $N = 2352$ at $a_{4,0} = 1$ and each occupied sector away from $k = 0$ (the fold band of the shells 1 to 26), the fold-band level (label 0) and the first bulk level (label 1) are solved also at $a_{4,0} \pm\delta$ and $\pm2\delta$ ($\delta = 0.002$, the solver's step). `d1` and `d2` are the central differences with the steps $\delta$ and $2\delta$, and $\tfrac13(4d_1 - d_2)$ is their **Richardson** combination, which removes the error proportional to $\delta^2$ (Chapter 2). It is compared with the diagonal matrix element $\langle n|\partial_a h|n\rangle$ (`da_h` with the same orbital twice).

```python
hf_dev = max(abs(a - b) for a, b in zip(finite, element))
band_dev = max(abs(e + k * math.exp(-a0)) for e, k, kind in zip(element, shells, kinds)
               if kind == 0)
de_da = sum(4.0 * levels[l][3] * levels[l][1] * da_h(levels[l][2], sector[1], a0,
                                                       levels[l][4], levels[l][4],
                                                       levels[l][0])
            for sector, levels in state.items() for l in levels)
recorded = float(adiabatic[state_id(2352, a0)]["dE_da4_finite_difference"])
```

`hf_dev` is the largest difference of the two derivatives; `band_dev` the largest difference between the band's matrix element and the exact $-\kappa k$ (Section 15.21). `de_da` adds up $g f_o\langle n|\partial_a h|n\rangle$ over every solved level of every sector, with $g = 4r_3$ (`levels[l][3]` is $r_3$, `levels[l][1]` the occupation); the zero modes contribute nothing (their $s_2$ and $\varepsilon$ vanish). `recorded` is the solver's finite-difference derivative of $E$.

```python
fig, ax = plt.subplots()
for label, colour, text in ((0, PALETTE[0], "fold band"), (1, PALETTE[1],
                                                           "first bulk level")):
    xs = [s for s, kind in zip(shells, kinds) if kind == label]
    ax.plot(xs, [v for v, kind in zip(finite, kinds) if kind == label], "o",
            color=colour, ms=8, label=f"{text}: finite differences")
    ax.plot(xs, [v for v, kind in zip(element, kinds) if kind == label], "x",
            color="black", ms=8, mew=1.5)
ax.plot([], [], "x", color="black", ms=8, mew=1.5,
        label="$\\langle n|\\partial_a h|n\\rangle$")
ax.axhline(0.0, color="0.5", lw=0.8)
ax.set_xlabel("3-momentum $k$ of the shell (units of $m$)")
ax.set_ylabel("$d\\varepsilon/da_4$ (units of $m$)")
ax.set_title("Hellmann-Feynman: $N = 2352$, $\\lambda = 0$, $a_{4,0} = 1$")
ax.legend(fontsize=8)
save_figure(fig, "hellmann_feynman",
            "The derivative $d\\varepsilon/da_4$ (vertical axis, units of $m$) of "
...)
```

The finite differences are drawn as circles (blue for the band, orange for the bulk levels) and the matrix elements as black crosses, against $k$. This is Figure 15c.4: the band derivatives lie on the line $-\kappa k$; the bulk derivatives are positive at small $k$ (the level rises as the hidden direction shrinks) and negative at large $k$, where the momentum term wins.

```python
report("largest |finite difference - matrix element| (52 levels)", f"{hf_dev:.1e}")
report("largest |<n| d_a h |n> + kappa k| of the fold band", f"{band_dev:.1e}")
report("dE/da4 of N2352_lam0_a10: Hellmann-Feynman / record",
       f"{de_da:.10f} / {recorded:.10f}")
check(hf_dev < 1e-7 and band_dev < 1e-12,
      "d eps/da4 = <n| d_a h |n> within 1e-7, and -kappa k on the fold band",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "adiabatic_hellmann_feynman")
check(abs(de_da / recorded - 1.0) < 1e-9, "dE/da4 = sum g f <n| d_a h |n>",
      record=f"{ADIABATIC}, N2352_lam0_a10, column dE_da4_finite_difference")
```

Out [8]: the two derivatives of the 52 levels agree to $7.2 \times 10^{-13}$; the band's matrix element is $-\kappa k$ to $1.1 \times 10^{-16}$; and $dE/da_4 = -841.8509845084$ from Hellmann-Feynman against $-841.8509845081$ in the record, which is $-E_{KS}$ (Section 15.15). Both checks pass.

**In [9], the Fermi-level crossing of $N = 2360$.**

```python
K27 = 0.25 * math.sqrt(27.0)


def odd0(a4):
    return find_level(0.0, 1, "odd", 0, a4, 1.3)


def band27(a4):
    return find_level(K27, 1, "even", 0, a4, 0.9 * K27 * math.exp(-a4))
```

`K27` is the momentum $0.25\sqrt{27} = 1.2990$ of the shell $n_2 = 27$. `odd0` is the odd bulk level of label 0 at $k = 0$ (the bulk edge at the first slice), `band27` the fold-band level of the shell 27, each at a given slice.

```python
lo, hi = 0.0, 0.5  # bisection for band27(a4) = odd0(a4)
for _ in range(45):
    mid = 0.5 * (lo + hi)
    lo, hi = (mid, hi) if band27(mid) > odd0(mid) else (lo, mid)
crossing = 0.5 * (lo + hi)
dense = np.linspace(0.0, 2.0, 21)
band_curve = [band27(a) for a in dense]
odd_curve = [odd0(a) for a in dense]
```

The crossing slice is found by bisection (45 halvings of $[0, 0.5]$): while the band level lies above the odd level, the crossing lies later. Then both levels are computed at 21 slices from 0 to 2 for the figure.

```python
with open(repository_file("Revision/kohn_sham/results/adiabatic/crossing-demo.csv"),
          newline="", encoding="utf-8") as handle:
    demo = {float(row["a4"]): row for row in csv.DictReader(handle)}
mine = {a4: max(0.0, 8.0 * (odd0(a4) - band27(a4))) for a4 in SLICES}
worst_demo = max(abs(mine[a4] - float(demo[a4]["difference"])) for a4 in SLICES)
```

The record's demonstration lists, at the five slices, the energy of the aufbau state, of the adiabatically continued state and their difference. After the crossing the aufbau state puts the eight extra particles into the band level, while the continued state keeps them in the odd level, so the difference is $8(\varepsilon_{odd} - \varepsilon_{27})$, and zero before the crossing (`max(0.0, ...)`). `worst_demo` compares this with the record.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
left.plot(dense, band_curve, color=PALETTE[0], lw=2.0,
          label="fold band $n_2 = 27$ (128 orbitals)")
left.plot(dense, odd_curve, color=PALETTE[1], lw=2.0,
          label="odd bulk level, $k = 0$ (8)")
left.axvline(crossing, color="0.4", ls=":", lw=1.2, label="crossing")
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("level (units of $m$)")
left.set_title("Two levels near the Fermi level, $N = 2360$")
left.legend(fontsize=8)
right.plot(SLICES, [float(demo[a]["difference"]) for a in SLICES], "o", color="black",
           ms=9, label="record")
right.plot(SLICES, [mine[a] for a in SLICES], "x", color=PALETTE[0], ms=10, mew=2,
           label="$8(\\varepsilon_{odd} - \\varepsilon_{27})$, this notebook")
right.set_xlabel("slice $a_{4,0}$")
right.set_ylabel("$E_{continued} - E_{aufbau}$ (units of $m$)")
right.set_title("Energy above the instantaneous ground state")
right.legend(fontsize=8)
save_figure(fig, "fermi_crossing",
            "The Fermi-level crossing of the demonstration state $N = 2360$ without "
...)
```

The left panel draws the two levels along the history with the crossing as a dotted line (the band level holds $4r_3(27) = 4\cdot32 = 128$ orbitals, the odd level 8); the right panel the recorded energy differences (black dots) and those computed here (crosses). This is Figure 15c.5.

```python
report("band level n2 = 27 minus the odd level at a4,0 = 0",
       f"{band_curve[0] - odd_curve[0]:.10f}")
report("crossing slice a4,0", f"{crossing:.6f}")
report("largest |8 (eps_odd - eps_27) - recorded difference|", f"{worst_demo:.1e}")
check(0.0 < crossing < 0.5, "the crossing lies between the slices 0 and 0.5",
      record="Revision/kohn_sham/results/adiabatic/crossing-demo.csv, flags at 0 "
             "and 0.5")
check(worst_demo < 1e-9, "the energy differences of the demonstration reproduced",
      record="Revision/kohn_sham/results/adiabatic/crossing-demo.csv, column "
             "difference")
```

Out [9]: at the first slice the band level lies $0.0067452776\,m$ above the odd level; they cross at $a_{4,0} = 0.004684$; the energy differences agree with the record to $5.2 \times 10^{-14}$ ($4.676354$ at $a_{4,0} = 0.5$ up to $12.47799\,m$ at $2$, Section 15.21). Both checks pass.

**In [10], the heat map.**

```python
rows, names = [], []
for n in (8, 592, 2352):
    for tag, label in tags:
        rows.append([float(adiabatic[state_id(n, a4, tag)]["Q_max"]) for a4 in SLICES])
        names.append(f"N = {n}, {tag}")
table = np.array(rows)
```

The 75 values of $Q_{max}$ are arranged in a table of 15 rows (a series each) and 5 columns (the slices), with a name for every row.

```python
fig, ax = plt.subplots(figsize=(6.5, 6.0))
image = ax.imshow(table, cmap="Blues", aspect="auto", vmin=0.0, vmax=0.2)
ax.grid(False)  # no grid lines across the coloured squares
ax.set_xticks(range(5), [f"{a:.1f}" for a in SLICES])
ax.set_yticks(range(len(names)), names, fontsize=8)
for i in range(table.shape[0]):
    for jj in range(table.shape[1]):
        ax.text(jj, i, f"{table[i, jj]:.3f}", ha="center", va="center", fontsize=7,
                color="white" if table[i, jj] > 0.12 else "black")
ax.set_xlabel("slice $a_{4,0}$")
ax.set_title("$Q_{max}$ of the 75 ground states (record)")
fig.colorbar(image, ax=ax, label="$Q_{max}$")
save_figure(fig, "q_map",
            "Heat map of the largest adiabaticity measure $Q_{max}$ of the 75 ground "
...)
```

`ax.imshow` draws the table as coloured squares (a **heat map**), from white for 0 to dark blue for $0.2$ (`vmin`, `vmax`); the grid of the figure style is switched off, the axes are labelled with the slices and the row names, every square gets its value printed (white on the dark squares above $0.12$; the counter is called `jj` because `j` is the block type elsewhere), and a colour bar shows the scale. This is Figure 15c.6.

```python
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

The record of Fermi-level crossings has one row per step between two neighbouring slices of each series (15 series times 4 steps); the cell counts the rows whose occupied set changed. Out [10]: 60 rows, none changed; the check passes.

**In [11], the last check.**

```python
NAMES = ["transition_orbitals", "q_by_pair", "q_history", "hellmann_feynman",
         "fermi_crossing", "q_map"]
missing = [name for number, name in enumerate(NAMES, start=1)
           if not output_file(f"{FIGURE_FOLDER}/15c_{number}_{name}.png").is_file()]
check(missing == [], "every figure file of this notebook exists")
all_checks_passed()
```

As in the other notebooks; the cell prints PASS every figure file of this notebook exists and ALL 12 CHECKS PASSED (notebook 15c).

### 15.26 The gas at a temperature

**Mermin's functional.** At a temperature $T > 0$ the particles no longer fill exactly the lowest levels. Mermin's finite-temperature form of Kohn-Sham theory (Chapter 13) occupies each level with the **Fermi-Dirac** probability

$$
f(x) = \frac{1}{1 + e^{x}}, \qquad x = \frac{\varepsilon - \mu}{T},
$$

where the **chemical potential** $\mu$ is fixed by the particle number, $\sum gf = N$. (In this section $f$ is always the occupation; the hidden scale of the slice does not appear.) The function $f$ is 1 far below $\mu$, 0 far above, and $\tfrac12$ at $\varepsilon = \mu$; it falls from nearly 1 to nearly 0 over a few $T$ (Figure 15d.5 shows it). A useful identity: $1 - f(x) = f(-x)$, because $1 - \frac{1}{1 + e^x} = \frac{e^x}{1 + e^x} = \frac{1}{e^{-x} + 1}$. The functions of state of the whole cell are (ks-theory.json, thermodynamics):

$$
E = \sum g f\varepsilon - 2\,\mathrm{Vol}_7\!\int e^{3Hy}e_{int}\,dy, \qquad S = -\sum g\big[f\ln f + (1 - f)\ln(1 - f)\big],
$$

$$
F = E - TS, \qquad \Omega = -T\sum g\ln\big(1 + e^{-(\varepsilon - \mu)/T}\big) - 2\,\mathrm{Vol}_7\!\int e^{3Hy}e_{int}\,dy = F - \mu N ,
$$

the energy, the **entropy** (a measure of how many arrangements of the particles the occupations allow), the **free energy** and the **grand potential**. The last equality is Exercise 5. The self-consistent loop is the one of Section 15.5 with the Fermi-Dirac occupations in place of the aufbau.

**Which count fixes $\mu$: a discrepancy of the record.** The particle number in these formulas is the number of the whole cell, $\sum gf = N$, with each half holding $N/2$ (Section 15.2). The theory file `Revision/kohn_sham/ks-theory.json` states this count in its densities (densities.total: "N = sum g f over both fold conditions is the particle number of the cell (N/2 per half)"), but its line on the occupations (thermodynamics.occupation) reads "mu fixed by sum w g f = N", with the weight $w = \tfrac12$ of the densities. The two disagree by a factor 2 in the particle number. The second line also contradicts the file's own $\Omega$ and $F = \Omega + \mu N$, whose $\mu N$ term belongs to the count $\sum gf = N$ (Exercise 5). What the Rust solver actually does is fixed by its source: `Revision/kohn_sham/solver/src/mermin.rs` solves $\sum_i g_if((\varepsilon_i - \mu)/T) = N$ with the full degeneracies $g_i$ (its function `solve` receives the levels and the degeneracies and no weight), and `scf.rs` multiplies by $w = \tfrac12$ only when it builds the densities. The record notes the discrepancy itself (`Revision/kohn_sham/results/parameters.json`, conventions.particleNumber, and `Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md`, section 4), and the solver's check thermo_N_conservation confirms $\sum gf = N$ in all 135 thermal states. Notebook 15d checks it once more and prints $\sum wgf = N/2$ (Out [8]). Status: the count used is $\sum gf = N$ (COMPUTED, as above); the line of the theory file is a recorded inconsistency of that file, not a different physics.

**The record's thermal states.** 135 states: $N = 8, 592, 2352$, the couplings $0, \pm\lambda_1$, the five slices and $T = 0.01, 0.02, 0.05$ (Section 15.2). Their label sets reach so high that every omitted level above the cut has an occupation below $2 \times 10^{-12}$ (the thermal window; the largest occupation at a cut is $1.5 \times 10^{-14}$, check thermo_window_cut), and the solver checks $\sum gf = N$ to $3 \times 10^{-11}$ (check thermo_N_conservation), the two forms of $\Omega$ (check thermo_grand_potential_two_forms) and the identities $C_V = T\,dS/dT = dE/dT$ and $-dF/dT = S$ with Richardson differences of self-consistent states at $T \pm 0.01\,T$ and $T \pm 0.02\,T$ (checks thermo_CV_identity and thermo_entropy_identity).

**The heat capacity in closed form.** The **heat capacity** $C_V = dE/dT$ at fixed $N$ says how much energy one unit of temperature costs. Without interaction the levels do not depend on $T$, and $C_V$ has a closed form. With the shorthand $f_i = f(x_i)$, $d_i = \varepsilon_i - \mu$ and $w_i = g_if_i(1 - f_i)$ (a thermal weight, not the weight $w = \tfrac12$ of the densities; Notebook 15d calls it `w` too), line by line:

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

**The two-level formula for $N = 8$.** At $a_{4,0} = 0$ and low temperature only two groups of levels matter for $N = 8$: the eight zero modes at $\varepsilon = 0$ and the 24 orbitals of the first fold-band shell at $\varepsilon = \Delta = 0.25$ (the gap, $\kappa\Delta k$). The particles that leave the zero modes must enter the band, line by line:

$$
8\,\big(1 - f(-\mu/T)\big) = 24\,f\big((\Delta - \mu)/T\big) .
$$

Rule: the holes in the zero modes equal the particles in the band, because $N$ is fixed.

$$
8\,e^{-\mu/T} = 24\,e^{-(\Delta - \mu)/T} .
$$

Rule: $1 - f(x) = f(-x)$, and $f(x) \approx e^{-x}$ for $x \gg 1$; here $\mu/T$ and $(\Delta - \mu)/T$ are about 12 and 13 at $T = 0.01$.

$$
\ln 8 - \frac{\mu}{T} = \ln 24 - \frac{\Delta - \mu}{T}, \qquad \mu = \frac{\Delta}{2} - \frac{T}{2}\ln 3 .
$$

Rule: take the logarithm of both sides; collect $\mu$ on one side ($-2\mu/T = \ln 3 - \Delta/T$, since $\ln 24 - \ln 8 = \ln 3$) and divide by $-2/T$. At $T \to 0$ the chemical potential sits in the middle of the gap; it falls linearly with the slope $-\tfrac12\ln 3$, the logarithm of the ratio of the degeneracies. At $T = 0.01$ the formula gives $0.1195069386$, the record $0.1195065987$ (Notebook 15d, Out [5]): the difference $3.4 \times 10^{-7}$ is the size of the neglected terms. The largest of them is the next shell: the fold band of $n_2 = 2$, with 48 orbitals at $\varepsilon_2 = 0.25\sqrt2 = 0.3536$, also takes particles, and with it the balance reads $8e^{-\mu/T} = 24e^{-(\Delta - \mu)/T}\big(1 + 2e^{-(\varepsilon_2 - \Delta)/T}\big)$, so that

$$
\mu = \frac{\Delta}{2} - \frac{T}{2}\ln\Big[3\Big(1 + 2e^{-(\varepsilon_2 - \Delta)/T}\Big)\Big] .
$$

Rule: the particles of the second shell are $48e^{-(\varepsilon_2 - \mu)/T} = 24e^{-(\Delta - \mu)/T}\cdot2e^{-(\varepsilon_2 - \Delta)/T}$; the same logarithm as before, with the extra factor in the bracket. It gives $0.1195066203$, $2.2 \times 10^{-8}$ from the record (Out [5]). The rest is the approximation $f(x) \approx e^{-x}$ itself: $\ln f(x) = -x - \ln(1 + e^{-x}) \approx -x - e^{-x}$ for $x \gg 1$, so the two logarithms gain $-e^{-\mu/T}$ and $-e^{-(\Delta - \mu)/T}$, and collecting $\mu$ as before moves it by $-\tfrac T2\big(e^{-\mu/T} - e^{-(\Delta - \mu)/T}\big) = -2.2 \times 10^{-8}$, which closes the gap to the record; the third shell ($n_2 = 3$, 32 orbitals at $0.25\sqrt3$) moves $\mu$ by less than $10^{-10}$.

**Why $\mu$ must be computed with care.** Near a closed shell at low temperature almost every level is either full or empty. The direct count $\sum gf - N$ then adds numbers very close to 1 and subtracts $N$; in double precision (the computer's numbers, about 16 significant digits) the result is only known to about $\epsilon\,N$, where $\epsilon = 2^{-52} = 2.2 \times 10^{-16}$ is the rounding unit, while the count changes with $\mu$ only at the rate $dN/d\mu$. A root of the direct count is therefore uncertain by about $\epsilon N/(dN/d\mu)$. For $N = 8$ at $a_{4,0} = 0$, $T = 0.01$, the smallest $dN/d\mu$ of the record, $1.03 \times 10^{-2}$ (`Revision/kohn_sham/results/thermo/thermodynamics.csv`), this uncertainty is $2.2 \times 10^{-16}\cdot8/(1.03 \times 10^{-2}) = 1.7 \times 10^{-13}\,m$, more than ten thousand times the spacing $1.4 \times 10^{-17}$ of the double-precision numbers near $\mu = 0.12$; the record's column mu_direct_count_minus_mu gives $-1.68 \times 10^{-13}\,m$ for this state. In an earlier computation of the record, for the metric of 2026-10-14 (withdrawn on 2026-10-16), the gaps were larger, $dN/d\mu$ of the same state was about $1.2 \times 10^{-6}$, and the direct count, then used by the solver, missed $\mu$ by $8.3 \times 10^{-10}\,m$ in the state `N8_lamm1_a00_T10`, a failure found by the independent cross-check of Chapter 16 (Section 16.20; `Revision/kohn_sham/solver/src/mermin.rs`, its header, and `Revision/kohn_sham/reports/ks-rust-mermin-roots.json`). That failure is why the solver computes $\mu$ from a balance.

**The balance form, line by line.** Let $\mathcal S$ be the set of the levels that are filled at $T = 0$ and $d = N - \sum_{\mathcal S}g$ (zero for a closed shell). Then

$$
\sum_i g_if(x_i) - N = \sum_{i \notin \mathcal S}g_if(x_i) + \sum_{i \in \mathcal S}g_i\big(1 - f(-x_i)\big) - N = P - H_l - d ,
$$

with the thermal particles above the filled levels $P = \sum_{i \notin \mathcal S}g_if(x_i)$ and the thermal holes below them $H_l = \sum_{i \in \mathcal S}g_if(-x_i)$. Rule: split the sum into the levels outside and inside $\mathcal S$; inside use $f(x) = 1 - f(-x)$; then $\sum_{\mathcal S}g_i - N = -d$. The condition $\sum gf = N$ becomes $P = H_l + d$, and for a closed shell simply $\ln P = \ln H_l$: the thermal particles balance the thermal holes. No numbers close to 1 are added and no large number is subtracted; each hole factor is computed as $f(-x)$ directly, never as $1 - f$. The solver solves $\ln(P + d_-) - \ln(H_l + d_+) = 0$ with $d_\pm = \max(\pm d, 0)$, adding each sum in the form $\ln\sum e^{t_i} = t_{max} + \ln\sum e^{t_i - t_{max}}$ (the **log-sum-exp**, which never overflows or underflows), by Newton's method in a bracket and then bisection down to neighbouring double-precision numbers (`Revision/kohn_sham/solver/src/mermin.rs`, the form LogBalance). The record checks every one of the 135 roots against a root computed with 40 significant digits by mpmath: all lie within their rounding bound, the largest difference is $2.9 \times 10^{-16}\,m$ (`Revision/kohn_sham/reports/ks-rust-mermin-roots.json`, check solver_mu_within_rounding_bound).

**What the thermal states show** (COMPUTED; `Revision/kohn_sham/results/thermo/thermodynamics.csv`, Notebook 15d). For $N = 592$ without interaction the chemical potential lies near the middle of the gap between the shells $n_2 = 10$ and $11$ ($\mu = 0.8099$ at $a_{4,0} = 0$, $T = 0.01$) and comes down with the band ($0.1078$ at $a_{4,0} = 2$); the entropy at $T = 0.01$ grows from $76.0$ at $a_{4,0} = 0$ to $518.0$ at $a_{4,0} = 2$, because the redshifted band levels crowd together and the same temperature excites more particles. For $N = 8$ the gas is activated across its gap $0.25\,e^{-a_{4,0}}$: at $a_{4,0} = 0$ and $T = 0.01$ its heat capacity is only $0.016$, at $a_{4,0} = 2$ already $25.1$. The interaction shifts the free energy as it shifts the ground-state energy: repulsion lowers it and attraction raises it for $N = 8$ and $592$, almost independently of $T$; for $N = 2352$ at $a_{4,0} = 0$ the thermal particles reach the bulk edge, $0.0175\,m$ above the highest occupied level, and at $T = 0.05$ the attraction lowers the free energy by $42.79\,m$, with a much larger entropy ($1777.4$ against $1179.8$; Notebook 15d, Out [10]).

**The sea holes: where the filling convention stops being reasonable.** The CONVENTION of Section 15.2 never occupies the negative branch, not even thermally. How good is that? Without interaction the sea's fold band (block type $j = -1$, even fold condition, label 0) has the levels $-\kappa k$ (Section 15.4). If the sea were treated thermally, each of its orbitals would be empty with the probability $1 - f\big((-\kappa k - \mu)/T\big) = f\big((\kappa k + \mu)/T\big) = 1/(1 + e^{(\mu + \kappa k)/T})$; such an empty sea orbital is a **thermal hole**, which a full quantum treatment would count as an antiparticle of the same universe. The record computes the number of these holes for every thermal state as a DIAGNOSTIC (check thermo_sea_hole_diagnostic_computed): it exceeds 1 per cent of $N$ in 27 of the 135 states, all at $a_{4,0} \ge 0.5$ (21 of them with $N = 8$, three each with $N = 592$ and $2352$, at $a_{4,0} = 2$ and $T = 0.05$), and reaches $594.5\,N$ in `N8_lamp1_a20_T50` ($N = 8$, $+\lambda_1$, $a_{4,0} = 2$, $T = 0.05$; the free state and the state with $-\lambda_1$ at the same slice and temperature have nearly the same value). There the band has been redshifted so close to $\varepsilon = 0$ (its slope is $e^{-2} = 0.135$) that the temperature excites the sea as easily as the particles, $\mu$ itself is negative ($-0.187$), and the particle-only ensemble is outside its range of validity; a thermal treatment of the sea is OPEN. These thermal holes are excitations inside one universe; they say nothing about pairs of universes or about the matter-antimatter asymmetry.

### 15.27 Example: thermodynamics (Notebook 15d)

Notebook 15d runs the solver's command `single` for 20 free thermal states ($N = 8$ and $592$) and reads their final levels exactly. From these levels alone it recomputes, in plain Python, the chemical potential (with mpmath at 40 digits), $E$, $S$, $F$, $\Omega$, $C_V$ and $dN/d\mu$, and compares them with the record. It shows why the direct count is too coarse (Figure 15d.1), draws $\mu(T)$ with the two-level formula and checks the formula with the second shell (Figure 15d.2), $F$ and $S$ along the history (Figure 15d.3), the heat capacity (Figure 15d.4), the occupations and the count $\sum gf = N$ (Figure 15d.5), the sea-hole diagnostic (Figure 15d.6) and the effect of the interaction on $F$ (Figure 15d.7). It needs Rust, takes about a minute, and ends with ALL 16 CHECKS PASSED (notebook 15d).

What to look for: in Figure 15d.1 the orange staircase of the double-precision count, flat at zero over a whole stretch, against the smooth blue line of the exact count; in Figure 15d.2 the straight start of $\mu(T)$ from the middle of the gap; in Figure 15d.4 how the heat capacity of $N = 8$ wakes up at ever lower temperatures as the history closes the gap; in Figure 15d.6 the values above the 1 per cent line late in the history.

<!-- NOTEBOOK 15d -->

### 15.30 Line-by-line walk-through of Notebook 15d

The notebook has 11 code cells, In [1] to In [11]. As in Section 15.9, docstrings are left out of the quotations, and long caption strings in calls of `save_figure` are shortened: the quotation shows the first line of the call and the first line of the caption, and then a line `...)` that stands for the rest of the caption and the closing parenthesis; the complete cells are printed in Section 15.29.

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

The colours, one shade per slice in a dictionary, the three temperatures of the record, and the names of the thermal states, for example `N8_lam0_a00_T10` for $N = 8$, $\lambda = 0$, $a_{4,0} = 0$, $T = 0.01$ (`round(1000 * t)` is a thousand times the temperature).

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

`thermal_state` runs `single` for one free thermal state. Compared with Notebook 15b it adds the temperature, the margin 0.2 that the canonical matrix uses for free thermal states (so that the label set, and therefore the state, is exactly the recorded one), and the option that writes the final levels and $\mu$ into a second file as decimal numbers that read back into exactly the solver's double-precision numbers. If the solver fails, the notebook stops with the end of its error message.

```python
    exact = json.loads(lev.read_text(encoding="utf-8"))
    full = json.loads(out.read_text(encoding="utf-8"))
    eps = [float(e) for e, _ in exact["levels_eps_deg"]]  # exactly the solver's
    deg = [float(g) for _, g in exact["levels_eps_deg"]]
    return float(exact["mu"]), eps, deg, full["levels_n2_j_parity_label_eps_deg_f"]
```

The two files are read; `eps` and `deg` are the levels and their degeneracies $g$, and the function returns the solver's $\mu$, these two lists, and the full level list (shell, block type, fold condition, label, energy, degeneracy, occupation) from the main JSON file, whose key keeps the word parity for the fold condition.

```python
THERMO = "Revision/kohn_sham/results/thermo/thermodynamics.csv"
with open(repository_file(THERMO), newline="", encoding="utf-8") as handle:
    record = {row["id"]: row for row in csv.DictReader(handle)}
states = {}
for n in (8, 592):
    for a4 in (0.0, 1.0, 2.0):
        for t in TEMPS:
            states[(n, a4, t)] = thermal_state(n, a4, t)
for a4 in (0.5, 1.5):
    states[(592, a4, 0.05)] = thermal_state(592, a4, 0.05)
```

The record's table of the 135 thermal states is read, and 20 free states are computed: $N = 8$ and $592$ at the slices 0, 1, 2 and the three temperatures (18 states), and $N = 592$ at $a_{4,0} = 0.5$ and $1.5$ with $T = 0.05$.

```python
worst_mu = max(abs(mu - float(record[state_id(n, a4, t)]["mu"]))
               for (n, a4, t), (mu, _, _, _) in states.items())
report("free thermal states computed", len(states))
report("largest |mu(solver now) - mu(record)|", f"{worst_mu:.1e}")
check(worst_mu < 1e-12, f"the solver reproduces the recorded mu of {len(states)} states",
      record=f"{THERMO}, column mu")
```

Out [2]: 20 states, and the new $\mu$ agrees with the record to $5.6 \times 10^{-17}$ (the record's column holds 16 significant digits). The check passes.

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

`exact_root` solves $\sum gf = N$ with 40 significant digits: inside `with mpmath.workdps(40):` every mpmath number (`mpmath.mpf`) carries 40 digits. Starting at the solver's $\mu$, Newton's method takes the step $(\sum gf - N)/(dN/d\mu)$ with $dN/d\mu = \sum gf(1 - f)/T$ (Section 15.26), at most 60 times, until the step is below $10^{-36}$. With 40 digits the subtraction of $N$ loses nothing that matters. The count is $\sum gf$ with the full degeneracies, the count of the whole cell (Section 15.26).

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

Out [3]: $\mu$ lies within $0.02$ of its rounding bound of the exact root; $E$, $S$, $F$, $\Omega$ agree to $2.0 \times 10^{-14}$; the closed-form $C_V$ agrees with the record's Richardson difference $T\,dS/dT$ to $2.0 \times 10^{-8}$ (the accuracy of the difference quotient); $dN/d\mu$ to $5.4 \times 10^{-15}$. All four checks pass.

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
offsets = np.linspace(-3e-13, 3e-13, 61)
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

For the activated state $N = 8$, $a_{4,0} = 0$, $T = 0.01$ the cell evaluates the count $\sum gf - 8$ at 61 values of $\mu$ within $\pm 3 \times 10^{-13}$ of the solver's $\mu$ (spacing $10^{-14}$): once directly in double precision (`direct`) and once with 40 digits (`exact`).

```python
fig, ax = plt.subplots()
ax.plot(offsets * 1e13, direct, "s-", color=PALETTE[1], ms=4, lw=1.2,
        label="direct count, double precision")
ax.plot(offsets * 1e13, exact, color=PALETTE[0], lw=2.0, label="exact count, 40 digits")
ax.axvline(float(root8 - mu8) * 1e13, color="0.3", ls=":", lw=1.2, label="exact root")
ax.axhline(0.0, color="0.6", lw=0.8)
ax.set_xlabel("$\\mu$ minus the solver's $\\mu$ (units of $10^{-13}\\,m$)")
ax.set_ylabel("$\\sum g f - N$")
ax.set_title("$N = 8$, $a_{4,0} = 0$, $T = 0.01$: the direct count is too coarse")
ax.legend(fontsize=8)
```

Both counts are drawn against the offset in units of $10^{-13}$, with the exact root as a dotted vertical line and a zero line.

```python
zero_at = [off for off, value in zip(offsets, direct) if value == 0.0]  # direct = 0
true_root = float(root8 - mu8)  # the 40-digit root, measured from the solver's mu
if zero_at and min(zero_at) <= true_root <= max(zero_at):  # the usual case here
    width = max(zero_at) - min(zero_at)  # where the count says "exactly N"
    where = ("is exactly zero on a whole interval of width about "
             f"${width * 1e13:.1f} \\times 10^{{-13}}\\,m$ around the true root, so "
             "it cannot tell the root from any other point of that interval")
    report("sampled interval where the direct count is 0 (from the solver's mu)",
           f"{min(zero_at):.1e} to {max(zero_at):.1e} m")
elif zero_at:  # (on another computer the rounding steps may fall differently)
    miss = min(abs(off - true_root) for off in zero_at)  # the nearest such point
    where = ("is zero only on a short interval that misses the true root by at "
             f"least ${miss * 1e14:.0f} \\times 10^{{-14}}\\,m$")
else:
    where = "is never exactly zero at the sampled points"
report("the record's direct-count root minus mu, N8_lam0_a00_T10",
       f"{float(record[state_id(8, 0.0, 0.01)]['mu_direct_count_minus_mu']):.2e} m")
```

`zero_at` collects the sampled offsets at which the double-precision count is exactly zero, and `true_root` is the 40-digit root measured from the solver's $\mu$. If the zero points enclose the true root, `where` describes a flat stretch of the stated width around the root (the case on the computer that built the book; the doubled braces of the f-string print single braces), and the interval is reported; on a computer whose rounding steps fall differently the other two branches describe what is seen. The last line reports the record's own direct-count root for this state (the column mu_direct_count_minus_mu). Out [4]: the direct count is zero from $-1.2 \times 10^{-13}$ to $4.0 \times 10^{-14}\,m$ (measured from the solver's $\mu$, which lies within 0.02 of its rounding bound of the true root, Out [3]), and the record's own direct-count root of this state, from the solver's sum in its own order, lies $1.68 \times 10^{-13}\,m$ below $\mu$: both are errors of the size $\epsilon N/(dN/d\mu) = 1.7 \times 10^{-13}\,m$ estimated in Section 15.26.

```python
save_figure(fig, "root_conditioning",
            "The particle-number condition $\\sum g f - N$ (vertical axis, of size "
...)
```

`save_figure` saves Figure 15d.1, whose caption takes the sentence `where`.

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

Then the balance root is compared with the 40-digit root for all 20 states, and the width of the flat stretch is measured (the number of zero samples times their spacing). Out [4]: the width is $1.7 \times 10^{-13}\,m$, while the balance finds every root to $1.1 \times 10^{-16}\,m$, a thousand times better. The check passes.

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

`T_GRID` holds 49 temperatures from $0.002$ to $0.05$. `curves(n, a4)` computes $\mu$ with the balance and then $E$, $S$, $F$ and $C_V$ at every temperature of the grid, from the level set of the solver's state at $T = 0.05$ (the largest window; at lower temperatures the extra levels are empty to far below the rounding); `np.array(rows)` makes a table with one row per temperature and the five columns.

```python
GROUND = "Revision/kohn_sham/results/ground/summary.csv"
with open(repository_file(GROUND), newline="", encoding="utf-8") as handle:
    ground = {row["id"]: row for row in csv.DictReader(handle)}
gap8 = float(ground["N8_lam0_a00"]["KS_gap"])
two_level = gap8 / 2.0 - 0.5 * T_GRID * math.log(3.0)
curve8 = {a4: curves(8, a4) for a4 in (0.0, 1.0, 2.0)}
```

The ground states of the record are read, `gap8` is the gap $0.25$ of $N = 8$ at $a_{4,0} = 0$, `two_level` the formula $\Delta/2 - (T/2)\ln3$ on the grid, and `curve8` the curves of $N = 8$ at the slices 0, 1, 2.

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

For each slice the curve $\mu(T)$ is drawn in its shade of blue with the record's three values as open circles, and the two-level formula as a dashed orange line; `save_figure` saves Figure 15d.2.

```python
band2 = next(lv[4] for lv in states[(8, 0.0, 0.05)][3]  # the fold band, n2 = 2
             if lv[0] == 2 and lv[1] == 1 and lv[2] == "even" and lv[3] == 0)
formula = gap8 / 2.0 - 0.005 * math.log(3.0)
formula3 = gap8 / 2.0 - 0.005 * math.log(3.0 * (1.0 + 2.0 * math.exp(-(band2 - gap8)
                                                                      / 0.01)))
recorded = float(record[state_id(8, 0.0, 0.01)]["mu"])
report("fold-band level of the shell n2 = 2 at a4,0 = 0", f"{band2:.12f}")
report("mu of N8_lam0_a00_T10 in the record", f"{recorded:.10f}")
report("mu from the two-level formula", f"{formula:.10f}")
report("mu from the formula with the shell n2 = 2", f"{formula3:.10f}")
check(abs(formula - recorded) < 1e-6, "the two-level formula gives mu to 1e-6",
      record=f"{THERMO}, N8_lam0_a00_T10")
check(abs(formula3 - recorded) < 1e-7, "with the shell n2 = 2 the formula gives mu "
      "to 1e-7", record=f"{THERMO}, N8_lam0_a00_T10")
```

`band2` is the fold-band level of the shell $n_2 = 2$ at the first slice, taken from the solver's level list (`next(...)` returns the first entry that satisfies the condition: shell 2, $j = +1$, even, label 0). `formula` is the two-level formula at $T = 0.01$ and `formula3` the formula with the second shell of Section 15.26. Out [5]: $\varepsilon_2 = 0.353553390593$ ($= 0.25\sqrt2$), the record's $\mu = 0.1195065987$, the two-level formula $0.1195069386$ and the formula with the second shell $0.1195066203$; both checks pass, the first with the tolerance $10^{-6}$, the second with $10^{-7}$.

**In [6], free energy and entropy.**

```python
curve592 = {a4: curves(592, a4) for a4 in (0.0, 0.5, 1.0, 1.5, 2.0)}
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
for a4, values in curve592.items():
    e0 = float(ground[f"N592_lam0_a{round(10 * a4):02d}"]["E_KS"])
    left.plot(T_GRID, values[:, 3] - e0, color=SHADES[a4], lw=2.0,
              label=f"$a_{{4,0}} = {a4}$")
    right.plot(T_GRID, values[:, 2], color=SHADES[a4], lw=2.0)
    if a4 in (0.0, 1.0, 2.0):
        ids = [state_id(592, a4, t) for t in TEMPS]
        left.plot(TEMPS, [float(record[i]["F"]) - e0 for i in ids], "o",
                  color=SHADES[a4], ms=7, markerfacecolor="white")
        right.plot(TEMPS, [float(record[i]["entropy"]) for i in ids], "o",
                   color=SHADES[a4], ms=7, markerfacecolor="white")
```

The curves of $N = 592$ at the five slices. For each slice the left panel draws $F(T) - E_0$, with the free ground-state energy $E_0$ from the record, and the right panel the entropy; at the slices 0, 1, 2 the record's values are added as open circles.

```python
left.set_xlabel("temperature $T$")
left.set_ylabel("$F - E_0$ (units of $m$)")
left.set_title("Free energy, $N = 592$, $\\lambda = 0$")
left.legend(fontsize=8)
right.set_xlabel("temperature $T$")
right.set_ylabel("entropy $S$")
right.set_title("Entropy (circles: record)")
save_figure(fig, "free_energy_entropy",
            "Left: the free energy measured from the ground-state energy, "
...)
```

The labels, and `save_figure` for Figure 15d.3: along the history the curves of $F - E_0$ fall faster and the entropy grows, because the redshifted band levels crowd together.

```python
_, eps, deg, _ = states[(592, 1.0, 0.05)]
worst_fs = 0.0
for t in T_GRID:
    h = 1e-3 * t
    f_plus = functions_of_state(eps, deg, balance_root(eps, deg, 592, t + h), t + h)[2]
    f_minus = functions_of_state(eps, deg, balance_root(eps, deg, 592, t - h), t - h)[2]
    s = functions_of_state(eps, deg, balance_root(eps, deg, 592, t), t)[1]
    worst_fs = max(worst_fs, abs(-(f_plus - f_minus) / (2 * h) - s) / s)
report("largest relative |-dF/dT - S|, N = 592, a4,0 = 1", f"{worst_fs:.1e}")
check(worst_fs < 1e-4, "-dF/dT = S along the whole temperature grid",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "thermo_entropy_identity")
```

The identity $-dF/dT = S$ is checked on the whole grid for $N = 592$ at $a_{4,0} = 1$: $F$ at $T \pm h$ with $h = 10^{-3}T$ (each with its own balance root), the central difference, and the relative difference to $S$. Out [6]: $1.8 \times 10^{-7}$, the error of the central difference; the check passes.

```python
rising = all(bool(np.all(np.diff(v[:, 2]) > 0)) and bool(np.all(np.diff(v[:, 3]) < 0))
             for v in curve592.values())
check(rising, "S rises and F falls with T at every slice")
```

The second check: on every curve the entropy rises and the free energy falls with $T$ (`np.diff` takes the differences of neighbouring rows of a column). It passes.

**In [7], the heat capacity.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
for a4, values in curve8.items():
    left.plot(T_GRID, values[:, 4], color=SHADES[a4], lw=2.0,
              label=f"$a_{{4,0}} = {a4:.0f}$")
    left.plot(TEMPS, [float(record[state_id(8, a4, t)]["C_V"]) for t in TEMPS], "o",
              color=SHADES[a4], ms=7, markerfacecolor="white")
for a4, values in curve592.items():
    right.plot(T_GRID, values[:, 4], color=SHADES[a4], lw=2.0,
               label=f"$a_{{4,0}} = {a4}$")
    if a4 in (0.0, 1.0, 2.0):
        right.plot(TEMPS, [float(record[state_id(592, a4, t)]["C_V"]) for t in TEMPS],
                   "o", color=SHADES[a4], ms=7, markerfacecolor="white")
for ax, n in ((left, 8), (right, 592)):
    ax.set_yscale("log")
    ax.set_xlabel("temperature $T$ (units of $m$)")
    ax.set_title(f"Heat capacity, $N = {n}$, $\\lambda = 0$")
    ax.legend(fontsize=8)
left.set_ylabel("$C_V$ (pure number)")
```

The closed-form $C_V$ of $N = 8$ at three slices (left) and $N = 592$ at five slices (right), on logarithmic axes, with the record's values as circles.

```python
save_figure(fig, "heat_capacity",
            "The heat capacity $C_V = dE/dT$ (vertical axis, logarithmic, pure "
...)
positive = all(bool(np.all(v[:, 4] > 0)) for v in list(curve8.values())
               + list(curve592.values()))
check(positive, "C_V > 0 at every temperature and slice")
```

`save_figure` saves Figure 15d.4, and the check confirms $C_V > 0$ on every curve. For $N = 8$ at $a_{4,0} = 0$ the heat capacity is tiny at the lowest temperatures, because the first excitation costs the gap $0.25\,m$; at $a_{4,0} = 2$ the gap is $0.034\,m$ and the heat capacity rises at much lower temperatures.

**In [8], the occupations.**

```python
fig, ax = plt.subplots()
sums = []
for colour, t in zip(PALETTE, TEMPS):
    mu, eps, deg, levels = states[(592, 1.0, t)]
    e = np.array(eps)
    f = 1.0 / (1.0 + np.exp(np.minimum((e - mu) / t, 700.0)))
    sums.append(float(np.sum(np.array(deg) * f)))
    order = np.argsort(e)
    ax.plot(e[order], f[order], "o-", color=colour, ms=4, lw=1.0, label=f"$T = {t}$")
    ax.axvline(mu, color=colour, ls=":", lw=1.2)
ax.set_xlim(0.1, 0.5)
ax.set_xlabel("level $\\varepsilon$ (units of $m$)")
ax.set_ylabel("occupation $f$")
ax.set_title("$N = 592$, $a_{4,0} = 1$: Fermi-Dirac occupations (dotted: $\\mu$)")
ax.legend()
```

For $N = 592$ at $a_{4,0} = 1$ and the three temperatures the cell computes the occupations $f$ of the solver's levels at the solver's $\mu$ (`np.minimum(..., 700.0)` keeps the exponent below the largest value the computer can exponentiate), adds up $\sum gf$, and draws $f$ against the energy, sorted, with $\mu$ as a dotted line, between $0.1$ and $0.5\,m$.

```python
save_figure(fig, "occupations",
            "The occupation $f$ of the levels of the free state $N = 592$ at "
...)
report("sum g f at the three temperatures", ", ".join(f"{s:.12f}" for s in sums))
report("sum w g f (w = 1/2, one half of the cell)",
       ", ".join(f"{0.5 * s:.9f}" for s in sums))
check(max(abs(s - 592.0) for s in sums) < 1e-9,
      "the occupations add up to N = 592 with sum g f (the whole cell)",
      record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
             "thermo_N_conservation")
```

`save_figure` saves Figure 15d.5. Out [8]: $\sum gf = 592.000000000000$ at all three temperatures, the count of the whole cell, and $\sum wgf = 296.000000000$, the particles in one half; the check passes. This is the count that the solver uses (Section 15.26).

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

`shell_sizes` counts the whole-number vectors $(x, y, z)$ with $x^2 + y^2 + z^2 = n_2$ for every $n_2$ up to a largest value, by three nested loops over a cube that contains them (`math.isqrt` is the whole-number square root); the result is the dictionary of the $r_3(n_2)$.

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

For $N = 8$ at $T = 0.05$ and the slices 0, 1, 2: `band` maps each shell to its fold-band level (from the solver's level list), and `holes` adds up $4r_3(n_2)$ times the hole probability $1/(1 + e^{(\mu + \varepsilon_{band})/T})$ of the sea band $-\varepsilon_{band}$ over the shells of the level set (the record sums over the same shells). The number per particle is kept, and the relative difference to the record's column `sea_holes_excluded` tracked.

```python
fig, ax = plt.subplots()
plotted = []  # every value drawn, to measure their range
for marker, n in (("o", 8), ("s", 592)):
    for colour, t in zip(PALETTE, TEMPS):
        values = [float(record[state_id(n, a, t)]["sea_holes_over_N"])
                  for a in (0.0, 0.5, 1.0, 1.5, 2.0)]
        plotted += values
        ax.plot([0, 0.5, 1, 1.5, 2], np.maximum(values, 1e-52), marker + "-",
                color=colour, ms=6, lw=1.2,
                markerfacecolor=colour if n == 8 else "white",
                label=f"$N = {n}$, $T = {t}$")
ax.plot(list(mine), list(mine.values()), "x", color="black", ms=11, mew=2,
        label="this notebook, $N = 8$, $T = 0.05$")
ax.axhline(0.01, color="0.3", ls=":", lw=1.2, label="1 percent")
ax.set_yscale("log")
ax.set_ylim(1e-52, 1e4)  # the smallest recorded value is about 4e-48
ax.set_xlabel("slice $a_{4,0}$")
ax.set_ylabel("sea holes per particle")
ax.set_title("Diagnostic of the filling convention ($\\lambda = 0$)")
ax.legend(fontsize=7, ncol=2, loc="lower right")
smallest = min(v for v in plotted if v > 0.0)  # the smallest nonzero value
powers = int(math.log10(max(plotted) / smallest))  # whole powers of ten spanned
```

The figure draws the record's sea holes per particle for $N = 8$ (filled markers) and $592$ (open) at the three temperatures against the slice, the values recomputed here as black crosses, and the 1 per cent line; `np.maximum(values, 1e-52)` keeps the logarithmic axis finite, and the axis runs from $10^{-52}$ to $10^4$. `smallest` is the smallest nonzero value drawn and `powers` the number of whole powers of ten between it and the largest, which the caption prints.

```python
save_figure(fig, "sea_holes",
            "The number of thermal holes that the excluded sea fold band would "
...)
report("smallest and largest sea holes per particle drawn",
       f"{smallest:.2e}, {max(plotted):.2e}")
report("sea holes per particle, N = 8, T = 0.05, a4,0 = 0, 1, 2",
       ", ".join(f"{v:.4g}" for v in mine.values()))
check(worst_sea < 1e-9, "the sea-hole diagnostic reproduced",
      record=f"{THERMO}, column sea_holes_excluded")
```

`save_figure` saves Figure 15d.6. Out [9]: the values drawn reach from $3.76 \times 10^{-48}$ to $594$ per particle; for $N = 8$ at $T = 0.05$ the sea holes per particle are $0.004566$, $3.638$ and $594.5$ at the slices 0, 1, 2; the diagnostic is reproduced (relative difference below $10^{-9}$), and the check passes.

**In [10], the interaction at a temperature.**

```python
fig, ax = plt.subplots()
by_series = {}  # (N, tag) -> the three values of F(lambda) - F(0)
for colour, n in zip(PALETTE, (8, 592, 2352)):
    for tag, style in (("lamp1", "-"), ("lamm1", "--")):
        values = [float(record[state_id(n, 0.0, t, tag)]["F"])
                  - float(record[state_id(n, 0.0, t)]["F"]) for t in TEMPS]
        by_series[(n, tag)] = values
        sign = "+" if tag == "lamp1" else "-"
        ax.plot(TEMPS, values, style, marker="o", color=colour, ms=6, lw=1.5,
                label=f"$N = {n}$, ${sign}\\lambda_1$")
ax.set_yscale("symlog", linthresh=1e-2)
ax.axhline(0.0, color="0.5", lw=0.8)
ax.set_xlabel("temperature $T$ (units of $m$)")
ax.set_ylabel("$F(\\lambda) - F(0)$ (units of $m$)")
ax.set_title("Effect of the interaction on the free energy, $a_{4,0} = 0$")
ax.legend(fontsize=8, ncol=2)
up = by_series[(592, "lamp1")]  # N = 592, +lambda_1, at T = 0.01, 0.02, 0.05
down = by_series[(2352, "lamm1")]  # N = 2352, -lambda_1
```

From the record only: for $N = 8$, $592$, $2352$ at $a_{4,0} = 0$ and the couplings $\pm\lambda_1$, the change $F(\lambda) - F(0)$ at the three temperatures, drawn with solid lines for $+\lambda_1$ and dashed for $-\lambda_1$ on a symmetric logarithmic axis (linear between $-0.01$ and $0.01$). `up` and `down` keep two series for the caption.

```python
save_figure(fig, "interaction_free_energy",
            "The change of the free energy caused by the couplings $+\\lambda_1$ "
...)
for (n, tag), values in sorted(by_series.items()):
    report(f"F(lam) - F(0), N = {n}, {tag}", ", ".join(f"{v:.6f}" for v in values))
signs = all(v < 0.0 for n in (8, 592) for v in by_series[(n, "lamp1")]) and all(
    v > 0.0 for n in (8, 592) for v in by_series[(n, "lamm1")])
check(signs, "repulsion lowers F and attraction raises it, N = 8 and 592",
      record=f"{THERMO}, column F")
steady = max(abs(v[-1] / v[0] - 1.0) for (n, _), v in by_series.items()
             if n in (8, 592))
report("relative change of the shift, T = 0.01 to 0.05, N = 8, 592", f"{steady:.1e}")
check(steady < 1e-3, "for N = 8 and 592 the shift changes by less than 0.1 percent "
      "with T", record=f"{THERMO}, column F")
row_t = record[state_id(2352, 0.0, 0.05, "lamm1")]
row_0 = record[state_id(2352, 0.0, 0.05)]
report("N2352_a00_T50 entropy, -lambda_1 / lambda = 0",
       f"{float(row_t['entropy']):.4f} / {float(row_0['entropy']):.4f}")
report("N2352_a00_T50 mu, -lambda_1 / lambda = 0",
       f"{float(row_t['mu']):.6f} / {float(row_0['mu']):.6f}")
```

`save_figure` saves Figure 15d.7, and the six series are printed. The first check: for $N = 8$ and $592$ repulsion lowers $F$ and attraction raises it at every temperature. `steady` is the largest relative change of the shift between $T = 0.01$ and $T = 0.05$ for these two particle numbers; the second check requires it to be below 0.1 per cent. The last two reports print the entropy and $\mu$ of the state `N2352_lam0_a00_T50` with and without the attraction. Out [10]: the shifts of $N = 8$ are $\mp0.037787$ ($\pm\lambda_1$), those of $N = 592$ $-2.815$ and $+2.779$, nearly independent of $T$ (largest relative change $4.4 \times 10^{-4}$); those of $N = 2352$ change with $T$, and at $T = 0.05$ the attraction lowers $F$ by $42.79\,m$, with the entropy $1777.4$ against $1179.8$ and $\mu = 1.1589$ against $1.2762$ (Section 15.26). Both checks pass.

**In [11], the last check.**

```python
NAMES = ["root_conditioning", "chemical_potential", "free_energy_entropy",
         "heat_capacity", "occupations", "sea_holes", "interaction_free_energy"]
missing = [name for number, name in enumerate(NAMES, start=1)
           if not output_file(f"{FIGURE_FOLDER}/15d_{number}_{name}.png").is_file()]
check(missing == [], "every figure file of this notebook exists")
all_checks_passed()
```

As in the other notebooks; the cell prints PASS every figure file of this notebook exists and ALL 16 CHECKS PASSED (notebook 15d).

### 15.31 What we proved, what we computed, what we assumed

**PROVED** (exact statements; derived line by line in this chapter or in Chapter 14, and, where a check is named, verified by sympy in `Revision/kohn_sham/reports/ks-theory-python.json` and by WolframScript in `Revision/kohn_sham/reports/ks-theory-wolfram.json`):

| statement | where | record check |
| --- | --- | --- |
| the real block equation, the fold and tip conditions, self-adjointness, real levels | Section 15.2 | `block_hamiltonian`, `block_ode_equivalent`, `bc_fold_conditions`, `bc_tip_family`, `bc_self_adjoint_boundary_term` |
| the Pruefer phase increases strictly and runs over all values: every level has its own label, none is missed | Section 15.3 | derived here; the solver's check `free_particle_branch_labels` |
| the exact levels at $k = 0$: the zero mode $(e^{fMy}, 0)$ at $\varepsilon = 0$, the even levels $\pm\sqrt{M^2 + (n\pi/(fL))^2}$, the odd levels with $\tan(pfL) = -p/M$ | Section 15.3 | `bc_exact_k0_spectra` |
| the cubic Hermite midpoint and the Anderson weights | Sections 15.3, 15.5 | derived here |
| the fold band: $\varepsilon = \kappa k$ exactly, with the orbital $(e^{fMy}, 0)$ and the slope $e^{-a_{4,0}}$ | Section 15.4, Exercise 2 | `brane_band_slope` (a name kept from an earlier construction) |
| the rescaling identity: a later slice is the first slice with redshifted momenta, a shorter hidden interval and a larger warp rate | Section 15.4 | `rescaling_identity` |
| $E_{KS} = \sum gf\varepsilon - 2\,\mathrm{Vol}_7\int e^{3Hy}e_{int}\,dy$ (double counting) | Section 15.5 | `ks_onshell_lagrangian` |
| $E_{KS}(-\hat\lambda) = -E_{KS}(\hat\lambda)$ for the zero-mode state of $N = 8$ | Section 15.5 | derived here |
| the energy-momentum tensor of the states | Section 15.16 | `emt_orbital_components`, `emt_trace_identity` |
| the free gas has $p_3 = \rho/3$ and $p_0 = p_t = 0$ at every point | Section 15.16 | derived here |
| the conservation law $(e^{3Hy}p_0)' = 3H\,e^{3Hy}p_t$ | Section 15.16 | `emt_y_conservation_selfconsistent` |
| the energy-change law $dE/da_4 = -3P_3 + P_t + \tfrac13P_0$ on the history, and $dE/da_4 = -E$ for the free gas | Section 15.16, Exercise 6 | `emt_x4_component`, `emt_energy_change_history` |
| the Hellmann-Feynman theorem, $\partial_a h_j = -j\kappa k\sigma_3 + \tfrac13T_j$ and the first-order estimate $Q_{nm}$ | Section 15.21, Exercise 7 | `adiabatic_hellmann_feynman`, `adiabatic_offdiagonal_identity` |
| the closed form of $C_V$, $C_V = T\,dS/dT$, $-dF/dT = S$, $\Omega = F - \mu N$ with $N = \sum gf$, the two-level formula for $\mu$ and its correction by the second shell, the balance form of $\sum gf = N$ | Section 15.26, Exercise 5 | derived here |

**COMPUTED** (numerical, with the record file and the measured agreement):

- The canonical matrix of the corrected metric: 75 ground states and 135 thermal states; all 45 checks of `Revision/kohn_sham/reports/ks-rust-solver.json` PASS; a repeat run byte-identical and a refined run within tolerances fixed in advance (`Revision/kohn_sham/reports/ks-rust-determinism.json`, 14 checks PASS); every chemical potential within its rounding bound of a 40-digit root (`Revision/kohn_sham/reports/ks-rust-mermin-roots.json`, 5 checks PASS). Notebook 15a reran the quick matrix (18 ground states, 12 thermal states): its report has 44 checks, all PASS (the record's 45 without the crossing demonstration, Out [4]), and every compared number agrees with the record within the tolerances fixed in advance, the energies to $1.6 \times 10^{-13}$ (Out [6]).
- The method by hand (Notebook 15e): the exact levels at $k = 0$ to $7.2 \times 10^{-10}$ and the solver's levels to $9.8 \times 10^{-15}$ (Out [6]), the RK4 error ratio 16.00 (Out [8]), the fold band $\varepsilon = \kappa k$ to $1.1 \times 10^{-16}$ in 123 levels and the rescaling identity to $7.5 \times 10^{-14}$ (Out [9]), the interacting states of $N = 8$ with the solver's 17 iterations, and $E_{KS}(-\hat\lambda) = -E_{KS}(\hat\lambda)$ to the last digit (Out [11] to Out [13]).
- Along the history (Section 15.15): the free gas lives on the fold band, so its band levels and the gaps of $N = 8$ and $592$ fall exactly like $e^{-a_{4,0}}$ (the gap of $N = 8$ is $0.25$, $0.0919699$, $0.0338338$ at $a_{4,0} = 0, 1, 2$) and its energy falls exactly like $e^{-a_{4,0}}$ ($N = 592$: $361.12$ to $48.87$; $N = 2352$: $2288.39$ to $309.70$), while the levels at $k = 0$ above the zero modes rise (the first even bulk level: $1.447972$, $1.770856$, $2.271612$; Notebook 15e, Out [9]).
- Delta-SCF equals the gap without interaction to $3.1 \times 10^{-13}\,m$; the orbital relaxation is at most $6.3 \times 10^{-4}\,m$ (`N2352_lamp1_a00`) and at most $2.1 \times 10^{-7}\,m$ in every other state; the interaction changes the energy of $N = 592$ by at most $8.32\,m$; all 75 self-consistent loops converge directly, in at most 29 iterations (Notebook 15a, Out [9] to Out [14]).
- The energy-momentum tensor (Notebook 15b): the free gas has $p_3 = \rho/3$ and $p_0 = p_t = 0$ to $1.6 \times 10^{-16}$ of $\max|T|$ (Out [4]); the conservation law holds pointwise to $1.7 \times 10^{-7}$ and integrated to $1.2 \times 10^{-10}$ (Out [6]); the energy-change law holds in all 75 states to $9.2 \times 10^{-10}$ (Out [8]; solver checks emt_y_conservation_pointwise, emt_y_conservation_integrated and emt_energy_change_dE_da4).
- The source conditions (`Revision/field_equations_a4/reports/ks-source-conditions.json`, 5 checks PASS; Notebook 15b, Out [12]): C1 fails in all 70 states with a nonzero tensor (ratio at least $0.456213$), C2 holds for the 10 nonzero free states and fails for all 60 interacting ones (at least $0.080929$), C3 holds, and C4 fails (the history needs $p_3/\rho = -1.26713$ and $p_0/\rho = p_t/\rho = -2.38212$ at $a_{4,0} = 0$, the free gas has $\tfrac13$ and 0); the five free states of $N = 8$ have a vanishing tensor.
- Adiabaticity (Notebook 15c): $Q_{max} \le 0.1982205$ over the matrix (state `N2352_lamm1_a00`; every transition probability below $0.04$), every $Q$ of the free states below 0.2, the zero modes coupled to the bulk levels of their sector by the shrinking hidden direction ($Q = 0.06814928$ for $N = 8$ at $a_{4,0} = 0$; Exercise 7), no Fermi-level crossing in the matrix, and the demonstration $N = 2360$, whose instantaneous ground state is wrong by $4.68$ to $12.48\,m$ after a crossing near $a_{4,0} = 0.0047$.
- Thermodynamics (Notebook 15d): $\mu$, $E$, $S$, $F$, $\Omega$, $C_V$ and $dN/d\mu$ of 20 free thermal states recomputed from the solver's levels ($E$, $S$, $F$, $\Omega$ to $2.0 \times 10^{-14}$, $C_V$ to $2.0 \times 10^{-8}$ of the record's difference quotient); the two-level formula gives $\mu$ to $3.4 \times 10^{-7}$, with the second shell to $2.2 \times 10^{-8}$; the balance finds $\mu$ to $1.1 \times 10^{-16}\,m$, the direct count only to about $10^{-13}\,m$. The particle count is $\sum gf = N$, the count of the whole cell (the solver's source `mermin.rs`, check thermo_N_conservation, Out [8]); the line "mu fixed by sum w g f = N" of `Revision/kohn_sham/ks-theory.json` contradicts that file's own densities and grand potential and is a recorded discrepancy (Section 15.26). The sea-hole diagnostic exceeds 1 per cent of $N$ in 27 of the 135 thermal states, all at $a_{4,0} \ge 0.5$, and reaches $594.5\,N$.
- The dependence on the cutoff from $L = 3$ to $6$ of 29 recorded states (`Revision/kohn_sham/tip_convergence/tip-convergence.json`, 7 of 7 checks PASS; Section 15.2): the free fold-band gases do not depend on $L$, except their values at the fold (high by 0.25, 1.38 and 4.8 per cent at $a_{4,0} = 0, 1, 2$) and except $N = 2352$ at $a_{4,0} = 0$, whose energy does not converge up to $L = 6$; the levels at $k = 0$ approach $\pm m$ like the levels of a box of proper length $fL$; the interacting energies of $N = 8$ at $L = 3$ are 0.977, 0.674 and 0.215 of their large-$L$ values at $a_{4,0} = 0, 1, 2$, and the interaction shifts of $N = 592$ and $2352$ at $a_{4,0} = 2$ are 4.6 to 4.7 times larger at large $L$. These are numbers of the record; the notebooks of this chapter compute at $L = 3$ only.
- The five notebooks print 95 PASS lines together (19, 28, 20, 12 and 16).

**ASSUMED**:

- the good sector (no dependence on the extra times) and the boundary construction at the fold $y = 0$, where the two halves of a cell meet: the fold condition follows from self-adjointness up to one parameter, and both of its values, the even and the odd fold condition, are solved and filled; the metric is degenerate at the fold, and no junction condition is derived;
- CHOSEN: the regular tip $b(-L) = 0$ at the cutoff $L = 3$. Its effect is COMPUTED in the record (above): nothing for the free fold-band gases except their values at the fold and the state $N = 2352$ at the first slice, but much for the interaction, whose effects grow with $L$ the more the later the slice. The couplings (calibrated at $L = 3$; the same rule at larger $L$ drives $\lambda_1$ toward zero) and $N = 2352$ (bulk edge at $L = 3$) are themselves choices at $L = 3$;
- CONVENTION: particles fill the positive branch and the zero modes, the sea is never occupied, not even thermally; its justification is OPEN, and the sea-hole diagnostic shows where it fails;
- PRESCRIBED BACKGROUND: the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = 1$ and $b_4(0) = 1$; the gas is a test field on it and cannot be its source (it violates the conditions C1, C2 with interaction, and C4 of `Revision/field_equations_a4/reports/ks-source-conditions.json`);
- the functional: Hartree plus the exact local exchange of the uniform gas, no correlation; the instantaneous (adiabatic) states, supported but not proved by $Q_{max} < 0.2$.

**HYPOTHESIS**: none.

**OPEN**: the time-dependent (non-adiabatic) evolution of the gas; a thermal treatment of the sea where the particle-only ensemble fails; the justification of the filling convention; the limit $L \to \infty$ wherever the record does not establish it ($N = 2352$ at $a_{4,0} = 0$, where the bulk levels at $k = 0$ approach $m$ only algebraically, the occupied set changes and the iteration of the interacting partners fails; the thermal state `N592_lam0_a20_T50`; every quantity not computed at $L \ne 3$, and everything beyond $L = 6$); states beyond $a_{4,0} = 2$, the continuum limit $\Delta k \to 0$ and states with extra-time momenta; what drives the history, since this gas cannot (Chapters 17 and 22). Nothing in this chapter concerns the creation of universes, pairs of universes or the matter-antimatter asymmetry.

### 15.32 Exercises

**Exercise 1 (closed shells).** (a) Show that $r_3(9) = 30$ and $r_3(10) = 24$. (b) The closed shell after $n_2 = 5$ is 232 (Section 15.2). Using $r_3(6) = 24$, $r_3(7) = 0$, $r_3(8) = 12$ and $r_3(11) = 24$, continue filling the fold band shell by shell up to $n_2 = 11$. (c) Which closed shell is nearest to $2352/4$, and why is it the record's middle particle number? (d) Compute the highest occupied level, the lowest empty level and the gap of the free state $N = 592$ at $a_{4,0} = 0$, and compare with the table of Section 15.15.

*Answer.* (a) For $n_1^2 + n_2^2 + n_3^2 = 9$ the squares are $9 + 0 + 0$ or $4 + 4 + 1$. In the first case the 3 can stand in any of the 3 places with two signs: $3\cdot2 = 6$ vectors; in the second the 1 can stand in any of the 3 places and each of the three numbers has two signs: $3\cdot2^3 = 24$ vectors; together 30. For 10 the squares must be $9 + 1 + 0$: the 3 in any of 3 places, the 1 in any of the 2 remaining places, and two signs each: $3\cdot2\cdot2\cdot2 = 24$. Rule: list the ways to write the number as a sum of three squares, then count places and signs. (b) With $g = 4r_3(n_2)$: $232 + 96 = 328$ ($n_2 = 6$); no shell at $n_2 = 7$; $328 + 48 = 376$ ($n_2 = 8$); $376 + 120 = 496$ ($n_2 = 9$); $496 + 96 = 592$ ($n_2 = 10$); $592 + 96 = 688$ ($n_2 = 11$). Rule: add $4r_3(n_2)$ for each new shell. (c) $2352/4 = 588$; the distances are $|496 - 588| = 92$, $|592 - 588| = 4$ and $|688 - 588| = 100$, so 592 is nearest. That is the rule of `Revision/kohn_sham/results/parameters.json` (particleNumbers.rule): the middle particle number is the closed shell, at least 8 and below the bulk edge, nearest to a quarter of the largest one. (d) At $a_{4,0} = 0$ the band level of a shell is $\kappa k = 0.25\sqrt{n_2}$. The last filled shell is $n_2 = 10$: $0.25\sqrt{10} = 0.790569$; the first empty one $n_2 = 11$: $0.25\sqrt{11} = 0.829156$; the gap is $0.038587$. Rule: $k = \Delta k\sqrt{n_2}$ with $\Delta k = 0.25$ and $\kappa = 1$ at the first slice. These are the HOMO, LUMO and $\Delta_{KS}$ of the table.

**Exercise 2 (the fold band and the gaps along the history).** (a) Show that for $j = +1$, $v = 0$ and a constant mass $M$ the orbital $(a, b) = (e^{fMy}, 0)$ solves the block equation of Section 15.2 and both of its boundary conditions (tip $b(-L) = 0$, even fold condition $b(0) = 0$) exactly when $\varepsilon = \kappa k$. (b) Compute the gaps of the free states $N = 8$ and $N = 592$ at $a_{4,0} = 1$ and compare with Section 15.15. (c) Why does the gap of $N = 2352$ not fall like $e^{-a_{4,0}}$ between the slices 0 and 0.5? Compute it at both slices from the bulk edge $1.2922928$ and the band shells $n_2 = 26$ and $27$.

*Answer.* (a) The block equation is $a' = f[Ma - (\kappa k + (\varepsilon - v))b]$, $b' = f[((\varepsilon - v) - \kappa k)a - Mb]$ for $j = +1$. With $b = 0$ the first line becomes $a' = fMa$, solved by $a = e^{fMy}$. Rule: the derivative of $e^{cy}$ is $ce^{cy}$. The second line becomes $0 = f(\varepsilon - \kappa k)\,e^{fMy}$ (with $v = 0$), and since $f e^{fMy} \ne 0$ this holds exactly when $\varepsilon = \kappa k$. Rule: insert $b = 0$, $b' = 0$. Both boundary conditions ask for $b = 0$ at an end, which holds everywhere. So every momentum $k$ has the level $\varepsilon = \kappa k = ke^{-a_{4,0}}$, whatever $M$, $f$ and $L$ are. (b) $N = 8$: the gap is the first band level, $0.25\,e^{-1} = 0.0919699$. $N = 592$: the gap is $\kappa(k_{11} - k_{10}) = 0.25(\sqrt{11} - \sqrt{10})\,e^{-1} = 0.25\cdot0.154347\cdot0.367879 = 0.014195$. Rule: both levels are band levels, so the gap is $\kappa$ times the difference of the momenta. Both agree with the table (0.091970 and 0.014195). (c) At $a_{4,0} = 0$ the lowest empty level of $N = 2352$ is not a band level but the bulk edge, the odd level of label 0 at $k = 0$, which does not lie on the fold band and does not redshift but rises; the gap is $1.2922928 - 0.25\sqrt{26} = 1.2922928 - 1.2747549 = 0.0175379$. Along the history the band comes down and the bulk levels go up (the hidden direction shrinks), so at $a_{4,0} = 0.5$ the next band shell $n_2 = 27$ is the lowest empty level, and the gap is $0.25(\sqrt{27} - \sqrt{26})\,e^{-0.5} = 0.25\cdot0.0971326\cdot0.606531 = 0.0147285$. Rule: the gap is the lowest empty minus the highest occupied level, whichever levels they are. The ratio $0.0147285/0.0175379 = 0.840$ is not $e^{-0.5} = 0.607$; from $a_{4,0} = 0.5$ on the gap does fall like $e^{-a_{4,0}}$: the recorded gaps $0.01472852$, $0.0089333$, $0.00541832$, $0.003286377$ at $a_{4,0} = 0.5, 1, 1.5, 2$ (`Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md`, section 6; Section 15.15 shows those at 1 and 2) have the ratio $e^{-0.5} = 0.60653$ from slice to slice.

**Exercise 3 (counting levels with the phase).** For the free block $j = +1$ at $k = 0$ and $a_{4,0} = 0$ ($f = 1$, $M = 1$, $L = 3$) the levels are (Section 15.3) the even levels $\sqrt{1 + (n\pi/3)^2}$ and the odd levels $1.2922928$, $2.0106286$, ... (a) How many levels lie strictly between $\varepsilon = 0$ and $\varepsilon = 2$? (b) Between which two multiples of $\pi/2$ does $\Phi(2)$ lie? (c) Why is $\Phi(0) = 0$ exactly? (d) Compute the even level of label 1 at $a_{4,0} = 1$ and explain why it is higher than at $a_{4,0} = 0$.

*Answer.* (a) Even: $n = 1$ gives $\sqrt{1 + 1.0966} = 1.4479719 < 2$, $n = 2$ gives $\sqrt{1 + 4.3865} = 2.3208815 > 2$. Odd: $1.2922928 < 2 < 2.0106286$. So two levels: the odd label 0 (target $\pi/2$) and the even label 1 (target $\pi$). (b) $\Phi$ increases strictly and has passed the targets $\pi/2$ (at $1.2923$) and $\pi$ (at $1.4480$), but not yet $3\pi/2$ (the odd label 1, at $2.0106$); so $\pi < \Phi(2) < 3\pi/2$, that is $1 < \Phi(2)/\pi < 1.5$, as Figure 15e.1 shows. Rule: the oscillation theorem of Section 15.3, each target is reached exactly once. (c) At $\varepsilon = 0$, $k = 0$, $v = 0$ the angle equation is $\theta' = -fM\sin2\theta$ with $\theta(-L) = 0$; the constant $\theta = 0$ solves it, and a solution of such an equation is fixed by its start value, so $\theta(0) = 0$. This is the zero mode, $b = 0$; Notebook 15e finds the value exactly 0.0 (Out [3]). (d) At $a_{4,0} = 1$ the hidden scale is $f = e^{-1/3} = 0.7165313$, and the level is $\sqrt{1 + (\pi/(3f))^2} = \sqrt{1 + 1.461482^2} = \sqrt{3.135930} = 1.7708556$. Rule: the exact formula $\sqrt{M^2 + (n\pi/(fL))^2}$ with $n = 1$. The orbital fits half a wave into the proper length $fL$ of the hidden interval, which shrinks along the history ($3$ to $2.1496$), so its momentum $\pi/(fL)$ and its energy grow; Notebook 15e prints the same value (Out [9]).

**Exercise 4 (Anderson weights for two residuals).** (a) For $p = 2$ solve the bordered system of Section 15.5 and show $c_1 = (G_{22} - G_{12})/(G_{11} - 2G_{12} + G_{22})$, $c_2 = 1 - c_1$. (b) Evaluate it for the residuals $r_1 = (2, 1)$ and $r_2 = (1, -1)$, and compare $|c_1r_1 + c_2r_2|^2$ with $|r_1|^2$ and $|r_2|^2$.

*Answer.* (a) With $c_2 = 1 - c_1$, $F = |c_1r_1 + (1 - c_1)r_2|^2 = c_1^2G_{11} + 2c_1(1 - c_1)G_{12} + (1 - c_1)^2G_{22}$. Rule: expand the square with the dot products $G_{ik} = r_i\cdot r_k$. Then $dF/dc_1 = 2c_1G_{11} + 2(1 - 2c_1)G_{12} - 2(1 - c_1)G_{22} = 0$. Rule: differentiate each term. Collecting $c_1$: $c_1(G_{11} - 2G_{12} + G_{22}) = G_{22} - G_{12}$, which is the claim (the same as eliminating $\nu$ from the bordered system). (b) $G_{11} = 4 + 1 = 5$, $G_{22} = 1 + 1 = 2$, $G_{12} = 2 - 1 = 1$, so $c_1 = (2 - 1)/(5 - 2 + 2) = 0.2$ and $c_2 = 0.8$. The combined residual is $0.2\,(2, 1) + 0.8\,(1, -1) = (1.2, -0.6)$ with $|\cdot|^2 = 1.44 + 0.36 = 1.8$, smaller than $|r_2|^2 = 2$ and $|r_1|^2 = 5$; check: $F(c_1) = 5c_1^2 - 2c_1 + 2$ has its minimum $1.8$ at $c_1 = 0.2$.

**Exercise 5 (the grand potential and the particle count).** (a) For fixed levels and without interaction show that, level by level, $\varepsilon f - TS_1 - \mu f = -T\ln(1 + e^{-x})$, where $S_1 = -[f\ln f + (1 - f)\ln(1 - f)]$ and $x = (\varepsilon - \mu)/T$. (b) Conclude $\Omega = E - TS - \mu N$, and say which particle count this needs. (c) Suppose $\mu$ were fixed by $\sum wgf = N$ with $w = \tfrac12$, as the line thermodynamics.occupation of `Revision/kohn_sham/ks-theory.json` states. What would become of the relation $F = \Omega + \mu N$ of the same file?

*Answer.* (a) Line by line. $1 - f = f(-x) = 1/(1 + e^{-x})$, so $\ln(1 - f) = -\ln(1 + e^{-x})$. Rule: the identity $1 - f(x) = f(-x)$ of Section 15.26. Next, $\ln f - \ln(1 - f) = \ln\frac{f}{1 - f} = -x$. Rule: $\frac{1 - f}{f} = e^x$. Hence $S_1 = -f[\ln f - \ln(1 - f)] - \ln(1 - f) = fx - \ln(1 - f)$. Rule: write $f\ln f + (1 - f)\ln(1 - f) = f[\ln f - \ln(1 - f)] + \ln(1 - f)$. Then $TS_1 = (\varepsilon - \mu)f - T\ln(1 - f)$, because $Tx = \varepsilon - \mu$, and $\varepsilon f - TS_1 - \mu f = T\ln(1 - f) = -T\ln(1 + e^{-x})$. (b) Multiply by the degeneracy $g$ and sum over the levels: $\sum gf\varepsilon - T\sum gS_1 - \mu\sum gf = -T\sum g\ln(1 + e^{-x})$. Rule: sum the identity of (a). The left side is $E - TS - \mu N$ exactly when $N = \sum gf$, the count of the whole cell with the full degeneracies, and the right side is $\Omega$. With interaction both $E$ and $\Omega$ contain the same term $-2\,\mathrm{Vol}_7\int e^{3Hy}e_{int}\,dy$ (Section 15.26), so the relation holds unchanged; the solver checks it in all 135 states (check thermo_grand_potential_two_forms, worst relative difference $2.9 \times 10^{-14}$). (c) If $\tfrac12\sum gf = N$, then $\sum gf = 2N$, and the sum of (b) reads $E - TS - 2\mu N = \Omega$, that is $F = \Omega + 2\mu N$. Rule: insert $\sum gf = 2N$. This contradicts $F = \Omega + \mu N$ of the same file unless $\mu = 0$; with $\Omega$ written with the full degeneracies, only the count $\sum gf = N$ is consistent, and it is the one the solver uses (Section 15.26).

**Exercise 6 (the energy along the history from its slope).** (a) Use the energy-change law of Section 15.16 to show that the free gas has $E(a_{4,0}) = E(0)\,e^{-a_{4,0}}$, and check it with the record's values $E(0) = 361.1161438$, $E(0.5) = 219.0280130$ and $E(2) = 48.8717556$ of the free state $N = 592$. (b) Estimate $E(0.5)$ from $E(0)$ with Euler's rule (one step with the slope at the start) and with the trapezoid rule (the mean of the slopes at the two ends), and explain the signs of the errors. (c) Notebook 15b integrates the slopes at 17 slices from $a_{4,0} = 0$ to $2$ (spacing $h = 0.125$) with Simpson's rule and finds $-312.244811$, against $E(2) - E(0) = -312.244388$ (Out [8]). Show that the difference is the error of Simpson's rule.

*Answer.* (a) For the free gas $p_t = e_{int} = 0$, $p_0 = 0$ and $p_3 = \rho/3$ at every point (Section 15.16), so the integrated pressures are $P_t = P_0 = 0$ and $P_3 = E/3$, and the energy-change law gives $dE/da_4 = -3\cdot E/3 = -E$. Rule: insert the free pressures into $dE/da_4 = -3P_3 + P_t + \tfrac13P_0$. The solution of $E' = -E$ is $E(a) = E(0)e^{-a}$. Rule: the derivative of $e^{-a}$ is $-e^{-a}$, and the start value fixes the factor. Check: $361.1161438\cdot e^{-0.5} = 361.1161438\cdot0.6065307 = 219.0280130$ and $361.1161438\cdot e^{-2} = 361.1161438\cdot0.1353353 = 48.8717556$, the recorded values to all printed digits. (b) The slopes are $E'(0) = -361.1161$ and $E'(0.5) = -219.0280$. Euler: $361.1161 + 0.5\cdot(-361.1161) = 180.5581$, too low by $38.470$. Trapezoid: $361.1161 + \tfrac{0.5}{2}(-361.1161 - 219.0280) = 361.1161 - 145.0360 = 216.0801$, too low by $2.948$. Rule: $E(a + h) \approx E(a) + h\,E'(a)$ (Euler) and $E(a + h) \approx E(a) + \tfrac h2[E'(a) + E'(a + h)]$ (trapezoid), Chapter 2. The slope $E' = -E(0)e^{-a}$ becomes less negative along the history. Euler uses the steepest slope, that of the start, for the whole step and so overestimates the drop. The trapezoid rule replaces the slope by the straight line between its end values; the slope $-E(0)e^{-a}$ rises fast at first and then more slowly, so between the two ends it lies above that straight line, the true mean slope is less negative than the mean of the two end slopes, and the drop is again overestimated, by much less. (c) On one pair of intervals $[a_0, a_0 + 2h]$ the exact integral of $e^{-a}$ is $e^{-a_0}(1 - e^{-2h})$ and Simpson's rule gives $\tfrac h3e^{-a_0}(1 + 4e^{-h} + e^{-2h})$. Rule: integrate $e^{-a}$; Simpson's weights $1, 4, 1$ times $h/3$ (Chapter 2). The ratio of the two,

$$
\frac{h}{3}\,\frac{1 + 4e^{-h} + e^{-2h}}{1 - e^{-2h}} = 0.0416667\cdot\frac{1 + 3.5299876 + 0.7788008}{0.2211992} = 1 + 1.354 \times 10^{-6} ,
$$

does not depend on $a_0$, because both carry the factor $e^{-a_0}$; so Simpson's rule overestimates the integral of every pair, and hence of the whole range, by the same relative amount $1.354 \times 10^{-6}$ (close to $h^4/180 = 1.356 \times 10^{-6}$, the leading term of the error of Simpson's rule). Rule: $e^{-h} = 0.8824969$, $e^{-2h} = 0.7788008$ for $h = 0.125$. The integral of the slopes is $\int_0^2(-E(0)e^{-a})\,da = E(2) - E(0) = -312.244388$, so Simpson's rule gives $-312.244388\cdot(1 + 1.354 \times 10^{-6}) = -312.244388 - 0.000423 = -312.244811$, exactly the notebook's value. The difference $4.2 \times 10^{-4}$ in Out [8] is the error of the integration rule, not of the solver.

**Exercise 7 (the zero modes feel the history).** Let $n$ be the zero mode of the sector $k = 0$, $j = +1$, even fold condition, with $\varepsilon_n = 0$ and the orbital $\chi_n = (a_n, 0)$, $a_n = A\,e^{fMy}$, and let $m$ be another orbital of the same sector, $\chi_m = (a_m, ib_m)$, without interaction. (a) Use the formulas of Section 15.21 to show that $\langle n|\partial_a h|n\rangle = 0$ and $\langle n|\partial_a h|m\rangle = -\tfrac M3\int_{-L}^{0}a_nb_m\,dy$. (b) At $a_{4,0} = 0$ ($f = 1$, $M = 1$, $L = 3$) take for $m$ the first even bulk level, $\varepsilon_m = \sqrt{1 + p^2} = 1.4479719$ with $p = \pi/3$, whose orbital has $b_m = B\sin\big(p(y + 3)\big)$ and $a_m = B\big(p\cos(p(y + 3)) + \sin(p(y + 3))\big)/\varepsilon_m$. Find $A$ and $B$ from the normalisation $\int_{-3}^{0}(a^2 + b^2)\,dy = 1$, compute the matrix element and $Q_{nm}$, and compare with the record's $0.06814928$ (Section 15.21). (c) For $N = 592$ at $a_{4,0} = 0$ the pair with the largest $Q$ has the matrix element $0.1031129$ and the energy difference $0.8591647$ (Notebook 15c, Out [4], and Section 15.21); compute $Q$ and the transition probability.

*Answer.* (a) At $k = 0$ and $v = 0$ the derivative of Section 15.21 is $\partial_a h = \tfrac13T$, and the eigen-equation gives $T\phi_m = (\varepsilon_m - M\sigma_2)\phi_m$. Rule: $\kappa k = 0$ removes the other terms ($j = +1$). So $\langle n|\partial_a h|m\rangle = \tfrac13\big(\varepsilon_m\int s_0\,dy - M\int s_2\,dy\big)$ with $s_0 = a_na_m + b_nb_m$ and $s_2 = a_nb_m + b_na_m$. Rule: the products $\chi_n^\dagger\chi_m = s_0$ and $\chi_n^\dagger\sigma_2\chi_m = s_2$ of Section 15.21. For $m \ne n$, $\int s_0\,dy = \langle n|m\rangle = 0$ (orbitals of one sector with different levels are orthogonal, Section 15.2), and $b_n = 0$ leaves $s_2 = a_nb_m$: $\langle n|\partial_a h|m\rangle = -\tfrac M3\int a_nb_m\,dy$. For $m = n$: $\varepsilon_n = 0$ and $s_2 = 2a_nb_n = 0$, so $\langle n|\partial_a h|n\rangle = 0$, and by Hellmann-Feynman the zero-mode level does not move along the history. (b) $\int_{-3}^{0}A^2e^{2y}\,dy = A^2\,\frac{1 - e^{-6}}{2} = 1$ gives $A = \sqrt{2/(1 - e^{-6})} = 1.4159696$. Rule: the antiderivative of $e^{2y}$ is $e^{2y}/2$. With $u = p(y + 3)$, which runs from 0 to $\pi$, $\int b_m^2\,dy = B^2\cdot\tfrac32$, and $\int a_m^2\,dy = \tfrac{B^2}{\varepsilon_m^2}\big(p^2\cdot\tfrac32 + 0 + \tfrac32\big) = B^2\cdot\tfrac32$. Rule: $\sin^2$ and $\cos^2$ each average to $\tfrac12$ over a half period, $\int\sin u\cos u = 0$ there, and $p^2 + 1 = \varepsilon_m^2$. So $3B^2 = 1$ and $B = 1/\sqrt3 = 0.5773503$. Next,

$$
\int_{-3}^{0}e^{y}\sin\big(p(y + 3)\big)\,dy = \Big[\frac{e^{y}\big(\sin(p(y + 3)) - p\cos(p(y + 3))\big)}{1 + p^2}\Big]_{-3}^{0} = \frac{p\,(1 + e^{-3})}{1 + p^2} ,
$$

which is $1.0993344/2.0966227 = 0.5243358$. Rule: differentiating the bracket gives back $e^y\sin(p(y + 3))$ (check it with the product rule); at $y = 0$, $\sin(3p) = \sin\pi = 0$ and $\cos\pi = -1$; at $y = -3$, $\sin0 = 0$ and $\cos0 = 1$. Then $\langle n|\partial_a h|m\rangle = -\tfrac13\cdot1.4159696\cdot0.5773503\cdot0.5243358 = -0.1428833$, and

$$
Q_{nm} = \frac{0.1428833}{1.4479719^2} = \frac{0.1428833}{2.0966227} = 0.0681493 ,
$$

the record's value. Rule: $Q_{nm} = AH|\langle n|\partial_a h|m\rangle|/(\varepsilon_m - \varepsilon_n)^2$ with $AH = 1$. The zero modes stay at $\varepsilon = 0$, but the shrinking hidden direction couples them to the bulk levels of their sector. (c) $Q = 0.1031129/0.8591647^2 = 0.1031129/0.7381639 = 0.1396883$, the value of the record (Section 15.21), and the transition probability is $Q^2 = 0.0195$. $Q$ is below 1 only by a factor of about 7: the gas follows its instantaneous states in the weak sense of the measure ($Q_{max} < 1$, Section 15.21), and the time-dependent problem stays OPEN.
