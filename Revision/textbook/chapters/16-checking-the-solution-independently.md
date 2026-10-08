## 16. Checking the solution independently: the reference solver and the cross-check

Chapter 15 solved the Kohn-Sham equations of the field dirac16complex in the author's primordial universe with one program, the Revision Rust solver, and read physics from its numbers: levels, energies, densities, pressures, heat capacities, all along the history in which ordinary 3-space inflates and the three extra times $x_5, x_6, x_7$ deflate exponentially. This chapter asks the question that every such calculation must answer before its numbers may be called results: how do we know that they are right? The Revision record answers it with a second program that shares no code with the first and solves the same equations by a different method (the **reference solver**), and with a third program that compares the two, number by number, with a rule for the allowed difference that was written down before any comparison was made (the **cross-check**). Three complete notebooks, 16a, 16b and 16c, repeat the essential steps and reproduce the numbers of the record.

### 16.1 What this chapter does

**Why checking is a chapter of its own.** A number printed by a program is not yet a result. Between the equations and the printed number stand a grid that replaces the continuous hidden direction by finitely many points, numbers in the computer that carry only about sixteen significant digits, thousands of lines of code in which a single wrong sign could hide, and the choices of the model itself. The first three can be tested by solving the same equations a second time in a completely different way: if two independent programs agree to many digits, within errors that each of them has measured, it is very unlikely that both are wrong in the same way. The fourth, the model, cannot be tested this way, because both programs share it; Section 16.25 says precisely what that means. The cross-check of the record did not only confirm the Rust solver: its first run failed, and the failure exposed a rounding error in the computation of the chemical potential that no test of either program alone had seen. This chapter tells that story too (Sections 16.20 to 16.24).

**What is done, in order.**

- Why a second program is needed and what agreement between two programs can and cannot show (Section 16.2).
- The two solvers side by side: what each one computes and how (Section 16.3).
- How the error of a grid calculation is measured: the order of convergence and the ratio test (Section 16.4), Richardson extrapolation and the uncertainty of the reference solver (Section 16.5), the canonical and refined runs that measure the uncertainty of the Rust solver (Section 16.6).
- The tolerance rule of the cross-check, derived line by line, and what the full cross-check of the record found (Sections 16.7 and 16.8).
- Notebook 16a, which runs the reference solver on five states, runs the Rust solver twice for each of them, applies the tolerance rule to 5140 comparisons and reproduces the worst cases of the record (Sections 16.9 to 16.12).
- Inside the reference solver: the exact levels of the free problem, the staggered grid, the matrix, counting eigenvalues, the exact discrete zero mode and the slope of the brane band (Sections 16.13 to 16.15), with Notebook 16b, which rebuilds the method by hand (Sections 16.16 to 16.19).
- How the cross-check caught a rounding error in the chemical potential, why sixteen digits were not enough, and how the computation was repaired (Section 16.20), with Notebook 16c (Sections 16.21 to 16.24).
- What the cross-check does not test, the closing summary and the exercises (Sections 16.25 to 16.27).

**The three notebooks.**

| notebook | what it computes | Rust | PASS lines | figures |
| --- | --- | --- | --- | --- |
| 16a | the reference solver on a subset of five states, the Rust solver with canonical and refined numerics, the tolerance rule on 5140 comparisons | yes | 51 | 7 |
| 16b | the method of the reference solver by hand on the free problem: exact levels, staggered grid, matrix, Sturm counts, bisection, zero mode, Richardson, brane-band slope | no | 31 | 7 |
| 16c | the chemical potential with 40 digits, the rounding staircase of the direct sum, the faulty value of the first cross-check reproduced, the repair, the rounding bounds for 45 states | no | 26 | 6 |

Notebook 16a is placed first because it shows the whole check at work; 16b then opens the reference solver and 16c the chemical potential.

**The status of every statement.** Every statement of this chapter carries one of the labels of Chapter 0.

- PROVED: the formulas of the method, each derived line by line in this chapter: the ratio test, Richardson extrapolation and why its uncertainty over-estimates the error, the factor $16/15$ of the Rust uncertainty, the tolerance rule as a consequence of the triangle inequality, the exact free levels (in the record: check bc_exact_k0_spectra of `Revision/kohn_sham/reports/ks-theory-python.json`), the staggered matrix and its symmetry, the pivots of the Sturm count, the exact discrete zero mode, the Hellmann-Feynman slope of the brane band (check brane_band_slope of the same report), the slope $dN/d\mu$ of the Mermin condition, Newton's method, the well-conditioned rewriting of the Mermin condition and the first-order rounding bounds. Two facts of linear algebra are quoted, not proved: Sylvester's law of inertia and the spectral theorem for symmetric matrices.
- COMPUTED: every number of the comparisons. The reference solver's own checks are in `Revision/kohn_sham/reports/ks-reference.json` (37 checks, all PASS), the cross-check in `Revision/kohn_sham/reports/ks-crosscheck.json` (29 checks, all PASS, 128313 comparisons) and its table `Revision/kohn_sham/reports/ks-crosscheck-table.csv`; the notebooks reproduce them, with the measured differences given with each number.
- ASSUMED: that the grid errors have the assumed form (even powers of the cell width for the reference, fourth order for the Rust solver). This is not proved for the self-consistent problem; it is tested by the ratio test on every level and by a fourth grid for one state (Sections 16.4 and 16.5). Also ASSUMED, as in Chapters 14 and 15: the good sector and the Z2 mirror brane at $y = 0$; CHOSEN: the regular tip at $y = -L$ with $L = 3$; CONVENTION, justification OPEN: which levels count as particles.
- PRESCRIBED BACKGROUND: the history $a_4 = AHx_4$ with $A = 1$ (the Kohn-Sham states violate the conditions that the $a_4$ field equations put on their source: `Revision/field_equations_a4/reports/ks-source-conditions.json`).
- OPEN: the time-dependent (non-adiabatic) problem. HYPOTHESIS: none is used in this chapter.

**What this chapter does not touch.** Nothing in this chapter concerns pairs of universes, their creation, or matter and antimatter. The cross-check compares two programs that solve the same Kohn-Sham equations; it says nothing about whether any universe is created, in pairs or otherwise. The pairing theorems and their exact scope are the subject of Chapters 18 to 21.

**Notation and units.** The author's coordinates are $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates with the scale factor $e^{a_4}\sin^{1/6}z$; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which deflate exponentially with the scale factor $e^{-a_4}\sin^{1/6}z$; $x_8$ is the hidden space direction, with $z = 6Hx_8$ between 0 and $\pi/2$. The hidden coordinate is $y = \ln(\sin z)/(6H)$; it runs from the **tip** $y = -L$ to the **brane** $y = 0$. A **slice** is one instant of the history, and $a_{4,0}$ is the value of $a_4$ there. In all numbers $H = 1$ and $m = 1$, so energies and temperatures are in units of $m$ and lengths in units of $1/H$. A state of the record is named like N136_lamp2_a20: $N = 136$ quanta, the coupling $+\lambda_2$ (the tags lam0, lamp1, lamm1, lamp2, lamm2 stand for $\lambda = 0, +\lambda_1, -\lambda_1, +\lambda_2, -\lambda_2$), the slice $a_{4,0} = 2.0$ (the two digits are ten times the slice); a thermal state ends in T10, T20 or T50 for the temperatures $T = 0.01$, $0.02$, $0.05$.

### 16.2 Why a second program, and what agreement can show

**Four kinds of error.** Suppose a program prints a number $x$ for a quantity whose exact value is $X$. The **error** of $x$ is the difference $x - X$. It has four sources.

- The **discretisation error**: the program replaces the continuous interval $-L \le y \le 0$ by finitely many points, so it solves a nearby problem, not the exact one. This error shrinks when the points are made denser.
- The **rounding error**: the computer stores each number with about sixteen significant digits (Section 16.20 explains exactly how), so almost every operation makes a tiny error, and long sums can make larger ones.
- **Mistakes in the program**: a wrong sign, a wrong index, a forgotten term. They do not shrink when the grid is refined.
- **Errors of the model or of its inputs**: a wrong formula in the theory, a wrong boundary condition, a wrong constant. The program then solves the wrong equations correctly.

**What a second program tests.** The record's reference solver is a second program written for this purpose. It shares no code with the Rust solver; it is written in another language (Python instead of Rust); it uses a different numerical method (a matrix on a grid instead of step-by-step integration, Section 16.3); and its only physics input is the theory file `Revision/kohn_sham/ks-theory.json`, which the Rust solver reads as well. Discretisation errors of two different methods are different, rounding errors take different paths, and a mistake in one program is very unlikely to be repeated, with the same size, in the other. So if the two programs agree within their measured errors, then, with high confidence, neither has a discretisation, rounding or programming error larger than those errors. But an error of the fourth kind is shared: both programs read the same theory file and use the same boundary conditions, so they would agree even if the model were wrong. The cross-check tests the numerics, not the physics model.

**Uncertainty, tolerance, ratio.** Neither program knows its own error exactly (otherwise it could subtract it). What each can do is measure an **uncertainty**: a number $U$ that, for reasons given in Sections 16.5 and 16.6, should be at least as large as the size $|x - X|$ of its error. The **tolerance** is the largest difference between the two programs that the comparison allows; Section 16.7 derives it from the two uncertainties. The **ratio** of a comparison is the difference of the two programs divided by the tolerance; the comparison passes when the ratio is at most 1.

**Why the tolerance must be fixed in advance.** A tolerance that is chosen after looking at the differences can always be made large enough for everything to pass, and then the comparison tests nothing. The record therefore fixes the tolerance rule in the cross-check program before any comparison and never adjusts it to a result (`Revision/kohn_sham/checker/crosscheck_ks.py`, its header, and the README of `Revision/kohn_sham/checker`). The rule was tested by its first use: it failed in one state, the tolerance was not widened, and the cause was found and repaired (Section 16.20).

### 16.3 The two solvers

**The equations both solve.** Both programs solve the Kohn-Sham problem of Chapters 14 and 15. At a slice $a_{4,0}$ an orbital of block type $j = \pm1$ with 3-momentum of length $k$ is a pair of real functions $a(y)$, $b(y)$ that obey

$$
a' = M a - \big(\kappa k + j(\varepsilon - v)\big)\,b, \qquad b' = \big(j(\varepsilon - v) - \kappa k\big)\,a - M b, \qquad \kappa = e^{-Hy - a_{4,0}},
$$

where the prime is $d/dy$, $\varepsilon$ is the level, $M(y) = m + \tfrac{15}{16}\lambda S(y)$ the effective mass and $v(y) = -\tfrac{1}{16}\lambda n(y)$ the potential (`Revision/kohn_sham/ks-theory.json`, blockEquation.realForm and exchange.kohnShamPotentials). The boundary conditions are the regular tip $b(-L) = 0$ (CHOSEN) and the ASSUMED Z2 brane: even orbitals have $b(0) = 0$, odd orbitals $a(0) = 0$. The densities $n$ and $S$ are sums over the occupied orbitals, so the potentials depend on the solution, and the problem is solved again and again until it reproduces itself (self-consistency). At a temperature $T > 0$ the occupations are Fermi-Dirac numbers $f = 1/(1 + e^{(\varepsilon - \mu)/T})$, and the chemical potential $\mu$ is fixed by $\sum g f = N$. The list of states, the **canonical matrix**, holds 75 ground states (three particle numbers, five couplings, five slices) and 135 thermal states (three particle numbers, three couplings, five slices, three temperatures).

**The Rust solver** (Chapter 15). For a trial energy it integrates the two equations from the tip to the brane with the Runge-Kutta rule RK4 in $G = 900$ steps, counts levels with the Pruefer angle, and finds each level by Newton's method inside a bracket to a tolerance of $10^{-13}$; self-consistency is reached with Anderson mixing to a residual of $10^{-11}$ (`Revision/kohn_sham/results/parameters.json`, numerics).

**The reference solver** (`Revision/kohn_sham/reference/run_reference.py` with the module `ks_fd.py` in the same folder). It places the two functions of an orbital on a **staggered grid** of $G$ cells: $a$ at the centres of the cells and $b$ at their ends. The differential equations then become the eigenvalue problem of a symmetric **tridiagonal matrix** with $2G - 1$ rows (a matrix whose only nonzero entries are on the main diagonal and its two neighbours). It finds each eigenvalue by its number, by counting how many eigenvalues lie below a trial value (the **Sturm count**) and halving an interval (**bisection**), so that no level can be missed; it then sharpens each eigenvalue and computes its eigenvector. Every quantity is computed on three grids, $G = 300$, $600$ and $1200$, and the three results are combined by **Richardson extrapolation** (Section 16.5) into a value $R$ with a measured uncertainty $U$. Self-consistency is reached with Anderson mixing to a residual of $10^{-12}$. The reference re-derives from their stated rules even the inputs it could have copied: the particle numbers 136 and 688 and the couplings $\lambda_1$, $\lambda_2$ (for $N = 8$: $0.01946$ and $0.05838$; `Revision/kohn_sham/reports/ks-reference.json`, check parameters_calibration).

**Side by side.**

| | Rust solver | reference solver |
| --- | --- | --- |
| language | Rust | Python with numpy |
| method | shooting with RK4 from the tip to the brane | staggered finite differences, one matrix per sector |
| finding a level | Pruefer count and Newton's method | Sturm count and bisection |
| grid | $G = 900$ steps | $G = 300$, $600$, $1200$ cells |
| error of one grid | proportional to $h^4$ | proportional to $h^2$ |
| uncertainty | canonical minus refined run (Section 16.6) | Richardson extrapolation (Section 16.5) |
| self-consistency | residual at most $10^{-11}$ | residual at most $10^{-12}$ |
| results | `Revision/kohn_sham/results` | `Revision/kohn_sham/reference/results` |

**What the reference computes for each state.** A ground-state **job** (one unit of work of the program) solves the state, its Delta-SCF excited state (one quantum moved from the highest occupied to the lowest empty group of levels), four neighbouring slices $a_{4,0} \pm 0.002$ and $a_{4,0} \pm 0.004$ at fixed occupations (for the derivative $dE/da_4$ and the adiabaticity measure of Chapter 15), and the list of the lowest particle-hole excitations, each on the three grids. A thermal job solves the state and four neighbouring temperatures $T(1 \pm 0.01)$, $T(1 \pm 0.02)$ (for the heat capacity). The program also solves an exact-exchange variant of the 60 states with $\lambda \ne 0$, the rescaling partners of the 60 states with $a_{4,0} > 0$, a demonstration of a level crossing, and one state on a fourth grid (Section 16.5). Its report `Revision/kohn_sham/reports/ks-reference.json` records 37 checks of the reference on itself, all PASS.

### 16.4 Order of convergence: the ratio test

**The error of a grid calculation.** Let a grid have cells of width $h$ ($h = L/G$ for $G$ cells), and let $x(h)$ be a number computed on it whose exact value is $X$. For the staggered grid of the reference the error has an expansion in even powers of $h$ (Section 16.14 shows where the even powers come from):

$$
x(h) = X + c\,h^2 + d\,h^4 + e\,h^6 + \dots ,
$$

where the numbers $c$, $d$, $e$ do not depend on $h$. Such a method is said to be of **second order** (or to have **order of convergence** 2), because for small $h$ the first term $c\,h^2$ dominates: halving $h$ divides the error by about $2^2 = 4$. The expansion is ASSUMED for the self-consistent problem; the ratio test below checks it on the computed numbers themselves.

**The ratio test, line by line.** Compute $x$ on three grids with the cell widths $h$, $h/2$ and $h/4$ (for the reference $G = 300$, $600$, $1200$, that is $h = 0.01$, $0.005$, $0.0025$).

$$
x(h) - x(h/2) = c\,h^2 - c\,\tfrac{h^2}{4} + d\,h^4 - d\,\tfrac{h^4}{16} + \dots = \tfrac34\,c\,h^2 + \tfrac{15}{16}\,d\,h^4 + \dots
$$

Rule: subtract the expansion with $h/2$ in place of $h$ from the expansion with $h$; $X$ cancels, and $(h/2)^2 = h^2/4$, $(h/2)^4 = h^4/16$.

$$
x(h/2) - x(h/4) = \tfrac34\,c\,\tfrac{h^2}{4} + \tfrac{15}{16}\,d\,\tfrac{h^4}{16} + \dots
$$

