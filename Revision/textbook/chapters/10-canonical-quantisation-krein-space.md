## 10. Canonical quantisation in 4+4: Krein space and the good sector

Chapters 7 to 9 treated the field dirac16complex as a classical field: 16 complex anticommuting numbers $\Psi_1, \dots, \Psi_{16}$ at every point of the author's 4+4 dimensional universe, with a Lagrangian, a field equation and an energy-momentum tensor. This chapter makes the field a quantum field. It follows the standard recipe, canonical quantisation with the time $x_4$, step by step, and finds what is new in signature (4,4): the quantum rule contains the matrix $B$, which has eight positive and eight negative eigenvalues, so the space of quantum states cannot carry an ordinary positive inner product when the field operators are read in the ordinary way; it is a Krein space. In the good sector (waves that do not depend on the three extra times) a positive state space exists for each momentum, with particles and antiparticles of positive energy. The chapter shows exactly how far this goes, where it stops, and what the quantum theory says about the pairing of universes of masses $+m$ and $-m$.

### 10.1 What this chapter does

**Why quantise.** Dirac's equation of 1928 describes one electron as a classical wave. It has waves of negative energy, and a classical theory cannot say why an electron does not fall into them. Quantum field theory answers: the field becomes a collection of operators that create and destroy particles, the negative-energy waves describe antiparticles, and every particle and every antiparticle has positive energy. The same recipe is applied here to dirac16complex, the author's fermion field with 16 complex anticommuting components (a spinor of Pin(4,4), Chapter 5). The second field of the theory, dirac16complex00, with 16 commuting components, is a classical ("semi-classical") field in the author's definition and is not quantised; Section 10.23 shows what that means for its energy.

**What happens in signature (4,4).** The recipe has three steps: read off from the Lagrangian the term with the time derivative; turn it into an anticommutator of the field operators; find a space of quantum states on which operators with this anticommutator act. In ordinary 3+1 dimensional physics the anticommutator is the identity matrix and the state space is an ordinary Hilbert space. Here the anticommutator is the matrix $B = -iC\gamma^{(x_4)}$, and the chapter proves that no space with a positive inner product carries it when $\Psi^\dagger$ is read as the ordinary adjoint. That is the central fact of the chapter, and everything else is built around it:

- one-particle waves: the evolution of a plane wave conserves the Krein form $u^\dagger Bu$, its frequencies are real or imaginary according to the sign of $w^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$, and at every real frequency the waves of one frequency carry four directions of positive and four of negative Krein form (Sections 10.2 to 10.6, Notebook 10a);
- quantum states, fermion modes and the Fock space from zero, the canonical rule, the theorem that forces the Krein space, and the conjugation of the quantised field (Sections 10.11 to 10.16, Notebook 10b);
- the good sector and its positive Fock space, the Dirac sea and normal ordering, and the contrast with the classical commuting field (Sections 10.21 to 10.23, Notebook 10c);
- the curved good sector of the author's metric, where Hermiticity needs a boundary condition at the patch end $z = \pi/2$ (Sections 10.28 and 10.29, Notebook 10d);
- the proof that no invariant choice of the charge density is positive, and the symmetries that keep the canonical rule (Sections 10.34 and 10.35, Notebook 10e);
- the same structure along the deflating history of the extra times, where every wave with extra-time momentum eventually grows (Section 10.40, Notebook 10f);
- the quantum reading of the pairing of universes of masses $+m$ and $-m$, with an exact list of what it does not establish (Sections 10.45 and 10.46, Notebook 10g).

The chapter closes with "What we proved, what we computed, what we assumed" (Section 10.51) and with exercises and their complete answers (Section 10.52).

**The seven worked examples.** Each is a complete Jupyter notebook; each is complete in itself, so you may run them in any order.

| notebook | what it computes | checks | figures |
| --- | --- | --- | --- |
| 10a | one-particle spectra and Krein inertia | 28 | 6 |
| 10b | the canonical rule on a Fock space; the Krein space | 24 | 5 |
| 10c | the positive Fock space of one good-sector momentum | 14 | 5 |
| 10d | the curved good sector along the hidden direction | 16 | 5 |
| 10e | invariant forms and Krein-unitary generators | 15 | 5 |
| 10f | the Krein structure along the deflating history | 19 | 5 |
| 10g | the quantum reading of the pairing | 29 | 5 |

**Notation.** The author's coordinates are written $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates (scale factor $e^{a_4}\sin^{1/6}z$); $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which are time-like and DEFLATE EXPONENTIALLY (scale factor $e^{-a_4}\sin^{1/6}z$ with $a_4$ increasing); $x_8$ is the hidden space direction, with $z = 6Hx_8$ between 0 and $\pi/2$ and $H > 0$ the author's constant. The flat frame metric is $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in the order $x_1, \dots, x_8$. The gamma matrices are the author's eight real $16 \times 16$ matrices; the one of the direction $x_a$ is written $\gamma^{(x_a)}$, and they obey the Clifford relation $\gamma^{(x_a)}\gamma^{(x_b)} + \gamma^{(x_b)}\gamma^{(x_a)} = 2\eta_{ab}I_{16}$ (Chapter 4), where $I_{16}$ is the $16 \times 16$ identity matrix and $\eta_{ab}$ is $\eta_{aa}$ for $a = b$ and 0 otherwise. So a space-like gamma ($x_1, x_2, x_3, x_8$) squares to $+I_{16}$, a time-like one ($x_4, \dots, x_7$) to $-I_{16}$, and two different gammas anticommute. Chapter 5 built from them the charge matrix $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$ (the author's sigma16), the chirality $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)} = \mathrm{diag}(-I_8, I_8)$ and the matrix $B = -iC\gamma^{(x_4)}$. For a matrix $M$, $M^T$ is its transpose, $M^*$ the matrix of the complex conjugate entries and $M^\dagger = (M^T)^*$ its conjugate transpose; for a column $u$, $u^\dagger$ is the row of the conjugated entries. The letter $m$ is the mass. The words used for the status of a statement are those of the whole book: PROVED (exact, with the verifying record and check), COMPUTED (a numerical result with its accuracy), ASSUMED, HYPOTHESIS and OPEN.

**The records this chapter uses.** Every formula and number comes from these Revision records or from the chapter's own notebooks, which reproduce the records where they overlap:

| record | what it holds |
| --- | --- |
| `Revision/algebra/gammas.json` | the eight gammas, $C$ and $B$ |
| `Revision/algebra/reports/` | the algebra checks: `python-algebra.json`, `wolfram-algebra.json` |
| `Revision/theory/reports/` | the field-theory checks: `python-field-theory.json`, `wolfram-field-theory.json`, `python-scope.json`, `wolfram-scope.json` |
| `Revision/theory/field-theory.json` | the formulas of the field theory |
| `Revision/pairing/pairing-theory.json` | the pairing theorems and their data |
| `Revision/pairing/reports/` | the pairing checks: `python-pairing.json`, `wolfram-pairing.json` |
| `Revision/lead_checks/reports/` | `charge-conjugation-and-u1.json` (12 checks) |
| `Revision/kohn_sham/results/parameters.json` | the parameters of the deflating history |

A report is a file in which a verifying program has recorded each check with its name, its verdict and a detail text; every check cited in this chapter has the verdict PASS. Below, a report is named by its file name only, for example "`python-field-theory.json`, check `canonical_anticommutator_B`".

### 10.2 The matrix B and the Krein form

**The charge.** Chapter 5 showed that the current of the field is $J^\mu = -i\bar\Psi\gamma^\mu\Psi$ with $\bar\Psi = \Psi^\dagger C$, and that its time component is the charge density

$$
J^{(x_4)} = -i\Psi^\dagger C\gamma^{(x_4)}\Psi = \Psi^\dagger B\Psi,\qquad B = -iC\gamma^{(x_4)} .
$$

The Revision record proves that the total charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ does not change in time when the field equation holds (`charge-conjugation-and-u1.json`, check `u1_noether_matrix_identity`; `wolfram-field-theory.json`, check `charge_density_is_Krein_form_G`). For two columns $u$ and $v$ of 16 complex numbers the number $u^\dagger Bv$ is called their **Krein form**, and $u^\dagger Bu$ the **Krein norm** of $u$ (a name, not a length: it can be negative).

**Five properties of B, derived line by line.** We use only the Clifford relation, the reality of the gammas, $C^T = C$, $CC = I_{16}$ and $(\gamma^{(x_4)})^T = -\gamma^{(x_4)}$ (Chapter 5).

(B1) $C\gamma^{(x_4)} = \gamma^{(x_4)}C$. Move $\gamma^{(x_4)}$ from the right of $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$ to its left, one factor at a time:

$$
\gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}\gamma^{(x_4)} = (-1)^4\,\gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)} .
$$

Each of the four steps exchanges $\gamma^{(x_4)}$ with a different gamma, which costs a sign by the Clifford relation; four signs give $+1$.

(B2) $B$ is purely imaginary: $C\gamma^{(x_4)}$ is a product of real matrices, and $B$ is $-i$ times it.

(B3) $B$ is Hermitian, $B^\dagger = B$:

$$
B^\dagger = (+i)\,(C\gamma^{(x_4)})^T = (+i)\,(\gamma^{(x_4)})^TC^T = (+i)(-\gamma^{(x_4)})C = -i\,\gamma^{(x_4)}C = -i\,C\gamma^{(x_4)} = B .
$$

The first step conjugates the number $-i$ and transposes the real matrix; the second uses $(MN)^T = N^TM^T$; the third uses $(\gamma^{(x_4)})^T = -\gamma^{(x_4)}$ and $C^T = C$; the fourth collects the signs; the fifth is (B1).

(B4) $BB = I_{16}$:

$$
BB = (-i)^2\,C\gamma^{(x_4)}C\gamma^{(x_4)} = -\,CC\,\gamma^{(x_4)}\gamma^{(x_4)} = -\,I_{16}\,(-I_{16}) = I_{16} .
$$

The first step uses $(-i)^2 = -1$; the second moves the middle $C$ to the left by (B1); the third uses $CC = I_{16}$ and $\gamma^{(x_4)}\gamma^{(x_4)} = \eta_{44}I_{16} = -I_{16}$.

(B5) $\mathrm{tr}\,B = 0$, and $B$ has eight eigenvalues $+1$ and eight $-1$. The trace of a matrix is the sum of its diagonal entries; it does not change when the factors of a product are rotated, $\mathrm{tr}(XY) = \mathrm{tr}(YX)$. The chirality $\Gamma$ anticommutes with every gamma (it is the product of all eight; moving one gamma through it passes seven different gammas and itself, sign $(-1)^7 = -1$), so it anticommutes with the product of the five gammas in $C\gamma^{(x_4)}$, and $\Gamma\Gamma = I_{16}$. Hence

$$
\mathrm{tr}\,B = \mathrm{tr}(\Gamma\Gamma B) = \mathrm{tr}(\Gamma B\Gamma) = \mathrm{tr}(-B\Gamma\Gamma) = -\mathrm{tr}\,B ,
$$

so $\mathrm{tr}\,B = 0$. The first step inserts $\Gamma\Gamma = I_{16}$, the second rotates the first factor $\Gamma$ to the end, the third moves $\Gamma$ through $B$ at the cost of a sign. If $Bu = \lambda u$ with $u \neq 0$, then $u = BBu = \lambda^2u$, so $\lambda^2 = 1$ and $\lambda = \pm1$; the trace is the sum of the 16 eigenvalues, and a sum of sixteen numbers $\pm1$ is 0 only with eight of each sign. A Hermitian matrix with $p$ positive and $n$ negative eigenvalues has the **signature** $(p, n)$: $B$ has signature (8,8).

