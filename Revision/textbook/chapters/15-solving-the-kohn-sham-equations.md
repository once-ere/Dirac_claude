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

**The five notebooks.**

| notebook | what it computes | Rust | PASS lines | figures |
| --- | --- | --- | --- | --- |
| 15e | the solver's method by hand: shooting, Pruefer label, Newton, RK4 order, brane band, self-consistency for $N = 8$ | no | 18 | 6 |
| 15a | the whole canonical matrix with the Rust solver, compared with the record | yes | 25 | 8 |
| 15b | the energy-momentum profiles, the conservation law along $y$, the energy change along the history | yes | 18 | 7 |
| 15c | the adiabaticity measure, Hellmann-Feynman, a Fermi-level crossing | no | 12 | 6 |
| 15d | thermodynamics: chemical potential, free energy, entropy, heat capacity | yes | 15 | 7 |

The notebooks are placed in the order in which the ideas are needed: 15e first, because it teaches the method that the Rust solver uses in the others.

**The status of every statement.** Every statement of this chapter carries one of the labels of Chapter 0.

- PROVED: the exact reduction to blocks, the boundary conditions, the exact free levels at zero momentum, the slope of the brane band, the rescaling identity between the instants of the history, the formulas of the densities, potentials, energy and energy-momentum tensor, the conservation law along $y$ and the energy-change law along the history, the Hellmann-Feynman relation and the adiabaticity measure. They are verified twice in the Revision record, by sympy in `Revision/kohn_sham/reports/ks-theory-python.json` and by WolframScript in `Revision/kohn_sham/reports/ks-theory-wolfram.json`; the check names are given with each statement. The mathematical facts of the method (the monotone Pruefer phase, the derivative formula of the phase, the Hermite midpoint, the balance form of the chemical potential, the two-level formula, the symmetry $E(-\lambda) = -E(\lambda)$ of the zero-mode state) are derived line by line in this chapter.
- COMPUTED: every level, energy, density, pressure, gap, adiabaticity number and thermodynamic function. They come from the Rust solver; its own checks are in `Revision/kohn_sham/reports/ks-rust-solver.json` (42 checks, all PASS), its repeat and refined runs in `Revision/kohn_sham/reports/ks-rust-determinism.json` (14 checks, all PASS), and the notebooks of this chapter reproduce them with the measured differences given with each number.
- ASSUMED: the good sector (no dependence on the extra times), and the Z2 mirror brane at $y = 0$.
- CHOSEN: the regular tip condition at the cutoff $y = -L$ and the value $L = 3$.
- CONVENTION, justification OPEN: which levels count as particles (the positive branch and the zero modes) and that the negative branch, the sea, is never populated, not even thermally.
- PRESCRIBED BACKGROUND: the history $a_4 = AHx_4$ with $A = 1$. It is given, not solved for: the gas does not act back on it, and Section 15.16 shows why it cannot (the record `Revision/field_equations_a4/reports/ks-source-conditions.json`).
- OPEN: the time-dependent (non-adiabatic) problem, and a thermal treatment of the sea.

**What this chapter does not touch.** No statement of this chapter concerns pairs of universes, their creation or matter and antimatter. One check of the solver's report, `t3_block_map_solver_selftest`, solves a state with the mass $m$ and a state with the mass $-m$ and finds equal energies; the report itself calls it a numerical self-test of the program and NOT a proof of the theorem T3, which belongs to Chapter 19. Nothing computed here says that any universe is created, in pairs or otherwise.

**Notation and units.** The author's coordinates are $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates with the scale factor $e^{a_4}\sin^{1/6}z$; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which deflate exponentially with the scale factor $e^{-a_4}\sin^{1/6}z$; $x_8$ is the hidden space direction, with $z = 6Hx_8$ between 0 and $\pi/2$. The hidden coordinate is $y = \ln(\sin z)/(6H)$ (Chapter 14); it runs from the **tip** $y = -L$ (where the model cuts the space) to the **brane** $y = 0$. A **slice** is one instant of the history, and $a_{4,0}$ is the value of $a_4$ there. In all numbers $H = 1$ and $m = 1$, so energies, momenta and temperatures are in units of $m$ (which equals $H$) and lengths in units of $1/H$; Boltzmann's constant is 1, so a temperature is an energy.

