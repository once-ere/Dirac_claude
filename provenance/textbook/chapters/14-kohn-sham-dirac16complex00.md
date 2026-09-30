## 14. The Kohn–Sham approximation for dirac16complex00

### 14.1 What this chapter does, and the status of its results

Chapter 13 built a Kohn–Sham (density-functional) approximation for dirac16complex, the field whose sixteen components anticommute, and computed its ground and first excited states in the static primordial field. This chapter does the same for the second field of the book, **dirac16complex00**, whose sixteen components are ordinary commuting complex numbers (Chapter 6). The request asked for such an approximation, with ground and first excited states, for each of the two fields (section 4 of `handoff/specs/STAGE5_SPEC.md`).

The main result fits in one sentence, and the chapter proves it step by step: **within the model defined in Section 14.2, the statistics of the components enters the mean-field energy only through the sign of the exchange term.** For dirac16complex the exchange energy density of the contact interaction is $e_x=-\tfrac\lambda{32}(n^2+S^2)$ (Section 13.8); for dirac16complex00 it is

$$
e_x^{00}=+\frac\lambda{32}\bigl(n^2+S^2\bigr),
$$

and consequently the Kohn–Sham effective mass and vector potential of dirac16complex00 are $M_{\text{eff}}^{00}=m+\tfrac{17}{16}\lambda S_p$ and $v^{00}=+\tfrac\lambda{16}n_p$, in place of $m+\tfrac{15}{16}\lambda S_p$ and $-\tfrac\lambda{16}n_p$.

The sentence contains a condition, “within the model”, and a large part of the chapter is about it. A classical field has no occupation numbers, no Pauli principle and, as Section 14.2 shows, no lowest energy. A Kohn–Sham model of such a field must therefore **state what is being averaged**, and the answer changes the result: Section 14.5 exhibits one density matrix for which three different averaging rules give three different interaction energies. Section 14.8 states plainly what the model is and what it is not.

**Sources.** The binding specification is section 4 of `handoff/specs/STAGE5_SPEC.md`. The exact results come from two Wolfram packages, each with a verifier, and from two independent sympy checkers. The four reports, all in the folder `artifacts/dirac16complex/pair-creation/` like every file named in this chapter without a folder, are:

- `wolfram-pairing-report.json`, 141 of 141 checks true, from the package `wolfram/Dirac16ComplexPairing.wl` and its verifier `scripts/verify_dirac16complex_pairing.wls`;
- `python-pairing-report.json`, 172 of 172 checks true, written by the independent checker `scripts/check_dirac16complex_pairing.py`;
- `wolfram-dirac16complex00-report.json`, 46 of 46 checks true, from the package `wolfram/Dirac16Complex00.wl` and its verifier `scripts/verify_dirac16complex00.wls`;
- `python-dirac16complex00-report.json`, 49 of 49 checks true, written by the independent checker `scripts/check_dirac16complex00.py`.

The statistics sign is the check family whose names begin with `PAIR_stat_` (Wolfram) and `S5_stat_` (Python); the field theory of dirac16complex00 is the family `C00_` (Wolfram) and `S5_` (the dirac16complex00 checker). The exact formulas are collected in `pairing-theory.json` (key `statistics`) and `dirac16complex00-theory.json` (keys `commutingFieldSpecifics` and `static`). The numbers of Sections 14.9 and 14.10 come from the independent reference solver `scripts/ks_reference_solver.py`, driven by `scripts/ks_reference_pairs.py`, whose outputs lie in `artifacts/dirac16complex/pair-creation/reference/` with the summary `reference-pairs-summary.json`. That summary records itself as incomplete (its key `complete` is `false`), and the committed Rust outputs of the Stage-5 subcommand `pairs` in `artifacts/dirac16complex/pair-creation/rust/pairs/` contain no dirac16complex00 run at all. The Stage-5 documents planned in section 6 of `handoff/specs/STAGE5_SPEC.md` were not written when this chapter was written, and the Stage-5 gate had not been run; the chapter therefore cites the reports and outputs directly.

**Status of the results (read this first).**

- PROVED (derived here, and verified by the named exact checks): the Gaussian moments of Section 14.3; the four-amplitude averages for waves and for fermions (Section 14.4); the statistics sign of the exchange term (Theorem 14.4); the Hartree–Fock energy of the contact interaction for both fields, the filled-shell ratio $E_x=\pm E_H/8$ and the uniform-gas exchange $e_x=\pm\tfrac\lambda{32}(n^2+S^2)$ (Section 14.6); the Kohn–Sham potentials and equations of dirac16complex00 (Section 14.7); and the first two facts of Section 14.8 that limit the meaning of the model (the indefinite covariance of the model and the Krein weighting of its energies).
- ASSUMED: the model itself (the prescriptions P1 to P4 of Section 14.2), together with everything that Chapter 13 assumes. The third point of Section 14.8, that the model is not a quantum theory, is a statement about how the model is defined (it is not obtained by quantizing the field); Pauli's spin–statistics theorem is quoted there, not proved, as the reason why no such quantization is attempted.
- COMPUTED: the Kohn–Sham ground and first excited states of dirac16complex00 in one configuration ($m=3H$, $L=3/H$, $N=112$, $\hat\lambda\in\{0,+\hat\lambda_1\}$, $T=0$) and, without interaction, at one temperature; by one solver only, with no independent cross-check (Sections 14.9 and 14.10).
- NOT COMPUTED: every other configuration of the planned run matrix, listed in Section 14.11.

**Units and conventions.** As in Chapter 13: $H=1$, coordinates $x_0,\dots,x_7$ with $x_4$ the time, $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$, the notebook's gammas $\gamma^a$ (Chapter 2), $C=\gamma^0\gamma^1\gamma^2\gamma^3$, $\bar\Psi=\Psi^\dagger C$, $S=\bar\Psi\Psi$, $B=-iC\gamma^4$, $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7$, and the Hermitian current $J^\mu=-i\bar\Psi\gamma^\mu\Psi$ with charge density $J^4=\Psi^\dagger B\Psi$ (Section 8.12). **The complex conjugate of a number $c$ is written $c^\ast$, never $\bar c$**, because the bar is reserved for the Dirac adjoint $\bar\Psi$. The numerical sections use $m=3$, so energies there are quoted in units of $H$ (not of $m$), with $m=3H$.

### 14.2 A classical field has no occupation numbers: what must be averaged

**The field and its Lagrangian.** At every point $x$ the field dirac16complex00 is a column $\Psi(x)=(\Psi_0(x),\dots,\Psi_{15}(x))^T$ of sixteen ordinary complex numbers that transform together as a Pin(4,4) spinor. Its Lagrangian is the same formula as for dirac16complex,

$$
\mathcal L=\sqrt{|g|}\,\Bigl[\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)-m\,\bar\Psi\Psi-\tfrac\lambda2(\bar\Psi\Psi)^2\Bigr],
$$

and so is its field equation $\gamma^\mu D_\mu\Psi=(m+\lambda S)\Psi$ (Chapters 6 and 7; checks `C00_EL_commutingCurved` and `C00_EL_identicalFormBothStatistics` of `wolfram-dirac16complex00-report.json`). For a given configuration of the field, $S(x)=\bar\Psi(x)\Psi(x)$ is a number at each point, and the interaction energy density is the number $\tfrac\lambda2S(x)^2$. Nothing is “exchanged”: exchange, in Chapter 12, was a property of many-particle states.

**What Chapter 13 used.** The Kohn–Sham model of dirac16complex rested on four facts of the quantized fermion field: (i) each one-particle level is either empty or occupied once (the Pauli principle, Section 8.3); (ii) with the filled Dirac sea and normal ordering the energy is not negative (Section 8.10); (iii) the expectation-value rule $\langle\Psi^\dagger M\Psi\rangle=u^\dagger BMu$ makes the number density of every one-particle state positive (Section 8.12); and (iv) Wick's theorem computes the average of $S^2$ in a determinant or a thermal ensemble (Section 12.5). None of the four is available for a classical commuting field. Three exact results of Stage 5 show what goes wrong (Chapter 7 derives the first two in detail).

**Fact 1: the charge density has no sign.** The phase symmetry $\Psi\to e^{i\alpha}\Psi$ gives the conserved charge density $J^4=\Psi^\dagger B\Psi$ for commuting components too (check `C00_current_conservationAndReality`). $B$ is Hermitian with $B^2=1$ and has the eigenvalues $+1$ and $-1$ eight times each (Section 2.12), so $J^4$ takes both signs. A worked example with the explicit matrix: the rows 6 and 15 of $B$ read $(Bu)_6=i\,u_{15}$ and $(Bu)_{15}=-i\,u_6$ (`dirac16complex00-theory.json`, key `commutingFieldSpecifics.B`). Write $e_n$ for the column with 1 in place $n$ (counting from 0) and take

$$
\Psi_+=i\,e_6+e_{15},\qquad \Psi_-=-i\,e_6+e_{15}.
$$

For $\Psi_+$: $(B\Psi_+)_6=i\cdot1=i=(\Psi_+)_6$ and $(B\Psi_+)_{15}=-i\cdot i=1=(\Psi_+)_{15}$, so $B\Psi_+=\Psi_+$ and $J^4=\Psi_+^\dagger\Psi_+=2$. For $\Psi_-$: $(B\Psi_-)_6=i=-(\Psi_-)_6$ and $(B\Psi_-)_{15}=-i(-i)=-1=-(\Psi_-)_{15}$, so $B\Psi_-=-\Psi_-$ and $J^4=-2$ (check `C00_charge_indefinite`, which records these two vectors). The argument of Section 8.8 applies unchanged to commuting spinors: every charge density built from a Spin(4,4)-invariant form is indefinite. So the probability density of Dirac's 1928 theory has no analogue here, and dirac16complex00 is not a wave function with a probability interpretation.

**Fact 2: the classical energy has no lower bound.** In flat space with $\lambda=0$, a plane wave $\Psi=u\,e^{-i\omega x_4+i\mathbf k\cdot\mathbf x}$ that solves the field equation has the energy density $\rho=T_{44}=\omega\,J^4$ with $J^4=u^\dagger Bu$ (check `C00_energy_unboundedBelow`). The report lists four exact solutions with $m=1$ and the wave numbers $(1,1,2,3,0,0,0)$ along $(x_0,x_1,x_2,x_3,x_5,x_6,x_7)$, so that $\omega^2=1+1+1+4+9=16$ and $\omega=\pm4$ (they are the entry `energyUnboundedBelow` under the key `commutingFieldSpecifics` of `dirac16complex00-theory.json`):

| $\omega$ | $J^4$ | $\rho$ |
| --- | --- | --- |
| $+4$ | $+224$ | $+896$ |
| $+4$ | $-224$ | $-896$ |
| $-4$ | $+32$ | $-128$ |
| $-4$ | $-32$ | $+128$ |

Multiplying a solution by a number $c$ gives a solution and multiplies $\rho$ by $|c|^2$, so the second solution can be made to carry as negative an energy as we like. The interaction does not help: with $m=1$ and $\lambda=-1$ the homogeneous states with $S=1$, $10$ and $100$ solve the nonlinear equation and have $\rho=mS+\tfrac\lambda2S^2=\tfrac12$, $10-50=-40$ and $100-5000=-4900$; for $\lambda=+1$ the report lists a family of self-consistent plane waves whose energy density decreases without bound as well. For the quantized Grassmann field the same indefinite matrix $B$ became the anticommutator, and the filled Dirac sea with normal ordering made the Hamiltonian non-negative in the good sector (Section 8.10). That mechanism needs the Pauli principle; a classical commuting field does not have it.

**Fact 3: no Pauli principle.** The amplitude of a mode of a classical field is any complex number. Nothing restricts the squared amplitude, the classical analogue of an occupation number, to 0 or 1.

**Consequence.** For dirac16complex00 the phrase “ground state” in the sense of Chapter 12 (the state of lowest energy, Section 12.2) has no meaning, because there is no lowest energy. A Kohn–Sham model of this field can therefore not be derived from a variational principle of the classical field. It must be **defined**, and the definition must say (a) over which collection of field configurations the densities $n$ and $S$ are averages, (b) which mean occupations the modes carry, and (c) which bilinear of the field is called the density.

**Why (a) matters: one mode, two answers.** Take one mode, $\Psi=c\,u$ with a fixed normalized spinor $u$ and a random complex amplitude $c$ whose squared modulus is $f$ on average. The scalar density is proportional to $|c|^2$, and the interaction energy to its square. (i) If every member of the collection has the same modulus, $|c|^2=f$, and only the phase of $c$ is random, then $\langle|c|^4\rangle=f^2=\langle|c|^2\rangle^2$. (ii) If $c$ is a Gaussian random number (Section 14.3), then $\langle|c|^4\rangle=2f^2$. Two collections with the same average density give average interaction energies that differ by a factor 2. The difference $\langle S^2\rangle-\langle S\rangle^2$ is exactly what the exchange term of a density functional must represent (Section 14.5), so a density functional must say which collection it describes.

**The Stage-5 model.** The Stage-5 specification (section 4 of `handoff/specs/STAGE5_SPEC.md`) answers (a) to (c) as follows, and `pairing-theory.json` (key `statistics.positivity.status`) records the resulting status: the model is “a DFT-motivated mean field of a random-phase (Gaussian) ensemble of classical modes with Fermi-Dirac occupations (Pauli filling imposed by prescription), not a quantum theory of commuting spinors”. In detail:

- **P1 (the ensemble).** The field is a sum of Kohn–Sham orbitals $u_n$ of Chapter 13 with independent random complex amplitudes $c_n$, and every average of products of amplitudes is computed with the rule of a circular Gaussian (Sections 14.3 and 14.4), with the mean squared amplitudes fixed by P2.
- **P2 (the occupations).** The mean squared amplitudes are the weights $w_n$ of Chapter 13: the Fermi–Dirac occupation $w_n=f_n$ on a particle level and $w_n=-(1-f_n)$ on a sea level, with normal ordering against the free Dirac sea (Section 13.7). For a commuting field this “Pauli filling” is not a consequence of anything; it is imposed, as the user specified (“fermion-gas thermodynamics”). Note what the sea weights mean for P1: a sea level that is not completely full has $w_n<0$, and no random complex number has a negative mean squared modulus. So already this bookkeeping of particles and sea makes the “ensemble” formal: P1 fixes a rule for computing averages, the rule of a circular Gaussian with the numbers $w_n$ in place of $f$, and not a probability distribution of fields. (At $T=0$ every sea level is full and has $w_n=0$; P3 adds a second reason, Section 14.8.)
- **P3 (the densities).** The density of a bilinear $\Psi^\dagger M\Psi$ is computed with the expectation-value rule of the quantized fermion field, $u^\dagger BMu$ for a mode $u$ (Section 8.12), so that the two fields differ **only** in the statistics.
- **P4 (the rest).** Exchange only, with no correlation term (Section 14.8), and everything else of Chapter 13: the static primordial field with the Z2 brane, the good sector, the eight $2\times2$ blocks, the boundary conditions, the torus, and the definition of the ground state by continuation in the coupling (erratum E4.8).

Section 14.8 examines what P3 costs.

### 14.3 Random complex amplitudes from zero

**Probability densities.** A random real number $x$ is described by a **probability density** $p(x)\ge0$ with $\int p(x)\,dx=1$: the probability that $x$ falls between $a$ and $b$ is $\int_a^bp(x)\,dx$, and the **average** (mean, expectation) of a function $g$ of $x$ is $\langle g\rangle=\int g(x)\,p(x)\,dx$. A random complex number $c=x+iy$ is a random point of the plane, described by a density $p(c)=p(x,y)$ with $\int\!\int p\,dx\,dy=1$ and $\langle g\rangle=\int\!\int g\,p\,dx\,dy$, which we write $\int g\,p\,d^2c$. Two random numbers $c_0,c_1$ are **independent** when their joint density is the product $p_0(c_0)\,p_1(c_1)$; then the double integral factorizes and $\langle g(c_0)h(c_1)\rangle=\langle g(c_0)\rangle\langle h(c_1)\rangle$.

**Polar coordinates in the plane.** Write $x=r\cos\varphi$ and $y=r\sin\varphi$, that is $c=r\,e^{i\varphi}$ (the polar form of Section 1.5), with $r\ge0$ and $0\le\varphi<2\pi$. The small region between the radii $r$ and $r+dr$ and the angles $\varphi$ and $\varphi+d\varphi$ is almost a rectangle with the sides $dr$ (along the radius) and $r\,d\varphi$ (along the circle of radius $r$), so its area is $r\,dr\,d\varphi$. Hence

$$
\int g\,d^2c=\int_0^\infty\!\!\int_0^{2\pi}g\bigl(re^{i\varphi}\bigr)\,r\,d\varphi\,dr .
$$

**The circular Gaussian.** For a number $f>0$ define

$$
p_f(c)=\frac1{\pi f}\,e^{-|c|^2/f}.
$$

It depends only on $|c|=r$, so all phases are equally likely: this is the precise meaning of a **random phase**. It is normalized: with the substitution $s=r^2/f$, $ds=2r\,dr/f$,

$$
\int p_f\,d^2c=\frac1{\pi f}\cdot2\pi\int_0^\infty e^{-r^2/f}\,r\,dr=\frac2f\cdot\frac f2\int_0^\infty e^{-s}\,ds=1 .
$$

(The density of the modulus alone, $(2r/f)\,e^{-r^2/f}$, is called the Rayleigh distribution.)

**A factorial integral.** For $k=0,1,2,\dots$ let $I_k=\int_0^\infty s^ke^{-s}\,ds$. Then $I_0=1$, and integrating by parts (Section 1.10) with $g'=e^{-s}$, $g=-e^{-s}$,

$$
I_k=\bigl[-s^ke^{-s}\bigr]_0^\infty+k\int_0^\infty s^{k-1}e^{-s}\,ds=k\,I_{k-1},
$$

because the boundary term vanishes at both ends ($e^{-s}$ decreases faster than any power grows, a fact of calculus used without proof). Hence $I_k=k(k-1)\cdots1=k!$.

**Proposition 14.1 (moments of one Gaussian amplitude).** For the circular Gaussian with $\langle|c|^2\rangle=f$ and integers $\alpha,\beta\ge0$,

$$
\bigl\langle(c^\ast)^\alpha c^\beta\bigr\rangle=\delta_{\alpha\beta}\,\alpha!\,f^\alpha .
$$

*Proof.* In polar form $(c^\ast)^\alpha c^\beta=r^{\alpha+\beta}e^{i(\beta-\alpha)\varphi}$. The angular integral is $\int_0^{2\pi}e^{ik\varphi}d\varphi=2\pi$ for $k=0$ and $\bigl[e^{ik\varphi}/(ik)\bigr]_0^{2\pi}=0$ for every integer $k\ne0$, so only $\alpha=\beta$ survives. Then, with $s=r^2/f$, so that $r^{2\alpha}=f^\alpha s^\alpha$ and $r\,dr=\tfrac f2ds$,

$$
\bigl\langle|c|^{2\alpha}\bigr\rangle=\frac{2\pi}{\pi f}\int_0^\infty r^{2\alpha}e^{-r^2/f}\,r\,dr=\frac2f\cdot f^\alpha\cdot\frac f2\,I_\alpha=\alpha!\,f^\alpha .\qquad\square
$$

In particular $\langle|c|^2\rangle=f$, confirming the name of the parameter, and $\langle|c|^4\rangle=2f^2$: the squared modulus fluctuates as much as its mean, $\langle|c|^4\rangle-\langle|c|^2\rangle^2=f^2$.

**Worked example.** For $f=\tfrac12$: $\langle|c|^2\rangle=\tfrac12$, $\langle|c|^4\rangle=2\cdot\tfrac14=\tfrac12$, $\langle|c|^6\rangle=6\cdot\tfrac18=\tfrac34$, and $\langle c\rangle=\langle c^2\rangle=\langle(c^\ast)^2c\rangle=0$. For comparison, the **fixed-modulus** collection $c=\sqrt f\,e^{i\varphi}$ with a random phase alone has $\langle(c^\ast)^\alpha c^\beta\rangle=\delta_{\alpha\beta}f^\alpha$ (the same angular integral, no radial integral): $\langle|c|^4\rangle=f^2=\tfrac14$.

**The quantum versions.** A **fermion mode** (Section 8.3) is empty or occupied once. If it is occupied with probability $f$, its occupation number $k\in\{0,1\}$ has $\langle k\rangle=f$ and $\langle k(k-1)\rangle=0$, because $k(k-1)=0$ for $k=0$ and $k=1$. In operator language $b^\dagger b^\dagger bb=0$ because $(b^\dagger)^2=0$. A **boson mode** is described by an operator with the commutator $[b,b^\dagger]=1$ instead of the anticommutator; its number operator $N=b^\dagger b$ has the eigenvalues $k=0,1,2,\dots$ (the quantum harmonic oscillator, a standard fact that we quote), and $b^\dagger b^\dagger bb=b^\dagger(bb^\dagger-1)b=N^2-N=N(N-1)$. In the Gibbs state of Section 12.14 the probability of $k$ quanta in a level of energy $\varepsilon$ is proportional to $e^{-k(\varepsilon-\mu)/T}$, that is $p_k=(1-x)\,x^k$ with $x=e^{-(\varepsilon-\mu)/T}<1$ (normalized by the geometric series $\sum_kx^k=1/(1-x)$). Differentiating the geometric series once and twice, $\sum_kkx^k=x/(1-x)^2$ and $\sum_kk(k-1)x^k=2x^2/(1-x)^3$, so

$$
\langle k\rangle=\frac x{1-x}=:f,\qquad \langle k(k-1)\rangle=(1-x)\,\frac{2x^2}{(1-x)^3}=2f^2 .
$$

(The first formula is the Bose–Einstein occupation $f=1/(e^{(\varepsilon-\mu)/T}-1)$.) The four cases side by side:

| one mode | mean number | mean number of ordered pairs |
| --- | --- | --- |
| fermion, occupation probability $f$ | $f$ | $0$ |
| boson, thermal | $f$ | $2f^2$ |
| classical Gaussian amplitude | $f$ | $2f^2$ |
| classical fixed modulus, random phase | $f$ | $f^2$ |

The last column is $\langle k(k-1)\rangle$ for the quantum modes and $\langle|c|^4\rangle$ for the classical ones. The thermal boson and the classical Gaussian agree: both follow from $\langle(c^\ast)^\alpha c^\alpha\rangle=\alpha!f^\alpha$ and its operator analogue. The Wolfram verifier computes these moments exactly, $\langle b^\dagger b\rangle=f$, $\langle b^\dagger b^\dagger bb\rangle=2f^2$, $\langle b^\dagger b^\dagger b^\dagger bbb\rangle=6f^3$, $\langle|c|^4\rangle=2f^2$, $\langle|c|^6\rangle=6f^3$ and $\langle(c^\ast)^2c\rangle=0$ (check `PAIR_stat_singleModeMoments`, `wolfram-pairing-report.json`).

### 14.4 Four amplitudes: Isserlis' rule for waves and Wick's rule for fermions

**Many modes.** Let $c_0,\dots,c_{M-1}$ be independent circular Gaussian amplitudes with $\langle|c_n|^2\rangle=f_n$. The exchange term of Section 14.5 needs the averages of products of two conjugated and two plain amplitudes.

