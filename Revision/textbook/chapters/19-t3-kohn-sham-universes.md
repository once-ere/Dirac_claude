## 19. T3: the Kohn-Sham universes of mass $+M$ and $-M$

Chapter 18 proved exact pairing theorems for the fields themselves: multiplied by the chirality matrix $\Gamma$, a field configuration of the theory with the mass $m$ and the coupling $\lambda$ becomes a configuration of the theory with $-m$ and $-\lambda$ (theorem T1). But the numbers that Chapters 15 and 16 computed, the levels, energies, densities and pressures of a gas of quanta of the field dirac16complex in the author's primordial universe, are not field configurations. They are **Kohn-Sham states**: quanta that fill one-quantum levels in a common, self-made mean field, with densities computed by the expectation-value rule of the quantised field, with boundary conditions at the two ends of the hidden direction, at one instant of the history in which ordinary 3-space inflates while the three extra times $x_5, x_6, x_7$ deflate exponentially. For these states the pairing question must be asked again, and it has a different answer. Theorem **T3** of the Revision record says: every self-consistent Kohn-Sham state of the universe with the bare mass $+M$ has an exact partner in the universe with the bare mass $-M$, with the **same** coupling $+\lambda$ and a transformed boundary condition at the tip, and the partner has the **same** levels, occupations, energies and energy-momentum profiles, while its scalar density is the mirror image. This chapter proves T3 line by line, shows by exact formulas what goes wrong when the boundary condition is not transformed, and watches the theorem at work in two complete notebooks: one that repeats every step of the proof by hand, and one that runs the Revision Rust Kohn-Sham solver 62 times on universes of mass $+M$, their partners and two kinds of wrong partners. Like every pairing theorem of this book, T3 is an exact map between two sets of solutions; it does not describe the creation of anything, and Section 19.22 says precisely what it does not establish.

### 19.1 What this chapter does

**Why a separate theorem for the Kohn-Sham states.** A theorem about a field equation does not automatically carry over to an approximation of it. Three things are new at the Kohn-Sham level. First, the densities that make the mean field are not the classical bilinears of the field but expectation values in the quantised theory, computed with the indefinite matrix $B$ of Chapter 10; the chirality matrix $\Gamma$ reverses the sign of $B$, and that sign decides which partner the theorem finds. Second, the Kohn-Sham problem has boundary conditions: the ASSUMED Z2 mirror at the brane $y = 0$ and a chosen condition at the tip $y = -L$; a map of solutions must map the boundary conditions too. Third, a Kohn-Sham state is self-consistent: the mean field is made by the occupied orbitals, so the map must carry the whole loop from densities to potentials to orbitals and back. T3 handles all three, and the answer is the pairing $(m, \lambda, \theta) \to (-m, +\lambda, \pi - \theta)$ at EQUAL energies, not the T1 pairing $(m, \lambda) \to (-m, -\lambda)$ at opposite energies.

**What is done, in order.**

- The words of the chapter (Section 19.2).
- The Kohn-Sham problem of one orbital: the slice, the hidden coordinate, the eight blocks, the block Hamiltonian, the boundary conditions (Section 19.3); and of the whole gas: the densities, the mean field, the occupations, the energies and the energy-momentum profiles (Section 19.4).
- Why the chirality $\Gamma$ acts on the blocks as the Pauli matrix $\sigma_2$, and what it does to the Krein sign (Section 19.5).
- The proof of T3 in four steps: the orbitals (Section 19.6), the boundary conditions (Section 19.7), the densities and the mean field, with the reason why the coupling must keep its sign (Section 19.8), and self-consistency with the equality of every energy and every energy-momentum profile (Section 19.9).
- The theorem with its hypotheses and its verification records, and its completion of 2026-10-08: the gaps that an adversarial verification found and closed, statement S6 (the 16-component expectation rule: every component of the energy-momentum tensor and of the current is unchanged), and the two numerical demonstrations of the record (Section 19.10); why T3 is not T1, and the mirror copy inside the Z2 orbifold (Section 19.11).
- The exact levels at zero 3-momentum, and the three things that go wrong when the tip is not transformed: the zero modes move to the tip, a level appears inside the mass gap, and the brane band gets a seven times steeper slope (Section 19.12).
- Notebook 19b, the proof by hand (Sections 19.13 to 19.16).
- The four universes A, B, C, D of the Rust runs and Notebook 19a (Sections 19.17 to 19.21).
- What T3 says about pairs of universes and what it does not (Section 19.22), the closing summary (Section 19.23) and exercises with complete answers (Section 19.24).

**The two notebooks.**

| notebook | what it computes | Rust | PASS lines | figures |
| --- | --- | --- | --- | --- |
| 19b | the gammas and the block map; every step of the proof of T3 in exact sympy algebra; the exact zero-momentum spectra of A, B and the control C; shooting; the brane-band slopes | no | 19 | 6 |
| 19a | the gammas and the block map; 62 runs of the Rust Kohn-Sham solver for A, B, C, D with 8, 136 and 688 quanta, along the history, for five couplings and three temperatures; comparison with the record's numerical demonstration of T3 | yes | 37 | 10 |

Notebook 19b is placed first, because it follows the proof step by step; Notebook 19a then shows the theorem in the full self-consistent computation. Each notebook is complete in itself; you may run them in either order.

**The status of every statement.** Every statement of this chapter carries one of the labels of Chapter 0.

- PROVED: theorem T3 itself, with every step derived line by line in Sections 19.5 to 19.12. In the Revision record T3 is proved by WolframScript (`Revision/pairing/kohn_sham/reports/wolfram-t3.json`, 10 of 10 checks PASS) and by sympy (`Revision/pairing/kohn_sham/reports/python-t3.json`, 13 of 13 checks PASS); the theorem record with its hypotheses, statement, proof and limits is `Revision/pairing/kohn_sham/t3-theory.json`. An adversarial verification (2026-10-08) found no error in the statement or the proof, but gaps in its verification; the **completion** record `Revision/pairing/kohn_sham/t3-completion.json` closes the three exact ones (`Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json`, 3 of 3 checks PASS; `Revision/pairing/kohn_sham/reports/python-t3-completion.json`, 7 of 7): the Kohn-Sham coefficients read from the record in both engines (Section 19.8), the filling convention carried onto the partner (Section 19.9), and statement S6, the 16-component expectation rule (Section 19.10). The facts about the blocks come from the Kohn-Sham theory reports `Revision/kohn_sham/reports/ks-theory-python.json` (in its present state 58 of 58 checks PASS) and `Revision/kohn_sham/reports/ks-theory-wolfram.json` (46 of 46).
- COMPUTED: every number of the Rust solver and of the notebooks, with its measured difference. The record's two numerical demonstrations of T3 (Section 19.10): `Revision/pairing/kohn_sham/reports/t3-rust-demo.json` (the Rust solver on all 210 states of the canonical matrix, 7 of 7 checks PASS) and `Revision/pairing/kohn_sham/reports/t3-reference-demo.json` (the independent reference solver on 18 states, 7 of 7). The solver's own T3 self-test is the check t3_block_map_solver_selftest of `Revision/kohn_sham/reports/ks-rust-solver.json` (in its present state 42 of 42 checks PASS). All of them are demonstrations, not part of the proof, and the Rust agreement is at the rounding level by construction (Section 19.17).
- ASSUMED: the good sector (no dependence on the extra times); the Z2 mirror construction at the brane $y = 0$; the cut of the hidden direction at the tip $y = -L$ with $L = 3$ and the chosen tip condition (T3 needs its transformed form); the mean field of Hartree plus the exact exchange of the uniform gas, without correlation. CONVENTION: which levels count as particles (the filling convention, Section 19.4); its justification is OPEN.
- PRESCRIBED BACKGROUND: the history $a_4 = AHx_4$ with $A = 1$; the Kohn-Sham states are not an admissible source of the $a_4$ field equations (`Revision/field_equations_a4/reports/ks-source-conditions.json`, checks ks_profiles_violate_algebraic_condition and ks_history_is_a_prescribed_background).
- OPEN: the time-dependent (non-adiabatic) Kohn-Sham problem; the justification of the filling convention.
- HYPOTHESIS: the author's statement that universes are created in pairs is a HYPOTHESIS. This chapter neither uses it nor proves it.

**Notation and units.** The author's coordinates are $x_1, \dots, x_8$: $x_1, x_2, x_3$ are ordinary 3-space, which inflates with the scale factor $e^{a_4}\sin^{1/6}z$; $x_4$ is the time; $x_5, x_6, x_7$ are the three extra times, which are time-like and deflate exponentially with the scale factor $e^{-a_4}\sin^{1/6}z$ while $a_4$ grows; $x_8$ is the hidden space direction, with $z = 6Hx_8$ between 0 and $\pi/2$ and the author's constant $H > 0$. The frame metric is $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in this order, and $\gamma^{(x_a)}$ is the author's real $16 \times 16$ gamma matrix of the direction $x_a$ (Chapters 4 and 5), with $\gamma^{(x_a)}\gamma^{(x_b)} + \gamma^{(x_b)}\gamma^{(x_a)} = 2\eta_{ab}$ times the unit matrix. The **universe of mass $+M$** of the title is the Kohn-Sham problem with the bare mass $m = +M$, the **universe of mass $-M$** the one with $m = -M$; in all numbers $M = 1$ and $H = 1$, so energies, momenta and temperatures are in units of $|m|$, lengths in units of $1/H$. A state of the record is named like N136_lamp1_a10: $N = 136$ quanta, the coupling $+\lambda_1$ (the tags lam0, lamp1, lamm1, lamp2, lamm2 stand for $\lambda = 0, +\lambda_1, -\lambda_1, +\lambda_2, -\lambda_2$), the slice $a_{4,0} = 1.0$ (the two digits are ten times the slice). The two couplings are fixed per particle number in `Revision/kohn_sham/results/parameters.json` so that the first-order mean field stays below $0.1$ and $0.3$ along the whole history: for $N = 8$, $\lambda_1 = 0.01946$ and $\lambda_2 = 0.05838$; for $N = 136$, $\lambda_1 = 0.0009298$ and $\lambda_2 = 0.002789$; for $N = 688$, $\lambda_1 = 0.0001846$ and $\lambda_2 = 0.0005538$.

### 19.2 The words of this chapter

- **Kohn-Sham state**: an approximate state of $N$ identical quanta built from one-quantum wave functions, the **orbitals**, each of which solves a one-quantum equation in a common **mean field**; the mean field is made from the densities of the occupied orbitals.
- **Self-consistent**: the orbitals reproduce the mean field that made them. A computer finds such a state by repeating "densities, then mean field, then orbitals, then densities" until nothing changes.
- **Slice**: one instant of the history $a_4 = AHx_4$; $a_{4,0}$ is the value of $a_4$ there. An **instantaneous** (adiabatic) Kohn-Sham state is the self-consistent state of the Kohn-Sham problem written at that one instant, with $a_4 = a_{4,0}$; along the history the extra times keep deflating, and the states are computed slice after slice.
- **Hidden coordinate** $y$: $y = \ln(\sin z)/(6H)$; the **brane** is $y = 0$ ($z = \pi/2$), the **tip** is the cut $y = -L$ with $L = 3$.
- **Block**: one of the eight pairs of spinor components into which the 16 components split exactly; labelled $(j, s_2, s_3)$ with three signs. The **block type** is $j = \pm1$. An orbital of a block is a pair of functions $\chi(y) = (\chi_1(y), \chi_2(y))$.
- **Level** $\varepsilon$: an allowed energy of one orbital; **occupation** $f$ between 0 and 1: how much of a quantum sits in that orbital; **degeneracy** $g$: how many orbitals share one level.
- **Brane parity**: even means $\chi_2(0) = 0$, odd means $\chi_1(0) = 0$; both kinds of orbitals belong to every state. **Tip angle** $\theta$: the angle of the tip condition $(1 - Q(\theta))\chi(-L) = 0$.
- **Zero mode**: an orbital with $\varepsilon = 0$ at zero 3-momentum. **Brane band**: the levels that grow out of the zero modes when the 3-momentum is switched on. **Mass gap**: the energies $-|M| < \varepsilon < |M|$, in which a free quantum of mass $M$ in an unbounded space has no level.
- **Image**: the orbital, state or problem obtained by applying the map of T3. **Partner**: the problem whose solutions are exactly the images. A map is an **involution** when applying it twice gives back the start.
- **Krein sign** of a block: the number $\pm1$ by which the matrix $B$ acts in the block.
- **Negative control**: a computation that must FAIL to agree; it shows that an agreement is not automatic. In this chapter the **control** C is the universe of mass $-M$ with the UNtransformed tip, and the **wrong partner** D the one with the reversed coupling.
- **Characteristic function**: a function of $\varepsilon$ whose zeros are exactly the levels.
- **Hellmann-Feynman rule**: a small change $\delta h$ of a Hamiltonian moves a non-degenerate level by $\langle\chi|\delta h|\chi\rangle/\langle\chi|\chi\rangle$ to first order.

### 19.3 The Kohn-Sham problem of one orbital

This section collects, from Chapter 14 and the record `Revision/kohn_sham/ks-theory.json`, every formula of the problem for one orbital that the proof will use. Each is PROVED in the Kohn-Sham theory reports; the check names are given.

**The slice and the hidden coordinate.** The Kohn-Sham states are computed at the slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$ of the history $a_4 = AHx_4$, $A = 1$ (`Revision/kohn_sham/results/parameters.json`). In the hidden coordinate $y$ the author's metric is

$$
ds^2 = e^{2Hy}\left[e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - e^{-2a_4}(dx_5^2 + dx_6^2 + dx_7^2)\right] - dx_4^2 + dy^2 ,
$$

the volume factor is $\sqrt{|g|} = e^{6Hy}$ (the inflation $e^{3a_4}$ of 3-space and the deflation $e^{-3a_4}$ of the extra times cancel), and a 3-momentum $k$ enters every equation through the **momentum weight**

$$
\kappa(y) = e^{-Hy - a_{4,0}} .
$$

(Checks geometry_hidden_coordinate, geometry_sqrt_det and geometry_warped_form.) The slice enters the problem only through $\kappa$. The proof below never changes $\kappa$, so it works at every slice.

**The orbital.** In the good sector (no dependence on the extra times) an orbital of 3-momentum $\mathbf k = (k, 0, 0)$ along $x_1$ is

$$
\Psi_{16} = \frac{e^{-i\varepsilon x_4}\,e^{ikx_1}\,e^{-3Hy}}{\sqrt{\ell^3v_t}}\;V_\beta\,\chi(y), \qquad \int_{-L}^{0}\chi^\dagger\chi\,dy = 1 ,
$$

where $V_\beta$ are the two columns of the block $\beta$ in the unitary $16 \times 16$ matrix $V$ of the record, $\ell$ is the size of the 3-torus of 3-space and $v_t$ the coordinate volume of the extra times. A rotation of 3-space does not change the levels, so turning $\mathbf k$ along $x_1$ loses nothing (check rotation_invariance). The allowed momenta are $\Delta k$ times triples of whole numbers, with $\Delta k = 0.25$; a **shell** is the set of momenta with the same $|\mathbf k|^2 = \Delta k^2 n_2$.

**The eight blocks.** The three matrices $J = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_4)}$, $K_1 = \gamma^{(x_2)}\gamma^{(x_3)}$ and $K_2 = \gamma^{(x_5)}\gamma^{(x_6)}$ commute with each other and with the Hamiltonian; their eigenvalues $j = \pm1$, $is_2$ and $is_3$ ($s_2, s_3 = \pm1$) label eight blocks of two components each (checks blocks_commuting_set, blocks_projectors, blocks_basis_unitary; Section 14.5). In the basis $V_\beta$ of the block $(j, s_2, s_3)$ the matrices that the proof needs act as $2 \times 2$ matrices or numbers (check blocks_forms):

| matrix | in the block $(j, s_2, s_3)$ |
| --- | --- |
| $\gamma^{(x_8)}$ | $\sigma_3$ |
| $\gamma^{(x_8)}\gamma^{(x_4)}$ | $j\sigma_1$ |
| $B = -iC\gamma^{(x_4)}$ | the number $js_2$ |
| $C$ | $s_2\sigma_2$ |
| $BC$ | $j\sigma_2$ |
| $B\gamma^{(x_8)}$ | $js_2\sigma_3$ |

Here $\sigma_1, \sigma_2, \sigma_3$ are the Pauli matrices

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} .
$$

Each squares to the unit matrix $\mathbf 1$, two different ones anticommute ($\sigma_a\sigma_b = -\sigma_b\sigma_a$ for $a \ne b$), each is Hermitian ($\sigma_a^\dagger = \sigma_a$, where $^\dagger$ means: transpose and replace every entry by its complex conjugate), and their products are $\sigma_1\sigma_2 = i\sigma_3$, $\sigma_2\sigma_3 = i\sigma_1$, $\sigma_3\sigma_1 = i\sigma_2$, with the opposite sign in the reversed order.

**The block Hamiltonian.** In a block of type $j$ the orbital solves $h_j\chi = \varepsilon\chi$ with

$$
h_j(M, v) = j\left[-i\sigma_1\frac{d}{dy} + M(y)\,\sigma_2 + \kappa(y)\,k\,\sigma_3\right] + v(y) ,
$$

where $M(y) = M_{\rm eff}(y)$ is the effective mass and $v(y) = v_v(y)$ the potential of the mean field (Section 19.4); the Hamiltonian depends on $j$ but not on $s_2, s_3$, so there are two types of blocks, four blocks of each type (check block_hamiltonian). We write $h_j(M, v)$ when we want to show which mass and potential it contains. Multiplying $h_j\chi = \varepsilon\chi$ from the left by $ij\sigma_1$ gives the first-order form (check block_ode_equivalent; Section 14.5)

$$
\frac{d\chi}{dy} = N\chi, \qquad N = M\sigma_3 - \kappa k\,\sigma_2 + ij(\varepsilon - v)\,\sigma_1 ,
$$

and with $\chi = (a, ib)$, $a$ and $b$ real, the **real form**

$$
\frac{da}{dy} = M a - \big(\kappa k + j(\varepsilon - v)\big)\, b, \qquad \frac{db}{dy} = \big(j(\varepsilon - v) - \kappa k\big)\, a - M b .
$$

**The boundary conditions.** At the brane the record ASSUMES the Z2 mirror (orbifold) construction: the field on the mirror side $y > 0$ is the reflected field, $\Psi(-y) = \pm\gamma^{(x_8)}\Psi(y)$, and continuity at $y = 0$ gives $(1 \mp \gamma^{(x_8)})\chi(0) = 0$, that is, in every block,

$$
\text{even parity: } \chi_2(0) = 0 \quad (b(0) = 0), \qquad \text{odd parity: } \chi_1(0) = 0 \quad (a(0) = 0) .
$$

Both parities are solved and filled together; they are the two sectors of the doubled system "universe plus mirror image" (check bc_brane_parity_conditions). At the tip the record CHOOSES a regular condition from the family

$$
\big(1 - Q(\theta)\big)\chi(-L) = 0, \qquad Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2 ,
$$

with the canonical angle $\theta = 0$: $(1 - \sigma_3)\chi(-L) = 0$, that is $\chi_2(-L) = 0$ ($b(-L) = 0$). For $\theta = \pi$, $Q(\pi) = -\sigma_3$ and the condition is $(1 + \sigma_3)\chi(-L) = 0$, that is $\chi_1(-L) = 0$ ($a(-L) = 0$) (check bc_tip_family).

**Why these conditions make sense: the current.** For two pairs of functions $\phi$, $\chi$ the record proves (check bc_self_adjoint_boundary_term)

$$
\phi^\dagger(h_j\chi) - (h_j\phi)^\dagger\chi = \frac{d}{dy}\Big[-ij\,\phi^\dagger\sigma_1\chi\Big] .
$$

Integrated from $-L$ to $0$, the left side becomes the difference between "$h_j$ acting to the right" and "$h_j$ acting to the left", and the right side the value of the bracket at $y = 0$ minus its value at $y = -L$. If both boundary conditions make the **current** $\phi^\dagger\sigma_1\chi$ vanish at the ends, the two integrals are equal: $h_j$ is self-adjoint, its levels are real and its orbitals of different levels are orthogonal. Both brane conditions and every tip condition of the family do this; Exercise 19.4 proves it for the tip.

### 19.4 The Kohn-Sham problem of the whole gas

**The expectation-value rule.** The quantised field (Chapter 10) gives every density as an expectation value. For the quasi-free states of the Kohn-Sham model the record uses the rule

$$
\langle\Psi^\dagger X\Psi\rangle = \mathrm{Tr}(X\rho), \qquad \rho = \sum_{\rm occupied} f\,u\,u^\dagger B ,
$$

where $X$ is a $16 \times 16$ matrix, $u$ runs over the occupied 16-component orbitals, $f$ is the occupation and $B = -iC\gamma^{(x_4)}$ is the Krein matrix ($B^2 = 1$, eigenvalues $+1$ eight times and $-1$ eight times). For one orbital, line by line:

$$
\mathrm{Tr}\big(X\,u\,u^\dagger B\big) = \mathrm{Tr}\big((u^\dagger B)(Xu)\big) = u^\dagger BXu .
$$

Rule: the trace of a product does not change when the factors are moved around in a circle, $\mathrm{Tr}(PR) = \mathrm{Tr}(RP)$, here with $P = Xu$ (a column) and $R = u^\dagger B$ (a row); a row times a column is a single number, its own trace. (Check gas_densities.) The three densities that matter are the **number density** (the U(1) charge density, whose integral counts the quanta), the **scalar density** and a third density $Q$:

$$
n = \langle\Psi^\dagger B\Psi\rangle = \sum f\,u^\dagger BBu = \sum f\,u^\dagger u, \qquad S = \langle\bar\Psi\Psi\rangle = \langle\Psi^\dagger C\Psi\rangle = \sum f\,u^\dagger BCu ,
$$

$$
Q = \langle\Psi^\dagger B\gamma^{(x_8)}\Psi\rangle = \sum f\,u^\dagger BB\gamma^{(x_8)}u = \sum f\,u^\dagger\gamma^{(x_8)}u .
$$

Rule: $X = B$, $C$, $B\gamma^{(x_8)}$ in the line above, and $BB = B^2 = 1$.

**The densities of one orbital.** Put in $u = \Psi_{16}$ of Section 19.3. The phases $e^{-i\varepsilon x_4}e^{ikx_1}$ cancel against their conjugates, and $e^{-3Hy}$ appears twice, so

$$
u^\dagger Xu = \frac{e^{-6Hy}}{\ell^3v_t}\;\chi^\dagger\big(V_\beta^\dagger XV_\beta\big)\chi = P\,\chi^\dagger\big(V_\beta^\dagger XV_\beta\big)\chi, \qquad P = \frac{e^{-6Hy}}{\ell^3v_t} .
$$

The middle matrix is the block form of $X$ (the table of Section 19.3). With $V_\beta^\dagger V_\beta = \mathbf 1$, $BC \to j\sigma_2$ and $\gamma^{(x_8)} \to \sigma_3$:

$$
n_o = P\,\chi^\dagger\chi, \qquad s_o = P\,\chi^\dagger j\sigma_2\chi, \qquad q_o = P\,\chi^\dagger\sigma_3\chi .
$$

The record adds two more (`ks-theory.json`, densities.perOrbital): the density of the 3-momentum current along $\mathbf k$, $t_o = P\,\chi^\dagger j\sigma_3\chi = j\,q_o$, and the current along $y$, $c_o = P\,\chi^\dagger j\sigma_1\chi$. In the real form $\chi = (a, ib)$ they are simple: $\sigma_2\chi = (-i\cdot ib,\ ia) = (b, ia)$ and $\chi^\dagger = (a, -ib)$, so

$$
\chi^\dagger\chi = a^2 + b^2, \qquad \chi^\dagger\sigma_2\chi = ab + (-ib)(ia) = 2ab,
$$

$$
\chi^\dagger\sigma_3\chi = a^2 - b^2, \qquad \chi^\dagger\sigma_1\chi = a(ib) + (-ib)a = 0 .
$$

Rule: multiply out, with $i\cdot i = -1$. So $c_o = 0$ for every orbital of real form: no current flows along the hidden direction.

**The totals.** Each level $\varepsilon$ of the block type $j$, the brane parity $p$ and the momentum shell $n_2$ has the degeneracy $g = 4r_3(n_2)$ (four blocks $(s_2, s_3)$ of the type $j$ times the number $r_3(n_2)$ of lattice momenta in the shell). Then

$$
n(y) = \sum_{\rm levels} w\,g\,f\,n_o(y), \qquad S(y) = \sum_{\rm levels} w\,g\,f\,s_o(y),
$$

and the same for $t(y)$ and $Q(y)$, with $w = w_{Z2} = \tfrac12$: every orbital is normalised on the patch $-L \le y \le 0$, which is half of the doubled interval of the Z2 construction. The particle number is $N = \sum g f$ over all levels of both parities; it counts the quanta of the doubled system, $N/2$ per copy (`ks-theory.json`, densities.total; the conventions of `Revision/kohn_sham/results/parameters.json`).

**The mean field.** The contact interaction is $U = \tfrac{\lambda}{2}S^2$. For the quasi-free states of the model, Hartree plus the exact exchange of the uniform gas give the **interaction energy density** (check exchange_uniform_gas; Chapter 14)

$$
e_{\rm int}(n, S) = \frac{15}{32}\lambda S^2 - \frac{1}{32}\lambda n^2 ,
$$

without a correlation term. The two potentials are its derivatives, line by line:

$$
M_{\rm eff} = m + \frac{\partial e_{\rm int}}{\partial S} = m + \frac{15}{32}\cdot 2\,\lambda S = m + \frac{15}{16}\lambda S, \qquad v_v = \frac{\partial e_{\rm int}}{\partial n} = -\frac{1}{32}\cdot 2\,\lambda n = -\frac{\lambda n}{16} .
$$

Rule: the derivative of $cx^2$ is $2cx$; the bare mass $m$ is added to the derivative with respect to $S$ because the mass term of the Lagrangian is $mS$ (check ks_potentials). Note for later: $e_{\rm int}$ contains $S$ only as $S^2$, and $M_{\rm eff} - m$ is proportional to $\lambda S$.

**The occupations.** At the temperature $T$ the occupations are Mermin's (Fermi's) $f = 1/(1 + e^{(\varepsilon - \mu)/T})$, with the chemical potential $\mu$ fixed by $\sum gf = N$; at $T = 0$ the lowest particle levels are filled. Which levels count as particle levels is a CONVENTION of the record (`ks-theory.json`, thermodynamics.fillingConvention): the levels of the positive branch of the problem without interaction, together with the zero modes at zero 3-momentum, each followed continuously as $\lambda$ is switched on; the negative branch is the normal-ordered sea and contributes nothing. Its justification is OPEN.

**The energies.** With $\mathrm{Vol}_7 = \ell^3v_t$ the record defines (`ks-theory.json`, thermodynamics)

$$
E_{KS} = \sum g f\varepsilon - 2\,\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}e_{\rm int}\,dy, \qquad S_{\rm ent} = -\sum g\big[f\ln f + (1 - f)\ln(1 - f)\big],
$$

$$
\Omega = -T\sum g\ln\big(1 + e^{-(\varepsilon - \mu)/T}\big) - 2\,\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}e_{\rm int}\,dy, \qquad F = \Omega + \mu N = E_{KS} - TS_{\rm ent} :
$$

the Kohn-Sham energy, the entropy, the grand potential and the free energy (Exercise 19.7 derives the last equality).

**The energy-momentum profiles.** The energy density and the three pressures of the gas, per unit proper volume, are (`ks-theory.json`, emt; check emt_orbital_components)

$$
\rho = \sum w g f\,\varepsilon\,n_o - e_{\rm int}, \qquad p_3 = \sum w g f\,\frac{\kappa|k|}{3}\,t_o + e_{\rm int}, \qquad p_t = e_{\rm int},
$$

$$
p_8 = \sum w g f\Big[(\varepsilon - v_v)\,n_o - M_{\rm eff}\,s_o - \kappa|k|\,t_o\Big] + e_{\rm int} :
$$

$\rho$ is the energy density, $p_3$ the pressure of 3-space, $p_t$ the pressure of the deflating extra times and $p_8$ the pressure of the hidden direction. Every self-consistent state obeys the conservation law along $y$, $p_8' + 6Hp_8 = 3H(p_3 + p_t)$ (check emt_y_conservation_selfconsistent).

**The loop.** A self-consistent state is found by repeating: from $n(y)$ and $S(y)$ build $M_{\rm eff}(y)$ and $v_v(y)$; solve $h_j\chi = \varepsilon\chi$ for both block types, every momentum shell and both parities with the boundary conditions; fill the levels; compute new $n(y)$ and $S(y)$. A state that reproduces itself is a **fixed point** of this loop. Chapter 15 describes how the Rust solver does it.

### 19.5 The chirality Γ on the blocks

**Γ and the gammas.** The chirality is the product of all eight gammas in the author's order,

$$
\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}\gamma^{(x_4)}\gamma^{(x_5)}\gamma^{(x_6)}\gamma^{(x_7)} = \mathrm{diag}(-1, \dots, -1, +1, \dots, +1) ,
$$

with $-1$ eight times and then $+1$ eight times (`Revision/algebra/reports/wolfram-algebra.json`, check Gamma_diag). Moving one gamma $\gamma^{(x_c)}$ from the left of $\Gamma$ to its right passes the seven other factors, each with a sign $-1$, and itself, without a sign: $\gamma^{(x_c)}\Gamma = (-1)^7\Gamma\gamma^{(x_c)} = -\Gamma\gamma^{(x_c)}$. So $\Gamma$ **anticommutes with every gamma**, hence with every product of an odd number of gammas, and **commutes with every product of an even number**. It is real and diagonal, so $\Gamma^\dagger = \Gamma$ and $\Gamma^2 = 1$.

**Γ moves every block to its partner block.** $J = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_4)}$ has three factors, $K_1$ and $K_2$ have two. Let $v$ be a column of the block $(j, s_2, s_3)$, that is $Jv = jv$, $K_1v = is_2v$, $K_2v = is_3v$. Then, line by line:

$$
J(\Gamma v) = -\Gamma Jv = -j\,(\Gamma v), \qquad K_1(\Gamma v) = \Gamma K_1v = is_2\,(\Gamma v), \qquad K_2(\Gamma v) = is_3\,(\Gamma v) .
$$

Rule: $\Gamma$ anticommutes with the odd product $J$ and commutes with the even products $K_1$, $K_2$; then use the eigenvalue equations of $v$. So $\Gamma v$ lies in the block $(-j, s_2, s_3)$: the **partner block**, with the opposite type and the same $s_2$, $s_3$ (check blocks_relation_to_Gamma).

**Γ acts as ±σ2 between the partner blocks.** Let $V_b$ be the two basis columns of the block $b = (j, s_2, s_3)$ and $V_p$ those of the partner block $p = (-j, s_2, s_3)$. Because $\Gamma V_b$ lies in the block $p$, it is a combination of the columns $V_p$: $\Gamma V_b = V_pG$ for some $2 \times 2$ matrix $G$. The block forms say $\gamma^{(x_8)}V_b = V_b\sigma_3$ and $\gamma^{(x_8)}V_p = V_p\sigma_3$ (in both blocks $\gamma^{(x_8)}$ is $\sigma_3$), and $\gamma^{(x_8)}\gamma^{(x_4)}V_b = V_b(j\sigma_1)$, $\gamma^{(x_8)}\gamma^{(x_4)}V_p = V_p(-j\sigma_1)$ (the type of $p$ is $-j$). Now line by line:

$$
\Gamma\gamma^{(x_8)}V_b = \Gamma V_b\sigma_3 = V_pG\sigma_3, \qquad -\gamma^{(x_8)}\Gamma V_b = -\gamma^{(x_8)}V_pG = -V_p\sigma_3G .
$$

Rule: the block forms and the definition of $G$. The two left sides are equal, because $\Gamma$ anticommutes with $\gamma^{(x_8)}$; the columns of $V_p$ are independent, so

$$
G\sigma_3 = -\sigma_3G .
$$

The same with the even product $\gamma^{(x_8)}\gamma^{(x_4)}$, which commutes with $\Gamma$:

$$
\Gamma\big(\gamma^{(x_8)}\gamma^{(x_4)}\big)V_b = V_pG\,(j\sigma_1), \qquad \big(\gamma^{(x_8)}\gamma^{(x_4)}\big)\Gamma V_b = V_p(-j\sigma_1)\,G, \qquad\text{so}\qquad G\sigma_1 = -\sigma_1G .
$$

Rule: equate the two lines and divide by $j = \pm1$. Every $2 \times 2$ matrix can be written as $G = g_0\mathbf 1 + g_1\sigma_1 + g_2\sigma_2 + g_3\sigma_3$ with four numbers $g_0, \dots, g_3$ (four numbers for four entries). Multiply $G\sigma_3 = -\sigma_3G$ from the left by $\sigma_3$: $\sigma_3G\sigma_3 = -G$. Line by line:

$$
\sigma_3G\sigma_3 = g_0\mathbf 1 - g_1\sigma_1 - g_2\sigma_2 + g_3\sigma_3 = -g_0\mathbf 1 - g_1\sigma_1 - g_2\sigma_2 - g_3\sigma_3 .
$$

Rule: $\sigma_3\sigma_3\sigma_3 = \sigma_3$, and $\sigma_3\sigma_a\sigma_3 = -\sigma_a\sigma_3\sigma_3 = -\sigma_a$ for $a = 1, 2$; the right side is $-G$. Comparing the coefficients gives $g_0 = -g_0$ and $g_3 = -g_3$, so $g_0 = g_3 = 0$. The same steps with $\sigma_1$ ($\sigma_1G\sigma_1 = g_0 + g_1\sigma_1 - g_2\sigma_2 - g_3\sigma_3 = -G$) give $g_0 = g_1 = 0$. Hence

$$
G = \tau\,\sigma_2, \qquad |\tau| = 1 ,
$$

where $|\tau| = 1$ because $\Gamma$ and $V$ are unitary, so $G$ is unitary too. The record computes the number $\tau$ for all eight blocks: $\tau = s_2$, that is $\Gamma V_{(j, s_2, s_3)} = V_{(-j, s_2, s_3)}\,(s_2\sigma_2)$ (checks blocks_relation_to_Gamma of `ks-theory-python.json`, T3_Gamma_is_the_block_map of `wolfram-t3.json`, T3.Gamma_is_the_block_map of `python-t3.json`). Notebooks 19a and 19b compute it again (Notebook 19b, figure 2, shows where the entries sit).

**The map of T3.** For a 16-component orbital $\Psi_{16}$ built from $\chi$ in the block $(j, s_2, s_3)$, the orbital $\Gamma\Psi_{16}$ is built from $s_2\sigma_2\chi$ in the block $(-j, s_2, s_3)$, at the same 3-momentum and the same point. The constant sign $s_2$ changes no density (every density contains the orbital twice, and $s_2^2 = 1$), so we drop it. On the reduced problem the chirality is the map

$$
(\chi,\ j) \longrightarrow (\sigma_2\chi,\ -j), \qquad\text{in the real form}\qquad (a, b, j) \longrightarrow (b, a, -j) ,
$$

because $\sigma_2(a, ib) = (b, ia)$: the map exchanges $a$ and $b$ and reverses the block type.

**Γ reverses the Krein sign.** In the block $(j, s_2, s_3)$ the matrix $B$ is the number $js_2$, its Krein sign; in the partner block it is $-js_2$. In 16 components: $B = -iC\gamma^{(x_4)}$ is $-i$ times a product of five gammas (four in $C$, one more), an odd product, so $\Gamma B = -B\Gamma$ and

$$
\Gamma B\Gamma^\dagger = \Gamma B\Gamma = -B\Gamma\Gamma = -B
$$

