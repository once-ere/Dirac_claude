## 10. Canonical quantisation in 4+4: Krein space and the good sector

Chapters 7 to 9 treated the field dirac16complex as a classical field: 16 complex anticommuting numbers $\Psi_1, \dots, \Psi_{16}$ at every point of the author's 4+4 dimensional universe, with a Lagrangian, a field equation and an energy-momentum tensor. This chapter makes the field a quantum field. It follows the standard recipe, canonical quantisation with the time $x_4$, step by step, and finds what is new in signature (4,4): the quantum rule contains the matrix $B$, which has eight positive and eight negative eigenvalues, so the space of quantum states cannot carry an ordinary positive inner product when the field operators are read in the ordinary way; it is a Krein space. In the good sector (waves that do not depend on the three extra times) a positive state space is constructed and checked for each single momentum with frozen coefficients (flat-frame plane waves, in which the deflation of the extra times does not enter), with particles and antiparticles of positive energy. The chapter shows exactly how far this goes, where it stops, and what the quantum theory says about the pairing of universes of masses $+m$ and $-m$.

### 10.1 What this chapter does

**Why quantise.** Dirac's equation of 1928 describes one electron as a classical wave. It has waves of negative energy, and a classical theory cannot say why an electron does not fall into them. Quantum field theory answers: the field becomes a collection of operators that create and destroy particles, the negative-energy waves describe antiparticles, and every particle and every antiparticle has positive energy. The same recipe is applied here to dirac16complex, the author's fermion field with 16 complex anticommuting components (a spinor of Pin(4,4), Chapter 5). The second field of the theory, dirac16complex00, with 16 commuting components, is a classical ("semi-classical") field in the author's definition and is not quantised; Section 10.22 shows what that means for its energy.

**What happens in signature (4,4).** The recipe has three steps: read off from the Lagrangian the term with the time derivative; turn it into an anticommutator of the field operators; find a space of quantum states on which operators with this anticommutator act. In ordinary 3+1 dimensional physics the anticommutator is the identity matrix and the state space is an ordinary Hilbert space. Here the anticommutator is the matrix $B = -iC\gamma^{(x_4)}$, and the chapter proves that no space with a positive inner product carries it when $\Psi^\dagger$ is read as the ordinary adjoint. That is the central fact of the chapter, and everything else is built around it:

- one-particle waves: the evolution of a plane wave conserves the Krein form $u^\dagger Bu$, its frequencies are real or imaginary according to the sign of $w^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$, and at every real frequency the waves of one frequency carry four directions of positive and four of negative Krein form (Sections 10.2 to 10.6, Notebook 10a);
- quantum states, fermion modes and the Fock space from zero, the canonical rule, the theorem that forces the Krein space, and the conjugation of the quantised field (Sections 10.11 to 10.15, Notebook 10b);
- the good sector and its positive Fock space (one momentum with frozen coefficients), the Dirac sea and normal ordering, the energy-momentum tensor operator, and the contrast with the classical commuting field (Sections 10.20 to 10.22, Notebook 10c);
- the curved good sector of the author's metric, where Hermiticity needs a boundary condition at the patch end $z = \pi/2$ (Sections 10.27 and 10.28, Notebook 10d);
- the proof that no invariant choice of the charge density is positive, and the symmetries that keep the canonical rule (Sections 10.33 and 10.34, Notebook 10e);
- the same structure along the deflating history of the extra times, where every wave with extra-time momentum eventually grows (Section 10.39, Notebook 10f);
- the quantum reading of the pairing of universes of masses $+m$ and $-m$, with an exact list of what it does not establish (Sections 10.44 and 10.45, Notebook 10g).

The chapter closes with "What we proved, what we computed, what we assumed" (Section 10.50), with exercises (Section 10.51) and with their complete answers (Section 10.52).

**The seven worked examples.** Each is a complete Jupyter notebook; each is complete in itself, so you may run them in any order.

| notebook | what it computes | checks | figures |
| --- | --- | --- | --- |
| 10a | one-particle spectra and Krein inertia | 28 | 6 |
| 10b | the canonical rule on a Fock space; the Krein space | 25 | 5 |
| 10c | the positive Fock space of one good-sector momentum | 14 | 5 |
| 10d | the curved good sector along the hidden direction | 16 | 5 |
| 10e | invariant forms and Krein-unitary generators | 15 | 5 |
| 10f | the Krein structure along the deflating history | 19 | 5 |
| 10g | the quantum reading of the pairing | 30 | 5 |

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
| `Revision/field_equations_a4/reports/ks-source-conditions.json` | the status of that history: a prescribed background |
| `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` | the theory document of the record (its sections 11 and 12: quantisation, the energy-momentum tensor operator) |
| `Revision/docs/PAIR_CREATION_PROOFS.md` | the proof document of the pairing (its section 6: the quantum reading Q) |

A report is a file in which a verifying program has recorded each check with its name, its verdict and a detail text; every check cited in this chapter has the verdict PASS. Below, a report is named by its file name only, for example "`python-field-theory.json`, check `canonical_anticommutator_B`".

### 10.2 The matrix B and the Krein form

**The charge.** Chapter 5 showed that the current of the field is $J^\mu = -i\bar\Psi\gamma^\mu\Psi$ with $\bar\Psi = \Psi^\dagger C$, and that its time component is the charge density

$$
J^{(x_4)} = -i\Psi^\dagger C\gamma^{(x_4)}\Psi = \Psi^\dagger B\Psi,\qquad B = -iC\gamma^{(x_4)} .
$$

The Revision record proves the **local conservation law** $\partial_\mu(\cos z\,J^\mu) = 0$ (summed over the eight directions $\mu$, as in Chapter 1) for every solution of the field equation (`charge-conjugation-and-u1.json`, check `u1_noether_matrix_identity`), and that $J^{(x_4)}$ is the density of the total charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$, the integral over a slice $x_4 = $ const (`wolfram-field-theory.json`, check `charge_density_is_Krein_form_G`). A local law does not by itself make $Q$ constant. Write it as $\partial_4(\cos z\,J^{(x_4)}) = -\sum_{a \neq 4}\partial_a(\cos z\,J^{(x_a)})$ and integrate over the slice: the left side gives $dQ/dx_4$, and each term on the right is the integral of a derivative along one direction, which by the fundamental theorem of calculus equals the difference of the values at the two ends of that direction. So $Q$ changes by exactly the charge that flows out through the boundary of the slice, and it is constant only when this **flux** vanishes. In flat space it vanishes for fields that die away at large distances. In the author's patch the boundary includes the patch end $z = \pi/2$, and there the flux vanishes only under a boundary condition, an ASSUMED no-flux condition that the quantisation of the Revision record does not impose; without it the constancy of $Q$ is OPEN (Revision theory document, section 11). Sections 10.27 and 10.28 show an exact solution whose charge $Q$ grows from $1/6$ to 454.007. For two columns $u$ and $v$ of 16 complex numbers the number $u^\dagger Bv$ is called their **Krein form**, and $u^\dagger Bu$ the **Krein norm** of $u$ (a name, not a length: it can be negative).

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

| row $r$ | column $c$ | entry $B_{rc}$ | row $r$ | column $c$ | entry $B_{rc}$ |
| --- | --- | --- | --- | --- | --- |
| 1 | 10 | $+i$ | 9 | 2 | $+i$ |
| 2 | 9 | $-i$ | 10 | 1 | $-i$ |
| 3 | 12 | $-i$ | 11 | 4 | $-i$ |
| 4 | 11 | $+i$ | 12 | 3 | $+i$ |
| 5 | 14 | $-i$ | 13 | 6 | $-i$ |
| 6 | 13 | $+i$ | 14 | 5 | $+i$ |
| 7 | 16 | $+i$ | 15 | 8 | $+i$ |
| 8 | 15 | $-i$ | 16 | 7 | $-i$ |

**Which gammas commute with B.** $B$ is $-i$ times the product of the five gammas of $x_8, x_1, x_2, x_3, x_4$. A gamma among these five passes four different gammas and itself when it is moved through the product, sign $(-1)^4 = +1$: it commutes with $B$. A gamma of $x_5, x_6, x_7$ passes five different gammas, sign $(-1)^5 = -1$: it anticommutes with $B$. Hence $B$ commutes with $\gamma^{(x_1)}, \gamma^{(x_2)}, \gamma^{(x_3)}, \gamma^{(x_4)}, \gamma^{(x_8)}$ and anticommutes with $\gamma^{(x_5)}, \gamma^{(x_6)}, \gamma^{(x_7)}$, and by the same counting $\Gamma B\Gamma = -B$.

| statement | status | where it is verified |
| --- | --- | --- |
| $B$ purely imaginary, Hermitian, $BB = I_{16}$, $\mathrm{tr}\,B = 0$, signature (8,8) | PROVED | `python-field-theory.json`, check `B_properties`; `wolfram-algebra.json`, check `B_signature_8_8` |
| $B$ commutes with the gammas of $x_1, x_2, x_3, x_4, x_8$, anticommutes with those of $x_5, x_6, x_7$ | PROVED | `python-algebra.json`, check `B_gamma_relations` |
| the local conservation law $\partial_\mu(\cos z\,J^\mu) = 0$ on shell; $J^{(x_4)} = \Psi^\dagger B\Psi$ | PROVED | `charge-conjugation-and-u1.json`, check `u1_noether_matrix_identity`; `wolfram-field-theory.json`, check `charge_density_is_Krein_form_G` |
| the total charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ is constant in time | OPEN (true only when no charge flows through the boundary; at $z = \pi/2$ this is an ASSUMED no-flux condition that the quantisation record does not impose, Sections 10.27 and 10.28) | Revision theory document, section 11 |

### 10.3 One plane wave: the mode Hamiltonian

We first study one wave of the field at a time, as a classical wave, before any quantisation. Take $U = 0$ (no self-interaction) and flat 4+4 space. Flat space is not the author's universe. The end of this section defines the **frozen-coefficient model** of the author's universe, which has the same equation with the derivatives divided by scale factors; it is an ASSUMPTION, because it also leaves out two terms of the author's field equation. The field equation in flat space is (Chapter 7)

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

**Frame momenta and the deflating extra times.** In the author's metric each derivative of the field equation is divided by the scale factor $f_a$ of its direction (Chapter 6): $f_a = e^{a_4}\sin^{1/6}z$ for $x_1, x_2, x_3$, $f_4 = 1$, $f_a = e^{-a_4}\sin^{1/6}z$ for $x_5, x_6, x_7$ and $f_8 = \cot z$ (record `Revision/theory/field-theory.json`, formula `vielbein_diagonal`). A wave $e^{iq_ax_a}$ with the **coordinate momentum** $q_a$ therefore enters the equation with the **frame momentum** $k_a = q_a/f_a$. Along 3-space $k_a = q_ae^{-a_4}\sin^{-1/6}z$ shrinks as 3-space inflates; along an extra time $k_a = q_ae^{a_4}\sin^{-1/6}z$ GROWS as the extra times deflate.

**The frozen-coefficient model, and what it leaves out.** The model evaluates the scale factors at one instant and one hidden position, so that the equation of that instant has constant coefficients and the plane waves above solve it with the frame momenta $k_a$; the extra times are never treated as static (Section 10.39 and Notebook 10f follow the frame momenta along the deflating history). But the author's field equation also contains two terms of the hidden direction (Section 10.27; record `Revision/theory/field-theory.json`, formula `field_equation`): the derivative $\tan z\,\gamma^{(x_8)}\partial_8\Psi$, whose coefficient changes along $x_8$, and the spin-connection term $3H\gamma^{(x_8)}\Psi$ (Chapter 6). The model leaves both out, so it is an ASSUMPTION, an approximation whose error this chapter does not estimate. The connection term matters. Kept in the equation, it adds to $h$ the matrix $h_c = 3iH\gamma^{(x_4)}\gamma^{(x_8)}$ (multiply $3H\gamma^{(x_8)}\Psi$ by $\gamma^{(x_4)}$ and by $i$, as in Steps 1 to 4). The real matrix $\gamma^{(x_4)}\gamma^{(x_8)}$ is symmetric (Chapter 5: $(\gamma^{(x_8)})^T = \gamma^{(x_8)}$ and $(\gamma^{(x_4)})^T = -\gamma^{(x_4)}$), $(\gamma^{(x_4)}\gamma^{(x_8)})^T = (\gamma^{(x_8)})^T(\gamma^{(x_4)})^T = \gamma^{(x_8)}(-\gamma^{(x_4)}) = \gamma^{(x_4)}\gamma^{(x_8)}$, so $h_c^\dagger = -h_c$; and $h_c$ commutes with $B$, because $\gamma^{(x_4)}$ and $\gamma^{(x_8)}$ do (Section 10.2). Section 10.4 proves $Bh = h^\dagger B$ for the flat $h$; for $h + h_c$ this becomes

$$
B(h + h_c) - (h + h_c)^\dagger B = (Bh - h^\dagger B) + Bh_c + h_cB = 2Bh_c = 6iH\,B\gamma^{(x_4)}\gamma^{(x_8)} \neq 0 ,
$$

by $h_c^\dagger = -h_c$ and $h_cB = Bh_c$; the right side is not zero because $B$, $\gamma^{(x_4)}$ and $\gamma^{(x_8)}$ are invertible. So with the connection term the Krein form of a single wave is no longer conserved, Theorem 10.1 below does not apply, and the frequencies can be complex: Section 10.28 finds $\pm2\sqrt2\,i$ for the waves that do not depend on $x_8$ at $m = H = 1$. Everything in Sections 10.4 to 10.6 and 10.20 holds exactly in flat 4+4 space and in the frozen-coefficient model; Sections 10.27 and 10.28 show what the terms of the hidden direction change.

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
(-i\gamma^{(x_4)})^\dagger = i(\gamma^{(x_4)})^T = -i\gamma^{(x_4)},
$$

$$
(\gamma^{(x_4)}\gamma^{(x_a)})^\dagger = (\gamma^{(x_a)})^T(\gamma^{(x_4)})^T = -\eta_{aa}\gamma^{(x_a)}\gamma^{(x_4)} = \eta_{aa}\gamma^{(x_4)}\gamma^{(x_a)} .
$$

So $-i\gamma^{(x_4)}$ and $\gamma^{(x_4)}\gamma^{(x_a)}$ for the space-like $a = 1, 2, 3, 8$ are Hermitian, while $\gamma^{(x_4)}\gamma^{(x_a)}$ for the extra times $a = 5, 6, 7$ is anti-Hermitian. Write $h = h_H + h_A$ with

$$
h_H = -im\gamma^{(x_4)} - \gamma^{(x_4)}\big(k_1\gamma^{(x_1)} + k_2\gamma^{(x_2)} + k_3\gamma^{(x_3)} + k_8\gamma^{(x_8)}\big),
$$

$$
h_A = -\gamma^{(x_4)}\big(k_5\gamma^{(x_5)} + k_6\gamma^{(x_6)} + k_7\gamma^{(x_7)}\big).
$$

$h_H$ is Hermitian and $h_A$ anti-Hermitian. By Section 10.2, $\gamma^{(x_4)}$ and the four space-like gammas commute with $B$, so $h_H$ commutes with $B$; the gammas of $x_5, x_6, x_7$ anticommute with $B$ while $\gamma^{(x_4)}$ commutes, so $h_A$ anticommutes with $B$. Two consequences:

- $h$ is Hermitian, and commutes with $B$, exactly when $k_5 = k_6 = k_7 = 0$: in the **good sector**, the waves that do not depend on the extra times;
- for all momenta, $h^\dagger B = (h_H - h_A)B = Bh_H + Bh_A = Bh$. In words, $h$ is **Krein self-adjoint**: $Bh = h^\dagger B$.

**The Krein form is conserved.** Let $u(x_4)$ solve $i\,du/dx_4 = hu$, so $du/dx_4 = -ihu$ and, taking the conjugate transpose, $du^\dagger/dx_4 = iu^\dagger h^\dagger$. By the product rule

$$
\frac{d}{dx_4}\big(u^\dagger Bu\big) = \frac{du^\dagger}{dx_4}Bu + u^\dagger B\frac{du}{dx_4} = iu^\dagger h^\dagger Bu - iu^\dagger Bhu = i\,u^\dagger\big(h^\dagger B - Bh\big)u = 0 .
$$

The last step is $h^\dagger B = Bh$. The Krein norm of every wave is constant in time, also when the wave grows; the ordinary squared length $u^\dagger u$ changes by $d(u^\dagger u)/dx_4 = iu^\dagger(h^\dagger - h)u = -2iu^\dagger h_Au$, which vanishes in the good sector only.

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

**Theorem 10.1 (Krein inertia of one-particle waves).** In flat 4+4 space (or in the frozen-coefficient model of Section 10.3, an ASSUMPTION that leaves out the connection term), for every real frequency, $w^2 > 0$, with or without extra-time momentum, each of the two eigenspaces of $h$ has dimension 8 and Krein inertia (4,4). For every imaginary frequency both eigenspaces are Krein-neutral, and for $w = 0$ the range of $h$ is Krein-neutral.

| statement | status | where it is verified |
| --- | --- | --- |
| Theorem 10.1, real frequencies: inertia (4,4) | PROVED | `wolfram-pairing.json`, check `Q_one_particle_Krein_inertia_real_frequencies`; `python-pairing.json`, check `Q.one_particle_Krein_inertia_proof` |
| Theorem 10.1, imaginary and zero frequencies: Krein-neutral | PROVED | `wolfram-pairing.json`, check `Q_one_particle_complex_and_zero_frequencies_Krein_neutral`; `python-pairing.json`, check `Q.one_particle_complex_frequency_Krein_neutral` |

*Proof, step (i): the two eigenspaces are Krein-orthogonal.* Let $w > 0$ be real, so $P_+^\dagger = \frac12(I_{16} + h^\dagger/w)$. Then

$$
4w^2\,P_+^\dagger BP_- = (wI_{16} + h^\dagger)\,B\,(wI_{16} - h) = w^2B - wBh + wh^\dagger B - h^\dagger Bh .
$$

The first step multiplies each projector by $2w$; the second multiplies out. By $h^\dagger B = Bh$ the two middle terms cancel, and $h^\dagger Bh = Bhh = w^2B$, so the right side is $w^2B - w^2B = 0$. A wave of frequency $+w$ and one of $-w$ have zero mixed Krein form. In the same way $P_+^\dagger BP_+ = BP_+$. Because $B$ is invertible and the two eigenspaces together span all 16 directions, $B$ cannot vanish on either eigenspace: if a column $u$ of the $+w$ eigenspace had $u^\dagger Bv = 0$ for all $v$ in that eigenspace, it would also have it for all $v$ in the other (step (i)), hence for all columns, so $Bu = 0$ and $u = BBu = 0$. Such a form is called **nondegenerate** on the eigenspace: its Gram matrix has no zero eigenvalue.

*Step (ii): in the good sector the inertia is (4,4).* There $Bh = hB$, so $B$ commutes with $P_\pm$ and maps each eigenspace into itself. In the good sector $h$ is also Hermitian (Section 10.4), so $P_+$ is Hermitian, and its range, the $+w$ eigenspace, has dimension $\mathrm{tr}\,P_+ = \frac12(16 + \mathrm{tr}\,h/w) = 8$ (the trace of a projector is the dimension of its range; $\mathrm{tr}\,h = 0$ because $h$ is a combination of $\gamma^{(x_4)}$ and of products of two different gammas, which have trace 0 by the argument given below for $Bh$). Choose an orthonormal basis $v_1, \dots, v_8$ of this eigenspace ($v_i^\dagger v_j$ is 1 for $i = j$ and 0 otherwise); then $P_+ = \sum_iv_iv_i^\dagger$. Because $Bv_j$ lies in the same eigenspace, $Bv_j = \sum_iv_i\,(v_i^\dagger Bv_j) = \sum_iv_iG_{ij}$: the Gram matrix $G_{ij} = v_i^\dagger Bv_j$ of the Krein form in this basis is exactly the matrix of $B$ restricted to the eigenspace. So its eight eigenvalues are eigenvalues of $B$, each $+1$ or $-1$ (because $BB = I_{16}$), and the Krein inertia counts how many are $+1$ and how many $-1$. Their sum is the trace of the Gram matrix, $\sum_iv_i^\dagger Bv_i = \mathrm{tr}(B\sum_iv_iv_i^\dagger) = \mathrm{tr}(BP_+)$, by $\mathrm{tr}(XY) = \mathrm{tr}(YX)$ for the column $v_i$ and the row $v_i^\dagger B$. Now

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
\Gamma\gamma^{(x_4)}\Gamma = -\gamma^{(x_4)}\Gamma\Gamma = -\gamma^{(x_4)},
$$

$$
\Gamma\gamma^{(x_4)}\gamma^{(x_a)}\Gamma = (\Gamma\gamma^{(x_4)}\Gamma)(\Gamma\gamma^{(x_a)}\Gamma) = (-\gamma^{(x_4)})(-\gamma^{(x_a)}) = \gamma^{(x_4)}\gamma^{(x_a)} ,
$$

where the second identity inserts $\Gamma\Gamma = I_{16}$ between the two gammas. Insert into $h_m(k)$:

$$
\Gamma h_m(k)\Gamma = +im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_{a \neq 4}k_a\gamma^{(x_a)} = h_{-m}(k) .
$$

**The mirror map.** In the same way, with $\gamma^{(x_8)}\gamma^{(x_8)} = I_{16}$: $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_8)} = -\gamma^{(x_4)}$; $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_a)}\gamma^{(x_8)} = \gamma^{(x_4)}\gamma^{(x_a)}$ for $a \neq 4, 8$ (two sign changes); and $\gamma^{(x_8)}\gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_8)} = -\gamma^{(x_4)}\gamma^{(x_8)}$ (one sign change). So $\gamma^{(x_8)}h_m(k)\gamma^{(x_8)} = h_{-m}(R_8k)$, where $R_8k$ is $k$ with $k_8$ replaced by $-k_8$.

**Equal spectra.** If $h_mu = w'u$, then $h_{-m}(\Gamma u) = \Gamma h_m\Gamma\Gamma u = \Gamma h_mu = w'\,\Gamma u$: the matrix $\Gamma$ carries every eigenvector of $h_m$ to an eigenvector of $h_{-m}$ with the same eigenvalue. Matrices related in this way ($N = SMS^{-1}$) are called **similar**, and similar matrices have the same eigenvalues. So the one-particle spectra of the universes of masses $+m$ and $-m$ are IDENTICAL, not opposite; the same follows from $w^2$, which contains the mass only as $m^2$. (PROVED: `wolfram-pairing.json`, checks `Q_one_particle_maps` and `Q_one_particle_Krein_signatures`; `python-pairing.json`, check `Q.one_particle_maps`.) This is statement Q4 of the quantum reading of the Revision record; Sections 10.44 and 10.45 discuss the whole quantum reading and what it does not establish.

### 10.7 Example: Notebook 10a computes the one-particle spectra and their Krein inertia

Notebook 10a reads the author's gammas from the record `Revision/algebra/gammas.json`, builds $C$ and $B$, checks the properties of Section 10.2, builds the mode Hamiltonian of Section 10.3, proves exactly with sympy that $h^2 = w^2I_{16}$ and $Bh = h^\dagger B$ (Section 10.4), follows the eigenvalues as the extra-time momentum grows, computes the Krein inertia of the eigenspaces for the eight samples stored in the pairing record and for a scan across the threshold of growth, repeats steps (i) and (ii) of the proof of Theorem 10.1 exactly, and checks the identities of Section 10.6. It draws six figures and ends with the line ALL 28 CHECKS PASSED (notebook 10a).

<!-- NOTEBOOK 10a -->

### 10.10 Line-by-line walk-through of Notebook 10a

The notebook has 18 code cells, In [1] to In [18]. This section explains every line of each of them. Python, the language of the notebooks, is read from top to bottom; a line that starts with `#` is a **comment** for the reader, which Python skips, and the text after `#` on a line of code is a comment too. Where a cell defines a function, the **docstring** (the text in triple quotes below the `def` line, which only describes the function) is left out of the quotations; it is printed in Section 10.9.

**In [1], the set-up cell.** Its first 247 lines are comments: they repeat, word for word, the run instructions of Section 10.8 (Python skips them; they are there so that the notebook carries its own instructions, so this comment block is different in every notebook), and end with the heading THE SET-UP between two lines of `=` signs. The code starts below that heading. The code is the same in all seven notebooks of this chapter, except for the line that sets `NOTEBOOK_ID` (the notebooks of the book that run a Rust program define one more helper, `rust_program`, which this chapter does not need).

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
REPORT_CHECKS = {}  # report file -> {check name: verdict}; each file is read once


def record_says_pass(record):
    path, separator, check_name = record.partition(", check ")
    if not separator:  # a data entry of a record file that the notebook reads itself
        return True
    if path not in REPORT_CHECKS:
        checks = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
        REPORT_CHECKS[path] = {c["name"]: c["verdict"].upper() for c in checks}
    return REPORT_CHECKS[path].get(check_name) == "PASS"
```

`REPORT_CHECKS` starts as an empty dictionary; it will hold, for every report file that the notebook cites, the verdicts of the report's checks, stored under the check names. `record_says_pass(record)` answers one question: does the cited record still say what the notebook claims? A record name such as `"Revision/theory/reports/python-field-theory.json, check B_properties"` is a file name and a check name joined by the text `, check `. `record.partition(", check ")` cuts the record name at the first occurrence of that text into three pieces: the part before it (`path`), the text itself (`separator`) and the part after it (`check_name`). If the text does not occur, `separator` is empty and the record names a data entry of a file, such as `"Revision/algebra/gammas.json, entry B"`, which the notebook reads and compares itself; the answer is then True. Otherwise the report file is read, once: `json.loads(...)["checks"]` is the list of its checks, each a dictionary with the keys `name`, `verdict` and `detail`, and the dictionary comprehension stores every verdict under its check name in capital letters (`.upper()`; some reports write `pass` in small letters). The answer is True only if a check of that name exists and its verdict is `PASS`; `.get` gives `None` for a missing name, and `None == "PASS"` is False.

```python
def check_record(condition, name, record):
    if not record_says_pass(record):  # the cited check must exist and say PASS
        raise AssertionError("the cited record check is missing or not PASS: " + record)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
        check(condition, name, record=record)
    sys.stdout.write(buffer.getvalue())  # one single piece of output
```

`check_record` first asks `record_says_pass`. If the answer is False, `raise AssertionError(...)` stops the notebook with an error message that names the record, in the same way as a failed check: the notebook never prints that it reproduces a record check that has been renamed, removed or turned to FAIL. Otherwise `check_record` does what `check(condition, name, record=record)` does, but prints the PASS line and the reproduces line in one piece. `io.StringIO()` is a **text buffer**, a piece of memory that collects printed text. Inside the `with` block everything that is printed goes into the buffer instead of the screen; `check` prints its two lines there (or stops the notebook if the condition is false). Then `sys.stdout.write` sends the collected text to the screen at once. Jupyter delivers printed text in pieces whose boundaries depend on timing; printing the two lines as one piece keeps the stored output of the notebook the same in every run.

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
save_figure(fig, "gamma4_c_and_b",
...)
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
save_figure(fig, "frequency_squared",
...)
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
save_figure(fig, "eigenvalue_flow",
...)
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
save_figure(fig, "krein_inertia_scan",
...)
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
save_figure(fig, "krein_gram_matrices",
...)
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
save_figure(fig, "plus_minus_mass_spectra",
...)
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

### 10.11 Quantum states, operators and fermion modes from zero

Sections 10.2 to 10.6 treated one wave as a column $u$ of 16 complex numbers. A quantum field is something else: its components become *operators* that act on *quantum states*. This section introduces the few notions that are needed, from zero, with small worked examples; Notebook 10b then builds all of them in Python.

**States and the inner product.** In the examples of this chapter a **quantum state** is a column $\psi = (\psi_1, \dots, \psi_n)$ of $n$ complex numbers. The **inner product** of two states $\phi$ and $\psi$ is the complex number

$$
\langle\phi|\psi\rangle = \sum_{j=1}^{n}\phi_j^*\psi_j .
$$

For $\phi = \psi$ every term is $\psi_j^*\psi_j = |\psi_j|^2 \geq 0$, so $\langle\psi|\psi\rangle > 0$ for every state $\psi$ that is not the zero column: the inner product is **positive**. The number $\lVert\psi\rVert = \sqrt{\langle\psi|\psi\rangle}$ is the **length** of $\psi$, and a state of length 1 is **normalised**. A space of states with a positive inner product is a **Hilbert space**. Positivity is what quantum mechanics needs for probabilities: for normalised $\phi$ and $\psi$ the number $|\langle\phi|\psi\rangle|^2$ is the probability of finding $\phi$ in the state $\psi$, and a probability cannot be negative.

**Operators and the Hilbert adjoint.** An **operator** $X$ maps every state to a state and respects sums and multiples, $X(a\phi + b\psi) = aX\phi + bX\psi$; here it is a matrix. The **Hilbert adjoint** of $X$ is the operator $X^*$ with

$$
\langle\phi|X\psi\rangle = \langle X^*\phi|\psi\rangle\quad\text{for all states }\phi, \psi .
$$

For the inner product above $X^*$ is the conjugate transpose of the matrix $X$: $\langle\phi|X\psi\rangle = \phi^\dagger X\psi = (X^\dagger\phi)^\dagger\psi$. In this chapter the star on an operator always means the Hilbert adjoint, and the dagger on a field operator is kept for the *canonical conjugate* of Section 10.12; for numbers, matrices and columns the star and the dagger keep their meaning of Section 10.1 (complex conjugate, conjugate transpose). One consequence of the definition is used again and again. Put $\psi = X^*\phi$:

$$
\langle\phi|XX^*\phi\rangle = \langle X^*\phi|X^*\phi\rangle = \lVert X^*\phi\rVert^2 \geq 0 .
$$

The first step is the definition of $X^*$ with $\psi = X^*\phi$; the second is the definition of the length. An operator with $X^* = X$ is **Hermitian**; its expectation values $\langle\phi|X\phi\rangle$ are real.

**Commutator, anticommutator and the Heisenberg equation.** For two operators, $[X, Y] = XY - YX$ is the **commutator** and $\{X, Y\} = XY + YX$ the **anticommutator**. We shall need the identity

$$
[XY, Z] = X\{Y, Z\} - \{X, Z\}Y .
$$

Proof: the right side is $X(YZ + ZY) - (XZ + ZX)Y = XYZ + XZY - XZY - ZXY = XYZ - ZXY$, by multiplying out and cancelling $XZY$, and $XYZ - ZXY$ is $[XY, Z]$ by the definition of the commutator. The energy operator $H$ (the **Hamiltonian**) moves the system in time. In the Heisenberg picture the states stay fixed and an operator $O$ changes with the time $x_4$ as $O(x_4) = e^{iHx_4}Oe^{-iHx_4}$. Differentiating with the product rule, and using that $H$ commutes with $e^{\pm iHx_4}$ (both are power series in $H$), gives the **Heisenberg equation**

$$
\frac{dO}{dx_4} = iH\,O(x_4) - i\,O(x_4)H = i\,[H, O(x_4)] .
$$

**One fermion mode and the Pauli principle.** Let $b$ be an operator with

$$
\{b, b^*\} = 1,\qquad b\,b = 0 .
$$

Then also $b^*b^* = (bb)^* = 0$. The **number operator** $N = b^*b$ obeys

$$
NN = b^*bb^*b = b^*(1 - b^*b)b = b^*b - b^*b^*bb = N .
$$

The second step replaces $bb^*$ by $1 - b^*b$ (the anticommutator); the third multiplies out; the fourth uses $b^*b^* = 0$. If $Nv = nv$ for a state $v \neq 0$, then $nv = Nv = NNv = n^2v$, so $n^2 = n$: $n = 0$ or $n = 1$. A fermion mode is either empty or occupied once. This is the **Pauli principle**, and it follows from the anticommutator alone. Example: on the two states $|0\rangle = (1, 0)$ (empty) and $|1\rangle = (0, 1)$ (occupied) the matrices

$$
b = \begin{pmatrix}0 & 1\\ 0 & 0\end{pmatrix},\qquad b^* = \begin{pmatrix}0 & 0\\ 1 & 0\end{pmatrix}
$$

give $bb^* = \mathrm{diag}(1, 0)$ and $b^*b = \mathrm{diag}(0, 1)$, whose sum is the identity; $b|1\rangle = |0\rangle$ (it **annihilates** the fermion), $b^*|0\rangle = |1\rangle$ (it **creates** one), and $b^*|1\rangle = 0$: a second fermion cannot be created.

**Many modes, patterns and the sign.** With $n$ modes $f_0, \dots, f_{n-1}$ the rules are

$$
\{f_p, f_q^*\} = \delta_{pq},\qquad \{f_p, f_q\} = 0,
$$

where $\delta_{pq}$ is 1 for $p = q$ and 0 otherwise. A basis state is a **pattern** of occupations $(o_0, o_1, \dots, o_{n-1})$, each $o_p$ being 0 (empty) or 1 (occupied); there are $2^n$ patterns. The pattern with every mode empty is the **vacuum** $|0\rangle$. The **Fock space** is the set of all superpositions of patterns, with the positive inner product in which the patterns are orthonormal. The operators act on a pattern as follows:

- $f_p$: if mode $p$ is occupied it empties it and multiplies by $(-1)^{s}$, where $s$ is the number of occupied modes below $p$ (the modes $0, \dots, p - 1$); if mode $p$ is empty the result is 0;
- $f_p^*$: if mode $p$ is empty it fills it and multiplies by the same $(-1)^{s}$; if it is occupied the result is 0.

Why the sign: take two modes and write a pattern as $|o_0o_1\rangle$. Then $f_0|11\rangle = |01\rangle$ (no occupied mode below 0), and $f_1|01\rangle = |00\rangle$ (mode 0 is empty), so $f_1f_0|11\rangle = |00\rangle$. In the other order $f_1|11\rangle = -|10\rangle$ (one occupied mode, mode 0, lies below mode 1), and $f_0|10\rangle = |00\rangle$, so $f_0f_1|11\rangle = -|00\rangle$. The sum is $\{f_0, f_1\}|11\rangle = 0$, as the rules require; without the sign it would be $2|00\rangle$. The rule $\{f_p, f_p^*\} = 1$ holds on every pattern: if mode $p$ is empty, $f_p^*$ fills it with a sign $(-1)^s$, $f_p$ empties it again with the same sign (the modes below $p$ have not changed), and $f_p^*f_p$ gives 0; the sum is $(-1)^{2s} = 1$ times the pattern. If mode $p$ is occupied, the roles of the two products are exchanged.

**A pattern as one whole number.** The notebooks store the pattern $(o_0, \dots, o_{n-1})$ as the whole number $n_{\mathrm{pattern}} = \sum_p o_p2^p$, whose binary digit number $p$ (counted from 0, the last digit first) is $o_p$. For example, with modes 0 and 3 occupied the number is $1 + 8 = 9$, binary 1001. The number of occupied modes below $p$ is the number of digits 1 among the binary digits $0, \dots, p - 1$. A state is stored as a Python dictionary that pairs every pattern of nonzero amplitude with its amplitude; the vacuum is the dictionary with the pattern 0 and the amplitude 1. With 16 modes there are $2^{16} = 65536$ patterns, but a state is stored by the few patterns it contains.

### 10.12 The canonical rule from the Lagrangian

To **quantise** dirac16complex means to replace its 16 components $\Psi_A$ by operators and to fix their anticommutators. *Canonical quantisation* reads the rule off the Lagrangian, with the time $x_4$ as the evolution time. The slices $x_4 = $ const are seven-dimensional, with the coordinates $x_1, x_2, x_3, x_5, x_6, x_7, x_8$.

**The time-derivative term, line by line.** In the author's metric the Lagrangian density of dirac16complex is (Chapter 7, record `Revision/theory/field-theory.json`)

$$
\mathcal{L} = \cos z\,\Big[\tfrac12\sum_{a}f_a^{-1}\big(\bar\Psi\gamma^{(x_a)}\partial_a\Psi - \partial_a\bar\Psi\gamma^{(x_a)}\Psi\big) - mS - U(S)\Big],
$$

with $\sqrt{|g|} = \cos z$, the scale factors $f_a$ of Section 10.3 ($f_4 = 1$), $\bar\Psi = \Psi^\dagger C$ and $S = \bar\Psi\Psi$; in this metric the spin connection drops out of the Lagrangian (`wolfram-field-theory.json`, check `L_spin_connection_drops_out_G`). The only terms with a derivative in $x_4$ are those with $a = 4$:

$$
\tfrac12\cos z\,\big(\Psi^\dagger C\gamma^{(x_4)}\partial_4\Psi - \partial_4\Psi^\dagger C\gamma^{(x_4)}\Psi\big).
$$

This line writes out $\bar\Psi = \Psi^\dagger C$. Now $C\gamma^{(x_4)} = iB$, because the definition $B = -iC\gamma^{(x_4)}$ multiplied by $i$ gives $iB = C\gamma^{(x_4)}$. Insert it:

$$
\tfrac{i}{2}\cos z\,\big(\Psi^\dagger B\,\partial_4\Psi - \partial_4\Psi^\dagger B\,\Psi\big).
$$

Add the total derivative $\frac{i}{2}\partial_4(\cos z\,\Psi^\dagger B\Psi)$. A total derivative does not change the field equations (its integral over the time depends only on the end values, which the variation keeps fixed; Chapter 7). Since $\cos z$ does not depend on $x_4$, the product rule gives $\frac{i}{2}\partial_4(\cos z\,\Psi^\dagger B\Psi) = \frac{i}{2}\cos z\,(\partial_4\Psi^\dagger B\Psi + \Psi^\dagger B\partial_4\Psi)$. Added to the line above, the two terms with $\partial_4\Psi^\dagger$ cancel and the two with $\partial_4\Psi$ add:

$$
i\cos z\,\Psi^\dagger B\,\partial_4\Psi = \Psi^\dagger K\,\partial_4\Psi,\qquad K = i\cos z\,B .
$$

The rest of the Lagrangian has no $x_4$-derivative; the Revision record writes it as $-\mathcal{H}$ with the **Hamiltonian density** $\mathcal{H} = \cos z\,[\Psi^\dagger(mC - \sum_{\mu \neq x_4}C\gamma^\mu D_\mu)\Psi + U(S)]$, so that $\mathcal{L} = \Psi^\dagger K\partial_4\Psi - \mathcal{H}$ exactly, up to the total derivative (`python-field-theory.json`, check `hamiltonian_form_and_heisenberg_equation`). In words: the time-derivative term contains the matrix $B$, and the momentum conjugate to $\Psi_A$ is $\pi_A = i\cos z\,(\Psi^\dagger B)_A$, which depends on $\Psi^\dagger$ only, as for Dirac's electron (`python-field-theory.json`, check `canonical_momentum`).

**The rule, line by line.** Take a Lagrangian of the form $\Psi^\dagger K\partial_4\Psi - \Psi^\dagger h'\Psi$ with constant matrices $K$ and $h'$ (one point of the slice; the derivatives along the slice are inside $h'$). Varying $\Psi^\dagger$ gives the classical equation

$$
K\,\partial_4\Psi = h'\Psi,\qquad\text{that is}\qquad \partial_4\Psi = K^{-1}h'\Psi .
$$

In the quantum theory suppose that the operators obey $\{\Psi_A, \Psi^\dagger_C\} = A_{AC}$ with an unknown matrix $A$, and $\{\Psi_A, \Psi_C\} = 0$. The energy operator is $H = \Psi^\dagger h'\Psi = \sum_{A,C}\Psi^\dagger_Ah'_{AC}\Psi_C$. For one component $\Psi_c$:

$$
[H, \Psi_c] = \sum_{A,C}h'_{AC}\,[\Psi^\dagger_A\Psi_C, \Psi_c] = \sum_{A,C}h'_{AC}\big(\Psi^\dagger_A\{\Psi_C, \Psi_c\} - \{\Psi^\dagger_A, \Psi_c\}\Psi_C\big) .
$$

The first step takes the numbers $h'_{AC}$ out of the commutator; the second is the identity $[XY, Z] = X\{Y, Z\} - \{X, Z\}Y$ of Section 10.11 with $X = \Psi^\dagger_A$, $Y = \Psi_C$, $Z = \Psi_c$. Now $\{\Psi_C, \Psi_c\} = 0$ and $\{\Psi^\dagger_A, \Psi_c\} = \{\Psi_c, \Psi^\dagger_A\} = A_{cA}$, so

$$
[H, \Psi_c] = -\sum_{A,C}A_{cA}h'_{AC}\Psi_C = -(Ah'\Psi)_c ,
$$

by the definition of a matrix product. The Heisenberg equation then reads

$$
\partial_4\Psi = i[H, \Psi] = -iAh'\Psi .
$$

It agrees with the classical equation $\partial_4\Psi = K^{-1}h'\Psi$ for every $h'$ exactly when $-iA = K^{-1}$, that is $A = iK^{-1}$. With $K = i\cos z\,B$, $B^{-1} = B$ (Section 10.2) and $1/i = -i$:

$$
iK^{-1} = i\cdot\frac{1}{i\cos z}\,B^{-1} = \frac{B}{\cos z} .
$$

**From one point to the whole slice.** So far the slice was a single point. To pass to the whole slice, divide it into many small cells, each with the coordinate volume $\Delta V$ (the product of its seven coordinate widths), and keep one value $\Psi(x)$ of the field per cell $x$. The Lagrangian of the slice is then the sum over the cells of $\Delta V$ times the density, so the time-derivative term of the cell $x$ is $\Psi(x)^\dagger(K\Delta V)\,\partial_4\Psi(x)$, with $K = i\cos z\,B$ at the position of that cell; this term couples no two different cells (the derivatives along the slice, which do couple neighbouring cells, sit in $h'$). The rule just derived holds for any number of components: take as the components all 16 components of all cells. Their time-derivative kernel is block diagonal, with one block $K\Delta V$ per cell, so its inverse is block diagonal with the blocks $(K\Delta V)^{-1}$, and the rule $A = iK^{-1}$ gives

$$
\{\Psi_A(x), \Psi^\dagger_C(y)\} = i\,(K\Delta V)^{-1}_{AC}\,\delta_{xy} = B_{AC}\,\frac{\delta_{xy}}{\cos z\,\Delta V} ,
$$

where $\delta_{xy}$ is 1 for the same cell and 0 for two different cells: components of different cells anticommute. The second step is $iK^{-1} = B/\cos z$ from above, divided by $\Delta V$. As the cells shrink, $\delta_{xy}/\Delta V$ becomes the seven-dimensional **delta function** $\delta^7(x - y)$. It is defined by what it does in an integral: it is zero for $x \neq y$, and for every smooth function $f$ on the slice

$$
\int f(y)\,\delta^7(x - y)\,d^7y = f(x) ,
$$

just as the sum over the cells $\sum_y\Delta V\,f(y)\,\delta_{xy}/\Delta V = f(x)$ picks out the cell $x$. It is not an ordinary function (no ordinary function is zero everywhere but at one point and still has the integral 1) but a rule for integrals, and in the theory it only appears inside such integrals. So the **canonical anticommutator** of dirac16complex on a slice $x_4 = $ const is

$$
\{\Psi_A(x), \Psi^\dagger_C(y)\} = B_{AC}\,\frac{\delta^7(x - y)}{\cos z} .
$$

At one point the factor $1/\cos z$ is a positive number, which changes no sign; the notebooks therefore work with $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$.

**The Heisenberg equation is the wave equation.** For a plane wave with frame momenta $k_a$ along the slice, at one point with frozen coefficients, the derivatives $D_a$ in $\mathcal{H}$ become $ik_a$ and

$$
h' = mC - i\sum_{a \neq 4}k_a\,C\gamma^{(x_a)} .
$$

Multiply by $B = -iC\gamma^{(x_4)}$:

$$
Bh' = -im\,C\gamma^{(x_4)}C - \sum_{a \neq 4}k_a\,C\gamma^{(x_4)}C\gamma^{(x_a)} = -im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_{a \neq 4}k_a\gamma^{(x_a)} = h .
$$

The first step multiplies out ($(-i)(-i) = -1$); the second moves $C$ through $\gamma^{(x_4)}$ (they commute, (B1) of Section 10.2) and uses $CC = I_{16}$; the result is the mode Hamiltonian $h$ of Section 10.3. With $A = B$ the Heisenberg equation is $\partial_4\Psi = -iBh'\Psi = -ih\Psi$, that is $i\,\partial_4\Psi = h\Psi$: the quantum field obeys the classical wave equation of the field.

**Why anticommutators.** The rule uses anticommutators because dirac16complex is a fermion field by the author's definition: its components are anticommuting numbers. In ordinary 3+1 dimensional physics this choice is not free: the **spin-statistics theorem** of quantum field theory shows that, if the energy is to be bounded below and measurements at two points that no signal can connect are not to disturb each other, fields of half-integer spin (such as the electron's) must be quantised with anticommutators and fields of whole-number spin with commutators. No such theorem is proved for signature (4,4); here the anticommutator is an ASSUMPTION, part of the definition of the field.

| statement | status | where it is verified |
| --- | --- | --- |
| the time-derivative term is $\Psi^\dagger K\partial_4\Psi$ with $K = i\cos z\,B$; $\pi_A = i\cos z\,(\Psi^\dagger B)_A$ | PROVED | `wolfram-field-theory.json`, checks `canonical_momentum` and `first_order_form_and_anticommutator`; `python-field-theory.json`, check `canonical_momentum` |
| $\{\Psi_A(x), \Psi^\dagger_C(y)\} = B_{AC}\,\delta^7(x - y)/\cos z$ | PROVED | `python-field-theory.json`, check `canonical_anticommutator_B`; `python-pairing.json`, check `Q.canonical_anticommutator` |
| the Heisenberg equation reproduces the field equation (general $U$) | PROVED | `wolfram-field-theory.json`, check `Heisenberg_equation_reproduces_field_equation`; `python-field-theory.json`, check `hamiltonian_form_and_heisenberg_equation` |
| anticommutators (not commutators) for dirac16complex | ASSUMED | part of the definition of the field as a fermion field; no spin-statistics theorem for signature (4,4) is proved |

### 10.13 The canonical conjugate is not the Hilbert adjoint: the Krein space

In ordinary quantum theory the canonical conjugate $\Psi^\dagger$ is the Hilbert adjoint of $\Psi$. In signature (4,4) this is impossible.

**Theorem 10.2 (the canonical rule forces a Krein space).** There is no space of states with a positive inner product on which operators $\Psi_A$ obey $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$ with $\Psi^\dagger_A$ the Hilbert adjoint of $\Psi_A$. (PROVED: `python-field-theory.json` and `wolfram-field-theory.json`, check `no_positive_inner_product`.)

*Proof.* Take the column $u$ with $u_7 = -i/\sqrt2$, $u_{16} = 1/\sqrt2$ and all other entries 0 (the column named by the record). By the table of $B$ in Section 10.2, $(Bu)_7 = B_{7,16}u_{16} = i/\sqrt2 = -u_7$ and $(Bu)_{16} = B_{16,7}u_7 = (-i)(-i/\sqrt2) = -1/\sqrt2 = -u_{16}$, so $Bu = -u$; and $u^\dagger u = \frac12 + \frac12 = 1$, so $u^\dagger Bu = -u^\dagger u = -1$. Define the operator $X = \sum_Au_A^*\Psi_A$ and its canonical conjugate $X^\dagger = \sum_Au_A\Psi^\dagger_A$. Then

$$
\{X, X^\dagger\} = \sum_{A,C}u_A^*u_C\{\Psi_A, \Psi^\dagger_C\} = \sum_{A,C}u_A^*B_{AC}u_C = u^\dagger Bu = -1 .
$$

The first step takes the numbers out of the anticommutator; the second is the canonical rule; the third is the definition of $u^\dagger Bu$. Suppose now that $X^\dagger$ were the Hilbert adjoint $X^*$. Then for every normalised state $\phi$, by the consequence of the definition of the adjoint in Section 10.11,

$$
\langle\phi|\{X, X^*\}\phi\rangle = \langle\phi|XX^*\phi\rangle + \langle\phi|X^*X\phi\rangle = \lVert X^*\phi\rVert^2 + \lVert X\phi\rVert^2 \geq 0,
$$

while $\{X, X^*\} = -1$ gives $\langle\phi|(-1)\phi\rangle = -1$. A number cannot be both $\geq 0$ and $-1$. QED.

**What remains: a Krein space.** The canonical rule itself is consistent; what fails is only its reading with a positive inner product. A **Krein space** is a space with a Hermitian form $[u, v]$ that is *nondegenerate* (no nonzero $u$ has $[u, v] = 0$ for all $v$) but *indefinite* (it takes both signs), together with a matrix $J$, the **fundamental symmetry**, with $J^\dagger = J = J^{-1}$, such that $[u, Jv]$ is a positive inner product. For the one-particle columns of dirac16complex, $[u, v] = u^\dagger Bv$ and $J = B$: indeed $[u, Bv] = u^\dagger BBv = u^\dagger v$, the ordinary positive inner product. The theorem says that the canonical rule turns the state space of the field into a Krein space with fundamental symmetry $B$, whenever $\Psi^\dagger$ is read as the adjoint.

### 10.14 Two realisations and the expectation-value rule

The Revision record describes two honest ways to realise the canonical rule on a concrete space of states.

**(a) The positive realisation.** Keep a POSITIVE Fock space, with 16 modes $f_0, \dots, f_{15}$, and let $\Psi_A = f_{A-1}$ and $\chi_A = f_{A-1}^*$, the Hilbert adjoint. Then *define* the canonical conjugate as

$$
\Psi^\dagger_A = \sum_C\chi_CB_{CA},\qquad\text{briefly}\qquad \Psi^\dagger = \chi B .
$$

Line by line,

$$
\{\Psi_A, \Psi^\dagger_C\} = \sum_D\{\Psi_A, \chi_D\}B_{DC} = \sum_D\delta_{AD}B_{DC} = B_{AC} .
$$

The first step takes the numbers $B_{DC}$ out of the anticommutator; the second is the Fock rule $\{f_{A-1}, f^*_{D-1}\} = \delta_{AD}$; the third keeps the one term $D = A$. So the canonical rule holds on a positive space, but $\Psi^\dagger$ is not the Hilbert adjoint: for the column $u$ of Theorem 10.2,

$$
X^\dagger = \sum_Au_A\Psi^\dagger_A = \sum_{A,C}u_A\chi_CB_{CA} = \sum_C(Bu)_C\chi_C = -\sum_Cu_C\chi_C = -X^* ,
$$

where the third step collects $\sum_AB_{CA}u_A = (Bu)_C$, the fourth uses $Bu = -u$, and the last recognises $X^* = \sum_Cu_C\chi_C$, the Hilbert adjoint of $X = \sum_Cu_C^*\Psi_C$. So $\{X, X^*\} = +1$ (positive, as in every Hilbert space) while $\{X, X^\dagger\} = -1$ (the canonical value): the two differ by a sign. This is the form the Revision record uses for the good sector (Section 10.20).

**(b) The Krein-Fock realisation.** Keep $\Psi^\dagger$ as the conjugate and let the modes carry Krein norms $\pm1$. Choose 16 columns $u_1, \dots, u_{16}$ with $u_n^\dagger Bu_{n'} = \epsilon_n\delta_{nn'}$, $\epsilon_n = +1$ or $-1$ (*Krein-orthonormal* modes). Write $U$ for the matrix with these columns and $E = \mathrm{diag}(\epsilon_1, \dots, \epsilon_{16})$, so that $U^\dagger BU = E$. Then also $UEU^\dagger = B$: multiply $U^\dagger BU = E$ from the left by $UE$, which gives $UEU^\dagger BU = UEE = U$ (because $EE = I_{16}$); multiply from the right by $U^{-1}$: $UEU^\dagger B = I_{16}$; multiply from the right by $B$: $UEU^\dagger = B$ (because $BB = I_{16}$). Take operators $b_n$ with $\{b_n, b_{n'}^\dagger\} = \epsilon_n\delta_{nn'}$ and put $\Psi = \sum_nu_nb_n$, $\Psi^\dagger = \sum_nu_n^\dagger b_n^\dagger$. Then

$$
\{\Psi_A, \Psi^\dagger_C\} = \sum_{n,n'}(u_n)_A(u_{n'})_C^*\{b_n, b_{n'}^\dagger\} = \sum_n\epsilon_n(u_n)_A(u_n)_C^* = (UEU^\dagger)_{AC} = B_{AC} :
$$

the same canonical rule. The simplest choice takes 8 eigenvectors of $B$ with eigenvalue $+1$ ($\epsilon = +1$) and 8 with eigenvalue $-1$ ($\epsilon = -1$). A **Krein boost** of a pair, $u_1' = \cosh t\,u_1 + \sinh t\,u_9$ and $u_9' = \sinh t\,u_1 + \cosh t\,u_9$ (with $Bu_1 = u_1$, $Bu_9 = -u_9$, both of length 1 and orthogonal), keeps the Krein norms, because $\cosh^2t - \sinh^2t = 1$, and keeps the two modes Krein-orthogonal, because $\cosh t\,\sinh t - \sinh t\,\cosh t = 0$; but it changes the ordinary squared length to $\cosh^2t + \sinh^2t$. The record uses $\cosh t = \frac54$, $\sinh t = \frac34$ ($\frac{25}{16} - \frac{9}{16} = 1$), so the boosted mode has the ordinary squared length $\frac{25}{16} + \frac{9}{16} = \frac{34}{16} = 2.125$.

**The expectation-value rule, line by line.** In the one-mode state $b_n^\dagger|0\rangle$ (with $b_{n'}|0\rangle = 0$ for all $n'$) the observable $\Psi^\dagger M\Psi = \sum_{k,k'}(u_k^\dagger Mu_{k'})\,b_k^\dagger b_{k'}$ has the vacuum value

$$
\langle 0|b_n(\Psi^\dagger M\Psi)b_n^\dagger|0\rangle = \sum_{k,k'}(u_k^\dagger Mu_{k'})\langle 0|b_nb_k^\dagger b_{k'}b_n^\dagger|0\rangle = \sum_{k,k'}(u_k^\dagger Mu_{k'})\,\epsilon_n\delta_{k'n}\,\epsilon_n\delta_{kn} = u_n^\dagger Mu_n .
$$

The first step inserts the expansion; the second uses $b_{k'}b_n^\dagger|0\rangle = \{b_{k'}, b_n^\dagger\}|0\rangle = \epsilon_n\delta_{k'n}|0\rangle$ (the term $b_n^\dagger b_{k'}|0\rangle$ vanishes) and in the same way $\langle 0|b_nb_k^\dagger|0\rangle = \epsilon_n\delta_{kn}$; the third uses $\epsilon_n^2 = 1$. The Krein norm of the state is $\langle 0|b_nb_n^\dagger|0\rangle = \epsilon_n$, so the **normalised** expectation value is

$$
\frac{\langle 0|b_n(\Psi^\dagger M\Psi)b_n^\dagger|0\rangle}{\langle 0|b_nb_n^\dagger|0\rangle} = \epsilon_n\,u_n^\dagger Mu_n .
$$

For a mode that is an eigenvector of $B$, $Bu_n = \epsilon_nu_n$, the conjugate transpose gives $u_n^\dagger B = \epsilon_nu_n^\dagger$ ($B$ is Hermitian and $\epsilon_n$ real), so $\epsilon_nu_n^\dagger Mu_n = u_n^\dagger BMu_n$, the form in which the Revision specification states the rule. For a Krein-boosted mode $Bu_n \neq \epsilon_nu_n$, and the form $u_n^\dagger BMu_n$ is wrong; the general rule is $\epsilon_nu_n^\dagger Mu_n$ (`python-field-theory.json`, check `expectation_value_rule`).

### 10.15 Maps that keep the canonical rule, and the conjugation of the quantised field

**Linear maps.** If $\Psi' = M\Psi$ with a constant matrix $M$, the conjugate is $\Psi'^\dagger = \Psi^\dagger M^\dagger$, that is $\Psi'^\dagger_C = \sum_F\Psi^\dagger_FM^*_{CF}$, and

$$
\{\Psi'_A, \Psi'^\dagger_C\} = \sum_{D,F}M_{AD}M^*_{CF}\{\Psi_D, \Psi^\dagger_F\} = \sum_{D,F}M_{AD}B_{DF}M^*_{CF} = (MBM^\dagger)_{AC} .
$$

The map keeps the canonical rule exactly when $MBM^\dagger = B$. The Revision pairing record lists $MBM^\dagger = \sigma B$ with a sign $\sigma$ for 17 maps (`Revision/pairing/pairing-theory.json`, data `Krein_signs_M_B_Mdagger`; `wolfram-pairing.json`, check `Q_Krein_metric_of_images`). The signs follow from Section 10.2 in three lines. For a gamma, $(\gamma^{(x_a)})^\dagger = (\gamma^{(x_a)})^T = \eta_{aa}\gamma^{(x_a)}$ (the gammas are real; the space-like ones are symmetric, the time-like ones antisymmetric) and $\gamma^{(x_a)}B = s_aB\gamma^{(x_a)}$ with $s_a = +1$ for $a = 1, 2, 3, 4, 8$ and $s_a = -1$ for $a = 5, 6, 7$; so

$$
\gamma^{(x_a)}B(\gamma^{(x_a)})^\dagger = \eta_{aa}\,\gamma^{(x_a)}B\gamma^{(x_a)} = \eta_{aa}s_a\,B\gamma^{(x_a)}\gamma^{(x_a)} = \eta_{aa}s_a\eta_{aa}\,B = s_aB .
$$

For the chirality, $\Gamma$ is real and symmetric and $\Gamma B\Gamma = -B$ (Section 10.2), so $\Gamma B\Gamma^\dagger = -B$. For the reflection $P_a = \Gamma\gamma^{(x_a)}$ the two signs multiply: $\sigma = -s_a$. The table:

| map $M$ | sign $\sigma$ in $MBM^\dagger = \sigma B$ |
| --- | --- |
| $\Gamma$ | $-1$ |
| $\gamma^{(x_1)}, \gamma^{(x_2)}, \gamma^{(x_3)}, \gamma^{(x_4)}, \gamma^{(x_8)}$ | $+1$ |
| $\gamma^{(x_5)}, \gamma^{(x_6)}, \gamma^{(x_7)}$ | $-1$ |
| $P_1, P_2, P_3, P_4, P_8$ | $-1$ |
| $P_5, P_6, P_7$ | $+1$ |

The chirality image $\Gamma\Psi$ of the pairing theorem T1 therefore carries the Krein metric $-B$ (statement Q1 of the quantum reading of the pairing record, Section 10.44), while the mirror image $\gamma^{(x_8)}\Psi$ of theorem T2 keeps $+B$ (statement Q5).

**The conjugation of the quantised field.** Charge conjugation is a MATRIX map (Chapter 5): the two charge-conjugation matrices are $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$, and for a classical field they give $\Psi^c = \mathcal{C}_+\bar\Psi^T = CC\Psi^* = \Psi^*$ (same mass) and $\Psi^c = \mathcal{C}_-\bar\Psi^T = \Gamma\Psi^*$ (mass reversed), since $\bar\Psi^T = (\Psi^\dagger C)^T = C^T\Psi^* = C\Psi^*$. (For a REAL field $\Psi^* = \Psi$, so the first map is the identity: a real field is its own conjugate, and plain complex conjugation does nothing to it; the nontrivial real map is $\Gamma$, Chapter 5.) For the QUANTISED field the role of $\Psi^*$ is played by the column of conjugate operators $\Psi^{\dagger T}$, and the candidate conjugations are $\Psi^c = M\Psi^{\dagger T}$, that is $\Psi^c_A = \sum_DM_{AD}\Psi^\dagger_D$. Its conjugate is $\Psi^{c\dagger}_C = \sum_FM^*_{CF}\Psi_F$ (the conjugate of $\Psi^\dagger$ is $\Psi$). Line by line,

$$
\{\Psi^c_A, \Psi^{c\dagger}_C\} = \sum_{D,F}M_{AD}M^*_{CF}\{\Psi^\dagger_D, \Psi_F\} = \sum_{D,F}M_{AD}B_{FD}M^*_{CF} = (MB^TM^\dagger)_{AC} .
$$

The second step uses $\{\Psi^\dagger_D, \Psi_F\} = \{\Psi_F, \Psi^\dagger_D\} = B_{FD}$, and the third $B_{FD} = (B^T)_{DF}$. Because $B$ is Hermitian and purely imaginary, $B^T = (B^\dagger)^* = B^* = -B$. Hence:

- $M = I_{16}$ (the $\mathcal{C}_+$ type, $\Psi \to \Psi^{\dagger T}$): $MB^TM^\dagger = -B$, the sign of the canonical rule is REVERSED;
- $M = \Gamma$ (the $\mathcal{C}_-$ type, $\Psi \to \Gamma\Psi^{\dagger T}$): $\Gamma B^T\Gamma^\dagger = -\Gamma B\Gamma = +B$, the canonical rule is KEPT.

So the conjugation of the quantised field that preserves $\{\Psi, \Psi^\dagger\} = B\delta$ is $\Psi \to \Gamma\Psi^{\dagger T}$, and it reverses the mass: the gammas are real, so the conjugate of the field equation $\gamma^\mu\partial_\mu\Psi = m\Psi$ (flat space, $U = 0$) is $\gamma^\mu\partial_\mu\Psi^* = m\Psi^*$, and since $\Gamma$ anticommutes with every gamma, $\gamma^\mu\partial_\mu(\Gamma\Psi^*) = -\Gamma\gamma^\mu\partial_\mu\Psi^* = -m\,\Gamma\Psi^*$: the conjugated field obeys the equation of mass $-m$ (`charge-conjugation-and-u1.json`, check `quantum_charge_conjugation_unitary_type`). Chapter 21 uses this result for matter and antimatter.

| statement | status | where it is verified |
| --- | --- | --- |
| Theorem 10.2: no positive inner product with $\Psi^\dagger$ the adjoint | PROVED | `python-field-theory.json` and `wolfram-field-theory.json`, check `no_positive_inner_product` |
| positive realisation $\Psi^\dagger = \chi B$ gives $\{\Psi, \Psi^\dagger\} = B$ | PROVED | `python-field-theory.json`, check `good_sector_positive_fock_realisation`; Notebook 10b on a Fock space |
| expectation-value rule $\epsilon_nu_n^\dagger Mu_n$; $u_n^\dagger BMu_n$ only for eigenvectors of $B$ | PROVED | `python-field-theory.json`, check `expectation_value_rule` |
| the 17 signs $\sigma$ of $MBM^\dagger = \sigma B$ | PROVED | `pairing-theory.json`, data `Krein_signs_M_B_Mdagger`; `wolfram-pairing.json`, check `Q_Krein_metric_of_images`; `python-pairing.json`, check `compare.theory.krein_signs` |
| $\Psi \to \Gamma\Psi^{\dagger T}$ keeps $B$ and reverses the mass; $M = I_{16}$ gives $-B$ | PROVED | `charge-conjugation-and-u1.json`, check `quantum_charge_conjugation_unitary_type` |

### 10.16 Example: Notebook 10b builds the canonical rule on a Fock space

Notebook 10b repeats the derivation of $iK^{-1} = B/\cos z$ exactly with sympy, builds the fermionic Fock space of Section 10.11 in a few lines of Python, realises on it the canonical rule $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$ with $\Psi^\dagger = \chi B$ (Section 10.14), checks that the Heisenberg equation gives the classical wave equation (Section 10.12), checks Theorem 10.2 on the recorded column and makes the positivity visible for 300 random states, builds the Krein-Fock realisation with a Krein-boosted pair and checks the expectation-value rule for 60 random matrices, and reproduces the 17 signs of Section 10.15 and the conjugation $\Psi \to \Gamma\Psi^{\dagger T}$. It draws five figures and ends with the line ALL 25 CHECKS PASSED (notebook 10b).

<!-- NOTEBOOK 10b -->

### 10.19 Line-by-line walk-through of Notebook 10b

The notebook has 12 code cells, In [1] to In [12]. As in Section 10.10, the docstrings of the functions (the text in triple quotes under a `def` line) are left out of the quotations; they are printed in Section 10.18.

**In [1], the set-up cell.** Its first 248 lines are comments that repeat the run instructions of Section 10.17. The code below the heading THE SET-UP is word for word the code of In [1] of Notebook 10a, explained line by line in Section 10.10, except for one line, `NOTEBOOK_ID = "10b"  # this notebook: chapter 10, example b`. It defines `REPO`, `OUTPUT_ROOT`, `repository_file`, `output_file`, `say`, `save_figure`, `check`, `report` and `all_checks_passed`, and prints the single line `Set-up of notebook 10b complete: repository folder found, helpers defined.`

**In [2], the time-derivative kernel and the canonical rule.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer
import sys  # the screen output, sys.stdout

import numpy as np  # numbers, arrays and matrices
import sympy as sp  # exact algebra with symbols
```

The same imports as In [2] of Notebook 10a: three modules of Python for printing into a buffer, numpy for numbers and sympy for exact algebra.

```python
REPORT_CHECKS = {}  # report file -> {check name: verdict}; each file is read once


def record_says_pass(record):
    path, separator, check_name = record.partition(", check ")
    if not separator:  # a data entry of a record file that the notebook reads itself
        return True
    if path not in REPORT_CHECKS:
        checks = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
        REPORT_CHECKS[path] = {c["name"]: c["verdict"].upper() for c in checks}
    return REPORT_CHECKS[path].get(check_name) == "PASS"
```

`REPORT_CHECKS` and `record_says_pass` are those of In [2] of Notebook 10a (Section 10.10): for a record name `<report file>, check <check name>` the function reads the report once and answers True only if a check of that name exists there with the verdict PASS; for a data entry of a file that the notebook reads itself it answers True.

```python
def check_record(condition, name, record):
    if not record_says_pass(record):  # the cited check must exist and say PASS
        raise AssertionError("the cited record check is missing or not PASS: " + record)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
        check(condition, name, record=record)
    sys.stdout.write(buffer.getvalue())  # one single piece of output
```

`check_record` is the function of In [2] of Notebook 10a (Section 10.10): it stops the notebook with an error if the cited record check is missing or not PASS; otherwise it runs `check(condition, name, record=record)`, collects the PASS line and the line naming the reproduced Revision record in a text buffer, and prints both in one piece, so that the stored output is the same in every run.

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
    encoding="utf-8"))
gamma = {a: np.array(fixture["gamma"][a - 1], dtype=int) for a in range(1, 9)}
C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]  # the author's sigma16
Gamma = (gamma[8] @ gamma[1] @ gamma[2] @ gamma[3] @ gamma[4] @ gamma[5]
         @ gamma[6] @ gamma[7])  # the chirality matrix
B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4)
```

The record `Revision/algebra/gammas.json` is read and the eight gammas are stored as whole-number arrays, `gamma[a]` being $\gamma^{(x_a)}$. `C` is $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$, `Gamma` the chirality $\Gamma$, the product of all eight gammas in the author's order (the parentheses let the product run over two lines), and `B` is $B = -iC\gamma^{(x_4)}$.

```python
check(np.array_equal(C @ gamma[4], 1j * B), "C gamma^(x4) = i B")
check(np.array_equal(B @ B, np.eye(16)), "B B = I, so the inverse of B is B")
```

The two facts used in Section 10.12: $C\gamma^{(x_4)} = iB$ and $BB = I_{16}$. Both comparisons are exact (whole numbers times $\pm i$), and two PASS lines are printed.

```python
c = sp.Symbol("c", positive=True)  # c stands for cos z, positive on the patch
B_exact = sp.Matrix(16, 16, lambda i, j: sp.I * int(round(B[i, j].imag)))
K = sp.I * c * B_exact  # the kernel of the time-derivative term
rule = (sp.I * K.inv()).applyfunc(sp.simplify)  # the anticommutator matrix i K^-1
```

`c` is a sympy letter for $\cos z$, declared positive (on the patch $0 < z < \pi/2$, $\cos z > 0$). `sp.Matrix(16, 16, lambda i, j: ...)` builds a $16 \times 16$ exact matrix entry by entry: entry $(i, j)$ is $i$ times the whole number nearest to the imaginary part of the numpy entry $B_{ij}$ (`round` and `int` turn $\pm1.0$ into $\pm1$), so `B_exact` is $B$ with exact entries. `K` is the kernel $K = i\cos z\,B$ of Section 10.12, `K.inv()` its exact inverse, and `rule` is $iK^{-1}$, every entry simplified.

```python
check_record(rule == B_exact / c,
             "exact: i K^(-1) = B / cos z with K = i cos z B",
             record="Revision/theory/reports/wolfram-field-theory.json, check "
                    "first_order_form_and_anticommutator")
```

The check confirms $iK^{-1} = B/\cos z$ exactly, the canonical rule of Section 10.12, and reproduces the Wolfram record check `first_order_form_and_anticommutator`. The cell prints three PASS lines.

**In [3], a fermionic Fock space.**

```python
def sign_below(n, p):
    occupied_below = bin(n & ((1 << p) - 1)).count("1")  # count the 1-digits below p
    return -1 if occupied_below % 2 else 1
```

`sign_below(n, p)` is the sign $(-1)^s$ of Section 10.11, where $s$ is the number of occupied modes below $p$ in the pattern $n$. The operator written with two less-than signs shifts the binary digits of 1 to the left by $p$ places, which gives $2^p$; minus 1 gives the number whose $p$ lowest binary digits are all 1. The operator `&` (binary *and*) keeps a binary digit only where both numbers have a 1, so `n & ...` keeps the digits of $n$ below $p$. `bin` writes a whole number in binary as a text (for example `bin(9)` is the text `0b1001`), and `.count("1")` counts the digits 1 in it. `occupied_below % 2` is the remainder after division by 2: 1 for an odd count (sign $-1$), 0 for an even one (sign $+1$; a remainder 0 counts as false in the `if`).

```python
def annihilate(p, state):
    result = {}
    for n, amplitude in state.items():
        if n >> p & 1:  # mode p is occupied in the pattern n
            new = n ^ (1 << p)  # the same pattern with mode p emptied
            result[new] = result.get(new, 0) + sign_below(n, p) * amplitude
    return result
```

`annihilate(p, state)` is $f_p$. A state is a dictionary `{pattern: amplitude}`, and the loop takes its pairs one by one. The test in the `if` line shifts $n$ to the right by $p$ binary places (the operator of two greater-than signs) and keeps the last digit (`& 1`): it is 1 exactly when mode $p$ is occupied. Then `^` (binary *exclusive or*) with $2^p$ flips digit $p$ from 1 to 0: `new` is the pattern with mode $p$ emptied. The amplitude times the sign is added to whatever `result` already holds for `new` (`result.get(new, 0)` is 0 when `new` is not yet there). Patterns in which mode $p$ is empty contribute nothing.

```python
def create(p, state):
    result = {}
    for n, amplitude in state.items():
        if not n >> p & 1:  # mode p is empty in the pattern n
            new = n | (1 << p)  # the same pattern with mode p filled
            result[new] = result.get(new, 0) + sign_below(n, p) * amplitude
    return result
```

`create(p, state)` is $f_p^*$, the Hilbert adjoint of $f_p$: it acts only where mode $p$ is empty, and `|` (binary *or*) with $2^p$ sets digit $p$ to 1. The sign is the same $(-1)^s$.

```python
def add(*terms):
    result = {}
    for coefficient, state in terms:
        for n, amplitude in state.items():
            result[n] = result.get(n, 0) + coefficient * amplitude
    return result
```

`add` forms a combination of states. The star in `*terms` lets the function take any number of arguments, each a pair `(coefficient, state)`; the result is the sum of the coefficients times the states, pattern by pattern. For example `add((1, a), (-1, b))` is the state $a - b$.

```python
def inner(left, right):
    return sum(np.conj(a) * right.get(n, 0) for n, a in left.items())


def largest(state):
    return max((abs(a) for a in state.values()), default=0.0)
```

`inner(left, right)` is the positive inner product $\langle\mathrm{left}|\mathrm{right}\rangle = \sum_n\mathrm{left}_n^*\,\mathrm{right}_n$ of Section 10.11; `np.conj` is the complex conjugate, and patterns missing from `right` count as amplitude 0. `largest(state)` is the largest size of an amplitude; `default=0.0` returns 0 for the empty dictionary, the zero state. A check of the form "`largest(a - b)` is tiny" says that the states $a$ and $b$ agree.

```python
VACUUM = {0: 1.0}
rng = np.random.default_rng(12345)  # random numbers with a fixed seed


def random_state(patterns=6):
    state = {}
    for n in rng.integers(0, 2 ** 16, size=patterns):
        state[int(n)] = complex(rng.normal(), rng.normal())
    length = np.sqrt(inner(state, state).real)
    return {n: a / length for n, a in state.items()}
```

`VACUUM` is the pattern 0 (every mode empty) with amplitude 1. `rng` is a generator of random numbers started with the fixed *seed* 12345, so that every run draws the same numbers and the notebook prints the same output every time. `random_state` picks a few patterns at random (`rng.integers(0, 2 ** 16, size=patterns)` draws whole numbers from 0 up to $2^{16} - 1$), gives each a complex amplitude whose real and imaginary parts are drawn from the normal distribution (`rng.normal()`), and divides by the length, so that the state is normalised.

```python
phi = random_state()
worst = 0.0
for p in range(16):
    for q in range(16):
        # {f_p, f_q^*} phi = f_p f_q^* phi + f_q^* f_p phi must be phi (p = q) or 0
        both = add((1, annihilate(p, create(q, phi))),
                   (1, create(q, annihilate(p, phi))))
        expected = phi if p == q else {}
        worst = max(worst, largest(add((1, both), (-1, expected))))
        # {f_p, f_q} phi must be 0
        pair = add((1, annihilate(p, annihilate(q, phi))),
                   (1, annihilate(q, annihilate(p, phi))))
        worst = max(worst, largest(pair))
```

For a random state $\phi$ the loops test every pair of modes $(p, q)$, $16 \times 16 = 256$ pairs. `both` is $\{f_p, f_q^*\}\phi = f_pf_q^*\phi + f_q^*f_p\phi$ (an operator applied to the result of another is a product of operators), which must be $\phi$ for $p = q$ and 0 otherwise, as the comment line says; `pair` is $\{f_p, f_q\}\phi$, which must be 0. `worst` keeps the largest deviation seen in the $2 \times 256 = 512$ relations.

```python
report("largest violation of the 512 anticommutation relations", f"{worst:.1e}")
check(worst < 1e-14, "the Fock operators obey {f_p, f_q^*} = delta_pq, {f_p, f_q} = 0")
```

The RESULT line shows `0.0e+00`: the relations hold exactly, because the amplitudes are only multiplied by $\pm1$ and added. The check prints its PASS line.

**In [4], the canonical field on the Fock space.**

```python
def psi(A, state):
    return annihilate(A - 1, state)


def psi_dagger(A, state):
    return add(*[(B[C - 1, A - 1], create(C - 1, state))
                 for C in range(1, 17) if B[C - 1, A - 1] != 0])
```

These are the operators of the positive realisation of Section 10.14: $\Psi_A = f_{A-1}$ (component $A$ uses mode $A - 1$, because the computer counts from 0), and the canonical conjugate $\Psi^\dagger_A = \sum_C\chi_CB_{CA}$ with $\chi_C = f^*_{C-1}$. The list comprehension builds the pairs (coefficient $B_{CA}$, state $f^*_{C-1}$ applied to the state) for the components $C$ with $B_{CA} \neq 0$ (only one per column, because $B$ has one nonzero entry in every column), and the star in `add(*[...])` passes the list as separate arguments.

```python
worst = 0.0
for A in range(1, 17):
    for C_index in range(1, 17):
        both = add((1, psi(A, psi_dagger(C_index, phi))),
                   (1, psi_dagger(C_index, psi(A, phi))))
        worst = max(worst, largest(add((1, both), (-B[A - 1, C_index - 1], phi))))
report("largest violation of {Psi_A, Psi^dagger_C} = B_AC", f"{worst:.1e}")
check_record(worst < 1e-14, "on the Fock space {Psi_A, Psi^dagger_C} = B_AC (256 pairs)",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "canonical_anticommutator_B")
```

For all 256 pairs $(A, C)$ the loop computes $\{\Psi_A, \Psi^\dagger_C\}\phi$ and subtracts $B_{AC}\phi$ (the name `C_index` avoids overwriting the matrix `C`). The largest deviation is printed as `0.0e+00`, and the check reproduces the record check `canonical_anticommutator_B`: the canonical rule holds on a positive Fock space once $\Psi^\dagger$ is defined as $\chi B$.

```python
m_value = 1.3  # any mass and momenta (here with momenta along the extra times too)
k = {1: 0.4, 2: -0.7, 3: 0.2, 5: 0.9, 6: -0.3, 7: 0.5, 8: 1.1}
h_prime = m_value * C - 1j * sum(k_a * (C @ gamma[a]) for a, k_a in k.items())
h_mode = -1j * m_value * gamma[4] - sum(k_a * (gamma[4] @ gamma[a])
                                         for a, k_a in k.items())
check(np.max(np.abs(B @ h_prime - h_mode)) < 1e-14,
      "B (m C - i sum_a k_a C gamma^a) equals the mode Hamiltonian h")
```

A mass of 1.3 and momenta along all seven slice directions, including the extra times (the identity holds for all of them). `h_prime` is the Hamiltonian-density matrix $h' = mC - i\sum_ak_aC\gamma^{(x_a)}$ of Section 10.12 and `h_mode` the mode Hamiltonian $h = -im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_ak_a\gamma^{(x_a)}$ of Section 10.3. The check confirms $Bh' = h$, derived line by line in Section 10.12.

```python
def hamiltonian(state):
    M = B @ h_prime
    return add(*[(M[c_, d_], create(c_, annihilate(d_, state)))
                 for c_ in range(16) for d_ in range(16) if abs(M[c_, d_]) > 0])
```

`hamiltonian(state)` applies the energy operator $H = \Psi^\dagger h'\Psi = \sum_{A,D}\chi_C B_{CA}h'_{AD}\Psi_D = \sum_{C,D}(Bh')_{CD}\chi_C\Psi_D$ to a state: for each pair of modes $(c, d)$ with a nonzero entry of $M = Bh'$ it takes $f_c^*f_d$ applied to the state (first empty mode $d$, then fill mode $c$) with the coefficient $M_{cd}$. The underscores in `c_` and `d_` only distinguish these names from others.

```python
worst = 0.0
for c_ in range(16):
    commutator = add((1, hamiltonian(annihilate(c_, phi))),
                     (-1, annihilate(c_, hamiltonian(phi))))  # [H, Psi_c] phi
    expected = add(*[(-h_mode[c_, d_], annihilate(d_, phi)) for d_ in range(16)])
    worst = max(worst, largest(add((1, commutator), (-1, expected))))
report("largest violation of [H, Psi_c] = -(h Psi)_c", f"{worst:.1e}")
check_record(worst < 1e-12,
             "Heisenberg: i d4 Psi = h Psi, the classical wave equation",
             record="Revision/theory/reports/wolfram-field-theory.json, check "
                    "Heisenberg_equation_reproduces_field_equation")
```

For each component the loop computes $[H, \Psi_c]\phi = H\Psi_c\phi - \Psi_cH\phi$ and compares it with $-(h\Psi)_c\phi = -\sum_dh_{cd}\Psi_d\phi$, the result $[H, \Psi_c] = -(Ah'\Psi)_c$ of Section 10.12 with $A = B$ and $Bh' = h$. The largest deviation is printed as `1.6e-17`, rounding only. By the Heisenberg equation this is $i\,\partial_4\Psi = h\Psi$, the classical wave equation of the field, and the check reproduces the Wolfram record check `Heisenberg_equation_reproduces_field_equation`. The cell prints three PASS lines in all.

**In [5], Theorem 10.2 on the recorded column.**

```python
u = np.zeros(16, dtype=complex)
u[6] = -1j / np.sqrt(2)  # u_7 (the computer counts from 0)
u[15] = 1 / np.sqrt(2)  # u_16
krein_norm_u = (u.conj() @ B @ u).real
report("u^dagger u and u^dagger B u", f"{(u.conj() @ u).real:.12f} and "
       f"{krein_norm_u:.12f}")
```

`np.zeros(16, dtype=complex)` is a column of 16 complex zeros; entries 7 and 16 (positions 6 and 15) are set to $-i/\sqrt2$ and $1/\sqrt2$, the column of the proof of Theorem 10.2. The RESULT line prints its ordinary squared length $u^\dagger u = 1.000000000000$ and its Krein norm $u^\dagger Bu = -1.000000000000$.

```python
def X(state):  # X = sum_A conj(u_A) Psi_A
    return add(*[(np.conj(u[A - 1]), psi(A, state)) for A in range(1, 17)])


def X_hilbert(state):  # X^* = sum_A u_A chi_A (the Hilbert adjoint of X)
    return add(*[(u[A - 1], create(A - 1, state)) for A in range(1, 17)])


def X_canonical(state):  # X^dagger = sum_A u_A Psi^dagger_A (canonical conjugate)
    return add(*[(u[A - 1], psi_dagger(A, state)) for A in range(1, 17)])
```

The three operators of Section 10.14: $X = \sum_Au_A^*\Psi_A$, its Hilbert adjoint $X^* = \sum_Au_A\chi_A$ (with $\chi_A = f^*_{A-1}$, the function `create`), and its canonical conjugate $X^\dagger = \sum_Au_A\Psi^\dagger_A$, as the comments say.

```python
hilbert = add((1, X(X_hilbert(phi))), (1, X_hilbert(X(phi))))
canonical = add((1, X(X_canonical(phi))), (1, X_canonical(X(phi))))
hilbert_ok = largest(add((1, hilbert), (-1, phi))) < 1e-14  # {X, X^*} = +1
canonical_ok = largest(add((1, canonical), (1, phi))) < 1e-14  # {X, X^dagger} = -1
check_record(np.max(np.abs(B @ u + u)) < 1e-15 and abs(krein_norm_u + 1) < 1e-15
             and hilbert_ok and canonical_ok,
             "B u = -u: {X, X^*} = +1 but the canonical {X, X^dagger} = -1",
             record="Revision/theory/reports/wolfram-field-theory.json, check "
                    "no_positive_inner_product")
```

`hilbert` is $\{X, X^*\}\phi$ and `canonical` is $\{X, X^\dagger\}\phi$. The check requires $Bu = -u$, $u^\dagger Bu = -1$, $\{X, X^*\}\phi = +\phi$ and $\{X, X^\dagger\}\phi = -\phi$, and reproduces the record check `no_positive_inner_product`: on a positive space the canonical conjugate is $-X^*$, not $X^*$, exactly as derived in Section 10.14.

**In [6], positivity made visible.**

```python
lengths = []
for _ in range(300):
    state = random_state(patterns=4)
    x_part, x_star_part = X(state), X_hilbert(state)
    lengths.append((inner(x_part, x_part).real, inner(x_star_part, x_star_part).real))
lengths = np.array(lengths)
sums = lengths.sum(axis=1)
```

For 300 random normalised states (each a combination of 4 random patterns) the loop stores the pair of squared lengths $(\lVert X\phi\rVert^2, \lVert X^*\phi\rVert^2)$. `np.array` turns the list of pairs into a table with 300 rows and 2 columns, and `.sum(axis=1)` adds the two numbers of each row.

```python
report("smallest and largest |X phi|^2 + |X^* phi|^2",
       f"{sums.min():.12f} and {sums.max():.12f}")
check(np.all(lengths >= 0) and np.max(np.abs(sums - 1)) < 1e-12,
      "positivity: |X phi|^2 + |X^* phi|^2 = 1 for every random state")
```

By Section 10.11, $\lVert X\phi\rVert^2 + \lVert X^*\phi\rVert^2 = \langle\phi|\{X, X^*\}\phi\rangle = \langle\phi|\phi\rangle = 1$. The printed smallest and largest sums are both `1.000000000000`, and the check requires every squared length to be $\geq 0$ and every sum to be 1.

```python
columns = rng.normal(size=(5000, 16)) + 1j * rng.normal(size=(5000, 16))
columns = columns / np.linalg.norm(columns, axis=1, keepdims=True)  # unit length
krein_norms = np.einsum("ni,ij,nj->n", columns.conj(), B, columns).real
```

5000 random complex columns with 16 entries (one per row of the table `columns`) are drawn and each is divided by its length (`np.linalg.norm(..., axis=1, keepdims=True)` computes the length of every row and keeps it as a column, so that the division acts row by row). `np.einsum("ni,ij,nj->n", ...)` computes, for each row $n$, the sum $\sum_{i,j}v_i^*B_{ij}v_j = v^\dagger Bv$: the letters name the indices, and the indices that do not appear after the arrow are summed over.

```python
report("smallest and largest Krein norm of the 5000 unit columns",
       f"{krein_norms.min():.3f} and {krein_norms.max():.3f}")
check(krein_norms.min() < -0.5 and krein_norms.max() > 0.5
      and np.all(np.abs(krein_norms) <= 1 + 1e-12),
      "random unit columns have Krein norms of both signs, all between -1 and 1")
```

The printed range is from `-0.777` to `0.704`. A Krein norm of a unit column can never lie outside $[-1, 1]$, because the eigenvalues of $B$ are $\pm1$; the check requires values below $-0.5$ and above $0.5$ (both signs) and none outside that interval.

```python
fig, ax = plt.subplots(figsize=(6.0, 4.6))
ax.plot(lengths[:, 0], lengths[:, 1], "o", color="#2a78d6", markersize=4,
        label="300 random states $\\phi$")
line = np.linspace(-1.4, 1.2, 2)
ax.plot(line, 1 - line, color="#52514e", linewidth=1, label="$x + y = 1$")
ax.plot(line, -1 - line, "--", color="#eb6834", linewidth=2,
        label="$x + y = -1$ (canonical rule)")
```

The first picture: each random state is a blue dot at $x = \lVert X\phi\rVert^2$, $y = \lVert X^*\phi\rVert^2$. `line` holds the two end points $-1.4$ and $1.2$ of a horizontal range, and the two `plot` calls draw the straight lines $y = 1 - x$ (grey) and $y = -1 - x$ (orange, dashed): the line on which the dots lie, and the line on which they would have to lie if the canonical conjugate were the Hilbert adjoint.

```python
ax.set_xlim(-1.4, 1.2)
ax.set_ylim(-1.4, 1.2)
ax.set_xlabel("$x = \\|X\\phi\\|^2$")
ax.set_ylabel("$y = \\|X^*\\phi\\|^2$")
ax.set_title("Squared lengths are never negative")
ax.legend(loc="lower left")
save_figure(fig, "positivity",
...)
```

The ranges of both axes are fixed so that the negative quarter, where the dashed line runs, is visible. Figure 1 of Notebook 10b shows all 300 dots on the grey line, inside the quarter where both squared lengths are positive, and the orange dashed line far away in the region of negative values that no state can reach: this is Theorem 10.2 in one picture.

```python
fig, ax = plt.subplots()
ax.set_axisbelow(True)  # draw the grid lines behind the bars
ax.hist(krein_norms, bins=50, range=(-1, 1), color="#2a78d6", edgecolor="white")
ax.axvline(0.0, color="#52514e", linewidth=1)
ax.set_xlabel("Krein norm $v^\\dagger B v$ of a random column with $v^\\dagger v = 1$")
ax.set_ylabel("number of columns (of 5000)")
ax.set_title("The Krein form is indefinite: both signs occur")
save_figure(fig, "krein_norms_random",
...)
```

The second picture is a **histogram**: `ax.hist` divides the interval from $-1$ to 1 into 50 equal bins and draws one bar per bin, as tall as the number of Krein norms that fall into it. Figure 2 of Notebook 10b shows a bell-shaped distribution centred at 0 and symmetric: every random unit column has the ordinary length 1, but its Krein norm is positive about as often as negative, and usually small, because a random column mixes the eight directions of positive and the eight of negative charge.

**In [7], the Krein-Fock realisation.**

```python
def orthonormal_columns(P):
    basis = []
    for column in P.T:
        v = column.astype(complex)
        for _ in range(2):
            for e in basis:
                v = v - (e.conj() @ v) * e
        length = np.sqrt((v.conj() @ v).real)
        if length > 1e-8:
            basis.append(v / length)
    return np.array(basis).T
```

This is the Gram-Schmidt function `orthonormal_basis` of In [10] of Notebook 10a under another name (Section 10.10): it returns orthonormal columns that span the range of the matrix $P$, removing from each column of $P$ its parts along the columns found so far (twice, to remove rounding errors) and keeping what is left, divided by its length, when anything is left.

```python
plus_modes = orthonormal_columns((np.eye(16) + B) / 2)  # B u = +u, 8 columns
minus_modes = orthonormal_columns((np.eye(16) - B) / 2)  # B u = -u, 8 columns
U = np.hstack([plus_modes, minus_modes]).astype(complex)  # 16 modes as columns
epsilon = np.array([1.0] * 8 + [-1.0] * 8)  # their Krein norms
```

$\frac12(I_{16} \pm B)$ are the projectors onto the eigenspaces of $B$ for $+1$ and $-1$ (by $BB = I_{16}$, the argument of Section 10.5). Their orthonormal columns are 8 modes with $Bu = u$ and 8 with $Bu = -u$; `U` holds the 16 modes as its columns, and `epsilon` their Krein norms $+1$ (eight times) and $-1$ (eight times).

```python
cosh_t, sinh_t = 5 / 4, 3 / 4  # a Krein boost of the modes 1 and 9
first, ninth = U[:, 0].copy(), U[:, 8].copy()
U[:, 0] = cosh_t * first + sinh_t * ninth
U[:, 8] = sinh_t * first + cosh_t * ninth
E = np.diag(epsilon)
```

The Krein boost of Section 10.14 with $\cosh t = \frac54$, $\sinh t = \frac34$ replaces mode 1 by $\frac54u_1 + \frac34u_9$ and mode 9 by $\frac34u_1 + \frac54u_9$. `.copy()` keeps the old columns, so that the second line still uses the old first column. `E` is the diagonal matrix $E = \mathrm{diag}(\epsilon_1, \dots, \epsilon_{16})$.

```python
gram_ok = np.max(np.abs(U.conj().T @ B @ U - E)) < 1e-14  # U^dagger B U = E
complete_ok = np.max(np.abs(U @ E @ U.conj().T - B)) < 1e-14  # U E U^dagger = B
report("squared ordinary length of the boosted mode 1",
       f"{np.linalg.norm(U[:, 0]) ** 2:.6f}")
check(gram_ok and complete_ok,
      "Krein-orthonormal modes: U^dagger B U = E and U E U^dagger = B")
```

The check confirms the two matrix identities of Section 10.14, $U^\dagger BU = E$ (the boosted modes are still Krein-orthonormal) and $UEU^\dagger = B$. The RESULT line prints the squared ordinary length of the boosted mode, `2.125000`, which is $\frac{34}{16}$.

```python
def b(n, state):  # b_n = f_n
    return annihilate(n, state)


def b_dagger(n, state):  # b_n^dagger = epsilon_n f_n^*
    return add((epsilon[n], create(n, state)))
```

On the positive Fock space the Krein-Fock operators are realised as $b_n = f_n$ and $b_n^\dagger = \epsilon_nf_n^*$, so that $\{b_n, b_n^\dagger\} = \epsilon_n\{f_n, f_n^*\} = \epsilon_n$, the rule of Section 10.14.

```python
def krein_psi(A, state):  # Psi_A = sum_n (u_n)_A b_n
    return add(*[(U[A - 1, n], b(n, state)) for n in range(16)])


def krein_psi_dagger(A, state):  # Psi^dagger_A = sum_n conj((u_n)_A) b_n^dagger
    return add(*[(np.conj(U[A - 1, n]), b_dagger(n, state)) for n in range(16)])
```

The field $\Psi = \sum_nu_nb_n$ and its conjugate $\Psi^\dagger = \sum_nu_n^\dagger b_n^\dagger$, component by component; `U[A - 1, n]` is entry $A$ of the mode $u_{n+1}$.

```python
worst = 0.0
for A in range(1, 17):
    for C_index in range(1, 17):
        both = add((1, krein_psi(A, krein_psi_dagger(C_index, phi))),
                   (1, krein_psi_dagger(C_index, krein_psi(A, phi))))
        worst = max(worst, largest(add((1, both), (-B[A - 1, C_index - 1], phi))))
report("Krein-Fock: largest violation of {Psi_A, Psi^dagger_C} = B_AC", f"{worst:.1e}")
check(worst < 1e-13, "Krein-Fock realisation: {Psi, Psi^dagger} = B again")
```

As in In [4], all 256 anticommutators are compared with $B_{AC}$. The largest deviation is printed as `1.6e-16`: the Krein-Fock realisation gives the same canonical rule. The cell prints two PASS lines.

**In [8], the expectation-value rule.**

```python
def expectation(n, M):
    excited = b_dagger(n, VACUUM)  # b_n^dagger |0>
    acted = {}
    for A in range(1, 17):
        psi_part = krein_psi(A, excited)
        for C_index in range(1, 17):
            if M[C_index - 1, A - 1] != 0:
                acted = add((1, acted), (M[C_index - 1, A - 1],
                                         krein_psi_dagger(C_index, psi_part)))
    numerator = inner(VACUUM, b(n, acted))  # <0| b_n ... |0>, a number
    norm = inner(VACUUM, b(n, excited))  # <0| b_n b_n^dagger |0> = epsilon_n
    return numerator / norm
```

`expectation(n, M)` computes the left side of the normalised rule of Section 10.14. `excited` is the state $b_n^\dagger|0\rangle$. The double loop applies $\Psi^\dagger M\Psi = \sum_{C,A}M_{CA}\Psi^\dagger_C\Psi_A$ to it: for each $A$ it computes $\Psi_A$ applied to the excited state once (`psi_part`), and adds $M_{CA}\Psi^\dagger_C$ applied to that. Then $b_n$ is applied and the result is projected on the vacuum: `numerator` is $\langle 0|b_n(\Psi^\dagger M\Psi)b_n^\dagger|0\rangle$ and `norm` is $\langle 0|b_nb_n^\dagger|0\rangle = \epsilon_n$, as the comments say. The function returns their quotient.

```python
rule_errors, naive_errors, points = [], [], []
for _ in range(60):
    M = rng.normal(size=(16, 16)) + 1j * rng.normal(size=(16, 16))
    for n in (3, 0):  # mode 4 (unboosted) and mode 1 (boosted), counted from 0
        value = expectation(n, M)
        rule = epsilon[n] * (U[:, n].conj() @ M @ U[:, n])
        naive = U[:, n].conj() @ B @ M @ U[:, n]
        rule_errors.append(abs(value - rule))
        if n == 3:
            naive_errors.append(abs(value - naive))
        else:
            points.append((value.real, rule.real, naive.real))
points = np.array(points)
```

For 60 random complex matrices $M$ and two modes, mode 4 (not boosted, an eigenvector of $B$) and mode 1 (boosted), the loop compares the Fock-space value with the rule $\epsilon_nu_n^\dagger Mu_n$ and with the form $u_n^\dagger BMu_n$. The deviations from the rule are collected for both modes; the deviations from $u^\dagger BMu$ only for mode 4, where it must also hold; for the boosted mode the three real parts are stored for the figure.

```python
naive_boosted = np.max(np.abs(points[:, 0] - points[:, 2]))
report("largest |Fock value - epsilon u^dagger M u| (both modes)",
       f"{max(rule_errors):.1e}")
report("boosted mode: largest |Fock value - u^dagger B M u|", f"{naive_boosted:.2f}")
check_record(max(rule_errors) < 1e-12 and max(naive_errors) < 1e-12
             and naive_boosted > 0.1,
             "expectation rule eps u^dagger M u; u^dagger B M u fails if boosted",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "expectation_value_rule")
```

The printed lines show the deviation from the rule, `1.3e-15` (rounding only), and the deviation of the form $u^\dagger BMu$ for the boosted mode, `5.82`: large. The check requires both and reproduces the record check `expectation_value_rule`.

**In [9], two pictures of the Krein-Fock realisation.**

```python
fig, ax = plt.subplots(figsize=(6.0, 6.0))
angle = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(angle), np.sin(angle), color="#52514e", linewidth=1.5,
        label="ordinary length 1: $a^2 + b^2 = 1$")
```

In the plane of the columns $au_1 + bu_9$ (with $Bu_1 = u_1$, $Bu_9 = -u_9$, both of length 1 and orthogonal) the ordinary squared length is $a^2 + b^2$ and the Krein norm is $a^2 - b^2$. The points $(\cos\theta, \sin\theta)$ for 400 angles from 0 to $2\pi$ draw the grey unit circle, the columns of ordinary length 1.

```python
t = np.linspace(-1.6, 1.6, 400)
for side in (1, -1):  # the two branches of each hyperbola
    ax.plot(side * np.cosh(t), np.sinh(t), color="#2a78d6", linewidth=2,
            label="Krein norm $+1$: $a^2 - b^2 = 1$" if side == 1 else None)
    ax.plot(np.sinh(t), side * np.cosh(t), color="#eb6834", linewidth=2,
            label="Krein norm $-1$: $a^2 - b^2 = -1$" if side == 1 else None)
```

Since $\cosh^2t - \sinh^2t = 1$, the points $(\pm\cosh t, \sinh t)$ lie on the **hyperbola** $a^2 - b^2 = 1$ (blue, the columns of Krein norm $+1$) and the points $(\sinh t, \pm\cosh t)$ on $a^2 - b^2 = -1$ (orange). Each hyperbola has two branches, drawn by the two passes of the loop; only the first pass labels the curves (`None` gives no legend entry).

```python
ax.plot([0, 1, 0], [1, 0, 0], "s", color="#52514e", markersize=7)
ax.annotate("$u_1$", (1.0, 0.0), xytext=(1.05, -0.3))
ax.annotate("$u_9$", (0.0, 1.0), xytext=(-0.35, 1.05))
ax.plot([1.25, 0.75], [0.75, 1.25], "o", color="#1baf7a", markersize=9,
        label="boosted modes $(5/4, 3/4)$, $(3/4, 5/4)$")
for x_end, y_end in ((1.25, 0.75), (0.75, 1.25)):
    ax.annotate("", xy=(x_end, y_end), xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "color": "#1baf7a"})
```

Grey squares mark the origin and the two unboosted modes, $u_1 = (1, 0)$ and $u_9 = (0, 1)$, which `annotate` labels. Green dots mark the boosted modes $(\frac54, \frac34)$ and $(\frac34, \frac54)$, and an annotation without text but with `arrowprops` draws an arrow from the origin to each.

```python
ax.set_xlim(-2.6, 2.6)
ax.set_ylim(-2.6, 2.6)
ax.set_aspect("equal")
ax.set_xlabel("coefficient $a$ of $u_1$")
ax.set_ylabel("coefficient $b$ of $u_9$")
ax.set_title("Ordinary length versus Krein norm in one plane")
ax.legend(loc="lower left", fontsize=8)
save_figure(fig, "krein_plane",
...)
```

`set_aspect("equal")` gives both axes the same scale, so that the circle looks round. Figure 3 of Notebook 10b shows the boosted modes outside the unit circle (their ordinary length is larger than 1) but exactly on the hyperbolas of Krein norm $+1$ and $-1$: a Krein boost keeps the Krein norms and changes the ordinary lengths, as a Lorentz boost keeps $t^2 - x^2$ and changes $t$ and $x$.

```python
fig, ax = plt.subplots(figsize=(6.0, 5.0))
ax.plot(points[:, 1], points[:, 0], "o", color="#1baf7a", markersize=5,
        label="against the rule $\\epsilon\\,u^\\dagger M u$")
ax.plot(points[:, 2], points[:, 0], "x", color="#eb6834", markersize=6,
        label="against $u^\\dagger B M u$")
low, high = points.min() - 1, points.max() + 1
ax.plot([low, high], [low, high], color="#52514e", linewidth=1)
ax.set_xlabel("value of the formula (real part)")
ax.set_ylabel("value computed on the Fock space (real part)")
ax.set_title("The boosted mode: which formula is right?")
ax.legend(loc="upper left", fontsize=8)
save_figure(fig, "expectation_rule",
...)
```

The second picture plots, for the boosted mode and the 60 random matrices, the Fock-space value (vertical) against the rule (green dots) and against $u^\dagger BMu$ (orange crosses), with the grey diagonal from a little below the smallest to a little above the largest value. Figure 4 of Notebook 10b shows the green dots exactly on the diagonal and the orange crosses scattered around it: the rule of the record is right, the form $u^\dagger BMu$ is right only for modes that are eigenvectors of $B$.

**In [10], maps that keep the canonical rule, and the conjugation.**

```python
pairing = json.loads(repository_file("Revision/pairing/pairing-theory.json")
                     .read_text(encoding="utf-8"))
rows = pairing["data"]["Krein_signs_M_B_Mdagger"]
maps = {"Gamma": Gamma}
for a in range(1, 9):
    maps[f"gamma^x{a}"] = gamma[a]
    maps[f"P_x{a}"] = Gamma @ gamma[a]  # the reflection P_a = Gamma gamma^(x_a)
```

The pairing record is read, and `rows` is its list of 17 entries, each holding the name of a map and the recorded sign. The dictionary `maps` pairs the same names with the matrices: the chirality, the eight gammas and the eight reflections $P_a = \Gamma\gamma^{(x_a)}$.

```python
signs, agree = [], True
for row in rows:
    M = maps[row["map"]]
    transformed = M @ B @ M.conj().T  # M B M^dagger
    sign = (1 if np.array_equal(transformed, B)
            else -1 if np.array_equal(transformed, -B) else 0)
    signs.append(sign)
    agree = agree and sign == row["sign"]
names = [row["map"] for row in rows]  # the names of the 17 maps in the record
```

For each recorded map the loop computes $MBM^\dagger$ exactly and reads off its sign: $+1$ if it equals $B$, $-1$ if it equals $-B$, and 0 otherwise (which never happens). `agree` stays true while every computed sign equals the recorded one.

```python
say("map: sign sigma in M B M^dagger = sigma B")
say(", ".join(f"{name}: {s:+d}" for name, s in zip(names, signs)))
check_record(agree and len(rows) == 17,
             "the Krein signs of all 17 recorded maps are reproduced",
             record="Revision/pairing/pairing-theory.json, data "
                    "Krein_signs_M_B_Mdagger")
```

The format code `+d` prints a whole number with its sign. The printed list is the table of Section 10.15: `Gamma: -1`, the gammas of $x_1$ to $x_4$ and $x_8$ with $+1$, those of $x_5$ to $x_7$ with $-1$, the reflections $P_1$ to $P_4$ and $P_8$ with $-1$ and $P_5$ to $P_7$ with $+1$. The check reproduces the record's data.

```python
check_record(np.array_equal(Gamma @ B @ Gamma.T, -B),
             "the chirality image Gamma Psi carries the Krein metric -B",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.image_krein_metric")
check_record(np.array_equal(gamma[8] @ B @ gamma[8].T, B),
             "the mirror image gamma^(x8) Psi keeps +B",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.T2_image_keeps_B")
```

The two maps of the pairing theorems separately: $\Gamma B\Gamma^T = -B$ and $\gamma^{(x_8)}B(\gamma^{(x_8)})^T = +B$ (for real matrices the conjugate transpose is the transpose). They reproduce the sympy record checks `Q.image_krein_metric` and `Q.T2_image_keeps_B`.

```python
identity = np.eye(16)
conjugation_identity = identity @ B.T @ identity.conj().T  # M = I
conjugation_gamma = Gamma @ B.T @ Gamma.conj().T  # M = Gamma
check(np.array_equal(B.T, -B), "B^T = -B (B is Hermitian and purely imaginary)")
check_record(np.array_equal(conjugation_gamma, B)
             and np.array_equal(conjugation_identity, -B),
             "Psi -> Gamma Psi^(dagger T) keeps B; with M = I one gets -B",
             record="Revision/lead_checks/reports/charge-conjugation-and-u1.json, "
                    "check quantum_charge_conjugation_unitary_type")
```

The conjugations of the quantised field, $\Psi \to M\Psi^{\dagger T}$, change the canonical matrix into $MB^TM^\dagger$ (Section 10.15). The cell checks $B^T = -B$, then $\Gamma B^T\Gamma^\dagger = +B$ and $I_{16}B^TI_{16} = -B$, and reproduces the lead check `quantum_charge_conjugation_unitary_type`.

```python
lead_file = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
lead_verdicts = list(REPORT_CHECKS[lead_file].values())  # read by check_record
passed = lead_verdicts.count("PASS")
report("checks of charge-conjugation-and-u1.json with the verdict PASS",
       f"{passed} of {len(lead_verdicts)}")
check(lead_verdicts == ["PASS"] * 12,
      "the lead-check report charge-conjugation-and-u1.json holds 12 checks, all PASS")
```

The previous `check_record` has just read the lead-check report into the dictionary `REPORT_CHECKS` of In [2]. `REPORT_CHECKS[lead_file].values()` are the verdicts of all its checks, and `list(...)` makes a list of them; `lead_verdicts.count("PASS")` counts the entries equal to `PASS`. The RESULT line prints `12 of 12`, and the check confirms that the report holds exactly 12 checks, all with the verdict PASS (`["PASS"] * 12` is the list of twelve such entries): the number of checks that the table of records in Section 10.1 gives for this report.

```python
mass_reversed = all(np.array_equal(Gamma @ gamma[a] @ Gamma, -gamma[a])
                    for a in range(1, 9))
check(mass_reversed, "Gamma anticommutes with every gamma: the conjugation reverses m")
```

$\Gamma\gamma^{(x_a)}\Gamma = -\gamma^{(x_a)}$ for all eight gammas, which is the reason why $\Gamma\Psi^*$ obeys the equation of mass $-m$ (Section 10.15). The cell prints seven PASS lines.

**In [11], the signs as a bar chart.**

```python
labels = [row["map"].replace("gamma^x", "g").replace("P_x", "P") for row in rows]
labels = [lab if lab != "Gamma" else "Gam" for lab in labels]
colours = ["#2a78d6" if s > 0 else "#eb6834" for s in signs]
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0),
                         gridspec_kw={"width_ratios": [4, 1]})
for ax in axes:
    ax.set_axisbelow(True)  # draw the grid lines behind the bars
```

Short labels are made from the recorded names (`gamma^x1` becomes `g1`, `P_x1` becomes `P1`, and `Gamma` becomes `Gam`), and each bar gets blue for the sign $+1$ and orange for $-1$. The figure has two panels; `width_ratios` makes the first four times as wide as the second.

```python
axes[0].bar(range(len(signs)), signs, color=colours, width=0.7)
axes[0].set_xticks(range(len(signs)), labels)
axes[0].axhline(0, color="#52514e", linewidth=1)
axes[0].set_ylim(-1.4, 1.4)
axes[0].set_yticks([-1, 0, 1])
axes[0].set_ylabel("sign $\\sigma$ in $M B M^\\dagger = \\sigma B$")
axes[0].set_title("linear maps $\\Psi \\to M\\Psi$")
```

The left panel draws one bar of height $+1$ or $-1$ per map, labelled under the axis.

```python
conjugation_signs = [-1, 1]  # M = I gives -B, M = Gamma gives +B
axes[1].bar([0, 1], conjugation_signs, color=["#eb6834", "#2a78d6"], width=0.6)
axes[1].set_xticks([0, 1], ["$M = I$", "$M = \\Gamma$"])
axes[1].axhline(0, color="#52514e", linewidth=1)
axes[1].set_ylim(-1.4, 1.4)
axes[1].set_yticks([-1, 0, 1])
axes[1].set_title("$\\Psi \\to M\\Psi^{\\dagger T}$")
save_figure(fig, "krein_signs",
...)
```

The right panel draws the two conjugations, with the signs just checked in In [10]. Figure 5 of Notebook 10b shows five orange bars among the gammas and reflections ($\Gamma$, $\gamma^{(x_5)}$ to $\gamma^{(x_7)}$ and five reflections) and, on the right, the orange bar of $M = I$ next to the blue bar of $M = \Gamma$: only the conjugation $\Psi \to \Gamma\Psi^{\dagger T}$, which reverses the mass, keeps the canonical rule.

**In [12], the last check.**

```python
for name in ("10b_1_positivity.png", "10b_2_krein_norms_random.png",
             "10b_3_krein_plane.png", "10b_4_expectation_rule.png",
             "10b_5_krein_signs.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The loop checks that each of the five figure files exists, and the last line prints ALL 25 CHECKS PASSED (notebook 10b): the five figure checks and the 20 checks of the cells before (3 in In [2], 1 in In [3], 3 in In [4], 1 in In [5], 2 in In [6], 2 in In [7], 1 in In [8] and 7 in In [10]).

### 10.20 The good sector: a positive Fock space for one momentum

Theorem 10.2 forbids a positive inner product with $\Psi^\dagger$ read as the Hilbert adjoint, and Theorem 10.1 says that even the one-particle waves of real frequency mix the two signs of charge four and four. Yet the Revision record constructs, in the **good sector** (no momentum along the extra times, $k_5 = k_6 = k_7 = 0$), a POSITIVE quantum state space for each single momentum with frozen coefficients (flat-frame plane waves, in which the deflation of the extra times does not enter), with particles and antiparticles of positive energy. This section derives it line by line; the scope is stated at its end.

**The waves of one good-sector momentum.** In the good sector the mode Hamiltonian is

$$
h = m\beta + \sum_{a = 1, 2, 3, 8}k_a\alpha^a,\qquad \beta = -i\gamma^{(x_4)},\qquad \alpha^a = -\gamma^{(x_4)}\gamma^{(x_a)} .
$$

All five matrices are Hermitian (Section 10.4), so $h$ is Hermitian. By Section 10.4, $hh = E^2I_{16}$ with $E = \sqrt{m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2} > 0$ and $\mathrm{tr}\,h = 0$, so $h$ has the eigenvalue $+E$ eight times and $-E$ eight times. Choose orthonormal eigenvectors $u_1, \dots, u_8$ with $hu_s = Eu_s$ and $v_1, \dots, v_8$ with $hv_s = -Ev_s$ (for example by the Gram-Schmidt method applied to the columns of the projectors $\frac12(I_{16} \pm h/E)$ of Section 10.5). A $u$ and a $v$ are orthogonal:

$$
E\,v^\dagger u = v^\dagger hu = (h^\dagger v)^\dagger u = (hv)^\dagger u = -E\,v^\dagger u ,
$$

by $hu = Eu$, the rule $(Xv)^\dagger = v^\dagger X^\dagger$, $h^\dagger = h$ and $hv = -Ev$ ($E$ is real); so $2E\,v^\dagger u = 0$ and $v^\dagger u = 0$. The $16 \times 16$ matrix $W = (u_1, \dots, u_8, v_1, \dots, v_8)$ therefore has orthonormal columns, $W^\dagger W = I_{16}$. Then $W$ is invertible with $W^{-1} = W^\dagger$, and so also $WW^\dagger = I_{16}$, which written out is the **completeness** relation $\sum_s u_su_s^\dagger + \sum_s v_sv_s^\dagger = I_{16}$.

**The field on a positive Fock space.** Take 16 fermion modes on a positive Fock space, called $b_1, \dots, b_8$ (particles) and $d_1, \dots, d_8$ (antiparticles), with $\{b_s, b_{s'}^*\} = \{d_s, d_{s'}^*\} = \delta_{ss'}$ and all other anticommutators zero, and put

$$
\Psi = \sum_s\big(u_s\,b_s + v_s\,d_s^*\big),\qquad \chi = \sum_s\big(u_s^\dagger\,b_s^* + v_s^\dagger\,d_s\big),\qquad \Psi^\dagger = \chi B .
$$

$\chi$ (a row of 16 operators) is the Hilbert adjoint of $\Psi$, and $\Psi^\dagger = \chi B$ is the positive realisation of Section 10.14. Line by line:

$$
\{\Psi_A, \chi_C\} = \sum_s(u_s)_A(u_s)_C^*\{b_s, b_s^*\} + \sum_s(v_s)_A(v_s)_C^*\{d_s^*, d_s\}
$$

$$
= \sum_s(u_s)_A(u_s)_C^* + \sum_s(v_s)_A(v_s)_C^* = (WW^\dagger)_{AC} = \delta_{AC} .
$$

The first step keeps only the anticommutators of an operator with its own adjoint (all others vanish); the second uses $\{b_s, b_s^*\} = \{d_s^*, d_s\} = 1$; the third recognises the product $WW^\dagger$; the fourth is completeness. Then, exactly as in Section 10.14, $\{\Psi_A, \Psi^\dagger_C\} = \sum_D\{\Psi_A, \chi_D\}B_{DC} = B_{AC}$: the canonical rule holds.

**The energy, line by line.** By Section 10.12 the energy of the momentum is $H = \Psi^\dagger h'\Psi = \chi Bh'\Psi = \chi h\Psi$. Since $h\Psi = \sum_s(Eu_sb_s - Ev_sd_s^*)$,

$$
\chi h\Psi = \sum_{s,s'}\big(u_{s'}^\dagger b_{s'}^* + v_{s'}^\dagger d_{s'}\big)\big(Eu_sb_s - Ev_sd_s^*\big) = \sum_sE\,b_s^*b_s - \sum_sE\,d_sd_s^* .
$$

The second step multiplies out and uses the orthonormality: $u_{s'}^\dagger u_s = v_{s'}^\dagger v_s = \delta_{ss'}$ and $u_{s'}^\dagger v_s = v_{s'}^\dagger u_s = 0$ (the numbers stand in front of the operators). Now $d_sd_s^* = 1 - d_s^*d_s$ by the anticommutator, for each of the 8 values of $s$:

$$
H = \sum_sE\,\big(b_s^*b_s + d_s^*d_s\big) - 8E .
$$

The **vacuum** $|0\rangle$ is the state with $b_s|0\rangle = d_s|0\rangle = 0$ for all $s$. Its energy is $-8E$: in the old picture of Dirac, every one of the 8 negative-energy levels $-E$ is filled, the filled **Dirac sea**. **Normal ordering** is the prescription that drops this constant: the normal-ordered energy is the energy minus that of the vacuum,

$$
{:}H{:} = \sum_sE\,\big(b_s^*b_s + d_s^*d_s\big) \geq 0 .
$$

A **particle** $b_s^*|0\rangle$ and an **antiparticle** $d_s^*|0\rangle$ (a hole in the filled sea) both have the energy $+E > 0$.

**The charge.** $Q = \Psi^\dagger B\Psi = \chi BB\Psi = \chi\Psi$, and the same steps with $h$ replaced by $I_{16}$ give

$$
\chi\Psi = \sum_s\big(b_s^*b_s + d_sd_s^*\big) = \sum_s\big(b_s^*b_s - d_s^*d_s\big) + 8 .
$$

After normal ordering a particle has the charge $+1$ and an antiparticle $-1$.

**Counting the states of one momentum.** A pattern with $N_b$ occupied particle modes and $N_d$ occupied antiparticle modes is an eigenstate of both operators: its normal-ordered energy is $E(N_b + N_d)$ and its normal-ordered charge is $N_b - N_d$ (each $b_s^*b_s$ and $d_s^*d_s$ counts whether its mode is occupied). The number of ways to choose $j$ occupied modes out of 8 is the **binomial coefficient** $\binom{8}{j} = \frac{8!}{j!\,(8 - j)!}$, where $n! = 1 \cdot 2 \cdots n$ and $0! = 1$; for example $\binom{8}{0} = 1$, $\binom{8}{1} = 8$ and $\binom{8}{4} = \frac{40320}{24 \cdot 24} = 70$. So $\binom{8}{N_b}\binom{8}{N_d}$ patterns have the given $N_b$ and $N_d$, and the total is $\sum_{N_b}\binom{8}{N_b}\sum_{N_d}\binom{8}{N_d} = 2^8 \cdot 2^8 = 65536$. Only the vacuum ($N_b = N_d = 0$) has the energy 0; $8 + 8 = 16$ states have one quantum; the largest group, $\binom84^2 = 4900$ states, has 8 quanta and the charge 0. No state has a negative normal-ordered energy.

| statement | status | where it is verified |
| --- | --- | --- |
| good sector, one momentum with frozen coefficients: positive Fock space, $\Psi^\dagger = \chi B$, $\{\Psi, \Psi^\dagger\} = B$; vacuum $-8E$; every quantum $+E$; charges $\pm1$ | PROVED (derivation above) and checked for $m = 2$, $k = (1, 2, 0, 4)$, $E = 5$ (vacuum $-40$) and for $m = 3$, $k_1 = 4$, $E = 5$ | `python-field-theory.json`, check `good_sector_positive_fock_realisation`; `wolfram-field-theory.json`, check `Fock_space_good_sector_example` |
| normal ordering (dropping the vacuum value) | ASSUMED | a prescription, as in Dirac's theory |
| scope: single good-sector momenta, in flat 4+4 space or in the frozen-coefficient model of Section 10.3 (ASSUMED: it leaves out the hidden-direction terms, including the connection term $3H\gamma^{(x_8)}$) | OPEN beyond it | a positive-norm Hilbert space for the whole field in the deflating background, the extra-time sector and the operator theory for $\lambda \neq 0$ beyond the finite model of Section 10.21 are not constructed; in the author's metric the curved good-sector mode operator is Hermitian only up to a boundary term at $z = \pi/2$ (Section 10.27; Revision theory document, section 11) |

### 10.21 The expectation-value rule and the energy-momentum tensor operator

**The rule in the positive realisation.** Every classical bilinear $\Psi^\dagger M\Psi$ becomes the operator $\chi BM\Psi$. Write $N = BM$ and insert the expansion:

$$
\chi N\Psi = \sum_{s,s'}\Big[(u_{s'}^\dagger Nu_s)\,b_{s'}^*b_s + (u_{s'}^\dagger Nv_s)\,b_{s'}^*d_s^* + (v_{s'}^\dagger Nu_s)\,d_{s'}b_s + (v_{s'}^\dagger Nv_s)\,d_{s'}d_s^*\Big].
$$

In the particle state $b_1^*|0\rangle$ the second and third kinds of terms change the number of quanta by two and have expectation value 0; the first kind gives $u_1^\dagger Nu_1$; the fourth gives $\sum_sv_s^\dagger Nv_s$, which is also its vacuum value and is removed by normal ordering. So the normal-ordered expectation value is $u_1^\dagger BMu_1$. In the antiparticle state $d_1^*|0\rangle$ the first kind gives 0, and the fourth gives $\sum_{s \neq 1}v_s^\dagger Nv_s$ (the term $s = 1$ vanishes, because $d_1^*d_1^*|0\rangle = 0$); minus the vacuum value this is $-v_1^\dagger Nv_1$. Hence the **expectation-value rule** of the Revision record:

$$
\langle{:}\Psi^\dagger M\Psi{:}\rangle = u^\dagger BMu\ \text{(particle)},\qquad \langle{:}\Psi^\dagger M\Psi{:}\rangle = -v^\dagger BMv\ \text{(antiparticle)} .
$$

Two examples: for $M = B$ (the charge) the rule gives $u^\dagger BBu = u^\dagger u = 1$ and $-v^\dagger v = -1$; for $M = h' = Bh$ (the energy) it gives $u^\dagger BBhu = u^\dagger hu = E$ and $-v^\dagger hv = -(-E) = E$.

**The energy-momentum tensor operator.** The energy-momentum tensor of Chapter 9 becomes an operator by replacing the field by the quantised field and normal ordering with respect to the good-sector modes (Revision record `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md`, section 12):

$$
\hat T^\nu{}_\mu(x) = {:}\,T^\nu{}_\mu\big[\hat\Psi, \hat{\bar\Psi}\big]\,{:},\qquad \hat{\bar\Psi} = \hat\Psi^\dagger C,\qquad \hat\Psi^\dagger = \hat\chi B .
$$

With $\hat S = \hat\Psi^\dagger C\hat\Psi$ and the kinetic terms $\hat K_\mu = \frac{1}{2f_\mu}(\hat{\bar\Psi}\gamma^{(\mu)}\partial_\mu\hat\Psi - \partial_\mu\hat{\bar\Psi}\gamma^{(\mu)}\hat\Psi)$, the energy density and the pressures are

$$
\hat\rho = -\hat T^{x_4}{}_{x_4} = {:}\Big(-\sum_{\mu \neq x_4}\hat K_\mu + m\hat S + U(\hat S)\Big){:},\qquad \hat p_\mu = \hat T^\mu{}_\mu = {:}\Big(\sum_{\nu \neq \mu}\hat K_\nu - m\hat S - U(\hat S)\Big){:}\quad(\mu \neq x_4),
$$

with the kinetic part ${:}(-\sum_{\mu \neq x_4}\hat K_\mu){:}$ and the potential part ${:}(m\hat S + U(\hat S)){:}$ of the energy density. For $\lambda = 0$ every component is a normal-ordered bilinear, and its one-particle expectation values follow the rule just derived. For $\lambda \neq 0$ the potential term is quartic in the field, and the expectation value of ${:}U(S){:}$ is not $U$ of the expectation value of ${:}S{:}$ in general.

**The case $\lambda \neq 0$ in a finite model.** The operator form of the on-shell identity $\sum_\mu\langle{:}K_\mu{:}\rangle = \langle{:}(m + U')S{:}\rangle$, and with it $\rho = mS + U$ and $p = SU' - U$, is verified by the Revision record in one finite model only (`Revision/theory/fock_quartic/`, one Python checker with sympy and an exact engine for the anticommutation rules, no Wolfram counterpart; 21 of 21 checks pass). The model is the positive Fock space of Section 10.20 ($\Psi^\dagger = \chi B$) for one good-sector plane-wave mode set with frozen coefficients: flat frame, volume 1, 16 modes and $2^{16}$ states, at rest ($k = 0$, symbolic $m$) and for $m = 3$, $k = (4, 0, 0, 0)$. There, for solutions of the interacting operator field equation, ${:}\sum_\mu K_\mu{:} = {:}(m + U'(S))S{:}$ holds as an exact operator identity on every state if and only if the potential $U = \frac{\lambda}{2}{:}SS{:}$ and the energy-momentum tensor are both Wick (normal) ordered, and at rest $\hat\rho = {:}mS + U{:}$ and $\hat p = {:}SU' - U{:}$ hold in the same sense (checks `trace_identity_operator_identity_wick` and `homogeneous_rho_p_operator_identities_wick`). Every other tested combination (four orderings of the potential, two definitions of the left-hand side, two right-hand sides; 30 combinations on the two mode sets) violates the identity by a nonzero one-body operator, sometimes plus a constant, that is linear in $\lambda$ (check `trace_identity_fails_for_every_other_combination`), and it fails already in expectation values: at rest on every state except the vacuum of the mode set (check `expectation_classes_M0`), and for $k = (4, 0, 0, 0)$ in a state with a single particle or a single antiparticle (check `expectation_values_M1`). An occupation state with $n$ quanta at rest has $\rho = mn + \frac{\lambda}{2}n(n - 1)$ and $p = \frac{\lambda}{2}n(n - 1)$, so $\langle{:}U(S){:}\rangle = \frac{\lambda}{2}n(n - 1)$ differs from $U(\langle{:}S{:}\rangle) = \frac{\lambda}{2}n^2$ (check `homogeneous_expectation_values_are_not_U_of_expectation`). For the field on a whole slice (many momenta), for the curved $x_8$ dependence with its boundary term at $z = \pi/2$ and for the extra-time sector the operator form stays OPEN, and symmetry and conservation of the quartic operator are not verified. Numerical expectation values of $\hat T$ for many-fermion states of the field on a whole slice are computed only in the Kohn-Sham approximation (Chapters 14 and 15); the finite model gives none for a physical many-fermion state.

| statement | status | where it is verified |
| --- | --- | --- |
| expectation-value rule $u^\dagger BMu$ (particle), $-v^\dagger BMv$ (antiparticle) | PROVED (above) and checked for a generic matrix and five recorded matrices | `python-field-theory.json`, check `good_sector_positive_fock_realisation`; `wolfram-field-theory.json`, check `Fock_space_good_sector_example` |
| $\hat T = {:}T[\hat\Psi, \hat\Psi^\dagger C]{:}$; normal ordering removes the vacuum value $-8E$ per momentum | definition; the vacuum value PROVED (Section 10.20) and checked in the exact examples | Revision theory document, section 12; `good_sector_positive_fock_realisation` |
| operator form of the on-shell identity for $\lambda \neq 0$ (at rest also $\hat\rho = {:}mS + U{:}$, $\hat p = {:}SU' - U{:}$) | PROVED (exact, sympy and an exact engine for the anticommutation rules) in the finite model of one good-sector mode set with frozen coefficients only, where, of the tested orderings, it holds if and only if $U$ and $\hat T$ are Wick ordered; OPEN for the field on a whole slice, the curved $x_8$ dependence and the extra-time sector; symmetry and conservation of the quartic operator not verified | `fock-quartic.json`, checks `trace_identity_operator_identity_wick`, `trace_identity_fails_for_every_other_combination` and `homogeneous_rho_p_operator_identities_wick` |

### 10.22 The commuting field dirac16complex00: an energy unbounded below

The second field of the theory, dirac16complex00 (written $\Phi$), has 16 COMMUTING complex components. The author defines it as a classical ("semi-classical") field, the analogue of Dirac's wave function of 1928, and the Revision record does not quantise it. Without anticommutators there is no Pauli principle, no filled sea and no normal ordering, and its classical energy is not positive.

**The energy density of one plane wave, line by line.** Take flat space, $U = 0$ and a positive-frequency plane wave $\Phi = c\,u\,e^{i(k\cdot x - Ex_4)}$ of the good sector, with $hu = Eu$, $E > 0$, a complex number $c$ and $k\cdot x = \sum_{a \neq 4}k_ax_a$. The energy density is $\rho = -T^{x_4}{}_{x_4} = -\sum_{\mu \neq x_4}K_\mu + mS$ (Chapter 9), with $K_a = \frac12(\bar\Phi\gamma^{(x_a)}\partial_a\Phi - \partial_a\bar\Phi\gamma^{(x_a)}\Phi)$, $S = \bar\Phi\Phi$ and $\bar\Phi = \Phi^\dagger C$.

- $\partial_a\Phi = ik_a\Phi$, and $\partial_a\bar\Phi = (\partial_a\Phi)^\dagger C = -ik_a\bar\Phi$, because the conjugate of $ik_a$ is $-ik_a$ (the derivative of the exponential, and the conjugate transpose of a number times a column).
- So $K_a = \frac12(ik_a + ik_a)\bar\Phi\gamma^{(x_a)}\Phi = ik_a|c|^2\,u^\dagger C\gamma^{(x_a)}u$, because in $\bar\Phi\gamma^{(x_a)}\Phi$ the exponentials $e^{-i(\ldots)}$ and $e^{+i(\ldots)}$ cancel and $c^*c = |c|^2$; in the same way $S = |c|^2u^\dagger Cu$.
- Therefore $\rho = |c|^2\,u^\dagger\big(mC - i\sum_ak_aC\gamma^{(x_a)}\big)u = |c|^2\,u^\dagger h'u$, with the matrix $h'$ of Section 10.12.
- From $Bh' = h$ and $BB = I_{16}$ follows $h' = Bh$ (multiply by $B$ from the left), and $hu = Eu$ gives $u^\dagger h'u = u^\dagger Bhu = E\,u^\dagger Bu$:

$$
\rho = E\,|c|^2\,u^\dagger Bu .
$$

The charge density is $\Phi^\dagger B\Phi = |c|^2u^\dagger Bu$. In the good sector $B$ commutes with $h$, and by Theorem 10.1 the eigenspace of $+E$ contains four orthonormal columns with $Bu = u$ and four with $Bu = -u$. The first four have $\rho = +E|c|^2$, the other four $\rho = -E|c|^2$, although all eight have the positive frequency $E$. Multiplying the wave by a large number $c$ makes its energy density as negative as one likes: **the classical energy of dirac16complex00 is unbounded below**, already for $U = 0$ in the good sector, and its charge density $\Phi^\dagger B\Phi$ is an indefinite form. For its charge, as for that of dirac16complex (Section 10.2), only the local conservation law is proved; the total over a slice is constant only if no charge flows through the boundary, which at $z = \pi/2$ is an ASSUMED no-flux condition that the record does not impose (`wolfram-field-theory.json`, check `charge_density_is_Krein_form_C`). Dirac's wave function of 1928 has the positive density $\psi^\dagger\psi$; dirac16complex00 does not. For the recorded momentum $m = 2$, $k = (1, 2, 0, 4)$, $E = 5$ and $|c| = 1$ the energy densities are $+5$ and $-5$ and the charge densities $+1$ and $-1$ (`python-scope.json`, check `commuting_field_energy_unbounded_below`). Quantising the fermion field with anticommutators and normal ordering makes the good-sector energy positive; for the classical commuting field there is no such mechanism, and no quantum statement is made for dirac16complex00 in this book.

### 10.23 Example: Notebook 10c builds the positive Fock space of one momentum

Notebook 10c builds the good-sector waves of the recorded momentum $m = 2$, $k = (1, 2, 0, 4)$, $E = 5$, the positive Fock space with the operators $b_s$ and $d_s$, and the field $\Psi$ with $\Psi^\dagger = \chi B$ (Section 10.20); it checks the canonical rule, computes the vacuum energy $-40$, the normal-ordered energies $+5$ and charges $\pm1$ of all 16 one-quantum states, checks the expectation-value rule of Section 10.21 for 100 random matrices and for the second recorded momentum $m = 3$, $k_1 = 4$, counts all 65536 states of one momentum, and computes the energy densities $\pm5$ of the commuting field (Section 10.22). It draws five figures and ends with the line ALL 14 CHECKS PASSED (notebook 10c).

<!-- NOTEBOOK 10c -->

### 10.26 Line-by-line walk-through of Notebook 10c

The notebook has 12 code cells, In [1] to In [12]; docstrings are left out of the quotations (they are printed in Section 10.25).

**In [1], the set-up cell.** Its first 249 lines are comments that repeat the run instructions of Section 10.24. The code is that of In [1] of Notebook 10a (Section 10.10), with the line `NOTEBOOK_ID = "10c"  # this notebook: chapter 10, example c`. It prints `Set-up of notebook 10c complete: repository folder found, helpers defined.`

**In [2], the gammas, B and the mode Hamiltonian.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer
import sys  # the screen output, sys.stdout

import numpy as np  # numbers, arrays and matrices


REPORT_CHECKS = {}  # report file -> {check name: verdict}; each file is read once


def record_says_pass(record):
    path, separator, check_name = record.partition(", check ")
    if not separator:  # a data entry of a record file that the notebook reads itself
        return True
    if path not in REPORT_CHECKS:
        checks = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
        REPORT_CHECKS[path] = {c["name"]: c["verdict"].upper() for c in checks}
    return REPORT_CHECKS[path].get(check_name) == "PASS"


def check_record(condition, name, record):
    if not record_says_pass(record):  # the cited check must exist and say PASS
        raise AssertionError("the cited record check is missing or not PASS: " + record)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
        check(condition, name, record=record)
    sys.stdout.write(buffer.getvalue())  # one single piece of output
```

The imports and the functions `record_says_pass` and `check_record` of In [2] of Notebook 10a (Section 10.10): `check_record` stops the notebook if the cited report check is missing or not PASS (the question that `record_says_pass` answers, reading each report file once into `REPORT_CHECKS`), and otherwise prints the PASS line and the line naming the reproduced record in one piece. This notebook needs no sympy.

```python
BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
    encoding="utf-8"))
gamma = {a: np.array(fixture["gamma"][a - 1], dtype=int) for a in range(1, 9)}
C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]  # the author's sigma16
B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4)
```

The four colours of the figures (as in Notebook 10a), the gammas of the record `Revision/algebra/gammas.json`, $C$ and $B$.

```python
def mode_hamiltonian(m, k):
    h = -1j * m * gamma[4]
    for a, k_a in k.items():
        h = h - k_a * (gamma[4] @ gamma[a])
    return h
```

The mode Hamiltonian $h = -im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_ak_a\gamma^{(x_a)}$ of Section 10.3, exactly as in In [5] of Notebook 10a; `k` is a dictionary of momenta.

```python
def orthonormal_columns(P):
    basis = []
    for column in P.T:
        v = column.astype(complex)
        for _ in range(2):
            for e in basis:
                v = v - (e.conj() @ v) * e
        length = np.sqrt((v.conj() @ v).real)
        if length > 1e-8:
            basis.append(v / length)
    return np.array(basis).T


say("gammas, C, B and the mode Hamiltonian are ready")
```

The Gram-Schmidt function of In [7] of Notebook 10b (Section 10.19): orthonormal columns that span the range of $P$. The last line prints the single output line of the cell.

**In [3], the waves of one good-sector momentum.**

```python
def good_sector_modes(m, k):
    h = mode_hamiltonian(m, k)
    E = np.sqrt(m ** 2 + sum(k_a ** 2 for k_a in k.values()))  # no extra times
    U_plus = orthonormal_columns((np.eye(16) + h / E) / 2)
    V_minus = orthonormal_columns((np.eye(16) - h / E) / 2)
    return h, E, np.hstack([U_plus, V_minus])
```

For a good-sector momentum (only the directions 1, 2, 3, 8 in `k`) the function computes $h$, the energy $E = \sqrt{m^2 + \sum_ak_a^2}$, and orthonormal bases of the ranges of the projectors $\frac12(I_{16} \pm h/E)$: the eigenvectors $u_1, \dots, u_8$ of $+E$ and $v_1, \dots, v_8$ of $-E$ (Section 10.20). It returns $h$, $E$ and the matrix $W$ with these 16 columns.

```python
h, E, W = good_sector_modes(2, {1: 1, 2: 2, 8: 4})
report("E for m = 2, k = (1, 2, 0, 4)", f"{E:.12f}")
hermitian = np.max(np.abs(h - h.conj().T)) < 1e-15
square_ok = np.max(np.abs(h @ h - 25 * np.eye(16))) < 1e-13
commutes = np.max(np.abs(B @ h - h @ B)) < 1e-15
```

The recorded momentum $m = 2$, $k_1 = 1$, $k_2 = 2$, $k_8 = 4$ gives $E = \sqrt{4 + 1 + 4 + 16} = 5$, printed as `5.000000000000`. The three truth values test that $h$ is Hermitian, that $hh = 25I_{16}$ and that $h$ commutes with $B$.

```python
eigen_ok = (np.max(np.abs(h @ W[:, :8] - E * W[:, :8])) < 1e-13
            and np.max(np.abs(h @ W[:, 8:] + E * W[:, 8:])) < 1e-13)
complete = (np.max(np.abs(W.conj().T @ W - np.eye(16))) < 1e-13
            and np.max(np.abs(W @ W.conj().T - np.eye(16))) < 1e-13)
say(f"h Hermitian: {hermitian}, h^2 = 25 I: {square_ok}, B h = h B: {commutes}")
say(f"8 + 8 eigenvectors: {eigen_ok}; orthonormal and complete: {complete}")
check(hermitian and square_ok and commutes and eigen_ok and complete
      and W.shape == (16, 16),
      "good sector: h Hermitian, h^2 = E^2, 8 + 8 orthonormal complete eigenvectors")
```

`W[:, :8]` are the first eight columns, the $u_s$, which must obey $hu = Eu$; `W[:, 8:]` are the last eight, the $v_s$, with $hv = -Ev$. `complete` tests $W^\dagger W = I_{16}$ (orthonormal) and $WW^\dagger = I_{16}$ (complete). The two printed lines show `True` for all five properties, and the check requires them and that $W$ has 16 rows and 16 columns.

**In [4], the positive Fock space and the field operators.**

```python
def sign_below(n, p):
    return -1 if bin(n & ((1 << p) - 1)).count("1") % 2 else 1


def annihilate(p, state):  # f_p
    result = {}
    for n, amplitude in state.items():
        if n >> p & 1:
            new = n ^ (1 << p)
            result[new] = result.get(new, 0) + sign_below(n, p) * amplitude
    return result


def create(p, state):  # f_p^*
    result = {}
    for n, amplitude in state.items():
        if not n >> p & 1:
            new = n | (1 << p)
            result[new] = result.get(new, 0) + sign_below(n, p) * amplitude
    return result
```

The Fock space of In [3] of Notebook 10b, explained line by line in Section 10.19: `sign_below` is the sign $(-1)^s$ ($s$ the number of occupied modes below $p$, written here in one line), `annihilate` is $f_p$ (it empties mode $p$ where it is occupied) and `create` is $f_p^*$ (it fills mode $p$ where it is empty), both with that sign.

```python
def add(*terms):
    result = {}
    for coefficient, state in terms:
        for n, amplitude in state.items():
            result[n] = result.get(n, 0) + coefficient * amplitude
    return result


def inner(left, right):
    return sum(np.conj(a) * right.get(n, 0) for n, a in left.items())


def largest(state):
    return max((abs(a) for a in state.values()), default=0.0)
```

The same three helpers as in Notebook 10b: combinations of states, the positive inner product, and the largest size of an amplitude.

```python
def F(p, state):  # F_p: b (p < 8) or d^* (p >= 8)
    return annihilate(p, state) if p < 8 else create(p, state)


def F_star(p, state):  # the Hilbert adjoint of F_p
    return create(p, state) if p < 8 else annihilate(p, state)
```

The 16 modes are used as follows: modes 0 to 7 are the particles, $b_s = f_{s-1}$; modes 8 to 15 the antiparticles, $d_s = f_{s+7}$. In the field $\Psi = \sum_s(u_sb_s + v_sd_s^*)$ the particle modes enter with $b$ and the antiparticle modes with $d^*$, so the field is $\Psi_A = \sum_pW_{Ap}F_p$ with $F_p = f_p$ for $p < 8$ and $F_p = f_p^*$ for $p \geq 8$. `F` is $F_p$, and `F_star` its Hilbert adjoint.

```python
def bilinear(N, state, modes):
    M = modes.conj().T @ N @ modes
    terms = []
    for q in range(16):
        lowered = F(q, state)
        if lowered:
            terms += [(M[p, q], F_star(p, lowered)) for p in range(16)
                      if abs(M[p, q]) > 1e-15]
    return add(*terms)
```

`bilinear(N, state, modes)` applies the operator $\chi N\Psi = \sum_{A,C}\chi_AN_{AC}\Psi_C$ to a state. Inserting $\Psi_C = \sum_qW_{Cq}F_q$ and $\chi_A = \sum_pW^*_{Ap}F_p^*$ gives $\sum_{p,q}(W^\dagger NW)_{pq}F_p^*F_q$, which needs only the $16 \times 16$ matrix `M` $= W^\dagger NW$. For each $q$ the function applies $F_q$ once (`lowered`); an empty dictionary counts as false, so a zero result is skipped. Then it adds $M_{pq}F_p^*$ applied to it for every $p$ with a nonzero entry; `terms += [...]` appends the new pairs to the list.

```python
def psi(A, state, modes):  # Psi_A = sum_p W_Ap F_p
    return add(*[(modes[A - 1, p], F(p, state)) for p in range(16)])


def chi(A, state, modes):  # chi_A = sum_p conj(W_Ap) F_p^*
    return add(*[(np.conj(modes[A - 1, p]), F_star(p, state)) for p in range(16)])


def psi_dagger(A, state, modes):  # the canonical conjugate: sum_C chi_C B_CA
    return add(*[(B[C_ - 1, A - 1], chi(C_, state, modes)) for C_ in range(1, 17)
                 if B[C_ - 1, A - 1] != 0])
```

The field component $\Psi_A$, its Hilbert adjoint $\chi_A$ and the canonical conjugate $\Psi^\dagger_A = \sum_C\chi_CB_{CA}$, as the comments say.

```python
VACUUM = {0: 1.0}
rng = np.random.default_rng(12345)
phi = {int(n): complex(rng.normal(), rng.normal())
       for n in rng.integers(0, 2 ** 16, size=5)}  # a random state
```

The vacuum (every mode empty: no particle and, in this realisation, no antiparticle), a random generator with the fixed seed 12345, and a random state of 5 patterns (not normalised; the anticommutator test does not need it).

```python
worst_delta, worst_B = 0.0, 0.0
for A in range(1, 17):
    for C_ in range(1, 17):
        with_chi = add((1, psi(A, chi(C_, phi, W), W)), (1, chi(C_, psi(A, phi, W), W)))
        expected = phi if A == C_ else {}
        worst_delta = max(worst_delta, largest(add((1, with_chi), (-1, expected))))
        with_dagger = add((1, psi(A, psi_dagger(C_, phi, W), W)),
                          (1, psi_dagger(C_, psi(A, phi, W), W)))
        worst_B = max(worst_B, largest(add((1, with_dagger), (-B[A - 1, C_ - 1], phi))))
report("largest violation of {Psi_A, chi_C} = delta_AC", f"{worst_delta:.1e}")
report("largest violation of {Psi_A, Psi^dagger_C} = B_AC", f"{worst_B:.1e}")
check(worst_delta < 1e-12 and worst_B < 1e-12,
      "positive Fock space: {Psi, chi} = I and {Psi, Psi^dagger} = B")
```

For all 256 pairs $(A, C)$ the loops compute $\{\Psi_A, \chi_C\}\phi$, which must be $\delta_{AC}\phi$ (completeness, Section 10.20), and $\{\Psi_A, \Psi^\dagger_C\}\phi$, which must be $B_{AC}\phi$. Both largest deviations are printed as `6.3e-16`, rounding only, and the check prints its PASS line: on this positive Fock space the canonical rule holds.

**In [5], vacuum energy, normal ordering, energies and charges.**

```python
def one_quantum_values(N, modes):
    vacuum_value = inner(VACUUM, bilinear(N, VACUUM, modes)).real
    values = []
    for p in range(16):  # p < 8: b^*|0>, p >= 8: d^*|0>
        state = create(p, VACUUM)
        values.append(inner(state, bilinear(N, state, modes)).real - vacuum_value)
    return np.array(values), vacuum_value
```

`one_quantum_values(N, modes)` computes the vacuum value $\langle 0|\chi N\Psi|0\rangle$ and, for each of the 16 one-quantum states (filling mode $p$ of the vacuum gives $b^*_{p+1}|0\rangle$ for $p < 8$ and $d^*_{p-7}|0\rangle$ for $p \geq 8$), the normal-ordered value: the value in that state minus the vacuum value (Section 10.20).

```python
energies, vacuum_energy = one_quantum_values(h, W)
charges, vacuum_charge = one_quantum_values(np.eye(16), W)
report("vacuum energy (the filled Dirac sea)", f"{vacuum_energy:.10f}")
report("vacuum charge before normal ordering", f"{vacuum_charge:.10f}")
say(f"normal-ordered energies of the 16 quanta: {np.round(energies, 10).tolist()}")
say(f"normal-ordered charges of the 16 quanta:  {np.round(charges, 10).tolist()}")
```

The energy is $\chi h\Psi$ ($N = h$) and the charge $\chi\Psi$ ($N = I_{16}$). The printed lines show the vacuum energy $-40.0000000000 = -8E$, the vacuum charge $8$ before normal ordering, the 16 normal-ordered energies, all $5.0$, and the 16 charges, eight times $1.0$ and eight times $-1.0$: exactly the results of Section 10.20.

```python
expected_charges = np.array([1] * 8 + [-1] * 8)  # 8 particles, 8 antiparticles
check_record(abs(vacuum_energy + 40) < 1e-12 and np.max(np.abs(energies - 5)) < 1e-12
             and np.max(np.abs(charges - expected_charges)) < 1e-12,
             "m = 2, k = (1, 2, 0, 4): vacuum -40, every quantum +5, charges +1, -1",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "good_sector_positive_fock_realisation")
```

The check requires these numbers and reproduces the record check `good_sector_positive_fock_realisation`.

**In [6], the expectation-value rule.**

```python
particle_points, antiparticle_points = [], []
for _ in range(100):
    M = rng.normal(size=(16, 16)) + 1j * rng.normal(size=(16, 16))
    values, _ = one_quantum_values(B @ M, W)  # real parts of <:chi B M Psi:>
    particle_points.append((values[0], (W[:, 0].conj() @ B @ M @ W[:, 0]).real))
    antiparticle_points.append((values[8], -(W[:, 8].conj() @ B @ M @ W[:, 8]).real))
particle_points = np.array(particle_points)
antiparticle_points = np.array(antiparticle_points)
```

For 100 random complex matrices $M$ the classical bilinear $\Psi^\dagger M\Psi$ becomes the operator $\chi BM\Psi$, and `one_quantum_values(B @ M, W)` gives its normal-ordered values (real parts) in the 16 one-quantum states. The value in the first particle state ($p = 0$) is paired with the formula $u_1^\dagger BMu_1$, and the value in the first antiparticle state ($p = 8$) with $-v_1^\dagger BMv_1$ (Section 10.21).

```python
worst = max(np.max(np.abs(particle_points[:, 0] - particle_points[:, 1])),
            np.max(np.abs(antiparticle_points[:, 0] - antiparticle_points[:, 1])))
report("largest deviation from the rule (100 random M)", f"{worst:.1e}")
check(worst < 1e-12,
      "rule: u^dagger B M u for a particle, -v^dagger B M v for an antiparticle")
```

The largest deviation is printed as `1.8e-15`, rounding only, and the check prints its PASS line.

```python
fig, ax = plt.subplots(figsize=(6.0, 5.0))
ax.plot(particle_points[:, 1], particle_points[:, 0], "o", color=BLUE, markersize=5,
        label="particle: against $u^\\dagger B M u$")
ax.plot(antiparticle_points[:, 1], antiparticle_points[:, 0], "s", color=ORANGE,
        markersize=5, fillstyle="none",
        label="antiparticle: against $-v^\\dagger B M v$")
low = min(particle_points.min(), antiparticle_points.min()) - 1
high = max(particle_points.max(), antiparticle_points.max()) + 1
ax.plot([low, high], [low, high], color=GREY, linewidth=1)
ax.set_xlabel("value of the formula (real part)")
ax.set_ylabel("normal-ordered value on the Fock space (real part)")
ax.set_title("The expectation-value rule in the good sector")
ax.legend(loc="upper left", fontsize=8)
save_figure(fig, "expectation_rule",
...)
```

The Fock-space values (vertical) are drawn against the formulas (horizontal): blue dots for particles, open orange squares for antiparticles, and the grey diagonal. Figure 1 of Notebook 10c shows all 200 points on the diagonal: the expectation-value rule of the Revision record holds in the good sector.

**In [7], the second recorded example.**

```python
h2, E2, W2 = good_sector_modes(3, {1: 4})
energies2, vacuum2 = one_quantum_values(h2, W2)
charges2, _ = one_quantum_values(np.eye(16), W2)
dense = np.array([[(3 * A + 5 * C_) % 7 - 3 for C_ in range(1, 17)]
                  for A in range(1, 17)])
tests = {"C": C, "-i C gamma4": -1j * C @ gamma[4], "-i C gamma1": -1j * C @ gamma[1],
         "C gamma2 gamma3": C @ gamma[2] @ gamma[3], "dense": dense}
```

The momentum of the Wolfram record, $m = 3$ and $k_1 = 4$ ($E = \sqrt{9 + 16} = 5$), with its energies and charges. The five test matrices are those named by the record: $C$, $-iC\gamma^{(x_4)}$, $-iC\gamma^{(x_1)}$, $C\gamma^{(x_2)}\gamma^{(x_3)}$, and a dense matrix of whole numbers, here the notebook's own: entry $(A, C)$ is the remainder of $3A + 5C$ after division by 7 (`%` is the remainder), minus 3.

```python
rule_ok = True
for label, M in tests.items():
    values, _ = one_quantum_values(B @ M, W2)
    expected_particle = (W2[:, 0].conj() @ B @ M @ W2[:, 0]).real
    expected_anti = -(W2[:, 8].conj() @ B @ M @ W2[:, 8]).real
    rule_ok = rule_ok and abs(values[0] - expected_particle) < 1e-12 \
        and abs(values[8] - expected_anti) < 1e-12
    say(f"M = {label:16s} particle {values[0]:+.6f}, antiparticle {values[8]:+.6f}")
report("E and the vacuum energy for m = 3, k1 = 4", f"{E2:.6f} and {vacuum2:.6f}")
```

For each test matrix the loop compares the normal-ordered values with the rule (a backslash at the end of a line continues the statement on the next line) and prints one line. The printed values are $+0.6$ for $M = C$ in both states, $+1$ and $-1$ for $M = -iC\gamma^{(x_4)} = B$ (the charges, as Section 10.21 predicts), $0.8$ for $M = -iC\gamma^{(x_1)}$, 0 for $M = C\gamma^{(x_2)}\gamma^{(x_3)}$, and $-0.48$ and $-1.92$ for the dense matrix. The RESULT line shows $E = 5$ and the vacuum energy $-40$.

```python
check_record(abs(vacuum2 + 8 * E2) < 1e-12 and np.max(np.abs(energies2 - E2)) < 1e-12
             and np.max(np.abs(charges2 - np.array([1] * 8 + [-1] * 8))) < 1e-12
             and rule_ok,
             "m = 3, k1 = 4: vacuum -8E, energies +E, charges +-1, the rule holds",
             record="Revision/theory/reports/wolfram-field-theory.json, check "
                    "Fock_space_good_sector_example")
```

The check reproduces the Wolfram record check `Fock_space_good_sector_example`: vacuum $-8E$, every quantum $+E$, charges $\pm1$, and the rule for all five matrices.

**In [8], all 65536 states of one momentum.**

```python
from math import comb  # comb(8, j): the number of ways to choose j of 8 things

eigen_ok = True
for n in rng.integers(0, 2 ** 16, size=200):
    n = int(n)
    n_b = bin(n & 0xFF).count("1")  # occupied particle modes (digits 0 to 7)
    n_d = bin(n >> 8).count("1")  # occupied antiparticle modes (digits 8 to 15)
    state = {n: 1.0}
```

`comb(8, j)` is the binomial coefficient $\binom{8}{j}$. For 200 random patterns: `0xFF` is the number 255 written in base 16, whose eight lowest binary digits are 1, so `n & 0xFF` keeps the digits 0 to 7 of $n$ and their count is $N_b$; shifting $n$ to the right by 8 binary places keeps the digits 8 to 15, whose count is $N_d$. `state` is the pattern itself with amplitude 1.

```python
    energy_state = bilinear(h, state, W)
    charge_state = bilinear(np.eye(16), state, W)
    eigen_ok = eigen_ok and largest(add(
        (1, energy_state), (-(E * (n_b + n_d) - 8 * E), state))) < 1e-12
    eigen_ok = eigen_ok and largest(add(
        (1, charge_state), (-(n_b - n_d + 8), state))) < 1e-12
check(eigen_ok, "every pattern has energy E (N_b + N_d) - 8E and charge N_b - N_d + 8")
```

The energy and the charge operators are applied to the pattern, and the results are compared with the pattern times $E(N_b + N_d) - 8E$ and times $N_b - N_d + 8$ (the values before normal ordering, Section 10.20). The check confirms that every one of the 200 patterns is an eigenstate with these eigenvalues.

```python
counts = np.zeros((17, 17), dtype=int)  # rows: N_b + N_d, columns: N_b - N_d + 8
for n in range(2 ** 16):
    n_b, n_d = bin(n & 0xFF).count("1"), bin(n >> 8).count("1")
    counts[n_b + n_d, n_b - n_d + 8] += 1
formula = np.zeros((17, 17), dtype=int)
for n_b in range(9):
    for n_d in range(9):
        formula[n_b + n_d, n_b - n_d + 8] += comb(8, n_b) * comb(8, n_d)
```

`counts` is a table of whole numbers: row $N_b + N_d$ (0 to 16 quanta) and column $N_b - N_d + 8$ (the charge from $-8$ to 8, shifted by 8 so that the column numbers start at 0). The first loop goes through all 65536 patterns and adds 1 in the square of each (`+= 1` adds to the stored value). `formula` holds the counts $\binom{8}{N_b}\binom{8}{N_d}$ of Section 10.20.

```python
report("number of patterns", int(counts.sum()))
report("patterns with energy 0 (the vacuum only)", int(counts[0].sum()))
report("patterns with one quantum (energy 5)", int(counts[1].sum()))
check(np.array_equal(counts, formula) and counts.sum() == 2 ** 16,
      "the 65536 patterns are counted by binomial(8, N_b) binomial(8, N_d)")
```

The printed numbers are 65536 patterns in all, 1 with the energy 0 (the vacuum) and 16 with one quantum. The check confirms that the direct count equals the formula in every square.

**In [9], the Dirac sea and the states of one momentum.**

```python
k_values = np.linspace(0.0, 5.0, 201)  # the size of the momentum
branch = np.sqrt(2.0 ** 2 + k_values ** 2)  # E for m = 2
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
ax = axes[0]
ax.plot(k_values, branch, color=BLUE, linewidth=2, label="$+E$: particle levels")
ax.plot(k_values, -branch, color=ORANGE, linewidth=2,
        label="$-E$: levels filled in the vacuum")
ax.fill_between(k_values, -branch, -6.5, color=ORANGE, alpha=0.2,
                label="the filled Dirac sea")
ax.set_xlabel("size of the momentum $|k|$ (with $m = 2$)")
ax.set_ylabel("eigenvalue of $h$ (classical wave energy)")
ax.set_ylim(-6.5, 6.5)
ax.set_title("classical energies of the waves")
ax.legend(loc="center right", fontsize=8)
```

The left panel draws the classical wave energies $\pm E = \pm\sqrt{4 + |k|^2}$ for $m = 2$ against the size $|k|$ of the momentum, from 0 to 5. `fill_between` shades, with 20 percent opacity (`alpha=0.2`), the region between the lower curve and the bottom of the picture: the filled sea of negative levels.

```python
ax = axes[1]
ax.plot(k_values, branch, color=BLUE, linewidth=2, label="particle $b^*|0\\rangle$")
ax.plot(k_values, branch, "--", color=ORANGE, linewidth=2,
        label="antiparticle $d^*|0\\rangle$ (same curve)")
ax.axhline(0.0, color=GREY, linewidth=1)
ax.set_xlabel("size of the momentum $|k|$ (with $m = 2$)")
ax.set_ylabel("normal-ordered energy of one quantum")
ax.set_ylim(-6.5, 6.5)
ax.set_title("quantum: both quanta have energy $+E$")
ax.legend(loc="lower right", fontsize=8)
save_figure(fig, "dirac_sea",
...)
```

The right panel draws the normal-ordered energies of a particle and of an antiparticle, both $+E$, so the dashed orange curve lies on the blue one. Figure 2 of Notebook 10c shows on the left two classical branches, one of them negative and filled, and on the right only positive energies: quantisation with normal ordering turns the negative classical branch into antiparticles of positive energy.

```python
from matplotlib.colors import LinearSegmentedColormap  # colour scales

fig, ax = plt.subplots(figsize=(7.0, 5.0))
shown = np.where(counts > 0, np.log10(np.maximum(counts, 1)), np.nan)  # NaN: empty
light_to_dark = LinearSegmentedColormap.from_list(
    "light_to_dark_blue", ["#cde2fb", "#2a78d6", "#0d366b"])  # 1 state is visible
image = ax.imshow(shown, origin="lower", cmap=light_to_dark, aspect="auto",
                  extent=(-8.5, 8.5, -0.5, 16.5))
```

The second figure is a heat map of the table `counts`. The colour shows the base-10 logarithm of the count (`np.log10`), so that 1 and 4900 states can both be seen; `np.maximum(counts, 1)` avoids the logarithm of 0, and `np.where` puts NaN ("not a number", drawn as white) into the empty squares. The colour scale runs from light blue (one state) to dark blue. `origin="lower"` puts row 0 at the bottom, and `extent` places the squares at the charges $-8, \dots, 8$ horizontally and the numbers of quanta $0, \dots, 16$ vertically.

```python
ax.annotate("vacuum", (0, 0), xytext=(1.5, 0.3), fontsize=8,
            arrowprops={"arrowstyle": "->", "color": GREY})
ax.annotate("4900 states", (0, 8), xytext=(3.0, 8.6), fontsize=8,
            arrowprops={"arrowstyle": "->", "color": GREY})
ax.set_xlabel("normal-ordered charge $N_b - N_d$")
ax.set_ylabel("number of quanta $N_b + N_d$ (energy $= 5(N_b + N_d)$)")
ax.set_title("The 65536 states of one momentum, $E = 5$")
ax.grid(False)
fig.colorbar(image, ax=ax, label="$\\log_{10}$ of the number of states")
save_figure(fig, "fock_spectrum",
...)
```

Two arrows label the vacuum and the largest group, 4900 states with 8 quanta and charge 0. Figure 3 of Notebook 10c shows a diamond of filled squares: one state at the bottom (the vacuum), 16 in the row above, the largest numbers in the middle, and nothing below the vacuum: no state has negative energy.

**In [10], the commuting field dirac16complex00.**

```python
energy_projector = (np.eye(16) + h / E) / 2  # onto the eigenspace of +E
plus_part = orthonormal_columns(energy_projector @ (np.eye(16) + B) / 2)
minus_part = orthonormal_columns(energy_projector @ (np.eye(16) - B) / 2)
k_sample = {1: 1, 2: 2, 8: 4}  # the momenta of the sample, m = 2
```

In the good sector $B$ commutes with $h$, so the product of the projector onto the eigenspace of $+E$ with the projector $\frac12(I_{16} \pm B)$ projects onto the columns that have both $hu = Eu$ and $Bu = \pm u$. Their orthonormal bases are `plus_part` and `minus_part`.

```python
def energy_density(u, m=2.0, k=k_sample):
    Phibar = u.conj() @ C  # the row Phi^dagger C at x = 0
    S = (Phibar @ u).real
    K = {a: (0.5 * (Phibar @ gamma[a] @ (1j * k_a * u))
             - 0.5 * ((-1j * k_a) * Phibar) @ gamma[a] @ u) for a, k_a in k.items()}
    return (-sum(K.values()) + m * S).real
```

`energy_density(u)` computes $\rho = -\sum_aK_a + mS$ for the wave $\Phi = u\,e^{i(k\cdot x - 5x_4)}$ with $|c| = 1$, at the point $x = 0$ and the time 0, directly from the definitions of Section 10.22 and not from the shortcut $\rho = E\,u^\dagger Bu$: `Phibar` is the row $\bar\Phi = \Phi^\dagger C$; $\partial_a\Phi = ik_a\Phi$ and $\partial_a\bar\Phi = -ik_a\bar\Phi$ are written as `1j * k_a * u` and `(-1j * k_a) * Phibar`, and `K` holds $K_a = \frac12(\bar\Phi\gamma^{(x_a)}\partial_a\Phi - \partial_a\bar\Phi\gamma^{(x_a)}\Phi)$ for the three directions of the momentum.

```python
densities_plus = [energy_density(plus_part[:, j]) for j in range(plus_part.shape[1])]
densities_minus = [energy_density(minus_part[:, j])
                   for j in range(minus_part.shape[1])]
charge_plus = [(u.conj() @ B @ u).real for u in plus_part.T]
charge_minus = [(u.conj() @ B @ u).real for u in minus_part.T]
say(f"dimensions: {plus_part.shape[1]} with B u = +u, {minus_part.shape[1]} with "
    f"B u = -u")
say(f"energy densities: {np.round(densities_plus, 10).tolist()} and "
    f"{np.round(densities_minus, 10).tolist()}")
say(f"charge densities: {np.round(charge_plus, 10).tolist()} and "
    f"{np.round(charge_minus, 10).tolist()}")
```

The energy densities and the charge densities $u^\dagger Bu$ of the columns of both bases. The printed lines show 4 columns of each kind, the energy densities $5.0$ (four times) and $-5.0$ (four times), and the charge densities $1.0$ and $-1.0$.

```python
check_record(plus_part.shape[1] == 4 and minus_part.shape[1] == 4
             and np.max(np.abs(np.array(densities_plus) - 5)) < 1e-12
             and np.max(np.abs(np.array(densities_minus) + 5)) < 1e-12
             and np.max(np.abs(np.array(charge_plus) - 1)) < 1e-12
             and np.max(np.abs(np.array(charge_minus) + 1)) < 1e-12,
             "commuting field: positive-frequency waves with energy +5 and -5",
             record="Revision/theory/reports/python-scope.json, check "
                    "commuting_field_energy_unbounded_below")
```

The check reproduces the record check `commuting_field_energy_unbounded_below`: waves of the same positive frequency with the energy densities $+5$ and $-5$.

**In [11], the two fields compared.**

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0), sharey=True)
for ax in axes:
    ax.set_axisbelow(True)  # draw the grid lines behind the bars
classical = densities_plus + densities_minus
axes[0].bar(range(1, 9), classical,
            color=[BLUE] * len(densities_plus) + [ORANGE] * len(densities_minus))
axes[0].axhline(0.0, color=GREY, linewidth=1)
axes[0].set_xticks(range(1, 9))
axes[0].set_xlabel("positive-frequency wave (4 with $Bu = u$, 4 with $Bu = -u$)")
axes[0].set_ylabel("energy (units of $m$)")
axes[0].set_title("classical commuting field: $\\rho = \\pm 5$")
```

Two panels with a common vertical axis (`sharey=True`). The `+` of two Python lists joins them, so `classical` is the list of the eight energy densities; the left panel draws them as bars, blue for $Bu = u$ and orange for $Bu = -u$.

```python
axes[1].bar(range(1, 17), energies, color=[BLUE] * 8 + [GREEN] * 8)
axes[1].axhline(0.0, color=GREY, linewidth=1)
axes[1].set_xticks(range(1, 17, 3))
axes[1].set_xlabel("quantum (1 to 8 particles, 9 to 16 antiparticles)")
axes[1].set_title("quantised fermion: every quantum $+5$")
save_figure(fig, "commuting_energy",
...)
```

The right panel draws the normal-ordered energies of the 16 one-quantum states of In [5], blue for particles and green for antiparticles. Figure 4 of Notebook 10c shows four bars of $+5$ and four of $-5$ on the left, and sixteen bars of $+5$ on the right: the same momentum, a positive energy for every quantum of the quantised fermion field, energies of both signs for the classical commuting field.

```python
coefficients = rng.normal(size=(4000, 8)) + 1j * rng.normal(size=(4000, 8))
eigenspace = np.hstack([plus_part, minus_part])  # 8 orthonormal columns
samples = coefficients @ eigenspace.T  # each row: a random column u in the space
samples = samples / np.linalg.norm(samples, axis=1, keepdims=True)
rho = E * np.einsum("ni,ij,nj->n", samples.conj(), B, samples).real
```

4000 random complex combinations of the 8 orthonormal columns of the eigenspace of $+E$: row $n$ of `samples` is $\sum_jc_{nj}e_j$ with the random coefficients $c_{nj}$, normalised to length 1. For each, `rho` is the energy density $E\,u^\dagger Bu$ of Section 10.22 (the sum $u^\dagger Bu$ is formed by `np.einsum`, as in In [6] of Notebook 10b).

```python
report("smallest and largest energy density of the 4000 waves",
       f"{rho.min():.3f} and {rho.max():.3f}")
check(rho.min() < -2 and rho.max() > 2 and np.all(np.abs(rho) <= 5 + 1e-12),
      "random positive-frequency commuting waves have energy densities of both signs")
```

The printed range is from `-4.364` to `4.333`, inside $[-5, 5]$, and the check requires values below $-2$ and above $2$.

```python
fig, ax = plt.subplots()
ax.set_axisbelow(True)
ax.hist(rho, bins=40, range=(-5, 5), color=BLUE, edgecolor="white")
ax.axvline(0.0, color=GREY, linewidth=1)
ax.set_xlabel("energy density $\\rho = E\\,u^\\dagger B u$ of a commuting wave "
              "($|c| = 1$)")
ax.set_ylabel("number of waves (of 4000)")
ax.set_title("dirac16complex00: positive frequency, energy of both signs")
save_figure(fig, "energy_density_spread",
...)
```

A histogram with 40 bins between $-5$ and 5. Figure 5 of Notebook 10c shows a distribution symmetric about 0: about half of the positive-frequency waves of the commuting field have a negative energy density, and multiplying a wave by a number $c$ multiplies its energy by $|c|^2$, so the classical energy is unbounded below.

**In [12], the last check.**

```python
for name in ("10c_1_expectation_rule.png", "10c_2_dirac_sea.png",
             "10c_3_fock_spectrum.png", "10c_4_commuting_energy.png",
             "10c_5_energy_density_spread.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The five figure files exist, and the last line prints ALL 14 CHECKS PASSED (notebook 10c): the five figure checks and the 9 checks of the cells before (one each in In [3] to In [7], In [10] and In [11], and two in In [8]).

### 10.27 The curved good sector: symmetric only up to a boundary term

The positive Fock space of Section 10.20 was built for one plane wave with frozen coefficients. In the author's curved metric the waves of the good sector depend on the hidden coordinate $x_8$, with $z = 6Hx_8$ between the **tip** $z = 0$ and the **patch end** $z = \pi/2$, where $g_{88} = \cot^2z$ and the volume factor $\sqrt{|g|} = \cos z$ vanish. Is the evolution there still Hermitian, and is the Krein charge still conserved?

**The field equation for waves in $x_4$ and $x_8$.** In the author's metric the field equation of dirac16complex with $U = 0$ is (Chapter 7, record `Revision/theory/field-theory.json`)

$$
e^{-a_4}\sin^{-1/6}z\sum_{i=1}^{3}\gamma^{(x_i)}\partial_i\Psi + \gamma^{(x_4)}\partial_4\Psi + e^{a_4}\sin^{-1/6}z\sum_{t=5}^{7}\gamma^{(x_t)}\partial_t\Psi + \tan z\,\gamma^{(x_8)}\partial_8\Psi + 3H\gamma^{(x_8)}\Psi = m\Psi .
$$

Each derivative is divided by the scale factor of its direction ($1/f_8 = 1/\cot z = \tan z$), and $3H\gamma^{(x_8)}$ is the term $\gamma^\mu\Omega_\mu$ of the canonical spin connection (Chapter 6). For a wave of the good sector that depends only on $x_4$ and $x_8$ the first and the third sums vanish:

$$
\gamma^{(x_4)}\partial_4\Psi + \tan z\,\gamma^{(x_8)}\partial_8\Psi + 3H\gamma^{(x_8)}\Psi = m\Psi .
$$

Multiply from the left by $\gamma^{(x_4)}$, use $\gamma^{(x_4)}\gamma^{(x_4)} = -I_{16}$, solve for $\partial_4\Psi$ (as in Section 10.3) and multiply by $i$:

$$
i\,\partial_4\Psi = h\Psi,\qquad h = A + D\,\partial_8,
$$

with the matrices

$$
A = -im\gamma^{(x_4)} + 3iH\gamma^{(x_4)}\gamma^{(x_8)},\qquad D = \tan z\,M_8,\qquad M_8 = i\gamma^{(x_4)}\gamma^{(x_8)} .
$$

**Four matrix facts.** With $(\gamma^{(x_4)})^T = -\gamma^{(x_4)}$, $(\gamma^{(x_8)})^T = \gamma^{(x_8)}$ and $\gamma^{(x_8)}\gamma^{(x_4)} = -\gamma^{(x_4)}\gamma^{(x_8)}$:

(D1) $M_8^\dagger = -i(\gamma^{(x_8)})^T(\gamma^{(x_4)})^T = -i\gamma^{(x_8)}(-\gamma^{(x_4)}) = i\gamma^{(x_8)}\gamma^{(x_4)} = -i\gamma^{(x_4)}\gamma^{(x_8)} = -M_8$: $M_8$ is anti-Hermitian, and so is $D$ ($\tan z$ is real).

(D2) $\cos z\,D = \cos z\tan z\,M_8 = \sin z\,M_8$.

(D3) $A^\dagger = im(\gamma^{(x_4)})^T - 3iH(\gamma^{(x_8)})^T(\gamma^{(x_4)})^T = -im\gamma^{(x_4)} + 3iH\gamma^{(x_8)}\gamma^{(x_4)} = -im\gamma^{(x_4)} - 3iH\gamma^{(x_4)}\gamma^{(x_8)}$, so $A - A^\dagger = 6iH\gamma^{(x_4)}\gamma^{(x_8)} = 6HM_8$. Since $\partial_8\sin z = 6H\cos z$ (chain rule, $z = 6Hx_8$), this is $\cos z\,(A - A^\dagger) = (\partial_8\sin z)\,M_8$.

(D4) $B$ commutes with $\gamma^{(x_4)}$ and $\gamma^{(x_8)}$ (Section 10.2), hence with $A$, $A^\dagger$, $D$ and $M_8$.

**Symmetric up to a boundary term, line by line.** Write $u'$ for $\partial_8u$, for two wave functions $u(x_8)$ and $v(x_8)$. Then

$$
u^\dagger(hv) - (hu)^\dagger v = u^\dagger Av + u^\dagger Dv' - u^\dagger A^\dagger v - u'^\dagger D^\dagger v = u^\dagger(A - A^\dagger)v + u^\dagger Dv' + u'^\dagger Dv .
$$

The first step inserts $h = A + D\partial_8$ and uses $(Xw)^\dagger = w^\dagger X^\dagger$; the second collects the $A$ terms and uses $D^\dagger = -D$ (D1). Multiply by $\cos z$ and write $G = \cos z\,D = \sin z\,M_8$ (D2):

$$
\cos z\,\big[u^\dagger(hv) - (hu)^\dagger v\big] = \cos z\,u^\dagger(A - A^\dagger)v + u^\dagger Gv' + u'^\dagger Gv = (\partial_8\sin z)\,u^\dagger M_8v + \partial_8\big(u^\dagger Gv\big) - u^\dagger(\partial_8G)v .
$$

The second step uses (D3) for the first term and the product rule $\partial_8(u^\dagger Gv) = u'^\dagger Gv + u^\dagger G'v + u^\dagger Gv'$ for the other two. Since $\partial_8G = (\partial_8\sin z)M_8$, the first and the last terms cancel:

$$
\cos z\,\big[u^\dagger(hv) - (hu)^\dagger v\big] = \partial_8\big(\sin z\;u^\dagger M_8v\big) .
$$

The left side, integrated over the hidden direction with the volume $\cos z\,dx_8$, is the difference between $\int\cos z\,u^\dagger(hv)\,dx_8$ and $\int\cos z\,(hu)^\dagger v\,dx_8$; the right side is a **boundary term**: its integral over $0 < z < \pi/2$ is the bracket $\sin z\,u^\dagger M_8v$ at $z = \pi/2$ minus its value at $z = 0$. At the tip $\sin z = 0$, so for wave functions that stay finite there the bracket vanishes. At the patch end $\sin z = 1$, and the bracket $u^\dagger M_8v$, the **flux** through $z = \pi/2$, does not vanish in general. Example: $\gamma^{(x_4)}\gamma^{(x_8)}$ is real and symmetric ($(\gamma^{(x_4)}\gamma^{(x_8)})^T = \gamma^{(x_8)}(-\gamma^{(x_4)}) = \gamma^{(x_4)}\gamma^{(x_8)}$) and squares to $-\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_8)} = I_{16}$, so it has the eigenvalue $+1$; for a column with $\gamma^{(x_4)}\gamma^{(x_8)}u = u$ and $u^\dagger u = 2$ the flux is $u^\dagger M_8u = i\,u^\dagger u = 2i$. The patch end is not infinitely far away: its proper distance from a point $z_0$ is $\int\sqrt{g_{88}}\,dx_8 = \frac{1}{6H}\int_{z_0}^{\pi/2}\cot z\,dz = -\frac{1}{6H}\ln\sin z_0$, a finite number.

**The Krein version.** Because $B$ commutes with every matrix in $h$ (D4) and is constant, $B(hu) = h(Bu)$, so $(hu)^\dagger Bv = (Bhu)^\dagger v = (h(Bu))^\dagger v$, while $u^\dagger B(hv) = (Bu)^\dagger(hv)$. The derivation above with $u$ replaced by $Bu$ gives

$$
\cos z\,\big[u^\dagger B(hv) - (hu)^\dagger Bv\big] = \partial_8\big(\sin z\;u^\dagger BM_8v\big) .
$$

**The role of the spin-connection term.** Without the term $3H\gamma^{(x_8)}$ the matrix $A$ would be $A_0 = -im\gamma^{(x_4)}$ with $A_0 - A_0^\dagger = 0$, and the same steps would leave

$$
\cos z\,\big[u^\dagger(h_0v) - (h_0u)^\dagger v\big] = \partial_8\big(\sin z\,u^\dagger M_8v\big) - 6H\cos z\,u^\dagger M_8v :
$$

a remainder that is not a boundary term. In these variables and with this volume, the spin-connection term is exactly what makes the hidden-direction operator symmetric up to the boundary term. (This role depends on the variables: with $\Psi = \sin^{-1/2}z\,\chi$ the connection term disappears from the equation altogether; `python-scope.json`, check `rescaling_removes_the_connection_term`.)

**What follows.** The good-sector evolution in the author's metric is Hermitian, and the Krein charge $\int\cos z\,\Psi^\dagger B\Psi\,d^7x$ conserved, only if a **boundary condition** at $z = \pi/2$ removes the flux. The Kohn-Sham record imposes such a condition, the Z2 brane condition, which is ASSUMED (Chapter 14); the quantisation of the Revision record imposes none.

### 10.28 Waves that do not depend on $x_8$, and where their Krein charge goes

**Finite norm.** A wave of the good sector that depends on $x_4$ only has $\partial_8\Psi = 0$, so $h$ acts on it as the constant matrix $A$. Its norm is finite: on the patch $0 < z < \pi/2$, that is $0 < x_8 < \pi/(12H)$,

$$
\int_0^{\pi/(12H)}\cos(6Hx_8)\,dx_8 = \Big[\frac{\sin(6Hx_8)}{6H}\Big]_0^{\pi/(12H)} = \frac{\sin(\pi/2) - \sin 0}{6H} = \frac{1}{6H},
$$

by the antiderivative of the cosine and the chain rule. So these waves are honest members of the good sector.

**Growth for $m^2 < 9H^2$.** Square $A$:

$$
(-im\gamma^{(x_4)})^2 = -m^2\gamma^{(x_4)}\gamma^{(x_4)} = m^2I_{16},\qquad (3iH\gamma^{(x_4)}\gamma^{(x_8)})^2 = -9H^2(\gamma^{(x_4)}\gamma^{(x_8)})^2 = -9H^2I_{16},
$$

and the mixed terms cancel:

$$
(-im\gamma^{(x_4)})(3iH\gamma^{(x_4)}\gamma^{(x_8)}) + (3iH\gamma^{(x_4)}\gamma^{(x_8)})(-im\gamma^{(x_4)}) = 3mH\big(\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_8)} + \gamma^{(x_4)}\gamma^{(x_8)}\gamma^{(x_4)}\big)
$$

$$
= 3mH\big(\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_8)} - \gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_8)}\big) = 0 ,
$$

by multiplying out ($(-i)(3i) = 3$) and by exchanging $\gamma^{(x_8)}\gamma^{(x_4)}$ in the second product. Hence

$$
AA = (m^2 - 9H^2)\,I_{16} .
$$

For $m^2 < 9H^2$, that is $-3H < m < 3H$, the eigenvalues of $A$ are $\pm i\sqrt{9H^2 - m^2}$ (eight of each, because $\mathrm{tr}\,A = 0$), and half of these finite-norm waves grow like $e^{\kappa x_4}$ with $\kappa = \sqrt{9H^2 - m^2}$. At $m = H = 1$ the eigenvalues are $\pm\sqrt{-8} = \pm2\sqrt2\,i$ (`python-scope.json`, check `good_sector_x8_independent_modes_without_boundary_condition`). For $m^2 > 9H^2$ they are real. So without a boundary condition the curved good sector of the author's metric contains growing waves whenever $|m| < 3H$.

**An exact growing solution.** The equation $i\,\partial_4\Psi = A\Psi$ is $\partial_4\Psi = M\Psi$ with $M = -iA = -m\gamma^{(x_4)} + 3H\gamma^{(x_4)}\gamma^{(x_8)}$, and $MM = -AA = (9H^2 - m^2)I_{16} = k^2I_{16}$ with $k = \sqrt{9H^2 - m^2}$. As in Section 10.4 the exponential series collapses (even powers $M^{2j} = k^{2j}I_{16}$, odd powers $M^{2j+1} = k^{2j}M$), and

$$
\Psi(x_4) = e^{Mx_4}\chi = \Big(\cosh(kx_4)\,I_{16} + \frac{\sinh(kx_4)}{k}\,M\Big)\chi
$$

for any constant column $\chi$, by the power series of $\cosh$ and $\sinh$. Check: $\partial_4\Psi = (k\sinh(kx_4)\,I_{16} + \cosh(kx_4)\,M)\chi$, while $M\Psi = (\cosh(kx_4)\,M + \frac{\sinh(kx_4)}{k}MM)\chi = (\cosh(kx_4)\,M + k\sinh(kx_4)\,I_{16})\chi$: equal. This is the member $\alpha = 0$ of the exact family of the Revision theory record (`python-field-theory.json`, check `exact_solution_family_x4_x8`). For large $x_4$ both $\cosh$ and $\sinh$ grow like $\frac12e^{kx_4}$, so the ordinary squared length $\Psi^\dagger\Psi$ grows like $e^{2kx_4}$.

**Where the Krein charge goes, line by line.** The Krein charge of this wave is $Q(x_4) = \int\cos z\,\Psi^\dagger B\Psi\,dx_8 = \Psi^\dagger B\Psi/(6H)$, because $\Psi$ does not depend on $x_8$. Its rate of change: from $\partial_4\Psi = -ih\Psi$ and $\partial_4\Psi^\dagger = i(h\Psi)^\dagger$,

$$
\partial_4(\Psi^\dagger B\Psi) = i(h\Psi)^\dagger B\Psi - i\Psi^\dagger B(h\Psi) = -i\big[\Psi^\dagger B(h\Psi) - (h\Psi)^\dagger B\Psi\big] .
$$

Multiply by $\cos z$, integrate over the patch, and use the Krein version of Section 10.27 with $u = v = \Psi$:

$$
\frac{dQ}{dx_4} = -i\int\partial_8\big(\sin z\,\Psi^\dagger BM_8\Psi\big)\,dx_8 = -i\,\Psi^\dagger BM_8\Psi\Big|_{z = \pi/2} = \Psi^\dagger B\gamma^{(x_4)}\gamma^{(x_8)}\Psi .
$$

The second step integrates the derivative (the bracket vanishes at the tip and is $\Psi^\dagger BM_8\Psi$ at $z = \pi/2$); the third inserts $M_8 = i\gamma^{(x_4)}\gamma^{(x_8)}$ and $-i \cdot i = 1$. The charge is not conserved: it changes by exactly the flux through the patch end. Notebook 10d follows it for $m = H = 1$ ($k = 2\sqrt2$) and a column $\chi$ with $B\chi = \chi$ and $\chi^\dagger\chi = 1$: $Q(0) = \chi^\dagger B\chi/6 = 1/6$, printed as 0.166667, and $Q(1.5) = 454.007$; the change agrees with the flux added up over time to a relative accuracy of $6.7 \times 10^{-7}$.

| statement | status | where it is verified |
| --- | --- | --- |
| $\cos z\,[u^\dagger(hv) - (hu)^\dagger v] = \partial_8(\sin z\,u^\dagger M_8v)$; flux $2i$ at $z = \pi/2$ for the recorded column | PROVED | `python-scope.json`, check `good_sector_hermiticity_up_to_the_brane_flux`; `wolfram-field-theory.json`, check `good_sector_hermiticity_curved` |
| without $3H\gamma^{(x_8)}$ the remainder $-6H\cos z\,u^\dagger M_8v$ survives | PROVED | `wolfram-field-theory.json`, check `good_sector_hermiticity_curved` |
| the Krein form is conserved only up to boundary terms | PROVED | `wolfram-field-theory.json`, check `Krein_form_conserved_curved` |
| $x_8$-independent waves: norm $1/(6H)$, $AA = (m^2 - 9H^2)I_{16}$, $\pm2\sqrt2\,i$ at $m = H = 1$ | PROVED | `python-scope.json`, check `good_sector_x8_independent_modes_without_boundary_condition` |
| the exact solution $(\cosh kx_4 + \sinh(kx_4)/k\,M)\chi$ | PROVED | `python-field-theory.json`, check `exact_solution_family_x4_x8` |
| its Krein charge changes by the flux through $z = \pi/2$ | COMPUTED (relative accuracy $6.7 \times 10^{-7}$) | Notebook 10d, In [8] |
| a boundary condition at $z = \pi/2$ for the quantised field | OPEN (the Kohn-Sham record ASSUMES the Z2 brane condition) | Revision theory document, section 11 |

### 10.29 Example: Notebook 10d studies the curved good sector

Notebook 10d proves the four matrix facts (D1) to (D4) and the boundary-term identities of Section 10.27 exactly with sympy, checks them on two concrete wave functions, computes the flux $2i$ of the recorded column, shows the role of the spin-connection term in a figure, proves $AA = (m^2 - 9H^2)I_{16}$ and the norm $1/(6H)$, follows the eigenvalues of $A$ as the mass grows, and verifies the exact growing solution and the change of its Krein charge by the flux through $z = \pi/2$ (Section 10.28). It draws five figures and ends with the line ALL 16 CHECKS PASSED (notebook 10d).

<!-- NOTEBOOK 10d -->

### 10.32 Line-by-line walk-through of Notebook 10d

The notebook has 10 code cells, In [1] to In [10]; docstrings are left out of the quotations (they are printed in Section 10.31).

**In [1], the set-up cell.** Its first 248 lines are comments that repeat the run instructions of Section 10.30. The code is that of In [1] of Notebook 10a (Section 10.10), with the line `NOTEBOOK_ID = "10d"  # this notebook: chapter 10, example d`. It prints `Set-up of notebook 10d complete: repository folder found, helpers defined.`

**In [2], the matrices of the hidden direction.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer
import sys  # the screen output, sys.stdout

import numpy as np  # numbers, arrays and matrices
import sympy as sp  # exact algebra with symbols


REPORT_CHECKS = {}  # report file -> {check name: verdict}; each file is read once


def record_says_pass(record):
    path, separator, check_name = record.partition(", check ")
    if not separator:  # a data entry of a record file that the notebook reads itself
        return True
    if path not in REPORT_CHECKS:
        checks = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
        REPORT_CHECKS[path] = {c["name"]: c["verdict"].upper() for c in checks}
    return REPORT_CHECKS[path].get(check_name) == "PASS"


def check_record(condition, name, record):
    if not record_says_pass(record):  # the cited check must exist and say PASS
        raise AssertionError("the cited record check is missing or not PASS: " + record)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
        check(condition, name, record=record)
    sys.stdout.write(buffer.getvalue())  # one single piece of output
```

The imports and the helpers `REPORT_CHECKS`, `record_says_pass` and `check_record` of In [2] of Notebook 10a (Section 10.10): a cited report check must still exist with the verdict PASS, and the PASS line and the line naming the record are printed in one piece.

```python
BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
    encoding="utf-8"))
gamma = {a: np.array(fixture["gamma"][a - 1], dtype=float) for a in range(1, 9)}
C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]
B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4)
g = {a: sp.Matrix(fixture["gamma"][a - 1]) for a in range(1, 9)}  # exact gammas
B_exact = -sp.I * g[8] * g[1] * g[2] * g[3] * g[4]
```

The colours; the gammas as numpy arrays of decimal numbers (`dtype=float`, because they will be combined with decimal numbers such as the mass 1.0), $C$ and $B$; and the same gammas and $B$ as exact sympy matrices.

```python
m = sp.Symbol("m", real=True)  # the mass
H = sp.Symbol("H", positive=True)  # the author's constant H > 0
x8 = sp.Symbol("x8", real=True)  # the hidden coordinate
z = 6 * H * x8  # z = 6 H x8
M8 = sp.I * g[4] * g[8]  # M_8 = i gamma^(x4) gamma^(x8)
A = -sp.I * m * g[4] + 3 * sp.I * H * g[4] * g[8]  # the part without derivative
A_no_connection = -sp.I * m * g[4]  # the same without the term 3 H
D = sp.tan(z) * M8  # the coefficient of the derivative d/dx8
zero = sp.zeros(16, 16)
```

The letters $m$ (any real number), $H$ (positive) and $x_8$, and the expression $z = 6Hx_8$. Then the matrices of Section 10.27: $M_8 = i\gamma^{(x_4)}\gamma^{(x_8)}$, $A = -im\gamma^{(x_4)} + 3iH\gamma^{(x_4)}\gamma^{(x_8)}$, the matrix $A_0 = -im\gamma^{(x_4)}$ without the spin-connection term, and $D = \tan z\,M_8$; `zero` is the $16 \times 16$ zero matrix.

```python
anti_hermitian = M8.H == -M8
identity_D = (sp.cos(z) * D - sp.sin(z) * M8).applyfunc(sp.simplify) == zero
identity_A = (sp.cos(z) * (A - A.H) - sp.diff(sp.sin(z), x8) * M8).applyfunc(
    sp.simplify) == zero
B_commutes = (B_exact * g[4] == g[4] * B_exact) and (B_exact * g[8] == g[8] * B_exact)
```

The four matrix facts: (D1) $M_8^\dagger = -M_8$ (`.H` is the conjugate transpose); (D2) $\cos z\,D - \sin z\,M_8 = 0$, every entry simplified; (D3) $\cos z\,(A - A^\dagger) - (\partial_8\sin z)M_8 = 0$, where `sp.diff(sp.sin(z), x8)` is the derivative $6H\cos z$; (D4) $B$ commutes with $\gamma^{(x_4)}$ and with $\gamma^{(x_8)}$.

```python
say(f"M8 anti-Hermitian: {anti_hermitian}; cos z D = sin z M8: {identity_D}; "
    f"cos z (A - A^dagger) = d8(sin z) M8: {identity_A}; B commutes with "
    f"gamma^(x4) and gamma^(x8): {B_commutes}")
check(anti_hermitian and identity_D and identity_A and B_commutes,
      "exact: the four matrix identities of the hidden direction")
```

The printed line shows `True` four times, and the check prints its PASS line.

**In [3], symmetric up to a boundary term, on wave functions.**

```python
rng = np.random.default_rng(12345)


def test_function():
    def number():
        return int(rng.integers(-3, 4)) + sp.I * int(rng.integers(-3, 4))
    return sp.Matrix([number() + number() * sp.sin(z) + number() * sp.cos(z)
                      for _ in range(16)])
```

A random generator with the fixed seed 12345. `test_function` builds a column of 16 exact functions of $x_8$, each of the form $a + b\sin z + c\cos z$. The inner function `number` returns a complex whole number whose real and imaginary parts are drawn from $-3$ to 3 (`rng.integers(-3, 4)` excludes the upper end 4).

```python
def apply_h(matrix_A, w):
    return matrix_A * w + D * w.diff(x8)


def is_zero(expression):
    zz = sp.Symbol("zz")
    rewritten = sp.expand_trig(sp.expand(expression.subs(x8, zz / (6 * H))))
    return sp.simplify(rewritten) == 0
```

`apply_h(matrix_A, w)` applies the operator $h = A + D\partial_8$ (or $h_0$ when the matrix $A_0$ is given) to a column $w$ of functions; `w.diff(x8)` differentiates every entry. `is_zero` decides exactly whether an expression vanishes: it writes $x_8 = zz/(6H)$ with a new letter $zz$, so that $z$ becomes $zz$ and $H$ drops out of the trigonometric functions, multiplies out, expands the trigonometric functions of sums (`sp.expand_trig`), and simplifies.

```python
u, v = test_function(), test_function()
hv, hu = apply_h(A, v), apply_h(A, u)
defect = (sp.cos(z) * ((u.H * hv)[0] - (hu.H * v)[0])
          - sp.diff(sp.sin(z) * (u.H * M8 * v)[0], x8))
```

Two test functions $u$ and $v$, and $hv$, $hu$. `u.H * hv` is the row $u^\dagger$ times the column $hv$, a $1 \times 1$ matrix, and `[0]` takes its single entry. `defect` is $\cos z\,[u^\dagger(hv) - (hu)^\dagger v] - \partial_8(\sin z\,u^\dagger M_8v)$, which must vanish (Section 10.27).

```python
hv0, hu0 = apply_h(A_no_connection, v), apply_h(A_no_connection, u)
defect_without = (sp.cos(z) * ((u.H * hv0)[0] - (hu0.H * v)[0])
                  - sp.diff(sp.sin(z) * (u.H * M8 * v)[0], x8))
remainder_ok = is_zero(defect_without + 6 * H * sp.cos(z) * (u.H * M8 * v)[0])
krein_defect = (sp.cos(z) * ((u.H * B_exact * hv)[0] - (hu.H * B_exact * v)[0])
                - sp.diff(sp.sin(z) * (u.H * B_exact * M8 * v)[0], x8))
```

The variable `defect_without` is the same defect for the operator without the spin-connection term. By Section 10.27 it must equal $-6H\cos z\,u^\dagger M_8v$, so `remainder_ok` tests that it plus $6H\cos z\,u^\dagger M_8v$ vanishes. The variable `krein_defect` is the Krein version, with $u^\dagger B$ in place of $u^\dagger$.

```python
check_record(is_zero(defect),
             "exact: cos z (u^dagger h v - (h u)^dagger v) = d8(sin z u^dagger M8 v)",
             record="Revision/theory/reports/python-scope.json, check "
                    "good_sector_hermiticity_up_to_the_brane_flux")
check_record(remainder_ok,
             "exact: without the term 3 H the remainder -6 H cos z u^dagger M8 v stays",
             record="Revision/theory/reports/wolfram-field-theory.json, check "
                    "good_sector_hermiticity_curved")
check_record(is_zero(krein_defect),
             "exact: the Krein form is conserved up to d8(sin z u^dagger B M8 v)",
             record="Revision/theory/reports/wolfram-field-theory.json, check "
                    "Krein_form_conserved_curved")
```

Three exact checks, reproducing the record checks `good_sector_hermiticity_up_to_the_brane_flux`, `good_sector_hermiticity_curved` and `Krein_form_conserved_curved`.

**In [4], the flux at the two ends.**

```python
G48 = gamma[4] @ gamma[8]  # gamma^(x4) gamma^(x8), real
symmetric_square = np.array_equal(G48, G48.T) and np.array_equal(G48 @ G48,
                                                                  np.eye(16))
e_first = np.eye(16)[:, 0]
u_flux = e_first + G48 @ e_first  # an eigenvector of G48 with eigenvalue +1
M8_numbers = 1j * G48
flux_value = u_flux.conj() @ M8_numbers @ u_flux
```

`G48` is $\gamma^{(x_4)}\gamma^{(x_8)}$; `symmetric_square` tests that it is symmetric and squares to $I_{16}$ (Section 10.27). `e_first` is the first unit column $e_1$ (the first column of the identity matrix), and `u_flux` $= e_1 + \gamma^{(x_4)}\gamma^{(x_8)}e_1$ is an eigenvector with eigenvalue $+1$: applying $\gamma^{(x_4)}\gamma^{(x_8)}$ gives $\gamma^{(x_4)}\gamma^{(x_8)}e_1 + e_1$, the same column, because the matrix squares to $I_{16}$. `flux_value` is $u^\dagger M_8u$.

```python
report("u^dagger u for the column u = e_1 + gamma4 gamma8 e_1", f"{u_flux @ u_flux:.1f}")
report("flux u^dagger M8 u at z = pi/2",
       f"{flux_value.imag:.1f} i (real part {abs(flux_value.real):.1f})")
check_record(symmetric_square and np.allclose(G48 @ u_flux, u_flux)
             and abs(flux_value - 2j) < 1e-14,
             "the flux at z = pi/2 is u^dagger M8 u = 2 i for gamma4 gamma8 u = u",
             record="Revision/theory/reports/python-scope.json, check "
                    "good_sector_hermiticity_up_to_the_brane_flux")
```

The printed lines show $u^\dagger u = 2.0$ and the flux $2.0\,i$ with real part 0.0 (the size of the real part is printed, so that no minus sign of a rounding zero appears). The check reproduces the record's example.

```python
z_values = np.linspace(0.0, np.pi / 2, 400)
fig, ax = plt.subplots()
ax.plot(z_values, np.cos(z_values), color=BLUE, linewidth=2,
        label="volume factor $\\sqrt{|g|} = \\cos z$")
ax.plot(z_values, np.sin(z_values), color=ORANGE, linewidth=2,
        label="flux factor $\\sin z$ of the bracket")
ax.plot([0.0], [0.0], "o", color=ORANGE, markersize=8)
ax.plot([np.pi / 2], [1.0], "o", color=ORANGE, markersize=8)
```

400 values of $z$ from 0 to $\pi/2$; the blue curve is the volume factor $\cos z$, the orange curve the factor $\sin z$ of the boundary bracket, with dots at its two ends.

```python
ax.annotate("tip: the flux vanishes", (0.0, 0.0), xytext=(0.15, 0.25),
            arrowprops={"arrowstyle": "->", "color": GREY})
ax.annotate("patch end: the flux remains", (np.pi / 2, 1.0), xytext=(0.55, 1.08),
            arrowprops={"arrowstyle": "->", "color": GREY})
ax.set_xlabel("$z = 6 H x_8$ (from the tip $z = 0$ to the patch end $z = \\pi/2$)")
ax.set_ylabel("value")
ax.set_ylim(-0.05, 1.25)
ax.set_title("The hidden direction: volume and boundary flux")
ax.legend(loc="center left")
save_figure(fig, "volume_and_flux",
...)
```

Two arrows explain the two dots. Figure 1 of Notebook 10d shows the volume falling from 1 to 0 and the bracket factor rising from 0 to 1: the volume vanishes at the patch end, but the boundary bracket does not, so a flux can pass through $z = \pi/2$.

**In [5], the role of the spin-connection term in a picture.**

```python
numbers = {m: 1, H: 1}  # m = H = 1, so z = 6 x8
hu_full, hu_bare = apply_h(A, u), apply_h(A_no_connection, u)
left = sp.cos(z) * ((u.H * hu_full)[0] - (hu_full.H * u)[0])
right = sp.diff(sp.sin(z) * (u.H * M8 * u)[0], x8)
left_bare = sp.cos(z) * ((u.H * hu_bare)[0] - (hu_bare.H * u)[0])
```

For $u = v$ and $m = H = 1$ the cell forms the three exact expressions: the defect with the term $3H$ (`left`), the derivative $\partial_8(\sin z\,u^\dagger M_8u)$ (`right`) and the defect without the term (`left_bare`).

```python
x8_values = np.linspace(0.002, np.pi / 12 - 0.002, 300)  # inside 0 < z < pi/2
curves = [np.imag(sp.lambdify(x8, e.subs(numbers), "numpy")(x8_values))
          for e in (left, right, left_bare)]
difference = np.max(np.abs(curves[0] - curves[1]))
report("largest |left - right| on the grid", f"{difference:.1e}")
check(difference < 1e-9, "numerical: the two sides agree along the hidden direction")
```

For $H = 1$ the patch is $0 < x_8 < \pi/12$; the 300 points stay a little inside it. `e.subs(numbers)` puts $m = H = 1$ into an expression, and `sp.lambdify(x8, ..., "numpy")` turns it into a fast numpy function of $x_8$, which is evaluated at all points at once. For $u = v$ each expression is a number minus its complex conjugate, purely imaginary, so `np.imag` keeps the imaginary parts. The largest difference between the left and the right side is printed as `5.7e-13`, rounding only.

```python
fig, ax = plt.subplots()
ax.plot(6 * x8_values, curves[0], color=BLUE, linewidth=3,
        label="left side, with the term $3H$")
ax.plot(6 * x8_values, curves[1], "--", color=GREEN, linewidth=2,
        label="right side $\\partial_8(\\sin z\\,u^\\dagger M_8 u)$")
ax.plot(6 * x8_values, curves[2], color=ORANGE, linewidth=2,
        label="left side WITHOUT the term $3H$")
ax.set_xlabel("$z = 6 H x_8$ ($m = H = 1$)")
ax.set_ylabel("imaginary part")
ax.set_title("The spin-connection term makes the defect a pure boundary term")
ax.legend(fontsize=8)
save_figure(fig, "symmetry_defect",
...)
```

The three curves against $z = 6x_8$. Figure 2 of Notebook 10d shows the green dashed curve exactly on the thick blue one, and the orange curve away from both: with the spin-connection term the defect is a derivative, whose integral is the flux at the ends; without it the remainder $-6H\cos z\,u^\dagger M_8u$ of Section 10.27 separates the curves.

**In [6], the waves that do not depend on $x_8$.**

```python
norm_integral = sp.integrate(sp.cos(6 * H * x8), (x8, 0, sp.pi / (12 * H)))
say(f"integral of cos(6 H x8) over the patch: {norm_integral}")
A_square_ok = (A * A - (m ** 2 - 9 * H ** 2) * sp.eye(16)).applyfunc(
    sp.expand) == zero
A_not_hermitian = (A - A.H).applyfunc(sp.expand) != zero
G48_numbers = gamma[4] @ gamma[8]  # gamma^(x4) gamma^(x8) as numbers
```

`sp.integrate(f, (x8, a, b))` computes the definite integral exactly; the printed value is `1/(6*H)`, the norm of Section 10.28. The two truth values test $AA = (m^2 - 9H^2)I_{16}$ and that $A$ is not Hermitian ($A - A^\dagger$ is not the zero matrix). `G48_numbers` is $\gamma^{(x_4)}\gamma^{(x_8)}$ again, for the numerical part.

```python
def A_numbers_of(mass, H_value=1.0):
    return -1j * mass * gamma[4] + 3j * H_value * G48_numbers


A_numbers = A_numbers_of(1.0)
eigenvalues = np.linalg.eigvals(A_numbers)
upper = int(np.sum(np.abs(eigenvalues - 2j * np.sqrt(2)) < 1e-9))
lower = int(np.sum(np.abs(eigenvalues + 2j * np.sqrt(2)) < 1e-9))
report("eigenvalues 2 sqrt(2) i and -2 sqrt(2) i at m = H = 1, how many",
       f"{upper} and {lower}")
```

`A_numbers_of(mass)` is the matrix $A$ as numbers for a given mass ($H = 1$ unless another value is given). At $m = H = 1$ the 16 eigenvalues are counted: how many lie within $10^{-9}$ of $2\sqrt2\,i$ and how many of $-2\sqrt2\,i$. The printed counts are 8 and 8.

```python
check_record(norm_integral == 1 / (6 * H) and A_square_ok and A_not_hermitian
             and (upper, lower) == (8, 8),
             "x8-independent waves: A^2 = (m^2 - 9 H^2) I, at m = H = 1: +-2 sqrt(2) i",
             record="Revision/theory/reports/python-scope.json, check "
                    "good_sector_x8_independent_modes_without_boundary_condition")
```

The check reproduces the record check `good_sector_x8_independent_modes_without_boundary_condition`.

**In [7], the frequencies against the mass.**

```python
mass_values = np.linspace(0.0, 5.0, 101)
paths = []
for mass in mass_values:
    paths.append(np.linalg.eigvals(A_numbers_of(mass)))
paths = np.array(paths)
worst = np.max(np.abs(np.sort(np.abs(paths), axis=1)
                      - np.sqrt(np.abs(mass_values ** 2 - 9))[:, None]))
report("largest deviation of |eigenvalue| from sqrt|m^2 - 9|", f"{worst:.1e}")
check(worst < 1e-6, "the eigenvalues of A follow +-sqrt(m^2 - 9 H^2)")
```

For 101 masses from 0 to 5 (step 0.05) the 16 eigenvalues of $A$ are stored as one row of the table `paths`. Every eigenvalue must have the size $\sqrt{|m^2 - 9|}$ ($H = 1$): `np.abs(paths)` are the sizes, sorted in each row, and `[:, None]` turns the 101 predicted values into a column, so that each is subtracted from its own row. The largest deviation is printed as `4.6e-08`: at $m = 3$ exactly the matrix $A$ has $AA = 0$ and cannot be diagonalised, and there the numerical eigenvalues are accurate only to about $10^{-8}$; the tolerance $10^{-6}$ allows for it.

```python
fig, ax = plt.subplots(figsize=(6.0, 5.0))
growing = mass_values < 3.0
for column in range(16):
    ax.plot(paths[growing, column].real, paths[growing, column].imag, ".",
            color=ORANGE, markersize=4)
    ax.plot(paths[~growing, column].real, paths[~growing, column].imag, ".",
            color=BLUE, markersize=4)
ax.plot([], [], ".", color=ORANGE, label="$m < 3H$: imaginary, the waves grow")
ax.plot([], [], ".", color=BLUE, label="$m > 3H$: real, the waves oscillate")
ax.plot([0, 0], [2 * np.sqrt(2), -2 * np.sqrt(2)], "o", color=GREEN, markersize=9,
        fillstyle="none", label="recorded: $m = H = 1$, $\\pm 2\\sqrt{2}\\,i$")
```

`growing` is a list of truth values, true for the masses below 3; `paths[growing, column]` picks the eigenvalue number `column` at those masses, and `~growing` is the opposite list. Each eigenvalue is drawn as a dot in the complex plane (real part horizontal, imaginary part vertical), orange for $m < 3$ and blue for $m \geq 3$; the empty plots only create legend entries; green circles mark the recorded values $\pm2\sqrt2\,i$.

```python
ax.set_xlabel("real part of the eigenvalue of $A$ (units of $H$)")
ax.set_ylabel("imaginary part (units of $H$)")
ax.set_aspect("equal")
ax.set_title("Frequencies of the $x_8$-independent waves, $m$ from 0 to 5")
ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), fontsize=8)  # outside
save_figure(fig, "frequency_paths",
...)
```

Equal scales on both axes; `bbox_to_anchor` places the legend outside the drawing, to its right. Figure 3 of Notebook 10d shows the eigenvalues coming down the imaginary axis from $\pm3i$ (at $m = 0$) to 0 (at $m = 3$) and then moving out along the real axis: growth for $m < 3H$, oscillation for $m > 3H$.

```python
rate = np.sqrt(np.maximum(9.0 - mass_values ** 2, 0.0))
fig, ax = plt.subplots()
ax.plot(mass_values, rate, color=ORANGE, linewidth=2,
        label="growth rate $\\kappa = \\sqrt{9H^2 - m^2}$")
ax.plot([1.0], [2 * np.sqrt(2)], "o", color=GREEN, markersize=9,
        label="recorded: $m = H = 1$, $\\kappa = 2\\sqrt{2}$")
ax.axvline(3.0, color=GREY, linestyle=":", linewidth=1)
ax.set_xlabel("mass $m$ in units of $H$")
ax.set_ylabel("growth rate $\\kappa$ (units of $H$)")
ax.set_title("Without a boundary condition: growth for $m < 3H$")
ax.legend()
save_figure(fig, "growth_rate",
...)
```

The growth rate $\kappa = \sqrt{9 - m^2}$ for $m < 3$ and 0 beyond (`np.maximum(..., 0.0)` replaces the negative values under the root by 0), with the recorded point $\kappa = 2\sqrt2 \approx 2.83$ at $m = 1$. Figure 4 of Notebook 10d shows the curve falling from 3 at $m = 0$ to 0 at $m = 3$ (a quarter of the circle $\kappa^2 + m^2 = 9$, drawn with unequal scales on the two axes): without a boundary condition at $z = \pi/2$, every mass below $3H$ gives growing waves of finite norm.

**In [8], the exact growing solution and its Krein charge.**

```python
x4, k = sp.symbols("x4 k", positive=True)
M_exact = -m * g[4] + 3 * H * g[4] * g[8]
chi = sp.Matrix(sp.symbols("q1:17"))  # any constant column
Psi = (sp.cosh(k * x4) * sp.eye(16) + sp.sinh(k * x4) / k * M_exact) * chi
field_equation = g[4] * Psi.diff(x4) + 3 * H * g[8] * Psi - m * Psi  # d8 Psi = 0
```

`sp.symbols("x4 k", positive=True)` makes two positive letters at once, and `sp.symbols("q1:17")` the 16 letters $q_1, \dots, q_{16}$, the entries of an arbitrary constant column $\chi$. `M_exact` is $M = -m\gamma^{(x_4)} + 3H\gamma^{(x_4)}\gamma^{(x_8)}$ and `Psi` the solution of Section 10.28. `field_equation` is the left side minus the right side of the field equation of Section 10.27 for a wave with $\partial_8\Psi = 0$, which must vanish.

```python
# multiply by k, then replace k^2 by 9 H^2 - m^2 (the definition of k)
residual = field_equation.applyfunc(
    lambda e: sp.expand(sp.expand(k * e).subs(k ** 2, 9 * H ** 2 - m ** 2)))
square_ok = (M_exact * M_exact - (9 * H ** 2 - m ** 2) * sp.eye(16)).applyfunc(
    sp.expand) == zero
check_record(square_ok and residual == sp.zeros(16, 1),
             "exact: Psi = (cosh kx4 + sinh(kx4)/k M) chi solves the field equation",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "exact_solution_family_x4_x8")
```

The expression contains $1/k$ (from $\sinh(kx_4)/k$); as the comment says, every entry is multiplied by $k$ to clear it, multiplied out, and every $k^2$ is replaced by $9H^2 - m^2$, the definition of $k$; then every entry must be 0. `square_ok` checks $MM = (9H^2 - m^2)I_{16}$. The check reproduces the record check `exact_solution_family_x4_x8`.

```python
M_numbers = -1.0 * gamma[4] + 3.0 * G48  # m = H = 1
k_number = np.sqrt(8.0)  # k = sqrt(9 - 1) = 2 sqrt(2)
plus_columns = (np.eye(16) + B) / 2  # columns with B chi = chi (after scaling)
chi_number = plus_columns[:, 0] / np.linalg.norm(plus_columns[:, 0])
x4_values = np.linspace(0.0, 1.5, 3001)
lengths, charges, fluxes = [], [], []
```

For $m = H = 1$: $M$ as numbers and $k = \sqrt{9 - 1} = 2\sqrt2$. The columns of the projector $\frac12(I_{16} + B)$ lie in the eigenspace $B\chi = \chi$; its first column, divided by its length, is the starting column $\chi$ with $\chi^\dagger\chi = 1$. 3001 times from 0 to 1.5 (step 0.0005).

```python
for t in x4_values:
    Psi_t = (np.cosh(k_number * t) * np.eye(16)
             + np.sinh(k_number * t) / k_number * M_numbers) @ chi_number
    lengths.append((Psi_t.conj() @ Psi_t).real)
    charges.append((Psi_t.conj() @ B @ Psi_t).real / 6.0)  # 6 H = 6
    fluxes.append((Psi_t.conj() @ B @ G48 @ Psi_t).real)
lengths, charges, fluxes = map(np.array, (lengths, charges, fluxes))
```

At each time the loop computes $\Psi(x_4)$, its ordinary squared length $\Psi^\dagger\Psi$, its Krein charge $Q = \Psi^\dagger B\Psi/(6H)$ and the flux $\Psi^\dagger B\gamma^{(x_4)}\gamma^{(x_8)}\Psi$, the rate $dQ/dx_4$ of Section 10.28. `map(np.array, ...)` turns each of the three lists into an array.

```python
step = x4_values[1] - x4_values[0]
added_flux = np.concatenate([[0.0], np.cumsum((fluxes[1:] + fluxes[:-1]) / 2) * step])
relative = np.max(np.abs(charges - charges[0] - added_flux)) / np.max(np.abs(charges))
report("Krein charge Q at x4 = 0 and at x4 = 1.5", f"{charges[0]:.6f} and "
       f"{charges[-1]:.3f}")
report("largest relative mismatch of Q(x4) - Q(0) and the added flux",
       f"{relative:.1e}")
check(relative < 1e-5, "the Krein charge changes by the flux through z = pi/2")
```

The flux is added up over time by the **trapezoidal rule**: on each step the area under the curve is the step times the mean of the two end values, `(fluxes[1:] + fluxes[:-1]) / 2` (`fluxes[1:]` drops the first value and `fluxes[:-1]` the last); `np.cumsum` forms the running sums, and a 0 is put in front for the time 0. The mismatch between $Q(x_4) - Q(0)$ and the added flux, divided by the largest charge, is printed as `6.7e-07`; the RESULT lines show $Q(0) = 0.166667 = 1/6$ and $Q(1.5) = 454.007$. The check confirms that the charge changes by the flux through the patch end.

```python
growth = np.polyfit(x4_values[1500:], np.log(lengths[1500:]), 1)[0]
report("late slope of ln(Psi^dagger Psi)", f"{growth:.4f} (2 k = {2 * k_number:.4f})")
check(abs(growth - 2 * k_number) < 0.05, "the squared length grows like exp(2 k x4)")
```

`np.polyfit(x, y, 1)` fits the straight line $y = ax + b$ through the points by least squares and returns $(a, b)$; `[0]` takes the slope. The fit uses the second half of the times (from index 1500, $x_4 = 0.75$, on) and the logarithm of the squared length $\Psi^\dagger\Psi$ (the list `lengths` holds these squared lengths). The printed slope is 5.6600, close to $2k = 5.6569$ (the squared length contains $\cosh$ and $\sinh$, not a pure exponential, so the slope only approaches $2k$), and the check allows a difference of 0.05. The cell prints three PASS lines.

**In [9], the growing wave and its charge in a picture.**

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
axes[0].plot(x4_values, np.log(lengths), color=BLUE, linewidth=2,
             label="$\\ln(\\Psi^\\dagger\\Psi)$")
axes[0].plot(x4_values, 2 * k_number * x4_values + np.log(lengths[-1])
             - 2 * k_number * x4_values[-1], "--", color=GREY, linewidth=1,
             label="slope $2k = 4\\sqrt{2}$")
axes[0].set_xlabel("time $x_4$ (units of $1/H$)")
axes[0].set_ylabel("$\\ln$ of the squared length $\\Psi^\\dagger\\Psi$")
axes[0].set_title("the wave grows")
axes[0].legend()
```

The left panel draws $\ln(\Psi^\dagger\Psi)$ against $x_4$ and a grey dashed straight line of slope $2k = 4\sqrt2$ through the last point.

```python
axes[1].plot(x4_values, charges, color=ORANGE, linewidth=3,
             label="Krein charge $Q(x_4)$")
axes[1].plot(x4_values, charges[0] + added_flux, "--", color=GREEN, linewidth=2,
             label="$Q(0)$ + flux through $z = \\pi/2$")
axes[1].set_xlabel("time $x_4$ (units of $1/H$)")
axes[1].set_ylabel("Krein charge (units of $1/H$)")
axes[1].set_title("not conserved: it changes by the flux")
axes[1].legend()
save_figure(fig, "krein_leak",
...)
```

The right panel draws the Krein charge and its starting value plus the added flux. Figure 5 of Notebook 10d shows the logarithm of the squared length rising along a straight line, and the charge rising from $1/6$ to several hundred, with the green dashed curve exactly on the orange one: without a boundary condition at $z = \pi/2$ the Krein charge of the curved good sector is not conserved; it changes by exactly what passes through the patch end.

**In [10], the last check.**

```python
for name in ("10d_1_volume_and_flux.png", "10d_2_symmetry_defect.png",
             "10d_3_frequency_paths.png", "10d_4_growth_rate.png",
             "10d_5_krein_leak.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The five figure files exist, and the last line prints ALL 16 CHECKS PASSED (notebook 10d): the five figure checks and the 11 checks of the cells before (1 in In [2], 3 in In [3], 1 each in In [4] to In [7], and 3 in In [8]).

### 10.33 No invariant charge density is positive

The charge density $\Psi^\dagger B\Psi$ takes both signs. Could a cleverer choice of the charge density avoid this? A charge density must not depend on how the frame of the eight directions is turned, so it must be built from a form that is unchanged by the spin transformations. This section shows that every such density is indefinite.

**Spin transformations and invariant forms.** The 28 **generators** $S^{ab} = \frac14[\gamma^{(x_a)}, \gamma^{(x_b)}] = \frac12\gamma^{(x_a)}\gamma^{(x_b)}$ ($a < b$; the second form uses $\gamma^{(x_b)}\gamma^{(x_a)} = -\gamma^{(x_a)}\gamma^{(x_b)}$) generate the spin transformations $R = \exp(\theta S^{ab})$, which turn the frame, and their products form Spin(4,4) (Chapter 5). A **bilinear form** $\Psi^TG\Phi$ with a $16 \times 16$ matrix $G$ is **invariant** if it does not change when both columns are transformed by the same $R$: $R^TGR = G$. For $R = I_{16} + \theta S$ with a small number $\theta$,

$$
R^TGR = G + \theta\,(S^TG + GS) + \theta^2S^TGS ,
$$

by multiplying out; the form is unchanged to first order in $\theta$ exactly when

$$
S^TG + GS = 0\quad\text{for all 28 generators}.
$$

The gammas are real, so $S^\dagger = S^T$, and the same condition makes the Hermitian form $\Psi^\dagger G\Psi$ invariant.

**All invariant forms.** Chapter 5 showed two facts. First, $C\gamma^{(x_a)}C = -(\gamma^{(x_a)})^T$ (the charge-conjugation property of $C = \mathcal{C}_+$; `wolfram-algebra.json`, check `C_gamma_C_inverse`). Hence

$$
(S^{ab})^T = \tfrac12(\gamma^{(x_b)})^T(\gamma^{(x_a)})^T = \tfrac12(C\gamma^{(x_b)}C)(C\gamma^{(x_a)}C) = \tfrac12C\gamma^{(x_b)}\gamma^{(x_a)}C = -CS^{ab}C ,
$$

by the transpose of a product, the property of $C$ (the two minus signs cancel), $CC = I_{16}$, and $\gamma^{(x_b)}\gamma^{(x_a)} = -\gamma^{(x_a)}\gamma^{(x_b)}$. Insert it into the condition and multiply from the left by $C$:

$$
S^TG + GS = 0\iff -CSCG + GS = 0\iff -SCG + CGS = 0\iff (CG)S = S(CG) .
$$

So $G$ is invariant exactly when $CG$ commutes with all 28 generators. Second, the matrices that commute with all generators of Spin(4,4) form a two-dimensional family, spanned by the chiral projectors $P_- = \frac12(I_{16} - \Gamma)$ and $P_+ = \frac12(I_{16} + \Gamma)$ (the commutant of Spin(4,4) has dimension 2; `python-algebra.json`, check `spin_commutant_dimension_2`; `wolfram-algebra.json`, check `Spin44_commutant_dim_2_chiral_projectors`). Hence $CG = r_-P_- + r_+P_+$, and, multiplying by $C$,

$$
G = r_-\,CP_- + r_+\,CP_+ .
$$

Every invariant form is a combination of $CP_-$ and $CP_+$; the choice $r_- = r_+ = 1$ gives $G = C$ and the Spin(4,4) scalar $\bar\Psi\Psi = \Psi^\dagger C\Psi$ (`wolfram-algebra.json`, check `S_preserves_C`).

**Every invariant charge density is indefinite.** A charge density is the time component of a current, so it is built from an invariant form and the time gamma: its matrix is the Hermitian part $X = \frac12(Y + Y^\dagger)$ of $Y = cG\gamma^{(x_4)}$ with a complex number $c$ (the Hermitian part makes the density $\Psi^\dagger X\Psi$ real). Now $C$ is a product of four gammas, so it commutes with $\Gamma$ (moving $\Gamma$ through four gammas costs $(-1)^4 = +1$), and $P_\mp$ commute with $\Gamma$; so $G$ commutes with $\Gamma$, while $\gamma^{(x_4)}$ anticommutes with it. With $\Gamma\Gamma = I_{16}$:

$$
\Gamma Y\Gamma = cG\,\Gamma\gamma^{(x_4)}\Gamma = -cG\gamma^{(x_4)} = -Y,\qquad \Gamma X\Gamma = \tfrac12\big(\Gamma Y\Gamma + (\Gamma Y\Gamma)^\dagger\big) = -X ,
$$

where the second identity uses that $\Gamma$ is Hermitian, so $\Gamma Y^\dagger\Gamma = (\Gamma Y\Gamma)^\dagger$. Multiply $\Gamma X\Gamma = -X$ from the left by $\Gamma$: $X\Gamma = -\Gamma X$. If $Xv = \lambda v$, then

$$
X(\Gamma v) = -\Gamma Xv = -\lambda\,\Gamma v :
$$

$\Gamma$ carries every eigenvector of $X$ with eigenvalue $\lambda$ to one with eigenvalue $-\lambda$, and back. So the eigenvalues of $X$ come in pairs $\lambda, -\lambda$ of equal multiplicity, and the density $\Psi^\dagger X\Psi$ takes both signs unless $X = 0$. The canonical choice $c = -i$, $G = C$ gives $Y = -iC\gamma^{(x_4)} = B$, which is already Hermitian, so $X = B$ with eigenvalues $\pm1$, eight each. **In signature (4,4) no invariant charge density is positive**: the indefinite charge of dirac16complex is not an accident of the choice $B$. (In ordinary 3+1 dimensions the time gamma also anticommutes with the chirality $\gamma_5$, so that fact alone is not the difference. The difference is the invariant form. In 3+1 dimensions it is $G = \gamma^0$, a single gamma, which anticommutes with $\gamma_5$; so the density matrix $G\gamma^0 = \gamma^0\gamma^0 = I_4$ commutes with $\gamma_5$, the argument above gives no pairing, and the density $\psi^\dagger\psi$ is positive. In (4,4) the invariant forms $r_-CP_- + r_+CP_+$ are built from $C$, a product of four gammas, and commute with $\Gamma$, while $\gamma^{(x_4)}$ anticommutes with it; this is what produces the pairing $\lambda \to -\lambda$.)

### 10.34 The symmetries that keep the canonical rule

A transformation $\Psi \to R\Psi$ keeps the canonical anticommutator exactly when $RBR^\dagger = B$ (Section 10.15). This is equivalent to $R^\dagger BR = B$: multiplying $RBR^\dagger = B$ from the left by $R^{-1}$ and from the right by $(R^\dagger)^{-1}$ gives $B = R^{-1}B(R^\dagger)^{-1}$; the inverse of both sides, with $B^{-1} = B$, is $B = R^\dagger BR$. We call such an $R$ **Krein-unitary**. An $R$ with $R^\dagger R = I_{16}$ keeps the ordinary length and is **unitary**.

**The conditions on a generator.** For $R = I_{16} + \theta S$ to first order, $R^\dagger R = I_{16} + \theta(S^\dagger + S)$ and $R^\dagger BR = B + \theta(S^\dagger B + BS)$, so the conditions are

$$
\text{unitary: } S^\dagger = -S,\qquad\text{Krein-unitary: } S^\dagger B + BS = 0 .
$$

The first order suffices for all $\theta$: if $S^\dagger B = -BS$, then $(S^\dagger)^nB = B(-S)^n$ by moving $B$ through one factor at a time, so $\exp(\theta S^\dagger)B = B\exp(-\theta S)$ (term by term in the power series) and $R^\dagger BR = B\exp(-\theta S)\exp(\theta S) = B$.

**Which generators are anti-Hermitian.** For $a \neq b$, with $(\gamma^{(x_a)})^\dagger = \eta_{aa}\gamma^{(x_a)}$ (Section 10.15),

$$
(\gamma^{(x_a)}\gamma^{(x_b)})^\dagger = (\gamma^{(x_b)})^\dagger(\gamma^{(x_a)})^\dagger = \eta_{aa}\eta_{bb}\,\gamma^{(x_b)}\gamma^{(x_a)} = -\eta_{aa}\eta_{bb}\,\gamma^{(x_a)}\gamma^{(x_b)} .
$$

So $S^{ab}$ is anti-Hermitian when $\eta_{aa}\eta_{bb} = +1$ (both directions space-like or both time-like: a **rotation**), and Hermitian when $\eta_{aa}\eta_{bb} = -1$ (one space-like and one time-like: a **boost**). The space-like directions are $x_1, x_2, x_3, x_8$ and the time-like ones $x_4, x_5, x_6, x_7$, so there are $6 + 6 = 12$ rotations (pairs within each group of four, $\binom42 = 6$) and $4 \times 4 = 16$ boosts.

**Which generators commute with B.** $\gamma^{(x_a)}B = s_aB\gamma^{(x_a)}$ with $s_a = +1$ for $a = 1, 2, 3, 4, 8$ and $-1$ for $a = 5, 6, 7$ (Section 10.2), so $\gamma^{(x_a)}\gamma^{(x_b)}B = s_as_b\,B\gamma^{(x_a)}\gamma^{(x_b)}$: $S^{ab}$ commutes with $B$ when $s_as_b = +1$, that is both in $\{1, 2, 3, 4, 8\}$ ($\binom52 = 10$ pairs) or both in $\{5, 6, 7\}$ (3 pairs), 13 in all, and anticommutes otherwise ($5 \times 3 = 15$ pairs).

**The Krein condition.** For an anti-Hermitian $S$ the condition $S^\dagger B + BS = 0$ reads $BS - SB = 0$: $S$ must commute with $B$. For a Hermitian $S$ it reads $SB + BS = 0$: $S$ must anticommute with $B$. Counting:

- rotations that commute with $B$: the 6 among $x_1, x_2, x_3, x_8$ and the 3 among $x_5, x_6, x_7$; the 3 rotations $S^{(x_4x_t)}$, $t = 5, 6, 7$, anticommute and fail;
- boosts that anticommute with $B$: one direction among $x_1, x_2, x_3, x_8$ and one among $x_5, x_6, x_7$, $4 \times 3 = 12$; the 4 boosts $S^{(x_ax_4)}$, $a = 1, 2, 3, 8$, commute and fail.

So exactly $9 + 12 = 21$ generators are Krein-unitary: precisely the $\binom72 = 21$ pairs that do not contain $x_4$. They generate **Spin(4,3)**, the spin group of the seven slice directions (four space-like, three time-like). For the 7 generators with $x_4$ written first, $S^{(x_4x_b)} = \frac12\gamma^{(x_4)}\gamma^{(x_b)}$, the condition fails by $S^\dagger B + BS = 2BS = -iC\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_b)} = iC\gamma^{(x_b)}$ (in both cases the left side equals $2BS$, because either $S^\dagger = S$ and $SB = BS$, or $S^\dagger = -S$ and $SB = -BS$; then $\gamma^{(x_4)}\gamma^{(x_4)} = -I_{16}$). Of the 21, the 9 rotations are also unitary; the 12 boosts mixing a space direction with an extra time keep the canonical rule but change the ordinary squared length (and so the length). The canonical structure singles out the time $x_4$, as $\psi^\dagger\psi$ does in ordinary Dirac theory: a transformation that turns $x_4$ into another direction also changes the slices $x_4 = $ const on which the field is quantised.

**Finite rotations and boosts.** For $a \neq b$, $(\gamma^{(x_a)}\gamma^{(x_b)})^2 = -\gamma^{(x_a)}\gamma^{(x_a)}\gamma^{(x_b)}\gamma^{(x_b)} = -\eta_{aa}\eta_{bb}I_{16}$, so $(S^{ab})^2 = -\frac14\eta_{aa}\eta_{bb}I_{16}$. As in Section 10.4 the exponential series collapses:

$$
\exp(\theta S^{ab}) = \cos\tfrac\theta2\,I_{16} + 2\sin\tfrac\theta2\,S^{ab}\ \text{(rotation)},\qquad \exp(\theta S^{ab}) = \cosh\tfrac\theta2\,I_{16} + 2\sinh\tfrac\theta2\,S^{ab}\ \text{(boost)} .
$$

(For a rotation write $S = \frac12J$ with $JJ = -I_{16}$; the even powers of $\theta S$ give the cosine series of $\theta/2$ and the odd ones $J$ times the sine series. For a boost $JJ = +I_{16}$ and the hyperbolic functions appear.) Example: a column $u$ with $Bu = u$ and $u^\dagger u = 1$, boosted by $S^{(x_1x_5)}$ (Hermitian, Krein-unitary). Since $R$ is Hermitian, $R^\dagger R = RR = \exp(2\theta S) = \cosh\theta\,I_{16} + 2\sinh\theta\,S$, and $u^\dagger Su = 0$ (because $S$ anticommutes with $B$: $u^\dagger Su = u^\dagger SBu = -u^\dagger BSu = -(Bu)^\dagger Su = -u^\dagger Su$); so the ordinary squared length $(Ru)^\dagger(Ru) = u^\dagger R^\dagger Ru$ becomes $\cosh\theta$, while the Krein norm stays 1.

| statement | status | where it is verified |
| --- | --- | --- |
| the invariant bilinear forms are $r_-CP_- + r_+CP_+$ | PROVED (from the commutant of Spin(4,4)); COMPUTED in Notebook 10e (two zero eigenvalues, separation from about 7 down to $1.3 \times 10^{-15}$) | `python-algebra.json`, checks `spin_commutant_dimension_2` and `S_preserves_C_and_commutes_with_Gamma`; `wolfram-algebra.json`, check `S_preserves_C` |
| every invariant charge density satisfies $\Gamma X\Gamma = -X$ and is indefinite | PROVED (above) and checked for 40 random densities | Notebook 10e, In [5]; `wolfram-algebra.json`, check `B_signature_8_8` for $X = B$ |
| exactly the 21 generators without $x_4$ are Krein-unitary; defect $iC\gamma^{(x_b)}$ for $S^{(x_4x_b)}$ | PROVED | `wolfram-algebra.json`, check `S_preserves_B_only_off_x4` |
| the counts 12 (anti-Hermitian), 13 (commuting with $B$), 9 (both) | PROVED (above) and checked | Notebook 10e, In [6] |

### 10.35 Example: Notebook 10e computes the invariant forms and the generators

Notebook 10e builds the 28 generators, solves the $28 \times 256$ linear equations $S^TG + GS = 0$ numerically and checks the two solutions $CP_\mp$ exactly (Section 10.33), checks for 40 random invariant densities that every one has eight positive and eight negative eigenvalues, sorts the 28 generators into unitary, commuting with $B$ and Krein-unitary (Section 10.34), and follows a column under a rotation and two boosts. It draws five figures and ends with the line ALL 15 CHECKS PASSED (notebook 10e).

<!-- NOTEBOOK 10e -->

### 10.38 Line-by-line walk-through of Notebook 10e

The notebook has 10 code cells, In [1] to In [10]; docstrings are left out of the quotations (they are printed in Section 10.37).

**In [1], the set-up cell.** Its first 246 lines are comments that repeat the run instructions of Section 10.36. The code is that of In [1] of Notebook 10a (Section 10.10), with the line `NOTEBOOK_ID = "10e"  # this notebook: chapter 10, example e`. It prints `Set-up of notebook 10e complete: repository folder found, helpers defined.`

**In [2], the gammas, the generators and the chiral projectors.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer
import itertools  # all pairs (a, b) with a < b
import sys  # the screen output, sys.stdout

import numpy as np  # numbers, arrays and matrices
from matplotlib.colors import LinearSegmentedColormap, ListedColormap  # colours


REPORT_CHECKS = {}  # report file -> {check name: verdict}; each file is read once


def record_says_pass(record):
    path, separator, check_name = record.partition(", check ")
    if not separator:  # a data entry of a record file that the notebook reads itself
        return True
    if path not in REPORT_CHECKS:
        checks = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
        REPORT_CHECKS[path] = {c["name"]: c["verdict"].upper() for c in checks}
    return REPORT_CHECKS[path].get(check_name) == "PASS"


def check_record(condition, name, record):
    if not record_says_pass(record):  # the cited check must exist and say PASS
        raise AssertionError("the cited record check is missing or not PASS: " + record)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
        check(condition, name, record=record)
    sys.stdout.write(buffer.getvalue())  # one single piece of output
```

The imports of In [2] of Notebook 10a, and in addition `itertools`, a module of Python that lists combinations, and two kinds of colour scales of matplotlib. `REPORT_CHECKS`, `record_says_pass` and `check_record` are the helpers of Section 10.10 (a cited report check must still exist with the verdict PASS; the two printed lines come in one piece).

```python
BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
DIVERGING = LinearSegmentedColormap.from_list(
    "blue_grey_red", ["#184f95", "#f0efec", "#e34948"])
fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
    encoding="utf-8"))
gamma = {a: np.array(fixture["gamma"][a - 1], dtype=float) for a in range(1, 9)}
eta = {a: fixture["eta"][a - 1] for a in range(1, 9)}
I16 = np.eye(16)
```

The colours and the blue-grey-red colour scale of Notebook 10a; the gammas of the record as decimal numbers, the signs $\eta_{aa}$ of the frame metric, and the identity $I_{16}$.

```python
C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]
Gamma = (gamma[8] @ gamma[1] @ gamma[2] @ gamma[3] @ gamma[4] @ gamma[5]
         @ gamma[6] @ gamma[7])
B = -1j * (C @ gamma[4])
P_minus, P_plus = (I16 - Gamma) / 2, (I16 + Gamma) / 2  # the chiral projectors
```

$C$, the chirality $\Gamma$, $B$, and the projectors $P_\mp = \frac12(I_{16} \mp \Gamma)$; since $\Gamma = \mathrm{diag}(-I_8, I_8)$, $P_-$ keeps the components 1 to 8 and $P_+$ the components 9 to 16.

```python
pairs = list(itertools.combinations(range(1, 9), 2))  # (1, 2), (1, 3), ..., (7, 8)
S = {(a, b): (gamma[a] @ gamma[b] - gamma[b] @ gamma[a]) / 4 for a, b in pairs}
report("number of generators S^ab", len(S))
```

`itertools.combinations(range(1, 9), 2)` lists every pair $(a, b)$ with $a < b$ from 1 to 8, $\binom82 = 28$ pairs. The dictionary `S` stores $S^{ab} = \frac14(\gamma^{(x_a)}\gamma^{(x_b)} - \gamma^{(x_b)}\gamma^{(x_a)})$ for each pair; the RESULT line prints 28.

```python
commuting = [a for a in range(1, 9) if np.array_equal(B @ gamma[a], gamma[a] @ B)]
anticommuting = [a for a in range(1, 9) if np.array_equal(B @ gamma[a], -gamma[a] @ B)]
say(f"B commutes with gamma^(x_a) for a = {commuting}, anticommutes for a = "
    f"{anticommuting}")
check_record(commuting == [1, 2, 3, 4, 8] and anticommuting == [5, 6, 7],
             "B commutes with the gammas of x1, x2, x3, x4, x8, anticommutes with x5-x7",
             record="Revision/algebra/reports/python-algebra.json, check "
                    "B_gamma_relations")
```

The lists of the directions whose gamma commutes or anticommutes with $B$. The printed line shows `[1, 2, 3, 4, 8]` and `[5, 6, 7]`, as Section 10.2 derived, and the check reproduces the record check `B_gamma_relations`.

**In [3], every invariant bilinear form.**

```python
rows = [np.kron(s.T, I16) + np.kron(I16, s.T) for s in S.values()]
M = np.vstack(rows)  # 7168 rows, 256 columns
values = np.linalg.eigvalsh(M.T @ M)  # 256 eigenvalues, sorted, all >= 0
zero_count = int(np.sum(values < 1e-9))
```

The unknown $G$ has 256 entries; write them, row after row, as one long column $\vec G$. The rule "the row-by-row column of $XGY$ is $(X \otimes Y^T)\vec G$", where $\otimes$ is the **Kronecker product** (`np.kron`: the matrix made of the blocks $X_{ij}Y^T$), turns $S^TG = S^TGI_{16}$ into $(S^T \otimes I_{16})\vec G$ and $GS = I_{16}GS$ into $(I_{16} \otimes S^T)\vec G$. So each generator gives a $256 \times 256$ block of equations, and `np.vstack` stacks the 28 blocks into the matrix $M$ with $28 \times 256 = 7168$ rows. The invariant forms are the solutions of $M\vec G = 0$. Their number equals the number of zero eigenvalues of the $256 \times 256$ matrix $M^TM$ (if $M^TM\vec G = 0$ then $\vec G^TM^TM\vec G = \lVert M\vec G\rVert^2 = 0$, so $M\vec G = 0$). `np.linalg.eigvalsh` computes its 256 eigenvalues, sorted, and `zero_count` counts those below $10^{-9}$.

```python
report("shape of M", M.shape)
report("eigenvalues of M^T M below 1e-9 (independent invariant forms)", zero_count)
report("largest of them and smallest nonzero eigenvalue",
       f"{values[zero_count - 1]:.1e} and {values[zero_count]:.4f}")
```

The printed lines show the shape `(7168, 256)`, two zero eigenvalues, the larger of them $1.3 \times 10^{-15}$ (rounding) and the smallest nonzero eigenvalue $7.0000$: a separation of about fifteen orders of magnitude, so rounding cannot change the count.

```python
forms = {"C P_minus": C @ P_minus, "C P_plus": C @ P_plus}
exact_ok = all(np.array_equal(s.T @ G + G @ s, np.zeros((16, 16)))
               for G in forms.values() for s in S.values())
independent = np.linalg.matrix_rank(np.vstack([G.reshape(1, -1)
                                               for G in forms.values()])) == 2
check(zero_count == 2 and exact_ok and independent,
      "the invariant bilinear forms are exactly the combinations of C P- and C P+")
```

The two candidates $CP_-$ and $CP_+$ of Section 10.33. Their entries, and those of the $S^{ab}$, are multiples of $\frac12$ and $\frac14$, which the computer stores without rounding, so `np.array_equal` checks $S^TG + GS = 0$ exactly for both forms and all 28 generators. `G.reshape(1, -1)` writes a matrix as one row of 256 numbers; the two rows stacked have rank 2, so the two forms are independent. With exactly two zero eigenvalues they span all solutions.

```python
check_record(all(np.array_equal(s.T @ C + C @ s, np.zeros((16, 16)))
                 for s in S.values()),
             "C itself (= C P- + C P+) is invariant: Psibar Psi is a Spin(4,4) scalar",
             record="Revision/algebra/reports/wolfram-algebra.json, check "
                    "S_preserves_C")
check_record(all(np.array_equal(Gamma @ s, s @ Gamma) for s in S.values()),
             "every generator commutes with Gamma: the chiral halves are invariant",
             record="Revision/algebra/reports/python-algebra.json, check "
                    "S_preserves_C_and_commutes_with_Gamma")
```

Two facts of the Revision algebra record: $C$ itself is invariant, and every generator commutes with $\Gamma$ (a product of two gammas passes $\Gamma$ with the sign $(-1)^2 = +1$). The cell prints three PASS lines.

**In [4], pictures of the invariant forms and of the eigenvalues.**

```python
titles = {"C P_minus": "$CP_-$ (components 1 to 8)",
          "C P_plus": "$CP_+$ (components 9 to 16)"}
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0))
for ax, (label, G) in zip(axes, forms.items()):
    image = ax.imshow(G, cmap=DIVERGING, vmin=-1, vmax=1)
    ticks = list(range(0, 16, 3))
    ax.set_xticks(ticks, [str(t + 1) for t in ticks])
    ax.set_yticks(ticks, [str(t + 1) for t in ticks])
    ax.grid(False)
    ax.set_title(titles[label])
fig.colorbar(image, ax=list(axes), shrink=0.8, label="entry")
save_figure(fig, "invariant_forms",
...)
```

The two forms as heat maps, with the steps of the function `draw_matrix` of Notebook 10a written out (rows and columns labelled from 1 at every third one, no grid). Figure 1 of Notebook 10e shows $CP_-$ filled only in the upper left $8 \times 8$ block and $CP_+$ only in the lower right one, each block with one red or blue square per row and column; together they make $C$.

```python
fig, ax = plt.subplots()
ax.semilogy(range(1, 257), np.maximum(values, 1e-18), "o", color=BLUE, markersize=3)
ax.axhline(1e-9, color=GREY, linestyle=":", linewidth=1)
ax.set_xlabel("number of the eigenvalue (sorted)")
ax.set_ylabel("eigenvalue of $M^TM$ (log scale)")
ax.set_title("Two zero eigenvalues: two invariant forms")
save_figure(fig, "singular_values",
...)
```

`ax.semilogy` draws with a logarithmic vertical axis; values below $10^{-18}$ (the zeros, which rounding may even make slightly negative) are drawn at $10^{-18}$. The dotted line marks the threshold $10^{-9}$. Figure 2 of Notebook 10e shows two points far down at the rounding level and all 254 others at about 7 or higher: two invariant forms.

**In [5], every invariant charge density is indefinite.**

```python
rng = np.random.default_rng(12345)
spectra, all_ok = [], True
for _ in range(40):
    r_minus, r_plus = rng.normal(size=2)
    c = complex(rng.normal(), rng.normal())
    G = r_minus * C @ P_minus + r_plus * C @ P_plus
    Y = c * G @ gamma[4]
    X = (Y + Y.conj().T) / 2  # the Hermitian part
```

For 40 random choices: two real coefficients $r_\mp$ (the two values returned by `rng.normal(size=2)` are given two names at once), a random complex number $c$, the invariant form $G = r_-CP_- + r_+CP_+$ (real coefficients, so that $G$ is Hermitian), $Y = cG\gamma^{(x_4)}$ and its Hermitian part $X$ (Section 10.33).

```python
    eigenvalues = np.linalg.eigvalsh(X)
    spectra.append(eigenvalues)
    positive = int(np.sum(eigenvalues > 1e-12))  # how many eigenvalues are > 0
    negative = int(np.sum(eigenvalues < -1e-12))  # how many are < 0
    all_ok = (all_ok and np.allclose(Gamma @ X @ Gamma, -X)
              and positive == 8 and negative == 8)
```

The 16 eigenvalues of $X$ are stored for the figure and counted by sign; `all_ok` stays true while every sample has $\Gamma X\Gamma = -X$ (`np.allclose` allows rounding) and eight eigenvalues of each sign.

```python
G_canonical = C @ P_minus + C @ P_plus  # = C
Y = -1j * G_canonical @ gamma[4]
X_canonical = (Y + Y.conj().T) / 2
canonical_ok = np.allclose(X_canonical, B)
canonical_values = np.linalg.eigvalsh(X_canonical)
check(all_ok,
      "40 random invariant densities: Gamma X Gamma = -X, 8 positive, 8 negative")
check_record(canonical_ok and np.allclose(canonical_values, [-1] * 8 + [1] * 8),
             "the canonical density is B, with eigenvalues -1 and +1, eight each",
             record="Revision/algebra/reports/wolfram-algebra.json, check "
                    "B_signature_8_8")
```

The canonical choice $r_\mp = 1$, $c = -i$ gives $X = B$ with the sorted eigenvalues eight times $-1$ and eight times $+1$. Two PASS lines; the second reproduces the record check `B_signature_8_8`.

```python
fig, ax = plt.subplots()
for index, eigenvalues in enumerate(spectra, 1):
    ax.plot([index] * 16, eigenvalues, "_", color=BLUE if index % 2 else GREEN,
            markersize=10, markeredgewidth=2)
ax.plot([42] * 16, canonical_values, "_", color=ORANGE, markersize=12,
        markeredgewidth=3)
ax.annotate("$B$", (42, 1.0), xytext=(40.5, 1.6), color=ORANGE)
ax.axhline(0.0, color=GREY, linewidth=1)
ax.set_xlabel("random invariant density (1 to 40), and the canonical $B$ (42)")
ax.set_ylabel("eigenvalues of the density matrix $X$")
ax.set_title("Every invariant charge density is indefinite")
save_figure(fig, "density_eigenvalues",
...)
```

`enumerate(spectra, 1)` numbers the samples from 1. Each sample is drawn as 16 short horizontal marks (the marker `"_"`) at its eigenvalues, above its number; the colours alternate between blue and green, and $B$ is drawn in orange at position 42. Figure 3 of Notebook 10e shows for every sample marks above and below the grey zero line in mirror-image positions: eigenvalues in pairs $\pm\lambda$, eight of each sign, as Section 10.33 proved.

**In [6], which generators keep the canonical rule.**

```python
kinds = {}
for (a, b), s in S.items():
    anti_hermitian = np.array_equal(s.conj().T, -s)
    commutes = np.allclose(B @ s, s @ B)
    krein = np.allclose(s.conj().T @ B + B @ s, 0)
    kinds[(a, b)] = (anti_hermitian, commutes, krein)
```

For each generator three truth values are stored: anti-Hermitian ($S^\dagger = -S$), commuting with $B$, and the Krein condition $S^\dagger B + BS = 0$ (Section 10.34).

```python
counts = {"anti-Hermitian (unitary)": sum(k[0] for k in kinds.values()),
          "commute with B": sum(k[1] for k in kinds.values()),
          "Krein-unitary": sum(k[2] for k in kinds.values()),
          "both unitary and Krein-unitary": sum(k[0] and k[2] for k in kinds.values())}
for label, number in counts.items():
    report(label, number)
```

Summing truth values counts the true ones (`True` counts as 1). The RESULT lines print 12 anti-Hermitian generators, 13 that commute with $B$, 21 Krein-unitary ones and 9 that are both: the counts derived in Section 10.34.

```python
krein_pairs = sorted(pair for pair, k in kinds.items() if k[2])
off_x4 = sorted(pair for pair in pairs if 4 not in pair)
x4_ok = True
for (a, b), s in S.items():
    if 4 in (a, b):
        other = b if a == 4 else a
        s_x4_first = s if a == 4 else -s  # S^(x4 b) = -S^(b x4)
        left = s_x4_first.conj().T @ B + B @ s_x4_first
        x4_ok = x4_ok and np.allclose(left, 1j * C @ gamma[other])
```

`krein_pairs` is the sorted list of the Krein-unitary pairs, `off_x4` the sorted list of the pairs without the direction 4. For each of the 7 pairs that contain 4, the generator is written with $x_4$ first ($S^{ab} = -S^{ba}$, so for the pairs $(1, 4)$, $(2, 4)$, $(3, 4)$ the sign is reversed), and the defect $S^\dagger B + BS$ is compared with $iC\gamma^{(x_b)}$, $b$ being the other direction.

```python
check_record(krein_pairs == off_x4 and len(krein_pairs) == 21 and x4_ok,
             "Krein-unitary: exactly the 21 generators without x4 (Spin(4,3))",
             record="Revision/algebra/reports/wolfram-algebra.json, check "
                    "S_preserves_B_only_off_x4")
check(counts["anti-Hermitian (unitary)"] == 12 and counts["commute with B"] == 13
      and counts["both unitary and Krein-unitary"] == 9,
      "counts: 12 anti-Hermitian, 13 commute with B, 9 both unitary and Krein")
```

The first check reproduces the record check `S_preserves_B_only_off_x4`: the Krein-unitary generators are exactly the 21 without $x_4$, and the 7 with $x_4$ have the defect $iC\gamma^{(x_b)}$. The second confirms the counts. Two PASS lines.

**In [7], the 28 generators as a picture.**

```python
grid = np.full((8, 8), np.nan)  # NaN: no generator (diagonal and below)
for (a, b), (anti_hermitian, _, krein) in kinds.items():
    grid[a - 1, b - 1] = 0 if (anti_hermitian and krein) else (1 if krein else 2)
colours = ListedColormap([BLUE, GREEN, ORANGE])
fig, ax = plt.subplots(figsize=(6.0, 5.4))
ax.imshow(grid, cmap=colours, vmin=-0.5, vmax=2.5)
```

An $8 \times 8$ table, empty (NaN, drawn white) on and below the diagonal; above it, the square of row $a$ and column $b$ gets 0 for a generator that is unitary and Krein-unitary, 1 for Krein-unitary only, 2 otherwise. `ListedColormap` is a colour scale of three fixed colours; with the range from $-0.5$ to $2.5$ the values 0, 1 and 2 fall into its three thirds: blue, green and orange.

```python
names = [f"$x_{a}$" for a in range(1, 9)]
ax.set_xticks(range(8), names)
ax.set_yticks(range(8), names)
ax.grid(False)
for (a, b), (anti_hermitian, _, krein) in kinds.items():
    mark = "rot" if anti_hermitian else "boost"  # a rotation or a boost
    ax.text(b - 1, a - 1, mark, ha="center", va="center", color="white", fontsize=7)
```

The rows and columns are labelled $x_1$ to $x_8$, and each square gets the word `rot` (an anti-Hermitian generator, a rotation) or `boost` (a Hermitian one), written in white at its centre.

```python
ax.plot([], [], "s", color=BLUE, label="unitary and Krein-unitary (9)")
ax.plot([], [], "s", color=GREEN, label="Krein-unitary only (12)")
ax.plot([], [], "s", color=ORANGE, label="breaks the anticommutator (7)")
ax.legend(loc="lower left", fontsize=8)
ax.set_xlabel("second direction $b$")
ax.set_ylabel("first direction $a$")
ax.set_title("The 28 generators $S^{ab}$ and the canonical anticommutator")
save_figure(fig, "generator_types",
...)
```

Empty plots with square markers create the three legend entries, placed in the empty lower left corner. Figure 4 of Notebook 10e shows the column and the row of $x_4$ orange (the 7 generators that break the canonical rule), blue rotations among $x_1, x_2, x_3$ and $x_8$ and among $x_5, x_6, x_7$, and green boosts between those two groups.

**In [8], finite rotations and boosts.**

```python
def spin_transformation(a, b, theta):
    s = S[(a, b)]
    if eta[a] * eta[b] == 1:  # a rotation
        return np.cos(theta / 2) * I16 + 2 * np.sin(theta / 2) * s
    return np.cosh(theta / 2) * I16 + 2 * np.sinh(theta / 2) * s  # a boost


def series_exponential(matrix, terms=30):
    result, power = np.eye(16), np.eye(16)
    for n in range(1, terms + 1):
        power = power @ matrix / n
        result = result + power
    return result
```

`spin_transformation` is the closed formula of Section 10.34; `series_exponential` sums the power series $\sum_{n=0}^{30}X^n/n!$ directly (each pass multiplies the previous term by $X/n$, so `power` is $X^n/n!$).

```python
worst = max(np.max(np.abs(spin_transformation(a, b, 0.7)
                          - series_exponential(0.7 * S[(a, b)]))) for a, b in pairs)
report("largest difference between the formula and the series", f"{worst:.1e}")
check(worst < 1e-12, "the closed formula for exp(theta S^ab) is right for all 28")
```

For $\theta = 0.7$ and all 28 generators the two agree to $6.7 \times 10^{-16}$, printed as `6.7e-16`.

```python
u = ((I16 + B) / 2)[:, 0]  # a column with B u = u
u = u / np.linalg.norm(u)
thetas = np.linspace(-3.0, 3.0, 241)
curves = {}
for pair in ((1, 2), (1, 5), (1, 4)):
    lengths, kreins = [], []
    for theta in thetas:
        v = spin_transformation(*pair, theta) @ u
        lengths.append((v.conj() @ v).real)
        kreins.append((v.conj() @ B @ v).real)
    curves[pair] = (np.array(lengths), np.array(kreins))
```

A column $u$ with $Bu = u$ and length 1 (so its Krein norm is 1) is transformed by the rotation $S^{(x_1x_2)}$, the boost $S^{(x_1x_5)}$ and the boost $S^{(x_1x_4)}$ for 241 values of $\theta$ from $-3$ to 3, and its ordinary squared length and its Krein norm are stored. `spin_transformation(*pair, theta)` passes the two numbers of the pair as the first two arguments.

```python
kept = {pair: np.max(np.abs(curves[pair][1] - 1)) < 1e-12 for pair in curves}
say(f"Krein norm kept: rotation x1x2 {kept[(1, 2)]}, boost x1x5 {kept[(1, 5)]}, "
    f"boost x1x4 {kept[(1, 4)]}")
check(kept[(1, 2)] and kept[(1, 5)] and not kept[(1, 4)]
      and np.max(np.abs(curves[(1, 2)][0] - 1)) < 1e-12,
      "finite: the rotation keeps both norms, the x1x5 boost only the Krein norm")
```

The printed line shows that the Krein norm is kept by the rotation and the $x_1x_5$ boost (`True`) but not by the $x_1x_4$ boost (`False`); the check also requires the rotation to keep the ordinary length. Two PASS lines in the cell.

**In [9], the two norms in a picture.**

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), sharex=True)
styles = {(1, 2): (BLUE, "-", "rotation $S^{(x_1x_2)}$"),
          (1, 5): (GREEN, "--", "boost $S^{(x_1x_5)}$"),
          (1, 4): (ORANGE, ":", "boost $S^{(x_1x_4)}$")}
for pair, (colour, style, label) in styles.items():
    axes[0].plot(thetas, curves[pair][0], style, color=colour, linewidth=2,
                 label=label)
    axes[1].plot(thetas, curves[pair][1], style, color=colour, linewidth=2,
                 label=label)
```

Each transformation gets a colour, a line style (solid, dashed, dotted) and a label; the left panel draws the ordinary squared lengths $(Ru)^\dagger(Ru)$, the right panel the Krein norms.

```python
axes[0].set_ylabel("squared length $(Ru)^\\dagger(Ru)$")
axes[1].set_ylabel("Krein norm $(Ru)^\\dagger B (Ru)$")
for ax in axes:
    ax.set_xlabel("angle or rapidity $\\theta$")
    ax.legend(fontsize=8)
axes[0].set_title("unitary: only the rotation keeps the length")
axes[1].set_title("Krein-unitary: the rotation and the $x_1x_5$ boost")
save_figure(fig, "finite_transformations",
...)
```

Figure 5 of Notebook 10e shows on the left the rotation flat at 1 while both boosts rise ($\cosh\theta$ for the $x_1x_5$ boost, Section 10.34), and on the right the rotation and the $x_1x_5$ boost flat at 1 while the $x_1x_4$ boost moves away: a boost between a space direction and an extra time keeps the canonical rule, a boost that involves the time $x_4$ does not.

**In [10], the last check.**

```python
for name in ("10e_1_invariant_forms.png", "10e_2_singular_values.png",
             "10e_3_density_eigenvalues.png", "10e_4_generator_types.png",
             "10e_5_finite_transformations.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The five figure files exist, and the last line prints ALL 15 CHECKS PASSED (notebook 10e): the five figure checks and the 10 checks of the cells before (1 in In [2], 3 in In [3], 2 each in In [5], In [6] and In [8]).

### 10.39 The Krein structure along the deflating history

Sections 10.3 to 10.6 studied waves with momenta that do not change. In the author's metric they DO change: the three extra times $x_5, x_6, x_7$ deflate exponentially (scale factor $e^{-a_4}\sin^{1/6}z$, with $a_4$ increasing), and 3-space inflates (scale factor $e^{a_4}\sin^{1/6}z$). This section follows the one-particle structure of the chapter along the deflating history that the Kohn-Sham record uses.

**The history and its status.** The Kohn-Sham record takes the linear history

$$
a_4 = AHx_4,\qquad A = H = m = 1
$$

(record `Revision/kohn_sham/results/parameters.json`, entries `physics.historyA`, `physics.H`, `physics.m`; its slices are $a_{4,0} = 0, 0.5, 1, 1.5, 2$). This history is a PRESCRIBED BACKGROUND: it is not solved from the field equations for $a_4$ with this field as the source, and the Kohn-Sham states violate the source conditions that the linear member requires (`Revision/field_equations_a4/reports/ks-source-conditions.json`, check `ks_history_is_a_prescribed_background`; Chapter 17). Every statement of this section is made under this ASSUMPTION.

**The local-frame model.** At each instant $x_4$ and at one hidden position, the coefficients of the wave equation are evaluated there and the two hidden-direction terms of Section 10.27 are left out; this is the *local-frame* (WKB-type) statement of the Revision record that "every extra-time mode eventually enters the growing regime" (`python-field-theory.json`, check `extra_time_modes_grow`). The model is an ASSUMPTION; the extra times are never treated as static: their scale factor changes at every instant. The Kohn-Sham record measures the hidden direction by $y = \ln(\sin z)/(6H)$, so that

$$
\sin^{1/6}z = e^{\ln(\sin z)/6} = e^{Hy},
$$

the patch end $z = \pi/2$ is $y = 0$, and $y < 0$ lies towards the tip.

**The wave equation of one instant, line by line.** Take a wave $\Psi = u(x_4)\,e^{i(q_1x_1 + q_5x_5)}$ with the **coordinate momenta** $q_1$ (along 3-space) and $q_5$ (along an extra time). In the field equation of Section 10.27 the derivative $\partial_1$ becomes $iq_1$ and $\partial_5$ becomes $iq_5$, each divided by its scale factor:

$$
ik_1\gamma^{(x_1)}u + \gamma^{(x_4)}\frac{du}{dx_4} + ik_5\gamma^{(x_5)}u = mu,
$$

with the frame momenta

$$
k_1 = \frac{q_1}{e^{a_4}\sin^{1/6}z} = q_1e^{-AHx_4 - Hy},\qquad k_5 = \frac{q_5}{e^{-a_4}\sin^{1/6}z} = q_5e^{AHx_4 - Hy} .
$$

The **frame momentum** $k_1$ SHRINKS as 3-space inflates; $k_5$ GROWS as the extra times deflate. The steps of Section 10.3 (multiply by $\gamma^{(x_4)}$, solve for $du/dx_4$, multiply by $i$) give

$$
i\frac{du}{dx_4} = h(x_4)\,u,\qquad h(x_4) = -im\gamma^{(x_4)} - k_1(x_4)\,\gamma^{(x_4)}\gamma^{(x_1)} - k_5(x_4)\,\gamma^{(x_4)}\gamma^{(x_5)} .
$$

At every instant this is a mode Hamiltonian of Section 10.3 with real frame momenta, so by Section 10.4

$$
h(x_4)^2 = w(x_4)^2I_{16},\qquad w(x_4)^2 = m^2 + k_1^2 - k_5^2 = m^2 + q_1^2e^{-2AHx_4 - 2Hy} - q_5^2e^{2AHx_4 - 2Hy} .
$$

For $A > 0$ the second term falls and the third grows, so $w^2$ falls all the time, and if $q_5 \neq 0$ it becomes negative after a finite time: every wave with an extra-time momentum eventually grows.

**The onset time, line by line.** Write $X = e^{2AHx_4} > 0$ and $c = e^{-2Hy} > 0$. Then $e^{-2AHx_4 - 2Hy} = c/X$ and $e^{2AHx_4 - 2Hy} = cX$, and the condition $w^2 = 0$ reads

$$
m^2 + q_1^2\,\frac{c}{X} - q_5^2\,cX = 0 .
$$

Multiply by $-X$ (which is not 0):

$$
q_5^2c\,X^2 - m^2X - q_1^2c = 0 .
$$

This is a quadratic equation $aX^2 + bX + d = 0$ with $a = q_5^2c$, $b = -m^2$, $d = -q_1^2c$; its roots are $X = (-b \pm \sqrt{b^2 - 4ad})/(2a)$, here $(m^2 \pm \sqrt{m^4 + 4q_1^2q_5^2c^2})/(2q_5^2c)$. The square root is at least $m^2$, so the root with the minus sign is negative (or 0 when $q_1 = 0$), while $X = e^{2AHx_4}$ is positive. The only possible root is

$$
X^\ast = \frac{m^2 + \sqrt{m^4 + 4q_1^2q_5^2c^2}}{2q_5^2c},\qquad x_4^\ast = \frac{\ln X^\ast}{2AH},
$$

the **onset time**, by taking the logarithm of $X^\ast = e^{2AHx_4^\ast}$. Before $x_4^\ast$ the frequency is real (the wave oscillates); after it, it is imaginary (the wave grows). For $q_1 = 0$ and $y = 0$ ($c = 1$): $X^\ast = 2m^2/(2q_5^2) = m^2/q_5^2$ and $x_4^\ast = \ln(m/q_5)/(AH)$: the onset comes when the growing frame momentum $k_5 = q_5e^{AHx_4}$ reaches the mass. With $A = H = m = 1$ and $q_5 = 0.05$ this is $\ln 20 \approx 2.996$; Notebook 10f computes the onset of the wave $q_1 = 0.5$, $q_5 = 0.05$, $y = 0$ as 2.996044. The record's exact sample "$m = 1$, $k_5 = 2$: eigenvalues $\pm i\sqrt3$" is an instant of this history: the wave $q_1 = 0$, $q_5 = 0.05$ has $k_5 = 0.05\,e^{x_4} = 2$ at $x_4 = \ln 40$.

**How far from Hermitian, line by line.** By Section 10.4, $-i\gamma^{(x_4)}$ and $\gamma^{(x_4)}\gamma^{(x_1)}$ are Hermitian and commute with $B$, while $\gamma^{(x_4)}\gamma^{(x_5)}$ is anti-Hermitian and anticommutes with $B$. So $h = h_H + h_A$ with the anti-Hermitian part

$$
h_A = -k_5\,\gamma^{(x_4)}\gamma^{(x_5)},
$$

$$
h_A^\dagger h_A = -h_Ah_A = -k_5^2(\gamma^{(x_4)}\gamma^{(x_5)})^2 = -k_5^2\big(-\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_5)}\gamma^{(x_5)}\big) = k_5^2I_{16} .
$$

The steps: $h_A^\dagger = -h_A$; the square of the product; exchanging the middle factors costs a sign; $\gamma^{(x_4)}\gamma^{(x_4)} = \gamma^{(x_5)}\gamma^{(x_5)} = -I_{16}$. The **size** of a matrix (the largest factor by which it stretches the length of a column) is therefore exactly $k_5$ for $h_A$: $\lVert h_Au\rVert^2 = u^\dagger h_A^\dagger h_Au = k_5^2\,u^\dagger u$. In the same way $Bh - hB = Bh_A - h_AB = 2Bh_A$ ($h_H$ commutes with $B$, $h_A$ anticommutes) has the size $2k_5$, because $B$ keeps lengths ($B^\dagger B = BB = I_{16}$). Both sizes grow like $e^{a_4}$: the deflation drives every wave with extra-time momentum ever further from a Hermitian evolution that keeps the two eigenspaces of $B$ apart. Both vanish at every time in the good sector, $q_5 = 0$.

**Krein inertia at every instant.** At each instant Theorem 10.1 applies: while $w^2 > 0$ each eigenspace of $h(x_4)$ has the Krein inertia $(4, 4)$; once $w^2 < 0$ each is Krein-neutral. The wave crosses from the first kind to the second at the onset time. For the band of waves with $q_1 = 0.5$ and $10^{-3} \leq q_5 \leq 1$ the onset times run from $6.9078$ (for $q_5 = 10^{-3}$) down to $0.0941$ (for $q_5 = 1$): as time goes on, smaller and smaller extra-time momenta cross into the growing, Krein-neutral regime, and only the good sector keeps real frequencies for ever.

**The good sector along the history.** For $q_5 = 0$ the mode Hamiltonian is Hermitian and commutes with $B$ at every time, with the energies

$$
\pm E(x_4),\qquad E(x_4) = \sqrt{m^2 + k_1^2} = \sqrt{m^2 + q_1^2e^{-2AHx_4 - 2Hy}},
$$

which fall towards $m$ as 3-space inflates. At each instant the positive Fock space of Section 10.20 can be built with the coefficients of that instant (an **instantaneous** Fock space): the filled sea has the value $-8E(x_4)$, and every particle and antiparticle the energy $+E(x_4) > 0$. For example, for $q_1 = 1$ and $y = 0$, $E = \sqrt2 = 1.414214$ at $a_{4,0} = 0$ and $E = \sqrt{1 + e^{-4}} = 1.009116$ at $a_{4,0} = 2$. Whether the instantaneous vacuum of one time contains quanta of a later time (the evolution of the quantum state through the changing background) is not computed: OPEN.

**The universes of masses $+m$ and $-m$ along the history.** At every instant $\Gamma h_m(x_4)\Gamma = h_{-m}(x_4)$ (Section 10.6; $\Gamma$ anticommutes with $\gamma^{(x_4)}$ and commutes with $\gamma^{(x_4)}\gamma^{(x_1)}$ and $\gamma^{(x_4)}\gamma^{(x_5)}$), and $w^2$ contains the mass only as $m^2$: the two universes have the same frequencies, the same onset times and the same Krein inertia at every instant.

| statement | status | where it is verified |
| --- | --- | --- |
| the history $a_4 = AHx_4$, $A = H = m = 1$ | ASSUMED (PRESCRIBED BACKGROUND) | `parameters.json`; `ks-source-conditions.json`, check `ks_history_is_a_prescribed_background` |
| the scale factors $e^{\pm a_4}\sin^{1/6}z$, 1, $\cot z$ | from the record | `Revision/theory/field-theory.json`, formula `vielbein_diagonal` |
| local-frame model (coefficients of one instant and position, no hidden-direction terms) | ASSUMED | `python-field-theory.json`, check `extra_time_modes_grow` (a local-frame statement) |
| $h(x_4)^2 = w(x_4)^2I_{16}$; $\lVert h_A\rVert = k_5$, $\lVert Bh - hB\rVert = 2k_5$; good sector Hermitian at all times | PROVED (exact, every instant) | Notebook 10f, In [4]; `python-field-theory.json`, check `good_sector_spectrum_and_B_sectors` |
| every wave with $q_5 \neq 0$ reaches the onset $x_4^\ast = \ln X^\ast/(2AH)$ | PROVED (above) | Notebook 10f, In [6] (agreement with bisection $8.9 \times 10^{-16}$) |
| onset 2.996044 for $q_1 = 0.5$, $q_5 = 0.05$; inertia $(4, 4)$ before, neutral after; onset map | COMPUTED | Notebook 10f, In [6], In [9], In [10]; `python-pairing.json`, checks `Q.one_particle_Krein_inertia_proof` and `Q.one_particle_complex_frequency_Krein_neutral` |
| instantaneous good-sector Fock space: sea $-8E(x_4)$, quanta $+E(x_4)$ | COMPUTED at the five slices | Notebook 10f, In [11] |
| evolution of the quantum state through the background; a positive state space for the extra-time sector | OPEN | not computed in the Revision record |

### 10.40 Example: Notebook 10f follows the Krein structure along the deflating history

Notebook 10f reads the history and the scale factors from the Revision records, proves the identities of Section 10.39 exactly for every instant, compares the sizes of $h_A$ and $Bh - hB$ with $k_5$ and $2k_5$, computes the onset time and checks it against a numerical root search for 48 waves, places the record's sample $k_5 = 2$ at $x_4 = \ln 40$, follows the eigenvalues and the Krein inertia of one wave through its onset, maps which waves still oscillate at which time, builds the instantaneous good-sector Fock space at the five slices of the Kohn-Sham record, and checks the masses $+m$ and $-m$ at every time. It draws five figures and ends with the line ALL 19 CHECKS PASSED (notebook 10f).

<!-- NOTEBOOK 10f -->

### 10.43 Line-by-line walk-through of Notebook 10f

The notebook has 13 code cells, In [1] to In [13]; docstrings are left out of the quotations (they are printed in Section 10.42).

**In [1], the set-up cell.** Its first 252 lines are comments that repeat the run instructions of Section 10.41. The code is that of In [1] of Notebook 10a (Section 10.10), with the line `NOTEBOOK_ID = "10f"  # this notebook: chapter 10, example f`. It prints `Set-up of notebook 10f complete: repository folder found, helpers defined.`

**In [2], the deflating history of the Revision record.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer
import sys  # the screen output, sys.stdout

import numpy as np  # numbers, arrays and matrices
import sympy as sp  # exact algebra with symbols


REPORT_CHECKS = {}  # report file -> {check name: verdict}; each file is read once


def record_says_pass(record):
    path, separator, check_name = record.partition(", check ")
    if not separator:  # a data entry of a record file that the notebook reads itself
        return True
    if path not in REPORT_CHECKS:
        checks = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
        REPORT_CHECKS[path] = {c["name"]: c["verdict"].upper() for c in checks}
    return REPORT_CHECKS[path].get(check_name) == "PASS"


def check_record(condition, name, record):
    if not record_says_pass(record):  # the cited check must exist and say PASS
        raise AssertionError("the cited record check is missing or not PASS: " + record)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
        check(condition, name, record=record)
    sys.stdout.write(buffer.getvalue())  # one single piece of output


BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
```

The imports, the helpers `REPORT_CHECKS`, `record_says_pass` and `check_record` of Section 10.10 (a cited report check must still exist with the verdict PASS; the two printed lines come in one piece), and the four colours.

```python
parameters = json.loads(repository_file(
    "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
H = parameters["physics"]["H"]  # the author's constant H
mass = parameters["physics"]["m"]  # the mass m
A = parameters["physics"]["historyA"]  # the history a4 = A H x4
slices = parameters["physics"]["slicesA4"]  # the values a4,0 of the record
```

The parameters of the Kohn-Sham record are read: the constant $H$, the mass $m$ (called `mass` here, because the letter `m` is kept free), the history constant $A$ and the list of the five slices $a_{4,0}$.

```python
say("status of the history: "
    + parameters["conventions"]["history"].split(": ")[0] + ".")
say(f"slices a4,0 of the Kohn-Sham record: {slices}")
check_record(A == 1.0 and H == 1.0 and mass == 1.0,
             "the deflating history a4 = A H x4 with A = 1, H = 1, m = 1",
             record="Revision/kohn_sham/results/parameters.json, physics.historyA, "
                    "physics.H, physics.m")
```

The record states the status of the history in a sentence that begins with `PRESCRIBED BACKGROUND:`; `.split(": ")` cuts the text at the first colon and blank (and at any later one), and `[0]` keeps the first piece. The printed lines are `status of the history: PRESCRIBED BACKGROUND.` and the slices `[0.0, 0.5, 1.0, 1.5, 2.0]`; the check confirms $A = H = m = 1$ and reproduces the three entries of the record.

```python
def a4_of(x4):
    return A * H * x4
```

`a4_of(x4)` is the prescribed history $a_4 = AHx_4$.

**In [3], frame momenta from the scale factors of the record.**

```python
theory = json.loads(repository_file("Revision/theory/field-theory.json").read_text(
    encoding="utf-8"))
text = next(f["wl"] for f in theory["formulas"] if f["key"] == "vielbein_diagonal")
a4_symbol, z_symbol = sp.symbols("a4 z", real=True)
```

The theory record holds a list of formulas, each a dictionary with a key and the formula as text in the Wolfram Language (entry `wl`). `next(...)` returns the first item of the generator expression in the parentheses: the text of the formula whose key is `vielbein_diagonal`, the eight scale factors. `a4_symbol` and `z_symbol` are two real sympy letters.

```python
translated = (text.replace("E^a4[x4]", "exp(a4)").replace("Sin[6*H*x8]", "sin(z)")
              .replace("Cot[6*H*x8]", "cot(z)").replace("^", "**")
              .replace("{", "[").replace("}", "]"))
f_record = sp.sympify(translated, locals={"a4": a4_symbol, "z": z_symbol})
```

The Wolfram text, for example `E^a4[x4]*Sin[6*H*x8]^(1/6)`, is translated step by step into sympy notation: $e^{a_4}$, $\sin z$ and $\cot z$ are written with the letters $a_4$ and $z$, `^` becomes `**` and the curly brackets of a Wolfram list become square brackets. `sp.sympify` reads the text as a list of eight exact expressions; `locals` tells it which letters to use.

```python
sixth_root = sp.sin(z_symbol) ** sp.Rational(1, 6)  # sin(z)^(1/6)
f_expected = ([sp.exp(a4_symbol) * sixth_root] * 3 + [sp.Integer(1)]
              + [sp.exp(-a4_symbol) * sixth_root] * 3 + [sp.cot(z_symbol)])
same = all(sp.simplify(r - e) == 0 for r, e in zip(f_record, f_expected))
say(f"scale factor of x1: {f_record[0]}")
say(f"scale factor of x5: {f_record[4]}")
check_record(len(f_record) == 8 and same,
             "the record's scale factors: e^a4 sin^(1/6) z (3-space), e^-a4 ... (x5-x7)",
             record="Revision/theory/field-theory.json, formula vielbein_diagonal")
```

`sp.Rational(1, 6)` is the exact fraction $\frac16$. The expected list is built by repeating and joining lists: three times $e^{a_4}\sin^{1/6}z$, then 1, three times $e^{-a_4}\sin^{1/6}z$, then $\cot z$. The comparison simplifies each difference to 0. The printed lines show the scale factors of $x_1$, `exp(a4)*sin(z)**(1/6)`, and of $x_5$, `exp(-a4)*sin(z)**(1/6)`: the extra times deflate exponentially as $a_4$ grows. The check reproduces the record's formula.

```python
def frame_momenta(x4, q1, q5, y):
    root = np.exp(H * y)  # sin(z)^(1/6) = e^(H y)
    k1 = q1 / (np.exp(a4_of(x4)) * root)  # q1 / f_1: shrinks, 3-space inflates
    k5 = q5 / (np.exp(-a4_of(x4)) * root)  # q5 / f_5: grows, extra times deflate
    return k1, k5
```

The frame momenta of Section 10.39: $k_1 = q_1/(e^{a_4}e^{Hy})$ and $k_5 = q_5/(e^{-a_4}e^{Hy})$, with $\sin^{1/6}z = e^{Hy}$.

**In [4], the mode Hamiltonian of each instant, exactly.**

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
    encoding="utf-8"))
gamma = {a: np.array(fixture["gamma"][a - 1], dtype=float) for a in range(1, 9)}
C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]  # the author's sigma16
B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4)
Gamma = (gamma[8] @ gamma[1] @ gamma[2] @ gamma[3] @ gamma[4] @ gamma[5]
         @ gamma[6] @ gamma[7])  # the chirality matrix
```

The gammas of the record as decimal numbers, $C$, $B$ and the chirality $\Gamma$.

```python
def mode_hamiltonian(x4, q1, q5, y, m=mass):
    k1, k5 = frame_momenta(x4, q1, q5, y)
    return (-1j * m * gamma[4] - k1 * (gamma[4] @ gamma[1])
            - k5 * (gamma[4] @ gamma[5]))


def w_squared(x4, q1, q5, y, m=mass):
    k1, k5 = frame_momenta(x4, q1, q5, y)
    return m ** 2 + k1 ** 2 - k5 ** 2
```

The mode Hamiltonian $h(x_4)$ of Section 10.39 and its squared frequency $w^2 = m^2 + k_1^2 - k_5^2$. The argument `m=mass` has a **default value**: when the call does not name `m`, the mass of the record is used.

```python
g = {a: sp.Matrix(fixture["gamma"][a - 1]) for a in range(1, 9)}  # exact gammas
B_exact = -sp.I * g[8] * g[1] * g[2] * g[3] * g[4]
m_s, q1_s, q5_s, y_s = sp.symbols("m q1 q5 y", real=True)
x4_s, H_s = sp.symbols("x4 H", positive=True)
a4_s = A * H_s * x4_s  # the history, with the record's A = 1
k1_s = q1_s * sp.exp(-a4_s - H_s * y_s)  # frame momentum along x1
k5_s = q5_s * sp.exp(a4_s - H_s * y_s)  # frame momentum along x5
h_s = -sp.I * m_s * g[4] - k1_s * g[4] * g[1] - k5_s * g[4] * g[5]
zero = sp.zeros(16, 16)
```

The same objects exactly: letters for $m$, $q_1$, $q_5$, $y$ (real) and $x_4$, $H$ (positive), the history, the frame momenta $k_1 = q_1e^{-a_4 - Hy}$ and $k_5 = q_5e^{a_4 - Hy}$, and the exact $h(x_4)$. A statement about these letters holds at every instant and every position.

```python
w2_s = m_s ** 2 + k1_s ** 2 - k5_s ** 2
square_ok = (h_s * h_s - w2_s * sp.eye(16)).applyfunc(sp.expand) == zero
h_A = ((h_s - h_s.H) / 2).applyfunc(sp.expand)  # the anti-Hermitian part
part_ok = (h_A + k5_s * g[4] * g[5]).applyfunc(sp.expand) == zero
size_ok = (h_A.H * h_A - k5_s ** 2 * sp.eye(16)).applyfunc(sp.expand) == zero
mixing_ok = (B_exact * h_s - h_s * B_exact - 2 * B_exact * h_A).applyfunc(
    sp.expand) == zero
```

The identities of Section 10.39: $h^2 = w^2I_{16}$; the anti-Hermitian part $h_A = \frac12(h - h^\dagger)$ equals $-k_5\gamma^{(x_4)}\gamma^{(x_5)}$; $h_A^\dagger h_A = k_5^2I_{16}$; and $Bh - hB = 2Bh_A$.

```python
good = h_s.subs(q5_s, 0)  # the good sector
good_ok = ((good - good.H).applyfunc(sp.expand) == zero
           and (B_exact * good - good * B_exact).applyfunc(sp.expand) == zero)
check(square_ok, "exact: h(x4)^2 = (m^2 + k1^2 - k5^2) I at every instant")
check(part_ok and size_ok and mixing_ok,
      "exact: h_A = -k5 g4 g5, h_A^dagger h_A = k5^2 I, B h - h B = 2 B h_A")
check_record(good_ok,
             "exact: good sector, h(x4) Hermitian and commuting with B at all times",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "good_sector_spectrum_and_B_sectors")
```

With $q_5 = 0$ the matrix must be Hermitian and commute with $B$ at all times. Three PASS lines; the third reproduces the record check `good_sector_spectrum_and_B_sectors`.

**In [5], the departure from Hermiticity and the mixing of the two sectors of $B$.**

```python
times = np.linspace(0.0, 6.0, 13)  # 0, 0.5, ..., 6
curve_times = np.linspace(0.0, 6.0, 241)
measured, worst = {}, 0.0
for q5 in (0.01, 0.05, 0.2):
    sizes = []
    for x4 in times:
        h = mode_hamiltonian(x4, 0.5, q5, 0.0)
        h_anti = (h - h.conj().T) / 2
        sizes.append((np.linalg.norm(h_anti, 2), np.linalg.norm(B @ h - h @ B, 2)))
```

For three extra-time momenta $q_5 = 0.01, 0.05, 0.2$ (with $q_1 = 0.5$ and $y = 0$) and 13 times from 0 to 6, the cell measures the size of the anti-Hermitian part and of the commutator $Bh - hB$; `np.linalg.norm(M, 2)` is the size of a matrix (its largest stretching factor).

```python
        k5 = frame_momenta(x4, 0.5, q5, 0.0)[1]
        worst = max(worst, abs(sizes[-1][0] - k5) / k5,
                    abs(sizes[-1][1] - 2 * k5) / (2 * k5))
    measured[q5] = np.array(sizes)
good_sizes = [np.linalg.norm(mode_hamiltonian(x4, 0.5, 0.0, 0.0)
                             - mode_hamiltonian(x4, 0.5, 0.0, 0.0).conj().T, 2)
              for x4 in times]
report("largest relative difference from k5 and 2 k5", f"{worst:.1e}")
check(worst < 1e-12 and max(good_sizes) == 0.0,
      "sizes of h_A and of B h - h B are k5 = q5 e^a4 and 2 k5; zero if q5 = 0")
```

The measured sizes are compared with $k_5$ and $2k_5$ (`sizes[-1]` is the pair just appended; `[1]` of the frame momenta is $k_5$), and in the good sector the size of $h - h^\dagger$ must be exactly 0 at every time. The largest relative difference is printed as `0.0e+00`.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), sharey=True)
for q5, colour in ((0.01, BLUE), (0.05, ORANGE), (0.2, GREEN)):
    k5_curve = frame_momenta(curve_times, 0.5, q5, 0.0)[1]
    axes[0].plot(curve_times, k5_curve, color=colour, linewidth=2,
                 label=f"$q_5 = {q5}$")
    axes[0].plot(times, measured[q5][:, 0], "o", color=colour, markersize=5)
    axes[1].plot(curve_times, 2 * k5_curve, color=colour, linewidth=2,
                 label=f"$q_5 = {q5}$")
    axes[1].plot(times, measured[q5][:, 1], "o", color=colour, markersize=5)
```

For each $q_5$ the formulas $k_5$ and $2k_5$ are drawn as lines (`frame_momenta` works on the whole array of 241 times at once) and the measured sizes as dots.

```python
for ax in axes:
    ax.set_yscale("log")
    ax.axhline(mass, color=GREY, linestyle=":", linewidth=1)
    ax.set_xlabel("time $x_4$ (units of $1/m$)")
    ax.legend(loc="lower right", fontsize=8)
axes[0].set_ylabel("size (units of $m$)")
axes[0].set_title("anti-Hermitian part $h_A$: size $k_5 = q_5e^{a_4}$")
axes[1].set_title("mixing of the $B$ sectors: size of $Bh - hB$")
save_figure(fig, "hermiticity_defect",
...)
```

Logarithmic vertical axes (`set_yscale("log")`), on which an exponential is a straight line, and a dotted line at the mass. Figure 1 of Notebook 10f shows three parallel straight lines in each panel with the dots on them: the departure from Hermiticity and the mixing of the two sectors of $B$ grow like $e^{a_4}$, crossing the level of the mass sooner for larger $q_5$.

**In [6], the exact onset time.**

```python
def onset_time(q1, q5, y):
    c = np.exp(-2 * H * y)
    X = (mass ** 2 + np.sqrt(mass ** 4 + 4 * q1 ** 2 * q5 ** 2 * c ** 2)) / (
        2 * q5 ** 2 * c)
    return np.log(X) / (2 * A * H)
```

The formula $x_4^\ast = \ln X^\ast/(2AH)$ of Section 10.39, with $c = e^{-2Hy}$.

```python
def bisection(q1, q5, y, low=-40.0, high=40.0):
    for _ in range(200):
        middle = (low + high) / 2
        if w_squared(middle, q1, q5, y) > 0:  # still oscillating: the onset is later
            low = middle
        else:
            high = middle
    return (low + high) / 2
```

An independent numerical root search, **bisection**: the interval from $-40$ to 40 contains the onset; at its midpoint, if $w^2 > 0$ the wave still oscillates and the onset lies in the right half, otherwise in the left half; halving 200 times shrinks the interval far below the rounding level, and its midpoint is returned.

```python
worst = max(abs(onset_time(q1, q5, y) - bisection(q1, q5, y))
            for q1 in (0.0, 0.5, 1.0, 3.0) for q5 in (0.01, 0.05, 0.1, 0.4)
            for y in (0.0, -1.0, -3.0))
report("largest difference, exact onset time minus bisection (48 waves)",
       f"{worst:.1e}")
check(worst < 1e-12 and abs(onset_time(0.0, 0.05, 0.0) - np.log(1 / 0.05)) < 1e-14,
      "the exact onset time agrees with bisection; q1 = 0, y = 0: ln(m / q5)")
onset = onset_time(0.5, 0.05, 0.0)  # the wave followed below
report("onset time of the wave q1 = 0.5, q5 = 0.05, y = 0", f"{onset:.6f}")
```

For $4 \times 4 \times 3 = 48$ waves the formula and the bisection agree to `8.9e-16`; the check also confirms the short form $\ln(m/q_5) = \ln 20$ for $q_1 = 0$, $y = 0$. The onset time of the wave followed below is printed as `2.996044`.

**In [7], the recorded sample as an instant of the history.**

```python
instant = np.log(40.0)  # the time at which k5 = 0.05 e^x4 = 2
k5_instant = frame_momenta(instant, 0.0, 0.05, 0.0)[1]
eigenvalues = np.linalg.eigvals(mode_hamiltonian(instant, 0.0, 0.05, 0.0))
plus = int(np.sum(np.abs(eigenvalues - 1j * np.sqrt(3)) < 1e-9))
minus = int(np.sum(np.abs(eigenvalues + 1j * np.sqrt(3)) < 1e-9))
early = np.linalg.eigvals(mode_hamiltonian(0.0, 0.0, 0.05, 0.0))
```

At $x_4 = \ln 40$ the wave $q_1 = 0$, $q_5 = 0.05$, $y = 0$ has $k_5 = 0.05 \cdot 40 = 2$. The 16 eigenvalues of that instant are counted near $+i\sqrt3$ and near $-i\sqrt3$; `early` are the eigenvalues of the same wave at $x_4 = 0$, where $k_5 = 0.05$.

```python
report("frame momentum k5 at x4 = ln 40", f"{k5_instant:.12f}")
report("eigenvalues +i sqrt(3) and -i sqrt(3), how many", f"{plus} and {minus}")
largest_imaginary = np.max(np.abs(early.imag))  # 0 up to rounding: oscillation
report("largest imaginary part of an eigenvalue at x4 = 0", f"{largest_imaginary:.1e}")
check_record(abs(k5_instant - 2) < 1e-12 and (plus, minus) == (8, 8)
             and largest_imaginary < 1e-12,
             "the recorded sample m = 1, k5 = 2 (+-i sqrt 3) is reached at x4 = ln 40",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "extra_time_modes_grow")
```

The printed lines show $k_5 = 2.000000000000$, eight eigenvalues near each of $\pm i\sqrt3$, and at $x_4 = 0$ a largest imaginary part of `1.8e-16` (zero up to rounding: the wave still oscillates). The check reproduces the record check `extra_time_modes_grow` and places its sample on the deflating history.

**In [8], the eigenvalues of one wave through the onset.**

```python
scan_times = np.linspace(0.0, 5.0, 251)
real_parts, imaginary_parts, worst = [], [], 0.0
for x4 in scan_times:
    eigenvalues = np.linalg.eigvals(mode_hamiltonian(x4, 0.5, 0.05, 0.0))
    real_parts.append(np.sort(eigenvalues.real))
    imaginary_parts.append(np.sort(eigenvalues.imag))
    w2 = w_squared(x4, 0.5, 0.05, 0.0)
    if abs(w2) > 0.05:  # away from the onset
        w = np.sqrt(complex(w2))  # real, or i kappa after the onset
        predicted = np.array([w] * 8 + [-w] * 8)
        worst = max(worst,
                    np.max(np.abs(np.sort(eigenvalues.real) - np.sort(predicted.real))),
                    np.max(np.abs(np.sort(eigenvalues.imag) - np.sort(predicted.imag))))
report("largest difference from +-w(x4) away from the onset", f"{worst:.1e}")
check(worst < 1e-10, "at every instant the eigenvalues of h(x4) are +-w(x4), 8 each")
```

The loop of In [9] of Notebook 10a (Section 10.10), now along the history: for the wave $q_1 = 0.5$, $q_5 = 0.05$ at 251 times from 0 to 5 it computes the 16 eigenvalues of $h(x_4)$, stores their sorted real and imaginary parts, and, away from the onset (where the matrix cannot be diagonalised), compares them with $\pm w(x_4)$, eight each. The largest difference is printed as `8.0e-15`.

```python
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.0), sharex=True)
axes[0].plot(scan_times, np.array(real_parts), color=BLUE, linewidth=2)
axes[1].plot(scan_times, np.array(imaginary_parts), color=ORANGE, linewidth=2)
for ax, what in ((axes[0], "real part"), (axes[1], "imaginary part")):
    ax.axvline(onset, color=GREY, linestyle=":", linewidth=1)
    ax.set_xlabel("time $x_4$ (units of $1/m$)")
    ax.set_ylabel(f"{what} of the eigenvalues (units of $m$)")
axes[0].set_title("oscillation before the onset")
axes[1].set_title("growth after the onset")
save_figure(fig, "eigenvalues_along_history",
...)
```

The real parts (left) and imaginary parts (right) against the time, with a dotted line at the onset. Figure 2 of Notebook 10f shows the real frequencies $\pm w(x_4)$ closing in to 0 at $x_4^\ast = 2.996$ and the imaginary parts opening up after it, growing further as the extra-time frame momentum keeps growing: the picture of Figure 3 of Notebook 10a, now produced by the deflation itself.

**In [9], the Krein inertia of one wave along the history.**

```python
def orthonormal_basis(P):
    basis = []
    for column in P.T:
        v = column.astype(complex)
        for _ in range(2):  # the second pass removes rounding errors
            for e in basis:
                v = v - (e.conj() @ v) * e
        length = np.sqrt((v.conj() @ v).real)
        if length > 1e-8:
            basis.append(v / length)
    return np.array(basis).T
```

The Gram-Schmidt function of In [10] of Notebook 10a (Section 10.10).

```python
def eigenspace(h, w2, sign):
    w = np.sqrt(complex(w2))
    return orthonormal_basis((np.eye(16) + sign * h / w) / 2)


def krein_inertia(V):
    values = np.linalg.eigvalsh(V.conj().T @ B @ V)
    return (int(np.sum(values > 1e-8)), int(np.sum(values < -1e-8)),
            int(np.sum(np.abs(values) <= 1e-8)))
```

`eigenspace(h, w2, sign)` returns an orthonormal basis of the eigenspace of $\pm w$ (or $\pm i\kappa$) of a given matrix $h$, as the range of the projector $\frac12(I_{16} \pm h/w)$; `krein_inertia(V)` counts the positive, negative and zero eigenvalues of the Gram matrix $V^\dagger BV$ (Section 10.5), as in Notebook 10a.

```python
kept = [x4 for x4 in scan_times if abs(x4 - onset) > 0.03]
inertias = [krein_inertia(eigenspace(mode_hamiltonian(x4, 0.5, 0.05, 0.0),
                                     w_squared(x4, 0.5, 0.05, 0.0), +1))
            for x4 in kept]
before = {c for x4, c in zip(kept, inertias) if x4 < onset}
after = {c for x4, c in zip(kept, inertias) if x4 > onset}
say(f"inertia before the onset: {sorted(before)}; after the onset: {sorted(after)}")
```

The inertia of the $+w$ eigenspace at every time farther than 0.03 from the onset. `before` and `after` are the **sets** of the different inertias found before and after the onset (a set, written with braces, keeps each value once). The printed line shows `[(4, 4, 0)]` before and `[(0, 0, 8)]` after.

```python
check_record(before == {(4, 4, 0)},
             "every instant before the onset: inertia (4, 4) (real frequency)",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.one_particle_Krein_inertia_proof")
check_record(after == {(0, 0, 8)},
             "every instant after the onset: the eigenspace is Krein-neutral",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.one_particle_complex_frequency_Krein_neutral")
```

Two PASS lines, reproducing the record checks of Theorem 10.1 instant by instant.

```python
counts = np.array(inertias)
fig, ax = plt.subplots()
width = 0.0205  # a little wider than the step 0.02 between the times (no gaps)
ax.bar(kept, counts[:, 0], width=width, color=BLUE,
       label="positive charge $u^\\dagger B u > 0$")
ax.bar(kept, counts[:, 1], width=width, bottom=counts[:, 0], color=ORANGE,
       label="negative charge $u^\\dagger B u < 0$")
ax.bar(kept, counts[:, 2], width=width, bottom=counts[:, 0] + counts[:, 1],
       color=GREEN, label="neutral")
```

Stacked bars, as in In [14] of Notebook 10a: at each time a bar of height 8, split into its positive (blue), negative (orange) and neutral (green) directions.

```python
ax.axvline(onset, color=GREY, linestyle=":", linewidth=1)
ax.set_xlabel("time $x_4$ (units of $1/m$)")
ax.set_ylabel("directions in the $+w$ eigenspace")
ax.set_yticks(range(0, 9))
ax.set_ylim(0.0, 10.5)  # room for the legend above the bars
ax.set_title("Krein inertia of one wave along the deflating history")
ax.legend(loc="upper center", ncol=3, fontsize=8)
save_figure(fig, "inertia_along_history",
...)
```

Figure 3 of Notebook 10f shows half-blue, half-orange bars up to the onset time 2.996 and green bars after it: the deflation of the extra times moves the wave from the kind with inertia $(4, 4)$ to the Krein-neutral kind at a definite time.

**In [10], the onset map.**

```python
map_times = np.linspace(0.0, 6.0, 241)
exponents = np.linspace(-3.0, 0.0, 121)  # log10 of q5
q5_values = 10.0 ** exponents
real_frequency = np.array([[w_squared(x4, 0.5, q5, 0.0) > 0 for x4 in map_times]
                           for q5 in q5_values])  # rows: q5, columns: x4
onsets = np.array([onset_time(0.5, q5, 0.0) for q5 in q5_values])
agree = np.array_equal(real_frequency, map_times[None, :] < onsets[:, None])
```

A grid of 241 times from 0 to 6 and 121 momenta $q_5$ from $10^{-3}$ to 1, equally spaced in $\log_{10}q_5$ (`10.0 ** exponents`). `real_frequency` is a table of truth values, true where $w^2 > 0$. `onsets` holds the exact onset of each momentum, and `agree` compares the table with "the time lies before the onset": `map_times[None, :]` is a row and `onsets[:, None]` a column, and comparing them gives the whole table at once.

```python
sampled, sample_ok = 0, True
for i in range(0, 121, 4):
    for j in range(0, 241, 60):
        x4, q5 = map_times[j], q5_values[i]
        if abs(x4 - onsets[i]) < 0.05:
            continue  # too close to the onset
        w2 = w_squared(x4, 0.5, q5, 0.0)
        found = krein_inertia(eigenspace(mode_hamiltonian(x4, 0.5, q5, 0.0), w2, +1))
        sample_ok = sample_ok and found == ((4, 4, 0) if w2 > 0 else (0, 0, 8))
        sampled += 1
```

At every fourth momentum and every 60th time (`range(0, 121, 4)` counts in steps of 4) the Krein inertia is computed directly and compared with the prediction: $(4, 4, 0)$ for a real frequency, $(0, 0, 8)$ for an imaginary one; points closer than 0.05 to the onset are skipped (`continue` jumps to the next pass of the loop).

```python
report("grid points sampled for the inertia", sampled)
report("onset time for q5 = 0.001 and for q5 = 1",
       f"{onsets[0]:.4f} and {onsets[-1]:.4f}")
check(agree and sample_ok and np.all(np.isfinite(onsets)),
      "the map agrees with the exact onset; (4, 4) before it, neutral after it")
```

153 grid points are sampled; the onset times run from `6.9078` ($q_5 = 0.001$) to `0.0941` ($q_5 = 1$). The check requires the agreement, the sampled inertias, and a finite onset for every momentum (`np.isfinite`): no wave with extra-time momentum keeps a real frequency for ever.

```python
from matplotlib.colors import ListedColormap  # a colour scale with two colours

fig, ax = plt.subplots(figsize=(7.0, 4.8))
ax.pcolormesh(map_times, exponents, real_frequency.astype(float),
              cmap=ListedColormap(["#f6c9b5", "#bcd6f5"]), vmin=0, vmax=1,
              shading="nearest")
inside = onsets <= map_times[-1]  # the part of the onset curve inside the map
ax.plot(onsets[inside], exponents[inside], color=GREY, linewidth=2,
        label="onset time $x_4^\\ast$")
ax.set_xlim(map_times[0], map_times[-1])
```

`ax.pcolormesh` colours every grid cell by the table (`astype(float)` turns the truth values into 0 and 1): light orange for 0 (imaginary frequency) and light blue for 1 (real frequency); `shading="nearest"` centres each cell on its grid point. The grey curve is the exact onset time, drawn where it lies inside the map.

```python
for a4_slice in slices:
    ax.axvline(a4_slice / (A * H), color=GREEN, linestyle="--", linewidth=1)
ax.plot([], [], "--", color=GREEN, label="slices $a_{4,0}$ of the Kohn-Sham record")
ax.text(0.3, -1.9, "real frequency:\ninertia (4, 4)", color=BLUE, fontsize=9)
ax.text(4.4, -0.6, "imaginary frequency:\nKrein-neutral", color=ORANGE, fontsize=9)
ax.set_xlabel("time $x_4$ (units of $1/m$)")
ax.set_ylabel("$\\log_{10}$ of the extra-time momentum $q_5$")
ax.set_title("Which waves still oscillate? ($q_1 = 0.5$, $y = 0$)")
ax.legend(loc="lower left", fontsize=8)  # the lower left corner is all blue
ax.grid(False)
save_figure(fig, "onset_map",
...)
```

Green dashed lines mark the times $x_4 = a_{4,0}/(AH)$ of the five slices of the Kohn-Sham record; the two texts (with a line break written as a backslash and n) name the two regions. Figure 4 of Notebook 10f shows the blue region shrinking towards small $q_5$ as time goes on, bounded by the grey onset curve, which is nearly a straight line on this logarithmic scale (for small $q_5$, $x_4^\ast \approx \ln(1/q_5)$): the band of oscillating extra-time waves shrinks exponentially, and only the good sector $q_5 = 0$ stays blue for ever.

**In [11], the good sector along the history.**

```python
slice_ok, table = True, []
for q1 in (0.5, 1.0, 2.0, 4.0):
    for a4_slice in slices:
        x4 = a4_slice / (A * H)  # the time of the slice
        h = mode_hamiltonian(x4, q1, 0.0, 0.0)
        E = np.sqrt(w_squared(x4, q1, 0.0, 0.0))
        U_plus = eigenspace(h, E ** 2, +1)  # the 8 particle columns u_s
        V_minus = eigenspace(h, E ** 2, -1)  # the 8 antiparticle columns v_s
```

For four momenta $q_1 = 0.5, 1, 2, 4$ ($q_5 = 0$, $y = 0$) and the five slices, the cell builds the instantaneous good-sector waves: the energy $E(x_4) = \sqrt{w^2}$ and orthonormal bases of the eigenspaces of $+E$ (the particle columns) and $-E$ (the antiparticle columns).

```python
        sea = sum((v.conj() @ h @ v).real for v in V_minus.T)
        particle = [(u.conj() @ h @ u).real for u in U_plus.T]
        antiparticle = [-(v.conj() @ h @ v).real for v in V_minus.T]
```

The value of the filled sea, $\sum_sv_s^\dagger hv_s$ (each term is $-E$), and the normal-ordered energies of a particle, $u_s^\dagger hu_s$, and of an antiparticle, $-v_s^\dagger hv_s$ (Section 10.20).

```python
        slice_ok = (slice_ok and np.allclose(h, h.conj().T) and np.allclose(B @ h, h @ B)
                    and U_plus.shape[1] == 8 and V_minus.shape[1] == 8
                    and krein_inertia(U_plus) == (4, 4, 0)
                    and krein_inertia(V_minus) == (4, 4, 0)
                    and abs(sea + 8 * E) < 1e-12
                    and np.allclose(particle, E) and np.allclose(antiparticle, E))
        table.append((q1, a4_slice, E, sea))
```

At each slice: $h$ Hermitian, $Bh = hB$, eight columns in each eigenspace, Krein inertia $(4, 4)$ on both, the sea value $-8E$, and every quantum $+E$. A row of the table is kept for the printout and the figure.

```python
say("q1    a4,0    E(x4)      sea value -8E")
for q1, a4_slice, E, sea in table:
    if q1 in (1.0, 4.0):  # print two of the four momenta
        say(f"{q1:3.1f}   {a4_slice:3.1f}   {E:9.6f}   {sea:11.6f}")
check_record(slice_ok,
             "good sector at all 5 slices: Hermitian, [B, h] = 0, +-E, (4, 4), sea -8E",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "good_sector_spectrum_and_B_sectors")
```

The printed table shows, for $q_1 = 1$, the energies $1.414214$, $1.169564$, $1.065521$, $1.024591$, $1.009116$ at $a_{4,0} = 0, 0.5, 1, 1.5, 2$ (that is $\sqrt{1 + e^{-2a_{4,0}}}$), with the sea values $-8$ times these, from $-11.313708$ to $-8.072930$; and for $q_1 = 4$ the energies from $4.123106$ down to $1.137124$. The check reproduces the record check `good_sector_spectrum_and_B_sectors` at every slice.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
for q1, colour in ((0.5, BLUE), (1.0, ORANGE), (2.0, GREEN), (4.0, GREY)):
    E_curve = np.sqrt(w_squared(curve_times, q1, 0.0, 0.0))
    axes[0].plot(curve_times, E_curve, color=colour, linewidth=2, label=f"$q_1 = {q1}$")
    axes[1].plot(curve_times, -8 * E_curve, color=colour, linewidth=2,
                 label=f"$q_1 = {q1}$")
    dots = [(a4_slice, E, sea) for q, a4_slice, E, sea in table if q == q1]
    axes[0].plot([d[0] for d in dots], [d[1] for d in dots], "o", color=colour)
    axes[1].plot([d[0] for d in dots], [d[2] for d in dots], "o", color=colour)
```

For each momentum the curves $E(x_4)$ (left) and $-8E(x_4)$ (right) are drawn from the formula, and the values computed from the eigenvectors at the slices as dots (the time of a slice equals $a_{4,0}$, because $AH = 1$).

```python
axes[0].axhline(mass, color=GREY, linestyle=":", linewidth=1)
axes[1].axhline(-8 * mass, color=GREY, linestyle=":", linewidth=1)
axes[0].set_ylabel("energy $E(x_4)$ of one quantum (units of $m$)")
axes[1].set_ylabel("value $-8E(x_4)$ of the filled sea (units of $m$)")
axes[0].set_title("particles and antiparticles: $+E(x_4) > 0$")
axes[1].set_title("the instantaneous vacuum")
for ax in axes:
    ax.set_xlabel("time $x_4$ (units of $1/m$)")
    ax.legend(fontsize=8)
save_figure(fig, "good_sector_energies",
...)
```

Dotted lines at the limits $m$ and $-8m$. Figure 5 of Notebook 10f shows the four energy curves falling towards the mass as 3-space inflates (larger $q_1$ fall from higher), with the dots on them, and the sea values rising towards $-8m$: in the good sector every quantum has a positive energy at every time, and the inertia stays $(4, 4)$.

**In [12], the universes of masses $+m$ and $-m$ along the history.**

```python
pair_ok, worst = True, 0.0
for x4 in np.linspace(0.0, 6.0, 25):
    h_plus = mode_hamiltonian(x4, 0.5, 0.05, 0.0, m=mass)
    h_minus = mode_hamiltonian(x4, 0.5, 0.05, 0.0, m=-mass)
    pair_ok = pair_ok and np.allclose(Gamma @ h_plus @ Gamma, h_minus, atol=1e-14)
    values_plus = np.linalg.eigvals(h_plus)
    values_minus = np.linalg.eigvals(h_minus)
```

At 25 times from 0 to 6, for the wave $q_1 = 0.5$, $q_5 = 0.05$, the cell builds $h_m(x_4)$ and $h_{-m}(x_4)$ (the default mass is overridden with `m=-mass`), checks $\Gamma h_m\Gamma = h_{-m}$ to within $10^{-14}$ (`atol` is the allowed absolute difference), and computes both spectra.

```python
    # compare the sorted real parts and the sorted imaginary parts separately
    worst = max(worst,
                np.max(np.abs(np.sort(values_plus.real) - np.sort(values_minus.real))),
                np.max(np.abs(np.sort(values_plus.imag) - np.sort(values_minus.imag))))
report("largest difference of the eigenvalues for +m and -m", f"{worst:.1e}")
check_record(pair_ok and worst < 1e-9,
             "Gamma h_m(x4) Gamma = h_-m(x4) at every time: same spectra and onset",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.one_particle_maps")
```

The sorted real parts and imaginary parts are compared separately, as the comment says (the times include the onset region, where the eigenvalues are complex). The largest difference is printed as `7.1e-15`, and the check reproduces the record check `Q.one_particle_maps` along the whole history.

**In [13], the last check.**

```python
for name in ("10f_1_hermiticity_defect.png", "10f_2_eigenvalues_along_history.png",
             "10f_3_inertia_along_history.png", "10f_4_onset_map.png",
             "10f_5_good_sector_energies.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The five figure files exist, and the last line prints ALL 19 CHECKS PASSED (notebook 10f): the five figure checks and the 14 checks of the cells before (1 each in In [2], In [3], In [5] to In [8], In [10], In [11] and In [12], 3 in In [4] and 2 in In [9]).

### 10.44 The quantum reading of the pairing

The pairing theorem T1 of the Revision record (proved in Chapter 18) says that the chirality matrix maps every solution $\Psi$ of the field with mass $m$ and coupling $\lambda$ to a solution $\Gamma\Psi$ of the field with $-m$ and $-\lambda$, with the energy-momentum tensor and the current reversed: $\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$, $T \to -T$, $J \to -J$. Theorem T2 combines $\Gamma$ with a reflection; in the author's field it is the mirror $\gamma^{(x_8)}$ across the ASSUMED Z2 brane, and it pairs $(m, \lambda)$ with $(-m, \lambda)$ at equal energy. What do these maps mean once dirac16complex is QUANTISED? The Revision pairing record answers with five statements, the **quantum reading Q** (record `Revision/pairing/pairing-theory.json`, theorem entry `Q`; Revision proof document, section 6). This section derives them, in flat 4+4 space at one point with $U = 0$ (so $\lambda = 0$; the record states them for general $\lambda$).

**The hypotheses.** (HQ1) dirac16complex is canonically quantised with $x_4$ as the evolution time; the $x_4$-derivative kernel of its Lagrangian is $N = B$ and the canonical anticommutator is $\{\Psi, \Psi^\dagger\} = N^{-1} = B$ at one point (Section 10.12). (HQ2) dirac16complex00 is a classical field and has no quantum reading.

**Two sign rules.** $\Gamma$ anticommutes with every gamma, so moving it through a product of $n$ gammas costs $(-1)^n$; with $\Gamma\Gamma = I_{16}$:

$$
\Gamma C\Gamma = C\ (n = 4),\qquad \Gamma C\gamma^{(x_a)}\Gamma = -C\gamma^{(x_a)}\ (n = 5),\qquad \Gamma B\Gamma = -B\ (n = 5) .
$$

**The Lagrangian identity, line by line.** In flat space with $U = 0$, $\mathcal{L}_m[\Psi] = \frac12\sum_a(\Psi^\dagger C\gamma^{(x_a)}\partial_a\Psi - \partial_a\Psi^\dagger C\gamma^{(x_a)}\Psi) - m\Psi^\dagger C\Psi$. Insert $\Psi = \Gamma\chi$ and $\Psi^\dagger = \chi^\dagger\Gamma$ ($\Gamma$ is real and symmetric):

$$
\mathcal{L}_m[\Gamma\chi] = \tfrac12\sum_a\big(\chi^\dagger\Gamma C\gamma^{(x_a)}\Gamma\,\partial_a\chi - \partial_a\chi^\dagger\,\Gamma C\gamma^{(x_a)}\Gamma\chi\big) - m\,\chi^\dagger\Gamma C\Gamma\chi .
$$

The two sign rules turn this into

$$
\mathcal{L}_m[\Gamma\chi] = -\tfrac12\sum_a\big(\chi^\dagger C\gamma^{(x_a)}\partial_a\chi - \partial_a\chi^\dagger C\gamma^{(x_a)}\chi\big) - m\,\chi^\dagger C\chi .
$$

 Take the sign $-1$ out of both terms; the mass term becomes $+m\chi^\dagger C\chi = -(-m)\chi^\dagger C\chi$, so the bracket is the Lagrangian with the mass $-m$:

$$
\mathcal{L}_m[\Gamma\chi] = -\mathcal{L}_{-m}[\chi] .
$$

**(Q1) The chirality image carries the Krein metric $-B$.** By Section 10.15, $\{\Gamma\Psi, (\Gamma\Psi)^\dagger\} = \Gamma B\Gamma^\dagger = -B$. The image's own Lagrangian says the same: in $\mathcal{L}_m[\Gamma\chi] = -\mathcal{L}_{-m}[\chi]$ the time-derivative terms of the variable $\chi$ have the kernel $\Gamma B\Gamma = -B$, and canonical quantisation of $\chi$ gives $\{\chi, \chi^\dagger\} = (-B)^{-1} = -B$. The two agree.

**(Q2) The image is the same quantum system.** For one plane wave the energy is $H_m[\Psi] = \Psi^\dagger h'_m\Psi$ with $h'_m = mC - i\sum_ak_aC\gamma^{(x_a)}$ (Section 10.12), and the charge is $Q[\Psi] = \Psi^\dagger B\Psi$. By the sign rules,

$$
\Gamma h'_m\Gamma = mC + i\sum_ak_aC\gamma^{(x_a)} = -\Big((-m)C - i\sum_ak_aC\gamma^{(x_a)}\Big) = -h'_{-m} .
$$

Written in the image variable $\chi = \Gamma\Psi$ (so $\Psi = \Gamma\chi$),

$$
H_m[\Psi] = \chi^\dagger\Gamma h'_m\Gamma\chi = -\chi^\dagger h'_{-m}\chi = -H_{-m}[\Gamma\Psi],\qquad Q[\Psi] = \chi^\dagger\Gamma B\Gamma\chi = -Q[\Gamma\Psi] .
$$

The energy and the charge of the field are MINUS the energy and the charge that the mass $-m$ theory assigns to the image: $T \to -T$ and $J \to -J$ of T1 are identities between operators of ONE quantum system. The image is not a second universe with negative energy; it is the first universe written in other variables. Its motion agrees. In its own variable $\chi = \Gamma\Psi$ the image has the metric $-B$ (Q1) and, by the display above ($H_m[\Psi] = -\chi^\dagger h'_{-m}\chi$), the generator density $-h'_{-m}$; its one-particle generator is the product of the two, as in Section 10.12, so it evolves by

$$
(-B)(-h'_{-m}) = Bh'_{-m} = h_{-m} ,
$$

the wave equation of mass $-m$. Written back in the variable $\Psi = \Gamma\chi$, the same motion is $\Gamma h_{-m}\Gamma = (\Gamma B\Gamma)(\Gamma h'_{-m}\Gamma) = (-B)(-h'_m) = Bh'_m = h_m$ (insert $\Gamma\Gamma = I_{16}$ between the factors; $\Gamma h'_{-m}\Gamma = -h'_m$ is the identity $\Gamma h'_m\Gamma = -h'_{-m}$ with $m$ replaced by $-m$): the dynamics of $\Psi$ itself. The Revision record states the same identity in the other direction, for the image of a field of mass $-m$: that image carries the metric $-B$ and the generator density $-h'_m$ and evolves by $(-B)(-h'_m) = Bh'_m = h_m$, the dynamics of mass $m$ (`python-pairing.json`, check `Q.image_generators_same_dynamics`). In terms of the image field, $i\,\partial_4(\Gamma\Psi) = \Gamma h_m\Psi = (\Gamma h_m\Gamma)(\Gamma\Psi) = h_{-m}\Gamma\Psi$: the image obeys the wave equation of mass $-m$ and is moved by the SAME energy operator $H_m[\Psi]$.

**(Q3) An independent universe of mass $-m$, and no cancellation.** An independently quantised universe of mass $-m$ is a NEW field $\Psi_2$ with its own Lagrangian $\mathcal{L}_{-m}[\Psi_2]$. The mass does not enter the time-derivative kernel, so its kernel is $+B$ and $\{\Psi_2, \Psi_2^\dagger\} = +B$; being independent of the first universe $\Psi_1$, it anticommutes with it: $\{\Psi_{2A}, \Psi^\dagger_{1C}\} = 0$ and $\{\Psi_{2A}, \Psi_{1C}\} = 0$. The image $\Gamma\Psi_1$ fails both requirements: it carries $-B$, not $+B$, and $\{(\Gamma\Psi_1)_A, \Psi^\dagger_{1C}\} = \sum_D\Gamma_{AD}B_{DC} = (\Gamma B)_{AC}$, a matrix of rank 16 (it is invertible), not 0. So no identification $\Psi_2 = \Gamma\Psi_1$ exists. The same holds for the other images built from $\Psi_1$: the mirror image $\gamma^{(x_8)}\Psi_1$ has the right rule $+B$ but $\{\gamma^{(x_8)}\Psi_1, \Psi_1^\dagger\} = \gamma^{(x_8)}B \neq 0$, and the conjugate field $\Psi^c = \Gamma\Psi_1^{\dagger T}$ has $+B$ (Section 10.15) but $\{\Psi^c_A, \Psi_{1C}\} = \sum_D\Gamma_{AD}B_{CD} = (\Gamma B^T)_{AC} = -(\Gamma B)_{AC} \neq 0$. A second universe must live on a larger state space. There the total energy is $H_1 + H_2$, the generators ADD ($P_{\mathrm{total}} = P_1 \otimes 1 + 1 \otimes P_2$ on the product space), and the T1 identity relates operators of universe 1 only; it gives no relation $P_2 = -P_1$. The one-particle generator of the two universes is the block matrix $\mathrm{diag}(Bh'_m, Bh'_{-m})$. At zero momentum $Bh'_{\pm m} = \pm mBC$, and

$$
BC = -iC\gamma^{(x_4)}C = -iCC\gamma^{(x_4)} = -i\gamma^{(x_4)},\qquad (BC)^2 = -\gamma^{(x_4)}\gamma^{(x_4)} = I_{16},\qquad \mathrm{tr}(BC) = 0,
$$

by (B1) of Section 10.2 and $CC = I_{16}$; so $BC$ has the eigenvalues $+1$ and $-1$, eight each, and the block generator has the eigenvalues $+m$ and $-m$, sixteen each: none is 0 for $m \neq 0$. With a momentum they are $\pm\sqrt{m^2 + k^2}$, sixteen each. After normal ordering each universe has quanta of energy $+E > 0$ (Section 10.20), so every state of the two universes has a total energy of at least 0, and only the vacuum has 0. A particle in universe 1 (charge $+1$) and an antiparticle in universe 2 (charge $-1$) have the total charge 0 and the total energy $2E$, NOT 0.

**(Q4) Identical one-particle spectra.** $\Gamma h_m\Gamma = h_{-m}$ and $\gamma^{(x_8)}h_m(k)\gamma^{(x_8)} = h_{-m}(R_8k)$, so the one-particle spectra of the universes of masses $+m$ and $-m$ are identical, not opposite (Section 10.6), and along the deflating history at every instant (Section 10.39).

**(Q5) The mirror image keeps $+B$.** $\gamma^{(x_8)}B(\gamma^{(x_8)})^\dagger = +B$ (Section 10.15): the mirror universe of T2, with $(-m, \lambda)$, can be quantised as an ordinary independent copy with equal energies.

| statement | status | where it is verified |
| --- | --- | --- |
| (HQ1) kernel $N = B$, $\{\Psi, \Psi^\dagger\} = B\delta^7/\sqrt{\lvert g\rvert}$ | PROVED | `wolfram-pairing.json`, checks `Q_symplectic_kernel_grassmann` and `Q_symplectic_kernel_commuting`; `python-pairing.json`, check `Q.canonical_anticommutator` |
| (Q1) the image carries $-B$, also from its own Lagrangian | PROVED | `wolfram-pairing.json`, check `Q_Krein_metric_of_images`; `python-pairing.json`, checks `Q.image_krein_metric` and `Q.image_own_quantisation` |
| (Q2) the image's generators are those of $\Psi$; $T \to -T$, $J \to -J$ inside one system | PROVED | `wolfram-pairing.json`, checks `Q_generators_of_the_image_grassmann` and `Q_generators_of_the_image_commuting`; `python-pairing.json`, check `Q.image_generators_same_dynamics` |
| (Q3) no identification with an independent universe; generators add; block eigenvalues $\pm m$, 16 each | PROVED | `wolfram-pairing.json`, check `Q_no_identification_of_independent_universes`; `python-pairing.json`, check `Q.no_cancellation_independent_universes` |
| (Q4) identical one-particle spectra; inertia $(4, 4)$ at real frequencies | PROVED | Sections 10.5 and 10.6 |
| (Q5) the mirror image keeps $+B$ | PROVED | `python-pairing.json`, check `Q.T2_image_keeps_B` |
| the two engines agree on Q | PROVED | `python-pairing.json`, check `compare.theory.theorem_Q` (10 sympy checks confirm the 12 Wolfram verifications) |

The statements Q1 to Q5 are statements about the canonical anticommutator; they neither use nor establish a positive state space for either universe (the positive Fock spaces of this chapter are built for single good-sector momenta with frozen coefficients).

### 10.45 What the quantum reading does not establish

The author asked to prove that universes of masses $+m$ and $-m$ are created in pairs. The honest answer, as far as this chapter reaches, is the following.

**What is proved.** The quantum reading Q1 to Q5 of Section 10.44, under the hypotheses HQ1 and HQ2, and the identical one-particle spectra of the universes of masses $+m$ and $-m$ (Sections 10.6 and 10.39). Like the classical theorems T1 and T2 (Chapter 18) they are exact MAPS BETWEEN SOLUTIONS and statements about operators; they say what the quantum theory does with a solution, its image and a second universe.

**What is NOT established** (the Revision record lists the same points, written independently by the two verification engines: `python-pairing.json`, check `compare.theory.not_established`):

1. No creation process. Nothing in these equations produces a universe, a pair of universes or a change of the number of universes; no transition from "no universe" to "two universes", no initial state, no vacuum decay (the transition of a state of lowest energy into another state of still lower energy) and no tunnelling process (a quantum transition through a barrier that the classical motion cannot cross) is derived.
2. No rate, probability or amplitude. No transition amplitude, probability, rate or Bogoliubov coefficient for creating universes of masses $+m$ and $-m$ is computed or implied (when the background changes in time, a **Bogoliubov coefficient** measures how much of a wave of negative frequency at a later time is contained in a wave of positive frequency at an earlier time; its square counts the quanta that the change creates). No wave function of the universe (in quantum cosmology, a quantum state of the geometry of the whole universe, from which probabilities for universes are computed) is part of these statements.
3. No dynamical necessity. No equation and no conservation law forces the partner to exist: a single universe of mass $+m$ is an equally valid solution without its partner.
4. No cancellation between two universes. The vanishing of the total energy-momentum and charge of a T1 pair holds for classical bilinears and, as Q2 shows, as an operator identity within ONE quantum system. For two independently quantised universes the generators ADD; a pair of total charge 0 has the positive energy $2E$ (Section 10.44).
5. No positive quantum theory of the whole field. The canonical rule forces a Krein space (Theorem 10.2); in flat 4+4 space every real-frequency eigenspace has Krein inertia $(4, 4)$; a positive Fock space is constructed and checked only for single good-sector momenta with frozen coefficients; the extra-time sector grows and becomes Krein-neutral along the deflating history (Section 10.39); the curved good sector needs a boundary condition at $z = \pi/2$ that the quantisation record does not impose (Section 10.27).
6. The gravitational field is a fixed background, the same for both members; the back-reaction through the field equations for $a_4$ is not part of these statements, and the history $a_4 = AHx_4$ used in Section 10.39 is a PRESCRIBED BACKGROUND.
7. dirac16complex00 is a classical field; no quantum statement is made for it.

**The hypothesis.** That the big bang creates universes in pairs of masses $+m$ and $-m$ is the author's HYPOTHESIS. This chapter neither supports nor refutes it: it contains no creation process. Chapter 20 states the hypothesis, what the equations prove, and what they do not, for both fields; Chapter 21 treats matter and antimatter, where the conjugation of the quantised field $\Psi \to \Gamma\Psi^{\dagger T}$ of Section 10.15 (which reverses the mass) appears again, and states precisely that the theory as built does not solve the matter-antimatter problem.

### 10.46 Example: Notebook 10g checks the quantum reading of the pairing

Notebook 10g proves the Lagrangian identity $\mathcal{L}_m[\Gamma\chi] = -\mathcal{L}_{-m}[\chi]$ for symbolic field components and computes the three time-derivative kernels $B$, $-B$ and $+B$ (Q1, Q3); checks on a Fock space that the image carries $-B$ and the mirror image $+B$ (Q1, Q5); checks $H_m[\Psi] = -H_{-m}[\Gamma\Psi]$ and $Q[\Psi] = -Q[\Gamma\Psi]$ as operator identities on 150 random states and that the image obeys the wave equation of mass $-m$ under the same energy operator (Q2); tests three candidates for an independent universe (Q3); builds two independently quantised universes on 32 fermion modes, computes their block generator, and counts all $2^{32}$ states of one good-sector momentum in both universes (Q3). It draws five figures and ends with the line ALL 30 CHECKS PASSED (notebook 10g).

<!-- NOTEBOOK 10g -->

### 10.49 Line-by-line walk-through of Notebook 10g

The notebook has 13 code cells, In [1] to In [13]; docstrings are left out of the quotations (they are printed in Section 10.48).

**In [1], the set-up cell.** Its first 252 lines are comments that repeat the run instructions of Section 10.47. The code is that of In [1] of Notebook 10a (Section 10.10), with the line `NOTEBOOK_ID = "10g"  # this notebook: chapter 10, example g`. It prints `Set-up of notebook 10g complete: repository folder found, helpers defined.`

**In [2], the matrices and the statements of the record.**

```python
import contextlib  # lets a block of code print into a text buffer
import io  # the text buffer
import sys  # the screen output, sys.stdout
from math import comb  # comb(8, j): the number of ways to choose j of 8 things

import numpy as np  # numbers, arrays and matrices
import sympy as sp  # exact algebra with symbols
from matplotlib.colors import LinearSegmentedColormap  # colour scales


REPORT_CHECKS = {}  # report file -> {check name: verdict}; each file is read once


def record_says_pass(record):
    path, separator, check_name = record.partition(", check ")
    if not separator:  # a data entry of a record file that the notebook reads itself
        return True
    if path not in REPORT_CHECKS:
        checks = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
        REPORT_CHECKS[path] = {c["name"]: c["verdict"].upper() for c in checks}
    return REPORT_CHECKS[path].get(check_name) == "PASS"


def check_record(condition, name, record):
    if not record_says_pass(record):  # the cited check must exist and say PASS
        raise AssertionError("the cited record check is missing or not PASS: " + record)
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
        check(condition, name, record=record)
    sys.stdout.write(buffer.getvalue())  # one single piece of output
```

The imports of the earlier notebooks (with the binomial coefficient `comb` of Notebook 10c and the colour scales of Notebook 10a) and the helpers `REPORT_CHECKS`, `record_says_pass` and `check_record` of Section 10.10 (a cited report check must still exist with the verdict PASS; the two printed lines come in one piece).

```python
BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
DIVERGING = LinearSegmentedColormap.from_list(
    "blue_grey_red", ["#184f95", "#f0efec", "#e34948"])  # -1 blue, 0 grey, +1 red
```

The colours and the blue-grey-red colour scale of Notebook 10a.

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
    encoding="utf-8"))
# gamma[a] is the matrix gamma^(x_a) of the coordinate x_a, a = 1, ..., 8.
gamma = {a: np.array(fixture["gamma"][a - 1], dtype=int) for a in range(1, 9)}
C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]  # the author's sigma16
Gamma = (gamma[8] @ gamma[1] @ gamma[2] @ gamma[3] @ gamma[4] @ gamma[5]
         @ gamma[6] @ gamma[7])  # the chirality matrix
B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4)
I16 = np.eye(16)
```

The gammas of the record as whole numbers, $C$, $\Gamma$, $B$ and the identity.

```python
diagonal = np.array([-1] * 8 + [1] * 8)  # the expected diagonal of Gamma
sign_rules = (np.array_equal(Gamma, np.diag(diagonal))
              and np.array_equal(Gamma @ C @ Gamma, C)
              and all(np.array_equal(Gamma @ C @ gamma[a] @ Gamma, -C @ gamma[a])
                      for a in range(1, 9)))
check(sign_rules, "Gamma = diag(-I8, I8), Gamma C Gamma = C, Gamma C g^a Gamma = -C g^a")
```

The check confirms $\Gamma = \mathrm{diag}(-I_8, I_8)$ (`np.diag` makes a diagonal matrix from a list) and the two sign rules of Section 10.44.

```python
pairing = json.loads(repository_file("Revision/pairing/pairing-theory.json")
                     .read_text(encoding="utf-8"))
theorem_Q = next(t for t in pairing["theorems"] if t["id"] == "Q")
say(f"record entry Q: {theorem_Q['name']}; {len(theorem_Q['hypotheses'])} "
    f"hypothesis, {len(theorem_Q['statement'])} statements")
for number, statement in enumerate(theorem_Q["statement"], 1):
    say(f"Q{number}: {statement[:70]} ...")  # the first 70 characters of each
check(len(theorem_Q["statement"]) == 5, "the record states five quantum statements")
```

The pairing record holds a list of theorems; `next(...)` finds the one whose identifier is `Q`. The cell prints its name, `quantum-level reading`, the number of its hypotheses (1) and of its statements (5), and the first 70 characters of each statement (`statement[:70]`): Q1 about the Krein metric $-B$ of the image, Q2 about the image's own generators, Q3 about an independently quantised universe, Q4 about the one-particle Hamiltonians, Q5 about the mirror image. The check confirms the five statements.

```python
compare_file = "Revision/pairing/reports/python-pairing.json"
compare_checks = json.loads(repository_file(compare_file).read_text(
    encoding="utf-8"))["checks"]
detail = next(c["detail"] for c in compare_checks
              if c["name"] == "compare.theory.theorem_Q")
confirming = detail.split("all PASS: ")[1].split(", ")  # the sympy checks named
say("compare.theory.theorem_Q: " + detail.split(" is independently")[0])
say(f"confirmed by {len(confirming)} sympy checks: {confirming[0]}, ...")
check_record("5 statements, 12 Wolfram verifications" in detail
             and "confirmed by 10 sympy checks" in detail and len(confirming) == 10
             and all(record_says_pass(f"{compare_file}, check {name}")
                     for name in confirming),
             "theorem Q: 10 sympy checks, all PASS, confirm 12 Wolfram verifications",
             record=f"{compare_file}, check compare.theory.theorem_Q")
```

The sympy pairing report `python-pairing.json` holds, besides its own checks, checks that compare its results with those of the Wolfram report; `compare.theory.theorem_Q` is the one for theorem Q. The cell reads the report and takes the detail text of that check (`next(...)` returns the first matching entry). The text ends with `all PASS: ` and the names of the confirming sympy checks separated by commas: `detail.split("all PASS: ")[1]` is the part after `all PASS: `, and `.split(", ")` cuts it into the list `confirming` of the names. The two `say` lines print the first part of the detail text, `Wolfram theorem Q (quantum-level reading; 5 statements, 12 Wolfram verifications)`, and the number 10 with the first name, `Q.canonical_anticommutator`. The check confirms that the text states 5 statements, 12 Wolfram verifications and 10 sympy checks, that it names exactly 10 checks, and, with `record_says_pass` of In [2], that each of the 10 exists in the report with the verdict PASS; `check_record` itself also confirms the verdict of `compare.theory.theorem_Q`. These are the numbers that the table of Section 10.44 quotes. Three PASS lines in the cell.

**In [3], the Krein metrics of the two images.**

```python
image_metric = Gamma @ B @ Gamma.conj().T  # Gamma B Gamma^dagger
mirror_metric = gamma[8] @ B @ gamma[8].conj().T  # gamma8 B gamma8^dagger
signature = np.round(np.linalg.eigvalsh(image_metric)).astype(int)
report("eigenvalues -1 and +1 of Gamma B Gamma^dagger",
       f"{int(np.sum(signature == -1))} and {int(np.sum(signature == 1))}")
```

The anticommutator matrices of the two images (Section 10.15): $\Gamma B\Gamma^\dagger$ and $\gamma^{(x_8)}B(\gamma^{(x_8)})^\dagger$. The eigenvalues of the first are rounded to whole numbers (`astype(int)`) and counted: 8 and 8, so $-B$ also has the signature (8,8).

```python
check_record(np.array_equal(image_metric, -B)
             and sorted(signature.tolist()) == [-1] * 8 + [1] * 8,
             "the chirality image Gamma Psi carries the Krein metric -B, (8,8)",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.image_krein_metric")
check_record(np.array_equal(mirror_metric, B),
             "the mirror image gamma^(x8) Psi keeps the Krein metric +B",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.T2_image_keeps_B")
check_record(np.array_equal(image_metric, -B) and np.array_equal(mirror_metric, B),
             "Krein signs: Gamma gives -1, gamma^(x8) gives +1",
             record="Revision/pairing/reports/wolfram-pairing.json, check "
                    "Q_Krein_metric_of_images")
```

Three checks: Q1 and Q5 of the sympy record and the corresponding Wolfram check.

```python
def draw_matrix(ax, matrix, title):
    image = ax.imshow(matrix, cmap=DIVERGING, vmin=-1.0, vmax=1.0)
    size = matrix.shape[0]
    step = 3 if size <= 16 else 4  # label every third (or fourth) row and column
    ticks = list(range(0, size, step))
    ax.set_xticks(ticks, [str(t + 1) for t in ticks])
    ax.set_yticks(ticks, [str(t + 1) for t in ticks])
    ax.grid(False)  # no grid lines on top of the squares
    ax.set_title(title)
    return image
```

The heat-map function of In [4] of Notebook 10a (Section 10.10), with one change: for matrices larger than $16 \times 16$ (the $32 \times 32$ matrices of In [9]) every fourth row and column is labelled.

```python
fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2))
draw_matrix(axes[0], B.imag, "field $\\Psi$: $B$")
draw_matrix(axes[1], image_metric.imag,
            "image $\\Gamma\\Psi$: $\\Gamma B\\Gamma^\\dagger = -B$")
image = draw_matrix(axes[2], mirror_metric.imag,
                    "mirror $\\gamma^{(x_8)}\\Psi$: $+B$")
fig.colorbar(image, ax=list(axes), shrink=0.8, label="imaginary part of the entry")
save_figure(fig, "krein_metrics",
...)
```

The three matrices are purely imaginary; their imaginary parts are drawn. Figure 1 of Notebook 10g shows the middle picture as the left one with every red and blue square exchanged ($-B$), and the right picture equal to the left one ($+B$).

**In [4], the Lagrangian identity and the three kernels, exactly.**

```python
g = {a: sp.Matrix(fixture["gamma"][a - 1]) for a in range(1, 9)}  # exact gammas
C_exact = g[8] * g[1] * g[2] * g[3]
Gamma_exact = sp.diag(*[int(x) for x in diagonal])  # diag(-I8, I8), exact
B_exact = -sp.I * C_exact * g[4]
m = sp.Symbol("m", real=True)  # the mass: any real number
```

Exact gammas, $C$, $\Gamma$ (`sp.diag` with the 16 whole numbers of the diagonal) and $B$, and the letter $m$.

```python
field = sp.Matrix(sp.symbols("c1:17"))  # chi_A, A = 1, ..., 16
field_conj = sp.Matrix(sp.symbols("cc1:17"))  # their complex conjugates chi_A^*
# d[a] and d_conj[a]: the derivatives of chi and of chi^* along x_a
d = {a: sp.Matrix(sp.symbols(f"d{a}c1:17")) for a in range(1, 9)}
d_conj = {a: sp.Matrix(sp.symbols(f"d{a}cc1:17")) for a in range(1, 9)}
```

Letters for the 16 components $\chi_A$ (`c1` to `c16`), for their complex conjugates (`cc1` to `cc16`), and for the derivatives of both along each of the eight directions (`d1c1` to `d8c16` and `d1cc1` to `d8cc16`): $16 \times 2 + 128 \times 2 = 288$ independent letters. sympy treats a component and its conjugate as independent letters, which is how a Lagrangian uses them.

```python
def lagrangian(mass, M):
    psi, psi_conj = M * field, M * field_conj  # M is real: (M chi)^* = M chi^*
    total = sp.Integer(0)
    for a in range(1, 9):
        kinetic = C_exact * g[a]  # the matrix C gamma^(x_a)
        dpsi, dpsi_conj = M * d[a], M * d_conj[a]
        total += sp.Rational(1, 2) * ((psi_conj.T * kinetic * dpsi)[0]
                                      - (dpsi_conj.T * kinetic * psi)[0])
    total -= mass * (psi_conj.T * C_exact * psi)[0]
    return sp.expand(total)
```

`lagrangian(mass, M)` evaluates $\mathcal{L}_{\mathrm{mass}}$ of Section 10.44 on the field $M\chi$ for a constant real matrix $M$: the column of conjugates of $M\chi$ is $M\chi^*$, and the row $(M\chi)^\dagger$ is its transpose, written `psi_conj.T`. For each direction the kinetic term $\frac12((M\chi)^\dagger C\gamma^{(x_a)}\partial_a(M\chi) - \partial_a(M\chi)^\dagger C\gamma^{(x_a)}M\chi)$ is added (`+=`), then the mass term is subtracted (`-=`), and the result is multiplied out.

```python
def kernel(expression):
    return sp.Matrix(16, 16, lambda A, C_: -2 * sp.I * expression.coeff(
        field_conj[A] * d[4][C_]))
```

The kernel $N$ is read off the terms $\frac{i}{2}N_{AC}\chi_A^*\partial_4\chi_C$: `expression.coeff(...)` returns the coefficient of the product $\chi_A^*\,\partial_4\chi_C$ in the expanded Lagrangian, and $N_{AC}$ is $-2i$ times it (because $-2i \cdot \frac{i}{2} = 1$).

```python
L_field = lagrangian(m, sp.eye(16))  # L_m[chi]
L_image = lagrangian(m, Gamma_exact)  # L_m[Gamma chi]: the same system, new variables
L_independent = lagrangian(-m, sp.eye(16))  # L_-m[chi]: an independent universe
say(f"number of terms of L_m[chi]: {len(L_field.args)}")
identity_ok = sp.expand(L_image + L_independent) == 0
check(identity_ok, "exact: L_m[Gamma chi] = -L_-m[chi] for all components and "
                   "derivatives")
```

The three Lagrangians of Section 10.44: of the field, of its chirality image (the same system in the variable $\chi$), and of an independent universe of mass $-m$. The expanded Lagrangian of the field has 272 terms (`.args` lists the terms of a sum). The check proves $\mathcal{L}_m[\Gamma\chi] + \mathcal{L}_{-m}[\chi] = 0$ for all values of the 288 letters.

```python
N_field, N_image, N_independent = map(kernel, (L_field, L_image, L_independent))
kernels_ok = (N_field == B_exact and N_image == -B_exact
              and N_independent == B_exact)
say(f"kernels equal to B: field {N_field == B_exact}, image {N_image == B_exact}, "
    f"independent universe {N_independent == B_exact}; image kernel = -B: "
    f"{N_image == -B_exact}")
check_record(kernels_ok,
             "kernels: N = B (field), N = -B (image), N = +B (independent universe)",
             record="Revision/pairing/reports/wolfram-pairing.json, check "
                    "Q_symplectic_kernel_grassmann")
```

`map(kernel, ...)` applies `kernel` to each of the three Lagrangians. The printed line shows the kernels equal to $B$ for the field and the independent universe (`True`), not for the image (`False`), whose kernel is $-B$ (`True`). The check reproduces the Wolfram record check `Q_symplectic_kernel_grassmann`.

```python
anticommutators = [N.inv() for N in (N_field, N_image, N_independent)]
check_record(anticommutators[0] == B_exact and anticommutators[1] == -B_exact
             and anticommutators[2] == B_exact,
             "canonical rules N^(-1): {Psi,Psi^dag} = B, {chi,chi^dag} = -B, +B",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.image_own_quantisation")
```

The canonical rules are the inverses of the kernels (Section 10.12): $B$, $-B$ and $+B$. Three PASS lines in the cell.

**In [5], the field and its two images on a Fock space.**

```python
def sign_below(n, p):
    return -1 if bin(n & ((1 << p) - 1)).count("1") % 2 else 1


def annihilate(p, state):
    result = {}
    for n, amplitude in state.items():
        if n >> p & 1:  # mode p is occupied in the pattern n
            new = n ^ (1 << p)  # the same pattern with mode p emptied
            result[new] = result.get(new, 0) + sign_below(n, p) * amplitude
    return result


def create(p, state):
    result = {}
    for n, amplitude in state.items():
        if not n >> p & 1:  # mode p is empty in the pattern n
            new = n | (1 << p)  # the same pattern with mode p filled
            result[new] = result.get(new, 0) + sign_below(n, p) * amplitude
    return result
```

The Fock space of In [3] of Notebook 10b (Section 10.19): the sign $(-1)^s$, $f_p$ and $f_p^*$. Nothing in these functions limits the number of modes, so they work for the 32 modes used below.

```python
def add(*terms):
    result = {}
    for coefficient, state in terms:
        for n, amplitude in state.items():
            result[n] = result.get(n, 0) + coefficient * amplitude
    return result


def inner(left, right):
    return sum(np.conj(a) * right.get(n, 0) for n, a in left.items())


def largest(state):
    return max((abs(a) for a in state.values()), default=0.0)
```

Combinations of states, the positive inner product and the largest amplitude, as in Notebook 10b.

```python
rng = np.random.default_rng(12345)  # random numbers with a fixed seed


def random_state(patterns, modes):
    state = {}
    for n in rng.integers(0, 2 ** modes, size=patterns):
        state[int(n)] = complex(rng.normal(), rng.normal())
    length = np.sqrt(inner(state, state).real)
    return {n: a / length for n, a in state.items()}
```

A normalised random state of a few patterns, as in Notebook 10b, now for any number of modes.

```python
def field_op(offset):
    return [lambda s, A=A: annihilate(A - 1 + offset, s) for A in range(1, 17)]


def conjugate_op(offset):
    return [lambda s, A=A: add(*[(B[C_ - 1, A - 1], create(C_ - 1 + offset, s))
                                 for C_ in range(1, 17) if B[C_ - 1, A - 1] != 0])
            for A in range(1, 17)]
```

`field_op(offset)` returns the 16 operators $\Psi_A = f_{A-1+\mathrm{offset}}$ of one universe whose modes start at `offset`, as a list of functions; `conjugate_op(offset)` the canonical conjugates $\Psi^\dagger_A = \sum_Cf^*_{C-1+\mathrm{offset}}B_{CA}$ (the positive realisation of Section 10.14). Each `lambda s, A=A: ...` is a small function of a state `s`; the default value `A=A` stores the current value of `A` in each function (without it all 16 functions would use the last value of the loop).

```python
def mapped(M, ops):
    return [lambda s, A=A: add(*[(M[A - 1, D - 1], ops[D - 1](s))
                                 for D in range(1, 17) if M[A - 1, D - 1] != 0])
            for A in range(1, 17)]


def mapped_conjugate(M, conj_ops):
    return mapped(M.conj(), conj_ops)
```

`mapped(M, ops)` returns the 16 operators $(MX)_A = \sum_DM_{AD}X_D$ of an image; `mapped_conjugate(M, conj_ops)` its conjugate $((M\Psi)^\dagger)_A = \sum_D\Psi^\dagger_DM^*_{AD}$, which is `mapped` with the conjugate matrix applied to the conjugate operators.

```python
def anticommutator_matrix(X, Y, state):
    result = np.zeros((len(X), len(Y)), dtype=complex)
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            both = add((1, x(y(state))), (1, y(x(state))))
            result[i, j] = inner(state, both)
    return result
```

For two lists of operators the matrix of the numbers $\langle\phi|\{X_i, Y_j\}\phi\rangle$; for a normalised state $\phi$ and anticommutators that are numbers, these entries ARE the anticommutators.

```python
Psi, Psi_dagger = field_op(0), conjugate_op(0)  # one universe: modes 0, ..., 15
phi = random_state(6, 16)
own_rule = anticommutator_matrix(Psi, Psi_dagger, phi)
image_rule = anticommutator_matrix(mapped(Gamma, Psi),
                                   mapped_conjugate(Gamma, Psi_dagger), phi)
mirror_rule = anticommutator_matrix(mapped(gamma[8], Psi),
                                    mapped_conjugate(gamma[8], Psi_dagger), phi)
errors = [np.max(np.abs(own_rule - B)), np.max(np.abs(image_rule + B)),
          np.max(np.abs(mirror_rule - B))]
report("largest deviations from B, -B and +B", ", ".join(f"{e:.1e}" for e in errors))
check(max(errors) < 1e-12,
      "Fock space: {Psi, Psi^dag} = B, image -B, mirror +B (256 entries each)")
```

One universe on the modes 0 to 15 and a random normalised state. The three $16 \times 16$ anticommutator matrices of the field, of its chirality image and of its mirror image are compared with $B$, $-B$ and $+B$; the deviations are printed as `2.2e-16` each, rounding only.

**In [6], one quantum system: $T \to -T$ and $J \to -J$ as operator identities.**

```python
m_value = 1.3  # any mass and momenta (here with momenta along the extra times too)
k = {1: 0.4, 2: -0.7, 3: 0.2, 5: 0.9, 6: -0.3, 7: 0.5, 8: 1.1}


def h_prime(mass):
    return mass * C - 1j * sum(k_a * (C @ gamma[a]) for a, k_a in k.items())
```

The mass and the momenta of In [4] of Notebook 10b, and the energy matrix $h'_{\mathrm{mass}} = \mathrm{mass}\,C - i\sum_ak_aC\gamma^{(x_a)}$ of Section 10.12.

```python
def bilinear(X_dagger, N, X, state):
    terms = []
    for C_ in range(16):
        lowered = X[C_](state)
        if lowered:
            terms += [(N[A, C_], X_dagger[A](lowered)) for A in range(16)
                      if N[A, C_] != 0]
    return add(*terms)
```

`bilinear(X_dagger, N, X, state)` applies $\sum_{A,C}X^\dagger_AN_{AC}X_C$ to a state: for each $C$ it applies $X_C$ once and then every $X^\dagger_A$ with $N_{AC} \neq 0$.

```python
image_field = mapped(Gamma, Psi)  # Gamma Psi
image_conjugate = mapped_conjugate(Gamma, Psi_dagger)  # (Gamma Psi)^dagger
worst_H, worst_Q, values = 0.0, 0.0, []
for _ in range(150):
    state = random_state(4, 16)
    H_field = bilinear(Psi_dagger, h_prime(m_value), Psi, state)
    H_image = bilinear(image_conjugate, h_prime(-m_value), image_field, state)
    Q_field = bilinear(Psi_dagger, B, Psi, state)
    Q_image = bilinear(image_conjugate, B, image_field, state)
```

For 150 random states the four operators of Section 10.44 are applied: the energy of the field $H_m[\Psi] = \Psi^\dagger h'_m\Psi$, the energy that the mass $-m$ theory assigns to the image $H_{-m}[\Gamma\Psi]$, the charge $Q[\Psi] = \Psi^\dagger B\Psi$ and the charge assigned to the image $Q[\Gamma\Psi]$.

```python
    worst_H = max(worst_H, largest(add((1, H_field), (1, H_image))))
    worst_Q = max(worst_Q, largest(add((1, Q_field), (1, Q_image))))
    values.append([inner(state, X).real for X in (H_field, H_image, Q_field,
                                                   Q_image)])
values = np.array(values)  # columns: <H_m[Psi]>, <H_-m[Gamma Psi]>, <Q>, <Q image>
report("largest |(H_m[Psi] + H_-m[Gamma Psi]) phi| over 150 states", f"{worst_H:.1e}")
report("largest |(Q[Psi] + Q[Gamma Psi]) phi| over 150 states", f"{worst_Q:.1e}")
check_record(worst_H < 1e-12 and worst_Q < 1e-12,
             "operators: H_m[Psi] = -H_-m[Gamma Psi] and Q[Psi] = -Q[Gamma Psi]",
             record="Revision/pairing/reports/wolfram-pairing.json, check "
                    "Q_generators_of_the_image_grassmann")
```

The sums $(H_m[\Psi] + H_{-m}[\Gamma\Psi])\phi$ and $(Q[\Psi] + Q[\Gamma\Psi])\phi$ must vanish; the largest amplitudes are printed as `0.0e+00`. The expectation values are kept for the figure. The check reproduces the Wolfram record check `Q_generators_of_the_image_grassmann`: Q2 as an operator identity.

```python
h_mode_minus = B @ h_prime(-m_value)  # the mode Hamiltonian of mass -m
worst = 0.0
for c_ in range(16):
    H_after = bilinear(Psi_dagger, h_prime(m_value), Psi, image_field[c_](phi))
    H_before = image_field[c_](bilinear(Psi_dagger, h_prime(m_value), Psi, phi))
    commutator = add((1, H_after), (-1, H_before))  # [H, (Gamma Psi)_c] phi
    expected = add(*[(-h_mode_minus[c_, d_], image_field[d_](phi))
                     for d_ in range(16)])
    worst = max(worst, largest(add((1, commutator), (-1, expected))))
report("largest violation of [H, (Gamma Psi)_c] = -(h_-m Gamma Psi)_c", f"{worst:.1e}")
check(worst < 1e-12, "the image obeys i d4 (Gamma Psi) = h_-m Gamma Psi under the "
                     "same H")
```

With the energy $H = H_m[\Psi]$ of the system, the commutator $[H, (\Gamma\Psi)_c]$ must equal $-(h_{-m}\Gamma\Psi)_c$ with $h_{-m} = Bh'_{-m}$; by the Heisenberg equation (Section 10.12) this is $i\,\partial_4(\Gamma\Psi) = h_{-m}\Gamma\Psi$. The largest violation is printed as `1.6e-17`. Two PASS lines in the cell.

**In [7], the same exactly, and a picture.**

```python
k_symbol = {a: sp.Symbol(f"k{a}", real=True) for a in (1, 2, 3, 5, 6, 7, 8)}


def h_prime_exact(mass):
    result = mass * C_exact
    for a, k_a in k_symbol.items():
        result = result - sp.I * k_a * C_exact * g[a]
    return result
```

Real letters for the seven momenta, and the exact energy matrix $h'_{\mathrm{mass}}$.

```python
zero = sp.zeros(16, 16)
own_data = (-B_exact) * (-h_prime_exact(m))  # the image: metric -B, energy -h'_m
by_map = Gamma_exact * (B_exact * h_prime_exact(-m)) * Gamma_exact
same = ((own_data - by_map).applyfunc(sp.expand) == zero
        and (own_data - B_exact * h_prime_exact(m)).applyfunc(sp.expand) == zero)
energy_rule = (Gamma_exact * h_prime_exact(m) * Gamma_exact
               + h_prime_exact(-m)).applyfunc(sp.expand) == zero
check_record(same and energy_rule,
             "exact: (-B)(-h'_m) = Gamma (B h'_-m) Gamma = B h'_m; "
             "Gamma h'_m Gamma = -h'_-m",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.image_generators_same_dynamics")
```

The identities of Q2, exactly for all masses and momenta, in the direction in which the record states them: `own_data` is the generator of the image of a field of mass $-m$, which carries the metric $-B$ and the energy matrix $-h'_m$ (the comment of the line says so), and `by_map` is the generator $Bh'_{-m}$ of that field carried over by $\Gamma$. The check confirms $(-B)(-h'_m) = \Gamma(Bh'_{-m})\Gamma = Bh'_m$, and $\Gamma h'_m\Gamma = -h'_{-m}$. Since $m$ is a symbol, replacing $m$ by $-m$ gives the direction of Section 10.44: the image of the field of mass $m$ evolves by $(-B)(-h'_{-m}) = Bh'_{-m} = h_{-m}$. The check reproduces the sympy record check `Q.image_generators_same_dynamics`.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.4))
panels = ((axes[0], 0, 1, BLUE, "energy",
           "$\\langle H_m[\\Psi]\\rangle$", "$\\langle H_{-m}[\\Gamma\\Psi]\\rangle$"),
          (axes[1], 2, 3, ORANGE, "charge",
           "$\\langle Q[\\Psi]\\rangle$", "$\\langle Q[\\Gamma\\Psi]\\rangle$"))
```

Two panels; for each, the tuple names the drawing area, the two columns of `values` to plot, a colour, a word and the two axis labels.

```python
for ax, x_col, y_col, colour, what, x_label, y_label in panels:
    ax.plot(values[:, x_col], values[:, y_col], "o", color=colour, markersize=4,
            label="150 random states")
    low, high = values[:, x_col].min() - 0.5, values[:, x_col].max() + 0.5
    ax.plot([low, high], [-low, -high], color=GREY, linewidth=1,
            label="the line $y = -x$")
    ax.set_xlabel(f"{what} of the field, {x_label}")
    ax.set_ylabel(f"{what} given to the image, {y_label}")
    ax.legend(fontsize=8)
axes[0].set_title("$T \\to -T$ inside one system")
axes[1].set_title("$J \\to -J$ inside one system")
save_figure(fig, "one_system",
...)
```

Each state is a dot at (value of the field, value given to the image), and the grey line is $y = -x$. Figure 2 of Notebook 10g shows all 150 dots exactly on the line $y = -x$ in both panels: the reversal of the energy and of the charge under T1 is an identity between operators of ONE quantum system, not a statement about a second universe.

**In [8], which images could be an independent universe?**

```python
conjugate_field = mapped(Gamma, Psi_dagger)  # Psi^c_A = sum_D Gamma_AD Psi^dag_D
# Its canonical conjugate: (Psi^c)^dagger_A = sum_D conj(Gamma_AD) Psi_D, by the
# rule (Psi^dagger)^dagger = Psi of the canonical relations (Gamma is real).
conjugate_field_dagger = mapped(Gamma, Psi)
```

The conjugate field $\Psi^c = \Gamma\Psi^{\dagger T}$ of Section 10.15 and, as the comment lines say, its canonical conjugate $\sum_D\Gamma_{AD}\Psi_D$ ($\Gamma$ is real, and the conjugate of $\Psi^\dagger$ is $\Psi$).

```python
candidates = {
    "Gamma Psi": (image_field, image_conjugate),
    "gamma8 Psi": (mapped(gamma[8], Psi), mapped_conjugate(gamma[8], Psi_dagger)),
    "Psi^c = Gamma Psi^dag T": (conjugate_field, conjugate_field_dagger),
}
phi = random_state(6, 16)
results = {}
```

The three candidates of Section 10.44, each with its operators and their conjugates, and a new random state.

```python
for label, (X, X_dagger) in candidates.items():
    metric = anticommutator_matrix(X, X_dagger, phi)  # {X_A, X_C^dagger}
    cross_1 = anticommutator_matrix(X, Psi_dagger, phi)  # {X_A, Psi^dagger_C}
    cross_2 = anticommutator_matrix(X, Psi, phi)  # {X_A, Psi_C}
    sign = (1 if np.allclose(metric, B) else -1 if np.allclose(metric, -B) else 0)
    ranks = (np.linalg.matrix_rank(cross_1), np.linalg.matrix_rank(cross_2))
    results[label] = (sign, ranks, cross_1, cross_2)
    say(f"{label:24s} metric {sign:+d} B; rank of {{X, Psi^dag}} = {ranks[0]:2d}, "
        f"rank of {{X, Psi}} = {ranks[1]:2d}")
```

For each candidate: its own anticommutator matrix (its sign, $+1$ for $B$ and $-1$ for $-B$), and the two cross matrices with the first field, with their ranks. In an f-string a doubled brace prints a single brace. The printed lines show: $\Gamma\Psi$ with the metric $-B$ and the ranks 16 and 0; $\gamma^{(x_8)}\Psi$ with $+B$ and the ranks 16 and 0; $\Psi^c$ with $+B$ and the ranks 0 and 16. Independence would need both ranks to be 0; every candidate has a cross matrix of rank 16.

```python
chirality = results["Gamma Psi"]
conjugate = results["Psi^c = Gamma Psi^dag T"]
check_record(chirality[0] == -1 and chirality[1] == (16, 0)
             and np.allclose(chirality[2], Gamma @ B),
             "Gamma Psi: metric -B and {Gamma Psi, Psi^dag} = Gamma B of rank 16",
             record="Revision/pairing/reports/wolfram-pairing.json, check "
                    "Q_no_identification_of_independent_universes")
check_record(conjugate[0] == 1 and conjugate[1] == (0, 16)
             and np.allclose(conjugate[3], -Gamma @ B),
             "Psi^c keeps +B (Gamma B^T Gamma^dag = B) but {Psi^c, Psi} = -Gamma B",
             record="Revision/lead_checks/reports/charge-conjugation-and-u1.json, "
                    "check quantum_charge_conjugation_unitary_type")
check(results["gamma8 Psi"][0] == 1 and results["gamma8 Psi"][1] == (16, 0),
      "gamma8 Psi keeps +B; as an operator of the same field it is not independent")
```

Three checks: the chirality image has $-B$ and $\{\Gamma\Psi, \Psi^\dagger\} = \Gamma B$ (Q3, reproducing `Q_no_identification_of_independent_universes`); the conjugate field keeps $+B$ but $\{\Psi^c, \Psi\} = -\Gamma B$ (reproducing `quantum_charge_conjugation_unitary_type`); the mirror image keeps $+B$ but is built from the same field.

**In [9], two independently quantised universes.**

```python
Psi_1, Psi_1_dagger = field_op(0), conjugate_op(0)  # universe 1: modes 0..15
Psi_2, Psi_2_dagger = field_op(16), conjugate_op(16)  # universe 2: modes 16..31
phi_32 = random_state(6, 32)
two_universes = anticommutator_matrix(Psi_1 + Psi_2, Psi_1_dagger + Psi_2_dagger,
                                      phi_32)
image_pair = anticommutator_matrix(
    Psi_1 + mapped(Gamma, Psi_1),
    Psi_1_dagger + mapped_conjugate(Gamma, Psi_1_dagger), phi_32)
```

Universe 1 lives on the modes 0 to 15 and universe 2 on the modes 16 to 31 of one Fock space of 32 modes, each with its own canonical conjugate; `phi_32` is a random state of 32 modes. The `+` of two lists of operators joins them into a list of 32. `two_universes` is the $32 \times 32$ anticommutator matrix of $(\Psi_1, \Psi_2)$ with their conjugates; `image_pair` the same for a field and its chirality image.

```python
zero_16 = np.zeros((16, 16))
expected_two = np.block([[B, zero_16], [zero_16, B]])
expected_image = np.block([[B, B @ Gamma], [Gamma @ B, -B]])
cross_zero = np.max(np.abs(anticommutator_matrix(Psi_1, Psi_2, phi_32)))
report("largest |{Psi_1, Psi_2}| (must be 0)", f"{cross_zero:.1e}")
check(np.allclose(two_universes, expected_two) and cross_zero < 1e-12
      and np.allclose(image_pair, expected_image),
      "two universes: diag(B, B); field and image: blocks B, B Gamma, Gamma B, -B")
```

`np.block` assembles a matrix from blocks. The expected matrices are $\mathrm{diag}(B, B)$ for two universes, and the blocks $B$, $B\Gamma$, $\Gamma B$, $-B$ for a field and its image (Section 10.44: $\{\Psi, (\Gamma\Psi)^\dagger\} = B\Gamma$ because $(\Gamma\Psi)^\dagger = \Psi^\dagger\Gamma$). The largest $\{\Psi_1, \Psi_2\}$ is printed as `0.0e+00`: the two universes anticommute.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.0))
draw_matrix(axes[0], two_universes.imag,
            "independent: $(\\Psi_1, \\Psi_2)$")
image = draw_matrix(axes[1], image_pair.imag,
                    "one field and its image: $(\\Psi_1, \\Gamma\\Psi_1)$")
for ax in axes:
    ax.axhline(15.5, color=GREY, linewidth=1)  # the border between the two halves
    ax.axvline(15.5, color=GREY, linewidth=1)
fig.colorbar(image, ax=list(axes), shrink=0.75, label="imaginary part of the entry")
save_figure(fig, "anticommutator_blocks",
...)
```

The two $32 \times 32$ matrices as heat maps, with grey lines between the halves. Figure 3 of Notebook 10g shows on the left two copies of $B$ on the diagonal and empty off-diagonal blocks (two independent universes), and on the right a lower right block $-B$ and full off-diagonal blocks (a field and its image are one system).

**In [10], the generators add.**

```python
zero_momentum = {k_a: 0 for k_a in k_symbol.values()}
block = sp.diag((B_exact * h_prime_exact(m)).subs(zero_momentum),
                (B_exact * h_prime_exact(-m)).subs(zero_momentum))
block_eigenvalues = block.eigenvals()  # {eigenvalue: how often}
say(f"exact eigenvalues of diag(B h'_m, B h'_-m) at k = 0: +m "
    f"{block_eigenvalues.get(m, 0)} times, -m {block_eigenvalues.get(-m, 0)} times, "
    f"{len(block_eigenvalues)} different values")
check_record(block_eigenvalues == {m: 16, -m: 16},
             "block generator at k = 0: eigenvalues +m and -m, 16 each, none zero",
             record="Revision/pairing/reports/python-pairing.json, check "
                    "Q.no_cancellation_independent_universes")
```

At zero momentum (every momentum letter replaced by 0) the function `sp.diag` assembles the exact block generator $\mathrm{diag}(Bh'_m, Bh'_{-m})$ from its two $16 \times 16$ blocks, and the method `eigenvals` returns its exact eigenvalues, each with its multiplicity. The printed line shows $+m$ 16 times and $-m$ 16 times (2 different values), as Section 10.44 derived. The check reproduces the record check `Q.no_cancellation_independent_universes` of the sympy pairing report.

```python
def block_numbers(mass, k1):
    def energy(mu):  # the energy matrix of mass mu and momentum k1
        return mu * C - 1j * k1 * (C @ gamma[1])
    top, bottom = B @ energy(mass), B @ energy(-mass)
    values = np.concatenate([np.linalg.eigvals(top), np.linalg.eigvals(bottom)])
    return np.sort(values.real)
```

The 32 eigenvalues of the block generator as numbers, for a mass and a momentum $k_1$ along $x_1$: the inner function `energy` is $h'_\mu$, and the eigenvalues of the two blocks are joined and sorted.

```python
masses = np.linspace(-3.0, 3.0, 121)
spectra_0 = np.array([block_numbers(x, 0.0) for x in masses])
spectra_k = np.array([block_numbers(x, 1.5) for x in masses])
formula_k = np.sqrt(masses ** 2 + 1.5 ** 2)
error_k = max(np.max(np.abs(spectra_k[:, 16:] - formula_k[:, None])),
              np.max(np.abs(spectra_k[:, :16] + formula_k[:, None])))
report("largest deviation from +-sqrt(m^2 + k1^2), 16 each", f"{error_k:.1e}")
check(error_k < 1e-10 and np.min(np.abs(spectra_k)) >= 1.5 - 1e-10,
      "with k1 = 1.5 the 32 eigenvalues are +-sqrt(m^2 + k1^2): never 0")
```

For 121 masses from $-3$ to 3, at zero momentum and at $k_1 = 1.5$: with the momentum the 16 largest eigenvalues must be $+\sqrt{m^2 + k_1^2}$ and the 16 smallest $-\sqrt{m^2 + k_1^2}$; the largest deviation is printed as `4.9e-15`, and no eigenvalue is smaller in size than $k_1 = 1.5$.

```python
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), sharey=True)
axes[0].plot(masses, spectra_0[:, [0, 31]], color=BLUE, linewidth=2)
axes[0].set_title("zero momentum: $+m$ and $-m$, 16 each")
axes[1].plot(masses, spectra_k[:, [0, 31]], color=GREEN, linewidth=2)
axes[1].set_title("momentum $k_1 = 1.5$: $\\pm\\sqrt{m^2 + k_1^2}$, 16 each")
for ax in axes:
    ax.axhline(0.0, color=GREY, linewidth=1)
    ax.set_xlabel("mass $m$ of universe 1 (universe 2 has $-m$)")
axes[0].set_ylabel("eigenvalues of diag$(Bh'_m, Bh'_{-m})$")
save_figure(fig, "block_generator",
...)
```

The smallest and the largest eigenvalue (columns 0 and 31; each carries 16) against the mass. Figure 4 of Notebook 10g shows on the left the two straight lines $\pm m$, crossing only at $m = 0$, and on the right the two branches $\pm\sqrt{m^2 + 2.25}$, which never reach 0: the generators of the two universes add, and nothing in them cancels.

**In [11], one good-sector momentum in both universes.**

```python
def orthonormal_columns(P):
    basis = []
    for column in P.T:
        v = column.astype(complex)
        for _ in range(2):  # the second pass removes rounding errors
            for e in basis:
                v = v - (e.conj() @ v) * e
        length = np.sqrt((v.conj() @ v).real)
        if length > 1e-8:
            basis.append(v / length)
    return np.array(basis).T


def mode_hamiltonian(mass, momenta):
    h = -1j * mass * gamma[4]
    for a, k_a in momenta.items():
        h = h - k_a * (gamma[4] @ gamma[a])
    return h
```

The Gram-Schmidt function (Section 10.19) and the mode Hamiltonian of Section 10.3, as in the earlier notebooks.

```python
sample = {1: 1, 2: 2, 8: 4}  # the recorded good-sector momentum, with m = 2
h_plus, h_minus = mode_hamiltonian(2, sample), mode_hamiltonian(-2, sample)
E = 5.0  # sqrt(4 + 1 + 4 + 16)
W1 = np.hstack([orthonormal_columns((I16 + h_plus / E) / 2),
                orthonormal_columns((I16 - h_plus / E) / 2)])  # u_1..u_8, v_1..v_8
W2 = Gamma @ W1  # the eigenvectors of h_-m = Gamma h_m Gamma
check(np.allclose(h_minus @ W2[:, :8], E * W2[:, :8])
      and np.allclose(h_minus @ W2[:, 8:], -E * W2[:, 8:])
      and np.allclose(W2.conj().T @ W2, I16),
      "Gamma u_s and Gamma v_s are orthonormal eigenvectors of h_-m, energies +-E")
```

The recorded good-sector momentum $m = 2$, $k = (1, 2, 0, 4)$, $E = 5$. Universe 1 uses the orthonormal eigenvectors $u_s$ and $v_s$ of $h_m$ (Section 10.20); universe 2 uses $\Gamma u_s$ and $\Gamma v_s$, which are eigenvectors of $h_{-m} = \Gamma h_m\Gamma$ with the same eigenvalues ($h_{-m}\Gamma u = \Gamma h_mu = E\,\Gamma u$) and orthonormal ($\Gamma$ keeps lengths). The check confirms both.

```python
def universe(W, offset):
    def F(p, s):  # b (particle modes p < 8) or d^* (antiparticle modes p >= 8)
        return annihilate(p + offset, s) if p < 8 else create(p + offset, s)

    def F_star(p, s):  # the Hilbert adjoint of F_p
        return create(p + offset, s) if p < 8 else annihilate(p + offset, s)
```

`universe(W, offset)` builds the positive realisation of one universe whose 16 modes start at `offset`. The inner functions `F` and `F_star` are those of In [4] of Notebook 10c (Section 10.26): $F_p$ is $b$ for the particle modes and $d^*$ for the antiparticle modes, and `F_star` its Hilbert adjoint.

```python
    psi = [lambda s, A=A: add(*[(W[A, p], F(p, s)) for p in range(16)])
           for A in range(16)]  # Psi_A = sum_p W_Ap F_p
    chi = [lambda s, A=A: add(*[(np.conj(W[A, p]), F_star(p, s)) for p in range(16)])
           for A in range(16)]  # chi_A = sum_p conj(W_Ap) F_p^*
    psi_dagger = mapped(B.T, chi)  # Psi^dagger_A = sum_C chi_C B_CA
    return psi, chi, psi_dagger, F, F_star
```

The field $\Psi_A = \sum_pW_{Ap}F_p$, its Hilbert adjoint $\chi_A$ and the canonical conjugate $\Psi^\dagger_A = \sum_C\chi_CB_{CA}$, written as `mapped(B.T, chi)` because $\sum_C(B^T)_{AC}\chi_C = \sum_C\chi_CB_{CA}$. (Here the components are counted from 0, so `W[A, p]` has no `- 1`.) The function returns the three lists and the two mode functions.

```python
def mode_bilinear(W, F, F_star, N, state):
    M = W.conj().T @ N @ W
    terms = []
    for q in range(16):
        lowered = F(q, state)
        if lowered:
            terms += [(M[p, q], F_star(p, lowered)) for p in range(16)
                      if abs(M[p, q]) > 1e-12]
    return add(*terms)
```

`mode_bilinear` applies $\chi N\Psi = \sum_{p,q}(W^\dagger NW)_{pq}F_p^*F_q$, the function `bilinear` of In [4] of Notebook 10c; it is much faster than the sum over the components because $W^\dagger hW$ is diagonal.

```python
psi_1, chi_1, psi_1_dagger, F_1, F_1_star = universe(W1, 0)
psi_2, chi_2, psi_2_dagger, F_2, F_2_star = universe(W2, 16)
phi_32 = random_state(4, 32)
rule_1 = anticommutator_matrix(psi_1, psi_1_dagger, phi_32)
rule_2 = anticommutator_matrix(psi_2, psi_2_dagger, phi_32)
rule_12 = anticommutator_matrix(psi_1, psi_2_dagger, phi_32)
check(np.allclose(rule_1, B) and np.allclose(rule_2, B) and np.allclose(rule_12, 0),
      "positive realisation: {Psi_1, Psi_1^dag} = {Psi_2, Psi_2^dag} = B, cross 0")
```

The two universes on the modes 0 to 15 and 16 to 31. The check confirms the canonical rule $B$ in each and the cross anticommutator 0.

```python
def total_energy(state):
    return add((1, mode_bilinear(W1, F_1, F_1_star, h_plus, state)),
               (1, mode_bilinear(W2, F_2, F_2_star, h_minus, state)))


def total_charge(state):
    return add((1, mode_bilinear(W1, F_1, F_1_star, I16, state)),
               (1, mode_bilinear(W2, F_2, F_2_star, I16, state)))
```

The total energy $H_1 + H_2$ (with $H = \chi h\Psi$ in each universe, Section 10.20) and the total charge $Q_1 + Q_2$ (with $Q = \chi\Psi$).

```python
VACUUM = {0: 1.0}
vacuum_energy = inner(VACUUM, total_energy(VACUUM)).real
vacuum_charge = inner(VACUUM, total_charge(VACUUM)).real
report("vacuum energy and charge of the two universes",
       f"{vacuum_energy:.10f} and {vacuum_charge:.10f}")
check_record(abs(vacuum_energy + 16 * E) < 1e-9 and abs(vacuum_charge - 16) < 1e-9,
             "each universe has the sea energy -8E = -40 (total -80) and charge 8",
             record="Revision/theory/reports/python-field-theory.json, check "
                    "good_sector_positive_fock_realisation")
```

The vacuum of both universes has the energy $-80 = 2 \times (-40)$ and the charge $16 = 2 \times 8$ before normal ordering; the check reproduces the record check `good_sector_positive_fock_realisation` for each universe. Three PASS lines in the cell.

**In [12], the states of the two universes.**

```python
def quanta_and_charge(n):
    groups = [bin((n >> shift) & 0xFF).count("1") for shift in (0, 8, 16, 24)]
    b_1, d_1, b_2, d_2 = groups  # particles and antiparticles of each universe
    return b_1 + d_1 + b_2 + d_2, b_1 - d_1 + b_2 - d_2
```

The 32 binary digits of a pattern fall into four groups of 8: the particles and the antiparticles of universe 1, then those of universe 2. For each group the pattern is shifted to the right by 0, 8, 16 or 24 places, the eight lowest digits are kept (`& 0xFF`) and their ones are counted. The function returns the number of quanta and the total charge (particles minus antiparticles).

```python
eigen_ok = True
for n in rng.integers(0, 2 ** 32, size=200):
    n = int(n)
    quanta, charge = quanta_and_charge(n)
    state = {n: 1.0}
    eigen_ok = eigen_ok and largest(add(
        (1, total_energy(state)), (-(E * quanta + vacuum_energy), state))) < 1e-9
    eigen_ok = eigen_ok and largest(add(
        (1, total_charge(state)), (-(charge + vacuum_charge), state))) < 1e-9
check(eigen_ok, "200 random patterns: energy E (quanta) - 16E, charge (b - d) + 16")
```

For 200 random patterns the total energy and charge are applied, and the results compared with the pattern times $E \times(\text{quanta}) - 16E$ and times $(\text{charge}) + 16$: every pattern is an eigenstate, with the normal-ordered total energy $E$ times its number of quanta.

```python
pair = create(24, create(0, VACUUM))  # b_1^* (mode 0), then d_2^* (mode 24)
pair_energy = inner(pair, total_energy(pair)).real - vacuum_energy
pair_charge = inner(pair, total_charge(pair)).real - vacuum_charge
report("pair state: normal-ordered total energy and total charge",
       f"{pair_energy:.10f} and {pair_charge:.10f}")
check(abs(pair_energy - 2 * E) < 1e-9 and abs(pair_charge) < 1e-9,
      "a particle in universe 1 and an antiparticle in universe 2: charge 0, "
      "energy 2E")
```

The pair state: a particle in universe 1 (mode 0) and an antiparticle in universe 2 (mode 24, the first antiparticle mode of universe 2). Its normal-ordered total energy is printed as $10.0000000000 = 2E$ and its total charge as 0: the energies of the two universes add.

```python
counts = np.zeros((33, 33), dtype=np.int64)  # rows: quanta, columns: charge + 16
for b_1 in range(9):
    for d_1 in range(9):
        for b_2 in range(9):
            for d_2 in range(9):
                number = comb(8, b_1) * comb(8, d_1) * comb(8, b_2) * comb(8, d_2)
                counts[b_1 + d_1 + b_2 + d_2, b_1 - d_1 + b_2 - d_2 + 16] += number
```

All $2^{32} = 4294967296$ patterns are counted by formula, not one by one: for given numbers $b_1, d_1, b_2, d_2$ of occupied modes in the four groups there are $\binom{8}{b_1}\binom{8}{d_1}\binom{8}{b_2}\binom{8}{d_2}$ patterns, added in the square (number of quanta, charge $+ 16$). `np.int64` holds whole numbers up to about $9 \times 10^{18}$.

```python
zero_energy_states = int(counts[0].sum())
zero_charge_lowest = min(q for q in range(33) if q > 0 and counts[q, 16] > 0)
report("number of patterns", int(counts.sum()))
report("patterns of zero normal-ordered energy", zero_energy_states)
report("fewest quanta of a non-vacuum state of total charge 0", zero_charge_lowest)
check(counts.sum() == 2 ** 32 and zero_energy_states == 1 and zero_charge_lowest == 2,
      "only the vacuum has energy 0; charge 0 needs at least 2 quanta (energy 2E)")
```

The printed numbers: 4294967296 patterns, 1 of zero energy (the vacuum), and 2 as the smallest positive number of quanta of a state of total charge 0 (column 16): a state of charge 0 other than the vacuum has at least the energy $2E$. Three PASS lines in the cell.

```python
fig, ax = plt.subplots(figsize=(7.5, 5.6))
shown = np.where(counts > 0, np.log10(np.maximum(counts, 1)), np.nan)  # NaN: empty
light_to_dark = LinearSegmentedColormap.from_list(
    "light_to_dark_blue", ["#cde2fb", "#2a78d6", "#0d366b"])
image = ax.imshow(shown, origin="lower", cmap=light_to_dark, aspect="auto",
                  extent=(-16.5, 16.5, -0.5, 32.5))
ax.annotate("vacuum: the only state of energy 0", (0, 0), xytext=(2.0, 1.5),
            fontsize=8, arrowprops={"arrowstyle": "->", "color": GREY})
ax.annotate("pair of total charge 0: energy $2E$", (0, 2), xytext=(3.0, 5.5),
            fontsize=8, arrowprops={"arrowstyle": "->", "color": GREY})
ax.set_xlabel("total charge (particles minus antiparticles, both universes)")
ax.set_ylabel("number of quanta (total energy $= 5 \\times$ quanta)")
ax.set_title("Two universes, one momentum: $2^{32}$ states")
ax.grid(False)
fig.colorbar(image, ax=ax, label="$\\log_{10}$ of the number of states")
save_figure(fig, "two_universe_states",
...)
```

The heat map of In [9] of Notebook 10c, now for two universes: the logarithm of the counts, white for empty squares, with arrows at the vacuum and at the pairs of total charge 0. Figure 5 of Notebook 10g shows a diamond of states from charge $-16$ to 16 and up to 32 quanta, with a single state at energy 0 and nothing below it: two independently quantised universes of masses $+m$ and $-m$ have energies that add; nothing cancels.

**In [13], the last check.**

```python
for name in ("10g_1_krein_metrics.png", "10g_2_one_system.png",
             "10g_3_anticommutator_blocks.png", "10g_4_block_generator.png",
             "10g_5_two_universe_states.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The five figure files exist, and the last line prints ALL 30 CHECKS PASSED (notebook 10g): the five figure checks and the 25 checks of the cells before (3 in In [2], 3 each in In [3], In [4], In [8], In [11] and In [12], 1 each in In [5], In [7] and In [9], and 2 each in In [6] and In [10]).

### 10.50 What we proved, what we computed, what we assumed

**Proved.** Exactly, for all values of the letters involved, each with the Revision record that verifies it and the notebook that reproduces it:

| statement | where it is verified | notebook |
| --- | --- | --- |
| $B = -iC\gamma^{(x_4)}$ is purely imaginary and Hermitian, $BB = I_{16}$, $\mathrm{tr}\,B = 0$, signature (8,8); it commutes with the gammas of $x_1, x_2, x_3, x_4, x_8$ and anticommutes with those of $x_5, x_6, x_7$ | `python-field-theory.json`, check `B_properties`; `wolfram-algebra.json`, check `B_signature_8_8`; `python-algebra.json`, check `B_gamma_relations` | 10a, 10e |
| the local conservation law $\partial_\mu(\cos z\,J^\mu) = 0$ on shell; the charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ is an indefinite (Krein) form (it is constant in time only when no charge flows through the boundary of the slice, which at $z = \pi/2$ is an ASSUMED no-flux condition that the record does not impose) | `charge-conjugation-and-u1.json`, check `u1_noether_matrix_identity`; `wolfram-field-theory.json`, check `charge_density_is_Krein_form_G` | none |
| one plane wave: $hh = w^2I_{16}$, $Bh = h^\dagger B$ (the Krein form is conserved, also by growing waves); $h$ Hermitian and $[B, h] = 0$ exactly in the good sector | `wolfram-pairing.json`, check `Q_one_particle_flat_dispersion`; `python-field-theory.json`, checks `mode_hamiltonian_B_selfadjoint_dispersion` and `good_sector_spectrum_and_B_sectors`; `wolfram-field-theory.json`, checks `mode_hamiltonian_good_sector` and `mode_hamiltonian_Krein_selfadjoint` | 10a |
| waves with $w^2 < 0$ grow, with rates that have no upper bound | `python-field-theory.json`, check `extra_time_modes_grow`; `python-scope.json`, check `extra_time_growth_rates_unbounded` | 10a, 10f |
| Theorem 10.1: Krein inertia (4,4) of every real-frequency eigenspace; Krein-neutral eigenspaces at imaginary and zero frequency | `wolfram-pairing.json`, checks `Q_one_particle_Krein_inertia_real_frequencies` and `Q_one_particle_complex_and_zero_frequencies_Krein_neutral`; `python-pairing.json`, checks `Q.one_particle_Krein_inertia_proof` and `Q.one_particle_complex_frequency_Krein_neutral` | 10a, 10f |
| $\Gamma h_m\Gamma = h_{-m}$ and $\gamma^{(x_8)}h_m(k)\gamma^{(x_8)} = h_{-m}(R_8k)$: identical one-particle spectra for $+m$ and $-m$ | `python-pairing.json` and `wolfram-pairing.json`, check `Q.one_particle_maps` / `Q_one_particle_maps` | 10a, 10f |
| the canonical rule $\{\Psi_A(x), \Psi^\dagger_C(y)\} = B_{AC}\,\delta^7(x - y)/\cos z$; the Heisenberg equation is the field equation | `python-field-theory.json`, check `canonical_anticommutator_B`; `wolfram-field-theory.json`, checks `first_order_form_and_anticommutator` and `Heisenberg_equation_reproduces_field_equation` | 10b |
| Theorem 10.2: no positive inner product with $\Psi^\dagger$ the Hilbert adjoint; the state space is a Krein space with fundamental symmetry $B$ | `python-field-theory.json` and `wolfram-field-theory.json`, check `no_positive_inner_product` | 10b |
| the expectation-value rule $\epsilon_nu_n^\dagger Mu_n$ (Krein-Fock), $u^\dagger BMu$ and $-v^\dagger BMv$ (positive realisation) | `python-field-theory.json`, checks `expectation_value_rule` and `good_sector_positive_fock_realisation` | 10b, 10c |
| the 17 signs of $MBM^\dagger = \sigma B$; the conjugation $\Psi \to \Gamma\Psi^{\dagger T}$ keeps $B$ and reverses the mass, $M = I_{16}$ gives $-B$ | `pairing-theory.json`, data `Krein_signs_M_B_Mdagger`; `charge-conjugation-and-u1.json`, check `quantum_charge_conjugation_unitary_type` | 10b, 10g |
| good sector, one momentum with frozen coefficients: positive Fock space with $\Psi^\dagger = \chi B$, vacuum $-8E$, quanta $+E$, charges $\pm1$ | `python-field-theory.json`, check `good_sector_positive_fock_realisation`; `wolfram-field-theory.json`, check `Fock_space_good_sector_example` | 10c, 10f, 10g |
| the classical commuting field dirac16complex00 has an energy unbounded below and an indefinite charge | `python-scope.json`, check `commuting_field_energy_unbounded_below` | 10c |
| $\lambda \neq 0$, in the finite Fock model of one good-sector mode set with frozen coefficients (16 modes; symbolic $\lambda$; at rest with symbolic $m$, and $m = 3$, $k = (4, 0, 0, 0)$): ${:}\sum_\mu K_\mu{:} = {:}(m + U'(S))S{:}$ and, at rest, $\hat\rho = {:}mS + U{:}$, $\hat p = {:}SU' - U{:}$ are exact operator identities for solutions of the interacting operator field equation if and only if $U$ and $\hat T$ are Wick ordered | `fock-quartic.json`, checks `trace_identity_operator_identity_wick`, `trace_identity_fails_for_every_other_combination` and `homogeneous_rho_p_operator_identities_wick` | none |
| curved good sector: symmetric, and the Krein form conserved, only up to the boundary term $\partial_8(\sin z\,u^\dagger M_8v)$; flux $2i$; role of $3H\gamma^{(x_8)}$; $x_8$-independent waves grow for $m^2 < 9H^2$; the exact solution | `python-scope.json`, checks `good_sector_hermiticity_up_to_the_brane_flux` and `good_sector_x8_independent_modes_without_boundary_condition`; `wolfram-field-theory.json`, checks `good_sector_hermiticity_curved` and `Krein_form_conserved_curved`; `python-field-theory.json`, check `exact_solution_family_x4_x8` | 10d |
| the invariant forms are $r_-CP_- + r_+CP_+$; every invariant charge density is indefinite; exactly the 21 generators without $x_4$ keep $B$ (Spin(4,3)) | `python-algebra.json`, checks `spin_commutant_dimension_2` and `S_preserves_C_and_commutes_with_Gamma`; `wolfram-algebra.json`, checks `S_preserves_C` and `S_preserves_B_only_off_x4` | 10e |
| along the deflating history (local-frame model): $h(x_4)^2 = w(x_4)^2I_{16}$, $\lVert h_A\rVert = k_5$, $\lVert Bh - hB\rVert = 2k_5$; every wave with extra-time momentum reaches the onset time $\ln X^\ast/(2AH)$; the good sector stays Hermitian | this chapter, Section 10.39 (the book's own derivation, exact in sympy) | 10f |
| the quantum reading Q1 to Q5 of the pairing | `wolfram-pairing.json`, checks `Q_Krein_metric_of_images`, `Q_symplectic_kernel_grassmann`, `Q_generators_of_the_image_grassmann`, `Q_no_identification_of_independent_universes`; `python-pairing.json`, checks `Q.image_krein_metric`, `Q.image_own_quantisation`, `Q.image_generators_same_dynamics`, `Q.no_cancellation_independent_universes`, `Q.T2_image_keeps_B`, `compare.theory.theorem_Q` | 10g |

**Computed.** Numerical results of the notebooks, with their accuracy:

- Notebook 10a: the 16 eigenvalues of $h$ agree with $\pm w$ to $3.6 \times 10^{-15}$; in the scan across the threshold the inertia is $(4, 4, 0)$ at all 110 real-frequency points and $(0, 0, 8)$ at all 137 imaginary-frequency points, with the smallest nonzero Gram eigenvalue 0.2225 below the threshold.
- Notebook 10b: the canonical rule holds on the Fock space exactly ($0.0$) and the Heisenberg equation to $1.6 \times 10^{-17}$; the Krein norms of 5000 random unit columns lie between $-0.777$ and $0.704$; for the boosted mode the rule $\epsilon u^\dagger Mu$ holds to $1.3 \times 10^{-15}$, while $u^\dagger BMu$ misses by up to 5.82.
- Notebook 10c: vacuum $-40$, every quantum $+5$, charges $\pm1$ (to $10^{-12}$), for $m = 2$, $k = (1, 2, 0, 4)$ and for $m = 3$, $k_1 = 4$; the 65536 states of one momentum, one of them of energy 0; the commuting field: densities $\pm5$, and from $-4.364$ to $4.333$ for 4000 random waves.
- Notebook 10d: the Krein charge of the exact growing solution rises from $1/6$ to 454.007 between $x_4 = 0$ and 1.5 and equals the flux added up over time to a relative $6.7 \times 10^{-7}$; the late growth slope 5.6600 approaches $2k = 5.6569$.
- Notebook 10e: exactly two zero eigenvalues of $M^TM$ (at most $1.3 \times 10^{-15}$) below the smallest nonzero one, 7.0.
- Notebook 10f: the onset time 2.996044 of the wave $q_1 = 0.5$, $q_5 = 0.05$ (agreement with bisection $8.9 \times 10^{-16}$ for 48 waves); onset times from 6.9078 to 0.0941 for $10^{-3} \leq q_5 \leq 1$; the good-sector energies at the five slices (for $q_1 = 1$ from 1.414214 down to 1.009116).
- Notebook 10g: the pair of total charge 0 in two independent universes has the normal-ordered energy $10 = 2E$; of the $2^{32} = 4294967296$ states of one momentum in both universes exactly one (the vacuum) has energy 0.

**Assumed.**

- Anticommutators (not commutators) for dirac16complex: part of its definition as a fermion field; no spin-statistics theorem for signature (4,4) is proved.
- Normal ordering: a prescription that drops the energy $-8E$ of the filled sea per momentum.
- Flat 4+4 space, or the frozen-coefficient model of Section 10.3 (the coefficients of one point and one instant, without the two hidden-direction terms of the author's field equation, among them the spin-connection term $3H\gamma^{(x_8)}$; keeping that term breaks $Bh = h^\dagger B$), for the one-particle statements and the Fock spaces; the good sector itself is a restriction imposed by hand (no mechanism that removes the extra-time waves is derived).
- The deflating history $a_4 = AHx_4$ ($A = H = m = 1$) is a PRESCRIBED BACKGROUND, and the local-frame model of Section 10.39 evaluates the coefficients at one instant and one hidden position (`parameters.json`; `ks-source-conditions.json`, check `ks_history_is_a_prescribed_background`).
- The Z2 brane condition at $z = \pi/2$ is ASSUMED by the Kohn-Sham record (Chapter 14); the quantisation of this chapter imposes no boundary condition there. The total charge $Q$ is constant in time only under such an ASSUMED no-flux condition at $z = \pi/2$; what is proved is its local conservation law (Section 10.2).

**Hypothesis.** That the big bang creates universes in pairs of masses $+m$ and $-m$ is the author's HYPOTHESIS; no equation of this chapter describes a creation, in pairs or otherwise (Section 10.45).

**Open.**

- A positive Hilbert space for the whole quantised field (all momenta, the curved metric), and the quantisation of the extra-time sector, whose waves grow and become Krein-neutral along the deflating history.
- A boundary condition at the patch end $z = \pi/2$ that makes the curved good-sector evolution Hermitian and conserves the Krein charge.
- The interacting theory $\lambda \neq 0$, in particular the operator form of the on-shell identity of the energy-momentum tensor beyond the finite model of one good-sector mode set with frozen coefficients (where it holds with Wick ordering only, Section 10.21): for the field on a whole slice, with the curved $x_8$ dependence and in the extra-time sector; symmetry and conservation of the quartic operator are not verified.
- The evolution of the quantum state through the changing background (whether the instantaneous vacuum of one time contains quanta of a later time).
- Any creation process, rate or amplitude for universes, which these equations do not contain.

### 10.51 Exercises

**Exercise 10.1.** Use the table of $B$ in Section 10.2. (a) Compute $Be_1$ and $Be_{10}$, where $e_j$ is the unit column with 1 in place $j$. (b) Find the two columns $u = ae_1 + be_{10}$ of length 1 that are eigenvectors of $B$, with their eigenvalues. (c) Compute the Krein norms of $e_1$ and of the two eigenvectors.

**Exercise 10.2.** For each wave compute $w^2$, say whether it oscillates, grows linearly or grows exponentially, and give the growth rate where there is one: (a) $m = 2$, $k_1 = 1$, $k_6 = 2$; (b) $m = 1$, $k_8 = 1$, $k_5 = 1$, $k_7 = 1$; (c) $m = 1$, $k_5 = 3$. In case (a), what is the Krein inertia of the eigenspaces?

**Exercise 10.3.** A two-dimensional model of a Krein space: $B = \mathrm{diag}(1, -1)$ and $h = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}$. (a) Show $h^\dagger B = Bh$ and $hh = -I_2$. (b) Solve $i\,du/dt = hu$ with $u(0) = (1, 0)$. (c) Compute $u^\dagger u$ and $u^\dagger Bu$ as functions of $t$.

**Exercise 10.4.** A toy Dirac sea: one positive level (operator $b$, energy $E$) and one negative level (operator $d^*$, energy $-E$), with $\{b, b^*\} = \{d, d^*\} = 1$ and all other anticommutators 0, have $H = E\,b^*b - E\,dd^*$ and $Q = b^*b + dd^*$. (a) Find the vacuum energy and charge before normal ordering. (b) Write ${:}H{:}$ and ${:}Q{:}$. (c) Give the normal-ordered energy and charge of $b^*|0\rangle$, $d^*|0\rangle$ and $b^*d^*|0\rangle$.

**Exercise 10.5.** For one good-sector momentum (8 particle and 8 antiparticle modes, energy $E$ per quantum), count the states (a) with 2 quanta, (b) with 2 quanta and charge 0, (c) with 8 quanta and charge 0, (d) in all.

**Exercise 10.6.** Using only $(\gamma^{(x_a)})^\dagger = \eta_{aa}\gamma^{(x_a)}$, $\gamma^{(x_a)}\gamma^{(x_a)} = \eta_{aa}I_{16}$, the commutation of $B$ with the gammas (Section 10.2) and $\Gamma B\Gamma = -B$, compute the sign $\sigma$ in $MBM^\dagger = \sigma B$ for $M = \gamma^{(x_5)}$, $M = \gamma^{(x_4)}$ and $M = P_5 = \Gamma\gamma^{(x_5)}$.

**Exercise 10.7.** (a) Show that $S^{(x_1x_5)} = \frac12\gamma^{(x_1)}\gamma^{(x_5)}$ is Hermitian and anticommutes with $B$, so that it is Krein-unitary but not unitary. (b) Show that $S^{(x_4x_1)} = \frac12\gamma^{(x_4)}\gamma^{(x_1)}$ is Hermitian and commutes with $B$, and compute its Krein defect $S^\dagger B + BS$.

**Exercise 10.8.** On the deflating history with $A = H = m = 1$ and $y = 0$: (a) find the onset time of the waves with $q_1 = 0$ and $q_5 = 0.05$, and $q_5 = 0.001$; (b) at what time does the wave $q_1 = 0$, $q_5 = 0.05$ reach the frame momentum $k_5 = 2$? (c) Compute $X^\ast$ and the onset time for $q_1 = 0.5$, $q_5 = 0.05$, and explain why it is later than in (a).

**Exercise 10.9.** For the good-sector waves that do not depend on $x_8$ (Section 10.28), with $H = 1$: find the eigenvalues of $A$ and the growth rate for $m = 2$ and for $m = 4$.

### 10.52 Answers to the exercises

**Answer 10.1.** (a) $(Be_1)_r = B_{r1}$, the entries of column 1: by the table only row 10 has its nonzero entry in column 1, with the value $-i$, so $Be_1 = -ie_{10}$. Row 1 has its entry $+i$ in column 10, so $Be_{10} = ie_1$. (b) For $u = ae_1 + be_{10}$, $Bu = aBe_1 + bBe_{10} = ib\,e_1 - ia\,e_{10}$, by (a). $Bu = \lambda u$ means $ib = \lambda a$ and $-ia = \lambda b$. The first gives $b = -i\lambda a$ (multiply by $-i$); insert it into the second: $-ia = \lambda(-i\lambda a) = -i\lambda^2a$, so $\lambda^2 = 1$. For $\lambda = +1$: $b = -ia$, and with length 1, $u_+ = (e_1 - ie_{10})/\sqrt2$. For $\lambda = -1$: $b = ia$, $u_- = (e_1 + ie_{10})/\sqrt2$. Check: $Bu_- = (i \cdot i\,e_1 - ie_{10})/\sqrt2 = (-e_1 - ie_{10})/\sqrt2 = -u_-$. (c) $e_1^\dagger Be_1 = B_{11} = 0$: the unit column $e_1$ has length 1 but Krein norm 0. $u_\pm^\dagger Bu_\pm = \pm u_\pm^\dagger u_\pm = \pm1$.

**Answer 10.2.** $w^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$ (Section 10.4). (a) $w^2 = 4 + 1 - 4 = 1$: the frequencies $\pm1$ are real and the wave oscillates, although $h$ is not Hermitian ($k_6 \neq 0$). By Theorem 10.1 both eigenspaces have the Krein inertia $(4, 4)$. (b) $w^2 = 1 + 1 - 1 - 1 = 0$ with $h \neq 0$: $hh = 0$, $e^{-ihx_4} = I_{16} - ihx_4$, and the wave grows linearly unless $hu(0) = 0$; the range of $h$ is Krein-neutral. (c) $w^2 = 1 - 9 = -8$: $w = \pm i\sqrt8 = \pm2\sqrt2\,i$, half of the waves grow like $e^{2\sqrt2\,x_4}$ (rate $2\sqrt2 \approx 2.828$), and both eigenspaces are Krein-neutral.

**Answer 10.3.** (a) $h^\dagger = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$ (transpose; the entries are real). $h^\dagger B = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ (the second column of $h^\dagger$ is multiplied by $-1$) and $Bh = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ (the second row of $h$ is multiplied by $-1$): equal. $hh = \begin{pmatrix}0\cdot0 + 1\cdot(-1) & 0\cdot1 + 1\cdot0\\ (-1)\cdot0 + 0\cdot(-1) & (-1)\cdot1 + 0\cdot0\end{pmatrix} = -I_2$, so $w^2 = -1$. (b) As in Section 10.4, $e^{-iht} = \cos(wt)I_2 - i\frac{\sin(wt)}{w}h$ with $w = i$; $\cos(it) = \cosh t$ and $\sin(it)/i = \sinh t$, so $e^{-iht} = \cosh t\,I_2 - i\sinh t\,h$. With $hu(0) = (0, -1)$ (the first column of $h$): $u(t) = (\cosh t, i\sinh t)$. Check: $i\,du/dt = i(\sinh t, i\cosh t) = (i\sinh t, -\cosh t)$ and $hu = (i\sinh t, -\cosh t)$. (c) $u^\dagger u = \cosh^2t + \sinh^2t = \cosh 2t$, which grows; $u^\dagger Bu = \cosh^2t - \sinh^2t = 1$, constant: the Krein norm is conserved by a growing wave, as Section 10.4 proved for dirac16complex.

**Answer 10.4.** (a) The vacuum has $b|0\rangle = d|0\rangle = 0$. With $dd^* = 1 - d^*d$: $H = E\,b^*b + E\,d^*d - E$ and $Q = b^*b - d^*d + 1$, so the vacuum has the energy $-E$ (the filled negative level) and the charge 1. (b) ${:}H{:} = E(b^*b + d^*d)$ and ${:}Q{:} = b^*b - d^*d$. (c) $b^*|0\rangle$: energy $E$, charge $+1$; $d^*|0\rangle$: energy $E$, charge $-1$; $b^*d^*|0\rangle$: energy $2E$, charge 0. A state of total charge 0 other than the vacuum has a positive energy, as for the two universes of Section 10.44.

**Answer 10.5.** A state is fixed by the set of occupied modes; with $N_b$ particles and $N_d$ antiparticles it has $N_b + N_d$ quanta and the charge $N_b - N_d$ (Section 10.20). (a) Any 2 of the 16 modes: $\binom{16}{2} = \frac{16 \cdot 15}{2} = 120$; split as $\binom82 = 28$ (two particles, charge 2), $8 \cdot 8 = 64$ (one of each, charge 0) and 28 (two antiparticles, charge $-2$). (b) 64. (c) $N_b = N_d = 4$: $\binom84\binom84 = 70 \cdot 70 = 4900$, the largest group of Figure 3 of Notebook 10c. (d) $2^{16} = 65536$.

**Answer 10.6.** $M = \gamma^{(x_5)}$: it is time-like, so $(\gamma^{(x_5)})^\dagger = -\gamma^{(x_5)}$ and $\gamma^{(x_5)}\gamma^{(x_5)} = -I_{16}$, and it anticommutes with $B$: $\gamma^{(x_5)}B(\gamma^{(x_5)})^\dagger = -\gamma^{(x_5)}B\gamma^{(x_5)} = B\gamma^{(x_5)}\gamma^{(x_5)} = -B$, $\sigma = -1$. $M = \gamma^{(x_4)}$: time-like and commuting with $B$: $\gamma^{(x_4)}B(\gamma^{(x_4)})^\dagger = -\gamma^{(x_4)}B\gamma^{(x_4)} = -B\gamma^{(x_4)}\gamma^{(x_4)} = B$, $\sigma = +1$. $M = P_5$: $P_5B P_5^\dagger = \Gamma\gamma^{(x_5)}B(\gamma^{(x_5)})^\dagger\Gamma^\dagger = \Gamma(-B)\Gamma = -\Gamma B\Gamma = B$, $\sigma = +1$. These are the signs of the record (Section 10.15).

**Answer 10.7.** (a) $(\gamma^{(x_1)}\gamma^{(x_5)})^\dagger = (\gamma^{(x_5)})^\dagger(\gamma^{(x_1)})^\dagger = (-\gamma^{(x_5)})\gamma^{(x_1)} = \gamma^{(x_1)}\gamma^{(x_5)}$, so $S = S^{(x_1x_5)}$ is Hermitian, $S^\dagger = S$ (and not anti-Hermitian, so $\exp(\theta S)$ is not unitary). $\gamma^{(x_1)}$ commutes and $\gamma^{(x_5)}$ anticommutes with $B$, so $SB = -BS$. The Krein condition: $S^\dagger B + BS = SB + BS = -BS + BS = 0$. (b) $(\gamma^{(x_4)}\gamma^{(x_1)})^\dagger = \gamma^{(x_1)}(-\gamma^{(x_4)}) = \gamma^{(x_4)}\gamma^{(x_1)}$: Hermitian; both gammas commute with $B$, so $SB = BS$. Then $S^\dagger B + BS = 2BS = -iC\gamma^{(x_4)}\gamma^{(x_4)}\gamma^{(x_1)} = iC\gamma^{(x_1)} \neq 0$, the defect of the record check `S_preserves_B_only_off_x4`.

**Answer 10.8.** (a) For $q_1 = 0$, $y = 0$: $x_4^\ast = \ln(m/q_5)/(AH) = \ln(1/q_5)$; $\ln 20 = 2.995732$ for $q_5 = 0.05$, and $\ln 1000 = 6.907755$ for $q_5 = 0.001$. (b) $k_5 = 0.05\,e^{x_4} = 2$ gives $e^{x_4} = 40$, $x_4 = \ln 40 = 3.688879$, where the eigenvalues are $\pm i\sqrt3$ (Notebook 10f, In [7]). (c) With $c = 1$: $X^\ast = (1 + \sqrt{1 + 4 \cdot 0.25 \cdot 0.0025})/(2 \cdot 0.0025) = (1 + \sqrt{1.0025})/0.005 = 400.249844$, and $x_4^\ast = \frac12\ln 400.249844 = 2.996044$, the value of Notebook 10f, In [6]. It is later than $\ln 20$ because the 3-space momentum adds $k_1^2 > 0$ to $w^2$, so the growing $k_5^2$ needs a little longer to overcome $m^2 + k_1^2$.

**Answer 10.9.** $AA = (m^2 - 9H^2)I_{16}$ and $\mathrm{tr}\,A = 0$ (Section 10.28). For $m = 2$: $AA = (4 - 9)I_{16} = -5I_{16}$, eigenvalues $\pm i\sqrt5$ (eight each), growth rate $\sqrt5 \approx 2.236$: these finite-norm waves grow. For $m = 4$: $AA = 7I_{16}$, eigenvalues $\pm\sqrt7 \approx \pm2.646$, real: the waves oscillate (Figure 4 of Notebook 10d: zero growth rate for $m \geq 3H$).
