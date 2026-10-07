## 13. Many-body quantum mechanics and DFT from zero

This chapter builds, from zero, the tool with which Chapters 14 to 16 compute the states of many quanta of the field dirac16complex in the author's primordial field: **density functional theory**, DFT for short, in the form of Kohn and Sham. Every idea is first developed for ordinary particles that move slowly (non-relativistic particles), because there every step can be seen and checked by hand. The chapter has five worked examples, Notebooks 13a to 13e, and every number in its text is computed by one of them.

### 13.1 What this chapter is for

**The problem.** Chapter 14 asks for the lowest-energy state (the **ground state**) and the first excited state of a fixed number $N$ of dirac16complex quanta that interact with each other inside the author's primordial gravitational field. A quantum state of one particle in ordinary three-dimensional space is a complex-valued function of three variables (its **wave function**, defined in Section 13.2). If we store such a function on a grid with 10 points along each coordinate, we need $10^3$ complex numbers. The state of two particles is a function of 6 variables, $10^6$ numbers; the state of ten particles a function of 30 variables, $10^{30}$ numbers, more than every computer on Earth can hold together. Every added particle multiplies the work by $10^3$. This growth is called the **exponential wall** of the many-body problem.

**The way around it.** DFT works with the **density** $n$ of the particles instead of their wave function: the expected number of particles per unit volume at each point of space. The density is a function of three variables, whatever $N$ is. Sections 13.8 to 13.10 prove that the density alone fixes the ground-state energy, and they show how Kohn and Sham turned this fact into equations that a computer can solve: one-particle equations in an effective potential, solved again and again until the potential and the density agree (**self-consistency**). The price is one quantity, the **exchange-correlation energy**, that is not known exactly and must be approximated. We will see exactly where the approximation enters and what it is.

**Plan.** Sections 13.2 to 13.7 are the quantum mechanics of many identical fermions: one particle, many particles, Slater determinants, creation and annihilation operators with Wick's theorem, the energy of a determinant with its direct and exchange parts, the Hartree-Fock equations, and an exactly solvable model of two electrons on two sites. Sections 13.8 to 13.10 are density functional theory proper: the Hohenberg-Kohn theorem, functional derivatives and the Kohn-Sham equations. Notebook 13c (Sections 13.11 to 13.14) checks all of this with numbers. Sections 13.15 and 13.16 compute the exchange energy of a uniform gas, show that for a contact interaction it is exactly local, and carry the result over to the 16-component field dirac16complex, reproducing the exchange formulas of the Revision record (Notebook 13b, Sections 13.17 to 13.20). Section 13.21 explains how the self-consistency loop is solved and why it can fail (Notebook 13d, Sections 13.22 to 13.25). Sections 13.26 and 13.27 extend everything to a finite temperature (Mermin's theorem) and to excited states (the Kohn-Sham gap, Janak's theorem and the Delta-SCF method), checked in Notebook 13e (Sections 13.28 to 13.31). Section 13.32 puts all the pieces together in one complete Kohn-Sham calculation, eight fermions in a trap, solved in Notebook 13a (Sections 13.33 to 13.36). Section 13.37 says what of this chapter is used for dirac16complex, Section 13.38 lists what was proved, computed and assumed, and Section 13.39 has exercises with complete answers.

**The order of the notebooks.** The notebooks are lettered in the order in which they were planned, and the chapter presents them in the order in which their ideas are needed: 13c, 13b, 13d, 13e, and last 13a, the complete calculation, which uses every idea of the others.

**Units.** In this chapter Planck's constant divided by $2\pi$ and the particle mass are set to 1 ($\hbar = m = 1$), so the kinetic-energy operator of one particle on a line is $-\tfrac12\,d^2/dx^2$. Each notebook states its other units (the hopping $t$ of the two-site model, the trap frequency of Notebook 13a). A temperature is measured as an energy (Boltzmann's constant is 1).

**Symbols with a local meaning.** Several letters mean something else in this chapter than in the rest of the book. (i) $x$ is the position of a particle, or a point of a grid, or (in Section 13.21) the excess of charge on one site; it is never one of the author's spacetime coordinates $x_1, \dots, x_8$, which appear only in Sections 13.16 and 13.37 and are named there. (ii) $\Psi$ is the wave function of $N$ particles, except in Sections 13.16 and 13.37, where it is the dirac16complex field, as those sections say. (iii) $\rho$ is a density matrix (Section 13.4) or a density operator (Section 13.26), not an energy density. (iv) $t$ is the hopping between two sites, $T$ the temperature and $T_s$ a kinetic energy. (v) $S$ is the entropy in Sections 13.26 to 13.31 and the scalar density of dirac16complex in Sections 13.16 to 13.20 and 13.37. (vi) $U$ is the repulsion of two electrons on one site in the two-site model, and $U_{kp}$ the entries of a unitary matrix. (vii) $g$ counts the internal labels of a particle and $g_c$ is the strength of a contact interaction; neither is the metric. (viii) $H$ and $\hat H$ are Hamiltonians (energy operators); the author's constant $H$ of the metric appears only in Section 13.37.