So the Krein norm $u^\dagger Bu$ is a real number for every column (because $B$ is Hermitian, $(u^\dagger Bu)^* = u^\dagger B^\dagger u = u^\dagger Bu$), and it is positive for the eight eigenvectors of $+1$ and negative for the eight eigenvectors of $-1$. Unlike the charge density $\psi^\dagger\psi$ of Dirac's electron, the charge density of dirac16complex takes both signs.

**B as a table.** $B$ is $i$ times a real signed permutation matrix: every row has exactly one nonzero entry, $+i$ or $-i$. The following table, computed from the record `Revision/algebra/gammas.json`, gives for every row $r$ the column $c$ of its nonzero entry and its value; so $(Bu)_r = B_{rc}\,u_c$.

| row $r$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| column $c$ | 10 | 9 | 12 | 11 | 14 | 13 | 16 | 15 |
| entry $B_{rc}$ | $+i$ | $-i$ | $-i$ | $+i$ | $-i$ | $+i$ | $+i$ | $-i$ |

| row $r$ | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| column $c$ | 2 | 1 | 4 | 3 | 6 | 5 | 8 | 7 |
| entry $B_{rc}$ | $+i$ | $-i$ | $-i$ | $+i$ | $-i$ | $+i$ | $+i$ | $-i$ |

**Which gammas commute with B.** $B$ is $-i$ times the product of the five gammas of $x_8, x_1, x_2, x_3, x_4$. A gamma among these five passes four different gammas and itself when it is moved through the product, sign $(-1)^4 = +1$: it commutes with $B$. A gamma of $x_5, x_6, x_7$ passes five different gammas, sign $(-1)^5 = -1$: it anticommutes with $B$. Hence $B$ commutes with $\gamma^{(x_1)}, \gamma^{(x_2)}, \gamma^{(x_3)}, \gamma^{(x_4)}, \gamma^{(x_8)}$ and anticommutes with $\gamma^{(x_5)}, \gamma^{(x_6)}, \gamma^{(x_7)}$, and by the same counting $\Gamma B\Gamma = -B$.

| statement | status | where it is verified |
| --- | --- | --- |
| $B$ purely imaginary, Hermitian, $BB = I_{16}$, $\mathrm{tr}\,B = 0$, signature (8,8) | PROVED | `python-field-theory.json`, check `B_properties`; `wolfram-algebra.json`, check `B_signature_8_8` |
| $B$ commutes with the gammas of $x_1, x_2, x_3, x_4, x_8$, anticommutes with those of $x_5, x_6, x_7$ | PROVED | `python-algebra.json`, check `B_gamma_relations` |
| the charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ is conserved | PROVED | `charge-conjugation-and-u1.json`, check `u1_noether_matrix_identity` |

### 10.3 One plane wave: the mode Hamiltonian

We first study one wave of the field at a time, as a classical wave, before any quantisation. Take $U = 0$ (no self-interaction) and flat 4+4 space. Flat space is not the author's universe, but the author's field equation, written at one point and one instant with its coefficients evaluated there ("frozen coefficients"), has the same form with the derivatives divided by scale factors; the end of this section says how. The field equation is (Chapter 7)

$$
\gamma^{(x_4)}\partial_4\Psi + \sum_{a \neq 4}\gamma^{(x_a)}\partial_a\Psi = m\Psi ,
$$

where $\partial_a$ is the derivative with respect to $x_a$ and the sum runs over the seven directions $a = 1, 2, 3, 5, 6, 7, 8$ of a slice $x_4 = $ const.

**Step 1.** Multiply from the left by $\gamma^{(x_4)}$ and use $\gamma^{(x_4)}\gamma^{(x_4)} = -I_{16}$:

$$
-\partial_4\Psi + \sum_{a \neq 4}\gamma^{(x_4)}\gamma^{(x_a)}\partial_a\Psi = m\gamma^{(x_4)}\Psi .
$$

**Step 2.** Add $\partial_4\Psi - m\gamma^{(x_4)}\Psi$ to both sides and exchange the two sides:

$$
\partial_4\Psi = -m\gamma^{(x_4)}\Psi + \sum_{a \neq 4}\gamma^{(x_4)}\gamma^{(x_a)}\partial_a\Psi .
$$

**Step 3.** A **plane wave** is $\Psi = u(x_4)\,e^{i\sum_{a \neq 4}k_ax_a}$ with a column $u$ that depends on the time only and real numbers $k_a$, the **momenta** (wave numbers) along the slice. The derivative of $e^{ik_ax_a}$ with respect to $x_a$ is $ik_ae^{ik_ax_a}$, so each $\partial_a$ with $a \neq 4$ becomes the factor $ik_a$; then the common exponential cancels:

$$
\frac{du}{dx_4} = -m\gamma^{(x_4)}u + i\sum_{a \neq 4}k_a\gamma^{(x_4)}\gamma^{(x_a)}u .
$$

**Step 4.** Multiply by $i$ and use $i \cdot i = -1$:

$$
i\frac{du}{dx_4} = h\,u,\qquad h = -im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_{a \neq 4}k_a\gamma^{(x_a)} .
$$

The $16 \times 16$ matrix $h$ is the **mode Hamiltonian** of the wave. The equation $i\,du/dx_4 = hu$ has the form of the Schrödinger equation of quantum mechanics; its solutions with $u(x_4) = u_0e^{-iwx_4}$ are the eigenvectors $hu_0 = wu_0$, and the eigenvalue $w$ is the **frequency** of the wave. A real $w$ means oscillation; an imaginary $w = i\kappa$ means $e^{-iwx_4} = e^{\kappa x_4}$, growth.

**Frame momenta and the deflating extra times.** In the author's metric each derivative of the field equation is divided by the scale factor $f_a$ of its direction (Chapter 6): $f_a = e^{a_4}\sin^{1/6}z$ for $x_1, x_2, x_3$, $f_4 = 1$, $f_a = e^{-a_4}\sin^{1/6}z$ for $x_5, x_6, x_7$ and $f_8 = \cot z$ (record `Revision/theory/field-theory.json`, formula `vielbein_diagonal`). A wave $e^{iq_ax_a}$ with the **coordinate momentum** $q_a$ therefore enters the equation with the **frame momentum** $k_a = q_a/f_a$. Along 3-space $k_a = q_ae^{-a_4}\sin^{-1/6}z$ shrinks as 3-space inflates; along an extra time $k_a = q_ae^{a_4}\sin^{-1/6}z$ GROWS as the extra times deflate. "Frozen coefficients" means only that these factors are evaluated at one instant and one hidden position; the extra times are never treated as static. Section 10.40 and Notebook 10f follow the frame momenta along the deflating history.

### 10.4 The square of h, the Krein form, and three kinds of waves

**The square.** Write $h$ as a sum of eight terms, $h = mE_0 + \sum_{a \neq 4}k_aE_a$, with $E_0 = -i\gamma^{(x_4)}$ and $E_a = -\gamma^{(x_4)}\gamma^{(x_a)}$. Three facts follow from the Clifford relation:

$$
E_0E_0 = (-i)^2\gamma^{(x_4)}\gamma^{(x_4)} = -(-I_{16}) = I_{16},
$$

$$
E_aE_a = \gamma^{(x_4)}\gamma^{(x_a)}\gamma^{(x_4)}\gamma^{(x_a)} = -\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_a)}\gamma^{(x_a)} = -(-I_{16})(\eta_{aa}I_{16}) = \eta_{aa}I_{16},
$$

where the second step exchanges the middle factors $\gamma^{(x_a)}\gamma^{(x_4)}$ at the cost of a sign; and any two different $E$'s anticommute, for example

$$
E_0E_a + E_aE_0 = i\big(\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_a)} + \gamma^{(x_4)}\gamma^{(x_a)}\gamma^{(x_4)}\big) = i\big(\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_a)} - \gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_a)}\big) = 0 ,
$$

and in the same way $E_aE_b + E_bE_a = -\gamma^{(x_4)}\gamma^{(x_4)}(\gamma^{(x_a)}\gamma^{(x_b)} + \gamma^{(x_b)}\gamma^{(x_a)}) = 0$ for $a \neq b$. Now multiply out $hh$: the products of a term with itself give $m^2I_{16}$ and $k_a^2\eta_{aa}I_{16}$, and the products of two different terms come in pairs $c_ic_j(E_iE_j + E_jE_i) = 0$. Therefore

$$
h^2 = w^2I_{16},\qquad w^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2 .
$$

The space-like momenta enter with $+$, the extra-time momenta with $-$ (because $\eta_{aa} = -1$ for $a = 5, 6, 7$). Every eigenvalue $w'$ of $h$ obeys $w'^2 = w^2$ (if $hu = w'u$ then $w^2u = hhu = w'^2u$), so the eigenvalues are $+w$ and $-w$; since $\mathrm{tr}\,h = 0$ (the traces of $\gamma^{(x_4)}$ and of $\gamma^{(x_4)}\gamma^{(x_a)}$ vanish, by the argument of (B5) for a product of an odd number of gammas and by $\mathrm{tr}(\gamma^{(x_4)}\gamma^{(x_a)}) = \mathrm{tr}(\gamma^{(x_a)}\gamma^{(x_4)}) = -\mathrm{tr}(\gamma^{(x_4)}\gamma^{(x_a)})$ for two), each occurs eight times when $w \neq 0$.

**Hermitian and anti-Hermitian parts.** A matrix is **Hermitian** if $M^\dagger = M$ and **anti-Hermitian** if $M^\dagger = -M$. Using $(\gamma^{(x_a)})^T = \eta_{aa}\gamma^{(x_a)}$ (Chapter 5):

$$
(-i\gamma^{(x_4)})^\dagger = i(\gamma^{(x_4)})^T = -i\gamma^{(x_4)},\qquad (\gamma^{(x_4)}\gamma^{(x_a)})^\dagger = (\gamma^{(x_a)})^T(\gamma^{(x_4)})^T = -\eta_{aa}\gamma^{(x_a)}\gamma^{(x_4)} = \eta_{aa}\gamma^{(x_4)}\gamma^{(x_a)} .
$$

So $-i\gamma^{(x_4)}$ and $\gamma^{(x_4)}\gamma^{(x_a)}$ for the space-like $a = 1, 2, 3, 8$ are Hermitian, while $\gamma^{(x_4)}\gamma^{(x_a)}$ for the extra times $a = 5, 6, 7$ is anti-Hermitian. Write $h = h_H + h_A$ with

$$
h_H = -im\gamma^{(x_4)} - \gamma^{(x_4)}\big(k_1\gamma^{(x_1)} + k_2\gamma^{(x_2)} + k_3\gamma^{(x_3)} + k_8\gamma^{(x_8)}\big),\qquad h_A = -\gamma^{(x_4)}\big(k_5\gamma^{(x_5)} + k_6\gamma^{(x_6)} + k_7\gamma^{(x_7)}\big).
$$

