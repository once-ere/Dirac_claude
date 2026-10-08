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

where the prime is $d/dy$, $\varepsilon$ is the level, $M(y) = m + \tfrac{15}{16}\lambda S(y)$ the effective mass and $v(y) = -\tfrac{1}{16}\lambda n(y)$ the potential (`Revision/kohn_sham/ks-theory.json`, `blockEquation.realForm` and `exchange.kohnShamPotentials`). The boundary conditions are the regular tip $b(-L) = 0$ (CHOSEN) and the ASSUMED Z2 brane: even orbitals have $b(0) = 0$, odd orbitals $a(0) = 0$. The densities $n$ and $S$ are sums over the occupied orbitals, so the potentials depend on the solution, and the problem is solved again and again until it reproduces itself (self-consistency). At a temperature $T > 0$ the occupations are Fermi-Dirac numbers $f = 1/(1 + e^{(\varepsilon - \mu)/T})$, and the chemical potential $\mu$ is fixed by $\sum g f = N$. The list of states, the **canonical matrix**, holds 75 ground states (three particle numbers, five couplings, five slices) and 135 thermal states (three particle numbers, three couplings, five slices, three temperatures).

**The Rust solver** (Chapter 15). For a trial energy it integrates the two equations from the tip to the brane with the Runge-Kutta rule RK4 in $G = 900$ steps, counts levels with the Pruefer angle, and finds each level by Newton's method inside a bracket to a tolerance of $10^{-13}$; self-consistency is reached with Anderson mixing to a residual of $10^{-11}$ (`Revision/kohn_sham/results/parameters.json`, numerics).

**The reference solver** (`Revision/kohn_sham/reference/run_reference.py` with the module `ks_fd.py` in the same folder). It places the two functions of an orbital on a **staggered grid** of $G$ cells: $a$ at the centres of the cells and $b$ at their ends. The differential equations then become the eigenvalue problem of a symmetric **tridiagonal matrix** with $2G - 1$ rows (a matrix whose only nonzero entries are on the main diagonal and its two neighbours). It finds each eigenvalue by its number, by counting how many eigenvalues lie below a trial value (the **Sturm count**) and halving an interval (**bisection**), so that no level can be missed; it then sharpens each eigenvalue and computes its eigenvector. Every quantity is computed on three grids, $G = 300$, $600$ and $1200$, and the three results are combined by **Richardson extrapolation** (Section 16.5) into a value $R$ with a measured uncertainty $U$. Self-consistency is reached with Anderson mixing to a residual of $10^{-12}$. The reference re-derives from their stated rules even the inputs it could have copied: the particle numbers 136 and 688 and the couplings $\lambda_1$, $\lambda_2$ (for $N = 8$: $0.01946$ and $0.05838$; `Revision/kohn_sham/reports/ks-reference.json`, check `parameters_calibration`).

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

**An example from the record.** Notebook 16a prints the Kohn-Sham energy of the state N136_lamp2_a20 on the three grids: $E_{KS}(300) = 12.449082943357$, $E_{KS}(600) = 12.449020346521$, $E_{KS}(1200) = 12.449004697554$. The two differences are $6.2597\times10^{-5}$ and $1.5649\times10^{-5}$, and their ratio is $4.00006$: second order, in the asymptotic regime. The reference applies the test to every level of every ground state and requires the median ratio of each state to lie within $0.05$ of 4; the worst state is within $7.4\times10^{-5}$ of 4 (`Revision/kohn_sham/reports/ks-reference.json`, check `richardson_asymptotic_ratio`).

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

**Testing the uncertainty on a fourth grid.** The argument above rests on the ASSUMED form of the error. The record tests it. One state, N136_lamp2_a20 (the strongest coupling, with the largest densities at the tip), is solved on a fourth grid as well, $G = 2400$. From $(300, 600, 1200)$ the three-grid value $R_{123}$ with its uncertainty $U_{123}$ is formed, and from $(600, 1200, 2400)$ the three-grid value $R_{234}$. The error of $R_{234}$ is of order $(h/2)^6 = h^6/64$, so it is about 64 times smaller than the error of $R_{123}$; hence $|R_{123} - R_{234}|$ is practically the error of $R_{123}$, and the test is whether it is at most $U_{123}$. For all 19 classes of quantities (energies, levels, integrals, values at the tip and at the brane, five profiles with 151 points each) it is: the largest ratio $|R_{123} - R_{234}|/U_{123}$ is $0.787$, for the value of the pressure $p_8$ at the tip (`Revision/kohn_sham/reports/ks-reference.json`, check `richardson_uncertainty_validated`). Notebook 16a repeats this test (In [7], Figure 16a.2). The uncertainty is therefore an honest estimate, and it is not hugely larger than the error either, which a useful estimate must also be.

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

**Two conditions.** First, the measured difference applies to the committed results only if the canonical run made for the measurement reproduces them. The record checks this for every state: the canonical runs reproduce the committed matrix with every difference zero (`Revision/kohn_sham/reports/ks-crosscheck.json`, check `rust_refinement_applies_to_matrix`). Second, some quantities (the Delta-SCF energy, the adiabaticity measure, the finite-difference $dE/da_4$, the heat capacity) are not printed by the single runs of the measurement. For them the cross-check uses the largest canonical-minus-refined difference over the whole canonical matrix, taken from the Rust solver's determinism report; the values are listed in `Revision/kohn_sham/reports/ks-crosscheck.json` under `rust_matrix_wide_uncertainties` (for example $2.135\times10^{-9}$ for the levels and $5.689\times10^{-9}$, relative, for the heat capacity).

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
| `ground_occupations_and_groups` | occupied levels, occupations, HOMO and LUMO groups | 300 | identical |
| `ground_energies` | $E_{KS}$, $E_{band}$, $E_{int}$ | 225 | 0.148 |
| `ground_homo_lumo_gap` | HOMO, LUMO, Kohn-Sham gap | 225 | 0.001 |
| `ground_eigenvalues` | every level present in both label sets | 9616 | 0.324 |
| `excited_delta_scf` | Delta-SCF energy, excited energy | 150 | 0.296 |
| `excited_particle_hole_lists` | particle-hole excitations | 4842 | 0.001 |
| `emt_integrals` | the five energy-momentum integrals | 375 | 0.225 |
| `emt_brane_tip_values` | $\rho$, $p_3$, $p_t$, $p_8$ at the brane and the tip | 600 | 0.495 |
| `ground_profiles` | ten profiles at 151 points | 113250 | 0.495 |
| `exchange_delta_E_x` | the exchange difference $\Delta E_x$ | 75 | 0.044 |
| `adiabatic_dE_da4` | $dE/da_4$ in two forms | 150 | 0.122 |
| `adiabatic_Q_max` | the adiabaticity measure and its pair | 225 | 0.314 |
| `exx_variant_scf` | the exact-exchange variant | 240 | 0.128 |
| `rescaling_partners` | the rescaling partners | 180 | 0.137 |
| `crossing_demonstration` | the level-crossing demonstration | 31 | 0.111 |
| `thermo_state_functions` | $\mu$, $E$, $S$, $F$, $\Omega$ in two forms | 810 | 0.284 |
| `thermo_derivatives` | $C_V$, $dE/dT$, $-dF/dT$ | 405 | 0.226 |
| `thermo_sea_hole_diagnostic` | the sea-hole diagnostic of the filling convention | 270 | 0.048 |
| `thermo_mu_high_precision` | $\mu$ recomputed with 40 digits, and $\Omega$ with it | 270 | 0.050 |

The other ten checks are preconditions and consistency tests: the three input reports pass every check (`inputs_all_pass`: at the time of the cross-check the reference report had 37 of 37, the Rust solver report 42 of 42 and the Rust determinism report 14 of 14); the canonical single runs reproduce the committed matrix (`rust_refinement_applies_to_matrix`, and its exact-exchange variant); both solvers solve the same problem and read the same theory file (`problem_definition_identical`); the reference re-derives the same particle numbers and couplings (`parameters_particle_numbers`, `parameters_couplings`); the floating-point chemical potentials lie within their rounding bounds (`thermo_mu_rounding_diagnostic`, Section 16.20); and the reference's own output is reproducible: the cross-check runs the reference a second time into a fresh folder and finds all 340 result files and the report byte for byte identical (`reference_outputs_lf_only`, `reference_manifest`, `reference_repeat_byte_identical`).

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

`RUST_PARAMS` and `REF_PARAMS` are the `parameters.json` files of the two solvers. The two programs name some constants differently (the tip cutoff is `L_tipCutoff` in one and `L` in the other), so `pairs` lists the names side by side. `differ` is built by a **list comprehension**, `[expression for ... in ... if condition]`, which collects the Rust name of every pair whose two values are not equal (`!=`); it must be empty. `same_theory` compares the SHA-256 fingerprints (a 64-character number computed from every byte of a file; two different files practically never have the same one) of the theory file that each solver read. The loop prints the nine pairs of values, the name padded to 13 characters (`:13s`). The check requires no difference and the same theory file, and names the cross-check's check `problem_definition_identical`, which it reproduces.

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

`check_reproduction` reads the committed file as text, compares its content with the new result, and also writes the new result as text exactly as the reference program writes its files (`json.dumps` with an indentation of one blank and only ASCII characters, plus a final line end) to report whether the two texts are identical byte for byte. It prints the number of numbers compared and that answer, then the first five differences, if any (`problems[:5]` is the first five entries of a list). The check requires no difference; its name gives the file name after `/results/` (`.split('/results/')[1]` cuts the path at that text and takes the second piece), and its record line names the cross-check's check `reference_repeat_byte_identical`, which made the same test for all files.

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

`classes` holds the 19 quantity classes of the validation, each with its number of elements and the largest ratio $|R_{123} - R_{234}|/U_{123}$; the loop prints them (Out [7]: from $0$ for the integral of $p_3$ to $0.787$ for $p_8$ at the tip). `max(classes, key=...)` finds the class with the largest ratio: the `key` is a **lambda**, a one-line function written in place, that gives each class name its ratio. `next(... for c in ... if ...)` takes the first check of the reference report whose name is `richardson_uncertainty_validated`, and `re.search` reads the number after the text `U123 = ` in its detail sentence: in the pattern, `[0-9.]+` means one or more digits or points, round brackets capture what they match (`.group(1)` returns it), `\(` and `\)` are literal brackets, and `\w+` is a word. The check requires every element of every class to lie within its $U_{123}$, 19 classes, the largest ratio at `p8_tip`, and our largest ratio equal to the one stated in the report within $5\times10^{-4}$.

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

