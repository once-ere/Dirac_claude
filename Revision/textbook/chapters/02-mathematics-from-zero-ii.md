## 2. Mathematics from zero II: several variables, ODEs, Euler and RK4, convergence, the shooting method

This chapter teaches the second half of the mathematics that the book needs: differential equations and how a computer solves them, how to tell how accurate a computed answer is, how to find the special energies of an equation with conditions at both ends of an interval (the shooting method), and how to differentiate a function of several variables. Every idea is built from school algebra and one-variable calculus, and every idea is tried out at once in a notebook. The chapter has four worked examples, Notebooks 02a, 02b, 02c and 02d; the last one rewrites, line by line in Python, the method with which the Rust program of the Revision record solves the Kohn-Sham equations of this book, and reproduces that program's published numbers.

### 2.1 What this chapter is for

The book's physics lives in equations that say how quantities change. Two places in the book need the tools of this chapter.

First, the author's metric. The metric (introduced from zero in Chapter 3; here we only need its formulas) is a list of eight numbers $g_{11}, \dots, g_{88}$ that turn small coordinate steps along the eight directions $x_1, \dots, x_8$ into true lengths. Its entries depend on TWO variables: the time $x_4$ and the hidden coordinate $x_8$. Lengths along the three directions of ordinary space, $x_1, x_2, x_3$, carry the **scale factor** $e^{a_4}\sin^{1/6} z$, and lengths along the three **extra times** $x_5, x_6, x_7$ carry the scale factor $e^{-a_4}\sin^{1/6} z$, where $a_4(x_4)$ is a function of the time and $z = 6 H x_8$ (with the author's positive constant $H$) is the author's variable for the hidden direction. When $a_4$ grows, ordinary space inflates and the three extra times **deflate exponentially**. To say how fast each length changes with $x_4$ or with $x_8$ we need **partial derivatives**, the derivatives of a function of several variables (Sections 2.18 and 2.19).

Second, the Kohn-Sham equations of the book (Chapters 14 and 15). They are two coupled first-order differential equations for the two components of an **orbital** (the wave function of one particle of the model) along the hidden coordinate, with one condition at each end of an interval, and they have solutions only for special energies, the **energy levels**. The Rust program of the Revision record solves them by the **shooting method**: it guesses an energy, integrates the equations from one end to the other with the **classical fourth-order Runge-Kutta method (RK4)** in 900 steps, measures by how much the condition at the far end fails, and corrects the energy with Newton's method. Sections 2.2 to 2.7 teach RK4 and the measurement of its accuracy, Sections 2.12 and 2.13 the shooting method, and Section 2.24 the special form of shooting (with the **Prüfer angle**) that the program uses.

The four notebooks of the chapter are:

| notebook | what it computes | Revision record it reproduces |
| --- | --- | --- |
| 02a | Euler, midpoint and RK4 on the deflating extra-time scale factor and on an oscillator; orders 1, 2, 4 on log-log plots; the rounding floor; the predicted error at the step of the Revision solver; Richardson's rule | `Revision/kohn_sham/results/parameters.json` (900 RK4 steps on an interval of length 3; the history constants $A = H = 1$) |
| 02b | the shooting method for a vibrating string and for a quantum well; bisection against the secant rule; exact levels with 30 digits | none (exact formulas only) |
| 02c | partial derivatives, finite differences, the chain rule for $z = 6 H x_8$, the growth and deflation rates of the author's metric, the volume factor, all 25 nonzero Christoffel entries | `Revision/gkd_lovelock/results/curvature.json` and `Revision/field_equations_a4/reports/wolfram-a4-report.json` |
| 02d | the Prüfer-angle shooting and the Newton root finder of the Revision Kohn-Sham solver, rewritten line by line; all 54 levels of its free spectrum | `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv` and two checks of `Revision/kohn_sham/reports/ks-rust-solver.json` |

Every statement of the chapter carries one of the five labels of Chapter 0. Most are PROVED here by elementary algebra (and confirmed by a check of a notebook) or COMPUTED by a notebook (with the cell that computes the number and, where it reproduces a Revision record, the record file and its check). A few standard theorems of calculus are quoted without proof; we label them ASSUMED, as the book does for everything it does not derive. Two physical inputs are ASSUMED as well and are named where they enter: the linear history $a_4 = A H x_4$, which is a PRESCRIBED BACKGROUND, and the mirror (brane) conditions of the Kohn-Sham model. No HYPOTHESIS enters this chapter.

### 2.2 Differential equations

**The derivative.** For a function $y(t)$ of one variable the derivative is

$$
y'(t) = \frac{dy}{dt}(t) = \lim_{h \to 0} \frac{y(t + h) - y(t)}{h},
$$

the slope of the graph of $y$ at $t$, or the rate of change of $y$ per unit of $t$. We write $y''$ for the derivative of $y'$ (the second derivative), and $y^{(n)}$ for the $n$-th derivative.

**An ordinary differential equation** (ODE) is an equation of the form

$$
y'(t) = f(t, y(t))
$$

for an unknown function $y(t)$, where $f$ is a known rule that produces a number from $t$ and $y$, the **right-hand side**. It is "ordinary" because the unknown depends on one variable only. Together with a starting value $y(0) = y_0$ it is an **initial-value problem**. When $f$ is smooth (it has continuous derivatives), the initial-value problem has exactly one solution, at least for some time after the start: this is the theorem of Picard and Lindelöf, which we quote without proof (ASSUMED: a standard theorem of calculus). A computer tries to approximate that one solution.

