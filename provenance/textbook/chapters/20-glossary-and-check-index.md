## 20. Glossary and index of verifier checks

This last chapter has two parts. The glossary (Sections 20.2 to 20.8) lists the technical terms of the book in alphabetical order, each with a short definition and the chapter in which the term is introduced; symbols and notation follow in their own section. The index of verifier checks (Sections 20.9 to 20.15) lists every machine check that the book names, with the committed report that contains it, its value there and the chapters that cite it. The chapter ends, like every chapter, with what it proves and assumes, exercises and answers.

### 20.1 How to use this chapter

**The glossary.** Each entry has the form "**term** (Chapter N)", followed by one or two sentences. The chapter is the one in which the term is first defined or first explained; where two chapters are named, the first gives a short definition and the second the full treatment, or the term has two uses. A term that returns later is not listed again under the later chapters. The definitions are short reminders, not replacements for the chapters: the full definition, the worked examples and the proofs are in the chapter named. Terms that consist of several words are sorted by their first word (for example "spin connection" under S), and a term that is usually abbreviated is listed under its abbreviation with a cross-reference ("BDF: see backward differentiation formula"). Upper and lower case, hyphens, mathematical symbols and accents are ignored in the ordering, and a term that begins with a digit is sorted as if the digit were written as a word ("3-space" under T). Where a term has a special meaning in this project that differs from its everyday meaning (for example "gate", "check", "good sector"), the entry gives the project's meaning.

**The index of checks.** A check is a named statement that a verifier has decided to be true or false and recorded in a report (Section 0.8). Section 20.9 explains how the index was made and verified.

### 20.2 Glossary: A to C

- **absolute tolerance, atol** (Chapter 10). The error that CVODE accepts in a component of the state whose size is near zero; together with the relative tolerance it sets the weight of each component in the error test.
- **action** (Chapter 5). The integral of the Lagrangian over time (for a particle) or of the Lagrangian density over spacetime (for a field); the equations of motion are the conditions under which it does not change to first order.
- **Adams methods** (Chapter 10). Linear multistep methods that integrate a polynomial through past values of the right-hand side; Adams–Bashforth is explicit, Adams–Moulton implicit. CVODE's Adams–Moulton family was used for EXP-2 to EXP-5.
- **adiabatic dressing** (Chapter 11). The small admixture of the other energy level that a slowly changing mode carries at every instant and that disappears when the change stops; it is not a created particle.
- **adiabatic theorem, adiabatic expansion** (Chapter 11). A state that starts in a level of a slowly changing Hamiltonian stays in that level; the expansion in the rate of change gives the created amplitude when the change is not slow.
- **adjoint** (Chapter 8). For an operator $O$, the operator $O^\dagger$ with $\langle f,Oh\rangle=\langle O^\dagger f,h\rangle$; for the standard inner product it is the conjugate transpose. See also Hermitian conjugate, Krein adjoint, Dirac adjoint.
- **algebra** (Chapter 3). A vector space with a bilinear product; it may have a unit and may be associative or commutative.
- **alternative** (Chapter 3). An algebra in which $x(xy)=(xx)y$ and $(yx)x=y(xx)$ for all $x,y$; the split octonions are alternative although not associative.
- **amplification factor** (Chapter 10). The number $R(z)$, $z=h\lambda$, by which a one-step method multiplies the solution of $y'=\lambda y$ in each step; its modulus decides stability.
- **Anderson mixing, Pulay mixing** (Chapter 12). A way to find the self-consistent density that combines several previous inputs and their residuals so as to make the residual smallest; the Rust Kohn–Sham solver uses it.
- **annihilate, annihilation operator** (Chapter 8). The operator $b$ (or $a_p$) that removes one fermion from a mode and gives zero on an empty mode; in particle physics a particle and its antiparticle also annihilate each other (Chapter 17).
- **anti-Hermitian** (Chapter 1). A square matrix with $A^\dagger=-A$; a real antisymmetric matrix is anti-Hermitian, and $i$ times an anti-Hermitian matrix is Hermitian.
- **anticommutation relations** (Chapter 12). The rules $\{a_p,a_q^\dagger\}=\delta_{pq}$ and $\{a_p,a_q\}=\{a_p^\dagger,a_q^\dagger\}=0$ of fermion creation and annihilation operators.
- **anticommutator** (Chapter 1). $\{A,B\}=AB+BA$; two matrices anticommute when it is zero.
- **antilinear** (Chapter 17). A map $A$ with $A(cv)=c^\ast A(v)$ for complex numbers $c$, such as complex conjugation; an antiunitary map is an antilinear map that preserves the modulus of inner products.
- **antiparticle** (Chapter 8). In the good-sector Fock space, a hole in the filled Dirac sea: it has positive energy and the opposite U(1) charge of a particle.
- **antisymmetric matrix** (Chapter 1). A square matrix with $A^T=-A$; its diagonal is zero.
- **associative** (Chapter 1). A product with $(AB)C=A(BC)$; matrix multiplication is associative, the product of the split octonions is not.
- **associator** (Chapter 3). $(xy)z-x(yz)$; it measures the failure of associativity, for example $(e_1e_2)e_4-e_1(e_2e_4)=2e_7$ for the split octonions.
- **ASSUMED** (Chapter 0). The status of a statement that is a starting point and not derived: a convention, a physical input or an approximation.
- **atol**: see absolute tolerance.
- **atomic units** (Chapter 12). Units in which $\hbar$, the electron mass and the electron charge are 1.
- **aufbau rule** (Chapter 12). Occupy the lowest available one-particle levels (German "building up").
- **average of a representation, $K_X$** (Chapter 3). The sum $\sum_A\gamma'_AX\gamma_A^{-1}$ over all 256 monomials; for a suitable matrix $X$ it gives a nonzero intertwiner between two sets of gamma matrices.
- **back-reaction** (Chapter 18). The response of the metric to the matter in it, computed self-consistently instead of keeping the gravitational field fixed; not computed anywhere in the repository.
- **backward differentiation formula, BDF** (Chapter 10). An implicit multistep method that differentiates a polynomial through the unknown and past values of the solution; stable for stiff problems. Used with Newton iteration for EXP-1.
- **bag condition** (Chapter 13). The boundary condition at the tip cutoff $y=-L$ of the Kohn–Sham problem, $\chi_2(-L)=0$, the member $\theta=0$ of a family $(1-Q(\theta))\chi(-L)=0$ that kills the current.
- **baryogenesis** (Chapter 17). Any process in the early universe that creates the observed excess of baryons over antibaryons; it needs the three conditions of Sakharov.
- **baryon, baryon number** (Chapter 17). Baryons are particles made of three quarks, such as protons and neutrons; the baryon number counts baryons minus antibaryons and is conserved by every process observed so far.
- **baryon-to-photon ratio** (Chapter 17). $\eta$, the number of baryons per photon of the cosmic microwave background, $\eta=6.12\times10^{-10}$ from the quoted measurements; the measured size of the matter–antimatter asymmetry, which this theory does not predict.
- **basis** (Chapter 1). A list of linearly independent vectors of which every vector is a combination; all bases of $\mathbb R^n$ have $n$ vectors.
- **BDF**: see backward differentiation formula.
- **Bianchi identities** (Chapter 4). The first, $R^\rho{}_{\sigma\mu\nu}+R^\rho{}_{\mu\nu\sigma}+R^\rho{}_{\nu\sigma\mu}=0$, and the second, the vanishing cyclic sum of covariant derivatives of the Riemann tensor; the contracted form gives $\nabla_\mu G^\mu{}_\nu=0$.
- **big-bang nucleosynthesis** (Chapter 17). The formation of the light nuclei in the first minutes of the universe; the observed abundances fix the baryon-to-photon ratio.
- **bilinear** (Chapters 3 and 5). Linear in each of two arguments; in field theory a bilinear is an expression $\Psi^\dagger M\Psi$ or $\bar\Psi M\Psi$ quadratic in the field.
- **binomial coefficient, binomial theorem** (Chapter 2). $\binom nk=\frac{n!}{k!(n-k)!}$, the number of subsets with $k$ elements of a set with $n$ elements (with the factorial $n!=1\cdot2\cdots n$, $0!=1$); the binomial theorem is $(x+y)^n=\sum_k\binom nkx^ky^{n-k}$.
- **bisection** (Chapter 10). A root finder that halves a bracketing interval in every step, keeping the half on which the function changes sign.
- **block matrix** (Chapter 1). A matrix cut into smaller matrices (blocks), multiplied block by block with the order of factors kept.
- **block type** (Chapter 13). The label $j=\pm1$ (the eigenvalue of $J=\gamma^0\gamma^1\gamma^4$) of the eight $2\times2$ blocks of the reduced Kohn–Sham equation; the two types carry opposite spectra of $h-v$.
- **Bogoliubov method, Bogoliubov coefficients** (Chapter 18; the computation is that of Chapter 11). Following each mode through a changing background and measuring the weight $|\beta_k|^2$ with which a mode that starts in its positive-energy level ends on the negative-energy level; the $\beta_k$ are the Bogoliubov coefficients. It is the only creation process computed in the repository, for particles in an expanding 3-space, not for universes.
- **bonding orbital** (Chapter 12). The lower orbital $\varphi_b=(\mathrm L+\mathrm R)/\sqrt2$ of the two-site model, the symmetric combination of the two site orbitals.
- **boost** (Chapter 2). A spin transformation $\exp(\theta S^{ab})$ with one space-like and one time-like index; it mixes the two directions hyperbolically. A boost pair of frame indices is such a pair (Chapter 4).
- **bosons** (Chapter 12). Particles whose many-body wave function is unchanged when two of them are exchanged.
- **bounce** (Chapter 11). The point of an EXP-3 run where the expansion rate reaches zero ($E^2=0$); it lies where the mean field is no longer valid.
- **bracket (of a root)** (Chapter 10). An interval at whose ends a function has opposite signs, so that it contains a zero; the Stage-4 solver first brackets each level and then refines it.
- **brane** (Chapter 9). A surface that carries energy and momentum of its own; here the surface $y=0$ where two mirror copies of the static primordial field are glued.
- **brane band** (Chapter 13). The Kohn–Sham levels $\varepsilon=\pm ck$ (to first order in the momentum $k$) into which the eight brane zero modes split at nonzero momentum; for $N=112$ and $N=1016$ the particles fill it up to a closed shell.
- **brane fraction** (Chapter 13). The fraction of the norm $\int\chi^\dagger\chi\,dy$ of an orbital, or of the particles of a state, within $|y|<1$, that is within the distance $1/H$ of the brane ($H=1$).
- **byte-identical** (Chapter 10). Two files are byte-identical when they are the same sequence of bytes; used as the test of reproducibility with a fixed program and engine.
- **canonical energy–momentum tensor** (Chapter 5). The Noether current of translations, $\Theta^\mu{}_\nu=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi_A)}\partial_\nu\phi_A-\delta^\mu{}_\nu\mathcal L$.
- **canonical Hartree–Fock equations** (Chapter 12). $\hat F\varphi_a=\varepsilon_a\varphi_a$, the Hartree–Fock equations after the occupied orbitals have been rotated so that the matrix of Lagrange multipliers is diagonal.
- **canonical quantization** (Chapter 8). Turning the fields into operators whose commutators or anticommutators at equal time follow from the Hamiltonian form of the Lagrangian; here with respect to the time $x_4$.
- **canonical spin connection** (Chapter 4). The unique solution $\omega_\mu{}^a{}_b$ of the vielbein postulate, lowered with $\eta$ to the antisymmetric $\omega_{\mu ab}$; the only connection used by the project.
- **Cartan–Dieudonné theorem** (Chapter 2). Every element of O(4,4) is a product of at most eight reflections; quoted without proof.
- **chain rule** (Chapter 1). The derivative of a composed function is the sum over the intermediate variables of the products of partial derivatives.
- **characteristic polynomial** (Chapter 1). $p(x)=\det(xI-A)$; its roots are the eigenvalues of $A$.
- **charge** (Chapters 5 and 7). The conserved quantity of a continuous symmetry, $Q=\int j^4\,d^7x$ over a slice; for dirac16complex the U(1) charge $Q=\int\sqrt{|g|}\,J^4\,d^7x$ of the phase symmetry, which in the good sector counts particles minus antiparticles (Chapter 8).
- **charge conjugation, C** (Chapters 6 and 17). A map that exchanges particles and antiparticles; for the fields of this book an antilinear map $\Psi\to M\Psi^\ast$ with a constant matrix, such as $C_0:\Psi\to\Psi^\ast$ and $C_8:\Psi\to\gamma^8\Psi^\ast$. For the commuting field $C_0$ is an exact symmetry that reverses the charge; for the Grassmann field no constant charge conjugation is a symmetry when $m\ne0$.
- **charge matrix, $C$** (Chapter 2). $C=\gamma^0\gamma^1\gamma^2\gamma^3$, the notebook's $\sigma_{16}$; real, symmetric, $C^2=1$, signature (8,8); it defines the Dirac adjoint.
- **charge sloshing** (Chapter 12). The failure of a plain self-consistency iteration in which the density jumps back and forth between two regions.
- **chart** (Chapter 4). A part of a manifold together with a one-to-one assignment of coordinates.
- **check** (Chapter 0). A named statement decided by a verifier and recorded in its report as `true` or `false`.
- **checker** (Chapter 2). An independent Python program (`scripts/check_*.py`, usually built on sympy) that recomputes the exact or numerical results of a Wolfram verifier or of a Rust program and writes its own report.
- **chemical potential** (Chapter 12). The Lagrange multiplier $\mu$ that fixes the particle number; the change of the minimal energy per added particle.
- **chirality, $\gamma^8$** (Chapter 2). The product $\gamma^0\gamma^1\cdots\gamma^7$; Hermitian, $(\gamma^8)^2=1$, anticommuting with every $\gamma^a$, equal to $\mathrm{diag}(-I_8,I_8)$ in the notebook basis. The chirality projectors $P_\mp=\tfrac12(1\mp\gamma^8)$ select the two halves.
- **chirality map, T1** (Chapter 15). The map $\Psi\to\gamma^8\Psi$; it turns the theory with $(m,\lambda)$ into the one with $(-m,-\lambda)$ and reverses the sign of the Lagrangian, the current and the energy–momentum tensor.
- **Christoffel symbols** (Chapter 4). The coefficients $\Gamma^\rho{}_{\mu\nu}$ of the Levi-Civita connection, computed from the metric and its first derivatives.
- **Clifford algebra, $\mathrm{Cl}(p,q)$** (Chapter 2). The algebra generated by elements $\gamma^a$ with $\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}$; $\mathrm{Cl}(4,4)$ is the algebra of all real $16\times16$ matrices.
- **Clifford picture, tensor-product picture** (Chapter 2). The construction of real $16\times16$ gammas as Kronecker products of $2\times2$ matrices, the "Clifford picture" of the reference implementation dirac-main.
- **Clifford relation** (Chapter 2). $\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}I$.
- **Clifford vector** (Chapter 2). A combination $v=\sum_cv_c\gamma^c$ of the gamma matrices.
- **closed shell** (Chapter 13). A particle number that fills complete Kohn–Sham levels (for example $N=8$, 112, 1016); for it the Kohn–Sham gap is well defined.
- **collisionless** (Chapter 11). A gas whose particles do not interact after the start, so that each momentum mode keeps its occupation.
- **commutant** (Chapter 2). The set of matrices that commute with every matrix of a representation; its dimension decides irreducibility and equivalence.
- **commutator** (Chapter 1). $[A,B]=AB-BA$; two matrices commute when it is zero.
- **comoving** (Chapter 11). Measured in coordinates that expand with the universe; a comoving momentum $k$ corresponds to the physical momentum $k/a$.
- **completeness relation** (Chapter 8). $\sum_s(u_s)_a(u_s)_b^\ast+\sum_s(v_s)_a(v_s)_b^\ast=\delta_{ab}$ for an orthonormal basis of positive- and negative-energy columns; it expresses that the basis spans all of $\mathbb C^{16}$.
- **complex conjugate** (Chapter 1). $z^\ast=a-ib$ for $z=a+ib$; for a matrix, conjugation of every entry.
- **complex number** (Chapter 1). A number $a+ib$ with real $a,b$ and $i^2=-1$.
- **complexification** (Chapter 6). The Lagrangian of dirac16complex00 viewed as two copies of the notebook's real Lagrangian, one for the real and one for the imaginary part of the field, coupled only through the interaction $U$.
- **components** (Chapter 1). The numbers $v_0,\dots,v_{n-1}$ of a vector (counted from 0); in Chapter 4 the numbers of a tensor in a chosen chart or frame.
- **composition algebra** (Chapter 3). An algebra with unit and a nondegenerate quadratic norm with $N(xy)=N(x)N(y)$.
- **COMPUTED** (Chapter 0). The status of a numerical result of a program, reproducible and checked but not a proof.
- **conjugation (Grassmann)** (Chapter 5). The rule $F\to F^\ast$ on a Grassmann algebra; it is antilinear and reverses products, $(FG)^\ast=G^\ast F^\ast$.
- **connection coefficients** (Chapter 4). The numbers $\Gamma^\mu{}_{\nu\lambda}$ added to partial derivatives to make the covariant derivative a tensor.
- **conserved current** (Chapter 5). A current $j^\mu$ with $\partial_\mu j^\mu=0$ on solutions; its time component integrates to a conserved charge.
- **conserved quantity** (Chapter 16). A number computed from the state that does not change in time; it forbids a transition exactly when its values before and after differ, so conservation laws are necessary, never sufficient, conditions for a process.
- **constraint** (Chapters 5 and 11). A relation that the variables must satisfy at every time: a momentum that is a function of the coordinates (Chapter 5), or an Einstein equation without second time derivatives (Chapter 11).
- **continuation in the coupling** (Chapter 13). Defining the Kohn–Sham ground state as the self-consistent solution reached from $\lambda=0$ through intermediate couplings.
- **continuous symmetry** (Chapter 5). A family of field changes under which the Lagrangian density changes only by a total divergence.
- **contraction** (Chapter 13). The number (times the unit operator) that an equal-time anticommutator of two field operators gives; Wick's theorem writes expectation values as sums of products of contractions.
- **convergence (of a numerical method)** (Chapter 10). A method converges if its error tends to 0 as the step size $h$ tends to 0.
- **correlation energy** (Chapter 12). The part of the ground-state energy that no single Slater determinant captures, $E_0-E_{HF}$.
- **cosmic microwave background** (Chapter 17). The thermal radiation left from the early universe; its temperature and pattern measure the baryon density.
- **cosmological constant** (Chapter 4). A constant $\Lambda$ in the Einstein equations; as a fluid it has $w=-1$ (Chapter 11).
- **counterterm, renormalization** (Chapter 18). Terms added to a Lagrangian to absorb the infinities of perturbation theory; a theory is renormalizable if finitely many kinds suffice. The contact interaction of dirac16complex in eight dimensions is not renormalizable.
- **covariance** (Chapter 14). The matrix $K_{ab}=\langle\Psi_a\Psi_b^\ast\rangle$ of a collection of classical fields; it is positive semidefinite for every probability distribution, while the expectation-value rule of the model makes it indefinite.
- **covariant derivative** (Chapter 4). A derivative corrected by connection coefficients so that it maps tensors to tensors; for spinors $D_\mu=\partial_\mu+\Omega_\mu$.
- **covector** (Chapter 4). An object with lower-index components that transform with $\partial x/\partial x'$, such as a gradient.
- **CP, CPT** (Chapter 17). CP combines charge conjugation with a spatial reflection (parity); CPT combines charge conjugation, parity and time reversal.
- **CPL form** (Chapter 11). The Chevallier–Polarski–Linder parametrization $w(a)=w_0+w_a(1-a)$ of a slowly changing equation of state.
- **CPT-symmetric universe** (Chapter 17). The proposal of L. Boyle, K. Finn and N. Turok (2018) that the universe after the big bang is the CPT image of the universe before it; cited as the known published example of a universe that is symmetric as a whole but made of two oppositely asymmetric parts.
- **creation operator** (Chapters 8 and 12). The operator $b^\dagger$ (or $a_p^\dagger$) that adds one fermion to an empty mode and gives zero on an occupied mode.
- **critical density** (Chapter 11). $\rho_{\mathrm{crit}}=3H_0^2/\kappa_4$, the energy density of a spatially flat universe with today's Hubble rate.
- **cross-check, cross-checker** (Chapter 13). The comparison of the Stage-4 Rust solver with the independent Python reference solver `scripts/ks_reference_solver.py`, made by the checker `scripts/check_dirac16complex_kohn_sham.py` with tolerances fixed in advance.
- **cross section** (Chapter 16). The effective target area $\sigma$ that quantum electrodynamics assigns to a nucleus for pair creation by a photon: aimed at random into an area $A$, the photon makes a pair with probability $\sigma/A$; the example of a computed creation probability.
- **curvature** (Chapter 4). The failure of parallel transport around small loops, measured by the Riemann tensor; for spinors by $F_{\mu\nu}$.
- **curved gamma matrices** (Chapter 4). $\gamma^\mu=e_a{}^\mu\gamma^a$, the gammas with a coordinate index, which satisfy $\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=2g^{\mu\nu}$.
- **CVODE** (Chapter 10). The initial-value solver of SUNDIALS (variable step and order, Adams and BDF families), used here in its pure-Rust translation.
- **cyclic property** (Chapter 2). $\mathrm{tr}(AB)=\mathrm{tr}(BA)$.

