## 14. The Kohn-Sham model of dirac16complex in the deflating primordial field

Chapter 13 taught density functional theory from zero: how the hopeless problem of many interacting quanta is replaced by a problem of independent quanta that move in a common, self-made potential, the Kohn-Sham problem. This chapter builds that problem for the quanta of the field dirac16complex in the author's primordial universe, whose three extra times deflate exponentially while ordinary space inflates. Everything is done exactly where it can be done: the change to the hidden coordinate $y$, the removal of the spin connection, the splitting of the 16 spinor components into eight independent pairs, the boundary conditions, the exact rescaling between the instants of the deflating history, the exact free spectra, and the exact exchange energy of the contact interaction. Four complete notebooks, 14a to 14d, repeat every step with the computer and reproduce the numbers of the Revision record.

### 14.1 What this chapter does

**Why a Kohn-Sham model.** The field dirac16complex has 16 complex anticommuting components at every point of the eight-dimensional universe of the author, and its quanta interact through the contact term $U(S) = \tfrac{\lambda}{2}S^2$ of the Lagrangian (Chapter 7). A state of many such quanta cannot be computed exactly. The Kohn-Sham method of Chapter 13 replaces it by a state of independent quanta, each described by its own wave function, called an **orbital**, which obeys a one-quantum equation with an effective mass $M_{\rm eff}$ and a potential $v_v$ made by all the other quanta. Solving that equation self-consistently is the work of Chapter 15. This chapter prepares it: it turns the one-quantum equation into a form a computer can solve, finds its exact solutions where they exist, and derives the effective mass and potential.

**What is derived, in order.**

- The hidden coordinate $y$ and the warped form of the author's metric (Section 14.2).
- The Kohn-Sham equation of dirac16complex, the good sector and the stationary-slice ansatz (Section 14.3).
- The spin-connection term $3H\gamma^{(x_8)}$, why the time derivative of $a_4$ drops out of it, and the factor $W^{-3}$ that removes it (Section 14.4).
- The splitting of the 16 components into eight independent $2 \times 2$ blocks of two types (Section 14.5), and the chirality matrix $\Gamma$ and the rotations of 3-space on these blocks (Section 14.6).
- The exact rescaling identity between the instants of the deflating history (Section 14.7).
- The block equation in real form and its boundary conditions at the brane and at the tip (Section 14.12), the exact free levels at zero 3-momentum (Section 14.13) and the shooting method that finds every level by an integer label (Section 14.14).
- The brane band that grows out of the zero modes when the 3-momentum is switched on, its exact slope, its redshift along the history, its insensitivity to the tip angle at the cutoff $L = 3$ and the slice 0, what the Revision record measured about the position $L$ of the cutoff itself, and the closed shells of the free filling (Sections 14.19 to 14.21).
- The exact local exchange energy of the contact interaction, the Kohn-Sham potentials, the exact Fock exchange of the model's states and the state of the eight zero modes (Sections 14.26 and 14.27).

**The four notebooks.**

| notebook | what it computes | PASS lines | figures |
| --- | --- | --- | --- |
| 14a | the block reduction and the rescaling identity, with exact algebra | 28 | 5 |
| 14b | the free spectra at zero 3-momentum, exact against numerical | 20 | 6 |
| 14c | the brane band, its slope, redshift, symmetries and closed shells | 15 | 6 |
| 14d | the exact local exchange, the potentials and the zero-mode state | 16 | 4 |

None of them needs Rust: Notebooks 14b and 14c write the shooting function of the Revision Rust solver (the same RK4 integration and Pruefer angle) in a few lines of numpy, find its roots by plain bisection where the Rust solver uses a safeguarded Newton-bisection, and reproduce the solver's recorded numbers; Chapter 15 runs the Rust solver itself.

**The status of every statement.** As everywhere in this book, every statement carries one of the five labels of Chapter 0: PROVED, COMPUTED, ASSUMED, HYPOTHESIS, OPEN. In this chapter they are used as follows.

- PROVED: every identity of Sections 14.2 to 14.7, the boundary-condition facts of Section 14.12, the exact spectra of Section 14.13, the counting property of the shooting angle in Section 14.14, the slope formula of Section 14.19 and the exchange formulas of Sections 14.26 and 14.27. The counting property is proved in the text of Section 14.14 and checked numerically by Notebook 14b; each of the others is verified in the Revision record by sympy in `Revision/kohn_sham/reports/ks-theory-python.json` (in its present state 58 of 58 checks passed), most of them also by WolframScript in `Revision/kohn_sham/reports/ks-theory-wolfram.json` (46 of 46 checks passed), and again by the notebooks of this chapter; the check names are given with each statement.
- COMPUTED: the numerical levels, slopes, shifts and closed shells; each comes with its measured error and the record file it reproduces (the Rust solver's report `Revision/kohn_sham/reports/ks-rust-solver.json`, in its present state 42 of 42 checks passed, and its result files).
- ASSUMED: the good sector (no dependence on the extra times); the Z2 mirror brane at $y = 0$; the regular tip condition at the cutoff $y = -L$, $L = 3$ (a choice of the numerical model; Section 14.20 shows that at this cutoff and at the slice $a_{4,0} = 0$, where it was measured, the brane band at nonzero 3-momentum does not feel the tip angle $\theta$, while at the later slices this is not established, and reports what the Revision record measured about the cutoff $L$ itself: the free results with $k \ne 0$ converge as $L$ grows, but the recorded $L = 3$ values are low by up to 1.4% in the Kohn-Sham energy, the nonzero (bulk) $k = 0$ levels approach $\pm m$ only algebraically, and the interaction energy of the brane zero modes depends strongly on $L$); the deflating history $a_4 = AHx_4$ along which the Kohn-Sham states are computed, which is a **prescribed background**, given and not solved for (Section 14.3); the convention that counts the zero modes at zero 3-momentum as particle levels (Section 14.21).
- OPEN: the justification of that convention (Section 14.21), the effect of the tip angle at the later slices (Section 14.20), and the behaviour of the gas when the history is not slow (the time-dependent problem, Chapter 15 and Chapter 22).
- HYPOTHESIS: none in this chapter.

**Notation and units.** The author's coordinates are $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which deflate exponentially; $x_8$ is the hidden space direction. The flat frame metric is $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in this order. The gamma matrix of the direction $x_4$ is written $\gamma^{(x_4)}$, and so on; these are the author's eight real $16 \times 16$ matrices of Chapters 4 and 5, read from the record `Revision/algebra/gammas.json`, with the Clifford relation $\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}$. The matrices $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$, $B = -iC\gamma^{(x_4)}$ and the chirality $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)} = \mathrm{diag}(-1_8, 1_8)$ are those of Chapter 5. The three **Pauli matrices**, written row by row, are

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .
$$

Each squares to the $2 \times 2$ unit matrix, two different ones anticommute, and their products are $\sigma_1\sigma_2 = i\sigma_3$, $\sigma_2\sigma_3 = i\sigma_1$, $\sigma_3\sigma_1 = i\sigma_2$ (and with the order reversed the sign changes). In the numbers of this chapter the author's constant $H$ is 1 and the mass $m$ of dirac16complex is 1, as in the Revision runs; energies, momenta and temperatures are then in units of $m$ (which equals $H$), lengths in units of $1/H$.

### 14.2 The author's field and the hidden coordinate y

**The metric.** The author's primordial field is the diagonal metric whose entries, in the order $x_1, \dots, x_8$, are

$$
\begin{aligned}
g = \mathrm{diag}\big(&e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ -1,\\
&-e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ \cot^2 z\big),
\end{aligned}
$$

with $z = 6Hx_8$ between $0$ and $\pi/2$, the author's constant $H > 0$, and a function $a_4(x_4)$ of the time. A **scale factor** is the number by which a coordinate step must be multiplied to give a length: along $x_1$ a step $dx_1$ has the length $e^{a_4}\sin^{1/6}z\,dx_1$ (the square root of the entry). When $a_4$ grows with the time, the 3-space factor $e^{a_4}$ grows (3-space **inflates**) and the extra-time factor $e^{-a_4}$ shrinks exponentially (the extra times **deflate**). The history used in this book is $a_4 = AHx_4$ with $A = 1$ (Section 14.3).

**The hidden coordinate.** The entry $g_{88} = \cot^2 z$ makes the hidden direction awkward. We replace $x_8$ by

$$
y = \frac{\ln(\sin z)}{6H}, \qquad z = 6Hx_8 .
$$

Line by line:

$$
\frac{dy}{dx_8} = \frac{1}{6H}\cdot\frac{\cos z}{\sin z}\cdot 6H = \cot z .
$$

Rule: the chain rule; the derivative of $\ln u$ is $1/u$ times the derivative of $u$, the derivative of $\sin z$ is $\cos z$, and $dz/dx_8 = 6H$.

$$
dy^2 = \cot^2 z\, dx_8^2 = g_{88}\,dx_8^2 .
$$

Rule: square the previous line. So $y$ measures length along the hidden direction, and in the coordinate $y$ the metric entry is simply 1.

$$
e^{6Hy} = \sin z, \qquad \sin^{1/3}z = e^{2Hy} .
$$

Rule: multiply the definition of $y$ by $6H$ and take the exponential of both sides; then take the power $1/3$.

When $z$ runs from 0 to $\pi/2$, $\sin z$ runs from 0 to 1 and $y$ from $-\infty$ to 0. The end $y \to -\infty$ ($z \to 0$) is called the **tip**; the end $y = 0$ ($z = \pi/2$), where the author's coordinate patch ends, is called the **brane**. The **warp factor** is $W = e^{Hy}$; by the last line, $\sin^{1/3}z = W^2$, and the metric takes the **warped form**

$$
ds^2 = e^{2Hy}\left[e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - e^{-2a_4}(dx_5^2 + dx_6^2 + dx_7^2)\right] - dx_4^2 + dy^2 .
$$

Its scale factors (the entries of the diagonal **vielbein**, the square roots of the absolute values of the metric entries) are

$$
h = \big(e^{a_4}W,\ e^{a_4}W,\ e^{a_4}W,\ 1,\ e^{-a_4}W,\ e^{-a_4}W,\ e^{-a_4}W,\ 1\big) .
$$

**The volume.** The square root of the absolute value of the determinant of a diagonal metric is the product of its scale factors:

$$
\sqrt{|g|} = (e^{a_4}W)^3\cdot 1\cdot(e^{-a_4}W)^3\cdot 1 = e^{3a_4}e^{-3a_4}W^6 = W^6 = e^{6Hy} .
$$

Rule: multiply the eight entries of $h$; the powers $e^{3a_4}$ and $e^{-3a_4}$ cancel. In the author's $x_8$ chart the same product is $\sin z\cdot\cot z = \cos z$; the two differ by the factor $dy/dx_8 = \cot z$, as they must. Neither contains $a_4$: while 3-space inflates and the extra times deflate, the volume of the seven directions other than the time stays the same. Toward the tip the factor $W^6$ goes to zero: at $y = -3$ it is $e^{-18}$. Status: PROVED; checks geometry_hidden_coordinate, geometry_sqrt_det and geometry_warped_form of `Revision/kohn_sham/reports/ks-theory-python.json` (the first two also in the Wolfram report `Revision/kohn_sham/reports/ks-theory-wolfram.json`).

**The momentum weight.** A plane wave $e^{ik_1x_1}$ along 3-space has the coordinate momentum $k_1$; the length of a coordinate step is $e^{a_4}W\,dx_1$, so the momentum per unit length, the one a quantum feels, is $k_1/(e^{a_4}W)$. We write

$$
\kappa(y, x_4) = \frac{1}{e^{a_4}W} = e^{-Hy - a_4(x_4)}
$$

for this **momentum weight**. It grows toward the tip (a given coordinate momentum costs more energy far from the brane) and, at a fixed $y$, it decreases as $a_4$ grows (3-momenta are **redshifted** while 3-space inflates).

### 14.3 The Kohn-Sham equation, the good sector and the stationary-slice ansatz

**The Kohn-Sham equation.** The field equation of dirac16complex is $\gamma^\mu D_\mu\Psi = (m + U'(S))\Psi$ (Chapter 7), where $\gamma^\mu = \gamma^{(\mu)}/h_\mu$ are the curved gammas and $D_\mu = \partial_\mu + \Omega_\mu$ is the covariant derivative with the spin connection $\Omega_\mu$ (Chapter 6). In the Kohn-Sham model every orbital obeys the one-quantum equation

$$
\gamma^\mu D_\mu\Psi = \big(M_{\rm eff}(y) - i\,v_v(y)\,\gamma^{(x_4)}\big)\Psi ,
$$

where the **effective mass** $M_{\rm eff} = m + \tfrac{15}{16}\lambda S$ and the **vector potential** $v_v = -\tfrac{1}{16}\lambda n$ are made by all the quanta through their scalar density $S$ and number density $n$. Sections 14.26 and 14.27 derive these two formulas exactly; until then $M_{\rm eff}$ and $v_v$ are any two real functions of $y$, written $M$ and $v$ for short.

**The good sector (ASSUMED).** We look only for orbitals that do not depend on the extra times $x_5, x_6, x_7$. Chapters 8 and 10 explain why: modes with enough momentum along the extra times grow without bound (the problem is ill-posed in the sense of Hadamard), and a quantum space of states with a positive norm has been built only for single good-sector momenta with frozen coefficients (Chapter 10); a positive-norm space of states for the whole field is OPEN. This restriction is an assumption of the Revision theory, not a result.

**The box.** The three directions of 3-space are taken as a **torus** of coordinate size $\ell$: a quantum leaving the box on one side comes back on the other, so the allowed coordinate momenta are $\mathbf k = \Delta k\,(n_1, n_2, n_3)$ with whole numbers $n_1, n_2, n_3$ and $\Delta k = 2\pi/\ell$. The Revision runs use $\Delta k = 0.25$, so $\ell = 8\pi \approx 25.13$. The extra times have the coordinate volume $v_t$ ($v_t = 1$ in the runs).

**The ansatz.** An **ansatz** is a guessed form of the solution with unknown parts to be determined. We try

$$
\Psi = e^{i\mathbf k\cdot\mathbf x}\,W(y)^{-3}\,\chi(y, x_4) ,
$$

a plane wave along 3-space, the factor $W^{-3} = e^{-3Hy}$, and a column $\chi$ of 16 unknown functions of $y$ and of the time. Section 14.4 shows that $\chi$ obeys exactly, for every history $a_4(x_4)$, an equation of the form

$$
i\,\partial_{x_4}\chi = h(x_4)\,\chi ,
$$

with a Hermitian matrix operator $h$ that depends on the time only through $a_4(x_4)$. This is the exact evolution of one orbital in the mean field.

**The stationary-slice (adiabatic) ansatz.** A **slice** is one instant $x_4$ of the history; $a_{4,0} = a_4(x_4)$ is the value of $a_4$ there. At a slice we freeze $h$ at its value $h(a_{4,0})$ and look for the stationary orbitals

$$
h(a_{4,0})\,\chi = \varepsilon\,\chi, \qquad \Psi = e^{-i\varepsilon x_4}\,e^{i\mathbf k\cdot\mathbf x}\,W^{-3}\,\chi(y)\,/\sqrt{\ell^3v_t}, \qquad \int_{-L}^{0}\chi^\dagger\chi\,dy = 1 .
$$

The number $\varepsilon$ is the **level** (the energy of the orbital), and the hidden direction is cut at $y = -L$ ($L = 3$ in the runs). The Kohn-Sham state of the slice fills the lowest particle levels. This is the **adiabatic** picture: if $h$ changes slowly enough along the history, a quantum stays in the level it occupies. The exact evolution conserves the 3-momentum, the block and the brane parity of every orbital (all defined below), so a quantum can only make transitions between levels of the same kind; Chapter 15 measures how slowly $h$ changes. The record states this in `Revision/kohn_sham/ks-theory.json`, section adiabaticity.

**The history is a PRESCRIBED BACKGROUND.** The slices are taken along the history $a_4 = AHx_4$ with $A = 1$, so $a_{4,0} = 0, 0.5, 1, 1.5, 2$ are five instants. This history is prescribed, not solved for: the field equations of $a_4$ (Chapter 12) allow the linear member $a_4 = AHx_4$ only with a source whose three pressures are equal and whose energy density is constant, and the Kohn-Sham states violate these conditions (their sources depend on $x_8$, and $p_3 \ne p_t$). The record `Revision/field_equations_a4/reports/ks-source-conditions.json` proves this with its checks ks_profiles_depend_on_x8, ks_profiles_violate_algebraic_condition and ks_history_is_a_prescribed_background (Chapter 17 explains it in full). So the Kohn-Sham gas is a **test field** on a given background: it feels the deflating field but does not act back on it.

### 14.4 The spin connection, the term 3H γ(x8) and the factor W^(-3)

**What we need.** The operator $\gamma^\mu D_\mu = \sum_\mu \gamma^\mu\partial_\mu + \sum_\mu\gamma^\mu\Omega_\mu$ contains the spin connection only through the matrix $\sum_\mu\gamma^\mu\Omega_\mu$. Chapter 6 derived the canonical spin connection in general; here we compute this one matrix for the diagonal vielbein $h$ of Section 14.2, with $a_4$ an arbitrary function of $x_4$, so that the result holds along every history.

**Step 1: the Christoffel symbols of a diagonal metric.** For a metric $g = \mathrm{diag}(g_{11}, \dots, g_{88})$ the Christoffel symbols $\Gamma^n{}_{mk} = \tfrac12 g^{nl}(\partial_m g_{lk} + \partial_k g_{lm} - \partial_l g_{mk})$ (sum over $l$) reduce to

$$
\Gamma^n{}_{mk} = \frac{\delta_{mn}\,\partial_k g_{nn} + \delta_{kn}\,\partial_m g_{nn} - \delta_{mk}\,\partial_n g_{mm}}{2g_{nn}} \qquad (\text{no sum}) .
$$

Rule: $g^{nl}$ is zero unless $l = n$, where it is $1/g_{nn}$, and $g_{lk}$ is zero unless $l = k$; the symbol $\delta_{mn}$ is 1 when $m = n$ and 0 otherwise. So a symbol is nonzero only when two of its three indices are equal.

**Step 2: the connection coefficients.** The vielbein postulate (Chapter 6) gives, for the diagonal vielbein with entries $h_A$,

$$
\omega_\mu{}^A{}_B = h_A\,\partial_\mu(1/h_B)\,\delta_{AB} + h_A\,\Gamma^A{}_{\mu B}/h_B \qquad (\text{no sum}) .
$$

Only $A \ne B$ will matter below, because the generators $S^{AB} = \tfrac14(\gamma^{(A)}\gamma^{(B)} - \gamma^{(B)}\gamma^{(A)})$ vanish for $A = B$. Take a direction $l$ whose scale factor $h_l$ depends on the coordinates, and $A \ne B$. From Step 1, with $g_{ll} = \eta_{ll}h_l^2$:

$$
\Gamma^l{}_{lB} = \frac{\partial_B g_{ll}}{2g_{ll}} = \frac{\partial_B h_l}{h_l}, \qquad \Gamma^A{}_{ll} = -\frac{\partial_A g_{ll}}{2g_{AA}} = -\eta_{ll}\eta_{AA}\frac{h_l\,\partial_A h_l}{h_A^2} ,
$$

and every other $\Gamma^A{}_{lB}$ with $A \ne B$ is zero. Rule: Step 1 with two equal indices; $\partial(h^2) = 2h\,\partial h$; and $1/\eta_{AA} = \eta_{AA}$ because $\eta_{AA} = \pm1$. Inserting into the formula for $\omega$:

$$
\omega_l{}^l{}_B = \frac{\partial_B h_l}{h_B}, \qquad \omega_l{}^A{}_l = -\eta_{ll}\eta_{AA}\frac{\partial_A h_l}{h_A} .
$$

**Step 3: the matrix $\Omega_l$.** With $\Omega_\mu = \tfrac12\sum_{A,B}\eta_{AA}\,\omega_\mu{}^A{}_B\,S^{AB}$ (Chapter 6):

$$
\Omega_l = \tfrac12\sum_{B \ne l}\eta_{ll}\frac{\partial_B h_l}{h_B}S^{lB} + \tfrac12\sum_{A \ne l}\eta_{AA}\Big(-\eta_{ll}\eta_{AA}\frac{\partial_A h_l}{h_A}\Big)S^{Al} = \eta_{ll}\sum_{B \ne l}\frac{\partial_B h_l}{h_B}\,S^{lB} .
$$

Rule: insert Step 2; in the second sum $\eta_{AA}\eta_{AA} = 1$, rename $A$ as $B$ and use $S^{Bl} = -S^{lB}$, so that the two sums are equal and add up. Since $\gamma^{(l)}\gamma^{(B)} = -\gamma^{(B)}\gamma^{(l)}$ for $B \ne l$, $S^{lB} = \tfrac12\gamma^{(l)}\gamma^{(B)}$.

**Step 4: one direction's contribution.** Multiply by the curved gamma $\gamma^l = \gamma^{(l)}/h_l$:

$$
\frac{\gamma^{(l)}}{h_l}\,\Omega_l = \frac{\eta_{ll}}{2h_l}\sum_{B \ne l}\frac{\partial_B h_l}{h_B}\,\gamma^{(l)}\gamma^{(l)}\gamma^{(B)} = \frac12\sum_{B \ne l}\frac{\partial_B \ln h_l}{h_B}\,\gamma^{(B)} .
$$

Rule: $\gamma^{(l)}\gamma^{(l)} = \eta_{ll}$ (the Clifford relation), $\eta_{ll}\eta_{ll} = 1$, and $\partial_B h_l/h_l = \partial_B\ln h_l$.

**Step 5: the author's field.** Here the scale factors depend only on $x_4$ (through $a_4$) and on $y$, and $h_{x_4} = h_y = 1$. For a 3-space direction, $\ln h_l = a_4 + Hy$, so $\partial_{x_4}\ln h_l = a_4'$ (the derivative $da_4/dx_4$) and $\partial_y\ln h_l = H$; Step 4 gives $\tfrac12 a_4'\gamma^{(x_4)} + \tfrac12 H\gamma^{(x_8)}$. For an extra time, $\ln h_l = -a_4 + Hy$, which gives $-\tfrac12 a_4'\gamma^{(x_4)} + \tfrac12 H\gamma^{(x_8)}$. For $x_4$ and $y$ themselves the scale factor is the constant 1, so $\Omega_{x_4} = \Omega_y = 0$. (In the vielbein language the frame direction of $y$ is that of $x_8$, so the gamma that goes with $y$ is $\gamma^{(x_8)}$.) Adding the eight contributions:

$$
\sum_\mu\gamma^\mu\Omega_\mu = 3\cdot\tfrac12 a_4'\gamma^{(x_4)} - 3\cdot\tfrac12 a_4'\gamma^{(x_4)} + 6\cdot\tfrac12 H\gamma^{(x_8)} = 3H\gamma^{(x_8)} .
$$

Rule: three inflating directions, three deflating directions, six warped directions. **The time-direction pieces of the three inflating directions, $+\tfrac32 a_4'\gamma^{(x_4)}$, and of the three deflating extra times, $-\tfrac32 a_4'\gamma^{(x_4)}$, cancel exactly**, for every history; what survives comes from the warp. Status: PROVED; checks `spin_connection_compatibility` (the curved gammas are covariantly constant, the proof that this is the right connection), `spin_connection_slash_3H`, `spin_connection_time_terms_cancel` and `spin_connection_time_term_value` of `Revision/kohn_sham/reports/ks-theory-python.json` (the first three also in the Wolfram report). Notebook 14a recomputes all of it with sympy and draws the eight contributions (its figure 3). That the surviving term $3H\gamma^{(x_8)}$ belongs to the diagonal vielbein, and can be removed by a change of frame or of the field, is the scope correction of Chapter 8.

**Step 6: the factor $W^{-3}$ removes it.** Insert the ansatz $\Psi = e^{i\mathbf k\cdot\mathbf x}W^{-3}\chi(y, x_4)$ into $\gamma^\mu D_\mu\Psi = \sum_\mu\gamma^\mu\partial_\mu\Psi + 3H\gamma^{(x_8)}\Psi$, term by term.

$$
\gamma^{(x_8)}\partial_y\big(e^{-3Hy}\chi\big) = e^{-3Hy}\big(\gamma^{(x_8)}\partial_y\chi - 3H\gamma^{(x_8)}\chi\big) .
$$

Rule: the product rule and $\partial_y e^{-3Hy} = -3He^{-3Hy}$. The term $-3H\gamma^{(x_8)}\chi$ cancels the $+3H\gamma^{(x_8)}\chi$ of the spin connection.

$$
\frac{\gamma^{(x_j)}}{e^{a_4}W}\,\partial_j e^{i\mathbf k\cdot\mathbf x} = i\kappa k_j\gamma^{(x_j)}\,e^{i\mathbf k\cdot\mathbf x}, \qquad j = 1, 2, 3 .
$$

Rule: $\partial_j e^{i\mathbf k\cdot\mathbf x} = ik_je^{i\mathbf k\cdot\mathbf x}$, and $1/(e^{a_4}W) = \kappa$ (Section 14.2). The time term is $\gamma^{(x_4)}\partial_{x_4}\chi$ (the scale factor of $x_4$ is 1), and the extra times give nothing (good sector). Dividing by the common factor $e^{i\mathbf k\cdot\mathbf x}e^{-3Hy}$, the Kohn-Sham equation becomes

$$
\gamma^{(x_8)}\partial_y\chi + \gamma^{(x_4)}\partial_{x_4}\chi + i\kappa k_j\gamma^{(x_j)}\chi = \big(M - iv\gamma^{(x_4)}\big)\chi \qquad (\text{sum over } j = 1, 2, 3) .
$$

The spin connection has disappeared, exactly and for every history. Without the factor $W^{-3}$ the term $3H\gamma^{(x_8)}\chi$ would survive. Status: PROVED; checks ansatz_removes_spin_connection and ansatz_without_W3_term_survives.

**Step 7: the Hamiltonian form.** Solve the last equation for the time derivative, line by line.

$$
\gamma^{(x_4)}\partial_{x_4}\chi = M\chi - iv\gamma^{(x_4)}\chi - \gamma^{(x_8)}\partial_y\chi - i\kappa k_j\gamma^{(x_j)}\chi .
$$

Rule: move every term except the time term to the right side.

$$
\partial_{x_4}\chi = -M\gamma^{(x_4)}\chi - iv\chi + \gamma^{(x_4)}\gamma^{(x_8)}\partial_y\chi + i\kappa k_j\gamma^{(x_4)}\gamma^{(x_j)}\chi .
$$

Rule: multiply from the left by $-\gamma^{(x_4)}$; on the left $-\gamma^{(x_4)}\gamma^{(x_4)} = -\eta_{44} = 1$; on the right $-\gamma^{(x_4)}(-iv\gamma^{(x_4)}) = iv\gamma^{(x_4)}\gamma^{(x_4)} = -iv$.

$$
i\partial_{x_4}\chi = h\chi, \qquad h = i\gamma^{(x_4)}\gamma^{(x_8)}\partial_y - \kappa k_j\gamma^{(x_4)}\gamma^{(x_j)} + M\big(-i\gamma^{(x_4)}\big) + v .
$$

Rule: multiply by $i$ and use $i\cdot i = -1$.

**Why $h$ is Hermitian.** A matrix $X$ is **Hermitian** when it equals its conjugate transpose, $X^\dagger = X$; an operator is Hermitian (self-adjoint) when $\int\varphi^\dagger(h\chi)\,dy = \int(h\varphi)^\dagger\chi\,dy$ for all allowed columns $\varphi$, $\chi$; then its levels are real and orbitals of different levels are orthogonal. Each piece of $h$ qualifies. (i) $\gamma^{(x_4)}\gamma^{(x_8)}$ is real and symmetric: $(\gamma^{(x_4)}\gamma^{(x_8)})^T = (\gamma^{(x_8)})^T(\gamma^{(x_4)})^T = \gamma^{(x_8)}(-\gamma^{(x_4)}) = \gamma^{(x_4)}\gamma^{(x_8)}$, by the symmetry pattern $(\gamma^a)^T = \eta_{aa}\gamma^a$ of Chapter 5 and the anticommutation of two different gammas; so $i\gamma^{(x_4)}\gamma^{(x_8)}$ is anti-Hermitian, $\partial_y$ is anti-Hermitian too (integration by parts, when the boundary terms vanish, Section 14.12), and the product of the two, which commute, is Hermitian. (ii) $\gamma^{(x_4)}\gamma^{(x_j)}$ for a 3-space direction is real and symmetric by the same rule, hence Hermitian. (iii) $(-i\gamma^{(x_4)})^\dagger = i(\gamma^{(x_4)})^T = -i\gamma^{(x_4)}$, and $(-i\gamma^{(x_4)})^2 = -\eta_{44} = 1$. (iv) $v$ is a real number times the unit matrix. Status: PROVED; check hamiltonian_16_hermitian.

**The flat measure.** The Hilbert norm of the problem is $\int\chi^\dagger\chi\,dy$: since $\sqrt{|g|}\,\Psi^\dagger\Psi = e^{6Hy}e^{-6Hy}\chi^\dagger\chi$, it is the integral of $\sqrt{|g|}\,\Psi^\dagger\Psi$ over the hidden direction, with the plain measure $dy$. It does not contain $a_4$.

### 14.5 Eight blocks of two components

**Only $|\mathbf k|$ matters.** Section 14.6 shows that a rotation of 3-space does not change the levels. So we may turn $\mathbf k$ into the direction $x_1$, $\mathbf k = (k, 0, 0)$. Then $h$ contains only the three gammas $\gamma^{(x_8)}$, $\gamma^{(x_1)}$, $\gamma^{(x_4)}$, and it is convenient to name three products:

$$
A_0 = \gamma^{(x_8)}, \qquad A_1 = \gamma^{(x_8)}\gamma^{(x_1)}, \qquad A_4 = \gamma^{(x_8)}\gamma^{(x_4)} .
$$

**Two rules from Chapter 5.** Let $P$ be a product of $p$ different gammas. (Rule 1) Moving a gamma $\gamma^c$ from the left of $P$ to its right gives the sign $(-1)^{p-1}$ if $\gamma^c$ is one of the factors and $(-1)^p$ if it is not, because passing each different factor costs a sign. (Rule 2) $PP = (-1)^{p(p-1)/2}$ times the product of the $\eta$ of its factors.

**Three labels.** Define

$$
J = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_4)}, \qquad K_1 = \gamma^{(x_2)}\gamma^{(x_3)}, \qquad K_2 = \gamma^{(x_5)}\gamma^{(x_6)} .
$$

By Rule 1, $J$ ($p = 3$) commutes with its own three factors and anticommutes with the five other gammas; $K_1$ ($p = 2$) anticommutes with $\gamma^{(x_2)}$, $\gamma^{(x_3)}$ and commutes with the six others; $K_2$ anticommutes with $\gamma^{(x_5)}$, $\gamma^{(x_6)}$ and commutes with the others. A product of gammas commutes with $J$ when it contains an even number of factors that anticommute with $J$. Therefore all three commute with $A_0, A_1, A_4$ (built from $\gamma^{(x_8)}, \gamma^{(x_1)}, \gamma^{(x_4)}$), with $C$ (for $J$ the two anticommuting factors $\gamma^{(x_2)}, \gamma^{(x_3)}$ give two signs, which cancel), with $B = -iC\gamma^{(x_4)}$, and with each other. By Rule 2:

$$
J^2 = (-1)^3\,\eta_{88}\eta_{11}\eta_{44} = (-1)(1)(1)(-1) = +1,
$$

$$
K_1^2 = (-1)^1\eta_{22}\eta_{33} = -1, \qquad K_2^2 = (-1)^1\eta_{55}\eta_{66} = -1 .
$$

So $J$ has the eigenvalues $j = \pm1$, and $K_1$, $K_2$ have the eigenvalues $is_2$, $is_3$ with $s_2, s_3 = \pm1$ (if $Xu = cu$ for a column $u \ne 0$ and $X^2 = 1$, then $u = X^2u = c^2u$, so $c^2 = 1$; with $X^2 = -1$ the same step gives $c^2 = -1$). Status: PROVED; check blocks_commuting_set.

**The projectors.** A **projector** is a matrix with $P^2 = P$; its eigenvalues are 0 or 1 (from $\lambda^2 = \lambda$), so its trace equals the number of eigenvalues 1, its **rank** (the dimension of the space it projects onto). For each of the eight label triples put

$$
P(j, s_2, s_3) = \frac{1 + jJ}{2}\cdot\frac{1 - is_2K_1}{2}\cdot\frac{1 - is_3K_2}{2} .
$$

Each factor is $\tfrac12(1 + X)$ with $X^2 = 1$ ($(jJ)^2 = 1$, $(-is_2K_1)^2 = -K_1^2 = 1$), hence a projector; the three factors commute, so their product is a projector; it keeps exactly the columns with $J = j$, $K_1 = is_2$, $K_2 = is_3$. Multiplied out, $P$ is $\tfrac18$ times the unit matrix plus seven products of different gammas ($J$, $K_1$, $K_2$, $JK_1$, $JK_2$, $K_1K_2$, $JK_1K_2$, each with a number in front), and every product of one or more different gammas has trace 0 (Rule 5 of Chapter 5). So

$$
\mathrm{tr}\,P(j, s_2, s_3) = \tfrac18\,\mathrm{tr}\,1 = \tfrac{16}{8} = 2 .
$$

The eight projectors have rank 2 and add up to the unit matrix: **the 16 components split into eight blocks of two**. Status: PROVED; check blocks_projectors.

**A basis in each block.** Inside a block, $A_0 = \gamma^{(x_8)}$ squares to 1 and $A_1$ anticommutes with it ($A_1 = \gamma^{(x_8)}\gamma^{(x_1)}$ contains $\gamma^{(x_8)}$ once and $p = 2$, so by Rule 1 the sign is $-1$), so $A_0$ has the eigenvalue $+1$ once and $-1$ once in the block. The record chooses

$$
v_+ = 8\,P(j, s_2, s_3)\,\tfrac12\big(1 + \gamma^{(x_8)}\big)\,e_c, \qquad v_- = A_1v_+ ,
$$

where $e_c$ is the first unit column (counting $c$ from 0) that gives a nonzero $v_+$. Then $A_0v_+ = v_+$ and $A_0v_- = A_0A_1v_+ = -A_1A_0v_+ = -v_-$. The 16 columns $v_+, v_-$ of the eight blocks, in the order $(j, s_2, s_3) = (1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)$, form the matrix $U$; every entry of $U$ is $0$, $\pm1$ or $\pm i$, every column has length $\sqrt8 = 2\sqrt2$, and $V = U/(2\sqrt2)$ is **unitary** ($V^\dagger V = 1$: a change of basis that keeps lengths). The seed columns are $c = 4, 0, 0, 4, 0, 4, 4, 0$. The record stores $U$ entry by entry in `Revision/kohn_sham/ks-theory.json` (blockBasis), and the Rust solver uses it. Status: PROVED; check blocks_basis_unitary.

**The block forms.** In the basis $(v_+, v_-)$ of one block every matrix that commutes with $J, K_1, K_2$ becomes a $2 \times 2$ matrix. Column $k$ of the $2 \times 2$ matrix is the image of the $k$-th basis vector. Line by line:

$$
A_0 \to \sigma_3 .
$$

Rule: $A_0v_+ = v_+$ and $A_0v_- = -v_-$.

$$
A_1 \to \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = -i\sigma_2 .
$$

Rule: $A_1v_+ = v_-$ (first column $(0, 1)$), and $A_1v_- = A_1A_1v_+ = -v_+$ (second column $(-1, 0)$), because $A_1^2 = -1$ by Rule 2.

$$
A_4 \to j\sigma_1 .
$$

Rule: $A_4$ anticommutes with $A_0$ (Rule 1), so it has no diagonal entries; and $A_0A_1A_4 = \gamma^{(x_8)}\gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_8)}\gamma^{(x_4)} = \gamma^{(x_1)}\gamma^{(x_8)}\gamma^{(x_4)} = -J$, which is the number $-j$ in the block; with $\sigma_3(-i\sigma_2) = -i\sigma_3\sigma_2 = -\sigma_1$ the condition $-\sigma_1A_4 = -j$ gives $A_4 = j\sigma_1$.

$$
C = A_1K_1 \to (-i\sigma_2)(is_2) = s_2\sigma_2, \qquad B = -iJK_1 \to -i\,j\,(is_2) = js_2 .
$$

Rule: $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)} = A_1K_1$; and $JK_1 = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_4)}\gamma^{(x_2)}\gamma^{(x_3)} = C\gamma^{(x_4)}$ after moving $\gamma^{(x_4)}$ past two gammas (two signs), so $B = -iC\gamma^{(x_4)} = -iJK_1$. So $B$ is a number in every block, $+1$ or $-1$: the **Krein sign** $js_2$ of the block.

$$
\gamma^{(x_4)} = A_0A_4 \to ij\sigma_2, \qquad \gamma^{(x_1)} = A_0A_1 \to -\sigma_1, \qquad \gamma^{(x_4)}\gamma^{(x_1)} \to (ij\sigma_2)(-\sigma_1) = -j\sigma_3 .
$$

Rule: $A_0A_0 = 1$; the Pauli products $\sigma_3\sigma_1 = i\sigma_2$, $\sigma_3\sigma_2 = -i\sigma_1$, $\sigma_2\sigma_1 = -i\sigma_3$.

The record lists eleven such forms (for $\gamma^{(x_8)}$, $A_1$, $A_4$, $B$, $C$, $BC = -i\gamma^{(x_4)} \to j\sigma_2$, $\gamma^{(x_4)}\gamma^{(x_1)}$, $B\gamma^{(x_8)} \to js_2\sigma_3$, $J$, $K_1$, $K_2$); Notebook 14a checks all of them. Not every matrix is block diagonal: $\gamma^{(x_2)}$, $\gamma^{(x_5)}$ and $\gamma^{(x_8)}\gamma^{(x_2)}$ anticommute with $J$ and connect different blocks, which is why $\mathbf k$ was turned along $x_1$. Status: PROVED; checks blocks_forms and blocks_not_everything_block_diagonal.

**The block Hamiltonian.** Put the forms into $h$ of Section 14.4 with $\mathbf k = (k, 0, 0)$: $i\gamma^{(x_4)}\gamma^{(x_8)} = -iA_4 \to -ij\sigma_1$; $-\kappa k\gamma^{(x_4)}\gamma^{(x_1)} \to j\kappa k\sigma_3$; $M(-i\gamma^{(x_4)}) \to jM\sigma_2$. So in every block of type $j$

$$
h_j = j\left[-i\sigma_1\frac{d}{dy} + M\sigma_2 + \kappa k\,\sigma_3\right] + v .
$$

It depends on $j$ but not on $s_2$, $s_3$: there are only **two types of block**, four blocks of each type. Status: PROVED; check block_hamiltonian.

**The first-order form.** The eigenvalue equation $h_j\chi = \varepsilon\chi$ is a pair of first-order differential equations. Line by line:

$$
-ij\sigma_1\chi' = (\varepsilon - v)\chi - j(M\sigma_2 + \kappa k\sigma_3)\chi .
$$

Rule: move the terms without derivative to the right; $\chi'$ is $d\chi/dy$.

$$
\chi' = ij(\varepsilon - v)\sigma_1\chi - i\,(M\sigma_1\sigma_2 + \kappa k\,\sigma_1\sigma_3)\chi .
$$

Rule: multiply from the left by $ij\sigma_1$; $(ij\sigma_1)(-ij\sigma_1) = j^2\sigma_1^2 = 1$ and $j\cdot j = 1$.

$$
\chi' = N\chi, \qquad N = M\sigma_3 - \kappa k\,\sigma_2 + ij(\varepsilon - v)\,\sigma_1 .
$$

Rule: $\sigma_1\sigma_2 = i\sigma_3$, $\sigma_1\sigma_3 = -i\sigma_2$, so $-i(iM\sigma_3 - i\kappa k\sigma_2) = M\sigma_3 - \kappa k\sigma_2$. Status: PROVED; check block_ode_equivalent.

**The two types mirror each other.** Write $h_j - v = jD(M, k)$ with $D(M, k) = -i\sigma_1\,d/dy + M\sigma_2 + \kappa k\sigma_3$. Then:

- $h_{-1} - v = -(h_{+1} - v)$. For $v = 0$ the levels of the blocks $j = -1$ are the negatives of those of $j = +1$.
- $\sigma_3D(M, k)\sigma_3 = i\sigma_1\,d/dy - M\sigma_2 + \kappa k\sigma_3 = -D(M, -k)$, because $\sigma_3\sigma_1\sigma_3 = -\sigma_1$ and $\sigma_3\sigma_2\sigma_3 = -\sigma_2$. Hence $\sigma_3h_j(k)\sigma_3 = h_{-j}(-k)$: the orbital $\sigma_3\chi$ of $(-j, -k)$ has the same level as the orbital $\chi$ of $(j, k)$.

Status: PROVED; check block_type_relation.

### 14.6 The chirality matrix Γ on the blocks, and the rotations of 3-space

**Γ pairs the two types.** The chirality $\Gamma$ is a product of all eight gammas, so it anticommutes with every gamma (Rule 1 with $p = 8$: a factor passes seven others), with every product of an odd number of gammas such as $J$, and commutes with every even product such as $K_1$, $K_2$. If $Jv = jv$, then $J\Gamma v = -\Gamma Jv = -j\,\Gamma v$, while $K_1\Gamma v = \Gamma K_1 v$: so $\Gamma$ maps the block $(j, s_2, s_3)$ onto the block $(-j, s_2, s_3)$. In the block basis its $2 \times 2$ entry between the paired blocks is $s_2\sigma_2$ (computed in Notebook 14a, In [16]; its figure 4 shows where these entries sit). Status: PROVED; check blocks_relation_to_Gamma.

**Γ reverses the mass.** Line by line:

$$
\sigma_2D(M, k)\sigma_2 = i\sigma_1\frac{d}{dy} + M\sigma_2 - \kappa k\sigma_3 = -D(-M, k) .
$$

Rule: $\sigma_2\sigma_1\sigma_2 = -\sigma_1$, $\sigma_2\sigma_2\sigma_2 = \sigma_2$, $\sigma_2\sigma_3\sigma_2 = -\sigma_3$.

$$
\sigma_2h_j(M, k)\sigma_2 = j\big(-D(-M, k)\big) + v = h_{-j}(-M, k) .
$$

Rule: $h_j = jD + v$ and $\sigma_2\sigma_2 = 1$. So if $\chi$ solves the block equation of type $j$ with the mass $M$, then $\sigma_2\chi$ solves the block equation of type $-j$ with the mass $-M$, at the same $k$, the same potential $v$ and the same level $\varepsilon$. Because $\sigma_2(\chi_1, \chi_2) = (-i\chi_2, i\chi_1)$, the map also exchanges the two brane conditions $\chi_2(0) = 0$ and $\chi_1(0) = 0$ of Section 14.12. Status: PROVED; check block_Gamma_map.

The same fact is visible in 16 components without blocks. $\Gamma$ anticommutes with every $\gamma^\mu$ and commutes with every $\Omega_\mu$ (a sum of products of two gammas), so $\gamma^\mu D_\mu(\Gamma\Psi) = -\Gamma\gamma^\mu D_\mu\Psi$. If $\gamma^\mu D_\mu\Psi = (M - iv\gamma^{(x_4)})\Psi$, then

$$
\gamma^\mu D_\mu(\Gamma\Psi) = -\Gamma\big(M - iv\gamma^{(x_4)}\big)\Psi = \big(-M - iv\gamma^{(x_4)}\big)\Gamma\Psi ,
$$

where the last step uses $\Gamma\gamma^{(x_4)} = -\gamma^{(x_4)}\Gamma$. Here $M$ and $v$ are regarded as given functions of $y$. In the full theory they are made by the quanta themselves, and how the parameters $m$, $\lambda$ and the boundary conditions transform is the content of the pairing theorems: T1 for the field equations, which Chapter 18 proves (the chirality MATRIX $\Gamma$ carries the solutions of the Lagrangian with $(m, \lambda)$ to those with $(-m, -\lambda)$), and T3 for the Kohn-Sham states, which Chapter 19 proves. On the blocks, $\sigma_2$ also exchanges the tip condition $b(-L) = 0$ with $a(-L) = 0$ (Section 14.12). The maps of this theory are matrices. The author's gammas are real, so for a real field plain complex conjugation changes nothing and is not a charge conjugation; the charge-conjugation matrices of the theory are $\mathcal C_+ = C$ and $\mathcal C_- = \Gamma C$ (Chapter 5). The map used here is the chirality matrix $\Gamma$ itself, the real matrix map of the theorem T1, which reverses the mass; on the blocks it acts as $s_2\sigma_2$ from the block $(j, s_2, s_3)$ to the block $(-j, s_2, s_3)$.

**What this does and does not say (honesty).** The map $\Gamma$ is an exact map between two sets of solutions: every solution with the mass $M$ has a partner with the mass $-M$. It says nothing about whether a partner is ever realised, and nothing about a process that would create universes, in pairs or otherwise. Chapters 18 to 20 give the complete statements of the pairing theorems T1, T2, Q and T3 and the precise list of what they do not establish.

**Rotations of 3-space.** A rotation by the angle $\theta$ in the $(x_1, x_2)$ plane acts on spinors with the matrix $R = \cos\tfrac\theta2 + \sin\tfrac\theta2\,G$, $G = \gamma^{(x_1)}\gamma^{(x_2)}$. Line by line, with $c = \cos\tfrac\theta2$, $s = \sin\tfrac\theta2$:

$$
G^2 = -1, \qquad (c + sG)(c - sG) = c^2 - s^2G^2 = c^2 + s^2 = 1 .
$$

Rule: Rule 2 with $p = 2$ and $\eta_{11}\eta_{22} = 1$; so $R^{-1} = c - sG$.

$$
\gamma^{(x_1)}G = \gamma^{(x_2)}, \qquad G\gamma^{(x_1)} = -\gamma^{(x_2)}, \qquad R\gamma^{(x_1)} = \gamma^{(x_1)}R^{-1} .
$$

Rule: $\gamma^{(x_1)}\gamma^{(x_1)} = 1$ and $\gamma^{(x_2)}\gamma^{(x_1)} = -\gamma^{(x_1)}\gamma^{(x_2)}$; so $G$ anticommutes with $\gamma^{(x_1)}$, which turns $c + sG$ into $c - sG$ when $\gamma^{(x_1)}$ passes it.

$$
R\gamma^{(x_1)}R^{-1} = \gamma^{(x_1)}(c - sG)^2 = \gamma^{(x_1)}\big(\cos\theta - \sin\theta\,G\big) = \cos\theta\,\gamma^{(x_1)} - \sin\theta\,\gamma^{(x_2)} .
$$

Rule: $(c - sG)^2 = c^2 - s^2 - 2csG$ (with $G^2 = -1$), the double-angle formulas $c^2 - s^2 = \cos\theta$, $2cs = \sin\theta$, and $\gamma^{(x_1)}G = \gamma^{(x_2)}$. So $R$ turns the momentum term $k\gamma^{(x_1)}$ into the same momentum in a rotated direction. And $R$ commutes with $\gamma^{(x_8)}$, $\gamma^{(x_4)}$, $B$ and $C$ (each contains $\gamma^{(x_1)}$ and $\gamma^{(x_2)}$ both or neither, so the signs cancel), so it changes nothing else in $h$. Hence the levels of the whole 16-component problem depend on $|\mathbf k|$ only, and $\mathbf k = (k, 0, 0)$ is no loss of generality. Status: PROVED; check rotation_invariance. (The labels $j$ themselves refer to the direction of $\mathbf k$: a rotation by $\pi$, $R = G$, anticommutes with $J$ and turns the blocks $(j, k)$ into $(-j, -k)$, in agreement with the $\sigma_3$ relation of Section 14.5.)

### 14.7 The exact rescaling identity between the slices

**Where the slice enters.** Look at the block Hamiltonian $h_j$ of Section 14.5. The slice $a_{4,0}$ appears only in the momentum term, through

$$
\kappa k = e^{-Hy - a_{4,0}}\,k = e^{-Hy}\,\big(k\,e^{-a_{4,0}}\big) .
$$

Rule: $e^{u + w} = e^ue^w$. Line by line, what follows:

- At the slice $a_{4,0}$ the allowed momenta are $\Delta k\,\mathbf n$ (Section 14.3). By the line above they act exactly like the momenta $\Delta k\,e^{-a_{4,0}}\,\mathbf n$ at the slice 0. So every level and every orbital of the slice $a_{4,0}$ equals a level and orbital of the slice 0 with the lattice spacing $\Delta k\,e^{-a_{4,0}}$.
- The lattice spacing $\Delta k\,e^{-a_{4,0}}$ belongs to the box size $\ell e^{a_{4,0}}$ (because $\Delta k = 2\pi/\ell$).
- Densities carry the factor $P = e^{-6Hy}/(\ell^3v_t)$ (the orbital is spread over the coordinate volume $\ell^3v_t$ of 3-space and the extra times, and $e^{-6Hy} = 1/\sqrt{|g|}$ turns a density per unit $y$ into a density per unit proper volume). If the partner problem at the slice 0 has the box $\ell e^{a_{4,0}}$ and the extra-time volume $v_te^{-3a_{4,0}}$, its factor is $e^{-6Hy}/(\ell^3e^{3a_{4,0}}v_te^{-3a_{4,0}}) = P$: the same proper densities.
- The interaction enters only through the proper densities (Section 14.26), so self-consistency, the energy and every profile agree as well.

Hence, exactly (for the free gas, with the interaction, at every temperature):

$$
\mathrm{KS}(a_{4,0};\ \Delta k,\ v_t,\ \lambda) = \mathrm{KS}\big(0;\ \Delta k\,e^{-a_{4,0}},\ v_t\,e^{-3a_{4,0}},\ \lambda\big) .
$$

In words: a later slice of the deflating history is the slice 0 with all 3-momenta redshifted by $e^{-a_{4,0}}$ and the same proper box. The proper size of 3-space has grown by $e^{a_{4,0}}$, the proper volume of the extra times has shrunk by $e^{-3a_{4,0}}$, and the proper 7-volume has not changed. Equivalently, keeping the extra-time volume $v_t$, the partner has the coupling $\lambda e^{3a_{4,0}}$ and every proper density multiplied by $e^{-3a_{4,0}}$ (the coupling enters only as $\lambda$ times a density). Status: PROVED; check rescaling_identity. The Rust solver solved each partner problem independently and found the same levels to $1.5\times10^{-13}$ and the same energies and profiles to $3.3\times10^{-13}$ (checks rescaling_identity_between_slices and rescaling_identity_energy_profiles of `Revision/kohn_sham/reports/ks-rust-solver.json`; the partner numbers are in `Revision/kohn_sham/results/rescaling/rescaling.csv`). For the slice $a_{4,0} = 0.5$ the partner has $\Delta k\,e^{-0.5} = 0.151632664928$ and $v_t\,e^{-1.5} = 0.223130160148$ (Notebook 14a, Out [18]).

### 14.8 Example: Notebook 14a, the block reduction and the rescaling identity

Notebook 14a repeats Sections 14.2 to 14.7 with exact computer algebra. It reads the author's gammas from the Revision record, checks the Clifford relation and the matrices $C$, $B$, $\Gamma$, verifies the hidden coordinate and the determinant, computes the canonical spin connection of the warped metric with $a_4$ an arbitrary function of the time and shows that $\sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ with the time-direction pieces cancelling, verifies that $W^{-3}$ removes it, builds the Hamiltonian, the labels $J, K_1, K_2$, the projectors, the block basis (compared entry by entry with the record) and the block forms, checks the two block types, the matrix $\Gamma$ on the blocks, the rotations and the rescaling identity, and compares the partner spacings and volumes with all 60 rows of the Rust record. It draws five figures. It runs in about 30 seconds (two cells do exact algebra with $16 \times 16$ matrices of symbols and take about 10 seconds each), and its last line is ALL 28 CHECKS PASSED (notebook 14a).

<!-- NOTEBOOK 14a -->

### 14.11 Line-by-line walk-through of Notebook 14a

The notebook has 20 code cells, In [1] to In [20]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted, then explained. Docstrings (the texts in triple quotes under a `def` line, which say what a function does) and some comment lines are left out of the quotations; the complete cells are printed in Section 14.10.

**In [1], the set-up cell.** Every line that starts with `#` is a **comment**, which Python skips. The first part of the cell, down to the lines of `-` and `=` signs, is the complete run instructions of Section 14.9 again, as comments, so that the notebook file carries its own instructions. The code starts after the heading THE SET-UP; it computes no physics and is the same in every notebook of the book, except for the line that names the notebook. The notebooks 14b, 14c and 14d have exactly this cell with their own name, and their walk-throughs refer back to this paragraph.

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
NOTEBOOK_ID = "14a"  # this notebook: chapter 14, example a
```

A **variable** is a name for a value; this line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"14a"`. The figure files are named after it.

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
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The comment lines say in short what this paragraph explains. The first statement calls the function and names its result `REPO`. It is never printed, because it differs from computer to computer, while the printed output of a notebook must not. The second line chooses where files are written. `os.environ` holds the **environment variables** of the program (named texts that it receives from the computer); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and the default `str(REPO)` (the repository folder as a string) otherwise. When you run the notebook the variable is not set, so the files go into the repository; the book's checking tool sets it to a scratch folder, so that a check never changes the repository.

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
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: a name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/14a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty JSON dictionary `{}` and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored as bytes, and `newline="\n"` stores the same line end on Windows, macOS and Linux.

```python
def save_figure(fig, name, caption):
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

`setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far: the figures are numbered 1, 2, 3, and a cell that is run twice keeps its number. The file name joins the notebook id, the number and the name, for example `14a_1_hidden_coordinate.png`. `fig.savefig` writes a PNG picture with 150 dots per inch, cuts away the empty margin (`bbox_inches="tight"`) and stores no program name (`metadata`), so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time at the end of the cell. The caption is stored, the whole dictionary is written to the captions file (`json.dumps` turns it into JSON text with sorted keys, one item per line), `display(Image(...))` shows the saved picture below the cell, and the last line prints where it was saved. The caption given to `save_figure` is the caption that the book prints under the figure.

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

`PASSED` is an empty **list** (an ordered collection, written with square brackets). `check` is the function behind every PASS line: if the condition is false, `raise AssertionError(...)` stops the notebook with a message that names the check; otherwise the name is appended to the list and the line PASS and the name is printed. When the check repeats a number or a verdict of the Revision record, the argument `record` names the record file and its check, and a second line starting with `reproduces` is printed. (An `if` statement is used instead of Python's `assert`, because `python -O` would skip an `assert`.)

```python
def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a line that starts with RESULT (the provenance file of the notebook lists these lines). `x if c else y` is the value `x` when `c` is true and `y` otherwise, so the unit is added only when one is given. `all_checks_passed` prints the last line of the notebook with the number of checks that passed; `len` is the length of a list. The last statement prints the only output of the cell, Out [1].

**In [2], the gammas and the Clifford relation.**

```python
import numpy as np  # floating-point arrays and matrices
import sympy as sp  # exact algebra with symbols
```

numpy computes with **floating-point numbers** (numbers with about 16 significant digits, which the computer rounds after every operation); sympy computes **exactly** with whole numbers, fractions and symbols such as $H$. Every identity of this notebook is checked with sympy, so a PASS means an exact identity, not an approximation; numpy is used only for the figures.

```python
PY_REPORT = "Revision/kohn_sham/reports/ks-theory-python.json"
WL_REPORT = "Revision/kohn_sham/reports/ks-theory-wolfram.json"
```

The two reports of the Revision record of the Kohn-Sham theory: the sympy checker and the WolframScript verifier.

```python
def record_check(name):
    verdicts = {}
    for report in (PY_REPORT, WL_REPORT):
        data = json.loads(repository_file(report).read_text(encoding="utf-8"))
        found = [c["verdict"] for c in data["checks"] if c["name"] == name]
        verdicts[report] = found[0] if found else "absent"
    return (verdicts[PY_REPORT] == "PASS"
            and verdicts[WL_REPORT] in ("PASS", "absent"))
```

`record_check(name)` reads both reports (`read_text` reads the file, `json.loads` turns the JSON text into Python lists and dictionaries) and looks for the check called `name` in the list `data["checks"]`. The bracketed expression is a **list comprehension**: it collects `c["verdict"]` for every check `c` whose name matches. If the check is found, its verdict (PASS or FAIL) is kept; otherwise the word absent. The function returns true when the sympy report says PASS and the Wolfram report says PASS or has no check of that name. Every check below that repeats a Revision check uses it, so the notebook passes only if the record itself passed.

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
g = [sp.Matrix(m) for m in fixture["gamma"]]  # g[0] = gamma^(x1) ... g[7] = gamma^(x8)
eta = [int(v) for v in fixture["eta"]]  # +1 space-like, -1 time-like
g1, g2, g3, g4, g5, g6, g7, g8 = g  # gN is gamma^(xN)
I16, Z16 = sp.eye(16), sp.zeros(16)  # the 16 x 16 unit and zero matrices
```

The record `Revision/algebra/gammas.json` stores the eight matrices as lists of rows of whole numbers, in the order $x_1, \dots, x_8$. `sp.Matrix(m)` turns each into an exact sympy matrix; `g[0]` is $\gamma^{(x_1)}$ and `g[7]` is $\gamma^{(x_8)}$ (Python counts from 0). `eta` is the list of the eight signs. The third line gives the eight matrices the names `g1` to `g8` (unpacking a list into names). `sp.eye(16)` is the unit matrix and `sp.zeros(16)` the zero matrix.

```python
say(f"eta in the order x1 ... x8: {eta}")
entries = sorted({int(e) for m in g for e in m})  # the different entries
say(f"the entries of the eight gamma matrices are the integers {entries}")
```

The first line prints the signs. The second collects every entry of every matrix into a **set** (braces without colons: a collection in which each value occurs once) and sorts it; the printout shows that the only entries are $-1$, $0$ and $1$: the gammas are real.

```python
clifford = all(g[a] * g[b] + g[b] * g[a] == (2 * eta[a] if a == b else 0) * I16
               for a in range(8) for b in range(8))
check(clifford and eta == [1, 1, 1, -1, -1, -1, -1, 1]
      and record_check("clifford_relation"),
      "the Clifford relation gamma^a gamma^b + gamma^b gamma^a = 2 eta^ab",
      record=f"{PY_REPORT}, check clifford_relation")
```

`range(8)` runs through 0 to 7, so the two `for` clauses visit all 64 pairs $(a, b)$; `all(...)` is true when every comparison is true. For each pair the anticommutator $\gamma^a\gamma^b + \gamma^b\gamma^a$ (the operator `*` multiplies sympy matrices) is compared exactly with $2\eta^{aa}$ times the unit matrix when $a = b$ and with the zero matrix otherwise. The check also requires the signs $\eta = (+,+,+,-,-,-,-,+)$ and the recorded verdict; Out [2] shows its PASS line and the record it reproduces.

**In [3], the matrices C, B and Γ.**

```python
C = g8 * g1 * g2 * g3  # the matrix of the Dirac adjoint
B = -sp.I * C * g4  # the matrix of the positive inner product
Gamma = g8 * g1 * g2 * g3 * g4 * g5 * g6 * g7  # the chirality matrix
```

The three products of Chapter 5; `sp.I` is the imaginary unit $i$.

```python
check(C.T == C and C * C == I16 and B.H == B and B * B == I16
      and Gamma == sp.diag(*([-1] * 8 + [1] * 8)) and record_check("C_B_Gamma"),
      "C real symmetric with C^2 = 1, B Hermitian with B^2 = 1, Gamma = diag(-1, 1)",
      record=f"{PY_REPORT}, check C_B_Gamma")
```

`C.T` is the transpose and `B.H` the conjugate transpose. `[-1] * 8 + [1] * 8` is the list of eight entries $-1$ followed by eight entries $+1$, and `sp.diag(*...)` the diagonal matrix with these entries (the star hands the list over as separate numbers). So the check says: $C$ is symmetric (it is real because the gammas are) with $C^2 = 1$; $B$ is Hermitian with $B^2 = 1$; $\Gamma = \mathrm{diag}(-1_8, 1_8)$.

```python
check(B * C == -sp.I * g4 and C * g4 == sp.I * B and C * B * C == B
      and record_check("BC_and_Cg4"),
      "BC = -i gamma^(x4), C gamma^(x4) = i B and C B C = B",
      record=f"{PY_REPORT}, check BC_and_Cg4")
```

Three product rules used in Section 14.5 and in Notebook 14d. They follow from the definitions: $C\gamma^{(x_4)} = iB$ is $B = -iC\gamma^{(x_4)}$ multiplied by $i$; $BC = -iC\gamma^{(x_4)}C = -iC C\gamma^{(x_4)} = -i\gamma^{(x_4)}$ because $C$ commutes with $\gamma^{(x_4)}$ (a time-like gamma is not a factor of $C$, and $C$ has four factors) and $C^2 = 1$; and $CBC = C(-i\gamma^{(x_4)}) = -iC\gamma^{(x_4)} = B$.

**In [4], the hidden coordinate and the determinant.**

```python
H = sp.symbols("H", positive=True)  # the author's constant H > 0
y_neg = sp.symbols("y", negative=True)  # the hidden coordinate inside the patch
x8, z = sp.symbols("x8 z", positive=True)
```

`sp.symbols` makes symbols; the options tell sympy what it may assume: $H > 0$, $y < 0$ (inside the patch), $x_8 > 0$ and $z > 0$. With these assumptions sympy can simplify square roots and inverse sines correctly.

```python
z_of_y = sp.asin(sp.exp(6 * H * y_neg))  # z(y): the solution of sin z = e^(6Hy)
dx8_dy = sp.diff(z_of_y / (6 * H), y_neg)  # x8 = z/(6H) differentiated in y
ok_line = sp.simplify(sp.cot(z_of_y) ** 2 * dx8_dy ** 2 - 1) == 0  # g88 dx8^2 = dy^2
```

The first line solves $\sin z = e^{6Hy}$ for $z$ with the inverse sine, `sp.asin`. The second differentiates $x_8 = z/(6H)$ with respect to $y$ (`sp.diff(expression, variable)`). The third checks step 2 of Section 14.2 in the form $\cot^2 z\,(dx_8/dy)^2 = 1$, which is $\cot^2z\,dx_8^2 = dy^2$: `sp.simplify` brings the expression to its simplest form, and the comparison `== 0` asks whether it is exactly zero.

```python
ok_warp = sp.simplify(sp.sin(z_of_y) ** sp.Rational(1, 3)
                      - sp.exp(2 * H * y_neg)) == 0  # sin^(1/3) z = e^(2Hy)
ok_dy = sp.simplify(sp.diff(sp.log(sp.sin(6 * H * x8)) / (6 * H), x8)
                    - sp.cot(6 * H * x8)) == 0  # dy/dx8 = cot z
check(ok_line and ok_warp and ok_dy and record_check("geometry_hidden_coordinate"),
      "y = ln(sin z)/(6H): dy = cot z dx8 and sin^(1/3) z = e^(2Hy)",
      record=f"{PY_REPORT}, check geometry_hidden_coordinate")
```

`sp.Rational(1, 3)` is the exact fraction $1/3$ (the Python expression `1/3` would be a rounded floating-point number). The first test is step 3 of Section 14.2, $\sin^{1/3}z = e^{2Hy}$; the second is step 1, $dy/dx_8 = \cot z$, differentiating the definition $y = \ln(\sin 6Hx_8)/(6H)$ directly. The check combines the three tests.

```python
a0 = sp.symbols("a0", real=True)  # the value of a4 at one slice
third = sp.Rational(1, 3)
metric_x8 = ([sp.exp(2 * a0) * sp.sin(z) ** third] * 3 + [-1]
             + [-sp.exp(-2 * a0) * sp.sin(z) ** third] * 3 + [sp.cot(z) ** 2])
det_x8 = sp.simplify(sp.Abs(sp.prod(metric_x8)))  # |det g| in the x8 chart
say(f"|det g| in the x8 chart of the author = {det_x8}")
check(sp.simplify(det_x8 - sp.cos(z) ** 2) == 0 and record_check("geometry_sqrt_det"),
      "|det g| = cos^2 z in the x8 chart; it does not contain a4",
      record=f"{PY_REPORT}, check geometry_sqrt_det")
```

`metric_x8` is the list of the eight diagonal entries of the author's metric in his $x_8$ chart (a list times 3 repeats it three times; `+` joins lists). The determinant of a diagonal matrix is the product of its diagonal entries (`sp.prod`), and `sp.Abs` takes its absolute value. sympy prints `cos(z)**2` (Out [4]; `**` is the power): the cubes of the 3-space and extra-time entries give $e^{6a_0}\sin z$ and $-e^{-6a_0}\sin z$, the factors $e^{6a_0}$ and $e^{-6a_0}$ cancel, the signs $(-1)(-1) = 1$, and $\sin z\cdot\sin z\cdot\cot^2 z = \cos^2 z$. The square root is $\cos z$, as Section 14.2 says.

**In [5], figure 1.**

```python
z_values = np.linspace(1e-3, np.pi / 2, 600)  # z from almost 0 to pi/2
y_of_z = np.log(np.sin(z_values)) / 6.0  # y = ln(sin z)/(6H) with H = 1
y_values = np.linspace(-3.0, 0.0, 301)  # the hidden coordinate from -L to 0
```

`np.linspace(start, stop, count)` makes `count` equally spaced numbers from `start` to `stop`; `1e-3` means $10^{-3}$ (the value $z = 0$ itself would give $\ln 0$). numpy applies `np.log` and `np.sin` to every number of an array at once. The third line is the hidden coordinate from the cutoff $-L = -3$ of the Revision solver to the brane.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(z_values, y_of_z, color="C0")
left.set_xlabel("$z = 6 H x_8$ (radians)")
left.set_ylabel("$y = \\ln(\\sin z)/(6H)$")
left.set_title("the hidden coordinate $y$ ($H = 1$)")
left.annotate("tip: $y \\to -\\infty$", (0.03, -1.0), fontsize=9)
left.annotate("brane: $y = 0$", (1.05, -0.15), fontsize=9)
```

`plt.subplots(1, 2, ...)` makes a figure with one row of two panels (called **axes** in matplotlib), named `left` and `right`, 10 by 4 inches. `plot(x, y)` draws a curve; `"C0"` is the first colour of matplotlib's standard list. The labels are written in LaTeX between dollar signs, with a doubled backslash because a single backslash starts a special character in a Python string. `annotate(text, (x, y))` writes a text at a point of the panel.

```python
right.semilogy(y_values, np.exp(y_values), label="warp $W = e^{Hy}$")
right.semilogy(y_values, np.exp(2 * y_values), "--",
               label="$\\sin^{1/3} z = W^2$")
right.semilogy(y_values, np.exp(6 * y_values), ":",
               label="volume factor $\\sqrt{|g|} = W^6$")
right.set_xlabel("$y$ (units of $1/H$)")
right.set_ylabel("factor (logarithmic scale)")
right.set_title("the factors of the warped metric")
right.legend(fontsize=8)
```

`semilogy` draws with a **logarithmic vertical axis**: equal distances mean equal factors (each tick is ten times the one below). On such an axis an exponential $e^{cy}$ is a straight line of slope $c$. The three curves are $W$, $W^2$ and $W^6$ with $H = 1$; the third argument of `semilogy`, a short text called a **format string**, sets the line style: two hyphens draw a dashed line and a colon a dotted one (the plain `plot` lines of this book use the same format strings); `legend` shows the `label` texts in a box.

```python
save_figure(fig, "hidden_coordinate",
            "Left: the hidden coordinate $y = \\ln(\\sin z)/(6H)$ against "
            ...)
```

The figure is saved as `14a_1_hidden_coordinate.png` with its caption (the long caption, printed under the figure in Section 14.10, is shortened here to `...`). **What figure 14a.1 shows.** Left: $y$ against $z$; the curve drops steeply to minus infinity as $z \to 0$ (the tip; the plot stops at $z = 10^{-3}$, $y = -1.15$) and approaches 0 with zero slope at the brane $z = \pi/2$ (because $dy/dz = \cot z/(6H)$ vanishes there). Right: the three straight lines with slopes 1, 2 and 6 on the logarithmic axis; all equal 1 at the brane, and at the cutoff $y = -3$ the volume factor is $e^{-18} \approx 1.5\times10^{-8}$. This small proper volume near the tip is why the proper densities of Notebook 14d become large there.

**In [6], figure 2.**

```python
a4_values = np.linspace(0.0, 2.0, 201)  # a4 along the history (= x4 for A = H = 1)
slices = [0.0, 0.5, 1.0, 1.5, 2.0]  # the five slices of the Revision solver
```

The values of $a_4$ from 0 to 2 (along the history $a_4 = AHx_4$ with $A = H = 1$ these are also the times $x_4$), and the five slices of the Revision runs.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(a4_values, np.exp(a4_values), label="3-space: $e^{a_4}$ (inflates)")
left.plot(a4_values, np.exp(-a4_values), "--",
          label="extra times: $e^{-a_4}$ (deflates)")
left.plot(a4_values, np.exp(3 * a4_values) * np.exp(-3 * a4_values), ":",
          color="black", label="7-volume: $e^{3a_4} e^{-3a_4} = 1$")
left.set_xlabel("$a_4 = A H x_4$ (with $A = H = 1$: the time $x_4$)")
left.set_ylabel("scale factor at the brane $y = 0$")
left.set_title("inflation and deflation along the history")
left.legend(fontsize=8)
```

The left panel draws the 3-space scale factor $e^{a_4}$, the extra-time scale factor $e^{-a_4}$ and the product of their cubes, all at the brane where $W = 1$.

```python
for a in slices:  # one curve per slice
    right.semilogy(y_values, np.exp(-y_values - a), label=f"$a_{{4,0}} = {a}$")
right.set_xlabel("$y$ (units of $1/H$)")
right.set_ylabel("$\\kappa = e^{-Hy - a_{4,0}}$ (logarithmic)")
right.set_title("the momentum weight at five slices")
right.legend(fontsize=8)
save_figure(fig, "inflation_deflation",
            ...)
```

The loop draws the momentum weight $\kappa = e^{-y - a}$ ($H = 1$) for each slice $a$; in an f-string a doubled brace `{{` prints one brace, so the label reads $a_{4,0} = 0.5$ and so on. **What figure 14a.2 shows.** Left: $e^{a_4}$ grows to $e^2 \approx 7.4$, $e^{-a_4}$ falls to $e^{-2} \approx 0.14$, and the dotted line stays at 1: inflation of 3-space and deflation of the extra times exactly balance in the volume. Right: five parallel straight lines falling from left to right: $\kappa$ is largest at the tip ($e^3 \approx 20$ at $y = -3$ for the slice 0), and each later slice lies lower by the factor $e^{-0.5}$: the same coordinate momentum costs less energy as 3-space inflates.

**In [7], the spin connection.** This cell carries out Steps 1 to 3 of Section 14.4 with sympy.

```python
X = sp.symbols("x1:8", real=True) + (sp.Symbol("y", real=True),)  # x1..x7 and y
Y, x4 = X[7], X[3]  # the hidden coordinate and the time
a4 = sp.Function("a4", real=True)(x4)  # a4 is any function of the time x4
a4p = sp.diff(a4, x4)  # its derivative a4'
```

`sp.symbols("x1:8")` makes the seven symbols $x_1, \dots, x_7$; adding a one-element **tuple** (a list in round brackets) with the symbol $y$ gives the eight coordinates, with $y$ in the place of $x_8$. `sp.Function("a4")(x4)` is an unknown function $a_4(x_4)$, so everything below holds along every history; `a4p` is its derivative $a_4'$.

```python
W = sp.exp(H * Y)  # the warp factor
vb = [sp.exp(a4) * W] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * W] * 3 + [sp.Integer(1)]
gdiag = [eta[i] * vb[i] ** 2 for i in range(8)]  # the diagonal metric entries
```

`vb` is the list of the eight scale factors $h$ of Section 14.2 (`sp.Integer(1)` is the exact number 1), and `gdiag` the metric entries $\eta_{ii}h_i^2$, which reproduce the warped form.

```python
def christoffel(n, m, k):
    total = 0
    if m == n:
        total += sp.diff(gdiag[n], X[k])
    if k == n:
        total += sp.diff(gdiag[n], X[m])
    if m == k:
        total -= sp.diff(gdiag[m], X[n])
    return sp.simplify(total / (2 * gdiag[n]))
```

Step 1 of Section 14.4, the formula for $\Gamma^n{}_{mk}$ of a diagonal metric: each `if` adds one of the three terms when its Kronecker delta is 1 (`+=` adds to a variable, `-=` subtracts).

```python
Chr = [[[christoffel(n, m, k) for k in range(8)] for m in range(8)]
       for n in range(8)]
S = [[(g[a] * g[b] - g[b] * g[a]) / 4 for b in range(8)] for a in range(8)]
```

`Chr[n][m][k]` holds all $8^3 = 512$ Christoffel symbols, and `S[a][b]` the 64 generators $S^{ab} = \tfrac14(\gamma^a\gamma^b - \gamma^b\gamma^a)$.

```python
Omega = []  # Omega[mu] is the 16 x 16 matrix Omega_mu
for mu in range(8):
    total = sp.zeros(16)
    for A in range(8):
        for Bi in range(8):
            w = (vb[A] * sp.diff(1 / vb[Bi], X[mu]) if A == Bi else 0) \
                + vb[A] * Chr[A][mu][Bi] / vb[Bi]  # omega_mu^A_B (step 2)
            w = sp.simplify(w)
            if w != 0:
                total += sp.Rational(1, 2) * eta[A] * w * S[A][Bi]  # step 3
    Omega.append(sp.simplify(total))
```

For each direction $\mu$ the double loop over the frame indices $A$ and $B$ (`Bi`, because `B` is the matrix $B$) computes the connection coefficient $\omega_\mu{}^A{}_B$ of Step 2 (a backslash at the end of a line continues the statement on the next line) and adds $\tfrac12\eta_{AA}\,\omega_\mu{}^A{}_B\,S^{AB}$ to the matrix $\Omega_\mu$ (Step 3); terms with a zero coefficient are skipped to save time. `append` puts the finished $\Omega_\mu$ at the end of the list.

```python
compatible = all(
    (sp.diff(g[n] / vb[n], X[m])
     + sum((Chr[n][m][l] * g[l] / vb[l] for l in range(8)), Z16)
     + Omega[m] * g[n] / vb[n] - g[n] / vb[n] * Omega[m]).applyfunc(sp.simplify)
    .is_zero_matrix for m in range(8) for n in range(8))
check(compatible and record_check("spin_connection_compatibility"),
      "the curved gammas are covariantly constant (64 matrix equations)",
      record=f"{PY_REPORT}, check spin_connection_compatibility")
```

The proof that $\Omega_\mu$ is the right connection: the **curved gammas** $\gamma^\nu = \gamma^{(\nu)}/h_\nu$ must be **covariantly constant**, $\partial_\mu\gamma^\nu + \Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$, for all 64 pairs $(\mu, \nu)$, where $[X, Y] = XY - YX$ is the **commutator**. `sum(..., Z16)` adds sixteen-by-sixteen matrices starting from the zero matrix; `applyfunc(sp.simplify)` simplifies every entry; `.is_zero_matrix` is true when every entry is 0.

```python
slash = sp.simplify(sum((g[m] / vb[m] * Omega[m] for m in range(8)), Z16))
check((slash - 3 * H * g8).is_zero_matrix and record_check("spin_connection_slash_3H"),
      "gamma^mu Omega_mu = 3H gamma^(x8) exactly, for every history a4(x4)",
      record=f"{PY_REPORT}, check spin_connection_slash_3H")
```

The sum $\sum_\mu\gamma^\mu\Omega_\mu$ (often written with a slash through $\Omega$, hence the name), compared with $3H\gamma^{(x_8)}$. Out [7] shows the two PASS lines.

**In [8], where 3Hγ(x8) comes from.**

```python
names = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8 (y)"]
PRIME = sp.Symbol("da4dx4")  # a name for the derivative da4/dx4 in the printout
c4_list, c8_list = [], []  # the coefficients of gamma^(x4) and gamma^(x8)
split_ok = True
```

Names for the printout, a symbol that stands for $a_4'$ when it is printed, two empty lists and a flag that starts true.

```python
for m in range(8):
    part = sp.simplify(g[m] / vb[m] * Omega[m])  # the contribution of direction m
    c4 = sp.simplify(-(part * g4).trace() / 16)
    c8 = sp.simplify((part * g8).trace() / 16)
    split_ok &= (part - c4 * g4 - c8 * g8).applyfunc(sp.simplify).is_zero_matrix
    c4_list.append(c4)
    c8_list.append(c8)
    shown_c4 = str(c4.subs(a4p, PRIME))  # write da4dx4 for da4/dx4
    say(f"direction {names[m]:7}: c4 = {shown_c4:12} c8 = {c8}")
check(split_ok, "every contribution is c4 gamma^(x4) + c8 gamma^(x8)")
```

For each direction the contribution $X = (\gamma^{(\mu)}/h_\mu)\Omega_\mu$ of Step 4. If $X = c_4\gamma^{(x_4)} + c_8\gamma^{(x_8)}$, then $X\gamma^{(x_4)} = -c_4 + c_8\gamma^{(x_8)}\gamma^{(x_4)}$, and since the **trace** (the sum of the diagonal entries) of the unit matrix is 16 and that of a product of two different gammas is 0, $\mathrm{tr}(X\gamma^{(x_4)}) = -16c_4$; in the same way $\mathrm{tr}(X\gamma^{(x_8)}) = 16c_8$. These are the second and third lines. The fourth line checks that $X$ is exactly $c_4\gamma^{(x_4)} + c_8\gamma^{(x_8)}$ (`&=` keeps the flag true only if every direction passes). `subs(a4p, PRIME)` replaces the derivative by the printable name, and the format `:7` and `:12` pads the texts to 7 and 12 characters, so that the printout forms columns. Out [8] shows $c_4 = a_4'/2$ and $c_8 = H/2$ for $x_1, x_2, x_3$; $c_4 = 0$, $c_8 = 0$ for $x_4$ and for $y$; $c_4 = -a_4'/2$ and $c_8 = H/2$ for $x_5, x_6, x_7$: exactly Step 5 of Section 14.4.

```python
inflating = sp.simplify(sum(c4_list[0:3]))  # x1, x2, x3
deflating = sp.simplify(sum(c4_list[4:7]))  # x5, x6, x7
say("sum of c4 over the inflating directions x1, x2, x3: "
    f"{inflating.subs(a4p, PRIME)}")
say("sum of c4 over the deflating directions x5, x6, x7: "
    f"{deflating.subs(a4p, PRIME)}")
say(f"sum of c8 over all directions: {sp.simplify(sum(c8_list))}")
```

`c4_list[0:3]` is the part of the list from position 0 up to, but not including, position 3 (the directions $x_1, x_2, x_3$), and `c4_list[4:7]` the positions 4 to 6 ($x_5, x_6, x_7$). The printout: $3a_4'/2$, $-3a_4'/2$ and $3H$.

```python
check(sp.simplify(inflating - sp.Rational(3, 2) * a4p) == 0
      and sp.simplify(deflating + sp.Rational(3, 2) * a4p) == 0
      and Omega[3].is_zero_matrix and Omega[7].is_zero_matrix
      and record_check("spin_connection_time_terms_cancel")
      and record_check("spin_connection_time_term_value"),
      "the da4/dx4 pieces +3/2 and -3/2 cancel; Omega_x4 = Omega_y = 0",
      record=f"{PY_REPORT}, checks spin_connection_time_terms_cancel and "
             "spin_connection_time_term_value")
```

The two facts of the record: the pieces $+\tfrac32a_4'$ of the inflating and $-\tfrac32a_4'$ of the deflating directions, and $\Omega_{x_4} = \Omega_y = 0$ (positions 3 and 7 of the list).

**In [9], figure 3.**

```python
c4_numbers = [float(c.subs(a4p, 1).subs(H, 1)) for c in c4_list]  # da4/dx4 = H = 1
c8_numbers = [float(c.subs(a4p, 1).subs(H, 1)) for c in c8_list]
positions = np.arange(8)  # one group of two bars per direction
```

The coefficients become ordinary numbers by putting $a_4' = 1$ and $H = 1$ (`float` turns an exact number into a floating-point one); `np.arange(8)` is the array 0, 1, ..., 7, one position per direction.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.0))
ax.bar(positions - 0.2, c4_numbers, width=0.38,
       label="coefficient of $\\gamma^{(x_4)}$ (per unit $da_4/dx_4$)")
ax.bar(positions + 0.2, c8_numbers, width=0.38,
       label="coefficient of $\\gamma^{(x_8)}$ (per unit $H$)")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xticks(positions)
ax.set_xticklabels(["$x_1$", "$x_2$", "$x_3$", "$x_4$", "$x_5$", "$x_6$", "$x_7$",
                    "$x_8$"])
```

`bar(x, heights, width=...)` draws bars; the two sets are shifted by $-0.2$ and $+0.2$ so that they stand side by side. `axhline` draws the horizontal line at 0; `set_xticks` and `set_xticklabels` put the names of the directions under the groups.

```python
ax.set_xlabel("direction $\\mu$ of the term $(\\gamma^{(\\mu)}/h_\\mu)\\,"
              "\\Omega_\\mu$")
ax.set_ylabel("coefficient")
ax.set_title("$\\gamma^\\mu\\Omega_\\mu = 3H\\gamma^{(x_8)}$: "
             "the $da_4/dx_4$ pieces cancel")
ax.legend(fontsize=8)
save_figure(fig, "spin_connection_terms",
            ...)
```

Labels, title, legend and saving. **What figure 14a.3 shows.** Above $x_1$, $x_2$, $x_3$ two bars of height $+\tfrac12$; above $x_5$, $x_6$, $x_7$ a bar of height $-\tfrac12$ (the coefficient of $\gamma^{(x_4)}$) and one of $+\tfrac12$ (the coefficient of $\gamma^{(x_8)}$); nothing above $x_4$ and $x_8$. The six left bars of the $\gamma^{(x_4)}$ coefficient add to zero (inflation against deflation), the six bars of the $\gamma^{(x_8)}$ coefficient add to $3H$.

**In [10], the factor W^(-3).**

```python
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)  # the 3-momentum
chi = sp.Matrix([sp.Function(f"chi{i}")(Y, x4) for i in range(16)])
phase = sp.exp(sp.I * (k1 * X[0] + k2 * X[1] + k3 * X[2]))  # the plane wave
kappa = sp.exp(-H * Y - a4)  # the momentum weight
```

The three components of $\mathbf k$; a column `chi` of 16 unknown functions $\chi_0(y, x_4), \dots, \chi_{15}(y, x_4)$; the plane wave $e^{i\mathbf k\cdot\mathbf x}$; and the weight $\kappa = e^{-Hy - a_4(x_4)}$.

```python
def dirac(Psi):
    result = sp.zeros(16, 1)
    for m in range(8):
        result += g[m] / vb[m] * (sp.diff(Psi, X[m]) + Omega[m] * Psi)
    return result
```

The Dirac operator $\gamma^\mu D_\mu\Psi = \sum_\mu(\gamma^{(\mu)}/h_\mu)(\partial_\mu\Psi + \Omega_\mu\Psi)$ with the spin connection of In [7]; `sp.zeros(16, 1)` is a zero column.

```python
reduced = (g8 * sp.diff(chi, Y) + g4 * sp.diff(chi, x4)
           + sp.I * kappa * (k1 * g1 + k2 * g2 + k3 * g3) * chi)
with_W3 = sp.simplify(dirac(phase * W ** -3 * chi) / (phase * W ** -3))
without_W3 = sp.simplify(dirac(phase * chi) / phase)
```

`reduced` is the operator of Step 6 of Section 14.4 applied to $\chi$. `with_W3` applies the full Dirac operator to $e^{i\mathbf k\cdot\mathbf x}W^{-3}\chi$ and divides by the common factor; `without_W3` does the same without $W^{-3}$.

```python
check((with_W3 - reduced).applyfunc(sp.simplify).is_zero_matrix
      and record_check("ansatz_removes_spin_connection"),
      "with W^(-3): the reduced operator g8 d_y + g4 d_x4 + i kappa k.g, exactly",
      record=f"{PY_REPORT}, check ansatz_removes_spin_connection")
check((without_W3 - reduced - 3 * H * g8 * chi).applyfunc(sp.simplify)
      .is_zero_matrix and record_check("ansatz_without_W3_term_survives"),
      "without W^(-3) the term 3H gamma^(x8) chi survives",
      record=f"{PY_REPORT}, check ansatz_without_W3_term_survives")
```

With the factor the result equals the reduced operator exactly; without it, the difference is exactly $3H\gamma^{(x_8)}\chi$. The cell takes about 5 seconds.

**In [11], the Hamiltonian and its Hermitian pieces.**

```python
M, v = sp.symbols("M v", real=True)  # effective mass and vector potential
chi_s = sp.Matrix(sp.symbols("c0:16"))  # chi at one point (16 symbols)
dchi_s = sp.Matrix(sp.symbols("d0:16"))  # d chi/dy at that point
kap = sp.symbols("kappa", positive=True)
kg = kap * (k1 * g1 + k2 * g2 + k3 * g3)  # kappa k.gamma
```

The derivation of Step 7 is pure algebra at one point, so $\chi$ and $\chi'$ are replaced by two columns of 16 independent symbols, and $\kappa$ by a positive symbol.

```python
# line 1 and 2: d chi/dx4 = -g4 [(M - i v g4) chi - g8 chi' - i kappa k.g chi]
dt_chi = -g4 * ((M * I16 - sp.I * v * g4) * chi_s - g8 * dchi_s - sp.I * kg * chi_s)
# line 3: h chi with the four pieces of h
h_chi = (sp.I * g4 * g8 * dchi_s - kap * g4 * (k1 * g1 + k2 * g2 + k3 * g3) * chi_s
         + M * (-sp.I * g4) * chi_s + v * chi_s)
check((sp.I * dt_chi - h_chi).expand().is_zero_matrix,
      "i d_x4 chi = h chi with h = i g4 g8 d_y - kappa k_j g4 g_j + M(-i g4) + v")
```

The two comment lines name the lines of Step 7 that the statement below each writes out. `dt_chi` is $\partial_{x_4}\chi$ from the first two lines of Step 7 (move the terms, multiply by $-\gamma^{(x_4)}$); `h_chi` is $h\chi$ with the four pieces of the third line. The check confirms $i\,\partial_{x_4}\chi = h\chi$ after multiplying out (`expand`).

```python
hermitian = ((g4 * g8).T == g4 * g8 and all((-g4 * gj).H == -g4 * gj
                                            for gj in (g1, g2, g3))
             and (-sp.I * g4).H == -sp.I * g4 and (-sp.I * g4) ** 2 == I16)
check(hermitian and record_check("hamiltonian_16_hermitian"),
      "g4 g8 real symmetric; g4 g_j and -i g4 Hermitian; (-i g4)^2 = 1",
      record=f"{PY_REPORT}, check hamiltonian_16_hermitian")
```

The Hermitian pieces of Section 14.4: $\gamma^{(x_4)}\gamma^{(x_8)}$ symmetric, $-\gamma^{(x_4)}\gamma^{(x_j)}$ Hermitian for the three 3-space directions, $-i\gamma^{(x_4)}$ Hermitian with square 1.

**In [12], the labels J, K1, K2 and the projectors.**

```python
A0, A1, A4 = g8, g8 * g1, g8 * g4  # the matrices of the equation (k along x1)
J, K1, K2 = g8 * g1 * g4, g2 * g3, g5 * g6
commute = all((P * Q - Q * P).is_zero_matrix for P in (J, K1, K2)
              for Q in (A0, A1, A4, B, C, J, K1, K2))
check(commute and J * J == I16 and K1 * K1 == -I16 and K2 * K2 == -I16
      and record_check("blocks_commuting_set"),
      "J, K1, K2 commute with A0, A1, A4, B, C and each other; J^2 = 1, K^2 = -1",
      record=f"{PY_REPORT}, check blocks_commuting_set")
```

The matrices of Section 14.5; `commute` tests the 24 commutators of each of $J$, $K_1$, $K_2$ with each of $A_0$, $A_1$, $A_4$, $B$, $C$, $J$, $K_1$, $K_2$; the check adds the three squares.

```python
labels = [(j, s2, s3) for j in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]
projectors = [(I16 + j * J) / 2 * (I16 - sp.I * s2 * K1) / 2
              * (I16 - sp.I * s3 * K2) / 2 for (j, s2, s3) in labels]
check(all(P.rank() == 2 and (P * P - P).is_zero_matrix for P in projectors)
      and sum(projectors, Z16) == I16 and record_check("blocks_projectors"),
      "eight projectors P(j, s2, s3) of rank 2 that add up to 1",
      record=f"{PY_REPORT}, check blocks_projectors")
```

`labels` lists the eight triples in the order of the record, $(1,1,1), (1,1,-1), \dots, (-1,-1,-1)$. `projectors` builds $P(j, s_2, s_3)$ for each. The check: each has `rank()` 2 and $P^2 = P$, and the eight add up to the unit matrix.

**In [13], the block basis.**

```python
columns, seeds = [], []
for P in projectors:
    P_plus = P * (I16 + g8) / 2  # project on gamma^(x8) = +1 inside the block
    c = next(c for c in range(16) if not P_plus[:, c].is_zero_matrix)
    seeds.append(c)
    v_plus = 8 * P_plus[:, c]
    columns += [v_plus, A1 * v_plus]  # v+ and v- = A1 v+
```

For each block: `P_plus` projects onto the block and onto $\gamma^{(x_8)} = +1$. Its columns are the images of the unit columns $e_c$ (`P_plus[:, c]` is column $c$). `next(...)` returns the first $c$ whose column is not zero, the **seed**. Then $v_+ = 8\,P_+e_c$, and both $v_+$ and $v_- = A_1v_+$ are added to the list (`+=` appends a list to a list).

```python
U = sp.Matrix.hstack(*columns)  # 16 x 16, entries 0, +-1, +-i
V = U / (2 * sp.sqrt(2))  # the unitary block basis
say(f"seed columns c of the eight blocks: {seeds}")
```

`hstack` places the 16 columns side by side into the matrix $U$; $V = U/(2\sqrt2)$. Out [13] prints the seeds 4, 0, 0, 4, 0, 4, 4, 0.

```python
theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                    .read_text(encoding="utf-8"))
as_number = {"0": 0, "1": 1, "-1": -1, "I": sp.I, "-I": -sp.I}
U_record = sp.Matrix([[as_number[e] for e in row] for row in
                      theory["blockBasis"]["unnormalisedColumns2Sqrt2V"]])
```

The record stores $U$ row by row as texts such as `"I"` and `"-1"`; the dictionary `as_number` turns each text into the exact number, and `U_record` is the recorded matrix.

```python
check(sp.simplify(V.H * V) == I16 and set(U) <= {0, 1, -1, sp.I, -sp.I}
      and seeds == theory["blockBasis"]["seedColumns0Based"]
      and record_check("blocks_basis_unitary"),
      "V = U/(2 sqrt 2) is unitary, U has entries 0, +-1, +-i",
      record=f"{PY_REPORT}, check blocks_basis_unitary")
check(U == U_record,
      "U equals the basis of the Revision record entry by entry",
      record="Revision/kohn_sham/ks-theory.json, blockBasis.unnormalisedColumns2Sqrt2V")
```

The first check: $V^\dagger V = 1$, the set of entries of $U$ is contained in (`<=`) the set $\{0, \pm1, \pm i\}$, and the seeds equal the recorded ones. The second: $U$ equals the recorded matrix in all 256 entries. This is the basis the Rust solver uses.

**In [14], the block forms.**

```python
s1 = sp.Matrix([[0, 1], [1, 0]])  # the Pauli matrices
s2m = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)
```

The Pauli matrices (`s2m` is $\sigma_2$; the name `s2` is used for the label $s_2$) and the $2 \times 2$ unit matrix.

```python
def blocks_of(Xm):
    Yb = sp.simplify(V.H * Xm * V)
    diagonal = [Yb[2 * b:2 * b + 2, 2 * b:2 * b + 2] for b in range(8)]
    rebuilt = sp.zeros(16)
    for b in range(8):
        rebuilt[2 * b:2 * b + 2, 2 * b:2 * b + 2] = diagonal[b]
    return diagonal, rebuilt == Yb
```

`blocks_of(X)` changes $X$ to the block basis, $V^\dagger XV$, cuts out the eight $2 \times 2$ blocks on the diagonal (rows and columns $2b$ and $2b + 1$ of block $b$), rebuilds a matrix from these blocks alone, and returns the blocks and whether the rebuilt matrix equals $V^\dagger XV$, that is, whether $X$ is block diagonal.

```python
expected = [  # (name, matrix, the block form as a function of (j, s2, s3))
    ("gamma^(x8)", g8, lambda j, a, b: s3, "sigma3"),
    ("gamma^(x8) gamma^(x1)", A1, lambda j, a, b: -sp.I * s2m, "-i sigma2"),
    ("gamma^(x8) gamma^(x4)", A4, lambda j, a, b: j * s1, "j sigma1"),
    ("B", B, lambda j, a, b: j * a * I2, "j s2"),
    ("C", C, lambda j, a, b: a * s2m, "s2 sigma2"),
    ("BC = -i gamma^(x4)", B * C, lambda j, a, b: j * s2m, "j sigma2"),
    ("gamma^(x4) gamma^(x1)", g4 * g1, lambda j, a, b: -j * s3, "-j sigma3"),
    ("B gamma^(x8)", B * g8, lambda j, a, b: j * a * s3, "j s2 sigma3"),
    ("J", J, lambda j, a, b: j * I2, "j"),
    ("K1", K1, lambda j, a, b: sp.I * a * I2, "i s2"),
    ("K2", K2, lambda j, a, b: sp.I * b * I2, "i s3"),
]
```

A list of eleven entries, one per line: the name, the matrix, its expected block form and the text to print. A `lambda` is a short nameless function: `lambda j, a, b: j * s1` returns $j\sigma_1$ for the labels $(j, s_2, s_3) = (j, a, b)$; so the name `a` stands for $s_2$ and `b` for $s_3$ inside these lines (they are not the real-form components of Section 14.12). Line by line the expected forms are: $\gamma^{(x_8)} \to \sigma_3$; $A_1 \to -i\sigma_2$; $A_4 \to j\sigma_1$; $B \to js_2$ times the $2 \times 2$ unit matrix `I2`; $C \to s_2\sigma_2$; $BC \to j\sigma_2$; $\gamma^{(x_4)}\gamma^{(x_1)} \to -j\sigma_3$; $B\gamma^{(x_8)} \to js_2\sigma_3$; $J \to j$; $K_1 \to is_2$; $K_2 \to is_3$. These are the eleven forms of Section 14.5; the two not derived there follow from them: $BC = (js_2)(s_2\sigma_2) = j\sigma_2$ because $s_2^2 = 1$, and $B\gamma^{(x_8)} = (js_2)\sigma_3$.

```python
all_forms = True
for name, Xm, form, text in expected:
    diagonal, only_diagonal = blocks_of(Xm)
    ok = only_diagonal and all(diagonal[i] == form(*labels[i]) for i in range(8))
    all_forms &= ok
    say(f"{name:24} -> {text:12} in block (j, s2, s3): {ok}")
check(all_forms and record_check("blocks_forms"),
      "all eleven matrices are block diagonal with the forms of the record",
      record=f"{PY_REPORT}, check blocks_forms")
```

For each matrix: block diagonal, and in block $i$ equal to the expected form at the labels of that block. Out [14] prints True for all eleven.

```python
not_diagonal = (not blocks_of(g2)[1] and not blocks_of(g5)[1]
                and not blocks_of(g8 * g2)[1] and blocks_of(g1)[1])
check(not_diagonal and record_check("blocks_not_everything_block_diagonal"),
      "gamma^(x2), gamma^(x5), gamma^(x8)gamma^(x2) connect blocks; gamma^(x1) not",
      record=f"{PY_REPORT}, check blocks_not_everything_block_diagonal")
```

`blocks_of(X)[1]` is the second returned value, the yes-or-no answer. $\gamma^{(x_2)}$, $\gamma^{(x_5)}$ and $\gamma^{(x_8)}\gamma^{(x_2)}$ are not block diagonal; $\gamma^{(x_1)}$ is.

**In [15], figure 4.**

```python
N16 = (1 * g8 + sp.I * sp.Rational(1, 2) * g8 * g4
       - sp.I * sp.Rational(7, 10) * g8 * g1)  # M = 1, eps = 1/2, v = 0, kappa k = 7/10
```

The first-order matrix of the stationary equation in 16 components, $N_{16} = M\gamma^{(x_8)} + i(\varepsilon - v)\gamma^{(x_8)}\gamma^{(x_4)} - i\kappa k\,\gamma^{(x_8)}\gamma^{(x_1)}$ (from Step 7 of Section 14.4 with $\partial_{x_4}\chi = -i\varepsilon\chi$, multiplied by $\gamma^{(x_8)}$), at sample values. With the block forms it becomes $N = M\sigma_3 - \kappa k\sigma_2 + ij(\varepsilon - v)\sigma_1$ in every block.

```python
pictures = [
    (np.abs(np.array(N16.evalf(), dtype=complex)), "$|N_{16}|$, original basis"),
    (np.abs(np.array(sp.simplify(V.H * N16 * V).evalf(), dtype=complex)),
     "$|V^\\dagger N_{16} V|$, block basis"),
    (np.abs(np.array(sp.simplify(V.H * Gamma * V).evalf(), dtype=complex)),
     "$|V^\\dagger \\Gamma V|$: pairs of blocks"),
]
```

Three matrices to draw, each with its title: `evalf()` turns exact entries into decimal numbers, `np.array(..., dtype=complex)` into a numpy array of complex numbers, and `np.abs` takes the absolute value of every entry.

```python
fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.9))
fig.subplots_adjust(wspace=0.45)  # room between the panels for the colour bars
for ax, (values, title) in zip(axes, pictures):
    image = ax.imshow(values, cmap="Blues", vmin=0.0, interpolation="nearest")
    ax.set_title(title, fontsize=9)
    ax.set_xticks([0, 5, 10, 15])
    ax.set_yticks([0, 5, 10, 15])
    ax.set_xlabel("column")
    ax.set_ylabel("row")
    ax.grid(False)  # no grid lines over the matrix
    fig.colorbar(image, ax=ax, shrink=0.75)
```

`zip` pairs each panel with its picture. `imshow` draws a matrix as a **heat map**: one small square per entry, coloured by its value (`cmap="Blues"`: white for 0, dark blue for the largest value; `interpolation="nearest"` keeps the squares sharp). `colorbar` adds the scale of colours beside the panel.

```python
for ax in axes[1:]:  # mark the 2 x 2 blocks in the block basis
    for edge in np.arange(1.5, 15.0, 2.0):
        ax.axhline(edge, color="gray", linewidth=0.4)
        ax.axvline(edge, color="gray", linewidth=0.4)
save_figure(fig, "block_structure",
            ...)
```

In the second and third panels thin gray lines are drawn between rows and columns 1 and 2, 3 and 4, and so on (`np.arange(1.5, 15.0, 2.0)` is 1.5, 3.5, ..., 13.5), which frame the eight blocks. **What figure 14a.4 shows.** Left: in the original basis the entries of $N_{16}$ are spread over the whole matrix in a diamond pattern. Middle: in the block basis only the eight $2 \times 2$ blocks on the diagonal are nonzero. In every block the diagonal entries are $\pm M$ ($|1|$) and the two off-diagonal entries have the sizes $|\kappa k + j\varepsilon| = 1.2$ and $|j\varepsilon - \kappa k| = 0.2$; in the first four blocks ($j = +1$) the large one is above the diagonal, in the last four ($j = -1$) below it: the two block types are visible. Right: $V^\dagger\Gamma V$ has entries of size 1 only between the block $b$ and the block $b \pm 4$, the pairs $(j, s_2, s_3) \leftrightarrow (-j, s_2, s_3)$.

**In [16], the block Hamiltonian, its two types and Γ.**

```python
ok_h = True
for i, (j, a, b) in enumerate(labels):  # the three pieces of h in block i
    Vb = V[:, 2 * i:2 * i + 2]
    ok_h &= sp.simplify(Vb.H * (sp.I * g4 * g8) * Vb + sp.I * j * s1).is_zero_matrix
    ok_h &= sp.simplify(Vb.H * (-g4 * g1) * Vb - j * s3).is_zero_matrix
    ok_h &= sp.simplify(Vb.H * (-sp.I * g4) * Vb - j * s2m).is_zero_matrix
check(ok_h and record_check("block_hamiltonian"),
      "h_j = j[-i sigma1 d/dy + M sigma2 + kappa k sigma3] + v in all 8 blocks",
      record=f"{PY_REPORT}, check block_hamiltonian")
```

`enumerate` gives each block its number `i` together with its labels. `Vb` holds the two basis columns of the block. The three lines check the three matrix pieces of $h$ (with $\mathbf k$ along $x_1$): $i\gamma^{(x_4)}\gamma^{(x_8)} \to -ij\sigma_1$, $-\gamma^{(x_4)}\gamma^{(x_1)} \to j\sigma_3$, $-i\gamma^{(x_4)} \to j\sigma_2$. Together they give $h_j$.

```python
eps = sp.symbols("epsilon", real=True)  # the level


def h_algebraic(j, M_, k_, kap_):
    return j * (M_ * s2m + kap_ * k_ * s3)


def N_matrix(j, M_, k_, eps_, v_, kap_):
    return M_ * s3 - kap_ * k_ * s2m + sp.I * j * (eps_ - v_) * s1
```

The level $\varepsilon$ as a symbol; `h_algebraic` is the part of $h_j - v$ without the derivative, $j(M\sigma_2 + \kappa k\sigma_3)$; `N_matrix` is the matrix $N$ of the first-order form.

```python
kk = sp.symbols("k", real=True)
# h chi = eps chi  <=>  -i j sigma1 chi' = (eps - v - j(M s2 + kappa k s3)) chi
ok_ode = all(sp.simplify(-sp.I * j * s1 * N_matrix(j, M, kk, eps, v, kap)
                         - ((eps - v) * I2 - h_algebraic(j, M, kk, kap)))
             .is_zero_matrix for j in (1, -1))
check(ok_ode and record_check("block_ode_equivalent"),
      "h_j chi = eps chi is the same as d chi/dy = N chi",
      record=f"{PY_REPORT}, check block_ode_equivalent")
```

`kk` is the momentum $k$ as a real symbol. The comment line says what the check is about: the equation $h_j\chi = \varepsilon\chi$ reads $-ij\sigma_1\chi' = (\varepsilon - v)\chi - j(M\sigma_2 + \kappa k\sigma_3)\chi$ (the first line of the first-order form in Section 14.5; `<=>` means "is the same as"). If $\chi' = N\chi$, this holds for every $\chi$ exactly when $-ij\sigma_1N = (\varepsilon - v) - j(M\sigma_2 + \kappa k\sigma_3)$, which is checked for both types.

```python
d_term = -sp.I * s1  # the matrix in front of d/dy (times j)
ok_types = ((h_algebraic(1, M, kk, kap) + h_algebraic(-1, M, kk, kap))
            .is_zero_matrix
            and (s3 * h_algebraic(1, M, kk, kap) * s3
                 - h_algebraic(-1, M, -kk, kap)).is_zero_matrix
            and (s3 * d_term * s3 + d_term).is_zero_matrix)
check(ok_types and record_check("block_type_relation"),
      "h_(-1) - v = -(h_(+1) - v) and sigma3 h_j(k) sigma3 = h_(-j)(-k)",
      record=f"{PY_REPORT}, check block_type_relation")
```

The two type relations of Section 14.5: the algebraic parts of the two types add to zero; $\sigma_3$ turns the algebraic part of $(+1, k)$ into that of $(-1, -k)$; and $\sigma_3(-i\sigma_1)\sigma_3 = i\sigma_1$, so the derivative term changes sign as $j$ does.

```python
YG = sp.simplify(V.H * Gamma * V)
pairs = [(a, b) for a in range(8) for b in range(8)
         if not YG[2 * a:2 * a + 2, 2 * b:2 * b + 2].is_zero_matrix]
say(f"Gamma connects the blocks (from, to): {pairs}")
```

$\Gamma$ in the block basis, and the list of the block pairs $(a, b)$ between which it has a nonzero $2 \times 2$ entry. Out [16] prints the eight pairs $(0, 4), (1, 5), \dots, (7, 3)$.

```python
ok_pairs = (pairs == [(0, 4), (1, 5), (2, 6), (3, 7), (4, 0), (5, 1), (6, 2), (7, 3)]
            and all(YG[2 * a:2 * a + 2, 2 * b:2 * b + 2] == labels[a][1] * s2m
                    for (a, b) in pairs)
            and (Gamma * J + J * Gamma).is_zero_matrix
            and (Gamma * K1 - K1 * Gamma).is_zero_matrix
            and (Gamma * K2 - K2 * Gamma).is_zero_matrix)
check(ok_pairs and record_check("blocks_relation_to_Gamma"),
      "Gamma maps block (j, s2, s3) onto (-j, s2, s3) with the entry s2 sigma2",
      record=f"{PY_REPORT}, check blocks_relation_to_Gamma")
```

Block $b$ and block $b + 4$ differ only in $j$ (the order of `labels`); each entry is $s_2\sigma_2$ (`labels[a][1]` is the $s_2$ of block $a$); $\Gamma$ anticommutes with $J$ and commutes with $K_1$, $K_2$.

```python
ok_map = ((s2m * h_algebraic(1, M, kk, kap) * s2m
           - h_algebraic(-1, -M, kk, kap)).is_zero_matrix
          and (s2m * d_term * s2m + d_term).is_zero_matrix)
check(ok_map and record_check("block_Gamma_map"),
      "sigma2 h_j(M, k) sigma2 = h_(-j)(-M, k): Gamma reverses the mass",
      record=f"{PY_REPORT}, check block_Gamma_map")
```

Section 14.6 line by line: $\sigma_2$ turns the algebraic part of $(j = 1, M)$ into that of $(j = -1, -M)$ at the same $k$, and changes the sign of the derivative term.

**In [17], rotations.**

```python
theta = sp.symbols("theta", real=True)
R = sp.cos(theta / 2) * I16 + sp.sin(theta / 2) * g1 * g2  # the spinor rotation
R_inverse = sp.cos(theta / 2) * I16 - sp.sin(theta / 2) * g1 * g2  # its inverse
rotated = sp.simplify(R * (kk * g1) * R_inverse)
```

The spinor rotation of Section 14.6, its inverse, and the rotated momentum term $R(k\gamma^{(x_1)})R^{-1}$.

```python
ok_rotation = (sp.simplify(R * R_inverse) == I16
               and sp.simplify(rotated - kk * (sp.cos(theta) * g1
                                               - sp.sin(theta) * g2)).is_zero_matrix
               and all((R * Xm - Xm * R).is_zero_matrix for Xm in (g8, g4, B, C)))
check(ok_rotation and record_check("rotation_invariance"),
      "a 3-space rotation commutes with g8, g4, B, C and rotates k: only |k| counts",
      record=f"{PY_REPORT}, check rotation_invariance")
```

Three facts: $RR^{-1} = 1$; $R\,k\gamma^{(x_1)}R^{-1} = k(\cos\theta\,\gamma^{(x_1)} - \sin\theta\,\gamma^{(x_2)})$; $R$ commutes with $\gamma^{(x_8)}$, $\gamma^{(x_4)}$, $B$, $C$.

**In [18], the rescaling identity.**

```python
a_sym, y_sym = sp.symbols("a y", real=True)
ell, v_t, lam = sp.symbols("ell v_t lambda", positive=True)


def h_slice(j, k_, a_):
    return j * (M * s2m + sp.exp(-H * y_sym - a_) * k_ * s3)


def proper_factor(ell_, v_t_):
    return sp.exp(-6 * H * y_sym) / (ell_ ** 3 * v_t_)
```

Symbols for the slice $a_{4,0}$ (`a_sym`), the hidden coordinate, the box size $\ell$, the extra-time volume $v_t$ and the coupling $\lambda$. `h_slice` is the algebraic part of $h_j$ at a slice, with $\kappa = e^{-Hy - a}$; `proper_factor` is the factor $P$ of the proper densities.

```python
ok_h_slice = all(sp.simplify(h_slice(j, kk, a_sym)
                             - h_slice(j, kk * sp.exp(-a_sym), 0)).is_zero_matrix
                 for j in (1, -1))
ok_box = sp.simplify(proper_factor(ell, v_t) - proper_factor(
    ell * sp.exp(a_sym), v_t * sp.exp(-3 * a_sym))) == 0
ok_lambda = sp.simplify(lam * proper_factor(ell, v_t) - lam * sp.exp(3 * a_sym)
                        * proper_factor(ell * sp.exp(a_sym), v_t)) == 0
check(ok_h_slice and ok_box and ok_lambda and record_check("rescaling_identity"),
      "KS(a4,0; dk, v_t, lambda) = KS(0; dk e^(-a4,0), v_t e^(-3 a4,0), lambda)",
      record=f"{PY_REPORT}, check rescaling_identity")
```

The three statements of Section 14.7: the block Hamiltonian at the slice $a$ with momentum $k$ equals the one at the slice 0 with momentum $ke^{-a}$; the box $(\ell e^a, v_te^{-3a})$ has the same factor $P$; and the coupling $\lambda e^{3a}$ times the density factor of the box $(\ell e^a, v_t)$ equals $\lambda$ times the original factor.

```python
rows = repository_file("Revision/kohn_sham/results/rescaling/rescaling.csv") \
    .read_text(encoding="utf-8").splitlines()
header = rows[0].split(",")
table = [dict(zip(header, row.split(","))) for row in rows[1:]]
```

The Rust solver's record of the partner problems, a **CSV file** (comma-separated values: a table as text, one row per line, the cells separated by commas, the first line the column names). `splitlines` cuts the text into lines and `split(",")` a line into cells; `dict(zip(header, cells))` makes a dictionary from column name to cell for every row.

```python
worst = 0.0
for a in slices[1:]:
    dk_partner = 0.25 * np.exp(-a)  # the partner lattice spacing
    vt_partner = 1.0 * np.exp(-3 * a)  # the partner extra-time volume (v_t = 1)
    say(f"slice a4,0 = {a}: partner dk = {dk_partner:.12f}, "
        f"partner v_t = {vt_partner:.12f}")
    for row in table:
        if float(row["a4"]) == a:
            worst = max(worst, abs(float(row["partner_dk"]) / dk_partner - 1),
                        abs(float(row["partner_v_t"]) / vt_partner - 1))
check(len(table) == 60 and worst < 1e-14,
      "the partner spacings and volumes equal those of all 60 rows of the record",
      record="Revision/kohn_sham/results/rescaling/rescaling.csv, columns "
             "partner_dk and partner_v_t")
```

For each later slice (`slices[1:]` leaves out the slice 0) the partner spacing $0.25\,e^{-a}$ and the partner volume $e^{-3a}$ are computed and printed with 12 decimals (the format `:.12f`). For every row of the record at that slice the relative difference is taken, and the largest is kept in `worst`. The record has 60 rows (three particle numbers, five couplings and four later slices) and agrees to better than $10^{-14}$. Out [18] shows the partner numbers, for example $0.151632664928$ and $0.223130160148$ for $a_{4,0} = 0.5$.

**In [19], figure 5.**

```python
ell_value = 2 * np.pi / 0.25  # the coordinate box size of the solver (dk = 0.25)
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
for n2 in (1, 2, 3, 4, 5, 6):  # the first shells n1^2 + n2^2 + n3^2
    left.semilogy(a4_values, 0.25 * np.sqrt(n2) * np.exp(-a4_values),
                  label=f"$n^2 = {n2}$")
```

The box size $\ell = 2\pi/0.25$; the left panel draws, for the first six lattice shells ($|\mathbf k| = 0.25\sqrt{n^2}$), the redshifted momentum $|\mathbf k|e^{-a_{4,0}}$ against the slice.

```python
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("$|\\mathbf{k}|\\,e^{-a_{4,0}}$ (units of $H$, logarithmic)")
left.set_title("redshift of the lattice momenta")
left.legend(fontsize=8, ncol=2)
right.semilogy(a4_values, (ell_value * np.exp(a4_values)) ** 3,
               label="3-space box $(\\ell e^{a_{4,0}})^3$")
right.semilogy(a4_values, np.exp(-3 * a4_values), "--",
               label="extra-time box $v_t e^{-3a_{4,0}}$")
right.semilogy(a4_values, ell_value ** 3 * np.exp(3 * a4_values)
               * np.exp(-3 * a4_values), ":", color="black",
               label="7-volume $\\ell^3 v_t$ (constant)")
```

Labels (`ncol=2` puts the legend in two columns), and in the right panel the proper volumes at the brane of the 3-space box, of the extra-time box and their product.

```python
right.set_xlabel("slice $a_{4,0}$")
right.set_ylabel("proper volume at $y = 0$ (logarithmic)")
right.set_title("the boxes inflate and deflate, the 7-volume stays")
right.legend(fontsize=8)
save_figure(fig, "rescaling",
            ...)
```

**What figure 14a.5 shows.** Left: six parallel straight lines of slope $-1$ on the logarithmic axis: every lattice momentum is redshifted by the same factor $e^{-a_{4,0}}$, so the ordering of the shells never changes. Right: the 3-space box grows from $(8\pi)^3 \approx 1.6\times10^4$ by the factor $e^6 \approx 403$, the extra-time box shrinks from 1 to $e^{-6} \approx 0.0025$, and their product, the dotted line, stays constant. This is the rescaling identity in a picture: a later slice is the slice 0 with a finer momentum lattice and the same proper box.

**In [20], the last check.**

```python
figure_names = ["14a_1_hidden_coordinate.png", "14a_2_inflation_deflation.png",
                "14a_3_spin_connection_terms.png", "14a_4_block_structure.png",
                "14a_5_rescaling.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all five figure files of this notebook exist")
all_checks_passed()
```

The five figure files must exist where the notebook wrote them; the last line prints ALL 28 CHECKS PASSED (notebook 14a). The 28 checks are: 1 in In [2], 2 in In [3], 2 in In [4], 2 in In [7], 2 in In [8], 2 in In [10], 2 in In [11], 2 in In [12], 2 in In [13], 2 in In [14], 5 in In [16], 1 in In [17], 2 in In [18] and 1 in In [20].

### 14.12 The block equation in real form and the boundary conditions

**The real form.** In every block the stationary equation is $\chi' = N\chi$ with $N = M\sigma_3 - \kappa k\,\sigma_2 + ij(\varepsilon - v)\sigma_1$ (Section 14.5). Write the two components of $\chi$ as $\chi = (a, ib)$ with two real functions $a(y)$ and $b(y)$, and write $K = \kappa k$ and $\varepsilon' = \varepsilon - v$ for short. Line by line:

$$
\sigma_3\chi = (a,\ -ib), \qquad \sigma_2\chi = (b,\ ia), \qquad \sigma_1\chi = (ib,\ a) .
$$

Rule: multiply each Pauli matrix of Section 14.1 with the column $(a, ib)$; for example the first entry of $\sigma_2\chi$ is $(-i)(ib) = -i^2b = b$.

$$
N\chi = \Big(Ma - Kb - j\varepsilon' b,\ \ i\big[(j\varepsilon' - K)a - Mb\big]\Big) .
$$

Rule: $N\chi = M\sigma_3\chi - K\sigma_2\chi + ij\varepsilon'\sigma_1\chi$, entry by entry; in the first entry $ij\varepsilon'(ib) = i^2j\varepsilon' b = -j\varepsilon' b$; the second entry is $-iMb - iKa + ij\varepsilon' a$, which is $i$ times the bracket.

$$
a' = Ma - (K + j\varepsilon')\,b, \qquad b' = (j\varepsilon' - K)\,a - Mb .
$$

Rule: $\chi' = (a', ib')$; compare the first entries, and the second entries divided by $i$. Every coefficient is a real number, so a solution that starts with real values $a$, $b$ stays real: the computer needs only real numbers. Status: PROVED; the record states this form as blockEquation.realForm in `Revision/kohn_sham/ks-theory.json`, and Notebook 14b checks it with sympy (In [2]).

**The densities of one orbital.** From the three products above and $\chi^\dagger = (a, -ib)$ (the conjugate transpose of the column, with $a$, $b$ real):

$$
\chi^\dagger\chi = a^2 + b^2, \qquad \chi^\dagger\sigma_2\chi = 2ab, \qquad \chi^\dagger\sigma_3\chi = a^2 - b^2, \qquad \chi^\dagger\sigma_1\chi = 0 .
$$

Rule: multiply the row $(a, -ib)$ with each column; for example $\chi^\dagger\sigma_2\chi = a\cdot b + (-ib)(ia) = ab + ab$, and $\chi^\dagger\sigma_1\chi = a(ib) + (-ib)a = 0$. These four numbers become the number density, the scalar density, the density $Q$ and the current along $y$ of the orbital (Sections 14.26 and 14.27). Status: PROVED (the multiplication above); the record states the same four formulas as blockEquation.realFormDensities in `Revision/kohn_sham/ks-theory.json`.

**The current along $y$ is the same at every point.** The number $\chi^\dagger\sigma_1\chi$ is the flow along the hidden direction of the U(1) charge of the field (the **current** along $y$). Of this charge only the local conservation law is proved; its total is constant only under the ASSUMED no-flux condition at the brane $z = \pi/2$ (Chapter 5, Section 5.6), and the Z2 mirror assumed below is such a condition. For every solution of the block equation, complex or real:

$$
\frac{d}{dy}\big(\chi^\dagger\sigma_1\chi\big) = \chi'^\dagger\sigma_1\chi + \chi^\dagger\sigma_1\chi' = \chi^\dagger\big(N^\dagger\sigma_1 + \sigma_1N\big)\chi .
$$

Rule: the product rule; then $\chi' = N\chi$ and $\chi'^\dagger = (N\chi)^\dagger = \chi^\dagger N^\dagger$.

$$
N^\dagger = M\sigma_3 - K\sigma_2 - ij\varepsilon'\sigma_1 .
$$

Rule: the Pauli matrices are Hermitian, $M$, $K$, $\varepsilon'$ are real, and the complex conjugate of $i$ is $-i$.

$$
N^\dagger\sigma_1 + \sigma_1N = M(\sigma_3\sigma_1 + \sigma_1\sigma_3) - K(\sigma_2\sigma_1 + \sigma_1\sigma_2) - ij\varepsilon'\sigma_1\sigma_1 + ij\varepsilon'\sigma_1\sigma_1 = 0 .
$$

Rule: two different Pauli matrices anticommute, so the first two brackets are zero, and the last two terms cancel. So the current has the same value at every $y$. The density $\chi^\dagger\chi$ is not constant: its derivative is $\chi^\dagger(N^\dagger + N)\chi$ with $N^\dagger + N = 2M\sigma_3 - 2K\sigma_2 \ne 0$. Status: PROVED; check bc_current_conserved_along_y of `Revision/kohn_sham/reports/ks-theory-python.json` and of the Wolfram report.

**Why the two ends must stop the current.** Section 14.4 called $h$ Hermitian "when the boundary terms vanish". Here is the boundary term. For two columns $\varphi$ and $\chi$ of functions of $y$:

$$
\varphi^\dagger h_j\chi - (h_j\varphi)^\dagger\chi = -ij\varphi^\dagger\sigma_1\chi' - ij\varphi'^\dagger\sigma_1\chi = \frac{d}{dy}\big[-ij\,\varphi^\dagger\sigma_1\chi\big] .
$$

Rule, for the first equality: the part of $h_j$ without derivative, $j(M\sigma_2 + K\sigma_3) + v$, is a Hermitian matrix, so it gives $\varphi^\dagger X\chi - (X\varphi)^\dagger\chi = \varphi^\dagger X\chi - \varphi^\dagger X^\dagger\chi = 0$; the derivative part gives $\varphi^\dagger(-ij\sigma_1\chi') - (-ij\sigma_1\varphi')^\dagger\chi$, and $(-ij\sigma_1\varphi')^\dagger = +ij\varphi'^\dagger\sigma_1$. Rule, for the second: the product rule backwards. Integrating from $-L$ to $0$:

$$
\int_{-L}^{0}\varphi^\dagger h_j\chi\,dy - \int_{-L}^{0}(h_j\varphi)^\dagger\chi\,dy = -ij\big[\varphi^\dagger\sigma_1\chi\big]_{y=-L}^{y=0} .
$$

Rule: the integral of a derivative is the difference of its end values. So $h_j$ is self-adjoint (the two integrals are equal, the levels are real and orbitals of different levels are orthogonal, Section 14.4) exactly when the boundary conditions make $\varphi^\dagger\sigma_1\chi$ vanish at both ends: the conditions must **kill the current**. Status: PROVED; check bc_self_adjoint_boundary_term (both reports).

**The brane at $y = 0$ (ASSUMED).** The author's coordinate patch ends at $y = 0$, where $z = \pi/2$. Something must be said about what lies beyond it. The Revision theory ASSUMES a **Z2 mirror** (also called an **orbifold**): the patch $y \le 0$ is glued at $y = 0$ to a mirror copy of itself, with the warp $e^{-H|y|}$ on both sides, and a field on the doubled interval obeys $\Psi(-y) = \pm\gamma^{(x_8)}\Psi(y)$. At $y = 0$ this relation says $\Psi(0) = \pm\gamma^{(x_8)}\Psi(0)$, that is $(1 \mp \gamma^{(x_8)})\chi(0) = 0$. In every block $\gamma^{(x_8)}$ is $\sigma_3$ (Section 14.5), and $1 - \sigma_3 = \mathrm{diag}(0, 2)$, $1 + \sigma_3 = \mathrm{diag}(2, 0)$. Hence two kinds of orbitals, called the two **parities**:

- EVEN parity (upper sign): $\chi_2(0) = 0$; in real form $b(0) = 0$.
- ODD parity (lower sign): $\chi_1(0) = 0$; in real form $a(0) = 0$.

Both kill the current, because $\chi^\dagger\sigma_1\chi = \chi_1^*\chi_2 + \chi_2^*\chi_1$ (the star is the complex conjugate) is zero when $\chi_1$ or $\chi_2$ is zero. Status: the mirror is ASSUMED; the two conditions follow from it (PROVED; check bc_brane_parity_conditions, both reports).

**What the mirror does to the mass.** Let $\chi$ solve $\chi'(y) = N(y)\chi(y)$ and put $\tilde\chi(y) = \sigma_3\chi(-y)$. Line by line:

$$
\tilde\chi'(y) = -\sigma_3\chi'(-y) = -\sigma_3N(-y)\chi(-y) = -\sigma_3N(-y)\sigma_3\,\tilde\chi(y) .
$$

Rule: the chain rule (the derivative of $\chi(-y)$ is $-\chi'(-y)$), then the equation at the point $-y$, then $\chi(-y) = \sigma_3\tilde\chi(y)$ because $\sigma_3\sigma_3 = 1$.

$$
-\sigma_3N\sigma_3 = -M\sigma_3 - K\sigma_2 + ij\varepsilon'\sigma_1 .
$$

Rule: $\sigma_3\sigma_3\sigma_3 = \sigma_3$, $\sigma_3\sigma_2\sigma_3 = -\sigma_2$, $\sigma_3\sigma_1\sigma_3 = -\sigma_1$. This is the matrix $N$ with $M$ replaced by $-M$. So $\tilde\chi$ solves the block equation with the mass $-M(-y)$, the potential $v(-y)$ and the weight $\kappa(-y)$ (the weight of the mirror copy). The doubled problem is therefore mirror-symmetric only if the mass is **odd** across the brane. The densities say the same: under the map the number density and $Q$ (built from $\chi^\dagger\chi$ and $\chi^\dagger\sigma_3\chi$) are even, while the scalar density $S$ (built from $\chi^\dagger\sigma_2\chi$) and the current change sign, because $\sigma_3$ commutes with $1$ and $\sigma_3$ and anticommutes with $\sigma_2$ and $\sigma_1$. Since $M_{\rm eff} = m + \tfrac{15}{16}\lambda S$ (Section 14.27) and $S$ is odd, the mirror copy carries $(-m, +\lambda)$. Status: PROVED; checks bc_mirror_map_PA and bc_mirror_parities_of_densities (both reports).

**What this does and does not say (honesty).** The pair $(+m, -m)$ of the patch and its mirror copy is the mirror pair of the pairing theorem T3, which Chapter 19 proves. It is an exact map between solutions of the equations with an ASSUMED boundary construction. It does not say that a mirror copy, a second universe or a pair of universes is created by any process: no creation process, rate or amplitude follows from these equations (Chapters 18 to 20 give the complete statements and the list of what is not proved).

**The tip (ASSUMED: a chosen cutoff condition).** The hidden coordinate runs to minus infinity at the tip, which a computer cannot reach. The Revision solver stops at $y = -L$ ($L = 3$) and imposes there one member of the family

$$
\big(1 - Q(\theta)\big)\chi(-L) = 0, \qquad Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2 .
$$

Line by line, why every member kills the current. First, $Q^\dagger = Q$ (rule: $\sigma_3$, $\sigma_2$ are Hermitian, $\cos\theta$ and $\sin\theta$ are real). Second, $Q^2 = \cos^2\theta + \sin^2\theta + \cos\theta\sin\theta(\sigma_3\sigma_2 + \sigma_2\sigma_3) = 1$ (rule: multiply out; each $\sigma^2 = 1$ and the bracket is zero). Third, $Q\sigma_1 = -\sigma_1Q$ (rule: $\sigma_1$ anticommutes with $\sigma_3$ and with $\sigma_2$). Now if $Q\chi = \chi$ at the end point, then

$$
\chi^\dagger\sigma_1\chi = \chi^\dagger\sigma_1Q\chi = -\chi^\dagger Q\sigma_1\chi = -(Q\chi)^\dagger\sigma_1\chi = -\chi^\dagger\sigma_1\chi ,
$$

so $\chi^\dagger\sigma_1\chi = 0$ there. Rule: replace $\chi$ by $Q\chi$, move $Q$ to the left with the third fact, use $Q^\dagger = Q$, then $Q\chi = \chi$ again. The canonical choice is $\theta = 0$: $(1 - \sigma_3)\chi(-L) = 0$, that is $\chi_2(-L) = 0$, $b(-L) = 0$, the **regular tip**. In real form a member $\theta$ is satisfied by the starting point $(a, b) = (\cos\tfrac\theta2, \sin\tfrac\theta2)$ at $y = -L$ (Exercise 14.3), which is where the shooting of Section 14.14 starts. Status: the algebra is PROVED (check bc_tip_family, both reports); the choice of the condition is ASSUMED.

**Zero current everywhere.** An **orbital** is a solution that satisfies the brane condition and the tip condition. Its current is zero at the two ends and the same at every $y$, so it is zero everywhere. (For a real solution $(a, b)$ it is zero anyway, by the densities above.)

**Why the tip hardly matters when the 3-momentum is not zero.** Toward the tip the weight $\kappa = e^{-Hy - a_{4,0}}$ grows without bound, and for large $\kappa$ the matrix $N$ is dominated by its momentum term, $N \approx -\kappa k\,\sigma_2$. Line by line:

- $\sigma_2$ has the eigenvalues $s = +1$ and $s = -1$ (it squares to 1 and its trace is 0), with eigenvectors $u_+$ and $u_-$.
- On $u_s$ the equation $\chi' \approx -\kappa k\sigma_2\chi$ reads $\chi' \approx -s\kappa k\,\chi$.
- Its solution is $\chi \propto \exp(sk\kappa/H)\,u_s$. Rule: the derivative of $e^{-Hy}$ is $-He^{-Hy}$, so the derivative of $\kappa/H$ is $-\kappa$, and the chain rule gives the derivative of $\exp(sk\kappa/H)$ as $(sk)(-\kappa)\exp(sk\kappa/H)$.
- For $k > 0$ the branch $s = +1$ grows enormously toward the tip and the branch $s = -1$ decays toward the tip (for $k < 0$ the two exchange their roles). The decaying branch, $\sigma_2\chi = -\chi$ for $k > 0$, is the **regular** one.
- An orbital is therefore suppressed at the cutoff, compared with its size at a point $y$, by about the factor $\exp(-|k|(\kappa(-L) - \kappa(y))/H)$. Rule: the ratio of $\exp(-|k|\kappa/H)$ at the two points.

Whatever condition is imposed at $y = -L$ acts on a part of the orbital that is already this small, so for $k \ne 0$ the levels should change by about this factor at most; this last step is an estimate, not a proof. At the slice $a_{4,0} = 0$, between the brane and the cutoff, $\kappa(-L) - \kappa(0) = e^{HL} - 1 = e^3 - 1 \approx 19.09$, and for the smallest lattice momentum $k = 0.25$ the factor is $8.47\times10^{-3}$ (the column suppression_factor of `Revision/kohn_sham/results/spectrum/tip-angle.csv`). At a later slice the difference is smaller by the factor $e^{-a_{4,0}}$, $\kappa(-L) - \kappa(0) = e^{-a_{4,0}}(e^{HL} - 1)$ (rule: $\kappa = e^{-Hy - a_{4,0}}$ at the two points): along the history the redshifted orbitals reach farther toward the tip, and the position $L$ of the cutoff begins to matter (Section 14.20). At $k = 0$ there is no suppression and the tip condition matters: there the choice $\theta = 0$ selects the brane zero mode of Section 14.13. Status: the two asymptotic branches, the regular branch and the suppression factor of the orbital are PROVED (check bc_tip_asymptotics, both reports); the bound on the change of the levels is an estimate, whose size is COMPUTED in Section 14.20 (check free_tip_angle_insensitivity of `Revision/kohn_sham/reports/ks-rust-solver.json`, record `Revision/kohn_sham/results/spectrum/tip-angle.csv`).

### 14.13 The exact free levels at zero 3-momentum

Take $k = 0$, $v = 0$ and a constant mass $M > 0$. The real form becomes $a' = Ma - j\varepsilon b$, $b' = j\varepsilon a - Mb$. These two equations can be solved by hand, completely. The solutions are the first test of any numerical method for the model.

**Step 1: one equation of second order.** Suppose $\varepsilon \ne 0$. Line by line:

$$
a = \frac{b' + Mb}{j\varepsilon} .
$$

Rule: solve the second equation for $a$ (add $Mb$ and divide by $j\varepsilon \ne 0$).

$$
a' = \frac{b'' + Mb'}{j\varepsilon} .
$$

Rule: differentiate; $M$, $j$, $\varepsilon$ are constants.

$$
b'' + Mb' = M(b' + Mb) - j^2\varepsilon^2b .
$$

Rule: insert the two lines into the first equation $a' = Ma - j\varepsilon b$ and multiply by $j\varepsilon$.

$$
b'' = (M^2 - \varepsilon^2)\,b .
$$

Rule: $j^2 = 1$, and $Mb'$ cancels on both sides.

The general solution of this equation depends on the sign of $M^2 - \varepsilon^2$ (check each by differentiating twice): if $\varepsilon^2 > M^2$, write $M^2 - \varepsilon^2 = -p^2$ with $p > 0$, and $b = A\sin(py) + B\cos(py)$; if $\varepsilon^2 < M^2$, write $M^2 - \varepsilon^2 = q^2$ with $q > 0$, and $b = Ae^{qy} + Be^{-qy}$; if $\varepsilon^2 = M^2$, then $b = A + By$. Here $A$ and $B$ are constants.

**Step 2: even parity, $b(0) = 0$ and $b(-L) = 0$.**

- $\varepsilon^2 > M^2$: $b(0) = B = 0$, so $b = A\sin(py)$; then $b(-L) = -A\sin(pL) = 0$ with $A \ne 0$ requires $pL = n\pi$, $n = 1, 2, 3, \dots$ Hence the levels $\varepsilon = \pm\sqrt{M^2 + (n\pi/L)^2}$.
- $\varepsilon^2 < M^2$, $\varepsilon \ne 0$: $b(0) = A + B = 0$ gives $b = A(e^{qy} - e^{-qy})$, and $b(-L) = A(e^{-qL} - e^{qL}) = 0$ forces $A = 0$ (because $e^{qL} > e^{-qL}$); then $b = 0$ and $a = (b' + Mb)/(j\varepsilon) = 0$: no orbital.
- $\varepsilon^2 = M^2$: $b(0) = A = 0$ and $b(-L) = -BL = 0$, so $b = 0$ and again no orbital.
- $\varepsilon = 0$ (Step 1 does not apply): the equations separate, $a' = Ma$ and $b' = -Mb$, so $a = Ae^{My}$, $b = Be^{-My}$. The brane condition $b(0) = B = 0$ makes $b = 0$ everywhere, which also satisfies $b(-L) = 0$. So $\chi = (Ae^{My}, 0)$ is an orbital with $\varepsilon = 0$, for every $L$: the **brane zero mode**, largest at the brane.

The constant of the zero mode follows from the normalisation $\int_{-L}^0 a^2\,dy = 1$:

$$
\int_{-L}^{0}A^2e^{2My}\,dy = A^2\,\frac{1 - e^{-2ML}}{2M} = 1, \qquad A = \sqrt{\frac{2M}{1 - e^{-2ML}}} .
$$

Rule: the integral of $e^{2My}$ is $e^{2My}/(2M)$; evaluate at $0$ and $-L$ and subtract; solve for $A > 0$.

**Step 3: odd parity, $a(0) = 0$ and $b(-L) = 0$.**

- $\varepsilon^2 > M^2$: the solution with $b(-L) = 0$ is $b = A\sin(p(y + L))$ (the general solution written around the point $-L$, where the cosine term must vanish). By Step 1, $a(0) = 0$ means $b'(0) + Mb(0) = 0$, that is $A[p\cos(pL) + M\sin(pL)] = 0$. So the levels are $\varepsilon = \pm\sqrt{M^2 + p^2}$ where $p > 0$ solves

$$
f(p) = M\sin(pL) + p\cos(pL) = 0, \qquad \text{equivalently} \qquad \tan(pL) = -\frac{p}{M} .
$$

Rule: divide by $M\cos(pL)$, which is not zero (if $\cos(pL) = 0$ then $f = \pm M \ne 0$).
- $\varepsilon^2 < M^2$, $\varepsilon \ne 0$: $b = A(e^{q(y+L)} - e^{-q(y+L)})$, and $b'(0) + Mb(0) = A[q(e^{qL} + e^{-qL}) + M(e^{qL} - e^{-qL})] = 0$ forces $A = 0$ (the bracket is positive): no orbital.
- $\varepsilon^2 = M^2$: $b = B(y + L)$ and $b'(0) + Mb(0) = B(1 + ML) = 0$ forces $B = 0$: no orbital.
- $\varepsilon = 0$: $a = Ae^{My}$ with $a(0) = A = 0$, and $b = Be^{-My}$ with $b(-L) = Be^{ML} = 0$, so $B = 0$: there is no zero mode of odd parity.

**Step 4: the odd roots.** Count the roots of $f(p) = M\sin(pL) + p\cos(pL)$ for $p > 0$. At $p = (n + \tfrac12)\pi/L$ the sine is $(-1)^n$ and the cosine 0, so $f = M(-1)^n$; at $p = (n + 1)\pi/L$ the sine is 0 and the cosine $(-1)^{n+1}$, so $f = p(-1)^{n+1}$. The two values have opposite signs, so $f$ has a root in between (rule: a continuous function that changes sign on an interval is zero somewhere in it). It has exactly one there: on this interval $\tan(pL)$ rises from minus infinity to 0 while $-p/M$ falls, so the two curves meet once; and on the intervals from $n\pi/L$ to $(n + \tfrac12)\pi/L$ there is no root, because there $\tan(pL) > 0 > -p/M$. So the roots are $p_0 < p_1 < p_2 < \dots$, one in each interval $((n + \tfrac12)\pi/L,\ (n + 1)\pi/L)$.

**Summary (PROVED).** At $k = 0$, $v = 0$, constant $M > 0$ and the canonical tip:

| parity | levels | orbital |
| --- | --- | --- |
| even | $0$ (the brane zero mode) | $(\sqrt{2M/(1 - e^{-2ML})}\,e^{My},\ 0)$ |
| even | $\pm\sqrt{M^2 + (n\pi/L)^2}$, $n = 1, 2, \dots$ | $b = \sin(n\pi y/L)$, $a = (b' + Mb)/(j\varepsilon)$ |
| odd | $\pm\sqrt{M^2 + p_n^2}$, $\tan(p_nL) = -p_n/M$ | $b = \sin(p_n(y + L))$, $a = (b' + Mb)/(j\varepsilon)$ |

Apart from the zero mode, every level has $|\varepsilon| > M$: the free spectrum has a gap from $-M$ to $M$ that contains only the zero modes. Every level of one block type is held by its four blocks $(s_2, s_3)$, so it is 4-fold per type and 8-fold in all (for $v = 0$ the levels of the type $j = -1$ are the negatives of those of $j = +1$, Section 14.5, and the set of levels above is symmetric). Status: PROVED; check bc_exact_k0_spectra (both reports).

**The numbers for $M = 1$, $L = 3$** (Notebook 14b, Out [4]): the first odd roots are $p_0 = 0.818548$, $p_1 = 1.744313$, $p_2 = 2.734844$; the lowest odd level is $\sqrt{1 + p_0^2} = 1.292292828069\,m$ and the lowest positive even level is $\sqrt{1 + (\pi/3)^2} = 1.447971930402\,m$. The Rust solver's record `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv` lists 54 such exact levels (labels $-3$ to $5$, both parities, $(m, L) = (1, 3), (1, 2), (2, 3)$) next to its numerical ones (check free_k0_analytic_spectra of `Revision/kohn_sham/reports/ks-rust-solver.json`); Notebook 14b reproduces both columns.

**The labels.** The Revision solver names the levels by integer **labels**: even parity, label 0 is the zero mode, label $n > 0$ the $n$-th positive level and $-n$ its negative; odd parity, label $l \ge 0$ is the level $+\sqrt{M^2 + p_l^2}$ and label $l \le -1$ the level $-\sqrt{M^2 + p_{-l-1}^2}$. Section 14.14 shows that these labels are not arbitrary names: they count half-turns.

### 14.14 Shooting with a Pruefer angle: every level has a label

**Shooting.** For nonzero $k$, or a mass and a potential that depend on $y$, the block equation cannot be solved by hand, and the computer finds the levels by **shooting** (Chapter 2): start at one end with the condition there, integrate to the other end, and adjust the energy until the condition there holds too. Here the start is the tip, with $(a, b) = (\cos\tfrac\theta2, \sin\tfrac\theta2)$ at $y = -L$, which is $(1, 0)$ for the canonical $\theta = 0$; the real form is integrated from $y = -L$ to $y = 0$ for a trial energy $\varepsilon$; and $\varepsilon$ is a level of even parity if $b(0) = 0$, of odd parity if $a(0) = 0$.

**The Pruefer angle.** Write the point $(a, b)$ of the plane in polar form, $a = r\cos\theta$, $b = r\sin\theta$, with the length $r = \sqrt{a^2 + b^2} > 0$ and the angle $\theta$ (the **Pruefer angle**, after the mathematician Pruefer). On a computer the angle of a point is the function $\mathrm{atan2}(b, a)$, which returns a value between $-\pi$ and $\pi$; following it **continuously** means adding or subtracting $2\pi$ whenever that value jumps, so that $\theta(y)$ has no jumps and can count whole turns. Line by line:

$$
a' = r'\cos\theta - r\theta'\sin\theta, \qquad b' = r'\sin\theta + r\theta'\cos\theta .
$$

Rule: the product rule and the chain rule.

$$
ab' - ba' = r^2\theta'(\cos^2\theta + \sin^2\theta) = r^2\theta' .
$$

Rule: multiply out; the terms with $r'$ cancel; $\cos^2\theta + \sin^2\theta = 1$.

$$
ab' - ba' = j\varepsilon'(a^2 + b^2) - K(a^2 - b^2) - 2Mab .
$$

Rule: insert the real form, $a[(j\varepsilon' - K)a - Mb] - b[Ma - (K + j\varepsilon')b]$, and collect the terms.

$$
\theta' = j\varepsilon' - K\cos2\theta - M\sin2\theta .
$$

Rule: divide the last two lines by $r^2$, with $a^2 - b^2 = r^2(\cos^2\theta - \sin^2\theta) = r^2\cos2\theta$ and $2ab = 2r^2\sin\theta\cos\theta = r^2\sin2\theta$ (the double-angle formulas). The equation for $\theta$ does not contain $r$, so the angle can be followed by itself. Status: PROVED; Notebook 14b checks the last line with sympy (In [6]).

**The angle at the brane grows with the energy.** Let $a_\varepsilon = \partial a/\partial\varepsilon$ and $b_\varepsilon = \partial b/\partial\varepsilon$ be the rates at which the solution changes when the trial energy changes (the tip values do not depend on $\varepsilon$), and put $w = ab_\varepsilon - ba_\varepsilon$. By the same rule as for $\theta'$, with $\varepsilon$ in place of $y$, $\partial\theta/\partial\varepsilon = w/r^2$. Line by line:

$$
w' = a'b_\varepsilon + ab_\varepsilon' - b'a_\varepsilon - ba_\varepsilon' .
$$

Rule: the product rule.

$$
a_\varepsilon' = Ma_\varepsilon - (K + j\varepsilon')b_\varepsilon - jb, \qquad b_\varepsilon' = (j\varepsilon' - K)a_\varepsilon - Mb_\varepsilon + ja .
$$

Rule: differentiate the real form with respect to $\varepsilon$; the product rule applied to $j\varepsilon' b$ and $j\varepsilon' a$ gives the extra terms $-jb$ and $+ja$, since $\partial\varepsilon'/\partial\varepsilon = 1$.

$$
w' = j(a^2 + b^2) = jr^2 .
$$

Rule: insert the real form and the last line into the first line; every term that contains $M$, $K$ or $\varepsilon'$ appears twice with opposite signs and cancels, and what is left is $a(ja) - b(-jb)$.

$$
\frac{\partial\theta(0)}{\partial\varepsilon} = \frac{w(0)}{r(0)^2} = \frac{j}{r(0)^2}\int_{-L}^{0}r^2\,dy .
$$

Rule: $w(-L) = 0$, because the starting point does not depend on $\varepsilon$ ($a_\varepsilon = b_\varepsilon = 0$ at $y = -L$); integrate $w' = jr^2$ from $-L$ to $0$. So the **shooting function** $\Phi(\varepsilon) = j\,\theta(0)$ has the derivative $\int r^2dy/r(0)^2 > 0$: it grows strictly with the energy. Status: PROVED (this derivation); Notebook 14b confirms it numerically for $k = 0$ and $k = 0.75$ (In [7]).

**Every level has an integer label.** $b(0) = 0$ means that $\theta(0)$ is a whole multiple of $\pi$; $a(0) = 0$ means that $\theta(0)$ is $\pi/2$ plus a whole multiple of $\pi$. With $\Phi = j\theta(0)$:

$$
\text{even level:}\ \ \Phi(\varepsilon) = l\pi, \qquad \text{odd level:}\ \ \Phi(\varepsilon) = \frac\pi2 + l\pi, \qquad l = \dots, -1, 0, 1, \dots
$$

The integer $l$ is the **label** of the level. Because $\Phi$ grows strictly, it passes every target value at most once. It passes every target value at least once, because it runs from $-\infty$ to $+\infty$. Line by line:

$$
\theta(0) - \theta(-L) = \int_{-L}^{0}\theta'\,dy = j\varepsilon L - j\int_{-L}^{0}v\,dy - \int_{-L}^{0}\big(K\cos2\theta + M\sin2\theta\big)\,dy .
$$

Rule: integrate the equation of the Pruefer angle from $-L$ to $0$, with $\varepsilon' = \varepsilon - v$ (the integral of the constant $j\varepsilon$ over an interval of length $L$ is $j\varepsilon L$).

$$
\big|\Phi(\varepsilon) - \varepsilon L\big| \le |\theta(-L)| + \int_{-L}^{0}|v|\,dy + \int_{-L}^{0}\big(|K| + |M|\big)\,dy .
$$

Rule: multiply the last line by $j$ (with $j^2 = 1$ this gives $\Phi = j\theta(0)$ on the left and $\varepsilon L$ as the first term on the right), move every other term to the right side, and use $|j| = 1$, $|\cos2\theta| \le 1$, $|\sin2\theta| \le 1$ and the rule that the size of an integral is at most the integral of the size. The right side does not depend on $\varepsilon$: the start angle $\theta(-L)$ is fixed by the tip condition, and $v$, $K$ and $M$ are given functions of $y$. So $\Phi(\varepsilon)$ stays within a fixed distance of the straight line $\varepsilon L$: for very negative $\varepsilon$ it lies below every target value, for very positive $\varepsilon$ above it, and because it has no jumps it passes the target value in between (the intermediate value theorem, Section 2.12). Hence there is exactly one level for every label and parity, no level can be missed and none can be counted twice. Status: PROVED (this derivation; it is not a separate check of the Revision record, and Notebook 14b confirms the labels numerically). At $k = 0$ these are exactly the labels of Section 14.13 (Figure 14b.6 shows the angles).

**Finding a level.** The notebooks of this chapter find a level by plain **bisection** on $\Phi(\varepsilon) - $ target (Chapter 2): they keep an interval with the target between $\Phi(\text{lo})$ and $\Phi(\text{hi})$ and halve it 72 times, starting from $[-20, 20]$. After 72 halvings the interval has the length $40/2^{72} \approx 8.5\times10^{-21}$, far below the spacing of floating-point numbers near 1 (about $2.2\times10^{-16}$): the result is the level of the integrated equation to the last digit the computer can hold, and the error that remains is the error of the integration. The Revision Rust solver finds the root of the same function $\Phi$ with fewer evaluations, by the **safeguarded Newton-bisection** of Section 2.24 (the function find_level of `Revision/kohn_sham/solver/src/shoot.rs`): it widens a bracket around a first guess until $\Phi - $ target changes sign, then takes Newton steps with the derivative $d\Phi/d\varepsilon = \int r^2dy/r(0)^2$ derived above, takes the midpoint of the bracket instead whenever a Newton step would leave the bracket or the last step has not at least halved the mismatch $|\Phi - \text{target}|$, and stops when the bracket, or its last Newton step, is shorter than the tolerance $10^{-13}$ (rootTolerance of `Revision/kohn_sham/results/parameters.json`). Both find the root of the same integrated $\Phi$, so the two sets of levels agree to far below $10^{-11}$; Notebook 14b measures the largest difference, $7.1\times10^{-15}$ (In [8]).

**The integration (RK4).** The real form is integrated with the classical fourth-order Runge-Kutta method of Chapter 2, with $G$ steps of size $h = L/G$ (the Revision solver uses $G = 900$ for $L = 3$, so $h = 1/300$). RK4 needs the coefficient $K = \kappa k$ at the nodes and at the midpoints of the steps, that is on a fine grid of $2G + 1$ points. Its error is proportional to $h^4$: halving the step divides the error of a level by $2^4 = 16$. The Revision record measured exactly this: doubling the step number ($G = 1800$ for $L = 3$, $1200$ for $L = 2$) divided the errors of the 39 levels whose error is above $10^{-11}$ by the median factor 16.00, and the largest errors were $5.050\times10^{-8}$ with the canonical and $3.157\times10^{-9}$ with the refined step (check refined_free_spectra_convergence_order of `Revision/kohn_sham/reports/ks-rust-determinism.json`). Status: COMPUTED; Notebook 14b repeats the measurement (In [10]).

### 14.15 Example: Notebook 14b, the free spectra exact and numerical

Notebook 14b does Sections 14.12 to 14.14 with the computer. With sympy it checks the real form, the mirror map and the parities of the densities, the brane conditions, the boundary term, the tip family, the constant current, the exact solutions of Section 14.13 and the equation of the Pruefer angle, each against the verdict of the Revision record. With numpy it writes the shooting function of the Revision Rust solver in about forty lines (RK4 on the fine grid, the Pruefer angle followed step by step) with plain bisection on the labels (the Rust solver uses the safeguarded Newton-bisection of Section 14.14 instead), finds the 54 levels of the record and compares them with the exact levels and with the Rust numbers, repeats the fourth-order measurement, and compares the numerical orbitals with the exact ones. It draws six figures. It needs no Rust. It runs in about 40 seconds (two cells integrate the equation for hundreds of energies at once, 72 times over, and take 10 to 20 seconds each), and its last line is ALL 20 CHECKS PASSED (notebook 14b).

<!-- NOTEBOOK 14b -->

### 14.18 Line-by-line walk-through of Notebook 14b

The notebook has 15 code cells, In [1] to In [15]. As in Section 14.11, a line or a small group of lines is quoted and then explained; docstrings and the long caption texts are left out of the quotations (the captions are printed under the figures in Section 14.17).

**In [1], the set-up cell.** Its code is, line for line, the code of In [1] of Notebook 14a, which Section 14.11 explains, with one exception: the line

```python
NOTEBOOK_ID = "14b"  # this notebook: chapter 14, example b
```

gives this notebook its name, so that its figure files start with 14b and its captions go into the file `Revision/textbook/figures/14b.captions.json`. Its comment lines are the run instructions of Section 14.16. Out [1] is the line Set-up of notebook 14b complete.

**In [2], the real form.**

```python
import math  # exp, cos, sin of single numbers

import numpy as np  # floating-point arrays
import sympy as sp  # exact algebra with symbols
```

`math` is the module of Python for single numbers (square roots, $\pi$, sine, cosine ...); numpy computes with whole arrays of floating-point numbers at once; sympy computes exactly with symbols.

```python
PY_REPORT = "Revision/kohn_sham/reports/ks-theory-python.json"
WL_REPORT = "Revision/kohn_sham/reports/ks-theory-wolfram.json"
RUST_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
```

The names of three Revision reports: the sympy and the WolframScript checks of the theory, and the report of the Rust solver.

```python
def record_check(name, reports=(PY_REPORT, WL_REPORT)):
    verdicts = []
    for report in reports:
        data = json.loads(repository_file(report).read_text(encoding="utf-8"))
        found = [c["verdict"] for c in data["checks"] if c["name"] == name]
        verdicts.append(found[0] if found else "absent")
    return verdicts[0] == "PASS" and all(v in ("PASS", "absent") for v in verdicts)
```

The same idea as `record_check` of Notebook 14a, with one improvement: the reports to read are a parameter with a **default value** (`reports=(PY_REPORT, WL_REPORT)` is used when the call gives no second argument). A call can name other reports, for example `record_check("free_zero_mode_exact", (RUST_REPORT,))`; the comma after `RUST_REPORT` makes a **tuple** with one element. The function collects the verdict of the check `name` in every report (or the word absent) and returns true when the first report says PASS and every report says PASS or absent.

```python
s1 = sp.Matrix([[0, 1], [1, 0]])  # the Pauli matrices
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)
a, b, M, K, e, v = sp.symbols("a b M K epsilon v", real=True)
ok_all = True
```

The three Pauli matrices (in this notebook `s2` is $\sigma_2$), the $2 \times 2$ unit matrix, six real symbols ($a$, $b$, the mass $M$, $K = \kappa k$, $e$ for $\varepsilon$ and $v$) and a flag.

```python
for j in (1, -1):
    N = M * s3 - K * s2 + sp.I * j * (e - v) * s1  # the matrix of chi' = N chi
    derivative = sp.expand(N * sp.Matrix([a, sp.I * b]))  # N times (a, i b)
    a_prime = M * a - (K + j * (e - v)) * b  # the real form
    b_prime = (j * (e - v) - K) * a - M * b
    ok = (sp.expand(derivative[0] - a_prime) == 0
          and sp.expand(derivative[1] - sp.I * b_prime) == 0)
    ok_all &= ok
    say(f"j = {j:+d}: d chi/dy = N chi with chi = (a, i b) gives the real form: "
        f"{ok}")
```

For both block types: the matrix $N$; the product $N\chi$ for $\chi = (a, ib)$, multiplied out by `sp.expand`; the right sides of the real form of Section 14.12; and the test that the first entry of $N\chi$ is $a'$ and the second is $i b'$. The format `{j:+d}` prints the whole number $j$ with its sign ($+1$ or $-1$); two strings written next to each other are joined into one. Out [2] shows True twice.

```python
theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                    .read_text(encoding="utf-8"))
say("record: " + theory["blockEquation"]["realForm"])
check(ok_all, "the real form da/dy = M a - (K + j(eps - v)) b, "
      "db/dy = (j(eps - v) - K) a - M b")
```

The Revision theory record is read and its entry blockEquation.realForm is printed, so that the reader can compare it with the derived form (Out [2], third line); then the first PASS line.

**In [3], the boundary conditions.**

```python
y = sp.symbols("y", real=True)
H, a0, k = sp.symbols("H a0 k", real=True)
Mf = sp.Function("M", real=True)(y)  # a mass that depends on y
vf = sp.Function("v", real=True)(y)  # a potential that depends on y
kap = sp.exp(-H * y - a0)  # the momentum weight kappa(y)
```

Symbols for $y$, $H$, the slice $a_{4,0}$ (`a0`) and $k$, and two unknown real functions $M(y)$ and $v(y)$: everything below then holds for every mass profile and every potential, as in the self-consistent problem, not only for constants. `kap` is $\kappa(y)$.

```python
def N_of(j, M_, v_, kap_):
    return M_ * s3 - kap_ * k * s2 + sp.I * j * (e - v_) * s1
```

The matrix $N$ as a function of the block type, the mass, the potential and the weight.

```python
ok_mirror = True
for j in (1, -1):  # chi~(y) = s3 chi(-y) solves chi~' = -s3 N(-y) s3 chi~
    mirrored = -s3 * N_of(j, Mf.subs(y, -y), vf.subs(y, -y), kap.subs(y, -y)) * s3
    target = N_of(j, -Mf.subs(y, -y), vf.subs(y, -y), kap.subs(y, -y))
    ok_mirror &= sp.simplify(mirrored - target).is_zero_matrix
check(ok_mirror and record_check("bc_mirror_map_PA"),
      "the mirror map chi(y) -> sigma3 chi(-y) turns M(y) into -M(-y)",
      record=f"{PY_REPORT}, check bc_mirror_map_PA")
```

`subs(y, -y)` replaces $y$ by $-y$, so `Mf.subs(y, -y)` is $M(-y)$. `mirrored` is $-\sigma_3N(-y)\sigma_3$, the matrix of the equation that $\tilde\chi(y) = \sigma_3\chi(-y)$ solves (Section 14.12), and `target` is $N$ with the mass $-M(-y)$, the potential $v(-y)$ and the weight $\kappa(-y)$; they must be equal for both block types.

```python
even = {name: (s3 * X * s3 - X).is_zero_matrix
        for name, X in {"n": I2, "S": s2, "Q": s3, "current": s1}.items()}
say(f"even under the mirror map: {even}")
check(even == {"n": True, "S": False, "Q": True, "current": False}
      and record_check("bc_mirror_parities_of_densities"),
      "n and Q are even, S and the current odd: the mirror copy carries -m",
      record=f"{PY_REPORT}, check bc_mirror_parities_of_densities")
```

A **dictionary comprehension** (braces with `key: value for ...`): for each density and its $2 \times 2$ matrix (the number density with $1$, $S$ with $\sigma_2$, $Q$ with $\sigma_3$, the current with $\sigma_1$; `.items()` gives the pairs of a dictionary) the value is true when $\sigma_3X\sigma_3 = X$. That is the condition for the density to be even: the mirrored orbital has at $y$ the density $\chi(-y)^\dagger\sigma_3X\sigma_3\chi(-y)$, which equals the density of the original orbital at $-y$ exactly when $\sigma_3X\sigma_3 = X$. Out [3] prints the dictionary.

```python
c1f, c2f = sp.Function("chi1")(y), sp.Function("chi2")(y)
current = sp.expand((sp.Matrix([c1f, c2f]).H * s1 * sp.Matrix([c1f, c2f]))[0])
check(current.subs(c2f, 0) == 0 and current.subs(c1f, 0) == 0
      and record_check("bc_brane_parity_conditions"),
      "both brane parities (chi2(0) = 0 or chi1(0) = 0) kill the current",
      record=f"{PY_REPORT}, check bc_brane_parity_conditions")
```

Two unknown complex functions $\chi_1$, $\chi_2$; the current $\chi^\dagger\sigma_1\chi$ (a $1 \times 1$ matrix, whose single entry is `[0]`); putting $\chi_2 = 0$ (even parity) or $\chi_1 = 0$ (odd parity) makes it zero.

```python
phi = sp.Matrix([sp.Function("phi1")(y), sp.Function("phi2")(y)])
chi = sp.Matrix([c1f, c2f])
ok_adjoint = True
for j in (1, -1):
    def h_on(w, j=j):  # h_j applied to the column w
        return j * (-sp.I * s1 * sp.diff(w, y) + Mf * s2 * w + kap * k * s3 * w) \
            + vf * w
    difference = (phi.H * h_on(chi))[0] - (h_on(phi).H * chi)[0]
    boundary = sp.diff(-sp.I * j * (phi.H * s1 * chi)[0], y)
    ok_adjoint &= sp.simplify(sp.expand(difference - boundary)) == 0
check(ok_adjoint and record_check("bc_self_adjoint_boundary_term"),
      "phi^dag h chi - (h phi)^dag chi = d/dy[-i j phi^dag sigma1 chi]",
      record=f"{PY_REPORT}, check bc_self_adjoint_boundary_term")
```

Two columns of unknown functions $\varphi$ and $\chi$. Inside the loop, `h_on(w)` applies $h_j = j[-i\sigma_1\,d/dy + M\sigma_2 + \kappa k\sigma_3] + v$ to a column; the argument `j=j` stores the current value of `j` in the function (a function defined in a loop otherwise reads the loop variable only when it is called). `difference` is $\varphi^\dagger h_j\chi - (h_j\varphi)^\dagger\chi$, `boundary` is $\frac{d}{dy}[-ij\varphi^\dagger\sigma_1\chi]$; they must be equal (Section 14.12).

```python
th = sp.symbols("theta", real=True)
Q = sp.cos(th) * s3 + sp.sin(th) * s2  # the tip family
check(sp.simplify(Q * Q - I2).is_zero_matrix and Q.H == Q
      and sp.simplify(Q * s1 + s1 * Q).is_zero_matrix and record_check("bc_tip_family"),
      "the tip family Q(theta): Q^dag = Q, Q^2 = 1, Q sigma1 = -sigma1 Q",
      record=f"{PY_REPORT}, check bc_tip_family")
```

The three facts of the tip family: $Q^2 = 1$, $Q^\dagger = Q$, $Q\sigma_1 + \sigma_1Q = 0$.

```python
kp = sp.symbols("kappa", positive=True)
ok_current = True
for j in (1, -1):
    Nn = M * s3 - kp * k * s2 + sp.I * j * (e - v) * s1
    ok_current &= sp.simplify(Nn.H * s1 + s1 * Nn).is_zero_matrix
    density_changes = not sp.simplify(Nn.H + Nn).is_zero_matrix
check(ok_current and density_changes and record_check("bc_current_conserved_along_y"),
      "the current is constant along y on every solution, the density is not",
      record=f"{PY_REPORT}, check bc_current_conserved_along_y")
```

For both types: $N^\dagger\sigma_1 + \sigma_1N = 0$ (the current is constant) and $N^\dagger + N \ne 0$ (the density is not). The variable `density_changes` is set anew in each pass; the check uses the value of the last pass, $j = -1$, which is the same as for $j = +1$. Out [3] shows six PASS lines.

**In [4], the exact solutions and the record.**

```python
Lc = sp.symbols("L", positive=True)
n_int = sp.symbols("n", integer=True, positive=True)
ok_exact = sp.simplify(sp.diff(sp.exp(M * y), y) - M * sp.exp(M * y)) == 0  # step 5
```

The symbol $L$ (named `Lc` because the plain name `L` is used for numbers below) and a positive whole number $n$. The first test is the zero mode: the derivative of $e^{My}$ is $Me^{My}$, so $a = e^{My}$ solves $a' = Ma$ (step 5 of the notebook's section 7 is Step 2 of Section 14.13, case $\varepsilon = 0$).

```python
for j in (1, -1):  # step 4: b = sin(n pi y/L), a = (b' + M b)/(j eps)
    p_n = n_int * sp.pi / Lc
    eps_n = sp.sqrt(M ** 2 + p_n ** 2)
    b_n = sp.sin(p_n * y)
    a_n = (sp.diff(b_n, y) + M * b_n) / (j * eps_n)
    ok_exact &= sp.simplify(sp.diff(a_n, y) - (M * a_n - j * eps_n * b_n)) == 0
    ok_exact &= b_n.subs(y, 0) == 0 and sp.simplify(b_n.subs(y, -Lc)) == 0
```

The even levels of Step 2: $b = \sin(n\pi y/L)$, $a = (b' + Mb)/(j\varepsilon_n)$. The second equation of the real form, $b' = j\varepsilon a - Mb$, holds by the construction of $a$; the loop checks the first one, $a' = Ma - j\varepsilon b$, and the two conditions $b(0) = 0$ and $b(-L) = \sin(-n\pi) = 0$ (sympy knows that the sine of a whole multiple of $\pi$ is zero, because $n$ was declared a whole number).

```python
p = sp.symbols("p", positive=True)  # step 6 (j = +1)
b_odd = sp.sin(p * (y + Lc))
eps_odd = sp.sqrt(M ** 2 + p ** 2)
a_odd = (sp.diff(b_odd, y) + M * b_odd) / eps_odd
ok_exact &= sp.simplify(sp.diff(a_odd, y) - (M * a_odd - eps_odd * b_odd)) == 0
ok_exact &= sp.simplify(a_odd.subs(y, 0) * eps_odd
                        - (p * sp.cos(p * Lc) + M * sp.sin(p * Lc))) == 0
check(ok_exact and record_check("bc_exact_k0_spectra"),
      "the zero mode, the even levels and the odd condition tan(pL) = -p/M",
      record=f"{PY_REPORT}, check bc_exact_k0_spectra")
```

The odd levels of Step 3 for $j = +1$: $b = \sin(p(y + L))$ vanishes at $y = -L$; $a$ is built as before; the first equation is checked; and $\varepsilon\,a(0) = p\cos(pL) + M\sin(pL)$, so $a(0) = 0$ is exactly the condition $f(p) = 0$.

```python
def odd_roots(m, L, count):
    roots = []
    for n in range(count):
        lo, hi = (n + 0.5) * math.pi / L, (n + 1.0) * math.pi / L
        f = lambda q: m * math.sin(q * L) + q * math.cos(q * L)
        f_lo = f(lo)
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if mid <= lo or mid >= hi:  # the interval cannot shrink any more
                break
            if (f(mid) > 0.0) == (f_lo > 0.0):
                lo = mid
            else:
                hi = mid
        roots.append(0.5 * (lo + hi))
    return roots
```

The first `count` roots of $f(p) = m\sin(pL) + p\cos(pL)$ by **bisection**, one in each interval of Step 4. `f` is the function as a `lambda`; `f_lo` its value at the left end. The inner loop runs at most 200 times (the name `_` is used for a loop counter whose value is not needed); it stops earlier when the midpoint is no longer strictly inside the interval, which happens when the two ends are neighbouring floating-point numbers. If $f$ has the same sign at the midpoint as at the left end, the root lies in the right half and `lo` moves to the midpoint; otherwise `hi` does. (The sign at the left end never changes, because `lo` only moves to points of the same sign.)

```python
def exact_level(m, L, parity, label):
    if parity == "even":
        if label == 0:
            return 0.0
        return math.copysign(math.sqrt(m * m + (label * math.pi / L) ** 2), label)
    roots = odd_roots(m, L, 6)
    if label >= 0:
        return math.sqrt(m * m + roots[label] ** 2)
    return -math.sqrt(m * m + roots[-label - 1] ** 2)
```

The exact level of a given parity and label, in the label convention of Section 14.13. `math.copysign(x, label)` is the size of $x$ with the sign of the label.

```python
CASES = [(1.0, 3.0), (1.0, 2.0), (2.0, 3.0)]  # (m, L)
LABELS = list(range(-3, 6))  # the labels -3 ... 5
record_rows = repository_file(
    "Revision/kohn_sham/results/spectrum/free-k0-analytic.csv"
).read_text(encoding="utf-8").splitlines()
header = record_rows[0].split(",")
record = [dict(zip(header, row.split(","))) for row in record_rows[1:]]
```

The three cases $(m, L)$ and the nine labels: with two parities, $3 \times 9 \times 2 = 54$ levels. The record of the Rust solver is a CSV file with the columns m, L, parity, label, eps_numeric, eps_analytic and difference; each row becomes a dictionary from column name to text, as in In [18] of Notebook 14a.

```python
exact = {}  # (m, L, parity, label) -> exact level
for m_, L_ in CASES:
    for label in LABELS:
        for parity in ("even", "odd"):
            exact[(m_, L_, parity, label)] = exact_level(m_, L_, parity, label)
worst = max(abs(exact[(float(r["m"]), float(r["L"]), r["parity"], int(r["label"]))]
                - float(r["eps_analytic"])) for r in record)
```

A dictionary whose keys are tuples $(m, L, \text{parity}, \text{label})$ holds the 54 exact levels. `worst` is the largest difference between them and the column eps_analytic of the record (each text is turned into a number with `float` or `int`).

```python
say(f"(m, L) = (1, 3): odd roots p = "
    + ", ".join(f"{q:.6f}" for q in odd_roots(1.0, 3.0, 3)) + ", ...")
lowest_odd = exact[(1.0, 3.0, "odd", 0)]  # the lowest odd level, m = 1, L = 3
lowest_even = exact[(1.0, 3.0, "even", 1)]  # the lowest positive even level
report("lowest odd level for m = 1, L = 3", f"{lowest_odd:.12f}", "m")
report("lowest positive even level for m = 1, L = 3", f"{lowest_even:.12f}", "m")
check(len(record) == 54 and worst < 1e-12,
      "the 54 exact levels equal the column eps_analytic of the record",
      record="Revision/kohn_sham/results/spectrum/free-k0-analytic.csv, eps_analytic")
```

`", ".join(...)` joins the three roots, each written with 6 decimals, into one text separated by commas. Then the two RESULT lines, $1.292292828069\,m$ and $1.447971930402\,m$, and the check that the record has 54 rows that agree with the exact levels to better than $10^{-12}$. Out [4] shows two PASS lines.

**In [5], figure 1.**

```python
p_values = np.linspace(0.0, 7.0, 1401)
f_values = 1.0 * np.sin(3.0 * p_values) + p_values * np.cos(3.0 * p_values)
roots_13 = odd_roots(1.0, 3.0, 6)
fig, ax = plt.subplots(figsize=(8.0, 4.0))
for n in range(6):  # the intervals in which the roots lie
    ax.axvspan((n + 0.5) * math.pi / 3.0, (n + 1.0) * math.pi / 3.0, color="C0",
               alpha=0.08)
```

1401 values of $p$ from 0 to 7, the function $f(p)$ for $M = 1$, $L = 3$, and its first six roots. `axvspan(x1, x2, ...)` shades the vertical strip between $x_1$ and $x_2$; `alpha=0.08` makes it almost transparent. The six strips are the intervals $((n + \tfrac12)\pi/3, (n + 1)\pi/3)$.

```python
ax.plot(p_values, f_values, color="C0", label="$f(p) = M\\sin(pL) + p\\cos(pL)$")
ax.plot(roots_13, [0.0] * 6, "o", color="C3", label="roots $p_0, p_1, \\dots$")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("$p$ (wave number along $y$, units of $H$)")
ax.set_ylabel("$f(p)$")
ax.set_title("the odd-parity condition $\\tan(pL) = -p/M$ for $M = 1$, $L = 3$")
ax.legend(fontsize=8, loc="lower left")
save_figure(fig, "odd_condition",
            "The odd-parity level condition for $M = 1$ and $L = 3$: the function "
            ...)
```

The curve, the six roots as red dots on the axis (`[0.0] * 6` is a list of six zeros; the format string `"o"` draws dots without a line), the horizontal axis line, labels, title, legend and saving. **What figure 14b.1 shows.** The function $f(p)$ oscillates with a growing amplitude (the term $p\cos(pL)$ grows with $p$). It starts at $f(0) = 0$, which is not a level ($p = 0$ gives $b = 0$), and crosses zero once in every shaded strip and nowhere else, at $p_0 = 0.8185$, $p_1 = 1.744$, $p_2 = 2.735$, ... as Step 4 of Section 14.13 proved; each crossing is a pair of odd levels $\pm\sqrt{1 + p_n^2}$.

**In [6], the Pruefer angle and the shooting tools.**

```python
r_s, t_s = sp.symbols("r t", positive=True)  # polar coordinates of (a, b)
a_p = r_s * sp.cos(t_s)
b_p = r_s * sp.sin(t_s)
j_s = sp.symbols("j")
num = a_p * ((j_s * e - K) * a_p - M * b_p) - b_p * (M * a_p - (K + j_s * e) * b_p)
pruefer = j_s * e - K * sp.cos(2 * t_s) - M * sp.sin(2 * t_s)
check(sp.simplify(num / r_s ** 2 - pruefer) == 0,
      "d theta/dy = j(eps - v) - K cos 2theta - M sin 2theta")
```

The point $(a, b) = (r\cos\theta, r\sin\theta)$ with symbols $r$ and $\theta$ (`t_s`), a symbol $j$, the expression $ab' - ba'$ with the real form inserted (`num`, written with $v = 0$, so that $e$ stands for $\varepsilon - v$), and the claimed $\theta'$. The check: $(ab' - ba')/r^2$ equals it (Section 14.14).

```python
def shoot(eps, k=0.0, j=1.0, M=1.0, L=3.0, G=900, H=1.0, a4=0.0, tip=0.0,
          keep=False):
    eps, k, j = np.broadcast_arrays(np.asarray(eps, dtype=float),
                                    np.asarray(k, dtype=float),
                                    np.asarray(j, dtype=float))
```

`shoot` integrates the real form from the tip to the brane for many energies at once and returns $\Phi = j\theta(0)$. Its parameters have default values (the canonical $M = 1$, $L = 3$, $G = 900$, $H = 1$, slice 0, tip angle 0), so a call can name only what differs. `np.asarray` turns a single number or a list into a numpy array; `np.broadcast_arrays` brings the arrays to a common shape (a single number is repeated), so that `eps`, `k` and `j` may each be one number or an array of the same length.

```python
    nf = 2 * G + 1  # the fine grid: nodes and step midpoints
    y_fine = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))
    e_minus_Hy = np.exp(-H * y_fine)  # e^(-Hy) on the fine grid
    kk = k * np.exp(-a4)  # k e^(-a4,0): kappa k = kk e^(-Hy)
    h = L / G
```

The fine grid of $2G + 1$ points from $y = -L$ to $y = 0$ (`np.arange(nf)` is $0, 1, \dots, 2G$, so the first point is $-L$ and the last $0$); $e^{-Hy}$ on it; the redshifted momentum $ke^{-a_{4,0}}$, so that $K = \kappa k$ is `kk` times $e^{-Hy}$; and the step $h = L/G$.

```python
    a_ = np.full(eps.shape, math.cos(0.5 * tip))  # the tip condition
    b_ = np.full(eps.shape, math.sin(0.5 * tip))
    theta = np.full(eps.shape, 0.5 * tip)
    raw = np.arctan2(b_, a_)
    je = j * eps
    path = [(theta, a_, b_)]
```

The starting point $(a, b) = (\cos\tfrac\theta2, \sin\tfrac\theta2)$ for every energy (`np.full(shape, value)` is an array filled with one value), the starting angle $\theta(-L) = \theta_{\rm tip}/2$, `raw`, the angle as `np.arctan2` returns it (between $-\pi$ and $\pi$), the products $j\varepsilon$, and a list that will keep the path when it is asked for.

```python
    for i in range(G):
        K0, K1, K2 = (kk * e_minus_Hy[2 * i], kk * e_minus_Hy[2 * i + 1],
                      kk * e_minus_Hy[2 * i + 2])  # K at y, y + h/2, y + h
        p1a, p1b = M * a_ - (K0 + je) * b_, (je - K0) * a_ - M * b_
        a2, b2 = a_ + 0.5 * h * p1a, b_ + 0.5 * h * p1b
        p2a, p2b = M * a2 - (K1 + je) * b2, (je - K1) * a2 - M * b2
        a3, b3 = a_ + 0.5 * h * p2a, b_ + 0.5 * h * p2b
        p3a, p3b = M * a3 - (K1 + je) * b3, (je - K1) * a3 - M * b3
        a4_, b4_ = a_ + h * p3a, b_ + h * p3b
        p4a, p4b = M * a4_ - (K2 + je) * b4_, (je - K2) * a4_ - M * b4_
        a_ = a_ + h / 6.0 * (p1a + 2.0 * p2a + 2.0 * p3a + p4a)
        b_ = b_ + h / 6.0 * (p1b + 2.0 * p2b + 2.0 * p3b + p4b)
```

One RK4 step per pass, for all energies at once. Step $i$ goes from the node $2i$ of the fine grid to the node $2i + 2$; `K0`, `K1`, `K2` are $K$ at its start, its midpoint and its end. The four slopes of RK4 (Chapter 2): `p1` at the start, `p2` at the midpoint with half a step along `p1`, `p3` at the midpoint with half a step along `p2`, `p4` at the end with a whole step along `p3`; each slope is the right side of the real form, $(Ma - (K + j\varepsilon)b,\ (j\varepsilon - K)a - Mb)$, with $v = 0$. The new point adds $h/6$ times the weighted sum with the weights $1, 2, 2, 1$. (The name `a4_` with a final underscore is the trial point of the fourth slope; `a4` without it is the slice.)

```python
        new = np.arctan2(b_, a_)
        step = new - raw  # the change of the angle, brought into (-pi, pi]
        step = np.where(step > np.pi, step - 2 * np.pi,
                        np.where(step <= -np.pi, step + 2 * np.pi, step))
        theta = theta + step
        raw = new
        if keep:
            path.append((theta, a_, b_))
```

Following the angle continuously: the change of the raw angle over one step is brought into the interval from $-\pi$ to $\pi$ (`np.where(condition, x, y)` takes `x` where the condition holds and `y` elsewhere; a jump of almost $2\pi$ of the raw angle is the passage through $\pm\pi$, not a real turn) and added to `theta`. The step is so small that the true change of the angle over one step is much less than $\pi$. With `keep=True` the angle and the point after every step are stored.

```python
    if keep:
        return j * theta, [np.array(q) for q in zip(*path)]
    return j * theta
```

The result is $\Phi = j\theta(0)$. With `keep=True` also the paths: `zip(*path)` regroups the list of triples $(\theta, a, b)$ into three sequences, each turned into an array with one row per node ($G + 1$ rows) and one column per energy.

```python
def target(parity, label):
    offset = np.where(np.asarray(parity) == "even", 0.0, 0.5 * np.pi)
    return offset + np.asarray(label, dtype=float) * np.pi
```

The value of $\Phi$ at a level: $l\pi$ for even parity and $\pi/2 + l\pi$ for odd parity, for arrays of parities and labels.

```python
def levels(k, j, parity, label, iterations=72, **options):
    k, j, parity, label = np.broadcast_arrays(
        np.asarray(k, dtype=float), np.asarray(j, dtype=float),
        np.asarray(parity), np.asarray(label))
    goal = target(parity, label)
    lo, hi = np.full(k.shape, -20.0), np.full(k.shape, 20.0)
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        g = shoot(mid, k, j, **options) - goal
        lo = np.where(g <= 0.0, mid, lo)  # g = 0: an exact level
        hi = np.where(g >= 0.0, mid, hi)
    return 0.5 * (lo + hi)
```

The levels with given momenta, block types, parities and labels, all at once, by 72 bisections of $[-20, 20]$ (Section 14.14). `**options` collects any further named arguments (for example `M=2.0` or `G=1800`) and hands them on to `shoot`. In each pass $\Phi$ is computed at the midpoints; where it is at or below the target, the level lies above the midpoint and `lo` moves there; where it is at or above, `hi` moves there. If $\Phi$ equals the target exactly, both ends move to the midpoint and the level is found exactly; this is what happens for the zero mode (In [8]).

```python
say("defined: shoot(eps, k, j, M, L, G, ...) and levels(k, j, parity, label, ...)")
```

Out [6]: the PASS line of the angle equation and this line.

**In [7], the shooting function and figure 2.**

```python
trial = np.linspace(-4.0, 4.0, 801)  # 801 trial energies
phi_curve = shoot(trial, 0.0, 1.0)  # Phi for k = 0, j = +1 (both parities)
grows = bool(np.all(np.diff(phi_curve) > 0.0))
grows_k = all(bool(np.all(np.diff(shoot(np.linspace(-4.0, 3.96, 200), 0.75, jj)) > 0))
              for jj in (1.0, -1.0))
check(grows and grows_k,
      "Phi(eps) grows strictly with eps (k = 0 and k = 0.75, both block types)")
```

$\Phi(\varepsilon)$ at 801 energies from $-4$ to $4$ in one call. `np.diff` gives the differences of neighbouring values; `np.all(... > 0.0)` is true when every difference is positive, that is when $\Phi$ grows strictly; `bool` turns numpy's answer into a plain true or false. The same test for $k = 0.75$, 200 energies and both block types. One PASS line: the monotonicity proved in Section 14.14, seen numerically.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
ax.plot(trial, phi_curve / np.pi, color="C0", label="$\\Phi(\\varepsilon)/\\pi$")
for label in range(-3, 4):  # the targets in units of pi
    ax.axhline(label, color="C1", linewidth=0.7)
    ax.axhline(label + 0.5, color="C2", linewidth=0.7, linestyle="--")
```

The curve $\Phi/\pi$ and the targets: solid lines at the whole numbers (even), dashed lines at the half numbers (odd).

```python
even_levels = [exact[(1.0, 3.0, "even", l)] for l in range(-2, 3)]
odd_levels = [exact[(1.0, 3.0, "odd", l)] for l in range(-2, 2)]
ax.plot(even_levels, range(-2, 3), "o", color="C1",
        label="even levels: $\\Phi = l\\pi$")
ax.plot(odd_levels, [l + 0.5 for l in range(-2, 2)], "s", color="C2",
        label="odd levels: $\\Phi = \\pi/2 + l\\pi$")
```

The exact levels of the labels $-2$ to $2$ (even) and $-2$ to $1$ (odd), drawn as circles and squares at the heights of their targets.

```python
ax.set_xlabel("trial energy $\\varepsilon$ (units of $m$)")
ax.set_ylabel("$\\Phi(\\varepsilon) / \\pi$")
ax.set_title("the shooting function for $k = 0$, $j = +1$, $m = 1$, $L = 3$")
ax.legend(fontsize=8, loc="upper left")
save_figure(fig, "shooting_function",
            "The shooting function $\\Phi(\\varepsilon) = j\\,\\theta(0)$ (the "
            ...)
```

**What figure 14b.2 shows.** The curve rises from about $-3.6$ to $+3.6$ (in units of $\pi$) as the trial energy goes from $-4$ to $4$, never falling. Every circle and square sits exactly on the curve where it crosses its target line: the crossings are the levels, one per label. Between $-1$ and $1$ the curve is almost flat and crosses only the line $0$, at $\varepsilon = 0$: the gap $(-M, M)$ contains only the zero mode. Where the levels are dense, the curve is steep.

**In [8], all 54 levels.**

```python
numeric = {}  # (m, L, parity, label) -> numerical level at the canonical step
for m_, L_ in CASES:
    pars = np.array([p_ for l_ in LABELS for p_ in ("even", "odd")])
    labs = np.array([l_ for l_ in LABELS for p_ in ("even", "odd")])
    found = levels(0.0, 1.0, pars, labs, M=m_, L=L_, G=round(900 * L_ / 3))
    for p_, l_, x in zip(pars, labs, found):
        numeric[(m_, L_, str(p_), int(l_))] = float(x)
```

For each case, the 18 parities and labels as two arrays (the double list comprehension runs over the labels and, for each, over the two parities), and the 18 levels found in one call with $k = 0$, $j = +1$, the mass $m$, the cutoff $L$ and $G = 900L/3$ steps ($900$ for $L = 3$, $600$ for $L = 2$: always the step $h = 1/300$ of the Rust solver). `round` gives the nearest whole number. The levels go into the dictionary `numeric`.

```python
say("m = 1, L = 3:  label  even (numerical)   even (exact)    "
    "odd (numerical)    odd (exact)")
for l_ in LABELS:
    row = [numeric[(1.0, 3.0, "even", l_)], exact[(1.0, 3.0, "even", l_)],
           numeric[(1.0, 3.0, "odd", l_)], exact[(1.0, 3.0, "odd", l_)]]
    say(f"               {l_:+d}   " + "  ".join(f"{x:15.10f}" for x in row))
```

A table of the case $m = 1$, $L = 3$: for each label the numerical and exact levels of both parities, each printed in 15 places with 10 decimals (`{x:15.10f}`).

```python
rust_diff = max(abs(numeric[(float(r["m"]), float(r["L"]), r["parity"],
                             int(r["label"]))] - float(r["eps_numeric"]))
                for r in record)
report("largest difference from the Rust solver's levels", f"{rust_diff:.1e}", "m")
check(rust_diff < 1e-11,
      "the 54 numerical levels equal those of the Rust solver",
      record="Revision/kohn_sham/results/spectrum/free-k0-analytic.csv, eps_numeric")
```

The largest difference between the notebook's numerical levels and the Rust solver's (column eps_numeric), printed as a RESULT line with one decimal (`.1e`). The two programs integrate the same RK4 discretisation and look for the roots of the same shooting function $\Phi$; they differ only in the root finder (plain bisection to the last digit here, the safeguarded Newton-bisection with the tolerance $10^{-13}$ in the Rust solver, Section 14.14) and in rounding. The check requires agreement to $10^{-11}$; Out [8] shows the difference $7.1\times10^{-15}\,m$.

```python
errors = {key: abs(numeric[key] - exact[key]) for key in numeric}
low = max(err for key, err in errors.items() if abs(exact[key]) < 4.0)
high = max(err for key, err in errors.items() if abs(exact[key]) >= 4.0)
report("largest error for |eps| < 4 m", f"{low:.2e}", "m")
report("largest error for |eps| >= 4 m", f"{high:.2e}", "m")
```

The errors against the exact levels, and the largest of them below and above $|\varepsilon| = 4m$, printed with two decimals (`.2e`). The Rust check free_k0_analytic_spectra measured the same two numbers; the next lines read them from its record.

```python
import re  # regular expressions: patterns that find numbers in a text


def record_detail(name, report_file):
    """The detail text of the check called name in a Revision report."""
    data = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
    return [c["detail"] for c in data["checks"] if c["name"] == name][0]
```

`re` is Python's module for **regular expressions**, patterns that describe pieces of text. `record_detail` reads a report as `record_check` does (In [2]), keeps the checks with the given name and returns the detail text of the first, the sentence in which the record states its numbers. The argument is called `report_file` and not `report`, so that inside the function it does not hide the helper `report` of the set-up cell.

```python
detail = record_detail("free_k0_analytic_spectra", RUST_REPORT)
rec_low, tol_low, rec_high, tol_high = re.findall(r"\d+(?:\.\d+)?e-\d+", detail)
check(f"{low:.2e}" == f"{float(rec_low):.2e}"
      and f"{high:.2e}" == f"{float(rec_high):.2e}"
      and low < float(tol_low) and high < float(tol_high)
      and record_check("free_k0_analytic_spectra", (RUST_REPORT,)),
      f"largest errors {low:.2e} for |eps| < 4 m and {high:.2e} above, as in the "
      f"record, below its tolerances {tol_low} and {tol_high}",
      record=f"{RUST_REPORT}, check free_k0_analytic_spectra")
```

The detail of the Rust check ends with the words

```text
max |difference| 7.23e-10 for |eps| < 4 m (tolerance 5e-9, RK4 error ~ (h eps)^4),
5.05e-8 for 4 m <= |eps| < 7 m (tolerance 3e-7)
```

(one line in the record). The pattern `\d+(?:\.\d+)?e-\d+` describes a number with a negative power of ten: one or more digits (`\d+`), then, if present, a point and more digits (the group `(?:\.\d+)` followed by `?`, which makes it optional), then `e-` and digits; the `r` before the string keeps the backslashes as they are. `re.findall` returns every piece of the text that fits the pattern, in order: the texts `7.23e-10`, `5e-9`, `5.05e-8` and `3e-7`, which are unpacked into the four names (if the record ever stated a different number of such numbers, the unpacking would fail and the notebook would stop). The check requires: the notebook's two largest errors, written with two decimals, equal the record's, written the same way (`float` turns a text into a number, so the record's `5.05e-8` is written `5.05e-08`); both lie below the record's tolerances; and the record's verdict is PASS. Because the numbers are read from the record, the check fails if the record is ever recomputed with different results.

```python
check(all(numeric[(m_, L_, "even", 0)] == 0.0 for m_, L_ in CASES),
      "the brane zero mode comes out as exactly eps = 0")
```

The last check: the zero mode is exactly 0 in all three cases. Why exactly: the first midpoint of the bisection is $\varepsilon = 0$; there, with $k = 0$ and the start $b = 0$, every RK4 slope of $b$ is exactly zero, so $b$ stays exactly 0, the angle stays exactly 0, $\Phi - $ target is exactly 0, and both ends of the interval jump to 0. Out [8] shows the table, three RESULT lines and three PASS lines: the largest difference from the Rust levels $7.1\times10^{-15}$, and the largest errors $7.23\times10^{-10}$ below $4m$ and $5.05\times10^{-8}$ above, the numbers of the record. In the table the numerical and exact levels agree in all 10 printed decimals for the even labels $-2$ to $2$ and the odd labels $-1$ and $0$; the odd labels $-2$, $1$ and $2$ differ by one unit in the 10th decimal (for example $2.0106285601$ against $2.0106285600$ for the odd label 1), and the higher labels differ in the 8th to 10th decimal (for example $5.3306254627$ against $5.3306254587$ for the even label 5): the error grows with the level, because the orbital oscillates faster.

**In [9], figure 3.**

```python
fig, ax = plt.subplots(figsize=(8.0, 5.0))
for position, (m_, L_) in enumerate(CASES):
    x0 = 3.0 * position  # the horizontal place of this ladder
    for l_ in LABELS:
        for shift, parity, color, marker in ((0.0, "even", "C0", "o"),
                                             (1.2, "odd", "C1", "s")):
            level = exact[(m_, L_, parity, l_)]
            ax.plot([x0 + shift - 0.4, x0 + shift + 0.4], [level, level],
                    color=color, linewidth=1.5)
            ax.plot([x0 + shift], [numeric[(m_, L_, parity, l_)]], marker,
                    color=color, markersize=4)
    ax.fill_between([x0 - 0.5, x0 + 1.7], -m_, m_, color="gray", alpha=0.12)
```

For each case a **level ladder** at the horizontal place $x_0 = 0, 3, 6$: every exact level is a short horizontal line (from $x_0 + \text{shift} - 0.4$ to $x_0 + \text{shift} + 0.4$), even parity at the left and odd parity $1.2$ further right, and the numerical level is a marker in its middle. `fill_between(x, y1, y2)` shades the band from $-m$ to $m$ across the ladder.

```python
ax.set_xlim(-0.6, 8.4)
ax.set_ylim(-7.0, 9.5)
ax.set_xticks([0.6, 3.6, 6.6])
ax.set_xticklabels(["$m = 1$, $L = 3$", "$m = 1$, $L = 2$", "$m = 2$, $L = 3$"])
ax.plot([], [], "o-", color="C0", label="even parity (line exact, dot numerical)")
ax.plot([], [], "s-", color="C1", label="odd parity (line exact, square numerical)")
ax.set_ylabel("level $\\varepsilon$ (units of $H = 1$)")
ax.set_title("the free $k = 0$ spectra, labels $-3$ to $5$")
ax.legend(fontsize=8, loc="lower right")
save_figure(fig, "spectrum_ladder",
            "The free $k = 0$ spectra for the three cases $(m, L) = (1, 3)$, "
            ...)
```

The ranges of the axes, the names of the three ladders under them, and two empty plots (`ax.plot([], [], ...)` draws nothing) whose only purpose is to put the two styles into the legend. **What figure 14b.3 shows.** Three ladders. In each, the shaded band from $-m$ to $m$ contains only the even zero mode at 0. For $m = 2$ the band is twice as wide and the lowest levels move out with it; for $L = 2$ the levels are farther apart than for $L = 3$, because the wave numbers $n\pi/L$ are larger. The even and odd levels alternate. On this scale every marker sits exactly on its line.

**In [10], fourth-order convergence.**

```python
refined = {}
for m_, L_ in CASES:
    pars = np.array([p_ for l_ in LABELS for p_ in ("even", "odd")])
    labs = np.array([l_ for l_ in LABELS for p_ in ("even", "odd")])
    found = levels(0.0, 1.0, pars, labs, M=m_, L=L_, G=round(1800 * L_ / 3))
    for p_, l_, x in zip(pars, labs, found):
        refined[(m_, L_, str(p_), int(l_))] = float(x)
refined_errors = {key: abs(refined[key] - exact[key]) for key in refined}
```

The same 54 levels with twice as many steps ($G = 1800$ for $L = 3$, $1200$ for $L = 2$, the refined run of the Revision solver) and their errors.

```python
ratios = sorted(errors[key] / refined_errors[key] for key in errors
                if errors[key] > 1e-11 and refined_errors[key] > 0.0)
median = ratios[len(ratios) // 2]
```

For every level whose canonical error is above $10^{-11}$ (smaller errors are dominated by rounding), the ratio of the canonical to the refined error, sorted. The **median** is the middle value of the sorted list: `len(ratios) // 2` is the position of the middle (`//` divides and drops the remainder; with 39 ratios it is the 20th value, position 19 counting from 0).

```python
report("number of levels with a canonical error above 1e-11", len(ratios))
report("median error ratio canonical / refined", f"{median:.2f}")
report("largest error, canonical step", f"{max(errors.values()):.3e}", "m")
report("largest error, refined step", f"{max(refined_errors.values()):.3e}", "m")
```

Four RESULT lines: the number of ratios, the median ratio with two decimals, and the largest canonical and refined errors with three decimals and an exponent (`f"{x:.3e}"`).

```python
DETERMINISM = "Revision/kohn_sham/reports/ks-rust-determinism.json"
detail = record_detail("refined_free_spectra_convergence_order", DETERMINISM)
rec_canonical, rec_refined = re.search(r"canonical (\S+), refined (\S+);",
                                       detail).groups()
rec_median, rec_count = re.search(r"ratio (\S+) over (\d+) levels",
                                  detail).groups()
```

The detail text of the record's check, read with `record_detail` of In [8], is

```text
analytic k = 0 spectra: max error canonical 5.050e-08, refined 3.157e-09; median
error ratio 16.00 over 39 levels (RK4 order 4 predicts 16)
```

(one line in the record). `re.search` finds the first place where a pattern fits, and `.groups()` returns the pieces of text matched by the bracketed parts of the pattern: `\S+` is one or more characters that are not spaces, `\d+` one or more digits. So the first pattern picks out the texts `5.050e-08` and `3.157e-09` (the words "canonical" and "refined", the comma and the semicolon fix where they stand), and the second the texts `16.00` and `39`. If the record's sentence had another form, `re.search` would find nothing, return `None`, and `.groups()` would stop the notebook with an error.

```python
check(len(ratios) == int(rec_count) and f"{median:.2f}" == rec_median
      and f"{max(errors.values()):.3e}" == rec_canonical
      and f"{max(refined_errors.values()):.3e}" == rec_refined
      and record_check("refined_free_spectra_convergence_order", (DETERMINISM,)),
      f"{len(ratios)} levels, median error ratio {median:.2f}, largest errors "
      f"{max(errors.values()):.3e} and {max(refined_errors.values()):.3e}",
      record=f"{DETERMINISM}, check refined_free_spectra_convergence_order")
```

The check that the notebook's four numbers equal the record's: 39 levels (`int` turns the text into a whole number), the median ratio 16.00 (RK4's $2^4 = 16$), and the largest errors $5.050\times10^{-8}$ and $3.157\times10^{-9}$. The comparison is made on the printed texts, written in the same form as the record writes them, and the numbers come from the record itself, so a recomputed record with other numbers would make the check fail. The name of the check is built from the notebook's own numbers.

**In [11], figure 4.**

```python
chosen = [("even", 1), ("even", 3), ("odd", 0), ("odd", 3)]
steps = [150, 300, 600, 900, 1800]
curves = {key: [] for key in chosen}
for G_ in steps:
    found = levels(0.0, 1.0, np.array([p_ for p_, l_ in chosen]),
                   np.array([l_ for p_, l_ in chosen]), M=1.0, L=3.0, G=G_)
    for key, x in zip(chosen, found):
        curves[key].append(abs(float(x) - exact[(1.0, 3.0) + key]))
```

Four levels and five step numbers; for each step number the four levels in one call, and their errors appended to four lists. `(1.0, 3.0) + key` joins two tuples into the key $(1, 3, \text{parity}, \text{label})$.

```python
h_values = np.array([3.0 / G_ for G_ in steps])
fig, ax = plt.subplots(figsize=(7.0, 4.6))
for (parity, label), errs in curves.items():
    ax.loglog(h_values, errs, "o-", label=f"{parity}, label {label}")
ax.loglog(h_values, 3e-2 * h_values ** 4, ":", color="black",
          label="slope 4: error $\\propto h^4$")
```

The steps $h = 3/G$; `loglog` draws with logarithmic axes in both directions, on which a power law $h^4$ is a straight line of slope 4; the dotted guide line is $0.03\,h^4$.

```python
ax.set_xticks(h_values)  # one tick at each step used
ax.set_xticklabels([f"{x:.4f}" for x in h_values], fontsize=8)
ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())  # no extra ticks
ax.set_xlabel("RK4 step $h = L/G$ (units of $1/H$)")
ax.set_ylabel("$|\\varepsilon_{\\rm RK4} - \\varepsilon_{\\rm exact}|$ (units of $m$)")
ax.set_title("fourth-order convergence of the shooting method ($m = 1$, $L = 3$)")
ax.legend(fontsize=8)
```

One tick mark at each step used, labelled with 4 decimals; `NullLocator` removes the small extra ticks that a logarithmic axis draws by default.

```python
fourth = all(12.0 < errs[i] / errs[i + 1] < 20.0 for errs in curves.values()
             for i in range(2))  # halving h from 0.02 to 0.005: ratios near 16
check(fourth, "halving the step divides each error by about 16 (between 12 and 20)")
save_figure(fig, "rk4_convergence",
            "The error of four numerical levels ($m = 1$, $L = 3$; even labels 1 "
            ...)
```

For the first three step numbers (150, 300, 600: $h = 0.02$, $0.01$, $0.005$) each halving must divide each of the four errors by a factor between 12 and 20. **What figure 14b.4 shows.** Four straight lines parallel to the dotted line of slope 4, from errors near $10^{-6}$ at $h = 0.02$ down to $10^{-13}$ or $10^{-14}$ at $h = 0.0017$: the method is of fourth order over the whole range. The lines of the higher levels (labels 3) lie about three powers of ten above those of the lowest levels.

**In [12], the orbitals.**

```python
def orbital(eps, k=0.0, j=1.0, M=1.0, L=3.0, G=900, H=1.0, a4=0.0, tip=0.0):
    _, (theta_n, a_n, b_n) = shoot(eps, k, j, M=M, L=L, G=G, H=H, a4=a4, tip=tip,
                                   keep=True)
    nf, h = 2 * G + 1, L / G
    y_fine = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))
    K_fine = k * np.exp(-a4) * np.exp(-H * y_fine)
```

The orbital of one level. `shoot(..., keep=True)` returns the angle and the paths; `_` receives $\Phi$, which is not needed, and the paths are unpacked into three arrays (one value per node, since a single energy is given). Then the fine grid and $K = \kappa k$ on it.

```python
    a_f, b_f = np.zeros(nf), np.zeros(nf)
    a_f[0::2], b_f[0::2] = a_n, b_n  # the node values
    da = M * a_f - (K_fine + j * eps) * b_f  # the derivatives at the nodes
    db = (j * eps - K_fine) * a_f - M * b_f
```

Two arrays for the fine grid; `a_f[0::2]` is every second entry starting at 0, the nodes, which receive the node values. `da` and `db` are the derivatives $a'$, $b'$ from the real form; only their values at the nodes are used below.

```python
    for f in range(1, nf, 2):  # cubic Hermite value at each midpoint
        a_f[f] = 0.5 * (a_f[f - 1] + a_f[f + 1]) + h / 8.0 * (da[f - 1] - da[f + 1])
        b_f[f] = 0.5 * (b_f[f - 1] + b_f[f + 1]) + h / 8.0 * (db[f - 1] - db[f + 1])
```

The midpoints (odd positions 1, 3, 5, ...) get their values by **cubic Hermite interpolation**: the cubic polynomial that has the values $f_0$, $f_1$ and the derivatives $f_0'$, $f_1'$ at the two neighbouring nodes, a step $h$ apart, has at the midpoint the value $\tfrac12(f_0 + f_1) + \tfrac h8(f_0' - f_1')$ (Exercise 14.4). Its error is of order $h^4$, like that of RK4.

```python
    weights = np.full(nf, 2.0)  # Simpson: 1, 4, 2, 4, ..., 4, 1 times (h/2)/3
    weights[1::2] = 4.0
    weights[0] = weights[-1] = 1.0
    weights *= 0.5 * h / 3.0
    norm = math.sqrt(float(np.sum(weights * (a_f ** 2 + b_f ** 2))))
    return y_fine, a_f / norm, b_f / norm, weights
```

**Simpson's rule** (Chapter 2) on the fine grid, whose spacing is $h/2$: the weights $1, 4, 2, 4, \dots, 4, 1$ times $(h/2)/3$ (`weights[1::2]` are the odd positions, `weights[-1]` the last entry). The integral $\int(a^2 + b^2)dy$ is the weighted sum, and dividing $a$, $b$ by its square root normalises the orbital. The function returns the grid, the normalised components and the weights.

```python
y_f, a_zero, b_zero, simpson = orbital(numeric[(1.0, 3.0, "even", 0)])
a_exact = math.sqrt(2.0 / (1.0 - math.exp(-6.0))) * np.exp(y_f)
deviation = float(np.max(np.abs(a_zero - a_exact)))
check(numeric[(1.0, 3.0, "even", 0)] == 0.0 and np.all(b_zero == 0.0)
      and deviation < 1e-9 and record_check("free_zero_mode_exact", (RUST_REPORT,)),
      "zero mode: eps = 0 and b = 0 exactly, a = sqrt(2M/(1 - e^(-2ML))) e^(My)",
      record=f"{RUST_REPORT}, check free_zero_mode_exact")
```

The zero mode of $m = 1$, $L = 3$ against the exact $a = \sqrt{2/(1 - e^{-6})}\,e^{y}$ (Section 14.13 with $M = 1$, $L = 3$): its level is exactly 0, its $b$ is exactly 0 at every point, and $a$ agrees to $10^{-9}$, as in the Rust check free_zero_mode_exact.

```python
def exact_orbital(parity, label, m_=1.0, L_=3.0):
    level = exact[(m_, L_, parity, label)]
    p_ = math.sqrt(level ** 2 - m_ ** 2)
    if parity == "even":
        b_e = np.sin(p_ * y_f)
        a_e = (p_ * np.cos(p_ * y_f) + m_ * b_e) / level
    else:
        b_e = np.sin(p_ * (y_f + L_))
        a_e = (p_ * np.cos(p_ * (y_f + L_)) + m_ * b_e) / level
    sign = 1.0 if a_e[0] > 0 else -1.0  # the sign with a(-L) > 0
    norm = math.sqrt(float(np.sum(simpson * (a_e ** 2 + b_e ** 2))))
    return sign * a_e / norm, sign * b_e / norm
```

The exact orbitals of Section 14.13 for $j = +1$: $p = \sqrt{\varepsilon^2 - m^2}$, $b$ the sine, $a = (b' + mb)/\varepsilon$ written out ($b' = p\cos$). An orbital is fixed only up to a constant factor; the numerical one starts with $a(-L) = 1 > 0$, so the exact one is given the sign that makes $a(-L) > 0$ (`a_e[0]` is its value at $y = -L$) and is normalised with the same Simpson weights.

```python
shown = {}
worst_orbital = 0.0
for parity, label in (("even", 1), ("odd", 0)):
    _, a_num, b_num, _ = orbital(numeric[(1.0, 3.0, parity, label)])
    a_ex, b_ex = exact_orbital(parity, label)
    worst_orbital = max(worst_orbital, float(np.max(np.abs(a_num - a_ex))),
                        float(np.max(np.abs(b_num - b_ex))))
    shown[(parity, label)] = (a_num, b_num, a_ex, b_ex)
check(worst_orbital < 1e-8,
      "the even label 1 and odd label 0 orbitals equal the exact ones to 1e-8")
```

The numerical and exact orbitals of the even level 1 and the odd level 0, their largest difference over all points (below $10^{-8}$), and a dictionary `shown` that keeps them for the figure. Out [12] shows two PASS lines.

**In [13], figure 5.**

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.8), sharey=True)
panels = [("zero mode, $\\varepsilon = 0$", a_zero, b_zero, a_exact,
           np.zeros_like(a_exact)),
          (f"even label 1, $\\varepsilon = {lowest_even:.4f}$",) + shown[("even", 1)],
          (f"odd label 0, $\\varepsilon = {lowest_odd:.4f}$",) + shown[("odd", 0)]]
```

Three panels side by side that share the vertical axis (`sharey=True`), and for each a tuple of the title, the numerical $a$, $b$ and the exact $a$, $b$; `(title,) + shown[...]` puts the title in front of the stored four arrays, and `np.zeros_like` is an array of zeros of the same shape (the exact $b$ of the zero mode).

```python
for ax, (title, a_num, b_num, a_ex, b_ex) in zip(axes, panels):
    ax.plot(y_f, a_num, color="C0", label="$a$ (numerical)")
    ax.plot(y_f, b_num, "--", color="C1", label="$b$ (numerical)")
    ax.plot(y_f[::60], a_ex[::60], ".", color="black", label="exact")
    ax.plot(y_f[::60], b_ex[::60], ".", color="black")
    ax.set_title(title, fontsize=9)
    ax.set_xlabel("$y$ (units of $1/H$)")
axes[0].set_ylabel("orbital component (normalised)")
axes[0].legend(fontsize=8, loc="upper left")
save_figure(fig, "orbitals",
            "The normalised orbitals $\\chi = (a, ib)$ of three free $k = 0$ "
            ...)
```

In each panel the numerical $a$ (solid) and $b$ (dashed) and every 60th point of the exact ones as black dots (`[::60]` takes every 60th entry). **What figure 14b.5 shows.** Left: the zero mode, $a$ rising like $e^{y}$ from $0.07$ at the tip to $1.42$ at the brane, $b = 0$: the orbital lives at the brane. Middle: the even level 1, $b$ a half sine wave that vanishes at both ends, $a$ falling from $+0.42$ to $-0.42$. Right: the odd level 0, $b$ vanishing at the tip, $a$ vanishing at the brane. All black dots lie on the curves.

**In [14], figure 6.**

```python
picks = [("even", l_) for l_ in range(4)] + [("odd", l_) for l_ in range(3)]
energies = np.array([numeric[(1.0, 3.0, p_, l_)] for p_, l_ in picks])
_, (theta_path, _, _) = shoot(energies, 0.0, 1.0, keep=True)
y_nodes = np.linspace(-3.0, 0.0, 901)
end_values = theta_path[-1] / np.pi
goals = np.array([l_ + (0.0 if p_ == "even" else 0.5) for p_, l_ in picks])
check(np.max(np.abs(end_values - goals)) < 1e-9,
      "the Pruefer angle ends on its target l pi or (l + 1/2) pi for every level")
```

Seven levels (even labels 0 to 3, odd labels 0 to 2), one call of `shoot` that keeps the angle paths (an array with 901 rows, the nodes, and seven columns), the 901 node positions, the end angles in units of $\pi$ (`theta_path[-1]` is the last row) and the targets $l$ or $l + \tfrac12$. The check: every path ends on its target to $10^{-9}$.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
for column, (p_, l_) in enumerate(picks):
    style = "-" if p_ == "even" else "--"
    ax.plot(y_nodes, theta_path[:, column] / np.pi, style,
            label=f"{p_}, label {l_}")
ax.set_xlabel("$y$ (units of $1/H$; tip at $-3$, brane at $0$)")
ax.set_ylabel("Pruefer angle $\\theta(y)/\\pi$")
ax.set_title("the Pruefer angle counts the half-turns ($m = 1$, $L = 3$, $k = 0$)")
ax.legend(fontsize=8, ncol=2, loc="upper left")
save_figure(fig, "pruefer_angle",
            "The Pruefer angle $\\theta(y) = \\mathrm{atan2}(b, a)$ in units of "
            ...)
```

`theta_path[:, column]` is one column, the path of one level; even levels are drawn solid, odd ones dashed. **What figure 14b.6 shows.** All curves start at 0 at the tip ($b(-3) = 0$) and climb to their targets at the brane: the even labels 0, 1, 2, 3 end at 0, 1, 2, 3 and the odd labels 0, 1, 2 at 0.5, 1.5, 2.5. The zero mode stays at 0 all the way. A higher level turns faster: the label counts the half-turns of the point $(a, b)$ between the tip and the brane.

**In [15], the last check.**

```python
figure_names = ["14b_1_odd_condition.png", "14b_2_shooting_function.png",
                "14b_3_spectrum_ladder.png", "14b_4_rk4_convergence.png",
                "14b_5_orbitals.png", "14b_6_pruefer_angle.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all six figure files of this notebook exist")
all_checks_passed()
```

The six figure files must exist where the notebook wrote them; the last line prints ALL 20 CHECKS PASSED (notebook 14b). The 20 checks are: 1 in In [2], 6 in In [3], 2 in In [4], 1 in In [6], 1 in In [7], 3 in In [8], 1 in In [10], 1 in In [11], 2 in In [12], 1 in In [14] and 1 in In [15].

### 14.19 The brane band and its exact slope

**What happens when the 3-momentum is switched on.** At $k = 0$ the free spectrum has eight zero modes, four in the blocks of type $j = +1$ and four in those of type $j = -1$ (Section 14.13). For $k \ne 0$ the momentum term $j\kappa k\,\sigma_3$ of $h_j$ moves them. In the blocks $j = +1$ the even level of label 0 rises with $k$: this is the **brane band**, because its orbital stays at the brane. In the blocks $j = -1$ the even level of label 0 falls by exactly the same amount, because $h_{-1} = -h_{+1}$ for $v = 0$ (Section 14.5): its levels are the negatives of those of $j = +1$, with the label $l$ of even parity going to $-l$. How fast does the band rise? Its slope at $k = 0$ can be computed exactly.

**The Hellmann-Feynman rule.** Let $h(k)$ be a self-adjoint operator that depends on a number $k$, with boundary conditions that do not depend on $k$, and let $h(k)\chi = \varepsilon(k)\chi$ with $\int\chi^\dagger\chi\,dy = 1$. Line by line:

$$
\varepsilon = \int\chi^\dagger h\chi\,dy .
$$

Rule: multiply $h\chi = \varepsilon\chi$ from the left by $\chi^\dagger$, integrate, and use the normalisation.

$$
\frac{d\varepsilon}{dk} = \int\frac{\partial\chi^\dagger}{\partial k}h\chi\,dy + \int\chi^\dagger h\frac{\partial\chi}{\partial k}\,dy + \int\chi^\dagger\frac{\partial h}{\partial k}\chi\,dy .
$$

Rule: the product rule for the three factors.

$$
\int\frac{\partial\chi^\dagger}{\partial k}h\chi\,dy + \int\chi^\dagger h\frac{\partial\chi}{\partial k}\,dy = \varepsilon\int\Big(\frac{\partial\chi^\dagger}{\partial k}\chi + \chi^\dagger\frac{\partial\chi}{\partial k}\Big)dy = \varepsilon\frac{d}{dk}\int\chi^\dagger\chi\,dy = 0 .
$$

Rule: in the first integral $h\chi = \varepsilon\chi$; in the second $h$ is self-adjoint, so $\int\chi^\dagger h\,\partial_k\chi\,dy = \int(h\chi)^\dagger\partial_k\chi\,dy = \varepsilon\int\chi^\dagger\partial_k\chi\,dy$ (the derivative $\partial_k\chi$ obeys the same boundary conditions, because they do not depend on $k$); then the product rule backwards, and the normalisation integral is the constant 1. Hence

$$
\frac{d\varepsilon}{dk} = \int\chi^\dagger\frac{\partial h}{\partial k}\chi\,dy .
$$

In words: the rate of change of a level is the expectation value of the rate of change of the operator.

**The slope of the band.** Line by line:

$$
\frac{\partial h_j}{\partial k} = j\kappa(y)\,\sigma_3 .
$$

Rule: in $h_j = j[-i\sigma_1\,d/dy + M\sigma_2 + \kappa k\sigma_3] + v$ only the last term contains $k$.

$$
\frac{d\varepsilon}{dk}\Big|_{k=0} = j\int_{-L}^{0}\kappa(y)\,\chi^\dagger\sigma_3\chi\,dy = j\int_{-L}^{0}e^{-Hy - a_{4,0}}\,a(y)^2\,dy .
$$

Rule: the Hellmann-Feynman rule at $k = 0$, where the orbital is the zero mode $\chi = (a, 0)$ and $\chi^\dagger\sigma_3\chi = a^2 - b^2 = a^2$ (Section 14.12).

$$
c = \frac{\int_{-L}^{0}e^{-Hy - a_{4,0}}e^{2My}\,dy}{\int_{-L}^{0}e^{2My}\,dy} .
$$

Rule: $a^2 = A^2e^{2My}$ with $A^2 = 1/\int_{-L}^0e^{2My}dy$ (the normalisation); we call $c$ the slope of the band of type $j = +1$, so that $d\varepsilon/dk = jc$.

$$
\int_{-L}^{0}e^{-Hy}e^{2My}\,dy = \frac{1 - e^{-(2M - H)L}}{2M - H}, \qquad \int_{-L}^{0}e^{2My}\,dy = \frac{1 - e^{-2ML}}{2M} .
$$

Rule: $e^{-Hy}e^{2My} = e^{(2M - H)y}$; the integral of $e^{sy}$ is $e^{sy}/s$, evaluated at $0$ and $-L$ (here $2M \ne H$).

$$
c = e^{-a_{4,0}}\,\frac{2M}{2M - H}\,\frac{1 - e^{-(2M - H)L}}{1 - e^{-2ML}} .
$$

Rule: divide the two integrals and take the constant factor $e^{-a_{4,0}}$ out of the first. For $M = H = 1$:

$$
c = e^{-a_{4,0}}\,\frac{2(1 - e^{-L})}{1 - e^{-2L}} = \frac{2e^{-a_{4,0}}}{1 + e^{-L}} .
$$

Rule: $1 - e^{-2L} = (1 - e^{-L})(1 + e^{-L})$ (the difference of two squares). For $L = 3$ and $a_{4,0} = 0$: $c = 2/(1 + e^{-3}) = 1.9051482536$. Status: PROVED; check brane_band_slope of `Revision/kohn_sham/reports/ks-theory-python.json` and of the Wolfram report, and the value braneBandSlope_M1_H1_L3_a0 = 1.9051482536448664 under checksNumeric in `Revision/kohn_sham/ks-theory.json`.

**What the formula says.** Three things. (1) The band starts linearly, $\varepsilon \approx ck$, like the energy of a massless particle, although the mass $m$ is not zero: the mass term only keeps the orbital at the brane. The slope is the average of the momentum weight $\kappa$ over the zero-mode orbital (the integral above), and it is larger than the value $e^{-a_{4,0}}$ of $\kappa$ at the brane because the orbital reaches somewhat toward the tip, where $\kappa$ is larger. (2) For a long hidden interval, $L \to \infty$, the slope tends to $2M/(2M - H)$, which is 2 for $M = H = 1$; for $L = 2$, $3$, $4$ it is $1.761594$, $1.905148$, $1.964028$ (Notebook 14c, Out [5]). (3) Along the deflating history the slope shrinks like $e^{-a_{4,0}}$: at the five slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$ the exact values are $1.905148253645$, $1.155530827134$, $0.700864874900$, $0.425096034942$, $0.257833778515$ (Notebook 14c, Out [5]).

**The band is an odd function of $k$.** The relation $\sigma_3h_j(k)\sigma_3 = h_{-j}(-k)$ of Section 14.5 says that the level of $(j, k)$ equals the level of $(-j, -k)$ with the same label; and $h_{-1} = -h_{+1}$ says that the level of $(-1, k)$ with even label 0 is minus the level of $(+1, k)$ with even label 0. Together: $\varepsilon_{\rm band}(-k) = \varepsilon_{-1}(k) = -\varepsilon_{\rm band}(k)$. So $\varepsilon_{\rm band}(k)/k = c + dk^2 + \dots$ contains only even powers of $k$. The Revision solver used this to measure the slope numerically: with $R(k) = \varepsilon(k)/k$ at $k_1 = 10^{-4}$ and $k_2 = 2\times10^{-4}$,

$$
\frac{4R(k_1) - R(k_2)}{3} = \frac{4(c + dk_1^2) - (c + 4dk_1^2)}{3} = c .
$$

Rule: $k_2 = 2k_1$, so $k_2^2 = 4k_1^2$, and the terms with $d$ cancel (**Richardson extrapolation**, Chapter 2; what remains is of order $k^4$). The Rust solver found the exact $c\,e^{-a_{4,0}}$ at all five slices to $1.87\times10^{-12}$ (relative; check free_brane_band_slope of `Revision/kohn_sham/reports/ks-rust-solver.json`; the values are in `Revision/kohn_sham/results/spectrum/brane-band-slope.csv`). Status: COMPUTED; Notebook 14c reproduces the five values.

**The band at larger momenta.** The record `Revision/kohn_sham/results/spectrum/brane-band.csv` follows the band and three other levels from $k = 0$ to $k = 4$ at the slice 0. At the first lattice shell, $k = \Delta k = 0.25$, the band is at $0.4307336786\,m$ (Notebook 14c, Out [3]), a little below the straight line $ck = 0.476$: the band bends downward. At $k = 4$ it is at $4.992\,m$. The lowest level that is not on the brane band at $k = 0$ is the odd level of label 0 at $1.2922928281\,m$ (Section 14.13), called the **bulk edge**; all other levels start at or above it (Figure 14c.1). Status: COMPUTED.

### 14.20 The band along the deflating history, and the tip

**The redshift.** By the exact rescaling identity (Section 14.7) every level at the slice $a_{4,0}$ equals the level at the slice 0 with the redshifted momentum: $\varepsilon(k, a_{4,0}) = \varepsilon(ke^{-a_{4,0}}, 0)$. So the whole band shrinks toward zero along the history: at a later slice the same lattice momentum $k$ sits lower on the band. The Rust solver checked the identity for the three momenta $k = 0.25, 1, 2.5$, the five slices and three sectors, and found the two sides equal to the last bit, with the difference 0 (check free_rescaling_relation_and_band_monotone of the Rust report; the same check found the band strictly increasing in $k$ on $[0, 4]$). Status: PROVED (the identity), COMPUTED (the check).

**The gap of the eight zero modes along the history.** In the free state $N = 8$ the eight zero modes are filled and the lowest empty particle level is the brane band at the first lattice shell, $k = 0.25$. This level is the **gap** of the state. At the five slices it is

| slice $a_{4,0}$ | 0 | 0.5 | 1 | 1.5 | 2 |
| --- | --- | --- | --- | --- | --- |
| gap of the free $N = 8$ state (units of $m$) | 0.4307336786 | 0.2726448766 | 0.1703492513 | 0.1050152416 | 0.0641594107 |

(Notebook 14c, Out [7]; the rows $N = 8$ of `Revision/kohn_sham/results/spectrum/closed-shells.csv`). The gap shrinks almost like $e^{-a_{4,0}}$ (for small momenta the band is nearly $c\,ke^{-a_{4,0}}$): as 3-space inflates, the lattice momenta are redshifted and the empty levels come down toward the filled zero modes. Status: COMPUTED. (Chapter 15 asks whether the gas can follow this change: the adiabaticity of the history.)

**The tip angle does not matter for the band (at the cutoff $L = 3$ and the slice 0).** Section 14.12 showed that an orbital with $k \ne 0$ is suppressed at the cutoff by about $\exp(-|k|(\kappa(-L) - \kappa(y))/H)$, so the band level should hardly change if the tip condition is changed. The Rust solver computed the band with the tip angles $\theta = 0, 0.5, 1$ (record `Revision/kohn_sham/results/spectrum/tip-angle.csv`): at $k = 0.25$ the level moves by $-8.58\times10^{-6}$ and $-2.74\times10^{-5}$, while the suppression factor is $8.47\times10^{-3}$; at $k = 0.5$ by $-2.49\times10^{-9}$ and $-8.58\times10^{-9}$ against $7.17\times10^{-5}$; at $k = 1$ only by rounding errors (below $10^{-15}$) against $5.14\times10^{-9}$ (check free_tip_angle_insensitivity of the Rust report: every shift lies below the suppression factor). Notebook 14c computes the shifts for ten momenta from 0.1 to 1 (Out [11]): each step of 0.1 in $k$ makes them 11 to 33 times smaller, faster than the suppression factor itself (which falls by $e^{0.1(e^3 - 1)} \approx 6.7$ per step), until they reach the rounding level of the computer at $k = 0.9$. Status: COMPUTED. Both the record and the notebook work at the slice $a_{4,0} = 0$. So, at the cutoff $L = 3$ and the slice $a_{4,0} = 0$, where it was measured (record: $k = 0.25, 0.5, 1$; Notebook 14c: $k = 0.1$ to $1$), the choice of the tip angle $\theta$ in the ASSUMED tip condition is harmless for every lattice level with $k \ne 0$; at $k = 0$, where it selects the zero mode, it is a real assumption of the model.

**The tip angle at the later slices (not established).** By the rescaling identity above, the lattice momentum $k$ at the slice $a_{4,0}$ acts like the momentum $ke^{-a_{4,0}}$ at the slice 0, and there the suppression factor of Section 14.12 is no longer small: for the first lattice shell, $k = 0.25$, it is $\exp(-0.25e^{-a_{4,0}}(e^3 - 1))$, which is $0.173$ at the slice 1 and $0.524$ at the slice 2. Rule: $0.25(e^3 - 1) = 4.771$; times $e^{-1} = 0.3679$ this is $1.755$, and $e^{-1.755} = 0.173$; times $e^{-2} = 0.1353$ it is $0.646$, and $e^{-0.646} = 0.524$. The notebook's own smallest momentum points the same way: by the identity, its shift $1.2\times10^{-3}$ for $\theta = 1$ at $k = 0.1$ and the slice 0 (Out [11]) is the shift at $k = 0.25$ and the slice $\ln 2.5 = 0.92$, more than forty times the shift $2.74\times10^{-5}$ at $k = 0.25$ and the slice 0. Neither the Revision record nor a notebook of this chapter computes the tip angle at the later slices, where the gaps of the table above at the slices 1 to 2 and the recorded Kohn-Sham states there live; so at those slices the insensitivity to $\theta$ is not established (OPEN).

**The position $L$ of the cutoff (measured by the Revision record).** The angle is one question; where the cutoff sits is another. The Revision record measures it in `Revision/kohn_sham/tip_convergence/` (its README, "Answer in brief"; the report `Revision/kohn_sham/tip_convergence/tip-convergence.json`, 7 of 7 checks PASS; `Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md`, sections 5, 15.3 and 15.4): $L = 3$ to $6$ in steps of $0.5$, with the step $h = 1/300$ of the record and every run repeated at $h/2$; a copy of the solver that reads $L$ from the environment reproduces the committed matrix byte for byte at $L = 3$, and the independent reference solver agrees at $L = 3$ and $4$. No notebook of this chapter repeats the study; its findings, with the record's numbers:

- The free results with $k \ne 0$ converge as $L$ grows, faster than exponentially, because of the suppression of Section 14.12 (at the cutoff it is $\exp(-|k|e^{L - a_{4,0}}/H)$). But the recorded $L = 3$ values are low by up to 1.4% in the Kohn-Sham energy $E_{\rm KS}$ and 12% in the $y$-pressure integral $2\mathrm{Vol}_7\int e^{6Hy}p_8\,dy$ at $a_{4,0} = 2$ ($N = 136$, $\lambda = 0$: $12.44507$ against the extrapolated $12.62207$, and $8.47270$ against $9.63839$): at the late slice the redshifted brane band reaches the tip. The gap of the free $N = 8$ state in the table above is low in the same way: $0.4307336786$ against the extrapolated $0.4307456266$ at the slice 0 ($2.8\times10^{-5}$ relative), but $0.06415941073$ against $0.06563459278$ at the slice 2 ($2.2\times10^{-2}$ relative).
- The nonzero $k = 0$ levels approach $\pm m$ only algebraically, like $(n\pi)^2/(2mL^2)$ (for large $L$, from the exact levels of Section 14.13, $\sqrt{m^2 + (n\pi/L)^2} - m \approx (n\pi)^2/(2mL^2)$; the record verifies all 84 $k = 0$ levels of its scan against the exact formulas to $1.42\times10^{-10}\,m$). The bulk edge $1.2923\,m$ that defines $N = 688$ (Section 14.21) is an $L = 3$ value: $1.0977\,m$ at $L = 6$, and $m$ as $L \to \infty$. From $L = 3.5$ on, the $N = 688$ ground state at $a_{4,0} = 0$ occupies $k = 0$ bulk levels, its Kohn-Sham gap $0.0452$ closes, and its energy does not converge up to $L = 6$.
- The interaction energy of the brane zero modes depends strongly on $L$. Their proper density grows toward the tip like $e^{(6H - 2m)|y|}$ (Section 14.27; exact, and verified by the record), so for $N = 8$ the recorded $E_{\rm KS} = \mp9.868\times10^{-4}$ at $L = 3$ ($\lambda = \pm\lambda_1$, every slice) is about one third of the large-$L$ value $\mp3.0046\times10^{-3}$ (extrapolated from $\lambda = -\lambda_1$ at $a_{4,0} = 2$, the only interacting $N = 8$ state solved up to $L = 6$). The self-consistent iteration fails at some larger $L$ for 13 of the 19 interacting states studied (a failure of the iteration, not a proof that no self-consistent state exists), and for 7 of them the limit of $E_{\rm KS}$ is not established.

Status: COMPUTED by the Revision record with its two solvers (the $L$-dependence of the $k = 0$ levels and of the zero-mode density is exact and verified there). So the cutoff $L = 3$ is itself a choice that shapes the recorded numbers: within the percentages above for the free results with $k \ne 0$, and decisively for the nonzero $k = 0$ levels, for $N = 688$ at $a_{4,0} = 0$ and for the interaction energy of the zero modes.

### 14.21 Particles, degeneracies and closed shells

**Lattice shells.** On the 3-torus the allowed momenta are $\mathbf k = \Delta k\,(n_1, n_2, n_3)$ with whole numbers $n_i$ (Section 14.3). All vectors with the same $n^2 = n_1^2 + n_2^2 + n_3^2$ have the same length $|\mathbf k| = \Delta k\sqrt{n^2}$ and form a **shell**; their number is written $r_3(n^2)$. For example $r_3(0) = 1$ (only $(0, 0, 0)$), $r_3(1) = 6$ (the six vectors $(\pm1, 0, 0)$, $(0, \pm1, 0)$, $(0, 0, \pm1)$) and $r_3(2) = 12$ (two entries $\pm1$ and one 0: three places for the 0 times four sign choices). The first values are $r_3 = 1, 6, 12, 8, 6, 24, 24, 12, 30$ for $n^2 = 0, 1, 2, 3, 4, 5, 6, 8, 9$; no vector has $n^2 = 7$, because the squares below 8 are 0, 1 and 4, and no three of them add up to 7.

**Degeneracy.** The levels depend on $|\mathbf k|$ only (Section 14.6), and the four blocks $(s_2, s_3)$ of one type have the same Hamiltonian (Section 14.5). So every level of the block type $j$ on the shell $n^2$ holds $4r_3(n^2)$ states: four blocks times $r_3(n^2)$ directions. Status: PROVED (the argument above; the record states it as blockEquation.degeneracy in `Revision/kohn_sham/ks-theory.json`).

**Particles and the sea (ASSUMED convention; its justification is OPEN).** The free spectrum has positive and negative levels. In the quantised theory (Chapter 10) the field is normal ordered: the negative levels form the filled **sea**, which is not counted, and the quanta that are counted, the **particles**, occupy the positive levels. The Revision theory adopts the following rule: in each sector (shell, block type, parity) the particle levels are those whose level in the free problem ($\lambda = 0$) is positive, together with the zero modes at $k = 0$, each followed continuously when the interaction is switched on; the sea contributes nothing to the particle number and the densities. The zero modes need a decision: at $k = 0$ and $v = 0$ the spectrum of $h_{+1}$ is minus that of $h_{-1}$, so a level at exactly zero is its own mirror image and the sign does not decide whether it is a particle or a sea level. Counting it as a particle level is a stated CONVENTION of the record (ks-theory.json, thermodynamics.fillingConvention), and its justification is OPEN. (The words particle and sea are used here in this technical sense only; nothing in this chapter is a statement about matter and antimatter, which Chapter 21 treats.)

Because $\Phi$ grows with $\varepsilon$ (Section 14.14), the particle levels of a sector are exactly the labels $l \ge l_{\min}$, where $l_{\min}$ is the first label whose target lies above $\Phi(0)$, the value of the shooting function at $\varepsilon = 0$ (and at $k = 0$, even parity, the zero mode has $\Phi(0) = 0$ exactly on the target of label 0). The Rust solver verified this for every shell $n^2 \le 30$ and every sector, and found that the level closest to zero, apart from the zero modes, is $0.4307\,m$: the brane band at the first shell (check free_particle_branch_labels of the Rust report). Status: COMPUTED.

**Closed shells.** The **aufbau** (German for building up) fills the particle states from the lowest level upward. A particle number $N$ is a **closed shell** when the filling ends exactly at the end of a group of degenerate levels (levels equal within $10^{-9}$), so that the state is unique. At the slice 0 the first closed shells are built like this (record `Revision/kohn_sham/results/spectrum/closed-shells.csv`, reproduced by Notebook 14c, Out [14]):

| $N$ | the last group filled | states added | its level (units of $m$) |
| --- | --- | --- | --- |
| 8 | the zero modes, both block types | $4 + 4 = 8$ | 0 |
| 32 | the brane band on the shell $n^2 = 1$ | $4 \times 6 = 24$ | 0.4307336786 |
| 80 | the brane band on the shell $n^2 = 2$ | $4 \times 12 = 48$ | 0.5879568528 |
| 112 | the brane band on the shell $n^2 = 3$ | $4 \times 8 = 32$ | 0.7040995646 |
| 136 | the brane band on the shell $n^2 = 4$ | $4 \times 6 = 24$ | 0.7996457668 |
| 232 | the brane band on the shell $n^2 = 5$ | $4 \times 24 = 96$ | 0.8823195405 |

Only the brane band of the blocks $j = +1$ appears on the shells $n^2 \ge 1$ in this table: the band of the blocks $j = -1$ is negative (sea), and every other level lies higher. The list of closed shells at the slice 0 continues $328, 376, 496, 592, 688, 696, 728, \dots$ up to the energy $1.6\,m$ (22 closed shells in all). The shell $N = 696$ is the first that fills a level off the brane band: the odd level of label 0 at $k = 0$, at the bulk edge $1.2922928281\,m$.

**The particle numbers of the Revision runs.** The Revision solver chose its three particle numbers by a rule fixed in advance (record `Revision/kohn_sham/results/parameters.json`, particleNumbers): $N = 8$, the zero modes; $N_{\rm large}$, the largest closed shell whose last filled level lies below the bulk edge, which is 688; and $N_{\rm mid}$, the closed shell nearest to $N_{\rm large}/4 = 172$, which is 136 (the neighbours 136 and 232 are 36 and 60 away). Status: COMPUTED; Notebook 14c repeats the rule and finds 8, 136, 688. The rule is applied at the cutoff $L = 3$: the bulk edge is an $L = 3$ value ($1.0977\,m$ at $L = 6$, and $m$ as $L \to \infty$), so $N = 688$ is itself an $L = 3$ choice (Section 14.20).

**At a later slice.** At the slice $a_{4,0} = 0.5$ the redshifted band holds many more states below the same energy: 55 closed shells below $1.6\,m$ instead of 22 (Notebook 14c, Out [14]; Figure 14c.6).

### 14.22 Example: Notebook 14c, the brane band

Notebook 14c does Sections 14.19 to 14.21 with the computer, with the shooting method of Notebook 14b (now also for nonzero 3-momenta and any slice). It computes the brane band and three other levels for $k$ from 0 to 4 and compares 324 levels with the Rust record; it derives the slope formula with sympy, checks the integral of Section 14.19 on the numerical zero mode, measures the slope by Richardson extrapolation at the five slices and for two other cutoffs; it checks the rescaling identity for 45 levels and the gap of the state $N = 8$ at the five slices; it checks the two block-type symmetries; it measures the effect of the tip angle at the cutoff $L = 3$ and the slice 0; and it builds the lattice shells, the particle labels, the closed shells at the slices 0 and 0.5 and the particle numbers of the Revision runs, all against the Rust records. It draws six figures and needs no Rust. It runs in about 90 seconds (the cells of its sections 8 to 11 integrate the equation for hundreds of energies at once, 72 times over, and take 5 to 20 seconds each), and its last line is ALL 15 CHECKS PASSED (notebook 14c).

<!-- NOTEBOOK 14c -->

### 14.25 Line-by-line walk-through of Notebook 14c

The notebook has 16 code cells, In [1] to In [16]. Docstrings and the long caption texts are again left out of the quotations; the captions are printed under the figures in Section 14.24.

**In [1], the set-up cell.** The code of In [1] of Notebook 14a (Section 14.11), line for line, except

```python
NOTEBOOK_ID = "14c"  # this notebook: chapter 14, example c
```

which names this notebook. Its comment lines are the run instructions of Section 14.23.

**In [2], the tools.**

```python
import math  # exp, cos, sin of single numbers

import numpy as np  # floating-point arrays
import sympy as sp  # exact algebra with symbols

RUST_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
SPECTRUM = "Revision/kohn_sham/results/spectrum"  # the folder of the records
```

The three modules of In [2] of Notebook 14b, the name of the Rust solver's report, and the folder of its spectrum records.

```python
def record_check(name, report=RUST_REPORT):
    data = json.loads(repository_file(report).read_text(encoding="utf-8"))
    return [c["verdict"] for c in data["checks"] if c["name"] == name] == ["PASS"]
```

A simpler `record_check`: true when the report (by default the Rust report) holds exactly one check of this name and its verdict is PASS (the list of all verdicts of that name must be the one-element list `["PASS"]`).

```python
def read_csv(relative):
    lines = repository_file(relative).read_text(encoding="utf-8").splitlines()
    header = lines[0].split(",")
    return [dict(zip(header, line.split(","))) for line in lines[1:]]
```

A small CSV reader: the rows of a record as a list of dictionaries from column name to text, as in Notebooks 14a and 14b.

```python
def shoot(eps, k=0.0, j=1.0, a4=0.0, M=1.0, L=3.0, G=900, H=1.0, tip=0.0,
          keep=False):
    eps, k, j, a4 = np.broadcast_arrays(*(np.asarray(x, dtype=float)
                                          for x in (eps, k, j, a4)))
    nf = 2 * G + 1  # nodes and step midpoints
    y_fine = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))
    e_minus_Hy = np.exp(-H * y_fine)
    kk = k * np.exp(-a4)  # kappa k = kk e^(-Hy)
    h = L / G
    a_ = np.full(eps.shape, math.cos(0.5 * tip))
    b_ = np.full(eps.shape, math.sin(0.5 * tip))
    theta = np.full(eps.shape, 0.5 * tip)
    raw = np.arctan2(b_, a_)
    je = j * eps
    path = [(theta, a_, b_)]
    for i in range(G):
        K0, K1, K2 = (kk * e_minus_Hy[2 * i], kk * e_minus_Hy[2 * i + 1],
                      kk * e_minus_Hy[2 * i + 2])
        p1a, p1b = M * a_ - (K0 + je) * b_, (je - K0) * a_ - M * b_
        a2, b2 = a_ + 0.5 * h * p1a, b_ + 0.5 * h * p1b
        p2a, p2b = M * a2 - (K1 + je) * b2, (je - K1) * a2 - M * b2
        a3, b3 = a_ + 0.5 * h * p2a, b_ + 0.5 * h * p2b
        p3a, p3b = M * a3 - (K1 + je) * b3, (je - K1) * a3 - M * b3
        a4_, b4_ = a_ + h * p3a, b_ + h * p3b
        p4a, p4b = M * a4_ - (K2 + je) * b4_, (je - K2) * a4_ - M * b4_
        a_ = a_ + h / 6.0 * (p1a + 2.0 * p2a + 2.0 * p3a + p4a)
        b_ = b_ + h / 6.0 * (p1b + 2.0 * p2b + 2.0 * p3b + p4b)
        new = np.arctan2(b_, a_)
        step = new - raw  # brought into (-pi, pi]
        step = np.where(step > np.pi, step - 2 * np.pi,
                        np.where(step <= -np.pi, step + 2 * np.pi, step))
        theta = theta + step
        raw = new
        if keep:
            path.append((theta, a_, b_))
    if keep:
        return j * theta, [np.array(q) for q in zip(*path)]
    return j * theta
```

The function `shoot` of Notebook 14b (Section 14.18 explains every line), with one change: the slice `a4` is now the fourth argument and may also be an array, so that levels at different slices are computed in one call. The first two lines therefore bring four inputs to a common shape; `*(...)` hands the four arrays made by the generator over as four separate arguments.

```python
def target(parity, label):
    offset = np.where(np.asarray(parity) == "even", 0.0, 0.5 * np.pi)
    return offset + np.asarray(label, dtype=float) * np.pi


def levels(k, j, parity, label, a4=0.0, iterations=72, **options):
    k, j, parity, label, a4 = np.broadcast_arrays(
        np.asarray(k, dtype=float), np.asarray(j, dtype=float), np.asarray(parity),
        np.asarray(label), np.asarray(a4, dtype=float))
    goal = target(parity, label)
    lo, hi = np.full(k.shape, -20.0), np.full(k.shape, 20.0)
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        g = shoot(mid, k, j, a4, **options) - goal
        lo = np.where(g <= 0.0, mid, lo)
        hi = np.where(g >= 0.0, mid, hi)
    return 0.5 * (lo + hi)
```

`target` and `levels` as in Notebook 14b, with the slice `a4` as an extra input that may differ from level to level.

```python
def orbital(eps, k=0.0, j=1.0, a4=0.0, M=1.0, L=3.0, G=900, H=1.0):
    _, (_, a_n, b_n) = shoot(eps, k, j, a4, M=M, L=L, G=G, H=H, keep=True)
    nf, h = 2 * G + 1, L / G
    y_fine = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))
    K_fine = k * math.exp(-a4) * np.exp(-H * y_fine)
    a_f, b_f = np.zeros(nf), np.zeros(nf)
    a_f[0::2], b_f[0::2] = a_n, b_n
    da = M * a_f - (K_fine + j * eps) * b_f
    db = (j * eps - K_fine) * a_f - M * b_f
    for f in range(1, nf, 2):  # cubic Hermite values at the midpoints
        a_f[f] = 0.5 * (a_f[f - 1] + a_f[f + 1]) + h / 8.0 * (da[f - 1] - da[f + 1])
        b_f[f] = 0.5 * (b_f[f - 1] + b_f[f + 1]) + h / 8.0 * (db[f - 1] - db[f + 1])
    weights = np.full(nf, 2.0)  # Simpson weights 1, 4, 2, ..., 4, 1 times (h/2)/3
    weights[1::2] = 4.0
    weights[0] = weights[-1] = 1.0
    weights *= 0.5 * h / 3.0
    norm = math.sqrt(float(np.sum(weights * (a_f ** 2 + b_f ** 2))))
    return y_fine, a_f / norm, b_f / norm, weights
```

The normalised orbital of one level, exactly as `orbital` of Notebook 14b (In [12] there): the node values from `shoot`, cubic Hermite values at the midpoints, Simpson's weights and the normalisation. Here the slice is a single number, so `math.exp` suffices.

```python
SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]  # the slices of the Revision solver
say("defined: shoot, levels, orbital, read_csv, record_check")
```

The five slices of the history and the only output of the cell.

**In [3], the band and three other levels.**

```python
k_list, kk = [], 0.0
while kk <= 4.0 + 1e-12:  # 0, 0.05, 0.10, ... as the Rust program makes them
    k_list.append(kk)
    kk += 0.05
k_band = np.array(k_list)
```

The momenta $0, 0.05, 0.10, \dots, 4$, made by adding 0.05 again and again, as the Rust program does. A `while` loop repeats as long as its condition holds. The decimal number 0.05 is not exactly representable in binary floating point, so the sums differ in the last digits from $0.05\,n$; making them the same way as the Rust program makes the last digits agree with the record (and the small $10^{-12}$ in the condition makes sure that the last value, about 4, is included).

```python
sectors = [(1.0, "even", 0), (1.0, "even", 1), (1.0, "odd", 0), (-1.0, "even", 1),
           (-1.0, "even", 0)]  # (j, parity, label); the last one for the figure
K_all = np.concatenate([k_band] * len(sectors))
J_all = np.concatenate([[j_] * len(k_band) for j_, _, _ in sectors])
P_all = np.concatenate([[p_] * len(k_band) for _, p_, _ in sectors])
L_all = np.concatenate([[l_] * len(k_band) for _, _, l_ in sectors])
found = levels(K_all, J_all, P_all, L_all).reshape(len(sectors), len(k_band))
band, bulk_even, odd0, minus_even1, minus_band = found
```

Five sectors (block type, parity, label): the brane band, the even label 1 and the odd label 0 of $j = +1$, the even label 1 of $j = -1$ (the four levels of the record), and the even label 0 of $j = -1$ for the figure. `np.concatenate` joins lists end to end, so the four arrays hold all $5 \times 81 = 405$ combinations; one call of `levels` finds all of them, and `reshape` arranges the result as 5 rows of 81. The last line unpacks the five rows into five names.

```python
rows = read_csv(f"{SPECTRUM}/brane-band.csv")
record = np.array([[float(r[c]) for r in rows] for c in
                   ("eps_band_a0", "eps_band_bulk_even_l1", "eps_odd_l0",
                    "eps_jm1_even_l1")])
k_record = np.array([float(r["k"]) for r in rows])
say(f"k = 0.25: brane band {band[5]:.10f}, odd level {odd0[5]:.10f} (units of m)")
```

The record's four columns as an array of 4 rows of 81 numbers, its momenta, and a printed sample: position 5 of the list is $k = 0.25$.

```python
check(len(rows) == 81 and np.max(np.abs(k_record - k_band)) < 1e-15
      and np.max(np.abs(found[:4] - record)) < 1e-11,
      "the 324 levels equal the record brane-band.csv",
      record=f"{SPECTRUM}/brane-band.csv")
check(bool(np.all(np.diff(band) > 0.0)) and np.max(np.abs(minus_band + band)) < 1e-12,
      "the band rises strictly with k; the j = -1 band is its mirror image -eps")
```

The first check: 81 rows, the same momenta, and the first four rows of levels (`found[:4]`, $4 \times 81 = 324$ levels) equal to the record to $10^{-11}$. The second: the band rises strictly, and the band of $j = -1$ is exactly its negative (Section 14.19). Out [3] prints the band at $k = 0.25$, $0.4307336786$, and the odd level $1.9195133815$, and two PASS lines.

**In [4], figure 1.**

```python
c_theory = 2.0 / (1.0 + math.exp(-3.0))  # the slope for M = H = 1, L = 3, a4,0 = 0
fig, ax = plt.subplots(figsize=(9.5, 4.8))
ax.plot(k_band, band, color="C0", linewidth=2, label="brane band ($j = +1$, even, 0)")
ax.plot(k_band, bulk_even, color="C1", label="$j = +1$, even, label 1")
ax.plot(k_band, odd0, color="C2", label="$j = +1$, odd, label 0")
ax.plot(k_band, minus_even1, color="C4", label="$j = -1$, even, label 1")
ax.plot(k_band, minus_band, "--", color="C0",
        label="$j = -1$, even, label 0 (sea)")
```

The slope $c = 2/(1 + e^{-3})$ of Section 14.19 and the five level curves; the band is drawn thick.

```python
ax.plot(k_band[:13], c_theory * k_band[:13], ":", color="black",
        label="first order: $c\\,k$, $c = 1.9051$")
ax.axhline(odd0[0], color="gray", linewidth=0.8, linestyle="-.")
ax.annotate("bulk edge 1.2923", (2.6, odd0[0] - 0.55), fontsize=8,
            color="gray")  # just below the dash-dotted line
```

The straight line $ck$ for the first 13 momenta ($k \le 0.6$), and a dash-dotted horizontal line at the bulk edge, the odd level at $k = 0$ (`odd0[0]`), with its name written just below it.

```python
ax.set_xlabel("3-momentum $k$ (units of $H$), slice $a_{4,0} = 0$")
ax.set_ylabel("level $\\varepsilon$ (units of $m$)")
ax.set_title("the free levels at nonzero 3-momentum ($m = 1$, $L = 3$)")
ax.legend(fontsize=7, loc="center left", bbox_to_anchor=(1.01, 0.5))
save_figure(fig, "band_structure",
            "The free Kohn-Sham levels against the 3-momentum $k$ (units of "
            ...)
```

Labels, title, and a legend placed outside the panel on the right (`bbox_to_anchor=(1.01, 0.5)` anchors its left centre just beyond the right edge). **What figure 14c.1 shows.** The brane band starts at 0, follows the dotted line $ck$ for small $k$, bends below it and then rises almost straight to about $5\,m$ at $k = 4$. Its mirror image, the dashed band of $j = -1$, falls to about $-5\,m$: it belongs to the sea. The three other levels start at or above the bulk edge $1.2923\,m$ (the even level 1 of $j = -1$ dips slightly below its start before rising) and rise roughly parallel to the band. Nothing else enters the region between the band and the bulk edge.

**In [5], the slope.**

```python
Ms, Hs, Ls = sp.symbols("M H L", positive=True)
ys, a4s = sp.symbols("y a", real=True)
ratio = (sp.integrate(sp.exp(-Hs * ys - a4s) * sp.exp(2 * Ms * ys), (ys, -Ls, 0))
         / sp.integrate(sp.exp(2 * Ms * ys), (ys, -Ls, 0)))  # step 3
formula = (sp.exp(-a4s) * 2 * Ms / (2 * Ms - Hs) * (1 - sp.exp(-(2 * Ms - Hs) * Ls))
           / (1 - sp.exp(-2 * Ms * Ls)))  # step 4
```

Symbols, the ratio of the two integrals of Section 14.19 computed by `sp.integrate(expression, (variable, lower, upper))`, and the closed formula.

```python
same = sp.simplify((ratio - formula).subs({Ms: 1, Hs: 1, Ls: 3})) == 0 and \
    sp.simplify((ratio - formula).subs({Ms: 2, Hs: 1, Ls: 3})) == 0
c_exact = float(formula.subs({Ms: 1, Hs: 1, Ls: 3, a4s: 0}))
```

The ratio and the formula agree exactly for $(M, H, L) = (1, 1, 3)$ and $(2, 1, 3)$, for every slice (the symbol $a$ stays free); `subs` with a dictionary replaces several symbols at once. `c_exact` is the number $c$ for $M = H = 1$, $L = 3$, slice 0.

```python
theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                    .read_text(encoding="utf-8"))
c_record = float(theory["checksNumeric"]["braneBandSlope_M1_H1_L3_a0"])
report("slope c for M = H = 1, L = 3, a4,0 = 0", f"{c_exact:.13f}", "m/H")
check(same and abs(c_exact - c_record) < 1e-15 and abs(c_exact - c_theory) < 1e-15
      and record_check("brane_band_slope",
                       "Revision/kohn_sham/reports/ks-theory-python.json"),
      "c = e^(-a4,0) (2M/(2M - H)) (1 - e^(-(2M-H)L))/(1 - e^(-2ML)) = 1.9051482536",
      record="Revision/kohn_sham/ks-theory.json, checksNumeric "
             "braneBandSlope_M1_H1_L3_a0")
```

The value of the record, the RESULT line $1.9051482536449$, and the check: the formula, the record's number, the short form $2/(1 + e^{-3})$ of In [4] and the verdict of the sympy report all agree.

```python
y_f, a_zero, b_zero, simpson = orbital(0.0)  # the zero mode at k = 0
c_integral = float(np.sum(simpson * np.exp(-y_f) * a_zero ** 2))  # step 3
check(abs(c_integral - c_exact) < 1e-9,
      "the integral of kappa a^2 over the numerical zero mode gives c")
```

The numerical zero mode, and the Hellmann-Feynman integral $\int\kappa\,a^2dy$ (with $\kappa = e^{-y}$ at the slice 0) by Simpson's rule: it equals $c$ to $10^{-9}$.

```python
tiny = np.array([1e-4, 2e-4] * 5)  # two small momenta at each slice
slice_of = np.repeat(SLICES, 2)
small = levels(tiny, 1.0, "even", 0, a4=slice_of).reshape(5, 2)
c_numeric = (4.0 * small[:, 0] / 1e-4 - small[:, 1] / 2e-4) / 3.0
```

The two small momenta $10^{-4}$ and $2\times10^{-4}$, five times; `np.repeat(SLICES, 2)` repeats every slice twice (0, 0, 0.5, 0.5, ...), so that each slice gets both momenta. The ten band levels in one call, arranged as 5 rows of 2, and the Richardson combination $(4R(k_1) - R(k_2))/3$ of Section 14.19 for each slice.

```python
rows = read_csv(f"{SPECTRUM}/brane-band-slope.csv")
c_rows = np.array([float(r["c_numeric"]) for r in rows])
for a_, c_ in zip(SLICES, c_numeric):
    say(f"slice a4,0 = {a_}: c numerical {c_:.12f}, "
        f"c e^(-a4,0) exact {c_exact * math.exp(-a_):.12f}")
```

The Rust solver's numerical slopes, and a printed comparison of the notebook's numerical slopes with the exact $c\,e^{-a_{4,0}}$ at each slice (Out [5]).

```python
check(np.max(np.abs(c_numeric / c_rows - 1.0)) < 1e-11
      and np.max(np.abs(c_numeric / (c_exact * np.exp(-np.array(SLICES))) - 1.0))
      < 1e-9 and record_check("free_brane_band_slope"),
      "the numerical slope equals c e^(-a4,0) at all five slices",
      record=f"{SPECTRUM}/brane-band-slope.csv and {RUST_REPORT}, check "
             "free_brane_band_slope")
```

The notebook's slopes equal the Rust slopes to $10^{-11}$ and the exact ones to $10^{-9}$ (relative), and the Rust check passed.

```python
c_by_L = {}
for L_ in (2.0, 4.0):  # the slope for two other cutoffs
    pair = levels(np.array([1e-4, 2e-4]), 1.0, "even", 0, L=L_, G=round(300 * L_))
    c_by_L[L_] = (4.0 * pair[0] / 1e-4 - pair[1] / 2e-4) / 3.0
c_by_L[3.0] = float(c_numeric[0])
exact_by_L = {L_: 2.0 / (1.0 + math.exp(-L_)) for L_ in (2.0, 3.0, 4.0)}
```

The slope for the cutoffs $L = 2$ and $L = 4$ by the same Richardson combination (with $G = 300L$ steps, the same step $h = 1/300$), the slope for $L = 3$ from the slice 0 above, and the exact $2/(1 + e^{-L})$ for the three cutoffs, as a dictionary comprehension.

```python
say("c for L = 2, 3, 4: " + ", ".join(f"{c_by_L[L_]:.6f}" for L_ in (2.0, 3.0, 4.0))
    + " (exact " + ", ".join(f"{exact_by_L[L_]:.6f}" for L_ in (2.0, 3.0, 4.0)) + ")")
check(all(abs(c_by_L[L_] - exact_by_L[L_]) < 1e-9 for L_ in (2.0, 4.0)),
      "the slope formula holds for L = 2 and L = 4 too")
```

A printed line with the three numerical and the three exact slopes, $1.761594$, $1.905148$, $1.964028$ (they agree in all six decimals), and the check for the two new cutoffs. Out [5] shows four PASS lines.

**In [6], figure 2.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
a_grid = np.linspace(0.0, 2.0, 201)
left.semilogy(a_grid, c_exact * np.exp(-a_grid), color="C0",
              label="exact $c\\,e^{-a_{4,0}}$")
left.semilogy(SLICES, c_numeric, "o", color="C3", label="numerical (Richardson)")
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("slope $c$ (units of $m/H$, logarithmic)")
left.set_title("the slope along the history")
left.legend(fontsize=8)
```

Left panel: the exact slope $c\,e^{-a_{4,0}}$ for 201 slices from 0 to 2 on a logarithmic axis, and the five numerical values as red dots.

```python
L_grid = np.linspace(0.5, 6.0, 221)
right.plot(L_grid, 2.0 / (1.0 + np.exp(-L_grid)), color="C0",
           label="exact $2/(1 + e^{-L})$")
right.plot(list(c_by_L), list(c_by_L.values()), "o", color="C3", label="numerical")
right.axhline(2.0, color="gray", linestyle=":", label="limit $2M/(2M - H) = 2$")
right.set_xlabel("cutoff $L$ (units of $1/H$)")
right.set_ylabel("slope $c$ at $a_{4,0} = 0$")
right.set_title("the slope against the cutoff ($M = H = 1$)")
right.legend(fontsize=8)
save_figure(fig, "band_slope",
            "The slope $c = d\\varepsilon/dk$ of the brane band at $k = 0$ "
            ...)
```

Right panel: the exact slope $2/(1 + e^{-L})$ for cutoffs from 0.5 to 6, the three numerical values (`list(c_by_L)` is the list of the keys of the dictionary, the cutoffs, and `c_by_L.values()` the slopes), and the limit 2 as a dotted line. **What figure 14c.2 shows.** Left: the five dots lie on a straight line on the logarithmic axis, falling from $1.905$ to $0.258$: the slope decreases exactly like $e^{-a_{4,0}}$, the redshift. Right: the slope grows with the cutoff and approaches 2 from below; the three dots lie on the curve.

**In [7], the rescaling identity and the gap of $N = 8$.**

```python
test_k = [0.25, 1.0, 2.5]
test_sectors = [(1.0, "even", 0), (1.0, "odd", 0), (-1.0, "even", 1)]
combos = [(a_, k_, s_) for a_ in SLICES for k_ in test_k for s_ in test_sectors]
```

Three momenta and three sectors (the band, the odd label 0, the even label 1 of $j = -1$), and all $5 \times 3 \times 3 = 45$ combinations with the slices.

```python
at_slice = levels(np.array([k_ for a_, k_, s_ in combos]),
                  np.array([s_[0] for a_, k_, s_ in combos]),
                  np.array([s_[1] for a_, k_, s_ in combos]),
                  np.array([s_[2] for a_, k_, s_ in combos]),
                  a4=np.array([a_ for a_, k_, s_ in combos]))
at_zero = levels(np.array([k_ * math.exp(-a_) for a_, k_, s_ in combos]),
                 np.array([s_[0] for a_, k_, s_ in combos]),
                 np.array([s_[1] for a_, k_, s_ in combos]),
                 np.array([s_[2] for a_, k_, s_ in combos]))
```

The 45 levels twice: at their slices with the momentum $k$, and at the slice 0 with the momentum $ke^{-a_{4,0}}$ (`a4` is then the default 0).

```python
check(np.max(np.abs(at_slice - at_zero)) < 1e-12
      and record_check("free_rescaling_relation_and_band_monotone"),
      "eps(k, a4,0) = eps(k e^(-a4,0), 0) for 45 levels at the five slices",
      record=f"{RUST_REPORT}, check free_rescaling_relation_and_band_monotone")
```

They agree to $10^{-12}$: the rescaling identity of Section 14.7 for the levels.

```python
k_fig = np.linspace(0.0, 4.0, 41)
band_slices = levels(np.tile(k_fig, 5), 1.0, "even", 0,
                     a4=np.repeat(SLICES, len(k_fig))).reshape(5, len(k_fig))
gaps = levels(np.full(5, 0.25), 1.0, "even", 0, a4=np.array(SLICES))
```

For the figure, the band at 41 momenta at each of the five slices: `np.tile(k_fig, 5)` repeats the whole list five times, `np.repeat` repeats each slice 41 times, so the pairs match. Then the gaps: the band at $k = 0.25$ at the five slices.

```python
shells_record = read_csv(f"{SPECTRUM}/closed-shells.csv")
gap_record = [float(r["gap"]) for r in shells_record if r["N_closed"] == "8"]
for a_, g_ in zip(SLICES, gaps):
    say(f"slice a4,0 = {a_}: gap of the free N = 8 state {g_:.10f} m")
check(len(gap_record) == 5 and np.max(np.abs(gaps - np.array(gap_record))) < 1e-11,
      "the N = 8 gaps at the five slices equal the record",
      record=f"{SPECTRUM}/closed-shells.csv, rows N_closed = 8")
```

The column gap of the five rows with $N = 8$ of the closed-shell record, the five printed gaps (the table of Section 14.20) and the check. Out [7] shows two PASS lines.

**In [8], figure 3.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), sharey=True)
for index, a_ in enumerate(SLICES):
    left.plot(k_fig, band_slices[index], label=f"$a_{{4,0}} = {a_}$")
    right.plot(k_fig * math.exp(-a_), band_slices[index], "o", markersize=3,
               label=f"$a_{{4,0}} = {a_}$")
right.plot(k_fig, band_slices[0], color="black", linewidth=0.8,
           label="slice 0 band")
```

Left: the band against $k$ at each slice. Right: the same levels against the redshifted momentum $ke^{-a_{4,0}}$ as dots, and the band of the slice 0 as a thin black line.

```python
left.set_xlabel("3-momentum $k$ (units of $H$)")
left.set_ylabel("brane band $\\varepsilon$ (units of $m$)")
left.set_title("the band at five slices")
left.legend(fontsize=8)
right.set_xlabel("redshifted momentum $k\\,e^{-a_{4,0}}$ (units of $H$)")
right.set_title("all slices on one curve")
right.legend(fontsize=7)
save_figure(fig, "band_redshift",
            "The brane band along the prescribed deflating history. Left: the "
            ...)
```

**What figure 14c.3 shows.** Left: five curves from the origin, the later slices lower: at $k = 4$ the band is near $5\,m$ at the slice 0 and below $1\,m$ at the slice 2. Right: all dots fall on the black curve; a later slice covers only a shorter piece of it (up to $4e^{-a_{4,0}}$). This is the rescaling identity: nothing but the momentum scale changes along the history.

**In [9], the block-type symmetries.**

```python
sym_k = [0.25 * math.sqrt(n2) for n2 in (0, 1, 2, 5, 9)]
sym_l = list(range(-3, 4))
grid = [(k_, l_) for k_ in sym_k for l_ in sym_l]
K_s = np.array([k_ for k_, l_ in grid])
L_s = np.array([l_ for k_, l_ in grid])
```

The momenta of five shells ($k = 0.25\sqrt{n^2}$ for $n^2 = 0, 1, 2, 5, 9$), the labels $-3$ to $3$, and their 35 combinations as two arrays.

```python
plus_even = levels(K_s, 1.0, "even", L_s)
minus_even = levels(K_s, -1.0, "even", -L_s)
plus_odd = levels(K_s, 1.0, "odd", L_s)
minus_odd = levels(K_s, -1.0, "odd", -L_s - 1)
flipped_even = levels(-K_s, -1.0, "even", L_s)
flipped_odd = levels(-K_s, -1.0, "odd", L_s)
```

Six sets of levels: both parities of $j = +1$; those of $j = -1$ with the mirrored labels ($l \to -l$ for even parity and $l \to -l - 1$ for odd parity, the label map of Section 14.13, because the target $\pi/2 + l\pi$ goes to $-(\pi/2 + l\pi) = \pi/2 + (-l - 1)\pi$); and those of $j = -1$ at the reversed momentum $-k$ with the same labels.

```python
mirror = max(np.max(np.abs(plus_even + minus_even)),
             np.max(np.abs(plus_odd + minus_odd)))
flip = max(np.max(np.abs(flipped_even - plus_even)),
           np.max(np.abs(flipped_odd - plus_odd)))
check(mirror < 1e-12 and flip < 1e-12 and record_check("free_block_type_symmetries"),
      "spec h_(-1) = -spec h_(+1) and eps_(-1)(-k) = eps_(+1)(k), label by label",
      record=f"{RUST_REPORT}, check free_block_type_symmetries")
```

The two relations of Section 14.5: the levels of $j = -1$ are minus those of $j = +1$ (`mirror`), and the level of $(-1, -k)$ equals that of $(+1, k)$ (`flip`); both to $10^{-12}$, label by label.

```python
k_mirror = np.linspace(0.0, 2.0, 41)
fig_labels = list(range(-2, 3))
plus_curves = levels(np.tile(k_mirror, 5), 1.0, "even",
                     np.repeat(fig_labels, len(k_mirror))).reshape(5, -1)
minus_curves = levels(np.tile(k_mirror, 5), -1.0, "even",
                      np.repeat(fig_labels, len(k_mirror))).reshape(5, -1)
say("even levels at k = 2, labels -2 ... 2:")
say("  j = +1: " + ", ".join(f"{x:.4f}" for x in plus_curves[:, -1]))
say("  j = -1: " + ", ".join(f"{x:.4f}" for x in minus_curves[:, -1]))
```

For the figure, the even levels of labels $-2$ to $2$ for 41 momenta from 0 to 2, for both types (`reshape(5, -1)`: five rows, the length of each row worked out by numpy). The printout of the last column, $k = 2$: for $j = +1$ the levels $-6.3742$, $-4.4814$, $2.6976$, $5.4109$, $7.1695$ and for $j = -1$ the same numbers with the opposite signs, in the opposite order (Out [9]).

**In [10], figure 4.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
for row, label in enumerate(fig_labels):
    left.plot(k_mirror, plus_curves[row], label=f"label {label}")
    right.plot(k_mirror, minus_curves[row], label=f"label {label}")
for ax, title in ((left, "block type $j = +1$"), (right, "block type $j = -1$")):
    ax.axhline(0.0, color="black", linewidth=0.6)
    ax.set_xlabel("3-momentum $k$ (units of $H$)")
    ax.set_title(title + ", even parity")
    ax.legend(fontsize=7, loc="upper left")
left.set_ylabel("level $\\varepsilon$ (units of $m$)")
save_figure(fig, "block_type_mirror",
            "The even-parity levels with labels $-2$ to $2$ against the "
            ...)
```

Five curves in each panel, the zero line, labels and titles (a loop over the two panels sets what they share). **What figure 14c.4 shows.** Left ($j = +1$): the label 0 curve starts at 0 and rises (the brane band); labels 1 and 2 start at $1.448$ and $2.321$ and rise; labels $-1$ and $-2$ are their mirror images below zero. Right ($j = -1$): the same picture turned upside down: the label 0 curve falls from 0 (the sea partner of the band).

**In [11], the tip angle.**

```python
tip_rows = read_csv(f"{SPECTRUM}/tip-angle.csv")
tip_k = np.array([0.25, 0.5, 1.0])
tip_levels = {th: levels(tip_k, 1.0, "even", 0, tip=th) for th in (0.0, 0.5, 1.0)}
suppression = np.exp(-tip_k * (math.exp(3.0) - 1.0))  # H = 1, L = 3
worst_tip, below = 0.0, True
```

The record of the Rust solver (9 rows), the three momenta of the record, the band at these momenta for the three tip angles (a dictionary from the angle to an array of three levels; `tip=th` is handed on to `shoot` through `**options`), the suppression factor $\exp(-k(e^{3} - 1))$ at the brane for $H = 1$, $L = 3$ and the slice 0, and two variables for the results.

```python
for r in tip_rows:
    i_k = list(tip_k).index(float(r["k"]))
    mine = tip_levels[float(r["theta_tip"])][i_k]
    worst_tip = max(worst_tip, abs(mine - float(r["eps"])))
    shift = mine - tip_levels[0.0][i_k]
    below &= abs(shift) <= max(suppression[i_k], 1e-12)
check(len(tip_rows) == 9 and worst_tip < 1e-11 and below
      and record_check("free_tip_angle_insensitivity"),
      "the band levels equal tip-angle.csv; the shifts are below the suppression",
      record=f"{SPECTRUM}/tip-angle.csv and {RUST_REPORT}, check "
             "free_tip_angle_insensitivity")
```

For every row: the position of its momentum in the list (`index` finds it), the notebook's level for its angle and momentum, the largest difference from the recorded level, and the shift from the angle 0, which must not exceed the suppression factor (or $10^{-12}$, the size of rounding, whichever is larger).

```python
k_tip = np.linspace(0.1, 1.0, 10)
shifts = {th: np.abs(levels(k_tip, 1.0, "even", 0, tip=th)
                     - levels(k_tip, 1.0, "even", 0, tip=0.0)) for th in (0.5, 1.0)}
def shown(x):
    return f"{x:.1e}" if x >= 1e-14 else "below 1e-14 (rounding)"


for k_, s5, s10 in zip(k_tip, shifts[0.5], shifts[1.0]):
    say(f"k = {k_:.1f}: shift for theta = 0.5: {shown(s5)}, for theta = 1: "
        f"{shown(s10)}")
```

The shifts for ten momenta $0.1, 0.2, \dots, 1$ and the angles 0.5 and 1. The small function `shown` writes a shift with one decimal and an exponent, or, below $10^{-14}$, the words "below 1e-14 (rounding)": such tiny numbers are rounding errors and differ from computer to computer, and the printed output of a notebook must be the same everywhere. Out [11] prints the ten lines of Section 14.20: $4.6\times10^{-4}$ and $1.2\times10^{-3}$ at $k = 0.1$, down to $7.7\times10^{-14}$ and $2.7\times10^{-13}$ at $k = 0.8$, and rounding from $k = 0.9$ on.

**In [12], figure 5.**

```python
fig, ax = plt.subplots(figsize=(7.5, 4.4))
k_line = np.linspace(0.1, 1.0, 91)
ax.semilogy(k_line, np.exp(-k_line * (math.exp(3.0) - 1.0)), color="black",
            label="suppression $\\exp(-k(e^{HL} - 1)/H)$")
for th, marker in ((0.5, "o"), (1.0, "s")):
    ax.semilogy(k_tip, np.maximum(shifts[th], 1e-16), marker, markersize=5,
                label=f"$|\\varepsilon(\\theta = {th}) - \\varepsilon(\\theta = 0)|$")
```

The suppression factor as a line on a logarithmic axis, and the shifts as circles and squares; `np.maximum(x, 1e-16)` replaces any shift below $10^{-16}$ (or exactly 0, whose logarithm does not exist) by $10^{-16}$, so that it can be drawn.

```python
ax.axhline(1e-15, color="gray", linestyle=":", linewidth=0.8)
ax.annotate("rounding level", (0.75, 2e-15), fontsize=8, color="gray")
ax.set_xlabel("3-momentum $k$ (units of $H$)")
ax.set_ylabel("shift of the band level (units of $m$, logarithmic)")
ax.set_title("the band does not feel the tip angle ($L = 3$, slice 0)")
ax.legend(fontsize=8)
save_figure(fig, "tip_insensitivity",
            "The change of the brane-band level when the tip condition "
            ...)
```

A dotted line at $10^{-15}$, the rounding level, with its name. **What figure 14c.5 shows.** Both rows of markers fall steeply, by a factor 11 to 33 per step of 0.1, much faster than the black suppression line, and stay below it by two to six powers of ten; the squares ($\theta = 1$) lie a little above the circles ($\theta = 0.5$). At $k = 0.9$ and $1$ the markers sit at the rounding level, where their exact positions are noise.

**In [13], shells and particle labels.**

```python
def shells(n2_max):
    r = math.isqrt(n2_max) + 1
    count = [0] * (n2_max + 1)
    for x in range(-r, r + 1):
        for y_ in range(-r, r + 1):
            for z_ in range(-r, r + 1):
                s = x * x + y_ * y_ + z_ * z_
                if s <= n2_max:
                    count[s] += 1
    return [(n2, c) for n2, c in enumerate(count) if c > 0]
```

The shells up to $n^2_{\max}$ by counting: `math.isqrt` is the whole-number square root (rounded down), so every integer vector with $n^2 \le n^2_{\max}$ has entries between $-r$ and $r$; the three loops visit all of them and count each $n^2$. The result is the list of pairs $(n^2, r_3(n^2))$ with $r_3 > 0$.

```python
check(shells(9) == [(0, 1), (1, 6), (2, 12), (3, 8), (4, 6), (5, 24), (6, 24),
                    (8, 12), (9, 30)],
      "r3(n2) = 1, 6, 12, 8, 6, 24, 24, 12, 30 for n2 = 0, 1, 2, 3, 4, 5, 6, 8, 9")
SECTORS = [(1, "even"), (1, "odd"), (-1, "even"), (-1, "odd")]
SIGN = {1: "+1", -1: "-1"}
```

The first values of $r_3$ (Section 14.21; no shell 7), the four sectors of a shell, and the texts $+1$, $-1$ used in the names of the levels.

```python
def lowest_particle_labels(pairs, a4):
    k_ = np.array([0.25 * math.sqrt(n2) for n2, _, _, _ in pairs])
    j_ = np.array([float(j) for _, _, j, _ in pairs])
    par = np.array([p for _, _, _, p in pairs])
    phi0 = shoot(0.0, k_, j_, a4)
    offset = np.where(par == "even", 0.0, 0.5 * np.pi)
    l_min = np.floor((phi0 - offset) / np.pi).astype(int) + 1
    nearest = np.round((phi0 - offset) / np.pi).astype(int)
    zero_mode = (k_ == 0.0) & (np.abs(phi0 - offset - nearest * np.pi) < 1e-12)
    return np.where(zero_mode, nearest, l_min), phi0, offset, k_, j_, par
```

For a list of sectors $(n^2, r_3, j, \text{parity})$: their momenta, types and parities as arrays, and $\Phi(0)$, the shooting function at $\varepsilon = 0$. Since $\Phi$ grows with $\varepsilon$, a label is a particle label when its target lies above $\Phi(0)$; the first such label is $\lfloor(\Phi(0) - \text{offset})/\pi\rfloor + 1$ (`np.floor` rounds down; `astype(int)` makes whole numbers). The exception is a zero mode: at $k = 0$, when $\Phi(0)$ lies exactly on a target (to $10^{-12}$; `&` is "and" for arrays), that label itself is the first particle label (the convention of Section 14.21). The function returns these labels and the arrays it made.

```python
pairs30 = [(n2, r3, j, p) for n2, r3 in shells(30) for j, p in SECTORS]
l_min, phi0, offset, k30, j30, p30 = lowest_particle_labels(pairs30, 0.0)
e_first = levels(k30, j30, p30, l_min)
e_below = levels(k30, j30, p30, l_min - 1)
zero_k = k30 == 0.0
```

All sectors of the shells up to $n^2 = 30$; their first particle labels at the slice 0; the levels of these labels and of the labels just below; and a marker for the sectors with $k = 0$.

```python
branch_ok = (np.all(e_below < 0.0)
             and np.all(e_first[zero_k & (p30 == "even")] == 0.0)
             and np.all(e_first[~(zero_k & (p30 == "even"))] > 0.0))
closest = float(min(np.min(e_first[~(zero_k & (p30 == "even"))]),
                    np.min(-e_below)))
report("level closest to zero away from the zero modes (n2 <= 30)",
       f"{closest:.4f}", "m")
check(branch_ok and f"{closest:.4f}" == "0.4307"
      and record_check("free_particle_branch_labels"),
      "particles are the labels l >= l_min in every sector (n2 <= 30)",
      record=f"{RUST_REPORT}, check free_particle_branch_labels")
```

The particle rule holds when every level just below the first particle label is negative, the first particle level is exactly 0 in the even sectors at $k = 0$ (the zero modes) and positive in all other sectors (`~` is "not" for arrays; an array indexed by a true-false array keeps the entries marked true). `closest` is the level nearest to zero apart from the zero modes, from above or from below: $0.4307\,m$, as in the Rust check. Out [13] shows two PASS lines.

**In [14], the closed shells.**

```python
def closed_shells(a4, n2_max, e_max=1.6):
    pairs = [(n2, r3, j, p) for n2, r3 in shells(n2_max) for j, p in SECTORS]
    l_next, _, _, k_, j_, par = lowest_particle_labels(pairs, a4)
    found_levels = []  # (energy, degeneracy, name, n2)
    active = np.arange(len(pairs))
```

The free aufbau at one slice, up to the energy $1.6\,m$. For every sector the next label to compute starts at its first particle label; `active` lists the sectors that are still open (all, at the start).

```python
    while len(active) > 0:  # one more label in every sector that is still open
        e_ = levels(k_[active], j_[active], par[active], l_next[active], a4=a4)
        keep = e_ <= e_max
        for index, energy in zip(active[keep], e_[keep]):
            n2, r3, j, p = pairs[index]
            found_levels.append((float(energy), 4.0 * r3,
                                 f"{n2}:{SIGN[j]}:{p}:{l_next[index]}", n2))
        active = active[keep]
        l_next[active] += 1
```

In each pass the next level of every open sector is computed at once; the levels at or below $1.6\,m$ are stored with their degeneracy $4r_3(n^2)$ and a name such as `1:+1:even:0` (shell, block type, parity, label); a sector whose next level lies above $1.6\,m$ is closed, because its higher labels lie higher still; the open sectors move on to the next label.

```python
    with_levels = {n2 for _, _, _, n2 in found_levels}
    stop = next(n2 for n2, _ in shells(n2_max) if n2 > 0 and n2 not in with_levels)
    found_levels = [lev for lev in found_levels if lev[3] < stop]
    found_levels.sort(key=lambda lev: (lev[0], lev[2]))
```

The set of shells that have a level below $1.6\,m$, the first shell $n^2 > 0$ without one (the band rises with $|\mathbf k|$, so no later shell can contribute; this is the rule of the Rust solver), only the levels of the shells before it, sorted by energy and, for equal energies, by name.

```python
    table, total, i = [], 0.0, 0
    while i < len(found_levels):  # group the degenerate levels
        e0, group, names = found_levels[i][0], 0.0, []
        while i < len(found_levels) and found_levels[i][0] - e0 <= 1e-9:
            group += found_levels[i][1]
            names.append(found_levels[i][2])
            i += 1
        total += group
        following = found_levels[i][0] if i < len(found_levels) else float("nan")
        table.append((int(total), e0, following, ";".join(names)))
    return table, stop
```

Walking through the sorted levels, the levels within $10^{-9}$ of the first level of a group are collected into one degenerate group; after each group the running total $N$ is a closed shell, stored with the energy of the group, the energy of the next level (or `nan`, "not a number", at the end) and the names of the group joined by semicolons.

```python
agree = True
tables = {}
for a_, n2_max in ((0.0, 40), (0.5, 80)):
    table, stop = closed_shells(a_, n2_max)
    tables[a_] = table
    mine_rows = [r for r in shells_record if float(r["a4"]) == a_]
    same = len(table) == len(mine_rows) and all(
        int(r["N_closed"]) == t[0] and r["levels_of_the_last_group"] == t[3]
        and abs(float(r["eps_last_filled"]) - t[1]) < 1e-11
        for r, t in zip(mine_rows, table))
    agree &= same and stop < n2_max
    say(f"slice {a_}: {len(table)} closed shells up to 1.6 m, the first shell "
        f"without a level below 1.6 m is n2 = {stop}; equal to the record: {same}")
check(agree, "the closed shells of the slices 0 and 0.5 equal the record row by row",
      record=f"{SPECTRUM}/closed-shells.csv, rows a4 = 0 and 0.5")
say("slice 0: N = " + ", ".join(str(t[0]) for t in tables[0.0]))
```

The closed shells at the slices 0 (shells up to $n^2 = 40$) and 0.5 (up to 80; the redshifted band needs more shells), compared row by row with the record: the same numbers $N$, the same names of the last group, the same energies to $10^{-11}$; and the stopping shell must lie inside the range searched. Out [14] prints 22 closed shells at the slice 0 (stopping shell $n^2 = 20$) and 55 at the slice 0.5 (stopping shell 53), and the list of $N$ at the slice 0.

```python
bulk_edge = float(min(levels(0.0, 1.0, "odd", 0), levels(0.0, 1.0, "even", 1)))
below_edge = [t for t in tables[0.0] if t[1] < bulk_edge and t[2] - t[1] > 1e-6]
N_large = below_edge[-1][0]
N_mid = min((t[0] for t in below_edge if t[0] >= 8),
            key=lambda n: abs(n - N_large / 4))
```

The bulk edge, the smaller of the odd level 0 and the even level 1 at $k = 0$; the closed shells whose last level lies below it (and are separated from the next level by more than $10^{-6}$); $N_{\rm large}$, the last of them; and $N_{\rm mid}$, the one nearest to $N_{\rm large}/4$ (`min` with `key=` picks the element with the smallest value of the key function).

```python
parameters = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                        .read_text(encoding="utf-8"))
numbers = parameters["particleNumbers"]
report("bulk edge", f"{bulk_edge:.12f}", "m")
report("particle numbers N", f"8, {N_mid}, {N_large}")
check(abs(bulk_edge - numbers["bulkEdge"]) < 1e-12 and N_large == 688
      and N_mid == 136 and numbers["values"] == [8.0, 136.0, 688.0],
      "the bulk edge 1.2922928281 and the particle numbers 8, 136, 688",
      record="Revision/kohn_sham/results/parameters.json, particleNumbers")
```

The record of the Revision runs, the two RESULT lines (the bulk edge $1.292292828069\,m$ and the numbers 8, 136, 688) and the check against the record. Out [14] shows two PASS lines.

**In [15], figure 6.**

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
for a_, style in ((0.0, "-"), (0.5, "--")):
    energies = [t[1] for t in tables[a_]]
    counts = [t[0] for t in tables[a_]]
    ax.step(energies, counts, style, where="post",
            label=f"slice $a_{{4,0}} = {a_}$")
```

For each slice a **staircase**: `step(x, y, where="post")` draws a horizontal line from each point to the next value of $x$, then a vertical jump; here $x$ is the energy of the last filled group and $y$ the closed-shell number $N$.

```python
ax.axvline(bulk_edge, color="gray", linestyle="-.", linewidth=0.8)
ax.annotate("bulk edge", (bulk_edge + 0.015, 15), fontsize=8, color="gray")
last_filled = {t[0]: t[1] for t in tables[0.0]}  # N -> its last filled level
for n_ in (8, N_mid, N_large):
    t_ = last_filled[n_]
    ax.plot([t_], [n_], "o", color="C3")
    ax.annotate(f"N = {n_}", (t_ + 0.02, n_ * 0.75), fontsize=8, color="C3")
```

A vertical line at the bulk edge, and the three particle numbers of the Revision runs as red dots at their last filled levels, with their names.

```python
ax.set_yscale("log")
ax.set_xlabel("energy of the last filled level (units of $m$)")
ax.set_ylabel("closed-shell particle number $N$ (logarithmic)")
ax.set_title("the free aufbau: closed shells up to $1.6\\,m$")
ax.legend(fontsize=8, loc="upper left")
save_figure(fig, "closed_shells",
            "The closed shells of the free aufbau: the particle number $N$ "
            ...)
```

A logarithmic vertical axis, labels and title. **What figure 14c.6 shows.** At the slice 0 (solid) the staircase stays at $N = 8$ up to $0.43\,m$ (the gap), then climbs in steps, one per lattice shell of the band, to $688$ just below the bulk edge and to $1552$ at $1.584\,m$, the last group below $1.6\,m$. At the slice 0.5 (dashed) the first step comes already at $0.27\,m$ and the staircase lies far higher: the redshifted band puts many more states below the same energy.

**In [16], the last check.**

```python
figure_names = ["14c_1_band_structure.png", "14c_2_band_slope.png",
                "14c_3_band_redshift.png", "14c_4_block_type_mirror.png",
                "14c_5_tip_insensitivity.png", "14c_6_closed_shells.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all six figure files of this notebook exist")
all_checks_passed()
```

The six figure files must exist; the last line prints ALL 15 CHECKS PASSED (notebook 14c). The 15 checks are: 2 in In [3], 4 in In [5], 2 in In [7], 1 in In [9], 1 in In [11], 2 in In [13], 2 in In [14] and 1 in In [16].

### 14.26 The exact local exchange of the contact interaction

**What is needed.** The quanta of dirac16complex interact through the contact term $U = \tfrac\lambda2S^2$ of the Lagrangian, with the scalar density $S = \bar\Psi\Psi = \Psi^\dagger C\Psi$, normal ordered in the quantised theory; $\lambda > 0$ is a repulsion, and $\lambda$ has the dimension $\text{mass}^{-6}$ because the field has the dimension $7/2$ in eight dimensions (`Revision/kohn_sham/ks-theory.json`, units). The Kohn-Sham model needs the energy of this interaction in a Kohn-Sham state, a Slater determinant of orbitals or a thermal mixture of them (Chapter 13), as a function of the densities. This section derives it exactly. The result is surprising and very useful: the exchange energy, which for most interactions depends on the orbitals in a complicated way, is here an ordinary function of two densities at the same point.

**The expectation-value rule (Chapter 10).** For one quantum in the mode $u$ (a column of 16 numbers), the expectation value of a density $\Psi^\dagger X\Psi$ is $u^\dagger BXu$, with the matrix $B$ of the indefinite (Krein) inner product. For many independent quanta in the modes $u$ with the occupations $f$ (1 for filled, 0 for empty, or a number between at a temperature),

$$
\langle\Psi^\dagger X\Psi\rangle = \mathrm{Tr}(X\rho), \qquad \rho = \sum_{\rm occupied} f\,uu^\dagger B .
$$

Rule: $\mathrm{Tr}(Xuu^\dagger B) = \mathrm{Tr}(u^\dagger BXu) = u^\dagger BXu$, because a trace does not change when the first factors are moved to the end, and $u^\dagger BXu$ is a single number. The $16 \times 16$ matrix $\rho$ is the **one-body matrix** of the state. The number density and the scalar density are

$$
n = \langle\Psi^\dagger B\Psi\rangle = \mathrm{Tr}(B\rho), \qquad S = \langle\bar\Psi\Psi\rangle = \langle\Psi^\dagger C\Psi\rangle = \mathrm{Tr}(C\rho) .
$$

Status: the rule is the expectation-value rule of the canonical quantisation (Chapter 10), stated in the record as exchange.expectationRule of `Revision/kohn_sham/ks-theory.json`; the two density formulas are the check gas_densities of both theory reports.

**The plane waves of the good sector.** In flat space ($H = 0$, so $W = 1$ and $\kappa = 1$ at the slice 0) a plane wave $e^{-i\varepsilon x_4 + i\mathbf p\cdot\mathbf x}u$ with the momentum $\mathbf p = (p_1, p_2, p_3, p_8)$ along the four space-like directions $x_1, x_2, x_3, x_8$ (the good sector has no momentum along the extra times) solves $h_{\mathbf p}u = \varepsilon u$ with

$$
h_{\mathbf p} = M(-i\gamma^{(x_4)}) - \sum_a p_a\,\gamma^{(x_4)}\gamma^{(a)} \qquad (a = x_1, x_2, x_3, x_8) .
$$

Rule: the Hamiltonian $h$ of Section 14.4 with $v = 0$; its derivative term $i\gamma^{(x_4)}\gamma^{(x_8)}\partial_y$ acting on $e^{ip_8y}$ gives $i\gamma^{(x_4)}\gamma^{(x_8)}(ip_8) = -p_8\gamma^{(x_4)}\gamma^{(x_8)}$. Its square, line by line:

$$
\big(-i\gamma^{(x_4)}\big)^2 = -\big(\gamma^{(x_4)}\big)^2 = 1, \qquad \big(\gamma^{(x_4)}\gamma^{(a)}\big)^2 = -\big(\gamma^{(x_4)}\big)^2\big(\gamma^{(a)}\big)^2 = 1 .
$$

Rule: $(\gamma^{(x_4)})^2 = \eta_{44} = -1$ and $(\gamma^{(a)})^2 = +1$ for a space-like direction; in the second, moving the second $\gamma^{(x_4)}$ to the left past $\gamma^{(a)}$ costs one sign.

$$
\big(-i\gamma^{(x_4)}\big)\big(\gamma^{(x_4)}\gamma^{(a)}\big) + \big(\gamma^{(x_4)}\gamma^{(a)}\big)\big(-i\gamma^{(x_4)}\big) = -i\big(\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(a)} - \gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(a)}\big) = 0 ,
$$

Rule: anticommutation of different gammas ($\gamma^{(x_4)}$ is moved to the left past $\gamma^{(a)}$ in the second product, which costs one sign). For two different space-like directions $a \ne b$, line by line:

$$
\big(\gamma^{(x_4)}\gamma^{(a)}\big)\big(\gamma^{(x_4)}\gamma^{(b)}\big) = -\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(a)}\gamma^{(b)} = \gamma^{(a)}\gamma^{(b)}, \qquad \big(\gamma^{(x_4)}\gamma^{(b)}\big)\big(\gamma^{(x_4)}\gamma^{(a)}\big) = \gamma^{(b)}\gamma^{(a)} .
$$

Rule: move the second $\gamma^{(x_4)}$ to the left past $\gamma^{(a)}$, which costs one sign, and use $\gamma^{(x_4)}\gamma^{(x_4)} = -1$; the second product is the same with $a$ and $b$ exchanged.

$$
\big(\gamma^{(x_4)}\gamma^{(a)}\big)\big(\gamma^{(x_4)}\gamma^{(b)}\big) + \big(\gamma^{(x_4)}\gamma^{(b)}\big)\big(\gamma^{(x_4)}\gamma^{(a)}\big) = \gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 0 .
$$

Rule: add the two products; different gammas anticommute, $\gamma^{(a)}\gamma^{(b)} = -\gamma^{(b)}\gamma^{(a)}$. Hence

$$
h_{\mathbf p}^2 = \big(M^2 + p_1^2 + p_2^2 + p_3^2 + p_8^2\big)\,1 = E^2\,1, \qquad E = \sqrt{M^2 + p^2} .
$$

Rule: multiply out the square of the sum; the squares of the five terms give $M^2$ and the $p_a^2$, and the mixed products cancel in pairs. Since $h_{\mathbf p}$ is Hermitian (Section 14.4), its eigenvalues are real numbers whose squares are $E^2$: they are $+E$ and $-E$. Its trace is zero (it is a sum of products of one or two different gammas, Chapter 5), so the two eigenvalues occur equally often: $+E$ eight times and $-E$ eight times. Every momentum carries eight positive-energy modes. The matrix

$$
G_{\mathbf p} = \tfrac12\big(1 + h_{\mathbf p}/E\big)
$$

is the **projector** on them: $G_{\mathbf p}^2 = \tfrac14(1 + 2h_{\mathbf p}/E + h_{\mathbf p}^2/E^2) = \tfrac14(2 + 2h_{\mathbf p}/E) = G_{\mathbf p}$, and $\mathrm{Tr}\,G_{\mathbf p} = \tfrac12(16 + 0) = 8$. Status: PROVED; check gas_mode_projector (both reports).

**Why every symmetric occupation has $\rho = (nB + SC)/16$.** The sum of $uu^\dagger$ over the eight positive-energy modes (orthonormal, because $h_{\mathbf p}$ is Hermitian) is the projector $G_{\mathbf p}$. We assume that the eight modes of one momentum carry the same occupation $f$, as they do in every closed shell (all eight filled) and in every thermal state (the occupation depends only on the energy, which is the same for the eight). Then these eight modes contribute $fG_{\mathbf p}B$ to $\rho$; we write the case $f = 1$, and a common factor $f$ changes nothing below. Line by line:

$$
G_{\mathbf p}B = \tfrac12B + \frac{M}{2E}\big(-i\gamma^{(x_4)}\big)B - \frac{1}{2E}\sum_a p_a\gamma^{(x_4)}\gamma^{(a)}B .
$$

Rule: insert $h_{\mathbf p}$ into $G_{\mathbf p}$ and multiply by $B$.

$$
\big(-i\gamma^{(x_4)}\big)B = \big(-i\gamma^{(x_4)}\big)\big(-iC\gamma^{(x_4)}\big) = -\gamma^{(x_4)}C\gamma^{(x_4)} = -C\gamma^{(x_4)}\gamma^{(x_4)} = C .
$$

Rule: $B = -iC\gamma^{(x_4)}$; $(-i)^2 = -1$; $\gamma^{(x_4)}$ commutes with $C$ (it passes the four factors of $C$, none of which is $\gamma^{(x_4)}$: four signs); $(\gamma^{(x_4)})^2 = -1$.

$$
G_{\mathbf p}B = \tfrac12\Big(B + \frac ME\,C\Big) - \frac{1}{2E}\sum_a p_a\gamma^{(x_4)}\gamma^{(a)}B .
$$

The last term changes its sign when $\mathbf p$ is replaced by $-\mathbf p$. If the state occupies $\mathbf p$ and $-\mathbf p$ equally, which is true for every closed shell and for every thermal state, these terms cancel in pairs, and each pair leaves $B + (M/E)C$ (times the common occupation). Filled negative-energy modes give in the same way $\tfrac12(1 - h_{\mathbf p}/E)B$, whose symmetric part is $\tfrac12(B - (M/E)C)$. So the one-body matrix of any such state is a combination of $B$ and $C$ only, $\rho = \alpha B + \beta C$. The two numbers follow from the densities:

$$
n = \mathrm{Tr}(B\rho) = \alpha\,\mathrm{Tr}(B^2) + \beta\,\mathrm{Tr}(BC) = 16\alpha, \qquad S = \mathrm{Tr}(C\rho) = \alpha\,\mathrm{Tr}(CB) + \beta\,\mathrm{Tr}(C^2) = 16\beta .
$$

Rule: $B^2 = C^2 = 1$, whose trace is 16, and $\mathrm{Tr}(BC) = \mathrm{Tr}(-i\gamma^{(x_4)}) = 0$ (Chapter 5: $BC = -i\gamma^{(x_4)}$). Hence

$$
\rho = \frac{nB + SC}{16} ,
$$

for every occupation that gives the eight modes of each momentum the same occupation and is symmetric under $\mathbf p \to -\mathbf p$, at every temperature (the record: "any p -> -p symmetric occupation of the 8-fold good-sector gas", `Revision/kohn_sham/ks-theory.json`, exchange.uniformGas). If only some of the eight modes of a momentum were filled, their one-body matrix would in general not be a combination of $B$ and $C$, and the formula would not apply. Status: PROVED; checks gas_angular_average (both reports), gas_negative_energy_modes (sympy report) and gas_densities (both).

**Wick's rule for the contact term.** Write $S = \Psi^\dagger C\Psi = \sum_{A,B}\Psi_A^\dagger C_{AB}\Psi_B$, with the components $A, B = 0, \dots, 15$. For a quasi-free state (a determinant or a thermal state of independent quanta), Wick's theorem (Section 13.4) gives the expectation of a normal-ordered product of two creation and two annihilation operators as the sum over the ways of pairing each $\Psi^\dagger$ with a $\Psi$, with a minus sign for the crossed pairing because the field anticommutes. With $f_{AB} = \langle\Psi_A^\dagger\Psi_B\rangle$:

$$
\langle{:}S^2{:}\rangle = \sum_{A,B,C',D}C_{AB}C_{C'D}\big(f_{AB}f_{C'D} - f_{AD}f_{C'B}\big) .
$$

(The index $C'$ carries a prime so that it is not confused with the matrix $C$.) The first product is the **direct** (Hartree) term, the second the **exchange** (Fock) term. Now the matrix form, line by line:

$$
f_{AB} = \rho_{BA} .
$$

Rule: $\langle\Psi^\dagger X\Psi\rangle = \sum_{A,B}X_{AB}f_{AB}$ and $\mathrm{Tr}(X\rho) = \sum_{A,B}X_{AB}\rho_{BA}$ must agree for every matrix $X$.

$$
\sum C_{AB}C_{C'D}f_{AB}f_{C'D} = \Big(\sum_{A,B}C_{AB}\rho_{BA}\Big)\Big(\sum_{C',D}C_{C'D}\rho_{DC'}\Big) = \big(\mathrm{Tr}\,C\rho\big)^2 .
$$

Rule: the sum of a product of two factors with separate indices is the product of the two sums.

$$
\sum C_{AB}C_{C'D}f_{AD}f_{C'B} = \sum C_{AB}\rho_{BC'}C_{C'D}\rho_{DA} = \mathrm{Tr}(C\rho C\rho) .
$$

Rule: $f_{AD} = \rho_{DA}$ and $f_{C'B} = \rho_{BC'}$; reorder the four numbers so that neighbouring indices agree, $A \to B \to C' \to D \to A$: a chain of matrix products that closes on itself is a trace. Hence

$$
\langle{:}S^2{:}\rangle = \big(\mathrm{Tr}\,C\rho\big)^2 - \mathrm{Tr}(C\rho C\rho) .
$$

Status: PROVED (Section 13.4 and the lines above); the record verified it term by term on an explicit two-mode state (check hf_wick_contraction of the sympy report), and Notebook 14d repeats that on two states (In [6]).

**The exact local exchange.** Insert $\rho = (nB + SC)/16$. Line by line:

$$
C\rho = \frac{nCB + S\,1}{16} .
$$

Rule: $C^2 = 1$.

$$
C\rho C\rho = \frac{n^2\,CBCB + nS\,CB + nS\,CB + S^2\,1}{256} = \frac{n^2 + 2nS\,CB + S^2}{256} .
$$

Rule: multiply out the four products; $CBCB = (CBC)B = BB = 1$ by $CBC = B$ (Chapter 5) and $B^2 = 1$.

$$
\mathrm{Tr}(C\rho C\rho) = \frac{16n^2 + 0 + 16S^2}{256} = \frac{n^2 + S^2}{16} .
$$

Rule: $\mathrm{Tr}\,1 = 16$ and $\mathrm{Tr}(CB) = 0$. The interaction energy per unit (proper) volume, $\tfrac\lambda2\langle{:}S^2{:}\rangle$, is therefore $e_H + e_x$ with

$$
e_H = \frac\lambda2S^2, \qquad e_x = -\frac\lambda2\mathrm{Tr}(C\rho C\rho) = -\frac{\lambda}{32}\big(n^2 + S^2\big) .
$$

The **Hartree** term $e_H$ and the **exchange** term $e_x$ are both functions of the two densities at one point: the exchange of the contact interaction is exactly **local**, at every temperature, for every symmetric occupation. For one filled 8-fold level at rest the scalar and number densities are equal, $n = S$ (Exercise 14.8), and $e_x/e_H = -\tfrac{1}{32}\cdot2S^2\big/\tfrac12S^2 = -\tfrac18$: the exchange removes one eighth of the Hartree energy, the rule $E_x = -E_H/g$ of Section 13.5 with the $g = 8$ modes per momentum. Status: PROVED; checks exchange_uniform_gas (both reports) and filled_shell_ratio (sympy report); the coefficients $-1/32$, $-1/32$ are recorded under exchange.uniformGas in ks-theory.json.

### 14.27 The Kohn-Sham potentials, the exact Fock exchange of the model's states, and the eight zero modes

**The potentials.** The interaction energy density is

$$
e_{\rm int}(n, S) = e_H + e_x = \frac{15}{32}\lambda S^2 - \frac{1}{32}\lambda n^2 .
$$

Rule: $\tfrac12 - \tfrac1{32} = \tfrac{15}{32}$. As in Chapter 13 (Section 13.9), the Kohn-Sham potential that belongs to a density is the derivative of the interaction energy density with respect to that density (for a local energy the functional derivative is an ordinary derivative). The density $S$ multiplies the mass term of the Lagrangian, so its potential shifts the mass; the number density gives a potential that is added to $h$ as $v_v$ times the unit matrix:

$$
M_{\rm eff} = m + \frac{\partial e_{\rm int}}{\partial S} = m + \frac{15}{16}\lambda S, \qquad v_v = \frac{\partial e_{\rm int}}{\partial n} = -\frac{1}{16}\lambda n .
$$

Rule: the derivative of $S^2$ is $2S$, and $2\cdot\tfrac{15}{32} = \tfrac{15}{16}$, $2\cdot\tfrac1{32} = \tfrac1{16}$. In the covariant equation $v_v$ appears as $-iv_v\gamma^{(x_4)}$ (Section 14.3). These are the $M_{\rm eff}$ and $v_v$ that Sections 14.3 to 14.25 used as given functions. Status: PROVED; check ks_potentials (both reports); the coefficients $15/16$ and $-1/16$ are recorded in ks-theory.json (exchange.kohnShamPotentials) and are the numbers $0.9375$ and $-0.0625$ that the Rust solver reads (`Revision/kohn_sham/results/parameters.json`, theoryInputs).

**The Lagrangian on shell.** $e_{\rm int}$ is **homogeneous of degree 2**: doubling both densities multiplies it by 4. Line by line:

$$
S\frac{\partial e_{\rm int}}{\partial S} + n\frac{\partial e_{\rm int}}{\partial n} = \frac{15}{16}\lambda S^2 - \frac{1}{16}\lambda n^2 = 2e_{\rm int} .
$$

Rule: insert the two derivatives and compare with twice $e_{\rm int}$.

$$
\frac{\langle L\rangle}{\sqrt{|g|}} = M_{\rm eff}S + v_vn - mS - e_{\rm int} = mS + 2e_{\rm int} - mS - e_{\rm int} = e_{\rm int} .
$$

Rule: the Lagrangian of Chapter 7 is a kinetic part minus $mS$ minus the interaction, whose expectation value is $e_{\rm int}$. On shell (for orbitals that solve the Kohn-Sham equation $\gamma^\mu D_\mu\Psi = (M_{\rm eff} - iv_v\gamma^{(x_4)})\Psi$) the kinetic part is $\bar\Psi\gamma^\mu D_\mu\Psi = M_{\rm eff}\bar\Psi\Psi + v_v\Psi^\dagger(-iC\gamma^{(x_4)})\Psi = M_{\rm eff}S + v_vn$, because $\bar\Psi = \Psi^\dagger C$ and $B = -iC\gamma^{(x_4)}$ (the symmetrised form of the kinetic term has the same value on shell); then the line above gives $M_{\rm eff}S + v_vn = mS + 2e_{\rm int}$. This value of the Lagrangian enters the energy-momentum tensor (Chapter 15). Status: PROVED; check ks_onshell_lagrangian (both reports).

**What the functional leaves out.** The Kohn-Sham functional of the Revision theory is Hartree plus this uniform-gas exchange, with no correlation energy. Its states, however, are not uniform along $y$. The record computes the EXACT Fock exchange of such a state (exchange.exactFockSlab in ks-theory.json): take one level, closed over a shell ($\mathbf k$ and $-\mathbf k$ equally filled), with the $2 \times 2$ block density $D = \tfrac12(d_0 + d_1\sigma_1 + d_2\sigma_2 + d_3\sigma_3)$ in each of the four blocks of type $j = +1$ and $\sigma_3D\sigma_3$ in each of the four of type $-1$ (their degenerate partners, Section 14.5), and average it over the directions of the shell. Two facts make this average simple. First, averaging a matrix over all the rotations of a group gives a matrix that no rotation of the group changes, that is, one that commutes with all of them; and a matrix that already commutes with them is its own average. So the average over all rotations of 3-space is the projection onto the matrices that commute with the rotations, a space of dimension 64. Second, a closed shell contains only a finite set of directions, which the 24 rotations of a cube carry into each other, not all directions. But under the rotations of 3-space the $16 \times 16$ matrices split into parts of spin 0 (unchanged by every rotation) and parts of spin 1 (turned like an arrow), and nothing else; and the average of an arrow over the 24 rotations of a cube is zero, just as its average over all rotations. So for these matrices the average over the cube equals the average over all rotations (both theory reports state this: the 16 x 16 matrices carry only spin 0 and spin 1). The result, with $Q = \langle\Psi^\dagger B\gamma^{(x_8)}\Psi\rangle$ and the $y$-current $Y$:

$$
n = 8d_0, \qquad S = 8d_2, \qquad Q = 8d_3, \qquad Y = 8d_1, \qquad e_x^{\rm exact} = -\frac{\lambda}{32}\big(n^2 + S^2 - Q^2 - Y^2\big) .
$$

For orbitals $Y = 0$ (Section 14.12), so the uniform-gas exchange $-\tfrac{\lambda}{32}(n^2 + S^2)$ omits the term $+\tfrac{\lambda}{32}Q^2$. The record labels this a DIAGNOSTIC: the canonical functional stays the uniform-gas one, and the Rust solver reports the omitted part and also solves an exact-Fock variant of the model, which adds the potential $w_Q\sigma_3$ with $w_Q = +\tfrac{\lambda}{16}Q$ to $h$ and $+\tfrac{\lambda}{32}Q^2$ to $e_{\rm int}$. Status: PROVED; check exchange_slab_exact_fock (both reports, by two different methods: the sympy report projects onto the 64-dimensional space of matrices that commute with the rotations, the Wolfram report averages over the 48 spinor matrices of the 24 rotations of a cube, each rotation appearing with both signs).

**The size of $Q$.** For one orbital $\chi = (a, ib)$ the three densities are proportional to $a^2 + b^2$ ($n$), $2ab$ ($S$, up to the sign $j$) and $a^2 - b^2$ ($Q$) (Section 14.12). Line by line:

$$
(2ab)^2 + (a^2 - b^2)^2 = 4a^2b^2 + a^4 - 2a^2b^2 + b^4 = (a^2 + b^2)^2 .
$$

Rule: the binomial formulas. So for one orbital $S^2 + Q^2 = n^2$, and for a mixture of orbitals $S^2 + Q^2 \le n^2$ (Exercise 14.9): the possible states fill the disk $(S/n)^2 + (Q/n)^2 \le 1$. The uniform-gas and the exact exchange agree on the line $Q = 0$ and differ most at the top and bottom of the disk, $S = 0$, $Q = \pm n$ (Figure 14d.3).

**The state of the eight zero modes ($N = 8$).** The simplest Kohn-Sham state of the model fills the eight brane zero modes at $k = 0$ (both block types, even parity). Each orbital is $\chi = (a, 0)$ with $a = \sqrt{2M/(1 - e^{-2ML})}\,e^{My}$ (Section 14.13). The densities, line by line (the record's densities section in ks-theory.json):

- One orbital: $n_o = P(a^2 + b^2) = Pa^2$, $s_o = P\,j\,2ab = 0$, $q_o = P(a^2 - b^2) = Pa^2$, with $P = e^{-6Hy}/(\ell^3v_t)$, the factor that makes the densities proper (Section 14.7).
- The state: $n = \sum w\,g\,f\,n_o$, with the degeneracy $g = 4$ per block type, the occupation $f = 1$, and the weight $w = \tfrac12$ of the ASSUMED Z2 doubled system: the orbitals are normalised on the patch, $\int_{-L}^0\chi^\dagger\chi\,dy = 1$, but the system consists of the patch and its mirror copy, so the patch holds half of each orbital, and the particle number $N = \sum g f$ counts the doubled system. So $n = \tfrac12(4 + 4)Pa^2 = 4Pa^2$, $S = 0$ and $Q = n$.
- The proper density $n = 4e^{-6Hy}a^2/(\ell^3v_t) \propto e^{(2M - 6H)y}$ is largest at the cutoff $y = -L$ (for $M = H = 1$: $e^{-4y}$), although the orbital itself sits at the brane: the proper 7-volume $e^{6Hy}$ is tiny near the tip. With $H = m = 1$, $L = 3$, $\ell = 2\pi/0.25$ and $v_t = 1$ its largest value is $n_{\max} = 82.2208638894$ (Notebook 14d, Out [12]; the column n_max of the row N8_lam0_a00 of `Revision/kohn_sham/results/ground/summary.csv`).
- To first order in $\lambda$ the potentials are $M_{\rm eff} - m = \tfrac{15}{16}\lambda S = 0$ and $v_v = -\tfrac{\lambda}{16}n$. The Revision solver calibrates its couplings by the largest first-order potential per unit $\lambda$, $n_{\max}/16 = 5.138803993$; $\lambda_1$ and $\lambda_2$ are $0.1$ and $0.3$ divided by it, rounded to 4 significant digits: $\lambda_1 = 0.01946$, $\lambda_2 = 0.05838$, so that the largest first-order potential is $0.1\,m$ and $0.3\,m$ to four significant digits (after the rounding of $\lambda$ it is $0.1000011\,m$ and $0.3000034\,m$, Notebook 14d, Out [12]; `Revision/kohn_sham/results/parameters.json`, couplingCalibration; the states $N = 136$ and $688$ have their own, smaller couplings, fixed the same way along the whole history). This calibration is an $L = 3$ statement: the largest proper density sits at the cutoff and grows with $L$ like $e^{(6H - 2M)L}$, so the same rule applied at a larger cutoff drives $\lambda_1$ toward zero, for $N = 8$ like $e^{-4L}$, from $0.01946$ at $L = 3$ to $1.2\times10^{-7}$ at $L = 6$ (`Revision/kohn_sham/tip_convergence/`; `Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md`, section 5); with the couplings held fixed, the interaction energy of the zero modes depends strongly on $L$ (Section 14.20).
- The exact Fock exchange of this state vanishes: with $S = 0$ and $Q = n$, $e_x^{\rm exact} = -\tfrac{\lambda}{32}(n^2 - Q^2) = 0$. In the exact-Fock variant the potential on $(a, 0)$ is $v_v + w_Q = \tfrac{\lambda}{16}(Q - n) = 0$ (because $\sigma_3$ acts as $+1$ on $(a, 0)$), so the zero modes stay exact solutions with $\varepsilon = 0$ and the energy of the state is exactly zero. The record's twenty self-consistent exact-Fock states with $N = 8$ (four couplings, five slices) have energies zero to rounding, below $10^{-12}$ (`Revision/kohn_sham/results/exx/exact-fock-variant.csv`).

Status: the formulas PROVED; the numbers COMPUTED (they reproduce the records named); the weight $w = \tfrac12$ rests on the ASSUMED Z2 mirror.

### 14.28 Example: Notebook 14d, the exact local exchange

Notebook 14d does Sections 14.26 and 14.27 with exact algebra on the author's gamma matrices: the plane waves of the good sector and their projector, the cancellation that makes $\rho = (nB + SC)/16$, Wick's rule term by term on two explicit states, the exact local exchange and the ratio $-1/8$, the Kohn-Sham potentials and the on-shell Lagrangian (compared with the coefficients that the Rust solver read), and the exact Fock exchange of the closed-shell states by projection onto the 64-dimensional space of matrices that commute with the rotations. With numpy it computes the densities of the eight zero modes, reproduces the largest proper density, the calibration of the couplings and the zero exact-Fock energies of the record. It draws four figures, needs no Rust, runs in about 30 seconds, and its last line is ALL 16 CHECKS PASSED (notebook 14d).

<!-- NOTEBOOK 14d -->

### 14.31 Line-by-line walk-through of Notebook 14d

The notebook has 14 code cells, In [1] to In [14]. Docstrings and the long caption texts are left out of the quotations; the captions are printed under the figures in Section 14.30.

**In [1], the set-up cell.** The code of In [1] of Notebook 14a (Section 14.11), line for line, except

```python
NOTEBOOK_ID = "14d"  # this notebook: chapter 14, example d
```

which names this notebook. Its comment lines are the run instructions of Section 14.29.

**In [2], the gamma matrices, $B$ and $C$.**

```python
import math  # exp, sqrt, log10 of single numbers

import numpy as np  # floating-point arrays
import sympy as sp  # exact algebra with symbols

PY_REPORT = "Revision/kohn_sham/reports/ks-theory-python.json"
WL_REPORT = "Revision/kohn_sham/reports/ks-theory-wolfram.json"
```

The three modules and the two theory reports.

```python
def record_check(name):
    verdicts = []
    for report_file in (PY_REPORT, WL_REPORT):
        data = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
        found = [c["verdict"] for c in data["checks"] if c["name"] == name]
        verdicts.append(found[0] if found else "absent")
    return verdicts[0] == "PASS" and verdicts[1] in ("PASS", "absent")
```

The `record_check` of Notebook 14a: true when the sympy report says PASS and the Wolfram report says PASS or has no check of that name. (The loop variable is called `report_file`, so that it does not hide the helper `report` of the set-up cell.)

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                     .read_text(encoding="utf-8"))
g = [sp.Matrix(m) for m in fixture["gamma"]]
g1, g2, g3, g4, g5, g6, g7, g8 = g
I16, Z16 = sp.eye(16), sp.zeros(16)
C = g8 * g1 * g2 * g3
B = -sp.I * C * g4
```

The author's gammas from the Revision record, exactly as in In [2] and In [3] of Notebook 14a, and the matrices $C$ and $B$.

```python
facts_ok = (B * B == I16 and C * C == I16 and (B * B).trace() == 16
            and (C * C).trace() == 16 and (B * C).trace() == 0 and C * B * C == B
            and (-sp.I * g4) * B == C)
check(facts_ok, "B^2 = C^2 = 1, Tr B^2 = Tr C^2 = 16, Tr BC = 0, CBC = B, (-i g4) B = C")
```

Every matrix fact used in Section 14.26, checked exactly: $B^2 = C^2 = 1$, their traces 16, $\mathrm{Tr}(BC) = 0$, $CBC = B$ and $(-i\gamma^{(x_4)})B = C$. Out [2] is one PASS line.

**In [3], the plane waves and their projector.**

```python
M = sp.symbols("M", positive=True)  # the mass
p1, p2, p3, p8 = sp.symbols("p1 p2 p3 p8", real=True)  # the momentum
E = sp.symbols("E", positive=True)  # stands for sqrt(M^2 + p^2)
h_p = M * (-sp.I * g4) - (p1 * g4 * g1 + p2 * g4 * g2 + p3 * g4 * g3 + p8 * g4 * g8)
E_squared = M ** 2 + p1 ** 2 + p2 ** 2 + p3 ** 2 + p8 ** 2
square_ok = (h_p * h_p - E_squared * I16).applyfunc(sp.expand).is_zero_matrix
```

The mass, the four momentum components, a positive symbol $E$, the matrix $h_{\mathbf p}$ of Section 14.26, and the test $h_{\mathbf p}^2 = (M^2 + p^2)\,1$ entry by entry (`applyfunc(sp.expand)` multiplies out every entry).

```python
G_p = (I16 + h_p / E) / 2  # the projector on the positive energy
projector_ok = ((G_p * G_p - G_p).subs(E, sp.sqrt(E_squared))
                .applyfunc(sp.simplify).is_zero_matrix
                and G_p.H == G_p and sp.simplify(G_p.trace()) == 8)
check(square_ok and projector_ok and record_check("gas_mode_projector"),
      "h_p^2 = (M^2 + p^2) 1 and G_p = (1 + h_p/E)/2 is a projector of rank 8",
      record=f"{PY_REPORT}, check gas_mode_projector")
```

$G_{\mathbf p}$; the test $G_{\mathbf p}^2 = G_{\mathbf p}$ after replacing $E$ by $\sqrt{M^2 + p^2}$; $G_{\mathbf p}$ Hermitian; its trace 8 (for a projector the trace is the rank, Section 14.5). One PASS line.

**In [4], the symmetric one-body matrix.**

```python
p_flip = {p1: -p1, p2: -p2, p3: -p3, p8: -p8}
pair_average = ((G_p * B + (G_p * B).subs(p_flip)) / 2).applyfunc(sp.simplify)
pair_ok = (pair_average - (B + M / E * C) / 2).applyfunc(sp.simplify).is_zero_matrix
```

A dictionary that replaces $\mathbf p$ by $-\mathbf p$; the average of $G_{\mathbf p}B$ and $G_{-\mathbf p}B$; and the test that it is $\tfrac12(B + (M/E)C)$ (Section 14.26).

```python
th, ph = sp.symbols("vartheta varphi", real=True)  # angles on the sphere
components = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
sphere = [sp.integrate(sp.integrate(c * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi))
          / (4 * sp.pi) for c in components]  # the averages of the components
say(f"sphere averages of the three direction components: {sphere}")
check(pair_ok and sphere == [0, 0, 0] and record_check("gas_angular_average"),
      "the average over p and -p (or over all directions) is (B + (M/E) C)/2",
      record=f"{PY_REPORT}, check gas_angular_average")
```

The same for an average over all directions of $\mathbf p$: a direction on the sphere has the three components $\sin\vartheta\cos\varphi$, $\sin\vartheta\sin\varphi$ and $\cos\vartheta$, with the two angles $\vartheta$ and $\varphi$; the average of a function over the sphere is its integral with the area element $\sin\vartheta\,d\varphi\,d\vartheta$ divided by the area $4\pi$. All three components average to 0 (printed in Out [4]), so the part of $G_{\mathbf p}B$ linear in $\mathbf p$ averages away too.

```python
h_0 = M * (-sp.I * g4)  # the p-independent part of h_p
negative_ok = (((I16 - h_0 / E) / 2) * B - (B - M / E * C) / 2).is_zero_matrix
check(negative_ok and record_check("gas_negative_energy_modes"),
      "negative-energy modes give (B - (M/E) C)/2: only B and C ever appear",
      record=f"{PY_REPORT}, check gas_negative_energy_modes")
```

The negative-energy modes: the part of $\tfrac12(1 - h_{\mathbf p}/E)B$ that survives the average (the part of $h_{\mathbf p}$ without $\mathbf p$, `h_0`) is $\tfrac12(B - (M/E)C)$.

```python
n, S, lam = sp.symbols("n S lambda", real=True)
rho = (n * B + S * C) / 16  # the one-body matrix of a symmetric occupation
check(sp.expand((B * rho).trace()) == n and sp.expand((C * rho).trace()) == S
      and record_check("gas_densities"),
      "rho = (nB + SC)/16 has Tr(B rho) = n and Tr(C rho) = S",
      record=f"{PY_REPORT}, check gas_densities")
```

Symbols for the two densities and the coupling, the matrix $\rho = (nB + SC)/16$, and the check that it gives back $n$ and $S$. Out [4] shows three PASS lines.

**In [5], figure 1.**

```python
values = {M: 1, E: sp.sqrt(2), p1: 1, p2: 0, p3: 0, p8: 0}
one_mode = np.abs(np.array((G_p * B).subs(values).evalf(), dtype=complex))
averaged = np.abs(np.array(pair_average.subs(values).evalf(), dtype=complex))
odd_part = np.abs(np.array((G_p * B - pair_average).subs(values).evalf(),
                           dtype=complex))
```

The example $M = 1$, $\mathbf p = (1, 0, 0, 0)$, $E = \sqrt2$, and the absolute values of the entries of three matrices: $G_{\mathbf p}B$, its average with $-\mathbf p$, and their difference, the part linear in $\mathbf p$.

```python
fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.9))
fig.subplots_adjust(wspace=0.45)
titles = ["$|G_{\\mathbf{p}}B|$: one momentum",
          "$|(G_{\\mathbf{p}} + G_{-\\mathbf{p}})B/2|$",
          "$|$part linear in $\\mathbf{p}|$"]
for ax, data, title in zip(axes, (one_mode, averaged, odd_part), titles):
    image = ax.imshow(data, cmap="Blues", vmin=0.0, vmax=0.6,
                      interpolation="nearest")
    ax.set_title(title, fontsize=9)
    ax.set_xticks([0, 5, 10, 15])
    ax.set_yticks([0, 5, 10, 15])
    ax.set_xlabel("column")
    ax.set_ylabel("row")
    ax.grid(False)
    fig.colorbar(image, ax=ax, shrink=0.75)
save_figure(fig, "pair_average",
            "Absolute values of the entries (rows and columns 0 to 15, darker is "
            ...)
```

Three heat maps as in In [15] of Notebook 14a, with one common colour scale from 0 to 0.6 (`vmax=0.6`), so that the three panels can be compared. **What figure 14d.1 shows.** Left: the matrix of one momentum has entries in many places. Middle: after the average with $-\mathbf p$ only the entries of $\tfrac12B$ (size $\tfrac12$, dark) and of $\tfrac{M}{2E}C = \tfrac{1}{2\sqrt2}C$ (size about $0.35$, lighter) remain. Right: the part linear in $\mathbf p$, $-\tfrac{1}{2E}p_1\gamma^{(x_4)}\gamma^{(x_1)}B$, with entries of size $\tfrac{1}{2\sqrt2} \approx 0.35$ in other places; it is exactly what the average with $-\mathbf p$ removes.

**In [6], Wick's rule term by term.**

```python
half, i_half = sp.Rational(1, 2), sp.I / 2
u1 = sp.Matrix([half, i_half, 0, 0, 0, 0, 0, 0, half, 0, 0, 0, 0, 0, -i_half, 0])
u2 = sp.Matrix([0, 0, half, 0, -half, 0, 0, 0, 0, 0, i_half, 0, 0, 0, 0, i_half])
v1 = sp.Matrix([1, 2, 0, -1, sp.I, 0, 3, 1, 0, 1, -2, sp.I, 0, 1, 1, 0]) / 4
v2 = sp.Matrix([0, 1, sp.I, 2, 1, -1, 0, 0, 1, 0, sp.I, 1, 2, 0, -1, 1]) / 4
nonzero = [(A_, B_) for A_ in range(16) for B_ in range(16) if C[A_, B_] != 0]
wick_ok = True
```

Two pairs of mode vectors: $u_1, u_2$, the two-mode state of the Revision check, and $v_1, v_2$, a second state with less symmetry. `nonzero` lists the 16 positions $(A, B)$ where $C$ has a nonzero entry; only these contribute to the sum.

```python
for name, modes in (("u1, u2 (record)", (u1, u2)), ("v1, v2", (v1, v2))):
    rho_2 = (modes[0] * modes[0].H + modes[1] * modes[1].H) * B  # one-body matrix
    f = rho_2.T  # f_AB = rho_BA
    brute = sp.simplify(sum(
        C[A_, B_] * C[C_, D_] * (f[A_, B_] * f[C_, D_] - f[A_, D_] * f[C_, B_])
        for A_, B_ in nonzero for C_, D_ in nonzero))
    direct = sp.simplify((C * rho_2).trace() ** 2)
    exchange = sp.simplify((C * rho_2 * C * rho_2).trace())
    say(f"state {name}: (Tr C rho)^2 = {direct}, Tr(C rho C rho) = {exchange}, "
        f"term-by-term sum = {brute}")
    wick_ok &= sp.simplify(brute - (direct - exchange)) == 0
```

For each state: the one-body matrix $\rho = (u_1u_1^\dagger + u_2u_2^\dagger)B$, the expectations $f_{AB} = \rho_{BA}$ (the transpose), the sum of Wick's rule over the $16 \times 16 = 256$ pairs of nonzero entries of $C$ (`brute`), and the two traces. Out [6] prints, for the record's state, $(\mathrm{Tr}\,C\rho)^2 = 1/4$, $\mathrm{Tr}(C\rho C\rho) = 1/4$ and the sum 0, and for the second state $25/64$, $9/32$ and $7/64$: in both cases the sum equals the difference of the traces ($25/64 - 18/64 = 7/64$).

```python
check(len(nonzero) == 16 and wick_ok and record_check("hf_wick_contraction"),
      "<:S^2:> = (Tr C rho)^2 - Tr(C rho C rho), checked term by term",
      record=f"{PY_REPORT}, check hf_wick_contraction")
```

One PASS line.

**In [7], the exchange and the ratio $-1/8$.**

```python
e_x = sp.factor(-lam / 2 * (C * rho * C * rho).trace())  # the exchange energy density
say(f"e_x = -(lambda/2) Tr(C rho C rho) = {e_x}")
check(sp.simplify(e_x + lam / 32 * (n ** 2 + S ** 2)) == 0
      and record_check("exchange_uniform_gas"),
      "the exact local exchange e_x = -(lambda/32)(n^2 + S^2)",
      record=f"{PY_REPORT}, check exchange_uniform_gas")
```

$e_x = -\tfrac\lambda2\mathrm{Tr}(C\rho C\rho)$ with $\rho = (nB + SC)/16$, written by `sp.factor` as a product (Out [7]: `-lambda*(S**2 + n**2)/32`), and the check.

```python
e_H = lam / 2 * S ** 2  # the Hartree energy density
ratio = sp.simplify((e_x / e_H).subs({n: 8, S: 8}))
say(f"one filled level at rest (n = S = 8): e_x/e_H = {ratio}")
check(ratio == sp.Rational(-1, 8) and record_check("filled_shell_ratio"),
      "a filled 8-fold level at rest has e_x/e_H = -1/8",
      record=f"{PY_REPORT}, check filled_shell_ratio")
```

The Hartree term and the ratio for one filled level at rest, $n = S = 8$ (Exercise 14.8): $-1/8$. Out [7] shows two PASS lines.

**In [8], the Kohn-Sham potentials.**

```python
m = sp.symbols("m", real=True)
e_int = sp.expand(e_H + e_x)
M_eff = m + sp.diff(e_int, S)  # the effective mass
v_v = sp.diff(e_int, n)  # the vector potential
say(f"e_int = {e_int}")
say(f"M_eff = {M_eff},  v_v = {v_v}")
```

The bare mass $m$, $e_{\rm int} = e_H + e_x$, and the two potentials as derivatives (Section 14.27). Out [8] prints $e_{\rm int} = \tfrac{15}{32}\lambda S^2 - \tfrac{1}{32}\lambda n^2$ and the potentials in sympy's notation.

```python
check(sp.simplify(M_eff - m - sp.Rational(15, 16) * lam * S) == 0
      and sp.simplify(v_v + lam * n / 16) == 0 and record_check("ks_potentials"),
      "M_eff = m + (15/16) lambda S and v_v = -lambda n/16",
      record=f"{PY_REPORT}, check ks_potentials")
on_shell = sp.simplify(M_eff * S + v_v * n - m * S - e_int - e_int)
check(on_shell == 0 and record_check("ks_onshell_lagrangian"),
      "on shell <L>/sqrt|g| = M_eff S + v_v n - m S - e_int = e_int",
      record=f"{PY_REPORT}, check ks_onshell_lagrangian")
```

The two potentials, and the on-shell Lagrangian: $M_{\rm eff}S + v_vn - mS - e_{\rm int}$ minus $e_{\rm int}$ must be zero.

```python
theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                    .read_text(encoding="utf-8"))
potentials = theory["exchange"]["kohnShamPotentials"]
gas = theory["exchange"]["uniformGas"]
inputs = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                    .read_text(encoding="utf-8"))["theoryInputs"]
```

The parts of the theory record that hold the coefficients, and the coefficients that the Rust solver read (its parameters record).

```python
same = (sp.Rational(potentials["Meff_coefficient_of_lambda_S"]) == sp.Rational(15, 16)
        and sp.Rational(potentials["vv_coefficient_of_lambda_n"]) == sp.Rational(-1, 16)
        and sp.Rational(gas["coefficient_n2"]) == sp.Rational(-1, 32)
        and sp.Rational(gas["coefficient_S2"]) == sp.Rational(-1, 32)
        and inputs["MeffCoefficientOfLambdaS"] == 0.9375
        and inputs["vvCoefficientOfLambdaN"] == -0.0625
        and inputs["exchangeCoefficientN2"] == -0.03125
        and inputs["exchangeCoefficientS2"] == -0.03125)
check(same and record_check("ks_theory_json_exchange"),
      "the coefficients 15/16, -1/16, -1/32, -1/32 equal the records",
      record="Revision/kohn_sham/ks-theory.json, exchange; "
             "Revision/kohn_sham/results/parameters.json, theoryInputs")
```

The theory record stores the coefficients as texts such as "15/16", which `sp.Rational` turns into exact fractions; the solver's record stores them as decimal numbers, $0.9375 = 15/16$, $-0.0625 = -1/16$ and $-0.03125 = -1/32$ (all four are exact in binary floating point). The PASS line names both records with the parts that hold the coefficients: the section exchange of the theory record and the section theoryInputs of the solver's parameters record (two strings written next to each other are joined into one). Out [8] shows three PASS lines.

**In [9], figure 2.**

```python
s_over_n = np.linspace(-1.0, 1.0, 401)
hartree = 0.5 * s_over_n ** 2
exchange_curve = -(1.0 + s_over_n ** 2) / 32.0
fig, ax = plt.subplots(figsize=(7.5, 4.4))
ax.plot(s_over_n, hartree, label="Hartree $e_H/(\\lambda n^2) = (S/n)^2/2$")
ax.plot(s_over_n, exchange_curve, "--",
        label="exchange $e_x/(\\lambda n^2) = -(1 + (S/n)^2)/32$")
ax.plot(s_over_n, hartree + exchange_curve, ":", color="black",
        label="$e_{\\rm int} = e_H + e_x$")
```

The ratio $S/n$ from $-1$ to $1$ and the three energy densities divided by $\lambda n^2$: Hartree $\tfrac12(S/n)^2$, exchange $-\tfrac1{32}(1 + (S/n)^2)$ and their sum.

```python
ax.plot([1.0], [-1.0 / 16.0], "o", color="C3")
ax.annotate("$S = n$: $e_x = -e_H/8$", xy=(1.0, -1.0 / 16.0), xytext=(-0.05, 0.3),
            fontsize=8, color="C3", arrowprops={"arrowstyle": "->", "color": "C3"})
ax.axhline(0.0, color="gray", linewidth=0.6)
ax.set_xlabel("ratio of the scalar to the number density $S/n$")
ax.set_ylabel("energy density per $\\lambda n^2$")
ax.set_title("the Hartree-Fock energy of the contact interaction")
ax.legend(fontsize=8, loc="upper center")
save_figure(fig, "energy_densities",
            "The interaction energy densities of the contact term per unit "
            ...)
```

A red dot at $S/n = 1$ on the exchange curve, $-\tfrac1{16}$, with an arrow from its label (`annotate` with `xy` the point, `xytext` the place of the text and `arrowprops` the style of the arrow), the zero line, labels and saving. **What figure 14d.2 shows.** The Hartree parabola is zero at $S = 0$ and $\tfrac12$ at $S = \pm n$. The exchange curve is small and negative everywhere, between $-\tfrac1{32}$ and $-\tfrac1{16}$. Their sum is slightly negative near $S = 0$, where only the exchange is left, and positive for larger $|S|$. At $S = n$ the exchange $-\tfrac1{16}$ is one eighth of the Hartree term $\tfrac12$.

**In [10], the exact Fock exchange of the closed-shell states.**

```python
as_number = {"0": 0, "1": 1, "-1": -1, "I": sp.I, "-I": -sp.I}
U = sp.Matrix([[as_number[e] for e in row] for row in
               theory["blockBasis"]["unnormalisedColumns2Sqrt2V"]])
V = U / (2 * sp.sqrt(2))  # the block basis of the record
labels = [(j, s2, s3) for j in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]
s1 = sp.Matrix([[0, 1], [1, 0]])
s2m = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
```

The block basis $V$ of the record (as in In [13] of Notebook 14a), the eight block labels in the record's order, and the Pauli matrices (`s2m` is $\sigma_2$).

```python
d0, d1, d2, d3 = sp.symbols("d0 d1 d2 d3", real=True)
D = (d0 * sp.eye(2) + d1 * s1 + d2 * s2m + d3 * s3) / 2  # the block density
G_slab = Z16
for b, (j, _, _) in enumerate(labels):
    Vb = V[:, 2 * b:2 * b + 2]
    G_slab = G_slab + Vb * (D if j == 1 else s3 * D * s3) * Vb.H
```

A general $2 \times 2$ Hermitian block density $D$ with four real numbers $d_0, \dots, d_3$ (every Hermitian $2 \times 2$ matrix is a combination of $1$ and the three Pauli matrices), and the $16 \times 16$ matrix of one level that has $D$ in the four blocks of type $+1$ and $\sigma_3D\sigma_3$ in the four of type $-1$: each block's $2 \times 2$ matrix is carried back to 16 components with its two basis columns, $V_bDV_b^\dagger$.

```python
unknowns = sp.Matrix(16, 16, sp.symbols("x0:256"))  # a general 16 x 16 matrix
equations = []
for rotation in (g1 * g2, g1 * g3, g2 * g3):  # commute with the 3-space rotations
    equations += list(rotation * unknowns - unknowns * rotation)
solution = sp.Matrix(16, 16, list(list(sp.linsolve(equations, list(unknowns)))[0]))
```

The matrices that commute with the three generators $\gamma^{(x_1)}\gamma^{(x_2)}$, $\gamma^{(x_1)}\gamma^{(x_3)}$, $\gamma^{(x_2)}\gamma^{(x_3)}$ of the rotations of 3-space: a general matrix of 256 unknowns, the $3 \times 256$ linear equations "commutator = 0", and their general solution by `sp.linsolve`, which returns the set of solutions; `list(...)[0]` takes its single element, a list of 256 expressions in the unknowns that remain free.

```python
free = sorted(solution.free_symbols, key=lambda s_: int(str(s_)[1:]))
basis = [solution.subs({x: (1 if x == y else 0) for x in free}) for y in free]
gram = sp.Matrix(len(basis), len(basis),
                 lambda i, k: (basis[i].H * basis[k]).trace())
coefficients = gram.LUsolve(sp.Matrix([(b_.H * G_slab).trace() for b_ in basis]))
G_avg = sp.simplify(sum((c_ * b_ for c_, b_ in zip(coefficients, basis)), Z16))
```

The free unknowns, sorted by their numbers (`str(s_)[1:]` is the name without its first letter); a basis of the solution space, one matrix for each free unknown set to 1 and the others to 0 (64 of them); the **Gram matrix** of the inner products $\mathrm{Tr}(X^\dagger Y)$ of the basis matrices; and the orthogonal projection of $G_{\rm slab}$ onto the space, found by solving the linear equations with the Gram matrix (`LUsolve`). The projection is the average over all directions of the shell.

```python
rho_slab = G_avg * B
n_s, S_s = sp.simplify((B * rho_slab).trace()), sp.simplify((C * rho_slab).trace())
Q_s = sp.simplify((B * g8 * rho_slab).trace())
e_x_slab = sp.expand(-lam / 2 * (C * rho_slab * C * rho_slab).trace())
say(f"commutant dimension {len(basis)}; n = {n_s}, S = {S_s}, Q = {Q_s}")
say(f"V unitary: {sp.simplify(V.H * V) == I16}")
```

The averaged one-body matrix, its three densities $n$, $S$ and $Q = \langle\Psi^\dagger B\gamma^{(x_8)}\Psi\rangle$, and its exchange energy. Out [10] prints the dimension 64, $n = 8d_0$, $S = 8d_2$, $Q = 8d_3$, and that $V$ is unitary.

```python
check(len(basis) == 64 and n_s == 8 * d0 and S_s == 8 * d2 and Q_s == 8 * d3
      and sp.simplify(e_x_slab + lam / 32 * (n_s ** 2 + S_s ** 2 - Q_s ** 2
                                             - (8 * d1) ** 2)) == 0
      and record_check("exchange_slab_exact_fock"),
      "exact Fock exchange of the slab: -(lambda/32)(n^2 + S^2 - Q^2 - Y^2)",
      record=f"{PY_REPORT}, check exchange_slab_exact_fock")
```

The check of Section 14.27 with $Y = 8d_1$. This cell does the heaviest algebra of the notebook. One PASS line.

**In [11], figure 3.**

```python
grid = np.linspace(-1.0, 1.0, 401)
S_grid, Q_grid = np.meshgrid(grid, grid)  # S/n horizontally, Q/n vertically
inside = S_grid ** 2 + Q_grid ** 2 <= 1.0
ratio_grid = np.where(inside, (1.0 + S_grid ** 2 - Q_grid ** 2) / (1.0 + S_grid ** 2),
                      np.nan)
```

A square grid of $401 \times 401$ points in the plane of $S/n$ and $Q/n$ (`np.meshgrid` makes the two coordinate arrays of the grid), the points inside the unit disk, and there the ratio of the exact to the uniform-gas exchange, $(n^2 + S^2 - Q^2)/(n^2 + S^2)$ with $Y = 0$; outside the disk the value `np.nan` ("not a number"), which is not drawn.

```python
fig, ax = plt.subplots(figsize=(6.4, 5.2))
filled = ax.contourf(S_grid, Q_grid, ratio_grid, levels=np.linspace(0.0, 1.0, 11),
                     cmap="Blues")
ax.contour(S_grid, Q_grid, ratio_grid, levels=[0.5], colors="gray", linewidths=0.8)
fig.colorbar(filled, ax=ax, label="$e_x^{\\rm exact} / e_x^{\\rm gas}$")
```

`contourf` fills the regions between the levels $0, 0.1, \dots, 1$ of the ratio with colours, `contour` draws the line where the ratio is $\tfrac12$, and the colour bar explains the colours.

```python
ax.plot([0.0, 0.0], [1.0, -1.0], "o", color="C3")  # S = 0, Q = +n and -n
ax.annotate("zero modes ($N = 8$): ratio 0", (0.05, 0.9), fontsize=8, color="C3")
ax.annotate("$Q = 0$: ratio 1", (-0.95, 0.04), fontsize=8,
            color="white")  # white text on the dark band
ax.set_xlabel("$S/n$")
ax.set_ylabel("$Q/n$")
ax.set_aspect("equal")
ax.grid(False)
ax.set_title("exact Fock exchange / uniform-gas exchange")
save_figure(fig, "exact_fock_ratio",
            "The ratio of the exact Fock exchange of a closed-shell slab state, "
            ...)
```

Two red dots at $S = 0$, $Q = \pm n$, two labels, equal scales on both axes (`set_aspect("equal")`, so that the disk is round), and saving. **What figure 14d.3 shows.** A dark band (ratio near 1) across the middle of the disk, around the line $Q = 0$, where the uniform-gas formula is exact; toward the top and the bottom the colour fades and the ratio falls to 0 at the two red dots; the gray line marks the ratio $\tfrac12$. The state of the eight zero modes sits at the top dot: for it the uniform-gas formula gives a nonzero exchange, while the exact exchange is zero.

**In [12], the state of the eight zero modes.**

```python
H_val, m_val, L_val = 1.0, 1.0, 3.0
ell = 2.0 * math.pi / 0.25  # the coordinate size of the 3-torus
vol7 = ell ** 3 * 1.0  # the coordinate 7-volume ell^3 v_t
y = np.linspace(-L_val, 0.0, 1801)  # the hidden coordinate
a_sq = 2.0 * m_val / (1.0 - math.exp(-2.0 * m_val * L_val)) * np.exp(2.0 * m_val * y)
P = np.exp(-6.0 * H_val * y) / vol7  # proper-density factor
n_y = 4.0 * P * a_sq  # line 2
n_max = float(np.max(n_y))
```

The canonical numbers $H = m = 1$, $L = 3$, $\ell = 2\pi/0.25$, $v_t = 1$; 1801 points of $y$; $a^2$ of the normalised zero mode; the factor $P$; the proper density $n = 4Pa^2$ of Section 14.27; and its largest value.

```python
summary = repository_file("Revision/kohn_sham/results/ground/summary.csv") \
    .read_text(encoding="utf-8").splitlines()
header = summary[0].split(",")
free8 = dict(zip(header, [r for r in summary if r.startswith("N8_lam0_a00,")][0]
                 .split(",")))
report("largest proper density of the free N = 8 state", f"{n_max:.10f}",
       "per unit proper 7-volume")
check(abs(n_max / float(free8["n_max"]) - 1.0) < 1e-9 and float(y[np.argmax(n_y)])
      == -3.0,
      "n_max = 4 P a^2 at the tip y = -3 equals the record",
      record="Revision/kohn_sham/results/ground/summary.csv, N8_lam0_a00, n_max")
```

The summary record of the Rust ground states, its row for $N = 8$, $\lambda = 0$, slice 0 (`startswith` finds the row whose text starts with its name), the RESULT line $82.2208638894$, and the check: the notebook's value equals the record's to $10^{-9}$ (relative), and the maximum lies at $y = -3$ (`np.argmax` gives the position of the largest entry).

```python
def round_significant(x, digits):
    exponent = math.floor(math.log10(abs(x))) - (digits - 1)
    scale = 10.0 ** (-exponent)
    return math.copysign(math.floor(abs(x) * scale + 0.5), x) / scale
```

Rounding to a number of significant digits, halves away from zero: for $x = 0.019460\ldots$ and 4 digits, $\log_{10}|x| = -1.71$, rounded down to $-2$, so the exponent is $-5$; the number is multiplied by $10^5$ to $1946.0\ldots$, rounded to the whole number 1946 (adding $\tfrac12$ and rounding down), and divided back: $0.01946$.

```python
strength = n_max / 16.0  # line 4: the largest first-order potential per lambda
lambda_1 = round_significant(0.1 / strength, 4)
lambda_2 = round_significant(0.3 / strength, 4)
parameters = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                        .read_text(encoding="utf-8"))
calibration = [c for c in parameters["couplingCalibration"]["values"]
               if c["N"] == 8.0][0]
```

The strength $n_{\max}/16$ (with $S = 0$ only the term $|n|/16$ counts), the two couplings by the record's rule, and the record's calibration entry for $N = 8$.

```python
report("strength per lambda", f"{strength:.9f}")
report("lambda_1, lambda_2", f"{lambda_1}, {lambda_2}")
report("first-order potentials", f"{lambda_1 * strength:.10f}, "
       f"{lambda_2 * strength:.10f}", "m")
check(abs(strength / calibration["strengthPerLambda"] - 1.0) < 1e-9
      and lambda_1 == calibration["lambda1"] and lambda_2 == calibration["lambda2"]
      and abs(lambda_1 * strength - calibration["firstOrderPotential1"]) < 1e-9
      and len(set(calibration["strengthPerLambdaAtSlices"])) == 1,
      "strength 5.1388, lambda_1 = 0.01946, lambda_2 = 0.05838 (the same at all "
      "slices)", record="Revision/kohn_sham/results/parameters.json, "
      "couplingCalibration N = 8")
```

Three RESULT lines ($5.138803993$; $0.01946$, $0.05838$; the first-order potentials $0.1000011257$ and $0.3000033771\,m$, just above $0.1$ and $0.3$ because of the rounding of $\lambda$) and the check against the record; the last condition says that the record found the same strength at all five slices (a set keeps each value once, so its size is 1). That is the rescaling identity again: the zero modes do not depend on the slice.

```python
exx = repository_file("Revision/kohn_sham/results/exx/exact-fock-variant.csv") \
    .read_text(encoding="utf-8").splitlines()
exx_header = exx[0].split(",")
rows8 = [dict(zip(exx_header, r.split(","))) for r in exx[1:] if r.startswith("N8_")]
largest = max(abs(float(r["E_exact_fock_scf"])) for r in rows8)
check(len(rows8) == 20 and largest < 1e-12,
      "the self-consistent exact-Fock energy of all 20 N = 8 states is 0",
      record="Revision/kohn_sham/results/exx/exact-fock-variant.csv, "
             "E_exact_fock_scf")
```

The record of the exact-Fock variant, its 20 rows with $N = 8$, and the check that their self-consistent energies are all below $10^{-12}$ in size: zero up to rounding, as Section 14.27 predicts. Out [12] shows three PASS lines.

**In [13], figure 4.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 4.0))
fig.subplots_adjust(wspace=0.32)  # room for the label of the right panel
left.semilogy(y, n_y, label="proper density $n(y) = 4Pa^2$")
left.semilogy(y, np.exp(6.0 * y) * n_y, "--",
              label="coordinate density $e^{6Hy} n(y)$")
left.set_xlabel("$y$ (units of $1/H$; tip at $-3$, brane at $0$)")
left.set_ylabel("density (logarithmic)")
left.set_title("the eight zero modes ($N = 8$, $\\lambda = 0$)")
left.legend(fontsize=8)
```

Left panel, logarithmic: the proper density and the coordinate density $e^{6Hy}n$ (the number of particles per unit $y$ and per unit coordinate volume of the other directions).

```python
right.plot(y, -lambda_1 * n_y / 16.0, label=f"$v_v$, $\\lambda_1 = {lambda_1}$")
right.plot(y, -lambda_2 * n_y / 16.0, label=f"$v_v$, $\\lambda_2 = {lambda_2}$")
right.plot(y, np.zeros_like(y), ":", color="black",
           label="exact Fock: $v_v + w_Q = 0$")
right.set_xlabel("$y$ (units of $1/H$)")
right.set_ylabel("first-order potential (units of $m$)")
right.set_title("the Kohn-Sham potential of the zero modes")
right.legend(fontsize=8, loc="lower right")
save_figure(fig, "zero_mode_state",
            "The state of the eight brane zero modes ($N = 8$, $m = H = 1$, "
            ...)
```

Right panel: the first-order potential $v_v = -\lambda n/16$ for the two couplings and the zero exact-Fock potential. **What figure 14d.4 shows.** Left: two straight lines on the logarithmic axis. The coordinate density (dashed) rises like $e^{2y}$ toward the brane, from about $10^{-6}$ to $5\times10^{-4}$: the particles sit at the brane. The proper density (solid) falls like $e^{-4y}$ from $82$ at the tip to $5\times10^{-4}$ at the brane, where the two meet ($e^{6Hy} = 1$ there): per unit proper volume the gas is densest at the tip, because the proper 7-volume is tiny there. Right: the potential is zero over most of the interval and dips to $-0.1$ and $-0.3\,m$ only near the tip; the exact-Fock potential is zero everywhere.

**In [14], the last check.**

```python
figure_names = ["14d_1_pair_average.png", "14d_2_energy_densities.png",
                "14d_3_exact_fock_ratio.png", "14d_4_zero_mode_state.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all four figure files of this notebook exist")
all_checks_passed()
```

The four figure files must exist; the last line prints ALL 16 CHECKS PASSED (notebook 14d). The 16 checks are: 1 in In [2], 1 in In [3], 3 in In [4], 1 in In [6], 2 in In [7], 3 in In [8], 1 in In [10], 3 in In [12] and 1 in In [14].

### 14.32 What we proved, what we computed, what we assumed

**PROVED** (exact; the derivation is in this chapter, and the Revision record checks it in `Revision/kohn_sham/reports/ks-theory-python.json`, with the checks marked "both" also in `Revision/kohn_sham/reports/ks-theory-wolfram.json`):

| statement (section; notebook) | record checks |
| --- | --- |
| the hidden coordinate, the warped form, the volume factor $e^{6Hy}$ without $a_4$ (Section 14.2; Notebook 14a) | `geometry_hidden_coordinate` and `geometry_sqrt_det` (both), `geometry_warped_form` |
| $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ along every history; the pieces of the inflating and the deflating directions cancel (Section 14.4; Notebook 14a) | `spin_connection_compatibility`, `spin_connection_slash_3H`, `spin_connection_time_terms_cancel` (both), `spin_connection_time_term_value` |
| the factor $W^{-3}$ removes the spin connection; the Hamiltonian is Hermitian (Section 14.4; Notebook 14a) | `ansatz_removes_spin_connection`, `ansatz_without_W3_term_survives`, `hamiltonian_16_hermitian` (both) |
| eight blocks of two components, two block types, the block forms and the block Hamiltonian (Section 14.5; Notebook 14a) | `blocks_commuting_set`, `blocks_basis_unitary`, `blocks_forms`, `block_hamiltonian`, `block_ode_equivalent`, `block_type_relation` (both), `blocks_projectors`, `blocks_not_everything_block_diagonal` |
| the chirality matrix $\Gamma$ pairs the block types and reverses the mass (Section 14.6; Notebook 14a) | `blocks_relation_to_Gamma`, `block_Gamma_map` (both) |
| the levels depend only on the length of the 3-momentum (Section 14.6; Notebook 14a) | `rotation_invariance` (both) |
| the exact rescaling identity between the slices (Section 14.7; Notebooks 14a and 14c) | `rescaling_identity` (both) |
| the real form, the boundary term, the mirror map and the parities, the tip family, the constant current, the suppression at the tip (Section 14.12; Notebook 14b) | `bc_mirror_map_PA`, `bc_mirror_parities_of_densities`, `bc_brane_parity_conditions`, `bc_self_adjoint_boundary_term`, `bc_tip_family`, `bc_current_conserved_along_y`, `bc_tip_asymptotics` (all both) |
| the exact free levels at zero 3-momentum, the zero mode and the gap (Section 14.13; Notebook 14b) | `bc_exact_k0_spectra` (both) |
| the equation of the Pruefer angle; the shooting function grows with the energy; one level per label (Section 14.14; Notebook 14b) | derived in Section 14.14 (not a separate check of the record); Notebook 14b checks the equation of the angle with sympy and the labels numerically |
| the slope of the brane band; the band is odd in $k$ (Section 14.19; Notebook 14c) | `brane_band_slope` (both) |
| $h_{\mathbf p}^2 = E^2$; $\rho = (nB + SC)/16$; Wick's rule; the exact local exchange; the ratio $-1/8$ (Section 14.26; Notebook 14d) | `gas_mode_projector`, `gas_angular_average`, `gas_densities`, `exchange_uniform_gas` (both), `gas_negative_energy_modes`, `hf_wick_contraction`, `filled_shell_ratio` |
| the Kohn-Sham potentials; the Lagrangian on shell (Section 14.27; Notebook 14d) | `ks_potentials`, `ks_onshell_lagrangian` (both) |
| the exact Fock exchange of the closed-shell states and the term $+\tfrac{\lambda}{32}Q^2$ that the functional omits (Section 14.27; Notebook 14d) | `exchange_slab_exact_fock` (both) |

**COMPUTED** (numerical, with the record that holds the numbers and their measured accuracy):

| result (notebook) | record and measured accuracy |
| --- | --- |
| the 54 free levels at $k = 0$ by RK4 shooting (Notebook 14b) | `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv`; check `free_k0_analytic_spectra` of `Revision/kohn_sham/reports/ks-rust-solver.json`; measured largest errors against the exact levels $7.23\times10^{-10}$ below $4m$ and $5.05\times10^{-8}$ above (tolerances of the record $5\times10^{-9}$ and $3\times10^{-7}$); the notebook reproduces both numbers and agrees with the Rust levels to $7.1\times10^{-15}$ |
| fourth-order convergence (Notebook 14b) | check `refined_free_spectra_convergence_order` of `Revision/kohn_sham/reports/ks-rust-determinism.json`; measured: median error ratio 16.00 over 39 levels, largest errors $5.050\times10^{-8}$ (canonical step) and $3.157\times10^{-9}$ (refined step), reproduced by the notebook |
| the brane band and three other levels for $k$ from 0 to 4 (Notebook 14c) | `Revision/kohn_sham/results/spectrum/brane-band.csv`; accuracy: reproduced to $10^{-11}$ |
| the numerical slope $c\,e^{-a_{4,0}}$ at five slices (Notebook 14c) | `brane-band-slope.csv` (spectrum folder); check `free_brane_band_slope`; accuracy: $1.87\times10^{-12}$ relative |
| the rescaling identity solved as two separate problems (Notebook 14a, the partner parameters) | `Revision/kohn_sham/results/rescaling/rescaling.csv`; checks `rescaling_identity_between_slices` and `rescaling_identity_energy_profiles`; accuracy: levels to $1.5\times10^{-13}$, energies and profiles to $3.3\times10^{-13}$ |
| the gap of the free $N = 8$ state, $0.4307$ to $0.0642\,m$ along the history (Notebook 14c) | `closed-shells.csv` (spectrum folder); accuracy: reproduced to $10^{-11}$ |
| at the cutoff $L = 3$ and the slice 0 the band does not feel the tip angle for $k \ne 0$ (Notebook 14c; the later slices are not computed) | `tip-angle.csv` (spectrum folder); check `free_tip_angle_insensitivity`; accuracy: shifts below the suppression factor |
| the dependence on the cutoff $L$ from 3 to 6 (Section 14.20; the Revision record, not repeated by a notebook of this chapter) | `Revision/kohn_sham/tip_convergence/` (README and `tip-convergence-table.csv`); report `tip-convergence.json`, 7 of 7 checks PASS; the step error of every run at most $5\times10^{-9}$; the free results with $k \ne 0$ at $L = 3$ low by up to 1.4% ($E_{\rm KS}$) and 12% (the $p_8$ integral) at $a_{4,0} = 2$; the interacting $N = 8$ energy at $L = 3$ about one third of its large-$L$ value |
| the particle labels, the closed shells, the bulk edge and $N = 8, 136, 688$ (Notebook 14c) | check `free_particle_branch_labels`; `closed-shells.csv`; `Revision/kohn_sham/results/parameters.json`; accuracy: exact agreement of the shells; energies to $10^{-11}$ |
| the state $N = 8$: $n_{\max} = 82.2208638894$, $\lambda_1 = 0.01946$, $\lambda_2 = 0.05838$, exact-Fock energy 0 (Notebook 14d) | `Revision/kohn_sham/results/ground/summary.csv`; `parameters.json`; `Revision/kohn_sham/results/exx/exact-fock-variant.csv`; accuracy: $10^{-9}$ relative; energies below $10^{-12}$ |

**ASSUMED** (starting points that this chapter does not derive):

- The good sector: the orbitals do not depend on the extra times $x_5, x_6, x_7$ (Section 14.3; Chapters 8 and 10 give the reasons).
- The Z2 mirror brane at $y = 0$, with its two parities; with it the weight $w = \tfrac12$ of the densities and the mirror copy with the mass $-m$ (Section 14.12).
- The regular tip condition at the cutoff $y = -L$, $L = 3$: a choice of the numerical model. At this cutoff and the slice $a_{4,0} = 0$, where it was measured, its angle $\theta$ is harmless for every lattice level with $k \ne 0$ (at the later slices, where the suppression factor of Section 14.12 is no longer small, this is not computed), and it is decisive for the zero modes at $k = 0$ (Section 14.20). The cutoff $L$ itself matters, as the Revision record measured for $L = 3$ to $6$ (Section 14.20; `Revision/kohn_sham/tip_convergence/`): the free results with $k \ne 0$ converge, but the recorded $L = 3$ values are low by up to 1.4% in $E_{\rm KS}$ and 12% in the $p_8$ integral at $a_{4,0} = 2$ (the redshifted brane band reaches the tip); the nonzero $k = 0$ levels approach $\pm m$ only algebraically, so the bulk edge and $N = 688$ are $L = 3$ choices; the interaction energy of the brane zero modes depends strongly on $L$, and the couplings are calibrated at $L = 3$.
- The deflating history $a_4 = AHx_4$ with $A = 1$ is a **prescribed background**: the Kohn-Sham states are computed on it but are not its source in the field equations of $a_4$ (`Revision/field_equations_a4/reports/ks-source-conditions.json`; Chapter 17). The Kohn-Sham gas is a test field.
- The stationary-slice (adiabatic) ansatz: at each slice the instantaneous Kohn-Sham states are computed (Section 14.3); whether the gas can follow the history is measured in Chapter 15.
- The convention that counts the zero modes at $k = 0$ as particle levels (Section 14.21).
- The functional: Hartree plus the uniform-gas exchange, without correlation (an approximation; the exact Fock exchange differs by $+\tfrac{\lambda}{32}Q^2$ and is reported as a diagnostic, Section 14.27).
- The canonical numbers $H = m = 1$, $L = 3$, $\Delta k = 0.25$, $v_t = 1$ and the five slices.

**HYPOTHESIS:** none in this chapter.

**OPEN:** the justification of the zero-mode convention; the effect of the tip angle $\theta$ on the levels with $k \ne 0$ at the later slices, which neither the record nor a notebook computes (Section 14.20); the time-dependent (non-adiabatic) evolution of the gas along the history; the action of the gas back on $a_4$ (the history is not a solution of the coupled equations); the correlation energy of the contact interaction in this geometry; the limit $L \to \infty$ of the cutoff where the Revision record does not establish it (the state $N = 688$ at $a_{4,0} = 0$, and 7 of the 19 interacting states studied, whose self-consistent iteration fails before their energies meet the record's convergence rule; Section 14.20).

**Honesty about pairs and charges (rule of Chapter 0).** Two places of this chapter touch the pairing of universes. The chirality matrix $\Gamma$ maps every solution with the mass $M$ onto a solution with the mass $-M$ (Section 14.6), and the ASSUMED mirror brane pairs the patch, with $+m$, with a mirror copy carrying $-m$ (Section 14.12). Both are exact maps between sets of solutions; Chapters 18 and 19 prove the theorems T1 and T3 built on them. Neither says that a universe, or a pair of universes, is created: no creation process, rate or amplitude follows from these equations (Chapter 20 gives the complete list of what is and is not proved). The words particle and sea in Section 14.21 describe the filling of the levels of the normal-ordered quantum field; this chapter makes no statement about matter and antimatter, which Chapter 21 treats, and it does not claim that the theory explains why our universe contains more matter than antimatter.

### 14.33 Exercises

**Exercise 14.1.** (a) Show that in the coordinate $y$ the volume factor is $\sqrt{|g|} = e^{6Hy}$, and compute it at $y = -3$ for $H = 1$. (b) Compute the momentum weight $\kappa$ at the cutoff $y = -3$ and at the brane $y = 0$, for the slices $a_{4,0} = 0$ and $2$ ($H = 1$). (c) A density per unit $y$ and per unit coordinate volume is turned into a proper density by dividing it by $\sqrt{|g|}$. Explain with (a) why the proper density of the zero modes is largest at the cutoff, although the orbitals sit at the brane.

**Answer 14.1.** (a) The scale factors are $e^{a_4}W$ (three times), $1$, $e^{-a_4}W$ (three times) and $1$, with $W = e^{Hy}$ (Section 14.2). The square root of the absolute value of the determinant of a diagonal metric is the product of the scale factors: $(e^{a_4}W)^3(e^{-a_4}W)^3 = e^{3a_4 - 3a_4}W^6 = e^{6Hy}$. At $y = -3$: $e^{-18} \approx 1.52\times10^{-8}$. (b) $\kappa = e^{-Hy - a_{4,0}}$. At $y = -3$: $e^{3 - a_{4,0}}$, which is $e^3 \approx 20.09$ at the slice 0 and $e^{1} \approx 2.718$ at the slice 2. At $y = 0$: $e^{-a_{4,0}}$, which is $1$ and $e^{-2} \approx 0.135$. (c) The zero-mode orbital gives the coordinate density $\propto a^2 \propto e^{2My}$, largest at the brane. Dividing by $e^{6Hy}$ gives $e^{(2M - 6H)y}$, which for $M = H = 1$ is $e^{-4y}$: it grows toward the tip. The proper 7-volume near the tip is so small (the factor $e^{-18}$ at the cutoff) that the few particles there are packed densely (Figure 14d.4).

**Exercise 14.2.** Using the two rules of Section 14.5, show that $A_0A_1A_4 = -J$, and deduce from it the block form $A_4 \to j\sigma_1$. Then derive the block form of $\gamma^{(x_4)} = A_0A_4$.

**Answer 14.2.** $A_0A_1A_4 = \gamma^{(x_8)}\gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_8)}\gamma^{(x_4)}$. The first two factors give $(\gamma^{(x_8)})^2 = \eta_{88} = 1$, so the product is $\gamma^{(x_1)}\gamma^{(x_8)}\gamma^{(x_4)}$. Exchanging the first two factors (they anticommute) gives $-\gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_4)} = -J$. In a block of type $j$, $J$ is the number $j$, so $A_0A_1A_4 = -j$ there. With $A_0 \to \sigma_3$ and $A_1 \to -i\sigma_2$: $\sigma_3(-i\sigma_2) = -i\sigma_3\sigma_2 = -i(-i\sigma_1) = -\sigma_1$, so $-\sigma_1A_4 = -j$, and multiplying by $-\sigma_1$ from the left ($\sigma_1^2 = 1$): $A_4 = j\sigma_1$. Finally $\gamma^{(x_4)} = \gamma^{(x_8)}\gamma^{(x_8)}\gamma^{(x_4)} = A_0A_4 \to \sigma_3(j\sigma_1) = j\sigma_3\sigma_1 = ij\sigma_2$, as in Section 14.5.

**Exercise 14.3.** (a) Show that the column $\chi = (\cos\tfrac\theta2,\ i\sin\tfrac\theta2)$, that is $(a, b) = (\cos\tfrac\theta2, \sin\tfrac\theta2)$ in real form, satisfies $Q(\theta)\chi = \chi$ for $Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2$. (b) Show that the tip condition with $\theta = \pi$ is $a(-L) = 0$, and that the matrix $\sigma_2$ of Section 14.6 turns the canonical tip condition $b(-L) = 0$ into it.

**Answer 14.3.** (a) For $\chi = (a, ib)$ the products of Section 14.12 give $\sigma_3\chi = (a, -ib)$ and $\sigma_2\chi = (b, ia)$, so $Q\chi = \big(a\cos\theta + b\sin\theta,\ i(a\sin\theta - b\cos\theta)\big)$. With $a = \cos\tfrac\theta2$, $b = \sin\tfrac\theta2$ the first entry is $\cos\theta\cos\tfrac\theta2 + \sin\theta\sin\tfrac\theta2 = \cos(\theta - \tfrac\theta2) = \cos\tfrac\theta2 = a$, and the bracket of the second is $\sin\theta\cos\tfrac\theta2 - \cos\theta\sin\tfrac\theta2 = \sin(\theta - \tfrac\theta2) = \sin\tfrac\theta2 = b$ (the subtraction formulas of cosine and sine). So $Q\chi = \chi$. (b) For $\theta = \pi$, $Q = -\sigma_3$ and $(1 - Q)\chi = (1 + \sigma_3)\chi = (2\chi_1, 0) = 0$ means $\chi_1(-L) = 0$, that is $a(-L) = 0$. The map $\chi \to \sigma_2\chi$ sends $(a, ib)$ to $(b, ia)$, so the new components are $\tilde a = b$ and $\tilde b = a$: the condition $b(-L) = 0$ of the old orbital becomes $\tilde a(-L) = 0$, the condition with $\theta = \pi$. (The Rust solver's numerical self-test of the Kohn-Sham-level map, check t3_block_map_solver_selftest of `Revision/kohn_sham/reports/ks-rust-solver.json`, solves the problem with $(m, \lambda)$ and the tip $\theta = 0$ and the problem with $(-m, \lambda)$ and exactly this transformed tip, $\theta = \pi$, and finds the same levels; the record states that this self-test is not a proof of T3, which Chapter 19 proves.)

**Exercise 14.4.** Let $p$ be the cubic polynomial with the values $f_0$, $f_1$ and the derivatives $d_0$, $d_1$ at the two ends of an interval of length $h$. Show that its value at the midpoint is $\tfrac12(f_0 + f_1) + \tfrac h8(d_0 - d_1)$, the formula used by `orbital` in Notebooks 14b and 14c.

**Answer 14.4.** Measure the position from the midpoint, $s$, so that the ends are $s = \mp h/2$, and write $p(s) = A + Bs + Cs^2 + Ds^3$; the value at the midpoint is $A$. Then $p(\mp h/2) = A \mp Bh/2 + Ch^2/4 \mp Dh^3/8$ and $p'(\mp h/2) = B \mp Ch + 3Dh^2/4$. Adding the two values: $f_0 + f_1 = 2A + Ch^2/2$ (the odd terms cancel). Subtracting the two derivatives: $d_0 - d_1 = -2Ch$, so $C = (d_1 - d_0)/(2h)$. Hence $A = \tfrac12(f_0 + f_1) - Ch^2/4 = \tfrac12(f_0 + f_1) - \tfrac{h}{8}(d_1 - d_0) = \tfrac12(f_0 + f_1) + \tfrac h8(d_0 - d_1)$.

**Exercise 14.5.** For $M = 1$ and $L = 2$ (the second case of Notebook 14b): (a) compute the lowest positive even level; (b) show that the lowest odd root $p_0$ lies between $\pi/4$ and $\pi/2$ and that no root lies between 0 and $\pi/4$; (c) the record gives the lowest odd level $1.519802561206\,m$; compute $p_0$ from it and check (b).

**Answer 14.5.** (a) $\varepsilon = \sqrt{M^2 + (\pi/L)^2} = \sqrt{1 + (\pi/2)^2} = \sqrt{1 + 2.4674} = \sqrt{3.4674} = 1.862096\,m$; the record `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv` lists $1.862095889118587$ (column eps_analytic, $m = 1$, $L = 2$, even, label 1). (b) With $f(p) = \sin(2p) + p\cos(2p)$: $f(\pi/4) = \sin(\pi/2) + \tfrac\pi4\cos(\pi/2) = 1 > 0$ and $f(\pi/2) = \sin\pi + \tfrac\pi2\cos\pi = -\pi/2 < 0$, so a root lies between them (Step 4 of Section 14.13); for $0 < p < \pi/4$ both $\sin(2p)$ and $\cos(2p)$ are positive, so $f(p) > 0$ and there is no root. (c) $p_0 = \sqrt{\varepsilon^2 - M^2} = \sqrt{1.519803^2 - 1} = \sqrt{2.309801 - 1} = \sqrt{1.309801} = 1.14447$, and indeed $\pi/4 = 0.785 < 1.144 < 1.571 = \pi/2$.

**Exercise 14.6.** (a) Show that for $M = H = 1$ the slope of the brane band is $c = 2e^{-a_{4,0}}/(1 + e^{-L})$. (b) Evaluate it at the slice 0 for $L = 2$ and $L = 4$ and compare with Notebook 14c, Out [5]. (c) Evaluate it for $L = 3$ at the slice 1. (d) What is the limit for $L \to \infty$, and why is it not 1, the value of $\kappa$ at the brane at the slice 0?

**Answer 14.6.** (a) Section 14.19 with $M = H = 1$: $c = e^{-a_{4,0}}\cdot\tfrac{2}{1}\cdot(1 - e^{-L})/(1 - e^{-2L})$, and $1 - e^{-2L} = (1 - e^{-L})(1 + e^{-L})$, so the factor $1 - e^{-L}$ cancels. (b) $L = 2$: $2/(1 + e^{-2}) = 2/1.135335 = 1.761594$; $L = 4$: $2/(1 + e^{-4}) = 2/1.018316 = 1.964028$; both equal the printed numerical and exact values. (c) $2e^{-1}/(1 + e^{-3}) = 1.905148 \times 0.367879 = 0.700865$, the value of Out [5] for the slice 1 ($0.700864874900$). (d) For $L \to \infty$, $e^{-L} \to 0$ and $c \to 2$. The slope is the average of $\kappa = e^{-y}$ over the zero mode, whose weight $2e^{2y}$ extends toward the tip; the average of $e^{-y}$ with the weight $2e^{2y}$ over $(-\infty, 0]$ is $\int 2e^{y}dy = 2$, larger than the value 1 at the brane.

**Exercise 14.7.** Estimate the gap of the free $N = 8$ state at the slices 0 and 1 from the first-order band, $\varepsilon \approx c\,e^{-a_{4,0}}k$ with $k = 0.25$, and compare with the computed gaps of Section 14.20. Why is the estimate too large, and why is it better at the later slice?

**Answer 14.7.** Slice 0: $1.905148 \times 0.25 = 0.4763\,m$ against the computed $0.4307\,m$, too large by $0.0456\,m$ (about 11 per cent). Slice 1: $0.700865 \times 0.25 = 0.1752\,m$ against $0.1703\,m$, too large by $0.0049\,m$ (about 3 per cent). The band bends below its tangent line $ck$ (Figure 14c.1), so the straight line overestimates it. By the rescaling identity the gap at the slice 1 is the band at the slice 0 at the smaller momentum $0.25e^{-1} = 0.092$, where the band is still close to its tangent: along the history the redshift moves the lattice momenta into the region where the first-order formula is accurate.

**Exercise 14.8.** For a single momentum at rest, $\mathbf p = 0$, show that the projector on the eight positive-energy modes is $G_0 = \tfrac12(1 - i\gamma^{(x_4)})$, that these eight modes, filled, give $\rho = \tfrac12(B + C)$, and deduce $n = S = 8$ and $e_x/e_H = -1/8$.

**Answer 14.8.** At $\mathbf p = 0$, $h_0 = M(-i\gamma^{(x_4)})$ and $E = M$, so $G_0 = \tfrac12(1 + h_0/M) = \tfrac12(1 - i\gamma^{(x_4)})$. The filled modes give $\rho = G_0B = \tfrac12(B + (-i\gamma^{(x_4)})B) = \tfrac12(B + C)$, by $(-i\gamma^{(x_4)})B = C$ (Section 14.26). Then $n = \mathrm{Tr}(B\rho) = \tfrac12(\mathrm{Tr}\,B^2 + \mathrm{Tr}\,BC) = \tfrac12(16 + 0) = 8$ and $S = \mathrm{Tr}(C\rho) = \tfrac12(\mathrm{Tr}\,CB + \mathrm{Tr}\,C^2) = 8$. With $n = S = 8$: $e_x = -\tfrac{\lambda}{32}(64 + 64) = -4\lambda$ and $e_H = \tfrac\lambda2\cdot64 = 32\lambda$, so $e_x/e_H = -4/32 = -1/8$, the check filled_shell_ratio and Out [7] of Notebook 14d.

**Exercise 14.9.** Show that for any state built from orbitals with occupations $f \ge 0$ the densities at a point satisfy $S^2 + Q^2 \le n^2$, so that the possible states fill the disk of Figure 14d.3. When does the equality hold?

**Answer 14.9.** For one orbital $\chi = (a, ib)$ at the point $y$ the three contributions are $n_o = P(a^2 + b^2)$, $s_o = Pj\,2ab$ and $q_o = P(a^2 - b^2)$ with $P > 0$ (Section 14.27), and $(2ab)^2 + (a^2 - b^2)^2 = (a^2 + b^2)^2$ (Section 14.27), so the vector $(s_o, q_o)$ in the plane has the length $n_o$ ($j^2 = 1$). The state has $n = \sum c_on_o$, $(S, Q) = \sum c_o(s_o, q_o)$ with the non-negative weights $c_o = wgf$. The length of a sum of vectors is at most the sum of their lengths (the triangle inequality), so $\sqrt{S^2 + Q^2} \le \sum c_on_o = n$. The equality holds when all the vectors $(s_o, q_o)$ with $c_o > 0$ point in the same direction, for example when only one kind of orbital is filled, as for the eight zero modes, where every vector is $(0, n_o)$ and the state sits at $S = 0$, $Q = n$.

**Exercise 14.10.** For the eight zero modes with $M = H = 1$, $L = 3$, $\ell = 8\pi$ and $v_t = 1$: (a) compute the largest proper density $n_{\max} = n(-3)$ from $n = 4Pa^2$; (b) compute the couplings $\lambda_1$ and $\lambda_2$ by the calibration rule of Section 14.27; (c) explain why the exact-Fock energy of this state is zero for every $\lambda$, while the uniform-gas exchange is not.

**Answer 14.10.** (a) $a^2 = \tfrac{2}{1 - e^{-6}}e^{2y}$ and $P = e^{-6y}/(8\pi)^3$, so $n(-3) = 4\cdot\tfrac{2}{1 - e^{-6}}\cdot e^{-6}\cdot e^{18}/(8\pi)^3 = \tfrac{8e^{12}}{(1 - e^{-6})(8\pi)^3}$. With $e^{12} = 162754.79$, $1 - e^{-6} = 0.997521$ and $(8\pi)^3 = 15875.21$: $n_{\max} = 1302038.3/(0.997521 \times 15875.21) = 82.2209$, the RESULT of Notebook 14d ($82.2208638894$) and the record. (b) The strength is $n_{\max}/16 = 5.13880$ ($S = 0$, so only $|n|/16$ counts); $0.1/5.13880 = 0.019460$ and $0.3/5.13880 = 0.058380$, rounded to four significant digits $\lambda_1 = 0.01946$, $\lambda_2 = 0.05838$. (c) The state has $S = 0$ and $Q = n$ at every point. The exact Fock exchange $-\tfrac{\lambda}{32}(n^2 + S^2 - Q^2)$ is therefore zero, and the exact-Fock potential acting on the orbitals $(a, 0)$ is $v_v + w_Q = \tfrac{\lambda}{16}(Q - n) = 0$: the orbitals are unchanged and their levels stay 0. The Kohn-Sham energy of the record is the sum of the filled levels minus the interaction energy integrated over the doubled patch, $E_{\rm KS} = \sum gf\varepsilon - 2\ell^3v_t\int_{-L}^0e^{6Hy}e_{\rm int}\,dy$ (the second term removes the interaction that the levels count twice, as in Chapter 13; `Revision/kohn_sham/ks-theory.json`, thermodynamics.energy). Here both terms vanish: the levels are 0, and $e_{\rm int}^{\rm exact} = \tfrac{15}{32}\lambda S^2 - \tfrac{1}{32}\lambda(n^2 - Q^2) = 0$. So the energy is 0. The uniform-gas exchange $-\tfrac{\lambda}{32}(n^2 + S^2) = -\tfrac{\lambda}{32}n^2$ is not zero: it misses the $+\tfrac{\lambda}{32}Q^2 = +\tfrac{\lambda}{32}n^2$ that cancels it.
