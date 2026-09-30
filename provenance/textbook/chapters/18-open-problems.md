## 18. Open problems and how a student could attack them

### 18.1 What this chapter is for

A textbook usually ends where its theory is complete. This one cannot, because the theory it teaches is not complete, and the honesty rule of Section 0.2 forbids pretending otherwise. The earlier chapters marked every unanswered question with the word OPEN (Section 0.3). This chapter collects all of them: the open questions of this book and those listed in the project documents. For each one it gives five things:

1. **the question**, stated as precisely as we can;
2. **why it is hard**, that is, which obstacle is known and which step nobody has taken;
3. **what is known**, with the status words of Section 0.3 and the file or check where each statement is verified;
4. **a first step** that a student who has worked through this book could take, often carried out on a small example in this chapter;
5. **where to start** in the repository: the files, programs and reports that already exist.

Nothing in this chapter is claimed to be solved. Two of the problems below, a creation amplitude for pairs of universes (Section 18.9) and baryogenesis (Section 18.10), are the two parts of the author's request that this project has not established (Section 0.2). They appear here because they are open, and the chapter says exactly why.

**A label used only in this chapter.** Several first steps below contain a short calculation of our own. Such a calculation is marked **derived here**. It is complete as written and uses only results proved earlier in the book, but no program of the repository has checked it. In the language of Section 0.3 its status is that of a derivation without a machine check, and the first task of a student who wants to build on it is to redo it and then to verify it exactly, by machine, in two independent programs, as the project does for every exact statement (Section 18.2).

**The state of the project on which the problems stand** (2026-09-30, from `README.md`, `HANDOFF.md` section 2 and the committed reports). Stages 1 to 3 are complete, and their gates passed from fresh public clones of the repository. In Stage 4 the exact theory is complete (125 of 125 Wolfram and 157 of 157 sympy checks) and so is the Rust Kohn–Sham solver, but the final cross-check against the independent reference solver has one failed check out of 63 and the Stage-4 gate has not been run (Section 18.7). In Stage 5 the exact theory is committed and checked (Wolfram 46 of 46 and 141 of 141 checks, Python 49 of 49 and 172 of 172), the Kohn–Sham pair numerics are partial, and the Stage-5 documents are not written (Section 18.8). The matter–antimatter analysis is complete (44 of 44 and 75 of 75 checks) and its answer is negative (Chapter 17).

**The list.** The table gives every problem, where it is treated and its status.

| Problem | Section | Status | Where it arose |
| --- | --- | --- | --- |
| An interacting quantum field theory of dirac16complex, and renormalisation | 18.3 | OPEN | Chapters 8, 12 and 13 |
| The extra-time instability, and signature (4,4) against the observed world | 18.4 | OPEN | Chapters 5, 8 and 11 |
| What determines $a_4$; Einstein–Lovelock gravity with an acceptable source | 18.5 | OPEN | Chapters 4 and 9 |
| Can a Kohn–Sham state be the source of the primordial field? | 18.6 | OPEN; no computed state is | Chapter 13 |
| The last Stage-4 cross-check and the Stage-4 gate | 18.7 | OPEN; 62 of 63 cross-checks pass | Chapter 13 |
| The Stage-5 numerics | 18.8 | OPEN; partly computed | Chapters 14 and 15 |
| A creation amplitude for pairs of universes | 18.9 | OPEN; pair creation itself is a HYPOTHESIS | Chapters 15 and 16 |
| Baryogenesis in this framework | 18.10 | OPEN; the theory as built fails Sakharov's first two conditions | Chapter 17 |
| Smaller open items of the book and the project documents | 18.11 | OPEN | various |

The problems are not independent. The instability of Section 18.4 is one of the obstacles to the quantum theory of Section 18.3; the gravitational field equations of Section 18.5 decide both the sourcing question of Section 18.6 and any creation amplitude of Section 18.9; and baryogenesis (Section 18.10) needs a quantum theory, a non-equilibrium history and new interactions at once. A student is well advised to start with the problems whose first step is a finite calculation: Sections 18.5, 18.6 and 18.7.

### 18.2 How to work on an open problem in this repository

The project answered every question it did answer by the same procedure, and a student who attacks an open problem should follow it, because it is what makes an answer trustworthy. The steps are these.

1. **Write the question down precisely**, together with what would count as an answer and what would not. The project's specifications are examples: `handoff/specs/STAGE4_SPEC.md`, `handoff/specs/STAGE5_SPEC.md` and `handoff/specs/MATTER_ANTIMATTER_SPEC.md`. When a measurement contradicts the text of a specification, the specification receives an **erratum** that records the correction and the evidence (the Stage-4 specification has thirteen, E4.1 to E4.13).
2. **Derive the result by hand**, step by step, as this book does.
3. **Verify every exact statement in two independent programs**: a Wolfram Language package with its verifier and an independent Python checker built on sympy, each writing a report whose entry `checks` maps check names to true or false (Section 0.8). Include **negative controls**, tests that must fail for deliberately wrong input (Section 10.11).
4. **Compute every number with two independent solvers** and compare them with a checker whose tolerances are fixed before the comparison. A tolerance is changed only on the basis of a recorded measurement, and the change is itself an erratum (E4.12 and E4.13 are examples). Repeat each run to show that it is deterministic, and repeat it with tighter tolerances to show that it has converged (Section 10.11).
5. **Never weaken a check to make it pass.** A check that fails is information; the procedure is to find out why.
6. **Write a document and a gate**: the document states what is proved, what is computed, what is assumed and what is not claimed; the gate reruns everything from a fresh copy of the repository (Chapter 19).

The tools that already exist, and that the first steps below use, are the following.

| Tool | What it does | Examples in the repository |
| --- | --- | --- |
| exact Wolfram Language packages and verifiers | prove identities with exact integers, fractions and symbols, and write a report | `wolfram/*.wl` with `scripts/verify_*.wls` |
| independent exact Python checkers | redo the same statements with sympy, without Wolfram code | `scripts/check_dirac16complex_*.py` |
| an exact Grassmann algebra | anticommuting variables as computer objects | `scripts/grassmann_algebra.py` |
| Rust solvers with the CVODE engine | ordinary differential equations in $x_4$ (Stage 3) and shooting in $y$ (Stages 4 and 5) | `studies/dirac16complex_cosmology`, `studies/dirac16complex_kohn_sham` |
| independent numpy reference solvers | a second numerical method for the Kohn–Sham problems | `scripts/ks_reference_solver.py`, `scripts/ks_reference_pairs.py` |
| checkers of numerical results | compare two solvers, test identities, tolerances fixed in advance | `scripts/check_dirac16complex_kohn_sham.py`, `scripts/check_dirac16complex_pairs.py` |
| gates | rerun a whole stage from a fresh clone | `scripts/verify_stage1_arbitrary_field.ps1` to `scripts/verify_stage4_kohn_sham.ps1`, each with a `.sh` twin |
| the document builder | Markdown to LaTeX to a reproducible PDF | `scripts/build_provenance_pdf.py` |

Chapter 19 lists the commands that run each of them in PowerShell and in Bash.

### 18.3 Problem 1: an interacting quantum field theory, and renormalisation

**The question.** Chapter 8 quantized dirac16complex canonically, but only as a free field: the anticommutator, the Krein space, the Fock space of the good sector and the expectation-value rule are statements about the theory with $U=0$. The interaction $U(S)=\tfrac\lambda2S^2$ entered afterwards only through mean-field approximations: the homogeneous condensates of Chapter 11 and the Hartree–Fock and exchange-only Kohn–Sham functionals of Chapter 13. The open question is whether there is a quantum theory of the **interacting** field: a space of states with positive probabilities, a Hamiltonian that is bounded below, and predictions that are finite and do not depend on how a calculation is cut off at high energy. The ledger of Section 0.9 lists it as OPEN, and the Stage-1 document says the same (§1.3, item 4: no interacting Fock space or renormalization is constructed).

**Why it is hard.** There are four separate obstacles, and each would be serious on its own.

*(1) The indefinite inner product.* No positive Hilbert space carries the canonical anticommutator (Theorem 8.1). The state space is a Krein space, and every Spin(4,4)-invariant charge density is indefinite (Sections 8.7 and 8.8). Probabilities in quantum theory are squared lengths in a positive space (Section 8.2). The free theory escapes in the good sector, where a positive Fock space exists (Section 8.10), but nobody has shown that an interaction keeps a positive subspace of states invariant.

*(2) Power counting.* Measure every quantity in powers of a mass, with $\hbar=c=1$ (Section 0.6). A length has mass dimension $-1$, so the volume element $d^Dx$ has dimension $-D$, and because the action $\int\mathcal L\,d^Dx$ is a pure number, the Lagrangian density has dimension $D$. The kinetic term $\bar\Psi\gamma^\mu\partial_\mu\Psi$ contains two fields and one derivative (dimension 1), so $2[\Psi]+1=D$, that is

$$
[\Psi]=\frac{D-1}2 .
$$

The mass term $m\bar\Psi\Psi$ then gives $[m]+2[\Psi]=D$, so $[m]=1$, as it should be. The interaction $\lambda(\bar\Psi\Psi)^2$ contains four fields: $[\lambda]+4[\Psi]=D$, so

$$
[\lambda]=D-2(D-1)=2-D,\qquad [\lambda]=-6\ \text{ for }D=8 .
$$

This is the value found in Section 13.8 (check `KS_exchange_couplingDimension`). A coupling of negative mass dimension makes the dimensionless strength of the interaction at an energy $E$, the combination $\lambda E^{D-2}=\lambda E^6$, grow without bound. The standard power-counting argument of quantum field theory (chapter 10 of M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory*, Addison-Wesley 1995; quoted, not derived here) concludes that every higher order of perturbation theory in $\lambda$ needs new kinds of counterterms: the theory is **not renormalisable**. Section 13.8 used the same fact to explain why the Kohn–Sham functional has no correlation term. The four-fermion theory of the weak interaction in four dimensions has the same problem ($[\lambda]=2-4=-2$); it is understood today as the low-energy limit of a renormalisable theory. Whether dirac16complex has such a completion is not known.

*(3) The interaction does not respect the good sector* (derived here). On a slice $x_4=\text{const}$ take the seven slice coordinates periodic, so that every field is a sum of plane waves $e^{i\mathbf k\cdot\mathbf x}$ with allowed wave numbers $\mathbf k=(k_0,k_1,k_2,k_3,k_5,k_6,k_7)$. A term of $\int(\bar\Psi\Psi)^2\,d^7x$ that removes two quanta with wave numbers $\mathbf k_1,\mathbf k_2$ and creates two with $\mathbf k_3,\mathbf k_4$ contains the integral of $e^{i(\mathbf k_1+\mathbf k_2-\mathbf k_3-\mathbf k_4)\cdot\mathbf x}$ over the slice. On a period of length $\ell$ the integral $\int_0^\ell e^{2\pi inx/\ell}dx$ is zero for every integer $n\ne0$, so the term vanishes unless $\mathbf k_1+\mathbf k_2=\mathbf k_3+\mathbf k_4$ in each of the seven directions: momentum is conserved. It is conserved, but it does not forbid two quanta without extra-time momentum ($k_5=0$) from turning into two quanta with $k_5=+q$ and $k_5=-q$. Energy does not forbid it either: by the dispersion relation $E^2=m^2+k_0^2+\dots+k_3^2-k_5^2-k_6^2-k_7^2$ of Section 8.9, two quanta at rest have the energy $2m$, and two quanta with the wave numbers $(k_1,k_5)=(p,q)$ and $(-p,-q)$ have $2\sqrt{m^2+p^2-q^2}$, which equals $2m$ whenever $p^2=q^2$. The final quanta carry extra-time momentum, so their mode Hamiltonian is not Hermitian (Section 8.9) and they lie outside the positive Fock space of Section 8.10. This is a kinematic statement, not a rate: whether the matrix element of such a process vanishes for another reason, for example because of the Krein structure, is part of the open problem.

*(4) No Euclidean shortcut.* The usual tool of quantum field theory for defining and computing loop corrections replaces the time by an imaginary time, which turns the one minus sign of the four-dimensional metric into a plus and makes the metric positive. Here the same step applied to $x_4$ removes only one of the four minus signs of $\eta$: the signature becomes (5,3), still indefinite, and the standard Euclidean methods do not apply directly.

**What is known.**

- PROVED: the Krein structure is forced, $B=-iC\gamma^4$ is Hermitian with eight eigenvalues of each sign, and every invariant density is indefinite (Theorem 8.1, Section 8.8; checks `ALG_chargeFormB`, `ALG_invariantForms` and `QNT_kreinSignature` in both algebra reports of `artifacts/dirac16complex/arbitrary-field/`).
- PROVED by derivation, without a machine check: a positive Fock space and a normal-ordered Hamiltonian $H\ge0$ in the good sector (Section 8.10; Stage-1 document, §10.7).
- PROVED: the first order of perturbation theory in $\lambda$ for quasi-free states, the Hartree–Fock energy $\tfrac\lambda2\bigl[S^2-\mathrm{Tr}(BC\rho BC\rho)\bigr]$ and its exactly local uniform-gas form $e_x=-\tfrac\lambda{32}(n^2+S^2)$ (Section 13.8; checks `KS_exchange_wickTheoremHF` and `KS_exchange_uniformGasClosedForm`). For commuting components the exchange term changes sign (Chapter 14). The checks of the sign are `PAIR_stat_fermionWickMinus` and `PAIR_stat_classicalGaussianWickPlus` of the Stage-5 Wolfram pairing report and their twins with the prefix `S5_` in the independent Python pairing report.
- PROVED: an exact finite Fock model with Krein anticommutators: four modes of the rest sector with $m=1$, a Dirac sea made of the two negative-energy modes, and normal ordering as the subtraction of the sea value (checks `PAIR_T1krein_*` in the Wolfram pairing report and `S5_T1krein_*` in the Python one). It is a free model.
- PROVED: the classical energy of the commuting field dirac16complex00 is not bounded below (check `C00_energy_unboundedBelow` in `wolfram-dirac16complex00-report.json` and `S5_energy_unboundedBelow` in `python-dirac16complex00-report.json`, both in the Stage-5 folder `artifacts/dirac16complex/pair-creation/`). For the anticommuting field the positivity of the good sector comes from the Pauli principle and the filled Dirac sea (Section 8.10), a mechanism that commuting components do not have (`dirac16complex00-theory.json`, key `commutingFieldSpecifics`). No spin–statistics theorem for signature (4,4) is proved (Section 8.15).
- ASSUMED: the Kohn–Sham functional of Chapter 13 is exchange-only, without correlation (Section 13.8).