$h_H$ is Hermitian and $h_A$ anti-Hermitian. By Section 10.2, $\gamma^{(x_4)}$ and the four space-like gammas commute with $B$, so $h_H$ commutes with $B$; the gammas of $x_5, x_6, x_7$ anticommute with $B$ while $\gamma^{(x_4)}$ commutes, so $h_A$ anticommutes with $B$. Two consequences:

- $h$ is Hermitian, and commutes with $B$, exactly when $k_5 = k_6 = k_7 = 0$: in the **good sector**, the waves that do not depend on the extra times;
- for all momenta, $h^\dagger B = (h_H - h_A)B = Bh_H + Bh_A = Bh$. In words, $h$ is **Krein self-adjoint**: $Bh = h^\dagger B$.

**The Krein form is conserved.** Let $u(x_4)$ solve $i\,du/dx_4 = hu$, so $du/dx_4 = -ihu$ and, taking the conjugate transpose, $du^\dagger/dx_4 = iu^\dagger h^\dagger$. By the product rule

$$
\frac{d}{dx_4}\big(u^\dagger Bu\big) = \frac{du^\dagger}{dx_4}Bu + u^\dagger B\frac{du}{dx_4} = iu^\dagger h^\dagger Bu - iu^\dagger Bhu = i\,u^\dagger\big(h^\dagger B - Bh\big)u = 0 .
$$

The last step is $h^\dagger B = Bh$. The Krein norm of every wave is constant in time, also when the wave grows; the ordinary length $u^\dagger u$ changes by $d(u^\dagger u)/dx_4 = iu^\dagger(h^\dagger - h)u = -2iu^\dagger h_Au$, which vanishes in the good sector only.

**Three kinds of waves.** Because $h^2 = w^2I_{16}$, the exponential series of the solution collapses. The solution is $u(x_4) = e^{-ihx_4}u(0)$ with $e^{X} = I_{16} + X + X^2/2! + \dots$; the even powers of $-ihx_4$ are $(-1)^jw^{2j}x_4^{2j}I_{16}$ and the odd powers are $-i(-1)^jw^{2j}x_4^{2j+1}h$, so

$$
e^{-ihx_4} = \cos(wx_4)\,I_{16} - i\,\frac{\sin(wx_4)}{w}\,h ,
$$

by the power series of the cosine and the sine. Three cases follow:

- $w^2 > 0$: real frequencies $\pm w$, the wave oscillates;
- $w^2 = 0$ with $h \neq 0$: $h^2 = 0$ and $e^{-ihx_4} = I_{16} - ihx_4$, the wave grows linearly;
- $w^2 < 0$, that is $k_5^2 + k_6^2 + k_7^2 > m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2$: $w = i\kappa$ with $\kappa = \sqrt{-w^2}$, and since $\cos(i\kappa x_4) = \cosh(\kappa x_4)$ and $\sin(i\kappa x_4)/(i\kappa) = \sinh(\kappa x_4)/\kappa$, half of the waves grow like $e^{\kappa x_4}$.

A large enough extra-time momentum always produces growth, and the growth rate $\kappa$ has no upper bound as that momentum grows: the initial-value problem with data that depend on the extra times is not well posed (Chapter 8).

| statement | status | where it is verified |
| --- | --- | --- |
| $h^2 = w^2I_{16}$ for all real $m$, $k$ | PROVED | `wolfram-pairing.json`, check `Q_one_particle_flat_dispersion`; `python-field-theory.json`, check `mode_hamiltonian_B_selfadjoint_dispersion` |
| $Bh = h^\dagger B$ for all real $m$, $k$ | PROVED | `python-field-theory.json`, check `mode_hamiltonian_B_selfadjoint_dispersion`; `wolfram-field-theory.json`, check `mode_hamiltonian_Krein_selfadjoint` |
| $h$ Hermitian and $[B, h] = 0$ exactly in the good sector | PROVED | `wolfram-field-theory.json`, check `mode_hamiltonian_good_sector`; `python-field-theory.json`, check `good_sector_spectrum_and_B_sectors` |
| growth for $w^2 < 0$, rates unbounded | PROVED | `python-field-theory.json`, check `extra_time_modes_grow`; `python-scope.json`, check `extra_time_growth_rates_unbounded` |

### 10.5 Krein inertia of the eigenspaces

**Projectors onto the eigenspaces.** An **eigenspace** of $h$ is the set of all columns $u$ with $hu = w'u$ for one eigenvalue $w'$ (with the zero column). For $w \neq 0$ define

$$
P_\pm = \tfrac12\big(I_{16} \pm h/w\big).
$$

Then $P_\pm P_\pm = \frac14(I_{16} \pm 2h/w + h^2/w^2) = \frac14(2I_{16} \pm 2h/w) = P_\pm$, by $h^2 = w^2I_{16}$: $P_\pm$ is a **projector** (a matrix with $PP = P$, which maps every column into one subspace, its range, and leaves the columns of that range unchanged). And $hP_\pm = \frac12(h \pm w^2/w\,I_{16}) = \pm wP_\pm$, so the range of $P_+$ is the eigenspace of $+w$ and the range of $P_-$ that of $-w$. Since $P_+ + P_- = I_{16}$, every column is the sum of a column of each.

**Krein inertia.** Choose a basis $v_1, \dots, v_d$ of a subspace and form the **Gram matrix** $G_{ij} = v_i^\dagger Bv_j$. It is Hermitian; its numbers of positive, negative and zero eigenvalues do not depend on the basis chosen (a fact of linear algebra called Sylvester's law of inertia), and they form the **Krein inertia** $(p, n, z)$ of the subspace. It says how many independent waves of the subspace carry positive, negative and zero Krein norm. A subspace on which $u^\dagger Bv = 0$ for all its members has inertia $(0, 0, d)$ and is called **Krein-neutral**.

**Theorem 10.1 (Krein inertia of one-particle waves).** In flat 4+4 space (or with frozen coefficients), for every real frequency, $w^2 > 0$, with or without extra-time momentum, each of the two eigenspaces of $h$ has dimension 8 and Krein inertia (4,4). For every imaginary frequency both eigenspaces are Krein-neutral, and for $w = 0$ the range of $h$ is Krein-neutral. (PROVED: `wolfram-pairing.json`, checks `Q_one_particle_Krein_inertia_real_frequencies` and `Q_one_particle_complex_and_zero_frequencies_Krein_neutral`; `python-pairing.json`, checks `Q.one_particle_Krein_inertia_proof` and `Q.one_particle_complex_frequency_Krein_neutral`.)

*Proof, step (i): the two eigenspaces are Krein-orthogonal.* Let $w > 0$ be real, so $P_+^\dagger = \frac12(I_{16} + h^\dagger/w)$. Then

$$
4w^2\,P_+^\dagger BP_- = (wI_{16} + h^\dagger)\,B\,(wI_{16} - h) = w^2B - wBh + wh^\dagger B - h^\dagger Bh .
$$

The first step multiplies each projector by $2w$; the second multiplies out. By $h^\dagger B = Bh$ the two middle terms cancel, and $h^\dagger Bh = Bhh = w^2B$, so the right side is $w^2B - w^2B = 0$. A wave of frequency $+w$ and one of $-w$ have zero mixed Krein form. In the same way $P_+^\dagger BP_+ = BP_+$. Because $B$ is invertible and the two eigenspaces together span all 16 directions, $B$ cannot vanish on either eigenspace: if a column $u$ of the $+w$ eigenspace had $u^\dagger Bv = 0$ for all $v$ in that eigenspace, it would also have it for all $v$ in the other (step (i)), hence for all columns, so $Bu = 0$ and $u = BBu = 0$. Such a form is called **nondegenerate** on the eigenspace: its Gram matrix has no zero eigenvalue.

*Step (ii): in the good sector the inertia is (4,4).* There $Bh = hB$, so $B$ commutes with $P_\pm$ and maps each eigenspace into itself. The trace of $BP_+$ is the sum of the eigenvalues of $B$ on the $+w$ eigenspace; each is $+1$ or $-1$ (because $BB = I_{16}$), and there are eight of them (because $\mathrm{tr}\,P_+ = \frac12(16 + \mathrm{tr}\,h/w) = 8$). Now

$$
\mathrm{tr}(BP_\pm) = \tfrac12\,\mathrm{tr}\,B \pm \tfrac{1}{2w}\,\mathrm{tr}(Bh) = 0 ,
$$

because $\mathrm{tr}\,B = 0$ (Section 10.2) and $Bh = mC - i\sum_ak_aC\gamma^{(x_a)}$ is a combination of $C$ (a product of four different gammas) and of products of three or five different gammas, all of trace 0: a product of an odd number of different gammas has trace 0 by the argument of (B5), and a product of an even number $k$ of different gammas has trace 0 because moving its first factor to the end does not change the trace but costs the sign $(-1)^{k-1} = -1$. Eight numbers $\pm1$ with the sum 0 are four $+1$ and four $-1$: inertia (4,4).

*Step (iii): every real frequency.* Start in the good sector and turn on the extra-time momenta slowly, keeping $m, k_1, k_2, k_3, k_8$ fixed. As long as $w^2 > 0$ the projectors $P_\pm$ change continuously, and by step (i) the Gram matrix of each eigenspace never has a zero eigenvalue. An eigenvalue of a continuously changing Gram matrix can change its sign only by passing through 0, which is forbidden, so the inertia stays (4,4). Every real-frequency point can be reached in this way (lowering $k_5, k_6, k_7$ to 0 only increases $w^2$).

*Imaginary frequencies.* Let $w$ be an eigenvalue that is not real, and $hu = wu$, $hv = wv$. Compute $u^\dagger Bhv$ in two ways: it is $w\,u^\dagger Bv$; and with $Bh = h^\dagger B$ it is $u^\dagger h^\dagger Bv = (hu)^\dagger Bv = w^*\,u^\dagger Bv$. Subtracting, $(w - w^*)\,u^\dagger Bv = 0$, and $w - w^* \neq 0$, so $u^\dagger Bv = 0$ on the whole eigenspace. *Zero frequency:* $h^2 = 0$ and $(hx)^\dagger B(hy) = x^\dagger h^\dagger Bhy = x^\dagger Bhhy = 0$. QED.

**What it means.** In flat 4+4 space the waves of every real frequency mix positive and negative charge half and half; the good sector removes the complex frequencies, but not this indefiniteness of the one-particle waves. The growing waves carry no charge at all: their eigenspaces are neutral.

### 10.6 The universes of masses $+m$ and $-m$ have the same one-particle spectrum

The pairing theorem T1 of the Revision record (proved in Chapter 18) relates the field of mass $m$ to the field of mass $-m$ by the chirality matrix: if $\Psi$ solves the equations with $(m, \lambda)$, then $\Gamma\Psi$ solves them with $(-m, -\lambda)$. What does this do to the one-particle waves? Write $h_m(k)$ for the mode Hamiltonian of mass $m$ and momenta $k$.

**The chirality map.** $\Gamma$ anticommutes with every gamma and $\Gamma\Gamma = I_{16}$, so

$$
\Gamma\gamma^{(x_4)}\Gamma = -\gamma^{(x_4)}\Gamma\Gamma = -\gamma^{(x_4)},\qquad \Gamma\gamma^{(x_4)}\gamma^{(x_a)}\Gamma = (\Gamma\gamma^{(x_4)}\Gamma)(\Gamma\gamma^{(x_a)}\Gamma) = (-\gamma^{(x_4)})(-\gamma^{(x_a)}) = \gamma^{(x_4)}\gamma^{(x_a)} ,
$$

where the second identity inserts $\Gamma\Gamma = I_{16}$ between the two gammas. Insert into $h_m(k)$:

$$
\Gamma h_m(k)\Gamma = +im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_{a \neq 4}k_a\gamma^{(x_a)} = h_{-m}(k) .
$$

**The mirror map.** In the same way, with $\gamma^{(x_8)}\gamma^{(x_8)} = I_{16}$: $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_8)} = -\gamma^{(x_4)}$; $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_a)}\gamma^{(x_8)} = \gamma^{(x_4)}\gamma^{(x_a)}$ for $a \neq 4, 8$ (two sign changes); and $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_8)} = -\gamma^{(x_4)}\gamma^{(x_8)}$ (one sign change). So $\gamma^{(x_8)}h_m(k)\gamma^{(x_8)} = h_{-m}(R_8k)$, where $R_8k$ is $k$ with $k_8$ replaced by $-k_8$.

