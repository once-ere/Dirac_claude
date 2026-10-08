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

Notebook 16a repeats the cross-check for a **subset** of five states: three ground states and two thermal states, four of them chosen because the full cross-check found its largest ratios there, and the fifth (N688_lam0_a00) because it has the most quanta. It runs the reference program of the repository on these states and on the fourth grid, checks that every new number reproduces the committed reference files, shows the convergence and Richardson extrapolation at work, builds and runs the Rust solver with its canonical and its refined numerics, applies the tolerance rule (Section 16.7) to 5140 comparisons, and reproduces 97 rows of the committed comparison table and the worst cases of six classes of the full cross-check. It needs Rust, takes about four minutes on a fast computer, draws seven figures and ends with the line ALL 51 CHECKS PASSED (notebook 16a).

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

### 16.13 Inside the reference solver I: the free problem and its exact levels

**Why a problem with known answers.** A grid method can be tested best on a problem whose exact answers are known, because then its error can be measured directly instead of estimated. The Kohn-Sham problem has such a special case: no interaction ($\lambda = 0$, so $M = m$ and $v = 0$) and no 3-momentum ($k = 0$). We call it the **free problem at zero momentum**. With $k = 0$ the factor $\kappa$ drops out of the equations of Section 16.3, and so does the slice $a_{4,0}$:

$$
a' = M a - j\varepsilon\, b, \qquad b' = j\varepsilon\, a - M b ,
$$

with a constant $M > 0$ (in the numbers $M = m = 1$, $L = 3$). Its exact levels are derived in this section (in the record: `Revision/kohn_sham/ks-theory.json`, boundaryConditions.exactK0Spectra, verified by check bc_exact_k0_spectra of `Revision/kohn_sham/reports/ks-theory-python.json`; status PROVED). Notebook 16b checks the derivation with the symbolic algebra package sympy and uses the levels to measure the errors of the reference's grid.

**Even parity, line by line.** The conditions are $b(-L) = 0$ (tip) and $b(0) = 0$ (brane). Let $\varepsilon \ne 0$; recall $j = \pm1$, so $j^2 = 1$.

$$
j\,b' = \varepsilon\,a - jM\,b \quad\Longrightarrow\quad a = \frac{j\,(b' + M b)}{\varepsilon}.
$$

Rule: multiply the second equation by $j$ (using $j^2 = 1$), move $jMb$ to the left side and divide by $\varepsilon$.

$$
\frac{j\,(b'' + M b')}{\varepsilon} = M\,\frac{j\,(b' + M b)}{\varepsilon} - j\varepsilon\,b .
$$

Rule: insert this $a$ into the first equation $a' = Ma - j\varepsilon b$; the derivative of $a$ is $j(b'' + Mb')/\varepsilon$ because $M$ and $\varepsilon$ are constants.

$$
b'' + M b' = M b' + M^2 b - \varepsilon^2 b .
$$

Rule: multiply both sides by $\varepsilon/j$ (which equals $j\varepsilon$, since $1/j = j$).

$$
b'' = -\big(\varepsilon^2 - M^2\big)\,b .
$$

Rule: cancel $Mb'$ on both sides and collect the terms with $b$.

If $\varepsilon^2 > M^2$, write $p^2 = \varepsilon^2 - M^2$ with $p > 0$. The equation $b'' = -p^2 b$ has the solutions $\alpha\sin(p(y + L)) + \beta\cos(p(y + L))$ (differentiate twice to check). The tip condition $b(-L) = 0$ gives $\beta = 0$, and since the equations are linear we may take $\alpha = 1$:

$$
b = \sin\big(p\,(y + L)\big), \qquad b(0) = \sin(pL) = 0 \quad\Longrightarrow\quad p = \frac{n\pi}{L},\ n = 1, 2, 3, \dots
$$

Rule: the sine vanishes exactly at the whole multiples of $\pi$. Hence the even levels are

$$
\varepsilon = \pm\sqrt{M^2 + \Big(\frac{n\pi}{L}\Big)^2}, \qquad n = 1, 2, 3, \dots
$$

Rule: $\varepsilon^2 = M^2 + p^2$, and both signs of the square root are allowed. (For $\varepsilon^2 \le M^2$ the solutions with $b(-L) = 0$ are $\sinh(q(y + L))$ or $y + L$, which do not vanish again at $y = 0$; so there are no other nonzero levels.) For $M = 1$, $L = 3$ the first one is $\sqrt{1 + (\pi/3)^2} = \sqrt{2.096623} = 1.447972$.

**The zero mode, line by line.** For $\varepsilon = 0$ the two equations no longer mix $a$ and $b$:

$$
a' = M a, \qquad b' = -M b \quad\Longrightarrow\quad a = A\,e^{My}, \qquad b = B\,e^{-My}.
$$

Rule: the solution of $f' = cf$ is $f = f(0)\,e^{cy}$ (Chapter 2). The tip condition $b(-L) = B\,e^{ML} = 0$ forces $B = 0$, so $b = 0$ everywhere and the brane condition $b(0) = 0$ holds automatically: $\varepsilon = 0$ is an even level, the **zero mode**, whose orbital $a = A\,e^{My}$ grows towards the brane. Its normalisation $\int_{-L}^{0}(a^2 + b^2)\,dy = 1$ fixes $A$:

$$
A^2\int_{-L}^{0} e^{2My}\,dy = A^2\,\Big[\frac{e^{2My}}{2M}\Big]_{-L}^{0} = A^2\,\frac{1 - e^{-2ML}}{2M} = 1 \quad\Longrightarrow\quad A = \sqrt{\frac{2M}{1 - e^{-2ML}}}.
$$

Rule: the antiderivative of $e^{2My}$ is $e^{2My}/(2M)$, evaluated at $0$ and at $-L$; then solve for $A > 0$. For $M = 1$, $L = 3$: $A = \sqrt{2/(1 - e^{-6})} = 1.415970$.