### 20.3 Glossary: D to F

- **d16c, d16c00** (Chapter 14). Abbreviations of dirac16complex and dirac16complex00 in tables and in the names of numerical runs, such as `d16c_m3_L3_N112_lam0_T0`.
- **dark energy** (Chapter 11). Whatever makes the expansion of the observed universe speed up today; it needs a large negative pressure, and in the standard model of cosmology it is a cosmological constant. EXP-3 tests whether a condensate of dirac16complex can supply it (the answer of Chapter 11 is no).
- **dark matter** (Chapter 11). Gravitating matter that cannot be seen; it clusters like ordinary matter and has almost no pressure. EXP-4 tests whether the quanta of dirac16complex behave like it (the answer of Chapter 11 is a qualified yes).
- **DEC**: see dominant energy condition.
- **deceleration parameter** (Chapter 11). $q=-\ddot aa/\dot a^2$, positive when the expansion slows down and negative when it speeds up.
- **delta function, Dirac delta** (Chapters 8 and 9). The generalized function $\delta(x)$ with $\int\delta(x)f(x)\,dx=f(0)$; it describes a source concentrated on a point or, in Chapter 9, on the brane.
- **Delta-SCF** (Chapter 12). An excitation energy obtained as the difference of two self-consistent energies, of the excited and of the ground state, $E_1-E_0$; unlike the Kohn–Sham gap it includes the relaxation of the orbitals.
- **dense direct solver** (Chapter 10). The solution of a linear system by Gaussian elimination on the full matrix; used by CVODE's Newton iteration in EXP-1.
- **density** (Chapter 12). The expected number of particles per unit volume at a point, $n(\mathbf r)$; for orbitals with occupations $f_a$ it is $\sum_af_a|\varphi_a(\mathbf r)|^2$. The basic variable of density functional theory.
- **density functional theory, DFT** (Chapter 12). The method that computes the ground-state energy as a functional of the density instead of the many-body wave function; in practice through the Kohn–Sham equations.
- **density matrix** (Chapter 14). $\rho=\sum_nf_n\,u_nu_n^\dagger$, the matrix of two-point averages $\langle\psi_a^\ast\psi_b\rangle=\rho_{ba}$; in Chapter 12 the one-body density matrix of a many-body state.
- **density operator** (Chapter 12). The operator $\hat\rho=\sum_ip_i|\Psi_i\rangle\langle\Psi_i|$ of a statistical ensemble; at a temperature $T$ it is $e^{-(\hat H-\mu\hat N)/T}$ divided by its trace.
- **density parameters** (Chapter 11). $\Omega_i=\rho_i/\rho_{\mathrm{crit}}$, the energy densities of the components of the universe today in units of the critical density.
- **derived here** (Chapter 18). The mark of a short calculation that is complete as written but has not been checked by any program of the repository.
- **determinant** (Chapter 1). The number $\det A=\sum_\pi\mathrm{sgn}(\pi)\prod_iA_{i\pi(i)}$; it is nonzero exactly when $A$ is invertible, and $\det(AB)=\det A\det B$.
- **DFT**: see density functional theory.
- **diagonal matrix** (Chapter 1). A square matrix whose entries off the main diagonal are zero.
- **difference quotient** (Chapter 10). An approximate derivative $(f(x+h)-f(x))/h$; CVODE uses difference quotients to build the Jacobian matrix.
- **dimension** (Chapter 1). The number of vectors in a basis of a vector space.
- **Dirac adjoint** (Chapter 2). The row $\bar\Psi=\Psi^\dagger C$ built with the charge matrix $C$; the bilinears $\bar\Psi M\Psi$ with suitable $M$ do not change under spin transformations.
- **Dirac bracket** (Chapter 8). The bracket of Hamiltonian mechanics with second-class constraints, built from the inverse of the matrix of the constraint brackets; its quantized form gives the canonical anticommutator.
- **dirac-main** (Chapter 2). The reference implementation of the gamma matrices and the split octonions with which Stage 1 compares (its tensor matrices are the Clifford picture); its files are kept in the git-ignored folder `dirac-main/`, so that a public clone runs the gates without those comparisons (Section 19.6).
- **Dirac operator** (Chapter 4). The operator $\gamma^\mu D_\mu$ of the field equation in a curved space; its square is given by the Lichnerowicz formula.
- **Dirac's exchange energy** (Chapter 12). The exchange energy per volume of the uniform electron gas, $-\tfrac34(3/\pi)^{1/3}n^{4/3}$ in atomic units; the local exchange of the LDA.
- **Dirac sea** (Chapter 8). The state in which every negative-energy mode is filled; the vacuum of the good sector, in which a hole is an antiparticle with positive energy.
- **dirac16complex** (Chapter 0). The field theory of this book: a 16-component complex spinor field with anticommuting (Grassmann) components in eight dimensions of signature (4,4), with a mass term, a scalar interaction and the canonical spin connection.
- **dirac16complex00** (Chapter 0). The same Lagrangian for a field with ordinary commuting complex components (a classical field); its real restriction is the notebook's Lagrangian (Chapter 6).
- **direct and exchange terms** (Chapter 14). The two ways of pairing the four amplitudes of an average $\langle c_n^\ast c_q^\ast c_rc_p\rangle$; the exchange term has the sign $+$ for Gaussian waves and $-$ for fermions.
- **distance modulus** (Chapter 11). $\mu=5\log_{10}(d_L/10\,\mathrm{pc})$, the logarithm of the luminosity distance used in supernova tables.
- **dominant energy condition, DEC** (Chapter 9). The weak energy condition together with the requirement that energy does not flow faster than light; it needs $\rho\ge0$ in particular.
- **dot product, cross product** (Chapter 3). For vectors of three components $u\cdot r=u_1r_1+u_2r_2+u_3r_3$ (a symmetric number) and $u\times r$ (an antisymmetric vector); the quaternion product contains both.
- **double cover** (Chapter 2). A map from a group onto another that sends exactly two elements (here $R$ and $-R$) to each image; Pin(4,4) and Spin(4,4) are double covers of O(4,4) and SO(4,4).
- **double, double precision** (Chapter 10). The standard 64-bit floating-point number, with about 16 significant decimal digits.
- **dual (of an antisymmetric $4\times4$ matrix)** (Chapter 3). $({\ast}A)_{pq}=\tfrac12\sum_{r,s}\epsilon_{pqrs}A_{rs}$; the matrix is self-dual if ${\ast}A=A$ and anti-self-dual if ${\ast}A=-A$.
- **dummy index** (Chapter 1). An index that is summed over; its name can be changed without changing the expression.
- **dynamics** (Chapter 16). The equations that say how a state changes in time and how often a transition happens; conservation laws alone do not decide this.
- **eigenvalue, eigenvector** (Chapter 1). A number $\lambda$ and a nonzero vector $v$ with $Av=\lambda v$.
- **eigenvalue problem** (Chapter 10). The task of finding the values of a parameter (for example the Kohn–Sham level $\varepsilon$) for which a differential equation with boundary conditions has a nonzero solution.
- **Einstein equations** (Chapter 4). $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ (in this book with $\kappa$ of eight dimensions), relating the curvature of spacetime to its energy–momentum source.
- **Einstein–Lovelock equations** (Chapter 4). The Einstein equations supplemented by the Lovelock tensors of orders 2 and 3, the most general equations of this kind in eight dimensions; the notebook names them, but neither the notebook nor the project computes the higher orders.
- **Einstein summation convention** (Chapter 1). An index that appears once up and once down in a product is summed over.
- **Einstein tensor** (Chapter 4). $G_{\mu\nu}=R_{\mu\nu}-\tfrac12g_{\mu\nu}R$; its covariant divergence vanishes identically.
- **electric charge** (Chapter 17). The conserved charge of electromagnetism; particles and antiparticles carry opposite electric charges.
- **elementary matrix** (Chapter 2). $E_{ij}$, the matrix with a 1 in row $i$ and column $j$ and 0 everywhere else; the $E_{ij}$ form a basis of all matrices.
- **energy condition** (Chapter 9). An inequality for the energy density and the pressures of a source, such as the weak, null, strong and dominant conditions; the primordial field violates some of them.
- **energy density** (Chapter 5). The energy per volume: for the canonical tensor of Chapter 5 the component $\Theta^4{}_4$; for the metric energy–momentum tensor and an observer moving along $x_4$ with $g_{44}=-1$, $\rho=T_{44}=-T^4{}_4$ (Chapters 7 and 9).
- **energy–momentum tensor** (Chapter 5). The tensor $T^\mu{}_\nu$ that contains energy density, momentum density, pressures and stresses; in Chapter 7 the metric (Hilbert) energy–momentum tensor from the variation of the action with respect to the metric, the source of the Einstein equations.
- **energy projectors** (Chapter 8). $\Lambda_\pm=\tfrac12(1\pm h_k/E)$, which split the modes of a momentum into those with energy $+E$ and $-E$.
- **ensemble** (Chapter 12). A statistical mixture of many-body states with probabilities; at a temperature $T$ the grand-canonical ensemble.
- **entropy** (Chapter 12). $S=-\mathrm{tr}(\hat\rho\ln\hat\rho)$, for independent fermions $-\sum_n[f_n\ln f_n+(1-f_n)\ln(1-f_n)]$.
- **envelope theorem** (Chapter 12). The derivative of the minimum of a function with respect to a parameter equals the partial derivative at the minimizer; it underlies the Hellmann–Feynman relations.
- **equation of state, equation-of-state parameter** (Chapter 5). A relation between pressure and energy density; the parameter is $w=p/\rho$ ($w=0$ for dust, $\tfrac13$ for radiation, $-1$ for a cosmological constant).
- **equivalent representations** (Chapter 2). Two representations $\rho,\rho'$ with an invertible intertwiner, $\rho'(g)=X\rho(g)X^{-1}$.
- **erratum** (Chapter 18). A recorded correction of a specification or of the notebook, with its evidence, such as the errata E4.1 to E4.13 of the Stage-4 specification; errata are cited from Chapter 3 on.
- **Euler–Lagrange equations** (Chapter 5). The conditions for the action to be stationary, $\frac{d}{dt}\frac{\partial L}{\partial\dot q}=\frac{\partial L}{\partial q}$, and their field version with $\partial_\mu$.
- **Euler–Lagrange expression** (Chapter 5). The left side $E^A$ of the Euler–Lagrange field equation of the component $A$; it vanishes exactly on solutions and is unchanged when a total divergence is added to $\mathcal L$.
- **Euler's method** (Chapter 10). The simplest method for $y'=f(t,y)$: $y_{n+1}=y_n+hf(t_n,y_n)$ (explicit); the implicit (backward) form evaluates $f$ at the new point.
- **even, odd** (Chapters 2 and 5). A Clifford monomial or a Grassmann monomial of even or odd degree; even Grassmann elements commute with everything, odd ones anticommute with each other.
- **evolution equations** (Chapter 11). The Einstein equations with second time derivatives, which advance the metric in time, as opposed to the constraint.
- **exact symmetry** (Chapter 17). A map $T$ with $\mathcal L_{m,\lambda}[T\Psi](x)=\mathcal L_{m,\lambda}[\Psi](Rx)$ for every field, in flat space or in a gravitational field in which the reflection $R$ is an isometry.
- **exchange–correlation energy** (Chapter 12). The unknown part $E_{xc}[n]$ of the Kohn–Sham energy functional that contains everything beyond the non-interacting kinetic energy, the external energy and the Hartree energy; it must be approximated.
- **exchange energy** (Chapter 12). The Fock term $E_x=-\tfrac12\int\!\int|\rho(x,x')|^2w(x,x')\,dx\,dx'$ of the energy of a Slater determinant; it has no classical analogue, comes from the antisymmetry of the wave function and lowers the energy for a repulsive interaction.
- **exchange-only** (Chapter 13). A Kohn–Sham calculation that keeps the exact exchange of the interaction and no correlation energy; Chapter 13 is of this kind.
- **exchange potentials** (Chapter 13). The derivatives $v_v=\partial e_x/\partial n=-\tfrac\lambda{16}n$ and $v_s=\partial e_x/\partial S=-\tfrac\lambda{16}S$ of the local exchange energy density; $v_v$ shifts the energy, $v_s$ adds to the mass.
- **EXP-1 to EXP-5** (Chapter 11). The five numerical experiments of Stage 3: the field in the primordial field of the notebook (EXP-1), a homogeneous self-gravitating universe in eight dimensions (EXP-2), a condensate as the dark energy of the late universe (EXP-3), the quanta of an expanding 3-space as dark matter and their creation (EXP-4), and the deflating extra times (EXP-5).
- **expectation value** (Chapter 8). $\langle f,Of\rangle$ for a normalized state $f$, the average of many measurements of $O$.
- **expectation-value rule** (Chapter 11). The rule that replaces a bilinear of the quantum field by its average in the state (normal ordered against the sea); it defines the mean-field sources.
- **explicit, implicit method** (Chapter 10). An explicit method computes the new value from known values; an implicit one solves an equation that contains the new value, and is needed for stiff problems.
- **exponential wall** (Chapter 12). The growth of the size of the many-body wave function exponentially with the number of particles, which makes a direct computation impossible.
- **extra times** (Chapter 9). The three coordinates $x_5,x_6,x_7$, time-like like $x_4$; in the primordial field they deflate.
- **extrinsic curvature** (Chapter 9). The rate of change of the induced metric of a surface along its unit normal; its jump across the brane is fixed by the Israel junction condition.
- **Fermi–Dirac distribution** (Chapter 12). $f(\varepsilon)=1/(e^{(\varepsilon-\mu)/T}+1)$, the occupation of a fermion level at temperature $T$.
- **Fermi momentum** (Chapter 12). The largest momentum occupied in the ground state of a uniform gas, $k_F=(3\pi^2n)^{1/3}$ for two spin states.
- **fermion mode, boson mode** (Chapter 14). A fermion mode is empty or occupied once; a boson mode has a commutator $[b,b^\dagger]=1$ and can be occupied any number of times.
- **fermions** (Chapter 5). Particles described by anticommuting variables or operators; their many-body wave functions change sign when two of them are exchanged, and no mode holds more than one.
- **fibre, base** (Chapter 9). In a warped metric the coordinates split into base coordinates (in Lemma 9.1 the two coordinates $x_0$ and $x_4$) and fibre coordinates (the six others), whose scale factors depend only on the base coordinates.
- **field** (Chapter 5). A quantity that has a value at every point of spacetime, such as a scalar field $\phi(x)$ or the spinor field $\Psi(x)$.
- **field equations** (Chapter 5). The Euler–Lagrange equations of a field; for the two fields of this book derived in Chapter 7.
- **first excited state** (Chapter 12). The state of lowest energy above the ground state; in Chapter 13 obtained by moving one particle from the highest occupied to the lowest empty level.
- **first-order adiabatic basis** (Chapter 11). The basis of instantaneous levels corrected to first order in the rate of change, in which EXP-4 measures the created weight $|\beta_k|^2$ so that the adiabatic dressing is not counted as creation.
- **first-order form** (Chapter 10). A system of first derivatives equivalent to a higher-order equation, obtained by treating derivatives as new unknowns.
- **first quantization** (Chapter 6). The description of a single particle by a wave function.
- **fixed-modulus** (Chapter 14). A random amplitude $c=\sqrt f\,e^{i\varphi}$ with a random phase and a fixed modulus; unlike Gaussian amplitudes it has $\langle|c|^4\rangle=f^2$.
- **fixed point** (Chapter 12). A density that the self-consistency map returns unchanged; the Kohn–Sham solution.
- **fixed-point iteration** (Chapter 10). Solving $x=g(x)$ by repeating $x\leftarrow g(x)$; CVODE solves the implicit equation of each Adams step this way.
- **FMA** (Chapter 10). Fused multiply-add, a processor instruction that computes $ab+c$ with a single rounding; the committed numerical files are byte-identical only when the program is built with it.
- **Fock operator** (Chapter 12). The one-particle operator of the Hartree–Fock equations, kinetic plus external plus Hartree plus exchange operator.
- **Fock space** (Chapter 8). The space of states with any number of particles and antiparticles, built from the vacuum by creation operators; positive in the good sector.
- **frame form** (Chapter 17). The way a reflection is applied in a gravitational field: the points are not moved, $\Psi'(x)=M\Psi(x)$, and the frame directions are multiplied by the signs $r_a$, which leaves the metric unchanged.
- **frame, vielbein** (Chapter 4). At every point a set of eight orthonormal directions, given by $e_\mu{}^a$ with $g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b$; spinor components are measured in it.
- **Friedmann equations** (Chapter 11). The Einstein equations of a homogeneous and isotropic four-dimensional universe, relating the Hubble rate and its derivative to the energy density and the pressure.
- **functional** (Chapter 5). A rule that assigns a number to a whole function, such as the action to a path or the energy to a density.
- **functional derivative** (Chapter 12). $\delta F/\delta n(\mathbf r)$, defined by $\delta F=\int\frac{\delta F}{\delta n}\,\delta n\,d^3r$ to first order.
- **fundamental gap** (Chapter 12). $E(N+1)+E(N-1)-2E(N)$, the difference of ionization energy and electron affinity; not equal to the Kohn–Sham gap in general.
- **fundamental symmetry** (Chapter 8). An operator $J$ with $J=J^\dagger=J^{-1}$ that turns the indefinite form of a Krein space into a positive inner product $[f,Jh]$.

### 20.4 Glossary: G to K