(`Revision/pairing/reports/python-pairing.json`, check Q.image_krein_metric). This one sign is why T3 differs from T1 (Section 19.11).

### 19.6 Step 1 of the proof: an orbital and its image

**The block Hamiltonian under σ2.** We conjugate $h_j(M, v)$ with $\sigma_2$, that is, we compute $\sigma_2h_j(M, v)\sigma_2$, term by term. The matrix $\sigma_2$ is constant, so it can be moved past the derivative: $\frac{d}{dy}(\sigma_2\chi) = \sigma_2\frac{d\chi}{dy}$. Line by line:

$$
\sigma_2\Big(-i\sigma_1\frac{d}{dy}\Big)\sigma_2 = -i\,\sigma_2\sigma_1\sigma_2\,\frac{d}{dy} = +i\sigma_1\frac{d}{dy} .
$$

Rule: $\sigma_2\sigma_1\sigma_2 = -\sigma_1\sigma_2\sigma_2 = -\sigma_1$ (the two anticommute, and $\sigma_2^2 = \mathbf 1$).

$$
\sigma_2\big(M\sigma_2\big)\sigma_2 = M\,\sigma_2\sigma_2\sigma_2 = M\sigma_2, \qquad \sigma_2\big(\kappa k\,\sigma_3\big)\sigma_2 = \kappa k\,\sigma_2\sigma_3\sigma_2 = -\kappa k\,\sigma_3, \qquad \sigma_2\,v\,\sigma_2 = v .
$$

Rule: $\sigma_2^2 = \mathbf 1$; $\sigma_2\sigma_3\sigma_2 = -\sigma_3\sigma_2\sigma_2 = -\sigma_3$; the numbers $M$, $\kappa k$, $v$ (functions of $y$) commute with every matrix. Adding the four terms, with the factor $j$ in front of the first three:

$$
\sigma_2h_j(M, v)\sigma_2 = j\Big[+i\sigma_1\frac{d}{dy} + M\sigma_2 - \kappa k\,\sigma_3\Big] + v = (-j)\Big[-i\sigma_1\frac{d}{dy} + (-M)\sigma_2 + \kappa k\,\sigma_3\Big] + v = h_{-j}(-M, v) .
$$

Rule: take the factor $-1$ out of the bracket and give it to $j$; then compare with the definition of $h_j$ in Section 19.3. This holds for every function $M(y)$, $\kappa(y)$, $v(y)$ and every $k$.

**The image orbital.** Suppose $h_j(M, v)\chi = \varepsilon\chi$. Then, line by line:

$$
h_{-j}(-M, v)(\sigma_2\chi) = \sigma_2h_j(M, v)\sigma_2\,\sigma_2\chi = \sigma_2h_j(M, v)\chi = \sigma_2\,\varepsilon\chi = \varepsilon\,(\sigma_2\chi) .
$$

Rule: replace $h_{-j}(-M, v)$ by $\sigma_2h_j(M, v)\sigma_2$ (the line above); $\sigma_2\sigma_2 = \mathbf 1$; the eigenvalue equation; a number commutes with $\sigma_2$. So **$\sigma_2\chi$ is an orbital of the partner block type $-j$, in the mass $-M$ and the SAME potential $v$, with the SAME level $\varepsilon$ and the same 3-momentum**. Because $\sigma_2^2 = \mathbf 1$, the argument also runs backwards. Without the change of the mass the identity fails: $h_{-j}(-M, v) - h_{-j}(M, v) = (-j)(-2M)\sigma_2 = 2jM\sigma_2$, which is not zero for $M \ne 0$. Status: PROVED; checks T3_block_hamiltonian_map of `wolfram-t3.json` and T3.block_hamiltonian_map of `python-t3.json` (each with this control), and block_Gamma_map of both Kohn-Sham theory reports.

**The same in the first-order form.** The solver integrates $d\chi/dy = N\chi$. Line by line, with $N_j(M) = M\sigma_3 - \kappa k\sigma_2 + ij(\varepsilon - v)\sigma_1$:

$$
\sigma_2N_j(M)\sigma_2 = M\sigma_2\sigma_3\sigma_2 - \kappa k\,\sigma_2\sigma_2\sigma_2 + ij(\varepsilon - v)\sigma_2\sigma_1\sigma_2 = -M\sigma_3 - \kappa k\,\sigma_2 - ij(\varepsilon - v)\sigma_1 = N_{-j}(-M) .
$$

Rule: the three conjugation rules above; then compare with $N_{-j}(-M) = (-M)\sigma_3 - \kappa k\sigma_2 + i(-j)(\varepsilon - v)\sigma_1$. Hence if $d\chi/dy = N_j(M)\chi$, then $\frac{d}{dy}(\sigma_2\chi) = \sigma_2N_j(M)\sigma_2\,\sigma_2\chi = N_{-j}(-M)\,(\sigma_2\chi)$ (checks T3_ode_map and T3.ode_map).

**The same in the real form.** In the real form the map is $(a, b, j, M) \to (b, a, -j, -M)$. Check it directly: call the image $A = b$, $\mathcal B = a$. The real form with $(-j, -M)$ asks

$$
\frac{dA}{dy} = (-M)A - \big(\kappa k + (-j)(\varepsilon - v)\big)\mathcal B = -Mb + \big(j(\varepsilon - v) - \kappa k\big)a ,
$$

and this is exactly the second equation of the original, $db/dy = (j(\varepsilon - v) - \kappa k)a - Mb$. Likewise

$$
\frac{d\mathcal B}{dy} = \big((-j)(\varepsilon - v) - \kappa k\big)A - (-M)\mathcal B = Ma - \big(\kappa k + j(\varepsilon - v)\big)b ,
$$

which is the first equation of the original, $da/dy$. Rule: insert $A = b$, $\mathcal B = a$ and multiply out the signs. Notebook 19b uses this form for its shooting.

**Every slice at once.** The slice $a_{4,0}$ and the 3-momentum enter only through $\kappa k$, which the map does not touch. So everything in this section, and therefore T3, holds at every slice of the deflating history, and for every 3-momentum.

### 19.7 Step 2 of the proof: the boundary conditions

**The tip.** Line by line:

$$
\begin{aligned}
\sigma_2Q(\theta)\sigma_2 &= \cos\theta\,\sigma_2\sigma_3\sigma_2 + \sin\theta\,\sigma_2\sigma_2\sigma_2 = -\cos\theta\,\sigma_3 + \sin\theta\,\sigma_2 \\
&= \cos(\pi - \theta)\,\sigma_3 + \sin(\pi - \theta)\,\sigma_2 = Q(\pi - \theta) .
\end{aligned}
$$

Rule: the conjugation rules of Section 19.6; then $\cos(\pi - \theta) = -\cos\theta$ and $\sin(\pi - \theta) = \sin\theta$. Therefore

$$
\sigma_2\big(1 - Q(\theta)\big)\chi = \sigma_2\chi - \sigma_2Q(\theta)\sigma_2\,\sigma_2\chi = \big(1 - Q(\pi - \theta)\big)\,\sigma_2\chi .
$$

Rule: insert $\sigma_2\sigma_2 = \mathbf 1$ between $Q(\theta)$ and $\chi$. Since $\sigma_2$ is invertible, the left side vanishes exactly when $(1 - Q(\theta))\chi = 0$. So **$\chi$ obeys the tip condition with the angle $\theta$ exactly when $\sigma_2\chi$ obeys the tip condition with the angle $\pi - \theta$**. The canonical $\theta = 0$ ($\chi_2(-L) = 0$) becomes $\theta = \pi$ ($\chi_1(-L) = 0$); in components this is plain, because $\sigma_2\chi = (-i\chi_2,\ i\chi_1)$ has the first component $-i\chi_2$. A control: the solution $(1, 0)$ of the condition $\theta = 0$ has the image $\sigma_2(1, 0) = (0, i)$, and $(1 - Q(0))(0, i) = (1 - \sigma_3)(0, i) = (0, 2i) \ne 0$: the image violates the UNtransformed condition, while $(1 - Q(\pi))(0, i) = (1 + \sigma_3)(0, i) = (0, 0)$. Status: PROVED; checks T3_tip_condition_map and T3.tip_condition_map.

**The brane.** Line by line:

$$
\sigma_2(1 - \sigma_3)\sigma_2 = \sigma_2\sigma_2 - \sigma_2\sigma_3\sigma_2 = 1 + \sigma_3 .
$$

So the even condition $(1 - \sigma_3)\chi(0) = 0$, that is $\chi_2(0) = 0$, holds exactly when $(1 + \sigma_3)\sigma_2\chi(0) = 0$, the odd condition for the image. **The map exchanges the two brane parities.** Both parities belong to every Kohn-Sham problem of the record (they are the two sectors of the ASSUMED Z2 construction, solved and filled together), so the set of boundary problems is mapped onto itself and only the names "even" and "odd" are exchanged. The tip is the only boundary condition that really changes.

**The current and the norm.** For the image orbitals of type $-j$, line by line:

$$
(\sigma_2\phi)^\dagger(\sigma_2\chi) = \phi^\dagger\sigma_2\sigma_2\chi = \phi^\dagger\chi, \qquad -i(-j)\,(\sigma_2\phi)^\dagger\sigma_1(\sigma_2\chi) = ij\,\phi^\dagger\sigma_2\sigma_1\sigma_2\chi = -ij\,\phi^\dagger\sigma_1\chi .
$$

Rule: $(\sigma_2\phi)^\dagger = \phi^\dagger\sigma_2^\dagger = \phi^\dagger\sigma_2$; $\sigma_2\sigma_1\sigma_2 = -\sigma_1$. The norm and the current of Section 19.3 are unchanged. So normalised orbitals go to normalised orbitals, orthogonal ones to orthogonal ones, and the image problem is self-adjoint with real levels, like the original. Status: PROVED; checks T3_brane_parities_exchanged and T3.brane_parities_exchanged.

**What Steps 1 and 2 give together.** Write $\mathcal P_j(M, v, \theta, p)$ for the boundary-value problem of the block type $j$ with the mass $M(y)$, the potential $v(y)$, the tip angle $\theta$ and the brane parity $p$. Then $\chi$ is a normalised eigen-orbital of $\mathcal P_j(M, v, \theta, \text{even})$ with the level $\varepsilon$ exactly when $\sigma_2\chi$ is a normalised eigen-orbital of $\mathcal P_{-j}(-M, v, \pi - \theta, \text{odd})$ with the same level, and the same with "even" and "odd" exchanged. The correspondence is one to one and onto, because $\sigma_2$ undoes itself. So **the two problems have the same levels, level by level, with the same multiplicities**. The degeneracies agree too: the map sends the four blocks of the type $j$ one to one onto the four blocks of the type $-j$, at the same momenta.

### 19.8 Step 3 of the proof: the densities and the mean field

**The densities of one orbital.** Under $(\chi, j) \to (\sigma_2\chi, -j)$ the five densities of Section 19.4 become, line by line:

$$
n_o \to P(\sigma_2\chi)^\dagger(\sigma_2\chi) = P\chi^\dagger\sigma_2\sigma_2\chi = P\chi^\dagger\chi = +n_o ,
$$

$$
s_o \to P(\sigma_2\chi)^\dagger(-j)\sigma_2(\sigma_2\chi) = -jP\chi^\dagger\sigma_2\sigma_2\sigma_2\chi = -jP\chi^\dagger\sigma_2\chi = -s_o ,
$$

$$
t_o \to -jP\chi^\dagger\sigma_2\sigma_3\sigma_2\chi = -jP\chi^\dagger(-\sigma_3)\chi = +t_o ,
$$

$$
q_o \to P\chi^\dagger\sigma_2\sigma_3\sigma_2\chi = -q_o, \qquad c_o \to -jP\chi^\dagger\sigma_2\sigma_1\sigma_2\chi = +c_o .
$$

Rule: $(\sigma_2\chi)^\dagger = \chi^\dagger\sigma_2$; $\sigma_2^2 = \mathbf 1$; $\sigma_2\sigma_3\sigma_2 = -\sigma_3$, $\sigma_2\sigma_1\sigma_2 = -\sigma_1$; the factor $P$ is the same because the map acts at the same point. In the real form it is even simpler: $(a, b, j) \to (b, a, -j)$ turns $a^2 + b^2$ into $b^2 + a^2$ (no change), $2jab$ into $2(-j)ba$ (sign change) and $a^2 - b^2$ into $b^2 - a^2$ (sign change). Status: PROVED; checks T3_orbital_densities and T3.orbital_densities (for arbitrary complex $\chi$ and both $j$).

**The densities of the gas.** If the image state has the same levels, degeneracies and occupations (Step 4 shows that it does), the sums of Section 19.4 give

$$
n(y) \to n(y), \qquad t(y) \to t(y), \qquad S(y) \to -S(y), \qquad Q(y) \to -Q(y) .
$$

**Which partner closes the mean field.** For the image orbitals to be orbitals of the partner problem, Step 1 demands that the partner's mean field be $(-M_{\rm eff}, v_v)$: the opposite mass and the same potential. Let the partner have the bare mass $m'$ and the coupling $\lambda'$; its mean field, built from the image densities $(n, -S)$, is $m' + \frac{15}{16}\lambda'(-S)$ and $-\lambda' n/16$. The potential decides the coupling, line by line:

$$
-\frac{\lambda' n}{16} = -\frac{\lambda n}{16} \quad\Longrightarrow\quad \lambda' = \lambda \qquad (n \ne 0) .
$$

Rule: multiply by $-16/n$. Then the mass decides the bare mass:

$$
m' - \frac{15}{16}\lambda S = -m - \frac{15}{16}\lambda S \quad\Longrightarrow\quad m' = -m .
$$

Rule: insert $\lambda' = \lambda$, and add $\frac{15}{16}\lambda S$ to both sides. Check, line by line, that $(m', \lambda') = (-m, +\lambda)$ works:

$$
M'_{\rm eff} = -m + \frac{15}{16}\lambda(-S) = -\Big(m + \frac{15}{16}\lambda S\Big) = -M_{\rm eff}, \qquad v'_v = -\frac{\lambda n}{16} = v_v,
$$

$$
e_{\rm int}(n, -S) = \frac{15}{32}\lambda(-S)^2 - \frac{1}{32}\lambda n^2 = e_{\rm int}(n, S) .
$$

Rule: take $-1$ out of the bracket; $(-S)^2 = S^2$. **The coupling keeps its sign; only the bare mass is reversed.** With the parameter change of T1, $(m', \lambda') = (-m, -\lambda)$, the mean field comes out wrong:

$$
-m + \frac{15}{16}(-\lambda)(-S) = -M_{\rm eff} + \frac{15}{8}\lambda S, \qquad -\frac{(-\lambda)n}{16} = v_v + \frac{\lambda n}{8} ,
$$

both off whenever $\lambda S \ne 0$ or $\lambda n \ne 0$. Status: PROVED; checks T3_mean_field_map and T3.mean_field_map (with the control $(-m, -\lambda)$). The sympy check also verifies that the potentials are the derivatives of $e_{\rm int}$. Notebook 19b, figure 3, draws these three mass lines; Notebook 19a, figure 9, shows the energies of $(-m, -\lambda)$.

**A gap in the verification of this step, and how it was closed.** The adversarial verification of 2026-10-08 (`Revision/pairing/kohn_sham/t3-completion.json`, entry adversarial_verification, Gap 1) found two weaknesses in the Wolfram verifier of T3 as it then stood: it wrote the four coefficients $\frac{15}{16}$, $-\frac{1}{16}$, $\frac{15}{32}$, $-\frac{1}{32}$ into its script instead of reading them from `Revision/kohn_sham/ks-theory.json`, and its clause about $v_v$ compared an expression with itself (`vvf[lam, n] === vvf[lam, n]`), which is true for every $v_v$ whatever. So, for $v_v$, the statement "two independent verifiers" did not hold at that time: only the sympy check, which reads the coefficients from the record, verified the potential. The algebra above was never in doubt; what was missing was an independent machine check of it. The completion closes the gap with the checks T3C_mean_field_coefficients_from_ks_theory (`Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json`) and T3C.mean_field_coefficients_from_ks_theory (`Revision/pairing/kohn_sham/reports/python-t3-completion.json`): both engines read the potentials from `ks-theory.json`, check that $M_{\rm eff} - m = \partial e_{\rm int}/\partial S$ and $v_v = \partial e_{\rm int}/\partial n$ (the two derivatives of Section 19.4), and repeat the map $M_{\rm eff}[-m, +\lambda, -S] = -M_{\rm eff}[m, \lambda, S]$, $e_{\rm int}$ even in $S$, $v_v$ free of $S$, with the control $(-m, -\lambda)$, which fails. Afterwards, on the same day, the T3 verifier itself was fixed at the root: it now reads the coefficients from `ks-theory.json`, and its check T3_mean_field_map writes $v_v$ as a function of $(m, \lambda, n, S)$ and compares its values at the original and at the image arguments, so that a wrong coefficient makes the check fail; it still has 10 of 10 checks PASS (`Revision/pairing/kohn_sham/README.md`; `Revision/pairing/kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md`, section 6.5). Status of Step 3 now: PROVED, by two independent verifiers in the T3 records and again by the completion checks in both engines.

### 19.9 Step 4 of the proof: self-consistency, energies and energy-momentum

Let A be a self-consistent Kohn-Sham state of the problem with $(m, \lambda, \theta)$ at a slice $a_{4,0}$, with $N$ quanta at the temperature $T$: its orbitals $\chi$ with the levels $\varepsilon$ and the occupations $f$ give the densities $n$, $S$, these give $M_{\rm eff}$, $v_v$, and the eigen-orbitals of this mean field with both parities and the tip angle $\theta$ are again the orbitals $\chi$. Define the state B: the orbitals $\sigma_2\chi$ in the partner blocks, with the same occupations. We show that B is a self-consistent state of the problem with $(-m, +\lambda, \pi - \theta)$, at the same slice, with the same $N$ and $T$.

- (i) The densities of B are $(n, -S)$ (Step 3).
- (ii) The partner problem builds from them the mean field $(-M_{\rm eff}, v_v)$ (Step 3).
- (iii) In this mean field, with the tip angle $\pi - \theta$ and both parities, the eigen-orbitals of the partner problem are exactly the orbitals $\sigma_2\chi$, with the same levels and degeneracies (Steps 1 and 2).
- (iv) The occupations. A Mermin occupation depends only on $\varepsilon$, $\mu$ and $T$. The particle number $N(\mu) = \sum gf(\varepsilon; \mu, T)$ is the same function of $\mu$ for both problems, because the levels and degeneracies are the same, so the same $\mu$ solves $N(\mu) = N$. Which levels are particle levels is decided by following the problem without interaction; at $\lambda = 0$ the two free problems ($M = m$ and $M = -m$, $v = 0$) are themselves mapped onto each other by Steps 1 and 2, so every image level carries the label of its original. In particular the zero mode $(e^{my}, 0)$ of A goes to $\sigma_2(e^{my}, 0) = (0, ie^{my})$, a zero mode of B. And because the coupling is the same, the continuous path from $\lambda = 0$ to $\lambda$ along which the labels are followed is the same path for both problems. Hence the partner problem gives every orbital $\sigma_2\chi$ the occupation $f$. This item was the second gap of the adversarial verification (`t3-completion.json`, Gap 2): the record's proof used the filling convention (hypothesis H5, defined for the member with $m > 0$ and $\theta = 0$) for the image with the remark that both block types and both parities belong to each problem, without showing that the image's set of particle levels is the image of the original's set. The argument of this item is what the completion checks: for every coupling $\lambda'$ on the path from $0$ to $\lambda$ and any $S(y)$, $\sigma_2h_j(m + \frac{15}{16}\lambda'S)\sigma_2 = h_{-j}\big(-(m + \frac{15}{16}\lambda'S)\big)$ for both $j$ (Step 1 with the mass $m + \frac{15}{16}\lambda'S$), so the map keeps the levels with $\varepsilon > 0$ at $\lambda = 0$ and commutes with the continuation in $\lambda$; the brane zero mode $(e^{My}, 0)$ goes to $(0, ie^{My})$, the brane zero mode of the image in its own boundary conditions (odd parity, tip angle $\pi$); with the untransformed tip the image mode violates the tip condition (the control). Checks T3C_filling_convention_mapped and T3C.filling_convention_mapped (statement "H5 for the pair" of `t3-completion.json`). Status: PROVED; the filling convention itself remains a CONVENTION whose justification is OPEN.
- (v) So the densities that the partner problem computes from its own orbitals and occupations are $(n, -S)$, the densities we started from in (ii): B is a fixed point of the partner's loop, a **self-consistent state**.

Applying the map twice gives back A, because $\sigma_2^2 = \mathbf 1$ and $(-(-m), \lambda, \pi - (\pi - \theta)) = (m, \lambda, \theta)$: the map is an **involution**, and every self-consistent state of the partner problem is the image of a self-consistent state of the original. The self-consistent states of the two problems are in one-to-one correspondence.

**Equal energies.** Line by line, for the quantities of Section 19.4:

- $\sum gf\varepsilon$ is the same: the same $g$, $f$ and $\varepsilon$.
- $e_{\rm int}(n, -S) = e_{\rm int}(n, S)$ at every $y$ (Step 3), so $2\,\mathrm{Vol}_7\int e^{6Hy}e_{\rm int}\,dy$ is the same.
- Hence $E_{KS}$ is the same; $S_{\rm ent}$ is the same (it contains only $g$ and $f$); $\Omega$ is the same (the same levels, $\mu$, $T$ and interaction integral); and $F = \Omega + \mu N$ is the same.

**Equal energy-momentum profiles.** Term by term in the formulas of Section 19.4:

- $\rho = \sum wgf\,\varepsilon n_o - e_{\rm int}$: $n_o$ and $e_{\rm int}$ are unchanged, so $\rho(y)$ is unchanged.
- $p_3 = \sum wgf\,\frac{\kappa|k|}{3}t_o + e_{\rm int}$: $t_o$ is unchanged, and so are $\kappa$ and $|k|$; $p_3(y)$ is unchanged.
- $p_t = e_{\rm int}$: unchanged.
- $p_8 = \sum wgf[(\varepsilon - v_v)n_o - M_{\rm eff}s_o - \kappa|k|t_o] + e_{\rm int}$: the only term with odd factors is $M_{\rm eff}s_o$, and it becomes $(-M_{\rm eff})(-s_o) = M_{\rm eff}s_o$, a product of two odd factors; $p_8(y)$ is unchanged.

So the four profiles are equal at every point $y$, while $S(y)$, $Q(y)$ and $M_{\rm eff}(y)$ change sign and $n(y)$, $t(y)$, $v_v(y)$, $e_{\rm int}(y)$ do not. The Kohn-Sham gap (the lowest empty level minus the highest occupied level) is a difference of two levels and is the same as well. Status: PROVED; checks `T3_energies_and_emt_profiles_equal` of `wolfram-t3.json` and `T3.energies_and_emt_profiles_equal` of `python-t3.json`; the sympy check takes three general occupied orbitals of both block types with arbitrary complex $\chi$, levels, occupations, degeneracies and momenta, and also verifies the control: with $(-m, -\lambda)$ the energy density differs. These are the four diagonal components of the energy-momentum tensor of the $2 \times 2$ reduction; that every other component and the current are equal too is statement S6 of the completion (Section 19.10; the third gap of the adversarial verification).

### 19.10 Theorem T3: the statement, its hypotheses and its records

**Hypotheses** (`Revision/pairing/kohn_sham/t3-theory.json`, hypotheses H1 to H6, in words):

- H1, the problem: the instantaneous Kohn-Sham problem of `Revision/kohn_sham/ks-theory.json` at a fixed slice $a_{4,0}$ of the author's metric, in the good sector, with a lattice of 3-momenta and the block Hamiltonians $h_j$ on $-L \le y \le 0$.
- H2, the functional: Hartree plus the exact exchange of the uniform gas, $M_{\rm eff} = m + \frac{15}{16}\lambda S$, $v_v = -\lambda n/16$, no correlation; the energy-momentum tensor of that record.
- H3, the brane, ASSUMED: the Z2 mirror construction at $y = 0$; both parities are solved and filled together with the weight $w_{Z2} = \tfrac12$.
- H4, the tip, chosen: $(1 - Q(\theta))\chi(-L) = 0$.
- H5, the occupations: Mermin's at fixed $N$, with the filling convention of the record.
- H6, the same remaining data for both members: the same $H$, $L$, $a_{4,0}$, lattice, extra-time volume, $N$ and $T$; mean-field (quasi-free) states only.

**Theorem T3 (the Kohn-Sham level of the pairing).** Under H1 to H6, the map $(\chi, j) \to (\sigma_2\chi, -j)$ at the same 3-momentum, which is the chirality $\Gamma$ of the 16-component orbital (up to the sign $s_2$ of each block), with the two brane parities exchanged and the tip angle $\theta \to \pi - \theta$, maps every self-consistent instantaneous Kohn-Sham state with $(m, \lambda, \theta)$ onto a self-consistent Kohn-Sham state with $(-m, +\lambda, \pi - \theta)$, and conversely (the map is an involution). The two states have:

- S1: the same levels, orbital by orbital: the orbital of the type $j$ and the parity $p$ goes to the type $-j$ and the other parity, at the same momentum and the same level;
- S2: with the untransformed tip the spectra differ (Section 19.12);
- S3: the densities transform as $n \to n$, $t \to t$, $S \to -S$, $Q \to -Q$, so $M_{\rm eff} \to -M_{\rm eff}$ and $v_v \to v_v$; with $(-m, -\lambda)$ instead of $(-m, +\lambda)$ the map fails;
- S4: equal levels with their degeneracies, occupations, chemical potential, particle number, entropy, Kohn-Sham energy $E_{KS}$, grand potential $\Omega$ and free energy $F$, and equal profiles $\rho(y)$, $p_3(y)$, $p_t(y)$, $p_8(y)$; $S(y)$ and $Q(y)$ change sign;
- S5: inside the ASSUMED Z2 orbifold the mirror copy of a self-consistent state carries $(-m, +\lambda)$ (Section 19.11).

**The records.** Each step of the proof is a named check of two independent verifiers that share no code (with one exception at the time of the adversarial verification, the $v_v$ clause of Step 3, Section 19.8, closed by the completion below). Every check below has the verdict PASS.

| step | what it shows | `wolfram-t3.json` | `python-t3.json` |
| --- | --- | --- | --- |
| 1 | $\sigma_2h_j(M)\sigma_2 = h_{-j}(-M)$, also for $N$ | `T3_block_hamiltonian_map`, `T3_ode_map` | `T3.block_hamiltonian_map`, `T3.ode_map` |
| 2 | tip $\theta \to \pi - \theta$; parities exchanged; current and norm kept | `T3_tip_condition_map`, `T3_brane_parities_exchanged` | `T3.tip_condition_map`, `T3.brane_parities_exchanged` |
| 3 | $n, t$ even, $S, Q$ odd; the mean field closes for $(-m, +\lambda)$ only | `T3_orbital_densities`, `T3_mean_field_map` | `T3.orbital_densities`, `T3.mean_field_map` |
| 4 | equal energies and profiles | `T3_energies_and_emt_profiles_equal` | `T3.energies_and_emt_profiles_equal` |
| confirmations | exact $k = 0$ spectra; $\Gamma$ is the block map; the mirror copy | `T3_exact_k0_spectra`, `T3_Gamma_is_the_block_map`, `T3_z2_mirror_copy_carries_minus_m_plus_lambda` | `T3.exact_k0_spectra`, `T3.Gamma_is_the_block_map`, `T3.z2_mirror_copy_carries_minus_m_plus_lambda` |
| comparison | the sympy side confirms the Wolfram theorem record and its list of limits | none | `compare.t3_theory.theorem`, `compare.t3_theory.not_established` |
| numbers | the Rust solver's self-test (a confirmation, not a proof) | none | `T3.rust_selftest_numerical_confirmation` |

So `wolfram-t3.json` has 10 checks and `python-t3.json` 13 (the ten counterparts, the two comparisons and the numerical confirmation). The record `Revision/docs/PAIR_CREATION_PROOFS.md` (its section 8) collects the same proof.

**The numerical confirmation.** The Rust solver's report `Revision/kohn_sham/reports/ks-rust-solver.json` holds the check t3_block_map_solver_selftest: the problems $(m, \lambda, \theta = 0)$ and $(-m, \lambda, \theta = \pi)$, solved independently at the slice $a_{4,0} = 1$, gave the same sorted levels, occupations, Kohn-Sham energies and integrated energy-momentum components and the opposite $S$, with the worst difference $9.95\times10^{-14}$ against the tolerance $10^{-9}$ fixed in advance. For $N = 8$ and $\lambda = 0.01946$: $E_{KS} = -9.868426190876\times10^{-4}$ against $-9.868426190868\times10^{-4}$ (80 levels), while the control with the untransformed tip gave $-2.0145243719$. For $N = 136$ and $\lambda = 0.0009298$: $E_{KS} = 32.39294915318$ in both runs (160 levels), control $29.283751318$. Status: COMPUTED; the report itself labels it "NOT a proof of T3". Notebook 19a reproduces these numbers. This self-test of two states was the only numerical confirmation recorded with T3 (the fourth gap of the adversarial verification); the completion replaces it by the two demonstrations below.

**The completion of 2026-10-08.** An adversarial verification re-ran both T3 verifiers (they reproduce `t3-theory.json` and the two T3 reports byte for byte) and re-derived every step of the proof by hand. It found no error in the statement or the proof of T3, and five gaps, listed in `Revision/pairing/kohn_sham/t3-completion.json`, entry adversarial_verification. The completion is a separate record; T3, its hypotheses H1 to H6 and its statements S1 to S5 are unchanged. Its exact checks are those of `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json` (3 of 3 PASS) and `Revision/pairing/kohn_sham/reports/python-t3-completion.json` (7 of 7 PASS):

| gap | what was missing | Wolfram check | sympy check |
| --- | --- | --- | --- |
| 1 | the coefficients of the mean field were typed into the Wolfram script, and its $v_v$ clause compared an expression with itself (Section 19.8; the script has since been fixed at the root) | `T3C_mean_field_coefficients_from_ks_theory` | `T3C.mean_field_coefficients_from_ks_theory` |
| 2 | the filling convention was used for the partner without showing that its particle levels are the images of the original's (Section 19.9, item (iv)) | `T3C_filling_convention_mapped` | `T3C.filling_convention_mapped` |
| 3 | only the four diagonal energy-momentum components of the $2 \times 2$ reduction were proved equal (statement S6 below) | `T3C_krein_rule_16_component` | `T3C.krein_rule_16_component` |
| 4 | the numerical confirmation was the two-state self-test (the demonstrations below) | none | `T3C.rust_demo_numerical_demonstration`, `T3C.reference_demo_numerical_demonstration` |
| 5 | `t3-theory.json` does not name the history of the numerical states a PRESCRIBED BACKGROUND; the completion record does | none | none |
| all | the T3 reports pass; the sympy side confirms the completion record | none | `T3C.t3_reports_pass`, `compare.t3_completion` |

**Statement S6: the 16-component expectation rule.** Steps 3 and 4 work with the $2 \times 2$ blocks and the four diagonal components $\rho$, $p_3$, $p_t$, $p_8$. S6 says: with the expectation rule $\rho = \sum f\,uu^\dagger B$ of Section 19.4 (here $\rho$ is the $16 \times 16$ matrix of the rule, not the energy density), the image state, whose orbitals are $u' = \Gamma u$, has $\rho' = -\Gamma\rho\Gamma$, so $n$ is unchanged, $S$ and $Q$ change sign, and every component of the energy-momentum tensor and of the current $J^a = \langle\bar\Psi\gamma^{(x_a)}\Psi\rangle$ is unchanged. The derivation, line by line. First, because $B^2 = 1$, multiplying $\rho = \sum f\,uu^\dagger B$ from the right by $B$ gives

$$
\sum f\,uu^\dagger = \rho B .
$$

Rule: $BB = 1$. Then, for the image orbitals,

$$
\rho' = \sum f\,(\Gamma u)(\Gamma u)^\dagger B = \sum f\,\Gamma uu^\dagger\Gamma^\dagger B = \Gamma\Big(\sum f\,uu^\dagger\Big)\Gamma B = \Gamma\rho B\Gamma B .
$$

Rule: $(\Gamma u)^\dagger = u^\dagger\Gamma^\dagger$; $\Gamma^\dagger = \Gamma$ (real and diagonal, Section 19.5); the constant matrix $\Gamma$ comes out of the sum; the line before. Now $\Gamma B = -B\Gamma$ (Section 19.5), so

$$
B\Gamma B = -\Gamma BB = -\Gamma, \qquad \rho' = \Gamma\rho(B\Gamma B) = -\Gamma\rho\Gamma .
$$

Rule: replace $B\Gamma$ by $-\Gamma B$, then $BB = 1$. The expectation value of any $16 \times 16$ matrix $X$ in the image state is then

$$
\langle X\rangle' = \mathrm{Tr}(X\rho') = -\mathrm{Tr}(X\Gamma\rho\Gamma) = -\mathrm{Tr}(\Gamma X\Gamma\rho) .
$$

Rule: the trace does not change when the factors are moved around in a circle; here the last factor $\Gamma$ is moved to the front. Section 19.5 showed $\Gamma X\Gamma = +X$ when $X$ is a number times a product of an even number of gammas, and $\Gamma X\Gamma = -X$ for an odd number. Hence **an even product changes sign**, $\langle X\rangle' = -\langle X\rangle$, and **an odd product is unchanged**, $\langle X\rangle' = +\langle X\rangle$. Line by line for the quantities of the theory:

| quantity | matrix $X$ | gammas in $X$ | in the image state |
| --- | --- | --- | --- |
| charge density $n$ | $B = -iC\gamma^{(x_4)}$ | 5, odd | unchanged |
| scalar density $S$ | $C$ | 4, even | sign reversed |
| density $Q$ | $B\gamma^{(x_8)}$ | 6, even | sign reversed |
| current $J^a$ | $C\gamma^{(x_a)}$ | 5, odd | unchanged |
| kinetic bilinears $\bar\Psi\gamma^{(x_a)}\partial\Psi$ | $C\gamma^{(x_a)}$ | 5, odd | unchanged |
| spin-connection bilinears $\bar\Psi\gamma^{(x_a)}S^{bc}\Psi$ | $C\gamma^{(x_a)}S^{bc}$ | 7, odd | unchanged |

Rule for the table: $C$ has four gammas, so $B = -iC\gamma^{(x_4)}$ has five, $B\gamma^{(x_8)}$ six and $C\gamma^{(x_a)}$ five, and $S^{bc} = \frac14(\gamma^{(x_b)}\gamma^{(x_c)} - \gamma^{(x_c)}\gamma^{(x_b)})$ adds two; a constant factor such as $-i$ or $\frac14$ does not matter, and $\Gamma$ is constant, so it passes through the derivative $\partial$. The energy-momentum tensor is built from the kinetic and spin-connection bilinears (unchanged), from the mass term $mS$ and from $U = \frac{\lambda}{2}S^2$: with $m \to -m$ and $S \to -S$ the product $mS$ is unchanged, and with the same $\lambda$ so is $U$. So every component of the 16-component energy-momentum tensor and every component of the current are the same in the two members, while $S$ and $Q$ change sign. The record verifies each ingredient with the author's matrices of `Revision/algebra/gammas.json`: $\Gamma^2 = 1$, $\Gamma B\Gamma = -B$, $\Gamma C\Gamma = C$, $\Gamma\gamma^{(x_a)}\Gamma = -\gamma^{(x_a)}$ for all eight $a$, $\Gamma S^{ab}\Gamma = S^{ab}$ for all 64 pairs, $(\Gamma u)(\Gamma u)^\dagger B = -\Gamma(uu^\dagger B)\Gamma$ for a general 16-component $u$, and the 8 + 512 kinetic bilinears. Status: PROVED; checks T3C_krein_rule_16_component and T3C.krein_rule_16_component. S6 is an equality of expectation values in Kohn-Sham (quasi-free) states with the fixed Krein matrix $B$, not a statement about two independently quantised universes.

