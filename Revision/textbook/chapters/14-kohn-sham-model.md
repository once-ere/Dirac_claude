## 14. The Kohn-Sham model of dirac16complex in the deflating primordial field

Chapter 13 taught density functional theory from zero: how the hopeless problem of many interacting quanta is replaced by a problem of independent quanta that move in a common, self-made potential, the Kohn-Sham problem. This chapter builds that problem for the quanta of the field dirac16complex in the author's primordial universe, in the corrected metric of 2026-10-16 that Chapter 3 introduced (Sections 3.5 to 3.9): ordinary space inflates, while the three extra times and the hidden direction deflate together, exponentially. Everything is done exactly where it can be done: the change to the hidden coordinate $y$ on the two halves of a cell, the removal of the spin connection, the splitting of the 16 spinor components into eight independent pairs, the boundary conditions at the fold and at the tip, the exact rescaling between the instants of the deflating history, the exact free spectra, the exact free band that grows out of the zero modes, and the exact exchange energy of the contact interaction. Four complete notebooks, 14a to 14d, repeat every step with the computer and reproduce the numbers of the Revision record.

### 14.1 What this chapter does

**Why a Kohn-Sham model.** The field dirac16complex has 16 complex anticommuting components at every point of the eight-dimensional universe of the author, and its quanta interact through the contact term $U(S) = \tfrac{\lambda}{2}S^2$ of the Lagrangian (Chapter 7). A state of many such quanta cannot be computed exactly. The Kohn-Sham method of Chapter 13 replaces it by a state of independent quanta, each described by its own wave function, called an **orbital**, which obeys a one-quantum equation with an effective mass $M_{\rm eff}$ and a potential $v_v$ made by all the other quanta. Solving that equation self-consistently is the work of Chapter 15. This chapter prepares it: it turns the one-quantum equation into a form a computer can solve, finds its exact solutions where they exist, and derives the effective mass and potential.

**What is derived, in order.**

- The hidden coordinate $y$ on the two halves of a cell, the metric in this coordinate with the hidden scale $f = e^{-a_4}b_4^{1/2}$, and the momentum weight $\kappa = e^{-a_4}$ (Section 14.2).
- The Kohn-Sham equation of dirac16complex, the good sector, the stationary-slice ansatz and the prescribed deflating history (Section 14.3).
- The spin-connection term $\tfrac32(H/f)\gamma^{(x_0)} + (b_4'/b_4 - \tfrac12a_4')\gamma^{(x_4)}$, what each direction contributes to it, and the factor $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$ that removes it (Section 14.4).
- The splitting of the 16 components into eight independent $2 \times 2$ blocks of two types (Section 14.5), and the chirality matrix $\Gamma$ and the rotations of 3-space on these blocks (Section 14.6).
- The exact rescaling identity between the instants of the deflating history (Section 14.7).
- The block equation in real form and its boundary conditions at the fold, where the two halves of a cell meet, and at the tip (Section 14.12), the exact free levels at zero 3-momentum (Section 14.13) and the shooting method that finds every level by an integer label (Section 14.14).
- The fold band that grows out of the zero modes when the 3-momentum is switched on, which is exactly $\varepsilon = \kappa k$; its slope; its redshift along the history; what the tip angle and the position of the cutoff do; and the closed shells of the free filling (Sections 14.19 to 14.21).
- The exact local exchange energy of the contact interaction, the Kohn-Sham potentials, the exact Fock exchange of the model's states, the dependence on the coupling and the cell volume, and the state of the eight zero modes (Sections 14.26 and 14.27).

**The four notebooks.**

| notebook | what it computes | PASS lines | figures |
| --- | --- | --- | --- |
| 14a | the block reduction and the rescaling identity, with exact algebra | 31 | 5 |
| 14b | the free spectra at zero 3-momentum, exact against numerical | 20 | 6 |
| 14c | the fold band, its slope, redshift, symmetries, the tip and the closed shells | 16 | 6 |
| 14d | the exact local exchange, the potentials and the zero-mode state | 18 | 4 |

None of them needs Rust: Notebooks 14b and 14c write the shooting function of the Revision Rust solver (the same RK4 integration and Pruefer angle) in a few lines of numpy, find its roots by plain bisection where the Rust solver uses a safeguarded Newton-bisection, and reproduce the solver's recorded numbers; Chapter 15 runs the Rust solver itself.

**The status of every statement.** As everywhere in this book, every statement carries one of the five labels of Chapter 0: PROVED, COMPUTED, ASSUMED, HYPOTHESIS, OPEN. In this chapter they are used as follows.

- PROVED: every identity of Sections 14.2 to 14.7, the boundary-condition facts of Section 14.12, the exact spectra of Section 14.13, the counting property of the shooting angle in Section 14.14, the fold band and its slope in Section 14.19, and the exchange and scaling formulas of Sections 14.26 and 14.27. The counting property is proved in the text of Section 14.14 and checked numerically by Notebook 14b; each of the others is verified in the Revision record by sympy in `Revision/kohn_sham/reports/ks-theory-python.json` (61 of 61 checks passed) and by WolframScript in `Revision/kohn_sham/reports/ks-theory-wolfram.json` (51 of 51 checks passed; a few checks exist only in the sympy report), and again by the notebooks of this chapter; the check names are given with each statement.
- COMPUTED: the numerical levels, slopes, shifts and closed shells; each comes with its measured error and the record file it reproduces (the Rust solver's report `Revision/kohn_sham/reports/ks-rust-solver.json`, 45 of 45 checks passed, and its result files).
- ASSUMED: the good sector (no dependence on the extra times); that both fold conditions are solved and filled at the fold $z = \pi/2$, where the two halves of a cell meet (the record's convention: the metric is degenerate there and no junction condition is derived); the regular tip condition at the cutoff $y = -L$, $L = 3$ (a choice of the numerical model; Section 14.20 shows what its angle does and reports what the Revision record measured about the position $L$ of the cutoff); the deflating history along which the Kohn-Sham states are computed, which is a **prescribed background**, given and not solved for (Section 14.3); the convention that counts the zero modes at zero 3-momentum as particle levels (Section 14.21).
- OPEN: the justification of that convention (Section 14.21), the limit of a very distant cutoff where the record does not establish it (Section 14.20), and the behaviour of the gas when the history is not slow (the time-dependent problem, Chapters 15 and 22).
- HYPOTHESIS: none in this chapter.

**Notation and units.** The author's coordinates are $x_0, \dots, x_7$, in this order: $x_0$ is the hidden space-like direction, listed first; $x_1, x_2, x_3$ are ordinary 3-space, which inflates; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which deflate exponentially. The flat frame metric is $\eta = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ in this order. The gamma matrix of the direction $x_4$ is written $\gamma^{(x_4)}$, and so on; these are the author's eight real $16 \times 16$ matrices of Chapters 4 and 5, read from the record `Revision/algebra/gammas.json`, with the Clifford relation $\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}$. The matrices $C = \gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$, $B = -iC\gamma^{(x_4)}$ and the chirality $\Gamma = \gamma^{(x_0)}\gamma^{(x_1)}\cdots\gamma^{(x_7)} = \mathrm{diag}(-1_8, 1_8)$ are those of Chapter 5. The three **Pauli matrices**, written row by row, are

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .
$$

Each squares to the $2 \times 2$ unit matrix, two different ones anticommute, and their products are $\sigma_1\sigma_2 = i\sigma_3$, $\sigma_2\sigma_3 = i\sigma_1$, $\sigma_3\sigma_1 = i\sigma_2$ (and with the order reversed the sign changes). In the numbers of this chapter the author's constant $H$ is 1 and the mass $m$ of dirac16complex is 1, as in the Revision runs; energies, momenta and temperatures are then in units of $m$ (which equals $H$), lengths in units of $1/H$. A prime on $a_4$ or $b_4$ means the derivative with respect to the time $x_4$; a prime on a function of $y$ means $d/dy$.

### 14.2 The author's field and the hidden coordinate y

**The metric.** The author's primordial field is the corrected metric of 2026-10-16 (Chapter 3, Sections 3.5 to 3.9). It is diagonal; its entries, in the order $x_0, \dots, x_7$, are

$$
g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\ -1,\ -g_t,\ -g_t,\ -g_t\big), \qquad g_t = e^{-2a_4}b_4(\sin^2 z)^{1/6},
$$

with $z = 6Hx_0$ taking every real value, the author's constant $H > 0$, and two functions $a_4(x_4)$ and $b_4(x_4) > 0$ of the time ($b_4$ is never 1); $(\sin^2 z)^{1/6}$ is the positive root. A **scale factor** is the number by which a coordinate step must be multiplied to give a length (the square root of the absolute value of the entry): along $x_1$ a step $dx_1$ has the length $e^{a_4}dx_1$, along an extra time the length $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}dx_5$, and along the hidden direction $e^{-a_4}b_4^{1/2}|\cot z|\,dx_0$. 3-space has no factor that depends on $z$. Wherever $\sin z\cos z \ne 0$ four entries are positive and four negative: the signature is (4,4). The history used in this book is $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = 1$ and $b_4(0) = 1$ (Section 14.3): along it $a_4$ grows, the 3-space factor $e^{a_4}$ grows (3-space **inflates**), and the factor $e^{-a_4}b_4^{1/2} = e^{-a_4/3}$ of the extra times and of the hidden direction shrinks exponentially (they **deflate** together).

**The cell and its two halves.** The entry $g_{00} = e^{-2a_4}b_4\cot^2 z$ vanishes where $\cos z = 0$ and grows without bound where $\sin z \to 0$. One period $0 < z < \pi$ is called a **cell**. The point $z = \pi/2$, where $\cos z = 0$, is the **fold**: it joins the two **halves** $0 < z < \pi/2$ and $\pi/2 < z < \pi$ of the cell. The ends $z \to 0$ and $z \to \pi$ of the cell, where $\sin z \to 0$, are the **tips**. The reflection $z \to \pi - z$ leaves $\sin z$ unchanged and changes the sign of $\cot z$; since the metric contains only $\cot^2 z$ and $\sin^2 z$, it maps the metric onto itself and one half onto the other. (This reflection is the isometry used by the pairing theorem T2 in Chapter 18.)

**The hidden coordinate.** The entry $g_{00}$ makes the hidden direction awkward. We replace $x_0$ by

$$
y = \frac{\ln|\sin z|}{6H} = \frac{\ln(\sin^2 z)}{12H}, \qquad z = 6Hx_0 .
$$

Line by line:

$$
\frac{dy}{dx_0} = \frac{1}{12H}\cdot\frac{2\sin z\cos z}{\sin^2 z}\cdot 6H = \cot z .
$$

Rule: the chain rule; the derivative of $\ln u$ is $1/u$ times the derivative of $u$, the derivative of $\sin^2 z$ is $2\sin z\cos z$, and $dz/dx_0 = 6H$. It holds for every real $z$ with $\sin z \ne 0$, on both halves of every cell.

$$
g_{00}\,dx_0^2 = e^{-2a_4}b_4\cot^2 z\,dx_0^2 = e^{-2a_4}b_4\,dy^2 = f^2\,dy^2, \qquad f = e^{-a_4}b_4^{1/2} .
$$

Rule: square the previous line, $dy^2 = \cot^2 z\,dx_0^2$, and multiply by $e^{-2a_4}b_4$. The number $f$ is the **hidden scale**: a step $dy$ along the hidden direction has the proper length $f\,dy$.

$$
e^{6Hy} = |\sin z|, \qquad (\sin^2 z)^{1/6} = |\sin z|^{1/3} = e^{2Hy} .
$$

Rule: multiply the definition of $y$ by $6H$ and take the exponential of both sides; then take the power $1/3$.

On each half of the cell $|\sin z|$ runs from 0 at the tip to 1 at the fold, so $y$ runs from $-\infty$ at the tip to $0$ at the fold. Because $|\sin z|$ is unchanged by $z \to \pi - z$, the same $y$ describes both halves. On the first half $\cot z > 0$, so $y$ increases with $x_0$; on the second half $\cot z < 0$, so $y$ decreases with $x_0$: on both halves $y$ increases toward the fold. Inserting the last two lines into the metric gives its form in the coordinate $y$:

$$
ds^2 = e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 + f^2\left[dy^2 - e^{2Hy}(dx_5^2 + dx_6^2 + dx_7^2)\right], \qquad f = e^{-a_4}b_4^{1/2} .
$$

Rule: $g_{00}dx_0^2 = f^2dy^2$ and $-e^{-2a_4}b_4(\sin^2 z)^{1/6} = -f^2e^{2Hy}$. The factor $e^{Hy}$, the **warp**, multiplies only the extra times; the block of the hidden direction and the extra times is $f^2$ times a space of constant curvature $-H^2$ (Chapter 3). Its scale factors (the entries of the diagonal **vielbein**), in the order $(y, x_1, \dots, x_7)$, are

$$
h = \big(f,\ e^{a_4},\ e^{a_4},\ e^{a_4},\ 1,\ fe^{Hy},\ fe^{Hy},\ fe^{Hy}\big) .
$$

On the history ($b_4 = e^{(4/3)a_4}$) the hidden scale is $f = e^{-a_4}e^{(2/3)a_4} = e^{-a_4/3}$ (rule: $b_4^{1/2} = e^{(2/3)a_4}$); the cut-off half $-L \le y \le 0$ has the proper length $fL$, which shrinks along the history.

**The volume.** The square root of the absolute value of the determinant of a diagonal metric is the product of its scale factors:

$$
\sqrt{|g|} = f\cdot(e^{a_4})^3\cdot 1\cdot(fe^{Hy})^3 = e^{3a_4}f^4e^{3Hy} = e^{-a_4}b_4^2e^{3Hy} .
$$

Rule: multiply the eight entries of $h$; $f^4 = e^{-4a_4}b_4^2$. In the author's $x_0$ chart the same product is $e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$; the two differ by the factor $|dy/dx_0| = |\cot z|$, as they must. The proper 7-volume of a coordinate cell grows like $e^{-a_4}b_4^2$, on the history like $e^{-a_4}e^{(8/3)a_4} = e^{(5/3)a_4}$. Toward the tip the factor $e^{3Hy}$ goes to zero: at $y = -3$ it is $e^{-9} \approx 1.23\times10^{-4}$. Status: PROVED; checks geometry_hidden_coordinate, geometry_sqrt_det and geometry_line_element of `Revision/kohn_sham/reports/ks-theory-python.json` (also in the Wolfram report `Revision/kohn_sham/reports/ks-theory-wolfram.json`).

**The momentum weight.** A plane wave $e^{ik_1x_1}$ along 3-space has the coordinate momentum $k_1$; the length of a coordinate step is $e^{a_4}dx_1$, so the momentum per unit length, the one a quantum feels, is $k_1e^{-a_4}$. We write

$$
\kappa(x_4) = e^{-a_4(x_4)}
$$

for this **momentum weight**. It is the same at every point $y$ of the hidden direction (3-space has no warp), and it decreases as $a_4$ grows: 3-momenta are **redshifted** while 3-space inflates.

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
\Psi = e^{i\mathbf k\cdot\mathbf x}\,e^{-(3/2)Hy}\,e^{a_4/2}\,b_4^{-1}\,\chi(y, x_4) ,
$$

a plane wave along 3-space, the factor $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$, and a column $\chi$ of 16 unknown functions of $y$ and of the time. Section 14.4 shows that $\chi$ obeys exactly, for every history $a_4(x_4)$, $b_4(x_4)$, an equation of the form

$$
i\,\partial_{x_4}\chi = h(x_4)\,\chi ,
$$

with a Hermitian matrix operator $h$ that depends on the time only through the two numbers $f(x_4)$ and $\kappa(x_4)$ (and through the potentials). This is the exact evolution of one orbital in the mean field.

**The stationary-slice (adiabatic) ansatz.** A **slice** is one instant $x_4$ of the history; $a_{4,0} = a_4(x_4)$ and $b_{4,0} = b_4(x_4)$ are the values there, and $f_0 = e^{-a_{4,0}}b_{4,0}^{1/2}$, $\kappa_0 = e^{-a_{4,0}}$. At a slice we freeze $h$ at its value $h(a_{4,0}, f_0)$ and look for the stationary orbitals

$$
h(a_{4,0}, f_0)\,\chi = \varepsilon\,\chi, \qquad \Psi = e^{-i\varepsilon x_4}\,e^{i\mathbf k\cdot\mathbf x}\,e^{-(3/2)Hy}\,e^{a_{4,0}/2}\,b_{4,0}^{-1}\,\chi(y)\,/\sqrt{\ell^3v_t}, \qquad \int_{-L}^{0}\chi^\dagger\chi\,dy = 1 .
$$

The number $\varepsilon$ is the **level** (the energy of the orbital); the hidden direction is cut at $y = -L$ ($L = 3$ in the runs), and the orbital is normalised on one half of the cell (Section 14.12). The Kohn-Sham state of the slice fills the lowest particle levels. This is the **adiabatic** picture: if $h$ changes slowly enough along the history, a quantum stays in the level it occupies. The exact evolution conserves the 3-momentum, the block and the fold condition of every orbital (all defined below), so a quantum can only make transitions between levels of the same kind; Chapter 15 measures how slowly $h$ changes. The record states this in `Revision/kohn_sham/ks-theory.json`, section adiabaticity.

**The history is a PRESCRIBED BACKGROUND.** The slices are taken along the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = 1$, $b_4(0) = 1$ and $H = 1$, so $a_{4,0} = 0, 0.5, 1, 1.5, 2$ are five instants, with $b_{4,0} = e^{(4/3)a_{4,0}}$. This history is prescribed, not solved for. In the corrected metric the field equations of $a_4$ and $b_4$ (Chapter 12) allow it only with a diagonal source whose components do not depend on $x_0$, whose hidden pressure equals its extra-time pressure ($p_0 = p_t$), and which grows along the history (`Revision/metric_warped/results/warped-metric.json`, key history_source). The Kohn-Sham states do not supply it: their energy density varies along the hidden direction, and with interaction their hidden and extra-time pressures differ. The record `Revision/field_equations_a4/reports/ks-source-conditions.json` (5 of 5 checks PASS) shows this with its checks ks_profiles_depend_on_x0, ks_hidden_pressure_condition, ks_offdiagonal_condition (this condition holds), ks_history_is_a_prescribed_background and ks_zero_source_states_listed (Chapter 17 explains it in full). So the Kohn-Sham gas is a **test field** on a given background: it feels the deflating field but does not act back on it.

### 14.4 The spin connection and the factor that removes it

**What we need.** The operator $\gamma^\mu D_\mu = \sum_\mu \gamma^\mu\partial_\mu + \sum_\mu\gamma^\mu\Omega_\mu$ contains the spin connection only through the matrix $\sum_\mu\gamma^\mu\Omega_\mu$. Chapter 6 derived the canonical spin connection in general; here we compute this one matrix for the diagonal vielbein $h$ of Section 14.2, with $a_4$ and $b_4$ arbitrary functions of $x_4$, so that the result holds along every history.

**Step 1: the Christoffel symbols of a diagonal metric.** For a diagonal metric with the entries $g_{nn}$ the Christoffel symbols $\Gamma^n{}_{mk} = \tfrac12 g^{nl}(\partial_m g_{lk} + \partial_k g_{lm} - \partial_l g_{mk})$ (sum over $l$) reduce to

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

**Step 5: the author's field.** Here the scale factors depend only on $x_4$ (through $a_4$ and $b_4$) and on $y$; the scale factor of $x_4$ is 1 and that of $y$ is $f$. In the vielbein language the frame direction of $y$ is that of $x_0$, so the gamma that goes with $y$ is $\gamma^{(x_0)}$. Write

$$
h_4 = \frac{\partial_{x_4}f}{f} = \frac{b_4'}{2b_4} - a_4'
$$

for the rate at which the hidden scale changes (rule: $\ln f = -a_4 + \tfrac12\ln b_4$). Step 4 gives, direction by direction:

- the hidden direction, $\ln h_y = \ln f$: $\partial_{x_4}\ln f = h_4$, so the contribution is $\tfrac12h_4\gamma^{(x_4)}$;
- each 3-space direction, $\ln h_l = a_4$: the contribution is $\tfrac12a_4'\gamma^{(x_4)}$;
- the time, $h_{x_4} = 1$: no contribution;
- each extra time, $\ln h_l = \ln f + Hy$: $\partial_{x_4}$ gives $h_4$ and $\partial_y$ gives $H$, divided by $h_y = f$, so the contribution is $\tfrac12h_4\gamma^{(x_4)} + \tfrac12(H/f)\gamma^{(x_0)}$.

Adding the eight contributions:

$$
\sum_\mu\gamma^\mu\Omega_\mu = \Big(\tfrac12h_4 + 3\cdot\tfrac12a_4' + 3\cdot\tfrac12h_4\Big)\gamma^{(x_4)} + 3\cdot\tfrac12\frac{H}{f}\gamma^{(x_0)} = \Big(2h_4 + \tfrac32a_4'\Big)\gamma^{(x_4)} + \frac32\frac{H}{f}\gamma^{(x_0)} .
$$

Rule: one hidden direction, three 3-space directions, three extra times; collect the terms.

$$
\sum_\mu\gamma^\mu\Omega_\mu = \frac32\frac{H}{f}\,\gamma^{(x_0)} + \Big(\frac{b_4'}{b_4} - \frac{a_4'}{2}\Big)\gamma^{(x_4)} .
$$

Rule: $2h_4 + \tfrac32a_4' = \tfrac{b_4'}{b_4} - 2a_4' + \tfrac32a_4'$. In the author's chart $H/f = He^{a_4}b_4^{-1/2}$, so the first term is $\tfrac32He^{a_4}b_4^{-1/2}\gamma^{(x_0)}$. On the history ($a_4' = AH = 1$, $b_4'/b_4 = \tfrac43$) at the first slice ($f = 1$) the term is $\tfrac32\gamma^{(x_0)} + \tfrac56\gamma^{(x_4)}$; figure 3 of Notebook 14a shows the eight contributions there. Note that $\Omega_y$ is not zero, because the scale factor $f$ of $y$ depends on the time. Status: PROVED; checks `spin_connection_compatibility` (the curved gammas are covariantly constant, the proof that this is the right connection), `spin_connection_slash`, `spin_connection_time_terms` and `spin_connection_slash_x0_chart` (the same in the author's chart, for every real $z$) of `Revision/kohn_sham/reports/ks-theory-python.json` and of the Wolfram report. That the surviving term belongs to the diagonal vielbein, and can be changed by a change of frame or of the field, is the scope correction of Chapter 8.

**Step 6: the factor $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$ removes it.** Write $F = e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$, insert the ansatz $\Psi = e^{i\mathbf k\cdot\mathbf x}F\chi(y, x_4)$ into $\gamma^\mu D_\mu\Psi = \sum_\mu\gamma^\mu\partial_\mu\Psi + \sum_\mu\gamma^\mu\Omega_\mu\Psi$, and go term by term.

$$
\frac{\gamma^{(x_0)}}{f}\,\partial_y\big(F\chi\big) = F\,\frac{\gamma^{(x_0)}}{f}\Big(\partial_y\chi - \frac32H\chi\Big) .
$$

Rule: the product rule and $\partial_yF = -\tfrac32HF$. The term $-\tfrac32(H/f)\gamma^{(x_0)}\chi$ cancels the $+\tfrac32(H/f)\gamma^{(x_0)}\chi$ of the spin connection.

$$
\gamma^{(x_4)}\,\partial_{x_4}\big(F\chi\big) = F\,\gamma^{(x_4)}\Big(\partial_{x_4}\chi + \Big(\frac{a_4'}{2} - \frac{b_4'}{b_4}\Big)\chi\Big) .
$$

Rule: the product rule; the derivative of $e^{a_4/2}$ is $\tfrac12a_4'e^{a_4/2}$ and that of $b_4^{-1}$ is $-b_4'/b_4^2 = -(b_4'/b_4)\,b_4^{-1}$ (the scale factor of $x_4$ is 1). The term $(\tfrac12a_4' - b_4'/b_4)\gamma^{(x_4)}\chi$ cancels the $(b_4'/b_4 - \tfrac12a_4')\gamma^{(x_4)}\chi$ of the spin connection.

$$
\frac{\gamma^{(x_j)}}{e^{a_4}}\,\partial_j e^{i\mathbf k\cdot\mathbf x} = i\kappa k_j\gamma^{(x_j)}\,e^{i\mathbf k\cdot\mathbf x}, \qquad j = 1, 2, 3 .
$$

Rule: $\partial_j e^{i\mathbf k\cdot\mathbf x} = ik_je^{i\mathbf k\cdot\mathbf x}$, and $e^{-a_4} = \kappa$ (Section 14.2). The extra times give nothing (good sector). Dividing by the common factor $e^{i\mathbf k\cdot\mathbf x}F$, the Kohn-Sham equation becomes

$$
\frac1f\gamma^{(x_0)}\partial_y\chi + \gamma^{(x_4)}\partial_{x_4}\chi + i\kappa k_j\gamma^{(x_j)}\chi = \big(M - iv\gamma^{(x_4)}\big)\chi \qquad (\text{sum over } j = 1, 2, 3) .
$$

The spin connection has disappeared, exactly and for every history. Without the factor $e^{-(3/2)Hy}$ the term $\tfrac32(H/f)\gamma^{(x_0)}\chi$ would survive, and without the factor $e^{a_4/2}b_4^{-1}$ the term $(b_4'/b_4 - \tfrac12a_4')\gamma^{(x_4)}\chi$. The factor $F$ is the **half-density** of the volume: $F^2\sqrt{|g|} = e^{-3Hy}e^{a_4}b_4^{-2}\cdot e^{-a_4}b_4^2e^{3Hy} = 1$ (rule: multiply the exponentials), so $\int\sqrt{|g|}\,\Psi^\dagger\Psi$ over the hidden direction is $\int\chi^\dagger\chi\,dy$ for every $a_4$ and $b_4$. Status: PROVED; checks ansatz_removes_spin_connection, ansatz_without_y_factor_term_survives, ansatz_without_x4_factor_term_survives and ansatz_norm (both reports).

**Step 7: the Hamiltonian form.** Solve the last equation for the time derivative, line by line.

$$
\gamma^{(x_4)}\partial_{x_4}\chi = M\chi - iv\gamma^{(x_4)}\chi - \frac1f\gamma^{(x_0)}\partial_y\chi - i\kappa k_j\gamma^{(x_j)}\chi .
$$

Rule: move every term except the time term to the right side.

$$
\partial_{x_4}\chi = -M\gamma^{(x_4)}\chi - iv\chi + \frac1f\gamma^{(x_4)}\gamma^{(x_0)}\partial_y\chi + i\kappa k_j\gamma^{(x_4)}\gamma^{(x_j)}\chi .
$$

Rule: multiply from the left by $-\gamma^{(x_4)}$; on the left $-\gamma^{(x_4)}\gamma^{(x_4)} = -\eta_{44} = 1$; on the right $-\gamma^{(x_4)}(-iv\gamma^{(x_4)}) = iv\gamma^{(x_4)}\gamma^{(x_4)} = -iv$.

$$
i\partial_{x_4}\chi = h\chi, \qquad h = \frac{i}{f}\gamma^{(x_4)}\gamma^{(x_0)}\partial_y - \kappa k_j\gamma^{(x_4)}\gamma^{(x_j)} + M\big(-i\gamma^{(x_4)}\big) + v .
$$

Rule: multiply by $i$ and use $i\cdot i = -1$.

**Why $h$ is Hermitian.** A matrix $X$ is **Hermitian** when it equals its conjugate transpose, $X^\dagger = X$; an operator is Hermitian (self-adjoint) when $\int\varphi^\dagger(h\chi)\,dy = \int(h\varphi)^\dagger\chi\,dy$ for all allowed columns $\varphi$, $\chi$; then its levels are real and orbitals of different levels are orthogonal. Each piece of $h$ qualifies. (i) $\gamma^{(x_4)}\gamma^{(x_0)}$ is real and symmetric: $(\gamma^{(x_4)}\gamma^{(x_0)})^T = (\gamma^{(x_0)})^T(\gamma^{(x_4)})^T = \gamma^{(x_0)}(-\gamma^{(x_4)}) = \gamma^{(x_4)}\gamma^{(x_0)}$, by the symmetry pattern $(\gamma^a)^T = \eta_{aa}\gamma^a$ of Chapter 5 and the anticommutation of two different gammas; so $i\gamma^{(x_4)}\gamma^{(x_0)}$ is anti-Hermitian, $\partial_y$ is anti-Hermitian too (integration by parts, when the boundary terms vanish, Section 14.12), the product of the two, which commute, is Hermitian, and the positive number $1/f$ does not change that. (ii) $\gamma^{(x_4)}\gamma^{(x_j)}$ for a 3-space direction is real and symmetric by the same rule, hence Hermitian. (iii) $(-i\gamma^{(x_4)})^\dagger = i(\gamma^{(x_4)})^T = -i\gamma^{(x_4)}$, and $(-i\gamma^{(x_4)})^2 = -\eta_{44} = 1$. (iv) $v$ is a real number times the unit matrix. Status: PROVED; check hamiltonian_16_hermitian.

### 14.5 Eight blocks of two components

**Only $|\mathbf k|$ matters.** Section 14.6 shows that a rotation of 3-space does not change the levels. So we may turn $\mathbf k$ into the direction $x_1$, $\mathbf k = (k, 0, 0)$. Then $h$ contains only the three gammas $\gamma^{(x_0)}$, $\gamma^{(x_1)}$, $\gamma^{(x_4)}$, and it is convenient to name three products:

$$
A_0 = \gamma^{(x_0)}, \qquad A_1 = \gamma^{(x_0)}\gamma^{(x_1)}, \qquad A_4 = \gamma^{(x_0)}\gamma^{(x_4)} .
$$

**Two rules from Chapter 5.** Let $P$ be a product of $p$ different gammas. (Rule 1) Moving a gamma $\gamma^c$ from the left of $P$ to its right gives the sign $(-1)^{p-1}$ if $\gamma^c$ is one of the factors and $(-1)^p$ if it is not, because passing each different factor costs a sign. (Rule 2) $PP = (-1)^{p(p-1)/2}$ times the product of the $\eta$ of its factors.

**Three labels.** Define

$$
J = \gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_4)}, \qquad K_1 = \gamma^{(x_2)}\gamma^{(x_3)}, \qquad K_2 = \gamma^{(x_5)}\gamma^{(x_6)} .
$$

By Rule 1, $J$ ($p = 3$) commutes with its own three factors and anticommutes with the five other gammas; $K_1$ ($p = 2$) anticommutes with $\gamma^{(x_2)}$, $\gamma^{(x_3)}$ and commutes with the six others; $K_2$ anticommutes with $\gamma^{(x_5)}$, $\gamma^{(x_6)}$ and commutes with the others. A product of gammas commutes with $J$ when it contains an even number of factors that anticommute with $J$. Therefore all three commute with $A_0, A_1, A_4$ (built from $\gamma^{(x_0)}, \gamma^{(x_1)}, \gamma^{(x_4)}$), with $C$ (for $J$ the two anticommuting factors $\gamma^{(x_2)}, \gamma^{(x_3)}$ give two signs, which cancel), with $B = -iC\gamma^{(x_4)}$, and with each other. By Rule 2:

$$
J^2 = (-1)^3\,\eta_{00}\eta_{11}\eta_{44} = (-1)(1)(1)(-1) = +1,
$$

$$
K_1^2 = (-1)^1\eta_{22}\eta_{33} = -1, \qquad K_2^2 = (-1)^1\eta_{55}\eta_{66} = -1 .
$$

So $J$ has the eigenvalues $j = \pm1$, and $K_1$, $K_2$ have the eigenvalues $is_2$, $is_3$ with $s_2, s_3 = \pm1$ (if $Xu = cu$ for a column $u \ne 0$ and $X^2 = 1$, then $u = X^2u = c^2u$, so $c^2 = 1$; with $X^2 = -1$ the same step gives $c^2 = -1$). Status: PROVED; check blocks_commuting_set.

**The projectors.** A **projector** is a matrix with $P^2 = P$; its eigenvalues are 0 or 1 (from $\lambda^2 = \lambda$), so its trace equals the number of eigenvalues 1, its **rank** (the dimension of the space it projects onto). For each of the eight label triples put

$$
P(j, s_2, s_3) = \frac{1 + jJ}{2}\cdot\frac{1 - is_2K_1}{2}\cdot\frac{1 - is_3K_2}{2} .
$$

Each factor is $\tfrac12(1 + X)$ with $X^2 = 1$ ($(jJ)^2 = 1$, $(-is_2K_1)^2 = -K_1^2 = 1$), hence a projector; the three factors commute, so their product is a projector; it keeps exactly the columns with $J = j$, $K_1 = is_2$, $K_2 = is_3$. Multiplied out, $P$ is $\tfrac18$ times the unit matrix plus seven products of different gammas ($J$, $K_1$, $K_2$, $JK_1$, $JK_2$, $K_1K_2$, $JK_1K_2$, each with a number in front), and every product of one or more different gammas has trace 0 (Chapter 5). So

$$
\mathrm{tr}\,P(j, s_2, s_3) = \tfrac18\,\mathrm{tr}\,1 = \tfrac{16}{8} = 2 .
$$

The eight projectors have rank 2 and add up to the unit matrix: **the 16 components split into eight blocks of two**. Status: PROVED; check blocks_projectors.

**A basis in each block.** Inside a block, $A_0 = \gamma^{(x_0)}$ squares to 1 and $A_1$ anticommutes with it ($A_1 = \gamma^{(x_0)}\gamma^{(x_1)}$ contains $\gamma^{(x_0)}$ once and $p = 2$, so by Rule 1 the sign is $-1$), so $A_0$ has the eigenvalue $+1$ once and $-1$ once in the block. The record chooses

$$
v_+ = 8\,P(j, s_2, s_3)\,\tfrac12\big(1 + \gamma^{(x_0)}\big)\,e_c, \qquad v_- = A_1v_+ ,
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

Rule: $A_4$ anticommutes with $A_0$ (Rule 1), so it has no diagonal entries; and $A_0A_1A_4 = \gamma^{(x_0)}\gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_0)}\gamma^{(x_4)} = \gamma^{(x_1)}\gamma^{(x_0)}\gamma^{(x_4)} = -J$, which is the number $-j$ in the block; with $\sigma_3(-i\sigma_2) = -i\sigma_3\sigma_2 = -\sigma_1$ the condition $-\sigma_1A_4 = -j$ gives $A_4 = j\sigma_1$.

$$
C = A_1K_1 \to (-i\sigma_2)(is_2) = s_2\sigma_2, \qquad B = -iJK_1 \to -i\,j\,(is_2) = js_2 .
$$

Rule: $C = \gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)} = A_1K_1$; and $JK_1 = \gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_4)}\gamma^{(x_2)}\gamma^{(x_3)} = C\gamma^{(x_4)}$ after moving $\gamma^{(x_4)}$ past two gammas (two signs), so $B = -iC\gamma^{(x_4)} = -iJK_1$. So $B$ is a number in every block, $+1$ or $-1$: the **Krein sign** $js_2$ of the block.

$$
\gamma^{(x_4)} = A_0A_4 \to ij\sigma_2, \qquad \gamma^{(x_1)} = A_0A_1 \to -\sigma_1, \qquad \gamma^{(x_4)}\gamma^{(x_1)} \to (ij\sigma_2)(-\sigma_1) = -j\sigma_3 .
$$

Rule: $A_0A_0 = 1$; the Pauli products $\sigma_3\sigma_1 = i\sigma_2$, $\sigma_3\sigma_2 = -i\sigma_1$, $\sigma_2\sigma_1 = -i\sigma_3$.

The record lists eleven such forms (for $\gamma^{(x_0)}$, $A_1$, $A_4$, $B$, $C$, $BC = -i\gamma^{(x_4)} \to j\sigma_2$, $\gamma^{(x_4)}\gamma^{(x_1)}$, $B\gamma^{(x_0)} \to js_2\sigma_3$, $J$, $K_1$, $K_2$); Notebook 14a checks all of them. Not every matrix is block diagonal: $\gamma^{(x_2)}$, $\gamma^{(x_5)}$ and $\gamma^{(x_0)}\gamma^{(x_2)}$ anticommute with $J$ and connect different blocks, which is why $\mathbf k$ was turned along $x_1$. Status: PROVED; checks blocks_forms and blocks_not_everything_block_diagonal.

**The block Hamiltonian.** Put the forms into $h$ of Section 14.4 with $\mathbf k = (k, 0, 0)$: $(i/f)\gamma^{(x_4)}\gamma^{(x_0)} = -(i/f)A_4 \to -(i/f)j\sigma_1$; $-\kappa k\gamma^{(x_4)}\gamma^{(x_1)} \to j\kappa k\sigma_3$; $M(-i\gamma^{(x_4)}) \to jM\sigma_2$. So in every block of type $j$

$$
h_j = j\left[-\frac{i}{f}\sigma_1\frac{d}{dy} + M\sigma_2 + \kappa k\,\sigma_3\right] + v .
$$

It depends on $j$ but not on $s_2$, $s_3$: there are only **two types of block**, four blocks of each type. The slice enters through the two numbers $f$ and $\kappa$, which are the same at every $y$. Status: PROVED; check block_hamiltonian.

**The first-order form.** The eigenvalue equation $h_j\chi = \varepsilon\chi$ is a pair of first-order differential equations. Line by line:

$$
-\frac{ij}{f}\sigma_1\chi' = (\varepsilon - v)\chi - j(M\sigma_2 + \kappa k\sigma_3)\chi .
$$

Rule: move the terms without derivative to the right; $\chi'$ is $d\chi/dy$.

$$
\chi' = ijf(\varepsilon - v)\sigma_1\chi - if\,(M\sigma_1\sigma_2 + \kappa k\,\sigma_1\sigma_3)\chi .
$$

Rule: multiply from the left by $ijf\sigma_1$; $(ijf\sigma_1)(-(ij/f)\sigma_1) = -i^2j^2\sigma_1^2 = 1$ and $j\cdot j = 1$.

$$
\chi' = fN\chi, \qquad N = M\sigma_3 - \kappa k\,\sigma_2 + ij(\varepsilon - v)\,\sigma_1 .
$$

Rule: $\sigma_1\sigma_2 = i\sigma_3$, $\sigma_1\sigma_3 = -i\sigma_2$, so $-i(iM\sigma_3 - i\kappa k\sigma_2) = M\sigma_3 - \kappa k\sigma_2$. The hidden scale multiplies the whole right side: in the proper hidden coordinate $fy$ the equation does not contain $f$ at all. Status: PROVED; check block_ode_equivalent.

**The two types mirror each other.** Write $h_j - v = jD(M, k)$ with $D(M, k) = -(i/f)\sigma_1\,d/dy + M\sigma_2 + \kappa k\sigma_3$. Then:

- $h_{-1} - v = -(h_{+1} - v)$. For $v = 0$ the levels of the blocks $j = -1$ are the negatives of those of $j = +1$.
- $\sigma_3D(M, k)\sigma_3 = (i/f)\sigma_1\,d/dy - M\sigma_2 + \kappa k\sigma_3 = -D(M, -k)$, because $\sigma_3\sigma_1\sigma_3 = -\sigma_1$ and $\sigma_3\sigma_2\sigma_3 = -\sigma_2$. Hence $\sigma_3h_j(k)\sigma_3 = h_{-j}(-k)$: the orbital $\sigma_3\chi$ of $(-j, -k)$ has the same level as the orbital $\chi$ of $(j, k)$.

Status: PROVED; check block_type_relation.

### 14.6 The chirality matrix Γ on the blocks, and the rotations of 3-space

**Γ pairs the two types.** The chirality $\Gamma$ is a product of all eight gammas, so it anticommutes with every gamma (Rule 1 with $p = 8$: a factor passes seven others), with every product of an odd number of gammas such as $J$, and commutes with every even product such as $K_1$, $K_2$. If $Jv = jv$, then $J\Gamma v = -\Gamma Jv = -j\,\Gamma v$, while $K_1\Gamma v = \Gamma K_1 v$: so $\Gamma$ maps the block $(j, s_2, s_3)$ onto the block $(-j, s_2, s_3)$. In the block basis its $2 \times 2$ entry between the paired blocks is $s_2\sigma_2$ (computed in Notebook 14a, In [16]; its figure 4 shows where these entries sit). Status: PROVED; check blocks_relation_to_Gamma.

**Γ reverses the mass.** Line by line:

$$
\sigma_2D(M, k)\sigma_2 = \frac{i}{f}\sigma_1\frac{d}{dy} + M\sigma_2 - \kappa k\sigma_3 = -D(-M, k) .
$$

Rule: $\sigma_2\sigma_1\sigma_2 = -\sigma_1$, $\sigma_2\sigma_2\sigma_2 = \sigma_2$, $\sigma_2\sigma_3\sigma_2 = -\sigma_3$.

$$
\sigma_2h_j(M, k)\sigma_2 = j\big(-D(-M, k)\big) + v = h_{-j}(-M, k) .
$$

Rule: $h_j = jD + v$ and $\sigma_2\sigma_2 = 1$. So if $\chi$ solves the block equation of type $j$ with the mass $M$, then $\sigma_2\chi$ solves the block equation of type $-j$ with the mass $-M$, at the same $k$, the same potential $v$ and the same level $\varepsilon$. Because $\sigma_2(\chi_1, \chi_2) = (-i\chi_2, i\chi_1)$, the map also exchanges the two fold conditions $\chi_2(0) = 0$ and $\chi_1(0) = 0$ of Section 14.12. Status: PROVED; check block_Gamma_map.

The same fact is visible in 16 components without blocks. $\Gamma$ anticommutes with every $\gamma^\mu$ and commutes with every $\Omega_\mu$ (a sum of products of two gammas), so $\gamma^\mu D_\mu(\Gamma\Psi) = -\Gamma\gamma^\mu D_\mu\Psi$. If $\gamma^\mu D_\mu\Psi = (M - iv\gamma^{(x_4)})\Psi$, then

$$
\gamma^\mu D_\mu(\Gamma\Psi) = -\Gamma\big(M - iv\gamma^{(x_4)}\big)\Psi = \big(-M - iv\gamma^{(x_4)}\big)\Gamma\Psi ,
$$

where the last step uses $\Gamma\gamma^{(x_4)} = -\gamma^{(x_4)}\Gamma$. Here $M$ and $v$ are regarded as given functions of $y$. In the full theory they are made by the quanta themselves, and how the parameters $m$, $\lambda$ and the boundary conditions transform is the content of the pairing theorems: T1 for the field equations, which Chapter 18 proves (the chirality MATRIX $\Gamma$ carries the solutions of the Lagrangian with $(m, \lambda)$ to those with $(-m, -\lambda)$), and T3 for the Kohn-Sham states, which Chapter 19 proves (the block map with the two fold conditions exchanged and the tip angle $\theta \to \pi - \theta$ carries a state with $(m, \lambda, \theta)$ to one with $(-m, +\lambda, \pi - \theta)$). On the blocks, $\sigma_2$ also exchanges the tip condition $b(-L) = 0$ with $a(-L) = 0$ (Section 14.12). The maps of this theory are matrices. The author's gammas are real, so for a real field plain complex conjugation changes nothing and is not a charge conjugation; the charge-conjugation matrices of the theory are $\mathcal C_+ = C$ and $\mathcal C_- = \Gamma C$ (Chapter 5). The map used here is the chirality matrix $\Gamma$ itself, the real matrix map of the theorem T1, which reverses the mass; on the blocks it acts as $s_2\sigma_2$ from the block $(j, s_2, s_3)$ to the block $(-j, s_2, s_3)$.

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

Rule: $(c - sG)^2 = c^2 - s^2 - 2csG$ (with $G^2 = -1$), the double-angle formulas $c^2 - s^2 = \cos\theta$, $2cs = \sin\theta$, and $\gamma^{(x_1)}G = \gamma^{(x_2)}$. So $R$ turns the momentum term $k\gamma^{(x_1)}$ into the same momentum in a rotated direction. And $R$ commutes with $\gamma^{(x_0)}$, $\gamma^{(x_4)}$, $B$ and $C$ (each contains $\gamma^{(x_1)}$ and $\gamma^{(x_2)}$ both or neither, so the signs cancel), so it changes nothing else in $h$. Hence the levels of the whole 16-component problem depend on $|\mathbf k|$ only, and $\mathbf k = (k, 0, 0)$ is no loss of generality. Status: PROVED; check rotation_invariance. (The labels $j$ themselves refer to the direction of $\mathbf k$: a rotation by $\pi$, $R = G$, anticommutes with $J$ and turns the blocks $(j, k)$ into $(-j, -k)$, in agreement with the $\sigma_3$ relation of Section 14.5.)

### 14.7 The exact rescaling identity between the slices

**Where the slice enters.** Look at the block Hamiltonian $h_j$ of Section 14.5. The slice $a_{4,0}$, $b_{4,0}$ appears in it only through the two numbers $f_0 = e^{-a_{4,0}}b_{4,0}^{1/2}$ and $\kappa_0 = e^{-a_{4,0}}$, which are the same at every $y$. The extra times themselves do not appear (the good sector has no extra-time momentum); they enter only through the proper volume of the cell, that is through the densities. Line by line, what follows:

$$
Y = f_0y, \qquad \frac{1}{f_0}\frac{d}{dy} = \frac{d}{dY}, \qquad h_j = j\left[-i\sigma_1\frac{d}{dY} + M\sigma_2 + \big(ke^{-a_{4,0}}\big)\sigma_3\right] + v .
$$

Rule: the **proper hidden coordinate** $Y$ measures proper length along $y$; the chain rule gives $d/dy = f_0\,d/dY$; and $\kappa_0k = ke^{-a_{4,0}}$. This is the block Hamiltonian of the first slice ($a_4 = 0$, $b_4 = 1$, so $f = \kappa = 1$) with the momentum $ke^{-a_{4,0}}$.

- The interval $-L \le y \le 0$ becomes $-f_0L \le Y \le 0$; the warp $e^{Hy}$ becomes $e^{(H/f_0)Y}$; and the orbital normalised in $Y$ is $\chi_Y = \chi/\sqrt{f_0}$ (rule: $\int\chi_Y^\dagger\chi_Y\,dY = \int(\chi^\dagger\chi/f_0)\,f_0\,dy$).
- At the slice the allowed momenta are $\Delta k\,\mathbf n$ (Section 14.3); by the line above they act exactly like the momenta $\Delta k\,e^{-a_{4,0}}\,\mathbf n$ at the first slice, which belong to the box $\ell e^{a_{4,0}}$ (because $\Delta k = 2\pi/\ell$).
- A density per unit proper volume is the orbital density per unit $y$ times the factor $P$ of the first line below, because the proper volume element of the cell is $\sqrt{|g|}\,\ell^3v_t\,dy = e^{-a_{4,0}}b_{4,0}^2e^{3Hy}\ell^3v_t\,dy$. The partner problem at the first slice has the constant $H/f_0$, the box $\ell e^{a_{4,0}}$ and the extra-time volume $v_te^{-3a_{4,0}}b_{4,0}^{3/2}$, and so the factor $P'(Y)$ of the second line, at the proper coordinate $Y = f_0y$.

$$
P = \frac{e^{-3Hy}\,e^{a_{4,0}}}{\ell^3v_t\,b_{4,0}^2}, \qquad P'(Y) = \frac{e^{-3(H/f_0)Y}}{\ell^3e^{3a_{4,0}}\,v_te^{-3a_{4,0}}b_{4,0}^{3/2}} = \frac{e^{-3Hy}}{\ell^3v_t\,b_{4,0}^{3/2}} .
$$

Rule: $\sqrt{|g|}$ of Section 14.2 at the slice; for the partner, $a_4 = 0$ and $b_4 = 1$, the box $(\ell e^{a_{4,0}})^3$, and $(H/f_0)Y = Hy$.

$$
\frac{P'}{f_0} = \frac{e^{-3Hy}\,e^{a_{4,0}}\,b_{4,0}^{-1/2}}{\ell^3v_t\,b_{4,0}^{3/2}} = P .
$$

Rule: $1/f_0 = e^{a_{4,0}}b_{4,0}^{-1/2}$ and $b_{4,0}^{-1/2}b_{4,0}^{-3/2} = b_{4,0}^{-2}$. With $\chi_Y^\dagger\chi_Y = \chi^\dagger\chi/f_0$ the proper densities agree.
- The interaction enters only through the proper densities (Section 14.26), so self-consistency, the energy and every profile agree as well.

Hence, exactly (for the free gas, with the interaction, at every temperature):

$$
\mathrm{KS}\big(a_{4,0}, b_{4,0};\ H, L, \Delta k, v_t, \lambda\big) = \mathrm{KS}\big(0, 1;\ H/f_0,\ f_0L,\ \Delta k\,e^{-a_{4,0}},\ v_t\,e^{-3a_{4,0}}b_{4,0}^{3/2},\ \lambda\big) .
$$

On the history ($b_{4,0} = e^{(4/3)a_{4,0}}$) the partner has $f_0 = e^{-a_{4,0}/3}$, the constant $He^{a_{4,0}/3}$, the cutoff $Le^{-a_{4,0}/3}$, the spacing $\Delta k\,e^{-a_{4,0}}$ and the extra-time volume $v_te^{-3a_{4,0}}e^{2a_{4,0}} = v_te^{-a_{4,0}}$, at the same coupling. In words (a reading of the record, labelled as such): a later slice of the deflating history is the first slice with a 3-torus larger by $e^{a_{4,0}}$ in each direction, a shorter and more strongly warped hidden direction and a smaller extra-time coordinate volume: the 3-momenta redshift while the hidden direction and the extra times shrink. Status: PROVED; check rescaling_identity (both reports). The Rust solver solved each of the 60 partner problems independently and found the same levels to $1.643\times10^{-13}$ and the same energies and profiles to $8.193\times10^{-13}$, relative (checks rescaling_identity_between_slices and rescaling_identity_energy_profiles of `Revision/kohn_sham/reports/ks-rust-solver.json`; the partner numbers are in `Revision/kohn_sham/results/rescaling/rescaling.csv`). For the slice $a_{4,0} = 0.5$ the partner has $\Delta k\,e^{-0.5} = 0.1516326649$, $v_te^{-0.5} = 0.6065306597$, $He^{1/6} = 1.1813604129$ and $Le^{-1/6} = 2.5394451747$ (Notebook 14a, Out [18]); for $N = 592$ and the coupling $\lambda_1$ the partner of the slice 1 has the Kohn-Sham energy $131.7652$, the energy of the slice itself (`rescaling.csv`, column partner_E_KS).

A second exact statement belongs here, although it is proved in Section 14.27: a Kohn-Sham state depends on the coupling and the volume of the cell only through their ratio. Along the history the proper volume of the cell grows like $e^{(5/3)a_{4,0}}$, so a fixed coupling acts more and more weakly: the slice state at the coupling $\hat\lambda$ is the state of the coordinate cell at the effective coupling $\hat\lambda e^{-(5/3)a_{4,0}}$, at the same $f$ and $\kappa$.

### 14.8 Example: Notebook 14a, the block reduction and the rescaling identity

Notebook 14a repeats Sections 14.2 to 14.7 with exact computer algebra. It reads the author's gammas from the Revision record, checks the Clifford relation and the matrices $C$, $B$, $\Gamma$, verifies the hidden coordinate, the metric in it and the two determinants, computes the canonical spin connection of the metric with $a_4$ and $b_4$ arbitrary functions of the time and shows that $\sum_\mu\gamma^\mu\Omega_\mu = \tfrac32(H/f)\gamma^{(x_0)} + (b_4'/b_4 - \tfrac12a_4')\gamma^{(x_4)}$, with the contribution of every direction; it verifies that the factor $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$ removes the term while each of its two parts alone does not, builds the Hamiltonian, the labels $J, K_1, K_2$, the projectors, the block basis (compared entry by entry with the record) and the block forms, checks the two block types, the matrix $\Gamma$ on the blocks, the rotations and the rescaling identity, and compares the partner parameters with all 60 rows of the Rust record. It draws five figures. It runs in about a minute and a half (two cells do exact algebra with $16 \times 16$ matrices of symbols and two unknown functions of the time, and take about 15 and 40 seconds), and its last line is ALL 31 CHECKS PASSED (notebook 14a).

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
g = [sp.Matrix(m) for m in fixture["gamma"]]  # g[0] = gamma^(x0) ... g[7] = gamma^(x7)
eta = [int(v) for v in fixture["eta"]]  # +1 space-like, -1 time-like
g0, g1, g2, g3, g4, g5, g6, g7 = g  # gN is gamma^(xN)
I16, Z16 = sp.eye(16), sp.zeros(16)  # the 16 x 16 unit and zero matrices
```

The record `Revision/algebra/gammas.json` stores the eight matrices as lists of rows of whole numbers, in the order $x_0, \dots, x_7$. `sp.Matrix(m)` turns each into an exact sympy matrix; `g[0]` is $\gamma^{(x_0)}$ and `g[7]` is $\gamma^{(x_7)}$ (Python counts from 0, like the author's coordinates). `eta` is the list of the eight signs. The third line gives the eight matrices the names `g0` to `g7` (unpacking a list into names), so `gN` is $\gamma^{(x_N)}$. `sp.eye(16)` is the unit matrix and `sp.zeros(16)` the zero matrix.

```python
say(f"eta in the order x0 ... x7: {eta}")
entries = sorted({int(e) for m in g for e in m})  # the different entries
say(f"the entries of the eight gamma matrices are the integers {entries}")
```

The first line prints the signs. The second collects every entry of every matrix into a **set** (braces without colons: a collection in which each value occurs once) and sorts it; the printout shows that the only entries are $-1$, $0$ and $1$: the gammas are real.

```python
clifford = all(g[a] * g[b] + g[b] * g[a] == (2 * eta[a] if a == b else 0) * I16
               for a in range(8) for b in range(8))
check(clifford and eta == [1, 1, 1, 1, -1, -1, -1, -1]
      and record_check("clifford_relation"),
      "the Clifford relation gamma^a gamma^b + gamma^b gamma^a = 2 eta^ab",
      record=f"{PY_REPORT}, check clifford_relation")
```

`range(8)` runs through 0 to 7, so the two `for` clauses visit all 64 pairs $(a, b)$; `all(...)` is true when every comparison is true. For each pair the anticommutator $\gamma^a\gamma^b + \gamma^b\gamma^a$ (the operator `*` multiplies sympy matrices) is compared exactly with $2\eta^{aa}$ times the unit matrix when $a = b$ and with the zero matrix otherwise. The check also requires the signs $\eta = (+,+,+,+,-,-,-,-)$ and the recorded verdict; Out [2] shows its PASS line and the record it reproduces.

**In [3], the matrices C, B and Γ.**

```python
C = g0 * g1 * g2 * g3  # the matrix of the Dirac adjoint
B = -sp.I * C * g4  # the matrix of the positive inner product
Gamma = g0 * g1 * g2 * g3 * g4 * g5 * g6 * g7  # the chirality matrix
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

**In [4], the hidden coordinate, the metric in it and the determinants.**

```python
H = sp.symbols("H", positive=True)  # the author's constant H > 0
y_neg = sp.symbols("y", negative=True)  # the hidden coordinate away from the fold
x0 = sp.symbols("x0", real=True)  # the author's hidden coordinate (every real value)
```

`sp.symbols` makes symbols; the options tell sympy what it may assume: $H > 0$, $y < 0$ (every point of a half except the fold itself) and $x_0$ any real number. With these assumptions sympy can simplify square roots, powers and inverse sines correctly.

```python
z_of_y = sp.asin(sp.exp(6 * H * y_neg))  # z(y) on the first quarter 0 < z < pi/2
dx0_dy = sp.diff(z_of_y / (6 * H), y_neg)  # x0 = z/(6H) differentiated in y
ok_line = sp.simplify(sp.cot(z_of_y) ** 2 * dx0_dy ** 2 - 1) == 0  # cot^2 z dx0^2 = dy^2
```

The first line solves $|\sin z| = e^{6Hy}$ for $z$ with the inverse sine, `sp.asin`, which gives the point of the first half $0 < z < \pi/2$ (the other half has the same $y$ at $\pi - z$, Section 14.2). The second differentiates $x_0 = z/(6H)$ with respect to $y$ (`sp.diff(expression, variable)`). The third checks the second line of the derivation in Section 14.2 in the form $\cot^2 z\,(dx_0/dy)^2 = 1$, which is $\cot^2 z\,dx_0^2 = dy^2$: `sp.simplify` brings the expression to its simplest form, and the comparison `== 0` asks whether it is exactly zero.

```python
ok_warp = sp.simplify((sp.sin(z_of_y) ** 2) ** sp.Rational(1, 6)
                      - sp.exp(2 * H * y_neg)) == 0  # (sin^2 z)^(1/6) = e^(2Hy)
ok_dy = sp.simplify(sp.diff(sp.log(sp.sin(6 * H * x0) ** 2) / (12 * H), x0)
                    - sp.cot(6 * H * x0)) == 0  # dy/dx0 = cot z for every real z
check(ok_line and ok_warp and ok_dy and record_check("geometry_hidden_coordinate"),
      "y = ln|sin z|/(6H): dy = cot z dx0 and (sin^2 z)^(1/6) = e^(2Hy)",
      record=f"{PY_REPORT}, check geometry_hidden_coordinate")
```

`sp.Rational(1, 6)` is the exact fraction $1/6$ (the Python expression `1/6` would be a rounded floating-point number). The first test is the third line of Section 14.2, $(\sin^2 z)^{1/6} = e^{2Hy}$; the second is its first line, $dy/dx_0 = \cot z$, obtained by differentiating the definition in the form $y = \ln(\sin^2 6Hx_0)/(12H)$ for every real $x_0$, so on both halves of every cell. The check combines the three tests with the verdict of the record.

```python
a0 = sp.symbols("a0", real=True)  # the value of a4 at one instant
b0 = sp.symbols("b0", positive=True)  # the value of b4 at that instant
f0 = sp.exp(-a0) * sp.sqrt(b0)  # the hidden scale f = e^(-a4) b4^(1/2)
z = 6 * H * x0
```

At one instant $a_4$ and $b_4$ are two numbers, here the symbols $a_0$ and $b_0 > 0$; `f0` is the hidden scale $f = e^{-a_4}b_4^{1/2}$, and `z` is the expression $6Hx_0$.

```python
metric_x0 = ([sp.exp(-2 * a0) * b0 * sp.cot(z) ** 2] + [sp.exp(2 * a0)] * 3 + [-1]
             + [-sp.exp(-2 * a0) * b0 * (sp.sin(z) ** 2) ** sp.Rational(1, 6)] * 3)
det_x0 = sp.simplify(sp.prod(metric_x0))  # det g in the author's x0 chart
say(f"det g in the x0 chart of the author = {det_x0}")
```

`metric_x0` is the list of the eight diagonal entries of the corrected metric in the author's chart, in the order $x_0, \dots, x_7$ (a list times 3 repeats it three times; `+` joins lists). The determinant of a diagonal matrix is the product of its diagonal entries (`sp.prod`). Out [4] prints `b0**4*exp(-2*a0)*cot(6*H*x0)**2*Abs(sin(6*H*x0))` (`**` is the power): the three 3-space entries give $e^{6a_0}$, the three extra-time entries $-e^{-6a_0}b_0^3|\sin z|$ (each $(\sin^2 z)^{1/6}$ is $|\sin z|^{1/3}$, and three of them give $|\sin z|$), the time entry gives $-1$, and the hidden entry $e^{-2a_0}b_0\cot^2 z$; the two minus signs cancel and $e^{6a_0}e^{-6a_0}e^{-2a_0} = e^{-2a_0}$.

```python
vielbein_y = [f0] + [sp.exp(a0)] * 3 + [1] + [f0 * sp.exp(H * y_neg)] * 3
sqrt_g_y = sp.simplify(sp.prod(vielbein_y))  # sqrt|g| in the y chart
say(f"sqrt|g| in the y chart = {sqrt_g_y}")
```

The eight scale factors of the $y$ chart, $(f, e^{a_4}, e^{a_4}, e^{a_4}, 1, fe^{Hy}, fe^{Hy}, fe^{Hy})$ of Section 14.2, and their product, $\sqrt{|g|}$ in the $y$ chart. Out [4] prints `b0**2*exp(3*H*y - a0)`, which is $e^{-a_4}b_4^2e^{3Hy}$.

```python
ok_x0 = sp.simplify(det_x0 - sp.exp(-2 * a0) * b0 ** 4 * sp.cot(z) ** 2
                    * sp.Abs(sp.sin(z))) == 0
ok_y = sp.simplify(sqrt_g_y - sp.exp(-a0) * b0 ** 2 * sp.exp(3 * H * y_neg)) == 0
check(ok_x0 and ok_y and record_check("geometry_sqrt_det"),
      "det g = e^(-2a4) b4^4 cot^2 z |sin z|; sqrt|g| = e^(-a4) b4^2 e^(3Hy) in y",
      record=f"{PY_REPORT}, check geometry_sqrt_det")
```

The two determinants compared with the formulas of Section 14.2. The square root of the first is $e^{-a_4}b_4^2|\cot z|\,|\sin z|^{1/2} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$; the two charts differ by the factor $|\cot z| = |dy/dx_0|$.

```python
ok_g00 = sp.simplify(f0 ** 2 / dx0_dy ** 2
                     - sp.exp(-2 * a0) * b0 * sp.cot(z_of_y) ** 2) == 0
ok_gtt = sp.simplify(f0 ** 2 * sp.exp(2 * H * y_neg) - sp.exp(-2 * a0) * b0
                     * (sp.sin(z_of_y) ** 2) ** sp.Rational(1, 6)) == 0
check(ok_g00 and ok_gtt and record_check("geometry_line_element"),
      "f^2 dy^2 and -f^2 e^(2Hy) dx_t^2 are the hidden and extra-time entries",
      record=f"{PY_REPORT}, check geometry_line_element")
```

The metric in the $y$ chart: the hidden entry $f^2dy^2$ is $g_{00}dx_0^2$ (the entry $f^2$ for $dy$ equals $g_{00}$ times $(dx_0/dy)^2$, which is the test `ok_g00` divided by that square), and the extra-time entry $-f^2e^{2Hy}$ equals the author's $-e^{-2a_4}b_4(\sin^2 z)^{1/6}$ (test `ok_gtt`). Out [4] shows the three PASS lines.

**In [5], figure 1.**

```python
z_cell = np.linspace(1e-3, np.pi - 1e-3, 1201)  # one cell 0 < z < pi
y_of_z = np.log(np.abs(np.sin(z_cell))) / 6.0  # y = ln|sin z|/(6H) with H = 1
y_values = np.linspace(-3.0, 0.0, 301)  # the hidden coordinate from -L to 0
```

`np.linspace(start, stop, count)` makes `count` equally spaced numbers from `start` to `stop`; `1e-3` means $10^{-3}$ (the end points $z = 0$ and $z = \pi$ themselves would give $\ln 0$). numpy applies `np.log`, `np.abs` and `np.sin` to every number of an array at once. The first line covers one whole cell, both halves; the third line is the hidden coordinate from the cutoff $-L = -3$ of the Revision solver to the fold.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.axvspan(0.0, np.pi / 2, color="C0", alpha=0.08)  # the first half
left.axvspan(np.pi / 2, np.pi, color="C1", alpha=0.08)  # the second half
left.plot(z_cell, y_of_z, color="C0")
left.axvline(np.pi / 2, color="gray", linestyle="--", linewidth=0.8)
```

`plt.subplots(1, 2, ...)` makes a figure with one row of two panels (called **axes** in matplotlib), named `left` and `right`, 10 by 4 inches. `axvspan(a, b, ...)` shades the vertical strip from $a$ to $b$ (here the two halves, in two faint colours: `alpha=0.08` means 8 per cent opaque; `"C0"` and `"C1"` are the first two colours of matplotlib's standard list). `plot(x, y)` draws the curve, and `axvline` a dashed vertical line at the fold $z = \pi/2$.

```python
left.set_xlabel("$z = 6 H x_0$ (radians), one cell $0 < z < \\pi$")
left.set_ylabel("$y = \\ln|\\sin z|/(6H)$")
left.set_title("the hidden coordinate on the two halves ($H = 1$)")
left.annotate("tip", (0.05, -1.05), fontsize=9)
left.annotate("tip", (2.85, -1.05), fontsize=9)
left.annotate("fold: $y = 0$", (1.62, -0.12), fontsize=9)
left.annotate("half $z < \\pi/2$", (0.35, -0.55), fontsize=8)
left.annotate("half $z > \\pi/2$", (1.85, -0.55), fontsize=8)
```

The labels are written in LaTeX between dollar signs, with a doubled backslash because a single backslash starts a special character in a Python string. `annotate(text, (x, y))` writes a text at a point of the panel: the two tips, the fold and the two halves.

```python
right.semilogy(y_values, np.exp(y_values), label="warp of the extra times $e^{Hy}$")
right.semilogy(y_values, np.exp(2 * y_values), "--",
               label="$(\\sin^2 z)^{1/6} = e^{2Hy}$")
right.semilogy(y_values, np.exp(3 * y_values), ":",
               label="volume factor $e^{3Hy}$ of $\\sqrt{|g|}$")
right.set_xlabel("$y$ (units of $1/H$)")
right.set_ylabel("factor (logarithmic scale)")
right.set_title("the factors of the metric in the $y$ chart")
right.legend(fontsize=8)
```

`semilogy` draws with a **logarithmic vertical axis**: equal distances mean equal factors (each labelled tick is ten times the one below). On such an axis an exponential $e^{cy}$ is a straight line of slope $c$. The three curves are $e^{y}$, $e^{2y}$ and $e^{3y}$ with $H = 1$; the third argument of `semilogy`, a short text called a **format string**, sets the line style: two hyphens draw a dashed line and a colon a dotted one (the plain `plot` lines of this book use the same format strings); `legend` shows the `label` texts in a box.

```python
save_figure(fig, "hidden_coordinate",
            "Left: the hidden coordinate $y = \\ln|\\sin z|/(6H)$ against "
            ...)
```

The figure is saved as `14a_1_hidden_coordinate.png` with its caption (the long caption, printed under the figure in Section 14.10, is shortened here to `...`). **What figure 14a.1 shows.** Left: $y$ over one cell; the curve is symmetric about the fold, where it reaches its largest value $0$ with zero slope (because $dy/dz = \cot z/(6H)$ vanishes at $z = \pi/2$), and it drops steeply toward both tips (the plot stops at $z = 10^{-3}$ and $\pi - 10^{-3}$, where $y = -1.15$). The two shaded halves carry the same values of $y$: one coordinate describes both. Right: three straight lines with the slopes 1, 2 and 3 on the logarithmic axis; all equal 1 at the fold, and at the cutoff $y = -3$ the volume factor is $e^{-9} \approx 1.2\times10^{-4}$. This small proper volume near the tip is why the proper densities of Notebook 14d grow toward the tip.

**In [6], figure 2.**

```python
a4_values = np.linspace(0.0, 2.0, 201)  # a4 along the history (= x4 for A = H = 1)
b4_values = np.exp(4.0 * a4_values / 3.0)  # b4 = b4(0) e^((4/3) a4) with b4(0) = 1
slices = [0.0, 0.5, 1.0, 1.5, 2.0]  # the five slices of the Revision solver
```

The values of $a_4$ from 0 to 2 (along the history $a_4 = AHx_4$ with $A = H = 1$ these are also the times $x_4$), the values of $b_4 = e^{(4/3)a_4}$ on the history, and the five slices of the Revision runs.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
left.semilogy(a4_values, np.exp(a4_values), label="3-space: $e^{a_4}$ (inflates)")
left.semilogy(a4_values, np.exp(-a4_values) * np.sqrt(b4_values), "--",
              label="extra times at the fold and hidden scale $f$")
left.semilogy(a4_values, np.exp(-a4_values), "-.",
              label="momentum weight $\\kappa = e^{-a_4}$")
left.semilogy(a4_values, np.exp(-a4_values) * b4_values ** 2, ":", color="black",
              label="cell 7-volume $e^{-a_4} b_4^2$")
left.set_xlabel("$a_4 = A H x_4$ (with $A = H = 1$: the time $x_4$)")
left.set_ylabel("factor (logarithmic scale)")
left.set_title("inflation and deflation along the history")
left.legend(fontsize=7)
```

The left panel draws four factors along the history on a logarithmic axis: the 3-space scale factor $e^{a_4}$; $e^{-a_4}b_4^{1/2}$, which is both the scale factor of the extra times at the fold ($e^{Hy} = 1$ there) and the hidden scale $f$; the momentum weight $\kappa = e^{-a_4}$ (the format string `"-."` draws a dash-dotted line); and the factor $e^{-a_4}b_4^2$ of the proper 7-volume of a coordinate cell ($\sqrt{|g|}$ without $e^{3Hy}$).

```python
for index, a in enumerate(slices):  # one colour per slice
    f_a = np.exp(-a / 3.0)  # the hidden scale on the history
    right.semilogy(y_values, f_a * np.exp(y_values), color=f"C{index}",
                   label=f"$a_{{4,0}} = {a}$")
    right.semilogy(y_values, np.full_like(y_values, np.exp(-a)), ":",
                   color=f"C{index}")
```

`enumerate` hands out each slice together with its position 0 to 4, which picks the colour `C0` to `C4`. For each slice the loop draws the extra-time scale factor $fe^{Hy}$ with $f = e^{-a/3}$ (solid) and the momentum weight $\kappa = e^{-a}$ as a horizontal dotted line (`np.full_like(y_values, value)` is an array of the same length filled with one value). In an f-string a doubled brace `{{` prints one brace, so the label reads $a_{4,0} = 0.5$ and so on.

```python
right.set_xlabel("$y$ (units of $1/H$)")
right.set_ylabel("factor (logarithmic scale)")
right.set_title("$f e^{Hy}$ (solid) and $\\kappa$ (dotted) at five slices")
right.legend(fontsize=7)
save_figure(fig, "inflation_deflation",
            ...)
```

**What figure 14a.2 shows.** Left: four straight lines from the common value 1: $e^{a_4}$ grows to $e^2 \approx 7.4$ (slope 1); $f = e^{-a_4/3}$ falls to $e^{-2/3} \approx 0.51$ (slope $-1/3$); $\kappa = e^{-a_4}$ falls faster, to $e^{-2} \approx 0.14$; and the cell volume $e^{(5/3)a_4}$ grows to $e^{10/3} \approx 28$. Inflation of 3-space wins over the deflation of the hidden direction and the extra times: the proper 7-volume of a coordinate cell grows. Right: five parallel solid lines of slope 1 (the warp $e^{Hy}$ of the extra times), each later slice lower by the factor $e^{-1/6}$, and five horizontal dotted lines, each lower by $e^{-1/2}$: the momentum weight does not depend on $y$.

**In [7], the spin connection.** This cell carries out Steps 1 to 4 of Section 14.4 with sympy, with $a_4$ and $b_4$ unknown functions of the time.

```python
X = (sp.Symbol("y", real=True),) + sp.symbols("x1:8", real=True)  # y, x1..x7
Y, x4 = X[0], X[4]  # the hidden coordinate and the time
a4 = sp.Function("a4", real=True)(x4)  # a4 is any function of the time x4
b4 = sp.Function("b4", positive=True)(x4)  # b4 > 0 is any function of x4
a4p, b4p = sp.diff(a4, x4), sp.diff(b4, x4)  # their derivatives a4' and b4'
```

`sp.symbols("x1:8")` makes the seven symbols $x_1, \dots, x_7$; a one-element **tuple** (a list in round brackets) with the symbol $y$ put in front of them gives the eight coordinates, with $y$ in the place of $x_0$ (position 0), so `X[k]` is $x_k$ for $k \ge 1$. `sp.Function("a4")(x4)` is an unknown function $a_4(x_4)$ and `sp.Function("b4", positive=True)(x4)` an unknown positive function $b_4(x_4)$, so everything below holds along every history; `a4p` and `b4p` are their derivatives $a_4'$ and $b_4'$.

```python
f = sp.exp(-a4) * sp.sqrt(b4)  # the hidden scale
W = sp.exp(H * Y)  # the warp of the extra times
vb = [f] + [sp.exp(a4)] * 3 + [sp.Integer(1)] + [f * W] * 3  # the scale factors
gdiag = [eta[i] * vb[i] ** 2 for i in range(8)]  # the diagonal metric entries
```

`f` is the hidden scale, now a function of the time, and `W` the warp $e^{Hy}$. `vb` is the list of the eight scale factors $h$ of Section 14.2 in the order $(y, x_1, \dots, x_7)$ (`sp.Integer(1)` is the exact number 1), and `gdiag` the metric entries $\eta_{ii}h_i^2$, which reproduce the metric in the $y$ chart.

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

For each direction $\mu$ the double loop over the frame indices $A$ and $B$ (`Bi`, because `B` is the matrix $B$) computes the connection coefficient $\omega_\mu{}^A{}_B$ of Step 2 (a backslash at the end of a line continues the statement on the next line; `x if c else y` is `x` when `c` holds and `y` otherwise) and adds $\tfrac12\eta_{AA}\,\omega_\mu{}^A{}_B\,S^{AB}$ to the matrix $\Omega_\mu$ (Step 3); terms with a zero coefficient are skipped to save time. `append` puts the finished $\Omega_\mu$ at the end of the list.

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

The proof that $\Omega_\mu$ is the right connection: the **curved gammas** $\gamma^\nu = \gamma^{(\nu)}/h_\nu$ must be **covariantly constant**, $\partial_\mu\gamma^\nu + \Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$, for all 64 pairs $(\mu, \nu)$, where $[X, Y] = XY - YX$ is the **commutator**. `sum(..., Z16)` adds $16 \times 16$ matrices starting from the zero matrix; `applyfunc(sp.simplify)` simplifies every entry; `.is_zero_matrix` is true when every entry is 0.

```python
slash = sp.simplify(sum((g[m] / vb[m] * Omega[m] for m in range(8)), Z16))
c_x0 = sp.Rational(3, 2) * H / f  # the coefficient of gamma^(x0)
c_x4 = b4p / b4 - a4p / 2  # the coefficient of gamma^(x4)
check((slash - c_x0 * g0 - c_x4 * g4).applyfunc(sp.simplify).is_zero_matrix
      and record_check("spin_connection_slash"),
      "gamma^mu Omega_mu = (3/2)(H/f) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4)",
      record=f"{PY_REPORT}, check spin_connection_slash")
```

The sum $\sum_\mu\gamma^\mu\Omega_\mu$ (often written with a slash through $\Omega$, hence the name), compared with $\tfrac32(H/f)\gamma^{(x_0)} + (b_4'/b_4 - \tfrac12a_4')\gamma^{(x_4)}$, the result of Section 14.4; the two coefficients are kept as `c_x0` and `c_x4` for In [8] and In [10]. Out [7] shows the two PASS lines. This cell takes about 15 seconds.

**In [8], what each direction contributes.**

```python
names = ["x0 (y)", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
A4P, B4P = sp.symbols("a4p b4p")  # names for a4' and b4' in the printout
c4_list, c0_list = [], []  # the coefficients of gamma^(x4) and gamma^(x0)
split_ok = True
```

Names for the printout, two symbols that stand for $a_4'$ and $b_4'$ when they are printed (sympy would otherwise print the long form `Derivative(a4(x4), x4)`), two empty lists and a flag that starts true.

```python
for m in range(8):
    part = sp.simplify(g[m] / vb[m] * Omega[m])  # the contribution of direction m
    c4 = sp.simplify(-(part * g4).trace() / 16)
    c0 = sp.simplify((part * g0).trace() / 16)
    split_ok &= (part - c4 * g4 - c0 * g0).applyfunc(sp.simplify).is_zero_matrix
    c4_list.append(c4)
    c0_list.append(c0)
    shown_c4 = str(c4.subs({a4p: A4P, b4p: B4P}))  # write a4p, b4p for a4', b4'
    say(f"direction {names[m]:7}: c4 = {shown_c4:24} c0 = {c0}")
check(split_ok, "every contribution is c4 gamma^(x4) + c0 gamma^(x0)")
```

For each direction the contribution $X = (\gamma^{(\mu)}/h_\mu)\Omega_\mu$ of Step 4. If $X = c_4\gamma^{(x_4)} + c_0\gamma^{(x_0)}$, then $X\gamma^{(x_4)} = -c_4 + c_0\gamma^{(x_0)}\gamma^{(x_4)}$, and since the **trace** (the sum of the diagonal entries) of the unit matrix is 16 and that of a product of two different gammas is 0, $\mathrm{tr}(X\gamma^{(x_4)}) = -16c_4$; in the same way $\mathrm{tr}(X\gamma^{(x_0)}) = 16c_0$. These are the second and third lines of the loop. The fourth line checks that $X$ is exactly $c_4\gamma^{(x_4)} + c_0\gamma^{(x_0)}$ (`&=` keeps the flag true only if every direction passes). `subs({...})` replaces the two derivatives by the printable names, and the formats `:7` and `:24` pad the texts to 7 and 24 characters, so that the printout forms columns. Out [8] shows, with `a4p` for $a_4'$ and `b4p` for $b_4'$: for $y$ and for each extra time $c_4 = -a_4'/2 + b_4'/(4b_4) = \tfrac12h_4$; for $x_1, x_2, x_3$ $c_4 = a_4'/2$; for $x_4$ nothing; and $c_0 = He^{a_4}/(2\sqrt{b_4}) = H/(2f)$ for each extra time and 0 for every other direction. These are exactly the four cases of Step 5 of Section 14.4.

```python
h4 = b4p / (2 * b4) - a4p  # the rate of the hidden scale, f'/f
terms_ok = (sp.simplify(c4_list[0] - h4 / 2) == 0 and c0_list[0] == 0
            and sp.simplify(sum(c4_list[1:4]) - sp.Rational(3, 2) * a4p) == 0
            and sp.simplify(sum(c4_list[5:8]) - sp.Rational(3, 2) * h4) == 0
            and sp.simplify(sum(c0_list[5:8]) - c_x0) == 0
            and Omega[4].is_zero_matrix and not Omega[0].is_zero_matrix)
check(terms_ok and record_check("spin_connection_time_terms"),
      "hidden h4/2, 3-space 3a4'/2, extra times 3h4/2 and (3/2)H/f; Omega_x4 = 0",
      record=f"{PY_REPORT}, check spin_connection_time_terms")
```

The facts of the record: with $h_4 = b_4'/(2b_4) - a_4'$, the hidden direction (position 0) gives $\tfrac12h_4\gamma^{(x_4)}$ and nothing along $\gamma^{(x_0)}$; the three 3-space directions together (`c4_list[1:4]`, the part of the list from position 1 up to, but not including, position 4) give $\tfrac32a_4'\gamma^{(x_4)}$; the three extra times (positions 5 to 7) give $\tfrac32h_4\gamma^{(x_4)}$ and $\tfrac32(H/f)\gamma^{(x_0)}$; $\Omega_{x_4} = 0$; and $\Omega_y$ is NOT zero (`not ... is_zero_matrix`), because the scale factor $f$ of $y$ depends on the time.

**In [9], figure 3.**

```python
on_history = {a4p: 1, b4p: sp.Rational(4, 3) * b4}  # a4' = 1, b4'/b4 = 4/3
at_first_slice = {a4: 0, b4: 1, H: 1}  # a4 = 0, b4 = 1, H = 1: f = 1
c4_numbers = [float(c.subs(on_history).subs(at_first_slice)) for c in c4_list]
c0_numbers = [float(c.subs(on_history).subs(at_first_slice)) for c in c0_list]
say("c4 on the history at the first slice: "
    + ", ".join(f"{c:+.4f}" for c in c4_numbers))
say("c0 on the history at the first slice: "
    + ", ".join(f"{c:+.4f}" for c in c0_numbers))
positions = np.arange(8)  # one group of two bars per direction
```

Two dictionaries of substitutions: on the history $a_4' = AH = 1$ and $b_4' = \tfrac43b_4$; at the first slice $a_4 = 0$, $b_4 = 1$, $H = 1$, so $f = 1$ and $h_4 = \tfrac23 - 1 = -\tfrac13$. The derivatives are replaced first (the order matters: replacing $b_4$ by 1 first would make $b_4'$ the derivative of a number). `float` turns each exact number into a floating-point one, and `", ".join(...)` joins the formatted numbers (`:+.4f`: a sign and four decimals) with commas. Out [9] prints the coefficients of $\gamma^{(x_4)}$ as -0.1667, +0.5000, +0.5000, +0.5000, +0.0000, -0.1667, -0.1667, -0.1667 and those of $\gamma^{(x_0)}$ as +0.0000 for the first five directions and +0.5000 for the three extra times. `np.arange(8)` is the array 0, 1, ..., 7, one position per direction.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.0))
ax.bar(positions - 0.2, c4_numbers, width=0.38,
       label="coefficient of $\\gamma^{(x_4)}$")
ax.bar(positions + 0.2, c0_numbers, width=0.38,
       label="coefficient of $\\gamma^{(x_0)}$")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xticks(positions)
ax.set_xticklabels(["$x_0$", "$x_1$", "$x_2$", "$x_3$", "$x_4$", "$x_5$", "$x_6$",
                    "$x_7$"])
```

`bar(x, heights, width=...)` draws bars; the two sets are shifted by $-0.2$ and $+0.2$ so that they stand side by side. `axhline` draws the horizontal line at 0; `set_xticks` and `set_xticklabels` put the names of the directions under the groups.

```python
ax.set_xlabel("direction $\\mu$ of the term $(\\gamma^{(\\mu)}/h_\\mu)\\,"
              "\\Omega_\\mu$")
ax.set_ylabel("coefficient (units of $H$)")
ax.set_title("$\\gamma^\\mu\\Omega_\\mu$ on the history at the first slice: "
             "$\\frac{3}{2}\\gamma^{(x_0)} + \\frac{5}{6}\\gamma^{(x_4)}$")
ax.legend(fontsize=8)
save_figure(fig, "spin_connection_terms",
            ...)
```

Labels, title, legend and saving. **What figure 14a.3 shows.** Above $x_0$ one bar of $-\tfrac16$ (the hidden direction deflates: $\tfrac12h_4$); above $x_1$, $x_2$, $x_3$ bars of $+\tfrac12$ (3-space inflates: $\tfrac12a_4'$); nothing above $x_4$; above each extra time a bar of $-\tfrac16$ for $\gamma^{(x_4)}$ and one of $+\tfrac12$ for $\gamma^{(x_0)}$ (the warp: $H/(2f)$). The blue bars add up to $-\tfrac16 + \tfrac32 - \tfrac12 = \tfrac56$ and the orange ones to $\tfrac32$: the title's $\tfrac32\gamma^{(x_0)} + \tfrac56\gamma^{(x_4)}$.

**In [10], the factor that removes the spin connection.**

```python
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)  # the 3-momentum
chi = sp.Matrix([sp.Function(f"chi{i}")(Y, x4) for i in range(16)])
phase = sp.exp(sp.I * (k1 * X[1] + k2 * X[2] + k3 * X[3]))  # the plane wave
kappa = sp.exp(-a4)  # the momentum weight (no y in it)
factor_y = sp.exp(-sp.Rational(3, 2) * H * Y)  # removes (3/2)(H/f) gamma^(x0)
factor_t = sp.exp(a4 / 2) / b4  # removes (b4'/b4 - a4'/2) gamma^(x4)
```

The three components of $\mathbf k$; a column `chi` of 16 unknown functions $\chi_0(y, x_4), \dots, \chi_{15}(y, x_4)$; the plane wave $e^{i\mathbf k\cdot\mathbf x}$; the weight $\kappa = e^{-a_4(x_4)}$; and the two parts of the factor $F$ of Step 6, $e^{-(3/2)Hy}$ and $e^{a_4/2}b_4^{-1}$.

```python
def dirac(Psi):
    result = sp.zeros(16, 1)
    for m in range(8):
        result += g[m] / vb[m] * (sp.diff(Psi, X[m]) + Omega[m] * Psi)
    return result
```

The Dirac operator $\gamma^\mu D_\mu\Psi = \sum_\mu(\gamma^{(\mu)}/h_\mu)(\partial_\mu\Psi + \Omega_\mu\Psi)$ with the spin connection of In [7]; `sp.zeros(16, 1)` is a zero column.

```python
reduced = (g0 * sp.diff(chi, Y) / f + g4 * sp.diff(chi, x4)
           + sp.I * kappa * (k1 * g1 + k2 * g2 + k3 * g3) * chi)
both = sp.simplify(dirac(phase * factor_y * factor_t * chi)
                   / (phase * factor_y * factor_t))
check((both - reduced).applyfunc(sp.simplify).is_zero_matrix
      and record_check("ansatz_removes_spin_connection"),
      "with both factors: (1/f) g0 d_y + g4 d_x4 + i kappa k.g, exactly",
      record=f"{PY_REPORT}, check ansatz_removes_spin_connection")
```

`reduced` is the reduced operator of Step 6 of Section 14.4 applied to $\chi$, $\tfrac1f\gamma^{(x_0)}\partial_y\chi + \gamma^{(x_4)}\partial_{x_4}\chi + i\kappa k_j\gamma^{(x_j)}\chi$. `both` applies the full Dirac operator to $e^{i\mathbf k\cdot\mathbf x}F\chi$ and divides by the common factor. The check: the two are equal, exactly, for every history.

```python
no_y = sp.simplify(dirac(phase * factor_t * chi) / (phase * factor_t))
check((no_y - reduced - c_x0 * g0 * chi).applyfunc(sp.simplify).is_zero_matrix
      and record_check("ansatz_without_y_factor_term_survives"),
      "without exp(-3Hy/2) the term (3/2)(H/f) gamma^(x0) chi survives",
      record=f"{PY_REPORT}, check ansatz_without_y_factor_term_survives")
no_t = sp.simplify(dirac(phase * factor_y * chi) / (phase * factor_y))
check((no_t - reduced - c_x4 * g4 * chi).applyfunc(sp.simplify).is_zero_matrix
      and record_check("ansatz_without_x4_factor_term_survives"),
      "without exp(a4/2)/b4 the term (b4'/b4 - a4'/2) gamma^(x4) chi survives",
      record=f"{PY_REPORT}, check ansatz_without_x4_factor_term_survives")
```

Two negative controls: with only the time part of the factor, the difference from the reduced operator is exactly the term `c_x0` $\gamma^{(x_0)}\chi = \tfrac32(H/f)\gamma^{(x_0)}\chi$; with only the $y$ part, it is exactly `c_x4` $\gamma^{(x_4)}\chi = (b_4'/b_4 - \tfrac12a_4')\gamma^{(x_4)}\chi$. Each part of $F$ removes one term and only that one.

```python
sqrt_g = sp.exp(-a4) * b4 ** 2 * sp.exp(3 * H * Y)  # sqrt|g| in the y chart
check(sp.simplify(sqrt_g * (factor_y * factor_t) ** 2 - 1) == 0
      and record_check("ansatz_norm"),
      "sqrt|g| times the square of the factor is 1: the norm is int chi^dag chi dy",
      record=f"{PY_REPORT}, check ansatz_norm")
```

The half-density property: $F^2\sqrt{|g|} = 1$, so the norm of $\Psi$ over the hidden direction is $\int\chi^\dagger\chi\,dy$. Out [10] shows the four PASS lines; the cell takes about 40 seconds.

**In [11], the Hamiltonian and its Hermitian pieces.**

```python
M, v = sp.symbols("M v", real=True)  # effective mass and vector potential
fs, kap = sp.symbols("f kappa", positive=True)  # the hidden scale, kappa at a point
chi_s = sp.Matrix(sp.symbols("c0:16"))  # chi at one point (16 symbols)
dchi_s = sp.Matrix(sp.symbols("d0:16"))  # d chi/dy at that point
kg = kap * (k1 * g1 + k2 * g2 + k3 * g3)  # kappa k.gamma
```

The derivation of Step 7 is pure algebra at one point, so $\chi$ and $\chi'$ are replaced by two columns of 16 independent symbols (`sp.symbols("c0:16")` makes $c_0, \dots, c_{15}$), and $f$ and $\kappa$ by positive symbols (`fs`, because `f` is the function of In [7]).

```python
# lines 1 and 2: d chi/dx4 = -g4 [(M - i v g4) chi - g0 chi'/f - i kappa k.g chi]
dt_chi = -g4 * ((M * I16 - sp.I * v * g4) * chi_s - g0 * dchi_s / fs
                - sp.I * kg * chi_s)
# line 3: h chi with the four pieces of h
h_chi = (sp.I / fs * g4 * g0 * dchi_s - kap * g4 * (k1 * g1 + k2 * g2 + k3 * g3)
         * chi_s + M * (-sp.I * g4) * chi_s + v * chi_s)
check((sp.I * dt_chi - h_chi).expand().is_zero_matrix,
      "i d_x4 chi = h chi, h = (i/f) g4 g0 d_y - kappa k_j g4 g_j + M(-i g4) + v")
```

The two comment lines name the lines of Step 7 that the statement below each writes out. `dt_chi` is $\partial_{x_4}\chi$ from the first two lines (move the terms, multiply by $-\gamma^{(x_4)}$); `h_chi` is $h\chi$ with the four pieces of the third line. The check confirms $i\,\partial_{x_4}\chi = h\chi$ after multiplying out (`expand`).

```python
hermitian = ((g4 * g0).T == g4 * g0 and all((-g4 * gj).H == -g4 * gj
                                            for gj in (g1, g2, g3))
             and (-sp.I * g4).H == -sp.I * g4 and (-sp.I * g4) ** 2 == I16)
check(hermitian and record_check("hamiltonian_16_hermitian"),
      "g4 g0 real symmetric; g4 g_j and -i g4 Hermitian; (-i g4)^2 = 1",
      record=f"{PY_REPORT}, check hamiltonian_16_hermitian")
```

The Hermitian pieces of Section 14.4: $\gamma^{(x_4)}\gamma^{(x_0)}$ symmetric, $-\gamma^{(x_4)}\gamma^{(x_j)}$ Hermitian for the three 3-space directions, $-i\gamma^{(x_4)}$ Hermitian with square 1.

**In [12], the labels J, K1, K2 and the projectors.**

```python
A0, A1, A4 = g0, g0 * g1, g0 * g4  # the matrices of the equation (k along x1)
J, K1, K2 = g0 * g1 * g4, g2 * g3, g5 * g6
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
    P_plus = P * (I16 + g0) / 2  # project on gamma^(x0) = +1 inside the block
    c = next(c for c in range(16) if not P_plus[:, c].is_zero_matrix)
    seeds.append(c)
    v_plus = 8 * P_plus[:, c]
    columns += [v_plus, A1 * v_plus]  # v+ and v- = A1 v+
```

For each block: `P_plus` projects onto the block and onto $\gamma^{(x_0)} = +1$. Its columns are the images of the unit columns $e_c$ (`P_plus[:, c]` is column $c$). `next(...)` returns the first $c$ whose column is not zero, the **seed**. Then $v_+ = 8\,P_+e_c$, and both $v_+$ and $v_- = A_1v_+$ are added to the list (`+=` appends a list to a list).

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
    ("gamma^(x0)", g0, lambda j, a, b: s3, "sigma3"),
    ("gamma^(x0) gamma^(x1)", A1, lambda j, a, b: -sp.I * s2m, "-i sigma2"),
    ("gamma^(x0) gamma^(x4)", A4, lambda j, a, b: j * s1, "j sigma1"),
    ("B", B, lambda j, a, b: j * a * I2, "j s2"),
    ("C", C, lambda j, a, b: a * s2m, "s2 sigma2"),
    ("BC = -i gamma^(x4)", B * C, lambda j, a, b: j * s2m, "j sigma2"),
    ("gamma^(x4) gamma^(x1)", g4 * g1, lambda j, a, b: -j * s3, "-j sigma3"),
    ("B gamma^(x0)", B * g0, lambda j, a, b: j * a * s3, "j s2 sigma3"),
    ("J", J, lambda j, a, b: j * I2, "j"),
    ("K1", K1, lambda j, a, b: sp.I * a * I2, "i s2"),
    ("K2", K2, lambda j, a, b: sp.I * b * I2, "i s3"),
]
```

A list of eleven entries, one per line: the name, the matrix, its expected block form and the text to print. A `lambda` is a short nameless function: `lambda j, a, b: j * s1` returns $j\sigma_1$ for the labels $(j, s_2, s_3) = (j, a, b)$; so the name `a` stands for $s_2$ and `b` for $s_3$ inside these lines (they are not the real-form components of Section 14.12). Line by line the expected forms are: $\gamma^{(x_0)} \to \sigma_3$; $A_1 \to -i\sigma_2$; $A_4 \to j\sigma_1$; $B \to js_2$ times the $2 \times 2$ unit matrix `I2`; $C \to s_2\sigma_2$; $BC \to j\sigma_2$; $\gamma^{(x_4)}\gamma^{(x_1)} \to -j\sigma_3$; $B\gamma^{(x_0)} \to js_2\sigma_3$; $J \to j$; $K_1 \to is_2$; $K_2 \to is_3$. These are the eleven forms of Section 14.5; the two not derived there follow from them: $BC = (js_2)(s_2\sigma_2) = j\sigma_2$ because $s_2^2 = 1$, and $B\gamma^{(x_0)} = (js_2)\sigma_3$.

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

For each matrix: block diagonal, and in block $i$ equal to the expected form at the labels of that block (`form(*labels[i])` hands the three labels over as separate arguments). Out [14] prints True for all eleven.

```python
not_diagonal = (not blocks_of(g2)[1] and not blocks_of(g5)[1]
                and not blocks_of(g0 * g2)[1] and blocks_of(g1)[1])
check(not_diagonal and record_check("blocks_not_everything_block_diagonal"),
      "gamma^(x2), gamma^(x5), gamma^(x0)gamma^(x2) connect blocks; gamma^(x1) not",
      record=f"{PY_REPORT}, check blocks_not_everything_block_diagonal")
```

`blocks_of(X)[1]` is the second returned value, the yes-or-no answer. $\gamma^{(x_2)}$, $\gamma^{(x_5)}$ and $\gamma^{(x_0)}\gamma^{(x_2)}$ are not block diagonal; $\gamma^{(x_1)}$ is.

**In [15], figure 4.**

```python
N16 = (1 * g0 + sp.I * sp.Rational(1, 2) * g0 * g4
       - sp.I * sp.Rational(7, 10) * g0 * g1)  # M = 1, eps = 1/2, v = 0, kappa k = 7/10
```

The first-order matrix of the stationary equation in 16 components, $N_{16} = M\gamma^{(x_0)} + i(\varepsilon - v)\gamma^{(x_0)}\gamma^{(x_4)} - i\kappa k\,\gamma^{(x_0)}\gamma^{(x_1)}$, at sample values. (It comes from the reduced equation of Step 6 of Section 14.4 with $\partial_{x_4}\chi = -i\varepsilon\chi$ and $\mathbf k = (k, 0, 0)$, multiplied from the left by $f\gamma^{(x_0)}$, so that $\chi' = fN_{16}\chi$.) With the block forms it becomes $N = M\sigma_3 - \kappa k\sigma_2 + ij(\varepsilon - v)\sigma_1$ in every block.

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

In the second and third panels thin gray lines are drawn between rows and columns 1 and 2, 3 and 4, and so on (`np.arange(1.5, 15.0, 2.0)` is 1.5, 3.5, ..., 13.5), which frame the eight blocks. **What figure 14a.4 shows.** Left: in the original basis the entries of $N_{16}$ are spread over the whole matrix in a diamond pattern. Middle: in the block basis only the eight $2 \times 2$ blocks on the diagonal are nonzero. In every block the diagonal entries are $\pm M$ (size 1) and the two off-diagonal entries are $i(\kappa k + j\varepsilon)$ and $i(j\varepsilon - \kappa k)$, of the sizes $1.2$ and $0.2$ for $j = +1$; in the first four blocks ($j = +1$) the large one is above the diagonal, in the last four ($j = -1$) below it: the two block types are visible. Right: $V^\dagger\Gamma V$ has entries of size 1 only between the block $b$ and the block $b \pm 4$, the pairs $(j, s_2, s_3) \leftrightarrow (-j, s_2, s_3)$.

**In [16], the block Hamiltonian, its two types and Γ.**

```python
ok_h = True
for i, (j, a, b) in enumerate(labels):  # the three pieces of h in block i
    Vb = V[:, 2 * i:2 * i + 2]
    ok_h &= sp.simplify(Vb.H * (sp.I * g4 * g0) * Vb + sp.I * j * s1).is_zero_matrix
    ok_h &= sp.simplify(Vb.H * (-g4 * g1) * Vb - j * s3).is_zero_matrix
    ok_h &= sp.simplify(Vb.H * (-sp.I * g4) * Vb - j * s2m).is_zero_matrix
check(ok_h and record_check("block_hamiltonian"),
      "h_j = j[-(i/f) sigma1 d/dy + M sigma2 + kappa k sigma3] + v in all 8 blocks",
      record=f"{PY_REPORT}, check block_hamiltonian")
```

`enumerate` gives each block its number `i` together with its labels. `Vb` holds the two basis columns of the block. The three lines check the three matrix pieces of $h$ (with $\mathbf k$ along $x_1$): $i\gamma^{(x_4)}\gamma^{(x_0)} \to -ij\sigma_1$, $-\gamma^{(x_4)}\gamma^{(x_1)} \to j\sigma_3$, $-i\gamma^{(x_4)} \to j\sigma_2$. With the numbers $1/f$, $\kappa k$ and $M$ in front of them they give $h_j$.

```python
eps = sp.symbols("epsilon", real=True)  # the level

def h_algebraic(j, M_, k_, kap_):
    return j * (M_ * s2m + kap_ * k_ * s3)

def N_matrix(j, M_, k_, eps_, v_, kap_):
    return M_ * s3 - kap_ * k_ * s2m + sp.I * j * (eps_ - v_) * s1
```

The level $\varepsilon$ as a symbol; `h_algebraic` is the part of $h_j - v$ without the derivative, $j(M\sigma_2 + \kappa k\sigma_3)$; `N_matrix` is the matrix $N$ of the first-order form $\chi' = fN\chi$.

```python
kk = sp.symbols("k", real=True)
# h chi = eps chi  <=>  -(i j/f) sigma1 chi' = (eps - v - j(M s2 + kappa k s3)) chi
ok_ode = all(sp.simplify(-sp.I * j / fs * s1 * (fs * N_matrix(j, M, kk, eps, v, kap))
                         - ((eps - v) * I2 - h_algebraic(j, M, kk, kap)))
             .is_zero_matrix for j in (1, -1))
check(ok_ode and record_check("block_ode_equivalent"),
      "h_j chi = eps chi is the same as d chi/dy = f N chi",
      record=f"{PY_REPORT}, check block_ode_equivalent")
```

`kk` is the momentum $k$ as a real symbol. The comment line says what the check is about: the equation $h_j\chi = \varepsilon\chi$ reads $-(ij/f)\sigma_1\chi' = (\varepsilon - v)\chi - j(M\sigma_2 + \kappa k\sigma_3)\chi$ (the first line of the first-order form in Section 14.5; `<=>` means "is the same as"). If $\chi' = fN\chi$, this holds for every $\chi$ exactly when $-(ij/f)\sigma_1\,fN = (\varepsilon - v) - j(M\sigma_2 + \kappa k\sigma_3)$, which is checked for both types; the hidden scale cancels.

```python
d_term = -sp.I / fs * s1  # the matrix in front of d/dy (times j)
ok_types = ((h_algebraic(1, M, kk, kap) + h_algebraic(-1, M, kk, kap))
            .is_zero_matrix
            and (s3 * h_algebraic(1, M, kk, kap) * s3
                 - h_algebraic(-1, M, -kk, kap)).is_zero_matrix
            and (s3 * d_term * s3 + d_term).is_zero_matrix)
check(ok_types and record_check("block_type_relation"),
      "h_(-1) - v = -(h_(+1) - v) and sigma3 h_j(k) sigma3 = h_(-j)(-k)",
      record=f"{PY_REPORT}, check block_type_relation")
```

The two type relations of Section 14.5: the algebraic parts of the two types add to zero; $\sigma_3$ turns the algebraic part of $(+1, k)$ into that of $(-1, -k)$; and $\sigma_3(-(i/f)\sigma_1)\sigma_3 = (i/f)\sigma_1$, so the derivative term changes sign as $j$ does.

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

Section 14.6 line by line: $\sigma_2$ turns the algebraic part of $(j = 1, M)$ into that of $(j = -1, -M)$ at the same $k$, and changes the sign of the derivative term. Out [16] shows the five PASS lines.

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
               and all((R * Xm - Xm * R).is_zero_matrix for Xm in (g0, g4, B, C)))
check(ok_rotation and record_check("rotation_invariance"),
      "a 3-space rotation commutes with g0, g4, B, C and rotates k: only |k| counts",
      record=f"{PY_REPORT}, check rotation_invariance")
```

Three facts: $RR^{-1} = 1$; $R\,k\gamma^{(x_1)}R^{-1} = k(\cos\theta\,\gamma^{(x_1)} - \sin\theta\,\gamma^{(x_2)})$; $R$ commutes with $\gamma^{(x_0)}$, $\gamma^{(x_4)}$, $B$, $C$.

**In [18], the rescaling identity.**

```python
a_sym, y_sym, Y_p = sp.symbols("a y Y", real=True)
b_sym, ell, v_t = sp.symbols("b ell v_t", positive=True)
f_slice = sp.exp(-a_sym) * sp.sqrt(b_sym)  # f0 at the slice
w_a, w_b = sp.Function("w_a"), sp.Function("w_b")  # any column (w_a, w_b)
```

Symbols for the slice values $a_{4,0}$ (`a_sym`) and $b_{4,0}$ (`b_sym`), the hidden coordinate $y$, the proper hidden coordinate $Y$ (`Y_p`), the box size $\ell$ and the extra-time volume $v_t$; `f_slice` is $f_0 = e^{-a_{4,0}}b_{4,0}^{1/2}$; `w_a` and `w_b` are two unknown functions, the components of an arbitrary column on which the Hamiltonians act.

```python
ok_h_slice = True
for j in (1, -1):  # line 1: h_j in y at the slice = h_j in Y at the first slice
    w_y = sp.Matrix([w_a(y_sym), w_b(y_sym)])
    h_y = j * (-sp.I * s1 * sp.diff(w_y, y_sym) / f_slice + M * s2m * w_y
               + sp.exp(-a_sym) * kk * s3 * w_y)
    w_Y = sp.Matrix([w_a(Y_p / f_slice), w_b(Y_p / f_slice)])
    h_Y = j * (-sp.I * s1 * sp.diff(w_Y, Y_p) + M * s2m * w_Y
               + (kk * sp.exp(-a_sym)) * s3 * w_Y)
    ok_h_slice &= sp.simplify(h_y.subs(y_sym, Y_p / f_slice) - h_Y).is_zero_matrix
```

The first line of Section 14.7 for both types: `h_y` is $h_j - v$ at the slice acting on the column $w(y)$, with the derivative divided by $f_0$ and the momentum weight $e^{-a_{4,0}}$; `h_Y` is $h_j - v$ of the first slice ($f = \kappa = 1$) acting on the same column written as a function of $Y$, $w(Y/f_0)$, with the momentum $ke^{-a_{4,0}}$. After putting $y = Y/f_0$ into `h_y` the two are equal: the chain rule $\frac{d}{dY}w(Y/f_0) = \frac1{f_0}w'$ supplies exactly the factor $1/f_0$.

```python
def proper_factor(a_, b_, H_, ell_, v_t_, y_):
    return sp.exp(-3 * H_ * y_) * sp.exp(a_) / (ell_ ** 3 * v_t_ * b_ ** 2)

ok_box = sp.simplify(proper_factor(a_sym, b_sym, H, ell, v_t, y_sym)
                     - proper_factor(0, 1, H / f_slice, ell * sp.exp(a_sym),
                                     v_t * sp.exp(-3 * a_sym)
                                     * b_sym ** sp.Rational(3, 2),
                                     f_slice * y_sym) / f_slice) == 0
```

`proper_factor` is the factor $P = e^{-3Hy}e^{a_{4,0}}/(\ell^3v_tb_{4,0}^2)$ that turns an orbital density per unit $y$ into a density per unit proper volume (Section 14.7). `ok_box` is the third line of Section 14.7: $P$ at the slice equals $P'/f_0$, where $P'$ is the factor of the partner problem at the first slice ($a = 0$, $b = 1$) with the constant $H/f_0$, the box $\ell e^{a_{4,0}}$, the extra-time volume $v_te^{-3a_{4,0}}b_{4,0}^{3/2}$, evaluated at the proper coordinate $Y = f_0y$.

```python
on_hist = {b_sym: sp.exp(sp.Rational(4, 3) * a_sym)}  # b4,0 = e^((4/3) a4,0)
ok_hist = (sp.simplify(f_slice.subs(on_hist) - sp.exp(-a_sym / 3)) == 0
           and sp.simplify((sp.exp(-3 * a_sym) * b_sym ** sp.Rational(3, 2))
                           .subs(on_hist) - sp.exp(-a_sym)) == 0)
check(ok_h_slice and ok_box and ok_hist and record_check("rescaling_identity"),
      "KS(a4,0, b4,0) = KS(0, 1; H/f0, f0 L, dk e^(-a4,0), v_t e^(-3a4,0) b4,0^(3/2))",
      record=f"{PY_REPORT}, check rescaling_identity")
```

On the history $b_{4,0} = e^{(4/3)a_{4,0}}$: $f_0 = e^{-a_{4,0}/3}$ and the partner extra-time factor $e^{-3a_{4,0}}b_{4,0}^{3/2} = e^{-a_{4,0}}$. The check combines the three tests and the verdict of the record.

```python
rows = repository_file("Revision/kohn_sham/results/rescaling/rescaling.csv") \
    .read_text(encoding="utf-8").splitlines()
header = rows[0].split(",")
table = [dict(zip(header, row.split(","))) for row in rows[1:]]
```

The Rust solver's record of the partner problems, a **CSV file** (comma-separated values: a table as text, one row per line, the cells separated by commas, the first line the column names). `splitlines` cuts the text into lines and `split(",")` a line into cells; `dict(zip(header, cells))` makes a dictionary from column name to cell for every row.

```python
partner = {}  # slice -> (dk, v_t, H, L) of the partner problem
worst = 0.0
for a in slices[1:]:
    partner[a] = (0.25 * np.exp(-a), 1.0 * np.exp(-a), 1.0 * np.exp(a / 3.0),
                  3.0 * np.exp(-a / 3.0))  # dk e^-a, v_t e^-a, H e^(a/3), L e^(-a/3)
    say(f"slice a4,0 = {a}: partner dk = {partner[a][0]:.10f}, v_t = "
        f"{partner[a][1]:.10f}, H = {partner[a][2]:.10f}, L = {partner[a][3]:.10f}")
    for row in table:
        if float(row["a4"]) == a:
            mine = zip(partner[a], ("partner_dk", "partner_v_t", "partner_H",
                                    "partner_L"))
            worst = max([worst] + [abs(float(row[c]) / x - 1) for x, c in mine])
check(len(table) == 60 and worst < 1e-14,
      "the partner dk, v_t, H and L equal those of all 60 rows of the record",
      record="Revision/kohn_sham/results/rescaling/rescaling.csv, columns "
             "partner_dk, partner_v_t, partner_H and partner_L")
```

For each later slice (`slices[1:]` leaves out the slice 0) the four partner parameters on the history are computed from the canonical $\Delta k = 0.25$, $v_t = 1$, $H = 1$, $L = 3$ and printed with 10 decimals (the format `:.10f`). For every row of the record at that slice the relative differences of the four columns are taken, and the largest is kept in `worst`. The record has 60 rows (three particle numbers, five couplings and four later slices) and agrees to better than $10^{-14}$. Out [18] shows the partner numbers: at $a_{4,0} = 0.5$ the spacing $0.1516326649$, the extra-time volume $0.6065306597$, the constant $1.1813604129$ and the cutoff $2.5394451747$; at $a_{4,0} = 2$ they are $0.0338338208$, $0.1353352832$, $1.9477340411$ and $1.5402513571$.

**In [19], figure 5.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
for n2 in (1, 2, 3, 4, 5, 6):  # the first shells n1^2 + n2^2 + n3^2
    left.semilogy(a4_values, 0.25 * np.sqrt(n2) * np.exp(-a4_values),
                  label=f"$n^2 = {n2}$")
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("$|\\mathbf{k}|\\,e^{-a_{4,0}}$ (units of $H$, logarithmic)")
left.set_title("redshift of the lattice momenta")
left.legend(fontsize=8, ncol=2)
```

The left panel draws, for the first six lattice shells ($|\mathbf k| = 0.25\sqrt{n^2}$), the redshifted momentum $|\mathbf k|e^{-a_{4,0}}$ against the slice; `ncol=2` puts the legend in two columns.

```python
curves = [(np.exp(a4_values / 3.0), "$H e^{a_{4,0}/3}$", 2),
          (3.0 * np.exp(-a4_values / 3.0), "$L e^{-a_{4,0}/3}$", 3),
          (0.25 * np.exp(-a4_values), "$\\Delta k\\, e^{-a_{4,0}}$", 0),
          (np.exp(-a4_values), "$v_t e^{-a_{4,0}}$", 1)]
for values, text, column in curves:
    line, = right.semilogy(a4_values, values, label=text)
    right.semilogy(slices[1:], [partner[a][column] for a in slices[1:]], "o",
                   color=line.get_color(), markersize=4)
```

The right panel: each entry of `curves` holds the formula of one partner parameter along the history, its label and its position in the tuples of `partner`. `line, = ...` takes the single line that `semilogy` returns, so that the dots (format `"o"`) at the four later slices get the same colour (`line.get_color()`). The dots are the partner values that In [18] compared with all 60 rows of the record.

```python
right.set_xlabel("slice $a_{4,0}$")
right.set_ylabel("partner parameter (logarithmic)")
right.set_title("the partner problem at the first slice")
right.legend(fontsize=8)
save_figure(fig, "rescaling",
            ...)
```

**What figure 14a.5 shows.** Left: six parallel straight lines of slope $-1$ on the logarithmic axis: every lattice momentum is redshifted by the same factor $e^{-a_{4,0}}$, so the ordering of the shells never changes. Right: the partner problem of a later slice has a larger constant $He^{a_{4,0}/3}$ (from 1 to $1.95$: the hidden direction is more strongly warped per unit proper length), a shorter proper cutoff $Le^{-a_{4,0}/3}$ (from 3 to $1.54$), a finer lattice $\Delta k\,e^{-a_{4,0}}$ (from $0.25$ to $0.034$) and a smaller extra-time volume $v_te^{-a_{4,0}}$ (from 1 to $0.135$); the dots of the record lie on the lines. This is the rescaling identity in a picture: a later slice of the deflating history is the first slice with a larger 3-torus and a shorter, more strongly warped hidden direction.

**In [20], the last check.**

```python
figure_names = ["14a_1_hidden_coordinate.png", "14a_2_inflation_deflation.png",
                "14a_3_spin_connection_terms.png", "14a_4_block_structure.png",
                "14a_5_rescaling.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all five figure files of this notebook exist")
all_checks_passed()
```

The five figure files must exist where the notebook wrote them; the last line prints ALL 31 CHECKS PASSED (notebook 14a). The 31 checks are: 1 in In [2], 2 in In [3], 3 in In [4], 2 in In [7], 2 in In [8], 4 in In [10], 2 in In [11], 2 in In [12], 2 in In [13], 2 in In [14], 5 in In [16], 1 in In [17], 2 in In [18] and 1 in In [20].

### 14.12 The block equation in real form and the boundary conditions

**The real form.** In every block the stationary equation is $\chi' = fN\chi$ with $N = M\sigma_3 - \kappa k\,\sigma_2 + ij(\varepsilon - v)\sigma_1$ (Section 14.5). Write the two components of $\chi$ as $\chi = (a, ib)$ with two real functions $a(y)$ and $b(y)$, and write $K = \kappa k$ and $\varepsilon' = \varepsilon - v$ for short. Line by line:

$$
\sigma_3\chi = (a,\ -ib), \qquad \sigma_2\chi = (b,\ ia), \qquad \sigma_1\chi = (ib,\ a) .
$$

Rule: multiply each Pauli matrix of Section 14.1 with the column $(a, ib)$; for example the first entry of $\sigma_2\chi$ is $(-i)(ib) = -i^2b = b$.

$$
N\chi = \Big(Ma - Kb - j\varepsilon' b,\ \ i\big[(j\varepsilon' - K)a - Mb\big]\Big) .
$$

Rule: $N\chi = M\sigma_3\chi - K\sigma_2\chi + ij\varepsilon'\sigma_1\chi$, entry by entry; in the first entry $ij\varepsilon'(ib) = i^2j\varepsilon' b = -j\varepsilon' b$; the second entry is $-iMb - iKa + ij\varepsilon' a$, which is $i$ times the bracket.

$$
a' = f\big[Ma - (K + j\varepsilon')\,b\big], \qquad b' = f\big[(j\varepsilon' - K)\,a - Mb\big] .
$$

Rule: $\chi' = (a', ib') = fN\chi$; compare the first entries, and the second entries divided by $i$. Every coefficient is a real number, so a solution that starts with real values $a$, $b$ stays real: the computer needs only real numbers. Status: PROVED; the record states this form as blockEquation.realForm in `Revision/kohn_sham/ks-theory.json`, and Notebook 14b checks it with sympy (In [2]).

**The densities of one orbital.** From the three products above and $\chi^\dagger = (a, -ib)$ (the conjugate transpose of the column, with $a$, $b$ real):

$$
\chi^\dagger\chi = a^2 + b^2, \qquad \chi^\dagger\sigma_2\chi = 2ab, \qquad \chi^\dagger\sigma_3\chi = a^2 - b^2, \qquad \chi^\dagger\sigma_1\chi = 0 .
$$

Rule: multiply the row $(a, -ib)$ with each column; for example $\chi^\dagger\sigma_2\chi = a\cdot b + (-ib)(ia) = ab + ab$, and $\chi^\dagger\sigma_1\chi = a(ib) + (-ib)a = 0$. These four numbers become the number density, the scalar density, the density $Q$ and the current along $y$ of the orbital (Sections 14.26 and 14.27). Status: PROVED (the multiplication above); the record states the same four formulas as blockEquation.realFormDensities in `Revision/kohn_sham/ks-theory.json`.

**The current along $y$ is the same at every point.** The number $\chi^\dagger\sigma_1\chi$ is the flow along the hidden direction of the U(1) charge of the field (the **current** along $y$). Of this charge only the local conservation law is proved; its total is constant only under the ASSUMED no-flux condition at the ends of the interval of $z$ (Chapter 5, Section 5.6). The fold conditions and the tip condition of the Kohn-Sham record, which are assumed or chosen below, are such conditions: they make the current vanish at both ends of each half. (The pairing theorem T2 of Chapter 18 relates a field on one half of a cell to its image on the other half; it derives no matching of the field across the fold and imposes no such condition.) For every solution of the block equation, complex or real:

$$
\frac{d}{dy}\big(\chi^\dagger\sigma_1\chi\big) = \chi'^\dagger\sigma_1\chi + \chi^\dagger\sigma_1\chi' = f\,\chi^\dagger\big(N^\dagger\sigma_1 + \sigma_1N\big)\chi .
$$

Rule: the product rule; then $\chi' = fN\chi$ and $\chi'^\dagger = (fN\chi)^\dagger = f\chi^\dagger N^\dagger$ ($f$ is a positive number).

$$
N^\dagger = M\sigma_3 - K\sigma_2 - ij\varepsilon'\sigma_1 .
$$

Rule: the Pauli matrices are Hermitian, $M$, $K$, $\varepsilon'$ are real, and the complex conjugate of $i$ is $-i$.

$$
N^\dagger\sigma_1 + \sigma_1N = M(\sigma_3\sigma_1 + \sigma_1\sigma_3) - K(\sigma_2\sigma_1 + \sigma_1\sigma_2) - ij\varepsilon'\sigma_1\sigma_1 + ij\varepsilon'\sigma_1\sigma_1 = 0 .
$$

Rule: two different Pauli matrices anticommute, so the first two brackets are zero, and the last two terms cancel. So the current has the same value at every $y$. The density $\chi^\dagger\chi$ is not constant: its derivative is $f\chi^\dagger(N^\dagger + N)\chi$ with $N^\dagger + N = 2M\sigma_3 - 2K\sigma_2 \ne 0$. Status: PROVED; check bc_current_conserved_along_y of `Revision/kohn_sham/reports/ks-theory-python.json` and of the Wolfram report.

**Why the ends must stop the current.** Section 14.4 called $h$ Hermitian "when the boundary terms vanish". Here is the boundary term. For two columns $\varphi$ and $\chi$ of functions of $y$:

$$
\varphi^\dagger h_j\chi - (h_j\varphi)^\dagger\chi = -\frac{ij}{f}\varphi^\dagger\sigma_1\chi' - \frac{ij}{f}\varphi'^\dagger\sigma_1\chi = \frac{d}{dy}\Big[-\frac{ij}{f}\,\varphi^\dagger\sigma_1\chi\Big] .
$$

Rule, for the first equality: the part of $h_j$ without derivative, $j(M\sigma_2 + K\sigma_3) + v$, is a Hermitian matrix, so it gives $\varphi^\dagger X\chi - (X\varphi)^\dagger\chi = \varphi^\dagger X\chi - \varphi^\dagger X^\dagger\chi = 0$; the derivative part gives $\varphi^\dagger(-(ij/f)\sigma_1\chi') - (-(ij/f)\sigma_1\varphi')^\dagger\chi$, and $(-(ij/f)\sigma_1\varphi')^\dagger = +(ij/f)\varphi'^\dagger\sigma_1$. Rule, for the second: the product rule backwards ($f$ does not depend on $y$). Integrating over one half, from $-L$ to $0$:

$$
\int_{-L}^{0}\varphi^\dagger h_j\chi\,dy - \int_{-L}^{0}(h_j\varphi)^\dagger\chi\,dy = -\frac{ij}{f}\big[\varphi^\dagger\sigma_1\chi\big]_{y=-L}^{y=0} .
$$

Rule: the integral of a derivative is the difference of its end values. So $h_j$ is self-adjoint (the two integrals are equal, the levels are real and orbitals of different levels are orthogonal, Section 14.4) exactly when the boundary conditions make $\varphi^\dagger\sigma_1\chi$ vanish at the ends: the conditions must **kill the current**. Status: PROVED; check bc_self_adjoint_boundary_term (both reports).

**The fold at $y = 0$: two halves, one equation.** The fold $\cos z = 0$ joins the two halves of a cell (Section 14.2). Line by line, why the same $\chi(y)$ describes both halves:

- The reflection $z \to \pi - z$ keeps $|\sin z|$, hence $y$, and changes the sign of $\cot z$ (Section 14.2).
- On each half $dy = \cot z\,dx_0$, and the hidden vielbein, with its sign, is $e^{-a_4}b_4^{1/2}\cot z$; so the proper step along the hidden direction is $e^{-a_4}b_4^{1/2}\cot z\,dx_0 = f\,dy$ on both halves.
- The spin-connection term $\tfrac32(H/f)\gamma^{(x_0)} + (b_4'/b_4 - \tfrac12a_4')\gamma^{(x_4)}$ (Section 14.4) contains no $y$.

So the reduced equation of Section 14.4 is the same on both halves, and a spinor that is continuous across the fold has the same $\chi(y)$ on both. Status: PROVED; the record's check `bc_fold_same_equation_on_both_halves` (both reports).

**The fold conditions (both filled: ASSUMED).** The whole cell, cut off at both tips, consists of the two halves, each described by $-L \le y \le 0$, joined at $y = 0$. On both halves $y$ increases toward the fold, so each half contributes the same end term at the fold, and the boundary form of the whole cell there is

$$
2\Big(-\frac{ij}{f}\Big)\varphi^\dagger\sigma_1\chi(0) .
$$

Rule: the integral over the cell is the sum of the integrals over the two halves; the same $\chi(y)$ and $\varphi(y)$ on both; the end term at $y = 0$ of the integral of Section 14.12 on each half. Self-adjointness needs this form to vanish: a condition $(1 - Q(\theta))\chi(0) = 0$ with $Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2$ (the same family as at the tip below, which kills the current for every $\theta$). Two members of the family are used:

- $\theta = 0$: $(1 - \sigma_3)\chi(0) = 0$, that is $\chi_2(0) = 0$; in real form $b(0) = 0$. It is called the EVEN fold condition.
- $\theta = \pi$: $(1 + \sigma_3)\chi(0) = 0$, that is $\chi_1(0) = 0$; in real form $a(0) = 0$. It is called the ODD fold condition.

Rule: $Q(0) = \sigma_3$, $Q(\pi) = -\sigma_3$, and $1 - \sigma_3 = \mathrm{diag}(0, 2)$, $1 + \sigma_3 = \mathrm{diag}(2, 0)$. Both kill the current, because $\chi^\dagger\sigma_1\chi = \chi_1^*\chi_2 + \chi_2^*\chi_1$ (the star is the complex conjugate) is zero when $\chi_1$ or $\chi_2$ is zero; a general value $\chi(0)$ does not. The Revision record solves both conditions and fills both together, with each orbital normalised on one half, $\int_{-L}^0\chi^\dagger\chi\,dy = 1$ (so its norm on the whole cell is 2); the particle number $N$ counts the whole cell, each half holds $N/2$, and a density at a point of either half carries the weight $w = \tfrac12$ (Section 14.27). That both conditions are filled is ASSUMED: it is the record's convention; the metric is degenerate at the fold ($g_{00}$ and $\sqrt{|g|}$ vanish there) and no junction condition across the fold is derived. Status: the family of fold conditions follows from self-adjointness (PROVED; check bc_fold_conditions, both reports); the filling of both members is ASSUMED. (A dated remark of history: the metric of 2026-10-14, withdrawn on 2026-10-16, ended its coordinate patch at $z = \pi/2$, and the record then assumed there a Z2 mirror copy of the patch that carried the mass $-m$; that construction was withdrawn with that metric. In the corrected metric there is no mirror copy: both halves of a cell carry the same $\chi(y)$ and the same mass.)

**The fold conditions and the mass.** The chirality map $\chi \to \sigma_2\chi$ of Section 14.6 turns the block equation with the mass $M$ into the one with $-M$ and exchanges the two fold conditions (it turns $b(0) = 0$ into $a(0) = 0$, because $\sigma_2(a, ib) = (b, ia)$). This is the ingredient of the Kohn-Sham-level pairing theorem T3 (Chapter 19): the partner with $-m$ is a different Kohn-Sham problem, with the two fold conditions exchanged and the tip angle $\pi - \theta$, not a copy carried by the other half of the cell. It is an exact map between solutions of the equations with an ASSUMED boundary construction; it does not say that a second universe, or a pair of universes, is created by any process: no creation process, rate or amplitude follows from these equations (Chapters 18 to 20 give the complete statements and the list of what is not proved).

**The tip (ASSUMED: a chosen cutoff condition).** The hidden coordinate runs to minus infinity at the tip, which a computer cannot reach. The Revision solver stops at $y = -L$ ($L = 3$) and imposes there one member of the family

$$
\big(1 - Q(\theta)\big)\chi(-L) = 0, \qquad Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2 .
$$

Line by line, why every member kills the current. First, $Q^\dagger = Q$ (rule: $\sigma_3$, $\sigma_2$ are Hermitian, $\cos\theta$ and $\sin\theta$ are real). Second, $Q^2 = \cos^2\theta + \sin^2\theta + \cos\theta\sin\theta(\sigma_3\sigma_2 + \sigma_2\sigma_3) = 1$ (rule: multiply out; each $\sigma^2 = 1$ and the bracket is zero). Third, $Q\sigma_1 = -\sigma_1Q$ (rule: $\sigma_1$ anticommutes with $\sigma_3$ and with $\sigma_2$). Now if $Q\chi = \chi$ at the end point, then

$$
\chi^\dagger\sigma_1\chi = \chi^\dagger\sigma_1Q\chi = -\chi^\dagger Q\sigma_1\chi = -(Q\chi)^\dagger\sigma_1\chi = -\chi^\dagger\sigma_1\chi ,
$$

so $\chi^\dagger\sigma_1\chi = 0$ there. Rule: replace $\chi$ by $Q\chi$, move $Q$ to the left with the third fact, use $Q^\dagger = Q$, then $Q\chi = \chi$ again. The canonical choice is $\theta = 0$: $(1 - \sigma_3)\chi(-L) = 0$, that is $\chi_2(-L) = 0$, $b(-L) = 0$, the **regular tip**. In real form a member $\theta$ is satisfied by the starting point $(a, b) = (\cos\tfrac\theta2, \sin\tfrac\theta2)$ at $y = -L$ (Exercise 14.3), which is where the shooting of Section 14.14 starts. Status: the algebra is PROVED (check bc_tip_family, both reports); the choice of the condition is ASSUMED.

**Zero current everywhere.** An **orbital** is a solution that satisfies the fold condition and the tip condition. Its current is zero at the two ends and the same at every $y$, so it is zero everywhere. (For a real solution $(a, b)$ it is zero anyway, by the densities above.)

**Nothing suppresses an orbital toward the tip.** Take $M$ and $v$ constant. Line by line:

$$
N^2 = M^2\sigma_3^2 + \kappa^2k^2\sigma_2^2 + \big(ij(\varepsilon - v)\big)^2\sigma_1^2 = \big(M^2 + \kappa^2k^2 - (\varepsilon - v)^2\big)\,1 .
$$

Rule: square the sum of the three terms of $N$; each $\sigma^2 = 1$; $(ij)^2 = -1$; the mixed products of two different Pauli matrices appear in pairs $\sigma_a\sigma_b + \sigma_b\sigma_a = 0$ and cancel.

- So $N$ has the eigenvalues $+\Lambda$ and $-\Lambda$ with $\Lambda = \sqrt{M^2 + \kappa^2k^2 - (\varepsilon - v)^2}$ (rule: if $Nu = \nu u$, then $\nu^2u = N^2u = \Lambda^2u$).
- On an eigenvector $u_\pm$ the equation $\chi' = fN\chi$ reads $\chi' = \pm f\Lambda\chi$, with the solution $e^{\pm f\Lambda y}u_\pm$ (rule: the derivative of $e^{cy}$ is $ce^{cy}$).
- For $\Lambda^2 > 0$ one branch decays toward the tip and the other grows, at the same rate $f\Lambda$ at every $y$; for $\Lambda^2 < 0$ both oscillate.

Because $\kappa$ does not depend on $y$, $\Lambda$ is the same everywhere: nothing pushes an orbital away from the tip, and the condition at the cutoff acts on a part of the orbital that is not small in general. An extended orbital (one that oscillates along $y$) feels the cutoff like a wave in a box of proper length $fL$. Only an orbital whose shape is exactly $e^{fMy}$, the zero mode of Section 14.13 and the fold band of Section 14.19, has at the cutoff the small relative size $e^{-fML}$. Status: the asymptotic branches are PROVED (check bc_tip_asymptotics, both reports); what the tip angle does to the levels is COMPUTED in Section 14.20 (check free_tip_angle_boundary_identity of `Revision/kohn_sham/reports/ks-rust-solver.json`, record `Revision/kohn_sham/results/spectrum/tip-angle.csv`).

### 14.13 The exact free levels at zero 3-momentum

Take $k = 0$, $v = 0$ and a constant mass $M > 0$. The real form becomes $a' = f(Ma - j\varepsilon b)$, $b' = f(j\varepsilon a - Mb)$. These two equations can be solved by hand, completely. The solutions are the first test of any numerical method for the model.

**Step 1: one equation of second order.** Suppose $\varepsilon \ne 0$. Line by line:

$$
a = \frac{b'/f + Mb}{j\varepsilon} .
$$

Rule: solve the second equation for $a$ (divide by $f$, add $Mb$ and divide by $j\varepsilon \ne 0$).

$$
a' = \frac{b''/f + Mb'}{j\varepsilon} .
$$

Rule: differentiate; $f$, $M$, $j$, $\varepsilon$ are constants.

$$
\frac{b''}{f} + Mb' = M\big(b' + fMb\big) - fj^2\varepsilon^2b .
$$

Rule: insert the two lines into the first equation $a' = f(Ma - j\varepsilon b)$ and multiply by $j\varepsilon$.

$$
b'' = f^2\big(M^2 - \varepsilon^2\big)\,b .
$$

Rule: $j^2 = 1$, $Mb'$ cancels on both sides, and multiply by $f$.

The general solution of this equation depends on the sign of $M^2 - \varepsilon^2$ (check each by differentiating twice): if $\varepsilon^2 > M^2$, write $M^2 - \varepsilon^2 = -p^2$ with $p > 0$, and $b = A\sin(fpy) + B\cos(fpy)$; if $\varepsilon^2 < M^2$, write $M^2 - \varepsilon^2 = q^2$ with $q > 0$, and $b = Ae^{fqy} + Be^{-fqy}$; if $\varepsilon^2 = M^2$, then $b = A + By$. Here $A$ and $B$ are constants.

**Step 2: the even fold condition, $b(0) = 0$ and $b(-L) = 0$.**

- $\varepsilon^2 > M^2$: $b(0) = B = 0$, so $b = A\sin(fpy)$; then $b(-L) = -A\sin(fpL) = 0$ with $A \ne 0$ requires $fpL = n\pi$, $n = 1, 2, 3, \dots$ Hence the levels $\varepsilon = \pm\sqrt{M^2 + (n\pi/(fL))^2}$, with the orbital $b = \sin(n\pi y/L)$.
- $\varepsilon^2 < M^2$, $\varepsilon \ne 0$: $b(0) = A + B = 0$ gives $b = A(e^{fqy} - e^{-fqy})$, and $b(-L) = A(e^{-fqL} - e^{fqL}) = 0$ forces $A = 0$ (because $e^{fqL} > e^{-fqL}$); then $b = 0$ and $a = (b'/f + Mb)/(j\varepsilon) = 0$: no orbital.
- $\varepsilon^2 = M^2$: $b(0) = A = 0$ and $b(-L) = -BL = 0$, so $b = 0$ and again no orbital.
- $\varepsilon = 0$ (Step 1 does not apply): the equations separate, $a' = fMa$ and $b' = -fMb$, so $a = Ae^{fMy}$, $b = Be^{-fMy}$. The fold condition $b(0) = B = 0$ makes $b = 0$ everywhere, which also satisfies $b(-L) = 0$. So $\chi = (Ae^{fMy}, 0)$ is an orbital with $\varepsilon = 0$, for every $L$: the **fold zero mode**, largest at the fold.

The constant of the zero mode follows from the normalisation $\int_{-L}^0 a^2\,dy = 1$:

$$
\int_{-L}^{0}A^2e^{2fMy}\,dy = A^2\,\frac{1 - e^{-2fML}}{2fM} = 1, \qquad A = \sqrt{\frac{2fM}{1 - e^{-2fML}}} .
$$

Rule: the integral of $e^{2fMy}$ is $e^{2fMy}/(2fM)$; evaluate at $0$ and $-L$ and subtract; solve for $A > 0$.

**Step 3: the odd fold condition, $a(0) = 0$ and $b(-L) = 0$.**

- $\varepsilon^2 > M^2$: the solution with $b(-L) = 0$ is $b = A\sin(fp(y + L))$ (the general solution written around the point $-L$, where the cosine term must vanish). By Step 1, $a(0) = 0$ means $b'(0)/f + Mb(0) = 0$, that is $A[p\cos(pfL) + M\sin(pfL)] = 0$. So the levels are $\varepsilon = \pm\sqrt{M^2 + p^2}$ where $p > 0$ solves

$$
g(p) = M\sin(pfL) + p\cos(pfL) = 0, \qquad \text{equivalently} \qquad \tan(pfL) = -\frac{p}{M} .
$$

Rule: divide by $M\cos(pfL)$, which is not zero (if $\cos(pfL) = 0$ then $g = \pm M \ne 0$).
- $\varepsilon^2 < M^2$, $\varepsilon \ne 0$: $b = A(e^{fq(y+L)} - e^{-fq(y+L)})$, and $b'(0)/f + Mb(0) = A[q(e^{fqL} + e^{-fqL}) + M(e^{fqL} - e^{-fqL})] = 0$ forces $A = 0$ (the bracket is positive): no orbital.
- $\varepsilon^2 = M^2$: $b = B(y + L)$ and $b'(0)/f + Mb(0) = B(1/f + ML) = 0$ forces $B = 0$: no orbital.
- $\varepsilon = 0$: $a = Ae^{fMy}$ with $a(0) = A = 0$, and $b = Be^{-fMy}$ with $b(-L) = Be^{fML} = 0$, so $B = 0$: there is no zero mode of the odd fold condition.

**Step 4: the odd roots.** Count the roots of $g(p) = M\sin(pfL) + p\cos(pfL)$ for $p > 0$. At $p = (n + \tfrac12)\pi/(fL)$ the sine is $(-1)^n$ and the cosine 0, so $g = M(-1)^n$; at $p = (n + 1)\pi/(fL)$ the sine is 0 and the cosine $(-1)^{n+1}$, so $g = p(-1)^{n+1}$. The two values have opposite signs, so $g$ has a root in between (rule: a continuous function that changes sign on an interval is zero somewhere in it). It has exactly one there: on this interval $\tan(pfL)$ rises from minus infinity to 0 while $-p/M$ falls, so the two curves meet once; and on the intervals from $n\pi/(fL)$ to $(n + \tfrac12)\pi/(fL)$ there is no root, because there $\tan(pfL) > 0 > -p/M$. So the roots are $p_0 < p_1 < p_2 < \dots$, one in each interval $((n + \tfrac12)\pi/(fL),\ (n + 1)\pi/(fL))$.

**Summary (PROVED).** At $k = 0$, $v = 0$, constant $M > 0$ and the canonical tip:

| fold condition | levels | orbital |
| --- | --- | --- |
| even | $0$ (the fold zero mode) | $a = A\,e^{fMy}$, $b = 0$ |
| even | $\pm\sqrt{M^2 + (n\pi/(fL))^2}$, $n = 1, 2, \dots$ | $b = \sin(n\pi y/L)$, $a = (b'/f + Mb)/(j\varepsilon)$ |
| odd | $\pm\sqrt{M^2 + p_n^2}$, $\tan(p_nfL) = -p_n/M$ | $b = \sin(fp_n(y + L))$, $a = (b'/f + Mb)/(j\varepsilon)$ |

Here $A = \sqrt{2fM/(1 - e^{-2fML})}$ is the normalisation constant computed above. Only the product $fL$, the proper length of the cut-off half, enters the levels. Apart from the zero mode, every level has $|\varepsilon| > M$: the free spectrum has a gap from $-M$ to $M$ that contains only the zero modes. Every level of one block type is held by its four blocks $(s_2, s_3)$, so it is 4-fold per type and 8-fold in all (for $v = 0$ the levels of the type $j = -1$ are the negatives of those of $j = +1$, Section 14.5, and the set of levels above is symmetric). Status: PROVED; check bc_exact_k0_spectra (both reports).

**The numbers for $M = 1$, $L = 3$** (Notebook 14b, Out [4]): at the slice 0 ($f = 1$) the first odd roots are $p_0 = 0.818548$, $p_1 = 1.744313$, $p_2 = 2.734844$; the lowest odd level is $\sqrt{1 + p_0^2} = 1.292292828069\,m$ and the lowest positive even level is $\sqrt{1 + (\pi/3)^2} = 1.447971930402\,m$. At the slice $a_{4,0} = 1.5$ of the history the hidden direction is shorter, $f = e^{-1/2}$ and $fL = 1.819592$; the first odd roots are $p_0 = 1.236913$, $p_1 = 2.779599$, $p_2 = 4.438138$, and the two lowest positive levels rise to $1.590582904485\,m$ (odd) and $1.995226701059\,m$ (even). The Rust solver's record `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv` lists 72 such exact levels (labels $-3$ to $5$, both fold conditions, $(m, L, a_{4,0}) = (1, 3, 0), (1, 2, 0), (2, 3, 0), (1, 3, 1.5)$) next to its numerical ones (check free_k0_analytic_spectra of `Revision/kohn_sham/reports/ks-rust-solver.json`); Notebook 14b reproduces both columns.

**The labels.** The Revision solver names the levels by integer **labels**: even fold condition, label 0 is the zero mode, label $n > 0$ the $n$-th positive level and $-n$ its negative; odd fold condition, label $l \ge 0$ is the level $+\sqrt{M^2 + p_l^2}$ and label $l \le -1$ the level $-\sqrt{M^2 + p_{-l-1}^2}$. Section 14.14 shows that these labels are not arbitrary names: they count half-turns.

### 14.14 Shooting with a Pruefer angle: every level has a label

**Shooting.** For nonzero $k$, or a mass and a potential that depend on $y$, the block equation cannot in general be solved by hand, and the computer finds the levels by **shooting** (Chapter 2): start at one end with the condition there, integrate to the other end, and adjust the energy until the condition there holds too. Here the start is the tip, with $(a, b) = (\cos\tfrac\theta2, \sin\tfrac\theta2)$ at $y = -L$, which is $(1, 0)$ for the canonical $\theta = 0$; the real form is integrated from $y = -L$ to $y = 0$ for a trial energy $\varepsilon$; and $\varepsilon$ is a level of the even fold condition if $b(0) = 0$, of the odd one if $a(0) = 0$.

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
ab' - ba' = f\big[j\varepsilon'(a^2 + b^2) - K(a^2 - b^2) - 2Mab\big] .
$$

Rule: insert the real form, $a f[(j\varepsilon' - K)a - Mb] - b f[Ma - (K + j\varepsilon')b]$, and collect the terms.

$$
\theta' = f\big[j\varepsilon' - K\cos2\theta - M\sin2\theta\big] .
$$

Rule: divide the last two lines by $r^2$, with $a^2 - b^2 = r^2(\cos^2\theta - \sin^2\theta) = r^2\cos2\theta$ and $2ab = 2r^2\sin\theta\cos\theta = r^2\sin2\theta$ (the double-angle formulas). The equation for $\theta$ does not contain $r$, so the angle can be followed by itself. Status: PROVED; Notebook 14b checks the last line with sympy (In [6]).

**The angle at the fold grows with the energy.** Let $a_\varepsilon = \partial a/\partial\varepsilon$ and $b_\varepsilon = \partial b/\partial\varepsilon$ be the rates at which the solution changes when the trial energy changes (the tip values do not depend on $\varepsilon$), and put $w = ab_\varepsilon - ba_\varepsilon$. By the same rule as for $\theta'$, with $\varepsilon$ in place of $y$, $\partial\theta/\partial\varepsilon = w/r^2$. Line by line:

$$
w' = a'b_\varepsilon + ab_\varepsilon' - b'a_\varepsilon - ba_\varepsilon' .
$$

Rule: the product rule.

$$
a_\varepsilon' = f\big[Ma_\varepsilon - (K + j\varepsilon')b_\varepsilon - jb\big], \qquad b_\varepsilon' = f\big[(j\varepsilon' - K)a_\varepsilon - Mb_\varepsilon + ja\big] .
$$

Rule: differentiate the real form with respect to $\varepsilon$; the product rule applied to $j\varepsilon' b$ and $j\varepsilon' a$ gives the extra terms $-jb$ and $+ja$, since $\partial\varepsilon'/\partial\varepsilon = 1$.

$$
w' = fj(a^2 + b^2) = fjr^2 .
$$

Rule: insert the real form and the last line into the first line; every term that contains $M$, $K$ or $\varepsilon'$ appears twice with opposite signs and cancels, and what is left is $a(fja) - b(-fjb)$.

$$
\frac{\partial\theta(0)}{\partial\varepsilon} = \frac{w(0)}{r(0)^2} = \frac{fj}{r(0)^2}\int_{-L}^{0}r^2\,dy .
$$

Rule: $w(-L) = 0$, because the starting point does not depend on $\varepsilon$ ($a_\varepsilon = b_\varepsilon = 0$ at $y = -L$); integrate $w' = fjr^2$ from $-L$ to $0$. So the **shooting function** $\Phi(\varepsilon) = j\,\theta(0)$ has the derivative $f\int r^2dy/r(0)^2 > 0$: it grows strictly with the energy. Status: PROVED (this derivation); Notebook 14b confirms it numerically for $k = 0$ and $k = 0.75$ at two slices (In [7]).

**Every level has an integer label.** $b(0) = 0$ means that $\theta(0)$ is a whole multiple of $\pi$; $a(0) = 0$ means that $\theta(0)$ is $\pi/2$ plus a whole multiple of $\pi$. With $\Phi = j\theta(0)$:

$$
\text{even level:}\ \ \Phi(\varepsilon) = l\pi, \qquad \text{odd level:}\ \ \Phi(\varepsilon) = \frac\pi2 + l\pi, \qquad l = \dots, -1, 0, 1, \dots
$$

The integer $l$ is the **label** of the level. Because $\Phi$ grows strictly, it passes every target value at most once. It passes every target value at least once, because it runs from $-\infty$ to $+\infty$. Line by line:

$$
\theta(0) - \theta(-L) = \int_{-L}^{0}\theta'\,dy = jf\varepsilon L - jf\int_{-L}^{0}v\,dy - f\int_{-L}^{0}\big(K\cos2\theta + M\sin2\theta\big)\,dy .
$$

Rule: integrate the equation of the Pruefer angle from $-L$ to $0$, with $\varepsilon' = \varepsilon - v$ (the integral of the constant $jf\varepsilon$ over an interval of length $L$ is $jf\varepsilon L$).

$$
\big|\Phi(\varepsilon) - f\varepsilon L\big| \le |\theta(-L)| + f\int_{-L}^{0}|v|\,dy + f\int_{-L}^{0}\big(|K| + |M|\big)\,dy .
$$

Rule: multiply the last line by $j$ (with $j^2 = 1$ this gives $\Phi = j\theta(0)$ on the left and $f\varepsilon L$ as the first term on the right), move every other term to the right side, and use $|j| = 1$, $|\cos2\theta| \le 1$, $|\sin2\theta| \le 1$ and the rule that the size of an integral is at most the integral of the size. The right side does not depend on $\varepsilon$: the start angle $\theta(-L)$ is fixed by the tip condition, and $v$, $K$ and $M$ are given. So $\Phi(\varepsilon)$ stays within a fixed distance of the straight line $f\varepsilon L$: for very negative $\varepsilon$ it lies below every target value, for very positive $\varepsilon$ above it, and because it has no jumps it passes the target value in between (the intermediate value theorem, Chapter 2). Hence there is exactly one level for every label and fold condition, no level can be missed and none can be counted twice. Status: PROVED (this derivation; it is not a separate check of the Revision record, and Notebook 14b confirms the labels numerically). At $k = 0$ these are exactly the labels of Section 14.13 (Figure 14b.6 shows the angles).

**Finding a level.** The notebooks of this chapter find a level by plain **bisection** on $\Phi(\varepsilon) - $ target (Chapter 2): they keep an interval with the target between $\Phi(\text{lo})$ and $\Phi(\text{hi})$ and halve it 72 times, starting from $[-20, 20]$. After 72 halvings the interval has the length $40/2^{72} \approx 8.5\times10^{-21}$, far below the spacing of floating-point numbers near 1 (about $2.2\times10^{-16}$): the result is the level of the integrated equation to the last digit the computer can hold, and the error that remains is the error of the integration. The Revision Rust solver finds the root of the same function $\Phi$ with fewer evaluations, by the **safeguarded Newton-bisection** of Section 2.24 (the function find_level of `Revision/kohn_sham/solver/src/shoot.rs`): it widens a bracket around a first guess until $\Phi - $ target changes sign, then takes Newton steps with the derivative $d\Phi/d\varepsilon = f\int r^2dy/r(0)^2$ derived above, takes the midpoint of the bracket instead whenever a Newton step would leave the bracket or the last step has not at least halved the mismatch $|\Phi - \text{target}|$, and stops when the bracket, or its last Newton step, is shorter than the tolerance $10^{-13}$ (rootTolerance of `Revision/kohn_sham/results/parameters.json`). Both find the root of the same integrated $\Phi$, so the two sets of levels agree to far below $10^{-11}$; Notebook 14b measures the largest difference, $1.1\times10^{-14}$ (Out [8]).

**The integration (RK4).** The real form is integrated with the classical fourth-order Runge-Kutta method of Chapter 2, with $G$ steps of size $h = L/G$ (the Revision solver uses $G = 900$ for $L = 3$, so $h = 1/300$). In the free problem the three coefficients $fM$, $f\kappa k$ and $fj\varepsilon$ are the same at every $y$; for the self-consistent problem the solver stores the potentials at the nodes and at the midpoints of the steps, a fine grid of $2G + 1$ points, because RK4 needs them there. Its error is proportional to $(fh\varepsilon)^4$: halving the step divides the error of a level by $2^4 = 16$. The Revision record measured exactly this: doubling the step number ($G = 1800$ for $L = 3$, $1200$ for $L = 2$) divided the errors of 39 levels whose error is above $10^{-11}$ by the median factor 16.00, and the largest errors were $5.050\times10^{-8}$ with the canonical and $3.157\times10^{-9}$ with the refined step (check refined_free_spectra_convergence_order of `Revision/kohn_sham/reports/ks-rust-determinism.json`). One detail of that measurement: its program (`Revision/kohn_sham/solver/tools/compare_runs.py`) keys the rows of the record by $(m, L$, fold condition, label$)$ without the slice, so the rows of the case $(1, 3, 1.5)$ replace those of $(1, 3, 0)$ and its 39 levels belong to the cases $(1, 3, 1.5)$, $(1, 2, 0)$ and $(2, 3, 0)$; Notebook 14b repeats the measurement that way and also over all 72 levels, where 52 levels are above $10^{-11}$ and the median ratio is again 16.00 (Out [10]). Status: COMPUTED.

### 14.15 Example: Notebook 14b, the free spectra exact and numerical

Notebook 14b does Sections 14.12 to 14.14 with the computer. With sympy it checks the real form with the hidden scale $f$, the fold facts (the same equation on both halves, with the spin-connection term recomputed from the scale factors), the fold conditions, the boundary term, the tip family, the constant current, the asymptotic branches, the exact solutions of Section 14.13 and the equation of the Pruefer angle, each against the verdict of the Revision record. With numpy it writes the shooting function of the Revision Rust solver in about forty lines (RK4 with the coefficients formed as the solver forms them, the Pruefer angle followed step by step) with plain bisection on the labels (the Rust solver uses the safeguarded Newton-bisection of Section 14.14 instead), finds the 72 levels of the record and compares them with the exact levels and with the Rust numbers, repeats the fourth-order measurement, and compares the numerical orbitals with the exact ones at two slices. It draws six figures. It needs no Rust. It runs in about a minute and a half (two cells integrate the equation for hundreds of energies at once, 72 times over, and take 10 to 30 seconds each), and its last line is ALL 20 CHECKS PASSED (notebook 14b).

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

PY_REPORT = "Revision/kohn_sham/reports/ks-theory-python.json"
WL_REPORT = "Revision/kohn_sham/reports/ks-theory-wolfram.json"
RUST_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
```

The module `math` computes with single floating-point numbers, numpy with whole arrays of them, sympy exactly with symbols (Section 14.11). The three reports of the Revision record that this notebook reproduces: the sympy and WolframScript verifiers of the theory and the Rust solver's report.

```python
def record_check(name, reports=(PY_REPORT, WL_REPORT)):
    verdicts = []
    for report in reports:
        data = json.loads(repository_file(report).read_text(encoding="utf-8"))
        found = [c["verdict"] for c in data["checks"] if c["name"] == name]
        verdicts.append(found[0] if found else "absent")
    return verdicts[0] == "PASS" and all(v in ("PASS", "absent") for v in verdicts)
```

As in Notebook 14a, but the reports to read are a parameter with a default value: the verdict of the check `name` must be PASS in the first report and PASS or absent in the others. Called with `(RUST_REPORT,)`, a tuple of one report, it reads only the Rust report.

```python
s1 = sp.Matrix([[0, 1], [1, 0]])  # the Pauli matrices
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)
a, b, M, K, e, v = sp.symbols("a b M K epsilon v", real=True)
fs = sp.symbols("f", positive=True)  # the hidden scale of the slice
```

The Pauli matrices (here `s2` is $\sigma_2$), the unit matrix, and real symbols for the two components $a$, $b$, the mass $M$, $K = \kappa k$, the level $\varepsilon$ (`e`) and the potential $v$; the hidden scale $f$ is a positive symbol.

```python
ok_all = True
for j in (1, -1):
    N = M * s3 - K * s2 + sp.I * j * (e - v) * s1  # the matrix of chi' = f N chi
    derivative = sp.expand(fs * N * sp.Matrix([a, sp.I * b]))  # f N times (a, i b)
    a_prime = fs * (M * a - (K + j * (e - v)) * b)  # the real form
    b_prime = fs * ((j * (e - v) - K) * a - M * b)
    ok = (sp.expand(derivative[0] - a_prime) == 0
          and sp.expand(derivative[1] - sp.I * b_prime) == 0)
    ok_all &= ok
    say(f"j = {j:+d}: d chi/dy = f N chi with chi = (a, i b) gives the real form: "
        f"{ok}")
```

For both block types: $fN$ times the column $(a, ib)$, multiplied out (`expand`), must be $(a', ib')$ with the two lines of the real form of Section 14.12. The format `:+d` prints a whole number with its sign. Out [2] prints True for $j = +1$ and $j = -1$.

```python
theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                    .read_text(encoding="utf-8"))
say("record: " + theory["blockEquation"]["realForm"])
check(ok_all, "the real form da/dy = f[M a - (K + j(eps - v)) b], "
      "db/dy = f[(j(eps - v) - K) a - M b]")
```

The record's own statement of the real form is printed for comparison (with $M_{\rm eff}$, $v_v$ and $\kappa k$ written out), and the PASS line follows.

**In [3], the boundary conditions.**

```python
y = sp.symbols("y", real=True)
a0, k, H = sp.symbols("a0 k H", real=True)
Mf = sp.Function("M", real=True)(y)  # a mass that depends on y
vf = sp.Function("v", real=True)(y)  # a potential that depends on y
kap = sp.exp(-a0)  # the momentum weight: the same at every y
```

The boundary facts hold for a mass $M(y)$ and a potential $v(y)$ that depend on $y$, so they are unknown functions here; `kap` is $\kappa = e^{-a_{4,0}}$, which contains no $y$.

```python
zeta, x4 = sp.symbols("zeta x4", real=True)
a4 = sp.Function("a4", real=True)(x4)
b4 = sp.Function("b4", positive=True)(x4)
f_t = sp.exp(-a4) * sp.sqrt(b4)  # the hidden scale as a function of the time
scale = [f_t] + [sp.exp(a4)] * 3 + [1] + [f_t * sp.exp(H * y)] * 3  # (y, x1..x7)
coords = [y, None, None, None, x4, None, None, None]  # what the factors depend on
```

`zeta` stands for $z$; $a_4$, $b_4$ are unknown functions of the time and `f_t` is the hidden scale; `scale` lists the eight scale factors of the $y$ chart, and `coords` the coordinate whose derivative matters for each frame direction (`None`, Python's word for nothing, where no scale factor depends on that coordinate).

```python
slash = {}  # B -> coefficient of gamma^(B) in gamma^mu Omega_mu
for B_ in (0, 4):  # only y and x4 appear in the scale factors
    slash[B_] = sp.simplify(sum(sp.diff(sp.log(scale[l]), coords[B_])
                                for l in range(8) if l != B_) / (2 * scale[B_]))
say(f"coefficient of gamma^(x0): {slash[0]}")
say(f"coefficient of gamma^(x4): {slash[4]}")
```

Step 4 of Section 14.4 summed over the directions: the coefficient of $\gamma^{(B)}$ in $\sum_\mu\gamma^\mu\Omega_\mu$ is $\tfrac12\sum_{l \ne B}\partial_B\ln h_l/h_B$. Only $B = y$ (position 0) and $B = x_4$ can occur, because the scale factors depend only on $y$ and $x_4$. Out [3] prints `3*H*exp(a4(x4))/(2*sqrt(b4(x4)))`, which is $\tfrac32H/f$, and `-Derivative(a4(x4), x4)/2 + Derivative(b4(x4), x4)/b4(x4)`, which is $b_4'/b_4 - \tfrac12a_4'$: the result of Notebook 14a, computed here in four lines.

```python
ok_fold = (sp.simplify(sp.sin(sp.pi - zeta) - sp.sin(zeta)) == 0
           and sp.simplify(sp.cot(sp.pi - zeta) + sp.cot(zeta)) == 0
           and sp.simplify(sp.diff(sp.log(sp.sin(zeta) ** 2) / 2, zeta)
                           - sp.cot(zeta)) == 0
           and sp.simplify(slash[0] - sp.Rational(3, 2) * H / f_t) == 0
           and sp.simplify(slash[4] - (sp.diff(b4, x4) / b4 - sp.diff(a4, x4) / 2))
           == 0 and not slash[0].has(y) and not slash[4].has(y))
check(ok_fold and record_check("bc_fold_same_equation_on_both_halves"),
      "z -> pi - z keeps y, flips cot z; gamma^mu Omega_mu has no y: same chi(y)",
      record=f"{PY_REPORT}, check bc_fold_same_equation_on_both_halves")
```

The fold facts of Section 14.12: $\sin(\pi - z) = \sin z$ (so $y$ is the same on both halves), $\cot(\pi - z) = -\cot z$, $\frac{d}{dz}\tfrac12\ln\sin^2z = \cot z$ (so $dy = \cot z\,dx_0$ on both halves, with $H$ scaled out), the two coefficients of the spin-connection term, and that neither contains $y$ (`has(y)`). Together: the same reduced equation, hence the same $\chi(y)$, on both halves.

```python
c1f, c2f = sp.Function("chi1")(y), sp.Function("chi2")(y)
chi = sp.Matrix([c1f, c2f])
current = sp.expand((chi.H * s1 * chi)[0])  # the current chi^dag sigma1 chi
th = sp.symbols("theta", real=True)
Q = sp.cos(th) * s3 + sp.sin(th) * s2  # the family of end conditions
c_a, c_b = sp.symbols("c_a c_b", positive=True)  # a general end value (c_a, c_b)
```

A column $\chi = (\chi_1, \chi_2)$ of two unknown complex functions; the current $\chi^\dagger\sigma_1\chi$ (the product is a $1 \times 1$ matrix, `[0]` takes its entry); the family $Q(\theta)$; and two positive symbols for a general end value.

```python
fold_ok = (Q.subs(th, 0) == s3 and Q.subs(th, sp.pi) == -s3  # (1 - Q) chi(0) = 0
           and sp.simplify(current.subs(c2f, 0)) == 0  # theta = 0: chi2(0) = 0
           and sp.simplify(current.subs(c1f, 0)) == 0  # theta = pi: chi1(0) = 0
           and sp.simplify(current.subs({c1f: c_a, c2f: c_b})) != 0)
check(fold_ok and record_check("bc_fold_conditions"),
      "both fold conditions chi2(0) = 0 and chi1(0) = 0 kill the current",
      record=f"{PY_REPORT}, check bc_fold_conditions")
```

$Q(0) = \sigma_3$ and $Q(\pi) = -\sigma_3$, the two members used at the fold; with $\chi_2 = 0$ or with $\chi_1 = 0$ the current vanishes, while for a general end value $(c_a, c_b)$ it does not (it is $2c_ac_b$): a condition is needed, and both fold conditions qualify.

```python
phi = sp.Matrix([sp.Function("phi1")(y), sp.Function("phi2")(y)])
ok_adjoint = True
for j in (1, -1):
    def h_on(w, j=j):  # h_j applied to the column w
        return j * (-sp.I / fs * s1 * sp.diff(w, y) + Mf * s2 * w
                    + kap * k * s3 * w) + vf * w
    difference = (phi.H * h_on(chi))[0] - (h_on(phi).H * chi)[0]
    boundary = sp.diff(-sp.I * j / fs * (phi.H * s1 * chi)[0], y)
    ok_adjoint &= sp.simplify(sp.expand(difference - boundary)) == 0
check(ok_adjoint and record_check("bc_self_adjoint_boundary_term"),
      "phi^dag h chi - (h phi)^dag chi = d/dy[-(i j/f) phi^dag sigma1 chi]",
      record=f"{PY_REPORT}, check bc_self_adjoint_boundary_term")
```

A second column $\varphi$ and the block Hamiltonian `h_on` with the $y$-dependent $M$ and $v$ (the default argument `j=j` fixes the current block type inside the function). The check is the identity of Section 14.12: $\varphi^\dagger h_j\chi - (h_j\varphi)^\dagger\chi$ is the derivative of $-(ij/f)\varphi^\dagger\sigma_1\chi$, for both types.

```python
check(sp.simplify(Q * Q - I2).is_zero_matrix and Q.H == Q
      and sp.simplify(Q * s1 + s1 * Q).is_zero_matrix and record_check("bc_tip_family"),
      "the tip family Q(theta): Q^dag = Q, Q^2 = 1, Q sigma1 = -sigma1 Q",
      record=f"{PY_REPORT}, check bc_tip_family")
```

The three facts behind the tip family: $Q^2 = 1$, $Q^\dagger = Q$, $Q\sigma_1 = -\sigma_1Q$.

```python
kp = sp.symbols("kappa", positive=True)
ok_current, ok_square = True, True
for j in (1, -1):
    Nn = M * s3 - kp * k * s2 + sp.I * j * (e - v) * s1
    ok_current &= sp.simplify(Nn.H * s1 + s1 * Nn).is_zero_matrix
    density_changes = not sp.simplify(Nn.H + Nn).is_zero_matrix
    ok_square &= sp.simplify(Nn * Nn - (M ** 2 + kp ** 2 * k ** 2 - (e - v) ** 2)
                             * I2).is_zero_matrix
check(ok_current and density_changes and record_check("bc_current_conserved_along_y"),
      "the current is constant along y on every solution, the density is not",
      record=f"{PY_REPORT}, check bc_current_conserved_along_y")
check(ok_square and record_check("bc_tip_asymptotics"),
      "N^2 = (M^2 + kappa^2 k^2 - (eps - v)^2) 1: branches exp(+-f Lambda y)",
      record=f"{PY_REPORT}, check bc_tip_asymptotics")
```

For both types: $N^\dagger\sigma_1 + \sigma_1N = 0$ (the current is constant), $N^\dagger + N \ne 0$ (the density is not), and $N^2 = (M^2 + \kappa^2k^2 - (\varepsilon - v)^2)\,1$ (the asymptotic branches). Out [3] shows the two printed coefficients and six PASS lines.

**In [4], the exact solutions and the record.**

```python
Lc = sp.symbols("L", positive=True)
n_int = sp.symbols("n", integer=True, positive=True)
ok_exact = sp.simplify(sp.diff(sp.exp(fs * M * y), y)
                       - fs * M * sp.exp(fs * M * y)) == 0  # step 5
```

A positive symbol $L$ and a positive whole number $n$; the first test is the zero mode: $a = e^{fMy}$ solves $a' = fMa$ (with $b = 0$ the second equation holds for $\varepsilon = 0$).

```python
for j in (1, -1):  # step 4: b = sin(n pi y/L), a = (b'/f + M b)/(j eps)
    p_n = n_int * sp.pi / (fs * Lc)
    eps_n = sp.sqrt(M ** 2 + p_n ** 2)
    b_n = sp.sin(n_int * sp.pi * y / Lc)
    a_n = (sp.diff(b_n, y) / fs + M * b_n) / (j * eps_n)
    ok_exact &= sp.simplify(sp.diff(a_n, y) - fs * (M * a_n - j * eps_n * b_n)) == 0
    ok_exact &= sp.simplify(sp.diff(b_n, y) - fs * (j * eps_n * a_n - M * b_n)) == 0
    ok_exact &= b_n.subs(y, 0) == 0 and sp.simplify(b_n.subs(y, -Lc)) == 0
```

The even levels of Section 14.13 for both types: with $p = n\pi/(fL)$, $\varepsilon = \sqrt{M^2 + p^2}$, $b = \sin(n\pi y/L)$ and $a = (b'/f + Mb)/(j\varepsilon)$, both equations of the real form hold, and $b$ vanishes at $0$ and at $-L$.

```python
p = sp.symbols("p", positive=True)  # step 6 (j = +1)
b_odd = sp.sin(fs * p * (y + Lc))
eps_odd = sp.sqrt(M ** 2 + p ** 2)
a_odd = (sp.diff(b_odd, y) / fs + M * b_odd) / eps_odd
ok_exact &= sp.simplify(sp.diff(a_odd, y) - fs * (M * a_odd - eps_odd * b_odd)) == 0
ok_exact &= sp.simplify(a_odd.subs(y, 0) * eps_odd
                        - (p * sp.cos(p * fs * Lc) + M * sp.sin(p * fs * Lc))) == 0
check(ok_exact and record_check("bc_exact_k0_spectra"),
      "the zero mode e^(fMy), the even levels and the odd condition tan(pfL) = -p/M",
      record=f"{PY_REPORT}, check bc_exact_k0_spectra")
```

The odd case: $b = \sin(fp(y + L))$ vanishes at the tip; with $a$ from the second equation the first holds, and $\varepsilon\,a(0) = p\cos(pfL) + M\sin(pfL)$, so $a(0) = 0$ is the condition $g(p) = 0$ of Section 14.13.

```python
BETA = 4.0 / 3.0  # the history b4 = b4(0) e^(beta a4) of the record

def hidden_scale(a4_value):
    return math.exp((0.5 * BETA - 1.0) * a4_value)
```

The hidden scale of a slice of the history, computed as the Rust solver computes it: with $b_{4,0} = e^{\beta a_{4,0}}$, $f = e^{-a_{4,0}}b_{4,0}^{1/2} = e^{(\beta/2 - 1)a_{4,0}}$; for $\beta = 4/3$ this is $e^{-a_{4,0}/3}$.

```python
def odd_roots(m, fL, count):
    roots = []
    for n in range(count):
        lo, hi = (n + 0.5) * math.pi / fL, (n + 1.0) * math.pi / fL
        g_ = lambda q: m * math.sin(q * fL) + q * math.cos(q * fL)
        g_lo = g_(lo)
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if mid <= lo or mid >= hi:  # the interval cannot shrink any more
                break
            if (g_(mid) > 0.0) == (g_lo > 0.0):
                lo = mid
            else:
                hi = mid
        roots.append(0.5 * (lo + hi))
    return roots
```

The first `count` roots of $g(p) = m\sin(pfL) + p\cos(pfL)$, each by bisection in its interval $((n + \tfrac12)\pi/(fL), (n + 1)\pi/(fL))$ of Section 14.13, where $g$ changes sign exactly once. The midpoint replaces the end at which $g$ has the same sign as at the midpoint (the comparison of two yes-or-no values with `==`); the loop stops when the midpoint can no longer be told apart from an end, that is at the resolution of floating-point numbers.

```python
def exact_level(m, L, a4_value, parity, label):
    fL = hidden_scale(a4_value) * L  # the proper length of the cut-off half
    if parity == "even":
        if label == 0:
            return 0.0
        return math.copysign(math.sqrt(m * m + (label * math.pi / fL) ** 2), label)
    roots = odd_roots(m, fL, 6)
    if label >= 0:
        return math.sqrt(m * m + roots[label] ** 2)
    return -math.sqrt(m * m + roots[-label - 1] ** 2)
```

The exact level of a fold condition and a label in the convention of Section 14.13: even label 0 is the zero mode, even label $l \ne 0$ is $\pm\sqrt{m^2 + (l\pi/(fL))^2}$ with the sign of $l$ (`math.copysign(x, l)`); odd label $l \ge 0$ is $+\sqrt{m^2 + p_l^2}$ and $l \le -1$ is $-\sqrt{m^2 + p_{-l-1}^2}$.

```python
CASES = [(1.0, 3.0, 0.0), (1.0, 2.0, 0.0), (2.0, 3.0, 0.0), (1.0, 3.0, 1.5)]
LABELS = list(range(-3, 6))  # the labels -3 ... 5
record_rows = repository_file(
    "Revision/kohn_sham/results/spectrum/free-k0-analytic.csv"
).read_text(encoding="utf-8").splitlines()
header = record_rows[0].split(",")
record = [dict(zip(header, row.split(","))) for row in record_rows[1:]]

def key_of(row):
    return (float(row["m"]), float(row["L"]), float(row["a4"]), row["parity"],
            int(row["label"]))
```

The four cases $(m, L, a_{4,0})$ of the record, the nine labels, and the record read as a list of dictionaries (as in Notebook 14a, In [18]); `key_of` makes the key $(m, L, a_{4,0}$, fold condition, label$)$ of a row, with the slice.

```python
exact = {}  # (m, L, a4, parity, label) -> exact level
for m_, L_, a_ in CASES:
    for label in LABELS:
        for parity in ("even", "odd"):
            exact[(m_, L_, a_, parity, label)] = exact_level(m_, L_, a_, parity,
                                                             label)
worst = max(abs(exact[key_of(r)] - float(r["eps_analytic"])) for r in record)
```

The 72 exact levels in a dictionary, and the largest difference from the record's column `eps_analytic`.

```python
for m_, L_, a_ in ((1.0, 3.0, 0.0), (1.0, 3.0, 1.5)):
    fL_ = hidden_scale(a_) * L_
    say(f"(m, L, a4,0) = ({m_:g}, {L_:g}, {a_:g}), fL = {fL_:.6f}: odd roots p = "
        + ", ".join(f"{q:.6f}" for q in odd_roots(m_, fL_, 3)) + ", ...")
lowest_odd = exact[(1.0, 3.0, 0.0, "odd", 0)]  # the lowest odd level, m = 1, L = 3
lowest_even = exact[(1.0, 3.0, 0.0, "even", 1)]  # the lowest positive even level
report("lowest odd level for m = 1, L = 3, a4,0 = 0", f"{lowest_odd:.12f}", "m")
report("lowest positive even level for m = 1, L = 3, a4,0 = 0",
       f"{lowest_even:.12f}", "m")
report("lowest odd and even levels at a4,0 = 1.5 (f = e^(-1/2))",
       f"{exact[(1.0, 3.0, 1.5, 'odd', 0)]:.12f}, "
       f"{exact[(1.0, 3.0, 1.5, 'even', 1)]:.12f}", "m")
check(len(record) == 72 and worst < 1e-12,
      "the 72 exact levels equal the column eps_analytic of the record",
      record="Revision/kohn_sham/results/spectrum/free-k0-analytic.csv, eps_analytic")
```

The format `:g` prints a number without needless zeros. Out [4]: at the slice 0, $fL = 3$ and the first odd roots are $0.818548$, $1.744313$, $2.734844$; at the slice 1.5, $fL = 1.819592$ and the roots are $1.236913$, $2.779599$, $4.438138$; the lowest odd level is $1.292292828069\,m$, the lowest positive even level $1.447971930402\,m$, and at the slice 1.5 they are $1.590582904485\,m$ and $1.995226701059\,m$. The PASS lines: the exact solutions, and the 72 exact levels equal to the record to $10^{-12}$.

**In [5], figure 1.**

```python
p_values = np.linspace(0.0, 7.0, 1401)
fig, ax = plt.subplots(figsize=(8.0, 4.0))
for a_, color in ((0.0, "C0"), (1.5, "C1")):
    fL_ = hidden_scale(a_) * 3.0
    ax.plot(p_values, 1.0 * np.sin(fL_ * p_values) + p_values * np.cos(fL_ * p_values),
            color=color, label=f"$a_{{4,0}} = {a_}$: $fL = {fL_:.4f}$")
    roots_ = odd_roots(1.0, fL_, 6)
    ax.plot([q for q in roots_ if q < 7.0], [0.0] * sum(q < 7.0 for q in roots_), "o",
            color=color)
```

For the two slices the function $g(p) = \sin(pfL) + p\cos(pfL)$ ($M = 1$, $L = 3$) on 1401 points from 0 to 7, and its roots below 7 as dots on the axis (`sum(q < 7.0 for q in roots_)` counts them, because a true comparison counts as 1).

```python
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("$p$ (wave number along $y$ per unit proper length, units of $H$)")
ax.set_ylabel("$g(p) = M\\sin(pfL) + p\\cos(pfL)$")
ax.set_title("the odd fold condition $\\tan(pfL) = -p/M$ for $M = 1$, $L = 3$")
ax.legend(fontsize=8, loc="lower left")
save_figure(fig, "odd_condition",
            ...)
```

**What figure 14b.1 shows.** Two oscillating curves whose swings grow with $p$ (the term $p\cos(pfL)$). The blue curve of the slice 0 crosses zero at $0.8185$, $1.7443$, $2.7348$, $3.7520$, $4.7811$ and $5.8163$ (the six dots; its next root, at $6.8551$, is not marked, because the cell computes six roots): one root in each interval of length $\pi/3$, always in its second half, as Section 14.13 proved. The orange curve of the slice 1.5 oscillates more slowly ($fL = 1.8196$ instead of 3) and its roots lie higher, at $1.2369$, $2.7796$, $4.4381$ and $6.1317$: a shorter hidden direction raises the odd levels.

**In [6], the Pruefer angle and the shooting tools.**

```python
r_s, t_s = sp.symbols("r t", positive=True)  # polar coordinates of (a, b)
a_p = r_s * sp.cos(t_s)
b_p = r_s * sp.sin(t_s)
j_s = sp.symbols("j")
num = (a_p * fs * ((j_s * e - K) * a_p - M * b_p)
       - b_p * fs * (M * a_p - (K + j_s * e) * b_p))  # a b' - b a'
pruefer = fs * (j_s * e - K * sp.cos(2 * t_s) - M * sp.sin(2 * t_s))
check(sp.simplify(num / r_s ** 2 - pruefer) == 0,
      "d theta/dy = f[j(eps - v) - K cos 2theta - M sin 2theta]")
```

The point $(a, b) = (r\cos\theta, r\sin\theta)$ with symbols $r$ and $\theta$ (`t_s`), a symbol $j$, the expression $ab' - ba'$ with the real form inserted (`num`, written with $v = 0$, so that $e$ stands for $\varepsilon - v$), and the claimed $\theta'$. The check: $(ab' - ba')/r^2$ equals it (Section 14.14).

```python
def shoot(eps, k=0.0, j=1.0, M=1.0, L=3.0, G=900, a4=0.0, tip=0.0, keep=False):
    eps, k, j = np.broadcast_arrays(np.asarray(eps, dtype=float),
                                    np.asarray(k, dtype=float),
                                    np.asarray(j, dtype=float))
```

`shoot` integrates the real form from the tip to the fold for many energies at once and returns $\Phi = j\theta(0)$. Its parameters have default values (the canonical $M = 1$, $L = 3$, $G = 900$, the slice 0, the tip angle 0), so a call names only what differs. `np.asarray` turns a single number or a list into a numpy array; `np.broadcast_arrays` brings the arrays to a common shape (a single number is repeated), so that `eps`, `k` and `j` may each be one number or an array of the same length.

```python
    f = hidden_scale(a4)  # the hidden scale of the slice
    kappa = math.exp(-a4)  # the momentum weight of the slice
    mass, K_, je = f * M, f * (k * kappa), f * j * eps  # the solver's coefficients
    h = L / G
```

The slice enters through $f$ and $\kappa$. The three coefficients of the real form multiplied by $f$, namely $fM$, $f\kappa k$ and $fj\varepsilon$, are formed once, in exactly the order of the operations of the Rust solver (the product $k\kappa$ first, then times $f$), so that the floating-point results agree to the last digits; $h = L/G$ is the step.

```python
    a_ = np.full(eps.shape, math.cos(0.5 * tip))  # the tip condition
    b_ = np.full(eps.shape, math.sin(0.5 * tip))
    theta = np.full(eps.shape, 0.5 * tip)
    raw = np.arctan2(b_, a_)
    path = [(theta, a_, b_)]
```

The starting point $(a, b) = (\cos\tfrac\theta2, \sin\tfrac\theta2)$ for every energy (`np.full(shape, value)` is an array filled with one value), the starting angle $\theta(-L)$, `raw`, the angle as `np.arctan2` returns it (between $-\pi$ and $\pi$), and a list that keeps the path when it is asked for.

```python
    for i in range(G):
        p1a, p1b = mass * a_ - (K_ + je) * b_, (je - K_) * a_ - mass * b_
        a2, b2 = a_ + 0.5 * h * p1a, b_ + 0.5 * h * p1b
        p2a, p2b = mass * a2 - (K_ + je) * b2, (je - K_) * a2 - mass * b2
        a3, b3 = a_ + 0.5 * h * p2a, b_ + 0.5 * h * p2b
        p3a, p3b = mass * a3 - (K_ + je) * b3, (je - K_) * a3 - mass * b3
        a4_, b4_ = a_ + h * p3a, b_ + h * p3b
        p4a, p4b = mass * a4_ - (K_ + je) * b4_, (je - K_) * a4_ - mass * b4_
        a_ = a_ + h / 6.0 * (p1a + 2.0 * p2a + 2.0 * p3a + p4a)
        b_ = b_ + h / 6.0 * (p1b + 2.0 * p2b + 2.0 * p3b + p4b)
```

One RK4 step per pass, for all energies at once. The four slopes of RK4 (Chapter 2): `p1` at the start, `p2` at the midpoint with half a step along `p1`, `p3` at the midpoint with half a step along `p2`, `p4` at the end with a whole step along `p3`; each slope is the right side of the real form, $(fMa - (f\kappa k + fj\varepsilon)b,\ (fj\varepsilon - f\kappa k)a - fMb)$, with $v = 0$. The new point adds $h/6$ times the weighted sum with the weights $1, 2, 2, 1$. (The name `a4_` with a final underscore is the trial point of the fourth slope; `a4` without it is the slice.) In the free problem the coefficients are the same at every $y$; the Rust solver stores them on the fine grid of nodes and midpoints because the self-consistent potentials change with $y$.

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

The value of $\Phi$ at a level: $l\pi$ for the even and $\pi/2 + l\pi$ for the odd fold condition, for arrays of conditions and labels.

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

say("defined: shoot(eps, k, j, M, L, G, a4, ...) and levels(k, j, parity, label, ...)")
```

The levels with given momenta, block types, fold conditions and labels, all at once, by 72 bisections of $[-20, 20]$ (Section 14.14). `**options` collects any further named arguments (for example `M=2.0`, `G=1800` or `a4=1.5`) and hands them on to `shoot`. In each pass $\Phi$ is computed at the midpoints; where it is at or below the target, the level lies above the midpoint and `lo` moves there; where it is at or above, `hi` moves there. If $\Phi$ equals the target exactly, both ends move to the midpoint and the level is found exactly; this is what happens for the zero mode (In [8]). Out [6]: the PASS line of the angle equation and the line defined: shoot(...).

**In [7], the shooting function and figure 2.**

```python
trial = np.linspace(-4.0, 4.0, 801)  # 801 trial energies
phi_curve = shoot(trial, 0.0, 1.0)  # Phi for k = 0, j = +1, slice 0
phi_late = shoot(trial, 0.0, 1.0, a4=1.5)  # the same at the slice 1.5
grows = bool(np.all(np.diff(phi_curve) > 0.0) and np.all(np.diff(phi_late) > 0.0))
grows_k = all(bool(np.all(np.diff(shoot(np.linspace(-4.0, 3.96, 200), 0.75, jj,
                                        a4=aa)) > 0))
              for jj in (1.0, -1.0) for aa in (0.0, 1.5))
check(grows and grows_k,
      "Phi(eps) grows strictly with eps (k = 0 and 0.75, both block types, 2 slices)")
```

$\Phi(\varepsilon)$ at 801 energies from $-4$ to $4$ in one call, at the slices 0 and 1.5. `np.diff` gives the differences of neighbouring values; `np.all(... > 0.0)` is true when every difference is positive, that is when $\Phi$ grows strictly; `bool` turns numpy's answer into a plain true or false. The same test for $k = 0.75$ with 200 energies, both block types and both slices. One PASS line: the monotonicity proved in Section 14.14, seen numerically.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
ax.plot(trial, phi_curve / np.pi, color="C0",
        label="$\\Phi(\\varepsilon)/\\pi$, $a_{4,0} = 0$")
ax.plot(trial, phi_late / np.pi, "--", color="C3",
        label="$\\Phi(\\varepsilon)/\\pi$, $a_{4,0} = 1.5$")
for label in range(-3, 4):  # the targets in units of pi
    ax.axhline(label, color="C1", linewidth=0.7)
    ax.axhline(label + 0.5, color="C2", linewidth=0.7, linestyle="--")
```

The two curves $\Phi/\pi$ and the targets: solid lines at the whole numbers (even), dashed lines at the half numbers (odd).

```python
even_levels = [exact[(1.0, 3.0, 0.0, "even", l)] for l in range(-2, 3)]
odd_levels = [exact[(1.0, 3.0, 0.0, "odd", l)] for l in range(-2, 2)]
ax.plot(even_levels, range(-2, 3), "o", color="C1",
        label="even levels: $\\Phi = l\\pi$")
ax.plot(odd_levels, [l + 0.5 for l in range(-2, 2)], "s", color="C2",
        label="odd levels: $\\Phi = \\pi/2 + l\\pi$")
ax.set_xlabel("trial energy $\\varepsilon$ (units of $m$)")
ax.set_ylabel("$\\Phi(\\varepsilon) / \\pi$")
ax.set_title("the shooting function for $k = 0$, $j = +1$, $m = 1$, $L = 3$")
ax.legend(fontsize=8, loc="upper left")
save_figure(fig, "shooting_function",
            ...)
```

The exact levels of the slice 0 with the labels $-2$ to $2$ (even) and $-2$ to $1$ (odd), drawn as circles and squares at the heights of their targets. **What figure 14b.2 shows.** The solid curve rises from about $-3.6$ to $+3.6$ (in units of $\pi$) as the trial energy goes from $-4$ to $4$, never falling. Every circle and square sits on the curve where it crosses its target line: the crossings are the levels, one per label. Between $-1$ and $1$ the curve is almost flat and crosses only the line $0$, at $\varepsilon = 0$: the gap $(-M, M)$ contains only the zero mode. The dashed curve of the slice 1.5 rises more slowly overall (it reaches only about $\pm2.2$; $\Phi$ grows like $f\varepsilon L$ with the smaller $fL = 1.82$), so it meets the targets at larger energies: the levels lie farther apart.

**In [8], all 72 levels.**

```python
numeric = {}  # (m, L, a4, parity, label) -> numerical level at the canonical step
pars = np.array([p_ for l_ in LABELS for p_ in ("even", "odd")])
labs = np.array([l_ for l_ in LABELS for p_ in ("even", "odd")])
for m_, L_, a_ in CASES:
    found = levels(0.0, 1.0, pars, labs, M=m_, L=L_, G=round(900 * L_ / 3), a4=a_)
    for p_, l_, x in zip(pars, labs, found):
        numeric[(m_, L_, a_, str(p_), int(l_))] = float(x)
```

`pars` and `labs` list the 18 pairs (fold condition, label) of one case. For each case the 18 levels are found in one call, with the step number of the Rust solver, $G = 900$ for $L = 3$ and $600$ for $L = 2$ (`round` gives the nearest whole number; the step is $h = 1/300$ in both), $k = 0$ and $j = +1$, and stored with their keys.

```python
say("m = 1, L = 3, a4,0 = 0:")
heads = ["even (numerical)", "even (exact)", "odd (numerical)", "odd (exact)"]
say("label  " + "  ".join(f"{text:>16}" for text in heads))
for l_ in LABELS:
    row = [numeric[(1.0, 3.0, 0.0, "even", l_)], exact[(1.0, 3.0, 0.0, "even", l_)],
           numeric[(1.0, 3.0, 0.0, "odd", l_)], exact[(1.0, 3.0, 0.0, "odd", l_)]]
    say(f"{l_:+5d}  " + "  ".join(f"{x:16.10f}" for x in row))
```

A table of the canonical case: a header line and one row per label with four columns 16 characters wide (`:>16` right-aligns a text, `:16.10f` prints a number with 10 decimals in 16 characters, `:+5d` a signed whole number in 5 characters). Out [8] shows, for example, the label $+1$: even $1.4479719304$ numerically and exactly, odd $2.0106285601$ numerically against $2.0106285600$ exactly; and the label $+5$: even $5.3306254627$ against $5.3306254587$, odd $5.9016800925$ against $5.9016800858$. The numerical and the exact levels agree to 10 decimals for the low levels; the high levels differ in the ninth decimal, the RK4 error.

```python
rust_diff = max(abs(numeric[key_of(r)] - float(r["eps_numeric"])) for r in record)
report("largest difference from the Rust solver's levels", f"{rust_diff:.1e}", "m")
check(rust_diff < 1e-11,
      "the 72 numerical levels equal those of the Rust solver",
      record="Revision/kohn_sham/results/spectrum/free-k0-analytic.csv, eps_numeric")
```

Out [8]: the largest difference from the Rust solver's numerical levels is $1.1\times10^{-14}$; both programs integrate the same RK4 discretisation and differ only in how they find the root and in the last rounding.

```python
errors = {key: abs(numeric[key] - exact[key]) for key in numeric}
low = max(err for key, err in errors.items() if abs(exact[key]) < 4.0)
high = max(err for key, err in errors.items() if abs(exact[key]) >= 4.0)
report("largest error for |eps| < 4 m", f"{low:.2e}", "m")
report("largest error for |eps| >= 4 m", f"{high:.2e}", "m")
import re  # regular expressions: patterns that find numbers in a text
```

The error of every numerical level against its exact value (a dictionary built by a **dictionary comprehension**), and the largest errors below and above $|\varepsilon| = 4m$: $7.23\times10^{-10}$ and $5.05\times10^{-8}$ (Out [8]). The module `re` finds patterns in texts.

```python
def record_detail(name, report_file):
    data = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
    return [c["detail"] for c in data["checks"] if c["name"] == name][0]

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

`record_detail` returns the text that explains a check of a report. The Rust check `free_k0_analytic_spectra` states its two largest errors and its two tolerances in that text; `re.findall` with the pattern `\d+(?:\.\d+)?e-\d+` (digits, optionally a decimal point and digits, then `e-` and digits) picks out the four numbers in the order they appear. The check: the notebook's errors, rounded to three digits, equal the recorded ones, and both lie below the tolerances $5\times10^{-9}$ and $3\times10^{-7}$.

```python
check(all(numeric[(m_, L_, a_, "even", 0)] == 0.0 for m_, L_, a_ in CASES),
      "the fold zero mode comes out as exactly eps = 0 in all four cases")
```

The zero mode is found as exactly $0$: at $\varepsilon = 0$ the shooting from $(1, 0)$ keeps $b = 0$ in every RK4 step, so $\Phi(0) = 0$ exactly, and the first bisection midpoint is $0$. Out [8] ends with three PASS lines.

**In [9], figure 3.**

```python
fig, ax = plt.subplots(figsize=(9.0, 5.0))
for position, (m_, L_, a_) in enumerate(CASES):
    x0 = 3.0 * position  # the horizontal place of this ladder
    for l_ in LABELS:
        for shift, parity, color, marker in ((0.0, "even", "C0", "o"),
                                             (1.2, "odd", "C1", "s")):
            level = exact[(m_, L_, a_, parity, l_)]
            ax.plot([x0 + shift - 0.4, x0 + shift + 0.4], [level, level],
                    color=color, linewidth=1.5)
            ax.plot([x0 + shift], [numeric[(m_, L_, a_, parity, l_)]], marker,
                    color=color, markersize=4)
    ax.fill_between([x0 - 0.5, x0 + 1.7], -m_, m_, color="gray", alpha=0.12)
```

One ladder per case, three units apart: every exact level is a short horizontal line (from `x0 + shift - 0.4` to `x0 + shift + 0.4`), the even ones on the left and the odd ones $1.2$ to the right, and the numerical level is a marker on it. `fill_between(x, low, high)` shades the gap from $-m$ to $m$.

```python
ax.set_xlim(-0.6, 11.4)
ax.set_ylim(-9.5, 10.5)
ax.set_xticks([0.6, 3.6, 6.6, 9.6])
ax.set_xticklabels(["$m = 1$, $L = 3$\n$a_{4,0} = 0$", "$m = 1$, $L = 2$\n$a_{4,0} = 0$",
                    "$m = 2$, $L = 3$\n$a_{4,0} = 0$",
                    "$m = 1$, $L = 3$\n$a_{4,0} = 1.5$"], fontsize=8)
ax.plot([], [], "o-", color="C0", label="even (line exact, dot numerical)")
ax.plot([], [], "s-", color="C1", label="odd (line exact, square numerical)")
ax.set_ylabel("level $\\varepsilon$ (units of $H = 1$)")
ax.set_title("the free $k = 0$ spectra, labels $-3$ to $5$")
ax.legend(fontsize=8, loc="lower right")
save_figure(fig, "spectrum_ladder",
            ...)
```

The ranges of the axes, the names of the four cases under the ladders (`\n` starts a new line), and two empty plots (`plot([], [])` draws nothing) that only give the legend its two entries. **What figure 14b.3 shows.** In every ladder the shaded gap contains only the zero mode at 0, and every marker sits on its line. The case $m = 2$ has the widest gap. The case $L = 2$ and the case of the slice 1.5 ($fL = 1.82$) have their levels farther apart than the canonical case ($fL = 3$): only the proper length $fL$ matters, and the case of the slice 1.5 has the widest spacing of all, its highest level near $9.6$.

**In [10], fourth-order convergence.**

```python
refined = {}
for m_, L_, a_ in CASES:
    found = levels(0.0, 1.0, pars, labs, M=m_, L=L_, G=round(1800 * L_ / 3), a4=a_)
    for p_, l_, x in zip(pars, labs, found):
        refined[(m_, L_, a_, str(p_), int(l_))] = float(x)
refined_errors = {key: abs(refined[key] - exact[key]) for key in refined}
```

The 72 levels again with twice the step number ($G = 1800$ for $L = 3$, $1200$ for $L = 2$), and their errors.

```python
as_in_record = {}  # keyed by (m, L, parity, label): later rows replace earlier ones
for r in record:
    as_in_record[(r["m"], r["L"], r["parity"], r["label"])] = key_of(r)
keys = list(as_in_record.values())
```

The keying of the Rust comparison program, without the slice: when a later row has the same $(m, L$, fold condition, label$)$, it replaces the earlier one in the dictionary. The rows of the case $(1, 3, 1.5)$ come after those of $(1, 3, 0)$ and replace them, so `keys` holds the 54 levels of the other three cases.

```python
def measurement(selected):
    ratios = sorted(errors[q] / refined_errors[q] for q in selected
                    if errors[q] > 1e-11 and refined_errors[q] > 0.0)
    return (len(ratios), ratios[len(ratios) // 2],
            max(errors[q] for q in selected), max(refined_errors[q] for q in selected))

count, median, worst_c, worst_r = measurement(keys)
count_all, median_all, _, _ = measurement(list(errors))
```

For a selection of levels: the ratios canonical error over refined error for the levels whose canonical error is above $10^{-11}$ (smaller errors are dominated by rounding), sorted; their number, the **median** (the middle value of the sorted list, at position `len // 2`; `//` divides and rounds down), and the largest errors at the two steps. It is computed for the record's 54 levels and for all 72 (`_` names a result that is not used).

```python
report("levels compared as in the record", len(keys))
report("number of levels with a canonical error above 1e-11", count)
report("median error ratio canonical / refined", f"{median:.2f}")
report("largest error, canonical step", f"{worst_c:.3e}", "m")
report("largest error, refined step", f"{worst_r:.3e}", "m")
report("over all 72 levels: levels above 1e-11, median ratio",
       f"{count_all}, {median_all:.2f}")
```

Out [10]: 54 levels compared, 39 of them above $10^{-11}$, the median ratio 16.00, the largest errors $5.050\times10^{-8}$ and $3.157\times10^{-9}$; over all 72 levels, 52 above $10^{-11}$ and again the median ratio 16.00.

```python
DETERMINISM = "Revision/kohn_sham/reports/ks-rust-determinism.json"
detail = record_detail("refined_free_spectra_convergence_order", DETERMINISM)
rec_canonical, rec_refined = re.search(r"canonical (\S+), refined (\S+);",
                                       detail).groups()
rec_median, rec_count = re.search(r"ratio (\S+) over (\d+) levels",
                                  detail).groups()
check(len(keys) == 54 and count == int(rec_count) and f"{median:.2f}" == rec_median
      and f"{worst_c:.3e}" == rec_canonical and f"{worst_r:.3e}" == rec_refined
      and record_check("refined_free_spectra_convergence_order", (DETERMINISM,)),
      f"{count} levels, median error ratio {median:.2f}, largest errors "
      f"{worst_c:.3e} and {worst_r:.3e}",
      record=f"{DETERMINISM}, check refined_free_spectra_convergence_order")
```

`re.search` finds the first place where a pattern matches, and `.groups()` returns the parts in round brackets (`\S+` is a run of characters without blanks). The four numbers of the record's detail text are compared with the notebook's, digit for digit. One PASS line.

**In [11], figure 4.**

```python
chosen = [("even", 1), ("even", 3), ("odd", 0), ("odd", 3)]
steps = [150, 300, 600, 900, 1800]
curves = {key: [] for key in chosen}
for G_ in steps:
    found = levels(0.0, 1.0, np.array([p_ for p_, l_ in chosen]),
                   np.array([l_ for p_, l_ in chosen]), M=1.0, L=3.0, G=G_)
    for key, x in zip(chosen, found):
        curves[key].append(abs(float(x) - exact[(1.0, 3.0, 0.0) + key]))
h_values = np.array([3.0 / G_ for G_ in steps])
```

Four levels of the canonical case at five step numbers; for each, the list of its errors (`(1.0, 3.0, 0.0) + key` joins two tuples into the key of the exact level). `h_values` are the steps $h = 3/G$.

```python
fig, ax = plt.subplots(figsize=(7.0, 4.6))
for (parity, label), errs in curves.items():
    ax.loglog(h_values, errs, "o-", label=f"{parity}, label {label}")
ax.loglog(h_values, 3e-2 * h_values ** 4, ":", color="black",
          label="slope 4: error $\\propto h^4$")
ax.set_xticks(h_values)  # one tick at each step used
ax.set_xticklabels([f"{x:.4f}" for x in h_values], fontsize=8)
ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())  # no extra ticks
ax.set_xlabel("RK4 step $h = L/G$ (units of $1/H$)")
ax.set_ylabel("$|\\varepsilon_{\\rm RK4} - \\varepsilon_{\\rm exact}|$ (units of $m$)")
ax.set_title("fourth-order convergence of the shooting method ($m = 1$, $L = 3$)")
ax.legend(fontsize=8)
```

`loglog` uses logarithmic scales on both axes, where a power law $\text{error} = c\,h^4$ is a straight line of slope 4; the dotted line $0.03\,h^4$ is drawn for comparison. The ticks are put at the five steps, and the small extra ticks of a logarithmic axis are switched off (`NullLocator`).

```python
fourth = all(12.0 < errs[i] / errs[i + 1] < 20.0 for errs in curves.values()
             for i in range(2))  # halving h from 0.02 to 0.005: ratios near 16
check(fourth, "halving the step divides each error by about 16 (between 12 and 20)")
save_figure(fig, "rk4_convergence",
            ...)
```

For the first two halvings of the step ($G = 150 \to 300 \to 600$) the error ratios must lie between 12 and 20 for all four levels. **What figure 14b.4 shows.** Four straight lines parallel to the dotted line of slope 4: halving the step divides every error by 16. The odd label 3 ($\varepsilon = 3.883$) has the largest errors, $9.4\times10^{-7}$ at $h = 0.02$ and $4.5\times10^{-11}$ at $h = 0.0017$; the even label 3 ($\varepsilon = 3.297$) follows, from $3.9\times10^{-7}$ to $1.9\times10^{-11}$; the even label 1 has $1.2\times10^{-9}$ to $5.8\times10^{-14}$ and the odd label 0 ($\varepsilon = 1.292$) the smallest, $2.6\times10^{-10}$ to $1.3\times10^{-14}$: the error grows steeply with the level, like $(fh\varepsilon)^4$.

**In [12], the orbitals.**

```python
def orbital(eps, k=0.0, j=1.0, M=1.0, L=3.0, G=900, a4=0.0, tip=0.0):
    _, (theta_n, a_n, b_n) = shoot(eps, k, j, M=M, L=L, G=G, a4=a4, tip=tip,
                                   keep=True)
    nf, h = 2 * G + 1, L / G
    y_fine = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))
    f = hidden_scale(a4)
    mass, K_, je = f * M, f * (k * math.exp(-a4)), f * j * eps
```

`orbital` shoots once with `keep=True` and takes the node values of $a$ and $b$. The fine grid has $2G + 1$ points from $-L$ to $0$ (`np.arange(nf)` is $0, 1, \dots, 2G$, so the first point is $-L$ and the last $0$); the three coefficients are formed as in `shoot`.

```python
    a_f, b_f = np.zeros(nf), np.zeros(nf)
    a_f[0::2], b_f[0::2] = a_n, b_n  # the node values
    da = mass * a_f - (K_ + je) * b_f  # the derivatives d/dy at the nodes
    db = (je - K_) * a_f - mass * b_f
    for i in range(1, nf, 2):  # cubic Hermite value at each midpoint
        a_f[i] = 0.5 * (a_f[i - 1] + a_f[i + 1]) + h / 8.0 * (da[i - 1] - da[i + 1])
        b_f[i] = 0.5 * (b_f[i - 1] + b_f[i + 1]) + h / 8.0 * (db[i - 1] - db[i + 1])
```

The node values go to the even positions of the fine grid (`[0::2]` is every second entry from the first). At the nodes the derivatives are known from the real form. At each midpoint the value of the cubic polynomial that matches the values and the derivatives at the two neighbouring nodes is the mean of the two values plus $h/8$ times the difference of the two derivatives (**cubic Hermite interpolation**, with an error of order $h^4$, like RK4). (The derivative entries at the midpoints, computed from the zeros there, are never used.)

```python
    weights = np.full(nf, 2.0)  # Simpson: 1, 4, 2, 4, ..., 4, 1 times (h/2)/3
    weights[1::2] = 4.0
    weights[0] = weights[-1] = 1.0
    weights *= 0.5 * h / 3.0
    norm = math.sqrt(float(np.sum(weights * (a_f ** 2 + b_f ** 2))))
    return y_fine, a_f / norm, b_f / norm, weights
```

**Simpson's rule** on the fine grid (spacing $h/2$): the integral of a function is approximately $(h/2)/3$ times the sum of its values with the weights $1, 4, 2, 4, \dots, 2, 4, 1$. The norm $\sqrt{\int(a^2 + b^2)\,dy}$ is computed with it, and the orbital is divided by it.

```python
zero_modes, deviation = {}, 0.0
for a_ in (0.0, 2.0):
    e0 = float(levels(0.0, 1.0, "even", 0, a4=a_))
    y_f, a_zero, b_zero, simpson = orbital(e0, a4=a_)
    fM = hidden_scale(a_) * 1.0
    a_exact = math.sqrt(2.0 * fM / (1.0 - math.exp(-2.0 * fM * 3.0))) * np.exp(fM * y_f)
    deviation = max(deviation, float(np.max(np.abs(a_zero - a_exact))))
    zero_modes[a_] = (e0, a_zero, b_zero, a_exact)
report("largest deviation of the zero-mode orbital from the exact one",
       f"{deviation:.1e}")
check(all(zero_modes[a_][0] == 0.0 and np.all(zero_modes[a_][2] == 0.0)
          for a_ in (0.0, 2.0))
      and deviation < 1e-9 and record_check("free_zero_mode_exact", (RUST_REPORT,)),
      "zero mode: eps = 0 and b = 0 exactly, a = sqrt(2fM/(1 - e^(-2fML))) e^(fMy)",
      record=f"{RUST_REPORT}, check free_zero_mode_exact")
```

At the slices 0 and 2 the zero mode is found, its orbital computed and compared with the exact $a = \sqrt{2fM/(1 - e^{-2fML})}\,e^{fMy}$ of Section 14.13. Out [12]: the largest deviation is $1.3\times10^{-12}$; the level is exactly 0 and $b$ is exactly 0 at every point, as the Rust check `free_zero_mode_exact` states.

```python
def exact_orbital(parity, label, m_=1.0, L_=3.0):
    level = exact[(m_, L_, 0.0, parity, label)]
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

The exact orbitals of Section 14.13 at the slice 0 ($f = 1$, $j = +1$): $p$ from the level, $b = \sin(py)$ (even) or $\sin(p(y + L))$ (odd), and $a = (b' + mb)/\varepsilon$; the sign is chosen so that $a(-L) > 0$, as the shooting from $(1, 0)$ gives, and the normalisation uses the same Simpson weights.

```python
shown = {}
worst_orbital = 0.0
for parity, label in (("even", 1), ("odd", 0)):
    _, a_num, b_num, _ = orbital(numeric[(1.0, 3.0, 0.0, parity, label)])
    a_ex, b_ex = exact_orbital(parity, label)
    worst_orbital = max(worst_orbital, float(np.max(np.abs(a_num - a_ex))),
                        float(np.max(np.abs(b_num - b_ex))))
    shown[(parity, label)] = (a_num, b_num, a_ex, b_ex)
check(worst_orbital < 1e-8,
      "the even label 1 and odd label 0 orbitals equal the exact ones to 1e-8")
```

The numerical orbitals of the even level 1 and the odd level 0 against the exact ones: the largest difference at any point of either component is below $10^{-8}$. Two PASS lines in all.

**In [13], figure 5.**

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.8), sharey=True)
for a_, style in ((0.0, "-"), (2.0, "-.")):
    e0, a_zero, b_zero, a_exact = zero_modes[a_]
    axes[0].plot(y_f, a_zero, style, color="C0",
                 label=f"$a$, $a_{{4,0}} = {a_:g}$")
    axes[0].plot(y_f[::60], a_exact[::60], ".", color="black")
axes[0].plot(y_f, zero_modes[0.0][2], "--", color="C1", label="$b = 0$")
axes[0].set_title("zero mode, $\\varepsilon = 0$", fontsize=9)
```

Three panels with a common vertical axis (`sharey=True`). The left one: the zero mode at the two slices (solid and dash-dotted), the exact values as black dots at every 60th point of the fine grid (`[::60]`), and $b = 0$.

```python
panels = [(f"even label 1, $\\varepsilon = {lowest_even:.4f}$",) + shown[("even", 1)],
          (f"odd label 0, $\\varepsilon = {lowest_odd:.4f}$",) + shown[("odd", 0)]]
for ax, (title, a_num, b_num, a_ex, b_ex) in zip(axes[1:], panels):
    ax.plot(y_f, a_num, color="C0", label="$a$ (numerical)")
    ax.plot(y_f, b_num, "--", color="C1", label="$b$ (numerical)")
    ax.plot(y_f[::60], a_ex[::60], ".", color="black", label="exact")
    ax.plot(y_f[::60], b_ex[::60], ".", color="black")
    ax.set_title(title, fontsize=9)
for ax in axes:
    ax.set_xlabel("$y$ (units of $1/H$)")
axes[0].set_ylabel("orbital component (normalised)")
axes[0].legend(fontsize=7, loc="upper left")
axes[1].legend(fontsize=7, loc="upper left")
save_figure(fig, "orbitals",
            ...)
```

The middle and right panels: the two components of the even level 1 and the odd level 0, numerical as lines and exact as dots. **What figure 14b.5 shows.** Left: the zero mode rises steeply toward the fold, from $0.07$ at the tip to $1.42$ at the fold at the slice 0; at the slice 2 ($f = e^{-2/3}$) it is flatter, from $0.22$ to $1.04$, and reaches farther toward the tip; $b = 0$ everywhere. Middle: the even level 1, $b$ (dashed) is a half sine wave vanishing at both ends, and $a$ falls from $0.42$ to $-0.42$ (the exact end values are $\pm p/(\varepsilon\sqrt3)$ with $p = \pi/3$ and $\varepsilon = 1.448$, because the norm of the exact orbital before normalisation is $\sqrt3$). Right: the odd level 0, $a$ vanishes at the fold and $b$ at the tip. In all panels the dots lie on the lines.

**In [14], figure 6.**

```python
picks = [("even", l_) for l_ in range(4)] + [("odd", l_) for l_ in range(3)]
energies = np.array([numeric[(1.0, 3.0, 0.0, p_, l_)] for p_, l_ in picks])
_, (theta_path, _, _) = shoot(energies, 0.0, 1.0, keep=True)
y_nodes = np.linspace(-3.0, 0.0, 901)
end_values = theta_path[-1] / np.pi
goals = np.array([l_ + (0.0 if p_ == "even" else 0.5) for p_, l_ in picks])
check(np.max(np.abs(end_values - goals)) < 1e-9,
      "the Pruefer angle ends on its target l pi or (l + 1/2) pi for every level")
```

Seven levels (even labels 0 to 3, odd labels 0 to 2) are shot once more with `keep=True`; `theta_path` has one row per node and one column per level, and its last row (`[-1]`) holds the end angles. The check: every end angle equals its target, in units of $\pi$, to $10^{-9}$.

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
for column, (p_, l_) in enumerate(picks):
    style = "-" if p_ == "even" else "--"
    ax.plot(y_nodes, theta_path[:, column] / np.pi, style,
            label=f"{p_}, label {l_}")
ax.set_xlabel("$y$ (units of $1/H$; tip cutoff at $-3$, fold at $0$)")
ax.set_ylabel("Pruefer angle $\\theta(y)/\\pi$")
ax.set_title("the Pruefer angle counts the half-turns ($m = 1$, $L = 3$, $k = 0$)")
ax.legend(fontsize=8, ncol=2, loc="upper left")
save_figure(fig, "pruefer_angle",
            ...)
```

`theta_path[:, column]` is the angle of one level along $y$. **What figure 14b.6 shows.** All seven curves start at $0$ at the tip and rise toward the fold, where each ends exactly on its target: $0, 1, 2, 3$ (even, solid) and $\tfrac12, \tfrac32, \tfrac52$ (odd, dashed). The zero mode stays at 0 all the way. The higher the level, the steeper the rise: the label counts the half-turns of the point $(a, b)$.

**In [15], the last check.**

```python
figure_names = ["14b_1_odd_condition.png", "14b_2_shooting_function.png",
                "14b_3_spectrum_ladder.png", "14b_4_rk4_convergence.png",
                "14b_5_orbitals.png", "14b_6_pruefer_angle.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all six figure files of this notebook exist")
all_checks_passed()
```

The six figure files must exist; the last line is ALL 20 CHECKS PASSED (notebook 14b). The 20 checks are: 1 in In [2], 6 in In [3], 2 in In [4], 1 in In [6], 1 in In [7], 3 in In [8], 1 in In [10], 1 in In [11], 2 in In [12], 1 in In [14] and 1 in In [15].

### 14.19 The fold band and its exact slope

**What happens when the 3-momentum is switched on.** At $k = 0$ the free spectrum has eight zero modes, four in the blocks of type $j = +1$ and four in those of type $j = -1$, all with the orbital $(e^{fMy}, 0)$, largest at the fold (Section 14.13). For $k \ne 0$ the momentum term $j\kappa k\,\sigma_3$ of $h_j$ moves them. In the blocks $j = +1$ the even level of label 0 rises with $k$: this is the **fold band**, because its orbital stays at the fold. In the blocks $j = -1$ the even level of label 0 falls by exactly the same amount, because $h_{-1} = -h_{+1}$ for $v = 0$ (Section 14.5): its levels are the negatives of those of $j = +1$, with the label $l$ of the even fold condition going to $-l$. (The record's files and checks still call the fold band by its earlier name, "brane band": `brane-band.csv`, `brane_band_slope`.)

**The band, exactly.** Take a constant mass $M > 0$, $v = 0$, any $k$, and try a solution with $b = 0$ everywhere. Line by line, from the real form of Section 14.12 with $K = \kappa k$:

$$
a' = f\big[Ma - (K + j\varepsilon)\cdot 0\big] = fMa, \qquad a = A\,e^{fMy} .
$$

Rule: put $b = 0$ into the first equation; the solution of $a' = ca$ is $Ae^{cy}$.

$$
0 = b' = f\big[(j\varepsilon - K)\,a - M\cdot 0\big] = f\,(j\varepsilon - \kappa k)\,A\,e^{fMy} .
$$

Rule: put $b = 0$ and the line above into the second equation; its left side is the derivative of $b = 0$.

$$
j\varepsilon = \kappa k, \qquad \varepsilon = j\kappa k .
$$

Rule: $f > 0$, $A \ne 0$ and $e^{fMy} > 0$, so the bracket must vanish; multiply by $j$ ($j^2 = 1$).

Both end conditions hold: $b(0) = 0$ is the even fold condition and $b(-L) = 0$ is the regular tip. So, for every 3-momentum $k$, every mass $M$, every cutoff $L$ and every slice, $\varepsilon = \kappa k$ in the blocks $j = +1$ (and $-\kappa k$ in the blocks $j = -1$) is an exact level, with the same orbital $(e^{fMy}, 0)$ as the zero mode, normalised by the constant $A = \sqrt{2fM/(1 - e^{-2fML})}$ of Section 14.13. Its point $(a, b)$ stays on the positive $a$ axis, so its Pruefer angle stays exactly 0 and its label is 0: it is the even level of label 0. The fold band is a straight line through the origin with the slope $\kappa = e^{-a_{4,0}}$. Status: PROVED (this derivation; Notebook 14c checks it with sympy, In [3]); the record states the same orbital and level (check free_rescaling_relation_and_band_monotone of `Revision/kohn_sham/reports/ks-rust-solver.json`: the Rust solver's band equals $\kappa k$ with the largest difference $0$ on $0 \le k \le 4$ at the slice 0).

**The slope again: the Hellmann-Feynman rule.** The slope can also be computed without knowing the band at every $k$, by a rule that Chapter 15 uses for many other quantities. Let $h(k)$ be a self-adjoint operator that depends on a number $k$, with boundary conditions that do not depend on $k$, and let $h(k)\chi = \varepsilon(k)\chi$ with $\int\chi^\dagger\chi\,dy = 1$. Line by line:

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

In words: the rate of change of a level is the expectation value of the rate of change of the operator. Now the band. Line by line:

$$
\frac{\partial h_j}{\partial k} = j\kappa\,\sigma_3 .
$$

Rule: in $h_j = j[-(i/f)\sigma_1\,d/dy + M\sigma_2 + \kappa k\sigma_3] + v$ only the last term contains $k$, and $\kappa$ is a number, the same at every $y$.

$$
\frac{d\varepsilon}{dk}\Big|_{k=0} = j\kappa\int_{-L}^{0}\chi^\dagger\sigma_3\chi\,dy = j\kappa\int_{-L}^{0}a^2\,dy = j\kappa .
$$

Rule: the Hellmann-Feynman rule at $k = 0$, where the orbital is the zero mode $\chi = (a, 0)$, so $\chi^\dagger\sigma_3\chi = a^2 - b^2 = a^2 = \chi^\dagger\chi$ (Section 14.12), and the normalisation $\int a^2\,dy = 1$.

So the slope of the band of type $j = +1$ is $c = \kappa = e^{-a_{4,0}}$, whatever $M$, $L$ and $f$: 1 at the slice 0, $e^{-1/2} = 0.6065306597$ at the slice 0.5. Status: PROVED; check brane_band_slope of `Revision/kohn_sham/reports/ks-theory-python.json` and of the Wolfram report, and the values braneBandSlope_a0 = 1 and braneBandSlope_a0_half_history $= e^{-1/2}$ under checksNumeric in `Revision/kohn_sham/ks-theory.json`; Notebook 14c repeats the integral with sympy (Out [5] prints the slope as `kappa`).

**What the band says.** Three things. (1) The band is exactly linear, $\varepsilon = \kappa k$, like the energy of a massless particle, although the mass $m$ is not zero: the mass term only holds the orbital at the fold, and the factor $e^{fMy}$ drops out of the level. (2) The slope is the momentum weight $\kappa$ itself, because $\kappa$ is the same at every point of the hidden direction: averaging it over the orbital gives $\kappa$, whatever the shape of the orbital. (3) Along the deflating history the slope shrinks like $e^{-a_{4,0}}$: $1$, $0.606530659712633$, $0.367879441171442$, $0.223130160148430$, $0.135335283236613$ at the five slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$.

**The slope measured numerically.** The band is an odd function of $k$: the relation $\sigma_3h_j(k)\sigma_3 = h_{-j}(-k)$ of Section 14.5 says that the level of $(j, k)$ equals the level of $(-j, -k)$ with the same label, and $h_{-1} = -h_{+1}$ says that the level of $(-1, k)$ with even label 0 is minus the level of $(+1, k)$ with even label 0; together $\varepsilon_{\rm band}(-k) = -\varepsilon_{\rm band}(k)$. So $R(k) = \varepsilon_{\rm band}(k)/k = c + dk^2 + \dots$ contains only even powers of $k$. The Revision solver used this to measure the slope without the exact solution: with $k_1 = 10^{-4}$ and $k_2 = 2\times10^{-4}$,

$$
\frac{4R(k_1) - R(k_2)}{3} = \frac{4(c + dk_1^2) - (c + 4dk_1^2)}{3} = c .
$$

Rule: $k_2 = 2k_1$, so $k_2^2 = 4k_1^2$, and the terms with $d$ cancel (**Richardson extrapolation**, Chapter 2; what remains is of order $k^4$; for the exactly linear band $d = 0$ anyway). The Rust solver found $c = e^{-a_{4,0}}$ at all five slices to $2.05\times10^{-16}$, relative (check free_brane_band_slope of `Revision/kohn_sham/reports/ks-rust-solver.json`; the values are in `Revision/kohn_sham/results/spectrum/brane-band-slope.csv`, with differences $0$ and $\pm2.8\times10^{-17}$ from $e^{-a_{4,0}}$). Notebook 14c repeats the measurement, prints the five numbers above (Out [5]) and finds the same slope for six other pairs of mass and cutoff, $(M, L) = (0.5, 3), (1, 1), (1, 2), (1, 4), (1, 6), (2, 3)$, at the slices 0 and 1: every value is $1.000000000000$ or $0.367879441171$. Status: COMPUTED.

**The other levels, exactly too.** The levels that are not on the band have an exact form as well. Keep $M$ and $v = 0$ constant. Then $N$ of Section 14.12 is a constant matrix with $N^2 = \Lambda^2\,1$, $\Lambda^2 = M^2 + \kappa^2k^2 - \varepsilon^2$ (Section 14.12), and the solution that starts at the tip is $\chi(y) = e^{fN(y + L)}\chi(-L)$. Line by line:

$$
e^{fNL} = \sum_{n \ge 0}\frac{(fNL)^n}{n!} = \sum_{n\ \rm even}\frac{(f\Lambda L)^n}{n!}\,1 + \sum_{n\ \rm odd}\frac{(f\Lambda L)^{n-1}}{n!}\,fLN = \cosh(f\Lambda L)\,1 + \frac{\sinh(f\Lambda L)}{\Lambda}\,N .
$$

Rule: the power series of the exponential of a matrix; $N^n = \Lambda^n\,1$ for even $n$ and $N^n = \Lambda^{n-1}N$ for odd $n$ (because $N^2 = \Lambda^2$); then the series of $\cosh$ and $\sinh$. (For $\Lambda^2 < 0$, $\Lambda = ip$ is imaginary and the two coefficients are the real numbers $\cos(fpL)$ and $\sin(fpL)/p$.)

$$
N(1,\ 0) = \big(M,\ i(j\varepsilon - \kappa k)\big) .
$$

Rule: the first column of $N = M\sigma_3 - \kappa k\sigma_2 + ij\varepsilon\sigma_1$, read from the Pauli matrices of Section 14.1 (columns written as rows, as in Section 14.12); the start $(1, 0)$ is the canonical tip.

$$
\chi_1(0) = \cosh(f\Lambda L) + M\,\frac{\sinh(f\Lambda L)}{\Lambda}, \qquad \chi_2(0) = i(j\varepsilon - \kappa k)\,\frac{\sinh(f\Lambda L)}{\Lambda} .
$$

Rule: $\chi(0) = e^{fNL}(1, 0)$ with the series formula above; the unit matrix keeps $(1, 0)$, and $N$ turns it into the column of the previous line.

- Even fold condition, $\chi_2(0) = 0$: either $j\varepsilon = \kappa k$ (the band) or $\sinh(f\Lambda L)/\Lambda = 0$, that is $\Lambda = ip$ with $fpL = n\pi$, $n = 1, 2, \dots$
- Odd fold condition, $\chi_1(0) = 0$: $\cosh(f\Lambda L) + M\sinh(f\Lambda L)/\Lambda = 0$, which for $\Lambda = ip$ is $\cos(fpL) + M\sin(fpL)/p = 0$, the condition $\tan(pfL) = -p/M$ of Section 14.13.

Away from the band, both conditions are conditions on $\Lambda^2$ alone, and $\Lambda^2 = M^2 + \kappa^2k^2 - \varepsilon^2$ contains $\varepsilon$ and $k$ only in the combination $\varepsilon^2 - \kappa^2k^2$. So $\varepsilon^2 - \kappa^2k^2$ has the same value at every $k$, namely its value $\varepsilon(0)^2$ at $k = 0$:

$$
\varepsilon(k) = \pm\sqrt{\varepsilon(0)^2 + \kappa^2k^2}, \qquad \varepsilon(0)^2 = M^2 + \Big(\frac{n\pi}{fL}\Big)^2 \ (\text{even}), \quad M^2 + p_n^2 \ (\text{odd}) .
$$

Rule: the levels of Section 14.13 at $k = 0$. This is the **relativistic dispersion** of a particle whose rest energy is the level at $k = 0$, and it is the same for $j = +1$ and $j = -1$. The classical RK4 method keeps it exactly as well: one step multiplies by a polynomial in $hfN$, which by $N^2 = \Lambda^2$ is again of the form $\alpha + \beta N$ with $\alpha$, $\beta$ depending on $\Lambda^2$ only, so the numerical conditions also depend on $\Lambda^2$ only. Notebook 14c checks this on the three recorded curves: the largest $|\varepsilon(k)^2 - \kappa^2k^2 - \varepsilon(0)^2|$ is $6.7\times10^{-15}$ (Out [3]). Status: PROVED (this derivation; it is not a separate check of the Revision record) and COMPUTED (Notebook 14c).

**The band at larger momenta.** The record `Revision/kohn_sham/results/spectrum/brane-band.csv` follows the band and three other levels from $k = 0$ to $k = 4$ at the slice 0 (the band of $j = +1$; the even level of label 1 of $j = +1$ and of $j = -1$; the odd level of label 0 of $j = +1$). At the first lattice shell, $k = \Delta k = 0.25$, the band is at exactly $0.25\,m$ and the odd level at $1.3162525417\,m = \sqrt{1.2922928281^2 + 0.25^2}\,m$ (Notebook 14c, Out [3]); at $k = 4$ the band is at $4\,m$. The lowest level that is not on the fold band at $k = 0$ is the odd level of label 0 at $1.2922928281\,m$ (Section 14.13), called the **bulk edge**; every other level starts at or above it and rises along its hyperbola (Figure 14c.1). Notebook 14c computes all 324 recorded levels and finds them equal to the record to $10^{-11}$. Status: COMPUTED.

### 14.20 The band along the deflating history, and the tip

**The redshift.** By the exact rescaling identity (Section 14.7) every free level at the slice $a_{4,0}$ equals the level at the slice 0 with the redshifted momentum and the proper cutoff: $\varepsilon(k, a_{4,0}; L) = \varepsilon(ke^{-a_{4,0}}, 0; f_0L)$ with $f_0 = e^{-a_{4,0}/3}$ (the constant $H$ does not enter the free levels). For the fold band this is the exact $\varepsilon = ke^{-a_{4,0}}$: the whole band turns down toward zero along the history, and at a later slice the same lattice momentum $k$ sits lower on it. The levels away from the band do the opposite: the proper length $f_0L$ of the cut-off half shrinks, so their rest energies grow; the lowest odd level at $k = 0$ rises from $1.292293\,m$ at the slice 0 to $1.735554\,m$ at the slice 2 (Notebook 14c, Out [7]; Figure 14c.3). The Rust solver checked the identity for the momenta $k = 0.25, 1, 2.5$, the five slices and four sectors, on the same number of RK4 steps, and found the two sides equal to $1.3\times10^{-15}$ (check free_rescaling_relation_and_band_monotone; the same check found the band strictly increasing on $0 \le k \le 4$); Notebook 14c repeats it and finds $8.9\times10^{-16}$ (Out [7]). Status: PROVED (the identity), COMPUTED (the checks).

**The gap of the eight zero modes along the history.** In the free state $N = 8$ the eight zero modes are filled, and the lowest empty particle level is the fold band at the first lattice shell, $k = \Delta k = 0.25$. Its level is the **gap** of the state, and by the exact band it is exactly $\kappa\Delta k = 0.25\,e^{-a_{4,0}}$:

| slice $a_{4,0}$ | gap of the free $N = 8$ state (units of $m$) |
| --- | --- |
| 0 | 0.2500000000000 |
| 0.5 | 0.1516326649282 |
| 1 | 0.0919698602929 |
| 1.5 | 0.0557825400371 |
| 2 | 0.0338338208092 |

(Notebook 14c, Out [7]; the rows $N = 8$ of `Revision/kohn_sham/results/spectrum/closed-shells.csv` and the column KS_gap of the free ground states N8_lam0_a00 to N8_lam0_a20 in `Revision/kohn_sham/results/ground/summary.csv`). As 3-space inflates, the lattice momenta are redshifted and the empty band levels come down toward the filled zero modes. Status: COMPUTED (and exact). (Chapter 15 asks whether the gas can follow this change: the adiabaticity of the history.)

**The tip angle: an exact identity.** The tip condition $(1 - Q(\theta))\chi(-L) = 0$ is a choice of the numerical model (Section 14.12). How much does the angle $\theta$ matter? Take the orbital $\chi_0$ of a level $\varepsilon_0$ with $\theta = 0$ and the orbital $\chi_\theta$ of the level $\varepsilon_\theta$ with the same label, the same $k$, $j$ and fold condition, and the tip angle $\theta$. Line by line:

$$
\int_{-L}^{0}\chi_0^\dagger h_j\chi_\theta\,dy - \int_{-L}^{0}(h_j\chi_0)^\dagger\chi_\theta\,dy = (\varepsilon_\theta - \varepsilon_0)\int_{-L}^{0}\chi_0^\dagger\chi_\theta\,dy .
$$

Rule: $h_j\chi_\theta = \varepsilon_\theta\chi_\theta$ and $(h_j\chi_0)^\dagger = \varepsilon_0\chi_0^\dagger$ (the level is real).

$$
(\varepsilon_\theta - \varepsilon_0)\int_{-L}^{0}\chi_0^\dagger\chi_\theta\,dy = -\frac{ij}{f}\Big[\chi_0^\dagger\sigma_1\chi_\theta\Big]_{y=-L}^{y=0} .
$$

Rule: the integrated boundary identity of Section 14.12 with $\varphi = \chi_0$ and $\chi = \chi_\theta$.

$$
\chi_0^\dagger\sigma_1\chi_\theta = i\,(a_0b_\theta - b_0a_\theta) .
$$

Rule: with $\chi = (a, ib)$ and real $a$, $b$: $\sigma_1\chi_\theta = (ib_\theta, a_\theta)$ and $\chi_0^\dagger = (a_0, -ib_0)$.

At the fold both orbitals obey the same fold condition, so both have $b(0) = 0$ or both have $a(0) = 0$, and the bracket vanishes there; at the tip $b_0(-L) = 0$ (the canonical condition). Hence

$$
(\varepsilon_\theta - \varepsilon_0)\int_{-L}^{0}\chi_0^\dagger\chi_\theta\,dy = -\frac{ij}{f}\big(0 - i\,a_0(-L)\,b_\theta(-L)\big) = -\frac{j}{f}\,a_0(-L)\,b_\theta(-L) .
$$

Rule: $(-i)(-i) = i^2 = -1$. Status: PROVED (this derivation, from the boundary identity of the check bc_self_adjoint_boundary_term); the Rust solver verified it on its 24 cases to $1.09\times10^{-12}$ (check free_tip_angle_boundary_identity), and Notebook 14c again to $1.1\times10^{-12}$ (Out [11]).

**What the identity says.** The overlap $\int\chi_0^\dagger\chi_\theta\,dy$ is close to 1 for a small change, so the shift of a level is set by the size of its orbital at the tip, $a_0(-L)$, times $b_\theta(-L)$, which is $\tan(\theta/2)$ times $a_\theta(-L)$ (the starting point $(\cos\tfrac\theta2, \sin\tfrac\theta2)$). For the fold band the orbital is $(Ae^{fMy}, 0)$, and at the tip

$$
a_0(-L)^2 = A^2e^{-2fML} = \frac{2fM\,e^{-2fML}}{1 - e^{-2fML}} ,
$$

its small tail (rule: the constant $A$ of Section 14.13); for $M = 1$, $L = 3$ it is $4.97\times10^{-3}$ at the slice 0 ($e^{-2fML} = e^{-6}$) and $3.27\times10^{-2}$ at the slice 1.5 ($f = e^{-1/2}$, $e^{-2fML} = e^{-3.64}$) (record: column fold_band_tail_2fM_exp of `tip-angle.csv`). To first order the band moves by about $-\tan(\theta/2)\,a_0(-L)^2/f$. Every other orbital is extended: nothing suppresses it toward the tip (Section 14.12), its value at the tip is not small, and its level moves a lot. The record `Revision/kohn_sham/results/spectrum/tip-angle.csv` lists the band and the even level of label 1 for $\theta = 0.5$ and $1$, $k = 0.25, 0.5, 1$, at the slices 0 and 1.5 (24 cases). At $k = 0.25$ and the slice 0 the band moves by $-1.35\times10^{-3}$ and $-3.13\times10^{-3}$, the level of label 1 by $-6.16\times10^{-2}$ and $-0.158$; over all cases the band moves by at most $3.26\times10^{-2}$ (at most 2.127 times the first-order estimate), the level of label 1 by at least $6.157\times10^{-2}$ (Notebook 14c, Out [11], reproducing the record). Figure 14c.5 follows the shifts at $k = 0.25$ for tip angles from 0.1 to 1.5. Status: COMPUTED. So the tip angle, a choice, changes the extended levels by several per cent of their value and the fold band by much less; at the later slice, where the hidden direction is shorter, the tail of the band is larger and so is its shift.

**The position $L$ of the cutoff (measured by the Revision record).** The angle is one question; where the cutoff sits is another. The Revision record measures it in `Revision/kohn_sham/tip_convergence/` (its README, "Answer in brief"; the report `Revision/kohn_sham/tip_convergence/tip-convergence.json`, 7 of 7 checks PASS, rerun for the corrected metric on 2026-10-17; summarised in `Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md`, section 5): $L = 3$ to $6$ in steps of $0.5$, with the step $h = 1/300$ of the record and every run repeated at $h/2$; a copy of the solver that reads $L$ from the environment reproduces the committed quick matrix byte for byte at $L = 3$, and the independent reference solver agrees at $L = 3$ and $4$. No notebook of this chapter repeats the study; its findings, with the record's numbers:

- The free states are exact fold-band gases: every occupied orbital of the free states $N = 8$ and $592$ (all slices) and $N = 2352$ at $a_{4,0} = 1, 2$ is the fold-band orbital $(e^{fmy}, 0)$ with $\varepsilon = \kappa|k|$, so their Kohn-Sham energy, highest occupied and lowest unoccupied levels and gap are the same at every $L$ (largest relative change $1.4\times10^{-17}$). Only the values at the fold depend on $L$, through the normalisation of the band orbital: $\rho(0; L) = \rho(0; \infty)/(1 - e^{-2fmL})$ exactly, so the recorded $L = 3$ fold values are high by 0.25%, 1.38% and 4.8% at $a_{4,0} = 0, 1, 2$.
- The $k = 0$ levels off the band converge only algebraically, like the levels of a box of proper length $fL$: $\varepsilon - m \approx (l\pi)^2/(2m(fL)^2)$ (for large $L$, from the exact levels of Section 14.13; the record verifies its 84 $k = 0$ levels against the exact formulas to $1.42\times10^{-10}\,m$). The bulk edge $1.2923\,m$ that defines $N = 2352$ (Section 14.21) is an $L = 3$ value: $1.0977\,m$ at $L = 6$, and $m$ as $L \to \infty$. The free $N = 2352$ ground state at $a_{4,0} = 0$ changes its occupied set from $L = 3.5$ on (its gap $0.01754$ closes), and its energy does not converge up to $L = 6$ ($2288.388$ at $L = 3$, $2245.486$ at $L = 6$).
- The interacting zero modes depend on $L$, the more the later the slice: their proper density grows toward the tip like $e^{(3H - 2fm)|y|}$ (Section 14.27). For $N = 8$ the recorded $E_{\rm KS}$ at the coupling $\pm\lambda_1$ is $\mp3.7787\times10^{-2}$ against $\mp3.8688\times10^{-2}$ at large $L$ at $a_{4,0} = 0$, $\mp1.4571\times10^{-2}$ against $\mp2.1622\times10^{-2}$ at $a_{4,0} = 1$ and $\mp6.980\times10^{-3}$ against $\mp3.239\times10^{-2}$ at $a_{4,0} = 2$; the interaction shifts of $N = 592$ and $2352$ at $a_{4,0} = 2$ are 4.6 to 4.7 times smaller at $L = 3$ than at large $L$. 17 of the 19 interacting states studied converge as $L$ grows; the self-consistent iteration fails only for $N = 2352$ at $a_{4,0} = 0$ (from $L = 3.5$ for $+\lambda_1$, from $L = 4.5$ for $-\lambda_1$), where $k = 0$ levels off the band are occupied (a failure of the iteration, not a proof that no self-consistent state exists).
- The record's rule for the couplings (Section 14.27), applied at each $L$, drives them toward zero: $\lambda_1 = 157.7$, $2.131$ and $0.5363$ at $L = 3$ ($N = 8$, $592$, $2352$), and $1.249$, $0.01687$ and $1.03\times10^{-5}$ at $L = 6$.

Status: COMPUTED by the Revision record with its two solvers (the $L$-dependence of the $k = 0$ levels and of the zero-mode density is exact and verified there). So the cutoff $L = 3$ is itself a choice that shapes the recorded numbers: not at all for the free fold-band gases away from the fold, decisively for the $k = 0$ levels off the band, for $N = 2352$ at $a_{4,0} = 0$ and for the interaction energy of the zero modes at the later slices. What the model gives in the limit of a distant cutoff is, where the record does not establish it, OPEN.

### 14.21 Particles, degeneracies and closed shells

**Lattice shells.** On the 3-torus the allowed momenta are $\mathbf k = \Delta k\,(n_1, n_2, n_3)$ with whole numbers $n_i$ (Section 14.3). All vectors with the same $n^2 = n_1^2 + n_2^2 + n_3^2$ have the same length $|\mathbf k| = \Delta k\sqrt{n^2}$ and form a **shell**; their number is written $r_3(n^2)$. For example $r_3(0) = 1$ (only $(0, 0, 0)$), $r_3(1) = 6$ (the six vectors $(\pm1, 0, 0)$, $(0, \pm1, 0)$, $(0, 0, \pm1)$) and $r_3(2) = 12$ (two entries $\pm1$ and one 0: three places for the 0 times four sign choices). The first values are $r_3 = 1, 6, 12, 8, 6, 24, 24, 12, 30$ for $n^2 = 0, 1, 2, 3, 4, 5, 6, 8, 9$; no vector has $n^2 = 7$, because the squares below 8 are 0, 1 and 4, and no three of them add up to 7.

**Degeneracy.** The levels depend on $|\mathbf k|$ only (Section 14.6), and the four blocks $(s_2, s_3)$ of one type have the same Hamiltonian (Section 14.5). So every level of the block type $j$ on the shell $n^2$ holds $4r_3(n^2)$ states: four blocks times $r_3(n^2)$ directions. Status: PROVED (the argument above; the record states it as blockEquation.degeneracy in `Revision/kohn_sham/ks-theory.json`).

**Particles and the sea (ASSUMED convention; its justification is OPEN).** The free spectrum has positive and negative levels. In the quantised theory (Chapter 10) the field is normal ordered: the negative levels form the filled **sea**, which is not counted, and the quanta that are counted, the **particles**, occupy the positive levels. The Revision theory adopts the following rule: in each sector (shell, block type, fold condition) the particle levels are those whose level in the free problem ($\lambda = 0$) is positive, together with the zero modes at $k = 0$, each followed continuously when the interaction is switched on; the sea contributes nothing to the particle number and the densities. The zero modes need a decision: at $k = 0$ and $v = 0$ the spectrum of $h_{+1}$ is minus that of $h_{-1}$, so a level at exactly zero is its own mirror image and the sign does not decide whether it is a particle or a sea level. Counting it as a particle level is a stated CONVENTION of the record (ks-theory.json, thermodynamics.fillingConvention; `Revision/kohn_sham/results/parameters.json`, conventions.filling), and its justification is OPEN. (The words particle and sea are used here in this technical sense only; nothing in this chapter is a statement about matter and antimatter, which Chapter 21 treats.)

Because $\Phi$ grows with $\varepsilon$ (Section 14.14), the particle levels of a sector are exactly the labels $l \ge l_{\min}$, where $l_{\min}$ is the first label whose target lies above $\Phi(0)$, the value of the shooting function at $\varepsilon = 0$ (and at $k = 0$, even fold condition, the zero mode has $\Phi(0) = 0$ exactly on the target of label 0). The Rust solver verified this for every shell $n^2 \le 30$ and every sector, and found that the level closest to zero, apart from the zero modes, is $0.2500\,m$: the fold band at the first shell (check free_particle_branch_labels); Notebook 14c repeats both (Out [13]). Status: COMPUTED.

**Closed shells.** The **aufbau** (German for building up) fills the particle states from the lowest level upward. A particle number $N$ is a **closed shell** when the filling ends exactly at the end of a group of degenerate levels (levels equal within $10^{-9}$), so that the state is unique. At the slice 0 the first closed shells are built like this (record `Revision/kohn_sham/results/spectrum/closed-shells.csv`, reproduced by Notebook 14c, Out [14]):

| $N$ | the last group filled | states added | its level (units of $m$) |
| --- | --- | --- | --- |
| 8 | the zero modes, both block types | $4 + 4 = 8$ | 0 |
| 32 | the fold band on the shell $n^2 = 1$ | $4 \times 6 = 24$ | 0.25 |
| 80 | the fold band on the shell $n^2 = 2$ | $4 \times 12 = 48$ | 0.3535533906 |
| 112 | the fold band on the shell $n^2 = 3$ | $4 \times 8 = 32$ | 0.4330127019 |
| 136 | the fold band on the shell $n^2 = 4$ | $4 \times 6 = 24$ | 0.5 |
| 232 | the fold band on the shell $n^2 = 5$ | $4 \times 24 = 96$ | 0.5590169944 |

Each level is $0.25\sqrt{n^2}$, the band $\kappa|\mathbf k|$ at $\kappa = 1$. Only the fold band of the blocks $j = +1$ appears on the shells $n^2 \ge 1$ in this table: the band of the blocks $j = -1$ is negative (sea), and every other level lies above the bulk edge. The list of closed shells at the slice 0 continues $328, 376, 496, 592, 688, 720, \dots, 2064, 2352$ (Out [14]); there are 56 closed shells up to the energy $1.6\,m$. The shell $N = 2360$ is the first that fills a level off the fold band: the odd level of label 0 at $k = 0$ in both block types (8 states), at the bulk edge $1.2922928281\,m$.

**The particle numbers of the Revision runs.** The Revision solver chose its three particle numbers by a rule fixed in advance (record `Revision/kohn_sham/results/parameters.json`, particleNumbers): $N = 8$, the zero modes; $N_{\rm large}$, the largest closed shell of the slice 0 whose last filled level lies below the bulk edge (the lowest level not on the fold band: the smaller of the odd level of label 0 and the even level of label 1 at $k = 0$), which is 2352, the fold band on the shell $n^2 = 26$ at $1.2747548784\,m$; and $N_{\rm mid}$, the closed shell nearest to $N_{\rm large}/4 = 588$, which is 592 (4 away; the fold band on the shell $n^2 = 10$). Status: COMPUTED; Notebook 14c repeats the rule and finds 8, 592, 2352 (Out [14]). The rule is applied at the cutoff $L = 3$: the bulk edge is an $L = 3$ value ($1.0977\,m$ at $L = 6$), so $N = 2352$ is itself an $L = 3$ choice (Section 14.20).

**At a later slice.** At the slice $a_{4,0} = 0.5$ the redshifted band holds many more states below the same energy: 123 closed shells up to $1.6\,m$ instead of 56 (Notebook 14c, Out [14]; Figure 14c.6).

### 14.22 Example: Notebook 14c, the fold band

Notebook 14c does Sections 14.19 to 14.21 with the computer, with the shooting method of Notebook 14b, now also for nonzero 3-momenta, any slice and any tip angle. It checks the exact band with sympy, computes the band and three other levels for $k$ from 0 to 4 and compares 324 levels with the Rust record, checks that shooting exactly at $\varepsilon = \kappa k$ leaves the Pruefer angle at 0 and that the other levels obey the relativistic dispersion; it derives the slope with sympy and measures it by Richardson extrapolation at the five slices and for six other masses and cutoffs; it checks the rescaling relation for 60 levels and the gap of the state $N = 8$ at the five slices; it checks the two block-type symmetries; it computes the 24 levels of the tip-angle record and verifies the exact boundary identity on each; and it builds the lattice shells, the particle labels, the closed shells at the slices 0 and 0.5 and the particle numbers of the Revision runs, all against the Rust records. It draws six figures and needs no Rust. It runs in about two minutes (the cells of its sections 6, 10 and 11 integrate the equation for hundreds of energies at once, 72 times over, and take 10 to 40 seconds each), and its last line is ALL 16 CHECKS PASSED (notebook 14c).

<!-- NOTEBOOK 14c -->

### 14.25 Line-by-line walk-through of Notebook 14c

The notebook has 16 code cells, In [1] to In [16]. Docstrings and the long caption texts are again left out of the quotations; the captions are printed under the figures in Section 14.24.

**In [1], the set-up cell.** The code of In [1] of Notebook 14a (Section 14.11), line for line, except

```python
NOTEBOOK_ID = "14c"  # this notebook: chapter 14, example c
```

so that the figure files start with 14c and the captions go into `Revision/textbook/figures/14c.captions.json`. Its comment lines are the run instructions of Section 14.23. Out [1] is the line Set-up of notebook 14c complete.

**In [2], the tools.**

```python
import math  # exp, cos, sin of single numbers

import numpy as np  # floating-point arrays
import sympy as sp  # exact algebra with symbols

RUST_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
SPECTRUM = "Revision/kohn_sham/results/spectrum"  # the folder of the records
BETA = 4.0 / 3.0  # the history b4 = b4(0) e^(beta a4) of the record
```

The modules (Section 14.18), the Rust report, the folder of the spectrum records, and the exponent $\beta = 4/3$ of the history $b_4 = e^{\beta a_4}$.

```python
def record_check(name, report=RUST_REPORT):
    data = json.loads(repository_file(report).read_text(encoding="utf-8"))
    return [c["verdict"] for c in data["checks"] if c["name"] == name] == ["PASS"]

def read_csv(relative):
    lines = repository_file(relative).read_text(encoding="utf-8").splitlines()
    header = lines[0].split(",")
    return [dict(zip(header, line.split(","))) for line in lines[1:]]
```

`record_check` is true when the report has exactly one check of that name and its verdict is PASS (the list of verdicts must equal the list `["PASS"]`). `read_csv` reads a record table as a list of dictionaries, one per row, from column name to the text of the cell (Notebook 14a, In [18]).

```python
def hidden_scale(a4):
    return np.exp((0.5 * BETA - 1.0) * np.asarray(a4, dtype=float))
```

The hidden scale $f = e^{(\beta/2 - 1)a_{4,0}} = e^{-a_{4,0}/3}$ of a slice of the history (Notebook 14b, In [4]), here for a single slice or an array of slices.

```python
def shoot(eps, k=0.0, j=1.0, a4=0.0, M=1.0, L=3.0, G=900, tip=0.0, keep=False):
    eps, k, j, a4, tip = np.broadcast_arrays(*(np.asarray(x, dtype=float)
                                               for x in (eps, k, j, a4, tip)))
    f = hidden_scale(a4)  # the hidden scale of each slice
    mass, K_, je = f * M, f * (k * np.exp(-a4)), f * j * eps  # f M, f kappa k, f j eps
    h = L / G
    a_ = np.cos(0.5 * tip)  # the tip condition (a, b) = (cos(theta/2), sin(theta/2))
    b_ = np.sin(0.5 * tip)
    theta = 0.5 * tip
    raw = np.arctan2(b_, a_)
    path = [(theta, a_, b_)]
```

The shooting function of Notebook 14b (In [6], explained there line by line), with one generalisation: the slice `a4` and the tip angle `tip` may be arrays too, so that one call integrates many energies at many slices with many tip angles at once. `np.broadcast_arrays(*(...))` brings all five inputs to one common shape (the star hands the five arrays over as separate arguments). The coefficients are formed as in the Rust solver: $fM$, $f(k\kappa)$ and $fj\varepsilon$ with $\kappa = e^{-a_{4,0}}$.

```python
    for i in range(G):
        p1a, p1b = mass * a_ - (K_ + je) * b_, (je - K_) * a_ - mass * b_
        a2, b2 = a_ + 0.5 * h * p1a, b_ + 0.5 * h * p1b
        p2a, p2b = mass * a2 - (K_ + je) * b2, (je - K_) * a2 - mass * b2
        a3, b3 = a_ + 0.5 * h * p2a, b_ + 0.5 * h * p2b
        p3a, p3b = mass * a3 - (K_ + je) * b3, (je - K_) * a3 - mass * b3
        a4_, b4_ = a_ + h * p3a, b_ + h * p3b
        p4a, p4b = mass * a4_ - (K_ + je) * b4_, (je - K_) * a4_ - mass * b4_
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

The RK4 steps and the continuous Pruefer angle, exactly as in Notebook 14b.

```python
def target(parity, label):
    offset = np.where(np.asarray(parity) == "even", 0.0, 0.5 * np.pi)
    return offset + np.asarray(label, dtype=float) * np.pi

def levels(k, j, parity, label, a4=0.0, tip=0.0, iterations=72, **options):
    k, j, parity, label, a4, tip = np.broadcast_arrays(
        np.asarray(k, dtype=float), np.asarray(j, dtype=float), np.asarray(parity),
        np.asarray(label), np.asarray(a4, dtype=float), np.asarray(tip, dtype=float))
    goal = target(parity, label)
    lo, hi = np.full(k.shape, -20.0), np.full(k.shape, 20.0)
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        g = shoot(mid, k, j, a4, tip=tip, **options) - goal
        lo = np.where(g <= 0.0, mid, lo)
        hi = np.where(g >= 0.0, mid, hi)
    return 0.5 * (lo + hi)
```

The targets and the bisection of Notebook 14b, again with arrays of slices and tip angles allowed.

```python
def orbital(eps, k=0.0, j=1.0, a4=0.0, M=1.0, L=3.0, G=900, tip=0.0):
    _, (_, a_n, b_n) = shoot(eps, k, j, a4, M=M, L=L, G=G, tip=tip, keep=True)
    nf, h = 2 * G + 1, L / G
    y_fine = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))
    f = float(hidden_scale(a4))
    mass, K_, je = f * M, f * (k * math.exp(-a4)), f * j * eps
    a_f, b_f = np.zeros(nf), np.zeros(nf)
    a_f[0::2], b_f[0::2] = a_n, b_n
    da = mass * a_f - (K_ + je) * b_f
    db = (je - K_) * a_f - mass * b_f
    for i in range(1, nf, 2):  # cubic Hermite values at the midpoints
        a_f[i] = 0.5 * (a_f[i - 1] + a_f[i + 1]) + h / 8.0 * (da[i - 1] - da[i + 1])
        b_f[i] = 0.5 * (b_f[i - 1] + b_f[i + 1]) + h / 8.0 * (db[i - 1] - db[i + 1])
    weights = np.full(nf, 2.0)  # Simpson weights 1, 4, 2, ..., 4, 1 times (h/2)/3
    weights[1::2] = 4.0
    weights[0] = weights[-1] = 1.0
    weights *= 0.5 * h / 3.0
    norm = math.sqrt(float(np.sum(weights * (a_f ** 2 + b_f ** 2))))
    return y_fine, a_f / norm, b_f / norm, weights

SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]  # the slices of the Revision solver
say("defined: shoot, levels, orbital, read_csv, record_check")
```

The normalised orbital of Notebook 14b (In [12]), with the tip angle as a further parameter, and the five slices. Out [2] is the line defined: shoot, levels, orbital, read_csv, record_check.

**In [3], the band and three other levels.**

```python
ys, fs, Ms, ks, kaps = sp.symbols("y f M k kappa", real=True)
a_band = sp.exp(fs * Ms * ys)  # the orbital (a, b) = (e^(fMy), 0)
exact_ok = True
for j in (1, -1):
    eps_band = j * kaps * ks  # the level j kappa k
    exact_ok &= sp.simplify(sp.diff(a_band, ys)
                            - fs * (Ms * a_band - (kaps * ks + j * eps_band) * 0)) == 0
    exact_ok &= sp.simplify(0 - fs * ((j * eps_band - kaps * ks) * a_band - Ms * 0)) == 0
check(exact_ok, "(e^(fMy), 0) solves the block equation with eps = j kappa k exactly")
```

The derivation of Section 14.19 with symbols: for both block types, $a = e^{fMy}$, $b = 0$ and $\varepsilon = j\kappa k$ make both equations of the real form hold (the written factors `* 0` are the places where $b = 0$ enters, so that the two lines are visibly the real form).

```python
k_list, kk = [], 0.0
while kk <= 4.0 + 1e-12:  # 0, 0.05, 0.10, ... as the Rust program makes them
    k_list.append(kk)
    kk += 0.05
k_band = np.array(k_list)
```

The 81 momenta $0, 0.05, \dots, 4$, made by adding $0.05$ again and again, as the Rust program makes them; a `while` loop repeats its body as long as its condition holds. Because $0.05$ has no exact binary representation, the repeated additions give slightly different last digits than $0.05\,n$ would, and the check below compares the momenta with those of the record to $10^{-15}$.

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

The five curves: the four of the record and, for the figure, the band of the blocks $j = -1$. `np.concatenate` joins arrays end to end, so `K_all`, `J_all`, `P_all` and `L_all` list $5 \times 81 = 405$ cases; one call of `levels` finds all of them, and `reshape(5, 81)` cuts the result into five rows, which are then named.

```python
rows = read_csv(f"{SPECTRUM}/brane-band.csv")
record = np.array([[float(r[c]) for r in rows] for c in
                   ("eps_band_a0", "eps_band_bulk_even_l1", "eps_odd_l0",
                    "eps_jm1_even_l1")])
k_record = np.array([float(r["k"]) for r in rows])
say(f"k = 0.25: fold band {band[5]:.13f}, odd level {odd0[5]:.10f} (units of m)")
check(len(rows) == 81 and np.max(np.abs(k_record - k_band)) < 1e-15
      and np.max(np.abs(found[:4] - record)) < 1e-11,
      "the 324 levels equal the record brane-band.csv",
      record=f"{SPECTRUM}/brane-band.csv")
```

The record's four columns as a $4 \times 81$ array and its momenta. Out [3] prints the two levels at $k = 0.25$ (position 5): the band $0.2500000000000$ and the odd level $1.3162525417$. The check: 81 rows, the same momenta, and the first four computed curves (`found[:4]`) equal to the record to $10^{-11}$.

```python
phi_on_band = shoot(k_band, k_band, 1.0)  # Phi at eps = kappa k (kappa = 1)
report("largest |eps - kappa k| of the band from bisection",
       f"{np.max(np.abs(band - k_band)):.1e}", "m")
check(np.all(phi_on_band == 0.0) and np.max(np.abs(band - k_band)) < 1e-14
      and bool(np.all(np.diff(band) > 0.0))
      and np.max(np.abs(minus_band + band)) < 1e-14
      and record_check("free_rescaling_relation_and_band_monotone"),
      "Phi(kappa k) = 0 exactly: the band is eps = kappa k, rising; j = -1 has -eps",
      record=f"{RUST_REPORT}, check free_rescaling_relation_and_band_monotone")
```

Shooting exactly at $\varepsilon = \kappa k$ ($\kappa = 1$ at the slice 0): the point $(a, b)$ starts at $(1, 0)$, every RK4 slope has $b$-component $(j\varepsilon - K)a - Mb = 0$, so $b$ stays exactly 0 and $\Phi = 0$ exactly, for all 81 momenta. The bisection therefore lands exactly on $\kappa k$: Out [3] prints the largest difference $0.0$. The check adds that the band rises strictly and that the band of $j = -1$ is its negative.

```python
drift = max(np.max(np.abs(x ** 2 - k_band ** 2 - x[0] ** 2))
            for x in (bulk_even, odd0, minus_even1))  # kappa = 1 at this slice
report("largest |eps(k)^2 - (kappa k)^2 - eps(0)^2| of the other three levels",
       f"{drift:.1e}", "m^2")
check(drift < 1e-12 and np.max(np.abs(bulk_even - minus_even1)) < 1e-12,
      "the other levels obey eps(k)^2 = eps(0)^2 + (kappa k)^2; label 1 of j = -1 too")
```

The relativistic dispersion of Section 14.19: for each of the three other curves `x`, `x[0]` is its value at $k = 0$ and $\varepsilon(k)^2 - k^2 - \varepsilon(0)^2$ must vanish; Out [3] prints $6.7\times10^{-15}$ (rounding). The even levels of label 1 of the two block types must be equal. Out [3] shows four PASS lines.

**In [4], figure 1.**

```python
fig, ax = plt.subplots(figsize=(9.5, 4.8))
ax.plot(k_band, band, color="C0", linewidth=2,
        label="fold band ($j = +1$, even, 0): $\\varepsilon = \\kappa k$")
ax.plot(k_band, bulk_even, color="C1", label="$j = +1$, even, label 1")
ax.plot(k_band, odd0, color="C2", label="$j = +1$, odd, label 0")
ax.plot(k_band, minus_even1, color="C4", label="$j = -1$, even, label 1")
ax.plot(k_band, minus_band, "--", color="C0",
        label="$j = -1$, even, label 0 (sea): $-\\kappa k$")
ax.axhline(odd0[0], color="gray", linewidth=0.8, linestyle="-.")
ax.annotate("bulk edge 1.2923", (2.6, odd0[0] - 0.55), fontsize=8,
            color="gray")  # just below the dash-dotted line
ax.set_xlabel("3-momentum $k$ (units of $H$), slice $a_{4,0} = 0$ ($\\kappa = 1$)")
ax.set_ylabel("level $\\varepsilon$ (units of $m$)")
ax.set_title("the free levels at nonzero 3-momentum ($m = 1$, $L = 3$)")
ax.legend(fontsize=7, loc="center left", bbox_to_anchor=(1.01, 0.5))
save_figure(fig, "band_structure",
            ...)
```

Five curves, the bulk edge as a dash-dotted horizontal line at the odd level of $k = 0$ with its name written just below it, and the legend placed to the right of the panel (`bbox_to_anchor=(1.01, 0.5)` puts its left middle just outside the right edge). **What figure 14c.1 shows.** The thick fold band is the straight line from $(0, 0)$ to $(4, 4)$; its sea partner is the dashed mirror line below. The three other curves start at the bulk edge $1.2923$ (odd) and at $1.4480$ (even, label 1) and rise along hyperbolas that approach the slope 1 for large $k$, always above the band: $\sqrt{\varepsilon(0)^2 + k^2} > k$. The orange curve of $j = +1$ is hidden under the purple one of $j = -1$, because the two are equal.

**In [5], the slope.**

```python
f_p, M_p, L_p = sp.symbols("f M L", positive=True)
s3 = sp.Matrix([[1, 0], [0, -1]])  # sigma3
zero_mode = sp.Matrix([sp.exp(f_p * M_p * ys), 0])  # (a, 0), not yet normalised
expect_s3 = (zero_mode.T * s3 * zero_mode)[0]  # chi^dag sigma3 chi = a^2
norm_sq = (zero_mode.T * zero_mode)[0]  # chi^dag chi = a^2
slope = sp.simplify(kaps * sp.integrate(expect_s3, (ys, -L_p, 0))
                    / sp.integrate(norm_sq, (ys, -L_p, 0)))  # step 3
```

The Hellmann-Feynman slope of Section 14.19 with symbols: the zero mode $(e^{fMy}, 0)$, not normalised, the two integrands $\chi^\dagger\sigma_3\chi$ and $\chi^\dagger\chi$ (for a real column the transpose `.T` is the conjugate transpose), and the slope $\kappa\int\chi^\dagger\sigma_3\chi\,dy/\int\chi^\dagger\chi\,dy$ (dividing by the norm normalises). `sp.integrate(expr, (ys, -L_p, 0))` integrates from $-L$ to 0; positive symbols $f$, $M$, $L$ let sympy evaluate the integrals in closed form.

```python
theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                    .read_text(encoding="utf-8"))
numbers = theory["checksNumeric"]
report("slope c of the fold band (exact)", f"{slope}")
check(slope == kaps and float(numbers["braneBandSlope_a0"]) == 1.0
      and abs(float(numbers["braneBandSlope_a0_half_history"]) - math.exp(-0.5))
      < 1e-15
      and record_check("brane_band_slope",
                       "Revision/kohn_sham/reports/ks-theory-python.json"),
      "c = kappa = e^(-a4,0) for every M, L, f (1 at the slice 0)",
      record="Revision/kohn_sham/ks-theory.json, checksNumeric braneBandSlope_a0 "
             "and braneBandSlope_a0_half_history")
```

Out [5] prints the slope as `kappa`: the two integrals are equal and cancel. The check compares with the two recorded values (1 at the slice 0, $e^{-1/2}$ at the slice 0.5) and with the verdict of the sympy check `brane_band_slope`.

```python
tiny = np.array([1e-4, 2e-4] * 5)  # two small momenta at each slice
slice_of = np.repeat(SLICES, 2)
small = levels(tiny, 1.0, "even", 0, a4=slice_of).reshape(5, 2)
c_numeric = (4.0 * small[:, 0] / 1e-4 - small[:, 1] / 2e-4) / 3.0
rows = read_csv(f"{SPECTRUM}/brane-band-slope.csv")
c_rows = np.array([float(r["c_numeric"]) for r in rows])
for a_, c_ in zip(SLICES, c_numeric):
    say(f"slice a4,0 = {a_}: c numerical {c_:.15f}, e^(-a4,0) {math.exp(-a_):.15f}")
check(np.max(np.abs(c_numeric / c_rows - 1.0)) < 1e-11
      and np.max(np.abs(c_numeric / np.exp(-np.array(SLICES)) - 1.0)) < 1e-11
      and record_check("free_brane_band_slope"),
      "the numerical slope equals e^(-a4,0) at all five slices",
      record=f"{SPECTRUM}/brane-band-slope.csv and {RUST_REPORT}, check "
             "free_brane_band_slope")
```

The numerical slope as the Rust solver measured it: the band at $k = 10^{-4}$ and $2\times10^{-4}$ at each slice (`[1e-4, 2e-4] * 5` repeats the pair five times, `np.repeat(SLICES, 2)` repeats each slice twice), and the Richardson combination of Section 14.19 for each row. Out [5] prints the five values next to $e^{-a_{4,0}}$, equal in all 15 printed decimals; the check compares them with the record to $10^{-11}$ relative.

```python
cases = [(M_, L_, a_) for a_ in (0.0, 1.0) for M_, L_ in
         ((0.5, 3.0), (1.0, 1.0), (1.0, 2.0), (1.0, 4.0), (1.0, 6.0), (2.0, 3.0))]
c_cases = []
for M_, L_, a_ in cases:
    pair = levels(np.array([1e-4, 2e-4]), 1.0, "even", 0, a4=a_, M=M_, L=L_,
                  G=round(300 * L_))
    c_cases.append((4.0 * pair[0] / 1e-4 - pair[1] / 2e-4) / 3.0)
worst_case = max(abs(c_ / math.exp(-a_) - 1.0) for c_, (_, _, a_) in
                 zip(c_cases, cases))
say("slopes for (M, L) = (0.5, 3), (1, 1), (1, 2), (1, 4), (1, 6), (2, 3):")
say("  slice 0: " + ", ".join(f"{c_:.12f}" for c_ in c_cases[:6]))
say("  slice 1: " + ", ".join(f"{c_:.12f}" for c_ in c_cases[6:]))
check(worst_case < 1e-11, "the slope is e^(-a4,0) for other masses and cutoffs too")
```

Six pairs of mass and cutoff at the slices 0 and 1, each with the step $h = 1/300$ ($G = 300L$). Out [5]: all twelve slopes are $1.000000000000$ or $0.367879441171$: the slope does not depend on the mass or the cutoff. Three PASS lines in all.

**In [6], figure 2.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
a_grid = np.linspace(0.0, 2.0, 201)
left.semilogy(a_grid, np.exp(-a_grid), color="C0",
              label="exact $c = \\kappa = e^{-a_{4,0}}$")
left.semilogy(SLICES, c_numeric, "o", color="C3", label="numerical (Richardson)")
left.set_xlabel("slice $a_{4,0}$")
left.set_ylabel("slope $c$ (units of $m/H$, logarithmic)")
left.set_title("the slope along the history")
left.legend(fontsize=8)
```

Left: the exact slope as a line on a logarithmic axis and the five numerical values as dots.

```python
names = [f"$M = {M_:g}$\n$L = {L_:g}$" for M_, L_, _ in cases[:6]]
positions = np.arange(6)
right.bar(positions - 0.2, c_cases[:6], width=0.38, label="slice $a_{4,0} = 0$")
right.bar(positions + 0.2, c_cases[6:], width=0.38, label="slice $a_{4,0} = 1$")
right.axhline(1.0, color="C0", linestyle=":", linewidth=0.8)
right.axhline(math.exp(-1.0), color="C1", linestyle=":", linewidth=0.8)
right.set_xticks(positions)
right.set_xticklabels(names, fontsize=7)
right.set_ylabel("slope $c$ (units of $m/H$)")
right.set_title("the slope for six masses and cutoffs")
right.legend(fontsize=8)
save_figure(fig, "band_slope",
            ...)
```

Right: one pair of bars per $(M, L)$, the slices 0 and 1, with dotted lines at $1$ and $e^{-1}$. **What figure 14c.2 shows.** Left: the dots lie on the straight line (slope $-1$ on the logarithmic axis), from 1 to $0.135$. Right: all six left bars reach the dotted line 1 and all six right bars the dotted line $e^{-1} = 0.368$: the slope is the momentum weight, whatever the mass and the cutoff.

**In [7], the rescaling relation and the gap of $N = 8$.**

```python
test_k = [0.25, 1.0, 2.5]
test_sectors = [(1.0, "even", 0), (1.0, "odd", 0), (-1.0, "even", 1),
                (1.0, "even", 1)]
worst_partner = 0.0
for a_ in SLICES:
    combos = [(k_, s_) for k_ in test_k for s_ in test_sectors]
    args = (np.array([s_[0] for _, s_ in combos]), np.array([s_[1] for _, s_ in combos]),
            np.array([s_[2] for _, s_ in combos]))
    at_slice = levels(np.array([k_ for k_, _ in combos]), *args, a4=a_)
    partner = levels(np.array([k_ * math.exp(-a_) for k_, _ in combos]), *args,
                     a4=0.0, L=float(hidden_scale(a_)) * 3.0, G=900)
    worst_partner = max(worst_partner, float(np.max(np.abs(at_slice - partner))))
report("largest difference between a slice and its partner", f"{worst_partner:.1e}",
       "m")
```

For each slice, 12 combinations of momentum and sector: the levels at the slice, and the levels of the partner at the slice 0 with the momentum $ke^{-a_{4,0}}$ and the proper cutoff $f_0L$, on the same number $G = 900$ of RK4 steps (so the step is $f_0h$ in proper length on both sides). `*args` hands the three arrays of block types, fold conditions and labels over as three arguments. Out [7]: the largest difference over the 60 pairs is $8.9\times10^{-16}$.

```python
gaps = levels(np.full(5, 0.25), 1.0, "even", 0, a4=np.array(SLICES))
shells_record = read_csv(f"{SPECTRUM}/closed-shells.csv")
gap_record = [float(r["gap"]) for r in shells_record if r["N_closed"] == "8"]
summary = read_csv("Revision/kohn_sham/results/ground/summary.csv")
gap_summary = [float(r["KS_gap"]) for r in summary if r["id"].startswith("N8_lam0_")]
for a_, g_ in zip(SLICES, gaps):
    say(f"slice a4,0 = {a_}: gap of the free N = 8 state {g_:.13f} m, "
        f"0.25 e^(-a4,0) = {0.25 * math.exp(-a_):.13f}")
check(worst_partner < 1e-12 and len(gap_record) == 5 and len(gap_summary) == 5
      and np.max(np.abs(gaps - np.array(gap_record))) < 1e-13
      and np.max(np.abs(gaps - np.array(gap_summary))) < 1e-13
      and np.max(np.abs(gaps - 0.25 * np.exp(-np.array(SLICES)))) < 1e-15,
      "eps(k, a4,0; L) = eps(k e^(-a4,0), 0; f0 L); the N = 8 gap is 0.25 e^(-a4,0)",
      record=f"{SPECTRUM}/closed-shells.csv (N_closed = 8) and "
             "Revision/kohn_sham/results/ground/summary.csv, KS_gap of N8_lam0")
```

The gap of the free $N = 8$ state at each slice is the band at $k = 0.25$; the record has it twice, as the column gap of the rows $N = 8$ of `closed-shells.csv` and as the Kohn-Sham gap of the free ground states N8_lam0_a00 to N8_lam0_a20 of `ground/summary.csv` (`startswith` tests the beginning of a name). Out [7] prints the five gaps, equal to $0.25\,e^{-a_{4,0}}$ in all 13 printed decimals (the table of Section 14.20), and the check compares them with both record files.

```python
k_fig = np.linspace(0.0, 2.0, 21)
band_slices = levels(np.tile(k_fig, 5), 1.0, "even", 0,
                     a4=np.repeat(SLICES, len(k_fig))).reshape(5, len(k_fig))
a_dense = np.linspace(0.0, 2.0, 21)
edge_odd = levels(np.zeros(21), 1.0, "odd", 0, a4=a_dense)  # bulk levels at k = 0
edge_even = levels(np.zeros(21), 1.0, "even", 1, a4=a_dense)
say(f"lowest odd level at k = 0: {edge_odd[0]:.6f} m at a4,0 = 0, "
    f"{edge_odd[-1]:.6f} m at a4,0 = 2")
```

For figure 3: the band at 21 momenta and five slices in one call (`np.tile(k_fig, 5)` repeats the whole array five times, `np.repeat` each slice 21 times), and the two lowest levels off the band at $k = 0$ at 21 slices. Out [7] ends with the line lowest odd level at k = 0: 1.292293 m at a4,0 = 0, 1.735554 m at a4,0 = 2.

**In [8], figure 3.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
for index, a_ in enumerate(SLICES):
    left.plot(k_fig, band_slices[index], label=f"$a_{{4,0}} = {a_}$")
left.set_xlabel("3-momentum $k$ (units of $H$)")
left.set_ylabel("fold band $\\varepsilon$ (units of $m$)")
left.set_title("the fold band at five slices")
left.legend(fontsize=8)
right.semilogy(a_dense, edge_even, color="C1", label="$k = 0$, even, label 1")
right.semilogy(a_dense, edge_odd, color="C2", label="$k = 0$, odd, label 0")
right.semilogy(a_grid, 0.25 * np.exp(-a_grid), color="C0",
               label="gap of $N = 8$: $\\kappa \\Delta k$")
right.semilogy(SLICES, gaps, "o", color="C0", markersize=4)
right.set_xlabel("slice $a_{4,0}$")
right.set_ylabel("level (units of $m$, logarithmic)")
right.set_title("the band falls, the bulk rises")
right.legend(fontsize=8)
save_figure(fig, "band_redshift",
            ...)
```

**What figure 14c.3 shows.** Left: five straight lines through the origin, the slope $e^{-a_{4,0}}$ falling from 1 to $0.135$; at $k = 2$ the band lies at $2$, $1.21$, $0.74$, $0.45$ and $0.27$. Right, on a logarithmic axis: the gap $\kappa\Delta k$ falls in a straight line from $0.25$ to $0.034$, with the five computed gaps as dots on it, while the two lowest levels off the band rise, the odd one from $1.29$ to $1.74$ and the even one from $1.45$ to about $2.27$: the band and the bulk move apart along the history.

**In [9], the block-type symmetries.**

```python
sym_k = [0.25 * math.sqrt(n2) for n2 in (0, 1, 2, 5, 9)]
sym_l = list(range(-3, 4))
grid = [(k_, l_) for k_ in sym_k for l_ in sym_l]
K_s = np.array([k_ for k_, l_ in grid])
L_s = np.array([l_ for k_, l_ in grid])
plus_even = levels(K_s, 1.0, "even", L_s)
minus_even = levels(K_s, -1.0, "even", -L_s)
plus_odd = levels(K_s, 1.0, "odd", L_s)
minus_odd = levels(K_s, -1.0, "odd", -L_s - 1)
flipped_even = levels(-K_s, -1.0, "even", L_s)
flipped_odd = levels(-K_s, -1.0, "odd", L_s)
```

Five shells and seven labels give 35 combinations. For the mirror relation $h_{-1} = -h_{+1}$ the label of $j = -1$ that belongs to the label $l$ of $j = +1$ is $-l$ for the even fold condition (the targets $l\pi$ and $-l\pi$ are mirror images) and $-l - 1$ for the odd one (the targets $\pi/2 + l\pi$ and $\pi/2 + (-l - 1)\pi = -(\pi/2 + l\pi)$ are mirror images). For the relation $\sigma_3h_j(k)\sigma_3 = h_{-j}(-k)$ the label stays and the momentum changes sign.

```python
mirror = max(np.max(np.abs(plus_even + minus_even)),
             np.max(np.abs(plus_odd + minus_odd)))
flip = max(np.max(np.abs(flipped_even - plus_even)),
           np.max(np.abs(flipped_odd - plus_odd)))
check(mirror < 1e-12 and flip < 1e-12 and record_check("free_block_type_symmetries"),
      "spec h_(-1) = -spec h_(+1) and eps_(-1)(-k) = eps_(+1)(k), label by label",
      record=f"{RUST_REPORT}, check free_block_type_symmetries")
```

The mirrored levels must add to zero, and the flipped ones must be equal, to $10^{-12}$.

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

For figure 4, the even levels with the labels $-2$ to $2$ of both block types at 41 momenta (`reshape(5, -1)`: five rows, the length of each row worked out by numpy). Out [9] prints them at $k = 2$: for $j = +1$ $-3.0637, -2.4691, 2.0000, 2.4691, 3.0637$, for $j = -1$ $-3.0637, -2.4691, -2.0000, 2.4691, 3.0637$. The band is $\pm2$; the others are $\pm\sqrt{1 + 4 + (n\pi/3)^2}$ with $n = 1, 2$, the dispersion of Section 14.19.

**In [10], figure 4.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
for row, label in enumerate(fig_labels):
    left.plot(k_mirror, plus_curves[row], label=f"label {label}")
    right.plot(k_mirror, minus_curves[row], label=f"label {label}")
for ax, title in ((left, "block type $j = +1$"), (right, "block type $j = -1$")):
    ax.axhline(0.0, color="black", linewidth=0.6)
    ax.set_xlabel("3-momentum $k$ (units of $H$)")
    ax.set_title(title + ", even fold condition")
    ax.legend(fontsize=7, loc="upper left")
left.set_ylabel("level $\\varepsilon$ (units of $m$)")
save_figure(fig, "block_type_mirror",
            ...)
```

**What figure 14c.4 shows.** Left ($j = +1$): two rising hyperbolas above $1.448$ and $2.32$ (labels 1 and 2), their mirror images below $-1.448$ and $-2.32$ (labels $-1$ and $-2$), and the straight band from 0 to 2 (label 0). Right ($j = -1$): the same four hyperbolas and the band falling from 0 to $-2$. Reflecting the left picture in the line $\varepsilon = 0$ gives the right one (with the labels $l \to -l$); because the hyperbolas are symmetric already, only the band visibly changes.

**In [11], the tip angle.**

```python
tip_rows = read_csv(f"{SPECTRUM}/tip-angle.csv")
rows_a = np.array([float(r["a4"]) for r in tip_rows])  # the 24 cases of the record
rows_k = np.array([float(r["k"]) for r in tip_rows])
rows_l = np.array([int(r["label"]) for r in tip_rows])
rows_t = np.array([float(r["theta_tip"]) for r in tip_rows])
e0_all = levels(rows_k, 1.0, "even", rows_l, a4=rows_a)  # tip angle 0
eth_all = levels(rows_k, 1.0, "even", rows_l, a4=rows_a, tip=rows_t)  # angle theta
```

The 24 cases of the record (two slices, three momenta, two labels, two angles) as arrays, and their levels with the canonical tip and with the tip angle of the case, each set in one call.

```python
worst_level, worst_identity = 0.0, 0.0
band_shift, ratio_max, bulk_shift = 0.0, 0.0, float("inf")
for r, a_, k_, label, th, e0, e_th in zip(tip_rows, rows_a, rows_k, rows_l, rows_t,
                                           e0_all, eth_all):
    f_ = float(hidden_scale(a_))
    _, a0_, b0_, w_ = orbital(float(e0), k_, 1.0, a_)
    _, at_, bt_, _ = orbital(float(e_th), k_, 1.0, a_, tip=th)
    overlap = float(np.sum(w_ * (a0_ * at_ + b0_ * bt_)))
    boundary = -a0_[0] * bt_[0] / f_  # -j a_0(-L) b_theta(-L)/f with j = +1
    worst_identity = max(worst_identity, abs((e_th - e0) * overlap - boundary))
    worst_level = max(worst_level, abs(e_th - float(r["eps"])))
```

For each case the two normalised orbitals, their overlap $\int\chi_0^\dagger\chi_\theta\,dy = \int(a_0a_\theta + b_0b_\theta)\,dy$ (Simpson weights `w_`), and the two sides of the boundary identity of Section 14.20 (`a0_[0]` and `bt_[0]` are the values at $y = -L$, the first point of the grid). `float("inf")` is infinity, the start of a running minimum.

```python
    tail = 2.0 * f_ * math.exp(-6.0 * f_) / (1.0 - math.exp(-6.0 * f_))  # a_0(-L)^2
    if label == 0:
        band_shift = max(band_shift, abs(e_th - e0))
        ratio_max = max(ratio_max, abs(e_th - e0) / (math.tan(0.5 * th) * tail / f_))
    else:
        bulk_shift = min(bulk_shift, abs(e_th - e0))
```

The tail $a_0(-L)^2 = 2fMe^{-2fML}/(1 - e^{-2fML})$ with $M = 1$, $L = 3$ ($2fML = 6f$); for the band the largest shift and its largest ratio to the first-order estimate, for the level of label 1 the smallest shift.

```python
report("largest shift of the fold band", f"{band_shift:.2e}", "m")
report("largest ratio to the first-order estimate", f"{ratio_max:.3f}")
report("smallest shift of the extended level (label 1)", f"{bulk_shift:.3e}", "m")
report("largest residual of the boundary identity", f"{worst_identity:.1e}")
check(len(tip_rows) == 24 and worst_level < 1e-11 and worst_identity < 1e-9
      and record_check("free_tip_angle_boundary_identity"),
      "the 24 levels equal tip-angle.csv and obey the exact boundary identity",
      record=f"{SPECTRUM}/tip-angle.csv and {RUST_REPORT}, check "
             "free_tip_angle_boundary_identity")
```

Out [11]: the band moves by at most $3.26\times10^{-2}$, at most 2.127 times the first-order estimate; the level of label 1 moves by at least $6.157\times10^{-2}$; the identity holds to $1.1\times10^{-12}$. The check: the 24 levels equal the record to $10^{-11}$ and the identity holds to $10^{-9}$.

```python
import re  # regular expressions: patterns that find numbers in a text

detail = [c["detail"] for c in json.loads(repository_file(RUST_REPORT).read_text(
    encoding="utf-8"))["checks"] if c["name"] == "free_tip_angle_boundary_identity"][0]
rec_band = re.search(r"shifts by at most (\S+),", detail).group(1)
rec_ratio = re.search(r"at most (\S+) times", detail).group(1)
rec_bulk = re.search(r"shifts by at least (\S+):", detail).group(1)
check(f"{band_shift:.2e}" == f"{float(rec_band):.2e}" and f"{ratio_max:.3f}" == rec_ratio
      and f"{bulk_shift:.3e}" == f"{float(rec_bulk):.3e}",
      f"band shift at most {band_shift:.2e}, extended level at least {bulk_shift:.3e}",
      record=f"{RUST_REPORT}, check free_tip_angle_boundary_identity (detail)")
```

The three numbers of the record's detail text are found with patterns (`.group(1)` is the part in the first round brackets) and compared digit for digit, each number turned into a floating-point number and printed again in the same format, so that the record's way of writing exponents (`3.26e-2`) and Python's (`3.26e-02`) do not matter.

```python
thetas = np.linspace(0.1, 1.5, 15)
shift_curves = {}
for a_ in (0.0, 1.5):
    for label in (0, 1):
        reference = float(levels(0.25, 1.0, "even", label, a4=a_))
        shift_curves[(a_, label)] = np.abs(
            levels(0.25, 1.0, "even", label, a4=a_, tip=thetas) - reference)
```

For figure 5: at $k = 0.25$, for the band and the level of label 1 at the slices 0 and 1.5, the shifts for 15 tip angles from 0.1 to 1.5. Two PASS lines in all.

**In [12], figure 5.**

```python
for (a_, label), values in shift_curves.items():
    say(f"slice {a_}, label {label}: shift {values[0]:.2e} m at theta = 0.1, "
        f"{values[-1]:.2e} m at theta = 1.5")
```

`items()` returns the pairs (key, value) of a dictionary; each key is a pair (slice, label), unpacked in the `for` line. Out [12] prints the shifts at the smallest and the largest angle of each curve: at the slice 0 the band moves by $2.52\times10^{-4}$ at $\theta = 0.1$ and $5.97\times10^{-3}$ at $\theta = 1.5$, the level of label 1 by $1.05\times10^{-2}$ and $0.325$; at the slice 1.5 the band moves by $2.71\times10^{-3}$ and $5.15\times10^{-2}$, the level of label 1 by $2.16\times10^{-2}$ and $0.497$ (all in units of $m$).

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
for a_, color in ((0.0, "C0"), (1.5, "C3")):
    f_ = float(hidden_scale(a_))
    tail = 2.0 * f_ * math.exp(-6.0 * f_) / (1.0 - math.exp(-6.0 * f_))
    ax.semilogy(thetas, shift_curves[(a_, 0)], "o-", color=color, markersize=4,
                label=f"fold band, $a_{{4,0}} = {a_}$")
    ax.semilogy(thetas, np.tan(0.5 * thetas) * tail / f_, ":", color=color,
                label=f"first-order estimate, $a_{{4,0}} = {a_}$")
    ax.semilogy(thetas, shift_curves[(a_, 1)], "s--", color=color, markersize=4,
                label=f"label 1 (extended), $a_{{4,0}} = {a_}$")
ax.set_xlabel("tip angle $\\theta$ (radians)")
ax.set_ylabel("$|\\varepsilon_\\theta - \\varepsilon_0|$ (units of $m$, logarithmic)")
ax.set_title("the tip angle moves the extended levels, the fold band little")
ax.legend(fontsize=7, loc="lower right")
save_figure(fig, "tip_angle",
            ...)
```

For each slice three curves: the band shift (circles), its first-order estimate $\tan(\theta/2)\,a_0(-L)^2/f$ (dotted) and the shift of the level of label 1 (squares). **What figure 14c.5 shows.** All four computed curves rise with the angle. At the slice 0 the band moves least, and the estimate follows it closely for small angles and falls below it by about a fifth at $\theta = 1.5$; the extended level moves about 40 times as much as the band at $\theta = 0.1$. At the slice 1.5 the shorter hidden direction ($f = e^{-1/2}$) gives the band a larger tail and a ten times larger shift, which the estimate follows to within a few per cent, and the extended level moves more than at the slice 0.

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

check(shells(9) == [(0, 1), (1, 6), (2, 12), (3, 8), (4, 6), (5, 24), (6, 24),
                    (8, 12), (9, 30)],
      "r3(n2) = 1, 6, 12, 8, 6, 24, 24, 12, 30 for n2 = 0, 1, 2, 3, 4, 5, 6, 8, 9")
```

`shells` counts the lattice points by brute force: every $(x, y, z)$ with coordinates from $-r$ to $r$ ($r$ one more than the integer square root, `math.isqrt`) adds one to the count of its $n^2$; the shells with at least one point are returned as pairs $(n^2, r_3(n^2))$. The check is the list of Section 14.21.

```python
SECTORS = [(1, "even"), (1, "odd"), (-1, "even"), (-1, "odd")]
SIGN = {1: "+1", -1: "-1"}

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

The four sectors, the names of the signs, and the lowest particle label of each (shell, sector): $\Phi(0)$ is computed for all at once; the first label whose target lies above it is $\lfloor(\Phi(0) - \text{offset})/\pi\rfloor + 1$ (`np.floor` rounds down, `astype(int)` makes whole numbers). At $k = 0$ in the even sectors $\Phi(0)$ lies exactly on the target of label 0 (the zero mode, `&` is the element-wise and), and the convention counts that label as a particle label.

```python
pairs30 = [(n2, r3, j, p) for n2, r3 in shells(30) for j, p in SECTORS]
l_min, phi0, offset, k30, j30, p30 = lowest_particle_labels(pairs30, 0.0)
e_first = levels(k30, j30, p30, l_min)
e_below = levels(k30, j30, p30, l_min - 1)
zero_k = k30 == 0.0
branch_ok = (np.all(e_below < 0.0)
             and np.all(e_first[zero_k & (p30 == "even")] == 0.0)
             and np.all(e_first[~(zero_k & (p30 == "even"))] > 0.0))
closest = float(min(np.min(e_first[~(zero_k & (p30 == "even"))]),
                    np.min(-e_below)))
report("level closest to zero away from the zero modes (n2 <= 30)",
       f"{closest:.4f}", "m")
check(branch_ok and f"{closest:.4f}" == "0.2500"
      and record_check("free_particle_branch_labels"),
      "particles are the labels l >= l_min in every sector (n2 <= 30)",
      record=f"{RUST_REPORT}, check free_particle_branch_labels")
```

For every shell up to $n^2 = 30$ and every sector: the level of label $l_{\min}$ must be positive (or exactly zero for the zero modes) and the level of label $l_{\min} - 1$ negative (`~` is the element-wise not); `closest` is the level nearest to zero apart from the zero modes. Out [13]: $0.2500\,m$, the band at the first shell, as in the Rust check. Two PASS lines.

**In [14], the closed shells.**

```python
def closed_shells(a4, n2_max, e_max=1.6):
    pairs = [(n2, r3, j, p) for n2, r3 in shells(n2_max) for j, p in SECTORS]
    l_next, _, _, k_, j_, par = lowest_particle_labels(pairs, a4)
    found_levels = []  # (energy, degeneracy, name, n2)
    active = np.arange(len(pairs))
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

The aufbau of the Rust solver. All (shell, sector) pairs up to `n2_max` start at their lowest particle label. In each pass of the `while` loop the next level of every sector that is still open is found in one call; the levels up to $1.6\,m$ are stored with their degeneracy $4r_3(n^2)$ and a name such as `1:+1:even:0` (shell, block type, fold condition, label); a sector whose level lies above $1.6\,m$ is closed (`active[keep]` keeps the others), and the open ones move on to their next label.

```python
    with_levels = {n2 for _, _, _, n2 in found_levels}
    stop = next(n2 for n2, _ in shells(n2_max) if n2 > 0 and n2 not in with_levels)
    found_levels = [lev for lev in found_levels if lev[3] < stop]
    found_levels.sort(key=lambda lev: (lev[0], lev[2]))
```

The shells that have at least one level below $1.6\,m$ (a set comprehension), the first shell $n^2 > 0$ that has none, where the Rust program stops, and only the levels of the shells before it; then the levels are sorted by energy and, for equal energies, by name (`sort` with a `key` function).

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

The grouping: levels within $10^{-9}$ of the first level of a group belong to it; the running total of states after each group is a closed shell, stored with the group's energy, the next energy (`float("nan")`, not a number, after the last group) and the names of the group joined by semicolons.

```python
agree = True
tables = {}
for a_, n2_max in ((0.0, 50), (0.5, 120)):
    table, stop = closed_shells(a_, n2_max)
    tables[a_] = table
    mine_rows = [r for r in shells_record if float(r["a4"]) == a_]
    same = len(table) == len(mine_rows) and all(
        int(r["N_closed"]) == t[0] and abs(float(r["eps_last_filled"]) - t[1]) < 1e-11
        and sorted(r["levels_of_the_last_group"].split(";")) == sorted(t[3].split(";"))
        for r, t in zip(mine_rows, table))  # a group is compared as a set of names
    agree &= same and stop < n2_max
    say(f"slice {a_}: {len(table)} closed shells up to 1.6 m, the first shell "
        f"without a level below 1.6 m is n2 = {stop}; equal to the record: {same}")
check(agree, "the closed shells of the slices 0 and 0.5 equal the record row by row",
      record=f"{SPECTRUM}/closed-shells.csv, rows a4 = 0 and 0.5")
```

The slices 0 and 0.5, with enough shells (50 and 120) that the stopping shell is reached (`stop < n2_max` is checked). Row by row the table must equal the record: the same number $N$, the energy to $10^{-11}$, and the same names in the last group, compared as sorted lists, because the order of the names inside a group of exactly degenerate levels (such as the odd levels of label 1 of the two block types) follows the last bits of the two computed energies, which differ between numpy and the Rust program. Out [14]: 56 closed shells at the slice 0 (stopping shell $n^2 = 41$) and 123 at the slice 0.5 (stopping shell $n^2 = 113$), both equal to the record.

```python
say("slice 0, the first closed shells: N = "
    + ", ".join(str(t[0]) for t in tables[0.0][:24]) + ", ...")
bulk_edge = float(min(levels(0.0, 1.0, "odd", 0), levels(0.0, 1.0, "even", 1)))
below_edge = [t for t in tables[0.0] if t[1] < bulk_edge and t[2] - t[1] > 1e-6]
N_large = below_edge[-1][0]
N_mid = min((t[0] for t in below_edge if t[0] >= 8),
            key=lambda n: abs(n - N_large / 4))
```

Out [14] lists the first 24 closed shells of the slice 0, $8, 32, 80, \dots, 2064, 2352$. The rule of `parameters.json`: the bulk edge is the smaller of the odd level of label 0 and the even level of label 1 at $k = 0$; `below_edge` keeps the closed shells whose last level lies below it (and whose next level is more than $10^{-6}$ higher); `N_large` is the last of them and `N_mid` the one nearest to `N_large / 4` (`min` with a `key` returns the element with the smallest key).

```python
parameters = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                        .read_text(encoding="utf-8"))
numbers = parameters["particleNumbers"]
report("bulk edge", f"{bulk_edge:.12f}", "m")
report("particle numbers N", f"8, {N_mid}, {N_large}")
check(abs(bulk_edge - numbers["bulkEdge"]) < 1e-12 and N_large == 2352
      and N_mid == 592 and numbers["values"] == [8.0, 592.0, 2352.0],
      "the bulk edge 1.2922928281 and the particle numbers 8, 592, 2352",
      record="Revision/kohn_sham/results/parameters.json, particleNumbers")
```

Out [14]: the bulk edge $1.292292828069\,m$ and the particle numbers 8, 592, 2352, equal to the record. Two PASS lines.

**In [15], figure 6.**

```python
fig, ax = plt.subplots(figsize=(8.0, 4.6))
for a_, style in ((0.0, "-"), (0.5, "--")):
    energies = [t[1] for t in tables[a_]]
    counts = [t[0] for t in tables[a_]]
    ax.step(energies, counts, style, where="post",
            label=f"slice $a_{{4,0}} = {a_}$")
ax.axvline(bulk_edge, color="gray", linestyle="-.", linewidth=0.8)
ax.annotate("bulk edge", (bulk_edge + 0.015, 15), fontsize=8, color="gray")
last_filled = {t[0]: t[1] for t in tables[0.0]}  # N -> its last filled level
for n_ in (8, N_mid, N_large):
    t_ = last_filled[n_]
    ax.plot([t_], [n_], "o", color="C3")
    ax.annotate(f"N = {n_}", (t_ + 0.02, n_ * 0.75), fontsize=8, color="C3")
ax.set_yscale("log")
ax.set_xlabel("energy of the last filled level (units of $m$)")
ax.set_ylabel("closed-shell particle number $N$ (logarithmic)")
ax.set_title("the free aufbau: closed shells up to $1.6\\,m$")
ax.legend(fontsize=8, loc="upper left")
save_figure(fig, "closed_shells",
            ...)
```

`step(x, y, where="post")` draws a staircase that keeps each value until the next point. The three particle numbers are marked at their last filled levels, and the vertical axis is made logarithmic (`set_yscale("log")`). **What figure 14c.6 shows.** Both staircases start at $N = 8$ at the energy 0. At the slice 0 the first step comes at $0.25$ (to 32), then $0.354$ (80), and so on along the band; $N = 592$ sits at $0.79$ and $N = 2352$ at $1.27$, just left of the bulk edge, after which the steps of the levels off the band begin. At the slice 0.5 every band level is lower by the factor $e^{-0.5}$, so the dashed staircase rises earlier and reaches about $2.5\times10^4$ at $1.6\,m$ against about $7\times10^3$ at the slice 0.

**In [16], the last check.**

```python
figure_names = ["14c_1_band_structure.png", "14c_2_band_slope.png",
                "14c_3_band_redshift.png", "14c_4_block_type_mirror.png",
                "14c_5_tip_angle.png", "14c_6_closed_shells.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all six figure files of this notebook exist")
all_checks_passed()
```

The last line is ALL 16 CHECKS PASSED (notebook 14c). The 16 checks are: 4 in In [3], 3 in In [5], 1 in In [7], 1 in In [9], 2 in In [11], 2 in In [13], 2 in In [14] and 1 in In [16].

### 14.26 The exact local exchange of the contact interaction

**What is needed.** The quanta of dirac16complex interact through the contact term $U = \tfrac\lambda2S^2$ of the Lagrangian, with the scalar density $S = \bar\Psi\Psi = \Psi^\dagger C\Psi$, normal ordered in the quantised theory; $\lambda > 0$ is a repulsion, and $\lambda$ has the dimension $\text{mass}^{-6}$ because the field has the dimension $7/2$ in eight dimensions (`Revision/kohn_sham/ks-theory.json`, units). The Kohn-Sham model needs the energy of this interaction in a Kohn-Sham state, a Slater determinant of orbitals or a thermal mixture of them (Chapter 13), as a function of the densities. This section derives it exactly. The result is surprising and very useful: the exchange energy, which for most interactions depends on the orbitals in a complicated way, is here an ordinary function of two densities at the same point.

**The expectation-value rule (Chapter 10).** For one quantum in the mode $u$ (a column of 16 numbers), the expectation value of a density $\Psi^\dagger X\Psi$ is $u^\dagger BXu$, with the matrix $B$ of the indefinite (Krein) inner product. For many independent quanta in the modes $u$ with the occupations $f_{\rm occ}$ (1 for filled, 0 for empty, or a number between at a temperature; the index distinguishes them from the hidden scale $f$),

$$
\langle\Psi^\dagger X\Psi\rangle = \mathrm{Tr}(X\rho), \qquad \rho = \sum_{\rm occupied} f_{\rm occ}\,uu^\dagger B .
$$

Rule: $\mathrm{Tr}(Xuu^\dagger B) = \mathrm{Tr}(u^\dagger BXu) = u^\dagger BXu$, because a trace does not change when the first factors are moved to the end, and $u^\dagger BXu$ is a single number. The $16 \times 16$ matrix $\rho$ is the **one-body matrix** of the state. The number density and the scalar density are

$$
n = \langle\Psi^\dagger B\Psi\rangle = \mathrm{Tr}(B\rho), \qquad S = \langle\bar\Psi\Psi\rangle = \langle\Psi^\dagger C\Psi\rangle = \mathrm{Tr}(C\rho) .
$$

Status: the rule is the expectation-value rule of the canonical quantisation (Chapter 10), stated in the record as exchange.expectationRule of `Revision/kohn_sham/ks-theory.json`; the two density formulas are the check gas_densities of both theory reports.

**The plane waves of the good sector.** In flat space ($H = 0$ and the slice 0, so that $f = \kappa = 1$ and nothing depends on $y$) a plane wave $e^{-i\varepsilon x_4 + i\mathbf p\cdot\mathbf x}u$ with the momentum $\mathbf p = (p_1, p_2, p_3, p_0)$ along the four space-like directions $x_0, x_1, x_2, x_3$ (the good sector has no momentum along the extra times) solves $h_{\mathbf p}u = \varepsilon u$ with

$$
h_{\mathbf p} = M(-i\gamma^{(x_4)}) - \sum_a p_a\,\gamma^{(x_4)}\gamma^{(a)} \qquad (a = x_0, x_1, x_2, x_3) .
$$

Rule: the Hamiltonian $h$ of Section 14.4 with $v = 0$; its derivative term $i\gamma^{(x_4)}\gamma^{(x_0)}\partial_y$ acting on $e^{ip_0y}$ gives $i\gamma^{(x_4)}\gamma^{(x_0)}(ip_0) = -p_0\gamma^{(x_4)}\gamma^{(x_0)}$. Its square, line by line:

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
h_{\mathbf p}^2 = \big(M^2 + p_1^2 + p_2^2 + p_3^2 + p_0^2\big)\,1 = E^2\,1, \qquad E = \sqrt{M^2 + p^2} .
$$

Rule: multiply out the square of the sum; the squares of the five terms give $M^2$ and the $p_a^2$, and the mixed products cancel in pairs. Since $h_{\mathbf p}$ is Hermitian (Section 14.4), its eigenvalues are real numbers whose squares are $E^2$: they are $+E$ and $-E$. Its trace is zero (it is a sum of products of one or two different gammas, Chapter 5), so the two eigenvalues occur equally often: $+E$ eight times and $-E$ eight times. Every momentum carries eight positive-energy modes. The matrix

$$
G_{\mathbf p} = \tfrac12\big(1 + h_{\mathbf p}/E\big)
$$

is the **projector** on them: $G_{\mathbf p}^2 = \tfrac14(1 + 2h_{\mathbf p}/E + h_{\mathbf p}^2/E^2) = \tfrac14(2 + 2h_{\mathbf p}/E) = G_{\mathbf p}$, and $\mathrm{Tr}\,G_{\mathbf p} = \tfrac12(16 + 0) = 8$. Status: PROVED; check gas_mode_projector (both reports).

**Why every symmetric occupation has $\rho = (nB + SC)/16$.** The sum of $uu^\dagger$ over the eight positive-energy modes (orthonormal, because $h_{\mathbf p}$ is Hermitian) is the projector $G_{\mathbf p}$. We assume that the eight modes of one momentum carry the same occupation $f_{\rm occ}$, as they do in every closed shell (all eight filled) and in every thermal state (the occupation depends only on the energy, which is the same for the eight). Then these eight modes contribute $f_{\rm occ}G_{\mathbf p}B$ to $\rho$; we write the case $f_{\rm occ} = 1$, and a common factor $f_{\rm occ}$ changes nothing below. Line by line:

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

**What the functional leaves out.** The Kohn-Sham functional of the Revision theory is Hartree plus this uniform-gas exchange, with no correlation energy. Its states, however, are not uniform along $y$. The record computes the EXACT Fock exchange of such a state (exchange.exactFockSlab in ks-theory.json): take one level, closed over a shell ($\mathbf k$ and $-\mathbf k$ equally filled), with the $2 \times 2$ block density $D = \tfrac12(d_0 + d_1\sigma_1 + d_2\sigma_2 + d_3\sigma_3)$ in each of the four blocks of type $j = +1$ and $\sigma_3D\sigma_3$ in each of the four of type $-1$ (their degenerate partners, Section 14.5), and average it over the directions of the shell. Two facts make this average simple. First, averaging a matrix over all the rotations of a group gives a matrix that no rotation of the group changes, that is, one that commutes with all of them; and a matrix that already commutes with them is its own average. So the average over all rotations of 3-space is the projection onto the matrices that commute with the rotations, a space of dimension 64. Second, a closed shell contains only a finite set of directions, which the 24 rotations of a cube carry into each other, not all directions. But under the rotations of 3-space the $16 \times 16$ matrices split into parts of spin 0 (unchanged by every rotation) and parts of spin 1 (turned like an arrow), and nothing else; and the average of an arrow over the 24 rotations of a cube is zero, just as its average over all rotations. So for these matrices the average over the cube equals the average over all rotations (both theory reports state this: the 16 x 16 matrices carry only spin 0 and spin 1). The result, with $Q = \langle\Psi^\dagger B\gamma^{(x_0)}\Psi\rangle$ and the $y$-current $Y$:

$$
n = 8d_0, \qquad S = 8d_2, \qquad Q = 8d_3, \qquad Y = 8d_1, \qquad e_x^{\rm exact} = -\frac{\lambda}{32}\big(n^2 + S^2 - Q^2 - Y^2\big) .
$$

For orbitals $Y = 0$ (Section 14.12), so the uniform-gas exchange $-\tfrac{\lambda}{32}(n^2 + S^2)$ omits the term $+\tfrac{\lambda}{32}Q^2$. The record labels this a DIAGNOSTIC: the canonical functional stays the uniform-gas one, and the Rust solver reports the omitted part and also solves an exact-Fock variant of the model, which adds the potential $w_Q\sigma_3$ with $w_Q = +\tfrac{\lambda}{16}Q$ to $h$ and $+\tfrac{\lambda}{32}Q^2$ to $e_{\rm int}$. Status: PROVED; check exchange_slab_exact_fock (both reports, by two different methods: the sympy report projects onto the 64-dimensional space of matrices that commute with the rotations, the Wolfram report averages over the 48 spinor matrices of the 24 rotations of a cube, each rotation appearing with both signs).

**The size of $Q$.** For one orbital $\chi = (a, ib)$ the three densities are proportional to $a^2 + b^2$ ($n$), $2ab$ ($S$, up to the sign $j$) and $a^2 - b^2$ ($Q$) (Section 14.12). Line by line:

$$
(2ab)^2 + (a^2 - b^2)^2 = 4a^2b^2 + a^4 - 2a^2b^2 + b^4 = (a^2 + b^2)^2 .
$$

Rule: the binomial formulas. So for one orbital $S^2 + Q^2 = n^2$, and for a mixture of orbitals $S^2 + Q^2 \le n^2$ (Exercise 14.9): the possible states fill the disk $(S/n)^2 + (Q/n)^2 \le 1$. The uniform-gas and the exact exchange agree on the line $Q = 0$ and differ most at the top and bottom of the disk, $S = 0$, $Q = \pm n$ (Figure 14d.3).

**Proper densities and the volume of the cell.** The densities that enter $e_{\rm int}$, $M_{\rm eff}$ and $v_v$ are **proper** densities: numbers of quanta per unit proper 7-volume. The cell of the model is the coordinate 3-torus of size $\ell$, the coordinate volume $v_t$ of the extra times and the hidden coordinate $-L \le y \le 0$ on each of its two halves. By Section 14.2 its proper volume element is $\sqrt{|g|}\,\ell^3v_t\,dy = e^{-a_{4,0}}b_{4,0}^2e^{3Hy}\ell^3v_t\,dy$. The Revision solver writes the factor in front of $e^{3Hy}dy$, on the history and in units with $b_4(0) = 1$, as

$$
\mathrm{Vol}_7(a_{4,0}) = \ell^3v_te^{-a_{4,0}}b_{4,0}^2 = \ell^3v_te^{-a_{4,0}}e^{(8/3)a_{4,0}} = \ell^3v_te^{(5/3)a_{4,0}} .
$$

Rule: $b_{4,0}^2 = e^{2\cdot(4/3)a_{4,0}}$ and $-1 + \tfrac83 = \tfrac53$. With $\ell = 2\pi/0.25 = 8\pi$ and $v_t = 1$, $\mathrm{Vol}_7(0) = (8\pi)^3 = 15875.2137$. A density per unit $y$ of the orbitals, divided by $\mathrm{Vol}_7e^{3Hy}$, is a proper density: the orbital densities are multiplied by $P = e^{-3Hy}/\mathrm{Vol}_7(a_{4,0})$ (the record's densities section in ks-theory.json; it is the factor $P$ of Section 14.7 in these units).

**The coupling and the volume enter only as their ratio.** Line by line:

- Every proper density is an orbital sum divided by Vol (with the factor $e^{-3Hy}$): $n = \bar n/\mathrm{Vol}$, $S = \bar S/\mathrm{Vol}$ with orbital sums $\bar n$, $\bar S$ that do not contain Vol.
- So $M_{\rm eff} - m = \tfrac{15}{16}\lambda\bar S/\mathrm{Vol}$ and $v_v = -\tfrac1{16}\lambda\bar n/\mathrm{Vol}$ contain $\lambda$ and Vol only as $\lambda/\mathrm{Vol}$.
- The interaction energy of the cell, $\mathrm{Vol}\,e_{\rm int} = \mathrm{Vol}\big(\tfrac{15}{32}\lambda\bar S^2 - \tfrac1{32}\lambda\bar n^2\big)/\mathrm{Vol}^2 = (\lambda/\mathrm{Vol})\big(\tfrac{15}{32}\bar S^2 - \tfrac1{32}\bar n^2\big)$, also.

Rule: insert and cancel one factor Vol. Hence the substitution $(\lambda, \mathrm{Vol}) \to (c\lambda, c\,\mathrm{Vol})$ changes nothing: a Kohn-Sham state depends on the coupling and the volume of the cell only through their ratio. In the solver's units the coupling is $\hat\lambda = \lambda b_4(0)^{-2}$, a constant of the theory, the same at every slice, and the slice state at $\hat\lambda$ is the state of the coordinate cell $\ell^3v_t$ at the **effective coupling**

$$
\hat\lambda_{\rm eff} = \hat\lambda\,e^{-(5/3)a_{4,0}} ,
$$

at the same $f$ and $\kappa$. Rule: $\hat\lambda/\mathrm{Vol}_7(a_{4,0}) = (\hat\lambda e^{-(5/3)a_{4,0}})/(\ell^3v_t)$. Along the history the proper cell grows like $e^{(5/3)a_{4,0}}$ (Figure 14a.2), so a fixed coupling acts more and more weakly. Status: PROVED; checks ks_coupling_volume_scaling and history_solver_units of `Revision/kohn_sham/reports/ks-theory-python.json` and of the Wolfram report (the record states it as densities.couplingVolumeScaling in ks-theory.json); Notebook 14d checks both with sympy (In [12]).

**The state of the eight zero modes ($N = 8$).** The simplest Kohn-Sham state of the model fills the eight fold zero modes at $k = 0$ (both block types, even fold condition). At the slice $a_{4,0}$ each orbital is $\chi = (a, 0)$ with $a = \sqrt{2fM/(1 - e^{-2fML})}\,e^{fMy}$ and $f = e^{-a_{4,0}/3}$ (Section 14.13). The densities, line by line (the record's densities section in ks-theory.json):

- One orbital: $n_o = P(a^2 + b^2) = Pa^2$, $s_o = P\,j\,2ab = 0$, $q_o = P(a^2 - b^2) = Pa^2$.
- The state: $n = \sum w\,g\,f_{\rm occ}\,n_o$, with the degeneracy $g = 4$ per block type, the occupation $f_{\rm occ} = 1$, and the weight $w = \tfrac12$: the orbital has the same $\chi(y)$ on both halves of the cell and is normalised on one half, $\int_{-L}^0\chi^\dagger\chi\,dy = 1$, so a point of either half holds half of it, and the particle number $N = \sum g f_{\rm occ}$ counts the whole cell (Section 14.12; the filling of both fold conditions behind this convention is ASSUMED). So $n = \tfrac12(4 + 4)Pa^2 = 4Pa^2$, $S = 0$ and $Q = n$, and the whole cell holds $2\mathrm{Vol}_7\int_{-L}^0e^{3Hy}n\,dy = 2\cdot4\int a^2\,dy = 8$ quanta.
- The proper density $n = 4e^{-3Hy}a^2/\mathrm{Vol}_7 \propto e^{(2fM - 3H)y}$ grows toward the tip, because $2fM \le 2 < 3 = 3H$ at every slice: although the orbital sits at the fold, the proper 7-volume $e^{3Hy}$ shrinks faster toward the tip than the orbital does. It is largest at the cutoff $y = -L$. With $H = m = 1$, $L = 3$, $\ell = 8\pi$ and $v_t = 1$ the largest values at the five slices are $1.0146860704\times10^{-2}$, $9.4124988502\times10^{-3}$, $7.6077487746\times10^{-3}$, $5.4855846489\times10^{-3}$ and $3.6009745365\times10^{-3}$ (Notebook 14d, Out [13]; the column n_max of the rows N8_lam0_a00 to N8_lam0_a20 of `Revision/kohn_sham/results/ground/summary.csv`): along the history the cell grows and the proper density falls.
- To first order in $\lambda$ the potentials are $M_{\rm eff} - m = \tfrac{15}{16}\lambda S = 0$ and $v_v = -\tfrac{\lambda}{16}n$.
- The Revision solver calibrates its couplings by the largest first-order potential per unit $\hat\lambda$, the maximum over the five slices and over $y$ of $\max(\tfrac{15}{16}|S|, |n|/16)$; here it is $n_{\max}/16$ at the slice 0, $6.341788\times10^{-4}$ (at the other slices $5.882812$, $4.754843$, $3.428490$ and $2.250609$ times $10^{-4}$). $\lambda_1$ and $\lambda_2$ are $0.1$ and $0.3$ divided by it, rounded to 4 significant digits: $\lambda_1 = 157.7$ and $\lambda_2 = 473.1$, so that the largest first-order potential is $0.1000099958\,m$ and $0.3000299875\,m$ (Notebook 14d, Out [13]; `Revision/kohn_sham/results/parameters.json`, couplingCalibration; the states $N = 592$ and $2352$ have their own couplings, fixed the same way along the whole history: $\lambda_1 = 2.131$ and $0.5363$). This calibration is an $L = 3$ statement: the largest proper density sits at the cutoff and grows with $L$, so the same rule applied at a larger cutoff gives smaller couplings ($\lambda_1 = 1.249$ for $N = 8$ at $L = 6$; Section 14.20).
- The exact Fock exchange of this state vanishes: with $S = 0$ and $Q = n$, $e_x^{\rm exact} = -\tfrac{\lambda}{32}(n^2 - Q^2) = 0$. In the exact-Fock variant the potential on $(a, 0)$ is $v_v + w_Q = \tfrac{\lambda}{16}(Q - n) = 0$ (because $\sigma_3$ acts as $+1$ on $(a, 0)$), so the zero modes, and the fold-band orbitals $(e^{fMy}, 0)$ above them, stay exact solutions: the energy of the state is exactly zero and its gap stays $\kappa\Delta k = 0.25\,e^{-a_{4,0}}$. The record's twenty self-consistent exact-Fock states with $N = 8$ (four couplings, five slices) have energies zero to rounding, at most $5.0\times10^{-12}$ in size, and gaps equal to $0.25\,e^{-a_{4,0}}$ to $9.9\times10^{-14}$; with the uniform-gas exchange the same states have energies of at least $6.980\times10^{-3}$ in size (`Revision/kohn_sham/results/exx/exact-fock-variant.csv`; Notebook 14d, Out [13]).

Status: the formulas PROVED; the numbers COMPUTED (they reproduce the records named); the weight $w = \tfrac12$ rests on the ASSUMED filling of both fold conditions. A remark on the record (a discrepancy it notes itself): the solver fixes the chemical potential by $\sum g f_{\rm occ} = N$, the particle number of the whole cell, while one line of the thermodynamics section of ks-theory.json writes $\sum w g f_{\rm occ} = N$; the solver's choice agrees with the rest of the theory file and with the counting above (`Revision/kohn_sham/results/parameters.json`, conventions.particleNumber).

### 14.28 Example: Notebook 14d, the exact local exchange

Notebook 14d does Sections 14.26 and 14.27 with exact algebra on the author's gamma matrices: the plane waves of the good sector and their projector, the cancellation that makes $\rho = (nB + SC)/16$, Wick's rule term by term on two explicit states, the exact local exchange and the ratio $-1/8$, the Kohn-Sham potentials and the on-shell Lagrangian (compared with the coefficients that the Rust solver read), the exact Fock exchange of the closed-shell states by projection onto the 64-dimensional space of matrices that commute with the rotations, and the scaling with the coupling and the cell volume. With numpy it computes the densities of the eight zero modes at the five slices of the history and reproduces the largest proper densities, the calibration of the couplings and the zero exact-Fock energies of the record. It draws four figures, needs no Rust, runs in about a minute, and its last line is ALL 18 CHECKS PASSED (notebook 14d).

<!-- NOTEBOOK 14d -->

### 14.31 Line-by-line walk-through of Notebook 14d

The notebook has 15 code cells, In [1] to In [15]. Docstrings and the long caption texts are left out of the quotations; the captions are printed under the figures in Section 14.30.

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
g0, g1, g2, g3, g4, g5, g6, g7 = g  # gN is gamma^(xN)
I16, Z16 = sp.eye(16), sp.zeros(16)
C = g0 * g1 * g2 * g3
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
p1, p2, p3, p0 = sp.symbols("p1 p2 p3 p0", real=True)  # the momentum
E = sp.symbols("E", positive=True)  # stands for sqrt(M^2 + p^2)
h_p = M * (-sp.I * g4) - (p1 * g4 * g1 + p2 * g4 * g2 + p3 * g4 * g3 + p0 * g4 * g0)
E_squared = M ** 2 + p1 ** 2 + p2 ** 2 + p3 ** 2 + p0 ** 2
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
p_flip = {p1: -p1, p2: -p2, p3: -p3, p0: -p0}
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
values = {M: 1, E: sp.sqrt(2), p1: 1, p2: 0, p3: 0, p0: 0}
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
Q_s = sp.simplify((B * g0 * rho_slab).trace())
e_x_slab = sp.expand(-lam / 2 * (C * rho_slab * C * rho_slab).trace())
say(f"commutant dimension {len(basis)}; n = {n_s}, S = {S_s}, Q = {Q_s}")
say(f"V unitary: {sp.simplify(V.H * V) == I16}")
```

The averaged one-body matrix, its three densities $n$, $S$ and $Q = \langle\Psi^\dagger B\gamma^{(x_0)}\Psi\rangle$, and its exchange energy. Out [10] prints the dimension 64, $n = 8d_0$, $S = 8d_2$, $Q = 8d_3$, and that $V$ is unitary.

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

**In [12], the coupling and the volume of the cell.**

```python
c_s, Vol, ell_s, v_t_s = sp.symbols("c Vol ell v_t", positive=True)
a_s, beta_s, y_s = sp.symbols("a beta y", real=True)
H_s, b_init = sp.symbols("H b_0", positive=True)
```

Symbols for a scale factor $c$, the volume Vol, the box size $\ell$, the extra-time volume $v_t$, the slice $a_{4,0}$ (`a_s`), the exponent $\beta$ of the history, the hidden coordinate, $H$ and $b_4(0)$ (`b_init`).

```python
def cell_energy(l_, V_):
    return V_ * (sp.Rational(15, 32) * l_ * (S / V_) ** 2 - l_ * (n / V_) ** 2 / 32)

ok_scaling = (sp.simplify(cell_energy(c_s * lam, c_s * Vol) - cell_energy(lam, Vol))
              == 0
              and sp.simplify(sp.Rational(15, 16) * c_s * lam * S / (c_s * Vol)
                              - sp.Rational(15, 16) * lam * S / Vol) == 0
              and sp.simplify(-c_s * lam * n / (16 * c_s * Vol)
                              + lam * n / (16 * Vol)) == 0)
check(ok_scaling and record_check("ks_coupling_volume_scaling"),
      "a Kohn-Sham state depends on the coupling and the volume only as lambda/Vol",
      record=f"{PY_REPORT}, check ks_coupling_volume_scaling")
```

Here the symbols `S` and `n` of In [4] play the part of the orbital sums $\bar S$ and $\bar n$ of Section 14.27, so the densities are `S / V_` and `n / V_`. `cell_energy` is the interaction energy of the cell, Vol times $e_{\rm int}$. The three tests are the three lines of Section 14.27: the cell energy, $M_{\rm eff} - m$ and $v_v$ do not change when $\lambda$ and Vol are both multiplied by $c$.

```python
b_on_history = b_init * sp.exp(beta_s * a_s)  # b4 = b4(0) e^(beta a4)
P_proper = (sp.exp(-3 * H_s * y_s) * sp.exp(a_s)
            / (ell_s ** 3 * v_t_s * b_on_history ** 2))  # per proper 7-volume
Vol7 = ell_s ** 3 * v_t_s * sp.exp((2 * beta_s - 1) * a_s)  # Vol_7 of the solver
P_solver = sp.exp(-3 * H_s * y_s) / Vol7
lam_hat = lam * b_init ** -2  # the solver's coupling
lam_eff = lam_hat * sp.exp(-(2 * beta_s - 1) * a_s)  # in the coordinate cell
```

The factor $P$ that makes a density proper, written twice: with the true proper volume $\ell^3v_te^{-a_{4,0}}b_{4,0}^2e^{3Hy}$ on the history $b_4 = b_4(0)e^{\beta a_4}$ (`P_proper`), and in the solver's units with $\mathrm{Vol}_7 = \ell^3v_te^{(2\beta - 1)a_{4,0}}$ (`P_solver`); the solver's coupling $\hat\lambda = \lambda b_4(0)^{-2}$ and the effective coupling of the coordinate cell.

```python
ok_units = (sp.simplify(lam * P_proper - lam_hat * P_solver) == 0
            and sp.simplify(lam_hat * P_solver
                            - lam_eff * sp.exp(-3 * H_s * y_s) / (ell_s ** 3 * v_t_s))
            == 0
            and sp.simplify(lam_eff.subs(beta_s, sp.Rational(4, 3))
                            - lam_hat * sp.exp(-sp.Rational(5, 3) * a_s)) == 0)
say(f"Vol_7 on the history (beta = 4/3): {Vol7.subs(beta_s, sp.Rational(4, 3))}")
check(ok_units and record_check("history_solver_units"),
      "lambda P_proper = lambda_hat e^(-3Hy)/Vol_7; lambda_eff = lambda_hat e^(-5a/3)",
      record=f"{PY_REPORT}, check history_solver_units")
```

Three tests: $\lambda P_{\rm proper} = \hat\lambda P_{\rm solver}$ (the factors $b_4(0)^2$ move from the volume to the coupling); $\hat\lambda P_{\rm solver}$ equals the effective coupling times the factor of the coordinate cell $\ell^3v_t$; and for $\beta = 4/3$ the effective coupling is $\hat\lambda e^{-(5/3)a_{4,0}}$. Out [12] prints `ell**3*v_t*exp(5*a/3)`, the cell volume on the history, and two PASS lines.

**In [13], the eight zero modes along the history.**

```python
H_val, m_val, L_val = 1.0, 1.0, 3.0
BETA = 4.0 / 3.0  # the history b4 = b4(0) e^(beta a4), b4(0) = 1
SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]
ell = 2.0 * math.pi / 0.25  # the coordinate size of the 3-torus
y = np.linspace(-L_val, 0.0, 1801)  # the hidden coordinate
```

The canonical numbers of the Revision runs, the five slices, the box size $\ell = 2\pi/\Delta k = 8\pi$, and 1801 points of the hidden coordinate from the cutoff to the fold (the solver's fine grid of $2G + 1$ points for $G = 900$).

```python
summary = repository_file("Revision/kohn_sham/results/ground/summary.csv") \
    .read_text(encoding="utf-8").splitlines()
header = summary[0].split(",")
free8 = {r.split(",")[0]: dict(zip(header, r.split(","))) for r in summary[1:]
         if r.startswith("N8_lam0_")}
```

The summary of the Rust solver's ground states, and from it the five free states $N = 8$ (their names start with `N8_lam0_`), stored in a dictionary under their names.

```python
n_curves, n_max, worst_n, at_tip = {}, [], 0.0, True
for a_, tag in zip(SLICES, ("a00", "a05", "a10", "a15", "a20")):
    f_ = math.exp((0.5 * BETA - 1.0) * a_)  # the hidden scale of the slice
    vol7 = ell ** 3 * 1.0 * math.exp((2.0 * BETA - 1.0) * a_)  # Vol_7(a4,0)
    fM = f_ * m_val
    a_sq = 2.0 * fM / (1.0 - math.exp(-2.0 * fM * L_val)) * np.exp(2.0 * fM * y)
    P = np.exp(-3.0 * H_val * y) / vol7  # the proper-density factor
    n_y = 4.0 * P * a_sq  # line 2
    n_curves[a_] = (n_y, a_sq, vol7)
    n_max.append(float(np.max(n_y)))
```

For each slice: the hidden scale $f = e^{-a_{4,0}/3}$, the cell volume $\mathrm{Vol}_7 = \ell^3v_te^{(5/3)a_{4,0}}$ (with $v_t = 1$), the square of the normalised zero mode $a^2 = 2fM e^{2fMy}/(1 - e^{-2fML})$, the factor $P = e^{-3Hy}/\mathrm{Vol}_7$, and the density $n = 4Pa^2$ of Section 14.27; its curve is kept for the figure and its largest value appended to the list `n_max`.

```python
    worst_n = max(worst_n, abs(n_max[-1] / float(free8[f"N8_lam0_{tag}"]["n_max"])
                               - 1.0))
    at_tip &= float(y[np.argmax(n_y)]) == -L_val
    say(f"slice a4,0 = {a_}: f = {f_:.6f}, Vol_7 = {vol7:.4f}, n_max = "
        f"{n_max[-1]:.10e} at y = {float(y[np.argmax(n_y)]):.1f}")
check(worst_n < 1e-9 and at_tip,
      "n_max = 4 P a^2 at the tip y = -3 equals the record at all five slices",
      record="Revision/kohn_sham/results/ground/summary.csv, N8_lam0, n_max")
```

The relative difference from the recorded largest density of the same slice (`n_max[-1]` is the last entry of the list), and where the largest value sits (`np.argmax` gives the position of the largest entry). Out [13] prints for the five slices $f = 1, 0.846482, 0.716531, 0.606531, 0.513417$, $\mathrm{Vol}_7 = 15875.2137, 36528.4839, 84051.1608, 193399.6945, 445008.0344$ and $n_{\max} = 1.0146860704\times10^{-2}$, $9.4124988502\times10^{-3}$, $7.6077487746\times10^{-3}$, $5.4855846489\times10^{-3}$, $3.6009745365\times10^{-3}$, each at $y = -3.0$, the cutoff. The check: equal to the record to $10^{-9}$, and at the tip at every slice.

```python
def round_significant(x, digits):
    exponent = math.floor(math.log10(abs(x))) - (digits - 1)
    scale = 10.0 ** (-exponent)
    return math.copysign(math.floor(abs(x) * scale + 0.5), x) / scale
```

Rounding to a number of significant digits, with halves rounded away from zero: `math.log10` gives the decimal exponent of the number, `scale` moves the last digit to keep in front of the decimal point, `math.floor(... + 0.5)` rounds, and the division moves it back.

```python
strengths = [x / 16.0 for x in n_max]  # line 5 at each slice (S = 0)
strength = max(strengths)  # the largest first-order potential per lambda_hat
lambda_1 = round_significant(0.1 / strength, 4)
lambda_2 = round_significant(0.3 / strength, 4)
parameters = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                        .read_text(encoding="utf-8"))
calibration = [c for c in parameters["couplingCalibration"]["values"]
               if c["N"] == 8.0][0]
```

The calibration rule of Section 14.27: since $S = 0$, the largest first-order potential per unit $\hat\lambda$ at a slice is $n_{\max}/16$; the largest over the slices fixes $\lambda_1$ and $\lambda_2$. The record's calibration of the state $N = 8$ is read from `parameters.json`.

```python
report("strength per lambda_hat at the five slices",
       ", ".join(f"{x:.6e}" for x in strengths))
report("lambda_1, lambda_2", f"{lambda_1}, {lambda_2}")
report("first-order potentials", f"{lambda_1 * strength:.10f}, "
       f"{lambda_2 * strength:.10f}", "m")
worst_s = max(abs(x / r - 1.0) for x, r in
              zip(strengths, calibration["strengthPerLambdaAtSlices"]))
check(worst_s < 1e-9 and abs(strength / calibration["strengthPerLambda"] - 1.0) < 1e-9
      and lambda_1 == calibration["lambda1"] and lambda_2 == calibration["lambda2"]
      and abs(lambda_1 * strength - calibration["firstOrderPotential1"]) < 1e-9
      and abs(lambda_2 * strength - calibration["firstOrderPotential2"]) < 1e-9,
      f"strengths at the five slices; lambda_1 = {lambda_1}, lambda_2 = {lambda_2}",
      record="Revision/kohn_sham/results/parameters.json, couplingCalibration N = 8")
```

Out [13]: the strengths $6.341788\times10^{-4}$, $5.882812\times10^{-4}$, $4.754843\times10^{-4}$, $3.428490\times10^{-4}$, $2.250609\times10^{-4}$ (largest at the slice 0), $\lambda_1 = 157.7$, $\lambda_2 = 473.1$, and the first-order potentials $0.1000099958\,m$ and $0.3000299875\,m$; all equal to the record.

```python
exx = repository_file("Revision/kohn_sham/results/exx/exact-fock-variant.csv") \
    .read_text(encoding="utf-8").splitlines()
exx_header = exx[0].split(",")
rows8 = [dict(zip(exx_header, r.split(","))) for r in exx[1:] if r.startswith("N8_")]
largest = max(abs(float(r["E_exact_fock_scf"])) for r in rows8)
smallest_gas = min(abs(float(r["E_uniform_gas"])) for r in rows8)
gap_dev = max(abs(float(r["gap_exact_fock"]) - 0.25 * math.exp(-float(r["a4"])))
              for r in rows8)
report("largest |E| of the 20 exact-Fock N = 8 states", f"{largest:.1e}")
report("smallest |E| of the same states with the uniform-gas exchange",
       f"{smallest_gas:.3e}")
report("largest deviation of their gaps from 0.25 e^(-a4,0)", f"{gap_dev:.1e}", "m")
check(len(rows8) == 20 and largest < 1e-11 and gap_dev < 1e-11,
      "the exact-Fock energy of all 20 N = 8 states is 0, the gap 0.25 e^(-a4,0)",
      record="Revision/kohn_sham/results/exx/exact-fock-variant.csv, "
             "E_exact_fock_scf and gap_exact_fock")
```

The record of the exact-Fock variant: its twenty rows with $N = 8$ (four couplings $\pm\lambda_1$, $\pm\lambda_2$ at five slices), their self-consistent exact-Fock energies, their energies with the uniform-gas exchange, and their gaps. Out [13]: the largest exact-Fock energy is $5.0\times10^{-12}$ in size (zero to rounding), the smallest uniform-gas energy $6.980\times10^{-3}$, and the gaps equal $0.25\,e^{-a_{4,0}}$ to $9.9\times10^{-14}$. Three PASS lines in all.

**In [14], figure 4.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 4.0))
fig.subplots_adjust(wspace=0.32)  # room for the label of the right panel
for index, a_ in enumerate(SLICES):
    n_y, a_sq, vol7 = n_curves[a_]
    left.semilogy(y, n_y, color=f"C{index}", label=f"$n(y)$, $a_{{4,0}} = {a_}$")
    right.plot(y, -lambda_1 * n_y / 16.0, color=f"C{index}",
               label=f"$a_{{4,0}} = {a_}$")
for a_, index in ((0.0, 0), (2.0, 4)):
    left.semilogy(y, 4.0 * n_curves[a_][1], "--", color=f"C{index}",
                  label=f"$4a^2$ per unit $y$, $a_{{4,0}} = {a_:g}$")
right.plot(y, np.zeros_like(y), ":", color="black",
           label="exact Fock: $v_v + w_Q = 0$")
```

Left, on a logarithmic axis: the proper density at the five slices (solid) and, at the slices 0 and 2, the density per unit $y$ of the cell, $\mathrm{Vol}_7e^{3Hy}n = 4a^2$ (dashed). Right: the first-order vector potential $v_v = -\lambda_1n/16$ at the five slices and the zero exact-Fock potential (`np.zeros_like(y)` is an array of zeros of the same length).

```python
left.set_xlabel("$y$ (units of $1/H$; tip cutoff at $-3$, fold at $0$)")
left.set_ylabel("density (logarithmic)")
left.set_title("the eight zero modes ($N = 8$, $\\lambda = 0$)")
left.legend(fontsize=6, loc="center right")
right.set_xlabel("$y$ (units of $1/H$)")
right.set_ylabel("first-order potential $v_v$ (units of $m$)")
right.set_title(f"$v_v = -\\lambda_1 n/16$, $\\lambda_1 = {lambda_1}$")
right.legend(fontsize=7, loc="lower right")
save_figure(fig, "zero_mode_state",
            ...)
```

Labels, titles, legends and saving. **What figure 14d.4 shows.** Left: the dashed densities per unit $y$ rise toward the fold, from $0.020$ to $8.0$ at the slice 0 and from $0.20$ to $4.3$ at the slice 2 (the orbital sits at the fold, and at the later slice it is spread farther toward the tip). The solid proper densities do the opposite: they fall from the tip to the fold, from $1.01\times10^{-2}$ to $5.1\times10^{-4}$ at the slice 0, because the proper volume $e^{3Hy}$ shrinks toward the tip; each later slice lies lower, down to $3.6\times10^{-3}$ at the tip at the slice 2, as the cell grows. Right: the potential $v_v$ is deepest at the tip, $-0.100\,m$ at the slice 0 (the calibration), $-0.035\,m$ at the slice 2, and almost zero at the fold; the exact-Fock potential is zero everywhere.

**In [15], the last check.**

```python
figure_names = ["14d_1_pair_average.png", "14d_2_energy_densities.png",
                "14d_3_exact_fock_ratio.png", "14d_4_zero_mode_state.png"]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
      "all four figure files of this notebook exist")
all_checks_passed()
```

The last line is ALL 18 CHECKS PASSED (notebook 14d). The 18 checks are: 1 in In [2], 1 in In [3], 3 in In [4], 1 in In [6], 2 in In [7], 3 in In [8], 1 in In [10], 2 in In [12], 3 in In [13] and 1 in In [15].

### 14.32 What we proved, what we computed, what we assumed

**PROVED** (exact; the derivation is in this chapter, and the Revision record checks it in `Revision/kohn_sham/reports/ks-theory-python.json`, with the checks marked "both" also in `Revision/kohn_sham/reports/ks-theory-wolfram.json`):

| statement (section; notebook) | record checks |
| --- | --- |
| the hidden coordinate $y = \ln(\sin^2 z)/(12H)$ on the two halves of a cell, the metric in it with the hidden scale $f = e^{-a_4}b_4^{1/2}$, the volume factor $e^{-a_4}b_4^2e^{3Hy}$ (Section 14.2; Notebook 14a) | `geometry_hidden_coordinate`, `geometry_sqrt_det`, `geometry_line_element` (both) |
| $\gamma^\mu\Omega_\mu = \tfrac32(H/f)\gamma^{(x_0)} + (b_4'/b_4 - \tfrac12a_4')\gamma^{(x_4)}$ along every history, with the contribution of every direction (Section 14.4; Notebook 14a) | `spin_connection_compatibility`, `spin_connection_slash`, `spin_connection_time_terms`, `spin_connection_slash_x0_chart` (both) |
| the factor $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$ removes the spin connection, each part alone does not; it is the half-density of the volume factor; the Hamiltonian is Hermitian (Section 14.4; Notebook 14a) | `ansatz_removes_spin_connection`, `ansatz_without_y_factor_term_survives`, `ansatz_without_x4_factor_term_survives`, `ansatz_norm`, `hamiltonian_16_hermitian` (both) |
| eight blocks of two components, two block types, the block forms and the block Hamiltonian $h_j = j[-(i/f)\sigma_1d/dy + M\sigma_2 + \kappa k\sigma_3] + v$ (Section 14.5; Notebook 14a) | `blocks_commuting_set`, `blocks_basis_unitary`, `blocks_forms`, `block_hamiltonian`, `block_ode_equivalent`, `block_type_relation` (both), `blocks_projectors`, `blocks_not_everything_block_diagonal` |
| the chirality matrix $\Gamma$ pairs the block types and reverses the mass (Section 14.6; Notebook 14a) | `blocks_relation_to_Gamma`, `block_Gamma_map` (both) |
| the levels depend only on the length of the 3-momentum (Section 14.6; Notebook 14a) | `rotation_invariance` (both) |
| the exact rescaling identity between the slices (Section 14.7; Notebooks 14a and 14c) | `rescaling_identity` (both) |
| the real form; the same equation on both halves of a cell; the fold conditions; the boundary term; the tip family; the constant current; the asymptotic branches (Section 14.12; Notebook 14b) | `bc_fold_same_equation_on_both_halves`, `bc_fold_conditions`, `bc_self_adjoint_boundary_term`, `bc_tip_family`, `bc_current_conserved_along_y`, `bc_tip_asymptotics` (all both) |
| the exact free levels at zero 3-momentum and the fold zero mode (Section 14.13; Notebook 14b) | `bc_exact_k0_spectra` (both) |
| the equation of the Pruefer angle; the shooting function grows with the energy; one level per label (Section 14.14; Notebook 14b) | derived in Section 14.14 (not a separate check of the record); Notebook 14b checks the equation of the angle with sympy and the labels numerically |
| the fold band $\varepsilon = \kappa k$ with the orbital $(e^{fMy}, 0)$, exactly; its slope $\kappa$ by the Hellmann-Feynman rule (Section 14.19; Notebook 14c) | `brane_band_slope` (both; the record keeps the earlier name), `ks_theory_json_slope` |
| the relativistic dispersion $\varepsilon(k)^2 = \varepsilon(0)^2 + \kappa^2k^2$ of the other free levels (Section 14.19; Notebook 14c) | derived in Section 14.19 (not a separate check of the record); Notebook 14c checks it numerically |
| the exact boundary identity of the tip angle (Section 14.20; Notebook 14c) | derived from `bc_self_adjoint_boundary_term`; verified numerically by the Rust check `free_tip_angle_boundary_identity` |
| $h_{\mathbf p}^2 = E^2$; $\rho = (nB + SC)/16$; Wick's rule; the exact local exchange; the ratio $-1/8$ (Section 14.26; Notebook 14d) | `gas_mode_projector`, `gas_angular_average`, `gas_densities`, `exchange_uniform_gas` (both), `gas_negative_energy_modes`, `hf_wick_contraction`, `filled_shell_ratio` |
| the Kohn-Sham potentials; the Lagrangian on shell (Section 14.27; Notebook 14d) | `ks_potentials`, `ks_onshell_lagrangian` (both), `ks_theory_json_exchange` |
| the exact Fock exchange of the closed-shell states and the term $+\tfrac{\lambda}{32}Q^2$ that the functional omits (Section 14.27; Notebook 14d) | `exchange_slab_exact_fock` (both) |
| a Kohn-Sham state depends on the coupling and the cell volume only through their ratio; the cell volume $\ell^3v_te^{(5/3)a_{4,0}}$ and the effective coupling $\hat\lambda e^{-(5/3)a_{4,0}}$ (Section 14.27; Notebook 14d) | `ks_coupling_volume_scaling`, `history_solver_units` (both) |

**COMPUTED** (numerical, with the record that holds the numbers and their measured accuracy):

| result (notebook) | record and measured accuracy |
| --- | --- |
| the 72 free levels at $k = 0$ by RK4 shooting, four cases including the slice 1.5 (Notebook 14b) | `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv`; check `free_k0_analytic_spectra` of `Revision/kohn_sham/reports/ks-rust-solver.json`; largest errors against the exact levels $7.23\times10^{-10}$ below $4m$ and $5.05\times10^{-8}$ above (tolerances $5\times10^{-9}$ and $3\times10^{-7}$); the notebook reproduces both and agrees with the Rust levels to $1.1\times10^{-14}$ |
| fourth-order convergence (Notebook 14b) | check `refined_free_spectra_convergence_order` of `Revision/kohn_sham/reports/ks-rust-determinism.json`: median error ratio 16.00 over 39 levels, largest errors $5.050\times10^{-8}$ and $3.157\times10^{-9}$, reproduced; over all 72 levels: 52 levels, median 16.00 |
| the fold band and three other levels for $k$ from 0 to 4 (Notebook 14c) | `Revision/kohn_sham/results/spectrum/brane-band.csv`; reproduced to $10^{-11}$; the band equals $\kappa k$ exactly (check `free_rescaling_relation_and_band_monotone`) |
| the numerical slope $e^{-a_{4,0}}$ at five slices, and for six other masses and cutoffs (Notebook 14c) | `Revision/kohn_sham/results/spectrum/brane-band-slope.csv`; check `free_brane_band_slope`: $2.05\times10^{-16}$ relative |
| the rescaling identity solved as separate problems (Notebook 14a, the partner parameters; Notebook 14c, 60 free levels) | `Revision/kohn_sham/results/rescaling/rescaling.csv`; checks `rescaling_identity_between_slices` and `rescaling_identity_energy_profiles`: levels to $1.643\times10^{-13}$, energies and profiles to $8.193\times10^{-13}$; free levels to $1.3\times10^{-15}$ (Rust) and $8.9\times10^{-16}$ (Notebook 14c) |
| the gap of the free $N = 8$ state, $0.25\,e^{-a_{4,0}}$, from $0.25$ to $0.0338\,m$ (Notebook 14c) | `Revision/kohn_sham/results/spectrum/closed-shells.csv` and `Revision/kohn_sham/results/ground/summary.csv`; reproduced to $10^{-13}$ |
| the two block-type symmetries (Notebook 14c) | check `free_block_type_symmetries`; reproduced to $10^{-12}$ |
| the tip angle: the band moves by at most $3.26\times10^{-2}$, the extended level by at least $6.157\times10^{-2}$ (Notebook 14c) | `Revision/kohn_sham/results/spectrum/tip-angle.csv`; check `free_tip_angle_boundary_identity`: identity to $1.09\times10^{-12}$ |
| the dependence on the cutoff $L$ from 3 to 6 (Section 14.20; the Revision record, not repeated by a notebook of this chapter) | `Revision/kohn_sham/tip_convergence/` (README); report `tip-convergence.json`, 7 of 7 checks PASS: the free fold-band gases do not depend on $L$; the bulk edge $1.2923$ is $1.0977$ at $L = 6$; the interacting $N = 8$ energy at $L = 3$ is 0.977, 0.674 and 0.215 of its large-$L$ value at $a_{4,0} = 0, 1, 2$ |
| the particle labels, the closed shells, the bulk edge and $N = 8, 592, 2352$ (Notebook 14c) | check `free_particle_branch_labels`; `closed-shells.csv`; `Revision/kohn_sham/results/parameters.json`; shells and names exact, energies to $10^{-11}$ |
| the state $N = 8$ along the history: $n_{\max}$ at five slices, $\lambda_1 = 157.7$, $\lambda_2 = 473.1$, exact-Fock energy 0 (Notebook 14d) | `Revision/kohn_sham/results/ground/summary.csv`; `parameters.json`; `Revision/kohn_sham/results/exx/exact-fock-variant.csv`; $10^{-9}$ relative; energies at most $5.0\times10^{-12}$ |

**ASSUMED** (starting points that this chapter does not derive):

- The good sector: the orbitals do not depend on the extra times $x_5, x_6, x_7$ (Section 14.3; Chapters 8 and 10 give the reasons).
- That both fold conditions, $b(0) = 0$ and $a(0) = 0$, are solved and filled at the fold where the two halves of a cell meet; with it the weight $w = \tfrac12$ of the densities (Section 14.12). The metric is degenerate at the fold and no junction condition across it is derived.
- The regular tip condition at the cutoff $y = -L$, $L = 3$: a choice of the numerical model. Its angle moves the fold band little and the extended levels much (Section 14.20); the cutoff position matters as the Revision record measured for $L = 3$ to $6$: not at all for the free fold-band gases away from the fold, decisively for the $k = 0$ levels off the band, for $N = 2352$ at $a_{4,0} = 0$ and for the interacting zero modes at the later slices (Section 14.20).
- The deflating history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = 1$, $b_4(0) = 1$ is a **prescribed background**: the Kohn-Sham states are computed on it but are not its source in the field equations of $a_4$ and $b_4$ (`Revision/field_equations_a4/reports/ks-source-conditions.json`; Chapter 17). The Kohn-Sham gas is a test field.
- The stationary-slice (adiabatic) ansatz: at each slice the instantaneous Kohn-Sham states are computed (Section 14.3); whether the gas can follow the history is measured in Chapter 15.
- The convention that counts the zero modes at $k = 0$ as particle levels (Section 14.21).
- The functional: Hartree plus the uniform-gas exchange, without correlation (an approximation; the exact Fock exchange differs by $+\tfrac{\lambda}{32}Q^2$ and is reported as a diagnostic, Section 14.27).
- The canonical numbers $H = m = 1$, $L = 3$, $\Delta k = 0.25$, $v_t = 1$, the five slices, and the calibration rule of the couplings.

**HYPOTHESIS:** none in this chapter.

**OPEN:** the justification of the zero-mode convention; the time-dependent (non-adiabatic) evolution of the gas along the history; the action of the gas back on $a_4$ and $b_4$ (the history is not a solution of the coupled equations); the correlation energy of the contact interaction in this geometry; what, if anything, joins the field across the fold; the limit of a distant cutoff where the Revision record does not establish it (the free state $N = 2352$ at $a_{4,0} = 0$, whose occupied set changes from $L = 3.5$ on, and the interacting states $N = 2352$ at $a_{4,0} = 0$, whose self-consistent iteration fails at larger $L$; with the calibration rule applied at each $L$ the couplings go to zero, Section 14.20).

**Honesty about pairs and charges (rule of Chapter 0).** One place of this chapter touches the pairing of universes: the chirality matrix $\Gamma$ maps every solution with the mass $M$ onto a solution with the mass $-M$ (Section 14.6), and with the two fold conditions exchanged and the tip angle $\theta \to \pi - \theta$ it carries a whole Kohn-Sham state with $(m, \lambda, \theta)$ to one with $(-m, +\lambda, \pi - \theta)$ (Section 14.12). These are exact maps between sets of solutions; Chapters 18 and 19 prove the theorems T1 and T3 built on them. Neither says that a universe, or a pair of universes, is created: no creation process, rate or amplitude follows from these equations (Chapter 20 gives the complete list of what is and is not proved). The words particle and sea in Section 14.21 describe the filling of the Kohn-Sham levels, not matter and antimatter (Chapter 21). The local conservation of the U(1) charge is proved; its total is constant only under the ASSUMED no-flux condition at the ends of the interval of $z$, which the fold and tip conditions of this chapter supply (Section 14.12). The gammas of this theory are real; plain complex conjugation of a real field changes nothing and is not a charge conjugation; the charge-conjugation matrices are $\mathcal C_+ = C$ and $\mathcal C_- = \Gamma C$ (Chapter 5).

### 14.33 Exercises

**Exercise 14.1.** (a) From the scale factors of Section 14.2, show that in the coordinate $y$ the volume factor is $\sqrt{|g|} = e^{-a_4}b_4^2e^{3Hy}$, and compute the factor $e^{3Hy}$ at $y = -3$ for $H = 1$. (b) Compute the hidden scale $f$ and the momentum weight $\kappa$ at the slices $a_{4,0} = 0$ and $2$ of the history, and say at which points $y$ they hold. (c) A density per unit $y$ is turned into a proper density by dividing it by $\mathrm{Vol}_7e^{3Hy}$. Explain why the proper density of the zero modes is largest at the cutoff, although the orbitals sit at the fold.

**Answer 14.1.** (a) The scale factors are $f$, $e^{a_4}$ (three times), $1$ and $fe^{Hy}$ (three times), with $f = e^{-a_4}b_4^{1/2}$. The square root of the absolute value of the determinant of a diagonal metric is the product of the scale factors: $f\cdot e^{3a_4}\cdot f^3e^{3Hy} = e^{3a_4}f^4e^{3Hy}$, and $f^4 = e^{-4a_4}b_4^2$, so $\sqrt{|g|} = e^{-a_4}b_4^2e^{3Hy}$. At $y = -3$: $e^{-9} \approx 1.23\times10^{-4}$. (b) On the history $f = e^{-a_{4,0}/3}$ and $\kappa = e^{-a_{4,0}}$: at the slice 0 both are 1; at the slice 2, $f = e^{-2/3} \approx 0.5134$ and $\kappa = e^{-2} \approx 0.1353$. Both are the same at every $y$: neither contains $y$. (c) The zero-mode orbital gives the density per unit $y$ $4a^2 \propto e^{2fMy}$, largest at the fold. Dividing by $e^{3Hy}$ gives $n \propto e^{(2fM - 3H)y}$. Since $f \le 1$ and $M = H = 1$, $2fM - 3H \le -1 < 0$: the exponent is negative, so $n$ grows as $y$ decreases toward the tip. The proper 7-volume near the tip is so small ($e^{-9}$ at the cutoff) that the few quanta there are densely packed.

**Exercise 14.2.** Using the two rules of Section 14.5, show that $A_0A_1A_4 = -J$, and deduce from it the block form $A_4 \to j\sigma_1$. Then derive the block form of $\gamma^{(x_4)} = A_0A_4$.

**Answer 14.2.** $A_0A_1A_4 = \gamma^{(x_0)}\gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_0)}\gamma^{(x_4)}$. The first two factors give $(\gamma^{(x_0)})^2 = \eta_{00} = 1$, so the product is $\gamma^{(x_1)}\gamma^{(x_0)}\gamma^{(x_4)}$. Exchanging the first two factors (they anticommute) gives $-\gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_4)} = -J$. In a block of type $j$, $J$ is the number $j$, so $A_0A_1A_4 = -j$ there. With $A_0 \to \sigma_3$ and $A_1 \to -i\sigma_2$: $\sigma_3(-i\sigma_2) = -i\sigma_3\sigma_2 = -i(-i\sigma_1) = -\sigma_1$, so $-\sigma_1A_4 = -j$, and multiplying by $-\sigma_1$ from the left ($\sigma_1^2 = 1$): $A_4 = j\sigma_1$. Finally $\gamma^{(x_4)} = \gamma^{(x_0)}\gamma^{(x_0)}\gamma^{(x_4)} = A_0A_4 \to \sigma_3(j\sigma_1) = j\sigma_3\sigma_1 = ij\sigma_2$, as stated in Section 14.5.

**Exercise 14.3.** (a) Show that the column $\chi = (\cos\tfrac\theta2,\ i\sin\tfrac\theta2)$, that is $(a, b) = (\cos\tfrac\theta2, \sin\tfrac\theta2)$ in real form, satisfies $Q(\theta)\chi = \chi$ for $Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2$. (b) Show that the tip condition with $\theta = \pi$ is $a(-L) = 0$, and that the matrix $\sigma_2$ of Section 14.6 turns the canonical tip condition $b(-L) = 0$ into it.

**Answer 14.3.** (a) For $\chi = (a, ib)$ the products of Section 14.12 give $\sigma_3\chi = (a, -ib)$ and $\sigma_2\chi = (b, ia)$, so $Q\chi = \big(a\cos\theta + b\sin\theta,\ i(a\sin\theta - b\cos\theta)\big)$. With $a = \cos\tfrac\theta2$, $b = \sin\tfrac\theta2$ the first entry is $\cos\theta\cos\tfrac\theta2 + \sin\theta\sin\tfrac\theta2 = \cos(\theta - \tfrac\theta2) = \cos\tfrac\theta2 = a$, and the bracket of the second is $\sin\theta\cos\tfrac\theta2 - \cos\theta\sin\tfrac\theta2 = \sin(\theta - \tfrac\theta2) = \sin\tfrac\theta2 = b$ (the subtraction formulas of cosine and sine). So $Q\chi = \chi$. (b) For $\theta = \pi$, $Q = -\sigma_3$ and $(1 - Q)\chi = (1 + \sigma_3)\chi = (2\chi_1, 0)$, so the condition is $\chi_1(-L) = 0$, that is $a(-L) = 0$. The map $\chi \to \sigma_2\chi$ sends $(a, ib)$ to $(b, ia)$: a column with $b(-L) = 0$ goes to one whose first entry vanishes at $-L$. So $\sigma_2$ turns the tip angle $0$ into the tip angle $\pi$, the special case $\theta \to \pi - \theta$ of the theorem T3 (Chapter 19).

**Exercise 14.4.** Let $p$ be the cubic polynomial with the values $f_0$, $f_1$ and the derivatives $d_0$, $d_1$ at the two ends of an interval of length $h$. Show that its value at the midpoint is $\tfrac12(f_0 + f_1) + \tfrac h8(d_0 - d_1)$, the formula used by `orbital` in Notebooks 14b and 14c.

**Answer 14.4.** Measure the position from the midpoint, $s$, so that the ends are $s = \mp h/2$, and write $p(s) = A + Bs + Cs^2 + Ds^3$; the value at the midpoint is $A$. Then $p(\mp h/2) = A \mp Bh/2 + Ch^2/4 \mp Dh^3/8$ and $p'(\mp h/2) = B \mp Ch + 3Dh^2/4$. Adding the two values: $f_0 + f_1 = 2A + Ch^2/2$ (the odd terms cancel). Subtracting the two derivatives: $d_0 - d_1 = -2Ch$, so $C = (d_1 - d_0)/(2h)$. Hence $A = \tfrac12(f_0 + f_1) - Ch^2/4 = \tfrac12(f_0 + f_1) - \tfrac{h}{8}(d_1 - d_0) = \tfrac12(f_0 + f_1) + \tfrac h8(d_0 - d_1)$.

**Exercise 14.5.** For $M = 1$, $L = 2$ and the slice 0 (the second case of Notebook 14b, $f = 1$): (a) compute the lowest positive even level; (b) show that the lowest odd root $p_0$ lies between $\pi/4$ and $\pi/2$ and that no root lies between 0 and $\pi/4$; (c) the record gives the lowest odd level $1.519802561206\,m$; compute $p_0$ from it and check (b) and the condition $\tan(2p_0) = -p_0$.

**Answer 14.5.** (a) $\sqrt{1 + (\pi/2)^2} = \sqrt{3.4674011} = 1.8620959\,m$ (Section 14.13 with $n = 1$, $fL = 2$). (b) The roots of $\tan(pfL) = -p/M$ lie one in each interval $((n + \tfrac12)\pi/(fL), (n + 1)\pi/(fL))$; for $fL = 2$ the first is $(\pi/4, \pi/2)$. For $0 < p < \pi/4$ the angle $2p$ lies between 0 and $\pi/2$, where $\tan(2p) > 0 > -p$: no root. (c) $p_0 = \sqrt{\varepsilon^2 - M^2} = \sqrt{1.519802561206^2 - 1} = \sqrt{1.3097998} = 1.1444649$, which lies between $\pi/4 = 0.7854$ and $\pi/2 = 1.5708$. And $\tan(2\cdot1.1444649) = \tan(2.2889297) = -1.1444649$: the condition holds.

**Exercise 14.6.** (a) Verify by inserting that $\chi = (Ae^{fMy}, 0)$ solves $h_{+1}\chi = \kappa k\,\chi$ with both end conditions $b(0) = b(-L) = 0$, for every $k$, $M$, $L$ and $f$. (b) Derive the slope $d\varepsilon/dk$ at $k = 0$ a second time with the Hellmann-Feynman rule. (c) Evaluate the slope at the slice 1 and compare with Notebook 14c, Out [5]. (d) Why does the slope not depend on $M$ or $L$?

**Answer 14.6.** (a) With $b = 0$ the real form reads $a' = fMa$ and $0 = f(\varepsilon - \kappa k)a$ ($j = +1$). The first holds for $a = Ae^{fMy}$, because the derivative of $e^{fMy}$ is $fMe^{fMy}$; the second holds for $\varepsilon = \kappa k$. Since $b$ is zero everywhere, $b(0) = b(-L) = 0$. Nothing in this used particular values of $k$, $M$, $L$ or $f$. (b) $\partial h_{+1}/\partial k = \kappa\sigma_3$, and at $k = 0$ the orbital is the zero mode $(a, 0)$, for which $\chi^\dagger\sigma_3\chi = a^2 = \chi^\dagger\chi$; the rule gives $d\varepsilon/dk = \kappa\int a^2\,dy = \kappa$. (c) $\kappa = e^{-1} = 0.367879441171$; Out [5] prints $0.367879441171442$ for the slice 1 and $0.367879441171$ for all six masses and cutoffs at that slice. (d) The slope is the average of $\kappa$ over the orbital, weighted by $\chi^\dagger\sigma_3\chi/\chi^\dagger\chi = 1$; since $\kappa$ is the same at every $y$, the average is $\kappa$, whatever the shape of the orbital, which is what $M$, $L$ and $f$ change.

**Exercise 14.7.** (a) Using the relativistic dispersion of Section 14.19, compute the odd level of label 0 at the first lattice shell $k = 0.25$ at the slice 0, and compare with Notebook 14c, Out [3]. (b) At the slice 2 the lowest odd level at $k = 0$ is $1.735554\,m$ (Notebook 14c, Out [7]); compute the same level at $k = 0.25$ there. (c) Compare the gap between the fold band at $k = 0.25$ and this level at the two slices.

**Answer 14.7.** (a) At the slice 0, $\kappa = 1$:

$$
\varepsilon = \sqrt{\varepsilon(0)^2 + \kappa^2k^2} = \sqrt{1.2922928281^2 + 0.25^2} = \sqrt{1.6700209 + 0.0625} = 1.3162525417\,m ,
$$

the value of Out [3]. (b) At the slice 2, $\kappa k = 0.25\,e^{-2} = 0.0338338$, so

$$
\varepsilon = \sqrt{1.735554^2 + 0.0338338^2} = 1.735884\,m .
$$

(c) The band at $k = 0.25$ is $0.25\,m$ at the slice 0 and $0.0338\,m$ at the slice 2; the odd level lies $1.066\,m$ above it at the slice 0 and $1.702\,m$ above it at the slice 2. Along the history the band falls and the level rises: the band and the bulk move apart.

**Exercise 14.8.** For a single momentum at rest, $\mathbf p = 0$, show that the projector on the eight positive-energy modes is $G_0 = \tfrac12(1 - i\gamma^{(x_4)})$, that these eight modes, filled, give $\rho = \tfrac12(B + C)$, and deduce $n = S = 8$ and $e_x/e_H = -1/8$.

**Answer 14.8.** At $\mathbf p = 0$, $h_0 = M(-i\gamma^{(x_4)})$ and $E = M$, so $G_0 = \tfrac12(1 + h_0/E) = \tfrac12(1 - i\gamma^{(x_4)})$. Filled, the eight modes give $\rho = G_0B = \tfrac12(B + (-i\gamma^{(x_4)})B) = \tfrac12(B + C)$, by $(-i\gamma^{(x_4)})B = C$ (Section 14.26). Then $n = \mathrm{Tr}(B\rho) = \tfrac12(\mathrm{Tr}\,B^2 + \mathrm{Tr}\,BC) = \tfrac12(16 + 0) = 8$ and $S = \mathrm{Tr}(C\rho) = \tfrac12(\mathrm{Tr}\,CB + \mathrm{Tr}\,C^2) = 8$. With $n = S = 8$: $e_H = \tfrac\lambda2\cdot64 = 32\lambda$ and $e_x = -\tfrac{\lambda}{32}(64 + 64) = -4\lambda$, so $e_x/e_H = -\tfrac18$.

**Exercise 14.9.** Show that for any state built from orbitals with occupations $f_{\rm occ} \ge 0$ the densities at a point satisfy $S^2 + Q^2 \le n^2$, so that the possible states fill the disk of Figure 14d.3. When does the equality hold?

**Answer 14.9.** Each orbital contributes a vector $(s_i, q_i)$ with length $\sqrt{s_i^2 + q_i^2} = n_i$ (Section 14.27: for one orbital $S^2 + Q^2 = n^2$), times its weight $c_i = w\,g\,f_{\rm occ} \ge 0$. The state has $(S, Q) = \sum_i c_i(s_i, q_i)$ and $n = \sum_i c_in_i$. By the triangle inequality the length of a sum of vectors is at most the sum of their lengths: $\sqrt{S^2 + Q^2} \le \sum_i c_in_i = n$. Equality holds exactly when all contributing vectors point in the same direction, for example for a state built from one orbital shape, such as the eight zero modes, which all have $(s, q) = (0, n)$: the state $N = 8$ lies on the edge of the disk, at $S = 0$, $Q = n$.

**Exercise 14.10.** For the eight zero modes with $M = H = 1$, $L = 3$, $\ell = 8\pi$ and $v_t = 1$: (a) compute the largest proper density $n_{\max} = n(-3)$ at the slices 0 and 2 from $n = 4Pa^2$; (b) compute the couplings $\lambda_1$ and $\lambda_2$ by the calibration rule of Section 14.27; (c) compute the effective coupling of $\lambda_1$ in the coordinate cell at the slice 2; (d) explain why the exact-Fock energy of this state is zero for every $\lambda$, while the uniform-gas exchange is not.

**Answer 14.10.** (a) At the slice 0, $f = 1$: $a(-3)^2 = 2e^{-6}/(1 - e^{-6}) = 4.9698\times10^{-3}$, $P(-3) = e^{9}/(8\pi)^3 = 8103.08/15875.21 = 0.510424$, so $n_{\max} = 4\cdot0.510424\cdot4.9698\times10^{-3} = 1.01469\times10^{-2}$. At the slice 2, $f = 0.513417$: $a(-3)^2 = 2f\,e^{-6f}/(1 - e^{-6f}) = 4.9440\times10^{-2}$, $\mathrm{Vol}_7 = (8\pi)^3e^{10/3} = 445008.03$, $P(-3) = e^9/445008.03 = 1.82088\times10^{-2}$, so $n_{\max} = 3.60097\times10^{-3}$. Both agree with Notebook 14d, Out [13]. (b) The largest of the five values $n_{\max}/16$ is the one of the slice 0, $6.34179\times10^{-4}$; $0.1/6.34179\times10^{-4} = 157.684$ and $0.3/6.34179\times10^{-4} = 473.053$, rounded to four significant digits $\lambda_1 = 157.7$ and $\lambda_2 = 473.1$. (c) $\hat\lambda_{\rm eff} = 157.7\,e^{-10/3} = 157.7\cdot0.035674 = 5.626$. (d) The exact Fock exchange is $-\tfrac{\lambda}{32}(n^2 + S^2 - Q^2)$, and for the zero modes $S = 0$ and $Q = n$ at every point, so it vanishes identically; in the exact-Fock variant the potential on $(a, 0)$ is $\tfrac{\lambda}{16}(Q - n) = 0$, so the free orbitals stay exact solutions with the level 0 and the state has zero energy at every coupling. The uniform-gas exchange $-\tfrac{\lambda}{32}(n^2 + S^2) = -\tfrac{\lambda}{32}n^2$ is not zero: it misses the term $+\tfrac{\lambda}{32}Q^2$, which here cancels it exactly.

**Exercise 14.11.** (a) Compute the tail $a_0(-L)^2$ of the fold band at the slice 0 ($f = 1$, $M = 1$, $L = 3$) and the first-order estimate $\tan(\theta/2)\,a_0(-L)^2/f$ of its shift for $\theta = 0.5$ and $1$. (b) The record `tip-angle.csv` gives the shifts $-1.353\times10^{-3}$ and $-3.129\times10^{-3}$ at $k = 0.25$; compute the ratios to the estimate. (c) Explain the sign of the shifts with the boundary identity of Section 14.20.

**Answer 14.11.** (a) $a_0(-L)^2 = 2e^{-6}/(1 - e^{-6}) = 4.9698\times10^{-3}$. With $\tan(0.25) = 0.25534$ and $\tan(0.5) = 0.54630$ the estimates are $1.2690\times10^{-3}$ and $2.7150\times10^{-3}$. (b) $1.353/1.2690 = 1.066$ and $3.129/2.7150 = 1.152$: the estimate is good for small angles and worse for larger ones (the record's largest ratio over all cases is 2.127). (c) $(\varepsilon_\theta - \varepsilon_0)\int\chi_0^\dagger\chi_\theta\,dy = -(j/f)\,a_0(-L)\,b_\theta(-L)$. For $j = +1$, $a_0(-L) > 0$ (the band orbital is positive), $b_\theta(-L) = \tan(\theta/2)\,a_\theta(-L)$ has the sign of $a_\theta(-L)$, which is positive for the starting point $(\cos\tfrac\theta2, \sin\tfrac\theta2)$ with $0 < \theta < \pi$, and the overlap is close to $+1$. So the right side is negative and the level moves down.
