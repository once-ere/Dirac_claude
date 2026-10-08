## 13. Many-body quantum mechanics and DFT from zero

This chapter builds, from zero, the tool with which Chapters 14 to 16 compute the states of many quanta of the field dirac16complex in the author's primordial field: **density functional theory**, DFT for short, in the form of Kohn and Sham. Every idea is first developed for ordinary particles that move slowly (non-relativistic particles), because there every step can be seen and checked by hand. The chapter has five worked examples, Notebooks 13a to 13e, and every number in its text is computed by one of them.

### 13.1 What this chapter is for

**The problem.** Chapter 14 asks for the lowest-energy state (the **ground state**) and the first excited state of a fixed number $N$ of dirac16complex quanta that interact with each other inside the author's primordial gravitational field. A quantum state of one particle in ordinary three-dimensional space is a complex-valued function of three variables (its **wave function**, defined in Section 13.2). If we store such a function on a grid with 10 points along each coordinate, we need $10^3$ complex numbers. The state of two particles is a function of 6 variables, $10^6$ numbers; the state of ten particles a function of 30 variables, $10^{30}$ numbers, more than every computer on Earth can hold together. Every added particle multiplies the work by $10^3$. This growth is called the **exponential wall** of the many-body problem.

**The way around it.** DFT works with the **density** $n$ of the particles instead of their wave function: the expected number of particles per unit volume at each point of space. The density is a function of three variables, whatever $N$ is. Sections 13.8 to 13.10 prove that the density alone fixes the ground-state energy, and they show how Kohn and Sham turned this fact into equations that a computer can solve: one-particle equations in an effective potential, solved again and again until the potential and the density agree (**self-consistency**). The price is one quantity, the **exchange-correlation energy**, that is not known exactly and must be approximated. We will see exactly where the approximation enters and what it is.

**Plan.** Sections 13.2 to 13.7 are the quantum mechanics of many identical fermions: one particle, many particles, Slater determinants, creation and annihilation operators with Wick's theorem, the energy of a determinant with its direct and exchange parts, the Hartree-Fock equations, and an exactly solvable model of two electrons on two sites. Sections 13.8 to 13.10 are density functional theory proper: the Hohenberg-Kohn theorem, functional derivatives and the Kohn-Sham equations. Notebook 13c (Sections 13.11 to 13.14) checks all of this with numbers. Sections 13.15 and 13.16 compute the exchange energy of a uniform gas, show that for a contact interaction it is exactly local, and carry the result over to the 16-component field dirac16complex, reproducing the exchange formulas of the Revision record (Notebook 13b, Sections 13.17 to 13.20). Section 13.21 explains how the self-consistency loop is solved and why it can fail (Notebook 13d, Sections 13.22 to 13.25). Sections 13.26 and 13.27 extend everything to a finite temperature (Mermin's theorem) and to excited states (the Kohn-Sham gap, Janak's theorem and the Delta-SCF method), checked in Notebook 13e (Sections 13.28 to 13.31). Section 13.32 puts all the pieces together in one complete Kohn-Sham calculation, eight fermions in a trap, solved in Notebook 13a (Sections 13.33 to 13.36). Section 13.37 says what of this chapter is used for dirac16complex, Section 13.38 lists what was proved, computed and assumed, and Section 13.39 has exercises with complete answers.

**The order of the notebooks.** The notebooks are lettered in the order in which they were planned, and the chapter presents them in the order in which their ideas are needed: 13c, 13b, 13d, 13e, and last 13a, the complete calculation, which uses every idea of the others.

**Units.** In this chapter Planck's constant divided by $2\pi$ and the particle mass are set to 1 ($\hbar = m = 1$), so the kinetic-energy operator of one particle on a line is $-\tfrac12\,d^2/dx^2$. Each notebook states its other units (the hopping $t$ of the two-site model, the trap frequency of Notebook 13a). A temperature is measured as an energy (Boltzmann's constant is 1).

**Symbols with a local meaning.** Several letters mean something else in this chapter than in the rest of the book. (i) $x$ is the position of a particle, or a point of a grid, or (in Section 13.21) the excess of charge on one site; it is never one of the author's spacetime coordinates $x_1, \dots, x_8$, which appear only in Sections 13.16 and 13.37 and are named there. (ii) $\Psi$ is the wave function of $N$ particles, except in Sections 13.16 and 13.37, where it is the dirac16complex field, as those sections say. (iii) $\rho$ is a density matrix (Section 13.4) or a density operator (Section 13.26), not an energy density. (iv) $t$ is the hopping between two sites, $T$ the temperature and $T_s$ a kinetic energy. (v) $S$ is a one-body quantity $\sum V_{pq}a_p^\dagger a_q$ in Section 13.4, the symmetric two-site state in Section 13.7, the scalar density of dirac16complex in Sections 13.16 to 13.20 and 13.37, and the entropy in Sections 13.26 to 13.31. (vi) $U$ is the repulsion of two electrons on one site in the two-site model, $U_{kp}$ the entries of a unitary matrix, and $U(S)$ the interaction potential of dirac16complex in Section 13.16. (vii) $g$ counts the internal labels of a particle and $g_c$ is the strength of a contact interaction; neither is the metric. (viii) $H$ and $\hat H$ are Hamiltonians (energy operators); the author's constant $H$ of the metric appears only in Section 13.37.

### 13.2 One quantum particle: states, operators and the variational principle

**States on a grid.** The state of one particle on a line is a complex-valued function $\phi(x)$, its **wave function**. Its squared modulus $|\phi(x)|^2 = \phi^*(x)\,\phi(x)$ (the star means complex conjugate) is the probability per unit length of finding the particle at $x$, so a physical state is **normalised**: $\int |\phi|^2\,dx = 1$. On a computer the line is replaced by $M$ equally spaced points $x_k$, $k = 1, \dots, M$, with the spacing $h$, and a state becomes a column of $M$ numbers $(\phi_1, \dots, \phi_M)$; integrals become sums, $\int f\,dx \approx \sum_k f_k\,h$. Two states are compared by their **inner product**

$$
\langle \chi | \phi \rangle = \int \chi^*(x)\,\phi(x)\,dx \approx \sum_k \chi_k^*\,\phi_k\,h .
$$

It is linear in $\phi$, it gives the complex conjugate when the two states are exchanged, $\langle \phi|\chi\rangle = \langle \chi|\phi\rangle^*$, and $\langle \phi|\phi\rangle \ge 0$. Two states with $\langle \chi|\phi\rangle = 0$ are **orthogonal**; a set of normalised, pairwise orthogonal states is **orthonormal**.

**Operators.** A measurable quantity is represented by a linear **operator** $A$: a rule that turns a state into a state, with $A(c_1\phi + c_2\chi) = c_1 A\phi + c_2 A\chi$ for numbers $c_1, c_2$. On a grid an operator is an $M \times M$ matrix. It is **Hermitian** when $\langle \chi | A\phi\rangle = \langle A\chi|\phi\rangle$ for all states; for a matrix this means that it equals its conjugate transpose, $A^\dagger = A$ (for a real matrix: it is symmetric). The **expectation value** $\langle A\rangle = \langle\phi|A\phi\rangle$ in a normalised state is the average of many measurements. The energy operator of one particle in an external potential $v(x)$ is the **Hamiltonian**

$$
h = -\frac12\,\frac{d^2}{dx^2} + v(x).
$$

On the grid the second derivative is replaced by the **difference formula** $(\phi_{k+1} - 2\phi_k + \phi_{k-1})/h^2$, which follows from the Taylor expansions $\phi_{k\pm1} = \phi_k \pm h\,\phi'_k + \tfrac12 h^2\phi''_k \pm \tfrac16 h^3 \phi'''_k + O(h^4)$: adding them, the odd powers cancel, and the error is of order $h^2$. So $-\tfrac12\,d^2/dx^2$ becomes the symmetric matrix with $1/h^2$ on the diagonal and $-1/(2h^2)$ just above and below it. A state with $h\phi = \epsilon\,\phi$ is an **eigenstate** (a stationary state) with the energy $\epsilon$, an **eigenvalue** of $h$.

**Two facts about Hermitian operators, line by line.** Let $A\phi = a\,\phi$ with $\phi \ne 0$. Then

$$
a\,\langle\phi|\phi\rangle = \langle\phi|A\phi\rangle = \langle A\phi|\phi\rangle = a^*\,\langle\phi|\phi\rangle .
$$

The first equality puts $A\phi = a\phi$ into the second slot (linearity); the second is the definition of Hermitian; the third puts $A\phi = a\phi$ into the first slot, where a number comes out complex conjugated. Since $\langle\phi|\phi\rangle > 0$, we may divide by it: $a = a^*$, **the eigenvalues are real**. Next let $A\phi = a\phi$ and $A\chi = b\chi$ with $a \ne b$ (both real by the first fact). Then

$$
b\,\langle\phi|\chi\rangle = \langle\phi|A\chi\rangle = \langle A\phi|\chi\rangle = a\,\langle\phi|\chi\rangle ,
$$

by the same three rules, so $(b - a)\langle\phi|\chi\rangle = 0$, and because $b - a \ne 0$, $\langle\phi|\chi\rangle = 0$: **eigenstates with different eigenvalues are orthogonal**. For a Hermitian matrix one can always choose an orthonormal basis of eigenvectors (the spectral theorem of linear algebra); numpy's function `eigh` returns exactly such a basis, with the eigenvalues in increasing order.

**Worked example: two sites.** Two grid points ("sites" L and R) and the hopping matrix

$$
h = \begin{pmatrix} 0 & -t \\ -t & 0 \end{pmatrix}, \qquad t > 0 .
$$

The eigenvalues solve $\det(h - \epsilon) = \epsilon^2 - t^2 = 0$, so $\epsilon = \pm t$. For $\epsilon = -t$ the first row of $(h + t)\phi = 0$ reads $t\phi_L - t\phi_R = 0$, so $\phi_L = \phi_R$, and normalised $\phi = (1, 1)/\sqrt2$ (the **bonding** orbital, lower energy); for $\epsilon = +t$ we get $(1, -1)/\sqrt2$ (antibonding). They are orthogonal: $(1\cdot 1 + 1\cdot(-1))/2 = 0$.

**The variational principle, line by line.** Let $\phi_0, \phi_1, \dots$ be an orthonormal basis of eigenvectors of a Hermitian $H$ with eigenvalues $E_0 \le E_1 \le \dots$, and let $\phi = \sum_n c_n \phi_n$ be any normalised state. Then

$$
\langle\phi|H\phi\rangle = \sum_{n,m} c_m^* c_n\,\langle\phi_m|H\phi_n\rangle = \sum_{n,m} c_m^* c_n E_n\,\delta_{mn} = \sum_n |c_n|^2 E_n .
$$

The first step expands both slots (linearity in the second slot, conjugation in the first); the second uses $H\phi_n = E_n\phi_n$ and orthonormality, $\langle\phi_m|\phi_n\rangle = \delta_{mn}$ (1 if $m = n$, else 0); the third keeps only $m = n$. Since every $E_n \ge E_0$ and $\sum_n|c_n|^2 = \langle\phi|\phi\rangle = 1$,

$$
\sum_n |c_n|^2 E_n \;\ge\; E_0\sum_n|c_n|^2 = E_0 ,
$$

with equality exactly when only the $c_n$ with $E_n = E_0$ are nonzero. So **the ground-state energy is the smallest expectation value of the energy over all normalised states**, and the states that reach it are the ground states. Every method of this chapter is an application of this inequality.

**Internal labels.** Real particles carry a label besides their position: an electron has a spin with two values, up and down. A particle with $g$ labels has a wave function $\phi(x, \sigma)$ with $\sigma = 1, \dots, g$. The quanta of dirac16complex in the sector of Chapter 14 have $g = 8$ states for each momentum (Section 13.16).

### 13.3 Many identical fermions and Slater determinants

**The many-particle wave function.** $N$ particles are described by one complex function of all their positions and labels, $\Psi(x_1\sigma_1, \dots, x_N\sigma_N)$. Its squared modulus is the probability density of finding particle 1 at $x_1$ with label $\sigma_1$, particle 2 at $x_2$ with $\sigma_2$, and so on. (In this paragraph the letters $x_1, \dots, x_N$ are the positions of particles $1, \dots, N$, not spacetime coordinates.)

**Identical particles and the Pauli principle.** No experiment can tell two electrons apart, so $|\Psi|^2$ must not change when two particles are exchanged. Nature realises this in two ways: for **bosons** $\Psi$ itself is unchanged, for **fermions** it changes sign:

$$
\Psi(\dots, x_i\sigma_i, \dots, x_j\sigma_j, \dots) = -\,\Psi(\dots, x_j\sigma_j, \dots, x_i\sigma_i, \dots) \qquad \text{(fermions)} .
$$

Electrons, protons and neutrons are fermions, and so are the quanta of dirac16complex, whose components are anticommuting (Grassmann) numbers (Chapter 7). That a field describes fermions is an ASSUMED property of the field: it is built into dirac16complex by the choice of Grassmann components. Put $x_i\sigma_i = x_j\sigma_j$ in the rule above: then $\Psi = -\Psi$ at such points, so $\Psi = 0$ there. **Two identical fermions are never found at the same place with the same label** (the Pauli principle).

**The many-body Hamiltonian.** For $N$ particles in an external potential $v$ with a pair interaction $w$,

$$
\hat H = \sum_{i=1}^{N}\Big[-\frac12\,\frac{\partial^2}{\partial x_i^2} + v(x_i)\Big] + \sum_{i<j} w(x_i, x_j) = \hat T + \hat V + \hat W .
$$

Only $\hat V$ distinguishes one system from another: all atoms with $N$ electrons share the same kinetic energy $\hat T$ and interaction $\hat W$. This observation is the seed of DFT.

**The density.** The density is the expected number of particles per unit length at $x$,

$$
n(x) = N\sum_{\sigma}\int |\Psi(x\sigma, x_2\sigma_2, \dots, x_N\sigma_N)|^2\,dx_2\cdots dx_N
$$

(the sum over $\sigma$ also includes the sums over $\sigma_2, \dots, \sigma_N$). The factor $N$ appears because any of the $N$ identical particles may be the one at $x$, and antisymmetry makes all $N$ choices give the same integral; so $\int n\,dx = N$. The external energy needs only the density: $\langle\Psi|\hat V\Psi\rangle = \int v(x)\,n(x)\,dx$, because each of the $N$ terms $v(x_i)$ gives the same integral.

**Slater determinants for two particles.** Take two orthonormal one-particle states $\phi_a$, $\phi_b$ (**orbitals**; we write $r$ for the position and label of one particle together). The product $\phi_a(r_1)\phi_b(r_2)$ is not antisymmetric, but

$$
\Phi(r_1, r_2) = \frac{1}{\sqrt2}\big[\phi_a(r_1)\phi_b(r_2) - \phi_b(r_1)\phi_a(r_2)\big] = \frac{1}{\sqrt2}\det\begin{pmatrix}\phi_a(r_1) & \phi_b(r_1)\\ \phi_a(r_2) & \phi_b(r_2)\end{pmatrix}
$$

is: exchanging $r_1$ and $r_2$ exchanges the two rows of the determinant, which changes its sign. If $\phi_a = \phi_b$ the two columns are equal and $\Phi = 0$: two fermions cannot occupy the same orbital. The norm follows line by line:

$$
\begin{aligned}
\int\!\!\int |\Phi|^2 &= \tfrac12\int\!\!\int \big[|\phi_a(r_1)|^2|\phi_b(r_2)|^2 + |\phi_b(r_1)|^2|\phi_a(r_2)|^2\big] - \tfrac12\int\!\!\int 2\,\mathrm{Re}\big[\phi_a^*(r_1)\phi_b(r_1)\,\phi_b^*(r_2)\phi_a(r_2)\big] \\
&= \tfrac12\,(1\cdot 1 + 1\cdot 1) - \mathrm{Re}\big[\langle\phi_a|\phi_b\rangle\langle\phi_b|\phi_a\rangle\big] = 1 - 0 = 1 .
\end{aligned}
$$

The first line multiplies out $|u - v|^2 = |u|^2 + |v|^2 - 2\,\mathrm{Re}(u^* v)$; the second integrates each factor separately (the integral of a product of a function of $r_1$ and a function of $r_2$ is the product of the integrals), uses the normalisation of $\phi_a$ and $\phi_b$, and uses their orthogonality, $\langle\phi_a|\phi_b\rangle = 0$.

**$N$ particles.** For $N$ orthonormal orbitals $\phi_1, \dots, \phi_N$ the **Slater determinant** is $\Phi = \det[\phi_a(r_i)]/\sqrt{N!}$, the determinant of the $N \times N$ table whose row $i$ holds the values of all orbitals at the position of particle $i$. The same three properties hold, by the same rules of determinants: exchanging two particles exchanges two rows (antisymmetry); two equal orbitals make two columns equal ($\Phi = 0$); and $\Phi$ is normalised. Its density is the sum of the orbital densities,

$$
n(r) = \sum_{a=1}^{N}|\phi_a(r)|^2 .
$$

For two particles this follows from the definition of $n$: $n(r) = 2\int|\Phi(r, r_2)|^2\,dr_2 = |\phi_a(r)|^2\cdot 1 + |\phi_b(r)|^2\cdot 1 - 2\,\mathrm{Re}[\phi_a^*(r)\phi_b(r)\langle\phi_b|\phi_a\rangle] = |\phi_a(r)|^2 + |\phi_b(r)|^2$ (multiply out as above, integrate over $r_2$ only, use orthonormality). A Slater determinant is the state of $N$ **independent** fermions; a general antisymmetric state is a sum of many determinants. Kohn-Sham theory (Section 13.10) rests on the fact that a single determinant can nevertheless carry the exact density.

**Worked example (Notebook 13c, In [2]).** Let space be three points $r = 0, 1, 2$ (no label), with the orthonormal orbitals $\phi_0 = (1, 0, 0)$ and $\phi_1 = (0, 1, 1)/\sqrt2$. Then $\Phi(0, 1) = [\phi_0(0)\phi_1(1) - \phi_1(0)\phi_0(1)]/\sqrt2 = [1\cdot\tfrac{1}{\sqrt2} - 0]/\sqrt2 = \tfrac12$, and $\Phi(1, 2) = [0\cdot\tfrac{1}{\sqrt2} - \tfrac{1}{\sqrt2}\cdot 0]/\sqrt2 = 0$. The nine values are $\pm\tfrac12$ (four of them) and 0 (five of them, among them the three diagonal values), so $\sum|\Phi|^2 = 4\cdot\tfrac14 = 1$, and the density is $n(r) = 2\sum_{r_2}|\Phi(r, r_2)|^2 = (1, \tfrac12, \tfrac12) = \phi_0^2 + \phi_1^2$. Figure 13c.1 draws this table and a determinant of two fermions in a box.

### 13.4 Creation and annihilation operators and Wick's theorem

Determinants are long to write. **Second quantisation** labels a determinant only by which orbitals it uses. It is the same formalism that Chapter 10 uses for the quantised dirac16complex field, here in its simplest form.

**Occupation numbers.** Fix an orthonormal basis of $M$ orbitals $\phi_0, \dots, \phi_{M-1}$. A determinant built from some of them is fixed, up to its sign, by the **occupation numbers** $n_p \in \{0, 1\}$, $n_p = 1$ when $\phi_p$ is used. We write it $|n_0 n_1 \cdots n_{M-1}\rangle$ and fix the sign by listing the occupied orbitals in increasing order of $p$ as the columns of the determinant. The state without any particle is the **vacuum** $|0\rangle$. With $M = 4$ orbitals there are $2^4 = 16$ such states; numbering them $s = 0, \dots, 15$, the occupation $n_p$ is the binary digit (bit) $p$ of $s$, so for example $s = 5 = 1 + 4$ occupies the orbitals 0 and 2.

**The operators.** The **creation operator** $a_p^\dagger$ adds a particle in orbital $p$, the **annihilation operator** $a_p$ removes one:

$$
\begin{aligned}
a_p^\dagger\,|\cdots n_p \cdots\rangle &= (-1)^{\nu_p}\,(1 - n_p)\,|\cdots n_p{+}1 \cdots\rangle ,\\
a_p\,|\cdots n_p \cdots\rangle &= (-1)^{\nu_p}\,n_p\,|\cdots n_p{-}1 \cdots\rangle ,\qquad \nu_p = \sum_{q<p} n_q .
\end{aligned}
$$

The factor $1 - n_p$ makes $a_p^\dagger$ give zero on an occupied orbital (Pauli), the factor $n_p$ makes $a_p$ give zero on an empty one, and the sign $(-1)^{\nu_p}$ is the sign that a determinant picks up when the column of orbital $p$ is moved past the $\nu_p$ occupied columns in front of it (each exchange of two columns changes the sign). On the 16 states of four orbitals each $a_p$ is a $16 \times 16$ matrix of zeros and $\pm1$, and $a_p^\dagger$ is its transpose (Figure 13c.2 draws two of them).

**The anticommutation relations.** With the **anticommutator** $\{A, B\} = AB + BA$,

$$
\{a_p, a_q^\dagger\} = \delta_{pq}, \qquad \{a_p, a_q\} = 0, \qquad \{a_p^\dagger, a_q^\dagger\} = 0 .
$$

Proof for $p = q$, on a state with $n_p = 0$: $a_p^\dagger$ creates the particle with the sign $(-1)^{\nu_p}$, and $a_p$ removes it again with the same sign (the orbitals before $p$ are unchanged), so $a_p a_p^\dagger$ gives the state back with the sign $(-1)^{2\nu_p} = +1$; and $a_p^\dagger a_p$ gives 0 because $a_p$ acts on an empty orbital. The sum is 1. On a state with $n_p = 1$ the two roles are exchanged, and the sum is again 1. For $p < q$: whichever of the two operators acts on orbital $p$ changes $n_p$, which changes $\nu_q$ by one and so flips the sign factor of the operator acting on $q$; the two orders therefore give the same state with opposite signs, and their sum vanishes. In particular $a_p^\dagger a_p^\dagger = 0$: the Pauli principle once more. The **number operator** $\hat n_p = a_p^\dagger a_p$ gives $n_p$, and $\hat N = \sum_p \hat n_p$ counts the particles of a state.

**Operators of the many-body theory.** A one-body operator, one copy $A(i)$ of a one-particle operator $A$ for each particle, becomes $\hat A = \sum_{p,q} A_{pq}\,a_p^\dagger a_q$ with $A_{pq} = \langle\phi_p|A\phi_q\rangle$: applied to a determinant, $\sum_i A(i)$ replaces one occupied orbital $\phi_q$ at a time by $A\phi_q = \sum_p \phi_p A_{pq}$, and "remove $q$, put $p$, with the weight $A_{pq}$" is what $A_{pq}\,a_p^\dagger a_q$ does, sign included. The pair interaction is

$$
\hat W = \frac12\sum_{p,q,r,s} w_{pqrs}\,a_p^\dagger a_q^\dagger a_s a_r, \qquad w_{pqrs} = \int\!\!\int \phi_p^*(r)\,\phi_q^*(r')\,w(r, r')\,\phi_r(r)\,\phi_s(r')\,dr\,dr' ,
$$

where $\int dr$ includes the sum over the label. The operator removes an occupied pair $(r, s)$ and puts $(p, q)$ in its place; the factor $\tfrac12$ compensates for counting each pair twice, and the reversed order $a_s a_r$ makes the direct term come with a plus sign.

**Expectation values in a determinant.** Let $|\Phi\rangle$ occupy the set $O$ of basis orbitals, and write $[p \in O]$ for 1 if $p$ is occupied and 0 otherwise. Then

$$
\langle\Phi|a_p^\dagger a_q|\Phi\rangle = \delta_{pq}\,[p \in O] .
$$

Reason: $a_q$ removes $q$, and $a_p^\dagger$ must put back the same orbital to return to $|\Phi\rangle$, because states with different occupations are orthogonal; for $p = q$ the operator is $\hat n_p$, which gives $[p \in O]$. For four operators the pair removed must be the pair put back, $\{p, q\} = \{r, s\}$ with $p \ne q$:

$$
\langle\Phi|a_p^\dagger a_q^\dagger a_s a_r|\Phi\rangle = [p\in O]\,[q\in O]\,\big(\delta_{pr}\delta_{qs} - \delta_{ps}\delta_{qr}\big) .
$$

If $p = r$ and $q = s$ the operator is $a_p^\dagger a_q^\dagger a_q a_p = a_p^\dagger \hat n_q a_p = \hat n_q\hat n_p$ (for $q \ne p$, $\hat n_q$ commutes with $a_p$ and $a_p^\dagger$, because moving $a_p$ past the pair $a_q^\dagger a_q$ costs two sign changes), which gives $[p\in O][q\in O]$; if $p = s$ and $q = r$, one exchange $a_q a_p = -a_p a_q$ gives the minus sign. Both formulas are summarised by the **one-body density matrix** $\rho = \sum_{a\in O}|\phi_a\rangle\langle\phi_a|$, whose matrix elements are $\rho_{qp} = \langle a_p^\dagger a_q\rangle$:

$$
\langle a_p^\dagger a_q\rangle = \rho_{qp}, \qquad \langle a_p^\dagger a_q^\dagger a_s a_r\rangle = \rho_{rp}\,\rho_{sq} - \rho_{sp}\,\rho_{rq} .
$$

This is **Wick's theorem** for a determinant: every expectation value is a sum of products of the density matrix. For a determinant $\rho$ is a projector: $\rho^2 = \rho$ (applying "project on the occupied orbitals" twice is the same as once), and $\mathrm{Tr}\,\rho = N$.

**Every basis.** If new orbitals are made from the old ones by a unitary matrix $U$ ($U^\dagger U = 1$), $\phi'_p = \sum_k \phi_k U_{kp}$, then a determinant is linear in each of its columns, so the creation operator of $\phi'_p$ is $a_p'^\dagger = \sum_k U_{kp}\,a_k^\dagger$, and its adjoint is $a'_p = \sum_k U_{kp}^*\,a_k$. Expectation values are linear in the operator, so

$$
\langle a_p'^\dagger a'_q\rangle = \sum_{k,l} U_{kp}\,U_{lq}^*\,\langle a_k^\dagger a_l\rangle = \sum_{k,l} U^*_{lq}\,\rho_{lk}\,U_{kp} = (U^\dagger\rho\,U)_{qp} ,
$$

which is the matrix element of the same $\rho$ between the new orbitals; the four-operator formula transforms in the same way, factor by factor. So Wick's theorem holds in every orthonormal basis. It also holds, with occupations $f_a$ between 0 and 1 in place of 0 and 1, for a **thermal ensemble** of non-interacting fermions (Section 13.26 shows that the occupations of different orbitals are then independent, which is all the proof needs). Notebook 13c checks all $16 + 256$ two- and four-operator values in a randomly rotated basis, for a determinant and for a thermal ensemble (In [6] and In [7]).

**The normal-ordered square of a one-body quantity.** The interaction of the dirac16complex Kohn-Sham model (Section 13.16) is the square of a one-body quantity $S = \sum_{p,q} V_{pq}\,a_p^\dagger a_q$ with a Hermitian matrix $V$ (the **vertex**). Its **normal-ordered square** puts all creation operators to the left: ${:}S^2{:} = \sum V_{pq}V_{rs}\,a_p^\dagger a_r^\dagger a_s a_q$. Line by line:

$$
\begin{aligned}
\langle {:}S^2{:}\rangle &= \sum_{p,q,r,s} V_{pq}V_{rs}\,\langle a_p^\dagger a_r^\dagger a_s a_q\rangle \\
&= \sum_{p,q,r,s} V_{pq}V_{rs}\,\big(\rho_{qp}\,\rho_{sr} - \rho_{sp}\,\rho_{qr}\big) \\
&= \Big(\sum_{p,q}V_{pq}\rho_{qp}\Big)\Big(\sum_{r,s}V_{rs}\rho_{sr}\Big) - \sum_{p,q,r,s}V_{pq}\,\rho_{qr}\,V_{rs}\,\rho_{sp} \\
&= (\mathrm{Tr}\,V\rho)^2 - \mathrm{Tr}(V\rho\,V\rho) .
\end{aligned}
$$

The first line uses the linearity of expectation values; the second is Wick's four-operator formula with the indices renamed (its $q, s, r$ are here $r, s, q$); the third splits the first product into two independent sums and reorders the factors of the second; the fourth recognises the sums as traces of matrix products ($\mathrm{Tr}\,AB = \sum_{p,q}A_{pq}B_{qp}$). The first term is a **Hartree** (direct) term, the second an **exchange** term. PROVED here, and recorded in the Revision record as the check hf_wick_contraction of `Revision/kohn_sham/reports/ks-theory-python.json` (brute force on a two-mode state); Notebook 13c (In [8]) checks it on four orbitals with a random Hermitian vertex.

### 13.5 The energy of a determinant: direct and exchange terms

**The formula.** The Hamiltonian in second quantisation is $\hat H = \sum h_{pq}\,a_p^\dagger a_q + \tfrac12\sum w_{pqrs}\,a_p^\dagger a_q^\dagger a_s a_r$ with $h = -\tfrac12\,d^2/dx^2 + v$. For the determinant of the basis orbitals in $O$, line by line:

$$
\begin{aligned}
\langle\Phi|\hat H|\Phi\rangle &= \sum_{p,q} h_{pq}\,\delta_{pq}[p\in O] + \tfrac12\sum_{p,q,r,s} w_{pqrs}\,[p\in O][q\in O]\,(\delta_{pr}\delta_{qs} - \delta_{ps}\delta_{qr}) \\
&= \sum_{a\in O} h_{aa} + \tfrac12\sum_{a,b\in O}\big(w_{abab} - w_{abba}\big) .
\end{aligned}
$$

The first line inserts the two expectation values of Section 13.4; the second carries out the sums over the Kronecker deltas ($\delta_{pr}$ sets $r = p$, and so on) and renames $p, q$ as $a, b$. Notebook 13c (In [10]) checks this formula for random one-body and two-body integrals.

**Direct and exchange in space.** Writing out the integrals and using $\sum_{a\in O}\phi_a(r)\phi_a^*(r') = \rho(r, r')$ (the density matrix in space, whose diagonal is the density $n$):

$$
\begin{aligned}
E_H &= \tfrac12\sum_{a,b} w_{abab} = \tfrac12\int\!\!\int n(r)\,w(r,r')\,n(r')\,dr\,dr' ,\\
E_x &= -\tfrac12\sum_{a,b} w_{abba} = -\tfrac12\int\!\!\int |\rho(r,r')|^2\,w(r,r')\,dr\,dr' .
\end{aligned}
$$

$E_H$ is the **Hartree energy**: the classical energy of the cloud $n$ with itself. $E_x$ is the **exchange energy** (the Fock term); it has no classical analogue, it comes from the antisymmetry of $\Phi$, and for a repulsive $w$ it lowers the energy. Three remarks. (1) **No self-interaction.** In $E_H$ the terms $a = b$ describe a particle repelling its own cloud, which is unphysical; in $E_x$ the terms $a = b$ are the same numbers with a minus sign, so they cancel. (2) **Exchange acts only between equal labels.** If every orbital has a definite label, $\rho(x\sigma, x'\sigma') = 0$ for $\sigma \ne \sigma'$, so for a label-independent $w$ the exchange term couples only particles with the same label. (3) **Double counting.** Adding orbital energies counts every pair twice (Section 13.6).

**The contact interaction.** Let the particles interact only when they are at the same point, with the strength $g_c$ and independently of their labels: $w(x\sigma, x'\sigma') = g_c\,\delta(x - x')$, where $\delta$ is Dirac's delta function ($\int f(x')\,\delta(x - x')\,dx' = f(x)$). For orbitals of definite label, with the label densities $n_\sigma(x) = \rho(x\sigma, x\sigma)$, line by line:

$$
\begin{aligned}
E_x &= -\tfrac12\sum_{\sigma,\sigma'}\int\!\!\int |\rho(x\sigma, x'\sigma')|^2\,g_c\,\delta(x - x')\,dx\,dx' \\
&= -\tfrac{g_c}{2}\sum_{\sigma,\sigma'}\int |\rho(x\sigma, x\sigma')|^2\,dx \\
&= -\tfrac{g_c}{2}\int\sum_{\sigma} n_\sigma(x)^2\,dx .
\end{aligned}
$$

The first line writes the space-and-label integral as a sum over both labels and integrals over both positions; the second does the $x'$ integral with the delta function; the third keeps only $\sigma' = \sigma$ (the other terms vanish for orbitals of definite label) and uses $\rho(x\sigma, x\sigma) = n_\sigma(x)$. In the same way $E_H = \tfrac{g_c}{2}\int n^2\,dx$. Two facts follow. **First, the exchange energy of a contact interaction is exactly local**: an integral over one point of a function of the densities at that point, although the general exchange integral involves two points. **Second**, if all $g$ labels are equally occupied, $n_\sigma = n/g$, then $\sum_\sigma n_\sigma^2 = g\,(n/g)^2 = n^2/g$, and

$$
E_x = -\frac{1}{g}\,E_H \qquad \text{(contact interaction, $g$ equally occupied labels)} .
$$

For $g = 2$: $E_H + E_x = \tfrac{g_c}{2}\int\big[(n_\uparrow + n_\downarrow)^2 - n_\uparrow^2 - n_\downarrow^2\big]dx = g_c\int n_\uparrow n_\downarrow\,dx$. Two fermions with the same label never meet (Pauli), so only opposite labels feel a contact force, and exchange removes exactly the unphysical same-label part of $E_H$. For a single label ($g = 1$) the contact interaction cancels completely. PROVED here; Notebook 13b checks it for the uniform gas, for a non-uniform determinant and with label-mixing orbitals (In [6], In [12], In [13]).

### 13.6 The Hartree and Hartree-Fock equations

The **Hartree-Fock approximation** takes the best single determinant: it minimises $\langle\Phi|\hat H|\Phi\rangle$ over all choices of $N$ orthonormal orbitals. By the variational principle (Section 13.2) its energy $E_{HF}$ is an upper bound on the true ground-state energy $E_0$.

**Minimising with side conditions: Lagrange multipliers.** To minimise a function $f(y_1, \dots, y_m)$ of $m$ real variables under a side condition $c(y) = c_0$, look at a small step $dy$ that keeps the condition: it changes $c$ by $dc = \sum_i (\partial c/\partial y_i)\,dy_i = 0$. At a minimum the change $df = \sum_i(\partial f/\partial y_i)\,dy_i$ must vanish for every such step (otherwise the step or the opposite step would lower $f$). Write the gradient of $f$ as $\partial f/\partial y_i = \lambda\,\partial c/\partial y_i + r_i$, where $\lambda$ is chosen so that the rest $r$ is perpendicular to the gradient of $c$, $\sum_i r_i\,\partial c/\partial y_i = 0$. Then the step $dy_i = \epsilon\,r_i$ keeps the condition, and

$$
0 = df = \epsilon\sum_i \big(\lambda\,\partial c/\partial y_i + r_i\big)\,r_i = \epsilon\sum_i r_i^2 ,
$$

where the first equality is the condition for a minimum, the second inserts the split gradient, and the third uses the perpendicularity of $r$. So every $r_i = 0$: **at a constrained minimum, $\partial f/\partial y_i = \lambda\,\partial c/\partial y_i$ for every $i$**. The number $\lambda$ is a **Lagrange multiplier**; with several conditions one takes one multiplier for each. (That a first-order step can be completed to a step that keeps the condition exactly is the implicit function theorem of analysis, used here without proof.) Differentiating the minimum value $f^*(c_0)$ by the chain rule shows that $df^*/dc_0 = \lambda$: the multiplier is the rate at which the constrained minimum changes with the condition.

**The Hartree-Fock equations.** A complex orbital $\phi = u + iv$ has two real parts; varying $\phi$ and $\phi^*$ as if they were independent is equivalent, because $u$ and $v$ are recovered from them. Add multipliers $\Lambda_{ba}$ for the conditions $\langle\phi_a|\phi_b\rangle = \delta_{ab}$ and set the derivative of $\sum_a h_{aa} + \tfrac12\sum_{a,b}(w_{abab} - w_{abba}) - \sum_{a,b}\Lambda_{ba}(\langle\phi_a|\phi_b\rangle - \delta_{ab})$ with respect to $\phi_a^*(r)$ to zero. Orbital $a$ appears in the first and in the second slot of $w_{abab}$ and $w_{abba}$; because $w(r, r') = w(r', r)$ the two contributions are equal, which cancels the $\tfrac12$. The result is

$$
\hat F\phi_a = \sum_b \Lambda_{ba}\,\phi_b, \qquad (\hat F\phi)(r) = h\phi(r) + v_H(r)\,\phi(r) - \int\rho(r, r')\,w(r, r')\,\phi(r')\,dr' ,
$$

with the **Hartree potential** $v_H(r) = \int w(r, r')\,n(r')\,dr'$. $\hat F$ is the **Fock operator**. It depends on the occupied orbitals only through $\rho$, which does not change when the occupied orbitals are mixed among themselves by a unitary matrix; such a mixing can make the Hermitian matrix $\Lambda$ diagonal, which gives the **canonical Hartree-Fock equations** $\hat F\phi_a = \epsilon_a\phi_a$. They look like one-particle equations, but $\hat F$ contains the unknown orbitals: they are **nonlinear** and are solved by iteration, starting from a guess and repeating until nothing changes any more (**self-consistency**, Section 13.21). For the ground state one occupies the $N$ orbitals with the lowest $\epsilon_a$ (the **aufbau** rule, German for "building up"). The older **Hartree approximation** keeps $v_H$ and drops the exchange integral, and with it the cancellation of the self-interaction.

**Double counting.** Summing the orbital energies over the occupied orbitals,

$$
\sum_{a\in O}\epsilon_a = \sum_a\langle\phi_a|\hat F\phi_a\rangle = \sum_a h_{aa} + \sum_{a,b}(w_{abab} - w_{abba}) = \sum_a h_{aa} + 2E_H + 2E_x ,
$$

where the first step uses $\hat F\phi_a = \epsilon_a\phi_a$ and normalisation, the second inserts the definition of $\hat F$, and the third the definitions of $E_H$ and $E_x$ of Section 13.5. Comparing with the energy of the determinant,

$$
E_{HF} = \sum_{a\in O}\epsilon_a - E_H - E_x .
$$

**Koopmans' theorem.** Removing the particle of orbital $a$ while the other orbitals are kept unchanged lowers the energy by $h_{aa} + \sum_b(w_{abab} - w_{abba}) = \langle\phi_a|\hat F\phi_a\rangle = \epsilon_a$: the orbital energy is the energy of that particle in the unrelaxed determinant. The Kohn-Sham analogue, Janak's theorem, is proved in Section 13.27.

### 13.7 Two electrons on two sites: exact and Hartree-Fock

The smallest system in which the interaction matters: two sites L and R with one orbital each, the hopping $t$ of Section 13.2 between them, a repulsion $U > 0$ when both electrons sit on the same site, and two electrons with opposite labels. In second quantisation, with the four orbitals L up, R up, L down, R down (numbers 0, 1, 2, 3) and site energies $-\Delta/2$ on L and $+\Delta/2$ on R,

$$
\hat H = -t\sum_\sigma\big(a_{L\sigma}^\dagger a_{R\sigma} + a_{R\sigma}^\dagger a_{L\sigma}\big) + U\big(\hat n_{L\uparrow}\hat n_{L\downarrow} + \hat n_{R\uparrow}\hat n_{R\downarrow}\big) - \tfrac{\Delta}{2}\hat n_L + \tfrac{\Delta}{2}\hat n_R ,
$$

with $\hat n_L = \hat n_{L\uparrow} + \hat n_{L\downarrow}$. In this section $\Delta = 0$.

**Exact solution.** Two electrons with opposite labels can be both on L (state LL), both on R (RR), or one on each, in the symmetric combination $S$ of "up on L, down on R" and "up on R, down on L"; the antisymmetric combination has energy 0 and plays no role. Hopping one electron turns LL into either of the two mixed states, which gives the matrix element $-\sqrt2\,t$ between LL and $S$ (two terms $-t$, and the normalisation $1/\sqrt2$ of $S$), and likewise between RR and $S$; the repulsion gives $U$ on LL and RR and 0 on $S$. In the basis (LL, RR, $S$)

$$
\hat H = \begin{pmatrix} U & 0 & -\sqrt2\,t \\ 0 & U & -\sqrt2\,t \\ -\sqrt2\,t & -\sqrt2\,t & 0 \end{pmatrix} .
$$

The combination $(LL - RR)/\sqrt2$ is decoupled, with the energy $U$. The combination $D = (LL + RR)/\sqrt2$ couples to $S$ with the element $\tfrac{1}{\sqrt2}(-\sqrt2\,t - \sqrt2\,t) = -2t$, which leaves the $2 \times 2$ matrix $\begin{pmatrix} U & -2t \\ -2t & 0\end{pmatrix}$. Its eigenvalues solve $\epsilon(\epsilon - U) - 4t^2 = 0$, so

$$
E_0 = \tfrac12\big(U - \sqrt{U^2 + 16t^2}\big) ,
$$

the lower root (it is negative, because $\sqrt{U^2 + 16t^2} > U$, so it is below the energies $0$ and $U$ of the other states). For $t = 1$, $U = 2$: $E_0 = \tfrac12(2 - \sqrt{20}) = -1.236068$ (Notebook 13c, In [11]).

**The energy of every determinant.** A determinant for two electrons of opposite labels uses one up orbital and one down orbital. Take the up orbital with the values $(\cos\alpha, \sin\alpha)$ on (L, R) and the down orbital $(\cos\beta, \sin\beta)$, $0 \le \alpha, \beta \le \pi/2$ (real positive values give the lowest hopping energy). The hopping energy of an orbital $(c_L, c_R)$ is $-2t\,c_L c_R$, which is $-2t\cos\alpha\sin\alpha = -t\sin2\alpha$ for the up orbital. The repulsion is a contact interaction on each site, so by Section 13.5 its Hartree plus exchange energy is $U$ times the product of the up and down densities on each site. Writing $c_\alpha = \cos2\alpha$ and $s_\alpha = \sin2\alpha$ (and the same for $\beta$), line by line:

$$
\begin{aligned}
E(\alpha, \beta) &= -t\,(s_\alpha + s_\beta) + U\big(\cos^2\!\alpha\,\cos^2\!\beta + \sin^2\!\alpha\,\sin^2\!\beta\big) \\
&= -t\,(s_\alpha + s_\beta) + \tfrac{U}{4}\big[(1 + c_\alpha)(1 + c_\beta) + (1 - c_\alpha)(1 - c_\beta)\big] \\
&= -t\,(s_\alpha + s_\beta) + \tfrac{U}{2}\big(1 + c_\alpha c_\beta\big) .
\end{aligned}
$$

The first line adds the two hopping energies and $U(n_{L\uparrow}n_{L\downarrow} + n_{R\uparrow}n_{R\downarrow})$; the second uses $\cos^2\alpha = \tfrac12(1 + \cos2\alpha)$ and $\sin^2\alpha = \tfrac12(1 - \cos2\alpha)$; the third multiplies out (the terms $\pm c_\alpha$, $\pm c_\beta$ cancel). Notebook 13c (In [12]) checks this formula against the expectation value of the Hamiltonian matrix.

**The best determinant.** Restricted Hartree-Fock puts both electrons into the bonding orbital, $\alpha = \beta = \pi/4$: $s = 1$, $c = 0$, so $E_{RHF} = -2t + U/2$. Is there a better determinant? Since $(c_\alpha + c_\beta)^2 \ge 0$, we have $c_\alpha c_\beta \ge -\tfrac12(c_\alpha^2 + c_\beta^2)$, and with $1 - c^2 = s^2$:

$$
E \;\ge\; -t\,(s_\alpha + s_\beta) + \tfrac{U}{2}\Big(1 - \tfrac{c_\alpha^2 + c_\beta^2}{2}\Big) = \Big(-t\,s_\alpha + \tfrac{U}{4}s_\alpha^2\Big) + \Big(-t\,s_\beta + \tfrac{U}{4}s_\beta^2\Big) .
$$

Each bracket is a parabola in one number $s \in [0, 1]$; its derivative $-t + \tfrac{U}{2}s$ vanishes at $s = 2t/U$. For $U \le 2t$ this lies at or beyond 1, so the smallest value on $[0, 1]$ is at $s = 1$, $-t + U/4$, and the minimum over all determinants is $E_{HF} = -2t + U/2$, the restricted one. For $U > 2t$ the smallest value is at $s = 2t/U$: $-t\cdot\tfrac{2t}{U} + \tfrac{U}{4}\cdot\tfrac{4t^2}{U^2} = -\tfrac{t^2}{U}$, so $E_{HF} = -2t^2/U$. Equality holds in the inequality for $\beta = \pi/2 - \alpha$ ($c_\beta = -c_\alpha$, $s_\beta = s_\alpha$): the **unrestricted** determinant puts the up electron mostly on one site and the down electron mostly on the other. It breaks the left-right symmetry of each label but keeps the total density $(1, 1)$. Figure 13c.6 shows the energy landscape $E(\alpha, \beta)$ at $U = 4t$, with the restricted point as a saddle.

**Correlation.** For $t = 1$, $U = 2$: $E_{HF} = -1$, and $E_c = E_0 - E_{HF} = -0.236068$ is the **correlation energy**, the energy that no single determinant can capture (it is never positive, by the variational principle). Its meaning is visible in the **double occupancy**, the probability that both electrons sit on the same site: $\tfrac12$ in the restricted determinant for every $U$, but only $0.276393$ in the exact ground state at $U = 2t$ (Notebook 13c, In [11]). The exact electrons avoid each other and keep each label shared equally between the sites; a single determinant cannot do both. Yet the density is the same, $(1, 1)$, in the exact state and in the Hartree-Fock state. A theory that works with the density alone must therefore contain somewhere the information that turns the density $(1, 1)$ into $-1.236068$ rather than $-1$. In DFT that information is the exchange-correlation energy.

### 13.8 The density decides everything: the Hohenberg-Kohn theorem

We now leave wave functions behind. Fix the particle number $N$ and the interaction $\hat W$, and regard the external potential $v$ as the only thing that distinguishes one system from another.

**Theorem (Hohenberg and Kohn, 1964).** Let $v$ and $v'$ be two external potentials whose Hamiltonians $\hat H = \hat T + \hat W + \hat V$ and $\hat H' = \hat T + \hat W + \hat V'$ have non-degenerate ground states $\Psi$ and $\Psi'$ (non-degenerate: no other state has the same lowest energy). If $v - v'$ is not a constant, the ground-state densities $n$ and $n'$ differ. So the ground-state density determines the potential up to a constant, hence the Hamiltonian, hence every property of the system.

**Proof, line by line.** First, $\Psi \ne \Psi'$. If they were equal, subtracting the two Schroedinger equations $\hat H\Psi = E_0\Psi$ and $\hat H'\Psi = E_0'\Psi$ would give $(\hat V - \hat V')\Psi = (E_0 - E_0')\Psi$, that is $\sum_i[v(x_i) - v'(x_i)] = E_0 - E_0'$ wherever $\Psi \ne 0$, which forces $v - v'$ to be a constant (this step ASSUMES that $\Psi$ does not vanish on a whole region, which holds for the potentials of physics). Now suppose, to reach a contradiction, that $n = n'$. Because $\Psi$ is the only ground state of $\hat H$ and $\Psi' \ne \Psi$, the variational principle holds with a strict inequality:

$$
E_0 < \langle\Psi'|\hat H\Psi'\rangle = \langle\Psi'|\hat H'\Psi'\rangle + \langle\Psi'|(\hat V - \hat V')\Psi'\rangle = E_0' + \int (v - v')\,n'\,dx .
$$

The first step is the strict variational principle; the second writes $\hat H = \hat H' + (\hat V - \hat V')$; the third uses $\hat H'\Psi' = E_0'\Psi'$ and the rule that an external energy needs only the density (Section 13.3). Exchanging the roles of the two systems gives in the same way

$$
E_0' < E_0 + \int (v' - v)\,n\,dx .
$$

Adding the two inequalities and using $n = n'$, the two integrals cancel and we get $E_0 + E_0' < E_0 + E_0'$, which is false. Hence $n \ne n'$. $\square$

**The universal functional (constrained search).** For every density $n$ that comes from some antisymmetric $N$-particle wave function define

$$
F[n] = \min_{\Psi \to n}\ \langle\Psi|\hat T + \hat W|\Psi\rangle ,
$$

the smallest kinetic-plus-interaction energy among all wave functions with the density $n$ (the arrow means "has the density"). $F$ is **universal**: it does not depend on $v$. (We ASSUME that the minimum is attained.) **The variational principle for the density** then reads

$$
E_0 = \min_n\Big(F[n] + \int v\,n\,dx\Big) .
$$

Proof: the variational principle over wave functions is $E_0 = \min_\Psi\langle\Psi|\hat T + \hat W + \hat V|\Psi\rangle$. Organise the minimisation in two steps, first over all $\Psi$ with a given density $n$, then over $n$. In the first step $\langle\Psi|\hat V|\Psi\rangle = \int v\,n\,dx$ is the same for all these $\Psi$, so the inner minimum is $F[n] + \int v\,n\,dx$; the outer minimum over $n$ is then the minimum over all $\Psi$, which is $E_0$. $\square$

These statements say that the energy is a functional of the density alone and that minimising it over densities gives the exact ground-state energy and density. They do not say what $F[n]$ is: finding good approximations to it is the work of DFT. On two sites the theorem can be seen at work: Notebook 13c (In [16], Figure 13c.7) shows that the exact density $n_L$ on the left site rises strictly with the site-energy difference $\Delta$, so each density belongs to exactly one $\Delta$.

### 13.9 Functionals and functional derivatives

A **functional** assigns a number to a whole function: $F[n]$ takes the function $n(x)$ and returns one number. Examples: $\int n\,dx$, $\int n^2\,dx$, the Hartree energy $E_H[n]$.

**Definition.** Change $n$ by a small amount $\epsilon\,\eta(x)$, where $\eta$ is any fixed function and $\epsilon$ a small number. If

$$
F[n + \epsilon\eta] = F[n] + \epsilon\int \frac{\delta F}{\delta n(x)}\,\eta(x)\,dx + O(\epsilon^2)
$$

for every $\eta$, the function $\delta F/\delta n(x)$ is the **functional derivative** of $F$ at $n$. On a grid with spacing $h$, $F$ is an ordinary function of the numbers $n_k$, and $\delta F/\delta n(x_k) = (\partial F/\partial n_k)/h$: the functional derivative is the gradient, divided by the length that belongs to one point.

**Examples, line by line.** (i) For $A[n] = \int n^2\,dx$: $A[n + \epsilon\eta] = \int (n^2 + 2\epsilon\,n\eta + \epsilon^2\eta^2)\,dx$ (multiply out the square), so the part of first order in $\epsilon$ is $\epsilon\int 2n\,\eta\,dx$ and $\delta A/\delta n = 2n$. (ii) For $G[n] = \int f(n(x))\,dx$ with a differentiable function $f$: Taylor's formula $f(n + \epsilon\eta) = f(n) + \epsilon f'(n)\,\eta + O(\epsilon^2)$ gives $\delta G/\delta n = f'(n)$. (iii) For $E_H = \tfrac12\int\!\int n(x)\,w(x, x')\,n(x')\,dx\,dx'$, the first-order change is $\tfrac{\epsilon}{2}\int\!\int[\eta(x)\,w\,n(x') + n(x)\,w\,\eta(x')]$; renaming $x \leftrightarrow x'$ in the second term and using $w(x, x') = w(x', x)$ makes the two terms equal, so $\delta E_H/\delta n(x) = \int w(x, x')\,n(x')\,dx' = v_H(x)$, the Hartree potential. (iv) $\delta\int v\,n\,dx/\delta n = v$. Notebook 13a (In [15]) tests the definition directly on a grid: it changes the density by $\pm\epsilon\eta$ and compares the difference quotient with $\int (\delta F/\delta n)\,\eta\,dx$.

**Minimising with a fixed particle number.** To minimise $E[n]$ over densities with $\int n\,dx = N$, take a Lagrange multiplier $\mu$ (Section 13.6) and require $\delta E/\delta n(x) = \mu$ at every point where $n > 0$. The multiplier is the **chemical potential**: $\mu = dE_0/dN$, the change of the lowest energy per added particle (where this derivative exists), by the meaning of a multiplier shown in Section 13.6.

### 13.10 The Kohn-Sham equations

The universal functional $F[n]$ contains the kinetic energy, the hardest part to write as an explicit formula of $n$ (Notebook 13a shows the crude attempt, the Thomas-Fermi approximation). Kohn and Sham (1965) avoided the problem: compute the kinetic energy **exactly**, but for a fictitious system of non-interacting particles that has the same density.

**The non-interacting reference system.** For non-interacting particles the constrained search defines

$$
T_s[n] = \min_{\Phi \to n}\ \langle\Phi|\hat T|\Phi\rangle ,
$$

the smallest kinetic energy of a non-interacting state with the density $n$; its minimiser is a single Slater determinant of orbitals $\phi_a$ with $n = \sum_a|\phi_a|^2$. The Kohn-Sham scheme ASSUMES that the density of interest is the ground-state density of some non-interacting system in some potential $v_s$ (**non-interacting $v$-representability**). This is an assumption, not a theorem; on two sites it holds (Notebook 13c, In [16], finds the potential exactly).

**Splitting the functional.** Write

$$
F[n] = T_s[n] + E_H[n] + E_{xc}[n] ,
$$

which **defines** the **exchange-correlation energy** $E_{xc} = F - T_s - E_H$. It collects everything the easy pieces miss: the exchange energy of Section 13.5, the correlation energy of Section 13.7, and the difference between the true kinetic energy and $T_s$. Nothing has been approximated yet.

**The equations.** Minimise $E[n] = T_s[n] + \int v\,n\,dx + E_H[n] + E_{xc}[n]$ by varying the orbitals of the determinant, with Lagrange multipliers $\epsilon_a$ for their normalisation. Since $n = \sum_a|\phi_a|^2$, a change of $\phi_a^*$ at the point $x$ changes $n$ at $x$ by $\phi_a(x)$ times that change; so every density functional $G[n]$ contributes $(\delta G/\delta n)\,\phi_a$ (chain rule), and the kinetic term contributes $-\tfrac12\,\phi_a''$. Setting the derivative to zero gives the **Kohn-Sham equations**

$$
\begin{aligned}
&\Big[-\frac12\,\frac{d^2}{dx^2} + v_s(x)\Big]\phi_a = \epsilon_a\,\phi_a, \qquad n(x) = \sum_{a\in O}|\phi_a(x)|^2 ,\\
&v_s = v + v_H + v_{xc}, \qquad v_{xc}(x) = \frac{\delta E_{xc}}{\delta n(x)} ,
\end{aligned}
$$

with the $N$ lowest orbitals occupied. The **Kohn-Sham potential** $v_s$ is local: a multiplication by a function, simpler than the Fock operator. If $E_{xc}$ were known exactly, these one-particle equations would give the exact ground-state density and energy of the interacting system.

**Total energy, line by line.** Multiply the equation of orbital $a$ by $\phi_a^*$, integrate and sum over the occupied orbitals:

$$
\sum_{a\in O}\epsilon_a = \sum_a\int\phi_a^*\Big(-\frac12\phi_a''\Big)dx + \int v_s\,n\,dx = T_s + \int v_s\,n\,dx .
$$

The first step uses normalisation, $\int|\phi_a|^2 = 1$, on the right and $\sum_a|\phi_a|^2 = n$ in the potential term; the second is the definition of $T_s$ for the minimising determinant. Solving for $T_s$ and inserting it into $E = T_s + \int v\,n + E_H + E_{xc}$, with $v_s = v + v_H + v_{xc}$ and $\int v_H\,n\,dx = 2E_H$:

$$
E_0 = \sum_{a\in O}\epsilon_a - E_H[n] + E_{xc}[n] - \int v_{xc}\,n\,dx ,
$$

the Kohn-Sham analogue of the double-counting formula of Section 13.6.

**Self-consistency.** $v_s$ depends on $n$, $n$ on the orbitals, and the orbitals on $v_s$. The equations are solved by the loop: (1) guess a density; (2) build $v_s$; (3) solve the one-particle equations and occupy the $N$ lowest orbitals; (4) form the new density; (5) if it equals the old one within a tolerance, stop; otherwise mix old and new (Section 13.21) and go back to (2).

**What the orbitals mean.** The Kohn-Sham orbitals and levels belong to the fictitious non-interacting system; only the density and the total energy are guaranteed to be physical. The levels are nevertheless useful: each is the derivative of the energy with respect to the occupation of its own orbital (Janak's theorem, Section 13.27).

**The exact Kohn-Sham potential on two sites.** Give the two sites the energies $\mp\Delta_s/2$ and put two non-interacting electrons into the lowest orbital of $\begin{pmatrix}-\Delta_s/2 & -t\\ -t & \Delta_s/2\end{pmatrix}$. Section 13.21 derives that the lowest eigenvector of $\begin{pmatrix} a & -t\\ -t & b\end{pmatrix}$ has $|c_L|^2 = \tfrac12\big(1 + (b - a)/\sqrt{(b - a)^2 + 4t^2}\big)$; here $b - a = \Delta_s$, so with $x = n_L - 1 = 2|c_L|^2 - 1$, line by line:

$$
\begin{aligned}
x &= \frac{\Delta_s}{\sqrt{\Delta_s^2 + 4t^2}} \\
x^2\,(\Delta_s^2 + 4t^2) &= \Delta_s^2 \\
\Delta_s^2\,(1 - x^2) &= 4t^2x^2 \\
\Delta_s &= \frac{2t\,x}{\sqrt{1 - x^2}} .
\end{aligned}
$$

The second line squares the first and multiplies by the denominator; the third collects the terms with $\Delta_s^2$; the fourth takes the square root, with the sign of $x$ (which is the sign of $\Delta_s$ by the first line). So for every exact density $n_L$ between 0 and 2 there is exactly one Kohn-Sham site-energy difference $\Delta_s$, and $\Delta_s - \Delta$ is the exact Hartree-exchange-correlation potential difference between the sites. Notebook 13c (In [16] to In [18], Figure 13c.8) computes it and splits it into a Hartree-exchange part and a correlation part.

### 13.11 Example: determinants, operators and the two-site model

Notebook 13c turns Sections 13.3 to 13.10 into numbers that can be checked: the three-point determinant of Section 13.3, the operator matrices and Wick's theorem of Section 13.4 (with the identity for ${:}S^2{:}$ that the Revision Kohn-Sham theory uses), the energy formula of Section 13.5, the exact and Hartree-Fock solutions of the two-site model of Section 13.7, and the Hohenberg-Kohn map and the exact Kohn-Sham potential of Sections 13.8 and 13.10. Everything in it is exact finite-dimensional mathematics: it is PROVED by the derivations above and checked by the notebook to rounding. It ends with the line ALL 33 CHECKS PASSED (notebook 13c) and draws eight figures.

<!-- NOTEBOOK 13c -->

### 13.14 Line-by-line walk-through of Notebook 13c

The notebook has nineteen code cells, In [1] to In [19]. This section explains every line of every one of them. Each code cell is preceded in the notebook by a text cell that says what it does; the numbers it prints are in Section 13.13.

**In [1], the set-up cell.** Apart from its comment lines and the notebook's name, it is the same in every notebook of the book; the notebooks 13b, 13d, 13e and 13a of this chapter have exactly this code with their own name, and their walk-throughs refer back to this paragraph. Its first part repeats the complete run instructions of Section 13.12 as **comment lines**: every line that starts with `#` is skipped by Python, and the lines are there so that the notebook file carries its own instructions. The code starts after the comment line THE SET-UP, which stands between two lines of `=` signs; the comment lines inside the code (which say, for example, why `REPO` is never printed) are left out below, because the text explains the same things.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell

NOTEBOOK_ID = "13c"  # this notebook: chapter 13, example c
```

`import` loads a **module** (a part of Python or of a package) so that the code can use it; the text after `#` on each line says what it is for. `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system. `import matplotlib.pyplot as plt` loads the drawing functions under the short name `plt`. The last line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"13c"`; the figure files are named after it.

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

(The docstring, the text in triple quotes under the `def` line that says what the function does, is left out here.) `def` defines a **function**, a named piece of code that runs when it is called. `Path.cwd()` is the folder in which the notebook runs and `.resolve()` writes it as a complete address. The list `[here, *here.parents]` holds this folder, its parent folder, the parent of that, and so on up to the top of the disk; the `for` loop takes them one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back; if none does, `raise` stops the notebook with an error message that says what to do.

```python
REPO = find_repository_root()
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))


def repository_file(relative):
    return REPO / relative


def output_file(relative):
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def say(text):
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`REPO` is the repository folder; it is never printed, because it differs from computer to computer while the printed output of a notebook must be the same everywhere. `os.environ.get(name, default)` reads an **environment variable** (a named text that a program receives from the computer) or returns the default; when you run the notebook the variable is not set, so `OUTPUT_ROOT` is the repository, and the book's checking tool sets it to a scratch folder so that a check never changes the repository. `repository_file` gives the full path of a repository file for reading (a Revision record); `output_file` gives the full path at which to write a file, after creating its folder (`mkdir` with `parents=True` makes missing parent folders too, and `exist_ok=True` makes it do nothing if the folder exists). `say` prints a text in lines of at most 89 characters (the width of a page of the book); continuation lines start with four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})

FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

`matplotlib.rcdefaults()` returns to the built-in plotting settings, so that the figures are the same on every computer, and `plt.rcParams.update` sets the figure size (7.0 by 4.2 inches), the letter size (10 points) and a faint grid. The braces `{...}` make a **dictionary**: pairs of a key and a value. A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/13c.captions.json"`. The last line writes an empty dictionary `{}` into the captions file; `newline="\n"` stores the same line end on every operating system.

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

`save_figure` (shown without its docstring and comment lines) numbers the figures 1, 2, 3, ... in the order in which they are saved (`setdefault` returns the number already stored for this name, or stores one more than the count so far), saves the figure as a PNG file with 150 dots per inch, cut to its content (`bbox_inches="tight"`) and without the program's name in the file (so that two runs write the same bytes), closes it, records its caption in the captions file (`json.dumps` turns the dictionary into JSON text), shows the saved picture below the cell, and prints where it was saved.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")


def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`PASSED` is an empty **list** (an ordered collection, in square brackets). `check` is the function behind every check: if the statement `condition` is false (`False`), `raise AssertionError(...)` stops the notebook with an error that names the check; if it is true, the name is appended to `PASSED` and the line PASS name is printed, followed by a line naming the Revision record and its check when the argument `record` is given. (Python's own `assert` statement is not used, because Python started with the option that optimises the code skips it.) `report` prints a key number as a line that starts with RESULT. `all_checks_passed` prints the last line of the notebook with the number of checks that passed. The last statement prints the one output line of In [1].

**In [2], the determinant on three points.**

```python
import itertools  # loops over all combinations of indices

import numpy as np  # arrays, matrices and linear algebra

phi0 = np.array([1.0, 0.0, 0.0])
phi1 = np.array([0.0, 1.0, 1.0]) / np.sqrt(2.0)
# Phi[r1, r2] = (phi0(r1) phi1(r2) - phi1(r1) phi0(r2)) / sqrt(2)
Phi = (np.outer(phi0, phi1) - np.outer(phi1, phi0)) / np.sqrt(2.0)
```

`itertools` is a module of Python that makes all combinations of indices; `numpy`, called `np`, holds arrays and matrices. `np.array([...])` makes an **array** (a list of numbers that supports arithmetic), so `phi0` and `phi1` are the two orbitals of Section 13.3; dividing an array by $\sqrt2$ divides every entry. `np.outer(u, w)` is the $3 \times 3$ table with the entries $u_{r_1} w_{r_2}$; so `Phi` is the table of $\Phi(r_1, r_2)$, row $r_1$ and column $r_2$, exactly the formula in the comment line.

```python
for r1 in range(3):
    say("Phi(%d, r2) for r2 = 0, 1, 2: %s" % (r1, np.array2string(
        Phi[r1], precision=6, floatmode="fixed", suppress_small=True)))
density_3 = 2.0 * np.sum(Phi ** 2, axis=1)  # n(r) = N sum_r2 |Phi(r, r2)|^2
```

The loop prints the three rows of the table. `"... %d ... %s" % (r1, text)` puts the number `r1` in place of `%d` and the text in place of `%s`; `np.array2string` writes a row with 6 digits after the point, showing $-0$ as $0$. `Phi ** 2` squares every entry, and `np.sum(..., axis=1)` adds along each row (over $r_2$); times $N = 2$ this is the density $n(r)$ of Section 13.3.

```python
check(abs(Phi[0, 1] - 0.5) < 1e-15 and abs(Phi[1, 2]) < 1e-15,
      "Phi(0,1) = 1/2 and Phi(1,2) = 0")
check(np.allclose(Phi, -Phi.T, atol=1e-15) and np.allclose(np.diag(Phi), 0.0),
      "Phi is antisymmetric and zero on the diagonal (Pauli)")
check(abs(np.sum(Phi ** 2) - 1.0) < 1e-15
      and np.allclose(density_3, [1.0, 0.5, 0.5], atol=1e-15)
      and np.allclose(density_3, phi0 ** 2 + phi1 ** 2, atol=1e-15),
      "Phi is normalised and its density is (1, 1/2, 1/2) = phi0^2 + phi1^2")
```

Three checks. `Phi[0, 1]` is the entry in row 0 and column 1, and `1e-15` means $10^{-15}$: the first check compares the two values worked out by hand in Section 13.3. `Phi.T` is the transposed table (rows and columns exchanged), so `Phi` equal to `-Phi.T` is antisymmetry; `np.allclose(a, b, atol=...)` is true when every entry of `a` differs from the entry of `b` by less than the given amount; `np.diag(Phi)` is the diagonal. The third check adds all nine squares (the normalisation) and compares the density with $(1, \tfrac12, \tfrac12)$ and with $\phi_0^2 + \phi_1^2$.

**In [3], two determinants as pictures.**

```python
x_box = np.linspace(0.0, 1.0, 101)
chi1 = np.sqrt(2.0) * np.sin(np.pi * x_box)
chi2 = np.sqrt(2.0) * np.sin(2.0 * np.pi * x_box)
Phi_box = (np.outer(chi1, chi2) - np.outer(chi2, chi1)) / np.sqrt(2.0)
```

`np.linspace(0.0, 1.0, 101)` is 101 equally spaced positions from 0 to 1. `chi1` and `chi2` are the two lowest orbitals of a particle in the box $0 < x < 1$ ($\sqrt2\sin(\pi x)$ and $\sqrt2\sin(2\pi x)$, normalised and orthogonal), and `Phi_box` their determinant on the $101 \times 101$ grid of positions of the two fermions.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
image = left.imshow(Phi, origin="lower", cmap="coolwarm", vmin=-0.6, vmax=0.6)
for r1, r2 in itertools.product(range(3), repeat=2):  # write every value in
    left.text(r2, r1, f"{Phi[r1, r2]:+.2f}", ha="center", va="center")
```

`plt.subplots(1, 2, ...)` makes a figure with two pairs of axes side by side, named `left` and `right`. `imshow` draws a table as a **heat map**: each entry is a coloured square, here red for positive and blue for negative (`cmap="coolwarm"`, the colour scale from $-0.6$ to $0.6$), with row 0 at the bottom (`origin="lower"`). `itertools.product(range(3), repeat=2)` gives all nine pairs $(r_1, r_2)$, and `left.text` writes each value, with its sign and two decimals (`:+.2f`), in the middle of its square.

```python
left.set_xticks([0, 1, 2])
left.set_yticks([0, 1, 2])
left.set_xlabel("position $r_2$ of fermion 2")
left.set_ylabel("position $r_1$ of fermion 1")
left.set_title("three points")
```

`set_xticks` and `set_yticks` put tick marks only at the three points 0, 1, 2; `set_xlabel`, `set_ylabel` and `set_title` write the axis labels and the title of the left panel. Text between two dollar signs is drawn by matplotlib as a formula, so the text r_2 between dollar signs in the label appears as $r_2$.

```python
image = right.imshow(Phi_box, origin="lower", extent=(0, 1, 0, 1),
                     cmap="coolwarm")
right.plot([0, 1], [0, 1], "k--", lw=0.8)
right.set_xlabel("position $r_2$ of fermion 2")
right.set_ylabel("position $r_1$ of fermion 1")
right.set_title("two fermions in a box")
fig.colorbar(image, ax=right, shrink=0.85)
save_figure(fig, "slater_determinants",
```

The right panel draws the $101 \times 101$ table `Phi_box` as a heat map; `extent=(0, 1, 0, 1)` stretches it over the square $0 \le r_1, r_2 \le 1$, so that the axes show positions instead of table indices, and without `vmin` and `vmax` the colour scale runs over the table's own range. The line with `right.plot([0, 1], [0, 1], ...)` draws the straight line from $(0, 0)$ to $(1, 1)$, the diagonal $r_1 = r_2$: in its style string the letter k means black and the two hyphens that follow it a dashed line, and `lw=0.8` is the line width in points. `fig.colorbar(image, ax=right, shrink=0.85)` adds the colour scale of the right panel, 85 per cent as tall as the panel. The call `save_figure(fig, "slater_determinants",` saves Figure 13c.1; the lines that follow it in the cell are the text of the caption, which the book prints under the figure. The last lines check that the box determinant is antisymmetric as well:

```python
check(np.allclose(Phi_box, -Phi_box.T, atol=1e-14), "the box determinant is "
      "antisymmetric")
```

(Python joins two strings written next to each other into one.)

**What Figure 13c.1 shows.** On the left, the nine values of the three-point determinant: $+0.50$ in row $r_1 = 0$ at $r_2 = 1, 2$, $-0.50$ in column $r_2 = 0$ at $r_1 = 1, 2$, and 0 everywhere else, in particular on the diagonal. Reflecting the table in its diagonal changes every sign: that is antisymmetry. On the right, the box determinant is positive (red, up to about $+2.2$) where fermion 1 is to the right of fermion 2 ($r_1 > r_2$, above the dashed diagonal), negative (blue) in the mirror-image region, and exactly zero along the diagonal: two fermions with the same label are never found at the same place.

**In [4], creation and annihilation operators as matrices.**

```python
M = 4  # orbitals
DIM = 2 ** M  # occupation-number states


def bit(state, p):
    """The occupation n_p (0 or 1) of orbital p in the state number state."""
    return (state >> p) & 1
```

In Python `**` means "to the power", so `DIM` is $2^4 = 16$. The function `bit` returns the occupation $n_p$ of orbital $p$ in the state with the number `state`: the operator written with two greater-than signs shifts the binary digits of the number `state` by `p` places to the right, and `& 1` keeps the last binary digit. For example, for the state 5 (binary 0101) and $p = 2$ the shift gives binary 01, whose last digit is 1: orbital 2 is occupied.

```python
a = []  # a[p] is the 16 x 16 matrix of the annihilation operator a_p
for p in range(M):
    matrix = np.zeros((DIM, DIM))
    for state in range(DIM):
        if bit(state, p) == 1:
            nu = sum(bit(state, q) for q in range(p))  # occupied before p
            matrix[state ^ (1 << p), state] = (-1) ** nu
    a.append(matrix)
a_dag = [matrix.T for matrix in a]  # creation operators: the transposes
```

For each orbital $p$ the cell starts from a $16 \times 16$ matrix of zeros and goes through the 16 states. Where orbital $p$ is occupied, it counts the occupied orbitals before $p$ ($\nu_p$ of Section 13.4). The row index is `state ^ (...)`, where the parentheses hold the number 1 shifted $p$ binary places to the left (the operator written with two less-than signs), which is $2^p$; the operator `^` is the "exclusive or" of the binary digits, so the row index is `state` with bit $p$ switched off: the number of the state after the removal. The entry in that row and in the column of the old state is $(-1)^{\nu_p}$: the matrix of $a_p$ maps the old state to the new one with the sign of Section 13.4. `a.append` adds the matrix to the list. The creation operators are the transposes (`.T`), because the matrices are real.

```python
identity = np.eye(DIM)
worst = 0.0
for p, q in itertools.product(range(M), repeat=2):
    worst = max(worst,
                np.abs(a[p] @ a_dag[q] + a_dag[q] @ a[p] - (p == q) * identity).max(),
                np.abs(a[p] @ a[q] + a[q] @ a[p]).max(),
                np.abs(a_dag[p] @ a_dag[q] + a_dag[q] @ a_dag[p]).max())
check(worst == 0.0, "{a_p, a_q^dag} = delta_pq and {a_p, a_q} = 0 exactly")
```

`np.eye(DIM)` is the $16 \times 16$ unit matrix and `@` is the matrix product. For all 16 pairs $(p, q)$ the loop computes the three anticommutators of Section 13.4 minus their required values (`(p == q)` is 1 when $p = q$ and 0 otherwise) and keeps the largest entry of any of them in `worst`. The check requires it to be exactly 0: the matrices hold only $0$ and $\pm1$, so there is no rounding at all.

```python
number = sum(a_dag[p] @ a[p] for p in range(M))  # the particle-number operator
check(np.array_equal(np.diag(number), [bin(s).count("1") for s in range(DIM)]),
      "the number operator counts the occupied orbitals of every state")
```

`number` is $\hat N = \sum_p a_p^\dagger a_p$. Its diagonal must hold, for every state $s$, the number of ones in the binary form of $s$ (`bin(s)` writes $s$ in binary, `.count("1")` counts its ones).

**In [5], the operator matrices as heat maps.**

```python
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.2))
for ax, p in zip(axes, (1, 3)):
    image = ax.imshow(a_dag[p], cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_title(f"creation operator $a_{p}^\\dagger$")
    ax.set_xlabel("state number before (column)")
    ax.set_ylabel("state number after (row)")
fig.colorbar(image, ax=axes, shrink=0.8)
save_figure(fig, "operator_matrices",
```

`plt.subplots(1, 2, ...)` makes two panels, kept together in `axes`. `zip(axes, (1, 3))` pairs the first panel with orbital 1 and the second with orbital 3, and the loop draws `a_dag[p]`, the $16 \times 16$ matrix of $a_p^\dagger$, as a heat map with the colour scale fixed from $-1$ (blue) through 0 (grey) to $+1$ (red). Without `origin="lower"`, `imshow` puts row 0 at the top, as a matrix is printed. In the title the f-string puts the value of `p` in place of `{p}`, and the doubled backslash is one backslash in the text, so matplotlib draws $a_1^\dagger$ and $a_3^\dagger$. The axis labels say that a column is the state before the operator acts and a row the state after it. `fig.colorbar(image, ax=axes, shrink=0.8)` draws one colour scale for both panels. `save_figure` saves Figure 13c.2 (the lines after it are the caption).

**What Figure 13c.2 shows.** Every column holds at most one coloured square, so each operator sends a state to exactly one other state or to zero. In the left panel ($a_1^\dagger$) the squares sit in the columns 0, 1, 4, 5, 8, 9, 12, 13, the states in which orbital 1 is empty, and in the rows two higher (bit 1 switched on, which adds $2^1 = 2$ to the state number); the columns 0, 4, 8, 12 (orbital 0 empty) carry $+1$ and the columns 1, 5, 9, 13 (orbital 0 occupied) carry $-1$, the sign $(-1)^{\nu_1}$. In the right panel ($a_3^\dagger$) the columns 0 to 7 go to the rows 8 to 15, with the sign $+1$ or $-1$ according to whether an even or an odd number of the orbitals 0, 1, 2 is occupied. The columns 8 to 15 are empty: there orbital 3 is already occupied, and the Pauli principle gives zero.

**In [6], Wick's theorem for a determinant.**

```python
rng = np.random.default_rng(12345)  # fixed seed: the same numbers every run
U_mix = np.linalg.qr(rng.normal(size=(M, M)) + 1j * rng.normal(size=(M, M)))[0]
a_dag_new = [sum(U_mix[k, p] * a_dag[k] for k in range(M)) for p in range(M)]
```

`np.random.default_rng(12345)` makes a generator of random numbers with a fixed starting value (**seed**), so every run draws the same numbers. `rng.normal(size=(M, M))` is a $4 \times 4$ table of random numbers, `1j` is the imaginary unit $i$, so the argument is a random complex matrix; `np.linalg.qr(...)[0]` is the first factor of its **QR factorisation**, a unitary matrix $U$ (its columns are orthonormal). `a_dag_new[p]` is $a_p'^\dagger = \sum_k U_{kp}\,a_k^\dagger$, the creation operator of the new orbital $p$ (Section 13.4).

```python
vacuum = np.zeros(DIM)
vacuum[0] = 1.0  # state number 0: no fermion at all
Phi_state = a_dag_new[0] @ a_dag_new[1] @ vacuum
rho_det = sum(np.outer(U_mix[:, k], U_mix[:, k].conj()) for k in (0, 1))
```

The vacuum is the column with 1 in place 0 (the state number 0 has no fermion). `Phi_state` is $a_0'^\dagger a_1'^\dagger|0\rangle$, the determinant of the new orbitals 0 and 1, and `rho_det` is its density matrix $\rho = \sum_{a = 0, 1} U_{:,a}U_{:,a}^\dagger$ (`U_mix[:, k]` is column $k$, `.conj()` the complex conjugate, and `np.outer` the column times the conjugated row).

```python
def wick_errors(expect, rho):
    """Largest errors of <a+_p a_q> = rho_qp and of the four-operator formula."""
    two = max(abs(expect(a_dag[p] @ a[q]) - rho[q, p])
              for p, q in itertools.product(range(M), repeat=2))
    four = max(abs(expect(a_dag[p] @ a_dag[q] @ a[s] @ a[r])
                   - (rho[r, p] * rho[s, q] - rho[s, p] * rho[r, q]))
               for p, q, r, s in itertools.product(range(M), repeat=4))
    return two, four


def in_determinant(operator):
    """<Phi| operator |Phi> for the determinant Phi_state."""
    return np.vdot(Phi_state, operator @ Phi_state)
```

`wick_errors` takes a rule `expect` that turns an operator into its expectation value, and a density matrix `rho`; it returns the largest error of the two-operator formula over the 16 pairs $(p, q)$ and of the four-operator formula over the $4^4 = 256$ combinations $(p, q, r, s)$, both written exactly as in Section 13.4. `in_determinant` is such a rule for the determinant: `np.vdot(u, w)` is $\sum_k u_k^* w_k$, the inner product.

```python
check(abs(np.vdot(Phi_state, Phi_state) - 1.0) < 1e-14, "the determinant is "
      "normalised")
two, four = wick_errors(in_determinant, rho_det)  # the largest errors (rounding)
check(two < 1e-14 and four < 1e-14,
      "Wick's theorem holds for the determinant (all 16 + 256 values, to 1e-14)")
check(np.allclose(rho_det @ rho_det, rho_det, atol=1e-14)
      and abs(np.trace(rho_det).real - 2.0) < 1e-14,
      "the density matrix of a determinant obeys rho^2 = rho, Tr rho = 2")
```

Three checks: the determinant has norm 1; all 272 Wick values agree to $10^{-14}$ (only rounding remains); and $\rho^2 = \rho$ with trace 2 (`np.trace` is the sum of the diagonal, `.real` its real part).

**In [7], Wick's theorem for a thermal ensemble.**

```python
energies = np.array([-1.0, -0.3, 0.4, 1.2])  # orbital energies (units of t)
MU, TEMPERATURE = 0.0, 0.5
H0 = sum(energies[p] * a_dag_new[p] @ a_dag_new[p].conj().T for p in range(M))
K = H0 - MU * number  # H0 - mu N, a Hermitian 16 x 16 matrix
```

Four orbital energies, the chemical potential $\mu = 0$ and the temperature $T = 0.5$. `a_dag_new[p].conj().T` is the conjugate transpose of $a_p'^\dagger$, which is $a'_p$; so `H0` is $\hat H_0 = \sum_p\epsilon_p\,a_p'^\dagger a'_p$, non-interacting fermions in the mixed orbitals, and `K` is $\hat H_0 - \mu\hat N$.

```python
k_values, k_vectors = np.linalg.eigh(K)
weights = np.exp(-(k_values - k_values.min()) / TEMPERATURE)  # shifted: no overflow
gibbs = (k_vectors * (weights / weights.sum())) @ k_vectors.conj().T
f = 1.0 / (np.exp((energies - MU) / TEMPERATURE) + 1.0)  # Fermi-Dirac
rho_thermal = sum(f[p] * np.outer(U_mix[:, p], U_mix[:, p].conj()) for p in range(M))
```

`np.linalg.eigh` returns the eigenvalues and the orthonormal eigenvectors (as columns) of the Hermitian matrix `K`. The Gibbs weights $e^{-k_i/T}$ are computed after subtracting the smallest eigenvalue, which multiplies every weight by the same number and so cancels after dividing by their sum, but keeps the exponentials from becoming too large for the computer. `k_vectors * (weights / weights.sum())` multiplies each eigenvector column by its normalised weight, and the product with the conjugate transpose gives the density operator $e^{-(\hat H_0 - \mu\hat N)/T}/Z = \sum_i p_i\,u_i u_i^\dagger$ (a function of a matrix defined through its eigenvalues, Section 13.26). `f` are the Fermi-Dirac occupations $1/(e^{(\epsilon_p - \mu)/T} + 1)$ and `rho_thermal` the density matrix $\sum_p f_p\,U_{:,p}U_{:,p}^\dagger$.

```python
two, four = wick_errors(lambda operator: np.trace(gibbs @ operator), rho_thermal)
check(two < 1e-13 and four < 1e-13,
      "Wick's theorem holds for the thermal ensemble of non-interacting fermions "
      "(to 1e-13)")
```

`lambda operator: ...` is a function without a name; here it is the rule "expectation value in the ensemble", $\mathrm{Tr}(\hat\rho\,A)$. The check requires all 272 Wick values to agree to $10^{-13}$.

**In [8], the normal-ordered square of a vertex.**

```python
raw = rng.normal(size=(M, M)) + 1j * rng.normal(size=(M, M))
V = (raw + raw.conj().T) / 2.0  # a random Hermitian vertex
S_square = sum(V[p, q] * V[r, s] * a_dag[p] @ a_dag[r] @ a[s] @ a[q]
               for p, q, r, s in itertools.product(range(M), repeat=4))
```

A random complex matrix plus its conjugate transpose, halved, is Hermitian: that is the vertex $V$. `S_square` is the $16 \times 16$ matrix of ${:}S^2{:} = \sum V_{pq}V_{rs}\,a_p^\dagger a_r^\dagger a_s a_q$, summed over all 256 index combinations.

```python
for label, expect, rho in (("determinant", in_determinant, rho_det),
                           ("thermal", lambda o: np.trace(gibbs @ o), rho_thermal)):
    lhs = expect(S_square)
    rhs = np.trace(V @ rho) ** 2 - np.trace(V @ rho @ V @ rho)
    say(f"{label}: <:S^2:> = {lhs.real:.10f}, Hartree - exchange = {rhs.real:.10f}")
    check(abs(lhs - rhs) < 1e-12,
          f"<:S^2:> = (Tr V rho)^2 - Tr(V rho V rho) in the {label} state",
          record="Revision/kohn_sham/reports/ks-theory-python.json, check "
                 "hf_wick_contraction")
```

For the determinant and for the thermal ensemble, `lhs` is the expectation value of ${:}S^2{:}$ computed from the matrices and `rhs` the formula $(\mathrm{Tr}\,V\rho)^2 - \mathrm{Tr}(V\rho V\rho)$ of Section 13.4. The printed values agree to all ten printed decimals, $-1.0717850309$ and $-1.9027816067$, and each check names the Revision check hf_wick_contraction whose identity it reproduces.

**In [9], the density matrices.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
image = left.imshow(np.abs(rho_det), cmap="viridis", vmin=0.0)
left.set_title("$|\\rho_{qp}|$ of the determinant")
left.set_xticks(range(M))
left.set_yticks(range(M))
left.set_xlabel("$p$")
left.set_ylabel("$q$")
fig.colorbar(image, ax=left, shrink=0.85)
```

The left panel is a heat map of `np.abs(rho_det)`, the sizes $|\rho_{qp}|$ of the 16 complex entries of the determinant's density matrix, on the colour scale viridis (dark blue for small, yellow for large values) starting at 0 (`vmin=0.0`); the column is $p$ and the row is $q$. The tick marks are put at the four orbital numbers (`range(M)` is $0, 1, 2, 3$), and the colour scale is added beside the panel.

```python
occupations_det = np.sort(np.linalg.eigvalsh(rho_det))[::-1]
occupations_th = np.sort(np.linalg.eigvalsh(rho_thermal))[::-1]
positions = np.arange(M)
right.bar(positions - 0.2, occupations_det, width=0.4, label="determinant")
right.bar(positions + 0.2, occupations_th, width=0.4, label="thermal, $T = 0.5$")
right.set_xticks(positions)
right.set_xlabel("eigenvalue number")
right.set_ylabel("occupation (eigenvalue of $\\rho$)")
right.legend()
save_figure(fig, "density_matrices",
```

`np.linalg.eigvalsh` computes the eigenvalues of a Hermitian matrix (real numbers, in increasing order); `np.sort(...)[::-1]` sorts them and reverses the order (the slice `[::-1]` steps backwards through an array), so the largest comes first. `positions` is $0, 1, 2, 3$. `right.bar(x, heights, width=0.4, ...)` draws a bar of the given height at each position $x$; shifting the two sets of bars by $\mp0.2$ puts them side by side. The `label` of each set appears in the legend (`right.legend()`). `save_figure` saves Figure 13c.3, and the check

```python
check(np.allclose(occupations_det, [1, 1, 0, 0], atol=1e-14)
      and np.allclose(occupations_th, np.sort(f)[::-1], atol=1e-14),
      "the occupations are 1, 1, 0, 0 and the Fermi-Dirac numbers")
```

requires the eigenvalues to be exactly $1, 1, 0, 0$ for the determinant and the Fermi-Dirac numbers $f_p$ for the ensemble.

**What Figure 13c.3 shows.** On the left, all 16 entries of the determinant's density matrix are nonzero (between about 0.05 and 0.85): in the randomly mixed basis the two occupied orbitals are spread over all four basis orbitals, so $\rho$ does not look like a projector. Its eigenvalues on the right are nevertheless exactly 1, 1, 0, 0 (blue bars): the determinant occupies two orbitals completely and the others not at all. The thermal ensemble (orange bars) has the four Fermi-Dirac numbers, about 0.88, 0.65, 0.31 and 0.08 for the levels $-1$, $-0.3$, $0.4$, $1.2$ at $T = 0.5$: every level is partly occupied, the lower ones more.

**In [10], the energy of a determinant.**

```python
chi = np.linalg.qr(rng.normal(size=(6, M)))[0]  # four orthonormal orbitals on 6 points
W_raw = rng.normal(size=(6, 6))
W_pair = (W_raw + W_raw.T) / 2.0  # a symmetric interaction W(x, x')
h_raw = rng.normal(size=(M, M))
h_one = (h_raw + h_raw.T) / 2.0  # a symmetric one-body matrix
# w[p,q,r,s] = sum_{x,x'} chi_p(x) chi_q(x') W(x,x') chi_r(x) chi_s(x')
w = np.einsum("xp,yq,xy,xr,ys->pqrs", chi, chi, W_pair, chi, chi)
```

The QR factorisation of a random $6 \times 4$ table gives four orthonormal real orbitals on six points. A random table plus its transpose, halved, is symmetric: a pair interaction $W(x, x')$ with the symmetry of a real interaction, and a one-body matrix $h_{pq}$. `np.einsum` computes a sum of products written as a pattern: here, for every $(p, q, r, s)$, the sum over the points $x$ and $y$ of $\chi_p(x)\chi_q(y)W(x, y)\chi_r(x)\chi_s(y)$, which is the two-body integral $w_{pqrs}$ of Section 13.4 on the six points.

```python
H_many = sum(h_one[p, q] * a_dag[p] @ a[q] for p, q in itertools.product(range(M),
                                                                         repeat=2))
H_many = H_many + 0.5 * sum(w[p, q, r, s] * a_dag[p] @ a_dag[q] @ a[s] @ a[r]
                            for p, q, r, s in itertools.product(range(M), repeat=4))
basis_det = a_dag[0] @ a_dag[1] @ vacuum  # occupies the basis orbitals 0 and 1
direct = basis_det @ H_many @ basis_det
formula = sum(h_one[k, k] for k in (0, 1)) + 0.5 * sum(
    w[k, l, k, l] - w[k, l, l, k] for k in (0, 1) for l in (0, 1))
```

`H_many` is the $16 \times 16$ matrix of $\hat H = \sum h_{pq}a_p^\dagger a_q + \tfrac12\sum w_{pqrs}a_p^\dagger a_q^\dagger a_s a_r$, built in two statements (the one-body part, then the two-body part added to it). `basis_det` is the column of the state $a_0^\dagger a_1^\dagger|0\rangle$; since all matrices here are real, `basis_det @ H_many @ basis_det` (row times matrix times column) is the expectation value `direct` of $\hat H$ in this determinant of the basis orbitals 0 and 1. `formula` is $\sum_a h_{aa} + \tfrac12\sum_{a,b}(w_{abab} - w_{abba})$ of Section 13.5, with the sums over $a, b \in \{0, 1\}$ written as generator expressions.

```python
say(f"<Phi|H|Phi> = {direct:.10f};  sum h_aa + (1/2) sum (w_abab - w_abba) = "
    f"{formula:.10f}")
check(abs(direct - formula) < 1e-12,
      "the energy of a determinant is one-body + direct - exchange")
```

The cell prints both numbers with ten decimals, $-1.5322375649$ and $-1.5322375649$, and checks that they agree to $10^{-12}$.

**In [11], the exact two-site model.**

```python
n_op = [a_dag[p] @ a[p] for p in range(M)]  # occupation operators
DOUBLE = n_op[0] @ n_op[2] + n_op[1] @ n_op[3]  # both electrons on one site
# The states with exactly one up (orbital 0 or 1) and one down (2 or 3) electron:
SECTOR = [s for s in range(DIM) if bit(s, 0) + bit(s, 1) == 1
          and bit(s, 2) + bit(s, 3) == 1]
```

With the orbitals numbered L up (0), R up (1), L down (2), R down (3), `DOUBLE` is $\hat n_{L\uparrow}\hat n_{L\downarrow} + \hat n_{R\uparrow}\hat n_{R\downarrow}$. The **list comprehension** `[s for s in range(DIM) if ...]` collects the state numbers with exactly one up and one down electron; it prints as $[5, 6, 9, 10]$: in binary 0101 (L up and L down: both on L), 0110 (R up, L down), 1001 (L up, R down) and 1010 (both on R).

```python
def two_site(t, U, delta=0.0):
    """Ground-state energy, double occupancy and n_L of the two-site model."""
    H = -t * (a_dag[0] @ a[1] + a_dag[1] @ a[0] + a_dag[2] @ a[3] + a_dag[3] @ a[2])
    H = H + U * DOUBLE - 0.5 * delta * (n_op[0] + n_op[2]) \
        + 0.5 * delta * (n_op[1] + n_op[3])
    block = H[np.ix_(SECTOR, SECTOR)]  # the 4 x 4 block of the sector
    values, vectors = np.linalg.eigh(block)
    ground = vectors[:, 0]
    occupancy = ground @ DOUBLE[np.ix_(SECTOR, SECTOR)] @ ground
    n_left = ground @ (n_op[0] + n_op[2])[np.ix_(SECTOR, SECTOR)] @ ground
    return values[0], occupancy, n_left
```

The function builds the Hamiltonian of Section 13.7 term by term (the backslash at the end of a line continues the statement on the next line): hopping of each label between L and R, the repulsion $U$ on doubly occupied sites, and the site energies $-\Delta/2$ on L and $+\Delta/2$ on R. `np.ix_(SECTOR, SECTOR)` selects the rows and columns of the four states of the sector, so `block` is a $4 \times 4$ matrix. Its lowest eigenvalue `values[0]` is the ground-state energy and the first column of `vectors` the ground state; the expectation values of `DOUBLE` and of $\hat n_L$ in it are the double occupancy and the density on L. The function returns the three numbers.

```python
say(f"the sector holds the states {SECTOR}")
for U in (2.0, 4.0):
    E0, occupancy, n_left = two_site(1.0, U)
    report(f"U = {U:.0f}: exact E_0", f"{E0:.6f}")
    report(f"U = {U:.0f}: exact double occupancy", f"{occupancy:.6f}")
    check(abs(E0 - 0.5 * (U - np.sqrt(U ** 2 + 16.0))) < 1e-12
          and abs(n_left - 1.0) < 1e-12,
          f"U = {U:.0f}: E_0 = (U - sqrt(U^2 + 16 t^2))/2 and n_L = 1")
```

For $t = 1$ and $U = 2$ and $4$ the cell prints the exact energy and double occupancy and checks the closed form $E_0 = \tfrac12(U - \sqrt{U^2 + 16t^2})$ of Section 13.7 and the symmetric density $n_L = 1$. The results are $E_0 = -1.236068$ with double occupancy $0.276393$ at $U = 2$, and $-0.828427$ with $0.146447$ at $U = 4$.

**In [12], Hartree-Fock, restricted and unrestricted.**

```python
def hf_energy(alpha, beta, U, t=1.0):
    """E(alpha, beta) of the determinant with up (cos a, sin a), down (cos b, sin b)."""
    return (-t * (np.sin(2 * alpha) + np.sin(2 * beta))
            + 0.5 * U * (1.0 + np.cos(2 * alpha) * np.cos(2 * beta)))
```

The formula $E(\alpha, \beta) = -t(\sin2\alpha + \sin2\beta) + \tfrac{U}{2}(1 + \cos2\alpha\cos2\beta)$ of Section 13.7.

```python
H_test = -(a_dag[0] @ a[1] + a_dag[1] @ a[0] + a_dag[2] @ a[3] + a_dag[3] @ a[2]) \
    + 3.0 * DOUBLE  # t = 1, U = 3
worst = 0.0
for alpha, beta in ((0.3, 1.1), (0.7, 0.2), (np.pi / 4, np.pi / 4)):
    det = (np.cos(alpha) * a_dag[0] + np.sin(alpha) * a_dag[1]) @ (
        np.cos(beta) * a_dag[2] + np.sin(beta) * a_dag[3]) @ vacuum
    worst = max(worst, abs(det @ H_test @ det - hf_energy(alpha, beta, 3.0)))
check(worst < 1e-12, "the Hartree-Fock energy formula equals <Phi|H|Phi>")
```

For $t = 1$, $U = 3$ and three pairs of angles the cell builds the determinant $(\cos\alpha\,a_{L\uparrow}^\dagger + \sin\alpha\,a_{R\uparrow}^\dagger)(\cos\beta\,a_{L\downarrow}^\dagger + \sin\beta\,a_{R\downarrow}^\dagger)|0\rangle$ from the operator matrices and checks that its energy equals the formula.

```python
angles = np.linspace(0.0, np.pi / 2, 1001)
A, B = np.meshgrid(angles, angles, indexing="ij")
U_values = np.linspace(0.0, 8.0, 33)
E_exact = np.array([two_site(1.0, U)[0] for U in U_values])
D_exact = np.array([two_site(1.0, U)[1] for U in U_values])
E_rhf = -2.0 + 0.5 * U_values  # restricted: alpha = beta = pi/4
E_uhf = np.array([hf_energy(A, B, U).min() for U in U_values])  # grid minimum
```

1001 angles from 0 to $\pi/2$; `np.meshgrid` makes the two $1001 \times 1001$ tables `A` and `B` of all pairs $(\alpha, \beta)$. For 33 repulsions $U = 0, 0.25, \dots, 8$ the cell computes the exact energy and double occupancy, the restricted energy $-2t + U/2$, and the smallest value of $E(\alpha, \beta)$ over the whole grid of angles (`.min()`).

```python
U_safe = np.where(U_values > 2.0, U_values, 1.0)  # avoids dividing by U = 0
E_closed = np.where(U_values <= 2.0, -2.0 + 0.5 * U_values, -2.0 / U_safe)
check(np.max(np.abs(E_uhf - E_closed)) < 1e-5,
      "the minimum over all determinants is -2t + U/2 (U <= 2t) and -2t^2/U")
check(np.all(E_exact <= E_uhf + 1e-12) and np.all(E_uhf <= E_rhf + 1e-12),
      "variational order: exact <= unrestricted HF <= restricted HF")
```

`np.where(condition, a, b)` takes `a` where the condition holds and `b` elsewhere. `E_closed` is the closed form of Section 13.7, $-2t + U/2$ for $U \le 2t$ and $-2t^2/U$ beyond; `U_safe` replaces the values $U \le 2$ (where the second formula is not used) by 1, so that no division by zero occurs. The first check compares the grid minimum with the closed form (the grid of angles allows an error below $10^{-5}$); the second checks the variational order exact $\le$ unrestricted $\le$ restricted at every $U$ (`np.all` is true when every entry is true).

```python
E_c = E_exact - E_closed  # correlation energy
report("U = 2: correlation energy E_0 - E_HF", f"{E_c[8]:.6f}")
fine_U = np.linspace(2.0, 8.0, 60001)  # closed forms on a fine grid of U > 2t
fine_c = 0.5 * (fine_U - np.sqrt(fine_U ** 2 + 16.0)) + 2.0 / fine_U
report("U of the largest correlation energy (in size)",
       f"{fine_U[np.argmin(fine_c)]:.3f}")
```

The correlation energy at the entry 8, $U = 8 \cdot 0.25 = 2$, is $-0.236068$. On a fine grid of $U$ beyond $2t$ the cell evaluates $E_0 - E_{HF} = \tfrac12(U - \sqrt{U^2 + 16}) + 2/U$, and `np.argmin` finds the place of its most negative value: the correlation energy is largest in size at $U = 3.335\,t$.

**In [13], the energies.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(U_values, E_rhf, "--", label="restricted HF $-2t + U/2$")
left.plot(U_values, E_closed, "-.", label="unrestricted HF")
left.plot(U_values, E_exact, color="black", lw=2.0, label="exact $E_0$")
left.axvline(2.0, color="gray", lw=0.8)
left.set_xlabel("repulsion $U/t$")
left.set_ylabel("ground-state energy ($t$)")
left.legend(fontsize=8)
```

`left.plot(x, y, style, label=...)` draws the points $(x, y)$ joined by a line: the restricted energy $-2t + U/2$ dashed (the style string of two hyphens), the best determinant's energy in closed form dash-dotted (`"-."`), and the exact energy as a thick black line (`lw=2.0`). `axvline(2.0, ...)` draws a thin grey vertical line at $U = 2t$, where restricted and unrestricted Hartree-Fock separate. The axis labels give the units: $U$ is divided by $t$, and the energies are in units of $t$. `legend(fontsize=8)` lists the three labels in small letters.

```python
right.plot(U_values, E_c, "o-", ms=3, color="black")
right.set_xlabel("repulsion $U/t$")
right.set_ylabel("correlation energy $E_0 - E_{HF}$ ($t$)")
fig.subplots_adjust(wspace=0.32)  # room between the panels for the axis label
fig.suptitle("Two electrons on two sites: exact versus Hartree-Fock")
save_figure(fig, "two_site_energies",
```

The right panel draws the correlation energy at the 33 values of $U$ as dots joined by a line (`"o-"`; `ms=3` is the size of the dots in points). `fig.subplots_adjust(wspace=0.32)` widens the gap between the panels so that the label of the right vertical axis does not touch the left panel, and `fig.suptitle` writes one title above both panels. `save_figure` saves Figure 13c.4. Its caption is not a fixed text: one of its lines is an f-string with the expression `fine_U[np.argmin(fine_c)]:.1f` in braces, which writes the computed place of the largest correlation energy, rounded to one decimal (3.3), into the caption.

**What Figure 13c.4 shows.** On the left, all three energies start at $-2t$ for $U = 0$ (both electrons in the bonding orbital, no repulsion). The restricted energy rises along the straight line $-2t + U/2$; the best determinant follows it up to $U = 2t$ and then bends away towards 0 as $-2t^2/U$; the exact energy lies below both at every $U > 0$ and also approaches 0 for large $U$. On the right, the correlation energy is zero at $U = 0$, falls to its most negative value, about $-0.337\,t$, near $U = 3.3t$, and then rises slowly towards zero: at large $U$ the electrons sit on different sites anyway, and the unrestricted determinant describes that well.

**In [14], the double occupancy.**

```python
D_uhf = np.where(U_values <= 2.0, 0.5, 2.0 / U_safe ** 2)
```

The unrestricted double occupancy is $\tfrac12(1 + c_\alpha c_\beta)$ with $c_\beta = -c_\alpha$ and $s_\alpha = 2t/U$, that is $\tfrac12(1 - c_\alpha^2) = \tfrac12 s_\alpha^2 = 2t^2/U^2$ for $U > 2t$, and $\tfrac12$ below (the formula $E(\alpha, \beta)$ of Section 13.7 is $U$ times this number plus the hopping energy).

```python
fig, ax = plt.subplots()
ax.plot(U_values, 0.5 * np.ones_like(U_values), "--", label="restricted HF: 1/2")
ax.plot(U_values, D_uhf, "-.", label="unrestricted HF: $2t^2/U^2$ for $U > 2t$")
ax.plot(U_values, D_exact, color="black", lw=2.0, label="exact")
ax.set_xlabel("repulsion $U/t$")
ax.set_ylabel("double occupancy")
ax.set_title("How often both electrons sit on the same site")
ax.legend()
save_figure(fig, "double_occupancy",
```

One panel with three curves against $U/t$: the restricted value $\tfrac12$ (`np.ones_like(U_values)` is an array of ones as long as `U_values`, so `0.5 * np.ones_like(U_values)` is the constant $\tfrac12$ at every $U$) dashed, the unrestricted value dash-dotted, and the exact double occupancy as a thick black line; then the axis labels, the title, the legend, and `save_figure` for Figure 13c.5. The cell then checks

```python
check(abs(D_exact[8] - 0.276393) < 1e-6 and abs(D_exact[16] - 0.146447) < 1e-6,
      "exact double occupancy 0.276393 at U = 2t and 0.146447 at U = 4t")
check(np.all(np.diff(D_exact) < 0), "the exact double occupancy falls as U grows")
```

the two worked values (entries 8 and 16 are $U = 2$ and $U = 4$) and that the exact double occupancy falls at every step of $U$ (`np.diff` gives the differences of neighbouring entries).

**What Figure 13c.5 shows.** All three curves start at $\tfrac12$ for $U = 0$. The exact double occupancy falls smoothly from the start: the exact electrons begin to avoid each other at any repulsion, while each label stays shared equally between the sites. The restricted determinant stays at $\tfrac12$ for every $U$. The unrestricted one stays at $\tfrac12$ up to $U = 2t$, then drops steeply as $2t^2/U^2$, crosses the exact curve near $U = 3.3t$ and lies below it beyond: by breaking the left-right symmetry it overshoots.

**In [15], the Hartree-Fock energy landscape.**

```python
E_map = hf_energy(A, B, 4.0)
index = np.unravel_index(np.argmin(E_map), E_map.shape)
```

`E_map` is $E(\alpha, \beta)$ at $U = 4t$ on the whole grid of angles; `np.argmin` finds the position of its smallest value in the table read as one long list, and `np.unravel_index` turns that position back into a row and a column, the pair `index`.

```python
fig, ax = plt.subplots(figsize=(6.0, 5.0))
contours = ax.contourf(A, B, E_map, levels=30, cmap="viridis")
fig.colorbar(contours, ax=ax, label="$E(\\alpha, \\beta)$ ($t$)")
ax.plot([np.pi / 4], [np.pi / 4], "wx", ms=10, label="restricted (saddle)")
ax.plot([angles[index[0]], angles[index[1]]], [angles[index[1]], angles[index[0]]],
        "r*", ms=12, label="unrestricted minima")
```

`ax.contourf(A, B, E_map, levels=30, ...)` colours the plane of the angles $(\alpha, \beta)$ in 30 bands of equal energy (a **contour map**: each band joins the points with nearly the same value), and the colour scale is labelled with the energy and its unit $t$. The style `"wx"` draws a white cross (w white, x cross) at the restricted point $(\pi/4, \pi/4)$, and `"r*"` red stars at the grid minimum $(\alpha, \beta)$ = `(angles[index[0]], angles[index[1]])` and at its mirror image with the two angles exchanged (the two lists hold the horizontal and the vertical coordinates of both points); `ms` sets the marker sizes.

```python
ax.set_xlabel("$\\alpha$ (up orbital)")
ax.set_ylabel("$\\beta$ (down orbital)")
ax.set_title("Hartree-Fock energy landscape at $U = 4t$")
ax.legend(loc="upper right", fontsize=8)
save_figure(fig, "hf_landscape",
```

Axis labels, title, the legend in the upper right corner, and `save_figure` for Figure 13c.6. Then

```python
check(abs(E_map.min() + 0.5) < 1e-5 and abs(hf_energy(np.pi / 4, np.pi / 4, 4.0)
                                             - 0.0) < 1e-12,
      "at U = 4t: minimum -0.5 t, restricted value 0")
```

requires the smallest value on the grid to be $-2t^2/U = -0.5$ (to $10^{-5}$, the accuracy of the grid of angles) and the restricted value to be $-2 + 4/2 = 0$.

**What Figure 13c.6 shows.** The landscape is lowest (dark) in two basins, around $(\alpha, \beta) \approx (0.26, 1.31)$ and its mirror image $(1.31, 0.26)$, where the energy is $-0.5t$; there $\beta \approx \pi/2 - \alpha$: the up electron sits mostly on one site and the down electron mostly on the other. The restricted point at $(0.785, 0.785)$ lies between the basins on a pass: moving along the line $\beta = \pi/2 - \alpha$ lowers the energy, moving along $\beta = \alpha$ raises it, so it is a saddle with the energy 0. The highest energies (yellow) are in the corners $(0, 0)$ and $(\pi/2, \pi/2)$, where both electrons sit on the same site.

**In [16], the Hohenberg-Kohn map and the exact Kohn-Sham potential.**

```python
deltas = np.linspace(-4.0, 4.0, 81)
density_maps = {U: np.array([two_site(1.0, U, d)[2] for d in deltas])
                for U in (0.0, 2.0, 4.0)}
for U, n_left in density_maps.items():
    check(np.all(np.diff(n_left) > 0),
          f"U = {U:.0f}: n_L increases strictly with Delta (one-to-one map)")
```

81 site-energy differences $\Delta$ from $-4$ to $4$ in steps of $0.1$. The **dictionary comprehension** `{U: ... for U in ...}` stores, for $U = 0, 2, 4$, the exact density $n_L$ of every $\Delta$ (the third number returned by `two_site`). The three checks require each map to rise strictly: different $\Delta$ give different densities (Section 13.8).

```python
def kohn_sham_delta(n_left, t=1.0):
    """The site-energy difference of non-interacting electrons with density n_L."""
    excess = n_left - 1.0
    return 2.0 * t * excess / np.sqrt(1.0 - excess ** 2)


def free_density(delta_s, t=1.0):
    """n_L of two non-interacting electrons with the site energies -+delta_s/2."""
    values, vectors = np.linalg.eigh(np.array([[-delta_s / 2, -t],
                                               [-t, delta_s / 2]]))
    return 2.0 * vectors[0, 0] ** 2
```

`kohn_sham_delta` is the inversion formula $\Delta_s = 2t\,x/\sqrt{1 - x^2}$, $x = n_L - 1$, of Section 13.10. `free_density` solves the non-interacting problem directly: the lowest eigenvector of the $2 \times 2$ matrix, whose L component squared, times two electrons, is $n_L$.

```python
delta_s = {U: kohn_sham_delta(n) for U, n in density_maps.items()}
rebuilt = max(abs(free_density(ds) - n) for U in density_maps
              for ds, n in zip(delta_s[U], density_maps[U]))
check(rebuilt < 1e-12, "the Kohn-Sham site energies reproduce the exact densities")
check(np.max(np.abs(delta_s[0.0] - deltas)) < 1e-12,
      "without interaction the Kohn-Sham potential is the true one")
```

For every $U$ and every exact density the cell computes $\Delta_s$, puts it back into the non-interacting problem and checks that the exact density comes out (to $10^{-12}$); for $U = 0$ the Kohn-Sham potential must be the true one, $\Delta_s = \Delta$.

**In [17], the density map.**

```python
fig, ax = plt.subplots()
for U, style in ((0.0, ":"), (2.0, "--"), (4.0, "-")):
    ax.plot(deltas, density_maps[U], style, label=f"$U = {U:.0f}t$")
ax.axhline(1.0, color="gray", lw=0.8)
ax.set_xlabel("site-energy difference $\\Delta$ ($t$)")
ax.set_ylabel("exact density on the left site $n_L$")
ax.set_title("Hohenberg-Kohn on two sites: the potential determines the density")
ax.legend()
save_figure(fig, "density_map",
```

The loop draws $n_L(\Delta)$ for $U = 0$ (dotted, `":"`), $2t$ (dashed) and $4t$ (solid); the label writes $U$ without decimals (`:.0f`). `axhline(1.0, ...)` draws a thin grey horizontal line at $n_L = 1$, the density of the symmetric sites. Then the axis labels with the unit $t$ of $\Delta$, the title, the legend, and `save_figure` for Figure 13c.7.

**What Figure 13c.7 shows.** All three curves pass through $n_L = 1$ at $\Delta = 0$ and rise strictly from left to right, so no horizontal line meets a curve twice: each density belongs to exactly one $\Delta$, which is the Hohenberg-Kohn statement on two sites. Without repulsion the curve is steep, from about $0.11$ to $1.89$ over $-4 \le \Delta \le 4$ (it is $1 + \Delta/\sqrt{\Delta^2 + 4}$); with $U = 4t$ it only reaches about $0.55$ and $1.45$, because the repulsion opposes putting both electrons on the lower site.

**In [18], the mean field and the parts of the exact Kohn-Sham potential.**

```python
def mean_field_excess(delta, U, t=1.0):
    """The self-consistent x = n_L - 1 of restricted Hartree + exchange."""
    low, high = -1.0, 1.0
    for _ in range(80):  # bisection on x - G(x), which increases with x
        middle = 0.5 * (low + high)
        shifted = delta - U * middle
        if middle - shifted / np.sqrt(shifted ** 2 + 4 * t * t) > 0:
            high = middle
        else:
            low = middle
    return 0.5 * (low + high)
```

In the restricted mean field each electron feels $U$ times the density of the other label on each site, which shifts the site-energy difference to $\Delta - U(n_L - 1)$; the self-consistent excess $x = n_L - 1$ solves $x = G(x) = (\Delta - Ux)/\sqrt{(\Delta - Ux)^2 + 4t^2}$ (derived in Section 13.21). The function finds the root by **bisection**: it starts with the interval $[-1, 1]$, which contains the root, and 80 times halves it, keeping the half in which $x - G(x)$ changes sign (this difference increases with $x$, because $G$ decreases, so there is exactly one root). `for _ in range(80)` repeats 80 times; the name `_` says that the counter is not used.

```python
mf_delta_s = np.array([d - 4.0 * mean_field_excess(d, 4.0) for d in deltas])
nonzero = np.abs(deltas) > 1e-9  # every Delta except 0
hx_part = {U: -U * (density_maps[U] - 1.0) for U in (2.0, 4.0)}  # at the exact n_L
c_part = {U: delta_s[U] - deltas - hx_part[U] for U in (2.0, 4.0)}  # the rest
report("U = 4t, Delta = 2t: Hartree-exchange part", f"{hx_part[4.0][60]:.6f}")
report("U = 4t, Delta = 2t: correlation part", f"{c_part[4.0][60]:.6f}")
```

`mf_delta_s` is the site-energy difference of the self-consistent mean field at $U = 4t$. `nonzero` is a list of true and false values that is false only at $\Delta = 0$. For $U = 2t$ and $4t$, the Hartree-exchange part of the screening, evaluated at the EXACT density, is $\Delta_{Hx} = -U(n_L - 1)$, and the correlation part is the rest, $\Delta_c = \Delta_s - \Delta - \Delta_{Hx}$. At $U = 4t$, $\Delta = 2t$ (entry 60) they are $-0.588239$ and $-1.114408$: correlation does more than half of the screening there.

```python
for U in (2.0, 4.0):
    check(np.all(c_part[U][nonzero] * deltas[nonzero] < 0.0),
          f"U = {U:.0f}t: the correlation part has the sign opposite to Delta")
check(np.all(np.abs(mf_delta_s[nonzero]) > np.abs(delta_s[4.0][nonzero])),
      "U = 4t: the mean field screens less than the exact Kohn-Sham potential")
```

`c_part[U][nonzero]` keeps the entries with $\Delta \ne 0$. The checks require the correlation part to have the sign opposite to $\Delta$ (it screens further, like the Hartree-exchange part) and the mean-field potential to be larger in size than the exact Kohn-Sham one (it screens less).

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.4))
left.plot(deltas, deltas, ":", color="gray", label="$\\Delta_s = \\Delta$ ($U = 0$)")
left.plot(deltas, delta_s[2.0], "--", label="exact Kohn-Sham, $U = 2t$")
left.plot(deltas, delta_s[4.0], color="black", lw=2.0,
          label="exact Kohn-Sham, $U = 4t$")
left.plot(deltas, mf_delta_s, "-.", label="mean field, $U = 4t$")
left.set_xlabel("true site-energy difference $\\Delta$ ($t$)")
left.set_ylabel("Kohn-Sham site-energy difference $\\Delta_s$ ($t$)")
left.set_title("The exact Kohn-Sham potential")
left.legend(fontsize=8)
```

The left panel draws, against the true $\Delta$: the grey dotted line $\Delta_s = \Delta$ (the answer without interaction), the exact Kohn-Sham $\Delta_s$ for $U = 2t$ (dashed) and $U = 4t$ (thick black), and the self-consistent mean field for $U = 4t$ (dash-dotted), with axis labels, title and legend.

```python
right.plot(deltas, delta_s[4.0] - deltas, color="black", lw=2.0,
           label="total screening $\\Delta_s - \\Delta$")
right.plot(deltas, hx_part[4.0], "--", label="Hartree-exchange $\\Delta_{Hx}$")
right.plot(deltas, c_part[4.0], color="tab:red", label="correlation $\\Delta_c$")
right.axhline(0.0, color="gray", lw=0.8)
right.set_xlabel("true site-energy difference $\\Delta$ ($t$)")
right.set_ylabel("parts of $\\Delta_s - \\Delta$ ($t$)")
right.set_title("Its parts at the exact density, $U = 4t$")
right.legend(fontsize=8)
save_figure(fig, "ks_inversion",
```

The right panel draws, for $U = 4t$, the total screening $\Delta_s - \Delta$ (thick black), the Hartree-exchange part (dashed) and the correlation part (red; `"tab:red"` is the red of matplotlib's standard colours), with a grey zero line, axis labels, title and legend. `save_figure` saves Figure 13c.8, and the last check of the cell

```python
check(np.all(np.abs(delta_s[4.0][nonzero]) < np.abs(deltas[nonzero])),
      "the repulsion screens the potential: |Delta_s| < |Delta|")
```

requires $|\Delta_s| < |\Delta|$ for every $\Delta \ne 0$ at $U = 4t$: the repulsion screens the potential.

**What Figure 13c.8 shows.** On the left, every interacting curve is flatter than the dotted line $\Delta_s = \Delta$: the non-interacting electrons need a smaller site-energy difference than the true one to reproduce the exact density, because the repulsion, which the Kohn-Sham electrons do not have, already pushes against piling up on the lower site. At $\Delta = 4t$ the exact $\Delta_s$ is about $2.3t$ for $U = 2t$ and about $1.0t$ for $U = 4t$; the mean field for $U = 4t$ gives about $1.55t$, between the two: it screens less than the exact potential. On the right, at $U = 4t$, both parts of the screening have the sign opposite to $\Delta$; the correlation part is the larger one for $|\Delta|$ up to about $3.4t$ (at $\Delta = 2t$: $-1.114$ against $-0.588$, the numbers printed by the cell), and the Hartree-exchange part beyond.

**In [19], the last check.**

```python
figure_names = ["slater_determinants", "operator_matrices", "density_matrices",
                "two_site_energies", "double_occupancy", "hf_landscape",
                "density_map", "ks_inversion"]
missing = [name for k, name in enumerate(figure_names, 1)
           if not output_file(f"{FIGURE_FOLDER}/13c_{k}_{name}.png").is_file()]
check(missing == [], "all eight figure files exist")
check(output_file(f"{FIGURE_FOLDER}/13c_8_ks_inversion.png").is_file(),
      "the figure file 13c_8_ks_inversion.png exists")
all_checks_passed()
```

`enumerate(figure_names, 1)` pairs each name with its number $k = 1, 2, \dots$; the list comprehension collects the names whose file `13c_k_name.png` does not exist, and the first check requires that list to be empty. The second check names the last figure file, and `all_checks_passed()` prints ALL 33 CHECKS PASSED (notebook 13c): three checks in In [2], one in In [3], two in In [4], three in In [6], one in In [7], two in In [8], one each in In [9] and In [10], two in In [11], three in In [12], two in In [14], one in In [15], five in In [16], four in In [18] and two in In [19].

### 13.15 The uniform gas, the local density approximation and exact local exchange

To use the Kohn-Sham equations we need an approximation for $E_{xc}[n]$. The oldest one borrows it from the only many-body system whose properties are known accurately: the **uniform gas**, infinitely many particles spread with the same density everywhere. This section computes, in three dimensions, its density matrix, its kinetic energy and its exchange energy, and shows why the exchange of a contact interaction is special.

**Spherical coordinates.** The integrals below are done in spherical coordinates: a point $\mathbf r = (x, y, z)$ is given by its distance $r$ from the origin, the angle $\theta$ from the $z$ axis and the angle $\phi$ around it, $x = r\sin\theta\cos\phi$, $y = r\sin\theta\sin\phi$, $z = r\cos\theta$. A small box with the edges $dr$, $r\,d\theta$ and $r\sin\theta\,d\phi$ has the volume $d^3r = r^2\sin\theta\,dr\,d\theta\,d\phi$. With $u = \cos\theta$ (so $du = -\sin\theta\,d\theta$, and $\theta$ from 0 to $\pi$ is $u$ from 1 to $-1$),

$$
\int f\,d^3r = \int_0^\infty r^2\,dr\int_{-1}^{1}du\int_0^{2\pi}d\phi\ f ,
$$

and for a function of $r$ alone this is $4\pi\int_0^\infty r^2 f\,dr$. The same holds for integrals over a wave vector $\mathbf k$, with $k = |\mathbf k|$ in place of $r$, and the axis may point in any direction.

**Plane waves in a box.** Put the gas in a cube of side $\ell$ and volume $V = \ell^3$ whose opposite faces are glued together (a **periodic box**). The orbitals of a free particle are the **plane waves** $e^{i\mathbf k\cdot\mathbf r}/\sqrt V$ with the kinetic energy $\tfrac12 k^2$, and periodicity allows only $\mathbf k = (2\pi/\ell)\,\mathbf m$ with three integers $\mathbf m = (m_x, m_y, m_z)$. Each allowed $\mathbf k$ occupies a little cube of volume $(2\pi/\ell)^3 = (2\pi)^3/V$, so for a large box a sum over the allowed vectors becomes an integral, $\sum_{\mathbf k} \to V\int d^3k/(2\pi)^3$.

**The Fermi sphere.** The non-interacting ground state fills all $\mathbf k$ with $|\mathbf k| < k_F$ (the **Fermi wave number**), once for each of the $g$ labels. Counting, line by line:

$$
N_\sigma = V\,\frac{\tfrac43\pi k_F^3}{(2\pi)^3}, \qquad n_\sigma = \frac{N_\sigma}{V} = \frac{k_F^3}{6\pi^2}, \qquad n = g\,n_\sigma = \frac{g\,k_F^3}{6\pi^2} .
$$

The first is the number of occupied plane waves of one label (the volume of the sphere divided by the volume per $\mathbf k$); the second divides by $V$ and simplifies $\tfrac43\pi/(8\pi^3) = 1/(6\pi^2)$; the third adds the $g$ labels. The kinetic energy per volume is $g\int_{k<k_F}\frac{d^3k}{(2\pi)^3}\frac{k^2}{2} = \frac{g}{2\pi^2}\cdot\frac{k_F^5}{10}$ (spherical coordinates: $4\pi\int_0^{k_F}k^2\cdot\tfrac{k^2}{2}\,dk/(8\pi^3)$). For $g = 2$, eliminating $k_F = (3\pi^2 n)^{1/3}$,

$$
e_{kin}(n) = C_F\,n^{5/3}, \qquad C_F = \tfrac{3}{10}\,(3\pi^2)^{2/3} = 2.871234 \quad \text{(Notebook 13b, In [15])} .
$$

The **Thomas-Fermi** model (1927) took the kinetic energy of every system to be $\int e_{kin}(n(\mathbf r))\,d^3r$, as if each small piece of it were a piece of uniform gas. It is too crude; the Kohn-Sham scheme keeps the kinetic energy exact through $T_s$ and approximates only $E_{xc}$. Notebook 13a (Section 13.32) compares a Thomas-Fermi density with a Kohn-Sham density.

**The density matrix of one label, line by line.** For one label the density matrix of the filled sphere is $\rho_\sigma(\mathbf r, \mathbf r') = \sum_{|\mathbf k|<k_F}\frac{e^{i\mathbf k\cdot\mathbf r}}{\sqrt V}\frac{e^{-i\mathbf k\cdot\mathbf r'}}{\sqrt V}$, a function of the separation $\mathbf R = \mathbf r - \mathbf r'$ only. For a large box, with $R = |\mathbf R|$ and spherical coordinates around $\mathbf R$ (so $\mathbf k\cdot\mathbf R = kRu$):

$$
\begin{aligned}
\rho_\sigma(R) &= \int_{k<k_F}\frac{d^3k}{(2\pi)^3}\,e^{i\mathbf k\cdot\mathbf R}
= \frac{1}{(2\pi)^3}\int_0^{k_F}k^2\,dk\int_{-1}^{1}du\int_0^{2\pi}d\phi\ e^{ikRu} \\
&= \frac{2\pi}{(2\pi)^3}\int_0^{k_F}k^2\,\frac{e^{ikR} - e^{-ikR}}{ikR}\,dk
= \frac{1}{2\pi^2 R}\int_0^{k_F}k\,\sin(kR)\,dk \\
&= \frac{1}{2\pi^2 R}\Big[\frac{\sin(kR)}{R^2} - \frac{k\cos(kR)}{R}\Big]_0^{k_F}
= \frac{\sin(k_F R) - k_F R\cos(k_F R)}{2\pi^2 R^3} .
\end{aligned}
$$

The first step replaces the sum by the integral; the second writes it in spherical coordinates; the third does the $\phi$ integral ($2\pi$) and the $u$ integral (the antiderivative of $e^{ikRu}$ in $u$ is $e^{ikRu}/(ikR)$); the fourth uses $e^{i\alpha} - e^{-i\alpha} = 2i\sin\alpha$ and simplifies; the fifth integrates by parts ($\int k\sin(kR)\,dk = -k\cos(kR)/R + \int\cos(kR)/R\,dk$); the sixth inserts the limits and collects. Dividing by $n_\sigma = k_F^3/(6\pi^2)$ and writing $s = k_F R$:

$$
\frac{\rho_\sigma(R)}{n_\sigma} = F(k_F R), \qquad F(s) = \frac{3\,(\sin s - s\cos s)}{s^3} .
$$

Near $s = 0$ the Taylor series $\sin s = s - s^3/6 + s^5/120 - s^7/5040$ and $s\cos s = s - s^3/2 + s^5/24 - s^7/720$ give $\sin s - s\cos s = s^3/3 - s^5/30 + s^7/840$, so $F(s) = 1 - s^2/10 + s^4/280 + \dots$, and $F(0) = 1$: at zero separation the density matrix is the density. Notebook 13b (In [3], Figure 13b.1) compares $F$ with the sums over the plane waves of finite boxes: along the $x$ axis only $m_x$ matters, the sine parts of $m_x$ and $-m_x$ cancel, and $\rho_\sigma(R)/n_\sigma = \frac{1}{N_\sigma}\sum_{m_x}c(m_x)\cos(2\pi m_x R/\ell)$, where $c(m_x)$ counts the occupied lattice points with this $m_x$; the difference from $F$ shrinks from $0.037$ to $0.0008$ as the box grows from 251 to 137059 plane waves.

**The exchange hole.** By Wick's theorem (Section 13.4) the probability density of finding one fermion at $\mathbf r$ and another at $\mathbf r'$ is $n(\mathbf r)n(\mathbf r') - \sum_\sigma|\rho_\sigma(\mathbf r, \mathbf r')|^2$ (the second term is the exchange term of the four-operator formula; only equal labels contribute). With $g$ equally occupied labels, $n_\sigma = n/g$, and divided by $n^2$:

$$
g_{pair}(R) = 1 - \frac{g\,n_\sigma^2F(k_F R)^2}{n^2} = 1 - \frac{1}{g}\,F(k_F R)^2 .
$$

At $R = 0$ it is $1 - 1/g$: a second fermion with the same label is never found at the same point, one with another label as often as without the Pauli principle. This dip is the **exchange hole** (Figure 13b.2); its size is about $1/k_F$.

**Contact interaction in the uniform gas.** With $w = g_c\,\delta(\mathbf r - \mathbf r')$, Section 13.5 gives per volume $e_H = \tfrac{g_c}{2}n^2$ and $e_x = -\tfrac{g_c}{2}\sum_\sigma n_\sigma^2 = -\tfrac{g_c}{2g}n^2$, so

$$
e_H + e_x = \frac{g_c}{2}\,n^2\Big(1 - \frac{1}{g}\Big) = \frac{g_c}{2}\,n^2\,g_{pair}(0) :
$$

the interaction counts only the pairs that can meet, those of different labels (Figure 13b.3).

**A finite range shrinking to a contact, line by line.** Replace the contact by a Gaussian of range $a$ with the same total strength, $w_a(R) = g_c\,(2\pi a^2)^{-3/2}e^{-R^2/(2a^2)}$, whose integral over all space is $g_c$. Its Hartree energy is still $\tfrac{g_c}{2}n^2$ (for a uniform density only the integral of $w$ enters), but its exchange energy per volume is $e_x(a) = -\tfrac12\sum_\sigma n_\sigma^2\int w_a(R)\,F(k_F R)^2\,d^3R$ (Section 13.5 with $\rho_\sigma = n_\sigma F$). Hence

$$
\frac{e_x(a)}{e_x(0)} = \frac{1}{g_c}\int w_a(R)\,F(k_F R)^2\,d^3R = \frac{1}{g_c}\int_0^\infty 4\pi R^2\,w_a(R)\,F(k_F R)^2\,dR .
$$

For a small range only small $R$ matter, where $F(s)^2 = (1 - s^2/10 + \dots)^2 = 1 - s^2/5 + \dots$:

$$
\frac{e_x(a)}{e_x(0)} \approx \frac{1}{g_c}\int w_a\Big(1 - \frac{k_F^2R^2}{5}\Big)d^3R = 1 - \frac{k_F^2}{5g_c}\int w_a\,R^2\,d^3R = 1 - \frac{k_F^2}{5}\cdot 3a^2 = 1 - \frac35\,(k_F a)^2 .
$$

The first step inserts the expansion; the second uses $\int w_a\,d^3R = g_c$; the third uses $\int w_a R^2\,d^3R = 3a^2g_c$ (the Gaussian has the variance $a^2$ along each of the three axes, and $R^2 = x^2 + y^2 + z^2$). So the exchange energy of a finite-range interaction approaches the contact value when the range is much smaller than the size $1/k_F$ of the exchange hole (Notebook 13b, In [8], Figure 13b.4).

**For comparison: the Coulomb interaction.** For electrons ($g = 2$, $w = 1/R$ in atomic units) the same formula gives

$$
e_x = -\tfrac12\cdot 2\,n_\sigma^2\int_0^\infty 4\pi R^2\,\frac{F(k_F R)^2}{R}\,dR = -\frac{4\pi n_\sigma^2}{k_F^2}\int_0^\infty s\,F(s)^2\,ds ,
$$

by substituting $s = k_F R$. The integral is $9/4$: COMPUTED by Notebook 13b (In [10]) to $10^{-7}$ with Simpson's rule up to $s = 4000$ plus the tail beyond (for large $s$, $F \approx -3\cos s/s^2$, so the integrand is about $9\cos^2 s/s^3$, whose average $\cos^2 = \tfrac12$ gives the tail $9/(4\cdot 4000^2)$); it can also be evaluated exactly by Fourier transforms, which this book does not need. With $n_\sigma = n/2$ and $k_F = (3\pi^2 n)^{1/3}$ this is **Dirac's exchange energy** (1930),

$$
e_x(n) = -\frac34\Big(\frac{3}{\pi}\Big)^{1/3}n^{4/3} = -0.738559\,n^{4/3} \quad \text{(Notebook 13b, In [10])} .
$$

It is a function of the local density because the gas is uniform; the contact exchange $-\tfrac{g_c}{4}n^2$ ($g = 2$) is a function of the local density because the interaction has no range (Figure 13b.5 compares the two per particle: slopes 1 and 1/3 on logarithmic axes).

**Simpson's rule.** Several notebooks of this chapter integrate with **Simpson's rule**. On three equally spaced points $-h, 0, h$ it integrates the parabola $a + bx + cx^2$ through the three values exactly: $\int_{-h}^{h}(a + bx + cx^2)\,dx = 2ah + \tfrac23 ch^3$; the values give $f(0) = a$ and $f(h) + f(-h) = 2a + 2ch^2$, so $ch^2 = \tfrac12(f(h) + f(-h)) - a$, and inserting, $\int = 2ah + \tfrac{h}{3}(f(h) + f(-h)) - \tfrac23 ah = \tfrac{h}{3}\big[f(-h) + 4f(0) + f(h)\big]$. Adding such panels over an even number of intervals gives $\tfrac{h}{3}[f_0 + 4f_1 + 2f_2 + 4f_3 + \dots + 4f_{K-1} + f_K]$: the end values once, the odd ones four times, the inner even ones twice. (It is even exact for cubic polynomials, because the term $x^3$ integrates to zero on a symmetric panel.)

**The local density approximation.** A real density varies in space. The **local density approximation** (LDA) treats each small volume as a piece of uniform gas with the local density:

$$
E_{xc}^{LDA}[n] = \int e_{xc}\big(n(\mathbf r)\big)\,d^3r, \qquad v_{xc}^{LDA}(\mathbf r) = \frac{de_{xc}}{dn}\Big|_{n(\mathbf r)}
$$

(example (ii) of Section 13.9). For electrons its exchange part is Dirac's formula, $v_x = -(3/\pi)^{1/3}n^{1/3}$; its correlation part is taken from numerical simulations of the uniform gas, which we quote as a fact of the literature and do not use in this book. The LDA is exact for a uniform density and an approximation for every other one.

**For a contact interaction exchange needs no approximation.** Put $w = g_c\,\delta(\mathbf r - \mathbf r')$ (independent of the labels) into the exchange integral of Section 13.5 for ANY determinant or non-interacting ensemble:

$$
E_x = -\frac{g_c}{2}\int\sum_{\sigma,\sigma'}\big|\rho(\mathbf r\sigma, \mathbf r\sigma')\big|^2\,d^3r .
$$

This is exactly local: it needs only the $g \times g$ matrix $\rho(\mathbf r\sigma, \mathbf r\sigma')$ at each point. For orbitals of definite label the off-diagonal entries vanish and $E_x = -\tfrac{g_c}{2}\int\sum_\sigma n_\sigma^2\,d^3r$; evaluated with all the label densities it is exact, evaluated with the total density alone as $-\tfrac{g_c}{2g}\int n^2$ it is exact only when all labels are equally occupied. Notebook 13b checks this for a non-uniform determinant in a box (In [12]: the two-point Fock form and the local form both give $-19.0000000000$) and for orbitals that mix the labels (In [13]: the local form needs the whole $2 \times 2$ matrix; its diagonal alone misses $1.24$ of the $8.74$). An "exchange-only" local functional of this kind is the Hartree-Fock energy written as a density functional; what it leaves out is correlation.

**Exchange favours unequal labels, line by line.** In this exchange-only picture a gas with two labels can lower its interaction energy by occupying the labels unequally, at the price of kinetic energy. With the **polarisation** $\zeta = (n_\uparrow - n_\downarrow)/n$, so $n_\uparrow = \tfrac{n}{2}(1 + \zeta)$ and $n_\downarrow = \tfrac{n}{2}(1 - \zeta)$: one label alone ($g = 1$) has the kinetic energy $\tfrac{3}{10}(6\pi^2)^{2/3}n_\sigma^{5/3}$ per volume (the formula above with $g = 1$), and the contact interaction gives $g_c\,n_\uparrow n_\downarrow$ (Section 13.5). Adding,

$$
e(\zeta) = C_F\,n^{5/3}\,\frac{(1 + \zeta)^{5/3} + (1 - \zeta)^{5/3}}{2} + \frac{g_c}{4}\,n^2\,(1 - \zeta^2) ,
$$

where the kinetic part was rewritten with $\tfrac{3}{10}(6\pi^2)^{2/3}(\tfrac{n}{2})^{5/3} = \tfrac12 C_F n^{5/3}$ (because $6^{2/3}\,2^{-5/3} = 3^{2/3}\,2^{2/3}\,2^{-5/3} = 3^{2/3}/2$) and $n_\uparrow n_\downarrow = \tfrac{n^2}{4}(1 - \zeta^2)$. Differentiating twice at $\zeta = 0$: $\frac{d^2}{d\zeta^2}(1 \pm \zeta)^{5/3} = \tfrac53\cdot\tfrac23(1\pm\zeta)^{-1/3} = \tfrac{10}{9}$ at $\zeta = 0$, so

$$
e''(0) = \frac{10}{9}\,C_F\,n^{5/3} - \frac{g_c}{2}\,n^2 ,
$$

which is negative (the unpolarised gas is unstable) exactly when $g_c\,n^{1/3} > \gamma_c = \tfrac{20}{9}C_F = \tfrac23(3\pi^2)^{2/3} = 6.380520$. This is a property of the exchange-only functional; correlation, left out here, weakens it (Notebook 13b, In [15], Figure 13b.7).

### 13.16 The exchange of the 16-component field dirac16complex

This section carries Section 13.15 over to the field of this book. In this section and in Section 13.37, $\Psi$ is the dirac16complex field and $x_1, \dots, x_8$ are the author's coordinates: $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the three extra times, which deflate exponentially, and $x_8$ the hidden direction.

**The matrices.** The author's gamma matrices $\gamma^{(x1)}, \dots, \gamma^{(x8)}$ are eight REAL $16 \times 16$ matrices (entries $0$ and $\pm1$) with $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}\,1$, $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in the order $x_1, \dots, x_8$ (Chapter 4 builds them; `Revision/algebra/reports/wolfram-algebra.json`, checks reality and Clifford_relation, both PASS). So each space-like gamma squares to $+1$, $\gamma^{(x4)}$ squares to $-1$, and two different gammas anticommute. From them,

$$
C = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}, \qquad B = -i\,C\,\gamma^{(x4)} .
$$

$C$ is real and symmetric (Revision check C_real_symmetric); $B$ is the indefinite (Krein) form of Chapter 10, with the number density $n = \langle\Psi^\dagger B\Psi\rangle$. Four facts, line by line. (a) $C^2 = 1$: in $C^2 = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}\gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}$ move the second $\gamma^{(x8)}$ to the left past three gammas (sign $(-1)^3$) and use $(\gamma^{(x8)})^2 = 1$; then move the second $\gamma^{(x1)}$ past two (sign $+1$), then the second $\gamma^{(x2)}$ past one (sign $-1$); the signs multiply to $(-1)(+1)(-1) = +1$ and every square is $+1$. (b) $\gamma^{(x4)}$ commutes with $C$: moving it through the four factors of $C$ costs four sign changes, $(-1)^4 = 1$. (c) $B^2 = 1$: $B^2 = (-i)^2\,C\gamma^{(x4)}C\gamma^{(x4)} = -\,C\,C\,\gamma^{(x4)}\gamma^{(x4)} = -(+1)(-1) = 1$, by (b), (a) and $(\gamma^{(x4)})^2 = -1$. (d) $CBC = -i\,C\,C\,\gamma^{(x4)}C = -i\,\gamma^{(x4)}C = -i\,C\gamma^{(x4)} = B$ by (a) and (b); and $\mathrm{Tr}(BC) = -i\,\mathrm{Tr}(C\gamma^{(x4)}C) = -i\,\mathrm{Tr}(\gamma^{(x4)}C^2) = -i\,\mathrm{Tr}\,\gamma^{(x4)} = 0$, using that a trace does not change when the first factor is moved to the end, and that the trace of a single gamma vanishes ($\mathrm{Tr}\,\gamma^{(x4)} = \mathrm{Tr}(\gamma^{(x4)}\gamma^{(x1)}\gamma^{(x1)}) = -\mathrm{Tr}(\gamma^{(x1)}\gamma^{(x4)}\gamma^{(x1)}) = -\mathrm{Tr}(\gamma^{(x4)}\gamma^{(x1)}\gamma^{(x1)}) = -\mathrm{Tr}\,\gamma^{(x4)}$). Finally $\mathrm{Tr}\,1 = 16$.

**The interaction and Wick's theorem.** The Kohn-Sham model of Chapter 14 has the contact interaction $U(S) = \tfrac{\lambda}{2}S^2$ with the scalar density $S = \bar\Psi\Psi = \Psi^\dagger C\,\Psi$ (normal ordered, $\lambda > 0$ repulsive). Its expectation values follow the rule $\langle\Psi^\dagger M\Psi\rangle = \mathrm{Tr}(M\rho)$ with a local $16 \times 16$ one-body matrix $\rho$ (Chapter 10), and the identity of Section 13.4 with the vertex $V = C$ gives, per unit volume,

$$
e_H = \frac{\lambda}{2}\,(\mathrm{Tr}\,C\rho)^2, \qquad e_x = -\frac{\lambda}{2}\,\mathrm{Tr}(C\rho\,C\rho) .
$$

(For $g$ ordinary labels the vertex is the unit matrix and $\rho = (n/g)\,1$, which gives back $e_x = -\tfrac{g_c}{2}\,g\,(n/g)^2 = -\tfrac{g_c}{2g}n^2$.)

**The uniform good-sector gas, line by line.** For the uniform gas of the good sector (no extra-time momentum, Chapter 14), with any occupation that is symmetric under $\mathbf p \to -\mathbf p$ and at any temperature, the Revision record finds $\rho = (nB + SC)/16$ (`Revision/kohn_sham/ks-theory.json`, exchange.uniformGas; Chapter 14 derives it). First the densities come back:

$$
\mathrm{Tr}(B\rho) = \frac{n\,\mathrm{Tr}\,B^2 + S\,\mathrm{Tr}\,BC}{16} = \frac{16n + 0}{16} = n, \qquad \mathrm{Tr}(C\rho) = \frac{n\,\mathrm{Tr}\,CB + S\,\mathrm{Tr}\,C^2}{16} = S ,
$$

by linearity of the trace, $B^2 = C^2 = 1$ and $\mathrm{Tr}(BC) = \mathrm{Tr}(CB) = 0$. Then the exchange trace:

$$
\begin{aligned}
\mathrm{Tr}(C\rho\,C\rho) &= \frac{1}{256}\,\mathrm{Tr}\big[C(nB + SC)\,C(nB + SC)\big] \\
&= \frac{1}{256}\big[n^2\,\mathrm{Tr}(CBCB) + nS\,\mathrm{Tr}(CBCC) + Sn\,\mathrm{Tr}(CCCB) + S^2\,\mathrm{Tr}(CCCC)\big] \\
&= \frac{1}{256}\big[n^2\,\mathrm{Tr}(B^2) + nS\,\mathrm{Tr}(CB) + Sn\,\mathrm{Tr}(CB) + S^2\,\mathrm{Tr}\,1\big] \\
&= \frac{16\,n^2 + 16\,S^2}{256} = \frac{n^2 + S^2}{16} .
\end{aligned}
$$

The first line inserts $\rho$; the second multiplies out (four terms); the third uses $CBC = B$ in the first term and $C^2 = 1$ in the others; the fourth uses $\mathrm{Tr}\,B^2 = \mathrm{Tr}\,1 = 16$ and $\mathrm{Tr}(CB) = 0$. Hence

$$
e_H = \frac{\lambda}{2}\,S^2, \qquad e_x = -\frac{\lambda}{32}\,\big(n^2 + S^2\big) .
$$

**The Kohn-Sham potentials.** The interaction energy per volume is $e_{int} = e_H + e_x = \tfrac{15}{32}\lambda S^2 - \tfrac{1}{32}\lambda n^2$. As in example (ii) of Section 13.9, the functional derivatives of $\int e_{int}$ are ordinary derivatives of $e_{int}$: with respect to $S$ it shifts the mass, with respect to $n$ it is a potential,

$$
M_{eff} = m + \frac{\partial e_{int}}{\partial S} = m + \frac{15}{16}\,\lambda S, \qquad v_v = \frac{\partial e_{int}}{\partial n} = -\frac{1}{16}\,\lambda n .
$$

For one filled 8-fold level at rest, $n = S$, the ratio is $e_x/e_H = -\tfrac{\lambda}{32}\cdot 2S^2\big/\tfrac{\lambda}{2}S^2 = -\tfrac18$: the rule $E_x = -E_H/g$ of Section 13.5 with $g = 8$, the number of good-sector states per momentum.

**Status.** PROVED in the Revision record by two independent programs, and used unchanged by the Revision Kohn-Sham solver:

| record file | checks or entries | result |
| --- | --- | --- |
| `Revision/kohn_sham/reports/ks-theory-python.json` | exchange_uniform_gas, ks_potentials, filled_shell_ratio | PASS |
| `Revision/kohn_sham/reports/ks-theory-wolfram.json` | exchange_uniform_gas, ks_potentials | PASS |
| `Revision/kohn_sham/results/parameters.json` | theoryInputs: the coefficients $-1/32$, $15/16$, $-1/16$ | used by the solver |

Notebook 13b reproduces all of them exactly from the gamma matrices. **What is approximate.** The record's functional is Hartree plus this uniform-gas exchange, with no correlation term. For the Kohn-Sham determinants of Chapter 14, which are not uniform, the exact Fock exchange of a closed shell is still local but differs from the uniform-gas form by $+\tfrac{\lambda}{32}Q^2$ per volume, where $Q$ is a further density (exactFockSlab in `Revision/kohn_sham/ks-theory.json`, labelled DIAGNOSTIC there; check exchange_slab_exact_fock of `Revision/kohn_sham/reports/ks-theory-python.json`, PASS; the solver reports this difference in the column deltaE_x_exact_fock_diag of `Revision/kohn_sham/results/exx/exact-fock-variant.csv`). Using the uniform-gas exchange and leaving out correlation is therefore the approximation of the dirac16complex Kohn-Sham model, as the omission of correlation is the approximation of the toy models of this chapter.

### 13.17 Example: exchange of a contact interaction

Notebook 13b computes everything of Sections 13.15 and 13.16: the density matrix of one label of the uniform gas from its closed form and from box sums, the exchange hole for 1, 2 and 8 labels, the contact energies and the rule $E_x = -E_H/g$, the approach of a Gaussian interaction to the contact limit, Dirac's Coulomb exchange for comparison, the exactness of the local formula for any determinant (also with label-mixing orbitals), the polarisation instability, and finally, exactly with fractions, the exchange of the 16-component field from the Revision gamma matrices, reproducing three checks of the Revision record. It ends with ALL 34 CHECKS PASSED (notebook 13b) and draws nine figures.

<!-- NOTEBOOK 13b -->

### 13.20 Line-by-line walk-through of Notebook 13b

The notebook has 21 code cells. **In [1]** is the set-up cell, identical to In [1] of Notebook 13c (explained line by line in Section 13.14) except that its name is `"13b"` and its comment lines hold the instructions of Section 13.18.

**In [2], the function $F$.**

```python
import numpy as np  # arrays, matrices and linear algebra
```

The cell loads numpy under the short name `np`, as in Notebook 13c.

```python
def F(s):
    """F(s) = 3 (sin s - s cos s) / s^3, the density matrix of one label over n."""
    s = np.asarray(s, dtype=float)
    result = 1.0 - s ** 2 / 10.0 + s ** 4 / 280.0  # the Taylor series near 0
    big = s >= 1e-3  # where the closed form is accurate
    sb = s[big]
    result[big] = 3.0 * (np.sin(sb) - sb * np.cos(sb)) / sb ** 3
    return result
```

`np.asarray(s, dtype=float)` turns the argument, a number or an array, into an array of floating-point numbers. For small $s$ the closed form divides two tiny numbers and loses digits, so the function first fills `result` with the Taylor series of Section 13.15 everywhere, then marks the places where $s \ge 10^{-3}$ (`big` is an array of true and false values), takes those values (`s[big]`) and overwrites the result there with the closed form.

```python
s_test = 1e-3
closed = 3.0 * (np.sin(s_test) - s_test * np.cos(s_test)) / s_test ** 3
series = 1.0 - s_test ** 2 / 10.0 + s_test ** 4 / 280.0
say(f"at s = 0.001: closed form {closed:.12f}, series {series:.12f}")
check(abs(closed - series) < 1e-8,
      "the closed form and the series agree at s = 0.001 (to about 9 digits)")
```

At the switching point both forms are computed and printed with 12 decimals: $0.999999899944$ and $0.999999900000$. They differ by $6\cdot10^{-11}$: the closed form has already lost several digits to rounding (the exact value is $1 - 10^{-7} + 3.6\cdot10^{-15}$), which is why the series is used below this point.

**In [3], box sums.**

```python
s_grid = np.linspace(0.0, 12.0, 121)  # s = k_F R from 0 to 12
box_results = {}
for m_F in (4, 8, 16, 32):
    m = np.arange(-m_F, m_F + 1)  # the possible integers m_x, m_y, m_z
    my, mz = np.meshgrid(m, m, indexing="ij")  # all pairs (m_y, m_z)
    q = my ** 2 + mz ** 2
    counts = np.array([np.count_nonzero(q < m_F ** 2 - mx ** 2) for mx in m])
    N_label = int(counts.sum())  # occupied plane waves of one label
```

For spheres of radius $m_F = 4, 8, 16, 32$ lattice steps: `np.arange(-m_F, m_F + 1)` is the list of integers from $-m_F$ to $m_F$; `np.meshgrid` makes all pairs $(m_y, m_z)$, and `q` their $m_y^2 + m_z^2$. For each $m_x$, `np.count_nonzero(q < m_F ** 2 - mx ** 2)` counts the pairs with $m_x^2 + m_y^2 + m_z^2 < m_F^2$: the number $c(m_x)$ of occupied plane waves with this $m_x$. Their sum is $N_\sigma$.

```python
    kF_ell = 2.0 * np.pi * (3.0 * N_label / (4.0 * np.pi)) ** (1.0 / 3.0)
    R_over_ell = s_grid / kF_ell  # the separations R / ell for these s
    ratio = np.array([np.sum(counts * np.cos(2.0 * np.pi * m * r))
                      for r in R_over_ell]) / N_label
    box_results[m_F] = (N_label, ratio)
    deviation = np.max(np.abs(ratio - F(s_grid)))
    say(f"m_F = {m_F:2d}: {N_label:6d} plane waves; largest difference from "
        f"F = {deviation:.5f}")
```

The Fermi wave number is defined by the count, $N_\sigma = \tfrac43\pi(k_F\ell/2\pi)^3$, solved for $k_F\ell$. For each $s$ the separation is $R/\ell = s/(k_F\ell)$, and `ratio` is the box sum $\frac{1}{N_\sigma}\sum_{m_x}c(m_x)\cos(2\pi m_x R/\ell)$ of Section 13.15. The cell stores the result and prints the largest difference from $F$ on the grid of $s$.

```python
deviations = [np.max(np.abs(box_results[m_F][1] - F(s_grid)))
              for m_F in (4, 8, 16, 32)]
shrinking = all(a > b for a, b in zip(deviations, deviations[1:]))
check(shrinking and deviations[-1] < 2e-3,
      "the box sums approach the closed form F as the box holds more particles")
```

`zip(deviations, deviations[1:])` pairs each difference with the next one; `all(a > b ...)` is true when every difference is larger than the next. The check also requires the largest box to be within $2\cdot10^{-3}$ of $F$. The printed differences are $0.03729$, $0.01218$, $0.00184$ and $0.00083$ for 251, 2103, 17071 and 137059 plane waves.

**In [4], the density matrix as a picture.**

```python
fig, ax = plt.subplots()
ax.plot(s_grid, F(s_grid), color="black", lw=2.0,
        label="continuum $F(k_F R) = 3(\\sin s - s\\cos s)/s^3$")
```

One panel; the closed form $F$ on the 121 values of $s$ as a thick black line. In the label, `\\sin` reaches matplotlib as `\sin`, which it draws as the function name sin.

```python
for m_F, marker in ((4, "o"), (32, "x")):
    N_label, ratio = box_results[m_F]
    ax.plot(s_grid[::3], ratio[::3], marker, ms=4,
            label=f"box sum, {N_label} plane waves")
ax.axhline(0.0, color="gray", lw=0.8)
```

For the smallest box ($m_F = 4$, circles, style `"o"`) and the largest ($m_F = 32$, crosses, `"x"`) the loop takes the stored count and box sum and draws every third value (`[::3]` takes the entries 0, 3, 6, ...), as markers without a connecting line, so that the black curve stays visible; the label gives the number of plane waves. `axhline(0.0, ...)` draws the zero line.

```python
ax.set_xlabel("$s = k_F R$ (separation times Fermi wave number)")
ax.set_ylabel("$\\rho_\\sigma(R) / n_\\sigma$")
ax.set_title("Density matrix of one label of the uniform gas")
ax.legend(fontsize=8)
save_figure(fig, "density_matrix",
```

Axis labels (both quantities are pure numbers), title, legend and `save_figure` for Figure 13b.1; one line of its caption is an f-string that writes the two plane-wave counts, 251 and 137059, into the caption.

**What Figure 13b.1 shows.** The density matrix of one label starts at 1 for $R = 0$ (there it is the density itself), falls to zero near $k_FR = 4.5$ (the first zero of $\sin s - s\cos s$, where $\tan s = s$), swings to a small negative minimum of about $-0.086$ near $k_FR = 5.76$, and oscillates with a shrinking amplitude. A fermion "remembers" another one of its label only within a distance of a few $1/k_F$. The crosses of the large box lie on the curve; the circles of the small box (251 plane waves) deviate visibly beyond $k_FR \approx 4$, by at most $0.037$.

**In [5], the exchange hole.**

```python
s_fine = np.linspace(0.0, 10.0, 501)
fig, ax = plt.subplots()
for g in (1, 2, 8):
    pair = 1.0 - F(s_fine) ** 2 / g  # the pair distribution
    ax.plot(s_fine, pair, label=f"$g = {g}$ labels: $g_{{pair}}(0) = {1 - 1 / g:.3f}$")
    check(abs(pair[0] - (1.0 - 1.0 / g)) < 1e-15,
          f"the pair distribution at contact is 1 - 1/g for g = {g}")
```

For $g = 1, 2, 8$ the cell computes $g_{pair} = 1 - F^2/g$ of Section 13.15 on 501 values of $s$ from 0 to 10, draws it (in an f-string a doubled brace prints one brace, so the label shows $g_{pair}$, followed by the value $1 - 1/g$ with three decimals), and checks its value at $s = 0$, the first entry `pair[0]`.

```python
ax.axhline(1.0, color="gray", ls="--", lw=0.8)
ax.set_xlabel("$k_F R$")
ax.set_ylabel("pair distribution $g_{pair}(R)$")
ax.set_title("The exchange hole of the uniform gas")
ax.legend(fontsize=8)
save_figure(fig, "exchange_hole",
```

A grey dashed horizontal line at 1 (the keyword `ls`, short for line style, set to two hyphens, makes it dashed), the value without the Pauli principle; axis labels, title, legend, and `save_figure` for Figure 13b.2.

**What Figure 13b.2 shows.** Far from a fermion (beyond about $k_FR = 4$) all three curves are at 1: there the Pauli principle has no effect. Near it they dip to $1 - 1/g$ at contact: to 0 for one label (no second fermion can come close), to $\tfrac12$ for two labels (only the half with the other label can), and to $0.875$ for eight labels. The more labels, the shallower the hole, because a smaller fraction $1/g$ of the other fermions shares the first one's label.

**In [6], contact energies.**

```python
G_C = 1.0  # the strength of the contact interaction
densities = np.linspace(0.0, 2.0, 41)  # n from 0 to 2 (particles per volume)


def contact_energies(n, g):
    """(e_H, e_x) per volume for g equally occupied labels: n_sigma = n / g."""
    e_hartree = 0.5 * G_C * n ** 2
    e_exchange = -0.5 * G_C * g * (n / g) ** 2  # -(g_c/2) sum over g labels
    return e_hartree, e_exchange
```

The function returns $e_H = \tfrac{g_c}{2}n^2$ and $e_x = -\tfrac{g_c}{2}\sum_\sigma n_\sigma^2$ with the $g$ equal label densities $n/g$, for 41 densities from 0 to 2.

```python
for g in (1, 2, 8):
    e_hartree, e_exchange = contact_energies(densities, g)
    ratio = e_exchange[1:] / e_hartree[1:]  # skip n = 0 (0/0)
    check(np.allclose(ratio, -1.0 / g, rtol=0, atol=1e-15),
          f"e_x = -e_H/g for g = {g}")
e_hartree, e_exchange = contact_energies(densities, 1)
check(np.max(np.abs(e_hartree + e_exchange)) == 0.0,
      "for a single label the contact interaction cancels exactly")
```

`[1:]` leaves out the first entry, $n = 0$, where the ratio would be $0/0$. Three checks of $e_x/e_H = -1/g$, and one that for $g = 1$ the sum is exactly zero.

**In [7], the energies as pictures.**

```python
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.0), sharey=True)
for ax, g in zip(axes, (2, 8)):
    e_hartree, e_exchange = contact_energies(densities, g)
    ax.plot(densities, e_hartree, label="Hartree $e_H = g_c n^2/2$")
    ax.plot(densities, e_exchange, label=f"exchange $e_x = -e_H/{g}$")
    ax.plot(densities, e_hartree + e_exchange, color="black", lw=2.0,
            label="sum $e_H + e_x$")
```

Two panels with a common vertical axis (`sharey=True`: both use the same scale, so the curves can be compared by eye). For $g = 2$ (left panel) and $g = 8$ (right panel) the loop computes the two energy densities on the 41 densities and draws $e_H$, $e_x$ and, as a thick black line, their sum.

```python
    ax.axhline(0.0, color="gray", lw=0.8)
    ax.set_xlabel("density $n$")
    ax.set_title(f"$g = {g}$ labels")
    ax.legend(fontsize=8)
axes[0].set_ylabel("energy per volume (units of $g_c$)")
save_figure(fig, "contact_energies",
```

Still inside the loop: the zero line, the horizontal label, a title that names $g$, and a legend for each panel. After the loop, only the left panel (`axes[0]`) gets the vertical label, which the right panel shares; `save_figure` saves Figure 13b.3.

**What Figure 13b.3 shows.** The Hartree energy $n^2/2$ is the same parabola in both panels (it reaches 2 at $n = 2$). The exchange energy mirrors a part of it below zero: half of it for two labels ($-1$ at $n = 2$), one eighth for eight labels ($-0.25$). The sum is therefore half of the Hartree energy for $g = 2$ and seven eighths of it for $g = 8$: the more labels, the larger the fraction of pairs that can meet, and the less exchange removes.

**In [8], a finite range.**

```python
def simpson(values, step):
    """Simpson's rule for equally spaced values (an odd number of them)."""
    return step / 3.0 * (values[0] + values[-1] + 4.0 * values[1:-1:2].sum()
                         + 2.0 * values[2:-1:2].sum())
```

Simpson's rule of Section 13.15: `values[1:-1:2]` are the entries 1, 3, 5, ... (every second one, starting at 1, without the last), weighted 4; `values[2:-1:2]` are the inner even entries 2, 4, ..., weighted 2; the two ends are weighted 1.

```python
s_int = np.linspace(0.0, 80.0, 400001)  # s = k_F R; the Gaussian is tiny beyond
ds = s_int[1] - s_int[0]
F2 = F(s_int) ** 2


def exchange_ratio(kF_a):
    """e_x(a) / e_x(0) for the Gaussian of range a (k_F a given)."""
    norm = (2.0 * np.pi * kF_a ** 2) ** -1.5  # makes the integral of w_a equal g_c
    gauss = norm * np.exp(-s_int ** 2 / (2.0 * kF_a ** 2))
    return simpson(4.0 * np.pi * s_int ** 2 * gauss * F2, ds)
```

The integral of Section 13.15 is written in the variable $s = k_F R$, so lengths are measured in units of $1/k_F$ and the range enters only as $k_F a$: the ratio is $\int_0^\infty 4\pi s^2\,(2\pi(k_Fa)^2)^{-3/2}e^{-s^2/(2(k_Fa)^2)}F(s)^2\,ds$, integrated by Simpson's rule on 400001 points from 0 to 80 (spacing $0.0002$; beyond 80 the Gaussian is negligible for the ranges used).

```python
ranges = np.logspace(-2, 1, 31)  # k_F a from 0.01 to 10
ratios = np.array([exchange_ratio(r) for r in ranges])
for r in (0.01, 0.1, 1.0):
    say(f"k_F a = {r:5.2f}: e_x(a)/e_x(0) = {exchange_ratio(r):.6f}, "
        f"small-a formula {1.0 - 0.6 * r ** 2:.6f}")
check(abs(exchange_ratio(0.05) - (1.0 - 0.6 * 0.05 ** 2)) < 1e-5,
      "for small range the ratio is 1 - (3/5)(k_F a)^2")
check(np.all(np.diff(ratios) < 0.0) and ratios[0] > 0.9999,
      "the exchange energy grows towards the contact value as the range shrinks")
```

`np.logspace(-2, 1, 31)` gives 31 numbers from $10^{-2}$ to $10^1$, equally spaced on a logarithmic scale. The printed lines compare the ratio with $1 - \tfrac35(k_Fa)^2$: they agree at $k_Fa = 0.01$ ($0.999940$) and nearly at $0.1$, and differ at $1$ ($0.588864$ against $0.4$), where the expansion no longer holds. The checks: the small-range formula at $k_Fa = 0.05$, and the ratio falls with every increase of the range and is above $0.9999$ at the smallest one.

**In [9], the ratio as a picture.**

```python
fig, ax = plt.subplots()
ax.semilogx(ranges, ratios, "o-", ms=3, color="black",
            label="$e_x(a)/e_x(0)$, Gaussian of range $a$")
small = ranges[ranges < 0.6]
ax.semilogx(small, 1.0 - 0.6 * small ** 2, "--",
            label="small-range formula $1 - (3/5)(k_F a)^2$")
```

`ax.semilogx` draws like `plot`, but with a logarithmic horizontal axis, on which the 31 ranges from $10^{-2}$ to 10 are equally spaced. The black dots joined by a line are the computed ratios. `ranges[ranges < 0.6]` keeps only the ranges below $0.6$ (an array indexed by an array of true and false values keeps the entries where the value is true), and for them the dashed curve is the small-range formula $1 - \tfrac35(k_Fa)^2$; for larger ranges the formula is meaningless (it becomes negative beyond $k_Fa = 1.29$).

```python
ax.set_ylim(0.0, 1.05)
ax.set_xlabel("range times Fermi wave number, $k_F a$")
ax.set_ylabel("exchange energy relative to contact")
ax.set_title("A finite-range interaction shrinking to a contact")
ax.legend(fontsize=8)
save_figure(fig, "finite_range",
```

`set_ylim(0.0, 1.05)` fixes the vertical range from 0 to $1.05$; then the labels, the title, the legend and `save_figure` for Figure 13b.4.

**What Figure 13b.4 shows.** For ranges up to about $k_Fa = 0.1$ the ratio is indistinguishable from 1: the interaction acts as a contact, and its exchange energy is the local contact value. Between $0.1$ and 1 the ratio falls, first along the dashed parabola $1 - \tfrac35(k_Fa)^2$, then faster ($0.589$ at $k_Fa = 1$), and for $k_Fa = 10$ it is nearly 0: when the interaction reaches much farther than the exchange hole (size $1/k_F$), only a small part of it acts inside the hole, and the exchange energy almost disappears relative to the contact value.

**In [10], Dirac's exchange.**

```python
S_MAX = 4000.0
s_long = np.linspace(0.0, S_MAX, 4000001)
integral_9_4 = simpson(s_long * F(s_long) ** 2, s_long[1] - s_long[0])
integral_9_4 += 9.0 / (4.0 * S_MAX ** 2)  # the tail beyond S_MAX
report("integral of s F(s)^2 from 0 to infinity", f"{integral_9_4:.8f}")
check(abs(integral_9_4 - 2.25) < 1e-7, "the Coulomb exchange integral is 9/4")
```

$\int_0^{4000}sF(s)^2\,ds$ by Simpson's rule on 4000001 points (spacing $0.001$), plus the tail $9/(4\cdot4000^2)$ of Section 13.15 (`+=` adds to the variable). The result prints as $2.25000000$ and the check requires it to be within $10^{-7}$ of $9/4$.

```python
dirac = 0.75 * (3.0 / np.pi) ** (1.0 / 3.0)  # e_x = -dirac n^(4/3)
n_test = 0.3
kF_test = (3.0 * np.pi ** 2 * n_test) ** (1.0 / 3.0)  # g = 2
e_x_coulomb = -4.0 * np.pi * (n_test / 2) ** 2 / kF_test ** 2 * integral_9_4
report("Dirac's constant (3/4)(3/pi)^(1/3)", f"{dirac:.6f}")
check(abs(e_x_coulomb + dirac * n_test ** (4.0 / 3.0)) < 1e-8,
      "the Coulomb exchange of the electron gas is -(3/4)(3/pi)^(1/3) n^(4/3)")
```

Dirac's constant is $0.738559$. At the density $n = 0.3$ the cell evaluates $e_x = -4\pi n_\sigma^2\,I/k_F^2$ with $n_\sigma = n/2$ and the computed integral $I$, and checks that it equals $-0.738559\,n^{4/3}$.

**In [11], exchange per particle.**

```python
n_values = np.logspace(-3, 1, 41)
contact_per_particle = 0.25 * G_C * n_values  # |e_x / n| for the contact, g = 2
coulomb_per_particle = dirac * n_values ** (1.0 / 3.0)  # |e_x / n|, Coulomb
slope_contact = np.polyfit(np.log(n_values), np.log(contact_per_particle), 1)[0]
slope_coulomb = np.polyfit(np.log(n_values), np.log(coulomb_per_particle), 1)[0]
```

For 41 densities from $10^{-3}$ to 10, the sizes of the exchange energy per particle: $g_c n/4$ for the contact with two labels ($e_x/n = -\tfrac{g_c}{2\cdot2}n$) and $0.738559\,n^{1/3}$ for the Coulomb gas. `np.polyfit(X, Y, 1)` fits the straight line $Y = pX + c$ through the points, and `[0]` takes its slope $p$; with $X = \ln n$ and $Y$ the logarithm of a power $n^p$, the slope is the power.

```python
say(f"slopes: contact {slope_contact:.6f}, Coulomb {slope_coulomb:.6f}")
check(abs(slope_contact - 1.0) < 1e-12 and abs(slope_coulomb - 1.0 / 3.0) < 1e-12,
      "exchange per particle grows like n (contact) and n^(1/3) (Coulomb)")
```

The cell prints the slopes $1.000000$ and $0.333333$ and checks them to $10^{-12}$ (the points lie exactly on straight lines, so the fit is exact up to rounding).

```python
fig, ax = plt.subplots()
ax.loglog(n_values, contact_per_particle, label="contact, $g_c = 1$: $n/4$")
ax.loglog(n_values, coulomb_per_particle, "--",
          label="Coulomb (Dirac): $0.7386\\,n^{1/3}$")
ax.set_xlabel("density $n$")
ax.set_ylabel("$|e_x|/n$, exchange energy per particle")
ax.set_title("Exchange per particle: contact versus Coulomb ($g = 2$)")
ax.legend()
save_figure(fig, "contact_vs_coulomb",
```

`ax.loglog` draws with both axes logarithmic: the contact curve solid, the Coulomb curve dashed (in the label, `\\,` is a small space in the formula). Labels, title, legend and `save_figure` for Figure 13b.5.

**What Figure 13b.5 shows.** On logarithmic axes both curves are straight lines: the contact exchange per particle rises with slope 1 (ten times the density gives ten times the exchange per particle), the Coulomb exchange with slope $1/3$. The lines cross where $n/4 = 0.7386\,n^{1/3}$, at $n = (2.954)^{3/2} \approx 5.1$: below that density the Coulomb exchange per particle is the larger one, above it the contact exchange.

**In [12], exact locality for a non-uniform determinant.**

```python
P = 99  # interior grid points of the box 0 < x < 1
h = 1.0 / (P + 1)
x = h * np.arange(1, P + 1)
W = G_C * np.eye(P) / h  # the contact interaction on the grid


def box_orbitals(count):
    """The lowest box orbitals sqrt(2) sin(m pi x), m = 1..count, as columns."""
    return np.array([np.sqrt(2.0) * np.sin(m * np.pi * x)
                     for m in range(1, count + 1)]).T
```

A line $0 < x < 1$ with 99 grid points, spacing $h = 1/100$. On the grid the delta function is the unit matrix divided by $h$ (a sum over the grid times $h$ then gives back $g_c$). `box_orbitals(count)` returns the lowest orbitals of a particle in the box as the columns of a matrix (`.T` transposes the list of rows).

```python
phi_up, phi_down = box_orbitals(5), box_orbitals(3)
rho_up = phi_up @ phi_up.T  # rho_up(x, x') = sum_a phi_a(x) phi_a(x')
rho_down = phi_down @ phi_down.T
n_up, n_down = np.diag(rho_up), np.diag(rho_down)  # the label densities
fock = -0.5 * h * h * (np.sum(rho_up ** 2 * W) + np.sum(rho_down ** 2 * W))
local = -0.5 * G_C * h * np.sum(n_up ** 2 + n_down ** 2)
```

Five fermions with label up and three with label down. The matrix product of the orbital columns with their transpose is the density matrix of each label, $\rho(x, x') = \sum_a\phi_a(x)\phi_a(x')$, and its diagonal the label density. `fock` is the two-point exchange $-\tfrac12\sum_{x,x'}h^2|\rho_\sigma(x, x')|^2W(x, x')$ summed over the labels (`rho_up ** 2 * W` multiplies entry by entry); `local` is $-\tfrac{g_c}{2}\sum_x h\,(n_\uparrow^2 + n_\downarrow^2)$.

```python
report("exchange energy, two-point (Fock) form", f"{fock:.10f}")
report("exchange energy, local form", f"{local:.10f}")
check(abs(h * n_up.sum() - 5.0) < 1e-12 and abs(h * n_down.sum() - 3.0) < 1e-12,
      "the box determinant holds 5 up and 3 down fermions")
check(abs(fock - local) < 1e-12,
      "the contact exchange of a non-uniform determinant is exactly local")
```

Both forms print as $-19.0000000000$ (Exercise 10 derives this number by hand). The checks require the particle numbers $h\sum n_\uparrow = 5$ and $h\sum n_\downarrow = 3$ and the agreement of the two forms to $10^{-12}$. (On the grid the two forms are equal term by term, because $W$ is zero off the diagonal; the check confirms that the code implements both formulas correctly.)

**In [13], label-mixing orbitals.**

```python
rng = np.random.default_rng(12345)  # a fixed seed: the same numbers every run
raw = rng.normal(size=(2 * P, 5)) + 1j * rng.normal(size=(2 * P, 5))
q_matrix = np.linalg.qr(raw)[0]  # five orthonormal columns of length 2P
spinor = (q_matrix / np.sqrt(h)).reshape(P, 2, 5)  # [point, label, orbital]
```

Five random orthonormal complex columns of length $2 \times 99$ (the QR factorisation of a random matrix with a fixed seed), divided by $\sqrt h$ so that $\sum|\phi|^2h = 1$. `.reshape(P, 2, 5)` reads each column as 99 pairs of numbers: `spinor[x, s, a]` is the value of orbital $a$ at the point $x$ with the label $s$. Each orbital now has an up part and a down part.

```python
pair = np.einsum("xsa,xsb->xab", spinor.conj(), spinor)
exact = -0.5 * G_C * h * np.sum(np.abs(pair) ** 2)
rho_local = np.einsum("xsa,xta->xst", spinor, spinor.conj())
local_all = -0.5 * G_C * h * np.sum(np.abs(rho_local) ** 2)
diagonal = np.einsum("xss->xs", rho_local).real  # n_up(x), n_down(x)
local_diagonal = -0.5 * G_C * h * np.sum(diagonal ** 2)
```

`pair[x, a, b]` is $\sum_s\phi_a^*(x s)\,\phi_b(x s)$, and `exact` is the exact exchange $-\tfrac12\sum_{a,b}w_{abba}$ with $w_{abba} = g_c\sum_x h\,|\sum_s\phi_a^*\phi_b|^2$, which is the integral of Section 13.4 for a label-independent contact (put $w = g_c\,\delta$ into $w_{abba}$ and do the delta integral). `rho_local[x, s, t]` is the local $2 \times 2$ density matrix $\sum_a\phi_a(xs)\phi_a^*(xt)$, and `local_all` the local formula of Section 13.15 with all label pairs. `np.einsum("xss->xs", ...)` takes the diagonal of each $2 \times 2$ matrix (the label densities), and `local_diagonal` the local formula with the diagonal only.

```python
say(f"exact {exact:.10f}; local, all label pairs {local_all:.10f}; "
    f"local, label diagonal only {local_diagonal:.10f}")
check(abs(exact - local_all) < 1e-10,
      "with label-mixing orbitals the exchange is local in the 2 x 2 matrix rho")
check(abs(exact - local_diagonal) > 0.1,
      "the label diagonal alone misses the label-mixing exchange")
```

The cell prints $-8.7398756465$, $-8.7398756465$ and $-7.5021209026$ and checks that the first two agree to $10^{-10}$ and that the third differs from them by more than $0.1$ (it misses $1.2377547439$, the part of the exchange carried by the off-diagonal entries of the local $2 \times 2$ matrix).

**In [14], the two-point function and the local energies.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
image = left.imshow(rho_up ** 2, origin="lower", extent=(0, 1, 0, 1),
                    cmap="viridis")
left.plot([0, 1], [0, 1], "w--", lw=1.0)  # the diagonal x = x'
left.set_xlabel("$x$")
left.set_ylabel("$x'$")
left.set_title("$|\\rho_{up}(x, x')|^2$, 5 up fermions in a box")
fig.colorbar(image, ax=left, shrink=0.85)
```

On the left, `rho_up ** 2` (the square of every entry; the entries are real) is $|\rho_\uparrow(x, x')|^2$ of the box determinant, drawn as a heat map over the square $0 < x, x' < 1$; the style string (the letter w, for white, and two hyphens) draws the diagonal $x = x'$ as a white dashed line; axis labels, title and colour scale follow.

```python
right.plot(x, 0.5 * G_C * (n_up + n_down) ** 2, label="Hartree $g_c n^2/2$")
right.plot(x, -0.5 * G_C * (n_up ** 2 + n_down ** 2),
           label="exchange $-g_c(n_{up}^2 + n_{down}^2)/2$")
right.plot(x, G_C * n_up * n_down, color="black", lw=2.0,
           label="sum $g_c\\,n_{up} n_{down}$")
```

On the right, along the box: the local Hartree energy density $\tfrac{g_c}{2}(n_\uparrow + n_\downarrow)^2$, the local exchange energy density $-\tfrac{g_c}{2}(n_\uparrow^2 + n_\downarrow^2)$, and (thick black) the product $g_c\,n_\uparrow n_\downarrow$, which Section 13.5 showed to be their sum.

```python
right.set_ylim(-50.0, 60.0)  # room below the curves for the legend
right.set_xlabel("$x$")
right.set_ylabel("energy per length (units of $g_c$)")
right.legend(fontsize=7, loc="lower center")
save_figure(fig, "local_exchange",
```

`set_ylim(-50.0, 60.0)` fixes the vertical range so that the legend, placed at the bottom centre (`loc="lower center"`), does not cover the curves; labels and `save_figure` for Figure 13b.6. Then

```python
check(np.allclose(0.5 * (n_up + n_down) ** 2 - 0.5 * (n_up ** 2 + n_down ** 2),
                  n_up * n_down, atol=1e-12),
      "Hartree plus exchange of a contact is g_c n_up n_down at every point")
```

confirms point by point that the Hartree plus the exchange energy density equals $g_c\,n_\uparrow n_\downarrow$ (here $g_c = 1$).

**What Figure 13b.6 shows.** On the left, $|\rho_\uparrow(x, x')|^2$ is large only near the diagonal, with five bright spots along it (the density of five fermions has five bumps) and faint ripples away from it: the density matrix of a determinant falls off with the distance $|x - x'|$, just as $F(k_FR)$ does in the uniform gas. A contact interaction samples only the diagonal. On the right, the Hartree energy density (up to about 52) and the exchange energy density (down to about $-28$) both follow the bumps of the densities, and their sum, $n_\uparrow n_\downarrow$, is everywhere smaller than the Hartree part: exchange removes, point by point, the energy of the same-label pairs.

**In [15], polarisation.**

```python
C_F = 0.3 * (3.0 * np.pi ** 2) ** (2.0 / 3.0)
gamma_c = (2.0 / 3.0) * (3.0 * np.pi ** 2) ** (2.0 / 3.0)


def energy_polarized(zeta, coupling):
    """e(zeta) at n = 1 for g_c = coupling (exchange-only picture)."""
    kinetic_part = C_F * ((1 + zeta) ** (5 / 3) + (1 - zeta) ** (5 / 3)) / 2
    return kinetic_part + 0.25 * coupling * (1 - zeta ** 2)
```

The constants $C_F = \tfrac{3}{10}(3\pi^2)^{2/3}$ and $\gamma_c = \tfrac23(3\pi^2)^{2/3}$, and the energy $e(\zeta)$ of Section 13.15 at $n = 1$ (so $g_cn^{1/3} = g_c$, the argument `coupling`). The exponent `5 / 3` is written with whole numbers; in Python the division `/` always gives a floating-point number, $1.6666\ldots$.

```python
report("C_F", f"{C_F:.6f}")
report("threshold gamma_c = g_c n^(1/3)", f"{gamma_c:.6f}")
```

They print as $C_F = 2.871234$ and $\gamma_c = 6.380520$.

```python
d = 1e-3
curvature = [(energy_polarized(d, c) - 2 * energy_polarized(0.0, c)
              + energy_polarized(-d, c)) / d ** 2
             for c in (0.99 * gamma_c, 1.01 * gamma_c)]
check(curvature[0] > 0 > curvature[1],
      "the unpolarized gas becomes unstable at g_c n^(1/3) = (2/3)(3 pi^2)^(2/3)")
```

The second difference $(e(d) - 2e(0) + e(-d))/d^2$ approximates $e''(0)$ (Section 13.2). Just below the threshold ($0.99\gamma_c$) it must be positive, just above ($1.01\gamma_c$) negative; `curvature[0] > 0 > curvature[1]` tests both at once.

```python
zetas = np.linspace(-1.0, 1.0, 401)
fig, ax = plt.subplots()
for gamma in (0.5, 1.0, 1.1, 1.5):
    curve = energy_polarized(zetas, gamma * gamma_c) - energy_polarized(0.0,
                                                                     gamma * gamma_c)
    ax.plot(zetas, curve / C_F, label=f"$\\gamma = {gamma}$")
```

401 polarisations from $-1$ (all fermions down) to $1$ (all up). For the couplings $\gamma = 0.5, 1, 1.1, 1.5$ in units of the threshold ($g_c = \gamma\,\gamma_c$), `curve` is $e(\zeta) - e(0)$ (the statement continues on the next line inside the open parenthesis), and the loop draws it divided by $C_F$, that is in units of $C_Fn^{5/3}$ at $n = 1$.

```python
ax.axhline(0.0, color="gray", lw=0.8)
ax.set_xlabel("polarization $\\zeta = (n_{up} - n_{down})/n$")
ax.set_ylabel("$(e(\\zeta) - e(0)) / (C_F n^{5/3})$")
ax.set_title("Exchange favours unequal labels at strong contact repulsion")
ax.legend()
save_figure(fig, "polarization",
```

The zero line, axis labels, title, legend and `save_figure` for Figure 13b.7.

**What Figure 13b.7 shows.** For $\gamma = 0.5$ the curve is a bowl with its lowest point at $\zeta = 0$: equal labels are stable. For $\gamma = 1$ it is extremely flat near $\zeta = 0$ (the second derivative vanishes there) and still rises towards $\zeta = \pm1$. For $\gamma = 1.1$ the curve bends down at $\zeta = 0$, has shallow minima near $\zeta = \pm0.9$ and comes back up slightly at $\zeta = \pm1$. For $\gamma = 1.5$ it falls all the way to $\zeta = \pm1$: in this exchange-only picture the gas would rather put every fermion into one label.

**In [16], the gamma matrices, exactly.**

```python
import sympy as sp  # exact algebra with fractions and symbols

gamma_record = json.loads(repository_file("Revision/algebra/gammas.json")
                          .read_text(encoding="utf-8"))


def exact_matrix(rows):
    """A sympy matrix of exact fractions from the record's rows of numbers."""
    return sp.Matrix([[sp.Rational(str(entry)) for entry in row] for row in rows])
```

`sympy` computes with exact fractions and symbols. The Revision record `Revision/algebra/gammas.json` is read as text (`read_text`) and turned into Python lists and dictionaries by `json.loads`. `exact_matrix` turns a list of rows of numbers into a sympy matrix of exact fractions: `str(entry)` writes each number as text and `sp.Rational` reads that text as a fraction, so no rounding can occur.

```python
gamma = [exact_matrix(rows) for rows in gamma_record["gamma"]]  # x1 .. x8
C = gamma[7] * gamma[0] * gamma[1] * gamma[2]  # C = g(x8) g(x1) g(x2) g(x3)
B = -sp.I * C * gamma[3]  # B = -i C g(x4)
B_record = (exact_matrix(gamma_record["B"]["re"])
            + sp.I * exact_matrix(gamma_record["B"]["im"]))
check(C == exact_matrix(gamma_record["C"]) and B == B_record,
      "C and B built from the gammas equal the matrices of the record")
check(C * C == sp.eye(16) and B * B == sp.eye(16) and C == C.T,
      "C is symmetric with C^2 = 1, and B^2 = 1")
```

The record lists the eight gammas in the order $x_1, \dots, x_8$, so `gamma[7]` is $\gamma^{(x8)}$ and `gamma[3]` is $\gamma^{(x4)}$; for sympy matrices `*` is the matrix product and `sp.I` is $i$. The first check compares $C$ and $B$ with the matrices stored in the same record ($B$ is stored as its real and imaginary parts); the second checks exactly the facts $C^2 = 1$, $B^2 = 1$ and $C$ symmetric (`C.T` is the transpose) of Section 13.16.

**In [17], the exchange of the uniform gas, exactly.**

```python
n_sym, S_sym, lam = sp.symbols("n S lambda", real=True)
rho = (n_sym * B + S_sym * C) / 16
check(sp.simplify((B * rho).trace() - n_sym) == 0
      and sp.simplify((C * rho).trace() - S_sym) == 0,
      "Tr(B rho) = n and Tr(C rho) = S")
e_H = sp.expand(lam / 2 * (C * rho).trace() ** 2)
e_x = sp.expand(-lam / 2 * (C * rho * C * rho).trace())
say(f"e_H = {e_H}")
say(f"e_x = {e_x}")
```

Three real symbols $n$, $S$, $\lambda$; the matrix $\rho = (nB + SC)/16$; the check that the densities come back ($\mathrm{Tr}\,B\rho = n$, $\mathrm{Tr}\,C\rho = S$; `.trace()` is the trace and `sp.simplify` brings the difference to its simplest form, which must be 0). `e_H` and `e_x` are the Hartree and exchange formulas of Section 13.16, multiplied out by `sp.expand`; they print as `S**2*lambda/2` and `-S**2*lambda/32 - lambda*n**2/32`.

```python
theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                    .read_text(encoding="utf-8"))
gas = theory["exchange"]["uniformGas"]
coefficient_n2 = sp.Rational(gas["coefficient_n2"])  # "-1/32" in the record
coefficient_S2 = sp.Rational(gas["coefficient_S2"])
check(e_H == lam * S_sym ** 2 / 2, "the Hartree energy is (lambda/2) S^2")
recorded = lam * (coefficient_n2 * n_sym ** 2 + coefficient_S2 * S_sym ** 2)
check(sp.expand(e_x - recorded) == 0
      and coefficient_n2 == coefficient_S2 == sp.Rational(-1, 32),
      "e_x = -(lambda/32)(n^2 + S^2)",
      record="Revision/kohn_sham/reports/ks-theory-python.json, check "
             "exchange_uniform_gas")
```

The cell reads the Revision Kohn-Sham theory record and its two exchange coefficients, stored as the texts "-1/32", which `sp.Rational` reads as exact fractions. The checks: the Hartree energy is $\tfrac{\lambda}{2}S^2$, and the exchange energy computed here equals the recorded one, with both coefficients $-1/32$; the PASS line names the Revision check exchange_uniform_gas that it reproduces.

**In [18], the potentials and the solver's numbers.**

```python
e_int = e_H + e_x
mass_coefficient = sp.simplify(sp.diff(e_int, S_sym) / (lam * S_sym))  # 15/16
vector_coefficient = sp.simplify(sp.diff(e_int, n_sym) / (lam * n_sym))  # -1/16
filled_ratio = sp.simplify((e_x / e_H).subs(n_sym, S_sym))  # n = S
```

`sp.diff(e_int, S_sym)` is $\partial e_{int}/\partial S$; divided by $\lambda S$ it is the coefficient $15/16$ of $M_{eff} - m$; in the same way $\partial e_{int}/\partial n$ divided by $\lambda n$ gives $-1/16$. `.subs(n_sym, S_sym)` replaces $n$ by $S$ in $e_x/e_H$: the ratio of one filled level at rest, $-1/8$.

```python
say(f"M_eff = m + ({mass_coefficient}) lambda S;  v_v = ({vector_coefficient}) "
    f"lambda n;  E_x/E_H at n = S: {filled_ratio}")
```

The printed line shows all three exact fractions: M_eff = m + (15/16) lambda S; v_v = (-1/16) lambda n; E_x/E_H at n = S: -1/8.

```python
potentials = theory["exchange"]["kohnShamPotentials"]
check(mass_coefficient == sp.Rational(potentials["Meff_coefficient_of_lambda_S"])
      == sp.Rational(15, 16)
      and vector_coefficient == sp.Rational(potentials["vv_coefficient_of_lambda_n"])
      == sp.Rational(-1, 16),
      "M_eff = m + (15/16) lambda S and v_v = -(1/16) lambda n",
      record="Revision/kohn_sham/reports/ks-theory-python.json, check ks_potentials")
check(filled_ratio == sp.Rational(-1, 8),
      "one filled 8-fold level at rest: E_x/E_H = -1/8",
      record="Revision/kohn_sham/reports/ks-theory-python.json, check "
             "filled_shell_ratio")
```

The coefficients are compared with the record's texts "15/16" and "-1/16" (a chain `a == b == c` means `a == b and b == c`), and the ratio with $-1/8$; the PASS lines name the Revision checks ks_potentials and filled_shell_ratio.

```python
solver = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                    .read_text(encoding="utf-8"))["theoryInputs"]
check(solver["exchangeCoefficientN2"] == solver["exchangeCoefficientS2"] == -1 / 32
      and solver["MeffCoefficientOfLambdaS"] == 15 / 16
      and solver["vvCoefficientOfLambdaN"] == -1 / 16,
      "the Revision solver uses exactly these coefficients (parameters.json)")
```

The Revision solver's parameter file stores the coefficients it uses as floating-point numbers. The fractions $-1/32$, $15/16$ and $-1/16$ have denominators that are powers of 2, so they are stored exactly in binary, and the comparison with `==` is exact.

```python
report_checks = {c["name"]: c["verdict"] for c in json.loads(repository_file(
    "Revision/kohn_sham/reports/ks-theory-python.json").read_text(
    encoding="utf-8"))["checks"]}
check(all(report_checks[name] == "PASS" for name in
          ("exchange_uniform_gas", "ks_potentials", "filled_shell_ratio")),
      "the three Revision checks are recorded as PASS")
```

The last check reads the Revision report itself, makes a dictionary from check name to verdict, and requires the three checks reproduced above to be recorded as PASS.

**In [19], the matrices as pictures.**

```python
C_numbers = np.array(C.tolist(), dtype=float)
B_imaginary = np.array([[float(sp.im(entry)) for entry in row] for row in B.tolist()])
check(all(sp.re(entry) == 0 for entry in B), "B is purely imaginary")
check(all(np.count_nonzero(row) == 1 for row in np.vstack([C_numbers, B_imaginary])),
      "every row of C and of B has exactly one nonzero entry")
```

`C.tolist()` gives the rows of the sympy matrix, which numpy turns into floating-point numbers; `sp.im` takes the imaginary part of each entry of $B$. The checks: every real part of $B$ is 0, and every row of $C$ and of $B$ (stacked into one table by `np.vstack`) has exactly one nonzero entry.

```python
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.2))
for ax, matrix, title in ((axes[0], C_numbers, "$C$ (real)"),
                          (axes[1], B_imaginary, "imaginary part of $B$")):
    image = ax.imshow(matrix, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_title(title)
    ax.set_xlabel("column")
    ax.set_ylabel("row")
fig.colorbar(image, ax=axes, shrink=0.8)
save_figure(fig, "dirac_matrices",
```

The loop goes through two triples (panel, matrix, title): $C$ in the left panel and the imaginary part of $B$ in the right one, each drawn as a heat map on the fixed scale from $-1$ (blue) to $+1$ (red), with row 0 at the top; one colour scale for both, and `save_figure` for Figure 13b.8.

**What Figure 13b.8 shows.** Each matrix has exactly one coloured square in every row and every column: $C$ and $B$ only exchange and re-sign the 16 components. $C$ pairs the components 0 to 3 with 4 to 7 (entries $-1$) and 8 to 11 with 12 to 15 (entries $+1$); it is symmetric, as its picture is unchanged by a reflection in the main diagonal. The imaginary part of $B$ pairs the first eight components with the last eight, with signs $\pm1$; together with the factor $i$ this makes $B$ Hermitian.

**In [20], the exchange of the 8-fold gas as a picture.**

```python
ratio_values = np.linspace(0.0, 1.0, 101)  # S / n
e_H_curve = 0.5 * ratio_values ** 2  # e_H / (lambda n^2)
e_x_curve = -(1.0 + ratio_values ** 2) / 32.0  # e_x / (lambda n^2)
```

Dividing $e_H$ and $e_x$ by $\lambda n^2$ leaves functions of $S/n$ alone: $\tfrac12(S/n)^2$ and $-(1 + (S/n)^2)/32$, on 101 values of $S/n$ from 0 to 1.

```python
fig, ax = plt.subplots()
ax.plot(ratio_values, e_H_curve, label="Hartree $e_H = \\lambda S^2/2$")
ax.plot(ratio_values, e_x_curve, label="exchange $e_x = -\\lambda(n^2+S^2)/32$")
ax.plot(ratio_values, e_H_curve + e_x_curve, color="black", lw=2.0,
        label="$e_{int} = e_H + e_x$")
ax.plot([1.0], [-1.0 / 16.0], "o", color="red",
        label="filled level at rest: $e_x/e_H = -1/8$")
```

The two curves and their sum (thick black), and one red dot at $S/n = 1$, $e_x/(\lambda n^2) = -2/32 = -1/16$: the filled level at rest.

```python
ax.axhline(0.0, color="gray", lw=0.8)
ax.set_xlabel("$S/n$ (scalar density over number density)")
ax.set_ylabel("energy per volume / $(\\lambda n^2)$")
ax.set_title("Hartree and exchange of the uniform 8-fold dirac16complex gas")
ax.legend(fontsize=8)
save_figure(fig, "dirac_exchange",
```

The zero line, labels, title, legend and `save_figure` for Figure 13b.9 (the lines after it are the caption). Then

```python
check(abs(e_x_curve[-1] / e_H_curve[-1] + 1.0 / 8.0) < 1e-15,
      "the plotted curves give e_x/e_H = -1/8 at S = n")
```

checks that the plotted curves give $e_x/e_H = -1/8$ at $S = n$ (the last entries, `[-1]`).

**What Figure 13b.9 shows.** The Hartree energy grows from 0 at $S = 0$ to $\tfrac12$ at $S = n$. The exchange energy is never zero: it is $-1/32$ even at $S = 0$, because its $n^2$ term does not depend on $S$, and $-1/16$ at $S = n$ (the red dot). Their sum is slightly negative for small $S/n$ (below $S/n = \sqrt{1/15} \approx 0.26$, where $\tfrac{15}{32}S^2 = \tfrac{1}{32}n^2$) and reaches $7/16$ at $S = n$ (Exercise 9).

**In [21], the last check.**

```python
figure_names = ["density_matrix", "exchange_hole", "contact_energies",
                "finite_range", "contact_vs_coulomb", "local_exchange",
                "polarization", "dirac_matrices", "dirac_exchange"]
missing = [name for k, name in enumerate(figure_names, 1)
           if not output_file(f"{FIGURE_FOLDER}/13b_{k}_{name}.png").is_file()]
check(missing == [], "all nine figure files exist")
check(output_file(f"{FIGURE_FOLDER}/13b_9_dirac_exchange.png").is_file(),
      "the figure file 13b_9_dirac_exchange.png exists")
all_checks_passed()
```

The same lines as In [19] of Notebook 13c (Section 13.14), with the nine figure names of this notebook. The last line prints ALL 34 CHECKS PASSED (notebook 13b): one check in In [2] and In [3] each, three in In [5], four in In [6], two in In [8], In [10], In [12] and In [13] each, one in In [11], In [14] and In [15] each, two in In [16], three in In [17], four in In [18], two in In [19], one in In [20] and two in In [21].

### 13.21 Solving the Kohn-Sham equations: iteration and mixing

The loop of Section 13.10 is a map from an input density (or potential) to an output density, $n_{out} = G[n_{in}]$, and the self-consistent solution is a **fixed point** of this map, $G[n] = n$. The simplest loop, "the output becomes the next input" (**plain iteration**), often fails. This section shows why with a model small enough to follow by hand, and how the remedies work.

**The model.** Two sites L and R with the site energies $-\Delta/2$ and $+\Delta/2$, the hopping $t$ and the on-site repulsion $U$, and two electrons with opposite labels in the lowest orbital. In the mean field each electron feels $U$ times the density of the OTHER label on its site (the contact rule of Section 13.5: exchange removes the same-label half); with two electrons in the same orbital each label has the density $n_L/2$ on L and $n_R/2$ on R. So the one-electron Hamiltonian and the output density are

$$
h[n_L] = \begin{pmatrix} -\tfrac{\Delta}{2} + \tfrac{U}{2}n_L & -t \\ -t & \tfrac{\Delta}{2} + \tfrac{U}{2}n_R \end{pmatrix}, \qquad n_R = 2 - n_L, \qquad n_L^{out} = 2\,|c_L|^2 ,
$$

where $(c_L, c_R)$ is the normalised lowest eigenvector of $h[n_L]$.

**The lowest eigenvector of a real symmetric $2 \times 2$ matrix, in four steps.** Take $\begin{pmatrix} a & -t\\ -t & b\end{pmatrix}$ with $t > 0$, and write $\delta = b - a$ and $D = \sqrt{\delta^2 + 4t^2}$. (1) The eigenvalues solve $(a - \epsilon)(b - \epsilon) - t^2 = \epsilon^2 - (a + b)\epsilon + ab - t^2 = 0$, so $\epsilon = \tfrac12(a + b) \pm \tfrac12\sqrt{(a + b)^2 - 4ab + 4t^2} = \tfrac12(a + b) \pm \tfrac12 D$, because $(a + b)^2 - 4ab = (b - a)^2$; the lowest is $\epsilon = \tfrac12(a + b) - \tfrac12 D$. (2) The first row of $(h - \epsilon)c = 0$ reads $(a - \epsilon)c_L - t\,c_R = 0$; since $a - \epsilon = \tfrac12(a - b) + \tfrac12 D = \tfrac12(D - \delta)$, the ratio of the components is $r = c_R/c_L = (D - \delta)/(2t)$. (3) From $D^2 - \delta^2 = 4t^2$, that is $4t^2 = (D - \delta)(D + \delta)$, we get $r^2 = (D - \delta)^2/\big((D - \delta)(D + \delta)\big) = (D - \delta)/(D + \delta)$. (4) The normalisation $|c_L|^2(1 + r^2) = 1$ gives

$$
|c_L|^2 = \frac{1}{1 + r^2} = \frac{D + \delta}{2D} = \frac12\Big(1 + \frac{b - a}{\sqrt{(b - a)^2 + 4t^2}}\Big) .
$$

**The reduced map.** Here, line by line,

$$
\begin{aligned}
b - a &= \Big(\tfrac{\Delta}{2} + \tfrac{U}{2}(2 - n_L)\Big) - \Big(-\tfrac{\Delta}{2} + \tfrac{U}{2}n_L\Big) = \Delta + U(1 - n_L) ,\\
n_L^{out} - 1 &= 2|c_L|^2 - 1 = \frac{b - a}{\sqrt{(b - a)^2 + 4t^2}} .
\end{aligned}
$$

The first line subtracts the two diagonal entries and collects; the second inserts the result of step (4). With $x = n_L - 1$ (the excess of charge on L) we have $b - a = \Delta - Ux$, and the whole loop becomes one function of one number:

$$
x_{out} = G(x) = \frac{\Delta - Ux}{\sqrt{(\Delta - Ux)^2 + 4t^2}} .
$$

**Numbers.** Take $\Delta = 2$, $t = 1$, $U = 4$ (energies in units of $t$) and the start $n_L = 2$ (both electrons on the low site). Plain iteration gives (Notebook 13d, In [5])

| step | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| $n_L$ in | 2.000000 | 0.292893 | 1.923880 | 0.353344 | 1.916644 | 0.359836 |
| $n_L$ out | 0.292893 | 1.923880 | 0.353344 | 1.916644 | 0.359836 | 1.915809 |

and continues to jump between about $0.3607$ and $1.9157$ forever: when the electrons sit on L, the repulsion pushes them to R, and when they sit on R, it pushes them back. This is called **charge sloshing**. **Linear mixing** feeds back only a fraction $\beta$ of the change, $n_L \leftarrow (1 - \beta)\,n_L + \beta\,n_L^{out}$ (so $\beta = 1$ is plain iteration). With $\beta = \tfrac12$ (Notebook 13d, In [6]):

| step | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| $n_L$ in | 2.000000 | 1.146447 | 1.361898 | 1.314066 | 1.331307 | 1.325494 |
| $n_L$ out | 0.292893 | 1.577350 | 1.266234 | 1.348548 | 1.319682 | 1.329519 |

The iteration converges to the self-consistent value $n_L^* = 1.326993$; input and output agree to $10^{-6}$ from step 13 on.

**Why, line by line.** Near the fixed point $x^*$ write $x = x^* + e$ with a small error $e$. To first order (the tangent line), $G(x^* + e) = x^* + G'(x^*)\,e$. One step of linear mixing then gives

$$
x^* + e_{new} = (1 - \beta)(x^* + e) + \beta\,\big(x^* + G'(x^*)\,e\big) \quad\Longrightarrow\quad e_{new} = \big[1 - \beta\,(1 - G'(x^*))\big]\,e ,
$$

where the left equation is the mixing rule with the tangent line inserted, and the right one subtracts $x^* = (1 - \beta)x^* + \beta x^*$ from both sides and collects the terms with $e$. So every step multiplies the error by the **convergence factor** $1 - \beta(1 - G')$, and the loop converges (for small errors) exactly when this number lies between $-1$ and $1$. The slope follows from the chain rule: with $u = \Delta - Ux$, $G = u\,(u^2 + 4t^2)^{-1/2}$ has $dG/du = (u^2 + 4t^2)^{-1/2} - u^2(u^2 + 4t^2)^{-3/2} = 4t^2(u^2 + 4t^2)^{-3/2}$, and $du/dx = -U$, so

$$
G'(x) = -\frac{4Ut^2}{\big((\Delta - Ux)^2 + 4t^2\big)^{3/2}} .
$$

Since $G' < 0$, the number $1 - G'$ is larger than 1, and the condition $-1 < 1 - \beta(1 - G') < 1$ reads $0 < \beta(1 - G') < 2$, that is

$$
0 < \beta < \beta_{max} = \frac{2}{1 - G'(x^*)} .
$$

With the numbers above, $x^* = 0.326993$ and $G'(x^*) = -1.687961$ (found by bisection in Notebook 13d, In [3]), so $\beta_{max} = 0.744058$. Plain iteration ($\beta = 1$) multiplies the error by $1 - 2.687961 = -1.688$: the error grows and changes its sign at every step, which is the sloshing, until the curvature of $G$ (left out by the tangent line) stops the growth on a cycle of period 2. With $\beta = \tfrac12$ the factor is $-0.344$, and the error shrinks by about a factor 3 per step, as the table shows. The choice $\beta = 1/(1 - G') = 0.372029$ makes the factor zero. The stronger the repulsion, the steeper $G$ and the smaller the step the loop may take: for $U = 2$, $G' = -0.688942$ and $\beta_{max} = 1.184174$, so even plain iteration converges, and plain iteration stops converging at the repulsion where $G'(x^*) = -1$, which Notebook 13d (In [12]) finds to be $U = 2.647393$ for $\Delta = 2$, $t = 1$. All these numbers are COMPUTED by Notebook 13d; the linear analysis that explains them is PROVED above for small errors.

**Anderson mixing.** For densities with many components the best $\beta$ differs from direction to direction, and it is not known in advance. **Anderson mixing** remembers the last few inputs $w^{(i)}$ and their residuals $R^{(i)} = G[w^{(i)}] - w^{(i)}$, finds numbers $c_i$ with $\sum_i c_i = 1$ that make the combined residual $\sum_i c_i R^{(i)}$ as small as possible, and takes as the next input $\sum_i c_i\,(w^{(i)} + \beta R^{(i)})$. The condition $\sum_i c_i = 1$ is built in by writing $c_i = \theta_i$ for the older passes and $c_{last} = 1 - \sum_i\theta_i$; then

$$
\sum_i c_i R^{(i)} = R^{(last)} + \sum_i \theta_i\,\big(R^{(i)} - R^{(last)}\big) ,
$$

which is smallest (in the sense of the sum of the squares of its entries) for the **least-squares** solution $\theta$ of $\sum_i\theta_i(R^{(i)} - R^{(last)}) \approx -R^{(last)}$, a standard problem of linear algebra that numpy's `lstsq` solves. For one variable and two remembered passes the combined residual can be made exactly zero, and the next input is the point where the straight line through the two last (input, residual) pairs crosses zero: the **secant method**, which estimates the slope of $G$ from the history. Anderson mixing is therefore a cheap substitute for Newton's method, and it needs no tuning of $\beta$.

**The Revision solver.** The Revision Kohn-Sham solver of the dirac16complex field (Chapter 15) uses Anderson mixing with these settings, recorded in `Revision/kohn_sham/results/parameters.json` (numerics): it remembers 6 passes (andersonDepth), uses $\beta = 0.4$ (andersonBeta), and stops when the largest difference between the potentials that come out and those that went in is at most $10^{-11}$ (scfTolerance), with at most 400 passes. What it mixes is the list of its potentials at every grid point of the hidden direction (the mass shift $M_{eff} - m$, the potential $v_v$, and a third potential used only by one variant). It solves the same least-squares problem in an equivalent form (with a Lagrange multiplier for $\sum_i c_i = 1$) and adds two safeguards: a tiny number ($10^{-12}$ times the largest diagonal entry) on the diagonal of its equations, which keeps them solvable, and a restart of the remembered passes whenever the residual grows to more than ten times the best one so far (`Revision/kohn_sham/solver/src/scf.rs`). Notebooks 13d and 13a read these settings from the parameter file and use them in their own small loops.

**Level crossings and smearing.** With whole-number occupations (aufbau), the output density jumps whenever two levels near the highest occupied one exchange their order during the iteration; if they cross back and forth, the loop never settles, whatever $\beta$ is. The remedy replaces the whole-number occupations by smooth Fermi-Dirac occupations (Section 13.26); the converged object is then an ensemble with fractional occupations near the highest level, not a single determinant.

### 13.22 Example: charge sloshing

Notebook 13d computes everything of Section 13.21 for the two-site model: it checks the reduced map against a direct diagonalisation, reproduces the two tables, finds the fixed point, the slope and the largest mixing parameter, compares the error histories of plain iteration, linear mixing and Anderson mixing with the Revision solver's settings (read from the parameter file), maps the long-run behaviour against $\beta$ and the threshold against $U$. Its numbers are COMPUTED and exact up to rounding; the model shows the mechanism and is not a physical system of the book. It ends with ALL 17 CHECKS PASSED (notebook 13d) and draws six figures.

<!-- NOTEBOOK 13d -->

### 13.25 Line-by-line walk-through of Notebook 13d

The notebook has fourteen code cells. **In [1]** is the set-up cell, identical to In [1] of Notebook 13c (Section 13.14) except for the name `"13d"` and its comment lines, which hold the instructions of Section 13.23.

**In [2], the loop and the reduced map.**

```python
import numpy as np  # arrays, matrices and linear algebra

DELTA, T_HOP, U = 2.0, 1.0, 4.0  # site-energy difference, hopping, repulsion


def loop_pass(n_left, delta=DELTA, t=T_HOP, u=U):
    """One pass: the output density n_L of the lowest orbital of h[n_L]."""
    n_right = 2.0 - n_left
    h = np.array([[-delta / 2 + u * n_left / 2, -t],
                  [-t, delta / 2 + u * n_right / 2]])
    values, vectors = np.linalg.eigh(h)  # levels in increasing order
    return 2.0 * vectors[0, 0] ** 2  # two electrons, |c_L|^2 each
```

The cell loads numpy as `np`. The model's numbers $\Delta = 2$, $t = 1$, $U = 4$ are written in one line: Python assigns the three values to the three names in order. `loop_pass` is one pass of the loop: it builds the matrix $h[n_L]$ of Section 13.21, diagonalises it with `eigh` (levels in increasing order, eigenvectors as columns), and returns $2|c_L|^2$, where `vectors[0, 0]` is the L component (row 0) of the lowest eigenvector (column 0). The arguments `delta=DELTA` and so on are **default values**: they are used when the call does not give them, so later cells can call `loop_pass(n, u=2.0)` with another repulsion.

```python
def G(x, delta=DELTA, t=T_HOP, u=U):
    """The reduced map x_out = G(x), x = n_L - 1."""
    shift = delta - u * x
    return shift / np.sqrt(shift ** 2 + 4.0 * t * t)


inputs = np.linspace(0.0, 2.0, 41)
worst = max(abs(loop_pass(n) - 1.0 - G(n - 1.0)) for n in inputs)
check(worst < 1e-12, "the 2 x 2 diagonalisation and the reduced map G agree")
```

`G` is the closed form of Section 13.21. For 41 inputs from 0 to 2 the cell compares $n_L^{out} - 1$ from the diagonalisation with $G(n_L - 1)$ and checks that the largest difference is below $10^{-12}$: the four-step derivation is confirmed.

**In [3], the fixed point and the slope.**

```python
def fixed_point(delta=DELTA, t=T_HOP, u=U):
    """x* with G(x*) = x*, by bisection on [-1, 1] (x - G(x) increases)."""
    low, high = -1.0, 1.0
    for _ in range(80):
        middle = 0.5 * (low + high)
        if middle - G(middle, delta, t, u) > 0.0:
            high = middle
        else:
            low = middle
    return 0.5 * (low + high)


def slope(x, delta=DELTA, t=T_HOP, u=U):
    """G'(x) = -4 U t^2 / ((Delta - U x)^2 + 4 t^2)^(3/2)."""
    return -4.0 * u * t * t / ((delta - u * x) ** 2 + 4.0 * t * t) ** 1.5
```

`fixed_point` finds $x^*$ by bisection: $x - G(x)$ increases with $x$ (because $G$ decreases), is negative at $x = -1$ and positive at $x = 1$; at each of 80 steps the cell evaluates it at the middle of the interval and keeps the half in which the sign changes. After 80 halvings the interval is far below the rounding of the computer. `slope` is the formula for $G'$ of Section 13.21.

```python
x_star = fixed_point()
g_prime = slope(x_star)
quotient = (G(x_star + 1e-6) - G(x_star - 1e-6)) / 2e-6
beta_max, beta_best = 2.0 / (1.0 - g_prime), 1.0 / (1.0 - g_prime)
```

The fixed point, the slope there, a central difference quotient $(G(x^* + 10^{-6}) - G(x^* - 10^{-6}))/(2\cdot10^{-6})$ as an independent estimate of the slope, and the largest and the best mixing parameters (two names assigned in one line).

```python
report("fixed point n_L* = 1 + x*", f"{1.0 + x_star:.6f}")
report("slope G'(x*)", f"{g_prime:.6f}")
report("largest mixing parameter 2/(1 - G')", f"{beta_max:.6f}")
report("best mixing parameter 1/(1 - G')", f"{beta_best:.6f}")
check(abs(x_star - 0.326993) < 1e-6 and abs(g_prime + 1.687961) < 1e-6
      and abs(beta_max - 0.744058) < 1e-6,
      "x* = 0.326993, G'(x*) = -1.687961, beta_max = 0.744058")
check(abs(quotient - g_prime) < 1e-6, "the slope formula equals a difference quotient")
```

The four `report` lines print $n_L^* = 1.326993$, $G' = -1.687961$, $\beta_{max} = 0.744058$ and $\beta_{best} = 0.372029$; the two checks compare the first three with these values (to $10^{-6}$) and the slope formula with the difference quotient (to $10^{-6}$; the central quotient has an error of order $(10^{-6})^2$ times the third derivative, plus rounding).

**In [4], the map as a picture.**

```python
n_in = np.linspace(0.0, 2.0, 401)
fig, ax = plt.subplots(figsize=(6.0, 5.0))
ax.plot(n_in, 1.0 + G(n_in - 1.0), color="black", lw=2.0,
        label="$n_L^{out} = 1 + G(n_L - 1)$")
ax.plot(n_in, n_in, "--", color="gray", label="diagonal $n_L^{out} = n_L$")
ax.plot([1.0 + x_star], [1.0 + x_star], "ro",
        label=f"fixed point $n_L^* = {1.0 + x_star:.6f}$")
```

`n_in` holds 401 input densities from 0 to 2. The cell draws the output $1 + G(n_L - 1)$ against the input as a thick black line, the diagonal $n_L^{out} = n_L$ grey and dashed, and the fixed point as a red dot (`"ro"`: r red, o a round marker) at $(n_L^*, n_L^*)$, whose value the legend shows with six decimals.

```python
ax.set_xlabel("input density on the left site $n_L$")
ax.set_ylabel("output density $n_L^{out}$")
ax.set_title("The self-consistency map of the two-site model")
ax.legend(fontsize=8)
save_figure(fig, "reduced_map",
```

Labels, title, legend and `save_figure` for Figure 13d.1.

**What Figure 13d.1 shows.** The map falls from the output $1.95$ at the input $n_L = 0$ to the output $0.29$ at the input $n_L = 2$: the more charge the input puts on the left site, the more the repulsion pushes the output to the right. Where the curve crosses the diagonal, input and output agree: the self-consistent density $1.326993$. The crossing is steep (slope $-1.69$), which is the cause of all the trouble of Section 13.21.

**In [5], plain iteration.**

```python
def iterate(beta, start=2.0, passes=6):
    """Inputs and outputs of the loop with linear mixing (beta = 1: plain)."""
    n, history = start, []
    for _ in range(passes):
        out = loop_pass(n)
        history.append((n, out))
        n = (1.0 - beta) * n + beta * out
    return history, n
```

`iterate` runs the loop with linear mixing: at each pass it computes the output, stores the pair (input, output) in the list `history` (a pair in parentheses is a **tuple**), and forms the next input $(1 - \beta)n + \beta\,n^{out}$. It returns the history and the next input.

```python
plain, _ = iterate(1.0)
say("step   n_L in     n_L out")
for step, (n, out) in enumerate(plain):
    say(f"{step:4d}   {n:.6f}   {out:.6f}")
expected_in = [2.000000, 0.292893, 1.923880, 0.353344, 1.916644, 0.359836]
check(all(abs(n - e) < 1e-6 for (n, _), e in zip(plain, expected_in)),
      "plain iteration reproduces the table 2.000000, 0.292893, 1.923880, ...")
```

Six passes of plain iteration ($\beta = 1$); the name `_` receives the second returned value, which is not needed. The loop prints the table of Section 13.21 (`{step:4d}` writes the step number in four places, `{n:.6f}` the density with six decimals), and the check compares the inputs with the six values of that table.

```python
_, late = iterate(1.0, passes=2000)
cycle = sorted([late, loop_pass(late)])
say(f"after 2000 passes the input alternates between {cycle[0]:.4f} and "
    f"{cycle[1]:.4f}")
check(abs(loop_pass(loop_pass(late)) - late) < 1e-10 and cycle[1] - cycle[0] > 1.5,
      "plain iteration ends in a cycle of period 2 (about 0.3607 and 1.9157)")
```

After 2000 passes, `late` is the next input; with its output it forms the two values of the cycle, sorted. The check requires that two passes return to the same value (a cycle of period 2, to $10^{-10}$) and that the two values are more than $1.5$ apart: the charge keeps jumping between the sites.

**In [6], linear mixing with $\beta = 1/2$.**

```python
mixed, _ = iterate(0.5)
say("step   n_L in     n_L out")
for step, (n, out) in enumerate(mixed):
    say(f"{step:4d}   {n:.6f}   {out:.6f}")
expected_in = [2.000000, 1.146447, 1.361898, 1.314066, 1.331307, 1.325494]
check(all(abs(n - e) < 1e-6 for (n, _), e in zip(mixed, expected_in)),
      "linear mixing with beta = 1/2 reproduces the table 2.000000, 1.146447, ...")
long_history, _ = iterate(0.5, passes=40)
agree = next(step for step, (n, out) in enumerate(long_history)
             if abs(n - out) < 1e-6)
report("passes until input and output agree to 1e-6 (beta = 1/2)", agree)
check(agree == 13 and abs(long_history[-1][0] - 1.326993) < 1e-6,
      "beta = 1/2 converges to 1.326993; input and output agree after 13 passes")
```

The same for $\beta = \tfrac12$: the second table of Section 13.21 and its check. Then 40 passes; `next(...)` returns the first step number whose input and output agree to $10^{-6}$, which is 13; the last check also requires the last input (`long_history[-1][0]`, the first element of the last pair) to be $1.326993$.

**In [7], cobweb diagrams.**

```python
def cobweb(ax, beta, passes):
    """Draw the cobweb of the loop with mixing beta on the axes ax."""
    ax.plot(n_in, 1.0 + G(n_in - 1.0), color="black", lw=1.5)
    ax.plot(n_in, n_in, "--", color="gray", lw=0.8)
    history, _ = iterate(beta, passes=passes)
    for n, out in history:
        n_next = (1.0 - beta) * n + beta * out
        ax.plot([n, n], [n, out], color="tab:red", lw=0.8)  # up to the curve
        ax.plot([n, n_next], [out, n_next], color="tab:blue", lw=0.8)  # across
    ax.plot([1.0 + x_star], [1.0 + x_star], "ko")
    ax.set_xlabel("input $n_L$")
    ax.set_ylabel("output $n_L^{out}$ and next input")
```

A **cobweb diagram** draws an iteration: from the point (input, input) on the diagonal a red segment goes vertically to the curve (the output), and a blue segment goes from there to the point (next input, next input) on the diagonal. The function draws the map and the diagonal, runs the loop, and draws the two segments of every pass (`[n, n]` and `[n, out]` are the horizontal and the vertical coordinates of the two ends of the red segment), the fixed point as a black dot (`"ko"`), and labels the axes.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.5))
cobweb(left, 1.0, 12)
left.set_title("plain iteration ($\\beta = 1$): sloshing")
cobweb(right, 0.5, 12)
right.set_title("linear mixing ($\\beta = 1/2$): converges")
save_figure(fig, "cobwebs",
```

The cell calls `cobweb` for plain iteration in the left panel and for $\beta = \tfrac12$ in the right panel, 12 passes each, gives each panel its title, and saves Figure 13d.2.

**What Figure 13d.2 shows.** On the left the path starts at $n_L = 2$, goes down to the output $0.29$, across to the input $0.29$, up to the output $1.92$, and so on: after a few passes it runs around the same rectangle with the corners near $0.36$ and $1.92$, far from the fixed point in the middle; the thick lines are the many passes drawn on top of each other. On the right each blue segment ends on the diagonal at the point halfway between the input and the output, and the path closes in on the fixed point within a few passes, in a spiral, because the error changes its sign at every pass (the factor $-0.344$).

**In [8], error histories and Anderson mixing.**

```python
parameters = json.loads(repository_file(
    "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
DEPTH = int(parameters["numerics"]["andersonDepth"])  # passes remembered
BETA_ANDERSON = float(parameters["numerics"]["andersonBeta"])  # mixing parameter
check(DEPTH == 6 and BETA_ANDERSON == 0.4,
      "the Revision solver mixes with depth 6 and beta 0.4 "
      "(Revision/kohn_sham/results/parameters.json, numerics)")
```

The cell reads the parameter file of the Revision solver and takes from its part "numerics" the number of remembered passes and $\beta$; `int` and `float` make a whole number and a floating-point number of them. The check confirms the values 6 and $0.4$.

```python
def errors_linear(beta, passes=60):
    """|n_L - n_L*| of the inputs of linear mixing."""
    history, _ = iterate(beta, passes=passes)
    return np.array([abs(n - 1.0 - x_star) for n, _ in history])
```

The distance of every input of 60 passes of linear mixing from the fixed point $n_L^* = 1 + x^*$.

```python
def errors_anderson(beta=BETA_ANDERSON, depth=DEPTH, passes=60, tolerance=1e-14):
    """|n_L - n_L*| of the inputs of Anderson mixing (one variable)."""
    n, inputs, residuals, errors = 2.0, [], [], []
    for _ in range(passes):
        errors.append(abs(n - 1.0 - x_star))
        residual = loop_pass(n) - n
        if abs(residual) < tolerance:
            break
        inputs, residuals = (inputs + [n])[-depth:], (residuals + [residual])[-depth:]
        if len(inputs) == 1:
            n = n + beta * residual
            continue
        last = residuals[-1]
        differences = np.array([[r - last for r in residuals[:-1]]])  # 1 row
        theta = np.linalg.lstsq(differences, -np.array([last]), rcond=None)[0]
        c = np.append(theta, 1.0 - theta.sum())
        n = float(sum(ci * (ni + beta * ri)
                      for ci, ni, ri in zip(c, inputs, residuals)))
    return np.array(errors)
```

Anderson mixing of Section 13.21 for one variable. Each pass records the error, computes the residual $R = n^{out} - n$ and stops (`break` leaves the loop) when it is below $10^{-14}$. `(inputs + [n])[-depth:]` appends the new input and keeps the last `depth` entries (a negative index counts from the end). In the first pass there is no history, so the step is linear mixing; `continue` goes on to the next pass. Otherwise `differences` is the table with one row of the differences $R^{(i)} - R^{(last)}$, `np.linalg.lstsq` solves the least-squares problem for $\theta$ (with one equation and several unknowns it returns the solution with the smallest $\sum\theta_i^2$), `np.append` adds $c_{last} = 1 - \sum\theta_i$, and the next input is $\sum_i c_i(n^{(i)} + \beta R^{(i)})$.

```python
histories = {beta: errors_linear(beta) for beta in (1.0, 0.8, 0.5, 0.2)}
histories["best"] = errors_linear(beta_best)
anderson_errors = errors_anderson()
ratio = histories[0.5][11] / histories[0.5][10]  # the ratio of two error sizes
predicted = 1.0 - 0.5 * (1.0 - g_prime)
```

The error histories for $\beta = 1, 0.8, 0.5, 0.2$ and for $\beta_{best}$, and that of Anderson mixing. `ratio` divides the error after pass 11 by the error after pass 10 for $\beta = \tfrac12$, and `predicted` is the factor $1 - \beta(1 - G')$ of Section 13.21.

```python
report("measured |error ratio| for beta = 1/2", f"{ratio:.6f}")
report("predicted factor 1 - beta (1 - G')", f"{predicted:.6f}")
```

They print as $0.343986$ and $-0.343980$: the size agrees (the sign of the measured ratio is lost because errors are taken as absolute values, and the small difference is the curvature of $G$).

```python
check(abs(ratio - abs(predicted)) < 1e-4,
      "the error shrinks by the predicted factor |1 - beta(1 - G')| = 0.344")
check(histories[1.0][-1] > 0.5 and histories[0.8][-1] > 0.1,
      "beta = 1 and beta = 0.8 (above 0.744) do not converge")
check(len(anderson_errors) < 15 and anderson_errors[-1] < 1e-12,
      "Anderson mixing converges to 1e-12 in fewer than 15 passes")
```

Three checks: the predicted factor; the failure of $\beta = 1$ and $\beta = 0.8$, both above $\beta_{max}$ (their last errors are still large); and the convergence of Anderson mixing to $10^{-12}$ in fewer than 15 passes.

**In [9], the error histories as a picture.**

```python
fig, ax = plt.subplots()
for key, style in ((1.0, "o-"), (0.8, "s-"), (0.5, "^-"), (0.2, "v-")):
    label = "plain iteration" if key == 1.0 else f"linear, $\\beta = {key}$"
    ax.semilogy(histories[key][:40], style, ms=3, label=label)
```

`ax.semilogy` draws with a logarithmic vertical axis; given only one list, it uses the pass numbers $0, 1, 2, \dots$ as horizontal coordinates. For the four linear runs the loop draws the first 40 errors with its own marker (circles, squares, and triangles pointing up and down, each joined by a line); the label is "plain iteration" for $\beta = 1$ and otherwise names $\beta$ (`a if condition else b` chooses).

```python
best = np.maximum(histories["best"][:12], 1e-16)  # rounding may give exactly 0
ax.semilogy(best, "D-", ms=3, label=f"linear, best $\\beta = {beta_best:.3f}$")
ax.semilogy(anderson_errors, "k*-", ms=6,
            label=f"Anderson, depth {DEPTH}, $\\beta = {BETA_ANDERSON}$")
```

The first 12 errors of the best linear mixing, with diamonds (`"D-"`); `np.maximum(..., 1e-16)` replaces an error of exactly 0, which a logarithmic axis cannot show, by $10^{-16}$. Then all errors of Anderson mixing as black stars joined by a line (`"k*-"`); the label shows the depth and $\beta$ read from the Revision parameter file.

```python
ax.set_ylim(1e-15, 10.0)
ax.set_xlabel("pass number")
ax.set_ylabel("error $|n_L - n_L^*|$")
ax.set_title("Error histories of the two-site loop")
ax.legend(fontsize=7, loc="upper right", bbox_to_anchor=(1.0, 0.86))
save_figure(fig, "error_histories",
```

`set_ylim(1e-15, 10.0)` fixes the vertical range from $10^{-15}$ to 10; labels and title; the legend is anchored with its upper right corner at 86 per cent of the height of the panel (`bbox_to_anchor=(1.0, 0.86)`), a little below the top, so that it does not cover the two upper curves. `save_figure` saves Figure 13d.3.

**What Figure 13d.3 shows.** Plain iteration and $\beta = 0.8$ stay between about $0.2$ and 1 for all 40 passes, zig-zagging: they never converge. The runs with $\beta = 0.5$ and $0.2$ are straight falling lines on the logarithmic axis, which means that the error is multiplied by the same factor at every pass ($0.344$ and about $0.46$); the first reaches $10^{-15}$ after about 31 passes, the second is near $10^{-13}$ after 40. The best $\beta = 0.372$ (factor zero for small errors) and Anderson mixing fall much faster, reaching rounding level within about 5 and 9 passes; Anderson mixing achieves this without knowing the slope $G'$ in advance.

**In [10], the convergence factor.**

```python
betas = np.linspace(0.0, 1.0, 501)
factor = np.abs(1.0 - betas * (1.0 - g_prime))
```

The size of the factor $|1 - \beta(1 - G')|$ for 501 values of $\beta$ from 0 to 1.

```python
fig, ax = plt.subplots()
ax.plot(betas, factor, color="black", lw=2.0, label="$|1 - \\beta(1 - G')|$")
ax.axhline(1.0, color="gray", ls="--")
ax.axvspan(0.0, beta_max, alpha=0.15, color="green", label="converges")
ax.axvline(beta_best, color="tab:blue", ls=":",
           label=f"best $\\beta = {beta_best:.3f}$")
```

The factor as a thick black line; the grey dashed line at 1; `axvspan(0.0, beta_max, ...)` colours the vertical band $0 < \beta < \beta_{max}$, where the loop converges, in a pale green (`alpha=0.15` makes it 85 per cent transparent); `axvline` draws a dotted vertical line at $\beta_{best}$.

```python
ax.set_xlabel("mixing parameter $\\beta$")
ax.set_ylabel("error factor per pass")
ax.set_title(f"Linear mixing converges for $\\beta < {beta_max:.4f}$")
ax.legend()
save_figure(fig, "convergence_factor",
```

Labels; the title shows $\beta_{max}$ with four decimals ($0.7441$); legend; `save_figure` for Figure 13d.4.

**What Figure 13d.4 shows.** A V-shaped curve: the factor falls from 1 at $\beta = 0$ (no change at all, so no progress) to 0 at $\beta_{best} = 0.372$, rises again, crosses 1 at $\beta_{max} = 0.744$ (the right edge of the green band) and reaches $1.688$ at $\beta = 1$. Every $\beta$ inside the band converges; the closer to $\beta_{best}$, the faster.

**In [11], the long run against $\beta$.**

```python
beta_scan = np.linspace(0.02, 1.0, 99)
tails = []
for beta in beta_scan:
    history, _ = iterate(beta, passes=600)
    tails.append([n for n, _ in history[-30:]])
tails = np.array(tails)
spread = tails.max(axis=1) - tails.min(axis=1)
check(np.all(spread[beta_scan < 0.72] < 1e-8) and np.all(spread[beta_scan > 0.77]
                                                        > 0.05),
      "the loop converges below beta = 0.744 and oscillates above it")
```

For 99 values of $\beta$ from $0.02$ to 1 the cell runs 600 passes and keeps the last 30 inputs (`history[-30:]`); `tails` becomes a table with one row per $\beta$. The spread of each row (largest minus smallest) is tiny where the loop converged and large where it ends in a cycle. The check requires a spread below $10^{-8}$ for every $\beta < 0.72$ and above $0.05$ for every $\beta > 0.77$ (close to $\beta_{max}$ the convergence or divergence is too slow to decide in 600 passes, so a small gap is left).

```python
fig, ax = plt.subplots()
for beta, tail in zip(beta_scan, tails):
    ax.plot(np.full(len(tail), beta), tail, "k.", ms=2)
ax.axvline(beta_max, color="tab:red", ls="--", label=f"$\\beta_{{max}} = "
           f"{beta_max:.4f}$")
```

For every $\beta$ the loop draws its 30 kept inputs as small black dots (`"k."`) above it: `np.full(len(tail), beta)` is a list of 30 copies of $\beta$, the horizontal coordinates. A red dashed vertical line marks $\beta_{max}$; its label is made of two f-strings written next to each other (the doubled braces print one brace each, so the label shows $\beta_{max} = 0.7441$).

```python
ax.set_xlabel("mixing parameter $\\beta$")
ax.set_ylabel("last 30 inputs $n_L$")
ax.set_title("Where the loop ends, against $\\beta$")
ax.legend()
save_figure(fig, "long_run_diagram",
```

Labels, title, legend and `save_figure` for Figure 13d.5.

**What Figure 13d.5 shows.** Left of the red line all 30 dots of each $\beta$ lie on one point at $1.327$: the loop has converged. Right of it the dots split into two branches, the two values of the cycle of period 2; just beyond $\beta_{max}$ they are close to $1.327$, and they move apart as $\beta$ grows, to about $0.36$ and $1.92$ at $\beta = 1$ (plain iteration). This splitting of one fixed point into a cycle of period 2 is called a **period-doubling bifurcation**.

**In [12], a weaker repulsion and the threshold.**

```python
x2 = fixed_point(u=2.0)
g2 = slope(x2, u=2.0)
```

The fixed point and the slope for $U = 2$ (the keyword `u=2.0` replaces the default repulsion).

```python
report("U = 2: n_L*", f"{1.0 + x2:.6f}")
report("U = 2: G'(x*)", f"{g2:.6f}")
report("U = 2: beta_max", f"{2.0 / (1.0 - g2):.6f}")
check(abs(x2 - 0.468990) < 1e-6 and abs(g2 + 0.688942) < 1e-6
      and abs(2.0 / (1.0 - g2) - 1.184174) < 1e-6,
      "U = 2: x* = 0.468990, G' = -0.688942, beta_max = 1.184174")
```

The three `report` lines print $n_L^* = 1.468990$, $G' = -0.688942$ and $\beta_{max} = 1.184174$, and the check compares them with these values (to $10^{-6}$). Then

```python
n = 2.0
for _ in range(200):  # plain iteration with U = 2
    n = loop_pass(n, u=2.0)
check(abs(n - 1.0 - x2) < 1e-10, "U = 2: plain iteration converges")
```

runs 200 passes of plain iteration at $U = 2$ and checks that they reach the fixed point to $10^{-10}$.

```python
U_scan = np.linspace(0.5, 8.0, 76)
beta_limits = np.array([2.0 / (1.0 - slope(fixed_point(u=u), u=u)) for u in U_scan])
low, high = 2.0, 4.0  # beta_max(2) > 1 > beta_max(4)
for _ in range(60):
    middle = 0.5 * (low + high)
    if 2.0 / (1.0 - slope(fixed_point(u=middle), u=middle)) > 1.0:
        low = middle
    else:
        high = middle
U_critical = 0.5 * (low + high)
```

$\beta_{max}$ for 76 repulsions from $0.5$ to 8 (for each one the fixed point is found again). Then a bisection in $U$ between 2 (where $\beta_{max} > 1$) and 4 (where it is below 1) finds the repulsion at which $\beta_{max} = 1$, that is $G'(x^*) = -1$ (if $\beta_{max}$ at the middle is still above 1, the threshold lies above the middle, so `low` moves up).

```python
report("repulsion where plain iteration stops converging", f"{U_critical:.6f}")
check(abs(slope(fixed_point(u=U_critical), u=U_critical) + 1.0) < 1e-9,
      "at this repulsion the slope at the fixed point is exactly -1")
```

The `report` line prints $U = 2.647393$, and the check confirms that the slope at the fixed point is $-1$ there, to $10^{-9}$.

**In [13], the threshold as a picture.**

```python
fig, ax = plt.subplots()
ax.plot(U_scan, beta_limits, color="black", lw=2.0, label="$\\beta_{max}(U)$")
ax.axhline(1.0, color="gray", ls="--", label="plain iteration, $\\beta = 1$")
ax.axvline(U_critical, color="tab:red", ls=":",
           label=f"$U = {U_critical:.3f}$: plain iteration fails beyond")
ax.set_xlabel("repulsion $U$ (units of $t$)")
ax.set_ylabel("largest convergent mixing parameter")
ax.set_title("Stronger repulsion needs gentler mixing")
ax.legend(fontsize=8)
save_figure(fig, "threshold_versus_u",
```

The curve $\beta_{max}(U)$ as a thick black line, the grey dashed line $\beta = 1$ (plain iteration), a red dotted vertical line at the critical repulsion (its label shows $U = 2.647$), labels, title, legend and `save_figure` for Figure 13d.6.

**What Figure 13d.6 shows.** $\beta_{max}$ falls steadily from about $1.8$ at $U = 0.5$ to about $0.42$ at $U = 8$. It crosses the line $\beta = 1$ at $U = 2.647$: for weaker repulsion plain iteration converges (the curve lies above the dashed line), for stronger repulsion it fails, and the mixing step must be smaller the stronger the repulsion.

**In [14], the last check.**

```python
figure_names = ["reduced_map", "cobwebs", "error_histories", "convergence_factor",
                "long_run_diagram", "threshold_versus_u"]
missing = [name for k, name in enumerate(figure_names, 1)
           if not output_file(f"{FIGURE_FOLDER}/13d_{k}_{name}.png").is_file()]
check(missing == [], "all six figure files exist")
check(output_file(f"{FIGURE_FOLDER}/13d_6_threshold_versus_u.png").is_file(),
      "the figure file 13d_6_threshold_versus_u.png exists")
all_checks_passed()
```

The same lines as In [19] of Notebook 13c (Section 13.14), with the six figure names of this notebook. The last line prints ALL 17 CHECKS PASSED (notebook 13d): one check in In [2], two each in In [3], In [5] and In [6], four in In [8], one in In [11], three in In [12] and two in In [14].

### 13.26 Finite temperature: Mermin's theorem

So far the system was in its ground state. At a temperature $T > 0$ it is in a statistical mixture of states. (Boltzmann's constant is 1, so a temperature is an energy.)

**Density operators.** A mixture in which the state $\Psi_k$ occurs with the probability $w_k \ge 0$ ($\sum_k w_k = 1$) is described by the **density operator** $\hat\rho = \sum_k w_k\,|\Psi_k\rangle\langle\Psi_k|$, where $|\Psi\rangle\langle\Psi|$ is the operator that maps a state $\chi$ to $\Psi\,\langle\Psi|\chi\rangle$ (on a grid: the column $\Psi$ times the conjugated row $\Psi^\dagger$). It is Hermitian, $\langle\chi|\hat\rho\chi\rangle = \sum_k w_k|\langle\Psi_k|\chi\rangle|^2 \ge 0$ for every state, and $\mathrm{Tr}\,\hat\rho = \sum_k w_k = 1$ for normalised $\Psi_k$; so its eigenvalues $p_i$ lie between 0 and 1 and add up to 1. The expectation value of an observable is $\mathrm{Tr}(\hat\rho A)$. A **function of a Hermitian matrix** $A = \sum_i a_i\,u_iu_i^\dagger$ (eigenvalues $a_i$, orthonormal eigenvectors $u_i$) is defined through its eigenvalues, $f(A) = \sum_i f(a_i)\,u_iu_i^\dagger$; for $f = \exp$ this agrees with the power series, because $A^m = \sum_i a_i^m u_iu_i^\dagger$. The **entropy** is

$$
S = -\mathrm{Tr}(\hat\rho\ln\hat\rho) = -\sum_i p_i\ln p_i \;\ge 0 ,
$$

with the rule $0\ln0 = 0$ (the limit of $p\ln p$ as $p \to 0$); every term is $\ge 0$ because $\ln p_i \le 0$. When the particle number is fixed only on average by a **chemical potential** $\mu$, the equilibrium state at the temperature $T$ minimises the **grand potential**

$$
\Omega[\hat\rho] = \mathrm{Tr}\big[\hat\rho\,(\hat H - \mu\hat N)\big] - T\,S[\hat\rho] .
$$

**Theorem (Gibbs principle).** In a finite-dimensional state space $\Omega$ has exactly one minimiser, the **Gibbs state** $\hat\rho_0 = e^{-(\hat H - \mu\hat N)/T}/Z$ with $Z = \mathrm{Tr}\,e^{-(\hat H - \mu\hat N)/T}$, and $\Omega[\hat\rho_0] = -T\ln Z$.

**Proof, line by line.** Taking the logarithm of $\hat\rho_0$ (a function of the Hermitian matrix $\hat H - \mu\hat N$),

$$
\ln\hat\rho_0 = -\frac{\hat H - \mu\hat N}{T} - \ln Z \quad\Longrightarrow\quad \hat H - \mu\hat N = -T\ln\hat\rho_0 - T\ln Z .
$$

Inserting this into $\Omega$ and using $\mathrm{Tr}\,\hat\rho = 1$:

$$
\Omega[\hat\rho] = -T\,\mathrm{Tr}(\hat\rho\ln\hat\rho_0) - T\ln Z + T\,\mathrm{Tr}(\hat\rho\ln\hat\rho) = -T\ln Z + T\,D, \qquad D = \mathrm{Tr}\big[\hat\rho\,(\ln\hat\rho - \ln\hat\rho_0)\big] .
$$

For $\hat\rho = \hat\rho_0$ the number $D$ is 0, so $\Omega[\hat\rho_0] = -T\ln Z$. It remains to show **Klein's inequality** $D \ge 0$ for two density operators, with $D = 0$ only when they are equal. Write $\hat\rho = \sum_i p_i|i\rangle\langle i|$ and $\hat\rho_0 = \sum_j q_j|j\rangle\langle j|$ with orthonormal eigenvectors (all $q_j > 0$). Then

$$
\begin{aligned}
D &= \sum_i p_i\ln p_i - \sum_{i,j}p_i\,|\langle i|j\rangle|^2\ln q_j = \sum_{i,j}|\langle i|j\rangle|^2\,p_i\,(\ln p_i - \ln q_j) \\
&\ge \sum_{i,j}|\langle i|j\rangle|^2\,(p_i - q_j) = \sum_i p_i - \sum_j q_j = 1 - 1 = 0 .
\end{aligned}
$$

The first step evaluates the two traces in the eigenvectors of $\hat\rho$ (and expands $|i\rangle$ in the eigenvectors of $\hat\rho_0$ for the second); the second inserts $\sum_j|\langle i|j\rangle|^2 = 1$ (completeness) in the first sum; the inequality uses $a\ln a - a\ln b \ge a - b$ for $a \ge 0$, $b > 0$, which is $\ln y \le y - 1$ with $y = b/a$, multiplied by $-a$ (for $a = 0$ it reads $0 \ge -b$); the last steps use completeness once more and the traces 1. The inequality $\ln y \le y - 1$ holds because $y - 1 - \ln y$ has the derivative $1 - 1/y$, negative for $y < 1$ and positive for $y > 1$, so its smallest value is 0 at $y = 1$, and only there. Hence $D = 0$ forces $p_i = q_j$ whenever $\langle i|j\rangle \ne 0$, which makes $\hat\rho$ and $\hat\rho_0$ act in the same way on every $|j\rangle$: $\hat\rho = \hat\rho_0$. $\square$

Notebook 13e (In [3] and In [4]) builds the Gibbs state of the two-site model, checks $\Omega[\hat\rho_0] = -T\ln Z$, and finds for 2000 random density operators that $\Omega$ is always larger, with $\Omega - \Omega[\hat\rho_0] = T\,D$ to $10^{-10}$ (Figure 13e.1).

**Mermin's theorem (1965).** Replace the variational principle of Section 13.8 by the Gibbs principle: the proof of the Hohenberg-Kohn theorem then goes through word for word, with the strict inequality $\Omega[\hat\rho_0'] > \Omega[\hat\rho_0]$ for two different Gibbs states in place of $\langle\Psi'|\hat H\Psi'\rangle > E_0$. At a fixed $T$ and $\mu$ the equilibrium density determines the external potential, and there is a universal functional of the density whose minimum gives $\Omega$. This is the foundation of DFT at a temperature.

**Non-interacting fermions: independent orbitals, line by line.** For non-interacting fermions with orbital energies $\epsilon_a$, $\hat H - \mu\hat N = \sum_a(\epsilon_a - \mu)\,\hat n_a$, and every occupation-number state $|n_0 n_1 \cdots\rangle$ is an eigenstate with the eigenvalue $\sum_a(\epsilon_a - \mu)n_a$. Its Gibbs weight is

$$
\frac{e^{-\sum_a(\epsilon_a - \mu)n_a/T}}{Z} = \prod_a\frac{e^{-(\epsilon_a - \mu)n_a/T}}{1 + e^{-(\epsilon_a - \mu)/T}}, \qquad Z = \prod_a\big(1 + e^{-(\epsilon_a - \mu)/T}\big) ,
$$

because the exponential of a sum is the product of the exponentials, and the sum over all choices $n_a \in \{0, 1\}$ of a product of factors, one per orbital, is the product of the sums of each factor over $n_a = 0, 1$. So the configuration $\{n_a\}$ has the probability $\prod_a p_a(n_a)$ with

$$
p_a(1) = \frac{e^{-(\epsilon_a - \mu)/T}}{1 + e^{-(\epsilon_a - \mu)/T}} = \frac{1}{e^{(\epsilon_a - \mu)/T} + 1} = f_a, \qquad p_a(0) = 1 - f_a :
$$

each orbital is an independent two-state system, occupied with the **Fermi-Dirac** probability $f_a$ (the second step multiplies numerator and denominator by $e^{(\epsilon_a - \mu)/T}$). Because the logarithm of a product is a sum, the entropy of independent orbitals is the sum of their entropies,

$$
S_s = -\sum_a\big[f_a\ln f_a + (1 - f_a)\ln(1 - f_a)\big] .
$$

Notebook 13e (In [6]) checks the product form on three orbitals: the eight Gibbs weights equal the eight products to $10^{-15}$.

**The Mermin-Kohn-Sham functional.** The non-interacting reference system at $T > 0$ is an ensemble of orbitals $\phi_a$ with occupations $f_a \in [0, 1]$, density $n = \sum_a f_a|\phi_a|^2$ and entropy $S_s$. Mermin's Kohn-Sham functional is the free energy

$$
F = \sum_a f_a\Big\langle\phi_a\Big|-\frac12\frac{d^2}{dx^2}\Big|\phi_a\Big\rangle - T\,S_s + \int v\,n\,dx + E_H[n] + F_{xc}[n] ,
$$

with a temperature-dependent exchange-correlation part $F_{xc}$. Making $F$ stationary with respect to the orbitals gives the Kohn-Sham equations of Section 13.10 unchanged. Making it stationary with respect to the occupations under the condition $\sum_a f_a = N$ (multiplier $\mu$), line by line:

$$
\begin{aligned}
\frac{\partial}{\partial f_a}\Big[F - \mu\Big(\sum_b f_b - N\Big)\Big] &= \epsilon_a + T\ln\frac{f_a}{1 - f_a} - \mu = 0 ,\\
\ln\frac{f_a}{1 - f_a} = -\frac{\epsilon_a - \mu}{T} \quad&\Longrightarrow\quad f_a = \frac{1}{e^{(\epsilon_a - \mu)/T} + 1} .
\end{aligned}
$$

The first line uses that the energy terms change with $f_a$ by $\langle\phi_a|-\tfrac12 d^2/dx^2|\phi_a\rangle + \int(v + v_H + v_{xc})|\phi_a|^2 = \epsilon_a$ (the chain rule through $n$), and that $\frac{d}{df}[f\ln f + (1 - f)\ln(1 - f)] = \ln f + 1 - \ln(1 - f) - 1 = \ln\frac{f}{1 - f}$; the second solves for $f_a$ (take the exponential of both sides and solve $f/(1 - f) = e^{-(\epsilon - \mu)/T}$). So the occupations are the Fermi-Dirac numbers. As $T \to 0$, $f_a \to 1$ below $\mu$ and $f_a \to 0$ above it: the aufbau rule (Figure 13e.2).

**Finding $\mu$.** The particle number $\sum_a g_a f_a$ ($g_a$: the number of states of level $a$) increases strictly with $\mu$, because each $f_a$ does; so exactly one $\mu$ gives $\sum_a g_a f_a = N$, and **bisection** finds it: start with an interval that surely contains $\mu$, look at its middle, keep the half in which the particle number crosses $N$, and repeat; every step halves the interval (Figure 13e.3). The Revision Kohn-Sham solver fixes $\mu$ by the same condition, written in a form that loses no digits when $N$ is large: it splits the levels at a dividing point and balances the thermally excited particles above it against the holes below it, counting a hole with $f(-x) = 1 - f(x)$ computed without a subtraction, and finds the root of this balance in a logarithmic form (named LogBalance) by Newton steps safeguarded by bisection (`Revision/kohn_sham/results/parameters.json`, conventions merminRoot and numerics merminRoot).

**A form of the entropy without $\ln 0$, line by line.** With $x = (\epsilon - \mu)/T$, $f = 1/(e^x + 1)$ and $1 - f = e^x/(e^x + 1)$:

$$
\begin{aligned}
-\ln f &= \ln(1 + e^x), \qquad -\ln(1 - f) = \ln(1 + e^x) - x = \ln(1 + e^{-x}) ,\\
s(x) &= -f\ln f - (1 - f)\ln(1 - f) = f\ln(1 + e^x) + (1 - f)\ln(1 + e^{-x}) .
\end{aligned}
$$

For $x \ge 0$ write $\ln(1 + e^x) = x + \ln(1 + e^{-x})$; then $s = f\,x + f\ln(1 + e^{-x}) + (1 - f)\ln(1 + e^{-x}) = \ln(1 + e^{-x}) + x\,f(x)$. Since $s(-x) = s(x)$ (exchanging $f$ and $1 - f$), for every $x$: $s = \ln(1 + e^{-|x|}) + |x|\,f(|x|)$, a form in which no logarithm of 0 and no overflow can occur. Notebook 13e uses it.

**Thermodynamics, line by line.** At fixed $N$ the energy is $E = \sum_a g_a f_a\epsilon_a$ and the free energy $F = E - TS_s$, both functions of $T$ through the occupations and $\mu$. (i) **$dF/dT = -S_s$** (the **envelope theorem**). $F$ depends on $T$ explicitly (the factor $T$ in $-TS_s$) and through the occupations:

$$
\frac{dF}{dT} = \frac{\partial F}{\partial T}\Big|_{f} + \sum_a\frac{\partial F}{\partial f_a}\,\frac{df_a}{dT} = -S_s + \mu\sum_a g_a\,\frac{df_a}{dT} = -S_s + \mu\,\frac{dN}{dT} = -S_s .
$$

The first step is the chain rule; the second uses the stationarity condition $\partial F/\partial f_a = g_a\mu$ found above (for a level with $g_a$ states); the third recognises the derivative of $N = \sum_a g_a f_a$; the fourth uses that $N$ is fixed. (ii) **$C_V = T\,dS_s/dT$**: the **heat capacity** $C_V = dE/dT = d(F + TS_s)/dT = -S_s + S_s + T\,dS_s/dT$. (iii) **The variance formula.** With $f = 1/(e^x + 1)$, $df/dx = -f(1 - f)$, and $x = (\epsilon - \mu)/T$ changes with $T$ by $dx/dT = -(\epsilon - \mu)/T^2 - \mu'/T$ ($\mu' = d\mu/dT$). So, with $w_a = g_a f_a(1 - f_a)$,

$$
\begin{aligned}
g_a\frac{df_a}{dT} &= w_a\Big[\frac{\epsilon_a - \mu}{T^2} + \frac{\mu'}{T}\Big] ,\qquad
0 = \frac{dN}{dT} = \sum_a w_a\Big[\frac{\epsilon_a - \mu}{T^2} + \frac{\mu'}{T}\Big] \;\Rightarrow\; \frac{\mu'}{T} = -\frac{\sum_a w_a(\epsilon_a - \mu)}{T^2\sum_a w_a} ,\\
C_V &= \sum_a\epsilon_a\,g_a\frac{df_a}{dT} = \sum_a(\epsilon_a - \mu)\,g_a\frac{df_a}{dT} = \frac{1}{T^2}\Big[\sum_a w_a(\epsilon_a - \mu)^2 - \frac{\big(\sum_a w_a(\epsilon_a - \mu)\big)^2}{\sum_a w_a}\Big] .
\end{aligned}
$$

The first line is the chain rule and the condition of fixed $N$, solved for $\mu'$; in the second line the second step subtracts $\mu\sum_a g_a\,df_a/dT = \mu\,dN/dT = 0$, and the third inserts the first line and $\mu'$. The bracket is $\sum_a w_a$ times the **weighted variance** of the numbers $\epsilon_a - \mu$ with the weights $w_a$, which is never negative (it equals $\sum_a w_a(\epsilon_a - \bar\epsilon)^2$ with the weighted mean $\bar\epsilon$, a sum of non-negative terms). Hence **$C_V \ge 0$**.

**Worked example: two levels, one particle.** Levels $\epsilon_0 = 0$ and $\epsilon_1 = 1$ (one state each), one particle, $T = \tfrac12$, no interaction. By symmetry $\mu = \tfrac12$: then $f_0 + f_1 = \frac{1}{e^{-1} + 1} + \frac{1}{e^{1} + 1} = 1$ (the two fractions add to 1, as one sees by multiplying the first by $e/e$). So $f_0 = 1/(e^{-1} + 1) = 0.731059$, $f_1 = 0.268941$, $E = f_1\epsilon_1 = 0.268941$, $S_s = 1.164406$ (each level contributes $0.582203$), and $F = E - TS_s = 0.268941 - 0.582203 = -0.313262$. Since $\mu = \tfrac12$ at every temperature, $E(T) = 1/(e^{1/(2T)} + 1)$ and $C_V = dE/dT = \frac{e^{1/(2T)}}{(e^{1/(2T)} + 1)^2}\cdot\frac{1}{2T^2}$, which at $T = \tfrac12$ is $2e/(e + 1)^2 = 0.393224$. Notebook 13e (In [8] and In [10]) computes all these numbers and checks $dF/dT = -S_s$ by a difference quotient.

### 13.27 Excited states: the Kohn-Sham gap, Janak's theorem and Delta-SCF

The ground-state theory says nothing directly about excited states. This section introduces the particle-hole energies, the Kohn-Sham gap, Janak's theorem and the Delta-SCF method. The Revision Kohn-Sham solver reports three of these quantities for dirac16complex, the particle-hole energies, the Kohn-Sham gap and the Delta-SCF excitation energy (the folder `Revision/kohn_sham/results/excited`); Janak's theorem is the exact statement that connects the last two.

**Particle-hole excitations and the Kohn-Sham gap.** In a non-interacting system, moving one particle from an occupied orbital $i$ (it leaves a **hole**) to an empty orbital $a$ (a **particle**) costs exactly $\epsilon_a - \epsilon_i$, because the levels do not depend on the occupations. The smallest such cost is the **Kohn-Sham gap**

$$
\Delta_{KS} = \epsilon_{LUMO} - \epsilon_{HOMO} ,
$$

where HOMO is the highest occupied orbital and LUMO the lowest unoccupied orbital (names taken over from chemistry). In the interacting system the Kohn-Sham levels move when the occupations change, so $\Delta_{KS}$ is only a first estimate of the lowest excitation energy.

**Janak's theorem.** Let the energy $E(\{f\})$ be evaluated with orbitals that are self-consistent for the given occupations. Then

$$
\frac{\partial E}{\partial f_a} = \epsilon_a .
$$

**Proof.** $E = \sum_b f_b\langle\phi_b|-\tfrac12 d^2/dx^2|\phi_b\rangle + E_{pot}[n]$, where $E_{pot}$ collects $\int v\,n$, $E_H$ and $E_{xc}$, and $n = \sum_b f_b|\phi_b|^2$. $E$ depends on $f_a$ explicitly and through the orbitals. The explicit derivative is $\langle\phi_a|-\tfrac12 d^2/dx^2|\phi_a\rangle + \int(\delta E_{pot}/\delta n)|\phi_a|^2 = \langle\phi_a|h_s\phi_a\rangle = \epsilon_a$, with the Kohn-Sham Hamiltonian $h_s$. The change through the orbitals is $\sum_b f_b\big(\langle d\phi_b|h_s\phi_b\rangle + \langle h_s\phi_b|d\phi_b\rangle\big) = \sum_b f_b\,\epsilon_b\,d\langle\phi_b|\phi_b\rangle = 0$, because the Kohn-Sham equations $h_s\phi_b = \epsilon_b\phi_b$ hold and the orbitals stay normalised ($\langle\phi_b|\phi_b\rangle = 1$ does not change). $\square$

**Delta-SCF.** The **Delta-SCF** method computes an excited state as a second self-consistent solution in which the occupations are fixed by hand: one particle is taken out of the HOMO and put into the LUMO, and the Kohn-Sham loop is run again with these occupations. The excitation energy is the difference of the two energies, $\Delta_{SCF} = E_1 - E_0$. Janak's theorem connects it with the gap: move the particle gradually, $f_{HOMO} = 1 - \tau$ and $f_{LUMO} = \tau$; then by the chain rule $dE/d\tau = \partial E/\partial f_{LUMO} - \partial E/\partial f_{HOMO} = \epsilon_{LUMO}(\tau) - \epsilon_{HOMO}(\tau)$, and integrating from $\tau = 0$ to $1$,

$$
\Delta_{SCF} = \int_0^1\big[\epsilon_{LUMO}(\tau) - \epsilon_{HOMO}(\tau)\big]\,d\tau .
$$

At $\tau = 0$ the integrand is $\Delta_{KS}$; the difference $\Delta_{SCF} - \Delta_{KS}$ measures how much the levels move when the particle is transferred (the **orbital relaxation**). The midpoint value $\epsilon_{LUMO}(\tfrac12) - \epsilon_{HOMO}(\tfrac12)$ (Slater's **transition state**) is a good estimate of the integral when the integrand is nearly a straight line in $\tau$. Janak's theorem and the integral formula are PROVED; that the Delta-SCF state approximates a true excited state of the interacting system is an ASSUMPTION of the method. The Revision solver uses an **ensemble** form: one particle is moved from the highest occupied group of equal levels to the lowest empty group, spread evenly over each group, which keeps the symmetries of its reduction (`Revision/kohn_sham/results/parameters.json`, conventions deltaScf).

**Toy example.** Take the model energy $E(f_H, f_L) = \epsilon_H^0 f_H + \epsilon_L^0 f_L + \tfrac{U}{2}(f_H^2 + f_L^2)$ with $\epsilon_H^0 = 0$, $\epsilon_L^0 = 1$, $U = 0.2$ (the last term plays the role of a self-interaction of each orbital). Janak's theorem gives the levels $\epsilon_H = \partial E/\partial f_H = Uf_H$ and $\epsilon_L = 1 + Uf_L$. In the ground state $(f_H, f_L) = (1, 0)$: $E_0 = 0.1$, $\epsilon_H = 0.2$, $\epsilon_L = 1$, so $\Delta_{KS} = 0.8$. In the Delta-SCF state $(0, 1)$: $E_1 = 1 + 0.1 = 1.1$, so $\Delta_{SCF} = 1.0$. The integral formula reproduces it: $\int_0^1[1 + U\tau - U(1 - \tau)]\,d\tau = \int_0^1(0.8 + 0.4\tau)\,d\tau = 0.8 + 0.2 = 1$. Here the relaxation raises the excitation energy by $U = 0.2$ above the gap, and the transition state is exact because the integrand is a straight line. (In the trap of Notebook 13a, Section 13.32, the relaxation lowers it instead: its sign depends on the system.)

### 13.28 Example: Mermin thermodynamics and Delta-SCF

Notebook 13e checks every exact statement of Sections 13.26 and 13.27 with numbers: the Gibbs principle and Klein's inequality on the 16 states of the two-site model with 2000 random density operators, the independence of the orbitals of non-interacting fermions, the Fermi-Dirac function, the bisection for $\mu$ (and the rule by which the Revision solver fixes $\mu$, read from its parameter file), the thermodynamics of two levels (the worked numbers $0.731059$, $1.164406$, $-0.313262$, $0.393224$) and of a ladder of levels, and Janak's theorem with the Delta-SCF integral on the toy model energy. Its statements are PROVED above; its numbers are toy numbers (no Revision number is reproduced). It ends with ALL 24 CHECKS PASSED (notebook 13e) and draws seven figures.

<!-- NOTEBOOK 13e -->

### 13.31 Line-by-line walk-through of Notebook 13e

The notebook has seventeen code cells. **In [1]** is the set-up cell, identical to In [1] of Notebook 13c (Section 13.14) except for the name `"13e"` and its comment lines, which hold the instructions of Section 13.29.

**In [2], the two-site model in Fock space.**

```python
import itertools  # loops over combinations

import numpy as np  # arrays, matrices and linear algebra

M, DIM = 4, 16  # four orbitals, sixteen occupation-number states
a = []  # annihilation operators
for p in range(M):
    matrix = np.zeros((DIM, DIM))
    for state in range(DIM):
        if (state >> p) & 1:  # orbital p is occupied in this state
            nu = sum((state >> q) & 1 for q in range(p))  # occupied before p
            matrix[state ^ (1 << p), state] = (-1) ** nu
    a.append(matrix)
a_dag = [matrix.T for matrix in a]
n_op = [a_dag[p] @ a[p] for p in range(M)]
N_op = sum(n_op)  # the particle-number operator
```

The same construction of the $16 \times 16$ operator matrices as in In [4] of Notebook 13c (Section 13.14 explains every line), with the bit test written directly instead of through a function `bit`. `n_op` are the occupation operators and `N_op` the number operator $\hat N$.

```python
H = -(a_dag[0] @ a[1] + a_dag[1] @ a[0] + a_dag[2] @ a[3] + a_dag[3] @ a[2]) \
    + 2.0 * (n_op[0] @ n_op[2] + n_op[1] @ n_op[3])  # t = 1, U = 2
check(np.allclose(H, H.T) and np.allclose(H @ N_op, N_op @ H),
      "H is symmetric and conserves the particle number")
```

The two-site Hamiltonian with $t = 1$, $U = 2$ on all 16 states (all particle numbers from 0 to 4). The check: $H$ is symmetric (real Hermitian) and commutes with $\hat N$ ($H\hat N = \hat N H$), so it never changes the particle number.

**In [3], the Gibbs state.**

```python
MU, TEMPERATURE = 1.0, 0.5
K = H - MU * N_op  # H - mu N


def entropy(rho):
    """S = -sum p ln p over the eigenvalues p of rho (0 ln 0 = 0)."""
    p = np.clip(np.linalg.eigvalsh(rho), 0.0, None)
    p = p[p > 1e-300]
    return float(-np.sum(p * np.log(p)))


def grand_potential(rho):
    """Omega = Tr[rho (H - mu N)] - T S."""
    return float(np.trace(rho @ K).real) - TEMPERATURE * entropy(rho)
```

$\mu = 1$, $T = 0.5$ and $K = \hat H - \mu\hat N$. `entropy` computes $-\sum_i p_i\ln p_i$ from the eigenvalues of a density operator: `np.clip(..., 0.0, None)` replaces tiny negative rounding errors by 0, and `p[p > 1e-300]` drops the zeros (the rule $0\ln0 = 0$). `grand_potential` is $\Omega = \mathrm{Tr}(\hat\rho K) - TS$.

```python
k_values, k_vectors = np.linalg.eigh(K)
boltzmann = np.exp(-(k_values - k_values.min()) / TEMPERATURE)  # shifted weights
Z_shifted = boltzmann.sum()
rho_gibbs = (k_vectors * (boltzmann / Z_shifted)) @ k_vectors.T
ln_Z = np.log(Z_shifted) - k_values.min() / TEMPERATURE  # undo the shift
omega_gibbs = grand_potential(rho_gibbs)
```

The Gibbs state as a function of $K$: eigenvalues and eigenvectors of $K$, the weights $e^{-k_i/T}$ shifted by the smallest eigenvalue to avoid overflow (Section 13.14 explains the shift), and $\hat\rho_0 = \sum_i(w_i/\sum w)\,u_iu_i^T$. The true $\ln Z$ undoes the shift: $Z = Z_{shifted}\,e^{-k_{min}/T}$, so $\ln Z = \ln Z_{shifted} - k_{min}/T$. `omega_gibbs` is $\Omega[\hat\rho_0]$, computed with the function above.

```python
report("Omega of the Gibbs state", f"{omega_gibbs:.10f}")
report("-T ln Z", f"{-TEMPERATURE * ln_Z:.10f}")
check(abs(omega_gibbs + TEMPERATURE * ln_Z) < 1e-12, "Omega[Gibbs] = -T ln Z")
```

The two `report` lines print $\Omega[\hat\rho_0]$ and $-T\ln Z$, both $-3.4716265446$, and the check requires them to agree to $10^{-12}$.

**In [4], 2000 random density operators.**

```python
ln_rho_gibbs = (k_vectors * (-k_values / TEMPERATURE - ln_Z)) @ k_vectors.T


def matrix_log(rho):
    """ln rho through the eigenvalues (all positive here)."""
    values, vectors = np.linalg.eigh(rho)
    return (vectors * np.log(values)) @ vectors.conj().T
```

$\ln\hat\rho_0 = -K/T - \ln Z$, built from the eigenvectors of $K$; `matrix_log` is the logarithm of a Hermitian matrix with positive eigenvalues, through its eigenvalues (Section 13.26).

```python
rng = np.random.default_rng(12345)  # fixed seed: the same numbers every run
gaps, kleins = [], []
for _ in range(2000):
    A = rng.normal(size=(DIM, DIM)) + 1j * rng.normal(size=(DIM, DIM))
    random_rho = A @ A.conj().T
    random_rho /= np.trace(random_rho).real
    s = rng.uniform(0.0, 1.0)  # how far from the Gibbs state
    rho = (1.0 - s) * rho_gibbs + s * random_rho
    gaps.append(grand_potential(rho) - omega_gibbs)
    kleins.append(np.trace(rho @ (matrix_log(rho) - ln_rho_gibbs)).real)
gaps, kleins = np.array(gaps), np.array(kleins)
```

For a random complex matrix $A$, the matrix $AA^\dagger$ is Hermitian with non-negative eigenvalues ($\langle\chi|AA^\dagger\chi\rangle = |A^\dagger\chi|^2 \ge 0$); divided by its trace (`/=` divides the variable in place) it is a density operator. Mixed with the Gibbs state with a random weight $s$ between 0 and 1 (`rng.uniform`), it gives states near and far from the minimum. For each, `gaps` stores $\Omega - \Omega_0$ and `kleins` Klein's $D$.

```python
say(f"smallest Omega - Omega_0 among 2000 states: {gaps.min():.3e}")
check(np.all(gaps > 0.0), "every random density operator has Omega > Omega[Gibbs]")
check(np.max(np.abs(gaps - TEMPERATURE * kleins)) < 1e-10,
      "Omega - Omega[Gibbs] = T D with Klein's D (identity)")
```

The smallest excess is $3.878\cdot10^{-6}$ (`:.3e` writes a number with three decimals and a power of ten), still positive. The checks: all 2000 excesses are positive, and each equals $T\,D$ to $10^{-10}$, the identity of the proof in Section 13.26.

**In [5], the histogram.**

```python
fig, ax = plt.subplots()
bins = np.logspace(np.floor(np.log10(gaps.min())), np.ceil(np.log10(gaps.max())), 40)
ax.hist(gaps, bins=bins, color="tab:blue", edgecolor="black", lw=0.5)
ax.set_xscale("log")
```

`np.log10` is the logarithm to the base 10; `np.floor` and `np.ceil` round down and up to whole numbers, so the two arguments are the exponents of the powers of ten just below the smallest excess and just above the largest ($-6$ and 1 here). `np.logspace(a, b, 40)` makes 40 numbers from $10^a$ to $10^b$, equally spaced on a logarithmic scale: the edges of the bins (the intervals in which the excesses are counted). `ax.hist` counts the excesses in each bin and draws the counts as blue bars with thin black edges, and `ax.set_xscale("log")` makes the horizontal axis logarithmic.

```python
ax.set_xlabel("$\\Omega[\\hat\\rho] - \\Omega[\\hat\\rho_0]$ (units of $t$)")
ax.set_ylabel("number of random states")
ax.set_title("The Gibbs state has the lowest grand potential")
save_figure(fig, "gibbs_principle",
```

Labels (the grand potential is an energy, in units of the hopping $t$), title, and `save_figure` for Figure 13e.1.

**What Figure 13e.1 shows.** Every bar lies to the right of zero (on a logarithmic axis zero itself cannot appear, and no excess is negative): all 2000 random states have a larger grand potential than the Gibbs state. Most excesses are between $0.1t$ and $2t$, from states mixed strongly away from the Gibbs state; a thin tail reaches down to about $4 \cdot 10^{-6}t$, from states with a mixing weight $s$ close to 0. The closer a state is to the Gibbs state, the smaller its excess, but it never becomes negative.

**In [6], independent orbitals.**

```python
levels3 = np.array([-0.5, 0.2, 1.0])
mu3, T3 = 0.1, 0.4
configurations = list(itertools.product((0, 1), repeat=3))
weights = np.array([np.exp(-np.dot(levels3 - mu3, c) / T3) for c in configurations])
weights /= weights.sum()  # divide by Z
f3 = 1.0 / (np.exp((levels3 - mu3) / T3) + 1.0)
products = np.array([np.prod([f3[k] if c[k] else 1.0 - f3[k] for k in range(3)])
                     for c in configurations])
```

Three orbitals with the energies $-0.5$, $0.2$, $1.0$ at $\mu = 0.1$, $T = 0.4$. The 8 configurations are all triples of zeros and ones (`itertools.product((0, 1), repeat=3)`). For each, `np.dot(levels3 - mu3, c)` is $\sum_a(\epsilon_a - \mu)n_a$, and its exponential, divided by the sum of all eight ($Z$), is the Gibbs weight. `products` multiplies, for each configuration, $f_a$ for the occupied and $1 - f_a$ for the empty orbitals (`x if condition else y` chooses; `np.prod` multiplies the three factors).

```python
for c, wgt, prod in zip(configurations, weights, products):
    say(f"occupations {c}: Gibbs weight {wgt:.6f}, product {prod:.6f}")
check(np.max(np.abs(weights - products)) < 1e-15,
      "the Gibbs weights are products of independent Fermi-Dirac probabilities")
```

The loop prints the eight pairs (for example $0.415797$ and $0.415797$ for the configuration (1, 0, 0), the most likely one: the lowest orbital, $0.6$ below $\mu$, filled, the others empty), and the check requires every weight to equal its product to $10^{-15}$.

**In [7], the Fermi-Dirac function.**

```python
def fermi(energy, mu, temperature):
    """The Fermi-Dirac occupation 1 / (exp(x) + 1), x = (energy - mu)/T, written
    as exp(-ln(1 + e^x)) so that no overflow can occur."""
    x = (np.asarray(energy, dtype=float) - mu) / temperature
    return np.exp(-np.logaddexp(0.0, x))
```

$e^x$ exceeds the largest number the computer can store (about $10^{308}$) for $x > 709$. Since $1/(e^x + 1) = e^{-\ln(1 + e^x)}$, the function uses numpy's `logaddexp(0, x)` $= \ln(e^0 + e^x)$, which is computed without overflow for every $x$.

```python
eps = np.linspace(-2.0, 2.0, 801)
check(abs(fermi(0.0, 0.0, 0.3) - 0.5) < 1e-15
      and np.allclose(fermi(eps, 0.0, 0.3), 1.0 - fermi(-eps, 0.0, 0.3), atol=1e-15),
      "f(mu) = 1/2 and f(mu + d) = 1 - f(mu - d)")
```

The check: $f(\mu) = \tfrac12$, and $f(\mu + d) = 1 - f(\mu - d)$ for 801 values of $d$ (a hole below $\mu$ is as likely as a particle above it; algebraically, $1 - \frac{1}{e^{-x} + 1} = \frac{e^{-x}}{e^{-x} + 1} = \frac{1}{1 + e^{x}}$).

```python
fig, ax = plt.subplots()
for temperature in (0.02, 0.1, 0.3, 1.0):
    ax.plot(eps, fermi(eps, 0.0, temperature), label=f"$T = {temperature}$")
ax.axvline(0.0, color="gray", ls="--", lw=0.8)
ax.set_xlabel("orbital energy $\\epsilon - \\mu$")
ax.set_ylabel("occupation $f$")
ax.set_title("The Fermi-Dirac occupation")
ax.legend()
save_figure(fig, "fermi_dirac",
```

The loop draws $f$ against $\epsilon - \mu$ (with $\mu = 0$) for $T = 0.02$, $0.1$, $0.3$ and 1; a grey dashed vertical line marks $\epsilon = \mu$; labels, title, legend and `save_figure` for Figure 13e.2.

**What Figure 13e.2 shows.** At $T = 0.02$ the curve is practically a step: every orbital below $\mu$ is occupied and every orbital above it empty, the aufbau rule. As $T$ grows, the step is smeared over a width of a few $T$: at $T = 1$ an orbital $2$ below $\mu$ is occupied only with the probability $0.88$. All four curves pass through $\tfrac12$ at $\epsilon = \mu$, and each is point-symmetric about that point (the hole-particle symmetry just checked).

**In [8], the chemical potential and the two-level system.**

```python
def chemical_potential(levels, degeneracies, N, temperature, history=None):
    """mu with sum g f = N, by bisection (the sum increases with mu)."""
    low, high = levels.min() - 50.0 * temperature - 5.0, levels.max() + 5.0
    for _ in range(100):
        middle = 0.5 * (low + high)
        if np.sum(degeneracies * fermi(levels, middle, temperature)) < N:
            low = middle  # too few particles: mu must rise
        else:
            high = middle
        if history is not None:
            history.append(high - low)
    return 0.5 * (low + high)
```

Bisection for $\mu$ (Section 13.26). The starting interval surely contains $\mu$: at its lower end every occupation is below $e^{-50}$, so the levels hold fewer than $N$ particles; at its upper end, 5 above the highest level, they hold almost all their states, more than $N$ when $N$ is less than the number of states. 100 halvings follow; if a list `history` is given, the width of the interval after each step is appended to it.

```python
def thermodynamics(levels, degeneracies, N, temperature):
    """mu, occupations, E, S, F of non-interacting levels at fixed N."""
    mu = chemical_potential(levels, degeneracies, N, temperature)
    f = fermi(levels, mu, temperature)
    x = np.abs(levels - mu) / temperature
    s_level = np.logaddexp(0.0, -x) + x * fermi(x, 0.0, 1.0)  # entropy of a state
    S = np.sum(degeneracies * s_level)
    E = np.sum(degeneracies * f * levels)
    return mu, f, E, S, E - temperature * S
```

For given levels, degeneracies $g_a$, particle number and temperature: $\mu$, the occupations, the entropy of one state in the form $\ln(1 + e^{-|x|}) + |x|f(|x|)$ of Section 13.26 (`fermi(x, 0.0, 1.0)` is $1/(e^x + 1)$), $S = \sum_a g_a s_a$, $E = \sum_a g_a f_a\epsilon_a$ and $F = E - TS$.

```python
two_levels, ones = np.array([0.0, 1.0]), np.array([1.0, 1.0])
widths = []
chemical_potential(two_levels, ones, 1.0, 0.5, widths)
mu2, f2, E2, S2, F2 = thermodynamics(two_levels, ones, 1.0, 0.5)
```

The worked example of Section 13.26: levels 0 and 1, one state each, one particle, $T = \tfrac12$. The first call records the widths of the bisection for the figure of In [10] (its result is not stored); the second computes the thermodynamics, and the five returned values are assigned to five names at once.

```python
report("mu", f"{mu2:.6f}")
report("f_0, f_1", f"{f2[0]:.6f}, {f2[1]:.6f}")
report("E, S, F", f"{E2:.6f}, {S2:.6f}, {F2:.6f}")
check(abs(mu2 - 0.5) < 1e-12 and abs(f2[0] - 0.731059) < 1e-6
      and abs(f2[1] - 0.268941) < 1e-6,
      "mu = 1/2, f_0 = 0.731059, f_1 = 0.268941")
check(abs(E2 - 0.268941) < 1e-6 and abs(S2 - 1.164406) < 1e-6
      and abs(F2 + 0.313262) < 1e-6, "E = 0.268941, S = 1.164406, F = -0.313262")
```

The `report` lines print $\mu = 0.500000$, the occupations $f_0 = 0.731059$ and $f_1 = 0.268941$, and $E = 0.268941$, $S = 1.164406$ and $F = -0.313262$, and the two checks compare them with the values worked out by hand in Section 13.26 ($\mu$ to $10^{-12}$, the others to $10^{-6}$, the rounding of the six printed decimals).

**In [9], the Revision solver's rule for $\mu$.**

```python
parameters = json.loads(repository_file(
    "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
root_rule = parameters["conventions"]["merminRoot"]  # a sentence of the record
root_form = parameters["numerics"]["merminRoot"]  # the name of the canonical form
say(f"Revision solver: canonical root form {root_form}")
check(root_rule.startswith("mu from sum g f = N")
      and "holes below a split of the levels" in root_rule
      and root_form == "LogBalance",
      "the Revision solver fixes mu by sum g f = N, balancing particles and holes "
      "(Revision/kohn_sham/results/parameters.json, conventions merminRoot)")
```

The cell reads two entries of the solver's parameter file: the sentence that describes the rule (`conventions`) and the name of the form it uses (`numerics`). The check requires the sentence to start with "mu from sum g f = N" and to contain the words about particles and holes, and the form to be LogBalance (Section 13.26).

**In [10], derivatives with respect to $T$, and the bisection history.**

```python
def at(temperature, levels=two_levels, degeneracies=ones, N=1.0):
    return thermodynamics(levels, degeneracies, N, temperature)


d = 1e-4
dF_dT = (at(0.5 + d)[4] - at(0.5 - d)[4]) / (2 * d)
dE_dT = (at(0.5 + d)[2] - at(0.5 - d)[2]) / (2 * d)
T_dS_dT = 0.5 * (at(0.5 + d)[3] - at(0.5 - d)[3]) / (2 * d)
```

`at(T)` is the two-level thermodynamics at the temperature $T$; its result is the tuple $(\mu, f, E, S, F)$, so `[2]`, `[3]`, `[4]` are $E$, $S$, $F$. Central difference quotients with the step $10^{-4}$ (with $\mu$ solved again at each temperature) give $dF/dT$, $dE/dT$ and $T\,dS/dT$ at $T = \tfrac12$ (the factor `0.5` in the third line is $T$).

```python
report("dF/dT", f"{dF_dT:.6f}")
report("C_V = dE/dT", f"{dE_dT:.6f}")
check(abs(dF_dT + S2) < 1e-7, "dF/dT = -S (envelope theorem)")
check(abs(dE_dT - 0.393224) < 1e-6 and abs(T_dS_dT - dE_dT) < 1e-7,
      "C_V = dE/dT = T dS/dT = 0.393224")
```

The cell prints $dF/dT = -1.164406$ and $C_V = 0.393224$ and checks $dF/dT = -S$ (to $10^{-7}$), $C_V = 0.393224$ (the value $2e/(e + 1)^2$ of Section 13.26) and $dE/dT = T\,dS/dT$ (to $10^{-7}$).

```python
fig, ax = plt.subplots()
ax.semilogy(range(1, 51), widths[:50], "o-", ms=3)
ax.set_xlabel("bisection step")
ax.set_ylabel("width of the interval that contains $\\mu$")
ax.set_title("Bisection halves the interval at every step")
save_figure(fig, "bisection",
```

The first 50 recorded widths against the step numbers 1 to 50 (`range(1, 51)`), on a logarithmic vertical axis; labels, title and `save_figure` for Figure 13e.3. The last check

```python
check(all(abs(b / a_ - 0.5) < 1e-12 for a_, b in zip(widths[:40], widths[1:41])),
      "every bisection step halves the interval")
```

requires every width to be half of the previous one (for the first 40 steps; the name `a_` avoids the name `a` of the operator list).

**What Figure 13e.3 shows.** The starting interval is $[-30, 6]$, 36 wide, so after the first step the width is 18. On the logarithmic axis the points then fall on a straight line, by $\log_{10}2 = 0.30$ per step, to about $3 \cdot 10^{-14}$ after 50 steps: bisection gains one binary digit of $\mu$ at every step, whatever the function, as long as the root is inside the interval.

**In [11], two levels at all temperatures.**

```python
temperatures = np.linspace(0.02, 3.0, 150)
table = np.array([at(T)[2:] for T in temperatures])  # columns E, S, F
C_V = np.array([T * (at(T + d)[3] - at(T - d)[3]) / (2 * d) for T in temperatures])
hot = at(1000.0)
check(table[0, 1] < 1e-8 and abs(hot[3] - np.log(4.0)) < 1e-5
      and abs(hot[2] - 0.5) < 1e-3, "S -> 0 for T -> 0; S -> ln 4, E -> 1/2 for T "
      "-> infinity")
check(np.all(C_V >= 0.0), "the heat capacity is never negative")
```

For 150 temperatures from $0.02$ to 3: the table of $E$, $S$, $F$ (`[2:]` keeps the last three entries of the tuple) and $C_V = T\,dS/dT$. The limits: at the lowest temperature $S < 10^{-8}$ (the particle sits in level 0); at $T = 1000$, practically infinite, both occupations are $\tfrac12$, so $S = 2\ln 2 = \ln 4$ and $E = \tfrac12$. The second check: $C_V \ge 0$ everywhere.

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(temperatures, table[:, 0], label="energy $E$")
left.plot(temperatures, temperatures * table[:, 1], label="$T S$")
left.plot(temperatures, table[:, 2], color="black", label="free energy $F = E - TS$")
left.set_xlabel("temperature $T$")
left.set_ylabel("energy (level-spacing units)")
left.legend(fontsize=8)
```

`table[:, 0]` is the first column of the table (all rows), the energy; `temperatures * table[:, 1]` multiplies each entropy by its temperature; `table[:, 2]` is the free energy, drawn in black. Labels and legend of the left panel.

```python
right.plot(temperatures, C_V, color="tab:red")
right.plot([0.5], [0.393224], "ko", label="$T = 1/2$: $C_V = 0.393224$")
right.set_xlabel("temperature $T$")
right.set_ylabel("heat capacity $C_V = dE/dT$")
right.legend(fontsize=8)
fig.suptitle("Two levels (0 and 1), one particle")
save_figure(fig, "two_level_thermo",
```

The right panel draws $C_V$ in red and the worked value at $T = \tfrac12$ as a black dot; then labels, legend, a title above both panels, and `save_figure` for Figure 13e.4.

**What Figure 13e.4 shows.** On the left, at low temperature $E$, $TS$ and $F$ are all near 0 (the particle sits in the lower level). As $T$ grows, $E$ rises towards $\tfrac12$ (both levels equally occupied), $TS$ grows almost linearly (towards $T\ln4$: the entropy $S_s$ approaches $2\ln2 = \ln4$, the value for two independent orbitals that are each occupied with the probability $\tfrac12$, Exercise 7), and $F = E - TS$ falls ever more steeply, with the slope $-S$. On the right, the heat capacity is practically 0 below $T = 0.05$, rises to a single peak of about $0.88$ near $T = 0.21$, passes through the black dot at $T = \tfrac12$, and decreases slowly towards 0: energy can be absorbed only while the upper level is filling up.

**In [12], a ladder of levels.**

```python
ladder = np.arange(60) + 0.5
twos = 2.0 * np.ones(60)
N_LADDER = 8.0


def ladder_at(T):
    return thermodynamics(ladder, twos, N_LADDER, T)


def variance_heat_capacity(T):
    """C_V = [sum w x^2 - (sum w x)^2 / sum w] / T^2, x = eps - mu, w = g f (1 - f)."""
    mu, f = ladder_at(T)[:2]
    w = twos * f * (1.0 - f)
    x = ladder - mu
    return (np.sum(w * x * x) - np.sum(w * x) ** 2 / np.sum(w)) / T ** 2
```

The levels $n + \tfrac12$, $n = 0, \dots, 59$, two states each, eight particles: the trap of Notebook 13a without interaction. `variance_heat_capacity` is the variance formula of Section 13.26.

```python
T_ladder = np.linspace(0.05, 3.0, 120)
mus = np.array([ladder_at(T)[0] for T in T_ladder])
C_numeric = np.array([(ladder_at(T + d)[2] - ladder_at(T - d)[2]) / (2 * d)
                      for T in T_ladder])
C_variance = np.array([variance_heat_capacity(T) for T in T_ladder])
```

For 120 temperatures from $0.05$ to 3: $\mu$, the heat capacity as a difference quotient of $E$ (the step `d` $= 10^{-4}$ of In [10]), and the variance formula.

```python
report("mu at T = 0.05", f"{mus[0]:.6f}")
check(abs(mus[0] - 4.0) < 1e-6, "at low T, mu lies halfway between 3.5 and 4.5")
check(np.max(np.abs(C_numeric - C_variance)) < 1e-5 * max(1.0, C_variance.max()),
      "the heat capacity equals the weighted-variance formula")
check(np.all(C_variance >= 0.0), "the variance formula is never negative")
```

The cell prints $\mu = 4.000000$ at $T = 0.05$ and checks it (at low temperature the four lowest levels are full, and by the symmetry of $f$ about $\mu$ the chemical potential lies halfway between the last full level $3.5$ and the first empty one $4.5$), then that the two heat capacities agree to $10^{-5}$ times the larger of 1 and the largest value (`max` of two numbers is the larger), and that the variance formula is never negative.

**In [13], the occupations of the ladder.**

```python
fig, ax = plt.subplots()
for T, marker in ((0.05, "o"), (0.5, "s"), (1.0, "^"), (2.0, "v")):
    mu, f = ladder_at(T)[:2]
    ax.plot(ladder[:12], f[:12], marker + "-", ms=4,
            label=f"$T = {T}$, $\\mu = {mu:.3f}$")
ax.set_xlabel("level $\\epsilon_n = n + 1/2$")
ax.set_ylabel("occupation $f_n$ of each of the two states")
ax.set_title("Eight particles in a ladder of levels")
ax.legend(fontsize=8)
save_figure(fig, "ladder_occupations",
```

For $T = 0.05, 0.5, 1, 2$ the loop computes $\mu$ and the occupations (`[:2]` keeps the first two returned values) and draws the occupations of the twelve lowest levels against their energies; `marker + "-"` joins a marker letter and a line style into one style string, and the label shows $T$ and $\mu$ with three decimals. Labels, title, legend and `save_figure` for Figure 13e.5.

**What Figure 13e.5 shows.** At $T = 0.05$ the occupation is 1 for the levels $0.5$ to $3.5$ and 0 above: a perfect step between $3.5$ and $4.5$. At $T = 0.5$ the levels $3.5$ and $4.5$ are partly occupied ($0.73$ and $0.27$). At $T = 1$ and 2 the step is smeared over several levels, and particles reach the levels $8.5$ and beyond. The chemical potential stays at $4.000$ up to $T = 0.5$ and falls to $3.982$ at $T = 1$ and $3.712$ at $T = 2$: the ladder continues upwards but not downwards (no level below $0.5$), so at high temperature the particles spread more to higher levels, and $\mu$ must fall to keep the number at 8.

**In [14], the chemical potential and the heat capacity of the ladder.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(T_ladder, mus, color="black")
left.set_xlabel("temperature $T$")
left.set_ylabel("chemical potential $\\mu$")
right.plot(T_ladder, C_numeric, color="tab:red", label="$dE/dT$ (differences)")
right.plot(T_ladder[::6], C_variance[::6], "ko", ms=3, label="variance formula")
right.set_xlabel("temperature $T$")
right.set_ylabel("heat capacity $C_V$")
right.legend(fontsize=8)
fig.suptitle("Ladder of levels, eight particles")
save_figure(fig, "ladder_thermo",
```

Left: $\mu$ against $T$. Right: the heat capacity from the difference quotient as a red line and from the variance formula at every sixth temperature (`[::6]`) as black dots, so that both can be seen; labels, legend, a common title and `save_figure` for Figure 13e.6.

**What Figure 13e.6 shows.** On the left, $\mu$ stays at 4 up to about $T = 0.5$ and then falls, to about $3.1$ at $T = 3$. On the right, the black dots lie on the red line at every temperature: the difference quotient and the weighted-variance formula agree, and both are positive. The heat capacity is nearly 0 at $T = 0.05$ (a gap of one level spacing separates the full from the empty levels), rises steeply, and approaches 8, one unit per particle, at high temperature, where each particle behaves like a classical oscillator.

**In [15], Janak's theorem and Delta-SCF.**

```python
EPS_H0, EPS_L0, U_MODEL = 0.0, 1.0, 0.2


def model_energy(f_H, f_L):
    return EPS_H0 * f_H + EPS_L0 * f_L + 0.5 * U_MODEL * (f_H ** 2 + f_L ** 2)


def model_levels(f_H, f_L):
    """Janak: eps_a = dE/df_a = eps_a^0 + U f_a."""
    return EPS_H0 + U_MODEL * f_H, EPS_L0 + U_MODEL * f_L
```

The model energy of Section 13.27 and its levels.

```python
h_step = 1e-6
for f_H, f_L in ((1.0, 0.0), (0.5, 0.5), (0.3, 0.9)):
    dE_dfH = (model_energy(f_H + h_step, f_L) - model_energy(f_H - h_step, f_L)) \
        / (2 * h_step)
    dE_dfL = (model_energy(f_H, f_L + h_step) - model_energy(f_H, f_L - h_step)) \
        / (2 * h_step)
    check(np.allclose((dE_dfH, dE_dfL), model_levels(f_H, f_L), atol=1e-9),
          f"Janak: dE/df_a = eps_a at (f_H, f_L) = ({f_H}, {f_L})")
```

At three pairs of occupations the derivatives of the energy are computed as central difference quotients and compared with the levels (three checks).

```python
taus = np.linspace(0.0, 1.0, 101)
integrand = np.array([model_levels(1 - t, t)[1] - model_levels(1 - t, t)[0]
                      for t in taus])
gap_KS = integrand[0]
delta_SCF = model_energy(0.0, 1.0) - model_energy(1.0, 0.0)
step = taus[1] - taus[0]
janak_integral = step / 3 * (integrand[0] + integrand[-1]
                             + 4 * integrand[1:-1:2].sum() + 2 * integrand[2:-1:2].sum())
```

101 values of the transferred fraction $\tau$; the level difference $\epsilon_L(\tau) - \epsilon_H(\tau)$ at $(f_H, f_L) = (1 - \tau, \tau)$ (the function `model_levels` returns the pair $(\epsilon_H, \epsilon_L)$, so `[1]` is $\epsilon_L$ and `[0]` is $\epsilon_H$); the gap (its value at $\tau = 0$); the Delta-SCF energy $E(0, 1) - E(1, 0)$; and the integral of the level difference by Simpson's rule (Section 13.15) on the 101 values.

```python
report("Kohn-Sham gap", f"{gap_KS:.6f}")
report("Delta-SCF", f"{delta_SCF:.6f}")
report("integral of eps_L - eps_H over tau", f"{janak_integral:.6f}")
report("transition state (tau = 1/2)", f"{integrand[50]:.6f}")
check(abs(gap_KS - 0.8) < 1e-12 and abs(delta_SCF - 1.0) < 1e-12
      and abs(janak_integral - delta_SCF) < 1e-12 and abs(integrand[50] - 1.0) < 1e-12,
      "gap 0.8, Delta-SCF 1.0 = the Janak integral = the transition state")
check(abs(delta_SCF - gap_KS - U_MODEL) < 1e-12, "Delta-SCF - gap = U (relaxation)")
```

The `report` lines print $0.800000$, $1.000000$, $1.000000$ and the transition-state value $1.000000$ (entry 50 is $\tau = \tfrac12$). The last two checks require these four values (Simpson's rule is exact here, because the integrand is a straight line) and $\Delta_{SCF} - \Delta_{KS} = U$.

**In [16], the transfer as a picture.**

```python
energies_tau = np.array([model_energy(1 - t, t) for t in taus])
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.plot(taus, energies_tau - energies_tau[0], color="black")
left.set_xlabel("transferred fraction $\\tau$")
left.set_ylabel("$E(\\tau) - E(0)$")
left.set_title("energy along the transfer")
```

`energies_tau` is the model energy $E(1 - \tau, \tau)$ at every $\tau$; the left panel draws its rise $E(\tau) - E(0)$ in black, with labels and a title.

```python
right.fill_between(taus, 0.0, integrand, alpha=0.25, label="area = Delta-SCF = 1")
right.plot(taus, integrand, color="black", label="$\\epsilon_L - \\epsilon_H$")
right.plot([0.0], [gap_KS], "s", ms=8, label="Kohn-Sham gap 0.8")
right.plot([0.5], [integrand[50]], "^", ms=8, label="transition state 1.0")
right.set_ylim(0.0, 1.3)
right.set_xlabel("transferred fraction $\\tau$")
right.set_ylabel("level difference")
right.legend(fontsize=8, loc="lower right")
```

`right.fill_between(taus, 0.0, integrand, ...)` shades the area between the zero line and the level difference (`alpha=0.25`: light), which by Janak's theorem is the Delta-SCF energy; the level difference itself as a black line; the gap as a large square at $\tau = 0$ and the transition state as a large triangle at $\tau = \tfrac12$; the vertical range from 0 to $1.3$; labels and a legend in the lower right corner.

```python
fig.suptitle("Janak's theorem and Delta-SCF ($\\epsilon_H^0 = 0$, "
             "$\\epsilon_L^0 = 1$, $U = 0.2$)")
save_figure(fig, "janak_delta_scf",
```

A title above both panels (two strings joined into one) with the parameters of the model, and `save_figure` for Figure 13e.7.

**What Figure 13e.7 shows.** On the left the energy rises from 0 to $1.0$ as one whole particle is moved from H to L, slightly curved upwards, because its slope, the level difference, grows with $\tau$. On the right that slope is the straight line $0.8 + 0.4\tau$ from the gap $0.8$ (square) to $1.2$; the shaded area under it is $1.0$, the Delta-SCF energy, and the value at the midpoint (triangle) is also exactly $1.0$, because the line is straight. The gap underestimates the excitation energy by $U = 0.2$, the orbital relaxation of this model.

**In [17], the last check.**

```python
figure_names = ["gibbs_principle", "fermi_dirac", "bisection", "two_level_thermo",
                "ladder_occupations", "ladder_thermo", "janak_delta_scf"]
missing = [name for k, name in enumerate(figure_names, 1)
           if not output_file(f"{FIGURE_FOLDER}/13e_{k}_{name}.png").is_file()]
check(missing == [], "all seven figure files exist")
check(output_file(f"{FIGURE_FOLDER}/13e_7_janak_delta_scf.png").is_file(),
      "the figure file 13e_7_janak_delta_scf.png exists")
all_checks_passed()
```

The same lines as In [19] of Notebook 13c (Section 13.14), with the seven figure names of this notebook. The last line prints ALL 24 CHECKS PASSED (notebook 13e): one check each in In [2], In [3], In [6], In [7] and In [9], two each in In [4], In [8] and In [11], three each in In [10] and In [12], five in In [15] and two in In [17].

### 13.32 A complete Kohn-Sham calculation: eight fermions in a trap

This section puts every piece of the chapter together in one small but complete Kohn-Sham calculation, the example of Notebook 13a. It is a teaching model: its numbers are COMPUTED by the notebook and belong to no physical system of the book. (Its letter $x$ is the position on a line, not a spacetime coordinate.)

**The model.** $N = 8$ identical fermions on a line, four with the label up and four with the label down, in the **harmonic trap** $v(x) = x^2/2$, with the contact repulsion $w(x, x') = g_c\,\delta(x - x')$ of strength $g_c = 2$. Units: $\hbar = m = \omega = 1$, where $\omega$ is the angular frequency of the trap; energies are in units of $\hbar\omega$ and lengths in units of $\sqrt{\hbar/(m\omega)}$. Without interaction a particle in the trap has the levels $\tfrac12, \tfrac32, \tfrac52, \dots$, and the ground state of the eight fermions fills the four lowest levels with two fermions each: $E = 2(\tfrac12 + \tfrac32 + \tfrac52 + \tfrac72) = 16$.

**The energy functional.** With the four lowest orbitals $\phi_0, \dots, \phi_3$ each occupied by one up and one down fermion, the density is $n = 2\sum_{a=0}^{3}\phi_a^2$ with $n_\uparrow = n_\downarrow = n/2$, and the energy of the determinant is (Section 13.5)

$$
E = T_s + \int v\,n\,dx + E_H + E_x, \qquad E_H = \frac{g_c}{2}\int n^2\,dx, \qquad E_x = -\frac{g_c}{2}\int\big(n_\uparrow^2 + n_\downarrow^2\big)dx = -\frac{g_c}{4}\int n^2\,dx ,
$$

with $T_s = 2\sum_{a=0}^{3}\int\phi_a\,(-\tfrac12\phi_a'')\,dx$. For a contact interaction the exchange of a determinant is exactly this local formula (Section 13.5); the correlation energy is left out. So this is an **exchange-only** Kohn-Sham scheme, which for a contact interaction is the same as the Hartree-Fock approximation: an approximation to the true ground state, whose error is the correlation energy (Section 13.7 showed how large it can be on two sites).

**The Kohn-Sham potential, line by line.** The functional derivatives are

$$
\frac{\delta E_H}{\delta n} = g_c\,n, \qquad \frac{\delta E_x}{\delta n_\uparrow} = -g_c\,n_\uparrow = -\frac{g_c}{2}\,n ,
$$

by example (i) of Section 13.9 (for $E_x$ applied to the up density, with the down density held fixed). A fermion with label up therefore feels

$$
v_s = v + g_c\,n - \frac{g_c}{2}\,n = v + w, \qquad w = \frac{g_c}{2}\,n ,
$$

the Hartree push of everybody minus the exchange with its own label, and the same holds for label down. $w$ is the **mean-field potential**. A solution of the Kohn-Sham equations is a $w$ for which the orbitals of $v + w$ give back $w_{out} = g_c n/2 = w$; the **residual** of one pass is $r = \max_x|w_{out}(x) - w(x)|$, and the loop stops when $r \le 10^{-11}$, the stopping rule of the Revision solver (Section 13.21).

**The energy, two ways, line by line.** Multiply the Kohn-Sham equation of orbital $a$ by $\phi_a$, integrate and sum with the occupation 2:

$$
\begin{aligned}
2\sum_{a=0}^{3}\epsilon_a &= T_s + \int v_s\,n\,dx = T_s + \int v\,n\,dx + \frac{g_c}{2}\int n^2\,dx ,\\
E &= T_s + \int v\,n\,dx + \frac{g_c}{4}\int n^2\,dx = 2\sum_{a=0}^{3}\epsilon_a - \frac{g_c}{4}\int n^2\,dx = 2\sum_{a=0}^{3}\epsilon_a - (E_H + E_x) .
\end{aligned}
$$

The first line is the computation of Section 13.10 with $v_s = v + g_c n/2$; the second writes $E_H + E_x = \tfrac{g_c}{4}\int n^2$ and subtracts the first line. This **double-counting formula** gives the same energy as the direct sum of the four parts, which the notebook checks.

**Stability of the equal-label solution.** So far the up and down densities were forced to be equal. Would the fermions lower their energy by separating the labels, as on two sites at strong repulsion (Section 13.7)? Let each label have its own potential: a fermion with label up feels $v + g_c n - g_c n_\uparrow = v + g_c n_\downarrow$, and one with label down $v + g_c n_\uparrow$, and the energy is $E = T_s + \int v\,n + g_c\int n_\uparrow n_\downarrow$ (Section 13.5). Started from a strongly separated guess, the loop for the two potentials together may return to equal densities; but that alone does not show stability, because the loop can also converge to a **saddle**: a self-consistent solution from which some change of the densities LOWERS the energy. Only the energy decides: the equal-label solution is a minimum when every small label-separating change raises the energy. Notebook 13a shows both cases: on two sites with $U = 4t$ the loop started from a small separation converges to the equal labels although separating them lowers the energy (a saddle), and in the trap every label-separating trial family raises the energy, quadratically for small separations (a minimum along these families).

**The variational principle at work.** The Kohn-Sham equations make the energy stationary in the orbitals, and for the ground state the stationary point is a minimum. A one-parameter test: for each number $c$, take the four lowest orbitals of the trial potential $v + c\,n_{scf}$ ($n_{scf}$ the self-consistent density) and evaluate the same energy formula with them. At $c = g_c/2 = 1$ these are the self-consistent orbitals; the energy must be smallest there, and near the minimum the curve is flat (a small error in the orbitals makes only a second-order error in the energy).

**Three simpler pictures.** (a) **No interaction**: $w = 0$. (b) **Hartree only**: drop the exchange, $v_s = v + g_c n$; every fermion is then also repelled by its own density (the self-interaction of Section 13.5). (c) **Thomas-Fermi**: the kinetic energy of each small piece of the line is that of a uniform gas with the local density. For a uniform gas on a line with two labels, the plane waves with $|k| < k_F$ are filled, two per wave number, and in a box of length $\ell$ the wave numbers are spaced by $2\pi/\ell$; line by line:

$$
\begin{aligned}
N &= 2\cdot\frac{2k_F}{2\pi/\ell} = \frac{2k_F\,\ell}{\pi} \quad\Longrightarrow\quad n = \frac{2k_F}{\pi} ,\\
\frac{E_{kin}}{\ell} &= 2\int_{-k_F}^{k_F}\frac{dk}{2\pi}\,\frac{k^2}{2} = \frac{1}{2\pi}\cdot\frac{2k_F^3}{3} = \frac{k_F^3}{3\pi} = \frac{\pi^2\,n^3}{24} .
\end{aligned}
$$

The first line counts the occupied wave numbers (the interval of length $2k_F$ divided by the spacing, times two labels) and divides by $\ell$; the second sums $k^2/2$ over them per unit length (a sum over wave numbers becomes $\ell\int dk/(2\pi)$), integrates ($\int_{-k_F}^{k_F}k^2\,dk = 2k_F^3/3$), and inserts $k_F = \pi n/2$. Minimising $\int[\pi^2 n^3/24 + v\,n + \tfrac{g_c}{4}n^2]\,dx$ at fixed $\int n\,dx = N$ with the multiplier $\mu$ (Section 13.9) gives, where $n > 0$,

$$
\frac{\pi^2}{8}\,n^2 + \frac{g_c}{2}\,n = \mu - v(x) \quad\Longrightarrow\quad n = \frac{-b + \sqrt{b^2 + 4a\,(\mu - v)}}{2a}, \qquad a = \frac{\pi^2}{8},\ b = \frac{g_c}{2} ,
$$

the positive root of a quadratic equation at each point, and $n = 0$ where $v > \mu$; $\mu$ is found by bisection so that the density holds 8 particles. Thomas-Fermi uses no orbitals, so it cannot show the four bumps of the Kohn-Sham density (its **shell structure**).

**The Hellmann-Feynman theorem.** How does the energy change with the strength $g_c$? The Kohn-Sham energy is $E(g_c) = \mathcal E[\phi^*(g_c); g_c]$, the functional evaluated at its stationary orbitals $\phi^*$. By the chain rule, $dE/dg_c = \partial\mathcal E/\partial g_c + \sum(\text{derivative with respect to the orbitals})\cdot d\phi^*/dg_c$, and the second part vanishes because $\mathcal E$ is stationary in the orbitals (with their normalisation kept), exactly as in the envelope theorem of Section 13.26. Only the explicit dependence remains, $E_H + E_x = \tfrac{g_c}{4}\int n^2$:

$$
\frac{dE}{dg_c} = \frac14\int n^2\,dx .
$$

**The virial theorem at $g_c = 0$.** For a particle in the harmonic trap the kinetic and the trap energy of every level are equal. Line by line, for a normalised stationary state $\phi$: the stretched states $\phi_\lambda(x) = \sqrt\lambda\,\phi(\lambda x)$ are normalised, their kinetic energy is $\lambda^2 T$ and their trap energy $V/\lambda^2$ (substitute $y = \lambda x$ in the integrals), so $E(\lambda) = \lambda^2 T + V/\lambda^2$. A stationary state makes the energy stationary under every change of the state, in particular under stretching, so $dE/d\lambda = 2\lambda T - 2V/\lambda^3 = 0$ at $\lambda = 1$, that is $T = V$. At $g_c = 0$ the kinetic and the trap energy of the eight fermions are therefore equal, $8$ each.

**The first excited state.** The Kohn-Sham gap is $\epsilon_4 - \epsilon_3$ of the ground state. The Delta-SCF energy moves one up fermion from orbital 3 (HOMO) to orbital 4 (LUMO) and solves the loop again (Section 13.27). By Janak's theorem it equals the integral of $\epsilon_4(\tau) - \epsilon_3(\tau)$ over the moved fraction $\tau$ from 0 to 1, which the notebook computes with Simpson's rule on nine values of $\tau$.

**What the notebook finds (COMPUTED, Notebook 13a).** The grid (200 points in $-6 < x < 6$) reproduces the levels $n + \tfrac12$ of the trap to $0.013$ (In [3]; an error of order $h^2$, Section 13.2). Plain iteration needs 40 passes, linear mixing with $\beta = 0.7$ needs 23 and with $\beta = 0.3$ needs 73 (In [6]), Anderson mixing with the Revision settings 19 (In [8]); all reach the same potential to $10^{-9}$ (Figure 13a.2), and plain iteration overshoots: the first density is too narrow, the second too wide (In [10], Figure 13a.3). The Kohn-Sham levels are $2.119598$, $3.006214$, $3.877952$, $4.723945$ (occupied) and $5.496606$ (LUMO) (In [11]). The energy is $E = 21.851498$ by both formulas, made of $T_s = 6.726297$, $\int v\,n = 9.521279$, $E_H = 11.207843$ and $E_x = -5.603922 = -E_H/2$ (In [14]). From a strongly separated start the two-label loop returns to equal labels (In [16]); the energy test shows that along three label-separating families the equal-label solution is a minimum, while on two sites with $U = 4t$ the loop converges to a saddle (In [17], In [18], Figure 13a.6). In the trial family the lowest energy is at $c = 1.00$ (In [19], Figure 13a.7). The root-mean-square widths of the cloud are $1.413346$ (no interaction), $1.542829$ (Kohn-Sham) and $1.659857$ (Hartree only): the repulsion spreads the cloud, and the self-interaction of Hartree spreads it too much (In [21], Figure 13a.8). $dE/dg_c = 2.801961$ both as a difference quotient and as $\tfrac14\int n^2$ (In [23]). The Kohn-Sham gap is $0.772662$, the Delta-SCF energy $0.714594$ (equal to the Janak integral), and the transition-state estimate $0.712784$ (In [25]): here the orbital relaxation lowers the excitation energy.

### 13.33 Example: the one-dimensional Kohn-Sham toy

Notebook 13a carries out the calculation of Section 13.32 from the first line to the last: the grid and its check against the exact levels of the trap; the Kohn-Sham map; plain iteration, linear mixing and Anderson mixing with exactly the settings of the Revision Kohn-Sham solver, read from its parameter file (its only link to the Revision record); the converged state with its potentials and density; the energy two ways and the functional-derivative test; the stability of the equal-label solution; the variational principle; the Hartree and Thomas-Fermi comparisons; the switching-on of the interaction with the Hellmann-Feynman theorem; and the first excited state by Delta-SCF with Janak's theorem. It ends with ALL 31 CHECKS PASSED (notebook 13a) and draws nine figures.

<!-- NOTEBOOK 13a -->

### 13.36 Line-by-line walk-through of Notebook 13a

The notebook has 25 code cells. **In [1]** is the set-up cell, identical to In [1] of Notebook 13c (Section 13.14) except for the name `"13a"` and its comment lines, which hold the instructions of Section 13.34.

**In [2], the grid and the kinetic-energy matrix.**

```python
import numpy as np  # arrays of numbers, matrices and linear algebra

L_HALF = 6.0  # the grid covers -6 < x < 6
M = 200  # the number of interior grid points
h = 2.0 * L_HALF / (M + 1)  # the grid spacing 12/201
x = -L_HALF + h * np.arange(1, M + 1)  # the grid points x_k, k = 1, ..., 200
v = 0.5 * x ** 2  # the harmonic trap v(x) = x^2/2 at every point
```

The interval from $-6$ to $6$ is cut into 201 equal steps of length $h = 12/201 = 0.059701$; the 200 inner points are the grid (`np.arange(1, M + 1)` is $1, \dots, 200$), and the orbitals vanish at the two ends $x = \pm6$ (hard walls; the occupied orbitals are negligibly small there anyway). `v` is the trap at every grid point.

```python
T = (np.diag(np.full(M, 1.0 / h ** 2))
     + np.diag(np.full(M - 1, -0.5 / h ** 2), 1)
     + np.diag(np.full(M - 1, -0.5 / h ** 2), -1))
say(f"grid: {M} points, spacing h = {h:.6f}")
check(np.allclose(T, T.T), "the kinetic-energy matrix is symmetric")
```

`np.full(M, value)` is a list of $M$ equal values and `np.diag(list, k)` the matrix with this list on the diagonal shifted by $k$ places ($k = 1$ above, $k = -1$ below the main diagonal). So `T` is the matrix of $-\tfrac12\,d^2/dx^2$ of Section 13.2: $1/h^2$ on the diagonal and $-1/(2h^2)$ beside it. The check confirms that it is symmetric, hence Hermitian.

**In [3], the levels and orbitals of one particle.**

```python
def orbitals(w):
    """Levels (increasing) and orbitals (columns, int phi^2 dx = 1) of T + v + w."""
    levels, vectors = np.linalg.eigh(T + np.diag(v + w))
    phi = vectors / np.sqrt(h)  # normalise to sum phi^2 h = 1
    for a in range(M):  # fix the sign of every orbital
        first = np.argmax(np.abs(phi[:, a]) > 1e-3 * np.abs(phi[:, a]).max())
        phi[:, a] *= np.sign(phi[first, a])
    return levels, phi
```

`orbitals(w)` diagonalises the Kohn-Sham Hamiltonian on the grid, the matrix $T + \mathrm{diag}(v + w)$ for a mean-field potential $w$, and returns its 200 levels in increasing order and the orbitals as the columns of a matrix. numpy returns eigenvectors with $\sum_k u_k^2 = 1$; dividing by $\sqrt h$ makes $\sum_k\phi_k^2\,h = 1$, the grid form of $\int\phi^2\,dx = 1$. An eigenvector is fixed only up to its sign, so the loop makes the first clearly nonzero value of each orbital (counted from the left) positive: the comparison gives a list of true and false values, `np.argmax` returns the place of its first true value, and multiplying the column by the sign of the value there (`*=`, `np.sign`) makes that value positive. So every run draws the same pictures.

```python
free_levels, free_phi = orbitals(np.zeros(M))  # no interaction: w = 0
exact_levels = np.arange(8) + 0.5  # 1/2, 3/2, ..., 15/2
for a in range(8):
    say(f"level {a}: grid {free_levels[a]:.6f}   exact {exact_levels[a]:.1f}")
check(np.max(np.abs(free_levels[:8] - exact_levels)) < 0.02,
      "the grid reproduces the levels n + 1/2 of the trap within 0.02")
overlaps = free_phi[:, :8].T @ free_phi[:, :8] * h  # sum_k phi_a phi_b h
check(np.allclose(overlaps, np.eye(8), atol=1e-12),
      "the orbitals are orthonormal on the grid")
```

Without interaction the eight lowest grid levels are printed beside the exact levels $n + \tfrac12$: $0.499889$ against $0.5$, ..., $7.487394$ against $7.5$. The first check allows $0.02$ (the difference formula makes errors of order $h^2$, growing with the level). `free_phi[:, :8]` keeps the first eight columns; the matrix of their sums $\sum_k\phi_a(x_k)\phi_b(x_k)\,h$ must be the unit matrix: the orbitals are orthonormal on the grid (second check).

**In [4], the trap and its orbitals as a picture.**

```python
fig, ax = plt.subplots(figsize=(7.0, 4.6))
ax.plot(x, v, color="black", label="trap $v(x) = x^2/2$")
for a in range(6):
    style = "-" if a < 4 else ":"  # occupied: solid; empty: dotted
    ax.axhline(free_levels[a], color="gray", lw=0.6, ls="--")
    ax.plot(x, free_levels[a] + 0.6 * free_phi[:, a], style,
            label=f"orbital {a}" + (" (occupied)" if a < 4 else " (empty)"))
```

`plt.subplots(figsize=(7.0, 4.6))` makes a figure slightly taller than the standard one. The trap is drawn in black. For each of the six lowest levels the loop chooses a solid line for the four occupied levels and a dotted line for the two empty ones (`style = "-" if a < 4 else ":"`), draws a thin dashed grey horizontal line at the level, and draws the orbital around it: `free_levels[a] + 0.6 * free_phi[:, a]` is 0.6 times the orbital, shifted up by its level, so that each orbital sits on its own energy. The label joins two strings with `+`: the orbital number and either " (occupied)" or " (empty)".

```python
ax.set_xlim(-5.0, 5.0)
ax.set_ylim(0.0, 8.4)  # room above the orbitals for the legend
ax.set_xlabel("position $x$")
ax.set_ylabel("energy (units of $\\hbar\\omega$)")
ax.set_title("Levels and orbitals of one particle in the trap (no interaction)")
ax.legend(fontsize=7, loc="upper center", ncol=3)
save_figure(fig, "trap_orbitals",
```

`set_xlim` and `set_ylim` fix the ranges of the axes: positions from $-5$ to 5 and energies from 0 to $8.4$, which leaves room at the top for the legend, written in three columns (`ncol=3`) at the upper centre. Labels, title, and `save_figure` for Figure 13a.1.

**What Figure 13a.1 shows.** The parabola $x^2/2$ and the six levels $0.5, 1.5, \dots, 5.5$, equally spaced by 1. Orbital 0 is a single bump, orbital 1 changes sign once, and in general orbital $a$ has $a$ zeros; each orbital is large where the level lies above the parabola (the region a classical particle of that energy could reach) and dies away quickly outside it. The eight fermions fill the four lowest levels (solid), two per level.

**In [5], the Kohn-Sham map.**

```python
G_C = 2.0  # the strength g_c of the contact repulsion
N_PER_LABEL = 4  # four fermions with label up and four with label down
N_TOTAL = 2 * N_PER_LABEL


def integral(f):
    """The integral of f over the line, as the sum of f_k h."""
    return float(np.sum(f) * h)


def density(phi):
    """n(x) = 2 (phi_0^2 + phi_1^2 + phi_2^2 + phi_3^2): two fermions per orbital."""
    return 2.0 * np.sum(phi[:, :N_PER_LABEL] ** 2, axis=1)


def ks_map(w):
    """One pass of the loop: the mean-field potential g_c n / 2 made from w."""
    levels, phi = orbitals(w)
    return 0.5 * G_C * density(phi)
```

The model's numbers; `integral(f)` approximates $\int f\,dx$ by $\sum_k f_k h$ (accurate here because the functions vanish at the walls); `density(phi)` adds the squares of the four lowest orbitals along each row (`axis=1`) and doubles them; `ks_map(w)` is one pass of the loop of Section 13.32, $w \to$ orbitals $\to n \to w_{out} = g_c n/2$.

```python
w_first = ks_map(np.zeros(M))  # one pass, starting from no interaction
report("largest value of the first mean-field potential", f"{w_first.max():.6f}")
check(abs(integral(2.0 * w_first / G_C) - N_TOTAL) < 1e-10,
      "the density of one pass holds exactly 8 particles")
```

One pass from $w = 0$ gives a mean-field potential with the largest value $1.887848$; its density $n = 2w/g_c$ must hold 8 particles.

**In [6], plain iteration and linear mixing.**

```python
def linear_mixing(beta, tolerance=1e-11, max_passes=150):
    """Linear mixing w <- w + beta (w_out - w), starting from w = 0."""
    w = np.zeros(M)
    residuals, first_densities = [], []
    for _ in range(max_passes):
        w_out = ks_map(w)
        residuals.append(np.max(np.abs(w_out - w)))  # the residual r
        if len(first_densities) < 5:
            first_densities.append(2.0 * w_out / G_C)  # n = 2 w_out / g_c
        if residuals[-1] <= tolerance:
            break
        w = w + beta * (w_out - w)
    return w, residuals, first_densities
```

Linear mixing of Section 13.21 for the potential: start at $w = 0$; in each pass compute $w_{out}$, record the residual $\max_x|w_{out} - w|$, keep the densities of the first five passes for the figure of In [10], stop when the residual is at most $10^{-11}$, otherwise mix. The function returns the last $w$, the residuals and the first densities.

```python
runs = {}
for beta in (1.0, 0.7, 0.3):
    runs[beta] = linear_mixing(beta)
    say(f"beta = {beta}: {len(runs[beta][1])} passes, last residual "
        f"{runs[beta][1][-1]:.1e}")
check(all(run[1][-1] <= 1e-11 for run in runs.values()),
      "plain iteration and linear mixing with beta = 0.7 and 0.3 all converge")
```

Three runs, stored in the dictionary `runs` under their $\beta$: 40 passes for plain iteration, 23 for $\beta = 0.7$, 73 for $\beta = 0.3$. The check requires every last residual to be at most $10^{-11}$. (Unlike the two-site model of Section 13.21, plain iteration converges here, slowly.)

**In [7], the settings of the Revision solver.**

```python
parameters = json.loads(repository_file(
    "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
numerics = parameters["numerics"]  # the numerical settings of the Revision solver
DEPTH = int(numerics["andersonDepth"])  # how many earlier passes are remembered
BETA_ANDERSON = float(numerics["andersonBeta"])  # the mixing parameter
TOLERANCE = float(numerics["scfTolerance"])  # the stopping rule
```

The cell reads the parameter file of the Revision Kohn-Sham solver and from its part "numerics" the number of remembered passes, $\beta$ and the stopping rule.

```python
say(f"Revision solver settings: depth {DEPTH}, beta {BETA_ANDERSON}, "
    f"tolerance {TOLERANCE:.0e}")
check(DEPTH == 6 and BETA_ANDERSON == 0.4 and abs(TOLERANCE - 1e-11) < 1e-24,
      "the Revision solver mixes with depth 6, beta 0.4 and stops at 1e-11 "
      "(Revision/kohn_sham/results/parameters.json, numerics)")
```

The printed line (`:.0e` writes a number as a power of ten without decimals) and the check confirm 6, $0.4$ and $10^{-11}$ (the file stores the tolerance as the floating-point number nearest to $10^{-11}$, so the check allows a difference below $10^{-24}$).

**In [8], Anderson mixing.**

```python
def anderson(step, w0, beta=BETA_ANDERSON, depth=DEPTH, tolerance=TOLERANCE,
             max_passes=400):
    """Anderson mixing for the fixed point step(w) = w, starting from w0."""
    w = np.array(w0, dtype=float)
    inputs, residual_vectors, residuals = [], [], []
    for _ in range(max_passes):
        residual = step(w) - w  # R = w_out - w
        residuals.append(np.max(np.abs(residual)))
        if residuals[-1] <= tolerance:
            return w, residuals
        inputs = (inputs + [w.copy()])[-depth:]  # keep the last `depth` passes
        residual_vectors = (residual_vectors + [residual])[-depth:]
        if len(inputs) == 1:
            w = w + beta * residual  # the first pass: linear mixing
            continue
        last_r = residual_vectors[-1]
        differences = np.array([r - last_r for r in residual_vectors[:-1]]).T
        theta = np.linalg.lstsq(differences, -last_r, rcond=None)[0]
        c = np.append(theta, 1.0 - theta.sum())  # the c_i; they add up to 1
        w = sum(ci * (wi + beta * ri)
                for ci, wi, ri in zip(c, inputs, residual_vectors))
    raise RuntimeError("Anderson mixing did not converge")
```

Anderson mixing of Section 13.21 for any map `step` (here `ks_map`; below also maps of two potentials at once and maps with another strength). Each pass computes the residual vector $R = w_{out} - w$ and its largest entry, and returns when that is at most the tolerance. The last `depth` inputs and residual vectors are kept (`w.copy()` stores a copy, so later changes of `w` do not change the stored input). The first pass is linear mixing. Afterwards `differences` is the matrix whose columns are $R^{(i)} - R^{(last)}$ (200 rows, one per grid point), `np.linalg.lstsq` gives the least-squares $\theta$ of $\sum_i\theta_i(R^{(i)} - R^{(last)}) \approx -R^{(last)}$, `c` appends $1 - \sum_i\theta_i$, and the next input is $\sum_i c_i(w^{(i)} + \beta R^{(i)})$. If 400 passes are not enough, the function stops the notebook with an error.

```python
w_scf, anderson_residuals = anderson(ks_map, np.zeros(M))
say(f"Anderson mixing: {len(anderson_residuals)} passes, last residual "
    f"{anderson_residuals[-1]:.1e}")
differences = [np.max(np.abs(runs[beta][0] - w_scf)) for beta in runs]
check(max(differences) < 1e-9,
      "all four routes reach the same self-consistent potential (within 1e-9)")
check(len(anderson_residuals) < len(runs[1.0][1]),
      "Anderson mixing needs fewer passes than plain iteration")
```

Anderson mixing from $w = 0$ needs 19 passes (last residual $1.8\cdot10^{-12}$). The checks: the three linear-mixing results agree with the Anderson result to $10^{-9}$ (`for beta in runs` goes through the keys of the dictionary), and Anderson needed fewer passes than plain iteration.

**In [9], the residuals as a picture.**

```python
fig, ax = plt.subplots()
for beta, style in ((1.0, "o-"), (0.7, "s-"), (0.3, "^-")):
    name = "plain iteration" if beta == 1.0 else f"linear mixing, beta = {beta}"
    ax.semilogy(range(1, len(runs[beta][1]) + 1), runs[beta][1], style, ms=3,
                label=f"{name} ({len(runs[beta][1])} passes)")
```

For the three linear runs the loop draws the residual of every pass (`runs[beta][1]`, the list of residuals) against the pass numbers $1, 2, \dots$ (`range(1, len(...) + 1)`), on a logarithmic vertical axis, with circles, squares and triangles; the label gives the name of the run and its number of passes.

```python
ax.semilogy(range(1, len(anderson_residuals) + 1), anderson_residuals, "D-",
            ms=3, color="black",
            label=f"Anderson, depth 6, beta 0.4 ({len(anderson_residuals)} passes)")
ax.axhline(TOLERANCE, color="gray", ls="--", lw=0.8)
ax.set_xlabel("pass number")
ax.set_ylabel("residual $\\max_x |w_{out} - w|$")
ax.set_title("Self-consistency: residual versus pass ($g_c = 2$)")
ax.legend(fontsize=8)
save_figure(fig, "scf_convergence",
```

The residuals of Anderson mixing as black diamonds; a grey dashed horizontal line at the stopping rule $10^{-11}$; labels, title, legend, and `save_figure` for Figure 13a.2.

**What Figure 13a.2 shows.** All four runs start with the residual $1.89$ (the first pass from $w = 0$) and end just below the dashed line. The three linear runs are nearly straight lines on the logarithmic axis: each pass multiplies the residual by about the same factor, smallest for $\beta = 0.7$ (23 passes), larger for plain iteration (40) and largest for $\beta = 0.3$ (73). Anderson mixing falls fastest and reaches the line after 19 passes; its line is not straight, because it changes its estimate of the slope as it learns from the remembered passes.

**In [10], why plain iteration is slow.**

```python
n_scf = 2.0 * w_scf / G_C  # the self-consistent density n = 2 w / g_c
fig, ax = plt.subplots()
for number, n_pass in enumerate(runs[1.0][2][:4], 1):
    ax.plot(x, n_pass, lw=1.0, label=f"density made by pass {number}")
ax.plot(x, n_scf, color="black", lw=2.0, label="self-consistent density")
```

The self-consistent density, and the densities made by the first four passes of plain iteration (`runs[1.0][2]` is the list of first densities of the run with $\beta = 1$, and `[:4]` keeps four of them), drawn as thin lines numbered from 1 by `enumerate(..., 1)`, and the self-consistent density as a thick black line.

```python
ax.set_xlim(-5.0, 5.0)
ax.set_xlabel("position $x$")
ax.set_ylabel("density $n(x)$ (particles per unit length)")
ax.set_title("Plain iteration overshoots: the first passes")
ax.legend(fontsize=8)
save_figure(fig, "first_iterations",
```

The range of positions, labels, title, legend and `save_figure` for Figure 13a.3. Then the check

```python
check(runs[1.0][2][0].max() > n_scf.max() > runs[1.0][2][1].max(),
      "the first pass is too narrow and the second too wide (overshooting)")
```

compares the largest values of the densities: the first density, made without repulsion, is higher (narrower) than the solution, and the second is lower (wider): the density swings around the solution.

**What Figure 13a.3 shows.** The density of pass 1 (no repulsion yet) is the highest in the middle, up to about $1.89$, and the narrowest. Pass 2, made in the strong repulsion of that narrow density, is the lowest in the middle (about $1.64$) and spreads furthest out. Passes 3 and 4 lie in between, closer and closer to the thick black solution, from alternating sides. All curves cross near $x = \pm2$: the charge sloshes between the centre and the flanks, the same mechanism as in the two-site model of Section 13.21, but here the swings shrink, because the slope of the map is below 1 in size.

**In [11], the converged state.**

```python
ks_levels, ks_phi = orbitals(w_scf)
n_ks = density(ks_phi)
for a in range(6):
    status = "occupied by 2" if a < N_PER_LABEL else "empty"
    say(f"Kohn-Sham level {a}: {ks_levels[a]:.6f} ({status})")
report("Kohn-Sham HOMO level", f"{ks_levels[3]:.6f}")
report("Kohn-Sham LUMO level", f"{ks_levels[4]:.6f}")
check(abs(integral(n_ks) - N_TOTAL) < 1e-10, "the density integrates to N = 8")
check(np.max(np.abs(n_ks - n_scf)) < 1e-10,
      "the density of the final orbitals reproduces the input density")
```

The orbitals of the self-consistent potential, their density, the six lowest levels with their occupation, and the HOMO and LUMO levels ($4.723945$ and $5.496606$). The checks: the density holds 8 particles, and the orbitals of $v + w_{scf}$ give back the density $2w_{scf}/g_c$ that made $w_{scf}$: self-consistency, to $10^{-10}$.

**In [12], the potentials.**

```python
v_hartree = G_C * n_ks  # v_H = g_c n
v_exchange = -0.5 * G_C * n_ks  # v_x = -g_c n_up = -g_c n / 2
```

The Hartree potential $g_c n$ and the exchange potential $-g_c n/2$ of Section 13.32, at the self-consistent density.

```python
fig, ax = plt.subplots()
ax.plot(x, v, color="black", label="trap $v$")
ax.plot(x, v_hartree, label="Hartree $v_H = g_c n$")
ax.plot(x, v_exchange, label="exchange $v_x = -g_c n/2$")
ax.plot(x, v + v_hartree + v_exchange, lw=2.0, label="Kohn-Sham $v_s$")
for a in range(N_PER_LABEL):
    ax.axhline(ks_levels[a], color="gray", ls="--", lw=0.6)
```

The trap (black), the two potentials, and their sum $v_s = v + v_H + v_x$ as a thick line; the loop draws the four occupied Kohn-Sham levels as thin dashed grey lines.

```python
ax.set_xlim(-5.0, 5.0)
ax.set_ylim(-3.0, 9.0)
ax.set_xlabel("position $x$")
ax.set_ylabel("potential (units of $\\hbar\\omega$)")
ax.set_title("The potentials of the self-consistent state ($g_c = 2$)")
ax.legend(fontsize=8)
save_figure(fig, "ks_potentials",
```

The ranges, labels, title, legend and `save_figure` for Figure 13a.4. After the caption,

```python
check(np.allclose(v + v_hartree + v_exchange, v + w_scf, atol=1e-10),
      "v + v_H + v_x equals the self-consistent v + w")
```

checks that $v + v_H + v_x$ equals $v + w_{scf}$ at every point to $10^{-10}$.

**What Figure 13a.4 shows.** The Hartree potential is a broad plateau of about 3 with small bumps (it is twice the density), the exchange potential is the same shape upside down at half the size, and the Kohn-Sham potential $v_s$ (green, thick) is the trap lifted in the middle: its bottom is no longer at 0 but at about $1.6$, and it is flattened over $-2 < x < 2$. The four occupied levels ($2.12$, $3.01$, $3.88$, $4.72$) are pushed up and squeezed together compared with $0.5, 1.5, 2.5, 3.5$ without interaction.

**In [13], the density as a stack of orbitals.**

```python
fig, ax = plt.subplots()
layers = [2.0 * ks_phi[:, a] ** 2 for a in range(N_PER_LABEL)]
ax.stackplot(x, layers, labels=[f"$2\\phi_{a}^2$" for a in range(N_PER_LABEL)],
             alpha=0.7)
```

The four contributions $2\phi_a^2$ of the occupied orbitals; `ax.stackplot` draws them on top of each other as coloured layers (orbital 0 at the bottom; `alpha=0.7` makes them 70 per cent opaque), so that the top edge is the density. The labels are made by a list comprehension, one per orbital. (In a Python string a backslash is written twice, so the label text reaches matplotlib with one backslash, which draws $\phi$.)

```python
ax.plot(x, n_ks, color="black", lw=1.5, label="total density $n$")
ax.set_xlim(-5.0, 5.0)
ax.set_xlabel("position $x$")
ax.set_ylabel("density (particles per unit length)")
ax.set_title("The density as the sum of the occupied orbitals")
ax.legend(fontsize=8)
save_figure(fig, "density_orbitals",
```

The total density as a black line on top of the layers; range, labels, title, legend and `save_figure` for Figure 13a.5.

**What Figure 13a.5 shows.** Orbital 0 contributes one central bump (blue), orbital 1 two bumps beside the centre (orange), orbital 2 three and orbital 3 four (each orbital $a$ has $a$ zeros, so $\phi_a^2$ has $a + 1$ bumps). Stacked, they give the density: about $1.6$ at the centre, two peaks of about $1.71$ near $x = \pm0.57$, two shoulders of about $1.43$ near $x = \pm1.7$, and a steep fall to nearly zero by $|x| = 3.8$. These ripples on top of a smooth profile are the shell structure. Each layer holds two fermions and the whole stack eight.

**In [14], the energy two ways.**

```python
def kinetic(phi, occupations):
    """T_s = sum_a f_a int phi_a (-1/2 phi_a'') dx with the occupations f_a."""
    return sum(f * float(phi[:, a] @ (T @ phi[:, a])) * h
               for a, f in enumerate(occupations))
```

The kinetic energy $T_s = \sum_a f_a\int\phi_a(-\tfrac12\phi_a'')\,dx$, on the grid $\sum_a f_a\,(\phi_a\cdot T\phi_a)\,h$, for any list of occupations.

```python
T_s = kinetic(ks_phi, [2.0] * N_PER_LABEL)
E_ext = integral(v * n_ks)
E_H = 0.5 * G_C * integral(n_ks ** 2)
E_x = -0.25 * G_C * integral(n_ks ** 2)
E_total = T_s + E_ext + E_H + E_x
E_double = 2.0 * ks_levels[:N_PER_LABEL].sum() - (E_H + E_x)
```

`[2.0] * N_PER_LABEL` is the list $[2, 2, 2, 2]$. The four parts of the energy of Section 13.32, their sum, and the double-counting formula (`ks_levels[:N_PER_LABEL].sum()` adds the four occupied levels).

```python
for label, value in (("kinetic T_s", T_s), ("external int v n dx", E_ext),
                     ("Hartree E_H", E_H), ("exchange E_x", E_x)):
    say(f"{label:22} = {value:.6f}")
report("total energy E (direct sum)", f"{E_total:.6f}")
report("total energy E (double counting)", f"{E_double:.6f}")
check(abs(E_total - E_double) < 1e-9, "the two energy formulas agree")
check(abs(E_x + 0.5 * E_H) < 1e-12, "E_x = -E_H/2 for two equally occupied labels")
```

The loop goes through four pairs (name, value) and prints the parts, $6.726297$, $9.521279$, $11.207843$ and $-5.603922$ (`{label:22}` pads the name with blanks to 22 characters, so that the equals signs line up); the `report` lines print both totals, $21.851498$, and the checks require them to agree to $10^{-9}$ and $E_x = -E_H/2$ to $10^{-12}$ (the rule $-1/g$ with $g = 2$).

**In [15], the functional derivative on the grid.**

```python
def interaction_energy(n):
    """E_H + E_x = (g_c/4) int n^2 dx for two equally occupied labels."""
    return 0.25 * G_C * integral(n ** 2)


eta = np.exp(-(x - 1.0) ** 2)  # a fixed change of shape, off the centre of the trap
epsilon = 1e-4  # the size of the change
quotient = (interaction_energy(n_ks + epsilon * eta)
            - interaction_energy(n_ks - epsilon * eta)) / (2.0 * epsilon)
w_ks = 0.5 * G_C * n_ks  # the mean-field potential w = g_c n / 2
```

The definition of Section 13.9 tested directly: change the density by $\pm\epsilon\eta$ with the bump $\eta = e^{-(x-1)^2}$ and $\epsilon = 10^{-4}$, and form the central difference quotient of $E_H + E_x$. By the definition it must equal $\int w\,\eta\,dx$ with $w = \delta(E_H + E_x)/\delta n = g_c n/2$, which is `w_ks`.

```python
report("difference quotient of E_H + E_x along eta", f"{quotient:.10f}")
report("integral of w eta dx", f"{integral(w_ks * eta):.10f}")
check(abs(quotient - integral(w_ks * eta)) < 1e-9,
      "w = g_c n/2 is the functional derivative of E_H + E_x")
```

Both print as $2.6845567944$, and the check requires agreement to $10^{-9}$ (because $E_H + E_x$ is a square of $n$, the central quotient is exact up to rounding: the terms of order $\epsilon^2$ cancel between $+\epsilon$ and $-\epsilon$, and there are no higher terms).

**In [16], the stability of equal labels.**

```python
def label_densities(w_pair, up_occupations, down_occupations):
    """The densities n_up, n_down and the levels for the pair of potentials."""
    up_levels, up_phi = orbitals(w_pair[:M])  # w_up: the first M numbers
    down_levels, down_phi = orbitals(w_pair[M:])  # w_down: the last M numbers
    n_up = (up_phi[:, :len(up_occupations)] ** 2) @ np.array(up_occupations)
    n_down = (down_phi[:, :len(down_occupations)] ** 2) @ np.array(down_occupations)
    return n_up, n_down, up_levels, up_phi, down_levels, down_phi
```

The two potentials are stored in one list of $2M = 400$ numbers: the first 200 for label up, the last 200 for label down (`w_pair[:M]`, `w_pair[M:]`). For each label the function solves the orbitals and forms the density with any occupations: the matrix of squared orbitals times the list of occupations is $\sum_a f_a\phi_a^2$ at every point.

```python
def labels_map(w_pair, up_occupations, down_occupations):
    """One pass for two labels: w_up = g_c n_down and w_down = g_c n_up."""
    n_up, n_down = label_densities(w_pair, up_occupations, down_occupations)[:2]
    return np.concatenate([G_C * n_down, G_C * n_up])


def labels_energy(w_pair, up_occupations, down_occupations):
    """E = T_s + int v n + g_c int n_up n_down (E_H + E_x for two labels)."""
    n_up, n_down, _, up_phi, _, down_phi = label_densities(
        w_pair, up_occupations, down_occupations)
    return (kinetic(up_phi, up_occupations) + kinetic(down_phi, down_occupations)
            + integral(v * (n_up + n_down)) + G_C * integral(n_up * n_down))
```

One pass of the two-label loop: the potential of label up is $g_c n_\downarrow$ and that of label down $g_c n_\uparrow$ (Section 13.32), joined into one list by `np.concatenate`. `labels_energy` is $E = T_s + \int v\,n + g_c\int n_\uparrow n_\downarrow$.

```python
FILLED = [1.0] * N_PER_LABEL  # the four lowest orbitals of each label occupied
push = 1.0 * np.tanh(x)  # pushes up-fermions to the left, down-fermions to the right
start = np.concatenate([w_scf + push, w_scf - push])
w_pair, pair_residuals = anderson(lambda q: labels_map(q, FILLED, FILLED), start)
n_up, n_down = label_densities(w_pair, FILLED, FILLED)[:2]
```

Each label has its four lowest orbitals occupied once. The start is strongly separated: $\tanh x$ rises from $-1$ to $1$ across the trap, so adding it to the up potential pushes the up fermions to the left, and subtracting it pushes the down fermions to the right. Anderson mixing then runs on both potentials together (the `lambda` fixes the occupations), and the label densities of the result are formed.

```python
say(f"two-label run: {len(pair_residuals)} passes; largest |n_up - n_down| = "
    f"{np.max(np.abs(n_up - n_down)):.1e}")
check(np.max(np.abs(n_up - n_down)) < 1e-8,
      "from a separated start the two-label loop returns to equal densities")
check(abs(labels_energy(w_pair, FILLED, FILLED) - E_total) < 1e-9,
      "the two-label run has the same energy as the equal-label solution")
```

The run needs 36 passes, and the largest difference between the label densities is $4.9\cdot10^{-12}$; the checks require it to be below $10^{-8}$ and the energy to equal the equal-label energy $21.851498$ to $10^{-9}$: from a strongly separated start the loop returns to equal labels. This does NOT yet show that the equal-label solution is stable: a converged loop can sit on a saddle. The next two cells show such a case and then make the test that decides, the energy test.

**In [17], a loop that converges to a saddle: two sites.**

```python
T_HOP, U_SITE = 1.0, 4.0  # the hopping t and the on-site repulsion U of two sites
left_right = np.array([-1.0, 1.0])  # lowers the potential on L and raises it on R
```

The two-site model of Section 13.7 with the hopping $t = 1$ and the repulsion $U = 4$ (so $U = 4t$, stronger than $2t$). `left_right` is the pattern $(-1, +1)$: added to a pair of site potentials $(w_L, w_R)$ it lowers $w_L$ and raises $w_R$.

```python
def site_orbital(w2):
    """(c_L, c_R): the orbital of the lower level of [[w_L, -t], [-t, w_R]]."""
    return np.linalg.eigh(np.array([[w2[0], -T_HOP], [-T_HOP, w2[1]]]))[1][:, 0]
```

For one label with the site potentials `w2` $= (w_L, w_R)$, the one-particle matrix is $\begin{pmatrix} w_L & -t \\ -t & w_R \end{pmatrix}$. `np.linalg.eigh` returns its eigenvalues in increasing order and the eigenvectors as columns; `[1][:, 0]` takes the eigenvector of the LOWER level, the occupied orbital $(c_L, c_R)$ with $c_L^2 + c_R^2 = 1$.

```python
def sites_map(q):
    """One pass on two sites, q = (w_up on L, R, w_down on L, R)."""
    n_up, n_down = site_orbital(q[:2]) ** 2, site_orbital(q[2:]) ** 2
    return np.concatenate([U_SITE * n_down, U_SITE * n_up])
```

One pass of the two-label loop on two sites, exactly as in the trap: the four numbers `q` are the potentials of label up on L and R and of label down on L and R; the occupations of the sites are the squares of the orbital components, and the new potential of label up is $U n_\downarrow$ (it feels only the other label), that of label down $U n_\uparrow$.

```python
def sites_energy(q):
    """-2t (c_L c_R of up + c_L c_R of down) + U sum_sites n_up n_down."""
    c_up, c_down = site_orbital(q[:2]), site_orbital(q[2:])
    return (-2.0 * T_HOP * (c_up[0] * c_up[1] + c_down[0] * c_down[1])
            + U_SITE * np.sum(c_up ** 2 * c_down ** 2))
```

The energy of the determinant built from the two orbitals: each orbital contributes the hopping energy $-2t\,c_L c_R$, and the repulsion is $U$ times the product of the up and down occupations on each site, summed over the two sites.

```python
def sites_start(size):
    """The potentials U/2 + size (-1, 1) for label up and U/2 - size (-1, 1)."""
    return np.concatenate([0.5 * U_SITE + size * left_right,
                           0.5 * U_SITE - size * left_right])
```

A family of label-separating potentials: at `size` $= 0$ both labels have $U/2$ on both sites (the equal-label solution); a positive `size` makes site L cheaper for label up and site R cheaper for label down.

```python
site_ends = {}
for site_push in (0.5, 1.0):
    q_end, site_residuals = anderson(sites_map, sites_start(site_push))
    site_ends[site_push] = q_end
    n_up_sites = site_orbital(q_end[:2]) ** 2
    energy = np.round(sites_energy(q_end), 9) + 0.0  # + 0.0 turns -0.0 into 0.0
    say(f"two sites, push {site_push}: {len(site_residuals)} passes, n_up = "
        f"({n_up_sites[0]:.6f}, {n_up_sites[1]:.6f}), energy {energy:.6f}")
```

The SAME Anderson loop as in the trap (`anderson`, In [8]) runs twice, from a small separation (push 0.5) and from a larger one (push 1). For each end it stores the potentials, prints the number of passes, the occupations of label up on L and R and the energy; `np.round(..., 9)` removes rounding noise and `+ 0.0` turns a printed $-0.000000$ into $0.000000$. The output: from push 0.5 the loop needs 16 passes and ends at $n_\uparrow = (0.5, 0.5)$ with the energy $0$, the equal-label solution; from push 1 it needs 18 passes and ends at $n_\uparrow = (0.933013, 0.066987)$ with the energy $-0.5$, the separated solution.

```python
site_sizes = np.linspace(0.0, 2.5, 51)  # epsilon = 0, 0.05, ..., 2.5
site_family = np.array([sites_energy(sites_start(size)) for size in site_sizes])
saddle_up = site_orbital(site_ends[0.5][:2]) ** 2
```

The energy along the whole family $\epsilon = 0, 0.05, \dots, 2.5$ (for the figure and the last check), and the occupations of label up at the end of the push-0.5 run.

```python
check(np.max(np.abs(saddle_up - 0.5)) < 1e-9
      and abs(sites_energy(site_ends[0.5]) - (-2.0 * T_HOP + 0.5 * U_SITE)) < 1e-9,
      "two sites, U = 4t, push 0.5: the loop converges to equal labels, E = -2t + U/2")
check(abs(sites_energy(site_ends[1.0]) + 2.0 * T_HOP ** 2 / U_SITE) < 1e-9,
      "two sites, push 1: the loop converges to separated labels, E = -2t^2/U")
check(site_family[1] < site_family[0] - 1e-3,
      "two sites: separating the labels lowers the energy, so the equal-label "
      "solution there is a saddle")
```

Three checks. The first: from push 0.5 the loop converges to equal occupations $1/2$ with the equal-label energy $-2t + U/2 = 0$. The second: from push 1 it converges to the separated energy $-2t^2/U = -0.5$ (Section 13.7). The third: already the first step of the family, $\epsilon = 0.05$, has a lower energy than $\epsilon = 0$; so the equal-label solution, although self-consistent and reached by the loop, is a saddle. A converged loop alone cannot tell a minimum from a saddle.

**In [18], the energy test in the trap, and Figure 13a.6.**

```python
shapes = {"tanh x": np.tanh(x), "x exp(-x^2/4)": x * np.exp(-x ** 2 / 4.0),
          "exp(-x^2/2)": np.exp(-x ** 2 / 2.0)}
```

Three shapes $s(x)$ of a label-separating change: $\tanh x$ pushes label up to the left and label down to the right across the whole trap; $x\,e^{-x^2/4}$ does the same but only near the centre; $e^{-x^2/2}$ pushes label up outwards and label down inwards.

```python
def separation_rise(shape, size):
    """E of the determinant made from w_scf +- size * shape, minus E_KS."""
    trial = np.concatenate([w_scf + size * shape, w_scf - size * shape])
    return labels_energy(trial, FILLED, FILLED) - E_total
```

The trial potentials are $w_\uparrow = w_{scf} + \epsilon\,s(x)$ and $w_\downarrow = w_{scf} - \epsilon\,s(x)$. `labels_energy` (In [16]) takes the four lowest orbitals of each label in its trial potential and evaluates the energy $E = T_s + \int v\,n + g_c\int n_\uparrow n_\downarrow$ of that determinant; for the contact interaction this formula is the exact energy of the determinant, so no self-consistency is needed. The function returns the energy above the Kohn-Sham energy `E_total`.

```python
sizes = [0.01, 0.05, 0.2, 0.5, 1.0]
rises = {name: [separation_rise(shape, size) for size in sizes]
         for name, shape in shapes.items()}
for name, values in rises.items():
    say(f"{name:14} E - E_KS: " + " ".join(f"{value:.2e}" for value in values))
```

The rise for the five sizes $\epsilon = 0.01, 0.05, 0.2, 0.5, 1$ and each shape, printed in powers of ten (`.2e`). The output: for $\tanh x$ the rises are $3.50\cdot10^{-5}$, $8.81\cdot10^{-4}$, $1.53\cdot10^{-2}$, $0.124$ and $0.593$; for $x\,e^{-x^2/4}$ they are $2.14\cdot10^{-5}$ to $0.254$; for $e^{-x^2/2}$, $8.58\cdot10^{-6}$ to $8.71\cdot10^{-2}$. All are positive.

```python
check(all(value > 0.0 for values in rises.values() for value in values),
      "every label-separating trial determinant in the trap has a higher energy "
      "than the Kohn-Sham state")
check(all(24.0 < values[1] / values[0] < 26.0 for values in rises.values()),
      "for small separations the energy rises as epsilon^2: in the trap the "
      "equal-label solution is a minimum along these families, not a saddle")
```

Two checks. The first: every one of the fifteen trial determinants lies above the Kohn-Sham energy. The second: going from $\epsilon = 0.01$ to $0.05$ (five times larger) multiplies the rise by between 24 and 26, close to $5^2 = 25$; for $\tanh x$, $8.81\cdot10^{-4} / 3.50\cdot10^{-5} \approx 25.2$. So for small separations the rise is of second order, $E - E_{KS} \approx a\,\epsilon^2$ with $a > 0$: the energy is flat (stationary) at the Kohn-Sham solution and curves upwards. Along these three families the equal-label solution is a minimum, not a saddle. (Three families are a test, not a proof for every possible change; this is a COMPUTED result for this trap at $g_c = 2$.)

```python
fine_sizes = np.linspace(0.0, 1.0, 41)  # epsilon = 0, 0.025, ..., 1
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
for (name, shape), style in zip(shapes.items(), ("-", "--", "-.")):
    left.plot(fine_sizes, [separation_rise(shape, size) for size in fine_sizes],
              style, label=f"shape {name}")
```

Figure 13a.6 has two panels side by side (`plt.subplots(1, 2, ...)`). On the left, the rise for each shape on a finer grid of 41 sizes, each shape with its own line style (solid, dashed, dash-dotted).

```python
left.set_xlabel("size $\\epsilon$ of the separation")
left.set_ylabel("$E - E_{KS}$ ($\\hbar\\omega$)")
left.set_title("Trap, $g_c = 2$: the energy rises (minimum)")
left.legend(fontsize=8)
```

Axis labels (the size is a pure number; the energy is in units of $\hbar\omega$), the title and the legend of the left panel.

```python
right.plot(site_sizes, site_family, color="black", label="energy of the family")
right.plot([0.0], [site_family[0]], "o", ms=8,
           label="loop from push 0.5 (saddle)")
size_end = 0.5 * (site_ends[1.0][1] - site_ends[1.0][0])  # (w_R - w_L)/2 of up
right.plot([size_end], [sites_energy(site_ends[1.0])], "s", ms=8,
           label="loop from push 1 (minimum)")
```

On the right, the two-site family of In [17] as a black line, a circle at $\epsilon = 0$ where the push-0.5 loop ended, and a square where the push-1 loop ended. The square's horizontal position is $(w_R - w_L)/2$ of label up at the end, the size of the separation that the loop found.

```python
right.set_xlabel("size $\\epsilon$ of the separation")
right.set_ylabel("$E$ (units of $t$)")
right.set_title("Two sites, $U = 4t$: the energy falls (saddle)")
right.legend(fontsize=8)
save_figure(fig, "label_separation",
            "The energy test of stability. Left: the trap with eight fermions; "
            "the energy of the determinant made from the label-separating trial "
            "potentials $w_{scf} \\pm \\epsilon\\,s(x)$, minus the Kohn-Sham "
            "energy, for three shapes $s$, against the size $\\epsilon$ (pure "
            "number); vertical axis in units of $\\hbar\\omega$. Every curve starts "
            "flat at 0 and rises: along these families the equal-label solution "
            "is a minimum. Right: two sites with $U = 4t$; the energy of the "
            "determinant made from the potentials $U/2 \\pm \\epsilon\\,(-1, 1)$, "
            "in units of $t$, against $\\epsilon$. It falls from the equal-label "
            "solution (circle, energy 0, where the loop from push 0.5 converged: "
            "a saddle) to the separated minimum $-2t^2/U = -0.5t$ (square, where "
            "the loop from push 1 converged). The converged loop could not tell "
            "the two cases apart; the energy does.")
```

Labels, title and legend of the right panel, and `save_figure`, which writes `13a_6_label_separation.png` with this caption, which the book prints below the figure.

**What Figure 13a.6 shows.** On the left, all three curves start flat at 0 and rise: for $\tanh x$ to about $0.59$ at $\epsilon = 1$, for the other two shapes less, because they move fewer fermions. A flat start means that the Kohn-Sham solution is stationary; the upward curve means a minimum along these families. On the right, the two-site energy starts at 0 (the circle, where the loop from push 0.5 converged) and FALLS to the separated minimum $-0.5t$ (the square, where the loop from push 1 converged): the circle is a saddle. Both loops converged; only the energy shows which end is stable.

**In [19], the variational principle.**

```python
def energy_of_orbitals(phi):
    """E = T_s + int v n dx + (g_c/4) int n^2 dx for 2 fermions in orbitals 0..3."""
    n = density(phi)
    return (kinetic(phi, [2.0] * N_PER_LABEL) + integral(v * n)
            + 0.25 * G_C * integral(n ** 2))


c_values = np.linspace(0.0, 2.0, 41)  # c = 0, 0.05, ..., 2
family_energies = np.array([energy_of_orbitals(orbitals(c * n_scf)[1])
                            for c in c_values])
c_best = c_values[np.argmin(family_energies)]
```

The energy formula of Section 13.32 for any set of orbitals; for 41 values of $c$ from 0 to 2 the orbitals of the trial potential $v + c\,n_{scf}$ (`orbitals(c * n_scf)[1]`) and their energy; `c_best` the value with the lowest energy.

```python
report("c of the lowest energy in the family", f"{c_best:.2f}")
check(abs(c_best - 0.5 * G_C) < 1e-9,
      "the lowest energy of the family is at c = g_c/2 (the self-consistent one)")
check(np.all(family_energies >= E_total - 1e-10),
      "no member of the family has a lower energy than the Kohn-Sham state")
```

`c_best` prints as $1.00$, and the checks require it to equal $g_c/2$ (to $10^{-9}$; the grid of $c$ contains the value 1 exactly) and every member of the family to have an energy at least $E_{KS}$ (to $10^{-10}$).

**In [20], the family as a picture.**

```python
fig, ax = plt.subplots()
ax.plot(c_values, family_energies - E_total, "o-", ms=3,
        label="$E(c) - E_{KS}$")
ax.axvline(0.5 * G_C, color="gray", ls="--", label="$c = g_c/2$ (self-consistent)")
ax.set_xlabel("$c$ in the trial potential $v + c\\,n_{scf}$")
ax.set_ylabel("energy above the Kohn-Sham energy ($\\hbar\\omega$)")
ax.set_title("Variational principle: a family of trial determinants")
ax.legend()
save_figure(fig, "variational_scan",
```

The energy above the Kohn-Sham energy against $c$, as dots joined by a line; a grey dashed vertical line at $c = g_c/2$; labels, title, legend and `save_figure` for Figure 13a.7.

**What Figure 13a.7 shows.** A curve shaped like a parabola that touches zero at $c = 1$ and is flat there: moving $c$ by $0.05$ away from 1 raises the energy by only about $0.001$, while the ends lie much higher, $0.29$ at $c = 0$ (the orbitals of the bare trap) and $0.72$ at $c = 2$ (the orbitals of the Hartree-like potential $v + g_c n$). A first-order error in the orbitals gives only a second-order error in the energy.

**In [21], Hartree only and Thomas-Fermi.**

```python
def hartree_map(w):
    """One pass of the Hartree approximation: w_out = g_c n (no exchange)."""
    return G_C * density(orbitals(w)[1])


w_hartree, hartree_residuals = anderson(hartree_map, np.zeros(M))
n_hartree = density(orbitals(w_hartree)[1])
n_free = density(free_phi)  # no interaction at all
```

The Hartree approximation has the mean-field potential $g_c n$ instead of $g_c n/2$; Anderson mixing solves it, and `n_hartree` is its density. `n_free` is the density without interaction.

```python
def thomas_fermi(mu):
    """The Thomas-Fermi density: the positive root of a n^2 + b n = mu - v."""
    a, b = np.pi ** 2 / 8.0, 0.5 * G_C
    room = np.maximum(mu - v, 0.0)  # zero where the trap is higher than mu
    return (-b + np.sqrt(b * b + 4.0 * a * room)) / (2.0 * a)
```

The Thomas-Fermi density of Section 13.32: `np.maximum(mu - v, 0.0)` replaces $\mu - v$ by 0 where the trap is higher than $\mu$, which makes the root 0 there.

```python
low, high = 0.0, 50.0  # mu lies between these two numbers
for _ in range(60):  # bisection: halve the interval 60 times
    middle = 0.5 * (low + high)
    if integral(thomas_fermi(middle)) < N_TOTAL:
        low = middle  # too few particles: mu must be larger
    else:
        high = middle
mu_tf = 0.5 * (low + high)
n_tf = thomas_fermi(mu_tf)
```

Bisection for $\mu$: the number of particles grows with $\mu$; with $\mu = 0$ there are none and with $\mu = 50$ far more than 8. 60 halvings of the interval of width 50 leave a width of $50/2^{60} \approx 4\cdot10^{-17}$, below the rounding of the computer.

```python
report("Thomas-Fermi chemical potential mu", f"{mu_tf:.6f}")
check(abs(integral(n_tf) - N_TOTAL) < 1e-9, "the Thomas-Fermi density holds 8")
check(abs(integral(n_hartree) - N_TOTAL) < 1e-10, "the Hartree density holds 8")
```

The cell prints $\mu = 5.110729$ and checks that the Thomas-Fermi and the Hartree densities hold 8 particles.

```python
widths = [np.sqrt(integral(x ** 2 * n) / N_TOTAL)
          for n in (n_free, n_ks, n_hartree)]
say("root-mean-square widths: free {:.6f}, Kohn-Sham {:.6f}, Hartree {:.6f}"
    .format(*widths))
check(widths[0] < widths[1] < widths[2],
      "repulsion widens the cloud, and self-interaction (Hartree) widens it more")
```

The **root-mean-square width** $\sqrt{\int x^2 n\,dx/N}$ measures how far the cloud spreads; `.format(*widths)` puts the three numbers into the three braces of the string. The widths $1.413346$, $1.542829$, $1.659857$ must increase in this order (last check).

**In [22], four pictures of the same fermions.**

```python
fig, ax = plt.subplots()
ax.plot(x, n_free, ":", label="no interaction")
ax.plot(x, n_hartree, "--", label="Hartree only (self-interaction)")
ax.plot(x, n_ks, lw=2.0, color="black", label="Kohn-Sham (Hartree + exchange)")
ax.plot(x, n_tf, "-.", label="Thomas-Fermi (local kinetic energy)")
ax.set_xlim(-5.0, 5.0)
ax.set_xlabel("position $x$")
ax.set_ylabel("density (particles per unit length)")
ax.set_title("Four pictures of the same eight fermions ($g_c = 2$)")
ax.legend(fontsize=8)
save_figure(fig, "approximations",
```

The four densities, without interaction (dotted), Hartree only (dashed), Kohn-Sham (thick black) and Thomas-Fermi (dash-dotted); range, labels, title, legend and `save_figure` for Figure 13a.8.

**What Figure 13a.8 shows.** Without interaction the cloud is the narrowest and the highest (peaks of about $1.89$); Kohn-Sham is lower and wider; Hartree only is lower and wider still, because each fermion also pushes against its own density. All three have the bumps of the four occupied orbitals. The Thomas-Fermi density is a smooth dome without bumps, close to the Kohn-Sham density on average, and it ends abruptly at $|x| = \sqrt{2\mu} = 3.20$, where the trap reaches $\mu$ (the orbital densities instead die away gradually beyond that point).

**In [23], switching the interaction on.**

```python
def solve_at(strength, start):
    """The self-consistent w and the three energies (T_s, int v n dx, E_H + E_x)
    at the coupling strength, starting the loop from the potential start."""

    def strength_map(w):  # the Kohn-Sham map with this strength instead of G_C
        return 0.5 * strength * density(orbitals(w)[1])

    w, _ = anderson(strength_map, start)
    phi = orbitals(w)[1]
    n = density(phi)
    parts = (kinetic(phi, [2.0] * N_PER_LABEL), integral(v * n),
             0.25 * strength * integral(n ** 2))
    return w, parts
```

`solve_at` solves the model for any strength: the inner function `strength_map` is the Kohn-Sham map with that strength, Anderson mixing solves it from the given start, and the function returns the potential and the three parts $T_s$, $\int v\,n$ and $E_H + E_x$.

```python
strengths = np.linspace(0.0, 2.0, 9)  # g_c = 0, 0.25, ..., 2
scan, w_start = [], np.zeros(M)
for strength in strengths:
    w_start, parts = solve_at(strength, w_start)  # start from the last solution
    scan.append(parts)
scan = np.array(scan)  # one row per strength; columns: T_s, int v n, E_H + E_x
say(f"E at g_c = 0: {scan[0].sum():.6f}; at g_c = 2: {scan[-1].sum():.6f}")
check(abs(scan[-1].sum() - E_total) < 1e-9, "the scan ends at the same E as above")
```

Nine strengths from 0 to 2, each solved starting from the solution of the previous strength (a good start saves passes). The energy is $15.990192$ at $g_c = 0$ (the grid's version of 16) and $21.851498$ at $g_c = 2$, the same as before (check).

```python
delta = 1e-3
E_plus = sum(solve_at(2.0 + delta, w_scf)[1])  # E at g_c = 2.001
E_minus = sum(solve_at(2.0 - delta, w_scf)[1])  # E at g_c = 1.999
slope = (E_plus - E_minus) / (2.0 * delta)
```

The Hellmann-Feynman test: the energies at $g_c = 2.001$ and $1.999$ (each solved by Anderson mixing from the solution at $g_c = 2$; `sum(...)` adds the three parts) and their central difference quotient.

```python
report("dE/dg_c at g_c = 2 (difference quotient)", f"{slope:.6f}")
report("(1/4) int n^2 dx at g_c = 2 (Hellmann-Feynman)",
       f"{0.25 * integral(n_ks ** 2):.6f}")
check(abs(slope - 0.25 * integral(n_ks ** 2)) < 1e-6,
      "Hellmann-Feynman: dE/dg_c = (1/4) int n^2 dx")
```

Both the quotient and $\tfrac14\int n^2\,dx$ print as $2.801961$, and the check requires agreement to $10^{-6}$ (the quotient has an error of order $\delta^2 = 10^{-6}$ times the third derivative, plus the effect of the loop's tolerance).

**In [24], the energies of the scan.**

```python
fig, ax = plt.subplots()
ax.plot(strengths, scan[:, 0], "o-", ms=4, label="kinetic $T_s$")
ax.plot(strengths, scan[:, 1], "s-", ms=4, label="trap $\\int v\\,n\\,dx$")
ax.plot(strengths, scan[:, 2], "^-", ms=4, label="interaction $E_H + E_x$")
ax.plot(strengths, scan.sum(axis=1), "D-", ms=4, color="black",
        label="total $E$")
ax.set_xlabel("strength $g_c$ of the contact repulsion")
ax.set_ylabel("energy (units of $\\hbar\\omega$)")
ax.set_title("Switching the repulsion on")
ax.legend(fontsize=8)
save_figure(fig, "coupling_scan",
```

The three columns of the table `scan` against the nine strengths, with different markers, and their sum along each row (`scan.sum(axis=1)`) as the black total; labels, title, legend and `save_figure` for Figure 13a.9. After the caption, the check

```python
check(abs(scan[0].sum() - 16.0) < 0.05 and abs(scan[0, 0] - scan[0, 1]) < 0.05,
      "at g_c = 0: E = 16 and T_s equals the trap energy (virial theorem)")
```

requires, at $g_c = 0$ (row 0 of the scan), the total 16 and equal kinetic and trap energies (the virial theorem of Section 13.32), both to $0.05$, the accuracy of the grid.

**What Figure 13a.9 shows.** At $g_c = 0$ the kinetic and the trap energy are both 8 and the total is 16 (the grid gives $15.99$). As the repulsion is switched on, the interaction energy grows almost linearly to $5.60$; the cloud spreads, so the trap energy rises (to $9.52$) and the kinetic energy falls (to $6.73$): wider orbitals curve less. The total rises to $21.85$ along a curve that bends slightly downwards: by the Hellmann-Feynman theorem its slope is $\tfrac14\int n^2\,dx$, which is $3.07$ at $g_c = 0$ (with the density without interaction) and $2.80$ at $g_c = 2$, because the spreading cloud has a smaller $\int n^2\,dx$.

**In [25], the first excited state.**

```python
taus = np.linspace(0.0, 1.0, 9)
gaps, energies, w_pair = [], [], np.concatenate([w_scf, w_scf])
for tau in taus:
    up = [1.0, 1.0, 1.0, 1.0 - tau, tau]  # orbitals 0..4 of label up
    w_pair, _ = anderson(lambda q: labels_map(q, up, FILLED), w_pair)
    up_levels = label_densities(w_pair, up, FILLED)[2]
    gaps.append(up_levels[4] - up_levels[3])  # eps_4(tau) - eps_3(tau)
    energies.append(labels_energy(w_pair, up, FILLED))
gaps, energies = np.array(gaps), np.array(energies)
n_excited = sum(label_densities(w_pair, up, FILLED)[:2])  # tau = 1: n_up + n_down
```

Nine values of the moved fraction $\tau = 0, \tfrac18, \dots, 1$. For each, label up has the occupations $1, 1, 1, 1 - \tau, \tau$ in its orbitals 0 to 4 and label down its four lowest orbitals full; the two-label loop is solved by Anderson mixing, starting from the previous solution, and the level difference $\epsilon_4 - \epsilon_3$ of label up and the energy are stored. After the loop `n_excited` is the total density at $\tau = 1$, the Delta-SCF excited state.

```python
step = taus[1] - taus[0]
simpson = step / 3.0 * (gaps[0] + gaps[-1] + 4.0 * gaps[1:-1:2].sum()
                        + 2.0 * gaps[2:-1:2].sum())
delta_scf = energies[-1] - energies[0]
```

Simpson's rule (Section 13.15) on the nine level differences (the name `simpson` is here a number, not a function), and the Delta-SCF energy $E(1) - E(0)$.

```python
report("Kohn-Sham gap (LUMO - HOMO)", f"{gaps[0]:.6f}")
report("Delta-SCF excitation energy E(1) - E(0)", f"{delta_scf:.6f}")
report("Janak integral of eps_4 - eps_3 (Simpson)", f"{simpson:.6f}")
report("transition state eps_4 - eps_3 at tau = 1/2", f"{gaps[4]:.6f}")
check(abs(energies[0] - E_total) < 1e-9, "tau = 0 is the ground state")
check(abs(gaps[0] - (ks_levels[4] - ks_levels[3])) < 1e-9,
      "at tau = 0 the level difference is the Kohn-Sham gap")
check(abs(simpson - delta_scf) < 1e-6,
      "Janak's theorem: the integral of eps_4 - eps_3 equals Delta-SCF")
check(delta_scf < gaps[0], "orbital relaxation lowers the excitation energy here")
```

The `report` lines print the gap $0.772662$, the Delta-SCF energy $0.714594$, the Janak integral $0.714594$ and the transition state $0.712784$ (entry 4 is $\tau = \tfrac12$). The four checks: $\tau = 0$ is the ground state; the level difference at $\tau = 0$ is the Kohn-Sham gap of In [11] ($5.496606 - 4.723945$); the Janak integral equals the Delta-SCF energy to $10^{-6}$; and the Delta-SCF energy is below the gap here.

**In [26], the excited state as a picture.**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
left.fill_between(taus, 0.0, gaps, alpha=0.25, label="area = Delta-SCF")
left.plot(taus, gaps, "o-", color="black", label="$\\epsilon_4 - \\epsilon_3$")
left.plot([0.0], [gaps[0]], "s", ms=8, label=f"Kohn-Sham gap {gaps[0]:.4f}")
left.plot([0.5], [gaps[4]], "^", ms=8, label=f"transition state {gaps[4]:.4f}")
left.axhline(delta_scf, color="gray", ls="--", label=f"Delta-SCF {delta_scf:.4f}")
```

On the left, `left.fill_between(taus, 0.0, gaps, alpha=0.25, ...)` shades the area between zero and the level difference, which is the Delta-SCF energy by Janak's theorem; the level difference itself as black dots joined by a line; the gap as a large square at $\tau = 0$, the transition state as a large triangle at $\tau = \tfrac12$, and the Delta-SCF energy as a grey dashed horizontal line, each with its value in the legend (four decimals).

```python
left.set_ylim(0.0, 1.0)
left.set_xlabel("fraction $\\tau$ of the moved fermion")
left.set_ylabel("level difference ($\\hbar\\omega$)")
left.legend(fontsize=7, loc="lower left")
```

The vertical range from 0 to 1, labels, and the legend in the lower left corner, inside the shaded area.

```python
right.plot(x, n_ks, color="black", label="ground state")
right.plot(x, n_excited, "--", label="excited (Delta-SCF)")
right.set_xlim(-5.0, 5.0)
right.set_xlabel("position $x$")
right.set_ylabel("density (particles per unit length)")
right.legend(fontsize=8)
fig.suptitle("The first excited state by Delta-SCF ($g_c = 2$)")
save_figure(fig, "delta_scf",
```

On the right the ground-state density (black) and the density of the Delta-SCF excited state (dashed); range, labels, legend, a common title, and `save_figure` for Figure 13a.10.

**What Figure 13a.10 shows.** On the left the level difference falls almost linearly from the gap $0.7727$ at $\tau = 0$ to about $0.66$ at $\tau = 1$: as the up fermion moves into orbital 4, the levels rearrange so that the two orbitals come closer. The shaded area, $0.7146$, is the Delta-SCF energy (dashed line); it is smaller than the gap, and the midpoint value $0.7128$ (triangle) is close to it, because the curve is nearly straight. On the right the excited density differs from the ground-state density mainly in the middle: the ground state has two peaks beside a dip at $x = 0$, the excited state a peak at $x = 0$ and shoulders beside it (orbital 4 has its largest value at the centre, orbital 3 a zero there), and slightly more density in the outer flanks.

**In [27], the last check.**

```python
figure_names = ["trap_orbitals", "scf_convergence", "first_iterations",
                "ks_potentials", "density_orbitals", "label_separation",
                "variational_scan", "approximations", "coupling_scan",
                "delta_scf"]
missing = [name for k, name in enumerate(figure_names, 1)
           if not output_file(f"{FIGURE_FOLDER}/13a_{k}_{name}.png").is_file()]
check(missing == [], "all ten figure files exist")
check(output_file(f"{FIGURE_FOLDER}/13a_10_delta_scf.png").is_file(),
      "the figure file 13a_10_delta_scf.png exists")
all_checks_passed()
```

The same lines as In [19] of Notebook 13c (Section 13.14), with the ten figure names of this notebook. The last line prints ALL 36 CHECKS PASSED (notebook 13a): one check each in In [2], In [5], In [6], In [7], In [10], In [12], In [15] and In [24], two each in In [3], In [8], In [11], In [14], In [16], In [18], In [19], In [23] and In [27], three each in In [17] and In [21], and four in In [25].

### 13.37 From the toy models to dirac16complex

This section says which ideas of the chapter the Kohn-Sham model of dirac16complex (Chapters 14 to 16) uses, and what is different there. As in Section 13.16, $x_1, x_2, x_3$ are the directions of ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the three extra times, which deflate exponentially (scale factor $e^{-a_4}\sin^{1/6}z$ while ordinary space inflates with $e^{a_4}\sin^{1/6}z$), and $x_8$ the hidden direction, $z = 6Hx_8$, with the author's constant $H > 0$.

**What carries over.**

- **The Kohn-Sham scheme and self-consistency.** The model is a Kohn-Sham fermion gas of dirac16complex quanta in the good sector (no momentum along the extra times), in which the 16-component equation reduces to $2 \times 2$ blocks in the hidden coordinate (Chapter 14). Its levels and orbitals are found self-consistently, with Anderson mixing of the potentials at every grid point of the hidden direction (depth 6, $\beta = 0.4$, stopping rule $10^{-11}$ on the largest residual; Section 13.21 and `Revision/kohn_sham/results/parameters.json`, numerics).
- **The interaction and its exchange.** The contact interaction $\tfrac{\lambda}{2}S^2$ with the vertex $C$, treated as Hartree plus the exact local exchange of the uniform 8-fold gas: $e_x = -\tfrac{\lambda}{32}(n^2 + S^2)$, $M_{eff} = m + \tfrac{15}{16}\lambda S$, $v_v = -\tfrac{1}{16}\lambda n$ (Section 13.16; PROVED in `Revision/kohn_sham/reports/ks-theory-python.json`, checks exchange_uniform_gas, ks_potentials, filled_shell_ratio).
- **Mermin's occupations.** At the temperatures $T = 0.01$, $0.02$ and $0.05$ (in units of the mass $m$) the occupations are Fermi-Dirac numbers with $\mu$ fixed by $\sum g f = N$, solved in the LogBalance form (Section 13.26; parameters.json, conventions merminRoot).
- **Excited states.** The Kohn-Sham gap and the particle-hole excitations of Section 13.27, and Delta-SCF in its ensemble form over groups of equal levels (parameters.json, conventions deltaScf).
- **Densities through the Krein form.** The number density is $n = \mathrm{Tr}(B\rho)$ with the indefinite form $B = -iC\gamma^{(x4)}$ of Chapter 10, and the scalar density is $S = \mathrm{Tr}(C\rho)$.

**What is different, and its status.**

- **No correlation.** The dirac16complex functional has no correlation term ("correlation: none (Hartree plus exchange only)" in `Revision/kohn_sham/ks-theory.json`), and for the non-uniform Kohn-Sham determinants its uniform-gas exchange differs from the exact local Fock exchange by $+\tfrac{\lambda}{32}Q^2$ (Section 13.16). These are the approximations of the model.
- **No density-functional theorem is claimed for the field.** The Hohenberg-Kohn and Mermin theorems of Sections 13.8 and 13.26 were proved for particles with a positive inner product and a Hamiltonian bounded from below. For the quantised dirac16complex field with its indefinite Krein form (Chapter 10) the book does not prove such a theorem; the model of Chapter 14 is used as a self-consistent mean-field (exchange-only) model, and whether an exact density functional exists for this field is OPEN.
- **Which levels are filled.** Particles occupy the positive branch of the levels and the brane zero modes; this filling is a CONVENTION of the record, and its justification is OPEN (`Revision/kohn_sham/ks-theory.json`, thermodynamics, fillingConvention).
- **The background.** The history $a_4 = AHx_4$ along which the instantaneous (adiabatic) Kohn-Sham states are computed is a PRESCRIBED BACKGROUND: the Kohn-Sham states violate the conditions that the $a_4$ field equations put on their source (`Revision/field_equations_a4/reports/ks-source-conditions.json`; the checks are named in Section 13.38). The time-dependent (non-adiabatic) problem is OPEN, and the mirror at the end of the hidden direction (the Z2 brane) is ASSUMED.

**The pairs.** Chapter 19 uses these Kohn-Sham states for theorem T3: the Kohn-Sham universes of mass $+M$ and $-M$, with the transformed boundary conditions, have equal energies and energy-momentum tensors (PROVED: `Revision/pairing/kohn_sham/reports/python-t3.json` and, independently, `wolfram-t3.json` in the same folder; every check of both reports is PASS). T3 is an exact map between two sets of solutions. It does not prove that any universe is created, in pairs or otherwise: no creation process, rate or amplitude follows from these equations, and nothing in this chapter changes that.

### 13.38 What we proved, what we computed, what we assumed

**PROVED** (exact derivations in this chapter, each checked numerically by a notebook; the Revision checks are named where the record holds the statement):

- One particle: the eigenvalues of a Hermitian operator are real and its eigenvectors for different eigenvalues orthogonal; the variational principle (Section 13.2).
- Many fermions: the Pauli principle; Slater determinants are antisymmetric, normalised, vanish for equal orbitals, and have the density $\sum_a|\phi_a|^2$ (Section 13.3; Notebook 13c, In [2]).
- Second quantisation: the anticommutation relations; Wick's theorem for a determinant and a thermal ensemble of non-interacting fermions, in every basis; $\langle{:}S^2{:}\rangle = (\mathrm{Tr}\,V\rho)^2 - \mathrm{Tr}(V\rho V\rho)$ (Section 13.4; Revision check hf_wick_contraction of `Revision/kohn_sham/reports/ks-theory-python.json`; Notebook 13c, In [4] to In [8]).
- The energy of a determinant, direct minus exchange; the cancellation of the self-interaction; the exact locality of contact exchange and $E_x = -E_H/g$ for equally occupied labels (Sections 13.5 and 13.15; Notebook 13c, In [10]; Notebook 13b, In [6], In [12], In [13]).
- The Lagrange-multiplier rule and the meaning of the multiplier; the Hartree-Fock equations, the double-counting formula and Koopmans' theorem (Section 13.6).
- The two-site model: $E_0 = \tfrac12(U - \sqrt{U^2 + 16t^2})$ and the best determinant ($-2t + U/2$ for $U \le 2t$, $-2t^2/U$ beyond) (Section 13.7; Notebook 13c, In [11], In [12]).
- The Hohenberg-Kohn theorem and the constrained-search variational principle; functional derivatives; the Kohn-Sham equations and their total energy; the exact Kohn-Sham potential of two sites (Sections 13.8 to 13.10; Notebook 13c, In [16]).
- The uniform gas: $n = gk_F^3/(6\pi^2)$, $C_F$, the density matrix $F(k_FR)$, the exchange hole $1 - F^2/g$, the small-range law $1 - \tfrac35(k_Fa)^2$, Dirac's formula given the integral $9/4$, and the polarisation threshold $\tfrac23(3\pi^2)^{2/3}$ (Section 13.15; Notebook 13b).
- The exchange of the 16-component field: $e_x = -\tfrac{\lambda}{32}(n^2 + S^2)$, $M_{eff} = m + \tfrac{15}{16}\lambda S$, $v_v = -\tfrac{1}{16}\lambda n$, the ratio $-1/8$ (Section 13.16; `Revision/kohn_sham/reports/ks-theory-python.json`, checks exchange_uniform_gas, ks_potentials and filled_shell_ratio; independently `ks-theory-wolfram.json` in the same folder, checks exchange_uniform_gas and ks_potentials; reproduced exactly by Notebook 13b, In [17], In [18]).
- Mixing: the reduced map of the two-site loop, the convergence factor $1 - \beta(1 - G')$ and the condition $0 < \beta < 2/(1 - G')$ for small errors, the least-squares form of Anderson mixing (Section 13.21).
- Temperature: the Gibbs principle with Klein's inequality; Mermin's theorem by the same argument; the independence of the orbitals of non-interacting fermions; the Fermi-Dirac occupations; $dF/dT = -S$, $C_V = T\,dS/dT$, the variance formula and $C_V \ge 0$ (Section 13.26; Notebook 13e).
- Excited states: Janak's theorem and the Delta-SCF integral formula (Section 13.27; Notebooks 13e and 13a).
- The trap model: its Kohn-Sham potential $v + g_cn/2$, the double-counting formula, the one-dimensional Thomas-Fermi equation, the Hellmann-Feynman theorem and the virial theorem (Section 13.32).

**COMPUTED** (numbers printed by the five executed notebooks of the chapter, which are stored in the folder `Revision/textbook/notebooks`; the uncertainty of each number is the tolerance of the check that confirms it):

- Notebook 13c: the two-site numbers $E_0 = -1.236068\,t$, double occupancy $0.276393$ and correlation energy $-0.236068\,t$ at $U = 2t$ (closed forms to $10^{-12}$), the largest correlation energy at $U = 3.335\,t$, and the split of the exact Kohn-Sham screening at $U = 4t$, $\Delta = 2t$ into $-0.588239$ (Hartree-exchange) and $-1.114408$ (correlation).
- Notebook 13b: box sums within $0.00083$ of $F$ for 137059 plane waves; $\int_0^\infty sF^2\,ds = 9/4$ to $10^{-7}$; the box exchange $-19.0000000000$ in two forms (to $10^{-12}$); the label-mixing exchange $-8.7398756465$ (to $10^{-10}$).
- Notebook 13d: $n_L^* = 1.326993$, $G' = -1.687961$, $\beta_{max} = 0.744058$ (to $10^{-6}$), the cycle $0.3607$/$1.9157$, convergence in 13 passes at $\beta = \tfrac12$, the threshold $U = 2.647393$.
- Notebook 13e: no state among 2000 has a lower grand potential than the Gibbs state (smallest excess $3.9\cdot10^{-6}$); the two-level numbers $0.731059$, $1.164406$, $-0.313262$, $0.393224$ (to $10^{-6}$); the ladder's $\mu = 4$ at low temperature.
- Notebook 13a: the trap model at $g_c = 2$: $E = 21.851498$ (two formulas agree to $10^{-9}$), the Kohn-Sham gap $0.772662$, the Delta-SCF energy $0.714594$ (Janak integral to $10^{-6}$), the widths, and the Hellmann-Feynman slope $2.801961$ (to $10^{-6}$); and the Revision solver's mixing settings, read and checked from `Revision/kohn_sham/results/parameters.json`.

**ASSUMED:**

- that the particles are fermions (for dirac16complex: the choice of Grassmann components, Chapter 7);
- for the Hohenberg-Kohn theorem: a non-degenerate ground state, a wave function that does not vanish on a whole region, and that the constrained minima exist; for the Kohn-Sham scheme: non-interacting $v$-representability;
- for the Lagrange rule: the implicit function theorem (used without proof); for the Gibbs principle: a finite number of states;
- that a Delta-SCF state approximates a true excited state;
- the approximations: no correlation in the toy models (they are Hartree-Fock models); in the dirac16complex functional, the uniform-gas exchange and no correlation (Sections 13.16 and 13.37);
- for the dirac16complex model (Section 13.37): the Z2 mirror, and the history of $a_4$ as a prescribed background.

**HYPOTHESIS:** none is used in this chapter. **OPEN:** an exact density functional for the quantised dirac16complex field, the justification of its filling convention, and its time-dependent (non-adiabatic) problem (Section 13.37).

**Where the background status is recorded.** That the history $a_4 = AHx_4$ is a prescribed background, not a solution of the $a_4$ field equations with the Kohn-Sham source, is recorded in the Revision report `Revision/field_equations_a4/reports/ks-source-conditions.json` by its checks ks_history_is_a_prescribed_background, ks_profiles_violate_algebraic_condition and ks_profiles_depend_on_x8, each with the verdict PASS.

### 13.39 Exercises

**Exercise 1.** In the three-point example of Section 13.3, compute $\Phi(2, 1)$, $\Phi(1, 0)$ and $\Phi(1, 1)$, and show from the definition that the two-particle determinant vanishes when $\phi_a = \phi_b$.

*Answer.* With $\phi_0 = (1, 0, 0)$ and $\phi_1 = (0, 1, 1)/\sqrt2$: $\Phi(2, 1) = [\phi_0(2)\phi_1(1) - \phi_1(2)\phi_0(1)]/\sqrt2 = [0\cdot\tfrac{1}{\sqrt2} - \tfrac{1}{\sqrt2}\cdot 0]/\sqrt2 = 0$. $\Phi(1, 0) = [\phi_0(1)\phi_1(0) - \phi_1(1)\phi_0(0)]/\sqrt2 = [0\cdot 0 - \tfrac{1}{\sqrt2}\cdot 1]/\sqrt2 = -\tfrac12$, as the table of Notebook 13c (In [2]) shows. $\Phi(1, 1) = [\phi_0(1)\phi_1(1) - \phi_1(1)\phi_0(1)]/\sqrt2 = 0$, because the two products are equal. If $\phi_a = \phi_b = \phi$, then $\Phi(r_1, r_2) = [\phi(r_1)\phi(r_2) - \phi(r_1)\phi(r_2)]/\sqrt2 = 0$ for all arguments.

**Exercise 2.** Using only the anticommutation relations of Section 13.4, show that $\hat n_p^2 = \hat n_p$, and conclude that $\hat n_p$ has only the eigenvalues 0 and 1.

*Answer.* $\hat n_p^2 = a_p^\dagger a_p a_p^\dagger a_p$. The relation $\{a_p, a_p^\dagger\} = 1$ gives $a_p a_p^\dagger = 1 - a_p^\dagger a_p$, so $\hat n_p^2 = a_p^\dagger(1 - a_p^\dagger a_p)a_p = a_p^\dagger a_p - a_p^\dagger a_p^\dagger a_p a_p$. The relation $\{a_p^\dagger, a_p^\dagger\} = 0$ says $2a_p^\dagger a_p^\dagger = 0$, so the last term vanishes and $\hat n_p^2 = \hat n_p$. If $\hat n_p u = \nu u$ with $u \ne 0$, then $\nu^2 u = \hat n_p^2 u = \hat n_p u = \nu u$, so $\nu^2 = \nu$, that is $\nu = 0$ or $\nu = 1$.

**Exercise 3.** For the three-point example, write the density matrix $\rho = \phi_0\phi_0^T + \phi_1\phi_1^T$ as a $3 \times 3$ matrix and check $\rho^2 = \rho$ and $\mathrm{Tr}\,\rho = 2$.

*Answer.* $\phi_0\phi_0^T$ has a single 1 in the top left corner; $\phi_1\phi_1^T$ has the entries $\tfrac12$ in the lower right $2 \times 2$ block. So $\rho = \begin{pmatrix} 1 & 0 & 0\\ 0 & \tfrac12 & \tfrac12\\ 0 & \tfrac12 & \tfrac12\end{pmatrix}$. Squaring, the corner gives $1\cdot 1 = 1$, and the block $\begin{pmatrix}\tfrac12 & \tfrac12\\ \tfrac12 & \tfrac12\end{pmatrix}^2$ has every entry $\tfrac14 + \tfrac14 = \tfrac12$, so $\rho^2 = \rho$. The trace is $1 + \tfrac12 + \tfrac12 = 2$, the number of particles, and the diagonal $(1, \tfrac12, \tfrac12)$ is the density of Section 13.3.

**Exercise 4.** Solve the two-site model of Section 13.7 for $t = 1$, $U = 4$: the exact energy, the Hartree-Fock energy, the correlation energy, and the exact double occupancy.

*Answer.* $E_0 = \tfrac12(4 - \sqrt{16 + 16}) = 2 - 2\sqrt2 = -0.828427$. Since $U > 2t$, the best determinant is unrestricted, $E_{HF} = -2t^2/U = -0.5$. The correlation energy is $E_0 - E_{HF} = -0.328427$. The ground state lies in the $2 \times 2$ problem $\begin{pmatrix} U & -2t\\ -2t & 0\end{pmatrix}$ on $(D, S)$; its first row gives $(U - E_0)\,d - 2t\,s = 0$, so $s = (U - E_0)\,d/(2t) = (4 + 0.828427)\,d/2 = 2.414214\,d$. The normalisation $d^2(1 + 2.414214^2) = 1$ gives $d^2 = 1/6.828427 = 0.146447$. The double occupancy is the weight of the states LL and RR, which here is $d^2 = 0.146447$, the value of Notebook 13c (In [11]); the restricted determinant would give $\tfrac12$.

**Exercise 5.** Fermions with two labels and a contact interaction of strength $g_c = 1$ have the label densities $n_\uparrow = 0.3$ and $n_\downarrow = 0.1$ at a point. Compute the Hartree and the exchange energy densities and check that their sum is $g_c\,n_\uparrow n_\downarrow$.

*Answer.* $n = 0.4$, so $e_H = \tfrac{g_c}{2}n^2 = 0.5\cdot0.16 = 0.08$ and $e_x = -\tfrac{g_c}{2}(n_\uparrow^2 + n_\downarrow^2) = -0.5\cdot(0.09 + 0.01) = -0.05$. The sum is $0.03 = 0.3\cdot0.1 = n_\uparrow n_\downarrow$. With unequal labels the exchange is not $-e_H/2 = -0.04$: the rule $-1/g$ needs equally occupied labels.

**Exercise 6.** Repeat the mixing analysis of Section 13.21 for $\Delta = 2$, $t = 1$, $U = 2$: check that $x^* = 0.468990$ is the fixed point, compute $G'(x^*)$ and $\beta_{max}$, and decide whether plain iteration converges.

*Answer.* $\Delta - Ux^* = 2 - 0.937980 = 1.062020$, and $\sqrt{1.062020^2 + 4} = \sqrt{5.127886} = 2.264484$, so $G(x^*) = 1.062020/2.264484 = 0.468990 = x^*$. Then $G'(x^*) = -4\cdot2\cdot1/5.127886^{3/2} = -8/(5.127886\cdot2.264484) = -8/11.612 = -0.688942$, and $\beta_{max} = 2/(1 + 0.688942) = 1.184174$. Since $1 < \beta_{max}$, plain iteration converges: its factor $1 - (1 + 0.688942) = -0.688942$ has a size below 1, so the error shrinks by about $0.69$ per pass while changing its sign (the density still swings, but the swings die out). These are the numbers of Notebook 13d (In [12]).

**Exercise 7.** For the two-level example of Section 13.26 (levels 0 and 1, one particle), find the limits of $f_0$, $E$ and $S_s$ as $T \to 0$ and as $T \to \infty$.

*Answer.* By symmetry $\mu = \tfrac12$ at every $T$, so $f_0 = 1/(e^{-1/(2T)} + 1)$ and $f_1 = 1 - f_0$. As $T \to 0$, $e^{-1/(2T)} \to 0$: $f_0 \to 1$, $f_1 \to 0$, $E = f_1 \to 0$, and $S_s \to 0$, because $f\ln f$ and $(1 - f)\ln(1 - f)$ tend to 0 when $f$ tends to 0 or 1. As $T \to \infty$, $e^{-1/(2T)} \to 1$: $f_0, f_1 \to \tfrac12$, $E \to \tfrac12$, and each level contributes $-2\cdot\tfrac12\ln\tfrac12 = \ln2$, so $S_s \to 2\ln2 = \ln4$. Notebook 13e (In [11]) checks both limits.

**Exercise 8.** For the model energy $E = \epsilon_H^0 f_H + \epsilon_L^0 f_L + \tfrac{U}{2}(f_H^2 + f_L^2)$ with any $\epsilon_H^0 < \epsilon_L^0$ and $U < \epsilon_L^0 - \epsilon_H^0$, show that $\Delta_{SCF} - \Delta_{KS} = U$.

*Answer.* By Janak's theorem the levels are $\epsilon_H = \epsilon_H^0 + Uf_H$ and $\epsilon_L = \epsilon_L^0 + Uf_L$. In the ground state $(1, 0)$ (the lower orbital filled; the condition on $U$ keeps $\epsilon_H < \epsilon_L$ there), $\Delta_{KS} = \epsilon_L^0 - (\epsilon_H^0 + U)$. The energies are $E(1, 0) = \epsilon_H^0 + \tfrac{U}{2}$ and $E(0, 1) = \epsilon_L^0 + \tfrac{U}{2}$, so $\Delta_{SCF} = \epsilon_L^0 - \epsilon_H^0$, and $\Delta_{SCF} - \Delta_{KS} = U$.

**Exercise 9.** For the uniform 8-fold gas of dirac16complex (Section 13.16), compute $e_x/e_H$ when $S = n/2$, and the interaction energy $e_{int}$ when $S = n$.

*Answer.* With $S = n/2$: $e_x = -\tfrac{\lambda}{32}(n^2 + \tfrac{n^2}{4}) = -\tfrac{5}{128}\lambda n^2$ and $e_H = \tfrac{\lambda}{2}\cdot\tfrac{n^2}{4} = \tfrac{1}{8}\lambda n^2$, so $e_x/e_H = -\tfrac{5}{128}\cdot 8 = -\tfrac{5}{16}$: exchange removes a larger fraction of the Hartree energy than for a filled level at rest ($-\tfrac18$). With $S = n$: $e_{int} = \tfrac{15}{32}\lambda n^2 - \tfrac{1}{32}\lambda n^2 = \tfrac{7}{16}\lambda n^2$, which is $e_H + e_x = \tfrac12\lambda n^2 - \tfrac{1}{16}\lambda n^2$: in Figure 13b.9 the black curve ends at $7/16 = 0.4375$ at $S/n = 1$.

**Exercise 10.** Notebook 13b (In [12]) finds the exchange energy $-19$ for five up and three down fermions in the box $0 < x < 1$ with $g_c = 1$. Derive this number: show that the density $n_N = \sum_{m=1}^{N}2\sin^2(m\pi x)$ of $N$ fermions with one label has $\int_0^1 n_N^2\,dx = N^2 + N/2$.

*Answer.* $\int_0^1 n_N^2\,dx = 4\sum_{m,m'}\int_0^1\sin^2(m\pi x)\sin^2(m'\pi x)\,dx$. With $\sin^2 A = \tfrac12(1 - \cos2A)$, the product is $\tfrac14[1 - \cos2A - \cos2B + \cos2A\cos2B]$. Over $0 < x < 1$, $\int\cos(2m\pi x)\,dx = 0$ for $m \ge 1$, and $\int\cos(2m\pi x)\cos(2m'\pi x)\,dx = \tfrac12$ if $m = m'$ and 0 otherwise. So each integral is $\tfrac14 + \tfrac18[m = m']$, and $\int n_N^2 = 4\big[N^2\cdot\tfrac14 + N\cdot\tfrac18\big] = N^2 + \tfrac{N}{2}$. Then $E_x = -\tfrac{g_c}{2}\big(\int n_\uparrow^2 + \int n_\downarrow^2\big) = -\tfrac12\big[(25 + 2.5) + (9 + 1.5)\big] = -\tfrac12\cdot 38 = -19$.