**Worked example: how coupling two modes of opposite Krein sign can make frequencies complex** (derived here). Take two modes with the Krein form $B=\mathrm{diag}(1,-1)$, the two-mode toy of Section 8.7. A mode Hamiltonian $h$ conserves the Krein norm $u^\dagger Bu$ exactly when $h^\dagger B=Bh$ (the computation of Section 8.9). Write $h=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with complex entries. Then

$$
h^\dagger B=\begin{pmatrix}a^\ast&-c^\ast\\b^\ast&-d^\ast\end{pmatrix},\qquad Bh=\begin{pmatrix}a&b\\-c&-d\end{pmatrix},
$$

and the two agree exactly when $a$ and $d$ are real and $c=-b^\ast$. So the most general Krein-norm-conserving $h$ is

$$
h=\begin{pmatrix}\omega_0&g\\-g^\ast&\omega_1\end{pmatrix},
$$

where $\omega_0$ and $\omega_1$ are the frequencies of the two uncoupled modes and $g$ couples them. Its eigenvalues solve $(\omega_0-x)(\omega_1-x)+\lvert g\rvert^2=0$:

$$
x=\frac{\omega_0+\omega_1}2\pm\sqrt{\Bigl(\frac{\omega_0-\omega_1}2\Bigr)^2-\lvert g\rvert^2}.
$$

They are real when $\lvert g\rvert\le\lvert\omega_0-\omega_1\rvert/2$. For a stronger coupling they form a complex pair, and the solution $e^{-ixt}$ of the eigenvalue with positive imaginary part grows like $e^{\kappa t}$ with $\kappa=\sqrt{\lvert g\rvert^2-(\omega_0-\omega_1)^2/4}$. Compare two modes of the same Krein sign ($B=1$): then the condition is $h^\dagger=h$, that is $c=b^\ast$, the eigenvalues are $\tfrac{\omega_0+\omega_1}2\pm\sqrt{(\omega_0-\omega_1)^2/4+\lvert g\rvert^2}$, and they are real for every coupling. With numbers: $\omega_0=3$, $\omega_1=1$, so the threshold is $\lvert g\rvert=1$. For $g=\tfrac12$ the eigenvalues are $2\pm\sqrt{3}/2=2.866025$ and $1.133975$; for $g=2$ they are $2\pm i\sqrt3$, and the growth rate is $\kappa=\sqrt3=1.732051$. Exercise 8.11 was the case $\omega_0=\omega_1=0$, $g=1$.

The toy explains the extra-time instability of Chapter 8 exactly. At rest the mode Hamiltonian is $h=-im\gamma^4-k_5\gamma^4\gamma^5$ for a wave number $k_5$ along $x_5$. Its first term commutes with $B$ and has the eigenvalues $\pm m$. Its second term anticommutes with $B$ (Section 8.9) and with $\gamma^4$, because $\gamma^4(\gamma^4\gamma^5)=-\gamma^5=-(\gamma^4\gamma^5)\gamma^4$; so it connects a mode of energy $+m$ and one Krein sign with a mode of energy $-m$ and the other. The toy with $\omega_0=m$, $\omega_1=-m$ and $\lvert g\rvert=\lvert k_5\rvert$ has the eigenvalues $\pm\sqrt{m^2-k_5^2}$, exactly the frequencies $\pm E$ of Section 8.9 at zero 3-momentum, and its frequencies become complex exactly when $k_5^2>m^2$ (at $k_5^2=m^2$ the two eigenvalues coincide and the mode grows linearly, as in Section 8.9; Exercise 18.3). The lesson for an interacting theory is that any interaction which couples modes of opposite Krein sign, as point (3) says the contact interaction can, may destabilise the system once the coupling exceeds half the difference of the frequencies.

**A first step.** (a) Redo the power counting and the toy (Exercises 18.1 to 18.3). (b) Take the exact four-mode Krein Fock model of the Stage-5 pairing package (`wolfram/Dirac16ComplexPairing.wl`, function `checkT1Krein`), add the normal-ordered contact interaction restricted to its four modes, and compute the spectrum of the resulting finite matrix exactly as a function of $\lambda$. In the rest sector the matrix $BC=-i\gamma^4$ of the scalar density commutes with $B$ (Section 8.6), so one expects no mixing of Krein signs there; verify this. (c) Add two modes with extra-time wave numbers $+q$ and $-q$ (their mode Hamiltonian is that of Section 8.9) and the part of the contact interaction that scatters two rest quanta into them (point 3), and follow the eigenvalues as $\lambda$ and $q$ vary: do complex pairs appear, as in the toy? Every step is a finite exact computation and can be checked in sympy as well. (d) For renormalisation, compute the second-order (correlation) energy of the uniform gas of Section 13.8 with an upper cutoff $\Lambda$ on all momenta, and determine how it depends on $\Lambda$; power counting predicts that the dependence cannot be absorbed into $m$ and $\lambda$ (quoted, not derived).

**Where to start.** The Stage-1 document, §10, for the canonical quantization, and these files:

```
artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
artifacts/dirac16complex/arbitrary-field/python-algebra-report.json
wolfram/Dirac16ComplexAlgebra.wl          with scripts/verify_dirac16complex_algebra.wls
scripts/check_dirac16complex_algebra.py   the independent algebra checker
wolfram/Dirac16ComplexPairing.wl          the four-mode Krein Fock model (checkT1Krein)
scripts/check_dirac16complex_pairing.py   its independent twin
artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json
artifacts/dirac16complex/pair-creation/python-pairing-report.json
wolfram/Dirac16ComplexKohnSham.wl         Wick's theorem on an exact Fock space
scripts/grassmann_algebra.py              anticommuting variables
```

### 18.4 Problem 2: the extra times, their instability, and the observed world

**The question.** Two linked questions. (a) The world we observe has one time and three space directions. The theory lives in four space-like and four time-like directions, signature (4,4) (Section 1.12), and the repository says plainly that this is not observed spacetime (`README.md`, "Scientific boundary"). How, if at all, does such a theory describe the observed world? (b) Waves with momentum along the extra times $x_5,x_6,x_7$ do not oscillate but grow (Section 8.9, experiment EXP-5), and every quantum statement and every Kohn–Sham result of this book is restricted **by hand** to the good sector, where nothing depends on the extra times (Section 8.13). Is there a mechanism that suppresses, removes or freezes these modes, and a formulation of the theory whose initial-value problem is well posed, that is, whose solutions exist, are unique and depend continuously on the initial data?

**Why it is hard.**

- *The equation is ultrahyperbolic.* The slices $x_4=\text{const}$ contain three time-like directions. For $E^2<0$ the growth rate $\kappa=\sqrt{k_5^2+k_6^2+k_7^2-m^2-k_0^2-\dots-k_3^2}$ of Section 8.9 is unbounded as the extra-time momentum grows, so an arbitrarily small change of the initial data with a short enough wavelength grows arbitrarily fast: the solution does not depend continuously on its data. This is the classical argument against several time directions (see, for example, M. Tegmark, "On the dimensionality of spacetime", Class. Quantum Grav. 14, L69 (1997)).
- *The energy is not bounded below*: for a scalar field in 4+4 dimensions (Section 5.7), for the commuting field dirac16complex00 (check `C00_energy_unboundedBelow`), and for dirac16complex outside the good sector.
- *The notebook's background makes it worse.* When 3-space inflates, the extra times deflate, the physical extra-time momentum grows like $e^{a_4}$, and every mode with extra-time momentum eventually passes the onset of growth (Section 8.13).
- *The extra dimensions are not stabilised.* In EXP-2, 8-dimensional Einstein gravity with this matter ends with all seven directions other than $x_4$ expanding equally, so that an observer in 3-space sees the effective equation of state $w_{\mathrm{eff}}\to4/3$; EXP-3 and EXP-4 simply assume static extra dimensions (Section 11.13).
- *The brane does not remove the extra times.* The metric induced on the brane of the Z2 construction (Section 9.16) is $h=\mathrm{diag}(e^{2a_{4,0}},e^{2a_{4,0}},e^{2a_{4,0}},-1,-e^{-2a_{4,0}},-e^{-2a_{4,0}},-e^{-2a_{4,0}})$: three positive and four negative entries, signature (3,4). The Kohn–Sham particles do gather near the brane (between 86.7 and 96.2 percent of them lie within $1/H$ of it for $m=1$, Section 13.11), which hides the direction $x_0$; but a world on the brane still has four time-like directions.

**What is known.**

- PROVED: the flat-space mode Hamiltonian satisfies $h_k^2=E^2$, it is Hermitian exactly when there is no extra-time momentum, and it always conserves the Krein norm (Section 8.9; check `QNT_flatModeHamiltonian` in both algebra reports).
- COMPUTED (EXP-5, Section 8.13; the numbers are in `artifacts/dirac16complex/numerics/exp5/summary.json`): for the comoving extra-time momenta $q=0.05$ and $0.1$ ($m=1$) the growth starts at $t_\ast=\ln(m/q)=2.99573$ and $2.30259$; the Hilbert norm grows to $1.258\times10^{16}$ and $1.313\times10^{16}$ by $x_4=t_\ast+3$, while the Krein norm drifts by at most $1.08\times10^{-9}$ relative.
- ASSUMED: the restriction to the good sector (Section 8.13).
- COMPUTED: the EXP-2 result on the extra dimensions quoted above (Section 11.13).

**Worked example 1: which modes keep oscillating** (derived here, with the frozen-coefficient estimate of Section 8.13). In the notebook's field a mode with 3-momentum $k_1$ along $x_1$ and extra-time momentum $k_5$ along $x_5$ has, with frozen coefficients,

$$
E^2=M_{\mathrm{eff}}^2+K^2+\bigl(k_1e^{-H\zeta-a_4}\bigr)^2-\bigl(k_5e^{-H\zeta+a_4}\bigr)^2
$$

(Section 8.13), with further terms of the same two kinds for $k_2,k_3$ and $k_6,k_7$. Three histories of $a_4$ behave differently.