**Systems.** Several unknown functions that change together, say a position $x(t)$ and a velocity $v(t)$, form a **system**. We collect them into one list $Y = (x, v)$, a **vector**, and write the system again as $Y' = f(t, Y)$, where now $f$ produces a list of the same length. An equation with a second derivative becomes a system of first-order equations by naming the first derivative: $x'' = -x$ becomes $x' = v$ and $v' = -x$, because $v' = (x')' = x'' = -x$.

**Problem A: the deflating extra time.** We now derive the first equation of Notebook 02a from the author's metric. The entry of the metric for the extra time $x_5$ is

$$
g_{55} = -e^{-2a_4}\sin^{1/3} z .
$$

(This is the author's metric entry, which Notebook 02c reads from the Revision record `Revision/gkd_lovelock/results/curvature.json`, key `metricDiagonal`; its minus sign marks a time-like direction.)

$$
s_5 = \sqrt{|g_{55}|} = \sqrt{e^{-2a_4}\sin^{1/3} z}
$$

(The scale factor of a direction is defined as the square root of the absolute value of its diagonal metric entry; the absolute value removes the minus sign.)

$$
s_5 = e^{-a_4}\sin^{1/6} z
$$

(The square root of a product is the product of the square roots; $\sqrt{e^{-2a_4}} = e^{-a_4}$ because $(e^{-a_4})^2 = e^{-2a_4}$, and $\sqrt{\sin^{1/3} z} = \sin^{1/6} z$ because $(\sin^{1/6} z)^2 = \sin^{2/6} z = \sin^{1/3} z$.)

$$
s_5(x_4) = e^{-A H x_4}\sin^{1/6} z
$$

(We insert the linear history $a_4 = A H x_4$; the number $A$ fixes how fast $a_4$ grows.)

$$
\frac{ds_5}{dx_4} = -A H\, e^{-A H x_4}\sin^{1/6} z
$$

(Chain rule: the derivative of $e^{c x_4}$ is $c\, e^{c x_4}$, here with $c = -AH$; at a fixed hidden position $\sin^{1/6} z$ does not depend on $x_4$ and stays a constant factor.)

$$
\frac{ds_5}{dx_4} = -A H\, s_5
$$

(The right side of the previous line is $-AH$ times $s_5$ itself.)

With $A = 1$ and $H = 1$, and after dividing by the constant $\sin^{1/6} z$, the function $b(x_4) = e^{-x_4}$ obeys

$$
\frac{db}{dx_4} = -b, \qquad b(0) = 1 .
$$

This is **Problem A** of Notebook 02a, written with $t = x_4$ and $y = b$: $y' = -y$, $y(0) = 1$, with the exact solution $y(t) = e^{-t}$ (its derivative is $-e^{-t}$ by the chain rule, and $e^{0} = 1$). The same steps with $g_{11} = e^{2a_4}\sin^{1/3} z$ give the 3-space factor $a(x_4) = e^{x_4}$ with $da/dx_4 = +a$: ordinary space inflates while the extra time deflates. Their product never changes:

$$
a\, b = e^{x_4} e^{-x_4} = e^{x_4 - x_4} = e^{0} = 1
$$

(the exponential turns sums into products, $e^{u} e^{v} = e^{u + v}$).

*Status.* The algebra above is PROVED. The history $a_4 = A H x_4$ with $A = 1$ is ASSUMED: it is a PRESCRIBED BACKGROUND along which the Revision record computes its Kohn-Sham states (record `Revision/kohn_sham/results/parameters.json`, keys `historyA` = 1 and `H` = 1, reproduced by Notebook 02a, In [11]); the Revision check `ks_history_is_a_prescribed_background` of `Revision/field_equations_a4/reports/ks-source-conditions.json` records that the Kohn-Sham states are not admissible sources of the metric along it, so the history is not derived from the field equations (the equations that determine $a_4$, Chapter 12): it is put in by hand. The deflation itself is not frozen or static anywhere in this book: $b$ shrinks exponentially as $x_4$ grows.

**Problem B: the oscillator.** $x'' = -x$ with $x(0) = 1$ and $x'(0) = 0$. As a system, $x' = v$ and $v' = -x$ with $x(0) = 1$, $v(0) = 0$. The exact solution is $x = \cos t$, $v = -\sin t$: indeed $x' = -\sin t = v$ and $v' = -\cos t = -x$. Its **energy** $E = (x^2 + v^2)/2$ does not change:

$$
\frac{dE}{dt} = x\, x' + v\, v'
$$

(the derivative of $x^2/2$ is $x x'$ by the chain rule, and likewise for $v^2/2$);

$$
\frac{dE}{dt} = x\, v + v\,(-x) = 0
$$

(we insert $x' = v$ and $v' = -x$). So $E = (1^2 + 0^2)/2 = 1/2$ at every time, and the point $(x, v)$ runs round the circle $x^2 + v^2 = 1$. A numerical method that does not keep $E$ fixed reveals its error at once; Notebook 02a uses this.

### 2.3 Taylor's theorem and the exponential series

**Taylor's theorem** (ASSUMED: a standard theorem of one-variable calculus, quoted without proof). If $y$ has $n + 1$ continuous derivatives, then for every step $h$

$$
y(t + h) = y(t) + h\, y'(t) + \frac{h^2}{2!}\, y''(t) + \dots + \frac{h^n}{n!}\, y^{(n)}(t) + \frac{h^{n+1}}{(n+1)!}\, y^{(n+1)}(s)
$$

for some number $s$ between $t$ and $t + h$. Here $n! = 1 \cdot 2 \cdot 3 \cdots n$ (with $0! = 1$) is the **factorial**. The last term is the **remainder**: it shows that the error of keeping only the terms up to $h^n$ is proportional to $h^{n+1}$ when $h$ is small.

**The exponential series.** Take $y(t) = e^{t}$ at $t = 0$ and the step $h = z$. Every derivative of $e^{t}$ is $e^{t}$ itself, so every derivative at $t = 0$ is $e^{0} = 1$; the term with $h^k$ is therefore $z^k/k!$, and

$$
e^{z} = 1 + z + \frac{z^2}{2} + \frac{z^3}{6} + \frac{z^4}{24} + \frac{z^5}{120} + \dots
$$

where the dots stand for the terms with higher powers of $z$ (the remainder goes to zero as more terms are kept, for every $z$). This series is the yardstick of Sections 2.5 and 2.6.

### 2.4 Three step rules: Euler, midpoint and RK4

A computer cannot follow a solution continuously. It chooses a **step size** $h$, the times $t_n = n h$, and computes numbers $y_n$ that approximate $y(t_n)$, one step after the other. $N$ steps of size $h = T/N$ reach the end time $T$. A **step rule** says how to compute $y_{n+1}$ from $y_n$.

**Euler's method.** Taylor's theorem with $n = 1$ says $y(t + h) = y(t) + h\, y'(t) + \frac{h^2}{2} y''(s)$. Dropping the last term and using $y' = f(t, y)$ gives

$$
y_{n+1} = y_n + h\, f(t_n, y_n) .
$$

It follows the slope at the start of the step for the whole step.

**The midpoint method.** It first uses the starting slope to estimate the value in the middle of the step, and then uses the slope there for the whole step:

$$
k_1 = f(t_n, y_n), \qquad k_2 = f(t_n + \tfrac{h}{2},\, y_n + \tfrac{h}{2} k_1), \qquad y_{n+1} = y_n + h\, k_2 .
$$

**The classical fourth-order Runge-Kutta method (RK4).** It computes four slopes and averages them with the weights $1 : 2 : 2 : 1$:

$$
k_1 = f(t_n, y_n), \quad k_2 = f(t_n + \tfrac{h}{2},\, y_n + \tfrac{h}{2} k_1), \quad k_3 = f(t_n + \tfrac{h}{2},\, y_n + \tfrac{h}{2} k_2), \quad k_4 = f(t_n + h,\, y_n + h\, k_3),
$$

$$
y_{n+1} = y_n + \frac{h}{6}\,(k_1 + 2 k_2 + 2 k_3 + k_4) .
$$

$k_1$ is the slope at the start, $k_2$ the slope at the midpoint reached with $k_1$, $k_3$ the slope at the midpoint reached with $k_2$, $k_4$ the slope at the end reached with $k_3$. RK4 is the method of the Rust program of the Revision record that solves the Kohn-Sham equations (file `Revision/kohn_sham/solver/src/shoot.rs`). For a system the same formulas hold with $y$, $f$ and the $k$'s read as vectors.

**One step by hand.** Take Problem A, $f(t, y) = -y$, from $y_0 = 1$ with the step $h = 1/2$. Euler:

$$
y_1 = 1 + \tfrac{1}{2} \cdot (-1) = \tfrac{1}{2}
$$

(Euler's rule with $f(0, 1) = -1$). The midpoint method:

$$
k_1 = f(0, 1) = -1
$$

(the slope at the start is $-y_0$);

$$
k_2 = f\big(\tfrac14,\, 1 + \tfrac14 \cdot (-1)\big) = -\big(1 - \tfrac14\big) = -\tfrac34
$$

(half a step is $h/2 = 1/4$; the slope at the estimated midpoint value $3/4$ is minus that value);

$$
y_1 = 1 + \tfrac12 \cdot \big(-\tfrac34\big) = 1 - \tfrac38 = \tfrac58
$$

(the midpoint rule $y_1 = y_0 + h k_2$). RK4:

$$
k_1 = -1, \qquad k_2 = -\big(1 + \tfrac14 \cdot (-1)\big) = -\tfrac34
$$

(the same two slopes as in the midpoint method);

$$
k_3 = -\big(1 + \tfrac14 \cdot \big(-\tfrac34\big)\big) = -\big(1 - \tfrac{3}{16}\big) = -\tfrac{13}{16}
$$

(the midpoint value is now reached with $k_2$);

$$
k_4 = -\big(1 + \tfrac12 \cdot \big(-\tfrac{13}{16}\big)\big) = -\big(1 - \tfrac{13}{32}\big) = -\tfrac{19}{32}
$$

(the end value is reached with the whole step $h = 1/2$ and the slope $k_3$);

$$
k_1 + 2k_2 + 2k_3 + k_4 = -\tfrac{32}{32} - \tfrac{48}{32} - \tfrac{52}{32} - \tfrac{19}{32} = -\tfrac{151}{32}
$$

(every term is written over the common denominator 32 and the numerators are added);

$$
y_1 = 1 + \tfrac{1/2}{6} \cdot \big(-\tfrac{151}{32}\big) = 1 - \tfrac{151}{384} = \tfrac{233}{384}
$$

(the RK4 rule with $h/6 = 1/12$, and $12 \cdot 32 = 384$). The exact value is $e^{-1/2} = 0.6065306597\dots$; the three methods give $0.5$, $0.625$ and $233/384 = 0.6067708333\dots$ (PROVED here; Notebook 02a, In [3], repeats the arithmetic with exact fractions and checks the three results). RK4 is already correct to about four digits after a single large step.

### 2.5 The amplification factor

To understand the accuracy of a method we apply it to the simplest equation of all, the **test equation**

$$
y' = \lambda y
$$

with a constant number $\lambda$; its exact solution is $y(t) = e^{\lambda t} y(0)$, so one exact step multiplies $y$ by $e^{\lambda h}$. Write $z = \lambda h$. We now show that one step of each method multiplies $y_n$ by a number $R(z)$, its **amplification factor**, and find $R$.

*Euler.*

$$
y_{n+1} = y_n + h\, \lambda y_n = (1 + z)\, y_n
$$

(Euler's rule with $f(t, y) = \lambda y$, then $h \lambda = z$ and $y_n$ taken out as a common factor). So $R(z) = 1 + z$.

*Midpoint.*

$$
k_1 = \lambda y_n
$$

(the slope at the start);

$$
k_2 = \lambda\big(y_n + \tfrac{h}{2}\lambda y_n\big) = \lambda y_n\big(1 + \tfrac{z}{2}\big)
$$

(the slope at the estimated midpoint, with $h\lambda = z$);

$$
y_{n+1} = y_n + h\lambda y_n\big(1 + \tfrac{z}{2}\big) = \big(1 + z + \tfrac{z^2}{2}\big)\, y_n
$$

(the midpoint rule, then $h\lambda = z$ and the product multiplied out). So $R(z) = 1 + z + z^2/2$.

*RK4.*

$$
k_1 = \lambda y_n, \qquad k_2 = \lambda y_n\big(1 + \tfrac{z}{2}\big)
$$

(as for the midpoint method);

$$
k_3 = \lambda\big(y_n + \tfrac{h}{2} k_2\big) = \lambda y_n\big(1 + \tfrac{z}{2} + \tfrac{z^2}{4}\big)
$$

(we insert $k_2$: $\frac{h}{2} k_2 = \frac{z}{2} y_n (1 + \frac{z}{2})$);

$$
k_4 = \lambda\big(y_n + h k_3\big) = \lambda y_n\big(1 + z + \tfrac{z^2}{2} + \tfrac{z^3}{4}\big)
$$

(we insert $k_3$: $h k_3 = z y_n (1 + \frac{z}{2} + \frac{z^2}{4})$);

$$
k_1 + 2k_2 + 2k_3 + k_4 = \lambda y_n\big(6 + 3z + z^2 + \tfrac{z^3}{4}\big)
$$

(we add the four brackets, the middle two counted twice: the constants $1 + 2 + 2 + 1 = 6$, the terms with $z$: $1 + 1 + 1 = 3$, with $z^2$: $\frac12 + \frac12 = 1$, with $z^3$: $\frac14$);

$$
y_{n+1} = y_n + \frac{h}{6}\lambda y_n\big(6 + 3z + z^2 + \tfrac{z^3}{4}\big) = \big(1 + z + \tfrac{z^2}{2} + \tfrac{z^3}{6} + \tfrac{z^4}{24}\big)\, y_n
$$

(the RK4 rule; $h\lambda = z$, and each term of the bracket is multiplied by $z/6$). So

$$
R_{\rm Euler}(z) = 1 + z, \qquad R_{\rm midpoint}(z) = 1 + z + \frac{z^2}{2}, \qquad R_{\rm RK4}(z) = 1 + z + \frac{z^2}{2} + \frac{z^3}{6} + \frac{z^4}{24} .
$$

Each $R$ is a **polynomial** in $z$ (a sum of powers of $z$ with constant coefficients). Compare with the exponential series of Section 2.3: Euler keeps its first 2 terms, the midpoint method its first 3, RK4 its first 5 (PROVED here; Notebook 02a, In [4], derives the same polynomials with sympy and compares them with the series). The first term that a method misses decides its accuracy, as the next section shows.

### 2.6 Error, order, the log-log plot, rounding and Richardson's rule

**Error and order.** The **error** of a computation is the computed value minus the exact value. A method has **order** $p$ when its error at a fixed end time is close to $C h^p$ for small $h$, with a number $C$ that does not depend on $h$. Halving $h$ then divides the error by $2^p$:

$$
\frac{C h^p}{C (h/2)^p} = \frac{h^p}{h^p / 2^p} = 2^p
$$

(the constant $C$ cancels, and $(h/2)^p = h^p/2^p$ because a power of a quotient is the quotient of the powers).

**Why Euler has order 1.** Taylor's theorem says that one Euler step makes an error of about $\frac12 h^2 |y''|$. To reach the end time $T$ one needs $N = T/h$ steps, and $N$ errors of size about $h^2$ add up to about $N h^2 = T h$, which is proportional to $h^1$.

**The exact leading error for Problem A.** For Problem A we can do better and compute the error of each method to leading order. Here $\lambda = -1$, so one step multiplies $y$ by $R(-h)$, while the exact factor is $e^{-h}$. A method of order $p$ keeps the terms of the series of $e^{-h}$ up to the power $h^p$ (Euler $p = 1$, midpoint $p = 2$, RK4 $p = 4$):

$$
R(-h) = \sum_{k=0}^{p} \frac{(-h)^k}{k!}, \qquad e^{-h} = \sum_{k=0}^{\infty} \frac{(-h)^k}{k!}
$$

(Section 2.5 for $R$ and Section 2.3 for the series of the exponential, both at $z = -h$).

$$
R(-h) = e^{-h} - \frac{(-h)^{p+1}}{(p+1)!} - \dots
$$

($R$ is the series minus all the terms it misses; the dots stand for the missed terms with the powers $h^{p+2}$ and higher).

$$
R(-h) = e^{-h}(1 - q), \qquad q = e^{h}\Big(\frac{(-h)^{p+1}}{(p+1)!} + \dots\Big) = \frac{(-h)^{p+1}}{(p+1)!} + \dots
$$

(we take out the factor $e^{-h}$, which multiplies everything in the bracket by $e^{h}$; since $e^{h} = 1 + h + \dots$, that changes only the terms with higher powers of $h$).

$$
y_N = R(-h)^N = e^{-N h}(1 - q)^N = e^{-1}(1 - q)^N
$$

($N$ steps multiply the start value $y_0 = 1$ by $R(-h)$ $N$ times; a power of a product is the product of the powers; and $N h = 1$ when we compute up to $t = 1$).

$$
(1 - q)^N \approx 1 - N q
$$

(the first two terms of the binomial theorem $(1 - q)^N = 1 - Nq + \frac{N(N-1)}{2} q^2 - \dots$; the next term is of the size $(Nq)^2$, which is much smaller than $Nq$ when $Nq$ is small).

$$
N q \approx \frac{1}{h} \cdot \frac{(-1)^{p+1} h^{p+1}}{(p+1)!} = \frac{(-1)^{p+1} h^{p}}{(p+1)!}
$$

($N = 1/h$, $(-h)^{p+1} = (-1)^{p+1} h^{p+1}$, and one factor $h$ cancels).

$$
y_N - e^{-1} \approx -e^{-1} N q = e^{-1}\, \frac{(-1)^{p}\, h^{p}}{(p+1)!}
$$

(we subtract $e^{-1}$ from $y_N \approx e^{-1}(1 - Nq)$, and $-(-1)^{p+1} = (-1)^{p}$).

So at $t = 1$ Euler ends too LOW by $e^{-1} h/2$, the midpoint method too HIGH by $e^{-1} h^2/6$, and RK4 too high by $e^{-1} h^4/120$ (PROVED here, to leading order in $h$). The Rust solver of the Revision record makes $G = 900$ RK4 steps on an interval of length $L = 3$, so its step is $h = L/G = 1/300$ (COMPUTED from the record `Revision/kohn_sham/results/parameters.json`, keys `rk4Steps` and `L_tipCutoff`; Notebook 02a, In [11]). At this step the formula predicts $-6.1313 \times 10^{-4}$ (Euler), $+6.8126 \times 10^{-7}$ (midpoint) and $+3.7848 \times 10^{-13}$ (RK4); Notebook 02a measures $-6.1399 \times 10^{-4}$, $+6.8296 \times 10^{-7}$ and $+3.7920 \times 10^{-13}$, the ratios 1.0014, 1.0025 and 1.0019 (COMPUTED, In [11]); the small remaining differences are the next terms of the expansion, which the formula leaves out.

**The log-log plot.** The **logarithm** $\log_{10} x$ is the power to which 10 must be raised to give $x$; for example $\log_{10} 1000 = 3$ and $\log_{10} 0.001 = -3$. Write $\Delta = C h^p$ for the size of the error and take the logarithm:

$$
\log_{10} \Delta = \log_{10} C + p \log_{10} h
$$

(the logarithm of a product is the sum of the logarithms, and $\log_{10}(h^p) = p \log_{10} h$). As a function of $\log_{10} h$ this is a straight line with **slope** $p$. A **log-log plot** marks both axes in powers of ten, so the errors of a method of order $p$ lie on a straight line of slope $p$, and the order can be read off as a slope. A straight line fitted through measured points by **least squares** (the line that makes the sum of the squared vertical distances smallest) gives the measured order.

**Rounding errors.** A computer stores a number with about 16 significant decimal digits (53 binary digits). The spacing of the stored numbers near 1 is the **machine epsilon** $\epsilon = 2^{-52} \approx 2.2 \times 10^{-16}$, and every arithmetic operation rounds its result to a relative error of at most about $\epsilon/2$. With $N$ steps about $N$ such rounding errors add up. If all of them had their largest size and the same sign, their total would be about $N \epsilon = \epsilon/h$ times the size of the solution; this is a pessimistic **bound**, the scale of the worst case. In practice the rounding errors have both signs and partly cancel, so their total stays far below the bound; but it still grows with the number of steps, while the truncation error $C h^p$ falls. A smaller step is therefore not always better: below some step size the rounding errors take over, and the error grows again, slowly. For RK4 on Problem A this **rounding floor** is near $10^{-16}$, and with more steps the error grows again but stays 524 to 3709 times below the bound $N\epsilon e^{-1}$ (COMPUTED, Notebook 02a, In [10]).

**Richardson's rule.** In a real problem the exact answer $Y$ is unknown. Suppose a method of order $p$ gives the value $Y_h$ with the step $h$ and the value $Y_{h/2}$ with half the step, and that both errors are already close to $C h^p$:

$$
Y_h = Y + C h^p, \qquad Y_{h/2} = Y + \frac{C h^p}{2^p}
$$

(the order-$p$ error law at the steps $h$ and $h/2$).

$$
Y_h - Y_{h/2} = C h^p\Big(1 - \frac{1}{2^p}\Big) = \frac{C h^p}{2^p}\,(2^p - 1)
$$

(we subtract the second equation from the first; $Y$ cancels; then $1 - 2^{-p} = (2^p - 1)/2^p$).

$$
Y_{h/2} - Y = \frac{C h^p}{2^p} = \frac{Y_h - Y_{h/2}}{2^p - 1}
$$

(the error of the finer value, from the second equation, and then divided out of the previous line).

So the difference of two runs, divided by $2^p - 1$, estimates the error of the finer run without knowing $Y$; for RK4 it is $(Y_h - Y_{h/2})/15$. Subtracting the estimate gives the **extrapolated** value

$$
Y_{h/2} - \frac{Y_h - Y_{h/2}}{15} = \frac{16\, Y_{h/2} - Y_h}{15}
$$

(both terms written over the denominator 15), which is more accurate than either run (Notebook 02a, In [14]). Richardson's rule is only as good as its assumption: the errors must already follow $C h^p$.

### 2.7 The oscillator and the product of the two scale factors

**A complex number turns the oscillator into the test equation.** A **complex number** is $w = x + i v$ with real numbers $x$, $v$ and the number $i$ with $i^2 = -1$ (complex numbers are the subject of Chapter 1); its **complex conjugate** is $\bar w = x - i v$, and $|w|^2 = w \bar w = x^2 + v^2$. For the oscillator of Problem B put $w = x + i v$. Then

$$
w' = x' + i v' = v - i x
$$

(differentiate each part, and insert $x' = v$, $v' = -x$);

$$
w' = -i\,(x + i v) = -i\, w
$$

(multiply out: $-i x - i^2 v = -i x + v$, which is the previous line). So $w$ obeys the test equation with $\lambda = -i$, and one step of a method multiplies $w$ by $R(-ih)$. The energy is $E = (x^2 + v^2)/2 = |w|^2/2$, so one step multiplies $E$ by

$$
|R(-ih)|^2 = R(-ih)\, R(ih)
$$

(the conjugate of $R(-ih)$ is $R(ih)$, because the coefficients of the polynomial $R$ are real numbers and the conjugate of $-i$ is $i$).

*Euler.*

$$
R(-ih) R(ih) = (1 - ih)(1 + ih) = 1 - i^2 h^2 = 1 + h^2
$$

(the product $(a - b)(a + b) = a^2 - b^2$, and $i^2 = -1$). Every Euler step multiplies the energy by $1 + h^2 > 1$: the computed point spirals outwards.

*Midpoint.* $R(ih) = 1 + ih + (ih)^2/2 = (1 - \frac{h^2}{2}) + i h$, a complex number with the real part $1 - h^2/2$ and the imaginary part $h$, so

$$
|R(ih)|^2 = \Big(1 - \frac{h^2}{2}\Big)^2 + h^2 = 1 - h^2 + \frac{h^4}{4} + h^2 = 1 + \frac{h^4}{4}
$$

($|w|^2 = x^2 + v^2$, then the square multiplied out).

*RK4.* $R(ih) = 1 + ih - \frac{h^2}{2} - \frac{i h^3}{6} + \frac{h^4}{24}$ (powers of $i$: $i^2 = -1$, $i^3 = -i$, $i^4 = 1$), with the real part $c = 1 - \frac{h^2}{2} + \frac{h^4}{24}$ and the imaginary part $s = h - \frac{h^3}{6}$.

$$
c^2 = 1 - h^2 + \frac{h^4}{4} + \frac{h^4}{12} - \frac{h^6}{24} + \frac{h^8}{576} = 1 - h^2 + \frac{h^4}{3} - \frac{h^6}{24} + \frac{h^8}{576}
$$

(the square of a sum of three terms, $(a + b + d)^2 = a^2 + b^2 + d^2 + 2ab + 2ad + 2bd$ with $a = 1$, $b = -h^2/2$, $d = h^4/24$; then $\frac14 + \frac{1}{12} = \frac13$);

$$
s^2 = h^2 - \frac{h^4}{3} + \frac{h^6}{36}
$$

($(a + b)^2 = a^2 + 2ab + b^2$ with $a = h$, $b = -h^3/6$);

$$
c^2 + s^2 = 1 + \Big(-\frac{1}{24} + \frac{1}{36}\Big) h^6 + \frac{h^8}{576} = 1 - \frac{h^6}{72} + \frac{h^8}{576}
$$

(we add; the terms with $h^2$ and $h^4$ cancel, and $-\frac{3}{72} + \frac{2}{72} = -\frac{1}{72}$).

So one step multiplies the energy by $1 + h^2$ (Euler), $1 + h^4/4$ (midpoint) and $1 - h^6/72 + h^8/576$ (RK4) (PROVED here; Notebook 02a, In [4], derives the same three polynomials with sympy, and In [12] shows that the computed energies follow them to 13 digits). With $h = 0.2$ the factors are $1.04$, $1.0004$ and $0.99999911$.

**The product of the scale factors.** The 3-space factor obeys $a' = +a$ ($\lambda = +1$) and the extra-time factor $b' = -b$ ($\lambda = -1$), so one step multiplies $a$ by $R(h)$, $b$ by $R(-h)$ and their product, exactly 1 for the true solution, by $R(h) R(-h)$. For Euler

$$
R(h) R(-h) = (1 + h)(1 - h) = 1 - h^2
$$

(again $(a + b)(a - b) = a^2 - b^2$): the product shrinks by the factor $1 - h^2$ at every step, and the compensation of inflation by deflation is lost. For RK4 split $R(h) = c + s$ into its even part $c = 1 + \frac{h^2}{2} + \frac{h^4}{24}$ and its odd part $s = h + \frac{h^3}{6}$ (the letters $c$ and $s$ now stand for these new polynomials); then $R(-h) = c - s$, because the odd powers change sign, and

$$
R(h) R(-h) = (c + s)(c - s) = c^2 - s^2
$$

(again $(a + b)(a - b) = a^2 - b^2$).

$$
c^2 = 1 + h^2 + \frac{h^4}{4} + \frac{h^4}{12} + \frac{h^6}{24} + \frac{h^8}{576} = 1 + h^2 + \frac{h^4}{3} + \frac{h^6}{24} + \frac{h^8}{576}
$$

(the square of a sum of three terms, $(a + b + d)^2 = a^2 + b^2 + d^2 + 2ab + 2ad + 2bd$, now with $a = 1$, $b = +h^2/2$, $d = h^4/24$: $a^2 = 1$, $2ab = h^2$, $b^2 = h^4/4$, $2ad = h^4/12$, $2bd = h^6/24$, $d^2 = h^8/576$; then $\frac14 + \frac{1}{12} = \frac13$);

$$
s^2 = h^2 + \frac{h^4}{3} + \frac{h^6}{36}
$$

($(a + b)^2 = a^2 + 2ab + b^2$ with $a = h$, $b = +h^3/6$: $a^2 = h^2$, $2ab = h^4/3$, $b^2 = h^6/36$);

$$
R(h) R(-h) = c^2 - s^2 = 1 + \Big(\frac{1}{24} - \frac{1}{36}\Big) h^6 + \frac{h^8}{576} = 1 + \frac{h^6}{72} + \frac{h^8}{576}
$$

(we subtract; the terms with $h^2$ and $h^4$ cancel, and $\frac{1}{24} - \frac{1}{36} = \frac{3}{72} - \frac{2}{72} = \frac{1}{72}$). With $h = 0.25$ and 8 steps, Euler multiplies the product by $0.9375^8 = 0.597$, RK4 by a number within $3 \times 10^{-5}$ of 1 (PROVED here; COMPUTED in Notebook 02a, In [6]).

### 2.8 Example: Euler, midpoint and RK4 on the deflating scale factor and the oscillator

Notebook 02a puts Sections 2.2 to 2.7 to work. It makes one step of each method by hand with exact fractions; derives the amplification factors and the energy factors with sympy; solves the inflating and the deflating scale factor with Euler and RK4 and shows what Euler does to their product; measures the errors of the three methods for step sizes from $1/2$ down to $1/4096$ and reads the orders 1, 2 and 4 from a log-log plot; shows the rounding floor of RK4 with up to 262144 steps; reads the step of the Revision Kohn-Sham solver from its record and checks the predicted errors of Section 2.6 at that step; draws the phase portrait of the oscillator, measures by what angle each method runs ahead of the exact solution and draws the energy drift; and tests Richardson's rule. It ends with the line ALL 29 CHECKS PASSED (notebook 02a).

<!-- NOTEBOOK 02a -->

### 2.11 Line-by-line walk-through of Notebook 02a

The notebook has fifteen code cells, In [1] to In [15]. This section explains every line of every one of them, in order. A line that starts with `#` is a **comment**: Python skips it; it is there for the reader. In the quoted code a line `...)` stands for the remaining lines of a long figure caption; every caption is printed in full under its figure in Section 2.10, and the paragraph "What Figure 02a.k shows" after the code says what to look for.

**In [1], the set-up cell.** Its first part is the complete run instructions of Section 2.9 again, as comment lines, so that the notebook file carries its own instructions. The code starts below the line of `=` signs that reads THE SET-UP. This part is the same in every notebook of the book except for one line (the notebook's name); we explain it here once, and the walk-throughs of Notebooks 02b, 02c and 02d refer back to this explanation.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module** (a part of Python or of an installed package) so that the code can use it. `json` reads and writes the text format JSON, in which the Revision record stores its results; `os` gives access to the computer's environment; `textwrap` breaks long text into lines; `from pathlib import Path` takes the single name `Path` out of the module `pathlib`. A `Path` is the address of a file or a folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

These lines load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python), which show a picture file below a cell.

```python
NOTEBOOK_ID = "02a"  # this notebook: chapter 02, example a
```

A **variable** is a name for a value. This line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"02a"`. It is the only line of the set-up code that differs between notebooks.

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

`def` defines a **function**: a named piece of code that runs when it is called. The text in triple quotes under the `def` line is its **docstring**, a description that Python stores but does not run. `Path.cwd()` is the folder in which the notebook runs and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it; `[here, *here.parents]` is the list that starts with `here` and continues with all of them. The `for` loop takes these folders one after the other; the operator `/` joins a folder and a name into a longer path; `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository and `return` hands it back. If none does, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

`REPO` is the repository folder. `os.environ` holds the **environment variables** of the running program (named texts that the computer hands to it); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and otherwise the default, the repository folder written as a string. When you run the notebook the variable is not set, so the notebook writes into the repository; the book's checking tool sets it to a scratch folder.

```python
def repository_file(relative):
    """The path of the repository file relative, for READING (a Revision record)."""
    return REPO / relative


def output_file(relative):
    """The path at which to WRITE the repository file relative (its folder is made)."""
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

`repository_file("Revision/...")` gives the full path of a repository file, for reading. `output_file("Revision/...")` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the folder that will hold it (and any missing folder above it) and does nothing if it exists.

```python
def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters; `textwrap.fill` breaks it at blanks, and every line after the first starts with four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to matplotlib's built-in settings, so that a personal settings file cannot change the figures. `plt.rcParams.update({...})` then sets, for every figure of the notebook, the size (7.0 by 4.2 inches), the size of the letters (10 points) and a faint grid (30 per cent opaque). The braces make a **dictionary**: pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/02a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty dictionary and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored and `newline="\n"` stores the same line end on every system.

```python
def save_figure(fig, name, caption):
    """Save the figure fig as Revision/textbook/figures/<id>_<k>_<name>.png, record its
    caption in CAPTION_FILE, show the saved picture below the cell and close the figure.
    k counts the figures of the notebook 1, 2, 3, ...; a cell run again keeps its k."""
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
```

`setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far; so the figures are numbered 1, 2, 3, ..., and a cell that is run twice keeps its numbers. The file name joins the notebook id, the number and the name, for example `02a_1_scale_factors.png`.

```python
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

`fig.savefig` writes the PNG file with 150 dots per inch, without an empty margin and without the program's name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory. The caption is stored, and the whole dictionary of captions is written into the captions file (`json.dumps` turns it into JSON text with sorted keys). `display(Image(...))` shows the saved picture below the cell; its `metadata` tells the book's tools which file it is. The last line prints where the figure was saved.

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
```

`PASSED` is an empty **list** (an ordered collection in square brackets). `check` is the function behind every check of the book. `condition` is either `True` or `False`; if it is false, `raise AssertionError(...)` stops the notebook with an error that names the check. Otherwise the name is appended to `PASSED` and the line PASS followed by the name is printed. `record=None` makes the third argument optional; a check that reproduces a Revision record passes the record's file and check name, and a second line names them.

```python
def report(label, value, unit=""):
    """Print a key number as a line "RESULT <label> = <value> <unit>"."""
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    """Print the last line of the notebook: how many checks passed."""
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a RESULT line; the expression in round brackets adds a blank and the unit when a unit is given and nothing otherwise. `all_checks_passed` prints the last line of the notebook; `len(PASSED)` is the number of checks that passed. The last statement prints the one output line of In [1].

**In [2], the step rules and the solver.**

```python
import math  # exp, log10 and other functions of one number
from fractions import Fraction  # exact fractions such as 233/384

import numpy as np  # arrays (vectors) of numbers
import sympy as sp  # exact algebra with symbols
```

`math` holds the functions of single numbers (`math.exp`, `math.log2`, `math.factorial`). `Fraction` stores a fraction exactly as a numerator and a denominator, with no rounding. numpy (short name `np`) works with **arrays**, lists of numbers on which arithmetic acts entry by entry. sympy (short name `sp`) does exact algebra with symbols.

```python
# One colour per method (a set that colour-blind readers can tell apart); every
# method also has its own line style and marker, so the plots read in grey too.
COLORS = {"euler": "#eb6834", "midpoint": "#1baf7a", "rk4": "#2a78d6",
          "exact": "#000000", "guide": "#8a8986"}
MARKERS = {"euler": "s", "midpoint": "^", "rk4": "o"}
LABELS = {"euler": "Euler", "midpoint": "midpoint", "rk4": "RK4"}
```

Three dictionaries fix, for each method, a colour (written as a hexadecimal code of red, green and blue: orange for Euler, green for the midpoint method, blue for RK4, black for exact curves, grey for guide lines), a marker (`"s"` a square, `"^"` a triangle, `"o"` a circle) and the name printed in the legends.

```python
def euler_step(f, t, y, h):
    """One Euler step: follow the slope at the start for the whole step."""
    return y + h * f(t, y)
```

This is Euler's rule $y_{n+1} = y_n + h f(t_n, y_n)$ of Section 2.4. The argument `f` is itself a function, the right-hand side; `f(t, y)` is its value, the slope.

```python
def midpoint_step(f, t, y, h):
    """One midpoint step: use the slope at the estimated middle of the step."""
    k1 = f(t, y)  # the slope at the start
    k2 = f(t + h / 2, y + (h / 2) * k1)  # the slope at the estimated midpoint
    return y + h * k2
```

The midpoint rule, line for line as in Section 2.4.

```python
def rk4_step(f, t, y, h):
    """One step of the classical fourth-order Runge-Kutta method (RK4)."""
    k1 = f(t, y)  # the slope at the start
    k2 = f(t + h / 2, y + (h / 2) * k1)  # at the midpoint, reached with k1
    k3 = f(t + h / 2, y + (h / 2) * k2)  # at the midpoint again, reached with k2
    k4 = f(t + h, y + h * k3)  # at the end, reached with k3
    return y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)  # weights 1 : 2 : 2 : 1
```

The RK4 rule of Section 2.4. Because these three functions use only `+`, `-`, `*` and `/`, they work unchanged with ordinary numbers, exact fractions, sympy symbols and numpy arrays (vectors); the notebook uses all four.

```python
METHODS = {"euler": euler_step, "midpoint": midpoint_step, "rk4": rk4_step}
```

A dictionary from the name of each method to its step function, so that a loop can run all three.

```python
def solve(step, f, y0, t_end, n):
    """n equal steps of the rule step from t = 0 to t = t_end.  Returns the list
    of the n + 1 times and the list of the n + 1 computed values."""
    h = t_end / n  # the step size
    times, values = [0 * h], [y0]
    y = y0
    for i in range(n):
        y = step(f, i * h, y, h)  # t_i = i h (no rounding drift of the time)
        times.append((i + 1) * h)
        values.append(y)
    return times, values
```

`solve` makes `n` steps of size $h = T/n$. The two lists start with the time 0 (written `0 * h`, so that it is a fraction when `h` is one) and the start value. `range(n)` counts $i = 0, 1, \dots, n - 1$; each pass makes one step from the time $t_i = i h$ and appends the new time and value. The time is computed as `i * h` rather than by adding `h` again and again, so that no rounding error piles up in the time.

```python
def decay(t, y):
    """Problem A: y' = -y (an extra-time scale factor along the linear history)."""
    return -y


def growth(t, y):
    """y' = +y (the 3-space scale factor along the same history)."""
    return y


say("Three step rules and the solver are defined.")
```

The two right-hand sides of Section 2.2: `decay` for the deflating extra-time factor $b$ and `growth` for the inflating 3-space factor $a$. The cell prints one line.

**In [3], one step by hand.**

```python
h = Fraction(1, 2)  # the step size 1/2 as an exact fraction
one_step = {name: step(decay, 0, Fraction(1), h) for name, step in METHODS.items()}
```

`Fraction(1, 2)` is the exact fraction $1/2$. The second line is a **dictionary comprehension**: for every pair (name, step function) of `METHODS.items()` it makes one step of Problem A from $y = 1$ and stores the result under the method's name. Because all numbers are fractions, the results are exact.

```python
for name, value in one_step.items():
    say(f"{LABELS[name]:9} after one step: {str(value):8} = {float(value):.10f}")
say(f"exact     e^(-1/2)                 = {math.exp(-0.5):.10f}")
```

The loop prints each result as a fraction and as a decimal number; `{...:9}` pads the name to 9 characters so that the columns line up, and `{...:.10f}` writes 10 digits after the decimal point. The last line prints $e^{-1/2} = 0.6065306597$.

```python
check(one_step["euler"] == Fraction(1, 2), "one Euler step of y' = -y gives 1/2")
check(one_step["midpoint"] == Fraction(5, 8), "one midpoint step gives 5/8")
check(one_step["rk4"] == Fraction(233, 384), "one RK4 step gives 233/384")
```

Three checks compare the exact results with the hand calculation of Section 2.4: $1/2$, $5/8$ and $233/384$. The output shows 0.5, 0.625 and 0.6067708333 against the exact 0.6065306597.

**In [4], the amplification factors.**

```python
z = sp.symbols("z")  # z = lambda h
hs = sp.symbols("h", positive=True)  # a positive step size, as a symbol
```

`sp.symbols` makes sympy symbols: letters that stand for any number. `z` is $\lambda h$; `hs` is a step size $h$, declared positive.

```python
def linear(t, y):
    """The test equation y' = z y."""
    return z * y


one = sp.Integer(1)  # sympy's exact 1 (so that 1/2 stays the exact fraction 1/2)
R = {name: sp.expand(step(linear, 0, one, one)) for name, step in METHODS.items()}
```

`linear` is the right-hand side of the test equation with $\lambda h = z$. With the step $h = 1$ (sympy's exact integer 1, so that `h / 2` is the exact fraction $1/2$ and not the rounded number 0.5) and the start value 1, one step of each method gives exactly $R(z)$; `sp.expand` multiplies out all brackets. This is the derivation of Section 2.5, done by the computer.

```python
taylor = sp.series(sp.exp(z), z, 0, 6).removeO()  # 1 + z + ... + z^5/120
terms = sp.Poly(taylor, z).all_coeffs()[::-1]  # the coefficients 1, 1, 1/2, ...
```

`sp.series(sp.exp(z), z, 0, 6)` is the series of $e^{z}$ around $z = 0$ up to the power $z^5$, followed by a symbol for the left-out terms, which `.removeO()` drops. `sp.Poly(...).all_coeffs()` lists the coefficients from the highest power down, and `[::-1]` reverses the list, so that `terms[k]` is the coefficient $1/k!$ of $z^k$.

```python
for name, keep in (("euler", 2), ("midpoint", 3), ("rk4", 5)):
    partial = sum(terms[k] * z ** k for k in range(keep))  # the first keep terms
    say(f"R_{name}(z) = {sp.expand(R[name])}")
    check(sp.expand(R[name] - partial) == 0,
          f"R_{name}(z) equals the first {keep} terms of the series of e^z")
```

For each method, `partial` is the sum of the first `keep` terms of the series ($z^k$ is written `z ** k` in Python). The cell prints $R(z)$ and checks that $R(z)$ minus that partial sum is exactly zero: Euler keeps 2 terms, the midpoint method 3, RK4 5. The output reads `z + 1`, `z**2/2 + z + 1` and `z**4/24 + z**3/6 + z**2/2 + z + 1`.

```python
# The energy factor of one oscillator step, R(i h) R(-i h), as a polynomial in h.
ENERGY_FACTOR = {name: sp.expand(R[name].subs(z, sp.I * hs) *
                                 R[name].subs(z, -sp.I * hs))
                 for name in METHODS}
for name, factor in ENERGY_FACTOR.items():
    say(f"energy factor per step, {LABELS[name]:8}: {factor}")
check(ENERGY_FACTOR["euler"] == 1 + hs ** 2
      and ENERGY_FACTOR["midpoint"] == 1 + hs ** 4 / 4
      and ENERGY_FACTOR["rk4"] == 1 - hs ** 6 / 72 + hs ** 8 / 576,
      "energy factors 1 + h^2, 1 + h^4/4, 1 - h^6/72 + h^8/576")
```

`.subs(z, sp.I * hs)` replaces $z$ by $ih$ (`sp.I` is sympy's $i$). The product $R(ih) R(-ih)$, multiplied out, is the factor by which one step multiplies the oscillator's energy (Section 2.7). The check compares it with $1 + h^2$, $1 + h^4/4$ and $1 - h^6/72 + h^8/576$, the results of Section 2.7; the output prints the three polynomials.

**In [5], the inflating and the deflating scale factor.**

```python
H_COARSE, STEPS = 0.25, 8  # step size and number of steps: t from 0 to 2
curves = {}
for name in ("euler", "rk4"):
    t_list, a_list = solve(METHODS[name], growth, 1.0, 2.0, STEPS)
    _, b_list = solve(METHODS[name], decay, 1.0, 2.0, STEPS)
    curves[name] = (np.array(t_list), np.array(a_list), np.array(b_list))
t_fine = np.linspace(0.0, 2.0, 201)  # many points for the exact curves
```

Two names are given two values at once: the step $0.25$ and the number of steps 8 (so $t$ runs from 0 to 2). For Euler and RK4 the loop solves $a' = a$ (`growth`) and $b' = -b$ (`decay`) from the value 1; `_` is the conventional name for a result that is not needed (the times, already known). The three lists are turned into numpy arrays and stored in `curves`. `np.linspace(0.0, 2.0, 201)` makes 201 equally spaced times for drawing the exact curves smoothly.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
left.plot(t_fine, np.exp(t_fine), color=COLORS["exact"], lw=1.0,
          label="exact $e^{t}$")
right.plot(t_fine, np.exp(-t_fine), color=COLORS["exact"], lw=1.0,
           label="exact $e^{-t}$")
```

`plt.subplots(1, 2, ...)` makes a figure with one row of two panels, named `left` and `right`. `.plot(xs, ys, ...)` draws a line through the points; `lw` is the line width and `label` the name in the legend (text between dollar signs is typeset as mathematics). The exact curves $e^{t}$ and $e^{-t}$ are drawn in black.

```python
for name in ("euler", "rk4"):
    t_n, a_n, b_n = curves[name]
    style = dict(color=COLORS[name], marker=MARKERS[name], ms=5, lw=1.2)
    left.plot(t_n, a_n, **style, label=f"{LABELS[name]}, $h = 0.25$")
    right.plot(t_n, b_n, **style, label=f"{LABELS[name]}, $h = 0.25$")
```

For each method the three arrays are unpacked; `style` is a dictionary of drawing options (colour, marker, marker size `ms`, line width), and `**style` passes its entries as named arguments. The computed points of $a$ go into the left panel, those of $b$ into the right panel.

```python
left.set_title("3-space factor $a$: $da/dx_4 = +a$ (inflates)")
right.set_title("extra-time factor $b$: $db/dx_4 = -b$ (deflates)")
for ax in (left, right):
    ax.set_xlabel("time $x_4$ (units $1/H$, $A = 1$)")
    ax.legend(fontsize=8)
left.set_ylabel("scale factor (pure number)")
save_figure(fig, "scale_factors",
            "Left: the 3-space scale factor $a = e^{x_4}$, which obeys "
            ...)
```

Titles, axis labels and legends; then `save_figure` saves the figure as `02a_1_scale_factors.png` with its caption (printed in full under Figure 02a.1 in Section 2.10; Python joins strings written next to each other into one). **What Figure 02a.1 shows:** in the left panel the Euler squares fall more and more below the growing exact curve, in the right panel they decay faster than the exact curve; the RK4 circles lie on both exact curves even with the coarse step $0.25$.

```python
a_euler, b_euler = curves["euler"][1][-1], curves["euler"][2][-1]
a_rk4, b_rk4 = curves["rk4"][1][-1], curves["rk4"][2][-1]
report("a(2): exact, Euler, RK4", f"{math.exp(2):.6f}, {a_euler:.6f}, {a_rk4:.6f}")
report("b(2): exact, Euler, RK4", f"{math.exp(-2):.6f}, {b_euler:.6f}, {b_rk4:.6f}")
```

`curves["euler"][1]` is the array of the Euler values of $a$, and `[-1]` its last entry (the value at $t = 2$). The two RESULT lines print $a(2)$: exact 7.389056, Euler 5.960464, RK4 7.388665, and $b(2)$: exact 0.135335, Euler 0.100113, RK4 0.135346.

```python
check(abs(a_euler - 1.25 ** 8) < 1e-12 and abs(b_euler - 0.75 ** 8) < 1e-15,
      "Euler gives exactly 1.25^8 and 0.75^8 after 8 steps")
check(abs(a_rk4 / math.exp(2) - 1) < 1e-3 and abs(b_rk4 / math.exp(-2) - 1) < 1e-3,
      "RK4 with h = 0.25 is within 0.1 percent of e^2 and e^(-2)")
```

Euler multiplies by $R(0.25) = 1.25$ and $R(-0.25) = 0.75$ per step, so after 8 steps it must give $1.25^8 = 5.960464\dots$ and $0.75^8 = 0.100113\dots$; `abs` is the absolute value and `1e-12` means $10^{-12}$ (the allowed rounding). The second check confirms that RK4 is within $10^{-3}$, that is 0.1 per cent, of the exact values.

**In [6], the product of the two scale factors.**

```python
PRODUCT_FACTOR = {name: sp.expand(R[name].subs(z, hs) * R[name].subs(z, -hs))
                  for name in ("euler", "rk4")}
for name, factor in PRODUCT_FACTOR.items():
    say(f"factor of a b per step, {LABELS[name]:5}: {factor}")
check(PRODUCT_FACTOR["euler"] == 1 - hs ** 2
      and PRODUCT_FACTOR["rk4"] == 1 + hs ** 6 / 72 + hs ** 8 / 576,
      "R(h) R(-h) is 1 - h^2 (Euler) and 1 + h^6/72 + h^8/576 (RK4)")
```

sympy multiplies out $R(h) R(-h)$, the factor by which one step multiplies the product $a b$ (Section 2.7), prints it and checks the two results of Section 2.7.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
left.axhline(1.0, color=COLORS["exact"], lw=1.0, label="exact $a b = 1$")
products = {}
```

A new figure with two panels; `axhline(1.0, ...)` draws a horizontal line at height 1, the exact product. `products` will hold the computed products.

```python
for name in ("euler", "rk4"):
    t_n, a_n, b_n = curves[name]
    products[name] = a_n * b_n  # the computed product at every step
    factor = float(PRODUCT_FACTOR[name].subs(hs, sp.Rational(1, 4)))  # h = 1/4
    style = dict(color=COLORS[name], marker=MARKERS[name], ms=5, lw=1.2)
    left.plot(t_n, products[name], **style, label=f"{LABELS[name]}, $h = 0.25$")
    right.semilogy(t_n[1:], np.abs(products[name][1:] - 1.0), **style,
                   label=f"{LABELS[name]}: measured")
    predicted = np.abs(factor ** np.arange(1, STEPS + 1) - 1.0)
    right.semilogy(t_n[1:], predicted, ":", color=COLORS["exact"], lw=1.0)
```

For each method `a_n * b_n` multiplies the two arrays entry by entry. `factor` is the per-step factor at $h = 1/4$ (sympy's exact `Rational(1, 4)`), turned into an ordinary number by `float`. The left panel shows the product; the right panel shows its distance from 1, $|ab - 1|$, with `semilogy`, which draws the vertical axis logarithmically. `[1:]` leaves out the starting point, where the distance is exactly 0 and cannot be drawn on a logarithmic axis. `np.arange(1, STEPS + 1)` is the array $1, 2, \dots, 8$, so `factor ** np.arange(...)` is the predicted product after $n$ steps; the dotted black line (`":"`) draws its distance from 1.

```python
right.plot([], [], ":", color=COLORS["exact"], label="predicted $|R(h)^n R(-h)^n - 1|$")
left.set_ylabel("product $a b$ (pure number)")
right.set_ylabel("$|a b - 1|$ (pure number)")
left.set_title("the product $a b$")
right.set_title("its distance from 1 (logarithmic axis)")
for ax in (left, right):
    ax.set_xlabel("time $x_4$ (units $1/H$)")
    ax.legend(fontsize=8)
save_figure(fig, "scale_factor_product",
            "Left: the product $a b$ of the 3-space factor and the extra-time "
            ...)
```

`right.plot([], [], ...)` draws nothing (two empty lists) but adds an entry for the dotted prediction to the legend. Then labels, titles, legends and the saved figure `02a_2_scale_factor_product.png`. **What Figure 02a.2 shows:** the Euler product falls step by step to $0.9375^8 = 0.597$; the RK4 product stays at 1 to within $3 \times 10^{-5}$; on the logarithmic right panel every measured point lies on its dotted prediction.

```python
check(abs(products["euler"][-1] - (1 - H_COARSE ** 2) ** 8) < 1e-14,
      "Euler multiplies the product a b by 1 - h^2 per step")
rk4_factor = 1 + H_COARSE ** 6 / 72 + H_COARSE ** 8 / 576
check(abs(products["rk4"][-1] - rk4_factor ** 8) < 1e-14
      and abs(products["rk4"][-1] - 1) < 3e-5,
      "RK4 multiplies a b by 1 + h^6/72 + h^8/576 per step (within 3e-5 of 1)")
```

The final products must equal $(1 - h^2)^8$ (Euler) and $(1 + h^6/72 + h^8/576)^8$ (RK4) up to rounding, and the RK4 product must be within $3 \times 10^{-5}$ of 1.

**In [7], the convergence study.**

```python
EXACT_A = math.exp(-1.0)  # the exact value y(1) = e^(-1)
N_LIST = [2 ** k for k in range(1, 13)]  # 2, 4, ..., 4096 steps
ends = {name: [solve(step, decay, 1.0, 1.0, n)[1][-1] for n in N_LIST]
        for name, step in METHODS.items()}
errors = {name: np.abs(np.array(values) - EXACT_A) for name, values in ends.items()}
```

`EXACT_A` is $e^{-1} = 0.367879\dots$. `N_LIST` is the list $2^1, 2^2, \dots, 2^{12}$ (`range(1, 13)` counts 1 to 12). For each method and each $N$, `solve(...)[1][-1]` is the computed value at $t = 1$; `ends` stores the twelve end values of each method and `errors` their distances from $e^{-1}$.

```python
say("     N        h     Euler y_N   error Euler  error midpoint     error RK4")
for i, n in enumerate(N_LIST):
    y_euler = ends["euler"][i]  # the Euler value y_N
    e_euler, e_mid, e_rk4 = (errors[name][i] for name in METHODS)  # three errors
    say(f"{n:6d} {1 / n:8.6f}  {y_euler:12.6f}  {e_euler:11.3e}  {e_mid:14.3e}  "
        f"{e_rk4:12.3e}")
```

`enumerate(N_LIST)` gives the position `i` together with each `n`. Each row prints $N$, $h = 1/N$, the Euler value and the three errors; `:6d` writes a whole number in 6 places, `:11.3e` a number in scientific notation with 3 digits after the point (for example `1.179e-01` means $1.179 \times 10^{-1}$). The table shows the Euler error halving and the midpoint error quartering from row to row, while the RK4 error falls 16-fold until it reaches about $10^{-16}$ at $N = 2048$.

```python
h_array = 1.0 / np.array(N_LIST, dtype=float)
FIT = {"euler": slice(5, 12), "midpoint": slice(5, 12), "rk4": slice(1, 8)}
slopes = {}
for name, part in FIT.items():
    # polyfit(x, y, 1) returns (slope, intercept) of the best straight line.
    slope, _ = np.polyfit(np.log10(h_array[part]), np.log10(errors[name][part]), 1)
    slopes[name] = slope
    report(f"measured order of {LABELS[name]} (slope)", f"{slope:.4f}")
```

`h_array` holds the twelve step sizes. `FIT` chooses, for each method, the rows used for the straight-line fit: `slice(5, 12)` is the positions 5 to 11 ($N = 64$ to 4096), where the Euler and midpoint errors are already close to $C h^p$; `slice(1, 8)` is the positions 1 to 7 ($N = 4$ to 256), where the RK4 error is not yet touched by rounding. `np.polyfit(x, y, 1)` fits the least-squares straight line through the points $(\log_{10} h, \log_{10} e)$ and returns its slope and its intercept. The measured orders are 1.0014, 2.0025 and 4.0439 (COMPUTED).

```python
check([round(v, 6) for v in ends["euler"][:4]]
      == [0.25, 0.316406, 0.343609, 0.356074],
      "Euler values (1 - h)^N for h = 1/2, 1/4, 1/8, 1/16")
check(abs(slopes["euler"] - 1) < 0.02 and abs(slopes["midpoint"] - 2) < 0.02
      and abs(slopes["rk4"] - 4) < 0.1,
      "the measured orders are 1, 2 and 4")
```

The first check compares the first four Euler values, rounded to 6 digits, with $(1 - h)^N$: $(1/2)^2 = 0.25$, $(3/4)^4 = 0.316406$, $(7/8)^8 = 0.343609$, $(15/16)^{16} = 0.356074$. The second requires the slopes to be within 0.02 of 1 and 2 and within 0.1 of 4.

**In [8], the log-log plot.**

```python
fig, ax = plt.subplots(figsize=(7.0, 5.0))
for name in METHODS:
    ax.loglog(h_array, errors[name], color=COLORS[name], marker=MARKERS[name],
              ms=5, lw=1.2, label=f"{LABELS[name]} (measured slope "
              f"{slopes[name]:.2f})")
```

`ax.loglog` draws with both axes logarithmic. Each method's twelve errors are drawn against the step sizes, with the measured slope in the legend.

```python
    order = {"euler": 1, "midpoint": 2, "rk4": 4}[name]
    anchor = FIT[name].stop - 1  # the last fitted point
    guide = errors[name][anchor] * (h_array / h_array[anchor]) ** order
    ax.loglog(h_array, guide, "--", color=COLORS["guide"], lw=0.9)
    ax.text(h_array[0] * 1.15, guide[0], f"slope {order}", fontsize=8,
            color=COLORS["guide"], va="center")
```

Still inside the loop: `order` is the expected order. `FIT[name].stop - 1` is the last position of the fitted rows. The guide line $\Delta_{\rm anchor} (h/h_{\rm anchor})^p$ (with $\Delta_{\rm anchor}$ the error at that point) passes through that point with the exact slope $p$; it is drawn dashed (the line-style string of two hyphens) in grey, and `ax.text` writes "slope p" next to its right end (`va="center"` centres the text vertically).

```python
ax.set_xlim(h_array[-1] / 1.5, h_array[0] * 3.0)
ax.set_ylim(1e-17, 1.0)
ax.set_xlabel("step size $h$ (time units)")
ax.set_ylabel("error $|y_N - e^{-1}|$ at $t = 1$")
ax.set_title("Problem A: error at the end time against the step size")
ax.legend(loc="lower right")
save_figure(fig, "convergence_loglog",
            "The error at the end time $t = 1$ of problem A, $y' = -y$, for the "
            ...)
check(errors["rk4"][7] < 1e-11 < errors["midpoint"][7] < errors["euler"][7],
      "at N = 256: RK4 error < 1e-11 < midpoint error < Euler error")
```

The axis ranges leave room for the slope labels; then labels, title, legend and the saved figure `02a_3_convergence_loglog.png`. The check is a chain of comparisons at position 7 ($N = 256$): the RK4 error $7.2 \times 10^{-13}$ is below $10^{-11}$, which is below the midpoint error $9.4 \times 10^{-7}$, which is below the Euler error $7.2 \times 10^{-4}$. **What Figure 02a.3 shows:** three straight lines of points, parallel to the guides of slopes 1, 2 and 4: the orders can be read off by eye. The RK4 line bends away at the bottom left, where rounding takes over.

**In [9], what halving the step does.**

```python
ratios = {name: errors[name][:-1] / errors[name][1:] for name in METHODS}
```

`errors[name][:-1]` is the array without its last entry and `errors[name][1:]` without its first, so the quotient is $e(h)/e(h/2)$ for every pair of neighbouring rows.

```python
fig, ax = plt.subplots()
for name in METHODS:
    shown = slice(0, 8) if name == "rk4" else slice(0, 11)  # RK4: before rounding
    ax.semilogx(N_LIST[1:][shown], ratios[name][shown], color=COLORS[name],
                marker=MARKERS[name], ms=5, lw=1.2, label=LABELS[name])
```

Each ratio is drawn against the $N$ of the finer run (`N_LIST[1:]`), with a logarithmic horizontal axis (`semilogx`); for RK4 only the first 8 ratios (up to $N = 512$) are drawn, because later its errors are rounding noise.

```python
for target in (2, 4, 16):
    # a dashed line from N = 3 to just beyond the data, its label to the right
    ax.hlines(target, 3.0, N_LIST[-1] * 1.4, ls="--", color=COLORS["guide"], lw=0.9)
    ax.text(N_LIST[-1] * 1.6, target, f"$2^{{{int(math.log2(target))}}}$ = "
            f"{target}", va="center", ha="left", fontsize=8, color=COLORS["guide"])
ax.set_xlim(3.0, N_LIST[-1] * 8.0)  # room on the right for the labels
```

Dashed horizontal guide lines at $2 = 2^1$, $4 = 2^2$ and $16 = 2^4$, each labelled; `math.log2(target)` is the power of 2, and in an f-string a doubled brace prints one brace, so the label reads $2^{1} = 2$, and so on.

```python
ax.set_xlabel("number of steps $N$ of the finer run ($h = 1/N$)")
ax.set_ylabel("error ratio $e(2h)/e(h)$")
ax.set_title("Halving the step divides the error by $2^p$")
ax.legend(loc="center left")
save_figure(fig, "error_ratios",
            "The factor by which the error of problem A at $t = 1$ shrinks when the "
            ...)
```

Labels, title, legend and the saved figure `02a_4_error_ratios.png`. **What Figure 02a.4 shows:** the three curves settle on the guide lines 2, 4 and 16, which is what order 1, 2 and 4 means.

```python
ratio_euler = ratios["euler"][-1]  # the last ratio: N = 2048 -> 4096
ratio_midpoint = ratios["midpoint"][-1]
ratio_rk4 = ratios["rk4"][5]  # N = 64 -> 128, before rounding matters
report("ratio Euler at N = 4096", f"{ratio_euler:.5f}")
report("ratio midpoint at N = 4096", f"{ratio_midpoint:.5f}")
report("ratio RK4 at N = 128", f"{ratio_rk4:.4f}")
check(abs(ratio_euler - 2) < 0.001 and abs(ratio_midpoint - 4) < 0.001
      and abs(ratio_rk4 - 16) < 0.2,
      "halving h divides the errors by 2, 4 and 16")
```

The cell picks the last ratios of Euler and of the midpoint method and the RK4 ratio from $N = 64$ to 128, prints them (2.00020, 4.00073 and 16.1047; COMPUTED) and checks them against 2, 4 and 16.

**In [10], where rounding takes over.**

```python
N_LONG = [2 ** k for k in range(1, 19)]  # 2 ... 262144 steps
rk4_long = np.array([abs(solve(rk4_step, decay, 1.0, 1.0, n)[1][-1] - EXACT_A)
                     for n in N_LONG])
h_long = 1.0 / np.array(N_LONG, dtype=float)
best = int(np.argmin(rk4_long))  # the position of the smallest error
EPS = 2.0 ** -52  # the machine epsilon
```

RK4 is run with $N = 2, 4, \dots, 2^{18} = 262144$ steps and the eighteen errors at $t = 1$ are stored. `np.argmin` is the position of the smallest error. `EPS` is the machine epsilon $2^{-52}$ of Section 2.6.

```python
fig, ax = plt.subplots()
shown = rk4_long > 0  # an error of exactly 0 cannot be drawn on a log axis
ax.loglog(h_long[shown], rk4_long[shown], color=COLORS["rk4"], marker="o", ms=5,
          lw=1.2, label="RK4: measured error")
ax.loglog(h_long, errors["rk4"][3] * (h_long / h_array[3]) ** 4, "--",
          color=COLORS["guide"], lw=0.9, label="truncation $C h^4$")
ax.loglog(h_long, EPS * EXACT_A / h_long, ":", color=COLORS["exact"], lw=1.0,
          label="rounding bound $N \\epsilon\\, e^{-1}$")
```

`rk4_long > 0` is an array of `True` and `False`; used as an index (`h_long[shown]`) it keeps only the entries where it is `True`. The measured errors are drawn as circles; the dashed line is the truncation error $C h^4$ through the point $N = 16$; the dotted line is $N \epsilon e^{-1} = \epsilon e^{-1}/h$, the pessimistic bound of Section 2.6: the size that $N$ rounding errors of relative size $\epsilon$ would reach only if all of them had their largest size and the same sign (in a Python string `\\` stands for one backslash, which matplotlib's mathematics needs).

```python
ax.set_ylim(1e-18, 1e-2)
ax.set_xlabel("step size $h = 1/N$ (time units)")
ax.set_ylabel("error $|y_N - e^{-1}|$")
ax.set_title("RK4: truncation error against rounding error")
ax.legend(loc="upper center")
save_figure(fig, "rounding_floor",
            "The error of RK4 for problem A at $t = 1$ against the step size $h$ "
            ...)
report("smallest RK4 error", f"{rk4_long[best]:.3e} at N = {N_LONG[best]}")
report("RK4 error at N = 262144", f"{rk4_long[-1]:.3e}")
```

Axis range, labels, legend, the saved figure `02a_5_rounding_floor.png`, and two RESULT lines: the smallest error is $1.110 \times 10^{-16}$ at $N = 4096$, and the error with 262144 steps is $5.773 \times 10^{-15}$, fifty times larger (COMPUTED).

```python
bound = EPS * EXACT_A * np.array(N_LONG, dtype=float)  # the dotted line
below = bound[best + 1:] / rk4_long[best + 1:]  # past the minimum: bound / error
report("bound N eps e^-1 / measured error past the minimum (smallest, largest)",
       f"{below.min():.0f}, {below.max():.0f}")
```

`bound` holds the value $N \epsilon e^{-1}$ of the dotted line for each of the eighteen runs. `bound[best + 1:]` keeps the entries after the position of the smallest error (the runs with more steps than $N = 4096$); dividing them by the measured errors of the same runs gives, for each run, how many times its error lies below the bound. The RESULT line prints the smallest and the largest of these ratios, 524 and 3709 (COMPUTED). **What Figure 02a.5 shows:** coming from the right (large steps), the error falls along the slope-4 line; near $10^{-16}$ it stops; for smaller steps it grows again, but slowly and 524 to 3709 times below the dotted bound. The rounding errors partly cancel, so the bound gives only the scale of the worst case, not the error itself.

```python
check(rk4_long[best] < 1e-15 and 256 <= N_LONG[best] <= 16384,
      "the smallest RK4 error is below 1e-15, reached at N between 256 and 16384")
check(rk4_long[-1] > 10 * max(rk4_long[best], EPS * EXACT_A)
      and rk4_long[-1] < 1e-11,
      "with 262144 steps rounding has made the error grow again")
check(np.all(below > 100),
      "past the minimum the error stays over 100 times below the bound N eps e^-1")
```

Three checks: the floor is below $10^{-15}$ and is reached at a moderate $N$; with the most steps the error is more than ten times the floor (so rounding has made it grow), yet still below $10^{-11}$; and past the minimum every error lies more than 100 times below the bound $N \epsilon e^{-1}$. The checks use ranges rather than exact values, because rounding errors can differ in the last bits from one computer to another.

**In [11], the step of the Revision solver and the first missed term.**

```python
PARAMETERS = "Revision/kohn_sham/results/parameters.json"
parameters = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
G_KS = parameters["numerics"]["rk4Steps"]  # the solver's number of RK4 steps
L_KS = parameters["physics"]["L_tipCutoff"]  # the length of its interval in y
A_KS = parameters["physics"]["historyA"]  # the constant A of a4 = A H x4
H_KS = parameters["physics"]["H"]  # the author's constant H
h_ks = L_KS / G_KS  # the solver's step
```

The cell reads the Revision record of the Kohn-Sham solver's parameters: `read_text` reads the file as text and `json.loads` turns the JSON text into nested dictionaries. `parameters["numerics"]["rk4Steps"]` is the entry `rk4Steps` inside the part `numerics`: the number $G = 900$ of RK4 steps. From the part `physics` come the length $L = 3$ of the interval in the hidden coordinate (the tip cut-off), the constant $A$ of the history and the author's $H$. The solver's step is $h = L/G$.

```python
report("solver: RK4 steps G, interval length L, step h = L/G",
       f"{G_KS}, {L_KS}, {h_ks:.10f}")
report("linear history a4 = A H x4 of the record: A, H", f"{A_KS}, {H_KS}")
check(G_KS == 900 and L_KS == 3.0 and A_KS == 1.0 and H_KS == 1.0,
      "the solver makes 900 RK4 steps on L = 3 (h = 1/300); the history has A = H = 1",
      record=f"{PARAMETERS}, keys rk4Steps, L_tipCutoff, historyA and H")
```

The two RESULT lines print 900, 3.0, 0.0033333333 and 1.0, 1.0; the check confirms the values and names the record and its keys in its second line (COMPUTED: reproduces `Revision/kohn_sham/results/parameters.json`, keys `rk4Steps`, `L_tipCutoff`, `historyA` and `H`).

```python
N_KS = round(1.0 / h_ks)  # 300 steps of h = 1/300 reach t = 1
ORDER = {"euler": 1, "midpoint": 2, "rk4": 4}  # the orders measured in section 9
agreement = []
```

`round(1.0 / h_ks)` is the whole number 300: so many steps of the solver's size reach $t = 1$. `ORDER` holds the orders, and `agreement` will collect the ratios of measured to predicted errors.

```python
for name, step in METHODS.items():
    p = ORDER[name]
    measured = solve(step, decay, 1.0, 1.0, N_KS)[1][-1] - EXACT_A  # signed error
    predicted = EXACT_A * (-1) ** p * h_ks ** p / math.factorial(p + 1)
    agreement.append(measured / predicted)
    say(f"{LABELS[name]:9} with h = 1/{N_KS}: error {measured:+.4e}, predicted "
        f"{predicted:+.4e}, ratio {measured / predicted:.5f}")
check(all(abs(ratio - 1) < 0.01 for ratio in agreement),
      "at the solver's step the errors are e^(-1) (-1)^p h^p/(p+1)! within 1 %")
```

For each method the signed error at $t = 1$ with 300 steps is measured (this time without `abs`, so that its sign is kept), and the prediction $e^{-1}(-1)^p h^p/(p+1)!$ of Section 2.6 is computed (`math.factorial(p + 1)` is $(p+1)!$, and `(-1) ** p` is $(-1)^p$). The quotient of the two is appended to `agreement`. The printed lines show Euler $-6.1399 \times 10^{-4}$ against the predicted $-6.1313 \times 10^{-4}$, the midpoint method $+6.8296 \times 10^{-7}$ against $+6.8126 \times 10^{-7}$, and RK4 $+3.7920 \times 10^{-13}$ against $+3.7848 \times 10^{-13}$; the ratios are 1.00139, 1.00250 and 1.00190 (COMPUTED). `all(...)` is true when every entry of the sequence in its brackets is true, so the check requires every ratio to be within 1 per cent of 1. The predicted signs (Euler too low, the other two too high) and sizes are right, and at the Revision solver's step RK4 is about a billion times more accurate than Euler.

**In [12], the oscillator: phase portrait and energy.**

```python
def oscillator(t, Y):
    """Problem B: x' = v, v' = -x for the state Y = (x, v)."""
    return np.array([Y[1], -Y[0]])


Y0 = np.array([1.0, 0.0])  # x(0) = 1, v(0) = 0
H_OSC = 0.2  # the step size
portraits = {name: np.array(solve(step, oscillator, Y0, 10.0, 50)[1])
             for name, step in METHODS.items()}
```

The state is a numpy array `Y` with `Y[0]` $= x$ and `Y[1]` $= v$ (positions are counted from 0), and the right-hand side returns the array $(v, -x)$. The start is $(1, 0)$. Each method makes 50 steps of $h = 0.2$ up to $t = 10$; the list of the 51 states becomes an array with 51 rows and 2 columns.

```python
angle = np.linspace(0.0, 2 * np.pi, 400)
t_n = H_OSC * np.arange(51)  # the times 0, 0.2, ..., 10 of the 51 points
fig, (whole, zoom) = plt.subplots(1, 2, figsize=(10.0, 5.2))
```

400 angles from 0 to $2\pi$ will give the exact circle $x = \cos t$, $v = -\sin t$. `t_n` holds the 51 times $t_n = 0.2\, n$ of the computed points. The figure has two panels side by side: `whole` (left) for the whole portrait and `zoom` (right) for a close-up.

```python
for name in METHODS:  # left panel: the whole portrait of each method
    whole.plot(portraits[name][:, 0], portraits[name][:, 1], color=COLORS[name],
               marker=MARKERS[name], ms=3, lw=0.9,
               label=f"{LABELS[name]}, $h = 0.2$, 50 steps")
for name in ("midpoint", "rk4"):  # right panel: the last three points only
    zoom.plot(portraits[name][48:, 0], portraits[name][48:, 1], ls="none",
              color=COLORS[name], marker=MARKERS[name], ms=8, label=LABELS[name])
```

`[:, 0]` is the first column of the array (all the positions) and `[:, 1]` the second (all the velocities). The left panel draws each method's whole path, points joined by lines. The right panel draws only the rows from position 48 on (`[48:, 0]`), the last three points at $t = 9.6$, $9.8$ and $10$, of the midpoint method and RK4, as large markers without lines (`ls="none"`); Euler's points are far outside the window of this panel.

```python
for ax in (whole, zoom):  # the exact circle, dashed, drawn on top (zorder 5)
    ax.plot(np.cos(angle), -np.sin(angle), "--", color=COLORS["exact"], lw=0.9,
            zorder=5, label="exact circle $x^2 + v^2 = 1$")
    ax.set_aspect("equal")
    ax.set_xlabel("position $x$")
    ax.set_ylabel("velocity $v$")
whole.plot([1.0], [0.0], "o", color=COLORS["exact"], ms=6, zorder=6)  # the start
zoom.plot(np.cos(t_n[48:]), -np.sin(t_n[48:]), "x", color=COLORS["exact"], ms=9,
          zorder=6, label="exact solution, same times")
```

In both panels the exact circle is drawn as a thin dashed black line. `zorder=5` puts it on top of the coloured paths (a drawing with a larger `zorder` covers one with a smaller), so it stays visible where the RK4 path lies on it. `set_aspect("equal")` makes one unit equally long on both axes, so that the circle looks round. The black dot marks the start; in the right panel black crosses mark the exact solution $(\cos t_n, -\sin t_n)$ at the same three times.

```python
zoom.set_xlim(-1.12, -0.74)  # a window round the points at t = 9.6, 9.8 and 10
zoom.set_ylim(0.12, 0.66)
whole.set_title("Phase portrait of $d^2x/dt^2 = -x$ up to $t = 10$")
zoom.set_title("Zoom: the points at $t = 9.6$, $9.8$, $10$")
whole.legend(loc="lower left", fontsize=8)
zoom.legend(loc="upper left", fontsize=8)
save_figure(fig, "phase_portrait",
            "Phase portrait of the oscillator $d^2x/dt^2 = -x$ started at $x = 1$, "
            ...)
```

The right panel shows only the window $-1.12 \le x \le -0.74$, $0.12 \le v \le 0.66$ around the last three points. Titles, legends, and the figure is saved as `02a_6_phase_portrait.png`. **What Figure 02a.6 shows:** on the left, Euler's path spirals outwards (each step multiplies the energy by $1.04$), while the midpoint and RK4 paths stay close to the dashed circle; on this scale they are hard to tell apart, because the midpoint radius grows only to $\sqrt{1.0004^{50}} = 1.010$. The zoom on the right separates them: the RK4 circles sit on the exact crosses, while the midpoint triangles have run ahead along the circle and lie slightly outside it.

```python
for name in METHODS:
    energy = 0.5 * (portraits[name][:, 0] ** 2 + portraits[name][:, 1] ** 2)
    factor = float(ENERGY_FACTOR[name].subs(hs, sp.Rational(1, 5)))  # at h = 0.2
    predicted = 0.5 * factor ** np.arange(51)  # E_0 times the factor n times
    report(f"energy after 50 steps, {LABELS[name]}", f"{energy[-1]:.10f}")
    check(np.max(np.abs(energy / predicted - 1)) < 1e-13,
          f"{LABELS[name]}: E_n = E_0 times the exact factor to the power n")
```

For each method the energy $E = (x^2 + v^2)/2$ is computed at all 51 points; the exact per-step factor of In [4] is evaluated at $h = 1/5$, and the prediction is $E_n = \frac12 q^n$ for $n = 0, \dots, 50$. The energies after 50 steps are 3.5533416731 (Euler), 0.5100986302 (midpoint) and 0.4999778894 (RK4); the checks require every computed energy to equal its prediction to a relative $10^{-13}$, and they pass: the energy drift of each method is exactly the one derived in Section 2.7.

```python
angle_agrees = []
for name in METHODS:
    x_end, v_end = portraits[name][-1]  # the point at t = 10
    # the clockwise angle from the exact point e^(-10 i) to the computed one
    ahead = -np.angle(complex(x_end, v_end) * np.exp(10j))
```

The last part measures the angle error that the zoom shows. The **argument** $\arg w$ of a complex number $w$ is its angle: the angle between the positive real axis and the arrow from 0 to $w$, counted anticlockwise; `np.angle` computes it, as a number between $-\pi$ and $\pi$. Write the computed point at $t = 10$ as $w = x + i v$ (`complex(x_end, v_end)`; `[-1]` is the last row). The exact solution is $x = \cos t$, $v = -\sin t$, that is $w = \cos t - i \sin t = e^{-it}$, so the exact point at $t = 10$ is $e^{-10i}$. In Python `10j` is the imaginary number $10i$, and `np.exp(10j)` is $e^{10i}$. Multiplying $w$ by $e^{10i}$ turns it back by the exact angle, so the argument of the product is the angle from the exact point to the computed one, counted anticlockwise; the minus sign counts it clockwise, the direction in which the point runs. So `ahead` is positive when the computed point has run ahead of the exact one and negative when it lags behind.

```python
    R_ih = complex(R[name].subs(z, sp.I * sp.Rational(1, 5)))  # R(ih), h = 0.2
    predicted_ahead = 50 * (np.angle(R_ih) - 0.2)  # 50 (arg R(ih) - h)
```

The prediction. `R[name]` is the amplification factor of In [4], a polynomial in `z`; `.subs(z, sp.I * sp.Rational(1, 5))` puts in $z = ih$ with $h = 1/5$ (`sp.I` is sympy's $i$), and `complex(...)` turns the exact sympy number into an ordinary complex number. One step multiplies $w$ by $R(-ih)$ (Section 2.7). Its argument is $-\arg R(ih)$, because $R(-ih)$ is the complex conjugate of $R(ih)$ (the coefficients of $R$ are real) and conjugation reflects a point in the real axis, which reverses its angle. The exact factor $e^{-ih}$ has the argument $-h$. The arguments of a product add up, so after 50 steps the computed point has turned by $-50 \arg R(ih)$ and the exact one by $-50 h$; the computed point is ahead, clockwise, by $50\,(\arg R(ih) - h)$.

```python
    report(f"t = 10, {LABELS[name]}: radius, angle ahead of the exact point",
           f"{math.hypot(x_end, v_end):.4f}, {ahead:+.3e} rad")
    angle_agrees.append(abs(ahead - predicted_ahead) < 1e-12)
check(all(angle_agrees),
      "at t = 10 each point is ahead of the exact one by 50 (arg R(ih) - h)")
```

`math.hypot(x_end, v_end)` is the radius $\sqrt{x^2 + v^2}$ of the end point. The three RESULT lines give the radius and the angle ahead: Euler 2.6658 and $-1.302 \times 10^{-1}$ rad (it lags behind by 0.13 rad); midpoint 1.0100 and $+6.586 \times 10^{-2}$ rad (ahead by 0.066 rad, the shift seen in the zoom); RK4 1.0000 and $-1.314 \times 10^{-4}$ rad (COMPUTED). The RK4 value agrees with the lag of $\omega^5/120$ per step derived in Section 2.24: $50 \cdot 0.2^5/120 = 1.33 \times 10^{-4}$ to leading order. The check requires each measured angle to equal its prediction within $10^{-12}$, and it passes.

**In [13], the energy over a long time.**

```python
long_runs = {name: np.array(solve(step, oscillator, Y0, 100.0, 500)[1])
             for name, step in METHODS.items()}
fig, ax = plt.subplots()
t_long = np.linspace(0.0, 100.0, 501)
drift = {}
for name in METHODS:
    energy = 0.5 * (long_runs[name][:, 0] ** 2 + long_runs[name][:, 1] ** 2)
    drift[name] = np.abs(energy / 0.5 - 1.0)
    ax.semilogy(t_long[1:], drift[name][1:], color=COLORS[name], lw=1.4,
                label=LABELS[name])
```

Now 500 steps of $h = 0.2$, up to $t = 100$. For each method the relative energy error $|E_n/E_0 - 1|$ (with $E_0 = 0.5$) is drawn on a logarithmic vertical axis against the 500 times after the start.

```python
ax.set_xlabel("time $t$ (arbitrary units)")
ax.set_ylabel("relative energy error $|E_n/E_0 - 1|$")
ax.set_title("Energy drift of the oscillator, step $h = 0.2$")
ax.legend()
save_figure(fig, "energy_drift",
            "The relative error of the oscillator energy, $|E_n/E_0 - 1|$, on a "
            ...)
report("energy errors at t = 100 (Euler, midpoint, RK4)",
       ", ".join(f"{drift[name][-1]:.3e}" for name in METHODS))
check(drift["euler"][-1] > 1e8 and 0.1 < drift["midpoint"][-1] < 0.3
      and drift["rk4"][-1] < 5e-4,
      "after 500 steps: Euler energy off by > 1e8, midpoint by 10-30 %, RK4 < 5e-4")
```

Labels, title, legend and the saved figure `02a_7_energy_drift.png`. `", ".join(...)` writes the three final errors separated by commas: $3.286 \times 10^{8}$ (Euler: $1.04^{500} - 1$), $0.2214$ (midpoint: $1.0004^{500} - 1$) and $4.421 \times 10^{-4}$ (RK4: $1 - 0.99999911^{500}$). The check confirms these sizes. **What Figure 02a.7 shows:** the Euler curve is a straight rising line (the same factor at every step makes a straight line on a logarithmic axis); the midpoint and RK4 curves bend over, because their factors are so close to 1 that $q^n - 1 \approx n(q - 1)$ grows only in proportion to $n$; the three methods differ by many powers of ten.

**In [14], Richardson's rule.**

```python
N_R = [2 ** k for k in range(1, 8)]  # the coarse runs: 2 ... 128 steps
coarse = np.array([solve(rk4_step, decay, 1.0, 1.0, n)[1][-1] for n in N_R])
fine = np.array([solve(rk4_step, decay, 1.0, 1.0, 2 * n)[1][-1] for n in N_R])
estimated = (coarse - fine) / 15.0  # Richardson's estimate of the error of fine
actual = fine - EXACT_A  # the true error of fine (we know the exact answer here)
extrapolated = (16.0 * fine - coarse) / 15.0
```

For $N = 2, 4, \dots, 128$ the cell runs RK4 with $N$ steps (`coarse`, the value $Y_h$) and with $2N$ steps (`fine`, the value $Y_{h/2}$). `estimated` is Richardson's estimate $(Y_h - Y_{h/2})/15$ of the error of the finer run, `actual` its true error, and `extrapolated` the value $(16 Y_{h/2} - Y_h)/15$ of Section 2.6.

```python
for n, e_est, e_act, e_ext in zip(N_R, estimated, actual, extrapolated - EXACT_A):
    say(f"N = {n:3d} -> {2 * n:3d}: estimated {e_est: .3e}, actual {e_act: .3e}, "
        f"extrapolated error {e_ext: .2e}")
```

`zip` walks through four sequences together. Each line prints the estimate, the true error and the error of the extrapolated value (the blank in `{e_est: .3e}` leaves room for a minus sign). From $N = 8$ on, the estimate agrees with the true error to within 6 per cent, and the extrapolated value is between 17 and 260 times more accurate than the finer run (COMPUTED).

```python
fig, ax = plt.subplots(figsize=(6.0, 5.4))
ax.loglog(np.abs(actual), np.abs(estimated), "o", color=COLORS["rk4"], ms=6,
          label="RK4 runs with $2N = 4$ to $256$ steps")
for n, x_value, y_value in zip(N_R, np.abs(actual), np.abs(estimated)):
    ax.annotate(f"$N = {n}$", (x_value, y_value), textcoords="offset points",
                xytext=(6, -10), fontsize=7)
diagonal = np.array([1e-14, 1e-4])
ax.loglog(diagonal, diagonal, "--", color=COLORS["guide"], lw=0.9,
          label="estimate = actual")
```

Each run becomes one point (true error, estimate) on logarithmic axes; `ax.annotate` writes its $N$ next to it, shifted by 6 points to the right and 10 points down. The dashed diagonal is the line on which estimate and true error are equal.

```python
ax.set_xlabel("actual error of the finer run")
ax.set_ylabel("Richardson estimate $(Y_h - Y_{h/2})/15$")
ax.set_title("Richardson's estimate against the true error")
ax.legend(loc="upper left")
save_figure(fig, "richardson",
            "Richardson's error estimate $(Y_h - Y_{h/2})/15$ of RK4 for problem A "
            ...)
ratio = estimated[2:] / actual[2:]
check(np.all((ratio > 0.9) & (ratio < 1.1)),
      "Richardson's estimate is within 10 % of the actual error for N >= 8")
check(np.all(np.abs(extrapolated[2:6] - EXACT_A) < np.abs(actual[2:6]) / 10),
      "the extrapolated value is more than 10 times more accurate (N = 8 to 64)")
```

Labels, legend and the saved figure `02a_8_richardson.png`. `ratio` is the estimate divided by the true error for $N \ge 8$ (positions 2 and later); `&` combines two arrays of truth values entry by entry, and `np.all` requires every entry to be true: all ratios lie between 0.9 and 1.1. The second check requires the extrapolated values for $N = 8$ to 64 to be more than ten times more accurate than the finer runs. **What Figure 02a.8 shows:** the points lie on the diagonal: Richardson's estimate, made without the exact answer, is the error itself once the coarse run has at least 8 steps; for $N = 2$ and 4 the error is not yet close to $C h^4$ and the estimate is off by up to 25 per cent.

**In [15], the last check.**

```python
names = ["scale_factors", "scale_factor_product", "convergence_loglog",
         "error_ratios", "rounding_floor", "phase_portrait", "energy_drift",
         "richardson"]
present = [output_file(f"{FIGURE_FOLDER}/02a_{k}_{name}.png").is_file()
           for k, name in enumerate(names, 1)]
check(all(present), f"all {len(names)} figure files of notebook 02a exist")
all_checks_passed()
```

`enumerate(names, 1)` numbers the eight figure names from 1. For each, the cell asks whether the file `02a_<k>_<name>.png` exists; the check requires all eight to exist, and `all_checks_passed()` prints the last line, ALL 29 CHECKS PASSED (notebook 02a). The 29 checks are: 3 in In [3], 4 in In [4], 2 in In [5], 3 in In [6], 2 in In [7], 1 in In [8], 1 in In [9], 3 in In [10], 2 in In [11], 4 in In [12], 1 in In [13], 2 in In [14] and 1 in In [15].

### 2.12 Boundary-value problems and the shooting method

**Conditions at both ends.** So far every condition was given at the start: $y(0)$, or $x(0)$ and $x'(0)$. Many problems give one condition at each END of an interval instead. Such a problem is a **boundary-value problem**. Often it contains a number that is not known in advance, and it has a solution that is not zero everywhere only for special values of that number: these values are the **eigenvalues** and the solutions the **eigenfunctions**. The energy levels of quantum mechanics, and the Kohn-Sham levels of this book, are eigenvalues of this kind.

**The vibrating string.** The simplest example is

$$
u''(x) = -\lambda\, u(x), \qquad u(0) = 0, \qquad u(1) = 0,
$$

the shape $u(x)$ of a string fixed at $x = 0$ and $x = 1$ that vibrates in one of its natural modes; $\lambda$ is the unknown number. For $\lambda > 0$ every solution of the equation has the form

$$
u(x) = A \sin(\sqrt{\lambda}\, x) + B \cos(\sqrt{\lambda}\, x)
$$

with two constants $A$ and $B$. (Differentiating twice brings each term back multiplied by $-\lambda$: the derivative of $\sin(c x)$ is $c \cos(c x)$ and that of $\cos(c x)$ is $-c \sin(c x)$, with $c = \sqrt{\lambda}$ and $c^2 = \lambda$. That these are ALL the solutions follows from the uniqueness theorem of Section 2.2, because $A$ and $B$ can match any starting values $u(0)$, $u'(0)$.)

$$
u(0) = A \sin 0 + B \cos 0 = B
$$

($\sin 0 = 0$ and $\cos 0 = 1$), so the left condition $u(0) = 0$ forces $B = 0$. A multiple of a solution is again a solution, so we may fix the size by choosing the starting slope $u'(0) = 1$:

$$
u'(0) = A \sqrt{\lambda} \cos 0 = A\sqrt{\lambda} = 1, \qquad A = \frac{1}{\sqrt{\lambda}}
$$

(the derivative of $A \sin(\sqrt{\lambda}\, x)$ at $x = 0$). So the solution that starts with $u(0) = 0$ and $u'(0) = 1$ is

$$
u(x; \lambda) = \frac{\sin(\sqrt{\lambda}\, x)}{\sqrt{\lambda}} .
$$

The right condition $u(1) = 0$ holds when $\sin\sqrt{\lambda} = 0$, that is when $\sqrt{\lambda}$ is a whole multiple of $\pi$:

$$
\sqrt{\lambda} = n\pi, \qquad \lambda_n = n^2 \pi^2, \qquad n = 1, 2, 3, \dots
$$

(the zeros of the sine are the whole multiples of $\pi$; $n = 0$ gives $\lambda = 0$, where the solution is $u = x$, which is not zero at $x = 1$). So the eigenvalues of the string are $\pi^2 = 9.8696$, $4\pi^2 = 39.478$, $9\pi^2 = 88.826$, ... (PROVED).

**The shooting method.** The computer does not know this formula. It turns the boundary-value problem into a sequence of initial-value problems, like aiming a cannon:

1. guess a value of $\lambda$;
2. solve the initial-value problem from the left end with the conditions there ($u(0) = 0$, $u'(0) = 1$), for example with RK4;
3. see where the "shot" lands at the right end: the **mismatch** $F(\lambda) = u(1; \lambda)$;
4. change the guess until the mismatch is zero.

The function $F(\lambda)$ is the **shooting function**, and the eigenvalues are its zeros. For the string we know it exactly, $F(\lambda) = \sin\sqrt{\lambda}/\sqrt{\lambda}$, which lets Notebook 02b check every shot.

**Brackets.** Two guesses $\lambda_{\rm lo}$ and $\lambda_{\rm hi}$ at which $F$ has opposite signs form a **bracket**. If $F$ is continuous, it has a zero between them: this is the **intermediate value theorem** of calculus (ASSUMED: quoted without proof). For the string $F(5) = 0.35184 > 0$ and $F(15) = -0.17245 < 0$, so $5 < \lambda < 15$ brackets an eigenvalue (it is $\pi^2$).

**Bisection.** Take the midpoint $m = (\lambda_{\rm lo} + \lambda_{\rm hi})/2$ of the bracket and evaluate $F(m)$. If $F(m)$ has the same sign as $F(\lambda_{\rm lo})$, the zero lies in the right half and $m$ becomes the new $\lambda_{\rm lo}$; otherwise it lies in the left half and $m$ becomes the new $\lambda_{\rm hi}$. Each step halves the bracket, so after $k$ steps its width is

$$
w_k = \frac{\lambda_{\rm hi} - \lambda_{\rm lo}}{2^k}
$$

(the starting width halved $k$ times). Bisection always works, but slowly: it gains one binary digit (a factor 2) per step; starting from the width 10, after 45 steps the width is $10/2^{45} = 2.8 \times 10^{-13}$. *Worked example.* From the bracket $(5, 15)$: $m = 10$, and $F(10) = \sin(3.1623)/3.1623 = -0.00654 < 0$ (because $\sqrt{10} = 3.1623$ is a little larger than $\pi$, where the sine turns negative), the opposite sign of $F(5)$, so the new bracket is $(5, 10)$; then $m = 7.5$ with $F > 0$, bracket $(7.5, 10)$; then $8.75$, $9.375$, $9.6875$, $9.84375$, ... (Notebook 02b, In [5], prints these midpoints and the signs of $F$).

**The secant rule.** Draw the straight line through the last two points $(x_0, F(x_0))$ and $(x_1, F(x_1))$ and take its zero as the next guess $x_2$. The line is

$$
\ell(x) = F(x_1) + \frac{F(x_1) - F(x_0)}{x_1 - x_0}\,(x - x_1)
$$

(the line through $(x_1, F(x_1))$ with the slope of the chord between the two points). Setting $\ell(x_2) = 0$:

$$
\frac{F(x_1) - F(x_0)}{x_1 - x_0}\,(x_2 - x_1) = -F(x_1)
$$

(subtract $F(x_1)$ from both sides);

$$
x_2 = x_1 - F(x_1)\, \frac{x_1 - x_0}{F(x_1) - F(x_0)}
$$

(divide by the slope and add $x_1$). Then repeat with the two newest points. *Worked example.* With $x_0 = 5$, $x_1 = 15$, $F(5) = 0.35184$, $F(15) = -0.17245$:

$$
x_2 = 15 - (-0.17245) \cdot \frac{15 - 5}{-0.17245 - 0.35184} = 15 - \frac{1.7245}{0.52429} = 15 - 3.2892 = 11.7108
$$

(the secant formula with these numbers). Notebook 02b prints $11.7107898$. Close to a zero, the number of correct digits of the secant rule is multiplied by about $1.618$ at every step (the golden ratio; ASSUMED: a standard result of numerical analysis, quoted without proof and only illustrated by the notebook), much faster than the one binary digit per step of bisection. Unlike bisection, the secant rule does not keep the root bracketed and can fail when the line is nearly flat; Section 2.24 shows how the Revision solver combines a fast rule with the safety of bisection.

### 2.13 The finite square well of quantum mechanics

**The equation.** In quantum mechanics the allowed energies $E$ of a particle in one dimension, moving in a **potential** $V(x)$ (its potential energy at the position $x$), are the eigenvalues of the **Schrödinger equation**; in units in which Planck's constant divided by $2\pi$ (written $\hbar$) and the mass $m$ are both 1, it reads

$$
-\frac12\, u''(x) + V(x)\, u(x) = E\, u(x) .
$$

We take this equation as given (ASSUMED here: it is the basic equation of quantum mechanics, used in this chapter only as an example of an eigenvalue problem). The function $u$ is the **wave function**: $u(x)^2$ is the probability density of finding the particle at $x$, so $u$ is **normalised**, $\int u^2\, dx = 1$. Multiplying the equation by $-2$ gives

$$
u'' - 2V u = -2E u
$$

(each term multiplied by $-2$), and adding $2Vu$ to both sides

$$
u'' = 2\,(V(x) - E)\, u .
$$

**The well.** We take $V(x) = -V_0$ inside $|x| < a$ and $V(x) = 0$ outside, with the depth $V_0 = 15$ and the half-width $a = 1$. A **bound state** is a solution with $-V_0 < E < 0$ that decays to zero far away on both sides; its energy is an eigenvalue. Write

$$
k = \sqrt{2(E + V_0)}, \qquad \kappa = \sqrt{-2E}
$$

(both are real and positive for $-V_0 < E < 0$).

*Outside the well* ($V = 0$): $u'' = -2E u = \kappa^2 u$, solved by $e^{\kappa x}$ and $e^{-\kappa x}$ (differentiating twice brings back the factor $\kappa^2$). For $x < -a$ only $e^{\kappa x}$ goes to zero as $x \to -\infty$, so the solution on the left is a multiple of $e^{\kappa(x + a)}$; we choose the multiple 1. At $x = -a$ this gives the starting values

$$
u(-a) = 1, \qquad u'(-a) = \kappa
$$

(the value and the derivative of $e^{\kappa(x + a)}$ at $x = -a$, where the exponent is 0). So, unlike the string, here we know exactly how to start the shot.

*Inside the well* ($V = -V_0$): $u'' = 2(-V_0 - E) u = -k^2 u$, solved by $\cos(k x)$ and $\sin(k x)$.

*The solution inside that continues the left tail* is

$$
u(x) = \cos\big(k(x + a)\big) + \frac{\kappa}{k} \sin\big(k(x + a)\big),
$$

because at $x = -a$ it gives $u = \cos 0 + 0 = 1$ and $u' = -k \sin 0 + \kappa \cos 0 = \kappa$ (derivative term by term), the starting values above, and it solves $u'' = -k^2 u$.

*Symmetry.* The well is symmetric, $V(-x) = V(x)$. If $u(x)$ solves the equation, so does $u(-x)$ (the second derivative does not notice the change of sign of $x$, by the chain rule applied twice), and a bound-state energy of a one-dimensional problem belongs to only one wave function up to a factor (ASSUMED: a standard fact of one-dimensional quantum mechanics, quoted without proof). So $u(-x) = c\, u(x)$, and applying this twice gives $c^2 = 1$: every bound state is **even**, $u(-x) = u(x)$, or **odd**, $u(-x) = -u(x)$. An even smooth function has $u'(0) = 0$ (its graph is flat at the centre) and an odd one has $u(0) = 0$. These are the conditions at the far end of the shot from $x = -a$ to $x = 0$:

$$
F_{\rm even}(E) = u'(0), \qquad F_{\rm odd}(E) = u(0) .
$$

**The exact conditions.** At $x = 0$ the inside solution gives

$$
u(0) = \cos(ka) + \frac{\kappa}{k}\sin(ka), \qquad u'(0) = -k \sin(ka) + \kappa \cos(ka)
$$

(insert $x = 0$ into $u$ and into its derivative). The even condition $u'(0) = 0$ becomes

$$
\kappa \cos(ka) = k \sin(ka), \qquad k \tan(ka) = \kappa
$$

(move the sine term to the other side; then divide by $\cos(ka)$, using $\tan = \sin/\cos$). The odd condition $u(0) = 0$ becomes

$$
\cos(ka) = -\frac{\kappa}{k}\sin(ka), \qquad -k \cot(ka) = \kappa
$$

(move the sine term; then multiply by $k$ and divide by $\sin(ka)$, using $\cot = \cos/\sin$). Now put $z = ka$ and $z_0 = a\sqrt{2V_0}$:

$$
z^2 + (\kappa a)^2 = 2(E + V_0)a^2 - 2E a^2 = 2V_0 a^2 = z_0^2
$$

(insert $k^2 = 2(E + V_0)$ and $\kappa^2 = -2E$; the terms with $E$ cancel), so $\kappa a = \sqrt{z_0^2 - z^2}$. Multiplying the even and the odd condition by $a$ and dividing by $z = ka$:

$$
\text{even: } \tan z = \frac{\sqrt{z_0^2 - z^2}}{z}, \qquad \text{odd: } -\cot z = \frac{\sqrt{z_0^2 - z^2}}{z}, \qquad E = \frac{z^2}{2a^2} - V_0
$$

(the last relation is $k^2 = 2(E + V_0)$ solved for $E$, with $k = z/a$). These are **transcendental equations**: no formula gives $z$, but a computer solves them to any number of digits. Here $z_0 = \sqrt{30} = 5.477$. The right side $\sqrt{z_0^2 - z^2}/z$ falls from $+\infty$ at $z = 0$ to 0 at $z = z_0$; on each interval of length $\pi/2$ one of the branches of $\tan z$ (on $(0, \pi/2)$, $(\pi, 3\pi/2)$, ...) or of $-\cot z$ (on $(\pi/2, \pi)$, ...) rises from 0 to $+\infty$ and crosses it exactly once. So the well has one bound state for every interval of length $\pi/2$ that begins below $z_0$: since $z_0/(\pi/2) = 3.487$, there are exactly 4 bound states, even, odd, even, odd. Their energies, computed with 30 digits by Notebook 02b (In [6]), are

$$
E_0 = -14.1206, \quad E_1 = -11.5181, \quad E_2 = -7.3330, \quad E_3 = -2.0437
$$

(COMPUTED from the exact equations).

**Why shots miss.** For an energy that is NOT an eigenvalue, the shot that starts with the decaying left tail arrives on the right side of the well as a mixture of $e^{-\kappa x}$ and the growing $e^{+\kappa x}$; the growing part takes over and the shot flies off to $+\infty$ or $-\infty$. Only at an eigenvalue is the growing part exactly absent. Just below and just above an eigenvalue the shot flies off to OPPOSITE infinities, which is what makes the shooting function change sign there (Figure 02b.6 shows it).

**Normalisation and orthogonality.** The tail on the left contributes to $\int u^2\,dx$ the amount

$$
\int_{-\infty}^{-a} e^{2\kappa(x + a)}\, dx = \Big[\frac{e^{2\kappa(x + a)}}{2\kappa}\Big]_{-\infty}^{-a} = \frac{1}{2\kappa} - 0 = \frac{1}{2\kappa}
$$

(an antiderivative of $e^{c x}$ is $e^{c x}/c$; at $x = -a$ the exponential is $e^0 = 1$, and at $-\infty$ it is 0). Two wave functions $u_m$, $u_n$ are **orthogonal** when $\int u_m u_n\, dx = 0$. For an even and an odd state the product $p(x) = u_m(x) u_n(x)$ is odd, $p(-x) = -p(x)$, and the integral of an odd function over the whole line is zero:

$$
\int_{-\infty}^{\infty} p(x)\, dx = \int_{-\infty}^{0} p(x)\, dx + \int_{0}^{\infty} p(x)\, dx = -\int_{0}^{\infty} p(s)\, ds + \int_{0}^{\infty} p(x)\, dx = 0
$$

(split at 0; in the first integral substitute $x = -s$, which turns $dx$ into $-ds$, reverses the limits and turns $p(x)$ into $p(-s) = -p(s)$). Two states of the same parity with different energies are also orthogonal (ASSUMED here: a theorem of quantum mechanics, which Notebook 02b confirms numerically).

**Simpson's rule.** To integrate a function given at equally spaced points $x_0, x_1, \dots, x_n$ (with $n$ even and spacing $h$), Simpson's rule passes a parabola through every three neighbouring points and integrates it exactly. For three points at $-h$, $0$, $h$ with the values $f_-, f_0, f_+$, write the parabola as $p(x) = \alpha + \beta x + \gamma x^2$:

$$
f_- = \alpha - \beta h + \gamma h^2, \qquad f_0 = \alpha, \qquad f_+ = \alpha + \beta h + \gamma h^2
$$

(the parabola takes the three values);

$$
\gamma h^2 = \frac{f_- + f_+}{2} - f_0
$$

(add the first and the third equation, $f_- + f_+ = 2\alpha + 2\gamma h^2$, then use $\alpha = f_0$);

$$
\int_{-h}^{h} p(x)\, dx = 2\alpha h + \frac{2\gamma h^3}{3}
$$

(integrate term by term; the odd term $\beta x$ gives zero);

$$
\int_{-h}^{h} p(x)\, dx = 2 f_0 h + \frac{2h}{3}\Big(\frac{f_- + f_+}{2} - f_0\Big) = \frac{h}{3}\big(f_- + 4 f_0 + f_+\big)
$$

(insert $\alpha$ and $\gamma h^2$; collect: $2h - \frac{2h}{3} = \frac{4h}{3}$). Adding these pieces over the pairs of intervals gives Simpson's rule

$$
\int_{x_0}^{x_n} f\, dx \approx \frac{h}{3}\big(f_0 + 4 f_1 + 2 f_2 + 4 f_3 + \dots + 2 f_{n-2} + 4 f_{n-1} + f_n\big)
$$

(every inner point with an even index belongs to two pieces and gets $1 + 1 = 2$). Its error is proportional to $h^4$ (ASSUMED: a standard result, quoted without proof), the same order as RK4.

**The connection to this book.** The Kohn-Sham equations of the book are solved in the same way. Two first-order equations along the hidden coordinate are shot from the tip of an interval to its other end, the brane, where, because of a mirror symmetry of the model that the Revision record labels ASSUMED, an even or an odd condition must hold, exactly like $u'(0) = 0$ or $u(0) = 0$ here (Section 2.24).

### 2.14 Example: shooting a string and a quantum well

Notebook 02b carries out Sections 2.12 and 2.13. Part A shoots the string with RK4 (200 steps), draws three shots and the whole shooting function, and finds $\lambda_1 = \pi^2$ both by bisection and by the secant rule, comparing how fast they converge. Part B solves the exact well equations with mpmath at 30 digits, shoots the well with RK4 from $x = -a$ with the even and the odd condition at the centre, refines all four levels at once by bisection, shows how a shot misses, draws the four normalised wave functions, checks their nodes, normalisation and orthogonality (for states of different parity also numerically), and measures the order 4 of the computed energies. It ends with ALL 16 CHECKS PASSED (notebook 02b).

<!-- NOTEBOOK 02b -->

### 2.17 Line-by-line walk-through of Notebook 02b

The notebook has twelve code cells, In [1] to In [12]. As in Section 2.11, a quoted line `...)` stands for the rest of a figure caption, which Section 2.16 prints in full under its figure.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 2.15. Its code is, line for line, the set-up code of Notebook 02a explained in Section 2.11, with the single difference `NOTEBOOK_ID = "02b"`, so that the figures are named `02b_<k>_<name>.png` and the captions file is `Revision/textbook/figures/02b.captions.json`. It prints one line, Set-up of notebook 02b complete: repository folder found, helpers defined.

**In [2], RK4 for systems, bisection and the secant rule.**

```python
import math  # sqrt, sin, pi for single numbers

import mpmath  # numbers with as many digits as we ask for
import numpy as np  # arrays (vectors) of numbers
```

`math` for single numbers, mpmath for numbers with as many digits as we ask for (used for the exact well levels), numpy for arrays.

```python
# Colours that colour-blind readers can tell apart; curves also differ by style.
BLUE, ORANGE, AQUA, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7"
GREY, BLACK = "#8a8986", "#000000"
LEVEL_COLORS = [BLUE, ORANGE, AQUA, VIOLET]  # one colour per bound state
```

Six colour names, given their hexadecimal codes at once (Python assigns the values on the right to the names on the left in order), and a list of four colours, one for each bound state of the well.

```python
def rk4_step(f, x, Y, h):
    """One classical RK4 step for the system Y' = f(x, Y)."""
    k1 = f(x, Y)
    k2 = f(x + h / 2, Y + (h / 2) * k1)
    k3 = f(x + h / 2, Y + (h / 2) * k2)
    k4 = f(x + h, Y + h * k3)
    return Y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
```

The RK4 rule of Section 2.4, now with the variable called $x$ (a position) and the state `Y` a numpy array $(u, u')$; since numpy adds and multiplies arrays entry by entry, the formulas act on both components at once.

```python
def bisection(F, lo, hi, steps):
    """steps bisection steps on the bracket (lo, hi); the list of midpoints."""
    f_lo = F(lo)
    guesses = []
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        f_mid = F(mid)
        guesses.append(mid)
        if (f_mid > 0) == (f_lo > 0):  # same sign as at lo: the root is right
            lo, f_lo = mid, f_mid
        else:  # opposite sign: the root lies between lo and mid
            hi = mid
    return guesses
```

Bisection as in Section 2.12. `f_lo` is the value of $F$ at the left end. Each of the `steps` passes (the loop variable `_` is not used) computes the midpoint and $F$ there and records the midpoint. `(f_mid > 0) == (f_lo > 0)` is true when both values have the same sign (both positive or both not positive): then the zero lies to the right of `mid`, which becomes the new left end (with its value); otherwise `mid` becomes the new right end. The function returns all the midpoints, so that their errors can be drawn.

```python
def secant(F, x0, x1, steps):
    """steps secant steps from the guesses x0, x1; the list of new guesses."""
    f0, f1 = F(x0), F(x1)
    guesses = []
    for _ in range(steps):
        if f1 == f0:  # the line is flat: no new information (converged)
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)  # the zero of the line
        x0, f0, x1, f1 = x1, f1, x2, F(x2)
        guesses.append(x2)
    return guesses


say("RK4 for systems, bisection and the secant rule are defined.")
```

The secant rule of Section 2.12. If the two last values of $F$ are equal the line is flat and has no zero; this happens when both guesses have already reached the root to the last digit, and `break` leaves the loop. Otherwise `x2` is the zero of the line through the last two points; the line `x0, f0, x1, f1 = x1, f1, x2, F(x2)` shifts the pair forward (the old newest point becomes the older one, and the new guess with its value becomes the newest). The cell prints one line.

**In [3], three shots for the string.**

```python
def shoot_string(lam, n):
    """RK4 solution of u'' = -lam u, u(0) = 0, u'(0) = 1 on 0 <= x <= 1 in n
    steps.  Returns the n + 1 positions and the n + 1 values of u."""
    def f(x, Y):
        return np.array([Y[1], -lam * Y[0]])  # (u', v') = (v, -lam u)
    h = 1.0 / n
    Y = np.array([0.0, 1.0])  # u(0) = 0, u'(0) = 1
    xs, us = [0.0], [0.0]
    for i in range(n):
        Y = rk4_step(f, i * h, Y, h)
        xs.append((i + 1) * h)
        us.append(Y[0])
    return np.array(xs), np.array(us)
```

The string equation $u'' = -\lambda u$ as the system $u' = v$, $v' = -\lambda u$: the inner function `f` returns $(v, -\lambda u)$ for the state `Y` $= (u, v)$ (`lam` stands for $\lambda$, because `lambda` is a reserved word of Python). The shot starts with $u = 0$, $u' = 1$ and makes `n` RK4 steps of size $1/n$, recording every position and value of $u$.

```python
def F_string(lam, n=200):
    """The shooting function: where the shot lands, u(1)."""
    return shoot_string(lam, n)[1][-1]
```

The shooting function $F(\lambda) = u(1; \lambda)$: the last value of $u$; `n=200` makes 200 steps the default.

```python
fig, ax = plt.subplots()
for lam, color, style in ((5.0, ORANGE, "--"), (math.pi ** 2, BLUE, "-"),
                          (15.0, AQUA, "-.")):
    xs, us = shoot_string(lam, 200)
    ax.plot(xs, us, style, color=color, lw=1.6,
            label=f"$\\lambda = {lam:.4f}$: $u(1) = {us[-1]:+.4f}$")
    ax.plot([1.0], [us[-1]], "o", color=color, ms=6)
```

Three shots, with $\lambda = 5$ (dashed orange), $\lambda = \pi^2$ (solid blue) and $\lambda = 15$ (dash-dotted aqua); each is drawn with its landing value $u(1)$ in the legend (`:+.4f` writes the sign and 4 decimals), and a dot marks where it lands.

```python
ax.axhline(0.0, color=BLACK, lw=0.8)
ax.plot([0.0, 1.0], [0.0, 0.0], "s", color=BLACK, ms=7, label="the two fixed ends")
ax.set_xlabel("position $x$ along the string")
ax.set_ylabel("displacement $u(x)$")
ax.set_title("Three shots for $u'' = -\\lambda u$, $u(0) = 0$, $u'(0) = 1$")
ax.legend(fontsize=8)
save_figure(fig, "trial_solutions_string",
            "Three shots for the string equation $d^2u/dx^2 = -\\lambda u$ started at "
            ...)
check(F_string(5.0) > 0 > F_string(15.0) and abs(F_string(math.pi ** 2)) < 1e-9,
      "u(1) > 0 for lambda = 5, < 0 for lambda = 15, = 0 for lambda = pi^2")
```

The horizontal axis line, two black squares at the fixed ends, labels, the legend and the saved figure `02b_1_trial_solutions_string.png`. The check confirms the picture in numbers: the shot lands above the target for $\lambda = 5$, below it for $\lambda = 15$, and within $10^{-9}$ of it for $\lambda = \pi^2$. **What Figure 02b.1 shows:** a small $\lambda$ bends the string too little (it comes down too late), a large one too much (it crosses zero too early); the eigenvalue $\pi^2$ lands exactly on the target.

**In [4], the whole shooting function.**

```python
lam_points = np.linspace(0.5, 100.0, 60)  # 60 guesses for RK4
lam_fine = np.linspace(0.5, 100.0, 800)  # many points for the exact curve
F_points = np.array([F_string(lam) for lam in lam_points])
F_exact = np.sin(np.sqrt(lam_fine)) / np.sqrt(lam_fine)
```

60 values of $\lambda$ between 0.5 and 100 are shot with RK4; 800 values give a smooth exact curve $\sin\sqrt\lambda/\sqrt\lambda$.

```python
fig, ax = plt.subplots()
ax.plot(lam_fine, F_exact, color=BLACK, lw=1.0,
        label="exact $\\sin\\sqrt{\\lambda}/\\sqrt{\\lambda}$")
ax.plot(lam_points, F_points, "o", color=BLUE, ms=4, label="RK4 shots, 200 steps")
for n in (1, 2, 3):
    ax.axvline(n ** 2 * math.pi ** 2, ls=":", color=GREY, lw=1.0)
    ax.text(n ** 2 * math.pi ** 2, 0.62, f"${n * n}\\pi^2$", ha="center",
            fontsize=9)
```

The exact curve in black, the RK4 values as blue points, and dotted vertical lines (`axvline`) at the first three eigenvalues $n^2\pi^2$, labelled $1\pi^2$, $4\pi^2$, $9\pi^2$ near the top.

```python
ax.axhline(0.0, color=BLACK, lw=0.8)
ax.set_xlabel("guessed eigenvalue $\\lambda$")
ax.set_ylabel("$F(\\lambda) = u(1; \\lambda)$")
ax.set_ylim(-0.3, 0.7)
ax.set_title("The shooting function of the string")
ax.legend()
save_figure(fig, "shooting_function_string",
            "The shooting function $F(\\lambda) = u(1; \\lambda)$ of the string, "
            ...)
```

The zero line, labels, the vertical range and the saved figure `02b_2_shooting_function_string.png`. **What Figure 02b.2 shows:** the RK4 points lie on the exact curve; it crosses zero exactly at the dotted lines, and between two crossings it keeps its sign, so any two guesses with opposite signs of $F$ bracket an eigenvalue.

```python
worst = np.max(np.abs(F_points - np.sin(np.sqrt(lam_points)) /
                      np.sqrt(lam_points)))
report("largest difference RK4 - exact shooting function", f"{worst:.2e}")
check(worst < 1e-7, "the RK4 shooting function equals sin(sqrt(lam))/sqrt(lam)")
```

The largest distance between the 60 RK4 values and the exact formula is $4.54 \times 10^{-8}$ (COMPUTED; it is largest at the biggest $\lambda$, where the solution oscillates fastest), and the check requires it to be below $10^{-7}$.

**In [5], bisection against the secant rule.**

```python
PI2 = math.pi ** 2  # the exact eigenvalue
bis = bisection(F_string, 5.0, 15.0, 45)
sec = secant(F_string, 5.0, 15.0, 12)
say("step   bisection midpoint   F(midpoint)    secant guess")
for k in range(6):
    say(f"{k + 1:4d}   {bis[k]:18.6f}   {F_string(bis[k]):+11.5f}   {sec[k]:13.7f}")
```

45 bisection steps and at most 12 secant steps, both started from 5 and 15. The table prints the first six of each: the bisection midpoints 10, 7.5, 8.75, 9.375, 9.6875, 9.84375 with the signs of $F$ that decided each halving (only the first is negative, so the bracket moves up each time after the first step), and the secant guesses 11.7107898, 8.8043277, 10.0237185, 9.8815597, 9.8694633, 9.8696045 (the first one is the worked example of Section 2.12).

```python
lam_rk4 = sec[-1]  # the converged secant value: the RK4 eigenvalue (200 steps)
report("eigenvalue by RK4 shooting (200 steps)", f"{lam_rk4:.12f}")
report("pi^2", f"{PI2:.12f}")
errors_bis = np.abs(np.array(bis) - lam_rk4)
errors_sec = np.abs(np.array(sec) - lam_rk4)
```

The last secant guess is the zero of the RK4 shooting function, 9.869604411103; it differs from $\pi^2 = 9.869604401089$ by $1.0 \times 10^{-8}$, the error of RK4 with 200 steps (COMPUTED). The errors of all guesses are measured against this zero (not against $\pi^2$), because that is the number the root finders are looking for.

```python
fig, ax = plt.subplots()
ax.semilogy(range(1, len(bis) + 1), np.maximum(errors_bis, 1e-17), "s-",
            color=ORANGE, ms=4, lw=1.2, label="bisection")
ax.semilogy(range(1, len(sec) + 1), np.maximum(errors_sec, 1e-17), "o-",
            color=BLUE, ms=5, lw=1.2, label="secant rule")
k_values = np.arange(1, len(bis) + 1)
ax.semilogy(k_values, 10.0 / 2.0 ** k_values, ":", color=GREY,
            label="bracket width $10/2^k$")
```

The errors after each step on a logarithmic axis; `np.maximum(errors, 1e-17)` replaces an error of exactly 0 (which a logarithmic axis cannot show) by $10^{-17}$. The dotted grey line is the bracket width $10/2^k$ of Section 2.12.

```python
ax.set_xlabel("step $k$")
ax.set_ylabel("error $|\\lambda_k - \\lambda_1|$")
ax.set_ylim(1e-17, 10.0)
ax.set_title("How fast the two root finders approach the eigenvalue $\\lambda_1$")
ax.legend()
save_figure(fig, "bisection_vs_secant",
            "The error of the guess after $k$ steps, $|\\lambda_k - \\lambda_1|$, "
            ...)
```

Labels and the saved figure `02b_3_bisection_vs_secant.png`. **What Figure 02b.3 shows:** the bisection errors follow the dotted halving line, one binary digit per step, and are still about $10^{-13}$ after 45 steps; the secant errors fall faster and faster and reach the rounding level in about 9 steps.

```python
check(bis[:6] == [10.0, 7.5, 8.75, 9.375, 9.6875, 9.84375],
      "the bisection midpoints 10, 7.5, 8.75, 9.375, 9.6875, 9.84375")
check(abs(sec[5] - PI2) < 1e-6 and abs(bis[5] - PI2) > 0.02,
      "after 6 steps: secant within 1e-6 of pi^2, bisection still 0.02 away")
check(abs(lam_rk4 - PI2) < 2e-8 and abs(bis[-1] - lam_rk4) < 1e-11,
      "RK4 eigenvalue = pi^2 within 2e-8; 45 bisections agree within 1e-11")
```

Three checks: the first six midpoints are exactly those of the worked example (these numbers are exact in binary, so `==` is safe); after six steps the secant rule is within $10^{-6}$ of $\pi^2$ while bisection is still more than $0.02$ away; the RK4 eigenvalue is within $2 \times 10^{-8}$ of $\pi^2$ and the 45th bisection midpoint within $10^{-11}$ of it.

**In [6], the exact well levels with mpmath.**

```python
V0, A = 15.0, 1.0  # the depth and the half-width of the well
mpmath.mp.dps = 30  # work with 30 significant digits
Z0 = mpmath.sqrt(2 * mpmath.mpf(V0)) * A  # z0 = a sqrt(2 V0) = sqrt(30)
```

The depth $V_0 = 15$ and the half-width $a = 1$ (called `A` in the code). `mpmath.mp.dps = 30` makes mpmath compute with 30 significant digits; `mpmath.mpf(V0)` turns 15 into an mpmath number, so that $z_0 = \sqrt{30}$ is computed to 30 digits.

```python
def g_even(z):
    return z * mpmath.sin(z) - mpmath.sqrt(Z0 ** 2 - z ** 2) * mpmath.cos(z)


def g_odd(z):
    return z * mpmath.cos(z) + mpmath.sqrt(Z0 ** 2 - z ** 2) * mpmath.sin(z)
```

The even condition $\tan z = \sqrt{z_0^2 - z^2}/z$ multiplied by $z\cos z$ becomes $z \sin z - \sqrt{z_0^2 - z^2}\cos z = 0$, and the odd condition $-\cot z = \sqrt{z_0^2 - z^2}/z$ multiplied by $z \sin z$ becomes $-z\cos z = \sqrt{z_0^2 - z^2} \sin z$, that is $z\cos z + \sqrt{z_0^2 - z^2}\sin z = 0$. These forms have no infinities, which makes them safe for a root finder.

```python
EXACT = []  # (energy, parity) of the bound states, lowest first
for j in range(8):  # the intervals of length pi/2 between 0 and z0
    lo = j * mpmath.pi / 2
    hi = min((j + 1) * mpmath.pi / 2, Z0)
    if lo >= Z0:
        break
    g, parity = (g_even, "even") if j % 2 == 0 else (g_odd, "odd")
    # the root inside the interval (lo, hi), searched a hair away from its ends
    z = mpmath.findroot(g, (lo + mpmath.mpf("1e-20"), hi - mpmath.mpf("1e-20")),
                        solver="anderson")
    EXACT.append((z ** 2 / (2 * A ** 2) - V0, parity, z))
```

The loop walks through the intervals $(j\pi/2, (j+1)\pi/2)$, the last one cut off at $z_0$, and stops (`break`) when an interval starts beyond $z_0$. `j % 2` is the remainder of $j$ divided by 2: on the intervals with even $j$ the even condition has its root, on the others the odd one (Section 2.13). `mpmath.findroot` with the method `"anderson"` (a bracketing root finder) refines the root inside the interval, started a hair ($10^{-20}$) away from its ends; then the energy $E = z^2/(2a^2) - V_0$ is stored with the parity and $z$. Each entry of `EXACT` is a **tuple**, a fixed group of values in round brackets.

```python
for n, (energy, parity, z) in enumerate(EXACT):
    say(f"state {n} ({parity:4}): z = {mpmath.nstr(z, 20)}, "
        f"E = {mpmath.nstr(energy, 20)}")
check(len(EXACT) == 4 and [p for _, p, _ in EXACT] == ["even", "odd", "even", "odd"],
      "the well has 4 bound states: even, odd, even, odd")
```

The four states are printed with 20 significant digits (`mpmath.nstr`): $E_0 = -14.120556743965630861$, $E_1 = -11.518123819661769376$, $E_2 = -7.3330267121044013902$, $E_3 = -2.0436840105252862495$ (COMPUTED). The check confirms that there are 4 and that the parities alternate.

```python
z_axis = np.linspace(0.01, float(Z0), 2000)
rhs = np.sqrt(float(Z0) ** 2 - z_axis ** 2) / z_axis
tan_z = np.tan(z_axis)
cot_z = -1.0 / np.tan(z_axis)
tan_z[np.abs(tan_z) > 12] = np.nan  # do not draw the jumps at the poles
cot_z[np.abs(cot_z) > 12] = np.nan
```

For the graphical solution: 2000 values of $z$ up to $z_0$, the right side $\sqrt{z_0^2 - z^2}/z$, and the two left sides $\tan z$ and $-\cot z$. Where these jump between $+\infty$ and $-\infty$ the plotting line would draw a misleading vertical stroke; the entries larger than 12 in size are therefore set to `np.nan` ("not a number"), which matplotlib leaves out.

```python
fig, ax = plt.subplots()
ax.plot(z_axis, rhs, color=BLACK, lw=1.5, label="$\\sqrt{z_0^2 - z^2}/z$")
ax.plot(z_axis, tan_z, color=BLUE, lw=1.2, label="$\\tan z$ (even states)")
ax.plot(z_axis, cot_z, "--", color=ORANGE, lw=1.2, label="$-\\cot z$ (odd states)")
for n, (energy, parity, z) in enumerate(EXACT):
    zf = float(z)
    ax.plot([zf], [math.sqrt(float(Z0) ** 2 - zf ** 2) / zf], "o",
            color=LEVEL_COLORS[n], ms=7, zorder=5)
    ax.annotate(f"$n = {n}$", (zf, math.sqrt(float(Z0) ** 2 - zf ** 2) / zf),
                textcoords="offset points", xytext=(5, 8), fontsize=9)
```

The three curves; then a dot at each solution (on the black curve), with `zorder=5` so that the dot is drawn on top of the lines, and the label $n$ next to it.

```python
ax.axvline(float(Z0), color=GREY, ls=":", lw=1.0)
ax.text(float(Z0), 7.3, "$z_0 = \\sqrt{30}$", ha="right", fontsize=9)
ax.set_ylim(0.0, 8.0)
ax.set_xlabel("$z = k a$")
ax.set_ylabel("value of each side of the equation")
ax.set_title("Graphical solution of the finite-well equations, $z_0 = 5.477$")
ax.legend(loc="upper center", fontsize=8)
save_figure(fig, "graphical_solution",
            "The graphical solution of the finite-well equations for "
            ...)
```

A dotted line at $z_0$, labels and the saved figure `02b_4_graphical_solution.png`. **What Figure 02b.4 shows:** the black curve falls from large values to zero at $z_0$; it crosses each rising branch of $\tan z$ and $-\cot z$ once, four times in all, alternately on a blue (even) and an orange (odd) branch.

**In [7], the shooting functions of the well.**

```python
def shoot_well(E, n):
    """RK4 from x = -a (u = 1, u' = kappa) to x = 0 inside the well; E may be an
    array.  Returns (u(0), u'(0))."""
    E = np.asarray(E, dtype=float)
    kappa = np.sqrt(-2.0 * E)  # the decay rate outside the well
```

`np.asarray` turns `E` into a numpy array (a single number becomes an array with no axes), so that the same code works for one energy and for many; `kappa` is $\kappa = \sqrt{-2E}$ for every energy.

```python
    def f(x, Y):
        return np.array([Y[1], 2.0 * (-V0 - E) * Y[0]])  # (u', 2 (V - E) u)
    h = A / n
    Y = np.array([np.ones_like(E), kappa])
    for i in range(n):
        Y = rk4_step(f, -A + i * h, Y, h)
    return Y[0], Y[1]
```

The right-hand side inside the well, $(u', 2(V - E)u)$ with $V = -V_0$. The step is $a/n$; the start is $u = 1$ (`np.ones_like(E)` is an array of ones of the same shape as `E`) and $u' = \kappa$. After `n` RK4 steps from $x = -a$ the function returns $u(0)$ and $u'(0)$, for all energies at once.

```python
def F_even(E, n=200):
    return shoot_well(E, n)[1]  # u'(0): zero for an even state


def F_odd(E, n=200):
    return shoot_well(E, n)[0]  # u(0): zero for an odd state
```

The two shooting functions of Section 2.13.

```python
E_scan = np.linspace(-V0 + 1e-3, -1e-3, 400)  # 400 guesses inside (-V0, 0)
fe, fo = F_even(E_scan), F_odd(E_scan)
fig, ax = plt.subplots()
ax.plot(E_scan, fe, color=BLUE, lw=1.4, label="$F_{\\rm even}(E) = u'(0)$")
ax.plot(E_scan, fo, "--", color=ORANGE, lw=1.4, label="$F_{\\rm odd}(E) = u(0)$")
```

400 energies, kept $10^{-3}$ away from the ends $-V_0$ and 0 (where $k$ or $\kappa$ would be zero), are shot all at once; the two shooting functions are drawn.

```python
for n, (energy, parity, _) in enumerate(EXACT):
    ax.axvline(float(energy), ls=":", color=GREY, lw=1.0)
    ax.plot([float(energy)], [0.0], "o", color=LEVEL_COLORS[n], ms=7, zorder=5)
    ax.text(float(energy), 4.6, f"$E_{n}$", ha="center", fontsize=9)
ax.axhline(0.0, color=BLACK, lw=0.8)
ax.set_ylim(-5.5, 5.5)
ax.set_xlabel("guessed energy $E$ (units $\\hbar^2/(m a^2)$)")
ax.set_ylabel("mismatch at $x = 0$")
ax.set_title("Shooting functions of the finite well ($V_0 = 15$, $a = 1$)")
ax.legend(loc="lower left")
save_figure(fig, "shooting_functions_well",
            "The shooting functions of the finite well: $F_{\\rm even}(E) = "
            ...)
```

A dotted line, a dot and a label at each exact energy; then axis labels (the energy unit $\hbar^2/(m a^2)$ is 1 in the units of the notebook) and the saved figure `02b_5_shooting_functions_well.png`. **What Figure 02b.5 shows:** the solid blue $F_{\rm even}$ crosses zero exactly at $E_0$ and $E_2$, the dashed orange $F_{\rm odd}$ at $E_1$ and $E_3$; each crossing of a shooting function is a level of its parity.

```python
even_changes = int(np.sum(np.sign(fe[:-1]) != np.sign(fe[1:])))
odd_changes = int(np.sum(np.sign(fo[:-1]) != np.sign(fo[1:])))
report("sign changes of F_even and F_odd in the scan", f"{even_changes}, {odd_changes}")
check(even_changes == 2 and odd_changes == 2,
      "the scan finds 2 even and 2 odd sign changes, one per bound state")
```

`np.sign` gives $+1$, $-1$ or 0 for each entry; comparing the signs of neighbouring entries with `!=` gives `True` wherever the sign changes, and `np.sum` counts the `True` entries. The scan finds 2 sign changes of each function, one per bound state of that parity.

**In [8], all four levels by bisection.**

```python
def well_levels(n, tolerance=1e-13):
    """The four energies with n RK4 steps: scan, then bisection on the brackets."""
    lo, hi, even = [], [], []
    for values, is_even in ((F_even(E_scan, n), True), (F_odd(E_scan, n), False)):
        # the places i where the sign of the mismatch differs from that at i + 1
        for i in np.nonzero(np.sign(values[:-1]) != np.sign(values[1:]))[0]:
            lo.append(E_scan[i])
            hi.append(E_scan[i + 1])
            even.append(is_even)
```

`well_levels` first scans both shooting functions on the 400 energies with `n` RK4 steps (the same `n` as the refinement, so that the brackets belong to the same shooting function). `np.nonzero(...)[0]` lists the positions `i` at which the sign changes between `i` and `i + 1`; each such pair of neighbouring energies is a bracket, stored with its parity.

```python
    order = np.argsort(lo)  # lowest energy first
    lo, hi = np.array(lo)[order], np.array(hi)[order]
    even = np.array(even)[order]
```

`np.argsort(lo)` is the order of positions that sorts the left ends; using it as an index sorts all three lists the same way, lowest energy first.

```python
    def mismatch(E):
        u0, du0 = shoot_well(E, n)
        return np.where(even, du0, u0)  # u'(0) for even, u(0) for odd states
    f_lo = mismatch(lo)
    while np.max(hi - lo) > tolerance:
        mid = 0.5 * (lo + hi)
        f_mid = mismatch(mid)
        same = np.sign(f_mid) == np.sign(f_lo)  # the root is above mid
        lo, f_lo = np.where(same, mid, lo), np.where(same, f_mid, f_lo)
        hi = np.where(same, hi, mid)
    return 0.5 * (lo + hi), even
```

`mismatch` shoots an array of energies and picks, entry by entry, $u'(0)$ for the even brackets and $u(0)$ for the odd ones: `np.where(condition, a, b)` takes the entry of `a` where the condition is true and that of `b` elsewhere. The `while` loop is bisection on all four brackets at once: as long as the widest bracket is wider than $10^{-13}$, it shoots the four midpoints, and where the sign at the midpoint equals the sign at the left end it moves the left end up, elsewhere the right end down. The function returns the four midpoints of the final brackets and their parities.

```python
LEVELS, EVEN = well_levels(200)
exact = np.array([float(energy) for energy, _, _ in EXACT])
for n, (E_n, E_x) in enumerate(zip(LEVELS, exact)):
    say(f"E_{n}: RK4 (200 steps) {E_n:.12f}, exact {E_x:.12f}, "
        f"difference {E_n - E_x:+.1e}")
check(np.max(np.abs(LEVELS - exact)) < 1e-7,
      "the four shooting energies agree with the exact ones within 1e-7")
check(list(EVEN) == [True, False, True, False],
      "the levels alternate: even, odd, even, odd")
```

The four levels with 200 RK4 steps are compared with the exact ones. The differences are $+2.4 \times 10^{-11}$, $+1.5 \times 10^{-9}$, $+1.5 \times 10^{-8}$ and $+6.1 \times 10^{-8}$ (COMPUTED): all below $10^{-7}$, and larger for the higher levels. The second check confirms the alternation of parities.

**In [9], what a shot looks like when it misses.**

```python
def shoot_line(E, x_start=-3.0, x_end=3.0, n=600):
    """RK4 across the whole line; the potential is taken at the middle of every
    step (constant inside a step, because the walls are grid points)."""
    kappa = math.sqrt(-2.0 * E)
    h = (x_end - x_start) / n
    Y = np.array([1.0, kappa]) * math.exp(kappa * (x_start + A))  # exact tail
    xs, us = [x_start], [Y[0]]
```

This shot crosses the whole line from $x = -3$ to $x = 3$ in 600 steps of $h = 0.01$. It starts with the exact decaying tail: $u = e^{\kappa(x + a)}$ and $u' = \kappa u$ at $x = -3$.

```python
    for i in range(n):
        x = x_start + i * h
        V = -V0 if abs(x + h / 2) < A else 0.0  # the potential of this step

        def f(x_value, Y_value, V=V):  # V=V freezes this step's potential in f
            return np.array([Y_value[1], 2.0 * (V - E) * Y_value[0]])
        Y = rk4_step(f, x, Y, h)
        xs.append(x + h)
        us.append(Y[0])
    return np.array(xs), np.array(us)
```

For every step the potential is read at the middle of the step: $-V_0$ if $|x + h/2| < a$, else 0. Because the walls $x = \pm 1$ are grid points, the potential is constant inside every step, and RK4 keeps its accuracy. The right-hand side is defined anew for each step; the default argument `V=V` stores the current step's potential inside the function. After each step the position and $u$ are recorded.

```python
E0 = float(EXACT[0][0])
fig, ax = plt.subplots()
for shift, color, style in ((-0.05, ORANGE, "--"), (0.0, BLUE, "-"),
                            (0.05, AQUA, "-.")):
    xs, us = shoot_line(E0 + shift)
    ax.plot(xs, us / np.max(np.abs(us[xs <= 0])), style, color=color, lw=1.6,
            label=f"$E = E_0 {shift:+.2f}$")
```

Three shots: at the ground-state energy $E_0$ and $0.05$ below and above it. Each is divided by its largest size on the left half (`us[xs <= 0]` keeps the values with $x \le 0$), so that the three curves have comparable heights.

```python
ax.axvspan(-A, A, color=GREY, alpha=0.15, label="inside the well")
ax.axhline(0.0, color=BLACK, lw=0.8)
ax.set_ylim(-2.0, 2.0)
ax.set_xlabel("position $x$ (units $a$)")
ax.set_ylabel("$u(x)$ (scaled to 1 at the left peak)")
ax.set_title("Shots across the well near the ground state $E_0 = %.4f$" % E0)
ax.legend(loc="lower left", fontsize=8)
save_figure(fig, "trial_solutions_well",
            "Shots across the whole line from $x = -3$ to $x = 3$ (horizontal "
            ...)
```

`axvspan` shades the well; `"... %.4f" % E0` is an older way of writing a number into a string (the same as an f-string with `:.4f`). The figure is saved as `02b_6_trial_solutions_well.png`; one line of its caption is an f-string, which writes the value of $E_0$ into the caption. **What Figure 02b.6 shows:** all three shots start alike on the left; only the one at $E_0$ decays again on the right, while the one just below flies off to one infinity and the one just above to the other.

```python
tail = {shift: shoot_line(E0 + shift)[1][-1] for shift in (-0.05, 0.05)}
check(tail[-0.05] * tail[0.05] < 0 and min(abs(tail[-0.05]), abs(tail[0.05])) > 10,
      "slightly below and above E0 the shots fly off to opposite infinities")
```

The end values of the two missing shots have opposite signs (their product is negative) and are both larger than 10 in size.

**In [10], the four wave functions.**

```python
def simpson(values, h):
    """Simpson's rule for equally spaced values (an even number of intervals)."""
    return h / 3 * (values[0] + values[-1] + 4 * values[1:-1:2].sum()
                    + 2 * values[2:-1:2].sum())
```

Simpson's rule of Section 2.13. `values[1:-1:2]` takes every second entry starting at position 1 and stopping before the last (the odd positions, weight 4); `values[2:-1:2]` every second entry starting at position 2 (the inner even positions, weight 2).

```python
def wave_function(E, is_even, n=200):
    """Normalised u on a grid of -3 <= x <= 3 (step a/n), built as described."""
    kappa = math.sqrt(-2.0 * E)
    h = A / n

    def f(x, Y):
        return np.array([Y[1], 2.0 * (-V0 - E) * Y[0]])
    Y = np.array([1.0, kappa])
    inside = [1.0]
    for i in range(n):
        Y = rk4_step(f, -A + i * h, Y, h)
        inside.append(Y[0])
    inside = np.array(inside)  # u on -a <= x <= 0
```

For one level, the shot from $x = -a$ to 0 inside the well (as in In [7], for a single energy), keeping all $n + 1$ values of $u$.

```python
    norm = 2.0 * (simpson(inside ** 2, h) + 1.0 / (2.0 * kappa))  # both halves
```

$\int u^2\,dx$ over the whole line: on the left half, Simpson's rule inside the well plus the exact tail integral $1/(2\kappa)$ of Section 2.13 (the tail starts with $u(-a) = 1$); the right half gives the same by symmetry, hence the factor 2.

```python
    x_left = np.arange(-3.0 * n, -n) * h  # -3 <= x < -a
    left = np.concatenate([np.exp(kappa * (x_left + A)), inside])
    x_half = np.concatenate([x_left, -A + np.arange(n + 1) * h])  # up to x = 0
```

`np.arange(-3.0 * n, -n)` counts from $-600$ up to $-201$, so times $h = 1/200$ it gives the positions from $-3$ to just before $-1$. On them $u$ is the exact tail; `np.concatenate` joins it with the inside values. `x_half` holds the matching positions from $-3$ to 0.

```python
    sign = 1.0 if is_even else -1.0
    x_all = np.concatenate([x_half, -x_half[-2::-1]])  # mirror x -> -x
    u_all = np.concatenate([left, sign * left[-2::-1]])
    return x_all, u_all / math.sqrt(norm), kappa, inside / math.sqrt(norm), h
```

The right half is the mirror image: `x_half[-2::-1]` runs backwards from the second-to-last entry to the first (leaving out $x = 0$, which is already there), and its negatives are the positions $x > 0$; the values are copied with the sign $+1$ for an even and $-1$ for an odd state. The function returns the positions, the normalised wave function (divided by $\sqrt{\int u^2 dx}$), $\kappa$, the normalised inside values and the step.

```python
STATES = [wave_function(E_n, bool(e)) for E_n, e in zip(LEVELS, EVEN)]
fig, ax = plt.subplots(figsize=(7.0, 5.6))
x_pot = np.array([-3.0, -A, -A, A, A, 3.0])
ax.plot(x_pot, [0.0, 0.0, -V0, -V0, 0.0, 0.0], color=BLACK, lw=1.5,
        label="potential $V(x)$")
nodes = []
```

The four wave functions are built; the potential is drawn as a black line through six corner points (the walls are vertical because two points share each $x = \pm a$).

```python
for n, (x_all, u_all, kappa, inside, h) in enumerate(STATES):
    E_n = LEVELS[n]
    ax.axhline(E_n, ls=":", color=GREY, lw=0.8)
    parity = "even" if EVEN[n] else "odd"
    ax.plot(x_all, E_n + 1.8 * u_all, color=LEVEL_COLORS[n], lw=1.6,
            label=f"$E_{n} = {E_n:.4f}$ ({parity})")
    big = u_all[np.abs(u_all) > 1e-8 * np.max(np.abs(u_all))]  # drop tiny values
    nodes.append(int(np.sum(np.sign(big[:-1]) != np.sign(big[1:]))))
```

Each state is drawn lifted to its energy, as $E_n + 1.8\,u_n(x)$, on a dotted line at its energy. To count the **nodes** (sign changes), the values smaller than $10^{-8}$ times the largest are dropped first, so that a value that is zero up to rounding (the centre of an odd state) cannot be counted as an extra sign change; then the sign changes are counted as in In [7].

```python
ax.set_xlabel("position $x$ (units $a$)")
ax.set_ylabel("energy (units $\\hbar^2/(m a^2)$) and $E_n + 1.8\\, u_n(x)$")
ax.set_ylim(-16.0, 5.0)  # room for the legend above the well
ax.set_title("The four bound states of the finite square well")
ax.legend(loc="upper center", ncol=2, fontsize=8)
save_figure(fig, "eigenfunctions",
            "The four bound states of the finite square well of depth 15 and "
            ...)
report("nodes of the states 0 to 3", nodes)
check(nodes == [0, 1, 2, 3], "the state n has exactly n nodes")
```

Labels, a legend in two columns (`ncol=2`) and the saved figure `02b_7_eigenfunctions.png`; the node counts are $[0, 1, 2, 3]$ and the check requires exactly that. **What Figure 02b.7 shows:** the state $n$ has $n$ nodes, even and odd states alternate, and the higher the energy, the further the wave function leaks out of the well, where it decays like $e^{-\kappa|x|}$ ($\kappa$ is smaller for a higher level).

```python
def overlap(m, n):
    """The integral of u_m u_n over the whole line: Simpson inside, exact tails."""
    _, _, k_m, in_m, h = STATES[m]
    _, _, k_n, in_n, _ = STATES[n]
    half = simpson(in_m * in_n, h) + in_m[0] * in_n[0] / (k_m + k_n)
    same = (EVEN[m] == EVEN[n])  # different parity: the halves cancel exactly
    return 2.0 * half if same else 0.0
```

$\int u_m u_n\,dx$ over the left half is Simpson's rule inside the well plus the exact tail integral: on the tail $u_m u_n = u_m(-a)\,u_n(-a)\, e^{(\kappa_m + \kappa_n)(x + a)}$, and $\int_{-\infty}^{-a} e^{(\kappa_m + \kappa_n)(x + a)}\,dx = 1/(\kappa_m + \kappa_n)$ (the same antiderivative as in Section 2.13), which gives the term `in_m[0] * in_n[0] / (k_m + k_n)`. For the same parity the right half equals the left half; for different parity the integral is exactly zero (Section 2.13).

```python
gram = np.array([[overlap(m, n) for n in range(4)] for m in range(4)])
report("largest |integral u_m u_n - (1 if m = n else 0)|",
       f"{np.max(np.abs(gram - np.eye(4))):.1e}")
check(np.max(np.abs(gram - np.eye(4))) < 1e-8,
      "the wave functions are normalised and orthogonal within 1e-8")
```

`gram` is the 4 by 4 table of all the integrals. For normalised, orthogonal functions it must be the unit matrix `np.eye(4)` (1 on the diagonal, 0 elsewhere); the largest difference is $1.6 \times 10^{-10}$ (COMPUTED), within the required $10^{-8}$. The entries for two states of different parity are set to 0 by `overlap` itself, using the proof; so this check tests the normalisation and the orthogonality of states of the same parity only. The next lines test the different-parity case numerically.

```python
middle = len(STATES[0][0]) // 2  # the position of x = 0 in the grid -3 ... 3
whole_line, left_half = [], []
```

`STATES[0][0]` is the grid of $x$ values from $-3$ to $3$ (the first entry returned by `wave_function`). It has $6n + 1 = 1201$ points, so the integer division `// 2` gives 600, the position of the middle point $x = 0$. Two empty lists will collect the results.

```python
for m, n in [(0, 1), (0, 3), (1, 2), (2, 3)]:  # the pairs of different parity
    product = STATES[m][1] * STATES[n][1]  # u_m u_n on the grid
    h_grid = STATES[m][4]  # the grid spacing a/200
    whole_line.append(abs(simpson(product, h_grid)))  # from x = -3 to x = 3
    left_half.append(abs(simpson(product[:middle + 1], h_grid)))  # -3 to 0
```

The states 0 and 2 are even, 1 and 3 odd, so these are the four pairs of different parity. `STATES[m][1]` is the normalised wave function $u_m$ on the whole grid (the second entry returned by `wave_function`) and `STATES[m][4]` the grid spacing $a/200 = 0.005$. For each pair the product $u_m u_n$ is integrated with Simpson's rule over the whole grid ($-3 \le x \le 3$, 1200 intervals, an even number as Simpson's rule needs) and over the left half alone (`product[:middle + 1]`, the points from $x = -3$ to $x = 0$, 600 intervals); the sizes are stored.

```python
report("different parity: largest |whole integral|, smallest |left half|",
       f"{max(whole_line):.1e}, {min(left_half):.2f}")
check(max(whole_line) < 1e-12 < 0.01 < min(left_half),
      "different parity: the two halves cancel, the whole integral is 0")
```

The RESULT line prints the largest whole integral, $9.5 \times 10^{-17}$, and the smallest half integral, 0.16 (COMPUTED). The chained comparison `a < b < c < d` means $a < b$ and $b < c$ and $c < d$: every whole integral is below $10^{-12}$ (zero up to rounding), while every half integral is above 0.01. So the two halves are far from zero each but cancel exactly, as the symmetry argument of Section 2.13 says: the product of an even and an odd function is odd.

**In [11], the order of the computed energies.**

```python
N_STEPS = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
level_errors = np.array([np.abs(well_levels(n)[0] - exact) for n in N_STEPS])
h_values = A / np.array(N_STEPS, dtype=float)
```

The whole level search is repeated with 4 to 1024 RK4 steps on $-a \le x \le 0$; `level_errors` is a table with one row per step count and one column per level.

```python
fig, ax = plt.subplots()
slopes = []
for n in range(4):
    ax.loglog(h_values, level_errors[:, n], "o-", color=LEVEL_COLORS[n], ms=5,
              lw=1.2, label=f"$E_{n}$")
    fit = level_errors[:, n] > 1e-12  # leave out the rounding-limited points
    slope, _ = np.polyfit(np.log10(h_values[fit]), np.log10(level_errors[fit, n]), 1)
    slopes.append(slope)
```

For each level the errors are drawn against the step on a log-log plot, and a straight line is fitted through the points above $10^{-12}$ (below that the errors are limited by rounding and by the bisection tolerance).

```python
guide = level_errors[0, 3] * (h_values / h_values[0]) ** 4
ax.loglog(h_values, guide, "--", color=GREY, lw=1.0, label="slope 4")
ax.set_xlabel("RK4 step size $h = a/n$ (units $a$)")
ax.set_ylabel("error of the energy (units $\\hbar^2/(m a^2)$)")
ax.set_title("Shooting energies converge like $h^4$")
ax.legend()
save_figure(fig, "eigenvalue_convergence",
            "The error of the four shooting energies of the finite well, "
            ...)
```

A dashed guide of slope 4 through the first point of the highest level, labels and the saved figure `02b_8_eigenvalue_convergence.png`. **What Figure 02b.8 shows:** four parallel lines of slope 4, the highest level on top: an eigenvalue found by shooting inherits the order of the integrator, and a level whose wave function oscillates faster (larger $k$) has a larger error, which grows like $(kh)^4$.

```python
report("measured orders of E_0 ... E_3", ", ".join(f"{s:.2f}" for s in slopes))
check(all(3.8 < s < 4.3 for s in slopes),
      "the energy errors fall with the order 4 (slopes between 3.8 and 4.3)")
check(np.all(level_errors[-1] < 1e-9), "with 1024 steps every energy is within 1e-9")
```

The measured orders are 3.99, 3.98, 3.96 and 3.92 (COMPUTED); the checks require them between 3.8 and 4.3 and every error with 1024 steps below $10^{-9}$.

**In [12], the last check.** It is built like In [15] of Notebook 02a: it checks that the eight figure files `02b_1_trial_solutions_string.png` to `02b_8_eigenvalue_convergence.png` exist and prints ALL 16 CHECKS PASSED (notebook 02b).

```python
names = ["trial_solutions_string", "shooting_function_string",
         "bisection_vs_secant", "graphical_solution", "shooting_functions_well",
         "trial_solutions_well", "eigenfunctions", "eigenvalue_convergence"]
present = [output_file(f"{FIGURE_FOLDER}/02b_{k}_{name}.png").is_file()
           for k, name in enumerate(names, 1)]
check(all(present), f"all {len(names)} figure files of notebook 02b exist")
all_checks_passed()
```

The 15 checks are: 1 in In [3], 1 in In [4], 3 in In [5], 1 in In [6], 1 in In [7], 2 in In [8], 1 in In [9], 2 in In [10], 2 in In [11] and 1 in In [12].

### 2.18 Functions of several variables and partial derivatives

**Functions of several variables.** A function of two variables is a rule $f(x, y)$ that gives a number for every pair of numbers $(x, y)$; a function of eight variables gives a number for every list $(x_1, \dots, x_8)$. The entries of the author's metric are functions of this kind (of $x_4$ and $x_8$ only).

**Partial derivatives.** The **partial derivative** of $f$ with respect to $x$ is the ordinary derivative with respect to $x$ while all the other variables are held fixed:

$$
\frac{\partial f}{\partial x}(x, y) = \lim_{h \to 0} \frac{f(x + h, y) - f(x, y)}{h} .
$$

The curly $\partial$ reminds us that other variables exist and are held fixed. We also write $\partial_x f$, and for the author's coordinates $\partial_4 = \partial/\partial x_4$ and $\partial_8 = \partial/\partial x_8$. Holding $y$ fixed at a value $y_0$ turns $f$ into the function $x \mapsto f(x, y_0)$ of one variable, a **slice**; the partial derivative is the slope of the slice. Every rule of one-variable calculus (sums, products, quotients, the chain rule) therefore holds for each partial derivative.

*Example.* $f(x, y) = x^2 \sin y$.

$$
\frac{\partial f}{\partial x} = 2x \sin y
$$

(with $y$ held fixed, $\sin y$ is a constant factor, and the derivative of $x^2$ is $2x$);

$$
\frac{\partial f}{\partial y} = x^2 \cos y
$$

(with $x$ held fixed, $x^2$ is a constant factor, and the derivative of $\sin y$ is $\cos y$). At the point $(x_0, y_0) = (1.2, 0.7)$ these slopes are $2 \cdot 1.2 \cdot \sin 0.7 = 1.5461$ and $1.44 \cos 0.7 = 1.1014$ (COMPUTED in Notebook 02c, In [3]).

**Second and mixed derivatives.** Differentiating again gives second partial derivatives; the **mixed** ones differentiate once with respect to each variable:

$$
\frac{\partial}{\partial y}\Big(\frac{\partial f}{\partial x}\Big) = \frac{\partial}{\partial y}(2x\sin y) = 2x\cos y, \qquad \frac{\partial}{\partial x}\Big(\frac{\partial f}{\partial y}\Big) = \frac{\partial}{\partial x}(x^2\cos y) = 2x\cos y
$$

(each time the other variable is a constant factor). The two orders agree. This is **Schwarz's theorem**: for a function whose second partial derivatives are continuous, the order of differentiation does not matter (ASSUMED: a standard theorem of calculus, quoted without proof; Notebook 02c confirms it for this example, and Section 2.24 uses it).

**The linear approximation.** How much does $f$ change when BOTH variables change a little, $x \to x + dx$ and $y \to y + dy$? Split the change into two moves, one variable at a time:

$$
f(x + dx, y + dy) - f(x, y) = \big[f(x + dx, y + dy) - f(x, y + dy)\big] + \big[f(x, y + dy) - f(x, y)\big]
$$

(we add and subtract $f(x, y + dy)$);

$$
f(x + dx, y + dy) - f(x, y) \approx \frac{\partial f}{\partial x}(x, y + dy)\, dx + \frac{\partial f}{\partial y}(x, y)\, dy
$$

(each bracket is the change of a slice, which is its slope times the step, up to terms of second order in the step);

$$
f(x + dx, y + dy) - f(x, y) \approx \frac{\partial f}{\partial x}\, dx + \frac{\partial f}{\partial y}\, dy
$$

(the slope in $x$ changes only a little when $y$ moves by $dy$, if $\partial f/\partial x$ is continuous; both slopes are now taken at $(x, y)$).

**The gradient and the level curves.** The **gradient** is the arrow $\nabla f = (\partial f/\partial x,\, \partial f/\partial y)$. A **level curve** (contour) is a curve on which $f$ has one fixed value. Move a small distance $s$ in the direction of a unit arrow $(c, d)$ (one with $c^2 + d^2 = 1$), that is $dx = s c$ and $dy = s d$. By the linear approximation the change of $f$ is

$$
\Delta f \approx s\,\Big(c\, \frac{\partial f}{\partial x} + d\, \frac{\partial f}{\partial y}\Big),
$$

$s$ times the **dot product** of the direction with the gradient (the dot product of two arrows $(c, d)$ and $(p, q)$ is the number $cp + dq$). For short write $f_x = \partial f/\partial x$ and $f_y = \partial f/\partial y$, so that $\nabla f = (f_x, f_y)$, and let

$$
|\nabla f| = \sqrt{f_x^2 + f_y^2}
$$

be the **length** of the gradient arrow (Pythagoras' theorem; we take a point where $\nabla f \ne (0, 0)$). Two facts follow. (1) The arrow $(c, d) = (-f_y,\, f_x)/|\nabla f|$ is a unit arrow, because $c^2 + d^2 = (f_y^2 + f_x^2)/|\nabla f|^2 = 1$. Along it the bracket is $c f_x + d f_y = (-f_y f_x + f_x f_y)/|\nabla f| = 0$: $f$ does not change to first order, so this direction runs along the level curve, and it is perpendicular to the gradient (their dot product is zero). (2) Every unit arrow can be written $(c, d) = (\cos\varphi, \sin\varphi)$, where $\varphi$ is its angle to the $x$ axis, and the gradient as $(f_x, f_y) = |\nabla f|\,(\cos\psi, \sin\psi)$ with its angle $\psi$. Then

$$
c f_x + d f_y = |\nabla f|\,(\cos\varphi\cos\psi + \sin\varphi\sin\psi) = |\nabla f|\cos(\varphi - \psi)
$$

(insert both; then the addition formula of the cosine, $\cos(a - b) = \cos a\cos b + \sin a\sin b$). The cosine is largest, 1, when $\varphi = \psi$: the change of $f$ per unit length is largest when the arrow points along the gradient, and there it is $|\nabla f|$. So the gradient points uphill, in the direction of the steepest increase, and its length is the steepest slope; in the opposite direction ($\varphi - \psi = \pi$, cosine $-1$) $f$ falls fastest. Notebook 02c, In [4], checks both facts at the point $(1.2, 0.7)$: a step of $10^{-4}$ along the level curve changes $f$ by only $-9.58 \times 10^{-9}$ (a second-order amount), and along the gradient $f$ rises at the rate 1.898407 per unit length, against $|\nabla f| = 1.898293$ (COMPUTED).

**Finite differences.** A computer approximates a derivative from values of the function at nearby points with a small spacing $h$. Taylor's theorem (Section 2.3) gives

$$
f(x + h) = f(x) + h f'(x) + \frac{h^2}{2} f''(x) + \frac{h^3}{6} f'''(x) + \dots
$$

and, with $h$ replaced by $-h$ (the odd powers change sign),

$$
f(x - h) = f(x) - h f'(x) + \frac{h^2}{2} f''(x) - \frac{h^3}{6} f'''(x) + \dots
$$

The **forward difference**:

$$
\frac{f(x + h) - f(x)}{h} = f'(x) + \frac{h}{2} f''(x) + \dots
$$

(subtract $f(x)$ from the first series and divide by $h$): its error is proportional to $h$ (order 1). The **central difference**:

$$
\frac{f(x + h) - f(x - h)}{2h} = f'(x) + \frac{h^2}{6} f'''(x) + \dots
$$

(subtract the second series from the first: the even powers cancel, $f(x + h) - f(x - h) = 2h f'(x) + \frac{h^3}{3} f'''(x) + \dots$; then divide by $2h$): its error is proportional to $h^2$ (order 2). For a partial derivative the same formulas are applied to a slice. A **mixed** derivative $\partial^2 f/\partial x \partial y$ is approximated by applying the central difference twice, first in $y$ and then in $x$:

$$
\frac{\partial^2 f}{\partial x\, \partial y} \approx \frac{f(x{+}h, y{+}h) - f(x{+}h, y{-}h) - f(x{-}h, y{+}h) + f(x{-}h, y{-}h)}{4h^2}
$$

(the central difference in $y$, $g(x) = [f(x, y + h) - f(x, y - h)]/(2h)$, inserted into the central difference in $x$, $[g(x + h) - g(x - h)]/(2h)$; each of the two steps has an error of order $h^2$, so the result has order 2).

**The best spacing.** The truncation error falls as $h$ shrinks, but rounding grows: each value of $f$ carries a rounding error of about $\epsilon |f|$ (Section 2.6), and a difference of two such values divided by $h$ carries an error of about $\epsilon |f| / h$. For the forward difference the total error is about

$$
E(h) = \alpha h + \frac{\beta}{h}, \qquad \alpha = \frac{|f''|}{2}, \quad \beta = \epsilon |f|
$$

(the truncation term of the forward difference plus the rounding term). It is smallest where its derivative vanishes:

$$
E'(h) = \alpha - \frac{\beta}{h^2} = 0, \qquad h_{\rm best} = \sqrt{\beta/\alpha}
$$

(differentiate term by term; then solve for $h$). For $f = x^2 \sin y$ at $(1.2, 0.7)$ in the variable $y$: $|f| = 0.928$ and $|\partial^2 f/\partial y^2| = |x^2 \sin y| = 0.928$, so $\beta = 2.2 \times 10^{-16} \cdot 0.928 = 2.0 \times 10^{-16}$, $\alpha = 0.46$ and $h_{\rm best} \approx 2 \times 10^{-8}$. For the central difference $E(h) = \alpha h^2 + \beta/h$ with $\alpha = |f'''|/6$, and $E'(h) = 2\alpha h - \beta/h^2 = 0$ gives $h_{\rm best} = (\beta/(2\alpha))^{1/3} \approx 10^{-5}$ (here $|f'''| = |\partial^3 f/\partial y^3| = |x^2\cos y| = 1.101$, so $\alpha = 0.184$ and $h_{\rm best} = 8 \times 10^{-6}$).

For the mixed formula both parts of the error are different. Its truncation term: the central difference in $y$ is $g(x) = \partial_y f(x, y) + \frac{h^2}{6}\,\partial_y^3 f(x, y) + \dots$ (the series of the central difference above, applied to the slice in $y$; $\partial_y^3$ means $\partial_y$ applied three times), and the central difference in $x$ of $g$ is $\partial_x g + \frac{h^2}{6}\,\partial_x^3 g + \dots$ (the same series in $x$). Inserting $g$ into the second series gives

$$
\frac{g(x + h) - g(x - h)}{2h} = \partial_x\partial_y f + \frac{h^2}{6}\big(\partial_x\partial_y^3 f + \partial_x^3\partial_y f\big) + \dots
$$

(the term $\frac{h^2}{6}\partial_x^3 g$ contributes $\frac{h^2}{6}\partial_x^3\partial_y f$; the terms with $h^4$ are left out). Its rounding term: each of the four values of $f$ carries about $\epsilon |f|$, together at most about $4\epsilon|f|$, and the formula divides by $4h^2$, which gives about $\epsilon|f|/h^2$. So

$$
E(h) = \alpha h^2 + \frac{\beta}{h^2}, \qquad \alpha = \frac{|\partial_x\partial_y^3 f + \partial_x^3\partial_y f|}{6}, \quad \beta = \epsilon |f|
$$

(the truncation term plus the rounding term);

$$
E'(h) = 2\alpha h - \frac{2\beta}{h^3} = 0, \qquad h^4 = \frac{\beta}{\alpha}, \qquad h_{\rm best} = \Big(\frac{\beta}{\alpha}\Big)^{1/4}
$$

(differentiate term by term, using $d(h^{-2})/dh = -2h^{-3}$; multiply by $h^3/(2\alpha)$; take the fourth root). For $f = x^2\sin y$: $\partial_y^3 f = -x^2\cos y$, so $\partial_x\partial_y^3 f = -2x\cos y$, while $\partial_x^3\partial_y f = \partial_x^3(x^2\cos y) = 0$ (the third derivative of $x^2$ is 0). At $(1.2, 0.7)$ this gives $\alpha = 2 \cdot 1.2 \cdot \cos 0.7/6 = 0.306$ and $h_{\rm best} = (2.0 \times 10^{-16}/0.306)^{1/4} = 1.6 \times 10^{-4}$, of the order $10^{-4}$.

These are estimates of the scale only (rounding errors are not always of their largest size); Notebook 02c (In [6]) measures the best spacings $1.0 \times 10^{-8}$, $1.8 \times 10^{-6}$ and $5.6 \times 10^{-5}$ (COMPUTED). The lesson: the best spacing is far from the smallest one.

### 2.19 The chain rule and the derivatives of the author's metric

**The chain rule for $z = 6 H x_8$.** The author writes the hidden direction with the variable $z = 6 H x_8$, which runs over $0 < z < \pi/2$. A function of $z$, such as $g_{88} = \cot^2 z$, depends on $x_8$ through $z$, and the chain rule of one-variable calculus gives

$$
\frac{\partial}{\partial x_8}\, F(z) = \frac{dF}{dz}\, \frac{\partial z}{\partial x_8} = 6H\, \frac{dF}{dz}
$$

(the chain rule, and $\partial z/\partial x_8 = 6H$ because $z$ is $6H$ times $x_8$). In short, $\partial_8 = 6H\, d/dz$ on functions of $z$. *Example.*

$$
\frac{d}{dz}\cot^2 z = 2\cot z \cdot \Big(-\frac{1}{\sin^2 z}\Big) = -\frac{2\cot z}{\sin^2 z}
$$

(the chain rule for the square, and the derivative of $\cot z$ is $-1/\sin^2 z$), so $\partial_8 \cot^2(6Hx_8) = -12 H \cot z/\sin^2 z$ (multiply by $6H$); Notebook 02c, In [7], prints exactly this.

**The metric and its scale factors.** The metric is an $8 \times 8$ table of numbers $g_{ab}$, a **matrix** (Chapter 1). In the author's coordinates it is **diagonal**: only the entries $g_{11}, \dots, g_{88}$ on its diagonal are nonzero, with

$$
g_{11} = g_{22} = g_{33} = e^{2 a_4}\sin^{1/3} z, \quad g_{44} = -1, \quad g_{55} = g_{66} = g_{77} = -e^{-2 a_4}\sin^{1/3} z, \quad g_{88} = \cot^2 z
$$

(the author's metric; COMPUTED: Notebook 02c, In [8], reads these eight entries from the Revision record `Revision/gkd_lovelock/results/curvature.json`, key `metricDiagonal`, and checks them against the formulas). The entries are positive for the space-like directions $x_1, x_2, x_3, x_8$ and negative for the time-like directions $x_4, x_5, x_6, x_7$; four positive and four negative entries are what the **signature** (4,4) means. The scale factor $s_a = \sqrt{|g_{aa}|}$ of each direction is

$$
s_{1,2,3} = e^{a_4}\sin^{1/6} z, \qquad s_4 = 1, \qquad s_{5,6,7} = e^{-a_4}\sin^{1/6} z, \qquad s_8 = \cot z
$$

(the square root of each absolute value, as in Section 2.2; for $s_8$ we use $\cot z > 0$ on $0 < z < \pi/2$).

**The logarithmic rates.** The rate at which a scale factor grows, as a fraction of itself, is its **logarithmic derivative** $\partial_c \ln s_a = (\partial_c s_a)/s_a$ (the chain rule for the logarithm, whose derivative is $1/s$). Since $s_a^2 = |g_{aa}|$,

$$
\partial_c \ln s_a = \frac12\, \partial_c \ln |g_{aa}| = \frac{\partial_c g_{aa}}{2 g_{aa}}
$$

($\ln s = \frac12 \ln s^2$; then the chain rule for the logarithm; the absolute value does not matter because $\partial_c |g|/|g| = \partial_c g/g$). For 3-space:

$$
\ln s_1 = a_4 + \tfrac16 \ln \sin z
$$

(the logarithm of a product is the sum of the logarithms, $\ln e^{a_4} = a_4$, and $\ln(\sin^{1/6} z) = \frac16 \ln \sin z$);

$$
\partial_4 \ln s_1 = a_4', \qquad \partial_8 \ln s_1 = \tfrac16 \cdot 6H \cdot \frac{\cos z}{\sin z} = H\cot z
$$

($a_4$ depends on $x_4$ only, $z$ on $x_8$ only; the derivative of $\ln \sin z$ is $\cos z/\sin z$, and the chain rule supplies $6H$). For the extra times $\ln s_5 = -a_4 + \frac16\ln\sin z$, so

$$
\partial_4 \ln s_5 = -a_4', \qquad \partial_8 \ln s_5 = H\cot z
$$

(the same steps with $-a_4$). For the hidden direction $\ln s_8 = \ln \cot z$:

$$
\partial_8 \ln s_8 = 6H\, \frac{-1/\sin^2 z}{\cot z} = -\frac{6H}{\sin z \cos z}
$$

(the chain rule twice; then $\cot z \sin^2 z = \sin z \cos z$), and $\partial_4 \ln s_8 = 0$; the time direction has $s_4 = 1$ and both rates 0. Along the history $a_4 = A H x_4$ we have $a_4' = AH$; with $A = H = 1$ the three 3-space factors grow at the rate $+1$ and the three extra-time factors shrink at the rate $-1$: 3-space inflates and the extra times deflate exponentially (Notebook 02c, In [9]).

**The rates add up to the rate of the volume.** Along $x_4$:

$$
\sum_{a=1}^{8} \partial_4 \ln s_a = 3a_4' + 0 - 3a_4' + 0 = 0
$$

(three 3-space directions, the time, three extra times, the hidden direction). Along $x_8$:

$$
\sum_{a=1}^{8} \partial_8 \ln s_a = 6H\cot z - \frac{6H}{\sin z \cos z} = 6H\, \frac{\cos^2 z - 1}{\sin z \cos z} = -6H\, \frac{\sin^2 z}{\sin z\cos z} = -6H\tan z
$$

(six directions with $H\cot z$; both terms written over the denominator $\sin z\cos z$; then $\cos^2 z - 1 = -\sin^2 z$). We now show that these sums are the rates of the **volume factor** $\sqrt{|\det g|}$.

**The determinant.** The **determinant** of a diagonal matrix is the product of its diagonal entries (Chapter 1). So

$$
\det g = \big(e^{2a_4}\sin^{1/3} z\big)^3 \cdot (-1) \cdot \big(-e^{-2a_4}\sin^{1/3} z\big)^3 \cdot \cot^2 z
$$

(the product of the eight entries);

$$
\det g = (-1)(-1)^3\, e^{6a_4} e^{-6a_4} \sin^{6/3} z\, \cot^2 z = \sin^2 z \cot^2 z
$$

(the four minus signs multiply to $+1$; $(e^{2a_4})^3 = e^{6a_4}$ and $(e^{-2a_4})^3 = e^{-6a_4}$ multiply to $e^0 = 1$; the six factors $\sin^{1/3} z$ give $\sin^2 z$);

$$
\det g = \sin^2 z\, \frac{\cos^2 z}{\sin^2 z} = \cos^2 z, \qquad \sqrt{|\det g|} = \sin z \cot z = \cos z
$$

($\cot z = \cos z/\sin z$; and $\cos z > 0$ on $0 < z < \pi/2$). The factors $e^{6a_4}$ of the inflating 3-space and $e^{-6a_4}$ of the deflating extra times cancel: the volume factor does not depend on $x_4$, for EVERY function $a_4(x_4)$ (PROVED here; COMPUTED in Notebook 02c, In [11], which reproduces the record's entry `sqrtAbsDetG` $= \sin z\cot z$ of `Revision/gkd_lovelock/results/curvature.json` and the Wolfram check `sqrt_abs_det_g_is_cos_z` of `Revision/field_equations_a4/reports/wolfram-a4-report.json`).

**Jacobi's formula** for the derivative of the volume factor of a diagonal metric:

$$
\sqrt{|\det g|} = \prod_{a=1}^{8} s_a
$$

($|\det g|$ is the product of the $|g_{aa}| = s_a^2$, and the square root of a product is the product of the square roots);

$$
\partial_c \ln \sqrt{|\det g|} = \sum_{a=1}^{8} \partial_c \ln s_a = \sum_{a=1}^{8} \frac{\partial_c g_{aa}}{2 g_{aa}} = \frac12\, \mathrm{tr}\big(g^{-1}\, \partial_c g\big)
$$

(the logarithm of a product is the sum of the logarithms; then the rates computed above; finally, for a diagonal $g$ the inverse $g^{-1}$ is diagonal with the entries $1/g_{aa}$, the matrix $g^{-1}\partial_c g$ is diagonal with the entries $\partial_c g_{aa}/g_{aa}$, and the **trace** tr is the sum of the diagonal entries). Multiplying by $\sqrt{|\det g|}$ gives Jacobi's formula $\partial_c \sqrt{|\det g|} = \frac12 \sqrt{|\det g|}\, \mathrm{tr}(g^{-1}\partial_c g)$. With the sums above: $\partial_4 \ln\cos z = 0$ and $\partial_8 \ln \cos z = 6H \cdot (-\sin z/\cos z) = -6H\tan z$, in agreement (Notebook 02c, In [10] and In [11]).

**Christoffel symbols of a diagonal metric.** The geometry of Chapter 3 combines first partial derivatives of the metric into the **Christoffel symbols** $\Gamma^a{}_{bc}$. Here we take their formula for a diagonal metric as given (ASSUMED in this chapter; derived in Chapter 3) and use it only as an exercise in partial derivatives:

$$
\Gamma^a{}_{bc} = \frac{1}{2 g_{aa}}\big(\partial_b g_{ac} + \partial_c g_{ab} - \partial_a g_{bc}\big) \qquad \text{(no sum over } a\text{)} .
$$

Because $g$ is diagonal, $g_{ac}$ is zero unless $a = c$. Going through the cases: if $a$, $b$ and $c$ are all different, every term contains an off-diagonal entry and vanishes. If $b = a$ ($c$ arbitrary):

$$
\Gamma^a{}_{ac} = \frac{1}{2g_{aa}}\big(\partial_a g_{ac} + \partial_c g_{aa} - \partial_a g_{ac}\big) = \frac{\partial_c g_{aa}}{2 g_{aa}} = \partial_c \ln s_a
$$

(the first and third terms cancel; what remains is the logarithmic rate; the case $c = a$ gives the same by the symmetry in $b$ and $c$). If $b = c \ne a$:

$$
\Gamma^a{}_{bb} = \frac{1}{2g_{aa}}\big(\partial_b g_{ab} + \partial_b g_{ab} - \partial_a g_{bb}\big) = -\frac{\partial_a g_{bb}}{2 g_{aa}}
$$

($g_{ab} = 0$ for $b \ne a$). Since the metric depends only on $x_4$ and $x_8$, the nonzero entries are (listing $\Gamma^a{}_{bc}$ with $b$ not after $c$, because the symbol is symmetric in $b$ and $c$):

| entries | value | how many |
| --- | --- | --- |
| $\Gamma^a{}_{a4}$, $a = 1, 2, 3$ | $a_4'$ | 3 |
| $\Gamma^a{}_{4a}$, $a = 5, 6, 7$ | $-a_4'$ | 3 |
| $\Gamma^a{}_{a8}$, $a = 1, 2, 3, 5, 6, 7$ | $H\cot z$ | 6 |
| $\Gamma^8{}_{88}$ | $-6H/(\sin z\cos z)$ | 1 |
| $\Gamma^4{}_{bb}$, $b = 1, 2, 3$ | $a_4'\, e^{2a_4}\sin^{1/3} z$ | 3 |
| $\Gamma^4{}_{bb}$, $b = 5, 6, 7$ | $a_4'\, e^{-2a_4}\sin^{1/3} z$ | 3 |
| $\Gamma^8{}_{bb}$, $b = 1, 2, 3$ | $-H e^{2a_4}\sin^{1/3} z\, \tan z$ | 3 |
| $\Gamma^8{}_{bb}$, $b = 5, 6, 7$ | $+H e^{-2a_4}\sin^{1/3} z\, \tan z$ | 3 |

which makes $3 + 3 + 6 + 1 + 3 + 3 + 3 + 3 = 25$ entries. Two of them worked out: $\Gamma^4{}_{11} = -\partial_4 g_{11}/(2 g_{44}) = -2a_4' g_{11}/(2 \cdot (-1)) = a_4' g_{11}$ (the derivative of $e^{2a_4}$ is $2a_4' e^{2a_4}$); and

$$
\Gamma^8{}_{11} = -\frac{\partial_8 g_{11}}{2 g_{88}} = -\frac{e^{2a_4} \cdot \frac13 \sin^{-2/3} z \cos z \cdot 6H}{2\cot^2 z}
$$

(the case formula; the power rule and the chain rule for $\sin^{1/3} z$);

$$
\Gamma^8{}_{11} = -H e^{2a_4} \sin^{-2/3} z\, \cos z\, \frac{\sin^2 z}{\cos^2 z} = -H e^{2a_4}\sin^{1/3} z\, \tan z
$$

($\frac13 \cdot 6H/2 = H$ and $1/\cot^2 z = \sin^2 z/\cos^2 z$; then $\sin^{-2/3} z \sin^2 z = \sin^{4/3} z = \sin^{1/3} z \cdot \sin z$ and $\sin z/\cos z = \tan z$). The extra-time entries $\Gamma^8{}_{55}$ have the opposite sign because $g_{55}$ carries the minus sign of a time-like direction. Notebook 02c, In [12], computes all $8 \times 36 = 288$ entries with $b$ not after $c$ from the formula, finds exactly 25 nonzero ones and compares each with the Revision record (COMPUTED: reproduces `Revision/gkd_lovelock/results/curvature.json`, key `christoffelNonzero_b_le_c`).

### 2.20 Example: partial derivatives of a model function and of the author's metric

Notebook 02c carries out Sections 2.18 and 2.19. It differentiates $f = x^2\sin y$ with sympy, checks Schwarz's theorem, draws the level curves with the gradient arrows and checks that the gradient is perpendicular to them and points uphill, draws two slices with their tangent lines, measures the orders and the rounding limits of three finite-difference formulas, checks the chain rule for $z = 6Hx_8$, and then reads the author's metric from the Revision record and computes its rates along $x_4$ and $x_8$, the volume factor $\cos z$, Jacobi's formula and all 25 Christoffel entries. It ends with ALL 17 CHECKS PASSED (notebook 02c).

<!-- NOTEBOOK 02c -->

### 2.23 Line-by-line walk-through of Notebook 02c

The notebook has thirteen code cells, In [1] to In [13]. A quoted line `...)` stands for the rest of a figure caption, which Section 2.22 prints in full under its figure.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 2.21; its code is the set-up code of Notebook 02a explained in Section 2.11, with `NOTEBOOK_ID = "02c"`. It prints Set-up of notebook 02c complete: repository folder found, helpers defined.

**In [2], packages and symbols.**

```python
import math  # functions of single numbers

import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra and calculus with symbols

BLUE, ORANGE, AQUA, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7"
GREY, BLACK = "#8a8986", "#000000"
x, y = sp.symbols("x y", real=True)  # the two variables of the first example
say("Packages imported; symbols x and y defined.")
```

The packages and the colours as in Notebook 02b, and two sympy symbols $x$ and $y$, declared real (so that sympy may use rules that hold for real numbers only).

**In [3], partial derivatives with sympy.**

```python
f = x ** 2 * sp.sin(y)
f_x = sp.diff(f, x)  # hold y fixed
f_y = sp.diff(f, y)  # hold x fixed
f_xy = sp.diff(f, x, y)  # first x, then y
f_yx = sp.diff(f, y, x)  # first y, then x
```

`f` is the expression $x^2\sin y$. `sp.diff(f, x)` differentiates with respect to $x$ and treats every other symbol as a constant, which is exactly the definition of the partial derivative of Section 2.18. `sp.diff(f, x, y)` differentiates first with respect to $x$ and then with respect to $y$; `sp.diff(f, y, x)` in the other order.

```python
say(f"df/dx = {f_x},  df/dy = {f_y}")
say(f"d2f/dxdy = {f_xy},  d2f/dydx = {f_yx}")
check(sp.simplify(f_x - 2 * x * sp.sin(y)) == 0
      and sp.simplify(f_y - x ** 2 * sp.cos(y)) == 0,
      "df/dx = 2 x sin y and df/dy = x^2 cos y")
check(sp.simplify(f_xy - f_yx) == 0 and sp.simplify(f_xy - 2 * x * sp.cos(y)) == 0,
      "the mixed derivatives agree (Schwarz): both are 2 x cos y")
```

The four derivatives are printed (`2*x*sin(y)`, `x**2*cos(y)`, and `2*x*cos(y)` twice), and two checks compare them with the hand calculation of Section 2.18: `sp.simplify` reduces the difference to its simplest form, which must be 0. The second check is Schwarz's theorem for this example.

```python
X0, Y0 = 1.2, 0.7  # the point at which we evaluate
at_point = {x: X0, y: Y0}
for label, expression in (("f", f), ("df/dx", f_x), ("df/dy", f_y),
                          ("d2f/dxdy", f_xy)):
    report(f"{label} at (1.2, 0.7)", f"{float(expression.subs(at_point)):.12f}")
```

The dictionary `at_point` tells `.subs` to put $x = 1.2$ and $y = 0.7$ into an expression; `float` turns the result into an ordinary number. The RESULT lines give $f = 0.927673469622$, $\partial f/\partial x = 1.546122449370$, $\partial f/\partial y = 1.101372749690$ and $\partial^2 f/\partial x\partial y = 1.835621249483$ (COMPUTED; for example $2 \cdot 1.2 \cdot \cos 0.7 = 1.8356$).

**In [4], level curves and gradient arrows.**

```python
F = sp.lambdify((x, y), f, "numpy")  # f as a numpy function
FX = sp.lambdify((x, y), f_x, "numpy")
FY = sp.lambdify((x, y), f_y, "numpy")
```

`sp.lambdify` turns a sympy expression into an ordinary Python function of $(x, y)$ that computes with numpy, so that it can be applied to whole arrays of points at once: `F` computes $f$, `FX` and `FY` its two partial derivatives.

```python
xs = np.linspace(-2.0, 2.0, 201)
ys = np.linspace(0.0, 2.0 * np.pi, 201)
XX, YY = np.meshgrid(xs, ys)  # all grid points as two 2-dimensional arrays
```

201 values of $x$ from $-2$ to 2 and 201 values of $y$ from 0 to $2\pi$. `np.meshgrid` makes the grid of all $201 \times 201$ pairs: `XX` holds the $x$ of every grid point and `YY` its $y$, both as tables of 201 rows and 201 columns.

```python
fig, ax = plt.subplots(figsize=(7.0, 5.2))
bands = ax.contourf(XX, YY, F(XX, YY), levels=17, cmap="RdBu_r")  # coloured bands
ax.contour(XX, YY, F(XX, YY), levels=17, colors=BLACK, linewidths=0.4)
fig.colorbar(bands, ax=ax, label="$f(x, y) = x^2 \\sin y$")
```

`contourf` fills the regions between 17 levels of $f$ with colours from the colour map `"RdBu_r"` (red for large, blue for small values; `_r` reverses the map); `contour` draws the level curves themselves as thin black lines; `colorbar` adds the scale that translates colours into values.

```python
xq, yq = np.meshgrid(np.linspace(-1.8, 1.8, 10), np.linspace(0.3, 6.0, 12))  # coarse
# an arrow (df/dx, df/dy) at every coarse grid point; scale=40 shortens all arrows
ax.quiver(xq, yq, FX(xq, yq), FY(xq, yq), color=BLACK, scale=40, width=0.004)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Level curves of $f = x^2 \\sin y$ and its gradient arrows")
save_figure(fig, "level_curves_gradient",
            "A map of the function $f(x, y) = x^2 \\sin y$ for $x$ from $-2$ to $2$ "
            ...)
```

A coarse grid of $10 \times 12$ points carries the gradient arrows: `quiver` draws at each point $(x, y)$ an arrow with the components $(\partial f/\partial x, \partial f/\partial y)$, all shortened by the same factor (`scale=40`) so that they fit; `width` sets their thickness. Labels and the saved figure `02c_1_level_curves_gradient.png`. **What Figure 02c.1 shows:** every arrow points uphill, from blue towards red, and crosses the level curves at a right angle; where the level curves crowd together the arrows are long, because the slope is steep (Section 2.18).

```python
gx, gy = float(f_x.subs(at_point)), float(f_y.subs(at_point))
tangent = np.array([-gy, gx]) / math.hypot(gx, gy)  # along the level curve
step = 1e-4
change = F(X0 + step * tangent[0], Y0 + step * tangent[1]) - F(X0, Y0)
report("change of f along the level curve for a step of 1e-4", f"{change:.2e}")
check(abs(gx * tangent[0] + gy * tangent[1]) < 1e-15 and abs(change) < 1e-7,
      "the gradient is perpendicular to the level curve")
```

`gx` and `gy` are the gradient's components at $(1.2, 0.7)$. `math.hypot(gx, gy)` is the length $\sqrt{g_x^2 + g_y^2}$, so `tangent` is the unit arrow $(-g_y, g_x)/|\nabla f|$ of Section 2.18. A step of $10^{-4}$ along it changes $f$ by only $-9.58 \times 10^{-9}$ (COMPUTED), a second-order amount ($10^{-8}$ is the square of $10^{-4}$). The check requires the dot product of the gradient with this direction to vanish (up to rounding) and the change of $f$ to be below $10^{-7}$.

```python
length = math.hypot(gx, gy)  # the length |grad f| of the gradient arrow
rise = F(X0 + step * gx / length, Y0 + step * gy / length) - F(X0, Y0)
report("rise of f per unit length along the gradient, |grad f|",
       f"{rise / step:.6f}, {length:.6f}")
```

Now the second fact of Section 2.18. `length` is $|\nabla f| = \sqrt{g_x^2 + g_y^2}$, and $(g_x, g_y)/|\nabla f|$ is the unit arrow along the gradient. `rise` is the change of $f$ for a step of $10^{-4}$ along it, and `rise / step` the change per unit length. The RESULT line prints 1.898407 and $|\nabla f| = 1.898293$ (COMPUTED): along the gradient $f$ rises at the rate $|\nabla f|$, the steepest slope; the two differ by $1.1 \times 10^{-4}$, the second-order term of the step.

```python
gxq, gyq = FX(xq, yq), FY(xq, yq)  # the arrows of the figure
lengths = np.hypot(gxq, gyq)
rises = F(xq + step * gxq / lengths, yq + step * gyq / lengths) - F(xq, yq)
check(abs(rise / step / length - 1) < 1e-3 and np.all(rises > 0),
      "the gradient points uphill: f rises at the rate |grad f| along it")
```

The same test at all 120 points of the coarse grid of the figure: `gxq`, `gyq` are the components of the 120 arrows, `np.hypot` their lengths (one for each point), and `rises` the change of $f$ for a step of $10^{-4}$ along each arrow. The check requires the measured rate at $(1.2, 0.7)$ to equal $|\nabla f|$ within one part in a thousand, and every one of the 120 rises to be positive: every arrow of Figure 02c.1 points uphill.

**In [5], two slices and their slopes.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
fig.subplots_adjust(wspace=0.3)  # room between the two panels
f0 = F(X0, Y0)
x_line = np.linspace(-0.5, 2.5, 200)
left.plot(x_line, F(x_line, Y0), color=BLUE, lw=1.6,
          label="slice $f(x, 0.7)$")
left.plot(x_line, f0 + gx * (x_line - X0), "--", color=ORANGE, lw=1.2,
          label=f"slope $\\partial f/\\partial x = {gx:.4f}$")
left.set_xlabel("$x$ (with $y = 0.7$ fixed)")
```

Two panels with some room between them (`wspace`). `f0` is $f(1.2, 0.7)$. The left panel draws the slice $x \mapsto f(x, 0.7)$ and the straight line $f_0 + g_x (x - x_0)$ through the point with the slope $\partial f/\partial x$.

```python
y_line = np.linspace(-0.6, 2.4, 200)
right.plot(y_line, F(X0, y_line), color=BLUE, lw=1.6, label="slice $f(1.2, y)$")
right.plot(y_line, f0 + gy * (y_line - Y0), "--", color=ORANGE, lw=1.2,
           label=f"slope $\\partial f/\\partial y = {gy:.4f}$")
right.set_xlabel("$y$ (with $x = 1.2$ fixed)")
```

The right panel does the same for the slice $y \mapsto f(1.2, y)$ and the slope $\partial f/\partial y$.

```python
for ax in (left, right):
    ax.plot([X0 if ax is left else Y0], [f0], "o", color=BLACK, ms=6)
    ax.set_ylabel("$f$")
    ax.legend(fontsize=8)
save_figure(fig, "slices_and_slopes",
            "Two slices of $f(x, y) = x^2 \\sin y$ through the point "
            ...)
check(abs(gx - 2 * X0 * math.sin(Y0)) < 1e-15 and abs(gy - X0 ** 2 * math.cos(Y0))
      < 1e-15, "the slopes of the slices are 2 x0 sin y0 and x0^2 cos y0")
```

In each panel a black dot marks the point ($x_0$ in the left panel, $y_0$ in the right one: `X0 if ax is left else Y0` chooses); then the saved figure `02c_2_slices_and_slopes.png`, and a check that the two slopes are $2x_0\sin y_0$ and $x_0^2\cos y_0$. **What Figure 02c.2 shows:** each dashed line touches its slice at the dot: a partial derivative is the slope of a slice.

**In [6], finite differences: order and rounding.**

```python
exact_y = X0 ** 2 * math.cos(Y0)  # df/dy at the point
exact_xy = 2 * X0 * math.cos(Y0)  # d2f/dxdy at the point
h_values = np.logspace(-12, 0, 49)  # 1e-12 ... 1
```

The exact values of $\partial f/\partial y$ and $\partial^2 f/\partial x\partial y$ at the point, and 49 spacings from $10^{-12}$ to 1, equally spaced in $\log_{10} h$ (`np.logspace(-12, 0, 49)` gives $10^{-12}, 10^{-11.75}, \dots, 10^{0}$).

```python
forward = np.array([(F(X0, Y0 + h) - F(X0, Y0)) / h for h in h_values])
central = np.array([(F(X0, Y0 + h) - F(X0, Y0 - h)) / (2 * h) for h in h_values])
mixed = np.array([(F(X0 + h, Y0 + h) - F(X0 + h, Y0 - h) - F(X0 - h, Y0 + h)
                   + F(X0 - h, Y0 - h)) / (4 * h * h) for h in h_values])
```

The three formulas of Section 2.18, evaluated for every spacing: the forward and the central difference in $y$, and the central formula for the mixed derivative.

```python
err = {"forward": np.abs(forward - exact_y), "central": np.abs(central - exact_y),
       "mixed": np.abs(mixed - exact_xy)}
RANGES = {"forward": (1e-5, 1e-2), "central": (1e-3, 1e-1), "mixed": (1e-2, 1e-1)}
slope_of = {}
for name, (low, high) in RANGES.items():
    part = (h_values >= low) & (h_values <= high)
    slope_of[name], _ = np.polyfit(np.log10(h_values[part]),
                                   np.log10(err[name][part]), 1)
    best = int(np.argmin(err[name]))
    report(f"{name}: slope {slope_of[name]:.3f}, best h", f"{h_values[best]:.1e} "
           f"(error {err[name][best]:.1e})")
```

`err` holds the three error arrays. `RANGES` gives, for each formula, the range of spacings where the truncation error clearly dominates (larger than the rounding error, but small enough for the leading Taylor term to rule); `part` selects those spacings, and `np.polyfit` fits the slope there, as in Notebook 02a. `np.argmin` finds the spacing with the smallest error. The RESULT lines: forward slope 1.000, best $h = 1.0 \times 10^{-8}$ (error $1.1 \times 10^{-9}$); central slope 2.000, best $h = 1.8 \times 10^{-6}$ (error $5.3 \times 10^{-12}$); mixed slope 2.000, best $h = 5.6 \times 10^{-5}$ (error $1.4 \times 10^{-9}$) (COMPUTED; compare the estimates of Section 2.18).

```python
fig, ax = plt.subplots(figsize=(7.0, 5.0))
styles = {"forward": (ORANGE, "s", "forward difference, $\\partial f/\\partial y$"),
          "central": (BLUE, "o", "central difference, $\\partial f/\\partial y$"),
          "mixed": (AQUA, "^", "central mixed, $\\partial^2 f/\\partial x "
                               "\\partial y$")}
for name, (color, marker, label) in styles.items():
    shown = err[name] > 0  # an exact zero cannot be drawn on a log axis
    ax.loglog(h_values[shown], err[name][shown], marker=marker, color=color, ms=4,
              lw=1.0, label=label)
```

A colour, a marker and a legend text for each formula; each error curve is drawn on log-log axes, leaving out errors that happen to be exactly zero.

```python
ax.loglog(h_values, 2.2e-16 / h_values, ":", color=BLACK, lw=1.0,
          label="rounding scale $\\epsilon / h$")
ax.loglog(h_values, 2.2e-16 / h_values ** 2, "-.", color=GREY, lw=1.0,
          label="rounding scale $\\epsilon / h^2$ (mixed)")
ax.set_ylim(1e-14, 10.0)
ax.set_xlabel("spacing $h$")
ax.set_ylabel("error of the approximation")
ax.set_title("Finite differences at $(1.2, 0.7)$: truncation against rounding")
ax.legend(loc="lower left", fontsize=8)
save_figure(fig, "finite_differences",
            "The error of three finite-difference approximations at the point "
            ...)
```

The two rounding scales $\epsilon/h$ (dotted) and $\epsilon/h^2$ (dash-dotted, for the mixed formula, which divides by $h^2$), labels and the saved figure `02c_3_finite_differences.png`. **What Figure 02c.3 shows:** read from the right, the errors fall along straight lines of slope 1 (forward) and 2 (central, mixed); read from the left, they follow the rising rounding lines; each curve has its lowest point where the two effects balance, near $10^{-8}$, $10^{-6}$ and $10^{-4}$.

```python
check(abs(slope_of["forward"] - 1) < 0.05 and abs(slope_of["central"] - 2) < 0.05
      and abs(slope_of["mixed"] - 2) < 0.05,
      "measured orders: forward 1, central 2, mixed central 2")
check(err["central"].min() < 1e-10 < err["forward"].min() < 1e-7,
      "best central error < 1e-10 < best forward error < 1e-7")
```

Two checks: the measured orders are 1, 2 and 2 within 0.05; the best central error is below $10^{-10}$, which is below the best forward error, which is below $10^{-7}$ (a higher order buys accuracy even at the best spacing).

**In [7], the chain rule with $z = 6Hx_8$.**

```python
x4, x8 = sp.symbols("x4 x8", real=True)  # the time and the hidden coordinate
H = sp.symbols("H", positive=True)  # the author's constant H > 0
zs = sp.symbols("z", positive=True)  # z = 6 H x8 as a symbol of its own
```

Symbols for the time $x_4$, the hidden coordinate $x_8$, the author's constant $H$ (positive) and $z$ as a variable of its own.

```python
through_x8 = sp.diff(sp.cot(6 * H * x8) ** 2, x8)  # differentiate in x8 directly
through_z = 6 * H * sp.diff(sp.cot(zs) ** 2, zs).subs(zs, 6 * H * x8)  # chain rule
say(f"d/dx8 cot(6 H x8)^2 = {sp.simplify(through_x8)}")
check(sp.simplify(through_x8 - through_z) == 0,
      "chain rule: d/dx8 of cot(6 H x8)^2 = 6 H times d/dz of cot(z)^2")
```

`through_x8` differentiates $\cot^2(6Hx_8)$ directly with respect to $x_8$; `through_z` differentiates $\cot^2 z$ with respect to $z$, puts $z = 6Hx_8$ back in with `.subs`, and multiplies by $6H$, as the chain rule of Section 2.19 says. The printed derivative is `-12*H*cot(6*H*x8)/sin(6*H*x8)**2`, and the check confirms that both ways agree.

```python
z0 = 0.6  # the point z0 and the matching x8 = z0/6 (H = 1)
slope_z = -2.0 * math.cos(z0) / math.sin(z0) ** 3  # d/dz cot^2 z = -2 cot z / sin^2 z
```

At $z_0 = 0.6$ the slope of $\cot^2 z$ is $-2\cot z_0/\sin^2 z_0 = -2\cos z_0/\sin^3 z_0$ (Section 2.19).

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
z_line = np.linspace(0.35, 1.5, 300)
left.plot(z_line, 1 / np.tan(z_line) ** 2, color=BLUE, lw=1.6,
          label="$\\cot^2 z$")
left.plot(z_line, 1 / math.tan(z0) ** 2 + slope_z * (z_line - z0), "--",
          color=ORANGE, label=f"tangent, slope {slope_z:.3f}")
left.set_xlabel("$z$")
```

The left panel draws $\cot^2 z = 1/\tan^2 z$ for $z$ from 0.35 to 1.5 and its tangent line at $z_0$.

```python
x8_line = z_line / 6.0
right.plot(x8_line, 1 / np.tan(6 * x8_line) ** 2, color=BLUE, lw=1.6,
           label="$\\cot^2(6 H x_8)$, $H = 1$")
right.plot(x8_line, 1 / math.tan(z0) ** 2 + 6 * slope_z * (x8_line - z0 / 6), "--",
           color=ORANGE, label=f"tangent, slope $6 \\times$ {slope_z:.3f}")
right.set_xlabel("$x_8$ (units $1/H$)")
```

The right panel draws the same function against $x_8 = z/6$ (with $H = 1$) and the tangent line with 6 times the slope, through the matching point $x_8 = 0.1$.

```python
for ax, where in ((left, z0), (right, z0 / 6)):
    ax.plot([where], [1 / math.tan(z0) ** 2], "o", color=BLACK, ms=6)
    ax.set_ylim(0.0, 6.0)
    ax.set_ylabel("$g_{88}$ (pure number)")
    ax.legend(fontsize=8)
save_figure(fig, "chain_rule",
            "The chain rule for the author's hidden coordinate. Left: "
            ...)
```

A dot at the point in each panel, the vertical range, labels, and the saved figure `02c_4_chain_rule.png`. **What Figure 02c.4 shows:** the right curve is the left one squeezed sideways by the factor 6, and both dashed lines touch their curves; the right slope is 6 times the left one: $\partial_8 = 6H\, d/dz$.

**In [8], the author's metric from the Revision record.**

```python
CURVATURE = "Revision/gkd_lovelock/results/curvature.json"
record = json.loads(repository_file(CURVATURE).read_text(encoding="utf-8"))
a4 = sp.Function("a4")  # the unknown function a4(x4) of the metric
NAMES = {"a4": a4, "x4": x4, "x8": x8, "H": H, "Sin": sp.sin, "Cos": sp.cos,
         "Cot": sp.cot}
```

The cell reads the Revision record of the curvature program. `sp.Function("a4")` makes an unknown function $a_4$, so that $a_4(x_4)$ can be differentiated without knowing its form. `NAMES` tells the translator below which sympy object each name of the record stands for.

```python
def from_record(text):
    """A Wolfram-Language text of the record as a sympy expression."""
    text = text.replace("Derivative[1][a4][x4]", "Derivative(a4(x4), x4)")
    text = text.replace("[", "(").replace("]", ")").replace("^", "**")
    return sp.parse_expr(text, local_dict=NAMES)
```

The record writes its formulas in the notation of the Wolfram Language: `E^(...)` for $e^{\dots}$, `Sin[...]` for $\sin(\dots)$, `Derivative[1][a4][x4]` for $a_4'$. `from_record` translates such a text: first the derivative, then square brackets into round ones and `^` into Python's `**`; `sp.parse_expr` reads the result as a sympy expression with the names of `NAMES` (sympy knows `E` as $e$ by itself).

```python
def tidy(expression):
    """Write cot and tan as quotients of cos and sin (helps sympy simplify)."""
    expression = expression.replace(sp.cot, lambda u: sp.cos(u) / sp.sin(u))
    return expression.replace(sp.tan, lambda u: sp.sin(u) / sp.cos(u))


def same(first, second):
    """True when sympy simplifies first - second to zero."""
    return sp.simplify(tidy(first - second)) == 0
```

`tidy` replaces every $\cot u$ by $\cos u/\sin u$ and every $\tan u$ by $\sin u/\cos u$ (a `lambda` is a one-line function without a name); with only sines and cosines left, `sp.simplify` finds cancellations more reliably. `same` decides whether two expressions are equal by simplifying their difference to 0.

```python
COORDS = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
X = [sp.Symbol(name, real=True) for name in COORDS]
X[3], X[7] = x4, x8  # the metric depends on these two only
z = 6 * H * x8
third = sp.Rational(1, 3)
```

The eight coordinate names and a list of eight symbols; positions 3 and 7 (counted from 0) are replaced by the symbols $x_4$ and $x_8$ already in use. `z` is now the expression $6Hx_8$, and `third` the exact fraction $1/3$.

```python
BY_HAND = ([sp.exp(2 * a4(x4)) * sp.sin(z) ** third] * 3 + [sp.Integer(-1)]
           + [-sp.exp(-2 * a4(x4)) * sp.sin(z) ** third] * 3 + [sp.cot(z) ** 2])
G_RECORD = [from_record(text) for text in record["metricDiagonal"]]
for name, entry in zip(COORDS, G_RECORD):
    say(f"g_{name[1]}{name[1]} = {entry}")
```

`BY_HAND` is the diagonal of the author's metric typed in by hand: a list times 3 repeats it three times, and `+` joins lists, giving the eight entries of Section 2.19. `G_RECORD` translates the record's eight texts; the loop prints them (`name[1]` is the digit of the coordinate name), from `g_11 = exp(2*a4(x4))*sin(6*H*x8)**(1/3)` to `g_88 = cot(6*H*x8)**2`.

```python
check(record["coordinates"] == COORDS
      and all(same(a, b) for a, b in zip(G_RECORD, BY_HAND)),
      "the record's metric equals the author's metric typed in by hand",
      record=f"{CURVATURE}, key metricDiagonal")
G = sp.diag(*G_RECORD)  # the metric as an 8 x 8 diagonal sympy matrix
```

The check requires the record's coordinate list to be $x_1, \dots, x_8$ and every entry to equal the hand-typed one (COMPUTED: reproduces `Revision/gkd_lovelock/results/curvature.json`, key `metricDiagonal`). `sp.diag(*G_RECORD)` builds the $8 \times 8$ diagonal matrix with these entries (`*` unpacks the list into eight arguments).

**In [9], the rates along $x_4$ and $x_8$.**

```python
rate4 = [sp.simplify(sp.diff(G[a, a], x4) / (2 * G[a, a])) for a in range(8)]
rate8 = [sp.simplify(tidy(sp.diff(G[a, a], x8) / (2 * G[a, a]))) for a in range(8)]
da4 = sp.diff(a4(x4), x4)  # a4', the derivative of a4
```

For each of the eight diagonal entries `G[a, a]` the logarithmic rates $\partial_4 g_{aa}/(2g_{aa})$ and $\partial_8 g_{aa}/(2g_{aa})$ of Section 2.19. `da4` is the symbol for $a_4'$.

```python
expected4 = [da4] * 3 + [0] + [-da4] * 3 + [0]
expected8 = [H * sp.cot(z)] * 3 + [0] + [H * sp.cot(z)] * 3 + [-6 * H / (sp.sin(z)
                                                                      * sp.cos(z))]
for a, name in enumerate(COORDS):
    say(f"{name}: d4 ln s = {rate4[a]},  d8 ln s = {rate8[a]}")
```

The expected rates of Section 2.19, and a printout of the computed ones. sympy writes $H\cot z$ as `H/tan(6*H*x8)` and $-6H/(\sin z\cos z)$ as `-12*H/sin(12*H*x8)`; they are equal because $\sin 2z = 2\sin z\cos z$.

```python
check(all(same(r, e) for r, e in zip(rate4, expected4))
      and all(same(r, e) for r, e in zip(rate8, expected8)),
      "the rates a4', -a4', H cot z and -6H/(sin z cos z) of section 4")
check(sp.simplify(sum(rate4)) == 0, "the eight rates along x4 add up to zero")
```

The first check compares all sixteen rates with the expected ones; the second confirms that the eight rates along $x_4$ add up to zero (Section 2.19). (The check's text says "section 4" because it refers to section 4 of the notebook.)

```python
rates_now = [float(r.subs(da4, 1)) for r in rate4]
fig, ax = plt.subplots()
colors = [BLUE] * 3 + [GREY] + [ORANGE] * 3 + [GREY]
ax.bar(range(8), rates_now, color=colors, width=0.6)
ax.axhline(0.0, color=BLACK, lw=0.8)
ax.set_xticks(range(8), [f"$x_{k}$" for k in range(1, 9)])
```

On the history $a_4 = AHx_4$ with $A = H = 1$ we have $a_4' = 1$; `.subs(da4, 1)` puts this in. `ax.bar` draws a bar for each direction (blue for 3-space, orange for the extra times, grey for $x_4$ and $x_8$), and `set_xticks` labels the positions 0 to 7 with $x_1$ to $x_8$.

```python
for k, value in enumerate(rates_now):
    ax.text(k, value + (0.06 if value >= 0 else -0.14), f"{value:+.0f}",
            ha="center", fontsize=9)
ax.set_ylim(-1.4, 1.4)
ax.set_xlabel("direction")
ax.set_ylabel("$\\partial_4 \\ln s_a$ (units $H$)")
ax.set_title("Growth rate of each scale factor along the time $x_4$ ($A = H = 1$)")
save_figure(fig, "rates_along_x4",
            "The rate $\\partial_4 \\ln s_a$ at which the scale factor $s_a$ of "
            ...)
```

Each bar gets its value written just above (positive) or below (negative) it, then the axis range, labels and the saved figure `02c_5_rates_along_x4.png`. **What Figure 02c.5 shows:** three bars at $+1$ (3-space inflates), three at $-1$ (the extra times deflate exponentially), two at 0; the bars cancel, so the 7-volume of space and extra times does not change with time.

**In [10], the rates along the hidden coordinate.**

```python
rate_sum8 = sp.simplify(tidy(sum(rate8)))
check(same(rate_sum8, -6 * H * sp.tan(z)),
      "the eight rates along x8 add up to d8 ln cos z = -6 H tan z")
```

The sum of the eight rates along $x_8$ must be $-6H\tan z$, the rate of $\cos z$ (Section 2.19).

```python
z_line = np.linspace(0.05, np.pi / 2 - 0.05, 400)
fig, ax = plt.subplots()
ax.plot(z_line, 1 / np.tan(z_line), color=BLUE, lw=1.6,
        label="$H \\cot z$: directions $x_1, x_2, x_3$ and $x_5, x_6, x_7$")
ax.plot(z_line, -6 / (np.sin(z_line) * np.cos(z_line)), "--", color=VIOLET, lw=1.6,
        label="$-6H/(\\sin z \\cos z)$: direction $x_8$")
ax.plot(z_line, -6 * np.tan(z_line), "-.", color=ORANGE, lw=1.6,
        label="sum of all eight $= -6 H \\tan z$")
```

With $H = 1$, on $0.05 < z < \pi/2 - 0.05$ (the ends are left out because the rates become infinite there), the three rates are drawn.

```python
ax.axhline(0.0, color=BLACK, lw=0.8)
ax.set_ylim(-60.0, 20.0)
ax.set_xlabel("$z = 6 H x_8$")
ax.set_ylabel("$\\partial_8 \\ln s_a$ (units $H$)")
ax.set_title("Rates of the scale factors along the hidden coordinate ($H = 1$)")
ax.legend(loc="lower left", fontsize=8)
save_figure(fig, "rates_along_x8",
            "The rates $\\partial_8 \\ln s_a$ at which the scale factors change "
            ...)
```

Axis range, labels and the saved figure `02c_6_rates_along_x8.png`. **What Figure 02c.6 shows:** the 3-space and extra-time factors grow along $x_8$ near $z = 0$ and level off near $z = \pi/2$ (where $\cot z = 0$); the hidden factor $\cot z$ shrinks everywhere, fastest at both ends; the sum $-6H\tan z$ is the rate of the volume factor $\cos z$, which falls to zero at $z = \pi/2$.

**In [11], the volume factor and Jacobi's formula.**

```python
det_g = sp.simplify(tidy(G.det()))  # the product of the eight entries
say(f"det g = {det_g}")
sqrt_record = from_record(record["sqrtAbsDetG"])
say(f"sqrtAbsDetG of the record = {sqrt_record}")
check(same(det_g, sp.cos(z) ** 2) and same(sqrt_record, sp.cos(z)),
      "det g = cos(z)^2 and the record's sqrt|det g| = sin z cot z = cos z",
      record=f"{CURVATURE}, key sqrtAbsDetG")
```

`G.det()` is the determinant; sympy simplifies it to $\cos^2(6Hx_8)$, and the record's entry `sqrtAbsDetG` reads $\sin(6Hx_8)\cot(6Hx_8)$ (the printed lines show both as sympy writes them). The check confirms $\det g = \cos^2 z$ and $\sqrt{|\det g|} = \sin z\cot z = \cos z$ (COMPUTED: reproduces `Revision/gkd_lovelock/results/curvature.json`, key `sqrtAbsDetG`).

```python
A4REPORT = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
a4_report = json.loads(repository_file(A4REPORT).read_text(encoding="utf-8"))
verdict = [c["verdict"] for c in a4_report["checks"]
           if c["name"] == "sqrt_abs_det_g_is_cos_z"]
check(verdict == ["PASS"] and sp.diff(sqrt_record, x4) == 0,
      "sqrt|det g| = cos z does not depend on x4 (inflation and deflation cancel)",
      record=f"{A4REPORT}, check sqrt_abs_det_g_is_cos_z")
```

The cell reads the Wolfram report of the $a_4$ field equations and collects the verdict of its check `sqrt_abs_det_g_is_cos_z` (a list comprehension with an `if` keeps only the matching check). The check requires that verdict to be PASS and the derivative of $\sqrt{|\det g|}$ with respect to $x_4$ to be exactly 0 (COMPUTED: reproduces `Revision/field_equations_a4/reports/wolfram-a4-report.json`, check `sqrt_abs_det_g_is_cos_z`).

```python
jacobi = [same(sp.diff(sqrt_record, c),
               sp.Rational(1, 2) * sqrt_record * (G.inv() * G.diff(c)).trace())
          for c in (x4, x8)]
check(all(jacobi), "Jacobi's formula for the derivative of sqrt|det g| (x4 and x8)")
```

Jacobi's formula of Section 2.19 for $c = x_4$ and $c = x_8$: `G.inv()` is the inverse matrix, `G.diff(c)` the matrix of the derivatives of the entries, `*` the matrix product and `.trace()` the sum of the diagonal entries.

**In [12], all 25 Christoffel entries.**

```python
computed = {}
for a in range(8):
    for b in range(8):
        for c in range(b, 8):
            value = (sp.diff(G[a, c], X[b]) + sp.diff(G[a, b], X[c])
                     - sp.diff(G[b, c], X[a])) / (2 * G[a, a])
            value = sp.simplify(tidy(value))
            if value != 0:
                computed[(COORDS[a], COORDS[b], COORDS[c])] = value
```

Three nested loops run over $a$ (8 values), $b$ (8 values) and $c$ from $b$ to 7, that is over the $8 \times 36 = 288$ entries $\Gamma^a{}_{bc}$ with $b$ not after $c$. Each is computed from the formula of Section 2.19 (the derivative with respect to the coordinate `X[b]`, and so on), simplified, and stored under the key (a, b, c) of coordinate names if it is not zero.

```python
listed = {(e["a"], e["b"], e["c"]): from_record(e["value"])
          for e in record["christoffelNonzero_b_le_c"]}
for key in [("x1", "x1", "x4"), ("x5", "x4", "x5"), ("x8", "x1", "x1"),
            ("x8", "x8", "x8")]:
    say(f"Gamma^{key[0]}_({key[1]} {key[2]}) = {computed[key]}")
```

`listed` translates the record's list of nonzero entries into the same form. Four entries are printed: $\Gamma^1{}_{14} = a_4'$, $\Gamma^5{}_{45} = -a_4'$, $\Gamma^8{}_{11} = -H e^{2a_4}\sin^{4/3} z/\cos z$ (which is $-He^{2a_4}\sin^{1/3}z\tan z$ of Section 2.19) and $\Gamma^8{}_{88} = -12H/\sin(12Hx_8)$.

```python
report("nonzero entries computed / listed in the record",
       f"{len(computed)} / {len(listed)}")
check(sorted(computed) == sorted(listed)
      and all(same(computed[k], listed[k]) for k in listed),
      "all 25 nonzero Christoffel entries equal those of the record",
      record=f"{CURVATURE}, key christoffelNonzero_b_le_c")
```

25 entries are computed and 25 are listed. The check requires the same keys (`sorted` puts the keys of a dictionary in order) and equal values for every key (COMPUTED: reproduces `Revision/gkd_lovelock/results/curvature.json`, key `christoffelNonzero_b_le_c`).

**In [13], the last check.**

```python
names = ["level_curves_gradient", "slices_and_slopes", "finite_differences",
         "chain_rule", "rates_along_x4", "rates_along_x8"]
present = [output_file(f"{FIGURE_FOLDER}/02c_{k}_{name}.png").is_file()
           for k, name in enumerate(names, 1)]
check(all(present), f"all {len(names)} figure files of notebook 02c exist")
all_checks_passed()
```

As in Notebook 02a: the six figure files must exist; the last line is ALL 17 CHECKS PASSED (notebook 02c). The 17 checks are: 2 in In [3], 2 in In [4], 1 in In [5], 2 in In [6], 1 in In [7], 1 in In [8], 2 in In [9], 1 in In [10], 3 in In [11], 1 in In [12] and 1 in In [13].

### 2.24 Two first-order equations, the Prüfer angle and Newton's method

This section prepares the last notebook, which rewrites the shooting method of the Revision Kohn-Sham solver. We use the solver's equations only as mathematics here; where they come from, and what their levels mean physically, is the subject of Chapters 14 and 15.

**The equations.** The Revision record `Revision/kohn_sham/ks-theory.json` gives the Kohn-Sham equation of one two-component block in a real form (key `blockEquation.realForm`): an orbital is described by two real functions $a(y)$ and $b(y)$ of the **hidden coordinate** $y$, which is the record's coordinate along $x_8$, $y = \ln(\sin z)/(6H)$ (key `geometry.hiddenCoordinate`; $y = 0$ is the end of the patch $z = \pi/2$, called the **brane**, and $y \to -\infty$ is $z \to 0$). The record's general block contains a mass $M$, a momentum $k$ in 3-space, potentials and a sign $j = \pm 1$ of the block type. We take the simplest case: constant mass $M$, no 3-space momentum ($k = 0$), no potential, and $j = +1$. Then the equations are

$$
a' = M a - \varepsilon b, \qquad b' = \varepsilon a - M b, \qquad -L \le y \le 0,
$$

where the prime is now $d/dy$ and $\varepsilon$ is the unknown energy. The interval is cut off at $y = -L$, the **tip**. The conditions are

$$
b(-L) = 0 \ \ \text{(tip)}, \qquad b(0) = 0 \ \ \text{(even orbitals)} \quad \text{or} \quad a(0) = 0 \ \ \text{(odd orbitals)} .
$$

*Status.* The tip condition is a choice of the model (the record's status: "chosen (regular tip)"); the brane conditions follow from a mirror symmetry of the model across the brane that the record labels ASSUMED (key `boundaryConditions.brane.status`). Everything below is exact mathematics for these equations under these conditions. The record's values are $M = m = 1$, $H = 1$, $L = 3$ (units with $m = H = 1$: energies in units of the mass $m$, lengths along $y$ in units of $1/H$); the program also checks $L = 2$ and $M = 2$.

**The exact levels.** We eliminate $b$.

$$
b = \frac{M a - a'}{\varepsilon} \qquad (\varepsilon \ne 0)
$$

(solve the first equation for $b$);

$$
b' = \frac{M a' - a''}{\varepsilon}
$$

(differentiate; $M$ and $\varepsilon$ are constants);

$$
\frac{M a' - a''}{\varepsilon} = \varepsilon a - M\, \frac{M a - a'}{\varepsilon}
$$

(insert both into the second equation);

$$
M a' - a'' = \varepsilon^2 a - M^2 a + M a'
$$

(multiply by $\varepsilon$);

$$
a'' = (M^2 - \varepsilon^2)\, a
$$

(cancel $M a'$ on both sides and change all signs). The condition $b = 0$ at a point means $M a - a' = 0$ there (because $b = (Ma - a')/\varepsilon$).

*Case $|\varepsilon| > M$.* Put $p = \sqrt{\varepsilon^2 - M^2} > 0$; then $a'' = -p^2 a$, and $a = \cos(py + \varphi)$ up to a constant factor, with a phase $\varphi$.

- Even orbitals: $M a - a' = 0$ at $y = 0$ and at $y = -L$. With $a = \cos(py + \varphi)$ this reads $M\cos(py + \varphi) + p \sin(py + \varphi) = 0$, that is $\tan(py + \varphi) = -M/p$ at both points ($\cos(py + \varphi)$ cannot vanish there, since then the left side would be $\pm p \ne 0$). The tangent repeats itself after $\pi$ and takes each value once per period, so the two arguments $\varphi$ and $-pL + \varphi$ differ by a whole multiple of $\pi$: $pL = n\pi$ with $n = 1, 2, \dots$ Hence $\varepsilon = \pm\sqrt{M^2 + (n\pi/L)^2}$.
- Odd orbitals: $a(0) = 0$ makes $a$ a multiple of $\sin(py)$. The tip condition $M a(-L) - a'(-L) = 0$ becomes $M\sin(-pL) - p\cos(-pL) = 0$, that is $-M\sin(pL) - p\cos(pL) = 0$ (the sine is odd, the cosine even), or

$$
\tan(pL) = -\frac{p}{M} .
$$

This transcendental equation has one root $p_n$ on each interval $(n + \frac12)\pi/L < p < (n + 1)\pi/L$, $n = 0, 1, 2, \dots$ (there $\tan(pL)$ runs through all negative values once), and each root gives the two odd levels $\pm\sqrt{M^2 + p_n^2}$.

*Case $\varepsilon = 0$.* The equations separate: $a' = Ma$ and $b' = -Mb$. With $b(-L) = 0$ the solution of $b' = -Mb$ is $b = 0$ everywhere (the uniqueness theorem of Section 2.2), and $a = e^{M(y + L)}$, a multiple of $e^{My}$. This is an even orbital ($b(0) = 0$) with the energy exactly 0, the **zero mode**; an odd one would need $a(0) = 0$, which $e^{M(y+L)}$ never is.

*Case $0 < |\varepsilon| \le M$: no level.* For $0 < |\varepsilon| < M$ put $q = \sqrt{M^2 - \varepsilon^2}$, with $0 < q < M$; then $a = \alpha e^{qy} + \beta e^{-qy}$ and

$$
M a - a' = (M - q)\,\alpha\, e^{qy} + (M + q)\,\beta\, e^{-qy}
$$

(insert $a$ and $a' = q\alpha e^{qy} - q\beta e^{-qy}$). For an even orbital this must vanish at two different points; setting it to zero gives $e^{2qy} = -(M + q)\beta/((M - q)\alpha)$, and the left side takes each value only once (it is strictly increasing), so this can hold at two points only if $\alpha = \beta = 0$. For an odd orbital $a(0) = 0$ gives $\beta = -\alpha$, so $a = 2\alpha\sinh(qy)$ with $\sinh u = (e^{u} - e^{-u})/2$ and $\cosh u = (e^{u} + e^{-u})/2$, and the tip condition becomes $2\alpha(-M\sinh(qL) - q\cosh(qL)) = 0$; the bracket is negative, so $\alpha = 0$. For $|\varepsilon| = M$ the same steps with $a = \alpha + \beta y$ give $\alpha = \beta = 0$ (Exercise 7). So, between $-M$ and $M$ the only level is the zero mode (PROVED here).

These are the exact levels that the record states (key `boundaryConditions.exactK0Spectra` of `Revision/kohn_sham/ks-theory.json`) and lists in its column `eps_analytic` (Notebook 02d, In [7], recomputes all 54 of them; COMPUTED).

**The Prüfer angle.** The shooting method could use $b(0)$ or $a(0)$ directly as the mismatch. The Revision program does something better: it follows the ANGLE of the point $(a, b)$. Write

$$
a = r\cos\theta, \qquad b = r\sin\theta, \qquad r = \sqrt{a^2 + b^2} > 0 .
$$

$\theta(y)$ is the **Prüfer angle** (after the mathematician Heinz Prüfer; the notebooks, which use plain ASCII, write Pruefer). The point $(a, b)$ never reaches the origin: if $a = b = 0$ at some $y$, the uniqueness theorem would make the solution zero everywhere. So $\theta$ is defined everywhere, and we let it grow continuously, counting every full turn (**winding**), so that it can exceed $2\pi$. Where $a \ne 0$, $\theta = \arctan(b/a)$ plus a constant, and

$$
\theta' = \frac{1}{1 + (b/a)^2}\cdot \frac{b' a - b a'}{a^2}
$$

(the chain rule with the derivative $1/(1 + w^2)$ of $\arctan w$, and the quotient rule for $b/a$);

$$
\theta' = \frac{a b' - b a'}{a^2 + b^2} = \frac{a b' - b a'}{r^2}
$$

(multiply out: $\frac{1}{1 + b^2/a^2}\cdot\frac{1}{a^2} = \frac{1}{a^2 + b^2}$); the same formula holds where $a = 0$ (use $\theta = -\arctan(a/b)$ plus a constant there). Now insert the equations:

$$
a b' - b a' = a(\varepsilon a - M b) - b(M a - \varepsilon b) = \varepsilon(a^2 + b^2) - 2M a b
$$

(multiply out and collect);

$$
\theta' = \varepsilon - M\, \frac{2ab}{r^2} = \varepsilon - M\sin 2\theta
$$

(divide by $r^2$; then $2ab/r^2 = 2\sin\theta\cos\theta = \sin 2\theta$, the double-angle formula). The start $b(-L) = 0$ with $a(-L) = 1$ means $\theta(-L) = 0$. The brane conditions become conditions on the end angle $\Phi(\varepsilon) = \theta(0)$:

$$
\text{even: } b(0) = 0 \iff \Phi = l\pi, \qquad \text{odd: } a(0) = 0 \iff \Phi = \frac{\pi}{2} + l\pi,
$$

for a whole number $l$, the **label** of the level ($\sin\theta = 0$ exactly at the multiples of $\pi$, $\cos\theta = 0$ at $\pi/2$ plus multiples of $\pi$).

**The end angle grows with the energy.** First the radius:

$$
r r' = a a' + b b' = a(Ma - \varepsilon b) + b(\varepsilon a - Mb) = M(a^2 - b^2)
$$

(differentiate $r^2 = a^2 + b^2$, which gives $2rr' = 2aa' + 2bb'$; insert the equations; the terms with $\varepsilon$ cancel);

$$
\frac{r'}{r} = M\, \frac{a^2 - b^2}{r^2} = M\cos 2\theta
$$

(divide by $r^2$; $\cos^2\theta - \sin^2\theta = \cos 2\theta$). Now let $u(y) = \partial\theta(y)/\partial\varepsilon$, the change of the angle at $y$ per unit change of the energy (a partial derivative: $\theta$ depends on $y$ and on $\varepsilon$).

$$
u' = \frac{\partial}{\partial \varepsilon}\, \theta' = 1 - 2M\cos(2\theta)\, u
$$

(Schwarz's theorem of Section 2.18 lets us swap the derivatives with respect to $y$ and $\varepsilon$; then differentiate $\varepsilon - M\sin 2\theta$ with respect to $\varepsilon$ by the chain rule);

$$
u' = 1 - 2\,\frac{r'}{r}\, u
$$

(insert $M\cos 2\theta = r'/r$);

$$
r^2 u' + 2 r r' u = r^2
$$

(multiply by $r^2$ and move the $u$ term to the left);

$$
(r^2 u)' = r^2
$$

(the product rule: $(r^2 u)' = 2rr' u + r^2 u'$);

$$
r(0)^2 u(0) - r(-L)^2 u(-L) = \int_{-L}^{0} r^2\, dy
$$

(integrate from $-L$ to 0: the integral of a derivative is the difference of the end values);

$$
\frac{d\Phi}{d\varepsilon} = u(0) = \frac{1}{r(0)^2}\int_{-L}^{0} r^2\, dy > 0
$$

($u(-L) = 0$, because $\theta(-L) = 0$ for every energy; divide by $r(0)^2$; the integral of the positive function $r^2$ is positive). So $\Phi(\varepsilon)$ is **strictly increasing**: each target value $l\pi$ or $\pi/2 + l\pi$ is reached for exactly one energy. Every level has its own label $l$, and no level in a range of energies can be missed (PROVED here; this is the argument of the program's header comment in `Revision/kohn_sham/solver/src/shoot.rs`). The formula also gives the slope that Newton's method below needs, without any extra shot.

*Two values of the slope.* Far from the mass, $\theta' = \varepsilon - M\sin 2\theta$ is $\varepsilon$ on average, so $\Phi \approx \varepsilon L$ plus a bounded amount and the slope is about $L$. At $\varepsilon = 0$ the shot is $a = e^{M(y + L)}$, $b = 0$, so

$$
\frac{d\Phi}{d\varepsilon}\Big|_{\varepsilon = 0} = \frac{\int_{-L}^{0} e^{2M(y + L)}\, dy}{e^{2ML}} = \frac{(e^{2ML} - 1)/(2M)}{e^{2ML}} = \frac{1 - e^{-2ML}}{2M}
$$

($r^2 = e^{2M(y + L)}$; the antiderivative $e^{2M(y+L)}/(2M)$ between $-L$ and 0; divide by $r(0)^2 = e^{2ML}$), which is $0.498761$ for $M = 1$, $L = 3$ (Notebook 02d, In [5]).

**Counting the turns.** A computer's function $\mathrm{atan2}(b, a)$ returns the angle of the point $(a, b)$ in the range from $-\pi$ to $\pi$; it does not count turns. The program therefore adds up the changes of angle from step to step: after each RK4 step it computes the new $\mathrm{atan2}$, subtracts the previous one, and brings the difference into the range $(-\pi, \pi]$ by adding or subtracting $2\pi$. This is correct as long as one step turns the point by less than $\pi$; the program refuses a shot in which a single step turns by 2 or more (radians), a safe margin. Along the way it adds up $\int r^2\,dy$ with the **trapezoid rule** (the integral over one step is the step length times the average of the two end values). When $r^2$ exceeds $10^{250}$ it divides $a$, $b$ and the running integral by suitable powers of $r$, which changes neither the angle nor the quotient $\int r^2 dy/r(0)^2$ (in the free case of this chapter that never happens).

**Newton's method.** To find a level we solve $F(\varepsilon) = \Phi(\varepsilon) - t = 0$ for its target $t$. Replace $F$ near the current guess $\varepsilon_c$ by its tangent line

$$
F(\varepsilon) \approx F(\varepsilon_c) + F'(\varepsilon_c)\,(\varepsilon - \varepsilon_c)
$$

(the linear approximation of one-variable calculus), and take the zero of the line as the next guess:

$$
\varepsilon_{\rm new} = \varepsilon_c - \frac{F(\varepsilon_c)}{F'(\varepsilon_c)}, \qquad F'(\varepsilon) = \frac{d\Phi}{d\varepsilon} = \frac{1}{r(0)^2}\int_{-L}^{0} r^2\,dy
$$

(set the line to zero and solve for $\varepsilon$; the slope is the formula proved above). Close to the root the number of correct digits roughly doubles at every step (ASSUMED: a standard result of numerical analysis, quoted without proof; the notebook shows it). Far from the root the tangent can point anywhere, so the program (function `find_level` in `Revision/kohn_sham/solver/src/shoot.rs`) adds a safety net:

1. Shoot at the starting guess $\varepsilon = 0$; if $F(0) = 0$ exactly (the zero mode), stop.
2. Make a bracket: walk upwards if $F < 0$ (downwards if $F > 0$), with a first step of 1.2 times Newton's estimate $|F/F'|$, but at least $10^{-4}$ and at most 2, doubling the step until $F$ changes sign.
3. Inside the bracket take Newton steps; whenever Newton's point falls outside the bracket, or $|F|$ has not at least halved since the previous step, take the midpoint of the bracket instead (bisection). After each shot keep the half of the bracket that holds the sign change.
4. Stop when the bracket is narrower than the tolerance $10^{-13}$ (the record's `rootTolerance`), or after a Newton step shorter than it.

**The orbital between the grid points.** RK4 gives $a$ and $b$ at the ends of the steps (the **nodes**). The program also needs them in the middle of every step and takes them from the **cubic Hermite interpolation**: the polynomial of degree 3 that has the right values $f_0, f_1$ AND the right slopes $f_0', f_1'$ at the two ends of a step of length $h$ (the slopes come from the equations themselves). Put the step at $0 \le s \le h$ and write the cubic as $P(s) = f_0 + f_0' s + c s^2 + e s^3$ (its value and slope at $s = 0$ are then right). The two conditions at $s = h$ are

$$
f_0 + f_0' h + c h^2 + e h^3 = f_1, \qquad f_0' + 2ch + 3e h^2 = f_1'
$$

(the value and the derivative of $P$ at $s = h$);

$$
e h^3 = (f_0' + f_1')\, h - 2(f_1 - f_0), \qquad c h^2 = 3(f_1 - f_0) - (2f_0' + f_1')\, h
$$

(multiply the second equation by $h$, subtract twice the first equation written as $ch^2 + eh^3 = f_1 - f_0 - f_0' h$, which leaves $eh^3$; then $ch^2$ from the first equation);

$$
P\big(\tfrac{h}{2}\big) = f_0 + \frac{f_0' h}{2} + \frac{c h^2}{4} + \frac{e h^3}{8} = \frac{f_0 + f_1}{2} + \frac{h}{8}\,(f_0' - f_1')
$$

(insert $s = h/2$; then insert $ch^2$ and $eh^3$ and collect: the values give $f_0 + (f_1 - f_0)(\frac34 - \frac14) = \frac{f_0 + f_1}{2}$, the slopes give $h f_0'(\frac12 - \frac12 + \frac18) + h f_1'(-\frac14 + \frac18) = \frac{h}{8}(f_0' - f_1')$). Its error is of order $h^4$, the order of RK4 (ASSUMED: quoted). With the values at the nodes and the midpoints the program integrates with Simpson's rule (Section 2.13) on the fine grid of $2G + 1$ points, with spacing $h/2$.

**Why the error grows with the level.** Far above the mass the point $(a, b)$ turns at the rate $\theta' \approx \varepsilon$, like the oscillator of Section 2.7 with the frequency $\varepsilon$: one RK4 step multiplies the turning point by $R(i\omega)$ with $\omega = \varepsilon h$. Its angle $\phi$ is a little smaller than $\omega$. With $c = 1 - \frac{\omega^2}{2} + \frac{\omega^4}{24}$ and $s = \omega - \frac{\omega^3}{6}$ (the real and imaginary parts of $R(i\omega)$, Section 2.7),

$$
\tan\phi = \frac{s}{c}, \qquad \tan\omega = \frac{\omega - \frac{\omega^3}{6} + \frac{\omega^5}{120} - \dots}{1 - \frac{\omega^2}{2} + \frac{\omega^4}{24} - \frac{\omega^6}{720} + \dots}
$$

(the angle of a complex number has the tangent imaginary part over real part; $\tan = \sin/\cos$ with the Taylor series of the sine and the cosine, which follow from Section 2.3 as the series of $e^{i\omega}$);

$$
\tan\phi - \tan\omega = -\frac{\omega^5/120}{c} + (\text{terms with } \omega^7 \text{ and higher}) = -\frac{\omega^5}{120} + \dots
$$

(the numerators differ by $\omega^5/120$, the denominators only from $\omega^6$ on, which changes the quotient from $\omega^7$ on; and $1/c = 1 + \frac{\omega^2}{2} + \dots$ changes $\omega^5/120$ only from $\omega^7$ on);

$$
\phi - \omega = -\frac{\omega^5}{120} + \dots
$$

(by the **mean value theorem** of calculus, $g(\phi) - g(\omega) = (\phi - \omega)\, g'(\xi)$ for some $\xi$ between $\omega$ and $\phi$; applied to $g = \tan$, whose derivative is $1 + \tan^2$, it gives $\tan\phi - \tan\omega = (\phi - \omega)(1 + \tan^2\xi)$, and $1 + \tan^2\xi = 1 + \dots$ for small angles). So every step lags behind by $\omega^5/120 = \varepsilon^5 h^5/120$; after $G = L/h$ steps the end angle lags by

$$
\frac{L}{h}\cdot\frac{\varepsilon^5 h^5}{120} = \frac{L\, \varepsilon^5 h^4}{120}
$$

(the number of steps times the lag per step). Since $\Phi$ grows by about $L$ per unit of energy, the energy must be higher by $\delta\varepsilon$ with $L\,\delta\varepsilon = L\varepsilon^5h^4/120$ to make up for the lag:

$$
\delta\varepsilon \approx \frac{\varepsilon^5 h^4}{120}, \qquad \frac{\delta\varepsilon}{\varepsilon} \approx \frac{(h\varepsilon)^4}{120}
$$

(divide by $L$, then by $\varepsilon$). The computed levels come out slightly too HIGH, with an error of order $h^4$ that grows like the fifth power of the level (PROVED to leading order for levels far above the mass; near the mass the point does not turn uniformly and the error is smaller; Notebook 02d, In [12], compares this prediction with all 51 nonzero levels of the record).

### 2.25 Example: the shooting method of the Revision Kohn-Sham solver, rewritten

Notebook 02d reads the theory, the parameters and the table of the free spectrum from the Revision record; rewrites the program's RK4 shot with the counted Prüfer angle and checks it against the angle equation; draws the staircase $\Phi(\varepsilon)$ and its slope and checks the slope formula; draws the angle along $y$; recomputes the 54 exact levels; rewrites the program's Newton root finder with its safety net and compares it with plain bisection; reproduces all 54 numerical levels of the record and the numbers quoted by two checks of the program; builds the normalised orbitals as the program does; and measures the order 4 of the levels and the phase-lag law. It ends with ALL 17 CHECKS PASSED (notebook 02d).

<!-- NOTEBOOK 02d -->

### 2.28 Line-by-line walk-through of Notebook 02d

The notebook has thirteen code cells, In [1] to In [13]. A quoted line `...)` stands for the rest of a figure caption, which Section 2.27 prints in full under its figure.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 2.26; its code is the set-up code of Notebook 02a explained in Section 2.11, with `NOTEBOOK_ID = "02d"`. It prints Set-up of notebook 02d complete: repository folder found, helpers defined.

**In [2], the records and the settings.**

```python
import csv  # reads the table of levels (comma-separated values)
import math  # sqrt, atan2, pi for single numbers
import re  # finds numbers inside a text

import mpmath  # numbers with as many digits as we ask for
import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols

BLUE, ORANGE, AQUA, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7"
GREY, BLACK = "#8a8986", "#000000"
```

`csv` reads tables stored as comma-separated values (one row per line, the cells separated by commas), `re` finds patterns (here numbers) inside a text (**regular expressions**); the other packages and the colours are as before.

```python
THEORY = "Revision/kohn_sham/ks-theory.json"
PARAMETERS = "Revision/kohn_sham/results/parameters.json"
TABLE = "Revision/kohn_sham/results/spectrum/free-k0-analytic.csv"
SOLVER_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
theory = json.loads(repository_file(THEORY).read_text(encoding="utf-8"))
parameters = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
with open(repository_file(TABLE), encoding="utf-8", newline="") as table:
    ROWS = list(csv.DictReader(table))  # one dictionary per level
```

The four Revision records of the notebook: the Kohn-Sham theory, the solver's parameters, the table of the free spectrum written by the Rust program, and the program's report of checks. The two JSON files are read as in Notebook 02a. `with open(...) as table:` opens the table file and closes it again at the end of the block; `csv.DictReader` reads it row by row, each row as a dictionary from the column names of the first line (`m`, `L`, `parity`, `label`, `eps_numeric`, `eps_analytic`, `difference`) to the cell texts.

```python
say("realForm: " + theory["blockEquation"]["realForm"])
say("brane status: " + theory["boundaryConditions"]["brane"]["status"])
say("tip status: " + theory["boundaryConditions"]["tip"]["status"])
say("exact k = 0 spectra: " + theory["boundaryConditions"]["exactK0Spectra"])
```

Four statements of the theory record are printed: the real form of the block equation (with the general mass `M_eff`, momentum weight `kappa k` and potential `v_v` that Section 2.24 sets to $M$, 0 and 0), the status of the brane conditions (ASSUMED), the status of the tip condition (chosen, regular tip), and the exact $k = 0$ spectra derived in Section 2.24.

```python
G_CANONICAL = parameters["numerics"]["rk4Steps"]  # RK4 steps for L = 3
ROOT_TOLERANCE = parameters["numerics"]["rootTolerance"]
M_RECORD, L_RECORD = parameters["physics"]["m"], parameters["physics"]["L_tipCutoff"]
report("RK4 steps, root tolerance, m, L of the record",
       f"{G_CANONICAL}, {ROOT_TOLERANCE}, {M_RECORD}, {L_RECORD}")
report("levels in the table", len(ROWS))
check(theory["boundaryConditions"]["brane"]["status"] == "ASSUMED"
      and G_CANONICAL == 900 and ROOT_TOLERANCE == 1e-13 and len(ROWS) == 54,
      "records read: brane ASSUMED, 900 RK4 steps, tolerance 1e-13, 54 levels")
```

The solver's settings: 900 RK4 steps, the root tolerance $10^{-13}$, $m = 1$ and $L = 3$; the table has 54 rows. The check confirms these values and that the brane conditions are labelled ASSUMED in the record.

**In [3], shooting with RK4 and counting the turns.**

```python
def shoot(eps, M, L, G, keep=False):
    """RK4 from y = -L, (a, b) = (1, 0), to y = 0 in G steps.  Returns Phi =
    theta(0), the slope dPhi/deps = (integral of r^2) / r(0)^2 and the largest
    turn of one step; with keep=True also the arrays y, a, b, theta of the path."""
    h = L / G  # the step
    a, b = 1.0, 0.0  # the tip: b(-L) = 0, so theta(-L) = 0
    theta, raw = 0.0, 0.0  # the counted angle and the last atan2 value
    integral, r2_before = 0.0, 1.0  # running integral of r^2; r^2 at the last node
    largest = 0.0  # the largest turn of one step so far
    path = [(-L, a, b, theta)]
```

The function follows the Rust function `shoot` of `Revision/kohn_sham/solver/src/shoot.rs` for the free case. The start at the tip is $(a, b) = (1, 0)$, so $\theta = 0$. `theta` is the counted angle and `raw` the last value returned by `atan2`; `integral` collects $\int r^2 dy$ and `r2_before` holds $r^2$ at the last node (1 at the start); `largest` records the largest turn of one step; `path` holds $(y, a, b, \theta)$ at the nodes when it is asked for.

```python
    for i in range(G):
        p1a, p1b = M * a - eps * b, eps * a - M * b  # the slopes (a', b') at start
        a2, b2 = a + h / 2 * p1a, b + h / 2 * p1b  # half a step with them
        p2a, p2b = M * a2 - eps * b2, eps * a2 - M * b2  # the slopes there
        a3, b3 = a + h / 2 * p2a, b + h / 2 * p2b  # half a step with these
        p3a, p3b = M * a3 - eps * b3, eps * a3 - M * b3  # the slopes there
        a4, b4 = a + h * p3a, b + h * p3b  # a whole step with the third slopes
        p4a, p4b = M * a4 - eps * b4, eps * a4 - M * b4  # the slopes at the end
        a += h / 6 * (p1a + 2 * p2a + 2 * p3a + p4a)  # weights 1 : 2 : 2 : 1
        b += h / 6 * (p1b + 2 * p2b + 2 * p3b + p4b)
```

One RK4 step of the two equations $a' = Ma - \varepsilon b$, $b' = \varepsilon a - Mb$, written out component by component as the Rust code writes it: the four pairs of slopes `p1` to `p4` are the $k_1$ to $k_4$ of Section 2.4 for $a$ and for $b$, and `a += ...` means "add the right side to `a`". (The names `a4`, `b4` here are the RK4 end-of-step values; they have nothing to do with the metric function $a_4$.)

```python
        new = math.atan2(b, a)  # the angle of (a, b), between -pi and pi
        change = new - raw
        if change > math.pi:  # crossed from just below pi to just above -pi
            change -= 2 * math.pi
        elif change <= -math.pi:  # crossed the other way
            change += 2 * math.pi
        largest = max(largest, abs(change))
        theta += change
        raw = new
```

The winding count of Section 2.24: the new `atan2` angle minus the previous one, brought into $(-\pi, \pi]$ (a jump of almost $+2\pi$ means that the point crossed the negative horizontal axis downwards, where `atan2` jumps from $\pi$ to $-\pi$, and so on); the change is added to the counted angle, and the largest change is remembered.

```python
        r2 = a * a + b * b  # r^2 at the new node
        integral += h / 2 * (r2_before + r2)  # the trapezoid rule for this step
        r2_before = r2
        if keep:
            path.append((-L + (i + 1) * h, a, b, theta))
```

The trapezoid rule adds the step length times the average of $r^2$ at the two ends of the step; the node is stored if the path was asked for.

```python
    if keep:
        return theta, integral / r2_before, largest, np.array(path).T
    return theta, integral / r2_before, largest
```

After the last step `r2_before` is $r(0)^2$, so `integral / r2_before` is the slope $d\Phi/d\varepsilon$ of Section 2.24. The function returns $\Phi = \theta(0)$, that slope and the largest turn; with `keep=True` also the path, turned by `.T` (transpose) into four rows: all $y$, all $a$, all $b$, all $\theta$. (The Rust function also rescales $(a, b)$ when $r^2$ exceeds $10^{250}$; in this free case $r^2$ stays far below that, so the rewrite leaves it out.)

```python
def angle_equation(eps, M, L, G):
    """RK4 for the single equation theta' = eps - M sin(2 theta), theta(-L) = 0."""
    h = L / G
    theta = 0.0

    def slope(t):
        return eps - M * math.sin(2 * t)
    for _ in range(G):
        k1 = slope(theta)
        k2 = slope(theta + h / 2 * k1)
        k3 = slope(theta + h / 2 * k2)
        k4 = slope(theta + h * k3)
        theta += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return theta
```

An independent way to the same end angle: RK4 applied to the single angle equation $\theta' = \varepsilon - M\sin 2\theta$ of Section 2.24 (the right side does not depend on $y$, so `slope` takes only the angle).

```python
M1, L3 = 1.0, 3.0  # the canonical case of the record
for eps in (-2.0, 0.0, 1.0, 2.5):
    Phi = shoot(eps, M1, L3, 900)[0]  # element 0 of the result: Phi
    say(f"eps = {eps:+.1f}: Phi by (a, b) = {Phi:+.12f},  "
        f"by the angle equation = {angle_equation(eps, M1, L3, 900):+.12f}")
```

For four energies the two computations are printed side by side, for example $\Phi(2.5) = 6.798217350015$ by $(a, b)$ and $6.798217350074$ by the angle equation.

```python
differences = [abs(shoot(e, M1, L3, 900)[0] - angle_equation(e, M1, L3, 900))
               for e in np.linspace(-5.0, 5.0, 21)]
check(max(differences) < 1e-8 and shoot(0.0, M1, L3, 900)[0] == 0.0,
      "both ways of computing Phi agree within 1e-8; Phi(0) is exactly 0")
```

On 21 energies from $-5$ to 5 the two ways agree within $10^{-8}$ (they are different computations, each with its own small RK4 error), and at $\varepsilon = 0$ the shot gives exactly $\Phi = 0$, because $b$ stays exactly 0.

**In [4], the staircase.**

```python
eps_grid = np.linspace(-6.0, 7.0, 651)
shots = [shoot(e, M1, L3, 900) for e in eps_grid]  # (Phi, slope, largest turn)
Phi_grid = np.array([s[0] for s in shots])
slope_grid = np.array([s[1] for s in shots])  # dPhi/deps by the formula
check(np.all(np.diff(Phi_grid) > 0), "Phi(eps) increases on the whole grid")
```

651 energies from $-6$ to 7 (spacing 0.02) are shot; `Phi_grid` holds the end angles and `slope_grid` the slopes by the formula. `np.diff` gives the differences of neighbouring entries; the check requires all of them to be positive: $\Phi$ increases, as proved in Section 2.24.

```python
def target(parity, label):
    """The target value of Phi for a level of the given parity and label."""
    return label * math.pi if parity == "even" else math.pi / 2 + label * math.pi


canonical = [r for r in ROWS if float(r["m"]) == 1.0 and float(r["L"]) == 3.0]
```

`target` returns $l\pi$ for an even and $\pi/2 + l\pi$ for an odd level (the program's function of the same name). `canonical` keeps the 18 rows of the table with $M = 1$ and $L = 3$ (the cells are texts, so `float` turns them into numbers).

```python
fig, ax = plt.subplots(figsize=(7.0, 5.4))
ax.plot(eps_grid, Phi_grid / math.pi, color=BLACK, lw=1.4,
        label="$\\Phi(\\varepsilon)/\\pi$ (RK4, 900 steps)")
for label in range(-4, 7):
    ax.axhline(label, color=BLUE, lw=0.6, alpha=0.6)
    ax.axhline(label + 0.5, color=ORANGE, lw=0.6, ls="--", alpha=0.6)
```

The staircase $\Phi/\pi$ in black, and horizontal target lines: blue at the whole numbers (even targets $l\pi$), dashed orange halfway between them (odd targets).

```python
for r in canonical:
    is_even = r["parity"] == "even"
    ax.plot(float(r["eps_numeric"]), target(r["parity"], int(r["label"])) / math.pi,
            "o" if is_even else "s", color=BLUE if is_even else ORANGE, ms=6)
ax.plot([], [], "o", color=BLUE, label="even levels: $\\Phi = l\\pi$")
ax.plot([], [], "s", color=ORANGE, label="odd levels: $\\Phi = \\pi/2 + l\\pi$")
```

Each of the record's 18 levels is marked at its energy and its target (a blue dot for even, an orange square for odd); two empty plots add the legend entries.

```python
ax.set_ylim(-4.2, 6.2)
ax.set_xlabel("energy $\\varepsilon$ (units $m$)")
ax.set_ylabel("end angle $\\Phi = \\theta(0)$ in units of $\\pi$")
ax.set_title("The Pruefer staircase: $M = 1$, $L = 3$")
ax.legend(loc="upper left", fontsize=8)
save_figure(fig, "pruefer_staircase",
            "The end value of the Pruefer angle, $\\Phi(\\varepsilon) = "
            ...)
```

Labels and the saved figure `02d_1_pruefer_staircase.png`. **What Figure 02d.1 shows:** the curve rises steadily and crosses every target line exactly once, at a level of the record; even and odd levels alternate; the zero mode sits at $\varepsilon = 0$, $\Phi = 0$; between $-1$ and 1 (inside the mass gap, $|\varepsilon| < M$) the curve rises only slowly (In [5] finds slopes between 0.5 and 0.7 there) and crosses only the line 0, in agreement with Section 2.24.

**In [5], the slope of the staircase.**

```python
DELTA = 1e-4  # the half-width of the central difference
tested = [-4.0, -1.34, -0.5, 0.0, 0.7, 1.3, 3.0]  # seven energies
relative = []
for e in tested:
    formula = shoot(e, M1, L3, 900)[1]  # element 1 of the result: the slope
    central = (shoot(e + DELTA, M1, L3, 900)[0]
               - shoot(e - DELTA, M1, L3, 900)[0]) / (2 * DELTA)
    relative.append(abs(central / formula - 1))
    say(f"eps = {e:+.2f}: formula {formula:9.5f}, central difference {central:9.5f}")
```

At seven energies the slope formula $\int r^2 dy/r(0)^2$ is compared with the central difference $(\Phi(\varepsilon + \delta) - \Phi(\varepsilon - \delta))/(2\delta)$ of Section 2.18 with $\delta = 10^{-4}$; the relative differences are collected. The printout shows, for example, 3.85717 at $\varepsilon = -4$, 12.49831 at $-1.34$ and 0.49876 at 0.

```python
report("largest relative difference formula - central difference",
       f"{max(relative):.1e}")
check(max(relative) < 1e-4 and np.all(slope_grid > 0),
      "dPhi/deps = (integral of r^2)/r(0)^2 > 0 (agrees with central differences)")
```

The largest relative difference is $3.7 \times 10^{-6}$ (COMPUTED); the check requires less than $10^{-4}$, and a positive slope at all 651 energies of the grid.

```python
# At eps = 0 the shot is exactly a = e^(M(y + L)), b = 0, so the integral can be
# done by hand: (e^(2ML) - 1)/(2M) divided by r(0)^2 = e^(2ML).
at_zero = (1 - math.exp(-2 * M1 * L3)) / (2 * M1)
report("slope at eps = 0: formula, exact (1 - e^(-2ML))/(2M)",
       f"{shoot(0.0, M1, L3, 900)[1]:.6f}, {at_zero:.6f}")
check(abs(shoot(0.0, M1, L3, 900)[1] - at_zero) < 1e-4,
      "at eps = 0 the slope is (1 - e^(-2ML))/(2M), about 1/(2M)")
```

The slope at $\varepsilon = 0$ computed by hand in Section 2.24, $(1 - e^{-6})/2 = 0.498761$, against the program's 0.498762 (the difference is the error of the trapezoid rule).

```python
grid_difference = (Phi_grid[2:] - Phi_grid[:-2]) / (eps_grid[2:] - eps_grid[:-2])
fig, ax = plt.subplots()
ax.plot(eps_grid, slope_grid, color=BLACK, lw=1.4,
        label="formula $\\int r^2 dy / r(0)^2$")
ax.plot(eps_grid[1:-1][::6], grid_difference[::6], "o", color=AQUA, ms=4,
        label="central differences of the staircase")
ax.axhline(L3, color=GREY, ls="--", lw=1.0, label="$L = 3$")
```

`grid_difference` is the central difference of the staircase on the grid itself (the value two places ahead minus the value two places back, divided by the energy distance 0.04), belonging to the inner energies `eps_grid[1:-1]`; every sixth one is drawn (`[::6]`) as an aqua dot over the black formula curve, with a dashed line at $L = 3$.

```python
ax.set_ylim(0.0, 17.5)  # room for the legend above the two peaks
ax.set_xlabel("energy $\\varepsilon$ (units $m$)")
ax.set_ylabel("$d\\Phi/d\\varepsilon$ (units $1/m$)")
ax.set_title("The slope of the staircase is never negative")
ax.legend(loc="upper right", fontsize=8)
save_figure(fig, "staircase_slope",
            "The slope $d\\Phi/d\\varepsilon$ of the end angle (vertical axis, "
            ...)
```

Labels and the saved figure `02d_2_staircase_slope.png`. **What Figure 02d.2 shows:** the dots lie on the formula curve; the slope is positive everywhere; it is about $L = 3$ far from the mass, about $1/(2M) = 0.5$ near $\varepsilon = 0$ (the zero-mode shot grows towards the brane, so $r(0)^2$ is large), and it has two peaks near $|\varepsilon| = 1.34$ (there the shot ends with a small $r(0)$ compared with its size inside, so a small change of energy turns the end angle a lot).

**In [6], the angle along the interval.**

```python
chosen = [("even", 0), ("odd", 0), ("even", 1), ("odd", 1), ("even", 3)]
level_of = {(r["parity"], int(r["label"])): float(r["eps_numeric"]) for r in canonical}
fig, ax = plt.subplots()
```

Five levels of the canonical case, named by parity and label; `level_of` maps each (parity, label) of the canonical rows to the record's numerical level.

```python
for (parity, label), color in zip(chosen, [BLACK, ORANGE, BLUE, VIOLET, AQUA]):
    eps = level_of[(parity, label)]
    y_path, a_path, b_path, theta_path = shoot(eps, M1, L3, 900, keep=True)[3]
    ax.plot(y_path, theta_path / math.pi, color=color, lw=1.5,
            ls="-" if parity == "even" else "--",
            label=f"{parity} $l = {label}$, $\\varepsilon = {eps:.4f}$")
    ax.plot([0.0], [target(parity, label) / math.pi], "o", color=color, ms=6)
```

For each chosen level the shot is repeated with `keep=True`; element 3 of the result is the path, unpacked into its four rows. $\theta/\pi$ is drawn against $y$ (solid for even, dashed for odd), and a dot marks the target at the brane.

```python
ax.set_xlabel("hidden coordinate $y$ (units $1/H$): tip at $-3$, brane at $0$")
ax.set_ylabel("Pruefer angle $\\theta(y)/\\pi$")
ax.set_title("The angle winds up to its target at the brane")
ax.legend(loc="upper left", fontsize=8)
save_figure(fig, "angle_along_y",
            "The Pruefer angle $\\theta(y)$ in units of $\\pi$ (vertical axis) "
            ...)
```

Labels and the saved figure `02d_3_angle_along_y.png`. **What Figure 02d.3 shows:** every curve starts at 0 at the tip and ends exactly on its dot; the zero mode stays at 0; the number of half-turns made is the label; higher levels wind faster, at the average rate $\varepsilon$.

**In [7], the exact levels, computed again.**

```python
mpmath.mp.dps = 30


def odd_root(M, L, n):
    """The n-th positive root p of M sin(pL) + p cos(pL) = 0 (30 digits)."""
    g = lambda p: M * mpmath.sin(p * L) + p * mpmath.cos(p * L)  # noqa: E731
    return mpmath.findroot(g, ((n + 0.5) * mpmath.pi / L, (n + 1) * mpmath.pi / L),
                           solver="anderson")
```

mpmath at 30 digits. The odd condition $\tan(pL) = -p/M$ multiplied by $M\cos(pL)$ is $M\sin(pL) + p\cos(pL) = 0$ (no infinities). The $n$-th root lies between $(n + \frac12)\pi/L$ and $(n + 1)\pi/L$ (Section 2.24), and `findroot` refines it in that bracket. (The comment `noqa: E731` tells a style checker that the one-line `lambda` function is intended.)

```python
def exact_level(M, L, parity, label):
    """The exact level of the given parity and label."""
    if parity == "even":
        if label == 0:
            return 0.0  # the zero mode
        return math.copysign(float(mpmath.sqrt(M ** 2 + (label * mpmath.pi / L) ** 2)),
                             label)
    n = label if label >= 0 else -label - 1
    value = float(mpmath.sqrt(M ** 2 + odd_root(M, L, n) ** 2))
    return value if label >= 0 else -value
```

The exact level for a parity and a label, as the record defines them: even label 0 is the zero mode; even label $l \ne 0$ is $\pm\sqrt{M^2 + (l\pi/L)^2}$ with the sign of $l$ (`math.copysign(x, s)` is $|x|$ with the sign of $s$); the odd label $l \ge 0$ uses the root $p_l$ and gives $+\sqrt{M^2 + p_l^2}$, the odd label $l \le -1$ uses the root $p_{-l-1}$ and gives the negative level.

```python
analytic_ours = [exact_level(float(r["m"]), float(r["L"]), r["parity"],
                             int(r["label"])) for r in ROWS]
analytic_record = [float(r["eps_analytic"]) for r in ROWS]
worst_analytic = max(abs(a - b) for a, b in zip(analytic_ours, analytic_record))
report("largest |exact level (here) - eps_analytic (record)|", f"{worst_analytic:.1e}")
check(worst_analytic < 1e-14, "all 54 exact levels equal the column eps_analytic",
      record=f"{TABLE}, column eps_analytic")
```

All 54 exact levels are computed here and compared with the record's column `eps_analytic`: the largest difference is $1.8 \times 10^{-15}$, the size of the last printed digit (COMPUTED: reproduces `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv`, column `eps_analytic`).

```python
p_axis = np.linspace(0.01, 3.3, 3000)
tangent = np.tan(p_axis * L3)
tangent[np.abs(tangent) > 8] = np.nan  # do not draw the jumps at the poles
fig, ax = plt.subplots()
ax.plot(p_axis, tangent, color=BLUE, lw=1.4, label="$\\tan(pL)$, $L = 3$")
ax.plot(p_axis, -p_axis / M1, color=ORANGE, lw=1.4, ls="--", label="$-p/M$, $M = 1$")
```

The graphical solution of the odd condition for $M = 1$, $L = 3$: the branches of $\tan(pL)$ (with the jumps removed as in Notebook 02b) and the falling line $-p/M$.

```python
for n in range(3):
    p_n = float(odd_root(M1, L3, n))
    ax.plot([p_n], [-p_n], "o", color=BLACK, ms=6)
    ax.annotate(f"$p_{n} = {p_n:.4f}$", (p_n, -p_n), textcoords="offset points",
                xytext=(6, -14), fontsize=8)
ax.axhline(0.0, color=BLACK, lw=0.6)
ax.set_ylim(-6.0, 6.0)
ax.set_xlabel("$p$ (units $m$)")
ax.set_ylabel("value of each side")
ax.set_title("Odd levels: $\\tan(pL) = -p/M$, then $\\varepsilon = \\sqrt{M^2 + p^2}$")
ax.legend(loc="upper right", fontsize=8)
save_figure(fig, "odd_level_equation",
            "The equation of the odd levels for $M = 1$ and $L = 3$: the branches "
            ...)
```

The first three roots are marked and labelled on the line; labels and the saved figure `02d_4_odd_level_equation.png`. **What Figure 02d.4 shows:** one crossing on every branch of the tangent, each a root $p_n$; the first three give the odd levels 1.2923, 2.0106 and 2.9119.

**In [8], Newton's method with a safety net.**

```python
def find_level(M, L, G, goal, tolerance=ROOT_TOLERANCE, log=None):
    """The energy with Phi(eps) = goal, found as the Rust program finds it.  If log
    is a list, every energy that is shot is appended to it."""
    def mismatch(eps):
        Phi, slope, largest = shoot(eps, M, L, G)
        if largest >= 2.0:  # the program refuses such a shot
            raise ValueError(f"one step turns the angle by {largest:.2f}")
        if log is not None:
            log.append(eps)
        return Phi - goal, slope  # F(eps) and F'(eps)
```

`find_level` is the program's function of the same name, line for line (Section 2.24). The inner function `mismatch` shoots one energy, refuses a shot in which one step turns by 2 or more, records the energy if a list was given, and returns $F = \Phi - t$ and $F' = d\Phi/d\varepsilon$.

```python
    e_c = 0.0  # step 1: the starting guess
    F_c, dF_c = mismatch(e_c)
    if F_c == 0.0:
        return e_c
```

Step 1: shoot at $\varepsilon = 0$; for the zero mode ($t = 0$) the mismatch is exactly 0 and the search ends at once with the energy exactly 0.

```python
    if F_c < 0.0:  # step 2, upwards: the level lies above
        low = e_c
        step = min(max(1.2 * (-F_c / dF_c), 1e-4), 2.0)
        while True:
            e = low + step
            F, dF = mismatch(e)
            if F >= 0.0:  # the sign changed: the bracket is (low, e)
                high = e
                if abs(F) < abs(F_c):  # keep the better of the two guesses
                    e_c, F_c, dF_c = e, F, dF
                break
            low, e_c, F_c, dF_c = e, e, F, dF  # still below: move on
            step *= 2.0
```

Step 2 when $F(0) < 0$ (the level lies above, because $\Phi$ increases): the first step is 1.2 times Newton's estimate $-F/F'$, limited to between $10^{-4}$ and 2 (`max` then `min`). The `while True` loop repeats until `break`: it shoots one step further up; if the sign has changed the bracket is (`low`, `e`), and the better of the two end guesses becomes the current guess; otherwise the new point becomes the lower end and the current guess, and the step is doubled.

```python
    else:  # step 2, downwards: the level lies below
        high = e_c
        step = min(max(1.2 * (F_c / dF_c), 1e-4), 2.0)
        while True:
            e = high - step
            F, dF = mismatch(e)
            if F <= 0.0:  # the sign changed: the bracket is (e, high)
                low = e
                if abs(F) < abs(F_c):
                    e_c, F_c, dF_c = e, F, dF
                break
            high, e_c, F_c, dF_c = e, e, F, dF
            step *= 2.0
    if F_c == 0.0:
        return e_c
```

The same walk downwards when $F(0) > 0$. If the walk happens to land exactly on the level, the search ends. (The Rust function can also be given a known lower bound for the downward bracket, and it gives up after 400 shots without a bracket; neither is needed in this notebook.)

```python
    previous = math.inf  # |F| at the previous step
    for _ in range(300):  # step 3
        if high - low <= tolerance:  # step 4: the bracket is narrow enough
            break
        e_new = e_c - F_c / dF_c  # Newton's point
        bisect = not (low < e_new < high) or abs(F_c) > 0.5 * previous
        if bisect:
            e_new = 0.5 * (low + high)  # the safety net
        previous = abs(F_c)
```

Step 3, at most 300 times: stop if the bracket is narrower than the tolerance (step 4). Otherwise compute Newton's point; if it is not strictly inside the bracket, or if $|F|$ has not at least halved since the previous pass (`math.inf`, infinity, makes the first pass always pass this test), take the midpoint of the bracket instead. `previous` remembers $|F|$ for the next pass.

```python
        F, dF = mismatch(e_new)
        moved = abs(e_new - e_c)
        e_c, F_c, dF_c = e_new, F, dF
        if F == 0.0:
            break
        if F < 0.0:  # keep the half of the bracket with the sign change
            low = e_new
        else:
            high = e_new
        if moved <= tolerance and not bisect:  # step 4: a tiny Newton step
            break
    return e_c
```

Shoot the new point; it becomes the current guess. An exact zero ends the search; otherwise the new point replaces the end of the bracket with the same sign of $F$. A Newton step shorter than the tolerance also ends the search (step 4). The function returns the current guess.

```python
def find_level_by_bisection(M, L, G, goal, tolerance=ROOT_TOLERANCE, log=None):
    """The same level by plain bisection on the bracket (-12, 12)."""
    low, high = -12.0, 12.0
    while high - low > tolerance:
        middle = 0.5 * (low + high)
        if log is not None:
            log.append(middle)
        if shoot(middle, M, L, G)[0] < goal:
            low = middle
        else:
            high = middle
    return 0.5 * (low + high)
```

For comparison, plain bisection on the bracket $(-12, 12)$: because $\Phi$ increases, $\Phi(m) <$ target means that the level lies above the midpoint $m$.

```python
newton_log, bisection_log = [], []
by_newton = find_level(M1, L3, 900, target("even", 3), log=newton_log)
by_bisection = find_level_by_bisection(M1, L3, 900, target("even", 3),
                                       log=bisection_log)
report("even label 3 by Newton", f"{by_newton:.15f} ({len(newton_log)} shots)")
report("even label 3 by bisection",
       f"{by_bisection:.15f} ({len(bisection_log)} shots)")
for k, e in enumerate(newton_log, 1):
    say(f"Newton shot {k}: eps = {e:.15f}, error {abs(e - by_newton):.1e}")
```

Both search the even level with label 3 (target $3\pi$) of the case $M = 1$, $L = 3$, recording every energy they shoot. Newton finds 3.296908309775607 with 9 shots, bisection 3.296908309775617 with 48 shots (COMPUTED). The nine Newton shots are printed: 0 (step 1), 2 and 6 (the bracket walk: the first step is limited to 2, the doubled step 4 reaches 6, where $F$ has changed sign), then 3.1476, 3.2796, 3.29660, 3.2969082, ... with the errors $1.5 \times 10^{-1}$, $1.7 \times 10^{-2}$, $3.1 \times 10^{-4}$, $1.0 \times 10^{-7}$, $1.3 \times 10^{-14}$, 0: from the fourth shot on, each error is roughly the square of the previous one times a constant, so the number of correct digits about doubles.

```python
fig, ax = plt.subplots()
ax.semilogy(range(1, len(bisection_log) + 1),
            np.maximum(np.abs(np.array(bisection_log) - by_newton), 1e-17), "s-",
            color=ORANGE, ms=4, lw=1.2, label="bisection on $(-12, 12)$")
ax.semilogy(range(1, len(newton_log) + 1),
            np.maximum(np.abs(np.array(newton_log) - by_newton), 1e-17), "o-",
            color=BLUE, ms=5, lw=1.2, label="the program's Newton with safety net")
ax.set_ylim(1e-17, 30.0)
ax.set_xlabel("number of the shot")
ax.set_ylabel("$|\\varepsilon - \\varepsilon_3|$ (units $m$)")
ax.set_title("Finding the even level $l = 3$ ($M = 1$, $L = 3$)")
ax.legend(loc="upper right", fontsize=8)
save_figure(fig, "newton_vs_bisection",
            "The distance $|\\varepsilon - \\varepsilon_3|$ (units of $m$, "
            ...)
```

The distance of every shot energy from the level, on a logarithmic axis (exact zeros drawn at $10^{-17}$), for both methods; the saved figure is `02d_5_newton_vs_bisection.png`. **What Figure 02d.5 shows:** the bisection squares fall along a straight line (a factor 2 per shot) and need 48 shots; the Newton circles first jump around while the bracket is made, then plunge, and stop after 9 shots.

```python
check(abs(by_newton - level_of[("even", 3)]) < 1e-12
      and abs(by_bisection - by_newton) < 1e-13
      and len(newton_log) < 15 < 45 < len(bisection_log),
      "Newton (fewer than 15 shots) gives the record's level; bisection agrees",
      record=f"{TABLE}, column eps_numeric")
```

The Newton result equals the record's level within $10^{-12}$, bisection agrees within $10^{-13}$, and the numbers of shots are fewer than 15 and more than 45 (COMPUTED: reproduces `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv`, column `eps_numeric`, for this level).

**In [9], all 54 levels against the Rust program.**

```python
def rust_text(x):
    """x written as the Rust program writes numbers: 16 digits, exponent like e0."""
    mantissa, exponent = f"{x:.15e}".split("e")  # Python writes e+00, Rust e0
    return f"{mantissa}e{int(exponent)}"
```

`f"{x:.15e}"` writes $x$ with 16 significant digits in scientific notation, for example `3.296908309775607e+00`; the program writes the exponent as `e0`. The function splits the text at the `e` and writes the exponent back as a whole number, which turns `+00` into `0` and `-10` into `-10`.

```python
CASES = [(1.0, 3.0), (1.0, 2.0), (2.0, 3.0)]  # the three cases (M, L) of the table
numeric_ours, shots_per_level = [], []
for r in ROWS:
    M, L = float(r["m"]), float(r["L"])
    G = round(G_CANONICAL * L / 3.0)  # 900 steps for L = 3, 600 for L = 2
    log = []
    numeric_ours.append(find_level(M, L, G, target(r["parity"], int(r["label"])),
                                   log=log))
    shots_per_level.append(len(log))
```

`CASES` names the three cases of the table (a reminder; the loop takes $M$ and $L$ from each row). For every row the level is found with the program's number of steps, $G = 900 L/3$, which keeps the step $h = 1/300$, and the number of shots is recorded.

```python
numeric_record = [float(r["eps_numeric"]) for r in ROWS]
identical = sum(rust_text(x) == r["eps_numeric"] for x, r in zip(numeric_ours, ROWS))
worst_numeric = max(abs(a - b) for a, b in zip(numeric_ours, numeric_record))
report("levels whose 16 digits equal the column eps_numeric", f"{identical} of 54")
report("largest |level (here) - eps_numeric (Rust program)|", f"{worst_numeric:.1e}")
report("shots per level (fewest, most, all 54 together)",
       f"{min(shots_per_level)}, {max(shots_per_level)}, {sum(shots_per_level)}")
```

`identical` counts the levels whose text, written as the program writes it, equals the record's text (`sum` of `True`/`False` values counts the `True` ones): 54 of 54 on the computer that made the record. The largest numerical difference is $8.9 \times 10^{-16}$, and the searches needed between 1 and 15 shots, 510 in all (COMPUTED).

```python
check(worst_numeric < 1e-12 and max(shots_per_level) <= 20,
      "all 54 shooting levels equal the column eps_numeric (at most 20 shots each)",
      record=f"{TABLE}, column eps_numeric")
zero_rows = [i for i, r in enumerate(ROWS) if r["parity"] == "even"
             and int(r["label"]) == 0]
check(all(numeric_ours[i] == 0.0 == numeric_record[i] for i in zero_rows),
      "the zero mode has the energy exactly 0 in all three cases",
      record=f"{SOLVER_REPORT}, check free_zero_mode_exact")
```

The first check allows $10^{-12}$ rather than requiring identical digits, because on another computer the system's `atan2` may round differently in the last binary place (COMPUTED: reproduces `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv`, column `eps_numeric`). The second finds the three zero-mode rows and requires the energy exactly 0 both here and in the record (the chained comparison `a == 0.0 == b` means `a == 0.0` and `0.0 == b`; COMPUTED: reproduces `Revision/kohn_sham/reports/ks-rust-solver.json`, check `free_zero_mode_exact`).

```python
differences_ours = [n - a for n, a in zip(numeric_ours, analytic_ours)]
pairs = list(zip(differences_ours, analytic_ours))
low_band = max(abs(d) for d, a in pairs if abs(a) < 4)  # all levels below 4 m
high_band = max(abs(d) for d, a in pairs if abs(a) >= 4)  # all levels from 4 m on
below_7 = max(abs(d) for d, a in pairs if 4 <= abs(a) < 7)
top = max(abs(a) for _, a in pairs)  # the highest level of the table
```

The numerical minus the exact level for every row, and the largest difference in three bands of $|\varepsilon|$: below $4m$, from $4m$ on, and from $4m$ to below $7m$; `top` is the highest level of the table.

```python
solver_report = json.loads(repository_file(SOLVER_REPORT).read_text(encoding="utf-8"))
detail = [c["detail"] for c in solver_report["checks"]
          if c["name"] == "free_k0_analytic_spectra"][0]
quoted = float(re.findall(r"max \|difference\| ([0-9.]+e-[0-9]+) for \|eps\| < 4 m",
                          detail)[0])
quoted_high = float(re.findall(r"([0-9.]+e-[0-9]+) for 4 m <= \|eps\| < 7 m",
                               detail)[0])
```

The cell reads the text of the program's check `free_k0_analytic_spectra` and finds in it the two numbers it quotes. `re.findall(pattern, text)` returns every piece of the text that matches the pattern; in the pattern, `[0-9.]+` is one or more digits or points, `e-[0-9]+` an exponent, `\|` a literal vertical bar, and the round brackets mark the part to return. The two numbers are $7.23 \times 10^{-10}$ (levels below $4m$) and $5.05 \times 10^{-8}$ (the second band).

```python
report("largest |numeric - exact| for |eps| < 4 m (here, record)",
       f"{low_band:.2e}, {quoted:.2e}")
report("largest |numeric - exact| for |eps| >= 4 m (here, record)",
       f"{high_band:.2e}, {quoted_high:.2e}")
say(f"Note: the record's check text names its second band 4 m <= |eps| < 7 m, but "
    f"the solver puts every level with |eps| >= 4 m into it, and the table's "
    f"levels reach {top:.4f} m; the quoted number belongs to that level. For "
    f"4 m <= |eps| < 7 m alone the largest difference is {below_7:.2e}.")
check(abs(low_band / quoted - 1) < 0.005 and abs(high_band / quoted_high - 1) < 0.005,
      "the two largest differences quoted by the solver check are reproduced",
      record=f"{SOLVER_REPORT}, check free_k0_analytic_spectra")
```

Both quoted numbers are reproduced: $7.23 \times 10^{-10}$ and $5.05 \times 10^{-8}$ (COMPUTED: reproduces `Revision/kohn_sham/reports/ks-rust-solver.json`, check `free_k0_analytic_spectra`). The printed note records a wording error in that record: its text calls the second band "$4m \le |\varepsilon| < 7m$", but the Rust code (file `Revision/kohn_sham/solver/src/spectrum.rs`) puts every level with $|\varepsilon| \ge 4m$ into it, and the table reaches $8.7539m$; the quoted $5.05 \times 10^{-8}$ belongs to that highest level, while for $4m \le |\varepsilon| < 7m$ alone the largest difference is $9.95 \times 10^{-9}$. The check's verdict is unaffected, because its tolerance $3 \times 10^{-7}$ covers both numbers.

**In [10], the orbitals.**

```python
def orbital(eps, M, L, G):
    """The normalised orbital on the fine grid of 2G + 1 points, made as the Rust
    program makes it.  Returns the arrays y, a, b."""
    h = L / G
    nf = 2 * G + 1  # nodes and step midpoints
    y = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))  # the fine grid, as in the program
    _, a_nodes, b_nodes, _ = shoot(eps, M, L, G, keep=True)[3]
```

The program's function `profile` rewritten. The fine grid has $2G + 1$ points (the nodes and the step midpoints); its positions are computed exactly as the program computes them, $y_f = -L\,(n_f - 1 - f)/(n_f - 1)$, which runs from $-L$ to 0 (the same formula, so that the rounding is the same). The shot with `keep=True` gives $a$ and $b$ at the $G + 1$ nodes.

```python
    da = M * a_nodes - eps * b_nodes  # the slopes a' at the nodes (the equations)
    db = eps * a_nodes - M * b_nodes  # the slopes b'
    a, b = np.zeros(nf), np.zeros(nf)
    a[0::2], b[0::2] = a_nodes, b_nodes  # the nodes take the even places
    a[1::2] = 0.5 * (a_nodes[:-1] + a_nodes[1:]) + h / 8.0 * (da[:-1] - da[1:])
    b[1::2] = 0.5 * (b_nodes[:-1] + b_nodes[1:]) + h / 8.0 * (db[:-1] - db[1:])
```

The slopes at the nodes come from the equations themselves. The node values fill the even places of the fine grid (`0::2`: every second place from 0), and the odd places (`1::2`) get the cubic Hermite midpoint values $(f_0 + f_1)/2 + h(f_0' - f_1')/8$ of Section 2.24, for all steps at once.

```python
    half = 0.5 * h  # the spacing of the fine grid
    weights = np.full(nf, 2.0 * half / 3.0)  # Simpson: 2 at the even inner places
    weights[1::2] = 4.0 * half / 3.0  # 4 at the odd places (the midpoints)
    weights[0] = weights[-1] = half / 3.0  # 1 at the two ends
    scale = 1.0 / math.sqrt(np.sum(weights * (a * a + b * b)))
    return y, a * scale, b * scale
```

Simpson's weights for the spacing $h/2$: $\frac{h/2}{3}$ times 1 at the ends, 4 at the odd places and 2 at the inner even places (`np.full` makes an array filled with one value). The norm $\int(a^2 + b^2)dy$ is the weighted sum, and the orbital is divided by its square root, so that $\int(a^2 + b^2)dy = 1$.

```python
fig, axes = plt.subplots(2, 2, figsize=(9.0, 6.4), sharex=True)
residuals = []
for ax, (parity, label) in zip(axes.flat, [("even", 0), ("odd", 0), ("even", 1),
                                          ("odd", 2)]):
    eps = level_of[(parity, label)]
    y_fine, a_fine, b_fine = orbital(eps, M1, L3, 900)
    end = b_fine[-1] if parity == "even" else a_fine[-1]  # must vanish at y = 0
    residuals.append(abs(end))
```

A figure with $2 \times 2$ panels sharing the horizontal axis; `axes.flat` walks through the four panels. For four levels the orbital is built and the component that the brane condition must make zero ($b(0)$ for even, $a(0)$ for odd) is recorded.

```python
    ax.plot(y_fine, a_fine, color=BLUE, lw=1.5, label="$a(y)$")
    ax.plot(y_fine, b_fine, color=ORANGE, lw=1.5, ls="--", label="$b(y)$")
    ax.axhline(0.0, color=BLACK, lw=0.6)
    ax.set_title(f"{parity}, $l = {label}$, $\\varepsilon = {eps:.4f}$", fontsize=10)
    ax.legend(fontsize=8, loc="upper left")
```

Each panel draws $a(y)$ (solid blue) and $b(y)$ (dashed orange) with the zero line and a title naming the level.

```python
    if parity == "even" and label == 0:  # the zero mode against its exact form
        exact_a = math.sqrt(2 * M1 / (1 - math.exp(-2 * M1 * L3))) * np.exp(M1 * y_fine)
        zero_mode_distance = np.max(np.abs(a_fine - exact_a))
        zero_mode_b = np.max(np.abs(b_fine))
```

For the zero mode the exact normalised form is $a = \sqrt{2M/(1 - e^{-2ML})}\, e^{My}$, $b = 0$ (the factor makes $\int_{-L}^{0} a^2 dy = 1$, because $\int_{-L}^0 e^{2My}dy = (1 - e^{-2ML})/(2M)$). The cell records the largest distance of the computed $a$ from it and the largest $|b|$.

```python
for ax in axes[1]:
    ax.set_xlabel("hidden coordinate $y$ (units $1/H$)")
for ax in axes[:, 0]:
    ax.set_ylabel("component (units $H^{1/2}$)")
save_figure(fig, "orbitals",
            "The normalised orbitals of four levels of the case $M = 1$, $L = 3$: "
            ...)
```

Axis labels on the bottom row (`axes[1]`) and the left column (`axes[:, 0]`); the components carry the unit $H^{1/2}$ because $\int(a^2 + b^2)dy = 1$ with $y$ in units of $1/H$. The saved figure is `02d_6_orbitals.png`. **What Figure 02d.6 shows:** the zero mode ($a \propto e^{y}$, $b = 0$) is concentrated at the brane; every orbital has $b = 0$ at the tip $y = -3$; at the brane the even orbitals have $b = 0$ and the odd ones $a = 0$; higher levels oscillate more.

```python
report("largest brane residual |b(0)| or |a(0)|", f"{max(residuals):.1e}")
zero_detail = [c["detail"] for c in solver_report["checks"]
               if c["name"] == "free_zero_mode_exact"][0]
zero_quoted = float(re.findall(r"e\^\(My\) to ([0-9.]+e-[0-9]+)", zero_detail)[0])
report("zero mode: largest distance from the exact normalised form (here, record)",
       f"{zero_mode_distance:.2e}, {zero_quoted:.2e}")
```

The largest brane residual is $8.6 \times 10^{-16}$. The text of the program's check `free_zero_mode_exact` quotes the distance of the computed zero mode from its exact form after the words `e^(My) to`; in the pattern, `\^`, `\(` and `\)` stand for the literal characters. Both distances are $1.35 \times 10^{-12}$ (COMPUTED).

```python
check(max(residuals) < 1e-10, "every orbital meets its brane condition within 1e-10")
check(zero_mode_b == 0.0 and abs(zero_mode_distance / zero_quoted - 1) < 0.01,
      "the zero mode: b = 0 exactly, distance 1.35e-12 from sqrt(2M/(1 - e^(-2ML))) "
      "e^(My)", record=f"{SOLVER_REPORT}, check free_zero_mode_exact")
```

Two checks: the brane conditions hold within $10^{-10}$; the zero mode has $b$ exactly 0 and reproduces the quoted distance within 1 per cent (COMPUTED: reproduces `Revision/kohn_sham/reports/ks-rust-solver.json`, check `free_zero_mode_exact`).

**In [11], how the error depends on the step.**

```python
G_LIST = [25, 50, 100, 200, 400, 800]
tracked = [("even", 1), ("odd", 2), ("even", 5)]
fig, ax = plt.subplots()
orders = []
```

Six step counts and three levels to follow.

```python
for (parity, label), color, marker in zip(tracked, [BLUE, ORANGE, AQUA],
                                          ["o", "s", "^"]):
    exact = exact_level(M1, L3, parity, label)
    errors = np.array([abs(find_level(M1, L3, G, target(parity, label)) - exact)
                       for G in G_LIST])
    h_list = L3 / np.array(G_LIST, dtype=float)
    fit = errors > 1e-11  # leave out points limited by the root tolerance
    orders.append(np.polyfit(np.log10(h_list[fit]), np.log10(errors[fit]), 1)[0])
    ax.loglog(h_list, errors, marker=marker, color=color, ms=5, lw=1.2,
              label=f"{parity} $l = {label}$ ($\\varepsilon = {exact:.4f}$)")
```

For each level the search is repeated with every step count and the error against the exact level is stored; a straight line is fitted through the errors above $10^{-11}$ (below that the root tolerance and rounding interfere), and its slope (element 0 of `polyfit`'s result) is the measured order. The errors are drawn on a log-log plot.

```python
h_guide = L3 / np.array(G_LIST, dtype=float)
ax.loglog(h_guide, 2e-3 * (h_guide / h_guide[0]) ** 4, "--", color=GREY,
          label="slope 4")
ax.axvline(L3 / 900, color=BLACK, ls=":", lw=1.0)
ax.text(L3 / 900 * 1.08, 1e-4, "the record's\nstep 1/300", fontsize=8)
```

A guide of slope 4, and a dotted vertical line at the record's step $h = 3/900 = 1/300$ with a two-line label (`\n` starts a new line).

```python
ax.set_xlabel("RK4 step $h = L/G$ (units $1/H$)")
ax.set_ylabel("error of the level (units $m$)")
ax.set_title("The levels converge like $h^4$")
ax.legend(loc="lower right", fontsize=8)
save_figure(fig, "level_convergence",
            "The error of three levels of the case $M = 1$, $L = 3$ found by "
            ...)
report("measured orders", ", ".join(f"{q:.2f}" for q in orders))
check(all(3.8 < q < 4.2 for q in orders), "the level errors fall like h^4")
```

Labels and the saved figure `02d_7_level_convergence.png`; the measured orders are 4.00, 3.99 and 3.97 (COMPUTED), and the check requires them between 3.8 and 4.2. **What Figure 02d.7 shows:** three parallel lines of slope 4; the higher the level, the larger its error at a given step; at the record's step $1/300$ the errors are far below $10^{-6}$.

**In [12], why the error grows with the level.**

```python
w = sp.symbols("omega", positive=True)  # the angle turned in one step, eps h
R_rk4 = 1 + sp.I * w - w ** 2 / 2 - sp.I * w ** 3 / 6 + w ** 4 / 24  # R(i omega)
turned = sp.atan(sp.im(R_rk4) / sp.re(R_rk4))  # the angle of R(i omega)
lag = sp.series(turned - w, w, 0, 7).removeO()
say(f"angle of R(i omega) - omega = {lag} + ...")
check(sp.simplify(lag + w ** 5 / 120) == 0,
      "one RK4 step turns by omega - omega^5/120: the phase lags")
```

`R_rk4` is $R(i\omega)$ written out (Section 2.7). `sp.im` and `sp.re` take its imaginary and real parts, and the arctangent of their quotient is its angle (for small $\omega$ the real part is positive, so no turn is lost). `sp.series(..., w, 0, 7)` expands the angle minus $\omega$ up to $\omega^6$; the printout is `-omega**5/120`, and the check confirms the phase lag $\omega^5/120$ derived in Section 2.24.

```python
nonzero = [i for i, a in enumerate(analytic_record) if a != 0.0]
eps_abs = np.array([abs(analytic_record[i]) for i in nonzero])
x_values = eps_abs / 300.0  # h |eps| with h = 1/300
record_diff = np.array([abs(float(ROWS[i]["difference"])) for i in nonzero])
our_diff = np.array([abs(differences_ours[i]) for i in nonzero])
masses = np.array([float(ROWS[i]["m"]) for i in nonzero])
```

The 51 rows with a nonzero level (all except the three zero modes): their sizes $|\varepsilon|$, the quantity $h|\varepsilon|$ with $h = 1/300$ (the same step for all three cases), the record's column `difference` (numerical minus exact level), our own differences from In [9], and the masses.

```python
fig, ax = plt.subplots()
for mass, color in ((1.0, BLUE), (2.0, ORANGE)):
    pick = masses == mass
    ax.loglog(x_values[pick], record_diff[pick] / eps_abs[pick], "o", color=color,
              ms=6, label=f"record, $M = {mass:.0f}$")
ax.loglog(x_values, our_diff / eps_abs, "x", color=BLACK, ms=5,
          label="this notebook")
x_guide = np.linspace(x_values.min(), x_values.max(), 50)
ax.loglog(x_guide, x_guide ** 4 / 120, "--", color=GREY,
          label="prediction $(h\\varepsilon)^4/120$")
```

The relative errors $\delta\varepsilon/|\varepsilon|$ of the record (dots, blue for $M = 1$ and orange for $M = 2$; `pick` selects the rows of one mass) and of this notebook (black crosses) against $h|\varepsilon|$ on log-log axes, with the prediction $(h\varepsilon)^4/120$ of Section 2.24 as a dashed line.

```python
ax.set_xlabel("$h |\\varepsilon|$ with $h = 1/300$ (pure number)")
ax.set_ylabel("relative error $\\delta\\varepsilon / |\\varepsilon|$")
ax.set_title("The RK4 error of all 51 nonzero levels of the record")
ax.legend(loc="upper left", fontsize=8)
save_figure(fig, "record_differences",
            "The relative error $\\delta\\varepsilon/|\\varepsilon|$ of the "
            ...)
```

Labels and the saved figure `02d_8_record_differences.png`. **What Figure 02d.8 shows:** the crosses sit on the record's dots (our shooting reproduces the program's errors); all points lie below the dashed prediction, and the levels far above the mass approach it, while those near the mass (where the point does not turn uniformly) lie further below.

```python
ratio = (record_diff / eps_abs) / (x_values ** 4 / 120)
report("error / prediction for the levels above 7 m",
       ", ".join(f"{q:.3f}" for q in ratio[eps_abs > 7]))
check(np.all(ratio < 1) and np.all(ratio[eps_abs > 7] > 0.9),
      "every level error lies below the prediction, within 10 % above 7 m")
```

The ratio of each measured relative error to the prediction; for the three levels above $7m$ it is 0.934, 0.953 and 0.955 (COMPUTED). The check requires every ratio below 1 and those above $7m$ above 0.9.

```python
report("largest |difference (here) - difference (record)|",
       f"{np.max(np.abs(record_diff - our_diff)):.1e}")
check(np.max(np.abs(record_diff - our_diff)) < 1e-12,
      "our differences equal the record's column difference within 1e-12",
      record=f"{TABLE}, column difference")
```

Our differences equal the record's column `difference` to $1.8 \times 10^{-15}$ (COMPUTED: reproduces `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv`, column `difference`).

**In [13], the last check.**

```python
names = ["pruefer_staircase", "staircase_slope", "angle_along_y",
         "odd_level_equation", "newton_vs_bisection", "orbitals",
         "level_convergence", "record_differences"]
present = [output_file(f"{FIGURE_FOLDER}/02d_{k}_{name}.png").is_file()
           for k, name in enumerate(names, 1)]
check(all(present), f"all {len(names)} figure files of notebook 02d exist")
all_checks_passed()
```

As in Notebook 02a: the eight figure files must exist, and the last line is ALL 17 CHECKS PASSED (notebook 02d). The 17 checks are: 1 in In [2], 1 in In [3], 1 in In [4], 2 in In [5], 1 in In [7], 1 in In [8], 3 in In [9], 2 in In [10], 1 in In [11], 3 in In [12] and 1 in In [13].

### 2.29 What we proved, what we computed, what we assumed

**PROVED in this chapter** (by elementary algebra and calculus, each derivation written out line by line; every one is also confirmed by a check of a notebook):

- along the history $a_4 = A H x_4$ the extra-time scale factor obeys $ds_5/dx_4 = -AH\, s_5$ (it deflates exponentially) and the 3-space factor $ds_1/dx_4 = +AH\, s_1$; their product is constant (Section 2.2); the oscillator conserves $E = (x^2 + v^2)/2$;
- one step of size $1/2$ for $y' = -y$ gives $1/2$, $5/8$ and $233/384$; the amplification factors of Euler, midpoint and RK4 are the first 2, 3 and 5 terms of the series of $e^{z}$ (Sections 2.4 and 2.5);
- to leading order, the error of a method of order $p$ for Problem A at $t = 1$ is $e^{-1}(-1)^p h^p/(p+1)!$; halving the step divides an error $C h^p$ by $2^p$; Richardson's estimate $(Y_h - Y_{h/2})/(2^p - 1)$ (Section 2.6);
- the energy factors per step $1 + h^2$, $1 + h^4/4$, $1 - h^6/72 + h^8/576$ and the scale-factor product factors $1 - h^2$ (Euler) and $1 + h^6/72 + h^8/576$ (RK4) (Section 2.7);
- the string's eigenvalues $n^2\pi^2$; the secant formula; the even and odd conditions of the finite well, $\tan z = \sqrt{z_0^2 - z^2}/z$ and $-\cot z = \sqrt{z_0^2 - z^2}/z$, and its four bound states for $z_0 = \sqrt{30}$; the tail integral $1/(2\kappa)$; the orthogonality of states of different parity; Simpson's weights (Sections 2.12 and 2.13);
- the partial derivatives of $x^2\sin y$; the linear approximation; the gradient is perpendicular to the level curves and points uphill; the orders 1 and 2 of the forward and central differences and the scale of the best spacing (Section 2.18);
- $\partial_8 = 6H\, d/dz$; the rates $\pm a_4'$, $H\cot z$ and $-6H/(\sin z\cos z)$ of the scale factors; $\det g = \cos^2 z$ and $\sqrt{|\det g|} = \sin z\cot z = \cos z$, independent of $x_4$ for every $a_4(x_4)$, because the inflation of 3-space and the deflation of the extra times cancel; Jacobi's formula for a diagonal metric; the 25 nonzero Christoffel entries, given their formula (Section 2.19);
- the exact levels of the free Kohn-Sham block (the zero mode, $\pm\sqrt{M^2 + (n\pi/L)^2}$, $\pm\sqrt{M^2 + p^2}$ with $\tan(pL) = -p/M$) and the absence of any other level with $|\varepsilon| \le M$; the Prüfer equation $\theta' = \varepsilon - M\sin 2\theta$; $d\Phi/d\varepsilon = \int r^2 dy/r(0)^2 > 0$, so every level is found exactly once with its own label; the slope $(1 - e^{-2ML})/(2M)$ at $\varepsilon = 0$; the cubic Hermite midpoint formula; the RK4 phase lag $\omega^5/120$ per step and the level error $\delta\varepsilon \approx \varepsilon^5 h^4/120$ far above the mass (Section 2.24).

**COMPUTED by the notebooks** (each number in the cell named; where a Revision record is reproduced, the record file and its key or check):

- Notebook 02a: measured orders 1.0014, 2.0025, 4.0439 (In [7]); halving ratios 2.00020, 4.00073, 16.1047 (In [9]); the smallest RK4 error $1.110 \times 10^{-16}$ at $N = 4096$ and $5.773 \times 10^{-15}$ at $N = 262144$ (In [10]); the Revision solver's step $h = L/G = 3/900 = 1/300$ and the history constants $A = H = 1$ (In [11]; reproduces `Revision/kohn_sham/results/parameters.json`, keys `rk4Steps`, `L_tipCutoff`, `historyA` and `H`); the errors at that step, $-6.1399 \times 10^{-4}$, $+6.8296 \times 10^{-7}$, $+3.7920 \times 10^{-13}$, within 0.3 per cent of the predictions (In [11]); the oscillator energies (In [12], In [13]); Richardson's estimate within 6 per cent from $N = 8$ on (In [14]).
- Notebook 02b: the RK4 eigenvalue of the string 9.869604411103, within $1.0 \times 10^{-8}$ of $\pi^2$; 45 bisection steps against about 9 secant steps (In [5]); the four well levels $-14.1206$, $-11.5181$, $-7.3330$, $-2.0437$ (In [6]) and their shooting values within $10^{-7}$ (In [8]); nodes 0, 1, 2, 3 and orthonormality within $1.6 \times 10^{-10}$ (In [10]); orders 3.99, 3.98, 3.96, 3.92 (In [11]).
- Notebook 02c: the best finite-difference spacings $1.0 \times 10^{-8}$, $1.8 \times 10^{-6}$, $5.6 \times 10^{-5}$ (In [6]); the metric (In [8]; reproduces `Revision/gkd_lovelock/results/curvature.json`, key `metricDiagonal`); the volume factor (In [11]; reproduces the same record's key `sqrtAbsDetG` and `Revision/field_equations_a4/reports/wolfram-a4-report.json`, check `sqrt_abs_det_g_is_cos_z`); all 25 Christoffel entries (In [12]; reproduces `Revision/gkd_lovelock/results/curvature.json`, key `christoffelNonzero_b_le_c`).
- Notebook 02d: all 54 levels of the free spectrum, identical in all 16 printed digits on the computer that made the record, largest difference $8.9 \times 10^{-16}$ (In [9]; reproduces `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv`, column `eps_numeric`); the exact column to $1.8 \times 10^{-15}$ (In [7]; column `eps_analytic`) and the column `difference` to $1.8 \times 10^{-15}$ (In [12]); the zero mode exactly 0 and its distance $1.35 \times 10^{-12}$ from the exact form (In [9], In [10]; reproduces `Revision/kohn_sham/reports/ks-rust-solver.json`, check `free_zero_mode_exact`); the quoted largest differences $7.23 \times 10^{-10}$ and $5.05 \times 10^{-8}$ (In [9]; reproduces the same report's check `free_k0_analytic_spectra`, whose text misnames its second band as "$4m \le |\varepsilon| < 7m$" although it contains every level from $4m$ up to $8.7539m$; for the band below $7m$ alone the largest difference is $9.95 \times 10^{-9}$; the verdict is unaffected); Newton with 9 shots against bisection with 48 (In [8]); orders 4.00, 3.99, 3.97 (In [11]); errors 0.934 to 0.955 times the phase-lag prediction above $7m$ (In [12]).

**ASSUMED** (used, not derived here):

- standard theorems of calculus and numerical analysis, quoted without proof: the existence and uniqueness of solutions of initial-value problems (Picard and Lindelöf); Taylor's theorem; the intermediate value theorem; Schwarz's theorem; the mean value theorem; the speed of the secant rule (digits multiplied by about 1.618) and of Newton's method (digits doubled); the $h^4$ error orders of Simpson's rule and of cubic Hermite interpolation;
- from quantum mechanics, used only as an example: the Schrödinger equation, the uniqueness (up to a factor) of a one-dimensional bound state, and the orthogonality of states of different energies;
- the formula of the Christoffel symbols (derived in Chapter 3) and the Kohn-Sham block equations (taken from `Revision/kohn_sham/ks-theory.json`; derived in Chapter 14);
- the linear history $a_4 = A H x_4$ with $A = 1$, a PRESCRIBED BACKGROUND, not a solution of the field equations with the Kohn-Sham source (`Revision/field_equations_a4/reports/ks-source-conditions.json`, check `ks_history_is_a_prescribed_background`);
- the brane conditions $b(0) = 0$ or $a(0) = 0$, which rest on the mirror symmetry that the record labels ASSUMED; the tip condition $b(-L) = 0$ is a choice of the model ("chosen (regular tip)").

**HYPOTHESIS and OPEN.** No hypothesis enters this chapter, and it leaves no question open. It does not show where the Kohn-Sham equations come from or what their levels mean physically; that is the work of Chapters 14 and 15.

### 2.30 Exercises

**Exercise 1.** Make one Euler step and one midpoint step for $y' = -2y$ from $y(0) = 1$ with the step $h = 1/4$, with exact fractions. Compare with Section 2.4 and explain the agreement.

*Answer.* Euler: $y_1 = 1 + \frac14 \cdot (-2) = \frac12$. Midpoint: $k_1 = -2$; the midpoint value is $1 + \frac18 \cdot (-2) = \frac34$; $k_2 = -2 \cdot \frac34 = -\frac32$; $y_1 = 1 + \frac14 \cdot (-\frac32) = 1 - \frac38 = \frac58$. These are the same numbers as for $y' = -y$ with $h = 1/2$ in Section 2.4, because one step of each method multiplies $y$ by $R(z)$, which depends only on $z = \lambda h$, and here $z = -2 \cdot \frac14 = -\frac12$ as there: $R_{\rm Euler}(-\frac12) = \frac12$ and $R_{\rm midpoint}(-\frac12) = 1 - \frac12 + \frac18 = \frac58$.

**Exercise 2.** A method gives the errors $2.0 \times 10^{-4}$ with $h = 0.1$ and $1.25 \times 10^{-5}$ with $h = 0.05$. What is its order, and what error do you expect with $h = 0.025$?

*Answer.* Halving the step divided the error by $2.0 \times 10^{-4}/1.25 \times 10^{-5} = 16 = 2^4$, so (Section 2.6) the order is $p = 4$. Halving again divides by 16 once more: about $1.25 \times 10^{-5}/16 = 7.8 \times 10^{-7}$. Equivalently, the slope on a log-log plot is $(\log_{10} 1.25 \times 10^{-5} - \log_{10} 2.0 \times 10^{-4})/(\log_{10} 0.05 - \log_{10} 0.1) = (-1.2041)/(-0.30103) = 4.0$.

**Exercise 3.** Two RK4 runs of Problem A up to $t = 1$ give $Y_h = 0.3678802720$ (8 steps) and $Y_{h/2} = 0.3678794905$ (16 steps). Without using $e^{-1}$, estimate the error of $Y_{h/2}$ and give the extrapolated value. Then compare with $e^{-1} = 0.3678794412$.

*Answer.* By Richardson's rule (Section 2.6) with $p = 4$, the error of $Y_{h/2}$ is about $(Y_h - Y_{h/2})/15 = 7.815 \times 10^{-7}/15 = 5.21 \times 10^{-8}$. The extrapolated value is $Y_{h/2} - 5.21 \times 10^{-8} = 0.3678794384$. The true error of $Y_{h/2}$ is $0.3678794905 - 0.3678794412 = 4.93 \times 10^{-8}$ (the estimate is 6 per cent too large), and the extrapolated value is off by only $-2.8 \times 10^{-9}$, about 17 times better; these are the numbers of the row $N = 8 \to 16$ printed by Notebook 02a, In [14].

**Exercise 4.** Using the energy factor of the midpoint method (Section 2.7), compute the oscillator's energy after 50 steps of $h = 0.2$, starting from $E_0 = 1/2$.

*Answer.* Each step multiplies $E$ by $1 + h^4/4 = 1 + 0.0016/4 = 1.0004$. After 50 steps $E = \frac12 \cdot 1.0004^{50}$. With $1.0004^{50} = e^{50\ln 1.0004} = e^{50 \cdot 0.00039992} = e^{0.019996} = 1.020197$, we get $E = 0.5100986$, the value 0.5100986302 printed by Notebook 02a, In [12].

**Exercise 5.** How many bound states does a finite square well of half-width $a = 1$ have when its depth is $V_0 = 2$? And when $V_0 = 1$?

*Answer.* The number is the number of intervals of length $\pi/2$ that begin below $z_0 = a\sqrt{2V_0}$ (Section 2.13). For $V_0 = 2$: $z_0 = 2$ and $z_0/(\pi/2) = 1.27$, so two intervals begin below $z_0$ (at 0 and at $\pi/2 = 1.571$): two bound states, one even and one odd. For $V_0 = 1$: $z_0 = \sqrt2 = 1.414 < \pi/2$: one bound state, the even ground state. (A symmetric well in one dimension always has at least one bound state, however shallow, because the first interval starts at 0.)

**Exercise 6.** Plain bisection starts from the bracket $(-12, 12)$ and stops when the bracket is narrower than $10^{-13}$. How many shots does it need?

*Answer.* After $k$ shots the width is $24/2^k$ (Section 2.12). We need $24/2^k \le 10^{-13}$, that is $2^k \ge 2.4 \times 10^{14}$, or $k \ge \log_2(2.4 \times 10^{14}) = \log_{10}(2.4 \times 10^{14})/\log_{10} 2 = 14.380/0.30103 = 47.8$. So $k = 48$ shots, the number printed by Notebook 02d, In [8].

**Exercise 7.** Show that the free block of Section 2.24 has no level with $\varepsilon = +M$ or $\varepsilon = -M$.

*Answer.* For $\varepsilon^2 = M^2$ the equation $a'' = (M^2 - \varepsilon^2)a$ becomes $a'' = 0$, so $a = \alpha + \beta y$ with constants $\alpha$, $\beta$, and $b = (Ma - a')/\varepsilon$ vanishes where $Ma - a' = M(\alpha + \beta y) - \beta = 0$. Even orbitals need this at $y = 0$ and at $y = -L$: $M\alpha - \beta = 0$ and $M\alpha - M\beta L - \beta = 0$; subtracting the first from the second gives $-M\beta L = 0$, so $\beta = 0$ (because $M > 0$ and $L > 0$), and then $\alpha = \beta/M = 0$. Odd orbitals need $a(0) = \alpha = 0$ and the tip condition $M(-\beta L) - \beta = -\beta(ML + 1) = 0$, so $\beta = 0$. In both cases $a = 0$, and then $b = 0$: no level.

**Exercise 8.** Check the cubic Hermite midpoint formula $(f_0 + f_1)/2 + h(f_0' - f_1')/8$ of Section 2.24 on $f(s) = s^2$ and $f(s) = s^3$ on the step $0 \le s \le h$.

*Answer.* For $s^2$: $f_0 = 0$, $f_1 = h^2$, $f_0' = 0$, $f_1' = 2h$; the formula gives $\frac{h^2}{2} + \frac{h}{8}(0 - 2h) = \frac{h^2}{2} - \frac{h^2}{4} = \frac{h^2}{4} = (h/2)^2$, the exact value at $s = h/2$. For $s^3$: $f_0 = 0$, $f_1 = h^3$, $f_0' = 0$, $f_1' = 3h^2$; the formula gives $\frac{h^3}{2} - \frac{3h^3}{8} = \frac{h^3}{8} = (h/2)^3$, exact again. (It is exact for every polynomial of degree at most 3, because then the cubic through the four data is the polynomial itself.)

**Exercise 9.** For $M = 0$ the Prüfer equation is $\theta' = \varepsilon$. Find the even and odd levels directly from it and compare with the formulas of Section 2.24 at $M = 0$.

*Answer.* With $\theta(-L) = 0$ and $\theta' = \varepsilon$ we get $\theta(y) = \varepsilon(y + L)$, so $\Phi = \varepsilon L$. Even: $\varepsilon L = l\pi$, $\varepsilon = l\pi/L$. Odd: $\varepsilon L = \pi/2 + l\pi$, $\varepsilon = (l + \frac12)\pi/L$. The general formulas give the same: $\pm\sqrt{0 + (n\pi/L)^2} = \pm n\pi/L$ for the even levels; and as $M \to 0$ the odd condition $\tan(pL) = -p/M$ demands an infinitely large tangent, $pL = (n + \frac12)\pi$, so $\pm p = \pm(n + \frac12)\pi/L$.

**Exercise 10.** Compute $\partial_8 g_{11}$ for $g_{11} = e^{2a_4}\sin^{1/3}(6Hx_8)$, and use it to confirm the Christoffel entry $\Gamma^1{}_{18} = H\cot z$ of Section 2.19.

*Answer.* With $z = 6Hx_8$: $\partial_8 \sin^{1/3} z = \frac13 \sin^{-2/3} z \cdot \cos z \cdot 6H = 2H\sin^{-2/3} z\cos z$ (the power rule, the derivative of the sine, and the chain rule with $\partial z/\partial x_8 = 6H$). So $\partial_8 g_{11} = 2H e^{2a_4}\sin^{-2/3} z\cos z$. Then $\Gamma^1{}_{18} = \partial_8 g_{11}/(2g_{11}) = 2H e^{2a_4}\sin^{-2/3}z\cos z/(2e^{2a_4}\sin^{1/3} z) = H\cos z/\sin z = H\cot z$ (the factors $e^{2a_4}$ cancel and $\sin^{-2/3} z/\sin^{1/3} z = 1/\sin z$), the value listed in the record and in the table of Section 2.19.