- **G1, G2** (Chapter 4). The two test geometries of Stage 1: G1 is a generic non-diagonal vielbein $e_\mu{}^a=\delta_\mu{}^a+P_\mu{}^a(x)$ with polynomial entries, tested at three rational points; G2 is the primordial field. Check names end in `_G1` or `_G2` accordingly.
- **gamma matrices** (Chapter 2). Sixteen-by-sixteen matrices $\gamma^0,\dots,\gamma^7$ with $\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}$; the book uses the real matrices of the notebook.
- **gate** (Chapter 0). A script that runs every program of a stage in a fixed order, stops at the first failure, compares the outputs with the committed files and ends with one line `..._verification=OK` or `FAILED`; each exists as a PowerShell and a Bash twin (Chapter 19).
- **Gauss–Bonnet combination** (Chapter 9). The Lovelock Lagrangian of order 2, $R^2-4R_{\mu\nu}R^{\mu\nu}+R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$; in eight dimensions it would add a term to the Einstein equations that neither the notebook nor the project computes.
- **Gauss-Legendre quadrature** (Chapter 11). A rule $\sum_nw_nF(k_n)$ with nodes and weights chosen so that it integrates every polynomial up to degree $2n-1$ exactly; EXP-4 uses 48 nodes.
- **Gaussian amplitudes** (Chapter 14). Random complex amplitudes with the density $e^{-|c|^2/f}/(\pi f)$, the amplitudes of thermal (chaotic) waves; for them the exchange term of an average has the sign $+$.
- **Gaussian normal** (Chapter 7). A time coordinate with $g_{44}=-1$ and $g_{4i}=0$ for $i\ne4$, with the frame's time direction along $x_4$; the observer of the energy density and the pressures.
- **generalized Kronecker delta** (Chapter 4). $\delta^{\mu_1\cdots\mu_k}_{\nu_1\cdots\nu_k}$, the determinant of the $k\times k$ matrix of ordinary Kronecker deltas; the Lovelock tensors are built with it.
- **generators** (Chapter 2). Elements whose products and combinations give a whole algebra or group: the $\gamma^a$ generate the Clifford algebra, and the $S^{ab}$ generate the part of Spin(4,4) connected to 1.
- **geodesic** (Chapter 4). A curve that is as straight as the geometry allows: its velocity is parallel transported along itself; freely falling particles move on geodesics.
- **global error** (Chapter 10). The difference between the computed and the exact solution after many steps; for a method of order $p$ it is proportional to $h^p$.
- **good sector** (Chapter 8). The modes of the field that do not depend on the three extra times $x_5,x_6,x_7$; in it the Fock space is positive and the Hamiltonian not negative. The numerical chapters are restricted to it, by assumption.
- **grand potential** (Chapter 12). $\Omega=\mathrm{Tr}[\hat\rho(\hat H-\mu\hat N)]+T\,\mathrm{Tr}[\hat\rho\ln\hat\rho]$; the equilibrium state at temperature $T$ minimizes it.
- **Grassmann numbers, Grassmann algebra** (Chapter 5). Numbers generated by anticommuting symbols $\theta_i$ with $\theta_i\theta_j=-\theta_j\theta_i$, so $\theta_i^2=0$; the classical description of fermion fields. The components of dirac16complex are Grassmann-odd.
- **gravitational pair creation** (Chapter 11). The appearance of particle–antiparticle pairs out of the vacuum through the expansion of space alone; EXP-4 computes it for an inflation followed by radiation.
- **ground state** (Chapter 12). The state of lowest energy; its energy is the minimum of the energy expectation value over all normalized states.
- **group** (Chapter 2). A set with an associative product, a unit and inverses; a subgroup is a subset that is itself a group.
- **Hamilton's equations** (Chapter 8). $\dot q=\partial H/\partial p$ and $\dot p=-\partial H/\partial q$, the first-order form of the equations of motion.
- **Hamiltonian** (Chapter 5). The energy as a function of coordinates and momenta, $H=p\dot q-L$; it generates the time evolution through Hamilton's equations (Chapter 8) and, as an operator, the Schrödinger equation.
- **Hartree approximation** (Chapter 12). The mean-field approximation that keeps the Hartree potential and drops the exchange; it keeps the self-interaction of each particle.
- **Hartree energy, Hartree potential** (Chapter 12). $E_H=\tfrac12\int\!\int n(x)w(x,x')n(x')$, the classical interaction energy of the density with itself, and its functional derivative $v_H=\int w\,n$.
- **Hartree–Fock approximation** (Chapter 12). The best single Slater determinant, found by minimizing the energy over all choices of orthonormal orbitals; restricted if both spins share one spatial orbital, unrestricted otherwise.
- **Hartree–Fock energy density** (Chapter 13). For the contact interaction, $e_{HF}=\tfrac\lambda2(S^2-\mathrm{Tr}(BC\rho BC\rho))$ with $S=\mathrm{Tr}(BC\rho)$: the Hartree term $\tfrac\lambda2S^2$ and the exchange (Fock) term.
- **heat capacity** (Chapter 12). $C_V=dE/dT$ at fixed particle number; for the Kohn–Sham gas of Chapter 13 $C_V=T\,dS_s/dT$.
- **Heisenberg equation** (Chapter 8). $\dot O=i[H,O]$ for an operator without explicit time dependence; the quantum form of Hamilton's equations.
- **Hellmann–Feynman rule** (Chapter 13). For a normalized eigenvector $\chi$ of $h(k)$ with boundary conditions that do not depend on $k$, $d\varepsilon/dk=\langle\chi|(\partial_kh)\chi\rangle$; the Stage-4 checks whose names begin with `KS_functional_hellmannFeynman` test the analogous relations for the derivatives of the energy functional with respect to the coupling, the mass and the temperature.
- **Hermitian** (Chapter 1). A square matrix with $A^\dagger=A$; its eigenvalues are real and it has an orthonormal basis of eigenvectors.
- **Hermitian conjugate** (Chapter 1). $A^\dagger=(A^\ast)^T$, the conjugate transpose.
- **Hermitian form** (Chapter 8). A rule $[f,h]=f^\dagger Gh$ with a Hermitian matrix $G$; it is non-degenerate if $Gf=0$ only for $f=0$ and indefinite if some $[f,f]$ are negative.
- **hidden space** (Chapter 9). The coordinate $x_0$, space-like like $x_1,x_2,x_3$; in the static member of the primordial field the warp factor depends on it.
- **Hilbert adjoint, Hilbert norm** (Chapters 8 and 11). The adjoint and the norm $u^\dagger u$ with respect to the positive inner product, as opposed to the Krein adjoint and the Krein norm $u^\dagger Bu$.
- **Hilbert space** (Chapter 8). A complex vector space with a positive inner product; it gives probabilities.
- **Hohenberg–Kohn theorems** (Chapter 12). The ground-state density determines the external potential up to a constant, and the ground-state energy is the minimum of a functional of the density; the foundation of DFT.
- **hole** (Chapter 12). An empty level below the highest occupied one, created by removing a particle; in Chapter 8 a hole in the Dirac sea is an antiparticle.
- **homogeneous frames** (Chapter 4). Diagonal frames of the metrics $ds^2=-dt^2+\sum_{j\ne4}\eta_{jj}h_j(t)^2dx_j^2$ with $t=x_4$, whose scale factors $h_j$ depend only on the time; the metrics of cosmology in this book.
- **homomorphism** (Chapter 2). A map between groups that respects the products; its kernel is the set of elements sent to the unit.
- **honesty rule** (Chapter 0). The rule of this book that every statement carries its status (PROVED, COMPUTED, ASSUMED, HYPOTHESIS or OPEN) and that no claim goes beyond what the committed files support.
- **Hubble length** (Chapter 11). $c/H$, the distance light travels in one expansion time; a wave is inside the horizon when its physical wavelength is much shorter.
- **Hubble rate** (Chapter 9). The logarithmic rate of change of a scale factor, $H=\dot a/a$; today's value in ordinary cosmology is $H_0$ (Chapter 11).
- **Hurwitz's theorem** (Chapter 3). The only composition algebras with a positive norm have dimensions 1, 2, 4 and 8 (the real numbers, complex numbers, quaternions and octonions); quoted, not proved.
- **HYPOTHESIS** (Chapter 0). The status of a statement that is proposed but neither proved nor computed, such as the notebook's claim that universes are created in pairs.
- **identity matrix** (Chapter 1). The matrix $I$ with ones on the diagonal and zeros elsewhere, $IA=AI=A$.
- **Illinois variant** (Chapter 10). The regula falsi with the improvement that, when the same end is replaced twice in a row, the function value at the other end is halved; the level finder of the Stage-4 solver.
- **image field** (Chapter 15). $\Psi_-=\gamma^8\Psi_+$ regarded on the same state space as $\Psi_+$; it carries the reversed Krein metric $-B$, so its cancelling energy and charge are operator identities, not a second independent universe.
- **image (of a matrix)** (Chapter 2). The set of all columns $Mu$, a subspace; its dimension is the rank.
- **indefinite** (Chapter 8). A form or inner product that takes both positive and negative values, such as $f^\dagger Bf$.
- **initial-value problem** (Chapter 10). A differential equation together with the value of the solution at a starting time.
- **inner product** (Chapter 8). A rule $\langle f,h\rangle$, linear in $h$ and antilinear in $f$, with $\langle h,f\rangle=\langle f,h\rangle^\ast$; positive if $\langle f,f\rangle>0$ for $f\ne0$.
- **inside the horizon** (Chapter 11). A wave whose physical wavelength is much shorter than the Hubble length, $K\gg H$.
- **interacting quantum field theory** (Chapter 18). A quantum theory of the field with its interaction, with positive probabilities, a Hamiltonian bounded below and finite predictions; for dirac16complex it is OPEN.
- **interaction, $U(S)$** (Chapter 6). The term $-\sqrt{|g|}\,U(S)$ of the Lagrangian, a function of the scalar density $S=\bar\Psi\Psi$; for the contact interaction of Chapters 11 and 13, $U=\tfrac\lambda2S^2$.
- **interpolation** (Chapter 10). Computing the solution between two steps from a polynomial through computed values; CVODE returns output at requested times this way.
- **intertwiner** (Chapter 2). A matrix $X$ with $X\rho(g)=\rho'(g)X$ for all $g$; an invertible one makes the two representations equivalent.
- **invariant bilinear form** (Chapter 6). A matrix $G$ with $(S^{ab})^TG+GS^{ab}=0$ for all $a,b$, so that $\Psi^TG\Phi$ does not change under spin rotations; Chapter 8 shows that no such form gives a positive charge density, and Theorem M3 of Chapter 17 lists all of them.
- **invariant mass** (Chapter 16). $\mu^2=E_{\mathrm{tot}}^2-|\mathbf p_{\mathrm{tot}}|^2$ of a group of particles; conserved in every process, so a single photon in empty space cannot make a pair.
- **inversion (of a permutation)** (Chapter 1). A pair of places $i<j$ with $\sigma(i)>\sigma(j)$; the sign of the permutation is $(-1)$ to the number of inversions.
- **invertible** (Chapter 1). A square matrix $A$ with an inverse $A^{-1}$, $AA^{-1}=A^{-1}A=I$; equivalently $\det A\ne0$.
- **irreducible** (Chapter 2). A representation with no invariant subspace other than zero and the whole space; by Schur's lemma its commutant consists of multiples of the identity.
- **isometry** (Chapter 16). A map of spacetime to itself that leaves the metric unchanged, such as the reflection $y\to-y$ of the Z2 geometry.
- **Israel junction condition** (Chapter 9). The relation between the jump of the extrinsic curvature across a surface and the energy–momentum on the surface; it fixes the source that the brane must carry.
- **Jacobi's formula** (Chapter 1). $\partial\det A=\det A\,\mathrm{tr}(A^{-1}\partial A)$.
- **Jacobian matrix** (Chapter 10). The matrix of partial derivatives $\partial f_i/\partial y_j$ of the right-hand side; implicit methods need it for Newton's method. (Chapter 4 uses the Jacobian matrix $\partial x'/\partial x$ of a change of coordinates.)
- **Janak's theorem** (Chapter 12). The derivative of the Kohn–Sham energy with respect to the occupation of a level equals the level's energy, $\partial E/\partial f_b=\varepsilon_b$.
- **jets** (Chapter 5). The field, its first derivatives and higher derivatives treated as independent variables at a point; the Euler–Lagrange expression is a function of them.
- **Kasner exponents** (Chapter 11). The powers $p^{\mathrm K}_i$ in $h_i\propto(t-t_s)^{p^{\mathrm K}_i}$ near a singular time of a homogeneous metric (EXP-2).
- **kernel** (Chapter 2). The elements a homomorphism sends to the unit; in Chapter 13 the exchange kernel of the contact interaction.
- **ket** (Chapter 12). Dirac's notation $|\Psi\rangle$ for a state vector; the bra $\langle\Psi|$ is its adjoint.
- **kinetic and potential energy** (Chapter 7). Two splits of the energy density, both definitions: the Lagrangian split $\mathrm{KE}_L=\tfrac12K_4$, $\mathrm{PE}_L=\rho-\mathrm{KE}_L$, and the Hamiltonian split $\mathrm{KE}_H=-K_\perp$, $\mathrm{PE}_H=mS+U(S)$.
- **kinetic term** (Chapter 6). The part $K$ of the Lagrangian with one derivative of the field, symmetrized between $\Psi$ and $\bar\Psi$.
- **kink formula** (Chapter 11). The leading large-momentum estimate $|\beta_k|^2\approx(mkH_{\mathrm{inf}}^2/4E^4)^2$ of the particles created when the second derivative of the scale factor jumps.
- **Klein's inequality** (Chapter 12). $\mathrm{Tr}[\hat\rho(\ln\hat\rho-\ln\hat\sigma)]\ge0$ for density operators; it proves that the Gibbs state minimizes the grand potential.
- **Kohn–Sham equations** (Chapter 12). One-particle equations $[-\tfrac12\nabla^2+v_s]\varphi_a=\varepsilon_a\varphi_a$ with $v_s=v+v_H+v_{xc}$, whose occupied orbitals give the density of the interacting system if $E_{xc}$ is exact.
- **Kohn–Sham fermion-gas thermodynamic pseudo-potential** (Chapter 13). The Stage-4 specification's name for the pair $M_{\mathrm{eff}}=m+\tfrac{15}{16}\lambda S_p$ and $v_v=-\tfrac1{16}\lambda n_p$ of the Kohn–Sham equation, together with the gravitational terms: the local density approximation built from the exact exchange of the contact interaction in the uniform gas, used as an approximation in the primordial field.
- **Kohn–Sham gap** (Chapter 12). $\Delta_{KS}=\varepsilon_{\mathrm{LUMO}}-\varepsilon_{\mathrm{HOMO}}$, the smallest difference in the particle–hole spectrum; the first estimate of the lowest excitation energy.
- **Kohn–Sham potential** (Chapter 12). The local potential $v_s$ of the Kohn–Sham equations.
- **Koopmans' theorem** (Chapter 12). In Hartree–Fock theory the energy to remove a particle from an orbital, with all other orbitals frozen, is minus the orbital energy.
- **Krein adjoint** (Chapter 8). The adjoint with respect to the indefinite form $f^\dagger Bh$; the canonical $\Psi^\dagger=\chi B$ is the Krein adjoint of $\Psi$, while $\chi$ is its Hilbert adjoint.
- **Krein image pair** (Chapters 15 and 16). A $+M$ state together with its T1 image with $-\lambda$ and the reversed metric $-B$, formed as $(+M)-(-M)$ for every one-body density; its total energy, charge and energy–momentum tensor vanish at every point.
- **Krein norm** (Chapter 11). $u^\dagger Bu$, which can be positive, negative or zero and is conserved for every mode, in and out of the good sector.
- **Krein sign** (Chapters 7 and 14). The value $\beta=js_2=\pm1$ by which the matrix $B$ acts on one of the eight $2\times2$ blocks of the Kohn–Sham problem, the sign of the form $u^\dagger Bu$ on that block; four blocks have $+1$ and four $-1$.
- **Krein space** (Chapter 8). A complex vector space with a non-degenerate indefinite Hermitian form and a fundamental symmetry; the natural space of one-particle states of dirac16complex.
- **Krein-unitary** (Chapter 8). A matrix $R$ with $R^\dagger BR=B$; it preserves the canonical anticommutator.
- **Kronecker delta** (Chapter 1). $\delta_{ij}=1$ for $i=j$ and 0 otherwise; the entries of the identity matrix.

### 20.5 Glossary: L to O