**The two numerical demonstrations** (status COMPUTED; demonstrations, not part of the proof). Each solves, at the slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$ of the PRESCRIBED BACKGROUND history, three members of every state: **plus**, the universe $(m, \lambda)$ with the tip angle $0$ (the A of Section 19.17); **image**, the universe $(-m, +\lambda)$ with the tip angle $\pi$ (B); and **control**, $(-m, +\lambda)$ with the untransformed tip angle $0$ (C).

- The Rust solver (`Revision/pairing/kohn_sham/reports/t3-rust-demo.json`, 7 of 7 checks PASS; table `Revision/pairing/kohn_sham/numerics/results/t3-rust-states.csv`) on all 210 states of the canonical matrix: 75 ground states ($N = 8, 136, 688$; $\lambda = 0, \pm\lambda_1, \pm\lambda_2$; five slices) and 135 Mermin states ($\lambda = 0, \pm\lambda_1$ at $T = 0.01, 0.02, 0.05$), 630 runs in all. The plus members reproduce the committed canonical matrix to $2.538\times10^{-10}$. Image equals plus to $2.179\times10^{-13}$ in the ground states and $3.877\times10^{-12}$ in the thermal states (tolerance $10^{-9}$): the levels label by label with the sector map $(n_2, j, \text{parity}) \to (n_2, -j, \text{other parity})$, the occupations, $E_{KS}$, $\mu$, the entropy, $\Omega$, $F$, the gap, the energy-momentum integrals, the even profiles point by point, and $S$, $Q$, $M_{\rm eff}$ with the opposite sign. The control differs from plus: its density profile $n(y)$ differs by at least $4.750$ times the maximum of $n$ (state N8_lamm1_a15) in the 196 states where the solver found a control state; in the other 14 states, all with $\lambda < 0$, the self-consistency loop of the control diverges, which the record reports as such and not as a proof that no such state exists. A second control, the T1 parameters $(-m, -\lambda)$ with the tip angle $\pi$, differs from plus by at least $1.21\times10^{-2}$ in all 150 states with $\lambda \ne 0$: the Kohn-Sham partner carries $+\lambda$. The agreement of image and plus is at the rounding level **by construction**, because the solver's shooting is covariant under the map (Section 19.17 shows why); it tests the solver's handling of the transformed boundary conditions, the labels, the filling convention, the self-consistency loop and the Mermin root, not the discretisation.
- The independent reference solver (`Revision/pairing/kohn_sham/reports/t3-reference-demo.json`, 7 of 7 checks PASS; Chapter 16): finite differences on grids of 300, 600 and 1200 points, combined by Richardson extrapolation (the combination of the three grids in which the leading discretisation error cancels), on 18 states (13 ground, 5 Mermin). Its frame for the image is not the discrete image of the plus frame, so on a single grid the levels of the two members differ by up to $2.23\times10^{-4}$; after the extrapolation image equals plus to $2.043\times10^{-14}$ (ground) and $3.038\times10^{-14}$ (thermal). This is the test that does not depend on the discretisation: a statement about the continuum problem. The exact zero-momentum image spectra are reproduced to $2.80\times10^{-14}$; the control's density differs by at least $5.296$ times the maximum (3 states without a converged control, all with $\lambda < 0$); and the $-M$ universe of the reference solver equals the $-M$ universe of the Rust solver to $1.255\times10^{-11}$.

**What the completion adds to the list of what is not established** (`t3-completion.json`, entry not_established): the demonstrations show the equalities only on the states solved, to their stated tolerances, and control states for which a solver found no self-consistent solution are reported as such, not as a proof that none exists; S6 is not a statement about two independently quantised universes; the filling convention is a CONVENTION whose justification is OPEN. Section 19.22 collects the whole list.

### 19.11 Why T3 is not T1, and the mirror copy in the Z2 orbifold

**Two theorems, one matrix.** T1 (Chapter 18) and T3 are both built on the chirality $\Gamma$, yet T1 pairs $(m, \lambda)$ with $(-m, -\lambda)$ at opposite energies and T3 pairs $(m, \lambda, \theta)$ with $(-m, +\lambda, \pi - \theta)$ at equal energies. There is no contradiction, because they speak about different quantities.

- T1 is about the **classical bilinears** $\Psi^\dagger X\Psi$ of the field. Under $\Psi \to \Gamma\Psi$ such a bilinear becomes $\Psi^\dagger\Gamma X\Gamma\Psi$, and $\Gamma X\Gamma = +X$ for an even product of gammas, $-X$ for an odd one (Section 19.5).
- T3 is about the **expectation values** $u^\dagger BXu$ of the quantised theory (Section 19.4), which contain one more factor, the Krein matrix $B$. Under $u \to \Gamma u$ they become $u^\dagger\Gamma BX\Gamma u = u^\dagger(\Gamma B\Gamma)(\Gamma X\Gamma)u = -u^\dagger B(\Gamma X\Gamma)u$, because $\Gamma B\Gamma = -B$ (Section 19.5) and $\Gamma\Gamma = 1$.

So every sign of T1 is reversed at the Kohn-Sham level. Line by line for the two densities that matter:

| quantity | matrix $X$ | gammas in $X$ | classical bilinear (T1) | Kohn-Sham density (T3) |
| --- | --- | --- | --- | --- |
| scalar density $S$ | $C$ | 4, even | unchanged | sign reversed |
| charge density $n$ | $B$ | 5, odd | sign reversed | unchanged |

The classical scalar density is unchanged under $\Gamma$ (`Revision/pairing/reports/python-pairing.json`, checks T1.metric.grassmann.S_invariant and T1.metric.commuting.S_invariant) and the classical current is reversed (checks T1.metric.grassmann.current and T1.metric.commuting.current); then self-consistency of the mass term $m + \lambda S$ in the field equation $\gamma^\mu D_\mu\Psi = (m + \lambda S)\Psi$, whose left side changes sign under $\Gamma$, requires $(m, \lambda) \to (-m, -\lambda)$. At the Kohn-Sham level $S$ changes sign and $n$ does not, and the same requirement gives $(m, \lambda) \to (-m, +\lambda)$, as Step 3 found. The record states this comparison as an interpretation, labelled as such and not as a theorem: in its parameters the Kohn-Sham map is of the T2 type (same coupling, equal energies), although its matrix is the chirality of T1 (`t3-theory.json`, entry relation_to_T1_T2; section 8.4 of the record `Revision/docs/PAIR_CREATION_PROOFS.md`).

**The mirror copy inside the Z2 orbifold.** The brane condition of Section 19.3 comes from the ASSUMED Z2 construction: the patch $-L \le y \le 0$ is glued at $y = 0$ to its mirror image $0 \le y \le L$. On the doubled interval the record uses the reflection $P_A$: $\chi(y) \to \phi(y) = \sigma_3\chi(-y)$. Write $h(M, \kappa, v) = -i\sigma_1\frac{d}{dy} + M\sigma_2 + \kappa k\sigma_3 + v$ (the type $j$ is a common factor and plays no role here). Line by line, with $\frac{d\phi}{dy}(y) = -\sigma_3\chi'(-y)$ (chain rule):

$$
\begin{aligned}
h\big(-M(-y), \kappa(-y), v(-y)\big)\phi &= i\sigma_1\sigma_3\chi'(-y) - M(-y)\sigma_2\sigma_3\chi(-y) \\
&\quad + \kappa(-y)k\,\sigma_3\sigma_3\chi(-y) + v(-y)\sigma_3\chi(-y) ,
\end{aligned}
$$

$$
\begin{aligned}
\sigma_3\big(h(M, \kappa, v)\chi\big)(-y) &= -i\sigma_3\sigma_1\chi'(-y) + M(-y)\sigma_3\sigma_2\chi(-y) \\
&\quad + \kappa(-y)k\,\sigma_3\sigma_3\chi(-y) + v(-y)\sigma_3\chi(-y) .
\end{aligned}
$$

Rule: insert $\phi$ in the first line; multiply $h\chi$ at the point $-y$ by $\sigma_3$ in the second. The two lines are equal term by term, because $\sigma_1\sigma_3 = -\sigma_3\sigma_1$ and $\sigma_2\sigma_3 = -\sigma_3\sigma_2$. So $P_A$ maps an orbital of the mass function $M(y)$ onto an orbital of the mass function $-M(-y)$, with the potential $v(-y)$ (check bc_mirror_map_PA of the Kohn-Sham theory reports). The doubled problem has one mass function on the whole interval, so it is symmetric under $P_A$ exactly when $M_{\rm eff}(y) = -M_{\rm eff}(-y)$: the mass is **odd** across the brane. Under $\sigma_3$, $n_o$ is unchanged and $s_o$ changes sign ($\sigma_3\sigma_2\sigma_3 = -\sigma_2$), so on the mirror side $n(y) = n(-y)$ and $S(y) = -S(-y)$. If the mirror side has the parameters $(\tilde m, \tilde\lambda)$, its mass at a point $y > 0$ is, line by line,

$$
\tilde m + \frac{15}{16}\tilde\lambda S(y) = \tilde m - \frac{15}{16}\tilde\lambda S(-y) ,
$$

and it must equal $-M_{\rm eff}(-y) = -m - \frac{15}{16}\lambda S(-y)$ for every value of $S(-y)$; its potential $-\tilde\lambda n(y)/16 = -\tilde\lambda n(-y)/16$ must equal $v_v(-y) = -\lambda n(-y)/16$. Comparing the terms with and without the densities gives $\tilde\lambda = \lambda$ and $\tilde m = -m$: **inside the ASSUMED orbifold, the mirror copy of a self-consistent state of the universe of mass $+M$ is a universe of mass $-M$ with the same coupling**, the statement S5 (checks T3_z2_mirror_copy_carries_minus_m_plus_lambda and T3.z2_mirror_copy_carries_minus_m_plus_lambda; bc_mirror_parities_of_densities). This is a property of the assumed geometric construction, not a derivation that such a pair exists or was created.

### 19.12 The exact levels at zero momentum, and what goes wrong without the transformed tip

Without the 3-momentum ($k = 0$) and without the interaction ($M_{\rm eff} = M$ constant, $v_v = 0$) the block equation can be solved exactly. This gives T3 a second, independent confirmation, and it shows exactly what happens to the **control** C: the universe of mass $-M$ with the UNtransformed tip angle $\theta = 0$.

**The square of N.** With $k = 0$ and $v = 0$, $N = M\sigma_3 + ij\varepsilon\sigma_1$. Line by line:

$$
N^2 = M^2\sigma_3^2 + Mij\varepsilon\,(\sigma_3\sigma_1 + \sigma_1\sigma_3) + (ij\varepsilon)^2\sigma_1^2 = M^2\,\mathbf 1 + 0 - \varepsilon^2\,\mathbf 1 = (M^2 - \varepsilon^2)\,\mathbf 1 .
$$

Rule: multiply out the square of a sum of two matrices, keeping the order of the factors; $\sigma_3^2 = \sigma_1^2 = \mathbf 1$; $\sigma_3\sigma_1 + \sigma_1\sigma_3 = 0$; $(ij)^2 = i^2j^2 = -1$. Write $p = \sqrt{M^2 - \varepsilon^2}$; inside the mass gap ($\varepsilon^2 < M^2$) $p$ is real, outside it $p = ir$ with the real $r = \sqrt{\varepsilon^2 - M^2}$.

**The solution.** $\chi(y) = e^{Ny}\chi(0)$, with the matrix exponential $e^{Ny} = \sum_{n \ge 0}(Ny)^n/n!$. The even powers are $N^{2r} = p^{2r}\mathbf 1$ and the odd ones $N^{2r+1} = p^{2r}N$, so

$$
e^{Ny} = \sum_{r \ge 0}\frac{(py)^{2r}}{(2r)!}\,\mathbf 1 + \sum_{r \ge 0}\frac{p^{2r}y^{2r+1}}{(2r+1)!}\,N = \cosh(py)\,\mathbf 1 + \frac{\sinh(py)}{p}\,N .
$$

Rule: the series $\cosh x = \sum x^{2r}/(2r)!$ and $\sinh x = \sum x^{2r+1}/(2r+1)!$. Check: $\frac{d}{dy}e^{Ny} = p\sinh(py) + \cosh(py)N$ and $Ne^{Ny} = \cosh(py)N + \frac{\sinh(py)}{p}N^2 = \cosh(py)N + p\sinh(py)$: the same. At the tip $y = -L$, since $\cosh$ is even and $\sinh$ odd,

$$
\chi(-L) = \Big[\cosh(pL)\,\mathbf 1 - \frac{\sinh(pL)}{p}\,N\Big]\chi(0) .
$$

**The characteristic functions.** Start at the brane with the parity, $\chi(0) = (1, 0)$ (even) or $(0, 1)$ (odd), go to the tip, and take the component that the tip condition must make zero: as a function of $\varepsilon$ this is the **characteristic function** $D(\varepsilon)$, and its zeros are the levels. The matrix $N$ has the columns $N(1, 0) = (M, ij\varepsilon)$ and $N(0, 1) = (ij\varepsilon, -M)$. Line by line, for the three universes:

| universe | mass, type, tip | even: $\chi(0) = (1, 0)$ | odd: $\chi(0) = (0, 1)$ |
| --- | --- | --- | --- |
| A | $M$, $j$, $\theta = 0$: $\chi_2(-L) = 0$ | $D = -ij\varepsilon\,\sinh(pL)/p$ | $D = \cosh(pL) + M\sinh(pL)/p$ |
| B | $-M$, $-j$, $\theta = \pi$: $\chi_1(-L) = 0$ | $D = \cosh(pL) + M\sinh(pL)/p$ | $D = +ij\varepsilon\,\sinh(pL)/p$ |
| C | $-M$, $j$, $\theta = 0$: $\chi_2(-L) = 0$ | $D = -ij\varepsilon\,\sinh(pL)/p$ | $D = \cosh(pL) - M\sinh(pL)/p$ |

Rule, for example for B odd: with the mass $-M$ and the type $-j$, $N(0, 1) = (-ij\varepsilon, +M)$, and the first component of $\chi(-L)$ is $0\cdot\cosh(pL) - \frac{\sinh(pL)}{p}(-ij\varepsilon) = ij\varepsilon\sinh(pL)/p$. The other entries follow the same way. Reading the table: **B even is A odd, and B odd is minus A even**: the two problems have the same levels, with the parities exchanged, as T3 says. **C even is A even, but C odd is not A odd**: the control differs in the odd sector. Status: PROVED; checks T3_exact_k0_spectra and T3.exact_k0_spectra (identically in $\varepsilon$, $M$, $L$ and for both $j$, with the control).

**The levels of A (and B).** Even: $\varepsilon\sinh(pL)/p = 0$. Inside the gap $p > 0$ and $\sinh(pL) > 0$, so only $\varepsilon = 0$: the **zero mode**. Outside the gap $\sinh(irL)/(ir) = \sin(rL)/r$, so $\sin(rL) = 0$, $r = n\pi/L$ and $\varepsilon = \pm\sqrt{M^2 + (n\pi/L)^2}$, $n = 1, 2, 3, \dots$ Odd: $\cosh(pL) + M\sinh(pL)/p = 0$. Inside the gap both terms are positive (for $M > 0$): **no level in the gap**. Outside, $\cos(rL) + M\sin(rL)/r = 0$, that is $\tan(rL) = -r/M$ (check bc_exact_k0_spectra of the Kohn-Sham theory reports).

**The levels of C, and the level inside the gap.** Odd: $\cosh(pL) - M\sinh(pL)/p = 0$. Inside the gap, with $p = q$ real, this is $\cosh(qL) = M\sinh(qL)/q$, that is

$$
\tanh(qL) = \frac{q}{M} .
$$

The function $u(q) = \tanh(qL) - q/M$ has $u(0) = 0$, the slope $u'(0) = L - 1/M = 2$ for $M = 1$, $L = 3$ (positive), and $u(M) = \tanh(ML) - 1 < 0$; it is concave for $q > 0$ (because $\tanh$ is), so it has exactly one root $q$ in $(0, M)$. The level is, line by line,

$$
\varepsilon_b^2 = M^2 - q^2 = M^2 - M^2\tanh^2(qL) = \frac{M^2}{\cosh^2(qL)}, \qquad \varepsilon_b = \frac{M}{\cosh(qL)} .
$$

Rule: $q = M\tanh(qL)$ from the condition; $1 - \tanh^2 = 1/\cosh^2$. For $M = 1$, $L = 3$: $q = 0.994901528453$ and $\varepsilon_b = 0.100851121375$ (Notebook 19a, Out [18]; Notebook 19b finds the same level as a zero of $D$). Outside the gap the odd levels of C obey $\tan(rL) = +r/M$, and no odd level of C equals an odd level of A: if $\cos(rL) + M\sin(rL)/r = 0$ and $\cos(rL) - M\sin(rL)/r = 0$ both held, their sum would give $\cos(rL) = 0$ and their difference $\sin(rL) = 0$, impossible because $\cos^2 + \sin^2 = 1$.

**The numbers.** For $M = 1$, $L = 3$, below $\varepsilon = 4$ (Notebook 19b, Out [13] and Out [16]):

| sector | levels |
| --- | --- |
| A even = B odd = C even | 0, 1.4479719304, 2.3208814802, 3.2969083095 |
| A odd = B even | 1.2922928281, 2.0106285600, 2.9119358754, 3.8829900326 |
| C odd | 0.1008511214, 1.6875789860, 2.6839784554, 3.7115109122 |

The even levels are $\sqrt{1 + (n\pi/3)^2}$ for $n = 1, 2, 3$. The levels of A reproduce the analytic table `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv` to $8.9\times10^{-16}$, and the lowest odd level $1.2922928281$ is the "bulk edge" of `Revision/kohn_sham/results/parameters.json`. For $v = 0$ the levels of the type $-j$ are the negatives of those of the type $j$, so each ladder is symmetric about zero.

**Where the zero modes live.** At $\varepsilon = 0$, $N = M\sigma_3$, so $\chi_1' = M\chi_1$ and $\chi_2' = -M\chi_2$. For A (even, $\chi_2(0) = 0$) this forces $\chi_2 = 0$ everywhere and $\chi = (e^{My}, 0)$, which also obeys the tip condition $\chi_2(-L) = 0$: a zero mode **largest at the brane**. For B (mass $-M$, so $\chi_1' = -M\chi_1$, $\chi_2' = M\chi_2$; odd, $\chi_1(0) = 0$) it gives $\chi = (0, e^{My})$, again largest at the brane, the image $\sigma_2(e^{My}, 0) = (0, ie^{My})$ up to the factor $i$. For C (mass $-M$, even) it gives $\chi = (e^{-My}, 0)$: a zero mode **largest at the tip**. The coordinate density $e^{6Hy}n(y)$ of a zero mode is $|\chi|^2/(\ell^3v_t)$, proportional to $e^{2My}$ for A and B and to $e^{-2My}$ for C; its value at the brane divided by its value at the tip is $e^{2ML} = e^6 = 403.4288$ for A and B and $e^{-6} = 0.002478752$ for C (Notebook 19a, Out [17]).

**The brane band and its slope.** When a small 3-momentum $k$ is switched on, the zero mode becomes the lowest level of the **brane band**. Its slope follows from the Hellmann-Feynman rule with $\delta h = \frac{\partial h_j}{\partial k}k = jk\kappa\sigma_3$, $\kappa = e^{-Hy}$ at the slice $a_{4,0} = 0$. For A ($j = 1$, $\chi = (e^{My}, 0)$, $\chi^\dagger\sigma_3\chi = e^{2My}$), line by line:

$$
c = \frac{\int_{-L}^{0}e^{-Hy}e^{2My}\,dy}{\int_{-L}^{0}e^{2My}\,dy} = \frac{(1 - e^{-(2M - H)L})/(2M - H)}{(1 - e^{-2ML})/(2M)} = \frac{2M}{2M - H}\cdot\frac{1 - e^{-(2M - H)L}}{1 - e^{-2ML}} .
$$

Rule: $\int_{-L}^{0}e^{\alpha y}dy = (1 - e^{-\alpha L})/\alpha$, with $\alpha = 2M - H$ and $\alpha = 2M$. For B ($j = -1$, $\chi = (0, ie^{My})$): $j\chi^\dagger\sigma_3\chi = (-1)(-e^{2My}) = e^{2My}$, the same integrand: **the same slope**. For C ($j = 1$, $\chi = (e^{-My}, 0)$):

$$
c_{\rm ctrl} = \frac{\int_{-L}^{0}e^{-(2M + H)y}\,dy}{\int_{-L}^{0}e^{-2My}\,dy} = \frac{2M}{2M + H}\cdot\frac{e^{(2M + H)L} - 1}{e^{2ML} - 1} .
$$

Rule: $\int_{-L}^{0}e^{-\beta y}dy = (e^{\beta L} - 1)/\beta$. For $M = H = 1$, $L = 3$: $c = 2/(1 + e^{-3}) = 1.9051482536449$ (`ks-theory.json`, entry checksNumeric; check brane_band_slope; `Revision/kohn_sham/results/spectrum/brane-band-slope.csv`) and $c_{\rm ctrl} = 13.4219751976$, about seven times larger (Notebook 19b, Out [19]). The reason is visible in the integrands: the control's zero mode lives at the tip, where the redshift weight $\kappa = e^{-Hy}$ is largest ($e^{3}$ at $y = -3$), so a 3-momentum costs it much more energy. At a later slice both slopes are multiplied by $e^{-a_{4,0}}$, the redshift.

**Summary of the control.** With the untransformed tip, three things go wrong at once: the zero modes move from the brane to the tip; a level appears inside the mass gap, $\varepsilon_b = 0.1009$; and the brane band starts seven times steeper. The self-consistent states of C therefore differ from those of A in every number, as Notebook 19a shows. T3 is not an automatic symmetry of the solver: it needs exactly the transformed tip.

### 19.13 Example: the proof of T3 by hand (Notebook 19b)

Notebook 19b repeats Sections 19.5 to 19.12 with the computer, as far as possible exactly. It reads the author's eight gammas from the record, checks with whole numbers that they are real signed permutation matrices obeying the anticommutation rule, forms the chirality $\Gamma$, and shows that $\Gamma$ maps every block onto its partner block as $\pm\sigma_2$ (Section 19.5). With sympy it re-derives the four steps of the proof (Sections 19.6 to 19.9: the block Hamiltonian, the tip and brane conditions, the densities, the mean field), each time with the negative control, and reproduces the corresponding checks of `python-t3.json`. It computes the six characteristic functions of Section 19.12 symbolically, finds their zeros numerically, compares the levels of A with the analytic table of the record, finds the control's level inside the mass gap, finds all these levels a second time by shooting (Runge-Kutta integration from the tip to the brane), and measures the slopes of the brane band of A, B and C against the closed forms. It needs Python only (numpy, sympy, matplotlib), takes about 50 seconds (24.2 s in the recorded build on the computer that built this book), draws six figures and ends with the line ALL 19 CHECKS PASSED (notebook 19b).

<!-- NOTEBOOK 19b -->

### 19.16 Line-by-line walk-through of Notebook 19b

The notebook has 21 code cells, In [1] to In [21]. This section explains every line of every one of them, in order; the numbers that the cells print are in Section 19.15 under the labels Out [k]. In the notebook each code cell is preceded by a text cell that says what the cell does.

**In [1], the set-up cell.** It is the same in every notebook of the book except for the notebook's name; in notebooks that run a Rust program it has two more imports and one more function (the walk-through of Notebook 19a in Section 19.21 explains them). Its first 236 lines repeat the complete run instructions of Section 19.14 as **comment lines**: Python skips every line that starts with `#`; they are there so that the notebook file carries its own instructions. Line 237, a line of dashes, ends the instructions, and two lines of `=` signs around the title THE SET-UP mark where the code begins.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell

NOTEBOOK_ID = "19b"  # this notebook: chapter 19, example b
```

`import` loads a **module** (a part of Python or of an installed package) so that the cell can use it; the text after `#` on each line says what it is for. `json` reads and writes JSON files, the text format in which most Revision records are stored. `os` gives access to the operating system, here to read an environment variable. `textwrap` breaks long printed text into lines. `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or folder, written the same way on Windows, macOS and Linux. `matplotlib` is the plotting package and `matplotlib.pyplot` its drawing functions, called `plt` by convention. `Image` and `display` show a saved picture below a cell. The last line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"19b"`; the figure files are named after it.

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

`def` defines a **function**, a named piece of code that runs when it is called; the text in triple quotes under the `def` line is its **docstring**, a description that Python stores but does not run. `Path.cwd()` is the folder in which the notebook runs, and `.resolve()` writes it as a complete address. The list `[here, *here.parents]` holds this folder followed by its parent, the parent of that, and so on up to the top of the disk (the star unpacks the parents into the list); the `for` loop takes them one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back; if none does, `raise` stops the notebook with an error message that says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))


def repository_file(relative):
    """The path of the repository file relative, for READING (a Revision record)."""
    return REPO / relative


def output_file(relative):
    """The path at which to WRITE the repository file relative (its folder is made)."""
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`REPO` is the repository folder; it is never printed, because it differs from computer to computer while the printed output must be the same everywhere. `os.environ.get(name, default)` reads an **environment variable** (a named text that a program receives from the computer) or returns the default; when you run the notebook the variable TEXTBOOK_OUTPUT_ROOT is not set, so `OUTPUT_ROOT` is the repository, while the book's checking tool sets it to a scratch folder so that a check never changes the repository. `repository_file` gives the full path of a repository file for reading; `output_file` gives the full path at which to write one, after creating its folder (`mkdir` with `parents=True` creates missing parent folders too, and `exist_ok=True` makes it do nothing if the folder exists). `say` prints a text in lines of at most 89 characters, continuation lines starting with four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})

FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

`matplotlib.rcdefaults()` returns to the built-in plotting settings, so that the figures are the same on every computer, and `plt.rcParams.update` sets the figure size (7.0 by 4.2 inches), the letter size (10 points) and a faint grid. The braces `{...}` make a **dictionary**: pairs of a key and a value, written `key: value`. A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/19b.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty dictionary `{}` into the captions file; `newline="\n"` stores the same line end on every operating system.

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

`save_figure` numbers the figures 1, 2, 3, ... in the order in which they are saved (`setdefault` returns the number already stored for this name, or stores one more than the count so far), saves the figure as a PNG file with 150 dots per inch, cut to its content and without the program's name in the file (so that two runs write the same bytes), closes it, records its caption in the captions file (`json.dumps` turns the dictionary into JSON text, one entry per line, keys sorted), shows the saved picture below the cell and prints where it was saved. The caption given to it is the caption that the book prints under the figure.

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