### 13.2 One quantum particle: states, operators and the variational principle

**States on a grid.** The state of one particle on a line is a complex-valued function $\phi(x)$, its **wave function**. Its squared modulus $|\phi(x)|^2 = \phi^*(x)\,\phi(x)$ (the star means complex conjugate) is the probability per unit length of finding the particle at $x$, so a physical state is **normalised**: $\int |\phi|^2\,dx = 1$. On a computer the line is replaced by $M$ equally spaced points $x_k = x_0 + k h$ with spacing $h$, and a state becomes a column of $M$ numbers $(\phi_1, \dots, \phi_M)$; integrals become sums, $\int f\,dx \approx \sum_k f_k\,h$. Two states are compared by their **inner product**

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
E_H = \tfrac12\sum_{a,b} w_{abab} = \tfrac12\int\!\!\int n(r)\,w(r,r')\,n(r')\,dr\,dr', \qquad E_x = -\tfrac12\sum_{a,b} w_{abba} = -\tfrac12\int\!\!\int |\rho(r,r')|^2\,w(r,r')\,dr\,dr' .
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

**Koopmans' theorem.** Removing the particle of orbital $a$ while the other orbitals stay frozen lowers the energy by $h_{aa} + \sum_b(w_{abab} - w_{abba}) = \langle\phi_a|\hat F\phi_a\rangle = \epsilon_a$: the orbital energy is the energy of that particle in the frozen determinant. The Kohn-Sham analogue, Janak's theorem, is proved in Section 13.27.

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
\Big[-\frac12\,\frac{d^2}{dx^2} + v_s(x)\Big]\phi_a = \epsilon_a\,\phi_a, \qquad v_s = v + v_H + v_{xc}, \qquad v_{xc}(x) = \frac{\delta E_{xc}}{\delta n(x)}, \qquad n(x) = \sum_{a\in O}|\phi_a(x)|^2 ,
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

**In [1], the set-up cell.** It is the same in every notebook of the book except for the notebook's name; the notebooks 13b, 13d, 13e and 13a of this chapter have exactly this cell with their own name, and their walk-throughs refer back to this paragraph. Its first part repeats the complete run instructions of Section 13.12 as **comment lines**: every line that starts with `#` is skipped by Python, and the lines are there so that the notebook file carries its own instructions. The code starts after the line of `=` signs.

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

The following lines set the tick marks 0, 1, 2 (`set_xticks`, `set_yticks`), label the axes and set the title; then `right.imshow(Phi_box, ..., extent=(0, 1, 0, 1))` draws the box determinant over the square $0 \le r_1, r_2 \le 1$, the next line draws the diagonal $r_1 = r_2$ as a thin dashed black line (its style string is the letter k, for black, followed by two hyphens), and `fig.colorbar` adds the colour scale. `save_figure` saves Figure 13c.1 with its caption, and the last lines check that the box determinant is antisymmetric as well:

```python
check(np.allclose(Phi_box, -Phi_box.T, atol=1e-14), "the box determinant is "
      "antisymmetric")
```

(Python joins two strings written next to each other into one.)

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

**In [5], the operator matrices as heat maps.** The loop `for ax, p in zip(axes, (1, 3)):` pairs the two axes with the orbitals 1 and 3 and draws `a_dag[p]` with `imshow` on the colour scale from $-1$ to $1$, with the title "creation operator" and axis labels for the state numbers before (column) and after (row). `fig.colorbar(image, ax=axes, shrink=0.8)` adds one colour scale for both, and `save_figure` saves Figure 13c.2. In the figure every column has at most one entry, $\pm1$: one in the columns of the states in which orbital $p$ is empty.

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

**In [9], the density matrices.** The left heat map shows `np.abs(rho_det)`, the sizes of the 16 entries of the determinant's density matrix. On the right, `np.linalg.eigvalsh` computes the eigenvalues of each density matrix, `np.sort(...)[::-1]` sorts them from the largest down, and `right.bar(positions - 0.2, ..., width=0.4)` and `right.bar(positions + 0.2, ...)` draw them as two rows of bars side by side. `save_figure` saves Figure 13c.3, and the check

```python
check(np.allclose(occupations_det, [1, 1, 0, 0], atol=1e-14)
      and np.allclose(occupations_th, np.sort(f)[::-1], atol=1e-14),
      "the occupations are 1, 1, 0, 0 and the Fermi-Dirac numbers")
```

requires the eigenvalues to be exactly $1, 1, 0, 0$ for the determinant and the Fermi-Dirac numbers $f_p$ for the ensemble.

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

`H_many` is the $16 \times 16$ matrix of $\hat H = \sum h_{pq}a_p^\dagger a_q + \tfrac12\sum w_{pqrs}a_p^\dagger a_q^\dagger a_s a_r$. `direct` is the expectation value of $\hat H$ in the determinant of the basis orbitals 0 and 1, and `formula` is $\sum_a h_{aa} + \tfrac12\sum_{a,b}(w_{abab} - w_{abba})$ of Section 13.5. The cell prints both, $-1.5322375649$, and checks that they agree to $10^{-12}$.

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

**In [13], the energies.** The left panel draws the restricted energy (dashed), the closed-form unrestricted energy (dash-dotted) and the exact energy (thick black) against $U/t$, with a grey vertical line at $U = 2t$ (`axvline`); the right panel draws the correlation energy with points joined by a line (`"o-"`, `ms=3` sets the size of the points). `fig.subplots_adjust(wspace=0.32)` leaves room between the panels, `fig.suptitle` sets one title above both, and `save_figure` saves Figure 13c.4; its caption puts the computed place of the largest correlation energy into the text with an f-string.

**In [14], the double occupancy.**

```python
D_uhf = np.where(U_values <= 2.0, 0.5, 2.0 / U_safe ** 2)
```

The unrestricted double occupancy is $\tfrac12(1 + c_\alpha c_\beta)$ with $c_\beta = -c_\alpha$ and $s_\alpha = 2t/U$, that is $\tfrac12(1 - c_\alpha^2) = \tfrac12 s_\alpha^2 = 2t^2/U^2$ for $U > 2t$, and $\tfrac12$ below. The cell draws the three double occupancies against $U/t$ (`np.ones_like(U_values)` is an array of ones of the same length), saves Figure 13c.5 and checks

```python
check(abs(D_exact[8] - 0.276393) < 1e-6 and abs(D_exact[16] - 0.146447) < 1e-6,
      "exact double occupancy 0.276393 at U = 2t and 0.146447 at U = 4t")
check(np.all(np.diff(D_exact) < 0), "the exact double occupancy falls as U grows")
```

the two worked values (entries 8 and 16 are $U = 2$ and $U = 4$) and that the exact double occupancy falls at every step of $U$ (`np.diff` gives the differences of neighbouring entries).

**In [15], the Hartree-Fock energy landscape.**

```python
E_map = hf_energy(A, B, 4.0)
index = np.unravel_index(np.argmin(E_map), E_map.shape)
```

`E_map` is $E(\alpha, \beta)$ at $U = 4t$ on the whole grid of angles; `np.argmin` finds the position of its smallest value in the table read as one long list, and `np.unravel_index` turns that position back into a row and a column. `ax.contourf(A, B, E_map, levels=30, cmap="viridis")` draws the landscape with 30 colour bands; the white cross marks the restricted point $\alpha = \beta = \pi/4$ and the two red stars the minimum and its mirror image (the angles exchanged). After `save_figure` (Figure 13c.6) the check requires the smallest value to be $-2t^2/U = -0.5$ (to $10^{-5}$, the grid) and the restricted value to be $-2 + 4/2 = 0$.

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

**In [17], the density map.** The loop draws $n_L(\Delta)$ for the three repulsions with dotted, dashed and solid lines, `axhline(1.0)` marks the symmetric density, and `save_figure` saves Figure 13c.7. The stronger the repulsion, the flatter the curve.

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

`c_part[U][nonzero]` keeps the entries with $\Delta \ne 0$. The checks require the correlation part to have the sign opposite to $\Delta$ (it screens further, like the Hartree-exchange part) and the mean-field potential to be larger in size than the exact Kohn-Sham one (it screens less). The plotting lines draw, on the left, $\Delta_s$ against $\Delta$ for both repulsions with the mean field and the line $\Delta_s = \Delta$; on the right, the screening $\Delta_s - \Delta$ at $U = 4t$ with its two parts. After `save_figure` (Figure 13c.8) the last check requires $|\Delta_s| < |\Delta|$ for every $\Delta \ne 0$: the repulsion screens the potential.

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

### 13.15 Placeholder 15

Text.

### 13.16 Placeholder 16

Text.

### 13.17 Placeholder 17

Text.

### 13.18 Placeholder 18

Text.

### 13.19 Placeholder 19

Text.

### 13.20 Placeholder 20

Text.

### 13.21 Placeholder 21

Text.

### 13.22 Placeholder 22

Text.

### 13.23 Placeholder 23

Text.

### 13.24 Placeholder 24

Text.

### 13.25 Placeholder 25

Text.

### 13.26 Placeholder 26

Text.

### 13.27 Placeholder 27

Text.

### 13.28 Placeholder 28

Text.

### 13.29 Placeholder 29

Text.

### 13.30 Placeholder 30

Text.

### 13.31 Placeholder 31

Text.

### 13.32 Placeholder 32

Text.

### 13.33 Placeholder 33

Text.

### 13.34 Placeholder 34

Text.

### 13.35 Placeholder 35

Text.

### 13.36 Placeholder 36

Text.

### 13.37 Placeholder 37

Text.

### 13.38 Placeholder 38

Text.

### 13.39 Placeholder 39

Text.