Rule: the same subtraction with $h/2$ in place of $h$, so every $h^2$ gets a factor $\tfrac14$ and every $h^4$ a factor $\tfrac{1}{16}$.

$$
\frac{x(h) - x(h/2)}{x(h/2) - x(h/4)} = \frac{\tfrac34 c\,h^2\,(1 + \tfrac54\tfrac{d}{c}h^2 + \dots)}{\tfrac{3}{16} c\,h^2\,(1 + \tfrac{5}{16}\tfrac{d}{c}h^2 + \dots)} = 4\,\Big(1 + \tfrac{15}{16}\,\tfrac{d}{c}\,h^2 + \dots\Big).
$$

Rule: take $\tfrac34 c h^2$ and $\tfrac3{16} c h^2$ out of the two brackets ($\tfrac{15}{16}/\tfrac34 = \tfrac54$ and $\tfrac{15}{256}/\tfrac{3}{16} = \tfrac{5}{16}$), then divide, using $1/(1 + s) = 1 - s + \dots$ for small $s$, so that $\tfrac54 - \tfrac{5}{16} = \tfrac{15}{16}$.

So the **convergence ratio** $(x(h) - x(h/2))/(x(h/2) - x(h/4))$ is 4 up to a correction of order $h^2$. A ratio close to 4 shows that the grids are fine enough for the $h^2$ term to dominate (the **asymptotic regime**), which is what Richardson extrapolation needs. The test uses only computed numbers, not the unknown $X$.

**An example from the record.** Notebook 16a prints the Kohn-Sham energy of the state N136_lamp2_a20 on the three grids: $E_{KS}(300) = 12.449082943357$, $E_{KS}(600) = 12.449020346521$, $E_{KS}(1200) = 12.449004697554$. The two differences are $6.2597\times10^{-5}$ and $1.5649\times10^{-5}$, and their ratio is $4.00006$: second order, in the asymptotic regime. The reference applies the test to every level of every ground state and requires the median ratio of each state to lie within $0.05$ of 4; the worst state is within $7.4\times10^{-5}$ of 4 (`Revision/kohn_sham/reports/ks-reference.json`, check richardson_asymptotic_ratio).

### 16.5 Richardson extrapolation and the uncertainty of the reference

**The idea.** If we know the form of the error, we can combine results on several grids so that the leading error terms cancel. This is **Richardson extrapolation**, named after the meteorologist Lewis Fry Richardson, who used it in 1911.

**One step, line by line.** Start from the expansion of Section 16.4 on the grids $h$ and $h/2$.

$$
x(h/2) = X + c\,\tfrac{h^2}{4} + d\,\tfrac{h^4}{16} + \dots
$$

Rule: put $h/2$ in place of $h$ in the expansion.

$$
4\,x(h/2) - x(h) = 3X + \big(1 - 1\big)\,c\,h^2 + \big(\tfrac{4}{16} - 1\big)\,d\,h^4 + \dots = 3X - \tfrac34\,d\,h^4 + \dots
$$

Rule: multiply the line above by 4 and subtract the expansion for $h$; the $c\,h^2$ terms cancel because $4\cdot\tfrac14 = 1$.

$$
r(h) = \frac{4\,x(h/2) - x(h)}{3} = X - \tfrac14\,d\,h^4 + \dots
$$

Rule: divide by 3. The **one-step value** $r(h)$ has no $h^2$ error left; its error starts with $h^4$.

**The second step, line by line.** The same step on the finer pair $h/2$, $h/4$ gives

$$
r(h/2) = \frac{4\,x(h/4) - x(h/2)}{3} = X - \tfrac14\,d\,\tfrac{h^4}{16} + \dots = X - \tfrac{1}{64}\,d\,h^4 + \dots
$$

Rule: the line before, with $h/2$ in place of $h$, so $h^4$ becomes $h^4/16$.

$$
16\,r(h/2) - r(h) = 15X + \big(-\tfrac{16}{64} + \tfrac14\big)\,d\,h^4 + \dots = 15X + \dots
$$

Rule: multiply by 16 and subtract $r(h)$; the $h^4$ terms cancel because $16\cdot\tfrac1{64} = \tfrac14$. What remains are terms of order $h^6$.

$$
R = \frac{16\,r(h/2) - r(h)}{15} = X + O(h^6).
$$

Rule: divide by 15. The notation $O(h^6)$ means terms that are at most a constant times $h^6$.

**The same value in one line.** Insert the two one-step values:

$$
16\,r(h/2) - r(h) = \frac{64\,x(h/4) - 16\,x(h/2)}{3} - \frac{4\,x(h/2) - x(h)}{3} = \frac{64\,x(h/4) - 20\,x(h/2) + x(h)}{3}.
$$

Rule: $16 \cdot \tfrac{4x(h/4) - x(h/2)}{3}$ multiplied out, then the two fractions with the same denominator subtracted, collecting $-16 - 4 = -20$ for $x(h/2)$.

$$
R = \frac{64\,x(h/4) - 20\,x(h/2) + x(h)}{45}.
$$

Rule: divide by 15, and $3\cdot15 = 45$. The three weights add up to $(64 - 20 + 1)/45 = 1$, as they must: if all three grids gave the same number, $R$ would be that number.

**The uncertainty.** The reference states as the uncertainty of $R$

$$
U = \big|R - r(h/2)\big| + 2\cdot10^{-12}\max(1, |R|).
$$

Why this is a safe estimate, line by line:

$$
R - r(h/2) = \Big(X + O(h^6)\Big) - \Big(X - \tfrac{1}{64}d\,h^4 + O(h^6)\Big) = \tfrac{1}{64}\,d\,h^4 + O(h^6).
$$

Rule: subtract the two expansions derived above; $X$ cancels.

So the first term of $U$ is the size of the $h^4$ error of the finest one-step value $r(h/2)$, while $R$ itself has only an $h^6$ error. When $h$ is small, $h^6$ is much smaller than $h^4$, so $U$ is larger than the error of $R$: it over-estimates it. The second term, $2\cdot10^{-12}$ times the size of $R$ (at least 1), is a **floor** for the rounding errors of the computer, which do not shrink with $h$.

**An example.** For N136_lamp2_a20 the one-step values are $r(h) = 12.448999480909$ and $r(h/2) = 12.448999481232$, the three-grid value is $R = 12.448999481253$, and $U = 4.6\times10^{-11}$ (Notebook 16a, In [6]; the record has $R = 12.44899948125322$ with $U = 4.6\times10^{-11}$, `Revision/kohn_sham/reference/README.md`). The single grid $G = 1200$ is $5.2\times10^{-6}$ away from $R$; two Richardson steps have gained five significant digits.

**Testing the uncertainty on a fourth grid.** The argument above rests on the ASSUMED form of the error. The record tests it. One state, N136_lamp2_a20 (the strongest coupling, with the largest densities at the tip), is solved on a fourth grid as well, $G = 2400$. From $(300, 600, 1200)$ the three-grid value $R_{123}$ with its uncertainty $U_{123}$ is formed, and from $(600, 1200, 2400)$ the three-grid value $R_{234}$. The error of $R_{234}$ is of order $(h/2)^6 = h^6/64$, so it is about 64 times smaller than the error of $R_{123}$; hence $|R_{123} - R_{234}|$ is practically the error of $R_{123}$, and the test is whether it is at most $U_{123}$. For all 19 classes of quantities (energies, levels, integrals, values at the tip and at the brane, five profiles with 151 points each) it is: the largest ratio $|R_{123} - R_{234}|/U_{123}$ is $0.787$, for the value of the pressure $p_8$ at the tip (`Revision/kohn_sham/reports/ks-reference.json`, check richardson_uncertainty_validated). Notebook 16a repeats this test (In [7], Figure 16a.2). The uncertainty is therefore an honest estimate, and it is not hugely larger than the error either, which a useful estimate must also be.

### 16.6 The uncertainty of the Rust solver: canonical and refined runs

**The idea.** The Rust solver uses the Runge-Kutta rule RK4, whose error over the whole interval is proportional to $h^4$ for the step width $h = L/G$ (Chapter 2). If the step is halved, the error is divided by $2^4 = 16$. The record therefore runs every state twice: with the **canonical numerics** of the committed results and with the **refined numerics**, which halve the step and tighten the other tolerances. The canonical numerics are $G = 900$ steps, a root tolerance of $10^{-13}$ and a self-consistency tolerance of $10^{-11}$; the refined numerics are $G = 1800$, $10^{-14}$ and $10^{-12}$ (`Revision/kohn_sham/checker/measure_rust_refinement.py`, which writes `Revision/kohn_sham/checker/rust-refinement.json`).

**The factor 16/15, line by line.** Let $e$ be the error of the canonical result $x_c$, so $x_c = X + e$, and let the refined result be $x_r$.

$$
x_r = X + \tfrac{e}{16}.
$$

Rule: halving the step of a fourth-order method divides the error by $2^4 = 16$ (ASSUMED error model; the other tolerances are tightened so that they do not spoil it).

$$
x_c - x_r = e - \tfrac{e}{16} = \tfrac{15}{16}\,e.
$$

Rule: subtract the two lines; $X$ cancels.

$$
e = \tfrac{16}{15}\,(x_c - x_r), \qquad U_{Rust} = \tfrac{16}{15}\,|x_c - x_r|.
$$

Rule: multiply by $\tfrac{16}{15}$; the size of the canonical error is the **Rust uncertainty**.

So the difference between the two runs, which can be measured, gives the error of the canonical run, which cannot. For example, Notebook 16a (In [13]) measures $|x_c - x_r| = 7.529\times10^{-10}$ for the Kohn-Sham energy of N688_lam0_a00, so $U_{Rust} = \tfrac{16}{15}\cdot7.529\times10^{-10} = 8.03\times10^{-10}$.

**Two conditions.** First, the measured difference applies to the committed results only if the canonical run made for the measurement reproduces them. The record checks this for every state: the canonical runs reproduce the committed matrix with every difference zero (`Revision/kohn_sham/reports/ks-crosscheck.json`, check rust_refinement_applies_to_matrix). Second, some quantities (the Delta-SCF energy, the adiabaticity measure, the finite-difference $dE/da_4$, the heat capacity) are not printed by the single runs of the measurement. For them the cross-check uses the largest canonical-minus-refined difference over the whole canonical matrix, taken from the Rust solver's determinism report; the values are listed in `Revision/kohn_sham/reports/ks-crosscheck.json` under rust_matrix_wide_uncertainties (for example $2.135\times10^{-9}$ for the levels and $5.689\times10^{-9}$, relative, for the heat capacity).

### 16.7 The tolerance rule, fixed in advance

**The rule.** For every number that both programs compute, the cross-check requires

$$
|x_{Rust} - x_{ref}| \le 3\,(U_{ref} + U_{Rust}) + 10^{-12}\cdot s ,
$$

where $U_{ref}$ is the Richardson uncertainty of the reference, $U_{Rust}$ the measured uncertainty of the Rust solver, and the **scale** $s$ is $\max(1, |x_{ref}|)$ for a single number and the largest value of the profile for a point of a profile. The right side is the **tolerance**, and the left side divided by the right side is the **ratio**.

**Why the two uncertainties are added, line by line.** Let $X$ be the exact value.

$$
x_{Rust} - x_{ref} = (x_{Rust} - X) - (x_{ref} - X).
$$

Rule: add and subtract $X$.

$$
|x_{Rust} - x_{ref}| \le |x_{Rust} - X| + |x_{ref} - X|.
$$

Rule: the **triangle inequality** $|p - q| \le |p| + |q|$ for any two numbers $p$, $q$.

$$
|x_{Rust} - x_{ref}| \le U_{Rust} + U_{ref}.
$$

Rule: each uncertainty is at least the size of its program's error (that is what an uncertainty is meant to be).

So if both uncertainties are honest, the difference can never exceed their sum. The rule allows three times the sum, because the uncertainties are estimates, not proven bounds (Sections 16.5 and 16.6 explain the assumptions behind them): the factor 3 keeps a comparison from failing merely because an estimate was a little too small, while a real mistake, which usually produces differences many times the uncertainties, still fails. The last term, $10^{-12}$ times the scale, is a floor for rounding, which neither uncertainty measures.

**Propagated uncertainties, line by line.** Some compared quantities are built from others, and their uncertainties are added up the same way. The free energy is $F = E - TS$, so

$$
F_{Rust} - F = (E_{Rust} - E) - T\,(S_{Rust} - S), \qquad U_F = U_E + T\,U_S .
$$

Rule: subtract the exact $F = E - TS$ from the computed one, then apply the triangle inequality as above. In the same way the grand potential $\Omega = F - \mu N$ gets $U_\Omega = U_F + N\,U_\mu$. The derivative of the energy along the history has the energy-momentum form $dE/da_4 = -6\,\mathrm{Vol}_7\int e^{6Hy}(p_3 - p_t)\,dy = -3\,(I_3 - I_t)$, where $I_3$ and $I_t$ are the integrals $2\,\mathrm{Vol}_7\int e^{6Hy}p_3\,dy$ and $2\,\mathrm{Vol}_7\int e^{6Hy}p_t\,dy$ that the solvers report; hence its uncertainty is $3\,(U_{I_3} + U_{I_t})$. The exchange difference $\Delta E_x = \tfrac{\lambda}{32}\,2\,\mathrm{Vol}_7\int e^{6Hy}Q^2\,dy$ is quadratic in the profile $Q$, and a relative change $\delta$ of $Q$ changes $Q^2$ by the relative amount $(1 + \delta)^2 - 1 = 2\delta + \delta^2 \approx 2\delta$; hence its uncertainty is twice the relative uncertainty of $Q$ times $|\Delta E_x|$.

**A floor for difference quotients.** The heat capacity is also computed as $dE/dT$, a **difference quotient**: energies at the temperatures $T \pm dT$ (and $T \pm 2dT$) are subtracted and divided by multiples of $dT = 0.01\,T$. Each energy comes from a self-consistent calculation that stops when its residual is below a tolerance, so each energy carries a small noise of about $N$ times that tolerance, and dividing by $dT$ magnifies the noise to about $N\times\text{tolerance}/dT$. The cross-check adds this floor for each solver: $N\cdot10^{-13}/dT$ for the Rust solver (its root tolerance) and $N\cdot10^{-12}/dT$ for the reference (its self-consistency tolerance).

**A worked comparison.** Notebook 16a (In [14]) shows every piece of one comparison, the Kohn-Sham energy of N8_lamm2_a00. Rust gives $0.002862652173608389$ and the reference $0.002862652173734779$, a difference of $1.264\times10^{-13}$. The uncertainties are $U_{ref} = 2.096\times10^{-12}$ and $U_{Rust} = 1.214\times10^{-13}$. The tolerance is

$$
3\,(2.096 + 0.1214)\times10^{-12} + 10^{-12}\cdot1 = 6.652\times10^{-12} + 1.000\times10^{-12} = 7.652\times10^{-12},
$$

Rule: insert the numbers; the scale is $\max(1, 0.00286) = 1$. The ratio is $1.264\times10^{-13}/7.652\times10^{-12} = 0.0165$: the two programs agree to less than a sixtieth of what the rule allows.

### 16.8 What the full cross-check found

The cross-check program `Revision/kohn_sham/checker/crosscheck_ks.py` compares the full canonical matrix. Its report `Revision/kohn_sham/reports/ks-crosscheck.json` holds 29 checks, all PASS, with 128313 comparisons in all. Nineteen of the checks are classes of comparisons; for each, the table gives the number of comparisons and the largest ratio found (from the details of the checks in that report).