def report(label, value, unit=""):
    """Print a key number as a line "RESULT <label> = <value> <unit>"."""
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    """Print the last line of the notebook: how many checks passed."""
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`PASSED` is an empty **list** (an ordered collection, in square brackets). `check` is the function behind every check of the notebook: if the statement `condition` is false, `raise AssertionError(...)` stops the notebook with an error that names the check; if it is true, the name is appended to `PASSED`, the line PASS followed by the name is printed, and a second line names the Revision record and its check when the argument `record` is given (`None` is Python's word for "nothing"). Python's own `assert` statement is not used, because Python started with the option `-O` skips it. `report` prints a key number as a line that starts with RESULT. `all_checks_passed` prints the last line of the notebook with the number of checks that passed (`len` is the length of a list). The last statement prints the one output line of In [1].

**In [2], the eight gammas as whole numbers.**

```python
import csv  # reads the tables (CSV files) of the record
import math  # sqrt, pi, exp, sinh, cosh, tanh of single numbers

import numpy as np  # arrays of numbers
import sympy as sp  # exact symbolic algebra
from matplotlib.colors import ListedColormap  # a colour map with three colours
```

`csv` reads tables stored as CSV files (comma-separated values: one line per row, the entries separated by commas). `math` computes functions of single numbers. `numpy`, called `np`, holds arrays of numbers and multiplies matrices; `sympy`, called `sp`, computes with exact symbols, fractions and functions. `ListedColormap` makes a colour scale out of a short list of colours; it is used for the heat maps.

```python
GAMMAS = "Revision/algebra/gammas.json"  # the record of the gamma matrices
ALGEBRA = "Revision/algebra/reports/wolfram-algebra.json"  # its check report
fixture = json.loads(repository_file(GAMMAS).read_text(encoding="utf-8"))
stored_real = all(isinstance(g, list) for g in fixture["gamma"])  # no complex part
gamma = [np.array(g, dtype=int) for g in fixture["gamma"]]  # gamma[0] is x1
eta = [int(e) for e in fixture["eta"]]  # +1 +1 +1 -1 -1 -1 -1 +1
names = fixture["coordinates"]  # "x1", ..., "x8"
values = sorted({int(x) for g in gamma for x in g.flat})  # the values that occur
```

`GAMMAS` and `ALGEBRA` are the repository paths of the gamma record and of its Wolfram check report. `read_text` reads the record as text and `json.loads` turns it into Python objects: `fixture` is a dictionary whose keys are the names stored in the record. The record stores a real matrix as a plain list of rows and a complex one as a pair of real and imaginary parts (a dictionary), so `stored_real` is true when all eight entries of `fixture["gamma"]` are plain lists (`isinstance(g, list)` asks whether `g` is a list; `all` is true when every one is). `gamma` is the list of the eight matrices as numpy arrays of whole numbers (`dtype=int`), so that every product below is exact; Python counts list positions from 0, so `gamma[0]` is $\gamma^{(x_1)}$ and `gamma[7]` is $\gamma^{(x_8)}$. `eta` holds the eight signs of the frame metric, `names` the coordinate names. The **set comprehension** `{int(x) for g in gamma for x in g.flat}` collects every value that occurs in any matrix (`g.flat` runs through all 256 entries; a set keeps each value once), and `sorted` puts them in order.

```python
one_per_line = all(
    np.array_equal(np.abs(g).sum(axis=0), np.ones(16, dtype=int))
    and np.array_equal(np.abs(g).sum(axis=1), np.ones(16, dtype=int))
    for g in gamma)  # every column and every row holds one entry +1 or -1
say(f"{len(gamma)} matrices of size {gamma[0].shape}, entries {values}, "
    f"eta = {eta}")
check(stored_real and values == [-1, 0, 1] and one_per_line,
      "the eight gammas are real signed permutation matrices",
      record=f"{ALGEBRA}, checks reality and signed_permutation_matrices")
```

`np.abs(g)` replaces every entry by its absolute value; `.sum(axis=0)` adds each column, `.sum(axis=1)` each row. If the entries are $-1$, $0$, $+1$ and every column and every row sums to 1 in absolute value, then every row and every column holds exactly one nonzero entry $\pm1$: the matrix is a **signed permutation matrix**. `one_per_line` is true when this holds for all eight. Out [2] shows the line printed by `say` (eight $16 \times 16$ matrices, entries $-1, 0, 1$, and $\eta$) and the PASS line, which reproduces the checks reality and signed_permutation_matrices of `wolfram-algebra.json`.

**In [3], the eight heat maps (Figure 19b.1).**

```python
THREE = ListedColormap(["#2a78d6", "#ffffff", "#eb6834"])  # -1, 0, +1
fig, axes = plt.subplots(2, 4, figsize=(9.0, 4.9))
for a, ax in enumerate(axes.flat):
    ax.imshow(gamma[a], cmap=THREE, vmin=-1, vmax=1, interpolation="nearest")
    ax.set_title(f"$\\gamma^{{({names[a][0]}_{names[a][1]})}}$, "
                 f"$\\eta = {eta[a]:+d}$", fontsize=9)
    ax.set_xticks([0, 15])
    ax.set_yticks([0, 15])
    ax.tick_params(labelsize=7)
    ax.grid(False)
fig.tight_layout()
```

A colour is written `"#rrggbb"`, three two-digit numbers in base 16 for its red, green and blue parts; `THREE` is a colour scale with blue for $-1$, white for $0$ and orange for $+1$. `plt.subplots(2, 4, ...)` makes a figure with a grid of two rows of four **axes** (drawing areas), 9.0 by 4.9 inches. `enumerate(axes.flat)` runs through the eight axes and counts them, $a = 0, \dots, 7$. `imshow` draws a matrix as a picture, one coloured square per entry, with the colour scale fixed from $-1$ to $+1$ (`vmin`, `vmax`) and sharp squares (`interpolation="nearest"`). The title is an f-string that writes, for example, $\gamma^{(x_1)}$, $\eta = +1$: `names[a][0]` is the letter x and `names[a][1]` the digit, the doubled braces `{{` and `}}` produce single braces in the text, and `:+d` writes a whole number with its sign. The ticks are put only at 0 and 15, in small letters, and the grid is switched off. `tight_layout` arranges the eight pictures without overlaps.

```python
save_figure(fig, "eight_gammas",
            "The author's eight real $16 \\times 16$ gamma matrices "
            "$\\gamma^{(x_1)}, \\dots, \\gamma^{(x_8)}$ as heat maps (row index "
            "down, column index across, both from 0 to 15): blue is $-1$, white "
            "$0$, orange $+1$. Each matrix has exactly one nonzero entry in every "
            "row and every column. The four with $\\eta = +1$ (3-space and the "
            "hidden direction) are symmetric about the diagonal; the four with "
            "$\\eta = -1$ (the time and the three deflating extra times) are "
            "antisymmetric.")
```

`save_figure` saves Figure 19b.1 with its caption (Python joins strings written next to each other into one; a doubled backslash writes one backslash). What the student should see: eight square pictures of $16 \times 16$ coloured squares; in each row and each column exactly one square is coloured, the rest white; the four pictures of $x_1, x_2, x_3$ and $x_8$ are mirror-symmetric about the diagonal from top left to bottom right, and the four of $x_4, \dots, x_7$ are antisymmetric (a blue square on one side of the diagonal faces an orange one on the other). In [4] explains why.

**In [4], the anticommutation rule, exactly.**

```python
unit = np.eye(16, dtype=int)
worst = 0  # largest violation of the anticommutation rule (an integer)
for a in range(8):
    for b in range(8):
        anti = gamma[a] @ gamma[b] + gamma[b] @ gamma[a]
        rule = 2 * eta[a] * (a == b) * unit  # 2 eta^ab times the unit matrix
        worst = max(worst, int(np.max(np.abs(anti - rule))))
pattern = all(np.array_equal(g.T, e * g) for g, e in zip(gamma, eta))
say(f"largest violation of the anticommutation rule over 64 pairs: {worst}")
check(worst == 0 and pattern,
      "g^a g^b + g^b g^a = 2 eta^ab exactly; g^T = eta g (symmetry pattern)",
      record=f"{ALGEBRA}, checks Clifford_relation and symmetry_pattern")
```

`np.eye(16, dtype=int)` is the $16 \times 16$ unit matrix of whole numbers. The two loops run over all $8 \times 8 = 64$ pairs $(a, b)$; `@` multiplies matrices. `anti` is $\gamma^a\gamma^b + \gamma^b\gamma^a$ and `rule` is $2\eta^{ab}$ times the unit matrix: `(a == b)` is `True` (counted as 1) when $a = b$ and `False` (0) otherwise. `worst` keeps the largest absolute difference of any entry; with whole numbers it is exact. `pattern` checks the symmetry pattern seen in Figure 19b.1: `g.T` is the transpose, `zip(gamma, eta)` pairs each matrix with its sign, and the test is $(\gamma^a)^T = \eta^{aa}\gamma^a$. The reason, given in the text cell before the code: a signed permutation matrix $P$ obeys $P^TP = \mathbf 1$, and $\gamma^a\gamma^a = \eta^{aa}\mathbf 1$, so $(\gamma^a)^T = (\gamma^a)^T\gamma^a\gamma^a\eta^{aa} = \eta^{aa}\gamma^a$. Out [4] prints the largest violation, 0, and the PASS line, which reproduces the checks Clifford_relation and symmetry_pattern of `wolfram-algebra.json`.

**In [5], the chirality and the block map (Section 19.5).**

```python
Gamma = gamma[7]  # gamma^(x8) first ...
for a in range(7):
    Gamma = Gamma @ gamma[a]  # ... times gamma^(x1), ..., gamma^(x7)
diagonal = np.diag([-1] * 8 + [1] * 8)
anticommutes = all(np.array_equal(Gamma @ g, -(g @ Gamma)) for g in gamma)
check(np.array_equal(Gamma, diagonal) and np.array_equal(Gamma @ Gamma, unit)
      and np.array_equal(Gamma, np.array(fixture["Gamma"])) and anticommutes,
      "Gamma = diag(-1 (8 times), +1 (8 times)), Gamma^2 = 1, Gamma g^a = -g^a Gamma",
      record=f"{ALGEBRA}, checks Gamma_diag and Gamma_anticommutes_with_gammas")
```

`Gamma` starts as $\gamma^{(x_8)}$ and is multiplied from the right by $\gamma^{(x_1)}, \dots, \gamma^{(x_7)}$ in turn: the author's order of Section 19.5. `[-1] * 8 + [1] * 8` is the list of eight $-1$ followed by eight $+1$, and `np.diag` makes the diagonal matrix with these entries. `anticommutes` tests $\Gamma\gamma^a = -\gamma^a\Gamma$ for all eight. The check requires all four facts: $\Gamma$ is this diagonal matrix, $\Gamma^2 = \mathbf 1$, it equals the matrix stored in the record under the key `Gamma`, and it anticommutes with every gamma; it reproduces the checks Gamma_diag and Gamma_anticommutes_with_gammas of `wolfram-algebra.json`.

```python
KS_THEORY = "Revision/kohn_sham/ks-theory.json"
ks = json.loads(repository_file(KS_THEORY).read_text(encoding="utf-8"))
ENTRY = {"0": 0.0, "1": 1.0, "-1": -1.0, "I": 1j, "-I": -1j}  # the record's text
V = np.array([[ENTRY[x] for x in row]
              for row in ks["blockBasis"]["unnormalisedColumns2Sqrt2V"]])
V = V / (2.0 * math.sqrt(2.0))  # the record stores 2 sqrt(2) V
labels = [tuple(int(x) for x in label) for label in ks["blockBasis"]["labels"]]
pauli1 = np.array([[0, 1], [1, 0]], dtype=complex)
pauli2 = np.array([[0, -1j], [1j, 0]])
pauli3 = np.array([[1, 0], [0, -1]], dtype=complex)
unitary = float(np.max(np.abs(V.conj().T @ V - np.eye(16))))
```

`ks` is the Kohn-Sham theory record. It stores the block basis as $2\sqrt2\,V$, entry by entry as text: `"0"`, `"1"`, `"-1"`, `"I"`, `"-I"`; the dictionary `ENTRY` translates each text into a number (Python writes the imaginary unit $i$ as `1j`). The nested **list comprehension** `[[ENTRY[x] for x in row] for row in ...]` translates every entry of every row, `np.array` makes a $16 \times 16$ array of complex numbers, and the next line divides by $2\sqrt2$. `labels` is the list of the eight block labels $(j, s_2, s_3)$ as **tuples** (fixed groups of numbers in round brackets) of whole numbers. `pauli1`, `pauli2`, `pauli3` are the Pauli matrices as complex arrays. `unitary` is the largest entry of $|V^\dagger V - \mathbf 1|$: `.conj()` takes the complex conjugate of every entry and `.T` transposes, so `V.conj().T` is $V^\dagger$; for a unitary matrix this is 0 up to rounding.

```python
worst_map, worst_form = 0.0, 0.0
for b, (j, s2, s3) in enumerate(labels):
    p = labels.index((-j, s2, s3))  # the partner block
    Vb, Vp = V[:, 2 * b:2 * b + 2], V[:, 2 * p:2 * p + 2]
    worst_map = max(worst_map, float(np.max(np.abs(Gamma @ Vb
                                                    - Vp @ (s2 * pauli2)))))
    g8 = Vb.conj().T @ gamma[7] @ Vb  # gamma^(x8) inside block b
    g84 = Vb.conj().T @ gamma[7] @ gamma[3] @ Vb  # gamma^(x8) gamma^(x4) there
    worst_form = max(worst_form, float(np.max(np.abs(g8 - pauli3))),
                     float(np.max(np.abs(g84 - j * pauli1))))
```

The loop runs over the eight blocks: `b` is the number of the block and `(j, s2, s3)` its label. `labels.index((-j, s2, s3))` finds the number `p` of the partner block. `V[:, 2 * b:2 * b + 2]` takes all rows and the two columns $2b$ and $2b + 1$ (a **slice** `start:stop` runs up to, but not including, `stop`): the basis $V_b$ of the block, and $V_p$ likewise. `worst_map` keeps the largest entry of $|\Gamma V_b - V_p(s_2\sigma_2)|$: the statement $\Gamma V_b = V_p\,s_2\sigma_2$ of Section 19.5. `g8` is $V_b^\dagger\gamma^{(x_8)}V_b$, the block form of $\gamma^{(x_8)}$, and `g84` the block form of $\gamma^{(x_8)}\gamma^{(x_4)}$ (`gamma[3]` is $\gamma^{(x_4)}$); `worst_form` keeps their largest deviations from $\sigma_3$ and $j\sigma_1$, the two block forms that the proof of Section 19.5 uses.

```python
say(f"largest deviations: unitarity {unitary:.1e}, block map {worst_map:.1e}, "
    f"forms gamma^(x8) = sigma3 and gamma^(x8) gamma^(x4) = j sigma1 "
    f"{worst_form:.1e}")
check(unitary < 1e-12 and worst_map < 1e-12 and worst_form < 1e-12,
      "Gamma maps block (j, s2, s3) onto block (-j, s2, s3) as s2 sigma2",
      record="Revision/pairing/kohn_sham/reports/python-t3.json, check "
             "T3.Gamma_is_the_block_map")
```

`:.1e` writes a number in exponent form with one digit after the point. Out [5] shows the deviations: unitarity $1.1\times10^{-16}$ (rounding of the division by $2\sqrt2$), block map exactly 0, block forms $1.1\times10^{-16}$; the check, with the tolerance $10^{-12}$, reproduces T3.Gamma_is_the_block_map of `python-t3.json`. So the computer confirms $\tau = s_2$ of Section 19.5 for all eight blocks.

**In [6], Γ in the block basis (Figure 19b.2).**

```python
in_blocks = V.conj().T @ Gamma @ V  # Gamma in the block basis
real_part = float(np.max(np.abs(in_blocks.real)))
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 4.4))
left.imshow(Gamma, cmap=THREE, vmin=-1, vmax=1, interpolation="nearest")
left.set_title("$\\Gamma = \\gamma^{(x_8)}\\gamma^{(x_1)}\\cdots\\gamma^{(x_7)}$",
               fontsize=10)
right.imshow(in_blocks.imag, cmap=THREE, vmin=-1, vmax=1, interpolation="nearest")
right.set_title("imaginary part of $V^\\dagger\\Gamma V$ (block basis)", fontsize=10)
```

$V^\dagger\Gamma V$ is $\Gamma$ written in the block basis: its entry in row $r$ and column $c$ is the component along the $r$-th basis column of the image of the $c$-th one. `real_part` is the largest absolute real part of its entries. The figure has two axes side by side, `left` and `right` (the pair returned by `subplots(1, 2, ...)` is unpacked into two names). The left one shows $\Gamma$, the right one the imaginary part of $V^\dagger\Gamma V$ (`.imag`), both with the three-colour scale.

```python
tags = [f"({j:+d},{s2:+d},{s3:+d})" for j, s2, s3 in labels]
right.set_xticks([2 * b + 0.5 for b in range(8)])
right.set_xticklabels(tags, rotation=90, fontsize=6)
right.set_yticks([2 * b + 0.5 for b in range(8)])
right.set_yticklabels(tags, fontsize=6)
for edge in range(1, 8):
    right.axhline(2 * edge - 0.5, color="0.6", lw=0.5)
    right.axvline(2 * edge - 0.5, color="0.6", lw=0.5)
for ax in (left, right):
    ax.grid(False)
left.set_xticks([0, 7, 8, 15])
left.set_yticks([0, 7, 8, 15])
fig.tight_layout()
```

`tags` are the block labels written like `(+1,+1,+1)`. On the right picture each label is put in the middle of its two rows and columns ($2b + 0.5$), turned by 90 degrees on the horizontal axis. `axhline` and `axvline` draw thin grey lines (`"0.6"` is a grey level between black 0 and white 1, `lw` the line width) on the borders between the blocks, so that the eight $2 \times 2$ squares can be seen. The grid is switched off in both pictures, and the left one gets ticks at 0, 7, 8 and 15, where $\Gamma$ changes from $-1$ to $+1$.

```python
save_figure(fig, "gamma_block_map",
            "Left: the chirality $\\Gamma$, the product of the eight real gamma "
            "matrices, as a heat map (blue $-1$, white $0$, orange $+1$; indices 0 "
            "to 15): $-1$ on the first eight diagonal places, $+1$ on the last "
            "eight. Right: the imaginary part of $\\Gamma$ in the Kohn-Sham block "
            "basis, with the block labels $(j, s_2, s_3)$ on the axes. The nonzero "
            "$2 \\times 2$ squares join each block to the block with the opposite "
            "$j$ and the same $s_2, s_3$, and each square is $\\pm\\sigma_2$: this "
            "is the map $(\\chi, j) \\to (\\sigma_2\\chi, -j)$ of theorem T3.")
report("largest real part of V^dagger Gamma V", f"{real_part:.1e}")
```

`save_figure` saves Figure 19b.2, and `report` prints that the real part is at most $2.2\times10^{-17}$ (Out [6]), so the imaginary part is the whole matrix. What the student should see: on the left a diagonal line, blue in the upper half and orange in the lower half; on the right no square on the diagonal (no block is mapped into itself) but, in the upper-right and lower-left quarters, eight $2 \times 2$ squares, each joining a block $(j, s_2, s_3)$ to $(-j, s_2, s_3)$. Each square holds the pattern of $\sigma_2$, whose imaginary part is $-1$ above and $+1$ below its diagonal, or its negative: the blocks with $s_2 = +1$ show $+\sigma_2$, those with $s_2 = -1$ show $-\sigma_2$. This is $G = s_2\sigma_2$ of Section 19.5.

**In [7], Step 1 of the proof in sympy (Section 19.6).**

```python
y = sp.Symbol("y", real=True)  # the hidden coordinate
k, eps, vv = sp.symbols("k epsilon v_v", real=True)  # momentum, level, potential
Mf, kappa, vf = (sp.Function(name)(y) for name in ("M", "kappa", "v"))
chi = sp.Matrix([sp.Function("chi1")(y), sp.Function("chi2")(y)])  # any orbital
s1 = sp.Matrix([[0, 1], [1, 0]])  # the Pauli matrices, exactly
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
one = sp.eye(2)
```

`sp.Symbol("y", real=True)` makes an exact symbol $y$ that sympy treats as a real number; `sp.symbols` makes several at once: $k$, $\varepsilon$ and a constant potential $v_v$. `sp.Function(name)(y)` makes an **undetermined function** of $y$: sympy knows nothing about it except that it depends on $y$, so an identity proved with it holds for every function. `Mf`, `kappa`, `vf` are the functions $M(y)$, $\kappa(y)$, $v(y)$ (a generator expression in round brackets is unpacked into the three names), and `chi` is an arbitrary orbital $(\chi_1(y), \chi_2(y))$ as a sympy column. `s1`, `s2`, `s3` are the exact Pauli matrices (`sp.I` is $i$) and `one` the $2 \times 2$ unit matrix.

```python
def h(j, mass, c):
    """h_j(mass) applied to the two-component function c."""
    return j * (-sp.I * s1 * c.diff(y) + mass * s2 * c + kappa * k * s3 * c) + vf * c


def is_zero(matrix):
    """True when every entry simplifies to exactly 0."""
    return all(sp.simplify(sp.expand(entry)) == 0 for entry in matrix)
```

`h` applies the block Hamiltonian $h_j$ of Section 19.3, with the mass function `mass`, to a two-component function `c`: `c.diff(y)` is the derivative $dc/dy$, and the products `*` of sympy matrices are matrix products. `is_zero` is true when every entry of a matrix, multiplied out (`expand`) and simplified (`simplify`), is exactly 0.

```python
rules = (s2 * s1 * s2 == -s1 and s2 * s2 * s2 == s2 and s2 * s3 * s2 == -s3)
maps = all(is_zero(h(-j, -Mf, s2 * chi) - s2 * h(j, Mf, chi)) for j in (1, -1))
control = not is_zero(h(-1, Mf, s2 * chi) - s2 * h(1, Mf, chi))  # no M -> -M
Ms = sp.Symbol("M", real=True)
jj = sp.Symbol("j", real=True)
```

`rules` tests the three conjugation rules $\sigma_2\sigma_1\sigma_2 = -\sigma_1$, $\sigma_2^3 = \sigma_2$, $\sigma_2\sigma_3\sigma_2 = -\sigma_3$ of Section 19.6 (`==` compares two exact matrices). `maps` tests, for both block types, the identity $h_{-j}(-M)(\sigma_2\chi) - \sigma_2h_j(M)\chi = 0$ for the arbitrary functions: this is the statement "the image of every orbital is an orbital of the partner" in its strongest form, as an identity of differential operators. `control` is the negative control: without $M \to -M$ the difference is not zero. `Ms` and `jj` are a constant mass $M$ and a symbolic type $j$ for the next test.

```python
def N(j, mass):
    """The first-order matrix N of d chi/dy = N chi (constant data)."""
    return mass * s3 - sp.Symbol("kappa") * k * s2 + sp.I * j * (eps - vv) * s1


ode = (s2 * N(jj, Ms) * s2 - N(-jj, -Ms)).applyfunc(sp.expand) == sp.zeros(2, 2)
say(f"conjugation rules: {rules}; block map for both j: {maps}; control fails "
    f"as it must: {control}; first-order form: {ode}")
```

`N` is the matrix $N_j(M) = M\sigma_3 - \kappa k\sigma_2 + ij(\varepsilon - v)\sigma_1$ of the first-order form, with a constant symbol $\kappa$. `ode` tests $\sigma_2N_j(M)\sigma_2 - N_{-j}(-M) = 0$ with the symbolic $j$: `.applyfunc(sp.expand)` multiplies out every entry, and the result is compared with the $2 \times 2$ zero matrix. The `say` line prints the four truth values (Out [7]: all `True`).

```python
check(rules and maps and control,
      "sigma2 h_j(M) sigma2 = h_(-j)(-M) for arbitrary M(y), kappa(y), v(y)",
      record="Revision/pairing/kohn_sham/reports/python-t3.json, check "
             "T3.block_hamiltonian_map")
check(ode, "sigma2 N_j(M) sigma2 = N_(-j)(-M) for the first-order form",
      record="Revision/pairing/kohn_sham/reports/python-t3.json, check T3.ode_map")
```

Two checks, reproducing T3.block_hamiltonian_map and T3.ode_map of `python-t3.json`.

**In [8], Step 2: the tip and the brane (Section 19.7).**

```python
theta = sp.Symbol("theta", real=True)


def Q(angle):
    """The tip matrix Q(angle) = cos(angle) sigma3 + sin(angle) sigma2."""
    return sp.cos(angle) * s3 + sp.sin(angle) * s2


tip = (s2 * Q(theta) * s2 - Q(sp.pi - theta)).applyfunc(sp.simplify) == sp.zeros(2, 2)
e1 = sp.Matrix([1, 0])  # the vector (1, 0)
zero2 = sp.zeros(2, 1)
tip_control = ((one - Q(0)) * e1 == zero2 and (one - Q(0)) * (s2 * e1) != zero2
               and (one - Q(sp.pi)) * (s2 * e1) == zero2)
brane = s2 * (one - s3) * s2 == one + s3
```

`theta` is a symbolic angle and `Q` the tip matrix $Q(\theta)$. `tip` tests $\sigma_2Q(\theta)\sigma_2 = Q(\pi - \theta)$ for every $\theta$ (sympy simplifies $\cos(\pi - \theta)$ to $-\cos\theta$). `tip_control` is the control of Section 19.7: $(1, 0)$ obeys the condition $\theta = 0$; its image $\sigma_2(1, 0)$ violates it (`!=` means "is not equal") and obeys the condition $\theta = \pi$. `brane` tests $\sigma_2(1 - \sigma_3)\sigma_2 = 1 + \sigma_3$: the parities are exchanged.

```python
say(f"tip: sigma2 Q(theta) sigma2 = Q(pi - theta): {tip}; control: {tip_control}; "
    f"brane parities exchanged: {brane}")
check(tip and tip_control and brane,
      "tip angle theta -> pi - theta and the brane parities are exchanged",
      record="Revision/pairing/kohn_sham/reports/python-t3.json, checks "
             "T3.tip_condition_map and T3.brane_parities_exchanged")
```

Out [8] prints three `True` and the PASS line, reproducing two checks of `python-t3.json`.

**In [9], Step 3: the densities of one orbital (Section 19.8).**

```python
a1, b1, a2, b2 = sp.symbols("a1 b1 a2 b2", real=True)
psi = sp.Matrix([a1 + sp.I * b1, a2 + sp.I * b2])  # an arbitrary complex orbital


def densities(j, c):
    """(n, s, t, q, c) of one orbital c of block type j."""
    dag = c.H  # the row of complex conjugates
    return [sp.expand((dag * m * c)[0, 0]) for m in
            (one, j * s2, j * s3, s3, j * s1)]
```

Four real symbols make an arbitrary complex orbital $\psi = (a_1 + ib_1, a_2 + ib_2)$ at one point. `densities` returns the five densities $n_o, s_o, t_o, q_o, c_o$ without the common factor $P$: `c.H` is the conjugate transpose $c^\dagger$ (a row), and for each of the five matrices $\mathbf 1$, $j\sigma_2$, $j\sigma_3$, $\sigma_3$, $j\sigma_1$ the product $c^\dagger Xc$ is a $1 \times 1$ matrix whose only entry `[0, 0]` is multiplied out.

```python
SIGNS = (1, -1, 1, -1, 1)  # expected: n, t, c even; s, q odd
signs_ok = all(sp.expand(after - sign * before) == 0
               for j in (1, -1)
               for after, before, sign in zip(densities(-j, s2 * psi),
                                              densities(j, psi), SIGNS))
say(f"n = {densities(1, psi)[0]},  s (j = +1) = {densities(1, psi)[1]}")
check(signs_ok, "under the map n, t, c keep their sign, s and q change it",
      record="Revision/pairing/kohn_sham/reports/python-t3.json, check "
             "T3.orbital_densities")
```

`SIGNS` lists the expected signs of Section 19.8. For both $j$ the test compares each density of the image $(\sigma_2\psi, -j)$ with the sign times the density of $(\psi, j)$; `zip` runs through the three lists side by side. The `say` line prints two of the densities as formulas (Out [9]): $n_o = a_1^2 + a_2^2 + b_1^2 + b_2^2$ and $s_o = 2a_1b_2 - 2a_2b_1$ for $j = +1$ (sympy writes powers as `**`). For a real-form orbital, $a_1 = a$, $b_2 = b$ and $b_1 = a_2 = 0$, these are $a^2 + b^2$ and $2ab$, as in Section 19.4. The check reproduces T3.orbital_densities.

**In [10], Step 4 of the record: the mean field (Section 19.8).**

```python
potentials = ks["exchange"]["kohnShamPotentials"]
cM = sp.Rational(potentials["Meff_coefficient_of_lambda_S"])  # 15/16
cv = sp.Rational(potentials["vv_coefficient_of_lambda_n"])  # -1/16
m, lam, S, n = sp.symbols("m lambda S n", real=True)


def M_eff(mass, coupling, scalar):
    """The effective mass m + cM lambda S of the record."""
    return mass + cM * coupling * scalar
```

The two coefficients are read from the Kohn-Sham record as texts, `"15/16"` and `"-1/16"`, and `sp.Rational` turns them into exact fractions. $m$, $\lambda$, $S$, $n$ are symbols, and `M_eff` builds $M_{\rm eff} = m + c_M\lambda S$ for any bare mass, coupling and scalar density.

```python
e_int = sp.Rational(15, 32) * lam * S ** 2 - sp.Rational(1, 32) * lam * n ** 2
partner = sp.expand(M_eff(-m, lam, -S) + M_eff(m, lam, S)) == 0
wrong = sp.expand(M_eff(-m, -lam, -S) + M_eff(m, lam, S)) != 0
even = sp.expand(e_int.subs(S, -S) - e_int) == 0
derivatives = (sp.expand(sp.diff(e_int, S) - (M_eff(m, lam, S) - m)) == 0
               and sp.expand(sp.diff(e_int, n) - cv * lam * n) == 0)
```

`e_int` is $e_{\rm int} = \frac{15}{32}\lambda S^2 - \frac{1}{32}\lambda n^2$. `partner` tests $M_{\rm eff}(-m, +\lambda, -S) = -M_{\rm eff}(m, \lambda, S)$; `wrong` tests that $(-m, -\lambda)$ does NOT give it; `even` tests $e_{\rm int}(n, -S) = e_{\rm int}(n, S)$ (`.subs(S, -S)` replaces $S$ by $-S$); `derivatives` tests $\partial e_{\rm int}/\partial S = M_{\rm eff} - m$ and $\partial e_{\rm int}/\partial n = v_v$ (`sp.diff` differentiates).

```python
say(f"cM = {cM}, cv = {cv}; (-m, +lambda) works: {partner}; (-m, -lambda) fails: "
    f"{wrong}; e_int even in S: {even}; derivatives: {derivatives}")
check(partner and wrong and even and derivatives and (cM, cv) == (
    sp.Rational(15, 16), sp.Rational(-1, 16)),
    "M_eff(-m, +lambda, -S) = -M_eff(m, lambda, S); (-m, -lambda) fails",
    record="Revision/pairing/kohn_sham/reports/python-t3.json, check "
           "T3.mean_field_map")
```

Out [10] prints the two coefficients and four `True`; the check also requires the coefficients to be exactly $15/16$ and $-1/16$, and reproduces T3.mean_field_map.

**In [11], the mean-field map as a picture (Figure 19b.3).**

```python
S_values = np.linspace(-1.0, 1.0, 201)
lam_demo, m_demo, cM_value = 0.8, 1.0, float(cM)
need = -(m_demo + cM_value * lam_demo * S_values)  # -M_eff(m, lambda, S)
give_partner = -m_demo + cM_value * lam_demo * (-S_values)  # (-m, +lambda) at -S
give_wrong = -m_demo + cM_value * (-lam_demo) * (-S_values)  # (-m, -lambda) at -S
```

`np.linspace(-1.0, 1.0, 201)` is an array of 201 equally spaced values of $S$ from $-1$ to $1$. The coupling $0.8$ is deliberately large so that the slopes are visible. The three arrays are, for every $S$, the mass the image needs, $-M_{\rm eff}(m, \lambda, S)$, the mass the partner $(-m, +\lambda)$ gives to the image density $-S$, and the mass $(-m, -\lambda)$ would give (numpy computes each formula for all 201 values at once).

```python
fig, ax = plt.subplots()
ax.plot(S_values, need, color="#2a78d6", lw=3.0,
        label="needed: $-M_{eff}(m, \\lambda, S)$")
ax.plot(S_values, give_partner, color="#eb6834", lw=1.6, ls="--",
        label="partner $(-m, +\\lambda)$ at $-S$")
ax.plot(S_values, give_wrong, color="#eda100", lw=1.6, ls=":",
        label="$(-m, -\\lambda)$ at $-S$")
ax.set_xlabel("scalar density $S$ (units of $|m|^7$)")
ax.set_ylabel("effective mass (units of $|m|$)")
ax.legend(fontsize=8, loc="upper right")
```

`plot` draws a curve through the points; `lw` is the line width, `ls` the line style (two hyphens in quotes mean dashed, a colon `":"` dotted), and `label` the text for the **legend** (the box that names the curves), which `legend` draws in the upper right corner. The axis labels name the quantities and units.

```python
save_figure(fig, "mean_field_map",
            "Step 4 of the proof of T3: the effective mass that the image state "
            "needs, $-M_{eff}(m, \\lambda, S)$ (blue), against the scalar density "
            "$S$, with $m = 1$ and an exaggerated coupling $\\lambda = 0.8$ "
            "(units of $|m|$ and $|m|^7$). The partner universe with the bare mass "
            "$-m$ and the same coupling $+\\lambda$ gives exactly this mass to the "
            "image density $-S$ (orange dashed, on top of the blue line); the "
            "universe with $(-m, -\\lambda)$ gives a line with the opposite slope "
            "(yellow dotted), which agrees only at $S = 0$.")
check(float(np.max(np.abs(need - give_partner))) < 1e-15
      and float(np.max(np.abs(need - give_wrong))) > 1.0,
      "the drawn lines: the partner gives the needed mass, (-m, -lambda) does not")
```

`save_figure` saves Figure 19b.3; the check confirms what the picture shows. What the student should see: a thick blue line falling from $-0.25$ at $S = -1$ to $-1.75$ at $S = 1$ (slope $-\frac{15}{16}\cdot0.8 = -0.75$), the orange dashed line exactly on top of it, and the yellow dotted line rising with the opposite slope, crossing the blue one only at $S = 0$, where both are $-m = -1$. (The caption's "Step 4" is the numbering of the record's proof list, where the mean field belongs to the third item; in this chapter it is part of Step 3.)

**In [12], the characteristic functions at zero momentum (Section 19.12).**

```python
Mp, L = sp.symbols("M L", positive=True)
yy = sp.Symbol("yy", real=True)
p = sp.sqrt(Mp ** 2 - eps ** 2)


def propagator(j, mass):
    """exp(N yy) for k = 0, v = 0: cosh(p yy) 1 + sinh(p yy)/p N."""
    N0 = mass * s3 + sp.I * j * eps * s1
    return sp.cosh(p * yy) * one + sp.sinh(p * yy) / p * N0
```

$M$ and $L$ are positive symbols, `yy` the position, and $p = \sqrt{M^2 - \varepsilon^2}$. `propagator` is the matrix $e^{Ny} = \cosh(py)\mathbf 1 + \frac{\sinh(py)}{p}N$ of Section 19.12 with $N = M\sigma_3 + ij\varepsilon\sigma_1$, for any type and mass.

```python
e2 = sp.Matrix([0, 1])  # the vector (0, 1)
at_tip = {yy: -L}
D = {}  # characteristic functions, for j = +1
D["A even"] = (propagator(1, Mp) * e1)[1].subs(at_tip)  # chi2(-L)
D["A odd"] = (propagator(1, Mp) * e2)[1].subs(at_tip)
D["B even"] = (propagator(-1, -Mp) * e1)[0].subs(at_tip)  # chi1(-L)
D["B odd"] = (propagator(-1, -Mp) * e2)[0].subs(at_tip)
D["C even"] = (propagator(1, -Mp) * e1)[1].subs(at_tip)  # chi2(-L)
D["C odd"] = (propagator(1, -Mp) * e2)[1].subs(at_tip)
for name in D:
    say(f"D({name}) = {sp.simplify(D[name])}")
```

The six entries of the table of Section 19.12, with $j = +1$: the propagator applied to the start at the brane, $(1, 0)$ for even or $(0, 1)$ for odd, evaluated at the tip ($y = -L$, the substitution `at_tip`), and the component that the tip condition must make zero: the second (index 1) for $\theta = 0$, the first (index 0) for $\theta = \pi$. A has $(M, +1, \theta = 0)$, B $(-M, -1, \theta = \pi)$, C $(-M, +1, \theta = 0)$. The loop prints them (Out [12]); sympy writes `I` for $i$, `sqrt` for the square root and `epsilon` for $\varepsilon$. Compare with the table of Section 19.12: D(A even) $= -i\varepsilon\sinh(pL)/p$, D(A odd) $= D$(B even) $= \cosh(pL) + M\sinh(pL)/p$, D(B odd) $= +i\varepsilon\sinh(pL)/p$, D(C even) $=$ D(A even), D(C odd) $= \cosh(pL) - M\sinh(pL)/p$.

```python
pairs_equal = (sp.simplify(D["A even"] + D["B odd"]) == 0
               and sp.simplify(D["A odd"] - D["B even"]) == 0)
control_differs = (sp.simplify(D["C even"] - D["A even"]) == 0
                   and sp.simplify(D["C odd"] - D["A odd"]) != 0)
check(pairs_equal and control_differs,
      "k = 0: A and B have equal characteristic functions; C differs (odd sector)",
      record="Revision/pairing/kohn_sham/reports/python-t3.json, check "
             "T3.exact_k0_spectra")
```

`pairs_equal` tests A even $= -$B odd and A odd $=$ B even, identically in $\varepsilon$, $M$, $L$; `control_differs` tests C even $=$ A even and C odd $\ne$ A odd. The check reproduces T3.exact_k0_spectra.

**In [13], the zeros of the characteristic functions.**

```python
M_BARE, L_TIP = 1.0, 3.0  # the mass |m| and the tip distance L of the record


def C_and_Sigma(e):
    """cosh(pL) and sinh(pL)/p for the level(s) e, real for every real e."""
    pc = np.sqrt(M_BARE ** 2 - np.asarray(e, dtype=float) ** 2 + 0j)  # complex p
    small = np.abs(pc) < 1e-12  # p = 0: sinh(pL)/p -> L
    safe = np.where(small, 1.0, pc)
    sigma = np.where(small, L_TIP, np.sinh(safe * L_TIP) / safe)
    return np.cosh(pc * L_TIP).real, sigma.real
```

From here on the numbers $M = 1$, $L = 3$ of the record are used. `C_and_Sigma` computes the two building blocks $\cosh(pL)$ and $\Sigma = \sinh(pL)/p$ for one level or an array of levels. Adding `0j` makes the number under the square root complex, so that for $\varepsilon^2 > M^2$ numpy returns $p = ir$ instead of an error; as Section 19.12 showed, $\cosh(irL) = \cos(rL)$ and $\sinh(irL)/(ir) = \sin(rL)/r$ are real, so `.real` keeps everything. At $p = 0$ the quotient $\sinh(pL)/p$ has the limit $L$; `np.where(small, a, b)` takes `a` where `small` is true and `b` elsewhere, and `safe` avoids a division by zero.

```python
def f_A_even(e):
    return np.asarray(e) * C_and_Sigma(e)[1]


def f_A_odd(e):
    c, sig = C_and_Sigma(e)
    return c + M_BARE * sig


def f_C_odd(e):
    c, sig = C_and_Sigma(e)
    return c - M_BARE * sig
```

The three different characteristic functions, without the constant factor $-ij$ of the even one: $\varepsilon\Sigma$, $\cosh(pL) + M\Sigma$ and $\cosh(pL) - M\Sigma$.

```python
def zeros(f, top=4.0, points=40001):
    """All sign changes of f on (0, top], each refined by 80 bisection steps."""
    grid = np.linspace(1e-9, top, points)
    values = f(grid)
    found = []
    for i in np.nonzero(np.sign(values[:-1]) * np.sign(values[1:]) < 0)[0]:
        low, high = grid[i], grid[i + 1]
        for _ in range(80):
            middle = 0.5 * (low + high)
            if np.sign(f(middle)) == np.sign(f(low)):
                low = middle
            else:
                high = middle
        found.append(0.5 * (low + high))
    return found
```

`zeros` finds every zero of a function between $10^{-9}$ and `top`. It evaluates the function on 40001 grid points; `values[:-1]` are all values but the last and `values[1:]` all but the first, so their signs multiplied are negative exactly where the sign changes between two neighbouring points, and `np.nonzero(...)[0]` lists those positions. Each sign change is refined by **bisection**: halve the interval, keep the half whose ends still have opposite signs, 80 times (the interval then is $2^{-80}$ times its first length, far below the rounding of the computer). The middle of the last interval is the zero.

```python
levels = {"A even": [0.0] + zeros(f_A_even), "A odd": zeros(f_A_odd),
          "C odd": zeros(f_C_odd)}
for name, values in levels.items():
    say(f"{name}: " + ", ".join(f"{v:.10f}" for v in values))
```

The levels of the three sectors; the zero mode $\varepsilon = 0$ of the even sector is put in front by hand (the grid starts just above 0). `", ".join(...)` writes the numbers separated by commas, each with ten digits. Out [13] shows the three ladders of the table in Section 19.12.

```python
SPECTRUM = "Revision/kohn_sham/results/spectrum/free-k0-analytic.csv"
with repository_file(SPECTRUM).open(encoding="utf-8", newline="") as handle:
    rows = [r for r in csv.DictReader(handle)
            if float(r["m"]) == 1.0 and float(r["L"]) == 3.0]
recorded = {parity: sorted(float(r["eps_analytic"]) for r in rows
                           if r["parity"] == parity
                           and 0.0 <= float(r["eps_analytic"]) < 4.0)
            for parity in ("even", "odd")}
```

The record's table of the analytic free levels is read with `csv.DictReader`, which gives each row as a dictionary from the column names to the texts (`with ... as handle:` opens the file and closes it again at the end of the block). Only the rows with $m = 1$ and $L = 3$ are kept. `recorded` holds, for each parity, the sorted recorded levels between 0 and 4.

```python
worst = max(max(abs(x - y) for x, y in zip(levels["A even"], recorded["even"])),
            max(abs(x - y) for x, y in zip(levels["A odd"], recorded["odd"])))
report("largest difference of the levels of A from the record", f"{worst:.1e}")
check(len(levels["A even"]) == len(recorded["even"])
      and len(levels["A odd"]) == len(recorded["odd"]) and worst < 1e-12,
      "the k = 0 levels of A are the analytic levels of the record",
      record=f"{SPECTRUM}, rows m = 1, L = 3")
```

`worst` is the largest difference between our levels of A and the recorded ones: $8.9\times10^{-16}$ (Out [13]). The check also requires the same number of levels.

**In [14], the control's level in the gap (Figure 19b.4).**

```python
eps_b = levels["C odd"][0]  # the first zero: inside the gap?
q_b = math.sqrt(M_BARE ** 2 - eps_b ** 2)
two_forms = (abs(math.tanh(q_b * L_TIP) - q_b / M_BARE) < 1e-12
             and abs(M_BARE / math.cosh(q_b * L_TIP) - eps_b) < 1e-12)
report("sub-gap level of the control eps_b", f"{eps_b:.12f}", "|m|")
above = levels["C odd"][1:]  # the control's odd levels above the gap
distinct = min(abs(x - y) for x in above for y in levels["A odd"]) > 1e-3
check(0.0 < eps_b < M_BARE and two_forms and distinct,
      "only the control has a level in the gap, eps_b = M/cosh(qL), tanh(qL) = q/M")
```

`eps_b` is the lowest odd level of the control and `q_b` $= \sqrt{M^2 - \varepsilon_b^2}$. `two_forms` tests the two statements of Section 19.12: $\tanh(qL) = q/M$ and $\varepsilon_b = M/\cosh(qL)$. `above` holds the other odd levels of C, and `distinct` tests that none of them is within $10^{-3}$ of an odd level of A. The check requires $0 < \varepsilon_b < M$ (inside the gap) as well. Out [14] prints $\varepsilon_b = 0.100851121375$.

```python
grid = np.linspace(0.0, 4.0, 2001)
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
left.plot(grid, f_A_even(grid), color="#2a78d6", lw=2.0,
          label="$\\varepsilon\\,\\sinh(pL)/p$ (even A = odd B = even C)")
left.plot(levels["A even"], np.zeros(len(levels["A even"])), "o", color="#2a78d6")
right.plot(grid, f_A_odd(grid), color="#2a78d6", lw=2.0,
           label="A odd $= $ B even: $\\cosh(pL) + M\\sinh(pL)/p$")
right.plot(grid, f_C_odd(grid), color="#1baf7a", lw=1.6, ls=":",
           label="C odd: $\\cosh(pL) - M\\sinh(pL)/p$")
right.plot(levels["A odd"], np.zeros(len(levels["A odd"])), "o", color="#2a78d6")
right.plot(levels["C odd"], np.zeros(len(levels["C odd"])), "^", color="#1baf7a")
```

The left picture draws the even function on 2001 points from 0 to 4 and marks its zeros, the levels, with dots on the axis (`"o"`; `np.zeros(n)` gives the height 0 for every dot). The right picture draws the odd functions of A and of the control C and marks their zeros with dots and triangles (`"^"`).

```python
for ax in (left, right):
    ax.axhline(0.0, color="0.3", lw=0.8)
    ax.axvline(M_BARE, color="0.5", lw=0.8, ls="--")  # the edge of the mass gap
    ax.set_xlabel("level $\\varepsilon$ (units of $|m|$)")
    ax.set_ylim(-4.0, 6.0)
    ax.legend(fontsize=7, loc="upper right")
left.set_ylabel("characteristic function")
fig.tight_layout()
save_figure(fig, "characteristic_functions",
            "The characteristic functions of the zero-momentum spectra for "
            "$M = 1$, $L = 3$ (horizontal axis: the level $\\varepsilon$ in units "
            "of $|m|$; the dashed vertical line is the edge $\\varepsilon = M$ of "
            "the mass gap). Left: the function of the even sector of A, which is "
            "also that of the odd sector of the partner B and of the even sector of "
            "the control C; its zeros (dots) are $0$ and $\\sqrt{M^2 + "
            "(n\\pi/L)^2}$. Right: the odd sector of A (equal to the even sector of "
            "B) and the odd sector of the control C. Only C has a zero inside the "
            "gap, the level $\\varepsilon_b = 0.1009$, and its other zeros differ "
            "from those of A.")
```

In both pictures a horizontal line marks zero and a dashed vertical line the edge of the mass gap $\varepsilon = M$; the vertical range is cut to $-4$ to $6$ because the functions grow like $\cosh$ inside the gap. `save_figure` saves Figure 19b.4. What the student should see: on the left a curve that is positive inside the gap (its only zero there is the zero mode at $\varepsilon = 0$) and oscillates like $\varepsilon\sin(rL)/r$ outside, crossing zero at $1.448$, $2.321$, $3.297$; on the right the blue curve of A, which starts at $\cosh(3) + \sinh(3) = e^3$ (above the drawn range), stays above zero in the whole gap and crosses zero only above it, and the aqua dotted curve of the control, which starts at $\cosh(3) - \sinh(3) = e^{-3} = 0.05$, falls through zero at $\varepsilon_b = 0.1009$ inside the gap, and crosses zero above the gap at other places than the blue curve.

**In [15], shooting: the functions `brane_value` and `find_levels`.**

```python
H, STEPS = 1.0, 3000  # the constant H and the number of RK4 steps


def brane_value(e, kk, mass, j, tip, odd):
    """Shoot from the tip y = -L to the brane y = 0 at the slice a4,0 = 0.  All
    arguments are numpy arrays of equal shape (one entry per problem); returns
    a(0) where odd is 1 and b(0) where odd is 0."""
    a = np.where(tip == 0.0, 1.0, 0.0)  # theta = 0: (a, b) = (1, 0) at the tip
    b = 1.0 - a  # theta = pi: (a, b) = (0, 1)
    step = L_TIP / STEPS
```

**Shooting** finds levels without a formula: start at the tip with the values that the tip condition allows, integrate the real form of Section 19.3 to the brane, and ask whether the brane condition holds. `brane_value` does this for many problems at once: every argument is a numpy array, and each array position is one problem (its level `e`, momentum `kk`, mass, type `j`, tip angle and parity). At the tip, $\theta = 0$ demands $b(-L) = 0$, so the start is $(a, b) = (1, 0)$; $\theta = \pi$ demands $a(-L) = 0$, so the start is $(0, 1)$ (the overall size does not matter, the equations are linear). The step length is $L/3000 = 0.001$.

```python
    def slope(yv, a, b):
        w = math.exp(-H * yv) * kk  # kappa(y) k
        return mass * a - (w + j * e) * b, (j * e - w) * a - mass * b
```

`slope` is the right side of the real form at the point `yv`, with $v = 0$ and the momentum weight $\kappa k = e^{-Hy}k$ at the slice $a_{4,0} = 0$: it returns $da/dy = Ma - (\kappa k + j\varepsilon)b$ and $db/dy = (j\varepsilon - \kappa k)a - Mb$.

```python
    for i in range(STEPS):
        yv = -L_TIP + i * step
        ka1, kb1 = slope(yv, a, b)
        ka2, kb2 = slope(yv + step / 2, a + step / 2 * ka1, b + step / 2 * kb1)
        ka3, kb3 = slope(yv + step / 2, a + step / 2 * ka2, b + step / 2 * kb2)
        ka4, kb4 = slope(yv + step, a + step * ka3, b + step * kb3)
        a = a + step / 6 * (ka1 + 2 * ka2 + 2 * ka3 + ka4)
        b = b + step / 6 * (kb1 + 2 * kb2 + 2 * kb3 + kb4)
    return np.where(odd == 1.0, a, b)
```

The loop makes 3000 steps of the classical **Runge-Kutta method** of fourth order (RK4, Chapter 2): from the slope at the start of a step, two slopes at its middle and one at its end, the step adds the weighted mean $\frac16(k_1 + 2k_2 + 2k_3 + k_4)$ times the step length. At the brane the function returns the component that must vanish there: $a(0)$ for the odd parity, $b(0)$ for the even parity. A level is a value of $\varepsilon$ at which this **brane value** is zero.

```python
def find_levels(problems, top, points=2001, rounds=16, first_only=False):
    """problems: rows (k, mass, j, tip, odd).  Returns (row index, level) for every
    sign change of brane_value on (0, top] (only the lowest one per row when
    first_only is True)."""
    P = np.array(problems, dtype=float)
    grid = np.linspace(1e-9, top, points)
    columns = [np.repeat(P[:, c:c + 1], points, axis=1) for c in range(5)]
    values = brane_value(np.tile(grid, (len(P), 1)), *columns)
```

`find_levels` takes a list of problems, each a row $(k, M, j, \theta, \text{odd})$, and a top energy. `P` is the table of the problems, one row each. The scan grid has `points` energies between $10^{-9}$ and `top`. To shoot all problems at all grid energies in one call, two tables of the same shape are made: `np.tile(grid, (len(P), 1))` repeats the grid once per problem (one row per problem), and `np.repeat(P[:, c:c + 1], points, axis=1)` repeats column `c` of the problem table along each row; `*columns` passes the five tables as the five last arguments. `values` holds the brane value of every problem at every grid energy.

```python
    rows, cols = np.nonzero(np.sign(values[:, :-1]) * np.sign(values[:, 1:]) < 0)
    if first_only:  # keep the first sign change of every row
        keep = np.concatenate(([True], rows[1:] != rows[:-1]))
        rows, cols = rows[keep], cols[keep]
    lo, hi = grid[cols], grid[cols + 1]  # brackets with a sign change
    f_lo, f_hi = values[rows, cols], values[rows, cols + 1]
    data = [P[rows, c] for c in range(5)]  # the problem of every root
```

The sign changes between neighbouring grid energies are found as in In [13], now in every row at once: `rows` and `cols` list the problem and the grid position of each sign change, in order. With `first_only`, only the first sign change of each problem is kept (an entry is kept when its row differs from the row of the entry before it). Each sign change gives a **bracket** `lo`, `hi` with the brane values `f_lo`, `f_hi` of opposite signs, and `data` lists the problem data of each bracket.

```python
    kept = np.zeros(len(rows))  # which end was kept last: +1 high, -1 low
    new = lo
    for _ in range(rounds):
        new = (lo * f_hi - hi * f_lo) / (f_hi - f_lo)  # zero of the straight line
        f_new = brane_value(new, *data)
        move_low = np.sign(f_new) == np.sign(f_lo)  # the zero lies above new
        f_hi = np.where(move_low & (kept == 1), f_hi / 2, f_hi)  # Illinois rule
        f_lo = np.where(~move_low & (kept == -1), f_lo / 2, f_lo)
        lo, f_lo = np.where(move_low, new, lo), np.where(move_low, f_new, f_lo)
        hi, f_hi = np.where(move_low, hi, new), np.where(move_low, f_hi, f_new)
        kept = np.where(move_low, 1, -1)
    return rows, new
```

All brackets are refined together, 16 rounds, by the **Illinois method**. In each round the new point is the zero of the straight line through $(\text{lo}, f_{\rm lo})$ and $(\text{hi}, f_{\rm hi})$: $\text{new} = (\text{lo}\,f_{\rm hi} - \text{hi}\,f_{\rm lo})/(f_{\rm hi} - f_{\rm lo})$. Its brane value decides which end moves: if it has the sign of the low end, the zero lies above `new` and the low end moves there (`move_low`), otherwise the high end moves. A plain straight-line rule can keep one end fixed for many rounds and converge slowly; the Illinois rule halves the stored value at an end that is kept twice in a row (the high end when the low end moved again, `& (kept == 1)`; the low end in the opposite case, `~` meaning "not"), which pulls the next straight line toward that end. `kept` remembers which end was kept. The function returns the problem number and the level of every root.

```python
say("brane_value and find_levels defined")
```

The cell prints one line (Out [15]).

**In [16], the six sectors at k = 0 by shooting.**

```python
SECTORS = {  # name: (mass, j, tip angle, odd)
    "A even": (1.0, 1.0, 0.0, 0.0), "A odd": (1.0, 1.0, 0.0, 1.0),
    "B even": (-1.0, -1.0, math.pi, 0.0), "B odd": (-1.0, -1.0, math.pi, 1.0),
    "C even": (-1.0, 1.0, 0.0, 0.0), "C odd": (-1.0, 1.0, 0.0, 1.0)}
names_k0 = list(SECTORS)
rows, found = find_levels([(0.0, *SECTORS[name]) for name in names_k0], top=4.0)
shot = {name: sorted(found[rows == r]) for r, name in enumerate(names_k0)}
```

`SECTORS` gives the data of the six problems: A has the mass $+1$, type $+1$ and tip angle 0; B the mass $-1$, type $-1$ and tip angle $\pi$; C the mass $-1$, type $+1$ and tip angle 0; each in both parities. `find_levels` shoots all six at $k = 0$ up to $\varepsilon = 4$. `found[rows == r]` picks the levels of the problem `r` (a comparison of an array with a number gives an array of truth values, which selects the matching entries), and `shot` stores them sorted under the sector's name.

```python
zero_mode = {name: float(brane_value(np.zeros(1), np.zeros(1),
                                     *(np.full(1, x) for x in SECTORS[name]))[0])
             for name in ("A even", "B odd", "C even")}
for name in ("A even", "B odd", "C even"):
    shot[name] = [0.0] + shot[name]  # the zero mode at eps = 0
expected = {"A even": levels["A even"], "A odd": levels["A odd"],
            "B even": levels["A odd"], "B odd": levels["A even"],
            "C even": levels["A even"], "C odd": levels["C odd"]}
```

The zero modes sit exactly at $\varepsilon = 0$, where the scan cannot see a sign change. So `zero_mode` evaluates the brane value at $\varepsilon = 0$, $k = 0$ in the three sectors that have one (`np.full(1, x)` is an array of length one holding `x`), and the zero level is added to their lists. `expected` says what each sector must give according to Section 19.12: A its own levels; B even the levels of A odd and B odd those of A even (T3 exchanges the parities); C even those of A even; C odd the control's own levels.

```python
worst_shot = 0.0
for name in names_k0:
    say(f"{name}: " + ", ".join(f"{e:.10f}" for e in shot[name]))
    if len(shot[name]) != len(expected[name]):
        worst_shot = math.inf  # a level is missing or extra
    else:
        worst_shot = max(worst_shot, max(abs(x - y) for x, y in
                                         zip(shot[name], expected[name])))
report("largest difference shooting - formula at k = 0", f"{worst_shot:.1e}")
check(worst_shot < 1e-9 and all(v == 0.0 for v in zero_mode.values()),
      "shooting finds exactly the formula levels of A, B and C at k = 0")
```

The loop prints the six ladders (Out [16]) and keeps the largest difference from the formula levels; a missing or extra level would make it infinite (`math.inf`). The largest difference is $5.9\times10^{-12}$, the error of 3000 Runge-Kutta steps, and the brane values at $\varepsilon = 0$ are exactly 0: at $\varepsilon = 0$, $k = 0$ the starting value has no component that could grow into the forbidden one (for example, for A even $b$ stays exactly 0 along the whole integration).

**In [17], the ladders (Figure 19b.5).**

```python
COLOUR = {"A": "#2a78d6", "B": "#eb6834", "C": "#1baf7a"}
fig, ax = plt.subplots(figsize=(7.0, 5.0))
for x, kind in enumerate("ABC"):
    for parity, style in (("even", "-"), ("odd", "--")):
        for e in shot[f"{kind} {parity}"]:
            for sign in ((1,) if e == 0.0 else (1, -1)):
                ax.plot([x - 0.3, x + 0.3], [sign * e, sign * e],
                        color=COLOUR[kind], ls=style, lw=2.0)
ax.axhspan(-M_BARE, M_BARE, color="0.9", zorder=0)  # the mass gap
```

`COLOUR` gives each universe its colour: blue A, orange B, aqua C. For each universe (at the horizontal positions 0, 1, 2) and each parity (solid lines for even, dashed for odd) every level is drawn as a short horizontal line, and, except the zero mode, also its negative: at $k = 0$ the levels come in pairs $\pm\varepsilon$ (the characteristic functions are even or odd in $\varepsilon$). `axhspan` shades the mass gap $-1 < \varepsilon < 1$ in light grey behind everything (`zorder=0`).

```python
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["A: $+m$, $\\theta = 0$", "B: $-m$, $\\theta = \\pi$",
                    "C: $-m$, $\\theta = 0$ (control)"])
ax.set_xlim(-0.6, 2.6)
ax.set_ylabel("level $\\varepsilon$ at $k = 0$ (units of $|m|$)")
ax.grid(axis="x", visible=False)
save_figure(fig, "k0_ladders",
            "The levels at zero momentum of the universes A (mass $+m$, tip angle "
            "0), B (mass $-m$, tip angle $\\pi$, the T3 partner) and C (mass $-m$, "
            "tip angle 0, the control), for $m = 1$, $L = 3$, no interaction, found "
            "by shooting (vertical axis: the level in units of $|m|$; solid lines "
            "even parity, dashed lines odd parity; grey band: the mass gap "
            "$|\\varepsilon| < m$). A and B have the same ladder with the parities "
            "exchanged; the control has different odd levels and the pair "
            "$\\pm\\varepsilon_b$ inside the gap.")
```

The three ladders are labelled under the horizontal axis, the vertical grid lines are switched off, and `save_figure` saves Figure 19b.5. What the student should see: the ladders of A and B at exactly the same heights, but where A has a solid line B has a dashed one and the other way round (the exchanged parities); the zero mode at 0; nothing else inside the grey gap for A and B; the control C with the zero mode, two dashed lines at $\pm0.1009$ inside the gap, and dashed lines above the gap at heights different from those of A.

```python
ladder_A = np.array(sorted(shot["A even"] + shot["A odd"]))
ladder_B = np.array(sorted(shot["B even"] + shot["B odd"]))
check(len(ladder_A) == len(ladder_B)
      and float(np.max(np.abs(ladder_A - ladder_B))) < 1e-12,
      "the shooting ladders of A and B agree level by level")
```

The two complete ladders (both parities, sorted) of A and B are compared level by level; they agree to better than $10^{-12}$ although they were shot with different masses, types, tip conditions and parities.

**In [18], the brane band at small momenta.**

```python
BAND = {"A": (1.0, 1.0, 0.0, 0.0), "B": (-1.0, -1.0, math.pi, 1.0),
        "C": (-1.0, 1.0, 0.0, 0.0)}  # mass, j, tip angle, odd
k_plot = np.linspace(0.0, 0.25, 26)[1:]  # 25 momenta for the figure
problems = [(kk, *BAND[kind]) for kind in "ABC" for kk in k_plot]
rows, found = find_levels(problems, top=2.0, points=401, first_only=True)
band = {kind: found[i * len(k_plot):(i + 1) * len(k_plot)]
        for i, kind in enumerate("ABC")}
```

`BAND` gives the sector of the zero mode of each universe: A type $+1$ even, B type $-1$ odd (its image), C type $+1$ even. `k_plot` are the 25 momenta $0.01, 0.02, \dots, 0.25$ (26 points from 0 to 0.25 without the first). The 75 problems are shot together, and only the lowest positive level of each is kept (`first_only=True`); a scan with 401 points up to $\varepsilon = 2$ suffices. `band` cuts the 75 levels into the three lists of 25, in the order in which the problems were made.

```python
band_gap = float(np.max(np.abs(band["A"] - band["B"])))
report("largest |eps_A - eps_B| on the band", f"{band_gap:.1e}")
check(len(rows) == 3 * len(k_plot) and band_gap < 1e-10
      and float(np.min(np.abs(band["A"] - band["C"]))) > 1e-3,
      "the band of B equals that of A at every momentum; the control differs")
```

The largest difference between the bands of A and B is exactly 0 (Out [18]): with $\sigma_2$ the shooting of B performs, step by step, the same arithmetic as that of A with $a$ and $b$ exchanged. The check also requires a level for every problem and a difference larger than $10^{-3}$ between A and C at every momentum.

**In [19], the slopes at zero momentum.**

```python
small = 1e-4
problems = [(kk, *BAND[kind]) for kind in "ABC" for kk in (small, 2 * small)]
rows, found = find_levels(problems, top=0.01, points=401, first_only=True)
slopes = {kind: (4 * found[2 * i] / small - found[2 * i + 1] / (2 * small)) / 3
          for i, kind in enumerate("ABC")}
```

The band is an odd function of $k$, $\varepsilon(k) = ck + dk^3 + \dots$, so $\varepsilon(k)/k = c + dk^2 + \dots$. At $k$ and $2k$: $\varepsilon(k)/k = c + dk^2$ and $\varepsilon(2k)/(2k) = c + 4dk^2$, so $4\varepsilon(k)/k - \varepsilon(2k)/(2k) = 3c$: the combination divided by 3 removes the $k^2$ term (**Richardson extrapolation**, Chapter 16). The cell shoots the three bands at $k = 10^{-4}$ and $2\times10^{-4}$ (six problems; levels below $0.01$) and forms this combination for each universe.

```python
c_A = (2 * M_BARE / (2 * M_BARE - H) * (1 - math.exp(-(2 * M_BARE - H) * L_TIP))
       / (1 - math.exp(-2 * M_BARE * L_TIP)))
c_C = (2 * M_BARE / (2 * M_BARE + H) * (math.exp((2 * M_BARE + H) * L_TIP) - 1)
       / (math.exp(2 * M_BARE * L_TIP) - 1))
c_record = float(ks["checksNumeric"]["braneBandSlope_M1_H1_L3_a0"])
SLOPES = "Revision/kohn_sham/results/spectrum/brane-band-slope.csv"
with repository_file(SLOPES).open(encoding="utf-8", newline="") as handle:
    c_csv = float(next(csv.DictReader(handle))["c_theory"])  # the row a4,0 = 0
```

`c_A` and `c_C` are the closed forms $c$ and $c_{\rm ctrl}$ of Section 19.12. `c_record` is the slope stored in `ks-theory.json` under checksNumeric, and `c_csv` the theoretical slope of the first row (the slice $a_{4,0} = 0$) of the record's slope table; `next(...)` takes the first row that the reader gives.

```python
say(f"closed forms: c = {c_A:.13f}, c_ctrl = {c_C:.10f}; records: "
    f"{c_record:.13f} and {c_csv:.13f}")
for kind in "ABC":
    say(f"{kind}: shooting slope {slopes[kind]:.10f}")
check(len(rows) == 6 and abs(c_A - c_record) < 1e-13 and abs(c_A - c_csv) < 1e-13
      and abs(slopes["A"] / c_A - 1) < 1e-7 and abs(slopes["B"] / c_A - 1) < 1e-7,
      "the brane-band slope of A and of its partner B is c = 1.9051482536",
      record=f"{KS_THEORY}, checksNumeric braneBandSlope_M1_H1_L3_a0, and {SLOPES}")
check(abs(slopes["C"] / c_C - 1) < 1e-6 and c_C > 7 * c_A,
      "the control's band starts with the much larger slope c_ctrl = 13.42")
```

Out [19] shows $c = 1.9051482536449$ from the closed form and from both records, and $c_{\rm ctrl} = 13.4219751976$; the shooting slopes of A and B are $1.9051482536$ and that of C $13.4219751976$. The first check requires the closed form to equal both records to $10^{-13}$ and the shooting slopes of A and B to agree with it to a relative $10^{-7}$; the second requires the control's slope to agree with its closed form and to be more than seven times larger.

**In [20], the brane band (Figure 19b.6).**

```python
fig, ax = plt.subplots()
ax.plot(k_plot, band["A"], "o-", color=COLOUR["A"], lw=2.2, ms=6,
        label="A: $+m$, $\\theta = 0$")
ax.plot(k_plot, band["B"], "s--", color=COLOUR["B"], lw=1.4, ms=3,
        label="B: $-m$, $\\theta = \\pi$ (T3 partner)")
ax.plot(k_plot, band["C"], "^:", color=COLOUR["C"], lw=1.4, ms=5,
        label="C: $-m$, $\\theta = 0$ (control)")
k_line = np.linspace(0.0, 0.25, 51)
ax.plot(k_line, c_A * k_line, "k--", lw=0.8, label="$c\\,k$, $c = 1.905$")
short = k_line[k_line < 0.11]  # the control's line leaves the picture early
ax.plot(short, c_C * short, "k:", lw=0.8, label="$c_{ctrl}\\,k$, $c_{ctrl} = 13.42$")
ax.set_xlabel("3-space momentum $k$ (units of $|m|$)")
ax.set_ylabel("lowest positive level $\\varepsilon$ (units of $|m|$)")
ax.legend(fontsize=8, loc="lower right")
```

The three bands are drawn with markers joined by lines (`"o-"` circles and a solid line, an `s` followed by two hyphens squares and dashes, `"^:"` triangles and dots; `ms` is the marker size; B's small squares sit inside A's large circles). The straight lines $ck$ and $c_{\rm ctrl}k$ are drawn in black (`k` for black, followed by two hyphens for the dashed line and by a colon, `"k:"`, for the dotted one); the control's line only up to $k = 0.11$, where it reaches about $1.5$ (`k_line[k_line < 0.11]` keeps the momenta below $0.11$).

```python
save_figure(fig, "brane_band",
            "The lowest positive level of the band sector against the 3-space "
            "momentum $k$ (both in units of $|m|$) at the slice $a_{4,0} = 0$, for "
            "$m = 1$, $L = 3$, no interaction, found by shooting: A (blue circles), "
            "its T3 partner B (orange squares, on top of A) and the control C (aqua "
            "triangles). A and B start with the slope $c = 1.905$ of the brane band "
            "(dashed); the control's zero mode lives at the tip, where the redshift "
            "factor $e^{-Hy}$ is largest, so its level rises with the slope "
            "$c_{ctrl} = 13.42$ (dotted) and soon bends below the first level of "
            "the bulk.")
```

`save_figure` saves Figure 19b.6. What the student should see: the blue circles of A, each with the orange square of B inside, rising close to the dashed line $1.905k$ over the whole range; the control's triangles leaving zero along the steep dotted line and then bending over, staying below the first level of the bulk (the levels above the gap), as the caption says.

**In [21], the last check.**

```python
paths = [output_file(f"{FIGURE_FOLDER}/{name}.png") for name in
         ["19b_1_eight_gammas", "19b_2_gamma_block_map", "19b_3_mean_field_map",
          "19b_4_characteristic_functions", "19b_5_k0_ladders", "19b_6_brane_band"]]
check(all(path.is_file() for path in paths),
      "every figure file of this notebook exists")
all_checks_passed()
```

The list holds the paths of the six figure files; the check requires that all exist, and `all_checks_passed` prints the last line, ALL 19 CHECKS PASSED (notebook 19b) (Out [21]).

### 19.17 Watching T3 in the Rust solver: four universes

**What the solver does.** The Revision Rust Kohn-Sham solver (Chapter 15; `Revision/kohn_sham/solver`) solves one instantaneous Kohn-Sham problem at a time with its subcommand `single`: given the bare mass $m$, the coupling $\lambda$, the slice $a_{4,0}$, the particle number $N$, the tip angle $\theta$ and, for a thermal state, the temperature $T$, it finds every level of every sector by shooting with a counting angle, fills the levels, builds the mean field, mixes old and new densities (Anderson mixing) and repeats until the state reproduces itself; its canonical numerics are 900 Runge-Kutta steps, root tolerance $10^{-13}$ and self-consistency tolerance $10^{-11}$ (`Revision/kohn_sham/results/parameters.json`, entry numerics). A `single` run contains no map from one universe to another: each universe is solved on its own. (The solver does contain T3 code elsewhere: its self-test t3_block_map_solver_selftest, in `Revision/kohn_sham/solver/src/runs.rs`, solves two members and compares them; the runs of this chapter do not use it.)

**What the agreement of two universes tests.** The counting angle is the angle $\phi$ of the real form of Section 19.3, $a = r\cos\phi$, $b = r\sin\phi$, so that $\tan\phi = b/a$ (`Revision/kohn_sham/solver/src/shoot.rs`, its header). Write $K = \kappa k$ and $E = \varepsilon - v$. Its equation follows from the real form, line by line:

$$
\frac{d\phi}{dy} = \frac{a\,b' - b\,a'}{a^2 + b^2} = \frac{(jE - K)a^2 - Mab - Mab + (K + jE)b^2}{r^2} = jE - K\cos2\phi - M\sin2\phi .
$$

Rule: the derivative of $\arctan(b/a)$ is $(ab' - ba')/(a^2 + b^2)$; insert $a' = Ma - (K + jE)b$ and $b' = (jE - K)a - Mb$; then $a^2 + b^2 = r^2$, $(a^2 - b^2)/r^2 = \cos^2\phi - \sin^2\phi = \cos2\phi$ and $2ab/r^2 = 2\sin\phi\cos\phi = \sin2\phi$. The map of T3 in the real form, $(a, b, j, M) \to (b, a, -j, -M)$, exchanges $a$ and $b$, so the angle of the image is $\psi = \pi/2 - \phi$. Its derivative is $\psi' = -\phi' = -jE + K\cos2\phi + M\sin2\phi$. The equation of the partner problem, with $-j$ and $-M$, gives for $\psi$, line by line:

$$
(-j)E - K\cos2\psi - (-M)\sin2\psi = -jE - K\cos(\pi - 2\phi) + M\sin(\pi - 2\phi) = -jE + K\cos2\phi + M\sin2\phi .
$$

Rule: $\cos(\pi - x) = -\cos x$ and $\sin(\pi - x) = \sin x$. The two right sides are equal: the angle of B obeys the equation of A with $\phi$ replaced by $\pi/2 - \phi$. The tip condition of the solver starts the angle at $\theta/2$, that is at $0$ for A and at $\pi/2 = \pi/2 - 0$ for B. So every Runge-Kutta step for B is the step for A, mirrored: the solver does the same arithmetic for both, and their agreement to the last digits is guaranteed **by construction**. The record says this explicitly (`Revision/pairing/kohn_sham/t3-completion.json`, entry numerical_demonstration; the README of `Revision/pairing/kohn_sham`): the shooting method is covariant under the map. What the agreement does test is the solver's handling of both members: the transformed boundary conditions, the labels of the levels, the filling convention, the self-consistency loop and the Mermin root. It does not test the discretisation. The test that does not depend on the discretisation is the record's demonstration with the independent reference solver of Chapter 16 (Section 19.10): its frames for the two members are not images of each other, so on one grid their levels differ by up to $2.23\times10^{-4}$, and only after Richardson extrapolation do they agree, to $2.043\times10^{-14}$ (ground) and $3.038\times10^{-14}$ (thermal). The controls, on the other hand, are real tests: nothing in the solver forces C, or D at the same coupling $\lambda$, to agree with A, and they do not (D agrees with A at the opposite coupling $-\lambda$, which is again the covariance of the shooting).

**The four universes.** Notebook 19a solves, always with $|m| = 1$:

| name | bare mass | coupling | tip angle | role |
| --- | --- | --- | --- | --- |
| A | $+1$ | $+\lambda$ | $0$ | the canonical state of the record |
| B | $-1$ | $+\lambda$ | $\pi$ | the T3 partner of A |
| C | $-1$ | $+\lambda$ | $0$ | negative control: the tip is not transformed |
| D | $-1$ | $-\lambda$ | $\pi$ | wrong partner: the coupling is reversed, as in T1 |

By T3, B must agree with A in every level, occupation, energy and energy-momentum profile, with the opposite $S$, $Q$ and $M_{\rm eff}$; C must differ (Section 19.12); and D, which is the T3 partner of the state of A with the coupling $-\lambda$, must agree with A at $-\lambda$, not at $\lambda$.

**What is compared, and the tolerance.** The solver writes for every state a record with the list of levels (each with its momentum shell $n_2$, block type $j$, brane parity, label, level $\varepsilon$, degeneracy $g$ and occupation $f$), the energy $E_{KS}$, the chemical potential or Fermi level, the entropy, the four integrals $2\,\mathrm{Vol}_7\int e^{6Hy}X\,dy$ of $X = \rho, p_3, p_t, p_8$ and of $n$, the measured residuals of the conservation law along $y$, and a table of the profiles $n, S, Q, M_{\rm eff}, v_v, e_{\rm int}, \rho, p_3, p_t, p_8$ at the 151 points $y = -3, -2.98, \dots, 0$. The notebook compares A and B in exactly the way the solver's self-test of the record does: the sorted lists of $(\varepsilon, g, f)$, the energies, the integrals and the scalar densities, with the tolerance $10^{-9}$ that the record fixed before its comparison. It adds the orbital-by-orbital pairing of statement S1 and a point-by-point comparison of every profile column. The differences between A and B that the notebook measures are $6.88\times10^{-14}$ ($N = 8$) and $9.86\times10^{-14}$ ($N = 136$) for the levels at the slice $a_{4,0} = 1$ (Notebook 19a, Out [7]) and, over all the 19 pairs it shares with the record, at most $9.9\times10^{-14}$ for the ground states, $1.0\times10^{-13}$ along the history and $8.1\times10^{-13}$ for the thermal states (Notebook 19a, Out [27]). The largest is the entropy of the thermal state at $T = 0.01$, a number near $42$ that the solver adds up level by level from the occupations. The record's own demonstration finds at most $2.179\times10^{-13}$ (ground states) and $3.877\times10^{-12}$ (thermal states) in its 210 states (`Revision/pairing/kohn_sham/reports/t3-rust-demo.json`, printed again in Out [27]). All of these are rounding errors: a computer carries about sixteen significant digits, and the tiny rounding errors of the many arithmetic steps of the shooting and of the self-consistency loop add up. They lie far below the tolerance $10^{-9}$, and the paragraph "What the agreement of two universes tests" above explains why the agreement stays at the rounding level by construction.

**The margin.** The solver keeps, above the highest occupied level, empty levels up to a **margin**; the record uses $0.25 + 2\sigma$ with $\sigma = 0$, $0.1$ and $0.3$ for $\lambda = 0$, $\pm\lambda_1$, $\pm\lambda_2$, that is the margins $0.25$, $0.45$, $0.85$, for its ground states, and $0.2 + 2\sigma$ for its thermal states, that is $0.4$ for the coupling $\lambda_1$ used here (`Revision/kohn_sham/solver/src/runs.rs`, functions margin_for and the thermal run). The notebook uses the same margins, so that its runs are the record's runs.

**What the runs reproduce.** Every run of A is a state of the committed canonical matrix (`Revision/kohn_sham/results/ground/summary.csv`, `emt-integrals.csv`, the profile files, and `Revision/kohn_sham/results/thermo/thermodynamics.csv` for the thermal states), and the notebook checks that it reproduces the recorded numbers. Its runs of A, B and C for $N = 8$ and $136$ at $\lambda_1$, $a_{4,0} = 1$ repeat the solver's T3 self-test of `Revision/kohn_sham/reports/ks-rust-solver.json` (Section 19.10) number by number. And 19 of its states are states of the record's own demonstration `Revision/pairing/kohn_sham/reports/t3-rust-demo.json` (Section 19.10): there A, B and C equal the plus, image and control members of the table `Revision/pairing/kohn_sham/numerics/results/t3-rust-states.csv`, and D at the coupling $\lambda$ equals its image member at $-\lambda$ (notebook section 17).

### 19.18 Example: the universes of mass $+M$ and $-M$ in the Rust solver (Notebook 19a)

Notebook 19a checks the eight gammas and the block map of $\Gamma$ again, builds the Rust solver with cargo, and runs it 62 times: A, B and C for $N = 8$ and $136$ at the slice $a_{4,0} = 1$ (the self-test of the record); A, B and C without interaction for $N = 8$ (the zero modes and the level in the gap); A, B and C at the five slices of the deflating history for $N = 136$ and $688$; A, B, C and D for five couplings; and A, B and C at three temperatures. Then it compares the 19 states it shares with the record's demonstration of T3. It needs Rust (cargo 1.91.1 or newer), takes about two minutes (33.6 s in the recorded build on the computer that built this book), writes the solver's raw output (about 2 MB) into a folder that git ignores, draws ten figures and ends with the line ALL 37 CHECKS PASSED (notebook 19a).

<!-- NOTEBOOK 19a -->

### 19.21 Line-by-line walk-through of Notebook 19a

The notebook has 28 code cells, In [1] to In [28]; the numbers they print are in Section 19.20 under the labels Out [k].

**In [1], the set-up cell.** Its first 298 lines are the complete run instructions of Section 19.19 as comment lines, followed by a line of dashes. The code after the title THE SET-UP is the set-up code of Notebook 19b, explained line by line in Section 19.16, with three differences: the name is `NOTEBOOK_ID = "19a"`, and, because this notebook runs a Rust program, the imports contain two more lines and the cell defines one more function.

```python
import shutil  # finds the program cargo
import subprocess  # runs cargo and the Rust programs
```

`shutil` can find a program on the computer, here cargo, the build tool of Rust; `subprocess` can run a program and collect what it prints.

```python
def rust_program(manifest, binary):
    """Build the Rust program binary of the crate whose Cargo.toml is manifest (a
    repository path) with "cargo build --release" (about a second when it is up to date;
    minutes the first time) and return the path of the program."""
    if shutil.which("cargo") is None:
        raise FileNotFoundError(
            "cargo was not found: install Rust from https://rustup.rs, open a new "
            "terminal, activate the environment and start JupyterLab again")
    crate = (REPO / manifest).parent  # the folder that holds Cargo.toml
    completed = subprocess.run(
        ["cargo", "build", "--release", "--manifest-path", str(REPO / manifest),
         "--target-dir", str(crate / "target")],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if completed.returncode != 0:  # show the end of cargo's error message
        print(completed.stderr[-3000:])
        raise RuntimeError(f"cargo build failed for {manifest}")
    for file_name in (binary, binary + ".exe"):  # Linux and macOS; Windows
        path = crate / "target" / "release" / file_name
        if path.is_file():
            say(f"Rust program {binary} is built and ready.")
            return path
    raise FileNotFoundError(f"cargo built {manifest} but {binary} is missing")
```

`rust_program` builds a Rust program and returns where it is. `shutil.which("cargo")` looks for cargo; if it is not found (`is None`), the function stops with a message that says how to install Rust. A **crate** is a Rust package; `crate` is the folder that holds its file `Cargo.toml` (`.parent` removes the last part of a path). `subprocess.run([...])` runs cargo with the arguments in the list, exactly as if the release build command for this manifest, with the build folder `target` next to `Cargo.toml`, were typed into a terminal; `capture_output=True` keeps cargo's messages instead of printing them, and `text=True` with `encoding="utf-8"` reads them as text (`errors="replace"` replaces a character that cannot be read instead of stopping). The **return code** of a program is 0 when it succeeded; otherwise the function prints the last 3000 characters of cargo's error messages (`[-3000:]` takes the end of a string) and stops. The `for` loop tries the program's name without and with the ending `.exe` (Linux and macOS have no ending, Windows has `.exe`) and returns the first one that exists, after printing that the program is ready.

**In [2], the eight gammas and Γ.**

```python
import csv  # reads the tables (CSV files) of the record
import math  # pi, exp, tanh and cosh of single numbers
import re  # regular expressions: reads numbers out of the record's text

import numpy as np  # arrays of numbers
```

`csv`, `math` and `numpy` as in Notebook 19b; `re` finds patterns in text (**regular expressions**), used in In [6] to read numbers out of a sentence of the record.

```python
GAMMAS = "Revision/algebra/gammas.json"  # the record of the gamma matrices
ALGEBRA = "Revision/algebra/reports/wolfram-algebra.json"  # its check report
fixture = json.loads(repository_file(GAMMAS).read_text(encoding="utf-8"))
stored_real = all(isinstance(g, list) for g in fixture["gamma"])  # no complex part
gamma = [np.array(g, dtype=float) for g in fixture["gamma"]]  # gamma[0] is x1
eta = np.array(fixture["eta"], dtype=float)  # +1 +1 +1 -1 -1 -1 -1 +1
entries = sorted({float(x) for g in gamma for x in g.flat})  # all values used
say(f"{len(gamma)} matrices of size {gamma[0].shape}; their entries: {entries}")
```

The same reading as In [2] of Notebook 19b, but with the matrices as arrays of decimal numbers (`dtype=float`); whole numbers up to $2^{53}$ are stored exactly in this format, so the products below are still exact. `entries` lists the values that occur; Out [2] prints $-1.0$, $0.0$, $1.0$.

```python
worst = 0.0  # largest violation of the anticommutation rule
for a in range(8):
    for b in range(8):
        anti = gamma[a] @ gamma[b] + gamma[b] @ gamma[a]
        rule = 2.0 * eta[a] * (a == b) * np.eye(16)  # 2 eta^ab times the unit
        worst = max(worst, float(np.max(np.abs(anti - rule))))
Gamma = gamma[7]  # gamma^(x8) first ...
for a in range(7):
    Gamma = Gamma @ gamma[a]  # ... times gamma^(x1), gamma^(x2), ..., gamma^(x7)
diagonal = np.diag([-1.0] * 8 + [1.0] * 8)
anticommutes = all(np.array_equal(Gamma @ g, -(g @ Gamma)) for g in gamma)
```

The anticommutation rule for all 64 pairs and the chirality $\Gamma$ in the author's order, exactly as In [4] and In [5] of Notebook 19b (Section 19.16).

```python
check(stored_real and entries == [-1.0, 0.0, 1.0] and worst == 0.0,
      "the eight gamma matrices are real and obey g^a g^b + g^b g^a = 2 eta^ab",
      record=f"{ALGEBRA}, checks reality and Clifford_relation")
check(np.array_equal(Gamma, diagonal) and anticommutes
      and np.array_equal(Gamma, np.array(fixture["Gamma"], dtype=float)),
      "Gamma = g^(x8) g^(x1) ... g^(x7) = diag(-1 (8 times), +1 (8 times))",
      record=f"{ALGEBRA}, check Gamma_diag")
```

Two checks (Out [2]), reproducing the checks reality, Clifford_relation and Gamma_diag of `wolfram-algebra.json`.

**In [3], Γ is the block map of T3.**

```python
KS_THEORY = "Revision/kohn_sham/ks-theory.json"
ks = json.loads(repository_file(KS_THEORY).read_text(encoding="utf-8"))
ENTRY = {"0": 0.0, "1": 1.0, "-1": -1.0, "I": 1j, "-I": -1j}  # the record's text
V = np.array([[ENTRY[x] for x in row]
              for row in ks["blockBasis"]["unnormalisedColumns2Sqrt2V"]])
V = V / (2.0 * math.sqrt(2.0))  # the record stores 2 sqrt(2) V
labels = [tuple(int(x) for x in label) for label in ks["blockBasis"]["labels"]]
sig1 = np.array([[0, 1], [1, 0]], dtype=complex)  # Pauli matrix sigma1
sig2 = np.array([[0, -1j], [1j, 0]])  # Pauli matrix sigma2
sig3 = np.array([[1, 0], [0, -1]], dtype=complex)  # Pauli matrix sigma3
unitary = float(np.max(np.abs(V.conj().T @ V - np.eye(16))))
worst_map, worst_form = 0.0, 0.0
for b, (j, s2, s3) in enumerate(labels):
    p = labels.index((-j, s2, s3))  # the partner block
    Vb, Vp = V[:, 2 * b:2 * b + 2], V[:, 2 * p:2 * p + 2]  # their two columns
    worst_map = max(worst_map, float(np.max(np.abs(Gamma @ Vb - Vp @ (s2 * sig2)))))
    g8 = Vb.conj().T @ gamma[7] @ Vb  # gamma^(x8) inside block b
    g84 = Vb.conj().T @ gamma[7] @ gamma[3] @ Vb  # gamma^(x8) gamma^(x4) there
    worst_form = max(worst_form, float(np.max(np.abs(g8 - sig3))),
                     float(np.max(np.abs(g84 - j * sig1))))
```

These lines are In [5] of Notebook 19b (the second half), with the Pauli matrices called `sig1`, `sig2`, `sig3`: the block basis $V$ read from the record, its unitarity, and for every block the deviation of $\Gamma V_b$ from $V_p\,s_2\sigma_2$ and of the block forms of $\gamma^{(x_8)}$ and $\gamma^{(x_8)}\gamma^{(x_4)}$ from $\sigma_3$ and $j\sigma_1$.

```python
    if b < 4:
        say(f"block {b} {labels[b]} <-> block {p} {labels[p]}: matrix "
            f"{s2:+d} sigma2")
say(f"largest deviations: unitarity {unitary:.1e}, block map {worst_map:.1e}, "
    f"block forms {worst_form:.1e}")
check(unitary < 1e-12 and worst_map < 1e-12 and worst_form < 1e-12,
      "Gamma maps block (j, s2, s3) onto block (-j, s2, s3) as s2 sigma2",
      record="Revision/pairing/kohn_sham/reports/python-t3.json, check "
             "T3.Gamma_is_the_block_map")
```

For the four blocks of type $j = +1$ (`b < 4`) the loop also prints which block is the partner and the matrix $s_2\sigma_2$ between them. Out [3] shows block 0 $(1, 1, 1)$ with block 4 $(-1, 1, 1)$ and block 1 $(1, 1, -1)$ with block 5, both with $+\sigma_2$; block 2 $(1, -1, 1)$ with block 6 and block 3 $(1, -1, -1)$ with block 7, both with $-\sigma_2$; then the deviations ($1.1\times10^{-16}$, exactly 0, $1.1\times10^{-16}$) and the PASS line.

**In [4], the solver is built.**

```python
SOLVER_MANIFEST = "Revision/kohn_sham/solver/Cargo.toml"  # the crate of the solver
program = rust_program(SOLVER_MANIFEST, "revision_ks_solver")  # build it, get path
RUN_FOLDER = REPO / "Revision/kohn_sham/solver/target/textbook_19a"  # git ignores it
RUN_FOLDER.mkdir(parents=True, exist_ok=True)
```

`rust_program` (In [1]) builds the solver, which takes a second when it is up to date, and returns the path of the program, `program`. `RUN_FOLDER` is a folder inside the solver's build folder `target`, which git ignores, so the raw outputs of the 62 runs never enter the record; `mkdir` creates it.

```python
COLOUR = {"A": "#2a78d6", "B": "#eb6834", "C": "#1baf7a", "D": "#eda100"}
NAME = {"A": "A: $+m$, $+\\lambda$, $\\theta = 0$",
        "B": "B: $-m$, $+\\lambda$, $\\theta = \\pi$ (T3 partner)",
        "C": "C: $-m$, $+\\lambda$, $\\theta = 0$ (control)",
        "D": "D: $-m$, $-\\lambda$, $\\theta = \\pi$ (wrong partner)"}
say("Solver ready, colours defined.")
```

Every universe keeps one colour in all ten figures, blue A, orange B, aqua C, yellow D, and one legend text, `NAME`. Out [4] shows the two printed lines.

**In [5], the helpers `solve` and `universe`.**

```python
TIP = {"A": 0.0, "B": math.pi, "C": 0.0, "D": math.pi}  # tip angle of each kind
MASS = {"A": 1.0, "B": -1.0, "C": -1.0, "D": -1.0}  # bare mass of each kind
SIGN = {"A": 1.0, "B": 1.0, "C": 1.0, "D": -1.0}  # D reverses the coupling


def read_profile(path):
    """A profile table as a dictionary: column name -> numpy array (151 values)."""
    data = np.genfromtxt(path, delimiter=",", names=True)
    return {name: data[name] for name in data.dtype.names}
```

The three dictionaries are the table of Section 19.17: the tip angle, the bare mass and the sign of the coupling of each universe. `read_profile` reads a profile table: `np.genfromtxt` reads a CSV file of numbers whose first line holds the column names (`names=True`), and the dictionary comprehension makes one numpy array of 151 values per column (`data.dtype.names` is the list of the column names).

```python
def solve(label, m, lam, a4, N, theta, margin, T=None):
    """Run "revision_ks_solver single" for one state and return its results."""
    out = RUN_FOLDER / f"{label}.json"  # the solver's record of this state
    table = RUN_FOLDER / f"{label}.csv"  # its profiles
    command = [str(program), "single", "--root", str(REPO), "--m", repr(m),
               "--lambda", repr(lam), "--a4", repr(a4), "--N", repr(float(N)),
               "--tip-theta", repr(theta), "--margin", repr(margin),
               "--out", str(out), "--profiles", str(table)]
    if T is not None:
        command += ["--T", repr(T)]  # a thermal (Mermin) state
```

`solve` runs the solver once. The two output files are named after the `label`. `command` is the command line as a list: the program, its subcommand `single` (solve one state), and pairs of an option and its value: the options named root (where the repository is: the solver reads `ks-theory.json` and the gammas from there), m, lambda, a4 (the slice), N, tip-theta, margin, out (the JSON record of the state) and profiles (the CSV table), each written with two hyphens in front, as the code shows. `repr(x)` writes a number with all its digits, so the solver receives exactly the value of the notebook. For a thermal state the option T with the temperature is appended (`+=` appends a list).

```python
    done = subprocess.run(command, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    last = (done.stdout.strip().split("\n") or [""])[-1]  # SUCCESS or FAILURE
    if done.returncode != 0 or last != "SUCCESS":
        raise RuntimeError(f"the solver failed for {label}: {done.stderr[-400:]}")
    state = json.loads(out.read_text(encoding="utf-8"))
    state["levels"] = [tuple(level) for level in
                       state["levels_n2_j_parity_label_eps_deg_f"]]
    state["profile"] = read_profile(table)
    return state
```

`subprocess.run` runs the solver and keeps its printed text. The solver's last printed line is SUCCESS or FAILURE; `last` takes it (`.strip()` removes blank space at the ends, `.split("\n")` cuts the text into lines, `[-1]` takes the last one). If the return code is not 0 or the last line is not SUCCESS, the notebook stops with the end of the solver's error text. Otherwise the solver's JSON record is read into the dictionary `state`; its list of levels, each a list $(n_2, j, \text{parity}, \text{label}, \varepsilon, g, f)$, is stored again as tuples under the shorter key `levels`, and the profile table under `profile`.

```python
def universe(kind, lam, a4, N, margin, T=None):
    """Solve universe A, B, C or D with the coupling lam (D uses -lam)."""
    label = f"{kind}_N{N}_lam{lam:+.4g}_a{a4:g}" + ("" if T is None else f"_T{T:g}")
    return solve(label, MASS[kind], SIGN[kind] * lam, a4, N, TIP[kind], margin, T)


say("solve and universe defined; outputs go to the folder "
    "Revision/kohn_sham/solver/target/textbook_19a")
```

`universe` solves one of the four universes: it makes a label such as `A_N136_lam+0.0009298_a1` (`:+.4g` writes the coupling with its sign and four significant digits, `:g` a short number) and calls `solve` with the bare mass, the signed coupling and the tip angle of that kind. Out [5] prints the line about the output folder.

**In [6], what the record says.**

```python
T3_WOLFRAM = "Revision/pairing/kohn_sham/reports/wolfram-t3.json"
T3_SYMPY = "Revision/pairing/kohn_sham/reports/python-t3.json"
wolfram_t3 = json.loads(repository_file(T3_WOLFRAM).read_text(encoding="utf-8"))
sympy_t3 = json.loads(repository_file(T3_SYMPY).read_text(encoding="utf-8"))
passed_w = sum(c["verdict"] == "PASS" for c in wolfram_t3["checks"])
passed_s = sum(c["verdict"] == "PASS" for c in sympy_t3["checks"])
total_w, total_s = len(wolfram_t3["checks"]), len(sympy_t3["checks"])
say(f"proof of T3: Wolfram {passed_w} of {total_w} checks pass, "
    f"sympy {passed_s} of {total_s}")
check(passed_w == total_w == 10 and passed_s == total_s == 13,
      "the proof records of T3 pass completely (10 and 13 checks)",
      record=f"{T3_WOLFRAM} and {T3_SYMPY}")
```

The two proof reports of T3 are read; `sum(c["verdict"] == "PASS" for c in ...)` counts the checks with the verdict PASS (each `True` counts as 1). The check requires 10 of 10 and 13 of 13 (Out [6]); `a == b == c` in Python means $a = b$ and $b = c$.

```python
SOLVER_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
PARAMETERS = "Revision/kohn_sham/results/parameters.json"
SELFTEST = "t3_block_map_solver_selftest"
solver_report = json.loads(repository_file(SOLVER_REPORT).read_text(encoding="utf-8"))
parameters = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
LAMBDA = {int(entry["N"]): (entry["lambda1"], entry["lambda2"])
          for entry in parameters["couplingCalibration"]["values"]}
for N, (l1, l2) in LAMBDA.items():
    say(f"N = {N:3d}: lambda_1 = {l1}, lambda_2 = {l2}")
selftest = next(c for c in solver_report["checks"] if c["name"] == SELFTEST)
```

The solver's report and the parameter record are read. `LAMBDA` maps each particle number to its pair of couplings $(\lambda_1, \lambda_2)$; Out [6] prints the table of Section 19.1 (`:3d` writes a whole number three places wide). `next(c for c in ... if ...)` takes the first check whose name is t3_block_map_solver_selftest.

```python
PATTERN = re.compile(r"N = (\d+), lambda = (\S+), a4,0 = 1: E_KS (\S+) vs (\S+); "
                     r"(\d+) levels; .*?untransformed tip b\(-L\) = 0\): "
                     r"E_KS = (\S+) vs")
RECORD = {}  # N -> the recorded numbers of the self-test
for part in selftest["detail"].split(" | "):
    found = PATTERN.search(part)
    RECORD[int(found.group(1))] = {
        "lambda": float(found.group(2)), "E_A": float(found.group(3)),
        "E_B": float(found.group(4)), "levels": int(found.group(5)),
        "E_C": float(found.group(6))}
```

The self-test stores its numbers inside a sentence, one part per particle number, separated by a vertical bar. `PATTERN` is a regular expression that matches such a part: `\d+` matches one or more digits, `\S+` one or more characters that are not blank, `.*?` as few arbitrary characters as possible, `\(` a literal bracket; every pattern in round brackets is a **group** whose matched text `found.group(k)` can be read out. A string written `r"..."` keeps its backslashes. For each part the notebook reads the particle number, the coupling, the energies of A and B, the number of levels and the energy of the control C, and stores them in `RECORD`.

```python
for N, entry in RECORD.items():
    E_A, E_B, E_C, count = (entry[key] for key in ("E_A", "E_B", "E_C", "levels"))
    say(f"record, N = {N}: E_KS(A) = {E_A:.12e}, E_KS(B) = {E_B:.12e}, "
        f"{count} levels, control E_KS(C) = {E_C:.10e}")
check(selftest["verdict"] == "PASS" and sorted(RECORD) == [8, 136]
      and all(RECORD[N]["lambda"] == LAMBDA[N][0] for N in RECORD),
      "the record holds the passing self-test for N = 8 and 136 at lambda_1",
      record=f"{SOLVER_REPORT}, check {SELFTEST}")
```

The loop prints the recorded numbers (Out [6]: the numbers of Section 19.10). The check requires the self-test to have passed, to hold exactly the particle numbers 8 and 136, and to have used the coupling $\lambda_1$ of each.

**In [7], the self-test repeated: six runs.**

```python
SELF = {}  # (N, kind) -> state
for N in (8, 136):
    for kind in "ABC":
        SELF[(N, kind)] = universe(kind, LAMBDA[N][0], 1.0, N, 0.45)
```

Six runs of the solver: A, B and C (`for kind in "ABC"` takes the three letters one after the other) for $N = 8$ and $136$, at the slice $a_{4,0} = 1$, with $\lambda_1$ and the margin $0.45$. `SELF` stores the six states under the key $(N, \text{kind})$.

```python
def sorted_levels(state):
    """The levels as a sorted list of (eps, g, f), as the self-test compares them."""
    return sorted((level[4], level[5], level[6]) for level in state["levels"])


def level_difference(first, second):
    """Largest difference of the sorted (eps, g, f) lists of two states."""
    pairs = zip(sorted_levels(first), sorted_levels(second))
    return max(max(abs(x - y) for x, y in zip(p, q)) for p, q in pairs)
```

`sorted_levels` keeps of each level the triple $(\varepsilon, g, f)$ (positions 4, 5, 6 of the tuple) and sorts the triples. `level_difference` pairs the sorted lists of two states entry by entry and returns the largest difference of any $\varepsilon$, $g$ or $f$.

```python
def integral_difference(first, second):
    """Largest relative difference of the four integrated EMT components."""
    a, b = first["emtIntegrals_2Vol7_int_e6Hy"], second["emtIntegrals_2Vol7_int_e6Hy"]
    return max(abs(a[c] - b[c]) / max(abs(a[c]), 1.0) for c in ("rho", "p3", "p_t",
                                                                "p8"))


def scalar_sum(first, second):
    """max|S_A + S_B| / max|S_A| on the 151 profile points."""
    sa, sb = first["profile"]["S"], second["profile"]["S"]
    return float(np.max(np.abs(sa + sb)) / max(np.max(np.abs(sa)), 1e-300))
```

`integral_difference` compares the four integrals $2\,\mathrm{Vol}_7\int e^{6Hy}X\,dy$ of $X = \rho, p_3, p_t, p_8$, each relative to $\max(|a|, 1)$. `scalar_sum` measures how well $S_B = -S_A$ holds: the largest $|S_A + S_B|$ over the 151 points, divided by the largest $|S_A|$ (the `1e-300` avoids a division by zero).

```python
for N in (8, 136):
    A, B, C = SELF[(N, "A")], SELF[(N, "B")], SELF[(N, "C")]
    E_A, E_B, E_C = A["E_KS"], B["E_KS"], C["E_KS"]
    count_A, count_B = len(A["levels"]), len(B["levels"])
    say(f"N = {N}: E_KS(A) = {E_A:.12e}, E_KS(B) = {E_B:.12e}, "
        f"{count_A} and {count_B} levels")
    say(f"    levels (eps, g, f): {level_difference(A, B):.2e}; EMT integrals: "
        f"{integral_difference(A, B):.2e}; |S_A + S_B|/max|S|: "
        f"{scalar_sum(A, B):.2e}; control E_KS(C) = {E_C:.10e}")
```

For each $N$ the energies, the numbers of levels and the three differences are printed (Out [7]). For $N = 8$: $E_{KS}(A) = -9.868426190876\times10^{-4}$ and $E_{KS}(B) = -9.868426190868\times10^{-4}$, the record's numbers digit for digit; 80 levels each; level difference $6.88\times10^{-14}$, integrals $8.96\times10^{-16}$, $|S_A + S_B|/\max|S|$ $1.84\times10^{-15}$; the control $-2.0145243719$. For $N = 136$: $32.39294915318$ for both, 160 levels, differences $9.86\times10^{-14}$, $2.19\times10^{-16}$, $8.38\times10^{-16}$; the control $29.283751318$. The record's self-test reports $6.91\times10^{-14}$ and $9.95\times10^{-14}$ for the level differences of its own runs; differences of this size are rounding, and all of them are ten thousand times below the tolerance.

**In [8], the self-test as checks.**

```python
TOL = 1e-9  # the tolerance of the self-test, fixed in the record
REC = f"{SOLVER_REPORT}, check {SELFTEST}"


def close(a, b, tol=TOL):
    """True when a and b agree within tol relative to max(|a|, 1)."""
    return abs(a - b) <= tol * max(abs(a), 1.0)
```

`TOL` is the record's tolerance $10^{-9}$, and `close` compares two numbers relative to $\max(|a|, 1)$: relative for large numbers, absolute for numbers below 1.

```python
for N in (8, 136):
    A, B, C = SELF[(N, "A")], SELF[(N, "B")], SELF[(N, "C")]
    rec = RECORD[N]
    check(len(A["levels"]) == len(B["levels"]) == rec["levels"]
          and level_difference(A, B) < TOL and integral_difference(A, B) < TOL
          and scalar_sum(A, B) < TOL and close(A["E_KS"], B["E_KS"]),
          f"N = {N}: A and B have equal levels, energies, EMT integrals, S_B = -S_A",
          record=REC)
    check(close(A["E_KS"], rec["E_A"]) and close(B["E_KS"], rec["E_B"])
          and close(C["E_KS"], rec["E_C"]) and abs(C["E_KS"] - A["E_KS"]) > 1.0,
          f"N = {N}: the energies of A, B and the control C are those of the record",
          record=REC)
```

Two checks per particle number (Out [8]): A and B have the recorded number of levels and agree within the tolerance in levels, integrals, scalar density and energy; and the three energies are the recorded ones, with the control more than 1 away from A.

**In [9], A is the canonical state of the record.**

```python
GROUND = "Revision/kohn_sham/results/ground"


def read_rows(relative):
    """A CSV file of the record as {id: row}."""
    with repository_file(relative).open(encoding="utf-8", newline="") as handle:
        return {row["id"]: row for row in csv.DictReader(handle)}


def homo_lumo(state):
    """The highest occupied (f = 1) and the lowest empty (f = 0) level."""
    occupied = [lv[4] for lv in state["levels"] if lv[6] > 0.5]
    empty = [lv[4] for lv in state["levels"] if lv[6] < 0.5]
    return max(occupied), min(empty)
```

`read_rows` reads a CSV table of the record into a dictionary from the state name in the column `id` to its row. `homo_lumo` returns the highest occupied level (**HOMO**: occupation above one half) and the lowest empty one (**LUMO**).

```python
summary = read_rows(f"{GROUND}/summary.csv")
integrals = read_rows(f"{GROUND}/emt-integrals.csv")
A = SELF[(136, "A")]
homo, lumo = homo_lumo(A)
new = {"E_KS": A["E_KS"], "HOMO": homo, "LUMO": lumo, "KS_gap": lumo - homo}
row = summary["N136_lamp1_a10"]
worst_scalar = max(abs(new[key] - float(row[key])) for key in new)
emt_row = integrals["N136_lamp1_a10"]
new_int = A["emtIntegrals_2Vol7_int_e6Hy"]  # the new integrals
worst_integral = max(abs(new_int[c] - float(emt_row[f"int_{c}"]))
                     / max(abs(float(emt_row[f"int_{c}"])), 1.0)
                     for c in ("rho", "p3", "p_t", "p8", "n"))
```

The record's summary table and integral table are read. For the run A at $N = 136$, $\lambda_1$, $a_{4,0} = 1$, the four numbers energy, HOMO, LUMO and the Kohn-Sham gap (LUMO minus HOMO) are compared with the row N136_lamp1_a10 of the summary, and the five integrals ($\rho$, $p_3$, $p_t$, $p_8$ and $n$) with the same row of the integral table (columns `int_rho` and so on).

```python
committed = read_profile(repository_file(f"{GROUND}/profiles/N136_lamp1_a10.csv"))
worst_profile = max(float(np.max(np.abs(A["profile"][c] - committed[c]))
                          / max(np.max(np.abs(committed[c])), 1e-300))
                    for c in committed)
for key in new:
    say(f"{key:7}: new {new[key]: .15e}   record {float(row[key]): .15e}")
say(f"largest differences: scalars {worst_scalar:.1e}, integrals "
    f"{worst_integral:.1e}, profile columns {worst_profile:.1e}")
```

The committed profile file of the state is read, and every column of the new profile is compared with it at all 151 points, relative to the column's largest value. Out [9] prints the four numbers side by side (`{key:7}` pads the name to seven places, `: .15e` writes sixteen digits with a blank for the sign): $E_{KS} = 32.39294915318298$, HOMO $0.3258848143646794$, LUMO $0.3608587569459729$, gap $0.03497394258129349$, identical to the record; all three largest differences are exactly 0.

```python
same_bytes = ((RUN_FOLDER / "A_N136_lam+0.0009298_a1.csv").read_bytes()
              == repository_file(f"{GROUND}/profiles/N136_lamp1_a10.csv").read_bytes())
report("new profile file byte-identical to the record", same_bytes)
check(worst_scalar < TOL and worst_integral < TOL and worst_profile < TOL,
      "A reproduces the canonical state N136_lamp1_a10 of the record",
      record=f"{GROUND}/summary.csv, emt-integrals.csv and profiles, N136_lamp1_a10")
```

`read_bytes` reads a file as raw bytes; `same_bytes` is true when the new profile file is identical byte for byte to the committed one. On the computer that built this book it is (`True` in Out [9]); on another computer the last digit of a few numbers may differ, which is why the check itself uses the tolerance.

**In [10], the pairing level by level (statement S1).**

```python
OTHER = {"even": "odd", "odd": "even"}  # the brane parity is exchanged


def level_map(first, second, tol=TOL):
    """Pair every level (n2, j, p, l, eps, g, f) of first with a level of second in
    (n2, -j, other p) at the same eps; return the pairs (None if one is missing)."""
    unused = list(second["levels"])
    pairs = []
    for lv in sorted(first["levels"]):
        match = [w for w in unused if w[0] == lv[0] and w[1] == -lv[1]
                 and w[2] == OTHER[lv[2]] and abs(w[4] - lv[4]) <= tol]
        if not match:
            return None
        best = min(match, key=lambda w: abs(w[4] - lv[4]))
        unused.remove(best)
        pairs.append((lv, best))
    return pairs
```

`level_map` tests statement S1 of T3: for every level of the first state it searches, among the levels of the second state not yet used, one in the same momentum shell (`w[0] == lv[0]`), with the opposite block type, the other brane parity and the same level within the tolerance. If there is none, the pairing fails and the function returns `None`; otherwise it takes the closest one (`min` with `key=` compares by the distance; `lambda w: ...` is a short unnamed function), removes it from the unused list, so that each level of the second state is used once, and records the pair.

```python
pairs136 = level_map(SELF[(136, "A")], SELF[(136, "B")])
shifts = {}
for lv, w in pairs136:
    key = f"j = {lv[1]:+d}, {lv[2]:4}"
    shifts.setdefault(key, set()).add(w[3] - lv[3])  # label of B minus label of A
for key in sorted(shifts):
    say(f"A levels with {key}: partner in j = opposite, other parity; label shift "
        f"{sorted(shifts[key])}")
worst = max(abs(lv[4] - w[4]) for lv, w in pairs136)
report("largest |eps_A - eps_B| of the paired levels, N = 136", f"{worst:.2e}")
```

For $N = 136$ every level of A is paired with its level of B. For each sector of A (type and parity) the set of label differences, label of B minus label of A, is collected (`setdefault` starts an empty set for a new key). The **label** is the solver's count of a level inside its sector, counted from the boundary conditions; A and B have different boundary conditions, so the count of a partner can be shifted by one. Out [10] shows: the type $+1$ even levels of A are partnered by type $-1$ odd levels of B with labels one lower, the type $-1$ odd levels by labels one higher, the other two sectors with the same labels. The map of T3 is fixed by the sector and the energy, not by the label. The largest level difference of the pairs is $9.86\times10^{-14}$.

```python
check(pairs136 is not None and len(pairs136) == len(SELF[(136, "B")]["levels"])
      and all(lv[5] == w[5] and lv[6] == w[6] for lv, w in pairs136),
      "every level of A has its partner in B with -j and the other brane parity",
      record="Revision/pairing/kohn_sham/t3-theory.json, statement S1")
check(level_map(SELF[(136, "A")], SELF[(136, "C")]) is None,
      "the control C has no such partner levels (the pairing fails)")
```

The first check requires the pairing to exist, to use every level of B, and to pair equal degeneracies and occupations; the second requires the same pairing to FAIL for the control.

**In [11], the level ladders (Figure 19a.1).**

```python
fig, ax = plt.subplots(figsize=(7.0, 4.6))
for x, kind in enumerate("ABC"):
    state = SELF[(136, kind)]
    for lv in state["levels"]:
        if lv[4] > 1.3:
            continue  # only the lower part of the spectrum
        full = lv[6] > 0.5  # occupied?
        ax.plot([x - 0.32, x + 0.32], [lv[4], lv[4]],
                color=COLOUR[kind] if full else "0.7", lw=2.0 if full else 1.0)
    ax.plot([x - 0.42, x + 0.42], [state["mu_or_fermi_level"]] * 2, color="0.2",
            ls="--", lw=1.0)
```

At the horizontal positions 0, 1, 2 the levels of A, B and C below $1.3$ are drawn as short horizontal lines (`continue` skips a level above $1.3$), in the universe's colour and thicker when occupied, light grey and thinner when empty (`a if condition else b` chooses between two values). A dashed dark line marks the Fermi level that the solver reports (`[value] * 2` is a list holding the value twice, the heights of the two ends of the line).

```python
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["A: $+m$, $\\theta = 0$", "B: $-m$, $\\theta = \\pi$",
                    "C: $-m$, $\\theta = 0$ (control)"])
ax.set_xlim(-0.6, 2.6)
ax.set_ylabel("Kohn-Sham level $\\varepsilon$ (units of $|m|$)")
ax.set_title("$N = 136$, $\\lambda = \\lambda_1$, slice $a_{4,0} = 1$")
ax.grid(axis="x", visible=False)
save_figure(fig, "level_ladder",
            "Level ladders of the three universes A (bare mass $+m$, tip angle 0), B "
            "(bare mass $-m$, the same coupling, tip angle $\\pi$: the T3 partner) "
            "and C (bare mass $-m$, tip angle 0: the control) for $N = 136$ "
            "particles, $\\lambda = \\lambda_1$, slice $a_{4,0} = 1$, all solved "
            "independently by the Rust solver. Each short line is one Kohn-Sham "
            "level (vertical axis, units of $|m|$), coloured when occupied and grey "
            "when empty; the dashed line is the Fermi level. A and B are the same "
            "ladder; C, with the untransformed tip, is a different one.")
```

Labels, limits and title; `save_figure` saves Figure 19a.1. What the student should see: two identical ladders for A and B, occupied up to the dashed Fermi level, which the solver reports at the highest occupied level $0.3259$ (the HOMO of In [9]), with the first empty level at $0.3609$; a different ladder for the control C, with its levels at other heights.

**In [12], the level-by-level differences (Figure 19a.2).**

```python
FLOOR = 1e-17  # where exact zeros are drawn on the logarithmic axis
eps = {kind: np.array([e for e, g, f in sorted_levels(SELF[(136, kind)])])
       for kind in "ABC"}
index = np.arange(1, len(eps["A"]) + 1)
fig, ax = plt.subplots()
ax.semilogy(index, np.maximum(np.abs(eps["A"] - eps["B"]), FLOOR), "o",
            color=COLOUR["B"], ms=4, label="A against B (T3 partner)")
ax.semilogy(index, np.maximum(np.abs(eps["A"] - eps["C"]), FLOOR), "^",
            color=COLOUR["C"], ms=4, label="A against C (control)")
ax.axhline(TOL, color="0.3", ls="--", lw=1.0, label="tolerance $10^{-9}$")
```

`eps` holds the sorted levels of A, B and C (the tuple `(e, g, f)` is unpacked and only `e` kept); `index` numbers them $1, 2, \dots, 160$. `semilogy` draws with a **logarithmic** vertical axis (equal steps for each factor of ten). A logarithm of zero does not exist, so `np.maximum(..., FLOOR)` raises every exact zero to $10^{-17}$. A dashed horizontal line marks the tolerance.

```python
ax.set_xlabel("level number $i$ (levels sorted by energy)")
ax.set_ylabel("$|\\varepsilon_{A,i} - \\varepsilon_{X,i}|$ (units of $|m|$)")
ax.set_title("$N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$: 160 levels")
ax.legend(fontsize=8, loc="center right")
save_figure(fig, "level_differences",
            "Level-by-level differences between universe A and its T3 partner B "
            "(orange circles) and between A and the control C (aqua triangles), "
            "for $N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$; horizontal axis "
            "the number of the level in the sorted list, vertical axis the absolute "
            "difference in units of $|m|$ (logarithmic; exact zeros drawn at "
            "$10^{-17}$). The partner agrees to $10^{-13}$ or better, the rounding "
            "of the computer, far below the tolerance $10^{-9}$ (dashed); the "
            "control differs by $10^{-4}$ to $1$.")
```

Axis labels, title and legend; `save_figure` saves Figure 19a.2.

```python
max_partner = float(np.max(np.abs(eps["A"] - eps["B"])))
gaps_control = np.abs(eps["A"] - eps["C"])
report("largest level difference A - B", f"{max_partner:.2e}")
report("smallest and largest level difference A - C",
       f"{gaps_control.min():.2e} and {gaps_control.max():.3g}")
check(max_partner < 1e-12 and 1e-4 < gaps_control.min() and gaps_control.max() < 1,
      "levels: A - B below 1e-12, A - C between 1e-4 and 1 (the caption's ranges)")
```

The numbers behind the picture (Out [12]): A and B differ by at most $9.86\times10^{-14}$; A and C by between $1.88\times10^{-4}$ and $0.456$. The check guards the ranges that the caption states. What the student should see: a band of orange circles between the floor $10^{-17}$ and about $10^{-13}$, far below the dashed tolerance line, and the aqua triangles eight to sixteen powers of ten higher.

**In [13], the densities point by point (statements S3 and S4).**

```python
EVEN = ("n", "v_v", "e_int", "rho", "p3", "p_t", "p8")  # unchanged by the map
ODD = ("S", "Q", "M_eff")  # change sign under the map


def profile_mismatch(first, second):
    """Largest relative mismatch of the T3 rule (even columns equal, odd opposite)."""
    worst = 0.0
    for column in EVEN + ODD:
        sign = -1.0 if column in ODD else 1.0
        a, b = first["profile"][column], second["profile"][column]
        scale = max(float(np.max(np.abs(a))), 1e-300)
        worst = max(worst, float(np.max(np.abs(b - sign * a))) / scale)
    return worst
```

`EVEN` and `ODD` list the profile columns that T3 keeps and those it reverses (Section 19.9). `profile_mismatch` measures, for every column, the largest deviation of the second state's column from the first state's column times the expected sign, relative to the column's largest value, and returns the worst one.

```python
for N in (8, 136):
    mismatch = profile_mismatch(SELF[(N, "A")], SELF[(N, "B")])
    control = profile_mismatch(SELF[(N, "A")], SELF[(N, "C")])
    say(f"N = {N}: T3 rule for B: {mismatch:.2e}; the same rule for C: {control:.3g}")
    check(mismatch < TOL and control > 0.1,
          f"N = {N}: n, v_v, e_int, rho, p3, p_t, p8 equal; S, Q, M_eff opposite",
          record="Revision/pairing/kohn_sham/t3-theory.json, statements S3 and S4")
```

Out [13]: the partner B obeys the rule to $2.78\times10^{-15}$ ($N = 8$) and $5.80\times10^{-15}$ ($N = 136$); the control C violates it by factors of 298 and 4650 (its profiles are many times larger than those of A in some columns). Both checks pass.

**In [14], the densities (Figure 19a.3).**

```python
y = SELF[(136, "A")]["profile"]["y"]  # the 151 points from the tip to the brane
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
STYLE = {"A": dict(lw=2.6), "B": dict(lw=1.6, ls="--"), "C": dict(lw=1.4, ls=":")}
for kind in "ABC":
    prof = SELF[(136, kind)]["profile"]
    left.semilogy(y, prof["n"], color=COLOUR[kind], label=NAME[kind], **STYLE[kind])
    if kind != "C":
        right.plot(y, prof["S"], color=COLOUR[kind], label=NAME[kind],
                   **STYLE[kind])
```

`y` holds the 151 points. `STYLE` gives each universe a line width and style: A thick and solid, B thinner and dashed (so that A shows around it), C dotted; `dict(lw=2.6)` makes a dictionary, and `**STYLE[kind]` passes its entries as named arguments to `plot`. The left axes show the particle density $n(y)$ of the three universes on a logarithmic axis, the right axes the scalar density $S(y)$ of A and B only.

```python
left.set_xlabel("hidden coordinate $y$ (tip $-3$, brane $0$)")
left.set_ylabel("proper particle density $n(y)$")
left.legend(fontsize=7, loc="upper right")
right.set_xlabel("hidden coordinate $y$")
right.set_ylabel("proper scalar density $S(y)$")
right.axhline(0.0, color="0.3", lw=0.8)
right.legend(fontsize=7, loc="lower right")
fig.suptitle("$N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$", fontsize=10)
fig.tight_layout()
save_figure(fig, "density_profiles",
            "Left: the proper particle density $n(y)$ of the universes A (blue), B "
            "(orange, dashed) and C (aqua, dotted) for $N = 136$, "
            "$\\lambda = \\lambda_1$, $a_{4,0} = 1$, against the hidden coordinate $y$ "
            "from the tip $y = -3$ to the brane $y = 0$ (logarithmic vertical axis, "
            "units $|m|^7$). Right: the proper scalar density $S(y)$ of A and B. "
            "The density of B is that of A, and its scalar density is the mirror "
            "image $S_B = -S_A$, as T3 states. The control C has its own densities; "
            "its scalar density, more than ten times larger, is not drawn.")
```

Labels, a zero line on the right, legends and a common title (`suptitle`); `save_figure` saves Figure 19a.3. What the student should see: on the left the density of A falls from about 300 at the tip to about 0.009 at the brane (the record's profile file of N136_lamp1_a10: $298.7$ and $0.008849$), large at the tip because a proper density is a number per unit proper volume, and the proper volume factor $e^{6Hy}$ is tiny there; the dashed orange line of B lies exactly on the blue line of A; the dotted line of C is different. On the right $S_A$ is negative between the ends and zero at both ends (the tip condition $b(-L) = 0$ and either brane condition make $2ab$ vanish there), and $S_B$ is its mirror image, positive.

```python
size = {kind: float(np.max(np.abs(SELF[(136, kind)]["profile"]["S"])))
        for kind in "AC"}
factor = size["C"] / size["A"]  # how much larger the control's scalar density is
report("largest |S| of C divided by largest |S| of A", f"{factor:.1f}")
check(factor > 10.0,
      "the scalar density of the control is more than ten times that of A")
```

The caption says the control's scalar density is more than ten times larger; the cell measures the factor ($24.1$, Out [14]) and checks it.

**In [15], the mass and the potential (Figure 19a.4).**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
for kind in "ABC":
    prof = SELF[(136, kind)]["profile"]
    left.plot(y, prof["M_eff"], color=COLOUR[kind], label=NAME[kind], **STYLE[kind])
    right.plot(y, prof["v_v"], color=COLOUR[kind], label=NAME[kind], **STYLE[kind])
left.set_xlabel("hidden coordinate $y$")
left.set_ylabel("effective mass $M_{eff}(y)$ (units of $|m|$)")
left.legend(fontsize=7, loc="center right")
right.set_xlabel("hidden coordinate $y$")
right.set_ylabel("potential $v_v(y)$ (units of $|m|$)")
fig.suptitle("$N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$", fontsize=10)
fig.tight_layout()
```

The self-consistent effective mass $M_{\rm eff}(y)$ (left) and potential $v_v(y)$ (right) of the three universes, in the same styles.

```python
save_figure(fig, "mass_and_potential",
            "Left: the self-consistent effective mass $M_{eff}(y)$ of A (blue), B "
            "(orange, dashed) and C (aqua, dotted) for $N = 136$, "
            "$\\lambda = \\lambda_1$, $a_{4,0} = 1$ (units of $|m|$). Right: the "
            "self-consistent potential $v_v(y)$ (units of $|m|$). B has exactly the "
            "opposite mass of A at every point and the same potential: this is why "
            "the bare mass must change sign while the coupling keeps its sign. The "
            "control C has the mass $-m$ but its own, different mean field.")
```

`save_figure` saves Figure 19a.4. What the student should see: on the left the mass of A near $+1$, with a dip to about $0.97$ near $y = -2.4$ where $S$ is most negative ($1 + \frac{15}{16}\lambda_1 S$ with $S \approx -37$ in the record's profile), and the mass of B its exact negative near $-1$; the control near $-1$ with its own shape. On the right the potentials of A and B on top of each other, small and negative (about $-0.017$ at the tip), and the control's different curve.

**In [16], the energy-momentum profiles (Figure 19a.5).**

```python
weight = np.exp(6.0 * y)  # the proper-volume factor e^{6 H y}, H = 1
fig, axes = plt.subplots(2, 2, figsize=(9.0, 6.0), sharex=True)
for ax, column, title in zip(axes.flat, ("rho", "p3", "p_t", "p8"),
                             ("energy density $\\rho$", "pressure $p_3$ (3-space)",
                              "pressure $p_t$ (extra times)",
                              "pressure $p_8$ (hidden direction)")):
    for kind in "ABC":
        prof = SELF[(136, kind)]["profile"]
        ax.plot(y, weight * prof[column], color=COLOUR[kind], label=NAME[kind],
                **STYLE[kind])
    ax.set_title(title, fontsize=9)
    ax.set_ylabel("$e^{6Hy}$ times the component")
for ax in axes[1]:
    ax.set_xlabel("hidden coordinate $y$")
axes[0, 0].legend(fontsize=7, loc="upper left")
fig.tight_layout()
```

`weight` is the volume factor $e^{6Hy}$ at the 151 points; multiplying a proper density by it gives a density per unit of $y$, so the area under each curve is proportional to the integral over the hidden direction. A grid of $2 \times 2$ axes with a common horizontal axis (`sharex=True`) shows $\rho$, $p_3$, $p_t$, $p_8$ times the weight, one per axes, for the three universes; `zip` runs through the axes, the column names and the titles together. Only the lower row gets the horizontal label (`axes[1]` is the second row), and only the first axes the legend.

```python
save_figure(fig, "emt_profiles",
            "The energy-momentum profiles of A (blue), B (orange, dashed) and C "
            "(aqua, dotted) for $N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$: "
            "energy density $\\rho$, pressures $p_3$ (3-space), $p_t$ (the "
            "deflating extra times) and $p_8$ (hidden direction), each times the "
            "volume factor $e^{6Hy}$, against the hidden coordinate $y$ (units "
            "$|m|^8$ with $H = 1$). The four profiles of the partner B coincide "
            "with those of A at every point (T3, statement S4); the control C "
            "differs.")
```

`save_figure` saves Figure 19a.5. What the student should see: in all four panels the dashed orange curve of B exactly on the blue curve of A, and the dotted aqua curve of the control elsewhere; $p_t = e_{\rm int}$ is much smaller than the other three, because the good sector has no kinetic pressure along the extra times.

```python
for N in (8, 136):
    B = SELF[(N, "B")]
    integrated, pointwise = (B["yConservationIntegratedRel"],
                             B["yConservationPointwiseRel"])
    say(f"N = {N}, B: y-conservation, integrated {integrated:.1e}, pointwise "
        f"{pointwise:.1e} (relative)")
    check(integrated < 1e-8 and pointwise < 1e-6,
          f"N = {N}: the partner B obeys p8' + 6H p8 = 3H (p3 + p_t)",
          record=f"{SOLVER_REPORT}, checks emt_y_conservation_integrated, pointwise")
```

The solver measures for every state how well the conservation law $p_8' + 6Hp_8 = 3H(p_3 + p_t)$ of Section 19.4 holds, after integration over $y$ and point by point. For the partner B the residuals are $3.9\times10^{-13}$ and $2.2\times10^{-9}$ ($N = 8$) and $1.7\times10^{-12}$ and $8.4\times10^{-11}$ ($N = 136$) (Out [16]), below the tolerances $10^{-8}$ and $10^{-6}$ used here; B is a genuine self-consistent state of its own problem.

**In [17], where the zero modes live: three free runs.**

```python
FREE8 = {kind: universe(kind, 0.0, 1.0, 8, 0.25) for kind in "ABC"}  # lambda = 0
L_TIP, M_BARE = 3.0, 1.0  # the tip distance L and the bare mass |m| of the record


def brane_over_tip(state):
    """Coordinate density e^{6Hy} n(y) at the brane divided by its value at the tip."""
    n = state["profile"]["n"]
    return float(n[-1] * weight[-1] / (n[0] * weight[0]))
```

Three runs without interaction for $N = 8$ at $a_{4,0} = 1$ (margin $0.25$): the eight quanta fill the eight zero modes. `brane_over_tip` divides the coordinate density $e^{6Hy}n$ at the last point (the brane, index $-1$) by its value at the first point (the tip, index 0).

```python
expected = {"A": math.exp(2 * M_BARE * L_TIP), "B": math.exp(2 * M_BARE * L_TIP),
            "C": math.exp(-2 * M_BARE * L_TIP)}  # e^{+6}, e^{+6}, e^{-6}
ratio_error = 0.0
for kind in "ABC":
    ratio = brane_over_tip(FREE8[kind])
    ratio_error = max(ratio_error, abs(ratio / expected[kind] - 1.0))
    say(f"{kind}: brane / tip = {ratio:.6e}, closed form {expected[kind]:.6e}")
check(ratio_error < 1e-8,
      "free N = 8: the zero modes of A and B live at the brane, those of C at the tip")
```

The closed forms of Section 19.12: the ratio is $e^{2mL} = e^6$ for A and B and $e^{-6}$ for C. Out [17] prints $403.4288$ for A and B and $0.002478752$ for C, equal to the closed forms; the check requires a relative agreement better than $10^{-8}$.

**In [18], the control's level in the gap, by hand.**

```python
def bound_state_q(m, L):
    """The root q in (0, m) of tanh(q L) - q / m, by bisection."""
    low, high = 0.5 * m, m  # the function is positive at m/2 and negative at m
    for _ in range(200):
        middle = 0.5 * (low + high)
        if math.tanh(middle * L) - middle / m > 0.0:
            low = middle  # the root lies above the middle
        else:
            high = middle  # the root lies below the middle
    return 0.5 * (low + high)
```

`bound_state_q` finds the root of $\tanh(qL) = q/m$ of Section 19.12 by bisection, starting from the interval $(m/2, m)$, where the function changes sign (at $m/2$: $\tanh(1.5) - 0.5 = 0.405 > 0$; at $m$: $\tanh(3) - 1 < 0$). Each of the 200 steps keeps the half that contains the root.

```python
q_root = bound_state_q(M_BARE, L_TIP)
eps_b = M_BARE / math.cosh(q_root * L_TIP)  # the level inside the gap
report("q of the control's sub-gap level", f"{q_root:.12f}")
report("sub-gap level eps_b = m / cosh(q L)", f"{eps_b:.12f}", "|m|")
gap = {}
for kind in "ABC":
    homo, lumo = homo_lumo(FREE8[kind])
    gap[kind] = lumo - homo
    say(f"{kind}: HOMO {homo:.3e}, LUMO {lumo:.12f}, Kohn-Sham gap {gap[kind]:.12f}")
```

The root $q = 0.994901528453$ and the level $\varepsilon_b = m/\cosh(qL) = 0.100851121375$ (Out [18]). Then the Kohn-Sham gaps of the three free runs: in all three the HOMO is the zero modes at 0. For A and B the lowest empty level is $0.170349251323$, a level of the brane band at the smallest nonzero momentum shell; for the control it is $0.100851121375$: its level inside the gap, lower than its brane band.

```python
recorded = float(summary["N8_lam0_a10"]["KS_gap"])
same_level = abs(math.sqrt(M_BARE ** 2 - q_root ** 2) - eps_b) < 1e-12  # two forms
check(abs(gap["C"] - eps_b) < 1e-9 and same_level,
      "the free control has the Kohn-Sham gap m/cosh(qL) of the sub-gap level")
check(close(gap["A"], recorded) and close(gap["B"], gap["A"]),
      "the free A and B have the gap of the committed state N8_lam0_a10",
      record=f"{GROUND}/summary.csv, N8_lam0_a10, column KS_gap")
```

The first check: the control's gap equals $\varepsilon_b$, a number derived by hand, to $10^{-9}$ (in fact to twelve digits), and the two forms $\sqrt{m^2 - q^2}$ and $m/\cosh(qL)$ agree. The second: A has the gap of the committed state N8_lam0_a10, and B the gap of A.

**In [19], the zero modes (Figure 19a.6).**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8), sharey=True)
for kind in "ABC":
    left.semilogy(y, weight * FREE8[kind]["profile"]["n"], color=COLOUR[kind],
                  label=NAME[kind], **STYLE[kind])
    right.semilogy(y, weight * SELF[(8, kind)]["profile"]["n"], color=COLOUR[kind],
                   label=NAME[kind], **STYLE[kind])
top = {kind: float(weight[-1] * FREE8[kind]["profile"]["n"][-1]) for kind in "AC"}
left.semilogy(y, top["A"] * np.exp(2 * M_BARE * y), "k:", lw=0.8)  # e^{2 m y}
left.semilogy(y, top["C"] * np.exp(-2 * M_BARE * y), "k:", lw=0.8)  # e^{-2 m y}
```

Two axes with a common vertical scale (`sharey=True`): on the left the coordinate densities $e^{6Hy}n$ of the free runs, on the right those of the interacting runs of In [7]. `top` holds the brane values of the free A and C, and the two thin black dotted lines are the closed forms $e^{2my}$ and $e^{-2my}$ scaled to these values.

```python
left.set_title("$N = 8$, $\\lambda = 0$, $a_{4,0} = 1$", fontsize=10)
right.set_title("$N = 8$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$", fontsize=10)
left.set_ylabel("coordinate density $e^{6Hy}\\,n(y)$")
for ax in (left, right):
    ax.set_xlabel("hidden coordinate $y$ (tip $-3$, brane $0$)")
right.legend(fontsize=7, loc="lower right")
fig.tight_layout()
save_figure(fig, "zero_modes_n8",
            "The coordinate particle density $e^{6Hy}n(y)$ (particles per unit of "
            "$y$; logarithmic vertical axis) of the $N = 8$ universes A (blue), B "
            "(orange, dashed) and C (aqua, dotted) at $a_{4,0} = 1$, against the "
            "hidden coordinate $y$ from the tip $-3$ to the brane $0$. Left: without "
            "interaction; the thin black dotted lines are the closed forms "
            "$e^{2my}$ and $e^{-2my}$. A and B hold their particles in zero modes "
            "at the brane; with the untransformed tip (C) the zero modes sit at the "
            "tip. Right: with the coupling $\\lambda_1$; A and B are unchanged in "
            "shape, the control is reshaped by its strong mean field near the tip.")
```

Titles, labels, legend; `save_figure` saves Figure 19a.6. What the student should see: on the left two straight lines on the logarithmic scale, the rising one of A and B (B dashed on top of A) along $e^{2my}$, and the falling one of C along $e^{-2my}$, each covering a factor $e^6 \approx 403$ between tip and brane; on the right A and B unchanged in shape, and the control's line bent near the tip, where its quanta, at a huge proper density, feel a strong mean field.

**In [20], T3 along the deflating history: 27 runs.**

```python
SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]
HIST = {}  # (N, kind, a4) -> state
for N in (136, 688):
    for a4 in SLICES:
        for kind in "ABC":
            if N == 136 and a4 == 1.0:
                HIST[(N, kind, a4)] = SELF[(N, kind)]  # already solved
            else:
                HIST[(N, kind, a4)] = universe(kind, LAMBDA[N][0], a4, N, 0.45)
```

A, B and C at the five slices of the history for $N = 136$ and $688$, each with its coupling $\lambda_1$: 30 states, of which the three of $N = 136$ at $a_{4,0} = 1$ were solved in In [7] and are reused, so 27 new runs.

```python
ok_record, ok_partner, ok_control = True, True, True
partner_rel, control_pct = [], []  # relative differences A - B, percents A - C
for N in (136, 688):
    for a4 in SLICES:
        A, B, C = (HIST[(N, kind, a4)] for kind in "ABC")
        record_energy = float(summary[f"N{N}_lamp1_a{round(10 * a4):02d}"]["E_KS"])
        ok_record &= close(A["E_KS"], record_energy)
        partner_rel.append(abs(A["E_KS"] - B["E_KS"]) / abs(A["E_KS"]))
        control_pct.append(100.0 * abs(A["E_KS"] - C["E_KS"]) / abs(A["E_KS"]))
        ok_partner &= level_difference(A, B) < TOL and profile_mismatch(A, B) < TOL
        E_A, E_B, E_C = A["E_KS"], B["E_KS"], C["E_KS"]
        say(f"N = {N:3d}, a4,0 = {a4:3.1f}: E_KS A {E_A:.10f}, "
            f"B {E_B:.10f}, C {E_C:.6f}")
```

For each of the ten pairs (particle number, slice): the state name of the record is made from the particle number and ten times the slice written with two digits (`:02d`, so $0.5$ gives `a05`), and A must reproduce the recorded energy (`&=` keeps a truth value true only while every test is true); the relative energy difference A minus B and the percentage A minus C are collected; and B must agree with A in levels and in every profile column. The loop prints the three energies (Out [20]):

| $N$ | $a_{4,0}$ | $E_{KS}$ of A and B | $E_{KS}$ of C |
| --- | --- | --- | --- |
| 136 | 0.0 | 80.2837009244 | 73.179866 |
| 136 | 0.5 | 51.2491613321 | 46.475561 |
| 136 | 1.0 | 32.3929491532 | 29.283751 |
| 136 | 1.5 | 20.2130306754 | 18.533932 |
| 136 | 2.0 | 12.4470595905 | 12.175574 |
| 688 | 0.0 | 680.4447575708 | 670.715818 |
| 688 | 0.5 | 437.5215029073 | 431.359438 |
| 688 | 1.0 | 279.4468465636 | 275.745397 |
| 688 | 1.5 | 176.7808903556 | 175.297541 |
| 688 | 2.0 | 110.4456550192 | 112.097612 |

```python
report("largest relative E_KS difference A - B", f"{max(partner_rel):.1e}")
report("relative E_KS difference A - C", f"{min(control_pct):.1f} to "
       f"{max(control_pct):.1f}", "percent")
check(ok_record, "A reproduces the recorded E_KS at all 10 states of the history",
      record=f"{GROUND}/summary.csv, N136_lamp1_a00 to a20, N688_lamp1_a00 to a20")
check(ok_partner and max(partner_rel) < 1e-13,
      "B has the levels, energy and profiles of A at every slice")
check(0.5 < min(control_pct) and max(control_pct) < 10.0,
      "the control C differs from A by 0.5 to 10 percent at every slice")
```

The largest relative difference between A and B along the whole history is $4.0\times10^{-14}$; the control differs by $0.8$ to $9.6$ percent. Three checks: A is the record at all ten states; B is A at every slice; C differs at every slice. This is T3 slice by slice, as Section 19.6 predicted.

**In [21], the energy along the history (Figure 19a.7).**

```python
fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.8))
MARK = {"A": dict(marker="o", ms=7, lw=2.2), "B": dict(marker="s", ms=4, lw=1.4,
                                                       ls="--"),
        "C": dict(marker="^", ms=6, lw=1.2, ls=":"),
        "D": dict(marker="D", ms=5, lw=1.4)}
for ax, N in zip(axes, (136, 688)):
    for kind in "ABC":
        ax.plot(SLICES, [HIST[(N, kind, a4)]["E_KS"] for a4 in SLICES],
                color=COLOUR[kind], label=NAME[kind], **MARK[kind])
    ax.set_xlabel("slice $a_{4,0}$ of the history $a_4 = Hx_4$")
    ax.set_ylabel("Kohn-Sham energy $E_{KS}$ (units of $|m|$)")
    ax.set_title(f"$N = {N}$, $\\lambda = \\lambda_1$", fontsize=10)
axes[0].legend(fontsize=7, loc="upper right")
fig.tight_layout()
```

`MARK` gives each universe a marker (circle, square, triangle, diamond), a marker size and a line style, used in this figure and in Figures 19a.9 and 19a.10. The two axes show $E_{KS}$ against the slice for $N = 136$ and $N = 688$.

```python
save_figure(fig, "history_energy",
            "The Kohn-Sham energy $E_{KS}$ (units of $|m|$) of A (blue circles), B "
            "(orange squares, dashed) and C (aqua triangles, dotted) at the five "
            "slices $a_{4,0} = 0$ to $2$ of the deflating history, for $N = 136$ "
            "(left) and $N = 688$ (right) at the coupling $\\lambda_1$ of each $N$. "
            "The energy falls because the 3-momenta are redshifted as 3-space "
            "inflates and the extra times deflate; the T3 partner B follows A at "
            "every slice, the control C does not.")
```

`save_figure` saves Figure 19a.7. What the student should see: falling curves, from $80.3$ to $12.4$ ($N = 136$) and from $680$ to $110$ ($N = 688$), with B's small squares inside A's circles at every slice and the control's triangles below them (above at the last slice of $N = 688$). The fall is the redshift of Chapter 14: a later slice is the first slice with every 3-momentum multiplied by $e^{-a_{4,0}}$.

**In [22], the agreement along the history (Figure 19a.8).**

```python
fig, ax = plt.subplots()
for N, marker in ((136, "o"), (688, "s")):
    for kind in "BC":
        values = [max(abs(HIST[(N, "A", a4)]["E_KS"] - HIST[(N, kind, a4)]["E_KS"])
                      / abs(HIST[(N, "A", a4)]["E_KS"]), FLOOR) for a4 in SLICES]
        ax.semilogy(SLICES, values, marker=marker, color=COLOUR[kind],
                    ls="--" if kind == "B" else ":",
                    label=f"$N = {N}$, A against {kind}")
ax.axhline(TOL, color="0.3", lw=1.0, label="tolerance $10^{-9}$")
ax.set_xlabel("slice $a_{4,0}$ of the history")
ax.set_ylabel("relative difference of $E_{KS}$")
ax.legend(fontsize=7, loc="center right")
```

For both particle numbers and for B and C, the relative energy difference from A at the five slices, raised to the floor $10^{-17}$ where it is exactly zero, on a logarithmic axis, with the tolerance line.

```python
save_figure(fig, "history_agreement",
            "Relative differences of the Kohn-Sham energy between A and its T3 "
            "partner B (orange) and between A and the control C (aqua) at the five "
            "slices of the history, for $N = 136$ (circles) and $N = 688$ (squares); "
            "logarithmic vertical axis, exact zeros drawn at $10^{-17}$. The "
            "partner agrees to better than $10^{-13}$ at every slice: T3 holds slice "
            "by slice along the deflating history. The control is off by $0.5$ to "
            "$10$ percent.")
```

`save_figure` saves Figure 19a.8. What the student should see: the orange curves between $10^{-17}$ and a few times $10^{-14}$, far below the tolerance line; the aqua curves between about $8\times10^{-3}$ and $0.1$.

**In [23], the coupling must keep its sign: 17 runs.**

```python
l1, l2 = LAMBDA[136]
COUPLINGS = [("lamm2", -l2, 0.85), ("lamm1", -l1, 0.45), ("lam0", 0.0, 0.25),
             ("lamp1", l1, 0.45), ("lamp2", l2, 0.85)]  # tag, lambda, margin
SCAN = {}  # (tag, kind) -> state
for tag, lam, margin in COUPLINGS:
    for kind in "ABCD":
        if tag == "lamp1" and kind in "ABC":
            SCAN[(tag, kind)] = SELF[(136, kind)]  # already solved
        else:
            SCAN[(tag, kind)] = universe(kind, lam, 1.0, 136, margin)
MIRROR = {"lamm2": "lamp2", "lamm1": "lamp1", "lam0": "lam0", "lamp1": "lamm1",
          "lamp2": "lamm2"}  # the tag of -lambda
```

The five couplings $-\lambda_2, -\lambda_1, 0, +\lambda_1, +\lambda_2$ of $N = 136$, each with the record's tag and margin, for all four universes at $a_{4,0} = 1$: 20 states, three reused from In [7], so 17 new runs (D at $+\lambda_1$ is new). `MIRROR` gives for each tag the tag of the opposite coupling.

```python
ok_record, ok_partner, ok_mirror, ok_wrong = True, True, True, True
control_gap = []  # |E_C - E_A| at each coupling
for tag, lam, margin in COUPLINGS:
    E = {kind: SCAN[(tag, kind)]["E_KS"] for kind in "ABCD"}
    ok_record &= close(E["A"], float(summary[f"N136_{tag}_a10"]["E_KS"]))
    ok_partner &= close(E["A"], E["B"]) and level_difference(
        SCAN[(tag, "A")], SCAN[(tag, "B")]) < TOL
    ok_mirror &= close(E["D"], SCAN[(MIRROR[tag], "A")]["E_KS"])
    ok_wrong &= (lam == 0.0) or abs(E["D"] - E["A"]) > 1e-4
    control_gap.append(abs(E["C"] - E["A"]))
    E_A, E_B, E_C, E_D = (E[kind] for kind in "ABCD")
    say(f"lambda = {lam:+.4e}: A {E_A:.10f}  B {E_B:.10f}  "
        f"C {E_C:.6f}  D {E_D:.10f}")
```

For every coupling, four things are tested. The truth value `ok_record`: A is the record's state of that tag, one of N136_lamm2_a10 to N136_lamp2_a10. The truth value `ok_partner`: B equals A in energy and levels. The truth value `ok_mirror`: D at $\lambda$ equals A at $-\lambda$, because D $= (-m, -\lambda, \pi)$ is the T3 partner of $(m, -\lambda, 0)$. The truth value `ok_wrong`: D differs from A by more than $10^{-4}$ unless $\lambda = 0$ (at $\lambda = 0$, D and B are the same problem). The loop prints the four energies (Out [23]):

| $\lambda$ | A and B | C | D |
| --- | --- | --- | --- |
| $-0.002789$ | 32.3593734113 | 34.540794 | 32.4116192324 |
| $-0.0009298$ | 32.3755880337 | 33.529490 | 32.3929491532 |
| $0$ | 32.3841156874 | 30.731389 | 32.3841156874 |
| $+0.0009298$ | 32.3929491532 | 29.283751 | 32.3755880337 |
| $+0.002789$ | 32.4116192324 | 28.980584 | 32.3593734113 |

Read the D column from the bottom up: it is the A column. The control differs even at $\lambda = 0$, because its tip is wrong.

```python
check(ok_record, "A reproduces the recorded E_KS for all five couplings",
      record=f"{GROUND}/summary.csv, N136_lamm2_a10 to N136_lamp2_a10")
check(ok_partner, "B = A for every coupling: the partner keeps +lambda")
check(ok_mirror and ok_wrong,
      "D(lambda) = A(-lambda), so (-m, -lambda) is not the partner for lambda != 0",
      record="Revision/pairing/kohn_sham/reports/python-t3.json, check "
             "T3.mean_field_map (control)")
check(1.0 < min(control_gap) and max(control_gap) < 3.5,
      "the control C differs from A by 1 to 3.5 at every coupling")
```

Four checks (Out [23]); the third is the numerical face of the control of Step 3 (Section 19.8), and the fourth guards the range $1.15$ to $3.43$ that the caption of Figure 19a.9 states as "1 to 3.5".

**In [24], the coupling scan (Figure 19a.9).**

```python
x = [lam / l1 for tag, lam, margin in COUPLINGS]
E0 = SCAN[("lam0", "A")]["E_KS"]
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
for kind in "ABD":
    left.plot(x, [SCAN[(tag, kind)]["E_KS"] - E0 for tag, lam, margin in COUPLINGS],
              color=COLOUR[kind], label=NAME[kind], **MARK[kind])
left.set_xlabel("coupling $\\lambda/\\lambda_1$")
left.set_ylabel("$E_{KS} - E_{KS}(\\lambda = 0)$ (units of $|m|$)")
left.axhline(0.0, color="0.3", lw=0.8)
low, high = left.get_ylim()
left.set_ylim(low, high + 0.6 * (high - low))  # room for the legend at the top
left.legend(fontsize=7, loc="upper center")
```

The horizontal axis is the coupling in units of $\lambda_1$: $-3, -1, 0, 1, 3$ (the tuples of `COUPLINGS` are unpacked into three names, of which only `lam` is used). On the left, the interaction part of the energy, $E_{KS}$ minus the value of A at $\lambda = 0$, for A, B and D. `get_ylim` reads the vertical range that matplotlib chose, and `set_ylim` enlarges it upward by 60 percent so that the legend does not cover the curves.

```python
for kind in "AC":
    right.plot(x, [SCAN[(tag, kind)]["E_KS"] for tag, lam, margin in COUPLINGS],
               color=COLOUR[kind], label=NAME[kind], **MARK[kind])
right.set_xlabel("coupling $\\lambda/\\lambda_1$")
right.set_ylabel("$E_{KS}$ (units of $|m|$)")
right.legend(fontsize=7, loc="upper right")
fig.suptitle("$N = 136$, slice $a_{4,0} = 1$", fontsize=10)
fig.tight_layout()
save_figure(fig, "coupling_scan",
            "Left: the interaction part of the Kohn-Sham energy, $E_{KS}$ minus its "
            "value at $\\lambda = 0$ (units of $|m|$), against the coupling "
            "$\\lambda/\\lambda_1$ for $N = 136$, $a_{4,0} = 1$: universe A (blue), "
            "its T3 partner B with the same coupling (orange, dashed, on top of A) "
            "and D with the reversed coupling (yellow diamonds), which is the "
            "mirror image of A. Right: $E_{KS}$ of A and of the control C (aqua), "
            "which lies $1$ to $3.5$ away from A, above it for negative and below "
            "it for positive couplings. Only $(-m, +\\lambda)$ with the transformed "
            "tip is the partner of $(m, \\lambda)$.")
```

On the right, the energies of A and C. `save_figure` saves Figure 19a.9. What the student should see: on the left A's curve rising from $-0.025$ at $-3\lambda_1$ through 0 to $+0.027$ at $+3\lambda_1$, B's squares on it, and D's diamonds on the curve reflected about the vertical axis; on the right A's nearly flat curve near 32.4 and the control's falling curve, above A for the negative couplings and below A from $\lambda = 0$ on.

**In [25], thermal states: nine runs.**

```python
THERMO = read_rows("Revision/kohn_sham/results/thermo/thermodynamics.csv")
TEMPS = [0.01, 0.02, 0.05]
WARM = {}  # (T, kind) -> state
ok_record, ok_partner, ok_control = True, True, True
for T in TEMPS:
    for kind in "ABC":
        WARM[(T, kind)] = universe(kind, l1, 1.0, 136, 0.4, T=T)
    A, B, C = (WARM[(T, kind)] for kind in "ABC")
    F = {kind: WARM[(T, kind)]["E_KS"] - T * WARM[(T, kind)]["entropy"]
         for kind in "ABC"}  # free energy F = E - T S
    row = THERMO[f"N136_lamp1_a10_T{round(1000 * T)}"]
```

The record's table of thermal states is read. For the three temperatures $T = 0.01, 0.02, 0.05$ of the record, A, B and C are solved at $N = 136$, $\lambda_1$, $a_{4,0} = 1$, with the margin $0.4$ and Mermin occupations: nine runs. For each the free energy $F = E_{KS} - TS_{\rm ent}$ is formed (Exercise 19.7 shows that this equals $\Omega + \mu N$ of Section 19.4), and the record's row is found by its name, which ends in T10, T20 or T50 (a thousand times the temperature).

```python
    ok_record &= (close(A["mu_or_fermi_level"], float(row["mu"]))
                  and close(A["E_KS"], float(row["E"]))
                  and close(A["entropy"], float(row["entropy"]))
                  and close(F["A"], float(row["F"])))
    ok_partner &= (close(A["mu_or_fermi_level"], B["mu_or_fermi_level"])
                   and close(A["entropy"], B["entropy"]) and close(F["A"], F["B"])
                   and level_difference(A, B) < TOL)
    ok_control &= 2.5 < F["A"] - F["C"] < 3.5
    mu_A, mu_B, mu_C = (s["mu_or_fermi_level"] for s in (A, B, C))
    F_A, F_B, F_C = (F[kind] for kind in "ABC")
    say(f"T = {T:.2f}: mu A {mu_A:.12f} B {mu_B:.12f} C {mu_C:.6f}; "
        f"F A {F_A:.9f} B {F_B:.9f} C {F_C:.5f}")
```

A must reproduce the record's chemical potential, energy, entropy and free energy; B must have the chemical potential, entropy, free energy and levels (with their occupations) of A; and the control's free energy must lie between $2.5$ and $3.5$ below that of A (`2.5 < x < 3.5` tests both bounds). Out [25] shows, for example at $T = 0.05$: $\mu = 0.295073925379$ and $F = 27.091045285$ for both A and B, and $\mu = 0.289068$, $F = 24.21400$ for the control.

```python
check(ok_record, "A reproduces mu, E, entropy and F of the three thermal states",
      record="Revision/kohn_sham/results/thermo/thermodynamics.csv, "
             "N136_lamp1_a10_T10, T20, T50")
check(ok_partner, "B has the occupations, mu, entropy and F of A at every T",
      record="Revision/pairing/kohn_sham/t3-theory.json, statement S4")
check(ok_control, "the control C has a free energy 2.5 to 3.5 below A at every T")
```

Three checks (Out [25]).

**In [26], the thermal states (Figure 19a.10).**

```python
fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
T = 0.05
DOTS = {"A": dict(marker="o", ms=7, ls="none", mfc="none", mew=1.6),
        "B": dict(marker="x", ms=5, ls="none", mew=1.4),
        "C": dict(marker="^", ms=4, ls="none")}
for kind in "ABC":
    lv = WARM[(T, kind)]["levels"]
    left.plot([v[4] for v in lv], [v[6] for v in lv], color=COLOUR[kind],
              label=NAME[kind], **DOTS[kind])
mu = WARM[(T, "A")]["mu_or_fermi_level"]
grid = np.linspace(-0.3, 1.0, 400)
left.plot(grid, 1.0 / (1.0 + np.exp((grid - mu) / T)), color="0.4", lw=1.0,
          label="Fermi function of A")
```

On the left, at $T = 0.05$, every level is a marker at the height of its occupation: A as open rings (`mfc="none"`: no fill; `mew`: the width of the marker's edge), B as crosses, C as small triangles, without connecting lines (`ls="none"`). The grey curve is the Fermi function $1/(1 + e^{(\varepsilon - \mu)/T})$ of A on 400 points.

```python
left.set_xlim(-0.3, 1.0)
left.set_xlabel("level $\\varepsilon$ (units of $|m|$)")
left.set_ylabel("occupation $f$")
left.set_title(f"$T = {T}$", fontsize=10)
left.legend(fontsize=6, loc="lower left")
for kind in "ABC":
    right.plot(TEMPS, [WARM[(t, kind)]["E_KS"] - t * WARM[(t, kind)]["entropy"]
                       for t in TEMPS], color=COLOUR[kind], label=NAME[kind],
               **MARK[kind])
right.set_xlabel("temperature $T$ (units of $|m|$)")
right.set_ylabel("free energy $F = E - TS_{ent}$ (units of $|m|$)")
fig.suptitle("$N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$", fontsize=10)
fig.tight_layout()
```

The left axes show the levels between $-0.3$ and $1.0$. On the right, the free energy of the three universes against the temperature.

```python
save_figure(fig, "thermal_states",
            "Thermal Kohn-Sham states for $N = 136$, $\\lambda = \\lambda_1$, "
            "$a_{4,0} = 1$. Left: the occupation $f$ of every level against its "
            "energy (units of $|m|$) at $T = 0.05$ for A (blue rings), B (orange "
            "crosses) and C (aqua triangles); the grey curve is the Fermi function "
            "of A. Every cross of B sits in a ring of A. Right: the free energy "
            "$F = E - TS_{ent}$ against the temperature $T$ (units of $|m|$); A and "
            "B coincide, the control C lies $2.5$ to $3.5$ lower.")
```

`save_figure` saves Figure 19a.10. What the student should see: on the left the rings of A on the grey Fermi curve, falling from 1 to 0 around $\mu = 0.295$, each with an orange cross inside it, and the control's triangles on its own, shifted curve; on the right the free energy falling with the temperature, A and B on top of each other (32.24, 31.59, 27.09) and the control about 3 lower.

**In [27], the same runs in the record's demonstration of T3.** The record's numerical demonstration (Section 19.10) solved the members plus, image and control for all 210 states; this cell checks that the runs of this notebook are the record's runs where the two overlap.

```python
DEMO = "Revision/pairing/kohn_sham/reports/t3-rust-demo.json"
DEMO_TABLE = "Revision/pairing/kohn_sham/numerics/results/t3-rust-states.csv"
demo = json.loads(repository_file(DEMO).read_text(encoding="utf-8"))
verdict = {c["name"]: c["verdict"] for c in demo["checks"]}
detail = {c["name"]: c["detail"] for c in demo["checks"]}
passed = sum(v == "PASS" for v in verdict.values())
say(f"record: {demo['states']} states, {passed} of {len(verdict)} checks pass")
```

The two names are the report of the demonstration and its table. `json.loads` reads the report into a dictionary; its list `checks` holds one dictionary per check, with the keys `name`, `verdict` and `detail`. The two dictionary comprehensions make the look-ups "name to verdict" and "name to detail text". `passed` counts the verdicts equal to PASS (a comparison is `True` or `False`, and `sum` counts each `True` as 1). The line prints the number of states of the record (its key `states`) and the count: "record: 210 states, 7 of 7 checks pass" (Out [27]).

```python
for name in ("t3_equal_ground_states", "t3_equal_thermal_states"):
    worst = re.search(r"worst deviation (\S+),", detail[name]).group(1)
    say(f"record, {name}: worst deviation {worst}")
DEMO_ROWS = read_rows(DEMO_TABLE)
PAIRS, GROUP = {}, {}  # state id -> [A, B, C]; state id -> group of runs
```

The detail text of each of the two equality checks contains the words "worst deviation" followed by a number and a comma; the regular expression finds them, and `group(1)` is the part matched by `(\S+)`, the number (`\S+` means one or more characters that are not spaces). Out [27] prints the record's own worst deviations, $2.179\times10^{-13}$ for the 75 ground states and $3.877\times10^{-12}$ for the 135 thermal states. `read_rows` (In [9]) reads the table into a dictionary from the state id, such as N136_lamp1_a10, to its row. `PAIRS` will hold, for every state of the record that this notebook solved, the three states A, B and C of this notebook, and `GROUP` the group of runs the state belongs to.

```python
def add(state_id, group, states):
    """Store the states A, B, C of one state of the record, once."""
    if state_id not in PAIRS:
        PAIRS[state_id], GROUP[state_id] = states, group
```

`add` stores a state only the first time its id appears. This matters because some runs were reused: the state N136_lamp1_a10 is in `SELF`, in `HIST` (the slice $a_{4,0} = 1$) and in `SCAN` (the coupling $+\lambda_1$), and must be counted once.

```python
for N in (8, 136):
    add(f"N{N}_lamp1_a10", "ground", [SELF[(N, kind)] for kind in "ABC"])
add("N8_lam0_a10", "ground", [FREE8[kind] for kind in "ABC"])
for tag, lam, margin in COUPLINGS:
    add(f"N136_{tag}_a10", "ground", [SCAN[(tag, kind)] for kind in "ABC"])
for N in (136, 688):
    for a4 in SLICES:
        add(f"N{N}_lamp1_a{round(10 * a4):02d}", "history",
            [HIST[(N, kind, a4)] for kind in "ABC"])
for T in TEMPS:
    add(f"N136_lamp1_a10_T{round(1000 * T)}", "thermal",
        [WARM[(T, kind)] for kind in "ABC"])
```

The ids are built in the naming scheme of the record (Section 19.1): `round(10 * a4):02d` writes ten times the slice with two digits (0.5 becomes 05), and `round(1000 * T)` writes the temperature in thousandths (0.05 becomes 50). The group "ground" receives the states at the slice $a_{4,0} = 1$ of In [7] (two), In [17] (one, without interaction) and In [23] (four more couplings; $+\lambda_1$ is already stored): 7 states. The group "history" receives the states of In [20] not yet stored: four slices for $N = 136$ and five for $N = 688$, 9 states. The group "thermal" receives the 3 states of In [25]. Together 19 states.

```python
def relative(a, b):
    """|a - b| relative to max(|a|, 1), the measure of close()."""
    return abs(a - b) / max(abs(a), 1.0)
```

`relative` measures a difference in the same way as `close` of In [8]: relative to the size of the first number, but never relative to a number smaller than 1.

```python
worst_A, worst_B, worst_C = 0.0, 0.0, 0.0
for state_id, (A, B, C) in PAIRS.items():
    row = DEMO_ROWS[state_id]  # the record's row of this state
    worst_A = max(worst_A, relative(A["E_KS"], float(row["E_KS_plus"])))
    image = [(B["E_KS"], row["E_KS_image"]), (B["mu_or_fermi_level"],
             row["mu_image"]), (B["entropy"], row["entropy_image"])]
    image += [(B["emtIntegrals_2Vol7_int_e6Hy"][c], row[f"int_{c}_image"])
              for c in ("rho", "p3", "p_t", "p8")]
    worst_B = max([worst_B] + [relative(x, float(r)) for x, r in image])
    control = float(row["E_KS_control_untransformed_tip"])
    worst_C = max(worst_C, relative(C["E_KS"], control))
```

For every one of the 19 states the loop takes the record's row and compares: the energy of A with the record's plus member (column `E_KS_plus`); seven numbers of B with the record's image member (the energy, the chemical potential or Fermi level, the entropy, which is 0 in a ground state, and the four energy-momentum integrals, columns `int_rho_image` and so on); and the energy of C with the record's control (column `E_KS_control_untransformed_tip`). The table stores numbers as text, so `float` converts them. `max([worst_B] + [...])` takes the largest of the old worst value and the seven new differences.

```python
worst_D = max(relative(SCAN[(tag, "D")]["E_KS"],
                       float(DEMO_ROWS[f"N136_{MIRROR[tag]}_a10"]["E_KS_image"]))
              for tag, lam, margin in COUPLINGS)
say(f"{len(PAIRS)} states of the record solved here; largest relative differences "
    f"from the record: A {worst_A:.1e}, B {worst_B:.1e}, C {worst_C:.1e}, "
    f"D {worst_D:.1e}")
```

D at the coupling $\lambda$ is the universe $(-m, -\lambda)$ with the tip angle $\pi$, which is the image member of the record's state at the coupling $-\lambda$; `MIRROR` (In [23]) gives the tag of $-\lambda$. Out [27] prints the four largest differences: A $4.0\times10^{-14}$, B $2.8\times10^{-13}$, C $7.0\times10^{-14}$, D $0$. The record's runs and these runs were made by the same program on the same computer, so most numbers agree to every digit and the others to the rounding of the last digits.

```python
def t3_deviation(A, B):
    """Largest deviation of B from A under T3 (levels, E_KS, mu, entropy, EMT
    integrals, profiles with the odd columns reversed)."""
    return max(level_difference(A, B), relative(A["E_KS"], B["E_KS"]),
               relative(A["mu_or_fermi_level"], B["mu_or_fermi_level"]),
               relative(A["entropy"], B["entropy"]), integral_difference(A, B),
               profile_mismatch(A, B))
```

`t3_deviation` combines every comparison of A and B of this notebook into one number: the sorted levels with degeneracies and occupations (`level_difference`, In [7]), the energy, the chemical potential, the entropy, the four energy-momentum integrals (`integral_difference`, In [7]) and the ten profile columns with $S$, $Q$, $M_{\rm eff}$ reversed (`profile_mismatch`, In [13]).

```python
largest = {}
for group in ("ground", "history", "thermal"):
    ids = [state_id for state_id in PAIRS if GROUP[state_id] == group]
    largest[group] = max(t3_deviation(*PAIRS[state_id][:2]) for state_id in ids)
    say(f"{group}: {len(ids)} pairs A, B; largest T3 deviation "
        f"{largest[group]:.1e}")
```

For each group, `ids` lists its states; `PAIRS[state_id][:2]` is the list `[A, B]` of a state, and the star `*` hands its two entries to `t3_deviation` as its two arguments. Out [27]: ground 7 pairs, largest deviation $9.9\times10^{-14}$; history 9 pairs, $1.0\times10^{-13}$; thermal 3 pairs, $8.1\times10^{-13}$ (the entropy of the state N136_lamp1_a10_T10 at $T = 0.01$, a number near 42 that the solver adds up level by level from the occupations; the record's table `Revision/pairing/kohn_sham/numerics/results/t3-rust-states.csv` shows the same deviation, $8.117\times10^{-13}$, for this state in its column t3_scalars_dev). These are the rounding of the computer, and, as Section 19.17 showed, at the rounding level by construction, because the shooting is covariant under the map.

```python
check(passed == len(verdict) == 7 and demo["states"] == 210,
      "the record's T3 demonstration passes 7 of 7 checks in 210 states",
      record=DEMO)
check(len(PAIRS) == 19 and worst_A < TOL and worst_B < TOL,
      "A and B equal the record's plus and image members in 19 states",
      record=f"{DEMO}, checks t3_equal_ground_states, t3_equal_thermal_states")
check(worst_C < TOL, "C equals the record's control with the untransformed tip",
      record=f"{DEMO}, check negative_control_untransformed_tip")
check(worst_D < TOL, "D at lambda equals the record's image member at -lambda",
      record=f"{DEMO}, check negative_control_lambda_sign")
check(max(largest.values()) < TOL,
      "B equals A under T3 in all 19 pairs (ground, history, thermal)")
```

Five checks, each with the tolerance $10^{-9}$ of the record: the record's demonstration passes completely; A and B are the record's plus and image members in all 19 states; C is the record's control; D is the record's image at the opposite coupling; and B equals A under T3 in every pair of this notebook. The PASS lines name the report and the check of the record that each comparison reproduces (Out [27]).

**In [28], the last check.**

```python
runs = len({id(state) for state in [*SELF.values(), *FREE8.values(), *HIST.values(),
                                    *SCAN.values(), *WARM.values()]})
report("runs of the Rust solver in this notebook", runs)
names = ["level_ladder", "level_differences", "density_profiles",
         "mass_and_potential", "emt_profiles", "zero_modes_n8", "history_energy",
         "history_agreement", "coupling_scan", "thermal_states"]
paths = [output_file(f"{FIGURE_FOLDER}/19a_{k}_{name}.png")
         for k, name in enumerate(names, 1)]
check(runs == 62 and all(path.is_file() for path in paths),
      "every figure file of this notebook exists")
all_checks_passed()
```

`id(state)` is a number that identifies one object in the computer's memory; a state that was reused (stored under two keys) has one `id`, so the set of the ids of all stored states counts every run once: $6 + 3 + 27 + 17 + 9 = 62$. The check requires 62 runs and all ten figure files (`enumerate(names, 1)` counts from 1), and the last line is ALL 37 CHECKS PASSED (notebook 19a) (Out [28]). Of the 62 runs, 19 states compare A with its partner B (In [27]); the other runs are the controls C and D.

### 19.22 What T3 says about pairs of universes, and what it does not

**What is proved.** For the fermion field dirac16complex in the author's primordial universe, in the Kohn-Sham model of the Revision record: to every self-consistent instantaneous Kohn-Sham state of the universe of mass $+M$ (bare mass $m$, coupling $\lambda$, tip angle $\theta$) the chirality $\Gamma$, acting on the blocks as $\sigma_2$, assigns a self-consistent Kohn-Sham state of the universe of mass $-M$ with the same coupling and the tip angle $\pi - \theta$, at the same slice of the deflating history, with the same levels, occupations, chemical potential, entropy, Kohn-Sham energy, grand potential, free energy and energy-momentum profiles, and the opposite scalar density; and conversely. Inside the ASSUMED Z2 orbifold, the mirror copy of every state carries $(-m, +\lambda)$. With the completion of the record (statement S6, Section 19.10), at the level of the 16-component expectation rule, every component of the energy-momentum tensor and of the current $J^a$ is the same in the two members, while $S$ and $Q$ change sign; and the filling convention of the $+M$ member, carried by the map, is the filling convention of the $-M$ member. Status: PROVED (Sections 19.5 to 19.11; `wolfram-t3.json` 10 of 10, `python-t3.json` 13 of 13; the completion `t3-completion.json` with `wolfram-t3-completion.json` 3 of 3 and `python-t3-completion.json` 7 of 7).

**What is demonstrated numerically** (COMPUTED; demonstrations, not proofs). The record's Rust demonstration (`t3-rust-demo.json`) finds the $-M$ partner equal to the $+M$ state in all 75 ground and 135 Mermin states of the canonical matrix, to $2.179\times10^{-13}$ (ground) and $3.877\times10^{-12}$ (thermal); this agreement is at the rounding level by construction, because the solver's shooting is covariant under the map (Section 19.17), so it tests the solver's handling of the two members, not the discretisation. The record's reference demonstration (`t3-reference-demo.json`) is the discretisation-independent test: on one grid the two members differ by up to $2.23\times10^{-4}$, after Richardson extrapolation by $2.043\times10^{-14}$ (ground) and $3.038\times10^{-14}$ (thermal), in 18 states; and the $-M$ universes of the two solvers agree to $1.255\times10^{-11}$. Notebook 19a compares A and B in 19 states (7 ground states at $a_{4,0} = 1$, 9 more states of the history, 3 thermal states; 62 runs with the controls), with the largest deviations $9.9\times10^{-14}$, $1.0\times10^{-13}$ and $8.1\times10^{-13}$ (Out [27]), and finds every run equal to the record's demonstration. The controls do differ: the untransformed tip changes the density profile by at least $4.750$ times its maximum, and the T1 parameters $(-m, -\lambda)$ differ by at least $1.21\times10^{-2}$.

**What is not established** (the list of the theorem record `t3-theory.json`, entry not_established, in words):

- **No creation.** T3 maps self-consistent Kohn-Sham states onto self-consistent Kohn-Sham states of a second parameter set. It contains no process in which a universe, or a pair of universes, comes into being, no rate, no probability and no amplitude, and it does not force the partner to exist: a universe of mass $+M$ alone is an equally valid solution. The statement "the big bang creates universes in pairs" is the author's HYPOTHESIS; T3 is compatible with it, in the sense that a partner state with equal energy is always available, but compatibility is not a proof.
- **Instantaneous states only.** T3 holds slice by slice for the instantaneous (adiabatic) states along the PRESCRIBED BACKGROUND history $a_4 = AHx_4$; the time-dependent Kohn-Sham problem along the deflating history is OPEN.
- **An assumed brane and a chosen tip.** The Z2 mirror at the brane is ASSUMED; the tip condition is a choice of the model, and T3 needs its transformed form $\pi - \theta$ (Section 19.12 shows what fails without it).
- **Mean field only.** Hartree plus the exchange of the uniform gas, no correlation, quasi-free states, and the filling convention whose justification is OPEN.
- **Not two independently quantised universes.** The pairing is between two Kohn-Sham problems, $(m, \lambda)$ and $(-m, +\lambda)$; it is not the T1 pairing $(m, \lambda) \to (-m, -\lambda)$, and it says nothing about two separately quantised universes (that question is the quantum reading Q of Chapter 18).
- **No back-reaction.** The Kohn-Sham energy-momentum tensor is not an admissible source of the $a_4$ field equations: it depends on $x_8$, and $p_3 + p_t \ne 2p_8$ (`Revision/field_equations_a4/reports/ks-source-conditions.json`, checks ks_profiles_depend_on_x8 and ks_profiles_violate_algebraic_condition). So T3 says nothing about how the geometry of either universe would respond.
- **Numbers only where they were computed.** The numerical demonstrations show the equalities only on the states they solved, to their stated tolerances. Control states for which a solver found no self-consistent solution (14 states in the Rust demonstration, 3 in the reference demonstration, all with $\lambda < 0$) are reported as such, not as a proof that no such state exists (the completion record `t3-completion.json`, entry not_established).

**Matter and antimatter.** T3 does not touch the matter-antimatter question. The partner has the same charge density $n(y)$ and the same particle number $N$, not the opposite ones, and by S6 every component of its current $J^a$ is the same, not the opposite; it also has the same, not the opposite, energy: a T3 pair has twice the charge and twice the energy of one member; nothing cancels. (The pair-level statement with zero total charge belongs to T1 and the classical bilinears, Chapter 18.) Nothing in the Kohn-Sham model contains baryons, a violation of baryon number, a violation of CP, or a departure from equilibrium, the ingredients that an explanation of the observed excess of matter over antimatter would need. Chapter 21 teaches the observations and these conditions from zero and states what the theory of this book does and does not say about them; Chapter 20 collects what the pairing theorems T1, T2, Q and T3 together prove about pairs of universes and what they do not.

### 19.23 What we proved, what we computed, what we assumed

- PROVED, line by line in this chapter and in the records `Revision/pairing/kohn_sham/reports/wolfram-t3.json` (10 of 10 checks) and `Revision/pairing/kohn_sham/reports/python-t3.json` (13 of 13), theorem record `Revision/pairing/kohn_sham/t3-theory.json`: the chirality $\Gamma$ maps every block $(j, s_2, s_3)$ onto $(-j, s_2, s_3)$ and acts there as $s_2\sigma_2$ (Section 19.5; also blocks_relation_to_Gamma of `ks-theory-python.json`); $\sigma_2h_j(M, v)\sigma_2 = h_{-j}(-M, v)$ and $\sigma_2N_j(M)\sigma_2 = N_{-j}(-M)$ (Section 19.6); the tip angle goes to $\pi - \theta$, the brane parities are exchanged, norm and current are kept (Section 19.7); $n$, $t$ are even and $S$, $Q$ odd, and the mean field closes exactly for $(-m, +\lambda)$, not for $(-m, -\lambda)$ (Section 19.8); every self-consistent state has its partner with equal levels, occupations, energies and energy-momentum profiles (Section 19.9): theorem T3 (Section 19.10). Also PROVED, by the completion `Revision/pairing/kohn_sham/t3-completion.json` (`reports/wolfram-t3-completion.json` 3 of 3, `reports/python-t3-completion.json` 7 of 7): the mean-field coefficients read from `ks-theory.json` in both engines, with $M_{\rm eff} - m = \partial e_{\rm int}/\partial S$ and $v_v = \partial e_{\rm int}/\partial n$ (Section 19.8); the filling convention carried onto the partner (Section 19.9); statement S6, $\rho' = -\Gamma\rho\Gamma$, so that every component of the energy-momentum tensor and of the current is unchanged and $S$, $Q$ change sign (Section 19.10). Also PROVED: $\Gamma B\Gamma = -B$, the reason why T3 differs from T1 (Sections 19.5 and 19.11; check Q.image_krein_metric of `Revision/pairing/reports/python-pairing.json`); the mirror copy inside the assumed orbifold carries $(-m, +\lambda)$ (Section 19.11); the exact zero-momentum spectra, the zero modes, the control's level in the gap $\varepsilon_b = M/\cosh(qL)$ with $\tanh(qL) = q/M$, and the slopes $c$ and $c_{\rm ctrl}$ (Section 19.12; checks T3_exact_k0_spectra, bc_exact_k0_spectra, brane_band_slope).
- COMPUTED: Notebook 19b (19 checks) reproduces the proof checks with sympy, the analytic levels of `Revision/kohn_sham/results/spectrum/free-k0-analytic.csv` to $8.9\times10^{-16}$, the same levels by shooting to $5.9\times10^{-12}$, and the slope $c = 1.9051482536$ of the record; $c_{\rm ctrl} = 13.4219751976$. The record's demonstrations (Section 19.10): Rust, `Revision/pairing/kohn_sham/reports/t3-rust-demo.json` (210 states, 7 of 7), image equal to plus to $2.179\times10^{-13}$ (ground) and $3.877\times10^{-12}$ (thermal), at the rounding level by construction (the covariance of the shooting, Section 19.17); reference, `Revision/pairing/kohn_sham/reports/t3-reference-demo.json` (18 states, 7 of 7), equal to $2.043\times10^{-14}$ and $3.038\times10^{-14}$ after Richardson extrapolation against $2.23\times10^{-4}$ on a single grid, the discretisation-independent test; controls off by at least $4.750$ (untransformed tip) and $1.21\times10^{-2}$ (T1 parameters). Notebook 19a (37 checks, 62 runs of the Rust solver, 19 states with A and B) reproduces the solver's T3 self-test of `Revision/kohn_sham/reports/ks-rust-solver.json` (check t3_block_map_solver_selftest), the committed canonical states and, in its 19 states, the record's demonstration `t3-rust-demo.json`; it finds the partner B equal to A to $9.9\times10^{-14}$ (ground states), $1.0\times10^{-13}$ (history) and $8.1\times10^{-13}$ (thermal states) and $4.0\times10^{-14}$ relative in the energy along the whole history; the control C off by $0.8$ to $9.6$ percent along the history and by $1.15$ to $3.43$ across the couplings; the wrong partner D equal to A at the opposite coupling; the control's Kohn-Sham gap equal to $\varepsilon_b = 0.100851121375$ to twelve digits.
- ASSUMED: the good sector; the Z2 mirror at the brane; the cut at $L = 3$ with a chosen tip condition (T3 needs the transformed one); the mean field of Hartree plus uniform-gas exchange without correlation. CONVENTION: the filling of the particle levels.
- PRESCRIBED BACKGROUND: the history $a_4 = AHx_4$, $A = 1$; the Kohn-Sham states are not an admissible source of the $a_4$ equations.
- OPEN: the time-dependent Kohn-Sham problem; the justification of the filling convention.
- HYPOTHESIS: that universes are created in pairs. Not proved here, and not provable from these equations, which contain no creation process.

### 19.24 Exercises

**Exercise 19.1 (the conjugation rules).** Multiply out the $2 \times 2$ matrices to show $\sigma_2\sigma_1\sigma_2 = -\sigma_1$ and $\sigma_2\sigma_3\sigma_2 = -\sigma_3$, without using the anticommutation rule.

*Answer.* First $\sigma_2\sigma_1 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}$ (row times column: the first row $(0, -i)$ times the first column $(0, 1)$ gives $-i$, times the second column $(1, 0)$ gives 0; the second row $(i, 0)$ gives 0 and $i$). Then $(\sigma_2\sigma_1)\sigma_2 = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} 0 & (-i)(-i) \\ i\cdot i & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix} = -\sigma_1$. Likewise $\sigma_2\sigma_3 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}$ and $(\sigma_2\sigma_3)\sigma_2 = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} i\cdot i & 0 \\ 0 & i(-i) \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} = -\sigma_3$.