**Equal spectra.** If $h_mu = w'u$, then $h_{-m}(\Gamma u) = \Gamma h_m\Gamma\Gamma u = \Gamma h_mu = w'\,\Gamma u$: the matrix $\Gamma$ carries every eigenvector of $h_m$ to an eigenvector of $h_{-m}$ with the same eigenvalue. Matrices related in this way ($N = SMS^{-1}$) are called **similar**, and similar matrices have the same eigenvalues. So the one-particle spectra of the universes of masses $+m$ and $-m$ are IDENTICAL, not opposite; the same follows from $w^2$, which contains the mass only as $m^2$. (PROVED: `wolfram-pairing.json`, checks `Q_one_particle_maps` and `Q_one_particle_Krein_signatures`; `python-pairing.json`, check `Q.one_particle_maps`.) This is statement Q4 of the quantum reading of the Revision record; Sections 10.45 and 10.46 discuss the whole quantum reading and what it does not establish.

### 10.7 Example: Notebook 10a computes the one-particle spectra and their Krein inertia

Notebook 10a reads the author's gammas from the record `Revision/algebra/gammas.json`, builds $C$ and $B$, checks the properties of Section 10.2, builds the mode Hamiltonian of Section 10.3, proves exactly with sympy that $h^2 = w^2I_{16}$ and $Bh = h^\dagger B$ (Section 10.4), follows the eigenvalues as the extra-time momentum grows, computes the Krein inertia of the eigenspaces for the eight samples stored in the pairing record and for a scan across the threshold of growth, repeats steps (i) and (ii) of the proof of Theorem 10.1 exactly, and checks the identities of Section 10.6. It draws six figures and ends with the line ALL 28 CHECKS PASSED (notebook 10a).

<!-- NOTEBOOK 10a -->

### 10.10 Line-by-line walk-through of Notebook 10a

The notebook has 18 code cells, In [1] to In [18]. This section explains every line of each of them. Python, the language of the notebooks, is read from top to bottom; a line that starts with `#` is a **comment** for the reader, which Python skips, and the text after `#` on a line of code is a comment too. Where a cell defines a function, the **docstring** (the text in triple quotes below the `def` line, which only describes the function) is left out of the quotations; it is printed in Section 10.9.

**In [1], the set-up cell.** This cell is the same in every notebook of the book; only the line that sets `NOTEBOOK_ID` differs. Its first 236 lines are comments: they repeat, word for word, the run instructions of Section 10.8 (Python skips them; they are there so that the notebook carries its own instructions), and end with the heading THE SET-UP between two lines of `=` signs. The code starts below that heading.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module**, a collection of ready-made functions, so that the code can use it. The four modules come with Python. `json` reads and writes JSON files, the format of the Revision records; `os` gives access to the operating system; `textwrap` breaks a long text into lines. `from pathlib import Path` takes only the name `Path` out of the module `pathlib`: a `Path` is the address of a file or a folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

matplotlib is the package that draws the figures; its drawing functions are loaded under the short name `plt`. `Image` and `display` come from IPython, the part of Jupyter that runs Python code; together they show a picture file below a cell.

```python
NOTEBOOK_ID = "10a"  # this notebook: chapter 10, example a
```

A **variable** is a name for a value. This line gives the name `NOTEBOOK_ID` to the **string** (a text between quotes) `"10a"`. The figure files and the last printed line of the notebook use it.

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

`def` defines a **function**: a named piece of code that runs each time it is called. `Path.cwd()` is the folder in which the notebook runs (Jupyter runs a notebook in the folder that holds it), and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it; `[here, *here.parents]` is the list that starts with `here` and continues with them. The `for` loop takes these folders one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that holds the file `Revision/textbook/requirements.txt` is the repository, and `return` hands it back to the caller. If no folder qualifies, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The two comment lines say what the next line does and why. That line calls the function and names its result `REPO`. It is never printed, because it differs from computer to computer while the printed output of a notebook must be the same everywhere. The three comment lines that follow explain the last line, which chooses the folder below which files are written. `os.environ` holds the **environment variables**, named texts that a program receives from the computer; `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` if it is set, and otherwise the repository folder (`str(REPO)` writes it as a text). When you run the notebook the variable is not set, so files go into the repository; the book's checking tool sets it to a scratch folder, so that a check never changes the repository.

```python
def repository_file(relative):
    return REPO / relative


def output_file(relative):
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

`repository_file("Revision/...")` is the complete path of a file of the repository; the notebook uses it to READ the Revision records. `output_file("Revision/...")` is the path at which to WRITE a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the folder of the file, and every missing folder above it, and does nothing if it already exists.

```python
def say(text):
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters, the width of a page of this book: `textwrap.fill` breaks the text at blanks, and every line after the first starts with four blanks. `str(text)` turns a number or a list into text first.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to the built-in settings of matplotlib, so that a personal settings file on your computer cannot change the figures. `plt.rcParams.update({...})` then sets four of them: the size of a figure (7.0 by 4.2 inches), the size of the letters (10 points), and a faint grid behind every plot (`"grid.alpha": 0.3` makes it 30 percent opaque). The braces make a **dictionary**, a collection of pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with the letter `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is the text `Revision/textbook/figures/10a.captions.json`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty dictionary, `{}` and a line end, into the captions file, which `save_figure` fills later; `encoding="utf-8"` fixes how letters are stored and `newline="\n"` writes the same line end on every operating system, as the two comment lines above it say.

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

`setdefault(name, value)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far (`len` is the number of entries); so the figures are numbered 1, 2, 3, and a cell that is run again keeps its numbers. The file name joins the notebook id, the number and the name, for example `10a_1_gamma4_c_and_b.png`. The three comment lines explain the options of the next line: `fig.savefig` writes the picture as a PNG file with 150 dots per inch (`dpi=150`), cuts away the empty margin (`bbox_inches="tight"`) and stores no program name in the file (`metadata={"Software": None}`), so that two runs write exactly the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time at the end of the cell. The caption is stored, and the whole dictionary of captions is written to the captions file; `json.dumps` turns the dictionary into JSON text with sorted keys. `display(Image(...))` shows the saved picture below the cell, with a label that the book's tools read, and the last line prints where the figure was saved.

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

`PASSED` is an empty **list**, an ordered collection written in square brackets. `check` is the function behind every check of the book. `condition` is a truth value, `True` or `False`. If it is false, `raise AssertionError(...)` stops the notebook with an error message that names the check (an `if` statement is used instead of Python's `assert`, because Python started with the option O, for optimise, would skip an `assert`). If it is true, the name is appended to `PASSED` and the line PASS name is printed; when the optional third argument `record` names a Revision record, a second line says which record and check the result reproduces.

```python
def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a line that starts with RESULT; the unit is added only when one is given (`a if condition else b` is `a` when the condition holds and `b` otherwise). `all_checks_passed` prints the last line of the notebook with the number of checks that passed. The last statement prints the single output line of In [1]. Two strings written next to each other, as here, are joined into one.

**In [2], the gammas and the Clifford relation.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer
import sys  # the screen output, sys.stdout

import numpy as np  # numbers, arrays and matrices
import sympy as sp  # exact algebra with symbols
```

Three more modules of Python are loaded, and the two mathematical packages of the book: numpy (short name `np`) computes with arrays of numbers, sympy (short name `sp`) computes exactly with symbols.

```python
def check_record(condition, name, record):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
        check(condition, name, record=record)
    sys.stdout.write(buffer.getvalue())  # one single piece of output
```

`check_record` does what `check(condition, name, record=record)` does, but prints the PASS line and the reproduces line in one piece. `io.StringIO()` is a **text buffer**, a piece of memory that collects printed text. Inside the `with` block everything that is printed goes into the buffer instead of the screen; `check` prints its two lines there (or stops the notebook if the condition is false). Then `sys.stdout.write` sends the collected text to the screen at once. Jupyter delivers printed text in pieces whose boundaries depend on timing; printing the two lines as one piece keeps the stored output of the notebook the same in every run.

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
    encoding="utf-8"))
# gamma[a] is the matrix gamma^(x_a) of the coordinate x_a, a = 1, ..., 8.
gamma = {a: np.array(fixture["gamma"][a - 1], dtype=int) for a in range(1, 9)}
eta = {a: fixture["eta"][a - 1] for a in range(1, 9)}  # +1 space-like, -1 time-like
identity = np.eye(16, dtype=int)
say(f"eta = {[eta[a] for a in range(1, 9)]} for x1, ..., x8")
```

`read_text` reads the record file as text, and `json.loads` turns that text into Python objects: `fixture` is a dictionary whose keys are the names stored in the record. `fixture["gamma"]` is a list of eight matrices, each a list of 16 rows of 16 whole numbers, in the order $x_1, \dots, x_8$; Python counts list positions from 0, so the matrix of $x_a$ is at position `a - 1`. The **dictionary comprehension** `{a: ... for a in range(1, 9)}` builds a dictionary in one line: for $a = 1, \dots, 8$ (`range(1, 9)` runs from 1 up to, but not including, 9) it stores the matrix as a numpy array of whole numbers (`dtype=int`), so that every product below is exact. `eta` stores the eight signs of the frame metric in the same way, and `np.eye(16, dtype=int)` is the identity matrix $I_{16}$. The `say` line prints the list of the eight signs; its output, `eta = [1, 1, 1, -1, -1, -1, -1, 1] for x1, ..., x8`, is the frame metric $\eta$ of the notation paragraph of Section 10.1.

```python
clifford_ok = all(
    np.array_equal(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                   2 * (eta[a] if a == b else 0) * identity)
    for a in range(1, 9) for b in range(1, 9))  # all 64 pairs (a, b)
check(clifford_ok,
      "the 64 Clifford relations hold exactly (eta = diag(+,+,+,-,-,-,-,+))")
```

In Python the sign `@` multiplies two matrices. For each of the $8 \times 8 = 64$ pairs $(a, b)$ the expression compares $\gamma^{(x_a)}\gamma^{(x_b)} + \gamma^{(x_b)}\gamma^{(x_a)}$ with $2\eta_{ab}I_{16}$ (the factor is $\eta_{aa}$ when $a = b$ and 0 otherwise); `np.array_equal` is true only when all 256 entries agree. `all(...)` is true when the comparison holds for every pair. The check prints PASS: the Clifford relation of Section 10.1 holds exactly.

**In [3], the matrices C and B.**

```python
C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]  # the author's sigma16
B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4), a complex 16 x 16 matrix
B_file = np.array(fixture["B"]["re"]) + 1j * np.array(fixture["B"]["im"])
check_record(np.array_equal(B, B_file),
             "B = -i C gamma^(x4) equals the matrix B of the record",
             record="Revision/algebra/gammas.json, entry B")