| check | what is compared | comparisons | largest ratio |
| --- | --- | --- | --- |
| ground_occupations_and_groups | occupied levels, occupations, HOMO and LUMO groups | 300 | identical |
| ground_energies | $E_{KS}$, $E_{band}$, $E_{int}$ | 225 | 0.148 |
| ground_homo_lumo_gap | HOMO, LUMO, Kohn-Sham gap | 225 | 0.001 |
| ground_eigenvalues | every level present in both label sets | 9616 | 0.324 |
| excited_delta_scf | Delta-SCF energy, excited energy | 150 | 0.296 |
| excited_particle_hole_lists | particle-hole excitations | 4842 | 0.001 |
| emt_integrals | the five energy-momentum integrals | 375 | 0.225 |
| emt_brane_tip_values | $\rho$, $p_3$, $p_t$, $p_8$ at the brane and the tip | 600 | 0.495 |
| ground_profiles | ten profiles at 151 points | 113250 | 0.495 |
| exchange_delta_E_x | the exchange difference $\Delta E_x$ | 75 | 0.044 |
| adiabatic_dE_da4 | $dE/da_4$ in two forms | 150 | 0.122 |
| adiabatic_Q_max | the adiabaticity measure and its pair | 225 | 0.314 |
| exx_variant_scf | the exact-exchange variant | 240 | 0.128 |
| rescaling_partners | the rescaling partners | 180 | 0.137 |
| crossing_demonstration | the level-crossing demonstration | 31 | 0.111 |
| thermo_state_functions | $\mu$, $E$, $S$, $F$, $\Omega$ in two forms | 810 | 0.284 |
| thermo_derivatives | $C_V$, $dE/dT$, $-dF/dT$ | 405 | 0.226 |
| thermo_sea_hole_diagnostic | the sea-hole diagnostic of the filling convention | 270 | 0.048 |
| thermo_mu_high_precision | $\mu$ recomputed with 40 digits, and $\Omega$ with it | 270 | 0.050 |

The other ten checks are preconditions and consistency tests: the three input reports pass every check (inputs_all_pass: at the time of the cross-check the reference report had 37 of 37, the Rust solver report 42 of 42 and the Rust determinism report 14 of 14); the canonical single runs reproduce the committed matrix (rust_refinement_applies_to_matrix, and its exact-exchange variant); both solvers solve the same problem and read the same theory file (problem_definition_identical); the reference re-derives the same particle numbers and couplings (parameters_particle_numbers, parameters_couplings); the floating-point chemical potentials lie within their rounding bounds (thermo_mu_rounding_diagnostic, Section 16.20); and the reference's own output is reproducible: the cross-check runs the reference a second time into a fresh folder and finds all 340 result files and the report byte for byte identical (reference_outputs_lf_only, reference_manifest, reference_repeat_byte_identical).

**What the table shows.** No comparison of the whole matrix uses even half of its tolerance: the largest ratio is $0.495$, for the energy density $\rho$ at the tip of N8_lamm2_a00, where the densities are largest and both programs are least accurate. Many ratios are far smaller. Status: COMPUTED; the record files are named above, and Notebook 16a reproduces the worst case of six of the classes.

### 16.9 Example: the reference solver on a subset and the cross-check (Notebook 16a)

Notebook 16a repeats the cross-check for a **subset** of five states: three ground states and two thermal states, four of them chosen because the full cross-check found its largest ratios there, and the fifth (N688_lam0_a00) because it has the most quanta. It runs the reference program of the repository on these states and on the fourth grid, checks that every new number reproduces the committed reference files, shows the convergence and Richardson extrapolation at work, builds and runs the Rust solver with its canonical and its refined numerics, applies the tolerance rule of Section 16.7 to 5140 comparisons, and reproduces 97 rows of the committed comparison table and the worst cases of six classes of the full cross-check. It needs Rust, takes about four minutes on a fast computer, draws seven figures and ends with the line ALL 51 CHECKS PASSED (notebook 16a).

<!-- NOTEBOOK 16a -->

### 16.12 Line-by-line walk-through of Notebook 16a

The notebook has 23 code cells, In [1] to In [23]. This section explains every line of every one of them, in order. In the notebook each code cell is preceded by a text cell that says what the cell does; the numbers that the cells print are in Section 16.11 under the labels Out [k].

**In [1], the set-up cell.** It is the same in every notebook of the book except for the notebook's name and, in notebooks that run a Rust program, two more imports and the function `rust_program`; the walk-throughs of Notebooks 16b and 16c refer back to this paragraph. Its first 296 lines repeat the complete run instructions of Section 16.10 as **comment lines**: every line that starts with `#` is skipped by Python and is there only so that the notebook file carries its own instructions. Two lines of `=` signs around the title THE SET-UP mark where the code begins.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
import shutil  # finds the program cargo
import subprocess  # runs cargo and the Rust programs

NOTEBOOK_ID = "16a"  # this notebook: chapter 16, example a
```

`import` loads a **module** (a part of Python or of an installed package) so that the cell can use it; the text after `#` on each line says what the module is for. `json` reads and writes JSON files, the text format in which most Revision records are stored (names and numbers in braces). `os` gives access to the operating system, here to read an environment variable. `textwrap` breaks long printed text into lines. `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or folder, written the same way on Windows, macOS and Linux. `matplotlib` is the plotting package, and `matplotlib.pyplot` its drawing functions, called `plt` by convention. `Image` and `display` show a saved picture below a cell. `shutil` can find a program on the computer (here cargo, the Rust build tool) and `subprocess` can run one. The last line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"16a"`; the figure files are named after it.

```python
def find_repository_root():
    """Return the repository folder (Dirac_claude).

    Jupyter runs a notebook in the folder that holds it.  Starting there, go up one
    folder at a time until a folder contains Revision/textbook/requirements.txt (the
    list of the book's packages); that folder is the repository."""
    here = Path.cwd().resolve()  # the folder in which this notebook runs
    for folder in [here, *here.parents]:  # this folder, its parent, its grandparent ...
        if (folder / "Revision" / "textbook" / "requirements.txt").is_file():
            return folder
    raise FileNotFoundError(
        "The repository folder was not found: open this notebook inside the folder "
        "Revision/textbook/notebooks of the repository Dirac_claude")
```

`def` defines a **function**, a named piece of code that runs when it is called; the text in triple quotes under the `def` line is its **docstring**, a description that Python stores but does not run. `Path.cwd()` is the folder in which the notebook runs, and `.resolve()` writes it as a complete address. The list `[here, *here.parents]` holds this folder followed by its parent, the parent of that, and so on up to the top of the disk (the star unpacks the parents into the list); the `for` loop takes them one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back; if none does, `raise` stops the notebook with an error message that says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))

def repository_file(relative):
    """The path of the repository file relative, for READING (a Revision record)."""
    return REPO / relative

def output_file(relative):
    """The path at which to WRITE the repository file relative (its folder is made)."""
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path

def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`REPO` is the repository folder; it is never printed, because it differs from computer to computer while the printed output of the notebook must be the same everywhere. `os.environ.get(name, default)` reads an **environment variable** (a named text that a program receives from the computer) or returns the default; when you run the notebook the variable TEXTBOOK_OUTPUT_ROOT is not set, so `OUTPUT_ROOT` is the repository, while the book's checking tool sets it to a scratch folder so that a check never changes the repository. `repository_file` gives the full path of a repository file for reading; `output_file` gives the full path at which to write one, after creating its folder (`mkdir` with `parents=True` creates missing parent folders too, and `exist_ok=True` makes it do nothing if the folder exists). `say` prints a text in lines of at most 89 characters (the width of a page of the book), continuation lines starting with four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})

FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

`matplotlib.rcdefaults()` returns to the built-in plotting settings, so that the figures are the same on every computer, and `plt.rcParams.update` sets the figure size (7.0 by 4.2 inches), the letter size (10 points) and a faint grid. The braces `{...}` make a **dictionary**: pairs of a key and a value, written `key: value`. A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/16a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty dictionary `{}` into the captions file; `newline="\n"` stores the same line end on every operating system.

```python
def save_figure(fig, name, caption):
    """Save the figure fig as Revision/textbook/figures/<id>_<k>_<name>.png, record its
    caption in CAPTION_FILE, show the saved picture below the cell and close the figure.
    k counts the figures of the notebook 1, 2, 3, ...; a cell run again keeps its k."""
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
    # dpi=150: 150 dots per inch.  bbox_inches="tight": cut away the empty margin.
    # metadata={"Software": None}: no program name is stored in the PNG file, so that
    # every run writes exactly the same bytes.
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

`save_figure` numbers the figures 1, 2, 3, ... in the order in which they are saved (`setdefault` returns the number already stored for this name, or stores one more than the count so far), saves the figure as a PNG file with 150 dots per inch, cut to its content and without the program's name in the file (so that two runs write the same bytes), closes it, records its caption in the captions file (`json.dumps` turns the dictionary into JSON text, with one entry per line and the keys sorted), shows the saved picture below the cell, and prints where it was saved. The caption given to it is the caption that the book prints under the figure.

```python
PASSED = []  # the names of the checks that passed, in order

def check(condition, name, record=None):
    """A check.  If condition is False, stop with an AssertionError that names the
    check (an if statement is used instead of assert, because python -O would skip an
    assert).  Otherwise print "PASS <name>" and, when the check reproduces a Revision
    record, a second line naming the record file and its check."""
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")

def report(label, value, unit=""):
    """Print a key number as a line "RESULT <label> = <value> <unit>"."""
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))