**Exercise 19.2 (the zero modes in the real form).** The zero mode of A is $(a, b) = (e^{My}, 0)$ with $j = +1$, mass $M$, $k = 0$, $v = 0$, $\varepsilon = 0$. Write down its image under $(a, b, j, M) \to (b, a, -j, -M)$ and verify directly that the image solves the real form of B and obeys B's boundary conditions (odd parity at the brane, tip angle $\pi$).

*Answer.* The image is $(a, b) = (0, e^{My})$ with $j = -1$ and the mass $-M$. The real form with $k = 0$, $v = 0$, $\varepsilon = 0$ is $a' = (-M)a - 0\cdot b = -Ma$ and $b' = 0\cdot a - (-M)b = Mb$. For $a = 0$: $a' = 0 = -M\cdot0$; for $b = e^{My}$: $b' = Me^{My} = Mb$. Both hold. The odd brane condition is $a(0) = 0$: true, since $a = 0$ everywhere. The tip angle $\pi$ demands $a(-L) = 0$: true. So the image is the zero mode of B, largest at the brane, as Section 19.12 found.

**Exercise 19.3 (a tip that needs no transformation).** For which tip angles $\theta$ is the transformed condition, with $\pi - \theta$, the same condition as the original? What does the condition say in the real form, and why is it unchanged by $(a, b) \to (b, a)$?

