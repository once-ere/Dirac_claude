## 5. Classical field theory, Grassmann numbers, and why the notebook's Lg[] is empty

### 5.1 What this chapter does

Physics describes how things change. For a single particle the thing that changes is its position; for a field, such as the electromagnetic field or the dirac16complex field of this book, it is a list of numbers attached to every point of spacetime. In both cases the most economical way to write down the laws of change is to write down one function, the **Lagrangian**, and to demand that a certain integral of it, the **action**, does not change to first order when the motion is changed slightly. This one demand produces the equations of motion, called the **Euler–Lagrange equations**. The same Lagrangian also tells us which quantities are conserved (energy, momentum, charge), through a theorem of Emmy Noether, and it gives the **energy–momentum tensor**, the object that tells gravity where the energy is.

This chapter builds that machinery from zero. It then introduces **Grassmann numbers**, the anticommuting numbers ($\theta_1\theta_2=-\theta_2\theta_1$) that are needed to describe fermions such as electrons, and it ends with one of the first results of the dirac16complex project: the Lagrangian $\mathrm{Lg}[\,]$ that the author wrote in the notebook (cell 1064) contains no dynamics at all when its field is taken to be a real Grassmann field, as a fermion field must be. Its Euler–Lagrange equations read $0=0$. This is why the project had to replace $\mathrm{Lg}[\,]$ by a new Lagrangian (Chapter 6).

We use the conventions of the whole book (Chapter 1): everything is counted from 0; there are eight coordinates $x=(x_0,x_1,\dots,x_7)$; $x_4$ is the time; the flat metric is

$$
\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1),
$$

so directions 0 to 3 are space-like and directions 4 to 7 are time-like, and $x_5,x_6,x_7$ are called the three extra times. We write coordinates with a lower index, as the notebook does, and $\partial_\mu=\partial/\partial x_\mu$. A repeated index, one up and one down, is summed from 0 to 7 (the sum convention of Chapter 1).