def all_checks_passed():
    """Print the last line of the notebook: how many checks passed."""
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")
```

`PASSED` is an empty **list** (an ordered collection, in square brackets). `check` is the function behind every check of the notebook: if the statement `condition` is false, `raise AssertionError(...)` stops the notebook with an error that names the check; if it is true, the name is appended to `PASSED` and the line PASS followed by the name is printed, and a second line names the Revision record and its check when the argument `record` is given (`None` is Python's word for "nothing"). Python's own `assert` statement is not used, because Python started with the option `-O` skips it. `report` prints a key number as a line that starts with RESULT. `all_checks_passed` prints the last line of the notebook with the number of checks that passed; `len` is the length of a list.

```python
def rust_program(manifest, binary):
    """Build the Rust program binary of the crate whose Cargo.toml is manifest (a
    repository path) with "cargo build --release" (about a second when it is up to date;
    minutes the first time) and return the path of the program."""
    if shutil.which("cargo") is None:
        raise FileNotFoundError(
            "cargo was not found: install Rust from https://rustup.rs, open a new "
            "terminal, activate the environment and start JupyterLab again")
    crate = (REPO / manifest).parent  # the folder that holds Cargo.toml
    completed = subprocess.run(
        ["cargo", "build", "--release", "--manifest-path", str(REPO / manifest),
         "--target-dir", str(crate / "target")],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if completed.returncode != 0:  # show the end of cargo's error message
        print(completed.stderr[-3000:])
        raise RuntimeError(f"cargo build failed for {manifest}")
    for file_name in (binary, binary + ".exe"):  # Linux and macOS; Windows
        path = crate / "target" / "release" / file_name
        if path.is_file():
            say(f"Rust program {binary} is built and ready.")
            return path
    raise FileNotFoundError(f"cargo built {manifest} but {binary} is missing")
```

`rust_program` builds a Rust program and returns where it is. `shutil.which("cargo")` looks for the program cargo; if it is not found (`is None`), the function stops with a message that says how to install Rust. `crate` is the folder that holds the file `Cargo.toml` (`.parent` removes the last part of a path). `subprocess.run([...])` runs cargo with the arguments in the list, exactly as if the release build command for this manifest were typed into a terminal; `capture_output=True` keeps cargo's messages instead of printing them, and `text=True` with `encoding="utf-8"` reads them as text. The **return code** of a program is 0 when it succeeded; otherwise the function prints the last 3000 characters of cargo's error messages (`[-3000:]` takes the end of a string) and stops. The `for` loop tries the program's name without and with the ending `.exe` (Linux and macOS have no ending, Windows has `.exe`) and returns the first one that exists, after printing that the program is ready.

```python
say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

The last statement prints the one output line of In [1].

**In [2], the records and the problem definition of both solvers.**

```python
import csv  # reads tables stored as CSV files (comma-separated values)
import re  # finds patterns in text (used to read numbers out of report sentences)
import sys  # the list of folders in which Python looks for modules

import numpy as np  # arrays of numbers

KS = "Revision/kohn_sham"  # the folder of the Kohn-Sham record (repository path)
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
```

Three more modules: `csv` reads tables stored as CSV files (comma-separated values: one line per row, the entries separated by commas), `re` finds patterns in text (**regular expressions**, used below to read numbers out of the sentences of a report), and `sys` gives access to the list of folders in which Python looks for modules. `numpy`, called `np`, holds arrays of numbers. `KS` is the folder of the Kohn-Sham record, and `PALETTE` a list of eight colours, written as hexadecimal codes, used in a fixed order by all figures.

```python
def read_json(relative):
    """Read a JSON file of the repository (a Revision record)."""
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))

def read_csv(relative):
    """Read a CSV file of the repository: a list of rows, each row a dictionary from
    the column names to the texts in that row."""
    with open(repository_file(relative), newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))
```

Two small reading functions. `read_json` reads a repository file as text and turns it into Python objects with `json.loads` (dictionaries, lists, numbers and strings). `read_csv` opens a CSV file (`with open(...) as handle:` opens it and closes it again when the indented block ends), and `csv.DictReader` reads it row by row, each row a dictionary from the column names of the first line to the texts in that row; `list(...)` collects all rows.

```python
REPORTS = {"reference solver": read_json(f"{KS}/reports/ks-reference.json"),
           "Rust solver": read_json(f"{KS}/reports/ks-rust-solver.json"),
           "cross-check": read_json(f"{KS}/reports/ks-crosscheck.json")}
counts = {}
for label, rep in REPORTS.items():
    summary = rep["summary"]  # {"checks": ..., "pass": ..., "fail": ...}
    counts[label] = (summary["pass"], summary["checks"])
    say(f"{label}: {summary['pass']} of {summary['checks']} checks PASS")
check(counts == {"reference solver": (37, 37), "Rust solver": (42, 42),
                 "cross-check": (29, 29)},
      "the three committed reports pass every check (37, 42 and 29)")
```

`REPORTS` is a dictionary of the three committed reports: the reference solver's self-checks, the Rust solver's self-checks, and the cross-check. The loop goes through its pairs (`.items()`); each report has an entry `summary` with the numbers of checks and of PASS verdicts, which the loop stores in `counts` as a **tuple** (an unchangeable pair in round brackets) and prints. The check requires exactly 37 of 37, 42 of 42 and 29 of 29; Out [2] shows the three lines and the PASS line.

```python
RUST_PARAMS = read_json(f"{KS}/results/parameters.json")  # the Rust solver's
REF_PARAMS = read_json(f"{KS}/reference/results/parameters.json")  # the reference's
pairs = [("H", "H"), ("m", "m"), ("L_tipCutoff", "L"), ("dk", "dk"), ("v_t", "vt"),
         ("tipTheta", "tipTheta"), ("historyA", "historyA"),
         ("slicesA4", "slicesA4"), ("temperatures", "temperatures")]
differ = [rust_name for rust_name, ref_name in pairs
          if RUST_PARAMS["physics"][rust_name] != REF_PARAMS["physics"][ref_name]]
same_theory = (RUST_PARAMS["theoryInputs"]["ksTheorySha256"]
               == REF_PARAMS["theoryInputs"]["ksTheorySha256"])
for rust_name, ref_name in pairs:
    say(f"  {rust_name:13s} Rust {RUST_PARAMS['physics'][rust_name]}   reference "
        f"{REF_PARAMS['physics'][ref_name]}")
check(not differ and same_theory,
      "both solvers solve the same problem and read the same ks-theory.json",
      record=f"{KS}/reports/ks-crosscheck.json, check problem_definition_identical")
```

`RUST_PARAMS` and `REF_PARAMS` are the `parameters.json` files of the two solvers. The two programs name some constants differently (the tip cutoff is `L_tipCutoff` in one and `L` in the other), so `pairs` lists the names side by side. `differ` is built by a **list comprehension**, `[expression for ... in ... if condition]`, which collects the Rust name of every pair whose two values are not equal (`!=`); it must be empty. `same_theory` compares the SHA-256 fingerprints (a 64-character number computed from every byte of a file; two different files practically never have the same one) of the theory file that each solver read. The loop prints the nine pairs of values, the name padded to 13 characters (`:13s`). The check requires no difference and the same theory file, and names the cross-check's check problem_definition_identical, which it reproduces.

```python
LAMBDAS = {}  # N -> {"lamp1": +lambda_1, ...}: the couplings of the reference
rust_cal = {c["N"]: c for c in RUST_PARAMS["couplingCalibration"]["values"]}
same_couplings = True
for cal in REF_PARAMS["derived"]["calibration"]:
    N = cal["N"]
    LAMBDAS[N] = {"lam0": 0.0, "lamp1": cal["lambda1"], "lamm1": -cal["lambda1"],
                  "lamp2": cal["lambda2"], "lamm2": -cal["lambda2"]}
    same_couplings &= (cal["lambda1"] == rust_cal[N]["lambda1"]
                       and cal["lambda2"] == rust_cal[N]["lambda2"])
    say(f"N = {N:5.0f}: lambda_1 = {cal['lambda1']}, lambda_2 = {cal['lambda2']}")
check(same_couplings, "the six couplings derived by the two solvers are identical",
      record=f"{KS}/reports/ks-crosscheck.json, check parameters_couplings")
```

Each solver derived the couplings $\lambda_1$ and $\lambda_2$ for each particle number on its own, from the same rule (Section 16.3). `rust_cal` is a **dictionary comprehension** that files the Rust values under their $N$. The loop goes through the reference's values, stores for each $N$ the five couplings of the tags lam0, lamp1, lamm1, lamp2, lamm2 in `LAMBDAS` (they are used by the next cells), and compares with the Rust values; `same_couplings &= ...` keeps `same_couplings` true only while every comparison is true (`&=` combines with "and"). `{N:5.0f}` prints $N$ in five places without decimals. Out [2] shows $\lambda_1 = 0.01946$, $\lambda_2 = 0.05838$ for $N = 8$, $0.0009298$ and $0.002789$ for $N = 136$, and $0.0001846$ and $0.0005538$ for $N = 688$, identical in both solvers.

**In [3], the reference program and the five states.**

```python
sys.dont_write_bytecode = True  # do not write a __pycache__ folder into the record
sys.path.insert(0, str(repository_file(f"{KS}/reference")))  # Python looks here too
import run_reference as RR  # noqa: E402  the reference program (Revision code)

CO = RR.theory_coefficients()  # coefficients read and checked from ks-theory.json
say(f"functional coefficients: M_eff = m + {CO['cM']} lambda S, "
    f"v_v = {CO['cV']} lambda n, e_int = lambda ({CO['eS2']} S^2 + {CO['eN2']} n^2)")
```

`sys.dont_write_bytecode = True` stops Python from writing a folder of translated files (`__pycache__`) next to the imported program, which would otherwise appear inside the Revision record. `sys.path.insert(0, ...)` puts the folder of the reference program at the front of the list of folders in which Python looks for modules, so that `import run_reference as RR` finds `Revision/kohn_sham/reference/run_reference.py` and makes it available under the short name `RR`. Importing does not run the program: its last lines start the computation only when it is run as a program, so the import only defines its functions. (The comment `noqa: E402` tells a style checker that an import in the middle of a cell is intended.) `RR.theory_coefficients()` reads the coefficients of the functional from `ks-theory.json` as exact fractions; the printed line, Out [3], shows $M_{eff} = m + \tfrac{15}{16}\lambda S$, $v_v = -\tfrac{1}{16}\lambda n$ and $e_{int} = \lambda(\tfrac{15}{32}S^2 - \tfrac{1}{32}n^2)$, the formulas of Chapter 14.

```python
def job_spec(N, tag, a4, T=None):
    """The reference program's description of one state (a dictionary)."""
    spec = {"id": RR.run_id(N, tag, a4, T), "N": N, "tag": tag,
            "lam": LAMBDAS[N][tag], "a4": a4, "sigma": RR.SIGMA[tag]}
    if T is not None:
        spec["T"] = T
    return spec
```

`job_spec` writes one state as the reference program describes it: a dictionary with the id (made by the program's own function `RR.run_id`, so that the names agree with the record's file names), $N$, the coupling tag and its value from `LAMBDAS`, the slice, the first-order mean-field size $\sigma$ of the tag (`RR.SIGMA`: 0 for lam0, 0.1 for $\pm\lambda_1$, 0.3 for $\pm\lambda_2$; it decides how many levels the label set keeps), and, for a thermal state, the temperature. `T=None` makes the temperature optional.

```python
SPECS = {}
for args in [(8.0, "lamm2", 0.0), (688.0, "lam0", 0.0), (136.0, "lamp2", 2.0),
             (8.0, "lamm1", 0.0, 0.01), (8.0, "lam0", 1.5, 0.05)]:
    spec = job_spec(*args)
    SPECS[spec["id"]] = spec
GROUND_IDS = ["N8_lamm2_a00", "N688_lam0_a00", "N136_lamp2_a20"]
THERMAL_IDS = ["N8_lamm1_a00_T10", "N8_lam0_a15_T50"]
print("state               N   lambda       a4,0  sigma  T")
for sid, spec in SPECS.items():
    print(f"{sid:18s} {spec['N']:4.0f}  {spec['lam']:+.5f}  {spec['a4']:4.1f}  "
          f"{spec['sigma']:4.1f}   {spec.get('T', 0.0):.2f}")
check(sorted(SPECS) == sorted(GROUND_IDS + THERMAL_IDS),
      "the five job descriptions have the ids of the subset")
```

The loop makes the five job descriptions; `job_spec(*args)` unpacks each tuple into the arguments of the function, and the descriptions are filed under their ids in `SPECS`. `GROUND_IDS` and `THERMAL_IDS` list the five ids in the order used below. The table printed by the loop (Out [3]) shows each state's $N$, coupling (with sign and five decimals, `:+.5f`), slice, $\sigma$ and temperature (`spec.get("T", 0.0)` gives 0 when a state has no temperature). The check compares the sorted ids with the five ids of the subset.

**In [4], the reference solver on the three ground states.**

```python
PER_GRID = {}  # (state id, G) -> the levels of the state on grid G (an array)
original_ground_on_grid = RR._ground_on_grid  # the reference's function for one grid

def ground_on_grid_recorded(co, spec, G, labels):
    """Call the reference's own function for one grid and keep a copy of its levels."""
    result = original_ground_on_grid(co, spec, G, labels)
    PER_GRID[(spec["id"], G)] = result["eps"].copy()
    return result
```

The reference's ground-state job calls the program's internal function `_ground_on_grid` once per grid and keeps only the extrapolated levels. To draw the convergence of every level (In [10]) we want the levels on each grid as well. `original_ground_on_grid` keeps the program's function under a second name. The new function `ground_on_grid_recorded` takes the same four arguments, calls the original function, stores a copy of the levels it returned (`result["eps"]`, a numpy array; `.copy()` makes an independent copy) in `PER_GRID` under the pair (state id, grid), and passes the result on unchanged. Such a function, which calls another and adds something around it, is called a **wrapper**.

```python
RR._ground_on_grid = ground_on_grid_recorded  # the job now calls our wrapper
NEW = {}  # state id -> the new reference result (the content of its JSON file)
for sid in GROUND_IDS:
    NEW[sid] = RR.jsonable(RR.ground_job(CO, SPECS[sid])["data"])
    E = NEW[sid]["scalars"]["E_KS"]
    say(f"{sid}: {NEW[sid]['levels_in_set']} levels, E_KS = {E['value']:.13f} "
        f"(U = {E['U']:.1e})")
RR._ground_on_grid = original_ground_on_grid  # put the original function back
check(len(PER_GRID) == 9, "the levels of three states on three grids were kept")
```

`RR._ground_on_grid = ground_on_grid_recorded` puts the wrapper in the place of the program's function: the job looks the function up by its name in its module each time, so from now on it calls the wrapper. The loop runs the job `RR.ground_job` for each ground state; its result is a dictionary whose entry `data` is the content of the JSON file that the program writes, and `RR.jsonable` turns its numpy arrays into plain Python numbers exactly as the program does before writing. Each line of Out [4] prints the number of levels kept and the Richardson value of $E_{KS}$ with its uncertainty: N8_lamm2_a00 has 22 levels and $E_{KS} = 0.0028626521737$ ($U = 2.1\times10^{-12}$), N688_lam0_a00 has 137 levels and $E_{KS} = 680.4412465815219$ ($U = 3.3\times10^{-9}$), N136_lamp2_a20 has 354 levels and $E_{KS} = 12.4489994812532$ ($U = 4.6\times10^{-11}$). Then the original function is put back, and the check confirms that nine level arrays (three states, three grids) were kept. This cell runs for about two minutes on a fast computer: N136_lamp2_a20 alone solves 354 levels on three grids, each with its excited state and four neighbouring slices.

**In [5], comparing the new results with the committed files.**

```python
def compare_records(new, old, problems, where="top"):
    """Compare two JSON structures; return the number of numbers compared and append
    a description of every difference to the list problems."""
    if isinstance(new, bool) or isinstance(old, bool) or new is None or \
            isinstance(new, str):
        if new != old:
            problems.append(f"{where}: {new!r} != {old!r}")
        return 0
    if isinstance(new, (int, float)):
        if not isinstance(old, (int, float)) or \
                abs(new - old) > 1e-9 * max(1.0, abs(old)):
            problems.append(f"{where}: {new!r} != {old!r}")
        return 1
```

`compare_records` walks through two JSON structures at the same time and counts the numbers it compared. This first part handles the simplest cases. `isinstance(x, bool)` asks whether `x` is a truth value; a truth value, a missing value (`None`) or a text must be equal, and every inequality is appended to the list `problems` as a line naming the place (`{new!r}` writes the value as Python would type it). A number (`int` or `float`) must be within one part in a billion of the committed one, measured relative to $\max(1, |old|)$; it counts as one compared number. (A backslash at the end of a line continues the statement on the next line.)

```python
    if isinstance(new, dict):
        if sorted(new) != sorted(old):
            problems.append(f"{where}: different names")
            return 0
        return sum(compare_records(new[k], old[k], problems, f"{where}/{k}")
                   for k in new)
    if len(new) != len(old):  # a list
        problems.append(f"{where}: lengths {len(new)} and {len(old)}")
        return 0
    return sum(compare_records(a, b, problems, f"{where}[{i}]")
               for i, (a, b) in enumerate(zip(new, old)))
```

For a dictionary both must have the same names (sorted, because the order does not matter); then the function calls itself for each entry, with the place extended by `/name`, and adds up the counts with `sum(...)`. A function that calls itself is **recursive**: it goes down into the nested structure until it reaches single values. Anything else is a list: both must have the same length, and the function compares them entry by entry (`zip` pairs the entries, `enumerate` numbers them, and the place is extended by `[i]`).

```python
def check_reproduction(label, data, relative):
    """Check the new result data (named label) against its committed file."""
    committed = repository_file(relative).read_text(encoding="utf-8")
    problems = []
    numbers = compare_records(data, json.loads(committed), problems)
    text = json.dumps(data, indent=1, ensure_ascii=True) + "\n"  # as written
    say(f"{label}: {numbers} numbers compared; identical byte for byte: "
        f"{text == committed}")
    for line in problems[:5]:  # the first differences, if there are any
        say(f"  difference {line}")
    check(not problems,
          f"the re-run of {label} reproduces {relative.split('/results/')[1]}",
          record=f"{KS}/reports/ks-crosscheck.json, check "
                 "reference_repeat_byte_identical")
```

`check_reproduction` reads the committed file as text, compares its content with the new result, and also writes the new result as text exactly as the reference program writes its files (`json.dumps` with an indentation of one blank and only ASCII characters, plus a final line end) to report whether the two texts are identical byte for byte. It prints the number of numbers compared and that answer, then the first five differences, if any (`problems[:5]` is the first five entries of a list). The check requires no difference; its name gives the file name after `/results/` (`.split('/results/')[1]` cuts the path at that text and takes the second piece), and its record line names the cross-check's check reference_repeat_byte_identical, which made the same test for all files.

```python
for sid in GROUND_IDS:
    check_reproduction(sid, NEW[sid], f"{KS}/reference/results/ground/{sid}.json")
```

The loop applies this to the three ground states. Out [5] shows 3597, 4513 and 5815 numbers compared, every file identical byte for byte, and three PASS lines.

**In [6], Richardson extrapolation at work.**

```python
def richardson(x1, x2, x3):
    """Three-grid Richardson value R and its uncertainty U (x1 on the coarsest grid),
    in the two-step form of the reference program; also the two one-step values."""
    r_fine = (4.0 * x3 - x2) / 3.0  # one step on the grids h/2 and h/4
    r_coarse = (4.0 * x2 - x1) / 3.0  # one step on the grids h and h/2
    R = (16.0 * r_fine - r_coarse) / 15.0  # the second step
    U = abs(R - r_fine) + 2e-12 * max(1.0, abs(R))
    return R, U, r_coarse, r_fine
```

`richardson` is the two-step extrapolation of Section 16.5 written in Python: `r_fine` is the one-step value $r(h/2)$ of the two finer grids, `r_coarse` the one-step value $r(h)$, `R` the second step $(16\,r(h/2) - r(h))/15$, and `U` the uncertainty $|R - r(h/2)| + 2\cdot10^{-12}\max(1, |R|)$. The function returns all four numbers.

```python
CONVERGENCE = {}  # state id -> (E_KS on the three grids, R)
for sid in GROUND_IDS:
    xs = [grid["scalars"]["E_KS"] for grid in NEW[sid]["per_grid"]]
    R, U, _, _ = richardson(*xs)
    R_one_line = (64.0 * xs[2] - 20.0 * xs[1] + xs[0]) / 45.0
    stored = NEW[sid]["scalars"]["E_KS"]
    ratio = (xs[0] - xs[1]) / (xs[1] - xs[2])
    CONVERGENCE[sid] = (xs, R)
    say(f"{sid}: E_KS(300) = {xs[0]:.12f}, E_KS(600) = {xs[1]:.12f}, "
        f"E_KS(1200) = {xs[2]:.12f}")
    say(f"    R = {R:.13f}, U = {U:.1e}, ratio of the differences = {ratio:.5f}")
    check(abs(R - stored["value"]) <= 1e-14 * max(1.0, abs(R))
          and abs(U - stored["U"]) <= 1e-14 * max(1.0, abs(R))
          and abs(R_one_line - R) <= 1e-13 * max(1.0, abs(R)),
          f"our Richardson lines give the reference value and U of E_KS ({sid})")
```

For each ground state the list comprehension takes $E_{KS}$ from the three per-grid records of the new result (`per_grid` holds one record per grid, coarsest first). `R, U, _, _ = richardson(*xs)` keeps the first two returned numbers (the underscore is a name for values that are not needed). `R_one_line` is the one-line form $(64x(h/4) - 20x(h/2) + x(h))/45$ of Section 16.5, `stored` the value and uncertainty that the reference program wrote, and `ratio` the convergence ratio of Section 16.4. The three values are kept in `CONVERGENCE` for the figure of In [8]. The two printed lines per state (Out [6]) show the three grid values, $R$, $U$ and the ratio: $4.00020$, $4.00007$ and $4.00006$. The check requires our $R$ and $U$ to equal the program's within $10^{-14}$ (relative) and the two written forms of $R$ to agree within $10^{-13}$: Section 16.5's algebra and the program agree.

**In [7], a fourth grid tests the uncertainty.**

```python
FOUR_GRIDS = {}  # G -> (E_KS, levels, p8 at the tip) of N136_lamp2_a20 on grid G
original_observables = RR.K.observables  # the function of ks_fd (RR.K is ks_fd)

def observables_recorded(state):
    """Call ks_fd's own function and keep E_KS, the levels and p8 at the tip."""
    scalars, profiles = original_observables(state)
    FOUR_GRIDS[state.grid.G] = (scalars["E_KS"], state.eps.copy(),
                                scalars["p8_tip"])
    return scalars, profiles
```

A second wrapper, for the function `observables` of the module `ks_fd` (the reference program imported this module under the name `K`, so it is `RR.K` here). The validation job calls it once on each of the four grids; the wrapper keeps the grid's $E_{KS}$, a copy of its levels and the value of $p_8$ at the tip in `FOUR_GRIDS`, under the number of cells `state.grid.G`.

```python
RR.K.observables = observables_recorded  # the job now calls our wrapper
VALIDATION = RR.jsonable(RR.validation_job(CO, SPECS["N136_lamp2_a20"])["data"])
RR.K.observables = original_observables  # put the original function back
check_reproduction("the fourth-grid validation", VALIDATION,
                   f"{KS}/reference/results/validation/N136_lamp2_a20.json")
same = all(abs(FOUR_GRIDS[G][0] - grid["scalars"]["E_KS"]) <= 1e-12
           for G, grid in zip((300, 600, 1200), NEW["N136_lamp2_a20"]["per_grid"]))
check(sorted(FOUR_GRIDS) == [300, 600, 1200, 2400] and same,
      "the validation run repeats the ground job's E_KS on the three common grids")
```

The wrapper is put in place, the program's job `RR.validation_job` solves N136_lamp2_a20 on $G = 300$, $600$, $1200$ and $2400$ (about 40 seconds), and the original function is put back. `check_reproduction` compares the result with the committed file `validation/N136_lamp2_a20.json` (Out [7]: 99 numbers, identical byte for byte). The second check confirms that the validation run repeats the ground job's $E_{KS}$ on the three common grids to $10^{-12}$ (`all(...)` is true when every comparison in the brackets is true) and that the four grids were recorded.

```python
classes = VALIDATION["classes"]
for name, c in classes.items():
    say(f"  {name:20s} {c['elements']:4d} element(s): max |R123 - R234| / U123 = "
        f"{c['max_ratio_to_U123']:.2e}")
worst = max(classes, key=lambda name: classes[name]["max_ratio_to_U123"])
detail = next(c["detail"] for c in REPORTS["reference solver"]["checks"]
              if c["name"] == "richardson_uncertainty_validated")
stated = float(re.search(r"U123 = ([0-9.]+) \((\w+)\)", detail).group(1))
say(f"largest ratio {classes[worst]['max_ratio_to_U123']:.3f} ({worst}); "
    f"the report states {stated}")
check(all(c["all_within_U123"] for c in classes.values())
      and len(classes) == 19 and worst == "p8_tip"
      and abs(classes[worst]["max_ratio_to_U123"] - stated) <= 5e-4,
      "on the fourth grid every three-grid value moves by less than its U",
      record=f"{KS}/reports/ks-reference.json, check richardson_uncertainty_validated")
```

`classes` holds the 19 quantity classes of the validation, each with its number of elements and the largest ratio $|R_{123} - R_{234}|/U_{123}$; the loop prints them (Out [7]: from $0$ for the integral of $p_3$ to $0.787$ for $p_8$ at the tip). `max(classes, key=...)` finds the class with the largest ratio: the `key` is a **lambda**, a one-line function written in place, that gives each class name its ratio. `next(... for c in ... if ...)` takes the first check of the reference report whose name is richardson_uncertainty_validated, and `re.search` reads the number after the text `U123 = ` in its detail sentence: in the pattern, `[0-9.]+` means one or more digits or points, round brackets capture what they match (`.group(1)` returns it), `\(` and `\)` are literal brackets, and `\w+` is a word. The check requires every element of every class to lie within its $U_{123}$, 19 classes, the largest ratio at `p8_tip`, and our largest ratio equal to the one stated in the report within $5\times10^{-4}$.

**In [8], convergence as a picture (Figure 16a.1).**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.3))
h = np.array([3.0 / 300, 3.0 / 600, 3.0 / 1200])  # the cell widths
for colour, sid in zip(PALETTE, GROUND_IDS):
    xs, R = CONVERGENCE[sid]
    left.loglog(h, [abs(x - R) for x in xs], "o-", color=colour, lw=1.5, ms=6,
                label=sid)
    first = abs(xs[0] - R)  # a guide of slope 2, a factor 3 below the first point
    left.loglog(h, first / 3.0 * (h / h[0]) ** 2, "--", color=colour, lw=0.9)