### 15.2 The equations the solver must solve

This section collects, without proofs, the results of Chapter 14 that the solver uses, and adds the parameters of the model. Chapter 14 proves each formula; here we only need to read them.

**One orbital.** At a slice $a_{4,0}$, an orbital of the gas has a 3-momentum $\mathbf k$ (a vector of three numbers), a block type $j = +1$ or $j = -1$, and a pair of real functions $a(y)$, $b(y)$ on the interval $-L \le y \le 0$. Its level $\varepsilon$ and the two functions obey the **block equation in real form** (ks-theory.json, blockEquation.realForm; checks block_hamiltonian and block_ode_equivalent):

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

Section 15.5 derives why the interaction energy is subtracted here.

**Which levels are particles (CONVENTION).** The equations have levels of both signs. The convention of the record (ks-theory.json, thermodynamics.fillingConvention) is: particles occupy the **positive branch**, the levels whose value without interaction ($\lambda = 0$) at the same slice is positive, together with the **zero modes** at $k = 0$ (the levels $\varepsilon = 0$ of the free problem); the levels of the negative branch form the normal-ordered **sea** and are never occupied, not even at a temperature. The justification of this convention is OPEN; Section 15.26 measures where it stops being reasonable.

**The particle numbers.** The record uses three particle numbers (`Revision/kohn_sham/results/parameters.json`, particleNumbers). $N = 8$ fills exactly the eight zero modes at $k = 0$ (four blocks of each type). The next levels above the zero modes are the **brane band**, the lowest even level of block type $j = +1$ in each shell $n_2 \ge 1$ (Chapter 14 and Section 15.4); in the free gas at $a_{4,0} = 0$ the band levels increase with $n_2$, so filling them shell by shell gives **closed shells** (every level either full or empty). Line by line, with $g = 4r_3(n_2)$:

$$
8 + 4\big(r_3(1) + r_3(2) + r_3(3) + r_3(4)\big) = 8 + 4\,(6 + 12 + 8 + 6) = 8 + 128 = 136 .
$$

Rule: the eight zero modes plus four times the numbers of vectors in the shells 1 to 4. Continuing to $n_2 = 11$ with $r_3(5), \dots, r_3(11) = 24, 24, 0, 12, 30, 24, 24$:

$$
8 + 4\,(32 + 24 + 24 + 0 + 12 + 30 + 24 + 24) = 8 + 4\cdot170 = 688 .
$$

Rule: the sum $6 + 12 + 8 + 6 = 32$ of the first four shells plus the seven new shells. $N = 688$ is the largest closed shell whose highest level lies below the **bulk edge** $1.2922928$, the lowest level that is not on the brane band (the odd level at $k = 0$; parameters.json, particleNumbers.bulkEdge); $N = 136$ is the closed shell nearest to $688/4$.

**The couplings.** The coupling $\lambda$ is a constant of the theory, the same at every slice. For each $N$ the record chooses two values so that the interaction is a moderate perturbation along the whole history (parameters.json, couplingCalibration). In the free ground states of that $N$ at all five slices it takes the largest value over $y$ of $\max\big(\tfrac{15}{16}|S|, \tfrac{1}{16}n\big)$, the size of the mean-field potentials per unit $\lambda$ (called the **strength**), and sets $\lambda_1 = 0.1/\text{strength}$ and $\lambda_2 = 0.3/\text{strength}$, rounded to four significant digits; then the first-order potentials stay below $0.1\,m$ and $0.3\,m$. For $N = 8$ the strength is $5.138804$, so $\lambda_1 = 0.1/5.138804 = 0.019460$, rounded $0.01946$, and $\lambda_2 = 0.05838$. For $N = 136$ and $688$ the strengths are $107.548$ and $541.713$, so $\lambda_1 = 0.0009298$ and $0.0001846$, $\lambda_2 = 0.002789$ and $0.0005538$. The strength of $N = 136$ grows from $5.2$ at the first slice to $107.5$ at the last (parameters.json, strengthPerLambdaAtSlices): along the history the brane-band orbitals spread toward the tip, where the factor $P = e^{-6Hy}/\mathrm{Vol}_7$ is large. A calibration at the first slice alone would make the late states strongly coupled; this is why the whole history is used. The sign of $\lambda$ decides the kind of interaction: $\lambda > 0$ is repulsive, $\lambda < 0$ attractive. The run names use the tags `lam0`, `lamp1`, `lamm1`, `lamp2`, `lamm2` for $\lambda = 0, +\lambda_1, -\lambda_1, +\lambda_2, -\lambda_2$.

