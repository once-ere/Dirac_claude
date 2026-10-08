## 18. The pairing theorems T1, T2 and Q

The author asked for a proof that "Universes of masses {+mass, -mass} are created in pairs", for the fermion field dirac16complex and for the commuting field dirac16complex00. This chapter gives, with complete line-by-line proofs, everything that the equations of this book actually establish about such pairs, and it says exactly where that stops. Three theorems are proved. **T1** (the chirality pairing): multiplying a field by the chirality matrix $\Gamma$ turns every configuration of the theory with mass $m$ and coupling $\lambda$ into a configuration of the theory with $-m$ and $-\lambda$, in every gravitational field, and reverses its energy, momentum, stresses, current and charge. **T2** (the mirror pairing): multiplying by the gamma matrix of the hidden direction and reflecting the hidden coordinate across the surface $z = \pi/2$ turns a solution with $(-m, \lambda)$ into a solution with $(m, \lambda)$ at EQUAL, not opposite, energy and charge; this uses the Z2 mirror construction, which is an assumption. **Q** (the quantum reading): for the quantised field dirac16complex the T1 image carries the opposite Krein matrix $-B$, so it is the same quantum system relabelled, while two independently quantised universes of masses $+m$ and $-m$ have identical one-particle spectra and energies that do not cancel. All three are exact maps between sets of solutions. None of them describes a process in which a universe, or a pair of universes, comes into being: no creation process, rate, probability or amplitude follows from these equations. Section 18.28 lists precisely what is not established.

### 18.1 What this chapter does

**The question, and the honest answer.** In this book a **universe of mass $m$** means a configuration of one of the two fields, with mass parameter $m$ and coupling $\lambda$, in the author's primordial gravitational field; usually it is a **solution**, a configuration that obeys the field equations. Two universes are **paired** when an explicit invertible rule takes every solution of the theory with mass $m$ to a solution of the theory with mass $-m$, and takes its Lagrangian, its energy-momentum tensor and its current to stated multiples of those of the partner. The author's request asks for more: that such universes are *created* in pairs at the big bang. That statement is a HYPOTHESIS of the author. The field equations of this book are equations for a field on a given gravitational background, together with their canonical quantisation; no equation of the book produces a universe from anything, so the creation of pairs cannot be proved from them, and it is not proved here. What can be proved is that the solutions come in partnered families, and with which signs their energies and charges are partnered. That is the content of this chapter.

**The plan.** Sections 18.2 to 18.4 set the stage: the words, the author's metric, its spin connection, the Lagrangian, the field equation, the energy-momentum tensor and the current. Section 18.5 proves four matrix lemmas; everything later rests on them. Notebook 18a checks them exactly (Sections 18.6 to 18.9). Sections 18.10 to 18.13 state and prove T1; Sections 18.14 to 18.16 state and prove T2. Notebook 18b proves both theorems again, as exact polynomial identities, in the author's metric with an arbitrary deflating history (Sections 18.17 to 18.20). Section 18.21 derives a family of exact solutions, the fields that depend only on the time; Sections 18.22 and 18.23 state and prove Q. Notebook 18c solves the field equations numerically and shows each theorem at work on actual solutions (Sections 18.24 to 18.27). Section 18.28 states what is not established, Section 18.29 collects the status of every result, and Section 18.30 has exercises with complete answers. The Kohn-Sham version of the pairing, theorem T3, is the subject of Chapter 19; the corollary C1 and the question of the title of Chapter 20, "Do universes come in pairs?", are treated there; matter and antimatter are the subject of Chapter 21.

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

The constant $\Gamma$ passes through $\partial_\mu$ (a constant factor comes out of a derivative), and $\Omega_\mu\Gamma = \Gamma\Omega_\mu$. The adjoint statement is the same computation from the right. QED. PROVED: `wolfram-pairing.json`, check `Gamma_properties`; `python-pairing.json`, checks `gammas.Gamma` and `gammas.Gamma_anticommutes`; Notebook 18a, In [6] and In [7].

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