left.set_xlabel("cell width $h = L/G$")
left.set_ylabel("$|E_{KS}(G) - R|$ (units of $m$)")
left.set_title("three grids, three states")
left.legend(fontsize=8)
```

`plt.subplots(1, 2, ...)` makes a figure with two sets of axes side by side, `left` and `right`, 10 by 4.3 inches. `h` is the numpy array of the three cell widths $3/300$, $3/600$, $3/1200$. For each ground state (`zip` pairs the colours with the ids) the left axes draw the distances $|E_{KS}(G) - R|$ against $h$ with **logarithmic axes** (`loglog`: equal distances on the axis are equal factors), as circles joined by lines (`"o-"`, line width 1.5, marker size 6), and a dashed **guide line** proportional to $h^2$ that starts a factor 3 below the first point. On logarithmic axes a power law $C h^q$ is a straight line of slope $q$, so points parallel to the guide show an error proportional to $h^2$. The labels, title and legend complete the panel.

```python
grids = [300, 600, 1200, 2400]
e4 = [FOUR_GRIDS[G][0] for G in grids]  # E_KS of N136_lamp2_a20 on the four grids
h4 = np.array([3.0 / G for G in grids])
R123, U123, _, _ = richardson(*e4[:3])
R234, _, _, _ = richardson(*e4[1:])
single = [abs(x - R234) for x in e4]
one_step = [abs((4.0 * e4[i + 1] - e4[i]) / 3.0 - R234) for i in range(3)]
```

For the right panel: `e4` is $E_{KS}$ of N136_lamp2_a20 on the four grids (kept by the wrapper of In [7]), `h4` their cell widths, `R123` and `U123` the three-grid value and uncertainty of the three coarser grids (`e4[:3]` is the first three entries), and `R234` the three-grid value of the three finer ones (`e4[1:]` is everything after the first). `single` holds the distance of each single-grid value from $R_{234}$, and `one_step` the distance of each one-step value $(4x(2G) - x(G))/3$ from it.

```python
right.loglog(h4, single, "o-", color=PALETTE[0], lw=1.5, ms=6,
             label="single grid $x(G)$")
right.loglog(h4, single[0] / 3.0 * (h4 / h4[0]) ** 2, "--", color=PALETTE[0],
             lw=0.9, label="slope 2 (shifted down)")
right.loglog(h4[:3], one_step, "s-", color=PALETTE[1], lw=1.5, ms=6,
             label="one step $r$ (pair $G$, $2G$)")
right.loglog(h4[:3], one_step[0] / 3.0 * (h4[:3] / h4[0]) ** 4, "--",
             color=PALETTE[1], lw=0.9, label="slope 4 (shifted down)")
right.loglog([h4[0]], [max(abs(R123 - R234), 1e-16)], "D", color=PALETTE[2], ms=8,
             label="three grids $R_{123}$")
right.loglog([h4[0]], [U123], "_", color="k", ms=16, mew=2,
             label="its uncertainty $U_{123}$")
right.set_xlabel("cell width $h$ of the coarsest grid used")
right.set_ylabel("distance from $R_{234}$ (units of $m$)")
right.set_title("N136_lamp2_a20 on four grids")
right.legend(fontsize=7, loc="center right")
```

The right panel draws the single-grid distances with a dashed slope-2 guide, the one-step distances (squares) with a dashed slope-4 guide ($h^4$ is the error of a one-step value, Section 16.5), the distance $|R_{123} - R_{234}|$ as a diamond (`max(..., 1e-16)` keeps a zero away from the logarithmic axis) and the uncertainty $U_{123}$ as a short horizontal bar (marker `"_"`, black, edge width 2).

```python
for ax, ticks in ((left, h), (right, h4)):  # tick labels at the grids' h only
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"{t:g}" for t in ticks])
fig.tight_layout()
```

For both panels the tick labels are set at the grids' cell widths only: `NullFormatter` removes the labels of the small in-between ticks, `set_xticks` puts ticks at the given values, and `set_xticklabels` writes them in the shortest form (`:g`). `fig.tight_layout()` arranges the panels so that their labels do not overlap.

```python
save_figure(fig, "grid_convergence",
            "Convergence of the reference solver for the Kohn-Sham energy $E_{KS}$, "
            "logarithmic axes, energies in units of the mass $m$. Left: distance of "
            "the single-grid value from the Richardson value $R$ against the cell "
            "width $h = 3/G$ for $G = 300, 600, 1200$ for the three ground states; "
            "the points run parallel to the dashed lines of slope 2 (drawn a factor 3 "
            "lower), an error proportional to $h^2$. Right: the state N136_lamp2_a20 "
            "also on $G = 2400$, every "
            "distance measured from the four-grid best value $R_{234}$: single grids "
            "fall with slope 2, one Richardson step with slope 4, and the three-grid "
            "value $R_{123}$ (diamond) lies far below its stated uncertainty "
            "$U_{123}$ (bar), so $U$ is a safe over-estimate.")
check(all(abs(CONVERGENCE[s][0][0] - CONVERGENCE[s][1])
          > abs(CONVERGENCE[s][0][2] - CONVERGENCE[s][1]) for s in GROUND_IDS)
      and single[0] > single[1] > single[2] > single[3]
      and one_step[0] > one_step[1] > one_step[2] and abs(R123 - R234) <= U123,
      "the errors shrink grid by grid and R123 lies within U123 of R234")
```

`save_figure` saves Figure 16a.1 with its caption (Python joins strings written next to each other into one). What the student should see: on the left, three straight lines parallel to their slope-2 guides, the errors of the three states falling by a factor 4 from grid to grid although their sizes differ by five powers of ten; on the right, the slope-2 line of the single grids, the slope-4 line of one Richardson step, and the diamond of $R_{123}$, only $3.6\times10^{-14}$ from $R_{234}$ (`Revision/kohn_sham/reference/results/validation/N136_lamp2_a20.json`, class E_KS), far below the bar of its uncertainty $U_{123} = 4.6\times10^{-11}$: the uncertainty is a safe over-estimate. The check confirms what the picture shows: for each state the error shrinks from the coarsest to the finest grid, the single-grid and one-step distances shrink monotonically, and $R_{123}$ lies within $U_{123}$ of $R_{234}$.

**In [9], the fourth-grid test as a bar chart (Figure 16a.2).**

```python
names = list(classes)  # the 19 classes in the order of the record
values = [max(classes[n]["max_ratio_to_U123"], 1e-8) for n in names]
fig, ax = plt.subplots(figsize=(7.5, 6.2))
colours = [PALETTE[1] if n == worst else PALETTE[0] for n in names]
ax.barh(range(len(names)), values, color=colours, height=0.65)
ax.set_xscale("log")
ax.axvline(1.0, color="k", lw=1.2)
ax.set_yticks(range(len(names)))
ax.set_yticklabels([f"{n} ({classes[n]['elements']})" for n in names], fontsize=8)
ax.invert_yaxis()  # the first class at the top
ax.set_xlim(1e-9, 3.0)
```

`names` is the list of the 19 class names in the order of the record, and `values` their largest ratios, with exact zeros raised to $10^{-8}$ so that they can be drawn on a logarithmic axis. `colours` marks the worst class in orange (the second palette colour) and the others in blue. `barh` draws horizontal bars, one per class, at the heights 0 to 18; `set_xscale("log")` makes the horizontal axis logarithmic; `axvline(1.0, ...)` draws the vertical black line at ratio 1; the class names with their numbers of elements become the labels of the vertical axis; `invert_yaxis()` puts the first class at the top; and the horizontal axis runs from $10^{-9}$ to 3.

```python
for i, n in enumerate(names):
    if classes[n]["max_ratio_to_U123"] == 0.0:  # mark a class that agrees exactly
        ax.text(1.5e-8, i, "exactly 0", va="center", fontsize=8)
ax.set_xlabel("largest $|R_{123} - R_{234}|$ / $U_{123}$ of the class")
ax.set_title("Fourth-grid test of the uncertainty (N136_lamp2_a20)")
save_figure(fig, "uncertainty_validated",
            "Validation of the reference uncertainty on a fourth grid for the state "
            "N136_lamp2_a20: for each of the 19 classes of quantities (the number of "
            "elements in brackets) the largest change of the three-grid value between "
            "the grids $(300, 600, 1200)$ and $(600, 1200, 2400)$, divided by the "
            "stated uncertainty $U_{123}$, on a logarithmic axis; a class that agrees "
            f"exactly is drawn at $10^{{-8}}$ and marked. All bars end left of the "
            "line 1; the largest, "
            f"{classes[worst]['max_ratio_to_U123']:.3f}, is the value of $p_8$ at the "
            "tip, where the densities are largest.")
```

The loop writes "exactly 0" next to every class whose ratio is exactly zero (here only the integral of $p_3$). After the axis label and the title, `save_figure` saves Figure 16a.2. The caption is an f-string that inserts the largest ratio, `{{-8}}` writing a literal pair of braces. What the student should see: every bar ends left of the line 1; the energies, the integrals and the levels end far to the left (ratios between about $10^{-4}$ and $3\times10^{-3}$); only the values at the tip and the profiles, which include the tip, come within a factor of about 2 of the line, the largest ($p_8$ at the tip, $0.787$) within a factor of 1.3. The tip, where the densities are largest, is where the grids work hardest.

**In [10], every level converges like $h^2$ (Figure 16a.3).**

```python
level_points = []  # (state, level energy, ratio) of every level with a ratio
for sid in GROUND_IDS:
    eps = [PER_GRID[(sid, G)] for G in (300, 600, 1200)]
    ratios = RR.asym_ratio(*eps)  # the reference's own function
    stored = NEW[sid]["consistency"]["ratio_eps"]
    mine = (len(ratios), float(np.median(ratios)), min(ratios), max(ratios))
    say(f"{sid}: {mine[0]} levels, median ratio {mine[1]:.6f}, smallest "
        f"{mine[2]:.6f}, largest {mine[3]:.6f}")
    check(mine == (stored["count"], stored["median"], stored["min"], stored["max"])
          and abs(mine[1] - 4.0) <= 0.05,
          f"the levels of {sid} converge like h^2 (median ratio within 0.05 of 4)",
          record=f"{KS}/reports/ks-reference.json, check richardson_asymptotic_ratio")
```

For each ground state `eps` is the list of the level arrays on the three grids kept by the wrapper of In [4], and `RR.asym_ratio` (the reference's own function) computes the convergence ratio of Section 16.4 for every level whose two differences exceed $10^{-10}$ (smaller differences are dominated by rounding). `mine` collects the number of ratios, their **median** (the middle value when they are sorted; `np.median`), the smallest and the largest, and prints them. The check requires these four numbers to equal the ones the program stored in the entry `consistency` of the result, and the median to lie within $0.05$ of 4, the criterion of the reference's check richardson_asymptotic_ratio. Out [10] shows medians of $4.000053$, $4.000064$ and $4.000055$.

```python
    floor = 1e-10  # the same selection as asym_ratio: both differences above 1e-10
    d1, d2 = eps[0] - eps[1], eps[1] - eps[2]
    keep = (np.abs(d1) > floor) & (np.abs(d2) > floor)
    energies = np.asarray(NEW[sid]["levels"]["eps"])[keep]
    level_points += [(sid, e, r) for e, r in zip(energies, d1[keep] / d2[keep])]
```

The same selection by hand, to draw it: `d1` and `d2` are the two differences of every level (numpy subtracts arrays entry by entry), `keep` is a **mask**, an array of truth values that is true where both differences exceed the floor (`&` combines two masks with "and"), and `energies` are the Richardson values of the kept levels (`array[keep]` keeps the entries where the mask is true). `level_points` collects one tuple (state, level energy, ratio) per level.

```python
fig, ax = plt.subplots(figsize=(7.5, 4.3))
for colour, sid in zip(PALETTE, GROUND_IDS):
    pts = [(e, abs(r - 4.0)) for s, e, r in level_points if s == sid]
    ax.semilogy([p[0] for p in pts], [p[1] for p in pts], "o", color=colour, ms=4,
                alpha=0.8, label=f"{sid} ({len(pts)} levels)")
ax.axhline(0.05, color="k", lw=1.0, ls="--", label="limit 0.05 of the median test")
ax.set_xlabel("level energy $\\varepsilon$ (Richardson value, units of $m$)")
ax.set_ylabel("$|$ratio $- 4|$")
ax.set_title("Every level converges like $h^2$")
ax.legend(fontsize=8)
```

The figure draws, for each state, the distance of every ratio from 4 against the level energy, on a logarithmic vertical axis (`semilogy`), with the limit $0.05$ of the median test as a dashed line. Two backslashes in a Python string give one backslash in the text, so `"\\varepsilon"` reaches matplotlib as the LaTeX command for $\varepsilon$.

```python
worst_level = max(abs(r - 4.0) for _, _, r in level_points)
save_figure(fig, "eigenvalue_ratios",
            "Distance from 4 of the convergence ratio $(x(300) - x(600))/(x(600) - "
            "x(1200))$ of every level of the three ground states, against the "
            "level energy in units of $m$ (vertical axis logarithmic). A ratio of 4 "
            "means an error proportional to $h^2$. Low levels have ratios within a "
            "few millionths of 4; higher levels, whose orbitals oscillate faster, "
            "deviate more because the $h^4$ term is larger, but even the worst "
            f"level, at {worst_level:.4f}, stays below the limit 0.05 that the "
            "reference applies to the median.")