**The canonical matrix.** The solver computes a fixed list of states. **Ground states** ($T = 0$): three particle numbers $N = 8, 136, 688$, five couplings and five slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$, that is $3 \cdot 5 \cdot 5 = 75$ states. **Thermal states**: the same three $N$, the three couplings $0, \pm\lambda_1$, the five slices and three temperatures $T = 0.01, 0.02, 0.05$, that is $3\cdot3\cdot5\cdot3 = 135$ states. A state is named like `N136_lamp2_a20` ($N = 136$, $+\lambda_2$, $a_{4,0} = 2.0$; the last two digits are ten times the slice), and a thermal state carries in addition `_T10`, `_T20` or `_T50` (a thousand times the temperature).

**The numerical parameters** (parameters.json, numerics): $G = 900$ steps of the Runge-Kutta method on $[-L, 0]$, a root tolerance of $10^{-13}\,m$ for each level, a self-consistency tolerance of $10^{-11}\,m$ with at most 400 iterations, Anderson mixing with depth 6 and $\beta = 0.4$, and the step $\delta = 0.002$ in $a_4$ for derivatives along the history.

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

Rule: the first block equation says $j\varepsilon b = Ma - a'$. The same steps give $b'' = (M^2 - \varepsilon^2)b$. For $\varepsilon^2 > M^2$ put $p = \sqrt{\varepsilon^2 - M^2}$; then $b'' = -p^2b$, and the tip condition $b(-L) = 0$ leaves $b = B\sin\big(p(y + L)\big)$. Even parity, $b(0) = 0$: $\sin(pL) = 0$, so $p = n\pi/L$ and

$$
\varepsilon = \pm\sqrt{M^2 + (n\pi/L)^2}, \qquad n = 1, 2, \dots
$$

Odd parity, $a(0) = 0$: the second block equation gives $j\varepsilon a = b' + Mb$, so $a(0) = 0$ means $b'(0) + Mb(0) = 0$, that is $Bp\cos(pL) + MB\sin(pL) = 0$, or $\tan(pL) = -p/M$. Finally $\varepsilon = 0$: the equations become $a' = Ma$, $b' = -Mb$, so $b = 0$ (from $b(-L) = 0$) and $a = Ce^{My}$: the **zero mode**, which satisfies the even brane condition. Normalising, $\int_{-L}^{0}C^2e^{2My}dy = C^2(1 - e^{-2ML})/(2M) = 1$ gives $C = \sqrt{2M/(1 - e^{-2ML})}$. For $M = 1$, $L = 3$: the first even levels are $\pm\sqrt{1 + (\pi/3)^2} = \pm1.4479719$, and the first odd level is $\pm1.2922928$, the bulk edge of Section 15.2. Notebook 15e reproduces all of them by shooting.

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

**Label sets.** For a state of the gas the solver chooses the sectors and labels it will solve, its **label set**: every shell $n_2 = 0, 1, 2, \dots$ in turn, with all four sectors (two block types, two parities) of each shell, until the lowest level of a shell lies above the highest occupied level by a margin; in the occupied shells and the next one it solves three particle labels per sector, elsewhere the lowest only. The check ground_window_complete of the solver's report confirms for all 75 ground states that the lowest level outside the label set lies above the lowest empty level (the LUMO), so no level that matters was left out.

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