- **Lagrange multiplier** (Chapter 12). A number $\lambda$ added with a constraint $c(x)=c_0$ to a function being minimized; at the constrained minimum it equals the change of the minimum per unit change of $c_0$ (the chemical potential is one).
- **Lagrangian** (Chapter 5). The function $L(q,\dot q)$ whose time integral is the action; for a particle usually kinetic minus potential energy.
- **Lagrangian density** (Chapter 5). The function $\mathcal L$ of the fields and their derivatives whose integral over spacetime is the action of a field theory; for the two fields of this book given in Chapter 6.
- **lapse** (Chapter 18). The factor $N(x_4)$ in $g_{44}=-N^2$ that relates the coordinate time to proper time; the reduced model of Chapter 18 needs it to obtain its constraint.
- **LDA**: see local density approximation.
- **left derivative, right derivative** (Chapter 5). The two ways of differentiating a product of Grassmann variables, removing the variable after moving it to the left or to the right end; they differ by a sign for odd products.
- **Leibniz rule** (Chapter 1). The product rule $\partial(fg)=(\partial f)g+f\,\partial g$; for Grassmann variables and derivatives it acquires signs (Chapter 5).
- **lepton number** (Chapter 17). $L$: electrons, muons, tau leptons and neutrinos have $L=+1$, their antiparticles $L=-1$.
- **Levi-Civita connection** (Chapter 4). The unique connection that is torsion-free and preserves the metric; its coefficients are the Christoffel symbols. The project uses no other.
- **Levy–Lieb constrained search** (Chapter 12). The definition of the universal functional as a minimum over all wave functions with a given density.
- **Lichnerowicz formula** (Chapter 4). $(\gamma^\mu D_\mu)^2\Psi=g^{\mu\nu}(D_\mu D_\nu\Psi-\Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi)-\tfrac14R\Psi$, the square of the Dirac operator in a curved space.
- **light-cone basis, light-cone coordinates** (Chapter 3). Coordinates such as $x_0\pm x_7$, sums and differences of a space-like and a time-like coordinate, in which the norm of signature (4,4) becomes $y_0y_4+y_1y_5+y_2y_6+y_3y_7$; the notebook's $\tau_a$ are octonion multiplications written in such a basis.
- **line element** (Chapter 1). $ds^2=g_{\mu\nu}dx^\mu dx^\nu$, the squared length of a small displacement.
- **linear** (Chapter 1). A map with $f(ax+by)=af(x)+bf(y)$; matrices are the linear maps of $\mathbb R^n$ or $\mathbb C^n$.
- **linear combination** (Chapter 1). A sum $\sum_ic_iv_i$ of vectors multiplied by numbers.
- **linear mixing** (Chapter 12). The self-consistency update $n_{\mathrm{in}}\leftarrow(1-\beta)n_{\mathrm{in}}+\beta n_{\mathrm{out}}$ with a fraction $0<\beta<1$; it cures charge sloshing in simple cases.
- **linear multistep method** (Chapter 10). A method that computes the next value from several previous values and right-hand sides; Adams methods and BDF are of this kind.
- **linearly independent, dependent** (Chapter 1). Vectors are independent if no nontrivial combination of them is zero, dependent otherwise.
- **local density approximation, LDA** (Chapter 12). The approximation that treats each small volume as a piece of uniform gas with the local density, $E_{xc}\approx\int e_{xc}(n(\mathbf r))\,d^3r$; Chapter 13 uses its analogue for the exchange of the contact interaction.
- **local error** (Chapter 10). The error made in one step that starts from the exact solution; for Euler's method $\tfrac12h^2y''$, proportional to $h^2$, while the global error is proportional to $h$.
- **localized at the brane** (Chapter 13). A Kohn–Sham orbital whose weight grows toward $y=0$, such as the zero mode $\chi=(e^{My},0)^T$.
- **Lovelock gravity, Lovelock orders** (Chapter 4). The family of gravitational equations with at most second derivatives of the metric, built from powers of the curvature: order 1 is Einstein's, order 2 the Gauss–Bonnet term; in eight dimensions orders up to 3 exist (Lovelock's theorem, quoted).
- **lowering, raising an index** (Chapter 1). Contracting with $g_{\mu\nu}$ or $g^{\mu\nu}$ (or $\eta$ for frame indices) to turn an upper into a lower index or back.
- **machine epsilon** (Chapter 10). The spacing of double-precision numbers near 1, $2^{-52}\approx2.2\times10^{-16}$; the limit of every relative accuracy.
- **Magnus method** (Chapter 10). An integrator for $i\dot u=h(t)u$ that advances each step by the exponential of $-i$ times a Hermitian matrix, a unitary matrix, so that $u^\dagger u$ is kept exactly; the EXP-4 checker uses a fourth-order Magnus method.
- **Majorana-type term** (Chapter 17). A term built with $\Psi^T$ instead of $\Psi^\dagger$, such as $\Psi^TM\Psi$; it has U(1) charge 2 and would violate charge conservation. Theorem M3 shows that the anticommuting field has no Lorentz-invariant Majorana mass term.
- **manifold** (Chapter 4). A space that is covered by charts, each of which looks like a piece of $\mathbb R^n$, with smooth changes of coordinates where charts overlap.
- **mass dimension** (Chapter 13). The power of a mass unit that a quantity carries in units with $\hbar=c=1$ (a length has mass dimension $-1$); it measures the size of the coupling $\lambda$.
- **mass term** (Chapter 6). The part $-m\sqrt{|g|}\,\bar\Psi\Psi$ of the Lagrangian, linear in the mass and quadratic in the components.
- **matrix** (Chapter 1). A rectangular array of numbers; matrix multiplication is associative and distributive but not commutative.
- **matter–antimatter problem** (Chapter 17). The question why the universe contains baryons but essentially no antibaryons. Chapter 17 shows that the theory of this book, as built, does not solve it: its U(1) charge is exactly conserved (Theorem M1).
- **max_step** (Chapter 10). The largest step size allowed to CVODE in an experiment.
- **mean field** (Chapter 11). The approximation in which each quantum moves in the average field of all the others, with a bilinear such as $S$ replaced by its expectation value; the Hartree idea (Chapter 12).
- **Mermin's functional** (Chapter 12). The free energy functional of the Kohn–Sham ensemble at temperature $T$, $F=\sum_af_a\langle\varphi_a|-\tfrac12\nabla^2|\varphi_a\rangle-TS_s+\int vn+E_H+F_{xc}$; its stationary point has Fermi–Dirac occupations.
- **Mermin's theorem** (Chapter 12). The finite-temperature analogue of the Hohenberg–Kohn theorems (1965): the equilibrium density determines the potential, and the grand potential is minimal at it.
- **metric** (Chapter 1). A symmetric matrix $g_{\mu\nu}$ (in Chapter 4 a field of such matrices) that defines lengths and angles through the line element; of signature (4,4) in this book.
- **mirror map, T2** (Chapter 15). The combination of the field with the reflection of one space-like direction; it maps the theory with $(m,\lambda)$ to $(-m,\lambda)$ and leaves energy, momentum and charge unchanged (only reflected).
- **mirror pair** (Chapter 15). A $+M$ universe with its ordinary $-M$ partner of T3 (the same $\lambda$): its pair energy is $2E_+$, its charge $2N$ and its scalar density 0.
- **mismatch** (Chapter 10). In a shooting method, the amount by which the solution started from one boundary misses the condition at the other; a level is where it vanishes.
- **mixed-product rule** (Chapter 1). $(A\otimes B)(C\otimes D)=(AC)\otimes(BD)$ for tensor products.
- **mode amplitude** (Chapter 11). The column $u(t)$ of 16 complex numbers in the plane-wave ansatz $\Psi=V^{-1/2}e^{i\sum_jk_jx_j}u(t)$.
- **mode Hamiltonian** (Chapter 8). The $16\times16$ matrix $h_k$ with $i\partial_4u=h_ku$ for a plane wave of momentum $k$; its square is $E^2$ times the identity.
- **mode operators** (Chapter 8). The 16 operators $\Psi_k$ obtained from the field by a Fourier transform over the slice; they annihilate and create the quanta of momentum $k$.
- **modulus** (Chapter 1). $|z|=\sqrt{a^2+b^2}$ for $z=a+ib$.
- **momentum** (Chapter 5). $p=\partial L/\partial\dot q$, the canonical momentum; for a first-order Lagrangian it is a function of the coordinates (a constraint).
- **monomial** (Chapters 2 and 5). A product of generators, such as $\gamma^{a_1}\cdots\gamma^{a_k}$ with increasing indices (there are 256) or a product of distinct Grassmann generators.
- **N-representable** (Chapter 12). A density that comes from some antisymmetric $N$-particle wave function.
- **natural cubic spline** (Chapter 13). Piecewise cubic interpolation with continuous first and second derivatives and zero second derivatives at the ends; the Stage-4 solver interpolates its potentials this way.
- **NEC**: see null energy condition.
- **negative control** (Chapter 17). A computation that must fail, run to show that a check can detect the failure; for example the notebook's contraction of the spin connection, for which a divergence identity must fail.
- **Newton's constant** (Chapter 11). The coupling $G$ of gravity; in Chapter 11 a bound on its variation in time rules out one variant of the model.
- **Newton's method** (Chapter 10). Solving $g(x)=0$ by the iteration $x\leftarrow x-g(x)/g'(x)$, the zero of the tangent line; CVODE uses it (with the Jacobian matrix) for the implicit equations of BDF.
- **nilpotent** (Chapter 8). A matrix with a vanishing power, such as $h_k^2=0$; its exponential is a polynomial, and a mode with such a Hamiltonian grows linearly.
- **non-degenerate** (Chapter 8). A Hermitian form $f^\dagger Gh$ with $Gf=0$ only for $f=0$.
- **non-interacting $v$-representable** (Chapter 12). A density that is the ground-state density of some non-interacting system in some potential; the Kohn–Sham scheme assumes it.
- **nonlinear** (Chapter 12). Equations whose operator depends on the unknowns, like the Hartree–Fock and Kohn–Sham equations; they are solved by iteration.
- **norm** (Chapters 2 and 3). For a vector $u$ of $\mathbb R^{4,4}$ the number $n(u)=\eta(u,u)$, which can be negative ($u$ is a unit vector if $n(u)=\pm1$); for a split octonion the norm $N(x)=x\bar x$ of signature (4,4).
- **normal ordering** (Chapters 7 and 8). Writing products of creation and annihilation operators with the annihilation operators on the right (with the sign of each fermion exchange), which removes the constant contribution of the filled Dirac sea.
- **normalized** (Chapter 12). A state with $\langle\Psi|\Psi\rangle=1$.
- **null** (Chapter 1). A nonzero vector of zero length, $g(v,v)=0$.
- **null energy condition, NEC** (Chapter 9). $T(k,k)\ge0$ for every null vector $k$; for $k=e_4+e_0$ it reads $\rho+p_{(0)}\ge0$. In four dimensions it is $\rho+p\ge0$, which a phantom fluid violates (Chapter 11).
- **number operator** (Chapter 8). $N=b^\dagger b$, whose eigenvalues 0 and 1 count the fermions in a mode.
- **occupation numbers, occupation probabilities** (Chapter 12). The numbers $n_p\in\{0,1\}$ of particles in the orbitals of a determinant, and at a temperature the probabilities $f_a\in[0,1]$.
- **octonions** (Chapter 3). The eight-dimensional composition algebra that is neither commutative nor associative but alternative; the split octonions are its form with a norm of signature (4,4).
- **ODE**: see ordinary differential equation.
- **off shell, on shell** (Chapter 7). A statement holds off shell if it holds for every field configuration, and on shell if it holds only for solutions of the field equations.
- **one-body density matrix** (Chapter 12). $\rho=\sum_{a\in O}|\varphi_a\rangle\langle\varphi_a|$, with $\rho_{qp}=\langle a_p^\dagger a_q\rangle$; every expectation value in a Slater determinant is built from it (Wick's theorem).
- **onto** (Chapter 2). A map is onto if every element of the target is the image of some element; $\Lambda_{\mathrm t}$ maps Pin(4,4) onto O(4,4) (by the quoted Cartan–Dieudonné theorem).
- **OPEN** (Chapter 0). The status of a question that the project has not answered.
- **open interval** (Chapter 1). $(a,b)$, the set of real numbers $x$ with $a<x<b$.
- **operator** (Chapter 8). A rule that maps states to states, linear unless said otherwise.
- **orbital** (Chapters 7 and 12). A one-particle wave function, one of the factors of a Slater determinant; in the Kohn–Sham chapters one solution $\chi$ of the block equation, occupied by one quantum.
- **orbital relaxation** (Chapter 12). The change of the Kohn–Sham levels when a particle is moved; it is the difference between the Delta-SCF energy and the Kohn–Sham gap.
- **order** (Chapter 10). Of a differential equation, its highest derivative; of a numerical method, the power $p$ with a global error proportional to $h^p$.
- **ordinary differential equation** (Chapter 10). An equation for an unknown function of one variable and its derivatives.
- **orthogonal** (Chapters 1 and 2). Two vectors are orthogonal if their scalar product is zero; a real matrix $O$ is orthogonal if $O^TO=I$.
- **out of equilibrium** (Chapter 17). A system whose state is not the thermal equilibrium state; Sakharov's third condition, since in equilibrium the average baryon number vanishes.
- **the notebook** (Chapter 0). The Mathematica notebook `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` by Patrick L. Nash in the repository root, the starting point of the project.

### 20.6 Glossary: P to R

- **pairing symmetries** (Chapter 16). The exact maps of Chapter 15 that relate solutions with the masses $m$ and $-m$: the chirality map T1 and the mirror map T2.
- **pairing theorems T1, T2, T3** (Chapter 0; proved in Chapter 15). T1: the chirality map turns every configuration with $(m,\lambda)$ into one with $(-m,-\lambda)$ and reverses energy–momentum and charge; T2: the mirror map turns $(m,\lambda)$ into $(-m,\lambda)$ and keeps them; T3: the Kohn–Sham form of the pairing, a swap of the two components of every $2\times2$ block with transformed boundary conditions.
- **parity** (Chapters 2, 13 and 17). Of an element of Pin(4,4), whether it is a product of an even or an odd number of unit gammas; of a Kohn–Sham orbital, its behaviour under the brane reflection $y\to-y$ (the two parity sectors are the two boundary conditions at $y=0$); in particle physics (P), the reflection of space $\mathbf x\to-\mathbf x$.
- **part connected to 1** (Chapter 8). The part of a group that products of exponentials $\exp(\theta S^{ab})$ reach; for Spin(4,4) it is smaller than the whole group.
- **partial derivative** (Chapter 1). The derivative with respect to one variable while the others are kept fixed, $\partial_\mu=\partial/\partial x_\mu$.
- **particle, hole, particle–hole spectrum** (Chapter 12). An excitation moves a particle from an occupied level (leaving a hole) to an empty one; the list of the differences $\varepsilon_a-\varepsilon_i$ is the particle–hole spectrum, and in Chapter 13 the file `particle-hole.csv` of each run.
- **particle level, sea level** (Chapter 13). The classification of the Kohn–Sham levels of Chapter 13 by continuity from the free problem: a level whose free partner has $\varepsilon_{\mathrm{free}}\ge0$ is a particle level, otherwise a sea level; the exact zero modes count as particle levels by convention.
- **partner of mass $-M$** (Chapter 15). For a universe of mass $+M$, a configuration or Kohn–Sham state with the mass parameter $m=-M$.
- **path** (Chapter 5). A function $q(t)$ on a time interval; the action assigns a number to every path.
- **Pauli matrices** (Chapter 2). The Hermitian, traceless $2\times2$ matrices $\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}$, $\sigma_z=\mathrm{diag}(1,-1)$.
- **periodic boundary conditions** (Chapter 12). The requirement that wave functions repeat from one face of a box to the opposite one (a torus); the allowed momenta are then $2\pi/\ell$ times integers.
- **permanent** (Chapter 14). The determinant without signs, $g_{00}g_{11}+g_{01}g_{10}$ for a $2\times2$ matrix; Gaussian averages are permanents, fermion averages determinants.
- **permutation** (Chapter 1). A rearrangement of $0,\dots,n-1$; its sign is $(-1)^{\text{number of inversions}}$.
- **phantom** (Chapter 11). A fluid with $\rho>0$ and $w<-1$, that is $\rho+p<0$; it violates the null energy condition. The phantom epoch of EXP-3 is an artefact of the mean field.
- **phase** (Chapter 1). The angle $\varphi$ in the polar form $z=|z|e^{i\varphi}$; a phase factor is a number $e^{i\alpha}$.
- **physical momentum** (Chapter 11). $K_j=k_j/h_j$, the comoving momentum divided by the scale factor of its direction.
- **Pin(4,4), Spin(4,4)** (Chapter 2). The groups of products of unit gammas $\gamma(u_1)\cdots\gamma(u_k)$, and of products with an even number of factors; they act on spinors and are double covers of O(4,4) and SO(4,4).
- **plasma of thermal pairs** (Chapter 13). The Kohn–Sham gas at $T=m$, dominated by thermal particle–antiparticle pairs: the energy window of the solver then contains about 75000 levels, and the few added particles hardly change the energy and the entropy.
- **Poisson bracket** (Chapter 8). $\{F,G\}=\frac{\partial F}{\partial q}\frac{\partial G}{\partial p}-\frac{\partial F}{\partial p}\frac{\partial G}{\partial q}$; with it $\dot F=\{F,H\}$.
- **polar form** (Chapter 1). $z=|z|e^{i\varphi}$.
- **prescribed background** (Chapter 9). A metric that is taken as given rather than solved for; the primordial field is used this way.
- **pressure** (Chapter 5). The force per area exerted by a fluid, the spatial diagonal components $T^i{}_i$ of the energy–momentum tensor for an observer at rest; in eight dimensions there are seven principal pressures $p_{(i)}$.
- **primary constraints** (Chapter 8). The relations between momenta and fields that follow directly from a first-order Lagrangian, such as $\Pi_a-\sqrt{|g|}(\Psi^\dagger C\gamma^{x_4})_a\approx0$.
- **primary gamma matrices** (Chapter 2). The notebook's gammas $\gamma^a$ in block form, built from eight real $8\times8$ matrices $\tau_a$ and their partners $\bar\tau_a$; the gammas of the whole project.
- **primitive integer normalization, row-major order** (Chapter 3). The rule that fixes an intertwiner completely: its entries are scaled to integers without a common factor, with the first nonzero entry in row-major order (row 0 from left to right, then row 1, and so on) positive.
- **primordial field** (Chapter 9). The eight-dimensional metric of the notebook, in which 3-space inflates with $e^{a_4}$ and the three extra times deflate with $e^{-a_4}$; its static member (constant $a_4$) with a Z2 brane is the background of Chapters 13 to 15.
- **primordial window** (Chapter 11). The smooth switch-on and switch-off of the expansion used in EXP-1, $a_4'(t)=\tfrac A4(1+\tanh\frac{t-t_1}{\Delta})(1-\tanh\frac{t-t_2}{\Delta})$.
- **probability density** (Chapter 14). A function $p\ge0$ with $\int p=1$ that describes a random number; averages are $\langle g\rangle=\int g\,p$.
- **projector** (Chapter 1). A matrix with $P^2=P$; for example the chirality projectors $P_\mp=\tfrac12(1\mp\gamma^8)$.
- **proper densities, coordinate densities** (Chapter 13). Densities per unit proper volume, such as $n_p$ and $S_p$, and per unit $y$ and coordinate 3-volume, $n_c=e^{6Hy}n_p$; the total particle number is $N=\ell^3\int n_c\,dy$.
- **PROVED** (Chapter 0). The status of a statement derived in the book from stated assumptions, usually with an exact machine check.
- **Prüfer angle, Prüfer index** (Chapters 10 and 13). The angle $\theta$ in $a=r\cos\theta$, $b=-r\sin\theta$ of the two real components of an orbital; its end value increases with the energy, and the integer $n$ in the condition it must meet at $y=0$ numbers the levels (the Prüfer index), so that none is missed.
- **Pulay mixing**: see Anderson mixing.
- **$q$ vector** (Chapter 9). The Stage-2 document's name for the difference between the notebook's stored expressions and their Clifford-consistent rebuild (check `P_notebookCompare_qTermFromNonCliffordExtraTimeGammas`).
- **Q1, Q2, Q3** (Chapter 16). The three questions into which Chapter 16 splits the hypothesis of pair creation: is it allowed by the conservation laws, does it happen in a classical solution, and how likely is it.
- **quantization** (Chapter 8). The passage from classical fields to operators on a space of states; in this book canonical and formal (no regularization or renormalization).
- **quantum dynamics** (Chapter 16). The quantum theory that gives amplitudes and rates of transitions; it would be needed to say how likely the creation of a pair of universes is, and it is not computed.
- **quantum field** (Chapter 6). A field whose components are operators that create and annihilate particles and anticommute (for fermions).
- **quaternions** (Chapter 3). The four-dimensional associative but non-commutative algebra with $i^2=j^2=k^2=ijk=-1$.
- **random phase** (Chapter 14). A random complex amplitude whose distribution depends only on its modulus, so that all phases are equally likely.
- **rank** (Chapter 2). The largest number of independent elements in a list of matrices or rows, the dimension of their span.
- **real restriction** (Chapter 6). Setting the imaginary part of the commuting field of dirac16complex00 to zero; it gives the notebook's real Lagrangian $\mathrm{Lg}[\,]$ with the canonical connection.
- **redshift** (Chapter 11). $z$ with $1+z=1/a$, the stretching of wavelengths of light emitted when the scale factor was $a$.
- **reduced frequency** (Chapter 11). $\mu=M_{\mathrm{eff}}(a=1)/H_0$, a small stand-in (3 or 7) for the enormous ratio of a real fermion mass to the Hubble rate, used in EXP-3.
- **refined convergence** (Chapter 11). A checker test that reruns a program with ten times tighter tolerances and requires the errors to shrink or stay at an identified floor; the check `refinedConvergence`.
- **reflection** (Chapters 2 and 17). $R_u(v)=v-2\frac{\eta(u,v)}{\eta(u,u)}u$ for a unit vector $u$, which reverses $u$ and keeps its orthogonal hyperplane; in Chapter 17 a reflection $x_a\to r_ax_a$ of a set of coordinates.
- **regula falsi** (Chapter 10). The secant rule applied to the two ends of a bracket, keeping the part in which the sign changes; the Stage-4 solver uses its Illinois variant.
- **regulator** (Chapter 12). A small auxiliary number, such as $\kappa$ in $e^{-\kappa R}/R$, that makes an integral converge during a calculation and is sent to zero at the end.
- **relative residual, truncation estimate** (Chapter 10). The quantities with which the Mathematica notebook tests stored solutions: the largest difference between a derivative computed from the samples and the right-hand side, relative to the size of the right-hand side, and an estimate of the error of that derivative.
- **relative tolerance, rtol** (Chapter 10). The relative error per step that CVODE accepts; with the absolute tolerance it defines the weights of the error norm.
- **repeat-run byte identity** (Chapter 11). A checker test that reruns a program into a fresh folder and requires every file to be byte-identical; the check `repeatByteIdentity`.
- **report** (Chapter 0). A JSON file written by a verifier, with the named checks and their values `true` or `false`, the measurements and the hashes of the inputs.
- **representation** (Chapter 2). A homomorphism $\rho$ from a group to invertible matrices, $\rho(gh)=\rho(g)\rho(h)$; the group then acts on the columns.
- **representation theorem** (Chapter 2). Under Pin(4,4) the 16 components of a spinor form one irreducible block; under Spin(4,4) they split into two inequivalent irreducible halves of 8.
- **restricted, unrestricted Hartree–Fock**: see Hartree–Fock approximation.
- **reversed Krein metric** (Chapter 15). The matrix $-B$ in the anticommutator of the image field $\gamma^8\Psi$; it is the canonical structure of the Lagrangian $-\mathcal L_{-m,-\lambda}$.
- **Ricci tensor, Ricci scalar** (Chapter 4). $R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}$ and $R=g^{\mu\nu}R_{\mu\nu}$, contractions of the Riemann tensor.
- **Richardson's rule** (Chapter 10). An estimate of the error of a result computed with step $h$ from the difference to the result with step $h/2$, for a method of known order.
- **Riemann tensor** (Chapter 4). $R^\rho{}_{\sigma\mu\nu}$, the curvature: the change of a vector transported around a small loop.
- **right-hand side** (Chapter 10). The function $f$ in $Y'=f(t,Y)$; the cost of a solver is counted in its evaluations.
- **RK4**: see Runge–Kutta method.
- **rtol**: see relative tolerance.
- **Runge–Kutta method, RK4** (Chapter 10). The classical one-step method of order 4 with four evaluations of the right-hand side per step; used by the independent checkers of EXP-4 and EXP-5.
- **rustSolveIt** (Chapter 10). The repositories of the author's Rust translation of SUNDIALS (`sundials_rs`), which the setup scripts clone at a pinned commit into `vendor/rustSolveIt`; with the `win11` platform it is the numerical engine of Stages 3 to 5.

### 20.7 Glossary: S to Z