check(worst_level < 0.05, "every single level has a ratio within 0.05 of 4")
```

`worst_level` is the largest distance from 4 of any single level ($0.0336$). `save_figure` saves Figure 16a.3, and the check requires every single level, not only the median, to lie within $0.05$ of 4. What the student should see: most levels have ratios between about $10^{-6}$ and $10^{-3}$ from 4; higher levels of N136_lamp2_a20, whose orbitals oscillate faster from cell to cell, deviate more, because for them the $h^4$ term of the error is larger compared with the $h^2$ term (the correction $\tfrac{15}{16}\tfrac{d}{c}h^2$ of Section 16.4); but even the worst level stays below the dashed line.

**In [11], the two thermal states.**

```python
for sid in THERMAL_IDS:
    NEW[sid] = RR.jsonable(RR.thermo_job(CO, SPECS[sid])["data"])
    th = NEW[sid]["thermo"]
    say(f"{sid}: {NEW[sid]['levels_in_set']} levels; mu = {th['mu']['value']:.13f} "
        f"(U {th['mu']['U']:.1e}), E = {th['E']['value']:.12f} (U {th['E']['U']:.1e}),"
        f" C_V = {th['C_V']['value']:.9f} (U {th['C_V']['U']:.1e})")
    check_reproduction(sid, NEW[sid], f"{KS}/reference/results/thermo/{sid}.json")
```

For each thermal state the reference's thermal job is run (it solves the state on the three grids at $T$ and at four neighbouring temperatures), its result is turned into plain numbers and kept in `NEW`, and the chemical potential $\mu$, the energy $E$ and the heat capacity $C_V$ are printed with their uncertainties (`:.13f`, `:.12f` and `:.9f` give 13, 12 and 9 decimals, `:.1e` one decimal in powers of ten). Then `check_reproduction` compares with the committed thermal file. Out [11]: for N8_lamm1_a00_T10, $\mu = 0.2100104497343$ ($U = 2.3\times10^{-12}$), and for N8_lam0_a15_T50, $\mu = -0.0304029805513$ and $C_V = 32.379779710$; both files are reproduced byte for byte. N8_lamm1_a00_T10 is the state in which the first cross-check failed (Section 16.20).

**In [12], the Rust solver: canonical and refined runs.**

```python
SOLVER = rust_program(f"{KS}/solver/Cargo.toml", "revision_ks_solver")
RUN_FOLDER = REPO / f"{KS}/solver/target/textbook_16a"  # git ignores target folders
RUN_FOLDER.mkdir(parents=True, exist_ok=True)
```

`rust_program` (In [1]) builds the Rust solver with cargo, which takes a second when the program is up to date, and returns the path of the program, `SOLVER`. `RUN_FOLDER` is a folder inside the solver's `target` folder, which git ignores, so the raw outputs of the runs never enter the record; `mkdir` creates it.

```python
def run_single(sid, refined):
    """Run `revision_ks_solver single` for state sid; return (results, profiles,
    the arguments without the output files)."""
    spec = SPECS[sid]
    margin = (0.2 if "T" in spec else 0.25) + 2.0 * spec["sigma"]
    stem = f"{sid}_{'refined' if refined else 'canonical'}"
    arguments = ["single", "--m", "1", "--lambda", repr(spec["lam"]),
                 "--a4", repr(spec["a4"]), "--N", repr(spec["N"]),
                 "--margin", repr(margin)]
    if "T" in spec:
        arguments += ["--T", repr(spec["T"])]
    if refined:
        arguments.append("--refined")
```

`run_single` runs the solver's command `single` for one state. The **margin** decides how many levels above the Fermi level the label set keeps: $0.25 + 2\sigma$ at $T = 0$ and $0.2 + 2\sigma$ at $T > 0$, exactly as in the cross-check's measurement program (`"T" in spec` asks whether the dictionary has the key `"T"`). `stem` is the base of the two output file names, the state id followed by `_canonical` or `_refined`. `arguments` is the list of the program's arguments: the command, the mass 1, the coupling, the slice, $N$ and the margin, each number written with `repr` (the shortest decimal text that gives back exactly the same double); a thermal state adds its temperature, and a refined run adds the option that switches to the refined numerics of Section 16.6.

```python
    files = ["--out", f"{RUN_FOLDER / stem}.json",
             "--profiles", f"{RUN_FOLDER / stem}.csv"]
    done = subprocess.run([str(SOLVER)] + arguments + files, cwd=str(REPO),
                          capture_output=True, text=True)
    if done.returncode != 0 or not done.stdout.strip().endswith("SUCCESS"):
        print(done.stderr[-2000:])
        raise RuntimeError(f"the Rust run {stem} failed")
    results = json.loads((RUN_FOLDER / f"{stem}.json").read_text(encoding="utf-8"))
    with open(RUN_FOLDER / f"{stem}.csv", newline="", encoding="utf-8") as handle:
        profiles = [{k: float(v) for k, v in row.items()}
                    for row in csv.DictReader(handle)]
    return results, profiles, arguments
```

`files` adds the two output options: a JSON file with the energies, levels and integrals, and a CSV file with the profiles, both in `RUN_FOLDER` (`RUN_FOLDER / stem` joins the folder and the name). `subprocess.run` runs the program from the repository folder (`cwd=...`) and keeps its messages. If the program failed (a return code other than 0, or a last line other than SUCCESS; `.strip()` removes blanks and line ends), the function prints the end of the error messages and stops. Otherwise it reads the JSON file back and reads the CSV file as a list of rows, each a dictionary from the column names to numbers (`float(v)` turns each text into a number). It returns the two and the argument list.

```python
RUST = {}  # (state id, "canonical" or "refined") -> (results, profiles)
for sid in SPECS:
    for refined in (False, True):
        results, profiles, arguments = run_single(sid, refined)
        RUST[(sid, "refined" if refined else "canonical")] = (results, profiles)
    say("revision_ks_solver " + " ".join(arguments))  # the refined command
check(len(RUST) == 10, "ten Rust runs (five states, two numerics) completed")
```

The double loop runs every state twice, canonical (`refined` false) and refined (true), and keeps the results in the dictionary `RUST` under the pair (state id, kind). After each state it prints the refined command without the output files (whose folder differs from computer to computer): Out [12]. The check confirms ten runs.

**In [13], do the runs reproduce the committed Rust results?**

```python
SUMMARY = {r["id"]: r for r in read_csv(f"{KS}/results/ground/summary.csv")}
EMT = {r["id"]: r for r in read_csv(f"{KS}/results/ground/emt-integrals.csv")}
EXCITED = {r["id"]: r for r in read_csv(f"{KS}/results/excited/summary.csv")}
ADIABATIC = {r["id"]: r for r in read_csv(f"{KS}/results/adiabatic/adiabaticity.csv")}
THERMO = {r["id"]: r for r in read_csv(f"{KS}/results/thermo/thermodynamics.csv")}
REFINEMENT = {(s["kind"], s["id"]): s
              for s in read_json(f"{KS}/checker/rust-refinement.json")["states"]}
```

The committed canonical Rust results are read: the ground-state summary, the energy-momentum integrals, the excited-state summary, the adiabaticity table and the thermodynamics table, each filed under the state id. `REFINEMENT` holds the cross-check's measurement file `rust-refinement.json`, filed under the pair (kind, id).

```python
def rel(a, b):
    """|a - b| relative to max(1, |b|)."""
    return abs(a - b) / max(1.0, abs(b))

def level_map(results):
    """{(n2, j, parity, label): eps} of the levels of a `single` run."""
    return {tuple(l[:4]): l[4] for l in results["levels_n2_j_parity_label_eps_deg_f"]}
```

`rel(a, b)` is the difference of `a` and `b` relative to $\max(1, |b|)$. `level_map` turns the list of levels of a single run (each level a list of $n_2$, $j$, parity, label, energy, degeneracy, occupation) into a dictionary from the first four entries (`tuple(l[:4])`, the key of the level) to its energy (`l[4]`).

```python
for sid in SPECS:
    canon, canon_prof = RUST[(sid, "canonical")]
    refined, _ = RUST[(sid, "refined")]
    if sid in GROUND_IDS:
        worst = rel(canon["E_KS"], float(SUMMARY[sid]["E_KS"]))
        integrals = canon["emtIntegrals_2Vol7_int_e6Hy"]
        for k in ("rho", "p3", "p_t", "p8", "n"):
            worst = max(worst, rel(integrals[k], float(EMT[sid]["int_" + k])))
        committed = {(int(x["n2"]), int(x["j"]), x["parity"], int(x["label"])):
                     float(x["eps"])
                     for x in read_csv(f"{KS}/results/ground/levels/{sid}.csv")}
        mine = level_map(canon)
        worst = max([worst] + [abs(mine[k] - committed[k]) for k in mine
                               if k in committed])
        stored_prof = read_csv(f"{KS}/results/ground/profiles/{sid}.csv")
        for name in ("n", "S", "rho", "p3", "p_t", "p8"):
            top = max(abs(float(row[name])) for row in stored_prof)
            worst = max([worst] + [abs(a[name] - float(b[name])) / max(top, 1e-300)
                                   for a, b in zip(canon_prof, stored_prof)])
        kind = "ground"
```

For each state the canonical and refined results are taken from `RUST` (`refined, _ = ...` drops the refined profiles, which are not needed here). For a ground state `worst` collects the largest difference between the canonical run and the committed results: $E_{KS}$ relative; the five energy-momentum integrals relative; every level present in both (`committed` is a dictionary from the level key to the committed energy, read from the state's levels file); and every point of six profiles, measured relative to the largest value of that profile (`max(top, 1e-300)` avoids a division by zero for a profile that is zero everywhere).

```python
    else:
        row = THERMO[sid]
        worst = max(rel(canon["E_KS"], float(row["E"])),
                    abs(canon["mu_or_fermi_level"] - float(row["mu"])),
                    abs(canon["entropy"] - float(row["entropy"]))
                    / max(1e-6, abs(float(row["entropy"]))))
        kind = "thermo"
```

For a thermal state `worst` is the largest of three differences: $E$ relative, $\mu$ absolute, and the entropy relative to $\max(10^{-6}, |S|)$.

```python
    rec = REFINEMENT[(kind, sid)]
    lc, lr = level_map(canon), level_map(refined)
    level_diff = max(abs(lc[k] - lr[k]) for k in lc if k in lr)
    e_diff = abs(canon["E_KS"] - refined["E_KS"])
    say(f"{sid}: largest difference from the committed results {worst:.1e}; "
        f"|canonical - refined|: E_KS {e_diff:.3e}, levels {level_diff:.3e}")
    same = (abs(e_diff - rec["scalars"]["E_KS"]["abs_diff"])
            <= 1e-12 * max(1.0, abs(canon["E_KS"]))
            and abs(level_diff - rec["levels"]["max_abs_diff"]) <= 1e-12)
    if kind == "thermo":
        mu_diff = abs(canon["mu_or_fermi_level"] - refined["mu_or_fermi_level"])
        same = same and abs(mu_diff - rec["scalars"]["mu"]["abs_diff"]) <= 1e-12
    check(worst <= 1e-12, f"the canonical run of {sid} reproduces the committed "
                          "Rust results",
          record=f"{KS}/reports/ks-crosscheck.json, check "
                 "rust_refinement_applies_to_matrix")
    check(same, f"canonical minus refined of {sid} reproduces the measured values",
          record=f"{KS}/checker/rust-refinement.json, state {kind} {sid}")
```

`rec` is the measurement of this state in `rust-refinement.json`. `level_diff` is the largest canonical-minus-refined difference over the levels present in both runs, and `e_diff` the difference of $E_{KS}$. The printed line (Out [13]) shows both and `worst`, which is exactly 0 in all five states. `same` asks whether these differences equal the recorded ones within $10^{-12}$; for thermal states the difference of $\mu$ must also agree. The first check reproduces the cross-check's check rust_refinement_applies_to_matrix: the canonical run gives exactly the committed results, so the measured differences apply to them. The second reproduces the state's entry of the measurement file. For example N688_lam0_a00 has $|x_c - x_r| = 7.529\times10^{-10}$ for $E_{KS}$, the number used in Section 16.6.

**In [14], the tolerance rule in a few lines.**

```python
RK4_FACTOR = 16.0 / 15.0  # canonical error = (16/15) |canonical - refined|
ROWS = []  # (class, case, x_Rust, x_ref, U_ref, U_Rust, tolerance, |diff|, ratio)

def compare(cls, case, x_rust, x_ref, u_ref, u_rust, scale=None):
    """The tolerance rule of the cross-check; returns the ratio."""
    scale = max(1.0, abs(x_ref)) if scale is None else scale
    tolerance = 3.0 * (u_ref + u_rust) + 1e-12 * scale
    diff = abs(x_rust - x_ref)
    ratio = diff / tolerance
    ROWS.append((cls, case, x_rust, x_ref, u_ref, u_rust, tolerance, diff, ratio))
    return ratio
```

`RK4_FACTOR` is the factor $\tfrac{16}{15}$ of Section 16.6. `ROWS` will hold one tuple per comparison. `compare` is the tolerance rule of Section 16.7: the scale is $\max(1, |x_{ref}|)$ unless a scale is given (for profile points), the tolerance is $3(U_{ref} + U_{Rust}) + 10^{-12}\cdot$scale, the difference is $|x_{Rust} - x_{ref}|$, and the ratio is their quotient. The function stores all nine numbers of the comparison in `ROWS` and returns the ratio.

```python
PROFILE_NAMES = ("n", "S", "Q", "M_eff", "v_v", "e_int", "rho", "p3", "p_t", "p8")

def rust_uncertainties(sid):
    """U_Rust of every quantity reported by `single`, for state sid."""
    (canon, cp), (refined, rp) = RUST[(sid, "canonical")], RUST[(sid, "refined")]
    U = {k: RK4_FACTOR * abs(canon[k] - refined[k])
         for k in ("E_KS", "E_band", "E_int", "entropy")}
    U["mu"] = RK4_FACTOR * abs(canon["mu_or_fermi_level"]
                               - refined["mu_or_fermi_level"])
    ci, ri = canon["emtIntegrals_2Vol7_int_e6Hy"], refined["emtIntegrals_2Vol7_int_e6Hy"]
    for k in ("rho", "p3", "p_t", "p8", "n"):
        U["int_" + k] = RK4_FACTOR * abs(ci[k] - ri[k])
    for k in ("rho", "p3", "p_t", "p8"):  # profile end points: brane and tip
        U[k + "_brane"] = RK4_FACTOR * abs(cp[-1][k] - rp[-1][k])
        U[k + "_tip"] = RK4_FACTOR * abs(cp[0][k] - rp[0][k])
    lc, lr = level_map(canon), level_map(refined)
    U["levels"] = RK4_FACTOR * max(abs(lc[k] - lr[k]) for k in lc if k in lr)
    for name in PROFILE_NAMES:  # (U of the profile, largest |value|)
        U["profile_" + name] = (
            RK4_FACTOR * max(abs(a[name] - b[name]) for a, b in zip(cp, rp)),
            max(abs(a[name]) for a in cp))
    return U
```

`PROFILE_NAMES` are the ten profiles of the record: $n$, $S$, $Q$, $M_{eff}$, $v_v$, $e_{int}$, $\rho$, $p_3$, $p_t$, $p_8$. `rust_uncertainties` computes $U_{Rust} = \tfrac{16}{15}|x_c - x_r|$ for every quantity that the single runs report: the three energies and the entropy (a dictionary comprehension), $\mu$, the five integrals, the values of $\rho$, $p_3$, $p_t$, $p_8$ at the brane (the last profile point, index `-1`) and at the tip (the first, index 0), the levels (one number: $\tfrac{16}{15}$ times the largest difference over all levels of the state), and for each profile a pair: $\tfrac{16}{15}$ times the largest difference over its points, and the largest value of the profile.

```python
U_RUST = {sid: rust_uncertainties(sid) for sid in SPECS}
WIDE = REPORTS["cross-check"]["rust_matrix_wide_uncertainties"]
say("matrix-wide Rust differences: " + ", ".join(
    f"{k.replace('refined_', '')} {v:.2e}" for k, v in sorted(WIDE.items())))