*Answer.* The tip matrix $Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2$ repeats with the period $2\pi$, so the two conditions agree when $\pi - \theta = \theta$ up to a multiple of $2\pi$: $\theta = \pi/2$ or $\theta = -\pi/2$. For $\theta = \pi/2$, $Q = \sigma_2$, and $(1 - \sigma_2)\chi = 0$ reads $\chi_1 + i\chi_2 = 0$ in the first row (and $-i\chi_1 + \chi_2 = 0$ in the second, the same equation times $-i$): $\chi_2 = i\chi_1$. With $\chi = (a, ib)$ this is $ib = ia$, that is $b(-L) = a(-L)$, which is unchanged when $a$ and $b$ are exchanged. For $\theta = -\pi/2$ the condition is $b(-L) = -a(-L)$, also unchanged. With such a tip the "control" C would be the partner B; the canonical tip $\theta = 0$ is not of this kind.

**Exercise 19.4 (every tip condition kills the current).** Let $(1 - Q(\theta))\phi = 0$ and $(1 - Q(\theta))\chi = 0$ at $y = -L$. Show that $\phi^\dagger\sigma_1\chi = 0$ there, using only $Q^\dagger = Q$ and $\sigma_1Q = -Q\sigma_1$; prove these two facts first.

*Answer.* $Q^\dagger = \cos\theta\,\sigma_3^\dagger + \sin\theta\,\sigma_2^\dagger = Q$, because the Pauli matrices are Hermitian and $\cos\theta$, $\sin\theta$ are real. $\sigma_1Q = \cos\theta\,\sigma_1\sigma_3 + \sin\theta\,\sigma_1\sigma_2 = -\cos\theta\,\sigma_3\sigma_1 - \sin\theta\,\sigma_2\sigma_1 = -Q\sigma_1$, because $\sigma_1$ anticommutes with $\sigma_3$ and with $\sigma_2$. The conditions say $Q\chi = \chi$ and $Q\phi = \phi$. Then, line by line: $\phi^\dagger\sigma_1\chi = \phi^\dagger\sigma_1Q\chi$ (insert $\chi = Q\chi$) $= -\phi^\dagger Q\sigma_1\chi$ (anticommute) $= -(Q^\dagger\phi)^\dagger\sigma_1\chi$ (since $\phi^\dagger Q = (Q^\dagger\phi)^\dagger$) $= -(Q\phi)^\dagger\sigma_1\chi = -\phi^\dagger\sigma_1\chi$. A number equal to its own negative is 0. So the boundary term of Section 19.3 vanishes at the tip for every $\theta$.