**Proposition 14.2 (Isserlis' rule for four amplitudes).** For all mode labels $n,q,r,p$,

$$
\bigl\langle c_n^\ast\,c_q^\ast\,c_r\,c_p\bigr\rangle=f_nf_q\bigl(\delta_{np}\delta_{qr}+\delta_{nr}\delta_{qp}\bigr).
$$

*Proof.* By independence the average is the product, over the modes, of the averages of the factors that belong to each mode, and by Proposition 14.1 a mode contributes zero unless it appears as many times conjugated as unconjugated. Two cases remain. (i) $n=q$: the mode $n$ appears twice conjugated, so both plain factors must belong to it, $p=r=n$, and the average is $\langle|c_n|^4\rangle=2f_n^2$. (ii) $n\ne q$: the modes $n$ and $q$ appear once conjugated each, so $\{p,r\}=\{n,q\}$, and either $p=n,r=q$ or $p=q,r=n$; each gives $\langle|c_n|^2\rangle\langle|c_q|^2\rangle=f_nf_q$. The formula reproduces both cases: for $n=q=p=r$ the bracket is $1+1$, and otherwise exactly the matching Kronecker product is 1. $\square$

**Proposition 14.3 (Wick's rule for four fermion operators).** In a quasi-free fermion state with the occupation probabilities $f_n$ of orthonormal modes (a Slater determinant when every $f_n$ is 0 or 1, a non-interacting thermal ensemble otherwise; Section 12.5),

$$
\bigl\langle a_n^\dagger\,a_q^\dagger\,a_r\,a_p\bigr\rangle=f_nf_q\bigl(\delta_{np}\delta_{qr}-\delta_{nr}\delta_{qp}\bigr).
$$

*Proof.* Section 12.5 gives $\langle a_{p'}^\dagger a_{q'}^\dagger a_{s'}a_{r'}\rangle=\rho_{r'p'}\rho_{s'q'}-\rho_{s'p'}\rho_{r'q'}$ for any quasi-free state with the one-body density matrix $\rho_{ba}=\langle a_a^\dagger a_b\rangle$. Put $(p',q',s',r')=(n,q,r,p)$: the right side is $\rho_{pn}\rho_{rq}-\rho_{rn}\rho_{pq}$. In the basis of the modes $\rho$ is diagonal, $\rho_{pn}=f_n\delta_{pn}$, which gives the claim. $\square$

**Reading the two rules.** Both have two terms. The **direct** pairing joins $c_n^\ast$ with $c_p$ and $c_q^\ast$ with $c_r$; the **exchange** pairing joins $c_n^\ast$ with $c_r$ and $c_q^\ast$ with $c_p$. The direct term has the sign $+$ in both rules. The exchange term has the sign $+$ for Gaussian waves and $-$ for fermions: for fermions, reaching the exchange pairing requires one exchange of two anticommuting operators. A compact way to remember this: arrange the four two-point averages in the $2\times2$ matrix

$$
G=\begin{pmatrix}\langle c_n^\ast c_p\rangle&\langle c_n^\ast c_r\rangle\\ \langle c_q^\ast c_p\rangle&\langle c_q^\ast c_r\rangle\end{pmatrix}=\begin{pmatrix}g_{00}&g_{01}\\ g_{10}&g_{11}\end{pmatrix};
$$

the Gaussian average is its **permanent** $g_{00}g_{11}+g_{01}g_{10}$, and the fermion average is its **determinant** $g_{00}g_{11}-g_{01}g_{10}$. The general theorems, which we quote and do not use, say the same for products of any length: the average of $k$ conjugated and $k$ plain Gaussian amplitudes is the permanent of the $k\times k$ matrix of two-point averages (Isserlis, 1918), and the corresponding fermion average is its determinant (Wick, 1950).

**Worked examples.** With $n=q=p=r=0$ the Gaussian rule gives $2f_0^2$ and the fermion rule $0$ (the Pauli principle). With $n=p=0$ and $q=r=1$ both rules give $f_0f_1$ (direct pairing only). With $n=r=0$ and $q=p=1$ the Gaussian rule gives $+f_0f_1$ and the fermion rule $-f_0f_1$ (exchange pairing only).

### 14.5 The statistics sign of the exchange term

**The setting.** Let $\psi$ be a column of $d$ components (later $d=16$) built from $d$ orthonormal modes $u_0,\dots,u_{d-1}$, the columns of a unitary $d\times d$ matrix $U$:

$$
\psi=\sum_nc_n\,u_n=U\,c\quad(\text{waves}),\qquad \psi=\sum_na_n\,u_n=U\,a\quad(\text{fermions}).
$$

Define the **density matrix** $\rho=\sum_nf_n\,u_nu_n^\dagger=UFU^\dagger$ with $F=\mathrm{diag}(f_0,\dots,f_{d-1})$. Then the two-point average is

$$
\langle\psi_a^\ast\psi_b\rangle=\sum_{n,p}U_{an}^\ast U_{bp}\,\langle c_n^\ast c_p\rangle=\sum_nf_n\,U_{bn}U_{an}^\ast=\rho_{ba},
$$

using $\langle c_n^\ast c_p\rangle=f_n\delta_{np}$ (Proposition 14.1 and independence); for fermions the same computation with $\langle a_n^\dagger a_p\rangle=f_n\delta_{np}$ gives $\langle\psi_a^\dagger\psi_b\rangle=\rho_{ba}$. So both averages of a single bilinear are the same: $\langle\psi^\dagger X\psi\rangle=\sum_{a,b}X_{ab}\rho_{ba}=\mathrm{Tr}(X\rho)$ for every $d\times d$ matrix $X$.

**Theorem 14.4 (the statistics sign).** For all $d\times d$ matrices $X$ and $Y$,

$$
\bigl\langle(\psi^\dagger X\psi)(\psi^\dagger Y\psi)\bigr\rangle=\mathrm{Tr}(X\rho)\,\mathrm{Tr}(Y\rho)+\mathrm{sg}\,\mathrm{Tr}(X\rho\,Y\rho),
$$

with $\mathrm{sg}=+1$ for independent circular Gaussian amplitudes (a classical commuting field) and $\mathrm{sg}=-1$ for the normal-ordered product $:(\psi^\dagger X\psi)(\psi^\dagger Y\psi):$ of a fermion field in a quasi-free state. We call $\mathrm{sg}$ the **statistics sign**, with the name that the reports use (`pairing-theory.json`, key `conventions.statisticsSign`) and that Chapter 15 uses; Chapter 6 writes the same sign as $s$.

*Proof for waves.* Write $\tilde X=U^\dagger XU$ and $\tilde Y=U^\dagger YU$ (the matrices in the basis of the modes). Then $\psi^\dagger X\psi=c^\dagger U^\dagger XUc=\sum_{n,p}c_n^\ast\tilde X_{np}c_p$, and, because amplitudes commute,

$$
\bigl\langle(\psi^\dagger X\psi)(\psi^\dagger Y\psi)\bigr\rangle=\sum_{n,p,q,r}\tilde X_{np}\tilde Y_{qr}\,\bigl\langle c_n^\ast c_q^\ast c_rc_p\bigr\rangle .
$$

Insert Proposition 14.2. The direct term sets $p=n$, $r=q$ and gives $\sum_nf_n\tilde X_{nn}\sum_qf_q\tilde Y_{qq}=\mathrm{Tr}(F\tilde X)\,\mathrm{Tr}(F\tilde Y)$; the exchange term sets $r=n$, $p=q$ and gives $\sum_{n,q}f_n\tilde X_{nq}f_q\tilde Y_{qn}=\mathrm{Tr}(F\tilde XF\tilde Y)$. Return to the original basis with the cyclic property of the trace and $UFU^\dagger=\rho$: $\mathrm{Tr}(F\tilde X)=\mathrm{Tr}(FU^\dagger XU)=\mathrm{Tr}(UFU^\dagger X)=\mathrm{Tr}(X\rho)$, and $\mathrm{Tr}(F\tilde XF\tilde Y)=\mathrm{Tr}(UFU^\dagger X\,UFU^\dagger Y)=\mathrm{Tr}(\rho X\rho Y)=\mathrm{Tr}(X\rho Y\rho)$.

*Proof for fermions.* Now $\psi^\dagger X\psi=\sum_{n,p}a_n^\dagger\tilde X_{np}a_p$. Normal ordering moves every creation operator to the left of every annihilation operator, with the sign of the permutation, and drops the terms that the anticommutator would produce (Section 13.8): $:a_n^\dagger a_p\,a_q^\dagger a_r:=-a_n^\dagger a_q^\dagger a_pa_r=+a_n^\dagger a_q^\dagger a_ra_p$ (one exchange to move $a_q^\dagger$ past $a_p$, a second to exchange $a_p$ and $a_r$). Proposition 14.3 then gives the direct term with $+$ and the exchange term with $-$; the return to the original basis is the same. $\square$

**Remark 1: the full product.** Without normal ordering, $a_pa_q^\dagger=\delta_{pq}-a_q^\dagger a_p$ adds the term $\sum_{n,p,r}\tilde X_{np}\tilde Y_{pr}\langle a_n^\dagger a_r\rangle=\mathrm{Tr}(XY\rho)$, so the plain fermion product has the average $\mathrm{Tr}(X\rho)\mathrm{Tr}(Y\rho)-\mathrm{Tr}(X\rho Y\rho)+\mathrm{Tr}(XY\rho)$. A boson field ($b_pb_q^\dagger=\delta_{pq}+b_q^\dagger b_p$) gives the same with $+\mathrm{Tr}(X\rho Y\rho)$, and its normal-ordered average equals the classical Gaussian one. For classical amplitudes there is nothing to reorder and no $\mathrm{Tr}(XY\rho)$ term. The repository verifies all of this exactly, in exact rational arithmetic, and it is worth saying precisely what each check covers. (The prefix `PAIR_` marks checks of `wolfram-pairing-report.json`, the prefix `S5_` checks of the independent `python-pairing-report.json`.)

- **Fermions.** `PAIR_stat_fermionWickMinus` works on the complete 16-dimensional state space of four modes, in 12 quasi-free states (3 bases of modes times 4 sets of occupations, pure determinants and mixed states), with two fixed Hermitian $4\times4$ test matrices whose entries are complex numbers with rational real and imaginary parts; it checks both the normal-ordered and the full product. `S5_stat_fermionWickMinus` does the same on its own 16-dimensional space of four modes, with its own 12 states and test matrices.
- **Thermal bosons.** `PAIR_stat_bosonThermalWickPlus` checks the normal-ordered product for the same four occupation sets $\{1,1,0,0\}$, $\{1,0,1,1\}$, $\{\tfrac13,\tfrac25,0,1\}$ and $\{\tfrac12,\tfrac17,\tfrac34,\tfrac29\}$ of four modes in the same three bases; only its single-mode moments are computed symbolically in $f$, from the thermal series (the package also forms the full product, but this check does not test it). `S5_stat_bosonThermalWickPlus` checks the normal-ordered **and** the full product with symbolic occupations $f_0,f_1,f_2$ of three modes in one rational basis.
- **Classical Gaussian amplitudes.** The moments are exact integrals over the density $p_f$. `PAIR_stat_classicalGaussianWickPlus` uses the four occupation sets and three bases above, and also checks that every four-amplitude moment of the Gaussian equals the corresponding normal-ordered moment of the thermal boson; `S5_stat_classicalGaussianWickPlus` uses symbolic occupations of three modes, and confirms that no $\mathrm{Tr}(XY\rho)$ term appears.

**Remark 2: fixed moduli.** If the amplitudes have fixed moduli, $c_n=\sqrt{f_n}\,e^{i\varphi_n}$ with independent random phases, only case (i) of Proposition 14.2 changes ($f_n^2$ instead of $2f_n^2$), so

$$
\bigl\langle(\psi^\dagger X\psi)(\psi^\dagger Y\psi)\bigr\rangle_{\text{fixed moduli}}=\mathrm{Tr}(X\rho)\,\mathrm{Tr}(Y\rho)+\mathrm{Tr}(X\rho Y\rho)-\sum_nf_n^2\,\tilde X_{nn}\tilde Y_{nn}
$$

(check `PAIR_stat_fixedAmplitudePhasesDeviate`). The $+$ sign of the exchange term is therefore a property of **Gaussian** amplitudes, the amplitudes of thermal (chaotic) waves; it is not a property of every random-phase collection.

**Worked example: one density matrix, three answers.** Take $d=2$, the modes $u_0=(1,1)^T/\sqrt2$ and $u_1=(1,-1)^T/\sqrt2$, the occupations $f_0=1$, $f_1=\tfrac12$, and $X=Y=\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, the first Pauli matrix of Section 2.3. Then

$$
\rho=f_0u_0u_0^\dagger+f_1u_1u_1^\dagger=\frac12\begin{pmatrix}f_0+f_1&f_0-f_1\\ f_0-f_1&f_0+f_1\end{pmatrix}=\begin{pmatrix}\tfrac34&\tfrac14\\ \tfrac14&\tfrac34\end{pmatrix},\qquad
\sigma_x\rho=\begin{pmatrix}\tfrac14&\tfrac34\\ \tfrac34&\tfrac14\end{pmatrix},
$$

so $\mathrm{Tr}(\sigma_x\rho)=\tfrac12$ and $\mathrm{Tr}(\sigma_x\rho\,\sigma_x\rho)=\tfrac1{16}+\tfrac9{16}+\tfrac9{16}+\tfrac1{16}=\tfrac54$. Since $\sigma_xu_0=u_0$ and $\sigma_xu_1=-u_1$, the mode-basis matrix is $\tilde X=\mathrm{diag}(1,-1)$. The three averages of $(\psi^\dagger\sigma_x\psi)^2$ are:

| collection | formula | value |
| --- | --- | --- |
| Gaussian amplitudes ($\mathrm{sg}=+1$) | $\tfrac14+\tfrac54$ | $\tfrac32$ |
| fixed moduli, random phases | $\tfrac32-(f_0^2+f_1^2)$ | $\tfrac14$ |
| fermions, normal ordered ($\mathrm{sg}=-1$) | $\tfrac14-\tfrac54$ | $-1$ |

A direct check makes the three numbers transparent. In the mode basis $\psi^\dagger\sigma_x\psi=|c_0|^2-|c_1|^2$. With fixed moduli this is always $f_0-f_1=\tfrac12$, and its square is $\tfrac14$. With Gaussian amplitudes, $\langle(|c_0|^2-|c_1|^2)^2\rangle=2f_0^2-2f_0f_1+2f_1^2=2-1+\tfrac12=\tfrac32$. For fermions $\psi^\dagger\sigma_x\psi=\hat n_0-\hat n_1$, and $:\hat n_0^2:=a_0^\dagger a_0^\dagger a_0a_0=0$, so $\langle:(\hat n_0-\hat n_1)^2:\rangle=-2\langle\hat n_0\hat n_1\rangle=-2f_0f_1=-1$. All three collections have the same density matrix and the same average $\langle\psi^\dagger\sigma_x\psi\rangle=\tfrac12$. **The density matrix does not determine the average of a square; the statistics and the ensemble do.**

**Second example.** With the unrotated modes $u_n=e_n$ (so $\rho=\mathrm{diag}(f_0,f_1)$) and the same $X=Y=\sigma_x$, $\mathrm{Tr}(\sigma_x\rho)=0$ and $\mathrm{Tr}(\sigma_x\rho\sigma_x\rho)=2f_0f_1=1$: the Gaussian average is $+1$, the fermion average $-1$, and the fixed-modulus average $+1$ (the diagonal of $\sigma_x$ vanishes). With $X=Y=\mathrm{diag}(1,0)$ instead one gets $2f_0^2=2$ (Gaussian), $f_0^2=1$ (fixed moduli) and $0$ (fermions).

**What the sign means.** For fermions the exchange term removes the probability of finding two identical particles in the same state at the same place (Section 12.6: two fermions with the same internal label never meet at one point, and exchange removes exactly that part of the Hartree energy), so a repulsive contact interaction costs less than the Hartree estimate. Gaussian waves do the opposite: their intensity fluctuates, $\langle I^2\rangle=2\langle I\rangle^2$ for $I=|c|^2$, so high-intensity places are more likely than for a steady wave, and a repulsive contact interaction costs more. (In optics this “bunching” of thermal light is the effect observed by Hanbury Brown and Twiss in 1956; we quote it only as an illustration.)

### 14.6 The Hartree–Fock energy of the contact interaction for both fields

**The rule of the model.** For the quantized field dirac16complex, Section 13.8 showed that the expectation-value rule makes the two-point function $\langle\Psi_a^\dagger\Psi_b\rangle=(\rho B)_{ba}$, where $\rho=\sum_nw_nu_nu_n^\dagger$ is the Kohn–Sham density matrix of Section 13.7 (orbitals $u_n$ with weights $w_n$). Prescription P3 adopts the same two-point average for dirac16complex00: $\langle\Psi_a^\ast\Psi_b\rangle=K_{ba}$ with

$$
K=\rho B .
$$

In every state of the model each orbital lies in one of the eight blocks of Section 13.4, where $B$ is the number $\beta=js_2=\pm1$ (the **Krein sign** of the block). So $\rho$ commutes with $B$, and $K=\sum_nw_n\beta_n\,u_nu_n^\dagger$ is Hermitian. (The same holds for the uniform gas used below: its projectors $P_\pm(\mathbf p)$ are built from $\gamma^4$ and the products $\gamma^4\gamma^l$ with $l\le3$, which commute with $B$ by Section 8.11.) The model is therefore the Gaussian ensemble of Section 14.5 with the mean squared amplitude $w_n$ of each orbital replaced by $w_n\beta_n$, and it defines the average of a product of four amplitudes by the same pairing rule with these numbers. Both sides of Theorem 14.4 are polynomials in the occupations, and the proof used nothing but the pairing rule, so the theorem holds with $\rho$ replaced by $K$. (Section 14.8 returns to the fact that $w_n\beta_n$ can be negative, for two independent reasons: $\beta_n=-1$ in four of the eight blocks, and $w_n<0$ on a sea level that is not full.)

**The average of $S^2$.** Take $X=Y=C$, so that $\Psi^\dagger C\Psi=S$. The cyclic property of the trace gives

$$
\mathrm{Tr}(CK)=\mathrm{Tr}(C\rho B)=\mathrm{Tr}(BC\rho),\qquad \mathrm{Tr}(CKCK)=\mathrm{Tr}(C\rho B\,C\rho B)=\mathrm{Tr}(BC\rho\,BC\rho)
$$

(in the second identity the last factor $B$ is moved to the front). These two identities are check `PAIR_stat_expectationRuleTraces` (and `S5_stat_expectationRuleTraces`), verified on an exact random Hermitian $16\times16$ matrix. With Theorem 14.4:

**Theorem 14.5 (Hartree–Fock energy for both statistics).** In the model, and for the quantized dirac16complex (Section 13.8),

$$
e_{HF}=\frac\lambda2\bigl\langle S^2\bigr\rangle=\underbrace{\frac\lambda2\,S^2}_{e_H}+\underbrace{\mathrm{sg}\,\frac\lambda2\,\mathrm{Tr}(BC\rho\,BC\rho)}_{e_x},\qquad S=\mathrm{Tr}(BC\rho),
$$

with $\mathrm{sg}=-1$ for dirac16complex and $\mathrm{sg}=+1$ for dirac16complex00. The Hartree term $e_H$ is the same for both fields; only the exchange term $e_x$ changes sign (`pairing-theory.json`, key `statistics.hartreeFock.formula`). For $\mathrm{sg}=-1$ this is the formula of Section 13.8, where the normal-ordered quantum average $\langle{:}S^2{:}\rangle$ appears; the repository also checks it on an exact Krein–Fock space of four moving modes with both Krein signs (check `S5_stat_expectationRuleKreinFock`).

**A filled shell: the ratio $+1/8$.** Fill the eight positive-energy states at rest, $\rho=P_+=\tfrac12(1+BC)$ (Section 13.8, where $BC=-i\gamma^4$ and $BC\,P_+=P_+$). Then $S=\mathrm{Tr}(BCP_+)=8$ and $\mathrm{Tr}(BCP_+BCP_+)=\mathrm{Tr}(P_+)=8=S^2/8$, so

$$
\begin{aligned}
&E_x=\mathrm{sg}\,\frac\lambda2\cdot8=\mathrm{sg}\,\frac18\cdot\frac\lambda2\cdot64=\mathrm{sg}\,\frac{E_H}8:\\
&E_x=-\frac{E_H}8\ \ (\text{dirac16complex}),\qquad E_x=+\frac{E_H}8\ \ (\text{dirac16complex00}).
\end{aligned}
$$

The ratio $1/8$ holds at every momentum (check `PAIR_stat_filledShellExchangeRatio`, symbolic in $m$ and $\mathbf p$). **Worked example** at an exact point of the good sector recorded in `python-pairing-report.json` (entry `S5_stat.filledShellExchangeRatio`): $m=2$ and $\mathbf p=(0,1,2,4)$ along $(x_0,x_1,x_2,x_3)$, so $E_p^2=4+0+1+4+16=25$ and $E_p=5$. The report gives $\mathrm{Tr}(BCP_+)=\tfrac{16}5$, which is $8m/E_p=\tfrac{16}5$ (Section 13.8), and $\mathrm{Tr}(BCP_+BCP_+)=\tfrac{32}{25}$, which is $\bigl(\tfrac{16}5\bigr)^2/8=\tfrac{256}{200}=\tfrac{32}{25}$.

**The uniform gas.** Section 13.8 considered the uniform gas of particles and antiparticles with the density matrix $\rho=\int\frac{d^dp}{(2\pi)^d}\bigl[f_+P_+(\mathbf p)-f_-P_-(\mathbf p)\bigr]$, where $d$ is the number of **space dimensions** of the momenta $\mathbf p$ (as in Section 13.8; here $d$ is not the number of spinor components of Section 14.5), and with occupations that depend only on $|\mathbf p|$. It computed, for every $d$,

$$
\mathrm{Tr}(BC\rho\,BC\rho)=\frac{n^2+S^2}{16}.
$$

No step of that computation used the statistics: it is a statement about traces of projectors. (The Python checker notes that isotropy is more than needed: the term with $\mathbf p\cdot\mathbf q$ already vanishes when the occupations are unchanged under $\mathbf p\to-\mathbf p$; `S5_stat.uniformGasExchange` in `python-pairing-report.json`.) With Theorem 14.5:

$$
\begin{aligned}
&e_x=\mathrm{sg}\,\frac\lambda{32}\bigl(n^2+S^2\bigr):\\
&e_x=-\frac\lambda{32}\bigl(n^2+S^2\bigr)\ \ (\text{dirac16complex}),\qquad e_x^{00}=+\frac\lambda{32}\bigl(n^2+S^2\bigr)\ \ (\text{dirac16complex00}),
\end{aligned}
$$

exactly, at every temperature. This is the check `PAIR_stat_uniformGasExchange` of the Wolfram report and the check `S5_stat_uniformGasExchange` of the Python report. The Python checker also verifies the trace identity on an exact **finite** gas: $m=2$, eleven momenta with four components along $(x_0,x_1,x_2,x_3)$ (so $d=4$), on the four shells $E=2,3,4,5$ (the shell $E=2$ is $\mathbf p=0$; each other momentum comes with $-\mathbf p$), with the occupations $f_+=1,\tfrac34,\tfrac13,\tfrac1{10}$ and $f_-=\tfrac17,\tfrac1{11},0,\tfrac1{13}$ on the four shells. It finds $n=\tfrac{510808}{15015}\approx34.0198$, $S=\tfrac{2403416}{75075}\approx32.0135$ and $\mathrm{Tr}(BC\rho BC\rho)=\tfrac{768720549416}{5636255625}\approx136.3885=(n^2+S^2)/16$ exactly (check `S5_stat_uniformGasExactFinite`; Exercise 14.6 recomputes $n$ and $S$ by hand). For dirac16complex00 this gas has $e_x^{00}=\tfrac\lambda2\cdot136.3885=68.194\,\lambda$.

**Two limits.** A gas at rest has $S=n$ (every particle contributes $m/E_p=1$), so $e_x=\mathrm{sg}\,\tfrac\lambda{16}n^2=\mathrm{sg}\,e_H/8$, the filled-shell value (the limit is part of check `PAIR_stat_T0TotalDerivative`). A fast gas has $|S|\ll n$, and then the exchange term $\pm\tfrac\lambda{32}n^2$ can be much larger than the Hartree term $\tfrac\lambda2S^2$; Section 14.10 meets exactly this situation.

### 14.7 The Kohn–Sham equations of dirac16complex00

**The frame is that of Chapter 13.** The static primordial field in the warped coordinate $y$ with the Z2 brane (Section 13.2), the good sector and the stationary ansatz with the factor $W^{-3}$ (Section 13.3), the eight $2\times2$ blocks (Section 13.4), the block equation, its Hamiltonian form, the conserved $y$-current and the boundary conditions (Section 13.5), and the torus and the bookkeeping of particles and sea (Section 13.7) are statements about the linear Dirac operator in the fixed field. They hold word for word for commuting components. The reduced equation and the block forms were nevertheless derived again for dirac16complex00 and verified in both of its reports: see the check `C00_static_geometryAndReducedEquation` and the check `C00_static_blocksFromStage4Theory` in the Wolfram report, and the two checks with the same names after the prefix `S5_` in the Python report.

**The local potentials.** Evaluate $e_x=\mathrm{sg}\,\tfrac\lambda{32}(n^2+S^2)$ with the local proper densities $n_p(y)$ and $S_p(y)$ (the local density approximation of Section 12.12). Its derivatives are the exchange potentials

$$
v_v=\frac{\partial e_x}{\partial n}=\mathrm{sg}\,\frac\lambda{16}\,n,\qquad v_s=\frac{\partial e_x}{\partial S}=\mathrm{sg}\,\frac\lambda{16}\,S,
$$

and the effective mass is $M_{\text{eff}}=m+\lambda S_p+v_s=m+\bigl(1+\tfrac{\mathrm{sg}}{16}\bigr)\lambda S_p$ (checks `PAIR_stat_ldaPotentials`, `PAIR_T3block_statisticsCoefficients`, `S5_stat_ldaPotentials`). Side by side:

| quantity | dirac16complex ($\mathrm{sg}=-1$) | dirac16complex00 ($\mathrm{sg}=+1$) |
| --- | --- | --- |
| exchange energy density $e_x$ | $-\tfrac\lambda{32}(n^2+S^2)$ | $+\tfrac\lambda{32}(n^2+S^2)$ |
| filled shell $E_x/E_H$ | $-\tfrac18$ | $+\tfrac18$ |
| vector potential $v=v_v$ | $-\tfrac\lambda{16}n_p$ | $+\tfrac\lambda{16}n_p$ |
| scalar potential $v_s$ | $-\tfrac\lambda{16}S_p$ | $+\tfrac\lambda{16}S_p$ |
| effective mass $M_{\text{eff}}$ | $m+\tfrac{15}{16}\lambda S_p$ | $m+\tfrac{17}{16}\lambda S_p$ |

The pair $(M_{\text{eff}}^{00},v^{00})$ is the **Kohn–Sham fermion-gas thermodynamic pseudo-potential** of dirac16complex00: the name that section 3 of `handoff/specs/STAGE4_SPEC.md` gives to the pair $(M_{\text{eff}},v)$ and that Chapter 13 uses (the Stage-5 specification says “effective potential”).

**The functional.** In the notation of Section 13.9 (orbitals $\chi_n$ with block type $j_n$ and momentum $k_n$, normalized by $\int\chi_n^\dagger\chi_n\,dy=1$, occupations $f_n$, proper volume element $dV=e^{6Hy}\ell^3dy$, the Pauli matrices $\sigma_x,\sigma_y,\sigma_z$ of Section 2.3, and the momentum weight $\xi(y)=e^{-Hy-a_{4,0}}$ of Section 13.3), the Mermin functional of dirac16complex00 is

$$
\begin{aligned}
F^{00}&=\sum_nf_n\langle\chi_n|h_0|\chi_n\rangle-T\,S_{\text{ent}}+E_H+E_x^{00},\qquad h_0=j\Bigl[-i\sigma_x\frac d{dy}+m\sigma_y+\xi k\sigma_z\Bigr],\\
E_H&=\frac\lambda2\int S_p^2\,dV,\qquad E_x^{00}=+\frac\lambda{32}\int\bigl(n_p^2+S_p^2\bigr)\,dV,
\end{aligned}
$$

with $n_p=e^{-6Hy}\sum_nf_n\chi_n^\dagger\chi_n/\ell^3$ and $S_p=e^{-6Hy}\sum_nf_n\chi_n^\dagger(j_n\sigma_y)\chi_n/\ell^3$. (As in Section 13.9, in the solver these sums, and the one-body sum of $F^{00}$, run over the particle and the sea levels with the weights $w_n$ of Section 13.7 in place of $f_n$: $w_n=f_n$ on a particle level and $w_n=-(1-f_n)$ on a sea level, prescription P2. This is why the total energy below is written with $w_n$.) It differs from the functional of Section 13.9 only in the sign of the exchange term. (The theory files and the Rust code call the momentum weight `kappa`, and the check names write the Pauli matrices as sigma1, sigma2, sigma3; in this book $\kappa$ is the gravitational coupling of Section 13.2, as in Section 14.10.)

**Stationarity.** Vary $\chi_n^\dagger(y)$ as in Section 13.9. The derivative of $\int n_p^2\,dV$ is $2n_p(y)\cdot e^{6Hy}\ell^3\cdot e^{-6Hy}f_n\chi_n(y)/\ell^3=2f_nn_p\chi_n$: the factor $e^{6Hy}$ of the volume element cancels the factor $e^{-6Hy}$ of the density. In the same way $\int S_p^2\,dV$ gives $2f_nS_p\,j_n\sigma_y\chi_n$. Hence $E_x^{00}$ contributes $\tfrac\lambda{16}f_n\bigl(n_p+S_pj_n\sigma_y\bigr)\chi_n=f_n\bigl(v_v+v_sj_n\sigma_y\bigr)\chi_n$ and $E_H$ contributes $f_n\lambda S_pj_n\sigma_y\chi_n$. Dividing by $f_n$, the Kohn–Sham equation of dirac16complex00 is $h_j^{00}\chi_n=\varepsilon_n\chi_n$ with

$$
h_j^{00}=j\Bigl[-i\sigma_x\frac d{dy}+\Bigl(m+\tfrac{17}{16}\lambda S_p(y)\Bigr)\sigma_y+\xi(y)\,k\,\sigma_z\Bigr]+\frac\lambda{16}\,n_p(y),
$$

the Hamiltonian form $h_j$ of Section 13.5 with the new potentials (check `PAIR_T3ks_stationarityBothStatistics`, which carries the statistics sign as a symbol). In the real variables $\chi=(a,ib)$ of Section 13.5 it reads $a'=M_{\text{eff}}a-(jE+\xi k)b$ and $b'=(jE-\xi k)a-M_{\text{eff}}b$ with $M_{\text{eff}}=m+\tfrac{17}{16}\lambda S_p$ and $E=\varepsilon-\tfrac\lambda{16}n_p$. Stationarity with respect to the occupations gives the Fermi–Dirac occupations exactly as in Section 13.9: in this model they follow from the entropy term that prescription P2 puts into the functional, not from any property of the classical field.

**Total energy.** Both interaction functionals are quadratic in the densities, so the double-counting argument of Section 13.9 applies unchanged:

$$
E=\sum_nw_n\varepsilon_n-E_H-E_x^{00},\qquad F=E-TS_{\text{ent}},\qquad \frac{dF}{d\lambda}=\frac{E_H+E_x^{00}}\lambda .
$$

**Worked example.** To see the two sets of formulas at work, take at one point the numbers $\lambda=16$, $n=\tfrac12$ and $S=-\tfrac14$ (chosen for easy arithmetic, not taken from a run; $H=1$). Then $e_H=8\cdot\tfrac1{16}=\tfrac12$ and $\tfrac\lambda{32}(n^2+S^2)=\tfrac12\bigl(\tfrac14+\tfrac1{16}\bigr)=\tfrac5{32}$, so $e_x=-\tfrac5{32}$ for dirac16complex and $+\tfrac5{32}$ for dirac16complex00. The vector potentials are $\mp\tfrac{16}{16}\cdot\tfrac12=\mp\tfrac12$, the scalar potentials $\mp\tfrac{16}{16}\cdot(-\tfrac14)=\pm\tfrac14$, and the mass shifts $\lambda S+v_s=-4+\tfrac14=-\tfrac{15}4$ (dirac16complex, which is $\tfrac{15}{16}\cdot16\cdot(-\tfrac14)$) and $-4-\tfrac14=-\tfrac{17}4$ (dirac16complex00, which is $\tfrac{17}{16}\cdot16\cdot(-\tfrac14)$).

**The first-order effect of the sign.** By the Hellmann–Feynman relation just stated, $dE/d\lambda$ at $\lambda=0$ is the interaction energy per unit $\lambda$ evaluated with the densities of the free ($\lambda=0$) state (the envelope argument of Section 13.9: the change of the orbitals does not contribute at first order, because $F$ is stationary). Hence

$$
E(\lambda)=E(0)+E_H^{\text{free}}+\mathrm{sg}\,X^{\text{free}}+O(\lambda^2),\qquad X^{\text{free}}=\frac\lambda{32}\int\bigl(n_p^2+S_p^2\bigr)\,dV\Big|_{\lambda=0},
$$

with $X^{\text{free}}\ge0$ for $\lambda>0$. So at first order the energies of the two fields differ by $2X^{\text{free}}$, dirac16complex00 lying higher for a repulsive coupling. The orbital energies show the same sign: for $\lambda>0$ the exchange potential $v^{00}=+\tfrac\lambda{16}n_p$ is positive and shifts the particle levels up, whereas $v=-\tfrac\lambda{16}n_p$ shifts them down for dirac16complex; the mass shift, $\tfrac{17}{16}\lambda S_p$ against $\tfrac{15}{16}\lambda S_p$, is nearly the same for both fields. Section 14.10 confirms both statements numerically.

### 14.8 What the model is, and what it is not

The derivations of Sections 14.3 to 14.7 are exact. What they describe is fixed by the prescriptions P1 to P4. Two exact facts, proved below, limit what the resulting numbers mean, and a third point says what the model is not; it is a statement about how the model is defined, not a theorem.

**First fact: the covariance of the model is not positive.** For any collection of classical fields, whatever its probability distribution, the **covariance** matrix $K_{ab}=\langle\Psi_a\Psi_b^\ast\rangle$ is positive semidefinite: for every vector $v$ the number $v^\dagger\Psi=\sum_av_a^\ast\Psi_a$ has $|v^\dagger\Psi|^2=\sum_{a,b}v_a^\ast\Psi_a\Psi_b^\ast v_b$, whose average is

$$
\bigl\langle|v^\dagger\Psi|^2\bigr\rangle=\sum_{a,b}v_a^\ast K_{ab}v_b=v^\dagger Kv\ \ge\ 0,
$$

because the average of a non-negative quantity is not negative. Under prescription P3 the covariance is $K=\rho B$ (Section 14.6). Take the filled shell at rest, $\rho=P_+=\tfrac12(1-i\gamma^4)$. $P_+$ and $B$ are Hermitian and commute ($\gamma^4$ commutes with $B$, Section 8.11), so they have a common orthonormal basis of eigenvectors. On the eight-dimensional range of $P_+$ (the positive-energy states at rest) the Krein form $u^\dagger Bu$ has the signature (4,4) (Section 8.8): $B$ has the eigenvalue $+1$ four times and $-1$ four times there. Hence

$$
K=P_+B\ \text{ has the eigenvalues }\ +1\ (4\text{ times}),\quad -1\ (4\text{ times}),\quad 0\ (8\text{ times}),
$$

as the Wolfram verifier records (measurement `stat_restShellCovarianceEigenvalues` and check `PAIR_stat_expectationRuleCovarianceIndefinite`, `wolfram-pairing-report.json`). An explicit vector: the rest state $u_-=\tfrac12(e_0+e_4+i\,e_9-i\,e_{13})$ of Section 8.8 has $-i\gamma^4u_-=u_-$, so $P_+u_-=u_-$, and $Bu_-=-u_-$, so $Ku_-=-u_-$ and $u_-^\dagger Ku_-=-1$. The “average of $|u_-^\dagger\Psi|^2$” would be $-1$. **No probability distribution of classical fields has this covariance.** For the orbitals of the four blocks with Krein sign $js_2=-1$ the model is not an average over classical field configurations; it is a formal Gaussian functional whose covariance carries the Krein signs, which `pairing-theory.json` (key `statistics.positivity.consequence`) calls a “FORMAL (Krein-signed) Gaussian functional”.

**A second, independent source of negative variances.** In the model the mean squared amplitude of the orbital $u_n$ is $w_n\beta_n$, the eigenvalue of $K=\sum_nw_n\beta_nu_nu_n^\dagger$ on $u_n$ (Section 14.6). The Krein sign $\beta_n$ is one factor; the weight $w_n$ of prescription P2 is the other. On a sea level $w_n=-(1-f_n)$, which is negative whenever the level is not completely full, and at a temperature $T>0$ the Fermi–Dirac occupation $f_n=1/(e^{(\varepsilon_n-\mu)/T}+1)$ is smaller than 1 for every level, so every sea level carries a thermal hole of weight $1-f_n>0$ (tiny for deep levels, but not zero). The four possible cases are:

| level | block with $\beta_n=+1$ | block with $\beta_n=-1$ |
| --- | --- | --- |
| particle, $w_n=f_n\ge0$ | $w_n\beta_n\ge0$ | $w_n\beta_n\le0$ |
| sea, $w_n=-(1-f_n)\le0$ | $w_n\beta_n\le0$ | $w_n\beta_n\ge0$ |

So at $T>0$ negative variances occur in the blocks of both Krein signs: from the occupied particle levels in the blocks with $\beta_n=-1$, and from the thermal holes of the sea in the blocks with $\beta_n=+1$. This applies to the runs at $T=0.3H$ of Section 14.10. At $T=0$ every sea level is full, $w_n=0$ there, and only the Krein sign remains as a source of negative variances.

**What the honest alternative gives.** An honest Gaussian ensemble of classical waves filling the rest shell has the covariance $K=\rho=P_+$. Its charge density is $\mathrm{Tr}(BP_+)=\tfrac12\mathrm{Tr}B-\tfrac i2\mathrm{Tr}(B\gamma^4)=0$, because $\mathrm{Tr}B=0$ and $B\gamma^4=-iC(\gamma^4)^2=iC$ with $\mathrm{Tr}C=0$; and its scalar density is $\mathrm{Tr}(CP_+)=\tfrac12\mathrm{Tr}C-\tfrac i2\mathrm{Tr}(C\gamma^4)=0$, because a product of four or of five different gammas is traceless (Chapter 2). The four modes with Krein sign $+1$ and the four with $-1$ cancel in both densities. The expectation-value rule instead gives $\mathrm{Tr}(B\,BP_+)=\mathrm{Tr}P_+=8$ and $\mathrm{Tr}(BC\,P_+)=8$. The Stage-5 model keeps the rule, so that both fields carry the same densities as functions of their orbitals; `pairing-theory.json` records this as “a modelling choice, stated as such” (check `PAIR_stat_expectationRuleCovarianceIndefinite` contains the two zero traces).

**Second fact: the model's energies are not the classical energies.** In a block of type $(j,s_2)$ the matrix $B$ is the number $js_2$ (Section 13.4). So a field $\Psi$ whose sixteen components lie in one block satisfies $B\Psi=js_2\Psi$ at every point, and, because $B$ is Hermitian, $\Psi^\dagger B=(B\Psi)^\dagger=js_2\,\Psi^\dagger$: the row $\Psi^\dagger B$ is the row $\Psi^\dagger$ multiplied by the number $js_2$. The expectation-value rule of the Kohn–Sham model replaces $\Psi^\dagger$ by $\Psi^\dagger B$ (Section 13.7), that is, for a single-block mode, by $js_2\,\Psi^\dagger$, and it does so everywhere, also inside derivatives of $\Psi^\dagger$. Every term of the one-body energy–momentum tensor (the part without the interaction, Section 13.14) contains exactly one factor built from $\Psi^\dagger$ (the adjoint $\bar\Psi=\Psi^\dagger C$ or its derivative $D_\mu\bar\Psi$) and one built from $\Psi$. So every term, and with it every component, is multiplied by the same number $js_2$, and since $(js_2)^2=1$,

$$
T_{\mu\nu}^{\text{classical}}=js_2\;T_{\mu\nu}^{\text{KS one-body}}
$$

for every single-block mode, component by component, and even for fields that do not solve the field equation (check `C00_static_classicalModeIsKreinWeightedKS`, which compares all 64 components of the tensor in each of the eight blocks, and its twin `S5_static_classicalModeIsKreinWeightedKS` in `python-dirac16complex00-report.json`; `dirac16complex00-theory.json`, key `static.classicalVersusKohnSham`). The energy density shows it most simply. By Section 13.14 its one-body part is $\varepsilon\,\Psi^\dagger B\Psi$. For a classical single-block field this is $js_2\,\varepsilon\,\Psi^\dagger\Psi$, while the Kohn–Sham orbital contributes $\varepsilon\,u^\dagger B^2u=\varepsilon\,n$.

**A worked example: two box modes.** The report computes one explicit mode in a block of each Krein sign (check `C00_static_classicalEnergyKreinSigned`, and `S5_static_classicalEnergyKreinSigned` in the Python report; `dirac16complex00-theory.json`, key `static.boxModes`). Take the free problem ($\lambda=0$, so $M_{\text{eff}}=m$ and $v=0$) with $m=3$ at zero momentum $k=0$ in a box of length $L=\pi/4$, and the first massive level of parity $+$ of Section 13.6: $p=\pi/L=4$, $\varepsilon=\sqrt{m^2+p^2}=\sqrt{9+16}=5$ and

$$
\chi_2=\sin4y,\qquad \chi_1=\frac{3\sin4y+4\cos4y}{5ij},
$$

with $\chi_2(0)=\sin0=0$ (parity $+$) and $\chi_2(-\pi/4)=\sin(-\pi)=0$ (the bag condition at the end of the box). The check puts this orbital into block 0 ($js_2=+1$) and into block 2 ($js_2=-1$) as the sixteen-component column $\chi=\chi_1v_++\chi_2v_-$, with the unnormalized basis vectors $v_\pm$ of Section 13.4 ($|v_\pm|^2=8$), verifies the full sixteen-component reduced equation $\gamma^0\chi'-5i\gamma^4\chi=3\chi$ and the two boundary conditions, and computes the classical energy density. At $\lambda=0$ the energy density is $\varepsilon\,\Psi^\dagger B\Psi=js_2\,\varepsilon\,\Psi^\dagger\Psi$, and $W^6\Psi^\dagger\Psi=\chi^\dagger\chi=8\bigl(|\chi_1|^2+|\chi_2|^2\bigr)$ (Section 13.3, with $W^6=\sqrt{|g|}$), so

$$
\rho\,W^6=js_2\cdot5\cdot8\Bigl[\sin^24y+\tfrac1{25}\bigl(3\sin4y+4\cos4y\bigr)^2\Bigr]=js_2\cdot\tfrac85\bigl(25-9\cos8y+12\sin8y\bigr)
$$

(Exercise 14.15 does the trigonometry). The report records exactly this profile for block 0 and its negative for block 2. Since $-9\cos8y+12\sin8y$ never goes below $-\sqrt{9^2+12^2}=-15$ (Exercise 14.15), the bracket is at least $10$: the classical energy density is positive everywhere in block 0 and negative everywhere in block 2. The Kohn–Sham model gives both orbitals the positive energy $\varepsilon=5$. For the four blocks of Krein sign $-1$ a positive Kohn–Sham orbital energy therefore corresponds to a classical wave of negative energy: the Kohn–Sham energies of dirac16complex00 are Krein-weighted energies, not the energies of classical field configurations. (The example also shows that the classical energy of dirac16complex00 has no lower bound in the static primordial field either: multiply the mode of block 2 by a large number.)

**Third point: it is not a quantum theory.** This is a statement about how the model is defined, not a theorem. One might hope to reinterpret the model as the quantization of dirac16complex00 with commutators instead of anticommutators. The model is not obtained that way: the Stage-5 specification does not attempt such a quantization, and neither does this chapter. The reason for not attempting it is a theorem that we quote and do not prove: in ordinary space-time with one time, Pauli's spin–statistics theorem (1940) shows that a spinor field quantized with commutators has either an energy without lower bound or states of negative norm. No such theorem is proved for signature (4,4) in this book (Chapter 8).

**The words “ground state” and “excited state”.** In this chapter the **ground state** of dirac16complex00 means, by definition, the self-consistent solution of the Kohn–Sham equations of Section 14.7 reached by continuation in the coupling from $\lambda=0$ (erratum E4.8, the definition of Chapter 13). It is not the minimum of any energy of the classical field, which has none (Section 14.2). The **first excited state** means the three quantities of Section 12.15 computed in this model: the Kohn–Sham gap, the particle–hole list and the Delta-SCF energy.

**No correlation term.** For the quantized dirac16complex, Section 13.8 argued that a contact coupling of mass dimension $-6$ leaves no well-defined correlation energy to approximate. For the classical ensemble of the model the analogue of correlation would be the departure of the interacting ensemble from a Gaussian one; it is not computed either. The model is exchange-only for both fields.

**In one paragraph.** The dirac16complex00 Kohn–Sham model is a mean-field functional of a Gaussian (random-phase) ensemble of classical modes, with the occupations of a fermion gas imposed and with the Krein-signed densities of the quantized field adopted by prescription, so that the two fields differ in exactly one respect: the sign of the exchange term, which Theorems 14.4 and 14.5 derive. Its “ground state” is a definition, not a minimum. Its energies are not the energies of classical field configurations. It is not a quantum theory of commuting spinors.

### 14.9 How the model is solved, and what was computed

**Two solvers.** The equations of Section 14.7 are those of Chapter 13 with two coefficients changed, $\tfrac{15}{16}\to\tfrac{17}{16}$ in the effective mass and $-\tfrac1{16}\to+\tfrac1{16}$ in the vector potential. Both Stage-4 solvers received an option for the statistics sign in Stage 5. The Rust solver `studies/dirac16complex_kohn_sham`, which integrates the block equation by shooting (Section 13.10), has the subcommand `pairs` (module `src/pairs.rs`, with the statistics `Commuting` for dirac16complex00). The independent reference solver `scripts/ks_reference_solver.py`, driven by `scripts/ks_reference_pairs.py` (field label `d16c00`), uses a matrix method instead of shooting: it places one component of each block orbital on the nodes and the other on the half nodes of a uniform grid in $y$ (a staggered grid), turns the Hermitian block operator into a real symmetric matrix, diagonalizes it, solves every problem on three grids of $N_0$, $2N_0$ and $4N_0$ intervals ($N_0=120$ for $m=3$), and extrapolates to zero grid spacing by eliminating the error terms proportional to $h^2$ and $h^3$ (the header of `scripts/ks_reference_solver.py`). Without interaction the statistics does not enter at all, and the two fields are the same numerical problem: the reference runs of the two fields at $\lambda=0$ agree in every printed digit, and the Rust module states the same (“The two statistics at lambda = 0 are the same problem (bit for bit)”, header of `src/pairs.rs`).

**The couplings.** dirac16complex00 uses the same numerical $\hat\lambda=\lambda m^6$ as dirac16complex: the Stage-4 reference coupling of the configuration $(|m|,L,N)$, calibrated so that the first-order pseudo-potential of dirac16complex reaches $0.1\,m$ ($\hat\lambda_1$) or $1\,m$ ($\hat\lambda_2=10\hat\lambda_1$) (Section 13.10). For $(m,L,N)=(3,3,112)$ the file `artifacts/dirac16complex/kohn-sham/reference/couplings/coupling-m3_L3_N112.json` gives $\hat\lambda_1=852.6397026$, that is $\lambda=\hat\lambda_1/m^6=852.6397026/729=1.169602$ in units of $H^{-6}$ (the coupling has the mass dimension $-6$, Section 13.8).

**What was planned.** The Stage-5 run matrix (the header of `scripts/ks_reference_pairs.py`) is $(|m|,N)\in\{(1,8),(1,112),(3,8),(3,112)\}$ with $L=3$, $\Delta k=0.25\,|m|$, $\hat\lambda\in\{0,\pm\hat\lambda_1,\pm\hat\lambda_2\}$, $T=0$ for every configuration and $T=0.1\,|m|$ for $N=112$, both fields, and three universes each: $+M$ (the problem of Chapter 13), $-M$ with the transformed boundary conditions, and $-M$ with the untransformed ones (the two $-M$ universes belong to the pairing theorems of Chapter 15).

**What exists for dirac16complex00.** The committed summary `artifacts/dirac16complex/pair-creation/reference/reference-pairs-summary.json` (key `complete`: `false`) contains, for dirac16complex00 with $m=3$ and $N=112$, the following (“control” is the $-M$ universe with the untransformed boundary conditions):

| coupling, temperature | $+M$ | $-M$ | control |
| --- | --- | --- | --- |
| $\lambda=0$, $T=0$ | converged | converged | converged |
| $\lambda=0$, $T=0.3H$ | converged | converged | converged |
| $+\hat\lambda_1$, $T=0$ | converged | pending | failed |
| $+\hat\lambda_2$, $T=0$ | pending | failed | failed |
| $-\hat\lambda_1$, $T=0$ | pending | pending | pending |
| $-\hat\lambda_2$, $T=0$ | pending | pending | pending |
| $\lambda\ne0$, $T=0.3H$ | not attempted | not attempted | not attempted |

For $m=3$, $N=8$ and for $m=1$ ($N=8$ and $N=112$) every dirac16complex00 run is pending. “Pending” means never run; the three failed runs stopped because the energy window of the self-consistent loop grew beyond the cap of $20\,\lvert m\rvert$ that the driver imposes. The keys `failed`, `notAttempted` and `pending` of the summary list these runs, and the reason of each failure is the key `failed` of its run record.

For the interacting runs at $T=0.3H$ the driver estimates the first-order pseudo-potential from the free thermal state, $|\hat\lambda_1|$ times its strength, and finds $84.1\,|m|$ (key `thermoFirstOrder`): the free thermal gas at $T=0.1\,|m|$ has a much larger density near the tip than the brane-localized $T=0$ state that calibrates $\hat\lambda_1$, so the coupling calibrated at $T=0$ is far outside the window of Chapter 13 there. The committed Rust `pairs` outputs in `artifacts/dirac16complex/pair-creation/rust/pairs/` contain only dirac16complex configurations and no `summary.json`; the checker `scripts/check_dirac16complex_pairs.py` has no committed report. **So every number of dirac16complex00 in this chapter comes from one solver, without an independent cross-check.**

### 14.10 Ground and first excited states of both fields side by side

The only configuration in which both fields are computed with interaction is $m=3H$, $L=3/H$, $N=112$, $a_{4,0}=0$, $\Delta k=0.25\,m=0.75H$, both brane parities, $T=0$. In the tables below, as in the labels of the runs, **d16c** stands for dirac16complex and **d16c00** for dirac16complex00. The numbers are those of the following run records of `reference-pairs-summary.json`:

```
d16c_m3_L3_N112_lam0_T0/plusM       the free state (d16c00 has the identical record)
d16c_m3_L3_N112_lamp1_T0/plusM      dirac16complex at +lambda_hat_1
d16c00_m3_L3_N112_lamp1_T0/plusM    dirac16complex00 at +lambda_hat_1
```

Energies are in units of $H$; $\hat\lambda/\hat\lambda_1=0$ is the free state, which is the same for both fields.

**Ground states** (keys `extrapolated.total`, `ksSum`, `hartree`, `exchange` and `mu` of each run record; at $T=0$ the chemical potential is $\varepsilon_{\text{HOMO}}$):

| field | $\hat\lambda/\hat\lambda_1$ | $E_0$ | $\sum w\varepsilon$ | $E_H$ | $E_x$ | $\varepsilon_{\text{HOMO}}$ |
| --- | --- | --- | --- | --- | --- | --- |
| both | 0 | 131.448298 | 131.448298 | 0 | 0 | 1.542011 |
| d16c | +1 | 127.409033 | 123.547979 | 0.874212 | $-4.735266$ | 1.473938 |
| d16c00 | +1 | 136.882683 | 142.569624 | 0.947939 | $+4.739001$ | 1.644264 |

**First excited states** (keys `ksGap` and `excited.deltaSCF`; $\varepsilon_{\text{LUMO}}$ is the particle energy of the first particle–hole pair):

| field | $\hat\lambda/\hat\lambda_1$ | $\varepsilon_{\text{LUMO}}$ | $\Delta_{KS}$ | $\Delta_{\text{SCF}}$ | $\Delta_{\text{SCF}}-\Delta_{KS}$ |
| --- | --- | --- | --- | --- | --- |
| both | 0 | 1.776275 | 0.2342638 | 0.2342638 | $1\times10^{-15}$ |
| d16c | +1 | 1.708971 | 0.2350337 | 0.2350344 | $7.0\times10^{-7}$ |
| d16c00 | +1 | 1.879407 | 0.2351435 | 0.2351447 | $1.25\times10^{-6}$ |

For dirac16complex the Stage-4 Rust solver gives, for the same configuration, $E_0=127.409027$, $E_H=0.874212$, $E_x=-4.735270$ and $\Delta_{KS}=0.2350337$ at $+\hat\lambda_1$, and $E_0=131.448295$, $\Delta_{KS}=0.2342638$ at $\lambda=0$ (`artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lamp1_T0/run.json` and `m3_L3_N112_lam0_T0/run.json`; the Rust coupling $852.6397056$ is calibrated separately and differs from the reference one in the ninth digit). The two solvers agree to $6\times10^{-6}$ in $E_0$ and $6\times10^{-9}$ in the gap. (Section 13.15 describes how the Stage-4 cross-check works. Its final committed result is the report `artifacts/dirac16complex/kohn-sham/python-check-report.json`: 63 checks, of which 62 are true. The one that fails, `canonical_eigenvalues`, concerns a single run of Chapter 13, the smeared ground state for $m=1$, $L=3$, $N=1016$ at $-\hat\lambda_2$ computed by the Rust solver on 301 grid points. Of the 58412 level comparisons of all runs, the only ones outside their tolerance are four of the 79 compared levels of that run (in both of its records, the ground state and the excited state); the worst, the deep level $\varepsilon=-1.05374908\,m$, differs from the reference solver by $2.2\times10^{-6}$ against a tolerance of $1.05\times10^{-6}$ (key `canonical_eigenvalues_detail`), while the refined Rust run of the same state on 601 grid points agrees with the reference levels to $1.8\times10^{-7}$ (comparison `canonical_excited_m1_L3_N1016_lamm2_T0_g601`). The Delta-SCF energy of the same run agrees within its tolerance after erratum E4.13 of `handoff/specs/STAGE4_SPEC.md` (check `canonical_deltaSCF` true). The Stage-4 gate had not been run.) There is no second solver for the dirac16complex00 column.

**Worked checks.** (i) The double-counting formula of Section 14.7 holds in both rows: $123.547979-0.874212+4.735266=127.409033$ and $142.569624-0.947939-4.739001=136.882684$ (the last digit is rounding; the unrounded record gives $136.8826835$). (ii) The statistics sign: the exchange energies have opposite signs and nearly equal magnitudes, $-4.735$ and $+4.739$. (iii) The first-order estimate of Section 14.7 says that the two energies differ by $2X^{\text{free}}$, twice the magnitude of the exchange energy of the free densities; each computed $\lvert E_x\rvert$ equals $X^{\text{free}}$ up to terms of second order in $\lambda$. Indeed the computed difference $136.882683-127.409033=9.473650$ is close to $E_x^{00}-E_x=4.739001+4.735266=9.474267$: the two numbers are equal at first order in $\lambda$, and here they differ by $6.2\times10^{-4}$. (iv) The levels move as predicted: the highest occupied level rises from $1.542$ to $1.644$ for dirac16complex00, whose exchange potential $+\tfrac\lambda{16}n_p$ is positive, and falls to $1.474$ for dirac16complex, whose exchange potential $-\tfrac\lambda{16}n_p$ is negative (the nearly equal mass shifts contribute to both). (v) This is a fast gas in the sense of Section 14.6: the exchange energies are five times the Hartree energies, because the brane band carries a small scalar density ($\lvert S\rvert\ll n$).

**What the first excited state is.** In all three rows the highest occupied level is the brane band (Section 13.6) on the torus shell $\nu=n_1^2+n_2^2+n_3^2=3$, that is $k=\sqrt3\cdot0.75H=1.299H$ ($0.433\,m$), with $4\cdot8=32$ states, and the lowest empty level is the band on the shell $\nu=4$, $k=1.5H$ ($0.5\,m$), with $4\cdot6=24$ states (reference level labels `3:+1:-1:0` and `4:+1:-1:0`, which name the shell $\nu$, the brane parity, the block type in the reference solver's convention and the index of the level, with the multiplicities `homoMultiplicity` 32 and `lumoMultiplicity` 24). The filling is the one of Section 13.7: $8+24+48+32=112$. The first excitation moves one particle from the shell $\nu=3$ to the shell $\nu=4$, an excitation **within the brane band**, exactly as for the $m=1$ states of Chapter 13. The next particle–hole energies of dirac16complex00 are $0.441136$, $0.516079$ and $0.626495$ (dirac16complex: $0.440969$, $0.515752$, $0.626300$; key `excited.particleHole`). The interaction raises the gap by $7.7\times10^{-4}$ (dirac16complex) and $8.8\times10^{-4}$ (dirac16complex00), and the orbital relaxation $\Delta_{\text{SCF}}-\Delta_{KS}$ is of order $10^{-6}$ in both: at this coupling the difference between the two statistics shows in the total energy and in the absolute position of the levels, hardly in the excitation energy.

**Energy–momentum tensor.** The proper-volume averages of Section 13.14 (key `emt` of each run; $\kappa_{\text{needed}}=-21H^2/\langle\rho\rangle$):

| field | $\hat\lambda/\hat\lambda_1$ | $\langle\rho\rangle$ | $w_y$ | $w_3$ | $w_t$ | $\kappa_{\text{needed}}$ |
| --- | --- | --- | --- | --- | --- | --- |
| both | 0 | 1.341376 | 0.1772 | 0.3291 | 0 | $-15.66$ |
| d16c | +1 | 1.300157 | 0.1753 | 0.3110 | $-0.0303$ | $-16.15$ |
| d16c00 | +1 | 1.396831 | 0.2371 | 0.3596 | $+0.0415$ | $-15.03$ |

The pressure along the extra times is $p_t=L_s=e_H+e_x$ (Section 13.14), so its sign follows the exchange sign: the average $\langle p_t\rangle$ is $-0.0394$ for dirac16complex and $+0.0580$ for dirac16complex00. In every row $\langle\rho\rangle>0$, while the static field requires $\rho_{\text{req}}=-21H^2/\kappa<0$; a negative $\kappa$ would be needed, and the sourcing conditions of erratum E4.1 are not met (for dirac16complex00 the run records $\lambda\langle S_p\rangle/m=-0.0347$ against the required $-\tfrac56$; key `emt.E41_sourcingConditions`). The verdict of Section 13.14 is unchanged for dirac16complex00 at this coupling.

**Finite temperature without interaction.** At $T=0.1\,m=0.3H$ and $\lambda=0$ both fields give $\mu=1.469481$, $E=161.026343$, $F=104.727753$, $S_{\text{ent}}=187.661967$ and $\Delta_{KS}=0.279429$ (runs `d16c_m3_L3_N112_lam0_T0p1/plusM` and `d16c00_m3_L3_N112_lam0_T0p1/plusM`), and $F=E-TS_{\text{ent}}=161.026343-0.3\cdot187.661967=104.727753$ checks. The interacting thermal points were not attempted (Section 14.9), so no finite-temperature result distinguishes the two fields.

**The mirror universes, briefly.** Chapter 15 proves that the Kohn–Sham problem with mass $-m$, the same $\lambda$ and the transformed boundary conditions has exactly the same energies as the $+m$ problem, for both statistics (`pairing-theory.json`, key `T3.theoremStandardRule`; checks `PAIR_T3ks_sigma2FunctionalInvariant` and `PAIR_T3ks_sigma2KSOperatorEquivariant`, which carry the statistics sign). For dirac16complex00 the reference solver computed this partner only at $\lambda=0$: $E_0=131.448295$ for $-M$ against $131.448298$ for $+M$, a difference of $2.7\times10^{-6}$ that comes from the staggered grid, which treats the two components of an orbital differently (`pairing-theory.json`, key `T3.numericsPrescription.discretisationNote`). The interacting partner of dirac16complex00 is among the pending runs: **for the commuting field the pairing at $\lambda\ne0$ is proved (Chapter 15) but not demonstrated numerically.**

### 14.11 What was not computed

Stated plainly, for dirac16complex00:

- no Kohn–Sham state for $|m|=1$ (the configurations of Chapter 13) and none for $N=8$ ($N=1016$ was not part of the Stage-5 run matrix);
- for $m=3$, $N=112$: no attractive coupling ($-\hat\lambda_1$, $-\hat\lambda_2$) and no strong coupling ($+\hat\lambda_2$) at $T=0$;
- no interacting state at a finite temperature;
- no run of the Rust solver, hence no comparison of two independent solvers, and no report of the pairs checker; the Stage-5 gate was not run;
- no mirror ($-M$) partner at $\lambda\ne0$.

The missing runs were not completed because the Stage-5 numerics were stopped so that this book could be written (`HANDOFF.md`, section 2). The exact results of Sections 14.3 to 14.8 do not depend on them.

### 14.12 What we proved and what we assumed

**Proved** (derived step by step in this chapter and verified by the named exact checks): the normalization and the moments $\langle(c^\ast)^\alpha c^\beta\rangle=\delta_{\alpha\beta}\alpha!f^\alpha$ of the circular Gaussian, and the corresponding single-mode results for thermal bosons and for fermions; Isserlis' rule for four Gaussian amplitudes (Proposition 14.2) and Wick's rule for four fermion operators (Proposition 14.3); Theorem 14.4, $\langle(\psi^\dagger X\psi)(\psi^\dagger Y\psi)\rangle=\mathrm{Tr}(X\rho)\mathrm{Tr}(Y\rho)+\mathrm{sg}\,\mathrm{Tr}(X\rho Y\rho)$ with $\mathrm{sg}=+1$ for Gaussian waves and $\mathrm{sg}=-1$ for normal-ordered fermions, with the extra term $\mathrm{Tr}(XY\rho)$ of the full quantum products and the deviation of fixed-modulus waves; Theorem 14.5, the Hartree–Fock energy $\tfrac\lambda2[S^2+\mathrm{sg}\,\mathrm{Tr}(BC\rho BC\rho)]$ of the contact interaction for both fields; the filled-shell ratio $E_x=\mathrm{sg}\,E_H/8$; the exact uniform-gas exchange $e_x=\mathrm{sg}\,\tfrac\lambda{32}(n^2+S^2)$ at every temperature, hence $e_x^{00}=+\tfrac\lambda{32}(n^2+S^2)$; the potentials $v^{00}=+\tfrac\lambda{16}n_p$, $v_s^{00}=+\tfrac\lambda{16}S_p$, $M_{\text{eff}}^{00}=m+\tfrac{17}{16}\lambda S_p$; the Kohn–Sham equations of dirac16complex00 from its Mermin functional, and its double-counting formula; the indefinite charge density and the unbounded classical energy of dirac16complex00 (explicit solutions); the indefiniteness of the covariance $K=\rho B$ of the model and the vanishing charge and scalar density of an honest Gaussian filled shell; and the Krein weighting $T^{\text{classical}}=js_2\,T^{\text{KS}}$ of single-block modes, component by component, and the explicit box modes with the energy densities $\pm\tfrac85(25-9\cos8y+12\sin8y)$; and the negative variances $w_n\beta_n$ of the model from the Krein signs and, at $T>0$, from the thermal holes of the sea.

**Computed** (reference solver only, no independent cross-check): the ground and first excited states of dirac16complex00 for $m=3H$, $L=3/H$, $N=112$ at $\lambda=0$ and $+\hat\lambda_1$ and $T=0$, their energy–momentum averages, and the free thermal state at $T=0.3H$ (Section 14.10).

**Assumed:** the model P1 to P4 of Section 14.2: a Gaussian random-phase ensemble of the Kohn–Sham orbitals; Fermi–Dirac occupations and the particle/sea bookkeeping of Chapter 13 imposed on a commuting field; the expectation-value rule of the quantized fermion field adopted by prescription, which makes the covariance Krein-signed rather than positive; exchange only, with no correlation; and everything assumed in Chapter 13 (fixed static field with the Z2 brane, good sector, tip cutoff and bag condition, torus, normal ordering against the free sea, continuation in $\lambda$, no back-reaction). We quoted without proof the harmonic-oscillator spectrum of a boson mode, the general Isserlis and Wick theorems for products of any length (only the four-factor cases are used and proved), Pauli's spin–statistics theorem, and the Hanbury Brown–Twiss effect as an illustration.

**Not claimed:** that the model is a quantum theory of commuting spinors, that its ground state minimizes any energy of the classical field, that its energies are classical field energies, or anything about the creation of universes; Chapters 15 and 16 treat the pairing questions.

### 14.13 Exercises

**Exercise 14.1.** For the circular Gaussian with $f=2$, compute $\langle|c|^6\rangle$ from Proposition 14.1 and directly from the integral $\frac1{\pi f}\int r^6e^{-r^2/f}\,r\,dr\,d\varphi$. Show also that $\langle c^2\rangle=0$.

**Exercise 14.2.** Show that $\sum_{k\ge0}k(k-1)(k-2)\,x^k=6x^3/(1-x)^4$ for $0\le x<1$, and deduce that a thermal boson mode has $\langle k(k-1)(k-2)\rangle=6f^3$ with $f=x/(1-x)$. Compare with $\langle|c|^6\rangle$ of the Gaussian and with the fermion mode.

**Exercise 14.3.** Repeat the first worked example of Section 14.5 (the rotated modes, $X=Y=\sigma_1$) with $f_0=\tfrac12$ and $f_1=\tfrac14$: compute $\rho$, $\mathrm{Tr}(\sigma_1\rho)$, $\mathrm{Tr}(\sigma_1\rho\sigma_1\rho)$ and the three averages of $(\psi^\dagger\sigma_1\psi)^2$.

**Exercise 14.4.** One mode ($d=1$, $X=Y=1$). Compute (a) $\langle|c|^4\rangle$ for a Gaussian amplitude, (b) $\langle(a^\dagger a)^2\rangle$ for a fermion mode with occupation $f$, (c) $\langle(b^\dagger b)^2\rangle$ for a thermal boson mode, and check each against Theorem 14.4 and Remark 1 of Section 14.5.

**Exercise 14.5.** For the filled shell at the moving point of Section 14.6 ($\mathrm{Tr}(BCP_+)=\tfrac{16}5$, $\mathrm{Tr}(BCP_+BCP_+)=\tfrac{32}{25}$) and $\lambda=1$, compute $E_H$ and $E_x$ for both fields and the ratios $E_x/E_H$.

**Exercise 14.6.** Recompute the densities of the exact finite gas of Section 14.6. Each momentum contributes $8(f_+-f_-)$ to $n$ and $8\tfrac m{E}(f_++f_-)$ to $S$, with $m=2$; the shells $E=2,3,4,5$ contain $1,4,2,4$ momenta. Check that $(n^2+S^2)/16$ equals the trace $\tfrac{768720549416}{5636255625}$ recorded in `python-pairing-report.json`.

**Exercise 14.7.** At a point with $\lambda=8$, $n=0.4$ and $S=0.2$ ($H=1$), compute $e_H$, $e_x$, $v_v$, $v_s$ and $M_{\text{eff}}-m$ for both fields, and check the coefficients $\tfrac{15}{16}$ and $\tfrac{17}{16}$.

**Exercise 14.8.** Along the uniform gas at $T=0$, adding particles fills the Fermi surface, where every particle has the energy $E_F$. Show that $dS/dn=m/E_F$ there, and deduce the total derivative $\frac{d e_x}{dn}=\mathrm{sg}\,\tfrac\lambda{16}\bigl(n+S\,\tfrac m{E_F}\bigr)$ (check `PAIR_stat_T0TotalDerivative`).

**Exercise 14.9.** (a) Prove that the covariance $K_{ab}=\langle\Psi_a\Psi_b^\ast\rangle$ of any collection of classical fields is Hermitian and positive semidefinite. (b) For $K=P_+B$ and the vector $u_+=\tfrac12(e_0-e_4-i\,e_9-i\,e_{13})$ of Section 8.8 compute $u_+^\dagger Ku_+$, and compare with the value for $u_-$ found in Section 14.8.

**Exercise 14.10.** In a block of type $(j,s_2)=(1,-1)$, show that $\Psi^\dagger B\Psi=-\Psi^\dagger\Psi$ and conclude the sign of the classical energy density of a stationary single-block wave with $\varepsilon>0$. What does the Kohn–Sham model assign to the same orbital?

**Exercise 14.11.** Using the table of ground states in Section 14.10: (a) verify the double-counting formula for both fields; (b) compute $E_0^{00}-E_0$ and $E_x^{00}-E_x$ and explain why they nearly agree; (c) compute $E_0-E_0(\lambda=0)$ for both fields and compare with $E_H+E_x$ of the same run.

**Exercise 14.12.** Show that the argument of Exercise 13.9 carries over to dirac16complex00: for $N=8$ at $T=0$ the ground states at $\lambda$ and $-\lambda$ are related by moving every occupied orbital from block type $j$ to $-j$, and $E_0^{00}(-\lambda)=-E_0^{00}(\lambda)$. For $\lambda>0$, do the zero modes of dirac16complex00 move up or down? (This state was not computed; the exercise asks for the exact argument.)

**Exercise 14.13.** Explain, from the functional of Section 14.7, why the two fields give identical Kohn–Sham results at $\lambda=0$ at every temperature, and why the reference runs at $T=0.3H$ therefore cannot distinguish them.

**Exercise 14.14.** A classical Gaussian filled rest shell with the positive covariance $K=P_+$: compute the average charge density $\langle\Psi^\dagger B\Psi\rangle$, the scalar density $\langle\Psi^\dagger C\Psi\rangle$ and, with Theorem 14.4, $\langle S^2\rangle$. Compare with the expectation-value rule of the model.

### 14.14 Answers to the exercises

**Answer 14.1.** Proposition 14.1 gives $\langle|c|^6\rangle=3!\,f^3=6\cdot8=48$. Directly: the angular integral gives $2\pi$, so $\langle|c|^6\rangle=\frac2f\int_0^\infty r^7e^{-r^2/f}dr$; with $s=r^2/f$, $r^6=f^3s^3$ and $r\,dr=\tfrac f2ds$, this is $\frac2f\cdot f^3\cdot\frac f2\int_0^\infty s^3e^{-s}ds=f^3\cdot3!=48$. $\langle c^2\rangle$ has $\alpha=0$, $\beta=2$; its angular integral $\int_0^{2\pi}e^{2i\varphi}d\varphi=0$, so it vanishes.

**Answer 14.2.** Differentiate $\sum_kx^k=(1-x)^{-1}$ three times: $\sum_kk(k-1)(k-2)x^{k-3}=6(1-x)^{-4}$; multiply by $x^3$. Then $\langle k(k-1)(k-2)\rangle=(1-x)\cdot6x^3/(1-x)^4=6\bigl(x/(1-x)\bigr)^3=6f^3$, equal to the Gaussian $\langle|c|^6\rangle=3!f^3$. For a fermion mode $k(k-1)(k-2)=0$ for $k\in\{0,1\}$, so the average is 0.

**Answer 14.3.** $\rho=\tfrac12\begin{pmatrix}f_0+f_1&f_0-f_1\\ f_0-f_1&f_0+f_1\end{pmatrix}=\begin{pmatrix}\tfrac38&\tfrac18\\ \tfrac18&\tfrac38\end{pmatrix}$. $\mathrm{Tr}(\sigma_1\rho)=2\cdot\tfrac18=\tfrac14=f_0-f_1$. $\sigma_1\rho=\begin{pmatrix}\tfrac18&\tfrac38\\ \tfrac38&\tfrac18\end{pmatrix}$, so $\mathrm{Tr}(\sigma_1\rho\sigma_1\rho)=\tfrac1{64}+\tfrac9{64}+\tfrac9{64}+\tfrac1{64}=\tfrac{20}{64}=\tfrac5{16}=f_0^2+f_1^2$. Gaussian: $\tfrac1{16}+\tfrac5{16}=\tfrac38$; fixed moduli: $\tfrac38-\tfrac5{16}=\tfrac1{16}=(f_0-f_1)^2$; fermions: $\tfrac1{16}-\tfrac5{16}=-\tfrac14=-2f_0f_1$.

**Answer 14.4.** (a) $2f^2$; Theorem 14.4 with $\rho=f$: $f\cdot f+f\cdot f=2f^2$. (b) $(a^\dagger a)^2=a^\dagger a$ (Section 8.3), so the average is $f$; Remark 1: $f^2-f^2+\mathrm{Tr}(1\cdot1\cdot f)=f$. (c) $\langle N^2\rangle=\langle N(N-1)\rangle+\langle N\rangle=2f^2+f$; the boson version of Remark 1: $f^2+f^2+f$. The classical Gaussian (a) equals the normal-ordered boson value $2f^2$, without the extra $f$.

**Answer 14.5.** $E_H=\tfrac12\bigl(\tfrac{16}5\bigr)^2=\tfrac{128}{25}=5.12$ for both fields. $E_x=\mathrm{sg}\cdot\tfrac12\cdot\tfrac{32}{25}=\mathrm{sg}\,\tfrac{16}{25}=\mp0.64$: $-0.64$ for dirac16complex and $+0.64$ for dirac16complex00. The ratios are $\mp\tfrac{16/25}{128/25}=\mp\tfrac18$.

**Answer 14.6.** Per shell, $n$ receives $8(f_+-f_-)\times$(number of momenta): $E=2$: $8\cdot\tfrac67=\tfrac{48}7$; $E=3$: $8\cdot\tfrac{29}{44}\cdot4=\tfrac{232}{11}$; $E=4$: $8\cdot\tfrac13\cdot2=\tfrac{16}3$; $E=5$: $8\cdot\tfrac3{130}\cdot4=\tfrac{48}{65}$. $S$ receives $8\tfrac2E(f_++f_-)\times$(number): $E=2$: $8\cdot\tfrac87=\tfrac{64}7$; $E=3$: $\tfrac{16}3\cdot\tfrac{37}{44}\cdot4=\tfrac{592}{33}$; $E=4$: $4\cdot\tfrac13\cdot2=\tfrac83$; $E=5$: $\tfrac{16}5\cdot\tfrac{23}{130}\cdot4=\tfrac{736}{325}$. Summing, $n=\tfrac{510808}{15015}\approx34.01985$ and $S=\tfrac{2403416}{75075}\approx32.01353$, and $(n^2+S^2)/16=\tfrac{768720549416}{5636255625}\approx136.38852$, the recorded trace (the common denominators are best handled with a computer or with patience).

**Answer 14.7.** $e_H=\tfrac82\cdot0.04=0.16$. $\tfrac\lambda{32}(n^2+S^2)=\tfrac14(0.16+0.04)=0.05$, so $e_x=-0.05$ (dirac16complex) and $+0.05$ (dirac16complex00). $v_v=\mp\tfrac8{16}\cdot0.4=\mp0.2$ and $v_s=\mp\tfrac8{16}\cdot0.2=\mp0.1$ (upper sign dirac16complex). $\lambda S=1.6$, so $M_{\text{eff}}-m=1.6-0.1=1.5=\tfrac{15}{16}\cdot1.6$ and $1.6+0.1=1.7=\tfrac{17}{16}\cdot1.6$.

**Answer 14.8.** At $T=0$ the added particles sit on the Fermi surface; each adds 1 to the number and $m/E_F$ to the scalar density (Section 13.8: a particle of energy $E_p$ contributes $m/E_p$ to $S$ per unit of $n$), so $dS/dn=m/E_F$. By the chain rule $\frac{de_x}{dn}=\frac{\partial e_x}{\partial n}+\frac{\partial e_x}{\partial S}\frac{dS}{dn}=\mathrm{sg}\,\tfrac\lambda{16}n+\mathrm{sg}\,\tfrac\lambda{16}S\,\tfrac m{E_F}$.

**Answer 14.9.** (a) $K_{ba}^\ast=\langle\Psi_b\Psi_a^\ast\rangle^\ast=\langle\Psi_b^\ast\Psi_a\rangle=K_{ab}$, so $K^\dagger=K$; and $v^\dagger Kv=\langle|v^\dagger\Psi|^2\rangle\ge0$ as shown in Section 14.8. (b) Section 8.8 shows $-i\gamma^4u_+=u_+$ and $Bu_+=u_+$, so $Ku_+=P_+Bu_+=P_+u_+=u_+$ and $u_+^\dagger Ku_+=u_+^\dagger u_+=1$: positive, as a covariance should be, while $u_-^\dagger Ku_-=-1$. Both vectors are positive-energy states at rest; they differ only in their Krein sign.

**Answer 14.10.** In the block $B$ acts as the number $js_2=-1$, so $B\Psi=-\Psi$ and $\Psi^\dagger B\Psi=-\Psi^\dagger\Psi\le0$. The energy density of the classical wave contains $\varepsilon\Psi^\dagger B\Psi=-\varepsilon\Psi^\dagger\Psi<0$ for $\varepsilon>0$: negative. The Kohn–Sham model assigns $\varepsilon\,u^\dagger B^2u=\varepsilon\,n>0$: the opposite sign, which is the factor $js_2$ of Section 14.8.

**Answer 14.11.** (a) Section 14.10, worked check (i). (b) $136.882683-127.409033=9.473650$ and $4.739001+4.735266=9.474267$. At first order both energies are $E(0)+E_H^{\text{free}}\pm X^{\text{free}}$, so their difference is $2X^{\text{free}}$. Each run's $\lvert E_x\rvert$ is $X^{\text{free}}$ up to terms of second order in $\lambda$ (its densities differ from the free ones at first order), so the sum of the two magnitudes is also $2X^{\text{free}}$ at first order. The two numbers therefore agree at first order in $\lambda$, and their difference, $6.2\times10^{-4}$, is of second order. (c) dirac16complex: $127.409033-131.448298=-4.039265$, against $E_H+E_x=0.874212-4.735266=-3.861054$; dirac16complex00: $136.882683-131.448298=5.434385$, against $0.947939+4.739001=5.686940$. The Hellmann–Feynman relation $dE/d\lambda=(E_H+E_x)/\lambda$ (Section 14.7, at $T=0$ where $F=E$) gives $E(\lambda)-E(0)=\int_0^\lambda\bigl(E_H+E_x\bigr)(\lambda')\,\frac{d\lambda'}{\lambda'}$, which equals $(E_H+E_x)(\lambda)$ at first order in $\lambda$; the computed differences, $-0.178$ and $-0.253$, are of second order and say that $(E_H+E_x)/\lambda$ changed along the continuation. Note that no minimum principle fixes the sign of this second-order term here: the one-body Dirac operator has no lower bound, and the particle levels are defined by continuity from $\lambda=0$ (Section 13.7), so the variational argument of Section 12.2 (the exact minimum lies below every trial state) cannot be used to predict it.

**Answer 14.12.** At $T=0$ only the eight zero-mode particle levels carry weight. Move each occupied orbital unchanged from $j$ to $-j$ and replace $\lambda$ by $-\lambda$. Then $n_p$ is unchanged and $S_p\to-S_p$ (because $s=j\chi^\dagger\sigma_2\chi$), so $M_{\text{eff}}-m=\tfrac{17}{16}\lambda S_p$ is unchanged, and $v^{00}=\tfrac\lambda{16}n_p\to-v^{00}$. Writing $h_j^{00}=jD+v^{00}$ with $D$ built from $M_{\text{eff}}$, the new operator is $-jD-v^{00}=-h_j^{00}$: each orbital is an eigenvector with eigenvalue $-\varepsilon$, and it reproduces the densities used, so the mapped state is self-consistent at $-\lambda$ (and it is reached by continuation, since both start from the same eight zero modes). Then $\sum w\varepsilon\to-\sum w\varepsilon$, $E_H=\tfrac\lambda2\int S_p^2dV\to-E_H$ and $E_x^{00}=\tfrac\lambda{32}\int(n_p^2+S_p^2)dV\to-E_x^{00}$, so $E_0^{00}\to-E_0^{00}$. The zero modes have $\varepsilon=0$ and $\chi_2\equiv0$, hence zero scalar density, so to first order they move by the average of $v^{00}=+\tfrac\lambda{16}n_p>0$: **up** for $\lambda>0$, the opposite of dirac16complex, whose zero modes move down (Section 13.11).

**Answer 14.13.** At $\lambda=0$ the terms $E_H$ and $E_x$ vanish, and the only place where $\mathrm{sg}$ appears (the exchange term and its potentials) is multiplied by $\lambda$. The functional, and with it the Kohn–Sham equations, the occupations at every $T$, the energies and the levels, are then identical for the two fields. The only thermal runs of Section 14.10 have $\lambda=0$, so they carry no information on the statistics.

**Answer 14.14.** With $K=P_+$: $\langle\Psi^\dagger B\Psi\rangle=\mathrm{Tr}(BP_+)=0$ and $\langle\Psi^\dagger C\Psi\rangle=\mathrm{Tr}(CP_+)=0$ (Section 14.8). Theorem 14.4 with $X=Y=C$ and $\rho\to P_+$ gives $\langle S^2\rangle=[\mathrm{Tr}(CP_+)]^2+\mathrm{Tr}(CP_+CP_+)=0+\mathrm{Tr}(CP_+CP_+)$; since $C$ commutes with $\gamma^4$, it commutes with $P_+$, so $CP_+CP_+=C^2P_+^2=P_+$ and $\langle S^2\rangle=\mathrm{Tr}P_+=8$. The honest ensemble thus has zero average scalar density but a nonzero average of $S^2$: its interaction energy is pure fluctuation. The rule of the model instead gives $\langle\Psi^\dagger B\Psi\rangle=8$, $S=8$ and $\langle S^2\rangle=64+8=72$, that is $E_H=\tfrac\lambda2\cdot64$ and $E_x=+\tfrac\lambda2\cdot8=E_H/8$.