For each ground state `eps` is the list of the level arrays on the three grids kept by the wrapper of In [4], and `RR.asym_ratio` (the reference's own function) computes the convergence ratio of Section 16.4 for every level whose two differences exceed $10^{-10}$ (smaller differences are dominated by rounding). `mine` collects the number of ratios, their **median** (the middle value when they are sorted; `np.median`), the smallest and the largest, and prints them. The check requires these four numbers to equal the ones the program stored in the entry `consistency` of the result, and the median to lie within $0.05$ of 4, the criterion of the reference's check `richardson_asymptotic_ratio`. Out [10] shows medians of $4.000053$, $4.000064$ and $4.000055$.

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

`rec` is the measurement of this state in `rust-refinement.json`. `level_diff` is the largest canonical-minus-refined difference over the levels present in both runs, and `e_diff` the difference of $E_{KS}$. The printed line (Out [13]) shows both and `worst`, which is exactly 0 in all five states. `same` asks whether these differences equal the recorded ones within $10^{-12}$; for thermal states the difference of $\mu$ must also agree. The first check reproduces the cross-check's check `rust_refinement_applies_to_matrix`: the canonical run gives exactly the committed results, so the measured differences apply to them. The second reproduces the state's entry of the measurement file. For example N688_lam0_a00 has $|x_c - x_r| = 7.529\times10^{-10}$ for $E_{KS}$, the number used in Section 16.6.

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

`occupied_rust` and `occupied_ref` are the sorted keys of the occupied levels of each solver. The Delta-SCF energy and the energy of the excited state are compared (the latter with the sum of the uncertainties of $E_{KS}$ and of the Delta-SCF energy). The printed line (Out [15]) shows how many levels each solver kept and how many were compared: the Rust solver keeps more levels than the reference (64 against 22 for N8_lamm2_a00), and every reference level has a Rust partner. The check requires the same occupied levels, reproducing the check `ground_occupations_and_groups`.

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

with a constant $M > 0$ (in the numbers $M = m = 1$, $L = 3$). Its exact levels are derived in this section (in the record: `Revision/kohn_sham/ks-theory.json`, `boundaryConditions.exactK0Spectra`, verified by check bc_exact_k0_spectra of `Revision/kohn_sham/reports/ks-theory-python.json`; status PROVED). Notebook 16b checks the derivation with the symbolic algebra package sympy and uses the levels to measure the errors of the reference's grid.

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

Rule: insert the two rotated matrices and collect the coefficients of $\sigma_2$ and $\sigma_3$. So the rotated operator has the same form, $j[-i\sigma_1\tfrac{d}{dy} + \phi' + m_2\sigma_2 + k_2\sigma_3] + v$, with the new mass $m_2$ and momentum term $k_2$. In the matrix, $j(\phi' + k_2) + v$ stands on the diagonal of the $u$ rows and $j(\phi' - k_2) + v$ on the diagonal of the $w$ rows ($\sigma_3$ is $+1$ on the first component and $-1$ on the second), and $M$ in the neighbour entries is replaced by $m_2$, taken at the half node of the pair so that the matrix stays symmetric. For even parity $\phi = 0$, and everything reduces to the matrix above, with $\pm jK + v$ on the diagonal. The reference chooses the angle $j\phi$ for block type $j$ so that the exact symmetry between the two block types at $k = 0$ survives on the grid: their levels agree exactly, to $0$ in the record (`Revision/kohn_sham/reports/ks-reference.json`, check `free_k0_block_type_symmetry`).

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

Rule: $\kappa a^2 = e^{-a_{4,0}}A^2e^{-Hy}e^{2My}$; integrate the exponential as for the normalisation; insert $A^2$ from Section 16.13. The theory file `Revision/kohn_sham/ks-theory.json` holds this formula under the name `checksNumeric.braneBandSlopeFormula`, and the record proves it in the check brane_band_slope of its Python report `Revision/kohn_sham/reports/ks-theory-python.json` (status PROVED). For $M = H = 1$ and $L = 3$ it gives:

$$
c(0) = \frac{2\,(1 - e^{-3})}{1 - e^{-6}} = \frac{2\cdot0.950213}{0.997521} = 1.905148 .
$$

Rule: insert the numbers; $e^{-3} = 0.049787$ and $e^{-6} = 0.002479$.

**The meaning of the factor $e^{-a_{4,0}}$.** The weight $\kappa = e^{-Hy - a_{4,0}}$ is one over the 3-space scale factor $e^{a_4}\sin^{1/6}z = e^{a_4 + Hy}$ (because $\sin z = e^{6Hy}$, so $\sin^{1/6}z = e^{Hy}$). Along the history $a_4 = AHx_4$ the 3-space scale factor grows while the three extra times deflate with $e^{-a_4}$ (the 7-volume stays constant), and the energy carried by a 3-momentum is redshifted by $e^{-a_{4,0}}$: the brane band flattens. From slice to slice ($\Delta a_{4,0} = 0.5$) the slope shrinks by the factor $e^{-0.5} = 0.6065$: $1.905148$, $1.155531$, $0.700865$, $0.425096$, $0.257834$. The reference's grid reproduces the formula to $2.6\times10^{-15}$, relative (`Revision/kohn_sham/reports/ks-reference.json`, check `free_brane_band_slope`).

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

`R18` and `U18` are the Richardson values and uncertainties of the 18 levels from $G = 300$, $600$, $1200$. `record` is the committed file `free-checks.json`; `rows` keeps its rows with $m = 1$, $L = 3$ and $j = +1$ (each row lists $m$, $L$, parity, $j$, rank, $R$, $U$, the exact level, $R$ minus exact, and the $G = 1200$ value minus exact). The first check confirms that these are our 18 rows in our order (`order` lists the pairs (parity, rank)). `dev_R`, `dev_U` and `dev_1200` are the largest differences between the record and our $R$, our $U$ and our $G = 1200$ errors. Out [11]: $8.9\times10^{-15}$, $1.3\times10^{-15}$ and $6.2\times10^{-15}$, so the second check (all below $10^{-12}$) reproduces the record. The Richardson values lie within $1.2\times10^{-14}$ of the exact levels, while the best single grid $G = 1200$ is $4.1\times10^{-5}$ away: two Richardson steps gain about nine digits. The third check requires $10^{-11}$, the criterion of the reference's check `free_k0_analytic_spectra`.

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

`save_figure` saves Figure 16b.6, and the printed line (Out [13]) gives the largest distances from 4: $6.57\times10^{-4}$, $1.64\times10^{-4}$ and $4.10\times10^{-5}$ for the triples $(150, 300, 600)$, $(300, 600, 1200)$ and $(600, 1200, 2400)$, each four times smaller than the one before, as the correction $\tfrac{15}{16}\tfrac{d}{c}h^2$ of Section 16.4 predicts. What the student should see: the 16 ratios of each triple lie close to 4, the finer triples closer, and the high levels deviate most. The check requires the middle triple within $0.01$ of 4 (the reference's criterion `free_convergence_order_two` asks for $[3.99, 4.01]$) and the finest triple closer still.

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

`formula` holds the exact slopes. `theory` is the committed theory file `ks-theory.json`, and `stated` its number `checksNumeric.braneBandSlope_M1_H1_L3_a0`, the slope at $a_{4,0} = 0$ written in the file. `rec_rows` are the rows of the record's entry brane_band_slope. The table of Out [14] prints, for each slice, the grid value, the formula and the record with fifteen decimals; at $a_{4,0} = 0$ the three agree to fourteen decimals, $1.90514825364486$, and at $a_{4,0} = 2$ all three read $0.257833778514766$.

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

`rel_formula` and `rel_record` are the largest relative differences from the formula and from the record: $3.8\times10^{-16}$ and $2.6\times10^{-15}$ (Out [14]). The line printed next shows the number written in `ks-theory.json`. The first check requires the grid slope to equal the formula to $10^{-11}$ and the formula at $a_{4,0} = 0$ to equal the stated number to $10^{-15}$, the reference's criterion `free_brane_band_slope`; the second reproduces the record's rows; the third confirms that from slice to slice the slope shrinks by exactly $e^{-0.5}$ (`np.allclose` with a relative tolerance $10^{-12}$; `R_slope[1:] / R_slope[:-1]` divides each slope by the one before).

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

### 16.20 How the cross-check caught a rounding error: the chemical potential

**What happened.** The first cross-check of the record compared a representative subset of the canonical matrix (18 of the 75 ground states and 8 of the 135 thermal states). It failed one check, `thermo_state_functions`, in one state, N8_lamm1_a00_T10: the Rust solver gave the chemical potential $\mu = 0.2100104489071649$ and the reference $0.2100104497343054$, a difference of $8.27\times10^{-10}$ against a tolerance of $7.97\times10^{-12}$, a ratio of about 104 (`Revision/kohn_sham/checker/README.md`, History 1). The tolerance was not widened. Instead the cause was found: the levels of both solvers were right, and the Rust solver's computation of $\mu$ from them was wrong in the tenth decimal, because of the way ordinary computer numbers round. This section explains every step of that diagnosis; Notebook 16c repeats it with numbers it computes itself.

**The Mermin condition and its slope, line by line.** At a temperature $T > 0$ the occupation of a level $\varepsilon_i$ is the Fermi-Dirac number $f(x_i)$ with $x_i = (\varepsilon_i - \mu)/T$ and $f(x) = 1/(1 + e^x)$, and each level holds $g_i$ states (its **degeneracy**; in this model $g = 4r_3(n_2)$, Chapter 15). The chemical potential is the root of the **Mermin condition**

$$
N(\mu) = \sum_i g_i\,f\Big(\frac{\varepsilon_i - \mu}{T}\Big) = N .
$$

How fast does $N(\mu)$ change with $\mu$?

$$
f'(x) = -\frac{e^x}{(1 + e^x)^2}.
$$

Rule: $f = (1 + e^x)^{-1}$ and the chain rule: the derivative of $u^{-1}$ is $-u^{-2}u'$, with $u' = e^x$.

$$
\frac{e^x}{(1 + e^x)^2} = \frac{1}{1 + e^x}\cdot\frac{e^x}{1 + e^x} = f(x)\,\big(1 - f(x)\big).
$$

Rule: split the fraction, and $1 - f = \tfrac{1 + e^x - 1}{1 + e^x} = \tfrac{e^x}{1 + e^x}$.

$$
\frac{dN}{d\mu} = \sum_i g_i\,f'(x_i)\,\frac{dx_i}{d\mu} = \frac{1}{T}\sum_i g_i\,f(x_i)\,\big(1 - f(x_i)\big).
$$

Rule: the chain rule with $dx_i/d\mu = -1/T$, and $f' = -f(1 - f)$. Every term is positive, so $N(\mu)$ increases with $\mu$ and has at most one root. As $\mu$ goes to $-\infty$ every $f$ tends to 0, and as $\mu$ goes to $+\infty$ every $f$ tends to 1, so if the levels hold more than $N$ states the root exists (intermediate value theorem). We write $N' = dN/d\mu$.

**The activated regime, line by line.** In N8_lamm1_a00_T10 the eight quanta exactly fill the two lowest levels, $\varepsilon_0 = 0.000245562708$ (two levels of 4 states each, $g_0 = 8$ together); the next level is $\varepsilon_1 = 0.430761462627$ with $g_1 = 24$ states (Notebook 16c, Out [2]). The **gap** between them, $0.4305$, is 43 times the temperature $T = 0.01$. When a gap is many times $T$ the state is in the **activated regime**: only very few quanta are thermally lifted across it. Write $H$ for the **thermal holes**, the missing quanta below $\mu$, and $P$ for the **thermal particles** above it:

$$
H = g_0\,\big(1 - f(x_0)\big) = \frac{g_0}{1 + e^{(\mu - \varepsilon_0)/T}} \approx g_0\,e^{-(\mu - \varepsilon_0)/T}, \qquad P = g_1\,f(x_1) \approx g_1\,e^{-(\varepsilon_1 - \mu)/T}.
$$

Rule: $1 - f(x) = 1/(1 + e^{-x})$, and $1/(1 + e^{s}) \approx e^{-s}$ when $s$ is large (here $s \approx 21$, so the error is a relative $e^{-21} \approx 10^{-9}$). Since $g_0 = N$, the Mermin condition $g_0(1 - H/g_0) + P = N$ says simply $P = H$: as many quanta above the gap as are missing below it. Taking logarithms of $g_0\,e^{-(\mu - \varepsilon_0)/T} = g_1\,e^{-(\varepsilon_1 - \mu)/T}$:

$$
\ln g_0 - \frac{\mu - \varepsilon_0}{T} = \ln g_1 - \frac{\varepsilon_1 - \mu}{T} \quad\Longrightarrow\quad \mu = \frac{\varepsilon_0 + \varepsilon_1}{2} - \frac{T}{2}\,\ln\frac{g_1}{g_0}.
$$

Rule: $\ln(ge^{-s}) = \ln g - s$; collect the terms with $\mu$ ($2\mu/T$ on one side) and solve. With the numbers, $(\varepsilon_0 + \varepsilon_1)/2 = 0.215503513$ and $\tfrac T2\ln3 = 0.005493061$, so $\mu \approx 0.210010451$: $\mu$ sits near the middle of the gap, shifted a little towards the lower level because the upper level has three times more states. (This simple estimate is within $1.5\times10^{-9}$ of the exact root; Exercise 7 finds the small correction.) Then

$$
N' = \frac{1}{T}\sum_i g_i f_i(1 - f_i) \approx \frac{H + P}{T} = \frac{2H}{T} = \frac{2\cdot6.21\times10^{-9}}{0.01} = 1.24\times10^{-6}.
$$

Rule: for a full level $f(1 - f) \approx 1 - f$, for an empty level $f(1 - f) \approx f$; then $P = H$, and $H = 6.21\times10^{-9}$ (Notebook 16c, Out [3]). So $N(\mu)$ is extremely flat: moving $\mu$ by $10^{-9}$ changes $N(\mu)$ by only $1.2\times10^{-15}$. Conversely, an error $\delta$ in a computed value of $N(\mu) - N$ moves the computed root by $\delta/N'$, about $8\times10^{5}$ times $\delta$ (the root of the tangent line moves by the error divided by the slope). The problem is **ill-conditioned**: its answer reacts strongly to small errors of its input.

**Numbers in a computer.** A **double**, the ordinary number of a computer, is stored as a sign, 53 binary digits and an exponent (the IEEE 754 standard). Between two neighbouring powers of two, $2^k \le x < 2^{k+1}$, the doubles are equally spaced, $2^{k-52}$ apart. Between 1 and 2 the spacing is $2^{-52} = 2.2\times10^{-16}$, the **machine epsilon** $\epsilon_{mach}$; between 4 and 8 it is $2^{-50} = 8.9\times10^{-16}$; between 8 and 16 it is $2^{-49} = 1.8\times10^{-15}$. The result of every operation is **rounded** to the nearest double. A sum whose exact value is close to 8 can therefore come out only as a multiple of $2^{-50}$ (just below 8) or of $2^{-49}$ (just above 8).

**The staircase, line by line.** Near its root the exact sum is $S(\mu) = 8 + N'\,(\mu - \mu_{root})$. Added up directly in doubles, the computed residual $D(\mu) = S(\mu) - 8$ is exactly zero whenever the computed sum is the double 8 itself, and that happens whenever $S$ lies within half a spacing of 8:

$$
8 - 2^{-51} \le S(\mu) \le 8 + 2^{-50}.
$$

Rule: rounding to the nearest double; half the spacing below 8 is $\tfrac12 2^{-50} = 2^{-51}$, half the spacing above is $\tfrac12 2^{-49} = 2^{-50}$.

$$
\Delta\mu = \frac{2^{-51} + 2^{-50}}{N'} = \frac{3\cdot2^{-51}}{N'} = \frac{1.33\times10^{-15}}{1.242\times10^{-6}} = 1.07\times10^{-9}.
$$

Rule: an interval of length $3\cdot2^{-51}$ in $S$ is an interval of length $3\cdot2^{-51}/N'$ in $\mu$, because $S$ changes by $N'$ per unit of $\mu$. So in the computer the direct residual is a **staircase**: constant over intervals of about $10^{-9}$ in $\mu$, jumping by one spacing between them, and exactly zero over a whole interval about $10^{-9}$ wide. Notebook 16c measures this interval as $1.05\times10^{-9}$ wide, from $8.25\times10^{-10}$ below the root to $2.30\times10^{-10}$ above it; its position is shifted from the ideal one by the rounding of the individual terms of the sum (Figure 16c.2).

**Why bisection then stops at the wrong place.** Bisection on the residual asks at each midpoint only one question: is $D(mid) < 0$? If yes, the root is above $mid$; if not, at or below it. On the zero interval the answer is always "not below zero", so every midpoint inside it becomes the new upper end, and the search converges to the **left end** of the zero interval, about $8.3\times10^{-10}$ below the true root. That is the faulty value of the first cross-check: Notebook 16c reproduces $0.2100104489071649$ in all sixteen digits by bisection on the direct sum (In [7]). The record's Rust solver now writes for every thermal state the root that the former direct count would give on the same final levels, minus the present $\mu$, in the column `mu_direct_count_minus_mu` of `Revision/kohn_sham/results/thermo/thermodynamics.csv`; for N8_lamm1_a00_T10 it is $-8.267\times10^{-10}$.

**Deciding which value is right: 40 digits and Newton's method.** To decide, the checker recomputed $\mu$ from each solver's own final levels with 40 significant digits, using the package mpmath, which computes with as many digits as one asks for (slowly, in software). With 40 digits the rounding of the sum is about $10^{-40}N$, which moves the root by about $10^{-40}N/N' < 10^{-33}$: far below anything a double can hold. The root is found by **Newton's method**. Line by line: let $\mu_k$ be a guess.

$$
N(\mu) \approx N(\mu_k) + N'(\mu_k)\,(\mu - \mu_k).
$$

Rule: near $\mu_k$ a smooth function is close to its tangent line (Taylor's theorem to first order).

$$
N(\mu_k) + N'(\mu_k)\,(\mu_{k+1} - \mu_k) = N \quad\Longrightarrow\quad \mu_{k+1} = \mu_k - \frac{N(\mu_k) - N}{N'(\mu_k)}.
$$

Rule: the next guess is where the tangent line reaches the value $N$; subtract $N(\mu_k)$ and divide by $N'(\mu_k)$.

**Why Newton's method doubles the digits, line by line.** Let $e_k = \mu_k - \mu^*$ be the error of the guess, $\mu^*$ the root, and write $N'$, $N''$ for the derivatives at $\mu^*$.

$$
N(\mu_k) - N = N'e_k + \tfrac12N''e_k^2 + \dots, \qquad N'(\mu_k) = N' + N''e_k + \dots
$$

Rule: Taylor's theorem around $\mu^*$, with $N(\mu^*) = N$.

$$
e_{k+1} = e_k - \frac{N'e_k + \tfrac12N''e_k^2}{N' + N''e_k} = e_k - e_k\Big(1 + \tfrac12\tfrac{N''}{N'}e_k\Big)\Big(1 - \tfrac{N''}{N'}e_k\Big) + \dots = \frac{N''}{2N'}\,e_k^2 + \dots
$$

Rule: subtract $\mu^*$ from Newton's formula; take $N'e_k$ out of the numerator and $N'$ out of the denominator; $1/(1 + s) = 1 - s + \dots$; multiply out, keeping terms up to $e_k^2$. The new error is proportional to the square of the old one (**quadratic convergence**): once the error is small, the number of correct digits roughly doubles at every step. Notebook 16c (Out [4]) starts in the middle of the gap and shows the distances $5.5\times10^{-3}$, $4.9\times10^{-4}$, $4.0\times10^{-7}$, $2.1\times10^{-16}$ and $1.5\times10^{-34}$.

**The diagnosis.** The 40-digit root on the Rust levels is $0.21001044973390364544$ and on the reference levels $0.21001044973430543050$; they differ by $4.0\times10^{-13}$, which is how much the two solvers' levels differ (each is uncertain by about $10^{-12}$). The faulty Rust value was $8.3\times10^{-10}$ below both. So the levels were right and the root-finding was wrong (the cross-check's check `thermo_mu_high_precision` now compares these roots in all 270 level sets, worst ratio $0.050$: `Revision/kohn_sham/reports/ks-crosscheck.json`). The reference had had the same defect: in its first complete run its $\mu$ missed its own 40-digit root by $1.15\times10^{-9}$ in the same state (`Revision/kohn_sham/reference/README.md`, History); it was repaired in the same way.

**Why the measured uncertainty did not warn.** Before the repair the canonical and the refined Rust runs computed $\mu$ with the same direct count, so both made almost the same rounding error, and their difference, from which $U_{Rust}$ is measured (Section 16.6), did not contain it. An uncertainty measured by repeating a computation measures only the errors that the repetition changes. After the repair the refined run computes the root with a second, exactly equivalent form whose rounding takes a different path, so that their difference now contains the rounding error of the root (`Revision/kohn_sham/reports/ks-rust-determinism.json`, check `refined_mermin_root_path`). This is the deeper lesson of the episode, and the reason why a truly independent program is worth the effort.

**The repair: a well-conditioned form, line by line.** The trouble is that the direct sum adds numbers of size 1 (the full occupations) to get a total near 8 and then subtracts 8, so its rounding errors are of size $\epsilon_{mach}\cdot8$, while the interesting part, $P - H$, is about $10^{-9}$ in size. The repair rewrites the residual exactly so that the large numbers are added only as whole numbers. Split the levels into those below $\mu$ ($x_i < 0$) and those above ($x_i \ge 0$).

$$
f(x) + f(-x) = \frac{1}{1 + e^x} + \frac{1}{1 + e^{-x}} = \frac{1}{1 + e^x} + \frac{e^x}{e^x + 1} = 1 .
$$

Rule: multiply the numerator and the denominator of the second fraction by $e^x$; then the two fractions have the same denominator.

$$
\sum_i g_i f(x_i) - N = \sum_{\text{below}} g_i\big(1 - f(-x_i)\big) + \sum_{\text{above}} g_i f(x_i) - N .
$$

Rule: below $\mu$ write each occupation as $f(x_i) = 1 - f(-x_i)$.

$$
W(\mu) = \Big(\sum_{\text{below}} g_i - N\Big) - \sum_{\text{below}} g_i\,f(-x_i) + \sum_{\text{above}} g_i\,f(x_i) = -d - H + P .
$$

Rule: collect the terms; $d = N - \sum_{\text{below}}g_i$ is a whole number, $H$ the thermal holes and $P$ the thermal particles. The value of $W$ is exactly that of the direct residual; only the rounding differs. The bracket $d$ is a sum of whole numbers, which doubles add without any error. $H$ and $P$ are sums of small positive numbers, each computed with a relative error of about $\epsilon_{mach}$, so near the root $W$ is known to about $\epsilon_{mach}(P + H)$, here a few times $10^{-24}$, instead of $\epsilon_{mach}\cdot8$. The reference solver's module uses exactly this form (`mermin_residual` in `Revision/kohn_sham/reference/ks_fd.py`); the Rust solver uses its logarithm, $\ln(P + d_-) - \ln(H + d_+)$ with $d_\pm = \max(\pm d, 0)$, which is nearly a straight line in $\mu$ (the form LogBalance of `Revision/kohn_sham/solver/src/mermin.rs`), and its refined run uses the linear form (LinearDeviation).

**The rounding bounds, line by line.** How large can the error of a computed root be?

$$
N'\,(\mu_c - \mu^*) + \delta R = 0 \quad\Longrightarrow\quad |\mu_c - \mu^*| = \frac{|\delta R|}{N'} .
$$

Rule: near the root the computed residual is the tangent line plus its rounding error $\delta R$, and the computed root $\mu_c$ is where it vanishes. A sum of $n$ terms in doubles has a rounding error of at most about $n\,\epsilon_{mach}$ times the size of the terms. For the direct sum the terms add up to $N$, so $|\delta R| \lesssim n\,\epsilon_{mach}N$; for the well-conditioned form they add up to $P + H + |d|$. The Rust solver's documentation states the complete first-order bounds with generous constants (`Revision/kohn_sham/solver/src/mermin.rs`, its header; $n$ the number of levels, $g_{max}$ the largest degeneracy, $\langle|\varepsilon - \mu|\rangle$ the mean distance of the levels from $\mu$ weighted with $gf(1 - f)$, and $L_A = \max(|\ln(P + d_-)|, |\ln(H + d_+)|)$):

$$
B_{direct} = \epsilon_{mach}\Big[(n + 2)\,\frac{N}{N'} + 3\,\langle|\varepsilon - \mu|\rangle + T(\ln g_{max} + 3) + 2|\mu|\Big],
$$

$$
B_{well} = \epsilon_{mach}\Big[(n + 2 + L_A)\,\frac{P + H + |d|}{N'} + 3\,\langle|\varepsilon - \mu|\rangle + T(\ln g_{max} + 3) + 2|\mu|\Big].
$$

The extra terms count the rounding of the arguments $x_i$, of the logarithms and of the returned double. For N8_lamm1_a00_T10 ($n = 7$ Rust levels, $N' = 1.242072\times10^{-6}$) the first term of $B_{direct}$ is $9\cdot2.22\times10^{-16}\cdot8/1.242\times10^{-6} = 1.29\times10^{-8}$, and the record states $B_{direct} = 1.287\times10^{-8}$ and $B_{well} = 3.154\times10^{-16}$ (`Revision/kohn_sham/reports/ks-rust-mermin-roots.json`, state N8_lamm1_a00_T10). The faulty error, $8.27\times10^{-10}$, lies well inside $B_{direct}$: it is about $0.58$ of the shift $\epsilon_{mach}N/N' = 1.43\times10^{-9}$ that a single rounding of the size $\epsilon_{mach}N$ causes. The repaired Rust value differs from the 40-digit root by $2.5\times10^{-17}$ (same report, muRun_minus_root), inside $B_{well}$; over all 135 thermal states the repaired $\mu$ lies within its bound (same report, check `solver_mu_within_rounding_bound`), and in the cross-check the largest distance of a Rust $\mu$ from the 40-digit root on its own levels is $6.7\times10^{-16}$ (`Revision/kohn_sham/reports/ks-crosscheck.json`, check `thermo_mu_rounding_diagnostic`).

**Where the danger lies.** The bound $B_{direct}$ is large only where $N'$ is tiny, that is, where a gap is many times $T$. Among the 45 thermal states with $N = 8$ this happens only at the first slice and the lowest temperature, where the bound reaches $10^{-8}$; along the history 3-space inflates while the extra times deflate, the 3-momenta are redshifted by $e^{-a_{4,0}}$, the levels above the gap move down, the gap closes, $N'$ grows, and the bound falls to about $10^{-15}$ (Figure 16c.5). The three states with the largest direct-sum errors are the three couplings at $a_{4,0} = 0$ and $T = 0.01$: $-8.27\times10^{-10}$, $+2.72\times10^{-10}$ and $+6.96\times10^{-11}$ (Notebook 16c, Out [11]; the same numbers are in `Revision/kohn_sham/reports/ks-rust-solver.json`, check `thermo_mu_well_conditioned_root`).

**Status.** PROVED: the slope formula, the uniqueness of the root, the exact rewriting $W = -d - H + P$, Newton's formula and its quadratic convergence; the rounding bounds are first-order estimates derived in the Rust documentation and confirmed against 40-digit roots for every thermal state (check `solver_mu_within_rounding_bound`). COMPUTED: every number of this section, from the records named with it and reproduced by Notebook 16c.

### 16.21 Example: the Mermin root (Notebook 16c)

Notebook 16c reconstructs the diagnosis and the repair from the records. For N8_lamm1_a00_T10 it reads the final levels of both solvers, computes $\mu$ with 40 digits by Newton's method, evaluates the direct residual in doubles near the root and shows the staircase, reproduces the faulty value of the first cross-check by bisection on the direct sum and the correct value by bisection on the well-conditioned form, and evaluates the rounding bounds. Then it repeats the 40-digit comparison of the cross-check for all 45 thermal states with eight quanta, for the levels of both solvers, and reproduces the recorded roots, bounds, tolerances and ratios. It needs no Rust, runs in about half a minute, draws six figures and ends with the line ALL 26 CHECKS PASSED (notebook 16c).

<!-- NOTEBOOK 16c -->

### 16.24 Line-by-line walk-through of Notebook 16c

The notebook has 15 code cells, In [1] to In [15]; the numbers they print are in Section 16.23.

**In [1], the set-up cell.** As in Notebook 16b, it is the set-up cell of Notebook 16a (Section 16.12) without the Rust helper; its comment lines repeat the run instructions of Section 16.22, and its name line is

```python
NOTEBOOK_ID = "16c"  # this notebook: chapter 16, example c
```

**In [2], the levels of N8_lamm1_a00_T10 and the history.**

```python
import csv  # reads tables stored as CSV files (comma-separated values)
import math  # functions of single numbers (isqrt, log10, ...)
import re  # finds patterns in text (used to read numbers out of sentences)
import sys  # the list of folders in which Python looks for modules
from functools import lru_cache  # remembers the results of a function

import mpmath as mp  # numbers with as many digits as we ask for
import numpy as np  # arrays of numbers

KS = "Revision/kohn_sham"  # the folder of the Kohn-Sham record (repository path)
STATE = "N8_lamm1_a00_T10"  # the state in which the first cross-check failed
EPS_MACH = 2.0 ** -52  # machine epsilon: neighbouring doubles near 1 differ by this
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
           "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
```

Besides the modules of Notebook 16a, `math` gives functions of single numbers (here `isqrt`, the whole-number square root, `log`, `log10` and `ulp`), and `lru_cache` from the module `functools` makes a function remember its results. `mpmath`, called `mp`, computes with as many digits as one asks for. `STATE` is the state of the failed comparison, and `EPS_MACH` is the machine epsilon $2^{-52}$ (`**` is the power).

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

The two reading functions of Notebook 16a (Section 16.12, In [2]).

```python
@lru_cache(maxsize=None)
def r3(n2):
    """The number of whole-number points (a, b, c) with a^2 + b^2 + c^2 = n2."""
    R = math.isqrt(n2) + 1  # no coordinate can be larger than this
    return sum(1 for a in range(-R, R + 1) for b in range(-R, R + 1)
               for c in range(-R, R + 1) if a * a + b * b + c * c == n2)
```

`r3(n2)` counts the points $(a, b, c)$ with whole-number coordinates and $a^2 + b^2 + c^2 = n_2$, the number $r_3(n_2)$ of Chapter 15. No coordinate can be larger than $\sqrt{n_2}$, so the three nested ranges from $-R$ to $R$ with $R = \lfloor\sqrt{n_2}\rfloor + 1$ cover all candidates, and `sum(1 for ... if ...)` counts those that satisfy the equation. The line `@lru_cache(maxsize=None)` above the function is a **decorator**: it wraps the function so that a result, once computed for some $n_2$, is remembered and returned at once the next time.

```python
RUST_MU = {r["id"]: float(r["mu"])
           for r in read_csv(f"{KS}/results/thermo/thermodynamics.csv")}
REFINEMENT = {s["id"]: s for s in read_json(f"{KS}/checker/rust-refinement.json")
              ["states"] if s["kind"] == "thermo"}
```

`RUST_MU` files the committed Rust chemical potentials of all thermal states under their ids (from the column mu of `thermodynamics.csv`). `REFINEMENT` files the thermal entries of the cross-check's measurement file `rust-refinement.json`; each holds, among other things, the final levels and degeneracies of the canonical Rust run, from which the checker computed its 40-digit roots.

```python
def state_data(sid):
    """Everything this notebook needs about one thermal state, from the records."""
    rust = REFINEMENT[sid]  # the Rust run with the canonical numerics
    ref = read_json(f"{KS}/reference/results/thermo/{sid}.json")
    T, N = rust["canonical_T_N"]
    return {"id": sid, "T": T, "N": N,
            "eps_rust": np.array([e for e, g in rust["canonical_levels_eps_deg"]]),
            "g_rust": np.array([g for e, g in rust["canonical_levels_eps_deg"]]),
            "eps_ref": np.array(ref["levels"]["eps"]),
            "g_ref": np.array([4.0 * r3(k[0]) for k in ref["levels"]["keys"]]),
            "keys_ref": ref["levels"]["keys"],
            "U_levels_ref": max(ref["levels"]["U"]),  # largest level uncertainty
            "mu_rust": RUST_MU[sid], "mu_ref": ref["thermo"]["mu"]["value"],
            "U_mu_ref": ref["thermo"]["mu"]["U"]}
```

`state_data(sid)` collects everything the notebook needs about one thermal state: $T$ and $N$; the Rust levels and degeneracies (two list comprehensions over the pairs (energy, degeneracy)); the reference levels from its result file, with the degeneracies computed as $4r_3(n_2)$ from each level's shell (`k[0]` is the first entry of the level's key); the keys; the largest level uncertainty of the reference; and the committed $\mu$ of both solvers with the reference's uncertainty of $\mu$.

```python
S = state_data(STATE)
print(" i  key (n2:j:parity:rank)   g   eps reference        eps Rust")
for i, key in enumerate(S["keys_ref"]):
    rust = f"{S['eps_rust'][i]:.15f}" if i < len(S["eps_rust"]) else "(not kept)"
    print(f"{i:2d}  {key[0]}:{key[1]:+d}:{key[2]}:{key[3]}"
          f"{'':12s}{S['g_ref'][i]:3.0f}   {S['eps_ref'][i]:.15f}   {rust}")
common = len(S["eps_rust"])  # the Rust label set keeps one level fewer
say(f"T = {S['T']}, N = {S['N']}; committed mu: Rust {S['mu_rust']!r}, reference "
    f"{S['mu_ref']!r}")
check(np.array_equal(S["g_rust"], S["g_ref"][:common])
      and np.max(np.abs(S["eps_rust"] - S["eps_ref"][:common])) < 1e-11,
      "both solvers have the same levels (to 1e-11) and degeneracies")
check(np.sum(S["g_rust"][S["eps_rust"] < 0.2]) == S["N"],
      "the eight particles exactly fill the two levels below the gap")
```

`S` holds the data of N8_lamm1_a00_T10. The table of Out [2] prints each reference level with its key, degeneracy and energy, and the Rust level next to it (the braces with an empty text and the format `12s` print twelve blanks; `{key[1]:+d}` prints the block type with its sign); the reference keeps one level more than the Rust solver (`"(not kept)"`). The first check requires the same degeneracies and levels that agree to $10^{-11}$; they agree to about $10^{-12}$. The second requires that the levels below $0.2$ hold exactly the eight quanta: the two levels at $0.000245562708$ with 4 states each.

```python
checker_history = repository_file(f"{KS}/checker/README.md").read_text(
    encoding="utf-8")
found = re.search(r"Rust.s mu was ([0-9.]+) and the reference.s\s+([0-9.]+) "
                  r"\(\|diff\| ([0-9.e-]+) against a tolerance of ([0-9.e-]+)\)",
                  checker_history)
MU_OLD_RUST, MU_OLD_REF, DIFF_OLD, TOL_OLD = (float(x) for x in found.groups())
reference_history = repository_file(f"{KS}/reference/README.md").read_text(
    encoding="utf-8")
REF_OLD_MISS = float(re.search(r"this mu differed by ([0-9.e-]+) from the 40-digit",
                               reference_history).group(1))
say(f"history: Rust mu {MU_OLD_RUST!r}, reference mu {MU_OLD_REF!r}, |diff| "
    f"{DIFF_OLD:.3g}, tolerance {TOL_OLD:.3g}; reference first run missed its root "
    f"by {REF_OLD_MISS:.3g}")
check(abs(MU_OLD_RUST - MU_OLD_REF) - DIFF_OLD < 5e-13 and DIFF_OLD > TOL_OLD,
      "the recorded difference exceeds the recorded tolerance",
      record=f"{KS}/checker/README.md, History 1")
```

The numbers of the history are read from the two README files with regular expressions, so that the notebook uses the recorded values, not copies typed by hand. In the first pattern a point `.` matches any single character (here the apostrophe of the words "Rust's" and "reference's"), `\s+` one or more blanks or line breaks (the README breaks this sentence across two lines), `\(` and `\|` a literal bracket and vertical bar, and each `(...)` captures a number; `found.groups()` returns the four captured texts, which the **generator** `(float(x) for x in ...)` turns into four numbers given four names at once. The second pattern reads how far the reference's first complete run missed its own root. Out [2] prints the history: Rust $\mu = 0.2100104489071649$, reference $\mu = 0.2100104497343054$, difference $8.27\times10^{-10}$, tolerance $7.97\times10^{-12}$; the reference's first run missed its root by $1.15\times10^{-9}$. The check confirms that the recorded difference is the difference of the two recorded values (to $5\times10^{-13}$, the rounding of the printed digits) and exceeds the tolerance.

**In [3], the state as a picture (Figure 16c.1).**

```python
sys.dont_write_bytecode = True  # do not write a __pycache__ folder into the record
sys.path.insert(0, str(repository_file(f"{KS}/reference")))  # Python looks here too
import ks_fd as K  # noqa: E402  the reference solver's module (Revision code)
```

The reference module `ks_fd` is imported as `K`, as in Notebook 16b.

```python
eps, g, T, N = S["eps_ref"], S["g_ref"], S["T"], S["N"]
mu = S["mu_ref"]
x = (eps - mu) / T
below = eps < mu
holes = g * K.fermi(-x)  # g (1 - f): f(-x) = 1 - f(x), computed without subtracting
particles = g * K.fermi(x)  # g f
```

With the reference levels and committed $\mu$, `x` holds the arguments $(\varepsilon_i - \mu)/T$ and `below` marks the levels below $\mu$. `K.fermi` is the reference's Fermi function; it computes $e^{-|x|}$ first and returns $e^{-|x|}/(1 + e^{-|x|})$ for $x > 0$ and $1/(1 + e^{-|x|})$ otherwise, so it never computes the exponential of a large positive number, which would overflow. `holes` are $g(1 - f) = g\,f(-x)$, computed directly as $f(-x)$ and never as a subtraction $1 - f$ (which would lose all digits for a full level), and `particles` are $g\,f$.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 4.2))
energies = np.linspace(-0.05, 1.0, 2001)
left.plot(energies, K.fermi((energies - mu) / T), color=PALETTE[0], lw=1.8,
          label="occupation $f((\\varepsilon - \\mu)/T)$")
for e in np.unique(eps):  # one dotted line per energy, labelled with its states
    left.axvline(e, color="k", lw=0.8, ls=":")
    states = g[eps == e]
    label = (f"g = {states[0]:.0f}" if len(states) == 1
             else f"{len(states)} levels, g = {states[0]:.0f} each")
    left.text(e + 0.008, 0.08, label, rotation=90, fontsize=8)
left.axvline(mu, color=PALETTE[1], lw=1.4, ls="--", label=f"$\\mu = {mu:.6f}$")
left.annotate("", (eps[2], 1.12), (eps[1], 1.12), arrowprops={"arrowstyle": "<->"})
left.text(0.5 * (eps[1] + eps[2]), 1.15, "gap $= 43\\,T$", ha="center")
left.set_ylim(-0.05, 1.25)
left.set_xlabel("energy $\\varepsilon$ (units of $m$)")
left.set_ylabel("occupation $f$")
left.set_title("N8_lamm1_a00_T10: levels and occupation")
left.legend(fontsize=8, loc="center right", framealpha=1.0)
```

The left panel draws the occupation $f((\varepsilon - \mu)/T)$ on 2001 energies from $-0.05$ to $1$, a dotted vertical line at each distinct level (`np.unique`), labelled with its degeneracy, turned by 90 degrees (two levels share the lowest energy, so their label says "2 levels, g = 4 each"), $\mu$ as a dashed orange line, and a double arrow over the gap between the levels number 1 and 2 with the text "gap $= 43\,T$".

```python
right.semilogy(eps[below], holes[below], "v", color=PALETTE[1], ms=9,
               label=f"holes $g(1-f)$, sum {np.sum(holes[below]):.3e}")
right.semilogy(eps[~below], particles[~below], "^", color=PALETTE[0], ms=9,
               label=f"particles $g f$, sum {np.sum(particles[~below]):.3e}")
right.axvline(mu, color=PALETTE[1], lw=1.4, ls="--")
right.set_xlabel("energy $\\varepsilon$ (units of $m$)")
right.set_ylabel("thermal holes and particles")
right.set_title("the balance that fixes $\\mu$")
right.legend(fontsize=8, loc="upper right")
fig.tight_layout()
```

The right panel draws the holes of the levels below $\mu$ (triangles pointing down) and the particles of the levels above it (triangles up) on a logarithmic axis, with their sums in the legend.

```python
save_figure(fig, "levels_and_occupations",
            "The thermal Kohn-Sham state N8_lamm1_a00_T10 ($N = 8$, $\\lambda = "
            "-\\lambda_1$, $a_{4,0} = 0$, $T = 0.01\\,m$) of the reference solver. "
            "Left: the Fermi-Dirac occupation against the energy in units of $m$, "
            "with the levels as dotted lines and their degeneracies $g$; the two "
            "lowest levels hold the eight particles, the next level lies 43 times "
            "$T$ higher, and $\\mu$ (dashed) sits in the middle of this gap. Right: "
            "the thermal holes of the full levels and the thermal particles of the "
            "empty ones on a logarithmic axis; both sums are about $6 \\times "
            "10^{-9}$ and cancel, which is the Mermin condition.")
```

`save_figure` saves Figure 16c.1. What the student should see: on the left, the occupation is a step from 1 to 0 about $T = 0.01$ wide, centred at $\mu = 0.210010$, in the middle of a gap 43 times wider; the two lowest levels lie at the top of the step, all others at the bottom. On the right, the holes of the lowest levels and the particles of the level at $0.43$ are both about $6\times10^{-9}$; the particles of the higher levels fall off steeply ($10^{-15}$, $10^{-20}$, ...), because each level's particles shrink by $e^{-\Delta\varepsilon/T}$.

```python
balance = np.sum(holes[below]) - np.sum(particles[~below])
say(f"holes {np.sum(holes[below]):.6e}, particles {np.sum(particles[~below]):.6e}, "
    f"difference {balance:.2e}")
check(abs(balance) < 1e-15 and np.sum(g[below]) == N,
      "at the committed mu the thermal holes and particles balance (to 1e-15)")
```

`balance` is the holes minus the particles; Out [3] prints both, $6.210359\times10^{-9}$, and their difference, $-6.6\times10^{-24}$. The check requires a balance below $10^{-15}$ and the levels below $\mu$ to hold exactly $N$ states: the Mermin condition in the form $P = H$ of Section 16.20.

**In [4], the root with 40 digits: Newton's method.**

```python
mp.mp.dps = 40  # every mpmath number now carries 40 significant digits
```

`mp.mp.dps = 40` sets the working precision of mpmath to 40 decimal places (significant digits) for every following computation.

```python
def mermin_root_40(eps, g, N, T, start):
    """Newton's method for the root mu of sum g f((eps - mu)/T) = N with 40 digits.
    Returns (the root, dN/dmu there, the list of all guesses)."""
    E = [mp.mpf(float(e)) for e in eps]  # the levels, exactly the given doubles
    G = [mp.mpf(float(x)) for x in g]
    T40, N40, mu = mp.mpf(float(T)), mp.mpf(float(N)), mp.mpf(float(start))
    guesses = [mu]
    for _ in range(60):
        total, slope = mp.mpf(0), mp.mpf(0)
        for e, gi in zip(E, G):
            x = (e - mu) / T40
            if x > 2000:  # f < e^(-2000): invisible even with 40 digits
                continue
            f = 1 / (1 + mp.exp(x))
            total += gi * f  # N(mu)
            slope += gi * f * (1 - f) / T40  # dN/dmu
        step = (total - N40) / slope  # where the tangent line reaches N
        mu -= step
        guesses.append(mu)
        if abs(step) < mp.mpf(10) ** -32:  # the first 32 digits are settled
            break
    return mu, slope, guesses
```

`mermin_root_40` is Newton's method of Section 16.20 in 40-digit numbers. `mp.mpf(float(e))` turns each level into an mpmath number exactly equal to the given double (no digit is invented or lost). The loop makes at most 60 steps. In each it adds up $N(\mu)$ (`total`) and $N'(\mu) = \sum g f(1 - f)/T$ (`slope`) over the levels, skipping levels with $x > 2000$, whose occupation $e^{-2000}$ is invisible even with 40 digits. `step` is $(N(\mu) - N)/N'(\mu)$, and the new guess is $\mu$ minus the step; every guess is kept. The loop stops when a step is below $10^{-32}$ (`mp.mpf(10) ** -32`): then the first 32 digits are settled. The function returns the root, the slope there and all guesses.

```python
start = 0.5 * (S["eps_rust"][1] + S["eps_rust"][2])  # the middle of the gap
ROOT_R, SLOPE_R, NEWTON_PATH = mermin_root_40(S["eps_rust"], S["g_rust"], 8, 0.01,
                                              start)
ROOT_F, SLOPE_F, _ = mermin_root_40(S["eps_ref"], S["g_ref"], 8, 0.01, start)
print("Newton steps from the middle of the gap (Rust levels):")
for k, guess in enumerate(NEWTON_PATH):
    distance = mp.nstr(abs(guess - ROOT_R), 3)  # from the final root
    print(f"  mu_{k} = {mp.nstr(guess, 34)}   distance {distance}")
report("40-digit root on the Rust levels", mp.nstr(ROOT_R, 30))
report("40-digit root on the reference levels", mp.nstr(ROOT_F, 30))
report("dN/dmu at the root (Rust levels)", mp.nstr(SLOPE_R, 7))
```

Newton's method starts in the middle of the gap, at $(\varepsilon_1 + \varepsilon_2)/2$ of the Rust levels (positions 1 and 2 of the list), and is run on the Rust and on the reference levels. The loop prints every guess with 34 digits and its distance from the final root (`mp.nstr(x, n)` writes $x$ with $n$ significant digits): the distances $5.49\times10^{-3}$, $4.93\times10^{-4}$, $3.99\times10^{-7}$, $2.12\times10^{-16}$, $1.48\times10^{-34}$ and 0 show the doubling of the correct digits (Out [4]). The three RESULT lines give the two roots with 30 digits and $N' = 1.242072\times10^{-6}$.

```python
fixture = next(s for s in read_json(f"{KS}/solver/tools/mermin-roots-40digit.json")
               ["fixture"] if s["id"] == STATE)
same_doubles = [float(e) for e, _ in fixture["levels"]] == list(S["eps_rust"])
check(same_doubles and abs(ROOT_R - mp.mpf(fixture["root40"])) < mp.mpf(10) ** -32,
      "the root on the Rust levels equals the fixture root40 to 1e-32",
      record=f"{KS}/solver/tools/mermin-roots-40digit.json, state {STATE}")
```

`fixture` is the entry of this state in the Rust solver's 40-digit fixture `mermin-roots-40digit.json`, made from the exact doubles of its final levels. `same_doubles` confirms that the fixture's levels are exactly our Rust levels, and the check requires our root to equal the fixture's `root40` to $10^{-32}$.

```python
sys.path.insert(0, str(repository_file(f"{KS}/checker")))
import crosscheck_ks as CC  # noqa: E402  the cross-check program (Revision code)

checker_root, _ = CC.mu_high_precision(list(S["eps_rust"]), list(S["g_rust"]), 8.0,
                                       0.01, S["mu_rust"])
row = {r["case"]: r for r in read_csv(f"{KS}/reports/ks-crosscheck-table.csv")}[
    f"{STATE} mu_high_precision"]
say(f"table row: Rust {row['rust']}, reference {row['reference']}, |diff| "
    f"{row['abs_diff']}; ours: |diff| {mp.nstr(abs(ROOT_R - ROOT_F), 4)}")
check(checker_root == float(ROOT_R) and abs(float(ROOT_R) - float(row["rust"])) < 1e-16
      and abs(float(ROOT_F) - float(row["reference"])) < 1e-16,
      "our 40-digit roots equal the checker's function and its table row",
      record=f"{KS}/reports/ks-crosscheck.json, check thermo_mu_high_precision")
```

The cross-check program `crosscheck_ks.py` is imported as `CC` (its folder is added to the search list first), and its own 40-digit function `mu_high_precision` computes the root on the Rust levels, starting from the committed $\mu$. `row` is the row `N8_lamm1_a00_T10 mu_high_precision` of the cross-check table (a dictionary comprehension over all rows, then indexed by the case name). The printed line compares the table's two roots and their difference, $4.018\times10^{-13}$, with ours. The check requires our root, converted to a double, to equal the checker's exactly and both roots to equal the table's to $10^{-16}$.

```python
check(abs(abs(ROOT_R - ROOT_F) - mp.mpf(row["abs_diff"])) < 1e-16
      and abs(ROOT_R - ROOT_F) < 1e-12,
      "the two roots differ by only 4e-13: the levels agree, the old Rust mu did not")
```

The last check: our two roots differ by the table's $4.018\times10^{-13}$ and by less than $10^{-12}$. The levels of the two solvers agree; the old Rust $\mu$, $8.3\times10^{-10}$ below both roots, did not.

**In [5], why 16 digits are not enough: the staircase.**

```python
eps_r, g_r = S["eps_rust"], S["g_rust"]

def direct_residual(mu, eps, g, N, T):
    """sum g f - N, added up directly in doubles (the method of the first runs)."""
    return float(np.sum(g * K.fermi((eps - mu) / T))) - N

def exact_residual(mu40, eps, g, N, T):
    """sum g f - N with 40 digits (mu40 an mpmath number)."""
    return sum(mp.mpf(float(gi)) / (1 + mp.exp((mp.mpf(float(e)) - mu40) / T))
               for e, gi in zip(eps, g)) - N
```

`direct_residual` is the residual $\sum g f - N$ added up directly in doubles, the method of the first runs (`np.sum` of the products, `float` to make it an ordinary number). `exact_residual` is the same sum in 40-digit numbers, for a 40-digit $\mu$.

```python
shifts = np.linspace(-3e-9, 3e-9, 1201)  # distances from the root, units of m
mu_star = float(ROOT_R)  # the double nearest to the 40-digit root
D = np.array([direct_residual(mu_star + d, eps_r, g_r, 8.0, 0.01) for d in shifts])
W = np.array([K.mermin_residual(eps_r, g_r, 8.0, 0.01, mu_star + d) for d in shifts])
X = np.array([float(exact_residual(mp.mpf(mu_star) + mp.mpf(float(d)), eps_r, g_r,
                                   8, mp.mpf("0.01"))) for d in shifts])
steps = np.unique(D)  # the different values the direct residual takes
zero = shifts[D == 0.0]  # where the computed direct residual is exactly zero
```

`shifts` holds 1201 distances from the root between $-3\times10^{-9}$ and $3\times10^{-9}$, $5\times10^{-12}$ apart. `mu_star` is the double nearest to the 40-digit root. At each shifted $\mu$ the cell evaluates the direct residual `D`, the well-conditioned residual `W` of Section 16.20 with the reference's function `K.mermin_residual`, and the exact residual `X` with 40 digits (the shift is added in 40-digit numbers, and the temperature is given as the exact text `"0.01"`). `steps` holds the different values that `D` takes (`np.unique` sorts them and removes repetitions), and `zero` the shifts at which `D` is exactly zero.

```python
say(f"the direct residual takes {len(steps)} different values in this window: "
    + ", ".join(f"{v / 2.0 ** -50:+.0f}" for v in steps) + " times 2^-50")
say(f"it is exactly zero for mu - root from {zero.min():.3e} to {zero.max():.3e}, "
    f"an interval {zero.max() - zero.min():.2e} wide")
say(f"largest |W - exact| = {np.max(np.abs(W - X)):.1e}, largest |D - exact| = "
    f"{np.max(np.abs(D - X)):.1e}")
check(np.all(np.mod(D / 2.0 ** -50, 1.0) == 0.0) and len(steps) <= 12,
      "the direct residual is a staircase: whole multiples of 2^-50 only")
check(3e-10 < zero.max() - zero.min() < 3e-9,
      "the direct residual vanishes on an interval about 1e-9 wide")
check(np.max(np.abs(W - X)) < 1e-20,
      "the well-conditioned residual follows the exact one to 1e-20")
```

Out [5]: the direct residual takes only six values in this window, $-4$, $-3$, $-2$, $0$, $+2$ and $+4$ times $2^{-50}$: below 8 it moves in steps of $2^{-50}$ and above 8 in steps of $2^{-49} = 2\cdot2^{-50}$, the spacings of Section 16.20. It is exactly zero from $8.250\times10^{-10}$ below the root to $2.300\times10^{-10}$ above it, an interval $1.05\times10^{-9}$ wide (the estimate of Section 16.20 is $1.07\times10^{-9}$). The well-conditioned residual differs from the exact one by at most $3.9\times10^{-23}$, the direct one by up to $1.5\times10^{-15}$. The three checks require: every value of `D` a whole multiple of $2^{-50}$ (`np.mod(x, 1.0)` is the fractional part) and at most 12 different values; a zero interval between $3\times10^{-10}$ and $3\times10^{-9}$ wide; and `W` within $10^{-20}$ of the exact residual.

**In [6], the staircase as a picture (Figure 16c.2).**

```python
fig, ax = plt.subplots(figsize=(8.5, 5.0))
scale_mu, scale_r = 1e-9, 1e-15  # plot units: 1e-9 m and 1e-15 particles
ax.axvspan(zero.min() / scale_mu, zero.max() / scale_mu, color="0.85",
           label="direct residual exactly 0")
ax.step(shifts / scale_mu, D / scale_r, where="mid", color=PALETTE[1], lw=1.8,
        label="direct residual $D$ in doubles")
ax.plot(shifts / scale_mu, W / scale_r, color=PALETTE[0], lw=2.5, alpha=0.8,
        label="well-conditioned residual $W$ in doubles")
ax.plot(shifts / scale_mu, X / scale_r, "k--", lw=1.0, label="exact (40 digits)")
ax.axvline((MU_OLD_RUST - mu_star) / scale_mu, color=PALETTE[7], lw=1.5,
           label="mu of the first cross-check (Rust)")
ax.axhline(0.0, color="k", lw=0.6)
ax.set_xlabel("$\\mu$ minus the 40-digit root (units of $10^{-9}\\,m$)")
ax.set_ylabel("$N(\\mu) - N$ (units of $10^{-15}$)")
ax.set_title("N8_lamm1_a00_T10: the computed residual near the root")
ax.legend(fontsize=8, loc="upper left")
```

The plot units are $10^{-9}$ for $\mu$ and $10^{-15}$ for the residual. `axvspan` shades the zero interval in light grey (the colour `"0.85"` is a grey level). `ax.step(..., where="mid")` draws the direct residual as a staircase whose steps change half-way between the sample points; the well-conditioned residual is a thick blue line and the exact one a thin dashed black line. A red vertical line marks the faulty $\mu$ of the first cross-check, measured from the root.

```python
save_figure(fig, "residual_staircase",
            "The residual $N(\\mu) - N$ of the Mermin condition of the state "
            "N8_lamm1_a00_T10 (Rust levels) within $3 \\times 10^{-9}\\,m$ of the "
            "40-digit root, horizontal axis in units of $10^{-9}\\,m$, vertical axis "
            "in units of $10^{-15}$ particles. Added up directly in ordinary computer "
            "numbers (orange) the sum near 8 can only change in steps of $2^{-50}$ "
            "or $2^{-49}$, so the residual is a staircase that is exactly zero on an "
            "interval about $10^{-9}$ wide (grey); the faulty $\\mu$ of the first "
            "cross-check (red) is the left end of that interval. The "
            "well-conditioned form (blue) follows the exact line (dashed) and "
            "crosses zero at the root.")
```

`save_figure` saves Figure 16c.2. What the student should see: the exact residual is a straight line through zero at the root, with slope $N' = 1.24\times10^{-6}$ (in these units $1.24$ per unit); the blue well-conditioned residual lies on it everywhere; the orange direct residual is a staircase with steps of $2^{-50} = 0.89$ and $2^{-49} = 1.78$ units, exactly zero on the grey interval; and the red line, the faulty $\mu$, is the left end of that interval, where bisection on the direct sum must stop.

**In [7], bisection on the two forms: the faulty value and the repair.**

```python
def bisection(residual, lo, hi):
    """Bisection for the root of an increasing function with residual(lo) < 0 and
    residual(hi) >= 0, down to neighbouring doubles; returns (root, all midpoints)."""
    midpoints = []
    while True:
        mid = 0.5 * (lo + hi)
        if mid <= lo or mid >= hi:  # lo and hi are neighbouring doubles: done
            break
        midpoints.append(mid)
        if residual(mid) < 0.0:
            lo = mid  # the root lies above mid
        else:
            hi = mid  # the root lies at or below mid
    return 0.5 * (lo + hi), midpoints
```

`bisection(residual, lo, hi)` is the bisection of Section 16.20 for an increasing function given as an argument (in Python a function can be passed like any other value). The `while True:` loop runs until `break`: if the midpoint is not strictly between `lo` and `hi`, the two are neighbouring doubles and nothing is left to halve. Otherwise the midpoint is recorded, and the half is kept in which the root lies: above the midpoint if the residual is negative there, at or below it otherwise.

```python
def bracket(eps, T):
    """The starting interval of the reference: every level, 60 T and 1 m around."""
    return float(eps.min()) - 60.0 * T - 1.0, float(eps.max()) + 60.0 * T + 1.0
```

`bracket` gives the starting interval that the reference uses: from the lowest level minus $60T$ minus 1 to the highest level plus $60T$ plus 1, which surely contains the root.

```python
MU_DIRECT, PATH_DIRECT = bisection(
    lambda mu: direct_residual(mu, eps_r, g_r, 8.0, 0.01), *bracket(eps_r, 0.01))
MU_WELL, PATH_WELL = bisection(
    lambda mu: K.mermin_residual(eps_r, g_r, 8.0, 0.01, mu), *bracket(eps_r, 0.01))
_, mu_ks_fd = K.mermin(eps_r, g_r, 8.0, 0.01)  # the reference's own function
say(f"bisection, direct sum:      mu = {MU_DIRECT!r} after {len(PATH_DIRECT)} "
    f"halvings; minus root {float(MU_DIRECT - ROOT_R):+.3e}")
say(f"bisection, well-conditioned: mu = {MU_WELL!r} after {len(PATH_WELL)} "
    f"halvings; minus root {float(MU_WELL - ROOT_R):+.3e}")
say(f"recorded mu of the first cross-check (Rust): {MU_OLD_RUST!r}; committed "
    f"repaired Rust mu: {S['mu_rust']!r}")
report("direct-sum bisection minus the 40-digit root",
       f"{float(MU_DIRECT - ROOT_R):.4e}", "m")
```

The two bisections on the Rust levels: on the direct residual and on the well-conditioned one (each residual is given as a lambda of $\mu$ alone). `K.mermin` is the reference's own root finder, which bisects the well-conditioned form. Out [7]: the direct sum gives $\mu = 0.21001044890716491$, $8.267\times10^{-10}$ below the root, and the well-conditioned form $0.21001044973390365$, $2.6\times10^{-18}$ from it; both after 57 halvings. That number is no accident: the starting interval reaches from $-1.600$ to $2.482$, so it is $4.08$ wide; the doubles near $0.21$ are $2^{-55} = 2.8\times10^{-17}$ apart; and $4.08/2^{57} = 2.8\times10^{-17}$, so after 57 halvings `lo` and `hi` are neighbouring doubles. The RESULT line repeats the error of the direct sum.

```python
check(abs(MU_DIRECT - MU_OLD_RUST) <= 5e-17,
      "bisection on the direct sum gives the recorded faulty mu (all 16 digits)",
      record=f"{KS}/checker/README.md, History 1 (Rust mu 0.2100104489071649)")
check(MU_WELL == mu_ks_fd and abs(MU_WELL - ROOT_R) < 1e-16,
      "bisection on the well-conditioned form (ks_fd.mermin) finds the root to 1e-16")
check(abs(S["mu_rust"] - MU_WELL) < 1e-16,
      "the committed repaired Rust mu equals the well-conditioned root",
      record=f"{KS}/results/thermo/thermodynamics.csv, state {STATE}")
```

The three checks: the direct-sum bisection reproduces the recorded faulty $\mu = 0.2100104489071649$ of the first cross-check to $5\times10^{-17}$, that is, in all sixteen digits that the record prints; the well-conditioned bisection gives exactly the result of the reference's own function and lies within $10^{-16}$ of the root; and the committed, repaired Rust $\mu$ equals the well-conditioned root to $10^{-16}$.

```python
mu_direct_ref, _ = bisection(
    lambda mu: direct_residual(mu, S["eps_ref"], S["g_ref"], 8.0, 0.01),
    *bracket(S["eps_ref"], 0.01))
say(f"the direct sum on the reference levels misses their root by "
    f"{float(mu_direct_ref - ROOT_F):+.3e}")
```

The direct sum on the reference levels misses their own root by almost the same amount, $8.271\times10^{-10}$: the two level sets agree to about $10^{-12}$, so their staircases have zero intervals at almost the same place, and bisection stops at the left end again.

**In [8], three searches compared (Figure 16c.3).**

```python
fig, ax = plt.subplots(figsize=(8.5, 5.0))
floor = 1e-36  # distances that are exactly zero are drawn here
for colour, path, label, size in (
        (PALETTE[0], PATH_WELL, "bisection, well-conditioned form", 6),
        (PALETTE[1], PATH_DIRECT, "bisection, direct sum", 3)):  # drawn on top
    distance = [max(float(abs(mp.mpf(m) - ROOT_R)), floor) for m in path]
    ax.semilogy(range(1, len(path) + 1), distance, "o-", color=colour, ms=size,
                lw=1.2, label=f"{label} ({len(path)} steps)")
newton = [max(float(abs(m - ROOT_R)), floor) for m in NEWTON_PATH]
ax.semilogy(range(len(newton)), newton, "s-", color=PALETTE[2], ms=6, lw=1.5,
            label="Newton with 40 digits")
```

For the two bisections the distance of every midpoint from the 40-digit root is drawn against the step number on a logarithmic axis (distances that are exactly zero are raised to $10^{-36}$); the direct-sum path is drawn second, with smaller markers, so that it lies on top. The Newton guesses are drawn as green squares.

```python
ax.axhline(abs(MU_OLD_RUST - float(ROOT_R)), color=PALETTE[7], lw=1.0, ls="--",
           label="error of the first cross-check")
ax.axhline(math.ulp(mu_star), color="k", lw=0.8, ls=":",
           label="spacing of the doubles near $\\mu$")
ax.set_ylim(floor / 3.0, 10.0)
ax.set_xlabel("step")
ax.set_ylabel("distance from the 40-digit root (units of $m$)")
ax.set_title("Three searches for $\\mu$ in N8_lamm1_a00_T10")
ax.legend(fontsize=8, loc="upper right")
```

Two horizontal lines mark the error of the first cross-check (red, dashed) and the spacing of the doubles near $\mu$ (`math.ulp(x)` is the distance from $x$ to the next double; dotted).

```python
save_figure(fig, "convergence_paths",
            "The distance of each guess for $\\mu$ from the 40-digit root, units "
            "of $m$, logarithmic, against the step number, for the state "
            "N8_lamm1_a00_T10 with the Rust levels. Bisection halves the distance at "
            "every step; on the direct sum (orange) it stalls at $8.3 \\times "
            "10^{-10}$, the error of the first cross-check (red dashed), because "
            "the computed sum is zero on a whole interval; on the well-conditioned "
            "form (blue) it reaches the spacing of the doubles (dotted). Newton's "
            "method with 40 digits (green) doubles the number of correct digits at "
            "each step; zero distances are drawn at $10^{-36}$.")
check(min(float(abs(mp.mpf(m) - ROOT_R)) for m in PATH_DIRECT[-20:]) > 5e-10
      and float(abs(NEWTON_PATH[-2] - ROOT_R)) < 1e-32 and len(NEWTON_PATH) <= 7,
      "the direct bisection stalls above 5e-10; Newton reaches 1e-32 in 5 steps")
```

`save_figure` saves Figure 16c.3. What the student should see: the two bisection paths coincide for about 30 steps, halving the distance at every step on average (a straight line on this axis); then the direct-sum path stops falling and stays at $8.3\times10^{-10}$ (it now only explores the zero interval of the staircase), while the well-conditioned path continues down to the spacing of the doubles; Newton's method with 40 digits reaches $10^{-34}$ in four steps. The check requires the last 20 direct-sum midpoints to stay more than $5\times10^{-10}$ from the root, Newton's next-to-last guess to be within $10^{-32}$, and at most 7 Newton guesses.

**In [9], the rounding bounds.**

```python
def rounding_bounds(eps, g, N, T, mu):
    """dN/dmu, the bound of the direct sum and the bound of the well-conditioned form
    at mu (the formulas of solver/src/mermin.rs), and P, H, d."""
    x = (eps - mu) / T
    f_plus, f_minus = K.fermi(x), K.fermi(-x)  # f(x) and 1 - f(x) = f(-x)
    weight = g * f_plus * f_minus  # g f (1 - f): how strongly a level reacts to mu
    slope = float(np.sum(weight)) / T  # dN/dmu
    mean_distance = float(np.sum(weight * np.abs(eps - mu)) / np.sum(weight))
    below = x < 0.0
    particles = float(np.sum(g[~below] * f_plus[~below]))  # P
    holes = float(np.sum(g[below] * f_minus[below]))  # H
    d = N - float(np.sum(g[below]))  # a whole number
    n = len(eps)
    big_l = max(abs(math.log(particles + max(-d, 0.0))),  # |ln A|
                abs(math.log(holes + max(d, 0.0))))  # |ln B|
    common = EPS_MACH * (3.0 * mean_distance + T * (math.log(float(np.max(g))) + 3.0)
                         + 2.0 * abs(mu))
    direct = EPS_MACH * (n + 2) * N / slope + common
    well = EPS_MACH * (n + 2 + big_l) * (particles + holes + abs(d)) / slope + common
    return {"slope": slope, "direct": direct, "well": well, "P": particles,
            "H": holes, "d": d, "n": n, "L": big_l}
```

`rounding_bounds` evaluates the two bounds of Section 16.20 at a given $\mu$. `f_plus` and `f_minus` are $f(x)$ and $f(-x) = 1 - f(x)$; `weight` is $g\,f(1 - f)$, how strongly each level reacts to $\mu$; `slope` is $N' = \sum g f(1 - f)/T$; `mean_distance` is $\langle|\varepsilon - \mu|\rangle$, the mean distance of the levels from $\mu$ weighted with `weight`. `particles` is $P$ (the levels above $\mu$; `~below` reverses the mask), `holes` is $H$, and `d` the whole number $N - \sum_{\text{below}}g$. `big_l` is $L_A = \max(|\ln A|, |\ln B|)$ with $A = P + \max(-d, 0)$ and $B = H + \max(d, 0)$, the two sides of the balance. `common` holds the three small terms that both bounds share, and `direct` and `well` are $B_{direct}$ and $B_{well}$.

```python
MERMIN_REPORT = read_json(f"{KS}/reports/ks-rust-mermin-roots.json")
RECORD = {s["id"]: s for s in MERMIN_REPORT["states"]}
b = rounding_bounds(eps_r, g_r, 8.0, 0.01, mu_star)
rec = RECORD[STATE]
say(f"n = {b['n']} levels; P = {b['P']:.6e}, H = {b['H']:.6e}, d = {b['d']:.0f}, "
    f"L = {b['L']:.3f}; dN/dmu = {b['slope']:.6e} (record {rec['dN_dmu']})")
say(f"B_direct = {b['direct']:.4e} (record {rec['boundDirectCount']}); B_well = "
    f"{b['well']:.4e} (record {rec['boundWellConditioned']})")
```

`MERMIN_REPORT` is the Rust solver's 40-digit report `ks-rust-mermin-roots.json`, and `RECORD` files its states by id. The bounds are evaluated at the double nearest to the root, and Out [9] prints them next to the record: $n = 7$ levels, $P = H = 6.210359\times10^{-9}$, $d = 0$, $L_A = 18.897$ (which is $|\ln(6.21\times10^{-9})|$), $N' = 1.242072\times10^{-6}$ (record the same), $B_{direct} = 1.2871\times10^{-8}$ (record $1.287\times10^{-8}$) and $B_{well} = 3.1539\times10^{-16}$ (record $3.154\times10^{-16}$).

```python
one_step = EPS_MACH * 8.0 / b["slope"]  # one rounding of size eps_mach N, as mu
say(f"one rounding of size eps_mach N moves the root by {one_step:.3e}; the error "
    f"of the first cross-check is {DIFF_OLD / one_step:.2f} of that")
```

`one_step` is the shift $\epsilon_{mach}N/N' = 1.430\times10^{-9}$ that a single rounding of the size $\epsilon_{mach}N$ causes; the error of the first cross-check is $0.58$ of it (Out [9]).

```python
check(abs(b["slope"] / float(rec["dN_dmu"]) - 1) < 1e-5
      and abs(b["direct"] / float(rec["boundDirectCount"]) - 1) < 1e-3
      and abs(b["well"] / float(rec["boundWellConditioned"]) - 1) < 1e-3,
      "dN/dmu and both rounding bounds reproduce the Rust 40-digit report",
      record=f"{KS}/reports/ks-rust-mermin-roots.json, state {STATE}")
check(abs(MU_OLD_RUST - float(ROOT_R)) <= b["direct"]
      and abs(S["mu_rust"] - float(ROOT_R)) <= b["well"] + 1e-16,
      "the old error lies within B_direct, the repaired mu within B_well")
```

The first check reproduces the record: $N'$ to a relative $10^{-5}$ and both bounds to $10^{-3}$ (the report prints four digits). The second confirms that the old error lies within $B_{direct}$ and the repaired $\mu$ within $B_{well}$.

**In [10], all 45 thermal states with eight quanta.**

```python
TABLE = {r["case"]: r for r in read_csv(f"{KS}/reports/ks-crosscheck-table.csv")}

def tolerance(x_ref, u_ref, u_rust):
    """The tolerance rule of the cross-check for single numbers."""
    return 3.0 * (u_ref + u_rust) + 1e-12 * max(1.0, abs(x_ref))
```

`TABLE` files the rows of the cross-check table by case, and `tolerance` is the rule of Section 16.7 for single numbers.

```python
ROWS = []  # one dictionary per state
for sid in sorted(s for s in REFINEMENT if s.startswith("N8_")):
    s = state_data(sid)
    N, T = s["N"], s["T"]
    root_r, _, _ = mermin_root_40(s["eps_rust"], s["g_rust"], N, T, s["mu_rust"])
    root_f, _, _ = mermin_root_40(s["eps_ref"], s["g_ref"], N, T, s["mu_ref"])
    r = {"id": sid, "N": N, "T": T, "root_r": root_r, "root_f": root_f,
         "b_r": rounding_bounds(s["eps_rust"], s["g_rust"], N, T, float(root_r)),
         "b_f": rounding_bounds(s["eps_ref"], s["g_ref"], N, T, float(root_f))}
```

The loop goes through the 45 thermal states whose id begins with N8 (`startswith`), sorted. For each it collects the data, computes the 40-digit roots on the Rust and on the reference levels (Newton's method, started from each solver's committed $\mu$), and evaluates both bounds at both roots.

```python
    for side in ("r", "f"):  # the two bisections on each solver's levels
        e, gg = (s["eps_rust"], s["g_rust"]) if side == "r" else (s["eps_ref"],
                                                                    s["g_ref"])
        root = float(r["root_" + side])
        r["direct_" + side] = bisection(
            lambda mu: direct_residual(mu, e, gg, N, T), *bracket(e, T))[0] - root
        r["well_" + side] = bisection(
            lambda mu: K.mermin_residual(e, gg, N, T, mu), *bracket(e, T))[0] - root
```

For each solver's levels (`side` is `"r"` for Rust and `"f"` for the reference) it runs bisection on the direct sum and on the well-conditioned form and stores each result minus the root (`[0]` takes the root from the returned pair). The lambdas are used immediately inside the loop, so each sees the current levels `e` and degeneracies `gg`.

```python
    r["committed_r"] = float(mp.mpf(s["mu_rust"]) - root_r)
    r["committed_f"] = float(mp.mpf(s["mu_ref"]) - root_f)
    r["U_mu_ref"] = s["U_mu_ref"]
    u_lev_rust = 16.0 / 15.0 * REFINEMENT[sid]["levels"]["max_abs_diff"]
    u_mu_rust = 16.0 / 15.0 * REFINEMENT[sid]["scalars"]["mu"]["abs_diff"]
    tol_hp = tolerance(float(root_f), s["U_levels_ref"], u_lev_rust)
    tol_mu = tolerance(s["mu_ref"], s["U_mu_ref"], u_mu_rust)
    r["ratio_hp"] = float(abs(root_r - root_f)) / tol_hp
    r["ratio_mu"] = abs(s["mu_rust"] - s["mu_ref"]) / tol_mu
    r["tol_hp"], r["tol_mu"] = tol_hp, tol_mu
    r["n_r"], r["n_f"] = len(s["eps_rust"]), len(s["eps_ref"])
    ROWS.append(r)
```

`committed_r` and `committed_f` are the committed $\mu$ of each solver minus its 40-digit root. The cell then rebuilds two comparisons of the cross-check: the 40-digit roots, with $U_{ref}$ the reference's largest level uncertainty and $U_{Rust}$ $\tfrac{16}{15}$ times the largest canonical-minus-refined level difference (because $\mu$ is a weighted mean of the levels, its uncertainty is bounded by theirs: `Revision/kohn_sham/checker/crosscheck_ks.py`, comment before the 40-digit check), and the committed values of $\mu$, with the reference's $U$ of $\mu$ and $\tfrac{16}{15}|\mu_c - \mu_r|$; it keeps both tolerances and ratios and the numbers of levels.

```python
print("the nine states with the largest direct-sum bound (Rust levels):")
print("state                 n   dN/dmu     B_direct   direct error  B_well")
for r in sorted(ROWS, key=lambda r: -r["b_r"]["direct"])[:9]:
    print(f"{r['id']:20s} {r['n_r']:3d}  {r['b_r']['slope']:.3e}  "
          f"{r['b_r']['direct']:.3e}  {r['direct_r']:+.3e}    {r['b_r']['well']:.3e}")
```

The table of Out [10] lists the nine states with the largest $B_{direct}$ (Rust levels), sorted by it (`key=lambda r: -...` sorts from the largest down): their number of levels, $N'$, $B_{direct}$, the error of the direct sum and $B_{well}$. The three states at $a_{4,0} = 0$, $T = 0.01$ have $N' \approx 1.2\times10^{-6}$ and bounds near $10^{-8}$; the next ones, at $a_{4,0} = 0.5$ or $T = 0.02$, have $N'$ thousands of times larger and bounds below $10^{-11}$.

**In [11], the checks against the records.**

```python
worst = {"root": 0.0, "slope": 0.0, "bounds": 0.0, "hp": 0.0, "tol": 0.0,
         "ratio": 0.0}
for r in ROWS:
    rec = RECORD[r["id"]]
    worst["root"] = max(worst["root"], float(abs(r["root_r"] - mp.mpf(rec["root40"]))))
    worst["slope"] = max(worst["slope"],
                         abs(r["b_r"]["slope"] / float(rec["dN_dmu"]) - 1))
    worst["bounds"] = max(worst["bounds"],
                          abs(r["b_r"]["direct"] / float(rec["boundDirectCount"]) - 1),
                          abs(r["b_r"]["well"] / float(rec["boundWellConditioned"])
                              - 1))
    hp, mu_row = TABLE[f"{r['id']} mu_high_precision"], TABLE[f"{r['id']} mu"]
    worst["hp"] = max(worst["hp"], abs(float(r["root_r"]) - float(hp["rust"])),
                      abs(float(r["root_f"]) - float(hp["reference"])))
    worst["tol"] = max(worst["tol"], abs(r["tol_hp"] / float(hp["tolerance"]) - 1),
                       abs(r["tol_mu"] / float(mu_row["tolerance"]) - 1))
    worst["ratio"] = max(worst["ratio"], abs(r["ratio_hp"] - float(hp["ratio"])),
                         abs(r["ratio_mu"] - float(mu_row["ratio"])))
```

`worst` collects six largest differences: of our Rust roots from the report's `root40`; of $N'$ and of the two bounds from the report (relative); of both 40-digit roots from the table's rows `mu_high_precision`; of our tolerances from the table's (relative); and of our ratios from the table's, for both rows of each state (`mu_high_precision` and `mu`).

```python
say("largest differences from the records: " + ", ".join(
    f"{k} {v:.1e}" for k, v in worst.items()))
check(worst["root"] < 1e-16,
      "the 45 roots on the Rust levels reproduce root40 (to the 16-digit levels)",
      record=f"{KS}/reports/ks-rust-mermin-roots.json, states (root40)")
check(worst["slope"] < 1e-5 and worst["bounds"] < 1e-3,
      "dN/dmu and both bounds of all 45 states reproduce the Rust report",
      record=f"{KS}/reports/ks-rust-mermin-roots.json, states (bounds)")
check(worst["hp"] < 2e-16 and worst["tol"] < 1e-3 and worst["ratio"] <= 1e-4,
      "both 40-digit roots, tolerances and ratios reproduce 90 table rows",
      record=f"{KS}/reports/ks-crosscheck-table.csv, rows mu, mu_high_precision")
check(all(r["ratio_hp"] <= 1.0 and r["ratio_mu"] <= 1.0 for r in ROWS),
      "after the repair every mu comparison of the 45 states passes",
      record=f"{KS}/reports/ks-crosscheck.json, check thermo_state_functions")
```

Out [11] prints them: roots $2.8\times10^{-17}$, slope $4.5\times10^{-7}$, bounds $4.2\times10^{-4}$, table roots $5.6\times10^{-17}$, tolerances $3.9\times10^{-4}$, ratios $5.0\times10^{-5}$. The roots agree only to about $10^{-17}$, not $10^{-35}$, because the level files keep sixteen significant digits; the bounds and tolerances agree to the four digits the records print. The four checks reproduce the report (roots, then $N'$ and bounds), the 90 table rows, and the cross-check's verdict that after the repair every comparison of $\mu$ in these 45 states passes.

```python
diag_r = [abs(r["committed_r"]) / (r["n_r"] * EPS_MACH * r["N"] / r["b_r"]["slope"])
          for r in ROWS]
diag_f = [abs(r["committed_f"]) / (r["n_f"] * EPS_MACH * r["N"] / r["b_f"]["slope"]
                                   + 3.0 * r["U_mu_ref"]) for r in ROWS]
say(f"committed mu minus root, as a fraction of the diagnostic bound: Rust at most "
    f"{max(diag_r):.1e}, reference at most {max(diag_f):.1e}")
check(max(diag_r) <= 1.0 and max(diag_f) <= 1.0,
      "both solvers' committed mu lie within the rounding diagnostic",
      record=f"{KS}/reports/ks-crosscheck.json, check thermo_mu_rounding_diagnostic")
```

The diagnostic of the cross-check (`thermo_mu_rounding_diagnostic`): each committed $\mu$ minus the root on its own levels, divided by the conditioning bound $n\,\epsilon_{mach}N/N'$ (for the reference plus $3U$, because its $\mu$ combines three grids). Out [11]: at most $1.3\times10^{-2}$ for Rust and $1.4\times10^{-5}$ for the reference; the check requires at most 1.

```python
check(all(abs(r["direct_" + s]) <= r["b_" + s]["direct"]
          and abs(r["well_" + s]) <= r["b_" + s]["well"] for r in ROWS
          for s in ("r", "f")),
      "in all 90 level sets each bisection lies within its own bound")
big = sorted(ROWS, key=lambda r: -abs(r["direct_r"]))[:3]
say("largest direct-sum errors: " + ", ".join(
    f"{r['id']} {r['direct_r']:+.2e}" for r in big))
check({r["id"] for r in big} == {"N8_lam0_a00_T10", "N8_lamm1_a00_T10",
                                 "N8_lamp1_a00_T10"},
      "the direct sum fails worst in the three states with the largest gap/T")
```

The next check confirms that in all 90 level sets (45 states, two solvers) each bisection lies within its own bound: the direct sum within $B_{direct}$ and the well-conditioned form within $B_{well}$. `big` holds the three states with the largest direct-sum errors on the Rust levels, printed in Out [11] ($-8.27\times10^{-10}$, $+2.72\times10^{-10}$, $+6.96\times10^{-11}$), and the last check requires them to be the three states at $a_{4,0} = 0$ and $T = 0.01$, where the gap is largest compared with $T$ (a set `{...}` of ids is compared, so the order does not matter).

**In [12], error against conditioning (Figure 16c.4).**

```python
scale = np.array([EPS_MACH * r["N"] / r["b_r"]["slope"] for r in ROWS])
scale_f = np.array([EPS_MACH * r["N"] / r["b_f"]["slope"] for r in ROWS])
fig, ax = plt.subplots(figsize=(8.0, 6.0))
low = 1e-19  # exact zeros are drawn here
series = [(scale, "direct_r", "o", PALETTE[1], "direct sum, Rust levels"),
          (scale_f, "direct_f", "s", PALETTE[7], "direct sum, reference levels"),
          (scale, "well_r", "o", PALETTE[0], "well-conditioned, Rust levels"),
          (scale_f, "well_f", "s", PALETTE[6], "well-conditioned, reference levels"),
          (scale, "committed_r", "^", PALETTE[2], "committed Rust mu")]
for xs, key, marker, colour, label in series:
    ys = np.maximum([abs(r[key]) for r in ROWS], low)
    ax.loglog(xs, ys, marker, color=colour, ms=5, alpha=0.8, label=label)
```

`scale` and `scale_f` hold the conditioning scale $\epsilon_{mach}N/N'$ of each state for the Rust and the reference levels. `series` lists five sets of points with their key, marker, colour and label; the loop draws each error (raised to $10^{-19}$ if exactly zero) against the conditioning scale on logarithmic axes.

```python
line = np.array([1e-16, 1e-8])
ax.loglog(line, line, "k-", lw=1.0, label="error = $\\epsilon_{mach} N / N'$")
i_old = [r["id"] for r in ROWS].index(STATE)
ax.loglog([scale[i_old]], [DIFF_OLD], "*", color="k", ms=14,
          label="first cross-check (recorded)")
ax.set_xlabel("$\\epsilon_{mach} N / (dN/d\\mu)$ (units of $m$)")
ax.set_ylabel("$|\\mu$ computed $-$ 40-digit root$|$ (units of $m$)")
ax.set_title("45 thermal states with $N = 8$: error against conditioning")
ax.legend(fontsize=7, loc="upper left")
```

The black line is "error equals conditioning scale", a line of slope 1, and the star is the recorded error of the first cross-check at the scale of its state (`.index(STATE)` finds the state's position).

```python
save_figure(fig, "errors_versus_bound",
            "Errors of the computed chemical potential, in units of $m$, against "
            "the conditioning scale $\\epsilon_{mach} N/(dN/d\\mu)$ for the 45 "
            "thermal states with $N = 8$, both axes logarithmic. Bisection on the "
            "direct sum (orange: Rust levels, red: reference levels) has errors "
            "that grow with the conditioning scale and approach the line of slope 1 "
            "in the worst states; the star is the recorded error of the first "
            "cross-check. The well-conditioned form (blue, purple) and the "
            "committed repaired Rust values (green) stay near $10^{-17}$ for every "
            "state; exact zeros are drawn at $10^{-19}$.")
```

`save_figure` saves Figure 16c.4. What the student should see: the errors of the direct sum (orange and red) grow with the conditioning scale and come within a factor of about 2 of the line of slope 1 in the worst states, where the star of the first cross-check sits; the well-conditioned form (blue, purple) and the committed repaired Rust values (green) stay near $10^{-17}$ whatever the conditioning, many of them exactly zero (the bottom row).

**In [13], where the direct sum is dangerous (Figure 16c.5).**

```python
tags = [("lam0", "$\\lambda = 0$"), ("lamp1", "$\\lambda = +\\lambda_1$"),
        ("lamm1", "$\\lambda = -\\lambda_1$")]
slices, temps = ["a00", "a05", "a10", "a15", "a20"], ["T10", "T20", "T50"]
by_id = {r["id"]: r for r in ROWS}
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.6))
for ax, (tag, title) in zip(axes, tags):
    grid = np.array([[math.log10(by_id[f"N8_{tag}_{a}_{t}"]["b_r"]["direct"])
                      for t in temps] for a in slices])
    image = ax.imshow(grid, cmap="viridis", vmin=-15.0, vmax=-7.5, aspect="auto")
    ax.grid(False)  # no grid lines across the coloured squares
```

`tags` pairs the three coupling tags with their titles, `slices` and `temps` list the id parts of the five slices and three temperatures, and `by_id` files the 45 rows by id. For each coupling, `grid` is a $5\times3$ table of $\log_{10}B_{direct}$, slices down, temperatures across, built by a nested list comprehension; `imshow` paints it with the colour scale `viridis` between $-15$ and $-7.5$, and `ax.grid(False)` removes the grid lines over the squares.

```python
    for i in range(5):
        for j in range(3):
            ax.text(j, i, f"{grid[i, j]:.1f}", ha="center", va="center",
                    color="w" if grid[i, j] < -11.5 else "k", fontsize=9)
    ax.set_xticks(range(3))
    ax.set_xticklabels(["0.01", "0.02", "0.05"])
    ax.set_yticks(range(5))
    ax.set_yticklabels(["0", "0.5", "1", "1.5", "2"])
    ax.set_xlabel("temperature $T$ (units of $m$)")
    ax.set_title(title)
axes[0].set_ylabel("slice $a_{4,0}$")
fig.colorbar(image, ax=axes, shrink=0.9, label="$\\log_{10} B_{direct}$ (units of $m$)")
```

Each square gets its number with one decimal, written in white on the dark squares and in black on the light ones; the ticks are labelled with the temperatures and the slices, and one colour scale serves the three maps.

```python
save_figure(fig, "conditioning_map",
            "The rounding bound $B_{direct}$ of the direct sum, as $\\log_{10}$ of "
            "its value in units of $m$, for the 45 thermal states with $N = 8$ (Rust "
            "levels): one map per coupling, the slice $a_{4,0}$ of the deflating "
            "history downwards, the temperature across. The direct sum is dangerous "
            "only at low temperature early in the history, where the gap is 43 "
            "times $T$ and the bound reaches $10^{-8}$; later the redshift of the "
            "3-momenta closes the gap and the bound falls to about $10^{-15}$.")
check(max(by_id[f"N8_{t}_a00_T10"]["b_r"]["direct"] for t, _ in tags)
      == max(r["b_r"]["direct"] for r in ROWS)
      and all(by_id[f"N8_{t}_a00_T10"]["b_r"]["direct"]
              > 100.0 * by_id[f"N8_{t}_a10_T10"]["b_r"]["direct"] for t, _ in tags),
      "the bound is largest at a4,0 = 0, T = 0.01 and falls along the history")
```

`save_figure` saves Figure 16c.5. What the student should see: in each of the three maps only the top left square ($a_{4,0} = 0$, $T = 0.01$) is bright, at about $-8$, and its neighbours ($a_{4,0} = 0.5$ or $T = 0.02$) are near $-11$ to $-12$; everywhere else the bound lies between about $10^{-15}$ and $10^{-13}$. Along the deflating history the gap closes, because the redshift of the 3-momenta brings the levels of the brane band down towards the filled levels. The check requires the largest bound of all 45 to be one of the three states at $a_{4,0} = 0$, $T = 0.01$, and each of them to be more than 100 times its value at $a_{4,0} = 1$.

**In [14], what the tolerance rule did (Figure 16c.6).**

```python
order = sorted(range(len(ROWS)), key=lambda i: -ROWS[i]["b_r"]["direct"])
ratio_old = DIFF_OLD / TOL_OLD  # the ratio of the first, failed comparison
fig, ax = plt.subplots(figsize=(9.5, 4.8))
positions = np.arange(len(order))
ax.semilogy(positions, [ROWS[i]["ratio_mu"] for i in order], "o", color=PALETTE[0],
            ms=5, label="$\\mu$ (committed values), after the repair")
ax.semilogy(positions, [ROWS[i]["ratio_hp"] for i in order], "s", color=PALETTE[2],
            ms=5, mfc="none", label="$\\mu$ with 40 digits on each solver's levels")
k_old = order.index([r["id"] for r in ROWS].index(STATE))
ax.semilogy([k_old], [ratio_old], "*", color=PALETTE[7], ms=16,
            label=f"first cross-check, before the repair: {ratio_old:.0f}")
ax.axhline(1.0, color="k", lw=1.2, label="ratio 1: the tolerance")
```

`order` sorts the 45 states by $B_{direct}$, largest first, and `ratio_old` is the ratio of the failed first comparison, $8.27\times10^{-10}/7.97\times10^{-12} = 103.8$. The ratios of the committed $\mu$ (circles) and of the 40-digit roots (open squares, `mfc="none"`) are drawn for each state in that order, the old ratio as a red star at the position of N8_lamm1_a00_T10, and the line ratio 1.

```python
ax.set_xticks(positions[::4])
ax.set_xticklabels([ROWS[i]["id"].replace("N8_", "") for i in order][::4],
                   rotation=40, ha="right", fontsize=7)
ax.set_xlabel("state (sorted by the bound of the direct sum, largest first)")
ax.set_ylabel("$|\\mu_{Rust} - \\mu_{ref}|$ / tolerance")
ax.set_ylim(1e-4, 1e3)
ax.legend(fontsize=8, loc="upper right")
fig.tight_layout()
```

Every fourth state is named on the horizontal axis (without the common prefix N8_), and the vertical axis runs from $10^{-4}$ to $10^{3}$.

```python
save_figure(fig, "crosscheck_ratios",
            "The cross-check of the chemical potential for the 45 thermal states with "
            "$N = 8$: the difference of the two solvers divided by the tolerance "
            "fixed in advance, logarithmic, the states sorted by the rounding bound "
            "of the direct sum. Circles: the committed values after the repair; "
            "squares: the 40-digit roots on each solver's levels; all lie far below "
            "the line 1. The star is the first comparison in N8_lamm1_a00_T10, "
            f"before the repair, with the ratio {ratio_old:.0f}: the rule caught a "
            "rounding error of the Rust solver, and the repair, not a wider "
            "tolerance, removed it.")
```

`save_figure` saves Figure 16c.6. What the student should see: the star of the first comparison, at about 104, lies two orders of magnitude above the line 1; after the repair, the same rule gives ratios between about $5\times10^{-4}$ and $0.08$ for every state. The rule caught the error, and the repair, not a wider tolerance, removed it.

```python
report_detail = next(c["detail"] for c in read_json(
    f"{KS}/reports/ks-crosscheck.json")["checks"]
    if c["name"] == "thermo_mu_high_precision")
worst_all = float(re.search(r"worst \|diff\|/tolerance ([0-9.]+)",
                            report_detail).group(1))
say(f"first comparison: ratio {ratio_old:.1f}. After the repair, over these 45 "
    f"states: mu at most {max(r['ratio_mu'] for r in ROWS):.4f}, 40-digit roots at "
    f"most {max(r['ratio_hp'] for r in ROWS):.4f} (the report, over all 135 states: "
    f"40-digit roots at most {worst_all})")
check(ratio_old > 1.0 and max(r["ratio_hp"] for r in ROWS) <= worst_all + 5e-4
      and max(r["ratio_mu"] for r in ROWS) < 0.1,
      "the first comparison failed the rule; after the repair all ratios are small",
      record=f"{KS}/reports/ks-crosscheck.json, check thermo_mu_high_precision")
```

The worst ratio of the 40-digit comparison over all 135 thermal states is read from the detail of the cross-check's check `thermo_mu_high_precision` ($0.05$). Out [14] prints the old ratio, $103.8$, and the largest ratios over the 45 states after the repair: $0.0825$ for the committed $\mu$ and $0.0270$ for the 40-digit roots. The check requires the old ratio above 1, our 40-digit ratios no larger than the report's worst, and every ratio of the committed $\mu$ below $0.1$.

**In [15], the last check.**

```python
figure_files = [f"{FIGURE_FOLDER}/16c_{k}_{name}.png" for k, name in enumerate(
    ["levels_and_occupations", "residual_staircase", "convergence_paths",
     "errors_versus_bound", "conditioning_map", "crosscheck_ratios"], start=1)]
check(all(output_file(f).is_file() for f in figure_files),
      "every figure file of this notebook exists")
all_checks_passed()
```

As In [23] of Notebook 16a, for the six figures; it prints ALL 26 CHECKS PASSED (notebook 16c): seven checks in In [11], three each in In [2], In [4], In [5] and In [7], two in In [9], and one each in In [3], In [8], In [13], In [14] and In [15].

### 16.25 What the cross-check does not test

The cross-check is a test of the **numerics**: of the discretisation, the rounding and the programming of the Rust solver, against a second program that differs in all three. Everything that both programs take from the same source is outside its reach, and the record says so (`Revision/kohn_sham/reference/README.md`, the section on what the reference does not establish). Precisely:

- **The functional.** Both solvers read the same theory file `Revision/kohn_sham/ks-theory.json`: the contact interaction with Hartree and the exact local exchange of the uniform gas, and no correlation (Chapters 13 and 14). If that functional were a poor approximation for the field, both programs would agree on the wrong answer.
- **The boundary conditions.** Both use the ASSUMED Z2 mirror brane at $y = 0$ and the CHOSEN regular tip at the cutoff $y = -L$ with $L = 3$.
- **The filling convention.** Both fill only the positive branch and the brane zero modes and never populate the sea, not even thermally (a CONVENTION whose justification is OPEN). The sea-hole diagnostic, which both programs compute and which agree with each other (worst ratio $0.048$), shows where this convention leaves its range of validity: in 15 of the 135 thermal states the excluded sea would carry more than 1% of $N$, at most $30.98N$ (`Revision/kohn_sham/reports/ks-crosscheck.json`, check `thermo_sea_hole_diagnostic`). Agreement of the two programs on this diagnostic says nothing about whether the convention is right.
- **The history and the adiabatic states.** Both compute instantaneous (adiabatic) Kohn-Sham states along the PRESCRIBED BACKGROUND history $a_4 = AHx_4$ with $A = 1$. The history is not solved for: the Kohn-Sham states violate the conditions that the $a_4$ field equations put on their source (`Revision/field_equations_a4/reports/ks-source-conditions.json`, Chapter 17), and the time-dependent (non-adiabatic) problem is OPEN.
- **The good sector.** Both assume that the quanta do not depend on the extra times $x_5, x_6, x_7$ (ASSUMED, Chapter 14).

A test of these inputs would need something other than a second program for the same equations: an exact functional for the quantised field, a justification or a replacement of the filling convention, a solution of the coupled problem for $a_4$ and the gas, a time-dependent calculation. These are OPEN problems (Chapter 22). Nothing in this chapter concerns pairs of universes, their creation, or matter and antimatter.

### 16.26 What we proved, what we computed, what we assumed

**PROVED** (derived line by line in this chapter; where the Revision record holds the statement, its report and check are named):

- The convergence ratio $(x(h) - x(h/2))/(x(h/2) - x(h/4)) = 4(1 + \tfrac{15}{16}\tfrac dc h^2 + \dots)$ for an error with even powers of $h$ (Section 16.4).
- Richardson extrapolation: $r(h) = (4x(h/2) - x(h))/3 = X - \tfrac14dh^4 + \dots$, $R = (64x(h/4) - 20x(h/2) + x(h))/45 = X + O(h^6)$, and $R - r(h/2) = \tfrac{1}{64}dh^4 + O(h^6)$, so that the stated $U$ over-estimates the error of $R$ when $h$ is small (Section 16.5).
- The Rust uncertainty $U_{Rust} = \tfrac{16}{15}|x_c - x_r|$ for a fourth-order method whose step is halved, and in general the factor $2^p/(2^p - 1)$ for order $p$ (Section 16.6, Exercise 3).
- The tolerance rule as a consequence of the triangle inequality, and the propagated uncertainties $U_F = U_E + TU_S$, $U_\Omega = U_F + NU_\mu$, $3(U_{I_3} + U_{I_t})$ for $dE/da_4$, and the factor 2 for $\Delta E_x$ (Section 16.7).
- The exact free levels at zero momentum: $0$ and $\pm\sqrt{M^2 + (n\pi/L)^2}$ for even parity, $\pm\sqrt{M^2 + p_l^2}$ with $\tan(p_lL) = -p_l/M$ (one root in each interval) for odd parity, and the zero mode $A\,e^{My}$ with $A = \sqrt{2M/(1 - e^{-2ML})}$ (Section 16.13; `Revision/kohn_sham/reports/ks-theory-python.json`, check bc_exact_k0_spectra).
- The staggered discretisation: second-order centred differences and averages with even-power errors, the symmetric tridiagonal matrix, the rotated frame for odd parity with $m_2 = M\cos2\phi - K\sin2\phi$, $k_2 = M\sin2\phi + K\cos2\phi$ and the extra term $\phi'$ (Section 16.14).
- The pivot recursion $q_r = d_r - x - o_{r-1}^2/q_{r-1}$ and, with Sylvester's law, the Sturm count; Gershgorin's bound; the number of bisection steps (Section 16.15).
- The exact discrete zero mode $u_p = q^pu_0$, $q = (1 + Mh/2)/(1 - Mh/2)$, $\ln q = Mh + (Mh)^3/12 + \dots$; the Hellmann-Feynman theorem for symmetric matrices; the brane-band slope $c = e^{-a_{4,0}}\tfrac{2M}{1 - e^{-2ML}}\tfrac{1 - e^{-(2M - H)L}}{2M - H}$ (Section 16.15; same report, check brane_band_slope).
- The slope $dN/d\mu = \tfrac1T\sum gf(1 - f) > 0$ and the uniqueness of the chemical potential; the two-level estimate $\mu \approx \tfrac{\varepsilon_0 + \varepsilon_1}{2} - \tfrac T2\ln\tfrac{g_1}{g_0}$; Newton's method and its quadratic convergence; the width $3\cdot2^{-51}/N'$ of the zero interval of the direct sum near $N = 8$; the exact rewriting $W = -d - H + P$ of the Mermin residual (Section 16.20).

Quoted, not proved here: Sylvester's law of inertia and the spectral theorem for symmetric matrices (Sections 16.14 and 16.15). The first-order rounding bounds $B_{direct}$ and $B_{well}$ are derived in the Rust solver's documentation (`Revision/kohn_sham/solver/src/mermin.rs`); this chapter derives their main terms.

**COMPUTED** (numbers from the records named, each reproduced by a notebook of the chapter):

- The reference solver's self-checks: 37 checks, all PASS (`Revision/kohn_sham/reports/ks-reference.json`); among them the exact free levels reproduced to $2.8\times10^{-14}$, convergence ratios between $3.99977$ and $4.00019$, the brane-band slope to $2.6\times10^{-15}$, and the fourth-grid validation with the largest ratio $0.787$ (Notebooks 16a and 16b).
- The full cross-check: 29 checks, all PASS, 128313 comparisons, no ratio above $0.495$ (the report `Revision/kohn_sham/reports/ks-crosscheck.json` and its table `ks-crosscheck-table.csv` in the same folder). Notebook 16a reproduces, for five states, the reference results byte for byte, the Rust canonical results exactly, the canonical-minus-refined differences of `Revision/kohn_sham/checker/rust-refinement.json`, 97 table rows, and the worst cases of six classes; all 5140 of its comparisons pass, the largest with the ratio $0.4952$.
- The chemical potential: the faulty value $0.2100104489071649$ of the first cross-check reproduced in all sixteen digits by bisection on the direct sum; the 40-digit roots $0.21001044973390\dots$ (Rust levels) and $0.21001044973430\dots$ (reference levels), $4.0\times10^{-13}$ apart; the bounds $B_{direct} = 1.287\times10^{-8}$ and $B_{well} = 3.154\times10^{-16}$ of N8_lamm1_a00_T10 and of all 45 thermal states with $N = 8$ (`Revision/kohn_sham/reports/ks-rust-mermin-roots.json`; Notebook 16c).

**ASSUMED:**

- that the grid errors have the assumed forms (even powers of $h$ for the reference, fourth order for the Rust solver), tested by the ratio test on every level and by a fourth grid for one state, not proved for the self-consistent problem;
- that the measured uncertainties bound the errors (the factor 3 of the tolerance rule allows for estimates that are somewhat too small); Section 16.20 shows one way this can fail: a repeated computation that shares a rounding error does not measure it;
- the inputs shared by both programs, listed in Section 16.25: the functional, the Z2 mirror brane, the good sector; CHOSEN: the regular tip and $L = 3$; CONVENTION, justification OPEN: the filling of the levels; PRESCRIBED BACKGROUND: the history $a_4 = AHx_4$.

**HYPOTHESIS:** none is used in this chapter. **OPEN:** the time-dependent (non-adiabatic) problem, the justification of the filling convention, and any test of the shared inputs (Section 16.25).

### 16.27 Exercises

**Exercise 1 (Richardson by hand).** Notebook 16a prints the Kohn-Sham energy of N8_lamm2_a00 on the three grids: $E_{KS}(300) = 0.002862539189$, $E_{KS}(600) = 0.002862623929$, $E_{KS}(1200) = 0.002862645113$. Compute the convergence ratio, the one-step values $r(h)$ and $r(h/2)$, the three-grid value $R$ and its uncertainty $U$. Compare $R$ with the notebook's $0.0028626521737$ and explain the difference.

*Answer.* The differences are $x(h) - x(h/2) = -8.4740\times10^{-8}$ and $x(h/2) - x(h/4) = -2.1184\times10^{-8}$, and their ratio is $4.0002$: second order. Then $r(h) = (4\cdot0.002862623929 - 0.002862539189)/3 = (0.011450495716 - 0.002862539189)/3 = 0.008587956527/3 = 0.0028626521757$, and $r(h/2) = (4\cdot0.002862645113 - 0.002862623929)/3 = (0.011450580452 - 0.002862623929)/3 = 0.008587956523/3 = 0.0028626521743$. So $R = (16\,r(h/2) - r(h))/15 = r(h/2) + (r(h/2) - r(h))/15 = 0.0028626521743 - 0.0000000000001 = 0.0028626521742$, and $U = |R - r(h/2)| + 2\cdot10^{-12} = 0.9\times10^{-13} + 2\times10^{-12} = 2.1\times10^{-12}$, as in the notebook. Our $R$ differs from the notebook's $0.0028626521737$ by about $5\times10^{-13}$, because the printed grid values are rounded to $10^{-12}$: the weights of $R$ are $\tfrac{64}{45}$, $-\tfrac{20}{45}$ and $\tfrac{1}{45}$, so rounding errors of up to $0.5\times10^{-12}$ in the inputs can move $R$ by up to $\tfrac{64 + 20 + 1}{45}\cdot0.5\times10^{-12} = 0.94\times10^{-12}$. The notebook computes with the unrounded values. (Useful identity: $R = r(h/2) + (r(h/2) - r(h))/15$, which follows from $16r(h/2) - r(h) = 15r(h/2) + (r(h/2) - r(h))$.)

**Exercise 2 (the worst comparison).** The worst comparison of the whole cross-check is the energy density at the tip of N8_lamm2_a00: Rust gives $-10.1822650611886$, the reference $-10.182265056614$, and the tolerance is $9.238\times10^{-9}$ (`Revision/kohn_sham/reports/ks-crosscheck.json`, check emt_brane_tip_values). Compute the difference and the ratio, and the sum $U_{ref} + U_{Rust}$ of the two uncertainties.

*Answer.* $|x_{Rust} - x_{ref}| = 10.1822650611886 - 10.182265056614 = 4.5746\times10^{-9}$. The ratio is $4.5746\times10^{-9}/9.238\times10^{-9} = 0.495$, the largest ratio of the record. The tolerance is $3(U_{ref} + U_{Rust}) + 10^{-12}\max(1, 10.18)$, so $U_{ref} + U_{Rust} = (9.238\times10^{-9} - 1.018\times10^{-11})/3 = 3.076\times10^{-9}$. The difference is about $1.5$ times this sum. Since the difference of two numbers can exceed the sum of their errors only if at least one error exceeds its uncertainty (Section 16.7), at least one of the two estimates is too small at the tip, by a factor of up to about $1.5$. The factor 3 of the rule absorbs this, which is why it is there. Only the comparisons at and near the tip (the classes emt_brane_tip_values and ground_profiles, both with the largest ratio $0.495$) have ratios above $\tfrac13$, where the factor 3 is needed at all.

**Exercise 3 (the factor for a method of order $p$).** A method has the error $x(h) = X + c\,h^p + \dots$. It is run with the step $h$ (result $x_c$) and with $h/2$ (result $x_r$). Show that the error of $x_c$ is $\tfrac{2^p}{2^p - 1}(x_c - x_r)$, and evaluate the factor for $p = 2$ and $p = 4$. Use it to compute $U_{Rust}$ for $E_{KS}$ of N688_lam0_a00, where Notebook 16a measures $|x_c - x_r| = 7.529\times10^{-10}$.

*Answer.* $x_c = X + e$ with $e = ch^p$, and $x_r = X + c(h/2)^p = X + e/2^p$. Subtracting, $x_c - x_r = e(1 - 2^{-p}) = e\,\tfrac{2^p - 1}{2^p}$, so $e = \tfrac{2^p}{2^p - 1}(x_c - x_r)$. For $p = 2$ the factor is $\tfrac43$, for $p = 4$ it is $\tfrac{16}{15}$, the factor of Section 16.6. For N688_lam0_a00: $U_{Rust} = \tfrac{16}{15}\cdot7.529\times10^{-10} = 8.031\times10^{-10}$. (The same algebra gives Richardson's first step: $X = x_r - (x_c - x_r)/(2^p - 1)$, which for $p = 2$ is $(4x_r - x_c)/3$.)

**Exercise 4 (a Sturm count by hand).** Take the even-parity matrix of Section 16.14 for $G = 2$ cells ($h = 1.5$, $M = 1$, $j = +1$): the unknowns are $u_0, w_1, u_1$, and $T = \begin{pmatrix} 0 & a & 0 \\ a & 0 & b \\ 0 & b & 0 \end{pmatrix}$ with $a = \tfrac1h + \tfrac M2$, $b = -\tfrac1h + \tfrac M2$. (i) Compute $a$, $b$ and the three eigenvalues. (ii) Compute the pivots at $x = 0.5$ and the Sturm count $c(0.5)$. (iii) Construct the discrete zero mode. (iv) Compare the positive eigenvalue with the exact level $1.447972$.

*Answer.* (i) $a = \tfrac23 + \tfrac12 = \tfrac76$ and $b = -\tfrac23 + \tfrac12 = -\tfrac16$. The determinant of $T - \varepsilon\mathbb{1}$, expanded along the first row, is $-\varepsilon(\varepsilon^2 - b^2) - a(-a\varepsilon) = -\varepsilon(\varepsilon^2 - a^2 - b^2)$, so the eigenvalues are $0$ and $\pm\sqrt{a^2 + b^2} = \pm\sqrt{\tfrac{49}{36} + \tfrac{1}{36}} = \pm\sqrt{\tfrac{50}{36}} = \pm1.178511$. (ii) $q_1 = 0 - 0.5 = -0.5$; $q_2 = 0 - 0.5 - a^2/q_1 = -0.5 + 1.361111/0.5 = -0.5 + 2.722222 = 2.222222$; $q_3 = 0 - 0.5 - b^2/q_2 = -0.5 - 0.027778/2.222222 = -0.5 - 0.0125 = -0.5125$. Two pivots are negative, so $c(0.5) = 2$: indeed two eigenvalues, $-1.178511$ and $0$, lie below $0.5$. (iii) $q = (1 + Mh/2)/(1 - Mh/2) = 1.75/0.25 = 7$, so $u_1 = 7u_0$ and $w_1 = 0$. Check the row of $w_1$: $a\,u_0 + b\,u_1 = \tfrac76u_0 - \tfrac16\cdot7u_0 = 0$. Normalised with $\sum u^2h = 1$: $u_0^2(1 + 49)\cdot1.5 = 1$, so $u_0 = 0.11547$, $u_1 = 0.80829$. (iv) The coarse grid gives $1.178511$ instead of $1.447972$, an error of $0.27$: with only two cells the $h^2$ error is large, and Notebook 16b shows how it shrinks by a factor 4 per halving of $h$.

**Exercise 5 (how many halvings).** For the even-parity matrix with $G = 300$ cells ($M = 1$, $L = 3$, $k = 0$), find Gershgorin's starting interval and the number of bisection steps needed to locate the zero mode to $10^{-14}$.

*Answer.* $h = 3/300 = 0.01$, so the neighbour entries are $\tfrac1h + \tfrac12 = 100.5$ and $-\tfrac1h + \tfrac12 = -99.5$. Every inner row has the radius $100.5 + 99.5 = 200$ and the diagonal is zero, so the interval is $[\min(d - \rho) - 1, \max(d + \rho) + 1] = [-201, 201]$, of width $W = 402$. After $n$ halvings the width is $402/2^n$, and $402/2^n \le 10^{-14}$ needs $2^n \ge 4.02\times10^{16}$, that is $n \ge \log_2(4.02\times10^{16}) = 55.2$: 56 halvings. (For $G = 150$ the same reasoning gives 55, the number of Notebook 16b; doubling $G$ doubles $W$ and costs one more halving.)

**Exercise 6 (the accuracy of the discrete zero mode).** For $G = 150$ ($h = 0.02$, $M = 1$), compute $\ln q$ to nine decimals with the series of Section 16.15 and compare with $Mh$. By how much does the discrete exponential grow faster than $e^{My}$ across the whole interval $L = 3$, and is this consistent with the distance $6.93\times10^{-5}$ that Notebook 16b measures?

*Answer.* $\ln q = Mh + (Mh)^3/12 + \dots = 0.02 + 0.000008/12 = 0.02 + 0.000000667 = 0.020000667$ (the next term, $(Mh)^5/80 = 4\times10^{-11}$, does not change these digits). So the discrete exponential grows like $e^{1.0000333\,y}$ instead of $e^{y}$: over the 150 cells the exponents differ by $150\cdot6.67\times10^{-7} = 1.0\times10^{-4}$, a relative difference of $10^{-4}$ between the two ends. After both are normalised to $\int a^2dy = 1$, the difference is shared between the two ends, about $\pm0.5\times10^{-4}$ in relative size, and with values of $a$ up to $1.42$ at the brane this is about $7\times10^{-5}$: consistent with the measured $6.93\times10^{-5}$. The error is of order $h^2$, as the relative rate error $(Mh)^2/12$ shows.

**Exercise 7 (the chemical potential of N8_lamm1_a00_T10 by hand).** With the levels $\varepsilon_0 = 0.000245562708$ ($g_0 = 8$), $\varepsilon_1 = 0.430761462627$ ($g_1 = 24$), $\varepsilon_2 = 0.587973061749$ ($g_2 = 48$) and $T = 0.01$: (i) evaluate the two-level estimate of Section 16.20; (ii) show that the thermal particles of the level $\varepsilon_2$ lower $\mu$ by about $\tfrac T2P_2/P_1$ and evaluate the correction; (iii) compare with the 40-digit root $0.2100104497339$.

*Answer.* (i) $\mu_0 = \tfrac{0.000245562708 + 0.430761462627}{2} - 0.005\ln3 = 0.215503512668 - 0.005493061443 = 0.210010451225$. (ii) The Mermin condition $H = P_1 + P_2$ reads $g_0e^{-(\mu - \varepsilon_0)/T} = g_1e^{-(\varepsilon_1 - \mu)/T}(1 + P_2/P_1)$. Taking logarithms as in Section 16.20 gives $\mu = \mu_0 - \tfrac T2\ln(1 + P_2/P_1) \approx \mu_0 - \tfrac T2\,\tfrac{P_2}{P_1}$, because $\ln(1 + s) \approx s$ for small $s$. With $\mu \approx 0.2100104$: $P_2 = 48\,e^{-(0.587973 - 0.210010)/0.01} = 48\,e^{-37.796} = 48\cdot3.85\times10^{-17} = 1.85\times10^{-15}$ and $P_1 = H = 6.21\times10^{-9}$, so $P_2/P_1 = 2.97\times10^{-7}$ and the correction is $0.005\cdot2.97\times10^{-7} = 1.49\times10^{-9}$. (iii) $\mu \approx 0.210010451225 - 0.000000001488 = 0.210010449737$, within about $3\times10^{-12}$ of the 40-digit root $0.2100104497339$ (the remaining difference comes from the approximations $1/(1 + e^s) \approx e^{-s}$ and $\ln(1 + s) \approx s$, and from rounding the levels to twelve decimals). The direct sum in doubles can hardly see the level $\varepsilon_2$: its particles, $1.8\times10^{-15}$, are one or two spacings of the doubles near 8, so the direct sum blurs an effect that moves $\mu$ by $1.5\times10^{-9}$, the size of the error of the first cross-check.

**Exercise 8 (another activated state).** For the state N8_lam0_a00_T10 the record gives $n = 5$ levels and $dN/d\mu = 1.229\times10^{-6}$ (`Revision/kohn_sham/reports/ks-rust-mermin-roots.json`). Estimate the width of the interval of $\mu$ on which the direct residual is exactly zero, and the main term of $B_{direct}$. Compare with the error of the direct sum for this state printed by Notebook 16c ($+2.72\times10^{-10}$).

*Answer.* The width is $3\cdot2^{-51}/N' = 1.332\times10^{-15}/1.229\times10^{-6} = 1.08\times10^{-9}$, as for N8_lamm1_a00_T10, because $N'$ is almost the same. The main term of the bound is $(n + 2)\,\epsilon_{mach}N/N' = 7\cdot2.220\times10^{-16}\cdot8/1.229\times10^{-6} = 1.012\times10^{-8}$, the record's $1.012\times10^{-8}$ (the other terms are about $10^{-16}$). The actual error, $2.72\times10^{-10}$, lies inside the zero interval's width and far inside the bound. Its sign is positive here: where the zero interval lies relative to the root depends on how the individual terms of the sum are rounded, so bisection can stop above or below the root. A bound tells how large an error can be; it does not tell its sign.