The definition $B = -iC\gamma^{(x_4)}$; then $\Gamma C = C\Gamma$; then the line before with $k = 1$. QED. Nowhere were two field components exchanged: only the numbers of the matrices were moved, and every $\Psi^*$ still stands to the left of every $\Psi$. So Lemma 2 holds for commuting and for Grassmann components alike. PROVED: `wolfram-pairing.json`, checks `T1_kernel_scalar`, `T1_kernel_kinetic`, `T1_kernel_connection` (all 512 triples $(a, b, c)$), `T1_kernel_field_equation`, `Q_Krein_metric_of_images`; `python-pairing.json`, checks `T1.general_field.matrix_identities` (all 456 kinetic and connection kernels) and `Q.image_krein_metric`; Notebook 18a, In [9] and In [10] (all 256 products of different gammas).

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

We used $\Gamma C\Gamma = C\Gamma\Gamma = C$ (Lemma 1) and item 1. Finally $\Gamma P_n = \Gamma\Gamma\gamma^{(n)} = \gamma^{(n)}$. QED. The signs of $P_n$ relative to the product of the other seven gammas, in the order of $\Gamma$, are $+1, -1, +1, +1, -1, +1, -1, -1$ for $n = x_1, \dots, x_8$ (computed exactly; record data table `reflections` of `pairing-theory.json`). PROVED: `wolfram-pairing.json`, checks `T2_Pn_in_Pin44`, `T2_Pn_covers_the_reflection`, `T2_character_of_Pn`, `T2_Gamma_times_Pn_is_gamma_n`, `T2_kernels_gamma_n_with_frame_reflection`; `python-pairing.json`, checks `T2.general_field.matrix_identities`, `T2.general_field.reflection_table`, `compare.theory.reflection_table`; Notebook 18a, In [12] and In [13].

**Lemma 4 (the Krein signs of the maps).** $MBM^\dagger = \sigma_MB$, with $\sigma_\Gamma = -1$; $\sigma_{\gamma^{(n)}} = +1$ for $n = x_1, x_2, x_3, x_4, x_8$ and $-1$ for $n = x_5, x_6, x_7$; and $\sigma_{P_n} = -\sigma_{\gamma^{(n)}}$.

*Proof.* $\Gamma$ is real and symmetric, so $\Gamma B\Gamma^\dagger = \Gamma B\Gamma = -B$ by Lemma 2. For $M = \gamma^{(n)}$: transposing $C\gamma^{(n)}C^{-1} = -(\gamma^{(n)})^T$ and using $C^T = C = C^{-1}$ gives $\gamma^{(n)}C = -C(\gamma^{(n)})^T$. Then

$$
\begin{aligned}
\gamma^{(n)}B(\gamma^{(n)})^\dagger &= -i\,\gamma^{(n)}C\gamma^{(x_4)}(\gamma^{(n)})^T = i\,C(\gamma^{(n)})^T\gamma^{(x_4)}(\gamma^{(n)})^T \\
&= i\,\eta_{nn}^2\,C\gamma^{(n)}\gamma^{(x_4)}\gamma^{(n)} = i\,C\gamma^{(n)}\gamma^{(x_4)}\gamma^{(n)} .
\end{aligned}
$$

The definition of $B$ and $(\gamma^{(n)})^\dagger = (\gamma^{(n)})^T$ (real matrix); then the relation $\gamma^{(n)}C = -C(\gamma^{(n)})^T$; then $(\gamma^{(n)})^T = \eta_{nn}\gamma^{(n)}$ twice; then $\eta_{nn}^2 = 1$. For $n \neq 4$: $\gamma^{(n)}\gamma^{(x_4)}\gamma^{(n)} = -\gamma^{(x_4)}\gamma^{(n)}\gamma^{(n)} = -\eta_{nn}\gamma^{(x_4)}$, so the result is $-i\eta_{nn}C\gamma^{(x_4)} = \eta_{nn}B$: $+B$ for $x_1, x_2, x_3, x_8$ and $-B$ for $x_5, x_6, x_7$. For $n = 4$: $\gamma^{(4)}\gamma^{(4)}\gamma^{(4)} = -\gamma^{(4)}$, so the result is $-iC\gamma^{(4)} = +B$. For $P_n = \Gamma\gamma^{(n)}$: $P_nBP_n^\dagger = \Gamma\,\gamma^{(n)}B(\gamma^{(n)})^\dagger\,\Gamma = \sigma_{\gamma^{(n)}}\Gamma B\Gamma = -\sigma_{\gamma^{(n)}}B$. QED. PROVED: `wolfram-pairing.json`, check `Q_Krein_metric_of_images`; `python-pairing.json`, checks `compare.theory.krein_signs` and `Q.T2_image_keeps_B`; the 17 signs equal the data table `Krein_signs_M_B_Mdagger` of `pairing-theory.json` (Notebook 18a, In [17]).

