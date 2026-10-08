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
- The brane band that grows out of the zero modes when the 3-momentum is switched on, its exact slope, its redshift along the history, its insensitivity to the tip, and the closed shells of the free filling (Sections 14.19 to 14.21).
- The exact local exchange energy of the contact interaction, the Kohn-Sham potentials, the exact Fock exchange of the model's states and the state of the eight zero modes (Sections 14.26 and 14.27).

**The four notebooks.**

| notebook | what it computes | PASS lines | figures |
| --- | --- | --- | --- |
| 14a | the block reduction and the rescaling identity, with exact algebra | 28 | 5 |
| 14b | the free spectra at zero 3-momentum, exact against numerical | 20 | 6 |
| 14c | the brane band, its slope, redshift, symmetries and closed shells | 15 | 6 |
| 14d | the exact local exchange, the potentials and the zero-mode state | 16 | 4 |

None of them needs Rust: Notebooks 14b and 14c write the shooting method of the Revision Rust solver in a few lines of numpy and reproduce the solver's recorded numbers; Chapter 15 runs the Rust solver itself.

**The status of every statement.** As everywhere in this book, every statement carries one of the five labels of Chapter 0: PROVED, COMPUTED, ASSUMED, HYPOTHESIS, OPEN. In this chapter they are used as follows.

- PROVED: every identity of Sections 14.2 to 14.7, the boundary-condition facts of Section 14.12, the exact spectra of Section 14.13, the counting property of the shooting angle in Section 14.14, the slope formula of Section 14.19 and the exchange formulas of Sections 14.26 and 14.27. Each is verified in the Revision record by sympy in `Revision/kohn_sham/reports/ks-theory-python.json` (in its present state 58 of 58 checks passed), most of them also by WolframScript in `Revision/kohn_sham/reports/ks-theory-wolfram.json` (46 of 46 checks passed), and again by the notebooks of this chapter; the check names are given with each statement.
- COMPUTED: the numerical levels, slopes, shifts and closed shells; each comes with its measured error and the record file it reproduces (the Rust solver's report `Revision/kohn_sham/reports/ks-rust-solver.json`, in its present state 42 of 42 checks passed, and its result files).
- ASSUMED: the good sector (no dependence on the extra times); the Z2 mirror brane at $y = 0$; the regular tip condition at the cutoff $y = -L$ (a choice of the numerical model; Section 14.20 shows that the brane band at nonzero 3-momentum does not feel it); the deflating history $a_4 = AHx_4$ along which the Kohn-Sham states are computed, which is a **prescribed background**, given and not solved for (Section 14.3); the convention that counts the zero modes at zero 3-momentum as particle levels (Section 14.21).
- OPEN: the justification of that convention (Section 14.21), and the behaviour of the gas when the history is not slow (the time-dependent problem, Chapter 15 and Chapter 22).
- HYPOTHESIS: none in this chapter.

**Notation and units.** The author's coordinates are $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which deflate exponentially; $x_8$ is the hidden space direction. The flat frame metric is $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in this order. The gamma matrix of the direction $x_4$ is written $\gamma^{(x_4)}$, and so on; these are the author's eight real $16 \times 16$ matrices of Chapters 4 and 5, read from the record `Revision/algebra/gammas.json`, with the Clifford relation $\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}$. The matrices $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$, $B = -iC\gamma^{(x_4)}$ and the chirality $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)} = \mathrm{diag}(-1_8, 1_8)$ are those of Chapter 5. The three **Pauli matrices**, written row by row, are

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .
$$

Each squares to the $2 \times 2$ unit matrix, two different ones anticommute, and their products are $\sigma_1\sigma_2 = i\sigma_3$, $\sigma_2\sigma_3 = i\sigma_1$, $\sigma_3\sigma_1 = i\sigma_2$ (and with the order reversed the sign changes). In the numbers of this chapter the author's constant $H$ is 1 and the mass $m$ of dirac16complex is 1, as in the Revision runs; energies, momenta and temperatures are then in units of $m$ (which equals $H$), lengths in units of $1/H$.

### 14.2 The author's field and the hidden coordinate y

**The metric.** The author's primordial field is the diagonal metric whose entries, in the order $x_1, \dots, x_8$, are

$$
g = \mathrm{diag}\big(e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\ -1,\ -e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ -e^{-2a_4}\sin^{1/3}z,\ \cot^2 z\big),
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

**The good sector (ASSUMED).** We look only for orbitals that do not depend on the extra times $x_5, x_6, x_7$. Chapters 8 and 10 explain why: modes with enough momentum along the extra times grow without bound, and only without extra-time dependence does the quantised field have a space of states with a positive norm. This restriction is an assumption of the Revision theory, not a result.

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