1. *$a_4$ grows without bound* (the notebook's $a_4=t$). The factor $e^{a_4}$ grows and $e^{-a_4}$ shrinks. If any extra-time momentum is nonzero, the last term eventually dominates and $E^2<0$: the mode grows from then on. If all extra-time momenta vanish, $E^2\ge M_{\mathrm{eff}}^2+K^2\ge0$ at every time. So in this history **the good sector is exactly the set of modes that oscillate forever**.
2. *$a_4$ constant* (the static member of Chapter 13). Then $E^2$ does not change with time at a fixed position $\zeta$, and a mode that oscillates at the start oscillates forever. The set of oscillating modes is larger than the good sector: it contains every mode with $E^2\ge0$.
3. *$a_4$ decreasing without bound.* Now the extra-time terms shrink, and every mode eventually oscillates.

The good sector is therefore singled out dynamically only by the notebook's inflating history, and even there generic initial data contain the other modes; the calculation identifies the good sector, it does not remove the rest.

**Worked example 2: compact extra times do not help** (derived here). One might hope that rolling up the extra times into small circles, as is done with extra space dimensions, would remove the dangerous modes. Let $x_5$ be a circle of circumference $2\pi R$. A field on it is periodic, so $k_5=n/R$ with an integer $n$. In flat space

$$
E^2=m^2+\lvert\mathbf k\rvert^2-\frac{n^2}{R^2},
$$

where $\lvert\mathbf k\rvert^2=k_0^2+\dots+k_3^2$. For every radius $R$ and every $\mathbf k$ the modes with $\lvert n\rvert>R\sqrt{m^2+\lvert\mathbf k\rvert^2}$ have $E^2<0$ and grow. A small circle makes the first growing mode appear at a smaller $\lvert n\rvert$, not later: with $m=1$, $\mathbf k=0$ and $R=2$, the modes $n=\pm1$ oscillate ($E^2=\tfrac34$), $n=\pm2$ grow linearly ($E^2=0$) and every $\lvert n\rvert\ge3$ grows exponentially (Exercise 18.5).

**A known idea from the literature.** For the constant-coefficient ultrahyperbolic wave equation, W. Craig and S. Weinstein showed that the initial-value problem becomes well posed when the initial data satisfy a nonlocal constraint ("On determinism and well-posedness in multiple time dimensions", Proc. R. Soc. A 465, 3023 (2009)). For the mode equation of Section 8.9 the natural constraint of this kind keeps only the modes with $E^2\ge0$. Worked example 1 shows what that means in the notebook's background: with an inflating $a_4$, the only modes that satisfy such a constraint for all times are those of the good sector.

**A first step.** (a) Extend the reduced Kohn–Sham equation of Section 13.3 by an extra-time momentum and study its spectrum. With the ansatz factor $e^{ik_5x_5}$ and the curved gamma $\gamma^{x_5}=e^{-Hy+a_{4,0}}\gamma^5$ of Section 13.3, the reduced equation acquires the term $-i\,e^{-Hy+a_{4,0}}k_5\,\gamma^0\gamma^5\chi$ on its right-hand side. By the two rules of Section 13.4, $\gamma^0\gamma^5$ anticommutes with $J=\gamma^0\gamma^1\gamma^4$ and with $K_2=\gamma^5\gamma^6$ and commutes with $K_1=\gamma^2\gamma^3$ (derived here; Exercise 18.4 asks for the details). It therefore maps the block $(j,s_2,s_3)$ onto $(-j,s_2,-s_3)$: the eight $2\times2$ blocks couple in pairs into four $4\times4$ systems, and the two-component methods of Chapter 13 (the Prüfer angle of Section 13.10) no longer apply. A matrix method such as that of `scripts/ks_reference_solver.py` shows complex eigenvalues directly; the question is whether they appear and where the corresponding modes live in $y$. (b) Reproduce the EXP-5 onset times for other momenta with the committed program. (c) For question (a) of the problem, study the literature on theories with several times, and ask which structure could turn the three extra times into something unobservable; the observations above (the brane has signature (3,4), compactification does not help) rule out the two simplest answers.

**Where to start.** The Stage-1 document, §10.10, the Stage-2 document, §14.3, and these files:

```
artifacts/dirac16complex/numerics/exp5/            the EXP-5 outputs
studies/dirac16complex_cosmology/src/exp5.rs       the EXP-5 program
scripts/check_dirac16complex_exp5.py               its independent checker
studies/dirac16complex_cosmology/src/exp2.rs       EXP-2 (8-dimensional Einstein gravity)
studies/dirac16complex_kohn_sham/src/blocks.rs     the 2x2 block reduction
studies/dirac16complex_kohn_sham/src/shooting.rs   the shooting method
scripts/ks_reference_solver.py                     the matrix method
```

### 18.5 Problem 3: what determines $a_4$, and Einstein–Lovelock gravity

**The question.** The primordial field contains one arbitrary function, $a_4(t)$ (Section 9.2). The notebook intends it to be fixed by the Einstein–Lovelock equations of eight dimensions, with the Lovelock terms of orders 2 and 3 (cell 14; Sections 4.9 and 9.9), but no code of the notebook defines those terms and the project does not compute them either. In 8-dimensional Einstein gravity the field needs the energy density $\rho_{\mathrm{req}}=-3H^2(7+a_4'^2)/\kappa\le-21H^2/\kappa<0$ for every $a_4$ (Section 9.10), and the weak, null and dominant energy conditions fail (Section 9.11). The open questions: (a) do the Einstein–Lovelock equations with the orders 2 and 3 admit the notebook's field as a vacuum solution, or with a source of positive energy? (b) Which equation fixes $a_4$? (c) Can the slopes $a_4'=\tfrac23(M\mp1)$ that the notebook lists in cell 150 without derivation (Section 9.10) be derived?

**Why it is hard.** The Lovelock tensors of orders 2 and 3 are quadratic and cubic in the curvature; written with the generalized Kronecker delta (Section 4.9) they contain determinants with five and seven rows, and for a time-dependent $a_4$ they give nonlinear equations in $a_4'$ and $a_4''$. At the brane of the Z2 construction the Israel junction condition of Section 9.16 holds only for Einstein gravity; with a Gauss–Bonnet term it acquires further terms (derived in the literature, for example S. C. Davis, "Generalized Israel junction conditions for a Gauss–Bonnet brane world", Phys. Rev. D 67, 024030 (2003)). What "physically acceptable" means in signature (4,4) is itself unsettled, since the energy conditions of Section 9.11 are conditions for one observer and one choice of null vectors, not a complete classification. And the normalisation that the notebook intends for its Lovelock1, Lovelock2 and Lovelock3 is not recorded.

**What is known.**

- PROVED (Chapter 9, Stage-2 checks `P_einstein_requiredSource`, `P_einstein_rhoRequiredNegative`): the Einstein tensor for every $a_4$ and the negative required energy density.
- PROVED (Proposition 9.2; check `P_source_einsteinTransverseDifferenceIs2H2a4pp`): in Einstein gravity no dirac16complex state that depends on $x_0$ and $x_4$ only can be the source where $a_4''\ne0$. Read the other way round (derived here, one line): with such a source the field equations **force** $a_4''=0$, so $a_4$ is linear, $a_4=ct$ plus a constant; and by condition (3) of Proposition 9.4, $\lambda S^2=2H^2(15-3c^2)/\kappa$, the slope is fixed by the source, $c^2=5-\kappa\lambda S^2/(6H^2)$. In Einstein gravity with a homogeneous dirac16complex source, $a_4$ is therefore determined up to the sign of its slope and an additive constant, but only for a source of negative energy density.
- PROVED (Section 4.9): in eight dimensions only the Lovelock orders $k=0,1,2,3$ exist.
- PROVED (Section 9.15; checks `KS_geometry_constantCurvatureSevenSpace` and `KS_geometry_kretschmannConstant` in `wolfram-kohn-sham-report.json`): the static member ($a_4$ constant) is the product of the flat time line $x_4$ with a seven-dimensional space of constant curvature $-H^2$ in the directions $y,x_1,x_2,x_3,x_5,x_6,x_7$.

**Worked example: the Lovelock tensors of the static member** (derived here). No program of the repository computes the Lovelock terms of orders 2 and 3, and Chapter 16 records them as not computed. The derivation below is a first step toward changing that status, and the status changes only when the result has been checked exactly by machine. The last fact of the list above makes every Lovelock tensor of the static member computable by counting. Call the seven directions $y,x_1,x_2,x_3,x_5,x_6,x_7$ the set $\Sigma$ ($n=7$ elements) and put $K=-H^2$.

*Step 1: the curvature.* Constant curvature $K$ means $R_{rsmn}=K(g_{rm}g_{sn}-g_{rn}g_{sm})$ for indices in $\Sigma$ (Section 9.15). Raising indices as in Section 4.9, $R^{\alpha\beta}{}_{\mu\nu}=g^{\beta\lambda}R^\alpha{}_{\lambda\mu\nu}=K\bigl(\delta^\alpha_\mu\delta^\beta_\nu-\delta^\alpha_\nu\delta^\beta_\mu\bigr)=K\,\delta^{\alpha\beta}_{\mu\nu}$ for $\alpha,\beta,\mu,\nu\in\Sigma$. Every component with an index 4 vanishes, because $x_4$ is a flat factor.

*Step 2: the contraction.* In $E_{(k)}{}^\mu{}_\nu=-\frac1{2^{k+1}}\,\delta^{\mu\,\alpha_1\beta_1\cdots\alpha_k\beta_k}_{\nu\,\gamma_1\delta_1\cdots\gamma_k\delta_k}R^{\gamma_1\delta_1}{}_{\alpha_1\beta_1}\cdots R^{\gamma_k\delta_k}{}_{\alpha_k\beta_k}$ (Section 9.9) insert $R^{\gamma_i\delta_i}{}_{\alpha_i\beta_i}=K\bigl(\delta^{\gamma_i}_{\alpha_i}\delta^{\delta_i}_{\beta_i}-\delta^{\gamma_i}_{\beta_i}\delta^{\delta_i}_{\alpha_i}\bigr)$. Summing over $\gamma_i,\delta_i$ replaces them in the generalized delta by $\alpha_i,\beta_i$, once directly and once in exchanged order; the exchange of two lower indices flips the sign of the determinant, so the two terms add. Each factor gives $2K$, and

$$
E_{(k)}{}^\mu{}_\nu=-\frac{K^k}2\,\delta^{\mu\,\alpha_1\beta_1\cdots\alpha_k\beta_k}_{\nu\,\alpha_1\beta_1\cdots\alpha_k\beta_k},
$$

where the $2k$ repeated indices are summed over $\Sigma$ only.

*Step 3: counting.* The generalized delta with the same list of indices above and below is $+1$ when all its indices are different (the determinant of the unit matrix) and 0 when two coincide (two equal rows). For $\mu\ne\nu$ the lower list would have to be a rearrangement of the upper one, which needs $\nu=\mu$, so all off-diagonal components vanish. For $\mu=\nu$ the sum counts the ordered lists of $p=2k$ different elements of $\Sigma$ that are also different from $\mu$. If $\mu\in\Sigma$ there are $n-1=6$ elements to choose from, and the number of such lists is $6\cdot5\cdots(7-p)=6!/(6-p)!$. If $\mu=4$, which is not in $\Sigma$, there are $n=7$, and the number is $7!/(7-p)!$. Hence, with no sum over $\mu$,

$$
E_{(k)}{}^\mu{}_\mu=-\frac{K^k}2\cdot\frac{6!}{(6-2k)!}\ \ (\mu\in\Sigma),\qquad E_{(k)}{}^4{}_4=-\frac{K^k}2\cdot\frac{7!}{(7-2k)!}.
$$

With $K=-H^2$:

| $k$ | $6!/(6-2k)!$ | $7!/(7-2k)!$ | $E_{(k)}$ on each of the seven directions | $E_{(k)}{}^4{}_4$ |
| --- | --- | --- | --- | --- |
| 0 | 1 | 1 | $-\tfrac12$ | $-\tfrac12$ |
| 1 | 30 | 42 | $15H^2$ | $21H^2$ |
| 2 | 360 | 840 | $-180H^4$ | $-420H^4$ |
| 3 | 720 | 5040 | $360H^6$ | $2520H^6$ |

The row $k=1$ is the Einstein tensor $G^\mu{}_\nu=\mathrm{diag}(15,15,15,15,21,15,15,15)H^2$ of Section 9.15, verified there by `KS_geometry_einsteinMixedDiag`: the method passes its first test.

*Step 4: the field equations.* The Einstein–Lovelock equations $\sum_k\alpha_kE_{(k)}{}^\mu{}_\nu=\kappa T^\mu{}_\nu$ (Section 4.9) with $\rho=-T^4{}_4$ and the pressure $p=T^\mu{}_\mu$ (no sum) in each of the seven directions become two equations:

$$
\begin{aligned}
\kappa\,\rho_{\mathrm{req}}&=\tfrac12\alpha_0-21\alpha_1H^2+420\alpha_2H^4-2520\alpha_3H^6,\\
\kappa\,p_{\mathrm{req}}&=-\tfrac12\alpha_0+15\alpha_1H^2-180\alpha_2H^4+360\alpha_3H^6 .
\end{aligned}
$$

For Einstein gravity ($\alpha_1=1$, all others 0) they give back $\rho_{\mathrm{req}}=-21H^2/\kappa$ and $p_{\mathrm{req}}=15H^2/\kappa$ (Section 9.15). Two consequences follow.

- *The sign of the required energy can change.* With $\alpha_1=1$, $\alpha_0=\alpha_3=0$ and a Gauss–Bonnet coefficient $\alpha_2$: $\kappa\rho_{\mathrm{req}}=H^2(420\alpha_2H^2-21)$, which is positive when $\alpha_2>1/(20H^2)$. For example $\alpha_2=1/(10H^2)$ gives $\rho_{\mathrm{req}}=21H^2/\kappa>0$ and $p_{\mathrm{req}}=-3H^2/\kappa$ (Exercise 18.7).
- *The static member can be a vacuum solution.* Both right-hand sides vanish exactly when their sum and the second one vanish. The sum is $\kappa(\rho_{\mathrm{req}}+p_{\mathrm{req}})=-6\alpha_1H^2+240\alpha_2H^4-2160\alpha_3H^6=-6H^2\bigl(\alpha_1-40\alpha_2H^2+360\alpha_3H^4\bigr)$, so the conditions are

$$
\alpha_1-40\alpha_2H^2+360\alpha_3H^4=0,\qquad \alpha_0=2\bigl(15\alpha_1H^2-180\alpha_2H^4+360\alpha_3H^6\bigr).
$$

For $\alpha_1=1$ and $\alpha_3=0$: $\alpha_2=1/(40H^2)$ and $\alpha_0=21H^2$, that is a negative cosmological constant $\Lambda=-\tfrac12\alpha_0=-\tfrac{21}2H^2$ in the convention $\alpha_0=-2\Lambda$ of Section 4.9. Read the other way, given the couplings $\alpha_k$ the vacuum condition fixes $H$.

**What the worked example does not settle.** It is derived here and has not been checked by any program. It covers only the static member, in the bulk $y<0$; the notebook's inflating $a_4$ needs $E_{(2)}$ and $E_{(3)}$ for a time-dependent $a_4$, which are not computed. The brane at $y=0$ needs the Gauss–Bonnet junction conditions, which are not computed. Whether couplings of this size give a physically acceptable theory (for example, whether small perturbations of this background grow) is not examined. And the notebook's normalisation of its Lovelock terms is unknown, so nothing here says which values of its numbers $w_1,w_2,w_3$ and $\Lambda$ (cell 14) this corresponds to.

**A first step.** (a) Verify the table exactly by machine, twice. The Wolfram package `wolfram/Dirac16ComplexKohnSham.wl` already computes the Riemann tensor of the static member (it is used by `KS_geometry_constantCurvatureSevenSpace`); add the generalized-delta contractions for $k=2,3$. Do the same independently in sympy, starting from the geometry engine `scripts/d16c_geometry_sympy.py`. Include a negative control, for example a metric that is not of constant curvature. (b) Compute $E_{(2)}$ and $E_{(3)}$ for the notebook's metric with a general $a_4(t)$; the Stage-2 package `wolfram/Dirac16ComplexPrimordial.wl` computes its Riemann tensor exactly. Write the Einstein–Lovelock equations as ordinary differential equations for $a_4$, in vacuum and with the homogeneous source of Proposition 9.4, and ask whether the slopes of cell 150 appear. (c) Derive the junction conditions at the brane in the Gauss–Bonnet case.

**Where to start.** Chapter 9; the Stage-2 document (§15 for the source, §5 to §7 for the curvature); the Stage-4 specification, §1; D. Lovelock, J. Math. Phys. 12, 498 (1971), cited in Section 4.9; and these files:

```
wolfram/Dirac16ComplexPrimordial.wl       the primordial field, any a4 (Stage 2)
scripts/check_dirac16complex_primordial.py
artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json
wolfram/Dirac16ComplexKohnSham.wl         the static member and its brane (Stage 4)
scripts/check_dirac16complex_kohn_sham_theory.py
artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json
scripts/d16c_geometry_sympy.py            the independent sympy geometry engine
handoff/specs/STAGE4_SPEC.md
```

### 18.6 Problem 4: can a Kohn–Sham state be the source of the primordial field?

**The question.** In 8-dimensional Einstein gravity the static member of the primordial field needs the source $\rho_{\mathrm{req}}=-21H^2/\kappa$ and $p_{\mathrm{req}}=+15H^2/\kappa$ in all seven directions other than $x_4$ (Section 9.15). A homogeneous state $\Psi=u(x_4)$ is an exact source exactly when its three-gamma bilinears vanish, $mS=-36H^2/\kappa$ and $\lambda S^2=30H^2/\kappa$ (Proposition 9.4 with $c=0$; erratum E4.1 of `handoff/specs/STAGE4_SPEC.md`). Chapter 13 asked whether a Kohn–Sham state of finitely many quanta can meet these conditions and found that no computed state does (Section 13.14). The open question is whether **any** many-particle state of dirac16complex, or of dirac16complex00, can be the source of the static field: in the fixed field, or self-consistently, with the metric computed from the state (back-reaction).

**Why it is hard.**

- *Sign.* The field needs a negative energy density; every computed state with band or bulk levels has a positive proper-volume average $\langle\rho\rangle$, so the match would need a negative gravitational coupling (Section 13.14). In the good sector the free, normal-ordered energy is not negative (Section 8.10), so a negative energy must come from the interaction or from a negative-energy sector.
- *Strength.* The two conditions together need $\lambda\langle S_p\rangle/m=-\tfrac56$; at first order this means $\hat\lambda\approx105.7$ for $N=112$ and $9.55$ for $N=1016$, $10^3$ to $10^4$ times the largest coupling used, far outside the range for which the local exchange-only scheme was set up (Section 13.14; column `lambda_hat_needed_first_order` of `artifacts/dirac16complex/kohn-sham/rust/emt/emt-summary.csv`).
- *Shape.* The required source is the same at every $y$, while the computed energy density varies by orders of magnitude: between 0.00865 and 3.495 for $N=112$ and between 0.181 and 4768 for $N=1016$ (both at $\lambda=0$, $m=H=1$; columns `rho_min` and `rho_max` of the same file).
- *Back-reaction.* If the metric is computed from the state, the orbitals and the metric must be found together: a coupled nonlinear boundary-value problem in $y$ that nobody has set up.

**What is known.**

- PROVED (Proposition 9.4): exact homogeneous sources exist in the c-number (mean-field) reading of the bilinears, always with negative energy density. The Stage-2 report checks them in `P_source_x0IndependentSourceConditions` and `P_source_x0IndependentExactExamples`.
- PROVED for the commuting field: an exact classical solution of dirac16complex00 that is the source of the static field, with $m=-30$, $\lambda=\tfrac{125}6$, $S=\tfrac65$, $M_{\mathrm{eff}}=m+\lambda S=-5$, $\rho=-21$, $p=15$, $w=-\tfrac57$ in units $H=\kappa=1$ (`artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json`, key `primordial.staticSourceExample`; checks `C00_primordial_staticFieldSourcedExactly` and `S5_primordial_staticFieldSourcedExactly`). Indeed $mS=-36$, $\lambda S^2=\tfrac{125}6\cdot\tfrac{36}{25}=30$, $\rho=mS+\tfrac\lambda2S^2=-36+15=-21$ and $p=\tfrac\lambda2S^2=15$. Its negative energy density is possible because the classical energy of dirac16complex00 is not bounded below (Section 18.3).
- COMPUTED: no Kohn–Sham state meets the conditions (the column `sourcing_conditions_met` of `rust/emt/emt-summary.csv` is 0 in every row; Section 13.14).
- PROVED (Stage 5, Theorem T3; Section 13.14): the $-M$ universe with transformed boundary conditions has the same energies and pressures as the $+M$ universe and the opposite scalar density, so $mS$ and $\lambda S^2$ are unchanged: the mirror universe does not help.
- PROVED (Stage 5; `artifacts/dirac16complex/pair-creation/pairing-theory.json`, key `T3.theoremImageRule`; check `PAIR_totals_ksKreinImagePair`): the Krein image of a Kohn–Sham state (the $\gamma^8$ image with the Krein metric $-B$ and the coupling $-\lambda$) has the same orbitals and eigenvalues, the number density reversed ($n\to-n$), the scalar density unchanged ($S\to S$), and every energy and every component of the energy–momentum tensor reversed.

**Worked example 1: the fixed static field needs a uniform and isotropic source** (derived here). By the table of Section 18.5 every Lovelock tensor $E_{(k)}$ of the static member is diagonal and constant, with the same value on all seven directions $y,x_1,x_2,x_3,x_5,x_6,x_7$. Whatever the coefficients $\alpha_k$, the Einstein–Lovelock equations for the fixed static member therefore demand a source whose energy density is the same at every point and whose pressure is one and the same constant in all seven directions. The Kohn–Sham states are neither uniform (see "Shape" above) nor isotropic: for $N=112$ at $\lambda=0$ the proper-volume averages are $\langle p_y\rangle=0.0103747$, $\langle p_3\rangle=0.0068653$ and $\langle p_t\rangle=0$ (`rust/emt/emt-summary.csv`); without interaction the extra times carry no pressure at all (Section 13.14). So in the **fixed** static field these states are excluded in every Einstein–Lovelock theory, not only in Einstein gravity. The exact homogeneous sources above are isotropic by construction: their pressure is $SU'(S)-U(S)$ in all seven directions (Proposition 9.4). A Kohn–Sham state held near a brane is a different kind of object, and the remaining possibility is to let the metric respond.

**Worked example 2: what back-reaction demands** (derived here). Call a metric **ultrastatic** if it is diagonal, $g_{44}=-1$, and no entry depends on $x_4$. The static member is ultrastatic, and so is every static warp $W(y)$ of Section 9.16. For such a metric every Christoffel symbol with an index 4 vanishes, by the rules of Section 9.6: $\Gamma^p{}_{4p}=\tfrac12\partial_4\ln\lvert g_{pp}\rvert=0$ and $\Gamma^4{}_{\mu4}=\tfrac12\partial_\mu\ln\lvert g_{44}\rvert=0$ by (C1), $\Gamma^4{}_{pp}=-\partial_4g_{pp}/(2g_{44})=0$ and $\Gamma^\rho{}_{44}=-\partial_\rho g_{44}/(2g_{\rho\rho})=0$ by (C2), and those with three different indices by (C3). Every term of $R_{44}=\partial_\rho\Gamma^\rho{}_{44}-\partial_4\Gamma^\rho{}_{\rho4}+\Gamma^\rho{}_{\rho\lambda}\Gamma^\lambda{}_{44}-\Gamma^\rho{}_{4\lambda}\Gamma^\lambda{}_{\rho4}$ contains such a symbol, so $R_{44}=0$. Section 9.11 derived from the trace-reversed Einstein equations that $5\rho+\sum_{\mu\ne4}p_{(\mu)}=6R_{44}/\kappa$. Hence, in 8-dimensional Einstein gravity, every source of an ultrastatic metric must satisfy at every point

$$
5\rho+p_y+3p_3+3p_t=0,
$$

with $p_3$ the average 3-space pressure and $p_t$ the pressure along each extra time (or, in general, the sum of the seven pressures in place of $p_y+3p_3+3p_t$). Matter with $\rho>0$ and non-negative pressures can never do this: an ultrastatic geometry needs matter that exactly saturates the strong energy condition along $x_4$. (The same computation in four dimensions gives $\rho+3p=0$, the condition that made Einstein add a cosmological constant to obtain his static universe of 1917; Exercise 18.9.) Both exact sources above pass the test: for Proposition 9.4 with $c=0$, $5(mS+U)+7(SU'-U)=5mS+6\lambda S^2=5(-36)+6\cdot30=0$ in units $H=\kappa=1$, and for the dirac16complex00 example $5(-21)+7\cdot15=0$ (Exercise 18.8).

For a Kohn–Sham state in the static member insert the energy–momentum tensor of Section 13.14, $\rho=\sum_nw_n\varepsilon_nn_n-L_s$, $p_y=\sum_nw_n(\varepsilon_nn_n-ms_n-\kappa k_nt_n)-L_s$, $p_3=\tfrac13\sum_nw_n\kappa k_nt_n+L_s$ and $p_t=L_s$. The interaction terms cancel ($-5-1+3+3=0$) and so do the momentum terms:

$$
5\rho+p_y+3p_3+3p_t=6\sum_nw_n\varepsilon_nn_n(y)-m\,S_p(y).
$$

A Kohn–Sham state of the static member could therefore be the source of an ultrastatic metric only if $6\sum_nw_n\varepsilon_nn_n=mS_p$ at every $y$. (For a general warp the Kohn–Sham tensor has to be derived again, and whether the identity keeps this form is part of the first step below.) The committed states are far from it. Evaluated on the committed profiles (`rust/emt/<run>/profiles.csv`, columns `rho`, `p_y`, `p_3`, `p_t`), the left-hand side lies between 0.0519 and 27.07 for $N=112$ and between 1.085 and 28609 for $N=1016$ (both at $\lambda=0$), and in those files the identity with $6(\rho+L_s)-mS_p$ on the right holds to rounding (Exercise 18.10). The free state with $N=8$ satisfies the condition trivially, because its whole energy–momentum tensor vanishes (the eight zero modes have $\varepsilon=0$ and $S_p=0$, Section 13.11); but a vanishing tensor is the source only of a vacuum metric, and the static member is not a vacuum solution of Einstein gravity.

**Worked example 3: the Krein image of a computed state.** Take $N=112$ at $\lambda=0$ (`rust/emt/emt-summary.csv`, $m=H=1$): $\langle\rho\rangle=0.0230891$ and $\langle S_p\rangle=-0.00788147$. Its Krein image has $\langle\rho\rangle=-0.0230891$, negative as the field needs, and matching $\rho_{\mathrm{req}}=-21/\kappa$ on average gives $\kappa=21/0.0230891=909.5>0$. But the image carries the mass $-m=-1$ and the unchanged $\langle S_p\rangle$, so the mass condition, used on averages as a diagnostic exactly as in Section 13.14, reads $(-1)(-0.00788147)=-36/\kappa$ and gives $\kappa=-4568<0$. The two conditions contradict each other, the coupling condition $\lambda S^2=30/\kappa$ cannot hold at $\lambda=0$ at all, and the image inherits the anisotropy of worked example 1. The image is not a source either.

**A first step.** (a) Use the necessary condition $6\sum_nw_n\varepsilon_nn_n=mS_p$ as a cheap test for every candidate state; it needs only the committed profiles. (b) Generalise worked example 2 to static metrics in which $g_{44}$ is warped as well, $g_{44}=-e^{2f_4(y)}$: then $R_{44}\ne0$, and Lemma 9.1, with $x_4$ treated as one more fibre direction over the one-dimensional base $y$ (the proof of the lemma works unchanged for a base with one coordinate), gives the new condition. (c) Allow different warps for 3-space and the extra times, $g_{pp}\propto e^{2f_3(y)}$ for $p=1,2,3$ and $e^{2f_t(y)}$ for $p=5,6,7$. Lemma 9.1 with the base $(y,x_4)$, on which nothing depends on $x_4$, gives $R^p{}_p=-(f_p''+\Theta f_p')$ with $\Theta=3f_3'+3f_t'$, hence (derived here)

$$
\kappa\,(p_3-p_t)=G^1{}_1-G^5{}_5=-(f_3''-f_t'')-3(f_3'+f_t')(f_3'-f_t'),
$$

so the pressure difference of the Kohn–Sham states needs $f_3\ne f_t$, that is an $a_4$ that depends on $y$. Then set up the self-consistent problem: the unknown warps, the Kohn–Sham orbitals in that metric, and Einstein's equations as ordinary differential equations in $y$. (d) Combine with Section 18.5: with a Gauss–Bonnet term the required energy density of the static member can be positive, but by worked example 1 the fixed static metric still needs a uniform isotropic source, so back-reaction is needed there as well.

**Where to start.** Section 13.14; the Stage-2 document, §15.5; erratum E4.1 of the Stage-4 specification; and these files:

```
artifacts/dirac16complex/kohn-sham/rust/emt/emt-summary.csv    averages of every state
artifacts/dirac16complex/kohn-sham/rust/emt/<run>/profiles.csv the profiles in y
studies/dirac16complex_kohn_sham/src/emt.rs                    the energy-momentum tensor
studies/dirac16complex_kohn_sham/src/shooting.rs               the shooting method
artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json
artifacts/dirac16complex/pair-creation/pairing-theory.json     key T3: the pairing maps
handoff/specs/STAGE4_SPEC.md
```

### 18.7 Problem 5: the last Stage-4 cross-check and the Stage-4 gate

**The question.** Every number of Chapter 13 was computed by the Rust solver and is to be confirmed by the independent Python reference solver, which uses a matrix method on staggered grids and extrapolates in the grid spacing (Section 13.15). The report of the final cross-check has 63 checks, of which 62 are true:

```
artifacts/dirac16complex/kohn-sham/python-check-report.json   the report
scripts/check_dirac16complex_kohn_sham.py                      its producer
```

The problem is to resolve the one failed check and then to run the Stage-4 gate to the end.

**What is known.** The failed check is `canonical_eigenvalues`. It compares 58412 eigenvalues of the two solvers with the tolerance $10^{-6}\max(1,\lvert\varepsilon\rvert/m)\,m$ plus a small grid term, and its worst deviation is $2.195\times10^{-6}$ against the tolerance $1.054\times10^{-6}$ (ratio 2.08). All its failures belong to the run `m1_L3_N1016_lamm2_T0`, the smeared ensemble at the attractive coupling $-\hat\lambda_2$ of Sections 13.11 and 13.12: two deep levels of the Dirac sea at $k=0$, one in each parity sector, each in both block types, and each appearing in the ground-state and in the excited-state record of that run. Everything else about the run agrees: the ground-state energy (Rust 1126.8580930, reference 1126.8580892, deviation $3.8\times10^{-6}$ against a tolerance of $1.1\times10^{-3}$) and the Kohn–Sham gap (deviation $1.8\times10^{-8}$), both from the `comparisons` block of the report. The Delta-SCF of this run, the one open number of Section 13.12, now agrees: the reference on the finer grids 120/240/480 gives 0.0436199531, against the Rust values 0.0436193591 (601 points) and 0.0436196717 (extrapolated from 301 and 601 points) (erratum E4.13 of `handoff/specs/STAGE4_SPEC.md`).

The worse of the two failing levels is the $k=0$ sea level of parity $+$ whose free value is $-1.447972$, the negative-energy partner of the $k=0$ bulk level that the attraction pulls down to the Fermi level (Section 13.11); the other is the $k=0$ sea level of parity $-$ whose free value is $-1.292293$ (Section 13.6). The interaction moves both up, and three committed files give their eigenvalues:

| Source | File (under `artifacts/dirac16complex/kohn-sham/`) | $\varepsilon$, parity $+$ | $\varepsilon$, parity $-$ |
| --- | --- | --- | --- |
| Rust, 301 points (canonical) | `rust/scf/m1_L3_N1016_lamm2_T0/levels.csv` | $-1.05374908333$ | $-0.98844655130$ |
| Rust, 601 points | `rust/excited/m1_L3_N1016_lamm2_T0_g601/levels.csv` | $-1.05374707094$ | $-0.98844473928$ |
| reference, grids 120/240/480, extrapolated | `reference/m1_L3_N1016_lamm2_T0/spectrum.csv` | $-1.05374688831$ | $-0.98844457574$ |

For the level of parity $+$ the differences are: Rust (301) minus reference $=-2.195\times10^{-6}$, the failing deviation; Rust (601) minus reference $=-1.83\times10^{-7}$, well inside the tolerance; Rust (301) minus Rust (601) $=-2.012\times10^{-6}$. The level of parity $-$ shows the same pattern ($-1.976\times10^{-6}$, $-1.64\times10^{-7}$ and $-1.812\times10^{-6}$). The committed numbers therefore suggest that both deviations are the grid error of the 301-point Rust run for these two deep sea levels. That is a hypothesis to test, not a result. The checker already adds the measured Rust grid uncertainty $\lvert X(601)-X(301)\rvert$ to the tolerances of the ground-state energy, the chemical potential, the Kohn–Sham gap, the Delta-SCF energy and the lowest particle–hole energy of a run with a 601-point partner (erratum E4.12; function `rust_grid_uncertainties` of the checker), but not to single eigenvalues.

**Why it is hard.** Not conceptually; the difficulty is discipline. This run is the hardest of Stage 4: two levels cross at the Fermi level, the ground state is an ensemble with smeared occupations, and the nonlinear problem has more than one self-consistent solution (an exploratory reference run on finer grids converged to a state about $1.01\,m$ higher; Section 13.11). A tolerance may be changed only on the basis of a measurement, and the change must be recorded.

**A first step.** (1) Test the hypothesis: solve the run on a finer $y$ grid (1201 points, say) with the Rust solver, and check that its values of the two levels move toward the reference values in the way Richardson's rule of Section 10.11 predicts for a grid error. (2) If it does, decide, with that measurement, whether the rule of erratum E4.12 should be extended to single eigenvalues of runs with a finer-grid partner (Exercise 18.11 shows that the check would then pass), and record the decision as a new erratum of the Stage-4 specification. Enlarging the tolerance without such a measurement would be a weakened check, which the project does not allow. (3) Rerun the checker. (4) Run the gate: `scripts/verify_stage4_kohn_sham.ps1` in PowerShell or `bash scripts/verify_stage4_kohn_sham.sh`, first with `-DryRun` (PowerShell) or `--dry-run` (Bash), which prints every step and its expected wall time without running anything. The gate requires a fresh checker report without a failed check, and it rebuilds and verifies the two Stage-4 PDFs, which do not exist yet: the Stage-4 document exists only as the Markdown draft `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.md`, and the Stage-4 student guide is not written. A full run takes hours; the header of the PowerShell gate estimates about three hours for the Rust step alone. Chapter 19 describes the gates in general.

**Where to start.** The entries `checks`, `measurements` and `comparisons` of the cross-check report, the Stage-4 row of `HANDOFF.md`, and these files:

```
artifacts/dirac16complex/kohn-sham/python-check-report.json
scripts/check_dirac16complex_kohn_sham.py        the checker (rust_grid_uncertainties)
scripts/ks_reference_solver.py                   the reference (its list canonical_runs)
studies/dirac16complex_kohn_sham/README.md       the Rust solver
scripts/verify_stage4_kohn_sham.ps1              the gate (PowerShell)
scripts/verify_stage4_kohn_sham.sh               the gate (Bash)
```

### 18.8 Problem 6: the Stage-5 numerics

**The question.** Theorem T4 of `handoff/specs/STAGE5_SPEC.md` asks for a numerical demonstration of the Kohn–Sham pairing theorem T3 (Chapter 15): the ground and first excited states of three universes, the $+M$ universe, the $-M$ universe with the transformed boundary conditions, and the $-M$ universe with the untransformed ones (the control, which must not pair), for both fields, $m=1$ and $3$, $N=8$ and $112$, five couplings, and $T=0$ and $T=0.1\lvert m\rvert$, computed by two independent solvers and compared by a checker; then the two Stage-5 documents and the Stage-5 gate. The planned matrix has 60 configurations (two fields; four pairs $(\lvert m\rvert,N)$ with five couplings at $T=0$; the two pairs with $N=112$ with five couplings at $T=0.1\lvert m\rvert$), that is 180 runs of single universes.

**What is committed** (2026-09-30).

- The exact theory: `wolfram-dirac16complex00-report.json` (46 of 46 checks), `python-dirac16complex00-report.json` (49 of 49), `wolfram-pairing-report.json` (141 of 141) and `python-pairing-report.json` (172 of 172), all in `artifacts/dirac16complex/pair-creation/`.
- The Rust subcommand `pairs` (`studies/dirac16complex_kohn_sham/src/pairs.rs`) with outputs under `artifacts/dirac16complex/pair-creation/rust/pairs/`: 18 of the 60 configurations, all for dirac16complex: $m=1$, $N=8$ (five couplings, $T=0$); $m=1$, $N=112$ (five couplings at $T=0$ and at $T=0.1$); $m=3$, $N=8$ ($\lambda=0$ and $\pm\hat\lambda_1$). There is no run for dirac16complex00 and none for $m=3$, $N=112$.
- In every committed run the $-M$ universe with the transformed boundary conditions reproduces the $+M$ universe: the largest difference of an eigenvalue is $6.6\times10^{-9}$ (run `d16c_m1_L3_N8_lamm2_T0`), the largest difference of an energy $1.5\times10^{-8}$, and the scalar totals are opposite (key `pairingDeviation_plusM_vs_minusM` of each `pairing.json`). Every $+M$ run at $T=0$ is bit for bit the committed Stage-4 run with the same parameters (key `stage4Reproduction`).
- The controls ran only at $\lambda=0$ (four runs), and they differ as the exact theory predicts. For $m=1$, $N=8$ the control's Kohn–Sham gap is 0.100851 against 0.430734 for the pair. This value is the sub-gap bound state predicted by the exact theory (`pairing-theory.json`, key `T3.untransformedBCControl`; check `PAIR_T3ks_controlSubGapBoundState`): $\varepsilon=\sqrt{M^2-\kappa^2}$ with $\tanh(\kappa L)=\kappa/M$, which for $M=1$, $L=3$ gives $\kappa=0.994902$ and $\varepsilon=0.100851$ (the analytic value listed in `rust/pairs/free-section.json`). For $m=3$, $N=8$ the control gap is 0.000740 against 0.895833, and for $m=1$, $N=112$ the control's ground energy is 56.26550 against 61.09072. The interacting controls were not run: their first self-consistent update would violate the energy-window premise of the solver, because the untransformed tip bag puts the zero modes at the tip, where the proper-density factor is $e^{6HL}$ (the entry `minusM_control` under the key `universes` of each `pairing.json` records this).
- The pair totals (key `pairTotals`): for `d16c_m1_L3_N112_lam0_T0` the mirror pair (the $+M$ universe and the ordinary $-M$ universe) has $E=122.181447=2\times61.090723$ and charge 224, and the Krein-image pair has $E=-7.3\times10^{-11}$, zero to solver precision, and charge 0, as Theorem T3 predicts.
- The reference (`scripts/ks_reference_pairs.py`; `artifacts/dirac16complex/pair-creation/reference/reference-pairs-summary.json`, whose flag `complete` is false): of the 180 runs, 49 are recorded, all for $\lvert m\rvert=3$, $N=112$, and 17 of them converged; 131 are pending, among them every run with $\lvert m\rvert=1$ and every run with $N=8$, for both fields; 6 failed (five controls and one $-M$ run of dirac16complex00; five of them because their energy window exceeded the solver's cap of $20\lvert m\rvert$, one with the recorded error "tail: window never exhausted"); 26 did not converge, 24 of them interacting runs at $T=0.1\lvert m\rvert$ that were not attempted, and two runs of dirac16complex at $+\hat\lambda_2$.
- Not committed: a report of the pairs checker, the two Stage-5 documents and the Stage-5 gate. Their names are listed below.

```
scripts/check_dirac16complex_pairs.py          the pairs checker (no committed report)
provenance/DIRAC16COMPLEX00_FIELD_THEORY       planned document (not written)
provenance/DIRAC16COMPLEX_PAIR_CREATION        planned document (not written)
scripts/verify_stage5_pair_creation            planned gate (not written)
```

**Why it is hard.** The window premise stops the interacting controls. The couplings of the $m=3$ configurations are large ($\hat\lambda_1=42863$ for $N=8$ and $852.6$ for $N=112$, from the Stage-4 reference couplings listed in `reference-pairs-summary.json`), because the rule of Section 13.10 scales them to a fixed pseudo-potential. The commuting field has the opposite exchange sign, $M_{\mathrm{eff}}=m+\tfrac{17}{16}\lambda S_p$ and $v_x=+\tfrac1{16}\lambda n_p$ (Chapter 14), so attraction and repulsion exchange roles, and its Kohn–Sham model is a formal functional with the Pauli filling imposed by prescription (`pairing-theory.json`, key `notProved`). The staggered grid of the reference solver treats the two components of a block differently, so there the pairing holds only up to the discretisation error and must be judged after extrapolation (`pairing-theory.json`, key `T3.numericsPrescription`). And the reference runs take hours.

**A first step.** (1) Check one pair by hand: in `rust/pairs/free-section.json` compare the $k=0$ levels of the $+M$ and $-M$ universes with each other and with the exact values of Section 13.6 ($0$ and $\pm\sqrt{1+(n\pi/3)^2}$, for example $\pm1.447972$, in the parity sector with the zero mode; $\pm1.292293$ in the other), and find the control's sub-gap level. (2) Run the pairs checker on what exists, writing its report into the git-ignored folder `build/` (first command below), and read which comparisons ran and which were recorded as not run. (3) Run one pending reference configuration, again into `build/` (second command; the option `--list` prints all 180 labels). (4) Compute the missing dirac16complex00 configurations with the Rust `pairs` subcommand, whose parameters are described in the section "Stage 5" of the crate's `README.md`.

```
python scripts/check_dirac16complex_pairs.py --report build/pairs-check.json
python scripts/ks_reference_pairs.py --output build/refpairs \
    --runs d16c_m1_L3_N8_lam0_T0/plusM,d16c_m1_L3_N8_lam0_T0/minusM
```

(In PowerShell the second command is written on one line, without the backslash.)

**Where to start.** Sections 4 and 5 of the Stage-5 specification, its document outline, and these files:

```
handoff/specs/STAGE5_SPEC.md
handoff/specs/STAGE5_DOC_OUTLINE.md
artifacts/dirac16complex/pair-creation/            the exact reports and theory files
artifacts/dirac16complex/pair-creation/rust/pairs/ the Rust pair runs
artifacts/dirac16complex/pair-creation/reference/  the reference pair runs
studies/dirac16complex_kohn_sham/src/pairs.rs      the Rust subcommand pairs
scripts/ks_reference_pairs.py                      the reference driver
scripts/check_dirac16complex_pairs.py              the checker
```

### 18.9 Problem 7: a creation amplitude for pairs of universes

**The question.** The notebook states as a hypothesis that at the time $x_4=0$ a pair of universes with the masses $\pm M$ is created (cell 6), asks whether such universes are created in pairs (cell 7), and records the task "TODO: prove Universe(s) of masses ±M are created in pairs!" (cell 17; all three are quoted in Section 0.2). The project proves exact pairing theorems (Chapter 15), and Chapter 16 states exactly what they establish and what they do not; the creation itself remains a HYPOTHESIS. The open problem is to find a dynamical theory in which the creation of such a pair is a process with a computable amplitude, probability or rate, to compute it, and so to decide whether pairs are created.

**What is known.**

- PROVED (Theorem T1 of Chapter 15; checks `ALG_gamma8Map` of Stage 1 and `PAIR_totals_fieldLevelChiralPair`): a universe $\Psi_+$ with $(m,\lambda)$ and its chirality image $\gamma^8\Psi_+$ with $(-m,-\lambda)$, in the same gravitational field, have zero total energy–momentum tensor, zero total current and even zero total Lagrangian density, at every point and every $x_4$, in every gravitational field (`pairing-theory.json`, key `pairTotals.fieldLevel`). Creating such a pair from the field-free state therefore violates no conservation law and no constraint of the field equations, and at the level of the classical action it costs nothing.
- PROVED (Theorem T2; `PAIR_totals_fieldLevelMirrorPair`): the mirror pair, related by a Pin(4,4) reflection combined with $\gamma^8$ and with the same $\lambda$, has the same energy–momentum in both members, so its totals double instead of cancelling. In the Z2 construction every Kohn–Sham state of Stage 4 continues across the brane to a universe of mass $-M$ with the same $\lambda$ (`pairing-theory.json`, key `T3.stage4Z2Pair`; checks `PAIR_T2z2_*`).
- PROVED at the level of a Fock space (checks `PAIR_T1krein_*`): it matters which field is called "the $-M$ universe". The image field $\gamma^8\Psi$ on the same Fock space carries the Krein metric $-B$, the energy $-\lvert\varepsilon\rvert$ and the charge $-1$ per quantum, and the pair cancels; an independently quantized $-M$ field with its own positive structure has the energy $+\lvert\varepsilon\rvert$ and the charge $+1$ per quantum, and the totals add (matter–antimatter document, §7.3). Which of the two readings describes a physical pair is not decided anywhere: OPEN.
- COMPUTED (EXP-4b, Section 11.13): the creation of **quanta** in particle–antiparticle pairs by a changing background, computed with the Bogoliubov method, which L. Parker introduced for expanding universes (Phys. Rev. 183, 1057 (1969)); for example $na^3=4.412\times10^{-3}H_{\mathrm{inf}}^3$ for $m=H_{\mathrm{inf}}$ with the sudden end of inflation. It is the only creation process computed in the repository, and it creates quanta inside one universe, not universes.
- Stage 1 said it in one sentence: the pairing of the masses $\pm m$ is "a structural property of the equations, not a claim that universes of masses $\pm M$ are created in pairs" (Stage-1 document, §1.3, item 6).

**Why it is hard.**

- *The metric has no dynamics here.* The primordial field is prescribed, and what determines $a_4$ is open (Section 18.5). Without a dynamical geometry there is no process "creation of a universe".
- *A universe is not a quantum in a fixed background.* Creating one needs a quantum theory of the geometry itself: a wave function of the universe (the notebook's file name speaks of one) or a sum over geometries. The known proposals, the canonical equation of B. S. DeWitt (Phys. Rev. 160, 1113 (1967)), the creation "from nothing" of A. Vilenkin (Phys. Lett. B 117, 25 (1982)) and the no-boundary wave function of J. B. Hartle and S. W. Hawking (Phys. Rev. D 28, 2960 (1983)), are debated in four dimensions, and none has been formulated for this 8-dimensional theory.
- *A classical pair cannot appear from nothing.* Chapter 16 shows from the uniqueness of the solutions of the field equations in the good sector that a classical field which vanishes at one time vanishes at all times. A creation process must therefore be quantum, or start at a singular moment, which the notebook's field does not have (Chapter 16).
- *The matter side inherits Problems 1 and 2*: no interacting quantum theory, a Krein space, and the extra-time instability. In addition, if a $-M$ member with negative energies interacted with the $+M$ member, pairs of zero total energy could be produced without limit; Chapter 16 describes this stability question.
- *The cancelling pair has special parameters*: it needs $\lambda\to-\lambda$ (or $\lambda=0$) and, as a quantum field, the Krein metric $-B$ for its $-M$ member.
- *"At $x_4=0$" is not well defined yet.* The notebook's field singles out no moment ($a_4$ is an arbitrary function, and the static member does not depend on $x_4$ at all), and in signature (4,4) a rotation by $\pi$ in the plane of two time-like directions, which belongs to the identity component of the symmetry group, reverses $x_4$ and the charge (matter–antimatter document, §5.7): "before" and "after" refer to a chosen slicing.

**Worked example: a reduced model of the primordial family** (derived here). A standard first step of quantum cosmology is to keep only a few variables of the metric and to quantize them. The family of Section 9.5 has one variable, $a_4$. Add a **lapse** $N(x_4)>0$ through $g_{44}=-N^2$, so that $d\tau=N\,dx_4$ is proper time along $x_4$.

*The reduced action.* In the coordinates $(\zeta,\tau)$ the metric has the form of Lemma 9.1 with $f_p=H\zeta+\sigma_pa_4$, so the computation of Section 9.8 applies with the $t$-derivative replaced by the $\tau$-derivative: $R=6(da_4/d\tau)^2-42H^2=6\dot a_4^2/N^2-42H^2$, where $\dot a_4=da_4/dx_4$. No second derivative of $a_4$ appears, because the 7-volume is constant ($\Theta_4=0$ and $\sum_p\sigma_p=0$ in Section 9.8), so no boundary term is needed. With $\sqrt{\lvert g\rvert}=N\,e^{6H\zeta}$, the Einstein–Hilbert action $\tfrac1{2\kappa}\int\sqrt{\lvert g\rvert}\,R\,d^8x$ of Section 9.9, taken over a region of the slice whose proper 7-volume is $V=\int e^{6H\zeta}\,d\zeta\,d^6x$ (the same for every $a_4$ and every $x_4$, Section 9.4), becomes $\int L\,dx_4$ with

$$
L=\frac V{2\kappa}\Bigl(\frac{6\dot a_4^2}N-42H^2N\Bigr)-NV\rho .
$$

The last term is a homogeneous source with a constant energy density $\rho$, such as the condensate of Proposition 9.4 ($\rho=mS+U$). It is chosen so that its derivative with respect to $N$ at $N=1$ is $-VT_{44}=-V\rho$, which is what the definition $T_{\mu\nu}=-(2/\sqrt{\lvert g\rvert})\,\delta I_{\mathrm{matter}}/\delta g^{\mu\nu}$ of Section 9.9 requires (with $g^{44}=-1/N^2$).

*The equations.* The momentum of $a_4$ is $p=\partial L/\partial\dot a_4=6V\dot a_4/(\kappa N)$, and the energy function $p\dot a_4-L$ of Section 5.2 is

$$
\mathcal H=N\Bigl[\frac{\kappa p^2}{12V}+\frac{21H^2V}\kappa+V\rho\Bigr]
$$

(insert $\dot a_4=\kappa pN/(6V)$: $p\dot a_4=\kappa p^2N/(6V)$ and $L=\kappa p^2N/(12V)-21H^2VN/\kappa-NV\rho$). The variable $N$ appears in $L$ without a time derivative, so its Euler–Lagrange equation is $\partial L/\partial N=0$. At $N=1$ this reads $-\tfrac V\kappa(3\dot a_4^2+21H^2)-V\rho=0$, that is

$$
\rho=-\frac{3\dot a_4^2+21H^2}\kappa=-\frac{3H^2\bigl(7+a_4'^2\bigr)}\kappa \qquad(\dot a_4=Ha_4'),
$$

exactly the requirement $\rho_{\mathrm{req}}$ of Section 9.10. The Euler–Lagrange equation of $a_4$ is $\frac{d}{dx_4}\bigl(6V\dot a_4/\kappa\bigr)=0$, so $a_4$ is linear, as found in Section 18.5 from Proposition 9.2. The reduced model agrees with Chapter 9 on both counts. (The other Einstein equations, those of the directions $\zeta$ and of the transverse trace, are not contained in it; they give condition (3) of Proposition 9.4.)

*Quantization.* On wave functions $\psi(a_4)$ the operator $p=-i\,d/da_4$ satisfies the rule $[a_4,p]=i$ of Section 8.2: $a_4(-i\psi')+i(a_4\psi)'=i\psi$. The constraint $\mathcal H=0$ becomes the one-variable **Wheeler–DeWitt equation**

$$
-\frac\kappa{12V}\,\psi''+V\Bigl(\frac{21H^2}\kappa+\rho\Bigr)\psi=0,\qquad\text{that is}\qquad \psi''=\frac{12V^2}\kappa\Bigl(\frac{21H^2}\kappa+\rho\Bigr)\psi .
$$

If $\rho>-21H^2/\kappa$, in particular in vacuum, for every source of positive energy, and for a chiral pair, whose total energy–momentum vanishes, the right-hand side is a positive multiple of $\psi$ and the solutions are real exponentials $e^{\pm\ell a_4}$ with $\ell=V\sqrt{12(21H^2/\kappa+\rho)/\kappa}$: no oscillating, "classically allowed" solution exists, which is the quantum counterpart of the fact that no $a_4$ solves Einstein's equations with such a source. If $\rho<-21H^2/\kappa$ the solutions are $e^{\pm i\ell'a_4}$ with $\ell'=V\sqrt{12(-\rho-21H^2/\kappa)/\kappa}$, and the momentum $p=\pm\ell'$ belongs to the classical solution $a_4=ct$ with $3H^2c^2=-\kappa\rho-21H^2$; the notebook's $a_4=t$ belongs to $\rho=-24H^2/\kappa$ (Exercise 18.12).

**What the reduced model says, and what it does not.** In 8-dimensional Einstein gravity a chiral pair, whose total energy–momentum is zero, is invisible to the constraint: adding it changes nothing, and the geometry it lives in must be a vacuum solution, which the notebook's field is not. By Section 18.5 (derived there, not yet checked by machine) the static member is a vacuum solution of Einstein–Gauss–Bonnet gravity with tuned couplings, so there, as far as the bulk field equations are concerned, a chiral pair has a consistent home. The reduced model leaves out the Einstein equations of the other directions, the Lovelock terms, the brane, the matter modes and their instability, and the Krein structure; it has no boundary condition for $\psi$ (the no-boundary proposal and the tunnelling proposal are two choices from the literature); and it contains no process in which the number of universes changes. A creation amplitude needs a framework in which universes themselves can appear, and none is formulated in this repository.

**A first step.** (a) Redo the reduction (Exercise 18.12) and verify it exactly by machine: the variation with respect to $N$ must give $G^4{}_4$ of Section 9.8, and that with respect to $a_4$ the combination $G^1{}_1-G^5{}_5=2H^2a_4''$. (b) Add the Gauss–Bonnet term; its reduced form needs $E_{(2)}$ for a time-dependent $a_4$, the first step of Problem 3. (c) Formulate the matter side of a pair: the exact Fock model of `wolfram/Dirac16ComplexPairing.wl` contains both readings, the image field with $-B$ and the independent quantization. (d) Compare with the one creation process that is computed, the Bogoliubov creation of quanta in EXP-4b.

**Where to start.** Chapters 15 and 16; the matter–antimatter document, §7; the four papers cited above; and these files (the keys `T1`, `T1krein`, `T2`, `T3`, `pairTotals`, `notProved` and `notebookHypothesis` of the first one):

```
artifacts/dirac16complex/pair-creation/pairing-theory.json
wolfram/Dirac16ComplexPairing.wl                 the exact pairing theory, Fock model
studies/dirac16complex_cosmology/src/exp4.rs     EXP-4: creation of quanta
artifacts/dirac16complex/numerics/exp4/          its outputs
wolfram/Dirac16ComplexPrimordial.wl              the metric family and its curvature
```

### 18.10 Problem 8: baryogenesis in this framework

**The question.** The observed universe contains matter and almost no antimatter; the excess is measured by the baryon-to-photon ratio $\eta\approx6\times10^{-10}$ (matter–antimatter document, §2.2, from the Planck 2018 results and big-bang nucleosynthesis). The author asks that this theory solve the matter–antimatter mysteries. Chapter 17 shows that the theory as built does not: its charge is exactly conserved (Theorem M1), it has exact symmetries that reverse the charge without reversing $x_4$ (Theorem M2: charge conjugation $\Psi\to\Psi^\ast$ for dirac16complex00, a CP for dirac16complex), nothing computes a departure from equilibrium, and it contains no baryons of the Standard Model. The open problem is whether an extension of the framework could generate an asymmetry from a symmetric state, and what it would predict.

**Why it is hard.** Each of Sakharov's three conditions fails or is not addressed in the theory as built (the scorecard M6 of Chapter 17). In addition: identifying the charge of dirac16complex with baryon number (hypothesis H3 of Chapter 17) would need couplings to Standard-Model fields that the theory does not contain; the pair scenario M5 puts the asymmetry in as an initial condition and is not a mechanism; the quantum reading of the pair is unsettled (Section 18.9); the sign of the charge refers to a chosen slicing in (4,4) (matter–antimatter document, §5.7); and every quantum computation meets Problems 1 and 2.

**What is known.**

- PROVED (Chapter 17): M1, M2, and the classification M3 of the charge-violating terms allowed by the symmetry. For the anticommuting field no Majorana-type mass term exists; the derivative term $\Psi^TC\gamma^8\gamma^\mu D_\mu\Psi$ and quartic terms such as $Q_4$ and $Q_2$ survive. For the commuting field the two chiral mass terms $\Psi^TCP_\pm\Psi$ and the derivative term $\Psi^TC\gamma^\mu D_\mu\Psi$ (the form of the notebook's Lg[]) survive (checks `MA_M3_*` of both matter–antimatter reports).
- Derived in the matter–antimatter document (§10, item 2), not machine-checked: the phase of the coefficient of a single charge-2 term can be removed by redefining the field, so only relative phases between several such terms can be physical.
- OPEN: whether a given combination of charge-violating terms breaks all 64 charge-reversing symmetries of each field (matter–antimatter document, §10); whether the CP of dirac16complex is implemented on the positive Fock space of the good sector (§5.6); charge-violating terms of higher order than the quartic examples are not classified (§6.3).
- HYPOTHESIS: the conditional scenario M5 (Chapter 17), which predicts no value of $\eta$.

**Worked example 1: the first two Sakharov conditions for one complex variable** (derived here). Take a complex variable $z(t)$ with

$$
L=\dot z^\ast\dot z-\omega^2z^\ast z-\epsilon\bigl(z^2+z^{\ast2}\bigr),\qquad \epsilon\ \text{real}.
$$

Without the last term $L$ does not change under $z\to e^{i\alpha}z$, and Noether's theorem (Section 5.7, computed as in its Example 1) gives the conserved charge $Q=i(z^\ast\dot z-z\dot z^\ast)$, up to an overall sign, which is a convention; for $z=e^{-i\omega t}$ it is $Q=2\omega>0$. The last term has charge 2: it is multiplied by $e^{2i\alpha}$. The Euler–Lagrange equation of $z^\ast$ is $\ddot z=-\omega^2z-2\epsilon z^\ast$, and therefore

$$
\frac{dQ}{dt}=i\bigl(z^\ast\ddot z-z\ddot z^\ast\bigr)=i\bigl(-2\epsilon z^{\ast2}+2\epsilon z^2\bigr)=-4\epsilon\,\mathrm{Im}(z^2).
$$

The charge now changes: **the first condition** is met. But $L$ is unchanged by $z\to z^\ast$, which maps every solution $z(t)$ to a solution $z^\ast(t)$ with the charge $-Q(t)$. Starting from any collection of initial conditions that contains, with each one, its complex conjugate, the average charge stays zero at all times: this map is the "C" of the toy, and as long as it is a symmetry **the second condition** fails. A complex coefficient does not help by itself: the term $-(\epsilon z^2+\epsilon^\ast z^{\ast2})$ with $\epsilon=\lvert\epsilon\rvert e^{i\varphi}$ becomes $-\lvert\epsilon\rvert(w^2+w^{\ast2})$ for $w=e^{i\varphi/2}z$, and $w\to w^\ast$, that is $z\to e^{-i\varphi}z^\ast$, is again a charge-reversing symmetry. Two charge-violating terms whose phases cannot be removed together are needed (Exercise 18.14). The toy contains nothing that could meet **the third condition**: it has no out-of-equilibrium history.

**Worked example 2: the same computation for the commuting field** (derived here). Add to the Lagrangian of dirac16complex00 a charge-2 mass term of M3, $-\sqrt{\lvert g\rvert}\,(gX+g^\ast X^\ast)$ with $X=\Psi^TM\Psi$ and $M=CP_+$ or $CP_-$, which are real and symmetric because $C$ and $\gamma^8$ are real, symmetric and commute (Section 8.8, Chapter 17). The Euler–Lagrange expression of the old Lagrangian with respect to $\Psi^\ast$ is $\sqrt{\lvert g\rvert}\,CE$ with $E=\gamma^\mu D_\mu\Psi-(m+U')\Psi$, as in Chapter 17 (`dirac16complex00-theory.json`, key `fieldEquations`). Since $X^\ast=\Psi^\dagger M\Psi^\ast$ and $M$ is symmetric, the derivative of the new term with respect to $\Psi^\ast$ is $-2g^\ast\sqrt{\lvert g\rvert}\,M\Psi^\ast$, and the field equation becomes $CE=2g^\ast M\Psi^\ast$, that is $E=2g^\ast CM\Psi^\ast$ (because $C^2=1$). For commuting components the conjugate expression satisfies $\bar E=-E^\dagger C$ (use $(\gamma^a)^TC=-C\gamma^a$ and $(S^{ab})^TC=-CS^{ab}$, Sections 5.12 and 8.8), so $\bar E=-2g\,\Psi^TM$. The identity $\partial_\mu\bigl(\sqrt{\lvert g\rvert}\,j^\mu\bigr)=\sqrt{\lvert g\rvert}\,(\bar E\Psi+\bar\Psi E)$ of Theorem M1 holds for every configuration, so

$$
\partial_\mu\bigl(\sqrt{\lvert g\rvert}\,j^\mu\bigr)=\sqrt{\lvert g\rvert}\,\bigl(-2gX+2g^\ast X^\ast\bigr)=-4i\sqrt{\lvert g\rvert}\,\mathrm{Im}(gX),
$$

and with the real current $J^\mu=-ij^\mu$ of Section 8.12, when no charge flows out through the boundary of the slice,

$$
\frac{dQ}{dx_4}=-4\int\sqrt{\lvert g\rvert}\,\mathrm{Im}\bigl(g\,\Psi^TM\Psi\bigr)\,d^7x ,
$$

the field version of the toy. With one term the phase of $g$ can be removed and the charge conjugation $\Psi\to\Psi^\ast$, combined with a constant phase, remains a symmetry, exactly as in the toy.

**A first step.** (a) The toy and its two-term version (Exercises 18.13 and 18.14). (b) Worked example 2 numerically: the homogeneous state $\Psi=u(x_4)$ of dirac16complex00 is an exact solution for every potential (`dirac16complex00-theory.json`, key `primordial.stage2Homogeneous`); add the term $gX+g^\ast X^\ast$, integrate the 16 complex equations in $x_4$ (with the fourth-order Runge–Kutta method of Section 10.11, or the CVODE driver of Stage 3), and test the formula for $dQ/dx_4$ along the solution, as the checkers of Section 10.11 test conservation laws. (c) Take both chiral mass terms $g_+X_++g_-X_-$ with a relative phase and test, with the transformation rule of Theorem M2 (Chapter 17), all 64 charge-reversing symmetries of the commuting field: a finite exact computation. (d) Only then add a departure from equilibrium, for example a time-dependent background as in EXP-4b, and compute the charge produced from a symmetric initial ensemble. (e) Whether Theorem T1 still pairs solutions after such a term is added must be derived again: since $\gamma^8$ is diagonal (hence symmetric) and commutes with $C$ and with $P_\pm$, the term $X=\Psi^TM\Psi$ becomes $\Psi^T\gamma^8M\gamma^8\Psi=X$ under $\Psi\to\gamma^8\Psi$, so the map now needs $g\to-g$ in addition to $m\to-m$ and $\lambda\to-\lambda$ (derived here; check it).

**Where to start.** Chapter 17 and the matter–antimatter document (§6 for M3, §10 for what would have to be added); A. D. Sakharov, JETP Lett. 5, 24 (1967); the review of L. Canetti, M. Drewes and M. Shaposhnikov, New J. Phys. 14, 095012 (2012); as the known published example of a pair-of-universes idea, L. Boyle, K. Finn and N. Turok, Phys. Rev. Lett. 121, 251301 (2018), on which nothing in this repository depends; and these files, of which the first three contain the transformation rule of M2 and the classification of all 1024 maps per field:

```
wolfram/Dirac16ComplexMatterAntimatter.wl
scripts/verify_dirac16complex_matter_antimatter.wls
scripts/check_dirac16complex_matter_antimatter.py
wolfram/Dirac16Complex00.wl       dirac16complex00, including the homogeneous states
provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md
```

### 18.11 Smaller open items

The remaining open items of the book and of the project documents are smaller, or are parts of the problems above. Each has a first step.

| Item | Where it arises | A first step |
| --- | --- | --- |
| The $q$ term of the notebook is attributed to the rule of cell 1058 by a reconstruction (HYPOTHESIS) | Section 9.14; Stage-2 document, §11.3 | rerun the stored chain of cells 1058 to 1137 in an older Mathematica kernel, like the session that produced the stored outputs |
| Stability of the classical solutions under small perturbations is not studied | Stage-1 document, §1.3, item 3 | linearize the field equation around the homogeneous condensate of Proposition 9.4 and find the frequencies of the perturbations with the mode methods of Section 8.9 |
| Stability and quantum (Krein-space) status of the negative-energy source of Proposition 9.4 | Stage-2 document, §20, item 2 | the same linearization, and the expectation-value rule of Section 8.12 applied to the condensate |
| Sources that depend on the transverse coordinates, and plane waves with $\mathrm{Im}\,K=-3H$, $\mathrm{Re}\,K\ne0$ | Stage-2 document, §20, item 2 | extend Section 9.12; the off-diagonal components of $T_{\mu\nu}$ must vanish as well |
| A spin–statistics theorem for signature (4,4) | Section 8.15 | compare the commuting and the anticommuting quantization of the good sector; the unbounded classical energy of dirac16complex00 (Section 18.3) is the starting point |
| Is the CP of dirac16complex implemented on the positive Fock space of the good sector? | matter–antimatter document, §5.6 | test with the fixture whether its matrix preserves the good sector and is compatible with $J=B$ (Section 8.11 does the same for rotations) |
| Charge-violating terms of higher order than the quartic examples | matter–antimatter document, §6.3 | classify with the null-space method of M3 |
| Is the Kohn–Sham state reached by continuation in $\lambda$ the lowest self-consistent state when several exist? | Sections 13.10 and 13.11 | a search from many starting densities for $N=1016$ at $-\hat\lambda_2$ |
| The continuum limit of the 3-torus (6.6 percent change of $E/N$ at $\Delta k=0.125\,m$) | Section 13.15; erratum E4.11 | closed-shell runs at smaller $\Delta k$ and the same density |
| Correlation beyond the exchange-only functional | Section 13.8 | part of Problem 1 (Section 18.3) |
| The meaning of the Kohn–Sham model of dirac16complex00, with the Pauli filling imposed by prescription | Chapter 14; `pairing-theory.json`, key `notProved` | a statistical mechanics of the classical commuting field with Gaussian ensembles (the Wick sign of Section 18.3) |
| Dark matter: abundance, darkness, stabilised extra dimensions, structure formation, the hidden-space momentum $k_0$ | Section 11.13 | turn the EXP-4b yields into a relic density for physical values of $m$ and $H_{\mathrm{inf}}$ |
| Dark energy: other potentials, inhomogeneous states, a mechanism that stabilises the extra dimensions | Section 11.14 | repeat EXP-3 with a different $U(S)$ |
| The Fermi-degeneracy pressure of the condensate | Section 11.13; Stage-3 document, §4.6 | compute it with the uniform-gas formulas of Section 13.8 |
| Kohn–Sham states in a time-dependent primordial field ($a_4'\ne0$) | Chapter 13 uses only the static member | a time-dependent mean field in the good sector of the notebook's $a_4=t$ background |

### 18.12 What we proved and what we assumed

**Derived here**, with complete arguments in this chapter but without a check by any program of the repository: the power counting $[\Psi]=(D-1)/2$ and $[\lambda]=2-D$; the kinematic possibility that the contact interaction scatters quanta of the good sector into modes with extra-time momentum; the two-mode Krein toy, its threshold $\lvert g\rvert=\lvert\omega_0-\omega_1\rvert/2$ and its agreement with the extra-time dispersion relation at rest; the frozen-coefficient classification of the modes that keep oscillating for three histories of $a_4$, and the failure of compact extra times to remove the growing modes; the coupling of the $2\times2$ blocks in pairs by an extra-time momentum; the Lovelock tensors of all orders for the static member, the required source they imply, a positive required energy density for $\alpha_2>1/(20H^2)$, and the vacuum solution of Einstein–Gauss–Bonnet gravity with $\alpha_2=1/(40H^2)$ and $\alpha_0=21H^2$; the linearity of $a_4$ forced by a homogeneous source in Einstein gravity, with its slope; the uniform and isotropic source that the fixed static metric needs in every Einstein–Lovelock theory; the condition $5\rho+\sum_{\mu\ne4}p_{(\mu)}=0$ for every source of an ultrastatic metric in Einstein gravity and its Kohn–Sham form $6\sum_nw_n\varepsilon_nn_n=mS_p$; the pressure difference produced by different warps of 3-space and the extra times; the reduced model of the primordial family, its constraint, its agreement with Chapter 9 and its Wheeler–DeWitt equation; the charge-violation toy, the removability of a single phase and the condition for two terms; the formula $dQ/dx_4=-4\int\sqrt{\lvert g\rvert}\,\mathrm{Im}(g\Psi^TM\Psi)\,d^7x$ for the commuting field with a charge-2 mass term; and the extended pairing map with $g\to-g$. Each of these is a first step for a student, and the first task is to verify it exactly, by machine, in two independent programs.

**Computed for this chapter from committed files by a short calculation** (Exercise 18.10 shows one of them): the ranges of $5\rho+p_y+3p_3+3p_t$ on the committed Kohn–Sham profiles; the differences between the Rust and the reference eigenvalues of Section 18.7; the Krein-image diagnostics of Section 18.6; the counts and largest deviations of the Stage-5 numerics in Section 18.8. The files are named where the numbers are used.

**Quoted from earlier chapters and from the committed reports**, with the status given there: every statement listed under "What is known" in Sections 18.3 to 18.10.

**Quoted from the literature and not derived**: the power-counting argument for non-renormalisability; the argument against several time directions; the well-posedness of the ultrahyperbolic problem under a nonlocal constraint; Lovelock's theorem; the junction conditions of Gauss–Bonnet gravity; the proposals of DeWitt, Vilenkin and Hartle and Hawking; the Bogoliubov method of particle creation; Sakharov's conditions; the observed value of $\eta$.

**Assumed**: the frozen-coefficient estimate of Section 18.4; the matter term $-NV\rho$ with a constant $\rho$ in the reduced model of Section 18.9; the quantization rule $p=-i\,d/da_4$ for a variable of the metric.

**Not claimed**: that any problem of this chapter is solved; that universes are created in pairs, by the big bang or otherwise; that this theory explains the matter–antimatter asymmetry; that the Einstein–Gauss–Bonnet couplings of Section 18.5 describe an acceptable theory; that any Kohn–Sham state is the source of the primordial field.

### 18.13 Exercises

**Exercise 18.1.** (a) Compute $[\Psi]$ and $[\lambda]$ for $D=2,4,5,8$. For which $D$ is the contact coupling dimensionless? (b) Two quanta of mass $m=1$ at rest turn into two quanta with the wave numbers $(k_1,k_5)=(p,q)$ and $(-p,-q)$. Show that energy conservation requires $p^2=q^2$, and compute the energy of each final quantum for $p=q=2$.

**Exercise 18.2.** For the Krein toy of Section 18.3 with $\omega_0=3$ and $\omega_1=1$, compute the eigenvalues for $g=\tfrac12$, $1$ and $2$. For $g=1$ show that $h-2$ squares to zero and describe the growth of the solutions. Compare with two modes of the same Krein sign and $g=2$.

**Exercise 18.3.** Show that $h=\begin{pmatrix}m&g\\-g^\ast&-m\end{pmatrix}$ has the eigenvalues $\pm\sqrt{m^2-\lvert g\rvert^2}$. With $\lvert g\rvert=\lvert k_5\rvert$, compare with $E^2$ of Section 8.9 at zero 3-momentum, and give the growth rate for $m=1$, $k_5=2$. Which sample of the table of Section 8.9 has the same $E^2$?

**Exercise 18.4.** With the two rules of Section 13.4 show that $\gamma^0\gamma^5$ anticommutes with $J=\gamma^0\gamma^1\gamma^4$ and with $K_2=\gamma^5\gamma^6$ and commutes with $K_1=\gamma^2\gamma^3$. Compute $(\gamma^0\gamma^5)^2$ and compare it with $A_1^2$ and $A_4^2$ of Section 13.4.

**Exercise 18.5.** Let $x_5$ be a circle of radius $R$, $m=1$ and $\mathbf k=0$. (a) For $R=2$ compute $E^2$ for $n=0,\pm1,\pm2,\pm3$ and say how each mode behaves; give the growth rate for $n=3$. (b) Which modes grow for $R=\tfrac12$?

**Exercise 18.6.** (a) Compute $6!/(6-2k)!$ and $7!/(7-2k)!$ for $k=0,1,2,3$ and the entries of $E_{(2)}$ and $E_{(3)}$ of the static member. (b) Check that the row $k=1$ is the Einstein tensor of Section 9.15. (c) What does the counting of Section 18.5 give for $k=4$, and why does this agree with Section 4.9?

**Exercise 18.7.** (a) Derive the vacuum couplings $\alpha_2=1/(40H^2)$ and $\alpha_0=21H^2$ for $\alpha_1=1$, $\alpha_3=0$. (b) With $\alpha_1=1$, $\alpha_2=1/(10H^2)$ and $\alpha_0=\alpha_3=0$ compute $\rho_{\mathrm{req}}$, $p_{\mathrm{req}}$ and $w$. (c) Show that Einstein gravity with a cosmological constant alone ($\alpha_2=\alpha_3=0$) has no static vacuum of this form.

**Exercise 18.8.** For the dirac16complex00 source of Section 18.6 ($m=-30$, $\lambda=\tfrac{125}6$, $S=\tfrac65$, $H=\kappa=1$) check $mS=-36$, $\lambda S^2=30$, $M_{\mathrm{eff}}$, $\rho$, $p$ and $w$, the kinetic and potential energies $\mathrm{KE}_L=\tfrac12S(m+U')$ and $\mathrm{PE}_L=\rho-\mathrm{KE}_L$ of a homogeneous state (Chapter 7; `dirac16complex00-theory.json`, key `energySplits`), and the condition $5\rho+7p=0$.

**Exercise 18.9.** In $D$ dimensions, use the trace-reversed Einstein equations $R_{\mu\nu}=\kappa\bigl(T_{\mu\nu}-g_{\mu\nu}T/(D-2)\bigr)$ of Section 9.9 to show that every source of an ultrastatic metric satisfies $(D-3)\rho+\sum p=0$, the sum running over the $D-1$ directions other than the time. For $D=4$ and a source made of dust of density $\rho_m$ and a cosmological constant $\Lambda$, show that $\Lambda=\kappa\rho_m/2$.

**Exercise 18.10.** (a) Repeat worked example 3 of Section 18.6 for $N=1016$ at $\lambda=0$, where `rust/emt/emt-summary.csv` gives $\langle\rho\rangle=0.425999$ and $\langle S_p\rangle=-0.0872325$. (b) Write the Python lines that compute the smallest and the largest value of $5\rho+p_y+3p_3+3p_t$ on the committed profile of this run, and check the identity of worked example 2 on it.

**Exercise 18.11.** From the table of Section 18.7 compute, for both levels, the differences Rust (301) minus reference, Rust (601) minus reference and Rust (301) minus Rust (601). Test the rule "deviation at most the tolerance plus the measured grid uncertainty $\lvert\varepsilon(601)-\varepsilon(301)\rvert$", with the tolerance $1.054\times10^{-6}$ for the level of parity $+$ and at least $1.0\times10^{-6}$ for the level of parity $-$. Why does this arithmetic alone not justify changing the checker?

**Exercise 18.12.** (a) Derive the momentum $p$ and the function $\mathcal H$ of the reduced model of Section 18.9. (b) For $\rho=-33H^2/\kappa$ find the slope $c$ of the classical solution and compare with Exercise 9.5. (c) For a chiral pair ($\rho=0$) write the general solution of the Wheeler–DeWitt equation.

**Exercise 18.13.** For the toy of Section 18.10 with $\omega=1$ and $\epsilon=\tfrac1{10}$ write $z=x+iy$. (a) Show that $Q=2(y\dot x-x\dot y)$ and that $x$ and $y$ oscillate with the frequencies $\omega_1=\sqrt{\omega^2+2\epsilon}$ and $\omega_2=\sqrt{\omega^2-2\epsilon}$. (b) Show that real initial data, for example $z(0)=1$, $\dot z(0)=\tfrac3{10}$, give $Q=0$ at all times. (c) For $z(0)=1$, $\dot z(0)=-i$ compute $Q(t)$ and check $Q(0)=2$ and $dQ/dt=-4\epsilon\,\mathrm{Im}(z^2)$ at $t=0$.

**Exercise 18.14.** Add to the toy of Section 18.10 the terms $-(\epsilon_1z^2+\epsilon_1^\ast z^{\ast2})-(\epsilon_2z^4+\epsilon_2^\ast z^{\ast4})$ with $\epsilon_k=\lvert\epsilon_k\rvert e^{i\varphi_k}$. Show that a map $z\to e^{i\beta}z^\ast$ is a symmetry for some $\beta$ exactly when $2\varphi_1-\varphi_2$ is a multiple of $\pi$, and that the combination $2\varphi_1-\varphi_2$ does not change under $z\to e^{i\alpha}z$. What would still be missing for an asymmetry?

### 18.14 Answers to the exercises

**Answer 18.1.** (a) $[\Psi]=(D-1)/2$ and $[\lambda]=2-D$: for $D=2$, $\tfrac12$ and $0$; for $D=4$, $\tfrac32$ and $-2$; for $D=5$, $2$ and $-3$; for $D=8$, $\tfrac72$ and $-6$. The coupling is dimensionless only for $D=2$. (b) Each final quantum has $E=\sqrt{1+p^2-q^2}$, and $2E=2$ requires $p^2=q^2$. For $p=q=2$: $E=\sqrt{1+4-4}=1$ each, total 2, the energy of the two quanta at rest.

**Answer 18.2.** The threshold is $\lvert\omega_0-\omega_1\rvert/2=1$. $g=\tfrac12$: $2\pm\sqrt{1-\tfrac14}=2.866025$ and $1.133975$. $g=1$: the double eigenvalue 2. $g=2$: $2\pm i\sqrt3$, growth rate $\sqrt3=1.732051$. For $g=1$, $h=\begin{pmatrix}3&1\\-1&1\end{pmatrix}$ and $h-2=\begin{pmatrix}1&1\\-1&-1\end{pmatrix}$, whose square is $\begin{pmatrix}1-1&1-1\\-1+1&-1+1\end{pmatrix}=0$. So $e^{-iht}=e^{-2it}\bigl(1-i(h-2)t\bigr)$ (the series of the exponential of the nilpotent part stops after two terms): the solutions grow linearly, as in the case $E^2=0$ of Section 8.9. With the same Krein sign, $h=\begin{pmatrix}3&2\\2&1\end{pmatrix}$ has the real eigenvalues $2\pm\sqrt5=4.236068$ and $-0.236068$.

**Answer 18.3.** $\det(h-x)=(m-x)(-m-x)+\lvert g\rvert^2=x^2-m^2+\lvert g\rvert^2$, so $x=\pm\sqrt{m^2-\lvert g\rvert^2}$. With $\lvert g\rvert=\lvert k_5\rvert$ this is $\pm E$ with $E^2=m^2-k_5^2$, the relation of Section 8.9 at zero 3-momentum. For $m=1$, $k_5=2$: $E^2=-3$ and the growth rate is $\sqrt3=1.732051$; the table of Section 8.9 has the same $E^2=-3$ for the sample $m=1$, $k_7=2$.

**Answer 18.4.** $\gamma^0$ is a factor of $J$ ($k=3$) and commutes with it; $\gamma^5$ is not a factor and anticommutes with it; so $\gamma^0\gamma^5J=-J\gamma^0\gamma^5$. $\gamma^0$ is not a factor of $K_2$ ($k=2$) and commutes with it; $\gamma^5$ is a factor and anticommutes; so $\gamma^0\gamma^5$ anticommutes with $K_2$. Neither $\gamma^0$ nor $\gamma^5$ is a factor of $K_1$, so both commute with it. $(\gamma^0\gamma^5)^2=(-1)^1(\gamma^0)^2(\gamma^5)^2=-(1)(-1)=+1$, the same as $A_4^2=(\gamma^0\gamma^4)^2=+1$ and opposite to $A_1^2=-1$: an extra-time momentum enters the reduced equation like the frequency term, not like a 3-momentum.

**Answer 18.5.** (a) $E^2=1-n^2/4$: $n=0$ gives 1 and $n=\pm1$ gives $\tfrac34$ (oscillation); $n=\pm2$ gives 0 (linear growth); $n=\pm3$ gives $-\tfrac54$, exponential growth with $\kappa=\sqrt5/2=1.118034$, and every larger $\lvert n\rvert$ grows faster. (b) $E^2=1-4n^2<0$ for every $n\ne0$: all modes except $n=0$ grow. A smaller circle makes things worse.

**Answer 18.6.** (a) $6!/(6-2k)!=1,30,360,720$ and $7!/(7-2k)!=1,42,840,5040$. With $K=-H^2$: $E_{(2)}=-\tfrac{H^4}2\cdot360=-180H^4$ on the seven directions and $-\tfrac{H^4}2\cdot840=-420H^4$ on $x_4$; $E_{(3)}=-\tfrac{-H^6}2\cdot720=360H^6$ and $-\tfrac{-H^6}2\cdot5040=2520H^6$. (b) $k=1$: $-\tfrac{-H^2}2\cdot30=15H^2$ and $-\tfrac{-H^2}2\cdot42=21H^2$, the entries of $G^\mu{}_\nu=\mathrm{diag}(15,15,15,15,21,15,15,15)H^2$. (c) For $k=4$ one needs lists of 8 different elements of $\Sigma$, which has only 7 elements: there are none, and $E_{(4)}=0$. Section 4.9 found the same: the generalized delta of $E_{(4)}$ has $2k+1=9>8$ upper indices and vanishes.

**Answer 18.7.** (a) With $\alpha_3=0$ the first condition of Section 18.5 is $\alpha_1-40\alpha_2H^2=0$, so $\alpha_2=1/(40H^2)$; the second gives $\alpha_0=2(15H^2-180H^4/(40H^2))=2(15-4.5)H^2=21H^2$. Check on $x_4$: $-\tfrac{21}2+21-\tfrac{420}{40}=0$. (b) $\kappa\rho_{\mathrm{req}}=-21H^2+420H^4/(10H^2)=21H^2$ and $\kappa p_{\mathrm{req}}=15H^2-180H^4/(10H^2)=-3H^2$, so $\rho_{\mathrm{req}}=21H^2/\kappa>0$, $p_{\mathrm{req}}=-3H^2/\kappa$ and $w=-\tfrac17$. (c) The first condition becomes $\alpha_1=0$, which contradicts $\alpha_1=1$: no value of $\Lambda$ makes both components vanish, because $E_{(1)}$ has different entries on $x_4$ (21) and on the seven directions (15), while $E_{(0)}$ has equal ones.

**Answer 18.8.** $mS=-30\cdot\tfrac65=-36$; $\lambda S^2=\tfrac{125}6\cdot\tfrac{36}{25}=30$; $M_{\mathrm{eff}}=-30+\tfrac{125}6\cdot\tfrac65=-30+25=-5$; $\rho=mS+\tfrac\lambda2S^2=-36+15=-21$; $p=\tfrac\lambda2S^2=15$; $w=-\tfrac57$. $\mathrm{KE}_L=\tfrac12\cdot\tfrac65\cdot(-30+25)=-3$ and $\mathrm{PE}_L=-21+3=-18$, the values recorded in `dirac16complex00-theory.json`. $5\rho+7p=-105+105=0$.

**Answer 18.9.** For an ultrastatic metric $R_{00}=0$ (the argument of Section 18.6 works in every dimension). With $T_{00}=\rho$, $g_{00}=-1$ and $T=-\rho+\sum p$: $R_{00}=\kappa\bigl(\rho+(-\rho+\sum p)/(D-2)\bigr)=\kappa\bigl((D-3)\rho+\sum p\bigr)/(D-2)=0$. For $D=4$: $\rho+3p=0$ with $p$ the (equal) pressure. A cosmological constant, moved to the right-hand side of $G^\mu{}_\nu+\Lambda\delta^\mu{}_\nu=\kappa T^\mu{}_\nu$, acts like a source with $\rho_\Lambda=\Lambda/\kappa$ and $p_\Lambda=-\Lambda/\kappa$. With dust: $\rho_m+\Lambda/\kappa-3\Lambda/\kappa=0$, so $\Lambda=\kappa\rho_m/2$.

**Answer 18.10.** (a) The image has $\langle\rho\rangle=-0.425999$, so $\kappa=21/0.425999=49.30>0$ from the energy density; the mass condition $(-1)(-0.0872325)=-36/\kappa$ gives $\kappa=-412.7<0$ (the $+M$ state gave $+412.7$, Section 13.14). The two conditions contradict each other, and the coupling condition cannot hold at $\lambda=0$. (b) In the repository root:

```
import csv
path = "artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N1016_lam0_T0/profiles.csv"
rows = list(csv.DictReader(open(path)))
def comb(r):
    return (5 * float(r["rho"]) + float(r["p_y"])
            + 3 * float(r["p_3"]) + 3 * float(r["p_t"]))
def ks(r):
    return 6 * (float(r["rho"]) + float(r["L_s"])) - 1.0 * float(r["S_p"])
values = [comb(r) for r in rows]
print(min(values), max(values))
print(max(abs(comb(r) - ks(r)) / max(1.0, abs(comb(r))) for r in rows))
```

The first line prints about 1.0852 and 28609.2, the second a number of the order of $10^{-16}$: the identity holds to rounding. (Here $m=1$, and $\sum_nw_n\varepsilon_nn_n=\rho+L_s$ by Section 13.14.)

**Answer 18.11.** Parity $+$: $-1.05374908333+1.05374688831=-2.195\times10^{-6}$; $-1.05374707094+1.05374688831=-1.83\times10^{-7}$; $-1.05374908333+1.05374707094=-2.012\times10^{-6}$. Parity $-$: $-1.976\times10^{-6}$, $-1.64\times10^{-7}$ and $-1.812\times10^{-6}$. The extended rule passes: $2.195\times10^{-6}\le1.054\times10^{-6}+2.012\times10^{-6}=3.066\times10^{-6}$ and $1.976\times10^{-6}\le1.0\times10^{-6}+1.812\times10^{-6}=2.812\times10^{-6}$. But a rule chosen after seeing that it passes proves nothing. The change is justified only if an independent measurement, such as a finer-grid Rust run converging toward the reference, shows that the difference between 301 and 601 points is a real grid error of the Rust value; the rule must then be applied to every run with such a partner and recorded as an erratum.

**Answer 18.12.** (a) $p=\partial L/\partial\dot a_4=\tfrac V{2\kappa}\cdot\tfrac{12\dot a_4}N=\tfrac{6V\dot a_4}{\kappa N}$, and $p\dot a_4-L=N\bigl[\kappa p^2/(12V)+21H^2V/\kappa+V\rho\bigr]$ as in Section 18.9. (b) $3H^2c^2=-\kappa\rho-21H^2=33H^2-21H^2=12H^2$, so $c=\pm2$; Exercise 9.5 found $\rho_{\mathrm{req}}=-33H^2/\kappa$ for $a_4=2t$. (c) $\psi''=\ell^2\psi$ with $\ell=V\sqrt{12\cdot21}\,H/\kappa=6\sqrt7\,VH/\kappa=15.8745\,VH/\kappa$, so $\psi=A\,e^{\ell a_4}+B\,e^{-\ell a_4}$: no oscillating solution.

**Answer 18.13.** (a) $z^\ast\dot z=(x-iy)(\dot x+i\dot y)=x\dot x+y\dot y+i(x\dot y-y\dot x)$ and $z\dot z^\ast$ is its complex conjugate, so $Q=i\cdot2i(x\dot y-y\dot x)=2(y\dot x-x\dot y)$. Since $z^2+z^{\ast2}=2(x^2-y^2)$, the Lagrangian is $\dot x^2+\dot y^2-\omega^2(x^2+y^2)-2\epsilon(x^2-y^2)$, with the equations $\ddot x=-(\omega^2+2\epsilon)x$ and $\ddot y=-(\omega^2-2\epsilon)y$. (b) Real data have $y(0)=\dot y(0)=0$, so $y=0$ at all times and $Q=0$. (c) $x=\cos\omega_1t$ and $y=-\sin(\omega_2t)/\omega_2$ with $\omega_1=\sqrt{1.2}=1.095445$ and $\omega_2=\sqrt{0.8}=0.894427$, and $Q(t)=2\bigl[(\omega_1/\omega_2)\sin\omega_1t\,\sin\omega_2t+\cos\omega_1t\,\cos\omega_2t\bigr]$. At $t=0$, $Q=2$. Since $z^2=x^2-y^2+2ixy$, $\mathrm{Im}(z^2)=2xy=0$ at $t=0$, so $dQ/dt=0$ there; differentiating $Q(t)$ gives the same, because each term of $dQ/dt$ contains $\sin\omega_1t$ or $\sin\omega_2t$. For later times $Q$ oscillates, while the conjugate solution carries $-Q(t)$.

**Answer 18.14.** The kinetic and mass terms do not change under $z\to e^{i\beta}z^\ast$. The term $\epsilon_1z^2$ becomes $\epsilon_1e^{2i\beta}z^{\ast2}$, which must equal the old coefficient of $z^{\ast2}$, $\epsilon_1^\ast$: $e^{2i\beta}=e^{-2i\varphi_1}$. The term $\epsilon_2z^4$ requires $e^{4i\beta}=e^{-2i\varphi_2}$. The first gives $e^{4i\beta}=e^{-4i\varphi_1}$, so both hold exactly when $e^{-4i\varphi_1}=e^{-2i\varphi_2}$, that is when $2\varphi_1-\varphi_2$ is a multiple of $\pi$ (and then $\beta=-\varphi_1$ works). Under $z\to e^{i\alpha}z$ the coefficients become $\epsilon_1e^{2i\alpha}$ and $\epsilon_2e^{4i\alpha}$, and $2(\varphi_1+2\alpha)-(\varphi_2+4\alpha)=2\varphi_1-\varphi_2$: the combination is physical. When it is not a multiple of $\pi$, no map of this form reverses the charge; still missing are a check of all other charge-reversing maps, a departure from equilibrium, and a link to baryons.