**Exercise 19.5 (how wrong is the wrong partner?).** In the record's canonical state N136_lamp1_a10 ($\lambda_1 = 0.0009298$) the scalar density at $y = -2.4$ is $S = -37$ (the record's profile file `Revision/kohn_sham/results/ground/profiles/N136_lamp1_a10.csv`, rounded). How far is the mass that the wrong partner $(-m, -\lambda)$ gives to the image density from the mass $-M_{\rm eff}$ that the image needs at that point?

*Answer.* By Section 19.8 the wrong partner gives $-M_{\rm eff} + \frac{15}{8}\lambda S$. The mismatch is $\frac{15}{8}\lambda S = 1.875 \times 0.0009298 \times (-37) = -0.0645$ in units of $|m|$. The right partner gives exactly $-M_{\rm eff}$; here $M_{\rm eff} = 1 + \frac{15}{16}\lambda_1 S = 1 - 0.0323 = 0.968$, close to the value $0.9677$ of the profile file. So the wrong partner's mass is off by twice the mean-field shift $\frac{15}{16}\lambda S = -0.0323$, which is why Notebook 19a finds D at $+\lambda$ equal to A at $-\lambda$ and different from A at $+\lambda$ (In [23]).

**Exercise 19.6 (the two slopes for M = H).** Show that for $M = H$ and $Y = e^{HL}$ the slopes of Section 19.12 are $c = 2Y/(Y + 1)$ and $c_{\rm ctrl} = \frac23(Y^2 + Y + 1)/(Y + 1)$, that $c_{\rm ctrl} - c = \frac23(Y - 1)^2/(Y + 1)$, and evaluate the difference for $L = 3$.