- **Sakharov's conditions** (Chapter 17). The three conditions for creating a baryon excess from a symmetric start: a process that violates baryon number, violation of C and of CP, and a departure from thermal equilibrium. The theory of this book fails the first, because its charge is exactly conserved (Chapter 17).
- **scalar** (Chapter 1). A single number, as opposed to a vector or matrix; in geometry a quantity that does not change under changes of coordinates or frames.
- **scalar density, $S$** (Chapter 6). $S=\bar\Psi\Psi=\Psi^\dagger C\Psi$, the frame-independent bilinear on which the mass term and the interaction depend.
- **scalar field** (Chapter 5). A field with one component that does not change under changes of frame, such as $\phi(x)$ with the Klein–Gordon Lagrangian.
- **scalar product** (Chapter 1). $\langle u,v\rangle=\sum_iu_i^\ast v_i$ for complex columns (the dot product for real ones).
- **scale factor** (Chapter 9). The number that multiplies a coordinate interval to give its proper length, for example $s^{1/6}e^{a_4}$ for the directions of 3-space in the primordial field.
- **Schrödinger equation** (Chapter 8). $i\partial_t\psi=H\psi$, the time evolution of a quantum state.
- **Schur's lemma** (Chapter 2). The commutant of an irreducible complex representation consists of multiples of the identity; used to prove that the gammas and the two halves are irreducible and inequivalent.
- **SEC**: see strong energy condition.
- **secant rule** (Chapter 10). A root finder that replaces the function by the straight line through the last two points and takes its zero as the next point.
- **second class** (Chapter 8). Constraints whose brackets with each other form an invertible matrix; they are solved with the Dirac bracket.
- **second quantization** (Chapter 6). Turning a classical field into operators that create and annihilate particles; in Chapter 12 the occupation-number description of many fermions.
- **self-consistency** (Chapter 12). The condition that the orbitals computed in a potential give back the density or density matrix from which the potential was built; reached by iteration.
- **shells** (Chapter 13). The groups of lattice momenta with the same $|\mathbf k|^2=\Delta k^2\,\nu$, $\nu=n_1^2+n_2^2+n_3^2$, whose Kohn–Sham levels coincide.
- **shift bound, window floor** (Chapter 15). The Stage-4 solver searches for levels above a fixed negative energy, the window floor ($-4.594$ for $m=1$); the shift bound $\max|M_{\mathrm{eff}}-m|+\max|v_x|$ limits how far the interaction can move a level, and the solver requires it to be at most the absolute value of the floor (its window premise).
- **shooting method** (Chapter 10). Solving a boundary-value or eigenvalue problem by integrating from one end with trial values and adjusting them until the condition at the other end holds.
- **signature** (Chapter 1). The numbers of positive and negative eigenvalues of a symmetric matrix, such as (4,4) for $\eta$; by Sylvester's law of inertia it does not depend on the basis.
- **signed permutation matrix** (Chapter 2). A matrix with exactly one nonzero entry $\pm1$ in every row and every column; it is orthogonal. The notebook's gammas are of this kind.
- **singularity** (Chapter 16). A time at which the volume of space goes to zero and the equations break down; the notebook's metric has none at $x_4=0$.
- **Slater determinant** (Chapter 12). The antisymmetric wave function $\det[\varphi_a(x_i)]/\sqrt{N!}$ of $N$ fermions in $N$ orthonormal orbitals.
- **slices** (Chapter 8). The seven-dimensional surfaces $x_4=\mathrm{const}$ on which the canonical quantization is set up.
- **smearing** (Chapter 12). Replacing integer occupations by Fermi–Dirac occupations of a small width to make a self-consistency loop converge; the result is an ensemble. One run of Chapter 13 (smeared $N=1016$) needs it.
- **smooth** (Chapter 1). Having continuous derivatives of every order.
- **sound speed** (Chapter 11). $c_s^2=dp/d\rho$; a negative $c_s^2$ makes small perturbations grow instead of oscillate.
- **source-free** (Chapter 15). Gravitational field equations with zero right-hand side; the chirality pair $\Psi_+,\gamma^8\Psi_+$ has zero total energy–momentum, so as the only source it leaves the source-free equations.
- **space-like, time-like** (Chapter 1). A vector with positive, respectively negative, squared length; in signature (4,4) the frame directions 0 to 3 are space-like and 4 to 7 time-like.
- **span** (Chapter 2). The set of all linear combinations of a list of vectors or matrices.
- **spectral theorem** (Chapter 1). A Hermitian matrix has real eigenvalues and an orthonormal basis of eigenvectors.
- **sphaleron** (Chapter 17). A process of the electroweak theory that violates baryon number at high temperature.
- **spin connection** (Chapter 4). The antisymmetric $\omega_{\mu ab}$ that makes the frame covariantly constant; see canonical spin connection. The notebook's contraction of it is not the canonical one (Chapter 4).
- **spin generators** (Chapter 2). $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$; their exponentials rotate spinors, and they commute with $\gamma^8$.
- **spinor** (Chapter 2). A column of 16 components on which the gammas and the spin transformations act; a spinor in eight dimensions has at least 16 components.
- **spinor connection, $\Omega_\mu$** (Chapter 4). $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}=\tfrac18\omega_{\mu ab}[\gamma^a,\gamma^b]$, the term in $D_\mu=\partial_\mu+\Omega_\mu$ that makes the derivative of a spinor covariant; its curvature is $F_{\mu\nu}$.
- **spinor field** (Chapter 6). A field that attaches to every point a column of 16 components measured in the local frame, changing by a spin transformation when the frame is turned.
- **spinor norm** (Chapter 2). $N(g)=n(u_1)\cdots n(u_k)=\pm1$ for $g=\gamma(u_1)\cdots\gamma(u_k)$ in Pin(4,4), from $g^TCg=(-1)^kN(g)C$.
- **split octonions** (Chapter 3). The eight-dimensional composition algebra with a norm of signature (4,4); the notebook's $\tau_a$ are multiplications by split octonions.
- **square matrix** (Chapter 1). A matrix with as many rows as columns.
- **stability region, stable** (Chapter 10). A method is stable for $z=h\lambda$ if its amplification factor has $|R(z)|\le1$; the set of such $z$ is its stability region.
- **standard basis** (Chapter 1). The vectors $e_0,\dots,e_{n-1}$ of $\mathbb R^n$, $e_k$ having the component 1 in place $k$ and 0 elsewhere.
- **standard model of cosmology, $\Lambda$CDM** (Chapter 11). The model with radiation, ordinary matter, cold dark matter and a cosmological constant ($w=-1$), the reference against which the experiments of Chapter 11 compare a varying $w$.
- **start value** (Chapter 10). The value of the solution at the initial time of an initial-value problem.
- **state vector** (Chapter 10). The column $Y(t)$ of all unknowns of a system of ordinary differential equations.
- **static member** (Chapter 13). The member of the primordial family with constant $a_4=a_{4,0}$, a metric that does not change in time; the background of the Kohn–Sham states.
- **stationary** (Chapter 5). An action is stationary on a path if it does not change to first order under every variation with fixed end points.
- **stationary state** (Chapter 12). An eigenstate of the Hamiltonian; its time dependence is only a phase.
- **statistics sign, $s$** (Chapter 6). $s=+1$ for commuting and $s=-1$ for Grassmann components, produced by reordering factors, as in $\Psi^TY\Phi^\ast=s\,\Phi^\dagger Y^T\Psi$; it decides the sign of exchange (Chapter 14) and which charge conjugations are symmetries (Chapter 17).
- **step size** (Chapter 10). The distance $h$ between two consecutive points of a numerical solution; CVODE chooses it adaptively.
- **stiff** (Chapter 10). A problem with components that decay much faster than the solution of interest changes; explicit methods then need steps as small as the fastest decay time.
- **stop time** (Chapter 10). A time beyond which CVODE must not integrate; every integration of the project sets it to its last output time.
- **strength** (Chapter 13). For a configuration $(m,L,N)$, the largest first-order size of the pseudo-potential per unit coupling in the free ground state; the couplings are $\hat\lambda_1=0.1/\text{strength}$ and $\hat\lambda_2=1/\text{strength}$.
- **strong energy condition, SEC** (Chapter 9). $(T_{\mu\nu}-g_{\mu\nu}T/(D-2))u^\mu u^\nu\ge0$ for time-like $u$, equivalent through the Einstein equations to $R_{\mu\nu}u^\mu u^\nu\ge0$.
- **subgroup** (Chapter 2). A subset of a group that is itself a group under the same product.
- **subspace** (Chapter 2). A set of vectors or matrices that contains every linear combination of its elements; the span of any list is one.
- **SUNDIALS** (Chapter 10). A library of solvers for differential equations from the Lawrence Livermore National Laboratory; CVODE is its initial-value solver, used here in the Rust translation `sundials_rs`.
- **Sylvester's law of inertia** (Chapter 1). The numbers of positive, negative and zero eigenvalues of a symmetric matrix do not change under $A\to P^TAP$ with invertible $P$.
- **symmetric** (Chapter 1). A square matrix with $A^T=A$.
- **symmetric difference** (Chapter 2). $A\triangle B$, the set of indices in exactly one of $A$ and $B$; $\gamma_A\gamma_B=\pm\gamma_{A\triangle B}$.
- **symmetrized** (Chapter 6). The kinetic term with the derivative acting once on $\Psi$ and once on $\bar\Psi$ with opposite signs, which makes the Lagrangian real without a factor $i$.
- **symmetry of the dynamics** (Chapter 17). A transformation that turns every possible history into another possible history running in the same direction of time.
- **system** (Chapter 10). Several ordinary differential equations for several unknown functions, collected in a state vector.
- **T1, T2, T3**: see pairing theorems, chirality map, mirror map.
- **tangent CPL parameters** (Chapter 11). The values $w_0=w(1)$ and $w_a=-dw/da$ at $a=1$ of a model's equation of state, compared with the CPL fits of supernova data.
- **tensor** (Chapter 4). An object with upper and lower indices whose components transform with one factor $\partial x'/\partial x$ or $\partial x/\partial x'$ per index.
- **tensor product, Kronecker product** (Chapter 1). $A\otimes B$, the block matrix with blocks $a_{ij}B$.
- **thermal particle–antiparticle pairs** (Chapter 13). At $T>0$ particle and sea levels have fractional weights; the gas contains pairs that do not change $N$.
- **Thomas–Fermi model** (Chapter 12). The 1927 approximation of the kinetic energy by that of a uniform gas, $\int C_Fn^{5/3}$; too crude, which is why Kohn–Sham keeps the kinetic energy exact.
- **3-space, time, extra times, hidden space** (Chapter 9). The coordinates $x_1,x_2,x_3$ (ordinary space), $x_4$ (the time of evolution), $x_5,x_6,x_7$ (the extra times) and $x_0$ (the hidden space).
- **tip** (Chapter 9). The end $\zeta\to-\infty$ of the hidden direction of the static primordial field, where the warp factor goes to 0; the Kohn–Sham problem cuts it off at $y=-L$ (Chapter 13).
- **total derivative, total divergence** (Chapter 5). A term $\frac{d}{dt}F$ or $\partial_\mu V^\mu$; added to a Lagrangian it does not change the field equations.
- **totally antisymmetric part** (Chapter 6). The part of $\omega_{cab}$ antisymmetric in all three indices; only it enters the Lagrangian, so a diagonal vielbein contributes no spin connection to it.
- **trace** (Chapter 1). $\mathrm{tr}A=\sum_iA_{ii}$; $\mathrm{tr}(AB)=\mathrm{tr}(BA)$.
- **traceless** (Chapter 2). A matrix with trace zero; every gamma monomial except the unit is traceless.
- **transformation law of the metric** (Chapter 1). $g'_{\alpha\beta}=\frac{\partial x^\mu}{\partial x'^\alpha}\frac{\partial x^\nu}{\partial x'^\beta}g_{\mu\nu}$, in matrix form $g'=J^TgJ$, under a change of coordinates.
- **transformed boundary condition** (Chapter 15). The tip condition of the $-M$ universe with the bag angle $\pi-\theta$ instead of $\theta$, needed for T3; with the untransformed condition the $-M$ universe is the control.
- **transition state** (Chapter 12). Slater's estimate of an excitation energy from the Kohn–Sham levels with half a particle moved.
- **transpose** (Chapter 1). $A^T$, the matrix with rows and columns exchanged.
- **trapezoidal rule** (Chapter 10). The implicit method $Y_{n+1}=Y_n+\tfrac h2(f_n+f_{n+1})$, with $R(z)=(1+z/2)/(1-z/2)$.
- **triality** (Chapter 2). The symmetry of Spin(4,4) that permutes the vector representation and the two spinor halves; quoted, not used.
- **twin** (Chapters 6 and 19). The PowerShell or the Bash version of a gate, which run the same steps and print the same final line (Chapter 19); for checks, the sympy check `S5_x` that repeats the Wolfram check `C00_x` or `PAIR_x` with the same ending (Chapter 6).
- **twisted adjoint action** (Chapter 2). The map $\Lambda_{\mathrm t}$ from Pin(4,4) to O(4,4) defined by $\alpha(g)\gamma(v)g^{-1}=\gamma(\Lambda_{\mathrm t}(g)v)$ with $\alpha(g)=(-1)^{|g|}g$; the untwisted map $\Lambda_{\mathrm u}$ omits $\alpha$. The kernel of $\Lambda_{\mathrm t}$ is $\{\pm1\}$.
- **U(1) charge 2** (Chapter 17). The property of a term such as $\Psi^TM\Psi$ that is multiplied by $e^{2i\alpha}$ under $\Psi\to e^{i\alpha}\Psi$; such a term violates charge conservation.
- **U(1) symmetry, phase symmetry** (Chapter 7). The invariance of the Lagrangian under $\Psi\to e^{i\alpha}\Psi$ with a constant $\alpha$; its Noether current is the conserved current and its charge the U(1) charge (Theorem M1 of Chapter 17).
- **ulp** (Chapter 10). The unit in the last place, the gap between a double and the next one; $\mathrm{ulp}(1)=2.2\times10^{-16}$.
- **ultrahyperbolic** (Chapter 5). A wave equation with more than one time-like direction, such as the Klein–Gordon equation in signature (4,4); its initial-value problem is not well-posed.
- **ultrastatic** (Chapter 18). A diagonal metric with $g_{44}=-1$ none of whose entries depends on $x_4$; the static member of the primordial field is one.
- **uniform gas** (Chapter 12). Infinitely many particles at constant density; its exchange and correlation energies give the local density approximation.
- **unit** (Chapter 3). An element $1$ with $1x=x1=x$ for every $x$ of an algebra.
- **unit normal** (Chapter 9). The unit vector $n=\partial_y$ orthogonal to a surface $y=\mathrm{const}$.
- **unit vector** (Chapter 2). A vector $u$ with $\eta(u,u)=\pm1$; its gamma $\gamma(u)$ is invertible.
- **unitary** (Chapter 1). A complex matrix with $U^\dagger U=I$; it preserves scalar products. An antiunitary operator does so up to complex conjugation (Chapter 17).
- **unitary type, antiunitary type** (Chapter 17). A map of the field is of unitary type if it preserves the canonical anticommutation relations linearly and of antiunitary type if it does so antilinearly; passing the test is necessary, not sufficient, for an operator that implements the map.
- **universal functional** (Chapter 12). $F[n]=\min_{\Psi\to n}\langle\Psi|\hat T+\hat W|\Psi\rangle$, the same for every external potential.
- **universe of mass $+M$** (Chapter 15). A configuration, solution or Kohn–Sham state with the mass parameter $m=+M$; its partner of mass $-M$ has $m=-M$.
- **untransformed control** (Chapter 15). The $-M$ universe computed with the Stage-4 bag condition $\theta=0$ instead of the transformed one; it shows that the transformation of the boundary condition matters.
- **vacuum** (Chapter 8). The state annihilated by all annihilation operators; in the good sector the filled Dirac sea with no particles or antiparticles.
- **variation** (Chapter 5). A small change $\epsilon\xi(t)$ of a path (or of a field) that vanishes at the end points.
- **vector** (Chapter 1). A column of numbers, or an element of a vector space; in geometry an object with an upper index.
- **vielbein**: see frame.
- **vielbein postulate** (Chapter 4). The condition that the frame is covariantly constant, $\partial_\mu e_\nu{}^a-\Gamma^\lambda{}_{\mu\nu}e_\lambda{}^a+\omega_\mu{}^a{}_be_\nu{}^b=0$; it determines the canonical spin connection.
- **volume element** (Chapter 1). $\sqrt{|g|}\,d^8x$, the proper volume of a small coordinate box.
- **warped, warp factor** (Chapter 9). A metric in which several directions carry a common factor that depends on another coordinate, such as $e^{2H\zeta}$ in the static primordial field.
- **wave function** (Chapter 6). A complex function whose squared modulus gives probabilities; in Chapter 12 the many-body wave function $\Psi(x_0,\dots,x_{N-1})$.
- **weak energy condition, WEC** (Chapter 9). $T(u,u)\ge0$ for every time-like $u$; for $u=e_4$ it is $\rho\ge0$.
- **WEC**: see weak energy condition.
- **weighted root-mean-square norm** (Chapter 10). $\|e\|=\sqrt{\frac1n\sum_c(e_c/(\mathrm{rtol}|Y_c|+\mathrm{atol}))^2}$; CVODE accepts a step if it is at most 1.
- **well-posed** (Chapter 8). An initial-value problem whose solution exists, is unique and depends continuously on the data (Hadamard); the full dirac16complex problem is not.
- **Wheeler–DeWitt equation** (Chapters 16 and 18). The equation of quantum cosmology for a wave function of the geometry and the matter fields; Chapter 18 derives a one-variable version for a reduced model of the primordial family, and no program of the repository solves it.
- **Wick's theorem** (Chapter 12). In a Slater determinant or a non-interacting thermal ensemble every expectation value is a sum of products of the one-body density matrix.
- **win11** (Chapter 10). The platform name with which `scripts/setup_solver` installs the pinned engine; the byte identity of the committed numerical files is established with it on Windows 11 and on Ubuntu 24.04.
- **window** (Chapter 8). The interval of times, away from the turning point, over which EXP-5 compares the growth of a mode with the WKB estimate.
- **WKB approximation** (Chapter 8). The approximation (after Wentzel, Kramers and Brillouin) that treats a slowly changing coefficient as constant over the local growth or oscillation time; it estimates the growth of the extra-time modes of EXP-5.
- **Z2 brane** (Chapter 9). The surface $y=0$ at which two mirror copies of the static primordial patch are glued; a choice of model, not a derived result, with a kink in the warp factor that requires a source on the brane.
- **Z2-symmetric** (Chapter 15). A configuration with $\Psi(y)=\pm\gamma^0\Psi(-y)$; it solves the field equations on both sides of the brane with one mass function exactly when the mass function is odd, $m(-y)=-m(y)$, where $\Psi\ne0$.
- **zero mode** (Chapters 8 and 13). In Chapter 8, the part of the field that does not depend on $x_5,x_6,x_7$; in Chapter 13, the Kohn–Sham level $\varepsilon=0$ with $\chi=(e^{My},0)^T$ at zero momentum, localized at the brane.
- **zero vector** (Chapter 1). The vector with all components zero.

### 20.8 Symbols and notation

The table lists the symbols that are used in more than one chapter, with the chapter that introduces them. Indices are counted from 0 throughout the book (Chapter 0): coordinates $x_0,\dots,x_7$, frame directions $a,b=0,\dots,7$, spinor components $0,\dots,15$.

| Symbol | Meaning | Chapter |
| --- | --- | --- |
| $\eta_{ab}$ | the flat metric of signature (4,4): $\eta_{aa}=+1$ for $a\le3$ (space-like), $\eta_{aa}=-1$ for $a\ge4$ (time-like), zero off the diagonal | 1 |
| $x_0$; $x_1,x_2,x_3$; $x_4$; $x_5,x_6,x_7$ | the hidden space; ordinary 3-space; the time of evolution; the three extra times | 9 |
| $\gamma^a$, $a=0,\dots,7$ | the primary gamma matrices, real $16\times16$, $\{\gamma^a,\gamma^b\}=2\eta^{ab}$ | 2 |
| $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7$ | the chirality, $\mathrm{diag}(-I_8,I_8)$ in the notebook basis | 2 |
| $P_\mp=\tfrac12(1\mp\gamma^8)$ | the projectors on the two halves of chirality $\mp1$ | 2 |
| $C=\gamma^0\gamma^1\gamma^2\gamma^3$ | the charge matrix, the notebook's $\sigma_{16}$; real, symmetric, $C^2=1$ | 2 |
| $B=-iC\gamma^4$ | Hermitian, $B^2=1$, signature (8,8); the matrix of the canonical anticommutator and of the Krein form | 2, 8 |
| $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$ | the spin generators | 2 |
| $\Psi$, $\bar\Psi=\Psi^\dagger C$ | the 16-component field and its Dirac adjoint | 6 |
| $s=\pm1$ | the statistics sign: $+1$ for commuting (dirac16complex00), $-1$ for Grassmann (dirac16complex) components | 6 |
| $S=\bar\Psi\Psi$ | the scalar density | 6 |
| $m$, $M$ | the mass of the Lagrangian and the notebook's mass number, $m=-HM$ | 5 |
| $\lambda$, $U(S)=\tfrac\lambda2S^2$ | the coupling and the contact interaction | 6, 13 |
| $M_{\mathrm{eff}}=m+\lambda S$ | the effective mass of the mean field | 11 |
| $\hat\lambda=\lambda m^6$, $\hat\lambda_1$, $\hat\lambda_2$ | the dimensionless coupling of Stage 4 and its two strengths | 13 |
| $e_\mu{}^a$, $g_{\mu\nu}$, $\sqrt{\lvert g\rvert}$ | the vielbein, the metric $g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b$ and the volume factor | 4 |
| $\Gamma^\rho{}_{\mu\nu}$, $\omega_{\mu ab}$, $\Omega_\mu$, $D_\mu$ | the Christoffel symbols, the spin connection, the spinor connection and the spinor covariant derivative $D_\mu=\partial_\mu+\Omega_\mu$ | 4 |
| $R^\rho{}_{\sigma\mu\nu}$, $R_{\mu\nu}$, $R$, $G_{\mu\nu}$ | the Riemann tensor, the Ricci tensor, the Ricci scalar and the Einstein tensor | 4 |
| $\kappa$ | the gravitational coupling of the eight-dimensional Einstein equations $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ ($\kappa_4$ in four dimensions, Chapter 11) | 4 |
| $\Theta^\mu{}_\nu$, $T^\mu{}_\nu$ | the canonical and the metric energy–momentum tensors | 5, 7 |
| $\rho$, $p_{(i)}$, $w$ | the energy density, the pressures and the equation-of-state parameter | 5 |
| $j^\mu$, $Q$ | the conserved current and the charge | 5, 7 |
| $H$, $z=6Hx_0$, $t=Hx_4$, $a_4(t)$ | the notebook's inverse length, its hidden angle and dimensionless time, and the free function of the primordial field | 9 |
| $\zeta$, $y$ | the proper hidden coordinate of the static primordial field (called $y$ from Chapter 13 on) | 9, 13 |
| $L$, $\theta$ | the tip cutoff $y=-L$ and the bag angle of the tip condition | 13 |
| $h_k$, $E$ | the mode Hamiltonian of a plane wave and its energy, $h_k^2=E^2$ | 8 |
| $j=\pm1$, $\beta=\pm1$ | the block type of a Kohn–Sham block and its Krein sign | 13, 14 |
| $N$, $T$, $\mu$, $f$ | the particle number, the temperature, the chemical potential and the Fermi–Dirac occupation | 12 |
| $n_p$, $S_p$; $n_c$, $S_c$ | the proper and the coordinate number and scalar densities | 13 |
| $E_H$, $E_x$, $\Delta_{KS}$ | the Hartree energy, the exchange energy and the Kohn–Sham gap | 12 |
| $h$, rtol, atol | the step size and the relative and absolute tolerances of a numerical integration | 10 |
| $a$, $z$, $H_0$, $w_0$, $w_a$ | in cosmology: the scale factor, the redshift, today's Hubble rate and the CPL parameters (the redshift $z$ is not the angle $z$ of Chapter 9) | 11 |
| T1, T2, T3 | the three pairing theorems | 15 |
| M1 to M6, H1 to H3 | the results of the matter–antimatter analysis and the three hypotheses of the conditional scenario M5 | 17 |
| $\eta$ (in Chapter 17) | the baryon-to-photon ratio, not the flat metric | 17 |

### 20.9 How the index of checks was made, and how to look up a check yourself

**What is indexed.** A verifier writes its report as a JSON file with an entry `checks`, which maps every check name to `true` or `false` (Section 0.8); the Rust programs write the same kind of entry into the `summary.json` of each run folder. Sections 20.10 to 20.14 list every check name that Chapters 0 to 19 cite, in running text, in code or in a listing, together with the committed file or files whose entry `checks` contains it, its value there, and the chapters that cite it. Three kinds of name are indexed:

- a single check, such as `ALG_clifford`;
- a family written with a final `*`: `PAIR_T1krein_*` means every check whose name begins with `PAIR_T1krein_`, and `*_energy_from_rho` every Rust self-check whose name ends with `_energy_from_rho` (one per run); the column "Value" then gives the number of checks in the family and whether all of them are true;
- a name whose ending the text writes separately, such as `GEO_vielbeinPostulate_G1` and `_G2`, is indexed under its full names.

Names of **measurements** (numbers and tables that a report records next to its checks, such as `ALG_tauEqualsLeftMultiplicationPerIndex` in Chapter 3 or `canonical_eigenvalues_detail` in Chapter 19) are not checks and are not indexed; nor are the names of keys of theory files, such as `fieldEquations`. A name that the text uses only as a prefix of a whole stage, such as `S5_` in "the `S5_` twins", is not indexed either; the prefixes are explained at the head of each section.

**How it was verified.** The index was produced by a short program that reads every committed JSON file under `artifacts/`, collects the names in their entries `checks`, and then searches the chapter files for these names. Every row of Sections 20.10 to 20.14 therefore names a check that exists, with the value shown, in the committed file shown. The program also listed the names in the chapters that look like check names but occur in no entry `checks`; each of them was read in its sentence and found to be a measurement, a comparison recorded inside a report or a name inside a program, and none of them is called a check by the text. The reports were those of the commit named in Section 20.15.

**Looking up a check yourself.** The following command prints every committed file whose entry `checks` contains a given name, with its value. In PowerShell and in Bash alike (only the quoting of Section 19.3 matters, and the lines between the double quotes are the same):

```
python -c "
import json, pathlib, sys
for p in sorted(pathlib.Path('artifacts').rglob('*.json')):
    d = json.loads(p.read_text(encoding='utf-8'))
    c = d.get('checks') if isinstance(d, dict) else None
    if isinstance(c, dict) and sys.argv[1] in c:
        print(p.as_posix(), c[sys.argv[1]])
" ALG_clifford
```

Run from the root of the repository, it printed

```
artifacts/dirac16complex/arbitrary-field/python-algebra-report.json True
artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json True
```

in both shells within two seconds; with `canonical_eigenvalues` instead of `ALG_clifford` it printed the one line `artifacts/dirac16complex/kohn-sham/python-check-report.json False`. Nested entries `checks` inside a report (the fits of `numerics/exp3/fits.json`) are not found by this short command; the index includes them.

### 20.10 Index of checks: Stage 1, the field in an arbitrary gravitational field

The reports of Stage 1 lie in `artifacts/dirac16complex/arbitrary-field/`. The prefixes are `ALG_` (algebra), `GEO_` (geometry), `LAG_` (Lagrangian), `EMT_` (energy–momentum tensor), `QNT_` (quantization), `GR_` (Grassmann demonstration) and `NEG_` (negative controls); the endings `_G1` and `_G2` name the two test geometries (Chapter 4). The table has 90 rows.

| Check | Committed report | Value | Cited in chapters |
| --- | --- | --- | --- |
| `ALG_CAnticommutatorGammaSSymmetric` | `arbitrary-field/python-geometry-report.json` | true | 5 |
| `ALG_CCommutatorGammaSAntisymmetric` | `arbitrary-field/python-geometry-report.json` | true | 5 |
| `ALG_chargeFormB` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 2, 8, 18 |
| `ALG_chargeMatrix` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 0, 2, 3, 5 |
| `ALG_chirality` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json` | true | 0, 2, 3 |
| `ALG_clifford` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json` | true | 0, 2, 3, 5 |
| `ALG_cliffordPictureIntertwiner` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json` | true | 0, 2, 3 |
| `ALG_expression1` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json` | true | 0, 2, 3, 5 |
| `ALG_faithful` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json` | true | 2, 4 |
| `ALG_fixtureAgreement` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json` | true | 2, 3 |
| `ALG_gamma8Map` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 6, 15, 16, 18 |
| `ALG_gammaTransposeSymmetry` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json` | true | 2, 5 |
| `ALG_grassmannLemmas` | `arbitrary-field/wolfram-geometry-report.json` | true | 5 |
| `ALG_invariantForms` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 8, 18 |
| `ALG_octonionPictureIntertwiner` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json` | true | 0, 3 |
| `ALG_pinIrreducibleComplex` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 2, 4 |
| `ALG_pinLiftCharacter` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 2, 6 |
| `ALG_SabGammaCommutator` | `arbitrary-field/python-geometry-report.json` | true | 2, 4 |
| `ALG_spinDecomposition` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 2 |
| `ALG_spinTransposeProperties` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json` | true | 2, 4, 5 |
| `ALG_wolframAgreement` | `arbitrary-field/python-algebra-report.json` | true | 2, 3, 19 |
| `EMT_conservation_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 7 |
| `EMT_conservation_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `EMT_homogeneousReduction` | `arbitrary-field/python-geometry-report.json` | true | 0, 7, 11 |
| `EMT_homogeneousReduction_G3` | `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 7, 11 |
| `EMT_homogeneousTimeSpaceVanishesOnShell_G3` | `arbitrary-field/python-geometry-report.json` | true | 7 |
| `EMT_onshellLagrangianSUprimeMinusU_G1` | `arbitrary-field/python-geometry-report.json` | true | 7 |
| `EMT_onshellLagrangianSUprimeMinusU_G2` | `arbitrary-field/python-geometry-report.json` | true | 7 |
| `EMT_symmetricHermitian_G1` | `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 7 |
| `EMT_symmetricHermitian_G2` | `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `EMT_trace_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 7 |
| `EMT_trace_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `EMT_traceOffShellIdentity_G1` | `arbitrary-field/python-geometry-report.json` | true | 7 |
| `EMT_variation` | `arbitrary-field/python-geometry-report.json` | true | 7 |
| `EMT_variation_G3` | `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `GEO_anticommutatorGammaOmegaVanishesDiagonal_G2` | `arbitrary-field/python-geometry-report.json` | true | 4, 5, 6 |
| `GEO_curvature_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4 |
| `GEO_curvature_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4 |
| `GEO_diagonalSlashFormula_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4 |
| `GEO_diagonalSlashFormula_G3` | `arbitrary-field/python-geometry-report.json` | true | 4 |
| `GEO_divergenceIdentity_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 4, 5 |
| `GEO_divergenceIdentity_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 4, 5 |
| `GEO_frameNondegenerate_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4 |
| `GEO_gammaCovariantConstancy_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 0, 4, 5 |
| `GEO_gammaCovariantConstancy_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 0, 4, 5 |
| `GEO_lichnerowiczConstantSameG1G2` | `arbitrary-field/python-geometry-report.json` | true | 4 |
| `GEO_lichnerowicz_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4, 7 |
| `GEO_lichnerowicz_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4, 7 |
| `GEO_notebookContractionFails_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 0, 4 |
| `GEO_notebookContractionFails_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 0, 4 |
| `GEO_omegaAntisymmetry_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4 |
| `GEO_omegaAntisymmetry_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4 |
| `GEO_primordialInvariants_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4 |
| `GEO_sqrtgSquaredEqualsDetg_G1` | `arbitrary-field/python-geometry-report.json` | true | 4 |
| `GEO_vielbeinPostulate_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4 |
| `GEO_vielbeinPostulate_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json` | true | 4 |
| `GEO_wolframAgreement` | `arbitrary-field/python-geometry-report.json` | true | 19 |
| `GR_bilinearOnlyAntisymmetricPartSurvives` | `arbitrary-field/grassmann-demo-report.json` | true | 5 |
| `GR_complexPsiEquation` | `arbitrary-field/grassmann-demo-report.json` | true | 7 |
| `GR_complexQuarticEL` | `arbitrary-field/grassmann-demo-report.json` | true | 0, 7 |
| `GR_conjugationRules` | `arbitrary-field/grassmann-demo-report.json` | true | 5 |
| `GR_currentHermitian` | `arbitrary-field/grassmann-demo-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 7, 8 |
| `GR_emtHermitian` | `arbitrary-field/grassmann-demo-report.json` | true | 7 |
| `GR_kineticSymmetricMatrixContrast` | `arbitrary-field/grassmann-demo-report.json` | true | 5 |
| `GR_kineticTotalDerivativeReal` | `arbitrary-field/grassmann-demo-report.json` | true | 5 |
| `GR_lagrangianHermitian` | `arbitrary-field/grassmann-demo-report.json` | true | 6 |
| `GR_massTermVanishesReal` | `arbitrary-field/grassmann-demo-report.json` | true | 5 |
| `GR_notebookLgELTrivial` | `arbitrary-field/grassmann-demo-report.json` | true | 5 |
| `GR_notebookLgPureDivergence` | `arbitrary-field/grassmann-demo-report.json` | true | 0, 5 |
| `GR_quarticTermPolynomial` | `arbitrary-field/grassmann-demo-report.json` | true | 5 |
| `GR_scalarBilinearHermitian` | `arbitrary-field/grassmann-demo-report.json` | true | 5 |
| `GR_unsymmetrizedKineticNotHermitian` | `arbitrary-field/grassmann-demo-report.json` | true | 6 |
| `LAG_eulerLagrangePsibar_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 7 |
| `LAG_eulerLagrangePsibar_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `LAG_eulerLagrangePsi_G1` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 7 |
| `LAG_eulerLagrangePsi_G2` | `arbitrary-field/python-geometry-report.json`, `arbitrary-field/wolfram-geometry-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `LAG_hermiticity_G1` | `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `LAG_hermiticity_G2` | `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `LAG_localSpinInvariance_G1` | `arbitrary-field/wolfram-geometry-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 4, 6 |
| `LAG_localSpinInvariance_G2` | `arbitrary-field/wolfram-geometry-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 4, 6 |
| `LAG_notebookLgGrassmannTrivial_G1` | `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 5 |
| `LAG_notebookLgGrassmannTrivial_G2` | `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 5 |
| `NEG_notebookConnectionDetected_G2` | `arbitrary-field/wolfram-geometry-report.json` | true | 4 |
| `QNT_canonicalMomentum_G1` | `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 8 |
| `QNT_canonicalMomentum_G2` | `arbitrary-field/wolfram-geometry-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 8 |
| `QNT_currentHermiticity` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 7, 8 |
| `QNT_curvedAnticommutatorMatrix` | `arbitrary-field/wolfram-algebra-report.json` | true | 8 |
| `QNT_flatModeHamiltonian` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 8, 18 |
| `QNT_kreinSignature` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 0, 7, 8, 18 |
| `QNT_unitaryAndKreinSubgroups` | `arbitrary-field/python-algebra-report.json`, `arbitrary-field/wolfram-algebra-report.json` | true | 2, 8 |

### 20.11 Index of checks: Stage 2, the primordial field

The reports of Stage 2 lie in `artifacts/dirac16complex/primordial-field/`; every name begins with `P_`. The table has 70 rows.

| Check | Committed report | Value | Cited in chapters |
| --- | --- | --- | --- |
| `P_a4linear` | `primordial-field/python-primordial-report.json` | true | 4, 19 |
| `P_a4linear_cell150AlternativesRhoNegative` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_a4linear_values` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_blocks_fourBlocksOfFour` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_blocks_matchNotebookSets` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_christoffel` | `primordial-field/python-primordial-report.json` | true | 4 |
| `P_christoffel_closedForms512` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_christoffel_count` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_einstein` | `primordial-field/python-primordial-report.json` | true | 0, 4 |
| `P_einstein_energyConditionForms` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_einstein_GmixedClosedForms` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_einstein_notebookCell583` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_einstein_notebookCell584` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_einstein_offDiagonalZero` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_einstein_R44` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_einstein_requiredSource` | `primordial-field/wolfram-primordial-report.json` | true | 0, 9, 18 |
| `P_einstein_rhoRequiredNegative` | `primordial-field/wolfram-primordial-report.json` | true | 0, 4, 9, 18 |
| `P_einstein_ricciScalar` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_gammaConst_divergenceIdentity` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_gammaConst_divergenceIdentityFailsNotebookContraction` | `primordial-field/wolfram-primordial-report.json` | true | 4 |
| `P_gammaConst_DmuGammaNuZero64` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_gammaConst_notebookContractionClosedForms` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_gammaConst_notebookContractionFails` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_metric` | `primordial-field/python-primordial-report.json` | true | 0 |
| `P_metric_detG_equals_plus_cos2z` | `primordial-field/wolfram-primordial-report.json` | true | 0, 1, 4, 9 |
| `P_metric_notebookCell1060Det` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_metric_signature44` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_metric_sqrtAbsDetG_cosz` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_metric_vielbeinProduct` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_modes_exactReduction` | `primordial-field/wolfram-primordial-report.json` | true | 11 |
| `P_notebookCompare_*` | `primordial-field/wolfram-primordial-report.json` | all 16 true | 9 |
| `P_notebookCompare_cell1137Reproduced16of16` | `primordial-field/wolfram-primordial-report.json` | true | 0, 9 |
| `P_notebookCompare_commutingQ1DropsOutCliffordGammas` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_notebookCompare_correctVsStoredDifferOnlyByQ` | `primordial-field/wolfram-primordial-report.json` | true | 0, 9 |
| `P_notebookCompare_eLaztCell1096` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_notebookCompare_literalRebuildResidualIsExactlyQTerms` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_notebookCompare_qOnlyInYZ0to7` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_notebookCompare_qTermFromNonCliffordExtraTimeGammas` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_notebookCompare_qVectorIs2HqAtCell1079` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_notebookCompare_reconstructedGamma5NotClifford` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_notebookCompare_reconstructedGammaForm` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_notebookCompare_reconstructionReproducesStoredEla` | `primordial-field/wolfram-primordial-report.json` | true | 0, 9 |
| `P_notebookCompare_relabelCell1111` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_notebookCompare_storedEla16` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_Omega` | `primordial-field/python-primordial-report.json` | true | 0 |
| `P_Omega_closedForms` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_Omega_contractDiagonalFormula` | `primordial-field/wolfram-primordial-report.json` | true | 4 |
| `P_Omega_gammaSlash3Hgamma0` | `primordial-field/wolfram-primordial-report.json` | true | 0, 4, 9 |
| `P_Omega_OmegaGammaAndAnticommutator` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_Omega_slashA4Independent` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_source` | `primordial-field/python-primordial-report.json` | true | 0 |
| `P_source_einsteinTransverseDifferenceIs2H2a4pp` | `primordial-field/wolfram-primordial-report.json` | true | 0, 9, 18 |
| `P_source_realKDiagonalIsC1OverSPlusC2OverS2` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_source_realKPlaneWaveCannotSource` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_source_transversePressuresEqualForEveryX0X4State` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_source_x0IndependentDiagonalOnShell` | `pair-creation/wolfram-dirac16complex00-report.json`, `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_source_x0IndependentExactExamples` | `pair-creation/wolfram-dirac16complex00-report.json`, `primordial-field/wolfram-primordial-report.json` | true | 0, 9, 18 |
| `P_source_x0IndependentOffDiagonalAre15Bilinears` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_source_x0IndependentSourceConditions` | `primordial-field/wolfram-primordial-report.json` | true | 0, 9, 18 |
| `P_source_x0IndependentStateSolvesDiracExactly` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_spinconn` | `primordial-field/python-primordial-report.json` | true | 4 |
| `P_spinconn_antisymmetry` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_spinconn_closedForms` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_spinconn_count24` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_spinconn_notebookCell501OmegaMuIJEqualsMixedOmega` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_spinconn_vielbeinPostulate512` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_zeta_gZetaZetaIsOne` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_zeta_range` | `primordial-field/wolfram-primordial-report.json` | true | 9 |
| `P_zeta_warpedMetric` | `primordial-field/wolfram-primordial-report.json` | true | 4, 9 |
| `P_zeta_warpFactor` | `primordial-field/wolfram-primordial-report.json` | true | 9 |

### 20.12 Index of checks: Stage 3, the dark-sector experiments

The reports of Stage 3 lie in `artifacts/dirac16complex/numerics/`. Names with underscores between lower-case words (such as `seven_volume_constant`) are self-checks of the Rust program, stored in the `summary.json` of each experiment; names in camel case (such as `eigenmodeLaws`) are checks of the independent Python checkers, stored in `python-check-report.json`. The table has 52 rows.

| Check | Committed report | Value | Cited in chapters |
| --- | --- | --- | --- |
| `a4_profile_independence` | `numerics/exp1/summary.json` | true | 11 |
| `backward_kasner_exponents` | `numerics/exp2/summary.json` | true | 11 |
| `bounceAndStop` | `numerics/exp3/python-check-report.json` | true | 11 |
| `boundNonnegative` | `numerics/exp2/python-check-report.json` | true | 11 |
| `closedFormVerified` | `numerics/exp2/python-check-report.json` | true | 11 |
| `constraintPreserved` | `numerics/exp2/python-check-report.json` | true | 11 |
| `constraint_preserved` | `numerics/exp2/summary.json` | true | 11 |
| `decelerationRoots` | `numerics/exp3/python-check-report.json` | true | 11 |
| `diracEquationFd` | `numerics/exp2/python-check-report.json` | true | 11 |
| `eigenmodeLaws` | `numerics/exp1/python-check-report.json` | true | 11 |
| `einsteinSourceNegative` | `numerics/exp1/python-check-report.json` | true | 11 |
| `einstein_source_negative_energy` | `numerics/exp1/summary.json` | true | 11 |
| `einsteinTensorFromMetric` | `numerics/exp2/python-check-report.json` | true | 11 |
| `energy_squared_changes_sign_at_tstar` | `numerics/exp5/summary.json` | true | 11 |
| `exactSolution` | `numerics/exp1/python-check-report.json`, `numerics/exp2/python-check-report.json` | true | 11 |
| `exact_solution` | `numerics/exp2/summary.json` | true | 11 |
| `exact_solution_all_runs` | `numerics/exp1/summary.json` | true | 11 |
| `extra_times_turn_to_expansion` | `numerics/exp2/summary.json` | true | 11 |
| `gammaVariantReproducesUniteTangent` | `numerics/exp3/fits.json` | true | 11 |
| `growth_matches_wkb_first_order` | `numerics/exp5/summary.json` | true | 8 |
| `growth_matches_wkb_leading_order` | `numerics/exp5/summary.json` | true | 8, 11 |
| `hilbert_norm_superexponential_growth` | `numerics/exp5/summary.json` | true | 11 |
| `hubble_positive_backward_stop_at_predicted_bounce` | `numerics/exp3/summary.json` | true | 11 |
| `kasnerExponents` | `numerics/exp2/python-check-report.json` | true | 11 |
| `kreinConservedNormalized` | `numerics/exp5/python-check-report.json` | true | 11 |
| `mixedStateOscillationMatchesExact` | `numerics/exp1/python-check-report.json` | true | 11 |
| `muIndependence` | `numerics/exp3/python-check-report.json` | true | 11 |
| `offDiagonalStressVanishes` | `numerics/exp2/python-check-report.json`, `numerics/exp3/python-check-report.json` | true | 11 |
| `pairPauli` | `numerics/exp4/python-check-report.json` | true | 11 |
| `pairSmoothTransitionReference` | `numerics/exp4/python-check-report.json` | true | 11 |
| `pairSuddenSpectrumMagnusReference` | `numerics/exp4/python-check-report.json` | true | 11 |
| `pairTailMatchesKinkTheory` | `numerics/exp4/python-check-report.json` | true | 11 |
| `pair_tail_matches_kink_theory` | `numerics/exp4/summary.json` | true | 11 |
| `phantomCrossing` | `numerics/exp3/python-check-report.json` | true | 11 |
| `phantom_crossing_at_cube_root_2abs_x0` | `numerics/exp3/summary.json` | true | 11 |
| `phantom_iff_negative_kinetic_energy` | `numerics/exp2/summary.json` | true | 11 |
| `phantomStructure` | `numerics/exp2/python-check-report.json` | true | 11 |
| `phaseDriftIsTimeRounding` | `numerics/exp2/python-check-report.json` | true | 11 |
| `refinedConvergence` | `numerics/exp1/python-check-report.json`, `numerics/exp2/python-check-report.json`, `numerics/exp3/python-check-report.json`, `numerics/exp4/python-check-report.json`, `numerics/exp5/python-check-report.json` | true | 11, 19 |
| `repeatByteIdentity` | `numerics/exp1/python-check-report.json`, `numerics/exp2/python-check-report.json`, `numerics/exp3/python-check-report.json`, `numerics/exp4/python-check-report.json`, `numerics/exp5/python-check-report.json` | true | 10, 11, 19 |
| `rho_frozen_all_runs` | `numerics/exp1/summary.json` | true | 11 |
| `rho_p_w_match_closed_form` | `numerics/exp3/summary.json` | true | 11 |
| `rho_p_w_mu_independent` | `numerics/exp3/summary.json` | true | 11 |
| `rhoZeroLocation` | `numerics/exp3/python-check-report.json` | true | 11 |
| `seven_volume_constant` | `numerics/exp1/summary.json` | true | 11 |
| `sigma_from_spinor_equals_a_minus_3` | `numerics/exp3/summary.json` | true | 11 |
| `spinorPhaseWithinTimeRounding` | `numerics/exp2/python-check-report.json` | true | 11 |
| `S_times_V_constant` | `numerics/exp2/summary.json` | true | 11 |
| `tangentCPL` | `numerics/exp3/python-check-report.json` | true | 11 |
| `wkbFirstOrder` | `numerics/exp5/python-check-report.json` | true | 8, 11 |
| `wkbLateRate` | `numerics/exp5/python-check-report.json` | true | 8, 11 |
| `wkbLeading` | `numerics/exp5/python-check-report.json` | true | 8, 11 |

### 20.13 Index of checks: Stage 4, the Kohn–Sham states

The reports of Stage 4 lie in `artifacts/dirac16complex/kohn-sham/`. Names beginning with `KS_` are exact checks of the Wolfram verifier and of the sympy checker; names in lower case with underscores are self-checks of the Rust solver (in the `summary.json` of each folder of `rust/`) or checks of the cross-checker (in `python-check-report.json`); a Rust self-check that is made for every run carries the name of the run in front, such as `m1_L3_N112_lam0_T0_energy_from_rho`, and is indexed as a family `*_energy_from_rho`. The table has 102 rows.

| Check | Committed report | Value | Cited in chapters |
| --- | --- | --- | --- |
| `a4_rescaling_pair_exact` | `kohn-sham/rust/scf/summary.json` | true | 13 |
| `canonical_deltaSCF` | `kohn-sham/python-check-report.json` | true | 14, 19 |
| `canonical_eigenvalues` | `kohn-sham/python-check-report.json` | false | 14, 16, 18, 19 |
| `*_cv_finite_difference_vs_exact` | `kohn-sham/rust/thermo/summary.json` | all 4 true | 13 |
| `*_emt_conservation` | `kohn-sham/rust/emt/summary.json`, `kohn-sham/rust/scf/summary.json` | all 43 true | 13 |
| `*_energy_from_rho` | `kohn-sham/rust/emt/summary.json`, `kohn-sham/rust/scf/summary.json` | all 43 true | 13 |
| `*_entropy_positive` | `kohn-sham/rust/thermo/summary.json` | all 16 true | 13 |
| `exchange_table_d3_closed_form` | `kohn-sham/rust/spectrum/exchange-table-check.json`, `kohn-sham/rust/spectrum/summary.json` | true | 13 |
| `exchange_table_d4_closed_form` | `kohn-sham/rust/spectrum/exchange-table-check.json`, `kohn-sham/rust/spectrum/summary.json` | true | 13 |
| `excited_grid_refinement_delta_scf` | `kohn-sham/rust/excited/summary.json` | true | 13 |
| `*_free_energy_decreases` | `kohn-sham/rust/thermo/summary.json` | all 16 true | 13 |
| `gauntlet_*` | `kohn-sham/notebook-report.json` | 56 of 60 true | 19 |
| `grid_refinement_energy` | `kohn-sham/rust/scf/summary.json` | true | 13 |
| `*_heat_capacity_positive` | `kohn-sham/rust/thermo/summary.json` | all 16 true | 13 |
| `KS_boundary_bagFamily` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_boundary_bagThetaZeroIsEvenParity` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_boundary_currentBlockForm` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_boundary_currentConservedAlongY` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_boundary_currentMatrix` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_boundary_hilbertNormNotConservedAlongY` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_boundary_parityA_symmetryIffMassOdd` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 13 |
| `KS_boundary_parityB_couplesJBlocks` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_boundary_parityB_symmetryForEvenMass` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_boundary_parityKillsCurrent` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_boundary_parityProjectorsBlockForm` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_boundary_selfAdjointBoundaryTerm` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_emt_offBlockComponentsVanishPerOrbital` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_emt_p1` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_emt_p2p3` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_emt_pt` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_emt_py` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_emt_rho` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 13 |
| `KS_emt_T41cancelsOverShell` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_emt_Ty1ProportionalToCurrent` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_emt_Ty4ProportionalToCurrent` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_exchange_angularAverageOfPdotQVanishes` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 0, 13 |
| `KS_exchange_blockFormOfFockTerm` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 0, 13 |
| `KS_exchange_couplingDimension` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13, 18 |
| `KS_exchange_filledShellOneEighth` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_exchange_filledShellScalarDensity` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_exchange_kernelPlusMinus` | `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_exchange_kernelPlusPlus` | `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_exchange_ldaPotentials` | `kohn-sham/python-theory-report.json` | true | 13 |
| `KS_exchange_restGasLimit` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_exchange_uniformGasClosedForm` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 0, 13, 18 |
| `KS_exchange_wickTheoremHF` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13, 18 |
| `KS_functional` | `kohn-sham/python-theory-report.json` | true | 13 |
| `KS_functional_fermiDiracOccupations` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_functional_hellmannFeynmanLambda` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_functional_hellmannFeynmanMass` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_functional_hellmannFeynmanMomentum` | `kohn-sham/python-theory-report.json` | true | 13 |
| `KS_functional_hellmannFeynmanTemperature` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_functional_merminStructure` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_functional_stationarityGivesKSEquation` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_functional_totalEnergyDoubleCounting` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_geometry_braneEnergyPositive` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 9, 13 |
| `KS_geometry_christoffelClosedForms` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_geometry_christoffelCount18` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 9 |
| `KS_geometry_constantCurvatureSevenSpace` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 9, 13, 18 |
| `KS_geometry_einsteinMixedDiag` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 4, 9, 13, 18 |
| `KS_geometry_extrinsicCurvature` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 9, 13 |
| `KS_geometry_inducedMetricFlat` | `kohn-sham/wolfram-kohn-sham-report.json` | true | 9 |
| `KS_geometry_israelConventionRandallSundrum` | `kohn-sham/python-theory-report.json` | true | 9, 13 |
| `KS_geometry_israelJump` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 9, 13 |
| `KS_geometry_israelStress` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 0, 9, 13 |
| `KS_geometry_kretschmannConstant` | `kohn-sham/wolfram-kohn-sham-report.json` | true | 9, 18 |
| `KS_geometry_notebookChart` | `kohn-sham/wolfram-kohn-sham-report.json` | true | 9 |
| `KS_geometry_requiredSource` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 0, 4, 9, 13 |
| `KS_geometry_rhoRequiredNegative` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 9, 13 |
| `KS_geometry_ricciMixed` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 9 |
| `KS_geometry_ricciScalarMinus42H2` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 0, 4, 9, 13 |
| `KS_geometry_signature44` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 9 |
| `KS_geometry_sqrtDetG_W6` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 9, 13 |
| `KS_reduction_a4IsMomentumRescaling` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 9, 13 |
| `KS_reduction_algebraDim8` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_ansatzRemoves3H` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 13 |
| `KS_reduction_basisUnitary` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_blockHamiltonianEquivalentToODE` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_blockODEMatrix` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 0, 13 |
| `KS_reduction_blocksA0A1A4` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_blocksBC` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json`, `pair-creation/wolfram-dirac16complex00-report.json` | true | 13 |
| `KS_reduction_blockTypes` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_fiveMatricesBlockDiagonal` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_flatMeasure` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_gamma8SwapsJ` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_gammaSlashOmega3Hgamma0` | `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_hMinusEqualsMinusHPlus` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 0, 13 |
| `KS_reduction_JK1K2commute` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_k0MassiveLevels` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_k0ZeroMode` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_mirrorPatchSameForm` | `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_projectorsRank2` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_reconstructFromBlocks` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_reducedEquationODEForm` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_rotationalSymmetry` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_sigma3ConjugationFlipsK` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_withoutW3the3HTermSurvives` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `KS_reduction_zeroModeSplitting` | `kohn-sham/python-theory-report.json`, `kohn-sham/wolfram-kohn-sham-report.json` | true | 13 |
| `m1_L3_N112_lam0_T0_hellmann_feynman_dE_dm` | `kohn-sham/rust/scf/summary.json` | true | 13 |
| `m1_L3_N112_lamp1_T0_hellmann_feynman_dE_dm` | `kohn-sham/rust/scf/summary.json` | true | 13 |
| `r07_*` | `kohn-sham/notebook-report.json` | 0 of 2 true | 19 |
| `theory_zero_mode_splitting` | `kohn-sham/rust/spectrum/summary.json` | true | 13 |

### 20.14 Index of checks: Stage 5 and the matter–antimatter analysis

The reports of Stage 5 lie in `artifacts/dirac16complex/pair-creation/`, those of the matter–antimatter analysis in `artifacts/dirac16complex/matter-antimatter/`. The prefixes are `C00_` (dirac16complex00, Wolfram), `S5_` (the sympy checkers of Stage 5), `PAIR_` (pairing theorems, Wolfram) and `MA_` (matter and antimatter, both programs). The table has 269 rows.

| Check | Committed report | Value | Cited in chapters |
| --- | --- | --- | --- |
| `C00_algebra_anticommutatorTotallyAntisymmetric` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_algebra_leadFacts` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_algebra_pinModuleAndSpinInvariance` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_charge_indefinite` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7, 14, 15 |
| `C00_connection_nonTrivialCoupling` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6, 7 |
| `C00_connection_OmegaTermInFieldEquation` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_current_conservationAndReality` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7, 14 |
| `C00_EL_commutingCurved` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7, 14 |
| `C00_EL_commutingFlat` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `C00_EL_commutingGeneralSmoothU` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6, 7 |
| `C00_EL_identicalFormBothStatistics` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7, 14 |
| `C00_EMT_conservationOnShell` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `C00_EMT_generalSmoothU` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6, 7 |
| `C00_EMT_homogeneousEquationsOfState` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `C00_EMT_observerSplitGaussianNormal` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `C00_EMT_symmetricAndReal` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `C00_EMT_traceOnShell` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `C00_EMT_vielbeinVariation` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `C00_energy_unboundedBelow` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7, 14, 15, 18 |
| `C00_lagrangian_coefficientHermiticity` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_lagrangian_grassmannFlatHermitianAndEL` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_lagrangian_realCommuting` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_massTerm_commutingExplicitSpinors` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_massTerm_dispersionFlat` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_massTerm_grassmannNonzero` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_primordial_ELcommuting` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `C00_primordial_geometryMatchesStage2` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `C00_primordial_homogeneousState` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7 |
| `C00_primordial_staticFieldSourcedExactly` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7, 18 |
| `C00_realRestriction_commutingFlatDecomposition` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_realRestriction_commutingNonTrivial` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_realRestriction_commutingNotebookContraction` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_realRestriction_grassmannComplexDecomposition` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_realRestriction_grassmannCurvedTrivial` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_realRestriction_grassmannFlatTrivial` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_realRestriction_relationToL1` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 6 |
| `C00_static_blocksFromStage4Theory` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 14 |
| `C00_static_classicalEnergyKreinSigned` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7, 14, 15 |
| `C00_static_classicalModeIsKreinWeightedKS` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7, 14, 15 |
| `C00_static_geometryAndReducedEquation` | `pair-creation/wolfram-dirac16complex00-report.json` | true | 7, 14 |
| `MA_agreesWithWolfram` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M1` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M1_*` | `matter-antimatter/python-matter-antimatter-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json` | all 46 true | 16 |
| `MA_M1_chargeDensityMatrix` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M1_divergenceIdentityAllFirstJets` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M1_ksFixedNetNumberRecorded` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M1_negativeControlNotebookConnection` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 7, 17 |
| `MA_M1_noetherCurrentLocalPhase_grassmann_G1` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M1_noetherIdentity_*` | `matter-antimatter/python-matter-antimatter-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json` | all 6 true | 17 |
| `MA_M1_noetherIdentity_commuting_G1` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 7, 16, 17 |
| `MA_M1_noetherIdentity_grassmann_G1` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 7, 16, 17 |
| `MA_M1_onShellConservation_G1` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 16, 17 |
| `MA_M1_stage1ChecksCited` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M1_u1InvarianceCommutingGenericU_flat` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M1_u1InvarianceCommutingGenericU_G1` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 6 |
| `MA_M1_u1InvarianceGrassmann_G1` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 6, 17 |
| `MA_M2` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M2_*` | `matter-antimatter/python-matter-antimatter-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json` | all 26 true | 6 |
| `MA_M2_C_and_CP_status` | `matter-antimatter/python-matter-antimatter-report.json` | true | 6, 17 |
| `MA_M2_canonicalStructure` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M2_canonicalStructureOfExactGrassmannSymmetries` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M2_chargeConjugationSolutionSpaces` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M2_conjugationIntertwiners` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M2_cpScopeInCurvedFields` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17, 19 |
| `MA_M2_discreteGroupCharacterTable` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M2_frameLevelG1_commuting` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M2_frameLevelG1_grassmann` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M2_internalMapsCurvedJets` | `matter-antimatter/python-matter-antimatter-report.json` | true | 6 |
| `MA_M2_lagrangianFlatCommuting_all` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 6, 17 |
| `MA_M2_lagrangianFlatGrassmann_all` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 6, 17 |
| `MA_M2_namedReflectionsFlatJets` | `matter-antimatter/python-matter-antimatter-report.json` | true | 6 |
| `MA_M2_signPatternClassification` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M2_spin0ContainsChargeReversingTimeRotation` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M2_statisticsSign` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M2_symmetrySummaryAndChargeReversal` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M3` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M3_*` | `matter-antimatter/python-matter-antimatter-report.json`, `matter-antimatter/wolfram-matter-antimatter-report.json` | all 17 true | 18 |
| `MA_M3_allInvariantFormsSymmetric` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M3_commutingSurvival` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M3_derivativeTypeSurvivalCurved` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M3_extraGrassmannQuarticCharge4` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M3_grassmannSurvival` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M3_invariantFormsSpan_C_Cgamma8` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M3_kineticInvariantForms` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M3_massTypeSurvivalAndCharge` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M3_notebookLgIsMajoranaType` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M3_pinCharacterForms` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M3_pinCharactersMajoranaTerms` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M3_quarticChargeViolatingExamplesGrassmann` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M3_spinInvariantForms` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M3_u1Charge` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M4` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M4_currentFlipG1_grassmann` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M4_currentFlipMatrix` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 17 |
| `MA_M4_gamma8ChargeFlipCurved` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M4_gamma8EMTPairing` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M4_gamma8EulerLagrangePairing` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M4_gamma8MatrixFacts` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17 |
| `MA_M4_imageFieldFockModel` | `matter-antimatter/python-matter-antimatter-report.json` | true | 17, 19 |
| `MA_M4_kreinModeFacts` | `matter-antimatter/python-matter-antimatter-report.json` | true | 15, 17 |
| `MA_M4_kreinOneParticle` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 15, 16, 17 |
| `MA_M4_pairEMTAndCurrentG1_commuting` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 15, 16, 17 |
| `MA_M4_pairEMTG1_grassmann` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 15, 16, 17 |
| `MA_M5_implication` | `matter-antimatter/wolfram-matter-antimatter-report.json` | true | 16, 17 |
| `PAIR_algebra_bilinearParities` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_algebra_BProperties` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_algebra_chiralBlockStructure` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_algebra_CProperties` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_algebra_gamma8InIdentityComponent` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15 |
| `PAIR_algebra_gamma8Properties` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15 |
| `PAIR_algebra_kreinUnderBasicReflections` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_stat_*` | `pair-creation/wolfram-pairing-report.json` | all 13 true | 14 |
| `PAIR_stat_bosonThermalWickPlus` | `pair-creation/wolfram-pairing-report.json` | true | 14 |
| `PAIR_stat_classicalGaussianWickPlus` | `pair-creation/wolfram-pairing-report.json` | true | 14, 18 |
| `PAIR_stat_expectationRuleCovarianceIndefinite` | `pair-creation/wolfram-pairing-report.json` | true | 14, 15 |
| `PAIR_stat_expectationRuleTraces` | `pair-creation/wolfram-pairing-report.json` | true | 14 |
| `PAIR_stat_fermionWickMinus` | `pair-creation/wolfram-pairing-report.json` | true | 14, 18 |
| `PAIR_stat_filledShellExchangeRatio` | `pair-creation/wolfram-pairing-report.json` | true | 14 |
| `PAIR_stat_fixedAmplitudePhasesDeviate` | `pair-creation/wolfram-pairing-report.json` | true | 14 |
| `PAIR_stat_ldaPotentials` | `pair-creation/wolfram-pairing-report.json` | true | 14, 15 |
| `PAIR_stat_singleModeMoments` | `pair-creation/wolfram-pairing-report.json` | true | 14 |
| `PAIR_stat_T0TotalDerivative` | `pair-creation/wolfram-pairing-report.json` | true | 14 |
| `PAIR_stat_uniformGasExchange` | `pair-creation/wolfram-pairing-report.json` | true | 14, 15 |
| `PAIR_T1generic_*` | `pair-creation/wolfram-pairing-report.json` | all 9 true | 7, 16 |
| `PAIR_T1generic_conjugateFieldEquation` | `pair-creation/wolfram-pairing-report.json` | true | 7, 15, 16 |
| `PAIR_T1generic_current` | `pair-creation/wolfram-pairing-report.json` | true | 7, 15, 16 |
| `PAIR_T1generic_emtAll36` | `pair-creation/wolfram-pairing-report.json` | true | 7, 15, 16 |
| `PAIR_T1generic_fieldEquation` | `pair-creation/wolfram-pairing-report.json` | true | 7, 15, 16 |
| `PAIR_T1generic_lagrangian` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15, 16 |
| `PAIR_T1generic_naiveFixedLambdaFails` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15, 16 |
| `PAIR_T1grassmann_*` | `pair-creation/wolfram-pairing-report.json` | all 7 true | 7, 16 |
| `PAIR_T1grassmann_current` | `pair-creation/wolfram-pairing-report.json` | true | 7, 15, 16 |
| `PAIR_T1grassmann_diracOperator` | `pair-creation/wolfram-pairing-report.json` | true | 7, 15, 16 |
| `PAIR_T1grassmann_emt` | `pair-creation/wolfram-pairing-report.json` | true | 7, 15, 16 |
| `PAIR_T1grassmann_lagrangian` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15, 16 |
| `PAIR_T1grassmann_naiveFixedLambdaFails` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T1jets_*` | `pair-creation/wolfram-pairing-report.json` | all 13 true | 7, 15, 16 |
| `PAIR_T1jets_conservationBoth` | `pair-creation/wolfram-pairing-report.json` | true | 7 |
| `PAIR_T1jets_emt` | `pair-creation/wolfram-pairing-report.json` | true | 7, 16 |
| `PAIR_T1jets_fieldEquations` | `pair-creation/wolfram-pairing-report.json` | true | 7, 16 |
| `PAIR_T1jets_gamma8WithFrameSignIsSymmetry` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15, 16 |
| `PAIR_T1jets_lagrangian` | `pair-creation/wolfram-pairing-report.json` | true | 6, 16 |
| `PAIR_T1jets_naiveFixedLambdaFails` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T1jets_onShellImage` | `pair-creation/wolfram-pairing-report.json` | true | 7, 15 |
| `PAIR_T1jets_pairEMTAndCurrentVanish` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_T1jets_vielbeinSignFlipGeometry` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15 |
| `PAIR_T1jets_vielbeinSignFlipIsT1` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15, 16 |
| `PAIR_T1krein_*` | `pair-creation/wolfram-pairing-report.json` | all 12 true | 16, 17, 18 |
| `PAIR_T1krein_imageAnticommutatorMinusB` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16, 17 |
| `PAIR_T1krein_imageExpectationValues` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16, 17 |
| `PAIR_T1krein_imageOperatorIdentities` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16, 17 |
| `PAIR_T1krein_independentCARPlusB` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16, 17 |
| `PAIR_T1krein_independentExpectationValues` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16, 17 |
| `PAIR_T1krein_minusMModes` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T1primordial_*` | `pair-creation/wolfram-pairing-report.json` | all 6 true | 15, 16 |
| `PAIR_T1primordial_current` | `pair-creation/wolfram-pairing-report.json` | true | 16 |
| `PAIR_T1primordial_diracOperator` | `pair-creation/wolfram-pairing-report.json` | true | 16 |
| `PAIR_T1primordial_emt64` | `pair-creation/wolfram-pairing-report.json` | true | 7, 16 |
| `PAIR_T1primordial_lagrangian` | `pair-creation/wolfram-pairing-report.json` | true | 6, 16 |
| `PAIR_T2frame_*` | `pair-creation/wolfram-pairing-report.json` | all 12 true | 6, 16 |
| `PAIR_T2frame_characterIsMinusNorm` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_T2frame_frameReflectionsGeometry` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T2frame_gamma8TimesUntwistedSpacelike` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T2frame_onShellImage` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_T2frame_scalarAndCurrentSigns` | `pair-creation/wolfram-pairing-report.json` | true | 16 |
| `PAIR_T2frame_twistedSpacelikeMapsToMinusMSameLambda` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15, 16 |
| `PAIR_T2frame_twistedTimelike` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15 |
| `PAIR_T2frame_untwistedSpacelikeContractE3` | `pair-creation/wolfram-pairing-report.json` | true | 6, 15 |
| `PAIR_T2z2_*` | `pair-creation/wolfram-pairing-report.json` | all 11 true | 16, 18 |
| `PAIR_T2z2_currentPullback` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_T2z2_diracOperator` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_T2z2_emtPullback` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_T2z2_geometry` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T2z2_lagrangianEven` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T2z2_massFunctionMap` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_T2z2_PBfieldLevelFlipsLambda` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T2z2_ruleParities` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T2z2_sameMassFails` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T2z2_scalarOdd` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T2z2_symmetricIffOddMass` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_T3block_*` | `pair-creation/wolfram-pairing-report.json` | all 18 true | 16 |
| `PAIR_T3block_bagAngleMap` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3block_densityAndCurrentMaps` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3block_gamma1IsSigma1InEveryBlock` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3block_gamma8IsSigma2BetweenPartnerBlocks` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3block_hamiltonianSigma2` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3block_parityMap` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3block_potentialsImageRule` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3block_potentialsStandardRule` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3block_sigma2IsRustSwap` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3block_sigma2MapsBlockODE` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3block_statisticsCoefficients` | `pair-creation/wolfram-pairing-report.json` | true | 14 |
| `PAIR_T3emt_imageRuleMinusT` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3emt_stage4CrossCheck` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3emt_standardRulePlusT` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3ks_*` | `pair-creation/wolfram-pairing-report.json` | all 19 true | 16 |
| `PAIR_T3ks_controlDiffersFromPairedProblem` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3ks_controlMixedSectorLevelsDisjoint` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3ks_controlSplittingClosedForm` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_T3ks_controlSubGapBoundState` | `pair-creation/wolfram-pairing-report.json` | true | 15, 18 |
| `PAIR_T3ks_imageRuleEnergyOdd` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_T3ks_massiveLevelsMap` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3ks_mixedSectorSolutions` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3ks_occupationsAndTemperature` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3ks_sigma1FunctionalInvariant` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3ks_sigma2Densities` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3ks_sigma2FunctionalInvariant` | `pair-creation/wolfram-pairing-report.json` | true | 14, 15, 16 |
| `PAIR_T3ks_sigma2KSOperatorEquivariant` | `pair-creation/wolfram-pairing-report.json` | true | 14, 15, 16 |
| `PAIR_T3ks_stationarityBothStatistics` | `pair-creation/wolfram-pairing-report.json` | true | 14, 15 |
| `PAIR_T3ks_zeroModeImage` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3ks_zeroModeSplittingMapsExactly` | `pair-creation/wolfram-pairing-report.json` | true | 15 |
| `PAIR_T3ks_zeroModeUntransformedControl` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `PAIR_totals_fieldLevelChiralPair` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16, 18 |
| `PAIR_totals_fieldLevelMirrorPair` | `pair-creation/wolfram-pairing-report.json` | true | 15, 18 |
| `PAIR_totals_ksKreinImagePair` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16, 18 |
| `PAIR_totals_ksMirrorPair` | `pair-creation/wolfram-pairing-report.json` | true | 15, 16 |
| `S5_agreesWithWolfram` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_algebra_anticommutatorTotallyAntisymmetric` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_algebra_pinModuleAndSpinInvariance` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_connection_nonTrivialCoupling` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_connection_OmegaTermInFieldEquation` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_EL_grassmannCurved` | `pair-creation/python-dirac16complex00-report.json` | true | 7 |
| `S5_EL_identicalFormBothStatistics` | `pair-creation/python-dirac16complex00-report.json` | true | 7 |
| `S5_EMT_conservationOnShell` | `pair-creation/python-dirac16complex00-report.json` | true | 7 |
| `S5_EMT_homogeneousEquationsOfState` | `pair-creation/python-dirac16complex00-report.json` | true | 7 |
| `S5_EMT_symmetricAndReal` | `pair-creation/python-dirac16complex00-report.json` | true | 7 |
| `S5_EMT_traceOnShell` | `pair-creation/python-dirac16complex00-report.json` | true | 7 |
| `S5_EMT_vielbeinVariation` | `pair-creation/python-dirac16complex00-report.json` | true | 7 |
| `S5_energy_unboundedBelow` | `pair-creation/python-dirac16complex00-report.json` | true | 18 |
| `S5_lagrangian_coefficientHermiticity` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_lagrangian_realCommuting` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_massTerm_commutingExplicitSpinors` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_massTerm_dispersionFlat` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_massTerm_grassmannNonzero` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_pairingAgreesWithWolfram` | `pair-creation/python-pairing-report.json` | true | 15 |
| `S5_primordial_homogeneousState` | `pair-creation/python-dirac16complex00-report.json` | true | 7 |
| `S5_primordial_staticFieldSourcedExactly` | `pair-creation/python-dirac16complex00-report.json` | true | 7, 18 |
| `S5_realRestriction_commutingNonTrivial` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_realRestriction_commutingNotebookContraction` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_realRestriction_grassmannComplexDecomposition` | `pair-creation/python-dirac16complex00-report.json` | true | 6 |
| `S5_stat` | `pair-creation/python-pairing-report.json` | true | 14 |
| `S5_stat_*` | `pair-creation/python-pairing-report.json` | all 15 true | 14 |
| `S5_stat_bosonThermalWickPlus` | `pair-creation/python-pairing-report.json` | true | 14 |
| `S5_stat_classicalGaussianWickPlus` | `pair-creation/python-pairing-report.json` | true | 14 |
| `S5_stat_expectationRuleKreinFock` | `pair-creation/python-pairing-report.json` | true | 14 |
| `S5_stat_expectationRuleTraces` | `pair-creation/python-pairing-report.json` | true | 14 |
| `S5_stat_fermionWickMinus` | `pair-creation/python-pairing-report.json` | true | 14 |
| `S5_static_classicalEnergyKreinSigned` | `pair-creation/python-dirac16complex00-report.json` | true | 14 |
| `S5_static_classicalModeIsKreinWeightedKS` | `pair-creation/python-dirac16complex00-report.json` | true | 14 |
| `S5_static_geometryAndReducedEquation` | `pair-creation/python-dirac16complex00-report.json` | true | 7 |
| `S5_static_sourceProperChart` | `pair-creation/python-dirac16complex00-report.json` | true | 7 |
| `S5_stat_ldaPotentials` | `pair-creation/python-pairing-report.json` | true | 14 |
| `S5_stat_uniformGasExactFinite` | `pair-creation/python-pairing-report.json` | true | 14 |
| `S5_stat_uniformGasExchange` | `pair-creation/python-pairing-report.json` | true | 14 |
| `S5_T1generic` | `pair-creation/python-pairing-report.json` | true | 16 |
| `S5_T1generic_eulerLagrangeFromLagrangian` | `pair-creation/python-pairing-report.json` | true | 15 |
| `S5_T1generic_fieldEquation` | `pair-creation/python-pairing-report.json` | true | 7 |
| `S5_T1generic_lagrangian` | `pair-creation/python-pairing-report.json` | true | 6 |
| `S5_T1grassmann` | `pair-creation/python-pairing-report.json` | true | 15, 16 |
| `S5_T1jets` | `pair-creation/python-pairing-report.json` | true | 16 |
| `S5_T1krein_*` | `pair-creation/python-pairing-report.json` | all 13 true | 15, 18 |
| `S5_T1krein_imageOperatorIdentities` | `pair-creation/python-pairing-report.json` | true | 15 |
| `S5_T1primordial` | `pair-creation/python-pairing-report.json` | true | 16 |
| `S5_T2frame` | `pair-creation/python-pairing-report.json` | true | 16 |
| `S5_T2z2_fieldEquationMapsToMinusMSameLambda` | `pair-creation/python-pairing-report.json` | true | 15 |
| `S5_T2z2_kineticEven` | `pair-creation/python-pairing-report.json` | true | 15 |
| `S5_T2z2_PBRuleMatrixEvenCOdd` | `pair-creation/python-pairing-report.json` | true | 15 |
| `S5_T3block` | `pair-creation/python-pairing-report.json` | true | 16 |
| `S5_T3ks` | `pair-creation/python-pairing-report.json` | true | 16 |

### 20.15 Checks of the tools, and the state of the index

**Checks that no committed report stores.** Chapter 19 also names checks of the two programs that build this book. They are printed as lines `check_<name>=true` or `false` when the program runs and are not stored in a committed file:

| Check | Program that prints it | What it requires | Cited in chapters |
| --- | --- | --- | --- |
| `crossReferencesResolve` | `scripts/build_textbook.py` | every reference "Chapter N" and "Section N.M" of the book names an existing chapter or section | 19 |
| `editionRegistered` | `scripts/build_provenance_pdf.py` | the document has an edition in `provenance/pdf-specifications.json` | 19 |
| `registeredPath` | `scripts/build_provenance_pdf.py` | the registered edition names this PDF file | 19 |
| `registeredPageCount` | `scripts/build_provenance_pdf.py` | the PDF has the registered number of pages | 19 |
| `registeredSha256` | `scripts/build_provenance_pdf.py` | the PDF has the registered sha256 | 19 |
| `provenancePdfCopy` | `scripts/build_provenance_pdf.py` | the verified PDF was copied to its final place | 19 |

**The commit of the index.** The index of Sections 20.10 to 20.14 was made from the chapter files of this edition and the committed reports of commit `d4f7c58` (2026-09-30). The reports are the same as in commit `4cd47fe`, which Chapter 19 tested, except that further Rust runs of the subcommand `pairs` were added and that the sympy report of the matter–antimatter analysis, `matter-antimatter/python-matter-antimatter-report.json`, was regenerated in commit `27794e8`; it has 77 checks instead of 75 (Section 19.10). The two checks it gained, `MA_M2_cpScopeInCurvedFields` and `MA_M4_imageFieldFockModel`, are cited in Chapters 17 and 19; in commit `4cd47fe` they exist in the checker `scripts/check_dirac16complex_matter_antimatter.py` but not yet in the committed report.

**Counting.** The five tables list 583 rows: 558 single checks and 25 families. Every single check listed is true in every committed file shown, except `canonical_eigenvalues` (Section 19.9); every family is entirely true, except the two families `gauntlet_*` and `r07_*` of the Jupyter notebook's Stage-4 report, whose six false checks Section 19.9 explains.

### 20.16 What we proved and what we assumed

This chapter proves nothing new. The glossary repeats, in one or two sentences each, definitions made in Chapters 0 to 18; where an entry and a chapter seem to differ, the chapter is authoritative, and the entry names it. The index of checks is a **computed** list: every row was produced by a program from the committed reports and the chapter files of this edition, and the value shown is the value in the committed file shown. It assumes that the chapter files and the reports named in Section 20.15 are the ones of the edition you read; a later commit can add checks, add citations or change a value, and then the lookup command of Section 20.9 gives the current answer. That a check is listed as true says only that the program that wrote the report found it true; what the check establishes, and under which assumptions, is stated in the chapter that cites it.

### 20.17 Exercises

**Exercise 20.1.** Use the glossary to explain the difference between the Hilbert norm and the Krein norm of a mode amplitude. Which of the two is conserved for a mode with momentum along an extra time, and why does that not make such a mode harmless?

**Exercise 20.2.** Give the status word of Chapter 0 (PROVED, COMPUTED, ASSUMED, HYPOTHESIS or OPEN) for each statement: (a) the chirality map turns every solution with $(m,\lambda)$ into one with $(-m,-\lambda)$; (b) the Kohn–Sham gap of the free ground state with $N=8$; (c) the restriction of the numerical chapters to the good sector; (d) universes of masses $+M$ and $-M$ are created in pairs at $x_4=0$; (e) there is a consistent interacting quantum theory of dirac16complex.

**Exercise 20.3.** The symbols $\eta$ and $z$ each have two meanings in this book. Name them and say how the reader can tell them apart.

**Exercise 20.4.** Find in the index the one single check that is false in its committed report. Which programs are compared in it, and in which chapters is it discussed?

**Exercise 20.5.** The index lists the family `*_energy_from_rho` with 43 checks in two files. Use the table of Stage 4 and the lookup command of Section 20.9 to explain the number.

**Exercise 20.6.** Change the lookup command of Section 20.9 so that it counts, in every committed file, the checks whose names begin with a given text, and how many of them are true. Run it for `PAIR_T1krein_` and compare the result with the index and with Chapter 17.

**Exercise 20.7.** Why does the statistics sign decide whether complex conjugation is a symmetry of the Lagrangian? Answer with the glossary entries for statistics sign and charge conjugation, and name the chapter where the proof is.

**Exercise 20.8.** A classmate writes: "The index shows that `PAIR_T1krein_*` is all true, so the pair of universes has zero energy at the quantum level." Use the glossary entries for the image field, the reversed Krein metric and the Krein image pair to explain what the checks establish and what they do not.

### 20.18 Answers to the exercises

**Answer 20.1.** The Hilbert norm is $u^\dagger u$, the norm of the positive inner product; the Krein norm is $u^\dagger Bu$ with the indefinite matrix $B=-iC\gamma^4$ (Chapter 11). For every mode $h^\dagger B=Bh$, so the Krein norm is conserved always; the Hilbert norm is conserved only when the mode Hamiltonian is Hermitian, which holds in the good sector. A mode with enough momentum along an extra time has $E^2<0$ and grows exponentially (Chapter 8): in the committed EXP-5 run quoted there its Hilbert norm grows to $1.258\times10^{16}$, while its Krein norm keeps its initial value, up to a drift below $10^{-8}$ times the Hilbert norm, that is up to rounding (check `kreinConservedNormalized` of the EXP-5 checker). A conserved quantity that can be negative does not bound the size of the solution, because large positive and negative contributions can cancel in it; so its conservation does not make the mode harmless.

**Answer 20.2.** (a) PROVED (Theorem T1, Chapter 15, with exact checks). (b) COMPUTED (Chapter 13; a number of the Rust solver with its own checks and the cross-check status of Section 19.9). (c) ASSUMED: the restriction is imposed, not derived (Chapter 8). (d) HYPOTHESIS: the notebook's claim, which Chapter 16 shows to be consistent with the conservation laws for the classical fields but not derived; no creation process is computed. (e) OPEN (Chapter 18).

**Answer 20.3.** $\eta$ is the flat metric $\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$ everywhere except in Chapter 17, where $\eta$ also denotes the baryon-to-photon ratio $6.12\times10^{-10}$; the metric always carries indices ($\eta_{ab}$, $\eta^{ab}$) or appears as the matrix $\eta$, the ratio is a single number. $z=6Hx_0$ is the hidden angle of the primordial field in Chapter 9, and in Chapter 11 $z$ is the redshift, $1+z=1/a$; the chapter and the context (geometry of the notebook, or cosmology of the late universe) decide.

**Answer 20.4.** `canonical_eigenvalues` in `kohn-sham/python-check-report.json` is false (Section 20.13). It compares the Kohn–Sham levels of the Rust solver with those of the independent Python reference solver; one deep level of the smeared $N=1016$ ensemble differs by more than the tolerance (Section 19.9). The index lists Chapters 14, 16, 18 and 19 as citing it.

**Answer 20.5.** The Rust solver writes one self-check `<run>_energy_from_rho` for every run of the subcommand `scf` (33 runs) and of the subcommand `emt` (10 runs), in `rust/scf/summary.json` and `rust/emt/summary.json`: $33+10=43$. The check requires that the integral of the energy density equals the total energy of the run (Chapter 13). Since the names begin with the name of the run, the lookup command of Section 20.9 must be given a full name, such as `m1_L3_N112_lamp1_T0_energy_from_rho`; it then prints both files, because this run appears in both.

**Answer 20.6.** Replace the last two lines of the program:

```
python -c "
import json, pathlib, sys
for p in sorted(pathlib.Path('artifacts').rglob('*.json')):
    d = json.loads(p.read_text(encoding='utf-8'))
    c = d.get('checks') if isinstance(d, dict) else None
    if isinstance(c, dict):
        hits = [v for k, v in c.items() if k.startswith(sys.argv[1])]
        if hits:
            print(p.as_posix(), len(hits), 'true:', hits.count(True))
" PAIR_T1krein_
```

In both shells it printed

```
artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json 12 true: 12
```

that is twelve checks, all true, in one file, as the index says and as Chapter 17 states ("all twelve `PAIR_T1krein` checks true").

**Answer 20.7.** Complex conjugation $C_0:\Psi\to\Psi^\ast$ has to move a conjugated factor past an unconjugated one, and the statistics sign $s$ records the sign of that reordering: $+1$ for commuting components, $-1$ for Grassmann components. Theorem 6.10 shows that $C_0$ sends the kinetic term $K\to sK$ and the scalar density $S\to sS$. For the commuting field ($s=+1$) the Lagrangian is unchanged, so $C_0$ is an exact symmetry that reverses the charge: the charge conjugation of dirac16complex00. For the Grassmann field ($s=-1$) it reverses the sign of the Lagrangian and of $\lambda$, and no constant charge conjugation is a symmetry when $m\ne0$ (Chapter 6; the classification is Theorem M2 of Chapter 17).

**Answer 20.8.** The twelve checks `PAIR_T1krein_*` verify, in an exact Fock-space model with four rest modes, both readings of the $-M$ universe (Chapters 15 and 16): for the image field $\Psi_-=\gamma^8\Psi_+$ on the same state space, its anticommutator with the reversed Krein metric $-B$, the operator identities and the expectation values; and for the $-M$ theory quantized independently, its anticommutator with $+B$ and its expectation values. What they establish is that the cancelling energy and charge hold for the image, as operator identities of the form $X+(-X)=0$ on one state space, that is for the Krein image pair, which is one quantum system written in two sets of variables; and that the independently quantized $-M$ universe has positive kinetic and mass energies, which add to those of the $+M$ universe instead of cancelling (the entry `kreinLevelCaveat` quoted in Chapter 17). They do not show that two independent universes of zero total energy exist or are created: whether a physical pair with this property exists is OPEN, and no creation process is computed anywhere in the repository.