Rule: three inflating directions, three deflating directions, six warped directions. **The time-direction pieces of the three inflating directions, $+\tfrac32 a_4'\gamma^{(x_4)}$, and of the three deflating extra times, $-\tfrac32 a_4'\gamma^{(x_4)}$, cancel exactly**, for every history; what survives comes from the warp. Status: PROVED; checks spin_connection_compatibility (the curved gammas are covariantly constant, the proof that this is the right connection), spin_connection_slash_3H, spin_connection_time_terms_cancel and spin_connection_time_term_value of `Revision/kohn_sham/reports/ks-theory-python.json` (the first three also in the Wolfram report). Notebook 14a recomputes all of it with sympy and draws the eight contributions (its figure 3). That the surviving term $3H\gamma^{(x_8)}$ belongs to the diagonal vielbein, and can be removed by a change of frame or of the field, is the scope correction of Chapter 8.

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
J^2 = (-1)^3\,\eta_{88}\eta_{11}\eta_{44} = (-1)(1)(1)(-1) = +1, \qquad K_1^2 = (-1)^1\eta_{22}\eta_{33} = -1, \qquad K_2^2 = (-1)^1\eta_{55}\eta_{66} = -1 .
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

where the last step uses $\Gamma\gamma^{(x_4)} = -\gamma^{(x_4)}\Gamma$. Here $M$ and $v$ are regarded as given functions of $y$. In the full theory they are made by the quanta themselves, and how the parameters $m$, $\lambda$ and the boundary conditions transform is the content of the pairing theorems: T1 for the field equations, which Chapter 18 proves (the chirality MATRIX $\Gamma$ carries the solutions of the Lagrangian with $(m, \lambda)$ to those with $(-m, -\lambda)$), and T3 for the Kohn-Sham states, which Chapter 19 proves. On the blocks, $\sigma_2$ also exchanges the tip condition $b(-L) = 0$ with $a(-L) = 0$ (Section 14.12). The author's gammas are real, so for a real field plain complex conjugation changes nothing and is not a charge conjugation; the maps of this theory are matrices, such as $\Gamma$ here and $\sigma_2$, $\sigma_3$ on the blocks (Chapter 5).

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
REPO = find_repository_root()
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first line calls the function and names its result `REPO`. It is never printed, because it differs from computer to computer, while the printed output of a notebook must not. The second line chooses where files are written. `os.environ` holds the **environment variables** of the program (named texts that it receives from the computer); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and the default `str(REPO)` (the repository folder as a string) otherwise. When you run the notebook the variable is not set, so the files go into the repository; the book's checking tool sets it to a scratch folder, so that a check never changes the repository.

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

A string that starts with `f` is an **f-string**: a name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/14a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty JSON dictionary `{}` and a line end into the captions file; `encoding="utf-8"` fixes how letters are stored as bytes, and `newline="\n"` stores the same line end on Windows, macOS and Linux.

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
save_figure(fig, "inflation_deflation", ...)
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
save_figure(fig, "spin_connection_terms", ...)
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
dt_chi = -g4 * ((M * I16 - sp.I * v * g4) * chi_s - g8 * dchi_s - sp.I * kg * chi_s)
h_chi = (sp.I * g4 * g8 * dchi_s - kap * g4 * (k1 * g1 + k2 * g2 + k3 * g3) * chi_s
         + M * (-sp.I * g4) * chi_s + v * chi_s)
check((sp.I * dt_chi - h_chi).expand().is_zero_matrix,
      "i d_x4 chi = h chi with h = i g4 g8 d_y - kappa k_j g4 g_j + M(-i g4) + v")
```

`dt_chi` is $\partial_{x_4}\chi$ from the first two lines of Step 7 (move the terms, multiply by $-\gamma^{(x_4)}$); `h_chi` is $h\chi$ with the four pieces of the third line. The check confirms $i\,\partial_{x_4}\chi = h\chi$ after multiplying out (`expand`).

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

The matrices of Section 14.5; `commute` tests the 24 commutators of $J, K_1, K_2$ with $A_0, A_1, A_4, B, C, J, K_1, K_2$; the check adds the three squares.

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
save_figure(fig, "block_structure", ...)
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
ok_ode = all(sp.simplify(-sp.I * j * s1 * N_matrix(j, M, kk, eps, v, kap)
                         - ((eps - v) * I2 - h_algebraic(j, M, kk, kap)))
             .is_zero_matrix for j in (1, -1))
check(ok_ode and record_check("block_ode_equivalent"),
      "h_j chi = eps chi is the same as d chi/dy = N chi",
      record=f"{PY_REPORT}, check block_ode_equivalent")
```

The equation $h_j\chi = \varepsilon\chi$ reads $-ij\sigma_1\chi' = (\varepsilon - v)\chi - j(M\sigma_2 + \kappa k\sigma_3)\chi$ (the first line of the first-order form in Section 14.5). If $\chi' = N\chi$, this holds for every $\chi$ exactly when $-ij\sigma_1N = (\varepsilon - v) - j(M\sigma_2 + \kappa k\sigma_3)$, which is checked for both types.

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
save_figure(fig, "rescaling", ...)
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