*Answer.* With $M = H$, $2M - H = H$ and $2M/(2M - H) = 2$: $c = 2(1 - e^{-HL})/(1 - e^{-2HL}) = 2(1 - Y^{-1})/(1 - Y^{-2})$. Multiply the numerator and the denominator by $Y^2$: $c = 2(Y^2 - Y)/(Y^2 - 1) = 2Y(Y - 1)/\big((Y - 1)(Y + 1)\big) = 2Y/(Y + 1)$. With $2M + H = 3H$: $c_{\rm ctrl} = \frac23(e^{3HL} - 1)/(e^{2HL} - 1) = \frac23(Y^3 - 1)/(Y^2 - 1) = \frac23(Y - 1)(Y^2 + Y + 1)/\big((Y - 1)(Y + 1)\big) = \frac23(Y^2 + Y + 1)/(Y + 1)$, using $Y^3 - 1 = (Y - 1)(Y^2 + Y + 1)$. The difference over the common denominator: $\big[\frac23(Y^2 + Y + 1) - 2Y\big]/(Y + 1) = \frac23(Y^2 - 2Y + 1)/(Y + 1) = \frac23(Y - 1)^2/(Y + 1)$, positive for every $L > 0$: the control's band is always steeper. For $L = 3$, $Y = e^3 = 20.0855$: $\frac23 \times 19.0855^2/21.0855 = \frac23 \times 364.26/21.0855 = 11.517$, the difference $13.4220 - 1.9051$ of Notebook 19b.

**Exercise 19.7 (the free energy).** With the Fermi occupations $f = 1/(1 + e^x)$, $x = (\varepsilon - \mu)/T$, show that $F = \Omega + \mu N$ equals $E_{KS} - TS_{\rm ent}$, with the definitions of Section 19.4.

*Answer.* Three facts about one level, line by line. (1) $1 - f = e^x/(1 + e^x) = 1/(1 + e^{-x})$, so $\ln(1 + e^{-x}) = -\ln(1 - f)$. (2) $\ln f = -\ln(1 + e^x) = -x - \ln(1 + e^{-x}) = -x + \ln(1 - f)$, using $1 + e^x = e^x(1 + e^{-x})$ and fact (1). (3) Hence $f\ln f + (1 - f)\ln(1 - f) = -xf + f\ln(1 - f) + (1 - f)\ln(1 - f) = -xf + \ln(1 - f)$. Summed with the degeneracies: $TS_{\rm ent} = -T\sum g[-xf + \ln(1 - f)] = \sum g f(\varepsilon - \mu) - T\sum g\ln(1 - f) = \sum gf\varepsilon - \mu N + T\sum g\ln(1 + e^{-x})$, using $Tx = \varepsilon - \mu$, $\sum gf = N$ and fact (1). Write $I = 2\,\mathrm{Vol}_7\int e^{6Hy}e_{\rm int}\,dy$. Then $\Omega = -T\sum g\ln(1 + e^{-x}) - I = \big(\sum gf\varepsilon - \mu N - TS_{\rm ent}\big) - I = E_{KS} - TS_{\rm ent} - \mu N$, using the line before and $E_{KS} = \sum gf\varepsilon - I$. Adding $\mu N$ gives $F = E_{KS} - TS_{\rm ent}$. Notebook 19a computes $F$ in this form (In [25]).

**Exercise 19.8 (when does the control have a level in the gap?).** Take $M = 1$ and the tip at $L = \frac12$ instead of $L = 3$. Does the control's odd sector still have a level inside the gap?

*Answer.* The level in the gap is a root $q$ in $(0, M)$ of $u(q) = \tanh(qL) - q/M$ (Section 19.12). Now $u(0) = 0$ and $u'(0) = L - 1/M = -\frac12 < 0$. The function $\tanh$ is concave for $q > 0$, so $u$ is concave there, and a concave function that starts at 0 with a negative slope stays below the line $u'(0)q$, hence negative, for all $q > 0$: there is no root, and no level inside the gap. At the edge $\varepsilon = M$ ($p = 0$) the odd characteristic function of C is $\cosh 0 - M\cdot L = 1 - \frac12 \ne 0$, so there is no level at the edge either. The control has a level in the gap exactly when $L > 1/M$; the record's $L = 3$ is such a case.

**Exercise 19.9 (Krein signs of the eight blocks).** Using the block form $B = js_2$, list the Krein signs of the eight blocks and show that $\Gamma$, which moves $(j, s_2, s_3)$ to $(-j, s_2, s_3)$, reverses the Krein sign of every block. How many blocks have the Krein sign $+1$?

*Answer.* The products $js_2$ for $(j, s_2) = (1, 1), (1, -1), (-1, 1), (-1, -1)$ are $+1, -1, -1, +1$, each for $s_3 = \pm1$: the blocks $(1, 1, \pm1)$ and $(-1, -1, \pm1)$ have the Krein sign $+1$, the blocks $(1, -1, \pm1)$ and $(-1, 1, \pm1)$ have $-1$. Four blocks have $+1$ and four $-1$, eight components each way, in agreement with the eight eigenvalues $+1$ and eight $-1$ of $B$. The partner block of $(j, s_2, s_3)$ has the sign $(-j)s_2 = -js_2$: reversed, for every block. This is $\Gamma B\Gamma = -B$ written block by block (Section 19.5).