The sources of this chapter are the Stage-1 document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md` (its §6 “Why the notebook Lagrangian Lg[] is empty for a Grassmann field” and §3 on the matrices), the contract `handoff/specs/CONTRACT.md` (its §3), the exact Grassmann-algebra code `scripts/grassmann_algebra.py` and `scripts/demo_grassmann_lagrangians.py`, and the report `artifacts/dirac16complex/arbitrary-field/grassmann-demo-report.json`.

### 5.2 The action of a particle and the Euler–Lagrange equation

**Setting.** A particle moves on a line. Its position at time $t$ is a number $q(t)$, and its velocity is $\dot q(t)=dq/dt$. A **Lagrangian** is a function $L(q,\dot q)$ of the position and the velocity; for a particle of mass $m$ in a potential $V(q)$ it is

$$
L(q,\dot q)=\tfrac12m\dot q^2-V(q),
$$

the kinetic energy minus the potential energy. A **path** is a function $q(t)$ on a time interval $t_A\le t\le t_B$. The **action** of a path is the number

$$
S[q]=\int_{t_A}^{t_B}L\bigl(q(t),\dot q(t)\bigr)\,dt .
$$

The square brackets say that $S$ depends on the whole function $q$, not on one number. A rule that turns a function into a number is called a **functional**.

**The principle of stationary action.** Among all paths with fixed end points $q(t_A)=q_A$ and $q(t_B)=q_B$, the path that the particle actually follows is one for which $S$ does not change to first order when the path is changed a little. To make this precise, pick any smooth function $\xi(t)$ with $\xi(t_A)=\xi(t_B)=0$ (a **variation**) and a small number $\epsilon$, and compare $q$ with $q+\epsilon\xi$. The path $q$ is **stationary** if

$$
\frac{d}{d\epsilon}S[q+\epsilon\xi]\Big|_{\epsilon=0}=0\qquad\text{for every such }\xi .
$$

**Derivation of the Euler–Lagrange equation.** Differentiate under the integral sign with the chain rule; the Lagrangian depends on $\epsilon$ through its first argument $q+\epsilon\xi$ and its second argument $\dot q+\epsilon\dot\xi$:

$$
\frac{d}{d\epsilon}S[q+\epsilon\xi]\Big|_{\epsilon=0}=\int_{t_A}^{t_B}\Bigl(\frac{\partial L}{\partial q}\,\xi+\frac{\partial L}{\partial\dot q}\,\dot\xi\Bigr)dt .
$$

The second term contains $\dot\xi$. Integrate it by parts, which is the product rule $\frac{d}{dt}(fg)=\dot fg+f\dot g$ integrated from $t_A$ to $t_B$:

$$
\int_{t_A}^{t_B}\frac{\partial L}{\partial\dot q}\,\dot\xi\,dt=\Bigl[\frac{\partial L}{\partial\dot q}\,\xi\Bigr]_{t_A}^{t_B}-\int_{t_A}^{t_B}\frac{d}{dt}\Bigl(\frac{\partial L}{\partial\dot q}\Bigr)\xi\,dt .
$$

The bracket vanishes because $\xi(t_A)=\xi(t_B)=0$. Hence

$$
\frac{d}{d\epsilon}S[q+\epsilon\xi]\Big|_{\epsilon=0}=\int_{t_A}^{t_B}E(t)\,\xi(t)\,dt,\qquad E:=\frac{\partial L}{\partial q}-\frac{d}{dt}\frac{\partial L}{\partial\dot q}.
$$

**The fundamental lemma.** If a continuous function $E(t)$ satisfies $\int E\xi\,dt=0$ for every smooth $\xi$ that vanishes at the end points, then $E=0$ everywhere. *Proof.* Suppose $E(t_0)>0$ at some interior time $t_0$. By continuity $E>0$ on a small interval around $t_0$. Choose $\xi$ positive inside that interval and zero outside (a smooth “bump”). Then $\int E\xi\,dt>0$, a contradiction. The case $E(t_0)<0$ is the same with the sign reversed. $\square$

So a stationary path satisfies the **Euler–Lagrange equation**

$$
\frac{\partial L}{\partial q}-\frac{d}{dt}\frac{\partial L}{\partial\dot q}=0 .
$$

With several coordinates $q_0,\dots,q_{n-1}$ one varies each separately and obtains one equation for each $q_i$.

**Worked example (the harmonic oscillator).** Take $m=1$ and $V=\tfrac12\omega^2q^2$. Then $\partial L/\partial q=-\omega^2q$ and $\partial L/\partial\dot q=\dot q$, so the Euler–Lagrange equation is $-\omega^2q-\ddot q=0$, that is $\ddot q=-\omega^2q$. Its solutions are $q(t)=A\cos\omega t+B\sin\omega t$. For $\omega=2$, $A=1$, $B=0$: $q(t)=\cos2t$, $\ddot q=-4\cos2t=-\omega^2q$, as required.

**Energy.** For a Lagrangian that does not depend explicitly on $t$ the quantity $H:=\dot q\,\partial L/\partial\dot q-L$ is constant along every solution. *Proof.* $\frac{dH}{dt}=\ddot q\frac{\partial L}{\partial\dot q}+\dot q\frac{d}{dt}\frac{\partial L}{\partial\dot q}-\frac{\partial L}{\partial q}\dot q-\frac{\partial L}{\partial\dot q}\ddot q=\dot q\Bigl(\frac{d}{dt}\frac{\partial L}{\partial\dot q}-\frac{\partial L}{\partial q}\Bigr)=0$. $\square$ For the oscillator $H=\tfrac12\dot q^2+\tfrac12\omega^2q^2$, the kinetic plus the potential energy. $H$ written as a function of $q$ and the **momentum** $p:=\partial L/\partial\dot q$ is the **Hamiltonian**; it returns in Chapter 8.

### 5.3 Fields, Lagrangian densities and the field equations

**A field** is a rule that assigns numbers to every point $x=(x_0,\dots,x_7)$ of spacetime. A **scalar field** $\phi(x)$ assigns one real number; the dirac16complex field assigns 16 numbers $\Psi_0(x),\dots,\Psi_{15}(x)$ (of a new kind, Section 5.9). We write a general field as a list $\phi_A(x)$, $A=0,1,\dots$, of components.

**Lagrangian density and action.** For a field the Lagrangian is replaced by a **Lagrangian density** $\mathcal L$, a function of the field components $\phi_A$, their first derivatives $\partial_\mu\phi_A$, and possibly the point $x$ itself. The action of a field configuration in a region $R$ of spacetime is the eight-fold integral

$$
S[\phi]=\int_R\mathcal L\bigl(\phi_A(x),\partial_\mu\phi_A(x),x\bigr)\,d^8x,\qquad d^8x=dx_0\,dx_1\cdots dx_7 .
$$

Time is now just one of the eight coordinates, and the region $R$ plays the role of the time interval $[t_A,t_B]$.

**The divergence theorem in the form we need.** Let $V^\mu(x)$, $\mu=0,\dots,7$, be eight smooth functions that vanish near the boundary of a box $R=[a_0,b_0]\times\dots\times[a_7,b_7]$. Then

$$
\int_R\partial_\mu V^\mu\,d^8x=0 .
$$

*Proof.* The sum $\partial_\mu V^\mu$ has eight terms. In the term $\partial_0V^0$ do the $x_0$ integral first: by the fundamental theorem of calculus it equals $V^0(b_0,\dots)-V^0(a_0,\dots)=0$. The same holds for each of the other seven terms, doing the corresponding integral first. $\square$ (For a general region the integral equals a flux through the boundary, which vanishes when $V$ vanishes near the boundary; the box is enough for everything in this book.) An expression of the form $\partial_\mu V^\mu$ is called a **total divergence** or **total derivative**.

**Derivation of the field equations.** Vary every component, $\phi_A\to\phi_A+\epsilon\xi_A$, where the functions $\xi_A(x)$ vanish near the boundary of $R$. Exactly as in Section 5.2,

$$
\frac{d}{d\epsilon}S\Big|_{\epsilon=0}=\int_R\Bigl(\frac{\partial\mathcal L}{\partial\phi_A}\xi_A+\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)}\partial_\mu\xi_A\Bigr)d^8x .
$$

Here $\partial\mathcal L/\partial(\partial_\mu\phi_A)$ means: treat the eight numbers $\partial_0\phi_A,\dots,\partial_7\phi_A$ as independent variables of the function $\mathcal L$ and differentiate with respect to one of them. The product rule gives $\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)}\partial_\mu\xi_A=\partial_\mu\bigl(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)}\xi_A\bigr)-\partial_\mu\bigl(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)}\bigr)\xi_A$. The first piece is a total divergence of a function that vanishes near the boundary, so its integral is zero. Therefore

$$
\frac{d}{d\epsilon}S\Big|_{\epsilon=0}=\int_R E^A\xi_A\,d^8x,\qquad E^A:=\frac{\partial\mathcal L}{\partial\phi_A}-\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)} .
$$

The fundamental lemma, applied with a bump in one component $\xi_A$ at a time, gives the **Euler–Lagrange field equations**

$$
E^A=\frac{\partial\mathcal L}{\partial\phi_A}-\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)}=0\qquad\text{for every component }A .
$$

In $\partial_\mu(\dots)$ the derivative is the **total** derivative with respect to $x_\mu$: it acts on the explicit $x$-dependence of $\mathcal L$ and, through the chain rule, on the fields inside it. The expression $E^A$ is called the **Euler–Lagrange expression** of the component $A$.

### 5.4 Total derivatives change nothing

**Proposition 5.1.** If $\mathcal L=\partial_\mu V^\mu$, where each $V^\mu$ is a function of the fields $\phi_A$ and of $x$ (but not of the derivatives of the fields), then every Euler–Lagrange expression vanishes identically: $E^A=0$ for every field configuration, whether or not it satisfies any equation.

*Proof by the action.* Take any variation $\xi_A$ that vanishes near the boundary. The Lagrangian evaluated on $\phi+\epsilon\xi$ is the total divergence of the functions $x\mapsto V^\mu(\phi(x)+\epsilon\xi(x),x)$, so

$$
S[\phi+\epsilon\xi]-S[\phi]=\int_R\partial_\mu\Bigl(V^\mu(\phi+\epsilon\xi,x)-V^\mu(\phi,x)\Bigr)d^8x=0\qquad\text{for every }\epsilon,
$$

by the divergence theorem, because the bracket vanishes near the boundary (there $\xi=0$). Hence $\frac{d}{d\epsilon}S[\phi+\epsilon\xi]=0$, that is $\int E^A\xi_A\,d^8x=0$ for every $\xi$, and the fundamental lemma gives $E^A=0$ for every $\phi$. $\square$

*Proof by direct computation.* By the chain rule $\partial_\mu V^\mu=\partial^{\mathrm{expl}}_\mu V^\mu+\frac{\partial V^\mu}{\partial\phi_B}\partial_\mu\phi_B$, where $\partial^{\mathrm{expl}}_\mu$ differentiates only the explicit $x$-dependence. Then $\frac{\partial\mathcal L}{\partial(\partial_\nu\phi_A)}=\frac{\partial V^\nu}{\partial\phi_A}$ and $\frac{\partial\mathcal L}{\partial\phi_A}=\partial^{\mathrm{expl}}_\mu\frac{\partial V^\mu}{\partial\phi_A}+\frac{\partial^2V^\mu}{\partial\phi_A\partial\phi_B}\partial_\mu\phi_B=\partial_\mu\Bigl(\frac{\partial V^\mu}{\partial\phi_A}\Bigr)$, the total derivative of the function $\partial V^\mu/\partial\phi_A$. Hence $E^A=\partial_\mu(\partial V^\mu/\partial\phi_A)-\partial_\nu(\partial V^\nu/\partial\phi_A)=0$. $\square$

The consequence is used again and again: **adding a total divergence to a Lagrangian density does not change its field equations**, and a Lagrangian density that is nothing but a total divergence has the empty field equations $0=0$. It describes nothing.

**Worked example.** One field $\phi$ in one dimension $x$, $V=\phi^2$, so $\mathcal L=\frac{d}{dx}(\phi^2)=2\phi\phi'$. Then $\partial\mathcal L/\partial\phi=2\phi'$ and $\partial\mathcal L/\partial\phi'=2\phi$, so $E=2\phi'-\frac{d}{dx}(2\phi)=0$ for every function $\phi$.

### 5.5 Worked example: a scalar field in 4+4 dimensions

Take one real scalar field $\phi$ in flat space with the metric $\eta$ and

$$
\mathcal L=-\tfrac12\eta^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi-V(\phi),\qquad V(\phi)=\tfrac12m^2\phi^2 .
$$

Written out, $\eta^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi=\sum_{i=0}^{3}(\partial_i\phi)^2-\sum_{j=4}^{7}(\partial_j\phi)^2$. For a field that depends only on the time $x_4$ this Lagrangian is $\tfrac12\dot\phi^2-V$ (a dot is $\partial_4$), the kinetic minus the potential energy, exactly as for the particle. This is the sign convention of the whole project (`handoff/specs/CONTRACT.md`, its §0); it is the same function as the $\tfrac12\partial_\mu\phi\,\partial^\mu\phi-V$ of the scalar-field reference that the task supplied (a private input that is not in the repository; the Stage-1 document quotes its formulas in its §2.3), which uses the signature $(+,-,-,-)$ with time first.

**Field equation.** $\partial\mathcal L/\partial\phi=-m^2\phi$ and $\partial\mathcal L/\partial(\partial_\mu\phi)=-\eta^{\mu\nu}\partial_\nu\phi$ (the factor $\tfrac12$ is cancelled because $\partial_\mu\phi$ occurs twice in the product). The Euler–Lagrange equation $-m^2\phi+\partial_\mu(\eta^{\mu\nu}\partial_\nu\phi)=0$ is

$$
\eta^{\mu\nu}\partial_\mu\partial_\nu\phi=m^2\phi,\qquad\text{i.e.}\qquad \sum_{i=0}^{3}\partial_i^2\phi-\partial_4^2\phi-\sum_{j=5}^{7}\partial_j^2\phi=m^2\phi .
$$

With one time (signature (7,1)) this would be the ordinary Klein–Gordon wave equation. With four time-like directions it is called **ultrahyperbolic**.

**Plane waves.** Try $\phi=\cos\bigl(\sum_{j\ne4}k_jx_j-\omega x_4\bigr)$ with constant real $k_j$ and $\omega$. Each $\partial_j^2$ produces $-k_j^2\phi$ and $\partial_4^2$ produces $-\omega^2\phi$, so the field equation becomes $-\sum_{i=0}^{3}k_i^2+\omega^2+\sum_{j=5}^{7}k_j^2=m^2$, that is

$$
\omega^2=m^2+k_0^2+k_1^2+k_2^2+k_3^2-k_5^2-k_6^2-k_7^2 .
$$

A wave number $k_5,k_6,k_7$ along an extra time **lowers** $\omega^2$. For $m=1$, $k_1=1$ and $k_5=1$ we get $\omega^2=1$: an ordinary oscillation. For $m=1$, $k_1=1$ and $k_5=2$ we get $\omega^2=1+1-4=-2$: no real $\omega$ exists. The solution of the equation with this $k$ is then $\cos(k\cdot x)\,e^{\pm\sqrt2\,x_4}$, which grows exponentially in time. The same phenomenon, for the dirac16complex field, is the “unstable extra-time modes” of Chapter 8.

### 5.6 First-order Lagrangians and complex fields

The Lagrangians so far were quadratic in the velocities. The Lagrangian of a fermion is instead **linear** in the time derivative. This section shows, with two small examples, that such Lagrangians are perfectly good and what is special about them.

**Example A (two real coordinates).** Let $q_0(t)$, $q_1(t)$ be two real coordinates and

$$
L=\tfrac12\bigl(q_0\dot q_1-q_1\dot q_0\bigr)-\tfrac12\omega\bigl(q_0^2+q_1^2\bigr).
$$

For $q_0$: $\partial L/\partial q_0=\tfrac12\dot q_1-\omega q_0$ and $\partial L/\partial\dot q_0=-\tfrac12q_1$, whose time derivative is $-\tfrac12\dot q_1$. The Euler–Lagrange equation is $\tfrac12\dot q_1-\omega q_0+\tfrac12\dot q_1=0$, that is $\dot q_1=\omega q_0$. For $q_1$: $\partial L/\partial q_1=-\tfrac12\dot q_0-\omega q_1$ and $\partial L/\partial\dot q_1=\tfrac12q_0$, so $-\tfrac12\dot q_0-\omega q_1-\tfrac12\dot q_0=0$, that is $\dot q_0=-\omega q_1$. The solution with $q_0(0)=1$, $q_1(0)=0$ is $q_0=\cos\omega t$, $q_1=\sin\omega t$: a rotation. Three features matter later. The equations are of **first order** in time, so the initial positions alone fix the motion (no initial velocities are needed). The **momenta** $p_0=\partial L/\partial\dot q_0=-\tfrac12q_1$ and $p_1=\partial L/\partial\dot q_1=\tfrac12q_0$ are not new variables: they are fixed functions of the coordinates. Such relations are called **constraints**; they are the reason why the quantization of the dirac16complex field in Chapter 8 needs care. And the part $\tfrac12(q_0\dot q_1-q_1\dot q_0)$ is **not** a total derivative, although it is antisymmetric in $(q_0,q_1)$: its Euler–Lagrange expressions are $\dot q_1$ and $-\dot q_0$, not zero. Keep this in mind; for anticommuting variables exactly the same expression will turn out to be a total derivative (Section 5.11).

**Example B (one complex coordinate).** A **complex number** is $z=x+iy$ with real $x$, $y$ and $i^2=-1$; its complex conjugate is $z^\ast=x-iy$, and $z^\ast z=x^2+y^2\ge0$ (Chapter 1). Combine the two real coordinates into one complex coordinate $\psi=(q_0+iq_1)/\sqrt2$. Then $\psi^\ast\psi=\tfrac12(q_0^2+q_1^2)$, and multiplying out gives $\psi^\ast\dot\psi-\dot\psi^\ast\psi=i(q_0\dot q_1-q_1\dot q_0)$. The real Lagrangian

$$
L=\tfrac i2\bigl(\psi^\ast\dot\psi-\dot\psi^\ast\psi\bigr)-\omega\,\psi^\ast\psi=\tfrac12\bigl(q_1\dot q_0-q_0\dot q_1\bigr)-\tfrac12\omega\bigl(q_0^2+q_1^2\bigr)
$$

is Example A with the sense of rotation reversed. **One may vary $\psi$ and $\psi^\ast$ as if they were independent.** The reason is that $(q_0,q_1)\mapsto(\psi,\psi^\ast)$ is a linear change of variables with constant coefficients that can be inverted, $q_0=(\psi+\psi^\ast)/\sqrt2$ and $q_1=(\psi-\psi^\ast)/(i\sqrt2)$. With the derivatives $\partial/\partial\psi=\tfrac1{\sqrt2}(\partial/\partial q_0-i\,\partial/\partial q_1)$ and $\partial/\partial\psi^\ast=\tfrac1{\sqrt2}(\partial/\partial q_0+i\,\partial/\partial q_1)$ one checks $\partial\psi/\partial\psi=1$ and $\partial\psi^\ast/\partial\psi=0$, and the Euler–Lagrange expressions combine in the same way, $E_{\psi^\ast}=\tfrac1{\sqrt2}(E_{q_0}+iE_{q_1})$ and $E_\psi=\tfrac1{\sqrt2}(E_{q_0}-iE_{q_1})$. So $E_\psi=E_{\psi^\ast}=0$ holds exactly when $E_{q_0}=E_{q_1}=0$.

Varying $\psi^\ast$: $\partial L/\partial\psi^\ast=\tfrac i2\dot\psi-\omega\psi$ and $\partial L/\partial\dot\psi^\ast=-\tfrac i2\psi$, so the Euler–Lagrange equation is $\tfrac i2\dot\psi-\omega\psi+\tfrac i2\dot\psi=0$, that is

$$
i\dot\psi=\omega\psi,\qquad\psi(t)=e^{-i\omega t}\psi(0).
$$

This is a Schrödinger equation with the “Hamiltonian” $\omega$. Varying $\psi$ gives the complex conjugate equation $-i\dot\psi^\ast=\omega\psi^\ast$. The dirac16complex Lagrangian of Chapter 6 has exactly this structure, with $\psi$ replaced by a column of 16 anticommuting components and $\omega$ by a $16\times16$ matrix operator (Chapter 8).

### 5.7 Symmetries and Noether's theorem

**Definition.** A **continuous symmetry** of a Lagrangian density is a family of changes of the fields, $\phi_A\to\phi_A+\epsilon\,\Delta\phi_A+O(\epsilon^2)$, under which $\mathcal L$ changes, to first order in $\epsilon$, only by a total divergence: $\mathcal L\to\mathcal L+\epsilon\,\partial_\mu K^\mu$ for every field configuration (not only for solutions). By Section 5.4 such a change does not alter the field equations.

**Theorem 5.2 (Noether).** For a continuous symmetry the **current**

$$
j^\mu=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)}\,\Delta\phi_A-K^\mu
$$

satisfies $\partial_\mu j^\mu=0$ for every solution of the field equations.

*Proof.* To first order in $\epsilon$ the change of $\mathcal L$ is $\epsilon\bigl(\frac{\partial\mathcal L}{\partial\phi_A}\Delta\phi_A+\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)}\partial_\mu\Delta\phi_A\bigr)$. On a solution the field equation replaces $\partial\mathcal L/\partial\phi_A$ by $\partial_\mu\bigl(\partial\mathcal L/\partial(\partial_\mu\phi_A)\bigr)$, and the product rule turns the bracket into $\partial_\mu\bigl(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)}\Delta\phi_A\bigr)$. By assumption the change equals $\epsilon\,\partial_\mu K^\mu$. Subtracting gives $\partial_\mu j^\mu=0$. $\square$

**Conserved charge.** Integrate $j^4$ over a slice $x_4=\text{const}$, whose seven coordinates are $x_0,x_1,x_2,x_3,x_5,x_6,x_7$: $Q(x_4)=\int j^4\,d^7x$. Then $dQ/dx_4=\int\partial_4j^4\,d^7x=-\sum_{j\ne4}\int\partial_jj^j\,d^7x=0$ when the fields vanish far away, by the divergence theorem of Section 5.3 on the slice. So $Q$ does not change in time. (The overall sign of a current is a convention.)

**Example 1 (phase symmetry).** In Example B of Section 5.6 the change $\psi\to e^{i\alpha}\psi$, $\psi^\ast\to e^{-i\alpha}\psi^\ast$ leaves $L$ unchanged ($K=0$). To first order $\Delta\psi=i\psi$ and $\Delta\psi^\ast=-i\psi^\ast$. The “current” has only a time component, $j=\frac{\partial L}{\partial\dot\psi}\,i\psi+\frac{\partial L}{\partial\dot\psi^\ast}(-i\psi^\ast)=\tfrac i2\psi^\ast\,i\psi-\tfrac i2\psi\,(-i\psi^\ast)=-\psi^\ast\psi$. Its conservation says $\psi^\ast\psi$ is constant, which the solution $e^{-i\omega t}\psi(0)$ confirms. For the dirac16complex field the same symmetry gives the conserved current $J^\mu=-i\bar\Psi\gamma^\mu\Psi$ (Chapter 7) and the charge of Chapter 8.

**Example 2 (translations and the canonical energy–momentum tensor).** If $\mathcal L$ does not depend explicitly on $x$, shifting the field, $\phi_A(x)\to\phi_A(x+\epsilon e_\nu)$ with $e_\nu$ the unit step in direction $\nu$, is a symmetry: $\Delta\phi_A=\partial_\nu\phi_A$, and $\mathcal L$ changes by $\epsilon\,\partial_\nu\mathcal L=\epsilon\,\partial_\mu(\delta^\mu{}_\nu\mathcal L)$, so $K^\mu=\delta^\mu{}_\nu\mathcal L$ ($\delta^\mu{}_\nu$ is 1 for $\mu=\nu$ and 0 otherwise). Noether's theorem gives eight conserved currents, one for each $\nu$, collected in the **canonical energy–momentum tensor**

$$
\Theta^\mu{}_\nu=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)}\,\partial_\nu\phi_A-\delta^\mu{}_\nu\,\mathcal L,\qquad \partial_\mu\Theta^\mu{}_\nu=0\ \text{on solutions}.
$$

The component $\Theta^4{}_4=\frac{\partial\mathcal L}{\partial(\partial_4\phi_A)}\partial_4\phi_A-\mathcal L$ is the field version of the energy $H=\dot q\,\partial L/\partial\dot q-L$ of Section 5.2: it is the **energy density**, and $\int\Theta^4{}_4\,d^7x$ is the conserved energy.

**The scalar field in 4+4 dimensions.** For the $\mathcal L$ of Section 5.5, $\partial\mathcal L/\partial(\partial_\mu\phi)=-\eta^{\mu\lambda}\partial_\lambda\phi$, so $\Theta^\mu{}_\nu=-\eta^{\mu\lambda}\partial_\lambda\phi\,\partial_\nu\phi-\delta^\mu{}_\nu\mathcal L$. With $\eta^{44}=-1$ the energy density is

$$
\rho=\Theta^4{}_4=\tfrac12(\partial_4\phi)^2+\tfrac12\sum_{i=0}^{3}(\partial_i\phi)^2-\tfrac12\sum_{j=5}^{7}(\partial_j\phi)^2+V(\phi).
$$

(Derivation: $\Theta^4{}_4=(\partial_4\phi)^2-\mathcal L$ and $-\mathcal L=\tfrac12\sum_{i\le3}(\partial_i\phi)^2-\tfrac12(\partial_4\phi)^2-\tfrac12\sum_{j\ge5}(\partial_j\phi)^2+V$.) The gradients along the extra times enter with a **minus** sign. For example, at $x_4=0$ take $\partial_4\phi=0$ and $\phi=\epsilon\sin(kx_5)$ with $m=1$: then $\rho=\tfrac12\epsilon^2\bigl(\sin^2(kx_5)-k^2\cos^2(kx_5)\bigr)$, whose average over $x_5$ is $\tfrac14\epsilon^2(1-k^2)$, negative for $k>1$ and as negative as we like for large $k$. The energy of a scalar field in 4+4 dimensions is not bounded below; this is the classical face of the extra-time instability of Chapter 8. This observation is derived here; it is not a check of the repository.

### 5.8 The energy–momentum tensor

**Flat space.** For the scalar field define

$$
T_{\mu\nu}:=-\eta_{\mu\rho}\,\Theta^\rho{}_\nu=\partial_\mu\phi\,\partial_\nu\phi+\eta_{\mu\nu}\,\mathcal L .
$$

It is symmetric in $\mu,\nu$, it is conserved, and its sign is chosen so that $T_{44}=\Theta^4{}_4=\rho$ is the energy density (the project fixes the sign of every energy–momentum tensor this way; Stage-1 document, §1.2).

**Curved space.** In a gravitational field (Chapter 4) the flat metric $\eta_{\mu\nu}$ is replaced by a metric $g_{\mu\nu}(x)$ with inverse $g^{\mu\nu}$, and the volume element $d^8x$ by $\sqrt{|g|}\,d^8x$, where $g=\det(g_{\mu\nu})$. The scalar action becomes

$$
S=\int\sqrt{|g|}\,\Bigl(-\tfrac12g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi-V(\phi)\Bigr)d^8x=\int\sqrt{|g|}\,\mathcal L_\phi\,d^8x .
$$

The energy–momentum tensor is **defined** by how the action responds to a change of the metric:

$$
T_{\mu\nu}:=-\frac{2}{\sqrt{|g|}}\,\frac{\delta S}{\delta g^{\mu\nu}},
$$

where $\delta S/\delta g^{\mu\nu}$ is the function that multiplies $\delta g^{\mu\nu}(x)$ in the first-order change of $S$ when $g^{\mu\nu}$ is changed by a small symmetric $\delta g^{\mu\nu}(x)$ that vanishes near the boundary. It is the object that appears on the right-hand side of Einstein's equations (Chapter 4 and Chapter 9).

**Jacobi's formula.** We need the change of $\sqrt{|g|}$. First, for a square matrix $A$ and a small number $\epsilon$, $\det(1+\epsilon A)=1+\epsilon\,\mathrm{tr}A+O(\epsilon^2)$. *Proof.* The determinant is a sum over permutations of products of one entry from each row and each column. The identity permutation gives $\prod_i(1+\epsilon A_{ii})=1+\epsilon\sum_iA_{ii}+O(\epsilon^2)$. Every other permutation moves at least two indices, so its product contains at least two off-diagonal entries $\epsilon A_{ij}$ and is $O(\epsilon^2)$. $\square$ Hence $\det(g+\delta g)=\det g\,\det(1+g^{-1}\delta g)=\det g\,(1+g^{\mu\nu}\delta g_{\mu\nu})$ to first order, that is $\delta\ln|\det g|=g^{\mu\nu}\delta g_{\mu\nu}$. Second, varying $g^{\mu\lambda}g_{\lambda\nu}=\delta^\mu{}_\nu$ gives $\delta g^{\mu\lambda}\,g_{\lambda\nu}+g^{\mu\lambda}\,\delta g_{\lambda\nu}=0$; setting $\nu=\mu$ and summing gives $g^{\mu\nu}\delta g_{\mu\nu}=-g_{\mu\nu}\delta g^{\mu\nu}$. Together,

$$
\delta\sqrt{|g|}=\tfrac12\sqrt{|g|}\,g^{\mu\nu}\delta g_{\mu\nu}=-\tfrac12\sqrt{|g|}\,g_{\mu\nu}\,\delta g^{\mu\nu}.
$$

**The scalar energy–momentum tensor.** Now vary $S$. The explicit $g^{\mu\nu}$ in $\mathcal L_\phi$ and the factor $\sqrt{|g|}$ both change, and to first order

$$
\delta S=\int\Bigl(-\tfrac12\sqrt{|g|}\,\partial_\mu\phi\,\partial_\nu\phi-\tfrac12\sqrt{|g|}\,g_{\mu\nu}\,\mathcal L_\phi\Bigr)\delta g^{\mu\nu}\,d^8x .
$$

Multiplying the bracket by $-2/\sqrt{|g|}$,

$$
T_{\mu\nu}=\partial_\mu\phi\,\partial_\nu\phi+g_{\mu\nu}\,\mathcal L_\phi ,
$$

which in flat space is the tensor above: the Noether route and the metric route agree for a scalar field. For a spinor field the canonical tensor $\Theta$ is not symmetric, and the metric route has to be carried out through the vielbein of Chapter 4; the result for dirac16complex is derived in Chapter 7.

**A derivative of $\sqrt{|g|}$ that we need in Section 5.13.** Jacobi's formula with $\delta$ replaced by $\partial_\lambda$ gives $\partial_\lambda\ln|\det g|=g^{\rho\sigma}\partial_\lambda g_{\rho\sigma}$. The Christoffel symbols of Chapter 4, $\Gamma^\rho{}_{\mu\nu}=\tfrac12g^{\rho\sigma}(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\mu\sigma}-\partial_\sigma g_{\mu\nu})$, contracted over $\rho=\mu$, give $\Gamma^\rho{}_{\rho\lambda}=\tfrac12g^{\rho\sigma}(\partial_\rho g_{\lambda\sigma}+\partial_\lambda g_{\rho\sigma}-\partial_\sigma g_{\rho\lambda})$. The first and the third term cancel (rename $\rho\leftrightarrow\sigma$ in the third and use the symmetry of $g$). Therefore

$$
\Gamma^\rho{}_{\rho\lambda}=\tfrac12g^{\rho\sigma}\partial_\lambda g_{\rho\sigma}=\partial_\lambda\ln\sqrt{|g|},\qquad\text{i.e.}\qquad \partial_\lambda\sqrt{|g|}=\sqrt{|g|}\,\Gamma^\rho{}_{\rho\lambda}.
$$

**Energy density, pressure and equation of state of a homogeneous field.** In flat space let $\phi$ depend only on $x_4$. Then $\rho=T_{44}=\dot\phi^2+\eta_{44}\mathcal L=\dot\phi^2-(\tfrac12\dot\phi^2-V)=\tfrac12\dot\phi^2+V$. For a direction $i\ne4$, $T_{ii}=\eta_{ii}\mathcal L$ and the **pressure** along $i$ is $p_{(i)}:=T^i{}_i=\eta^{ii}T_{ii}=\mathcal L=\tfrac12\dot\phi^2-V$ (no sum over $i$). The **equation-of-state parameter** is

$$
w=\frac p\rho=\frac{\tfrac12\dot\phi^2-V}{\tfrac12\dot\phi^2+V}.
$$

These are the formulas $\rho_\phi=\tfrac12\dot\phi^2+V$ and $P_\phi=\tfrac12\dot\phi^2-V$ of the task's scalar-field reference. With small numbers: $\dot\phi=2$ and $V=1$ give $\rho=3$, $p=1$, $w=1/3$; $\dot\phi=0$ gives $w=-1$, the behaviour of a cosmological constant; $V=0$ gives $w=+1$. Chapter 7 derives the corresponding formulas for dirac16complex, and Chapter 11 uses them in the dark-sector experiments.

### 5.9 Grassmann numbers from zero

**Why a new kind of number.** Electrons, quarks and, by construction, the quanta of the dirac16complex field are **fermions**: two of them can never occupy the same state (the Pauli principle). In quantum theory this is expressed by operators that **anticommute**, $ab=-ba$ (Chapter 8). The classical field whose quantization produces such operators must itself take values that anticommute. Ordinary numbers cannot do that, so one introduces new symbols with exactly this property. They are called **Grassmann numbers** after Hermann Grassmann. They are not results of measurements; they are bookkeeping symbols with precise algebraic rules, and every statement about them in this book is a statement about those rules.

**Definition.** Choose $n$ symbols $\theta_0,\theta_1,\dots,\theta_{n-1}$, the **generators**. The **Grassmann algebra** $\Lambda_n$ consists of all finite sums of complex numbers times products of generators, added and multiplied with the usual distributive rules, with ordinary numbers commuting with everything, and with the single new rule

$$
\theta_i\theta_j=-\theta_j\theta_i\qquad\text{for all }i,j .
$$

Taking $i=j$ gives $\theta_i\theta_i=-\theta_i\theta_i$, hence $\theta_i^2=0$: a generator squares to zero.

**A basis.** Any product of generators can be reordered into increasing index order; each exchange of two neighbours gives a factor $-1$, so the reordering gives the sign of the permutation (the number $(-1)^s$, $s$ the number of neighbour exchanges needed). A product in which a generator occurs twice is zero. So every element is a unique combination of the $2^n$ **monomials**

$$
1,\qquad \theta_{i_1}\theta_{i_2}\cdots\theta_{i_k}\quad(i_1<i_2<\dots<i_k),
$$

and $\Lambda_n$ is a vector space of dimension $2^n$. This is exactly how the repository stores an element on a computer: `scripts/grassmann_algebra.py` keeps a dictionary from sorted tuples of generator indices to exact coefficients, and every product sorts the merged tuple and records the sign of the sorting permutation (its function `_merge`).

**Worked example ($n=2$).** Every element is $F=a+b\theta_0+c\theta_1+d\theta_0\theta_1$ with complex $a,b,c,d$. For a second element $F'=a'+b'\theta_0+c'\theta_1+d'\theta_0\theta_1$,

$$
FF'=aa'+(ab'+ba')\theta_0+(ac'+ca')\theta_1+(ad'+da'+bc'-cb')\theta_0\theta_1 .
$$

The term $bc'-cb'$ comes from $b\theta_0\,c'\theta_1=bc'\,\theta_0\theta_1$ and $c\theta_1\,b'\theta_0=cb'\,\theta_1\theta_0=-cb'\,\theta_0\theta_1$; all products with a repeated generator vanish. In particular $(b\theta_0+c\theta_1)^2=bc\,\theta_0\theta_1+cb\,\theta_1\theta_0=0$.

**Even and odd.** A monomial of $k$ generators has **degree** $k$; it is **even** if $k$ is even and **odd** if $k$ is odd, and an element is even (odd) if all its monomials are. Moving a monomial of degree $k$ past one of degree $l$ takes $kl$ exchanges, so

$$
XY=(-1)^{kl}\,YX\qquad\text{for monomials of degrees }k,l .
$$

Hence an even element commutes with every element, and two odd elements anticommute. An odd element $X$ satisfies $X^2=-X^2$, so $X^2=0$.

**Worked example: powers of a sum of commuting pairs.** Let $P_0,\dots,P_{15}$ be 16 products of two generators each, with no generator shared between two of them, for example $P_a=\theta_{2a}\theta_{2a+1}$ with 32 generators. Each $P_a$ is even, so they all commute with each other, and $P_a^2=0$. For $S=P_0+P_1+\dots+P_{15}$ the multinomial expansion therefore keeps only products of **distinct** $P$'s, each appearing $k!$ times in $S^k$ (once for every order):

$$
S^k=k!\sum_{a_1<a_2<\dots<a_k}P_{a_1}P_{a_2}\cdots P_{a_k}.
$$

So $S^k$ has $\binom{16}{k}$ monomials with coefficients $\pm k!$, $S^{16}=16!\,P_0P_1\cdots P_{15}$ is a single monomial, and $S^{17}=0$. With two pairs only: $S=P_0+P_1$, $S^2=P_0P_1+P_1P_0=2P_0P_1$ and $S^3=0$. This is exactly the structure of the scalar density $S=\bar\Psi\Psi$ of dirac16complex at one point (Chapter 6): there the pairs are $\Psi_a^\ast\Psi_b$, and the repository computed all powers in an explicit Grassmann algebra with 32 generators, finding 16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440, 8008, 4368, 1820, 560, 120, 16 and 1 monomials for $k=1,\dots,16$, coefficients of absolute value $k!$, and $S^{17}=0$ (check `GR_quarticTermPolynomial` in `artifacts/dirac16complex/arbitrary-field/grassmann-demo-report.json`; Stage-1 document, Result 7.2). A consequence: a function of $S$ can only be a polynomial of degree at most 16, which is why the self-interaction of dirac16complex is the polynomial $U(S)=\tfrac\lambda2S^2$ (Chapter 6).

**Complex conjugation.** A **conjugation** on the algebra is a rule $F\mapsto F^\ast$ with $(F+G)^\ast=F^\ast+G^\ast$, $(cF)^\ast=c^\ast F^\ast$ for numbers $c$, $(F^\ast)^\ast=F$, and the **order-reversing** product rule

$$
(FG)^\ast=G^\ast F^\ast .
$$

A generator with $\theta^\ast=\theta$ is called **real**. A **complex** Grassmann variable is described by two generators $\theta$ and $\theta^\ast$ that are exchanged by the conjugation. Two consequences are worth seeing once. The product of two real generators is imaginary: $(\theta_0\theta_1)^\ast=\theta_1^\ast\theta_0^\ast=\theta_1\theta_0=-\theta_0\theta_1$, so $i\theta_0\theta_1$ is real. The product $\theta^\ast\theta$ of a complex generator with its conjugate is real: $(\theta^\ast\theta)^\ast=\theta^\ast\theta^{\ast\ast}=\theta^\ast\theta$. More generally, for a column $\Psi=(\Psi_0,\dots,\Psi_{n-1})^T$ of complex odd generators, $\Psi^\dagger=(\Psi^\ast)^T$ and a numerical matrix $M$,

$$
\bigl(\Psi^\dagger M\Psi\bigr)^\ast=\sum_{a,b}M_{ab}^\ast\,\Psi_b^\ast\Psi_a=\Psi^\dagger M^\dagger\Psi,
$$

so a **bilinear** $\Psi^\dagger M\Psi$ is real (the book says Hermitian) exactly when the matrix $M$ is Hermitian, $M^\dagger=M$, just as for ordinary numbers. These rules, including the order reversal, were checked in an explicit Grassmann algebra (check `GR_conjugationRules`, `grassmann-demo-report.json`).

### 5.10 Calculus with Grassmann numbers

**Grassmann-valued fields.** A Grassmann field assigns to every point $x$ odd elements $\Psi_a(x)$; its derivatives $\partial_\mu\Psi_a(x)$ are odd as well. At one point, the values $\Psi_a$, the first derivatives $\partial_\mu\Psi_a$ and the second derivatives $\partial_\mu\partial_\nu\Psi_a$ ($\mu\le\nu$) can be treated as independent generators, called **jets**. For 16 real components this is $16\times(1+8+36)=720$ generators, and for a complex field with $\Psi$ and $\Psi^\ast$ it is 1440; these are the generator counts of the repository's Grassmann computations (measurement `GR_generatorCounts` in `grassmann-demo-report.json`; the class `JetSpace` in `scripts/grassmann_algebra.py`). The total derivative $\partial_\mu$ acts on jets by raising the derivative order, $\partial_\mu(\partial_\nu\Psi_a)=\partial_\mu\partial_\nu\Psi_a$, and on products by the ordinary product rule, with no extra signs, because $\partial_\mu$ itself is even (it does not change the degree).

**Left and right derivatives.** Let $F$ be an element and $\theta_k$ a generator. The **left derivative** $\partial_LF/\partial\theta_k$ is computed monomial by monomial: move $\theta_k$ to the far left, collecting a factor $-1$ for every generator it passes, and then delete it; monomials without $\theta_k$ give zero. The **right derivative** $\partial_RF/\partial\theta_k$ moves $\theta_k$ to the far right instead. Examples: for $F=\theta_0\theta_1$, $\partial_LF/\partial\theta_0=\theta_1$, $\partial_LF/\partial\theta_1=-\theta_0$ (write $F=-\theta_1\theta_0$), $\partial_RF/\partial\theta_1=\theta_0$ and $\partial_RF/\partial\theta_0=-\theta_1$.

**Proposition 5.3.** For an even element $F$, $\partial_RF/\partial\theta_k=-\partial_LF/\partial\theta_k$.

*Proof.* In a monomial of even degree $n$ let $\theta_k$ stand at position $p$ (counting from 0). Moving it to the left passes $p$ generators, moving it to the right passes $n-1-p$. The two signs differ by $(-1)^{n-1-2p}=(-1)^{n-1}=-1$. $\square$

**The first-order change.** For an odd “small” change $\delta\theta_k$ of one generator,

$$
F(\theta_k+\delta\theta_k)=F(\theta_k)+\delta\theta_k\,\frac{\partial_LF}{\partial\theta_k}\qquad\text{exactly, when }(\delta\theta_k)^2=0 .
$$

*Proof.* Write $F=G+\theta_kH$ with $G$, $H$ free of $\theta_k$ (move $\theta_k$ to the left in every monomial that contains it). Then $H=\partial_LF/\partial\theta_k$ and $F(\theta_k+\delta\theta_k)=G+\theta_kH+\delta\theta_kH$. $\square$ This is why the left derivative is the natural one when the variation is written on the left.

**Euler–Lagrange equations for Grassmann fields.** Let $\mathcal L$ be an even element built from odd fields $\Psi_a$ and their derivatives (a Lagrangian must be even: every term contains the odd fields in pairs, so that it commutes with everything like an ordinary function). Vary $\Psi_a\to\Psi_a+\varepsilon\,\xi(x)$ for one component $a$, where $\varepsilon$ is a new odd generator (so $\varepsilon^2=0$) and $\xi$ an ordinary bump function. By the first-order formula, and because $\xi$ is an ordinary function,

$$
\delta\mathcal L=\varepsilon\,\xi\,\frac{\partial_L\mathcal L}{\partial\Psi_a}+\varepsilon\,(\partial_\mu\xi)\,\frac{\partial_L\mathcal L}{\partial(\partial_\mu\Psi_a)} .
$$

Integrating by parts exactly as in Section 5.3 gives $\delta S=\varepsilon\int\xi\,E_a\,d^8x$ with

$$
E_a=\frac{\partial_L\mathcal L}{\partial\Psi_a}-\partial_\mu\frac{\partial_L\mathcal L}{\partial(\partial_\mu\Psi_a)} .
$$

Since $\varepsilon$ does not occur in $E_a$, $\varepsilon\int\xi E_a\,d^8x=0$ for all $\xi$ forces $E_a=0$: these are the field equations. With right derivatives, and the variation written on the right, one obtains the expression $E^R_a$; by Proposition 5.3, applied to the even $\mathcal L$, $E^R_a=-E_a$, so the two conventions give the same equations with opposite overall signs. (The Stage-1 document uses left derivatives for $\Psi^\dagger$ and right derivatives for $\Psi$; its §8.1 records the sign.) For a complex Grassmann field one varies $\Psi_a$ and $\Psi_a^\ast$ independently, by the same linear-substitution argument as in Section 5.6.

**Worked example (a complex Grassmann oscillator).** Let $\theta(t)$ be a complex odd variable and

$$
L=\tfrac i2\bigl(\theta^\ast\dot\theta-\dot\theta^\ast\theta\bigr)-\omega\,\theta^\ast\theta .
$$

This $L$ is real by the conjugation rules of Section 5.9. Varying $\theta^\ast$ (left derivative): $\partial_LL/\partial\theta^\ast=\tfrac i2\dot\theta-\omega\theta$, because $\theta^\ast$ already stands on the left; and $\partial_LL/\partial\dot\theta^\ast=-\tfrac i2\theta$. So $E=\tfrac i2\dot\theta-\omega\theta+\tfrac i2\dot\theta=i\dot\theta-\omega\theta$, and the field equation $i\dot\theta=\omega\theta$ has the same form as for the ordinary complex oscillator of Section 5.6. For **complex** Grassmann fields written with every conjugate factor to the left, the anticommutation does not change the form of the equations. For **real** Grassmann fields it changes everything, as the next section shows.

### 5.11 Bilinear forms in Grassmann variables: two lemmas

Let $\Psi=(\Psi_0,\dots,\Psi_{n-1})^T$ be a column of **real** odd fields and $M$ an $n\times n$ matrix of ordinary numbers (or of ordinary functions of $x$). Write $\Psi^TM\Psi=\sum_{a,b}\Psi_aM_{ab}\Psi_b$, and split $M$ into its symmetric and antisymmetric parts, $M_S=\tfrac12(M+M^T)$ and $M_A=\tfrac12(M-M^T)$.

**Lemma 5.4.** $\Psi^TM\Psi=\Psi^TM_A\Psi$. In particular $\Psi^TM\Psi=0$ for every symmetric $M$.

*Proof.* Exchange the two odd factors and rename the summation indices: $\Psi^TM\Psi=\sum_{a,b}\Psi_aM_{ab}\Psi_b=-\sum_{a,b}\Psi_bM_{ab}\Psi_a=-\sum_{a,b}\Psi_a(M^T)_{ab}\Psi_b=-\Psi^TM^T\Psi$. Hence $\Psi^TM_S\Psi=\tfrac12(\Psi^TM\Psi+\Psi^TM^T\Psi)=0$. $\square$

*Worked example.* For $n=2$ and $M=\begin{pmatrix}1&2\\3&4\end{pmatrix}$: $\Psi^TM\Psi=\Psi_0\Psi_0+2\Psi_0\Psi_1+3\Psi_1\Psi_0+4\Psi_1\Psi_1=(2-3)\Psi_0\Psi_1=-\Psi_0\Psi_1$. The antisymmetric part is $M_A=\begin{pmatrix}0&-1/2\\1/2&0\end{pmatrix}$, and $\Psi^TM_A\Psi=-\tfrac12\Psi_0\Psi_1+\tfrac12\Psi_1\Psi_0=-\Psi_0\Psi_1$, the same. For commuting variables the opposite holds: $q^TMq=q^TM_Sq$, since $q^TM_Aq=0$.

**Lemma 5.5.** If $A(x)$ is an antisymmetric matrix function, $A^T=-A$, then

$$
\Psi^TA\,\partial_\mu\Psi=\tfrac12\,\partial_\mu\bigl(\Psi^TA\Psi\bigr)-\tfrac12\,\Psi^T(\partial_\mu A)\Psi .
$$

*Proof.* The product rule gives $\partial_\mu(\Psi^TA\Psi)=(\partial_\mu\Psi)^TA\Psi+\Psi^T(\partial_\mu A)\Psi+\Psi^TA\,\partial_\mu\Psi$. In the first term exchange the two odd factors: $(\partial_\mu\Psi)^TA\Psi=\sum_{a,b}\partial_\mu\Psi_aA_{ab}\Psi_b=-\sum_{a,b}\Psi_bA_{ab}\partial_\mu\Psi_a=-\Psi^TA^T\partial_\mu\Psi=\Psi^TA\,\partial_\mu\Psi$. So $\partial_\mu(\Psi^TA\Psi)=2\Psi^TA\,\partial_\mu\Psi+\Psi^T(\partial_\mu A)\Psi$, which is the claim. $\square$

So for real Grassmann fields a first-order kinetic term with an antisymmetric matrix is **half a total derivative plus a term without derivatives**. For a constant $A$ it is a total derivative and has no field equations at all (Proposition 5.1; the proof by the action works unchanged for Grassmann fields, with $\varepsilon\xi$ as the variation).

*Worked example.* One coordinate $x$, two real odd fields $\theta_0(x)$, $\theta_1(x)$, a prime for $d/dx$, and $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. Then

$$
\theta^TA\theta'=\theta_0\theta_1'-\theta_1\theta_0'=\theta_0\theta_1'+\theta_0'\theta_1=(\theta_0\theta_1)'=\tfrac12\bigl(\theta^TA\theta\bigr)',
$$

because $\theta^TA\theta=\theta_0\theta_1-\theta_1\theta_0=2\theta_0\theta_1$. Directly: for $\theta_0$, $\partial_L/\partial\theta_0$ of $\theta_0\theta_1'-\theta_1\theta_0'$ is $\theta_1'$, and $\partial_L/\partial\theta_0'$ is $+\theta_1$ (write $-\theta_1\theta_0'=\theta_0'\theta_1$), so $E_0=\theta_1'-(\theta_1)'=0$; similarly $E_1=-\theta_0'-(-\theta_0)'=0$. Compare Example A of Section 5.6: the same expression with commuting $q_0,q_1$ gave the non-trivial expressions $\dot q_1$ and $-\dot q_0$. Now take instead the symmetric identity matrix $I_2$: $\theta^TI_2\theta=\theta_0\theta_0+\theta_1\theta_1=0$, but $\theta^TI_2\theta'=\theta_0\theta_0'+\theta_1\theta_1'$ is not a derivative, and its Euler–Lagrange expression for $\theta_0$ is $\theta_0'-(-\theta_0)'=2\theta_0'\ne0$. The repository found the same contrast for the $16\times16$ matrix $C$ of Chapter 2: with $C$ in place of an antisymmetric matrix the Euler–Lagrange expression is $2(C\partial_0\Psi)_0$ (check `GR_kineticSymmetricMatrixContrast`).

The two lemmas side by side:

| property | commuting real fields | real Grassmann fields |
| --- | --- | --- |
| part of $M$ that survives in $\Psi^TM\Psi$ | symmetric $M_S$ | antisymmetric $M_A$ |
| mass-type term $\Psi^TC\Psi$ with symmetric $C$ | survives | vanishes identically |
| kinetic term $\Psi^TA\,\partial\Psi$ with antisymmetric $A$ | genuine first-order dynamics | total derivative plus a derivative-free term |

### 5.12 The author's Lagrangian Lg[] and the matrices it uses

**The matrices.** Chapter 2 constructs the eight real $16\times16$ integer matrices $\gamma^0,\dots,\gamma^7$ of the notebook (its T16^A) and proves their properties. We need the following definitions and facts, all facts verified exactly by the repository (Stage-1 document, Results 3.1, 3.3 and 3.5; checks `ALG_clifford`, `ALG_gammaTransposeSymmetry`, `ALG_chargeMatrix`, `ALG_expression1` and `ALG_spinTransposeProperties` in `wolfram-algebra-report.json` and `python-algebra-report.json`):

- the Clifford relation $\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}I_{16}$, so different gammas anticommute, $(\gamma^a)^2=+1$ for $a\le3$ and $(\gamma^a)^2=-1$ for $a\ge4$;
- $\gamma^a$ is symmetric for $a\le3$ and antisymmetric for $a\ge4$;
- the charge matrix $C:=\gamma^0\gamma^1\gamma^2\gamma^3$ (the notebook's σ16) is symmetric and $C^2=I_{16}$;
- the spin matrices $S^{ab}=\tfrac14(\gamma^a\gamma^b-\gamma^b\gamma^a)$ generate the rotations of spinors (Chapter 2);
- expression [1] of the task: $(C\gamma^a)^T=-C\gamma^a$ for every $a$.

The properties of $C$ and expression [1] follow from the first two facts, and we prove them because the whole theorem rests on them. *$C$ is symmetric:* $C^T=(\gamma^3)^T(\gamma^2)^T(\gamma^1)^T(\gamma^0)^T=\gamma^3\gamma^2\gamma^1\gamma^0$, and reversing four mutually anticommuting factors takes $3+2+1=6$ exchanges, so $C^T=(+1)C$. *$C^2=1$:* $C\cdot C=C\cdot C^T=\gamma^0\gamma^1\gamma^2\gamma^3\gamma^3\gamma^2\gamma^1\gamma^0=1$, collapsing the squares $(\gamma^a)^2=1$ from the middle. *Expression [1]:* for $a\le3$, $(C\gamma^a)^T=(\gamma^a)^TC^T=\gamma^aC$, and $\gamma^a$ anticommutes with the three factors of $C$ other than itself and commutes with itself, so $\gamma^aC=(-1)^3C\gamma^a=-C\gamma^a$. For $a\ge4$, $(C\gamma^a)^T=-\gamma^aC$, and $\gamma^a$ anticommutes with all four factors, so $\gamma^aC=C\gamma^a$ and again $(C\gamma^a)^T=-C\gamma^a$. $\square$

**Two consequences.** Multiplying $(\gamma^a)^TC=-C\gamma^a$ on the right by $C$ gives $(\gamma^a)^T=-C\gamma^aC$. Then $(S^{ab})^T=\tfrac14[(\gamma^b)^T,(\gamma^a)^T]=\tfrac14C[\gamma^b,\gamma^a]C=-CS^{ab}C$, hence

$$
(CS^{ab})^T=(S^{ab})^TC=-CS^{ab},\qquad (C\gamma^cS^{ab})^T=(S^{ab})^T(\gamma^c)^TC=(-CS^{ab}C)(-C\gamma^cC)C=CS^{ab}\gamma^c .
$$

So the matrix $C\gamma^cS^{ab}$ splits into a symmetric part $\tfrac12C\{\gamma^c,S^{ab}\}$ and an antisymmetric part $\tfrac12C[\gamma^c,S^{ab}]$, where $\{X,Y\}=XY+YX$ is the **anticommutator** and $[X,Y]=XY-YX$ the **commutator**. This is Lemma 6.3 of the Stage-1 document (checks `ALG_CAnticommutatorGammaSSymmetric` and `ALG_CCommutatorGammaSAntisymmetric`, `python-geometry-report.json`).

**Worked example with the actual matrices.** The Student Guide (`provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md`, its §6.3 and §6.4) lists every gamma and $C$ as signed permutations: row 0 of $C$ reads “$-4$”, meaning $(Cu)_0=-u_4$, and row 4 reads “$-0$”, meaning $(Cu)_4=-u_0$. So $C_{0,4}=C_{4,0}=-1$, and in $\Psi^TC\Psi$ these two entries give $-\Psi_0\Psi_4-\Psi_4\Psi_0=0$; all 16 entries of $C$ cancel in pairs in the same way, and $\Psi^TC\Psi=0$. For $C\gamma^0$: row 4 of $\gamma^0$ reads “$+12$”, so $(C\gamma^0u)_0=-(\gamma^0u)_4=-u_{12}$, while row 12 of $C$ reads “$+8$” and row 8 of $\gamma^0$ reads “$+0$”, so $(C\gamma^0u)_{12}=+(\gamma^0u)_8=+u_0$. The entries $-1$ at $(0,12)$ and $+1$ at $(12,0)$ give $-\Psi_0\Psi_{12}+\Psi_{12}\Psi_0=-2\Psi_0\Psi_{12}$. Doing this for all rows,

$$
\Psi^TC\gamma^0\Psi=-2\bigl(\Psi_0\Psi_{12}+\Psi_1\Psi_{13}+\Psi_2\Psi_{14}+\Psi_3\Psi_{15}+\Psi_4\Psi_8+\Psi_5\Psi_9+\Psi_6\Psi_{10}+\Psi_7\Psi_{11}\bigr).
$$

The repository's Grassmann algebra finds exactly this pattern: $\Psi^TC\Psi$ has 0 monomials, and each of the eight $\Psi^TC\gamma^a\Psi$ has 8 monomials with coefficients $\pm2$ (the two measurements of `grassmann-demo-report.json` whose names begin with `GR_massTermVanishesReal_`).

**Geometry.** From Chapter 4 we need: the vielbein $e_\mu{}^a(x)$ and its inverse $e_a{}^\mu$, the metric $g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b$, the curved gammas $\gamma^\mu=e_a{}^\mu\gamma^a$ (ordinary functions times constant matrices), the canonical spin connection $\omega_{\mu ab}=-\omega_{\mu ba}$ fixed by the vielbein postulate, the spinor connection $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$, and the covariant constancy of the gammas,

$$
D_\mu\gamma^\nu:=\partial_\mu\gamma^\nu+\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda+[\Omega_\mu,\gamma^\nu]=0,
$$

which is equivalent to the vielbein postulate (Stage-1 document, Result 5.2; checks `GEO_gammaCovariantConstancy_G1` and `_G2`).

**The divergence identity.** Set $\nu=\mu$ in $D_\mu\gamma^\nu=0$ and sum: $\partial_\mu\gamma^\mu+\Gamma^\mu{}_{\mu\lambda}\gamma^\lambda+[\Omega_\mu,\gamma^\mu]=0$. Multiply by $\sqrt{|g|}$ and use $\partial_\lambda\sqrt{|g|}=\sqrt{|g|}\,\Gamma^\mu{}_{\mu\lambda}$ from Section 5.8: the first two terms become $\partial_\mu(\sqrt{|g|}\gamma^\mu)$. Hence

$$
\partial_\mu\bigl(\sqrt{|g|}\,\gamma^\mu\bigr)=\sqrt{|g|}\,[\gamma^\mu,\Omega_\mu] .
$$

This is Result 5.3 of the Stage-1 document (checks `GEO_divergenceIdentity_G1` and `GEO_divergenceIdentity_G2` in both geometry reports).

**The notebook's Lagrangian.** Cell 1064 of the notebook defines $\mathrm{Lg}[\,]$. Verbatim, as transcribed in the Stage-1 document (§6.1; the line breaks are only for the page width):

```
Lg[]:=Sqrt[detgg] *( Transpose[\[CapitalPsi]16].\[Sigma]16.
Sum[FullSimplify[((T16^\[Alpha])[\[Alpha]1-1]/.sg),constraintVars].
(D[ \[CapitalPsi]16,X[[\[Alpha]1]]]+(Q1/2)*Sum[\[Omega]mat[[\[Alpha]1,a,b]]*SAB[[a,
b]].\[CapitalPsi]16,{a,1,8},{b,1,8}]),{\[Alpha]1,1,Length[X]}]+
(H*M)*Transpose[\[CapitalPsi]16].\[Sigma]16.\[CapitalPsi]16)//Simplify[#,
constraintVars]&
```

In the notation of this book, with the switch Q1 = 1 and the mass $m:=-HM$ (so that $+HM\,\Psi^TC\Psi=-m\,\Psi^TC\Psi$),

$$
\mathrm{Lg}=\sqrt{|g|}\,\Bigl[\Psi^TC\gamma^\mu\bigl(\partial_\mu\Psi+\Omega^{\mathrm{nb}}_\mu\Psi\bigr)-m\,\Psi^TC\Psi\Bigr],\qquad \Omega^{\mathrm{nb}}_\mu=\tfrac12\,\omega_\mu{}^a{}_b\,S^{ab}.
$$

Here $\Psi$ is the notebook's Ψ16, a **real** column of 16 components f16[k]. The notebook contracts the mixed connection $\omega_\mu{}^a{}_b$ with $S^{ab}$; one factor of $\eta$ is missing, and Chapter 4 shows that this $\Omega^{\mathrm{nb}}$ is not the correct spinor connection. The notebook treats the f16[k] as ordinary commuting functions; a search of the notebook finds no Grassmann or anticommuting variable anywhere (`handoff/surveys/survey_notebook-physics.md`, its item 6). A fermion field, however, must have anticommuting components. We therefore ask what $\mathrm{Lg}[\,]$ gives for a real Grassmann field, first with the correct connection $\Omega_\mu$ in place of $\Omega^{\mathrm{nb}}_\mu$, then with the notebook's own.

### 5.13 Theorem: Lg[] is a pure divergence for a real Grassmann field

**Theorem 5.6.** Let $\Psi$ be a real 16-component Grassmann-odd field in an arbitrary gravitational field, and let the connection in $\mathrm{Lg}$ be the canonical $\Omega_\mu$. Then

$$
\mathrm{Lg}=\partial_\mu V^\mu,\qquad V^\mu=\tfrac12\sqrt{|g|}\,\Psi^TC\gamma^\mu\Psi,
$$

and all 16 Euler–Lagrange expressions of $\mathrm{Lg}$ vanish identically. The field equations of $\mathrm{Lg}[\,]$ are $0=0$.

*Proof.* We treat the three terms of $\mathrm{Lg}$ one by one.

*Step 1 (mass term).* $C$ is symmetric, so $\Psi^TC\Psi=0$ by Lemma 5.4. The mass term vanishes identically, whatever $m$ is.

*Step 2 (derivative term).* Put $A^\mu:=\sqrt{|g|}\,C\gamma^\mu=\sqrt{|g|}\,e_a{}^\mu\,C\gamma^a$. It is a sum of the antisymmetric matrices $C\gamma^a$ (expression [1]) with ordinary functions as coefficients, hence antisymmetric. Lemma 5.5 gives

$$
\sqrt{|g|}\,\Psi^TC\gamma^\mu\partial_\mu\Psi=\tfrac12\,\partial_\mu\bigl(\Psi^TA^\mu\Psi\bigr)-\tfrac12\,\Psi^TC\,\partial_\mu\bigl(\sqrt{|g|}\gamma^\mu\bigr)\Psi .
$$

*Step 3 (connection term).* $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$ and $\gamma^\mu=e_c{}^\mu\gamma^c$, so $C\gamma^\mu\Omega_\mu$ is a combination, with ordinary-function coefficients, of the matrices $C\gamma^cS^{ab}$. By Section 5.12 its symmetric part is $\tfrac12C\{\gamma^\mu,\Omega_\mu\}$ and its antisymmetric part is $\tfrac12C[\gamma^\mu,\Omega_\mu]$. By Lemma 5.4 only the antisymmetric part survives:

$$
\sqrt{|g|}\,\Psi^TC\gamma^\mu\Omega_\mu\Psi=\tfrac12\sqrt{|g|}\,\Psi^TC[\gamma^\mu,\Omega_\mu]\Psi=\tfrac12\,\Psi^TC\,\partial_\mu\bigl(\sqrt{|g|}\gamma^\mu\bigr)\Psi,
$$

where the last step is the divergence identity of Section 5.12.

*Step 4 (cancellation).* The result of Step 3 is exactly minus the second term of Step 2. Adding Steps 1 to 3,

$$
\mathrm{Lg}=\tfrac12\,\partial_\mu\bigl(\Psi^TA^\mu\Psi\bigr)=\partial_\mu V^\mu .
$$

*Step 5 (no field equations).* $V^\mu$ depends on the field $\Psi$ and on $x$ (through $\sqrt{|g|}$ and $e_a{}^\mu$) but not on derivatives of $\Psi$. By Proposition 5.1, in its Grassmann form (Section 5.11), every Euler–Lagrange expression of $\partial_\mu V^\mu$ vanishes identically. $\square$

The proof uses only the algebra of Section 5.12, the two lemmas, and the divergence identity, which holds in **every** gravitational field with the canonical connection. So the theorem holds in every gravitational field, not only at the points where the repository tested it (Section 5.15).

**What the theorem means.** $\mathrm{Lg}[\,]$ is the Lagrangian of nothing, for the kind of field that a fermion is. Its mass term is zero, its derivative term is a total derivative, and its spin-connection term exactly cancels the only part of the derivative term that is not a total derivative. This is Theorem 6.1 of the Stage-1 document, the first of the three findings about the notebook that the README lists.

### 5.14 The notebook's own contraction, commuting fields, and the way out

**With the notebook's contraction.** Repeat the proof with $\Omega^{\mathrm{nb}}_\mu$ in place of $\Omega_\mu$. Steps 1 and 2 do not involve the connection. $\Omega^{\mathrm{nb}}_\mu$ is also a combination of the $S^{ab}$, so Step 3 still gives $\tfrac12\sqrt{|g|}\,\Psi^TC[\gamma^\mu,\Omega^{\mathrm{nb}}_\mu]\Psi$; but the divergence identity holds for $\Omega_\mu$, not for $\Omega^{\mathrm{nb}}_\mu$, so the cancellation of Step 4 is incomplete. What remains is

$$
\mathrm{Lg}=\partial_\mu V^\mu+\tfrac12\,\Psi^TX\Psi,\qquad X=\sqrt{|g|}\;C\sum_{\mu}\bigl[\gamma^\mu,\Omega^{\mathrm{nb}}_\mu-\Omega_\mu\bigr],
$$

with an antisymmetric matrix $X$ (a sum of matrices $C[\gamma^c,S^{ab}]$). The left derivative of $\tfrac12\sum_{a,b}X_{ab}\Psi_a\Psi_b$ with respect to $\Psi_c$ is $\tfrac12\sum_bX_{cb}\Psi_b-\tfrac12\sum_aX_{ac}\Psi_a=(X\Psi)_c$, because $X^T=-X$; no derivative of $\Psi$ appears. So the Euler–Lagrange equations are the **algebraic** equations

$$
X\Psi=0 .
$$

At every point where the $16\times16$ matrix $X$ is invertible (rank 16) they force $\Psi=0$. The repository computed $X$ exactly at six points, three points of a generic non-diagonal test vielbein called G1 and three points of the notebook's primordial field called G2 (Chapter 9): $X$ has rank 16 at all six, with largest entries of absolute value about 9.927, 12.36 and 10.72 at the G1 points and $3\sqrt{455}/32\approx1.99976$, about 0.5977 and about 2.530 at the G2 points (measurements `G1.p1.notebookLgResidualXRank`, `G1.p1.notebookLgResidualXMaxAbsDecimal` and their analogues for the other five points in `artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json`). Either way, $\mathrm{Lg}[\,]$ gives no wave equation for a Grassmann field. That the rank is 16 is a computed fact at these six points, not a theorem for every field.

**With commuting fields (the notebook's actual use).** For ordinary commuting components the roles of the symmetric and antisymmetric parts are exchanged (Lemma 5.4 and the remark after it). Then the mass term $\Psi^TC\Psi$ survives, the derivative term $\Psi^TC\gamma^\mu\partial_\mu\Psi$ is a genuine first-order kinetic term (as in Example A of Section 5.6), and from the connection term only the symmetric part $\tfrac12C\{\gamma^\mu,\Omega_\mu\}$ survives. That part is small in a precise sense. For distinct $c,a,b$ one has $\gamma^cS^{ab}=\tfrac12\gamma^c\gamma^a\gamma^b=S^{ab}\gamma^c$ (moving $\gamma^c$ through two anticommuting factors), so $\{\gamma^c,S^{ab}\}=\gamma^c\gamma^a\gamma^b$; for $c=a\ne b$ one has $\gamma^aS^{ab}=\tfrac12\eta^{aa}\gamma^b=-S^{ab}\gamma^a$, so $\{\gamma^a,S^{ab}\}=0$. Hence $\{\gamma^\mu,\Omega_\mu\}$ contains only the components $\omega_{cab}$ with three different indices, and only their totally antisymmetric combination. For a diagonal vielbein, such as the notebook's field, these vanish (Stage-1 document, §6.5; check `GEO_anticommutatorGammaOmegaVanishesDiagonal_G2`). So for commuting fields in the notebook's diagonal field the spin connection drops out of $\mathrm{Lg}[\,]$ altogether, for either contraction, and the gravitational term of the field equations comes from $\partial_\mu(\sqrt{|g|}\gamma^\mu)$. The notebook's stored equations contain an additional term that Chapter 9 traces to a substitution rule in cell 1058. The commuting 16-component field, taken seriously as a classical field, is the second field of this book, dirac16complex00 (Chapter 6).

**The way out: a complex Grassmann field.** For a **complex** Grassmann field the Dirac adjoint $\bar\Psi:=\Psi^\dagger C$ pairs the conjugate components $\Psi_a^\ast$ with the components $\Psi_b$. These are independent generators, so Lemma 5.4 does not apply: $\bar\Psi\Psi=\sum_{a,b}\Psi_a^\ast C_{ab}\Psi_b$ has 16 nonzero monomials, one for each nonzero entry of $C$ (Stage-1 document, Results 7.1 and 7.2; checks `GR_scalarBilinearHermitian` and `GR_quarticTermPolynomial`), whereas the real $\Psi^TC\Psi$ has none. Chapter 6 builds the Lagrangian of dirac16complex from $\bar\Psi$:

$$
\mathcal L=\sqrt{|g|}\,\Bigl[\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)-m\,\bar\Psi\Psi-U(\bar\Psi\Psi)\Bigr],\qquad D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi .
$$

Its field equation $\gamma^\mu D_\mu\Psi=(m+U'(\bar\Psi\Psi))\Psi$ is derived in Chapter 7. In the repository's Grassmann algebra at the G1 point p1 the Euler–Lagrange expression of this $\mathcal L$ for component 0 contains 32 terms with derivatives of the field and 8 spin-connection terms, and $\gamma^\mu\Omega_\mu$ has 128 nonzero entries there (measurements `GR_complexLagrangianNonTrivial_EL0_derivativeJetTerms_G1_p1`, `_EL0_spinConnectionTerms_G1_p1` and `_gammaMuOmegaMu_nonzeroEntries_G1_p1`). Unlike $\mathrm{Lg}[\,]$, it is a genuine field theory.

### 5.15 How the repository checks all of this

Everything in Sections 5.12 to 5.14 was checked by two independent exact programs, in genuine Grassmann algebras (Stage-1 document, §6.4 and §11):

| statement | check (report) |
| --- | --- |
| $\Psi^TC\Psi=0$; $\Psi^TC\gamma^a\Psi$ has 8 monomials | `GR_massTermVanishesReal` (grassmann-demo) |
| only the antisymmetric part of a random integer matrix survives | `GR_bilinearOnlyAntisymmetricPartSurvives` (grassmann-demo) |
| Lemma 5.5 for each constant $C\gamma^a$ and a random antisymmetric matrix | `GR_kineticTotalDerivativeReal` (grassmann-demo) |
| the symmetric-matrix contrast | `GR_kineticSymmetricMatrixContrast` (grassmann-demo) |
| $\Psi^TC\Psi=0$, $\Psi^TC\gamma^0\Psi\ne0$, derivatives of $\tfrac\lambda2S^2$ | `ALG_grassmannLemmas` (wolfram-geometry) |
| the split of $C\gamma^cS^{ab}$ of Section 5.12 | `ALG_spinTransposeProperties` (both algebra reports) |
| Theorem 5.6 at G1 p1 and in the symbolic G2 | `GR_notebookLgELTrivial`, `GR_notebookLgPureDivergence` (grassmann-demo) |
| Theorem 5.6 and $X\Psi$ at all six G1 and G2 points | `LAG_notebookLgGrassmannTrivial_G1`, `_G2` (wolfram-geometry) |
| the divergence identity | `GEO_divergenceIdentity_G1`, `_G2` (wolfram-geometry, python-geometry) |

The Python demonstration works with 720 generators for the real field and 1440 for the complex one. With the canonical connection 0 of the 16 Euler–Lagrange components of $\mathrm{Lg}$ are nonzero, and $\mathrm{Lg}$ (544 monomials at G1 p1, 136 in G2) equals $\partial_\mu V^\mu$ exactly; with the notebook contraction all 16 components are nonzero, contain no derivative, and equal $X\Psi$ (measurements `GR_notebookLgEL_*` in `grassmann-demo-report.json`; the Wolfram report counts the same 544 and 136 monomials). All 16 checks of `grassmann-demo-report.json` are true. To rerun the Python demonstration from the repository root (it rewrites that report, so run it in a scratch clone if you want to keep the committed file untouched), in PowerShell

```
$env:PYTHONUTF8 = "1"
python scripts/demo_grassmann_lagrangians.py
```

and in Git Bash, macOS or Linux

```
export PYTHONUTF8=1
python scripts/demo_grassmann_lagrangians.py
```

The last two lines it prints are `check_count=16` and `failed_check_count=0`. The whole Stage-1 gate, which runs this step and all others, is described in Chapter 19.

### 5.16 What we proved and what we assumed

**What we proved.** With complete arguments in this chapter: the Euler–Lagrange equations of a particle and of a field follow from the principle of stationary action (Sections 5.2 and 5.3); a Lagrangian that is a total divergence has identically vanishing Euler–Lagrange expressions (Proposition 5.1), for ordinary and for Grassmann fields; Noether's theorem (Theorem 5.2) and the canonical energy–momentum tensor; the metric energy–momentum tensor of a scalar field and its agreement with the Noether one; $\rho=\tfrac12\dot\phi^2+V$, $p=\tfrac12\dot\phi^2-V$ for a homogeneous scalar field; the classical energy of a scalar field in 4+4 dimensions is not bounded below; the rules of Grassmann algebra, of conjugation and of left and right derivatives (Proposition 5.3); the two bilinear lemmas (Lemmas 5.4 and 5.5); the matrix identities $C^T=C$, $C^2=1$, $(C\gamma^a)^T=-C\gamma^a$ and the symmetric/antisymmetric split of $C\gamma^cS^{ab}$ from the Clifford relations and the transposition pattern of the gammas; the divergence identity from the covariant constancy of the gammas; and Theorem 5.6: in every gravitational field, with the canonical spin connection, the notebook's $\mathrm{Lg}[\,]$ is the total divergence $\partial_\mu(\tfrac12\sqrt{|g|}\,\Psi^TC\gamma^\mu\Psi)$ for a real Grassmann field, with the field equations $0=0$. With the notebook's own contraction the field equations are the algebraic $X\Psi=0$.

**What we assumed or took from elsewhere.** The Clifford relations, the symmetry pattern of the gammas and $C=\gamma^0\gamma^1\gamma^2\gamma^3$ are properties of the notebook's matrices, proved in Chapter 2 and verified exactly by the repository. The canonical spin connection and the covariant constancy $D_\mu\gamma^\nu=0$ come from Chapter 4 (they are equivalent to the vielbein postulate; the repository verifies them exactly at test points). The reading of cell 1064 as the formula of Section 5.12 is the transcription of the Stage-1 document. That a fermion field must have anticommuting (Grassmann) components is the physical premise of the whole construction, the classical counterpart of the anticommutators of Chapter 8; no spin–statistics theorem is proved for signature (4,4) in this book. That the matrix $X$ of the notebook contraction has rank 16 is a computed fact at six test points, not a theorem for every field. Fields are assumed smooth and to vanish near the boundary of the region of integration whenever we integrate by parts.

### 5.17 Exercises

**Exercise 5.1.** Show that $L=\tfrac12\dot q^2-\tfrac12\omega^2q^2+\frac{d}{dt}\bigl(q^3\bigr)$ has the same Euler–Lagrange equation as the harmonic oscillator.

**Exercise 5.2.** For the scalar field of Section 5.5 with $m=2$, compute $\omega^2$ for the wave numbers $k_0=1$, $k_7=1$ (all others 0) and for $k_0=1$, $k_7=3$. Which one grows in time, and how fast?

**Exercise 5.3.** A homogeneous scalar field has $\dot\phi=1$ and $V=3/2$ at some moment. Compute $\rho$, $p$ and $w$. Repeat for $\dot\phi=2$, $V=0$.

**Exercise 5.4.** For the complex oscillator $L=\tfrac i2(\psi^\ast\dot\psi-\dot\psi^\ast\psi)-\omega\psi^\ast\psi$ (commuting $\psi$) compute the energy $H=\dot\psi\,\partial L/\partial\dot\psi+\dot\psi^\ast\,\partial L/\partial\dot\psi^\ast-L$.

**Exercise 5.5.** In the Grassmann algebra with generators $\theta_0,\theta_1,\theta_2$ compute $(\theta_0+\theta_1\theta_2)^2$ and $(\theta_0+\theta_1)(\theta_0-\theta_1)$.

**Exercise 5.6.** For $F=\theta_0\theta_1\theta_2+\theta_1\theta_2$ compute the left and the right derivatives with respect to $\theta_1$ and with respect to $\theta_2$. Which part of $F$ changes sign between left and right, and why?

**Exercise 5.7.** For a real Grassmann column $\Psi=(\Psi_0,\Psi_1,\Psi_2)^T$ and $M=\begin{pmatrix}0&1&2\\3&0&4\\5&6&0\end{pmatrix}$, compute $\Psi^TM\Psi$ and check Lemma 5.4.

**Exercise 5.8.** Show by an example that Lemma 5.5 is false for commuting fields: take $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ and $q(x)=(\cos x,\sin x)^T$.

**Exercise 5.9.** Using the tables of the Student Guide (row 4 of $\gamma^4$ reads “$+9$”, row 13 of $\gamma^4$ reads “$+0$”, row 0 of $C$ reads “$-4$”, row 9 of $C$ reads “$+13$”), find the entries $(0,9)$ and $(9,0)$ of $C\gamma^4$, confirm the antisymmetry of expression [1] there, and write the corresponding term of $\Psi^TC\gamma^4\Psi$.

**Exercise 5.10.** Let $\theta$ be one complex Grassmann variable. Show that $\theta^\ast\theta\ne0$ although $\theta\theta=0$, and that $(\theta^\ast\theta)^2=0$. For two complex variables and $S=\theta_0^\ast\theta_0-\theta_1^\ast\theta_1$, compute $S^2$ and $S^3$.

**Exercise 5.11.** For two real Grassmann fields and the antisymmetric $X=\begin{pmatrix}0&x\\-x&0\end{pmatrix}$ with an ordinary number $x\ne0$, compute $\tfrac12\Psi^TX\Psi$, its Euler–Lagrange expressions, and the solutions of the resulting equations.

**Exercise 5.12.** Check $\det(1+\epsilon A)=1+\epsilon\,\mathrm{tr}A+O(\epsilon^2)$ for $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$.

### 5.18 Answers to the exercises

**Answer 5.1.** The extra term is $F=3q^2\dot q$. Its contribution to the Euler–Lagrange expression is $\partial F/\partial q-\frac{d}{dt}\partial F/\partial\dot q=6q\dot q-\frac{d}{dt}(3q^2)=6q\dot q-6q\dot q=0$, so the equation is still $\ddot q=-\omega^2q$ (Proposition 5.1 in one dimension).

**Answer 5.2.** $\omega^2=m^2+k_0^2-k_7^2$. For $k_7=1$: $\omega^2=4+1-1=4$, $\omega=\pm2$, an oscillation. For $k_7=3$: $\omega^2=4+1-9=-4$; the time dependence is $e^{\pm2x_4}$, and the solution with $e^{+2x_4}$ grows by the factor $e^2\approx7.39$ per unit of $x_4$.

**Answer 5.3.** $\rho=\tfrac12\cdot1+\tfrac32=2$, $p=\tfrac12-\tfrac32=-1$, $w=-1/2$. For $\dot\phi=2$, $V=0$: $\rho=p=2$ and $w=1$.

**Answer 5.4.** $\partial L/\partial\dot\psi=\tfrac i2\psi^\ast$ and $\partial L/\partial\dot\psi^\ast=-\tfrac i2\psi$, so $H=\tfrac i2\psi^\ast\dot\psi-\tfrac i2\dot\psi^\ast\psi-\tfrac i2(\psi^\ast\dot\psi-\dot\psi^\ast\psi)+\omega\psi^\ast\psi=\omega\,\psi^\ast\psi$. The time derivatives drop out: for a first-order Lagrangian they carry no energy, a fact that returns for dirac16complex in Chapter 7.

**Answer 5.5.** $(\theta_0+\theta_1\theta_2)^2=\theta_0\theta_0+\theta_0\theta_1\theta_2+\theta_1\theta_2\theta_0+\theta_1\theta_2\theta_1\theta_2=0+\theta_0\theta_1\theta_2+\theta_0\theta_1\theta_2+0=2\theta_0\theta_1\theta_2$ (moving $\theta_0$ to the front of $\theta_1\theta_2\theta_0$ takes two exchanges). So an element with an odd and an even part need not square to zero. $(\theta_0+\theta_1)(\theta_0-\theta_1)=\theta_0\theta_0-\theta_0\theta_1+\theta_1\theta_0-\theta_1\theta_1=-2\theta_0\theta_1$.

**Answer 5.6.** With respect to $\theta_1$: left $-\theta_0\theta_2+\theta_2$, right $-\theta_0\theta_2-\theta_2$. With respect to $\theta_2$: left $\theta_0\theta_1-\theta_1$ (in $\theta_0\theta_1\theta_2$ the generator $\theta_2$ passes two others, in $\theta_1\theta_2$ one), right $\theta_0\theta_1+\theta_1$. The even part $\theta_1\theta_2$ changes sign between left and right, the odd part $\theta_0\theta_1\theta_2$ does not: by the proof of Proposition 5.3 the two signs differ by $(-1)^{n-1}$, which is $-1$ for even degree $n$ and $+1$ for odd degree.

**Answer 5.7.** Collect each pair $a<b$: the coefficient of $\Psi_a\Psi_b$ is $M_{ab}-M_{ba}$. So $\Psi^TM\Psi=(1-3)\Psi_0\Psi_1+(2-5)\Psi_0\Psi_2+(4-6)\Psi_1\Psi_2=-2\Psi_0\Psi_1-3\Psi_0\Psi_2-2\Psi_1\Psi_2$; the diagonal of $M$ is zero anyway. With $M_A=\tfrac12(M-M^T)$ the coefficients are $2(M_A)_{ab}=M_{ab}-M_{ba}$, the same numbers.

**Answer 5.8.** $q^TAq'=q_0q_1'-q_1q_0'=\cos x\cos x-\sin x\,(-\sin x)=1$, while $q^TAq=q_0q_1-q_1q_0=0$ for commuting numbers. Lemma 5.5 would claim $1=\tfrac12\cdot0'-0=0$. Its proof needs the exchange $\partial_\mu\Psi_a\,\Psi_b=-\Psi_b\,\partial_\mu\Psi_a$, which holds only for anticommuting fields.

**Answer 5.9.** $(C\gamma^4u)_0=-(\gamma^4u)_4=-u_9$, so the entry $(0,9)$ is $-1$. $(C\gamma^4u)_9=+(\gamma^4u)_{13}=+u_0$, so the entry $(9,0)$ is $+1$. The two entries are opposite, as $(C\gamma^4)^T=-C\gamma^4$ requires. In $\Psi^TC\gamma^4\Psi$ they give $-\Psi_0\Psi_9+\Psi_9\Psi_0=-2\Psi_0\Psi_9$.

**Answer 5.10.** $\theta$ and $\theta^\ast$ are different generators, so $\theta^\ast\theta$ is a nonzero monomial, while $\theta\theta=0$ because a generator squares to zero. $(\theta^\ast\theta)^2=\theta^\ast\theta\theta^\ast\theta$ contains $\theta$ twice and vanishes. With $P_0=\theta_0^\ast\theta_0$ and $P_1=-\theta_1^\ast\theta_1$ (even, commuting, $P_a^2=0$): $S^2=2P_0P_1=-2\,\theta_0^\ast\theta_0\theta_1^\ast\theta_1$ and $S^3=0$. With 16 components the same reasoning gives $S^{17}=0$ (Section 5.9).

**Answer 5.11.** $\tfrac12\Psi^TX\Psi=\tfrac12(x\Psi_0\Psi_1-x\Psi_1\Psi_0)=x\Psi_0\Psi_1$. There are no derivatives, so $E_0=\partial_L(x\Psi_0\Psi_1)/\partial\Psi_0=x\Psi_1=(X\Psi)_0$ and $E_1=\partial_L(-x\Psi_1\Psi_0)/\partial\Psi_1=-x\Psi_0=(X\Psi)_1$. The equations $x\Psi_1=0$ and $x\Psi_0=0$ with $x\ne0$ give $\Psi=0$: no field survives.

**Answer 5.12.** $\det\begin{pmatrix}1+\epsilon&2\epsilon\\3\epsilon&1+4\epsilon\end{pmatrix}=(1+\epsilon)(1+4\epsilon)-6\epsilon^2=1+5\epsilon-2\epsilon^2$, and $\mathrm{tr}A=5$.