The record gives $0.4307337$, $0.1703493$ and $0.0641594$ at $a_{4,0} = 0, 1, 2$ (Notebook 15a, Out [7]). The ratios to the first value are $0.39549$ and $0.14895$, larger than $e^{-1} = 0.36788$ and $e^{-2} = 0.13534$: the gap shrinks somewhat more slowly than $e^{-a_{4,0}}$. The reason is visible in figure 4 of Notebook 15e: the band bends below its tangent line $c\,k$, so $\varepsilon_{band}(k)/k$ decreases with $k$; a redshifted momentum lies where the ratio is larger, closer to $c$. (Exercise 2 makes this precise.)

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

Rule: divide by 2, move $\nu$ to the left as the last unknown (with the sign it carries), and add the condition $\sum_k c_k = 1$ as the last row; $\mathbf 1$ is the column of $p$ ones. This is a small linear system of $p + 1$ equations. The solver adds $10^{-12}$ times the largest diagonal entry of $G$ to the diagonal (which keeps the system solvable when two residuals are nearly equal), drops the oldest pair when it still cannot be solved, and forgets the whole history when a residual grows to more than ten times the smallest seen so far (`Revision/kohn_sham/solver/src/scf.rs`). Notebook 15e writes exactly this in Python, and its figure 5 shows how much faster it converges than linear mixing.

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

This is PROVED for the mapped state; that the loop started from the free state finds exactly this state is COMPUTED (Notebook 15e finds $|E(+\lambda) + E(-\lambda)| = 0$ exactly, and the record lists $E_{KS} = \mp9.8684262\times10^{-4}$ for $\pm\lambda_1$). The symmetry is special to the zero modes: for larger $N$ the band orbitals have $k \ne 0$, the momentum term spoils the map, and repulsion raises the energy while attraction lowers it.

**The first excited state: Delta-SCF.** Chapter 13 defined the Kohn-Sham gap $\Delta_{KS} = \varepsilon_{LUMO} - \varepsilon_{HOMO}$ and the Delta-SCF energy $\Delta_{SCF} = E_1 - E_0$, the difference of two self-consistent energies, the second with one particle moved from the highest occupied level to the lowest empty one. The solver uses an **ensemble** form: it removes one particle uniformly from the whole highest occupied group of equal levels and adds it uniformly to the whole lowest empty group, so that every orbital of a group keeps the same occupation and the block and direction symmetry of the reduction is kept (parameters.json, conventions.deltaScf). Without interaction the levels do not depend on the occupations, so $\Delta_{SCF} = \Delta_{KS}$ exactly (Janak's theorem of Chapter 13 with constant levels); the solver checks this in all 15 free states (check excited_delta_scf_free_equals_gap, largest difference $2.0 \times 10^{-11}\,m$). With interaction the orbitals relax and the two differ by the **orbital relaxation** $\Delta_{SCF} - \Delta_{KS}$; for example for `N8_lamp2_a00` the record has $\Delta_{KS} = 0.4312996$ and $\Delta_{SCF} = 0.4312929$ (`Revision/kohn_sham/results/excited/summary.csv`).

### 15.6 Example: the solver's method by hand (Notebook 15e)

Notebook 15e writes the method of Sections 15.3 to 15.5 in plain Python, exactly as the Rust solver does it (`Revision/kohn_sham/solver/src/shoot.rs` and `scf.rs`), and reproduces numbers of the record: the grid and Simpson's rule; one shooting integration with the Pruefer angle; the phase function and the levels it labels (figure 1); Newton's method inside a bracket, the exact levels at $k = 0$ and the solver's own levels; the orbitals with Hermite midpoints (figure 2); the order 4 of RK4 (figure 3); the brane band, its slope and the rescaling identity (figure 4); the self-consistent loop with Anderson mixing for $N = 8$, compared with linear mixing (figure 5); the four couplings and the symmetry $E(-\lambda) = -E(\lambda)$; and the self-consistent potentials (figure 6). It needs no Rust, runs in about half a minute, and ends with ALL 18 CHECKS PASSED (notebook 15e).

<!-- NOTEBOOK 15e -->

### 15.9 Line-by-line walk-through of Notebook 15e

Draft.