**The block form.** Split $\Psi = (\psi_-, \psi_+)$ into its components 1 to 8 and 9 to 16. Because every gamma anticommutes with $\Gamma = \mathrm{diag}(-I_8, I_8)$, every gamma has nonzero entries only in the two off-diagonal $8 \times 8$ blocks (Chapter 5): it exchanges the two halves. The author's $\gamma^{(x_8)}$ has the identity $I_8$ in both off-diagonal blocks, so $\gamma^{(x_8)}(\psi_-, \psi_+) = (\psi_+, \psi_-)$. $C$, a product of four gammas, commutes with $\Gamma$ and is block diagonal; for the author's gammas $C = \mathrm{diag}(-\sigma, \sigma)$ with a real symmetric $8 \times 8$ matrix $\sigma$, so

$$
S = \Psi^\dagger C\Psi = -\psi_-^\dagger\sigma\psi_- + \psi_+^\dagger\sigma\psi_+ .
$$

Reading this line: reversing the sign of one half ($\Gamma$) keeps $S$; exchanging the two halves ($\gamma^{(x_8)}$) reverses $S$. PROVED: Notebook 18a, In [16]. The two halves are the two inequivalent irreducible 8-dimensional representations of Spin(4,4), and every gamma exchanges them (`python-algebra.json`, checks `spin_halves_irreducible`, `spin_halves_inequivalent`, `reflections_exchange_halves`; `wolfram-algebra.json`, check `Spin_Pin_reflection_swaps_halves`; Chapter 5).

### 18.6 Example: Notebook 18a checks the four lemmas

Notebook 18a first answers the question that every later step depends on: are the matrices of the Revision record really the author's? It rebuilds the eight matrices T16A[0], ..., T16A[7] from the author's own formulas (the tau matrices), maps the author's frame order (0 = hidden, 1 to 3 = 3-space, 4 = time, 5 to 7 = extra times) to the coordinates $x_1, \dots, x_8$, and compares them entry by entry with `Revision/algebra/gammas.json`; it checks that they are real signed permutation matrices with entries $-1$, 0, $+1$ and that the 64 Clifford relations hold. Then it proves Lemmas 1 to 4 and the block form with exact whole-number arithmetic, compares the reflection table and the table of Krein signs with the data tables of the pairing record row by row, and draws seven teaching figures: the eight gammas, the sign flip $\Gamma\gamma^{(x_1)}\Gamma = -\gamma^{(x_1)}$, the parity of the 256 products, the reflection table, the chiral projectors, the block form and the Krein signs. Its last line is ALL 16 CHECKS PASSED (notebook 18a); it runs in about 15 seconds.

<!-- NOTEBOOK 18a -->

### 18.9 Line-by-line walk-through of Notebook 18a

Stub.

### 18.10 Stub 10

Stub.

### 18.11 Stub 11

Stub.

### 18.12 Stub 12

Stub.

### 18.13 Stub 13

Stub.

### 18.14 Stub 14

Stub.

### 18.15 Stub 15

Stub.

### 18.16 Stub 16

Stub.

### 18.17 Stub 17

Stub.

### 18.18 Stub 18

Stub.

### 18.19 Stub 19

Stub.

### 18.20 Stub 20

Stub.

### 18.21 Stub 21

Stub.

### 18.22 Stub 22

Stub.

### 18.23 Stub 23

Stub.

### 18.24 Stub 24

Stub.

### 18.25 Stub 25

Stub.

### 18.26 Stub 26

Stub.

### 18.27 Stub 27

Stub.

### 18.28 Stub 28

Stub.

### 18.29 Stub 29

Stub.

### 18.30 Stub 30

Stub.