```

The first two lines build $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$ and $B = -iC\gamma^{(x_4)}$; Python writes the imaginary unit $i$ as `1j`. The record stores $B$ too, its real and imaginary parts as two tables of numbers; `B_file` puts them together. The check compares the two matrices entry by entry and reproduces the record's entry `B`.

```python
purely_imaginary = np.all(B.real == 0)  # every entry is 0, +i or -i
hermitian = np.array_equal(B, B.conj().T)  # B^dagger = B
squares_to_one = np.array_equal(B @ B, np.eye(16))  # B^2 = I
trace_B = np.trace(B)  # the sum of the diagonal entries
eigenvalues_B = np.linalg.eigvalsh(B)  # the 16 real eigenvalues, sorted
n_plus = int(np.sum(eigenvalues_B > 0.5))  # how many are +1
n_minus = int(np.sum(eigenvalues_B < -0.5))  # how many are -1
```

These lines test the properties (B2) to (B5) of Section 10.2. `B.real == 0` is a table of truth values, and `np.all` is true when all are true. `B.conj().T` is the conjugate transpose $B^\dagger$ (`.conj()` conjugates every entry, `.T` transposes). `np.trace` is the trace. `np.linalg.eigvalsh` computes the eigenvalues of a Hermitian matrix, which are real, sorted from the smallest; `eigenvalues_B > 0.5` marks those that are $+1$, `np.sum` counts the marks, and `int` writes the count as an ordinary whole number.

```python
report("trace of B", int(round(abs(trace_B))))
report("eigenvalues of B equal to +1 and to -1", f"{n_plus} and {n_minus}")
check_record(purely_imaginary and hermitian and squares_to_one and trace_B == 0
             and (n_plus, n_minus) == (8, 8),
             "B is imaginary and Hermitian, B^2 = I, tr B = 0, signature (8, 8)",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "B_properties")
```

The two RESULT lines print the trace, 0, and the counts, 8 and 8. The check requires all four properties and the signature (8,8), and reproduces the check `B_properties` of `python-field-theory.json`.

**In [4], a heat map of three matrices.**

```python
from matplotlib.colors import LinearSegmentedColormap  # colour scales

BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
# A diverging colour scale: dark blue (negative), light grey (zero), red (positive).
DIVERGING = LinearSegmentedColormap.from_list(
    "blue_grey_red", ["#184f95", "#f0efec", "#e34948"])
# A sequential colour scale for sizes: almost white (zero) to dark blue (large).
SEQUENTIAL = LinearSegmentedColormap.from_list(
    "white_blue", ["#fcfcfb", "#86b6ef", "#184f95"])
```

A colour is written as a text `"#rrggbb"`, three two-digit numbers in base 16 for its red, green and blue parts. The first line of assignments gives four colours four names at once (Python assigns the values on the right to the names on the left in order); the colours stay distinguishable for colour-blind readers. A **colour scale** turns a number into a colour: `DIVERGING` runs from dark blue for $-1$ through light grey for 0 to red for $+1$, and `SEQUENTIAL` from almost white for 0 to dark blue for large values. `from_list` builds a scale that blends smoothly between the listed colours.

```python
def draw_matrix(ax, matrix, title, cmap=DIVERGING, vmin=-1.0, vmax=1.0):
    image = ax.imshow(matrix, cmap=cmap, vmin=vmin, vmax=vmax)
    size = matrix.shape[0]
    ticks = list(range(0, size, 3))  # every third row and column is labelled
    ax.set_xticks(ticks, [str(t + 1) for t in ticks])
    ax.set_yticks(ticks, [str(t + 1) for t in ticks])
    ax.grid(False)  # no grid lines on top of the squares
    ax.set_title(title)
    return image
```

A **heat map** draws a matrix as a grid of coloured squares, one for each entry. `ax` is one drawing area (matplotlib calls it an axes); `ax.imshow` draws the matrix with the colour scale `cmap`, where `vmin` and `vmax` are the numbers that get the two end colours. `matrix.shape[0]` is the number of rows. The tick marks are put at every third row and column, labelled from 1 (the computer counts from 0, the book from 1). The grid is switched off because it would cut through the squares. The function returns the drawn image, which a colour bar needs.

```python
# A purely imaginary B = i Y (Y real) is Hermitian exactly when -i Y^T = i Y,
# that is when Y^T = -Y: the imaginary part of B must be antisymmetric.
one_per_row = all(np.count_nonzero(M, axis=1).tolist() == [1] * 16
                  and np.count_nonzero(M, axis=0).tolist() == [1] * 16
                  for M in (gamma[4], C, B.imag))  # signed permutation matrices
check(np.array_equal(gamma[4].T, -gamma[4]) and np.array_equal(C.T, C)
      and np.array_equal(B.imag.T, -B.imag) and one_per_row,
      "gamma^(x4) and Im B are antisymmetric, C is symmetric, all signed permutations")
```

`np.count_nonzero(M, axis=1)` counts the nonzero entries in each row of $M$ and `axis=0` in each column; `.tolist()` turns the result into a list, and `[1] * 16` is the list of sixteen ones. So `one_per_row` is true when each of the three matrices $\gamma^{(x_4)}$, $C$ and the imaginary part of $B$ has exactly one nonzero entry in every row and every column. The check also tests that $\gamma^{(x_4)}$ is antisymmetric ($M^T = -M$), $C$ symmetric, and the imaginary part of $B$ antisymmetric. The two comment lines at the top give the reason for the last fact: if $B = iY$ with $Y$ real, then $B^\dagger = -iY^T$, and $B^\dagger = B$ means $Y^T = -Y$.

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
draw_matrix(axes[0], gamma[4], "$\\gamma^{(x_4)}$ (real, antisymmetric)")
draw_matrix(axes[1], C, "$C$ (real, symmetric)")
image = draw_matrix(axes[2], B.imag, "imaginary part of $B = -iC\\gamma^{(x_4)}$")
fig.colorbar(image, ax=list(axes), shrink=0.8, label="entry")
save_figure(fig, "gamma4_c_and_b", ...)
```

(The caption text, the third argument of `save_figure`, is shortened here to three dots; it is printed in full under the figure in Section 10.9.) `plt.subplots(1, 3, ...)` makes a figure with one row of three drawing areas, 11 by 4 inches. The titles are written in LaTeX, the mathematical notation of the book; inside a Python string a backslash is written twice. `fig.colorbar` adds the colour bar on the right, shared by the three maps. Figure 1 of Notebook 10a shows the result: in each of the three heat maps every row and every column has exactly one coloured square; $C$ is the same after reflection in the diagonal, while $\gamma^{(x_4)}$ and the imaginary part of $B$ change colour under that reflection. This is the picture of the table of $B$ in Section 10.2.

**In [5], the mode Hamiltonian as numbers.**

```python
def mode_hamiltonian(m, k):
    h = -1j * m * gamma[4]
    for a, k_a in k.items():
        h = h - k_a * (gamma[4] @ gamma[a])
    return h


def frequency_squared(m, k):
    return m ** 2 + sum(eta[a] * k_a ** 2 for a, k_a in k.items())
```

`mode_hamiltonian(m, k)` builds $h = -im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_ak_a\gamma^{(x_a)}$ of Section 10.3; `k` is a dictionary that gives the momenta of some of the directions, for example `{1: 0.3, 5: 0.4}`, and `k.items()` runs through its pairs (direction, momentum). Directions that are not listed have momentum 0. `frequency_squared(m, k)` returns $w^2 = m^2 + \sum_a\eta_{aa}k_a^2$ (`**` is the power in Python): the space-like momenta enter with $+$, the extra-time momenta with $-$.

```python
example = {1: 0.3, 2: -1.1, 3: 0.7, 5: 0.4, 6: 0.2, 7: -0.9, 8: 1.3}  # any numbers
h_example = mode_hamiltonian(1.7, example)
w2_example = frequency_squared(1.7, example)
report("w^2 for m = 1.7 and the example momenta", f"{w2_example:.6f}")
error = np.max(np.abs(h_example @ h_example - w2_example * np.eye(16)))
report("largest entry of h^2 - w^2 I (rounding only)", f"{error:.1e}")
check(error < 1e-12, "numerical example: h^2 = w^2 I at one generic point")
```

For the mass 1.7 and momenta along all seven slice directions the cell computes $w^2 = 2.89 + (0.09 + 1.21 + 0.49 + 1.69) - (0.16 + 0.04 + 0.81) = 5.36$, printed with six decimals (`:.6f`), and the largest size of an entry of $h^2 - w^2I_{16}$ (`np.abs` takes sizes, `np.max` the largest), printed in the exponent form `8.9e-16`, which means $8.9 \times 10^{-16}$: only rounding. numpy computes with about 16 significant digits, so its checks allow a tiny tolerance.

**In [6], the same, exactly.**

```python
g = {a: sp.Matrix(fixture["gamma"][a - 1]) for a in range(1, 9)}  # exact gammas
C_exact = g[8] * g[1] * g[2] * g[3]
B_exact = -sp.I * C_exact * g[4]
m = sp.Symbol("m", real=True)  # the mass: any real number
k_sym = {a: sp.Symbol(f"k{a}", real=True) for a in (1, 2, 3, 5, 6, 7, 8)}
```

The same gammas are stored as sympy matrices, which hold exact whole numbers; for sympy matrices `*` is the matrix product and `sp.I` is the imaginary unit. `sp.Symbol("m", real=True)` is a letter $m$ that stands for any real number, and `k_sym` holds the seven letters $k_1, k_2, k_3, k_5, k_6, k_7, k_8$. A computation with these letters holds for all their values at once: it is a proof.

```python
def mode_hamiltonian_exact(mass, k):
    h = -sp.I * mass * g[4]
    for a, k_a in k.items():
        h = h - k_a * g[4] * g[a]
    return h


zero = sp.zeros(16, 16)
h_sym = mode_hamiltonian_exact(m, k_sym)
w2_sym = m ** 2 + sum(eta[a] * k_sym[a] ** 2 for a in k_sym)
say(f"w^2 = {w2_sym}")
```

The function builds $h$ exactly; `h_sym` is $h$ for the letters, `w2_sym` the expression $w^2$, which the cell prints: `k1**2 + k2**2 + k3**2 - k5**2 - k6**2 - k7**2 + k8**2 + m**2` (sympy writes the power as `**`).

```python
square_ok = (h_sym * h_sym - w2_sym * sp.eye(16)).applyfunc(sp.expand) == zero
check_record(square_ok, "exact: h^2 = w^2 I for all real m and k",
             record="Revision/pairing/reports/wolfram-pairing.json, check "
                    "Q_one_particle_flat_dispersion")
krein_ok = (B_exact * h_sym - h_sym.H * B_exact).applyfunc(sp.expand) == zero
check_record(krein_ok,
             "exact: B h = h^dagger B for all real m and k (Krein self-adjoint)",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "mode_hamiltonian_B_selfadjoint_dispersion")
```

