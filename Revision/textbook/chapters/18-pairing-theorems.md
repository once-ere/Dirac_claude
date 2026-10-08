## 18. The pairing theorems T1, T2 and Q

The author asked for a proof that "Universes of masses {+mass, -mass} are created in pairs", for the fermion field dirac16complex and for the commuting field dirac16complex00. This chapter gives, with complete line-by-line proofs, everything that the equations of this book actually establish about such pairs, and it says exactly where that stops. Three theorems are proved. **T1** (the chirality pairing): multiplying a field by the chirality matrix $\Gamma$ turns every configuration of the theory with mass $m$ and coupling $\lambda$ into a configuration of the theory with $-m$ and $-\lambda$, in every gravitational field, and reverses its energy, momentum, stresses, current and charge. **T2** (the mirror pairing): multiplying by the gamma matrix of the hidden direction and reflecting the hidden coordinate across the surface $z = \pi/2$ turns a solution with $(-m, \lambda)$ into a solution with $(m, \lambda)$ at EQUAL, not opposite, energy and charge; this uses the Z2 mirror construction, which is an assumption. **Q** (the quantum reading): for the quantised field dirac16complex the T1 image carries the opposite Krein matrix $-B$, so it is the same quantum system relabelled, while two independently quantised universes of masses $+m$ and $-m$ have identical one-particle spectra and energies that do not cancel. All three are exact maps between sets of solutions. None of them describes a process in which a universe, or a pair of universes, comes into being: no creation process, rate, probability or amplitude follows from these equations. Section 18.28 lists precisely what is not established.

### 18.1 What this chapter does

**The question, and the honest answer.** In this book a **universe of mass $m$** means a configuration of one of the two fields, with mass parameter $m$ and coupling $\lambda$, in the author's primordial gravitational field; usually it is a **solution**, a configuration that obeys the field equations. Two universes are **paired** when an explicit invertible rule takes every solution of the theory with mass $m$ to a solution of the theory with mass $-m$, and takes its Lagrangian, its energy-momentum tensor and its current to stated multiples of those of the partner. The author's request asks for more: that such universes are *created* in pairs at the big bang. That statement is a HYPOTHESIS of the author. The field equations of this book are equations for a field on a given gravitational background, together with their canonical quantisation; no equation of the book produces a universe from anything, so the creation of pairs cannot be proved from them, and it is not proved here. What can be proved is that the solutions come in partnered families, and with which signs their energies and charges are partnered. That is the content of this chapter.

**The plan.** Sections 18.2 to 18.4 set the stage: the words, the author's metric, its spin connection, the Lagrangian, the field equation, the energy-momentum tensor and the current. Section 18.5 proves four matrix lemmas; everything later rests on them. Notebook 18a checks them exactly (Sections 18.6 to 18.9). Sections 18.10 to 18.13 state and prove T1; Sections 18.14 to 18.16 state and prove T2. Notebook 18b proves both theorems again, as exact polynomial identities, in the author's metric with an arbitrary deflating history (Sections 18.17 to 18.20). Section 18.21 derives a family of exact solutions, the fields that depend only on the time; Sections 18.22 and 18.23 state and prove Q. Notebook 18c solves the field equations numerically and shows each theorem at work on actual solutions (Sections 18.24 to 18.27). Section 18.28 states what is not established, Section 18.29 collects the status of every result, and Sections 18.30 and 18.31 give exercises and their complete worked answers. The Kohn-Sham version of the pairing, theorem T3, is the subject of Chapter 19; the corollary C1 and the question of the title of Chapter 20, "Do universes come in pairs?", are treated there; matter and antimatter are the subject of Chapter 21.

**The three worked examples.** Each is a complete Jupyter notebook, complete in itself; you may run them in any order.

| notebook | what it computes | checks | figures |
| --- | --- | --- | --- |
| 18a | the author's gammas rebuilt from his formulas; the four matrix lemmas, exactly | 16 | 7 |
| 18b | T1 and T2 as exact sympy identities in the author's metric, both statistics | 20 | 5 |
| 18c | T1, T2 and Q on actual solutions: Runge-Kutta, spectra, Krein norms | 21 | 7 |

**Notation.** The author's coordinates are written $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates (scale factor $e^{a_4}\sin^{1/6}z$); $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which are time-like and DEFLATE EXPONENTIALLY (scale factor $e^{-a_4}\sin^{1/6}z$, with $a_4$ increasing); $x_8$ is the hidden space direction, with $z = 6Hx_8$ between 0 and $\pi/2$ and $H > 0$ the author's constant. The flat frame metric is $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in the order $x_1, \dots, x_8$; its entry for the direction $a$ is $\eta_{aa}$, and $\eta_{ab} = 0$ for $a \neq b$. The gamma matrices are the author's eight real $16 \times 16$ matrices; the one of the direction $x_a$ is written $\gamma^{(x_a)}$, or $\gamma^{(a)}$ for short. $I_{16}$ (also written 1) is the $16 \times 16$ identity matrix and $I_8$ the $8 \times 8$ one. For a matrix $M$, $M^T$ is its transpose (rows and columns exchanged), $M^*$ the matrix of the complex-conjugate entries and $M^\dagger = (M^T)^*$; for a real matrix $M^\dagger = M^T$. The letters $m$ and $\lambda$ are the mass and the coupling of the field. A statement is labelled PROVED (exact, with the verifying record and its check), COMPUTED (a numerical result with its accuracy), ASSUMED, HYPOTHESIS or OPEN.

**The records this chapter uses.** Every formula and number comes from these Revision records or from the chapter's own notebooks, which reproduce the records where they overlap (each such check prints the record file and the check name):

| record | what it holds |
| --- | --- |
| `Revision/algebra/gammas.json` | the eight gammas, $C$, $\Gamma$ and $B$ |
| `Revision/pairing/pairing-theory.json` | the theorems T1, T2, Q with hypotheses, proofs and data tables |
| `Revision/pairing/reports/wolfram-pairing.json` | the WolframScript verification of T1, T2, Q (101 checks, all PASS) |
| `Revision/pairing/reports/python-pairing.json` | the independent sympy verification (66 checks, all PASS) |
| `Revision/theory/reports/` | the field-theory checks used here: `python-field-theory.json`, `wolfram-field-theory.json`, `python-scope.json` |
| `Revision/lead_checks/reports/charge-conjugation-and-u1.json` | the charge-conjugation matrices and the charge (12 checks, all PASS) |
| `Revision/kohn_sham/results/parameters.json` | the canonical deflating history $a_4 = AHx_4$, $A = 1$ |

The Wolfram side and the sympy side share no code; the sympy side rebuilds the gammas from the author's formulas and compares them entry by entry with `gammas.json`. A report is a file in which a verifying program has recorded every check with its name, its verdict and a detail text; every check cited in this chapter has the verdict PASS. Below, a report is named by its file name only, for example "`python-pairing.json`, check `gammas.Gamma`". The Revision document that collects these proofs is `Revision/docs/PAIR_CREATION_PROOFS.md`; this chapter follows its logic and adds every intermediate line.

### 18.2 The words of this chapter

- **Configuration**: any field $\Psi$, that is, 16 components $\Psi_1(x), \dots, \Psi_{16}(x)$ given at every point $x$, whether or not it obeys the field equations. A statement that holds for every configuration holds **off shell**; one that holds only for solutions holds **on shell**. An off-shell identity holds in particular on shell.
- **Statistics**: dirac16complex has complex ANTICOMMUTING components, called **Grassmann** numbers ($\theta_1\theta_2 = -\theta_2\theta_1$, so $\theta\theta = 0$); dirac16complex00 has complex COMMUTING components (ordinary complex numbers). "Both statistics" means: the statement and its proof hold for both kinds of components.
- **Parameters**: the mass $m$ and the coupling $\lambda$ of the potential $U(S) = \frac{\lambda}{2}S^2$. The theory with the parameters $(m, \lambda)$ and the theory with $(-m, -\lambda)$ are two DIFFERENT theories: their Lagrangians are different functions of the field.
- **Map**: a rule that turns a field $\Psi$ into a new field $\Psi'$. All maps of this chapter are of the form $\Psi'(x) = M\Psi(x)$ with a constant $16 \times 16$ matrix $M$, possibly combined with a change of the coordinate $x_8$.
- **Bilinear**: an expression $\Psi^\dagger X\Phi = \sum_{A,B}\Psi_A^*X_{AB}\Phi_B$ with a matrix $X$ of numbers or of ordinary functions; $X$ is its **kernel**.
- **Dirac adjoint**: the row $\bar\Psi = \Psi^\dagger C$, with the charge matrix $C$ of Chapter 5. The **scalar** is $S = \bar\Psi\Psi = \Psi^\dagger C\Psi$.
- **Chirality**: the matrix $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\cdots\gamma^{(x_7)}$, the product of all eight gammas in the author's order (the author's T16[8]).
- **Chiral halves**: the components 1 to 8 of $\Psi$, written $\psi_-$ (where $\Gamma = -1$), and 9 to 16, written $\psi_+$ (where $\Gamma = +1$).
- **Reflection** $R_n$: the $8 \times 8$ diagonal matrix with $-1$ in place $n$ and $+1$ elsewhere; it reverses the direction $n$ and keeps $\eta$: $R_n\eta R_n = \eta$.
- **Pin(4,4)**: the group of all products of unit vectors $v = \sum_a v_a\gamma^{(a)}$ with $\sum_a\eta_{aa}v_a^2 = \pm1$ (Chapter 5). Each single gamma is such a unit vector, so every product of gammas belongs to Pin(4,4).
- **Character** of a map $M$: the sign $\chi$ in $M^\dagger CM = \chi C$. It says whether $S$ keeps ($\chi = +1$) or reverses ($\chi = -1$) its sign under $\Psi \to M\Psi$.
- **Krein matrix** $B = -iC\gamma^{(x_4)}$: the charge density is $\Psi^\dagger B\Psi$, and $B$ is the matrix of the canonical anticommutator of the quantised field (Chapter 10). $B$ has eight eigenvalues $+1$ and eight $-1$; the number $u^\dagger Bu$ of a column $u$ is its **Krein norm**, which can be negative. The **Krein sign** of a map $M$ is the sign $\sigma$ in $MBM^\dagger = \sigma B$.
- **Patch, mirror patch, brane**: $z = 6Hx_8$ runs over the **patch** $0 < z < \pi/2$. The map $z \to \pi - z$ takes it to the **mirror patch** $\pi/2 < z < \pi$. The surface $z = \pi/2$ between them is the **brane**. Gluing the mirror patch to the patch at the brane is the **Z2 construction** of the Revision record; it is ASSUMED.
- **Isometry**: a change of coordinates that does not change the metric.
- **Jet**: at one point, the values of the 16 components, of their 16 complex conjugates and of their $8 \times 16 + 8 \times 16$ first derivatives: 288 numbers. A Lagrangian at a point is a polynomial in these 288 numbers.
- **Negative control**: a computation that must FAIL. It shows that a test can detect a wrong statement.

### 18.3 The stage: the author's metric, its frame and its spin connection

**The metric.** The author's line element, in his coordinates, is

$$
\begin{aligned}
ds^2 = {} & e^{2a_4}\sin^{1/3}z\,(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 \\
& - e^{-2a_4}\sin^{1/3}z\,(dx_5^2 + dx_6^2 + dx_7^2) + \cot^2 z\,dx_8^2 ,
\end{aligned}
$$

with $a_4 = a_4(x_4)$ and $z = 6Hx_8$. It is diagonal: $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$ with the **vielbein factors**

$$
f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z,\quad f_4 = 1,\quad f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z,\quad f_8 = \cot z .
$$

The **diagonal vielbein** is $e^a{}_\mu = f_\mu\delta^a_\mu$, its inverse $e^\mu{}_a = \delta^\mu_a/f_a$, and the curved gammas are $\gamma^\mu = e^\mu{}_a\gamma^{(a)} = \gamma^{(\mu)}/f_\mu$ (no sum) and $\gamma_\mu = g_{\mu\mu}\gamma^\mu = \eta_{\mu\mu}f_\mu\gamma^{(\mu)}$. The volume factor is the product of the eight factors:

$$
\sqrt{|g|} = f_1f_2\cdots f_8 = \big(e^{a_4}\sin^{1/6}z\big)^3\cdot1\cdot\big(e^{-a_4}\sin^{1/6}z\big)^3\cdot\cot z .
$$

The rule $\sqrt{|\det g|} = \prod_\mu|g_{\mu\mu}|^{1/2}$ for a diagonal metric gave this line.

$$
\sqrt{|g|} = e^{3a_4 - 3a_4}\sin^{6/6}z\cdot\frac{\cos z}{\sin z} = \cos z .
$$

The powers of $e^{a_4}$ cancel (the inflation of 3-space is compensated by the deflation of the extra times), the six powers $\sin^{1/6}z$ multiply to $\sin z$, and $\cot z = \cos z/\sin z$. So $\sqrt{|g|} = \cos z$ for every history $a_4$ (record: `wolfram-pairing.json`, check `primordial_vielbein`; Notebook 18b checks it).

**The canonical spin connection, derived for a diagonal vielbein.** A spinor field needs a **spin connection** $\omega_{\mu ab}$ to define its covariant derivative (Chapter 6). The canonical one is fixed by the **vielbein postulate**, which says that the gammas are covariantly constant; its solution is

$$
\omega_\mu{}^a{}_b = e^a{}_\nu\big(\partial_\mu e^\nu{}_b + \Gamma^\nu{}_{\mu\lambda}e^\lambda{}_b\big),\qquad \omega_{\mu ab} = \eta_{aa}\,\omega_\mu{}^a{}_b ,
$$

where $\Gamma^\nu{}_{\mu\lambda}$ are the Christoffel symbols of the metric (Chapter 3). (In this chapter the symbol $\Gamma$ WITH indices is a Christoffel symbol; WITHOUT indices it is the chirality matrix.) For a diagonal metric the Christoffel symbols with three different indices vanish, and for $a \neq b$

$$
\Gamma^a{}_{ab} = \frac{\partial_bg_{aa}}{2g_{aa}},\qquad \Gamma^a{}_{bb} = -\frac{\partial_ag_{bb}}{2g_{aa}} .
$$

These are the Christoffel formula $\Gamma^\nu{}_{\mu\lambda} = \frac{1}{2}g^{\nu\nu}(\partial_\mu g_{\nu\lambda} + \partial_\lambda g_{\nu\mu} - \partial_\nu g_{\mu\lambda})$ with a diagonal $g$, in which only the terms with two equal indices survive. Now take a direction $a$ and a different direction $b$, and compute the component of the connection whose derivative index is $\mu = a$:

$$
\omega_a{}^a{}_b = e^a{}_a\big(\partial_ae^a{}_b + \Gamma^a{}_{a\lambda}e^\lambda{}_b\big) = f_a\Big(0 + \Gamma^a{}_{ab}\frac{1}{f_b}\Big) .
$$

The inverse vielbein is diagonal, so $e^a{}_b = 0$ for $a \neq b$ and $e^\lambda{}_b = \delta^\lambda_b/f_b$ keeps only $\lambda = b$.

$$
\Gamma^a{}_{ab} = \frac{\partial_b(\eta_{aa}f_a^2)}{2\eta_{aa}f_a^2} = \frac{2\eta_{aa}f_a\,\partial_bf_a}{2\eta_{aa}f_a^2} = \frac{\partial_bf_a}{f_a} .
$$

We inserted $g_{aa} = \eta_{aa}f_a^2$ and used the chain rule $\partial_b(f_a^2) = 2f_a\partial_bf_a$.

$$
\omega_a{}^a{}_b = f_a\,\frac{\partial_bf_a}{f_a}\,\frac{1}{f_b} = \frac{\partial_bf_a}{f_b},\qquad \omega_{a,ab} = \eta_{aa}\frac{\partial_bf_a}{f_b} .
$$

The first equation inserts the line before into the line before that; the second lowers the index $a$ with $\eta_{aa}$. The component with the derivative index $b$ follows in the same way from $\Gamma^a{}_{bb}$: $\omega_{b,ab} = -\eta_{bb}\,\partial_af_b/f_a = -\omega_{b,ba}$, which is the same formula with $a$ and $b$ exchanged and the antisymmetry $\omega_{\mu ab} = -\omega_{\mu ba}$. Components whose three indices are all different contain a Christoffel symbol with three different indices and vanish, and $\omega_\mu{}^a{}_a = f_a(-\partial_\mu f_a/f_a^2 + \partial_\mu f_a/f_a^2) = 0$. So **the only nonzero components are $\omega_{a,ab} = \eta_{aa}\,\partial_bf_a/f_b$ and $\omega_{a,ba} = -\omega_{a,ab}$, for $a \neq b$.**

**The twelve components in the author's metric.** The factors depend only on $x_4$ (through $a_4$) and on $x_8$ (through $z$), and $\partial_8 = 6H\,d/dz$ because $z = 6Hx_8$. Write $a_4' = da_4/dx_4$.

- $a = 1$, $b = 4$: $\eta_{11} = 1$, $\partial_4f_1 = a_4'e^{a_4}\sin^{1/6}z$ (chain rule), $f_4 = 1$, so $\omega_{x_1,x_1x_4} = a_4'e^{a_4}\sin^{1/6}z$.
- $a = 1$, $b = 8$: $\partial_8f_1 = 6H\,e^{a_4}\,\tfrac16\sin^{-5/6}z\cos z = He^{a_4}\sin^{-5/6}z\cos z$ (power rule and chain rule); dividing by $f_8 = \cos z/\sin z$ gives $\omega_{x_1,x_1x_8} = He^{a_4}\sin^{1/6}z$.
- $a = 5$, $b = 4$: $\eta_{55} = -1$, $\partial_4f_5 = -a_4'e^{-a_4}\sin^{1/6}z$, so $\omega_{x_5,x_5x_4} = +a_4'e^{-a_4}\sin^{1/6}z$, and by antisymmetry $\omega_{x_5,x_4x_5} = -a_4'e^{-a_4}\sin^{1/6}z$.
- $a = 5$, $b = 8$: $\partial_8f_5 = He^{-a_4}\sin^{-5/6}z\cos z$; with $\eta_{55} = -1$ and the division by $f_8$: $\omega_{x_5,x_5x_8} = -He^{-a_4}\sin^{1/6}z$.
- $x_2, x_3$ repeat $x_1$, and $x_6, x_7$ repeat $x_5$. $f_4 = 1$ is constant and $f_8$ depends only on $x_8$, so $a = 4$ and $a = 8$ give nothing.

That is $3 \times 2 + 3 \times 2 = 12$ nonzero components with $a < b$, exactly the list of the record (`python-pairing.json`, check `geometry.spin_connection_components`); Notebooks 18b and 18c reproduce the list character for character. Note that $\Omega_{x_4} = \Omega_{x_8} = 0$: no component has the derivative index 4 or 8.

**What enters the field equation: $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$.** The spinor connection is $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$ with the generators $S^{ab} = \frac14[\gamma^{(a)}, \gamma^{(b)}]$, which equal $\frac12\gamma^{(a)}\gamma^{(b)}$ for $a \neq b$ (two different gammas anticommute, so $\gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)} = 2\gamma^{(a)}\gamma^{(b)}$). For the inflating direction $x_1$:

$$
\Omega_{x_1} = \omega_{x_1,x_1x_4}S^{14} + \omega_{x_1,x_1x_8}S^{18} = \tfrac12\omega_{x_1,x_1x_4}\gamma^{(1)}\gamma^{(4)} + \tfrac12\omega_{x_1,x_1x_8}\gamma^{(1)}\gamma^{(8)} .
$$

The two terms $\omega_{\mu ab}S^{ab}$ and $\omega_{\mu ba}S^{ba}$ of the sum are equal (both factors change sign), which cancels the $\frac12$ of the definition; then $S^{ab} = \frac12\gamma^{(a)}\gamma^{(b)}$.

$$
\gamma^{x_1}\Omega_{x_1} = \frac{\gamma^{(1)}}{f_1}\,\Omega_{x_1} = \frac{1}{2f_1}\big(\omega_{x_1,x_1x_4}\gamma^{(4)} + \omega_{x_1,x_1x_8}\gamma^{(8)}\big) = \frac{a_4'}{2}\gamma^{(4)} + \frac{H}{2}\gamma^{(8)} .
$$

We used $\gamma^{(1)}\gamma^{(1)} = \eta_{11} = +1$ (Clifford relation), and the factor $1/f_1 = e^{-a_4}\sin^{-1/6}z$ cancels the factor $e^{a_4}\sin^{1/6}z$ of both components. For the deflating extra time $x_5$:

$$
\gamma^{x_5}\Omega_{x_5} = \frac{\gamma^{(5)}}{2f_5}\big(\omega_{x_5,x_4x_5}\gamma^{(4)}\gamma^{(5)} + \omega_{x_5,x_5x_8}\gamma^{(5)}\gamma^{(8)}\big) .
$$

This is the same construction with the two components of $x_5$ ($S^{45} = \frac12\gamma^{(4)}\gamma^{(5)}$ and $S^{58} = \frac12\gamma^{(5)}\gamma^{(8)}$).

$$
\gamma^{(5)}\gamma^{(4)}\gamma^{(5)} = -\gamma^{(4)}\gamma^{(5)}\gamma^{(5)} = -\gamma^{(4)}(-1) = \gamma^{(4)},\qquad \gamma^{(5)}\gamma^{(5)}\gamma^{(8)} = -\gamma^{(8)} .
$$

Two different gammas anticommute, and a time-like gamma squares to $\eta_{55} = -1$.

$$
\gamma^{x_5}\Omega_{x_5} = \frac{1}{2f_5}\big(-a_4'e^{-a_4}\sin^{1/6}z\,\gamma^{(4)} + He^{-a_4}\sin^{1/6}z\,\gamma^{(8)}\big) = -\frac{a_4'}{2}\gamma^{(4)} + \frac{H}{2}\gamma^{(8)} .
$$

We inserted the two components and cancelled $f_5 = e^{-a_4}\sin^{1/6}z$. Adding the three inflating and the three deflating directions (and nothing from $x_4$ and $x_8$):

$$
\gamma^\mu\Omega_\mu = 3\Big(\frac{a_4'}{2}\gamma^{(4)} + \frac{H}{2}\gamma^{(8)}\Big) + 3\Big(-\frac{a_4'}{2}\gamma^{(4)} + \frac{H}{2}\gamma^{(8)}\Big) = 3H\gamma^{(x_8)} .
$$

The $a_4'$ terms of the three inflating directions and of the three deflating extra times cancel exactly; the hidden-direction terms add. This is PROVED for every history $a_4(x_4)$ (`python-field-theory.json`, check `gamma_mu_Omega_mu_equals_3H_gamma_x8`; `wolfram-field-theory.json`, check `gammaOmega_equals_3H_gamma_x8`; Notebook 18b recomputes it direction by direction and draws it in its figure 1). The value $3H\gamma^{(x_8)}$ belongs to the diagonal vielbein: in another frame it changes (`python-scope.json`; Chapter 8). None of the theorems below depends on it: T1 holds for every connection, and T2 uses only the transformation of the connection.

### 18.4 The Lagrangian, the field equation, the energy-momentum tensor and the current

**The Lagrangian.** Both fields have the same Lagrangian density; only the statistics of the components differ:

$$
\mathcal{L}_{m,\lambda}[\Psi] = \sqrt{|g|}\,\Big[K[\Psi] - mS - \frac{\lambda}{2}S^2\Big],\qquad K = \frac12\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big),\qquad S = \bar\Psi\Psi ,
$$

with the covariant derivatives $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$ and $D_\mu\bar\Psi = \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu$, and a sum over $\mu = 1, \dots, 8$ in $K$. $K$ is the **kinetic term**, $mS$ the **mass term**, $\frac{\lambda}{2}S^2$ the **potential**. For a general potential $U(S)$ we write $\mathcal{L}_{m,U}$. The Lagrangian is real for both statistics (Chapter 7).

**The kinetic term written out.** Inserting $\gamma^\mu = e^\mu{}_a\gamma^{(a)}$ and the two covariant derivatives into $K$:

$$
K = \frac12\sum_{\mu,a}e^\mu{}_a\big(\bar\Psi\gamma^{(a)}\partial_\mu\Psi - \partial_\mu\bar\Psi\gamma^{(a)}\Psi\big) + \frac12\sum_{\mu,a}e^\mu{}_a\big(\bar\Psi\gamma^{(a)}\Omega_\mu\Psi + \bar\Psi\Omega_\mu\gamma^{(a)}\Psi\big) .
$$

The derivative parts give the first sum; the connection parts $+\bar\Psi\gamma^{(a)}\Omega_\mu\Psi$ (from $D_\mu\Psi$) and $-(-\bar\Psi\Omega_\mu)\gamma^{(a)}\Psi$ (from $D_\mu\bar\Psi$) give the second.

$$
K = \frac12\sum_{\mu,a}e^\mu{}_a\big(\bar\Psi\gamma^{(a)}\partial_\mu\Psi - \partial_\mu\bar\Psi\gamma^{(a)}\Psi\big) + \frac14\sum_{\mu,a,b,c}e^\mu{}_a\,\omega_{\mu bc}\,\bar\Psi\{\gamma^{(a)}, S^{bc}\}\Psi .
$$

We inserted $\Omega_\mu = \frac12\sum_{b,c}\omega_{\mu bc}S^{bc}$ and wrote $\gamma^{(a)}S^{bc} + S^{bc}\gamma^{(a)} = \{\gamma^{(a)}, S^{bc}\}$, the **anticommutator**. This form shows the structure that every proof below uses: $K$ is a sum of **coefficient functions** of the gravitational field ($e^\mu{}_a$, $\omega_{\mu bc}$; and $\sqrt{|g|}$ in front of $\mathcal{L}$) times **bilinears** whose kernels are $C\gamma^{(a)}$ and $C\gamma^{(a)}S^{bc}$, $CS^{bc}\gamma^{(a)}$, products of one or three gammas after $C$.

**The field equation.** Chapter 7 derived the Euler-Lagrange equations of $\mathcal{L}_{m,U}$; for both statistics they are

$$
E_{m,U}[\Psi] \equiv \gamma^\mu D_\mu\Psi - \big(m + U'(S)\big)\Psi = 0,\qquad (D_\mu\bar\Psi)\gamma^\mu = -\big(m + U'(S)\big)\bar\Psi ,
$$

with $U'(S) = \lambda S$ for $U = \frac{\lambda}{2}S^2$; we write $E_{m,\lambda}$. The record proves that the Euler-Lagrange expression of $\Psi^*_A$ derived from $\mathcal{L}$ is exactly $\sqrt{|g|}\,[CE_{m,\lambda}]_A$ (`python-pairing.json`, check `T1.metric.commuting.euler_lagrange_derived` and its Grassmann twin; Notebook 18b repeats it). In the author's metric, with $\gamma^\mu = \gamma^{(\mu)}/f_\mu$, $\partial_8 = 6H\,d/dz$ and $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$, the field equation reads

$$
\begin{aligned}
& e^{-a_4}\sin^{-1/6}z\,\big(\gamma^{(1)}\partial_1 + \gamma^{(2)}\partial_2 + \gamma^{(3)}\partial_3\big)\Psi + \gamma^{(4)}\partial_4\Psi \\
& \quad + e^{a_4}\sin^{-1/6}z\,\big(\gamma^{(5)}\partial_5 + \gamma^{(6)}\partial_6 + \gamma^{(7)}\partial_7\big)\Psi \\
& \quad + \tan z\,\gamma^{(8)}\partial_8\Psi + 3H\gamma^{(8)}\Psi = (m + \lambda S)\Psi .
\end{aligned}
$$

The derivative terms are $\gamma^\mu\partial_\mu\Psi$ with $1/f_\mu$ written out ($1/\cot z = \tan z$); the last term on the left is $\gamma^\mu\Omega_\mu\Psi$. The deflation of the extra times appears as the growing factor $e^{a_4}$ in front of their derivatives.

**The energy-momentum tensor and the current.** The pairing record uses the symmetric tensor

$$
T_{\mu\nu} = \frac14\big(\bar\Psi\gamma_\mu D_\nu\Psi + \bar\Psi\gamma_\nu D_\mu\Psi - (D_\mu\bar\Psi)\gamma_\nu\Psi - (D_\nu\bar\Psi)\gamma_\mu\Psi\big) - g_{\mu\nu}\frac{\mathcal{L}}{\sqrt{|g|}} ,
$$

which is minus the tensor of Chapter 9; in this convention the energy density is $\rho = -T_{x_4x_4}$ and the pressure of a direction $\mu \neq x_4$ is $p_\mu = -g^{\mu\mu}T_{\mu\mu}$. The current is a multiple of $\bar\Psi\gamma^\mu\Psi$: the theory record and Notebook 18c use $J^\mu = -i\bar\Psi\gamma^\mu\Psi$, whose time component is the charge density $J^{x_4} = -i\Psi^\dagger C\gamma^{(x_4)}\Psi = \Psi^\dagger B\Psi$, with the charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ of a slice $x_4 = \mathrm{const}$; the sympy pairing checker and Notebook 18b use $i\bar\Psi\gamma^\mu\Psi$, the Wolfram checker $\bar\Psi\gamma^\mu\Psi$. Every statement of this chapter about $T$ and $J$ has the form $T' = \pm T$ or $J' = \pm J$; such a statement is unchanged when $T$ or $J$ is multiplied by any fixed number, so the different conventions do not matter.

### 18.5 Four matrix lemmas

Every map of this chapter multiplies the field by a constant matrix. The lemmas below say what such a multiplication does to the adjoint, to bilinears, to the connection and to the Krein matrix. They are exact identities between the author's matrices. We use only the Clifford relation $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta_{ab}I_{16}$, the reality of the gammas, $(\gamma^{(a)})^T = \eta_{aa}\gamma^{(a)}$, and the facts about $C$ proved in Chapter 5: $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$ is real and symmetric, $CC = 1$, and

$$
C\gamma^{(a)}C^{-1} = -(\gamma^{(a)})^T \qquad\text{for every } a .
$$

**Rule P (moving a gamma through a product).** If $X$ is a product of $k$ gammas, $\gamma^{(a)}X = \pm X\gamma^{(a)}$, with one factor $-1$ for each factor of $X$ different from $\gamma^{(a)}$ (they anticommute) and $+1$ for each factor equal to $\gamma^{(a)}$ (it commutes with itself). This is the Clifford relation applied once per factor.

**Lemma 1 (the chirality).** $\Gamma$ is real and symmetric, $\Gamma\Gamma = 1$, $\Gamma\gamma^{(a)} = -\gamma^{(a)}\Gamma$ for every $a$, $\Gamma C = C\Gamma$ and $\Gamma S^{ab} = S^{ab}\Gamma$. Hence $\Gamma\Omega_\mu = \Omega_\mu\Gamma$ for EVERY connection $\Omega_\mu = \frac12\sum\omega_{\mu ab}S^{ab}$, and

$$
D_\mu(\Gamma\Psi) = \Gamma D_\mu\Psi,\qquad D_\mu(\bar\Psi\Gamma) = (D_\mu\bar\Psi)\Gamma .
$$

*Proof.* $\Gamma$ is the product of all eight different gammas. Moving $\gamma^{(b)}$ through it passes the seven factors $\gamma^{(a)}$, $a \neq b$, and the factor $\gamma^{(b)}$ itself; by Rule P the sign is $(-1)^7 = -1$, so $\gamma^{(b)}\Gamma = -\Gamma\gamma^{(b)}$. $C$ is a product of four gammas and $S^{ab}$ ($a \neq b$) is $\frac12$ times a product of two; moving $\Gamma$ through them costs $(-1)^4 = +1$ and $(-1)^2 = +1$, so both commute with $\Gamma$ ($S^{aa} = 0$ trivially). The product $\Gamma$ of the author's gammas is computed exactly: $\Gamma = \mathrm{diag}(-I_8, I_8)$, which is real, symmetric and squares to $1$. Since every $\Omega_\mu$ is a combination of the $S^{ab}$ with ordinary numbers as coefficients, $\Gamma$ commutes with it. Finally

$$
D_\mu(\Gamma\Psi) = \partial_\mu(\Gamma\Psi) + \Omega_\mu\Gamma\Psi = \Gamma\partial_\mu\Psi + \Gamma\Omega_\mu\Psi = \Gamma D_\mu\Psi .
$$

The constant $\Gamma$ passes through $\partial_\mu$ (a constant factor comes out of a derivative), and $\Omega_\mu\Gamma = \Gamma\Omega_\mu$. The adjoint statement is the same computation from the right. QED.

| statement | status | where it is verified |
| --- | --- | --- |
| Lemma 1 | PROVED | `wolfram-pairing.json`, check `Gamma_properties`; `python-pairing.json`, checks `gammas.Gamma` and `gammas.Gamma_anticommutes`; Notebook 18a, In [6] and In [7] |

**Lemma 2 (bilinears under $\Psi \to \Gamma\Psi$).** For $\Psi' = \Gamma\Psi$: $\bar\Psi' = \bar\Psi\Gamma$, and $\bar\Psi'X\Psi' = (-1)^k\,\bar\Psi X\Psi$ for every product $X$ of $k$ gammas. In particular $S$ is unchanged and every bilinear with the kernel $C\gamma^{(a)}$, $C\gamma^{(a)}S^{bc}$ or $CS^{bc}\gamma^{(a)}$ changes sign. Moreover $\Gamma B\Gamma = -B$.

*Proof.* Line by line:

$$
\bar\Psi' = (\Gamma\Psi)^\dagger C = \Psi^\dagger\Gamma^\dagger C .
$$

This is the definition of the adjoint and the rule $(MN)^\dagger = N^\dagger M^\dagger$ (the dagger of a product reverses the order).

$$
\Psi^\dagger\Gamma^\dagger C = \Psi^\dagger\Gamma C = \Psi^\dagger C\Gamma = \bar\Psi\Gamma .
$$

$\Gamma$ is real and symmetric, so $\Gamma^\dagger = \Gamma^T = \Gamma$; then $\Gamma C = C\Gamma$ (Lemma 1); then the definition $\bar\Psi = \Psi^\dagger C$.

$$
\bar\Psi'X\Psi' = \bar\Psi\,\Gamma X\Gamma\,\Psi .
$$

We inserted $\bar\Psi' = \bar\Psi\Gamma$ and $\Psi' = \Gamma\Psi$.

$$
\Gamma X\Gamma = (-1)^kX\,\Gamma\Gamma = (-1)^kX .
$$

Moving the left $\Gamma$ through the $k$ factors of $X$ costs $(-1)^k$ (Lemma 1: $\Gamma$ anticommutes with each gamma); then $\Gamma\Gamma = 1$. For $S$, $X = 1$ and $k = 0$; for the kinetic kernels $k = 1$; for the connection kernels $\gamma^{(a)}S^{bc}$ and $S^{bc}\gamma^{(a)}$ with $b \neq c$, $k = 3$ (when $a$ equals $b$ or $c$, two factors combine to $\eta_{aa}$ and one gamma is left, $k = 1$: odd in every case). Finally

$$
\Gamma B\Gamma = -i\,\Gamma C\gamma^{(x_4)}\Gamma = -i\,C\,\Gamma\gamma^{(x_4)}\Gamma = -i\,C(-\gamma^{(x_4)}) = +iC\gamma^{(x_4)} = -B .
$$

The definition $B = -iC\gamma^{(x_4)}$; then $\Gamma C = C\Gamma$; then the line before with $k = 1$. QED. Nowhere were two field components exchanged: only the numbers of the matrices were moved, and every $\Psi^*$ still stands to the left of every $\Psi$. So Lemma 2 holds for commuting and for Grassmann components alike.

| statement | status | where it is verified |
| --- | --- | --- |
| Lemma 2 for $S$ and the 456 kinetic and connection kernels | PROVED | `python-pairing.json`, check `T1.general_field.matrix_identities`; `wolfram-pairing.json`, checks `T1_kernel_scalar` and `T1_kernel_kinetic` |
| Lemma 2 for all 512 triples $(a, b, c)$ and the field-equation kernels | PROVED | `wolfram-pairing.json`, checks `T1_kernel_connection` and `T1_kernel_field_equation` |
| $\Gamma B\Gamma = -B$ | PROVED | `wolfram-pairing.json`, check `Q_Krein_metric_of_images`; `python-pairing.json`, check `Q.image_krein_metric` |
| the sign $(-1)^k$ for all 256 products of different gammas | PROVED | Notebook 18a, In [9] and In [10] |

**Lemma 3 (the eight reflections).** Let $n$ be one of the eight directions and $R_n$ its reflection.

1. $(\gamma^{(n)})^TC\gamma^{(n)} = -\eta_{nn}C$.
2. $\gamma^{(n)}\gamma^{(a)}(\gamma^{(n)})^{-1} = -(R_n)_{aa}\gamma^{(a)}$, and $\gamma^{(n)}S^{ab}(\gamma^{(n)})^{-1} = (R_n)_{aa}(R_n)_{bb}S^{ab}$.
3. $P_n := \Gamma\gamma^{(n)}$ is plus or minus the product of the seven other gammas, hence an element of Pin(4,4); $P_n^{-1}\gamma^{(a)}P_n = (R_n)_{aa}\gamma^{(a)}$ (it **covers** the reflection $R_n$: it acts on the gammas exactly as $R_n$ acts on the directions); its character is $\chi_n = -\eta_{nn}$, that is $P_n^\dagger CP_n = -\eta_{nn}C$: $-1$ for the space-like $x_1, x_2, x_3, x_8$ and $+1$ for the time-like $x_4, x_5, x_6, x_7$; and $\Gamma P_n = \gamma^{(n)}$.

*Proof of 1.* Multiply $C\gamma^{(n)}C^{-1} = -(\gamma^{(n)})^T$ on the right by $C$: $C\gamma^{(n)} = -(\gamma^{(n)})^TC$. Then

$$
(\gamma^{(n)})^TC\gamma^{(n)} = (\gamma^{(n)})^T\big(-(\gamma^{(n)})^TC\big) = -\big((\gamma^{(n)})^T\big)^2C = -\big((\gamma^{(n)})^2\big)^TC = -\eta_{nn}C .
$$

We replaced $C\gamma^{(n)}$, collected the two transposes, used $(M^T)^2 = (M^2)^T$ and the Clifford relation $(\gamma^{(n)})^2 = \eta_{nn}I_{16}$.

*Proof of 2.* $(\gamma^{(n)})^{-1} = \eta_{nn}\gamma^{(n)}$, because $\gamma^{(n)}\eta_{nn}\gamma^{(n)} = \eta_{nn}^2 = 1$. For $a \neq n$: $\gamma^{(n)}\gamma^{(a)}(\gamma^{(n)})^{-1} = -\gamma^{(a)}\gamma^{(n)}(\gamma^{(n)})^{-1} = -\gamma^{(a)}$ (anticommute, then cancel), and $-(R_n)_{aa} = -1$. For $a = n$: $\gamma^{(n)}\gamma^{(n)}(\gamma^{(n)})^{-1} = \gamma^{(n)}$, and $-(R_n)_{nn} = +1$. The statement for $S^{ab} = \frac12\gamma^{(a)}\gamma^{(b)}$ ($a \neq b$) follows by inserting $(\gamma^{(n)})^{-1}\gamma^{(n)} = 1$ between the two factors: the two signs $-(R_n)_{aa}$ and $-(R_n)_{bb}$ multiply to $(R_n)_{aa}(R_n)_{bb}$.

*Proof of 3.* $\Gamma\gamma^{(n)}$ is the ordered product of the eight gammas followed by $\gamma^{(n)}$. Moving the last factor to its place next to the factor $\gamma^{(n)}$ inside $\Gamma$ passes some of the other gammas, each costing a sign (Rule P); then $\gamma^{(n)}\gamma^{(n)} = \eta_{nn}$. So $P_n = \pm\eta_{nn}\times$ (the product of the seven other gammas in their order), a product of unit vectors, which lies in Pin(4,4). Next, with $(\gamma^{(n)})^{-1} = \eta_{nn}\gamma^{(n)}$ and $\Gamma^{-1} = \Gamma$:

$$
P_n^{-1}\gamma^{(a)}P_n = (\gamma^{(n)})^{-1}\Gamma\gamma^{(a)}\Gamma\gamma^{(n)} = -(\gamma^{(n)})^{-1}\gamma^{(a)}\gamma^{(n)} = (R_n)_{aa}\gamma^{(a)} .
$$

The inverse of a product reverses the order; $\Gamma\gamma^{(a)}\Gamma = -\gamma^{(a)}$ (Lemma 2 with $k = 1$); and item 2, read with $(\gamma^{(n)})^{-1}$ on the left, which gives the same signs. For the character, $P_n$ is real, so $P_n^\dagger = P_n^T = (\gamma^{(n)})^T\Gamma^T = (\gamma^{(n)})^T\Gamma$:

$$
P_n^\dagger CP_n = (\gamma^{(n)})^T\,\Gamma C\Gamma\,\gamma^{(n)} = (\gamma^{(n)})^TC\gamma^{(n)} = -\eta_{nn}C .
$$

We used $\Gamma C\Gamma = C\Gamma\Gamma = C$ (Lemma 1) and item 1. Finally $\Gamma P_n = \Gamma\Gamma\gamma^{(n)} = \gamma^{(n)}$. QED. The signs of $P_n$ relative to the product of the other seven gammas, in the order of $\Gamma$, are $+1, -1, +1, +1, -1, +1, -1, -1$ for $n = x_1, \dots, x_8$ (computed exactly; they equal the data table `reflections` of `pairing-theory.json`).

| statement | status | where it is verified |
| --- | --- | --- |
| Lemma 3, items 1 to 3 | PROVED | `wolfram-pairing.json`, checks `T2_Pn_in_Pin44`, `T2_Pn_covers_the_reflection`, `T2_character_of_Pn`, `T2_Gamma_times_Pn_is_gamma_n` and `T2_kernels_gamma_n_with_frame_reflection` |
| the reflection table | PROVED | `python-pairing.json`, checks `T2.general_field.matrix_identities`, `T2.general_field.reflection_table` and `compare.theory.reflection_table`; Notebook 18a, In [12] and In [13] |

**Lemma 4 (the Krein signs of the maps).** $MBM^\dagger = \sigma_MB$, with $\sigma_\Gamma = -1$; $\sigma_{\gamma^{(n)}} = +1$ for $n = x_1, x_2, x_3, x_4, x_8$ and $-1$ for $n = x_5, x_6, x_7$; and $\sigma_{P_n} = -\sigma_{\gamma^{(n)}}$.

*Proof.* $\Gamma$ is real and symmetric, so $\Gamma B\Gamma^\dagger = \Gamma B\Gamma = -B$ by Lemma 2. For $M = \gamma^{(n)}$: transposing $C\gamma^{(n)}C^{-1} = -(\gamma^{(n)})^T$ and using $C^T = C = C^{-1}$ gives $\gamma^{(n)}C = -C(\gamma^{(n)})^T$. Then

$$
\begin{aligned}
\gamma^{(n)}B(\gamma^{(n)})^\dagger &= -i\,\gamma^{(n)}C\gamma^{(x_4)}(\gamma^{(n)})^T = i\,C(\gamma^{(n)})^T\gamma^{(x_4)}(\gamma^{(n)})^T \\
&= i\,\eta_{nn}^2\,C\gamma^{(n)}\gamma^{(x_4)}\gamma^{(n)} = i\,C\gamma^{(n)}\gamma^{(x_4)}\gamma^{(n)} .
\end{aligned}
$$

The definition of $B$ and $(\gamma^{(n)})^\dagger = (\gamma^{(n)})^T$ (real matrix); then the relation $\gamma^{(n)}C = -C(\gamma^{(n)})^T$; then $(\gamma^{(n)})^T = \eta_{nn}\gamma^{(n)}$ twice; then $\eta_{nn}^2 = 1$. For $n \neq 4$: $\gamma^{(n)}\gamma^{(x_4)}\gamma^{(n)} = -\gamma^{(x_4)}\gamma^{(n)}\gamma^{(n)} = -\eta_{nn}\gamma^{(x_4)}$, so the result is $-i\eta_{nn}C\gamma^{(x_4)} = \eta_{nn}B$: $+B$ for $x_1, x_2, x_3, x_8$ and $-B$ for $x_5, x_6, x_7$. For $n = 4$: $\gamma^{(4)}\gamma^{(4)}\gamma^{(4)} = -\gamma^{(4)}$, so the result is $-iC\gamma^{(4)} = +B$. For $P_n = \Gamma\gamma^{(n)}$: $P_nBP_n^\dagger = \Gamma\,\gamma^{(n)}B(\gamma^{(n)})^\dagger\,\Gamma = \sigma_{\gamma^{(n)}}\Gamma B\Gamma = -\sigma_{\gamma^{(n)}}B$. QED.

| statement | status | where it is verified |
| --- | --- | --- |
| Lemma 4, the 17 Krein signs | PROVED | `wolfram-pairing.json`, check `Q_Krein_metric_of_images`; `python-pairing.json`, checks `compare.theory.krein_signs` and `Q.T2_image_keeps_B`; data table `Krein_signs_M_B_Mdagger` of `pairing-theory.json`; Notebook 18a, In [17] |

**The block form.** Split $\Psi = (\psi_-, \psi_+)$ into its components 1 to 8 and 9 to 16. Because every gamma anticommutes with $\Gamma = \mathrm{diag}(-I_8, I_8)$, every gamma has nonzero entries only in the two off-diagonal $8 \times 8$ blocks (Chapter 5): it exchanges the two halves. The author's $\gamma^{(x_8)}$ has the identity $I_8$ in both off-diagonal blocks, so $\gamma^{(x_8)}(\psi_-, \psi_+) = (\psi_+, \psi_-)$. $C$, a product of four gammas, commutes with $\Gamma$ and is block diagonal; for the author's gammas $C = \mathrm{diag}(-\sigma, \sigma)$ with a real symmetric $8 \times 8$ matrix $\sigma$, so

$$
S = \Psi^\dagger C\Psi = -\psi_-^\dagger\sigma\psi_- + \psi_+^\dagger\sigma\psi_+ .
$$

Reading this line: reversing the sign of one half ($\Gamma$) keeps $S$; exchanging the two halves ($\gamma^{(x_8)}$) reverses $S$. The two halves are the two inequivalent irreducible 8-dimensional representations of Spin(4,4) (Chapter 5).

| statement | status | where it is verified |
| --- | --- | --- |
| the block form: every gamma exchanges the halves, $\gamma^{(x_8)}$ swaps them, $C = \mathrm{diag}(-\sigma, \sigma)$ | PROVED | Notebook 18a, In [16] |
| the two halves are the two inequivalent irreducible representations of Spin(4,4), exchanged by every gamma | PROVED | `python-algebra.json`, checks `spin_halves_irreducible`, `spin_halves_inequivalent` and `reflections_exchange_halves`; `wolfram-algebra.json`, check `Spin_Pin_reflection_swaps_halves` |

### 18.6 Example: Notebook 18a checks the four lemmas

Notebook 18a first answers the question that every later step depends on: are the matrices of the Revision record really the author's? It rebuilds the eight matrices T16A[0], ..., T16A[7] from the author's own formulas (the tau matrices), maps the author's frame order (0 = hidden, 1 to 3 = 3-space, 4 = time, 5 to 7 = extra times) to the coordinates $x_1, \dots, x_8$, and compares them entry by entry with `Revision/algebra/gammas.json`; it checks that they are real signed permutation matrices with entries $-1$, 0, $+1$ and that the 64 Clifford relations hold. Then it proves Lemmas 1 to 4 and the block form with exact whole-number arithmetic, compares the reflection table and the table of Krein signs with the data tables of the pairing record row by row, and draws seven teaching figures: the eight gammas, the sign flip $\Gamma\gamma^{(x_1)}\Gamma = -\gamma^{(x_1)}$, the parity of the 256 products, the reflection table, the chiral projectors, the block form and the Krein signs. Its last line is ALL 16 CHECKS PASSED (notebook 18a); it runs in about 15 seconds.

<!-- NOTEBOOK 18a -->

### 18.9 Line-by-line walk-through of Notebook 18a

The notebook has 19 code cells, In [1] to In [19]. This section explains every line of every one of them. The words of the notebook's section 3 (matrix, transpose, signed permutation matrix, projector, character, Krein sign) were defined in Sections 18.2 and 18.5.

**In [1], the set-up cell.** Its first part repeats the complete run instructions of Section 18.7 as **comment lines**: every line that starts with `#` is a comment, which Python skips; they are there so that the notebook file carries its own instructions. The code starts below the line THE SET-UP between two lines of `=` signs. This code is the same in every notebook of the book except for the line that names the notebook; it is explained here once, and the walk-throughs of Notebooks 18b and 18c refer back to this explanation. The texts in triple quotes below a `def` line are **docstrings**: they describe the function and do nothing when the code runs.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

`import` loads a **module** (a part of Python or of an installed package) so that the code can use it. `json` reads and writes JSON files (text files that hold names, lists and numbers), `os` reads environment variables, `textwrap` breaks long texts into lines, and `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system. matplotlib is the plotting package; its drawing functions are loaded under the short name `plt`. `Image` and `display` come from IPython, the part of Jupyter that runs Python code; together they show a saved picture below a cell.

```python
NOTEBOOK_ID = "18a"  # this notebook: chapter 18, example a
```

A **variable** is a name for a value. This line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"18a"`; the figure files and the last printed line use it.

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

`def` defines a **function**, a named piece of code that runs when it is called. `Path.cwd()` is the folder in which the notebook runs, and `.resolve()` writes it as a complete address. `here.parents` lists its parent folder, the parent of that, and so on; `[here, *here.parents]` is the list that starts with `here` and continues with all of them. The `for` loop takes the folders one after the other; `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If there is none, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

`REPO` is the repository folder found by the function; it is never printed, because it differs from computer to computer while the printed output of a notebook must not. `OUTPUT_ROOT` is the folder below which files are written. `os.environ` holds the **environment variables** (named texts that a program receives from the computer); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set and the repository folder otherwise. When you run the notebook the variable is not set; the book's checking tool sets it to a scratch folder, so that a check never changes the repository.

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

`repository_file("Revision/...")` returns the full path of a repository file, for reading a Revision record. `output_file("Revision/...")` returns the full path at which to write a file; before that, `path.parent.mkdir(parents=True, exist_ok=True)` creates its folder (and every missing folder above it) and does nothing if the folder exists.

```python
def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters, the width of a page of the book: `textwrap.fill` breaks the text at blanks, and every line after the first starts with four blanks. `str(text)` first turns any value into text.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to the built-in settings of matplotlib, so that the figures are the same on every computer. `plt.rcParams.update({...})` then sets the size of a figure (7.0 by 4.2 inches), the size of its letters (10 points) and a faint grid behind the curves. The braces make a **dictionary**, a collection of pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: each name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/18a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty dictionary `{}` and a line end into the captions file, which `save_figure` then fills; `encoding="utf-8"` fixes how letters are stored and `newline="\n"` stores the same line end on every system.

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

`save_figure` is called once for every figure. `setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far; so the figures are numbered 1, 2, 3, and a cell run twice keeps its number. The file name joins the notebook id, the number and the name, for example `18a_1_eight_gammas.png`. `fig.savefig` writes the picture as a PNG file with 150 dots per inch, cuts away the empty margin and stores no program name, so that two runs write the same bytes. `plt.close(fig)` removes the figure from memory (otherwise Jupyter would draw it a second time). The caption is stored, and the whole dictionary of captions is written to the captions file (`json.dumps` turns it into JSON text with sorted keys). `display(Image(...))` shows the saved picture below the cell, and the last line prints where it was saved.

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

`PASSED` is an empty **list**, an ordered collection written with square brackets. `check` is the function behind every check of the book. `condition` is either `True` or `False`. If it is false, `raise AssertionError(...)` stops the notebook with an error that names the check (Python's own statement `assert` is not used here, because Python started with the option `-O` skips it). If it is true, the name is appended to `PASSED` and the line PASS name is printed; when the optional third argument `record` names a Revision record, a second line says which record and which check the result reproduces.

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

`report` prints a key number as a line that starts with RESULT, followed by the unit when one is given (`a if condition else b` is `a` when the condition holds and `b` otherwise). `all_checks_passed` prints the last line of the notebook with the number of checks that passed (`len` is the length of a list). The last statement prints the single output line of In [1].

**In [2], the record helpers, the gammas and the Clifford relations.**

```python
import itertools  # all subsets of a list (for the 256 products of gammas)
from math import comb  # binomial coefficients: comb(8, k) = number of k-subsets

import numpy as np  # arrays and matrices

GAMMAS = "Revision/algebra/gammas.json"
THEORY = "Revision/pairing/pairing-theory.json"
PY = "Revision/pairing/reports/python-pairing.json"  # the sympy verifier's report
WL = "Revision/pairing/reports/wolfram-pairing.json"  # the Wolfram verifier's report
```

`itertools` provides `combinations`, used in In [9] to list all subsets of the eight directions; `comb(8, k)` is the binomial coefficient $\binom{8}{k}$, the number of ways to choose $k$ things out of 8. numpy, the package for arrays and matrices, is loaded under the short name `np`. The four constants are the repository paths of the four Revision records the notebook reads: the gammas, the pairing theory record and the two reports of the pairing verifiers.

```python
def read_json(relative):
    """Read a JSON file of the repository (a Revision record)."""
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))


def verdict(report_file, name):
    """The recorded verdict (PASS or FAIL) of the check name of a report."""
    for entry in read_json(report_file)["checks"]:
        if entry["name"] == name:
            return entry["verdict"].upper()
    return "MISSING"
```

`read_json` reads a record file as text and turns it into Python objects (`json.loads`). `verdict` reads a report and looks through its list `"checks"`; each entry is a dictionary with the keys `name`, `verdict` and `detail`. It returns the verdict of the check with the given name in capital letters (`.upper()`; the two pairing reports write PASS, but some other Revision reports write pass in small letters, and the comparison should not depend on that), or `"MISSING"` if the report has no such check.

```python
def reproduces(condition, name, *sources, table=None):
    """check(condition, name), which also requires every named check of every
    source (report_file, [check names]) to have the recorded verdict PASS; table
    names a data table of the theory record that the result equals."""
    recorded = all(verdict(report_file, n) == "PASS"
                   for report_file, names in sources for n in names)
    parts = [f"{report_file}, check {', '.join(names)}"
             for report_file, names in sources]
    if table is not None:
        parts.insert(0, f"{THEORY}, data table {table}")
    check(condition and recorded, name, record="; ".join(parts))
```

`reproduces` is the check used whenever a result repeats a Revision record. `*sources` collects any number of pairs (report file, list of check names). `recorded` is true only when every named check of every named report has the verdict PASS: `all(...)` is true when every item of the following **generator expression** (a `for` loop written inside parentheses) is true. `parts` builds the text that names the reports and checks (`", ".join(names)` joins the names with commas); if a data table of the theory record is named, its text is put first. Finally `check` is called: the check passes only when the notebook's own result (`condition`) holds AND the record says PASS.

```python
fixture = read_json(GAMMAS)
gamma = {a: np.array(fixture["gamma"][a - 1], dtype=np.int64) for a in range(1, 9)}
eta = {a: int(fixture["eta"][a - 1]) for a in range(1, 9)}  # +1 or -1
I16 = np.eye(16, dtype=np.int64)


def same(M, N):
    """True when the two matrices are equal entry by entry (exact for integers)."""
    return np.array_equal(M, N)
```

`fixture` is the dictionary read from `gammas.json`. Its entry `"gamma"` is a list of eight matrices, each a list of 16 rows of 16 whole numbers; the **dictionary comprehension** `{a: ... for a in range(1, 9)}` stores the matrix of the direction $x_a$ under the key `a`, as a numpy array of 64-bit whole numbers (`dtype=np.int64`). With whole numbers every product below is exact: nothing is rounded. `range(1, 9)` runs through 1, 2, ..., 8 (the end is excluded), and `fixture["gamma"][a - 1]` takes the entry number `a - 1` because Python counts list places from 0. `eta` holds $\eta_{aa}$, and `I16` is the identity matrix (`np.eye`). `same(M, N)` is true when two matrices are equal entry by entry; for whole numbers that comparison is exact.

```python
say("eta = " + str([eta[a] for a in range(1, 9)]) + " for x1, ..., x8")
reproduces(all(same(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                    2 * (eta[a] if a == b else 0) * I16)
               for a in range(1, 9) for b in range(1, 9)),
           "the 64 Clifford relations hold exactly",
           (WL, ["fixture_Clifford_relation"]), (PY, ["gammas.clifford"]))
```

The first line prints the list of the eight values $\eta_{aa}$: `[1, 1, 1, -1, -1, -1, -1, 1]`, the signature (4,4) in the order $x_1, \dots, x_8$. The second statement checks the Clifford relation for all $8 \times 8 = 64$ pairs $(a, b)$: `@` is the matrix product, so `gamma[a] @ gamma[b] + gamma[b] @ gamma[a]` is $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)}$, compared with $2\eta_{aa}I_{16}$ when $a = b$ and with the zero matrix otherwise. It names the Wolfram check `fixture_Clifford_relation` and the sympy check `gammas.clifford`. Out [2] shows the PASS line and the record line.

**In [3], are these the author's matrices?** The markdown cell before it lists the author's five construction steps; the code follows them one by one.

```python
def perm_sign(seq):
    """The permutation sign of a list of numbers: +1 (even number of exchanges
    sorts it), -1 (odd number), 0 (two entries are equal)."""
    if len(set(seq)) != len(seq):
        return 0
    inversions = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq))
                     if seq[i] > seq[j])  # pairs in the wrong order
    return -1 if inversions % 2 else 1


def kd(p, q):
    """The Kronecker delta: 1 if p = q, else 0."""
    return 1 if p == q else 0
```

`perm_sign` computes the **permutation sign** of a list of numbers. `set(seq)` keeps each different number once; if it is shorter than the list, two entries are equal and the sign is 0. Otherwise the code counts the **inversions**, the pairs of places $i < j$ whose numbers stand in the wrong order (`seq[i] > seq[j]`); sorting the list needs an even number of exchanges exactly when this count is even, so the sign is $+1$ for an even and $-1$ for an odd count (`inversions % 2` is the remainder after division by 2). `kd(p, q)` is the Kronecker delta.

```python
I4, Z4 = np.eye(4, dtype=np.int64), np.zeros((4, 4), dtype=np.int64)
I8, Z8 = np.eye(8, dtype=np.int64), np.zeros((8, 8), dtype=np.int64)
s4, t4 = {}, {}
for h in (1, 2, 3):  # step 1: the self-dual and anti-self-dual 4 x 4 blocks
    Qa = np.array([[perm_sign([h, p, q, 4]) for q in range(1, 5)]
                   for p in range(1, 5)])
    Qb = np.array([[kd(p, 4) * kd(q, h) - kd(p, h) * kd(q, 4) for q in range(1, 5)]
                   for p in range(1, 5)])
    s4[h], t4[h] = Qa - Qb, Qa + Qb
```

`np.eye(4)` and `np.zeros((4, 4))` are the $4 \times 4$ identity and zero matrices; the line with `I8, Z8` makes the $8 \times 8$ ones. Step 1: for $h = 1, 2, 3$, `Qa` is the $4 \times 4$ table of the permutation signs of the arrangements $(h, p, q, 4)$ for $p, q = 1, \dots, 4$ (rows $p$, columns $q$), and `Qb` the table $\delta_{p4}\delta_{qh} - \delta_{ph}\delta_{q4}$; the author's blocks are $s_h = Q_a - Q_b$ and $t_h = Q_a + Q_b$.

```python
tau = {0: I8}  # step 2: the eight tau matrices
for h in (1, 2, 3):
    tau[h] = np.block([[Z4, s4[h]], [s4[h], Z4]])
    tau[7 - h] = np.block([[Z4, t4[h]], [-t4[h], Z4]])
tau[7] = tau[1] @ tau[2] @ tau[3] @ tau[4] @ tau[5] @ tau[6]
sigma4 = np.block([[Z4, I4], [I4, Z4]])  # step 3: tau-bar
taubar = {A: sigma4 @ tau[A].T @ sigma4 for A in range(8)}
T16A = {A: np.block([[Z8, taubar[A]], [tau[A], Z8]]) for A in range(8)}  # step 4
frame_index = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 0}  # step 5: x_a -> A
rebuilt_equal = all(same(T16A[frame_index[a]], gamma[a]) for a in range(1, 9))
```

Step 2: `tau[0]` is $I_8$; for $h = 1, 2, 3$, `np.block` assembles an $8 \times 8$ matrix from four $4 \times 4$ blocks: $\tau_h$ has $s_h$ in both off-diagonal blocks, $\tau_{7-h}$ has $t_h$ above and $-t_h$ below; $\tau_7$ is the product $\tau_1\tau_2\cdots\tau_6$. Step 3: $\bar\tau_A = \sigma\tau_A^T\sigma$ with $\sigma$ the $8 \times 8$ matrix with $I_4$ in both off-diagonal blocks (`.T` is the transpose). Step 4: the $16 \times 16$ matrix T16A[A] has $\bar\tau_A$ in the upper-right and $\tau_A$ in the lower-left block. Step 5: `frame_index` maps the author's coordinate $x_a$ to his frame number: $x_8$ to 0 (the hidden direction) and $x_1, \dots, x_7$ to $1, \dots, 7$. `rebuilt_equal` is true when every rebuilt matrix equals the record's matrix of the same direction.

```python
raw = fixture["gamma"]  # the numbers exactly as stored in the record
eight_real = (len(raw) == 8 and all(len(M) == 16 and all(len(row) == 16 for row in M)
                                    for M in raw)
              and all(type(x) is int and x in (-1, 0, 1)
                      for M in raw for row in M for x in row))
signed_perm = all((np.abs(gamma[a]).sum(axis=0) == 1).all()
                  and (np.abs(gamma[a]).sum(axis=1) == 1).all() for a in range(1, 9))
transpose_rule = all(same(gamma[a].T, eta[a] * gamma[a]) for a in range(1, 9))
say(f"8 matrices of 16 x 16 real entries -1, 0, +1: {eight_real}; signed "
    f"permutation matrices: {signed_perm}; transpose = eta_aa times the matrix: "
    f"{transpose_rule}; equal to the author's T16A rebuilt from the formulas: "
    f"{rebuilt_equal}")
reproduces(eight_real and signed_perm and transpose_rule and rebuilt_equal,
           "the record holds the author's eight real 16 x 16 gamma matrices",
           (PY, ["gammas.equal_wolfram_fixture"]))
```

`raw` is the list of numbers exactly as stored in the record (before numpy touched them). `eight_real` checks that there are 8 matrices, each with 16 rows of 16 entries, and that every entry is a Python whole number (`type(x) is int`, so no complex number and no fraction) equal to $-1$, 0 or $+1$. `signed_perm` checks the defining property of a signed permutation matrix: the absolute values `np.abs` sum to 1 in every column (`axis=0`) and in every row (`axis=1`). `transpose_rule` checks $(\gamma^{(a)})^T = \eta_{aa}\gamma^{(a)}$: the space-like gammas are symmetric and the time-like ones antisymmetric. The cell prints the four results and checks them together against `gammas.equal_wolfram_fixture`, the sympy check that compared its own rebuilt gammas with the record. Out [3] prints True four times and the PASS line: **the record holds the author's eight real $16 \times 16$ matrices**, and every computation of this chapter uses them.

**In [4], the first figure: the eight gammas.**

```python
from matplotlib.colors import LinearSegmentedColormap  # colour scales

BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
DIVERGING = LinearSegmentedColormap.from_list(
    "blue_grey_red", ["#184f95", "#f0efec", "#e34948"])
```

`LinearSegmentedColormap.from_list` makes a **colour scale** that runs from dark blue (for $-1$) through light grey (0) to red ($+1$). The four colour constants are a blue, an orange, a green and a grey that colour-blind readers can tell apart; they are written as hexadecimal colour codes.

```python
def draw_matrix(ax, matrix, title, ticks=True):
    """Heat map of a real 16 x 16 matrix with entries between -1 and +1."""
    image = ax.imshow(matrix, cmap=DIVERGING, vmin=-1.0, vmax=1.0)
    places = [0, 7, 15] if ticks else []  # label rows and columns 1, 8, 16
    ax.set_xticks(places, [str(t + 1) for t in places])
    ax.set_yticks(places, [str(t + 1) for t in places])
    ax.axhline(7.5, color=GREY, linewidth=0.8)  # the border between the halves
    ax.axvline(7.5, color=GREY, linewidth=0.8)
    ax.grid(False)  # no grid lines on top of the squares
    ax.set_title(title, fontsize=10)
    return image
```

`draw_matrix` draws one matrix as a **heat map**, a grid of coloured squares, one per entry. `ax` is one panel of a figure. `imshow` draws the squares with the colour scale fixed between $-1$ and $+1$ (`vmin`, `vmax`), so that equal numbers always get equal colours. The tick marks label the rows and columns 1, 8 and 16 (Python counts from 0, so the places are 0, 7 and 15 and the labels add 1). `axhline(7.5)` and `axvline(7.5)` draw thin lines between the rows 8 and 9 and the columns 8 and 9, the border between the two chiral halves. `ax.grid(False)` removes the grid, and the title is written above the panel. The function returns the drawn image, which the colour bar needs.

```python
fig, axes = plt.subplots(2, 4, figsize=(11.0, 6.0))
for a, ax in zip([1, 2, 3, 4, 5, 6, 7, 8], axes.flat):
    kind = "space-like" if eta[a] == 1 else "time-like"
    image = draw_matrix(ax, gamma[a], f"$\\gamma^{{(x_{a})}}$ ({kind})")
fig.colorbar(image, ax=list(axes.flat), shrink=0.7, label="entry")
save_figure(fig, "eight_gammas",
            "The author's eight real 16 by 16 gamma matrices, one heat map each, in "
            "the order $x_1$ to $x_8$ of the author's coordinates (top row: "
            "$x_1, x_2, x_3, x_4$; bottom row: $x_5, x_6, x_7, x_8$). Horizontal "
            "axis: column number, vertical axis: row number; red is $+1$, blue is "
            "$-1$, light grey is 0; thin lines separate the components 1 to 8 "
            "from 9 to 16. Every row and every column holds exactly one red or "
            "blue square (signed permutation matrices), no entry is complex, and "
            "every matrix has its squares only in the two off-diagonal blocks, so "
            "each gamma exchanges the two halves of a 16-component field.")
```

`plt.subplots(2, 4)` makes a figure with two rows of four panels, 11 by 6 inches. `zip` pairs the directions 1 to 8 with the panels (`axes.flat` lists the panels row by row). Each panel is titled with $\gamma^{(x_a)}$ and the word space-like or time-like; in the f-string, double braces `{{` and `}}` print single braces, and `\\` prints one backslash, so the title is LaTeX code. `fig.colorbar` adds the colour key. `save_figure` saves figure 18a.1 with its caption. **What you see in Figure 18a.1:** in every panel each row and each column has exactly one coloured square (signed permutation matrices), the squares lie only in the upper-right and lower-left $8 \times 8$ blocks (each gamma exchanges the two halves), and there are only the colours of $+1$ and $-1$: no entry is complex.

**In [5], C, Γ and B.**

```python
C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]  # the four space-like gammas
Gamma = I16.copy()
for a in [8, 1, 2, 3, 4, 5, 6, 7]:  # the order of the factors of Gamma
    Gamma = Gamma @ gamma[a]
B_over_i = -(C @ gamma[4])  # B = -i C gamma^(x4) = i * (-C gamma^(x4))
B = 1j * B_over_i  # the complex matrix B (entries 0, +i, -i)
B_file = np.array(fixture["B"]["re"]) + 1j * np.array(fixture["B"]["im"])
stored = (same(C, np.array(fixture["C"])) and same(Gamma, np.array(fixture["Gamma"]))
          and np.array_equal(B, B_file))
reproduces(stored, "C, Gamma and B built here equal the matrices of the gammas record",
           (WL, ["fixture_definitions"]))
```

$C$ is the product of the four space-like gammas in the author's order $x_8, x_1, x_2, x_3$. $\Gamma$ starts as a copy of the identity (`.copy()`, so that `I16` itself is not changed) and is multiplied on the right by the eight gammas in the order $x_8, x_1, \dots, x_7$. Because $B = -iC\gamma^{(x_4)}$ is $i$ times the real whole-number matrix $-C\gamma^{(x_4)}$, the cell keeps that real matrix as `B_over_i` and forms the complex matrix `B` with `1j`, Python's name for $i$. The record stores $B$ as a real part `"re"` and an imaginary part `"im"`, and `B_file` rebuilds it. `stored` compares the three matrices built here with the record's; the check names the Wolfram check `fixture_definitions`.

```python
basic = (same(C.T, C) and same(C @ C, I16)
         and all(same((C @ gamma[a]).T, -(C @ gamma[a])) for a in range(1, 9))
         and np.array_equal(B.conj().T, B) and np.array_equal(B @ B, np.eye(16))
         and np.array_equal(C @ gamma[4], 1j * B))
reproduces(basic, "C real symmetric, C^2 = 1, B Hermitian, B^2 = 1, C gamma^(x4) = i B",
           (WL, ["C_and_B_basic"]), (PY, ["gammas.C", "gammas.B"]))
```

`basic` checks five facts: $C^T = C$, $CC = 1$, every $C\gamma^{(a)}$ antisymmetric, $B^\dagger = B$ (`.conj().T` is the conjugate transpose) with $BB = 1$ (`np.eye(16)` is the identity), and $C\gamma^{(x_4)} = iB$. The last one is how $B$ enters the time-derivative term of the Lagrangian (Section 18.23). Out [5] shows two PASS lines.

**In [6], Lemma 1.**

```python
four_S = {(a, b): gamma[a] @ gamma[b] - gamma[b] @ gamma[a]  # 4 S^ab, whole numbers
          for a in range(1, 9) for b in range(1, 9)}
diagonal = same(Gamma, np.diag([-1] * 8 + [1] * 8))  # diag(-I8, I8)
real_symmetric_involution = same(Gamma.T, Gamma) and same(Gamma @ Gamma, I16)
anticommutes = all(same(Gamma @ gamma[a], -gamma[a] @ Gamma) for a in range(1, 9))
commutes_C = same(Gamma @ C, C @ Gamma)
commutes_S = all(same(Gamma @ M, M @ Gamma) for M in four_S.values())  # 64 pairs
say(f"Gamma = diag(-I8, I8): {diagonal}; real symmetric with Gamma^2 = 1: "
    f"{real_symmetric_involution}; anticommutes with all 8 gammas: {anticommutes}; "
    f"commutes with C: {commutes_C}; commutes with all 64 S^ab: {commutes_S}")
reproduces(diagonal and real_symmetric_involution and anticommutes and commutes_C
           and commutes_S, "Lemma 1: the chirality Gamma",
           (WL, ["Gamma_properties"]),
           (PY, ["gammas.Gamma", "gammas.Gamma_anticommutes"]))
```

`four_S` holds $4S^{ab} = \gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)}$ for all 64 pairs; with the factor 4 the entries are whole numbers, and a matrix commutes with $S^{ab}$ exactly when it commutes with $4S^{ab}$. `np.diag([-1] * 8 + [1] * 8)` is the diagonal matrix with eight entries $-1$ and eight $+1$ (`[-1] * 8` repeats the list eight times, `+` joins lists). The five results are: $\Gamma = \mathrm{diag}(-I_8, I_8)$; $\Gamma^T = \Gamma$ and $\Gamma\Gamma = 1$; $\Gamma\gamma^{(a)} = -\gamma^{(a)}\Gamma$ for all eight $a$; $\Gamma C = C\Gamma$; $\Gamma S^{ab} = S^{ab}\Gamma$ for all 64 pairs. Out [6] prints True five times and the PASS line for Lemma 1, with the records `Gamma_properties`, `gammas.Gamma` and `gammas.Gamma_anticommutes`.

**In [7], Γ commutes with a random connection.**

```python
rng = np.random.default_rng(12345)  # a fixed seed: the same numbers every run
omega = rng.normal(size=(9, 9))  # rows and columns 1..8 are used (row 0 unused)
omega = omega - omega.T  # antisymmetric: omega[a, b] = -omega[b, a]
Omega = sum(0.5 * omega[a, b] * four_S[(a, b)] / 4.0
            for a in range(1, 9) for b in range(1, 9))  # (1/2) omega_ab S^ab
commutator = np.abs(Gamma @ Omega - Omega @ Gamma).max()
check(commutator < 1e-12 and np.abs(Omega).max() > 0.1,
      "Gamma commutes with a random spin connection Omega (largest entry of the "
      "commutator below 1e-12)")
```

`np.random.default_rng(12345)` is a random-number generator with a fixed **seed**, so every run draws the same numbers. `rng.normal(size=(9, 9))` draws an array of $9 \times 9$ numbers from the normal (bell-curve) distribution; rows and columns 1 to 8 are used. `omega - omega.T` makes it antisymmetric, $\omega_{ab} = -\omega_{ba}$, as a connection must be. `Omega` is $\frac12\sum_{a,b}\omega_{ab}S^{ab}$, with $S^{ab}$ written as `four_S / 4.0`; `sum(...)` adds the 64 matrices. `commutator` is the largest absolute entry of $\Gamma\Omega - \Omega\Gamma$. The check requires it below $10^{-12}$ and requires $\Omega$ itself not to be tiny (largest entry above 0.1), so that the test is not empty. This is an illustration with floating-point numbers; the proof is the exact check of In [6].

**In [8], the second figure: Γ reverses every gamma.**

```python
flips = all(same(Gamma @ gamma[a] @ Gamma, -gamma[a]) for a in range(1, 9))
check(flips, "Gamma gamma^(a) Gamma = -gamma^(a) for all eight directions")
```

`flips` checks $\Gamma\gamma^{(a)}\Gamma = -\gamma^{(a)}$ for all eight directions, the identity behind T1.

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
draw_matrix(axes[0], Gamma, "$\\Gamma = \\mathrm{diag}(-I_8, I_8)$")
draw_matrix(axes[1], gamma[1], "$\\gamma^{(x_1)}$")
image = draw_matrix(axes[2], Gamma @ gamma[1] @ Gamma,
                    "$\\Gamma\\gamma^{(x_1)}\\Gamma = -\\gamma^{(x_1)}$")
fig.colorbar(image, ax=list(axes), shrink=0.8, label="entry")
save_figure(fig, "chirality_flips_gammas",
            "Heat maps of three 16 by 16 matrices: the chirality $\\Gamma$ (left), "
            "the gamma matrix $\\gamma^{(x_1)}$ of the first space direction "
            "(middle) and $\\Gamma\\gamma^{(x_1)}\\Gamma$ (right). Horizontal axis: "
            "column number, vertical axis: row number; red is $+1$, blue is $-1$, "
            "light grey is 0; thin lines separate the chiral halves, components 1 "
            "to 8 and 9 to 16. $\\Gamma$ is $-1$ on the first half and $+1$ on the "
            "second. $\\gamma^{(x_1)}$ has its entries only in the two off-diagonal "
            "blocks: it exchanges the halves. The right picture is the middle one "
            "with every colour reversed, because $\\Gamma$ anticommutes with every "
            "gamma. This sign is the whole content of the pairing theorem T1.")
```

A figure with three panels: $\Gamma$, $\gamma^{(x_1)}$ and $\Gamma\gamma^{(x_1)}\Gamma$, drawn with `draw_matrix`, a colour key, and `save_figure`. **What you see in Figure 18a.2:** $\Gamma$ is blue on the first eight diagonal places and red on the last eight; $\gamma^{(x_1)}$ has its squares only in the off-diagonal blocks; the right panel is the middle one with every colour reversed. Why: $\Gamma$ multiplies the rows 1 to 8 by $-1$ from the left and the columns 1 to 8 by $-1$ from the right, and every square of an off-diagonal block lies in exactly one of these rows or columns.

**In [9], Lemma 2 for all 256 products.**

```python
def sign_between(M, N):
    """+1 if M = N, -1 if M = -N, 0 otherwise (exact comparison)."""
    if same(M, N):
        return 1
    if same(M, -N):
        return -1
    return 0
```

`sign_between(M, N)` returns $+1$ if $M = N$, $-1$ if $M = -N$ and 0 otherwise, with exact comparisons.

```python
parity_ok = True
counts = {k: {1: 0, -1: 0} for k in range(9)}  # k -> number of products per sign
for k in range(9):
    for subset in itertools.combinations(range(1, 9), k):
        X = I16.copy()
        for a in subset:  # the product gamma^(a1) ... gamma^(ak)
            X = X @ gamma[a]
        s = sign_between(Gamma @ X @ Gamma, X)
        parity_ok = parity_ok and s == (-1) ** k
        counts[k][s] += 1
```

`counts[k]` counts, for each length $k = 0, \dots, 8$, the products with the sign $+1$ and with the sign $-1$. `itertools.combinations(range(1, 9), k)` lists every set of $k$ different directions in increasing order. For each, `X` is the product of their gammas (the empty product, $k = 0$, is the identity). `s` is the sign in $\Gamma X\Gamma = sX$; `parity_ok` stays true only if `s` equals $(-1)^k$ every time (`**` is the power).

```python
say("number of products of k different gammas, by the sign s: "
    + "; ".join(f"k={k}: {counts[k][1]} with s=+1, {counts[k][-1]} with s=-1"
                for k in range(9)))
check(parity_ok and all(counts[k][1] + counts[k][-1] == comb(8, k) for k in range(9)),
      "Gamma X Gamma = (-1)^k X for all 256 products X of k different gammas")
```

The cell prints the counts and checks that $s = (-1)^k$ always and that the number of products of length $k$ is $\binom{8}{k}$. Out [9] reads: $k = 0$: 1 product with $s = +1$; $k = 1$: 8 with $s = -1$; $k = 2$: 28 with $+1$; $k = 3$: 56 with $-1$; $k = 4$: 70 with $+1$; $k = 5$: 56 with $-1$; $k = 6$: 28 with $+1$; $k = 7$: 8 with $-1$; $k = 8$: 1 with $+1$. The total is $2^8 = 256$.

**In [10], the kernels of the Lagrangian.**

```python
kinetic = [C @ gamma[a] for a in range(1, 9)]
connection = [C @ gamma[a] @ four_S[(b, c)] for a in range(1, 9)
              for b in range(1, 9) for c in range(b + 1, 9)]
connection += [C @ four_S[(b, c)] @ gamma[a] for a in range(1, 9)
               for b in range(1, 9) for c in range(b + 1, 9)]
kernels = kinetic + connection
all_flip = all(same(Gamma @ X @ Gamma, -X) for X in kernels)
scalar_kept = same(Gamma @ C @ Gamma, C)
```

`kinetic` holds the 8 kernels $C\gamma^{(a)}$ of the kinetic bilinears. `connection` holds $C\gamma^{(a)}(4S^{bc})$ and $C(4S^{bc})\gamma^{(a)}$ for all $a$ and all $b < c$: $8 \times 28 = 224$ of each kind (`+=` appends the second list to the first). With the 8 kinetic kernels these are $8 + 224 + 224 = 456$ matrices, the list of the sympy verifier. `all_flip` checks $\Gamma X\Gamma = -X$ for all of them; since $\Gamma$ is real and symmetric, this is the change of the kernel of $\Psi^\dagger X\Psi$ under $\Psi \to \Gamma\Psi$. `scalar_kept` checks $\Gamma C\Gamma = C$, the kernel of $S$.

```python
triples = [C @ (gamma[a] @ four_S[(b, c)] + four_S[(b, c)] @ gamma[a])
           for a in range(1, 9) for b in range(1, 9) for c in range(1, 9)]
triples_flip = all(same(Gamma @ X @ Gamma, -X) for X in triples)
field_kernels = (all(same(Gamma @ gamma[a] @ Gamma, -gamma[a]) for a in range(1, 9))
                 and all(same(Gamma @ M @ Gamma, M) for M in four_S.values()))
krein_reversed = np.array_equal(Gamma @ B @ Gamma, -B)
```

`triples` holds the form of the Wolfram verifier, $C\{\gamma^{(a)}, 4S^{bc}\}$ for all $8^3 = 512$ triples $(a, b, c)$, and `triples_flip` checks that each changes sign. `field_kernels` checks the two kernels of the field equation: $\Gamma\gamma^{(a)}\Gamma = -\gamma^{(a)}$ and $\Gamma S^{bc}\Gamma = S^{bc}$. `krein_reversed` checks $\Gamma B\Gamma = -B$ (the last part of Lemma 2).

```python
report("number of kinetic and connection kernels", len(kernels))
report("number of triples (a, b, c)", len(triples))
reproduces(len(kernels) == 456 and all_flip and scalar_kept,
           "Lemma 2: all 456 kinetic and connection kernels flip, C is kept",
           (PY, ["T1.general_field.matrix_identities"]),
           (WL, ["T1_kernel_scalar", "T1_kernel_kinetic"]))
reproduces(len(triples) == 512 and triples_flip and field_kernels and krein_reversed,
           "Lemma 2: 512 connection triples flip; field-equation kernels; GBG = -B",
           (WL, ["T1_kernel_connection", "T1_kernel_field_equation"]),
           (PY, ["Q.image_krein_metric"]))
```

The cell prints the two counts, 456 and 512, as RESULT lines and makes two checks with their records. Out [10] shows both PASS lines.

**In [11], the third figure: the parity of the 256 products.**

```python
ks = np.arange(9)
heights = [comb(8, int(k)) for k in ks]
colours = ["#e34948" if k % 2 == 0 else "#184f95" for k in ks]
fig, ax = plt.subplots(figsize=(8.0, 4.6))
ax.bar(ks, heights, color=colours, width=0.7)
ax.set_xticks(ks)
ax.set_xlabel("number $k$ of gamma factors in the matrix $X$ of $\\bar\\Psi X\\Psi$")
ax.set_ylabel("number of products $\\binom{8}{k}$")
ax.set_ylim(0, 85)
notes = {0: "$S = \\bar\\Psi\\Psi$", 1: "kinetic, $J^\\mu$, $\\Psi^\\dagger B\\Psi$",
         3: "connection", 8: "$\\bar\\Psi\\Gamma\\Psi$"}
for k, text in notes.items():
    ax.text(k, heights[k] + 3, text, ha="center", fontsize=8.5, rotation=90,
            va="bottom")
ax.bar([0], [0], color="#e34948", label="sign kept, $(-1)^k = +1$")
ax.bar([0], [0], color="#184f95", label="sign reversed, $(-1)^k = -1$")
ax.legend(loc="upper right")
```

`ks` is the array $0, 1, \dots, 8$ and `heights` the numbers $\binom{8}{k}$. `colours` is red for even $k$ and blue for odd $k$ (`k % 2 == 0` tests evenness). `ax.bar` draws one bar per $k$. The axis labels are set, the vertical axis runs to 85, and `notes` writes, rotated by 90 degrees above four bars, which bilinear of the theory belongs there: $S$ at $k = 0$; the kinetic terms, the current and the charge density at $k = 1$; the connection terms at $k = 3$; $\bar\Psi\Gamma\Psi$ at $k = 8$. The two bars of height zero only create the two entries of the legend.

```python
save_figure(fig, "parity_of_products",
            "The 256 products $X$ of different gamma matrices, sorted by the number "
            "$k$ of factors (horizontal axis); the bar height is the number of "
            "such products, $\\binom{8}{k}$ (vertical axis). Red bars: the "
            "bilinear $\\bar\\Psi X\\Psi$ keeps its value under the chirality map "
            "$\\Psi \\to \\Gamma\\Psi$; blue bars: it changes sign. The sign is "
            "$(-1)^k$ for every one of the 256 products. The scalar $S$ sits in "
            "the red bar $k = 0$; the kinetic terms, the current $J^\\mu$ and the "
            "charge density $\\Psi^\\dagger B\\Psi$ in the blue bar $k = 1$; the "
            "spin-connection terms in the blue bar $k = 3$. This is why T1 "
            "reverses the kinetic term but not the mass term.")
```

The figure is saved as 18a.3. **What you see in Figure 18a.3:** a symmetric row of bars of heights 1, 8, 28, 56, 70, 56, 28, 8, 1, alternately red and blue. Why it matters: the mass term sits in a red bar (unchanged by $\Gamma$) and the kinetic term in blue bars (reversed); that difference is the whole of theorem T1.

**In [12], Lemma 3: the reflection table.**

```python
order = [8, 1, 2, 3, 4, 5, 6, 7]  # the order of the factors of Gamma
names = {a: f"x{a}" for a in range(1, 9)}
rows = []  # one row of the reflection table per direction n
lemma3_ok = True
for n in range(1, 9):
    P = Gamma @ gamma[n]
    others = I16.copy()
    for a in order:
        if a != n:
            others = others @ gamma[a]  # the product of the other seven gammas
    R = {a: (-1 if a == n else 1) for a in range(1, 9)}  # the diagonal of R_n
    orthogonal = same(P.T @ P, I16)  # so P^-1 = P^T
    covers = all(same(P.T @ gamma[a] @ P, R[a] * gamma[a]) for a in range(1, 9))
```

`order` is the order of the factors of $\Gamma$, and `names` gives the labels x1, ..., x8. For each direction $n$: `P` is $P_n = \Gamma\gamma^{(n)}$; `others` is the product of the seven other gammas in the order of $\Gamma$; `R` is the diagonal of the reflection $R_n$ (`-1 if a == n else 1`). `orthogonal` checks $P_n^TP_n = 1$, so that $P_n^{-1} = P_n^T$ (true for every signed permutation matrix); `covers` checks $P_n^{-1}\gamma^{(a)}P_n = (R_n)_{aa}\gamma^{(a)}$ for all eight $a$: $P_n$ acts on the gammas as the reflection of the direction $n$ (Lemma 3, item 3).

```python
    M = gamma[n]  # Gamma P_n = gamma^(n)
    kinetic_sign = eta[n]
    kinetic_ok = all(same(M.T @ C @ gamma[a] @ M, kinetic_sign * R[a] * C @ gamma[a])
                     for a in range(1, 9))
    connection_ok = all(
        same(M.T @ C @ (gamma[a] @ four_S[(b, c)] + four_S[(b, c)] @ gamma[a]) @ M,
             kinetic_sign * R[a] * R[b] * R[c]
             * C @ (gamma[a] @ four_S[(b, c)] + four_S[(b, c)] @ gamma[a]))
        for a in range(1, 9) for b in range(1, 9) for c in range(1, 9))
```

`M` is $\gamma^{(n)} = \Gamma P_n$, the matrix of the T2 map. `kinetic_ok` checks $M^TC\gamma^{(a)}M = \eta_{nn}(R_n)_{aa}C\gamma^{(a)}$ for all $a$: with the reflected frame the factor $(R_n)_{aa}$ is absorbed (Section 18.15), so the kinetic term gets the sign $\eta_{nn}$. `connection_ok` checks the same for the 512 connection kernels, with the three factors $(R_n)_{aa}(R_n)_{bb}(R_n)_{cc}$, two of which are absorbed by the reflected connection $R_n\omega R_n$.

```python
    row = {"direction": names[n], "eta_nn": eta[n],
           "product_sign": sign_between(P, others),
           "character": sign_between(P.T @ C @ P, C),
           "S_sign": sign_between(M.T @ C @ M, C),
           "kinetic_sign": kinetic_sign if kinetic_ok else 0}
    row["map"] = ("(m, lambda) -> (-m, lambda), L -> +L (T2)"
                  if (row["S_sign"], row["kinetic_sign"]) == (-1, 1)
                  else "(m, lambda) -> (-m, -lambda), L -> -L (T1-type)")
    rows.append(row)
    lemma3_ok = (lemma3_ok and orthogonal and covers and connection_ok and kinetic_ok
                 and same(Gamma @ P, gamma[n]) and row["character"] == -eta[n]
                 and row["product_sign"] in (1, -1))
```

One row of the table: the direction, $\eta_{nn}$, the sign of $P_n$ against the product of the other seven, the character (the sign in $P_n^TCP_n = \chi C$), the sign of $S$ under $\Psi \to \gamma^{(n)}\Psi$ (the sign in $M^TCM = \pm C$), and the kinetic sign (0 if the kinetic check failed, which would make the table differ from the record). `row["map"]` writes the resulting map of the parameters: if $S$ changes sign and the kinetic term does not, $(m, \lambda) \to (-m, \lambda)$ with $\mathcal{L} \to +\mathcal{L}$ (T2); otherwise a map of the T1 type. `lemma3_ok` collects all the conditions, including $\Gamma P_n = \gamma^{(n)}$ and the character $-\eta_{nn}$.

```python
for row in rows:
    say(f"{row['direction']}: eta {row['eta_nn']:+d}, P_n = {row['product_sign']:+d} "
        f"x (other seven), character {row['character']:+d}, S -> "
        f"{row['S_sign']:+d} S, kinetic {row['kinetic_sign']:+d}: {row['map']}")
product_signs = [r["product_sign"] for r in rows]
reproduces(lemma3_ok and product_signs == [1, -1, 1, 1, -1, 1, -1, -1],
           "Lemma 3: P_n in Pin(4,4), covers R_n, character -eta_nn, Gamma P_n = g^n",
           (WL, ["T2_Pn_in_Pin44", "T2_Pn_covers_the_reflection", "T2_character_of_Pn",
                 "T2_Gamma_times_Pn_is_gamma_n",
                 "T2_kernels_gamma_n_with_frame_reflection"]),
           (PY, ["T2.general_field.matrix_identities",
                 "T2.general_field.reflection_table"]))
```

The loop prints one line per direction (`:+d` writes a whole number with its sign); then the check requires all conditions and the recorded signs $+1, -1, +1, +1, -1, +1, -1, -1$, with five Wolfram checks and two sympy checks. Out [12] shows the eight rows: the space-like $x_1, x_2, x_3, x_8$ have character $-1$, reverse $S$ and keep the kinetic term (T2); the time-like $x_4, \dots, x_7$ have character $+1$, keep $S$ and reverse the kinetic term (T1 type).

**In [13], the table against the record.**

```python
theory = read_json(THEORY)
recorded_rows = theory["data"]["reflections"]
keys = [("eta_nn", "eta_nn"),
        ("product_sign", "P_n_equals_sign_times_product_of_other_seven"),
        ("character", "character_of_P_n"), ("S_sign", "S_sign_under_gamma_n"),
        ("kinetic_sign", "kinetic_sign_under_gamma_n_with_frame_reflection"),
        ("map", "mass_coupling_map")]
table_equal = len(recorded_rows) == 8 and all(
    recorded["direction"] == mine["direction"]
    and all(mine[k_mine] == recorded[k_rec] for k_mine, k_rec in keys)
    for mine, recorded in zip(rows, recorded_rows))
say("status of the theory record: " + theory["status"])
reproduces(table_equal and theory["status"] == "all checks of the report passed",
           "the reflection table equals the record's, row by row",
           (PY, ["compare.theory.reflection_table"]), table="reflections")
```

`theory` is the pairing theory record; `recorded_rows` its data table `reflections`, a list of eight dictionaries. `keys` pairs each field name of the notebook's rows with the field name of the record. `table_equal` requires eight recorded rows and, for each pair of rows (`zip` pairs them in order), the same direction and equal values in all six fields. The cell prints the status line of the record ("all checks of the report passed") and checks the table together with the sympy check `compare.theory.reflection_table`.

**In [14], the fourth figure: the reflection table.**

```python
columns = ["$\\eta_{nn}$", "sign of $P_n$", "character $\\chi_n$",
           "$S \\to \\pm S$", "kinetic $\\pm$"]
grid = np.array([[r["eta_nn"], r["product_sign"], r["character"], r["S_sign"],
                  r["kinetic_sign"]] for r in rows], dtype=float)
fig, ax = plt.subplots(figsize=(8.6, 5.6))
ax.imshow(grid, cmap=DIVERGING, vmin=-1.0, vmax=1.0, aspect="auto")
for i in range(8):
    for j in range(5):
        ax.text(j, i, f"{int(grid[i, j]):+d}", ha="center", va="center",
                color="white", fontsize=10)
    label = "T2: $(-m, \\lambda)$, $+\\mathcal{L}$" if rows[i]["S_sign"] == -1 \
        else "T1-type: $(-m, -\\lambda)$, $-\\mathcal{L}$"
    ax.text(5.0, i, label, ha="left", va="center", fontsize=9)
ax.set_xticks(range(5), columns, fontsize=9)
ax.set_yticks(range(8), [f"$n = x_{a}$" for a in range(1, 9)])
ax.set_xlim(-0.5, 7.4)
ax.grid(False)
ax.set_title("reflection of the direction $n$ with $\\Psi \\to \\gamma^{(n)}\\Psi$")
```

`columns` names the five columns of signs; `grid` is the $8 \times 5$ array of the signs (`dtype=float` because `imshow` draws numbers). `imshow` colours each sign (red $+1$, blue $-1$; `aspect="auto"` lets the cells be wider than high). The double loop writes each sign as white text in its cell; then the map of each row is written to the right of the grid (a backslash at the end of a line continues the statement on the next line). The axis ticks name the columns and the rows; `set_xlim(-0.5, 7.4)` leaves room for the text on the right.

```python
save_figure(fig, "reflection_table",
            "The reflection table of Lemma 3, one row for each direction $n$ (the "
            "space-like $x_1, x_2, x_3, x_8$ and the time-like $x_4$ to $x_7$). "
            "Columns: the sign $\\eta_{nn}$ of the direction; the sign of "
            "$P_n = \\Gamma\\gamma^{(n)}$ relative to the product of the other "
            "seven gammas; the character $\\chi_n$ in $P_n^\\dagger CP_n = "
            "\\chi_nC$; the sign of $S$ and of the kinetic term under "
            "$\\Psi \\to \\gamma^{(n)}\\Psi$ with the reflected frame. Red is "
            "$+1$, blue is $-1$. The character is always $-\\eta_{nn}$. A "
            "space-like reflection keeps the kinetic term and reverses $S$: the "
            "mass changes sign and the coupling does not (theorem T2). A "
            "time-like reflection does the opposite, which gives a map of the T1 "
            "type. The table equals the Revision record row by row.")
```

The figure is saved as 18a.4. **What you see in Figure 18a.4:** the columns of the character, of the sign of $S$ and of $\eta_{nn}$ form the same pattern up to sign: character $= -\eta_{nn}$ in every row; the four space-like rows read "T2", the four time-like rows "T1-type".

**In [15], the fifth figure: the chiral projectors.**

```python
P_minus = (I16 - Gamma) // 2  # whole numbers 0 and 1: the author's P_L
P_plus = (I16 + Gamma) // 2  # the author's P_R
projectors = (same(P_minus @ P_minus, P_minus) and same(P_plus @ P_plus, P_plus)
              and same(P_minus + P_plus, I16) and not (P_minus @ P_plus).any()
              and int(np.trace(P_minus)) == 8 and int(np.trace(P_plus)) == 8)
gamma_is_difference = same(Gamma, P_plus - P_minus)
gammas_swap = all(same(gamma[a] @ P_minus, P_plus @ gamma[a]) for a in range(1, 9))
halves_kept = (same(C @ P_minus, P_minus @ C)
               and all(same(M @ P_minus, P_minus @ M) for M in four_S.values()))
say(f"projectors of rank 8: {projectors}; Gamma = P+ - P-: {gamma_is_difference}; "
    f"every gamma maps the minus half to the plus half: {gammas_swap}; C and all "
    f"S^ab keep each half: {halves_kept}")
check(projectors and gamma_is_difference and gammas_swap and halves_kept,
      "the chiral projectors: P-^2 = P-, P+^2 = P+, Gamma = P+ - P-, gammas swap")
```

`P_minus` is $\frac12(1 - \Gamma)$; since $1 - \Gamma$ has entries 0 and 2, the whole-number division `// 2` gives exactly 0 and 1. `projectors` checks $P_-P_- = P_-$, $P_+P_+ = P_+$, $P_- + P_+ = 1$, $P_-P_+ = 0$ (`.any()` is false when all entries are 0, so `not (...).any()` means "is the zero matrix") and that each has trace 8 (the trace of a projector is its rank, the number of components it keeps). `gamma_is_difference` checks $\Gamma = P_+ - P_-$; `gammas_swap` checks $\gamma^{(a)}P_- = P_+\gamma^{(a)}$ for all $a$; `halves_kept` checks that $C$ and all $S^{ab}$ commute with $P_-$ (hence also with $P_+ = 1 - P_-$). One check combines them.

```python
fig, axes = plt.subplots(1, 4, figsize=(12.0, 3.6))
draw_matrix(axes[0], P_minus, "$P_- = \\frac{1}{2}(1 - \\Gamma)$")
draw_matrix(axes[1], P_plus, "$P_+ = \\frac{1}{2}(1 + \\Gamma)$")
draw_matrix(axes[2], gamma[1] @ P_minus, "$\\gamma^{(x_1)}P_-$")
image = draw_matrix(axes[3], P_plus @ gamma[1], "$P_+\\gamma^{(x_1)}$")
fig.colorbar(image, ax=list(axes), shrink=0.8, label="entry")
save_figure(fig, "chiral_projectors",
            "Heat maps of the two chiral projectors and of one gamma between them; "
            "columns horizontal, rows vertical, red $+1$, blue $-1$, grey 0, thin "
            "lines between the halves. $P_-$ (first picture, the author's P_L) is "
            "the identity on the components 1 to 8 and zero elsewhere; $P_+$ "
            "(second, the author's P_R) is the identity on 9 to 16. Their "
            "difference is $\\Gamma$. The third and fourth pictures are equal: "
            "$\\gamma^{(x_1)}P_- = P_+\\gamma^{(x_1)}$, so the gamma takes a field "
            "that lives in the first half into the second half. The T1 image "
            "$\\Gamma\\Psi = P_+\\Psi - P_-\\Psi$ reverses the relative sign of "
            "the two halves.")
```

Four heat maps: $P_-$, $P_+$, $\gamma^{(x_1)}P_-$ and $P_+\gamma^{(x_1)}$; saved as 18a.5. **What you see in Figure 18a.5:** $P_-$ is red on the first eight diagonal places, $P_+$ on the last eight; the third and the fourth panels are identical and occupy only the lower-left block: a field that lives in the first half is moved by the gamma into the second half.

**In [16], the sixth figure: the block form.**

```python
def blocks(M):
    """The four 8 x 8 blocks of a 16 x 16 matrix: upper left, upper right, lower
    left, lower right."""
    return M[:8, :8], M[:8, 8:], M[8:, :8], M[8:, 8:]
```

`blocks(M)` returns the four $8 \times 8$ blocks of a $16 \times 16$ matrix: `M[:8, :8]` is rows 1 to 8 and columns 1 to 8 (in Python, `:8` means the places 0 to 7), `M[:8, 8:]` rows 1 to 8 and columns 9 to 16, and so on.

```python
off_diagonal = all(not blocks(gamma[a])[0].any() and not blocks(gamma[a])[3].any()
                   for a in range(1, 9))  # .any() is False when all entries are 0
g8_swaps = (same(blocks(gamma[8])[1], I8) and same(blocks(gamma[8])[2], I8))
C_ul, C_ur, C_ll, C_lr = blocks(C)
C_block_diagonal = not C_ur.any() and not C_ll.any() and same(C_ul, -C_lr)
P8 = Gamma @ gamma[8]
say(f"every gamma off-diagonal: {off_diagonal}; gamma^(x8) = [[0, I8], [I8, 0]]: "
    f"{g8_swaps}; C = diag(-sigma, sigma): {C_block_diagonal}")
check(off_diagonal and g8_swaps and C_block_diagonal,
      "block form: gammas exchange the halves, gamma^(x8) swaps them, C is diagonal")
```

`off_diagonal` checks that the upper-left and lower-right blocks of every gamma are zero. `g8_swaps` checks that both off-diagonal blocks of $\gamma^{(x_8)}$ are $I_8$, so that $\gamma^{(x_8)}(\psi_-, \psi_+) = (\psi_+, \psi_-)$. `C_block_diagonal` checks that the off-diagonal blocks of $C$ vanish and that its upper-left block is minus its lower-right block: $C = \mathrm{diag}(-\sigma, \sigma)$. `P8` is $P_8 = \Gamma\gamma^{(x_8)}$, drawn below. One check combines the three facts.

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
draw_matrix(axes[0], C, "$C = \\mathrm{diag}(-\\sigma, \\sigma)$")
draw_matrix(axes[1], gamma[8], "$\\gamma^{(x_8)}$: exchanges the halves")
image = draw_matrix(axes[2], P8, "$P_8 = \\Gamma\\gamma^{(x_8)}$")
fig.colorbar(image, ax=list(axes), shrink=0.8, label="entry")
save_figure(fig, "chiral_blocks",
            "Heat maps of $C$ (left), $\\gamma^{(x_8)}$ (middle) and the reflection "
            "$P_8 = \\Gamma\\gamma^{(x_8)}$ of the hidden direction (right); axes "
            "as in the first figure (columns horizontal, rows vertical, red $+1$, "
            "blue $-1$, grey 0), thin lines between the chiral halves. $C$ lives "
            "in the two diagonal blocks, with opposite signs: "
            "$S = -\\psi_-^\\dagger\\sigma\\psi_- + \\psi_+^\\dagger\\sigma\\psi_+$. "
            "$\\gamma^{(x_8)}$ is the identity in both off-diagonal blocks: it "
            "exchanges $\\psi_-$ and $\\psi_+$, which reverses $S$ (the T2 image). "
            "$P_8$ differs from $\\gamma^{(x_8)}$ by the sign of one block, the "
            "work of $\\Gamma$.")
```

Three heat maps, $C$, $\gamma^{(x_8)}$ and $P_8$; saved as 18a.6. **What you see in Figure 18a.6:** $C$ fills the two diagonal blocks with patterns of opposite colours; $\gamma^{(x_8)}$ is two red diagonals in the off-diagonal blocks; $P_8$ is $\gamma^{(x_8)}$ with one of its two blocks turned blue. Why: $S = -\psi_-^\dagger\sigma\psi_- + \psi_+^\dagger\sigma\psi_+$, so swapping the halves (the T2 image) reverses $S$.

**In [17], Lemma 4: the 17 Krein signs.**

```python
maps = [("Gamma", Gamma)]
maps += [(f"gamma^x{n}", gamma[n]) for n in range(1, 9)]
maps += [(f"P_x{n}", Gamma @ gamma[n]) for n in range(1, 9)]
krein = {name: sign_between(M @ B_over_i @ M.T, B_over_i) for name, M in maps}
say("M B M^dagger = sigma B: " + ", ".join(f"{name} {s:+d}"
                                           for name, s in krein.items()))
```

`maps` is a list of 17 pairs (name, matrix): $\Gamma$, the eight $\gamma^{(n)}$ and the eight $P_n$. For a real $M$, $MBM^\dagger = i\,M(B/i)M^T$, so the sign $\sigma$ in $MBM^\dagger = \sigma B$ is the sign between `M @ B_over_i @ M.T` and `B_over_i`, exact whole numbers. `krein` stores the 17 signs and the cell prints them in one line.

```python
recorded_krein = {row["map"]: row["sign"]
                  for row in theory["data"]["Krein_signs_M_B_Mdagger"]}
reproduces(krein == recorded_krein and krein["Gamma"] == -1 and krein["gamma^x8"] == 1,
           "Lemma 4: the 17 Krein signs equal the record's; Gamma -1, gamma^(x8) +1",
           (WL, ["Q_Krein_metric_of_images"]),
           (PY, ["compare.theory.krein_signs", "Q.T2_image_keeps_B"]),
           table="Krein_signs_M_B_Mdagger")
```

`recorded_krein` turns the record's data table `Krein_signs_M_B_Mdagger` into a dictionary from the map's name to its sign; the check requires the two dictionaries to be equal (same names, same signs) and names the Wolfram check `Q_Krein_metric_of_images` and the sympy checks `compare.theory.krein_signs` and `Q.T2_image_keeps_B`. Out [17] lists: $\Gamma$: $-1$; $\gamma^{(x_1)}, \gamma^{(x_2)}, \gamma^{(x_3)}, \gamma^{(x_4)}, \gamma^{(x_8)}$: $+1$; $\gamma^{(x_5)}, \gamma^{(x_6)}, \gamma^{(x_7)}$: $-1$; $P_{x_1}, \dots, P_{x_4}$ and $P_{x_8}$: $-1$; $P_{x_5}, P_{x_6}, P_{x_7}$: $+1$.

**In [18], the seventh figure: the Krein signs.**

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
draw_matrix(axes[0], B_over_i, "imaginary part of $B$")
draw_matrix(axes[1], Gamma @ B_over_i @ Gamma.T,
            "imaginary part of $\\Gamma B\\Gamma^\\dagger = -B$")
image = draw_matrix(axes[2], gamma[8] @ B_over_i @ gamma[8].T,
                    "imaginary part of $\\gamma^{(x_8)}B\\gamma^{(x_8)\\dagger} = B$")
fig.colorbar(image, ax=list(axes), shrink=0.8, label="entry divided by $i$")
save_figure(fig, "krein_signs",
            "Heat maps of the imaginary parts of three 16 by 16 matrices (their "
            "real parts are zero): the Krein matrix $B = -iC\\gamma^{(x_4)}$ (left), "
            "$\\Gamma B\\Gamma^\\dagger$ (middle) and "
            "$\\gamma^{(x_8)}B\\gamma^{(x_8)\\dagger}$ (right); columns horizontal, "
            "rows vertical, red $+1$, blue $-1$, grey 0. The middle picture is the "
            "left one with all colours reversed: the chirality image "
            "$\\Gamma\\Psi$ of a quantised field has the anticommutator $-B$. The "
            "right picture equals the left one: the mirror image "
            "$\\gamma^{(x_8)}\\Psi$ of theorem T2 keeps $+B$, so it is an ordinary "
            "copy of the theory with equal energies.")
```

Three heat maps of the imaginary parts (that is, of `B_over_i` and its images): $B$, $\Gamma B\Gamma^T$ and $\gamma^{(x_8)}B\gamma^{(x_8)T}$; saved as 18a.7. **What you see in Figure 18a.7:** the middle panel is the left one with every colour reversed (the T1 image carries $-B$), and the right panel is identical to the left one (the T2 image keeps $+B$). Section 18.23 explains what this means for the quantised field.

**In [19], the last check.**

```python
figure_names = ["eight_gammas", "chirality_flips_gammas", "parity_of_products",
                "reflection_table", "chiral_projectors", "chiral_blocks",
                "krein_signs"]
paths = [output_file(f"{FIGURE_FOLDER}/18a_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths),
      "every figure file of this notebook exists")
all_checks_passed()
```

`figure_names` lists the seven figure names in order; `enumerate(figure_names, 1)` pairs each with its number, starting at 1, so `paths` holds the seven file paths. The check requires all seven files to exist, and `all_checks_passed()` prints the last line: ALL 16 CHECKS PASSED (notebook 18a).

**What Notebook 18a established.** PROVED by exact whole-number arithmetic: the matrices of the record are the author's (rebuilt from his formulas); Lemma 1; Lemma 2 for all 256 products and all 456 Lagrangian kernels; Lemma 3 with the reflection table of the record; the block form; Lemma 4 with the 17 Krein signs of the record. Nothing in the notebook concerns a particular solution or any process that creates a universe.

### 18.10 Theorem T1: the chirality pairing

**Hypotheses.**

- (H1) The gravitational field: ANY vielbein $e^a{}_\mu$ (so any metric $g_{\mu\nu} = \sum_a\eta_{aa}e^a{}_\mu e^a{}_\nu$ of signature (4,4)) and ANY spin connection $\omega_{\mu ab} = -\omega_{\mu ba}$, in particular the canonical connection of the author's metric with any history $a_4(x_4)$. The field is a fixed background: it is not varied, and both members of the pair live in the SAME field.
- (H2) The statistics: $\Psi$ has Grassmann components (dirac16complex) or commuting components (dirac16complex00). The map acts at the same point, $\Psi'(x) = \Gamma\Psi(x)$, with no change of coordinates.
- (H3) The potential: $U(S) = \frac{\lambda}{2}S^2$; more generally any function $U$ (commuting field) or any polynomial $U$ (Grassmann field), mapped to $-U$.
- (H4) $\mathcal{L}$, $E$, $T$ and $J$ as in Section 18.4, with any fixed overall sign or factor of $T$ and $J$.

**Theorem T1.** Under (H1) to (H4), for both fields:

- (T1a) $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$ for every configuration (off shell); for a general potential $\mathcal{L}_{m,U}[\Gamma\Psi] = -\mathcal{L}_{-m,-U}[\Psi]$. Separately, $S[\Gamma\Psi] = S[\Psi]$ and $K[\Gamma\Psi] = -K[\Psi]$.
- (T1b) $E_{m,\lambda}[\Gamma\Psi] = -\Gamma E_{-m,-\lambda}[\Psi]$: $\Gamma\Psi$ solves the field equations with $(m, \lambda)$ if and only if $\Psi$ solves those with $(-m, -\lambda)$. Equivalently, because $\Gamma\Gamma = 1$: $\Psi$ solves the $(m, \lambda)$ equations if and only if $\Gamma\Psi$ solves the $(-m, -\lambda)$ equations.
- (T1c) $T_{\mu\nu}^{(-m,-\lambda)}[\Gamma\Psi] = -T_{\mu\nu}^{(m,\lambda)}[\Psi]$ and $J^\mu[\Gamma\Psi] = -J^\mu[\Psi]$, at every point, off and on shell.
- (T1d) The pair ($\Psi$ with $(m, \lambda)$; $\Gamma\Psi$ with $(-m, -\lambda)$) has the total energy-momentum density $T + T' = 0$, the total current $J + J' = 0$ and the total charge $Q + Q' = 0$, as classical bilinears: ordinary numbers for dirac16complex00, elements of the Grassmann algebra for dirac16complex.

Status: PROVED. Records: `wolfram-pairing.json`, the 51 checks of the T1 group (four gravitational fields, both statistics; their names begin with `T1_`, plus `Gamma_properties`); `python-pairing.json`, the 23 checks whose names begin with `T1.` (the comparison check `compare.theory.theorem_T1` lists the 17 of them that confirm the Wolfram theorem independently); the theorem record `pairing-theory.json`, theorem T1. Notebook 18b proves it again in the author's metric (In [10] to In [12]); Notebook 18c shows it on actual solutions (In [7] to In [11]).

### 18.11 The proof of T1, line by line

**Step 1: the adjoint and the derivatives.** By Lemma 2, $\overline{\Gamma\Psi} = \bar\Psi\Gamma$. By Lemma 1,

$$
D_\mu(\Gamma\Psi) = \Gamma D_\mu\Psi,\qquad D_\mu\overline{\Gamma\Psi} = D_\mu(\bar\Psi\Gamma) = (D_\mu\bar\Psi)\Gamma .
$$

These hold for every connection, because $\Gamma$ commutes with every $S^{ab}$.

**Step 2: the scalar and the kinetic term.** Insert $\Psi' = \Gamma\Psi$ into $S$:

$$
S[\Gamma\Psi] = \overline{\Gamma\Psi}\,\Gamma\Psi = \bar\Psi\Gamma\Gamma\Psi = \bar\Psi\Psi = S[\Psi] .
$$

The first equality is the definition of $S$; the second is Step 1; the third is $\Gamma\Gamma = 1$ (Lemma 1). Now the first half of the kinetic term:

$$
\overline{\Gamma\Psi}\,\gamma^\mu D_\mu(\Gamma\Psi) = \bar\Psi\,\Gamma\gamma^\mu\Gamma\,D_\mu\Psi = -\bar\Psi\gamma^\mu D_\mu\Psi .
$$

The first equality is Step 1 twice. The second uses $\Gamma\gamma^\mu\Gamma = -\gamma^\mu$: $\gamma^\mu = \sum_ae^\mu{}_a\gamma^{(a)}$ is a combination of gammas with ordinary functions as coefficients, and each $\Gamma\gamma^{(a)}\Gamma = -\gamma^{(a)}$ (Lemma 2 with $k = 1$). The second half changes sign in the same way:

$$
\big(D_\mu\overline{\Gamma\Psi}\big)\gamma^\mu\,\Gamma\Psi = (D_\mu\bar\Psi)\,\Gamma\gamma^\mu\Gamma\,\Psi = -(D_\mu\bar\Psi)\gamma^\mu\Psi .
$$

Subtracting the two lines and multiplying by $\frac12$ gives

$$
K[\Gamma\Psi] = -K[\Psi] .
$$

In the written-out form of Section 18.4, $K$ is a sum of coefficient functions of the gravitational field times bilinears with an odd number of gammas; each such bilinear changes sign by Lemma 2, whatever the coefficients are.

**Step 3: the Lagrangian.** $U(S)$ is unchanged because $S$ is. So

$$
\mathcal{L}_{m,U}[\Gamma\Psi] = \sqrt{|g|}\,\big[-K - mS - U(S)\big] .
$$

This inserts Step 2 into the definition of $\mathcal{L}$; $\sqrt{|g|}$ is a property of the field, not of $\Psi$.

$$
\sqrt{|g|}\,\big[-K - mS - U(S)\big] = -\sqrt{|g|}\,\big[K - (-m)S - (-U)(S)\big] = -\mathcal{L}_{-m,-U}[\Psi] .
$$

We took out the factor $-1$ and recognised the Lagrangian with the mass $-m$ and the potential $-U$. For $U = \frac{\lambda}{2}S^2$, $-U = \frac{-\lambda}{2}S^2$, which is (T1a).

**Step 4: the field equations.** Using Step 1 and $\gamma^\mu\Gamma = -\Gamma\gamma^\mu$:

$$
\gamma^\mu D_\mu(\Gamma\Psi) = \gamma^\mu\Gamma D_\mu\Psi = -\Gamma\gamma^\mu D_\mu\Psi .
$$

Insert this and $S[\Gamma\Psi] = S$ into $E_{m,\lambda}$:

$$
E_{m,\lambda}[\Gamma\Psi] = -\Gamma\gamma^\mu D_\mu\Psi - (m + \lambda S)\Gamma\Psi = -\Gamma\big[\gamma^\mu D_\mu\Psi - (-m - \lambda S)\Psi\big] = -\Gamma E_{-m,-\lambda}[\Psi] .
$$

The middle step takes out $-\Gamma$ (a constant matrix commutes with the numbers $m$, $\lambda$, $S$); the last is the definition of $E$ with $(-m, -\lambda)$. Since $\Gamma$ is invertible, $E_{m,\lambda}[\Gamma\Psi] = 0$ exactly when $E_{-m,-\lambda}[\Psi] = 0$: this is (T1b). The same holds for the Euler-Lagrange expressions derived directly from $\mathcal{L}$, whatever their explicit form: (T1a) is an identity between functions of $\Psi$, and $\Psi \to \Gamma\Psi$ is a constant invertible linear substitution, so by the chain rule the Euler-Lagrange expressions of $\mathcal{L}_{m,\lambda}$ at $\Gamma\Psi$, multiplied by $\Gamma$, equal minus those of $\mathcal{L}_{-m,-\lambda}$ at $\Psi$; they vanish together. (The overall sign of a Lagrangian does not change its Euler-Lagrange equations: $-\mathcal{L}$ and $\mathcal{L}$ have the same solutions.)

**Step 5: the energy-momentum tensor and the current.** $T_{\mu\nu}$ is a sum of the kinetic bilinears $\bar\Psi\gamma_\mu D_\nu\Psi$ and $(D_\mu\bar\Psi)\gamma_\nu\Psi$ (one gamma each) and of $-g_{\mu\nu}\mathcal{L}/\sqrt{|g|}$. By Step 2 each kinetic bilinear changes sign under $\Psi \to \Gamma\Psi$. By Step 3 with $m$ replaced by $-m$ and $\lambda$ by $-\lambda$, $\mathcal{L}_{-m,-\lambda}[\Gamma\Psi] = -\mathcal{L}_{m,\lambda}[\Psi]$. Therefore

$$
T_{\mu\nu}^{(-m,-\lambda)}[\Gamma\Psi] = -\frac14\big(\cdots\big)_{\Psi} - g_{\mu\nu}\frac{-\mathcal{L}_{m,\lambda}[\Psi]}{\sqrt{|g|}} = -T_{\mu\nu}^{(m,\lambda)}[\Psi] ,
$$

where $(\cdots)_\Psi$ is the bracket of kinetic bilinears of $\Psi$. The current is a multiple of $\bar\Psi\gamma^\mu\Psi$, a bilinear with one gamma, so $J^\mu[\Gamma\Psi] = -J^\mu[\Psi]$; and the charge $Q = \int\sqrt{|g|}\,J^{x_4}\,d^7x$ changes sign with it. This is (T1c).

**Step 6: the pair.** Add (T1c) to the quantities of $\Psi$: $T^{(m,\lambda)}[\Psi] + T^{(-m,-\lambda)}[\Gamma\Psi] = 0$, $J[\Psi] + J[\Gamma\Psi] = 0$, $Q + Q' = 0$. This is (T1d).

**Step 7: both statistics.** $\Gamma = \mathrm{diag}(-I_8, I_8)$ multiplies each component by $+1$ or $-1$. No two Grassmann components are ever exchanged, so every line above holds word for word for anticommuting components, as identities between elements of the Grassmann algebra.

The proof used only Lemmas 1 and 2 and the fact that $\mathcal{L}$, $T$ and $J$ are sums of coefficient functions of the gravitational field ($\sqrt{|g|}$, $e^\mu{}_a$, $\omega_{\mu ab}$) times bilinears. It therefore holds in every gravitational field (H1). QED.

### 18.12 T1 in the block form of the author's field

In the author's field the proof can also be read off the field equation itself. In the chiral block form $\Psi = (\psi_-, \psi_+)$ every gamma is block off-diagonal; write its upper-right block $\bar\tau^a$ and its lower-left block $\tau^a$ (for the author's gammas these are his matrices $\bar\tau_A$ and $\tau_A$, and $\bar\tau^8 = \tau^8 = I_8$). Then $\gamma^{(a)}(\psi_-, \psi_+) = (\bar\tau^a\psi_+, \tau^a\psi_-)$, and the 16 equations of Section 18.4 become the two 8-component equations

$$
\sum_af_a^{-1}\bar\tau^a\partial_a\psi_+ + 3H\psi_+ = V\psi_-,\qquad \sum_af_a^{-1}\tau^a\partial_a\psi_- + 3H\psi_- = V\psi_+,\qquad V = m + \lambda S .
$$

The first equation is the upper half (rows 1 to 8) of $\gamma^\mu\partial_\mu\Psi + 3H\gamma^{(x_8)}\Psi = V\Psi$, the second the lower half; $3H\gamma^{(x_8)}$ contributes $3H\psi_+$ to the upper and $3H\psi_-$ to the lower half because both blocks of $\gamma^{(x_8)}$ are $I_8$. Now apply T1: $\Gamma(\psi_-, \psi_+) = (-\psi_-, \psi_+)$, $S = -\psi_-^\dagger\sigma\psi_- + \psi_+^\dagger\sigma\psi_+$ is unchanged (the sign of $\psi_-$ appears twice), and with the parameters $(-m, -\lambda)$ the coefficient becomes $-m - \lambda S = -V$. The two equations for the new field with $(-m, -\lambda)$ read

$$
\sum_af_a^{-1}\bar\tau^a\partial_a\psi_+ + 3H\psi_+ = (-V)(-\psi_-),\qquad -\Big(\sum_af_a^{-1}\tau^a\partial_a\psi_- + 3H\psi_-\Big) = -V\psi_+ ,
$$

which are the old equations: the first is unchanged because $(-V)(-\psi_-) = V\psi_-$, and the second is the old one multiplied by $-1$. None of the gravitational factors, $e^{\mp a_4}\sin^{-1/6}z$, $\tan z$ and $3H$, changed. This is T1 in the author's metric, PROVED again in this form by the records `wolfram-pairing.json`, checks `T1_field_equation_covariance_primordial_commuting` and `T1_field_equation_covariance_primordial_grassmann`.

### 18.13 What T1 says, and what it does not say

**Both $m$ and $\lambda$ must change sign.** The mass term keeps its sign under $\Gamma$ only if $m$ is replaced by $-m$, and the potential only if $\lambda$ is replaced by $-\lambda$. The **negative controls** of the record show that nothing weaker works: $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{m,\lambda}[\Psi] \neq 0$ and $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{-m,\lambda}[\Psi] \neq 0$ (`wolfram-pairing.json`, checks `T1_Lagrangian_negative_controls_primordial_commuting` and its Grassmann, diagonal8 and pointwise twins; `python-pairing.json`, checks `T1.metric.commuting.negative_controls` and `T1.metric.grassmann.negative_controls`; Notebook 18b, In [10] and In [11]; Notebook 18c, In [7], where the wrong partner $(-m, +\lambda)$ drifts away from $\Gamma\Psi$ by 1.641). So for $\lambda \neq 0$, T1 is not a pure $+m$ / $-m$ pairing; for $\lambda = 0$ (free fields) it pairs $+m$ with $-m$ exactly.

**The partner's energy density, pressures and equations of state.** By (T1c), $\rho' = -\rho$ and $p'_\mu = -p_\mu$ in every direction. For homogeneous solutions (Section 18.21) the record gives $\rho = mS + \frac{\lambda}{2}S^2$ and $p = \frac{\lambda}{2}S^2$ in every direction (`python-field-theory.json`, check `commuting_homogeneous_on_shell_rho_p`); the partner has $S' = S$ and $\rho' = -mS - \frac{\lambda}{2}S^2$, $p' = -\frac{\lambda}{2}S^2$. Every ratio of two components is the same for both members, in particular the equations of state $w_3 = p_3/\rho$, $w_t = p_t/\rho$ and $w_8 = p_8/\rho$.

**T1 is not a symmetry of one theory.** A **symmetry** maps the solutions of one theory to solutions of the SAME theory. T1 changes the parameters and the sign of the action; it maps the theory $(m, \lambda)$ onto the theory $(-m, -\lambda)$. Because $-\mathcal{L}$ and $\mathcal{L}$ have the same field equations, $\Gamma\Psi$ is a solution of the $(-m, -\lambda)$ theory; nothing more is asserted.

**What the map does to the components.** $\Gamma$ is $-1$ on one irreducible half of Spin(4,4) and $+1$ on the other; the partner differs from $\Psi$ only by the relative sign of its two inequivalent halves (Figure 18a.5). $\Gamma$ is itself an element of Pin(4,4), a product of eight unit vectors.

**T1 and charge conjugation (rule of this book: charge conjugation is a matrix).** Chapter 5 derived the two charge-conjugation matrices of the author's gammas. Every matrix $M$ with $M(\gamma^{(a)})^* = s\,\gamma^{(a)}M$ for all $a$ is a multiple of $1$ when $s = +1$ and a multiple of $\Gamma$ when $s = -1$ (`charge-conjugation-and-u1.json`, checks `intertwiners_same_mass` and `intertwiners_reversed_mass`). This gives two charge-conjugation matrices: $\mathcal{C}_+ = C$, with $\mathcal{C}_+^{-1}\gamma^{(a)}\mathcal{C}_+ = -(\gamma^{(a)})^T$, which keeps the mass and gives the conjugate field $\Psi^c = \mathcal{C}_+\bar\Psi^T = \Psi^*$; and $\mathcal{C}_- = \Gamma C$, with $\mathcal{C}_-^{-1}\gamma^{(a)}\mathcal{C}_- = +(\gamma^{(a)})^T$, which REVERSES the mass and gives $\Psi^c = \mathcal{C}_-\bar\Psi^T = \Gamma\Psi^*$ (checks `charge_conjugation_matrix_plus` and `charge_conjugation_matrix_minus`). Because the author's gammas, $C$ and the spin connection are REAL, plain complex conjugation of a real field does nothing: a real commuting field is its own $\mathcal{C}_+$ conjugate and carries no U(1) charge ($J^\mu = 0$ identically), so complex conjugation alone can never be what exchanges matter and antimatter (checks `representation_real` and `real_fields_charge_conjugation`). For such a real field, $\Psi^* = \Psi$, so the $\mathcal{C}_-$ conjugate $\Gamma\Psi^*$ is exactly the T1 image $\Gamma\Psi$: **on real fields, T1 is the mass-reversing charge conjugation by the matrix $\Gamma$**, and it maps solutions with $(m, \lambda)$ to solutions with $(-m, -\lambda)$ (same check). For complex fields the two maps differ: T1 is linear ($\Psi \to \Gamma\Psi$) and reverses $J$, while the $\mathcal{C}_-$ conjugation is antilinear ($\Psi \to \Gamma\Psi^*$); for commuting components it keeps $J$ (check `bilinears_under_charge_conjugation`). For the quantised field the conjugation that preserves the canonical anticommutator is $\Psi \to \Gamma\Psi^{\dagger T}$, and it too reverses the mass (check `quantum_charge_conjugation_unitary_type`). Chapter 21 uses these facts for matter and antimatter.

### 18.14 Theorem T2: the mirror pairing

T1 reverses the energy and needs $\lambda \to -\lambda$. Is there a map that pairs $(m, \lambda)$ with $(-m, \lambda)$, the same coupling? Lemma 3 points to it: the reflections of the space-like directions have the character $-1$, so they reverse $S$ and keep the kinetic term.

**Hypotheses.**

- (H5) $n$ is a space-like frame direction ($x_1$, $x_2$, $x_3$ or $x_8$), and $P_n = \Gamma\gamma^{(n)}$ is the Pin(4,4) lift of the reflection $R_n$, of character $-1$ (Lemma 3).
- (H6) General-field version: the frame is reflected, $e' = R_ne$, that is $e'^a{}_\mu = (R_n)_{aa}e^a{}_\mu$ (the same metric, since $R_n\eta R_n = \eta$, and the same $\sqrt{|g|}$), with its own canonical connection; and $\Psi'(x) = \Gamma P_n\Psi(x) = \gamma^{(n)}\Psi(x)$ at the same point.
- (H7) Author's-field version: the map $\phi$: $x_8 \to \pi/(6H) - x_8$, that is $z \to \pi - z$, takes the patch $0 < z < \pi/2$ onto the mirror patch $\pi/2 < z < \pi$; each patch carries its own positive vielbein ($f_8 = |\cot z|$, which is $-\cot z$ on the mirror patch); and $\Psi'(\phi(x)) = \gamma^{(x_8)}\Psi(x)$. The brane $z = \pi/2$ is a degenerate surface of the metric ($g_{88} = \cot^2 z = 0$ and $\sqrt{|g|} = \cos z = 0$ there); extending the field to the mirror patch is the Z2 construction, ASSUMED.
- (H8) Both statistics; $U(S) = \frac{\lambda}{2}S^2$, or any even function of $S$.

**Theorem T2.** Under (H5) to (H8), for both fields:

- (T2a) $\mathcal{L}_{m,\lambda}[\gamma^{(n)}\Psi;\,R_ne] = +\mathcal{L}_{-m,\lambda}[\Psi;\,e]$ in every gravitational field; in the author's field $\mathcal{L}_{m,\lambda}[\Psi'](\phi(x)) = \mathcal{L}_{-m,\lambda}[\Psi](x)$.
- (T2b) $S' = -S$, and $E_{m,\lambda}[\gamma^{(n)}\Psi;\,R_ne] = -\gamma^{(n)}E_{-m,\lambda}[\Psi;\,e]$: $\Psi$ solves the $(-m, \lambda)$ equations if and only if its image solves the $(m, \lambda)$ equations (in the author's field: on the patch and on the mirror patch respectively).
- (T2c) In the general-field version $T'_{\mu\nu} = T^{(-m,\lambda)}_{\mu\nu}[\Psi]$ and $J'^\mu = J^\mu[\Psi]$. In the author's field the coordinate components pick up the reflection of $x_8$: $T_{\mu\nu}[\Psi'](\phi(x)) = \Lambda_\mu\Lambda_\nu\,T^{(-m,\lambda)}_{\mu\nu}[\Psi](x)$ and $J'^\mu = \Lambda_\mu J^\mu$, with $\Lambda = \mathrm{diag}(1, 1, 1, 1, 1, 1, 1, -1)$. The energy density, the charge density and every component without an index $x_8$ are EQUAL, not opposite. T2 pairs $+m$ with $-m$ at equal energy-momentum.
- (T2d) For a time-like $n$ (character $+1$) the same construction gives $\mathcal{L} \to -\mathcal{L}_{-m,-\lambda}$, a map of the T1 type. The character $-1$ is what makes T2 a pairing $(m, \lambda) \to (-m, \lambda)$ with $\mathcal{L} \to +\mathcal{L}$.

Status: PROVED, the author's-field version under the ASSUMED Z2 construction. Records: `wolfram-pairing.json`, the 28 checks of the T2 group (the frame reflections of all eight directions in a general field at a point, both statistics, and the mirror in the author's field); `python-pairing.json`, the 16 checks of the T2 group (names beginning with `T2.` and the two geometry checks of the mirror); theorem T2 of `pairing-theory.json`. Notebook 18b proves it in the author's metric (In [15] to In [19]); Notebook 18c shows it on actual solutions (In [12] and In [13]).

### 18.15 The proof of T2 in a general field

Fix a space-like $n$ in the end, but keep $\eta_{nn}$ general as long as possible, so that (T2d) comes out too.

**Step 1: the geometry.** The reflected frame gives the same metric:

$$
g'_{\mu\nu} = \sum_a\eta_{aa}\,(R_n)_{aa}e^a{}_\mu\,(R_n)_{aa}e^a{}_\nu = \sum_a\eta_{aa}e^a{}_\mu e^a{}_\nu = g_{\mu\nu} .
$$

$(R_n)_{aa}^2 = 1$. Its canonical connection is $R_n\omega R_n$: in the formula $\omega_\mu{}^a{}_b = e^a{}_\nu(\partial_\mu e^\nu{}_b + \Gamma^\nu{}_{\mu\lambda}e^\lambda{}_b)$ the new vielbein carries a factor $(R_n)_{aa}$, its inverse a factor $(R_n)_{bb}$, the constant factors come out of $\partial_\mu$, and the Christoffel symbols of the unchanged metric are unchanged:

$$
\omega'_{\mu ab} = (R_n)_{aa}(R_n)_{bb}\,\omega_{\mu ab} .
$$

By Lemma 3, item 2, $(R_n)_{aa}(R_n)_{bb}S^{ab} = \gamma^{(n)}S^{ab}(\gamma^{(n)})^{-1}$, so

$$
\Omega'_\mu = \frac12\sum_{a,b}(R_n)_{aa}(R_n)_{bb}\,\omega_{\mu ab}S^{ab} = \gamma^{(n)}\,\Omega_\mu\,(\gamma^{(n)})^{-1},
$$

and therefore $D'_\mu(\gamma^{(n)}\Psi) = \gamma^{(n)}\partial_\mu\Psi + \gamma^{(n)}\Omega_\mu(\gamma^{(n)})^{-1}\gamma^{(n)}\Psi = \gamma^{(n)}D_\mu\Psi$.

**Step 2: the adjoint.** $\gamma^{(n)}$ is real with $(\gamma^{(n)})^T = \eta_{nn}\gamma^{(n)}$, and from $C\gamma^{(n)}C^{-1} = -(\gamma^{(n)})^T = -\eta_{nn}\gamma^{(n)}$ we get $C\gamma^{(n)} = -\eta_{nn}\gamma^{(n)}C$ (multiply on the right by $C$) and then $\gamma^{(n)}C = -\eta_{nn}C\gamma^{(n)}$ (multiply both sides by $-\eta_{nn}$ and use $\eta_{nn}^2 = 1$). Then

$$
\bar\Psi' = \Psi^\dagger(\gamma^{(n)})^TC = \eta_{nn}\Psi^\dagger\gamma^{(n)}C = \eta_{nn}\Psi^\dagger(-\eta_{nn}C\gamma^{(n)}) = -\bar\Psi\gamma^{(n)} .
$$

The definition of the adjoint with $(M\Psi)^\dagger = \Psi^\dagger M^T$ for a real $M$; the transpose rule; the relation just derived; $\eta_{nn}^2 = 1$. In the same way, with Step 1, $D'_\mu\bar\Psi' = -(D_\mu\bar\Psi)\gamma^{(n)}$.

**Step 3: the gammas of the reflected frame.** $\gamma'^\mu = \sum_ae'^\mu{}_a\gamma^{(a)} = \sum_ae^\mu{}_a(R_n)_{aa}\gamma^{(a)}$. For $a \neq n$, $(R_n)_{aa}\gamma^{(a)}\gamma^{(n)} = \gamma^{(a)}\gamma^{(n)} = -\gamma^{(n)}\gamma^{(a)}$; for $a = n$, $(R_n)_{nn}\gamma^{(n)}\gamma^{(n)} = -\gamma^{(n)}\gamma^{(n)}$. So in both cases $(R_n)_{aa}\gamma^{(a)}\gamma^{(n)} = -\gamma^{(n)}\gamma^{(a)}$, and summing with the coefficients $e^\mu{}_a$:

$$
\gamma'^\mu\gamma^{(n)} = -\gamma^{(n)}\gamma^\mu .
$$

**Step 4: the bilinears.** Insert Steps 1 to 3:

$$
\bar\Psi'\gamma'^\mu D'_\mu\Psi' = -\bar\Psi\gamma^{(n)}\,\gamma'^\mu\gamma^{(n)}D_\mu\Psi = -\bar\Psi\gamma^{(n)}(-\gamma^{(n)}\gamma^\mu)D_\mu\Psi = \eta_{nn}\,\bar\Psi\gamma^\mu D_\mu\Psi .
$$

The last step is $\gamma^{(n)}\gamma^{(n)} = \eta_{nn}$. In the same way $(D'_\mu\bar\Psi')\gamma'^\mu\Psi' = \eta_{nn}(D_\mu\bar\Psi)\gamma^\mu\Psi$, so $K' = \eta_{nn}K$. And

$$
S' = \bar\Psi'\Psi' = -\bar\Psi\gamma^{(n)}\gamma^{(n)}\Psi = -\eta_{nn}S .
$$

**Step 5: the Lagrangian.** For a space-like $n$, $\eta_{nn} = +1$: $K' = K$ and $S' = -S$, so

$$
\mathcal{L}_{m,\lambda}[\Psi'; e'] = \sqrt{|g|}\Big[K - m(-S) - \frac{\lambda}{2}(-S)^2\Big] = \sqrt{|g|}\Big[K - (-m)S - \frac{\lambda}{2}S^2\Big] = \mathcal{L}_{-m,\lambda}[\Psi; e] ,
$$

which is (T2a); the potential is even in $S$, so it does not change. For a time-like $n$, $\eta_{nn} = -1$: $K' = -K$ and $S' = S$, so $\mathcal{L}_{m,\lambda}[\Psi'; e'] = \sqrt{|g|}[-K - mS - \frac{\lambda}{2}S^2] = -\mathcal{L}_{-m,-\lambda}[\Psi; e]$, which is (T2d).

**Step 6: the field equations** (space-like $n$). With Step 1, Step 3 and $S' = -S$:

$$
E_{m,\lambda}[\Psi'; e'] = \gamma'^\mu\gamma^{(n)}D_\mu\Psi - (m - \lambda S)\gamma^{(n)}\Psi = -\gamma^{(n)}\big[\gamma^\mu D_\mu\Psi - (-m + \lambda S)\Psi\big] = -\gamma^{(n)}E_{-m,\lambda}[\Psi; e] ,
$$

which is (T2b), since $\gamma^{(n)}$ is invertible.

**Step 7: the energy-momentum tensor and the current.** The kinetic bilinears with free indices, $\bar\Psi\gamma_\mu D_\nu\Psi$, transform like the contracted one in Step 4 (with the factor $\eta_{nn} = +1$), and $\mathcal{L}/\sqrt{|g|}$ by Step 5, so $T'_{\mu\nu} = T^{(-m,\lambda)}_{\mu\nu}[\Psi]$. Likewise $\bar\Psi'\gamma'^\mu\Psi' = -\bar\Psi\gamma^{(n)}\gamma'^\mu\gamma^{(n)}\Psi = \eta_{nn}\bar\Psi\gamma^\mu\Psi$ gives $J' = J$. This is (T2c) in the general-field version.

**Step 8: both statistics.** $\gamma^{(n)}$ is a constant signed permutation matrix: it reorders the components and changes some signs, but in every bilinear each $\Psi^*$ still stands to the left of each $\Psi$. No two Grassmann components are exchanged, so Steps 1 to 7 hold for both statistics. QED.

### 18.16 T2 in the author's field: the mirror across the brane

**The mirror is an isometry.** Under $z \to \pi - z$: $\sin(\pi - z) = \sin z$, so the factors $\sin^{1/3}z$ of the 3-space and extra-time components are unchanged; $\cot(\pi - z) = -\cot z$, so $g_{88} = \cot^2 z$ is unchanged; the factors $e^{\pm2a_4}$ do not depend on $z$. So every $g_{\mu\mu}$ takes the same value at the mirror point (`python-pairing.json`, check `geometry.mirror_isometry`; `wolfram-pairing.json`, check `T2_mirror_is_isometry`; Notebook 18b, In [15], and its Figure 18b.4).

**The pulled-back frame is the reflected frame.** On the mirror patch the positive hidden vielbein factor is $f_8 = -\cot z$ (positive there, because $\cot z < 0$ for $\pi/2 < z < \pi$). Pull the hidden leg $e^8 = f_8\,dx_8$ back by $\phi$: $x_8 \to \pi/(6H) - x_8$ replaces $dx_8$ by $-dx_8$ and $z$ by $\pi - z$:

$$
-\cot(\pi - z)\,d\big(\tfrac{\pi}{6H} - x_8\big) = \cot z\,(-dx_8) = -e^8 .
$$

The other seven legs are unchanged. So the pulled-back vielbein is $R_8e$, the frame reflected in the direction $x_8$, and $\sqrt{|g|}\,d^8x$ is unchanged ($|\cos z|$ is unchanged and the Jacobian of $\phi$ has modulus 1). Pulling the Lagrangian of the mirror patch back by $\phi$ therefore gives exactly the frame-reflected Lagrangian of Section 18.15 with $n = x_8$, which proves (T2a) and (T2b) in the author's field. The coordinate components of $T$ and $J$ pick up the Jacobian $R_8$ of $\phi$, one factor $-1$ for each index $x_8$, which gives (T2c) with $\Lambda = R_8$. QED.

**The spin-connection term on the mirror patch.** With $f_8 = -\cot z$ the twelve components of Section 18.3 keep their form, except that the six components with an index $x_8$ change sign (they contain $1/f_8$). In the sum of Section 18.3 the $a_4'$ terms still cancel and the hidden terms add with the opposite sign: $\gamma^\mu\Omega_\mu = -3H\gamma^{(x_8)}$ on the mirror patch (Notebook 18c, In [3]). In block form, $\gamma^{(x_8)}(\psi_-, \psi_+) = (\psi_+, \psi_-)$: the mirror image exchanges the two inequivalent Spin(4,4) halves, and $S = -\psi_-^\dagger\sigma\psi_- + \psi_+^\dagger\sigma\psi_+$ changes sign.

**Which matrix makes the mirror a pairing?** The sympy record searched four candidates $P$ for the map $\Psi'(\phi(x)) = P\Psi(x)$ and all eight sign choices of a relation $\mathcal{L}^{\rm mirror}_{m,\lambda}[\Psi'] = \sigma\mathcal{L}^{\rm patch}_{\pm m,\pm\lambda}[\Psi]$. The result (`python-pairing.json`, checks `T2.metric.commuting.reflection_table` and `T2.metric.grassmann.reflection_table`; Notebook 18b, In [17], Figure 18b.5):

| matrix $P$ | relation found |
| --- | --- |
| $1$ (the plain mirror) | none |
| $\Gamma$ | none |
| $\gamma^{(x_8)} = \Gamma P_8$ | $+\mathcal{L}_{-m,\lambda}$: theorem T2 |
| $\Gamma\gamma^{(x_8)} = P_8$ (the reflection alone) | $-\mathcal{L}_{m,-\lambda}$ |

The plain mirror fails because the pull-back reverses the hidden leg of the frame: the part of the kinetic term along $x_8$ (and the connection terms with one index $x_8$) changes sign while the rest does not, so the pulled-back Lagrangian is neither $+$ nor $-$ a Lagrangian of the patch. The matrix $\gamma^{(x_8)}$ repairs exactly this sign (Steps 3 and 4 of Section 18.15 with $n = x_8$).

**The eight reflections.** For completeness, the frame reflections of all eight directions (the data table `reflections` of `pairing-theory.json`, recomputed exactly by Notebook 18a, In [12] and In [13], Figure 18a.4):

| direction | $\eta_{nn}$ | character of $P_n$ | $S$ under $\gamma^{(n)}$ | kinetic term | map |
| --- | --- | --- | --- | --- | --- |
| $x_1$ | $+1$ | $-1$ | $-S$ | $+K$ | $(-m, \lambda)$, $+\mathcal{L}$ (T2) |
| $x_2$ | $+1$ | $-1$ | $-S$ | $+K$ | $(-m, \lambda)$, $+\mathcal{L}$ (T2) |
| $x_3$ | $+1$ | $-1$ | $-S$ | $+K$ | $(-m, \lambda)$, $+\mathcal{L}$ (T2) |
| $x_4$ | $-1$ | $+1$ | $+S$ | $-K$ | $(-m, -\lambda)$, $-\mathcal{L}$ (T1 type) |
| $x_5$ | $-1$ | $+1$ | $+S$ | $-K$ | $(-m, -\lambda)$, $-\mathcal{L}$ (T1 type) |
| $x_6$ | $-1$ | $+1$ | $+S$ | $-K$ | $(-m, -\lambda)$, $-\mathcal{L}$ (T1 type) |
| $x_7$ | $-1$ | $+1$ | $+S$ | $-K$ | $(-m, -\lambda)$, $-\mathcal{L}$ (T1 type) |
| $x_8$ | $+1$ | $-1$ | $-S$ | $+K$ | $(-m, \lambda)$, $+\mathcal{L}$ (T2) |

In the author's field only the reflection of $x_8$ is realised by an isometry that maps the patch onto another patch, the mirror across the Z2 brane; the reflections of $x_1, x_2, x_3$ are statements about frames.

**What T2 says and does not say.** T2 pairs a solution with mass $-m$ on the patch with a solution with mass $+m$ on the mirror patch, at the SAME coupling and with EQUAL energy density and charge density: nothing cancels in a T2 pair. The gluing of the two patches at the degenerate brane is an assumption; no junction condition, brane tension or matching of the field across the brane is derived (`pairing-theory.json`, the list `not_established`).

### 18.17 Example: Notebook 18b proves T1 and T2 in the author's metric

Notebook 18b repeats the proofs of Sections 18.11 and 18.15 as exact computer algebra, without taking any step on trust. It builds the author's metric with an UNKNOWN history $a_4(x_4)$ (so every result holds for every deflating history), computes its Christoffel symbols and canonical spin connection with sympy, checks the vielbein postulate and the twelve components of Section 18.3, and recomputes $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ direction by direction. Then it writes the Lagrangian, the field operator, all 36 components of $T_{\mu\nu}$ and the 8 components of $J^\mu$ as polynomials in the 288 values of the first jet, in an algebra that can treat the jet values as commuting numbers (dirac16complex00) or as Grassmann numbers (dirac16complex), and proves T1 and T2 as identities in which every coefficient is zero. It reproduces 35 checks of `python-pairing.json` and the corresponding Wolfram checks, including the numbers of monomials of the Lagrangian recorded by the Wolfram verifier, 408 for commuting and 392 for Grassmann components, and draws five figures. Its last line is ALL 20 CHECKS PASSED (notebook 18b); it runs in about 2 minutes.

<!-- NOTEBOOK 18b -->

### 18.20 Line-by-line walk-through of Notebook 18b

The notebook has 20 code cells. **In [1]** is the set-up cell, word for word the set-up cell of Notebook 18a explained line by line in Section 18.9, except that its comment lines hold the run instructions of Section 18.18 and its line `NOTEBOOK_ID = "18b"` names this notebook, so its figures are saved as `18b_<k>_<name>.png` and their captions in `18b.captions.json`. It prints one line, Set-up of notebook 18b complete: repository folder found, helpers defined.

The idea of the notebook in one paragraph. At one point $x$, every quantity of the theory (the Lagrangian, the 16 components of the field operator, the 36 components of $T_{\mu\nu}$, the 8 of $J^\mu$) is a polynomial in the 288 numbers of the **first jet**: the 16 values $\Psi_A$, the 16 values $\Psi_A^*$ and the $2 \times 8 \times 16 = 256$ first derivatives $\partial_\mu\Psi_A$, $\partial_\mu\Psi_A^*$. The coefficients of the polynomial are functions of the point: of $x_4$ through $a_4(x_4)$ and $a_4'$, of $z$, and of $H$, $m$, $\lambda$. If a polynomial has only zero coefficients, it is zero for EVERY field at EVERY point and for EVERY history $a_4$. So proving "$\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{-m,-\lambda}[\Psi]$ has only zero coefficients" proves T1 in the author's metric. To handle dirac16complex, the 288 jet values are made ANTICOMMUTING symbols; the same computation then proves the theorem for Grassmann components.

**In [2], the exact gammas.**

```python
import itertools  # all combinations of signs
import random  # Python's random numbers with a fixed seed (the random field)

import numpy as np  # numbers for the figures
import sympy as sp  # exact symbolic algebra

GAMMAS = "Revision/algebra/gammas.json"
PY = "Revision/pairing/reports/python-pairing.json"  # the sympy verifier's report
WL = "Revision/pairing/reports/wolfram-pairing.json"  # the Wolfram verifier's report
PARAMETERS = "Revision/kohn_sham/results/parameters.json"
```

`itertools` gives `product`, which lists all combinations (used for index triples and sign choices); `random` is Python's own random-number module (used with a fixed seed in In [12]); numpy is used only for the figures; **sympy** (`sp`) is the package for exact symbolic algebra: it computes with symbols such as $z$ and $H$, with fractions and with functions, without rounding. The four constants name the records the notebook reads: the gammas, the two pairing reports, and the Kohn-Sham parameter file that holds the canonical history.

```python
def read_json(relative):
    """Read a JSON file of the repository (a Revision record)."""
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))


RECORDS = {PY: read_json(PY), WL: read_json(WL)}


def recorded(report_file, name):
    """The recorded entry (verdict and detail) of the check name of a report."""
    for entry in RECORDS[report_file]["checks"]:
        if entry["name"] == name:
            return entry
    return {"verdict": "MISSING", "detail": ""}


def reproduces(condition, name, *sources):
    """check(condition, name), which also requires every named check of every
    source (report_file, [check names]) to have the recorded verdict PASS."""
    ok = all(recorded(f, n)["verdict"].upper() == "PASS"
             for f, names in sources for n in names)
    text = "; ".join(f"{f}, check {', '.join(names)}" for f, names in sources)
    check(condition and ok, name, record=text)
```

`read_json` is the reader of Notebook 18a. `RECORDS` reads the two reports once and keeps them. `recorded(report_file, name)` returns the whole entry of a check (its verdict and its detail text), or a placeholder with the verdict MISSING. `reproduces` works as in Notebook 18a: the check passes only when the notebook's own result holds and every named record check has the verdict PASS.

```python
fixture = read_json(GAMMAS)
G = {a: sp.Matrix(fixture["gamma"][a - 1]) for a in range(1, 9)}  # gamma^(x_a)
ETA = {a: int(fixture["eta"][a - 1]) for a in range(1, 9)}
I16 = sp.eye(16)
C = G[8] * G[1] * G[2] * G[3]  # the four space-like gammas
GAM = G[8] * G[1] * G[2] * G[3] * G[4] * G[5] * G[6] * G[7]  # the chirality Gamma
SAB = {(a, b): (G[a] * G[b] - G[b] * G[a]) / 4  # the generators S^ab
       for a in range(1, 9) for b in range(1, 9)}
check(all(G[a] * G[b] + G[b] * G[a] == (2 * ETA[a] if a == b else 0) * I16
          for a in range(1, 9) for b in range(1, 9))
      and GAM == sp.diag(*([-1] * 8 + [1] * 8)),
      "eight real 16 x 16 gammas with the Clifford relations; Gamma = diag(-I8, I8)")
```

`sp.Matrix(...)` makes an exact sympy matrix from the lists of whole numbers of the record, one for each direction; `G[a]` is $\gamma^{(x_a)}$. `ETA` holds $\eta_{aa}$ and `I16` is the exact identity. `C` and `GAM` ($\Gamma$) are the products of Section 18.5, written with `*`, which is the matrix product for sympy matrices. `SAB` holds the 64 generators $S^{ab} = \frac14[\gamma^{(a)}, \gamma^{(b)}]$ exactly (entries $0$ and $\pm\frac12$). The check confirms the 64 Clifford relations and $\Gamma = \mathrm{diag}(-I_8, I_8)$ (`sp.diag(*list)` makes a diagonal matrix from the entries of the list). Out [2] shows one PASS line.

**In [3], the metric and its canonical connection.**

```python
x4, z, H = sp.symbols("x4 z H", real=True)
m, lam = sp.symbols("m lambda", real=True)
a4 = sp.Function("a4")(x4)  # the history: any function of the time x4
```

`sp.symbols` creates the symbols $x_4$, $z$, $H$, $m$ and $\lambda$, declared real. `sp.Function("a4")(x4)` is an UNKNOWN function $a_4(x_4)$: sympy differentiates it formally, writing its derivative as `Derivative(a4(x4), x4)`. Leaving $a_4$ unknown is what makes every result of this notebook hold for every history, in particular for the deflating ones.

```python
def d(expr, mu):
    """The derivative of a coefficient along the coordinate x_mu."""
    if mu == 4:
        return sp.diff(expr, x4)
    if mu == 8:
        return 6 * H * sp.diff(expr, z)  # z = 6 H x8
    return sp.Integer(0)  # nothing depends on x1, x2, x3, x5, x6, x7
```

`d(expr, mu)` is the derivative of a coefficient function along the coordinate $x_\mu$: along $x_4$ it is `sp.diff(expr, x4)`; along $x_8$ it is $6H\,d/dz$, the chain rule for $z = 6Hx_8$; along the other six coordinates it is zero, because no coefficient depends on them.

```python
class Geometry:
    """The author's metric with the diagonal vielbein; s8 = +1 on the patch,
    s8 = -1 on the mirror patch (then f8 = -cot z > 0)."""

    def __init__(self, s8):
        up, down = sp.exp(a4), sp.exp(-a4)  # inflating and deflating factors
        s6 = sp.sin(z) ** sp.Rational(1, 6)
        f = {1: up * s6, 2: up * s6, 3: up * s6, 4: sp.Integer(1),
             5: down * s6, 6: down * s6, 7: down * s6, 8: s8 * sp.cot(z)}
        self.f = f
        self.g = {mu: ETA[mu] * f[mu] ** 2 for mu in f}  # g_mu mu
        self.sqrtg = sp.simplify(sp.Mul(*f.values()))  # sqrt|g|
        g = self.g
```

A **class** is a recipe for an object that holds several named values; `Geometry(s8)` builds one, and `__init__` is the code that runs when it is built (`self` is the object being built). The factors $f_\mu$ of Section 18.3 are stored in the dictionary `f`, with $f_8 = s_8\cot z$: $s_8 = +1$ on the patch and $-1$ on the mirror patch, where $\cot z < 0$, so that $f_8$ is positive on both. `self.g` holds $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$, and `self.sqrtg` the product of the eight factors (`sp.Mul(*values)` multiplies them), simplified exactly.

```python
        self.chr = {}  # Christoffel symbols Gamma^nu_(mu lambda)
        for nu, mu, la in itertools.product(range(1, 9), repeat=3):
            v = 0
            if nu == la:
                v += d(g[nu], mu)
            if nu == mu:
                v += d(g[nu], la)
            if mu == la:
                v -= d(g[mu], nu)
            self.chr[nu, mu, la] = sp.simplify(v / (2 * g[nu]))
```

The Christoffel symbols of a diagonal metric, $\Gamma^\nu{}_{\mu\lambda} = \frac{1}{2g_{\nu\nu}}\big(\delta_{\nu\lambda}\partial_\mu g_{\nu\nu} + \delta_{\nu\mu}\partial_\lambda g_{\nu\nu} - \delta_{\mu\lambda}\partial_\nu g_{\mu\mu}\big)$, for all $8^3 = 512$ index triples (`itertools.product(range(1, 9), repeat=3)` lists them). Each `if` adds one of the three terms when its Kronecker delta is 1. This is the formula of Section 18.3 written for all indices at once.

```python
        self.om = {}  # omega_mu ab
        for mu, a, b in itertools.product(range(1, 9), repeat=3):
            v = self.chr[a, mu, b] / f[b]  # e^a_nu Gamma^nu_mu lam e^lam_b ...
            if a == b:
                v += d(1 / f[b], mu)  # ... + e^a_nu d_mu e^nu_b
            self.om[mu, a, b] = sp.simplify(ETA[a] * f[a] * v)
```

The canonical connection $\omega_\mu{}^a{}_b = e^a{}_\nu(\partial_\mu e^\nu{}_b + \Gamma^\nu{}_{\mu\lambda}e^\lambda{}_b)$ for the diagonal vielbein: $e^\lambda{}_b = \delta^\lambda_b/f_b$ turns the second term into $\Gamma^a{}_{\mu b}/f_b$; the first term exists only for $a = b$, where it is $\partial_\mu(1/f_b)$; the factor $e^a{}_a = f_a$ multiplies both; and $\eta_{aa}$ lowers the index $a$. So `self.om[mu, a, b]` is $\omega_{\mu ab}$.

```python
        self.Om = {}  # Omega_mu = (1/2) omega_mu ab S^ab
        for mu in range(1, 9):
            M = sp.zeros(16)
            for a, b in itertools.product(range(1, 9), repeat=2):
                if self.om[mu, a, b] != 0:
                    M += self.om[mu, a, b] * SAB[a, b] / 2
            self.Om[mu] = M.applyfunc(sp.simplify)
        self.gup = {mu: G[mu] / f[mu] for mu in f}  # gamma^mu
        self.glow = {mu: ETA[mu] * f[mu] * G[mu] for mu in f}  # gamma_mu
```

$\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$, summed over the nonzero components only and simplified entry by entry (`applyfunc` applies a function to every entry of a matrix). `gup` holds the curved gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and `glow` the lowered ones $\gamma_\mu = \eta_{\mu\mu}f_\mu\gamma^{(\mu)}$.

```python
patch = Geometry(1)  # the author's patch 0 < z < pi/2
author = {1: sp.exp(2 * a4) * sp.sin(z) ** sp.Rational(1, 3), 4: -1,
          5: -sp.exp(-2 * a4) * sp.sin(z) ** sp.Rational(1, 3), 8: sp.cot(z) ** 2}
author.update({2: author[1], 3: author[1], 6: author[5], 7: author[5]})
metric_ok = all(sp.simplify(patch.g[mu] - author[mu]) == 0 for mu in range(1, 9))
say(f"sqrt|g| on the patch = {patch.sqrtg}")
reproduces(metric_ok and sp.simplify(patch.sqrtg - sp.cos(z)) == 0,
           "the vielbein gives the author's metric and sqrt|g| = cos z",
           (WL, ["primordial_vielbein"]))
```

`patch` is the geometry of the author's patch. `author` writes the eight components of the author's metric exactly as the author gave them ($e^{2a_4}\sin^{1/3}z$ for 3-space, $-1$ for the time, $-e^{-2a_4}\sin^{1/3}z$ for the extra times, $\cot^2 z$ for the hidden direction); `update` fills in the repeated ones. `metric_ok` checks that the vielbein reproduces all eight. Out [3] prints $\sqrt{|g|} = \cos z$ and the PASS line with the Wolfram check `primordial_vielbein`.

**In [4], the connection checked three ways.**

```python
COORDS = {a: f"x{a}" for a in range(1, 9)}
antisymmetric = all(sp.simplify(patch.om[mu, a, b] + patch.om[mu, b, a]) == 0
                    for mu, a, b in itertools.product(range(1, 9), repeat=3))
postulate = True
for mu, nu in itertools.product(range(1, 9), repeat=2):
    M = patch.gup[nu].applyfunc(lambda e: d(e, mu))  # d_mu gamma^nu
    for la in range(1, 9):
        if patch.chr[nu, mu, la] != 0:
            M = M + patch.chr[nu, mu, la] * patch.gup[la]
    M = M + patch.Om[mu] * patch.gup[nu] - patch.gup[nu] * patch.Om[mu]
    postulate = postulate and all(sp.simplify(e) == 0 for e in M)
```

`antisymmetric` checks $\omega_{\mu ab} + \omega_{\mu ba} = 0$ for all 512 triples. The loop then checks the vielbein postulate for all 64 pairs $(\mu, \nu)$: `M` starts as $\partial_\mu\gamma^\nu$ (the derivative of each entry; `lambda e: d(e, mu)` is a one-line function), adds $\sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda$ and the commutator $\Omega_\mu\gamma^\nu - \gamma^\nu\Omega_\mu$; every entry of the result must simplify to zero.

```python
a4p = sp.Symbol("a4p")  # a short name for the derivative a4'


def short(expr):
    """Write a4' as a4p and a4(x4) as a4, as in the Revision report."""
    expr = sp.simplify(expr).subs(sp.Derivative(a4, x4), a4p)
    return expr.subs(a4, sp.Symbol("a4"))


nonzero = [(mu, a, b) for mu in range(1, 9) for a in range(1, 9)
           for b in range(a + 1, 9) if sp.simplify(patch.om[mu, a, b]) != 0]
listing = "; ".join(f"omega_{COORDS[mu]} {COORDS[a]}{COORDS[b]} = "
                    f"{short(patch.om[mu, a, b])}" for mu, a, b in nonzero)
for mu, a, b in nonzero:
    say(f"omega_{COORDS[mu]} {COORDS[a]}{COORDS[b]} = {short(patch.om[mu, a, b])}")
same_list = recorded(PY, "geometry.spin_connection_components")["detail"] == (
    "nonzero components (a < b): " + listing)
```

`a4p` is a plain symbol used to write $a_4'$ in the format of the record, and `short` replaces the derivative of $a_4$ by `a4p` and the function $a_4(x_4)$ by the plain symbol `a4`. `nonzero` lists the triples $(\mu, a, b)$ with $a < b$ whose component is not zero; `listing` writes them in one line, separated by semicolons, and the loop prints them one per line. `same_list` compares that line, character for character, with the detail text of the sympy check `geometry.spin_connection_components`.

```python
reproduces(antisymmetric and postulate, "the canonical spin connection is "
           "antisymmetric and obeys the vielbein postulate",
           (PY, ["geometry.omega_antisymmetric",
                 "geometry.gamma_covariantly_constant"]),
           (WL, ["connection_primordial"]))
reproduces(len(nonzero) == 12 and same_list,
           "the 12 nonzero connection components equal the recorded list",
           (PY, ["geometry.spin_connection_components"]))
```

Two checks: the connection is antisymmetric and canonical (three records), and it has exactly the 12 recorded components. Out [4] prints the twelve components, which are those derived by hand in Section 18.3: $a_4'e^{a_4}\sin^{1/6}z$ and $He^{a_4}\sin^{1/6}z$ for each inflating direction, $-a_4'e^{-a_4}\sin^{1/6}z$ and $-He^{-a_4}\sin^{1/6}z$ for each deflating extra time.

**In [5], γ^μ Ω_μ direction by direction.**

```python
def coefficient(X, a):
    """The coefficient of gamma^(a) in the matrix X (exact, by a trace)."""
    return sp.simplify((G[a] * X).trace() / (16 * ETA[a]))
```

`coefficient(X, a)` extracts the coefficient of $\gamma^{(a)}$ in a matrix $X$. The rule behind it: the **trace** (the sum of the diagonal entries) of $\gamma^{(a)}\gamma^{(b)}$ is $16\eta_{aa}$ if $a = b$ and 0 otherwise. So if $X = \sum_bc_b\gamma^{(b)} + (\text{products of several gammas})$, then $\mathrm{tr}(\gamma^{(a)}X) = 16\eta_{aa}c_a$, and $c_a = \mathrm{tr}(\gamma^{(a)}X)/(16\eta_{aa})$.

```python
contributions = {mu: (patch.gup[mu] * patch.Om[mu]).applyfunc(sp.simplify)
                 for mu in range(1, 9)}
for mu in range(1, 9):
    c4, c8 = coefficient(contributions[mu], 4), coefficient(contributions[mu], 8)
    rest = (contributions[mu] - c4 * G[4] - c8 * G[8]).applyfunc(sp.simplify)
    assert rest == sp.zeros(16)  # nothing but gamma^(x4) and gamma^(x8)
    say(f"direction {COORDS[mu]}: coefficient of gamma^(x4) = {short(c4)}, "
        f"of gamma^(x8) = {short(c8)}")
total = sp.zeros(16)
for mu in range(1, 9):
    total += contributions[mu]
check(total.applyfunc(sp.simplify) == 3 * H * G[8],
      "gamma^mu Omega_mu = 3 H gamma^(x8): the a4' terms of the deflation cancel")
```

`contributions[mu]` is $\gamma^\mu\Omega_\mu$ for one direction (no sum). For each direction the loop extracts the coefficients of $\gamma^{(x_4)}$ and $\gamma^{(x_8)}$ and asserts that nothing else is left (`assert` stops the notebook if the condition is false). Then `total` adds the eight contributions and the check requires $3H\gamma^{(x_8)}$. Out [5] prints, exactly as derived in Section 18.3: $a_4'/2$ and $H/2$ for $x_1, x_2, x_3$; $-a_4'/2$ and $H/2$ for $x_5, x_6, x_7$; zero for $x_4$ and $x_8$.

**In [6], Figure 18b.1: the connection along the deflating history.**

```python
params = read_json(PARAMETERS)["physics"]
A_hist, H_hist = params["historyA"], params["H"]  # 1.0 and 1.0
history = {a4: A_hist * H_hist * x4, H: H_hist}  # a4 = A H x4


def along(expr, times, zv=sp.pi / 4):
    """Evaluate expr along the history at the times x4 (numbers for the figure)."""
    e = expr.subs(sp.Derivative(a4, x4), A_hist * H_hist).subs(history)
    f = sp.lambdify(x4, e.subs(z, zv), "numpy")
    return np.broadcast_to(np.asarray(f(times), dtype=float), times.shape)
```

`params` is the physics block of the Kohn-Sham parameter record; it gives the canonical history $a_4 = AHx_4$ with $A = 1$ and $H = 1$. `history` is a substitution rule. `along(expr, times)` turns a sympy expression into numbers for the figure: it replaces $a_4'$ by $AH$ (the derivative of $AHx_4$), then $a_4$ by $AHx_4$ and $H$ by its value, sets $z = \pi/4$, and `sp.lambdify` turns the result into a numpy function of $x_4$. `np.broadcast_to` makes sure that a constant expression also returns one number per time.

```python
times = np.linspace(0.0, 2.0, 201)  # x4 from 0 to 2, a4 from 0 to 2
infl = along(patch.om[1, 1, 4], times)
defl = along(-patch.om[5, 4, 5], times)
c_infl = along(3 * coefficient(contributions[1], 4), times)
c_defl = along(3 * coefficient(contributions[5], 4), times)
```

`times` holds 201 evenly spaced times from 0 to 2 (`np.linspace`). `infl` is the component $\omega_{x_1,x_1x_4} = a_4'e^{a_4}\sin^{1/6}z$ of an inflating direction and `defl` the component $-\omega_{x_5,x_4x_5} = a_4'e^{-a_4}\sin^{1/6}z$ of a deflating extra time. `c_infl` and `c_defl` are three times the coefficient of $\gamma^{(x_4)}$ from one inflating and from one deflating direction: the contributions of the three directions of each kind.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
axes[0].semilogy(times, infl, color="#2a78d6", label="inflating, $x_1$")
axes[0].semilogy(times, defl, color="#eb6834", label="deflating extra time, $x_5$")
axes[0].set_xlabel("time $x_4$ (units $1/H$); $a_4 = AHx_4$")
axes[0].set_ylabel("connection coefficient (units $H$)")
axes[0].legend()
axes[1].plot(times, c_infl, color="#2a78d6", label="$x_1, x_2, x_3$ together")
axes[1].plot(times, c_defl, color="#eb6834", label="$x_5, x_6, x_7$ together")
axes[1].plot(times, c_infl + c_defl, color="#52514e", linestyle="--", label="sum")
axes[1].set_xlabel("time $x_4$ (units $1/H$)")
axes[1].set_ylabel("coefficient of $\\gamma^{(x_4)}$ in $\\gamma^\\mu\\Omega_\\mu$")
axes[1].set_ylim(-2.0, 2.0)
axes[1].legend(loc="center right")
save_figure(fig, "connection_history",
            "The spin connection of the author's metric along the canonical "
            "deflating history $a_4 = AHx_4$ with $A = 1$, $H = 1$, at $z = \\pi/4$. "
            "Left, logarithmic vertical axis: the coefficient "
            "$a_4^\\prime e^{a_4}\\sin^{1/6}z$ of an inflating 3-space direction "
            "grows and the coefficient $a_4^\\prime e^{-a_4}\\sin^{1/6}z$ of a "
            "deflating extra time decays, both in units of $H$, against the time "
            "$x_4$ in units of $1/H$. Right: their contributions to the "
            "coefficient of $\\gamma^{(x_4)}$ in $\\gamma^\\mu\\Omega_\\mu$, "
            "$+3AH/2$ from the three inflating and $-3AH/2$ from the three "
            "deflating directions, constant in time; their sum, dashed, is zero, "
            "so only $3H\\gamma^{(x_8)}$ survives.")
```

The left panel draws the two components with a logarithmic vertical axis (`semilogy`), the right panel the two contributions and their sum (dashed). **What you see in Figure 18b.1:** on the left a rising straight line (the inflating component grows like $e^{a_4}$, a straight line on a logarithmic axis) and a falling one (the deflating component decays like $e^{-a_4}$); on the right two horizontal lines at $+3AH/2 = +1.5$ and $-1.5$ and their sum at zero. Why: the factor $1/f_\mu$ of $\gamma^\mu$ undoes the growth and the decay exactly, and the two kinds of directions contribute with opposite signs; only $3H\gamma^{(x_8)}$ survives.

**In [7], an algebra for the jets.**

```python
class Jet:
    """A polynomial in numbered generators with sympy coefficients."""

    __slots__ = ("terms", "odd")

    def __init__(self, terms, odd):
        self.terms = terms  # {(generator numbers, sorted): coefficient}
        self.odd = odd  # True: Grassmann generators, False: commuting ones

    @staticmethod
    def symbol(number, odd):
        return Jet({(number,): sp.Integer(1)}, odd)
```

An object of the class `Jet` is a polynomial: `terms` is a dictionary whose keys are **monomials**, written as sorted tuples of generator numbers (the tuple `(3, 17)` is the product of generators 3 and 17), and whose values are sympy coefficients. `odd` says whether the generators anticommute (Grassmann) or commute. `__slots__` only fixes the two attribute names. `Jet.symbol(number, odd)` is the polynomial consisting of one generator with coefficient 1 (`@staticmethod` marks a function that belongs to the class but needs no object).

```python
    def __add__(self, other):
        terms = dict(self.terms)
        for key, c in other.terms.items():
            terms[key] = terms[key] + c if key in terms else c
        return Jet(terms, self.odd)

    def __neg__(self):
        return Jet({key: -c for key, c in self.terms.items()}, self.odd)

    def __sub__(self, other):
        return self + (-other)

    def times(self, number):
        """Multiply by a number or a sympy coefficient."""
        if number == 0:
            return Jet({}, self.odd)
        return Jet({key: number * c for key, c in self.terms.items()}, self.odd)
```

`__add__` defines what `+` does: copy the terms of the first polynomial and add the coefficients of the second, monomial by monomial (`terms[key] + c if key in terms else c` adds when the monomial is already present and inserts it otherwise). `__neg__` defines `-p` (every coefficient negated) and `__sub__` defines `p - q` as `p + (-q)`. `times(number)` multiplies every coefficient by a number or a sympy expression; multiplying by 0 returns the empty polynomial.

```python
    def __mul__(self, other):
        terms = {}
        for k1, c1 in self.terms.items():
            for k2, c2 in other.terms.items():
                sign = 1
                if self.odd:
                    if set(k1) & set(k2):  # a generator twice: theta theta = 0
                        continue
                    swaps = sum(1 for p in k1 for q in k2 if p > q)
                    sign = -1 if swaps % 2 else 1  # sorting costs (-1)^swaps
                key = tuple(sorted(k1 + k2))
                c = sign * c1 * c2
                terms[key] = terms[key] + c if key in terms else c
        return Jet(terms, self.odd)
```

`__mul__` defines `p * q`: every monomial of `p` is multiplied by every monomial of `q`. For commuting generators the product monomial is the sorted joined tuple. For Grassmann generators two more rules apply. If the two monomials share a generator, the product is zero ($\theta\theta = 0$) and is skipped (`set(k1) & set(k2)` is the set of common generators). Otherwise the joined tuple must be sorted, and each exchange of two anticommuting generators costs a sign: the number of exchanges needed is the number of pairs $(p, q)$ with $p$ from the first and $q$ from the second monomial and $p > q$, and the sign is $(-1)^{\mathrm{swaps}}$.

```python
    def derivative(self, number):
        """The left derivative with respect to the generator number."""
        terms = {}
        for key, c in self.terms.items():
            if number not in key:
                continue
            place = key.index(number)
            rest = key[:place] + key[place + 1:]
            if self.odd:  # move the generator to the front first
                c = c if place % 2 == 0 else -c
            else:  # an ordinary power rule
                c = key.count(number) * c
            terms[rest] = terms[rest] + c if rest in terms else c
        return Jet(terms, self.odd)
```

`derivative(number)` is the **left derivative** with respect to one generator: in each monomial that contains it, the generator is removed. For commuting generators this is the power rule (the coefficient is multiplied by the number of times the generator occurs). For Grassmann generators the generator is first moved to the front of the monomial, which passes the `place` generators before it and costs $(-1)^{\mathrm{place}}$; then it is removed. The left derivative is the one used for the Euler-Lagrange expressions of a Grassmann field.

```python
    def substitute(self, rule):
        """Replace symbols in every coefficient (rule: {old: new})."""
        return Jet({key: c.subs(rule) for key, c in self.terms.items()}, self.odd)

    def is_zero(self):
        """True when every coefficient is exactly zero."""
        for c in self.terms.values():
            e = sp.expand(c)
            if e != 0 and sp.simplify(e) != 0:
                return False
        return True


def zero(odd):
    return Jet({}, odd)


def all_zero(items):
    return all(item.is_zero() for item in items)
```

`substitute` replaces symbols in every coefficient (a helper that the later cells do not need). `is_zero` decides whether a polynomial is zero: every coefficient is first expanded (`sp.expand` multiplies out products and powers) and, if that does not give 0, simplified (`sp.simplify` uses identities such as $\sin^2 + \cos^2 = 1$). If any coefficient is not zero, the answer is False. `zero(odd)` is the empty polynomial and `all_zero(items)` tests a whole list.

**In [8], matrices acting on columns of polynomials, and the jet.**

```python
def mat_vec(M, v, odd):
    """The matrix M times the column v of algebra elements."""
    out = []
    for A in range(16):
        acc = zero(odd)
        for B in range(16):
            if M[A, B] != 0:
                acc = acc + v[B].times(M[A, B])
        out.append(acc)
    return out


def row_mat(v, M, odd):
    """The row v of algebra elements times the matrix M."""
    out = []
    for B in range(16):
        acc = zero(odd)
        for A in range(16):
            if M[A, B] != 0:
                acc = acc + v[A].times(M[A, B])
        out.append(acc)
    return out


def dot(u, v, odd):
    """The row u times the column v (the order of the factors is kept)."""
    acc = zero(odd)
    for p, q in zip(u, v):
        if p.terms and q.terms:
            acc = acc + p * q
    return acc
```

A spinor at one point is a column of 16 polynomials. `mat_vec(M, v)` is the matrix $M$ times the column $v$: component $A$ is $\sum_BM_{AB}v_B$ (only the nonzero entries are used). `row_mat(v, M)` is the row $v$ times $M$: component $B$ is $\sum_Av_AM_{AB}$. `dot(u, v)` is the row $u$ times the column $v$, $\sum_Au_Av_A$, with the factor of $u$ always written LEFT of the factor of $v$; this order matters for Grassmann generators, and it is the order of the bilinears $\Psi^\dagger X\Psi$.

```python
def number_psi_star(A):
    return A


def number_psi(A):
    return 16 + A


def number_dpsi_star(mu, A):
    return 32 + 16 * (mu - 1) + A


def number_dpsi(mu, A):
    return 160 + 16 * (mu - 1) + A


def jets(odd):
    """The first jet (Psi^*, Psi, d Psi^*, d Psi) as algebra generators."""
    return ([Jet.symbol(number_psi_star(A), odd) for A in range(16)],
            [Jet.symbol(number_psi(A), odd) for A in range(16)],
            {mu: [Jet.symbol(number_dpsi_star(mu, A), odd) for A in range(16)]
             for mu in range(1, 9)},
            {mu: [Jet.symbol(number_dpsi(mu, A), odd) for A in range(16)]
             for mu in range(1, 9)})
```

The numbering of the 288 generators: $\Psi^*_A$ is number $A$ ($A = 0, \dots, 15$; Python counts from 0), $\Psi_A$ is $16 + A$, $\partial_\mu\Psi^*_A$ is $32 + 16(\mu - 1) + A$ and $\partial_\mu\Psi_A$ is $160 + 16(\mu - 1) + A$, for $\mu = 1, \dots, 8$. `jets(odd)` returns the jet as four parts: the column $\Psi^*$, the column $\Psi$, and two dictionaries of columns for the derivatives.

```python
NO_REFLECTION = {mu: 1 for mu in range(1, 9)}
MIRROR = {mu: (-1 if mu == 8 else 1) for mu in range(1, 9)}  # x8 -> const - x8


def transform(J, P, signs, odd):
    """The jet of Psi'(x) = P Psi(R x)."""
    psi_star, psi, dpsi_star, dpsi = J
    Pc = P.conjugate()
    return (mat_vec(Pc, psi_star, odd), mat_vec(P, psi, odd),
            {mu: [x.times(signs[mu]) for x in mat_vec(Pc, dpsi_star[mu], odd)]
             for mu in range(1, 9)},
            {mu: [x.times(signs[mu]) for x in mat_vec(P, dpsi[mu], odd)]
             for mu in range(1, 9)})
```

`NO_REFLECTION` and `MIRROR` hold the signs of a coordinate reflection $R$: all $+1$, or $-1$ for $x_8$ only (the mirror $x_8 \to \pi/(6H) - x_8$). `transform(J, P, signs)` returns the jet of the new field $\Psi'(x) = P\Psi(Rx)$: the components are multiplied by $P$, their conjugates by $P^*$ (`P.conjugate()`, the matrix of conjugate entries; for the real matrices used here it equals $P$), and each derivative along $x_\mu$ also gets the sign of the reflection of $x_\mu$, by the chain rule.

**In [9], the theory on the jet.**

```python
def covariant(geo, J, odd):
    """D_mu Psi and D_mu Psibar for mu = 1..8."""
    psi_star, psi, dpsi_star, dpsi = J
    Dpsi = {mu: [p + q for p, q in zip(dpsi[mu], mat_vec(geo.Om[mu], psi, odd))]
            for mu in range(1, 9)}
    Dbar = {mu: [p - q for p, q in zip(row_mat(dpsi_star[mu], C, odd),
                                       row_mat(psi_star, C * geo.Om[mu], odd))]
            for mu in range(1, 9)}
    return Dpsi, Dbar
```

`covariant` returns, for each $\mu$, the columns $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$ and the rows $D_\mu\bar\Psi = (\partial_\mu\Psi^*)^TC - \Psi^{*T}C\Omega_\mu$; the second is $\partial_\mu\bar\Psi - \bar\Psi\Omega_\mu$ written with $\bar\Psi = \Psi^\dagger C$ (the row of the conjugates times $C$).

```python
def scalar(J, odd):
    """S = Psibar Psi = Psi^dagger C Psi."""
    return dot(J[0], mat_vec(C, J[1], odd), odd)
```

$S = \Psi^\dagger C\Psi$: the row of conjugates times the column $C\Psi$.

```python
def lagrangian(geo, J, odd, mass, coup, upoly=None, density=True):
    """L = sqrt|g| [ K - m S - U(S) ] (density=False: without sqrt|g|)."""
    Dpsi, Dbar = covariant(geo, J, odd)
    kin = zero(odd)
    for mu in range(1, 9):
        kin = kin + dot(J[0], mat_vec(C * geo.gup[mu], Dpsi[mu], odd), odd)
        kin = kin - dot(Dbar[mu], mat_vec(geo.gup[mu], J[1], odd), odd)
    S = scalar(J, odd)
    L = kin.times(sp.Rational(1, 2)) - S.times(mass)
    if upoly is None:  # U = (lambda/2) S^2
        L = L - (S * S).times(coup / 2)
    else:  # U = u1 S + u2 S^2 + u3 S^3
        L = L - S.times(upoly[1]) - (S * S).times(upoly[2])
        L = L - (S * S * S).times(upoly[3])
    return L.times(geo.sqrtg) if density else L
```

The Lagrangian of Section 18.4, term by term: `kin` adds, for each $\mu$, $\bar\Psi\gamma^\mu D_\mu\Psi$ (the row $\Psi^\dagger$ times $C\gamma^\mu D_\mu\Psi$) and subtracts $(D_\mu\bar\Psi)\gamma^\mu\Psi$. Then $\mathcal{L}/\sqrt{|g|} = \frac12K_{\rm sum} - mS - U(S)$, with $U = \frac{\lambda}{2}S^2$, or, when the argument `upoly` is given, the cubic $U = u_1S + u_2S^2 + u_3S^3$. With `density=True` the result is multiplied by $\sqrt{|g|}$.

```python
def field_operator(geo, J, odd, mass, coup):
    """E = gamma^mu D_mu Psi - (m + lambda S) Psi (16 algebra elements)."""
    Dpsi, _ = covariant(geo, J, odd)
    S = scalar(J, odd)
    out = [zero(odd) for _ in range(16)]
    for mu in range(1, 9):
        out = [p + q for p, q in zip(out, mat_vec(geo.gup[mu], Dpsi[mu], odd))]
    return [out[A] - J[1][A].times(mass) - (S * J[1][A]).times(coup)
            for A in range(16)]
```

`field_operator` returns the 16 components of $E = \gamma^\mu D_\mu\Psi - (m + \lambda S)\Psi$: the sum over $\mu$ of $\gamma^\mu D_\mu\Psi$, minus $m\Psi_A$, minus $\lambda S\Psi_A$.

```python
def emt(geo, J, odd, mass, coup):
    """T_mu nu for mu <= nu (36 components)."""
    Dpsi, Dbar = covariant(geo, J, odd)
    L = lagrangian(geo, J, odd, mass, coup, density=False)
    T = {}
    for mu in range(1, 9):
        for nu in range(mu, 9):
            t = (dot(J[0], mat_vec(C * geo.glow[mu], Dpsi[nu], odd), odd)
                 + dot(J[0], mat_vec(C * geo.glow[nu], Dpsi[mu], odd), odd)
                 - dot(Dbar[mu], mat_vec(geo.glow[nu], J[1], odd), odd)
                 - dot(Dbar[nu], mat_vec(geo.glow[mu], J[1], odd), odd))
            t = t.times(sp.Rational(1, 4))
            if mu == nu:
                t = t - L.times(geo.g[mu])
            T[mu, nu] = t
    return T
```

`emt` returns the 36 components $T_{\mu\nu}$ with $\mu \leq \nu$ of the tensor of Section 18.4: the four kinetic bilinears with the lowered gammas, times $\frac14$, and, on the diagonal, minus $g_{\mu\mu}\mathcal{L}/\sqrt{|g|}$ (the off-diagonal $g_{\mu\nu}$ vanish).

```python
def current(geo, J, odd):
    """J^mu = i Psibar gamma^mu Psi (8 components)."""
    return {mu: dot(J[0], mat_vec(sp.I * C * geo.gup[mu], J[1], odd), odd)
            for mu in range(1, 9)}
```

`current` returns the 8 components $J^\mu = i\bar\Psi\gamma^\mu\Psi$ (the convention of the sympy pairing report; `sp.I` is $i$).

```python
def euler_lagrange(geo, J, odd, mass, coup):
    """dL/dPsi^*_A - sum_mu d_mu (dL/d(d_mu Psi^*_A)), A = 0..15."""
    L = lagrangian(geo, J, odd, mass, coup)
    out = []
    for A in range(16):
        e = L.derivative(number_psi_star(A))
        for mu in range(1, 9):
            q = L.derivative(number_dpsi_star(mu, A))  # c Psi_B, linear in Psi
            for key, c in q.terms.items():
                B = key[0] - 16  # the component Psi_B of this term
                e = e - Jet({key: d(c, mu)}, odd)  # (d_mu c) Psi_B
                e = e - Jet({(number_dpsi(mu, B),): c}, odd)  # c d_mu Psi_B
        out.append(e)
    return out
```

`euler_lagrange` derives the Euler-Lagrange expressions from the Lagrangian itself, without using the formula for $E$: for each $A$, the derivative of $\mathcal{L}$ with respect to the generator $\Psi^*_A$, minus $\sum_\mu\partial_\mu$ of the derivative with respect to $\partial_\mu\Psi^*_A$. That second derivative, `q`, is a sum of terms $c\,\Psi_B$ with coefficient functions $c$ of the point (the kinetic term contains $\partial_\mu\Psi^*$ only multiplied by $\Psi$). Its total derivative is computed with the product rule, $\partial_\mu(c\Psi_B) = (\partial_\mu c)\Psi_B + c\,\partial_\mu\Psi_B$: the first piece keeps the monomial and differentiates the coefficient; the second replaces $\Psi_B$ by the generator of $\partial_\mu\Psi_B$.

**In [10], theorem T1 for dirac16complex00.**

```python
SAMPLE = {z: sp.Rational(7, 10), H: sp.Rational(13, 10), m: sp.Rational(11, 10),
          lam: sp.Rational(3, 5)}  # a sample point for counting only
SAMPLE_A4 = {"a4p": sp.Rational(9, 10), "a4": sp.Rational(2, 5)}


def count_nonzero(element):
    """The number of monomials whose coefficient is not zero at the sample."""
    n = 0
    for c in element.terms.values():
        c = c.subs(sp.Derivative(a4, x4), SAMPLE_A4["a4p"])  # a4' first,
        c = c.subs(a4, SAMPLE_A4["a4"]).subs(SAMPLE)  # then a4 and the rest
        value = complex(sp.N(c, 30))
        n += abs(value) > 1e-20
    return n


COUNTS = {}  # the monomial counts for the figures
```

Counting the monomials of a polynomial whose coefficients are long expressions is slow if every coefficient is simplified. `count_nonzero` evaluates each coefficient at one sample point (the fractions in `SAMPLE` and `SAMPLE_A4`: $z = 0.7$, $H = 1.3$, $m = 1.1$, $\lambda = 0.6$, $a_4' = 0.9$, $a_4 = 0.4$) with 30 digits (`sp.N(c, 30)`) and counts those that are not zero. The count only describes the size of a polynomial; it is not part of any proof. `COUNTS` keeps the counts for the figures.

```python
def t1_checks(odd):
    stat = "grassmann" if odd else "commuting"
    field = "dirac16complex" if odd else "dirac16complex00"
    tag = f"primordial_{stat}"
    J = jets(odd)
    JG = transform(J, GAM, NO_REFLECTION, odd)
    s_ok = (scalar(JG, odd) - scalar(J, odd)).is_zero()
    L_image = lagrangian(patch, JG, odd, m, lam)
    L_plain = lagrangian(patch, J, odd, m, lam)
    L_partner = lagrangian(patch, J, odd, -m, -lam)
    L_wrong = lagrangian(patch, J, odd, -m, lam)
    n_L = count_nonzero(L_plain)
    COUNTS[stat] = {"L": n_L, "L[Gamma Psi]": count_nonzero(L_image),
                    "T1 sum": count_nonzero(L_image + L_partner),
                    "control (m, l)": count_nonzero(L_image + L_plain),
                    "control (-m, l)": count_nonzero(L_image + L_wrong)}
    wl_count = f"L has {n_L} monomials" in recorded(WL, f"T1_Lagrangian_{tag}")[
        "detail"]
    report(f"{field}: monomials of L with a nonzero coefficient", n_L)
    reproduces(s_ok and (L_image + L_partner).is_zero() and wl_count,
               f"T1 {field}: S kept, L_m,l[Gamma Psi] = -L_-m,-l[Psi]",
               (PY, [f"T1.metric.{stat}.S_invariant", f"T1.metric.{stat}.lagrangian"]),
               (WL, [f"T1_scalar_and_kinetic_{tag}", f"T1_Lagrangian_{tag}"]))
```

`t1_checks(odd)` runs the whole T1 test for one statistics. `stat`, `field` and `tag` are the names used in the record's check names. `J` is the jet and `JG` the jet of $\Gamma\Psi$. `s_ok` tests $S[\Gamma\Psi] - S[\Psi] = 0$. Then four Lagrangians: of the image with $(m, \lambda)$, of $\Psi$ with $(m, \lambda)$, with $(-m, -\lambda)$ (the T1 partner) and with $(-m, \lambda)$ (a wrong partner). `n_L` is the number of monomials of $\mathcal{L}_{m,\lambda}[\Psi]$, and `COUNTS[stat]` stores the counts of five polynomials for Figure 18b.2. `wl_count` checks that the detail text of the Wolfram check `T1_Lagrangian_primordial_<stat>` contains the same number ("L has 408 monomials"). The first check requires $S$ kept, $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{-m,-\lambda}[\Psi] = 0$ in all coefficients, and the agreement of the count.

```python
    controls = (not (L_image + L_plain).is_zero()
                and not (L_image + L_wrong).is_zero())
    reproduces(controls, f"T1 {field}: the negative controls fail as they must",
               (PY, [f"T1.metric.{stat}.negative_controls"]),
               (WL, [f"T1_Lagrangian_negative_controls_{tag}"]))
```

The negative controls: $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{m,\lambda}[\Psi]$ and $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{-m,\lambda}[\Psi]$ must NOT be zero.

```python
    E = field_operator(patch, J, odd, m, lam)
    CE = mat_vec(C, E, odd)
    EL = euler_lagrange(patch, J, odd, m, lam)
    derived = all_zero([EL[A] - CE[A].times(patch.sqrtg) for A in range(16)])
    E_image = field_operator(patch, JG, odd, m, lam)
    E_partner = mat_vec(GAM, field_operator(patch, J, odd, -m, -lam), odd)
    mapped = all_zero([E_image[A] + E_partner[A] for A in range(16)])
    reproduces(derived and mapped,
               f"T1 {field}: EL = sqrt|g| C E; E_m,l[Gamma Psi] = -Gamma E_-m,-l",
               (PY, [f"T1.metric.{stat}.euler_lagrange_derived",
                     f"T1.metric.{stat}.euler_lagrange_map"]),
               (WL, [f"T1_Euler_Lagrange_derived_{tag}",
                     f"T1_field_equation_covariance_{tag}"]))
```

`E` is the field operator, `CE` is $C$ times it, and `EL` the Euler-Lagrange expressions derived from $\mathcal{L}$. `derived` checks $\mathrm{EL}_A = \sqrt{|g|}\,(CE)_A$ for all 16 $A$: the field equation $E = 0$ IS the Euler-Lagrange equation of this Lagrangian. `mapped` checks $E_{m,\lambda}[\Gamma\Psi] + \Gamma E_{-m,-\lambda}[\Psi] = 0$, statement (T1b).

```python
    T_image = emt(patch, JG, odd, m, lam)
    T_partner = emt(patch, J, odd, -m, -lam)
    T_plain = emt(patch, J, odd, m, lam)
    T_pair = emt(patch, JG, odd, -m, -lam)
    emt_ok = all_zero([T_image[k] + T_partner[k] for k in T_image])
    pair_ok = all_zero([T_plain[k] + T_pair[k] for k in T_plain])
    COUNTS[stat]["T"] = {k: count_nonzero(T_plain[k]) for k in T_plain}
    COUNTS[stat]["T1 sign"] = {k: -1 for k in T_plain if emt_ok}
    J_image, J_plain = current(patch, JG, odd), current(patch, J, odd)
    current_ok = all_zero([J_image[mu] + J_plain[mu] for mu in range(1, 9)])
    reproduces(emt_ok and pair_ok and current_ok and len(T_image) == 36,
               f"T1 {field}: T -> -T (36), pair T sum 0, J -> -J (8)",
               (PY, [f"T1.metric.{stat}.emt", f"T1.metric.{stat}.pair_total_emt_zero",
                     f"T1.metric.{stat}.current"]),
               (WL, [f"T1_energy_momentum_{tag}", f"T1_current_{tag}"]))
```

Four tensors: of the image with $(m, \lambda)$, of $\Psi$ with $(-m, -\lambda)$, of $\Psi$ with $(m, \lambda)$ and of the image with $(-m, -\lambda)$. `emt_ok` checks $T[\Gamma\Psi; m, \lambda] + T[\Psi; -m, -\lambda] = 0$ for all 36 components (T1c, read from the other side), and `pair_ok` checks the pair statement $T[\Psi; m, \lambda] + T[\Gamma\Psi; -m, -\lambda] = 0$ (T1d). The counts of the 36 components and the proved signs $-1$ are stored for Figure 18b.3. `current_ok` checks $J[\Gamma\Psi] + J[\Psi] = 0$ for the 8 components. One check combines them, with three sympy and two Wolfram records.

```python
t1_checks(False)  # dirac16complex00: commuting components
```

The test is run for commuting components. Out [10] prints RESULT dirac16complex00: monomials of L with a nonzero coefficient = 408 and four PASS lines.

**In [11], theorem T1 for dirac16complex.**

```python
t1_checks(True)  # dirac16complex: Grassmann components
say("monomials of L with a nonzero coefficient: commuting "
    f"{COUNTS['commuting']['L']}, Grassmann {COUNTS['grassmann']['L']}")
```

The same test with Grassmann generators, then a line with both counts. Out [11]: 392 monomials and four PASS lines; the last line reads commuting 408, Grassmann 392. Why fewer: in $S^2$, products in which the same Grassmann generator occurs twice vanish ($\theta\theta = 0$), so some monomials of the commuting case are absent.

**In [12], a general potential and a random gravitational field.**

```python
u1, u2, u3 = sp.symbols("u1 u2 u3", real=True)
cubic_ok = True
for odd in (False, True):
    J = jets(odd)
    JG = transform(J, GAM, NO_REFLECTION, odd)
    L1 = lagrangian(patch, JG, odd, m, 0, upoly={1: u1, 2: u2, 3: u3})
    L2 = lagrangian(patch, J, odd, -m, 0, upoly={1: -u1, 2: -u2, 3: -u3})
    cubic_ok = cubic_ok and (L1 + L2).is_zero()
reproduces(cubic_ok, "T1 with a general cubic potential: L_m,U[Gamma Psi] = "
           "-L_-m,-U[Psi]", (PY, ["T1.metric.commuting.general_potential",
                                  "T1.metric.grassmann.general_potential"]))
```

Three symbols $u_1, u_2, u_3$ for a general cubic potential. For both statistics: the Lagrangian of the image with $(m, U)$ (the coupling argument is 0 and unused when `upoly` is given) plus the Lagrangian of $\Psi$ with $(-m, -U)$, where $-U$ has the coefficients $-u_1, -u_2, -u_3$, must vanish. This is (T1a) for a general potential.

```python
rng = random.Random(20261001)  # the seed of the Revision report


def fraction():
    return sp.Rational(rng.randint(-9, 9), rng.randint(1, 5))


class RandomField:
    """A general gravitational field at one point (only what L and E use)."""


field = RandomField()
E8 = [[fraction() for _ in range(8)] for _ in range(8)]  # e^mu_a, not diagonal
field.gup = {mu: sum((E8[mu - 1][a - 1] * G[a] for a in range(1, 9)), sp.zeros(16))
             for mu in range(1, 9)}
field.Om = {}
for mu in range(1, 9):
    M = sp.zeros(16)
    for a in range(1, 9):
        for b in range(a + 1, 9):
            M += fraction() * SAB[a, b]  # an antisymmetric omega
    field.Om[mu] = M
field.sqrtg = abs(fraction()) + 1
```

`random.Random(20261001)` is a random-number generator with the seed number used by the Revision report (the instance drawn here is the notebook's own). `fraction()` returns a random fraction $p/q$ with $p$ from $-9$ to $9$ and $q$ from 1 to 5. `RandomField` is an empty class that serves as a container. The field gets 64 random entries $e^\mu{}_a$ (a non-diagonal vielbein; `field.gup[mu]` is $\gamma^\mu = \sum_ae^\mu{}_a\gamma^{(a)}$), for each $\mu$ a connection $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$ with 28 random independent components (antisymmetry is built in by summing over $a < b$ only), and a positive volume factor. It is not the author's field and not a solution of anything: it stands for an arbitrary gravitational field at one point.

```python
random_ok = True
for odd in (False, True):
    J = jets(odd)
    JG = transform(J, GAM, NO_REFLECTION, odd)
    L_sum = (lagrangian(field, JG, odd, m, lam)
             + lagrangian(field, J, odd, -m, -lam))
    E1 = field_operator(field, JG, odd, m, lam)
    E2 = mat_vec(GAM, field_operator(field, J, odd, -m, -lam), odd)
    random_ok = random_ok and all_zero([L_sum] + [E1[A] + E2[A] for A in range(16)])
reproduces(random_ok, "T1 in a random general field (seed 20261001), both fields",
           (PY, ["T1.general_field.random_instance.commuting",
                 "T1.general_field.random_instance.grassmann"]))
```

For both statistics: the T1 identity of the Lagrangian and the map of the 16 components of the field operator must hold in this random field. This shows, by an example with no special structure, why T1 holds in every gravitational field: the proof never used the form of the coefficients. Out [12] shows two PASS lines.

**In [13], Figure 18b.2: what cancels.**

```python
labels = ["L", "L[Gamma Psi]", "T1 sum", "control (m, l)", "control (-m, l)"]
texts = ["$\\mathcal{L}_{m,\\lambda}[\\Psi]$",
         "$\\mathcal{L}_{m,\\lambda}[\\Gamma\\Psi]$",
         "T1: $+\\,\\mathcal{L}_{-m,-\\lambda}[\\Psi]$",
         "control: $+\\,\\mathcal{L}_{m,\\lambda}[\\Psi]$",
         "control: $+\\,\\mathcal{L}_{-m,\\lambda}[\\Psi]$"]
fig, ax = plt.subplots(figsize=(9.0, 4.6))
xs = np.arange(len(labels))
for shift, stat, colour in [(-0.18, "commuting", "#2a78d6"),
                            (0.18, "grassmann", "#eb6834")]:
    values = [COUNTS[stat][k] for k in labels]
    ax.bar(xs + shift, values, width=0.36, color=colour,
           label="commuting (dirac16complex00)" if stat == "commuting"
           else "Grassmann (dirac16complex)")
    for x, v in zip(xs + shift, values):
        ax.text(x, v + 6, str(v), ha="center", fontsize=8)
ax.set_xticks(xs, texts, fontsize=8.5, rotation=12)
ax.set_ylabel("monomials with a nonzero coefficient")
ax.set_ylim(0, 480)
ax.legend(loc="upper right")
save_figure(fig, "lagrangian_cancellation",
            "What cancels in theorem T1, in the author's metric with an arbitrary "
            "deflating history. Vertical axis: the number of monomials in the 288 "
            "jet values whose coefficient is not zero. The first two bars of each "
            "colour: the Lagrangian of a field and of its chirality image, "
            "$408$ monomials for commuting components and $392$ for Grassmann "
            "components. Third: the T1 sum with the reversed mass and coupling, "
            "exactly zero. Fourth and fifth, the negative controls: with the "
            "same mass and coupling the mass term and the $S^2$ term survive; "
            "with only the mass reversed the $S^2$ term survives. So both $m$ and "
            "$\\lambda$ must change sign.")
```

Five groups of two bars (commuting in blue, Grassmann in orange; `xs + shift` moves the two bars of a group apart), with the number written above each bar. **What you see in Figure 18b.2:** 408 and 392 monomials for $\mathcal{L}_{m,\lambda}[\Psi]$ and the same numbers for $\mathcal{L}_{m,\lambda}[\Gamma\Psi]$; zero for the T1 sum; and nonzero bars for the two negative controls. In the first control only the mass term and the $S^2$ term survive (the kinetic terms cancel, the potential terms add), in the second only the $S^2$ term. Why: $\Gamma$ reverses exactly the kinetic part, so a cancellation needs both $m \to -m$ and $\lambda \to -\lambda$.

**In [14], Figure 18b.3: the 36 components of the tensor.**

```python
counts = np.zeros((8, 8))
signs = np.zeros((8, 8))
for (mu, nu), n in COUNTS["commuting"]["T"].items():
    counts[mu - 1, nu - 1] = counts[nu - 1, mu - 1] = n
for (mu, nu), s in COUNTS["commuting"]["T1 sign"].items():
    signs[mu - 1, nu - 1] = signs[nu - 1, mu - 1] = s
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.6))
image = axes[0].imshow(counts, cmap="Blues")
fig.colorbar(image, ax=axes[0], shrink=0.85, label="monomials")
axes[1].imshow(signs, cmap="coolwarm", vmin=-1, vmax=1)
for i in range(8):
    for j in range(8):
        axes[0].text(j, i, str(int(counts[i, j])), ha="center", va="center",
                     fontsize=7, color="black" if counts[i, j] < 200 else "white")
        axes[1].text(j, i, f"{int(signs[i, j]):+d}", ha="center", va="center",
                     fontsize=8, color="white")
for ax, title in [(axes[0], "monomials of $T_{\\mu\\nu}[\\Psi; m, \\lambda]$"),
                  (axes[1], "sign of the T1 partner's $T_{\\mu\\nu}$")]:
    ax.set_xticks(range(8), [f"$x_{a}$" for a in range(1, 9)])
    ax.set_yticks(range(8), [f"$x_{a}$" for a in range(1, 9)])
    ax.grid(False)
    ax.set_title(title, fontsize=10)
```

`counts` and `signs` are $8 \times 8$ arrays filled symmetrically from the 36 stored components ($T_{\nu\mu} = T_{\mu\nu}$). The left panel draws the counts with a blue colour scale and writes each number in its cell (white text on dark cells); the right panel draws the proved signs. The ticks name the coordinates.

```python
save_figure(fig, "emt_signs",
            "The 36 independent components of the energy-momentum tensor in the "
            "author's metric, row index $\\mu$ and column index $\\nu$ from $x_1$ "
            "to $x_8$. Left: the number of jet monomials in each component for a "
            "field with commuting components; the diagonal components carry the "
            "whole Lagrangian, the off-diagonal ones only kinetic terms. Right: "
            "the sign that relates the component of the T1 partner "
            "$\\Gamma\\Psi$ with $(-m, -\\lambda)$ to that of $\\Psi$ with "
            "$(m, \\lambda)$, proved to be $-1$ everywhere: energy density, "
            "momentum densities and pressures are all reversed, and the pair has "
            "a zero total.")
```

**What you see in Figure 18b.3:** on the left, 376 monomials in each diagonal component (those components contain the whole Lagrangian through $-g_{\mu\mu}\mathcal{L}/\sqrt{|g|}$) and 64 or 80 in each off-diagonal one (only kinetic bilinears); on the right, $-1$ in every one of the 64 cells. The T1 partner carries exactly the opposite energy density, momentum densities and pressures.

**In [15], the mirror patch.**

```python
mirror = Geometry(-1)  # the mirror patch pi/2 < z < pi, f8 = -cot z > 0
to_mirror = {z: sp.pi - z}


class Reflected:
    """The patch's coefficient functions evaluated at the mirror point pi - z."""


reflected = Reflected()
reflected.sqrtg = sp.expand(patch.sqrtg.subs(to_mirror))
reflected.g = {mu: sp.expand(patch.g[mu].subs(to_mirror)) for mu in range(1, 9)}
for name in ("Om", "gup", "glow"):
    setattr(reflected, name, {mu: getattr(patch, name)[mu].subs(to_mirror)
                              .applyfunc(sp.expand) for mu in range(1, 9)})
```

`mirror` is the geometry of the mirror patch ($s_8 = -1$, so $f_8 = -\cot z > 0$ there). `to_mirror` is the substitution $z \to \pi - z$. `reflected` holds the patch's coefficient functions evaluated at the mirror point: $\sqrt{|g|}$, the metric, $\Omega_\mu$ and both kinds of curved gammas, each with $z$ replaced by $\pi - z$ and expanded (`setattr(object, name, value)` stores a value under a name given as a string).

```python
isometry = all(sp.simplify(patch.g[mu].subs(to_mirror) - patch.g[mu]) == 0
               for mu in range(1, 9))
degenerate = (sp.limit(patch.g[8], z, sp.pi / 2) == 0
              and sp.limit(patch.sqrtg, z, sp.pi / 2) == 0)
reproduces(isometry and degenerate, "z -> pi - z is an isometry; the brane "
           "z = pi/2 is degenerate (g88 = 0, sqrt|g| = 0)",
           (PY, ["geometry.mirror_isometry", "geometry.brane_degenerate"]),
           (WL, ["T2_mirror_is_isometry"]))
```

`isometry` checks $g_{\mu\mu}(\pi - z) = g_{\mu\mu}(z)$ for all eight components; `degenerate` checks with limits (`sp.limit`) that $g_{88} \to 0$ and $\sqrt{|g|} \to 0$ as $z \to \pi/2$. One check, three records.

```python
mirror_postulate = all(
    sp.simplify(mirror.om[mu, a, b] + mirror.om[mu, b, a]) == 0
    for mu, a, b in itertools.product(range(1, 9), repeat=3))
for mu, nu in itertools.product(range(1, 9), repeat=2):
    M = mirror.gup[nu].applyfunc(lambda e: d(e, mu))
    for la in range(1, 9):
        if mirror.chr[nu, mu, la] != 0:
            M = M + mirror.chr[nu, mu, la] * mirror.gup[la]
    M = M + mirror.Om[mu] * mirror.gup[nu] - mirror.gup[nu] * mirror.Om[mu]
    mirror_postulate = mirror_postulate and all(sp.simplify(e) == 0 for e in M)
say(f"sqrt|g| on the mirror patch = {mirror.sqrtg} (positive there, cos z < 0)")
reproduces(mirror_postulate, "the mirror patch's own connection is canonical",
           (WL, ["connection_mirror_patch"]))
```

The mirror patch's own connection is antisymmetric and obeys the vielbein postulate (the same test as In [4]). Out [15] prints $\sqrt{|g|} = -\cos z$ on the mirror patch, positive there because $\cos z < 0$ for $\pi/2 < z < \pi$, and two PASS lines.

**In [16], Figure 18b.4: the metric on both patches.**

```python
zs = np.linspace(0.02, np.pi - 0.02, 400)
fig, ax = plt.subplots(figsize=(8.0, 4.4))
ax.plot(zs, np.sin(zs) ** (1.0 / 3.0), color="#2a78d6",
        label="$\\sin^{1/3}z$ (factor of $g_{11}$ and $-g_{55}$)")
ax.plot(zs, 1.0 / np.tan(zs) ** 2, color="#eb6834", label="$g_{88} = \\cot^2 z$")
ax.plot(zs, np.abs(np.cos(zs)), color="#1baf7a", label="$\\sqrt{|g|} = |\\cos z|$")
ax.axvline(np.pi / 2, color="#52514e", linestyle="--")
ax.text(np.pi / 2 + 0.04, 2.6, "brane $z = \\pi/2$", fontsize=9)
ax.axvspan(0.0, np.pi / 2, color="#2a78d6", alpha=0.05)
ax.text(0.25, 2.6, "patch", fontsize=9)
ax.text(2.35, 2.6, "mirror patch", fontsize=9)
ax.set_xlim(0.0, np.pi)
ax.set_ylim(0.0, 3.0)
ax.set_xlabel("hidden angle $z = 6Hx_8$ (radians)")
ax.set_ylabel("metric function (no unit)")
ax.legend(loc="center left", bbox_to_anchor=(0.02, 0.62), fontsize=8.5)
save_figure(fig, "mirror_metric",
            "The functions of the hidden angle that enter the author's metric, "
            "against $z = 6Hx_8$ from 0 to $\\pi$ (horizontal axis, radians; "
            "vertical axis, pure numbers): $\\sin^{1/3}z$, the factor of the "
            "3-space and extra-time components; $g_{88} = \\cot^2 z$; and "
            "$\\sqrt{|g|} = |\\cos z|$. The shaded half is the author's patch, the "
            "other half its mirror patch. Every curve is mirror-symmetric about "
            "the dashed brane $z = \\pi/2$, so $z \\to \\pi - z$ is an isometry. "
            "At the brane $g_{88}$ and $\\sqrt{|g|}$ vanish: the metric is "
            "degenerate there, and gluing the two patches is an assumption.")
```

400 values of $z$ from just above 0 to just below $\pi$ (the end points are avoided because $\cot^2 z$ is infinite there). Three curves: $\sin^{1/3}z$, $g_{88} = \cot^2 z$ (`1.0 / np.tan(zs) ** 2`) and $|\cos z|$; a dashed vertical line at the brane, a faint shading of the patch and three labels. **What you see in Figure 18b.4:** every curve is mirror-symmetric about $z = \pi/2$, so $z \to \pi - z$ is an isometry; at the brane $\sin^{1/3}z$ reaches its maximum 1 while $g_{88}$ and $\sqrt{|g|}$ touch zero: the metric is degenerate there, which is why gluing the two patches is an assumption and not a result.

**In [17], which matrix makes the mirror a pairing.**

```python
CANDIDATES = [("1", I16), ("Gamma", GAM), ("gamma^(x8)", G[8]),
              ("Gamma gamma^(x8)", GAM * G[8])]
FOUND = {}
for odd in (False, True):
    J = jets(odd)
    for name, P in CANDIDATES:
        JP = transform(J, P, MIRROR, odd)
        L_mirror = lagrangian(mirror, JP, odd, m, lam)
        hit = None
        for sigma, sm, sl in itertools.product((1, -1), repeat=3):
            L_patch = lagrangian(reflected, J, odd, sm * m, sl * lam)
            if (L_mirror - L_patch.times(sigma)).is_zero():
                hit = (sigma, sm, sl)
                break
        FOUND[odd, name] = hit
```

Four candidate matrices: $1$, $\Gamma$, $\gamma^{(x_8)}$ and $\Gamma\gamma^{(x_8)} = P_8$. For each statistics and each candidate, `JP` is the jet of $\Psi'(x) = P\Psi(Rx)$ with the mirror reflection, and `L_mirror` its Lagrangian with $(m, \lambda)$ in the mirror geometry. The inner loop tries the eight sign choices $(\sigma, s_m, s_\lambda)$ and compares with $\sigma\,\mathcal{L}_{s_mm,s_\lambda\lambda}[\Psi]$ in the reflected patch geometry; `break` stops at the first relation that holds exactly. `FOUND` stores the result (or `None`).

```python
for name, _ in CANDIDATES:
    hit = FOUND[False, name]
    text = "no relation" if hit is None else (
        f"L = {'+' if hit[0] > 0 else '-'}L_({'' if hit[1] > 0 else '-'}m, "
        f"{'' if hit[2] > 0 else '-'}lambda)")
    say(f"P = {name}: {text} (the same for Grassmann components: "
        f"{FOUND[True, name] == hit})")
```

For each candidate the cell prints the relation found for commuting components and whether the Grassmann result is the same (the nested f-string writes the signs as $+$ or $-$ and leaves out a $+$ in front of $m$ and $\lambda$).

```python
expected = {"1": None, "Gamma": None, "gamma^(x8)": (1, -1, 1),
            "Gamma gamma^(x8)": (-1, 1, -1)}
reproduces(all(FOUND[odd, name] == expected[name]
               for odd in (False, True) for name, _ in CANDIDATES),
           "T2: only gamma^(x8) maps (m, lambda) to (-m, lambda) with L -> +L",
           (PY, ["T2.metric.commuting.reflection_table",
                 "T2.metric.grassmann.reflection_table"]),
           (WL, ["T2_mirror_Lagrangian_commuting", "T2_mirror_Lagrangian_grassmann"]))
```

The expected results of the sympy record: none for $1$ and $\Gamma$; $(+1, -1, +1)$, that is $+\mathcal{L}_{-m,\lambda}$, for $\gamma^{(x_8)}$; $(-1, +1, -1)$, that is $-\mathcal{L}_{m,-\lambda}$, for $P_8$. Out [17] shows exactly these four lines and the PASS line.

**In [18], T2 completed.**

```python
t2_ok = True
T2_SIGNS = {}
for odd in (False, True):
    J = jets(odd)
    JP = transform(J, G[8], MIRROR, odd)
    E1 = field_operator(mirror, JP, odd, m, lam)
    E2 = mat_vec(G[8], field_operator(reflected, J, odd, -m, lam), odd)
    el_ok = all_zero([E1[A] + E2[A] for A in range(16)])
    T1_ = emt(mirror, JP, odd, m, lam)
    T2_ = emt(reflected, J, odd, -m, lam)
    emt_ok = all_zero([T1_[k] - T2_[k].times(MIRROR[k[0]] * MIRROR[k[1]])
                       for k in T1_])
    if not odd:
        T2_SIGNS = {k: MIRROR[k[0]] * MIRROR[k[1]] for k in T1_ if emt_ok}
    J1, J2 = current(mirror, JP, odd), current(reflected, J, odd)
    current_ok = all_zero([J1[mu] - J2[mu].times(MIRROR[mu]) for mu in range(1, 9)])
    s_odd = (scalar(JP, odd) + scalar(J, odd)).is_zero()
    stat = "grassmann" if odd else "commuting"
    say(f"{stat}: field equations mapped {el_ok}, T pulled back {emt_ok}, "
        f"J pulled back {current_ok}, S reversed {s_odd}")
    t2_ok = t2_ok and el_ok and emt_ok and current_ok and s_odd
```

For both statistics with $P = \gamma^{(x_8)}$ and the mirror reflection: `el_ok` checks $E^{\rm mirror}_{m,\lambda}[\Psi'] + \gamma^{(x_8)}E^{\rm patch}_{-m,\lambda}[\Psi] = 0$ (T2b); `emt_ok` checks $T_{\mu\nu}[\Psi'] = \Lambda_\mu\Lambda_\nu T_{\mu\nu}[\Psi; -m, \lambda]$ with $\Lambda$ = `MIRROR` (T2c), and for commuting components the signs $\Lambda_\mu\Lambda_\nu$ are stored for the figure; `current_ok` checks $J'^\mu = \Lambda_\mu J^\mu$; `s_odd` checks $S[\gamma^{(x_8)}\Psi] + S[\Psi] = 0$. The cell prints the four results for each statistics.

```python
reproduces(t2_ok, "T2: field equations mapped, T and J pulled back (equal energy), "
           "S reversed", (PY, [f"T2.metric.{s}.{c}" for s in ("commuting", "grassmann")
                               for c in ("euler_lagrange_map", "emt", "current",
                                         "S_odd")]),
           (WL, ["T2_mirror_energy_momentum_and_current_commuting",
                 "T2_mirror_energy_momentum_and_current_grassmann",
                 "T2_mirror_Euler_Lagrange_commuting",
                 "T2_mirror_Euler_Lagrange_grassmann"]))
```

One check with eight sympy and four Wolfram records (the list comprehension builds the eight sympy names). Out [18] prints True eight times and the PASS line.

**In [19], Figure 18b.5: the two summaries of T2.**

```python
choices = list(itertools.product((1, -1), repeat=3))
grid = np.zeros((len(CANDIDATES), len(choices)))
for i, (name, _) in enumerate(CANDIDATES):
    if FOUND[False, name] is not None:
        grid[i, choices.index(FOUND[False, name])] = 1.0
t2_signs = np.zeros((8, 8))
for (mu, nu), s in T2_SIGNS.items():
    t2_signs[mu - 1, nu - 1] = t2_signs[nu - 1, mu - 1] = s
```

`choices` lists the eight sign choices in the order of the search. `grid` has one row per candidate and one column per choice, with 1 where a relation was found (`choices.index` finds the column). `t2_signs` is the $8 \times 8$ array of the stored signs $\Lambda_\mu\Lambda_\nu$.

```python
fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.4),
                         gridspec_kw={"width_ratios": [1.4, 1.0]})
axes[0].imshow(grid, cmap="Greens", vmin=0, vmax=1.4, aspect="auto")
axes[0].set_xticks(range(len(choices)),
                   [f"{'+' if s > 0 else '-'}L\n{'' if a > 0 else '-'}m\n"
                    f"{'' if b > 0 else '-'}$\\lambda$" for s, a, b in choices],
                   fontsize=8)
axes[0].set_yticks(range(len(CANDIDATES)),
                   ["$P = 1$", "$P = \\Gamma$", "$P = \\gamma^{(x_8)}$",
                    "$P = \\Gamma\\gamma^{(x_8)}$"])
axes[0].set_title("relation $\\mathcal{L}^{mirror}_{m,\\lambda}[P\\Psi] = "
                  "\\sigma\\mathcal{L}_{\\pm m,\\pm\\lambda}[\\Psi]$", fontsize=10)
axes[0].grid(False)
axes[1].imshow(t2_signs, cmap="coolwarm", vmin=-1, vmax=1)
for i in range(8):
    for j in range(8):
        axes[1].text(j, i, f"{int(t2_signs[i, j]):+d}", ha="center", va="center",
                     fontsize=8, color="white")
axes[1].set_xticks(range(8), [f"$x_{a}$" for a in range(1, 9)])
axes[1].set_yticks(range(8), [f"$x_{a}$" for a in range(1, 9)])
axes[1].set_title("sign of the mirror image's $T_{\\mu\\nu}$", fontsize=10)
axes[1].grid(False)
```

Two panels of different widths (`width_ratios`). The left one draws `grid` in shades of green, with the sign choices as three-line column labels (`\n` starts a new line); the right one draws the signs with their values written in the cells.

```python
save_figure(fig, "mirror_candidates",
            "Theorem T2 in the author's metric. Left: for four candidate matrices "
            "$P$ (rows), the eight possible relations between the Lagrangian of "
            "the mirror image on the mirror patch and the Lagrangian of $\\Psi$ on "
            "the patch (columns: overall sign $\\sigma$, sign of $m$, sign of "
            "$\\lambda$); a green square marks the relation that holds exactly. "
            "$P = 1$ and $P = \\Gamma$ give none; $P = \\gamma^{(x_8)}$ gives "
            "$+\\mathcal{L}_{-m,\\lambda}$, theorem T2; $P = \\Gamma\\gamma^{(x_8)}$ "
            "gives $-\\mathcal{L}_{m,-\\lambda}$. Right: the sign of each component "
            "of the mirror image's $T_{\\mu\\nu}$ relative to that of the "
            "$(-m, \\lambda)$ field, $+1$ except the mixed components with one "
            "$x_8$ index: the energy density is equal, not opposite.")
```

**What you see in Figure 18b.5:** on the left, the rows of $1$ and $\Gamma$ are empty, the row of $\gamma^{(x_8)}$ has its green square under $+\mathcal{L}$, $-m$, $+\lambda$, and the row of $P_8$ under $-\mathcal{L}$, $+m$, $-\lambda$; on the right, $+1$ everywhere except the 14 cells of the row and the column $x_8$ off the diagonal (the seven mixed components with one index $x_8$, drawn twice), where the sign is $-1$. The energy density ($T_{x_4x_4}$, sign $+1$) of the mirror partner is EQUAL to that of the field it mirrors.

**In [20], the last check.**

```python
figure_names = ["connection_history", "lagrangian_cancellation", "emt_signs",
                "mirror_metric", "mirror_candidates"]
paths = [output_file(f"{FIGURE_FOLDER}/18b_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths),
      "every figure file of this notebook exists")
all_checks_passed()
```

The five figure files must exist; the last line is ALL 20 CHECKS PASSED (notebook 18b).

**What Notebook 18b established.** PROVED, as exact identities in the 288 jet values, for an arbitrary history $a_4(x_4)$ and for both statistics: the canonical connection and $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$; T1 in the author's metric (Lagrangian, field equations derived from the Lagrangian, all 36 components of $T$, all 8 of $J$, the pair totals, the negative controls), for a general cubic potential and in a random general field; T2 across the mirror, with the search that singles out $\gamma^{(x_8)}$. ASSUMED: the gluing at the degenerate brane. NOT shown: any process that creates a universe; the identities map solutions to solutions.

### 18.21 A family of exact solutions: the fields that depend only on the time

The theorems speak about every solution. To SEE them at work we need actual solutions, and the field equation of the author's metric has a family of exact ones: the **homogeneous** fields, which depend on the time $x_4$ only. We derive them line by line for the commuting field dirac16complex00, whose components are ordinary complex numbers (the Revision record also gives the Grassmann version).

**The field equation becomes an ordinary differential equation.** For $\Psi = \Psi(x_4)$ every derivative except $\partial_4$ vanishes, and $\gamma^{x_4} = \gamma^{(x_4)}/f_4 = \gamma^{(x_4)}$. The spin connection still acts, through $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ (Section 18.3). With $V = m + \lambda S$ the field equation of Section 18.4 is therefore

$$
\gamma^{(x_4)}\frac{d\Psi}{dx_4} + 3H\gamma^{(x_8)}\Psi = V\Psi .
$$

Subtract $3H\gamma^{(x_8)}\Psi$ and multiply on the left by $-\gamma^{(x_4)}$; since $\gamma^{(x_4)}\gamma^{(x_4)} = \eta_{44} = -1$, the left side becomes $d\Psi/dx_4$:

$$
\frac{d\Psi}{dx_4} = M\Psi,\qquad M = -\gamma^{(x_4)}\big(V - 3H\gamma^{(x_8)}\big) = -V\gamma^{(x_4)} + 3H\gamma^{(x_4)}\gamma^{(x_8)} .
$$

**$S$ is constant.** $M$ is real ($V$ is real because $S = \Psi^\dagger C\Psi$ is real for a real symmetric $C$, and the gammas are real), so $M^\dagger = M^T$. By the product rule,

$$
\frac{dS}{dx_4} = \Big(\frac{d\Psi}{dx_4}\Big)^\dagger C\Psi + \Psi^\dagger C\frac{d\Psi}{dx_4} = \Psi^\dagger\big(M^TC + CM\big)\Psi .
$$

Now $(\gamma^{(x_4)})^T = -\gamma^{(x_4)}$ and $(\gamma^{(x_8)})^T = \gamma^{(x_8)}$, and from $C\gamma^{(a)}C^{-1} = -(\gamma^{(a)})^T$: $C$ commutes with $\gamma^{(x_4)}$ and anticommutes with $\gamma^{(x_8)}$. Hence

$$
M^T = V\gamma^{(x_4)} + 3H(\gamma^{(x_8)})^T(\gamma^{(x_4)})^T = V\gamma^{(x_4)} - 3H\gamma^{(x_8)}\gamma^{(x_4)} = V\gamma^{(x_4)} + 3H\gamma^{(x_4)}\gamma^{(x_8)} .
$$

The transpose of a product reverses the order; then the two transpose rules; then $\gamma^{(x_8)}\gamma^{(x_4)} = -\gamma^{(x_4)}\gamma^{(x_8)}$.

$$
M^TC + CM = VC\gamma^{(x_4)} - 3HC\gamma^{(x_4)}\gamma^{(x_8)} - VC\gamma^{(x_4)} + 3HC\gamma^{(x_4)}\gamma^{(x_8)} = 0 .
$$

We moved $C$ to the left in $M^TC$: past $\gamma^{(x_4)}$ without a sign and past $\gamma^{(x_8)}$ with a sign. So $dS/dx_4 = 0$: $S$ keeps its initial value $S_0$, and $V = m + \lambda S_0$ and $M$ are constant along the solution (`python-field-theory.json`, check `exact_nonlinear_homogeneous_solution`).

**The square of $M$.** Move the second $\gamma^{(x_4)}$ to the left through $(V - 3H\gamma^{(x_8)})$, which turns it into $(V + 3H\gamma^{(x_8)})$:

$$
M^2 = \gamma^{(x_4)}\big(V - 3H\gamma^{(x_8)}\big)\gamma^{(x_4)}\big(V - 3H\gamma^{(x_8)}\big) = \gamma^{(x_4)}\gamma^{(x_4)}\big(V + 3H\gamma^{(x_8)}\big)\big(V - 3H\gamma^{(x_8)}\big) = -(V^2 - 9H^2) .
$$

The two signs in front of $\gamma^{(x_4)}$ cancel; then $\gamma^{(x_4)}\gamma^{(x_4)} = -1$ and $(\gamma^{(x_8)})^2 = 1$ in the product of the brackets. So $M^2 = (9H^2 - V^2)I_{16}$.

**The exact solution.** When $V^2 > 9H^2$ put $w = \sqrt{V^2 - 9H^2}$, so that $M^2 = -w^2$. Then

$$
\Psi(x_4) = \cos(wx_4)\,\Psi(0) + \frac{\sin(wx_4)}{w}\,M\Psi(0) .
$$

Check: the derivative is $-w\sin(wx_4)\Psi(0) + \cos(wx_4)M\Psi(0)$, and $M\Psi(x_4) = \cos(wx_4)M\Psi(0) + \frac{\sin(wx_4)}{w}M^2\Psi(0)$ is the same, because $M^2 = -w^2$. At $x_4 = 0$ the formula gives $\Psi(0)$. The solution **oscillates** with the frequency $w$. When $V^2 < 9H^2$, cosine and sine become cosh and sinh and the solution **grows** exponentially: inside the window $|m + \lambda S_0| < 3H$ these modes are not oscillations but growth (`python-scope.json`, check `good_sector_x8_independent_modes_without_boundary_condition`; Chapter 8). PROVED: `python-field-theory.json`, check `exact_nonlinear_homogeneous_solution`; `wolfram-field-theory.json`, check `exact_solution_nonlinear_homogeneous_C`. The history $a_4$ does not enter $M$, but it enters the energy-momentum tensor through the vielbein factors $e^{\pm a_4}$ and through the spin connection (Notebook 18c, Figure 18c.3).

**What the theory record says about these solutions.** For homogeneous solutions, on shell, the energy density is $\rho = mS + \frac{\lambda}{2}S^2$, every pressure (3-space, extra times, hidden direction) is $p = \frac{\lambda}{2}S^2$, and the mixed component $T_{x_4x_8}$ vanishes (`python-field-theory.json`, checks `commuting_homogeneous_on_shell_rho_p` and `commuting_T_x4x8_homogeneous`). The charge density $J^{x_4} = \Psi^\dagger B\Psi$ is NOT constant: the conservation law $\partial_4J^{x_4} + \frac{1}{\sqrt{|g|}}\partial_8(\sqrt{|g|}J^{x_8}) = 0$ holds with a flow along the hidden direction. For a homogeneous field $J^{x_8} = -i\bar\Psi\gamma^{(x_8)}\Psi/f_8 = \tan z\,Q$ with $Q = -i\bar\Psi\gamma^{(x_8)}\Psi$, and $\sqrt{|g|}J^{x_8} = \cos z\tan z\,Q = \sin z\,Q$, so

$$
\frac{1}{\sqrt{|g|}}\partial_8\big(\sqrt{|g|}J^{x_8}\big) = \frac{6H\cos z\,Q}{\cos z} = 6HQ,\qquad \frac{dJ^{x_4}}{dx_4} = -6HQ .
$$

The derivative $\partial_8 = 6H\,d/dz$ acts only on $\sin z$, because $Q$ does not depend on $x_8$. Notebook 18c checks this law along its solution (`python-field-theory.json`, check `commuting_current_conservation`).

**What T1 and T2 predict for this family.** T1: if $\Psi$ solves the equation with $(m, \lambda)$, then $\Gamma\Psi$ solves it with $(-m, -\lambda)$. Directly: $\Gamma$ anticommutes with $\gamma^{(x_4)}$ and commutes with $\gamma^{(x_4)}\gamma^{(x_8)}$, and $S[\Gamma\Psi] = S$, so $\Gamma M_{m,\lambda}\Gamma = +V\gamma^{(x_4)} + 3H\gamma^{(x_4)}\gamma^{(x_8)} = M_{-m,-\lambda}$: the partner's generator is the similar matrix $\Gamma M\Gamma$, with the same eigenvalues. T2: on the mirror patch the connection term is $-3H\gamma^{(x_8)}$ (Section 18.16), so the equation there has $M^{\rm mirror} = -V\gamma^{(x_4)} - 3H\gamma^{(x_4)}\gamma^{(x_8)}$; with $S[\gamma^{(x_8)}\Psi] = -S$ and the parameters $(-m, \lambda)$, $V \to -m - \lambda S = -V$, and $\gamma^{(x_8)}M_{m,\lambda}\gamma^{(x_8)} = V\gamma^{(x_4)} - 3H\gamma^{(x_4)}\gamma^{(x_8)}$, which is exactly $M^{\rm mirror}_{-m,\lambda}$. So $\gamma^{(x_8)}\Psi$ solves the mirror equation with $(-m, \lambda)$. (We used $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_8)} = -\gamma^{(x_4)}$ and $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_8)} = -\gamma^{(x_4)}\gamma^{(x_8)}$.) Notebook 18c checks both by solving the partner equations independently.

### 18.22 The quantum reading Q

**From fields to quantum fields, in one paragraph.** Chapter 10 quantised dirac16complex canonically, with $x_4$ as the time. The recipe reads off the term of the Lagrangian that contains the time derivative. With $\gamma^{x_4} = \gamma^{(x_4)}$ and $C\gamma^{(x_4)} = iB$ (Notebook 18a, In [5]), the time-derivative part of $K$ is

$$
\frac12\big(\Psi^\dagger C\gamma^{(x_4)}\partial_4\Psi - \partial_4\Psi^\dagger C\gamma^{(x_4)}\Psi\big) = \frac{i}{2}\big(\Psi^\dagger B\partial_4\Psi - \partial_4\Psi^\dagger B\Psi\big) ,
$$

so the Lagrangian contains $\frac{i}{2}\sqrt{|g|}\,\Psi^\dagger N\partial_4\Psi$ (plus its partner term) with the **velocity kernel** $N = B$. The canonical rule then fixes the anticommutator of the field operators on a slice $x_4 = \mathrm{const}$: the momentum is $\pi = i\sqrt{|g|}\Psi^\dagger N$, and $\{\Psi_A(x), \pi_B(y)\} = i\delta_{AB}\delta^7(x - y)$ forces

$$
\{\Psi_A(x), \Psi^\dagger_B(y)\} = (N^{-1})_{AB}\,\frac{\delta^7(x - y)}{\sqrt{|g|}} = B_{AB}\,\frac{\delta^7(x - y)}{\sqrt{|g|}} ,
$$

because $N^{-1} = B^{-1} = B$ ($BB = 1$). Here $\{X, Y\} = XY + YX$ is the anticommutator of two operators and $\delta^7$ the delta function of the seven coordinates other than $x_4$. Because $B$ has eight eigenvalues $+1$ and eight $-1$, the state space carries an indefinite **Krein** form when $\Psi^\dagger$ is read as the ordinary adjoint (Chapter 10).

| statement | status | where it is verified |
| --- | --- | --- |
| the canonical anticommutator is $B\,\delta^7/\sqrt{\lvert g\rvert}$ | PROVED | `python-field-theory.json`, check `canonical_anticommutator_B`; `python-pairing.json`, check `Q.canonical_anticommutator` |

**One-particle waves.** In flat 4+4 space ($H = 0$, $a_4$ constant, all $f_\mu = 1$) and for $\lambda = 0$, a plane wave $\Psi = u\,e^{-iwx_4 + i\sum_{a\neq4}k_ax_a}$ turns the field equation $\sum_a\gamma^{(a)}\partial_a\Psi = m\Psi$ into $-iw\gamma^{(x_4)}u + i\sum_{a\neq4}k_a\gamma^{(a)}u = mu$. Multiply on the left by $-i\gamma^{(x_4)}$ and use $\gamma^{(x_4)}\gamma^{(x_4)} = -1$:

$$
wu = h_m(k)u,\qquad h_m(k) = -im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_{a\neq x_4}k_a\gamma^{(a)} .
$$

The frequencies $w$ are the eigenvalues of the **one-particle matrix** $h_m(k)$. Its square: write $h = -\gamma^{(x_4)}(im + K)$ with $K = \sum_{a\neq4}k_a\gamma^{(a)}$; moving $\gamma^{(x_4)}$ through $(im + K)$ turns it into $(im - K)$, so

$$
\begin{aligned}
h^2 &= \gamma^{(x_4)}\gamma^{(x_4)}(im - K)(im + K) = -(-m^2 - K^2) = m^2 + K^2 \\
&= \big(m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2\big)I_{16} .
\end{aligned}
$$

$K^2 = \sum_ak_a^2\eta_{aa}$ by the Clifford relation (the mixed products cancel in pairs). So $h^2 = w^2I_{16}$ with $w^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$: real frequencies when $w^2 > 0$; imaginary ones, growing modes, when the extra-time momentum is large enough to make $w^2 < 0$.

**Hypotheses.**

- (HQ1) dirac16complex is canonically quantised with $x_4$ as the evolution time and the anticommutator fixed by the velocity kernel of its Lagrangian, as above.
- (HQ2) dirac16complex00 is a classical field and has no quantum reading.

**The statements.**

- (Q1) The chirality image $\chi = \Gamma\Psi$ carries the Krein matrix $-B$: $\{\chi_A, \chi_B^\dagger\} = -B_{AB}\,\delta^7/\sqrt{|g|}$. This is also the anticommutator demanded by its own Lagrangian $\mathcal{L}_{m,\lambda}[\Gamma\chi] = -\mathcal{L}_{-m,-\lambda}[\chi]$.
- (Q2) The image's own generators (energy, momentum and charge from its own Lagrangian) coincide with those of $\Psi$: the pair $\Psi$, $\Gamma\Psi$ is ONE quantum system, and the T1 identity $T^{(-m,-\lambda)}[\Gamma\Psi] = -T^{(m,\lambda)}[\Psi]$ is an identity between operators of that one system.
- (Q3) An independently quantised universe with $(-m, -\lambda)$ has the anticommutator $+B$ (from its own Lagrangian $\mathcal{L}_{-m,-\lambda}$), its own vacuum and its own generators. It cannot be identified with $\Gamma\Psi$. On the product state space the generators of two independent universes add, $P_{\rm total} = P_1\otimes1 + 1\otimes P_2$, and no cancellation $P_1 + P_2 = 0$ follows.
- (Q4) The one-particle matrices satisfy $\Gamma h_m(k)\Gamma = h_{-m}(k)$ and $\gamma^{(x_8)}h_m(k)\gamma^{(x_8)} = h_{-m}(R_8k)$ ($R_8k$: the momentum with $k_8$ reversed): the $+m$ and $-m$ one-particle spectra are IDENTICAL, not opposite. For every real frequency each of the two eigenspaces (for $+w$ and for $-w$) has dimension 8 and Krein inertia (4,4), for $+m$ and $-m$ alike; for imaginary or zero frequency the eigenspaces are Krein-neutral ($B$ vanishes on them). The same similarity holds in a general field at a point, with frozen coefficients.
- (Q5) The T2 image $\gamma^{(x_8)}\Psi$ keeps the anticommutator $+B$: the mirror $(-m, \lambda)$ universe is an ordinary, independently quantisable copy with equal energies.

Status: PROVED under (HQ1). Records: `wolfram-pairing.json`, the 12 checks of the Q group (names beginning with `Q_`); `python-pairing.json`, the 10 checks whose names begin with `Q.`; theorem Q of `pairing-theory.json`. Notebook 18a checks the Krein signs (In [17], In [18]); Notebook 18c checks Q4 and Q5 on plane waves (In [16] to In [20]). Chapter 10 treats the same quantum reading in its own Notebook 10g.

### 18.23 The proofs of Q1 to Q5

**Q1.** The field operators of the image are $\chi_A = \sum_C\Gamma_{AC}\Psi_C$ and $\chi^\dagger_B = \sum_D\Psi^\dagger_D\Gamma_{BD}$ ($\Gamma$ is real). The anticommutator is linear in each argument, so

$$
\{\chi_A, \chi_B^\dagger\} = \sum_{C,D}\Gamma_{AC}\{\Psi_C, \Psi_D^\dagger\}\Gamma_{BD} = \sum_{C,D}\Gamma_{AC}B_{CD}\Gamma_{DB}\,\frac{\delta^7}{\sqrt{|g|}} = (\Gamma B\Gamma)_{AB}\,\frac{\delta^7}{\sqrt{|g|}} = -B_{AB}\,\frac{\delta^7}{\sqrt{|g|}} .
$$

We used $\Gamma_{BD} = \Gamma_{DB}$ ($\Gamma$ symmetric) and Lemma 2, $\Gamma B\Gamma = -B$. For the image's own Lagrangian: written in terms of $\chi$, the Lagrangian of the theory is $\mathcal{L}_{m,\lambda}[\Psi] = \mathcal{L}_{m,\lambda}[\Gamma\chi]$; its velocity term is $\frac{i}{2}\sqrt{|g|}\,\chi^\dagger\Gamma B\Gamma\partial_4\chi = \frac{i}{2}\sqrt{|g|}\,\chi^\dagger(-B)\partial_4\chi$, so its velocity kernel is $N = -B$ and the canonical rule gives the anticommutator $N^{-1} = -B$. The two agree.

**Q2.** The image's own Lagrangian, evaluated at $\chi = \Gamma\Psi$, is $\mathcal{L}_{m,\lambda}[\Gamma\Gamma\Psi] = \mathcal{L}_{m,\lambda}[\Psi]$: the same function of the same operators. Its energy density (the Legendre transform) and its Noether densities are therefore the same operators as those of $\Psi$. At the one-particle level: the energy of a plane wave is $\Psi^\dagger\mathcal{E}_m(k)\Psi$ with the **energy kernel** $\mathcal{E}_m(k) = Bh_m(k)$, and the evolution is $i\partial_4\Psi = (\text{anticommutator matrix})(\text{energy kernel})\Psi = B\mathcal{E}_m\Psi = h_m\Psi$. The image's own Lagrangian is $-\mathcal{L}_{-m,-\lambda}[\chi]$, so its anticommutator matrix is $-B$ (Q1) and its energy kernel is $-\mathcal{E}_{-m}$; its evolution generator is

$$
(-B)(-\mathcal{E}_{-m}) = B\mathcal{E}_{-m} = h_{-m} = \Gamma h_m\Gamma ,
$$

which is exactly how $\Gamma\Psi$ must evolve: $i\partial_4(\Gamma\Psi) = \Gamma h_m\Psi = (\Gamma h_m\Gamma)(\Gamma\Psi)$. The sign of the Krein matrix and the sign of the energy kernel compensate: the image is the same quantum system relabelled.

**Q3.** An independent universe $\chi_2$ with the Lagrangian $\mathcal{L}_{-m,-\lambda}[\chi_2]$ has the velocity kernel $+B$ and therefore $\{\chi_2, \chi_2^\dagger\} = +B\,\delta^7/\sqrt{|g|}$, while $\{\Gamma\Psi_1, (\Gamma\Psi_1)^\dagger\} = -B\,\delta^7/\sqrt{|g|}$. Since $B \neq -B$, $\chi_2 = \Gamma\Psi_1$ is impossible. Independence also requires $\{\Psi_1, \chi_2^\dagger\} = 0$, whereas $\{\Gamma\Psi_1, \Psi_1^\dagger\} = \Gamma B\,\delta^7/\sqrt{|g|}$ is a matrix of rank 16, not zero. On the product of the two state spaces the generators of the two systems add; the T1 identity relates operators of universe 1 only and gives no relation $P_2 = -P_1$. At zero momentum the one-particle generator of the two universes together has the eigenvalues $-m$ and $+m$, 16 times each, all nonzero for $m \neq 0$: nothing cancels.

**Q4.** $\Gamma\gamma^{(x_4)}\Gamma = -\gamma^{(x_4)}$ (one gamma) and $\Gamma\gamma^{(x_4)}\gamma^{(a)}\Gamma = \gamma^{(x_4)}\gamma^{(a)}$ (two gammas), so

$$
\Gamma h_m(k)\Gamma = +im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_{a\neq4}k_a\gamma^{(a)} = h_{-m}(k) .
$$

With $(\gamma^{(x_8)})^2 = 1$: $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_8)} = -\gamma^{(x_4)}$; for $a \neq 4, 8$, $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(a)}\gamma^{(x_8)} = \gamma^{(x_4)}\gamma^{(a)}$ (two exchanges); and $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_8)} = -\gamma^{(x_4)}\gamma^{(x_8)}$. So the mass term and the $k_8$ term change sign and the others do not: $\gamma^{(x_8)}h_m(k)\gamma^{(x_8)} = h_{-m}(R_8k)$. **Similar matrices have equal spectra**: if $hu = wu$, then $(MhM^{-1})(Mu) = w(Mu)$. So $+m$ and $-m$ have the same frequencies.

The Krein inertia, in three steps. (i) $Bh_m = h_m^\dagger B$; this follows from the reality of the gammas and the relations of $C$ with $\gamma^{(x_4)}$ and $\gamma^{(a)}$ (Exercise 18.5 asks you to verify it). For a real $w > 0$ the matrices $P_\pm = \frac12(1 \pm h/w)$ are the projectors onto the eigenspaces of $\pm w$ (because $h^2 = w^2$), and

$$
P_+^\dagger BP_- = \tfrac14\big(1 + h^\dagger/w\big)B\big(1 - h/w\big) = \tfrac14B\big(1 + h/w\big)\big(1 - h/w\big) = \tfrac14B\big(1 - h^2/w^2\big) = 0 .
$$

We moved $B$ to the left with $h^\dagger B = Bh$, then multiplied out; $h^2 = w^2$. So the two eigenspaces are $B$-orthogonal, and $B$ is nondegenerate on each (it is invertible on the whole space). (ii) Without extra-time momentum ($k_5 = k_6 = k_7 = 0$) $B$ commutes with $h$, and $\mathrm{tr}\,B = \mathrm{tr}(Bh) = 0$, so $\mathrm{tr}(BP_\pm) = 0$: on each 8-dimensional eigenspace $B$ is an involution with trace 0, which has four eigenvalues $+1$ and four $-1$, Krein inertia (4,4). (iii) The region $w^2 > 0$ is connected and contains the case without extra-time momentum (lowering $k_5, k_6, k_7$ to zero only increases $w^2$), and the projectors change continuously with $k$; a nondegenerate form cannot change its inertia continuously, so (4,4) holds at every real frequency. For an imaginary $w$: if $hu = wu$ and $hv = wv$, then $w\,u^\dagger Bv = u^\dagger Bhv = u^\dagger h^\dagger Bv = \bar w\,u^\dagger Bv$ ($\bar w$ the complex conjugate), so $(w - \bar w)u^\dagger Bv = 0$ and $u^\dagger Bv = 0$: the eigenspace is **Krein-neutral**. For $w = 0$, $h^2 = 0$ with rank 8 and the null space of $h$ equals its range, also $B$-neutral. The records are listed in the table at the end of this section. The recorded samples, all reproduced by Notebook 18c (In [16]):

| $m$ | momentum $(k_1, \dots, k_8)$ | $w$ | dimensions of the $+w$ and $-w$ eigenspaces | Krein inertia on $+w$ and on $-w$ |
| --- | --- | --- | --- | --- |
| $\pm2$ | (1, 2, 0, 0, 0, 0, 0, 4) | $5$ | 8 and 8 | (4,4) and (4,4) |
| $\pm3$ | (0, 0, 0, 0, 0, 0, 0, 0) | $3$ | 8 and 8 | (4,4) and (4,4) |
| $\pm1$ | (1, 0, 0, 0, 0, 0, 0, 0) | $\sqrt2$ | 8 and 8 | (4,4) and (4,4) |
| $\pm2$ | (0, 0, 0, 0, 1, 0, 0, 0) | $\sqrt3$ | 8 and 8 | (4,4) and (4,4) |

(Each row stands for the two recorded samples with $+m$ and $-m$; the entry $k_4$ is not used. The last row has an extra-time momentum and still a real frequency: $w^2 = 4 - 1 = 3$.)

**Q5.** Lemma 4 gives $\gamma^{(x_8)}B(\gamma^{(x_8)})^\dagger = +B$, so the anticommutator of $\gamma^{(x_8)}\Psi$ is $+B\,\delta^7/\sqrt{|g|}$, the same as that of an ordinary field. QED.

| statement | status | where it is verified |
| --- | --- | --- |
| Q1: the T1 image carries $-B$, also by its own Lagrangian | PROVED | `wolfram-pairing.json`, checks `Q_Krein_metric_of_images`, `Q_symplectic_kernel_commuting` and `Q_symplectic_kernel_grassmann`; `python-pairing.json`, checks `Q.image_krein_metric` and `Q.image_own_quantisation` |
| Q2: the image's own generators are those of $\Psi$ | PROVED | `wolfram-pairing.json`, checks `Q_generators_of_the_image_commuting` and `Q_generators_of_the_image_grassmann`; `python-pairing.json`, check `Q.image_generators_same_dynamics` |
| Q3: no identification and no cancellation of independent universes | PROVED | `wolfram-pairing.json`, check `Q_no_identification_of_independent_universes`; `python-pairing.json`, check `Q.no_cancellation_independent_universes` |
| Q4: the maps of $h_m$ and the dispersion $h^2 = w^2$ | PROVED | `wolfram-pairing.json`, checks `Q_one_particle_flat_dispersion`, `Q_one_particle_maps` and `Q_one_particle_general_field`; `python-pairing.json`, check `Q.one_particle_maps` |
| Q4: Krein inertia (4,4) at every real frequency | PROVED | `wolfram-pairing.json`, checks `Q_one_particle_Krein_signatures` and `Q_one_particle_Krein_inertia_real_frequencies`; `python-pairing.json`, checks `Q.one_particle_Krein_inertia` and `Q.one_particle_Krein_inertia_proof` |
| Q4: imaginary and zero frequencies are Krein-neutral | PROVED | `wolfram-pairing.json`, check `Q_one_particle_complex_and_zero_frequencies_Krein_neutral`; `python-pairing.json`, check `Q.one_particle_complex_frequency_Krein_neutral` |
| Q5: the T2 image keeps $+B$ | PROVED | `wolfram-pairing.json`, check `Q_Krein_metric_of_images`; `python-pairing.json`, check `Q.T2_image_keeps_B` |
| the eight samples of the table above | PROVED (exact arithmetic of the record); COMPUTED again in floating point by Notebook 18c | data table `one_particle_flat` of `pairing-theory.json`; Notebook 18c, In [16] |

**What Q does not say.** Q1 to Q5 are statements about the canonical anticommutator. They neither use nor establish a positive-norm state space for either universe. The theory record constructs, separately, a positive Fock representation in the good sector without extra-time momentum (Chapter 10); it is not used here. And the vanishing total energy-momentum and charge of a T1 pair holds for classical bilinears and as an operator identity within ONE quantum system; it does not hold for two independently quantised universes, whose generators add without cancelling.

### 18.24 Example: Notebook 18c sees the theorems in numbers

Notebook 18c takes one homogeneous solution of dirac16complex00 in the author's metric (Section 18.21), with values chosen as an ILLUSTRATION: units in which $m = 1$, $H = 0.2$, $\lambda = 0.3$, the hidden angle $z_0 = \pi/4$, and an initial value of 16 complex numbers drawn with the fixed seed 2026. Only the history $a_4 = AHx_4$ with $A = 1$ is read from the Revision record `Revision/kohn_sham/results/parameters.json`. The notebook solves the equation with the classical Runge-Kutta method of fourth order and checks it against the exact formula; solves the T1 partner equation $(-m, -\lambda)$ and the mirror equation $(-m, \lambda)$ INDEPENDENTLY and finds $\Gamma\Psi$ and $\gamma^{(x_8)}\Psi$; computes $S$, all 8 components of $J^\mu$ and all 36 of $T_{\mu\nu}$ along the deflating history; compares the spectra of the evolution matrices; and, for the quantum reading, reproduces the plane-wave samples of the pairing record and follows the Krein norms of single eigenvectors under $\Gamma$ and $\gamma^{(x_8)}$. Its last line is ALL 21 CHECKS PASSED (notebook 18c); it runs in about 30 seconds.

<!-- NOTEBOOK 18c -->

### 18.27 Line-by-line walk-through of Notebook 18c

The notebook has 21 code cells. **In [1]** is the set-up cell, word for word the set-up cell of Notebook 18a explained line by line in Section 18.9, except that its comment lines hold the run instructions of Section 18.25 and its line `NOTEBOOK_ID = "18c"` names this notebook, so its figures are saved as `18c_<k>_<name>.png` and their captions in `18c.captions.json`. It prints one line, Set-up of notebook 18c complete: repository folder found, helpers defined.

The idea of the notebook in one paragraph. Notebooks 18a and 18b computed with exact numbers: whole numbers, fractions and symbols. This notebook computes with **floating-point numbers**, the ordinary numbers of a computer, which carry about 16 significant decimal digits and are rounded after every operation. So an identity such as $\Phi = \Gamma\Psi$ is checked by requiring the largest difference to be smaller than a **tolerance**, usually $10^{-12}$: far below the size of the quantities compared (about 0.1 to 3) and far above the rounding errors (about $10^{-16}$). The notebook takes one solution of the homogeneous family of Section 18.21, computes it in two independent ways (step by step with the Runge-Kutta method, and from the exact formula), then solves the two partner equations of T1 and T2 on their own, and compares the solutions and all their bilinears along the deflating history.

**In [2], the records and the matrices.**

```python
import numpy as np  # arrays, matrices, eigenvalues
import sympy as sp  # exact symbolic algebra for the spin connection

GAMMAS = "Revision/algebra/gammas.json"
PY = "Revision/pairing/reports/python-pairing.json"
WL = "Revision/pairing/reports/wolfram-pairing.json"
THEORY = "Revision/pairing/pairing-theory.json"
TH_PY = "Revision/theory/reports/python-field-theory.json"
TH_WL = "Revision/theory/reports/wolfram-field-theory.json"
SCOPE = "Revision/theory/reports/python-scope.json"
PARAMETERS = "Revision/kohn_sham/results/parameters.json"
```

numpy (`np`) is the package for arrays of floating-point numbers: matrix products, eigenvalues, the singular value decomposition. sympy (`sp`) is used once more, in In [3], to compute the spin connection exactly before it is turned into numbers. The eight constants are the repository paths of the eight Revision records the notebook reads: the gammas; the two reports of the pairing verifiers and the pairing theory record (for the plane-wave samples of the quantum reading); the two field-theory reports and the scope report (for the exact homogeneous solution and the conservation of the charge); and the Kohn-Sham parameter record, which holds the canonical deflating history.

```python
def read_json(relative):
    """Read a JSON file of the repository (a Revision record)."""
    return json.loads(repository_file(relative).read_text(encoding="utf-8"))


RECORDS = {f: read_json(f) for f in (PY, WL, TH_PY, TH_WL, SCOPE)}


def recorded(report_file, name):
    """The recorded entry (verdict and detail) of the check name of a report."""
    for entry in RECORDS[report_file]["checks"]:
        if entry["name"] == name:
            return entry
    return {"verdict": "MISSING", "detail": ""}


def reproduces(condition, name, *sources):
    """check(condition, name), which also requires every named check of every
    source (report_file, [check names]) to have the recorded verdict PASS."""
    ok = all(recorded(f, n)["verdict"].upper() == "PASS"
             for f, names in sources for n in names)
    text = "; ".join(f"{f}, check {', '.join(names)}" for f, names in sources)
    check(condition and ok, name, record=text)
```

The record helpers of Notebook 18b. `read_json` reads a record. `RECORDS` reads the five reports once, with the file name as the key (a dictionary comprehension). `recorded(report_file, name)` returns the entry of a named check, or a placeholder with the verdict MISSING. `reproduces` passes only when the notebook's own result holds AND every named check has the recorded verdict PASS; `.upper()` makes the comparison independent of capitalisation, which matters here, because the field-theory report writes its verdicts as pass in small letters.

```python
fixture = read_json(GAMMAS)
gamma = {a: np.array(fixture["gamma"][a - 1], dtype=float) for a in range(1, 9)}
ETA = {a: int(fixture["eta"][a - 1]) for a in range(1, 9)}
I16 = np.eye(16)
C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]
Gamma = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3] @ gamma[4] @ gamma[5] @ gamma[6] \
    @ gamma[7]
B = -1j * C @ gamma[4]  # the Krein matrix
check(all(np.array_equal(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                         2.0 * (ETA[a] if a == b else 0) * I16)
          for a in range(1, 9) for b in range(1, 9))
      and np.array_equal(Gamma, np.diag([-1.0] * 8 + [1.0] * 8))
      and np.array_equal(B.conj().T, B),
      "eight real 16 x 16 gammas (Clifford relations), Gamma = diag(-I8, I8), "
      "B Hermitian")
```

The gammas are read as numpy arrays of floating-point numbers (`dtype=float`). Their entries are $-1$, 0 and $+1$, which floating-point numbers store exactly, and sums and products of such whole numbers are again exact; so `np.array_equal`, an exact comparison, is still correct for them. `C`, `Gamma` and `B` are built as in Section 18.5 (a backslash at the end of a line continues the statement on the next line; `1j` is $i$). The check confirms the 64 Clifford relations, $\Gamma = \mathrm{diag}(-I_8, I_8)$ and $B^\dagger = B$ (`.conj().T` is the conjugate transpose). Out [2] shows one PASS line.

**In [3], the spin connection on the patch and on the mirror patch.**

```python
x4, z, H_sym = sp.symbols("x4 z H", real=True)
a4 = sp.Function("a4")(x4)
a4p = sp.Symbol("a4p")


def d(expr, b):
    """The derivative of a coefficient along the coordinate x_b (z = 6 H x8)."""
    if b == 4:
        return sp.diff(expr, x4)
    if b == 8:
        return 6 * H_sym * sp.diff(expr, z)
    return sp.Integer(0)
```

As in Notebook 18b: the symbols $x_4$, $z$ and $H$ (here named `H_sym`, because from In [4] on the name `H` holds the number 0.2), the unknown history $a_4(x_4)$, the plain symbol `a4p` for $a_4'$, and the derivative `d(expr, b)` along the coordinate $x_b$: $d/dx_4$ along $x_4$, $6H\,d/dz$ along $x_8$ (because $z = 6Hx_8$), and zero along the six coordinates on which no coefficient depends.

```python
def factors(s8):
    s6 = sp.sin(z) ** sp.Rational(1, 6)
    f = {a: sp.exp(a4) * s6 for a in (1, 2, 3)}
    f.update({a: sp.exp(-a4) * s6 for a in (5, 6, 7)})
    f.update({4: sp.Integer(1), 8: s8 * sp.cot(z)})
    return f
```

`factors(s8)` returns the eight vielbein factors of Section 18.3: $e^{a_4}\sin^{1/6}z$ for $x_1, x_2, x_3$; $e^{-a_4}\sin^{1/6}z$ for the deflating extra times $x_5, x_6, x_7$; 1 for $x_4$; and $s_8\cot z$ for $x_8$, with $s_8 = +1$ on the patch and $s_8 = -1$ on the mirror patch, where $\cot z < 0$, so that $f_8 > 0$ on both. `f.update({...})` adds entries to the dictionary.

```python
def connection(s8):
    """{(mu, a, b) with a < b: omega_mu ab} for the diagonal vielbein."""
    f, om = factors(s8), {}
    for a in range(1, 9):
        for b in range(1, 9):
            if a != b:
                value = sp.simplify(ETA[a] * d(f[a], b) / f[b])
                if value != 0:  # omega_a,ab (or -omega_a,ba when b < a)
                    om[(a, a, b) if a < b else (a, b, a)] = (
                        value if a < b else -value)
    return dict(sorted(om.items()))
```

`connection(s8)` uses the short formula derived in Section 18.3, $\omega_{a,ab} = \eta_{aa}\,\partial_bf_a/f_b$ for $a \neq b$, instead of the general Christoffel computation of Notebook 18b. Each nonzero value is stored under the key $(\mu, a, b)$ with $a < b$, the format of the record: when $a < b$ the value is $\omega_{a,ab}$ itself, stored under $(a, a, b)$; when $b < a$ the component with the smaller index first is $\omega_{a,ba} = -\omega_{a,ab}$, stored under $(a, b, a)$. `dict(sorted(...))` orders the keys, so that the list is printed in the order of the record.

```python
def short(expr):
    expr = sp.simplify(expr).subs(sp.Derivative(a4, x4), a4p)
    return expr.subs(a4, sp.Symbol("a4"))


patch_om, mirror_om = connection(1), connection(-1)
listing = "; ".join(f"omega_x{mu} x{a}x{b} = {short(v)}"
                    for (mu, a, b), v in patch_om.items())
say("patch: " + listing)
same = recorded(PY, "geometry.spin_connection_components")["detail"] == (
    "nonzero components (a < b): " + listing)
reproduces(len(patch_om) == 12 and same,
           "the formula gives the 12 recorded spin connection components",
           (PY, ["geometry.spin_connection_components"]))
```

`short` writes $a_4'$ as `a4p` and $a_4(x_4)$ as `a4`, as in Notebook 18b. The twelve components of the patch are printed in one line (the output wraps it) and compared, character for character, with the detail text of the sympy check `geometry.spin_connection_components`; the check requires 12 components and the agreement. So two different computations, the general Christoffel formula of Notebook 18b and the short formula of this cell, reproduce the same record.

```python
flips = all(sp.simplify(mirror_om[k] + patch_om[k]) == 0 if 8 in k[1:]
            else sp.simplify(mirror_om[k] - patch_om[k]) == 0 for k in patch_om)
```

`flips` compares the two patches component by component: the six components with an index $x_8$ (`8 in k[1:]` looks at the two frame indices of the key) must change sign, because they contain $1/f_8$, and the six others must be equal.

```python
divergence = {}
for s8 in (1, -1):
    f = factors(s8)
    sqrtg = sp.simplify(sp.Mul(*f.values()))
    divergence[s8] = {mu: sp.simplify(d(sqrtg / f[mu], mu) / (2 * sqrtg))
                      for mu in range(1, 9)}
say(f"divergence form, patch: coefficient of gamma^(x8) = {divergence[1][8]}, of "
    f"gamma^(x4) = {divergence[1][4]}; mirror patch: {divergence[-1][8]}, "
    f"{divergence[-1][4]}")
reproduces(flips and divergence[1][8] == 3 * H_sym and divergence[-1][8] == -3 * H_sym
           and all(divergence[s][mu] == 0 for s in (1, -1) for mu in range(1, 8)),
           "gamma^mu Omega_mu = +3 H gamma^(x8) (patch), -3 H gamma^(x8) (mirror)",
           (TH_PY, ["gamma_mu_Omega_mu_equals_3H_gamma_x8",
                    "divergence_of_sqrtg_gamma"]),
           (TH_WL, ["gammaOmega_equals_3H_gamma_x8", "gammaOmega_divergence_form"]))
```

The **divergence form** of the theory record, $\gamma^\mu\Omega_\mu = \frac{1}{2\sqrt{|g|}}\sum_\mu\partial_\mu\big(\sqrt{|g|}\,\gamma^{(\mu)}/f_\mu\big)$, computed on both patches: `divergence[s8][mu]` is the coefficient of $\gamma^{(\mu)}$, $\partial_\mu(\sqrt{|g|}/f_\mu)/(2\sqrt{|g|})$. Why this formula holds for a diagonal vielbein, line by line. Only the components $\omega_{\mu,\mu b}$ (and their partners $\omega_{\mu,b\mu} = -\omega_{\mu,\mu b}$) are nonzero (Section 18.3), so

$$
\gamma^\mu\Omega_\mu = \sum_\mu\frac{\gamma^{(\mu)}}{f_\mu}\sum_{b\neq\mu}\omega_{\mu,\mu b}S^{\mu b} .
$$

The two equal terms $\omega_{\mu,\mu b}S^{\mu b}$ and $\omega_{\mu,b\mu}S^{b\mu}$ of $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$ cancel the factor $\frac12$, as in Section 18.3.

$$
\gamma^{(\mu)}S^{\mu b} = \tfrac12\gamma^{(\mu)}\gamma^{(\mu)}\gamma^{(b)} = \tfrac12\eta_{\mu\mu}\gamma^{(b)} .
$$

$S^{\mu b} = \frac12\gamma^{(\mu)}\gamma^{(b)}$ for $b \neq \mu$; then the Clifford relation $\gamma^{(\mu)}\gamma^{(\mu)} = \eta_{\mu\mu}$.

$$
\gamma^\mu\Omega_\mu = \sum_b\gamma^{(b)}\sum_{\mu\neq b}\frac{\eta_{\mu\mu}}{2f_\mu}\,\eta_{\mu\mu}\frac{\partial_bf_\mu}{f_b} = \sum_b\frac{\gamma^{(b)}}{2f_b}\sum_{\mu\neq b}\frac{\partial_bf_\mu}{f_\mu} .
$$

We inserted $\omega_{\mu,\mu b} = \eta_{\mu\mu}\partial_bf_\mu/f_b$, exchanged the order of the two sums, and used $\eta_{\mu\mu}^2 = 1$.

$$
\sum_{\mu\neq b}\frac{\partial_bf_\mu}{f_\mu} = \partial_b\ln\prod_{\mu\neq b}f_\mu = \partial_b\ln\frac{\sqrt{|g|}}{f_b},\qquad \frac{1}{2f_b}\,\partial_b\ln\frac{\sqrt{|g|}}{f_b} = \frac{1}{2\sqrt{|g|}}\,\partial_b\frac{\sqrt{|g|}}{f_b} .
$$

The first equation is the rule $\partial\ln F = \partial F/F$ applied to each factor (the logarithm of a product is the sum of the logarithms), with $\sqrt{|g|} = \prod_\mu f_\mu$; the second is the same rule read backwards, with $F = \sqrt{|g|}/f_b$ and $\frac{1}{f_b}\cdot\frac{f_b}{\sqrt{|g|}} = \frac{1}{\sqrt{|g|}}$. Together they give the divergence form. On the patch, $\sqrt{|g|}/f_8 = \cos z/\cot z = \sin z$ and $\partial_8\sin z = 6H\cos z$, so the coefficient of $\gamma^{(x_8)}$ is $6H\cos z/(2\cos z) = 3H$; $\sqrt{|g|}/f_4 = \cos z$ does not depend on $x_4$, so the coefficient of $\gamma^{(x_4)}$ is 0. On the mirror patch $\sqrt{|g|} = -\cos z$ and $f_8 = -\cot z$ give the same quotient $\sin z$, but it is divided by $2\sqrt{|g|} = -2\cos z$: the coefficient is $-3H$. The check requires the sign flips, the two coefficients $\pm3H$ and zero for the seven other directions, and names two checks of each field-theory report. Out [3] prints the twelve components, then 3*H, 0, -3*H, 0, and two PASS lines.

**In [4], the numbers of the illustration and the geometry as numbers.**

```python
A_hist = read_json(PARAMETERS)["physics"]["historyA"]  # A = 1
m, H, lam = 1.0, 0.2, 0.3  # an illustration (units m = 1)
Z0 = np.pi / 4  # the patch point; the mirror point is pi - Z0
rng = np.random.default_rng(2026)
raw = rng.normal(size=16) + 1j * rng.normal(size=16)
P_C = 0.5 * (I16 + C)  # the projector on the eigenvalue +1 of C
psi0 = 2.0 * P_C @ raw + 0.5 * (I16 - P_C) @ raw  # mostly in the +1 part: S > 0
psi0 = psi0 / np.linalg.norm(psi0)  # length 1
S0 = float((psi0.conj() @ C @ psi0).real)  # S of the initial value
report("S of the initial value", f"{S0:.6f}")
report("m + lambda S", f"{m + lam * S0:.6f}")
report("3 H", f"{3 * H:.6f}")
```

`A_hist` is the number $A = 1$ of the canonical history $a_4 = AHx_4$, read from the Kohn-Sham parameter record. The next two lines fix the ILLUSTRATION chosen by this notebook: $m = 1$ (so lengths and times are measured in units of $1/m$), $H = 0.2$, $\lambda = 0.3$ and the patch point $z_0 = \pi/4$. `np.random.default_rng(2026)` is a random-number generator with the fixed seed 2026; `raw` is a column of 16 complex numbers whose real and imaginary parts are drawn from the normal distribution. The initial value is built so that $S > 0$. Since $C$ is real and symmetric with $CC = 1$, the matrices $P_{C\pm} = \frac12(1 \pm C)$ are projectors: $P_{C\pm}^\dagger = P_{C\pm}$, $P_{C\pm}P_{C\pm} = P_{C\pm}$, $P_{C+}P_{C-} = \frac14(1 - CC) = 0$ and $P_{C+} - P_{C-} = C$. Hence

$$
S = \Psi^\dagger C\Psi = \Psi^\dagger P_{C+}\Psi - \Psi^\dagger P_{C-}\Psi = |P_{C+}\Psi|^2 - |P_{C-}\Psi|^2 ,
$$

where $|v|^2 = v^\dagger v$ is the squared length; the last step writes $\Psi^\dagger P_{C\pm}\Psi = \Psi^\dagger P_{C\pm}^\dagger P_{C\pm}\Psi = (P_{C\pm}\Psi)^\dagger(P_{C\pm}\Psi)$. Weighting the part of $P_{C+}$ by 2 and the part of $P_{C-}$ by 0.5 makes the first term larger. `np.linalg.norm` is the length of a column, and dividing by it gives a column of length 1. `S0` is $S$ of the initial value (`.real` drops the imaginary part, which is zero up to rounding because $C$ is real and symmetric). Out [4] prints $S = 0.897319$, $m + \lambda S = 1.269196$ and $3H = 0.600000$.

```python
S_AB = {(a, b): 0.5 * gamma[a] @ gamma[b] for a in range(1, 9) for b in range(1, 9)}
history = {sp.Derivative(a4, x4): A_hist * H_sym}  # a4' = A H


def numeric(table):
    """Turn the sympy components into functions of (x4, z) for this H and A."""
    out = {}
    for key, value in table.items():
        e = value.subs(history).subs(a4, A_hist * H_sym * x4).subs(H_sym, H)
        out[key] = sp.lambdify((x4, z), e, "numpy")
    return out


OMEGA = {1: numeric(patch_om), -1: numeric(mirror_om)}
FACTOR = {s8: {mu: sp.lambdify((x4, z), e.subs(a4, A_hist * H_sym * x4)
                               .subs(H_sym, H), "numpy")
               for mu, e in factors(s8).items()} for s8 in (1, -1)}
```

`S_AB` holds $S^{ab} = \frac12\gamma^{(a)}\gamma^{(b)}$ (correct for $a \neq b$; the entries with $a = b$ are never used). `history` replaces $a_4'$ by $AH$. `numeric(table)` turns each sympy component into a numpy function of $(x_4, z)$: it substitutes $a_4' = AH$, then $a_4 = AHx_4$ and $H = 0.2$, and `sp.lambdify` makes a function that evaluates the resulting expression for numbers. `OMEGA` holds these functions for both patches (keys 1 and $-1$), and `FACTOR` the eight vielbein factors of both patches as functions of $(x_4, z)$.

```python
def geometry_at(t, zv, s8):
    """Numbers at the time t and angle zv: f, g, gamma^mu, gamma_mu, Omega_mu."""
    f = {mu: float(FACTOR[s8][mu](t, zv)) for mu in range(1, 9)}
    Om = {mu: np.zeros((16, 16)) for mu in range(1, 9)}
    for (mu, a, b), fn in OMEGA[s8].items():
        Om[mu] = Om[mu] + float(fn(t, zv)) * S_AB[a, b]
    return {"f": f, "g": {mu: ETA[mu] * f[mu] ** 2 for mu in f},
            "sqrtg": abs(np.prod(list(f.values()))),
            "up": {mu: gamma[mu] / f[mu] for mu in f},
            "down": {mu: ETA[mu] * f[mu] * gamma[mu] for mu in f}, "Om": Om}
```

`geometry_at(t, zv, s8)` returns the numbers of the geometry at the time $x_4 = t$ and the angle $z$ = `zv`: the eight factors $f_\mu$ (`float` turns a numpy number into a Python number); the matrices $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$; the metric components $g_{\mu\mu} = \eta_{\mu\mu}f_\mu^2$; $\sqrt{|g|}$ (`abs` of the product of the factors); the curved gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ (key `"up"`) and $\gamma_\mu = \eta_{\mu\mu}f_\mu\gamma^{(\mu)}$ (key `"down"`).

```python
for s8, zv in ((1, Z0), (-1, np.pi - Z0)):
    geo = geometry_at(1.3, zv, s8)
    total = sum(geo["up"][mu] @ geo["Om"][mu] for mu in range(1, 9))
    assert np.allclose(total, 3 * s8 * H * gamma[8], atol=1e-12)
check(abs(m + lam * S0) > 3 * H,
      "|m + lambda S| > 3 H: the solution and both partners oscillate")
```

A numerical test of the matrices just built: at the time 1.3 on each patch, $\sum_\mu\gamma^\mu\Omega_\mu$ must equal $3s_8H\gamma^{(x_8)}$ entry by entry to $10^{-12}$ (`np.allclose`; `assert` stops the notebook if not). Then the check $|m + \lambda S| = 1.269 > 3H = 0.6$: by Section 18.21 the solution oscillates. The partners oscillate too, because their generators have the same eigenvalues (In [14]). Out [4] ends with this PASS line.

**In [5], the solution: Runge-Kutta against the exact formula.**

```python
X_END = 20.0  # integrate from x4 = 0 to 20 (a4 from 0 to A H 20 = 4)


def generator(psi, mass, coup, s8):
    """The matrix M of d psi/dx4 = M psi (s8 = +1 patch, -1 mirror patch)."""
    S = (psi.conj() @ C @ psi).real
    return -gamma[4] @ ((mass + coup * S) * I16 - 3 * s8 * H * gamma[8])
```

`X_END` is the end time 20. Along the history $a_4 = AHx_4$ with $AH = 0.2$, $a_4$ runs from 0 to 4, so between $x_4 = 0$ and 20 the extra times deflate by the factor $e^{-4} \approx 0.018$ and 3-space inflates by $e^4 \approx 54.6$. `generator(psi, mass, coup, s8)` returns the matrix $M = -\gamma^{(x_4)}\big((m + \lambda S)I_{16} - 3s_8H\gamma^{(x_8)}\big)$ of Section 18.21. $S$ is computed from the column `psi` itself, because the equation is nonlinear ($M$ depends on the field through $S$), and $s_8 = -1$ selects the mirror patch, where the connection term is $-3H\gamma^{(x_8)}$.

```python
def rk4(psi_start, mass, coup, s8, steps):
    """The RK4 solution at x4 = 0, h, 2h, ..., X_END (steps + 1 rows)."""
    h = X_END / steps
    out = np.empty((steps + 1, 16), dtype=complex)
    psi = psi_start.astype(complex)
    out[0] = psi
    for n in range(steps):
        k1 = generator(psi, mass, coup, s8) @ psi
        k2 = generator(psi + 0.5 * h * k1, mass, coup, s8) @ (psi + 0.5 * h * k1)
        k3 = generator(psi + 0.5 * h * k2, mass, coup, s8) @ (psi + 0.5 * h * k2)
        k4 = generator(psi + h * k3, mass, coup, s8) @ (psi + h * k3)
        psi = psi + h / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        out[n + 1] = psi
    return out
```

`rk4` is the **classical Runge-Kutta method of fourth order** (Chapter 2). With the step $h$ and $F(\Psi) = M(\Psi)\Psi$, one step from $\Psi_n$ at the time $x_4 = nh$ computes four slopes,

$$
k_1 = F(\Psi_n),\qquad k_2 = F\big(\Psi_n + \tfrac{h}{2}k_1\big),\qquad k_3 = F\big(\Psi_n + \tfrac{h}{2}k_2\big),\qquad k_4 = F(\Psi_n + hk_3),
$$

and moves on to $\Psi_{n+1} = \Psi_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$. `np.empty` reserves an array of `steps + 1` rows of 16 complex numbers; row $n$ receives $\Psi_n$. `astype(complex)` makes a complex copy of the start column.

```python
def exact(psi_start, mass, coup, s8, times):
    """The exact solution cos(w x4) psi(0) + sin(w x4)/w M psi(0)."""
    M = generator(psi_start, mass, coup, s8)
    S = (psi_start.conj() @ C @ psi_start).real
    w = np.sqrt((mass + coup * S) ** 2 - 9 * H ** 2)
    return (np.cos(w * times)[:, None] * psi_start[None, :]
            + (np.sin(w * times) / w)[:, None] * (M @ psi_start)[None, :])
```

`exact` evaluates the formula $\Psi(x_4) = \cos(wx_4)\Psi(0) + \frac{\sin(wx_4)}{w}M\Psi(0)$ with $w = \sqrt{(m + \lambda S)^2 - 9H^2}$ (Section 18.21) at many times at once: `[:, None]` makes a column of the time values and `[None, :]` a row of the components, and their product is the table with one row per time (numpy's **broadcasting**).

```python
STEPS = 2000
times = np.linspace(0.0, X_END, STEPS + 1)
psi = rk4(psi0, m, lam, 1, STEPS)  # the universe of mass m on the patch
S_t = np.einsum("ti,ij,tj->t", psi.conj(), C, psi).real
error = np.abs(psi - exact(psi0, m, lam, 1, times)).max()
M0 = generator(psi0, m, lam, 1)
square_ok = np.allclose(M0 @ M0, (9 * H ** 2 - (m + lam * S0) ** 2) * I16, atol=1e-13)
```

The solution with 2000 steps of length 0.01, at the 2001 times `times` (`np.linspace(0, 20, 2001)`). `S_t` is $S$ at every time: `np.einsum("ti,ij,tj->t", ...)` computes, for each time $t$, the sum $\sum_{i,j}\Psi^*_{ti}C_{ij}\Psi_{tj}$ (the letters say which indices are summed and which one is kept). `error` is the largest difference between the Runge-Kutta table and the exact one, over all times and components. `square_ok` checks $M^2 = (9H^2 - (m + \lambda S)^2)I_{16}$ numerically.

```python
errors = {}
for n in (250, 500, 1000, 2000, 4000):
    sol = rk4(psi0, m, lam, 1, n)
    errors[n] = float(np.abs(sol[-1] - exact(psi0, m, lam, 1, np.array([X_END]))[0])
                      .max())
orders = [np.log2(errors[n] / errors[2 * n]) for n in (250, 500, 1000, 2000)]
say("RK4 error at x4 = 20 for 250, 500, 1000, 2000, 4000 steps: "
    + ", ".join(f"{errors[n]:.1e}" for n in errors))
say("measured orders: " + ", ".join(f"{p:.2f}" for p in orders))
report("largest RK4 error with 2000 steps (all times, all components)",
       f"{error:.1e}")
```

The **order** of the method is measured. If the error at the end time behaves like $e(h) = ch^p$, halving the step gives $e(h/2) = ch^p/2^p$, so $e(h)/e(h/2) = 2^p$ and $p = \log_2\big(e(h)/e(h/2)\big)$. The loop solves with 250, 500, 1000, 2000 and 4000 steps and stores the error at $x_4 = 20$; `orders` holds the four values of $p$. Out [5] prints the errors 2.0e-05, 1.2e-06, 6.9e-08, 4.3e-09 and 2.6e-10 (2.0e-05 means $2.0 \times 10^{-5}$), the measured orders 4.10, 4.06, 4.03 and 4.01, and the largest error with 2000 steps over all times and components, 4.3e-09.

```python
reproduces(np.abs(S_t - S0).max() < 1e-9 and error < 1e-7 and square_ok,
           "S is constant and RK4 equals the exact homogeneous solution (2000 steps)",
           (TH_PY, ["exact_nonlinear_homogeneous_solution"]),
           (TH_WL, ["exact_solution_nonlinear_homogeneous_C"]),
           (SCOPE, ["good_sector_x8_independent_modes_without_boundary_condition"]))
check(all(3.8 < p < 4.2 for p in orders), "RK4 is of fourth order here")
```

The first check requires $S$ to stay constant to $10^{-9}$, the error to be below $10^{-7}$, and the square of $M$; it names the exact homogeneous solution of the two field-theory reports and the scope report's check on these modes. The second requires every measured order between 3.8 and 4.2. COMPUTED: the Runge-Kutta solution agrees with the exact formula of the record to $4.3 \times 10^{-9}$, and the method is of fourth order.

**In [6], Figure 18c.1: the convergence of the method.**

```python
steps_list = sorted(errors)
hs = np.array([X_END / n for n in steps_list])
errs = np.array([errors[n] for n in steps_list])
fig, ax = plt.subplots(figsize=(7.0, 4.4))
ax.loglog(hs, errs, "o-", color="#2a78d6", label="RK4 error at $x_4 = 20$")
ax.loglog(hs, errs[-1] * (hs / hs[-1]) ** 4, "--", color="#52514e",
          label="slope 4: error $\\propto h^4$")
ax.set_xlabel("step length $h$ (units $1/m$)")
ax.set_ylabel("largest error of a component")
ax.legend()
```

`hs` holds the five step lengths $20/n$ and `errs` the five errors. `ax.loglog` draws with logarithmic axes on both sides: a power law $e = ch^p$ becomes a straight line of slope $p$, because $\log e = \log c + p\log h$. The dashed comparison line $e_{\rm last}(h/h_{\rm last})^4$ has the slope 4 and passes through the last point.

```python
save_figure(fig, "rk4_convergence",
            "Accuracy of the Runge-Kutta solution of the homogeneous field equation "
            "in the author's metric: the largest difference between a component of "
            "the computed field and of the exact solution of the Revision theory "
            "record at the time $x_4 = 20$ (vertical axis, logarithmic), against "
            "the step length $h$ in units of $1/m$ (horizontal axis, logarithmic), "
            "for 250 to 4000 steps. The points follow the dashed line of slope 4: "
            "halving the step divides the error by 16, the fourth order of the "
            "method. With 2000 steps the error is far below every difference "
            "studied in this notebook.")
```

**What you see in Figure 18c.1:** five points on a straight line parallel to the dashed line of slope 4, falling from about $2 \times 10^{-5}$ at $h = 0.08$ to about $3 \times 10^{-10}$ at $h = 0.005$. Why it matters for the theorems: the differences studied below are either zero by a theorem (they must come out below $10^{-12}$) or of order 1 (the negative control). Moreover the map $\Psi \to \Gamma\Psi$ commutes with every step of the method: the slopes of the T1 partner are $\Gamma$ times the slopes of the field, because $F_{-m,-\lambda}(\Gamma\Psi) = \Gamma F_{m,\lambda}(\Psi)$ (the same computation as $\Gamma M\Gamma$ in Section 18.21), and in the same way $F^{\rm mirror}_{-m,\lambda}(\gamma^{(x_8)}\Psi) = \gamma^{(x_8)}F_{m,\lambda}(\Psi)$. So a partner computed with the same steps equals the mapped field up to rounding, whatever the integration error; the comparison with the exact formula shows, in addition, that both are the true solutions to $10^{-9}$.

**In [7], theorem T1 in numbers.**

```python
phi = rk4(Gamma @ psi0, -m, -lam, 1, STEPS)  # the T1 partner, solved on its own
t1_gap = np.abs(phi - psi @ Gamma.T).max()  # row by row: Gamma psi(x4)
wrong = rk4(Gamma @ psi0, -m, lam, 1, STEPS)  # the negative control (-m, +lambda)
wrong_gap = np.abs(wrong - psi @ Gamma.T).max()
report("largest difference of the wrong partner (-m, +lambda) from Gamma Psi",
       f"{wrong_gap:.3f}")
check(t1_gap < 1e-12, "T1: the (-m, -lambda) solution from Gamma Psi(0) is Gamma "
      "Psi(x4) at all 2001 times (difference below 1e-12)")
check(wrong_gap > 0.1, "negative control: the (-m, +lambda) solution from Gamma "
      "Psi(0) is not Gamma Psi(x4)")
```

`phi` is the solution of the partner theory $(-m, -\lambda)$ started from $\Gamma\Psi(0)$, computed by the same Runge-Kutta function with no knowledge of `psi`. In `psi @ Gamma.T` each row of the table `psi` is $\Psi(x_4)$ written as a row, and a row times $\Gamma^T$ is $(\Gamma\Psi)^T$; so this table holds $\Gamma\Psi(x_4)$ at all 2001 times, and `t1_gap` is its largest difference from `phi`. `wrong` is the negative control, the theory $(-m, +\lambda)$ from the same start, and `wrong_gap` its largest difference from $\Gamma\Psi$. Out [7] prints RESULT largest difference of the wrong partner (-m, +lambda) from Gamma Psi = 1.641 and two PASS lines: the T1 partner equals $\Gamma\Psi$ to better than $10^{-12}$ at every time, while the wrong partner is off by 1.641, as much as the field itself (the column has length 1). Why it fails: with $S$ unchanged its coefficient is $V = -m + \lambda S = -1 + 0.269196 = -0.730804$ instead of $-1.269196$, so it oscillates with the frequency $\sqrt{0.730804^2 - 0.36} = 0.4172$ instead of $1.1184$.

**In [8], Figure 18c.2: the partner, component by component.**

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0), sharey=True)
every = slice(0, STEPS + 1, 40)  # a dot every 40 steps
for ax, A in zip(axes, (0, 8)):
    ax.plot(times, psi[:, A].real, color="#2a78d6",
            label=f"$\\Psi_{{{A + 1}}}$, mass $m$, coupling $\\lambda$")
    ax.plot(times[every], phi[every, A].real, "o", color="#eb6834", markersize=3.5,
            label=f"$\\Phi_{{{A + 1}}}$, mass $-m$, coupling $-\\lambda$")
    ax.plot(times, wrong[:, A].real, "--", color="#52514e", linewidth=0.9,
            label="wrong partner: $-m$, $+\\lambda$")
    ax.set_xlabel("time $x_4$ (units $1/m$)")
    ax.set_title(f"component {A + 1}: " + ("$\\Phi = -\\Psi$" if A < 8
                                            else "$\\Phi = +\\Psi$"), fontsize=10)
    ax.legend(loc="lower left", fontsize=8)
axes[0].set_ylabel("real part of the component")
```

Two panels side by side that share the vertical axis (`sharey=True`). `every` is a **slice** that takes every 40th of the 2001 times, so that the dots do not hide the line. The loop draws component 1 (Python place 0) in the left panel and component 9 (place 8) in the right one: the real part of $\Psi_A$ as a blue line, of the partner $\Phi_A$ as orange dots, and of the wrong partner as a thin dashed line. In the f-strings, `{{{A + 1}}}` prints a brace, the number $A + 1$ and a brace, so that the label reads $\Psi_1$ or $\Psi_9$ in LaTeX. The title of each panel says which relation holds in that half.

```python
save_figure(fig, "partner_components",
            "A solution and its T1 partner, computed separately. Lines: the real "
            "part of component 1 (left) and component 9 (right) of the homogeneous "
            "solution $\\Psi$ with mass $m = 1$ and coupling $\\lambda = 0.3$, "
            "against the time $x_4$ in units of $1/m$. Dots: the same components "
            "of the solution $\\Phi$ of the theory with $-m$ and $-\\lambda$, "
            "started from $\\Gamma\\Psi(0)$ and integrated on its own. In the first "
            "half of the components $\\Phi = -\\Psi$, in the second half "
            "$\\Phi = +\\Psi$: the partner is exactly $\\Gamma\\Psi$ at every time, "
            "as theorem T1 says. Dashed: the negative control with $-m$ and "
            "$+\\lambda$, which drifts away because it oscillates with another "
            "frequency.")
```

**What you see in Figure 18c.2:** on the left, the dots lie on the mirror image of the blue line in the horizontal axis ($\Phi_1 = -\Psi_1$: they start near $+0.21$ where the line starts near $-0.21$); on the right, the dots lie on the line ($\Phi_9 = +\Psi_9$). The dashed wrong partner starts at the same values as the dots but oscillates with the period $2\pi/0.4172 \approx 15.1$ instead of $2\pi/1.1184 \approx 5.62$ and drifts away. This is $\Gamma = \mathrm{diag}(-I_8, I_8)$ at work on an actual solution.

**In [9], the bilinears of a homogeneous field, and T1 for them.**

```python
def bilinears(field, mass, coup, t, zv, s8):
    """S, J^mu (8 numbers) and T_mu nu (8 x 8) of a homogeneous field at (t, zv)."""
    geo = geometry_at(t, zv, s8)
    D = {mu: geo["Om"][mu] @ field for mu in range(1, 9)}
    D[4] = D[4] + generator(field, mass, coup, s8) @ field  # d field / dx4
    bar = field.conj() @ C  # the adjoint row Psibar = Psi^dagger C
    Dbar = {mu: D[mu].conj() @ C for mu in range(1, 9)}
    S = (bar @ field).real
```

`bilinears(field, mass, coup, t, zv, s8)` computes, for one column `field` at the time `t` and the angle `zv`, every quantity the theorems speak about. `geo` holds the geometry there. The covariant derivatives: a homogeneous field has $\partial_\mu\Psi = 0$ for $\mu \neq 4$, so $D_\mu\Psi = \Omega_\mu\Psi$, and $\partial_4\Psi = M\Psi$ by the field equation, which the line `D[4] = D[4] + ...` adds to $\Omega_4\Psi$ (zero here). `bar` is the row $\bar\Psi = \Psi^\dagger C$ (`field.conj() @ C`: the conjugate column used as a row, times $C$). `Dbar` uses $D_\mu\bar\Psi = (D_\mu\Psi)^\dagger C$, which follows from the reality of $\Omega_\mu$:

$$
(D_\mu\Psi)^\dagger C = (\partial_\mu\Psi)^\dagger C + \Psi^\dagger\Omega_\mu^TC = \partial_\mu\bar\Psi - \Psi^\dagger C\Omega_\mu = D_\mu\bar\Psi .
$$

The rule $(XY)^\dagger = Y^\dagger X^\dagger$ with $\Omega_\mu^\dagger = \Omega_\mu^T$ ($\Omega_\mu$ is real); then $\Omega_\mu^TC = -C\Omega_\mu$ (Exercise 18.4 derives it from $C\gamma^{(a)}C^{-1} = -(\gamma^{(a)})^T$); then the definition of $D_\mu\bar\Psi$. `S` is $\bar\Psi\Psi$.

```python
    L = 0.5 * sum(bar @ geo["up"][mu] @ D[mu] - Dbar[mu] @ geo["up"][mu] @ field
                  for mu in range(1, 9)) - mass * S - 0.5 * coup * S ** 2
    T = np.zeros((8, 8), dtype=complex)
    for mu in range(1, 9):
        for nu in range(1, 9):
            T[mu - 1, nu - 1] = 0.25 * (
                bar @ geo["down"][mu] @ D[nu] + bar @ geo["down"][nu] @ D[mu]
                - Dbar[mu] @ geo["down"][nu] @ field
                - Dbar[nu] @ geo["down"][mu] @ field)
            if mu == nu:
                T[mu - 1, nu - 1] -= geo["g"][mu] * L
    J = np.array([-1j * bar @ geo["up"][mu] @ field for mu in range(1, 9)])
    assert np.abs(T.imag).max() < 1e-12 and np.abs(J.imag).max() < 1e-12
    return S, J.real, T.real
```

`L` is $\mathcal{L}/\sqrt{|g|}$ of Section 18.4: half the sum over $\mu$ of $\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi$, minus $mS$, minus $\frac{\lambda}{2}S^2$. `T` is the $8 \times 8$ table of $T_{\mu\nu}$ of the pairing record (Section 18.4), built from the lowered gammas $\gamma_\mu$ (`geo["down"]`), with $-g_{\mu\mu}\mathcal{L}/\sqrt{|g|}$ added on the diagonal; it is stored at the place `[mu - 1, nu - 1]` because Python counts from 0. `J` holds $J^\mu = -i\bar\Psi\gamma^\mu\Psi$, the convention of the theory record, for $\mu = 1, \dots, 8$. For a commuting field all these numbers are real (the Lagrangian is real, Chapter 7); `assert` confirms that their imaginary parts are below $10^{-12}$, and the function returns the real parts.

```python
SAMPLE = range(0, STEPS + 1, 20)  # 101 sampled times
sampled = times[list(SAMPLE)]
data = {"psi": [bilinears(psi[n], m, lam, times[n], Z0, 1) for n in SAMPLE],
        "phi": [bilinears(phi[n], -m, -lam, times[n], Z0, 1) for n in SAMPLE]}
scale_T = max(np.abs(T).max() for _, _, T in data["psi"])
scale_J = max(np.abs(J).max() for _, J, _ in data["psi"])
t1_T = max(np.abs(Tp + Tq).max() for (_, _, Tp), (_, _, Tq)
           in zip(data["psi"], data["phi"])) / scale_T
t1_J = max(np.abs(Jp + Jq).max() for (_, Jp, _), (_, Jq, _)
           in zip(data["psi"], data["phi"])) / scale_J
t1_S = max(abs(Sp - Sq) for (Sp, _, _), (Sq, _, _) in zip(data["psi"], data["phi"]))
reproduces(t1_T < 1e-12 and t1_J < 1e-12 and t1_S < 1e-12,
           "T1: S kept, J -> -J (8) and T -> -T (36) at all 101 sampled times",
           (PY, ["T1.metric.commuting.emt", "T1.metric.commuting.current"]))
```

`SAMPLE` takes every 20th time, $x_4 = 0, 0.2, 0.4, \dots, 20$: 101 times. `data` holds the bilinears of the field with $(m, \lambda)$ and of its T1 partner with $(-m, -\lambda)$ at the same point $z_0$ of the patch. `scale_T` and `scale_J` are the largest absolute entries of $T$ and $J$ of the field over all sampled times; the differences are divided by them, so that the test measures a relative error. `t1_T` is the largest relative entry of $T[\Psi] + T[\Phi]$, `t1_J` that of $J[\Psi] + J[\Phi]$, and `t1_S` the largest difference of the two values of $S$. The check requires all three below $10^{-12}$ and names the sympy checks `T1.metric.commuting.emt` and `T1.metric.commuting.current`. Out [9] shows the PASS line. COMPUTED on an actual solution along the deflating history: the 36 independent components of $T_{\mu\nu}$ (the table is symmetric) and the 8 of $J^\mu$ of the partner are the negatives of those of the field, and $S$ is the same.

**In [10], three facts of the theory record, and the conservation of the charge.**

```python
rho_ok = p_ok = mixed_ok = flow_ok = True
for n, (S, J, T) in zip(SAMPLE, data["psi"]):
    geo = geometry_at(times[n], Z0, 1)
    rho_ok = rho_ok and abs(-T[3, 3] - (m * S + 0.5 * lam * S ** 2)) < 1e-12
    p = [-T[mu - 1, mu - 1] / geo["g"][mu] for mu in (1, 2, 3, 5, 6, 7, 8)]
    p_ok = p_ok and max(abs(x - 0.5 * lam * S ** 2) for x in p) < 1e-12
    mixed_ok = mixed_ok and abs(T[3, 7]) < 1e-12 * scale_T
    field = psi[n]
    dJ4 = 2 * (field.conj() @ B @ generator(field, m, lam, 1) @ field).real
    Q = (-1j * field.conj() @ C @ gamma[8] @ field).real
    flow_ok = flow_ok and abs(dJ4 + 6 * H * Q) < 1e-12
```

The loop runs over the sampled times of the field (`zip` pairs the time indices with the stored bilinears). `T[3, 3]` is $T_{x_4x_4}$ (place 3 is $x_4$), so `-T[3, 3]` is the energy density $\rho$ of the pairing convention, compared with $mS + \frac{\lambda}{2}S^2$. `p` holds the seven pressures $p_\mu = -g^{\mu\mu}T_{\mu\mu} = -T_{\mu\mu}/g_{\mu\mu}$ of $x_1, x_2, x_3$, of the deflating extra times $x_5, x_6, x_7$ and of $x_8$, each compared with $\frac{\lambda}{2}S^2$. `T[3, 7]` is $T_{x_4x_8}$, which must vanish (relative to `scale_T`). Then the conservation law of Section 18.21: `dJ4` is $\partial_4J^{x_4}$, computed from the field equation $\partial_4\Psi = M\Psi$,

$$
\frac{d}{dx_4}\big(\Psi^\dagger B\Psi\big) = (M\Psi)^\dagger B\Psi + \Psi^\dagger BM\Psi = 2\,\mathrm{Re}\big(\Psi^\dagger BM\Psi\big) .
$$

The product rule; then $(M\Psi)^\dagger B\Psi = \Psi^\dagger M^\dagger B\Psi$ is the complex conjugate of $\Psi^\dagger B^\dagger M\Psi = \Psi^\dagger BM\Psi$ ($B$ is Hermitian), and a number plus its complex conjugate is twice its real part. `Q` is $-i\bar\Psi\gamma^{(x_8)}\Psi$, and the law of Section 18.21 requires $\partial_4J^{x_4} = -6HQ$.

```python
reproduces(rho_ok and p_ok and mixed_ok,
           "rho = m S + (l/2) S^2, all pressures (l/2) S^2, T_x4x8 = 0 (homogeneous)",
           (TH_PY, ["commuting_homogeneous_on_shell_rho_p",
                    "commuting_T_x4x8_homogeneous"]))
reproduces(flow_ok, "the charge is conserved: d4 J^x4 = -6 H Q (flow along x8)",
           (TH_PY, ["commuting_current_conservation"]))
```

Two checks. The first names two checks of the field-theory report `python-field-theory.json`, one for the energy density and the pressures and one for $T_{x_4x_8}$ of homogeneous solutions; the second names its check of the conservation of the charge. Out [10] shows both PASS lines. With the numbers of Out [4] the energy density is $\rho = mS + \frac{\lambda}{2}S^2 = 0.897319 + 0.15 \times 0.805181 = 1.0181$ and every pressure is $0.15 \times 0.805181 = 0.1208$; Exercise 18.2 continues this computation.

**In [11], Figure 18c.3: the T1 pair in numbers.**

```python
def series(name, pick):
    return np.array([pick(S, J, T) for S, J, T in data[name]])


panels = [("charge density $J^{x_4}$", lambda S, J, T: J[3]),
          ("energy density $\\rho = -T_{x_4x_4}$", lambda S, J, T: -T[3, 3]),
          ("$T_{x_4x_1}$ (history-dependent)", lambda S, J, T: T[3, 0])]
fig, axes = plt.subplots(1, 3, figsize=(13.0, 4.0))
for ax, (title, pick) in zip(axes, panels):
    a, b = series("psi", pick), series("phi", pick)
    ax.plot(sampled, a, color="#2a78d6", label="$\\Psi$: $(m, \\lambda)$")
    ax.plot(sampled, b, color="#eb6834", label="T1 partner: $(-m, -\\lambda)$")
    ax.plot(sampled, a + b, color="#52514e", linestyle="--", label="sum")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("time $x_4$ (units $1/m$)")
axes[0].legend(fontsize=8, loc="lower left")
```

`series(name, pick)` returns the time series of one quantity; `pick` is a small function that chooses it from $(S, J, T)$. `panels` lists three choices, each a title and a one-line function (`lambda S, J, T: ...`): $J^{x_4}$ (`J[3]`), $\rho = -T_{x_4x_4}$ and $T_{x_4x_1}$ (`T[3, 0]`). For each panel the field (blue), its T1 partner (orange) and their sum (dashed) are drawn against the sampled times.

```python
save_figure(fig, "t1_pair_densities",
            "The T1 pair in numbers, along the deflating history $a_4 = AHx_4$ "
            "($A = 1$, $H = 0.2$, $m = 1$, $\\lambda = 0.3$, at $z = \\pi/4$). "
            "Horizontal axes: the time $x_4$ in units of $1/m$. Left: the charge "
            "density $J^{x_4}$; middle: the energy density $\\rho$; right: the "
            "mixed component $T_{x_4x_1}$, which grows with the factor $e^{a_4}$ "
            "of the inflating direction. Blue: the solution with $(m, \\lambda)$; "
            "orange: its partner $\\Gamma\\Psi$ with $(-m, -\\lambda)$; dashed: "
            "their sum. Every orange curve is the mirror image of the blue one in "
            "the horizontal axis, and the sum is zero at every time: the pair has "
            "zero total charge and energy-momentum as classical bilinears.")
```

**What you see in Figure 18c.3:** on the left, the blue charge density oscillates between about $-0.04$ and $-0.40$ and the orange one between $+0.04$ and $+0.40$, seven times between $x_4 = 0$ and 20 (the density is quadratic in the field, so it oscillates with the period $\pi/w = 2.81$, half the period of the field); in the middle, two constant lines at $+1.018$ and $-1.018$; on the right, the blue component rises from about 0.05 to 3 and the orange one falls from $-0.05$ to $-3$. In each panel the dashed sum is zero at every time. Why the right panel grows: $T_{x_4x_1}$ contains $\gamma_{x_1} = f_1\gamma^{(x_1)}$ and the connection $\Omega_{x_1}$, both proportional to $e^{a_4} = e^{0.2x_4}$, which grows by the factor $e^4 \approx 54.6$ between $x_4 = 0$ and 20; this is where the deflating history enters the energy-momentum tensor. COMPUTED: $T + T' = 0$ and $J + J' = 0$ at every sampled time.

**In [12], theorem T2 in numbers: the mirror partner.**

```python
chi = rk4(gamma[8] @ psi0, -m, lam, -1, STEPS)  # the mirror partner, on its own
t2_gap = np.abs(chi - psi @ gamma[8].T).max()
data["chi"] = [bilinears(chi[n], -m, lam, times[n], np.pi - Z0, -1) for n in SAMPLE]
LAM = np.array([1, 1, 1, 1, 1, 1, 1, -1], dtype=float)
t2_S = max(abs(Sp + Sx) for (Sp, _, _), (Sx, _, _) in zip(data["psi"], data["chi"]))
t2_J = max(np.abs(Jx - LAM * Jp).max() for (_, Jp, _), (_, Jx, _)
           in zip(data["psi"], data["chi"])) / scale_J
t2_T = max(np.abs(Tx - np.outer(LAM, LAM) * Tp).max() for (_, _, Tp), (_, _, Tx)
           in zip(data["psi"], data["chi"])) / scale_T
```

`chi` is the mirror partner: the theory $(-m, \lambda)$ on the mirror patch ($s_8 = -1$), started from $\gamma^{(x_8)}\Psi(0)$ and solved on its own. `t2_gap` compares it with $\gamma^{(x_8)}\Psi(x_4)$ (`psi @ gamma[8].T`, as in In [7]). `data["chi"]` holds its bilinears at the MIRROR point $z = \pi - z_0 = 3\pi/4$, in the geometry of the mirror patch. `LAM` is $\Lambda = R_8 = \mathrm{diag}(1, 1, 1, 1, 1, 1, 1, -1)$. `t2_S` measures $S[X] + S[\Psi]$, which must vanish because $S$ is reversed; `t2_J` measures $J[X] - \Lambda J[\Psi]$ and `t2_T` measures $T[X] - \Lambda_\mu\Lambda_\nu T[\Psi]$ (`np.outer(LAM, LAM)` is the $8 \times 8$ table of the products $\Lambda_\mu\Lambda_\nu$), both relative.

```python
check(t2_gap < 1e-12, "T2: the (-m, lambda) mirror solution from gamma^(x8) Psi(0) "
      "is gamma^(x8) Psi(x4) at all 2001 times")
reproduces(t2_S < 1e-12 and t2_J < 1e-12 and t2_T < 1e-12,
           "T2: S -> -S, J and T pulled back (charge and energy density equal)",
           (PY, ["T2.metric.commuting.S_odd", "T2.metric.commuting.emt",
                 "T2.metric.commuting.current"]))
```

Two checks: the mirror partner is $\gamma^{(x_8)}\Psi$ at all 2001 times, and $S$ is reversed while $J$ and $T$ are pulled back, with the sympy checks `T2.metric.commuting.S_odd`, `T2.metric.commuting.emt` and `T2.metric.commuting.current`. Out [12] shows both PASS lines. Note what is compared: the field at $z_0 = \pi/4$ on the patch and its partner at $3\pi/4$ on the mirror patch, the two points that the mirror $z \to \pi - z$ exchanges.

**In [13], Figure 18c.4: the T2 pair in numbers.**

```python
panels = [("scalar $S$", lambda S, J, T: S),
          ("charge density $J^{x_4}$", lambda S, J, T: J[3]),
          ("$T_{x_4x_1}$ (history-dependent)", lambda S, J, T: T[3, 0])]
fig, axes = plt.subplots(1, 3, figsize=(13.0, 4.0))
for ax, (title, pick) in zip(axes, panels):
    ax.plot(sampled, series("psi", pick), color="#2a78d6",
            label="$\\Psi$ on the patch: $(m, \\lambda)$")
    ax.plot(sampled[::4], series("chi", pick)[::4], "o", color="#1baf7a",
            markersize=4, label="mirror partner: $(-m, \\lambda)$")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("time $x_4$ (units $1/m$)")
axes[0].set_ylim(-1.1, 1.1)
axes[0].legend(fontsize=8, loc="center left")
```

Three panels, $S$, $J^{x_4}$ and $T_{x_4x_1}$, with the field as a blue line and the mirror partner as green dots at every fourth sampled time (`[::4]` takes every fourth entry). `set_ylim(-1.1, 1.1)` fixes the vertical range of the first panel so that both values of $S$ are visible.

```python
save_figure(fig, "t2_mirror_densities",
            "The T2 pair in numbers, same values as in the previous figure. Blue "
            "line: the solution $\\Psi$ with $(m, \\lambda)$ on the patch at "
            "$z = \\pi/4$; green dots: its mirror partner $\\gamma^{(x_8)}\\Psi$, "
            "solved on its own with $(-m, \\lambda)$ on the mirror patch at "
            "$z = 3\\pi/4$. Horizontal axes: the time $x_4$ in units of $1/m$. "
            "Left: the scalar $S$, constant and exactly opposite for the partner. "
            "Middle and right: the charge density $J^{x_4}$ and the component "
            "$T_{x_4x_1}$, EQUAL for the partner. T2 pairs the mass $m$ with $-m$ "
            "at the same charge and energy-momentum; nothing cancels.")
```

**What you see in Figure 18c.4:** on the left two constant lines, $S = 0.897$ for the field and $S = -0.897$ for the partner; in the middle and on the right the green dots lie ON the blue curves: the mirror partner has the same charge density and the same $T_{x_4x_1}$. Compare Figure 18c.3, where the T1 partner was the mirror image in the horizontal axis. T2 pairs $m$ with $-m$ at EQUAL charge and energy-momentum: nothing cancels in a T2 pair.

**In [14], the spectra of the generators.**

```python
def spectrum(Mx):
    """The 16 eigenvalues, sorted by imaginary part, then real part (rounded)."""
    ev = np.linalg.eigvals(Mx)
    return ev[np.lexsort((np.round(ev.real, 9), np.round(ev.imag, 9)))]


M_psi = generator(psi0, m, lam, 1)
M_t1 = generator(Gamma @ psi0, -m, -lam, 1)
M_t2 = generator(gamma[8] @ psi0, -m, lam, -1)
similar = (np.array_equal(Gamma @ M_psi @ Gamma, M_t1)
           and np.allclose(gamma[8] @ M_psi @ gamma[8], M_t2, atol=1e-15))
sp_psi, sp_t1, sp_t2 = spectrum(M_psi), spectrum(M_t1), spectrum(M_t2)
w_exact = np.sqrt((m + lam * S0) ** 2 - 9 * H ** 2)
report("frequency w of the solution and of both partners", f"{w_exact:.6f}")
check(similar and np.abs(sp_psi - sp_t1).max() < 1e-12
      and np.abs(sp_psi - sp_t2).max() < 1e-12
      and np.allclose(np.sort(np.abs(sp_psi.imag)), w_exact, atol=1e-12),
      "the generators of the field and of its T1 and T2 partners are similar: "
      "equal spectra +-i w")
```

`spectrum(Mx)` returns the 16 eigenvalues of a matrix (`np.linalg.eigvals`) in a fixed order: `np.lexsort` sorts by its last key first, here by the imaginary part and then by the real part, both rounded to 9 decimals so that rounding differences do not change the order. `M_psi`, `M_t1` and `M_t2` are the generators of the field, of the T1 partner and of the mirror partner at the start. `similar` checks $\Gamma M\Gamma = M_{\rm T1}$ with the exact comparison `np.array_equal` ($\Gamma$ only changes the signs of rows and columns, which floating-point arithmetic does exactly) and $\gamma^{(x_8)}M\gamma^{(x_8)} = M_{\rm T2}$ to $10^{-15}$. Similar matrices have the same eigenvalues (Section 18.23), and the check compares the three sorted spectra. It also requires the absolute imaginary parts to equal $w$: since $M^2 = -w^2I_{16}$, every eigenvalue $\mu$ of $M$ obeys $\mu^2 = -w^2$, so $\mu = \pm iw$. Out [14] prints the frequency $w = 1.118417$ of the solution and of both partners, and the PASS line.

```python
masses = np.linspace(-2.0, 2.0, 161)
family = {}
for label, sign_m, sign_l in (("field", 1, 1), ("T1 partner", -1, -1)):
    rows = []
    for mv in masses:
        V = sign_m * mv + sign_l * lam * S0
        Mx = -V * gamma[4] + 3 * H * gamma[4] @ gamma[8]
        rows.append(spectrum(Mx))
    family[label] = np.array(rows)
check(np.abs(family["field"] - family["T1 partner"]).max() < 1e-9,
      "for every mass from -2 to 2 the field and its T1 partner have equal spectra")
```

The same comparison for a whole family: 161 masses from $-2$ to 2 (`np.linspace(-2.0, 2.0, 161)`), at the fixed $\lambda$ and $S_0$. For the field the generator has $V = m + \lambda S_0$; for the T1 partner the mass $-m$ and the coupling $-\lambda$ give $V = -m - \lambda S_0$. The generator $-V\gamma^{(x_4)} + 3H\gamma^{(x_4)}\gamma^{(x_8)}$ is built directly and its sorted spectrum stored, one row per mass. The check requires the two tables to agree to $10^{-9}$ at every mass; Out [14] ends with its PASS line.

**In [15], Figure 18c.5: the spectrum against the mass.**

```python
fig, ax = plt.subplots(figsize=(8.0, 4.4))
for label, colour, style in (("field", "#2a78d6", "-"),
                             ("T1 partner", "#eb6834", "o")):
    rows = family[label]
    kw = {"markersize": 3} if style == "o" else {}
    ax.plot(masses, rows.imag.max(axis=1), style, color=colour,
            label=f"frequency $w$, {label}", **kw)
    ax.plot(masses, rows.real.max(axis=1), style, color=colour, alpha=0.45,
            label=f"growth rate, {label}", **kw)
ax.axvline(m, color="#52514e", linestyle=":", label="the solution of this notebook")
ax.set_xlabel("mass $m$ of the field (the partner has $-m$, $-\\lambda$)")
ax.set_ylabel("eigenvalue part (units $m = 1$)")
ax.legend(fontsize=8, loc="upper center")
```

For the field (lines, style `"-"`) and the partner (dots, style `"o"`; `**kw` passes the marker size only for the dots): the largest imaginary part of the 16 eigenvalues at each mass (`rows.imag.max(axis=1)`, the oscillation frequency $w$) in full colour, and the largest real part (the growth rate) in a lighter shade (`alpha=0.45`). A dotted vertical line marks the mass $m = 1$ of the solution of the notebook.

```python
save_figure(fig, "family_spectrum",
            "The spectrum of the evolution generator of the homogeneous solutions, "
            "against the mass $m$ (horizontal axis) at the fixed coupling "
            "$\\lambda = 0.3$ and scalar $S$ of this notebook, $H = 0.2$. Dark "
            "curves: the oscillation frequency $w$, the largest imaginary part of "
            "the eigenvalues; light curves: the growth rate, the largest real part. "
            "Lines: the field with $(m, \\lambda)$; dots: its T1 partner with "
            "$(-m, -\\lambda)$. They coincide everywhere. Inside the window "
            "$|m + \\lambda S| < 3H$ the frequency is zero and the solutions grow; "
            "outside it they oscillate. The dotted line marks the solution "
            "plotted above.")
```

**What you see in Figure 18c.5:** the dots lie on the lines everywhere. Outside a window of masses the growth rate is zero and the frequency $w = \sqrt{(m + \lambda S_0)^2 - 9H^2}$ rises from 0 at the edges of the window towards the straight lines $|m + \lambda S_0|$; at the dotted line, $m = 1$, it is $1.118$. Inside the window $|m + \lambda S_0| < 3H$, that is $-0.869 < m < 0.331$, the frequency is zero and the growth rate is an arc with the top $3H = 0.6$ at $m = -\lambda S_0 = -0.269$. Why an arc: inside the window the eigenvalues are $\pm\kappa$ with $\kappa^2 = 9H^2 - (m + \lambda S_0)^2$, so $\kappa^2 + (m + \lambda S_0)^2 = (3H)^2$, the equation of a circle of radius $3H$ (drawn with different scales on the two axes). The field and its T1 partner have the same spectrum for every mass: T1 never turns an oscillating universe into a growing one.

**In [16], plane waves in flat space: the quantum reading Q.**

```python
def h_matrix(mass, k):
    """h_m(k) = -i m gamma^(x4) - gamma^(x4) sum_(a != 4) k_a gamma^(a)."""
    out = -1j * mass * gamma[4]
    for a in (1, 2, 3, 5, 6, 7, 8):
        out = out - k[a - 1] * gamma[4] @ gamma[a]
    return out


def w_squared(mass, k):
    return mass ** 2 + sum(k[a - 1] ** 2 for a in (1, 2, 3, 8)) - sum(
        k[a - 1] ** 2 for a in (5, 6, 7))


def eigenspace(Mx, value, tol=1e-9):
    """Orthonormal columns spanning the null space of Mx - value I."""
    _, sv, vh = np.linalg.svd(Mx - value * I16)
    return vh[sv < tol].conj().T


def inertia(V):
    """(positive, negative) eigenvalue counts of V^dagger B V."""
    ev = np.linalg.eigvalsh(V.conj().T @ B @ V)
    return int((ev > 1e-9).sum()), int((ev < -1e-9).sum())
```

Four helpers. The first, `h_matrix(mass, k)`, builds the one-particle matrix of Section 18.22,

$$
h_m(k) = -im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_{a\neq4}k_a\gamma^{(a)} ,
$$

where `k[a - 1]` is $k_a$ (the entry $k_4$ is never used). `w_squared` returns $m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$. `eigenspace(Mx, value)` returns orthonormal columns that span the eigenspace of the eigenvalue `value`, that is the null space of $M_x - wI_{16}$. It uses the **singular value decomposition** `np.linalg.svd`, which writes a matrix as $A = U\Sigma V^\dagger$ with $U$ and $V$ unitary (orthonormal columns) and $\Sigma$ diagonal with the singular values $\sigma_j \geq 0$; since $Av_j = \sigma_ju_j$ for the columns $u_j$ of $U$ and $v_j$ of $V$, the columns $v_j$ with $\sigma_j = 0$ (in floating point: below $10^{-9}$) span the null space. numpy returns $V^\dagger$ (`vh`), so the selected rows are conjugated and transposed into columns. `inertia(V)` counts the positive and the negative eigenvalues of the $8 \times 8$ Hermitian matrix $V^\dagger BV$, the Krein form restricted to the eigenspace (`np.linalg.eigvalsh` computes the eigenvalues of a Hermitian matrix).

```python
R8 = np.array([1, 1, 1, 1, 1, 1, 1, -1], dtype=float)
rand = np.random.default_rng(7)
square_ok = maps_ok = True
for _ in range(50):
    k, mv = rand.normal(size=8), rand.normal()
    h = h_matrix(mv, k)
    square_ok = square_ok and np.allclose(h @ h, w_squared(mv, k) * I16, atol=1e-12)
    maps_ok = (maps_ok and np.allclose(Gamma @ h @ Gamma, h_matrix(-mv, k))
               and np.allclose(gamma[8] @ h @ gamma[8], h_matrix(-mv, R8 * k)))
```

`R8` reverses $k_8$. With the fixed seed 7, fifty random masses and momenta are drawn; for each, `square_ok` checks $h^2 = w^2I_{16}$ and `maps_ok` checks $\Gamma h_m(k)\Gamma = h_{-m}(k)$ and $\gamma^{(x_8)}h_m(k)\gamma^{(x_8)} = h_{-m}(R_8k)$ (`R8 * k` multiplies entry by entry).

```python
samples = read_json(THEORY)["data"]["one_particle_flat"]["samples"]
rows_ok = True
for row in samples:
    k = np.array(row["k"], dtype=float)
    w = float(sp.sympify(row["w"].replace("Sqrt[", "sqrt(").replace("]", ")")))
    h = h_matrix(row["m"], k)
    Vp, Vn = eigenspace(h, w), eigenspace(h, -w)
    mine = (np.isclose(np.sqrt(w_squared(row["m"], k)), w), Vp.shape[1],
            Vn.shape[1], inertia(Vp), inertia(Vn))
    rows_ok = rows_ok and mine == (True, row["dim_plus_w"], row["dim_minus_w"],
                                   tuple(row["B_inertia_plus_w"]),
                                   tuple(row["B_inertia_minus_w"]))
    (pp, pn), (qp, qn) = inertia(Vp), inertia(Vn)
    say(f"m = {row['m']:+d}, k = {row['k']}: w = {w:.6f}, dimensions "
        f"{Vp.shape[1]} and {Vn.shape[1]}, Krein inertia ({pp},{pn}) and "
        f"({qp},{qn})")
```

`samples` is the data table `one_particle_flat` of `pairing-theory.json`: eight rows, each with $m$, $k$, the frequency $w$ as text (for example `Sqrt[2]`, the Wolfram way of writing $\sqrt2$), the dimensions of the two eigenspaces and their Krein inertias. The text of $w$ is translated into sympy's `sqrt(2)`, read by `sp.sympify` and turned into a number by `float`. For each row the cell computes the eigenspaces of $+w$ and $-w$, their dimensions (`shape[1]`, the number of columns) and their inertias; `mine` collects them in the order of the record, and `rows_ok` requires equality with the record. One line per sample is printed.

```python
reproduces(square_ok and maps_ok,
           "h_m^2 = w^2 I16; Gamma h_m Gamma = h_-m; gamma^(x8) h_m gamma^(x8) = "
           "h_-m(R8 k)", (WL, ["Q_one_particle_flat_dispersion", "Q_one_particle_maps"]),
           (PY, ["Q.one_particle_maps"]))
reproduces(rows_ok and len(samples) == 8,
           "the eight recorded samples: w, dimensions 8 and 8, Krein inertia (4,4)",
           (WL, ["Q_one_particle_Krein_signatures"]),
           (PY, ["compare.theory.one_particle", "Q.one_particle_Krein_inertia_proof"]))
```

Two checks with their records. Out [16] prints the eight samples, each with the dimensions 8 and 8 and the Krein inertias (4,4) and (4,4), and two PASS lines. COMPUTED in floating point, they agree with the exact samples of the record.

**In [17], imaginary and zero frequencies.**

```python
neutral_ok = True
for k in ([0, 0, 0, 0, 2, 0, 0, 0], [1, 0, 0, 0, 2, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0]):
    k = np.array(k, dtype=float)
    h, w2 = h_matrix(1.0, k), w_squared(1.0, k)
    if w2 == 0:
        spaces = [eigenspace(h, 0.0)]
        neutral_ok = neutral_ok and np.allclose(h @ h, 0.0)
    else:
        w = 1j * np.sqrt(-w2)
        spaces = [eigenspace(h, w), eigenspace(h, -w)]
    dims = [V.shape[1] for V in spaces]
    largest = max(np.abs(V.conj().T @ B @ V).max() for V in spaces)
    neutral_ok = neutral_ok and all(dim == 8 for dim in dims) and largest < 1e-9
    say(f"k = {k.astype(int).tolist()}: w^2 = {w2:+.0f}, eigenspace dimensions "
        f"{dims}, Krein form zero on them: {largest < 1e-9}")
```

Three momenta with an extra-time component $k_5$ at $m = 1$: $w^2 = 1 - 4 = -3$, $w^2 = 1 + 1 - 4 = -2$ and $w^2 = 1 - 1 = 0$. For $w^2 < 0$ the frequencies are $\pm i\sqrt{-w^2}$ (`1j * np.sqrt(-w2)`) and both eigenspaces are computed; for $w^2 = 0$ the eigenspace of 0 is computed and $h^2 = 0$ is checked. `largest` is the largest absolute entry of $V^\dagger BV$ over the eigenspaces; **Krein-neutral** means that it vanishes. The check requires the dimension 8 everywhere and `largest` below $10^{-9}$.

```python
reproduces(neutral_ok, "imaginary and zero frequencies: eigenspaces of dimension 8 "
           "are Krein-neutral",
           (PY, ["Q.one_particle_complex_frequency_Krein_neutral"]),
           (WL, ["Q_one_particle_complex_and_zero_frequencies_Krein_neutral"]))
```

Out [17] prints the three cases (eigenspace dimensions [8, 8], [8, 8] and [8]; Krein form zero on them: True) and the PASS line, with the checks `Q.one_particle_complex_frequency_Krein_neutral` and `Q_one_particle_complex_and_zero_frequencies_Krein_neutral`. These are the growing extra-time waves: they carry no Krein norm at all (Section 18.23).

**In [18], Figure 18c.6: the mapped spectra of plane waves.**

```python
ks = np.linspace(0.0, 3.0, 121)
curves = {}
for label, mass in (("plus", 1.0), ("minus", -1.0)):
    for axis in (1, 5):
        rows = []
        for kv in ks:
            k = np.zeros(8)
            k[axis - 1] = kv
            rows.append(spectrum(h_matrix(mass, k)))
        curves[label, axis] = np.array(rows)
away = np.abs(ks - 1.0) > 0.05
equal = max(np.abs(curves["plus", axis][away] - curves["minus", axis][away]).max()
            for axis in (1, 5))
check(equal < 1e-6, "the plane-wave spectra of the masses +1 and -1 are equal")
```

121 momenta from 0 to 3. For the masses $+1$ and $-1$, and for a momentum along $x_1$ (`axis = 1`) or along $x_5$ (`axis = 5`), the 16 sorted eigenvalues of $h_m(k)$ are stored. `away` excludes the momenta within 0.05 of $k = 1$: there the extra-time wave has $w = 0$ and $h^2 = 0$, and the eigenvalues of such a matrix are very sensitive to rounding (a change of its entries by $10^{-16}$ can move them by about $10^{-8}$, the square root). The check requires the two spectra to agree to $10^{-6}$ at all other momenta.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
for ax, axis, name in ((axes[0], 1, "3-space momentum $k_1$"),
                       (axes[1], 5, "extra-time momentum $k_5$")):
    ax.plot(ks, np.sqrt(np.clip(1.0 + (ks ** 2 if axis == 1 else -ks ** 2), 0, None)),
            color="#2a78d6", label="real part, mass $+1$")
    ax.plot(ks, np.sqrt(np.clip(-1.0 + (ks ** 2 if axis == 5 else -ks ** 2), 0,
                                None)), color="#eb6834",
            label="imaginary part, mass $+1$")
    dots = curves["minus", axis]
    ax.plot(ks[::5], np.abs(dots.real).max(axis=1)[::5], "o", color="#2a78d6",
            markersize=3.5, alpha=0.6, label="mass $-1$ (dots)")
    ax.plot(ks[::5], np.abs(dots.imag).max(axis=1)[::5], "o", color="#eb6834",
            markersize=3.5, alpha=0.6)
    ax.set_xlabel(name + " (units $m$)")
    ax.set_ylim(-0.1, 3.3)
axes[0].set_ylabel("frequency $|w|$: real and imaginary parts")
axes[0].legend(fontsize=8, loc="upper left")
```

Two panels. The lines are the exact formulas for the mass $+1$: the real part $\sqrt{1 + k_1^2}$ (left) or $\sqrt{1 - k_5^2}$ (right, where it exists) and the imaginary part, zero on the left and $\sqrt{k_5^2 - 1}$ on the right for $k_5 > 1$; `np.clip(x, 0, None)` replaces negative numbers by 0 before the square root. The dots are the largest absolute real part and the largest absolute imaginary part of the computed eigenvalues for the mass $-1$, at every fifth momentum.

```python
save_figure(fig, "flat_dispersion",
            "Mapped spectra of plane waves in flat 4+4 space: the frequencies, the "
            "eigenvalues of the one-particle matrix $h_m(k)$, for the mass $+1$ "
            "(lines) and $-1$ (dots), against a 3-space momentum $k_1$ (left) and "
            "an extra-time momentum $k_5$ (right), in units of the mass. Blue: "
            "the real part $\\sqrt{1 + k_1^2}$ or $\\sqrt{1 - k_5^2}$; orange: the "
            "imaginary part, which appears when the extra-time momentum exceeds the "
            "mass (a growing mode). Each value is 8-fold, with both signs. The "
            "dots lie on the lines: the universes of mass $+m$ and $-m$ have the "
            "same one-particle spectrum, because $\\Gamma h_m\\Gamma = h_{-m}$.")
```

**What you see in Figure 18c.6:** on the left the frequency rises from 1 along $\sqrt{1 + k_1^2}$ and the imaginary part stays zero; on the right the real part falls from 1 to 0 at $k_5 = 1$ and from there the imaginary part rises along $\sqrt{k_5^2 - 1}$, a growing wave whose growth rate increases without limit as $k_5$ grows. The dots of the mass $-1$ lie on the lines of the mass $+1$ everywhere: the universes of masses $+m$ and $-m$ have the same one-particle spectrum (Q4), because $\Gamma h_m\Gamma = h_{-m}$.

**In [19], the Krein norms of single modes.**

```python
row = samples[0]
k = np.array(row["k"], dtype=float)
w = 5.0
h = h_matrix(row["m"], k)
columns, freqs = [], []
for value in (w, -w):
    V = eigenspace(h, value)
    ev, U = np.linalg.eigh(V.conj().T @ B @ V)  # diagonalise the Krein form
    for j in np.argsort(-ev):  # positive norms first
        u = V @ U[:, j] / np.sqrt(abs(ev[j]))  # Krein norm +1 or -1
        columns.append(u)
        freqs.append(value)
```

The first recorded sample, $m = 2$, $k = (1, 2, 0, 0, 0, 0, 0, 4)$, with $w = \sqrt{4 + 1 + 4 + 16} = 5$. For each of the two eigenspaces ($+5$ and $-5$), `V` holds 8 orthonormal columns. The Krein form on the eigenspace is the $8 \times 8$ Hermitian matrix $V^\dagger BV$; `np.linalg.eigh` returns its eigenvalues `ev` and an orthonormal set of eigenvectors, the columns of `U`. The loop takes them in the order of decreasing eigenvalue (`np.argsort(-ev)`) and forms $u = VU_j/\sqrt{|\epsilon_j|}$, where $U_j$ is column $j$ of `U` and $\epsilon_j$ its eigenvalue. Its Krein norm is

$$
u^\dagger Bu = \frac{U_j^\dagger(V^\dagger BV)U_j}{|\epsilon_j|} = \frac{\epsilon_j\,U_j^\dagger U_j}{|\epsilon_j|} = \pm1 .
$$

The first step inserts $u$; the second uses $(V^\dagger BV)U_j = \epsilon_jU_j$; the last uses $U_j^\dagger U_j = 1$. So the 16 columns have the Krein norms $+1$ or $-1$, and `freqs` records the frequency of each.

```python
norms = np.array([(u.conj() @ B @ u).real for u in columns])
norms_G = np.array([((Gamma @ u).conj() @ B @ (Gamma @ u)).real for u in columns])
norms_8 = np.array([((gamma[8] @ u).conj() @ B @ (gamma[8] @ u)).real
                    for u in columns])
eig_G = all(np.allclose(h_matrix(-row["m"], k) @ (Gamma @ u), f * (Gamma @ u))
            for u, f in zip(columns, freqs))
eig_8 = all(np.allclose(h_matrix(-row["m"], R8 * k) @ (gamma[8] @ u),
                        f * (gamma[8] @ u)) for u, f in zip(columns, freqs))
say("Krein norms of the 16 columns: " + " ".join(f"{x:+.0f}" for x in norms))
reproduces(eig_G and eig_8 and np.allclose(norms_G, -norms)
           and np.allclose(norms_8, norms) and int((norms > 0).sum()) == 8,
           "Gamma u: eigenvector of h_-m, Krein norm reversed; gamma^(x8) u: kept",
           (WL, ["Q_Krein_metric_of_images"]),
           (PY, ["Q.image_krein_metric", "Q.T2_image_keeps_B"]))
```

`norms`, `norms_G` and `norms_8` are the Krein norms of $u$, of $\Gamma u$ and of $\gamma^{(x_8)}u$. `eig_G` checks that $\Gamma u$ is an eigenvector of $h_{-m}(k)$ with the same frequency, and `eig_8` that $\gamma^{(x_8)}u$ is one of $h_{-m}(R_8k)$ (the maps of Q4). The check requires these, $(\Gamma u)^\dagger B(\Gamma u) = -u^\dagger Bu$, $(\gamma^{(x_8)}u)^\dagger B(\gamma^{(x_8)}u) = u^\dagger Bu$, and eight positive norms among the sixteen. Why the norms behave so: $(Mu)^\dagger B(Mu) = u^\dagger M^\dagger BMu$, and for the real symmetric matrices $M = \Gamma$ and $M = \gamma^{(x_8)}$ Lemma 4 gives $M^\dagger BM = MBM^\dagger = \sigma_MB$ with $\sigma_\Gamma = -1$ and $\sigma_{\gamma^{(x_8)}} = +1$ (Exercise 18.6). Out [19] prints the norms $+1, +1, +1, +1, -1, -1, -1, -1$ twice, once for each eigenspace, and the PASS line.

**In [20], Figure 18c.7: the Krein norms as bars.**

```python
fig, ax = plt.subplots(figsize=(10.0, 4.2))
idx = np.arange(16)
ax.bar(idx - 0.27, norms, width=0.27, color="#2a78d6", label="$u^\\dagger Bu$")
ax.bar(idx, norms_G, width=0.27, color="#eb6834",
       label="$(\\Gamma u)^\\dagger B(\\Gamma u)$: T1 image")
ax.bar(idx + 0.27, norms_8, width=0.27, color="#1baf7a",
       label="$(\\gamma^{(x_8)}u)^\\dagger B(\\gamma^{(x_8)}u)$: T2 image")
ax.axvline(7.5, color="#52514e", linewidth=0.8)
ax.text(3.5, 1.35, "frequency $+5$", ha="center", fontsize=9)
ax.text(11.5, 1.35, "frequency $-5$", ha="center", fontsize=9)
ax.set_xticks(idx, [str(j + 1) for j in idx])
ax.set_xlabel("column number $j$ (eight per eigenspace)")
ax.set_ylabel("Krein norm")
ax.set_ylim(-1.6, 1.6)
ax.legend(fontsize=8, loc="lower left", ncol=3)
```

Three bars per column: the norm of $u$ (blue, shifted left by 0.27), of $\Gamma u$ (orange, in the middle) and of $\gamma^{(x_8)}u$ (green, shifted right). A thin vertical line separates the two eigenspaces and two labels name their frequencies; `set_xticks` labels the columns 1 to 16.

```python
save_figure(fig, "krein_norms",
            "Krein norms of plane-wave eigenvectors and of their images, for the "
            "recorded sample $m = 2$, $k = (1, 2, 0, 0, 0, 0, 0, 4)$, frequency "
            "$w = \\pm5$. Horizontal axis: the 16 eigenvector columns $u$, eight "
            "for $+5$ and eight for $-5$; vertical axis: the Krein norm. Blue: "
            "$u^\\dagger Bu$, four $+1$ and four $-1$ in each eigenspace (Krein "
            "inertia (4,4)). Orange: the chirality image $\\Gamma u$, an "
            "eigenvector of the mass $-m$ with every norm reversed. Green: the "
            "mirror image $\\gamma^{(x_8)}u$, an eigenvector of the mass $-m$ with "
            "every norm kept. This is the quantum reading Q at the level of single "
            "modes.")
```

**What you see in Figure 18c.7:** in each eigenspace four blue bars at $+1$ and four at $-1$ (the Krein inertia (4,4)); every orange bar points the other way; every green bar equals its blue bar. The chirality image (T1) of a mode with a positive Krein norm is a mode of the mass $-m$ with a negative norm; the mirror image (T2) keeps the norm. This is Q1 and Q5 at the level of single modes.

**In [21], the last check.**

```python
figure_names = ["rk4_convergence", "partner_components", "t1_pair_densities",
                "t2_mirror_densities", "family_spectrum", "flat_dispersion",
                "krein_norms"]
paths = [output_file(f"{FIGURE_FOLDER}/18c_{k}_{name}.png")
         for k, name in enumerate(figure_names, 1)]
check(all(path.is_file() for path in paths),
      "every figure file of this notebook exists")
all_checks_passed()
```

The seven figure files must exist; the last line is ALL 21 CHECKS PASSED (notebook 18c).

**What Notebook 18c established.** The following results are COMPUTED for one homogeneous solution of the commuting field dirac16complex00, with the illustrative values ($m = 1$, $H = 0.2$, $\lambda = 0.3$, $z_0 = \pi/4$, seed 2026) along the canonical deflating history $a_4 = AHx_4$ ($A = 1$, from the Revision record): the Runge-Kutta solution equals the exact solution of the theory record to $4.3 \times 10^{-9}$ (fourth order measured); the T1 partner, solved on its own, is $\Gamma\Psi$, with opposite charge density, current and energy-momentum tensor at every time, while the wrong partner $(-m, +\lambda)$ is not; the T2 partner on the mirror patch is $\gamma^{(x_8)}\Psi$, with $S$ reversed and EQUAL charge and energy densities; the generators of the field and of both partners have equal spectra; and for plane waves the eight recorded samples of Q are reproduced, the growing waves are Krein-neutral, $\Gamma$ reverses every Krein norm and $\gamma^{(x_8)}$ keeps it. ASSUMED: the mirror patch glued at the degenerate brane, and a fixed gravitational field. NOT shown: any process that creates a universe or a pair. The partners are solutions of OTHER parameter sets, computed from the first one; nothing in these equations makes them appear.

### 18.28 What the pairing theorems do not establish

T1, T2 and Q are exact. Their content is precisely this: explicit invertible maps between the solutions of two theories with different parameters, with stated signs for the Lagrangian, the energy-momentum tensor, the current and the canonical anticommutator. Both Revision verifiers wrote, independently of each other, a list of what these theorems do NOT establish, and a comparison check confirms that the two lists cover the same topics (`python-pairing.json`, check `compare.theory.not_established`; the lists are the entries `not_established` of `pairing-theory.json` and of `python-pairing.json`). Merged, with the reason for each item:

1. **No creation process.** The theorems map solutions to solutions and quantities to quantities. Nothing in these equations produces a universe, a pair of universes, or a change of the number of universes; no transition from "no universe" to "two universes", no initial state, no vacuum decay and no tunnelling process is derived.
2. **No rate, probability or amplitude.** No transition amplitude, probability, cross-section, rate or Bogoliubov coefficient for creating universes of masses $+m$ and $-m$ is computed or implied; no wave function of the universe and no path integral is part of the theorems.
3. **No dynamical necessity.** No equation and no conservation law forces the partner to exist. A single universe of mass $+m$ is an equally valid solution without its partner. T1 and T2 are correspondences between the solutions of two parameter sets, not a mechanism.
4. **T1 is not a symmetry of one theory, and for $\lambda \neq 0$ it is not a pure $+m$ / $-m$ pairing.** It changes the parameters to $(-m, -\lambda)$ and the sign of the action. The pairing $(m, \lambda) \to (-m, \lambda)$ at fixed coupling is T2, at EQUAL, not opposite, energy-momentum.
5. **The zero total of a T1 pair has a limited meaning.** $T + T' = 0$, $J + J' = 0$ and $Q + Q' = 0$ hold for classical bilinears (a configuration and its image) and as an operator identity within ONE quantum system (Q2). They do not hold for two independently quantised universes, whose generators add without cancelling (Q3).
6. **Test field only.** The gravitational field is fixed and the same for both members. The back-reaction through the field equations for $a_4$ is not part of the theorems. The only statement about it is the corollary C1 of Chapter 20: a T1 pair taken as the complete classical source of the author's metric is a zero source, and the Einstein equations then have no solution for $H > 0$. That is a statement about sources in one common geometry, not a derivation that the geometry, or the pair, is created.
7. **The Z2 brane is assumed.** The mirror across $z = \pi/2$ uses the ASSUMED Z2 construction; the metric is degenerate there ($g_{88} = 0$ and $\sqrt{|g|} = 0$), and no junction condition, brane tension or matching of the field across the brane is derived.
8. **Quantum positivity is not established.** Every real-frequency eigenspace of the one-particle matrix has the Krein inertia (4,4), and the growing waves are Krein-neutral (Q4); a positive-norm Fock space for either universe is not established by these theorems.
9. **dirac16complex00 is a classical field**: no quantum statement is made for it.
10. **The Kohn-Sham level is separate.** Theorem T3 is proved in Chapter 19 with its own hypotheses (the ASSUMED Z2 brane, instantaneous mean-field Kohn-Sham states); nothing in this chapter establishes it.

**The author's hypothesis.** The statement that the big bang CREATES universes in pairs of masses $+m$ and $-m$ is the author's HYPOTHESIS. This chapter proves that the solutions come in partnered families (T1 and T2) and how a quantised partner must be read (Q); it does not prove, and the equations of this book cannot prove, that any universe is created, in pairs or otherwise. Chapter 20 takes up the question "Do universes come in pairs?" and states the hypothesis as a hypothesis.

**Matter and antimatter.** Where this chapter touches matter and antimatter, the exact statements are these. The charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ of a slice $x_4 = \mathrm{const}$ is exactly conserved on shell, an exact U(1) symmetry (`charge-conjugation-and-u1.json`, check `u1_noether_matrix_identity`; Notebook 18c checks the local conservation law along its solution, In [10]); so no net charge can be generated inside one universe. A T1 partner carries the opposite charge, so a T1 pair has total charge zero as classical bilinears (T1d); this is a universe and anti-universe statement about solutions. Such ideas form a class in the published literature; one example is L. Boyle, K. Finn and N. Turok, "CPT-Symmetric Universe", Phys. Rev. Lett. 121, 251301 (2018); it is cited only as an example of the class, and nothing in this chapter is taken from it. On real fields T1 is the mass-reversing charge conjugation by the matrix $\Gamma$ (Section 18.13). The theory as built does NOT solve the matter-antimatter problem. In 1967 Sakharov showed that an excess of matter can grow from an equal start only if three conditions hold: a process that changes the baryon number, a violation of the symmetries C and CP, and a departure from thermal equilibrium (Chapter 21). The theory as built has no baryons, no process that changes the baryon number (its charge is exactly conserved), no violation of CP built in or computed, and no computation of a departure from thermal equilibrium. To solve the problem it would need all of these, and a computed excess of matter that agrees with the measured one. Every scenario in which our universe is one member of such a pair, or in which the pairing explains the excess of matter, is a HYPOTHESIS. Chapter 21 treats matter and antimatter from zero.

### 18.29 What we proved, what we computed, what we assumed

**Proved.** Exactly, for both fields unless something else is said, each with the Revision record that verifies it and the notebook of this chapter that reproduces it:

| statement | where it is verified | notebook |
| --- | --- | --- |
| the gammas of the record are the author's eight real $16 \times 16$ signed permutation matrices, rebuilt from his formulas | `python-pairing.json`, check `gammas.equal_wolfram_fixture` | 18a |
| $\sqrt{\lvert g\rvert} = \cos z$; the 12 components of the canonical spin connection; $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ for every history $a_4$ (the deflation terms cancel), $-3H\gamma^{(x_8)}$ on the mirror patch | `wolfram-pairing.json`, check `primordial_vielbein`; `python-pairing.json`, check `geometry.spin_connection_components`; `python-field-theory.json`, checks `gamma_mu_Omega_mu_equals_3H_gamma_x8` and `divergence_of_sqrtg_gamma` | 18b, 18c |
| Lemma 1: $\Gamma$ real, symmetric, $\Gamma\Gamma = 1$, anticommuting with every gamma, commuting with $C$ and every $S^{ab}$ | `wolfram-pairing.json`, check `Gamma_properties`; `python-pairing.json`, checks `gammas.Gamma` and `gammas.Gamma_anticommutes` | 18a |
| Lemma 2: $\bar\Psi X\Psi \to (-1)^k\bar\Psi X\Psi$ under $\Psi \to \Gamma\Psi$; $\Gamma B\Gamma = -B$ | `wolfram-pairing.json`, checks `T1_kernel_scalar`, `T1_kernel_kinetic`, `T1_kernel_connection` and `T1_kernel_field_equation`; `python-pairing.json`, checks `T1.general_field.matrix_identities` and `Q.image_krein_metric` | 18a |
| Lemma 3: the eight reflections $P_n$ in Pin(4,4), their characters $-\eta_{nn}$, the reflection table | `wolfram-pairing.json`, checks `T2_Pn_in_Pin44`, `T2_Pn_covers_the_reflection`, `T2_character_of_Pn` and `T2_Gamma_times_Pn_is_gamma_n`; `python-pairing.json`, checks `T2.general_field.reflection_table` and `compare.theory.reflection_table` | 18a |
| Lemma 4: the 17 Krein signs | `wolfram-pairing.json`, check `Q_Krein_metric_of_images`; `python-pairing.json`, check `compare.theory.krein_signs` | 18a |
| T1 (T1a to T1d), in every gravitational field taken as a fixed background, both statistics | `wolfram-pairing.json`, the 51 checks of T1; `python-pairing.json`, the 23 checks whose names begin with `T1.`, and `compare.theory.theorem_T1` | 18b, 18c |
| T2 (T2a to T2d); the author's-field version under the ASSUMED Z2 construction | `wolfram-pairing.json`, the 28 checks of T2; `python-pairing.json`, the 16 checks of T2 and `compare.theory.theorem_T2` | 18b, 18c |
| Q1 to Q5, for the canonically quantised dirac16complex | `wolfram-pairing.json`, the 12 checks whose names begin with `Q_`; `python-pairing.json`, the 10 checks whose names begin with `Q.`, and `compare.theory.theorem_Q` | 18a, 18c |
| the homogeneous solutions: $S$ constant, $M^2 = (9H^2 - (m + \lambda S)^2)I_{16}$, the exact formula; $\rho = mS + \frac{\lambda}{2}S^2$, every pressure $\frac{\lambda}{2}S^2$, $T_{x_4x_8} = 0$; the conservation of the charge | `python-field-theory.json`, checks `exact_nonlinear_homogeneous_solution`, `commuting_homogeneous_on_shell_rho_p`, `commuting_T_x4x8_homogeneous` and `commuting_current_conservation`; `wolfram-field-theory.json`, check `exact_solution_nonlinear_homogeneous_C` | 18c |
| the two charge-conjugation matrices $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$; on real fields T1 is the mass-reversing conjugation by $\Gamma$; the exact U(1) conservation of the charge | `charge-conjugation-and-u1.json`, checks `intertwiners_same_mass`, `intertwiners_reversed_mass`, `charge_conjugation_matrix_plus`, `charge_conjugation_matrix_minus`, `real_fields_charge_conjugation` and `u1_noether_matrix_identity` | none (Chapters 5 and 21) |

**Computed.** Numerical results of the notebooks, with their accuracy:

- Notebook 18a: every result is exact whole-number arithmetic, except the illustration of In [7], where $\Gamma$ commutes with a random connection to below $10^{-12}$.
- Notebook 18b: every result is exact (sympy). The monomial counts, evaluated at one sample point, are 408 (commuting) and 392 (Grassmann) for the Lagrangian, equal to the counts recorded by the Wolfram verifier, and 376 (diagonal) or 64 and 80 (off-diagonal) for the components of $T_{\mu\nu}$; they describe the size of the polynomials and prove nothing.
- Notebook 18c (illustrative values $m = 1$, $H = 0.2$, $\lambda = 0.3$, $z_0 = \pi/4$, seed 2026; history $A = 1$ from the record): $S = 0.897319$, $m + \lambda S = 1.269196$, $w = 1.118417$; Runge-Kutta errors at $x_4 = 20$ for 250 to 4000 steps from $2.0 \times 10^{-5}$ to $2.6 \times 10^{-10}$, measured orders 4.10, 4.06, 4.03 and 4.01, largest error with 2000 steps $4.3 \times 10^{-9}$ against the exact formula of the record; the T1 partner equals $\Gamma\Psi$ and the T2 partner equals $\gamma^{(x_8)}\Psi$ to below $10^{-12}$ at all 2001 times, while the wrong partner $(-m, +\lambda)$ is off by 1.641; $S$, $J^\mu$ and $T_{\mu\nu}$ of the partners as predicted, to a relative $10^{-12}$ at 101 sampled times; the eight plane-wave samples of the record reproduced (dimensions 8 and 8, Krein inertia (4,4)); the plane-wave spectra of the masses $\pm1$ equal to $10^{-6}$ at 121 momenta (away from $k_5 = 1$); the Krein norms $\pm1$ of the 16 modes of the first sample reversed by $\Gamma$ and kept by $\gamma^{(x_8)}$.

**Assumed.**

- The gravitational field is a fixed background (a test field) in every theorem of this chapter: it is not varied, and both members of a pair live in the same field.
- The Z2 mirror construction: gluing the mirror patch to the patch at the degenerate brane $z = \pi/2$; it enters T2 in the author's field, the mirror universe of Q5 and the mirror partner of Notebook 18c (`pairing-theory.json`, theorem T2, its hypothesis on the primordial field).
- For Q: the canonical quantisation of dirac16complex with $x_4$ as the time and with anticommutators (part of its definition as a fermion field); flat 4+4 space, or frozen coefficients at one point, for the one-particle statements.
- The history $a_4 = AHx_4$ with $A = 1$ used in the figures is the PRESCRIBED BACKGROUND of the Revision Kohn-Sham record (`parameters.json`; `ks-source-conditions.json`, check `ks_history_is_a_prescribed_background`). The theorems themselves hold for every history.
- The value $3H\gamma^{(x_8)}$ of $\gamma^\mu\Omega_\mu$ belongs to the diagonal vielbein (`python-scope.json`; Chapter 8); none of the theorems depends on it.
- The illustrative values of Notebook 18c.

**Hypothesis.**

- That the big bang creates universes in pairs of masses $+m$ and $-m$: the author's HYPOTHESIS, not derived from any equation of this book.
- That our universe has an anti-universe partner, or that the pairing explains the observed excess of matter over antimatter.

**Open.**

- Any creation process, rate or amplitude for universes, which these equations do not contain.
- The gravitational back-reaction of a pair: the pair as part of the source of the field equations for $a_4$ (C1 treats only the case in which a T1 pair is the complete source).
- A junction condition at the brane $z = \pi/2$ that would replace the assumed Z2 construction.
- A positive Hilbert space for the whole quantised field (all momenta, the curved metric), and the fate of the growing extra-time waves.

### 18.30 Exercises

**Exercise 18.1.** The factors of $\Gamma$ are $\gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}\gamma^{(x_4)}\gamma^{(x_5)}\gamma^{(x_6)}\gamma^{(x_7)}$, in this order. Use Rule P (Section 18.5) to write $P_n = \Gamma\gamma^{(n)}$ as a sign times the product of the seven other gammas in the order of $\Gamma$, for $n = x_1$, $x_4$, $x_5$ and $x_8$. Find the general rule for the sign and check it against all eight signs $+1, -1, +1, +1, -1, +1, -1, -1$ of the record.

**Exercise 18.2.** Notebook 18c has $S = 0.897319$, $m = 1$ and $\lambda = 0.3$ (Out [4]). For homogeneous solutions the record gives $\rho = mS + \frac{\lambda}{2}S^2$ and $p = \frac{\lambda}{2}S^2$ in every direction. (a) Compute $\rho$, $p$ and the equation of state $w = p/\rho$ of the solution, and compare $w$ with the formula $w = \lambda S/(2m + \lambda S)$ of the record. (b) The same for the T1 partner ($-m$, $-\lambda$, the same $S$). (c) The same for the T2 partner ($-m$, $\lambda$, the scalar $-S$). (d) Add the energy densities of each pair.

**Exercise 18.3.** (a) With $m + \lambda S = 1.269196$ and $3H = 0.6$, compute the frequency $w$ of the solution of Notebook 18c, the period of the field and the period of its charge density $J^{x_4}$, and the number of oscillations of $J^{x_4}$ between $x_4 = 0$ and 20 (Figure 18c.3). (b) Compute the coefficient $V$, the frequency and the period of the wrong partner $(-m, +\lambda)$ started from $\Gamma\Psi(0)$ (Figure 18c.2). (c) For which masses $m$ (at the same $\lambda$ and $S$) do the homogeneous solutions grow instead of oscillating, and what is the largest growth rate (Figure 18c.5)?

**Exercise 18.4.** (a) From $C\gamma^{(a)}C^{-1} = -(\gamma^{(a)})^T$ show that $(S^{ab})^TC = -CS^{ab}$ for $a \neq b$. (b) Conclude that $\Omega_\mu^TC = -C\Omega_\mu$ for every real connection, and that $D_\mu\bar\Psi = (D_\mu\Psi)^\dagger C$, the formula used by Notebook 18c in In [9].

**Exercise 18.5.** Show that $Bh_m(k) = h_m(k)^\dagger B$ for real $m$ and real momenta $k$, with $h_m(k) = -im\gamma^{(x_4)} - \gamma^{(x_4)}K$, $K = \sum_{a\neq4}k_a\gamma^{(a)}$ and $B = -iC\gamma^{(x_4)}$. Use only the reality of the gammas, $(\gamma^{(a)})^T = \eta_{aa}\gamma^{(a)}$, the Clifford relation and $C\gamma^{(a)}C^{-1} = -(\gamma^{(a)})^T$.

**Exercise 18.6.** Let $h_m(k)u = wu$ with a real $w$ and the Krein norm $u^\dagger Bu = 1$. (a) Show that $\Gamma u$ is an eigenvector of $h_{-m}(k)$ with the same $w$ and the Krein norm $-1$. (b) Show that $\gamma^{(x_8)}u$ is an eigenvector of $h_{-m}(R_8k)$ with the same $w$ and the Krein norm $+1$. (c) Which bars of Figure 18c.7 show (a) and (b)?

**Exercise 18.7.** Write $\mathcal{L}_{m,\lambda}[\Psi] = \sqrt{|g|}\,[K - mS - \frac{\lambda}{2}S^2]$. (a) Compute $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{m,\lambda}[\Psi]$, $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{-m,\lambda}[\Psi]$ and $\mathcal{L}_{m,\lambda}[\Gamma\Psi] + \mathcal{L}_{-m,-\lambda}[\Psi]$. (b) Which terms survive in each, and which bars of Figure 18b.2 show it? (c) For which $\lambda$ is T1 a pure $+m$ / $-m$ pairing?

**Exercise 18.8.** (a) Compute $\sin^{1/6}z$, $f_8$ and $\sqrt{|g|}$ at $z = \pi/4$ on the patch and at $z = 3\pi/4$ on the mirror patch, and check that the metric takes the same values at the two points. (b) Use the divergence form of Section 18.27 to compute the coefficient of $\gamma^{(x_8)}$ in $\gamma^\mu\Omega_\mu$ on the mirror patch, with $H = 0.2$. (c) Pull the hidden leg $e^8 = f_8\,dx_8$ of the mirror patch back by $\phi$: $x_8 \to \pi/(6H) - x_8$, and say which frame reflection results.

**Exercise 18.9.** A student writes: "Theorem T1 proves that the big bang creates every universe of mass $m$ together with a universe of mass $-m$: the two have opposite energies, so the pair costs no energy, and nothing forbids it." Name every step of this sentence that the equations of this book do not establish, and say what they do establish instead.

### 18.31 Answers to the exercises

**Answer 18.1.** Write $\gamma^{(a)}$ as $\gamma_a$ for short. For $n = x_1$: $\Gamma\gamma_1 = \gamma_8\gamma_1\gamma_2\gamma_3\gamma_4\gamma_5\gamma_6\gamma_7\gamma_1$. Move the last $\gamma_1$ to the left past $\gamma_7, \gamma_6, \gamma_5, \gamma_4, \gamma_3, \gamma_2$: six different gammas, each exchange costs $-1$ (Rule P), so the sign is $(-1)^6 = +1$, and $\Gamma\gamma_1 = \gamma_8\gamma_1\gamma_1\gamma_2\gamma_3\gamma_4\gamma_5\gamma_6\gamma_7$. Then $\gamma_1\gamma_1 = \eta_{11} = +1$ (Clifford relation): $P_{x_1} = +\gamma_8\gamma_2\gamma_3\gamma_4\gamma_5\gamma_6\gamma_7$, sign $+1$. For $n = x_4$: three exchanges (past $\gamma_7, \gamma_6, \gamma_5$), $(-1)^3 = -1$, then $\gamma_4\gamma_4 = \eta_{44} = -1$: the sign is $(-1)(-1) = +1$. For $n = x_5$: two exchanges, $(+1)$, then $\eta_{55} = -1$: the sign is $-1$. For $n = x_8$: seven exchanges (past $\gamma_7, \dots, \gamma_1$), $(-1)^7 = -1$, then $\eta_{88} = +1$: the sign is $-1$, $P_{x_8} = -\gamma_1\gamma_2\cdots\gamma_7$. General rule: the sign is $(-1)^{N_n}\eta_{nn}$, where $N_n$ is the number of factors that stand to the right of $\gamma^{(n)}$ in $\Gamma$. With $N = 6, 5, 4, 3, 2, 1, 0, 7$ for $x_1, \dots, x_8$ and $\eta = (+1, +1, +1, -1, -1, -1, -1, +1)$: $x_1$: $+1$; $x_2$: $(-1)^5 = -1$; $x_3$: $+1$; $x_4$: $(-1)^3(-1) = +1$; $x_5$: $(+1)(-1) = -1$; $x_6$: $(-1)(-1) = +1$; $x_7$: $(+1)(-1) = -1$; $x_8$: $-1$. These are the eight signs of the record (data table `reflections` of `pairing-theory.json`; Notebook 18a, Out [12]).

**Answer 18.2.** $S^2 = 0.897319^2 = 0.805181$. (a) $p = \frac{0.3}{2} \times 0.805181 = 0.120777$; $\rho = 1 \times 0.897319 + 0.120777 = 1.018096$; $w = 0.120777/1.018096 = 0.11863$. The record's formula: $\lambda S/(2m + \lambda S) = 0.269196/2.269196 = 0.11863$, the same, as it must be: dividing $p$ and $\rho$ by $S/2$ gives $w = \lambda S/(2m + \lambda S)$. (b) With $-m$ and $-\lambda$ and the same $S$: $\rho' = -mS - \frac{\lambda}{2}S^2 = -1.018096$ and $p' = -\frac{\lambda}{2}S^2 = -0.120777$ (for $U = -\frac{\lambda}{2}S^2$, $p' = SU' - U = -\lambda S^2 + \frac{\lambda}{2}S^2$); $w' = p'/\rho' = 0.11863$, the same equation of state, as T1 says (Section 18.13). (c) With $-m$, $\lambda$ and the scalar $-S$: $\rho'' = (-m)(-S) + \frac{\lambda}{2}(-S)^2 = 1.018096$ and $p'' = \frac{\lambda}{2}S^2 = 0.120777$: equal to those of the solution. (d) $\rho + \rho' = 0$: the T1 pair has zero total energy density as classical bilinears. $\rho + \rho'' = 2.036192$: nothing cancels in a T2 pair.

**Answer 18.3.** (a) $w^2 = 1.269196^2 - 0.6^2 = 1.610858 - 0.36 = 1.250858$, so $w = 1.11842$ (Out [14] prints 1.118417, computed with the unrounded $S$). The field oscillates with the period $2\pi/w = 5.618$. $J^{x_4} = \Psi^\dagger B\Psi$ is quadratic in $\Psi = \cos(wx_4)\Psi(0) + \frac{\sin(wx_4)}{w}M\Psi(0)$, so it contains $\cos^2$, $\sin^2$ and $\sin\cos$, which are combinations of 1, $\cos(2wx_4)$ and $\sin(2wx_4)$: its period is $\pi/w = 2.809$, and $20/2.809 = 7.1$, so seven full oscillations, as in Figure 18c.3. (b) $S[\Gamma\Psi] = S$, so $V = -m + \lambda S = -1 + 0.269196 = -0.730804$; $w^2 = 0.534075 - 0.36 = 0.174075$, $w = 0.41722$, period $2\pi/0.41722 = 15.06$: in Figure 18c.2 the dashed curve completes about $20/15.06 = 1.3$ oscillations. (c) The solutions grow when $(m + \lambda S)^2 < 9H^2$, that is $-0.6 < m + 0.269196 < 0.6$, or $-0.869196 < m < 0.330804$. There $M^2 = (9H^2 - V^2)I_{16}$ is positive, the eigenvalues are $\pm\kappa$ with $\kappa = \sqrt{9H^2 - V^2}$, and the largest growth rate is $3H = 0.6$, at $V = 0$, that is $m = -0.269196$: the top of the arc in Figure 18c.5.

**Answer 18.4.** (a) The given relation, solved for the transpose: $(\gamma^{(a)})^T = -C\gamma^{(a)}C^{-1}$. For $a \neq b$, $S^{ab} = \frac12\gamma^{(a)}\gamma^{(b)}$ and

$$
\begin{aligned}
(S^{ab})^T &= \tfrac12(\gamma^{(b)})^T(\gamma^{(a)})^T = \tfrac12\big(-C\gamma^{(b)}C^{-1}\big)\big(-C\gamma^{(a)}C^{-1}\big) \\
&= \tfrac12C\gamma^{(b)}\gamma^{(a)}C^{-1} = -\tfrac12C\gamma^{(a)}\gamma^{(b)}C^{-1} = -CS^{ab}C^{-1} .
\end{aligned}
$$

The transpose of a product reverses the order; the two minus signs multiply to $+1$; $C^{-1}C = 1$; two different gammas anticommute. Multiplying on the right by $C$ gives $(S^{ab})^TC = -CS^{ab}$. (b) $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$ with real numbers $\omega_{\mu ab}$; transposing is linear, so $\Omega_\mu^TC = \frac12\sum\omega_{\mu ab}(S^{ab})^TC = -C\Omega_\mu$. Then, with $C$ constant and $\Omega_\mu^\dagger = \Omega_\mu^T$ (real),

$$
(D_\mu\Psi)^\dagger C = (\partial_\mu\Psi)^\dagger C + \Psi^\dagger\Omega_\mu^TC = \partial_\mu(\Psi^\dagger C) - \Psi^\dagger C\Omega_\mu = \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu = D_\mu\bar\Psi .
$$

**Answer 18.5.** Step 1, the adjoint of $h$. The gammas are real, so $(\gamma^{(a)})^\dagger = (\gamma^{(a)})^T = \eta_{aa}\gamma^{(a)}$; in particular $(\gamma^{(x_4)})^\dagger = -\gamma^{(x_4)}$. Write $\tilde K = K^\dagger = \sum_{a\neq4}k_a\eta_{aa}\gamma^{(a)}$ ($k_a$ real). With $(XY)^\dagger = Y^\dagger X^\dagger$ and $(-i)^* = i$:

$$
h^\dagger = im(\gamma^{(x_4)})^\dagger - K^\dagger(\gamma^{(x_4)})^\dagger = -im\gamma^{(x_4)} + \tilde K\gamma^{(x_4)} .
$$

Step 2, two facts about $C$. From $C\gamma^{(a)}C^{-1} = -(\gamma^{(a)})^T = -\eta_{aa}\gamma^{(a)}$: for $a = 4$ ($\eta_{44} = -1$), $C$ commutes with $\gamma^{(x_4)}$; and summing with the coefficients $k_a$, $CKC^{-1} = -\tilde K$, that is $CK = -\tilde KC$. Step 3, the two products, using $\gamma^{(x_4)}\gamma^{(x_4)} = -1$:

$$
Bh = -iC\gamma^{(x_4)}\big(-im\gamma^{(x_4)} - \gamma^{(x_4)}K\big) = (-i)(-i)m\,C\gamma^{(x_4)}\gamma^{(x_4)} + iC\gamma^{(x_4)}\gamma^{(x_4)}K = mC - iCK ,
$$

$$
h^\dagger B = \big(-im\gamma^{(x_4)} + \tilde K\gamma^{(x_4)}\big)(-iC\gamma^{(x_4)}) = -m\,\gamma^{(x_4)}C\gamma^{(x_4)} - i\tilde K\gamma^{(x_4)}C\gamma^{(x_4)} = mC + i\tilde KC .
$$

In the second line $\gamma^{(x_4)}C\gamma^{(x_4)} = C\gamma^{(x_4)}\gamma^{(x_4)} = -C$ (Step 2). By Step 2, $-iCK = i\tilde KC$, so $Bh = h^\dagger B$. (The result $Bh = mC - iCK$ is the energy kernel $\mathcal{E}_m(k)$ of Section 18.23, which the sympy record writes as $m\,C - i\,k_aC\gamma^{(a)}$.)

**Answer 18.6.** (a) By Q4, $\Gamma h_m(k)\Gamma = h_{-m}(k)$, and $\Gamma\Gamma = 1$, so $h_{-m}(k)\Gamma u = \Gamma h_m(k)\Gamma\Gamma u = \Gamma h_m(k)u = w\,\Gamma u$. The Krein norm: $(\Gamma u)^\dagger B(\Gamma u) = u^\dagger\Gamma^\dagger B\Gamma u = u^\dagger\Gamma B\Gamma u = -u^\dagger Bu = -1$, because $\Gamma$ is real and symmetric ($\Gamma^\dagger = \Gamma$) and $\Gamma B\Gamma = -B$ (Lemma 2). (b) By Q4, $\gamma^{(x_8)}h_m(k)\gamma^{(x_8)} = h_{-m}(R_8k)$, and $\gamma^{(x_8)}\gamma^{(x_8)} = \eta_{88} = 1$, so $h_{-m}(R_8k)\gamma^{(x_8)}u = \gamma^{(x_8)}h_m(k)u = w\,\gamma^{(x_8)}u$. $\gamma^{(x_8)}$ is real and symmetric (space-like), so $(\gamma^{(x_8)}u)^\dagger B(\gamma^{(x_8)}u) = u^\dagger\gamma^{(x_8)}B\gamma^{(x_8)}u = u^\dagger Bu = 1$ by Lemma 4 ($\sigma_{\gamma^{(x_8)}} = +1$). (c) In Figure 18c.7 every orange bar ($\Gamma u$) is the blue bar ($u$) turned upside down, which is (a), and every green bar ($\gamma^{(x_8)}u$) equals the blue bar, which is (b).

**Answer 18.7.** (a) By T1, $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = \sqrt{|g|}\,[-K - mS - \frac{\lambda}{2}S^2]$ ($K$ reversed, $S$ kept). Adding $\mathcal{L}_{m,\lambda}[\Psi] = \sqrt{|g|}\,[K - mS - \frac{\lambda}{2}S^2]$ gives $-\sqrt{|g|}\,(2mS + \lambda S^2)$. Adding $\mathcal{L}_{-m,\lambda}[\Psi] = \sqrt{|g|}\,[K + mS - \frac{\lambda}{2}S^2]$ gives $-\sqrt{|g|}\,\lambda S^2$. Adding $\mathcal{L}_{-m,-\lambda}[\Psi] = \sqrt{|g|}\,[K + mS + \frac{\lambda}{2}S^2]$ gives 0. (b) In the first sum the kinetic terms cancel and the mass term and the $S^2$ term survive: the fourth pair of bars of Figure 18b.2. In the second only the $S^2$ term survives: the fifth pair, the shortest nonzero bars. The third sum is the zero bar of T1. (c) For $\lambda = 0$ the second sum vanishes, and T1 pairs $(m, 0)$ with $(-m, 0)$: a pure $+m$ / $-m$ pairing of free fields.

**Answer 18.8.** (a) $\sin(\pi/4) = \sin(3\pi/4) = 1/\sqrt2 = 0.707107$, so $\sin^{1/6}z = 2^{-1/12} = 0.943874$ at both points, and the components $e^{\pm2a_4}\sin^{1/3}z$ are equal. On the patch $f_8 = \cot(\pi/4) = 1$; on the mirror patch $f_8 = -\cot(3\pi/4) = -(-1) = 1$; so $g_{88} = f_8^2 = 1$ at both. $\sqrt{|g|} = \cos(\pi/4) = 0.707107$ on the patch and $-\cos(3\pi/4) = 0.707107$ on the mirror patch. The metric takes the same values: the mirror is an isometry. (b) On the mirror patch $\sqrt{|g|}/f_8 = (-\cos z)/(-\cot z) = \sin z$, whose derivative along $x_8$ is $6H\cos z$; divided by $2\sqrt{|g|} = -2\cos z$ this gives $-3H = -0.6$. (c) At the image point the hidden leg is $-\cot(\pi - z)\,d\big(\frac{\pi}{6H} - x_8\big) = \cot z\,(-dx_8) = -\cot z\,dx_8 = -e^8$, because $\cot(\pi - z) = -\cot z$ and $d(\mathrm{const} - x_8) = -dx_8$. The other seven legs are unchanged, so the pulled-back frame is the original frame with the direction $x_8$ reflected, $R_8e$ (Section 18.16).

**Answer 18.9.** Step by step. "Theorem T1 proves that the big bang creates": no. T1 maps the solutions of the theory $(m, \lambda)$ onto those of $(-m, -\lambda)$; no equation of this book describes the creation of a universe, in pairs or otherwise, and no process, rate, probability or amplitude follows (Section 18.28, items 1 and 2). "every universe of mass $m$ together with a universe of mass $-m$": no. A universe of mass $m$ is an equally valid solution without any partner (item 3), and the T1 partner has the coupling $-\lambda$, so for $\lambda \neq 0$ it is not merely a universe of mass $-m$ (item 4). "the two have opposite energies": true for the classical bilinears of a configuration and its image, and as an operator identity within one quantum system (T1c, Q2); false for two independently quantised universes, whose energies add without cancelling (Q3; item 5). "so the pair costs no energy": the theorems contain no energy balance of a creation process; the only statement about the pair as a source of gravity is the corollary C1 of Chapter 20, which says that a T1 pair taken as the complete source of the author's metric is a zero source, for which the Einstein equations have no solution with $H > 0$ (item 6). "and nothing forbids it": not established either way; the equations neither forbid nor produce it. What the equations do establish: the exact maps T1 and T2 between solution sets, with their signs, and the quantum reading Q. That the big bang creates universes in pairs remains the author's HYPOTHESIS.