```

`U_RUST` holds these uncertainties for the five states. `WIDE` is the dictionary of matrix-wide differences recorded in the cross-check report for the quantities that single runs do not report (Section 16.6); the printed line lists them, with the prefix `refined_` removed from each name (`.replace`), sorted by name (Out [14]).

```python
sid = "N8_lamm2_a00"  # one comparison, piece by piece
x_rust = float(SUMMARY[sid]["E_KS"])
x_ref = NEW[sid]["scalars"]["E_KS"]["value"]
u_ref = NEW[sid]["scalars"]["E_KS"]["U"]
u_rust = U_RUST[sid]["E_KS"]
ratio = compare("ground_energies", f"{sid} E_KS", x_rust, x_ref, u_ref, u_rust)
say(f"E_KS of {sid}: Rust {x_rust!r}, reference {x_ref!r}")
say(f"    |diff| = {abs(x_rust - x_ref):.3e}, U_ref = {u_ref:.3e}, "
    f"U_Rust = {u_rust:.3e}")
say(f"    tolerance = 3 (U_ref + U_Rust) + 1e-12 max(1, |x|) = {ROWS[-1][6]:.3e}, "
    f"ratio = {ratio:.4f}")
check(ratio <= 1.0, f"E_KS of {sid} agrees within the tolerance")
```

One comparison piece by piece: $E_{KS}$ of N8_lamm2_a00 from the committed Rust summary and from the new reference result, with $U_{ref}$ from the reference and $U_{Rust}$ from the measurement. The three printed lines (Out [14]) are the numbers of the worked comparison of Section 16.7: difference $1.264\times10^{-13}$, $U_{ref} = 2.096\times10^{-12}$, $U_{Rust} = 1.214\times10^{-13}$, tolerance $7.651\times10^{-12}$, ratio $0.0165$ (`ROWS[-1][6]` is the tolerance of the last comparison). The check requires the ratio to be at most 1.

**In [15], the ground-state comparisons.**

```python
def rank_key(n2, j, parity, rank):
    """The level key n2:j:parity:rank as a text, for example 1:-1:even:2."""
    return f"{int(n2)}:{'+1' if int(j) > 0 else '-1'}:{parity}:{int(rank)}"
```

`rank_key` writes the key of a level as a text such as `1:-1:even:2`: the shell $n_2$, the block type with its sign, the parity and the rank (Chapter 15: the rank counts the levels of a sector from the lowest particle level).

```python
U_DSCF = RK4_FACTOR * WIDE["refined_delta_scf"]  # matrix-wide Delta-SCF uncertainty
for sid in GROUND_IDS:
    sc, U = NEW[sid]["scalars"], U_RUST[sid]
    for k in ("E_KS", "E_band", "E_int"):
        if not (sid == "N8_lamm2_a00" and k == "E_KS"):  # made in section 13
            compare("ground_energies", f"{sid} {k}", float(SUMMARY[sid][k]),
                    sc[k]["value"], sc[k]["U"], U[k])
    for k, u in (("HOMO", U["levels"]), ("LUMO", U["levels"]),
                 ("KS_gap", 2.0 * U["levels"])):
        compare("ground_homo_lumo_gap", f"{sid} {k}", float(SUMMARY[sid][k]),
                sc[k]["value"], sc[k]["U"], u)
```

`U_DSCF` is the matrix-wide Delta-SCF uncertainty. For each ground state: the three energies are compared (skipping $E_{KS}$ of N8_lamm2_a00, which In [14] already compared), and HOMO, LUMO and the gap, each with the largest level uncertainty of the state, the gap with twice that (it is a difference of two levels).

```python
    rust_levels = {}  # key -> (eps, occupation) of the committed Rust levels
    for x in read_csv(f"{KS}/results/ground/levels/{sid}.csv"):
        rank = int(x["label"]) - int(x["label_min"])
        rust_levels[rank_key(x["n2"], x["j"], x["parity"], rank)] = (
            float(x["eps"]), float(x["f"]))
    lev = NEW[sid]["levels"]
    ref_levels = {rank_key(*k): (e, u, f)
                  for k, e, u, f in zip(lev["keys"], lev["eps"], lev["U"], lev["f"])}
    common = sorted(set(rust_levels) & set(ref_levels))
    for k in common:
        compare("ground_eigenvalues", f"{sid} level {k}", rust_levels[k][0],
                ref_levels[k][0], ref_levels[k][1], U["levels"])
```

The committed Rust levels of the state are read and filed under their keys, with the Rust label turned into a rank by subtracting `label_min`, the label of the lowest particle level of its sector; each entry holds the energy and the occupation. The reference levels are filed the same way, with energy, uncertainty and occupation (`zip` walks through four lists at once). `common` is the sorted list of the keys present in both (`&` of two sets is their common part), and every common level is compared with the level uncertainty of the state.

```python
    occupied_rust = sorted(k for k, v in rust_levels.items() if v[1] > 0)
    occupied_ref = sorted(k for k, v in ref_levels.items() if v[2] > 0)
    compare("excited_delta_scf", f"{sid} delta_SCF", float(EXCITED[sid]["delta_SCF"]),
            sc["delta_SCF"]["value"], sc["delta_SCF"]["U"], U_DSCF)
    compare("excited_delta_scf", f"{sid} E_excited", float(EXCITED[sid]["E_excited"]),
            sc["E_excited"]["value"], sc["E_excited"]["U"], U["E_KS"] + U_DSCF)
    say(f"{sid}: {len(rust_levels)} Rust levels, {len(ref_levels)} reference levels, "
        f"{len(common)} compared; {len(occupied_rust)} occupied in both")
    check(occupied_rust == occupied_ref, f"the same occupied levels in {sid}",
          record=f"{KS}/reports/ks-crosscheck.json, check "
                 "ground_occupations_and_groups")
```

`occupied_rust` and `occupied_ref` are the sorted keys of the occupied levels of each solver. The Delta-SCF energy and the energy of the excited state are compared (the latter with the sum of the uncertainties of $E_{KS}$ and of the Delta-SCF energy). The printed line (Out [15]) shows how many levels each solver kept and how many were compared: the Rust solver keeps more levels than the reference (64 against 22 for N8_lamm2_a00), and every reference level has a Rust partner. The check requires the same occupied levels, reproducing the check ground_occupations_and_groups.

**In [16], energy-momentum tensor and adiabaticity.**

```python
U_ADIABATIC = RK4_FACTOR * WIDE["refined_adiabatic_derivatives"]  # relative
for sid in GROUND_IDS:
    sc, U, e = NEW[sid]["scalars"], U_RUST[sid], EMT[sid]
    for k in ("rho", "p3", "p_t", "p8", "n"):
        compare("emt_integrals", f"{sid} int_{k}", float(e["int_" + k]),
                sc["int_" + k]["value"], sc["int_" + k]["U"], U["int_" + k])
    for k in ("rho", "p3", "p_t", "p8"):
        for end in ("brane", "tip"):
            name = f"{k}_{end}"
            compare("emt_brane_tip_values", f"{sid} {name}", float(e[name]),
                    sc[name]["value"], sc[name]["U"], U[name])
```

`U_ADIABATIC` is the matrix-wide relative uncertainty of the derivatives along the history. For each ground state the five integrals are compared, each with its measured $U_{Rust}$, and the four quantities $\rho$, $p_3$, $p_t$, $p_8$ at the brane and at the tip (eight comparisons; `name` is for example `rho_tip`).

```python
    stored = read_csv(f"{KS}/results/ground/profiles/{sid}.csv")
    for name in PROFILE_NAMES:
        values = [float(row[name]) for row in stored]
        top = max(max(abs(v) for v in values), 1e-300)  # the scale of the profile
        ref = NEW[sid]["profiles"][name]
        for i, row in enumerate(stored):
            compare("ground_profiles", f"{sid} {name}(y = {float(row['y']):.2f})",
                    values[i], ref["value"][i], ref["U"][i],
                    U["profile_" + name][0], scale=top)
```

The committed Rust profiles of the state are read; for each of the ten profiles `top` is its largest value (the scale of Section 16.7) and `ref` the reference profile with its uncertainties. Every one of the 151 points is compared, its case named with the profile and the position, for example `rho(y = -3.00)`.

```python
    u_q, top_q = U["profile_Q"]
    dex = float(e["deltaE_x_exact_fock"])
    compare("exchange_delta_E_x", f"{sid} deltaE_x", dex,
            sc["deltaE_x_exact_fock"]["value"], sc["deltaE_x_exact_fock"]["U"],
            RK4_FACTOR * 2.0 * (u_q / RK4_FACTOR) / max(top_q, 1e-300) * abs(dex))
```

The exchange difference $\Delta E_x$, with the uncertainty derived in Section 16.7: twice the relative uncertainty of the profile $Q$ times $|\Delta E_x|$. The code multiplies by `RK4_FACTOR` and divides `u_q` by it again; the two factors cancel, and what remains is $2\,(U_Q/\max|Q|)\,|\Delta E_x|$, where $U_Q$ already contains the factor $\tfrac{16}{15}$.

```python
    a = ADIABATIC[sid]
    compare("adiabatic_dE_da4", f"{sid} dE_da4_emt", float(a["dE_da4_emt"]),
            sc["dE_da4_emt"]["value"], sc["dE_da4_emt"]["U"],
            3.0 * (U["int_p3"] + U["int_p_t"]))
    fd = float(a["dE_da4_finite_difference"])
    compare("adiabatic_dE_da4", f"{sid} dE_da4_finite_difference", fd,
            sc["dE_da4_fd"]["value"], sc["dE_da4_fd"]["U"], U_ADIABATIC * abs(fd))
    q_rust, ad = float(a["Q_max"]), NEW[sid]["adiabatic"]
    compare("adiabatic_Q_max", f"{sid} Q_max", q_rust, ad["Q_max"], ad["U_Q_max"],
            U_ADIABATIC * abs(q_rust))
```

The derivative $dE/da_4$ in its energy-momentum form, with the uncertainty $3(U_{I_3} + U_{I_t})$ derived in Section 16.7, and as a difference quotient, with the matrix-wide relative uncertainty. Then the adiabaticity measure $Q_{max}$ of Chapter 15.

```python
    if q_rust > 0:
        top = ad["top"][0]  # the reference's maximising pair
        hole, particle = [s.strip() for s in a["Q_max_pair"].split("->")]
        say(f"{sid}: Q_max = {q_rust:.10f} for the pair {hole} -> {particle} (Rust), "
            f"{top['hole']} -> {top['particle']} (reference)")
        check((hole, particle) == (top["hole"], top["particle"]),
              f"both solvers find the same maximising pair in {sid}")
        me = float(a["Q_max_matrix_element"])
        compare("adiabatic_Q_max", f"{sid} Q_max matrix element", me,
                top["matrix_element"], top["U_matrix_element"], U_ADIABATIC * abs(me))
        compare("adiabatic_Q_max", f"{sid} Q_max delta eps", float(a["Q_max_delta_eps"]),
                top["delta_eps"], top["U_delta_eps"], 2.0 * U["levels"])
```

When $Q_{max}$ is not zero (it is zero for the states with $N = 8$, where no matrix element connects an occupied and an empty level of the same sector), the maximising pair of levels must be the same in both solvers. The Rust table writes the pair as `hole -> particle`; `.split("->")` cuts the text at the arrow and `.strip()` removes the blanks. The printed lines (Out [16]) show $Q_{max} = 0.0934505917$ for N688_lam0_a00 and $0.0421562349$ for N136_lamp2_a20, with the same pairs in both solvers; the check requires this. Then the matrix element and the level spacing of the pair are compared.

```python
ground_rows = [r for r in ROWS if r[1].split()[0] in GROUND_IDS]
say(f"{len(ground_rows)} ground-state comparisons so far")
check(all(r[8] <= 1.0 for r in ground_rows),
      "every ground-state comparison of the subset passes the tolerance rule")
```

`ground_rows` are the comparisons whose case begins with a ground-state id (`.split()[0]` is the first word). Out [16] reports 5122 of them, and the check requires every ratio to be at most 1.

**In [17], the thermal comparisons.**

```python
ROOT_TOLERANCE = RUST_PARAMS["numerics"]["rootTolerance"]  # 1e-13
U_HEAT = RK4_FACTOR * WIDE["refined_heat_capacity"]  # relative, matrix-wide
for sid in THERMAL_IDS:
    th, U, row = NEW[sid]["thermo"], U_RUST[sid], THERMO[sid]
    T, N = NEW[sid]["T"], NEW[sid]["N"]
    u_f = U["E_KS"] + T * U["entropy"]
    for k, u in (("mu", U["mu"]), ("E", U["E_KS"]), ("entropy", U["entropy"]),
                 ("F", u_f), ("Omega_direct", u_f + N * U["mu"]),
                 ("Omega_F_minus_muN", u_f + N * U["mu"])):
        compare("thermo_state_functions", f"{sid} {k}", float(row[k]),
                th[k]["value"], th[k]["U"], u)
```

`ROOT_TOLERANCE` is the Rust root tolerance $10^{-13}$, read from its parameters, and `U_HEAT` the matrix-wide relative uncertainty of the heat capacity. For each thermal state, `u_f` is $U_F = U_E + T\,U_S$ (Section 16.7), and six state functions are compared: $\mu$, $E$, $S$, $F$, and $\Omega$ in its two forms, both with $U_\Omega = U_F + N\,U_\mu$.

```python
    dT = 0.01 * T
    for k in ("C_V", "C_V_from_dEdT", "minus_dFdT"):
        x = float(row[k])
        quotient = k != "C_V"  # a difference quotient of energies
        compare("thermo_derivatives", f"{sid} {k}", x, th[k]["value"],
                th[k]["U"] + (N * 1e-12 / dT if quotient else 0.0),
                U_HEAT * max(abs(x), 1e-6)
                + (N * ROOT_TOLERANCE / dT if quotient else 0.0))
```

The three derivatives with respect to $T$: $C_V = T\,dS/dT$ and the two difference quotients $dE/dT$ and $-dF/dT$, for which the noise floors of Section 16.7 are added, $N\cdot10^{-12}/dT$ to the reference and $N\cdot10^{-13}/dT$ to the Rust solver, with $dT = 0.01\,T$ (`x if condition else y` takes `x` when the condition holds and `y` otherwise).

```python
    r = next(r for r in ROWS if r[1] == f"{sid} mu")
    say(f"{sid}: mu Rust {r[2]!r}, reference {r[3]!r}, ratio {r[8]:.4f}")
thermal_rows = [r for r in ROWS if r[1].split()[0] in THERMAL_IDS]
say(f"{len(thermal_rows)} thermal comparisons; {len(ROWS)} comparisons in all")
check(len(ROWS) == 5140 and all(r[8] <= 1.0 for r in ROWS),
      "all 5140 comparisons of the subset pass the tolerance rule")
```

`next(...)` finds the comparison of $\mu$ of the state, and its two values and ratio are printed (Out [17]: for N8_lamm1_a00_T10 the two values of $\mu$ differ by $4.0\times10^{-13}$, ratio $0.0438$). The last check counts all comparisons, 5140 (5122 ground and 18 thermal), and requires every ratio to be at most 1.

**In [18], reproducing the committed cross-check report.**

```python
TABLE = {r["case"]: r for r in read_csv(f"{KS}/reports/ks-crosscheck-table.csv")}
matched, largest = 0, 0.0
for cls, case, *_, tolerance, diff, ratio in ROWS:
    if case in TABLE:
        matched += 1
        stored = TABLE[case]
        largest = max(largest, abs(ratio - float(stored["ratio"])))
        if abs(ratio - float(stored["ratio"])) > 6e-4 or \
                abs(tolerance - float(stored["tolerance"])) > 1e-3 * tolerance:
            say(f"differs: {case}: {ratio:.4f} vs {stored['ratio']}")
say(f"{matched} of our comparisons are rows of the committed table; the largest "
    f"difference of the ratio is {largest:.1e}")
check(matched == 97 and largest <= 6e-4,
      "our tolerances and ratios equal the 97 matching rows of the committed table",
      record=f"{KS}/reports/ks-crosscheck-table.csv")
```

The cross-check wrote every comparison of single numbers into its table `ks-crosscheck-table.csv` (levels and profile points are too many and appear only in the report). `TABLE` files the rows under their case names. The loop goes through our comparisons, unpacking each tuple into its class, case, tolerance, difference and ratio (`*_` collects the four middle entries, which are not needed); whenever a case is a row of the table, it counts it and compares our ratio and tolerance with the stored ones, which the table keeps with four significant digits. Out [18]: 97 of our comparisons are rows of the table, and the largest difference of a ratio is $5.0\times10^{-5}$. The check requires 97 matches within $6\times10^{-4}$.

```python
WORST_CASES = {}  # class -> (worst ratio in the report, its case)
pattern = re.compile(r"worst \|diff\|/tolerance ([0-9.]+) \((.+?): Rust ")
for c in REPORTS["cross-check"]["checks"]:
    found = pattern.search(c["detail"])
    if found and c["name"] in ("ground_eigenvalues", "ground_profiles",
                               "emt_brane_tip_values", "adiabatic_Q_max",
                               "thermo_state_functions", "thermo_derivatives"):
        WORST_CASES[c["name"]] = (float(found.group(1)), found.group(2))
