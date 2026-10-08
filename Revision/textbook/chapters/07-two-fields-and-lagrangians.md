## 7. The two fields and their Lagrangians; Grassmann numbers; Euler-Lagrange equations

This chapter writes down the laws that the two fields of the book obey in the author's primordial gravitational field. A law of this kind is not guessed equation by equation. One writes down a single function, the **Lagrangian**, and a single principle, the **principle of stationary action**, and the field equations follow from them by a fixed recipe, the **Euler-Lagrange equations**. The chapter teaches the recipe from zero, then the strange numbers (Grassmann numbers) of which the field dirac16complex is made, then the Lagrangian of the two fields, its field equations written out in the author's metric, and finally what happens to real fields and why charge conjugation is a matrix.

### 7.1 What this chapter does

**The two fields.** The book studies two fields that live on the author's eight-dimensional space-time. Both attach to every point of space-time a column of 16 complex numbers $\Psi = (\Psi_1, \dots, \Psi_{16})$, and both change under the turnings of the eight directions in the same way, as a **spinor** of the group Pin(4,4) (Chapter 5). They differ in one respect only, the kind of numbers their 16 components are:

- **dirac16complex** has components that **anticommute**: for two of its components $\Psi_A\Psi_B = -\Psi_B\Psi_A$. Ordinary numbers cannot do this; the numbers that can are called **Grassmann numbers**, and Sections 7.10 to 7.13 build them from nothing. The Revision record defines the components of dirac16complex as Grassmann numbers (Revision/SPEC.md, section 3); this field is later turned into a quantum field (Chapter 10).
- **dirac16complex00** has ordinary commuting complex components. It is a classical field, the 16-component analogue in eight dimensions of the four-component wave function that Dirac wrote down in 1928; it is not quantised.

**The coordinates.** As everywhere in this book, the eight coordinates carry the author's names $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates; $x_4$ is the time; $x_5, x_6, x_7$ are three **extra times**, time-like directions which **deflate exponentially** as 3-space inflates; $x_8$ is the hidden space direction. With $z = 6Hx_8$, $0 < z < \pi/2$, the author's constant $H > 0$ and a function $a_4(x_4)$ of the time, the author's metric is (Chapter 3)

$$
ds^2 = e^{2a_4}\sin^{1/3}z\,(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 - e^{-2a_4}\sin^{1/3}z\,(dx_5^2 + dx_6^2 + dx_7^2) + \cot^2 z\,dx_8^2 .
$$

3-space has the scale factor $e^{a_4}\sin^{1/6}z$, the three extra times the scale factor $e^{-a_4}\sin^{1/6}z$: when $a_4$ grows, 3-space inflates and the extra times deflate. The signature is (4,4): $x_1, x_2, x_3, x_8$ are space-like (positive entries), $x_4, x_5, x_6, x_7$ time-like (negative entries).

**What the chapter derives, in order.**

- Sections 7.2 to 7.5: the action, the principle of stationary action, and the Euler-Lagrange equation, from one-variable calculus only; what changes for fields; and the first sign that the extra times are unusual: a wave along an extra time grows instead of oscillating. Notebook 07d computes every step (30 checks, 8 figures).
- Sections 7.10 to 7.13: Grassmann numbers from zero, the rules for their products, conjugation and derivatives, which bilinear forms survive for real columns, the powers of the scalar density $S = \bar\Psi\Psi$ (defined in Section 7.12; $S^{17} = 0$), and field equations with Grassmann numbers. Notebook 07a builds a Grassmann algebra in a few lines of Python (38 checks, 7 figures).
- Sections 7.18 to 7.23: the geometry the fields live in, the common Lagrangian of the two fields, its reality, the total divergence, why the spin connection drops out of the Lagrangian but not out of the field equation, the Euler-Lagrange equations of both fields, their explicit, block and evolution forms in the author's metric, non-triviality [1] and [2] with their exact scope, and an exact family of solutions. Notebook 07b derives all of it exactly and compares it with the Revision record (47 checks, 6 figures).
- Sections 7.28 and 7.29: real fields; the author's Majorana-type Lagrangian, which is empty for real Grassmann fields (the negative control of the Revision record); and why **charge conjugation is a matrix**: for a real field, plain complex conjugation changes nothing. Notebook 07c computes the charge-conjugation matrices $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$ and the mass reversal by the real matrix $\Gamma$ (23 checks, 4 figures).
- Section 7.34 lists what was proved, computed and assumed; Section 7.35 has exercises with complete answers.

**The notebooks.** The four notebooks appear in the order d, a, b, c, because Notebook 07d derives the recipe that the other three use. Each is complete in itself and may be run in any order. Before each notebook the book prints the complete instructions to run it, then the complete text of the notebook with its outputs and figures, then a section that explains every line of its code.

**Statuses.** Every statement carries one of five labels. PROVED: exact, derived here line by line and, where the Revision record contains it, verified there by a named check of a named report. COMPUTED: a number produced by a program, with its uncertainty. ASSUMED: used, not derived. HYPOTHESIS: a proposal that is being investigated and is not claimed. OPEN: a question that is not answered. The Revision reports cited in this chapter are `Revision/theory/reports/python-field-theory.json` (the sympy verifier, 70 of 70 checks pass), `Revision/theory/reports/wolfram-field-theory.json` (the Wolfram verifier, 84 of 84 checks pass), `Revision/theory/reports/python-scope.json` (14 of 14) and `Revision/theory/reports/wolfram-scope.json` (15 of 15) for the scope of the statements, the formula record `Revision/theory/field-theory.json`, and `Revision/lead_checks/reports/charge-conjugation-and-u1.json` (12 of 12) for charge conjugation. These counts are those that the reports state at the time of writing; each notebook reads the checks it relies on from the reports themselves and stops if one is missing or does not pass.

### 7.2 Paths, the action and the first variation

We begin with the simplest possible system, a particle that moves along a line, and learn the principle there. Everything carries over to fields in Section 7.5.

**A path.** A **path** (or motion) is a function $q(t)$ that gives the position $q$ of the particle at every time $t$ between a start time $0$ and an end time $T$. Its **velocity** is $\dot q = dq/dt$ and its **acceleration** $\ddot q = d^2q/dt^2$ (a dot over a letter is the derivative with respect to the time $t$).

**The Lagrangian.** A **Lagrangian** is a function $L(q, \dot q)$ of the position and the velocity. For the **oscillator**, a particle of mass 1 on a spring, it is the kinetic energy minus the potential energy:

$$
L(q, \dot q) = \tfrac12\dot q^2 - \tfrac12\omega^2 q^2 ,
$$

where $\omega > 0$ is a fixed number, the **angular frequency** of the spring. Here $L$ is a function of two ordinary variables; we call them $q$ and $\dot q$ because along a path we shall put the position and the velocity of the path into them. The two **partial derivatives** of $L$ (Chapter 2) are $\partial L/\partial q = -\omega^2 q$ (the velocity held fixed) and $\partial L/\partial\dot q = \dot q$ (the position held fixed).

**The action.** The **action** of a path is one number for the whole path:

$$
S[q] = \int_0^T L\big(q(t), \dot q(t)\big)\,dt .
$$

At every time we put the position and the velocity of the path into $L$ and add up (integrate) the values over the time interval. The square brackets in $S[q]$ say that $S$ depends on the whole function $q$, not on one number; a rule that takes a function and gives a number is called a **functional**.

**The principle of stationary action** (ASSUMED: it is the starting principle of classical mechanics and of classical field theory, not derived from anything simpler). Among all paths with the same end values $q(0) = q_A$ and $q(T) = q_B$, the particle follows one whose action does not change to first order when the path is changed a little. To make "changed a little" precise, take a fixed **shape** $\xi(t)$ with $\xi(0) = \xi(T) = 0$ (so that the changed path keeps the end values) and a small number $\epsilon$, and form the **varied path** $q + \epsilon\xi$. Its action $S[q + \epsilon\xi]$ is an ordinary function of the one number $\epsilon$. The **first variation** is its slope at $\epsilon = 0$:

$$
S_1 = \frac{d}{d\epsilon}S[q + \epsilon\xi]\Big|_{\epsilon = 0} .
$$

A path is **stationary** if $S_1 = 0$ for every shape $\xi$; the principle says that the true motion is stationary.

**For the oscillator the action is a polynomial in $\epsilon$.** Put the varied path into the Lagrangian:

$$
L(q + \epsilon\xi, \dot q + \epsilon\dot\xi) = \tfrac12(\dot q + \epsilon\dot\xi)^2 - \tfrac12\omega^2(q + \epsilon\xi)^2
$$

(the velocity of the varied path is $\dot q + \epsilon\dot\xi$, because the derivative of a sum is the sum of the derivatives and the constant $\epsilon$ comes out of the derivative);

$$
= \tfrac12\dot q^2 + \epsilon\,\dot q\dot\xi + \tfrac12\epsilon^2\dot\xi^2 - \tfrac12\omega^2q^2 - \epsilon\,\omega^2q\xi - \tfrac12\epsilon^2\omega^2\xi^2
$$

(the square of a sum, $(a + b)^2 = a^2 + 2ab + b^2$, applied twice);

$$
= \Big[\tfrac12\dot q^2 - \tfrac12\omega^2q^2\Big] + \epsilon\Big[\dot q\dot\xi - \omega^2q\xi\Big] + \epsilon^2\Big[\tfrac12\dot\xi^2 - \tfrac12\omega^2\xi^2\Big]
$$

(the terms collected by the power of $\epsilon$). Integrating from $0$ to $T$ term by term:

$$
S[q + \epsilon\xi] = S_0 + S_1\,\epsilon + S_2\,\epsilon^2,\qquad S_1 = \int_0^T\big(\dot q\dot\xi - \omega^2q\xi\big)dt,\qquad S_2 = \int_0^T\big(\tfrac12\dot\xi^2 - \tfrac12\omega^2\xi^2\big)dt ,
$$

with $S_0 = S[q]$. The coefficient $S_1$ of $\epsilon$ is exactly the first variation (the slope of a polynomial at 0 is its coefficient of the first power), and the coefficient $S_2$ contains only the shape $\xi$, not the path: it is the same for every path (PROVED; Notebook 07d checks both facts exactly, In [3]).

**The example of Notebook 07d.** Take $\omega = 1$, $T = 1$, $q(0) = 0$, $q(1) = 1$. The **true path** is $q(t) = \sin t/\sin 1$: it has $\ddot q = -\sin t/\sin 1 = -q$ (the second derivative of $\sin t$ is $-\sin t$), which is Newton's law $\ddot q = -\omega^2 q$ for the spring, and $q(0) = 0$, $q(1) = \sin 1/\sin 1 = 1$. Two wrong paths with the same end values are the **line** $q = t$ and the **parabola** $q = t^2$. The shapes are $\xi_n(t) = \sin(n\pi t)$ for $n = 1, 2, 3$; each vanishes at $t = 0$ and at $t = 1$, because $\sin 0 = \sin(n\pi) = 0$.

**One first variation by hand.** For the line, $\dot q = 1$, and for $\xi_1 = \sin\pi t$, $\dot\xi_1 = \pi\cos\pi t$:

$$
S_1 = \int_0^1\big(\pi\cos\pi t - t\sin\pi t\big)\,dt
$$

(the formula for $S_1$ with $\omega = 1$);

$$
= \big[\sin\pi t\big]_0^1 - \int_0^1 t\sin\pi t\,dt = 0 - \int_0^1 t\sin\pi t\,dt
$$

(an antiderivative of $\pi\cos\pi t$ is $\sin\pi t$, which is 0 at both ends). The last integral is done by **integration by parts** (Section 7.3 derives it; here it is used with $f = t$ and $g = -\cos(\pi t)/\pi$): $\int_0^1 t\sin\pi t\,dt = \big[-t\cos(\pi t)/\pi\big]_0^1 + \int_0^1\cos(\pi t)/\pi\,dt = 1/\pi + 0 = 1/\pi$, since $\cos\pi = -1$ and $\sin\pi = \sin 0 = 0$. So

$$
S_1 = -\frac{1}{\pi} = -0.318310 ,
$$

the value that Notebook 07d prints for the line and $n = 1$ (In [2]). The line is not stationary: its action changes to first order. For the true path the notebook finds $S_1 = 0$ exactly for all three shapes, and for the two wrong paths $S_1 \neq 0$ for all three (In [2] and In [3]; PROVED by exact integration with sympy).

**A minimum, or only stationary?** The coefficient $S_2$ decides what kind of stationary point the true path is. Take the shape $\xi_1 = \sin(\pi t/T)$ on an interval of length $T$. Then $\dot\xi_1 = (\pi/T)\cos(\pi t/T)$ (the chain rule), and

$$
S_2 = \int_0^T\Big(\frac{\pi^2}{2T^2}\cos^2\frac{\pi t}{T} - \frac{\omega^2}{2}\sin^2\frac{\pi t}{T}\Big)dt
$$

(the definition of $S_2$ with this shape);

$$
= \frac{\pi^2}{2T^2}\cdot\frac{T}{2} - \frac{\omega^2}{2}\cdot\frac{T}{2}
$$

(each of the two integrals is $T/2$: the double-angle formula $\cos 2x = 2\cos^2x - 1$ gives $\cos^2(\pi t/T) = \tfrac12\big(1 + \cos(2\pi t/T)\big)$; the interval from 0 to $T$ is one full period of $\cos(2\pi t/T)$, and indeed $\int_0^T\cos(2\pi t/T)\,dt = \big[\tfrac{T}{2\pi}\sin(2\pi t/T)\big]_0^T = 0$ because $\sin 2\pi = \sin 0 = 0$; so $\int_0^T\cos^2(\pi t/T)\,dt = \tfrac12T = T/2$, and because $\sin^2 = 1 - \cos^2$, $\int_0^T\sin^2(\pi t/T)\,dt = T - T/2 = T/2$);

$$
= \frac{T}{4}\Big(\frac{\pi^2}{T^2} - \omega^2\Big)
$$

(the common factor $T/4$ taken out). For $T < \pi/\omega$ the bracket is positive, so $S_2 > 0$ and the action of $q + \epsilon\xi_1$ is $S_0 + S_2\epsilon^2$ with a positive $S_2$: the true path is a **minimum** along this shape. For $T > \pi/\omega$ the coefficient is negative: the true path is still stationary ($S_1 = 0$), but along $\xi_1$ the action is a maximum, while along faster shapes ($\xi_n$ with large $n$) it is still a minimum; such a point is called a **saddle**. This is why the principle is called the principle of STATIONARY action and not of least action (PROVED; Notebook 07d checks the formula with $T$ as a symbol and its sign at $T = 1$ and $T = 4$, In [4], and draws Figure 07d.1). With $T = 1$, $\omega = 1$ the formula gives $S_2 = (\pi^2 - 1)/4 = 2.217401$ for $\xi_1$; the notebook prints this value and $S_2 = \pi^2 - 1/4 = 9.619604$ for $\xi_2$ and $9\pi^2/4 - 1/4 = 21.956610$ for $\xi_3$ (In [3]).

### 7.3 From the principle to the Euler-Lagrange equation

Computing the action of every path is not how one finds the true path. Instead the principle is turned into an equation that the true path must satisfy at every time. This takes three lines and one lemma.

**Integration by parts.** The **product rule** of differentiation says $\frac{d}{dt}(fg) = \dot f g + f\dot g$ for two functions $f(t)$, $g(t)$. Integrate both sides from 0 to $T$. The left side is the integral of a derivative, so by the fundamental theorem of calculus it is the difference of the end values, which we write $[fg]_0^T = f(T)g(T) - f(0)g(0)$:

$$
[fg]_0^T = \int_0^T\dot f g\,dt + \int_0^T f\dot g\,dt\qquad\Longrightarrow\qquad \int_0^T f\dot g\,dt = [fg]_0^T - \int_0^T\dot f g\,dt .
$$

The second form moves the derivative from $g$ to $f$ at the price of a minus sign and the **boundary term** $[fg]_0^T$.

**Line 1.** Differentiate the action of the varied path with respect to $\epsilon$:

$$
\frac{d}{d\epsilon}S[q + \epsilon\xi]\Big|_{\epsilon = 0} = \int_0^T\Big(\frac{\partial L}{\partial q}\,\xi + \frac{\partial L}{\partial\dot q}\,\dot\xi\Big)dt .
$$

Rule: the derivative may be taken inside the integral (true for the smooth functions of this book on a finite interval; a standard theorem of calculus, ASSUMED here), and inside, $L$ depends on $\epsilon$ through its first argument $q + \epsilon\xi$, whose derivative with respect to $\epsilon$ is $\xi$, and through its second argument $\dot q + \epsilon\dot\xi$, whose derivative is $\dot\xi$; the chain rule for a function of two variables (Chapter 2) adds the two contributions.

**Line 2.** Integrate the second term by parts with $f = \partial L/\partial\dot q$ and $g = \xi$:

$$
= \int_0^T\frac{\partial L}{\partial q}\,\xi\,dt + \Big[\frac{\partial L}{\partial\dot q}\,\xi\Big]_0^T - \int_0^T\frac{d}{dt}\Big(\frac{\partial L}{\partial\dot q}\Big)\xi\,dt .
$$

**Line 3.** The boundary term vanishes, because $\xi(0) = \xi(T) = 0$; collect the two integrals:

$$
= \int_0^T E(t)\,\xi(t)\,dt,\qquad E = \frac{\partial L}{\partial q} - \frac{d}{dt}\frac{\partial L}{\partial\dot q} .
$$

The function $E(t)$ is the **Euler-Lagrange expression** of the path. In $\partial L/\partial q$ and $\partial L/\partial\dot q$ the path's own position and velocity are put in after differentiating, and then $\frac{d}{dt}$ is an ordinary time derivative along the path.

**The fundamental lemma.** If a continuous function $E(t)$ has $\int_0^T E\xi\,dt = 0$ for every shape $\xi$ that vanishes at the ends, then $E(t) = 0$ at every time. *Proof.* Suppose $E(t_0) > 0$ at some time $t_0$ between 0 and $T$. Because $E$ is continuous, it stays positive on a small interval $t_0 - w < t < t_0 + w$ (if it were zero or negative arbitrarily close to $t_0$, its values there would not approach $E(t_0) > 0$). Take a **bump**: a smooth shape that is positive on that interval and zero outside, for example $\xi = \cos^2(\pi(t - t_0)/(2w))$ inside and 0 outside. Then $E\xi$ is positive inside the interval and zero outside, so $\int_0^T E\xi\,dt > 0$, which contradicts the assumption. The case $E(t_0) < 0$ is the same with every sign reversed. So $E(t_0) = 0$ for every $t_0$. $\square$

**The Euler-Lagrange equation.** Putting the three lines and the lemma together: the true path satisfies

$$
\frac{\partial L}{\partial q} - \frac{d}{dt}\frac{\partial L}{\partial\dot q} = 0
$$

at every time (PROVED, from the principle of stationary action). For the oscillator, $\partial L/\partial q = -\omega^2q$ and $\partial L/\partial\dot q = \dot q$, so $E = -\omega^2q - \ddot q$ and the equation is $\ddot q = -\omega^2q$: Newton's law for the spring. The true path of our example satisfies it; the line has $\ddot q = 0$ and so $E = -t$; the parabola has $\ddot q = 2$ and so $E = -2 - t^2$. Notebook 07d computes these three functions with a function `euler_lagrange` of its own and with sympy's `euler_equations` (In [5]) and checks that the first variation of every wrong path equals $\int_0^1 E\xi_n\,dt$ (for example, for the line and $n = 1$: $\int_0^1(-t)\sin\pi t\,dt = -1/\pi$, the value of Section 7.2).

**The boundary term, seen.** If the shape does not vanish at the end, the boundary term of Line 2 stays. For the oscillator $\partial L/\partial\dot q = \dot q$, so $S_1 = \int_0^1 E\xi\,dt + [\dot q\,\xi]_0^1$. Take the line and the shape $\xi = t$, which is 0 at $t = 0$ but 1 at $t = 1$. By the definition, $S_1 = \int_0^1(\dot q\dot\xi - q\xi)\,dt = \int_0^1(1 - t^2)\,dt = 1 - \tfrac13 = \tfrac23$. The integral part is $\int_0^1(-t)\,t\,dt = -\tfrac13$, and the boundary term is $\dot q(1)\xi(1) - \dot q(0)\xi(0) = 1\cdot 1 - 1\cdot 0 = 1$. Indeed $-\tfrac13 + 1 = \tfrac23$ (Notebook 07d prints these three numbers in In [5]; it does the same for the parabola: $\tfrac34 = -\tfrac54 + 2$).

**The lemma made visible with narrow bumps.** The ratio $\int E\xi\,dt/\int\xi\,dt$ is an **average** of $E$ over the bump. For a bump of half-width $w$ centred at $t_0$ it tends to $E(t_0)$ as $w$ shrinks. For the parabola, whose $E(t) = -2 - t^2$ is a polynomial of degree 2, the error of the average can be computed exactly. Write $t = t_0 + s$:

$$
E(t_0 + s) = E(t_0) + E'(t_0)\,s + \tfrac12E''(t_0)\,s^2
$$

(Taylor's formula, Chapter 2, which is exact for a polynomial of degree 2; here $E' = -2t_0$ and $E'' = -2$). The bump is symmetric around $t_0$, so the average of $s$ over it is 0 (the contributions of $s$ and $-s$ cancel), and

$$
\text{average of }E - E(t_0) = \tfrac12E''\cdot(\text{average of }s^2) = -(\text{average of }s^2) .
$$

With $s = wu$, where $u$ runs from $-1$ to $1$, the average of $s^2$ is $w^2$ times the number

$$
c = \frac{\int_{-1}^1u^2\cos^2(\pi u/2)\,du}{\int_{-1}^1\cos^2(\pi u/2)\,du} .
$$

Using $\cos^2(\pi u/2) = \tfrac12(1 + \cos\pi u)$ (the double-angle formula), the denominator is $\int_{-1}^1\tfrac12(1 + \cos\pi u)\,du = 1$ (the cosine integrates to $[\sin\pi u/\pi]_{-1}^1 = 0$). The numerator is

$$
\tfrac12\int_{-1}^1u^2\,du + \tfrac12\int_{-1}^1u^2\cos\pi u\,du = \tfrac13 + \tfrac12\cdot\Big(-\frac{4}{\pi^2}\Big) ,
$$

where the last integral follows from two integrations by parts: $\int_{-1}^1u^2\cos\pi u\,du = -\tfrac{2}{\pi}\int_{-1}^1u\sin\pi u\,du$ and $\int_{-1}^1u\sin\pi u\,du = \tfrac{2}{\pi}$. So

$$
\text{average of }E - E(t_0) = -\Big(\frac13 - \frac{2}{\pi^2}\Big)w^2 = -0.130691\,w^2 ,
$$

independent of $t_0$ and exactly proportional to $w^2$: halving $w$ divides the error by 4 (PROVED here). Of these steps only the replacement of $\tfrac12E''$ by $-1$ used the parabola's $E'' = -2$: for any polynomial $E$ of degree 2 the same steps give the error $\tfrac12E''\big(\tfrac13 - \tfrac{2}{\pi^2}\big)w^2$. For the parabola and $w = 0.2$ the error is $-0.130691 \times 0.04 = -5.228\times10^{-3}$, the number that Notebook 07d computes numerically for all three centres $t_0 = 0.3, 0.5, 0.7$, with the ratio 4.0000 between successive half-widths (In [7], Figure 07d.3; COMPUTED with the trapezoidal rule on 200001 points, whose own error is far below the printed digits).

**The action on a grid.** A computer stores a path as its values $q_0, q_1, \dots, q_N$ at the **grid** times $t_n = nh$, $h = T/N$, and replaces the integral by a sum. With the velocity of each step written as the difference quotient $(q_{n+1} - q_n)/h$ and the potential energy averaged over the two ends of the step,

$$
S_N = \sum_{n=0}^{N-1}h\Big[\frac12\Big(\frac{q_{n+1} - q_n}{h}\Big)^2 - \frac{\omega^2}{4}\big(q_n^2 + q_{n+1}^2\big)\Big] .
$$

An inner value $q_n$ ($0 < n < N$) appears in two terms of the sum: the step that ends at $t_n$ (number $n - 1$) and the step that starts there (number $n$). Differentiating with respect to $q_n$:

$$
\frac{\partial S_N}{\partial q_n} = h\Big[\frac{q_n - q_{n-1}}{h^2} - \frac{q_{n+1} - q_n}{h^2} - \frac{\omega^2}{2}q_n - \frac{\omega^2}{2}q_n\Big]
$$

(the chain rule on the two squares: $\frac{d}{dq_n}\tfrac12\big(\frac{q_n - q_{n-1}}{h}\big)^2 = \frac{q_n - q_{n-1}}{h}\cdot\frac1h$ and $\frac{d}{dq_n}\tfrac12\big(\frac{q_{n+1} - q_n}{h}\big)^2 = \frac{q_{n+1} - q_n}{h}\cdot\big(-\frac1h\big)$; and $\frac{d}{dq_n}\frac{\omega^2}{4}q_n^2 = \frac{\omega^2}{2}q_n$, once from each step);

$$
= h\Big[-\frac{q_{n+1} - 2q_n + q_{n-1}}{h^2} - \omega^2q_n\Big]
$$

(the terms collected). The bracket is $E = -\ddot q - \omega^2q$ with $\ddot q$ replaced by the **second difference quotient** $(q_{n+1} - 2q_n + q_{n-1})/h^2$. So "the action on the grid is stationary" means "the grid version of the Euler-Lagrange equation holds at every inner point" (PROVED; Notebook 07d checks it with sympy for $N = 5$, In [8]). The second difference quotient differs from $\ddot q$ by a term of size $h^2$: adding the Taylor series $q(t \pm h) = q \pm h\dot q + \tfrac12h^2\ddot q \pm \tfrac16h^3q^{(3)} + \tfrac1{24}h^4q^{(4)} + \dots$ (Chapter 2) the odd powers cancel and $\big(q(t + h) - 2q(t) + q(t - h)\big)/h^2 = \ddot q + \tfrac1{12}h^2q^{(4)} + \dots$. Accordingly, the path that makes the grid action stationary approaches the true path with an error proportional to $h^2$: Notebook 07d solves the grid equations for $N = 4, 8, \dots, 256$ and measures the largest errors $4.089\times10^{-4}$ ($N = 4$) down to $1.008\times10^{-7}$ ($N = 256$) and the observed orders 2.007, 1.978, 2.001, 2.000, 2.000, 2.000 (In [9], Figure 07d.4; COMPUTED).

### 7.4 Energy, total derivatives and first-order Lagrangians

**The energy.** For a Lagrangian $L(q, \dot q)$ that does not contain the time explicitly, the **energy** is

$$
H = \dot q\,\frac{\partial L}{\partial\dot q} - L .
$$

For the oscillator $H = \dot q\cdot\dot q - \big(\tfrac12\dot q^2 - \tfrac12\omega^2q^2\big) = \tfrac12\dot q^2 + \tfrac12\omega^2q^2$, kinetic plus potential energy. Its time derivative along any path, line by line:

$$
\frac{dH}{dt} = \ddot q\,\dot q + \omega^2q\,\dot q
$$

(the chain rule: the derivative of $\tfrac12\dot q^2$ is $\dot q\ddot q$, that of $\tfrac12\omega^2q^2$ is $\omega^2q\dot q$);

$$
= \dot q\,\big(\ddot q + \omega^2q\big) = -\dot q\,E
$$

(the common factor $\dot q$ taken out; then $E = -\ddot q - \omega^2q$). So the energy is constant on every solution of $E = 0$, and it changes on a path where $E \neq 0$ and $\dot q \neq 0$ (PROVED; Notebook 07d checks the identity for a general path, In [10]). On the true path, $\dot q = \cos t/\sin 1$, so $H = \tfrac12(\cos^2 t + \sin^2 t)/\sin^2 1 = 1/(2\sin^2 1) = 0.706141$, constant; on the line $H = \tfrac12 + \tfrac12t^2$ with $dH/dt = t$; on the parabola $H = 2t^2 + \tfrac12t^4$ with $dH/dt = 4t + 2t^3 = 2t(t^2 + 2)$ (all printed by In [10]; Figure 07d.5).

**A total derivative changes no equation.** Let $F(q, t)$ be any smooth function and add its **total derivative** along the path to the Lagrangian:

$$
L' = L + \frac{d}{dt}F\big(q(t), t\big) = L + \frac{\partial F}{\partial q}\,\dot q + \frac{\partial F}{\partial t}
$$

(the chain rule for a function of two variables, both of which change with $t$). Two proofs that $L'$ has the same Euler-Lagrange equation as $L$:

- *By the action.* The action changes by $\int_0^T\frac{dF}{dt}dt = F(q(T), T) - F(q(0), 0)$ (the fundamental theorem of calculus), which is the same number for every path with the given end values. A change that is the same for every path cannot change which path is stationary.
- *By the expression.* For $G = \frac{dF}{dt} = F_q\dot q + F_t$ (subscripts denote partial derivatives): $\partial G/\partial q = F_{qq}\dot q + F_{qt}$ and $\partial G/\partial\dot q = F_q$, whose time derivative along the path is $F_{qq}\dot q + F_{qt}$. The difference is 0, because the order of two partial derivatives does not matter ($F_{tq} = F_{qt}$, Chapter 2). So $G$ contributes nothing to $E$.

In particular a Lagrangian that is ONLY a total derivative, such as $\frac{d}{dt}(q^2) = 2q\dot q$, has the Euler-Lagrange expression $2\dot q - \frac{d}{dt}(2q) = 0$ for every path: it gives no equation at all (PROVED; Notebook 07d checks both statements with $F = tq^3$ and finds that the action changes by exactly 1 for each of the three paths, In [11]). This innocent fact decides, in Section 7.28, why the author's real Majorana-type Lagrangian describes nothing for anticommuting fields.

**First-order Lagrangians.** The Lagrangians of the two fields of this book contain the derivatives only to the first power. Two small examples show what such Lagrangians do.

*Example A: two real variables.* $L_A = \tfrac12(q_0\dot q_1 - q_1\dot q_0) - \tfrac12\omega(q_0^2 + q_1^2)$. With two variables there are two Euler-Lagrange expressions, one for each. For $q_0$: $\partial L_A/\partial q_0 = \tfrac12\dot q_1 - \omega q_0$ and $\partial L_A/\partial\dot q_0 = -\tfrac12q_1$, whose time derivative is $-\tfrac12\dot q_1$; so

$$
E_0 = \tfrac12\dot q_1 - \omega q_0 - \big(-\tfrac12\dot q_1\big) = \dot q_1 - \omega q_0 .
$$

For $q_1$: $\partial L_A/\partial q_1 = -\tfrac12\dot q_0 - \omega q_1$ and $\partial L_A/\partial\dot q_1 = \tfrac12q_0$, so $E_1 = -\tfrac12\dot q_0 - \omega q_1 - \tfrac12\dot q_0 = -\dot q_0 - \omega q_1$. The equations $\dot q_1 = \omega q_0$, $\dot q_0 = -\omega q_1$ are of FIRST order: the starting values alone fix the motion (no starting velocity is needed). For $q_0(0) = 1$, $q_1(0) = 0$ the solution is $q_0 = \cos\omega t$, $q_1 = \sin\omega t$: indeed $\dot q_1 = \omega\cos\omega t = \omega q_0$ and $\dot q_0 = -\omega\sin\omega t = -\omega q_1$. The point $(q_0, q_1)$ turns on a circle, counterclockwise.

*Example B: one complex variable.* Let $\psi = (q_0 + iq_1)/\sqrt2$, with the **complex conjugate** $\psi^* = (q_0 - iq_1)/\sqrt2$, and

$$
L_B = \frac{i}{2}\big(\psi^*\dot\psi - \dot\psi^*\psi\big) - \omega\,\psi^*\psi .
$$

In real variables: $\psi^*\psi = \tfrac12(q_0 - iq_1)(q_0 + iq_1) = \tfrac12(q_0^2 + q_1^2)$, and $\psi^*\dot\psi - \dot\psi^*\psi = \tfrac12\big[(q_0 - iq_1)(\dot q_0 + i\dot q_1) - (\dot q_0 - i\dot q_1)(q_0 + iq_1)\big] = \tfrac12\big[2iq_0\dot q_1 - 2iq_1\dot q_0\big] = i(q_0\dot q_1 - q_1\dot q_0)$ (multiply out; the terms $q_0\dot q_0$ and $q_1\dot q_1$ cancel). So

$$
L_B = \tfrac{i}{2}\cdot i(q_0\dot q_1 - q_1\dot q_0) - \tfrac12\omega(q_0^2 + q_1^2) = \tfrac12(q_1\dot q_0 - q_0\dot q_1) - \tfrac12\omega(q_0^2 + q_1^2) :
$$

Example A with the sign of the kinetic term reversed (because $i\cdot i = -1$). It is a real Lagrangian, although it is written with complex numbers.

**Varying $\psi$ and $\psi^*$ as if they were independent.** The pair $(q_0, q_1)$ and the pair $(\psi, \psi^*)$ determine each other ($q_0 = (\psi + \psi^*)/\sqrt2$, $q_1 = (\psi - \psi^*)/(i\sqrt2)$): the change of variables is linear and invertible. So one may use $\psi$ and $\psi^*$ as the two variables of the Lagrangian, and the Euler-Lagrange expressions combine in the same way. By the chain rule, $\partial/\partial\psi^* = \frac{\partial q_0}{\partial\psi^*}\partial/\partial q_0 + \frac{\partial q_1}{\partial\psi^*}\partial/\partial q_1 = \frac{1}{\sqrt2}\big(\partial/\partial q_0 + i\,\partial/\partial q_1\big)$, and therefore

$$
E_{\psi^*} = \frac{E_{q_0} + iE_{q_1}}{\sqrt2} .
$$

Varying $\psi^*$ directly: $\partial L_B/\partial\psi^* = \frac{i}{2}\dot\psi - \omega\psi$ and $\partial L_B/\partial\dot\psi^* = -\frac{i}{2}\psi$, whose time derivative is $-\frac{i}{2}\dot\psi$; so

$$
E_{\psi^*} = \tfrac{i}{2}\dot\psi - \omega\psi + \tfrac{i}{2}\dot\psi = i\dot\psi - \omega\psi .
$$

The field equation $i\dot\psi = \omega\psi$ has the solution $\psi(t) = e^{-i\omega t}\psi(0)$ (the derivative of $e^{-i\omega t}$ is $-i\omega e^{-i\omega t}$, and $i\cdot(-i\omega) = \omega$): the point turns clockwise, with $|\psi|^2 = \tfrac12(q_0^2 + q_1^2)$ constant (PROVED; Notebook 07d checks every statement of the two examples with $\omega$ as a symbol, In [12], and draws them in Figure 07d.6). The Lagrangians of the two fields of this book have exactly this structure: $\psi$ becomes the column $\Psi$ of 16 components, $\psi^*$ becomes the row $\bar\Psi = \Psi^\dagger C$ (Section 7.19), and $\omega$ becomes a matrix of derivatives.

### 7.5 Fields: one derivative term per coordinate, and what an extra time does

**A field** is a function of several coordinates, for example $\phi(x_1, x_4)$ of a 3-space coordinate $x_1$ and the time $x_4$. Its Lagrangian is a function $\mathcal{L}(\phi, \partial_1\phi, \partial_4\phi)$ of the value and of the partial derivatives $\partial_\mu\phi = \partial\phi/\partial x_\mu$, called a **Lagrangian density**, and the action is its integral over all coordinates of a region. The shapes $\xi(x_1, x_4)$ now vanish on the boundary of the region. Line 1 of Section 7.3 now has one term $\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\partial_\mu\xi$ for each coordinate; in Line 2 each of them is integrated by parts along its own coordinate (the other coordinates held fixed), and each boundary term vanishes because $\xi$ vanishes on the boundary; the fundamental lemma works with bumps in several variables in the same way. The result is the Euler-Lagrange expression of a field,

$$
E = \frac{\partial\mathcal{L}}{\partial\phi} - \sum_\mu\frac{\partial}{\partial x_\mu}\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)} ,
$$

with one derivative term for each coordinate, and the field equation $E = 0$ at every point (PROVED, by the same three lines and the lemma).

**A field of one space direction and time.** In the flat version of the author's signature, $\eta_{11} = +1$ and $\eta_{44} = -1$, the Lagrangian density of a field of mass $m$ is

$$
\mathcal{L} = -\tfrac12\big(\eta^{11}(\partial_1\phi)^2 + \eta^{44}(\partial_4\phi)^2\big) - \tfrac12m^2\phi^2 = \tfrac12(\partial_4\phi)^2 - \tfrac12(\partial_1\phi)^2 - \tfrac12m^2\phi^2
$$

(the numbers $\eta^{aa}$ are equal to $\eta_{aa}$, $\pm1$): kinetic energy $\tfrac12(\partial_4\phi)^2$ minus a gradient energy along $x_1$ and a potential energy. The Euler-Lagrange expression, line by line:

$$
E = \frac{\partial\mathcal{L}}{\partial\phi} - \partial_1\frac{\partial\mathcal{L}}{\partial(\partial_1\phi)} - \partial_4\frac{\partial\mathcal{L}}{\partial(\partial_4\phi)}
$$

(the formula with its two coordinates);

$$
= -m^2\phi - \partial_1(-\partial_1\phi) - \partial_4(\partial_4\phi)
$$

(the three partial derivatives of $\mathcal{L}$, each with the other two arguments held fixed);

$$
= \partial_1^2\phi - \partial_4^2\phi - m^2\phi
$$

(two minus signs give a plus). So $\partial_4^2\phi = \partial_1^2\phi - m^2\phi$: the wave equation with a mass, called the **Klein-Gordon equation**. A **plane wave** $\phi = \cos(kx_1)\cos(\omega x_4)$, with **wave number** $k$ and angular frequency $\omega$, has $\partial_1^2\phi = -k^2\phi$ and $\partial_4^2\phi = -\omega^2\phi$, so $E = (-k^2 + \omega^2 - m^2)\phi$, which vanishes exactly when

$$
\omega^2 = m^2 + k^2 ,
$$

the **dispersion relation**: the wave oscillates in time for every $k$ (PROVED; Notebook 07d, In [14]).

**A field of one extra time and time.** Replace $x_1$ by the extra time $x_5$. The author's signature makes $x_5$ time-like, $\eta_{55} = -1$, and the same recipe gives

$$
\mathcal{L} = \tfrac12(\partial_4\phi)^2 + \tfrac12(\partial_5\phi)^2 - \tfrac12m^2\phi^2,\qquad E = -\partial_5^2\phi - \partial_4^2\phi - m^2\phi .
$$

The only change is the sign of the $x_5$ term. Try $\phi = \cos(kx_5)\,P(x_4)$. Then $\partial_5^2\phi = -k^2\phi$ and $E = \cos(kx_5)\big(k^2P - P'' - m^2P\big)$, so the field equation becomes

$$
P'' = (k^2 - m^2)\,P .
$$

For $k < m$ the solutions oscillate. For $k > m$ they are $\cosh(\kappa x_4)$ and $\sinh(\kappa x_4)$ with

$$
\kappa = \sqrt{k^2 - m^2}
$$

(the second derivative of $\cosh(\kappa x_4)$ is $\kappa^2\cosh(\kappa x_4)$): they GROW exponentially, and the **growth rate** $\kappa$ becomes as large as we like when $k$ grows. A wave along a space direction raises $\omega^2$ above $m^2$; a wave along an extra time lowers it to $m^2 - k^2$, below zero when $k > m$ (PROVED; Notebook 07d, In [15], Figures 07d.7 and 07d.8).

**The same growth for the 16-component fields.** The fields of this book obey a first-order equation $\gamma^{(a)}\partial_a\Psi = m\Psi$ in flat space (Section 7.21). Multiplying it by the same operator once more turns it into a second-order equation for every component, because of the Clifford relation of the author's gamma matrices (Chapter 4), $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}$. For constant numbers $k_a$ it gives, line by line,

$$
\Big(\sum_a k_a\gamma^{(a)}\Big)^2 = \sum_{a,b}k_ak_b\,\gamma^{(a)}\gamma^{(b)} = \tfrac12\sum_{a,b}k_ak_b\big(\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)}\big) = \sum_a\eta^{aa}k_a^2\,I_{16}
$$

(multiply out the square of a sum; then use that the double sum does not change when the names $a$ and $b$ are exchanged, so it equals half the sum of itself and its exchanged form; then the Clifford relation, which leaves only $a = b$). Written out: $(k_1^2 + k_2^2 + k_3^2 - k_4^2 - k_5^2 - k_6^2 - k_7^2 + k_8^2)\,I_{16}$, where $I_{16}$ is the $16\times16$ identity matrix (PROVED; Notebook 07d checks it exactly with the author's gammas, In [15]; it reproduces `Revision/theory/reports/python-field-theory.json`, check `clifford_relations`). The Revision record finds for a plane wave of the 16-component field with an extra-time momentum $k_5 = K$ the growth rate $\sqrt{K^2 - k_1^2 - k_2^2 - k_3^2 - k_8^2 - m^2}$, which has no upper bound as $K$ grows (`Revision/theory/reports/python-scope.json`, check `extra_time_growth_rates_unbounded`); for a momentum along $x_5$ alone it is $\sqrt{K^2 - m^2}$, the $\kappa$ above (Notebook 07d reads the formula from the record and checks this, In [15]). What this unbounded growth means for the field equations of the book (no well-posed initial-value problem for data that depend on the extra times) is the subject of Chapter 8.

### 7.6 Example: Notebook 07d derives the Euler-Lagrange equation

Notebook 07d puts Sections 7.2 to 7.5 to work. It computes exactly, with sympy, the action of the true path and of the two wrong paths and of their variations, and shows that only the true path has a zero first variation; it checks the formula for $S_2$ and the change from minimum to saddle at $T = \pi/\omega$; it computes the Euler-Lagrange expression with a function of its own and with sympy's, checks the integration by parts with and without the boundary term, the fundamental lemma with narrow bumps, the action on a grid and its second-order convergence, the energy, the total derivative, the two first-order examples, and the field equations along a space direction and along an extra time, where it reproduces the growth rate of the Revision record. It draws eight figures and ends with the line ALL 30 CHECKS PASSED (notebook 07d).

<!-- NOTEBOOK 07d -->

### 7.9 Line-by-line walk-through of Notebook 07d

The notebook has 17 code cells, In [1] to In [17]. This section explains every line of every one of them, in order. A line that starts with `#` is a **comment**: Python skips it; it is there for the reader. A text in triple quotes directly below a `def` line is a **docstring**, a description that Python stores but does not run. In the quoted code a line `...)` stands for the remaining lines of a long figure caption; every caption is printed in full under its figure in Section 7.8, and the paragraph "What Figure 07d.k shows" after the code says what to look for.

**In [1], the set-up cell.** Its first 237 lines are the complete run instructions of Section 7.7 again, as comment lines, so that the notebook file carries its own instructions. The code starts below the line THE SET-UP between two lines of `=` signs. This part is the same in every notebook of the book except for one line (the notebook's name); we explain it here once, and the walk-throughs of Notebooks 07a, 07b and 07c refer back to this explanation.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

`import` loads a **module** (a part of Python or of an installed package) so that the code can use it. `json` reads and writes the text format JSON, in which the Revision record stores its results; `os` gives access to the computer's environment; `textwrap` breaks long text into lines; `from pathlib import Path` takes the single name `Path` out of the module `pathlib`. A `Path` is the address of a file or a folder, written the same way on every operating system. The next three lines load the plotting package matplotlib, its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python), which show a picture file below a cell.

```python
NOTEBOOK_ID = "07d"  # this notebook: chapter 07, example d
```

A **variable** is a name for a value. This line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"07d"`. It is the only line of the set-up code that differs between notebooks.

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

`def` defines a **function**: a named piece of code that runs when it is called. `Path.cwd()` is the folder in which the notebook runs and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it; `[here, *here.parents]` is the list that starts with `here` and continues with all of them. The `for` loop takes these folders one after the other; the operator `/` joins a folder and a name into a longer path; `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If none does, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

`REPO` is the repository folder. `os.environ` holds the **environment variables** of the running program (named texts that the computer hands to it); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and otherwise the default, the repository folder written as a string. When you run the notebook the variable is not set, so the notebook writes into the repository; the book's checking tool sets it to a scratch folder, so that a check run does not change the repository.

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

`say` prints a text in lines of at most 89 characters; `textwrap.fill` breaks it at blanks, and every line after the first starts with four blanks. `str(text)` turns any value into a string first.

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

A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/07d.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty dictionary and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored and `newline="\n"` stores the same line end on every system.

```python
def save_figure(fig, name, caption):
    """Save the figure fig as Revision/textbook/figures/<id>_<k>_<name>.png, record its
    caption in CAPTION_FILE, show the saved picture below the cell and close the figure.
    k counts the figures of the notebook 1, 2, 3, ...; a cell run again keeps its k."""
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
```

`save_figure` is called after a figure has been drawn. `setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far; so the figures are numbered 1, 2, 3, ..., and a cell that is run twice keeps its numbers. The file name joins the notebook id, the number and the name, for example `07d_1_action_versus_epsilon.png`.

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

`fig.savefig` writes the PNG file with 150 dots per inch, without an empty margin and without the program's name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory. The caption is stored, and the whole dictionary of captions is written into the captions file (`json.dumps` turns it into JSON text with sorted keys and one blank of indentation). `display(Image(...))` shows the saved picture below the cell; its `metadata` tells the book's tools which file it is. The last line prints where the figure was saved.

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

`PASSED` is an empty **list** (an ordered collection, written with square brackets) that collects the names of the checks that pass. `check(condition, name, record=None)` is the notebook's test: `record=None` makes the third argument optional. If `condition` is false, `raise AssertionError(...)` stops the notebook with a message that names the failed check. An `if` statement is used instead of Python's `assert`, because `python -O` would skip an `assert`. Otherwise the name is appended to `PASSED` and a line `PASS <name>` is printed; when the check reproduces a Revision record, a second line `reproduces <record>` follows.

```python
def report(label, value, unit=""):
    """Print a key number as a line "RESULT <label> = <value> <unit>"."""
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    """Print the last line of the notebook: how many checks passed."""
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")
```

`report` prints a key number as a line `RESULT <label> = <value> <unit>`; the expression `(f" {unit}" if unit else "")` adds the unit only when one is given. `all_checks_passed` prints the last line of the notebook with the number of passed checks, `len(PASSED)`.

```python
say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

The cell ends by printing one line. Two strings written next to each other inside the parentheses are joined into one by Python. **Out [1]:** `Set-up of notebook 07d complete: repository folder found, helpers defined.`

**In [2]: helpers, and the first variation of nine varied paths.**

```python
import contextlib  # redirect printed text into a buffer
import io  # an in-memory text file (the buffer)
import re  # regular expressions: read a formula from a check's detail text

import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
```

Three modules of Python: `contextlib` can send printed text somewhere else, `io` provides an in-memory text file, `re` reads patterns in text (**regular expressions**). Then the two packages of the computation: numpy (arrays of numbers, under the short name `np`) and sympy (exact algebra with symbols, `sp`).

```python
check_of_the_setup = check  # the helper check of the set-up cell


def check(condition, name, record=None):
    """The set-up cell's check, with its PASS line and its "reproduces" line
    printed by ONE print call, so that Jupyter delivers them together."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # collect what check prints
        check_of_the_setup(condition, name, record)
    print(buffer.getvalue(), end="")  # and print it in one piece
```

The first line keeps the set-up cell's `check` under a second name. The new `check` of the same name calls the old one while `contextlib.redirect_stdout(buffer)` sends everything it prints into the in-memory file `buffer`; then it prints the collected text with one single `print` (`end=""` adds no extra line end, because the collected text already ends with one). The reason: Jupyter delivers printed text in pieces, and the book's tools must see a PASS line and the "reproduces" line that may follow it as one piece.

```python
def revision_check(report, name):
    """The check called name of a Revision report (a JSON file): its dictionary
    (name, verdict, detail); stops if it is missing or its verdict is not PASS."""
    data = json.loads(repository_file(report).read_text(encoding="utf-8"))
    found = [item for item in data["checks"] if item["name"] == name]
    if len(found) != 1 or found[0]["verdict"].upper() != "PASS":
        raise ValueError(f"{name} is not a passing check of {report}")
    return found[0]


def reproduces(report, name):
    """The text "<report>, check <name>" after making sure the check passes."""
    revision_check(report, name)
    return f"{report}, check {name}"
```

`revision_check(report, name)` reads a Revision report (a JSON file) with `json.loads` and returns the entry of the check called `name` (a dictionary with the keys name, verdict and detail). The square brackets `[item for item in data["checks"] if ...]` form a **list comprehension**: the list of all entries whose name is `name`. If there is not exactly one, or its verdict, written in capitals with `.upper()`, is not PASS, the notebook stops with a `ValueError`. `reproduces(report, name)` makes sure that the check passes and returns the text that a PASS line prints after the word reproduces.

```python
t, eps = sp.symbols("t epsilon", real=True)  # the time and the size of the change
omega, T_end = sp.Integer(1), sp.Integer(1)  # omega = 1 and the end time T = 1


def lagrangian(q, q_dot):
    """The oscillator: kinetic energy minus potential energy."""
    return q_dot**2 / 2 - omega**2 * q**2 / 2
```

`sp.symbols("t epsilon", real=True)` makes two sympy symbols, the time $t$ and the size $\epsilon$ of the change, both real numbers. `sp.Integer(1)` is the exact number 1; here it is $\omega = 1$ and the end time $T = 1$ (called `T_end`, because the name `T` is used later for a symbol). The function `lagrangian(q, q_dot)` returns $\tfrac12\dot q^2 - \tfrac12\omega^2q^2$; in Python `**` is the power and `/` the division.

```python
PATHS = {"true path": sp.sin(t) / sp.sin(1), "line": t, "parabola": t**2}
SHAPES = {n: sp.sin(n * sp.pi * t) for n in (1, 2, 3)}  # xi_n, zero at t = 0, 1
```

`PATHS` is a dictionary from the names of the three paths to their formulas: the true path $\sin t/\sin 1$, the line $t$ and the parabola $t^2$. `SHAPES` is a **dictionary comprehension**: for $n = 1, 2, 3$ it stores the shape $\xi_n = \sin(n\pi t)$ under the key $n$; `sp.pi` is the exact number $\pi$.

```python
def action_polynomial(path, shape):
    """S[path + eps shape] as a polynomial in eps (exact)."""
    varied = path + eps * shape
    integrand = sp.expand(lagrangian(varied, sp.diff(varied, t)))
    return sp.Poly(sp.integrate(integrand, (t, 0, T_end)), eps)
```

`action_polynomial(path, shape)` forms the varied path $q + \epsilon\xi$, differentiates it with `sp.diff(varied, t)`, puts both into the Lagrangian, multiplies out with `sp.expand`, integrates exactly from 0 to $T$ with `sp.integrate(integrand, (t, 0, T_end))` and returns the result as a polynomial in $\epsilon$ (`sp.Poly(..., eps)`), the $S_0 + S_1\epsilon + S_2\epsilon^2$ of Section 7.2.

```python
S1 = {}  # the first variations, S1[(path name, n)]
S2 = {}  # the coefficients of eps^2
for name, path in PATHS.items():
    for n, shape in SHAPES.items():
        polynomial = action_polynomial(path, shape)
        S1[(name, n)] = sp.simplify(polynomial.coeff_monomial(eps))
        S2[(name, n)] = sp.simplify(polynomial.coeff_monomial(eps**2))
        say(f"{name:9s} n = {n}: S1 = {S1[(name, n)]} = "
            f"{float(S1[(name, n)]):+.6f}")
```

Two empty dictionaries collect the coefficients. The two nested loops go over the three paths and the three shapes (`PATHS.items()` gives the pairs name, formula). For each of the nine combinations the polynomial is computed; `coeff_monomial(eps)` takes the coefficient of $\epsilon$ and `coeff_monomial(eps**2)` that of $\epsilon^2$, and `sp.simplify` brings each to its simplest form. The key `(name, n)` is a **tuple**, a fixed pair of values. The `say` line prints the name in a field of 9 characters (`{name:9s}`), the exact coefficient, and its decimal value with sign and six decimals (`{...:+.6f}`; `float` turns the exact number into a decimal one). **Out [2]:** nine lines. For the true path $S_1 = 0$ for all three shapes; for the line $-1/\pi$, $1/(2\pi)$ and $-1/(3\pi)$; for the parabola $-5/\pi + 4/\pi^3 = -1.462543$, $1/(2\pi)$ and $(4 - 45\pi^2)/(27\pi^3)$. The value $-1/\pi = -0.318310$ is the one computed by hand in Section 7.2.

**In [3]: the checks of the table.**

```python
check(all(S1[("true path", n)] == 0 for n in SHAPES),
      "the true path: the first variation is exactly 0 for xi_1, xi_2, xi_3")
check(all(S1[(name, n)] != 0 for name in ("line", "parabola") for n in SHAPES),
      "the line and the parabola: the first variation is not 0")
check(all(S2[(name, n)] == S2[("true path", n)] for name in PATHS for n in SHAPES),
      "the coefficient of eps^2 is the same for every path")
for n in SHAPES:
    coefficient = S2[("true path", n)]  # the same for every path
    report(f"S2 for xi_{n}", f"{coefficient} = {float(coefficient):.6f}")
```

The first check uses `all(...)` over the three shapes: it is true when $S_1 = 0$ exactly for every shape of the true path. The second checks $S_1 \neq 0$ for all six combinations of a wrong path and a shape (a **generator expression** with two `for` parts goes over all of them). The third checks that $S_2$ is the same for every path, as Section 7.2 proved. The loop prints $S_2$ for each shape, exactly and to six decimals. **Out [3]:** three PASS lines and `RESULT S2 for xi_1 = -1/4 + pi**2/4 = 2.217401`, and the same for $\xi_2$ (9.619604) and $\xi_3$ (21.956610).

**In [4]: minimum or saddle, and Figure 07d.1.**

```python
T = sp.Symbol("T", positive=True)
xi_T = sp.sin(sp.pi * t / T)  # the shape xi_1 on the interval from 0 to T
S2_general = sp.integrate(sp.diff(xi_T, t) ** 2 / 2 - omega**2 * xi_T**2 / 2,
                          (t, 0, T))
say(f"S2(T) = {sp.simplify(S2_general)}")
check(sp.simplify(S2_general - T / 4 * (sp.pi**2 / T**2 - omega**2)) == 0,
      "S2 = (T/4)(pi^2/T^2 - omega^2) for the shape xi_1 on (0, T)")
check(S2_general.subs(T, 1) > 0 and S2_general.subs(T, 4) < 0,
      "S2 > 0 for T = 1 (a minimum), S2 < 0 for T = 4 > pi (a saddle)")
```

`sp.Symbol("T", positive=True)` is the length of the interval as a positive symbol. `xi_T` is the shape $\sin(\pi t/T)$, and `S2_general` the exact integral $\int_0^T(\tfrac12\dot\xi^2 - \tfrac12\omega^2\xi^2)\,dt$. The `say` line prints it (sympy writes it as `(-T**2 + pi**2)/(4*T)`, which is $\frac{T}{4}(\frac{\pi^2}{T^2} - 1)$ with $\omega = 1$). The first check compares it with the formula of Section 7.2: the difference simplifies to 0. The second evaluates it with `.subs(T, 1)` and `.subs(T, 4)` and checks the signs: positive at $T = 1$ (minimum), negative at $T = 4 > \pi$ (saddle).

```python
epsilons = np.linspace(-0.6, 0.6, 121)
fig, (left, right) = plt.subplots(1, 2, figsize=(9.8, 3.9))
for name, style in (("true path", "-"), ("line", "--"), ("parabola", ":")):
    polynomial = action_polynomial(PATHS[name], SHAPES[1])
    values = sp.lambdify(eps, polynomial.as_expr() - polynomial.coeff_monomial(1))
    left.plot(epsilons, values(epsilons), style, label=name)
    slope = float(S1[(name, 1)])
    left.plot(epsilons, slope * epsilons, style, color="grey", linewidth=0.8)
left.axvline(0.0, color="black", linewidth=0.8)
left.set_xlabel("size of the change $\\epsilon$")
left.set_ylabel("$S[q + \\epsilon\\xi_1] - S[q]$")
left.set_title("Only the true path has slope 0")
left.legend(fontsize=8)
```

`np.linspace(-0.6, 0.6, 121)` is 121 equally spaced values of $\epsilon$. `plt.subplots(1, 2, figsize=(9.8, 3.9))` makes a figure with one row of two panels, `left` and `right`. For each path with its line style (solid `"-"`, dashed, written as two minus signs, and dotted `":"`), the polynomial with the shape $\xi_1$ is computed again; `polynomial.as_expr() - polynomial.coeff_monomial(1)` is $S - S_0 = S_1\epsilon + S_2\epsilon^2$; `sp.lambdify(eps, ...)` turns this formula into a numerical function, which `values(epsilons)` evaluates at all 121 values at once. The curve is drawn with its label, and its tangent at $\epsilon = 0$, the straight line $S_1\epsilon$, is drawn thin and grey. `axvline(0.0)` draws a vertical line at $\epsilon = 0$. The axis labels use LaTeX inside `$...$`; in a Python string a backslash is written twice. `legend` draws the key of the line styles.

```python
lengths = np.linspace(0.3, 6.0, 300)
S2_values = sp.lambdify(T, S2_general)(lengths)
right.plot(lengths, S2_values)
right.axhline(0.0, color="black", linewidth=0.8)
right.axvline(np.pi, color="red", linestyle="--", label="$T = \\pi/\\omega$")
right.set_ylim(-2.0, 4.0)
right.set_xlabel("length of the time interval $T$")
right.set_ylabel("coefficient $S_2$ of $\\epsilon^2$")
right.set_title("Minimum for $T < \\pi$, saddle for $T > \\pi$")
right.legend(fontsize=8)
fig.tight_layout()
```

The right panel: 300 interval lengths from 0.3 to 6.0, the coefficient $S_2(T)$ evaluated on them, a black line at 0 and a red dashed vertical line at $T = \pi$ (`np.pi`), the place where $S_2$ changes sign. `set_ylim(-2.0, 4.0)` fixes the vertical range. `fig.tight_layout()` arranges the panels so that nothing overlaps.

```python
save_figure(fig, "action_versus_epsilon",
            "Left: the change of the action of the oscillator ($\\omega = 1$, from "
            ...)
```

`save_figure` saves and shows the figure with its caption. **Out [4]:** `S2(T) = (-T**2 + pi**2)/(4*T)`, two PASS lines, the figure and the line `Figure 07d.1 saved as Revision/textbook/figures/07d_1_action_versus_epsilon.png`.

**What Figure 07d.1 shows.** In the left panel the solid curve of the true path touches its horizontal tangent at $\epsilon = 0$: changing the true path a little changes its action only to second order. The dashed and dotted curves of the line and the parabola cross $\epsilon = 0$ with a slope (their grey tangents are tilted): their action changes to first order, so they are not stationary. All three curves are parabolas of the same shape, shifted, because $S_2$ is the same for every path. In the right panel $S_2$ is positive for short intervals and changes sign at $T = \pi$ (red line): beyond it the true path is a saddle, not a minimum.

**In [5]: the Euler-Lagrange expression and the integration by parts.**

```python
from sympy.calculus.euler import euler_equations  # sympy's own Euler-Lagrange
```

This line imports sympy's own function `euler_equations`, used below as an independent comparison.

```python
def euler_lagrange(L, functions, variable):
    """The Euler-Lagrange expressions dL/dq - d/dt dL/d(q') of the Lagrangian L
    for each function q of the list functions of the variable."""
    values = [sp.Symbol(f"Q{i}") for i in range(len(functions))]  # stand for q
    speeds = [sp.Symbol(f"V{i}") for i in range(len(functions))]  # stand for q'
    plain = L
    for function, speed in zip(functions, speeds):
        plain = plain.subs(sp.diff(function, variable), speed)  # q' -> V first
    for function, value in zip(functions, values):
        plain = plain.subs(function, value)  # then q -> Q
    back = {**{s: sp.diff(f, variable) for f, s in zip(functions, speeds)},
            **{v: f for f, v in zip(functions, values)}}  # Q -> q, V -> q'
    return [sp.expand(sp.diff(plain, value).subs(back)
                      - sp.diff(sp.diff(plain, speed).subs(back), variable))
            for value, speed in zip(values, speeds)]
```

`euler_lagrange(L, functions, variable)` computes $\partial L/\partial q - \frac{d}{dt}\partial L/\partial\dot q$ for each function $q$ in the list `functions`, exactly as Section 7.3 says. A partial derivative with respect to $q$ must hold $\dot q$ fixed, but in sympy $q(t)$ and its derivative are tied together. So the function first replaces them by plain symbols: `values` are symbols `Q0`, `Q1`, ... standing for the functions and `speeds` are `V0`, `V1`, ... standing for their derivatives (`range(len(functions))` counts the functions; `zip` walks through two lists side by side). The first loop replaces each derivative $\dot q$ by its speed symbol (this must come first, because $\dot q$ contains $q$); the second replaces each $q$ by its value symbol. The dictionary `back` undoes both replacements (the notation `{**a, **b}` merges two dictionaries). The returned list holds, for each function, the derivative of the plain Lagrangian with respect to its value symbol, put back into functions, minus the time derivative of the derivative with respect to its speed symbol, also put back; `sp.expand` multiplies out.

```python
q = sp.Function("q")(t)  # a general path
E_general = euler_lagrange(lagrangian(q, sp.diff(q, t)), [q], t)[0]
say(f"E for the oscillator: {E_general}")
sympy_E = euler_equations(lagrangian(q, sp.diff(q, t)), [q], t)[0]
check(sp.simplify(E_general - (sympy_E.lhs - sympy_E.rhs)) == 0
      and sp.simplify(E_general + sp.diff(q, t, 2) + omega**2 * q) == 0,
      "euler_lagrange gives E = -q'' - omega^2 q, as sympy's euler_equations")
```

`sp.Function("q")(t)` is an unknown function $q(t)$, a general path. `E_general` is its Euler-Lagrange expression for the oscillator. `euler_equations` returns sympy's own equation in the form left side = right side (`lhs`, `rhs`); the check requires that the two results agree and that `E_general` equals $-\ddot q - \omega^2q$ (`sp.diff(q, t, 2)` is the second derivative).

```python
def E_of(path):
    """E(t) of a given path (insert the path into E_general)."""
    return sp.simplify(E_general.subs(q, path).doit())


for name, path in PATHS.items():
    say(f"{name:9s}: E(t) = {E_of(path)}")
check(E_of(PATHS["true path"]) == 0, "the true path solves E = 0")
```

`E_of(path)` puts a given path into `E_general` (`.subs(q, path)` replaces the unknown function, `.doit()` carries out the derivatives) and simplifies. The loop prints $E(t)$ for the three paths, and the check confirms that the true path gives exactly 0.

```python
by_parts = all(sp.simplify(S1[(name, n)]
                           - sp.integrate(E_of(PATHS[name]) * SHAPES[n], (t, 0, 1)))
               == 0 for name in ("line", "parabola") for n in SHAPES)
check(by_parts, "S1 = integral of E xi_n from 0 to 1 for both wrong paths and n = 1, "
      "2, 3")
```

`by_parts` is true when, for both wrong paths and all three shapes, the first variation $S_1$ of In [2] equals the exact integral $\int_0^1E\,\xi_n\,dt$: Line 3 of Section 7.3 for shapes that vanish at both ends.

```python
boundary_ok = True
xi_open = t  # a shape with xi(0) = 0 but xi(1) = 1
for name in ("line", "parabola"):
    path = PATHS[name]
    first = action_polynomial(path, xi_open).coeff_monomial(eps)  # its S1
    inside = sp.integrate(E_of(path) * xi_open, (t, 0, 1))
    p_xi = sp.diff(path, t) * xi_open  # (dL/dq') xi = q' xi for the oscillator
    boundary = p_xi.subs(t, 1) - p_xi.subs(t, 0)  # [q' xi] from 0 to 1
    say(f"{name}, xi = t: S1 = {sp.simplify(first)}, integral = "
        f"{sp.simplify(inside)}, boundary term = {boundary}")
    boundary_ok = boundary_ok and sp.simplify(first - inside - boundary) == 0
check(boundary_ok, "for xi = t (not zero at t = 1): S1 = integral of E xi + "
      "boundary term q'(1) xi(1)")
```

Now the shape $\xi = t$, which is 1 at $t = 1$. For each wrong path: `first` is its $S_1$ (the coefficient of $\epsilon$), `inside` is $\int_0^1E\xi\,dt$, `p_xi` is $\dot q\,\xi$ (because $\partial L/\partial\dot q = \dot q$ for the oscillator), and `boundary` is $[\dot q\,\xi]_0^1$, the value at 1 minus the value at 0. The line printed shows the three numbers; `boundary_ok` stays true only if $S_1$ equals the integral plus the boundary term for both paths. **Out [5]:** `E for the oscillator: -q(t) - Derivative(q(t), (t, 2))`, the expressions $0$, $-t$ and $-t^2 - 2$ of the three paths, the lines `line, xi = t: S1 = 2/3, integral = -1/3, boundary term = 1` and `parabola, xi = t: S1 = 3/4, integral = -5/4, boundary term = 2`, and four PASS lines.

**In [6]: Figure 07d.2.**

```python
times = np.linspace(0.0, 1.0, 201)
styles = {"true path": "-", "line": "--", "parabola": ":"}
fig, (left, right) = plt.subplots(1, 2, figsize=(9.8, 3.9))
for name, path in PATHS.items():
    left.plot(times, sp.lambdify(t, path)(times) * np.ones_like(times),
              styles[name], label=name)
    residual = sp.lambdify(t, E_of(path))(times) * np.ones_like(times)
    right.plot(times, residual, styles[name], label=name)
left.set_xlabel("time $t$")
left.set_ylabel("position $q(t)$")
left.set_title("Three paths with $q(0) = 0$, $q(1) = 1$")
left.legend(fontsize=8)
right.axhline(0.0, color="black", linewidth=0.8)
right.set_xlabel("time $t$")
right.set_ylabel("$E(t) = -\\ddot q - q$")
right.set_title("Euler-Lagrange expression")
right.legend(fontsize=8)
fig.tight_layout()
```

201 times from 0 to 1 and a dictionary of line styles. For each path the left panel draws $q(t)$ and the right panel $E(t)$; `sp.lambdify(t, ...)` makes numerical functions of the formulas. The factor `np.ones_like(times)`, an array of ones of the same length, turns a constant result (the 0 of the true path, which `lambdify` returns as the single number 0) into an array that can be drawn. Labels, titles, a black zero line and the legends follow.

```python
save_figure(fig, "paths_and_residuals",
            "Left: three paths of the oscillator with the same end values $q(0) = "
            ...)
```

**Out [6]:** the figure and its saved file `07d_2_paths_and_residuals.png`. **What Figure 07d.2 shows.** The three paths in the left panel look alike; nothing in their shapes shows which one is the true motion. The right panel tells them apart at once: $E(t)$, the amount by which Newton's law $\ddot q = -q$ fails at time $t$, is zero at every time only for the true path, $-t$ for the line and $-2 - t^2$ for the parabola.

**In [7]: narrow bumps and Figure 07d.3.**

```python
grid = np.linspace(0.0, 1.0, 200001)  # fine grid for the integrals


def E_parabola(times_):
    return -2.0 - times_**2  # E(t) of the parabola path


def bump(times_, centre, width):
    """cos^2 bump of half-width width around centre, zero outside."""
    inside = np.abs(times_ - centre) < width
    return np.where(inside, np.cos(np.pi * (times_ - centre) / (2 * width)) ** 2, 0.0)
```

`grid` is 200001 equally spaced times from 0 to 1, fine enough that the integrals below are accurate to far more digits than are printed. `E_parabola` is $E(t) = -2 - t^2$ of the parabola path, for an array of times. `bump(times_, centre, width)` is the shape $\cos^2(\pi(t - t_0)/(2w))$ inside $|t - t_0| < w$ and 0 outside: `inside` is an array of true and false values, and `np.where(inside, a, b)` takes `a` where it is true and `b` elsewhere.

```python
widths = [0.2, 0.1, 0.05, 0.025]
centres = [0.3, 0.5, 0.7]
errors = {}
for centre in centres:
    errors[centre] = []
    for width in widths:
        weight = bump(grid, centre, width)
        average = (np.trapezoid(E_parabola(grid) * weight, grid)
                   / np.trapezoid(weight, grid))
        errors[centre].append(average - E_parabola(centre))
    ratios = [errors[centre][i] / errors[centre][i + 1] for i in range(3)]
    say(f"t0 = {centre}: errors " + ", ".join(f"{e:+.3e}" for e in errors[centre])
        + "; ratios " + ", ".join(f"{r:.4f}" for r in ratios))
check(all(abs(errors[c][i] / errors[c][i + 1] - 4.0) < 1e-6
          for c in centres for i in range(3)),
      "the average of E over the bump tends to E(t0); halving w divides the error by 4")
```

Four half-widths and three centres. For each centre and width, `weight` is the bump on the grid and `average` is $\int E\xi\,dt/\int\xi\,dt$; `np.trapezoid(f, grid)` computes an integral with the trapezoidal rule (Chapter 2). The error, the average minus $E(t_0)$, is appended to a list. `ratios` divides each error by the next one (half the width). The `say` line prints the errors in **scientific notation** (`{e:+.3e}` gives three decimals and a power of ten) and the ratios with four decimals; `", ".join(...)` joins the texts with commas. The check requires that every ratio equals 4 within $10^{-6}$. **Out [7]:** for each of the three centres the errors $-5.228\times10^{-3}$, $-1.307\times10^{-3}$, $-3.267\times10^{-4}$, $-8.168\times10^{-5}$ and the ratios 4.0000, 4.0000, 4.0000, then the PASS line. These are exactly $-0.130691\,w^2$ (Section 7.3), the same for every centre because $E'' = -2$ is the same everywhere.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.8, 3.9))
left.plot(times, E_parabola(times), color="black", label="$E(t) = -2 - t^2$")
for width, marker in zip(widths[:3], ["o", "s", "^"]):
    points = np.linspace(0.25, 0.75, 6)
    averages = [np.trapezoid(E_parabola(grid) * bump(grid, c, width), grid)
                / np.trapezoid(bump(grid, c, width), grid) for c in points]
    left.plot(points, averages, marker, label=f"bump average, $w = {width}$")
shown = bump(times, 0.5, 0.2)
left.fill_between(times, -2.9, -2.9 + 0.5 * shown, color="tab:green", alpha=0.3,
                  label="a bump ($t_0 = 0.5$, $w = 0.2$)")
left.set_ylim(-3.0, -1.8)
left.set_xlabel("time $t$ (bump centre $t_0$)")
left.set_ylabel("value")
left.set_title("Averages of $E$ over bumps")
left.legend(fontsize=7, loc="upper right")
```

The left panel draws $E(t)$ in black and, for the three larger widths with three marker shapes (`zip(widths[:3], ["o", "s", "^"])` pairs each width with circles, squares or triangles), the bump averages at six centres between 0.25 and 0.75. One bump ($t_0 = 0.5$, $w = 0.2$) is shown as a green shaded area near the bottom: `fill_between(times, -2.9, -2.9 + 0.5 * shown, ...)` fills the area between the level $-2.9$ and a curve that rises by half the bump's height, `alpha=0.3` makes it transparent.

```python
for centre, marker in zip(centres, ["o", "s", "^"]):
    right.loglog(widths, np.abs(errors[centre]), marker, label=f"$t_0 = {centre}$")
reference = np.abs(errors[0.5][0]) * (np.array(widths) / widths[0]) ** 2
right.loglog(widths, reference, "--", color="grey", label="slope 2")
right.set_xticks(widths, [str(width) for width in widths])  # plain tick labels
right.minorticks_off()  # no unlabelled minor ticks
right.set_xlabel("half-width $w$ of the bump")
right.set_ylabel("|average of $E$ minus $E(t_0)$|")
right.set_title("The error falls like $w^2$")
right.legend(fontsize=8)
fig.tight_layout()
```

The right panel draws the size of the errors (`np.abs`) against the width on **logarithmic axes** (`loglog`), one marker shape per centre, and a grey dashed reference line proportional to $w^2$, which on these axes is a straight line of slope 2. `set_xticks` writes the four widths as plain numbers under the axis, and `minorticks_off()` removes the unlabelled small ticks.

```python
save_figure(fig, "bump_lemma",
            "The fundamental lemma made visible, for the parabola path with $E(t) = "
            ...)
```

**What Figure 07d.3 shows.** In the left panel the markers move onto the black curve as the bumps narrow: averaging $E$ over a narrower and narrower bump recovers its value at the centre. In the right panel the points of all three centres lie on one line of slope 2: the distance falls like $w^2$. So if $\int E\xi\,dt$ vanished for every bump, every average would be 0, and so would $E$ at every point: the fundamental lemma.

**In [8]: the derivative of the grid action.**

```python
N5 = 5
h, w_sym = sp.symbols("h omega", positive=True)
qs = sp.symbols(f"q0:{N5 + 1}", real=True)  # q_0 .. q_5
S_grid = sum(h * (((qs[n + 1] - qs[n]) / h) ** 2 / 2
                  - w_sym**2 * (qs[n] ** 2 + qs[n + 1] ** 2) / 4) for n in range(N5))
grid_E = [h * (-(qs[n + 1] - 2 * qs[n] + qs[n - 1]) / h**2 - w_sym**2 * qs[n])
          for n in range(1, N5)]
check(all(sp.simplify(sp.diff(S_grid, qs[n]) - grid_E[n - 1]) == 0
          for n in range(1, N5)),
      "dS_N/dq_n = h (-(q_(n+1) - 2 q_n + q_(n-1))/h^2 - omega^2 q_n) for every "
      "inner n")
```

$N = 5$ steps. `h` and `w_sym` are positive symbols for the step and for $\omega$; `sp.symbols(f"q0:{N5 + 1}", real=True)` makes the six symbols `q0` to `q5` (the notation `q0:6` means "q0 up to but not including q6"). `S_grid` is the grid action $S_N$ of Section 7.3, a sum over the five steps. `grid_E` is the list of the expected derivatives $h[-(q_{n+1} - 2q_n + q_{n-1})/h^2 - \omega^2q_n]$ for the inner points $n = 1, \dots, 4$. The check differentiates `S_grid` with respect to each inner value and compares. **Out [8]:** one PASS line.

**In [9]: solving the grid equations, and Figure 07d.4.**

```python
def grid_path(N):
    """Solve the grid equations: returns the grid times and q_0 .. q_N."""
    step = 1.0 / N
    A = np.zeros((N - 1, N - 1))  # one row per inner point n = 1 .. N-1
    b = np.zeros(N - 1)
    for i in range(N - 1):
        A[i, i] = 2.0 / step**2 - 1.0  # from -(-2 q_n)/h^2 - omega^2 q_n
        if i > 0:
            A[i, i - 1] = -1.0 / step**2  # the neighbour q_(n-1)
        if i < N - 2:
            A[i, i + 1] = -1.0 / step**2  # the neighbour q_(n+1)
    b[-1] = 1.0 / step**2  # the known end value q_N = 1 moved to the right side
    inner = np.linalg.solve(A, b)
    return np.linspace(0.0, 1.0, N + 1), np.concatenate([[0.0], inner, [1.0]])
```

`grid_path(N)` solves the $N - 1$ linear equations "the bracket is zero at every inner point" for $\omega = 1$, $T = 1$, $q_0 = 0$, $q_N = 1$. Multiplying the bracket by $-1$, the equation at the inner point $n$ is $-q_{n-1}/h^2 + (2/h^2 - 1)q_n - q_{n+1}/h^2 = 0$. The matrix `A` holds these coefficients: row `i` belongs to the inner point $n = i + 1$; its diagonal entry is $2/h^2 - 1$ and its neighbours $-1/h^2$ (the `if` lines leave out neighbours that are end points). The known end value $q_N = 1$ appears only in the last row, as $-1/h^2$ times 1; moved to the right side it gives `b[-1] = 1.0 / step**2` (the index `-1` means the last entry). `np.linalg.solve(A, b)` solves the equations, and the function returns the $N + 1$ grid times and the values with the two end values added in front and behind (`np.concatenate`).

```python
sizes = [4, 8, 16, 32, 64, 128, 256]
grid_errors = []
for N in sizes:
    nodes, values = grid_path(N)
    grid_errors.append(np.abs(values - np.sin(nodes) / np.sin(1.0)).max())
orders = [np.log2(grid_errors[i] / grid_errors[i + 1]) for i in range(len(sizes) - 1)]
say("largest errors: " + ", ".join(f"N = {N}: {e:.3e}"
                                   for N, e in zip(sizes, grid_errors)))
say("observed orders: " + ", ".join(f"{p:.3f}" for p in orders))
check(all(1.9 < p < 2.1 for p in orders),
      "the stationary grid path converges to the true path with order 2")
```

For $N = 4, 8, \dots, 256$ the largest distance between the grid path and the true path $\sin t/\sin 1$ at the grid times is stored. `np.log2(e_N/e_{2N})` is the observed order: if the error is $Ch^p$, halving $h$ divides it by $2^p$, and the logarithm to base 2 of the ratio is $p$ (Chapter 2). The check requires every observed order between 1.9 and 2.1. **Out [9]:** the errors $4.089\times10^{-4}$ ($N = 4$), $1.017\times10^{-4}$, $2.582\times10^{-5}$, $6.452\times10^{-6}$, $1.613\times10^{-6}$, $4.032\times10^{-7}$, $1.008\times10^{-7}$ ($N = 256$), the orders 2.007, 1.978, 2.001, 2.000, 2.000, 2.000 and the PASS line.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.8, 3.9))
left.plot(times, np.sin(times) / np.sin(1.0), color="black", label="true path")
for N, marker in ((4, "o"), (8, "s")):
    nodes, values = grid_path(N)
    left.plot(nodes, values, marker, label=f"stationary grid path, $N = {N}$")
left.set_xlabel("time $t$")
left.set_ylabel("position $q$")
left.set_title("The action on a grid")
left.legend(fontsize=8)
steps = 1.0 / np.array(sizes)
right.loglog(steps, grid_errors, "o-", label="largest error")
right.loglog(steps, grid_errors[0] * (steps / steps[0]) ** 2, "--", color="grey",
             label="slope 2")
right.set_xlabel("step $h = 1/N$")
right.set_ylabel("largest difference from the true path")
right.set_title("Second-order convergence")
right.legend(fontsize=8)
fig.tight_layout()
save_figure(fig, "action_on_a_grid",
...)
```

The left panel draws the true path as a black line and, for $N = 4$ (circles) and $N = 8$ (squares), the points of the stationary grid path, computed again with `grid_path`. For the right panel `steps` is the array of the steps $h = 1/N$ (`np.array` turns the list of sizes into an array, so that `1.0 /` divides every entry); the largest errors are drawn against the steps on logarithmic axes, as dots joined by lines, and the grey dashed reference line is the first error times $(h/h_0)^2$, a line of slope 2 through the first point. Labels, titles and legends follow, and `save_figure` saves the figure.

**What Figure 07d.4 shows.** Already four steps give a grid path whose points lie on the true path to the eye. On the right the errors lie on a line parallel to the slope-2 guide: halving the step divides the error by 4. So the principle of stationary action can be used directly on a computer, and the grid solution converges to the true motion.

**In [10]: the energy, and Figure 07d.5.**

```python
def energy(path):
    """H = (1/2) q'^2 + (1/2) omega^2 q^2 of a path."""
    return sp.diff(path, t) ** 2 / 2 + omega**2 * path**2 / 2


check(sp.simplify(sp.diff(energy(q), t) + sp.diff(q, t) * E_general) == 0,
      "dH/dt = -q' E for every path")
for name, path in PATHS.items():
    say(f"{name:9s}: dH/dt = {sp.simplify(sp.diff(energy(path), t))}")
check(sp.simplify(sp.diff(energy(PATHS["true path"]), t)) == 0
      and all(sp.simplify(sp.diff(energy(PATHS[name]), t)) != 0
              for name in ("line", "parabola")),
      "H is constant on the true path and changes on the two wrong paths")
true_energy = sp.simplify(energy(PATHS["true path"]))
report("energy of the true path", f"{true_energy} = {float(true_energy):.6f}")
```

`energy(path)` is $H = \tfrac12\dot q^2 + \tfrac12\omega^2q^2$. The first check is the identity $dH/dt = -\dot q\,E$ of Section 7.4 for a general path (the sum $dH/dt + \dot q E$ simplifies to 0). The loop prints $dH/dt$ on the three paths; the second check requires 0 for the true path and a nonzero result for the two wrong ones. `report` prints the energy of the true path exactly and as a decimal. **Out [10]:** two PASS lines, `true path: dH/dt = 0`, `line: dH/dt = t`, `parabola: dH/dt = 2*t*(t**2 + 2)` and `RESULT energy of the true path = 1/(2*sin(1)**2) = 0.706141`.

```python
fig, ax = plt.subplots()
for name, path in PATHS.items():
    values = sp.lambdify(t, energy(path))(times) * np.ones_like(times)
    ax.plot(times, values, styles[name], label=name)
ax.set_xlabel("time $t$")
ax.set_ylabel("$H = \\frac{1}{2}\\dot q^2 + \\frac{1}{2}q^2$")
ax.set_title("The energy along the three paths")
ax.legend(fontsize=8)
save_figure(fig, "energy_along_paths",
...)
```

One panel: the energy along each path against the time. **What Figure 07d.5 shows.** The solid line of the true path is flat at $1/(2\sin^21) \approx 0.706$; the energies of the line and the parabola change, because their $E$ is not zero.

**In [11]: a total derivative changes nothing.**

```python
F = t * q**3  # F(q, t)
L = lagrangian(q, sp.diff(q, t))
E_changed = euler_lagrange(L + sp.diff(F, t), [q], t)[0]
check(sp.simplify(E_changed - E_general) == 0,
      "L + dF/dt with F = t q^3 has the same Euler-Lagrange expression as L")
E_pure = euler_lagrange(sp.diff(q**2, t), [q], t)[0]
check(E_pure == 0, "the pure total derivative d(q^2)/dt gives E = 0 for every path")
differences = [sp.simplify(sp.integrate(sp.diff(F.subs(q, path), t), (t, 0, 1)))
               for path in PATHS.values()]
say(f"S'[path] - S[path] for the three paths: {differences}")
check(all(d == 1 for d in differences),
      "the action changes by F(q(1), 1) - F(q(0), 0) = 1 for every path")
```

`F` is $F(q, t) = t\,q^3$ for the general path `q` of In [5]. `E_changed` is the Euler-Lagrange expression of $L + dF/dt$ (`sp.diff(F, t)` is the total derivative along the path, because `q` is a function of `t`); the first check requires it to equal that of $L$. `E_pure` is the expression of the pure total derivative $\frac{d}{dt}q^2$; the second check requires it to be 0. `differences` holds, for each of the three paths, the change $\int_0^1\frac{dF}{dt}\,dt$ of the action; it is printed, and the third check requires it to be 1 for every path. **Out [11]:** three PASS lines and `S'[path] - S[path] for the three paths: [1, 1, 1]`.

**In [12]: the two first-order Lagrangians.**

```python
w = sp.Symbol("omega", positive=True)
q0, q1 = sp.Function("q0")(t), sp.Function("q1")(t)
L_A = (q0 * sp.diff(q1, t) - q1 * sp.diff(q0, t)) / 2 - w * (q0**2 + q1**2) / 2
E_A = euler_lagrange(L_A, [q0, q1], t)
say(f"Example A: E_0 = {E_A[0]},  E_1 = {E_A[1]}")
check(sp.simplify(E_A[0] - (sp.diff(q1, t) - w * q0)) == 0
      and sp.simplify(E_A[1] - (-sp.diff(q0, t) - w * q1)) == 0,
      "Example A: E_0 = q1' - omega q0, E_1 = -q0' - omega q1")
rotation = {q0: sp.cos(w * t), q1: sp.sin(w * t)}
check(all(sp.simplify(e.subs(rotation).doit()) == 0 for e in E_A),
      "Example A: q0 = cos(omega t), q1 = sin(omega t) solves both equations")
```

`w` is $\omega$ as a positive symbol and `q0`, `q1` are two unknown functions of $t$. `L_A` is Example A of Section 7.4, and `E_A` the list of its two Euler-Lagrange expressions (the function `euler_lagrange` of In [5] works for several functions at once). The first check compares them with $\dot q_1 - \omega q_0$ and $-\dot q_0 - \omega q_1$, the second puts in the rotation $q_0 = \cos\omega t$, $q_1 = \sin\omega t$ and requires both to vanish.

```python
psi, psi_star = sp.Function("psi")(t), sp.Function("psistar")(t)
L_B = (sp.I / 2 * (psi_star * sp.diff(psi, t) - sp.diff(psi_star, t) * psi)
       - w * psi_star * psi)
E_B = euler_lagrange(L_B, [psi_star, psi], t)  # vary psi* first, then psi
say(f"Example B: E_psi* = {E_B[0]},  E_psi = {E_B[1]}")
complex_form = {psi: (q0 + sp.I * q1) / sp.sqrt(2), psi_star: (q0 - sp.I * q1)
                / sp.sqrt(2)}
L_B_real = (q1 * sp.diff(q0, t) - q0 * sp.diff(q1, t)) / 2 - w * (q0**2 + q1**2) / 2
check(sp.simplify(sp.expand(L_B.subs(complex_form).doit() - L_B_real)) == 0,
      "Example B in real variables is Example A with the rotation reversed")
```

`psi` and `psi_star` are two unknown functions $\psi$ and $\psi^*$, varied as independent functions; `sp.I` is the imaginary unit $i$. `L_B` is Example B. `E_B` lists the expressions for $\psi^*$ (first) and $\psi$. `complex_form` is the dictionary that writes $\psi$ and $\psi^*$ in terms of $q_0$ and $q_1$, and `L_B_real` is the real form of Section 7.4; the check requires `L_B` with the substitution to equal it.

```python
E_real = euler_lagrange(L_B_real, [q0, q1], t)
combined = E_B[0].subs(complex_form).doit() - (E_real[0] + sp.I * E_real[1]) / sp.sqrt(2)
check(sp.simplify(sp.expand(combined)) == 0,
      "E_psi* = (E_q0 + i E_q1)/sqrt(2): varying psi* is varying q0 and q1")
check(sp.simplify(E_B[0] - (sp.I * sp.diff(psi, t) - w * psi)) == 0
      and sp.simplify(E_B[0].subs(psi, sp.exp(-sp.I * w * t)).doit()) == 0,
      "Example B: i psi' = omega psi, solved by psi = exp(-i omega t)")
```

`E_real` are the expressions of the real form. `combined` is $E_{\psi^*}$ written in $q_0, q_1$ minus $(E_{q_0} + iE_{q_1})/\sqrt2$; the check requires it to vanish: varying $\psi^*$ is the same as varying $q_0$ and $q_1$. The last check compares $E_{\psi^*}$ with $i\dot\psi - \omega\psi$ and puts in $\psi = e^{-i\omega t}$. **Out [12]:** the four expressions and five PASS lines.

**In [13]: Figure 07d.6.**

```python
turn = np.linspace(0.0, 1.5 * np.pi, 200)  # times up to three quarters of a turn
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 4.2))
for sense, label, style, colour in ((1.0, "Example A", "-", "tab:blue"),
                                    (-1.0, "Example B", "--", "tab:orange")):
    x, y = np.cos(turn), sense * np.sin(turn)
    left.plot(x, y, style, color=colour, label=label)
    for i in (30, 150):  # arrows that show the sense of the motion
        left.annotate("", xy=(x[i + 4], y[i + 4]), xytext=(x[i], y[i]),
                      arrowprops={"arrowstyle": "->", "lw": 1.5, "color": colour})
left.plot([1.0], [0.0], "ko")
left.text(1.05, 0.05, "start")
left.set_aspect("equal")
left.set_xlim(-1.4, 1.4)
left.set_ylim(-1.4, 1.4)
left.set_xlabel("$q_0$")
left.set_ylabel("$q_1$")
left.set_title("First-order motion: a rotation")
left.legend(fontsize=8, loc="lower left")
```

`turn` holds 200 times from 0 to $1.5\pi$, three quarters of a turn for $\omega = 1$. The loop draws both motions in the plane $(q_0, q_1)$: `sense` is $+1$ for Example A ($q_1 = \sin t$) and $-1$ for Example B ($q_1 = -\sin t$). For each, two arrows show the sense of motion: `annotate("", xy=..., xytext=...)` draws an arrow from the point at index `i` to the point four indices later, with the arrow style given in `arrowprops`. A black dot marks the start $(1, 0)$; `set_aspect("equal")` makes one unit equally long on both axes, so the circle looks round.

```python
psi_values = np.exp(-1j * turn) / np.sqrt(2)  # psi(t) = exp(-i t) psi(0)
right.plot(turn, psi_values.real, label="real part of $\\psi$")
right.plot(turn, psi_values.imag, "--", label="imaginary part of $\\psi$")
right.plot(turn, np.abs(psi_values) ** 2, ":", color="black",
           label="$|\\psi|^2 = \\frac{1}{2}$")
right.set_xlabel("time $t$")
right.set_ylabel("value")
right.set_ylim(-0.85, 1.15)  # room for the legend above the curves
right.set_title("$\\psi(t) = e^{-it}\\psi(0)$")
right.legend(fontsize=7, loc="upper center", ncol=3)
fig.tight_layout()
save_figure(fig, "first_order_rotation",
...)
```

The right panel draws $\psi(t) = e^{-it}/\sqrt2$ (`1j` is Python's imaginary unit; `.real` and `.imag` are the real and imaginary parts) and $|\psi|^2$. **What Figure 07d.6 shows.** Both first-order motions run on the unit circle; Example A turns counterclockwise and Example B, whose kinetic term has the opposite sign, clockwise. On the right the real and imaginary parts of $\psi$ oscillate a quarter period apart while $|\psi|^2 = \tfrac12$ stays constant.

**In [14]: a field of a space direction and time.**

```python
x1, x4, x5 = sp.symbols("x1 x4 x5", real=True)
m = sp.Symbol("m", positive=True)
```

Three real coordinate symbols $x_1, x_4, x_5$ and the mass $m$ as a positive symbol.

```python
def field_euler_lagrange(L, field, coordinates):
    """dL/dphi - sum over the coordinates of d/dx dL/d(dphi/dx)."""
    value = sp.Symbol("P")  # stands for phi
    slopes = [sp.Symbol(f"D{i}") for i in range(len(coordinates))]  # dphi/dx
    plain = L
    for x, slope in zip(coordinates, slopes):
        plain = plain.subs(sp.diff(field, x), slope)
    plain = plain.subs(field, value)
    back = {**{s: sp.diff(field, x) for x, s in zip(coordinates, slopes)},
            value: field}
    result = sp.diff(plain, value).subs(back)
    for x, slope in zip(coordinates, slopes):
        result -= sp.diff(sp.diff(plain, slope).subs(back), x)
    return sp.expand(result)
```

`field_euler_lagrange(L, field, coordinates)` is the recipe of Section 7.5: like `euler_lagrange` of In [5], it replaces the field's derivatives by the symbols `D0`, `D1`, ... (one per coordinate) and then the field by `P`; it differentiates with respect to `P`, puts the functions back, and subtracts for each coordinate the derivative along that coordinate of the derivative with respect to its slope symbol.

```python
ETA = {x1: 1, x4: -1, x5: -1}  # the author's signs: x1 space-like, x4, x5 time-like
phi = sp.Function("phi")(x1, x4)
L_space = (-(ETA[x1] * sp.diff(phi, x1) ** 2 + ETA[x4] * sp.diff(phi, x4) ** 2) / 2
           - m**2 * phi**2 / 2)
E_space = field_euler_lagrange(L_space, phi, [x1, x4])
say(f"E = {E_space}")
check(sp.simplify(E_space - (sp.diff(phi, x1, 2) - sp.diff(phi, x4, 2)
                             - m**2 * phi)) == 0,
      "space and time: E = d1^2 phi - d4^2 phi - m^2 phi (Klein-Gordon)")
k, frequency = sp.symbols("k omega_k", positive=True)
wave = sp.cos(k * x1) * sp.cos(frequency * x4)
on_wave = E_space.subs(phi, wave).doit()
check(sp.simplify(on_wave.subs(frequency, sp.sqrt(m**2 + k**2))) == 0
      and sp.simplify(on_wave.subs(frequency, k)) != 0,
      "cos(k x1) cos(omega x4) solves it exactly when omega^2 = m^2 + k^2")
```

`ETA` holds the author's signs for the three coordinates used: $+1$ for $x_1$, $-1$ for $x_4$ and $x_5$. `phi` is an unknown field $\phi(x_1, x_4)$, and `L_space` the Lagrangian density of Section 7.5. The first check compares the Euler-Lagrange expression with $\partial_1^2\phi - \partial_4^2\phi - m^2\phi$. For the plane wave $\cos(kx_1)\cos(\omega x_4)$, the second check requires $E = 0$ when $\omega = \sqrt{m^2 + k^2}$ and $E \neq 0$ for the wrong value $\omega = k$.

```python
rng = np.random.default_rng(12345)  # random numbers with a fixed seed
h1, h4, mass = 0.3, 0.2, 1.5  # grid steps and the mass
field_values = rng.normal(size=(7, 6))  # phi_ij: i along x1, j along x4


def grid_action(f):
    """The field action on the grid: a sum over the cells."""
    d4 = (f[:-1, 1:] - f[:-1, :-1]) / h4  # time differences
    d1 = (f[1:, :-1] - f[:-1, :-1]) / h1  # space differences
    return h1 * h4 * np.sum(d4**2 / 2 - d1**2 / 2 - mass**2 * f[:-1, :-1] ** 2 / 2)

```

Now the same on a grid of 7 by 6 points with steps $h_1 = 0.3$ and $h_4 = 0.2$ and mass 1.5. `rng` is a random-number generator with a fixed **seed** 12345, so that every run draws the same numbers; `rng.normal(size=(7, 6))` gives a table of random field values $\phi_{ij}$. `grid_action(f)` is the action on the grid: in each cell the time difference `d4` and the space difference `d1` (array slices such as `f[:-1, 1:]` take all rows but the last and all columns but the first), and the sum of $h_1h_4[\tfrac12d_4^2 - \tfrac12d_1^2 - \tfrac12m^2\phi^2]$.

```python
largest = 0.0
delta = 1e-3
for i in range(1, 6):
    for j in range(1, 5):
        plus, minus = field_values.copy(), field_values.copy()
        plus[i, j] += delta
        minus[i, j] -= delta
        numeric = (grid_action(plus) - grid_action(minus)) / (2 * delta)
        f_ = field_values  # a short name for the formula below
        expected = h1 * h4 * (
            (f_[i + 1, j] - 2 * f_[i, j] + f_[i - 1, j]) / h1**2  # space part
            - (f_[i, j + 1] - 2 * f_[i, j] + f_[i, j - 1]) / h4**2  # time part
            - mass**2 * f_[i, j])
        largest = max(largest, abs(numeric - expected))
say("largest difference over the 20 inner points is below 1e-9: "
    f"{largest < 1e-9}")
check(largest < 1e-9, "on the grid: dS/dphi_ij = h1 h4 times the grid "
      "Euler-Lagrange expression at every inner point")
```

For each of the 20 inner points, the derivative of the grid action with respect to $\phi_{ij}$ is computed numerically by the **central difference** $(S(\phi_{ij} + \delta) - S(\phi_{ij} - \delta))/(2\delta)$ with $\delta = 10^{-3}$ (`.copy()` makes independent copies of the table, so that only one entry is changed). For an action that is quadratic in $\phi$ this is exact up to rounding. `expected` is $h_1h_4$ times the grid Euler-Lagrange expression (second difference quotients in place of $\partial_1^2$ and $\partial_4^2$). The largest difference is printed as a true or false statement and checked to be below $10^{-9}$. **Out [14]:** the expression `E = -m**2*phi(x1, x4) + Derivative(...) - Derivative(...)`, the PASS lines and `largest difference over the 20 inner points is below 1e-9: True`.

**In [15]: a field of an extra time and time, and the record's growth rate.**

```python
phi5 = sp.Function("phi")(x5, x4)
L_extra = (-(ETA[x5] * sp.diff(phi5, x5) ** 2 + ETA[x4] * sp.diff(phi5, x4) ** 2) / 2
           - m**2 * phi5**2 / 2)
E_extra = field_euler_lagrange(L_extra, phi5, [x5, x4])
say(f"E = {E_extra}")
check(sp.simplify(E_extra - (-sp.diff(phi5, x5, 2) - sp.diff(phi5, x4, 2)
                             - m**2 * phi5)) == 0,
      "extra time and time: E = -d5^2 phi - d4^2 phi - m^2 phi")
kappa = sp.Symbol("kappa", positive=True)
growing = sp.cos(k * x5) * sp.cosh(kappa * x4)
check(sp.simplify(E_extra.subs(phi5, growing).doit()
                  .subs(kappa, sp.sqrt(k**2 - m**2))) == 0,
      "cos(k x5) cosh(kappa x4) solves it with kappa^2 = k^2 - m^2: growth for k > m")
```

`phi5` is an unknown field $\phi(x_5, x_4)$ and `L_extra` its Lagrangian density with the sign $\eta_{55} = -1$. The first check compares the expression with $-\partial_5^2\phi - \partial_4^2\phi - m^2\phi$; the second puts in $\cos(kx_5)\cosh(\kappa x_4)$ and requires $E = 0$ when $\kappa = \sqrt{k^2 - m^2}$.

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
G = [sp.Matrix(g) for g in fixture["gamma"]]  # gamma^(x1) .. gamma^(x8)
signs = [1, 1, 1, -1, -1, -1, -1, 1]  # eta in the order x1 .. x8
ks = sp.symbols("k1:9", real=True)  # a frame momentum with 8 components
slash = sum((ks[a] * G[a] for a in range(8)), sp.zeros(16, 16))  # gamma^(a) k_a
norm = sum(signs[a] * ks[a] ** 2 for a in range(8))  # eta^ab k_a k_b
check((slash * slash - norm * sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16),
      "(gamma^a k_a)^2 = (k1^2 + k2^2 + k3^2 - k4^2 - k5^2 - k6^2 - k7^2 + k8^2) I16",
      record=reproduces("Revision/theory/reports/python-field-theory.json",
                        "clifford_relations"))
```

The notebook now reads the author's gammas from the Revision record `Revision/algebra/gammas.json` (the key `"gamma"` holds the eight $16\times16$ integer matrices in the order $x_1, \dots, x_8$) and turns them into exact sympy matrices. `signs` is $\eta$ in the same order, `ks` eight real symbols $k_1, \dots, k_8$. `slash` is $\sum_ak_a\gamma^{(a)}$ (the sum starts from the zero matrix `sp.zeros(16, 16)`), and `norm` is $\sum_a\eta^{aa}k_a^2$. The check multiplies out `slash * slash - norm * I16` entry by entry (`applyfunc(sp.expand)`) and requires the zero matrix; its second line names the Revision check it reproduces.

```python
SCOPE = "Revision/theory/reports/python-scope.json"
detail = revision_check(SCOPE, "extra_time_growth_rates_unbounded")["detail"]
formula = re.search(r"Im E = (sqrt\([^)]*\))", detail).group(1)  # the record's rate
say(f"growth rate in the record: {formula}")
K = sp.Symbol("K", positive=True)
rate = sp.sympify(formula, locals={"K": K, "m": m,
                                   **{f"k{i}": sp.Symbol(f"k{i}") for i in range(9)}})
along_x5 = rate.subs({sp.Symbol(f"k{i}"): 0 for i in (1, 2, 3, 8)}).subs(K, k)
check(sp.simplify(along_x5 - sp.sqrt(k**2 - m**2)) == 0,
      "the record's rate for a momentum along x5 only is sqrt(k^2 - m^2) = kappa",
      record=reproduces(SCOPE, "extra_time_growth_rates_unbounded"))
```

`detail` is the detail text of the scope record's check `extra_time_growth_rates_unbounded`. `re.search(r"Im E = (sqrt\([^)]*\))", detail)` finds in it the text that follows "Im E = ", a `sqrt(...)` up to the first closing parenthesis; `.group(1)` is that text, printed as `sqrt(K**2 - k1**2 - k2**2 - k3**2 - k8**2 - m**2)`. `sp.sympify` turns it into a formula (the dictionary `locals` tells sympy which names are which symbols). Setting $k_1 = k_2 = k_3 = k_8 = 0$ and $K = k$ gives the rate for a momentum along $x_5$ alone, and the check compares it with $\sqrt{k^2 - m^2}$. **Out [15]:** the expression, four PASS lines, two of them with the "reproduces" line, and the formula of the record.

**In [16]: Figures 07d.7 and 07d.8.**

```python
coordinate = np.linspace(0.0, 2 * np.pi / 2.0, 121)  # one wavelength for k = 2
clock = np.linspace(0.0, 2.0, 101)  # the time x4 from 0 to 2
X, Y = np.meshgrid(coordinate, clock)
space_wave = np.cos(2.0 * X) * np.cos(np.sqrt(5.0) * Y)
extra_wave = np.cos(2.0 * X) * np.cosh(np.sqrt(3.0) * Y)
fig, (left, right) = plt.subplots(1, 2, figsize=(9.8, 4.2))
image = left.pcolormesh(X, Y, space_wave, cmap="coolwarm", vmin=-1, vmax=1,
                        shading="auto")
fig.colorbar(image, ax=left, shrink=0.85)
left.set_xlabel("space coordinate $x_1$")
left.set_ylabel("time $x_4$")
left.set_title("$\\cos(2x_1)\\cos(\\sqrt{5}x_4)$: oscillates")
limit = float(np.cosh(np.sqrt(3.0) * 2.0))
image = right.pcolormesh(X, Y, extra_wave, cmap="coolwarm", vmin=-limit, vmax=limit,
                         shading="auto")
fig.colorbar(image, ax=right, shrink=0.85)
right.set_xlabel("extra time $x_5$")
right.set_ylabel("time $x_4$")
right.set_title("$\\cos(2x_5)\\cosh(\\sqrt{3}x_4)$: grows")
for ax in (left, right):
    ax.grid(False)
```

`coordinate` is one wavelength $2\pi/k = \pi$ of a coordinate for $k = 2$, `clock` the time from 0 to 2. `np.meshgrid` makes two tables `X`, `Y` that hold the coordinate and the time at every point of a 121 by 101 grid. `space_wave` is $\cos(2x_1)\cos(\sqrt5x_4)$ (for $m = 1$, $k = 2$: $\omega = \sqrt{1 + 4}$), `extra_wave` is $\cos(2x_5)\cosh(\sqrt3x_4)$ ($\kappa = \sqrt{4 - 1}$). `pcolormesh` draws each table as a colour map (red positive, blue negative in the colour scheme `coolwarm`); `colorbar` adds the colour scale. The right panel's scale reaches $\cosh(2\sqrt3) \approx 16$ (`limit`). `ax.grid(False)` switches the grid lines off over the colour maps.

```python
fig.tight_layout()
save_figure(fig, "space_and_extra_time",
            "Two exact solutions of the field equation with mass $m = 1$ and wave "
            ...)
```

**What Figure 07d.7 shows.** On the left the colours repeat in time: the wave along the space direction oscillates between $-1$ and $1$. On the right the colours grow stronger with time: the wave along the extra time grows like $\cosh(\sqrt3x_4)$. The two Lagrangians differ only by the sign of one term.

```python
numbers = np.linspace(0.0, 3.0, 301)  # the wave number k, with m = 1
fig, (left, right) = plt.subplots(1, 2, figsize=(9.8, 3.9))
left.plot(numbers, 1.0 + numbers**2, label="along a space direction: $m^2 + k^2$")
left.plot(numbers, 1.0 - numbers**2, "--",
          label="along an extra time: $m^2 - k^2$")
left.axhline(0.0, color="black", linewidth=0.8)
left.set_xlabel("wave number $k$")
left.set_ylabel("$\\omega^2$")
left.set_title("Dispersion relations ($m = 1$)")
left.legend(fontsize=8)
above = numbers[numbers > 1.0]
right.plot(above, np.sqrt(above**2 - 1.0), color="tab:red",
           label="$\\kappa = \\sqrt{k^2 - m^2}$")
right.plot(above, above, ":", color="grey", label="$\\kappa = k$ (large $k$)")
right.set_xlim(0.0, 3.0)
right.set_xlabel("wave number $k$ along the extra time")
right.set_ylabel("growth rate $\\kappa$")
right.set_title("Growth without upper bound")
right.legend(fontsize=8)
fig.tight_layout()
save_figure(fig, "dispersion",
...)
```

The second figure: on the left $\omega^2 = 1 + k^2$ and $\omega^2 = 1 - k^2$ against the wave number $k$ from 0 to 3; on the right, for $k > 1$ (`numbers[numbers > 1.0]` keeps only those values), the growth rate $\kappa = \sqrt{k^2 - 1}$ and the dotted line $\kappa = k$ that it approaches. **Out [16]:** the two figures and their saved files.

**What Figure 07d.8 shows.** Along a space direction $\omega^2$ is always positive (oscillation); along an extra time it falls below zero for $k > m$, and then the wave grows at the rate $\kappa$, which keeps growing with $k$ and has no upper bound: the same rate as in the Revision record for the 16-component field.

**In [17]: the last check.**

```python
names = ["action_versus_epsilon", "paths_and_residuals", "bump_lemma",
         "action_on_a_grid", "energy_along_paths", "first_order_rotation",
         "space_and_extra_time", "dispersion"]
files = [f"{FIGURE_FOLDER}/07d_{k_}_{name}.png" for k_, name in enumerate(names, 1)]
check(all(output_file(path).is_file() for path in files),
      "all 8 figure files of this notebook exist")
all_checks_passed()
```

The list of the eight figure names, and the list of their file paths built with `enumerate(names, 1)`, which numbers them from 1. The check requires that every file exists in the output folder; `all_checks_passed()` prints the last line. **Out [17]:** `PASS all 8 figure files of this notebook exist` and `ALL 30 CHECKS PASSED (notebook 07d)`.

### 7.10 Grassmann numbers from zero

**Why anticommuting numbers.** Electrons, and the quanta of the field dirac16complex, are **fermions**: two of them never occupy the same state (the Pauli principle). In the quantum theory this is expressed by field operators that **anticommute**, $XY = -YX$ (Chapter 10). The classical field from which such operators are obtained is therefore given values that anticommute: the Revision record defines the components of dirac16complex in this way (ASSUMED here as the definition of the field; Revision/SPEC.md, section 3). Such values are not measured; they are bookkeeping symbols with exact rules, and every statement about them is a statement about these rules.

**Generators and the defining rule.** Take $n$ symbols $\theta_0, \theta_1, \dots, \theta_{n-1}$, called **generators**. The one rule is

$$
\theta_i\theta_j = -\theta_j\theta_i\qquad\text{for all } i, j .
$$

Ordinary numbers are allowed as factors and commute with everything. Setting $j = i$ in the rule gives $\theta_i\theta_i = -\theta_i\theta_i$, that is $2\theta_i\theta_i = 0$ (add $\theta_i\theta_i$ to both sides), so

$$
\theta_i^2 = 0 .
$$

A generator times itself is zero. This is the algebraic form of the Pauli principle.

**Monomials and the sign of a reordering.** A product of generators can be put into increasing order of the indices by exchanging neighbours that stand in the wrong order, one pair at a time; every exchange costs a factor $-1$ by the defining rule. Example: $\theta_2\theta_0\theta_1$. Exchange $\theta_2$ and $\theta_0$: $-\theta_0\theta_2\theta_1$. Exchange $\theta_2$ and $\theta_1$: $+\theta_0\theta_1\theta_2$. Two exchanges, sign $+1$. Another: $\theta_1\theta_0 = -\theta_0\theta_1$, one exchange, sign $-1$. If a generator occurs twice, the two copies can be brought next to each other, and the product is 0. A product of different generators in increasing order, such as $\theta_0\theta_2\theta_5$, is called a **monomial**; the empty product is the number 1; the number of generators in a monomial is its **degree**. Every product of generators is therefore $0$, or $+1$ or $-1$ times exactly one monomial. The sign does not depend on the order in which the exchanges are made: every way of sorting a list by exchanging neighbours uses a number of exchanges of the same parity (even or odd), because each exchange of two neighbours changes the number of pairs that stand in the wrong order by exactly one. (Notebook 07a, In [2], computes the sign by sorting, and In [3] by counting the pairs in the wrong order; the two agree on 2000 random examples.)

**The Grassmann algebra.** The **Grassmann algebra** of the $n$ generators is the set of all sums of ordinary numbers times monomials, with the defining rule. Its elements are called **Grassmann numbers**, and the ordinary numbers in front of the monomials are their **coefficients**. Two elements are added by adding the coefficients of equal monomials, and multiplied by multiplying every term of the first with every term of the second, each product of monomials being reordered with its sign. Example with two generators: for $F = a + b\theta_0 + c\theta_1 + d\theta_0\theta_1$ and $F' = a' + b'\theta_0 + c'\theta_1 + d'\theta_0\theta_1$,

$$
FF' = aa' + (ab' + ba')\theta_0 + (ac' + ca')\theta_1 + (ad' + da' + bc' - cb')\,\theta_0\theta_1 .
$$

Rule for each term: $b\theta_0\,c'\theta_1 = bc'\,\theta_0\theta_1$ (already in order); $c\theta_1\,b'\theta_0 = cb'\,\theta_1\theta_0 = -cb'\,\theta_0\theta_1$ (one exchange); every product with a repeated generator, such as $b\theta_0\,b'\theta_0$ or $b\theta_0\,d'\theta_0\theta_1$, vanishes. (PROVED; Notebook 07a, In [5].)

**How big is a Grassmann algebra?** The product $(1 + \theta_0)(1 + \theta_1)\cdots(1 + \theta_{n-1})$, multiplied out, contains every monomial exactly once, with coefficient $+1$: from each bracket we take either 1 or $\theta_i$, and the chosen generators come out in increasing order, so no reordering is needed. So the number of monomials, called the **dimension** of the algebra, is $2^n$ (each generator is either in a monomial or not: two choices, $n$ times). The number of monomials of degree $k$ is the number of ways to choose $k$ of the $n$ generators, the **binomial coefficient** $\binom{n}{k} = \frac{n!}{k!(n-k)!}$, where $n! = 1\cdot2\cdots n$ is the **factorial** ($0! = 1$). For $n = 8$ these are 1, 8, 28, 56, 70, 56, 28, 8, 1, which add up to $2^8 = 256$ (PROVED; Notebook 07a counts the monomials for $n = 0$ to 12, In [6], Figure 07a.1). For ordinary commuting symbols there would be infinitely many monomials ($q, q^2, q^3, \dots$ are all different); anticommuting symbols give a finite algebra.

**The multiplication table of three generators.** With three generators the eight monomials are $1, \theta_0, \theta_1, \theta_2, \theta_0\theta_1, \theta_0\theta_2, \theta_1\theta_2, \theta_0\theta_1\theta_2$. A product of two of them is nonzero exactly when each of the three generators is in the left factor, in the right factor, or in neither (in both would repeat it): three possibilities for each of three generators, $3^3 = 27$ nonzero products among the $8\times8 = 64$ (PROVED; Notebook 07a, In [7], Figure 07a.2).

### 7.11 Even and odd elements, conjugation and derivatives

**Even and odd.** Moving a monomial $X$ of degree $k$ past a monomial $Y$ of degree $l$ (with no common generator) moves each of the $k$ generators of $X$ past each of the $l$ generators of $Y$: $kl$ exchanges. So

$$
YX = (-1)^{kl}\,XY .
$$

An element is **even** if all its monomials have even degree, **odd** if all have odd degree. If $k$ or $l$ is even, $kl$ is even and the sign is $+1$: an even element commutes with everything. If both are odd, the sign is $-1$: two odd elements anticommute (PROVED; Notebook 07a measures the sign for $k, l = 0$ to 4, In [8], Figure 07a.3). The Lagrangian of dirac16complex contains the components in pairs, so it is even and behaves like an ordinary number in the order of factors. One more consequence: every odd element squares to zero. For example $(3\theta_0 + 5\theta_1)^2 = 9\theta_0^2 + 15\theta_0\theta_1 + 15\theta_1\theta_0 + 25\theta_1^2 = 15\theta_0\theta_1 - 15\theta_0\theta_1 = 0$ (Notebook 07a, In [5]).

**Complex Grassmann numbers and conjugation.** The components of dirac16complex are complex, and complex numbers have conjugates. For complex Grassmann numbers the generators come in pairs, $\theta_k$ and its **conjugate** $\bar\theta_k = \theta_k^*$, two different generators. The **conjugation** $F \mapsto F^*$ of the algebra is defined by three rules: it exchanges the two members of every pair ($\theta_k^* = \bar\theta_k$, $\bar\theta_k^* = \theta_k$), it replaces every coefficient by its complex conjugate, and it REVERSES the order of every product:

$$
(FG)^* = G^*F^*,\qquad\text{for example}\qquad (\theta_1\theta_2)^* = \theta_2^*\theta_1^* = \bar\theta_2\bar\theta_1 .
$$

Why reverse? With this rule the product of a generator with its conjugate is real: $(\bar\theta\theta)^* = \theta^*\bar\theta^* = \bar\theta\theta$. Without the reversal we would get $\bar\theta^*\theta^* = \theta\bar\theta = -\bar\theta\theta$, and the analogue of $|z|^2 = z^*z$ would not be real. An element with $F^* = F$ is called **real**. Applying the conjugation twice gives back $F$ (the order is reversed twice, the pairs exchanged twice, the coefficients conjugated twice). (PROVED; Notebook 07a checks these rules on the test algebra of the Wolfram verifier and on the 32 generators of a 16-component field, In [9]; they reproduce `Revision/theory/reports/wolfram-field-theory.json`, check `grassmann_algebra_structure`, and `Revision/theory/reports/python-field-theory.json`, check `superalgebra_axioms`.)

**Left and right derivatives.** To vary a Lagrangian we must differentiate with respect to a generator. Because the order matters, there are two derivatives. The **left derivative** $\partial_L F/\partial\theta_k$: in every monomial that contains $\theta_k$, move $\theta_k$ to the far left, collecting a $-1$ for every generator it passes, and then delete it; monomials without $\theta_k$ give nothing. The **right derivative** $\partial_R F/\partial\theta_k$ moves $\theta_k$ to the far right instead. In a sorted monomial of degree $n$ in which $\theta_k$ stands at position $p$ (counting from 0), moving it left passes $p$ generators and moving it right passes $n - 1 - p$. Worked by hand for $F = \theta_0\theta_1$:

$$
\frac{\partial_L F}{\partial\theta_0} = \theta_1,\qquad \frac{\partial_L F}{\partial\theta_1} = -\theta_0,\qquad \frac{\partial_R F}{\partial\theta_1} = \theta_0,\qquad \frac{\partial_R F}{\partial\theta_0} = -\theta_1 .
$$

(The second: write $F = -\theta_1\theta_0$, then delete $\theta_1$. The fourth: $F = -\theta_1\theta_0$ has $\theta_0$ on the right.) For an EVEN monomial the two signs differ by $(-1)^{(n-1-p) - p} = (-1)^{n-1}\cdot(-1)^{-2p} = (-1)^{n-1} = -1$, because $n - 1$ is odd. So $\partial_R F = -\partial_L F$ for every even $F$ (PROVED; Notebook 07a, In [10], also checks the derivative rules of the sympy record and reproduces its check `superalgebra_axioms`).

### 7.12 Bilinear forms, real columns and the powers of $S$

**When is $\Psi^\dagger M\Psi$ real?** Take a column $\Psi$ of $n$ complex Grassmann components with generators $\psi_A = \Psi_A$ and the conjugate row $\Psi^\dagger$ with generators $\chi_A = \psi_A^*$ (the **dagger** $\dagger$ means transpose and conjugate). For a matrix $M$ of ordinary numbers the **bilinear form** $\Psi^\dagger M\Psi = \sum_{A,B}\chi_AM_{AB}\psi_B$ contains one factor from $\Psi^\dagger$ and one from $\Psi$ in every term. Its conjugate, line by line:

$$
\big(\Psi^\dagger M\Psi\big)^* = \sum_{A,B}\big(\chi_AM_{AB}\psi_B\big)^*
$$

(the conjugate of a sum is the sum of the conjugates);

$$
= \sum_{A,B}M_{AB}^*\,\psi_B^*\chi_A^* = \sum_{A,B}M_{AB}^*\,\chi_B\psi_A
$$

(the conjugation reverses the order of the two factors and conjugates the coefficient; then $\psi_B^* = \chi_B$ and $\chi_A^* = \psi_A$);

$$
= \sum_{B,A}\chi_B\,(M^\dagger)_{BA}\,\psi_A = \Psi^\dagger M^\dagger\Psi
$$

(the coefficient is an ordinary number and may stand anywhere; $(M^\dagger)_{BA} = M_{AB}^*$ by the definition of the dagger; the names of the two summation indices are exchanged). So the form is real exactly when $M$ is **Hermitian**, $M^\dagger = M$. For ordinary complex numbers the same result holds for the opposite reason: there nothing is reordered, because ordinary numbers commute. The reversal of the order built into the conjugation is what makes the two cases come out the same (PROVED; Notebook 07a checks it for $n = 4$ with a random Hermitian and a random non-Hermitian matrix, In [11]).

**Real columns keep opposite halves of a matrix.** Now take a REAL column $\Theta = (\theta_0, \dots, \theta_{15})^T$ of 16 real Grassmann generators (no conjugates at all) and the form $\Theta^TM\Theta = \sum_{A,B}\theta_AM_{AB}\theta_B$, where $^T$ is the **transpose** (rows and columns exchanged). Exchanging the two odd factors and renaming the indices, line by line:

$$
\Theta^TM\Theta = \sum_{A,B}\theta_AM_{AB}\theta_B = -\sum_{A,B}\theta_BM_{AB}\theta_A
$$

(the anticommutation of $\theta_A$ and $\theta_B$; for $A = B$ both sides are 0);

$$
= -\sum_{A,B}\theta_A M_{BA}\theta_B = -\sum_{A,B}\theta_A(M^T)_{AB}\theta_B = -\Theta^TM^T\Theta
$$

(the names $A$ and $B$ exchanged; then $(M^T)_{AB} = M_{BA}$). Write $M$ as the sum of its **symmetric part** $\tfrac12(M + M^T)$ and its **antisymmetric part** $\tfrac12(M - M^T)$. The identity says that the symmetric part gives zero. So: **for a real Grassmann column only the antisymmetric part of $M$ survives, and $\Theta^TM\Theta = 0$ for every symmetric $M$.** For a real column $q$ of ordinary numbers it is the other way round: there $q^TMq = q^TM^Tq$ (no sign when the factors are exchanged), so only the symmetric part survives and $q^TMq = 0$ for every antisymmetric $M$ (PROVED).

**The author's matrix $C$.** The author's $16\times16$ matrix $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$ (his $\sigma_{16}$; Chapter 5) is real and symmetric with $C^2 = 1$, and every $C\gamma^{(a)}$ is real and antisymmetric (`Revision/theory/reports/python-field-theory.json`, check `C_properties`). By the rule just proved: for a real Grassmann column $\Theta^TC\Theta = 0$, while every $\Theta^TC\gamma^{(a)}\Theta$ survives; for real ordinary numbers $q^TCq$ survives and every $q^TC\gamma^{(a)}q = 0$. Notebook 07a computes the nine forms with $M = C$ and $M = C\gamma^{(a)}$ for both kinds of numbers and counts the surviving monomials: $[0, 8, 8, 8, 8, 8, 8, 8, 8]$ for real Grassmann numbers and $[8, 0, 0, 0, 0, 0, 0, 0, 0]$ for real ordinary numbers (In [12] and In [13], Figures 07a.4 and 07a.5; the Grassmann statement is part of `Revision/theory/reports/wolfram-field-theory.json`, check `Majorana_Lg_total_derivative_grassmann`, the commuting one part of its check `Majorana_Lg_commuting_control`). Each of the 8 surviving monomials of $\Theta^TC\gamma^{(a)}\Theta$ has the coefficient $\pm2$: every row of the signed permutation matrix $C\gamma^{(a)}$ has one entry $\pm1$, and the two mirror entries $M_{AB} = -M_{BA}$ give $\theta_AM_{AB}\theta_B + \theta_BM_{BA}\theta_A = M_{AB}(\theta_A\theta_B - \theta_B\theta_A) = 2M_{AB}\theta_A\theta_B$.

**The scalar density and its powers.** At one point, the field dirac16complex consists of 16 complex Grassmann numbers: 32 generators $\chi_A = \Psi_A^*$ and $\psi_A = \Psi_A$. The **scalar density** is

$$
S = \Psi^\dagger C\Psi = \sum_{A,B}\chi_AC_{AB}\psi_B .
$$

$C$ is a **signed permutation matrix**: every row and every column has exactly one nonzero entry, $\pm1$ (Chapter 5). If row $A$ has its entry in column $\pi(A)$, then

$$
S = \sum_A C_{A\pi(A)}\,P_A,\qquad P_A = \chi_A\psi_{\pi(A)} ,
$$

a sum of 16 **pairs** that share no generator (different rows give different $\chi$'s, and different columns different $\psi$'s). Each pair is even, so the pairs commute with each other, and $P_A^2 = \chi_A\psi_{\pi(A)}\chi_A\psi_{\pi(A)} = 0$ (the generator $\chi_A$ repeats). Now take the $k$-th power. Multiplying out $S^k = S\cdot S\cdots S$ gives a sum over all ordered choices of $k$ pairs, one from each factor. A choice with a repeated pair gives 0. A choice of $k$ different pairs gives the product of those pairs, and since the pairs commute, all $k!$ orders of the same $k$ pairs give the same product. Each such product is $\pm1$ times one monomial of degree $2k$, and different sets of pairs give different monomials. So

$$
S^k = k!\sum_{\{A_1 < \dots < A_k\}}C_{A_1\pi(A_1)}\cdots C_{A_k\pi(A_k)}\,P_{A_1}\cdots P_{A_k} :
$$

$S^k$ has $\binom{16}{k}$ monomials, each with the coefficient $\pm k!$; $S^{16}$ is a single monomial (all 32 generators), and $S^{17} = 0$, because 17 different pairs do not exist (PROVED; Notebook 07a computes all 17 powers with its program: 16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440, 8008, 4368, 1820, 560, 120, 16, 1, 0 monomials, In [14], Figure 07a.6). Consequence for the Lagrangian: every function of $S$ is a polynomial of degree at most 16, so the potential $U(S) = \frac{\lambda}{2}S^2$ is a choice among finitely many possible terms. For ordinary commuting components the same $S$ has powers that never vanish; there $S^k$ has $\binom{16 + k - 1}{k}$ monomials (the number of ways to choose $k$ of the 16 pairs when a pair may be chosen several times): 16, 136, 816 for $k = 1, 2, 3$ (Notebook 07a checks these three with sympy, In [14]). The difference $136 - 120 = 16$ for $k = 2$ will reappear in Section 7.20: it is the number of squares $P_A^2$ that vanish for Grassmann numbers.

**The test algebra of the Revision record.** The Wolfram verifier of the Revision record does not give every component its own generators. It uses a Grassmann algebra with only two generators $\theta_1, \theta_2$ and their conjugates $\bar\theta_1, \bar\theta_2$, and writes each component as $\Psi_A = c_{A1}\theta_1 + c_{A2}\theta_2$ with ordinary complex coefficients $c_{Ak}$ (which may depend on the coordinates). This keeps the computation small and is still a genuine Grassmann field. Then $\Psi_A^* = c_{A1}^*\bar\theta_1 + c_{A2}^*\bar\theta_2$ (a single generator is not reordered), and

$$
S = \sum_{A,B}\Psi_A^*C_{AB}\Psi_B = \sum_{k,l}\bar\theta_k\theta_l\,\Big(\sum_{A,B}c_{Ak}^*C_{AB}c_{Bl}\Big)
$$

(multiply out and collect by the pair of generators). So $S$ lives on the four monomials $\bar\theta_k\theta_l$ (it is even), $S^2$ only on the one monomial that contains all four generators, and $S^3 = 0$, because it would need six different generators out of four. Hence in this test algebra the most general potential is $U = u_1S + \frac{\lambda}{2}S^2$ (PROVED; Notebook 07a checks it with random coefficients, In [16], and reproduces `Revision/theory/reports/wolfram-field-theory.json`, check `grassmann_algebra_structure`).

### 7.13 Field equations with Grassmann numbers

**Jets.** A field depends on coordinates. To vary a Lagrangian we treat the value of the field and its derivatives at one point as independent symbols; such a set of symbols is called a **jet**. For a Grassmann field each of them is a generator. The **total derivative** $d/dx$ acts on a jet by raising each generator to its derivative ($\theta \to \theta'$, $\theta' \to \theta''$) in each place in turn, with the product rule; $d/dx$ is even (it does not change the number of odd factors), so it needs no extra sign, but the raised generator may have to be sorted back into place.

**The Grassmann oscillator.** Take one complex Grassmann field $\theta(t)$ of one variable $t$ and the Lagrangian

$$
L = \tfrac{i}{2}\big(\bar\theta\theta' - \bar\theta'\theta\big) - \omega\,\bar\theta\theta ,
$$

the Grassmann copy of Example B of Section 7.4 (a prime is $d/dt$). It is real: $(\bar\theta\theta')^* = \theta'^*\bar\theta^* = \bar\theta'\theta$, so the bracket is $X - X^*$ with $X = \bar\theta\theta'$, and $\big(\tfrac{i}{2}(X - X^*)\big)^* = -\tfrac{i}{2}(X^* - X) = \tfrac{i}{2}(X - X^*)$ (the conjugate of $i$ is $-i$); and $(\bar\theta\theta)^* = \bar\theta\theta$. Varying $\bar\theta$ with LEFT derivatives:

$$
\mathcal{E} = \frac{\partial_LL}{\partial\bar\theta} - \frac{d}{dt}\frac{\partial_LL}{\partial\bar\theta'} = \Big(\tfrac{i}{2}\theta' - \omega\theta\Big) - \frac{d}{dt}\Big(-\tfrac{i}{2}\theta\Big) = i\theta' - \omega\theta .
$$

The first term: $\bar\theta$ already stands on the left in $\bar\theta\theta'$ and $\bar\theta\theta$, so deleting it costs no sign. The second: $\bar\theta'$ stands on the left in $-\tfrac{i}{2}\bar\theta'\theta$, its left derivative is $-\tfrac{i}{2}\theta$, whose $d/dt$ is $-\tfrac{i}{2}\theta'$. The field equation $i\theta' = \omega\theta$ has the same form as for an ordinary complex oscillator (PROVED; Notebook 07a, In [17]). Its solution is $\theta(t) = e^{-i\omega t}\theta_0$ with a constant generator $\theta_0$: an ordinary complex function times a fixed generator (In [18], Figure 07a.7). The anticommuting nature sits in $\theta_0$, not in the time dependence. The lesson, used again in Section 7.21: if every conjugate factor is written on the left of every non-conjugate factor, and left derivatives are taken with respect to the conjugates, field equations with Grassmann numbers keep their ordinary form.

**A first-order kinetic term of REAL Grassmann fields gives no equation.** Now two real Grassmann fields $\theta_0(x)$, $\theta_1(x)$ of one coordinate $x$, and the first-order kinetic term with the antisymmetric matrix $A = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}$:

$$
K_A = \theta^TA\,\theta' = \theta_0\theta_1' - \theta_1\theta_0' .
$$

Line by line:

$$
K_A = \theta_0\theta_1' + \theta_0'\theta_1
$$

(in the second term $\theta_1\theta_0' = -\theta_0'\theta_1$, one exchange of two odd factors);

$$
= (\theta_0\theta_1)'
$$

(the product rule read backwards); and $\theta^TA\theta = \theta_0\theta_1 - \theta_1\theta_0 = 2\theta_0\theta_1$, so

$$
K_A = \tfrac12\big(\theta^TA\theta\big)' ,
$$

a **total derivative**. By Section 7.4 it gives no field equation: both Euler-Lagrange expressions vanish identically. With the symmetric identity matrix instead, $K_I = \theta_0\theta_0' + \theta_1\theta_1'$ is not a total derivative ($(\theta_0\theta_0)' = 0$ because $\theta_0^2 = 0$), and its Euler-Lagrange expression for $\theta_0$ is $\theta_0' - \frac{d}{dx}(-\theta_0) = 2\theta_0'$ (the left derivative of $\theta_0\theta_0'$ with respect to $\theta_0'$ passes $\theta_0$, hence the $-\theta_0$). For ORDINARY numbers $q_0, q_1$ the roles are exchanged: $K_A = q_0q_1' - q_1q_0'$ gives the nonzero expressions $E_0 = q_1' - \frac{d}{dx}(-q_1) = 2q_1'$ and $E_1 = -q_0' - \frac{d}{dx}q_0 = -2q_0'$ (PROVED; Notebook 07a, In [19]). This is the one-dimensional model of the negative control of Section 7.28: a real anticommuting field whose kinetic matrices $C\gamma^\mu$ are antisymmetric has no field equation at all. That is why the Lagrangian of dirac16complex is written for a COMPLEX field, with the row $\bar\Psi = \Psi^\dagger C$ in place of a transpose.

### 7.14 Example: Notebook 07a builds a Grassmann algebra by hand

Notebook 07a builds the algebra of Sections 7.10 to 7.13 from nothing but its rules, in a few lines of plain Python: a sorting function that returns the sign of a reordering, a faster sign rule for the product of two sorted monomials, and a class `Grassmann` whose elements are dictionaries from monomials to coefficients. It checks the defining rules and the product of two general elements, counts the $2^n$ monomials, draws the multiplication table of three generators and the commutation signs $(-1)^{kl}$, builds the conjugation and the two derivatives, checks the reality rule for bilinear forms, shows with the author's matrix $C$ (read from the Revision record) which bilinear forms survive for real columns of the two kinds of numbers, computes all powers of the scalar density of a 16-component field up to $S^{17} = 0$, checks the test algebra of the Wolfram verifier, derives the Grassmann oscillator and shows that the first-order kinetic term of real Grassmann fields is a total derivative. It draws seven figures and ends with the line ALL 38 CHECKS PASSED (notebook 07a).

<!-- NOTEBOOK 07a -->

### 7.17 Line-by-line walk-through of Notebook 07a

The notebook has 20 code cells, In [1] to In [20]. This section explains every line of every one of them, with the conventions of Section 7.9 (comments, docstrings, and `...)` for the rest of a long caption, which is printed in full under its figure in Section 7.16).

**In [1], the set-up cell.** It is the set-up cell of Notebook 07d with one difference: the line `NOTEBOOK_ID = "07a"`. Its first part repeats the complete run instructions of Section 7.15 as comment lines; its code is explained line by line in Section 7.9. **Out [1]:** `Set-up of notebook 07a complete: repository folder found, helpers defined.`

**In [2]: the sign of a reordering.**

```python
import contextlib  # redirect printed text into a buffer
import io  # an in-memory text file (the buffer)
import math  # factorials and binomial coefficients
from bisect import bisect_right  # counts the entries of a sorted tuple that are <= y
from collections import Counter  # counts how often each value occurs

import numpy as np  # arrays of numbers
import sympy as sp  # exact algebra with symbols
```

The modules used by the notebook: `contextlib` and `io` for the combined printing of a PASS line (explained below), `math` for factorials and binomial coefficients, `bisect_right` from the module `bisect` (it finds how many entries of a sorted tuple are at most a given number), `Counter` from `collections` (it counts how often each value occurs), numpy and sympy.

```python
check_of_the_setup = check  # the helper check of the set-up cell


def check(condition, name, record=None):
    """The set-up cell's check, with its PASS line and its "reproduces" line
    printed by ONE print call, so that Jupyter delivers them together."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # collect what check prints
        check_of_the_setup(condition, name, record)
    print(buffer.getvalue(), end="")  # and print it in one piece
```

The same wrapper of `check` as in Notebook 07d (Section 7.9, In [2]): the set-up cell's check runs while its printed text is collected in `buffer`, and the collected text is then printed in one piece, so that a PASS line and its "reproduces" line reach the book's tools together.

```python
def sort_with_sign(generators):
    """Sort generator numbers by exchanging neighbours (bubble sort).
    Return (sign, sorted tuple): sign = +1 or -1 for an even or odd number of
    exchanges, and sign = 0 if a generator occurs twice (the product is zero)."""
    items = list(generators)  # a copy that we may reorder
    sign = 1
    for end in range(len(items) - 1, 0, -1):  # pass over items[0 .. end]
        for i in range(end):  # every neighbour pair of this pass
            if items[i] > items[i + 1]:  # a pair in the wrong order:
                items[i], items[i + 1] = items[i + 1], items[i]  # exchange it,
                sign = -sign  # which costs one factor -1
    if any(items[i] == items[i + 1] for i in range(len(items) - 1)):
        return 0, tuple(items)  # a repeated generator: theta_i theta_i = 0
    return sign, tuple(items)
```

`sort_with_sign(generators)` sorts a list of generator numbers by the method called **bubble sort** and counts the exchanges. `items` is a copy of the input that may be reordered, and `sign` starts at $+1$. The outer loop makes passes over shorter and shorter beginnings of the list (`range(len(items) - 1, 0, -1)` counts down from the last position to 1); in each pass the inner loop looks at every neighbour pair, and when a pair stands in the wrong order it is exchanged (`items[i], items[i + 1] = items[i + 1], items[i]` swaps two entries in one line) and the sign is reversed. After a pass the largest remaining number has bubbled to the end, so the list is sorted after the last pass. If two equal neighbours remain, a generator occurs twice and the function returns the sign 0 (the product contains $\theta_i\theta_i = 0$); otherwise it returns the sign and the sorted tuple.

```python
for example in [(0, 1), (1, 0), (2, 0, 1), (2, 1, 0), (0, 0), (3, 1, 2, 0)]:
    sign, ordered = sort_with_sign(example)
    say(f"generators {example} -> sign {sign:+d}, sorted {ordered}")
check(sort_with_sign((1, 0)) == (-1, (0, 1)), "theta_1 theta_0 = -theta_0 theta_1")
check(sort_with_sign((2, 0, 1)) == (1, (0, 1, 2)),
      "theta_2 theta_0 theta_1 = +theta_0 theta_1 theta_2 (two exchanges)")
check(sort_with_sign((0, 0))[0] == 0, "theta_0 theta_0 = 0")
```

Six examples are sorted and printed (`{sign:+d}` prints a whole number with its sign). The three checks are the examples of Section 7.10: one exchange for $\theta_1\theta_0$, two for $\theta_2\theta_0\theta_1$, and 0 for $\theta_0\theta_0$. **Out [2]:** six lines such as `generators (2, 0, 1) -> sign +1, sorted (0, 1, 2)` and `generators (3, 1, 2, 0) -> sign -1, sorted (0, 1, 2, 3)` (five exchanges), and three PASS lines.

**In [3]: a faster sign rule.**

```python
def shuffle_sign(left, right):
    """The sign of the product of the sorted monomials left and right: 0 if they
    share a generator, otherwise (-1)**N with N the number of pairs (x in left,
    y in right) with x > y, which is the number of neighbour exchanges needed."""
    if set(left) & set(right):  # a common generator: the product holds theta^2
        return 0
    # len(left) - bisect_right(left, y) entries of left are larger than y
    pairs = sum(len(left) - bisect_right(left, y) for y in right)
    return -1 if pairs % 2 else 1
```

`shuffle_sign(left, right)` gives the sign of the product of two monomials that are already sorted. `set(left) & set(right)` is the set of the generators that both contain; if it is not empty, the product holds a square and the sign is 0. Otherwise, placing `left` before `right`, each pair ($x$ from the left, $y$ from the right) with $x > y$ stands in the wrong order and needs exactly one exchange, and no other pair does. For each $y$ of the right factor, `bisect_right(left, y)` is the number of entries of `left` that are at most $y$, so `len(left) - bisect_right(left, y)` is the number larger than $y$. Their total `pairs` decides the sign: $-1$ if it is odd (`pairs % 2` is the remainder after division by 2), $+1$ if even.

```python
rng = np.random.default_rng(12345)  # random numbers with a fixed seed: same every run
agree = 0
for trial in range(2000):
    # two random sorted monomials with generators from 0 .. 9
    left = tuple(sorted(rng.choice(10, size=rng.integers(0, 5), replace=False)))
    right = tuple(sorted(rng.choice(10, size=rng.integers(0, 5), replace=False)))
    agree += shuffle_sign(left, right) == sort_with_sign(left + right)[0]
report("random pairs of monomials on which the two sign rules agree", f"{agree} of 2000")
check(agree == 2000, "shuffle_sign equals sort_with_sign on 2000 random pairs")
```

A random-number generator with the fixed seed 12345. In each of 2000 trials two random sorted monomials are drawn: `rng.integers(0, 5)` is a random degree from 0 to 4 and `rng.choice(10, size=..., replace=False)` that many different generators out of 0 to 9; `sorted` and `tuple` put them in increasing order. `agree` counts the trials in which the fast rule gives the same sign as sorting the joined list (`left + right` joins two tuples; a true comparison counts as 1). **Out [3]:** `RESULT random pairs of monomials on which the two sign rules agree = 2000 of 2000` and the PASS line.

**In [4]: the algebra itself.**

```python
class Grassmann:
    """An element of a Grassmann algebra: self.terms maps every monomial (a sorted
    tuple of generator numbers; () is the number 1) to its coefficient."""

    def __init__(self, terms=None):
        self.terms = {}
        for monomial, coefficient in (terms or {}).items():
            self.add(monomial, coefficient)
```

A **class** is a recipe for a new kind of object. Every object of the class `Grassmann` holds a dictionary `self.terms` from monomials (sorted tuples; `()` is the number 1) to coefficients. `__init__` is the function that runs when an object is made: it starts with an empty dictionary and adds the given terms one by one (`terms or {}` uses an empty dictionary when none is given).

```python
    def add(self, monomial, coefficient):
        """Add coefficient times monomial to this element (in place)."""
        total = self.terms.get(monomial, 0) + coefficient
        if isinstance(total, sp.Basic):  # an exact sympy number or expression:
            total = sp.expand(total)  # multiply out, so that equal terms cancel
        if total == 0:
            self.terms.pop(monomial, None)  # a zero coefficient is not stored
        else:
            self.terms[monomial] = total
```

`add` adds a coefficient times a monomial to the object itself. `self.terms.get(monomial, 0)` is the stored coefficient or 0. If the sum is an exact sympy expression (`isinstance(total, sp.Basic)`), it is multiplied out with `sp.expand`, so that terms that are equal also look equal and cancel. A coefficient that has become zero is removed (`pop(monomial, None)` removes the key if it is there), so an element is zero exactly when its dictionary is empty.

```python
    def __add__(self, other):  # self + other
        result = Grassmann(self.terms)
        for monomial, coefficient in other.terms.items():
            result.add(monomial, coefficient)
        return result

    def scaled(self, factor):  # factor * self, factor an ordinary number
        return Grassmann({m: factor * c for m, c in self.terms.items()})

    def __sub__(self, other):  # self - other
        return self + other.scaled(-1)
```

`__add__` defines what `+` does for two elements: a copy of the first with every term of the second added. `scaled(factor)` multiplies every coefficient by an ordinary number. `__sub__` defines `-` as adding the second element multiplied by $-1$.

```python
    def __mul__(self, other):  # self * other: every term times every term
        result = Grassmann()
        for left, a in self.terms.items():
            for right, b in other.terms.items():
                sign = shuffle_sign(left, right)
                if sign != 0:
                    result.add(tuple(sorted(left + right)), sign * a * b)
        return result

    def is_zero(self):
        return not self.terms  # True when no monomial is left
```

`__mul__` defines `*`: every term of the first element times every term of the second. For two monomials `left` and `right` the sign comes from `shuffle_sign`; if it is not 0, the joined and sorted monomial gets the product of the two coefficients times the sign. `is_zero` is true when no monomial is left.

```python
def number(value):
    """The ordinary number value as an element of the algebra."""
    return Grassmann({(): value})


def theta(i):
    """The generator number i."""
    return Grassmann({(i,): 1})


say("The class Grassmann and the helpers number and theta are defined.")
```

Two helpers: `number(value)` is an ordinary number as an element (the monomial `()` with that coefficient), and `theta(i)` is the generator number `i` (the monomial `(i,)` with coefficient 1; the comma makes a tuple of one entry). **Out [4]:** `The class Grassmann and the helpers number and theta are defined.`

**In [5]: the defining rules and a product worked by hand.**

```python
t0, t1, t2 = theta(0), theta(1), theta(2)
check((t0 * t1 + t1 * t0).is_zero(), "theta_0 theta_1 + theta_1 theta_0 = 0")
check((t0 * t0).is_zero() and (t2 * t2).is_zero(), "a generator squares to zero")
odd = t0.scaled(3) + t1.scaled(5)  # the odd element 3 theta_0 + 5 theta_1
check((odd * odd).is_zero(), "(3 theta_0 + 5 theta_1)^2 = 0")
```

`t0`, `t1`, `t2` are the generators $\theta_0, \theta_1, \theta_2$. The three checks: $\theta_0\theta_1 + \theta_1\theta_0 = 0$; $\theta_0^2 = \theta_2^2 = 0$; and $(3\theta_0 + 5\theta_1)^2 = 0$ (Section 7.11).

```python
a, b, c, d, a2, b2, c2, d2 = sp.symbols("a b c d a2 b2 c2 d2")  # 8 ordinary numbers
F = number(a) + t0.scaled(b) + t1.scaled(c) + (t0 * t1).scaled(d)
F2 = number(a2) + t0.scaled(b2) + t1.scaled(c2) + (t0 * t1).scaled(d2)
by_hand = {(): a * a2, (0,): a * b2 + b * a2, (1,): a * c2 + c * a2,
           (0, 1): a * d2 + d * a2 + b * c2 - c * b2}
product = F * F2
same = sorted(product.terms) == sorted(by_hand) and all(
    sp.expand(product.terms[key] - value) == 0 for key, value in by_hand.items())
say(f"coefficient of theta_0 theta_1 in F F': {product.terms[(0, 1)]}")
check(same, "the product of two general elements of a 2-generator algebra")
```

Eight ordinary sympy symbols for the coefficients of $F$ and $F'$ (the primes are written a2, b2, c2, d2). `F` and `F2` are the two general elements of Section 7.10, `by_hand` the dictionary of the product worked out there. `same` is true when the computed product has exactly the same monomials (`sorted(product.terms)` lists them in order) and every coefficient agrees after multiplying out. **Out [5]:** four PASS lines and the coefficient `a*d2 + a2*d + b*c2 - b2*c` of $\theta_0\theta_1$, with the minus sign of the exchange.

**In [6]: the dimension, and Figure 07a.1.**

```python
sizes = []  # the number of monomials for n = 0, 1, ..., 12
for n in range(13):
    everything = number(1)
    for i in range(n):
        everything = everything * (number(1) + theta(i))  # (1 + theta_i)
    sizes.append(len(everything.terms))
    if n == 8:
        degrees8 = Counter(len(monomial) for monomial in everything.terms)
        ones8 = all(value == 1 for value in everything.terms.values())
report("number of monomials for n = 12 generators", sizes[12])
check(sizes == [2 ** n for n in range(13)], "a Grassmann algebra with n generators "
      "has 2^n monomials (n = 0 to 12)")
check(ones8 and all(degrees8[k] == math.comb(8, k) for k in range(9)),
      "for n = 8 there are binom(8, k) monomials of degree k, each coefficient +1")
```

For $n = 0$ to 12 the product $(1 + \theta_0)\cdots(1 + \theta_{n-1})$ is computed, starting from the number 1, and the number of its monomials is stored. For $n = 8$, `Counter(len(monomial) ...)` counts the monomials of each degree and `ones8` records whether every coefficient is $+1$. The first check compares the counts with $2^n$, the second the degrees with `math.comb(8, k)` $= \binom{8}{k}$. **Out [6]:** `RESULT number of monomials for n = 12 generators = 4096` and two PASS lines.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
left.semilogy(range(13), sizes, "o", label="counted by the program")
left.semilogy(range(13), [2 ** n for n in range(13)], "-", label="$2^n$")
left.set_xlabel("number of generators $n$")
left.set_ylabel("number of monomials")
left.set_title("Dimension of the algebra")
left.legend()
right.bar(range(9), [degrees8[k] for k in range(9)], color="tab:orange")
right.set_xlabel("degree $k$ (generators in the monomial)")
right.set_ylabel("number of monomials")
right.set_title("Degrees for $n = 8$: $\\binom{8}{k}$")
fig.tight_layout()
save_figure(fig, "dimension_and_degrees",
...)
```

Left: the counts as dots and $2^n$ as a line on a logarithmic vertical axis (`semilogy`). Right: a bar chart (`bar`) of the number of monomials of each degree for $n = 8$. **What Figure 07a.1 shows.** On the logarithmic axis $2^n$ is a straight line and the dots lie on it: each new generator doubles the algebra. The bars are the binomial coefficients 1, 8, 28, 56, 70, 56, 28, 8, 1, symmetric around degree 4.

**In [7]: the multiplication table, and Figure 07a.2.**

```python
basis3 = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
names3 = ["$1$"] + ["$" + "".join(f"\\theta_{i}" for i in m) + "$" for m in basis3[1:]]
table = np.array([[shuffle_sign(row, column) for column in basis3] for row in basis3])
nonzero = int(np.count_nonzero(table))
report("nonzero products among the 64 products of the 8 monomials", nonzero)
check(nonzero == 27, "27 = 3^3 of the 64 products of monomials of 3 generators are "
      "nonzero")
check(np.array_equal(table[1:4, 1:4], -table[1:4, 1:4].T),
      "the table of the three generators is antisymmetric")
```

`basis3` lists the eight monomials of three generators, `names3` their labels for the plot (`"".join(...)` joins the texts $\theta_i$ of one monomial; a doubled backslash in a Python string is one backslash for LaTeX). `table` is the $8\times8$ array of the signs of all products, row = left factor, column = right factor. `np.count_nonzero` counts the nonzero entries. The first check requires 27; the second checks that the block of the three single generators (rows and columns 1 to 3; `table[1:4, 1:4]`) is antisymmetric. **Out [7]:** `RESULT nonzero products among the 64 products of the 8 monomials = 27` and two PASS lines.

```python
fig, ax = plt.subplots(figsize=(6.4, 5.4))
image = ax.imshow(table, cmap="coolwarm", vmin=-1, vmax=1)
for i in range(8):
    for j in range(8):
        ax.text(j, i, {1: "+", -1: "-", 0: "0"}[int(table[i, j])], ha="center",
                va="center", fontsize=12)
ax.set_xticks(range(8), names3, rotation=45)
ax.set_yticks(range(8), names3)
ax.set_xlabel("right factor")
ax.set_ylabel("left factor")
ax.set_title("Sign of (left factor) times (right factor)")
ax.grid(False)
fig.colorbar(image, ax=ax, ticks=[-1, 0, 1], shrink=0.8)
save_figure(fig, "multiplication_signs",
...)
```

`imshow` draws the table as a **heat map**, one coloured square per entry (red $+1$, blue $-1$, grey 0), and the two loops write $+$, $-$ or 0 into each square (`ha` and `va` centre the text). The ticks carry the monomial names, rotated by 45 degrees under the horizontal axis. **What Figure 07a.2 shows.** The first row and column (the factor 1) are all $+$; every product with a shared generator is grey; the $3\times3$ block of single generators has $+$ above and $-$ below the grey diagonal: $\theta_i\theta_j = -\theta_j\theta_i$.

**In [8]: even and odd, and Figure 07a.3.**

```python
signs = np.zeros((5, 5), dtype=int)
for k in range(5):
    for l in range(5):
        X = number(1)
        for i in range(k):
            X = X * theta(i)  # theta_0 ... theta_(k-1)
        Y = number(1)
        for i in range(l):
            Y = Y * theta(5 + i)  # theta_5 ... theta_(4+l)
        XY, YX = X * Y, Y * X
        (monomial, value), = XY.terms.items()  # XY is one monomial
        signs[k, l] = YX.terms[monomial] // value  # +1 or -1
expected = np.array([[(-1) ** (k * l) for l in range(5)] for k in range(5)])
check(np.array_equal(signs, expected), "YX = (-1)^(k l) XY for degrees k, l = 0 .. 4")
```

For degrees $k, l = 0$ to 4, `X` is the monomial $\theta_0\cdots\theta_{k-1}$ and `Y` the monomial $\theta_5\cdots\theta_{4+l}$ (no common generator). Both products `X * Y` and `Y * X` are formed. `(monomial, value), = XY.terms.items()` unpacks the single term of `XY` (the trailing comma says "exactly one item"), and the sign is the coefficient of the same monomial in `YX` divided by `value` (`//` divides whole numbers). The check compares the table of signs with $(-1)^{kl}$. **Out [8]:** one PASS line.

```python
fig, ax = plt.subplots(figsize=(5.6, 4.6))
image = ax.imshow(signs, cmap="coolwarm", vmin=-1, vmax=1)
for k in range(5):
    for l in range(5):
        ax.text(l, k, f"{signs[k, l]:+d}", ha="center", va="center", fontsize=12)
ax.set_xticks(range(5))
ax.set_yticks(range(5))
ax.set_xlabel("degree $l$ of $Y$")
ax.set_ylabel("degree $k$ of $X$")
ax.set_title("$YX = (\\pm 1)\\, XY$")
ax.grid(False)
fig.colorbar(image, ax=ax, ticks=[-1, 1], shrink=0.8)
save_figure(fig, "commutation_signs",
...)
```

A heat map of the $5\times5$ signs with the numbers written in. **What Figure 07a.3 shows.** Only the squares where both degrees are odd (1 and 3) are blue: two odd monomials anticommute. Every row and column of even degree is red: an even monomial commutes with everything.

**In [9]: the conjugation.**

```python
def reproduces(report, name):
    """The text "<report>, check <name>" for a PASS line, after making sure that
    the Revision report (a JSON file) contains the check name with verdict PASS."""
    data = json.loads(repository_file(report).read_text(encoding="utf-8"))
    found = [item for item in data["checks"] if item["name"] == name]
    if len(found) != 1 or found[0]["verdict"].upper() != "PASS":
        raise ValueError(f"{name} is not a passing check of {report}")
    return f"{report}, check {name}"


WLREP = "Revision/theory/reports/wolfram-field-theory.json"
PYREP = "Revision/theory/reports/python-field-theory.json"
```

`reproduces(report, name)` reads a Revision report, makes sure that it holds exactly one check of that name with the verdict PASS, and returns the text that a PASS line prints after "reproduces" (the same helper as in Notebook 07d). `WLREP` and `PYREP` are the paths of the Wolfram and the sympy field-theory reports.

```python
def conjugate(element, partner):
    """The conjugate of element: generator g -> partner[g], the order of every
    product reversed, every coefficient complex-conjugated."""
    result = Grassmann()
    for monomial, coefficient in element.terms.items():
        images = [partner[g] for g in reversed(monomial)]  # reversed order
        sign, ordered = sort_with_sign(images)  # back to increasing order
        if sign != 0:
            result.add(ordered, sign * sp.conjugate(coefficient))
    return result
```

`conjugate(element, partner)` implements the three rules of Section 7.11. For every term, `reversed(monomial)` runs through the generators in reverse order and `partner[g]` replaces each by its partner; `sort_with_sign` sorts the result back and gives its sign; the coefficient is conjugated with `sp.conjugate`.

```python
# the Wolfram test algebra: 0 = theta_1, 1 = theta_2, 2 = thetabar_1, 3 = thetabar_2
PAIR4 = [2, 3, 0, 1]
th1, th2, tb1, tb2 = theta(0), theta(1), theta(2), theta(3)
general = (number(sp.Rational(1, 2) + 2 * sp.I) + th1.scaled(3 - sp.I)
           + (th2 * tb1).scaled(-4 * sp.I) + (th1 * th2 * tb2).scaled(7))
check((th1 * th2 + th2 * th1).is_zero() and (th1 * th1).is_zero()
      and (conjugate(th1 * th2, PAIR4) - tb2 * tb1).is_zero()
      and (conjugate(conjugate(general, PAIR4), PAIR4) - general).is_zero(),
      "anticommutation, theta^2 = 0, (theta_1 theta_2)* = thetabar_2 thetabar_1, "
      "(F*)* = F",
      record=reproduces(WLREP, "grassmann_algebra_structure"))
```

The test algebra of the Wolfram verifier: generators 0 and 1 are $\theta_1, \theta_2$ and 2 and 3 are $\bar\theta_1, \bar\theta_2$, so the list `PAIR4 = [2, 3, 0, 1]` gives each generator its partner. `general` is an element with complex coefficients ($\tfrac12 + 2i$, $3 - i$, $-4i$, 7; `sp.Rational(1, 2)` is the exact fraction $\tfrac12$). The check combines four statements with `and`: anticommutation, $\theta_1^2 = 0$, $(\theta_1\theta_2)^* = \bar\theta_2\bar\theta_1$, and $(F^*)^* = F$.

```python
# the jet super-algebra of the sympy record: psi_A = generator A, chi_A = 16 + A
PAIR32 = [16 + A for A in range(16)] + list(range(16))
psi = [theta(A) for A in range(16)]
chi = [theta(16 + A) for A in range(16)]
rules = ((psi[0] * psi[0]).is_zero() and (psi[0] * psi[1] + psi[1] * psi[0]).is_zero()
         and (conjugate(chi[0] * psi[1], PAIR32) - chi[1] * psi[0]).is_zero()
         and (conjugate((chi[0] * psi[0]).scaled(sp.I), PAIR32)
              + (chi[0] * psi[0]).scaled(sp.I)).is_zero())
check(rules, "psi psi = 0, psi_A psi_B = -psi_B psi_A, (chi_A psi_B)* = chi_B "
      "psi_A, (i chi_A psi_A)* = -i chi_A psi_A",
      record=reproduces(PYREP, "superalgebra_axioms"))
check((conjugate(chi[3] * psi[3], PAIR32) - chi[3] * psi[3]).is_zero(),
      "chi_A psi_A (a component times its conjugate) is real")
```

The jet algebra of the sympy record for one point of a 16-component field: $\psi_A$ is generator $A$ (0 to 15) and $\chi_A = \psi_A^*$ is generator $16 + A$, so `PAIR32` sends $A$ to $16 + A$ and back. `rules` combines the four rules of the record's check `superalgebra_axioms`: $\psi\psi = 0$, $\psi_A\psi_B = -\psi_B\psi_A$, $(\chi_A\psi_B)^* = \chi_B\psi_A$ (order reversal) and $(i\chi_A\psi_A)^* = -i\chi_A\psi_A$. The last check: $\chi_A\psi_A$ is real. **Out [9]:** three PASS lines; the first two each followed by a "reproduces" line naming `wolfram-field-theory.json`, check `grassmann_algebra_structure`, and `python-field-theory.json`, check `superalgebra_axioms`.

**In [10]: left and right derivatives.**

```python
def left_derivative(element, k):
    """d_L element / d theta_k: move theta_k to the far left, then delete it."""
    result = Grassmann()
    for monomial, coefficient in element.terms.items():
        if k in monomial:
            p = monomial.index(k)  # the number of generators to its left
            result.add(monomial[:p] + monomial[p + 1:], (-1) ** p * coefficient)
    return result


def right_derivative(element, k):
    """d_R element / d theta_k: move theta_k to the far right, then delete it."""
    result = Grassmann()
    for monomial, coefficient in element.terms.items():
        if k in monomial:
            p = monomial.index(k)
            passed = len(monomial) - 1 - p  # generators to its right
            result.add(monomial[:p] + monomial[p + 1:], (-1) ** passed * coefficient)
    return result
```

`left_derivative(element, k)`: for every monomial that contains generator `k`, `monomial.index(k)` is its position `p`, which is the number of generators to its left; the generator is deleted (`monomial[:p] + monomial[p + 1:]` joins the parts before and after it) and the coefficient multiplied by $(-1)^p$. `right_derivative` does the same with the number of generators to its right, `len(monomial) - 1 - p`.

```python
F = t0 * t1
check((left_derivative(F, 0) - t1).is_zero() and (left_derivative(F, 1) + t0).is_zero()
      and (right_derivative(F, 1) - t0).is_zero()
      and (right_derivative(F, 0) + t1).is_zero(),
      "the four derivatives of theta_0 theta_1 worked by hand")
even = Grassmann()
for trial in range(40):  # a random even element of the algebra of 8 generators
    size = 2 * int(rng.integers(1, 4))  # degree 2, 4 or 6
    monomial = tuple(sorted(rng.choice(8, size=size, replace=False)))
    even.add(monomial, int(rng.integers(-9, 10)))
check(all((right_derivative(even, k) + left_derivative(even, k)).is_zero()
          for k in range(8)), "d_R F = -d_L F for a random even element F")
```

The four derivatives of $\theta_0\theta_1$ worked by hand in Section 7.11 are checked. Then a random even element of the algebra of 8 generators is built from 40 random monomials of degree 2, 4 or 6 (`2 * int(rng.integers(1, 4))`) with random whole coefficients from $-9$ to 9 (`rng.integers(-9, 10)`; a repeated monomial simply adds up); the check requires $\partial_R F = -\partial_L F$ for all 8 generators.

```python
x, a_, y = chi[0], psi[0], psi[1]  # x = chi_0 (generator 16), a = psi_0, y = psi_1
p_, q_ = x * a_ * y, x * a_
rules = ((left_derivative(p_, 1) - x * a_).is_zero()
         and (right_derivative(p_, 1) - x * a_).is_zero()
         and (left_derivative(p_, 0) + x * y).is_zero()
         and (right_derivative(p_, 0) + x * y).is_zero()
         and (left_derivative(q_, 0) + x).is_zero()
         and (right_derivative(q_, 0) - x).is_zero())
check(rules, "left and right derivatives with the Grassmann signs",
      record=reproduces(PYREP, "superalgebra_axioms"))
```

The derivative rules of the sympy record, with $x = \chi_0$, $a = \psi_0$, $y = \psi_1$ and $p = xay$, $q = xa$: $\partial_Lp/\partial y = \partial_Rp/\partial y = xa$, $\partial_Lp/\partial a = \partial_Rp/\partial a = -xy$, $\partial_Lq/\partial a = -x$ and $\partial_Rq/\partial a = +x$ (generators 1 and 0 are $y$ and $a$). **Out [10]:** three PASS lines, the last with its "reproduces" line.

**In [11]: when is a bilinear form real?**

```python
def bilinear(row, M, column):
    """sum over A, B of row[A] M[A, B] column[B] (one factor from each side)."""
    total = Grassmann()
    for A in range(len(row)):
        for B in range(len(column)):
            if M[A, B] != 0:
                total = total + (row[A] * column[B]).scaled(M[A, B])
    return total
```

`bilinear(row, M, column)` forms $\sum_{A,B}\mathrm{row}_AM_{AB}\mathrm{column}_B$, skipping the zero entries of $M$.

```python
n4 = 4
psi4 = [theta(A) for A in range(n4)]  # psi_A: generators 0 .. 3
chi4 = [theta(n4 + A) for A in range(n4)]  # chi_A = psi_A*: generators 4 .. 7
PAIR8 = [n4 + A for A in range(n4)] + list(range(n4))
random_matrix = sp.Matrix(n4, n4, lambda i, j: int(rng.integers(-3, 4))
                          + sp.I * int(rng.integers(-3, 4)))
hermitian = random_matrix + random_matrix.H  # M + M^dagger is Hermitian
form_h = bilinear(chi4, hermitian, psi4)
form_n = bilinear(chi4, random_matrix, psi4)
check((conjugate(form_h, PAIR8) - form_h).is_zero(),
      "Psi^dagger M Psi is real for a Hermitian M")
not_hermitian = random_matrix.H != random_matrix  # True: M^dagger differs from M
check(not_hermitian and not (conjugate(form_n, PAIR8) - form_n).is_zero(),
      "Psi^dagger M Psi is not real for a non-Hermitian M")
```

$n = 4$: the $\psi_A$ are generators 0 to 3, the $\chi_A$ generators 4 to 7, and `PAIR8` pairs them. `random_matrix` is a $4\times4$ sympy matrix with random **Gaussian integers** (whole numbers $a + bi$ with $a, b$ from $-3$ to 3; the `lambda i, j: ...` is a small unnamed function that gives the entry in row `i` and column `j`). `random_matrix.H` is its conjugate transpose $M^\dagger$, so `hermitian` $= M + M^\dagger$ is Hermitian. The first check: $\Psi^\dagger M\Psi$ with the Hermitian matrix equals its conjugate. The second: the random matrix is not Hermitian, and its form is not real. **Out [11]:** two PASS lines.

**In [12]: the author's $C$ and the real columns.**

```python
gammas_file = "Revision/algebra/gammas.json"
fixture = json.loads(repository_file(gammas_file).read_text(encoding="utf-8"))
G = [np.array(g, dtype=int) for g in fixture["gamma"]]  # gamma^(x1) .. gamma^(x8)
C = np.array(fixture["C"], dtype=int)  # C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)
check(np.array_equal(C, G[7] @ G[0] @ G[1] @ G[2]), "C = gamma^(x8) gamma^(x1) "
      "gamma^(x2) gamma^(x3) (read from Revision/algebra/gammas.json)")
check(np.array_equal(C.T, C) and np.array_equal(C @ C, np.eye(16, dtype=int))
      and all(np.array_equal((C @ g).T, -(C @ g)) for g in G),
      "C is symmetric, C^2 = 1, and every C gamma^(a) is antisymmetric",
      record=reproduces(PYREP, "C_properties"))
```

The notebook reads the Revision record `Revision/algebra/gammas.json`: `G` holds the eight gammas $\gamma^{(x_1)}, \dots, \gamma^{(x_8)}$ as integer arrays (`G[0]` is $\gamma^{(x_1)}$, `G[7]` is $\gamma^{(x_8)}$) and `C` the matrix $C$. The first check recomputes $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$ (`@` is the matrix product of numpy). The second checks that $C$ is symmetric (`C.T` is the transpose), $C^2 = 1$ (`np.eye(16)` is the identity), and every $C\gamma^{(a)}$ is antisymmetric; it names the record's check `C_properties`.

```python
Theta = [theta(A) for A in range(16)]  # a real Grassmann column
q = sp.Matrix(sp.symbols("q0:16"))  # a real column of ordinary numbers
labels = ["$C$"] + [f"$C\\gamma^{{(x_{a + 1})}}$" for a in range(8)]
matrices = [sp.Matrix(C)] + [sp.Matrix(C @ g) for g in G]  # exact sympy matrices
grassmann_counts, commuting_counts = [], []
for M in matrices:
    grassmann_counts.append(len(bilinear(Theta, M, Theta).terms))
    form = sp.expand((q.T * M * q)[0, 0])
    commuting_counts.append(0 if form == 0 else len(sp.Add.make_args(form)))
say(f"monomials, real Grassmann: {grassmann_counts}")
say(f"monomials, real commuting: {commuting_counts}")
```

`Theta` is a real Grassmann column of 16 generators, `q` a column of 16 ordinary sympy symbols. `labels` are the plot labels of the nine matrices (in an f-string a doubled brace `{{` prints one brace). `matrices` holds $C$ and the eight $C\gamma^{(a)}$ as exact sympy matrices. For each, the number of surviving monomials is counted: for Grassmann numbers with the class `Grassmann`, for ordinary numbers by expanding the sympy expression $q^TMq$ and counting its terms (`sp.Add.make_args` splits a sum into its terms; a zero form has no terms). **Out [12]:** two PASS lines (the second followed by its "reproduces" line, which names the check `C_properties`), and `monomials, real Grassmann: [0, 8, 8, 8, 8, 8, 8, 8, 8]`, `monomials, real commuting: [8, 0, 0, 0, 0, 0, 0, 0, 0]`.

**In [13]: the pattern and its figures.**

```python
two = all(abs(value) == 2 for M in matrices[1:]
          for value in bilinear(Theta, M, Theta).terms.values())
check(grassmann_counts == [0] + [8] * 8 and two, "real Grassmann: Theta^T C Theta "
      "= 0; each Theta^T C gamma^(a) Theta has 8 monomials with coefficients +-2",
      record=reproduces(WLREP, "Majorana_Lg_total_derivative_grassmann"))
check(commuting_counts == [8] + [0] * 8, "real commuting: q^T C q has 8 monomials, "
      "every q^T C gamma^(a) q is 0",
      record=reproduces(WLREP, "Majorana_Lg_commuting_control"))
```

`two` is true when every coefficient of every surviving Grassmann form is $\pm2$. The first check requires the counts $[0, 8, \dots, 8]$ and the coefficients $\pm2$ and names the Wolfram check `Majorana_Lg_total_derivative_grassmann`, of which this is the part about the bilinear forms; the second requires the commuting counts $[8, 0, \dots, 0]$ and names the Wolfram check `Majorana_Lg_commuting_control`. **Out [13]:** two PASS lines with their "reproduces" lines, and two figures.

```python
fig, ax = plt.subplots(figsize=(8.4, 4.0))
positions = np.arange(len(labels))
ax.bar(positions - 0.2, grassmann_counts, width=0.4, label="real Grassmann column")
ax.bar(positions + 0.2, commuting_counts, width=0.4, label="real ordinary numbers")
ax.set_xticks(positions, labels)
ax.set_ylabel("surviving monomials")
ax.set_ylim(0, 10.5)  # room for the legend above the bars
ax.set_title("Which bilinear forms survive for a real column")
ax.legend(loc="upper center", ncol=2)
save_figure(fig, "bilinear_survivors",
...)
```

Two bars per matrix, shifted left and right by 0.2 (`positions - 0.2`, `positions + 0.2`), for the two kinds of numbers. **What Figure 07a.4 shows.** The blue bars (real Grassmann columns) are zero for $C$ and 8 for every $C\gamma^{(a)}$; the orange bars (real ordinary numbers) are 8 for $C$ and zero for every $C\gamma^{(a)}$. The two kinds of numbers keep opposite halves of a matrix.

```python
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.2))
for ax, M, title in zip(axes, [C, C @ G[0]],
                        ["$C$ (symmetric)", "$C\\gamma^{(x_1)}$ (antisymmetric)"]):
    image = ax.imshow(M, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(0, 16, 3), [str(k + 1) for k in range(0, 16, 3)])
    ax.set_yticks(range(0, 16, 3), [str(k + 1) for k in range(0, 16, 3)])
    ax.set_xlabel("column $B$")
    ax.set_ylabel("row $A$")
    ax.set_title(title)
    ax.grid(False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8)
save_figure(fig, "symmetric_antisymmetric",
...)
```

Heat maps of $C$ and $C\gamma^{(x_1)}$ (`C @ G[0]`), with ticks every three rows labelled 1, 4, 7, ... (rows and columns counted from 1, as in the book), and one common colour scale for both panels (`fig.colorbar(image, ax=axes, ...)`). **What Figure 07a.5 shows.** Each row of both matrices has exactly one coloured square. Mirroring $C$ in its diagonal gives the same colours (symmetric); mirroring $C\gamma^{(x_1)}$ turns every red square into blue and every blue into red (antisymmetric).

**In [14]: the powers of the scalar density.**

```python
S = Grassmann()
for A in range(16):
    for B in range(16):
        if C[A, B] != 0:
            S = S + (theta(A) * theta(16 + B)).scaled(int(C[A, B]))  # chi_A C psi_B
```

$S = \sum_{A,B}\chi_AC_{AB}\psi_B$ is built from the 16 nonzero entries of $C$; here the $\chi_A$ are generators 0 to 15 and the $\psi_B$ generators 16 to 31.

```python
power = number(1)
counts, sizes_ok = [], True
for k in range(1, 18):
    power = power * S  # S^k
    counts.append(len(power.terms))
    sizes_ok = sizes_ok and all(abs(value) == math.factorial(k)
                                for value in power.terms.values())
report("monomials of S^k for k = 1 .. 8", counts[:8])
report("monomials of S^k for k = 9 .. 17", counts[8:])
check(counts[:16] == [math.comb(16, k) for k in range(1, 17)] and sizes_ok,
      "S^k has binom(16, k) monomials with coefficients +-k! (k = 1 .. 16)")
check(counts[16] == 0, "S^17 = 0: every function of S is a polynomial of degree <= 16")
```

`power` starts at 1 and is multiplied by $S$ seventeen times. After each multiplication the number of monomials is stored, and `sizes_ok` stays true only while every coefficient of $S^k$ has the size $k!$ (`math.factorial(k)`). The two `report` lines print the counts; `counts[:8]` is the first eight entries and `counts[8:]` the rest. The first check compares the counts for $k = 1$ to 16 with $\binom{16}{k}$, the second requires $S^{17} = 0$. The computation takes about one second.

```python
# ordinary (commuting) stand-ins for the 16 chi_A and the 16 psi_A
chi_c, psi_c = sp.symbols("chi0:16"), sp.symbols("psi0:16")
S_commuting = sum(int(C[A, B]) * chi_c[A] * psi_c[B]
                  for A in range(16) for B in range(16) if C[A, B] != 0)
commuting = [len(sp.Add.make_args(sp.expand(S_commuting ** k))) for k in (1, 2, 3)]
check(commuting == [math.comb(16 + k - 1, k) for k in (1, 2, 3)],
      "commuting numbers: S^k has binom(15 + k, k) monomials (k = 1, 2, 3)")
```

The same $S$ with 32 ordinary sympy symbols `chi0` to `chi15` and `psi0` to `psi15` in place of the generators. Its powers $k = 1, 2, 3$ are multiplied out and their terms counted; the check compares with $\binom{15 + k}{k}$. **Out [14]:** `RESULT monomials of S^k for k = 1 .. 8 = [16, 120, 560, 1820, 4368, 8008, 11440, 12870]`, `RESULT monomials of S^k for k = 9 .. 17 = [11440, 8008, 4368, 1820, 560, 120, 16, 1, 0]` and three PASS lines.

**In [15]: Figure 07a.6.**

```python
ks = np.arange(1, 18)
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 4.0))
left.bar(ks[:16], counts[:16], color="tab:blue", label="Grassmann (computed)")
left.plot(ks, [math.comb(15 + k, k) for k in ks], "s--", color="tab:orange",
          label="ordinary numbers $\\binom{15+k}{k}$")
left.set_yscale("log")
left.set_xticks(range(1, 18, 2))
left.set_xlabel("power $k$")
left.set_ylabel("number of monomials of $S^k$")
left.set_title("$S^{17} = 0$ for Grassmann numbers")
left.legend(fontsize=8)
right.semilogy(ks[:16], [math.factorial(k) for k in ks[:16]], "o-", color="tab:green")
right.set_xticks(range(1, 17, 3))
right.set_xlabel("power $k$")
right.set_ylabel("size of every coefficient of $S^k$")
right.set_title("Coefficients $\\pm k!$")
fig.tight_layout()
save_figure(fig, "powers_of_s",
...)
```

Left: blue bars of the Grassmann counts for $k = 1$ to 16 and orange squares joined by a dashed line for the commuting counts $\binom{15 + k}{k}$ for $k = 1$ to 17, on a logarithmic axis (`set_yscale("log")`). Right: the size $k!$ of the coefficients. **What Figure 07a.6 shows.** The Grassmann counts rise to 12870 at $k = 8$ and fall back symmetrically to 1 at $k = 16$, with no bar at $k = 17$; the commuting counts keep growing. On the right, the coefficients grow from 1 to $16! \approx 2.1\times10^{13}$.

**In [16]: the test algebra with two generators.**

```python
coefficients = [[int(rng.integers(-3, 4)) + sp.I * int(rng.integers(-3, 4))
                 for k in range(2)] for A in range(16)]
Psi = [th1.scaled(coefficients[A][0]) + th2.scaled(coefficients[A][1])
       for A in range(16)]
Psi_dagger = [conjugate(component, PAIR4) for component in Psi]
S2 = bilinear(Psi_dagger, sp.Matrix(C), Psi)  # S in the test algebra
shapes = sorted(S2.terms)
say(f"monomials of S (generator numbers): {shapes}")
say(f"monomials of S^2: {sorted((S2 * S2).terms)}")
check(all(len(m) == 2 and m[0] in (0, 1) and m[1] in (2, 3) for m in shapes)
      and (conjugate(S2, PAIR4) - S2).is_zero(),
      "S is a real even element on the monomials thetabar_k theta_l")
check(sorted((S2 * S2).terms) == [(0, 1, 2, 3)] and (S2 * S2 * S2).is_zero(),
      "S^2 != 0 lives on theta_1 theta_2 thetabar_1 thetabar_2 and S^3 = 0",
      record=reproduces(WLREP, "grassmann_algebra_structure"))
```

`coefficients` holds, for each of the 16 components, two random Gaussian integers $c_{A1}, c_{A2}$; `Psi` is the column of the components $c_{A1}\theta_1 + c_{A2}\theta_2$ (generators 0 and 1 of the test algebra of In [9]), and `Psi_dagger` the conjugates. `S2` is $S = \Psi^\dagger C\Psi$ in this algebra (the name says "S of the two-generator algebra"). The two `say` lines print the monomials of $S$ and of $S^2$ as tuples of generator numbers. The first check: every monomial of $S$ holds exactly one generator $\theta_l$ (number 0 or 1) and one conjugate $\bar\theta_k$ (number 2 or 3), which sorting puts second, and $S$ is real. The second: $S^2$ lives on the single monomial (0, 1, 2, 3) and $S^3 = 0$. **Out [16]:** `monomials of S (generator numbers): [(0, 2), (0, 3), (1, 2), (1, 3)]`, `monomials of S^2: [(0, 1, 2, 3)]` and two PASS lines, the second with its "reproduces" line.

**In [17]: the Grassmann oscillator.**

```python
def total_derivative(element, step):
    """d/dt on jets: every generator g in every place becomes g + step (from a
    variable to its derivative), with the product rule; the raised monomial is
    sorted back with its sign."""
    result = Grassmann()
    for monomial, coefficient in element.terms.items():
        for place, g in enumerate(monomial):
            raised = monomial[:place] + (g + step,) + monomial[place + 1:]
            sign, ordered = sort_with_sign(raised)
            if sign != 0:
                result.add(ordered, sign * coefficient)
    return result
```

`total_derivative(element, step)` is $d/dt$ on jets. In the numbering of this cell the generators of the value come first and their derivatives have numbers larger by `step` (here 2), so raising a generator `g` to its derivative means replacing it by `g + step`. For every monomial and every place in it, the raised monomial is formed, sorted back with its sign, and added (the product rule adds one term per place).

```python
omega = sp.Symbol("omega", positive=True)  # the angular frequency
bar, th, bar_d, th_d = theta(0), theta(1), theta(2), theta(3)
L_osc = ((bar * th_d - bar_d * th).scaled(sp.I / 2) - (bar * th).scaled(omega))
E_osc = left_derivative(L_osc, 0) - total_derivative(left_derivative(L_osc, 2), 2)
PAIR6 = [1, 0, 3, 2, 5, 4]  # theta-bar <-> theta for the value and two derivatives
say(f"Euler-Lagrange expression (monomial: coefficient): {E_osc.terms}")
check((E_osc - (th_d.scaled(sp.I) - th.scaled(omega))).is_zero(),
      "the oscillator's Euler-Lagrange expression is i theta' - omega theta")
check((conjugate(L_osc, PAIR6) - L_osc).is_zero(), "the oscillator Lagrangian is real")
```

`omega` is a positive symbol. The generators are $\bar\theta$ (0), $\theta$ (1), $\bar\theta'$ (2), $\theta'$ (3); `L_osc` is the Lagrangian of Section 7.13. `E_osc` is the Euler-Lagrange expression with left derivatives: the left derivative with respect to $\bar\theta$ minus the total derivative of the left derivative with respect to $\bar\theta'$. `PAIR6` pairs $\bar\theta \leftrightarrow \theta$ for the value and two derivatives (generators 4 and 5 are the second derivatives). The `say` line prints the expression as its dictionary of terms; the checks compare it with $i\theta' - \omega\theta$ and test that $L$ is real. **Out [17]:** `Euler-Lagrange expression (monomial: coefficient): {(3,): I, (1,): -omega}` (that is $i\theta' - \omega\theta$) and two PASS lines.

**In [18]: the solution, and Figure 07a.7.**

```python
t = sp.Symbol("t", real=True)
solution = sp.exp(-sp.I * omega * t)  # theta(t) = solution * theta_0
residual = sp.simplify(sp.I * sp.diff(solution, t) - omega * solution)
check(residual == 0, "theta(t) = exp(-i omega t) theta_0 solves i theta' = omega theta")
```

The coefficient function $e^{-i\omega t}$ of the solution $\theta(t) = e^{-i\omega t}\theta_0$; the residual $i\frac{d}{dt}e^{-i\omega t} - \omega e^{-i\omega t}$ simplifies to 0 (the generator $\theta_0$ is a common factor and drops out).

```python
times = np.linspace(0.0, 2.0 * np.pi, 400)
values = np.exp(-2.0j * times)  # omega = 2
fig, ax = plt.subplots()
ax.plot(times, values.real, label="real part $\\cos 2t$")
ax.plot(times, values.imag, "--", label="imaginary part $-\\sin 2t$")
ax.plot(times, np.abs(values), ":", color="black", label="absolute value 1")
ax.set_xlabel("time $t$")
ax.set_ylabel("coefficient of $\\theta_0$")
ax.set_title("$\\theta(t) = e^{-2it}\\,\\theta_0$")
ax.set_ylim(-1.75, 1.25)  # room for the legend below the curves
ax.legend(loc="lower center", ncol=3, fontsize=9)
save_figure(fig, "oscillator_solution",
...)
```

400 times from 0 to $2\pi$, the values of $e^{-2it}$ ($\omega = 2$), and one panel with the real part, the imaginary part and the absolute value; `set_ylim(-1.75, 1.25)` leaves room for the legend below the curves. **What Figure 07a.7 shows.** The function in front of $\theta_0$ is an ordinary complex function of absolute value 1 that turns with angular frequency 2: its real part is $\cos 2t$ and its imaginary part $-\sin 2t$. The anticommuting nature of the solution sits entirely in the constant generator $\theta_0$.

**In [19]: the first-order kinetic term of real fields.**

```python
th0, th1_, th0_d, th1_d = theta(0), theta(1), theta(2), theta(3)
K_A = th0 * th1_d - th1_ * th0_d  # theta^T A theta' with A = ((0, 1), (-1, 0))
K_I = th0 * th0_d + th1_ * th1_d  # theta^T I theta'
```

Four generators: $\theta_0$ (0), $\theta_1$ (1), $\theta_0'$ (2), $\theta_1'$ (3); the variable names `th1_` and `th0_d`, `th1_d` avoid clashing with names used earlier. `K_A` $= \theta^TA\theta'$ and `K_I` $= \theta^T\theta'$ of Section 7.13.

```python
def euler_lagrange(L, field):
    """dL/d(field) - d/dx dL/d(field') with left derivatives (field = 0 or 1)."""
    return left_derivative(L, field) - total_derivative(left_derivative(L, field + 2), 2)
```

`euler_lagrange(L, field)` is the Euler-Lagrange expression of field 0 or 1 with left derivatives; the derivative of field `field` is generator `field + 2`.

```python
check((K_A - total_derivative((th0 * th1_ - th1_ * th0).scaled(sp.Rational(1, 2)),
                              2)).is_zero(),
      "K_A = (1/2) d/dx (theta^T A theta): a total derivative")
check(euler_lagrange(K_A, 0).is_zero() and euler_lagrange(K_A, 1).is_zero(),
      "real Grassmann fields: both Euler-Lagrange expressions of K_A vanish")
check((euler_lagrange(K_I, 0) - th0_d.scaled(2)).is_zero(),
      "real Grassmann fields: K_I gives the expression 2 theta_0'")
```

Three checks: $K_A$ equals $\tfrac12\frac{d}{dx}(\theta^TA\theta)$ with $\theta^TA\theta = \theta_0\theta_1 - \theta_1\theta_0$; both Euler-Lagrange expressions of $K_A$ vanish; the expression of $K_I$ for $\theta_0$ is $2\theta_0'$.

```python
from sympy.calculus.euler import euler_equations  # sympy's Euler-Lagrange

xs = sp.Symbol("x", real=True)
q0, q1 = sp.Function("q0")(xs), sp.Function("q1")(xs)  # two ordinary functions
K_A_commuting = q0 * sp.diff(q1, xs) - q1 * sp.diff(q0, xs)
equations = euler_equations(K_A_commuting, [q0, q1], xs)
expressions = [sp.simplify(equation.lhs - equation.rhs) for equation in equations]
say(f"ordinary numbers, Euler-Lagrange expressions of K_A: {expressions}")
check(sp.simplify(expressions[0] - 2 * sp.diff(q1, xs)) == 0
      and sp.simplify(expressions[1] + 2 * sp.diff(q0, xs)) == 0,
      "ordinary numbers: K_A gives the nonzero expressions 2 q1' and -2 q0'")
```

The same kinetic term for two ordinary functions $q_0(x)$, $q_1(x)$, with sympy's `euler_equations`; the list `expressions` holds left side minus right side of each equation. The check requires $2q_1'$ and $-2q_0'$. **Out [19]:** four PASS lines and `ordinary numbers, Euler-Lagrange expressions of K_A: [2*Derivative(q1(x), x), -2*Derivative(q0(x), x)]`.

**In [20]: the last check.**

```python
names = ["dimension_and_degrees", "multiplication_signs", "commutation_signs",
         "bilinear_survivors", "symmetric_antisymmetric", "powers_of_s",
         "oscillator_solution"]
files = [f"{FIGURE_FOLDER}/07a_{k}_{name}.png" for k, name in enumerate(names, 1)]
check(all(output_file(path).is_file() for path in files),
      "all 7 figure files of this notebook exist")
all_checks_passed()
```

The seven figure files are listed and checked, and the last line is printed. **Out [20]:** `PASS all 7 figure files of this notebook exist` and `ALL 38 CHECKS PASSED (notebook 07a)`.

### 7.18 The geometry the fields live in

The Lagrangian of the two fields uses five geometric objects of the author's metric: the frame, the volume factor, the coordinate gammas, the Christoffel symbols and the spin connection. Chapter 3 introduced the first four and Chapter 6 treats the spin connection in full; this section collects what the field equations need, with the derivations that Notebook 07b repeats exactly.

**The frame and the volume factor.** The author's metric is diagonal, $g_{aa} = \eta_{aa}f_a^2$ (no sum), with the frame metric $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in the order $x_1, \dots, x_8$ and the **frame factors**

$$
f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z,\qquad f_4 = 1,\qquad f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z,\qquad f_8 = \cot z .
$$

The **diagonal frame** (or **vielbein**, "many legs") $e^a{}_\mu = f_a\delta^a_\mu$ is a set of eight local unit directions, one along each coordinate; a column of numbers written in this frame, such as the 16 components of a spinor, is measured with these unit directions. For a diagonal metric $|\det g|$ is the product of the $|g_{aa}| = f_a^2$, so the **volume factor** is

$$
\sqrt{|g|} = f_1f_2f_3\cdot f_4\cdot f_5f_6f_7\cdot f_8 = e^{3a_4}\sin^{1/2}z\cdot1\cdot e^{-3a_4}\sin^{1/2}z\cdot\frac{\cos z}{\sin z} = \cos z
$$

(insert the factors; $e^{3a_4}e^{-3a_4} = 1$; $\sin^{1/2}z\sin^{1/2}z = \sin z$ cancels against $1/\sin z$). It does not depend on the time: the inflation $e^{3a_4}$ of 3-space and the deflation $e^{-3a_4}$ of the extra times compensate exactly (PROVED; Notebook 07b, In [4]; the table at the end of this section names the Revision checks of this and the following statements).

**Exact bookkeeping with five symbols.** Notebook 07b writes every coefficient with the symbols $E = e^{a_4}$, $s = \sin^{1/6}z$, $c = \cos z$, $A_1 = a_4'$, $A_2 = a_4''$, $A_3 = a_4'''$, and $H$, $m$, $\lambda$ (a prime is $d/dx_4$). Then $f_{1,2,3} = Es$, $f_{5,6,7} = s/E$ and $f_8 = c/s^6$ (because $\sin z = s^6$). Their derivatives follow from the chain rule: $\partial_4E = EA_1$; $\partial_8s = \tfrac16\sin^{-5/6}z\cdot\cos z\cdot6H = Hc/s^5$ (the power rule, the derivative $\cos z$ of $\sin z$, then $dz/dx_8 = 6H$); $\partial_8c = -\sin z\cdot6H = -6Hs^6$; nothing depends on $x_1, x_2, x_3, x_5, x_6, x_7$. Because $\cos^2z + \sin^2z = 1$, the symbols obey $c^2 = 1 - s^{12}$; replacing $c^2$ by $1 - s^{12}$ decides exactly whether an expression is zero.

**The coordinate gammas.** The author's eight frame gammas $\gamma^{(x_1)}, \dots, \gamma^{(x_8)}$ (Chapter 4) obey $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}$. The **coordinate gammas** are $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ (the frame gamma of the same direction divided by its frame factor); they obey $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}$ with the inverse metric $g^{\mu\mu} = \eta_{\mu\mu}/f_\mu^2$.

**The Christoffel symbols.** The **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu}$ say how the coordinate directions turn from point to point (Chapter 3). For a diagonal metric the general formula keeps only a few terms:

$$
\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}\big(\delta_{\lambda\nu}\,\partial_\mu g_{\lambda\lambda} + \delta_{\lambda\mu}\,\partial_\nu g_{\lambda\lambda} - \delta_{\mu\nu}\,\partial_\lambda g_{\mu\mu}\big) .
$$

Four examples, each in one line. $\Gamma^{x_1}{}_{x_1x_4} = \partial_4g_{11}/(2g_{11}) = \partial_4(E^2s^2)/(2E^2s^2) = 2E^2A_1s^2/(2E^2s^2) = a_4'$: 3-space stretches at the rate $a_4'$. $\Gamma^{x_5}{}_{x_4x_5} = \partial_4g_{55}/(2g_{55})$ with $g_{55} = -s^2/E^2$, and $\partial_4(-s^2E^{-2}) = 2s^2E^{-2}A_1$, so $\Gamma^{x_5}{}_{x_4x_5} = 2s^2E^{-2}A_1/(-2s^2E^{-2}) = -a_4'$: the extra times shrink at the same rate. $\Gamma^{x_1}{}_{x_1x_8} = \partial_8(E^2s^2)/(2E^2s^2) = \partial_8s/s = Hc/s^6 = H\cot z$. $\Gamma^{x_8}{}_{x_8x_8} = \tfrac12\partial_8\ln g_{88}$ with $g_{88} = c^2/s^{12}$, so $\tfrac12\big(2\partial_8c/c - 12\,\partial_8s/s\big) = -6Hs^6/c - 6Hc/s^6 = -6H(s^{12} + c^2)/(cs^6) = -6H/(\sin z\cos z)$. The metric has 25 independent nonzero Christoffel symbols (COMPUTED exactly by Notebook 07b, In [7], and compared there with the formula record `Revision/theory/field-theory.json`).

**Why a spinor needs a connection.** The 16 components of a spinor are measured in the local frame. Because the frame turns from point to point (that is what the Christoffel symbols describe), the plain derivative $\partial_\mu\Psi$ compares components measured in two different frames, and an equation built from it would depend on the arbitrary choice of frames. The **canonical spin connection** $\omega_\mu{}^a{}_b$ records how the frame turns; it is fixed by the **vielbein postulate** $\partial_\mu e^a{}_\nu - \Gamma^\lambda{}_{\mu\nu}e^a{}_\lambda + \omega_\mu{}^a{}_b\,e^b{}_\nu = 0$ (the frame is carried along consistently with the metric). For the diagonal frame its solution is

$$
\omega_\mu{}^a{}_b = f_a\Big(\delta_{ab}\,\partial_\mu\frac{1}{f_b} + \frac{\Gamma^a{}_{\mu b}}{f_b}\Big),\qquad \omega_{\mu ab} = \eta_{aa}\,\omega_\mu{}^a{}_b ,
$$

and the lowered $\omega_{\mu ab}$ is antisymmetric in $a, b$. For $a \neq b$ it is $\eta_{aa}f_a\Gamma^a{}_{\mu b}/f_b$. Two examples: $\omega_{x_1(x_1)(x_4)} = (+1)\cdot Es\cdot a_4'/1 = a_4'e^{a_4}\sin^{1/6}z$, and $\omega_{x_5(x_4)(x_5)} = (-1)\cdot1\cdot\Gamma^{x_4}{}_{x_5x_5}/f_5$ with $\Gamma^{x_4}{}_{x_5x_5} = -\partial_4g_{55}/(2g_{44}) = s^2A_1/E^2$, which gives $-(s^2A_1/E^2)/(s/E) = -a_4'e^{-a_4}\sin^{1/6}z$. Exactly 12 components with $a < b$ are nonzero (COMPUTED exactly by Notebook 07b, In [8]):

$$
\begin{aligned}
\omega_{x_i(x_i)(x_4)} &= a_4'e^{a_4}\sin^{1/6}z, & \omega_{x_i(x_i)(x_8)} &= He^{a_4}\sin^{1/6}z, \\
\omega_{x_t(x_4)(x_t)} &= -a_4'e^{-a_4}\sin^{1/6}z, & \omega_{x_t(x_t)(x_8)} &= -He^{-a_4}\sin^{1/6}z ,
\end{aligned}
$$

for $i = 1, 2, 3$ and $t = 5, 6, 7$. Each is $a_4'$ or $H$ times a factor that never vanishes for $0 < z < \pi/2$.

**The spinor connection and the covariant derivatives.** With the **spin generators** $S^{ab} = \tfrac14(\gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)})$, which equal $\tfrac12\gamma^{(a)}\gamma^{(b)}$ for $a \neq b$ (the two products differ only in sign) and 0 for $a = b$ (Chapter 5), the **spinor connection** is

$$
\Omega_\mu = \tfrac12\,\omega_{\mu ab}S^{ab} = \sum_{a<b}\omega_{\mu ab}S^{ab}
$$

(the two halves of the double sum are equal, because both $\omega_{\mu ab}$ and $S^{ab}$ change sign when $a$ and $b$ are exchanged). The **covariant derivatives** of a column and of a row are

$$
D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi,\qquad D_\mu\bar\Psi = \partial_\mu\bar\Psi - \bar\Psi\,\Omega_\mu .
$$

In the author's metric $\Omega_{x_4} = \Omega_{x_8} = 0$, and for $i = 1, 2, 3$ and $t = 5, 6, 7$:

$$
\begin{aligned}
\Omega_{x_i} &= \tfrac12e^{a_4}\sin^{1/6}z\,\big(a_4'\gamma^{(x_i)}\gamma^{(x_4)} + H\gamma^{(x_i)}\gamma^{(x_8)}\big), \\
\Omega_{x_t} &= -\tfrac12e^{-a_4}\sin^{1/6}z\,\big(a_4'\gamma^{(x_4)}\gamma^{(x_t)} + H\gamma^{(x_t)}\gamma^{(x_8)}\big) .
\end{aligned}
$$

**The term $\gamma^\mu\Omega_\mu$, direction by direction.** The field equation will contain the matrix $\gamma^\mu\Omega_\mu$ (summed over $\mu$). For an inflating direction $x_i$:

$$
\gamma^{x_i}\Omega_{x_i} = \frac{\gamma^{(x_i)}}{e^{a_4}\sin^{1/6}z}\cdot\tfrac12e^{a_4}\sin^{1/6}z\,\big(a_4'\gamma^{(x_i)}\gamma^{(x_4)} + H\gamma^{(x_i)}\gamma^{(x_8)}\big) = \tfrac12\big(a_4'\gamma^{(x_4)} + H\gamma^{(x_8)}\big)
$$

(the frame factors cancel; then $\gamma^{(x_i)}\gamma^{(x_i)} = \eta_{ii} = +1$). For a deflating extra time $x_t$:

$$
\begin{aligned}
\gamma^{x_t}\Omega_{x_t} &= \frac{\gamma^{(x_t)}}{e^{-a_4}\sin^{1/6}z}\cdot\Big(-\tfrac12e^{-a_4}\sin^{1/6}z\Big)\big(a_4'\gamma^{(x_4)}\gamma^{(x_t)} + H\gamma^{(x_t)}\gamma^{(x_8)}\big) \\
&= -\tfrac12\big(a_4'\gamma^{(x_t)}\gamma^{(x_4)}\gamma^{(x_t)} + H\gamma^{(x_t)}\gamma^{(x_t)}\gamma^{(x_8)}\big)
\end{aligned}
$$

(the frame factors cancel), and $\gamma^{(x_t)}\gamma^{(x_4)}\gamma^{(x_t)} = -\gamma^{(x_4)}\gamma^{(x_t)}\gamma^{(x_t)} = -\gamma^{(x_4)}\cdot(-1) = \gamma^{(x_4)}$ (exchange two different gammas, then $\gamma^{(x_t)}\gamma^{(x_t)} = \eta_{tt} = -1$), and $\gamma^{(x_t)}\gamma^{(x_t)}\gamma^{(x_8)} = -\gamma^{(x_8)}$; so

$$
\gamma^{x_t}\Omega_{x_t} = -\tfrac12\big(a_4'\gamma^{(x_4)} - H\gamma^{(x_8)}\big) = -\tfrac12a_4'\gamma^{(x_4)} + \tfrac12H\gamma^{(x_8)} .
$$

Summing over the three inflating directions, the three deflating extra times and the two directions $x_4$, $x_8$ (which give 0):

$$
\gamma^\mu\Omega_\mu = 3\cdot\tfrac12a_4'\gamma^{(x_4)} - 3\cdot\tfrac12a_4'\gamma^{(x_4)} + 6\cdot\tfrac12H\gamma^{(x_8)} = 3H\gamma^{(x_8)} .
$$

The time-direction terms of the three inflating directions and the three deflating extra times cancel exactly, because 3-space inflates at the rate at which the extra times deflate; the hidden-direction terms of all six directions add up. The result does not contain $a_4$ at all, for every function $a_4(x_4)$ (PROVED; Notebook 07b, In [9], Figure 07b.2).

**Two more facts about $\Omega_\mu$.** (i) For each direction separately, $\gamma^\mu$ and $\Omega_\mu$ anticommute: $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ (no sum). The reason: $\Omega_\mu$ contains only products $\gamma^{(\mu)}\gamma^{(b)}$ that share the index $\mu$ with $\gamma^{(\mu)}$, and $\gamma^{(\mu)}\gamma^{(\mu)}\gamma^{(b)} = \eta_{\mu\mu}\gamma^{(b)}$ while $\gamma^{(\mu)}\gamma^{(b)}\gamma^{(\mu)} = -\gamma^{(\mu)}\gamma^{(\mu)}\gamma^{(b)} = -\eta_{\mu\mu}\gamma^{(b)}$; the two add to 0. (ii) The same matrix is a derivative of the volume factor and the coordinate gammas:

$$
\frac{1}{2\sqrt{|g|}}\,\partial_\mu\big(\sqrt{|g|}\,\gamma^\mu\big) = \frac{1}{2\cos z}\,\partial_8\Big(\cos z\cdot\frac{\sin z}{\cos z}\Big)\gamma^{(x_8)} = \frac{6H\cos z}{2\cos z}\,\gamma^{(x_8)} = 3H\gamma^{(x_8)} = \gamma^\mu\Omega_\mu .
$$

The first equality: $\sqrt{|g|}\gamma^\mu = \cos z\,\gamma^{(\mu)}/f_\mu$ depends only on $x_4$ and $x_8$; for $\mu = x_4$ it is $\cos z\,\gamma^{(x_4)}$, which does not depend on $x_4$, so only $\mu = x_8$ contributes, with $1/f_8 = \tan z = \sin z/\cos z$. The second: $\cos z\cdot\sin z/\cos z = \sin z$, whose derivative along $x_8$ is $6H\cos z$. The third cancels $\cos z$. So $\partial_\mu(\sqrt{|g|}\gamma^\mu) = 2\sqrt{|g|}\,\gamma^\mu\Omega_\mu$ in this metric (PROVED; Notebook 07b, In [11]). Both facts are used in the next three sections.

**Where the statements of this section are verified.** The reports are named by their file names; the theory reports lie in the folder `Revision/theory/reports`, the formula record is `Revision/theory/field-theory.json`.

| statement | status | where it is verified |
| --- | --- | --- |
| $\sqrt{\lvert g\rvert} = \cos z$ | PROVED; Notebook 07b, In [4] | `python-field-theory.json`, check `sqrt_det_g_equals_cos_z`; `wolfram-field-theory.json`, check `sqrt_det_g_is_cos_z` |
| 25 independent nonzero Christoffel symbols | COMPUTED exactly; In [7] | `python-field-theory.json`, check `christoffel_symmetric_metric_compatible`; formula record, key `christoffel_nonzero` |
| the vielbein postulate; the 12 nonzero components of $\omega_{\mu ab}$ | COMPUTED exactly; In [8] | `python-field-theory.json`, check `vielbein_postulate`; `wolfram-field-theory.json`, check `omega_components`; formula record, key `omega_nonzero` |
| $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$; the time terms cancel, the hidden terms add | PROVED; In [9] | `python-field-theory.json`, checks `gamma_mu_Omega_mu_equals_3H_gamma_x8` and `time_terms_cancel_hidden_term_survives`; `wolfram-field-theory.json`, checks `gammaOmega_equals_3H_gamma_x8` and `gammaOmega_x4_terms_cancel` |
| $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ for each $\mu$; $\partial_\mu(\sqrt{\lvert g\rvert}\gamma^\mu) = 2\sqrt{\lvert g\rvert}\gamma^\mu\Omega_\mu$ | PROVED; In [11] | `python-field-theory.json`, checks `anticommutator_gamma_Omega_vanishes` and `divergence_of_sqrtg_gamma` |

### 7.19 The two fields and their common Lagrangian

**Why the row contains $C$.** A Lagrangian must not depend on the choice of the local frames, so it must be built from combinations of the field that do not change when the frames are turned. Under a turning of the frames the column changes as $\Psi \to R\Psi$ with a real $16\times16$ **spin transformation** $R$ (Chapter 5). The simplest number, $\Psi^\dagger\Psi = \sum_A|\Psi_A|^2$, becomes $\Psi^\dagger R^TR\Psi$, which equals $\Psi^\dagger\Psi$ only if $R^TR = 1$: true for rotations, false for boosts (Chapter 5). The author's matrix $C$ cures this: every spin generator satisfies $(S^{ab})^TC = -CS^{ab}$ (`python-field-theory.json`, check `S_definition_and_C_S_antisymmetric`), and therefore $R^TCR = C$ for every spin transformation (Chapter 5), so

$$
\Psi^\dagger C\Psi \to \Psi^\dagger R^TCR\,\Psi = \Psi^\dagger C\Psi .
$$

The row $\bar\Psi = \Psi^\dagger C$ is called the **Dirac adjoint** of $\Psi$, and $S = \bar\Psi\Psi$ the **scalar density**. In the same way the eight numbers $\bar\Psi\gamma^{(a)}\Psi$ change like the components of a vector under the turnings, and contracted with a covariant derivative they give the frame-independent combination $\bar\Psi\gamma^\mu D_\mu\Psi$.

**The Lagrangian.** For both fields the Revision record uses the same Lagrangian density (Revision/SPEC.md, section 3; ASSUMED as the definition of the two theories):

$$
\mathcal{L} = \sqrt{|g|}\,\Big[\tfrac12\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big) - m\,S - U(S)\Big],\qquad \bar\Psi = \Psi^\dagger C,\quad S = \bar\Psi\Psi,\quad U(S) = \tfrac{\lambda}{2}S^2 ,
$$

with a sum over $\mu = x_1, \dots, x_8$. Read term by term:

- $\sqrt{|g|} = \cos z$ turns the coordinate volume into proper volume, so that the action does not depend on the coordinates.
- The **kinetic term** $K = \tfrac12\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big)$ contains each derivative to the first power, like the first-order Lagrangians of Section 7.4. It is **symmetrised**: the derivative acts once on $\Psi$ and once on $\bar\Psi$, with opposite signs (Section 7.20 shows why).
- The **mass term** $-mS = -m\bar\Psi\Psi$ is linear in the mass $m$ (a real number) and quadratic in the field: every term contains one component of $\Psi^\dagger$ and one of $\Psi$.
- The **interaction** $-U(S) = -\tfrac{\lambda}{2}S^2$ with a real coupling $\lambda$ is quartic in the field. For dirac16complex it must be a polynomial in $S$ (Section 7.12: $S^{17} = 0$); for dirac16complex00 any real function of $S$ would be allowed, and the record keeps the same $U$ so that the two theories differ only in the statistics. We write $V = m + U'(S) = m + \lambda S$, the **effective mass**.
- Gravity enters through $\sqrt{|g|}$, through the coordinate gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$, and through the spinor connection in $D_\mu$.

The structure is that of Example B of Section 7.4: $\Psi$ plays the role of $\psi$, the row $\bar\Psi$ that of $\psi^*$, and the kinetic term is symmetrised in the same way. The factor $i$ of Example B is not needed, because the matrices $C\gamma^{(a)}$ are antisymmetric (next section).

**The two statistics.** For dirac16complex the 16 components $\Psi_A$ and the 16 conjugates $\Psi_A^*$ are 32 Grassmann generators at each point, with the rules of Sections 7.10 and 7.11; for dirac16complex00 they are ordinary complex numbers. Every term of $\mathcal{L}$ is written with all factors of $\Psi^\dagger$ (or of its derivatives) to the LEFT of all factors of $\Psi$, so the formula can be read for both kinds of numbers without any reordering.

### 7.20 Reality, the total divergence, and the connection that drops out of $\mathcal{L}$

**The lemma for two columns.** For two columns $\Psi$ and $\Phi$ (for example $\Phi = D_\mu\Psi$), both commuting or both Grassmann, and a matrix $M$ of ordinary numbers,

$$
\big(\Psi^\dagger M\Phi\big)^* = \Phi^\dagger M^\dagger\Psi .
$$

The proof is the three-line computation of Section 7.12 with $\Phi$ in place of the second $\Psi$: for Grassmann components the conjugation reverses the order of the two factors; for commuting components nothing needs reordering (PROVED).

**The Lagrangian is real.** Call $K_u = \bar\Psi\gamma^\mu D_\mu\Psi = \Psi^\dagger(C\gamma^\mu)(D_\mu\Psi)$ the **unsymmetrised** kinetic term. Line by line:

$$
K_u^* = (D_\mu\Psi)^\dagger(C\gamma^\mu)^\dagger\Psi
$$

(the lemma with $M = C\gamma^\mu$ and $\Phi = D_\mu\Psi$);

$$
= -(D_\mu\Psi)^\dagger C\gamma^\mu\Psi
$$

($C\gamma^\mu = C\gamma^{(\mu)}/f_\mu$ is real and antisymmetric, so its dagger is its transpose, which is minus itself);

$$
= -(D_\mu\bar\Psi)\gamma^\mu\Psi
$$

(because $(D_\mu\Psi)^\dagger C = \partial_\mu\Psi^\dagger C + \Psi^\dagger\Omega_\mu^TC = \partial_\mu\bar\Psi - \Psi^\dagger C\Omega_\mu = D_\mu\bar\Psi$: the matrix $\Omega_\mu$ is real, and $\Omega_\mu^TC = -C\Omega_\mu$ since $\Omega_\mu$ is a combination of the $S^{ab}$ with real coefficients and $(S^{ab})^TC = -CS^{ab}$). So the kinetic term $K = \tfrac12\big(K_u - (D_\mu\bar\Psi)\gamma^\mu\Psi\big) = \tfrac12(K_u + K_u^*)$ is real. Next $S^* = \Psi^\dagger C^\dagger\Psi = S$, because $C$ is real and symmetric (the lemma with $M = C$). For Grassmann components $S$ is even, so $(S^2)^* = S^*S^* = S^2$, and $U(S) = \tfrac{\lambda}{2}S^2$ is real; for commuting components $S$ is a real number. Finally $m$, $\lambda$ and $\sqrt{|g|}$ are real. Hence $\mathcal{L}^* = \mathcal{L}$ for both statistics (PROVED; Notebook 07b, In [15]; `python-field-theory.json`, checks `grassmann_lagrangian_real` and `commuting_lagrangian_real`; `wolfram-field-theory.json`, checks `L_real_G` and `L_real_C`). The unsymmetrised form $\sqrt{|g|}\,[K_u - mS - U]$ is NOT real: its imaginary part is the difference $K_u - K_u^*$, which is not zero for a general field (checks `grassmann_controls_not_vacuous` and `commuting_controls_not_vacuous`); this control shows that the reality test is not empty. A real Lagrangian matters: the equations obtained by varying $\Psi^\dagger$ and by varying $\Psi$ are then conjugates of each other (Section 7.21), so there are exactly as many equations as unknown components.

**The two forms differ by a total divergence.** The product rule along $x_\mu$, applied to the three factors of $\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi$ (with the matrix $\sqrt{|g|}\gamma^\mu$ as one factor), gives

$$
\partial_\mu\big(\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi\big) = \sqrt{|g|}\,(\partial_\mu\bar\Psi)\gamma^\mu\Psi + \bar\Psi\,\partial_\mu\big(\sqrt{|g|}\gamma^\mu\big)\Psi + \sqrt{|g|}\,\bar\Psi\gamma^\mu\partial_\mu\Psi
$$

(for Grassmann components the derivative is even and needs no sign; the order of the factors is kept);

$$
= \sqrt{|g|}\,\big[(\partial_\mu\bar\Psi)\gamma^\mu\Psi + 2\bar\Psi\gamma^\mu\Omega_\mu\Psi + \bar\Psi\gamma^\mu\partial_\mu\Psi\big]
$$

(the identity $\partial_\mu(\sqrt{|g|}\gamma^\mu) = 2\sqrt{|g|}\gamma^\mu\Omega_\mu$ of Section 7.18);

$$
= \sqrt{|g|}\,\big[(\partial_\mu\bar\Psi - \bar\Psi\Omega_\mu)\gamma^\mu\Psi + \bar\Psi\gamma^\mu(\partial_\mu\Psi + \Omega_\mu\Psi)\big] = \sqrt{|g|}\,\big[(D_\mu\bar\Psi)\gamma^\mu\Psi + \bar\Psi\gamma^\mu D_\mu\Psi\big]
$$

(split $2\gamma^\mu\Omega_\mu = \gamma^\mu\Omega_\mu - \Omega_\mu\gamma^\mu$, using $\gamma^\mu\Omega_\mu = -\Omega_\mu\gamma^\mu$ for each $\mu$; then the definitions of the covariant derivatives). Now $K = \tfrac12\big(K_u - (D_\mu\bar\Psi)\gamma^\mu\Psi\big) = K_u - \tfrac12\big(K_u + (D_\mu\bar\Psi)\gamma^\mu\Psi\big)$, so

$$
\mathcal{L} = \sqrt{|g|}\,\big[\bar\Psi\gamma^\mu D_\mu\Psi - mS - U(S)\big] - \tfrac12\,\partial_\mu\big(\sqrt{|g|}\,\bar\Psi\gamma^\mu\Psi\big) .
$$

The two forms differ by a total divergence (the field version of the total derivative of Section 7.4) and give the same field equations; only the symmetrised one is real (PROVED; Notebook 07b, In [15]; checks `grassmann_total_divergence_relation` and `commuting_total_divergence_relation`; Wolfram `L_total_divergence_to_unsymmetrised_G` and `_C`).

**The spin connection drops out of $\mathcal{L}$ in this metric.** The terms of $K$ that contain $\Omega_\mu$ are $\tfrac12\bar\Psi\gamma^\mu\Omega_\mu\Psi$ from the first half and $-\tfrac12\big(-\bar\Psi\Omega_\mu\big)\gamma^\mu\Psi = +\tfrac12\bar\Psi\Omega_\mu\gamma^\mu\Psi$ from the second, together

$$
\tfrac12\,\bar\Psi\big(\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu\big)\Psi = 0 ,
$$

because $\gamma^\mu$ and $\Omega_\mu$ anticommute for each $\mu$ (Section 7.18). So in the author's metric

$$
\mathcal{L} = \cos z\,\Big[\tfrac12\sum_{a=1}^{8}\frac{1}{f_a}\big(\bar\Psi\gamma^{(a)}\partial_a\Psi - \partial_a\bar\Psi\,\gamma^{(a)}\Psi\big) - mS - U(S)\Big]
$$

contains no spin connection at all (PROVED; Notebook 07b, In [15]; Wolfram checks `L_spin_connection_drops_out_G` and `L_spin_connection_drops_out_C`). Gravity is still present in $\mathcal{L}$, through $\cos z$ and the frame factors $1/f_a$. Section 7.21 shows that the connection comes back in the field equation, through the derivative of $\sqrt{|g|}\gamma^\mu$.

**Counting the terms of $\mathcal{L}$ at one point.** Written in the jet symbols of Section 7.13 (the 16 components, their 16 conjugates and their first derivatives at one point), the Lagrangian is a sum of monomials. Every $C\gamma^{(a)}$ is a signed permutation matrix, so in each of the 8 directions $\bar\Psi\gamma^{(a)}\partial_a\Psi$ gives 16 monomials $\Psi_A^*\,\partial_a\Psi_B$ and $\partial_a\bar\Psi\gamma^{(a)}\Psi$ another 16: $8\times32 = 256$ kinetic monomials. The mass term gives 16 (one for each nonzero entry of $C$). The quartic term $\tfrac{\lambda}{2}S^2$ is $\tfrac{\lambda}{2}\big(\sum_Ac_AP_A\big)^2$ with the 16 pairs $P_A$ of Section 7.12: the $\binom{16}{2} = 120$ products of two different pairs survive for both statistics, while the 16 squares $P_A^2$ survive only for commuting numbers. So $\mathcal{L}$ has $256 + 16 + 120 = 392$ monomials for dirac16complex and $256 + 16 + 136 = 408$ for dirac16complex00 (COMPUTED by Notebook 07b, In [13] and In [14], Figure 07b.3; the counts reproduce those written in `python-field-theory.json`, checks `grassmann_lagrangian_real` and `commuting_lagrangian_real`).

### 7.21 The Euler-Lagrange equations of both fields

**The derivation by hand, for the commuting field.** Write $V = m + \lambda S$ and, with $\chi_A = \Psi_A^*$ the components of $\Psi^\dagger$,

$$
\frac{\mathcal{L}}{\sqrt{|g|}} = \tfrac12\,\chi C\gamma^\mu\big(\partial_\mu\Psi + \Omega_\mu\Psi\big) - \tfrac12\big(\partial_\mu\chi\,C - \chi C\Omega_\mu\big)\gamma^\mu\Psi - m\,\chi C\Psi - \tfrac{\lambda}{2}\big(\chi C\Psi\big)^2 ,
$$

where $\chi$ is the row $\Psi^\dagger$. Vary the component $\chi_A$; by Section 7.4 the components and their conjugates may be varied as if they were independent. The Euler-Lagrange expression of a field (Section 7.5) needs two partial derivatives.

- Step 1. $\partial\mathcal{L}/\partial\chi_A = \sqrt{|g|}\big[\tfrac12(C\gamma^\mu D_\mu\Psi)_A + \tfrac12(C\Omega_\mu\gamma^\mu\Psi)_A - V(C\Psi)_A\big]$. Rule: a term $\chi\,X$ with a column $X$ has the derivative $X_A$ with respect to $\chi_A$; the second half contributes through its part $+\tfrac12\chi C\Omega_\mu\gamma^\mu\Psi$; and the chain rule gives $\partial\big(\tfrac{\lambda}{2}S^2\big)/\partial\chi_A = \lambda S\,(C\Psi)_A$.
- Step 2. $\partial\mathcal{L}/\partial(\partial_\mu\chi_A) = -\tfrac12\sqrt{|g|}\,(C\gamma^\mu\Psi)_A$. Rule: only the second half contains $\partial_\mu\chi$.
- Step 3. The Euler-Lagrange expression is Step 1 minus $\partial_\mu$ of Step 2, that is Step 1 plus $\tfrac12\partial_\mu\big(\sqrt{|g|}\,C\gamma^\mu\Psi\big)_A$.
- Step 4. By the product rule and Section 7.18, $\partial_\mu\big(\sqrt{|g|}\gamma^\mu\Psi\big) = \partial_\mu\big(\sqrt{|g|}\gamma^\mu\big)\Psi + \sqrt{|g|}\gamma^\mu\partial_\mu\Psi = 2\sqrt{|g|}\,\gamma^\mu\Omega_\mu\Psi + \sqrt{|g|}\,\gamma^\mu\partial_\mu\Psi$ ($C$ is constant and comes out of the derivative).
- Step 5. Add: the expression is $\sqrt{|g|}\,\big(C\,[\tfrac12\gamma^\mu D_\mu\Psi + \tfrac12\Omega_\mu\gamma^\mu\Psi + \gamma^\mu\Omega_\mu\Psi + \tfrac12\gamma^\mu\partial_\mu\Psi - V\Psi]\big)_A$. With $\Omega_\mu\gamma^\mu = -\gamma^\mu\Omega_\mu$ the second and third terms give $\tfrac12\gamma^\mu\Omega_\mu\Psi$, and $\tfrac12\gamma^\mu\Omega_\mu\Psi + \tfrac12\gamma^\mu\partial_\mu\Psi = \tfrac12\gamma^\mu D_\mu\Psi$. So the expression is $\sqrt{|g|}\,\big(C\,(\gamma^\mu D_\mu\Psi - V\Psi)\big)_A$.
- Step 6. $\sqrt{|g|} = \cos z \neq 0$ and $C$ is invertible ($C^2 = 1$), so the 16 expressions vanish exactly when

$$
\gamma^\mu D_\mu\Psi = \big(m + \lambda S\big)\Psi .
$$

This is the **field equation** of both fields (for a general potential, $m + U'(S)$ in place of $m + \lambda S$). The spin connection, which was absent from $\mathcal{L}$, is present in it: Step 4 brought it back through $\partial_\mu(\sqrt{|g|}\gamma^\mu)$.

**Grassmann components.** For dirac16complex the LEFT derivative with respect to $\chi_A$ is used (Section 7.11). In every term of $\mathcal{L}$ the factor $\chi$ (or $\partial_\mu\chi$) stands on the far left, so moving it there costs no sign, and $S$ is even, so the chain rule of Step 1 holds unchanged. Steps 1 to 6 go through word for word: the field equation is the same for both statistics (PROVED; Notebook 07b, In [16], with the control that the comparison with $m$ replaced by $-m$ fails).

**The adjoint equation.** Varying $\Psi$ instead (for Grassmann components with RIGHT derivatives, because $\Psi$ stands on the far right) gives in the same way

$$
(D_\mu\bar\Psi)\gamma^\mu = -\big(m + \lambda S\big)\bar\Psi .
$$

It is not a new equation: it is the **Dirac conjugate** of the field equation. With the residual $\mathcal{E} = \gamma^\mu D_\mu\Psi - V\Psi$, line by line:

$$
\mathcal{E}^\dagger C = (D_\mu\Psi)^\dagger(\gamma^\mu)^TC - V\Psi^\dagger C
$$

(the dagger of a product reverses it; $\gamma^\mu$ and $V$ are real; for Grassmann components the conjugation reverses the order as well);

$$
= -(D_\mu\Psi)^\dagger C\gamma^\mu - V\bar\Psi = -(D_\mu\bar\Psi)\gamma^\mu - V\bar\Psi
$$

($(\gamma^\mu)^TC = -C\gamma^\mu$, because $C\gamma^\mu$ is antisymmetric and $C$ symmetric; then $(D_\mu\Psi)^\dagger C = D_\mu\bar\Psi$ as in Section 7.20). So $\mathcal{E}^\dagger C = -\big[(D_\mu\bar\Psi)\gamma^\mu + V\bar\Psi\big]$: the residual of the adjoint equation is minus the Dirac conjugate of the residual of the field equation. One equation holds exactly when the other does, and the two form one system (PROVED; Notebook 07b, In [16]).

**Where the statements of this section are verified** (in the folder `Revision/theory/reports`; the sympy names start with `grassmann_` or `commuting_` for the two statistics, the Wolfram names end in `_G` or `_C`):

| statement | status | where it is verified |
| --- | --- | --- |
| varying $\Psi^\dagger$ gives $\gamma^\mu D_\mu\Psi = (m + \lambda S)\Psi$, both statistics | PROVED; Notebook 07b, In [16] | `python-field-theory.json`, checks `grassmann_euler_lagrange_psibar_variation` and `commuting_euler_lagrange_psibar_variation`; `wolfram-field-theory.json`, checks `EL_Psibar_G` and `EL_Psibar_C` |
| varying $\Psi$ gives the adjoint equation | PROVED; In [16] | `python-field-theory.json`, checks `grassmann_euler_lagrange_psi_variation` and `commuting_euler_lagrange_psi_variation`; `wolfram-field-theory.json`, checks `EL_Psi_G` and `EL_Psi_C` |
| the adjoint equation is the Dirac conjugate of the field equation | PROVED; In [16] | `python-field-theory.json`, checks `grassmann_adjoint_equation_is_conjugate` and `commuting_adjoint_equation_is_conjugate`; `wolfram-field-theory.json`, checks `adjoint_equation_is_Dirac_conjugate_G` and `adjoint_equation_is_Dirac_conjugate_C` |

### 7.22 The equations in the author's metric: explicit, block and evolution forms

**The explicit form.** Since $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$, the Dirac operator is $\gamma^\mu D_\mu\Psi = \sum_a\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi + 3H\gamma^{(x_8)}\Psi$, and the field equation in the author's metric reads

$$
\frac{1}{e^{a_4}\sin^{1/6}z}\sum_{i=1}^{3}\gamma^{(x_i)}\partial_i\Psi + \gamma^{(x_4)}\partial_4\Psi + \frac{e^{a_4}}{\sin^{1/6}z}\sum_{t=5}^{7}\gamma^{(x_t)}\partial_t\Psi + \tan z\,\gamma^{(x_8)}\partial_8\Psi + 3H\gamma^{(x_8)}\Psi = (m + \lambda S)\Psi
$$

(PROVED; Notebook 07b, In [17]; Wolfram checks `Dirac_operator_explicit_G` and `Dirac_operator_explicit_C`; formula record key `field_equation`). The coefficient $e^{a_4}\sin^{-1/6}z$ of the extra-time derivatives GROWS as the extra times deflate, while that of the 3-space derivatives shrinks.

**One component equation, read off the gamma tables.** Every frame gamma is a signed permutation matrix: row 1 of $\gamma^{(x_1)}, \gamma^{(x_2)}, \gamma^{(x_3)}, \gamma^{(x_4)}, \gamma^{(x_5)}, \gamma^{(x_6)}, \gamma^{(x_7)}, \gamma^{(x_8)}$ has its single entry in the columns $-16, +15, -14, -14, +15, +16, +9, +9$ (the sign of the entry and its column; the tables of Chapter 5, read from the record `Revision/algebra/gammas.json`). So the first of the 16 component equations is

$$
\frac{-\partial_1\Psi_{16} + \partial_2\Psi_{15} - \partial_3\Psi_{14}}{e^{a_4}\sin^{1/6}z} - \partial_4\Psi_{14} + \frac{e^{a_4}(\partial_5\Psi_{15} + \partial_6\Psi_{16} + \partial_7\Psi_9)}{\sin^{1/6}z} + \tan z\,\partial_8\Psi_9 + 3H\Psi_9 = (m + \lambda S)\Psi_1 .
$$

Notebook 07b prints this equation in its own symbols and the same equation read from the formula record (`Revision/theory/field-theory.json`, key `field_equation_components`), and checks that all 16 equations agree term by term (In [17]). Each equation contains four components, each with derivatives along two directions (here $\Psi_{16}$ along $x_1$ and $x_6$, $\Psi_{15}$ along $x_2$ and $x_5$, $\Psi_{14}$ along $x_3$ and $x_4$, $\Psi_9$ along $x_7$ and $x_8$), and the gravitational term $3H\Psi_B$ stands next to the hidden-direction derivative $\tan z\,\partial_8\Psi_B$ of the same component (Figure 07b.4).

**The chiral block form.** Split $\Psi$ into its upper half $\psi_-$ (components 1 to 8, where the chirality matrix $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)} = \mathrm{diag}(-I_8, I_8)$ is $-1$; Chapter 5) and its lower half $\psi_+$ (components 9 to 16, $\Gamma = +1$). Every frame gamma anticommutes with $\Gamma$, and therefore has the block form

$$
\gamma^{(a)} = \begin{pmatrix}0 & \bar\tau_a\\ \tau_a & 0\end{pmatrix}
$$

with $8\times8$ blocks $\bar\tau_a$ (upper right) and $\tau_a$ (lower left); for the hidden direction $\bar\tau_{x_8} = \tau_{x_8} = I_8$. (Why: write $\gamma^{(a)}$ in $8\times8$ blocks $P, Q, R, T$; then $\Gamma\gamma^{(a)} = \begin{pmatrix}-P & -Q\\ R & T\end{pmatrix}$ and $\gamma^{(a)}\Gamma = \begin{pmatrix}-P & Q\\ -R & T\end{pmatrix}$, and $\Gamma\gamma^{(a)} = -\gamma^{(a)}\Gamma$ forces $P = 0$ and $T = 0$.) A block matrix times the column $(\psi_-, \psi_+)$ gives $(\bar\tau_a\psi_+, \tau_a\psi_-)$: the upper rows see only the lower half. The term $V\Psi$ keeps each half in its own rows. So the field equation is the pair

$$
\sum_a\frac{1}{f_a}\bar\tau_a\,\partial_a\psi_+ + 3H\psi_+ = V\psi_-,\qquad \sum_a\frac{1}{f_a}\tau_a\,\partial_a\psi_- + 3H\psi_- = V\psi_+ :
$$

the derivatives and the gravitational term of one half are balanced by the mass term of the other half (PROVED; Notebook 07b, In [19]; Wolfram check `block_form`; formula record key `field_equation_blocks`).

**The evolution form.** Write the explicit equation with the $x_4$ term separately ($f_4 = 1$) and solve it for $\partial_4\Psi$, line by line:

$$
\gamma^{(x_4)}\partial_4\Psi + \sum_{a\neq x_4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi + 3H\gamma^{(x_8)}\Psi = V\Psi
$$

(the field equation);

$$
\gamma^{(x_4)}\partial_4\Psi = V\Psi - \sum_{a\neq x_4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - 3H\gamma^{(x_8)}\Psi
$$

(every other term moved to the right side);

$$
\partial_4\Psi = -\gamma^{(x_4)}\Big[V\Psi - \sum_{a\neq x_4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - 3H\gamma^{(x_8)}\Psi\Big]
$$

(multiplied from the left by $-\gamma^{(x_4)}$, using $-\gamma^{(x_4)}\gamma^{(x_4)} = 1$ because $(\gamma^{(x_4)})^2 = \eta_{44} = -1$). So the time derivative of every component is fixed by the field and its derivatives along the other seven directions at the same time $x_4$: the slices $x_4 = $ const are **non-characteristic** (PROVED; Notebook 07b, In [19]; Wolfram checks `evolution_form_G` and `evolution_form_C`). Scope, from the Revision scope record: this does NOT make the initial-value problem well posed. For data that depend on the extra times the growth rates of the modes have no upper bound (Section 7.5; `Revision/theory/reports/python-scope.json`, check `extra_time_growth_rates_unbounded`), so small changes of the data can grow without limit in any time; Chapter 8 treats this.

### 7.23 Non-triviality [1] and [2], their exact scope, and an exact family of solutions

**The author's requirement.** The author asked that the Lagrangians of both fields be **non-trivial**: their Euler-Lagrange equations must always contain nonzero contributions from gravity through the canonical spin connection, unless space-time is flat 4+4 space ([1] for dirac16complex, [2] for dirac16complex00), and must be self-consistent.

**Theorem (non-triviality [1] and [2] in the diagonal frame).** Hypotheses: the author's metric with $H > 0$ and $0 < z < \pi/2$; any function $a_4(x_4)$, a constant one included; real $m$ and $\lambda$; the diagonal frame and its canonical spin connection; a field $\Psi$ of either statistics that is not identically zero. Then the field-equation residual computed with the spin connection minus the one computed with $\Omega_\mu = 0$ is

$$
\gamma^\mu\Omega_\mu\Psi = 3H\gamma^{(x_8)}\Psi \neq 0 .
$$

*Proof.* The difference is $\gamma^\mu(D_\mu - \partial_\mu)\Psi = \gamma^\mu\Omega_\mu\Psi$ by the definition of $D_\mu$, and $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ by Section 7.18. The matrix $\gamma^{(x_8)}$ is a signed permutation matrix with $(\gamma^{(x_8)})^2 = 1$, so every component of $\gamma^{(x_8)}\Psi$ is $\pm$ a component of $\Psi$, and $3H\gamma^{(x_8)}\Psi = 0$ forces $\Psi = 0$ when $H > 0$. $\square$ (PROVED; Notebook 07b, In [20], checks the difference in all 16 components for both statistics.) Moreover, $\Omega_\mu$ vanishes for all $\mu$ only if $a_4' = 0$ AND $H = 0$, because each of its 12 nonzero components is $a_4'$ or $H$ times a factor that never vanishes; $H = 0$ is not a member of the author's family (it is a degenerate limit in which $g_{11}$ and $g_{55}$ go to 0 and $g_{88}$ to infinity), and the metric is curved for every $H > 0$, since $R^{x_8}{}_{x_8} = -6H^2$ (the checks are listed in the table at the end of this section).

**The exact scope of the theorem.** The value $3H\gamma^{(x_8)}$ belongs to the diagonal frame and to the field variables $\Psi$; read without these hypotheses the theorem would overstate [1] and [2]. The Revision record states, and its scope reports verify exactly:

- In another frame of the same metric, boosted in the $(x_4, x_8)$ plane with the rapidity $6Hx_4 + b_0$, the term $\gamma^\mu\Omega_\mu$ vanishes identically.
- Within the diagonal frame the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it (derived below).
- The deflation contributes nothing to $\gamma^\mu\Omega_\mu$: $a_4$ enters the field equation only through the frame factors $e^{\mp a_4}\sin^{-1/6}z$ of the derivative terms. And since the connection drops out of $\mathcal{L}$ (Section 7.20), the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian; $3H\gamma^{(x_8)} = \frac{1}{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$ is its volume-and-frame term.
- What is frame-independent: $\Omega_\mu$ itself vanishes in no frame, because its curvature is the Riemann tensor of the metric, which is not zero; and the frame factors enter every derivative term. In this qualified sense [1] and [2] hold; Chapter 8 discusses the frame dependence further.

**The rescaling, line by line.** Put $\Psi = \sin^{-1/2}z\,\chi$. Only the $x_8$ term of the Dirac operator acts on the factor $\sin^{-1/2}z$, so by the product rule

$$
\gamma^\mu D_\mu\Psi = \sin^{-1/2}z\,\gamma^\mu D_\mu\chi + \tan z\,\gamma^{(x_8)}\big(\partial_8\sin^{-1/2}z\big)\chi .
$$

The derivative is $\partial_8\sin^{-1/2}z = -\tfrac12\sin^{-3/2}z\cos z\cdot6H$ (the power rule and the chain rule with $dz/dx_8 = 6H$), so the last term is

$$
\frac{\sin z}{\cos z}\cdot\big(-3H\sin^{-3/2}z\cos z\big)\gamma^{(x_8)}\chi = -3H\sin^{-1/2}z\,\gamma^{(x_8)}\chi .
$$

And $\gamma^\mu D_\mu\chi = \gamma^\mu\partial_\mu\chi + 3H\gamma^{(x_8)}\chi$. The two $3H$ terms cancel:

$$
\gamma^\mu D_\mu\Psi = \sin^{-1/2}z\,\gamma^\mu\partial_\mu\chi .
$$

For $U = 0$ the equation for $\chi$ therefore has no spin-connection term. For $U = \frac{\lambda}{2}S^2$ the scalar density is $S[\Psi] = S[\chi]/\sin z$ (the factor is real), and the term becomes the $x_8$-dependent coupling $\lambda S[\chi]/\sin z$ in $\gamma^\mu\partial_\mu\chi = (m + \lambda S[\chi]/\sin z)\chi$.

**An exact family of solutions.** Look for solutions that depend only on the time $x_4$ and the hidden direction $x_8$, of the form $\Psi = \sin^\alpha z\,P(x_4)\,\chi_0$ with a constant column $\chi_0$, a number $\alpha$ and a $16\times16$ matrix function $P$. Take $\lambda = 0$. Line by line:

$$
\gamma^{(x_4)}\partial_4\Psi + \tan z\,\gamma^{(x_8)}\partial_8\Psi + 3H\gamma^{(x_8)}\Psi = m\Psi
$$

(the explicit equation; the derivatives along the other six directions vanish, which is why the result holds for EVERY $a_4$);

$$
\sin^\alpha z\,\big[\gamma^{(x_4)}P' + (6H\alpha + 3H)\gamma^{(x_8)}P\big]\chi_0 = m\sin^\alpha z\,P\chi_0
$$

(because $\tan z\,\partial_8\sin^\alpha z = \frac{\sin z}{\cos z}\,\alpha\sin^{\alpha - 1}z\cos z\cdot6H = 6H\alpha\sin^\alpha z$);

$$
P' = -\gamma^{(x_4)}\big(m - 3H(2\alpha + 1)\gamma^{(x_8)}\big)P = MP,\qquad M = -m\gamma^{(x_4)} + 3H(2\alpha + 1)\gamma^{(x_4)}\gamma^{(x_8)}
$$

(divide by $\sin^\alpha z$, require the bracket for every $\chi_0$, and multiply by $-\gamma^{(x_4)}$, using $(\gamma^{(x_4)})^2 = -1$). The matrix $M$ squares to a number: with $\beta = 3H(2\alpha + 1)$,

$$
M^2 = m^2(\gamma^{(x_4)})^2 - m\beta\big(\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_8)} + \gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_4)}\big) + \beta^2\gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_8)} = -m^2 + 0 + \beta^2 = k^2
$$

with $k^2 = 9H^2(2\alpha + 1)^2 - m^2$ (the middle bracket is $-\gamma^{(x_8)} + \gamma^{(x_8)} = 0$, because $\gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_4)} = -\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_8)} = \gamma^{(x_8)}$; the last product is $-\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_8)} = -(-1)(1) = 1$). Therefore

$$
P(x_4) = \cosh(kx_4) + \frac{\sinh(kx_4)}{k}M
$$

solves $P' = MP$ with $P(0) = 1$: $P' = k\sinh(kx_4) + \cosh(kx_4)M$ and $MP = \cosh(kx_4)M + \frac{\sinh(kx_4)}{k}k^2$, the same. Moreover $M^TC + CM = 0$ (from $(\gamma^{(x_4)})^TC = -C\gamma^{(x_4)}$ and $\gamma^{(x_4)}C = C\gamma^{(x_4)}$, $\gamma^{(x_8)}C = -C\gamma^{(x_8)}$), which gives $\frac{d}{dx_4}(P^TCP) = P^T(M^TC + CM)P = 0$, so $P^TCP = C$ and the scalar density $S = \sin^{2\alpha}z\,\chi_0^\dagger C\chi_0$ does not change with $x_4$ ($P$ is real) (PROVED; Notebook 07b, In [21]). Two members, with the illustration values $H = 1$, $m = 2$, $\chi_0 = e_1 + e_5$ (components 1 and 5 equal to 1):

- $\alpha = 0$: $k^2 = 9 - 4 = 5$, and $P$ grows like $e^{\sqrt5x_4}$. This is an $x_8$-independent growing mode, which exists without a boundary condition at $z = \pi/2$ whenever $m^2 < 9H^2$ (the scope record, table below). Its scalar density is $\chi_0^TC\chi_0 = 2C_{1,5} = -2$.
- $\alpha = -\tfrac12$: $2\alpha + 1 = 0$, $M = -m\gamma^{(x_4)}$, $k^2 = -m^2 = -4$, so $\cosh(kx_4) = \cos2x_4$ and $\sinh(kx_4)/k = \sin(2x_4)/2$: the solution oscillates. This is the rescaling $\Psi = \sin^{-1/2}z\,\chi$ above, in which the $3H$ term disappears. Its scalar density at $z = \pi/4$ is $-2/\sin z = -2\sqrt2 = -2.828427$.

Notebook 07b evaluates both members at $z = \pi/4$ for $x_4$ from 0 to 2 and finds $S = -2.000000$ and $-2.828427$, constant along $x_4$ (In [22], Figure 07b.5; COMPUTED). Put into the equation WITHOUT the term $3H\gamma^{(x_8)}\Psi$, the growing solution leaves the residual $3H\gamma^{(x_8)}\Psi$, whose largest component is $3H$ times the largest component of $\Psi$ (In [24], Figure 07b.6): the gravitational term is needed for the solution. These solutions are test points; at them the pressures vanish, so they are a weak test of the energy-momentum tensor, whose conservation is proved in general in Chapter 9.

**Where the statements of this section are verified** (the reports in the folder `Revision/theory/reports`):

| statement | status | where it is verified |
| --- | --- | --- |
| the gravitational term $3H\gamma^{(x_8)}\Psi$ of the field equation is nonzero, both statistics | PROVED; Notebook 07b, In [20] | `wolfram-field-theory.json`, checks `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00` |
| $\Omega_\mu = 0$ only for $a_4' = 0$ and $H = 0$; $H = 0$ degenerate; curved for every $H > 0$ | PROVED | `python-field-theory.json`, check `nontriviality_Omega_zero_iff_flat`; `wolfram-field-theory.json`, checks `Omega_vanishes_iff_a4prime_and_H_vanish`, `degenerate_at_H_0` and `never_flat_for_H_positive` |
| the boosted frame removes $\gamma^\mu\Omega_\mu$ | PROVED (quoted) | `wolfram-scope.json` and `python-scope.json`, check `boosted_frame_gammaOmega_vanishes` |
| the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it; the coupling $\lambda S[\chi]/\sin z$ | PROVED here | scope reports, checks `rescaling_removes_the_connection_term` and `rescaled_equation_quadratic_potential` |
| $\gamma^\mu\Omega_\mu$ does not see the deflation; the equations are those of the connection-free Lagrangian | PROVED (quoted) | scope reports, checks `gammaOmega_blind_to_the_deflation` and `connection_free_lagrangian_same_equations` |
| $\Omega_\mu$ vanishes in no frame | PROVED (quoted) | `wolfram-scope.json`, check `boosted_frame_curvature_nonzero`; `wolfram-field-theory.json`, check `spin_curvature_equals_Riemann` |
| the exact family of solutions, $M^2 = k^2$, $M^TC + CM = 0$ | PROVED; In [21] | `python-field-theory.json`, check `exact_solution_family_x4_x8` |
| growing $x_8$-independent modes without a boundary condition at $z = \pi/2$ when $m^2 < 9H^2$ | PROVED (quoted); In [21] | `python-scope.json`, check `good_sector_x8_independent_modes_without_boundary_condition` |

### 7.24 Example: Notebook 07b derives the field equations in the author's metric

Notebook 07b derives everything of Sections 7.18 to 7.23 exactly, with the computer doing every step of algebra that a person would do by hand. It reads the author's gammas and $C$ from the Revision record; builds the metric from its frame and checks $\sqrt{|g|} = \cos z$; computes the 25 Christoffel symbols, the 12 components of the spin connection and $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ direction by direction; writes the Lagrangian of both fields in an exact jet algebra (392 and 408 monomials); proves its reality, the total divergence and the absence of the connection; derives the 16 Euler-Lagrange equations of both statistics and compares them term by term with the formula record; checks the block and evolution forms, non-triviality, and the exact family of solutions. Every result that the Revision record also contains is checked against it. It draws six figures and ends with the line ALL 47 CHECKS PASSED (notebook 07b).

<!-- NOTEBOOK 07b -->

### 7.27 Line-by-line walk-through of Notebook 07b

The notebook has 25 code cells, In [1] to In [25]. This section explains every line of every one of them, with the conventions of Section 7.9; every caption is printed in full under its figure in Section 7.26.

**In [1], the set-up cell.** It is the set-up cell of Notebook 07d with the one line `NOTEBOOK_ID = "07b"`; its first part repeats the complete run instructions of Section 7.25 as comment lines, and its code is explained line by line in Section 7.9. **Out [1]:** `Set-up of notebook 07b complete: repository folder found, helpers defined.`

**In [2]: the gammas and $C$ from the Revision record.**

```python
import contextlib  # redirect printed text into a buffer
import io  # an in-memory text file (the buffer)
import re  # regular expressions: used to read the Wolfram formula record

import numpy as np  # numbers for the plots
import sympy as sp  # exact algebra

check_of_the_setup = check  # the helper check of the set-up cell


def check(condition, name, record=None):
    """The set-up cell's check, with its PASS line and its "reproduces" line
    printed by ONE print call, so that Jupyter delivers them together."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # collect what check prints
        check_of_the_setup(condition, name, record)
    print(buffer.getvalue(), end="")  # and print it in one piece
```

The modules (as in Notebook 07d; `re` is used here to read formulas and numbers from the record's texts) and the same wrapper of `check` that prints a PASS line and its "reproduces" line in one piece (Section 7.9, In [2]).

```python
GAMMAS = "Revision/algebra/gammas.json"
FORMULAS = "Revision/theory/field-theory.json"
PYREP = "Revision/theory/reports/python-field-theory.json"
WLREP = "Revision/theory/reports/wolfram-field-theory.json"
SCOPE = "Revision/theory/reports/python-scope.json"
```

The repository paths of the five Revision files the notebook reads: the gammas, the formula record of the Wolfram verifier, the sympy and the Wolfram field-theory reports, and the sympy scope report.

```python
def revision_check(report, name):
    """The check called name of the Revision report (a JSON file): a dictionary
    with its name, verdict and detail; stops if it is missing or not PASS."""
    data = json.loads(repository_file(report).read_text(encoding="utf-8"))
    found = [item for item in data["checks"] if item["name"] == name]
    if len(found) != 1 or found[0]["verdict"].upper() != "PASS":
        raise ValueError(f"{name} is not a passing check of {report}")
    return found[0]


def reproduces(report, name):
    """The text "<report>, check <name>" for a PASS line, after making sure that
    the Revision report contains the check name with the verdict PASS."""
    revision_check(report, name)
    return f"{report}, check {name}"
```

`revision_check` returns the entry of a named check of a report and stops if it is missing or does not pass; `reproduces` uses it and returns the text for the "reproduces" line. Both are explained in Section 7.9 (In [2] of Notebook 07d).

```python
fixture = json.loads(repository_file(GAMMAS).read_text(encoding="utf-8"))
G = [sp.Matrix(g) for g in fixture["gamma"]]  # gamma^(x1) .. gamma^(x8), integers
C = sp.Matrix(fixture["C"])  # the author's sigma16
ETA = [1, 1, 1, -1, -1, -1, -1, 1]  # eta in the order x1 .. x8
I16, Z16 = sp.eye(16), sp.zeros(16, 16)
SAB = [[(G[a] * G[b] - G[b] * G[a]) / 4 for b in range(8)] for a in range(8)]
X4, X8 = 3, 7  # list positions of the time x4 and of the hidden direction x8
NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
```

The gammas are read as exact sympy matrices: `G[0]` to `G[7]` are $\gamma^{(x_1)}$ to $\gamma^{(x_8)}$, `C` is $C$. `ETA` is $\eta$ in the order $x_1, \dots, x_8$; `I16` and `Z16` are the $16\times16$ identity and zero matrices. `SAB[a][b]` is the spin generator $S^{ab} = \tfrac14(\gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)})$, built for all 64 pairs with a nested list comprehension. `X4, X8 = 3, 7` are the list positions of $x_4$ and $x_8$ (positions count from 0), and `NAMES` the printed names of the eight coordinates.

```python
clifford = all(G[a] * G[b] + G[b] * G[a] == 2 * (ETA[a] if a == b else 0) * I16
               for a in range(8) for b in range(8))
check(clifford, "{gamma^a, gamma^b} = 2 eta^ab I16 for all 64 pairs",
      record=reproduces(PYREP, "clifford_relations"))
c_ok = (C == G[7] * G[0] * G[1] * G[2] and C.T == C and C * C == I16
        and all((C * g).T == -(C * g) for g in G))
check(c_ok, "C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3), symmetric, C^2 = 1, "
      "every C gamma^a antisymmetric", record=reproduces(PYREP, "C_properties"))
```

`clifford` is true when $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}I_{16}$ for all 64 pairs (the expression `(ETA[a] if a == b else 0)` is $\eta^{ab}$). `c_ok` checks $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$, $C^T = C$, $C^2 = 1$ and that every $C\gamma^{(a)}$ is antisymmetric. **Out [2]:** two PASS lines with their "reproduces" lines (`clifford_relations` and `C_properties` of the sympy report).

**In [3]: the coefficient ring.**

```python
E, s, c = sp.symbols("E s c", positive=True)  # e^a4, sin(z)^(1/6), cos z
A1, A2, A3 = sp.symbols("A1 A2 A3", real=True)  # 1st, 2nd, 3rd derivative of a4
H = sp.Symbol("H", positive=True)  # the author's constant
m, lam = sp.symbols("m lambda", real=True)  # the mass and the coupling
```

The symbols of Section 7.18: `E`, `s`, `c` (positive), `A1`, `A2`, `A3` (the first three derivatives of $a_4$), `H` (positive), and `m`, `lam` ($\lambda$; the name `lambda` is reserved in Python).

```python
def cd(expression, mu):
    """The derivative of a ring expression along coordinate mu (0 .. 7)."""
    expression = sp.sympify(expression)
    if mu == X4:
        return (sp.diff(expression, E) * E * A1 + sp.diff(expression, A1) * A2
                + sp.diff(expression, A2) * A3)
    if mu == X8:
        return (sp.diff(expression, s) * H * c / s**5
                + sp.diff(expression, c) * (-6 * H * s**6))
    return sp.Integer(0)  # nothing depends on x1, x2, x3, x5, x6, x7
```

`cd(expression, mu)` differentiates a ring expression along the coordinate at list position `mu`. Along $x_4$: by the chain rule, through $E$ ($\partial_4E = EA_1$), through $A_1$ ($\partial_4A_1 = A_2$) and through $A_2$ ($\partial_4A_2 = A_3$). Along $x_8$: through $s$ ($\partial_8s = Hc/s^5$) and through $c$ ($\partial_8c = -6Hs^6$). Along every other coordinate: 0.

```python
def is_zero(expression):
    """Exact test: the numerator vanishes after c^2 -> 1 - s^12."""
    numerator, _ = sp.fraction(sp.together(sp.sympify(expression)))
    numerator = sp.expand(numerator)
    if numerator == 0:
        return True
    remainder = sp.rem(sp.Poly(numerator, c), sp.Poly(c**2 - 1 + s**12, c))
    return sp.expand(remainder.as_expr()) == 0
```

`is_zero(expression)` decides exactly whether a ring expression is zero. `sp.together` brings it to one fraction and `sp.fraction` returns its numerator and denominator; the numerator is multiplied out. If it is not already 0, it is divided as a polynomial in $c$ by $c^2 - 1 + s^{12}$ (`sp.rem` gives the remainder of the division); the remainder no longer contains $c^2$, and it vanishes exactly when the expression is zero.

```python
x4, x8 = sp.symbols("x4 x8", real=True)
a4 = sp.Function("a4")(x4)  # the free function of the metric
z = 6 * H * x8


def to_physical(expression):
    """Ring symbols -> the functions they stand for."""
    return sp.sympify(expression).subs(
        {E: sp.exp(a4), s: sp.sin(z) ** sp.Rational(1, 6), c: sp.cos(z),
         A1: a4.diff(x4), A2: a4.diff(x4, 2), A3: a4.diff(x4, 3)})
```

The physical variables: `x4`, `x8`, the unknown function $a_4(x_4)$ and $z = 6Hx_8$. `to_physical` replaces the ring symbols by the functions they stand for.

```python
rules_ok = all(
    sp.simplify(to_physical(cd(v, mu)) - sp.diff(to_physical(v), variable)) == 0
    for v in (E, s, c, A1, A2) for mu, variable in ((X4, x4), (X8, x8)))
check(rules_ok, "the derivative rules of the ring agree with sympy's derivatives")
check(is_zero(c**2 + s**12 - 1) and not is_zero(c) and not is_zero(s - c),
      "the exact zero test: c^2 + s^12 - 1 is zero, c and s - c are not")
```

The first check compares, for the five symbols $E, s, c, A_1, A_2$ and the two coordinates, the ring derivative put back into functions with sympy's own derivative of the functions. The second checks the zero test on three examples: $c^2 + s^{12} - 1$ is zero, $c$ and $s - c$ are not. **Out [3]:** two PASS lines.

**In [4]: the metric and the volume factor.**

```python
f = [E * s] * 3 + [sp.Integer(1)] + [s / E] * 3 + [c / s**6]  # the frame factors
g = [ETA[a] * f[a] ** 2 for a in range(8)]  # the diagonal metric entries
sqrt_g = sp.prod(f)  # the volume factor
third = sp.sin(z) ** sp.Rational(1, 3)
author = ([sp.exp(2 * a4) * third] * 3 + [-1] + [-sp.exp(-2 * a4) * third] * 3
          + [sp.cot(z) ** 2])  # the author's metric, typed from Revision/SPEC.md
check(all(sp.simplify(to_physical(g[a]) - author[a]) == 0 for a in range(8)),
      "the diagonal frame reproduces the author's metric entry by entry",
      record=reproduces(PYREP, "metric_from_vielbein_equals_SPEC"))
say(f"sqrt|g| = {sqrt_g} (ring) = {to_physical(sqrt_g)}")
check(sqrt_g == c, "sqrt|g| = cos z, independent of x4",
      record=reproduces(WLREP, "sqrt_det_g_is_cos_z"))
```

`f` is the list of the eight frame factors (`[E * s] * 3` repeats a one-entry list three times), `g` the diagonal metric entries $\eta_{aa}f_a^2$, and `sqrt_g` their product $\sqrt{|g|}$ (`sp.prod`). `author` is the author's metric typed from Revision/SPEC.md. The first check compares the eight entries; the `say` line prints the volume factor in the ring and as a function; the second check requires it to be $c$. **Out [4]:** two PASS lines with "reproduces" lines and `sqrt|g| = c (ring) = cos(6*H*x8)`.

**In [5]: reading the formula record.**

```python
record = {item["key"]: item["wl"] for item in
          json.loads(repository_file(FORMULAS).read_text(encoding="utf-8"))["formulas"]}
a4x, A1w = sp.symbols("a4x A1w", real=True)  # a4(x4) and a4'(x4) in the record
```

`record` is a dictionary from the keys of the formula record `Revision/theory/field-theory.json` to their Wolfram-language texts (the field `wl` of each entry). `a4x` and `A1w` are symbols for $a_4(x_4)$ and $a_4'(x_4)$ as they appear in those texts.

```python
def from_wolfram(text):
    """Read a Wolfram InputForm text of the formula record into sympy."""
    t = text.replace("Derivative[1][a4][x4]", "A1w").replace("a4[x4]", "a4x")
    t = re.sub(r'dd\["x(\d)",\s*Psi\[(\d+)\]\]', r"d\1_\2", t)  # d_a Psi_B
    t = re.sub(r"Psi\[(\d+)\]", r"P\1", t)  # Psi_B
    for name in ("Sin", "Cos", "Tan", "Cot", "Sec", "Csc"):
        t = t.replace(name + "[", name.lower() + "(")
    t = t.replace("[", "(").replace("]", ")").replace("{", "[").replace("}", "]")
    t = t.replace("^", "**")
    names = {"E": sp.E, "H": H, "x8": x8, "a4x": a4x, "A1w": A1w}
    for symbol in set(re.findall(r"\b(d\d_\d+|P\d+)\b", t)):
        names[symbol] = sp.Symbol(symbol)
    return sp.sympify(t, locals=names)
```

`from_wolfram(text)` turns a Wolfram-language text into a sympy expression in five steps: the derivative and the function $a_4$ are replaced by the two symbols; a regular expression replaces each derivative `dd["x5", Psi[15]]` by the name `d5_15` (the pattern `(\d)` captures a digit and `\1`, `\2` put the captured parts back); each `Psi[9]` becomes `P9`; the function names `Sin` ... `Csc` become `sin` ... `csc`; square brackets become round ones, braces (Wolfram lists) square ones (Python lists), and `^` becomes `**`. The dictionary `names` tells sympy what each name means; the loop adds a plain symbol for every derivative name and component name found in the text (`set(...)` removes repetitions). `sp.sympify` reads the result.

```python
RING = {sp.sin(z): s**6, sp.cos(z): c, sp.tan(z): s**6 / c, sp.cot(z): c / s**6,
        sp.sec(z): 1 / c, sp.csc(z): 1 / s**6, sp.csc(2 * z): 1 / (2 * s**6 * c)}


def to_ring(expression):
    """A record formula in the ring symbols E, s, c, A1."""
    return sp.sympify(expression).subs(a4x, sp.log(E)).subs(A1w, A1).subs(RING)
```

`RING` replaces the trigonometric functions of $z$ by ring expressions: $\sin z = s^6$, $\cos z = c$, $\tan z = s^6/c$, $\cot z = c/s^6$, $\sec z = 1/c$, $\csc z = 1/s^6$ and $\csc 2z = 1/(2s^6c)$ (because $\sin 2z = 2\sin z\cos z$). `to_ring` puts a record formula into the ring: $a_4 \to \ln E$ (so $e^{a_4} \to E$), $a_4' \to A_1$, and the replacements of `RING`.

```python
frame_record = from_wolfram(record["vielbein_diagonal"])
say(f"record vielbein_diagonal in the ring: {[to_ring(v) for v in frame_record]}")
check(all(is_zero(to_ring(v) - f[a]) for a, v in enumerate(frame_record))
      and is_zero(to_ring(from_wolfram(record["sqrt_det_g"])) - sqrt_g),
      "the frame factors and sqrt|g| equal the formula record",
      record=f"{FORMULAS}, formulas vielbein_diagonal and sqrt_det_g")
```

The record's frame factors (key `vielbein_diagonal`) are put into the ring and printed; the check compares each with our `f[a]` and the record's volume factor with ours. The `record=` text names the record file and the two formula keys. **Out [5]:** `record vielbein_diagonal in the ring: [E*s, E*s, E*s, 1, s/E, s/E, s/E, c/s**6]` and the PASS line with its "reproduces" line.

**In [6]: Figure 07b.1.**

```python
times = np.linspace(0.0, 3.0, 301)  # x4 from 0 to 3 (H = 1, A = 1: a4 = x4)
warp = np.sin(np.pi / 4) ** (1 / 6)  # sin^(1/6) z at z = pi/4
angles = np.linspace(0.01, np.pi / 2 - 0.01, 300)  # z inside (0, pi/2)
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
left.semilogy(times, np.exp(times) * warp, label="3-space $e^{a_4}\\sin^{1/6}z$")
left.semilogy(times, np.exp(-times) * warp, "--",
              label="extra times $e^{-a_4}\\sin^{1/6}z$")
left.semilogy(times, np.exp(times) * np.exp(-times) * warp**2, ":", color="black",
              label="their product")
left.set_xlabel("time $x_4$ (with $a_4 = x_4$)")
left.set_ylabel("scale factor")
left.set_title("Inflation and deflation at $z = \\pi/4$")
left.legend(fontsize=8)
right.plot(angles, np.sin(angles) ** (1 / 6), label="$\\sin^{1/6}z$")
right.plot(angles, np.cos(angles), "--", label="$\\sqrt{|g|} = \\cos z$")
right.plot(angles, 1 / np.tan(angles), ":", label="$f_8 = \\cot z$")
right.set_ylim(0, 3)
right.set_xlabel("$z = 6Hx_8$")
right.set_ylabel("value")
right.set_title("Dependence on the hidden direction")
right.legend(fontsize=8)
fig.tight_layout()
save_figure(fig, "scale_factors",
...)
```

`times` is $x_4$ from 0 to 3 (with $H = 1$, $A = 1$ the history is $a_4 = x_4$); `warp` is $\sin^{1/6}z$ at $z = \pi/4$; `angles` is $z$ from just above 0 to just below $\pi/2$. The left panel draws, on a logarithmic axis, the scale factor of 3-space $e^{x_4}\sin^{1/6}z$, that of the extra times $e^{-x_4}\sin^{1/6}z$ and their product; the right panel draws $\sin^{1/6}z$, $\cos z$ and $\cot z$ against $z$, with the vertical range cut at 3 because $\cot z$ grows without bound near $z = 0$. **What Figure 07b.1 shows.** On the logarithmic axis the 3-space factor is a rising straight line and the extra-time factor a falling one: exponential inflation and exponential deflation, with a constant product. On the right, $\sin^{1/6}z$ rises steeply near the tip $z = 0$ and is almost 1 elsewhere; the volume factor $\cos z$ falls to 0 at $z = \pi/2$, where the frame factor $\cot z$ of the hidden direction also vanishes. The history $a_4 = x_4$ is an illustration chosen for the picture, not a result: every equation of the notebook holds for every $a_4(x_4)$.

**In [7]: the Christoffel symbols.**

```python
Gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]  # Gam[l][mu][nu]
for l in range(8):
    for mu in range(8):
        for nu in range(8):
            value = 0
            if l == nu:
                value += cd(g[l], mu)
            if l == mu:
                value += cd(g[l], nu)
            if mu == nu:
                value -= cd(g[mu], l)
            if value != 0:
                Gam[l][mu][nu] = sp.expand(value / (2 * g[l]))
```

`Gam[l][mu][nu]` is $\Gamma^\lambda{}_{\mu\nu}$, a three-index table of zeros to start with (`[sp.Integer(0)] * 8` is a list of eight zeros; the underscore `_` is a loop variable whose value is not used). The three `if` lines add the three terms of the diagonal formula of Section 7.18, and a nonzero result is divided by $2g_{\lambda\lambda}$ and multiplied out.

```python
nonzero = [(l, mu, nu) for l in range(8) for mu in range(8) for nu in range(mu, 8)
           if not is_zero(Gam[l][mu][nu])]
report("independent nonzero Christoffel symbols", len(nonzero))
for l, mu, nu in [(0, 0, 3), (4, 3, 4), (0, 0, 7), (7, 7, 7)]:
    say(f"Gamma^{NAMES[l]}_{NAMES[mu]}{NAMES[nu]} = {sp.factor(Gam[l][mu][nu])}")
```

`nonzero` lists the index triples with $\mu \le \nu$ (the symbols are symmetric in $\mu$ and $\nu$) whose symbol is not zero; its length is reported. Four of them are printed, factored with `sp.factor`.

```python
recorded = int(re.search(r"(\d+) independent nonzero",
                         revision_check(PYREP, "christoffel_symmetric_metric_"
                                        "compatible")["detail"]).group(1))
check(len(nonzero) == recorded == 25, "25 independent nonzero Christoffel symbols",
      record=reproduces(PYREP, "christoffel_symmetric_metric_compatible"))
listed = from_wolfram(record["christoffel_nonzero"])
check(len(listed) == 25 and all(is_zero(to_ring(v) - Gam[l - 1][mu - 1][nu - 1])
                                for l, mu, nu, v in listed),
      "every Christoffel symbol equals the formula record",
      record=f"{FORMULAS}, formula christoffel_nonzero")
```

`recorded` is the number that the detail text of the sympy check `christoffel_symmetric_metric_compatible` states ("25 independent nonzero"), read with a regular expression (`(\d+)` captures the digits) and turned into a whole number with `int`. The first check requires our count to equal it and 25. `listed` is the record's list of all nonzero symbols (key `christoffel_nonzero`), each a list $\lambda, \mu, \nu$, value with indices counted from 1; the second check compares each value with ours (`Gam[l - 1][mu - 1][nu - 1]` shifts to positions counted from 0). **Out [7]:** `RESULT independent nonzero Christoffel symbols = 25`, the four symbols `Gamma^x1_x1x4 = A1`, `Gamma^x5_x4x5 = -A1`, `Gamma^x1_x1x8 = H*c/s**6`, `Gamma^x8_x8x8 = -6*H*(c**2 + s**12)/(c*s**6)` (the values derived in Section 7.18; with $c^2 + s^{12} = 1$ the last is $-6H/(\sin z\cos z)$), and two PASS lines with their "reproduces" lines.

**In [8]: the canonical spin connection.**

```python
om = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]  # om[mu][a][b]
for mu in range(8):
    for a in range(8):
        for b in range(8):
            mixed = f[a] * ((cd(1 / f[b], mu) if a == b else 0) + Gam[a][mu][b] / f[b])
            om[mu][a][b] = sp.expand(ETA[a] * mixed)  # lowered with eta_aa
```

`om[mu][a][b]` is $\omega_{\mu ab}$: the formula $f_a(\delta_{ab}\partial_\mu(1/f_b) + \Gamma^a{}_{\mu b}/f_b)$ of Section 7.18 for the mixed connection, lowered with $\eta_{aa}$.

```python
antisymmetric = all(is_zero(om[mu][a][b] + om[mu][b][a])
                    for mu in range(8) for a in range(8) for b in range(8))
postulate = all(is_zero((cd(f[a], mu) if a == nu else 0) - Gam[a][mu][nu] * f[a]
                        + ETA[a] * om[mu][a][nu] * f[nu])
                for mu in range(8) for a in range(8) for nu in range(8))
check(antisymmetric and postulate, "omega_mu ab = -omega_mu ba and the vielbein "
      "postulate holds in all 512 components",
      record=reproduces(PYREP, "vielbein_postulate"))
```

`antisymmetric` checks $\omega_{\mu ab} + \omega_{\mu ba} = 0$ for all 512 index triples. `postulate` checks the vielbein postulate for the diagonal frame in all 512 components: $\partial_\mu e^a{}_\nu$ (nonzero only for $\nu = a$, where it is $\partial_\mu f_a$), minus $\Gamma^a{}_{\mu\nu}f_a$, plus $\omega_\mu{}^a{}_\nu f_\nu$ with $\omega_\mu{}^a{}_\nu = \eta_{aa}\omega_{\mu a\nu}$.

```python
pairs = [(mu, a, b) for mu in range(8) for a in range(8) for b in range(a + 1, 8)
         if not is_zero(om[mu][a][b])]
for mu, a, b in pairs:
    say(f"omega_{NAMES[mu]} ({NAMES[a]})({NAMES[b]}) = {sp.factor(om[mu][a][b])}")
listed = from_wolfram(record["omega_nonzero"])
check(len(pairs) == 12 and len(listed) == 12 and all(
    is_zero(to_ring(v) - om[mu - 1][a - 1][b - 1]) for mu, a, b, v in listed),
      "exactly 12 nonzero components, equal to the formula record",
      record=reproduces(WLREP, "omega_components"))
```

`pairs` lists the nonzero components with $a < b$, which are printed. `listed` is the record's list (key `omega_nonzero`); the check requires exactly 12 components, equal to the record's. **Out [8]:** a PASS line with its "reproduces" line, the twelve components (for example `omega_x1 (x1)(x4) = A1*E*s` and `omega_x5 (x4)(x5) = -A1*s/E`), and a second PASS line with its "reproduces" line (Wolfram check `omega_components`).

**In [9]: the spinor connection and $\gamma^\mu\Omega_\mu$.**

```python
Om = []  # Omega_mu, mu = x1 .. x8
for mu in range(8):
    M = sp.zeros(16, 16)
    for a in range(8):
        for b in range(a + 1, 8):
            if om[mu][a][b] != 0:
                M += om[mu][a][b] * SAB[a][b]
    Om.append(M.applyfunc(sp.expand))
```

`Om[mu]` is $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$, a $16\times16$ matrix, built for each of the eight directions and multiplied out entry by entry.

```python
gam = [G[a] / f[a] for a in range(8)]  # the coordinate gammas gamma^mu
alpha, beta, rest_zero = [], [], True
for mu in range(8):
    M = (gam[mu] * Om[mu]).applyfunc(sp.expand)  # gamma^mu Omega_mu, no sum
    alpha.append(sp.expand(-(M * G[X4]).trace() / 16))  # coefficient of gamma^(x4)
    beta.append(sp.expand((M * G[X8]).trace() / 16))  # coefficient of gamma^(x8)
    rest_zero = rest_zero and all(
        is_zero(v) for v in (M - alpha[-1] * G[X4] - beta[-1] * G[X8]))
```

`gam` holds the coordinate gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$. For each direction separately (no sum), `M` is $\gamma^\mu\Omega_\mu$, and it is written as $\alpha_\mu\gamma^{(x_4)} + \beta_\mu\gamma^{(x_8)}$. The two numbers come from **traces** (the trace of a matrix is the sum of its diagonal entries): because $\mathrm{tr}(\gamma^{(x_4)}\gamma^{(x_4)}) = -16$, $\mathrm{tr}(\gamma^{(x_8)}\gamma^{(x_8)}) = 16$ and $\mathrm{tr}(\gamma^{(x_4)}\gamma^{(x_8)}) = 0$, the trace of $M\gamma^{(x_4)}$ is $-16\alpha_\mu$ and the trace of $M\gamma^{(x_8)}$ is $16\beta_\mu$. `rest_zero` stays true only if nothing else is left over: every entry of $M - \alpha_\mu\gamma^{(x_4)} - \beta_\mu\gamma^{(x_8)}$ is zero.

```python
for mu in range(8):
    say(f"gamma^{NAMES[mu]} Omega_{NAMES[mu]} = ({alpha[mu]}) gamma^(x4) + "
        f"({beta[mu]}) gamma^(x8)")
listed = from_wolfram(record["gammaOmega_per_direction"])
check(rest_zero and all(is_zero(to_ring(al) - alpha[mu - 1])
                        and is_zero(to_ring(be) - beta[mu - 1])
                        for mu, al, be in listed),
      "per direction gamma^mu Omega_mu = alpha gamma^(x4) + beta gamma^(x8), equal "
      "to the formula record", record=f"{FORMULAS}, formula gammaOmega_per_direction")
```

The eight decompositions are printed. The check compares each pair $(\alpha_\mu, \beta_\mu)$ with the record's list (key `gammaOmega_per_direction`).

```python
total = sum((gam[mu] * Om[mu] for mu in range(8)), Z16)
check(all(is_zero(v) for v in (total - 3 * H * G[X8])),
      "gamma^mu Omega_mu = 3 H gamma^(x8) (summed over mu)",
      record=reproduces(PYREP, "gamma_mu_Omega_mu_equals_3H_gamma_x8"))
check(sp.expand(sum(alpha[0:3])) == sp.Rational(3, 2) * A1
      and sp.expand(sum(alpha[4:7])) == -sp.Rational(3, 2) * A1
      and sp.expand(sum(beta)) == 3 * H,
      "the x4 terms cancel (+3 A1/2 inflating, -3 A1/2 deflating), the six x8 "
      "terms add to 3 H",
      record=reproduces(PYREP, "time_terms_cancel_hidden_term_survives"))
```

`total` is the sum over $\mu$; the first check requires $3H\gamma^{(x_8)}$. The second checks the cancellation: the $\alpha$ of the three inflating directions (positions 0 to 2, `alpha[0:3]`) add to $\tfrac32A_1$, those of the three extra times (positions 4 to 6) to $-\tfrac32A_1$, and all $\beta$ add to $3H$. **Out [9]:** the eight lines `gamma^x1 Omega_x1 = (A1/2) gamma^(x4) + (H/2) gamma^(x8)` ... `gamma^x5 Omega_x5 = (-A1/2) gamma^(x4) + (H/2) gamma^(x8)` ..., with zeros for $x_4$ and $x_8$, and three PASS lines with their "reproduces" lines.

**In [10]: Figure 07b.2.**

```python
a_units = [float(sp.expand(v / A1)) if v != 0 else 0.0 for v in alpha]  # a4' units
b_units = [float(sp.expand(v / H)) if v != 0 else 0.0 for v in beta]  # H units
positions = np.arange(8)
fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9), sharey=True)
for ax, values, unit, title in [
        (left, a_units, "$a_4'$", "coefficient of $\\gamma^{(x_4)}$"),
        (right, b_units, "$H$", "coefficient of $\\gamma^{(x_8)}$")]:
    ax.bar(positions, values, color=["tab:blue"] * 3 + ["grey"] + ["tab:red"] * 3
           + ["grey"], label="one direction")
    ax.plot(positions, np.cumsum(values), "ko-", label="running sum")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(positions, [f"$x_{k}$" for k in range(1, 9)])
    ax.set_xlabel("direction $\\mu$ (blue 3-space, red extra times)")
    ax.set_title(f"{title} (units of {unit})")
    ax.legend(fontsize=8, loc="upper left")
left.set_ylabel("coefficient")
fig.tight_layout()
save_figure(fig, "gamma_omega_per_direction",
...)
```

`a_units` and `b_units` are the coefficients in units of $a_4'$ and of $H$ (the zeros of $x_4$ and $x_8$ become 0.0). Two panels with a shared vertical axis (`sharey=True`); the loop draws in each a bar chart with blue bars for 3-space, grey for $x_4$ and $x_8$ and red for the extra times, and the **running sum** (`np.cumsum`, the sum of the first one, two, three, ... values) as black dots joined by lines. **What Figure 07b.2 shows.** On the left the bars are $+\tfrac12$ (blue) and $-\tfrac12$ (red): the running sum climbs to $\tfrac32$ and falls back to 0, the time terms cancel. On the right all six bars are $+\tfrac12$ and the running sum ends at 3: $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$.

**In [11]: why the connection drops out of $\mathcal{L}$ but not out of the equation.**

```python
anti = all(all(is_zero(v) for v in (gam[mu] * Om[mu] + Om[mu] * gam[mu]))
           for mu in range(8))
check(anti, "{gamma^mu, Omega_mu} = 0 for each mu: the connection drops out of L",
      record=reproduces(PYREP, "anticommutator_gamma_Omega_vanishes"))
divergence = sum((((sqrt_g * gam[mu]).applyfunc(lambda v: cd(v, mu)))
                  for mu in range(8)), Z16) / (2 * sqrt_g)
check(all(is_zero(v) for v in (divergence - 3 * H * G[X8])),
      "(1/(2 sqrt|g|)) d_mu (sqrt|g| gamma^mu) = 3 H gamma^(x8)",
      record=reproduces(PYREP, "divergence_of_sqrtg_gamma"))
```

`anti` checks $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ for each direction. `divergence` is $\frac{1}{2\sqrt{|g|}}\sum_\mu\partial_\mu(\sqrt{|g|}\gamma^\mu)$: `applyfunc(lambda v: cd(v, mu))` differentiates every entry of the matrix $\sqrt{|g|}\gamma^\mu$ along $x_\mu$. The second check requires $3H\gamma^{(x_8)}$. **Out [11]:** two PASS lines with their "reproduces" lines.

**In [12]: a jet algebra for both statistics.**

```python
CHI, PSI = 0, 1  # the two kinds: components of Psi^dagger and of Psi


def gen(kind, A, derivatives=()):
    """The generator: component A of chi (kind 0) or psi (kind 1), differentiated
    along the coordinate positions in derivatives."""
    return (kind, A, tuple(sorted(derivatives)))
```

A generator of the jet algebra is a triple `(kind, A, derivatives)`: kind 0 for a component $\chi_A = \Psi_A^*$ of $\Psi^\dagger$, kind 1 for a component $\psi_A$ of $\Psi$; `A` from 0 to 15; `derivatives` a sorted tuple of coordinate positions (empty for the value itself, `(3,)` for $\partial_4$). `gen` builds such a triple.

```python
def sort_sign(keys, odd):
    """Sorted tuple of generators and the sign; (None, 0) for a zero product."""
    items, sign = list(keys), 1
    for end in range(len(items) - 1, 0, -1):  # bubble sort, counting exchanges
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                sign = -sign
    if not odd:
        return tuple(items), 1  # commuting generators: no signs, squares allowed
    if any(items[i] == items[i + 1] for i in range(len(items) - 1)):
        return None, 0  # a repeated Grassmann generator: the product is zero
    return tuple(items), sign
```

`sort_sign(keys, odd)` sorts a tuple of generators with the bubble sort of Notebook 07a and counts the exchanges (Python compares triples entry by entry, so the order is first by kind, then by component, then by derivatives). For commuting generators (`odd` false) there is no sign and squares are allowed; for Grassmann generators a repeated generator gives the zero product, `(None, 0)`.

```python
class Jet:
    """An element of the jet algebra: self.terms maps monomials to coefficients."""

    def __init__(self, odd, terms=None):
        self.odd, self.terms = odd, {}
        for monomial, coefficient in (terms or {}).items():
            self.add(monomial, coefficient)

    def add(self, monomial, coefficient):
        total = sp.expand(self.terms.get(monomial, 0) + coefficient)
        if total == 0:
            self.terms.pop(monomial, None)
        else:
            self.terms[monomial] = total
```

The class `Jet`: an element remembers whether its generators are odd and holds a dictionary from monomials to ring coefficients. `add` adds a coefficient to a monomial, multiplies out and removes zeros, as in Notebook 07a.

```python
    def __add__(self, other):
        result = Jet(self.odd, self.terms)
        for monomial, coefficient in other.terms.items():
            result.add(monomial, coefficient)
        return result

    def __sub__(self, other):
        return self + other.times(-1)

    def times(self, factor):  # an ordinary (ring) factor
        return Jet(self.odd, {k: factor * v for k, v in self.terms.items()})
```

Addition, subtraction, and `times(factor)`, the multiplication by an ordinary ring factor.

```python
    def __mul__(self, other):
        result = Jet(self.odd)
        for k1, v1 in self.terms.items():
            for k2, v2 in other.terms.items():
                monomial, sign = sort_sign(k1 + k2, self.odd)
                if monomial is not None:
                    result.add(monomial, sign * v1 * v2)
        return result
```

The product: every term times every term, the joined monomial sorted with its sign.

```python
    def conj(self):
        result = Jet(self.odd)
        for monomial, coefficient in self.terms.items():
            images = [(1 - kind, A, d) for kind, A, d in reversed(monomial)]
            ordered, sign = sort_sign(images, self.odd)
            if ordered is not None:
                result.add(ordered, sign * sp.sympify(coefficient).subs(sp.I, -sp.I))
        return result
```

`conj` is the conjugation of Section 7.11: the monomial is reversed, each generator's kind is exchanged ($\chi_A \leftrightarrow \psi_A$, `1 - kind`) while its component and derivatives are kept, the result is sorted with its sign (for commuting generators no sign), and $i$ is replaced by $-i$ in the coefficient (all other symbols are real).

```python
    def lderiv(self, key):
        result = Jet(self.odd)
        for monomial, coefficient in self.terms.items():
            if key in monomial:
                p = monomial.index(key)
                factor = (-1) ** p if self.odd else monomial.count(key)
                result.add(monomial[:p] + monomial[p + 1:], factor * coefficient)
        return result

    def rderiv(self, key):
        if not self.odd:
            return self.lderiv(key)
        result = Jet(self.odd)
        for monomial, coefficient in self.terms.items():
            if key in monomial:
                p = monomial.index(key)
                factor = (-1) ** (len(monomial) - 1 - p)
                result.add(monomial[:p] + monomial[p + 1:], factor * coefficient)
        return result
```

`lderiv(key)` is the left derivative: for Grassmann generators the sign $(-1)^p$ of the position; for commuting generators the ordinary derivative, which brings down the power (`monomial.count(key)` is the number of times the generator occurs, the $n$ of $x^n \to nx^{n-1}$). `rderiv(key)` is the right derivative; for commuting generators it is the same as the left one.

```python
    def total(self, mu):
        result = Jet(self.odd)
        for monomial, coefficient in self.terms.items():
            derivative = cd(coefficient, mu)
            if derivative != 0:
                result.add(monomial, derivative)
            for p, (kind, A, d) in enumerate(monomial):
                raised = (kind, A, tuple(sorted(d + (mu,))))
                ordered, sign = sort_sign(monomial[:p] + (raised,) + monomial[p + 1:],
                                          self.odd)
                if ordered is not None:
                    result.add(ordered, sign * coefficient)
        return result

    def is_zero(self):
        return all(is_zero(v) for v in self.terms.values())
```

`total(mu)` is the total derivative $d/dx_\mu$ on jets: the coefficient is differentiated with `cd` (the explicit dependence on $x_4$ and $x_8$), and every generator of the monomial in turn gets the additional derivative $\mu$ (its derivative tuple grows by `mu`), with the product rule and the sign of sorting back. `is_zero` uses the exact zero test of In [3] on every coefficient.

```python
def column(odd, kind, derivatives=()):
    """The 16 generators of chi or psi (or of one of their derivatives)."""
    return [Jet(odd, {(gen(kind, A, derivatives),): 1}) for A in range(16)]


def matvec(M, v, odd):
    """The column M v."""
    out = [Jet(odd) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if M[i, j] != 0:
                out[i] = out[i] + v[j].times(M[i, j])
    return out


def vecmat(v, M, odd):
    """The row v M."""
    out = [Jet(odd) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if M[i, j] != 0:
                out[j] = out[j] + v[i].times(M[i, j])
    return out


def dot(row, col, odd):
    """The number row col (row first)."""
    result = Jet(odd)
    for x, y in zip(row, col):
        result = result + x * y
    return result


say("The jet algebra and the vector helpers are defined.")
```

Vector helpers: `column(odd, kind, derivatives)` is the list of the 16 generators of $\chi$ or $\psi$ (or of one of their derivatives) as elements; `matvec(M, v, odd)` is the column $Mv$, `vecmat(v, M, odd)` the row $vM$ (each skips the zero entries of the matrix), and `dot(row, col, odd)` the number $\sum_A\mathrm{row}_A\mathrm{col}_A$ with the row factor first. **Out [12]:** `The jet algebra and the vector helpers are defined.`

**In [13]: the Lagrangian of both fields.**

```python
def build(odd, connection):
    """Lagrangian, unsymmetrised Lagrangian, field-equation residual and pieces
    for one statistics (odd True: Grassmann) and one spinor connection."""
    psi, chi = column(odd, PSI), column(odd, CHI)
    psibar = vecmat(chi, C, odd)  # Psibar = Psi^dagger C
    Dpsi = [[x + y for x, y in zip(column(odd, PSI, (mu,)),
                                   matvec(connection[mu], psi, odd))]
            for mu in range(8)]
    Dpsibar = [[x - y for x, y in zip(vecmat(column(odd, CHI, (mu,)), C, odd),
                                      vecmat(psibar, connection[mu], odd))]
               for mu in range(8)]
```

`build(odd, connection)` builds everything for one statistics and one spinor connection (a list of eight matrices). `psi` and `chi` are the columns of generators; `psibar` is the row $\bar\Psi = \chi C$. `Dpsi[mu]` is $D_\mu\psi = \partial_\mu\psi + \Omega_\mu\psi$ and `Dpsibar[mu]` is $D_\mu\bar\Psi = \partial_\mu\chi\,C - \bar\Psi\Omega_\mu$, each a list of 16 elements.

```python
    K, Ku = Jet(odd), Jet(odd)
    for mu in range(8):
        forward = dot(psibar, matvec(gam[mu], Dpsi[mu], odd), odd)
        K = K + forward - dot(vecmat(Dpsibar[mu], gam[mu], odd), psi, odd)
        Ku = Ku + forward
    S = dot(psibar, psi, odd)
    potential = S.times(m) + (S * S).times(lam / 2)  # m S + (lambda/2) S^2
    L = (K.times(sp.Rational(1, 2)) - potential).times(sqrt_g)
    Lu = (Ku - potential).times(sqrt_g)
```

`K` collects $\sum_\mu(\bar\Psi\gamma^\mu D_\mu\psi - D_\mu\bar\Psi\gamma^\mu\psi)$ and `Ku` the unsymmetrised $\sum_\mu\bar\Psi\gamma^\mu D_\mu\psi$ (`forward` is the first product, computed once). `S` is $\bar\Psi\psi$, `potential` is $mS + \tfrac{\lambda}{2}S^2$. `L` is $\sqrt{|g|}(\tfrac12K - mS - \tfrac{\lambda}{2}S^2)$, `Lu` the unsymmetrised form.

```python
    dirac = [Jet(odd) for _ in range(16)]  # gamma^mu D_mu psi
    for mu in range(8):
        dirac = [x + y for x, y in zip(dirac, matvec(gam[mu], Dpsi[mu], odd))]
    V = Jet(odd, {(): m}) + S.times(lam)  # m + lambda S
    residual = [dirac[A] - V * psi[A] for A in range(16)]
    bar_residual = [Jet(odd)] * 16  # -(D_mu Psibar gamma^mu + V Psibar)
    for mu in range(8):
        bar_residual = [x - y for x, y in zip(bar_residual,
                                              vecmat(Dpsibar[mu], gam[mu], odd))]
    bar_residual = [x - V * y for x, y in zip(bar_residual, psibar)]
    return {"L": L, "Lu": Lu, "E": residual, "Ebar": bar_residual, "S": S,
            "psi": psi, "psibar": psibar, "dirac": dirac}
```

`dirac` is the column $\gamma^\mu D_\mu\psi$; `V` is the element $m + \lambda S$; `residual` is the column $\mathcal{E} = \gamma^\mu D_\mu\psi - V\psi$. `bar_residual` is the row $-(D_\mu\bar\Psi\gamma^\mu + V\bar\Psi)$. The function returns all pieces in a dictionary.

```python
STATS = {"grassmann": True, "commuting": False}  # statistics -> odd
fields = {name: build(odd, Om) for name, odd in STATS.items()}
kinds = {}
for name, data in fields.items():
    monomials = data["L"].terms
    kinetic = sum(1 for k in monomials if any(d for (_, _, d) in k))
    quartic = sum(1 for k in monomials if len(k) == 4)
    kinds[name] = (kinetic, len(monomials) - kinetic - quartic, quartic)
    report(f"monomials of L, {name}", f"{len(monomials)} = {kinetic} kinetic + "
           f"{kinds[name][1]} mass + {quartic} quartic")
```

`STATS` maps the two names to the switch `odd`. `fields` holds the pieces for both statistics with the canonical connection `Om`. For each, the monomials of $\mathcal{L}$ are sorted by type: kinetic if some generator carries a derivative (`any(d for (_, _, d) in k)` is true when a derivative tuple is not empty), quartic if the monomial has four generators, and mass otherwise. **Out [13]:** `RESULT monomials of L, grassmann = 392 = 256 kinetic + 16 mass + 120 quartic` and `RESULT monomials of L, commuting = 408 = 256 kinetic + 16 mass + 136 quartic`.

**In [14]: the counts against the record, and Figure 07b.3.**

```python
for name in STATS:
    detail = revision_check(PYREP, f"{name}_lagrangian_real")["detail"]
    recorded = int(re.search(r"\((\d+) monomials", detail).group(1))
    check(len(fields[name]["L"].terms) == recorded,
          f"{name}: L has {recorded} monomials, as recorded",
          record=reproduces(PYREP, f"{name}_lagrangian_real"))
check(kinds["grassmann"] == (256, 16, 120) and kinds["commuting"] == (256, 16, 136),
      "the difference is the 16 squares of the pairs in S^2 (136 - 120)")
```

For each statistics the number of monomials is read from the detail text of the record's reality check ("(392 monomials" and "(408 monomials") and compared. The last check is the difference of Section 7.20: 136 minus 120 quartic monomials, the 16 squares of the pairs.

```python
fig, ax = plt.subplots(figsize=(7.0, 4.2))
labels = ["dirac16complex\n(Grassmann)", "dirac16complex00\n(commuting)"]
bottoms = np.zeros(2)
for index, (part, colour) in enumerate([("kinetic", "tab:blue"), ("mass", "tab:green"),
                                        ("quartic", "tab:orange")]):
    values = np.array([kinds["grassmann"][index], kinds["commuting"][index]])
    ax.bar(labels, values, bottom=bottoms, color=colour, label=part, width=0.5)
    for x, (value, bottom) in enumerate(zip(values, bottoms)):
        ax.text(x, bottom + value / 2, str(value), ha="center", va="center")
    bottoms = bottoms + values
for x, total in enumerate(bottoms):
    ax.text(x, total + 6, f"total {int(total)}", ha="center")
ax.set_ylim(0, 520)  # room above the bars for the legend
ax.set_ylabel("number of monomials of $L$")
ax.set_title("The Lagrangian at one point, by type of term")
ax.legend(loc="upper center", ncol=3, fontsize=8)
save_figure(fig, "lagrangian_monomials",
...)
```

A **stacked bar chart**: for each field the bars of the three types are drawn on top of each other (`bottom=bottoms` starts each new bar where the previous one ended), the counts are written into the bars and the totals above them (`"\n"` in a label is a line break). **Out [14]:** three PASS lines (the first two with "reproduces" lines) and the figure. **What Figure 07b.3 shows.** The kinetic (blue) and mass (green) parts are equal for the two fields; the only difference is the quartic part (orange), 120 against 136: the 16 squares $(\bar\Psi_A\Psi_B)^2$ vanish for Grassmann numbers.

**In [15]: reality, the total divergence and the connection that drops out.**

```python
no_connection = [Z16] * 8  # Omega_mu = 0
for name, odd in STATS.items():
    data = fields[name]
    L, Lu = data["L"], data["Lu"]
    check((L.conj() - L).is_zero() and not (Lu.conj() - Lu).is_zero(),
          f"{name}: L is real, the unsymmetrised L_u is not",
          record=reproduces(PYREP, f"{name}_controls_not_vacuous"))
    current = Jet(odd)
    for mu in range(8):
        current = current + dot(data["psibar"], matvec(gam[mu], data["psi"], odd),
                                odd).times(sqrt_g).total(mu)
    check((L - Lu + current.times(sp.Rational(1, 2))).is_zero(),
          f"{name}: L = L_u - (1/2) d_mu (sqrt|g| Psibar gamma^mu Psi)",
          record=reproduces(PYREP, f"{name}_total_divergence_relation"))
    flat_connection = build(odd, no_connection)["L"]
    tag = "G" if odd else "C"
    check((L - flat_connection).is_zero(),
          f"{name}: L with Omega equals L with Omega = 0 in this metric",
          record=reproduces(WLREP, f"L_spin_connection_drops_out_{tag}"))
```

`no_connection` is the list of eight zero matrices ($\Omega_\mu = 0$). For each statistics: the first check requires $\mathcal{L}^* = \mathcal{L}$ and that the unsymmetrised form is not real (the control). `current` is $\sum_\mu\frac{d}{dx_\mu}\big(\sqrt{|g|}\,\bar\Psi\gamma^\mu\psi\big)$, built with the total derivative of the jet algebra; the second check is the relation $\mathcal{L} = \mathcal{L}_u - \tfrac12\,\cdot$ current of Section 7.20. `flat_connection` is the Lagrangian built with $\Omega_\mu = 0$; the third check requires it to equal $\mathcal{L}$. `tag` is `"G"` or `"C"`, the ending of the Wolfram check names. **Out [15]:** six PASS lines, each with its "reproduces" line.

**In [16]: the Euler-Lagrange equations.**

```python
def euler_lagrange_chi(L, A):
    """dL/dchi_A - d_mu dL/d(d_mu chi_A), left derivatives."""
    result = L.lderiv(gen(CHI, A))
    for mu in range(8):
        result = result - L.lderiv(gen(CHI, A, (mu,))).total(mu)
    return result


def euler_lagrange_psi(L, B):
    """dL/dpsi_B - d_mu dL/d(d_mu psi_B), right derivatives."""
    result = L.rderiv(gen(PSI, B))
    for mu in range(8):
        result = result - L.rderiv(gen(PSI, B, (mu,))).total(mu)
    return result
```

`euler_lagrange_chi(L, A)` is $\partial_L\mathcal{L}/\partial\chi_A - \sum_\mu\frac{d}{dx_\mu}\partial_L\mathcal{L}/\partial(\partial_\mu\chi_A)$ with left derivatives; `euler_lagrange_psi(L, B)` is the same for $\psi_B$ with right derivatives.

```python
for name, odd in STATS.items():
    data = fields[name]
    L, residual, psi = data["L"], data["E"], data["psi"]
    expected = matvec(C, residual, odd)  # C times the residual
    ok = all((euler_lagrange_chi(L, A) - expected[A].times(sqrt_g)).is_zero()
             for A in range(16))
    wrong = matvec(C, [residual[B] + psi[B].times(2 * m) for B in range(16)], odd)
    control = not (euler_lagrange_chi(L, 0) - wrong[0].times(sqrt_g)).is_zero()
    check(ok and control, f"{name}: varying Psi^dagger gives gamma^mu D_mu Psi = "
          "(m + lambda S) Psi in all 16 components (control m -> -m fails)",
          record=reproduces(PYREP, f"{name}_euler_lagrange_psibar_variation"))
    ok = all((euler_lagrange_psi(L, B) - data["Ebar"][B].times(sqrt_g)).is_zero()
             for B in range(16))
    check(ok, f"{name}: varying Psi gives D_mu Psibar gamma^mu = -(m + lambda S) "
          "Psibar", record=reproduces(PYREP, f"{name}_euler_lagrange_psi_variation"))
    conjugate_row = vecmat([x.conj() for x in residual], C, odd)
    check(all((conjugate_row[B] - data["Ebar"][B]).is_zero() for B in range(16)),
          f"{name}: the adjoint equation is the Dirac conjugate of the field equation",
          record=reproduces(PYREP, f"{name}_adjoint_equation_is_conjugate"))
```

For each statistics: `expected` is the column $C\mathcal{E}$; the first check requires the Euler-Lagrange expression of every $\chi_A$ to equal $\sqrt{|g|}(C\mathcal{E})_A$ (Steps 1 to 6 of Section 7.21), and, as a control, that the comparison with $m$ replaced by $-m$ fails (`wrong` adds $2m\psi$ to the residual; only component 0 is tested, which suffices to show the failure). The second check: the expressions for $\psi_B$ equal $\sqrt{|g|}$ times the adjoint residual. The third: the conjugate of the residual, as a row times $C$ (`conjugate_row`), equals the adjoint residual. **Out [16]:** six PASS lines, each with its "reproduces" line.

**In [17]: the equations written out in the author's metric.**

```python
for name, odd in STATS.items():
    data = fields[name]
    explicit = matvec(G[X8] * 3 * H, data["psi"], odd)  # 3 H gamma^(x8) psi
    for a in range(8):
        explicit = [x + y for x, y in zip(explicit, matvec(
            G[a] / f[a], column(odd, PSI, (a,)), odd))]
    tag = "G" if odd else "C"
    check(all((data["dirac"][A] - explicit[A]).is_zero() for A in range(16)),
          f"{name}: gamma^mu D_mu Psi = sum_a (1/f_a) gamma^(a) d_a Psi + 3 H "
          "gamma^(x8) Psi", record=reproduces(WLREP, f"Dirac_operator_explicit_{tag}"))
```

For each statistics `explicit` is the column $3H\gamma^{(x_8)}\psi + \sum_a\frac{1}{f_a}\gamma^{(a)}\partial_a\psi$; the check requires it to equal $\gamma^\mu D_\mu\psi$ in all 16 components.

```python
def as_sympy(element):
    """A linear jet element as a sympy expression in d<a>_<B> and P<B>."""
    total = 0
    for ((kind, B, d),), coefficient in element.terms.items():
        symbol = f"d{d[0] + 1}_{B + 1}" if d else f"P{B + 1}"
        total += coefficient * sp.Symbol(symbol)
    return total
```

`as_sympy(element)` turns a linear jet element into an ordinary sympy expression: each monomial has exactly one generator (the unpacking `((kind, B, d),)` requires this), which becomes the symbol `d<a>_<B>` for $\partial_a\Psi_B$ or `P<B>` for $\Psi_B$, counted from 1 like the record.

```python
ours = [as_sympy(x) for x in fields["grassmann"]["dirac"]]
theirs = [to_ring(from_wolfram(text.split("==")[0]))
          for text in record["field_equation_components"]]
say(f"equation 1, this notebook: {ours[0]} = V P1")
say(f"equation 1, formula record: {theirs[0]} = V P1")
check(len(theirs) == 16 and all(is_zero(x - y) for x, y in zip(ours, theirs)),
      "all 16 component equations equal the formula record term by term",
      record=f"{FORMULAS}, formula field_equation_components")
```

`ours` are our 16 Dirac-operator components, `theirs` the left sides of the record's 16 component equations (each text is split at `==` and its first part translated and put into the ring). The first equation is printed in both forms, and the check compares all 16 with the exact zero test. **Out [17]:** two PASS lines with their "reproduces" lines, the first equation twice (identical: `E*d5_15/s + E*d6_16/s + E*d7_9/s + 3*H*P9 - d4_14 + d8_9*s**6/c - d1_16/(E*s) + d2_15/(E*s) - d3_14/(E*s) = V P1`, the equation of Section 7.22 in ring symbols), and the third PASS line.

**In [18]: the coupling map, Figure 07b.4.**

```python
counts = np.zeros((16, 16), dtype=int)
tags = [["" for _ in range(16)] for _ in range(16)]
for a in range(8):
    for A in range(16):
        for B in range(16):
            if G[a][A, B] != 0:
                counts[A, B] += 1
                tags[A][B] += str(a + 1)
four_twos = all(np.count_nonzero(counts[A]) == 4 and counts[A].max() == 2
                for A in range(16))  # 4 components, each with 2 directions
check(four_twos and int(counts.sum()) == 128
      and not counts[:8, :8].any() and not counts[8:, 8:].any(),
      "each equation couples 4 components with 2 directions each, across the chiral "
      "halves")
```

`counts[A, B]` counts the directions $a$ whose gamma has a nonzero entry in row $A$, column $B$, that is the directions whose derivative of $\Psi_B$ appears in equation $A$; `tags[A][B]` collects their numbers as a text. The check: every row has 4 nonzero entries, each 2; 128 derivative terms in total ($8\times16$); and the two diagonal $8\times8$ blocks are empty (`counts[:8, :8]` is the upper left block): every equation couples the two chiral halves.

```python
fig, ax = plt.subplots(figsize=(7.4, 6.6))
image = ax.imshow(counts, cmap="Blues", vmin=0, vmax=2)
for A in range(16):
    for B in range(16):
        if tags[A][B]:
            ax.text(B, A, tags[A][B], ha="center", va="center", fontsize=7,
                    color="white" if counts[A, B] == 2 else "black")
ax.axhline(7.5, color="red", linewidth=1)
ax.axvline(7.5, color="red", linewidth=1)
ax.set_xticks(range(0, 16, 3), [str(k + 1) for k in range(0, 16, 3)])
ax.set_yticks(range(0, 16, 3), [str(k + 1) for k in range(0, 16, 3)])
ax.set_xlabel("component $B$ whose derivative appears")
ax.set_ylabel("equation $A$")
ax.set_title("Which derivatives $\\partial_a\\Psi_B$ enter equation $A$")
ax.grid(False)
fig.colorbar(image, ax=ax, ticks=[0, 1, 2], shrink=0.8,
             label="number of directions $a$")
save_figure(fig, "coupling_map",
...)
```

A heat map of `counts` in shades of blue, with the direction numbers written in (white on the darker squares) and red lines between rows 8 and 9 and columns 8 and 9 (`axhline(7.5)` lies between positions 7 and 8). **What Figure 07b.4 shows.** Each row has four coloured squares, each labelled with two direction numbers; the upper left and lower right quarters are empty: the equations of the upper half contain only the lower half of the field, and the other way round. The digit 8 marks the components that carry both $\tan z\,\partial_8$ and the term $3H$.

**In [19]: the chiral blocks and the evolution form.**

```python
blocks = {}  # direction name -> (tau-bar_a, tau_a)
for text in record["field_equation_blocks"]:
    # the Wolfram list {"x1", {{...}}, {{...}}} is the JSON list ["x1", [[...]], [[...]]]
    name, upper, lower = json.loads(text.replace("{", "[").replace("}", "]"))
    blocks[name] = (sp.Matrix(upper), sp.Matrix(lower))
GAMMA = sp.Matrix(fixture["Gamma"])  # the chirality matrix of Revision/algebra
Z8 = sp.zeros(8, 8)
blocks_ok = sorted(blocks) == NAMES and GAMMA == sp.diag(*([-1] * 8 + [1] * 8))
for a in range(8):
    upper, lower = blocks[NAMES[a]]
    blocks_ok = (blocks_ok and G[a][:8, :8] == Z8 and G[a][8:, 8:] == Z8  # zero
                 and G[a][:8, 8:] == upper and G[a][8:, :8] == lower)  # the blocks
blocks_ok = blocks_ok and blocks["x8"][0] == sp.eye(8) and blocks["x8"][1] == sp.eye(8)
check(blocks_ok, "Gamma = diag(-I8, I8); every gamma^(a) is block off-diagonal with the "
      "blocks of the formula record; tau-bar_x8 = tau_x8 = I8",
      record=reproduces(WLREP, "block_form"))
```

The record's key `field_equation_blocks` holds, for each direction, its name and its two $8\times8$ blocks as a Wolfram list; replacing braces by square brackets makes it a JSON list, which `json.loads` reads. `GAMMA` is the chirality matrix of the record, `Z8` the $8\times8$ zero matrix. The check requires: the eight direction names; $\Gamma = \mathrm{diag}(-I_8, I_8)$ (`sp.diag(*list)` builds a diagonal matrix from a list); for every gamma the two diagonal blocks zero and the off-diagonal blocks equal to the record's (`G[a][:8, 8:]` is the upper right block); and $\bar\tau_{x_8} = \tau_{x_8} = I_8$.

```python
for name, odd in STATS.items():
    data = fields[name]
    psi = data["psi"]
    V = Jet(odd, {(): m}) + data["S"].times(lam)  # m + lambda S
    others = matvec(3 * H * G[X8], psi, odd)  # 3 H gamma^(x8) Psi, then the sum
    for a in range(8):
        if a != X4:  # (1/f_a) gamma^(a) d_a Psi for the seven other directions
            others = [x + y for x, y in zip(others, matvec(
                G[a] / f[a], column(odd, PSI, (a,)), odd))]
    bracket = [V * psi[A] - others[A] for A in range(16)]  # the square bracket
    right = matvec(-G[X4], bracket, odd)  # R = -gamma^(x4) [ ... ]
    difference = [x - y for x, y in zip(column(odd, PSI, (X4,)), right)]  # d4 Psi - R
    left = matvec(G[X4], difference, odd)  # gamma^(x4) (d4 Psi - R)
    tag = "G" if odd else "C"
    check(all((left[A] - data["E"][A]).is_zero() for A in range(16)),
          f"{name}: the evolution form d4 Psi = R is the field equation "
          "(gamma^(x4) (d4 Psi - R) = E in all 16 components)",
          record=reproduces(WLREP, f"evolution_form_{tag}"))
```

For each statistics: `others` is $3H\gamma^{(x_8)}\psi + \sum_{a\neq x_4}\frac{1}{f_a}\gamma^{(a)}\partial_a\psi$, `bracket` is $V\psi - $ others, `right` is $R = -\gamma^{(x_4)}[\dots]$, `difference` is $\partial_4\psi - R$ and `left` is $\gamma^{(x_4)}(\partial_4\psi - R)$. The check requires `left` to equal the residual $\mathcal{E}$ in all 16 components: the evolution form is the field equation. **Out [19]:** three PASS lines with their "reproduces" lines.

**In [20]: non-triviality.**

```python
for name, odd in STATS.items():
    data = fields[name]
    without = build(odd, no_connection)["E"]  # residual with Omega = 0
    gravity = matvec(3 * H * G[X8], data["psi"], odd)
    ok = all((data["E"][A] - without[A] - gravity[A]).is_zero() for A in range(16))
    nonzero = all(len(gravity[A].terms) == 1 for A in range(16))
    number = "1_dirac16complex" if odd else "2_dirac16complex00"
    check(ok and nonzero, f"{name}: residual(Omega) - residual(Omega = 0) = 3 H "
          "gamma^(x8) Psi, nonzero in all 16 components",
          record=reproduces(WLREP, f"nontriviality_{number}"))
```

For each statistics, `without` is the residual computed with $\Omega_\mu = 0$ and `gravity` the column $3H\gamma^{(x_8)}\psi$. The check requires residual(with $\Omega$) minus residual(without) to equal `gravity` in all 16 components, and every component of `gravity` to be one nonzero monomial. **Out [20]:** two PASS lines with their "reproduces" lines (Wolfram checks `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00`).

**In [21]: the exact family of solutions.**

```python
al, k, ch, sh = sp.symbols("alpha k ch sh", real=True)
chi0 = sp.Matrix(sp.symbols("q1:17"))  # an arbitrary constant column
M = -m * G[X4] + 3 * H * (2 * al + 1) * G[X4] * G[X8]
k_squared = 9 * H**2 * (2 * al + 1) ** 2 - m**2
check((M * M - k_squared * I16).applyfunc(sp.expand) == Z16
      and (M.T * C + C * M).applyfunc(sp.expand) == Z16,
      "M^2 = k^2 with k^2 = 9 H^2 (2 alpha + 1)^2 - m^2, and M^T C + C M = 0")
```

Symbols for $\alpha$, $k$ and the two functions $\cosh(kx_4)$, $\sinh(kx_4)$ (written `ch`, `sh`); `chi0` is a column of 16 arbitrary symbols. `M` and `k_squared` are those of Section 7.23. The check: $M^2 = k^2$ and $M^TC + CM = 0$.

```python
def d4(v):  # derivative along x4 with ch' = k sh, sh' = k ch
    return v.diff(ch) * k * sh + v.diff(sh) * k * ch


def d8(v):  # derivative along x8 in the ring (s^(6 alpha) included)
    return v.diff(s) * H * c / s**5 + v.diff(c) * (-6 * H * s**6)


Psi = s ** (6 * al) * (ch * I16 + sh / k * M) * chi0  # sin^alpha z P(x4) chi0
residual = (G[X4] * Psi.applyfunc(d4) + (s**6 / c) * G[X8] * Psi.applyfunc(d8)
            + 3 * H * G[X8] * Psi - m * Psi)
```

`d4` differentiates along $x_4$ with $\partial_4\,\mathrm{ch} = k\,\mathrm{sh}$ and $\partial_4\,\mathrm{sh} = k\,\mathrm{ch}$; `d8` along $x_8$ in the ring (the factor $\sin^\alpha z$ is written $s^{6\alpha}$, whose derivative sympy handles). `Psi` is the family $\sin^\alpha z\,(\cosh kx_4 + \sinh(kx_4)/k\,M)\chi_0$ and `residual` the left side minus the right side of the explicit equation (the other six derivative terms vanish for a field of $x_4$ and $x_8$ only).

```python
def vanishes(v):
    """Multiply by k and divide by sin^alpha z = s^(6 alpha), multiply out, use
    k^2 = 9 H^2 (2 alpha + 1)^2 - m^2: is the result zero?"""
    v = sp.expand(v * k / s ** (6 * al))
    return sp.expand(v.subs(k**2, k_squared)) == 0


without_term = residual - 3 * H * G[X8] * Psi  # the same without 3 H gamma^(x8)
check(all(vanishes(v) for v in residual)
      and not all(vanishes(v) for v in without_term),
      "Psi = sin^alpha z (cosh k x4 + sinh k x4 / k M) chi0 solves the field "
      "equation for every alpha and every a4 (and fails without 3 H gamma^(x8))",
      record=reproduces(PYREP, "exact_solution_family_x4_x8"))
```

`vanishes(v)` multiplies a residual entry by $k$, divides by $s^{6\alpha}$, multiplies out, replaces $k^2$ by its value, and tests for zero. The check requires all 16 entries of the residual to vanish, and at least one entry of the residual without the term $3H\gamma^{(x_8)}\Psi$ not to vanish.

```python
A_matrix = -sp.I * m * G[X4] + 3 * sp.I * H * G[X4] * G[X8]
check((A_matrix * A_matrix - (m**2 - 9 * H**2) * I16).applyfunc(sp.expand) == Z16,
      "the mode matrix A = -i m gamma^(x4) + 3 i H gamma^(x4) gamma^(x8) has A^2 = "
      "(m^2 - 9 H^2) I16", record=reproduces(
          SCOPE, "good_sector_x8_independent_modes_without_boundary_condition"))
```

The mode matrix of the scope record, $A = -im\gamma^{(x_4)} + 3iH\gamma^{(x_4)}\gamma^{(x_8)}$ (the matrix that $i\partial_4$ applies to the $x_8$-independent fields), squares to $(m^2 - 9H^2)I_{16}$. **Out [21]:** three PASS lines, the last two with their "reproduces" lines.

**In [22]: two members of the family, numerically.**

```python
Gn = [np.array(gm.tolist(), dtype=float) for gm in G]  # the gammas as float arrays
Cn = np.array(C.tolist(), dtype=float)
chi_n = np.zeros(16)
chi_n[[0, 4]] = 1.0  # e_1 + e_5
zeta = np.pi / 4  # the point z = pi/4 of the hidden direction
xs4 = np.linspace(0.0, 2.0, 201)
```

The gammas and $C$ as floating-point numpy arrays; `chi_n` is $e_1 + e_5$ (positions 0 and 4 set to 1); the point $z = \pi/4$ and 201 times from 0 to 2.

```python
def member(alpha_value, mass=2.0, h=1.0):
    """Psi(x4) at z = pi/4 for the family member alpha (columns = times)."""
    Mn = -mass * Gn[X4] + 3 * h * (2 * alpha_value + 1) * Gn[X4] @ Gn[X8]
    ksq = 9 * h**2 * (2 * alpha_value + 1) ** 2 - mass**2
    kk = np.sqrt(complex(ksq))  # real for ksq > 0, imaginary for ksq < 0
    values = [(np.cosh(kk * t) * np.eye(16) + np.sinh(kk * t) / kk * Mn) @ chi_n
              for t in xs4]
    return np.sin(zeta) ** alpha_value * np.real(np.array(values).T)
```

`member(alpha_value)` evaluates the family at $z = \pi/4$ with $m = 2$, $H = 1$. `np.sqrt(complex(ksq))` is real for $k^2 > 0$ and imaginary for $k^2 < 0$; `np.cosh` and `np.sinh` of an imaginary argument give $\cos$ and $i\sin$, so the formula works in both cases; `np.real` drops the zero imaginary parts. The result is a table with one column per time (`.T` transposes).

```python
growing, oscillating = member(0.0), member(-0.5)
S_growing = np.einsum("it,ij,jt->t", growing, Cn, growing)  # Psi^T C Psi
S_oscillating = np.einsum("it,ij,jt->t", oscillating, Cn, oscillating)
report("S of the alpha = 0 member", f"{S_growing[0]:.6f}")
report("S of the alpha = -1/2 member", f"{S_oscillating[0]:.6f}")
check(np.allclose(S_growing, -2.0, atol=1e-9 * np.abs(growing).max() ** 2)
      and np.allclose(S_oscillating, -2.0 / np.sin(zeta), atol=1e-9),
      "S is constant along x4 for both members (-2 and -2/sin z)")
```

The growing member ($\alpha = 0$) and the oscillating member ($\alpha = -\tfrac12$). `np.einsum("it,ij,jt->t", ...)` computes $\Psi^TC\Psi$ at every time $t$ (a sum over the repeated indices $i$ and $j$). The check requires the constant values $-2$ and $-2/\sin z$ (for the growing member the tolerance grows with the size of $\Psi$, because rounding errors grow with it). **Out [22]:** `RESULT S of the alpha = 0 member = -2.000000`, `RESULT S of the alpha = -1/2 member = -2.828427` and the PASS line.

**In [23]: Figure 07b.5.**

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.6))
for A in range(16):
    if np.abs(growing[A]).max() > 1e-12:  # draw only the nonzero components
        axes[0].semilogy(xs4, np.abs(growing[A]), label=f"$|\\Psi_{{{A + 1}}}|$")
    if np.abs(oscillating[A]).max() > 1e-12:
        axes[1].plot(xs4, oscillating[A], label=f"$\\Psi_{{{A + 1}}}$")
axes[0].set_title("$\\alpha = 0$: growth like $e^{\\sqrt{5}x_4}$")
axes[1].set_title("$\\alpha = -1/2$: oscillation")
axes[2].plot(xs4, S_growing, label="$\\alpha = 0$")
axes[2].plot(xs4, S_oscillating, "--", label="$\\alpha = -1/2$")
axes[2].set_ylim(-3.5, 0.5)
axes[2].set_title("scalar density $S = \\Psi^T C\\Psi$")
for ax in axes:
    ax.set_xlabel("time $x_4$")
    ax.legend(fontsize=7)
axes[0].set_ylabel("value at $z = \\pi/4$")
fig.tight_layout()
save_figure(fig, "exact_solutions",
...)
```

Three panels: the size of the nonzero components of the growing member on a logarithmic axis, the nonzero components of the oscillating member, and the two scalar densities. `f"$|\\Psi_{{{A + 1}}}|$"` writes the component number as a LaTeX subscript (three braces: two give one literal brace, the third encloses the value). **What Figure 07b.5 shows.** Left: straight rising lines on the logarithmic axis, growth like $e^{\sqrt5x_4}$. Middle: oscillations of period $\pi$ (angular frequency 2). Right: both scalar densities are flat lines, at $-2$ and at $-2.83$.

**In [24]: the exact solution fails the wrong equations, Figure 07b.6.**

```python
Mn = -2.0 * Gn[X4] + 3.0 * Gn[X4] @ Gn[X8]  # alpha = 0, m = 2, H = 1
kk = np.sqrt(5.0)
psi_t = np.array([(np.cosh(kk * t) * np.eye(16) + np.sinh(kk * t) / kk * Mn) @ chi_n
                  for t in xs4])
dpsi_t = np.array([(kk * np.sinh(kk * t) * np.eye(16) + np.cosh(kk * t) * Mn) @ chi_n
                   for t in xs4])
full = np.array([Gn[X4] @ dp + 3.0 * Gn[X8] @ p - 2.0 * p
                 for p, dp in zip(psi_t, dpsi_t)])
no_gravity = np.array([Gn[X4] @ dp - 2.0 * p for p, dp in zip(psi_t, dpsi_t)])
wrong_mass = np.array([Gn[X4] @ dp + 3.0 * Gn[X8] @ p + 2.0 * p
                       for p, dp in zip(psi_t, dpsi_t)])
size = np.abs(psi_t).max(axis=1)  # the size of Psi at each time
relative_full = np.abs(full).max(axis=1) / size
check(relative_full.max() < 1e-12, "the full field equation holds to rounding "
      "(relative residual below 1e-12 at all 201 times)")
check(np.allclose(np.abs(no_gravity).max(axis=1), 3.0 * size),
      "without the term 3 H gamma^(x8) Psi the residual is 3 H |Psi|")
```

For the growing member, `psi_t` and `dpsi_t` are $\Psi$ and its exact derivative $\partial_4\Psi = (k\sinh(kx_4) + \cosh(kx_4)M)\chi_0$ at the 201 times ($\partial_8\Psi = 0$ for $\alpha = 0$). `full` is the residual $\gamma^{(x_4)}\partial_4\Psi + 3H\gamma^{(x_8)}\Psi - m\Psi$, `no_gravity` the residual without the gravitational term, `wrong_mass` the residual of the equation with the mass $m$ replaced by $-m$ (the term $-m\Psi$ becomes $+m\Psi$). `size` is the largest component of $\Psi$ at each time. The first check: the full residual is below $10^{-12}$ of the size at every time; the second: without the gravitational term the residual is $3H$ times the size.

```python
fig, ax = plt.subplots()
ax.semilogy(xs4, np.abs(no_gravity).max(axis=1),
            label="without $3H\\gamma^{(x_8)}\\Psi$")
ax.semilogy(xs4, np.abs(wrong_mass).max(axis=1), "--", label="mass $m \\to -m$")
ax.semilogy(xs4, size, ":", color="black", label="size of $\\Psi$")
ax.set_xlabel("time $x_4$")
ax.set_ylabel("largest component of the residual")
ax.set_title("The exact solution fails the wrong equations")
ax.legend(fontsize=8)
save_figure(fig, "residuals",
...)
```

One panel with the two wrong residuals and the size of $\Psi$ on a logarithmic axis. **Out [24]:** two PASS lines and the figure. **What Figure 07b.6 shows.** Both wrong residuals grow as fast as the solution itself (parallel lines on the logarithmic axis); the residual without the gravitational term lies a factor 3 above the size of $\Psi$. The correct residual, below $10^{-12}$ of the size, is too small to be drawn.

**In [25]: the last check.**

```python
names = ["scale_factors", "gamma_omega_per_direction", "lagrangian_monomials",
         "coupling_map", "exact_solutions", "residuals"]
files = [f"{FIGURE_FOLDER}/07b_{k}_{name}.png" for k, name in enumerate(names, 1)]
check(all(output_file(path).is_file() for path in files),
      "all 6 figure files of this notebook exist")
all_checks_passed()
```

The six figure files are checked and the last line printed. **Out [25]:** `PASS all 6 figure files of this notebook exist` and `ALL 47 CHECKS PASSED (notebook 07b)`.

### 7.28 Real fields and the Majorana-type negative control

**Real fields.** A **real field** is a column whose components are their own conjugates: $\Phi^* = \Phi$ for ordinary numbers, and for Grassmann components a column of real generators, $\theta^* = \theta$ (no separate conjugate generators at all). For a real column the row $\Phi^\dagger$ is just the transpose $\Phi^T$. Real fields matter in this book for two reasons: the author's own notebook wrote its Lagrangian for a real column, and the question "what is charge conjugation?" has a surprising answer for real fields (Section 7.29).

**The author's Majorana-type Lagrangian.** The author's notebook used a real column $\Theta$ of 16 components and, with the canonical connection, the Lagrangian

$$
L_g = \sqrt{|g|}\,\big[\Theta^TC\gamma^\mu D_\mu\Theta + (\text{a number})\,\Theta^TC\Theta\big] ,
$$

built with the transpose $\Theta^T$ instead of the Dirac adjoint (a Lagrangian of this kind is called **Majorana-type**, after the physicist Ettore Majorana, who studied real spinor fields). If the components anticommute, as the components of dirac16complex do, this Lagrangian describes nothing:

- Its mass-type term vanishes: $\Theta^TC\Theta = 0$, because $C$ is symmetric (Section 7.12).
- Its kinetic term is a total derivative. Three identities show it. First, for an antisymmetric matrix $A$ (here $A = C\gamma^\mu$, which may depend on the coordinates) and an odd column, $(\partial_\mu\Theta)^TA\Theta = \Theta^TA\,\partial_\mu\Theta$: exchanging the two odd factors gives a minus sign, and the transpose of $A$ another one. So the product rule gives $\partial_\mu(\Theta^TA\Theta) = 2\,\Theta^TA\,\partial_\mu\Theta + \Theta^T(\partial_\mu A)\Theta$, that is

$$
\Theta^TC\gamma^\mu\partial_\mu\Theta = \tfrac12\partial_\mu\big(\Theta^TC\gamma^\mu\Theta\big) - \tfrac12\Theta^T\partial_\mu\big(C\gamma^\mu\big)\Theta .
$$

Second, in $\Theta^TC\gamma^\mu\Omega_\mu\Theta$ only the antisymmetric part of the matrix $N = C\gamma^\mu\Omega_\mu$ survives (Section 7.12), and $N^T = \Omega_\mu^T(\gamma^\mu)^TC = \Omega_\mu^T(-C\gamma^\mu) = C\Omega_\mu\gamma^\mu$ (using $(\gamma^\mu)^TC = -C\gamma^\mu$ and $\Omega_\mu^TC = -C\Omega_\mu$), so $\tfrac12(N - N^T) = \tfrac12C[\gamma^\mu, \Omega_\mu]$ with the **commutator** $[X, Y] = XY - YX$:

$$
\Theta^TC\gamma^\mu\Omega_\mu\Theta = \tfrac12\Theta^TC[\gamma^\mu, \Omega_\mu]\Theta .
$$

Third, multiply both by $\sqrt{|g|}$, use $\sqrt{|g|}\,\partial_\mu X = \partial_\mu(\sqrt{|g|}X) - (\partial_\mu\sqrt{|g|})X$ and collect:

$$
\sqrt{|g|}\,\Theta^TC\gamma^\mu D_\mu\Theta = \tfrac12\partial_\mu\big(\sqrt{|g|}\,\Theta^TC\gamma^\mu\Theta\big) - \tfrac12\Theta^TC\Big(\partial_\mu\big(\sqrt{|g|}\gamma^\mu\big) - \sqrt{|g|}\,[\gamma^\mu, \Omega_\mu]\Big)\Theta .
$$

The last bracket is zero: in the author's metric $[\gamma^\mu, \Omega_\mu] = 2\gamma^\mu\Omega_\mu$ (they anticommute) and $\partial_\mu(\sqrt{|g|}\gamma^\mu) = 2\sqrt{|g|}\gamma^\mu\Omega_\mu$ (Section 7.18); in a general metric this is the covariant constancy of the gammas (Wolfram check `gamma_covariantly_constant`). So $L_g$ is the total derivative of $\tfrac12\sqrt{|g|}\,\Theta^TC\gamma^\mu\Theta$, and by Section 7.4 all its Euler-Lagrange expressions vanish identically: no field equation at all (PROVED; Notebook 07c computes it in the author's metric, In [5] and In [6]: $L_g$ has 136 monomials, it equals its total-derivative form exactly, and 0 of its 16 Euler-Lagrange expressions are nonzero; the Revision checks are listed in the table at the end of this section).

This is the **negative control** of the Revision record: a test designed to show what does NOT work. It is the reason why the Revision Lagrangian of dirac16complex is written for a complex field with $\bar\Psi = \Psi^\dagger C$ (Section 7.19), and Section 7.13 showed the same mechanism with two components.

**Real commuting fields.** For ordinary numbers the roles are exchanged (Section 7.12): $\Phi^TC\gamma^\mu\Phi = 0$, while $\Phi^TC\Phi$ survives, and the kinetic term is not a total derivative. Varying $\Phi_A$ in $\sqrt{|g|}\,\Phi^TC\gamma^\mu D_\mu\Phi$: the derivative with respect to $\Phi_A$ is $\sqrt{|g|}\big[(C\gamma^\mu\partial_\mu\Phi)_A + (C\gamma^\mu\Omega_\mu\Phi)_A + (N^T\Phi)_A\big]$ (each factor $\Phi$ contributes once), the derivative with respect to $\partial_\mu\Phi_A$ is $\sqrt{|g|}\big((C\gamma^\mu)^T\Phi\big)_A = -\sqrt{|g|}(C\gamma^\mu\Phi)_A$, and with $N^T = C\Omega_\mu\gamma^\mu$ and $\partial_\mu(\sqrt{|g|}\gamma^\mu) = 2\sqrt{|g|}\gamma^\mu\Omega_\mu$ the Euler-Lagrange expression becomes

$$
\sqrt{|g|}\,C\big[2\gamma^\mu\partial_\mu\Phi + \gamma^\mu\Omega_\mu\Phi + \Omega_\mu\gamma^\mu\Phi + 2\gamma^\mu\Omega_\mu\Phi\big] = 2\sqrt{|g|}\,C\gamma^\mu D_\mu\Phi
$$

(using $\Omega_\mu\gamma^\mu = -\gamma^\mu\Omega_\mu$): a massless field equation $\gamma^\mu D_\mu\Phi = 0$ in all 16 components (PROVED; Notebook 07c, In [7]; `python-field-theory.json`, check `negative_control_majorana_commuting_contrast`, "16 of 16 components"; `wolfram-field-theory.json`, check `Majorana_Lg_commuting_control`).

**The Revision Lagrangian for a real commuting field.** Put $\Psi = \Phi$ real and commuting into the Lagrangian of Section 7.19. Then $\bar\Phi = \Phi^TC$, and the second half of the kinetic term equals the first: $(D_\mu\bar\Phi)\gamma^\mu\Phi = (D_\mu\Phi)^TC\gamma^\mu\Phi = \Phi^T(C\gamma^\mu)^TD_\mu\Phi = -\Phi^TC\gamma^\mu D_\mu\Phi$ (a single number equals its own transpose, and $C\gamma^\mu$ is antisymmetric). So $K = \Phi^TC\gamma^\mu D_\mu\Phi$ and

$$
\mathcal{L}[\Phi] = \sqrt{|g|}\,\big[\Phi^TC\gamma^\mu D_\mu\Phi - m\,\Phi^TC\Phi - \tfrac{\lambda}{2}(\Phi^TC\Phi)^2\big] :
$$

the author's $L_g$ with a mass term and the interaction. Its Euler-Lagrange expressions are $2\sqrt{|g|}\,\big(C(\gamma^\mu D_\mu\Phi - (m + \lambda S)\Phi)\big)_A$ (the kinetic part as just computed; $\partial(\Phi^TC\Phi)/\partial\Phi_A = 2(C\Phi)_A$ because $C$ is symmetric): a real commuting field obeys the same field equation as the complex one (PROVED; Notebook 07c, In [12]). Because the gammas, $C$ and the spinor connection are real (`Revision/lead_checks/reports/charge-conjugation-and-u1.json`, checks `representation_real` and `spinor_connection_real`), the operator $\gamma^\mu D_\mu$ is real, the complex conjugate of a solution is again a solution, and real fields are a consistent restriction of dirac16complex00.

**A real field carries no charge.** The phase change $\Psi \to e^{i\alpha}\Psi$ leaves the Lagrangian unchanged (every term contains as many factors of $\Psi^\dagger$ as of $\Psi$), and the conserved quantity that belongs to it is the **current** $J^\mu = -i\bar\Psi\gamma^\mu\Psi$, whose time component $J^{x_4} = \Psi^\dagger B\Psi$, with $B = -iC\gamma^{(x_4)}$, is the **charge density** (Chapter 5; Chapter 21 proves its conservation). For a real commuting field $J^\mu = -i\Phi^TC\gamma^\mu\Phi = 0$ identically, because $C\gamma^\mu$ is antisymmetric (Section 7.12): a real field has no charge (PROVED; Notebook 07c, In [11]; `charge-conjugation-and-u1.json`, check `real_fields_charge_conjugation`).

**Where the negative control is verified** (the theory reports in the folder `Revision/theory/reports`):

| statement | status | where it is verified |
| --- | --- | --- |
| $L_g$ of a real Grassmann field is a total derivative: no field equation; $\Theta^TC\Theta = 0$ | PROVED; Notebook 07c, In [5] and In [6] | `python-field-theory.json`, check `negative_control_majorana_grassmann_total_derivative`; `wolfram-field-theory.json`, check `Majorana_Lg_total_derivative_grassmann` |
| $L_g$ of a real commuting field gives $2\sqrt{\lvert g\rvert}\,C\gamma^\mu D_\mu\Phi$ in 16 of 16 components | PROVED; In [7] | `python-field-theory.json`, check `negative_control_majorana_commuting_contrast`; `wolfram-field-theory.json`, check `Majorana_Lg_commuting_control` |

### 7.29 Charge conjugation is a matrix

**What charge conjugation must do.** A **charge conjugation** is a map that turns a field into a field of the opposite charge, the map that exchanges matter and antimatter. For a spinor field it is a MATRIX map

$$
\Psi^c = \mathcal{C}\,\bar\Psi^T ,
$$

with a fixed $16\times16$ matrix $\mathcal{C}$, the **charge-conjugation matrix**. Since $\bar\Psi^T = (\Psi^\dagger C)^T = C^T\Psi^* = C\Psi^*$ ($C$ is symmetric), it reads $\Psi^c = M\Psi^*$ with the constant matrix $M = \mathcal{C}C$. It must turn every solution of the field equation into a solution, of the same equation or of the equation with the mass reversed. The author's gammas are REAL. So for a REAL field $\Psi^* = \Psi$: the plain complex conjugate of a real field is the field itself, and plain complex conjugation cannot exchange anything. Everything therefore rests on the matrix.

**The condition on $M$, line by line.** Let $\Psi$ solve $(\gamma^\mu D_\mu - V)\Psi = 0$ with a real $V$. Then

$$
(\gamma^\mu D_\mu - V)\Psi^* = 0
$$

(take the complex conjugate: $\gamma^\mu$, $\Omega_\mu$ and $V$ are real, so only $\Psi$ changes);

$$
M(\gamma^\mu D_\mu - V)M^{-1}\,\big(M\Psi^*\big) = 0
$$

(insert $M^{-1}M = 1$ in front of $\Psi^*$ and multiply from the left by $M$). If $M\gamma^{(a)}M^{-1} = s\gamma^{(a)}$ for all eight $a$, with $s = +1$ or $s = -1$, then $M\Omega_\mu M^{-1} = \Omega_\mu$ (each $S^{ab}$ is a product of two gammas, and $s^2 = 1$), $M$ commutes with $\partial_\mu$ (it is constant), and $M(\gamma^\mu D_\mu - V)M^{-1} = s\gamma^\mu D_\mu - V = s(\gamma^\mu D_\mu - sV)$. So $M\Psi^*$ solves the equation with $V$ replaced by $sV$: the same mass for $s = +1$, the reversed mass for $s = -1$. We must find all matrices $M$ with

$$
M\gamma^{(a)} = s\,\gamma^{(a)}M\qquad\text{for all } a .
$$

**All solutions, line by line.** The 256 products $\gamma_I = \gamma^{(a_1)}\cdots\gamma^{(a_k)}$ with $a_1 < \dots < a_k$ (all subsets $I$ of the eight directions, the empty product being $1$) are a **basis** of all $16\times16$ matrices: every matrix is exactly one combination $\sum_Ic_I\gamma_I$. *Proof.* Each gamma is a signed permutation matrix with $(\gamma^{(a)})^T = (\gamma^{(a)})^{-1}$, so $\gamma_I^T = \gamma_I^{-1}$ and $\gamma_I^T\gamma_J = \pm\gamma_K$, where $K$ is the set of directions in exactly one of $I$, $J$ (the shared gammas square to $\pm1$). The trace of $\gamma_K$ is 0 for every nonempty $K$: if $K$ has an even number of elements, take $a$ in $K$; by Rule 1 of Chapter 5 $\gamma_K$ anticommutes with $\gamma^{(a)}$, so $\mathrm{tr}\,\gamma_K = \mathrm{tr}\big((\gamma^{(a)})^{-1}\gamma_K\gamma^{(a)}\big) = -\mathrm{tr}\,\gamma_K$ (the trace does not change when a matrix is moved from the front to the back of a product); if $K$ has an odd number of elements fewer than 8, take $a$ not in $K$, and the same argument applies. So $\mathrm{tr}(\gamma_I^T\gamma_J) = 16\,\delta_{IJ}$: the 256 matrices are **orthogonal** (for the scalar product $\mathrm{tr}(X^TY)$ of matrices), hence independent, and 256 independent matrices span the 256-dimensional space of $16\times16$ matrices. $\square$ (Notebook 07c checks the orthogonality with exact integers, In [8].)

Next, each basis product either commutes or anticommutes with a given $\gamma^{(a)}$: moving $\gamma^{(a)}$ through the $k$ factors of $\gamma_I$ costs $(-1)^k$ if $a$ is not in $I$ and $(-1)^{k-1}$ if it is (it passes $k - 1$ other factors and commutes with itself) (Rule 1 of Chapter 5). So $\gamma^{(a)}\gamma_I(\gamma^{(a)})^{-1} = \epsilon_I(a)\gamma_I$ with a sign $\epsilon_I(a)$. Write $M = \sum_Ic_I\gamma_I$. The condition $\gamma^{(a)}M(\gamma^{(a)})^{-1} = sM$ (the condition above, multiplied by $(\gamma^{(a)})^{-1}$ from the right and divided by $s$, since $1/s = s$) becomes $\sum_I\epsilon_I(a)c_I\gamma_I = \sum_Isc_I\gamma_I$, and because the $\gamma_I$ are independent, $\epsilon_I(a)c_I = sc_I$ for every $I$ and every $a$. So $c_I \neq 0$ only for products that have the sign $s$ with ALL eight gammas.

Count, for a product of $k$ gammas, the number of gammas it commutes with. If $k$ is even, it commutes with the $8 - k$ gammas not in it and anticommutes with the $k$ in it: $8 - k$. If $k$ is odd, it anticommutes with those not in it and commutes with those in it: $k$. Commuting with all eight needs $8 - k = 8$ ($k = 0$, the identity) or $k = 8$ with $k$ odd (impossible): only the identity. Anticommuting with all eight needs $8 - k = 0$ ($k = 8$, the product of all eight, which is $\pm\Gamma$) or $k = 0$ with $k$ odd (impossible): only $\Gamma$. Hence (PROVED; Notebook 07c, In [8] and In [9], Figure 07c.2; `charge-conjugation-and-u1.json`, checks `intertwiners_same_mass` and `intertwiners_reversed_mass`):

$$
M = c\cdot1\quad(s = +1,\ \text{same mass}),\qquad M = c\cdot\Gamma\quad(s = -1,\ \text{mass reversed}),
$$

with a constant $c$. With $M = \mathcal{C}C$ and $C^{-1} = C$ (because $C^2 = 1$) the two **charge-conjugation matrices** are, up to a constant factor,

$$
\mathcal{C}_+ = C,\quad \Psi^c = \Psi^*;\qquad\qquad \mathcal{C}_- = \Gamma C,\quad \Psi^c = \Gamma\Psi^* .
$$

**Their defining properties.** For $\mathcal{C}_+ = C$, line by line:

$$
\mathcal{C}_+^{-1}\gamma^{(a)}\mathcal{C}_+ = (C\gamma^{(a)})\,C = -(C\gamma^{(a)})^TC = -(\gamma^{(a)})^TC^TC = -(\gamma^{(a)})^T
$$

($C^{-1} = C$; $C\gamma^{(a)}$ is antisymmetric; the transpose of a product is the product of the transposes in reversed order; $C^TC = C^2 = 1$). For $\mathcal{C}_- = \Gamma C$: $\mathcal{C}_-^{-1} = C\Gamma$ (both square to 1), and $\Gamma\gamma^{(a)}\Gamma = -\gamma^{(a)}$, so $\mathcal{C}_-^{-1}\gamma^{(a)}\mathcal{C}_- = C\Gamma\gamma^{(a)}\Gamma C = -C\gamma^{(a)}C = +(\gamma^{(a)})^T$. Both matrices are real (PROVED; Notebook 07c, In [10]; checks `charge_conjugation_matrix_plus` and `charge_conjugation_matrix_minus`). A **Majorana (reality) condition** $\Psi = M\Psi^*$ is consistent only if $MM^* = 1$ (apply it twice: $\Psi^* = M^*\Psi$, so $\Psi = MM^*\Psi$); this holds for $M = 1$ and for $M = \Gamma$ (real, $\Gamma^2 = 1$), so both reality conditions are consistent (check `majorana_conditions_consistent`). Chapter 5 derives the same matrices from the algebra alone.

**What they do to a real field.** For a real column $\Phi$:

$$
\Phi^c_+ = \mathcal{C}_+\bar\Phi^T = C\,(\Phi^TC)^T = CC\Phi = \Phi,\qquad \Phi^c_- = \mathcal{C}_-\bar\Phi^T = \Gamma CC\Phi = \Gamma\Phi .
$$

$\mathcal{C}_+$ does nothing to a real field: a real field is its own conjugate, in agreement with $J^\mu = 0$ (Section 7.28). The only nontrivial map of real fields is the REAL matrix $\Gamma = \mathrm{diag}(-I_8, I_8)$. It keeps the scalar density and reverses every kinetic matrix:

$$
\Gamma^TC\Gamma = C,\qquad \Gamma^TC\gamma^{(a)}\Gamma = -C\gamma^{(a)}
$$

($\Gamma^T = \Gamma$ is diagonal; it commutes with $C$, a product of four gammas, and anticommutes with $\gamma^{(a)}$; and $\Gamma^2 = 1$). It also commutes with every $\Omega_\mu$ (a combination of products of two gammas), so $D_\mu(\Gamma\Phi) = \Gamma D_\mu\Phi$. Therefore $K[\Gamma\Phi] = -K[\Phi]$ and $S[\Gamma\Phi] = S[\Phi]$, and

$$
\mathcal{L}_{m,\lambda}[\Gamma\Phi] = \sqrt{|g|}\,\big[-K - mS - \tfrac{\lambda}{2}S^2\big] = -\sqrt{|g|}\,\big[K - (-m)S - \tfrac{(-\lambda)}{2}S^2\big] = -\mathcal{L}_{-m,-\lambda}[\Phi] :
$$

the matrix $\Gamma$, together with $(m, \lambda) \to (-m, -\lambda)$, maps solutions to solutions; a real solution of mass $m$ goes to a real solution of mass $-m$ (PROVED; Notebook 07c, In [11] and In [12], and numerically on an exact solution, In [13], Figure 07c.4; `charge-conjugation-and-u1.json`, check `real_fields_charge_conjugation`). This is the form that the pairing theorem T1 takes for real fields; Chapter 18 proves T1 for both fields in every gravitational field. For a COMPLEX field the same matrix map $\Psi \to \Gamma\Psi$ (without any conjugation) also reverses the current: since $\Gamma$ is real, $(\Gamma\Psi)^\dagger = \Psi^\dagger\Gamma^T$, and $J^a[\Gamma\Psi] = -i\Psi^\dagger\Gamma^TC\gamma^{(a)}\Gamma\Psi = +i\Psi^\dagger C\gamma^{(a)}\Psi = -J^a[\Psi]$ by the identity just proved; for a real field both sides are zero.

**The signs of $S$ and $J$ under the two conjugations.** For a complex field and $\Psi' = M\Psi^*$ with the real $M = 1$ or $M = \Gamma$, the row is $\Psi'^\dagger = \Psi^TM^T$, and both matrices satisfy $M^TCM = C$, while $M^TC\gamma^{(a)}M = \pm C\gamma^{(a)}$ ($+$ for $M = 1$, $-$ for $M = \Gamma$). So

$$
S' = \Psi^TC\Psi^* = \sum_{A,B}\Psi_AC_{AB}\Psi_B^* = \sigma\sum_{A,B}\Psi_B^*C_{BA}\Psi_A = \sigma S
$$

(exchange the two factors, with $\sigma = +1$ for commuting and $\sigma = -1$ for Grassmann components; then $C_{AB} = C_{BA}$), and in the same way, with the antisymmetric $C\gamma^{(a)}$, $-i\Psi^TC\gamma^{(a)}\Psi^* = -\sigma J^a$ for $M = 1$, and the opposite sign for $M = \Gamma$. In a table:

| map | commuting components | Grassmann components (classical) |
| --- | --- | --- |
| $\Psi \to \Psi^*$ (matrix $\mathcal{C}_+$) | $(S, J) \to (S, -J)$ | $(S, J) \to (-S, +J)$ |
| $\Psi \to \Gamma\Psi^*$ (matrix $\mathcal{C}_-$) | $(S, J) \to (S, +J)$ | $(S, J) \to (-S, -J)$ |

(PROVED here; it reproduces `charge-conjugation-and-u1.json`, check `bilinears_under_charge_conjugation`.) For the commuting complex field dirac16complex00 the map built with $\mathcal{C}_+$ keeps the mass and reverses the charge. For the Grassmann field the classical signs differ; the record states that in the quantum theory normal ordering supplies one more sign for each bilinear, and that for the QUANTISED field the conjugation that preserves the canonical anticommutator $\{\Psi, \Psi^\dagger\} = B\delta$ is $\Psi \to \Gamma\Psi^{\dagger T}$, which reverses the mass (quoted here from the same report, checks `bilinears_under_charge_conjugation` and `quantum_charge_conjugation_unitary_type`; Chapter 10 and Chapter 21 derive both).

**What this does and does not say.** The two charge-conjugation matrices and the mass reversal by $\Gamma$ are exact maps between the solutions of two equations (PROVED, with the checks named above). They do not say how any solution comes about: nothing in this chapter says that solutions, or universes, are created, in pairs or otherwise. Nor do they explain the observed excess of matter over antimatter: as built, the theory has no baryons, no violation of baryon number, no CP violation and no departure from equilibrium, the ingredients that such an explanation needs; Chapter 21 treats this question from zero, and Chapter 20 states exactly what the pairing theorems do and do not establish.

### 7.30 Example: Notebook 07c: real fields and the charge-conjugation matrices

Notebook 07c computes Sections 7.28 and 7.29 exactly. It reads the gammas, $C$ and $\Gamma$ from the Revision record and checks that they are real and that $B$ is imaginary and Hermitian; rebuilds the spin connection of the author's metric and checks that it is real; builds a jet algebra for a real field; computes the Majorana-type Lagrangian for real Grassmann and real commuting components (no field equation in the first case, 16 equations in the second); finds all matrices that turn solutions into solutions from the 256 products of gammas; checks the two charge-conjugation matrices and the two reality conditions; shows that $\mathcal{C}_+$ is the identity on a real field and that $J = 0$; and checks the mass reversal by $\Gamma$ in the author's metric and on an exact solution. Every result that the Revision record also contains is checked against it. It draws four figures and ends with the line ALL 23 CHECKS PASSED (notebook 07c).

<!-- NOTEBOOK 07c -->

### 7.33 Line-by-line walk-through of Notebook 07c

The notebook has 15 code cells, In [1] to In [15]. This section explains every line of every one of them, with the conventions of Section 7.9; every caption is printed in full under its figure in Section 7.32.

**In [1], the set-up cell.** It is the set-up cell of Notebook 07d with the one line `NOTEBOOK_ID = "07c"`; its first part repeats the complete run instructions of Section 7.31 as comment lines, and its code is explained line by line in Section 7.9. **Out [1]:** `Set-up of notebook 07c complete: repository folder found, helpers defined.`

**In [2]: the matrices are real or imaginary.**

```python
import contextlib  # redirect printed text into a buffer
import io  # an in-memory text file (the buffer)
import re  # regular expressions: read a number from a check's detail text
from itertools import combinations  # all subsets of the eight gammas

import numpy as np  # integer and floating-point arrays
import sympy as sp  # exact algebra

check_of_the_setup = check  # the helper check of the set-up cell


def check(condition, name, record=None):
    """The set-up cell's check, with its PASS line and its "reproduces" line
    printed by ONE print call, so that Jupyter delivers them together."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # collect what check prints
        check_of_the_setup(condition, name, record)
    print(buffer.getvalue(), end="")  # and print it in one piece
```

The modules (as in Notebook 07d, plus `combinations` from `itertools`, which lists all subsets of a given size) and the wrapper of `check` that prints a PASS line and its "reproduces" line in one piece (Section 7.9, In [2]).

```python
PYREP = "Revision/theory/reports/python-field-theory.json"
WLREP = "Revision/theory/reports/wolfram-field-theory.json"
LEAD = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"


def revision_check(report, name):
    """The check called name of a Revision report: its dictionary (name, verdict,
    detail); stops if it is missing or its verdict is not PASS."""
    data = json.loads(repository_file(report).read_text(encoding="utf-8"))
    found = [item for item in data["checks"] if item["name"] == name]
    if len(found) != 1 or found[0]["verdict"].upper() != "PASS":
        raise ValueError(f"{name} is not a passing check of {report}")
    return found[0]


def reproduces(report, name):
    """The text "<report>, check <name>" after making sure the check passes."""
    revision_check(report, name)
    return f"{report}, check {name}"
```

The paths of the three Revision reports used (the sympy and Wolfram field-theory reports and the lead's charge-conjugation report), and the helpers `revision_check` and `reproduces` of Section 7.9.

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
G = [sp.Matrix(g) for g in fixture["gamma"]]  # gamma^(x1) .. gamma^(x8)
C = sp.Matrix(fixture["C"])
GAMMA = G[7] * G[0] * G[1] * G[2] * G[3] * G[4] * G[5] * G[6]  # chirality
I16, Z16 = sp.eye(16), sp.zeros(16, 16)
X4, X8 = 3, 7  # list positions of x4 and x8
B = -sp.I * C * G[X4]
```

The gammas and $C$ read from `Revision/algebra/gammas.json` as exact sympy matrices. `GAMMA` is the chirality matrix computed as the product $\gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)}$ in the author's order; `I16`, `Z16` the identity and zero matrices; `X4`, `X8` the list positions of $x_4$ and $x_8$; `B` is $-iC\gamma^{(x_4)}$.

```python
real = all(v.is_real for M in G + [C, GAMMA] for v in M)
check(real and C.T == C and C * C == I16 and GAMMA == sp.Matrix(fixture["Gamma"])
      and GAMMA * GAMMA == I16 and all(GAMMA * g == -g * GAMMA for g in G),
      "the gammas, C and Gamma are real; C^T = C, C^2 = 1; Gamma^2 = 1 and Gamma "
      "anticommutes with every gamma", record=reproduces(LEAD, "representation_real"))
check(all(sp.re(v) == 0 for v in B) and B.H == B and B * B == I16,
      "B = -i C gamma^(x4) is purely imaginary and Hermitian, B^2 = 1",
      record=reproduces(LEAD, "B_imaginary_hermitian"))
```

`real` is true when every entry of every gamma, of $C$ and of $\Gamma$ is a real number (`v.is_real`). The first check adds: $C^T = C$, $C^2 = 1$, $\Gamma$ equal to the record's matrix (key `"Gamma"`), $\Gamma^2 = 1$, and $\Gamma$ anticommutes with every gamma. The second: every entry of $B$ has zero real part (`sp.re(v) == 0`), $B^\dagger = B$ (`B.H` is the conjugate transpose) and $B^2 = 1$.

```python
r = sp.Matrix(sp.symbols("r1:17", real=True))  # a real column of 16 numbers
check(r.conjugate() == r, "complex conjugation leaves a real column unchanged: on "
      "a real field it is the identity")
```

`r` is a column of 16 real symbols; its complex conjugate (`r.conjugate()`) equals itself: on a real field, complex conjugation is the identity. **Out [2]:** three PASS lines, the first two with "reproduces" lines naming `charge-conjugation-and-u1.json`, checks `representation_real` and `B_imaginary_hermitian`.

**In [3]: the metric and its spin connection, in brief.**

```python
E, s, c = sp.symbols("E s c", positive=True)  # e^a4, sin(z)^(1/6), cos z
A1, A2, A3 = sp.symbols("A1 A2 A3", real=True)  # derivatives of a4 (1st to 3rd)
H = sp.Symbol("H", positive=True)
m, lam = sp.symbols("m lambda", real=True)
ETA = [1, 1, 1, -1, -1, -1, -1, 1]
```

The ring symbols and $\eta$, as in Notebook 07b (Section 7.27, In [3]).

```python
def cd(expression, mu):
    """The derivative of a ring expression along coordinate mu (0 .. 7)."""
    expression = sp.sympify(expression)
    if mu == X4:
        return (sp.diff(expression, E) * E * A1 + sp.diff(expression, A1) * A2
                + sp.diff(expression, A2) * A3)
    if mu == X8:
        return (sp.diff(expression, s) * H * c / s**5
                + sp.diff(expression, c) * (-6 * H * s**6))
    return sp.Integer(0)


def is_zero(expression):
    """Exact test: the numerator vanishes after c^2 -> 1 - s^12."""
    numerator, _ = sp.fraction(sp.together(sp.sympify(expression)))
    numerator = sp.expand(numerator)
    if numerator == 0:
        return True
    remainder = sp.rem(sp.Poly(numerator, c), sp.Poly(c**2 - 1 + s**12, c))
    return sp.expand(remainder.as_expr()) == 0
```

The ring derivative `cd` and the exact zero test `is_zero`, the same functions as in Notebook 07b (explained in Section 7.27, In [3]).

```python
f = [E * s] * 3 + [sp.Integer(1)] + [s / E] * 3 + [c / s**6]  # the frame
g = [ETA[a] * f[a] ** 2 for a in range(8)]  # the diagonal metric
sqrt_g = sp.prod(f)  # = c = cos z
Gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
for l in range(8):
    for mu in range(8):
        for nu in range(8):
            value = ((cd(g[l], mu) if l == nu else 0) + (cd(g[l], nu) if l == mu else 0)
                     - (cd(g[mu], l) if mu == nu else 0))
            if value != 0:
                Gam[l][mu][nu] = sp.expand(value / (2 * g[l]))
```

The frame factors `f`, the metric entries `g`, the volume factor $\sqrt{|g|}$ (which is $c = \cos z$), and the Christoffel symbols of the diagonal formula, written here with conditional expressions (`(cd(g[l], mu) if l == nu else 0)` is the first term, and so on) instead of three `if` statements.

```python
SAB = [[(G[a] * G[b] - G[b] * G[a]) / 4 for b in range(8)] for a in range(8)]
Om = []  # the spinor connection Omega_mu
for mu in range(8):
    M = sp.zeros(16, 16)
    for a in range(8):
        for b in range(a + 1, 8):
            mixed = f[a] * Gam[a][mu][b] / f[b]  # omega_mu^a_b for a != b
            if mixed != 0:
                M += sp.expand(ETA[a] * mixed) * SAB[a][b]
    Om.append(M.applyfunc(sp.expand))
gam = [G[a] / f[a] for a in range(8)]  # the coordinate gammas
```

The spin generators $S^{ab}$ and the spinor connection $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$. Only $a \neq b$ is needed (because $S^{aa} = 0$), and for $a \neq b$ the formula of Section 7.18 reduces to $\omega_{\mu ab} = \eta_{aa}f_a\Gamma^a{}_{\mu b}/f_b$ (`mixed` is the part before $\eta_{aa}$). `gam` holds the coordinate gammas $\gamma^{(\mu)}/f_\mu$.

```python
# real: no imaginary unit, and sympy does not find the entry non-real
real_entries = all(not v.has(sp.I) and v.is_real is not False
                   for M in Om + gam for v in M)
check(real_entries, "every entry of every Omega_mu and gamma^mu is real: gamma^mu "
      "D_mu is a real operator", record=reproduces(LEAD, "spinor_connection_real"))
total = sum((gam[mu] * Om[mu] for mu in range(8)), Z16)
check(all(is_zero(v) for v in (total - 3 * H * G[X8])),
      "gamma^mu Omega_mu = 3 H gamma^(x8), the value of the Revision record",
      record=reproduces(PYREP, "gamma_mu_Omega_mu_equals_3H_gamma_x8"))
```

`real_entries` is true when no entry of any $\Omega_\mu$ or $\gamma^\mu$ contains the imaginary unit and sympy does not find any entry non-real (`v.is_real is not False`: sympy answers true, false, or "unknown", and only an explicit false would fail). So $\gamma^\mu D_\mu$ is a real operator. The second check is the consistency check $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$. **Out [3]:** two PASS lines with their "reproduces" lines (`spinor_connection_real` of the lead's report and `gamma_mu_Omega_mu_equals_3H_gamma_x8` of the sympy report).

**In [4]: a jet algebra for a real field.**

```python
def sort_sign(keys, odd):
    """Sorted tuple of generators and the sign; (None, 0) for a zero product."""
    items, sign = list(keys), 1
    for end in range(len(items) - 1, 0, -1):  # bubble sort, counting exchanges
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                sign = -sign
    if not odd:
        return tuple(items), 1
    if any(items[i] == items[i + 1] for i in range(len(items) - 1)):
        return None, 0
    return tuple(items), sign
```

`sort_sign` is the bubble sort with the Grassmann sign of Notebook 07b (Section 7.27, In [12]).

```python
class RealJet:
    """An element of the jet algebra of a real field: monomial -> coefficient."""

    def __init__(self, odd, terms=None):
        self.odd, self.terms = odd, {}
        for monomial, coefficient in (terms or {}).items():
            self.add(monomial, coefficient)

    def add(self, monomial, coefficient):
        total = sp.expand(self.terms.get(monomial, 0) + coefficient)
        if total == 0:
            self.terms.pop(monomial, None)
        else:
            self.terms[monomial] = total

    def __add__(self, other):
        result = RealJet(self.odd, self.terms)
        for monomial, coefficient in other.terms.items():
            result.add(monomial, coefficient)
        return result

    def __sub__(self, other):
        return self + other.times(-1)

    def times(self, factor):
        return RealJet(self.odd, {k: factor * v for k, v in self.terms.items()})

    def __mul__(self, other):
        result = RealJet(self.odd)
        for k1, v1 in self.terms.items():
            for k2, v2 in other.terms.items():
                monomial, sign = sort_sign(k1 + k2, self.odd)
                if monomial is not None:
                    result.add(monomial, sign * v1 * v2)
        return result
```

The class `RealJet` is the class `Jet` of Notebook 07b without the conjugation: a real field has no separate conjugate components, so a generator is a pair `(A, derivatives)` (component and derivative tuple), and there is no kind. `add`, addition, subtraction, `times` and the product work exactly as there.

```python
    def lderiv(self, key):
        result = RealJet(self.odd)
        for monomial, coefficient in self.terms.items():
            if key in monomial:
                p = monomial.index(key)
                factor = (-1) ** p if self.odd else monomial.count(key)
                result.add(monomial[:p] + monomial[p + 1:], factor * coefficient)
        return result

    def total(self, mu):
        result = RealJet(self.odd)
        for monomial, coefficient in self.terms.items():
            derivative = cd(coefficient, mu)
            if derivative != 0:
                result.add(monomial, derivative)
            for p, (A, d) in enumerate(monomial):
                raised = (A, tuple(sorted(d + (mu,))))
                ordered, sign = sort_sign(monomial[:p] + (raised,) + monomial[p + 1:],
                                          self.odd)
                if ordered is not None:
                    result.add(ordered, sign * coefficient)
        return result

    def is_zero(self):
        return all(is_zero(v) for v in self.terms.values())
```

The left derivative (with the Grassmann sign $(-1)^p$, or the power for commuting generators), the total derivative $d/dx_\mu$ (the coefficient differentiated with `cd`, each generator raised in turn), and the exact zero test of an element; all as in Notebook 07b.

```python
def column(odd, derivatives=()):
    """The 16 generators theta_A (or one of their derivatives)."""
    return [RealJet(odd, {((A, tuple(sorted(derivatives))),): 1}) for A in range(16)]


def matvec(M, v, odd):
    out = [RealJet(odd) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if M[i, j] != 0:
                out[i] = out[i] + v[j].times(M[i, j])
    return out


def vecmat(v, M, odd):
    out = [RealJet(odd) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if M[i, j] != 0:
                out[j] = out[j] + v[i].times(M[i, j])
    return out


def dot(row, col, odd):
    result = RealJet(odd)
    for x, y in zip(row, col):
        result = result + x * y
    return result


say("The jet algebra of a real field is defined.")
```

The vector helpers `column` (the 16 generators $\theta_A$ or one of their derivatives), `matvec`, `vecmat` and `dot`, as in Notebook 07b. **Out [4]:** `The jet algebra of a real field is defined.`

**In [5]: the Majorana-type Lagrangian for both kinds of numbers.**

```python
results = {}
for name, odd in (("grassmann", True), ("commuting", False)):
    theta = column(odd)
    row = vecmat(theta, C, odd)  # Theta^T C
    Lg = RealJet(odd)
    derivative_form = RealJet(odd)
    for mu in range(8):
        D_theta = [x + y for x, y in zip(column(odd, (mu,)),
                                         matvec(Om[mu], theta, odd))]
        Lg = Lg + dot(row, matvec(gam[mu], D_theta, odd), odd)
        current = dot(row, matvec(gam[mu], theta, odd), odd).times(sqrt_g / 2)
        derivative_form = derivative_form + current.total(mu)
    Lg = Lg.times(sqrt_g)
```

For real Grassmann and real commuting components: `theta` is the column of the 16 generators and `row` the row $\Theta^TC$. For each direction, `D_theta` is $\partial_\mu\Theta + \Omega_\mu\Theta$, `Lg` collects $\Theta^TC\gamma^\mu D_\mu\Theta$, and `derivative_form` collects $\frac{d}{dx_\mu}\big(\tfrac12\sqrt{|g|}\,\Theta^TC\gamma^\mu\Theta\big)$, the candidate total-derivative form of Section 7.28. Finally `Lg` is multiplied by $\sqrt{|g|}$.

```python
    euler_lagrange = []
    for A in range(16):
        value = Lg.lderiv((A, ()))
        for mu in range(8):
            value = value - Lg.lderiv((A, (mu,))).total(mu)
        euler_lagrange.append(value)
    results[name] = {"Lg": Lg, "derivative_form": derivative_form,
                     "EL": euler_lagrange, "mass": dot(row, theta, odd),
                     "theta": theta}
    nonzero = sum(1 for e in euler_lagrange if not e.is_zero())
    report(f"{name}: monomials of Lg", len(Lg.terms))
    report(f"{name}: nonzero Euler-Lagrange expressions", f"{nonzero} of 16")
```

The 16 Euler-Lagrange expressions with left derivatives, stored with the other pieces in the dictionary `results`; the mass-type term $\Theta^TC\Theta$ is stored too. The two `report` lines print the number of monomials of $L_g$ and how many Euler-Lagrange expressions are not zero. **Out [5]:** four lines,

```text
RESULT grassmann: monomials of Lg = 136
RESULT grassmann: nonzero Euler-Lagrange expressions = 0 of 16
RESULT commuting: monomials of Lg = 128
RESULT commuting: nonzero Euler-Lagrange expressions = 16 of 16
```

**In [6]: the anticommuting case against the record.**

```python
grassmann = results["grassmann"]
check(len(grassmann["Lg"].terms) > 0
      and (grassmann["Lg"] - grassmann["derivative_form"]).is_zero(),
      "real Grassmann field: Lg = (1/2) d_mu (sqrt|g| Theta^T C gamma^mu Theta), not 0",
      record=reproduces(PYREP, "negative_control_majorana_grassmann_total_derivative"))
check(all(e.is_zero() for e in grassmann["EL"]) and grassmann["mass"].is_zero(),
      "real Grassmann field: all 16 Euler-Lagrange expressions vanish and Theta^T C "
      "Theta = 0", record=reproduces(WLREP, "Majorana_Lg_total_derivative_grassmann"))
```

The first check: $L_g$ is not zero and equals its total-derivative form exactly. The second: all 16 Euler-Lagrange expressions vanish and $\Theta^TC\Theta = 0$. **Out [6]:** two PASS lines with their "reproduces" lines (`negative_control_majorana_grassmann_total_derivative` of the sympy report, `Majorana_Lg_total_derivative_grassmann` of the Wolfram report).

**In [7]: the commuting case, and Figure 07c.1.**

```python
commuting = results["commuting"]
phi = commuting["theta"]
operator = [RealJet(False) for _ in range(16)]  # gamma^mu D_mu Phi
for mu in range(8):
    D_phi = [x + y for x, y in zip(column(False, (mu,)), matvec(Om[mu], phi, False))]
    operator = [x + y for x, y in zip(operator, matvec(gam[mu], D_phi, False))]
expected = matvec(C * 2 * sqrt_g, operator, False)  # 2 sqrt|g| C gamma^mu D_mu Phi
nonzero = sum(1 for e in commuting["EL"] if not e.is_zero())
detail = revision_check(PYREP, "negative_control_majorana_commuting_contrast")["detail"]
recorded = int(re.search(r"in (\d+) of 16 components", detail).group(1))
check(nonzero == recorded == 16, "real commuting field: Lg gives nonzero "
      "Euler-Lagrange expressions in 16 of 16 components",
      record=reproduces(PYREP, "negative_control_majorana_commuting_contrast"))
vector_zero = all(dot(vecmat(phi, C, False), matvec(G[a], phi, False), False)
                  .is_zero() for a in range(8))
check(all((e - x).is_zero() for e, x in zip(commuting["EL"], expected))
      and vector_zero, "real commuting field: the expression is 2 sqrt|g| (C "
      "gamma^mu D_mu Phi)_A and Phi^T C gamma^(a) Phi = 0",
      record=reproduces(WLREP, "Majorana_Lg_commuting_control"))
```

`operator` is the column $\gamma^\mu D_\mu\Phi$ for the real commuting field, `expected` the column $2\sqrt{|g|}\,C\gamma^\mu D_\mu\Phi$ of Section 7.28. `recorded` is the number read from the detail text of the sympy check ("in 16 of 16 components"). The first check: 16 nonzero expressions, as recorded. `vector_zero` is true when $\Phi^TC\gamma^{(a)}\Phi = 0$ for all eight $a$. The second check: every expression equals the expected one, and the vector forms vanish.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
labels = ["real Grassmann", "real commuting"]
left.bar(labels, [len(grassmann["Lg"].terms), len(commuting["Lg"].terms)],
         color=["tab:blue", "tab:orange"])
left.set_ylabel("monomials of $L_g$")
left.set_title("$L_g$ is not zero in either case")
counts = [sum(1 for e in grassmann["EL"] if not e.is_zero()), nonzero]
right.bar(labels, counts, color=["tab:blue", "tab:orange"])
right.set_ylim(0, 17)
right.set_ylabel("nonzero Euler-Lagrange expressions")
right.set_title("Field equations from $L_g$")
for x, value in enumerate(counts):
    right.text(x, value + 0.4, f"{value} of 16", ha="center")
fig.tight_layout()
save_figure(fig, "majorana_control",
...)
```

Two bar charts: the number of monomials of $L_g$, and the number of nonzero Euler-Lagrange expressions with the text "0 of 16" and "16 of 16" written above the bars. **Out [7]:** two PASS lines with their "reproduces" lines and the figure. **What Figure 07c.1 shows.** The left panel shows that $L_g$ is not zero for either kind of numbers (136 and 128 monomials). The right panel shows the decisive difference: for anticommuting components no Euler-Lagrange expression survives, $L_g$ gives no field equation; for commuting components all 16 do.

**In [8]: all matrices that turn solutions into solutions.**

```python
Gn = [np.array(gm.tolist(), dtype=np.int64) for gm in G]  # exact integer arrays
products, commute_counts, degrees = [], [], []
for k in range(9):
    for subset in combinations(range(8), k):
        P = np.eye(16, dtype=np.int64)
        for a in subset:
            P = P @ Gn[a]  # gamma_(a1) ... gamma_(ak)
        products.append(P)
        degrees.append(k)
        commute_counts.append(sum(1 for a in range(8)
                                  if np.array_equal(P @ Gn[a], Gn[a] @ P)))
flat = np.array([P.reshape(256) for P in products])  # one row per product
gram = flat @ flat.T  # all traces tr(gamma_I^T gamma_J), exact integers
check(len(products) == 256 and np.array_equal(gram, 16 * np.eye(256, dtype=np.int64)),
      "the 256 products of gammas are orthogonal: a basis of all 16 x 16 matrices")
```

`Gn` holds the gammas as exact 64-bit integer arrays. The loops run over all subsets of the eight directions, by size $k = 0$ to 8 (`combinations(range(8), k)` lists the subsets of size $k$ in increasing order); `P` is the product of the gammas of the subset, starting from the identity. For each product the notebook stores it, its degree, and the number of gammas it commutes with. `flat` writes each product as one row of 256 numbers (`reshape(256)`), and `gram = flat @ flat.T` is the table of all traces $\mathrm{tr}(\gamma_I^T\gamma_J)$ (the sum of the products of corresponding entries is exactly this trace). The check: 256 products, and the table is 16 times the $256\times256$ identity.

```python
same = [i for i in range(256) if commute_counts[i] == 8]  # commute with all
reversed_ = [i for i in range(256) if commute_counts[i] == 0]  # anticommute with all
report("products that commute with all 8 gammas (degree)", [degrees[i] for i in same])
report("products that anticommute with all 8 gammas (degree)",
       [degrees[i] for i in reversed_])
GAMMAn = np.array(GAMMA.tolist(), dtype=np.int64)
check(len(same) == 1 and np.array_equal(products[same[0]], np.eye(16, dtype=np.int64)),
      "s = +1: the solutions M form a 1-dimensional space, spanned by the identity",
      record=reproduces(LEAD, "intertwiners_same_mass"))
check(len(reversed_) == 1 and (np.array_equal(products[reversed_[0]], GAMMAn)
                               or np.array_equal(products[reversed_[0]], -GAMMAn)),
      "s = -1: the solutions M form a 1-dimensional space, spanned by Gamma",
      record=reproduces(LEAD, "intertwiners_reversed_mass"))
```

`same` lists the products that commute with all eight gammas, `reversed_` those that commute with none (they anticommute with all eight); the trailing underscore avoids the name of Python's function `reversed`. Their degrees are reported. The two checks: exactly one product commutes with all, and it is the identity; exactly one anticommutes with all, and it is $\pm\Gamma$. **Out [8]:** a PASS line, `RESULT products that commute with all 8 gammas (degree) = [0]`, `RESULT products that anticommute with all 8 gammas (degree) = [8]`, and two PASS lines with their "reproduces" lines (`intertwiners_same_mass` and `intertwiners_reversed_mass`).

**In [9]: the commutation pattern, Figure 07c.2.**

```python
table = np.zeros((9, 9), dtype=int)  # rows: degree k, columns: number commuted with
for k, j in zip(degrees, commute_counts):
    table[k, j] += 1
binomials = [1, 8, 28, 56, 70, 56, 28, 8, 1]  # the number of products of k gammas
check(all(table[k, k if k % 2 else 8 - k] == binomials[k] for k in range(9)),
      "a product of k gammas commutes with k of them (k odd) or 8 - k (k even)")
```

`table[k, j]` counts the products of $k$ gammas that commute with $j$ of the eight. `binomials` are the numbers $\binom{8}{k}$ of products of $k$ gammas. The check: all $\binom{8}{k}$ products of $k$ gammas commute with exactly $k$ gammas for odd $k$ and $8 - k$ for even $k$ (Section 7.29).

```python
fig, ax = plt.subplots(figsize=(6.6, 5.4))
shown = np.where(table > 0, np.log10(np.maximum(table, 1)) + 0.3, 0.0)
image = ax.imshow(shown, cmap="Purples", vmin=0, vmax=2.3)
for k in range(9):
    for j in range(9):
        if table[k, j]:
            ax.text(j, k, str(table[k, j]), ha="center", va="center",
                    color="white" if table[k, j] > 20 else "black")
ax.add_patch(plt.Rectangle((7.5, -0.5), 1, 1, fill=False, edgecolor="red",
                           linewidth=2))
ax.add_patch(plt.Rectangle((-0.5, 7.5), 1, 1, fill=False, edgecolor="red",
                           linewidth=2))
ax.set_xticks(range(9))
ax.set_yticks(range(9))
ax.set_xlabel("number of the 8 gammas that the product commutes with")
ax.set_ylabel("number $k$ of gamma factors in the product")
ax.set_title("The 256 products of gammas")
ax.grid(False)
save_figure(fig, "commutation_pattern",
...)
```

A heat map of the table on a logarithmic colour scale (`np.log10` of the counts, shifted so that 1 is still visible, and 0 left white), with the counts written in, and two red frames (`plt.Rectangle`) around the two squares of the outer columns. **Out [9]:** a PASS line and the figure. **What Figure 07c.2 shows.** The counts form two diagonals: odd products on the line "commutes with $k$", even products on the line "commutes with $8 - k$". Only two squares reach the outer columns: the identity (row 0, column 8) and $\Gamma$ (row 8, column 0). Every matrix that commutes or anticommutes with all eight gammas is therefore a multiple of 1 or of $\Gamma$.

**In [10]: the two charge-conjugation matrices.**

```python
C_plus, C_minus = C, GAMMA * C
check(all(C_plus.inv() * g * C_plus == -g.T for g in G) and C_plus.T == C_plus,
      "calC_+ = C: calC_+^-1 gamma^a calC_+ = -(gamma^a)^T, real symmetric",
      record=reproduces(LEAD, "charge_conjugation_matrix_plus"))
check(all(C_minus.inv() * g * C_minus == g.T for g in G)
      and all(v.is_real for v in C_minus),
      "calC_- = Gamma C: calC_-^-1 gamma^a calC_- = +(gamma^a)^T, real",
      record=reproduces(LEAD, "charge_conjugation_matrix_minus"))
check(I16 * I16.conjugate() == I16 and GAMMA * GAMMA.conjugate() == I16,
      "M M* = 1 for M = 1 and M = Gamma: both reality conditions are consistent",
      record=reproduces(LEAD, "majorana_conditions_consistent"))
```

$\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$. The first check: $\mathcal{C}_+^{-1}\gamma^{(a)}\mathcal{C}_+ = -(\gamma^{(a)})^T$ for every gamma (`C_plus.inv()` is the inverse matrix), and $\mathcal{C}_+$ is symmetric. The second: $\mathcal{C}_-^{-1}\gamma^{(a)}\mathcal{C}_- = +(\gamma^{(a)})^T$, and $\mathcal{C}_-$ is real. The third: $MM^* = 1$ for $M = 1$ and $M = \Gamma$. **Out [10]:** three PASS lines with their "reproduces" lines (`charge_conjugation_matrix_plus`, `charge_conjugation_matrix_minus`, `majorana_conditions_consistent`).

**In [11]: real fields under charge conjugation, Figure 07c.3.**

```python
phi_bar_T = (r.T * C).T  # (Phi^T C)^T for the real column r
check((C_plus * phi_bar_T - r).applyfunc(sp.expand) == sp.zeros(16, 1)
      and (C_minus * phi_bar_T - GAMMA * r).applyfunc(sp.expand) == sp.zeros(16, 1),
      "for a real field Phi: calC_+ gives Phi itself, calC_- gives Gamma Phi")
currents = [sp.expand((-sp.I * r.T * C * g * r)[0, 0]) for g in G]
kinetic_reversed = all(GAMMA.T * C * g * GAMMA == -(C * g) for g in G)
check(all(j == 0 for j in currents) and GAMMA.T * C * GAMMA == C and kinetic_reversed,
      "real commuting field: J^a = 0 for every a; Gamma^T C Gamma = C and Gamma^T C "
      "gamma^a Gamma = -C gamma^a",
      record=reproduces(LEAD, "real_fields_charge_conjugation"))
```

`phi_bar_T` is $\bar\Phi^T = (\Phi^TC)^T$ for the real column `r` of In [2]. The first check: $\mathcal{C}_+\bar\Phi^T = \Phi$ and $\mathcal{C}_-\bar\Phi^T = \Gamma\Phi$. `currents` are the eight components $J^a = -i\Phi^TC\gamma^{(a)}\Phi$ for the real commuting column; `kinetic_reversed` tests $\Gamma^TC\gamma^{(a)}\Gamma = -C\gamma^{(a)}$ for all $a$. The second check: every $J^a = 0$, $\Gamma^TC\Gamma = C$, and the kinetic matrices are reversed.

```python
numbers = [np.array(M.tolist(), dtype=float) for M in
           (C, GAMMA.T * C * GAMMA, C * G[X4], GAMMA.T * C * G[X4] * GAMMA)]
titles = ["$C$", "$\\Gamma^T C\\,\\Gamma$ (equal)", "$C\\gamma^{(x_4)}$",
          "$\\Gamma^T C\\gamma^{(x_4)}\\Gamma$ (opposite)"]
fig, axes = plt.subplots(2, 2, figsize=(7.6, 7.4))
for ax, M, title in zip(axes.flat, numbers, titles):
    image = ax.imshow(M, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_title(title)
    ax.set_xticks([0, 7, 15], ["1", "8", "16"])
    ax.set_yticks([0, 7, 15], ["1", "8", "16"])
    ax.grid(False)
fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.6)
save_figure(fig, "gamma_map_matrices",
...)
```

Four heat maps in a $2\times2$ arrangement (`axes.flat` runs through the four panels): $C$, $\Gamma^TC\Gamma$, $C\gamma^{(x_4)}$ and $\Gamma^TC\gamma^{(x_4)}\Gamma$, with one common colour scale. **Out [11]:** two PASS lines (the second with its "reproduces" line, `real_fields_charge_conjugation`) and the figure. **What Figure 07c.3 shows.** The two upper maps are identical: $\Gamma$ keeps the scalar density. The two lower maps have the same pattern with every colour swapped: $\Gamma$ reverses the kinetic matrix of $x_4$ (and, as the check showed, of all eight directions).

**In [12]: the mass reversal in the author's metric.**

```python
def real_lagrangian(columns, mass, coupling):
    """sqrt|g| [K - mass S - (coupling/2) S^2] of the real field whose value and
    derivatives are columns(derivatives)."""
    field = columns(())
    bar = vecmat(field, C, False)  # Phi^T C
    K = RealJet(False)
    for mu in range(8):
        D_field = [x + y for x, y in zip(columns((mu,)), matvec(Om[mu], field, False))]
        D_bar = [x - y for x, y in zip(vecmat(columns((mu,)), C, False),
                                       vecmat(bar, Om[mu], False))]
        K = K + dot(bar, matvec(gam[mu], D_field, False), False)
        K = K - dot(vecmat(D_bar, gam[mu], False), field, False)
    S = dot(bar, field, False)
    return (K.times(sp.Rational(1, 2)) - S.times(mass)
            - (S * S).times(coupling / 2)).times(sqrt_g)
```

`real_lagrangian(columns, mass, coupling)` builds the Revision Lagrangian of a real commuting field whose value and derivatives are given by the function `columns(derivatives)`: the row $\bar\Phi = \Phi^TC$, the two halves of the kinetic term with the covariant derivatives $D_\mu\Phi$ and $D_\mu\bar\Phi = \partial_\mu\Phi^TC - \bar\Phi\Omega_\mu$, the scalar density, and $\sqrt{|g|}[\tfrac12K - mS - \tfrac{\lambda}{2}S^2]$ with the given mass and coupling.

```python
def plain(derivatives):  # the components of Phi
    return column(False, derivatives)


def mapped(derivatives):  # the components of Gamma Phi
    return matvec(GAMMA, column(False, derivatives), False)
```

Two ways to give the field: `plain` returns the components of $\Phi$ (or their derivatives), `mapped` those of $\Gamma\Phi$, that is $\sum_B\Gamma_{AB}\theta_B$ and the same for each derivative ($\Gamma$ is constant).

```python
L_mapped = real_lagrangian(mapped, m, lam)
L_reversed = real_lagrangian(plain, -m, -lam)
check((L_mapped + L_reversed).is_zero(), "real field in the author's metric: "
      "L_(m, lambda)[Gamma Phi] = -L_(-m, -lambda)[Phi]")
```

`L_mapped` is $\mathcal{L}_{m,\lambda}[\Gamma\Phi]$ and `L_reversed` is $\mathcal{L}_{-m,-\lambda}[\Phi]$; the check requires their sum to vanish exactly.

```python
L_real = real_lagrangian(plain, m, lam)
S_real = dot(vecmat(phi, C, False), phi, False)
residual = [x - (RealJet(False, {(): m}) + S_real.times(lam)) * y
            for x, y in zip(operator, phi)]  # gamma D Phi - (m + lambda S) Phi
target = matvec(C * 2 * sqrt_g, residual, False)
ok = True
for A in range(16):
    value = L_real.lderiv((A, ()))
    for mu in range(8):
        value = value - L_real.lderiv((A, (mu,))).total(mu)
    ok = ok and (value - target[A]).is_zero()
check(ok, "real commuting field: Euler-Lagrange expressions 2 sqrt|g| (C (gamma^mu "
      "D_mu Phi - (m + lambda S) Phi))_A")
```

`L_real` is $\mathcal{L}_{m,\lambda}[\Phi]$ and `S_real` the scalar density $\Phi^TC\Phi$. `residual` is the column $\gamma^\mu D_\mu\Phi - (m + \lambda S)\Phi$ (with `operator` from In [7]) and `target` is $2\sqrt{|g|}\,C$ times it. The loop computes the 16 Euler-Lagrange expressions of `L_real` and compares each with `target`. **Out [12]:** two PASS lines.

**In [13]: a real solution and its image.**

```python
mass_symbol = sp.Symbol("mu", real=True)


def M_of(mass):
    return -mass * G[X4] + 3 * H * G[X4] * G[X8]  # alpha = 0


check((GAMMA * M_of(mass_symbol) * GAMMA - M_of(-mass_symbol)).applyfunc(sp.expand)
      == Z16, "Gamma M_m Gamma = M_(-m): Gamma maps the family of mass m to mass -m")
```

`mass_symbol` is a real symbol $\mu$ for the mass, and `M_of(mass)` the matrix $M$ of the exact family of Section 7.23 with $\alpha = 0$. The check: $\Gamma M_\mu\Gamma = M_{-\mu}$ exactly, so $\Gamma$ maps the member of mass $\mu$ to the member of mass $-\mu$.

```python
Gf = [np.array(gm.tolist(), dtype=float) for gm in G]
GAMMAf = np.array(GAMMA.tolist(), dtype=float)
chi0 = np.zeros(16)
chi0[0], chi0[12] = 1.0, 2.0  # e_1 + 2 e_13: one component in each chiral half
times = np.linspace(0.0, 2.0, 201)
Mf = -2.0 * Gf[X4] + 3.0 * Gf[X4] @ Gf[X8]  # m = 2, H = 1
kk = np.sqrt(5.0)
Phi = np.array([(np.cosh(kk * t) * np.eye(16) + np.sinh(kk * t) / kk * Mf) @ chi0
                for t in times])
dPhi = np.array([(kk * np.sinh(kk * t) * np.eye(16) + np.cosh(kk * t) * Mf) @ chi0
                 for t in times])
```

The gammas and $\Gamma$ as floating-point arrays; `chi0` is $e_1 + 2e_{13}$ (one component in each chiral half); 201 times from 0 to 2; `Mf` is $M$ for $m = 2$, $H = 1$, and $k = \sqrt5$. `Phi` and `dPhi` are the real solution $\Phi = (\cosh kx_4 + \sinh(kx_4)/k\,M)\chi_0$ and its exact time derivative, one row per time.

```python
def residual_size(values, derivatives, mass):
    """The largest component of gamma4 d4 Psi + 3 gamma8 Psi - mass Psi."""
    return np.array([np.abs(Gf[X4] @ d + 3.0 * Gf[X8] @ v - mass * v).max()
                     for v, d in zip(values, derivatives)])
```

`residual_size(values, derivatives, mass)` returns, at every time, the largest component of $\gamma^{(x_4)}\partial_4\Psi + 3\gamma^{(x_8)}\Psi - \mathrm{mass}\,\Psi$, the residual of the field equation for a field of $x_4$ alone ($H = 1$).

```python
image_values, image_derivatives = Phi @ GAMMAf.T, dPhi @ GAMMAf.T  # Gamma Phi
size = np.abs(Phi).max(axis=1)
phi_plus = residual_size(Phi, dPhi, 2.0) / size
image_minus = residual_size(image_values, image_derivatives, -2.0) / size
image_plus = residual_size(image_values, image_derivatives, 2.0)
check(phi_plus.max() < 1e-12 and image_minus.max() < 1e-12
      and np.allclose(image_plus, 4.0 * size),
      "numerically: Phi solves the mass +2 equation, Gamma Phi the mass -2 equation "
      "(relative residuals below 1e-12); Gamma Phi fails the +2 equation by 2 m |Phi|")
```

The image $\Gamma\Phi$ and its derivative (`Phi @ GAMMAf.T` applies $\Gamma$ to every row). `phi_plus` is the relative residual of $\Phi$ in the equation of mass $+2$, `image_minus` that of $\Gamma\Phi$ in the equation of mass $-2$, and `image_plus` the residual of $\Gamma\Phi$ in the equation of mass $+2$. The check: the first two are below $10^{-12}$ at all times, and the third equals $2m = 4$ times the size of $\Phi$ (because $\Gamma\Phi$ solves the $-m$ equation, its residual in the $+m$ equation is $-2m\,\Gamma\Phi$). **Out [13]:** two PASS lines.

**In [14]: Figure 07c.4.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.8, 3.9))
left.plot(times, Phi[:, 0], label="$\\Phi_1$")
left.plot(times, image_values[:, 0], "--", label="$(\\Gamma\\Phi)_1 = -\\Phi_1$")
left.plot(times, Phi[:, 12], label="$\\Phi_{13}$")
left.plot(times, image_values[:, 12], ":", label="$(\\Gamma\\Phi)_{13} = \\Phi_{13}$")
left.set_xlabel("time $x_4$")
left.set_ylabel("component at $z = \\pi/4$")
left.set_title("A real solution and its image")
left.legend(fontsize=8)
right.semilogy(times, image_plus, label="$\\Gamma\\Phi$ in the mass $+m$ equation")
right.semilogy(times, size, ":", color="black", label="size of $\\Phi$")
right.set_xlabel("time $x_4$")
right.set_ylabel("largest residual component")
right.set_title("$\\Gamma\\Phi$ solves the mass $-m$ equation")
right.legend(fontsize=8)
fig.tight_layout()
save_figure(fig, "mass_reversal",
...)
```

Left: components 1 and 13 of $\Phi$ and of $\Gamma\Phi$ against the time; right: the residual of $\Gamma\Phi$ in the wrong equation and the size of $\Phi$ on a logarithmic axis. **What Figure 07c.4 shows.** Component 1 of the image is minus component 1 of $\Phi$ (the two curves are mirror images), component 13 is unchanged (the curves coincide): $\Gamma = \mathrm{diag}(-I_8, I_8)$. On the right the residual of $\Gamma\Phi$ in the equation of mass $+m$ runs parallel to the size of $\Phi$, a factor 4 above it; in the equation of mass $-m$ its residual is zero up to rounding. A real field carries no charge; the real matrix $\Gamma$ relates its solutions of mass $m$ to solutions of mass $-m$.

**In [15]: the last check.**

```python
names = ["majorana_control", "commutation_pattern", "gamma_map_matrices",
         "mass_reversal"]
files = [f"{FIGURE_FOLDER}/07c_{k}_{name}.png" for k, name in enumerate(names, 1)]
check(all(output_file(path).is_file() for path in files),
      "all 4 figure files of this notebook exist")
all_checks_passed()
```

The four figure files are checked and the last line printed. **Out [15]:** `PASS all 4 figure files of this notebook exist` and `ALL 23 CHECKS PASSED (notebook 07c)`.

### 7.34 What we proved, what we computed, what we assumed

**PROVED in this chapter** (each derivation written out line by line; each is also confirmed by a check of a notebook, and where the Revision record contains it, by the check of the Revision record named in the table after this list):

- the principle of stationary action gives the Euler-Lagrange equation $\partial L/\partial q - \frac{d}{dt}\partial L/\partial\dot q = 0$ (Line 1 by the chain rule, Line 2 by integration by parts, Line 3 because the shapes vanish at the ends, and the fundamental lemma); for the oscillator the action of a varied path is $S_0 + S_1\epsilon + S_2\epsilon^2$ with $S_2$ independent of the path, $S_2 = \frac{T}{4}(\frac{\pi^2}{T^2} - \omega^2)$ for the slowest shape, so the true path is a minimum for $T < \pi/\omega$ and a saddle beyond; the error of a bump average of the parabola path's $E = -2 - t^2$ (with $E'' = -2$) is $-(\tfrac13 - \tfrac{2}{\pi^2})w^2$, and for any quadratic $E$ it is $\tfrac12E''(\tfrac13 - \tfrac{2}{\pi^2})w^2$; the derivative of the grid action is $h$ times the grid Euler-Lagrange expression; $dH/dt = -\dot q E$; a total derivative changes no equation; a complex variable and its conjugate may be varied as if independent, $E_{\psi^*} = (E_{q_0} + iE_{q_1})/\sqrt2$ (Sections 7.2 to 7.4);
- the Euler-Lagrange expression of a field has one derivative term per coordinate; along a space direction a plane wave oscillates with $\omega^2 = m^2 + k^2$, along an extra time it grows with the rate $\kappa = \sqrt{k^2 - m^2}$ for $k > m$; $(\sum_ak_a\gamma^{(a)})^2 = \sum_a\eta^{aa}k_a^2\,I_{16}$, so the 16-component field has the same growth rate as the record (Section 7.5);
- the rules of Grassmann numbers: $\theta_i^2 = 0$; the sign of a reordering; $2^n$ monomials, $\binom{n}{k}$ of degree $k$; $YX = (-1)^{kl}XY$; the conjugation reverses products; $\partial_R F = -\partial_L F$ for even $F$; $(\Psi^\dagger M\Psi)^* = \Psi^\dagger M^\dagger\Psi$ for both statistics; a real Grassmann column keeps only the antisymmetric part of a matrix and a real commuting column only the symmetric part; $S^k$ has $\binom{16}{k}$ monomials with coefficients $\pm k!$ and $S^{17} = 0$; in the two-generator test algebra $S^3 = 0$; a first-order kinetic term of real Grassmann fields with an antisymmetric matrix is a total derivative (Sections 7.10 to 7.13);
- $\sqrt{|g|} = \cos z$, independent of the time; $\gamma^{x_i}\Omega_{x_i} = \tfrac12(a_4'\gamma^{(x_4)} + H\gamma^{(x_8)})$ for 3-space and $\gamma^{x_t}\Omega_{x_t} = \tfrac12(-a_4'\gamma^{(x_4)} + H\gamma^{(x_8)})$ for the extra times, so $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)} = \frac{1}{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$: the time terms cancel because the extra times deflate; $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$ (Section 7.18);
- the Lagrangian of both fields is real; it differs from the unsymmetrised form by the total divergence $\tfrac12\partial_\mu(\sqrt{|g|}\bar\Psi\gamma^\mu\Psi)$; in the author's metric the spin connection drops out of it (Section 7.20);
- its Euler-Lagrange equations are, for both statistics, $\gamma^\mu D_\mu\Psi = (m + \lambda S)\Psi$ and the Dirac-conjugate equation $(D_\mu\bar\Psi)\gamma^\mu = -(m + \lambda S)\bar\Psi$; written out in the author's metric they have the frame factors $e^{\mp a_4}\sin^{-1/6}z$, $1$, $\tan z$ and the term $3H\gamma^{(x_8)}\Psi$; they have a chiral block form and an evolution form with non-characteristic slices $x_4 = $ const (Sections 7.21 and 7.22);
- non-triviality [1] and [2] in the diagonal frame: the gravitational term $3H\gamma^{(x_8)}\Psi$ is nonzero for every $\Psi \neq 0$ and every $H > 0$, and $\Omega_\mu$ vanishes only for $a_4' = 0$ and $H = 0$; with the exact scope that the value of the term depends on the frame and on the variables (the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it, derived here), while $\Omega_\mu$ vanishes in no frame (Section 7.23);
- the exact family $\Psi = \sin^\alpha z\,(\cosh kx_4 + \sinh(kx_4)/k\,M)\chi_0$ with $M^2 = k^2 = 9H^2(2\alpha + 1)^2 - m^2$ and constant $S$ solves the field equation for every $a_4$ when $\lambda = 0$ (Section 7.23);
- the author's Majorana-type Lagrangian is a total derivative for real Grassmann fields (no field equation) and gives $2\sqrt{|g|}C\gamma^\mu D_\mu\Phi$ for real commuting fields; the Revision Lagrangian of a real commuting field gives the same field equation as the complex one, and its current vanishes (Section 7.28);
- charge conjugation is a MATRIX: every matrix $M$ with $M\gamma^{(a)} = s\gamma^{(a)}M$ for all $a$ is a multiple of $1$ ($s = +1$) or of $\Gamma$ ($s = -1$), because the 256 products of gammas are an orthogonal basis and only $1$ and $\Gamma$ commute or anticommute with all eight; hence $\mathcal{C}_+ = C$ with $\mathcal{C}_+^{-1}\gamma^{(a)}\mathcal{C}_+ = -(\gamma^{(a)})^T$ and $\mathcal{C}_- = \Gamma C$ with $\mathcal{C}_-^{-1}\gamma^{(a)}\mathcal{C}_- = +(\gamma^{(a)})^T$; both reality conditions are consistent; for a real field $\mathcal{C}_+$ is the identity and the nontrivial real map is $\Gamma$, with $\mathcal{L}_{m,\lambda}[\Gamma\Phi] = -\mathcal{L}_{-m,-\lambda}[\Phi]$; the signs of $S$ and $J$ under the two conjugations for both statistics (Section 7.29).

The checks of the Revision record that state the same results (the theory reports lie in the folder `Revision/theory/reports`, the lead's report is `Revision/lead_checks/reports/charge-conjugation-and-u1.json`):

| result | sections | Revision checks |
| --- | --- | --- |
| the Clifford square and the unbounded extra-time growth rate | 7.5 | `python-field-theory.json`, check `clifford_relations`; `python-scope.json`, check `extra_time_growth_rates_unbounded` |
| the Grassmann rules and the matrix $C$ | 7.10 to 7.13 | `wolfram-field-theory.json`, check `grassmann_algebra_structure`; `python-field-theory.json`, checks `superalgebra_axioms` and `C_properties` |
| the geometry and $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ | 7.18 | the table at the end of Section 7.18 |
| reality, total divergence, connection absent from $\mathcal{L}$ | 7.20 | `python-field-theory.json`, checks `grassmann_lagrangian_real`, `commuting_lagrangian_real`, `grassmann_total_divergence_relation` and `commuting_total_divergence_relation`; `wolfram-field-theory.json`, checks `L_spin_connection_drops_out_G` and `L_spin_connection_drops_out_C` |
| the Euler-Lagrange equations and the adjoint equation | 7.21 | the table at the end of Section 7.21 |
| explicit, block and evolution forms | 7.22 | `wolfram-field-theory.json`, checks `Dirac_operator_explicit_G`, `Dirac_operator_explicit_C`, `block_form`, `evolution_form_G` and `evolution_form_C`; formula record `Revision/theory/field-theory.json`, keys `field_equation_components` and `field_equation_blocks` |
| non-triviality, its scope, the exact family | 7.23 | the table at the end of Section 7.23 |
| the Majorana-type negative control; $J = 0$ for real fields | 7.28 | the table in Section 7.28; lead check `real_fields_charge_conjugation` |
| the charge-conjugation matrices and the sign table | 7.29 | lead checks `representation_real`, `spinor_connection_real`, `intertwiners_same_mass`, `intertwiners_reversed_mass`, `charge_conjugation_matrix_plus`, `charge_conjugation_matrix_minus`, `majorana_conditions_consistent`, `real_fields_charge_conjugation` and `bilinears_under_charge_conjugation` |

**COMPUTED by the notebooks** (each number in the cell named; exact unless an uncertainty is given):

- Notebook 07d: the first variations of the nine varied paths, for example $S_1 = -1/\pi = -0.318310$ for the line (In [2]); $S_2 = 2.217401$, $9.619604$, $21.956610$ (In [3]); the bump errors $-5.228\times10^{-3}$ to $-8.168\times10^{-5}$ with ratios 4.0000 (In [7], trapezoidal rule on 200001 points); the grid errors $4.089\times10^{-4}$ ($N = 4$) to $1.008\times10^{-7}$ ($N = 256$) with orders 2.007, 1.978, 2.001, 2.000, 2.000, 2.000 (In [9]); the energy $1/(2\sin^21) = 0.706141$ of the true path (In [10]); the grid derivative of the field action equal to $h_1h_4$ times the grid Euler-Lagrange expression to better than $10^{-9}$ at 20 inner points (In [14]); the record's growth rate for a momentum along $x_5$ (In [15]).
- Notebook 07a: 2000 of 2000 random sign comparisons (In [3]); 4096 monomials for $n = 12$ (In [6]); 27 nonzero products of the 64 (In [7]); the surviving monomials $[0, 8, \dots, 8]$ and $[8, 0, \dots, 0]$ (In [12]); the counts 16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440, 8008, 4368, 1820, 560, 120, 16, 1, 0 of $S^1$ to $S^{17}$ (In [14]).
- Notebook 07b: 25 Christoffel symbols and 12 connection components, equal to the formula record (In [7], In [8]); 392 and 408 monomials of $\mathcal{L}$, equal to the counts written in the record (In [13], In [14]); all 16 component equations equal to the formula record term by term (In [17]); $S = -2.000000$ and $-2.828427$ for the two exact solutions, constant along $x_4$, and the full residual below $10^{-12}$ of the size of $\Psi$ at 201 times (In [22], In [24]).
- Notebook 07c: 136 and 128 monomials of $L_g$, with 0 and 16 nonzero Euler-Lagrange expressions (In [5]); the 256 products orthogonal with the trace table $16\cdot1$, one product commuting with all gammas (degree 0) and one anticommuting with all (degree 8) (In [8]); the real solution of mass $+2$ and its image of mass $-2$ with relative residuals below $10^{-12}$ (In [13]).

**ASSUMED** (used, not derived here):

- the principle of stationary action, the starting principle of classical mechanics and field theory; standard theorems of calculus (differentiation under the integral sign, the fundamental theorem, Taylor's formula, the equality of mixed partial derivatives);
- the definition of the two fields by the Revision record (Revision/SPEC.md, section 3): dirac16complex has complex Grassmann components, dirac16complex00 ordinary complex components; the form of their common Lagrangian (the symmetrised kinetic term, the Dirac adjoint with $C$, the mass term $-mS$ and the potential $U = \frac{\lambda}{2}S^2$) is a choice of the theory, not a derivation; the method of varying jets (the field and its derivatives at a point treated as independent symbols);
- the author's gammas, $C$, $\Gamma$, $B$ and $S^{ab}$ with their properties (Chapters 4 and 5; read from `Revision/algebra/gammas.json` and checked again in the notebooks), the spin transformations and $R^TCR = C$ (Chapter 5), and the vielbein postulate as the definition of the canonical spin connection (Chapter 6);
- the illustration values ($H = 1$, $m = 2$, $\chi_0$, $z = \pi/4$) and, in Figure 07b.1 only, the linear history $a_4 = AHx_4$ with $A = 1$: a prescribed history chosen for the picture, not a result (every equation of the chapter holds for every $a_4(x_4)$);
- quoted from the record and derived in later chapters: the general covariant constancy of the gammas (`gamma_covariantly_constant`), the frame and scope statements of the scope reports, the boundary behaviour at $z = \pi/2$ and the growing modes without a boundary condition there (`good_sector_x8_independent_modes_without_boundary_condition`), and the quantum statements about conjugation (`quantum_charge_conjugation_unitary_type`; Chapters 8, 10 and 21).

**HYPOTHESIS.** No hypothesis enters this chapter. In particular the chapter does not use the author's hypothesis that the big bang creates universes in pairs; the mass reversal by $\Gamma$ is an exact map between solutions and says nothing about creation (Chapter 20).

**OPEN.** The chapter leaves open what the unbounded growth of extra-time modes means for the time evolution of the fields (no well-posed initial-value problem is claimed; Chapter 8), which boundary condition belongs at $z = \pi/2$ (none is imposed here), and, for the matter-antimatter question, everything that Chapter 21 lists as needed beyond this theory.

### 7.35 Exercises

**Exercise 1.** For the oscillator with $\omega = 1$, $T = 1$, $q(0) = 0$, $q(1) = 1$, compute the action of the line $q = t$ and of the true path $q = \sin t/\sin 1$. Which is smaller, and why must it be so?

*Answer.* Line: $\dot q = 1$, $L = \tfrac12 - \tfrac12t^2$, so $S = \int_0^1(\tfrac12 - \tfrac12t^2)\,dt = \tfrac12 - \tfrac16 = \tfrac13 = 0.333333$. True path: $\dot q = \cos t/\sin 1$, so $L = \frac{\cos^2t - \sin^2t}{2\sin^21} = \frac{\cos 2t}{2\sin^21}$ (the double-angle formula), and $S = \frac{1}{2\sin^21}\big[\tfrac12\sin2t\big]_0^1 = \frac{\sin2}{4\sin^21} = \frac{2\sin1\cos1}{4\sin^21} = \tfrac12\cot1 = 0.321046$. The true path has the smaller action. It must: the line is the true path plus the shape $\xi = t - \sin t/\sin 1$, which vanishes at both ends, so by Section 7.2 $S[\text{line}] = S_0 + S_1 + S_2[\xi]$ with $S_1 = 0$ (the true path is stationary) and $S_2[\xi] = \int_0^1(\tfrac12\dot\xi^2 - \tfrac12\xi^2)\,dt$. For the shapes $\sin(n\pi t)$ this coefficient is $(n^2\pi^2 - 1)/4 > 0$ (Section 7.2 with $T = 1$, $\omega = 1$; for $n = 1, 2, 3$ the values 2.217401, 9.619604, 21.956610 of Notebook 07d), and every smooth shape that vanishes at both ends is a combination of these sine shapes (a Fourier sine series; quoted here without proof), whose cross terms integrate to zero; so for $T = 1 < \pi$ the coefficient is positive for every nonzero such shape. Indeed $S[\text{line}] - S[\text{true}] = 0.333333 - 0.321046 = 0.012287 > 0$.

**Exercise 2.** Compute the first variation of the parabola $q = t^2$ for the shape $\xi_2 = \sin2\pi t$ in two ways: from the definition $S_1 = \int_0^1(\dot q\dot\xi - q\xi)\,dt$ and from $S_1 = \int_0^1E\xi\,dt$ with $E = -2 - t^2$. Compare with Notebook 07d.

*Answer.* Second way first: $\int_0^1\sin2\pi t\,dt = 0$ (a whole period), and $\int_0^1t^2\sin2\pi t\,dt = \big[-\frac{t^2\cos2\pi t}{2\pi}\big]_0^1 + \frac{1}{\pi}\int_0^1t\cos2\pi t\,dt = -\frac{1}{2\pi} + \frac1\pi\Big(\big[\frac{t\sin2\pi t}{2\pi}\big]_0^1 - \int_0^1\frac{\sin2\pi t}{2\pi}dt\Big) = -\frac{1}{2\pi} + 0$ (integration by parts twice; $\cos2\pi = 1$, $\sin2\pi = 0$). So $S_1 = -2\cdot0 - \big(-\frac{1}{2\pi}\big) = \frac{1}{2\pi}$. First way: $\dot q = 2t$, $\dot\xi = 2\pi\cos2\pi t$, so $S_1 = \int_0^1 4\pi t\cos2\pi t\,dt - \int_0^1t^2\sin2\pi t\,dt = 4\pi\cdot0 + \frac{1}{2\pi} = \frac{1}{2\pi}$, the same. Notebook 07d prints `parabola  n = 2: S1 = 1/(2*pi) = +0.159155` (In [2]).

**Exercise 3.** Let $F = 1 + 2\theta_0 + 3\theta_1\theta_2$ and $G = \theta_0 - \theta_1$. Compute $FG$ and $GF$, and explain the difference with the rule $YX = (-1)^{kl}XY$.

*Answer.* $FG = \theta_0 - \theta_1 + 2\theta_0\theta_0 - 2\theta_0\theta_1 + 3\theta_1\theta_2\theta_0 - 3\theta_1\theta_2\theta_1$. Here $\theta_0\theta_0 = 0$; $\theta_1\theta_2\theta_1 = -\theta_1\theta_1\theta_2 = 0$; and $\theta_1\theta_2\theta_0 = +\theta_0\theta_1\theta_2$ (two exchanges). So $FG = \theta_0 - \theta_1 - 2\theta_0\theta_1 + 3\theta_0\theta_1\theta_2$. $GF = \theta_0 + 2\theta_0\theta_0 + 3\theta_0\theta_1\theta_2 - \theta_1 - 2\theta_1\theta_0 - 3\theta_1\theta_1\theta_2 = \theta_0 - \theta_1 + 2\theta_0\theta_1 + 3\theta_0\theta_1\theta_2$. The difference $FG - GF = -4\theta_0\theta_1$ comes only from the odd part $2\theta_0$ of $F$ times the odd $G$: two odd elements anticommute ($k = l = 1$), while the even part $1 + 3\theta_1\theta_2$ commutes with everything ($k = 0$ or 2).

**Exercise 4.** For the odd monomial $F = \theta_0\theta_1\theta_2$ compute $\partial_LF/\partial\theta_1$ and $\partial_RF/\partial\theta_1$. Show that for every odd element the two derivatives are equal.

*Answer.* $\theta_1$ stands at position $p = 1$ of a monomial of degree $n = 3$. Moving it left passes one generator: $\partial_LF/\partial\theta_1 = -\theta_0\theta_2$. Moving it right passes $n - 1 - p = 1$ generator: $\partial_RF/\partial\theta_1 = -\theta_0\theta_2$. In general the two signs differ by $(-1)^{(n-1-p) - p} = (-1)^{n-1}$; for odd $n$ the exponent $n - 1$ is even, so the two derivatives of every odd monomial, and hence of every odd element, are equal (for even elements they are opposite, Section 7.11).

**Exercise 5.** A field with two complex Grassmann components has $S = \chi_0\psi_0 - \chi_1\psi_1$ (the matrix $C = \mathrm{diag}(1, -1)$). Compute $S^2$, $S^3$ and the "exponential" $1 + S + \tfrac12S^2 + \tfrac16S^3 + \dots$. Check the counts $\binom{2}{k}$ and the coefficients $\pm k!$ of Section 7.12.

*Answer.* The pairs $P_0 = \chi_0\psi_0$ and $P_1 = \chi_1\psi_1$ are even, commute and square to zero. $S^2 = P_0P_0 - P_0P_1 - P_1P_0 + P_1P_1 = -2P_0P_1 = -2\chi_0\psi_0\chi_1\psi_1$: one monomial ($\binom22 = 1$) with coefficient of size $2 = 2!$. $S^3 = S\cdot S^2 = -2(P_0 - P_1)P_0P_1 = 0$, because every term repeats a pair. So the series stops: $e^S = 1 + \chi_0\psi_0 - \chi_1\psi_1 - \chi_0\psi_0\chi_1\psi_1$, an exact finite sum. $S$ itself has $\binom21 = 2$ monomials with coefficients $\pm1 = \pm1!$.

**Exercise 6.** For two real components and $M = \begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix}$, compute $\Theta^TM\Theta$ for a real Grassmann column $\Theta = (\theta_0, \theta_1)^T$ and $q^TMq$ for a real column of ordinary numbers. Which part of $M$ does each keep?

*Answer.* $\Theta^TM\Theta = \theta_0\theta_0 + 2\theta_0\theta_1 + 3\theta_1\theta_0 + 4\theta_1\theta_1 = 2\theta_0\theta_1 - 3\theta_0\theta_1 = -\theta_0\theta_1$. The antisymmetric part of $M$ is $\tfrac12(M - M^T) = \begin{pmatrix}0 & -\frac12\\ \frac12 & 0\end{pmatrix}$, which gives $-\tfrac12\theta_0\theta_1 + \tfrac12\theta_1\theta_0 = -\theta_0\theta_1$, the same: only the antisymmetric part survives. For ordinary numbers $q^TMq = q_0^2 + 2q_0q_1 + 3q_1q_0 + 4q_1^2 = q_0^2 + 5q_0q_1 + 4q_1^2$, which is the form of the symmetric part $\begin{pmatrix}1 & \frac52\\ \frac52 & 4\end{pmatrix}$: only the symmetric part survives.

**Exercise 7.** Suppose the extra times INFLATED like 3-space, with the scale factor $e^{a_4}\sin^{1/6}z$ (that is $g_{55} = -e^{2a_4}\sin^{1/3}z$). Compute $\gamma^{x_5}\Omega_{x_5}$ and $\gamma^\mu\Omega_\mu$. What does this show about the author's metric?

*Answer.* Now $f_5 = Es$ and $g_{55} = -E^2s^2$, so $\partial_4g_{55} = -2E^2s^2A_1$. The Christoffel symbol and the connection component are

$$
\begin{aligned}
\Gamma^{x_4}{}_{x_5x_5} &= -\frac{\partial_4g_{55}}{2g_{44}} = -\frac{-2E^2s^2A_1}{-2} = -E^2s^2A_1, \\
\omega_{x_5(x_4)(x_5)} &= \frac{\eta_{44}f_4\,\Gamma^{x_4}{}_{x_5x_5}}{f_5} = \frac{E^2s^2A_1}{Es} = EsA_1 ,
\end{aligned}
$$

so the $a_4'$ part of $\Omega_{x_5}$ is $EsA_1S^{(x_4)(x_5)} = \tfrac12EsA_1\gamma^{(x_4)}\gamma^{(x_5)}$, and the $a_4'$ part of $\gamma^{x_5}\Omega_{x_5}$ is

$$
\frac{\gamma^{(x_5)}}{Es}\cdot\tfrac12EsA_1\gamma^{(x_4)}\gamma^{(x_5)} = \tfrac12A_1\gamma^{(x_5)}\gamma^{(x_4)}\gamma^{(x_5)} = \tfrac12A_1\gamma^{(x_4)}
$$

(as in Section 7.18, $\gamma^{(x_5)}\gamma^{(x_4)}\gamma^{(x_5)} = \gamma^{(x_4)}$). The $H$ part is unchanged, $\tfrac12H\gamma^{(x_8)}$, because the warp $\sin^{1/6}z$ is the same. So each of the six directions now contributes $+\tfrac12a_4'\gamma^{(x_4)}$, and $\gamma^\mu\Omega_\mu = 3a_4'\gamma^{(x_4)} + 3H\gamma^{(x_8)}$. The cancellation of the time terms in the author's metric is due to the DEFLATION of the extra times. This is the negative control of the lead's independent check `negative_control_inflating_extra_times` in the report `Revision/lead_checks/reports/emt-divergence-and-spin-connection.json`.

**Exercise 8.** In flat space with $m = 2$, a plane wave of the 16-component field has the frame momenta $k_8 = 1$ along the hidden direction and $k_7 = 3$ along an extra time, all others zero. Does it oscillate or grow, and at what rate?

*Answer.* By the Clifford square of Section 7.5, $\omega^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2 = 4 + 1 - 9 = -4 < 0$: it grows, with the rate $\sqrt{4} = 2$. This agrees with the record's formula $\sqrt{K^2 - k_1^2 - k_2^2 - k_3^2 - k_8^2 - m^2} = \sqrt{9 - 1 - 4} = 2$ with the extra-time momentum $K = 3$ (the record writes it for $x_5$; the three extra times enter the formula in the same way).

**Exercise 9.** The reality condition with the matrix $\Gamma$ is $\Psi = \Gamma\Psi^*$. What does it say about the 16 components? Is it consistent?

*Answer.* $\Gamma = \mathrm{diag}(-I_8, I_8)$, so the condition reads $\Psi_A = -\Psi_A^*$ for $A = 1, \dots, 8$ and $\Psi_A = \Psi_A^*$ for $A = 9, \dots, 16$: the upper eight components are purely imaginary and the lower eight real. It is consistent: applying it twice gives $\Psi = \Gamma(\Gamma\Psi^*)^* = \Gamma\Gamma\Psi = \Psi$, because $\Gamma$ is real and $\Gamma^2 = 1$ (the condition $MM^* = 1$ of Section 7.29).

**Exercise 10.** Show that for $U = \tfrac{\lambda}{2}S^2$ the map $\Gamma$ does NOT relate $\mathcal{L}_{m,\lambda}$ to $-\mathcal{L}_{-m,\lambda}$ when $\lambda \neq 0$: compute $\mathcal{L}_{m,\lambda}[\Gamma\Phi] + \mathcal{L}_{-m,\lambda}[\Phi]$ for a real commuting field.

*Answer.* By Section 7.29, $K[\Gamma\Phi] = -K[\Phi]$ and $S[\Gamma\Phi] = S[\Phi]$, so $\mathcal{L}_{m,\lambda}[\Gamma\Phi] = \sqrt{|g|}\,(-K - mS - \tfrac{\lambda}{2}S^2)$, while $\mathcal{L}_{-m,\lambda}[\Phi] = \sqrt{|g|}\,(K + mS - \tfrac{\lambda}{2}S^2)$. The sum is $-\lambda\sqrt{|g|}\,S^2$, which is not zero when $\lambda \neq 0$ and $S \neq 0$. The potential does not change sign under $\Gamma$, so the coupling must be reversed together with the mass: $(m, \lambda) \to (-m, -\lambda)$, as in Section 7.29.