`applyfunc(sp.expand)` multiplies out every entry of a matrix, so that an entry that is zero for all values of the letters becomes literally 0; comparing with the zero matrix then decides the identity. The first check proves $h^2 = w^2I_{16}$ (Section 10.4) and reproduces the Wolfram check `Q_one_particle_flat_dispersion`; the second proves $Bh = h^\dagger B$ (`.H` is sympy's conjugate transpose; the letters are declared real, so their conjugates are themselves) and reproduces the sympy record check `mode_hamiltonian_B_selfadjoint_dispersion`.

**In [7], where h stops being Hermitian.**

```python
not_hermitian_part = (h_sym - h_sym.H).applyfunc(sp.expand)
commutator = (B_exact * h_sym - h_sym * B_exact).applyfunc(sp.expand)
symbols_1 = sorted(str(s) for s in not_hermitian_part.free_symbols)
symbols_2 = sorted(str(s) for s in commutator.free_symbols)
say(f"symbols in h - h^dagger: {symbols_1}")
say(f"symbols in B h - h B:    {symbols_2}")
```

The cell computes the exact matrices $h - h^\dagger$ and $Bh - hB$. `.free_symbols` is the set of the letters that occur in an expression; `sorted(str(s) for s in ...)` writes them as a sorted list of names (a set has no fixed order, a sorted list has). Both printed lists are `['k5', 'k6', 'k7']`: only the extra-time momenta make $h$ non-Hermitian and make it fail to commute with $B$, as Section 10.4 derived from $h = h_H + h_A$.

```python
good_sector = {k_sym[5]: 0, k_sym[6]: 0, k_sym[7]: 0}  # no extra-time momentum
check_record(symbols_1 == ["k5", "k6", "k7"]
             and not_hermitian_part.subs(good_sector) == zero,
             "exact: h is Hermitian exactly in the good sector k5 = k6 = k7 = 0",
             record="Revision/theory/reports/wolfram-field-theory.json, check "
                    "mode_hamiltonian_good_sector")
check_record(symbols_2 == ["k5", "k6", "k7"]
             and commutator.subs(good_sector) == zero,
             "exact: B h = h B exactly in the good sector",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "good_sector_spectrum_and_B_sectors")
```

`.subs(good_sector)` replaces $k_5$, $k_6$, $k_7$ by 0. The two checks require that only these letters occur and that both matrices vanish when they are 0, and reproduce the two record checks named.

**In [8], the squared frequency against the extra-time momentum.**

```python
k5_values = np.linspace(0.0, 3.0, 301)  # 301 values of k5 from 0 to 3
fig, ax = plt.subplots()
for k_s, colour in ((0.0, BLUE), (1.0, ORANGE), (2.0, GREEN)):
    w2_curve = [frequency_squared(1.0, {1: k_s, 5: k5}) for k5 in k5_values]
    ax.plot(k5_values, w2_curve, color=colour, linewidth=2,
            label=f"$k_s = {k_s:.0f}$")
    crossing = np.sqrt(1.0 + k_s ** 2)  # where w^2 = 0
    ax.plot([crossing], [0.0], "o", color=colour, markersize=8)
```

`np.linspace(0.0, 3.0, 301)` is a list of 301 equally spaced numbers from 0 to 3. For the mass 1 and three space-like momenta $k_s = 0, 1, 2$ (put along $x_1$) the loop computes $w^2 = 1 + k_s^2 - k_5^2$ at every $k_5$ (a **list comprehension** `[... for k5 in k5_values]` builds the list in one line), draws it as a line (`ax.plot(x, y, ...)`), and marks with a dot (`"o"`) the point $k_5 = \sqrt{1 + k_s^2}$ where $w^2 = 0$.

```python
ax.axhline(0.0, color=GREY, linewidth=1)
ax.text(0.1, 3.0, "$w^2 > 0$: real frequency, the wave oscillates", color=GREY)
ax.text(0.1, -6.0, "$w^2 < 0$: imaginary frequency, the wave grows", color=GREY)
ax.set_xlabel("momentum $k_5$ along the extra time $x_5$")
ax.set_ylabel("$w^2 = m^2 + k_s^2 - k_5^2$")
ax.set_title("The squared frequency of a plane wave, $m = 1$")
ax.legend(title="space-like momentum")
save_figure(fig, "frequency_squared", ...)
```

`axhline` draws a horizontal line at height 0; `ax.text` writes a text at a point of the plot; the labels name the axes; `ax.legend` lists the three curves with their labels. Figure 2 of Notebook 10a shows three downward parabolas, one for each $k_s$, each crossing zero at its dot: above the grey line the wave oscillates, below it the wave grows. A larger space-like momentum moves the crossing to the right, but every curve crosses: a large enough extra-time momentum always wins.

```python
check(all(abs(frequency_squared(1.0, {1: k_s, 5: np.sqrt(1.0 + k_s ** 2)})) < 1e-12
          for k_s in (0.0, 1.0, 2.0)),
      "w^2 = 0 exactly at k5 = sqrt(m^2 + k_s^2)")
```

The check confirms that $w^2$ vanishes at the three dots, up to rounding.

**In [9], the eigenvalues as $k_5$ grows.**

```python
real_parts, imaginary_parts, worst = [], [], 0.0
for k5 in k5_values:
    eigenvalues = np.linalg.eigvals(mode_hamiltonian(1.0, {5: k5}))
    real_parts.append(np.sort(eigenvalues.real))
    imaginary_parts.append(np.sort(eigenvalues.imag))
```

For each of the 301 values of $k_5$ (mass 1, no other momentum) `np.linalg.eigvals` computes the 16 eigenvalues of $h$, which may be complex numbers; their real parts and their imaginary parts are sorted and stored for the figure.

```python
    w2 = 1.0 - k5 ** 2
    if abs(w2) > 0.05:  # away from the point where h cannot be diagonalised
        w = np.sqrt(complex(w2))  # sqrt of a negative number is imaginary
        predicted = np.array([w] * 8 + [-w] * 8)
        # compare the sorted real parts and the sorted imaginary parts separately
        worst = max(worst,
                    np.max(np.abs(np.sort(eigenvalues.real) - np.sort(predicted.real))),
                    np.max(np.abs(np.sort(eigenvalues.imag) - np.sort(predicted.imag))))
report("largest difference from the formula +-w (8 times each)", f"{worst:.1e}")
check(worst < 1e-10, "the 16 eigenvalues of h are +w and -w, eight times each")
```

The predicted eigenvalues are $+w$ eight times and $-w$ eight times; `complex(w2)` makes $w^2$ a complex number, so that `np.sqrt` of a negative number gives the imaginary $i\kappa$ instead of an error. At $k_5 = 1$ exactly, $h^2 = 0$ but $h \neq 0$: such a matrix has no basis of eigenvectors, and numerical eigenvalues are then only accurate to about $10^{-8}$; points with $|w^2| < 0.05$ are therefore left out of the comparison. `worst` keeps the largest difference seen; it is printed as `3.6e-15`, so the formula holds to rounding.

```python
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.0), sharex=True)
axes[0].plot(k5_values, np.array(real_parts), color=BLUE, linewidth=2)
axes[1].plot(k5_values, np.array(imaginary_parts), color=ORANGE, linewidth=2)
for ax, what in ((axes[0], "real part"), (axes[1], "imaginary part")):
    ax.axvline(1.0, color=GREY, linestyle=":", linewidth=1)
    ax.set_xlabel("momentum $k_5$ along the extra time $x_5$ ($m = 1$)")
    ax.set_ylabel(f"{what} of the eigenvalues of $h$")
axes[0].set_title("oscillation: real frequencies $\\pm w$")
axes[1].set_title("growth: imaginary frequencies $\\pm i\\kappa$")
save_figure(fig, "eigenvalue_flow", ...)
```

`np.array(real_parts)` is a table with one row per $k_5$ and 16 columns; `plot` draws each column as a curve. `sharex=True` gives both panels the same horizontal axis, and `axvline` draws a dotted vertical line at $k_5 = 1$. Figure 3 of Notebook 10a shows the real parts $\pm\sqrt{1 - k_5^2}$ closing in to 0 at $k_5 = 1$ and staying 0 afterwards, while the imaginary parts are 0 before and open up as $\pm\sqrt{k_5^2 - 1}$ afterwards: oscillation turns into growth. Each curve carries eight eigenvalues on top of each other.

**In [10], three functions for the Krein inertia.**

```python
def orthonormal_basis(P):
    basis = []
    for column in P.T:  # the columns of P, in order
        v = column.astype(complex)
        for _ in range(2):  # the second pass removes rounding errors
            for e in basis:
                v = v - (e.conj() @ v) * e  # remove the part of v along e
        length = np.sqrt((v.conj() @ v).real)
        if length > 1e-8:  # v is not a combination of the earlier columns
            basis.append(v / length)
    return np.array(basis).T  # the basis vectors as the columns of a matrix
```

This is the **Gram-Schmidt method**. Two columns are **orthonormal** when each has length 1 and $e^\dagger v = 0$ between them. Going through the columns of $P$ in order (`P.T` lists the columns of $P$ as rows), the function removes from each column $v$ its part along every basis vector $e$ found so far ($e^\dagger v$ is the size of that part, and `e.conj() @ v` computes it), and keeps what is left, divided by its length $\sqrt{v^\dagger v}$, if anything is left. The removal is done twice, because the first pass leaves tiny rounding errors. A column that is a combination of the earlier ones leaves nothing (a length below $10^{-8}$) and is skipped. The result is a matrix whose columns are an orthonormal basis of the range of $P$; `for _ in range(2)` repeats a block twice without needing the counter.

```python
def eigenspace(m, k, sign):
    h = mode_hamiltonian(m, k)
    w = np.sqrt(complex(frequency_squared(m, k)))  # w, or i kappa when w^2 < 0
    P = (np.eye(16) + sign * h / w) / 2  # the projector P_+ or P_-
    return orthonormal_basis(P)
```

`eigenspace(m, k, sign)` builds the projector $P_\pm = \frac12(I_{16} \pm h/w)$ of Section 10.5 and returns an orthonormal basis of its range, the eigenspace of $+w$ (`sign = +1`) or $-w$ (`sign = -1`). For $w^2 < 0$ the number $w$ is $i\kappa$, and the same formula gives the eigenspaces of $\pm i\kappa$.

```python
def krein_inertia(V):
    G = V.conj().T @ B @ V  # the Krein form on the span of the columns of V
    values = np.linalg.eigvalsh(G)
    nonzero = np.abs(values[np.abs(values) > 1e-8])
    counts = (int(np.sum(values > 1e-8)), int(np.sum(values < -1e-8)),
              int(np.sum(np.abs(values) <= 1e-8)))
    return counts, (float(nonzero.min()) if nonzero.size else None)
```

`krein_inertia(V)` forms the Gram matrix $G = V^\dagger BV$ of the columns of $V$ (Section 10.5) and counts its positive, negative and zero eigenvalues, "zero" meaning smaller in size than $10^{-8}$. It returns the triple $(p, n, z)$ and, in addition, the smallest size of a nonzero eigenvalue (or `None`, Python's word for "nothing", when all are zero), to show that no eigenvalue lies near the borderline $10^{-8}$. `values[np.abs(values) > 1e-8]` picks out the eigenvalues that are not zero.

**In [11], the eight recorded samples.**

```python
pairing = json.loads(repository_file("Revision/pairing/pairing-theory.json")
                     .read_text(encoding="utf-8"))
samples = pairing["data"]["one_particle_flat"]["samples"]
all_agree = True
say("   m  nonzero momenta         w      dims   inertia(+w)  inertia(-w)")
```

The cell reads the pairing record and takes the list of eight samples stored under `data`, `one_particle_flat`, `samples`. Each sample is a dictionary with a mass `m`, a list `k` of eight momenta $(k_1, \dots, k_8)$ (the entry $k_4$ is not used), the frequency `w` as text, the dimensions of the two eigenspaces and their Krein inertia. The `say` line prints the header of the table.

```python
for sample in samples:
    m_value, k_list = sample["m"], sample["k"]
    k = {a: k_list[a - 1] for a in (1, 2, 3, 5, 6, 7, 8) if k_list[a - 1] != 0}
    # "Sqrt[2]" (Wolfram notation) -> the number sqrt(2)
    w_recorded = float(sp.sympify(sample["w"].replace("Sqrt[", "sqrt(")
                                  .replace("]", ")")))
    w = np.sqrt(frequency_squared(m_value, k))
```

For each sample the loop builds the dictionary of the nonzero momenta (the `if` inside the comprehension skips the zeros). The record writes the frequency in the notation of the Wolfram Language, for example `Sqrt[2]`; `.replace` turns it into the sympy notation `sqrt(2)`, `sp.sympify` reads that text as an exact number, and `float` gives its decimal value. `w` is the frequency recomputed from $m$ and $k$.

```python
    found = []
    for sign in (+1, -1):
        V = eigenspace(m_value, k, sign)
        counts, _ = krein_inertia(V)
        found.append((V.shape[1], counts))
```

For both eigenspaces the loop computes a basis, its dimension (`V.shape[1]`, the number of columns) and its Krein inertia; the underscore receives the second result of `krein_inertia`, which is not needed here.

```python
    agree = (abs(w - w_recorded) < 1e-12
             and found[0][0] == sample["dim_plus_w"]
             and found[1][0] == sample["dim_minus_w"]
             and list(found[0][1][:2]) == sample["B_inertia_plus_w"]
             and list(found[1][1][:2]) == sample["B_inertia_minus_w"]
             and found[0][1][2] == 0 and found[1][1][2] == 0)
    all_agree = all_agree and agree
```

`agree` requires the frequency, both dimensions and both inertias to equal the recorded ones, and no zero eigenvalue (`[:2]` takes the first two numbers of a triple, `[2]` the third). `all_agree` stays true only if every sample agrees.

```python
    momenta = ", ".join(f"k{a}={v}" for a, v in k.items()) or "none"
    say(f"{m_value:4d}  {momenta:22s} {w:7.4f}   {found[0][0]},{found[1][0]}    "
        f"{found[0][1][:2]}       {found[1][1][:2]}")
check_record(all_agree,
             "all 8 recorded samples: w, dimensions 8 and 8, Krein inertia (4, 4)",
             record="Revision/pairing/pairing-theory.json, data one_particle_flat")
```

`", ".join(...)` writes the momenta as one text separated by commas, or the word `none` when there is no momentum (an empty text counts as false, so `or` takes the second value). The format codes fix the widths of the columns: `:4d` a whole number in 4 places, `:22s` a text in 22 places, `:7.4f` a decimal number in 7 places with 4 decimals. The printed table has one line per sample: for the masses $\pm2$ with $(k_1, k_2, k_8) = (1, 2, 4)$ the frequency is $5 = \sqrt{4 + 1 + 4 + 16}$; for $\pm3$ at rest it is 3; for $\pm1$ with $k_1 = 1$ it is $1.4142 = \sqrt2$; for $\pm2$ with the extra-time momentum $k_5 = 1$ it is $1.7321 = \sqrt3$. Every line shows the dimensions 8 and 8 and the inertia (4, 4) on both eigenspaces, the same for $+m$ and $-m$, and the check reproduces the record's data `one_particle_flat`.

**In [12], one more real-frequency sample and the neutral eigenspaces.**

```python
sample_3 = {1: 2, 8: 2}
inertias_3 = [krein_inertia(eigenspace(1, sample_3, s))[0] for s in (+1, -1)]
report("w for m = 1, k1 = 2, k8 = 2", f"{np.sqrt(frequency_squared(1, sample_3)):.6f}")
say(f"inertia of the +w and -w eigenspaces: {inertias_3}")
check_record(inertias_3 == [(4, 4, 0), (4, 4, 0)],
             "m = 1, k1 = 2, k8 = 2 (w = 3): inertia (4, 4) on both eigenspaces",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.one_particle_Krein_inertia")
```

The sympy pairing verifier uses the sample $m = 1$, $k_1 = 2$, $k_8 = 2$, so $w = \sqrt{1 + 4 + 4} = 3$, printed as `3.000000`. The inertia of both eigenspaces is printed as `[(4, 4, 0), (4, 4, 0)]` and reproduces the check `Q.one_particle_Krein_inertia`.

```python
neutral_ok = True
for k in ({5: 2}, {1: 1, 5: 2}):
    spaces = [eigenspace(1, k, s) for s in (+1, -1)]
    inertias = [krein_inertia(V)[0] for V in spaces]
    say(f"m = 1, momenta {k}: w^2 = {frequency_squared(1, k)}, dimensions "
        f"{[V.shape[1] for V in spaces]}, inertia {inertias}")
    neutral_ok = neutral_ok and inertias == [(0, 0, 8), (0, 0, 8)]
```

Two imaginary-frequency samples of the record: $m = 1$ with $k_5 = 2$ ($w^2 = 1 - 4 = -3$) and with $k_1 = 1$, $k_5 = 2$ ($w^2 = 1 + 1 - 4 = -2$). The printed lines show dimensions 8 and 8 and the inertia $(0, 0, 8)$ for both eigenspaces: they are Krein-neutral, as the last part of the proof of Theorem 10.1 says.

```python
h_zero = mode_hamiltonian(1, {5: 1})  # w^2 = 1 - 1 = 0
rank_h = int(np.linalg.matrix_rank(h_zero))
nilpotent = np.max(np.abs(h_zero @ h_zero)) < 1e-12  # h^2 = 0
range_neutral = np.max(np.abs(h_zero.conj().T @ B @ h_zero)) < 1e-12
say(f"m = 1, k5 = 1: w^2 = 0, h^2 = 0: {nilpotent}, rank of h = {rank_h}, "
    f"range of h neutral: {range_neutral}")
check_record(neutral_ok and nilpotent and rank_h == 8 and range_neutral,
             "imaginary and zero frequencies: the eigenspaces are Krein-neutral",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.one_particle_complex_frequency_Krein_neutral")
```

The zero-frequency sample $m = 1$, $k_5 = 1$: `np.linalg.matrix_rank` is the **rank** of a matrix, the number of its independent columns. The cell checks $h^2 = 0$, rank 8, and that $h^\dagger Bh = 0$, which says that the columns of $h$ (and so its whole range) have zero Krein form with each other. The printed line shows `True`, 8 and `True`, and the check reproduces the record.

**In [13], steps (i) and (ii) of the proof, exactly.**

```python
w = sp.Symbol("w", positive=True)
I16 = sp.eye(16)


def replace_w_squared(matrix):
    return matrix.applyfunc(lambda e: sp.expand(sp.expand(e).subs(w ** 2, w2_sym)))
```

`w` is now a positive letter. A **lambda** is a function written in one line without a name: `lambda e: ...` takes an entry `e`, multiplies it out, replaces every $w^2$ by $m^2 + k_s^2 - k_t^2$ (the expression `w2_sym` of In [6]) and multiplies out again. `replace_w_squared` does this for every entry of a matrix.

```python
step_i_a = replace_w_squared((w * I16 + h_sym.H) * B_exact * (w * I16 - h_sym))
step_i_b = replace_w_squared((w * I16 + h_sym.H) * B_exact * (w * I16 + h_sym)
                             - 2 * w * B_exact * (w * I16 + h_sym))
check_record(step_i_a == zero and step_i_b == zero,
             "exact step (i): 4 w^2 P+^dagger B P- = 0 and P+^dagger B P+ = B P+",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.one_particle_Krein_inertia_proof")
```

`step_i_a` is $(wI + h^\dagger)B(wI - h) = 4w^2P_+^\dagger BP_-$, and `step_i_b` is $(wI + h^\dagger)B(wI + h) - 2wB(wI + h)$, which is $4w^2(P_+^\dagger BP_+ - BP_+)$. Both vanish exactly, which is step (i) of Theorem 10.1, and the check reproduces `Q.one_particle_Krein_inertia_proof`.

```python
trace_B_h = sp.expand((B_exact * h_sym).trace())
say(f"exact: tr B = {B_exact.trace()}, tr(B h) = {trace_B_h}")
check(B_exact.trace() == 0 and trace_B_h == 0,
      "exact step (ii): tr B = tr(B h) = 0, so tr(B P+) = tr(B P-) = 0")
```

The exact traces of $B$ and of $Bh$ are printed as 0 and 0; with them $\mathrm{tr}(BP_\pm) = 0$, step (ii).

**In [14], step (iii) at work: a scan across the threshold.**

```python
threshold = np.sqrt(1.25)
scan = [k5 for k5 in np.linspace(0.0, 2.5, 251) if abs(k5 - threshold) > 0.02]
counts_scan, margins = [], []
for k5 in scan:
    counts, margin = krein_inertia(eigenspace(1.0, {1: 0.5, 5: k5}, +1))
    counts_scan.append(counts)
    if margin is not None:
        margins.append(margin)
```

For $m = 1$ and $k_1 = 0.5$ the frequency is real while $k_5 < \sqrt{1 + 0.25} = \sqrt{1.25} \approx 1.118$. The list `scan` holds 251 values of $k_5$ from 0 to 2.5 without those closer than 0.02 to the threshold (there the two eigenspaces merge and the numbers become inaccurate). For each value the loop stores the inertia of the $+w$ eigenspace and the smallest size of a nonzero Gram eigenvalue.

```python
below = [c for k5, c in zip(scan, counts_scan) if k5 < threshold]
above = [c for k5, c in zip(scan, counts_scan) if k5 > threshold]
report("points below and above the threshold", f"{len(below)} and {len(above)}")
report("smallest nonzero Gram eigenvalue below the threshold", f"{min(margins):.4f}")
check(set(below) == {(4, 4, 0)} and set(above) == {(0, 0, 8)},
      "scan: inertia (4, 4) at every real frequency, (0, 0, 8) at every imaginary "
      "one")
```

`zip` pairs each $k_5$ with its inertia. The cell prints 110 points below and 137 above the threshold, and the smallest nonzero Gram eigenvalue below the threshold, 0.2225: well away from 0, as step (iii) requires. `set(below)` is the set of the different inertias found below the threshold; the check requires it to be the single triple $(4, 4, 0)$, and above the threshold the single triple $(0, 0, 8)$.

```python
counts_array = np.array(counts_scan)  # one row (positive, negative, zero) per k5
fig, ax = plt.subplots()
width = 0.0105  # a little wider than the step 0.01 between the k5 values (no gaps)
# Stacked bars: the blue part (positive directions) starts at 0, the orange part
# (negative directions) on top of it, the green part (neutral) on top of both.
ax.bar(scan, counts_array[:, 0], width=width, color=BLUE,
       label="positive charge $u^\\dagger B u > 0$")
ax.bar(scan, counts_array[:, 1], width=width, bottom=counts_array[:, 0],
       color=ORANGE, label="negative charge $u^\\dagger B u < 0$")
ax.bar(scan, counts_array[:, 2], width=width,
       bottom=counts_array[:, 0] + counts_array[:, 1], color=GREEN,
       label="neutral (the form vanishes)")
```

`counts_array[:, 0]` is the first column of the table (the positive counts), and so on. `ax.bar` draws one thin bar at each $k_5$ (the variable `width`, 0.0105, is a little more than the step 0.01 between neighbouring values of $k_5$, so that the bars touch); as the two comment lines say, `bottom=` stacks the second kind of bar on top of the first and the third on top of both, so each full bar has the height 8, split by colour into positive, negative and neutral directions.

```python
ax.axvline(threshold, color=GREY, linestyle=":", linewidth=1)
ax.set_xlabel("momentum $k_5$ along the extra time ($m = 1$, $k_1 = 0.5$)")
ax.set_ylabel("directions in the $+w$ eigenspace")
ax.set_yticks(range(0, 9))
ax.set_ylim(0.0, 10.5)  # room for the legend above the bars
ax.set_title("Krein inertia of one eigenspace across the threshold")
ax.legend(loc="upper center", ncol=3, fontsize=8)
save_figure(fig, "krein_inertia_scan", ...)
```

The dotted line marks the threshold; the vertical axis is labelled 0 to 8 and extended to 10.5 to leave room for the legend, which is written in three columns at the top. Figure 4 of Notebook 10a shows bars that are half blue and half orange left of the threshold and entirely green right of it: the waves of real frequency mix the two signs of charge four and four, the growing waves carry no charge.

**In [15], the Gram matrices of three waves.**

```python
cases = [(2, {1: 1, 2: 2, 8: 4}, "$m = 2$, $k = (1, 2, 0, 4)$: $w = 5$"),
         (2, {5: 1}, "$m = 2$, $k_5 = 1$: $w = \\sqrt{3}$"),
         (1, {5: 2}, "$m = 1$, $k_5 = 2$: $w = i\\sqrt{3}$")]
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2))
block_sizes = []
```

Three waves are compared: a good-sector wave with $w = 5$, a wave with extra-time momentum and a real frequency $w = \sqrt{4 - 1} = \sqrt3$, and a wave with an imaginary frequency $w = \sqrt{1 - 4} = i\sqrt3$. Each entry of `cases` holds the mass, the momenta and the title of its panel.

```python
for ax, (m_value, k, title) in zip(axes, cases):
    W = np.hstack([eigenspace(m_value, k, +1), eigenspace(m_value, k, -1)])
    gram = np.abs(W.conj().T @ B @ W)  # sizes of the Krein form between columns
    image = draw_matrix(ax, gram, title, cmap=SEQUENTIAL, vmin=0.0, vmax=1.0)
    ax.axhline(7.5, color=GREY, linewidth=1)  # the border between the two
    ax.axvline(7.5, color=GREY, linewidth=1)  # eigenspaces (rows/columns 8 and 9)
```

`np.hstack` puts the 8 basis columns of the $+w$ eigenspace and the 8 of the $-w$ eigenspace side by side into one $16 \times 16$ matrix $W$. `gram` holds the sizes of the entries of $W^\dagger BW$, the Krein form between every pair of these columns, drawn with the white-to-blue scale; grey lines separate the two eigenspaces.

```python
    diagonal_blocks = max(gram[:8, :8].max(), gram[8:, 8:].max())
    off_blocks = max(gram[:8, 8:].max(), gram[8:, :8].max())
    block_sizes.append((diagonal_blocks, off_blocks))
    say(f"case {len(block_sizes)}: largest entry in the diagonal blocks "
        f"{diagonal_blocks:.3f}; off-diagonal blocks below 1e-12: {off_blocks < 1e-12}")
fig.colorbar(image, ax=list(axes), shrink=0.8, label="size of the entry")
save_figure(fig, "krein_gram_matrices", ...)
```

`gram[:8, :8]` is the upper left $8 \times 8$ block (rows and columns 1 to 8), `gram[8:, 8:]` the lower right one, and the two others are the off-diagonal blocks. The printed lines show, for the first two cases, diagonal blocks with entries up to 0.894 and 0.866 and empty off-diagonal blocks (`True`), and for the third case empty diagonal blocks (`0.000`) and filled off-diagonal blocks (`False`). Figure 5 of Notebook 10a shows exactly this: for a real frequency the two eigenspaces are Krein-orthogonal (step (i)); for an imaginary frequency each eigenspace is neutral, and a growing wave has a nonzero Krein form only with a decaying one.

```python
check(block_sizes[0][1] < 1e-12 and block_sizes[1][1] < 1e-12
      and block_sizes[2][0] < 1e-12 and block_sizes[2][1] > 0.1,
      "real w: the eigenspaces are Krein-orthogonal; imaginary w: each is neutral")
```

The check states the same in numbers.

**In [16], the universes of masses $+m$ and $-m$.**

```python
Gamma_exact = g[8] * g[1] * g[2] * g[3] * g[4] * g[5] * g[6] * g[7]
h_minus = mode_hamiltonian_exact(-m, k_sym)  # the same momenta, mass -m
k_reflected = dict(k_sym)
k_reflected[8] = -k_sym[8]  # R_8: k8 -> -k8
h_minus_reflected = mode_hamiltonian_exact(-m, k_reflected)
```

The exact chirality $\Gamma$ is the product of the eight gammas in the author's order. `h_minus` is $h_{-m}(k)$; `dict(k_sym)` makes a copy of the dictionary of momenta, in which $k_8$ is replaced by $-k_8$, and `h_minus_reflected` is $h_{-m}(R_8k)$.

```python
chirality_ok = (Gamma_exact * h_sym * Gamma_exact - h_minus).applyfunc(
    sp.expand) == zero
mirror_ok = (g[8] * h_sym * g[8] - h_minus_reflected).applyfunc(sp.expand) == zero
check_record(Gamma_exact * Gamma_exact == I16 and chirality_ok,
             "exact: Gamma h_m(k) Gamma = h_-m(k)",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.one_particle_maps")
check_record(mirror_ok, "exact: gamma^(x8) h_m(k) gamma^(x8) = h_-m(R_8 k)",
             record="Revision/pairing/reports/wolfram-pairing.json, check "
                    "Q_one_particle_maps")
```

The two identities of Section 10.6 are checked exactly, for all $m$ and $k$, with $\Gamma\Gamma = I_{16}$; they reproduce the sympy and the Wolfram record.

**In [17], the B-sectors of the good sector and the two spectra.**

```python
h_sample = mode_hamiltonian(2, {1: 1, 2: 2, 8: 4})
P_B = (np.eye(16) + B) / 2  # projector onto the eigenvalue +1 of B
sector_values = np.round(np.linalg.eigvals(P_B @ h_sample @ P_B).real, 10)
multiplicities = {v: int(np.sum(sector_values == v)) for v in (5.0, -5.0, 0.0)}
say(f"eigenvalues of P_B h P_B and how often each occurs: {multiplicities}")
check_record(multiplicities == {5.0: 4, -5.0: 4, 0.0: 8},
             "good sector, m = 2, k = (1, 2, 0, 4): on B = +1 energies +5, -5 (4 each)",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "good_sector_spectrum_and_B_sectors")
```

In the good sector $B$ commutes with $h$, so the projector $P_B = \frac12(I_{16} + B)$ onto the eight columns with $Bu = u$ commutes with $h$, and $h$ acts inside that 8-dimensional space. The eigenvalues of $P_BhP_B$ are those of $h$ on that space, together with 0 for the eight directions that $P_B$ removes. `np.round(..., 10)` rounds them to 10 decimals so that equal values compare equal. The printed dictionary `{5.0: 4, -5.0: 4, 0.0: 8}` says: on the $B = +1$ sector the energies are $+5$ and $-5$, four of each, as step (ii) of Theorem 10.1 requires; this is the record's exact example.

```python
k1_values = np.linspace(0.0, 4.0, 41)
plus_spectra = [np.sort(np.linalg.eigvals(mode_hamiltonian(2.0, {1: x})).real)
                for x in k1_values]
minus_spectra = [np.sort(np.linalg.eigvals(mode_hamiltonian(-2.0, {1: x})).real)
                 for x in k1_values]
mass_values = np.linspace(-3.0, 3.0, 61)
mass_spectra = [np.sort(np.linalg.eigvals(mode_hamiltonian(x, {1: 1.0})).real)
                for x in mass_values]
difference = np.max(np.abs(np.array(plus_spectra) - np.array(minus_spectra)))
report("largest difference between the spectra of m = 2 and m = -2", f"{difference:.1e}")
check(difference < 1e-10, "numerical: the spectra of h_m and h_-m coincide")
```

The sorted eigenvalues of $h$ are computed for $m = +2$ and $m = -2$ at 41 values of $k_1$ from 0 to 4, and at $k_1 = 1$ for 61 masses from $-3$ to 3. The largest difference between the spectra of $+2$ and $-2$ is printed as `0.0e+00`: identical.

```python
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.0))
axes[0].plot(k1_values, np.array(plus_spectra)[:, [0, 15]], color=BLUE, linewidth=2)
axes[0].plot(k1_values, np.array(minus_spectra)[:, [0, 15]], "o", color=ORANGE,
             markersize=5, fillstyle="none")
axes[0].plot([], [], color=BLUE, linewidth=2, label="$m = +2$ (line)")
axes[0].plot([], [], "o", color=ORANGE, fillstyle="none", label="$m = -2$ (circles)")
```

`[:, [0, 15]]` picks the smallest and the largest eigenvalue, $-w$ and $+w$ (the other fourteen lie on top of these two). The spectra of $+2$ are drawn as lines, those of $-2$ as open circles (`fillstyle="none"`). The two calls with empty lists draw nothing; they only create the entries of the legend.

```python
axes[0].set_xlabel("momentum $k_1$ (with $m = \\pm 2$)")
axes[0].set_ylabel("eigenvalues $\\pm w$ of $h$")
axes[0].set_title("same spectrum for $+m$ and $-m$")
axes[0].legend(loc="center left")
axes[1].plot(mass_values, np.array(mass_spectra)[:, [0, 15]], color=GREEN,
             linewidth=2)
axes[1].set_xlabel("mass $m$ (with $k_1 = 1$)")
axes[1].set_ylabel("eigenvalues $\\pm\\sqrt{m^2 + k_1^2}$ of $h$")
axes[1].set_title("the spectrum is even in $m$")
save_figure(fig, "plus_minus_mass_spectra", ...)
```

Figure 6 of Notebook 10a shows on the left the circles of $m = -2$ sitting exactly on the lines of $m = +2$, and on the right the eigenvalues $\pm\sqrt{m^2 + 1}$ against the mass: curves that are mirror images in the vertical axis $m = 0$. The one-particle spectra of the universes of masses $+m$ and $-m$ are identical, not opposite.

**In [18], the last check.**

```python
for name in ("10a_1_gamma4_c_and_b.png", "10a_2_frequency_squared.png",
             "10a_3_eigenvalue_flow.png", "10a_4_krein_inertia_scan.png",
             "10a_5_krein_gram_matrices.png", "10a_6_plus_minus_mass_spectra.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The loop checks that each of the six figure files exists in the figure folder, and `all_checks_passed()` prints the last line, ALL 28 CHECKS PASSED (notebook 10a): the six figure checks of this cell and the 22 checks of the cells before.