for cls, (ratio, case) in sorted(WORST_CASES.items()):
    mine = max((r for r in ROWS if r[0] == cls), key=lambda r: r[8])
    say(f"{cls}: report {ratio:.3f} ({case}); this notebook {mine[8]:.3f} "
        f"({mine[1]})")
    check(mine[1] == case and abs(mine[8] - ratio) <= 6e-4,
          f"the worst case of {cls} is reproduced",
          record=f"{KS}/reports/ks-crosscheck.json, check {cls}")
```

`re.compile` prepares a pattern that reads, from the detail sentence of a check of the cross-check report, the worst ratio and its case: `\|` is a literal vertical bar, and `(.+?)` captures the shortest text up to `: Rust` (the question mark makes the match as short as possible). For six classes the worst ratio and case are kept in `WORST_CASES`. For each, `mine` is our comparison with the largest ratio in that class. Out [18] prints both: the worst case of the whole cross-check in each of the six classes is a comparison of our subset, with the same ratio ($0.314$, $0.495$, $0.324$, $0.495$, $0.226$, $0.284$). The six checks require the same case and the same ratio within $6\times10^{-4}$.

**In [19], the levels of N136_lamp2_a20 (Figure 16a.4).**

```python
rows = [r for r in ROWS if r[0] == "ground_eigenvalues"
        and r[1].startswith("N136_lamp2_a20 ")]
worst = max(rows, key=lambda r: r[8])
fig, ax = plt.subplots(figsize=(7.5, 4.3))
ax.semilogy([r[3] for r in rows], [max(r[8], 1e-6) for r in rows], "o",
            color=PALETTE[0], ms=4, alpha=0.8, label="one level of N136_lamp2_a20")
ax.semilogy([worst[3]], [worst[8]], "o", color=PALETTE[1], ms=9,
            label=f"largest ratio {worst[8]:.3f}: level "
                  f"{worst[1].split('level ')[1]}")
ax.axhline(1.0, color="k", lw=1.2, label="ratio 1: the tolerance")
ax.set_ylim(1e-6, 3.0)
ax.set_xlabel("level energy $\\varepsilon$ (reference value, units of $m$)")
ax.set_ylabel("$|\\varepsilon_{Rust} - \\varepsilon_{ref}|$ / tolerance")
ax.set_title(f"{len(rows)} levels of N136_lamp2_a20 compared")
ax.legend(fontsize=8, loc="lower right")
```

`rows` are the 354 level comparisons of N136_lamp2_a20 (`startswith` tests the beginning of the case name), and `worst` the one with the largest ratio. The figure draws each level's ratio against its reference energy on a logarithmic vertical axis (ratios below $10^{-6}$ raised to $10^{-6}$), the worst level as a large orange circle with its key in the legend (`.split('level ')[1]` takes the text after `level `), and the line ratio 1.

```python
save_figure(fig, "level_agreement",
            "Agreement of the two solvers for every level of the ground state "
            "N136_lamp2_a20 ($N = 136$, $\\lambda = +\\lambda_2$, $a_{4,0} = 2$): the "
            "difference of the two level energies divided by the tolerance $3(U_{ref} "
            "+ U_{Rust}) + 10^{-12}\\max(1, |\\varepsilon|)$, against the level energy "
            "in units of $m$ (vertical axis logarithmic; ratios below one millionth "
            "are drawn at $10^{-6}$). Every point lies below the line 1, so every "
            f"level passes; the largest ratio, {worst[8]:.3f}, is the largest of all "
            "9616 level comparisons of the full cross-check.")
check(len(rows) == 354 and worst[8] < 1.0,
      "all 354 levels of N136_lamp2_a20 agree within the tolerance")
```

`save_figure` saves Figure 16a.4. What the student should see: every point lies below the line 1. The ratios rise with the level energy, from below $10^{-4}$ near 0 to $0.324$ for the level 1:-1:even:2 at $3.24$, because the higher levels' orbitals oscillate faster and both solvers are less accurate there; the largest ratio is the largest of all 9616 level comparisons of the full cross-check. The check requires 354 levels and the largest ratio below 1.

**In [20], the profile with the largest ratio (Figure 16a.5).**

```python
sid = "N8_lamm2_a00"
stored = read_csv(f"{KS}/results/ground/profiles/{sid}.csv")
y = np.array([float(row["y"]) for row in stored])
fig, (top, bottom) = plt.subplots(2, 1, figsize=(7.5, 6.6), sharex=True)
top.plot(y, [float(row["rho"]) for row in stored], color=PALETTE[0], lw=1.8,
         label="Rust solver")
top.plot(y[::5], NEW[sid]["profiles"]["rho"]["value"][::5], "o", color=PALETTE[1],
         ms=5, mfc="none", label="reference solver")
top.set_ylabel("$\\rho(y)$ (proper energy density, units of $m$)")
top.set_title("Energy density of N8_lamm2_a00")
top.legend(fontsize=8)
```

The committed Rust profiles of N8_lamm2_a00 are read, `y` holds the 151 positions $-3, -2.98, \dots, 0$, and a figure with two panels one above the other is made (`sharex=True` gives them the same horizontal axis). The upper panel draws the Rust energy density as a line and the reference energy density at every fifth point (`[::5]`) as open circles (`mfc="none"`: no fill).

```python
largest = 0.0
for colour, name in ((PALETTE[0], "rho"), (PALETTE[2], "p8")):
    ratios = [r[8] for r in ROWS if r[0] == "ground_profiles"
              and r[1].startswith(f"{sid} {name}(")]
    largest = max(largest, max(ratios))
    bottom.semilogy(y, np.maximum(ratios, 1e-6), "-", color=colour, lw=1.5,
                    label=f"profile {name}")
bottom.axhline(1.0, color="k", lw=1.2, label="ratio 1: the tolerance")
bottom.set_ylim(1e-6, 3.0)
bottom.set_xlabel("hidden coordinate $y$ (tip $y = -3$, brane $y = 0$)")
bottom.set_ylabel("$|$Rust $-$ reference$|$ / tolerance")
bottom.legend(fontsize=8, loc="center right")
fig.tight_layout()
```

The lower panel draws, for $\rho$ and for $p_8$, the ratio of each of the 151 point comparisons against $y$ (`np.maximum` raises the small ratios to $10^{-6}$ point by point), and the line ratio 1; `largest` keeps the largest ratio of the two profiles.

```python
save_figure(fig, "profile_agreement",
            "The profile with the largest ratio of the whole cross-check. Top: the "
            "proper energy density $\\rho(y)$ of the ground state N8_lamm2_a00 "
            "($N = 8$, $\\lambda = -\\lambda_2$, $a_{4,0} = 0$) from the Rust solver "
            "(line) and the reference solver (circles), in units of $m$, against the "
            "hidden coordinate $y$. Bottom: the difference divided by the tolerance "
            "at each of the 151 points for $\\rho$ and $p_8$ (logarithmic). The "
            f"largest ratio, {largest:.3f}, is at the tip $y = -3$, where the "
            "densities are largest and both solvers are least accurate.")
```

`save_figure` saves Figure 16a.5. What the student should see: in the upper panel the energy density of this state is negative and steep near the tip (it reaches about $-10.2$ at $y = -3$) and practically zero over most of the interval, and the circles of the reference lie on the Rust line; in the lower panel the ratios fall from $0.495$ at the tip to below $10^{-6}$ towards the brane. The largest ratio of the whole cross-check sits at the tip because that is where the densities, and with them both programs' errors, are largest.

**In [21], who sets the tolerance? (Figure 16a.6).**

```python
groups = {"ground states, single numbers": [], "ground states, levels": [],
          "thermal states": []}
for r in ROWS:
    if r[0] == "ground_profiles" or r[4] <= 0.0 or r[5] <= 0.0:
        continue  # profile points are drawn elsewhere; a zero U has no logarithm
    if r[1].split()[0] in THERMAL_IDS:
        groups["thermal states"].append(r)
    elif r[0] == "ground_eigenvalues":
        groups["ground states, levels"].append(r)
    else:
        groups["ground states, single numbers"].append(r)
```

The comparisons are sorted into three groups for the figure: ground-state single numbers, ground-state levels and thermal states. Profile points are left out (they appear in Figure 16a.7), and so are comparisons in which one of the two uncertainties is exactly zero, because zero has no logarithm (`continue` skips to the next comparison).

```python
fig, ax = plt.subplots(figsize=(6.6, 5.6))
for colour, (label, rows) in zip(PALETTE, groups.items()):
    ax.loglog([r[4] for r in rows], [r[5] for r in rows], "o", color=colour, ms=4,
              alpha=0.75, label=f"{label} ({len(rows)})")
span = np.array([1e-18, 1e-5])
ax.loglog(span, span, "k-", lw=1.0, label="$U_{Rust} = U_{ref}$")
ax.set_xlabel("$U_{ref}$ (Richardson uncertainty of the reference)")
ax.set_ylabel("$U_{Rust}$ (16/15 of canonical minus refined)")
ax.set_title("Who sets the tolerance?")
ax.legend(fontsize=8)
above = sum(1 for rows in groups.values() for r in rows if r[5] > r[4])
total = sum(len(rows) for rows in groups.values())
```

Each group is drawn as points at the position ($U_{ref}$, $U_{Rust}$) on logarithmic axes, with the diagonal $U_{Rust} = U_{ref}$ as a black line. `above` counts the points above the diagonal and `total` all points.

```python
save_figure(fig, "uncertainty_budget",
            "The two uncertainties that make the tolerance, for every comparison of "
            "single numbers and of levels in the five states of the subset: the "
            "Richardson uncertainty $U_{ref}$ of the reference solver (horizontal) "
            "and the measured uncertainty $U_{Rust}$ of the Rust solver (vertical), "
            "both logarithmic and in the units of the quantity. Points above the "
            "diagonal are dominated by the Rust uncertainty, points below it by the "
            f"reference; {above} of the {total} points lie above it. Comparisons in "
            "which one uncertainty is exactly zero are left out.")
say(f"{above} of {total} drawn comparisons have U_Rust > U_ref")
check(total > 500, "the uncertainty budget has more than 500 comparisons")
```

`save_figure` saves Figure 16a.6, and the printed line (Out [21]) says that 547 of the 602 drawn comparisons have $U_{Rust} > U_{ref}$. What the student should see: most points lie above the diagonal, so in most comparisons the measured Rust uncertainty is the larger part of the tolerance. The reference uncertainties of the levels lie between their floor $2\cdot10^{-12}$ and about $10^{-10}$, while the Rust level uncertainties form horizontal rows, one value per state (the largest level difference of the state, Section 16.6). The reference, with its three grids and two Richardson steps, is usually the more accurate program, and the tolerance is set mainly by the Rust solver. The check requires more than 500 drawn comparisons.

**In [22], all comparisons by class (Figure 16a.7).**

```python
classes = ["ground_energies", "ground_homo_lumo_gap", "ground_eigenvalues",
           "excited_delta_scf", "emt_integrals", "emt_brane_tip_values",
           "ground_profiles", "exchange_delta_E_x", "adiabatic_dE_da4",
           "adiabatic_Q_max", "thermo_state_functions", "thermo_derivatives"]
rng = np.random.default_rng(12345)  # fixed seed: the same picture in every run
fig, ax = plt.subplots(figsize=(9.0, 5.0))
worst_by_class = {}
```

`classes` lists the twelve classes of the cross-check that the subset fills. `rng` is a **random-number generator** with a fixed starting value (the **seed** 12345), so that the "random" numbers it gives are the same in every run and the figure is the same byte for byte. A figure of 9 by 5 inches is made, and `worst_by_class` will hold each class's largest ratio.

```python
for i, cls in enumerate(classes):
    ratios = np.array([r[8] for r in ROWS if r[0] == cls])
    jitter = rng.uniform(-0.28, 0.28, size=len(ratios))
    ax.semilogy(i + jitter, np.maximum(ratios, 1e-6), "o", color=PALETTE[0], ms=2.5,
                alpha=0.35)
    worst_by_class[cls] = float(ratios.max())
    ax.semilogy([i], [max(ratios.max(), 1e-6)], "D", color=PALETTE[1], ms=7)
    ax.text(i, 1.6, f"{len(ratios)}", ha="center", fontsize=7)
```

For each class `ratios` is the array of its ratios. `rng.uniform(-0.28, 0.28, size=...)` gives one random number between $-0.28$ and $0.28$ per ratio; adding it to the class's position spreads the dots a little sideways so that they do not hide one another (**jitter**). The dots are drawn small and half transparent (`alpha=0.35`), the class's largest ratio as an orange diamond, and the number of comparisons of the class as a small text above the plot area.

```python
ax.axhline(1.0, color="k", lw=1.2)
ax.set_xticks(range(len(classes)))
ax.set_xticklabels([c.replace("_", " ") for c in classes], rotation=40, ha="right",
                   fontsize=8)
ax.set_ylim(1e-6, 4.0)
ax.set_ylabel("$|x_{Rust} - x_{ref}|$ / tolerance")
ax.set_title("All comparisons of the subset (number of comparisons above each class)")
fig.tight_layout()
```

The line ratio 1 is drawn; the class names, with underscores replaced by blanks, are written under their positions, turned by 40 degrees and aligned at their right ends; the vertical axis runs from $10^{-6}$ to 4.

```python
top_class = max(worst_by_class, key=worst_by_class.get)
save_figure(fig, "ratios_by_class",
            f"All {len(ROWS)} comparisons of the five states of the subset, grouped "
            "by the class of the cross-check: each dot is one ratio of the difference "
            "of the two solvers to the tolerance (logarithmic; ratios below "
            "$10^{-6}$ drawn at $10^{-6}$), the diamond is the largest ratio of the "
            "class, the number above a class counts its comparisons, and the black "
            "line is the tolerance. Every dot lies below it; the largest ratio, "
            f"{worst_by_class[top_class]:.3f}, belongs to the tip value of the energy "
            "density of N8_lamm2_a00.")
for cls in classes:
    say(f"  {cls:24s} largest ratio {worst_by_class[cls]:.4f}")
top_row = max(ROWS, key=lambda r: r[8])  # the comparison with the largest ratio
say(f"the largest ratio of the subset: {top_row[8]:.4f} ({top_row[1]})")
check(max(worst_by_class.values()) < 0.5
      and top_row[1] == "N8_lamm2_a00 rho_tip",
      "no comparison uses half of its tolerance; the largest is rho at the tip")
```

`top_class` is the class with the largest ratio (`max` with `key=worst_by_class.get` compares the classes by their values). `save_figure` saves Figure 16a.7, the loop prints each class's largest ratio (Out [22]), and `top_row` is the single comparison with the largest ratio of all 5140: $0.4952$, the energy density at the tip of N8_lamm2_a00. What the student should see: every dot of every class lies below the line 1; the 4530 profile points fill a dense column from $10^{-6}$ to just below $0.5$; and no class comes closer to the line than about one half. The check requires every largest ratio below $0.5$ and the overall largest at `N8_lamm2_a00 rho_tip`.

**In [23], the last check.**

```python
figure_files = [f"{FIGURE_FOLDER}/16a_{k}_{name}.png" for k, name in enumerate(
    ["grid_convergence", "uncertainty_validated", "eigenvalue_ratios",
     "level_agreement", "profile_agreement", "uncertainty_budget",
     "ratios_by_class"], start=1)]
check(all(output_file(f).is_file() for f in figure_files),
      "every figure file of this notebook exists")
all_checks_passed()
```

`enumerate(..., start=1)` numbers the seven figure names from 1, and the list comprehension builds their file names, for example `Revision/textbook/figures/16a_1_grid_convergence.png`. The check confirms that each file exists where the notebook writes (`output_file`), and `all_checks_passed()` prints the last line, ALL 51 CHECKS PASSED (notebook 16a): three checks each in In [2], In [5], In [6], In [7], In [15] and In [16], four in In [10], ten in In [13], seven in In [18], two in In [11], and one each in In [3], In [4], In [8], In [12], In [14], In [17], In [19], In [21], In [22] and In [23].
