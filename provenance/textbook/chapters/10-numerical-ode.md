## 10. Solving differential equations on a computer from zero

### 10.1 What this chapter does

Most equations of this book cannot be solved with pencil and paper once the background changes in time or the particles interact. The Stage-3 experiments of Chapter 11 follow a 16-component complex spinor through expanding and deflating universes; the Kohn–Sham calculation of Chapter 13 has to find the stationary states of many quanta in the static primordial field. In both cases the computer solves **ordinary differential equations**, equations for functions of one variable, with a program called **CVODE**. This chapter explains from zero what that program does, why each of its settings was chosen, and, most importantly, why we may trust its answers: every numerical result of Stage 3 is checked by independent programs against exact solutions, conservation laws and each other; the Stage-4 results and the status of their independent cross-check are described in Chapter 13.

The sources of this chapter are these files of the repository.

| Source | What this chapter takes from it |
| --- | --- |
| `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md` | the Stage-3 document: §5 (method and verification strategy) and the solver and verification sections of each experiment, cited as §N |
| `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` | §4.5 (engines), §5.2 (FMA), §6.9 (real state layout), §6.16 (CVODE), §7 and §8 (program and files), §13 (exercises) |
| `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md` | the Stage-2 document: §14.1 (the exact mode solution), §13.5 and §15.5 (negative controls), cited as Stage-2 §N |
| `handoff/specs/NUMERICS_CONTRACT.md` | the numerical programme and its errata |
| `studies/dirac16complex_cosmology/src/driver.rs` | the CVODE driver |
| `studies/dirac16complex_cosmology/src/output.rs` and `src/exp1.rs` to `src/exp5.rs` | the output format and the solver settings of the five experiments |
| `scripts/check_dirac16complex_exp1.py` to `..._exp5.py` | the independent checkers |
| `artifacts/dirac16complex/numerics/expN/summary.json` | settings, solver statistics and self-checks of experiment N = 1, ..., 5 |
| `artifacts/dirac16complex/numerics/expN/python-check-report.json` | the results of the independent checker of experiment N |
| `artifacts/dirac16complex/numerics/mathematica-report.json` | the checks and negative controls of the Mathematica notebook |
| `scripts/build_dirac16complex_mathematica_notebook.wls` | the finite-difference test of the Mathematica notebook (function `fdCheck`) |
| `studies/dirac16complex_kohn_sham/src/shooting.rs` and `handoff/specs/STAGE4_SPEC.md` | the level search of the Stage-4 shooting solver and its plan (§5) |

Every number about the project's runs in this chapter is copied from those files. The small examples that teach the methods (in Sections 10.2 to 10.8, 10.11 and 10.12) are ordinary arithmetic that the reader can repeat with a pocket calculator.

### 10.2 Ordinary differential equations

**Definitions.** Let $t$ be a real variable (a time, or a position along a line) and $y(t)$ an unknown function. An **ordinary differential equation** (ODE) is an equation that relates $y$ and some of its derivatives $y'=dy/dt$, $y''=d^2y/dt^2$, and so on, at the same $t$. Its **order** is the highest derivative that occurs. A **system** of ODEs has several unknown functions $y_0(t),\dots,y_{n-1}(t)$, which we collect into one column, the **state vector** $Y(t)=(y_0,\dots,y_{n-1})^T$. Every system we meet can be written in the **first-order form**

$$
Y'(t)=f\bigl(t,Y(t)\bigr),
$$

where $f$ is a given rule, the **right-hand side**, that produces a column of $n$ numbers from $t$ and $Y$. Together with a **start value** $Y(t_0)=Y_0$ it is an **initial-value problem**.

**Example 1 (decay).** $y'=-y$ with $y(0)=1$ has the solution $y(t)=e^{-t}$: indeed $\tfrac{d}{dt}e^{-t}=-e^{-t}$ and $e^0=1$.

**Example 2 (oscillation, and how to lower the order).** The oscillator $x''=-\omega^2x$ is second order. Introduce the velocity $v=x'$ as a second unknown. Then $x'=v$ and $v'=x''=-\omega^2x$, a first-order system with $Y=(x,v)^T$ and $f(t,Y)=(v,\,-\omega^2x)^T$. Every equation of higher order can be lowered in this way.

**Existence and uniqueness.** If $f$ is smooth (it has continuous derivatives with respect to $Y$), then the initial-value problem has exactly one solution, at least for some time around $t_0$ (the theorem of Picard and Lindelöf, quoted here without proof). A numerical method tries to approximate that one solution.

**The project's equation.** The mode equation of the Stage-3 experiments (Chapter 11; Stage-3 document §4.5) is

$$
i\,\dot u=h(t)\,u,\qquad u(t)\in\mathbb C^{16},
$$

where the dot is $d/dt$, $t=x_4$, and $h(t)$ is a 16 by 16 complex matrix, the mode Hamiltonian, for example $h=-iM_{\mathrm{eff}}\gamma^4-K\gamma^4\gamma^0$ in experiment EXP-1. CVODE works with real numbers only, so the complex equation is split into real and imaginary parts. Write $u=x+iy$ and $h=h_r+ih_i$ with real columns $x,y$ and real matrices $h_r,h_i$. Then $i(\dot x+i\dot y)=(h_r+ih_i)(x+iy)$. The left side is $i\dot x-\dot y$; the right side is $(h_rx-h_iy)+i(h_ix+h_ry)$. Comparing real parts and imaginary parts:

$$
\dot x=h_ry+h_ix,\qquad \dot y=h_iy-h_rx .
$$

These are 32 real first-order equations. Where further quantities are integrated together with the spinor, the state is longer: 38 reals in EXP-2 (the logarithms of the three scale factors of the metric and their three rates of change besides $u$), 35 in EXP-3 (the time, a distance and the logarithm $\ln\sigma$ of the scaled density $\sigma$ besides $u$) and 33 in the smooth-transition runs of EXP-4 (the logarithm $\ln a$ of the scale factor besides $u$) (Stage-3 document §7.2, §8.2 and §9.2; these experiments are Chapter 11). The program stores the spinor part as 32 consecutive numbers, first the 16 real parts, then the 16 imaginary parts (the columns `u_re_0` to `u_re_15` and `u_im_0` to `u_im_15` of every output file that stores the spinor, for example `exp1/run_A1_K0_pos_Bp.csv`; student guide §6.9). **A worked component.** For zero momentum the matrix is $h=-iM\gamma^4$, so $h_r=0$ and $h_i=-M\gamma^4$. Row 0 of $\gamma^4$ has its single entry $-1$ in column 13 (Chapter 2), so $(\gamma^4x)_0=-x_{13}$ and the first equation reads $\dot x_0=(h_ix)_0=-M(-x_{13})=M\,x_{13}$: one multiplication.

**An exact solution to test against.** When $h$ is a constant matrix with $h^2=E^2\cdot1$ for a number $E>0$ (true in EXP-1, where $E=\sqrt{M_{\mathrm{eff}}^2+K^2}$; Stage-2 document §14.1), the solution is known exactly. Formally $u(t)=e^{-iht}u_0$, where the exponential of a matrix is defined by its power series $e^{A}=\sum_{n\ge0}A^n/n!$. Split the series into even and odd powers and use $h^{2k}=E^{2k}\cdot1$ and $h^{2k+1}=E^{2k}h$:

$$
e^{-iht}=\sum_{k\ge0}\frac{(-1)^k(Et)^{2k}}{(2k)!}\cdot1-i\,\frac hE\sum_{k\ge0}\frac{(-1)^k(Et)^{2k+1}}{(2k+1)!}=\cos(Et)\cdot1-i\sin(Et)\,\frac hE .
$$

**Worked example.** The 2 by 2 matrix $h=\begin{pmatrix}3&4\\4&-3\end{pmatrix}$ has $h^2=25\cdot1$, so $E=5$. For $u_0=(1,0)^T$:

$$
u(t)=\Bigl(\cos5t-\tfrac{3i}{5}\sin5t,\ -\tfrac{4i}{5}\sin5t\Bigr)^T,\qquad u^\dagger u=\cos^25t+\tfrac{9}{25}\sin^25t+\tfrac{16}{25}\sin^25t=1 .
$$

The length $u^\dagger u$ stays exactly 1 for all $t$. This is general: for a Hermitian $h$ ($h^\dagger=h$) the quantity $u^\dagger u$ is conserved, because $\tfrac{d}{dt}(u^\dagger u)=\dot u^\dagger u+u^\dagger\dot u=(iu^\dagger h)u+u^\dagger(-ihu)=0$. Exact solutions and conserved quantities are the two strongest tests of a numerical solution (Section 10.11).

### 10.3 Euler's method and the idea of error

**The method.** Choose a **step size** $h>0$ (here $h$ is a small number, not the Hamiltonian) and the times $t_n=t_0+nh$. Taylor's theorem says $y(t+h)=y(t)+h\,y'(t)+\tfrac12h^2y''(\xi)$ for some $\xi$ between $t$ and $t+h$. Dropping the last term and using $y'=f(t,y)$ gives **Euler's method**:

$$
Y_{n+1}=Y_n+h\,f(t_n,Y_n),
$$

where $Y_n$ is the computed approximation of $Y(t_n)$.

**Local and global error.** One step makes the error $\tfrac12h^2y''$, the **local error**, proportional to $h^2$. To reach a fixed end time $T$ one needs $N=(T-t_0)/h$ steps, and the local errors add up to a **global error** of order $N\cdot h^2\propto h$. A method whose global error is proportional to $h^p$ is said to have **order** $p$. Euler's method has order 1.

**Worked example.** Solve $y'=-y$, $y(0)=1$ up to $t=1$. Each Euler step multiplies by $1-h$, so $Y_N=(1-h)^N$ with $N=1/h$. The exact value is $e^{-1}=0.367879$.

| Step $h$ | Steps $N$ | Euler value $(1-h)^N$ | Error | Error ratio |
| --- | --- | --- | --- | --- |
| 0.5 | 2 | 0.250000 | 0.117879 | — |
| 0.25 | 4 | 0.316406 | 0.051473 | 2.29 |
| 0.125 | 8 | 0.343609 | 0.024271 | 2.12 |
| 0.0625 | 16 | 0.356074 | 0.011805 | 2.06 |

Halving the step halves the error (the ratio tends to $2^1=2$): order 1 confirmed. The method **converges**, the error tends to 0 as $h\to0$, but slowly: the error is close to $0.19\,h$, so for 6 correct digits (an error below $5\times10^{-7}$) Euler would need a step of about $2.6\times10^{-6}$, that is about 400000 steps. Better methods (Section 10.6) reach the same accuracy with far fewer steps.

### 10.4 Stability: decay and oscillation

**The test equation.** Much can be learned from $y'=\lambda y$ with a constant, possibly complex, number $\lambda$. Its exact solution $y=e^{\lambda t}y_0$ decays if the real part $\mathrm{Re}\,\lambda<0$ and oscillates with constant size if $\lambda=i\omega$ is purely imaginary. A one-step method applied to it multiplies $y$ by a fixed **amplification factor** $R(z)$ per step, with $z=h\lambda$:

- **explicit Euler** $Y_{n+1}=Y_n+h\lambda Y_n$ gives $R(z)=1+z$;
- **implicit (backward) Euler** $Y_{n+1}=Y_n+h\lambda Y_{n+1}$ gives, solving for $Y_{n+1}$, $R(z)=1/(1-z)$;
- **the trapezoidal rule** $Y_{n+1}=Y_n+\tfrac h2\lambda(Y_n+Y_{n+1})$ gives $R(z)=(1+z/2)/(1-z/2)$.

A method is **stable** for a given $z$ if $\lvert R(z)\rvert\le1$, so that errors do not grow from step to step. The set of such $z$ is the method's **stability region**.

**Oscillation.** For $\lambda=i\omega$ the exact factor per step is $\lvert e^{i\omega h}\rvert=1$. Explicit Euler has $\lvert1+i\omega h\rvert=\sqrt{1+\omega^2h^2}>1$: the numerical oscillation grows. With $\omega=1$ and $h=0.1$, after 100 steps (up to $t=10$) the squared size $\lvert y\rvert^2$ has grown by $(1.01)^{100}=2.70$. Backward Euler has $\lvert R\rvert=1/\sqrt{1+\omega^2h^2}<1$: the oscillation is damped, $\lvert y\rvert^2$ falls by $(1.01)^{-100}=0.370$. The trapezoidal rule has $\lvert R\rvert=\lvert1+i\omega h/2\rvert/\lvert1-i\omega h/2\rvert=1$ exactly: it keeps the size of an oscillation (Exercise 10.3). The lesson for the mode equation $i\dot u=hu$, whose right-hand side $-ihu$ has purely imaginary eigenvalues when $h$ is Hermitian, is that a method can gain or lose norm purely by its own error. Monitoring the conserved $u^\dagger u$ therefore measures the accuracy of the integration directly (Section 10.11).

**Decay.** For $\lambda=-1$ the trapezoidal rule gives $y(1)=\bigl(\tfrac{1-h/2}{1+h/2}\bigr)^{1/h}$: $0.360000$ for $h=0.5$ (error $0.0079$) and $0.365950$ for $h=0.25$ (error $0.0019$). The error falls by a factor 4.1 when $h$ is halved: the trapezoidal rule has order 2.

### 10.5 Stiffness

**Definition.** A problem is **stiff** when it contains components that decay much faster than the solution we are interested in changes. An explicit method is then forced, by stability and not by accuracy, to take steps as small as the fastest decay time, even long after the fast components have died away.

**Example.** Consider $y'=-1000\,(y-\cos t)-\sin t$. Its solution with $y(0)=y_0$ is $y(t)=\cos t+(y_0-1)\,e^{-1000t}$ (check: $y'=-\sin t-1000(y_0-1)e^{-1000t}$, and $-1000(y-\cos t)=-1000(y_0-1)e^{-1000t}$). After a time of about $0.005$ the second term is gone and $y=\cos t$ changes slowly. But an error $\delta$ added to $y$ obeys $\delta'=-1000\,\delta$, the test equation with $\lambda=-1000$. Explicit Euler multiplies it by $1-1000h$ per step, and it stays bounded only if $\lvert1-1000h\rvert\le1$, that is $h\le0.002$. With $h=0.01$, a step that would describe $\cos t$ perfectly well, the factor is $-9$ and any rounding error grows ninefold per step. Backward Euler multiplies the error by $1/(1+1000h)=1/11$ at $h=0.01$: it is damped for every step size. The price is that each step of an implicit method requires solving an equation for $Y_{n+1}$ (Section 10.7).

**Are the project's equations stiff?** In the good sector (no momentum along the extra times) the mode equations are oscillations: $h$ is Hermitian and the right-hand side $-ihu$ has purely imaginary eigenvalues. In the extra-time experiment EXP-5 the matrix $h$ satisfies $h^2=E^2(t)\cdot1$ with $E^2(t)=m^2-Q(t)^2$, where $m$ is the mass and $Q(t)$ a momentum along an extra time that grows as the extra times deflate, so that $E^2$ turns negative at a time $t_\ast$ (Chapter 11). If $hv=\lambda v$ for a vector $v\ne0$, then $\lambda^2v=h^2v=E^2v$, so every eigenvalue of $h$ satisfies $\lambda^2=E^2$. Before $t_\ast$ ($E^2>0$) the eigenvalues of $-ih$ are therefore imaginary, $\mp iE$; after it ($E^2<0$) they are real, $\pm\varkappa$ with $\varkappa=\sqrt{Q^2-m^2}$. The runs have $m=1$ and end three time units after $t_\ast$, where $Q=me^3$ (Stage-3 document §10.2 and §10.3), so $\varkappa$ grows to at most $\sqrt{e^6-1}=20.06$ (computed here). So after $t_\ast$ one component grows and one decays, both at the same moderate rate $\varkappa$. In none of these problems does a component decay much faster than the solution changes, so none of them is **stiff** (Stage-3 document §5.1 and §10.2; header of `src/driver.rs`). This is why four of the five experiments use a method designed for non-stiff problems (Adams–Moulton, Section 10.6), and why a test in EXP-4 found it both more accurate and cheaper than the stiff method (Section 10.8).

### 10.6 Multistep methods: Adams and BDF

A **linear multistep method** uses several past values to make one step. CVODE offers two families (student guide §6.16).

**Adams methods** integrate the equation, $Y(t_{n+1})=Y(t_n)+\int_{t_n}^{t_{n+1}}f\,dt$, and replace $f$ under the integral by the polynomial that interpolates its known values. *Adams–Bashforth of order 2.* Through the two known values $f_{n-1}$ and $f_n$ (with $f_n=f(t_n,Y_n)$) passes the straight line $p(t)=f_n+(t-t_n)(f_n-f_{n-1})/h$. Its integral over $[t_n,t_n+h]$ is $hf_n+\tfrac{h^2}{2}\cdot\tfrac{f_n-f_{n-1}}{h}$, so

$$
Y_{n+1}=Y_n+\frac h2\bigl(3f_n-f_{n-1}\bigr).
$$

This is **explicit**: everything on the right is known. *Adams–Moulton* methods include the unknown value $f_{n+1}$ among the interpolation points, which makes them **implicit** and more accurate. The simplest one that uses $f_n$ and $f_{n+1}$ is the trapezoidal rule of Section 10.4, $Y_{n+1}=Y_n+\tfrac h2(f_n+f_{n+1})$. CVODE's Adams–Moulton family has the orders 1 to 12.

**Backward differentiation formulas (BDF)** interpolate $Y$ instead of $f$: they pass a polynomial through the unknown $Y_{n+1}$ and the known $Y_n,Y_{n-1},\dots$, differentiate it at $t_{n+1}$, and set the derivative equal to $f(t_{n+1},Y_{n+1})$. With one past value this is backward Euler. *BDF of order 2.* Let $s=(t-t_{n+1})/h$. The quadratic