**Odd parity, line by line.** Now the conditions are $b(-L) = 0$ and $a(0) = 0$. The derivation of $b'' = -(\varepsilon^2 - M^2)b$ did not use any brane condition, so again $b = \sin(p(y + L))$ and $a = j(b' + Mb)/\varepsilon$:

$$
a = \frac{j\,\big(p\cos(p(y + L)) + M\sin(p(y + L))\big)}{\varepsilon}, \qquad a(0) = 0 \iff p\cos(pL) + M\sin(pL) = 0 .
$$

Rule: differentiate $b$ ($b' = p\cos(p(y + L))$), insert, and set $y = 0$; the factor $j/\varepsilon$ is not zero.

$$
\tan(pL) = -\frac{p}{M}.
$$

Rule: divide by $M\cos(pL)$ (which is not zero at a root: if $\cos(pL) = 0$ then $\sin(pL) = \pm1$ and the left side would be $\pm M \ne 0$).

**One root in each interval.** Let $F(p) = M\sin(pL) + p\cos(pL)$ and $l = 0, 1, 2, \dots$. At $pL = (l + \tfrac12)\pi$ we have $\cos = 0$ and $\sin = (-1)^l$, so $F = M(-1)^l$. At $pL = (l + 1)\pi$ we have $\sin = 0$ and $\cos = (-1)^{l+1}$, so $F = p\,(-1)^{l+1}$. The two values have opposite signs, so $F$ has a root $p_l$ between them (a continuous function that changes sign has a zero in between: the intermediate value theorem). There is only one: on that interval $\tan(pL)$ increases from $-\infty$ to 0 while $-p/M$ decreases, so they meet once; and on the intervals $l\pi < pL < (l + \tfrac12)\pi$ there is none, because there $\tan(pL) > 0 > -p/M$. So the odd levels are $\varepsilon = \pm\sqrt{M^2 + p_l^2}$, $l = 0, 1, 2, \dots$, with $p_l$ the root in $((l + \tfrac12)\pi/L, (l + 1)\pi/L)$. For $M = 1$, $L = 3$ the lowest is $1.292292828069$ (Notebook 16b, Out [2]); this is the **bulk edge** of Chapter 15, the lowest level that does not belong to the brane band.

**Ranks.** The levels of one sector (one parity and one block type) are numbered from the lowest **particle** level, which gets the **rank** 0, upwards $1, 2, \dots$ and downwards $-1, -2, \dots$. By the convention of `ks-theory.json` the brane zero modes are particles. So for even parity rank 0 is the zero mode, rank $n \ge 1$ is $+\sqrt{M^2 + (n\pi/L)^2}$ and rank $-n$ its negative; for odd parity rank $r \ge 0$ is $+\sqrt{M^2 + p_r^2}$ and rank $-r - 1$ its negative. Notebook 16b computes the ranks $-3$ to $5$ of both parities (Out [2]); for example the even levels of ranks 1 to 5 are $1.447972$, $2.320881$, $3.296908$, $4.306502$ and $5.330625$.

### 16.14 Inside the reference solver II: the staggered grid and the matrix

**The equations as an eigenvalue problem, line by line.** A matrix method needs the equations in the form "level times orbital equals an operator applied to the orbital".

$$
\varepsilon\,a = j\,(b' + M b).
$$

Rule: from the second equation $b' = j\varepsilon a - Mb$, multiply by $j$ and move $jMb$ over (as in Section 16.13).

$$
\varepsilon\,b = j\,(-a' + M a).
$$

Rule: from the first equation $a' = Ma - j\varepsilon b$, multiply by $-j$ ($-ja' = -jMa + \varepsilon b$, using $j^2 = 1$) and solve for $\varepsilon b$. (With a 3-momentum and a potential the record's operator is the same with $+jK + v$ added to the first line and $-jK + v$ to the second, $K = \kappa k$: `Revision/kohn_sham/reference/ks_fd.py`, its header.)

**The staggered grid.** Divide $-L \le y \le 0$ into $G$ equal **cells** of width $h = L/G$. The cell ends, the **nodes**, are $y_i = -L + i\,h$ for $i = 0, \dots, G$; the cell centres, the **half nodes**, are $y_{p+1/2} = -L + (p + \tfrac12)\,h$ for $p = 0, \dots, G - 1$. The reference stores $a$ at the half nodes and $b$ at the nodes: $u_p \approx a(y_{p+1/2})$ and $w_i \approx b(y_i)$. At the two end nodes $b$ is zero for even parity ($w_0 = 0$ at the tip and $w_G = 0$ at the brane), so they are not unknowns. The unknowns, in the order of $y$, are

$$
(u_0,\ w_1,\ u_1,\ w_2,\ \dots,\ w_{G-1},\ u_{G-1}),
$$

$G$ values of $u$ and $G - 1$ values of $w$, $2G - 1$ in all (Figure 16b.1 draws them for $G = 6$). Such a grid, on which the two components live on alternating points, is called **staggered**. On an ordinary grid, with both components at the same points and the centred difference $(f_{i+1} - f_{i-1})/(2h)$, a zigzag pattern $+1, -1, +1, \dots$ has a difference of zero and produces spurious extra levels (the **doubling** problem of naive discretisations of Dirac-type equations; the record's reference README names it as the reason for the staggering, `Revision/kohn_sham/reference/README.md`). On the staggered grid every difference connects neighbours one half cell apart, and no such pattern escapes.

**Centred differences and averages, line by line.** Let $f$ be a smooth function. Taylor's theorem (Chapter 2) gives

$$
f\big(y \pm \tfrac h2\big) = f \pm \tfrac h2\,f' + \tfrac{h^2}{8}\,f'' \pm \tfrac{h^3}{48}\,f''' + \tfrac{h^4}{384}\,f'''' \pm \dots ,
$$

Rule: $f(y + s) = f + sf' + \tfrac{s^2}{2}f'' + \tfrac{s^3}{6}f''' + \tfrac{s^4}{24}f'''' + \dots$ with $s = \pm h/2$, so $\tfrac{s^2}{2} = \tfrac{h^2}{8}$, $\tfrac{s^3}{6} = \pm\tfrac{h^3}{48}$, $\tfrac{s^4}{24} = \tfrac{h^4}{384}$.

$$
\frac{f(y + \tfrac h2) - f(y - \tfrac h2)}{h} = f' + \frac{h^2}{24}\,f''' + \dots
$$

Rule: subtract the two expansions; the even terms cancel and the odd terms double ($2\cdot\tfrac h2 = h$, $2\cdot\tfrac{h^3}{48} = \tfrac{h^3}{24}$), then divide by $h$.

$$
\frac{f(y + \tfrac h2) + f(y - \tfrac h2)}{2} = f + \frac{h^2}{8}\,f'' + \dots
$$

Rule: add the two expansions; now the odd terms cancel; divide by 2.

So the **centred difference** and the **centred average** of the two neighbours half a cell away are second-order approximations of $f'$ and $f$ at the midpoint, and their errors contain only even powers of $h$ (the next terms are $h^4$, $h^6$, ...). This is where the even-power expansion of Section 16.4 comes from.

**The rows of the matrix, line by line.** Write the first eigenvalue equation at the half node $y_{p+1/2}$, the place where $u_p$ lives; its neighbours of $b$ are $w_p$ and $w_{p+1}$:

$$
\varepsilon\,u_p = j\Big(\frac{w_{p+1} - w_p}{h} + M\,\frac{w_p + w_{p+1}}{2}\Big) = j\Big(-\frac1h + \frac M2\Big)\,w_p + j\Big(\frac1h + \frac M2\Big)\,w_{p+1}.
$$

Rule: replace $b'$ by the centred difference and $b$ by the centred average, then collect the coefficients of $w_p$ and $w_{p+1}$. Write the second equation at the node $y_i$, where $w_i$ lives; its neighbours of $a$ are $u_{i-1}$ and $u_i$:

$$
\varepsilon\,w_i = j\Big(-\frac{u_i - u_{i-1}}{h} + M\,\frac{u_{i-1} + u_i}{2}\Big) = j\Big(\frac1h + \frac M2\Big)\,u_{i-1} + j\Big(-\frac1h + \frac M2\Big)\,u_i .
$$

Rule: the same replacements for $a'$ and $a$, then collect.

**The matrix is tridiagonal and symmetric.** In the order of the unknowns each row couples only to its two neighbours in the list (a $u$ to the $w$ on either side, a $w$ to the $u$ on either side), so the matrix $T$ of the problem $T z = \varepsilon z$ is **tridiagonal**; at $k = 0$ its diagonal is zero. It is also **symmetric** ($T_{rc} = T_{cr}$): the coefficient of $w_{p+1}$ in the row of $u_p$ is $j(\tfrac1h + \tfrac M2)$, and the coefficient of $u_p$ in the row of $w_{p+1}$ (put $i = p + 1$, so $u_{i-1} = u_p$) is the same number; likewise the coefficient of $w_p$ in the row of $u_p$ and of $u_p$ in the row of $w_p$ (put $i = p$) are both $j(-\tfrac1h + \tfrac M2)$. So the entry between the neighbours number $r$ and $r + 1$ of the list is

$$
T_{r,r+1} = T_{r+1,r} = \begin{cases} j\,(\tfrac1h + \tfrac M2) & r \text{ even (a } u \text{ followed by a } w), \\ j\,(-\tfrac1h + \tfrac M2) & r \text{ odd (a } w \text{ followed by a } u). \end{cases}
$$

For $G = 4$ ($h = 0.75$) and $M = 1$ the two values are $1.8333$ and $-0.8333$ (Notebook 16b, Out [4] prints the whole $7\times7$ matrix). Symmetry matters: a real symmetric matrix has only real eigenvalues and an orthonormal set of eigenvectors (the **spectral theorem**, quoted from linear algebra), as the levels of a self-adjoint problem must; and the counting method of Section 16.15 works only for symmetric matrices.

**Odd parity: the rotated frame.** For odd parity the brane condition is $a(0) = 0$, but $a$ lives at half nodes, so no unknown sits at $y = 0$ to be set to zero. The reference rotates the two components before it discretises, so that both conditions become "$b$-type component zero at the ends" again. With the Pauli matrices $\sigma_1 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\sigma_2 = \begin{pmatrix}0&-i\\i&0\end{pmatrix}$, $\sigma_3 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$ and the complex orbital $\chi = (a, ib)$ of Chapter 14, write $\chi = R\,\psi$ with $\psi = (u, iw)$ and $R = e^{i\phi\sigma_1}$ for an angle $\phi(y)$.

$$
R = e^{i\phi\sigma_1} = \cos\phi + i\sin\phi\,\sigma_1 .
$$

Rule: the series $e^{X} = 1 + X + X^2/2 + \dots$ with $X = i\phi\sigma_1$ and $\sigma_1^2 = 1$ splits into the even terms, the series of $\cos\phi$, and the odd terms, $i\sigma_1$ times the series of $\sin\phi$.

$$
\begin{pmatrix} a \\ ib \end{pmatrix} = \begin{pmatrix} \cos\phi\,u + i\sin\phi\cdot iw \\ \cos\phi\cdot iw + i\sin\phi\,u \end{pmatrix} = \begin{pmatrix} \cos\phi\,u - \sin\phi\,w \\ i\,(\sin\phi\,u + \cos\phi\,w) \end{pmatrix}.
$$

Rule: $\sigma_1$ exchanges the two components of $(u, iw)$, and $i\cdot i = -1$. So $a = \cos\phi\,u - \sin\phi\,w$ and $b = \sin\phi\,u + \cos\phi\,w$. The reference chooses $\phi = j\,\tfrac{\pi}{2}\,\tfrac{y + L}{L}$: at the tip $\phi = 0$, so $b = w$ and $b(-L) = 0$ means $w(-L) = 0$; at the brane $\phi = j\pi/2$, so $\cos\phi = 0$, $\sin\phi = j$, $a = -j\,w$, and $a(0) = 0$ means $w(0) = 0$. Both conditions are again "$w = 0$ at the ends", and the same staggered grid works.

**The rotated operator, line by line.** The operator of Section 16.3 is $h_j = j[-i\sigma_1\tfrac{d}{dy} + M\sigma_2 + K\sigma_3] + v$, and $h_j\chi = \varepsilon\chi$ becomes $R^{-1}h_jR\,\psi = \varepsilon\psi$, with $R^{-1} = \cos\phi - i\sin\phi\,\sigma_1$.

$$
R^{-1}\Big(-i\sigma_1\frac{d}{dy}\Big)(R\psi) = -i\sigma_1\big(\psi' + R^{-1}R'\,\psi\big) = -i\sigma_1\psi' - i\sigma_1\cdot i\phi'\sigma_1\,\psi = -i\sigma_1\psi' + \phi'\,\psi .
$$

Rule: the product rule $(R\psi)' = R'\psi + R\psi'$; $\sigma_1$ commutes with $R$; $R^{-1}R' = i\phi'\sigma_1$ (differentiate $e^{i\phi\sigma_1}$); and $-i\cdot i\cdot\sigma_1^2 = 1$. The derivative of the rotation adds the plain number $\phi'$.

$$
R^{-1}\sigma_2R = (\cos\phi - i\sin\phi\,\sigma_1)(\cos\phi\,\sigma_2 + \sin\phi\,\sigma_3) = \cos 2\phi\,\sigma_2 + \sin 2\phi\,\sigma_3 .
$$

Rule: first $\sigma_2R = \cos\phi\,\sigma_2 + i\sin\phi\,\sigma_2\sigma_1 = \cos\phi\,\sigma_2 + \sin\phi\,\sigma_3$ (because $\sigma_2\sigma_1 = -i\sigma_3$); then multiply out with $\sigma_1\sigma_2 = i\sigma_3$, $\sigma_1\sigma_3 = -i\sigma_2$, and use $\cos^2\phi - \sin^2\phi = \cos2\phi$, $2\sin\phi\cos\phi = \sin2\phi$. In the same way $R^{-1}\sigma_3R = \cos2\phi\,\sigma_3 - \sin2\phi\,\sigma_2$ (Notebook 16b checks both with sympy, In [9]).

$$
R^{-1}(M\sigma_2 + K\sigma_3)R = \big(M\cos2\phi - K\sin2\phi\big)\,\sigma_2 + \big(M\sin2\phi + K\cos2\phi\big)\,\sigma_3 = m_2\,\sigma_2 + k_2\,\sigma_3 .
$$

Rule: insert the two rotated matrices and collect the coefficients of $\sigma_2$ and $\sigma_3$. So the rotated operator has the same form, $j[-i\sigma_1\tfrac{d}{dy} + \phi' + m_2\sigma_2 + k_2\sigma_3] + v$, with the new mass $m_2$ and momentum term $k_2$. In the matrix, $j(\phi' + k_2) + v$ stands on the diagonal of the $u$ rows and $j(\phi' - k_2) + v$ on the diagonal of the $w$ rows ($\sigma_3$ is $+1$ on the first component and $-1$ on the second), and $M$ in the neighbour entries is replaced by $m_2$, taken at the half node of the pair so that the matrix stays symmetric. For even parity $\phi = 0$, and everything reduces to the matrix above, with $\pm jK + v$ on the diagonal. The reference chooses the angle $j\phi$ for block type $j$ so that the exact symmetry between the two block types at $k = 0$ survives on the grid: their levels agree exactly, to $0$ in the record (`Revision/kohn_sham/reports/ks-reference.json`, check free_k0_block_type_symmetry).

### 16.15 Inside the reference solver III: counting eigenvalues, the zero mode and the brane band

**The pivots, line by line.** How does one find eigenvalue number $i$ of a matrix with thousands of rows without computing all of them? By counting. Let $T$ be tridiagonal with diagonal $d_1, \dots, d_n$ and neighbour entries $o_1, \dots, o_{n-1}$, and let $x$ be a trial number. Write $T - x\,\mathbb{1}$ (where $\mathbb{1}$ is the unit matrix) as a product $L D L^T$, with $L$ having ones on its diagonal and one band below it, and $D$ diagonal with entries $q_1, \dots, q_n$, the **pivots**. For two rows:

$$
\begin{pmatrix} d_1 - x & o_1 \\ o_1 & d_2 - x \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ \ell & 1 \end{pmatrix}\begin{pmatrix} q_1 & 0 \\ 0 & q_2 \end{pmatrix}\begin{pmatrix} 1 & \ell \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} q_1 & \ell q_1 \\ \ell q_1 & \ell^2 q_1 + q_2 \end{pmatrix}.
$$

Rule: multiply the three matrices (row times column).

$$
q_1 = d_1 - x, \qquad \ell = \frac{o_1}{q_1}, \qquad q_2 = d_2 - x - \ell^2 q_1 = d_2 - x - \frac{o_1^2}{q_1}.
$$

Rule: compare the entries of the two sides, first the top left, then the off-diagonal, then the bottom right. The same comparison, row after row, gives for every $n$

$$
q_1 = d_1 - x, \qquad q_r = d_r - x - \frac{o_{r-1}^2}{q_{r-1}} \quad (r = 2, \dots, n).
$$

Rule: each new row of $L D L^T$ involves only the previous pivot, because $T$ has only one band on each side of the diagonal.

**Sylvester's law of inertia and the Sturm count.** A theorem of linear algebra that we quote without proof, **Sylvester's law of inertia**, says: if $A = L D L^T$ with an invertible $L$, then $A$ and $D$ have the same number of negative eigenvalues. The eigenvalues of $D$ are its diagonal entries, the pivots, and the eigenvalues of $T - x\,\mathbb{1}$ are $\varepsilon - x$ for the eigenvalues $\varepsilon$ of $T$. Hence

$$
c(x) = \text{(number of negative pivots)} = \text{(number of eigenvalues of } T \text{ below } x).
$$

Rule: $\varepsilon - x < 0$ exactly when $\varepsilon < x$. The function $c(x)$ is the **Sturm count**; it jumps by one at every eigenvalue (Figure 16b.2 draws it as a staircase). If a pivot happens to be exactly zero, the next one would divide by zero; the reference then replaces it by the tiny negative number $-10^{-290}$, which is the same as moving $x$ by a tiny amount. A worked example with three rows is Exercise 4 of Section 16.27.

**Bisection.** To find eigenvalue number $i$ (counting from 0 at the lowest), start with an interval $[lo, hi]$ that contains every eigenvalue. Take the midpoint $mid$. If $c(mid) \le i$, at most $i$ eigenvalues lie below $mid$, so eigenvalue number $i$ lies at or above it: replace $lo$ by $mid$; otherwise replace $hi$ by $mid$. Each step halves the interval and keeps the eigenvalue inside, so no eigenvalue can be missed or counted twice. After $n$ steps an interval of width $W$ has shrunk to $W/2^n$; to reach a width $\tau$ one needs $n \ge \log_2(W/\tau)$ steps.

**The starting interval: Gershgorin's bound, line by line.** Let $Tz = \varepsilon z$ with $z \ne 0$, and let $r$ be the row in which $|z_r|$ is largest.

$$
(\varepsilon - T_{rr})\,z_r = \sum_{c \ne r} T_{rc}\,z_c .
$$

Rule: row $r$ of $Tz = \varepsilon z$, with the diagonal term moved to the left.

$$
|\varepsilon - T_{rr}|\,|z_r| \le \sum_{c \ne r} |T_{rc}|\,|z_c| \le \Big(\sum_{c \ne r} |T_{rc}|\Big)\,|z_r| .
$$

Rule: the triangle inequality, then $|z_c| \le |z_r|$ for every $c$.

$$
|\varepsilon - T_{rr}| \le \rho_r = \sum_{c \ne r} |T_{rc}| .
$$

Rule: divide by $|z_r| > 0$. So every eigenvalue lies within the **radius** $\rho_r$ of some diagonal entry (Gershgorin's theorem), and the interval from $\min(d - \rho) - 1$ to $\max(d + \rho) + 1$ contains them all. For $G = 150$ ($h = 0.02$) the neighbour entries are $50.5$ and $-49.5$, every inner radius is $100$, and the interval is $[-101, 101]$, of width $W = 202$. The notebook stops when the width is below $10^{-14}\max(1, |lo|)$, so for a level near zero $\tau = 10^{-14}$ and $n \ge \log_2(202/10^{-14}) = 54.2$: 55 halvings, the number Notebook 16b prints (Out [5]).

**The exact discrete zero mode, line by line.** At $k = 0$ the grid problem keeps an eigenvalue that is exactly zero. Put $\varepsilon = 0$ and all $w_i = 0$. The rows of the $u$ then read $0 = 0$. The row of $w_i$ demands

$$
\Big(\frac1h + \frac M2\Big)\,u_{i-1} + \Big(-\frac1h + \frac M2\Big)\,u_i = 0 \quad\Longrightarrow\quad u_i = q\,u_{i-1}, \qquad q = \frac{1 + Mh/2}{1 - Mh/2}.
$$

Rule: multiply by $h$ and solve for $u_i$. Hence $u_p = q^p\,u_0$: a discrete exponential, with $b = 0$ exactly, as in the continuum. How close is it to $e^{My}$?

$$
\ln q = \ln\big(1 + \tfrac{Mh}{2}\big) - \ln\big(1 - \tfrac{Mh}{2}\big) = 2\Big(\tfrac{Mh}{2} + \tfrac13\big(\tfrac{Mh}{2}\big)^3 + \dots\Big) = Mh + \frac{(Mh)^3}{12} + \dots
$$

Rule: the series $\ln(1 + t) = t - \tfrac{t^2}{2} + \tfrac{t^3}{3} - \dots$ with $t = \pm Mh/2$; in the difference the even powers cancel and the odd powers double. So $q^p = e^{p\ln q} = e^{Mph\,(1 + (Mh)^2/12 + \dots)}$: the exponent is $M$ times the distance $ph$ from the first half node, up to a relative error $(Mh)^2/12$, an error of order $h^2$. For $G = 150$ the grid values lie within $6.9\times10^{-5}$ of $A\,e^{My}$ (Notebook 16b, Out [7]). In the record the zero mode's eigenvalue is at most $1.3\times10^{-39}$ and the extrapolated profile agrees with $A\,e^{My}$ to $4.0\times10^{-15}$ (`Revision/kohn_sham/reports/ks-reference.json`, check free_zero_mode).

**The slope of the brane band: Hellmann-Feynman, line by line.** Now switch on a small 3-momentum $k$. The zero mode moves away from zero and becomes the lowest level of the **brane band**, $\varepsilon \approx c\,k$ for small $k$ (Chapter 15). Its slope $c = d\varepsilon/dk$ at $k = 0$ follows from a general fact about symmetric matrices. Let $T(k)z(k) = \varepsilon(k)z(k)$ with $z^Tz = 1$, and write a prime for $d/dk$.

$$
T'z + Tz' = \varepsilon'z + \varepsilon z' .
$$

Rule: differentiate both sides with the product rule.

$$
z^TT'z + z^TTz' = \varepsilon'\,z^Tz + \varepsilon\,z^Tz' .
$$

Rule: multiply from the left by the row $z^T$.

$$
z^TT'z + \varepsilon\,z^Tz' = \varepsilon' + \varepsilon\,z^Tz' \quad\Longrightarrow\quad \varepsilon' = z^T\,T'\,z .
$$

Rule: $z^TT = (T^Tz)^T = (Tz)^T = \varepsilon z^T$ because $T$ is symmetric, and $z^Tz = 1$; then cancel $\varepsilon z^Tz'$. This is the **Hellmann-Feynman theorem** for matrices: the derivative of a level is the expectation value of the derivative of the matrix. For even parity and $j = +1$ the momentum enters only the diagonal, $+\kappa(y)k$ in the $u$ rows and $-\kappa(y)k$ in the $w$ rows, so $T'$ is diagonal with $\pm\kappa$. The zero mode has $w = 0$, and its normalised vector holds $u_p\sqrt h$, so

$$
c = \sum_p \kappa\big(y_{p+1/2}\big)\,u_p^2\,h \ \longrightarrow\ \int_{-L}^{0}\kappa\,a^2\,dy \quad (h \to 0).
$$

Rule: only the $u$ entries contribute; the sum is the midpoint rule for the integral. In the continuum, with $a = A\,e^{My}$ and $\kappa = e^{-Hy - a_{4,0}}$:

$$
c = e^{-a_{4,0}}A^2\int_{-L}^{0}e^{(2M - H)y}\,dy = e^{-a_{4,0}}\,\frac{2M}{1 - e^{-2ML}}\,\frac{1 - e^{-(2M - H)L}}{2M - H}.
$$

Rule: $\kappa a^2 = e^{-a_{4,0}}A^2e^{-Hy}e^{2My}$; integrate the exponential as for the normalisation; insert $A^2$ from Section 16.13. This is the formula checksNumeric.braneBandSlopeFormula of `Revision/kohn_sham/ks-theory.json` (PROVED: check brane_band_slope of `Revision/kohn_sham/reports/ks-theory-python.json`). For $M = H = 1$, $L = 3$:

$$
c(0) = \frac{2\,(1 - e^{-3})}{1 - e^{-6}} = \frac{2\cdot0.950213}{0.997521} = 1.905148 .
$$

Rule: insert the numbers; $e^{-3} = 0.049787$ and $e^{-6} = 0.002479$.

**The meaning of the factor $e^{-a_{4,0}}$.** The weight $\kappa = e^{-Hy - a_{4,0}}$ is one over the 3-space scale factor $e^{a_4}\sin^{1/6}z = e^{a_4 + Hy}$ (because $\sin z = e^{6Hy}$, so $\sin^{1/6}z = e^{Hy}$). Along the history $a_4 = AHx_4$ the 3-space scale factor grows while the three extra times deflate with $e^{-a_4}$ (the 7-volume stays constant), and the energy carried by a 3-momentum is redshifted by $e^{-a_{4,0}}$: the brane band flattens. From slice to slice ($\Delta a_{4,0} = 0.5$) the slope shrinks by the factor $e^{-0.5} = 0.6065$: $1.905148$, $1.155531$, $0.700865$, $0.425096$, $0.257834$. The reference's grid reproduces the formula to $2.6\times10^{-15}$, relative (`Revision/kohn_sham/reports/ks-reference.json`, check free_brane_band_slope).

### 16.16 Example: the reference method by hand (Notebook 16b)

Notebook 16b opens the reference solver and rebuilds its method by hand on the free problem of Section 16.13, where every answer is known: it derives the exact levels and checks them with sympy, draws the staggered grid, builds the matrix and checks it entry by entry against the reference's own function, finds eigenvalues with Sturm counts and bisection, constructs the exact discrete zero mode, treats the odd parity in the rotated frame, measures the convergence on five grids and the effect of one and two Richardson steps, computes the slope of the brane band at the five slices of the history, and finally runs the reference program's own free-field job and checks its six free-field criteria. It needs no Rust, runs in less than a minute, draws seven figures and ends with the line ALL 31 CHECKS PASSED (notebook 16b).

<!-- NOTEBOOK 16b -->

### 16.19 Line-by-line walk-through of Notebook 16b

The notebook has 17 code cells, In [1] to In [17]; the numbers they print are in Section 16.18.

**In [1], the set-up cell.** It is the set-up cell of Notebook 16a, explained line by line in Section 16.12, without the two imports `shutil` and `subprocess` and without the function `rust_program`, because this notebook runs no Rust program. Its comment lines repeat the run instructions of Section 16.17, and its only other difference is the name:

```python
NOTEBOOK_ID = "16b"  # this notebook: chapter 16, example b
```

**In [2], the exact levels.**

```python
import math  # functions of single numbers (sqrt, sin, pi, ...)
import sys  # the list of folders in which Python looks for modules

import numpy as np  # arrays of numbers
import sympy as sp  # exact symbolic algebra

PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
M_VALUE, L_VALUE = 1.0, 3.0  # the mass M = m = 1 and the tip cutoff L = 3
```

`math` holds functions of single numbers ($\sqrt{\ }$, $\sin$, $\pi$, ...), `sys` the list of module folders, `numpy` arrays, and `sympy`, called `sp`, exact symbolic algebra: it computes with letters and formulas instead of numbers. `PALETTE` is the list of figure colours of Notebook 16a. The last line gives two names at once: `M_VALUE` is the mass $M = m = 1$ and `L_VALUE` the tip cutoff $L = 3$.

```python
y, p, eps = sp.symbols("y p epsilon", real=True)  # real symbols
M, L = sp.symbols("M L", positive=True)  # M > 0 and L > 0 (needed by the integral)
for j_value in (1, -1):
    j = sp.Integer(j_value)
    b = sp.sin(p * (y + L))  # the even and odd solution for b
    a = j * (sp.diff(b, y) + M * b) / eps  # a from the second equation
    on_shell = {eps: sp.sqrt(M ** 2 + p ** 2)}  # epsilon^2 = M^2 + p^2
    first = sp.diff(a, y) - (M * a - j * eps * b)  # a' - (M a - j eps b)
    second = sp.diff(b, y) - (j * eps * a - M * b)  # b' - (j eps a - M b)
    residuals = [sp.simplify(r.subs(on_shell)) for r in (first, second)]
    check(residuals == [0, 0],
          f"sympy: b = sin(p(y+L)), a = j(b' + M b)/eps solve both equations (j = "
          f"{j_value}) when eps^2 = M^2 + p^2")
```

`sp.symbols` creates the symbols $y$, $p$, $\varepsilon$ (declared real) and $M$, $L$ (declared positive; the integral below needs $M > 0$). For both block types ($j = 1$ and $j = -1$, made an exact sympy integer by `sp.Integer`) the cell writes the solution of Section 16.13: $b = \sin(p(y + L))$ and $a = j(b' + Mb)/\varepsilon$ (`sp.diff(b, y)` is the derivative $b'$). `on_shell` is a dictionary that replaces $\varepsilon$ by $\sqrt{M^2 + p^2}$. `first` and `second` are the two equations written as "left side minus right side", which must be zero for a solution; `.subs(on_shell)` inserts $\varepsilon$, and `sp.simplify` brings each to its simplest form. The check requires both to be exactly 0: the formulas of Section 16.13 solve both equations whenever $\varepsilon^2 = M^2 + p^2$, for both block types (Out [2], two PASS lines).

```python
zero_a = sp.exp(M * y)  # the zero mode a = e^{My}, b = 0
check(sp.simplify(sp.diff(zero_a, y) - M * zero_a) == 0,
      "sympy: a = e^(My), b = 0 solves the equations with eps = 0")
norm = sp.integrate(zero_a ** 2, (y, -L, 0))  # int_{-L}^0 e^{2My} dy
check(sp.simplify(norm - (1 - sp.exp(-2 * M * L)) / (2 * M)) == 0,
      "sympy: int e^(2My) dy over -L..0 equals (1 - e^(-2ML))/(2M)")
```

The zero mode: $a = e^{My}$ must satisfy $a' - Ma = 0$, which sympy confirms, and `sp.integrate` computes $\int_{-L}^{0}e^{2My}\,dy$ symbolically, which must equal $(1 - e^{-2ML})/(2M)$, the normalisation integral of Section 16.13.

```python
def odd_root(l, M=M_VALUE, L=L_VALUE):
    """The root p_l of p cos(pL) + M sin(pL) = 0 in ((l + 1/2) pi/L, (l + 1) pi/L),
    by bisection (200 halvings: far below the rounding of a double)."""
    lo, hi = (l + 0.5) * math.pi / L, (l + 1) * math.pi / L
    f = lambda q: M * math.sin(q * L) + q * math.cos(q * L)
    f_lo = f(lo)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if (f(mid) > 0) == (f_lo > 0):  # same sign as at lo: the root is above mid
            lo, f_lo = mid, f(mid)
        else:
            hi = mid
    return 0.5 * (lo + hi)
```

`odd_root(l)` finds the root $p_l$ of $F(p) = M\sin(pL) + p\cos(pL)$ in the interval $((l + \tfrac12)\pi/L, (l + 1)\pi/L)$, which Section 16.13 proved to contain exactly one root, by bisection: `f` is $F$ written as a **lambda** (a one-line function); `f_lo` is its value at the left end; each of the 200 steps takes the midpoint and keeps the half in which $F$ changes sign (if $F(mid)$ has the sign of $F(lo)$, the root lies above $mid$). Two hundred halvings shrink the interval far below the spacing of the computer's numbers, so the result is the root to the last digit.

```python
RANKS = np.arange(-3, 6)  # the ranks -3, ..., 5 of the record
P_ODD = [odd_root(l) for l in range(12)]
EXACT_EVEN = np.array([0.0 if r == 0 else
                       math.copysign(math.sqrt(M_VALUE ** 2
                                               + (abs(r) * math.pi / L_VALUE) ** 2),
                                     r) for r in RANKS])
EXACT_ODD = np.array([math.sqrt(M_VALUE ** 2 + P_ODD[r] ** 2) if r >= 0 else
                      -math.sqrt(M_VALUE ** 2 + P_ODD[-r - 1] ** 2) for r in RANKS])
print("rank    even level      odd level")
for r, e, o in zip(RANKS, EXACT_EVEN, EXACT_ODD):
    print(f"{r:4d}  {e:+.12f}  {o:+.12f}")
check(all(abs(math.tan(q * L_VALUE) + q / M_VALUE) < 1e-9 for q in P_ODD),
      "the twelve odd roots satisfy tan(pL) = -p/M")
```

`RANKS` is the array of the ranks $-3$ to $5$, `P_ODD` the first twelve odd roots. `EXACT_EVEN` holds the even levels by rank: 0 for rank 0, and $\sqrt{M^2 + (|r|\pi/L)^2}$ with the sign of the rank (`math.copysign(x, r)` gives $x$ the sign of $r$). `EXACT_ODD` holds the odd levels: $+\sqrt{M^2 + p_r^2}$ for $r \ge 0$ and $-\sqrt{M^2 + p_{-r-1}^2}$ for negative ranks (rank $-1$ belongs to $p_0$). The table of Out [2] prints both with twelve decimals and a sign (`:+.12f`); for example the even level of rank 1 is $+1.447971930402$ and the odd level of rank 0 is $+1.292292828069$. The check confirms that every odd root satisfies $\tan(pL) = -p/M$ to $10^{-9}$.

**In [3], the staggered grid as a picture (Figure 16b.1).**

```python
G_SHOW = 6
h_show = L_VALUE / G_SHOW
nodes = -L_VALUE + h_show * np.arange(G_SHOW + 1)  # y_0, ..., y_G
halves = -L_VALUE + h_show * (np.arange(G_SHOW) + 0.5)  # y_{1/2}, ..., y_{G-1/2}
fig, ax = plt.subplots(figsize=(9.0, 3.0))
ax.axhline(0.0, color="k", lw=1.0)
ax.plot(halves, np.zeros(G_SHOW), "o", color=PALETTE[0], ms=10,
        label="$u_p \\approx a(y_{p+1/2})$ (half nodes)")
ax.plot(nodes[1:-1], np.zeros(G_SHOW - 1), "s", color=PALETTE[1], ms=9,
        label="$w_i \\approx b(y_i)$ (inner nodes)")
ax.plot(nodes[[0, -1]], [0.0, 0.0], "s", color=PALETTE[1], ms=9, mfc="white",
        label="$w_0 = w_G = 0$ (tip and brane, even parity)")
```

For $G = 6$ cells, `h_show` is the cell width $0.5$, `nodes` the seven cell ends $y_0, \dots, y_6$ and `halves` the six cell centres (`np.arange(n)` is the array $0, 1, \dots, n - 1$, and adding $0.5$ moves to the centres). A wide, low figure is made; `axhline` draws the $y$ axis as a horizontal line. The half nodes are drawn as blue circles (the values $u_p$), the inner nodes as orange squares (`nodes[1:-1]` leaves out the first and the last; the values $w_i$), and the two end nodes as open squares (`mfc="white"`), because there $b = 0$ is known and is not an unknown. Each label explains its marker.

```python
for p_index, yp in enumerate(halves):
    ax.annotate(f"$u_{p_index}$", (yp, 0.0), (yp, 0.25), ha="center", fontsize=9)
for i_index, yi in enumerate(nodes):
    ax.annotate(f"$w_{i_index}$", (yi, 0.0), (yi, -0.35), ha="center", fontsize=9)
ax.annotate("tip $y = -L$", (nodes[0], 0.0), (nodes[0], 0.55), ha="center")
ax.annotate("brane $y = 0$", (nodes[-1], 0.0), (nodes[-1], 0.55), ha="center")
ax.annotate("", (nodes[1], -0.75), (nodes[0], -0.75),
            arrowprops={"arrowstyle": "<->"})
ax.text(0.5 * (nodes[0] + nodes[1]), -0.95, "$h = L/G$", ha="center")
ax.set_ylim(-1.2, 0.9)
ax.set_xlim(-L_VALUE - 0.3, 0.3)
ax.set_yticks([])
ax.set_xlabel("hidden coordinate $y$")
ax.legend(fontsize=8, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3)
```

`annotate(text, point, text_position)` writes a text near a point: the names $u_0, \dots, u_5$ above the circles and $w_0, \dots, w_6$ below the nodes, and the words tip and brane above the two ends. An empty annotation with `arrowprops` draws a double arrow over the first cell, labelled $h = L/G$. The axes are set (no ticks on the vertical axis, `set_yticks([])`) and the legend is placed above the plot (`bbox_to_anchor` gives its position relative to the axes, `ncol=3` makes three columns).

```python
save_figure(fig, "staggered_grid",
            "The staggered grid of the reference solver for $G = 6$ cells of width "
            "$h = L/G = 0.5$ on the hidden coordinate $-3 \\le y \\le 0$: the first "
            "orbital component $a$ is stored at the cell centres (circles, $u_p$), "
            "the second component $b$ at the inner cell ends (squares, $w_i$); at the "
            "tip and at the brane $b$ is zero (open squares) and is not an unknown. "
            "The $2G - 1 = 11$ unknowns alternate $u_0, w_1, u_1, \\dots, u_5$.")
```

`save_figure` saves Figure 16b.1. What the student should see: along the hidden coordinate from the tip at $-3$ to the brane at $0$, circles and squares alternate; the $2G - 1 = 11$ unknowns are, in order, $u_0, w_1, u_1, \dots, w_5, u_5$; every circle has a square on each side, so every difference of Section 16.14 connects neighbours half a cell apart.

**In [4], from the differential equation to a matrix.**

```python
sys.dont_write_bytecode = True  # do not write a __pycache__ folder into the record
sys.path.insert(0, str(repository_file("Revision/kohn_sham/reference")))
import ks_fd as K  # noqa: E402  the reference solver's module (Revision code)
```

As in Notebook 16a (Section 16.12, In [3]): no translated files are written into the record, the reference folder is added to the module search list, and the reference solver's module `ks_fd.py` is imported under the name `K`.

```python
def even_matrix(G, j=1.0, M=M_VALUE, L=L_VALUE):
    """Diagonal d (2G - 1 numbers) and off-diagonal o (2G - 2 numbers) of T for
    even parity, k = 0, constant M."""
    h = L / G
    d = np.zeros(2 * G - 1)  # the diagonal is zero at k = 0
    r = np.arange(2 * G - 2)  # the number of the first of two neighbours
    o = np.where(r % 2 == 0, j * (1.0 / h + M / 2.0), j * (-1.0 / h + M / 2.0))
    return d, o
```

`even_matrix(G)` builds the tridiagonal matrix of Section 16.14 for even parity, $k = 0$ and constant $M$ in its compact form: the diagonal `d` ($2G - 1$ zeros, `np.zeros`) and the neighbour entries `o` ($2G - 2$ numbers). `r` numbers the pairs of neighbours; `r % 2` is the remainder of $r$ divided by 2, so `r % 2 == 0` is true for even $r$, and `np.where(condition, x, y)` takes $j(\tfrac1h + \tfrac M2)$ where it is true and $j(-\tfrac1h + \tfrac M2)$ where it is false: exactly the entries $T_{r,r+1}$ derived in Section 16.14.

```python
d4, o4 = even_matrix(4)
T4 = np.diag(d4) + np.diag(o4, 1) + np.diag(o4, -1)  # the full 7 x 7 matrix
print("T for G = 4 (h = 0.75), even parity, j = +1:")
for row in T4:
    print("  " + " ".join(f"{x:+7.3f}" for x in row))
```

For $G = 4$ the full matrix is assembled: `np.diag(d4)` puts the diagonal into a square matrix, and `np.diag(o4, 1)` and `np.diag(o4, -1)` put the neighbour entries one place above and one place below it. The loop prints the $7\times7$ matrix row by row, each entry with sign and three decimals in seven places (`:+7.3f`); Out [4] shows the alternating entries $+1.833$ and $-0.833$ next to the zero diagonal.

```python
for G in (4, 300):
    d, o = even_matrix(G)
    phys = K.Phys(m=M_VALUE, L=L_VALUE, H=1.0)  # the reference's parameters
    grid = K.Grid(phys, G)
    sector = K.Sectors([(0, 1, 1, 0)])  # (n2 = 0, r3 = 1, j = +1, even)
    alpha, beta = K.sector_arrays(grid, phys, sector, np.full(grid.n, M_VALUE),
                                  np.zeros(grid.n))
    check(np.array_equal(alpha[:, 0], d) and np.array_equal(beta[:, 0], o),
          f"G = {G}: our matrix equals the reference's (ks_fd.sector_arrays), "
          "entry by entry")
check(np.array_equal(T4, T4.T), "the matrix is symmetric")
```

For $G = 4$ and $G = 300$ the cell builds the same matrix with the reference's own function: `K.Phys` holds the reference's parameters ($m = 1$, $L = 3$, $H = 1$), `K.Grid` its grid, and `K.Sectors` a list of sectors, here one, $(n_2 = 0, r_3 = 1, j = +1, \text{even})$. `K.sector_arrays` returns the diagonals `alpha` and the neighbour entries `beta` of every sector's matrix (one column per sector), for the effective mass $M = 1$ at every position (`np.full(n, value)` is an array of $n$ equal values) and the potential $v = 0$. The check requires our arrays to be **exactly** equal to the reference's (`np.array_equal`), entry by entry; the last check confirms that the $7\times7$ matrix equals its transpose `T4.T` (rows and columns exchanged), that is, that it is symmetric.

**In [5], eigenvalues by counting: the Sturm count and bisection.**

```python
def sturm_count(d, o, x):
    """Number of eigenvalues below x of the tridiagonal matrix (d, o), for every
    entry of the array x."""
    x = np.asarray(x, dtype=float)
    o2 = o * o
    q = d[0] - x  # the first pivot
    q = np.where(np.abs(q) < 1e-290, -1e-290, q)  # never divide by an exact zero
    count = (q < 0).astype(int)
    for r in range(1, len(d)):
        q = d[r] - x - o2[r - 1] / q  # the next pivot
        q = np.where(np.abs(q) < 1e-290, -1e-290, q)
        count += q < 0
    return count
```

`sturm_count(d, o, x)` is the pivot recursion of Section 16.15 for every entry of the array `x` at once. `np.asarray(x, dtype=float)` makes sure `x` is an array of numbers, and `o2` holds the squares $o_r^2$. `q` starts as the first pivot $d_1 - x$; `np.where` replaces a pivot whose size is below $10^{-290}$ by $-10^{-290}$ (never divide by an exact zero); `count` starts as 1 where the pivot is negative and 0 elsewhere (`.astype(int)` turns truth values into the numbers 1 and 0). The loop computes each next pivot $q_r = d_r - x - o_{r-1}^2/q_{r-1}$ and adds 1 to the count wherever it is negative (`count += q < 0` adds the truth values as numbers). The returned count is the number of eigenvalues below each $x$.

```python
def bisection(d, o, index, rel_tol=1e-14):
    """Eigenvalues number index (an array of integers, 0 = the lowest) of (d, o)."""
    index = np.asarray(index)
    radius = np.zeros_like(d)
    radius[:-1] += np.abs(o)
    radius[1:] += np.abs(o)
    lo = np.full(len(index), np.min(d - radius) - 1.0)  # Gershgorin: below all
    hi = np.full(len(index), np.max(d + radius) + 1.0)  # Gershgorin: above all
    steps = 0
    while np.any(hi - lo > rel_tol * np.maximum(1.0, np.abs(lo))):
        mid = 0.5 * (lo + hi)
        above = sturm_count(d, o, mid) <= index  # True: the eigenvalue is above mid
        lo = np.where(above, mid, lo)
        hi = np.where(above, hi, mid)
        steps += 1
    return 0.5 * (lo + hi), steps
```

`bisection(d, o, index)` finds the eigenvalues with the numbers in the array `index` (0 is the lowest), all at once. `radius` is Gershgorin's radius of every row: each row gets the size of the neighbour entry on its right (`radius[:-1] += ...`, all rows but the last) and on its left (`radius[1:] += ...`, all rows but the first). `lo` and `hi` start one unit beyond Gershgorin's bounds, so every eigenvalue lies inside (Section 16.15). The `while` loop runs as long as some interval is wider than $10^{-14}\max(1, |lo|)$ (`np.any` is true if any entry is true). In each step `above` is true where at most `index` eigenvalues lie below the midpoint, that is, where the wanted eigenvalue lies at or above it; there `lo` moves up to the midpoint, elsewhere `hi` moves down. `steps` counts the halvings. The function returns the midpoints of the final intervals and the number of steps.

```python
d150, o150 = even_matrix(150)
T150 = np.diag(d150) + np.diag(o150, 1) + np.diag(o150, -1)
all_eigs = np.linalg.eigvalsh(T150)  # every eigenvalue, sorted
test_x = np.linspace(-6.0, 6.0, 241) + 0.0123  # 241 test points, none at a level
counts_ok = np.array_equal(sturm_count(d150, o150, test_x),
                           np.searchsorted(all_eigs, test_x))
first_particle = int(sturm_count(d150, o150, np.array([-1e-9]))[0])
found, steps = bisection(d150, o150, first_particle + RANKS)
```

For $G = 150$ the full matrix `T150` ($299\times299$) is assembled, and `np.linalg.eigvalsh` computes all its eigenvalues with a standard routine for symmetric matrices, sorted. `test_x` holds 241 trial values between $-6$ and $6$, shifted by $0.0123$ so that none falls on a level. `counts_ok` compares our Sturm counts with the number of eigenvalues below each trial value found by `np.searchsorted` (it tells where each `x` would be inserted into the sorted list, which is exactly that number). `first_particle` is the Sturm count at $-10^{-9}$, the number of eigenvalues below zero: the zero mode, the lowest particle level (rank 0), has this number. Bisection then finds the nine levels of ranks $-3$ to $5$.

```python
say(f"G = 150: {len(all_eigs)} eigenvalues; {first_particle} lie below -1e-9, so the "
    f"lowest particle level (rank 0) is eigenvalue number {first_particle}")
say(f"bisection: {steps} halvings; largest difference from eigvalsh "
    f"{np.max(np.abs(found - all_eigs[first_particle + RANKS])):.1e}")
check(counts_ok, "the Sturm count equals the number of eigvalsh eigenvalues below x "
                 "at 241 test points")
check(np.max(np.abs(found - all_eigs[first_particle + RANKS])) < 1e-12,
      "bisection with Sturm counts finds the same nine levels as eigvalsh")
```

Out [5]: 299 eigenvalues, 149 of them below $-10^{-9}$, so the zero mode is eigenvalue number 149; bisection needed 55 halvings (the number estimated in Section 16.15) and agrees with the standard routine to $3.8\times10^{-14}$. The two checks require the Sturm counts to agree at all 241 trial values and the nine bisection levels to agree with `eigvalsh` to $10^{-12}$.

**In [6], the Sturm staircase (Figure 16b.2).**

```python
d30, o30 = even_matrix(30)
xs = np.linspace(-4.5, 4.5, 3601)  # a fine set of x values
stairs = sturm_count(d30, o30, xs)
eigs30 = np.linalg.eigvalsh(np.diag(d30) + np.diag(o30, 1) + np.diag(o30, -1))
fig, ax = plt.subplots(figsize=(8.0, 4.6))
ax.step(xs, stairs, where="post", color=PALETTE[0], lw=1.6,
        label="Sturm count $c(x)$, $G = 30$")
shown = eigs30[np.abs(eigs30) < 4.5]
ax.plot(shown, np.searchsorted(eigs30, shown) + 0.5, "o", color=PALETTE[1], ms=5,
        label="eigenvalues of the matrix")
```

For a coarse grid, $G = 30$ (59 eigenvalues), `xs` holds 3601 values of $x$ between $-4.5$ and $4.5$, `stairs` the Sturm count at each, and `eigs30` all eigenvalues. `ax.step(..., where="post")` draws the count as a staircase whose value changes just after each $x$. `shown` keeps the eigenvalues inside the window (`np.abs(eigs30) < 4.5` is a mask), and each is drawn as a circle half-way up its step (`searchsorted` gives the count below it, plus $0.5$).

```python
exact_lines = [0.0] + [s * math.sqrt(1.0 + (n * math.pi / 3.0) ** 2)
                       for n in range(1, 5) for s in (1, -1)]
for k, e in enumerate(sorted(exact_lines)):
    ax.axvline(e, color="k", lw=0.8, ls="--",
               label="exact levels (even parity)" if k == 0 else None)
ax.set_xlabel("$x$ (units of $m$)")
ax.set_ylabel("number of eigenvalues below $x$")
ax.set_title("Counting eigenvalues: the Sturm staircase")
ax.legend(fontsize=8, loc="upper left")
save_figure(fig, "sturm_staircase",
            "The Sturm count $c(x)$, the number of eigenvalues below $x$ of the "
            "even-parity matrix with $G = 30$ cells ($M = 1$, $L = 3$, $k = 0$), "
            "against $x$ in units of $m$. The count rises by one at each eigenvalue "
            "(circles, from a standard eigenvalue routine); the dashed lines are the "
            "exact levels $0$ and $\\pm\\sqrt{1 + (n\\pi/3)^2}$. Bisection finds "
            "eigenvalue number $i$ by asking only how many eigenvalues lie below a "
            "trial value.")
```

`exact_lines` holds the exact even levels of Section 16.13 in the window: 0 and $\pm\sqrt{1 + (n\pi/3)^2}$ for $n = 1$ to 4 (a list comprehension with two `for` parts makes both signs for each $n$). Each is drawn as a dashed vertical line, and only the first gets a legend label (`label=... if k == 0 else None`). After the axis labels, title and legend, `save_figure` saves Figure 16b.2. What the student should see: the staircase rises by exactly one at each eigenvalue; near zero the eigenvalues of the coarse matrix sit on the dashed exact levels (the zero mode exactly), while the outermost ones, at about $\pm4.3$, are visibly shifted from them, because their orbitals oscillate on the scale of a few cells and the grid error is larger.

```python
check(int(sturm_count(d30, o30, np.array([4.5]))[0]
          - sturm_count(d30, o30, np.array([-4.5]))[0]) == len(shown),
      "the staircase rises by one for each eigenvalue in the window")
```

The check: the count at $4.5$ minus the count at $-4.5$ equals the number of eigenvalues in the window.

**In [7], the exact discrete zero mode and an orbital.**

```python
def zero_mode(G, M=M_VALUE, L=L_VALUE):
    """The exact discrete zero mode: u_p = exp(p ln q), normalised so that
    sum u^2 h = 1; returns (half nodes y, u)."""
    h = L / G
    log_q = np.log1p(M * h / 2.0) - np.log1p(-M * h / 2.0)  # ln q, accurately
    u = np.exp(np.arange(G) * log_q)
    u /= math.sqrt(np.sum(u * u) * h)
    return -L + (np.arange(G) + 0.5) * h, u
```

`zero_mode(G)` builds the discrete zero mode of Section 16.15 as $u_p = e^{p\ln q}$. `np.log1p(t)` computes $\ln(1 + t)$ accurately also for small $t$, so `log_q` is $\ln(1 + Mh/2) - \ln(1 - Mh/2) = \ln q$ without first forming $q$: computing $q$ and then $q^p$ would multiply the rounding error of $q$ (about $10^{-16}$) by $p$, up to $10^{-13}$ for $p = 1200$. The vector is normalised so that $\sum u_p^2h = 1$ (`u /= x` divides every entry by $x$), the discrete form of $\int a^2\,dy = 1$. The function returns the half nodes and the values.

```python
y_half, u0 = zero_mode(150)
z = np.zeros(2 * 150 - 1)
z[0::2] = u0  # the u entries; every w entry stays 0
residual = np.max(np.abs(T150 @ z)) / np.max(np.abs(z))
A = math.sqrt(2.0 * M_VALUE / (1.0 - math.exp(-2.0 * M_VALUE * L_VALUE)))
shape_error = np.max(np.abs(u0 - A * np.exp(M_VALUE * y_half)))
say(f"discrete zero mode, G = 150: |T z| / |z| = {residual:.1e}; largest distance "
    f"from A e^(My) at the half nodes {shape_error:.2e} (A = {A:.6f})")
check(residual < 1e-12, "the discrete zero mode is an exact eigenvector with "
                        "eigenvalue 0 (to rounding), with b = 0")
check(shape_error < 1e-3, "the discrete zero mode follows A e^(My) to order h^2")
```

For $G = 150$ the zero mode is placed into a vector `z` of length 299: the $u$ entries at the even positions (`z[0::2]` takes every second entry from the first) and zeros at the $w$ positions. `T150 @ z` is the product of the matrix with the vector (`@` is matrix multiplication), and `residual` is its largest entry relative to the largest entry of `z`; it must vanish if $z$ is an eigenvector with eigenvalue 0. `A` is the continuum normalisation of Section 16.13 and `shape_error` the largest distance of the grid values from $A\,e^{My}$ at the half nodes. Out [7]: residual $1.5\times10^{-14}$ (rounding), distance $6.93\times10^{-5}$, $A = 1.415970$. The two checks require the residual below $10^{-12}$ and the distance below $10^{-3}$ (second order: with $h = 0.02$, $h^2 = 4\times10^{-4}$).

```python
values, vectors = np.linalg.eigh(T150)
level = first_particle + 1  # rank 1
vec = vectors[:, level] / math.sqrt(L_VALUE / 150)  # u and w with sum (u^2+w^2) h = 1
vec *= np.sign(vec[-1])  # fix the overall sign: u at the brane positive
u1, w1 = vec[0::2], vec[1::2]
y_node = -L_VALUE + np.arange(1, 150) * (L_VALUE / 150)
p1 = math.pi / L_VALUE
e1 = math.sqrt(M_VALUE ** 2 + p1 ** 2)
b_exact = lambda yy: np.sin(p1 * (yy + L_VALUE))
a_exact = lambda yy: (p1 * np.cos(p1 * (yy + L_VALUE))
                      + M_VALUE * np.sin(p1 * (yy + L_VALUE))) / e1
norm_exact = math.sqrt(L_VALUE)  # int (a^2 + b^2) dy = L for these a and b
scale = np.sign(a_exact(np.array([y_half[-1]]))[0]) / norm_exact
```

`np.linalg.eigh` returns all eigenvalues and eigenvectors (one per column) of `T150`. `level` is the number of the level of rank 1, one above the zero mode. Its eigenvector has length 1; dividing by $\sqrt h$ turns it into grid values $u_p$, $w_i$ with $\sum(u^2 + w^2)h = 1$, and multiplying by the sign of its last entry makes $u$ at the brane positive (an eigenvector is fixed only up to its sign). `u1` and `w1` are its $u$ and $w$ entries, `y_node` the 149 inner nodes. The exact orbital of rank 1 is $b = \sin(p_1(y + L))$ and $a = (p_1\cos(p_1(y + L)) + M\sin(p_1(y + L)))/\varepsilon_1$ with $p_1 = \pi/L$ (Section 16.13, $j = 1$); its integral $\int(a^2 + b^2)\,dy$ equals $L$, so `scale` divides by $\sqrt L$ and gives the exact orbital the sign of the grid's.

```python
say(f"level of rank 1: eigenvalue {values[level]:.10f}, exact {e1:.10f}")
check(np.max(np.abs(u1 - scale * a_exact(y_half))) < 1e-3
      and np.max(np.abs(w1 - scale * b_exact(y_node))) < 1e-3,
      "the eigenvector of rank 1 follows the exact orbital (a, b) to order h^2")
```

Out [7] prints the eigenvalue $1.4479202214$ next to the exact level $1.4479719304$ (the grid error $5.2\times10^{-5}$ is of order $h^2$), and the check requires the grid values of both components within $10^{-3}$ of the exact functions.

**In [8], the orbitals as a picture (Figure 16b.3).**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
fine = np.linspace(-L_VALUE, 0.0, 400)
left.plot(fine, A * np.exp(M_VALUE * fine), color="k", lw=1.2,
          label="exact $a = A\\,e^{My}$")
left.plot(y_half[::5], u0[::5], "o", color=PALETTE[0], ms=5,
          label="grid $u_p$, $G = 150$")
left.axhline(0.0, color=PALETTE[1], lw=2.0, label="$b = 0$ (exactly)")
left.set_xlabel("$y$")
left.set_ylabel("orbital component")
left.set_title("zero mode, $\\varepsilon = 0$")
left.legend(fontsize=8)
```

The left panel draws the exact zero mode $A\,e^{My}$ as a black line on 400 points, the grid values $u_p$ at every fifth half node as circles, and the line $b = 0$ in orange.

```python
right.plot(fine, scale * a_exact(fine), color="k", lw=1.2, label="exact $a$")
right.plot(fine, scale * b_exact(fine), color="k", lw=1.2, ls="--",
           label="exact $b$")
right.plot(y_half[::5], u1[::5], "o", color=PALETTE[0], ms=5, label="grid $u_p$")
right.plot(y_node[::5], w1[::5], "s", color=PALETTE[1], ms=5, label="grid $w_i$")
right.set_xlabel("$y$")
right.set_title(f"rank 1, $\\varepsilon = {e1:.4f}$")
right.legend(fontsize=8)
fig.tight_layout()
```

The right panel draws the exact $a$ (solid) and $b$ (dashed) of rank 1 and the grid values $u_p$ (circles) and $w_i$ (squares), every fifth point; its title shows the level.

```python
save_figure(fig, "orbitals",
            "Orbitals of the free problem at zero 3-momentum ($M = 1$, $L = 3$), "
            "normalised to $\\int (a^2 + b^2)\\,dy = 1$, against the hidden coordinate "
            "$y$ (tip $-3$, brane $0$). Left: the zero mode, $a = A e^{My}$ with "
            "$A = \\sqrt{2M/(1 - e^{-2ML})}$ and $b = 0$, localised at the brane; the "
            "circles are the exact discrete zero mode $u_p = q^p u_0$ of the grid "
            "with $G = 150$. Right: the even level of rank 1, "
            "$\\varepsilon = \\sqrt{1 + (\\pi/3)^2}$: its $b$ vanishes at the tip "
            "and at the brane, and the grid values lie on the exact curves.")
```

`save_figure` saves Figure 16b.3. What the student should see: on the left, the zero mode rises from $0.07$ at the tip to $1.42$ at the brane, an orbital bound to the brane, with $b$ exactly zero; on the right, the orbital of rank 1, whose $b$ vanishes at both ends (the even boundary conditions) while $a$ does not; in both panels the grid points lie on the exact curves.

**In [9], odd parity in the rotated frame.**

```python
phi = sp.symbols("phi", real=True)
s1 = sp.Matrix([[0, 1], [1, 0]])  # the Pauli matrices
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
rot = sp.cos(phi) * sp.eye(2) + sp.I * sp.sin(phi) * s1  # e^{i phi sigma1}
back = sp.cos(phi) * sp.eye(2) - sp.I * sp.sin(phi) * s1  # e^{-i phi sigma1}
ok2 = sp.simplify(back * s2 * rot - (sp.cos(2 * phi) * s2 + sp.sin(2 * phi) * s3))
ok3 = sp.simplify(back * s3 * rot - (sp.cos(2 * phi) * s3 - sp.sin(2 * phi) * s2))
check(ok2 == sp.zeros(2, 2) and ok3 == sp.zeros(2, 2),
      "sympy: the rotation turns sigma2 into cos(2 phi) sigma2 + sin(2 phi) sigma3 "
      "and sigma3 into cos(2 phi) sigma3 - sin(2 phi) sigma2")
```

The Pauli matrices are written as sympy matrices, `rot` is $R = \cos\phi + i\sin\phi\,\sigma_1$ and `back` its inverse $R^{-1} = \cos\phi - i\sin\phi\,\sigma_1$ (`sp.eye(2)` is the $2\times2$ unit matrix and `sp.I` the imaginary unit). `ok2` and `ok3` are $R^{-1}\sigma_2R - (\cos2\phi\,\sigma_2 + \sin2\phi\,\sigma_3)$ and $R^{-1}\sigma_3R - (\cos2\phi\,\sigma_3 - \sin2\phi\,\sigma_2)$, simplified; the check requires both to be the zero matrix: the two rotation rules of Section 16.14.

```python
def sector_matrix(G, odd, j=1.0, k=0.0, a4=0.0, M=M_VALUE, L=L_VALUE, H=1.0):
    """Diagonal and off-diagonal of T for one sector: parity (odd True/False),
    block type j, 3-momentum k, slice a4; constant M, v = 0."""
    h = L / G
    r = np.arange(2 * G - 1)  # the position of each unknown in the list
    y_r = -L + (r + 1) * h / 2.0  # its y (half node for even r, node for odd r)
    is_u = r % 2 == 0
    K_r = np.exp(-H * y_r - a4) * k  # K = kappa k
    angle = j * 0.5 * math.pi * (y_r + L) / L if odd else np.zeros_like(y_r)
    dangle = j * math.pi / (2.0 * L) if odd else 0.0  # phi'
    m2 = M * np.cos(2 * angle) - K_r * np.sin(2 * angle)
    k2 = M * np.sin(2 * angle) + K_r * np.cos(2 * angle)
    d = np.where(is_u, j * (dangle + k2), j * (dangle - k2))
    pair = np.arange(2 * G - 2)  # the pair (r, r + 1)
    u_of_pair = np.where(pair % 2 == 0, pair, pair + 1)  # its half node
    sign = np.where(pair % 2 == 0, 1.0, -1.0)  # +1/h (u then w), -1/h (w then u)
    o = j * (sign / h + 0.5 * m2[u_of_pair])
    return d, o
```

`sector_matrix` builds the matrix of any sector, both parities, any block type $j$, 3-momentum $k$ and slice $a_{4,0}$, for constant $M$ and $v = 0$. `r` numbers the $2G - 1$ unknowns and `y_r` gives each its position: the unknown number $r$ lies at $-L + (r + 1)h/2$, a half node for even $r$ and a node for odd $r$; `is_u` marks the $u$ unknowns. `K_r` is $K = \kappa k$ at each position. For odd parity `angle` is $\phi = j\,\tfrac{\pi}{2}\,\tfrac{y + L}{L}$ and `dangle` its derivative $\phi' = j\pi/(2L)$; for even parity both are zero. `m2` and `k2` are $m_2 = M\cos2\phi - K\sin2\phi$ and $k_2 = M\sin2\phi + K\cos2\phi$. The diagonal is $j(\phi' + k_2)$ in the $u$ rows and $j(\phi' - k_2)$ in the $w$ rows. For the neighbour entries, `pair` numbers the pairs $(r, r + 1)$, `u_of_pair` is the position of the $u$ in each pair (the first for even $r$, the second for odd $r$), and `sign` gives $+1/h$ for a $u$ followed by a $w$ and $-1/h$ for a $w$ followed by a $u$; the entry is $j(\pm\tfrac1h + \tfrac12m_2)$ with $m_2$ at the half node of the pair. These are the formulas of Section 16.14.

```python
agree = []
for odd in (False, True):
    for j_value in (1.0, -1.0):
        for n2, r3, k_value in ((0, 1, 0.0), (4, 6, 0.5)):  # |k| = 0.25 sqrt(n2)
            phys = K.Phys(m=M_VALUE, L=L_VALUE, H=1.0)
            grid = K.Grid(phys, 300)
            sector = K.Sectors([(n2, r3, j_value, int(odd))])
            alpha, beta = K.sector_arrays(grid, phys, sector,
                                          np.full(grid.n, M_VALUE), np.zeros(grid.n))
            d, o = sector_matrix(300, odd, j=j_value, k=k_value)
            agree.append(max(np.max(np.abs(alpha[:, 0] - d)),
                             np.max(np.abs(beta[:, 0] - o))))
say(f"largest difference from ks_fd.sector_arrays over 8 sectors: {max(agree):.1e}")
check(max(agree) <= 1e-12,
      "sector_matrix equals the reference's matrices for both parities, both block "
      "types, k = 0 and k = 0.5")
```

The loops compare `sector_matrix` with the reference's `K.sector_arrays` for both parities (`int(odd)` is 1 for odd), both block types, and two momenta: $k = 0$ (shell $n_2 = 0$) and the shell $n_2 = 4$ with $r_3(4) = 6$ points, where $|k| = 0.25\sqrt4 = 0.5$. `agree` collects the largest difference of each of the 8 comparisons. Out [9]: the largest is $0.0$; the check requires at most $10^{-12}$.

**In [10], the matrices as heat maps (Figure 16b.4).**

```python
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.6))
for ax, odd, title in ((axes[0], False, "even parity"), (axes[1], True, "odd parity")):
    d, o = sector_matrix(8, odd)
    T = np.diag(d) + np.diag(o, 1) + np.diag(o, -1)
    image = ax.imshow(T, cmap="RdBu_r", vmin=-3.5, vmax=3.5)
    ax.set_title(f"$T$, {title}, $G = 8$")
    ax.set_xticks(range(0, 15, 2))  # whole numbers: rows and columns 0 to 14
    ax.set_yticks(range(0, 15, 2))
    ax.set_xlabel("column $c$")
    ax.set_ylabel("row $r$")
fig.colorbar(image, ax=axes, shrink=0.85, label="entry $T_{rc}$ (units of $m$)")
```

For $G = 8$ ($15$ unknowns, $h = 0.375$) the even and the odd matrix are assembled and drawn as **heat maps**: `imshow` paints entry $T_{rc}$ as a coloured square in row $r$ and column $c$, with the colour scale `"RdBu_r"` from blue (negative) through white (zero) to red (positive), fixed between $-3.5$ and $3.5$ so that both panels use the same colours. The ticks are placed at the even numbers 0 to 14, and `fig.colorbar` adds one colour scale for both panels.

```python
save_figure(fig, "matrix_heat_maps",
            "The reference matrices $T$ for $G = 8$ cells ($h = 0.375$, $M = 1$, "
            "$L = 3$, $j = +1$, $k = 0$) as heat maps, entry $T_{rc}$ in units of $m$ "
            "by colour (blue negative, red positive, white zero). Left, even parity: "
            "only the two neighbouring diagonals are filled, alternating "
            "$1/h + M/2 = 3.17$ and $-1/h + M/2 = -2.17$. Right, odd parity in the "
            "rotated frame: the diagonal carries $\\phi' \\pm M\\sin 2\\phi$ and the "
            "off-diagonal entries carry $M\\cos 2\\phi$, which changes sign along $y$.")
```

`save_figure` saves Figure 16b.4. What the student should see: both matrices are filled only on the two diagonals next to the main diagonal (tridiagonal), and each is its own mirror image across the main diagonal (symmetric). In the even matrix the main diagonal is white (zero) and the neighbour entries alternate between red, $1/h + M/2 = 3.17$, and blue, $-1/h + M/2 = -2.17$. In the odd matrix the rotation puts $\phi' \pm M\sin2\phi$ on the main diagonal, and the neighbour entries carry $M\cos2\phi$, which changes sign along $y$ (from $+M$ at the tip to $-M$ at the brane), so the colours of the pairs change from the top left to the bottom right.

**In [11], five grids and Richardson extrapolation.**

```python
GRIDS = (150, 300, 600, 1200, 2400)
EXACT = np.concatenate([EXACT_EVEN, EXACT_ODD])  # 18 levels: even, then odd
LEVELS = {}  # G -> the 18 levels on that grid
for G in GRIDS:
    found = []
    for odd in (False, True):
        d, o = sector_matrix(G, odd)
        lowest_particle = int(sturm_count(d, o, np.array([-1e-9]))[0])
        values_g, _ = bisection(d, o, lowest_particle + RANKS)
        found.append(values_g)
    LEVELS[G] = np.concatenate(found)
    say(f"G = {G:4d}: largest |level - exact| = "
        f"{np.max(np.abs(LEVELS[G] - EXACT)):.3e}")
```

`GRIDS` holds the five grids $G = 150$ to $2400$ and `EXACT` the 18 exact levels (nine even, then nine odd; `np.concatenate` joins arrays). For each grid and each parity the matrix is built, the zero-mode number is found by a Sturm count at $-10^{-9}$, and bisection finds the nine levels of ranks $-3$ to $5$; the 18 levels are kept in `LEVELS`, and the largest distance from the exact levels is printed. Out [11]: $2.607\times10^{-3}$ for $G = 150$, then $6.518\times10^{-4}$, $1.629\times10^{-4}$, $4.074\times10^{-5}$ and $1.018\times10^{-5}$: each halving of $h$ divides the error by 4, as second order demands. This cell takes about ten seconds; the largest matrix has 4799 rows.

```python
def richardson(x1, x2, x3):
    """Three-grid Richardson value and uncertainty, as in the reference program."""
    r_fine, r_coarse = (4.0 * x3 - x2) / 3.0, (4.0 * x2 - x1) / 3.0
    R = (16.0 * r_fine - r_coarse) / 15.0
    return R, np.abs(R - r_fine) + 2e-12 * np.maximum(1.0, np.abs(R))
```

`richardson` is the reference's three-grid extrapolation of Section 16.5, now for whole arrays at once (`np.abs` and `np.maximum` work entry by entry).

```python
R18, U18 = richardson(LEVELS[300], LEVELS[600], LEVELS[1200])
record = json.loads(repository_file(
    "Revision/kohn_sham/reference/results/free-checks.json").read_text(encoding="utf-8"))
rows = [r for r in record["analytic"]["rows"]
        if float(r[0]) == 1.0 and float(r[1]) == 3.0 and r[3] == 1]
order = [(par, rank) for par in ("even", "odd") for rank in RANKS]
check([(r[2], r[4]) for r in rows] == order, "the record has our 18 rows in our order")
dev_R = max(abs(float(r[5]) - R18[i]) for i, r in enumerate(rows))
dev_U = max(abs(float(r[6]) - U18[i]) for i, r in enumerate(rows))
dev_1200 = max(abs(float(r[9]) - (LEVELS[1200][i] - EXACT[i]))
               for i, r in enumerate(rows))
say(f"against the record: R differs by at most {dev_R:.1e}, U by {dev_U:.1e}, "
    f"G = 1200 minus exact by {dev_1200:.1e}")
say(f"Richardson value minus exact: at most {np.max(np.abs(R18 - EXACT)):.1e} "
    f"(single grid G = 1200: {np.max(np.abs(LEVELS[1200] - EXACT)):.1e})")
check(dev_R < 1e-12 and dev_U < 1e-12 and dev_1200 < 1e-12,
      "our levels, R and U reproduce the 18 rows of the record",
      record="Revision/kohn_sham/reference/results/free-checks.json, analytic rows")
check(np.max(np.abs(R18 - EXACT)) <= 1e-11,
      "the Richardson values equal the exact levels to 1e-11",
      record="Revision/kohn_sham/reports/ks-reference.json, check "
             "free_k0_analytic_spectra")
```

`R18` and `U18` are the Richardson values and uncertainties of the 18 levels from $G = 300$, $600$, $1200$. `record` is the committed file `free-checks.json`; `rows` keeps its rows with $m = 1$, $L = 3$ and $j = +1$ (each row lists $m$, $L$, parity, $j$, rank, $R$, $U$, the exact level, $R$ minus exact, and the $G = 1200$ value minus exact). The first check confirms that these are our 18 rows in our order (`order` lists the pairs (parity, rank)). `dev_R`, `dev_U` and `dev_1200` are the largest differences between the record and our $R$, our $U$ and our $G = 1200$ errors. Out [11]: $8.9\times10^{-15}$, $1.3\times10^{-15}$ and $6.2\times10^{-15}$, so the second check (all below $10^{-12}$) reproduces the record. The Richardson values lie within $1.2\times10^{-14}$ of the exact levels, while the best single grid $G = 1200$ is $4.1\times10^{-5}$ away: two Richardson steps gain about nine digits. The third check requires $10^{-11}$, the criterion of the reference's check free_k0_analytic_spectra.

**In [12], the Richardson ladder (Figure 16b.5).**

```python
hs = np.array([L_VALUE / G for G in GRIDS])
picks = [("even", 1), ("odd", 0), ("even", 5)]
fig, ax = plt.subplots(figsize=(8.0, 6.4))
for colour, (par, rank) in zip(PALETTE, picks):
    i = order.index((par, rank))
    single = np.array([abs(LEVELS[G][i] - EXACT[i]) for G in GRIDS])
    one = np.array([abs((4.0 * LEVELS[GRIDS[g + 1]][i] - LEVELS[GRIDS[g]][i]) / 3.0
                        - EXACT[i]) for g in range(4)])
    two = np.array([abs(richardson(LEVELS[GRIDS[g]][i], LEVELS[GRIDS[g + 1]][i],
                                   LEVELS[GRIDS[g + 2]][i])[0] - EXACT[i])
                    for g in range(3)])
    label = f"{par} rank {rank} ($\\varepsilon = {EXACT[i]:.3f}$)"
    ax.loglog(hs, single, "o-", color=colour, lw=1.4, label=f"{label}: single grid")
    ax.loglog(hs[:4], one, "s--", color=colour, lw=1.2, label="one step")
    ax.loglog(hs[:3], np.maximum(two, 1e-16), "^:", color=colour, lw=1.2,
              label="two steps")
```

`hs` holds the five cell widths. For three levels (even rank 1, odd rank 0 and even rank 5; `order.index` finds a level's position), the cell computes three error series against the exact level: `single`, the five single grids; `one`, the four one-step values $(4x(h/2) - x(h))/3$ of neighbouring pairs; and `two`, the three three-grid values of neighbouring triples. Each series is drawn on logarithmic axes in the level's colour: circles with solid lines, squares with dashed lines, triangles with dotted lines (`"^:"`); zero errors are raised to $10^{-16}$.

```python
ax.axhline(1e-14, color="k", lw=0.8, ls="-.", label="rounding floor $10^{-14}$")
ax.set_xlabel("cell width $h$ of the coarsest grid used (units of $1/H$)")
ax.set_ylabel("distance from the exact level (units of $m$)")
ax.set_title("The Richardson ladder: slopes 2, 4 and then rounding")
ax.set_ylim(1e-16, 1e-1)
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_xticks(hs)  # tick labels only at the five cell widths
ax.set_xticklabels([f"{t:g}" for t in hs])
ax.legend(fontsize=7, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.13))
```

The dash-dotted line at $10^{-14}$ marks the rounding floor. The axes, the tick labels at the five cell widths (as in Notebook 16a, In [8]) and a legend in three columns below the plot (`bbox_to_anchor=(0.5, -0.13)` places it under the axes) complete the figure.

```python
save_figure(fig, "convergence_ladder",
            "Distance of the computed level from the exact level, in units of $m$, "
            "against the cell width $h = 3/G$ for $G = 150$ to $2400$, logarithmic "
            "axes, for three levels of the free problem: circles, single grids "
            "(slope 2, error proportional to $h^2$); squares, one Richardson step "
            "$(4x(h/2) - x(h))/3$ (slope 4); triangles, the three-grid value of the "
            "reference (two steps), already at the rounding floor near $10^{-14}$. "
            "The high level of rank 5 has the largest errors, because its orbital "
            "varies fastest from cell to cell.")
```

`save_figure` saves Figure 16b.5. What the student should see: the single-grid errors fall along straight lines of slope 2 (a factor 4 per halving), the one-step errors along lines of slope 4 (a factor 16), and the two-step errors reach the rounding floor of about $10^{-14}$ at once, for the two lower levels already on the coarsest triple and for the level of rank 5 from the second triple on; there they scatter instead of falling further, because at the floor rounding, not the grid, sets the error. The high level of rank 5 has the largest errors in every series, because its orbital varies fastest from cell to cell.

**In [13], every ratio tends to 4 (Figure 16b.6).**

```python
fig, ax = plt.subplots(figsize=(8.0, 4.4))
worst = {}
for colour, (g1, g2, g3) in zip(PALETTE, ((150, 300, 600), (300, 600, 1200),
                                          (600, 1200, 2400))):
    d1, d2 = LEVELS[g1] - LEVELS[g2], LEVELS[g2] - LEVELS[g3]
    keep = (np.abs(d1) > 1e-10) & (np.abs(d2) > 1e-10)  # not the zero modes
    ratio = d1[keep] / d2[keep]
    worst[(g1, g2, g3)] = float(np.max(np.abs(ratio - 4.0)))
    ax.plot(EXACT[keep], ratio, "o", color=colour, ms=6,
            label=f"grids {g1}, {g2}, {g3}: largest $|$ratio $- 4|$ = "
                  f"{worst[(g1, g2, g3)]:.1e}")
ax.axhline(4.0, color="k", lw=1.0)
ax.set_xlabel("exact level $\\varepsilon$ (units of $m$)")
ax.set_ylabel("$(x(G) - x(2G))/(x(2G) - x(4G))$")
ax.set_title("Second-order convergence: every ratio tends to 4")
ax.legend(fontsize=8)
```

For three triples of grids the convergence ratio of Section 16.4 is computed for all 18 levels; `keep` leaves out the two zero modes, whose differences are below $10^{-10}$ because they are exact on every grid. `worst` keeps each triple's largest distance from 4, and the ratios are drawn against the exact level energies, one colour per triple, with the line 4.

```python
save_figure(fig, "error_ratios",
            "The convergence ratio $(x(G) - x(2G))/(x(2G) - x(4G))$ of the 16 nonzero "
            "levels of ranks $-3$ to $5$ (both parities, $M = 1$, $L = 3$, $k = 0$) "
            "against the exact level in units of $m$, for three triples of grids. A "
            "ratio of 4 means an error proportional to $h^2$; the ratios approach 4 "
            "as the grids get finer, fastest for the low levels. The two zero modes "
            "are exact on every grid and have no ratio.")
say("largest |ratio - 4| per triple: " + ", ".join(
    f"{k}: {v:.2e}" for k, v in worst.items()))
check(worst[(300, 600, 1200)] <= 0.01
      and worst[(600, 1200, 2400)] < worst[(300, 600, 1200)],
      "the ratios lie within 0.01 of 4 and approach 4 on finer grids",
      record="Revision/kohn_sham/reports/ks-reference.json, check "
             "free_convergence_order_two")
```

`save_figure` saves Figure 16b.6, and the printed line (Out [13]) gives the largest distances from 4: $6.57\times10^{-4}$, $1.64\times10^{-4}$ and $4.10\times10^{-5}$ for the triples $(150, 300, 600)$, $(300, 600, 1200)$ and $(600, 1200, 2400)$, each four times smaller than the one before, as the correction $\tfrac{15}{16}\tfrac{d}{c}h^2$ of Section 16.4 predicts. What the student should see: the 16 ratios of each triple lie close to 4, the finer triples closer, and the high levels deviate most. The check requires the middle triple within $0.01$ of 4 (the reference's criterion free_convergence_order_two asks for $[3.99, 4.01]$) and the finest triple closer still.

**In [14], the brane band along the deflating history.**

```python
SLICES = (0.0, 0.5, 1.0, 1.5, 2.0)

def slope_formula(a4, M=M_VALUE, H=1.0, L=L_VALUE):
    """c = e^(-a4) (2M/(1 - e^(-2ML))) (1 - e^(-(2M - H)L))/(2M - H)."""
    return (math.exp(-a4) * 2.0 * M / (1.0 - math.exp(-2.0 * M * L))
            * (1.0 - math.exp(-(2.0 * M - H) * L)) / (2.0 * M - H))
```

`SLICES` are the five slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$, and `slope_formula` is the slope $c(a_{4,0})$ derived in Section 16.15.

```python
per_grid = {}
for G in (300, 600, 1200):
    yh, u = zero_mode(G)
    weight = u * u * (L_VALUE / G)  # u_p^2 h, summing to 1
    per_grid[G] = np.array([np.sum(np.exp(-yh - a4) * weight) for a4 in SLICES])
R_slope, U_slope = richardson(per_grid[300], per_grid[600], per_grid[1200])
```

For the grids $300$, $600$, $1200$ the discrete zero mode is built; `weight` holds $u_p^2h$, which adds up to 1; and the slope at each slice is $\sum\kappa(y_{p+1/2})\,u_p^2\,h$ with $\kappa = e^{-y - a_{4,0}}$ ($H = 1$), the discrete Hellmann-Feynman formula of Section 16.15. Richardson extrapolation over the three grids gives `R_slope`.

```python
formula = np.array([slope_formula(a4) for a4 in SLICES])
theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json").read_text(
    encoding="utf-8"))
stated = float(theory["checksNumeric"]["braneBandSlope_M1_H1_L3_a0"])
rec_rows = record["brane_band_slope"]["rows"]
print("a4,0   slope (grid, Richardson)   formula            record")
for i, a4 in enumerate(SLICES):
    print(f"{a4:4.1f}   {R_slope[i]:.15f}      {formula[i]:.15f}  "
          f"{float(rec_rows[i][1]):.15f}")
```

`formula` holds the exact slopes. `theory` is the committed theory file `ks-theory.json`, and `stated` its number checksNumeric.braneBandSlope_M1_H1_L3_a0, the slope at $a_{4,0} = 0$ written in the file. `rec_rows` are the rows of the record's entry brane_band_slope. The table of Out [14] prints, for each slice, the grid value, the formula and the record with fifteen decimals; at $a_{4,0} = 0$ the three agree to fourteen decimals, $1.90514825364486$, and at $a_{4,0} = 2$ all three read $0.257833778514766$.

```python
rel_formula = np.max(np.abs(R_slope - formula) / formula)
rel_record = max(abs(float(r[1]) - R_slope[i]) / formula[i]
                 for i, r in enumerate(rec_rows))
say(f"largest relative difference: from the formula {rel_formula:.1e}, from the "
    f"record {rel_record:.1e}")
print("stated in ks-theory.json (checksNumeric): c at a4,0 = 0 is "
      + theory["checksNumeric"]["braneBandSlope_M1_H1_L3_a0"])
check(rel_formula <= 1e-11 and abs(slope_formula(0.0) - stated) <= 1e-15 * stated,
      "the grid slope equals c e^(-a4,0) of ks-theory.json at the five slices",
      record="Revision/kohn_sham/reports/ks-reference.json, check "
             "free_brane_band_slope")
check(rel_record <= 1e-13, "our slopes reproduce the record's brane_band_slope rows",
      record="Revision/kohn_sham/reference/results/free-checks.json, brane_band_slope")
check(np.allclose(R_slope[1:] / R_slope[:-1], math.exp(-0.5), rtol=1e-12, atol=0),
      "from slice to slice the slope shrinks by exactly e^(-0.5)")
```

`rel_formula` and `rel_record` are the largest relative differences from the formula and from the record: $3.8\times10^{-16}$ and $2.6\times10^{-15}$ (Out [14]). The line printed next shows the number written in `ks-theory.json`. The first check requires the grid slope to equal the formula to $10^{-11}$ and the formula at $a_{4,0} = 0$ to equal the stated number to $10^{-15}$, the reference's criterion free_brane_band_slope; the second reproduces the record's rows; the third confirms that from slice to slice the slope shrinks by exactly $e^{-0.5}$ (`np.allclose` with a relative tolerance $10^{-12}$; `R_slope[1:] / R_slope[:-1]` divides each slope by the one before).

**In [15], the brane band as a picture (Figure 16b.7).**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
a_fine = np.linspace(0.0, 2.0, 100)
left.semilogy(a_fine, [slope_formula(a) for a in a_fine], color="k", lw=1.2,
              label="formula $c\\,e^{-a_{4,0}}$")
left.semilogy(SLICES, R_slope, "o", color=PALETTE[0], ms=8,
              label="grid, three-grid Richardson value")
left.set_xlabel("slice $a_{4,0}$ (3-space inflates, extra times deflate)")
left.set_ylabel("brane-band slope $d\\varepsilon/dk$ at $k = 0$")
left.set_title("The brane band flattens as $e^{-a_{4,0}}$")
left.legend(fontsize=8)
```

The left panel draws the formula $c\,e^{-a_{4,0}}$ on 100 slices as a black line and the five Richardson values as circles, on a logarithmic vertical axis, where a function $e^{-a}$ is a straight line.

```python
hs3 = np.array([L_VALUE / G for G in (300, 600, 1200)])
right.loglog(hs3, [abs(per_grid[G][0] - formula[0]) for G in (300, 600, 1200)],
             "o-", color=PALETTE[1], lw=1.5, ms=7,
             label="single grid, $a_{4,0} = 0$")
right.loglog(hs3, abs(per_grid[300][0] - formula[0]) / 3.0 * (hs3 / hs3[0]) ** 2,
             "k--", lw=0.9, label="slope 2 (drawn a factor 3 lower)")
right.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
right.set_xticks(hs3)  # tick labels only at the three cell widths
right.set_xticklabels([f"{t:g}" for t in hs3])
right.set_xlabel("cell width $h$")
right.set_ylabel("$|c(G) - c|$")
right.set_title("grid error of the slope")
right.legend(fontsize=8)
fig.tight_layout()
```

The right panel draws, for $a_{4,0} = 0$, the distance of the single-grid slopes from the exact slope against the cell width, with a dashed line of slope 2 drawn a factor 3 lower, and tick labels at the three cell widths.

```python
save_figure(fig, "brane_band_slope",
            "The slope $d\\varepsilon/dk$ at $k = 0$ of the brane band (even parity, "
            "$j = +1$, $M = H = 1$, $L = 3$). Left: against the slice $a_{4,0}$ of the "
            "history, logarithmic vertical axis; the Richardson values of the grid "
            "(circles) lie on the formula of ks-theory.json, $c(0)\\,e^{-a_{4,0}}$ "
            "with $c(0) = 1.90515$: the 3-momentum is redshifted as 3-space inflates "
            "while the three extra times deflate. Right: the single-grid values at "
            "$a_{4,0} = 0$ approach the exact slope with an error proportional to "
            "$h^2$ (parallel to the dashed line of slope 2).")
```

`save_figure` saves Figure 16b.7. What the student should see: on the left, the five circles lie exactly on a straight line falling by a factor $e^{-2} = 0.135$ from $1.905$ to $0.258$: the brane band flattens as 3-space inflates and the extra times deflate, because the 3-momentum is redshifted; on the right, the grid error of the slope falls with slope 2, from about $1.3\times10^{-5}$ to $8\times10^{-7}$.

**In [16], the reference program's own free-field job.**

```python
import run_reference as RR  # noqa: E402  the reference program (Revision code)

CO = RR.theory_coefficients()  # coefficients read and checked from ks-theory.json
free = RR.jsonable(RR.free_checks_job(CO)["data"])
committed = repository_file(
    "Revision/kohn_sham/reference/results/free-checks.json").read_text(encoding="utf-8")
text = json.dumps(free, indent=1, ensure_ascii=True) + "\n"  # as the program writes
say(f"the new free-field result is identical to the record byte for byte: "
    f"{text == committed}")
```

The reference program is imported (as in Notebook 16a), and its job `free_checks_job` is run: it computes the exact-level comparison for three choices of $(M, L)$, both block types and both parities on five grids, the zero mode, the brane-band slope and the split of every sector into particle and sea levels (about ten seconds). Its result is written as text exactly as the program writes the file and compared with the committed file; Out [16] says that the two are identical byte for byte.

```python
same = json.loads(text) == json.loads(committed)
if not same:  # another computer may round the last digits differently
    old = json.loads(committed)["analytic"]
    same = all(abs(float(a[5]) - float(b[5])) < 1e-12
               for a, b in zip(free["analytic"]["rows"], old["rows"]))
check(same, "the reference's free-field job reproduces free-checks.json",
      record="Revision/kohn_sham/reference/results/free-checks.json")
```

If the texts were not identical (another computer may round the last digits differently), `same` would still accept the result when the decoded contents are equal or the Richardson values of all rows agree to $10^{-12}$. The check requires this.

```python
an, zm = free["analytic"], free["zero_mode"]
bb, pb = free["brane_band_slope"], free["particle_branch"]
criteria = {
    "free_k0_analytic_spectra": an["max_error_richardson"] <= 1e-11,
    "free_convergence_order_two": 3.99 <= an["ratio_min"] and an["ratio_max"] <= 4.01,
    "free_k0_block_type_symmetry": an["jsym_max"] <= 1e-13
    and zm["jsym_profile"] <= 1e-13,
    "free_zero_mode": zm["max_abs_eps"] <= 1e-13 and zm["max_w_over_u"] <= 1e-12
    and zm["profile_richardson_max_error"] <= 1e-9,
    "free_brane_band_slope": bb["max_rel"] <= 1e-11
    and bb["formula_vs_theory_number"] <= 1e-15,
    "free_particle_branch": pb["violations"] == 0
    and pb["closest_to_zero_away_from_zero_modes"] > 1e-3,
}
```

`an`, `zm`, `bb` and `pb` are the four parts of the result. `criteria` is a dictionary from the names of the six free-field checks of the reference report to their conditions, with exactly the thresholds of the reference program: the Richardson levels within $10^{-11}$ of the exact ones; all convergence ratios in $[3.99, 4.01]$; the two block types' spectra and zero-mode profiles equal to $10^{-13}$; the zero mode's eigenvalue below $10^{-13}$, its $w$ entries below $10^{-12}$ of its $u$ entries and its extrapolated profile within $10^{-9}$ of $A\,e^{My}$; the slope within $10^{-11}$ (relative) of the formula, and the formula equal to the stated number; and no level on the wrong side of zero, with no level within $10^{-3}$ of zero apart from the zero modes.

```python
say(f"max error of the Richardson values {an['max_error_richardson']:.1e}; ratios "
    f"{an['ratio_min']:.5f} to {an['ratio_max']:.5f}; zero mode |eps| <= "
    f"{zm['max_abs_eps']:.1e}; slope {bb['max_rel']:.1e} relative")
report = json.loads(repository_file(
    "Revision/kohn_sham/reports/ks-reference.json").read_text(encoding="utf-8"))
verdicts = {c["name"]: c["verdict"] for c in report["checks"]}
for name, ok in criteria.items():
    check(ok and verdicts[name] == "PASS", f"{name} holds for the new run",
          record=f"Revision/kohn_sham/reports/ks-reference.json, check {name}")
```

The printed line (Out [16]) gives the largest error of the Richardson levels ($2.8\times10^{-14}$, over all three $(M, L)$), the range of the ratios ($3.99977$ to $4.00019$), the size of the zero mode's eigenvalue ($1.3\times10^{-39}$) and the slope's relative error ($2.6\times10^{-15}$); these are the numbers of the reference report. The report's verdicts are read into a dictionary, and the loop makes one check per criterion: it must hold for the new run and the report's verdict must be PASS. Six PASS lines follow, each naming the check of `Revision/kohn_sham/reports/ks-reference.json` that it reproduces.

**In [17], the last check.**

```python
figure_files = [f"{FIGURE_FOLDER}/16b_{k}_{name}.png" for k, name in enumerate(
    ["staggered_grid", "sturm_staircase", "orbitals", "matrix_heat_maps",
     "convergence_ladder", "error_ratios", "brane_band_slope"], start=1)]
check(all(output_file(f).is_file() for f in figure_files),
      "every figure file of this notebook exists")
all_checks_passed()
```

As In [23] of Notebook 16a, for the seven figures; it prints ALL 31 CHECKS PASSED (notebook 16b): five checks in In [2], three each in In [4], In [7], In [11] and In [14], two each in In [5] and In [9], seven in In [16], and one each in In [6], In [13] and In [17].