$$
p(s)=Y_{n+1}+s\,(Y_{n+1}-Y_n)+\frac{s(s+1)}{2}\,(Y_{n+1}-2Y_n+Y_{n-1})
$$

takes the values $Y_{n+1}$, $Y_n$ and $Y_{n-1}$ at $s=0,-1,-2$ (put them in: at $s=-1$ the last term vanishes and $p=Y_n$; at $s=-2$ it is $Y_{n+1}-2(Y_{n+1}-Y_n)+(Y_{n+1}-2Y_n+Y_{n-1})=Y_{n-1}$). Its time derivative is $\tfrac1h\,dp/ds$, and at $s=0$

$$
\frac1h\Bigl[(Y_{n+1}-Y_n)+\tfrac12(Y_{n+1}-2Y_n+Y_{n-1})\Bigr]=\frac{\tfrac32Y_{n+1}-2Y_n+\tfrac12Y_{n-1}}{h}=f(t_{n+1},Y_{n+1}).
$$

CVODE's BDF family has the orders 1 to 5. BDF methods are very stable for decaying components, which makes them the standard choice for stiff problems, and like backward Euler they slightly damp oscillations.

**Variable step, variable order.** CVODE does not use a fixed $h$: after every step it estimates the error (Section 10.8) and chooses the next step size and the order within its family. The number of steps it takes is reported in every summary file of the project.

**One implicit equation per step.** Both implicit families lead to an equation of the form

$$
Y_{n+1}=\gamma\,f(t_{n+1},Y_{n+1})+a_n ,
$$

with a number $\gamma$ proportional to $h$ and a known vector $a_n$ built from past values. For the trapezoidal rule $\gamma=h/2$ and $a_n=Y_n+\tfrac h2f_n$; for BDF2, multiplying the BDF2 formula above, $(\tfrac32Y_{n+1}-2Y_n+\tfrac12Y_{n-1})/h=f(t_{n+1},Y_{n+1})$, by $\tfrac23h$ and solving for $Y_{n+1}$ gives $Y_{n+1}=\tfrac23h\,f(t_{n+1},Y_{n+1})+\tfrac43Y_n-\tfrac13Y_{n-1}$, so $\gamma=\tfrac23h$ and $a_n=\tfrac13(4Y_n-Y_{n-1})$.

### 10.7 Solving the implicit equation: fixed point or Newton

**Fixed-point iteration.** Start from a guess $Y^{(0)}$ (CVODE uses an explicit prediction) and repeat $Y^{(m+1)}=\gamma f(t_{n+1},Y^{(m)})+a_n$. The error of the iterate is multiplied at each iteration by about $\gamma J$, where $J=\partial f/\partial Y$ is the **Jacobian matrix** of the right-hand side (its entry in row $r$ and column $c$ is $\partial f_r/\partial Y_c$). *Derivation.* Let $Y^\ast$ be the exact solution of the implicit equation, $Y^\ast=\gamma f(t_{n+1},Y^\ast)+a_n$, and let $e^{(m)}=Y^{(m)}-Y^\ast$ be the error of the $m$-th iterate. Subtracting the equation for $Y^\ast$ from the iteration gives $e^{(m+1)}=\gamma\bigl[f(t_{n+1},Y^\ast+e^{(m)})-f(t_{n+1},Y^\ast)\bigr]$. The linear approximation of Section 1.9, applied to each component $f_r$ as a function of the components $Y_0,Y_1,\dots$ of $Y$, gives for a small column $d$ the expansion $f_r(t,Y^\ast+d)=f_r(t,Y^\ast)+\sum_c(\partial f_r/\partial Y_c)\,d_c+\dots$, that is $f(t,Y^\ast+d)=f(t,Y^\ast)+J\,d+\dots$, where the dots are terms of second order in $d$. With $d=e^{(m)}$ and those terms dropped, $e^{(m+1)}\approx\gamma J\,e^{(m)}$. The iteration therefore converges when $\gamma$ times the size of $J$ is below 1. For the test equation $y'=\lambda y$ the Jacobian is the number $\lambda$, there are no second-order terms, and the factor is exactly $\gamma\lambda$. *Worked example.* Backward Euler for $y'=-y$ with $h=0.1$ from $y_n=1$: $\gamma=h$, $a_n=1$, and the iteration is $Y\leftarrow1-0.1\,Y$. From $Y^{(0)}=1$ it gives $0.9$, $0.91$, $0.909$, $0.9091$, $0.90909$, approaching the exact solution $1/1.1=0.909090\ldots$; each iteration gains one digit, because $\gamma\lambda=-0.1$ (the errors $+0.0909$, $-0.0091$, $+0.0009$, ... shrink tenfold and alternate in sign). For the stiff $\lambda=-1000$ the same factor would be 100 and the iteration would diverge. Fixed-point iteration needs no Jacobian and no linear algebra, and it is the classical partner of Adams methods for non-stiff problems.

**Newton's method.** For one unknown $x$ and an equation $g(x)=0$, **Newton's method** replaces $g$ near the current guess $x^{(m)}$ by its linear approximation $g(x^{(m)})+g'(x^{(m)})\,(x-x^{(m)})$, the tangent line of the graph, and takes the zero of that line as the next guess:

$$
x^{(m+1)}=x^{(m)}-\frac{g(x^{(m)})}{g'(x^{(m)})}.
$$

*Worked example.* For $g(x)=x^2-2$, with $g'(x)=2x$, from $x^{(0)}=1$: $x^{(1)}=1-(-1)/2=1.5$, $x^{(2)}=1.5-0.25/3=1.416667$ and $x^{(3)}=1.416667-0.006944/2.833333=1.414216$, against $\sqrt2=1.414214$. The errors $0.086$, $0.0025$ and $2.1\times10^{-6}$ are each roughly the square of the one before (times a fixed factor), so the number of correct digits roughly doubles at every iteration.

For the implicit equation of a step, write it as $G(Y)=Y-\gamma f(t_{n+1},Y)-a_n=0$. Near the current iterate the linear approximation of Section 1.9 gives $G(Y^{(m)}+d)=G(Y^{(m)})+(1-\gamma J)\,d+\dots$ for a small column $d$, because the matrix of derivatives of $Y$ with respect to $Y$ is the unit matrix $1$ and that of $\gamma f$ is $\gamma J$ (with $J$ taken at $Y^{(m)}$). Newton's method sets the linear part to zero, $(1-\gamma J)\,d=-G(Y^{(m)})$, and takes $Y^{(m+1)}=Y^{(m)}+d$:

$$
Y^{(m+1)}=Y^{(m)}-\bigl(1-\gamma J\bigr)^{-1}G\bigl(Y^{(m)}\bigr).
$$

For a linear right-hand side, $f(t,Y)=A(t)\,Y+b(t)$ with a matrix $A$ and a column $b$, the Jacobian is $J=A$, and $G(Y^{(m)}+d)=G(Y^{(m)})+(1-\gamma A)\,d$ holds exactly, with no dropped terms. The step $d$ therefore makes $G(Y^{(m+1)})=0$: one iteration is exact, whatever the stiffness (provided $1-\gamma A$ is invertible). The price is the Jacobian and the solution of a linear system with the matrix $1-\gamma J$. CVODE can estimate the Jacobian by **difference quotients**: column $c$ is approximately $\bigl[f(t,Y+\delta e_c)-f(t,Y)\bigr]/\delta$ for a small $\delta$, where $e_c$ is the $c$-th unit column, so one estimate costs one extra evaluation of $f$ per state component. For a linear $f$ this quotient is $\bigl[A(Y+\delta e_c)+b-AY-b\bigr]/\delta=Ae_c$, the column $c$ of $A$, so the estimate is exact up to rounding. The linear system is then solved by a **dense direct solver** (Gaussian elimination on the full matrix).

**The two configurations of the project.** The driver `studies/dirac16complex_cosmology/src/driver.rs` offers exactly two, and every summary file records which one was used:

- BDF with Newton iteration and the dense direct linear solver, using the difference-quotient Jacobian, called `Method::Bdf` in the code: used for EXP-1 (according to the driver's header it is the house style of the related projects dirac-main and planet_Mercury);
- Adams–Moulton with fixed-point iteration and no linear solver, called `Method::Adams` in the code: used for EXP-2 to EXP-5.

The EXP-4 method test of Section 10.8 shows the cost of the Jacobian: its BDF runs spent 2464 and 164384 right-hand-side evaluations on difference-quotient Jacobians, which are $77\times32$ and $5137\times32$, one evaluation per component of the 32-dimensional state (this factorization is our reading of the recorded counts).

### 10.8 Error control: rtol, atol and max_step

**The local error test.** After each step CVODE estimates the local error $e_c$ of every component $c$ of the state (by comparing the implicit solution with its explicit prediction; we quote this from the CVODE design and do not derive it). It then forms the **weighted root-mean-square norm**

$$
\lVert e\rVert=\sqrt{\frac1n\sum_{c=0}^{n-1}\Bigl(\frac{e_c}{\mathrm{rtol}\cdot\lvert Y_c\rvert+\mathrm{atol}}\Bigr)^2}
$$

and accepts the step if $\lVert e\rVert\le1$; otherwise it repeats the step with a smaller $h$. Here **rtol** is the **relative tolerance** (the accepted error as a fraction of the size of each component) and **atol** the **absolute tolerance** (the accepted error for components that are near zero, where $\mathrm{rtol}\cdot\lvert Y_c\rvert$ would be useless). A third setting, **max_step**, caps the step size.

**Worked example.** Let $\mathrm{rtol}=10^{-6}$, $\mathrm{atol}=10^{-8}$, $Y=(2,0)$ and estimated errors $e=(10^{-6},5\times10^{-9})$. The weights are $10^{-6}\cdot2+10^{-8}=2.01\times10^{-6}$ and $0+10^{-8}=10^{-8}$; the ratios are $0.4975$ and $0.5$; the norm is $\sqrt{(0.4975^2+0.5^2)/2}=0.4988\le1$, so the step is accepted. Without atol the second weight would be zero and no step could ever be accepted for a component that passes through zero.

**Tolerances bound the local error, not the global error.** The per-step errors accumulate over thousands of steps. The figure shows it for EXP-1: the drifts of the conserved energy density and of the two norms grow steadily with time, while staying below $5\times10^{-9}$ (the committed values in `artifacts/dirac16complex/numerics/exp1/summary.json`: largest drift of $\rho$ $4.19\times10^{-9}$, of the norms $2.70\times10^{-9}$). At the tolerance $\mathrm{rtol}=10^{-12}$ the largest distance from the exact solution over the 26 runs is $6.25\times10^{-9}$ (measurement `maxExactError`), several thousand times rtol. Each experiment therefore checks itself against exact solutions or conserved quantities rather than trusting the tolerance.

![EXP-1 of Stage 3, where every quantity should stay exactly constant. Panels (a) to (d) show the energy density, the mean pressure, the Lagrangian split and the equation of state of several runs, flat as expected (the dashed mixed state oscillates for a physical reason explained in Chapter 11). Panels (e) and (f) show the numerical drifts of $\rho$ and of the Hilbert and Krein norms for all 26 runs: they grow with time as the local errors accumulate and stay below about $5\times10^{-9}$.](artifacts/dirac16complex/numerics/figures/exp1_frozen_observables.png)

**The settings of the five experiments** (from the `tolerances`, `solver` and `solverTotals` entries of the five `summary.json` files):

| Run | Method | rtol | atol | max_step | Steps | RHS evaluations |
| --- | --- | --- | --- | --- | --- | --- |
| EXP-1 | BDF + Newton + dense | $10^{-12}$ | $10^{-14}$ | 0.02 | 33866 | 34950 |
| EXP-2 | Adams + fixed point | $10^{-12}$ | $10^{-15}$ | 0.02 | 1779784 | 1781396 |
| EXP-3 | Adams + fixed point | $10^{-11}$ | $10^{-13}$ | 0.01 | 6074 | 10115 |
| EXP-4 | Adams + fixed point | $10^{-13}$ | $10^{-14}$ | 2.0 | 339071692 | 511425232 |
| EXP-5 | Adams + fixed point | $10^{-10}$ | $10^{-12}$ | 0.02 | 2548 | 4800 |

**Why these values: four measured stories.**

1. **EXP-1: tighten the tolerance, never relax the limit.** The checks of EXP-1 require the conserved quantities to drift by less than $10^{-8}$ (the `limits` entry of its summary). At $\mathrm{rtol}=10^{-10}$ the quantities that should stay constant drifted by up to $1.2\times10^{-7}$ ($\rho$), $5.4\times10^{-8}$ (the Hilbert and Krein norms) and $1.4\times10^{-8}$ (the mass $M_{\mathrm{eff}}$ of the interacting run), and the pressure check failed as well, all against the limit $10^{-8}$, while the distance from the exact solution, $7.8\times10^{-8}$, still passed its limit $10^{-7}$ (student guide Exercise 13.1, which reruns EXP-1 with `--rtol 1e-10` and lets you watch the checks fail; the Stage-3 document §6.4 quotes drifts of about $4\times10^{-8}$, which this rerun does not reproduce). So the tolerance was tightened to $10^{-12}$ instead of loosening the limit.
2. **EXP-2: why a step cap.** Without max_step the Adams method took steps of about 0.045 and made an amplitude error of about $5\times10^{-13}$ per step on the oscillating spinor. Over times of order $10^4$ this drifted the conserved scalar density by $1.7\times10^{-7}$ and pushed the residual of the Einstein constraint to $3\times10^{-8}$. With the cap 0.02 the relative constraint residual stays below $1.26\times10^{-10}$ (Stage-3 document §7.4; measurement `maxConstraintRelative` in `exp2/summary.json`).
3. **EXP-4: error follows rtol.** Each thermal mode turns through about $10^5$ radians. The largest deviation of the conserved $u^\dagger u$ from 1 was $2.4\times10^{-4}$ at $\mathrm{rtol}=10^{-10}$ and $2.4\times10^{-7}$ at $10^{-13}$: a thousand times smaller tolerance, a thousand times smaller error (Stage-3 document §9.4).
4. **EXP-4: Adams against BDF, measured.** The program chooses its method at run time by a recorded test on two momentum nodes, comparing, over the window $1\le a\le2$ of the scale factor, with a reference run of the Adams method at $\mathrm{rtol}/10$ and $\mathrm{atol}/10$ (the `methodSelection` entry of `exp4/summary.json`):

| Node, momentum | Method | Steps | RHS evaluations | Jacobian RHS evaluations | Largest error |
| --- | --- | --- | --- | --- | --- |
| 2, $k=0.9525$ | Adams | 1007 | 1370 | 0 | $1.25\times10^{-12}$ |
| 2, $k=0.9525$ | BDF | 4573 | 4730 | 2464 | $2.27\times10^{-10}$ |
| 47, $k=119.93$ | Adams | 68001 | 88979 | 0 | $1.71\times10^{-9}$ |
| 47, $k=119.93$ | BDF | 308166 | 313247 | 164384 | $1.84\times10^{-8}$ |

On this oscillatory, non-stiff problem the Adams method is 11 to 180 times more accurate against that Adams reference, and it needs about 3.5 times fewer right-hand-side evaluations, or about 5.3 times fewer when the Jacobian evaluations of BDF are counted as well (ratios computed here from the table). Since the reference is itself an Adams run, a measure that needs no reference is a useful second opinion: the largest drift of the conserved $u^\dagger u$ (key `maxNormDrift` of the same entry) is $2.6\times10^{-12}$ for Adams against $4.5\times10^{-10}$ for BDF at node 2, and $9.9\times10^{-10}$ against $2.9\times10^{-8}$ at node 47, so it too is 29 to 173 times smaller for Adams (ratios computed here). This is what Sections 10.4 to 10.6 lead one to expect.

### 10.9 CVODE and the project's driver

**What CVODE is.** CVODE is the solver for initial-value problems of SUNDIALS, a suite of numerical software from Lawrence Livermore National Laboratory. It implements the variable-step, variable-order Adams–Moulton and BDF methods of Section 10.6, the two nonlinear iterations of Section 10.7 and the error test of Section 10.8. The project uses a pure-Rust translation of SUNDIALS 7.8.0 (`sundials_rs`) from the rustSolveIt repositories of the same author. The setup scripts `scripts/setup_solver.ps1` and `scripts/setup_solver.sh` clone it at a pinned commit into the folder `vendor/rustSolveIt`, which Git ignores; the engine is licensed BSD-3-Clause and is fetched at build time, not redistributed (Stage-3 document §5.1):

```
https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0
  a8fdff459adfe181573d7924b18bffbdf378fdb3
https://github.com/once-ere/rustSolveIt_macos-silicon_SUNDIALS_7_8_0
  5360157f4f6160978f66400566c31b2ae25dd44d
https://github.com/once-ere/rustSolveIt_linux_SUNDIALS_7_8_0
  6f58e02e53717a51375bd4bc5918edc57088d922
```

**The driver.** All five experiments call one function of `studies/dirac16complex_cosmology/src/driver.rs`, `integrate(y0, t0, targets, rhs, cfg)`. It integrates $Y'=f(t,Y)$ from $t_0$ through a list of output times and returns the state at $t_0$ and at every output time. In outline (the real code checks every return flag of SUNDIALS and frees every object in the order the C library requires):

```
integrate(y0, t0, targets, rhs, cfg):
    check: y0 finite, targets strictly monotone, rtol > 0, atol > 0, max_step >= 0
    create CVODE with lmm = BDF or ADAMS
    CVodeInit(rhs, t0, y0);  CVodeSStolerances(rtol, atol)
    if BDF:   dense matrix + dense linear solver (Newton, difference-quotient Jacobian)
    if Adams: fixed-point nonlinear solver, no linear solver
    CVodeSetMaxNumSteps(1000000, or 50000000 in EXP-4)
    if max_step > 0: CVodeSetMaxStep(max_step)
    if a stop time is given: CVodeSetStopTime(stop time)
    for each target: CVode(target, CV_NORMAL) -> state at target; stop on a negative flag
    record steps, rhs evaluations, Jacobian rhs evaluations, error-test failures
```

The maximum number of steps applies to each output interval; EXP-4 raises it to 50000000 for all its integrations (`MAX_NUM_STEPS` in `src/exp4.rs`; `print-config` shows it). Three details matter for correctness. In the mode `CV_NORMAL` CVODE may step beyond an intermediate output time and return the state there by **interpolation** with its own polynomial, so the output grid does not force small steps. Every integration of the project also sets a **stop time** equal to its last output time (EXP-2 and EXP-3 separately for their forward and backward runs, EXP-4 also at the junction $t=0$ of its sudden-transition pair modes, where the background changes its law and the integration is restarted), which keeps CVODE from stepping past the end. And the right-hand side is an ordinary Rust function; if it returns a non-finite number, CVODE is told that the failure is recoverable and retries with a smaller step, while an explicit error aborts the run with a named message.

**The program.** The Rust crate `studies/dirac16complex_cosmology` has the subcommands `print-config`, `exp1` to `exp5` and `all`, and the options `--output DIR`, `--rtol X`, `--atol X` and `--refined`; the last divides rtol and atol by 10 and max_step by 2 (Stage-3 document §5.2). Following the convention of the rustSolveIt examples, every self-check prints a line `PASS - name: detail` or `FAIL - name: detail`, and the last line of the output is `SUCCESS` (exit code 0) or `FAILURE` (exit code 1). The five experiments run 69 self-checks, all passing. How to build and run it on Windows, macOS and Linux is Chapter 19 and the student guide.

### 10.10 Numbers in a computer: rounding and reproducibility

**Floating-point numbers.** A computer stores a real number as a **double**: a sign, 53 binary digits and an exponent (the IEEE 754 standard). Only finitely many numbers can be stored, so most results are rounded to the nearest double. The relative spacing of doubles is $2^{-52}\approx2.2\times10^{-16}$ (the **machine epsilon**), and the gap between a double $x$ and the next one is called $\mathrm{ulp}(x)$, the unit in the last place: $\mathrm{ulp}(1)=2.2\times10^{-16}$ and $\mathrm{ulp}(10^4)=2^{-39}\approx1.8\times10^{-12}$. The decimal number $10^{-10}$ has no exact double; the nearest one, written with 18 significant digits, is $1.00000000000000004\times10^{-10}$, which is why the program's `print-config` shows the default tolerance of EXP-5 as `1.00000000000000004e-10` (student guide §7.1).

**How the files are written.** Every floating-point number in every output file is written by the C format `%.17e`, one digit before the decimal point and 17 after it: 18 significant digits (`studies/dirac16complex_cosmology/src/output.rs`). Integers such as step counts are written as plain integers (for example `"steps": 769` in `exp1/summary.json`), and a JSON entry without a finite value is written as `null`. The Stage-3 document says "17 significant digits"; the format has 17 digits after the point and hence 18 significant digits, as the student guide §8.1 states. Seventeen significant digits already identify every double uniquely, so no information is lost and two files can be compared byte by byte. The files use line feeds only and contain no dates, timings or folder names.

**Rounding can set a floor that no tolerance removes.** In EXP-2 the runs last until $t\approx10^4$; the three runs together take 1779784 steps, several hundred thousand each. CVODE advances its internal time by $t_{n+1}=t_n+h_n$, and near $t=10^4$ each addition is rounded to a multiple of about $1.8\times10^{-12}$. The spinor's phase rotates at the rate $M_{\mathrm{eff}}$, so the phase error can accumulate up to about $\max\lvert M_{\mathrm{eff}}\rvert\cdot N_{\mathrm{steps}}\cdot\mathrm{ulp}(t_{\mathrm{end}})/2$, recorded as `maxSpinorPhaseRoundingBound` $=1.32\times10^{-6}$ in `exp2/summary.json`. The measured phase error is $2.24\times10^{-7}$ (`maxSpinorPhaseError`), below the bound. The decisive test: in the refined run the phase error does **not** shrink ($2.71\times10^{-7}$), whereas the phase-invariant shape error of the spinor shrinks from $2.0\times10^{-10}$ to $5.2\times10^{-11}$ (Stage-3 document §7.6). A truncation error would have shrunk; a rounding floor does not. Only phase-invariant quantities enter the physical results.

**Determinism and byte identity.** Run twice with the same inputs, the program must write byte-identical files. That requires more than correct mathematics:

- a deterministic mathematical library: the engine brings its own implementation of the elementary functions (`sundials_libm`) instead of using the operating system's;
- the same machine instructions: the file `.cargo/config.toml` compiles with the processor feature FMA (fused multiply-add, $a\cdot b+c$ with a single rounding), which the engine's library and the pinned results assume (student guide §5.2);
- a fixed order of operations: EXP-4 distributes its modes over up to 8 threads, but every mode is integrated independently and the results are collected in a fixed order, so the outcome does not depend on the number of threads (header of `parallel_map` in `src/exp4.rs`);
- output without timings, dates or absolute paths.

Each independent checker reruns the program into a fresh folder and requires every output file to be byte-identical to the committed one (check `repeatByteIdentity` in every `python-check-report.json`; all five are true).

**Byte identity depends on the engine.** The three rustSolveIt engines are not identical: the Windows 11 engine's mathematical library differs from the one of the macOS and Linux engines, and some functions (the logarithm for some arguments) differ in the last bit. With the Windows 11 engine every committed file is reproduced byte for byte, on Windows 11 and on Ubuntu 24.04. With the Linux engine all 69 self-checks and all 167 checker checks still pass, but 14 committed files differ in their last digits (student guide §4.5; erratum in `handoff/specs/NUMERICS_CONTRACT.md`). Byte identity is a test of reproducibility with a fixed engine; agreement to the tolerance is the test of correctness.

### 10.11 Independent checkers: how to trust a numerical result

A number printed by a program is not yet a result. Stage 3 accepts a numerical result only after an **independent** program has confirmed it, and the checkers follow four rules (Stage-3 document §5.3): they are separate code, in Python with numpy and the standard library only; they rebuild the gamma matrices from the exact algebra fixture `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` instead of trusting the program's copy; they recompute every physical quantity from the raw state columns of the output files, never from the program's derived columns; and they test the program against mathematics that does not involve the program. Six kinds of test are used.

**1. Exact solutions.** Where an exact solution exists it is computed independently. For EXP-1 the checker computes $u(t)=e^{-iht}u_0$ from the eigenvalues and eigenvectors of $h$ (numpy's `eigh`) and finds the largest distance $6.25\times10^{-9}$ from the CVODE solution over all 26 runs, against the limit $10^{-7}$ (`exactMaxError` in `exp1/python-check-report.json`).

**2. Conservation laws.** In the good sector the Hilbert norm $u^\dagger u$ is conserved (Section 10.2), and in every sector the Krein norm $u^\dagger Bu$ is conserved, because the mode Hamiltonian satisfies $h^\dagger B=Bh$ (Chapter 8) and therefore $\tfrac{d}{dt}(u^\dagger Bu)=(iu^\dagger h^\dagger)Bu+u^\dagger B(-ihu)=iu^\dagger(h^\dagger B-Bh)u=0$. In EXP-1 both drift by at most $2.70\times10^{-9}$ (`normMaxDrift`). EXP-5 is the hard case: there $h$ is not Hermitian, $u^\dagger u$ grows to about $10^{16}$, and the Krein norm must nevertheless stay constant; its drift, divided by $\max(u^\dagger u,1)$, stays below $1.08\times10^{-9}$ (`kreinMaxNormalizedDrift` in `exp5/python-check-report.json`).

![EXP-5 of Stage 3: (a) the drift of the Krein norm, divided by $\max(u^\dagger u,1)$, for the four runs, below the limit $10^{-8}$ (dashed) throughout; (b) the Krein norm itself, drawn while $u^\dagger u<10^8$, stays at its initial value $\pm E_0/m$. Later, when $u^\dagger u$ approaches $10^{16}$, the computed $u^\dagger Bu$ is a difference of numbers of that size and loses its digits to rounding (absolute drift up to 1.005, `kreinDrift.maxAbs` in `exp5/summary.json`), which is why panel (a) divides the drift by $\max(u^\dagger u,1)$.](artifacts/dirac16complex/numerics/figures/exp5_krein.png)

**3. Finite-difference residuals.** The checker inserts the stored solution back into the equation. The derivative is estimated from five neighbouring samples with spacing $\Delta$:

$$
u'(t)\approx\frac{u(t-2\Delta)-8u(t-\Delta)+8u(t+\Delta)-u(t+2\Delta)}{12\Delta}.
$$

*Derivation.* By Taylor's theorem $u(t\pm\Delta)=u\pm\Delta u'+\tfrac{\Delta^2}{2}u''\pm\tfrac{\Delta^3}{6}u'''+\tfrac{\Delta^4}{24}u''''\pm\tfrac{\Delta^5}{120}u^{(5)}+\dots$, so $u(t+\Delta)-u(t-\Delta)=2\Delta u'+\tfrac{\Delta^3}{3}u'''+\tfrac{\Delta^5}{60}u^{(5)}+\dots$ and, with $2\Delta$ in place of $\Delta$, $u(t+2\Delta)-u(t-2\Delta)=4\Delta u'+\tfrac{8\Delta^3}{3}u'''+\tfrac{32\Delta^5}{60}u^{(5)}+\dots$. Eight times the first minus the second removes the $u'''$ terms:

$$
8\bigl[u(t+\Delta)-u(t-\Delta)\bigr]-\bigl[u(t+2\Delta)-u(t-2\Delta)\bigr]=12\Delta\,u'-\tfrac{24}{60}\Delta^5u^{(5)}+\dots,
$$

and dividing by $12\Delta$ gives $u'-\tfrac{\Delta^4}{30}u^{(5)}$. The formula is exact up to $\tfrac{\Delta^4}{30}u^{(5)}$. For an oscillation with frequency at most $E$, $\lvert u^{(5)}\rvert\le E^5\lvert u\rvert$. *Derivation.* For a constant $h$ each derivative of a solution multiplies it by $-ih$ ($\dot u=-ihu$, $\ddot u=-ih\dot u=(-ih)^2u$, and so on), so $u^{(5)}=(-ih)^5u=-i\,h^5u$. In EXP-1, $h^2=E^2\cdot1$ gives $h^5=E^4h$, and for the Hermitian $h$ we have $\lvert hu\rvert^2=u^\dagger h^\dagger hu=u^\dagger h^2u=E^2\lvert u\rvert^2$; hence $\lvert u^{(5)}\rvert=E^4\lvert hu\rvert=E^5\lvert u\rvert$ exactly. For a general constant Hermitian $h$ whose eigenvalues $\lambda_j$ all have modulus at most $E$, expand $u=\sum_jc_jv_j$ in orthonormal eigenvectors $v_j$ (the spectral theorem of Section 1.6); then $h^5u=\sum_jc_j\lambda_j^5v_j$ and $\lvert h^5u\rvert^2=\sum_j\lvert c_j\rvert^2\lambda_j^{10}\le E^{10}\sum_j\lvert c_j\rvert^2=E^{10}\lvert u\rvert^2$. So the residual $\lVert\text{formula}-(-ihu)\rVert$ must stay below about $\tfrac{\Delta^4}{30}E^5$ for a spinor with $\lvert u\rvert=1$, as in EXP-1. The EXP-1 checker allows $1.5\,\tfrac{\Delta^4}{30}E^5+10^{-6}$ and finds at most 0.63 of it (`fdResidualWorstRatioToBound`); EXP-5 finds at most 0.71.

**4. Refined-tolerance convergence.** The checker reruns the program with `--refined` (rtol and atol divided by 10, max_step by 2) and requires the errors to shrink. In EXP-5 the relative error against an independent reference falls from $3.34\times10^{-8}$ to $2.28\times10^{-9}$ (`canonicalMaxRelativeError` and `refinedMaxRelativeError` in `exp5/python-check-report.json`). In EXP-1 every run's distance from the exact solution strictly decreases. Where a floor was identified instead, such as the rounding floor of Section 10.10, the check requires the error to stay within that floor rather than to shrink (Stage-3 document §5.3).

**5. Independent integrators.** Where no exact solution exists, the checkers integrate selected modes again with methods that share no code with CVODE. The classical **fourth-order Runge–Kutta method** (RK4) makes a step with four evaluations of $f$,

$$
k_1=f(t_n,Y_n),\quad k_2=f\bigl(t_n+\tfrac h2,Y_n+\tfrac h2k_1\bigr),\quad k_3=f\bigl(t_n+\tfrac h2,Y_n+\tfrac h2k_2\bigr),\quad k_4=f(t_n+h,Y_n+hk_3),
$$

$$
Y_{n+1}=Y_n+\tfrac h6\bigl(k_1+2k_2+2k_3+k_4\bigr).
$$

For $y'=-y$ one RK4 step multiplies by $1-h+\tfrac{h^2}{2}-\tfrac{h^3}{6}+\tfrac{h^4}{24}$, which is $0.606771$ for $h=0.5$; two steps give $y(1)\approx0.368171$, an error of only $2.9\times10^{-4}$, against $0.118$ for Euler with the same step (Section 10.3). The error of such a reference is itself estimated by **Richardson's rule**: for a method of order $p$, halving the step reduces the error by about $2^p$, so the difference $Y_{h/2}-Y_h$ is about $(2^p-1)$ times the error of $Y_{h/2}$. The EXP-4 and EXP-5 checkers use RK4 with a Richardson estimate, and the EXP-4 checker also uses a fourth-order **Magnus method**, which advances $i\dot u=h(t)u$ by the exponential of $-i$ times a Hermitian matrix, a unitary matrix, and therefore keeps $u^\dagger u$ exactly (Stage-3 document §9.6 and §10.6). A Mathematica notebook re-integrates runs of all five experiments with Mathematica's NDSolve (for EXP-4 only a subset: four of its 48 thermal modes, two of them only up to the scale factor $a=10$ instead of 100, and ten pair-creation modes; Stage-3 document §9.6), including an order-8 Runge–Kutta method and a 32-digit arithmetic run (Stage-3 document §11.2); the figure shows its agreement with CVODE.

![Agreement of Mathematica's NDSolve with the Rust CVODE solutions, as digits of agreement ($-\log_{10}$ of the largest deviation) for each experiment; "aligned" means that a constant phase was removed first. From the Stage-3 Mathematica notebook.](artifacts/dirac16complex/numerics/figures/mathematica/cross_check_deviations.png)

**6. Negative controls.** A test that cannot fail proves nothing. The checks are therefore also run with deliberately wrong physics and must fail. The Mathematica notebook has its own finite-difference test, built like test 3 but with nine-point (eighth-order) derivatives: row by row (one row per output time, leaving out the rows that the output grid samples too coarsely) it compares the derivative of the stored solution with the right-hand side $f$, divides the largest difference of a component by the largest size of a component of $f$ in that row (the **relative residual**), and uses the difference between the eighth-order and a sixth-order derivative as the row's **truncation estimate**. A row passes only if its residual is at most twice its truncation estimate plus an allowance, proportional to the Rust tolerance, for the noise of the stored samples (function `fdCheck` of `scripts/build_dirac16complex_mathematica_notebook.wls`). With the correct sign of the mass the residual is at most $1.0\times10^{-10}$ for EXP-1 and $7.1\times10^{-5}$ for EXP-3, against truncation estimates of at most $1.4\times10^{-8}$ and $5.4\times10^{-4}$, and every row passes. With the sign of the mass flipped (in one run of each experiment) the largest residual becomes 1.19 times the size of the right-hand side for EXP-1 and 2.0 times for EXP-3. For EXP-3 the value 2 is no accident: there the right-hand side of the spinor equation is proportional to the mass, so flipping its sign turns $f$ into $-f$, and the finite-difference derivative of the stored solution, which is close to $f$, differs from $-f$ by about $2f$. Both controls therefore miss their pass bound by orders of magnitude, as they must (keys `maxRelativeResidual`, `maxRelativeTruncationEstimate` and `negativeControlFlippedMassMaxRelativeResidual` of `exp1.finiteDifference` and `exp3.finiteDifference` in `artifacts/dirac16complex/numerics/mathematica-report.json`; Stage-3 document §6.6 and §8.6). The exact Stage-2 verifier contains controls of the same kind: the conservation law $\nabla_\mu T^\mu{}_\nu=0$ must fail off shell, and the exact source of Chapter 9 must fail for a wrong slope of $a_4$ (Stage-2 document §13.5 and §15.5).

**The count.** Over the five experiments: 69 of 69 self-checks of the Rust program, 167 of 167 checks of the five independent checkers, 10 of 10 checks of the EXP-3 analysis, all 49 checks of the Mathematica notebook and all 71 assertions of the Jupyter notebook are true (Stage-3 document §13). Chapter 11 describes what these experiments show.

### 10.12 Boundary-value problems and shooting

**Two-point problems.** Some problems do not give all conditions at one end. A Kohn–Sham orbital of Chapter 13 must satisfy one condition at the tip cutoff $y=-L$ and one at the brane $y=0$, and it exists only for special values of its energy $\varepsilon$: an **eigenvalue problem** for an ODE. The **shooting method** turns it into initial-value problems: guess $\varepsilon$, integrate from one end with the condition there, measure how badly the condition at the other end fails (the **mismatch**), and adjust $\varepsilon$ until the mismatch is zero. The Stage-4 Rust solver `studies/dirac16complex_kohn_sham` shoots with CVODE from $-L$ to 0. Instead of the raw mismatch it uses the **Prüfer angle**: it writes the two real components $a$ and $b$ of the orbital as $a=r\cos\theta$ and $b=-r\sin\theta$, integrates the equation for the angle $\theta(y)$ from $\theta(-L)=0$, and takes the end value $\Theta(\varepsilon)=\theta(0;\varepsilon)$, which increases with $\varepsilon$. Each level is the solution of $\Theta(\varepsilon)=n\pi$ (or $\tfrac\pi2+n\pi$, depending on the parity of the orbital) for an integer $n$ (Section 13.10). The solver first **brackets** each target by doubling the step in $\varepsilon$ until $\Theta(\varepsilon)$ minus the target changes sign. It then refines it by the **regula falsi**: the secant rule applied to the two ends of the bracket, keeping, as bisection does, the part in which the sign changes, so that the root always stays bracketed. In the plain regula falsi one end can stay fixed for many steps, and the bracket then shrinks only slowly from the other side. The solver therefore uses the **Illinois** variant: when the same end is replaced twice in a row, the function value kept at the other end is halved, which pulls the next point towards the end that has stayed fixed, so that this end is soon replaced as well (header and `find_level` of `src/shooting.rs`; the plan `handoff/specs/STAGE4_SPEC.md` §5 had named bisection and the secant rule, the two ingredients shown in the worked example below; Exercise 10.13 compares the two versions of the regula falsi). The solver's results, and the status of its independent cross-check, are the subject of Chapter 13.

**Worked example.** Find the values $E$ for which $u''=-Eu$ has a solution with $u(0)=0$ and $u(1)=0$. As a first-order system, $u'=v$ and $v'=-Eu$; start with $u(0)=0$, $v(0)=1$. For $E>0$ the solution is $u(x)=\sin(\sqrt Ex)/\sqrt E$, so the mismatch is $F(E)=u(1)=\sin\sqrt E/\sqrt E$ (a computer would get it from CVODE; here we know it exactly). Since $F(5)=0.3518>0$ and $F(15)=-0.1725<0$, a zero lies between. **Bisection** halves the bracket and keeps the half on which $F$ changes sign:

| Step | Midpoint $E$ | $F(E)$ | New bracket |
| --- | --- | --- | --- |
| 1 | 10 | $-0.00654$ | [5, 10] |
| 2 | 7.5 | $+0.14320$ | [7.5, 10] |
| 3 | 8.75 | $+0.06170$ | [8.75, 10] |
| 4 | 9.375 | $+0.02601$ | [9.375, 10] |
| 5 | 9.6875 | $+0.00935$ | [9.6875, 10] |
| 6 | 9.84375 | $+0.00131$ | [9.84375, 10] |

Each step gains one binary digit. The **secant rule** instead draws the straight line through the last two points and takes its zero, $E_{\mathrm{new}}=E_1-F(E_1)\,(E_1-E_0)/(F(E_1)-F(E_0))$. From $E_0=5$ and $E_1=15$ it gives 11.7108, 8.8043, 10.0237, 9.88156, 9.869463 and 9.8696045: after six steps seven correct digits of the exact answer $\pi^2=9.8696044$, because $u(x)=\sin(\pi x)/\pi$ vanishes at $x=1$.

### 10.13 What we proved and what we assumed

**Derived in this chapter:** how a complex 16-component mode equation becomes 32 real first-order equations; the exact solution $u(t)=\bigl(\cos Et-i\sin Et\,h/E\bigr)u_0$ when $h^2=E^2\cdot1$, and the conservation of $u^\dagger u$ for Hermitian $h$ (and of $u^\dagger Bu$ when $h^\dagger B=Bh$); the order of Euler's method; the amplification factors of explicit Euler, backward Euler and the trapezoidal rule and what they do to decaying and oscillating solutions; why stiffness forces implicit methods, and that the eigenvalues of $-ih$ are $\mp iE$ or $\pm\varkappa$ when $h^2=E^2\cdot1$ with $E^2$ positive or negative; the Adams–Bashforth, trapezoidal and BDF2 formulas and the implicit equation of each step; the convergence factor $\gamma J$ of fixed-point iteration; Newton's method from the linear approximation, its exactness for linear problems and the exactness of the difference-quotient Jacobian for a linear right-hand side; the weighted error norm; the five-point derivative formula with its error $\tfrac{\Delta^4}{30}u^{(5)}$ and the bound $\lvert u^{(5)}\rvert\le E^5\lvert u\rvert$ for a constant Hermitian $h$ whose eigenvalues have modulus at most $E$ (with equality when $h^2=E^2\cdot1$); the RK4 step and Richardson's rule; bisection, the secant rule and the regula falsi with its Illinois variant for shooting. **Computed by the project and copied from its committed reports:** the methods, tolerances and step counts of the five Stage-3 experiments; the drifts, exact-solution errors, finite-difference ratios and refined-run errors quoted above; the failing checks of EXP-1 at $\mathrm{rtol}=10^{-10}$ (student guide Exercise 13.1); the recorded Adams-against-BDF test, with its errors against an Adams reference and its norm drifts; the residuals, truncation estimates and flipped-mass negative controls of the Mathematica finite-difference test; the byte identity of repeat runs; and the totals of 69 self-checks, 167 checker checks, 49 Mathematica checks and 71 notebook assertions, all true.

**Assumed or quoted, not proved here:** the existence and uniqueness theorem of Picard and Lindelöf; Taylor's theorem and the spectral theorem of Chapter 1; how fast Newton's method and the Illinois regula falsi converge in general, which the worked examples and Exercise 10.13 only illustrate; the internal design of CVODE (its error estimate and its choice of step and order), which we describe but do not derive, and the correctness of its Rust translation, which is tested only through the checks of Section 10.11; the fact that 17 significant digits identify a double uniquely; the independence of the EXP-4 results from the number of threads, which rests on the code's design and on the repeat-run check; and the engine differences of Section 10.10, which were measured and recorded in the student guide. The Stage-4 shooting solver is only introduced here: the Prüfer angle, its increase with $\varepsilon$ and the level condition $\Theta(\varepsilon)=n\pi$ or $\tfrac\pi2+n\pi$ are derived in Section 13.10, and its accuracy and cross-check status belong to Chapter 13.

### 10.14 Exercises

**Exercise 10.1.** Write the damped oscillator $x''+2x'+5x=0$ as a first-order system $Y'=f(t,Y)$, and check that $x=e^{-t}\cos2t$ solves it.

**Exercise 10.2.** Apply Euler's method to $y'=-2y$, $y(0)=1$, up to $t=1$ with $h=0.25$ and with $h=0.125$. Compare with $e^{-2}$ and determine the order from the two errors.

**Exercise 10.3.** Show that the trapezoidal rule applied to $y'=i\omega y$ keeps $\lvert y\rvert$ exactly constant, for every real $\omega$ and every step $h$.

**Exercise 10.4.** For $y'=-50y$, find the largest step for which explicit Euler is stable, and the factor by which backward Euler multiplies $y$ per step when $h=0.1$.

**Exercise 10.5.** Derive the BDF2 formula a second way: find numbers $a,b,c$ such that $(a\,y_{n+1}+b\,y_n+c\,y_{n-1})/h$ equals $y'(t_{n+1})$ exactly for $y=1$, $y=t$ and $y=t^2$. (Put $t_{n+1}=0$, $t_n=-h$, $t_{n-1}=-2h$.)

**Exercise 10.6.** With $\mathrm{rtol}=10^{-6}$ and $\mathrm{atol}=10^{-9}$, a step has the state $Y=(1,\,10^{-3},\,0)$ and the error estimate $e=(5\times10^{-7},\,2\times10^{-9},\,10^{-9})$. Is the step accepted?

**Exercise 10.7.** Apply the five-point derivative formula of Section 10.11 to $u(t)=t^5$ at $t=0$ with $\Delta=0.1$, and compare the result with the predicted error $-\tfrac{\Delta^4}{30}u^{(5)}$.

**Exercise 10.8.** For $h=\begin{pmatrix}3&4\\4&-3\end{pmatrix}$ and $u_0=(1,0)^T$, evaluate the exact solution of $i\dot u=hu$ at $t=\pi/10$ and check its norm. Then make one explicit Euler step of size $0.01$ from $u_0$ and compute the new $u^\dagger u$.

**Exercise 10.9.** Carry out the first secant step of Section 10.12 from $E_0=5$ and $E_1=15$ with the values $F(5)=0.35184$ and $F(15)=-0.17245$.

**Exercise 10.10.** Euler's method for $y'=-y$ gave $0.316406$ with $h=0.25$ and $0.343609$ with $h=0.125$ (Section 10.3). Use Richardson's rule with $p=1$ to estimate the error of the second value and to improve it. Compare with $e^{-1}=0.367879$.

**Exercise 10.11.** Near $t=10^4$ the spacing of doubles is $2^{-39}$. Estimate how large the rounding error of CVODE's internal time can become after $6\times10^5$ additions $t_{n+1}=t_n+h_n$, and the resulting phase error of a spinor that rotates at the rate $M_{\mathrm{eff}}=2$.

**Exercise 10.12.** In EXP-5 the refined run (rtol and atol divided by 10, max_step by 2) reduced the relative error from $3.34\times10^{-8}$ to $2.28\times10^{-9}$. What does the ratio suggest, and what ratio would a rounding floor give?

**Exercise 10.13.** Apply the regula falsi of Section 10.12 to the shooting example $F(E)=\sin\sqrt E/\sqrt E$ with the starting bracket $[5,15]$ and the values $F(5)=0.35184$, $F(15)=-0.17245$. (a) Compute the first two points with the plain regula falsi, using $F(11.7108)=-0.08090$, and say which end of the bracket is replaced each time. (b) In the Illinois variant the second step replaces the same end as the first. Halve the value kept at the other end and compute the third point, using $F(10.4562)=-0.02842$. Which end does it replace?

### 10.15 Answers to the exercises

**Answer 10.1.** With $v=x'$: $x'=v$ and $v'=x''=-5x-2v$, so $Y=(x,v)^T$ and $f(t,Y)=(v,\,-5x-2v)^T$. For $x=e^{-t}\cos2t$: $x'=-e^{-t}\cos2t-2e^{-t}\sin2t$ and $x''=e^{-t}\cos2t+2e^{-t}\sin2t+2e^{-t}\sin2t-4e^{-t}\cos2t=-3e^{-t}\cos2t+4e^{-t}\sin2t$. Then $x''+2x'+5x=e^{-t}\bigl[(-3-2+5)\cos2t+(4-4)\sin2t\bigr]=0$.

**Answer 10.2.** Each step multiplies by $1-2h$. With $h=0.25$: $(0.5)^4=0.0625$; with $h=0.125$: $(0.75)^8=0.100113$. The exact value is $e^{-2}=0.135335$, so the errors are $0.072835$ and $0.035222$. Their ratio is 2.07, close to $2^1$: order 1.

**Answer 10.3.** The factor is $R=(1+i\omega h/2)/(1-i\omega h/2)$. Numerator and denominator are complex conjugates of each other, so they have the same modulus $\sqrt{1+\omega^2h^2/4}$, and $\lvert R\rvert=1$. Hence $\lvert y_{n+1}\rvert=\lvert y_n\rvert$ at every step.

**Answer 10.4.** Explicit Euler multiplies by $1-50h$; stability needs $\lvert1-50h\rvert\le1$, that is $0\le h\le0.04$. Backward Euler multiplies by $1/(1+50h)=1/(1+5)=1/6$ at $h=0.1$, stable and decaying.

**Answer 10.5.** For $y=1$ the derivative is 0: $a+b+c=0$. For $y=t$ the derivative is 1, and the values are $0,-h,-2h$: $(0\cdot a-hb-2hc)/h=1$, that is $-b-2c=1$. For $y=t^2$ the derivative at $t=0$ is 0, and the values are $0,h^2,4h^2$: $(h^2b+4h^2c)/h=0$, that is $b=-4c$. Then $4c-2c=1$ gives $c=\tfrac12$, $b=-2$ and $a=\tfrac32$: the formula $(\tfrac32y_{n+1}-2y_n+\tfrac12y_{n-1})/h$ of Section 10.6.

**Answer 10.6.** The weights are $10^{-6}\cdot1+10^{-9}=1.001\times10^{-6}$, $10^{-6}\cdot10^{-3}+10^{-9}=2\times10^{-9}$ and $0+10^{-9}=10^{-9}$. The ratios are $0.4995$, $1.0$ and $1.0$. The norm is $\sqrt{(0.2495+1+1)/3}=\sqrt{0.7498}=0.866\le1$: the step is accepted, although two components sit exactly at their limit.

**Answer 10.7.** $u(\pm0.1)=\pm10^{-5}$ and $u(\pm0.2)=\pm3.2\times10^{-4}$. The formula gives $\bigl[-3.2\times10^{-4}-8(-10^{-5})+8(10^{-5})-3.2\times10^{-4}\bigr]/1.2=-4.8\times10^{-4}/1.2=-4\times10^{-4}$, whereas $u'(0)=0$. The predicted error is $-\tfrac{(0.1)^4}{30}\cdot120=-4\times10^{-4}$: exact agreement, because $t^5$ has no derivatives beyond the fifth.

**Answer 10.8.** At $t=\pi/10$, $5t=\pi/2$, $\cos5t=0$ and $\sin5t=1$, so $u=(-\tfrac{3i}5,-\tfrac{4i}5)^T$ and $u^\dagger u=\tfrac9{25}+\tfrac{16}{25}=1$. One Euler step of $\dot u=-ihu$ gives $u_1=(1-0.01\,ih)u_0$, and $u_1^\dagger u_1=u_0^\dagger(1+0.01\,ih)(1-0.01\,ih)u_0=u_0^\dagger(1+10^{-4}h^2)u_0=1+10^{-4}\cdot25=1.0025$: the norm has grown by $(\Delta t)^2E^2$ in one step, the explicit-Euler growth of Section 10.4.

**Answer 10.9.** $E_2=15-(-0.17245)\cdot\dfrac{15-5}{-0.17245-0.35184}=15-\dfrac{1.7245}{0.52429}=15-3.2892=11.7108$, the first secant value quoted in Section 10.12.

**Answer 10.10.** The difference is $0.343609-0.316406=0.027203$. With $p=1$, $2^p-1=1$, so the estimated error of the second value is $0.0272$ (the true error is $0.0243$), and the improved value is $0.343609+0.027203=0.370812$, whose error $0.0029$ is about eight times smaller.

**Answer 10.11.** Each rounded addition is off by at most half the spacing, $2^{-40}\approx9.1\times10^{-13}$. After $6\times10^5$ additions the time can be off by up to about $5.5\times10^{-7}$ (if all roundings go the same way), and a phase that grows at the rate 2 can then be off by about $1.1\times10^{-6}$. This is the size of the bound $1.32\times10^{-6}$ recorded for EXP-2 (Section 10.10), which is computed with the exact step counts and masses of the runs; the measured phase error, $2.24\times10^{-7}$, is below it.

**Answer 10.12.** The ratio is $3.34\times10^{-8}/2.28\times10^{-9}=14.6$ for a tenfold smaller tolerance: the error decreases at least in proportion to the tolerance, as a truncation error should, so the canonical run's error is dominated by truncation. A rounding floor would give a ratio close to 1, as the EXP-2 phase error did ($2.24\times10^{-7}$ against $2.71\times10^{-7}$).

**Answer 10.13.** (a) The point between the ends $E_{\mathrm{lo}}$ and $E_{\mathrm{hi}}$ of a bracket is the zero of the straight line through the two ends, $E=\bigl(E_{\mathrm{lo}}F(E_{\mathrm{hi}})-E_{\mathrm{hi}}F(E_{\mathrm{lo}})\bigr)/\bigl(F(E_{\mathrm{hi}})-F(E_{\mathrm{lo}})\bigr)$, which is the secant formula of Section 10.12 written for the two ends. The first point is therefore the first secant value, $11.7108$ (Answer 10.9). Since $F(11.7108)=-0.08090$ has the sign of $F(15)$, the sign change lies in $[5,11.7108]$: the right end is replaced. The second point is $\bigl(5\cdot(-0.08090)-11.7108\cdot0.35184\bigr)/(-0.08090-0.35184)=(-0.40450-4.12033)/(-0.43274)=10.4562$. Again $F(10.4562)=-0.02842<0$, so the right end is replaced again and the left end $5$ stays. The plain regula falsi goes on in this way: carrying all digits, its next points are $10.0485$, $9.9234$, $9.8857$, $9.8744$ and $9.8710$, all to the right of the root and all with the left end $5$, so that after seven points the error is still $1.4\times10^{-3}$. (b) The second step replaced the right end for the second time in a row, so the value kept at the left end is halved, $0.35184/2=0.17592$. The third point is $\bigl(5\cdot(-0.02842)-10.4562\cdot0.17592\bigr)/(-0.02842-0.17592)=(-0.14210-1.83945)/(-0.20434)=9.697$ ($9.69746$ with all digits). There $F$ is about $+0.009>0$, the sign of $F$ at the left end, so this time the **left** end is replaced and the bracket becomes $[9.697,10.4562]$. Carrying all digits, the next points are $9.87743$, $9.86971$, $9.86951$ and $9.8696044$: after seven points the value agrees with $\pi^2=9.8696044$ in all the digits shown, like the secant rule of Section 10.12, but with the root kept inside a bracket at every step.
