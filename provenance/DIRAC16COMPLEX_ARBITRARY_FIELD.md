# dirac16complex: a complex Grassmann spinor of Pin(4,4) in an arbitrary gravitational field

## Lagrangian, covariant field equations, energy-momentum tensor, canonical quantization and equations of state

## Abstract

This document defines dirac16complex, a new 16-component fermion field on an 8-dimensional manifold whose metric has signature (4,4), and derives its physics in an arbitrary gravitational field. The components $\Psi_0,\dots,\Psi_{15}$ are complex-valued and anticommuting (complex Grassmann-odd). They carry the irreducible 16-dimensional complex representation of Pin(4,4), and under Spin(4,4) the same space splits into two inequivalent irreducible 8-dimensional modules. The split-octonion gamma matrices of the author's notebook and the tensor-product gamma matrices of dirac-main describe one Clifford module; exact integer intertwiners, unique up to scale, connect the two pictures. The field couples to gravity only through the canonical spin connection, which is fixed by the vielbein postulate (the total covariant derivative of the vielbein vanishes). We prove that the notebook's Lagrangian Lg[] is a pure divergence for a Grassmann field, so its Euler-Lagrange equations are empty, and we replace it by a Hermitian first-order Lagrangian. Its covariant field equations $\gamma^\mu D_\mu\Psi=(m+U'(S))\Psi$, $S=\bar\Psi\Psi$, contain the spin connection in every curved field: the connection is pure gauge exactly when the Riemann tensor vanishes, and the squared Dirac operator carries the curvature term $cR$ with the measured constant $c=-1/4$. The energy-momentum tensor operator follows from the metric variation of the action; it is symmetric, Hermitian and conserved on shell, and its on-shell trace is $-mS+7SU'-8U$. In homogeneous diagonal backgrounds the energy density is $\rho=mS+U$ and the pressure is $p=SU'-U$ in all seven transverse directions. We define the kinetic and potential energies in two ways, give the equation of state $w=p/\rho$, and compare everything term by term with the scalar-field formulas $\rho_\phi=\tfrac12\dot\phi^2+V$, $P_\phi=\tfrac12\dot\phi^2-V$ of the reference PDF. Canonical quantization with respect to the time $x_4$ gives the equal-time anticommutator $\{\Psi,\Psi^\dagger\}=i(\sqrt{|g|}\,C\gamma^{x_4})^{-1}\delta^7$ and a Krein structure with fundamental symmetry $J=B=-iC\gamma^4$ of signature (8,8). The sector without momenta along the three extra times has an ordinary Fock space; momenta along the extra times give complex frequencies. Two independent exact implementations, one in WolframScript and one in Python, pass 153 of 153 checks in five reports. Their cross-comparison of 47 algebra and 84 geometry measurements finds no disagreement.

## 1. Scope, claims and non-claims

### 1.1 What is proved

Every numbered result below is backed by named checks in the five Stage-1 reports:

```
artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json
artifacts/dirac16complex/arbitrary-field/python-algebra-report.json
artifacts/dirac16complex/arbitrary-field/python-geometry-report.json
artifacts/dirac16complex/arbitrary-field/grassmann-demo-report.json
```

The check names are quoted in a "checks" block after each result, and Section 11 lists all of them. Numbers are copied from these reports. A statement marked "derived" follows from the checked results by the argument given, but is not itself a machine check.

- **Algebra (exact).** The Clifford relations, the charge matrix, expression [1], the chirality, the representation theory (commutants, intertwiners, invariant forms), the Krein signatures and the subgroup counts are exact integer or Gaussian-rational computations with the actual 16 by 16 matrices. Where a statement depends on parameters (masses and momenta in Section 10), the text says whether it was proved for symbolic values or checked at exact sample values.
- **Geometry (general proof, exact test points).** The statements about an arbitrary gravitational field are proved in this document by general arguments. They are then checked with exact arithmetic in three test geometries (Section 5.7): G1, a generic non-diagonal vielbein at three rational points; G2, the primordial family of Stage 2 (checked by Wolfram at three exact points and by Python at a fully symbolic point); and G3, homogeneous diagonal (Bianchi-I type) frames at three times.
- **Grassmann statements** are checked in genuine Grassmann algebras with up to 1440 odd generators (grassmann-demo-report.json), and the Euler-Lagrange checks of the Wolfram geometry verifier also use a genuine Grassmann algebra.

### 1.2 What is conventional

The following are choices, not results:

- counting from 0;
- the tangent metric $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$, with $x_4$ as the evolution time;
- the split-octonion basis of the notebook as the primary basis;
- the Dirac adjoint $\bar\Psi=\Psi^\dagger C$ with $C=\sigma_{16}$;
- the symmetrized form of the kinetic term and the default potential $U(S)=\tfrac\lambda2S^2$;
- the sign of $T_{\mu\nu}$, fixed so that $T_{44}$ is the energy density;
- the two definitions of kinetic and potential energy in Section 9.5;
- units with $\hbar=1$.

### 1.3 What is not claimed

1. No observational claim is made. The signature (4,4) is not the signature of observed spacetime, and nothing here is fitted to data.
2. The dark-energy and dark-matter questions are not answered in this document. Section 9 supplies the exact energy density, pressures and equation of state that such a study needs; the numerical investigation is separate work.
3. Perturbative stability of the classical field equations is not studied.
4. The quantization is canonical and formal. The state space carries an indefinite (Krein) metric (Section 10.5), the modes with momentum along the extra times have complex frequencies (Section 10.10), and no interacting Fock space or renormalization is constructed.
5. The homogeneous-sector formulas of Section 9.7 treat the bilinears as classical (mean-field) quantities.
6. The pairing of the masses $\pm m$ by the chirality map (Section 7.7) is a structural property of the equations, not a claim that universes of masses $\pm M$ are created in pairs.

## 2. Counting and notation dictionary

### 2.1 Counting and complex vector spaces

As the task prescribes, everything is counted from 0. A complex vector space is a set whose elements can be added and multiplied by complex numbers while satisfying the usual distributive rules. A basis $(e_0,\dots,e_7)$ of an 8-dimensional complex vector space is an ordered list in which every vector $v$ has one and only one expansion $v=v_0e_0+v_1e_1+\dots+v_7e_7$; the coordinate column of $v$ is $(v_0,\dots,v_7)^T$. The dimension counts basis vectors, not the number of vectors: an 8-dimensional complex space contains infinitely many vectors. The spinor space $\mathbb C^{16}$ of dirac16complex is used in the same way, with the basis $(e_0,\dots,e_{15})$ and coordinate columns $(\Psi_0,\dots,\Psi_{15})^T$.

- Coordinates $x=\{x_0,x_1,\dots,x_7\}$; curved indices $\mu,\nu,\rho,\sigma,\lambda=0,\dots,7$; frame indices $a,b,c=0,\dots,7$; spinor indices $0,\dots,15$.
- Roles of the coordinates (from the notebook): $x_0$ is a hidden space direction, $x_1,x_2,x_3$ are ordinary 3-space, $x_4$ is the evolution time, and $x_5,x_6,x_7$ are three extra times. Frame directions 0 to 3 are space-like ($\eta_{aa}=+1$) and 4 to 7 are time-like ($\eta_{aa}=-1$).
- A gamma matrix with a numeric upper index, $\gamma^0,\dots,\gamma^7$, is always the constant frame matrix. Curved gammas carry a Greek index, $\gamma^\mu=e_a{}^\mu\gamma^a$; with a numeric value they are written $\gamma^{x_4}$ and so on. Lowered gammas $\gamma_\mu=g_{\mu\nu}\gamma^\nu$ are curved.
- Mathematica lists are 1-based. A notebook entry such as SAB[[a,b]] with $a,b=1,\dots,8$ is $S^{a-1\,b-1}$ in this document.
- The only other 1-based indices are those of the notebook's 4 by 4 building blocks in Section 3.1, which are labelled as such.

### 2.2 This document, the notebook and dirac-main

The notebook is the file

```
Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb
```

in the repository root (read only, never modified). Cell numbers refer to the cell numbering of the project's text dump of the notebook. dirac-main is the reference implementation of the Clifford and split-octonion pictures (read only).

| This document | Notebook (WolframScript) | dirac-main |
| --- | --- | --- |
| $x_0,\dots,x_7$ | X (cell 61) | $x^0,\dots,x^7$ |
| $\eta_{ab}$ | η4488 | $\eta_{ab}$ |
| frame gamma $\gamma^a$ | (T16^A)[a] | $\gamma^a$ (list below) |
| $\gamma^\mu=e_a{}^\mu\gamma^a$ | (T16^α)[μ] | $\gamma^\mu=e_a{}^\mu\gamma^a$ |
| $C=\sigma_{16}$ | σ16 | $C$ (tensor picture) |
| $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$ | SAB[[a+1,b+1]] | $\Sigma_{ab}=\tfrac14[\gamma_a,\gamma_b]$ |
| $\omega_\mu{}^a{}_b$ | ωmat[[μ+1,a+1,b+1]] | $\omega_\mu{}^a{}_b$ |
| $\omega_{\mu ab}=\eta_{ac}\omega_\mu{}^c{}_b$ | not formed | $\omega_{\mu ab}$ |
| $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$ | (Q1/2) ωmat SAB, see 5.6 | $\tfrac18\omega_{\mu ab}[\gamma^a,\gamma^b]$ |
| $D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi$ | D[Ψ16, X[[μ+1]]] + ... | $D_\mu\psi$ |
| $\Psi$, complex Grassmann | Ψ16, commuting | $\psi$, commuting |
| $\bar\Psi=\Psi^\dagger C$ | Transpose[Ψ16].σ16 | $\bar\psi=\psi^TC$ |
| $\sqrt{\lvert g\rvert}$ | Sqrt[detgg] | $\sqrt{\lvert g\rvert}$ |
| mass $m$ | $-HM$ | none |
| $\Psi_0,\dots,\Psi_7$ | Ψ16upper | image of $P_-$ |
| $\Psi_8,\dots,\Psi_{15}$ | Ψ16lower | image of $P_+$ |

Further notebook names used in Lg[] (Section 6.1): Q1 is the notebook's book-keeping switch for the spin connection (1 switches it on); sg is the list of rules that turns the metric symbols into diagonal functions of $(x_0,x_4)$ (cell 269); detgg is Det[g4488 /. sg] (cell 275); constraintVars is the list of positivity assumptions used by Simplify (cell 73); H and M are the notebook's inverse length and mass.

The notebook's Ψ16 is the column of the 16 functions f16[k], which the notebook treats as real commuting functions of $(x_0,x_4)$. The dirac-main gammas form the ordered list $(\gamma_1^+,\gamma_2^+,\gamma_3^+,\gamma_4^+,\gamma_1^-,\gamma_2^-,\gamma_3^-,\gamma_4^-)$ of Section 3.3, with 1-based labels: $\gamma_k^+$ is the frame matrix $\gamma^{k-1}$ and $\gamma_k^-$ is $\gamma^{k+3}$ ($k=1,\dots,4$), so the evolution-time generator $\gamma^4$ is $\gamma_1^-$.

### 2.3 The scalar-field PDF

The reference on the equation of state is the PDF file whose name begins with "Gmail - w = equation of state parameter" (repository root, read only). It treats a canonical scalar field $\phi$ in four dimensions with metric signature $(+,-,-,-)$ and $\mathcal L_\phi=\tfrac12\partial_\mu\phi\,\partial^\mu\phi-V(\phi)$.

| PDF | This document |
| --- | --- |
| signature $(+,-,-,-)$, time first | signature (4,4), time $x_4$; the PDF metric is $-g$ on the coordinates $x_1,x_2,x_3,x_4$ |
| $\mathcal L_\phi=\tfrac12\partial_\mu\phi\,\partial^\mu\phi-V$ | the same function: $\mathcal L_\phi=-\tfrac12g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi-V$ |
| $T^\mu{}_\nu=\partial^\mu\phi\,\partial_\nu\phi-\delta^\mu{}_\nu\mathcal L_\phi$ | $T_{\mu\nu}=\partial_\mu\phi\,\partial_\nu\phi+g_{\mu\nu}\mathcal L_\phi$ (same covariant components) |
| $\rho_\phi=\tfrac12\dot\phi^2+V$ | $\rho=T_{44}$ |
| $P_\phi=\tfrac12\dot\phi^2-V$ | $p_{(i)}=T^i{}_i$ (no sum), $i\ne4$ |
| $w_\phi=P_\phi/\rho_\phi$ | $w=p/\rho$ |
| KE $=\tfrac12\dot\phi^2$, PE $=V$ | $\mathrm{KE}_L$, $\mathrm{PE}_L$ and $\mathrm{KE}_H$, $\mathrm{PE}_H$ (Section 9.5) |
| $\dot\phi=d\phi/dt$ | $\partial_4=\partial/\partial x_4$ |
| CPL: $w(a)=w_0+w_a(1-a)$ | not used; $a$ is the PDF's scale factor |

In both conventions a homogeneous scalar field has $\rho=\tfrac12\dot\phi^2+V$ and $p=\tfrac12\dot\phi^2-V$. The two metrics differ by an overall sign on the 4-dimensional subspace; the covariant tensor $T_{\mu\nu}$ is the same in both, and the mixed tensor $T^\mu{}_\nu$ changes sign. (These scalar-field formulas are standard and are quoted for comparison; they are not part of the machine checks.)

**Sign hazard in the PDF.** The PDF writes $w(a)=w_0+w_a(1-a)$, so $dw/da=-w_a$. Since $a$ grows with time, "$w$ increases with time" means $w_a<0$, and "$w$ decreases towards $-1$" means $w_a>0$. The PDF's table of thawing and freezing models nevertheless labels thawing ("$w$ starts near $-1$ and increases over time") with $w_a>0$ and freezing ("$w$ starts less negative and approaches $-1$") with $w_a<0$. That is the reverse of what its own formula implies. Wherever thawing or freezing is meant in this project, the formula-consistent signs are used: thawing has $w_a<0$ and freezing has $w_a>0$.

## 3. The Clifford module in the split-octonion and Clifford pictures

### 3.1 The split-octonion (notebook) construction

The notebook builds its gamma matrices from 4 by 4 blocks. With 1-based $p,q\in\{1,2,3,4\}$ and $h\in\{1,2,3\}$,

$$
\begin{aligned}
&Q_a[h]_{pq}=\epsilon_{hpq4},\qquad Q_b[h]_{pq}=\delta_{p4}\delta_{qh}-\delta_{ph}\delta_{q4},\\
&s_4[h]=Q_a[h]-Q_b[h],\qquad t_4[h]=Q_a[h]+Q_b[h],\\
&\tau_0=I_8,\qquad \tau_h=\begin{pmatrix}0&s_4[h]\\ s_4[h]&0\end{pmatrix},\qquad \tau_{7-h}=\begin{pmatrix}0&t_4[h]\\ -t_4[h]&0\end{pmatrix},\\
&\tau_7=\tau_1\tau_2\tau_3\tau_4\tau_5\tau_6,\qquad \sigma=\begin{pmatrix}0&I_4\\ I_4&0\end{pmatrix},\qquad \bar\tau_0=I_8,\qquad \bar\tau_a=\sigma\,\tau_a^T\sigma\quad(a=1,\dots,7),\\
&\gamma^a=\begin{pmatrix}0&\bar\tau_a\\ \tau_a&0\end{pmatrix}\qquad(a=0,\dots,7),
\end{aligned}
$$

where $\epsilon_{hpq4}$ is Mathematica's Signature[{h,p,q,4}]. In the notebook $\gamma^a$ is (T16^A)[a] and $\bar\tau_a$ is OverBar[τ][a].

**Result 3.1.** The $\gamma^a$ are integer matrices with $\{\gamma^a,\gamma^b\}=2\eta^{ab}I_{16}$ for all 64 ordered pairs; $(\gamma^a)^2=+1$ for $a<4$ and $-1$ for $a\ge4$. The matrix $\gamma^a$ is symmetric for $a<4$ and antisymmetric for $a\ge4$.

```
checks
  ALG_clifford, ALG_gammaTransposeSymmetry: wolfram-algebra, python-algebra
  ALG_cliffordRelations: wolfram-geometry, python-geometry
```

**Result 3.2 (faithfulness).** The 256 ordered monomials $\gamma^{a_1}\cdots\gamma^{a_k}$ ($a_1<\dots<a_k$) are linearly independent (rank 256), and the 128 even ones have rank 128. The gammas therefore generate the full matrix algebra, $\mathrm{Cl}(4,4)\cong\mathrm{Mat}_{16}(\mathbb R)$.

```
checks
  ALG_faithful: wolfram-algebra, python-algebra
```

### 3.2 Charge matrix, expression [1] and chirality

The charge (Dirac-adjoint) matrix is the notebook's σ16:

$$
C:=\sigma_{16}=\gamma^0\gamma^1\gamma^2\gamma^3=\begin{pmatrix}-\sigma&0\\ 0&\sigma\end{pmatrix},\qquad C^T=C,\qquad C^2=I_{16}.
$$

**Result 3.3.** $C=\gamma^0\gamma^1\gamma^2\gamma^3=\mathrm{diag}(-\sigma,\sigma)$, $C$ is symmetric with $C^2=1$, its characteristic polynomial is $(x-1)^8(x+1)^8$, and its signature is (8,8).

```
checks
  ALG_chargeMatrix: wolfram-algebra, python-algebra, wolfram-geometry
  ALG_sigma16EqualsGamma0123, ALG_CSymmetricInvolution: python-geometry
```

Expression [1] of the task, verbatim in WolframScript:

```
\[Sigma]16.(T16^A)[#]==-Transpose[\[Sigma]16.(T16^A)[#]]&/@Range[0,7]
```

It states $(C\gamma^a)^T=-C\gamma^a$ for $a=0,\dots,7$.

**Result 3.4 (expression [1]).** Expression [1] evaluates to {True, True, True, True, True, True, True, True}. The Wolfram verifier evaluates it twice: with the package's matrices, and literally, from the 11 verbatim notebook definition cells evaluated in an isolated context (the notebook's Symbolize'd names T16^A and OverBar[τ] are reproduced in two independent ways, and both reproduce the package's $\eta$, $\sigma$, $\tau$, $\bar\tau$, $\gamma^a$ and σ16 exactly).

```
checks
  ALG_expression1: wolfram-algebra, python-algebra
  ALG_expression1CgammaAntisymmetric: python-geometry
```

*Proof.* $(C\gamma^a)^T=(\gamma^a)^TC$. For $a<4$, $\gamma^a$ is symmetric and anticommutes with three of the four factors of $C=\gamma^0\gamma^1\gamma^2\gamma^3$, so $\gamma^aC=-C\gamma^a$. For $a\ge4$, $\gamma^a$ is antisymmetric and anticommutes with all four factors, so $(\gamma^a)^TC=-\gamma^aC=-C\gamma^a$. In both cases $(C\gamma^a)^T=-C\gamma^a$.

**Result 3.5.** With $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$: $(CS^{ab})^T=-CS^{ab}$ for all 64 pairs; $C\{\gamma^c,S^{ab}\}$ is symmetric and $C[\gamma^c,S^{ab}]$ is antisymmetric for all 512 triples; $[S^{ab},\gamma^c]=\eta^{bc}\gamma^a-\eta^{ac}\gamma^b$. The Python algebra checker counts 476 verified identities of this kind.

```
checks
  ALG_spinTransposeProperties: wolfram-algebra, python-algebra
  ALG_CSabAntisymmetric, ALG_CAnticommutatorGammaSSymmetric,
  ALG_CCommutatorGammaSAntisymmetric, ALG_SabGammaCommutator: python-geometry
```

**Result 3.6 (chirality).** $\gamma^8:=\gamma^0\gamma^1\cdots\gamma^7=\mathrm{diag}(-I_8,I_8)$, $(\gamma^8)^2=1$, $\gamma^8$ anticommutes with every $\gamma^a$ and commutes with every $S^{ab}$ and with $C$. The upper components $\Psi_0,\dots,\Psi_7$ (the notebook's Ψ16upper) have chirality $-1$ and the lower components $\Psi_8,\dots,\Psi_{15}$ (Ψ16lower) have chirality $+1$. The chiral projectors are $P_\mp=\tfrac12(1\mp\gamma^8)$.

```
checks
  ALG_chirality: wolfram-algebra, python-algebra
  ALG_chiralityDiag: python-geometry
```

### 3.3 The Clifford picture of dirac-main and the intertwiners

dirac-main builds its gammas from the 2 by 2 matrices

$$
\begin{aligned}
&P=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad N=\begin{pmatrix}0&1\\ -1&0\end{pmatrix},\qquad G=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix},\\
&\hat\gamma_k^{+}=G^{\otimes(k-1)}\otimes P\otimes I_2^{\otimes(4-k)},\qquad \hat\gamma_k^{-}=G^{\otimes(k-1)}\otimes N\otimes I_2^{\otimes(4-k)}\qquad(k=1,2,3,4),
\end{aligned}
$$

ordered $(\hat\gamma_1^+,\dots,\hat\gamma_4^+,\hat\gamma_1^-,\dots,\hat\gamma_4^-)=(\hat\gamma^0,\dots,\hat\gamma^7)$, with charge matrix $C_{\mathrm{dm}}=\hat\gamma^0\hat\gamma^1\hat\gamma^2\hat\gamma^3$ and volume element $G\otimes G\otimes G\otimes G$. Its split-octonion picture uses the Zorn vector-matrix model: a vector $x=(x_0,\dots,x_7)$ is the Zorn matrix $(a,u,v,b)$ with $a=x_0+x_4$, $u_i=x_i+x_{i+4}$, $v_i=-x_i+x_{i+4}$ ($i=1,2,3$) and $b=x_0-x_4$, and

$$
\begin{aligned}
&(a,u,v,b)(c,r,w,d)=\bigl(ac+u\cdot w,\ ar+du-v\times w,\ cv+bw+u\times r,\ v\cdot r+bd\bigr),\\
&\Gamma(x)=\begin{pmatrix}0&L_{\bar x}\\ L_x&0\end{pmatrix},\qquad \Gamma^a=\Gamma(e_a),
\end{aligned}
$$

where $L_x(y)=xy$ and $\bar x=(x_0,-x_1,\dots,-x_7)$.

**Result 3.7 (Clifford picture).** The tensor matrices satisfy the Clifford relations with the same $\eta$ and equal dirac-main's committed cl44-seed generators. The intertwiner equation $\hat\gamma^aK=K\gamma^a$ ($a=0,\dots,7$) has a solution space of dimension exactly 1. Its primitive integer generator K_clifford (first nonzero entry positive, coprime entries) has rank 16, so it is invertible, and it satisfies $K C K^{-1}=C_{\mathrm{dm}}$ and $K\gamma^8K^{-1}=+G\otimes G\otimes G\otimes G$. The notebook's chirality $-1$ block $\Psi_0,\dots,\Psi_7$ maps onto the dirac-main basis indices {1, 2, 4, 7, 8, 11, 13, 14} and the $+1$ block onto {0, 3, 5, 6, 9, 10, 12, 15}. K_clifford is not a signed permutation: its entries are $0,\pm1$ with four nonzero entries per row.

```
checks
  ALG_cliffordPictureIntertwiner: wolfram-algebra, python-algebra
```

```
K_clifford =
[ 0  0  0  0  0  0  0  0  1 -1  0  0  1  1  0  0 ]
[-1  1  0  0  1  1  0  0  0  0  0  0  0  0  0  0 ]
[ 0  0 -1  1  0  0 -1 -1  0  0  0  0  0  0  0  0 ]
[ 0  0  0  0  0  0  0  0  0  0  1 -1  0  0 -1 -1 ]
[ 0  0  1  1  0  0 -1  1  0  0  0  0  0  0  0  0 ]
[ 0  0  0  0  0  0  0  0  0  0 -1 -1  0  0 -1  1 ]
[ 0  0  0  0  0  0  0  0 -1 -1  0  0  1 -1  0  0 ]
[ 1  1  0  0  1 -1  0  0  0  0  0  0  0  0  0  0 ]
[ 1 -1  0  0  1  1  0  0  0  0  0  0  0  0  0  0 ]
[ 0  0  0  0  0  0  0  0 -1  1  0  0  1  1  0  0 ]
[ 0  0  0  0  0  0  0  0  0  0 -1  1  0  0 -1 -1 ]
[ 0  0  1 -1  0  0 -1 -1  0  0  0  0  0  0  0  0 ]
[ 0  0  0  0  0  0  0  0  0  0  1  1  0  0 -1  1 ]
[ 0  0 -1 -1  0  0 -1  1  0  0  0  0  0  0  0  0 ]
[-1 -1  0  0  1 -1  0  0  0  0  0  0  0  0  0  0 ]
[ 0  0  0  0  0  0  0  0  1  1  0  0  1 -1  0  0 ]
```

**Result 3.8 (split-octonion picture).** The Zorn product has the unit $e_0$, satisfies $N(xy)=N(x)N(y)$ for the norm $N(x)=\eta(x,x)$, has conjugation reversing products, and is not associative (the associator of $e_1,e_2,e_4$ is $2e_7$). It has 64 nonzero structure constants and equals dirac-main's split-octonion.json multiplication tensor, and the $\Gamma^a$ equal dirac-main's triality44.json octonion Clifford generators. The intertwiner equation $\gamma^aK=K\Gamma^a$ has a solution space of dimension exactly 1; its primitive generator K_octonion has rank 16 and is block diagonal, $K_{\mathrm{octonion}}=\mathrm{diag}(Q,Q)$ with the matrix $Q$ below, $Q^TQ=2I_8$ and $Q^T\sigma Q=2\eta$. Hence $\tau_a=QL_{e_a}Q^{-1}$ and $\bar\tau_a=QL_{\bar e_a}Q^{-1}$ for every $a$. The notebook's $\tau_a$ equal the octonion multiplications $L_{e_a}$ only for $a=0$, and no signed permutation relates them. Since $Q/\sqrt2$ is orthogonal, the notebook's 8-space basis is a null (light-cone) basis of the split octonions, in which the octonion norm $\eta$ appears as $\sigma/2$. Finally, the product K_clifford K_octonion, made primitive, equals dirac-main's canonicalCliffordIntertwiner.

```
checks
  ALG_octonionPictureIntertwiner: wolfram-algebra, python-algebra
```

```
Q =
[ 1  0  0  0  0  0  0 -1 ]
[ 0  0  0 -1 -1  0  0  0 ]
[ 0  0  1  0  0  1  0  0 ]
[ 0 -1  0  0  0  0  1  0 ]
[ 1  0  0  0  0  0  0  1 ]
[ 0  0  0 -1  1  0  0  0 ]
[ 0  0  1  0  0 -1  0  0 ]
[ 0 -1  0  0  0  0 -1  0 ]
```

**Compatibility.** The three sets of matrices, $\gamma^a$ (notebook), $\hat\gamma^a$ (tensor) and $\Gamma^a$ (octonion), are one Clifford module written in three bases: $\hat\gamma^a=K_{\mathrm{clifford}}\gamma^aK_{\mathrm{clifford}}^{-1}$ and $\Gamma^a=K_{\mathrm{octonion}}^{-1}\gamma^aK_{\mathrm{octonion}}$. Each intertwiner is unique up to a scalar, as Schur's lemma requires for an irreducible module (Section 4.3), and the notebook-to-tensor map sends $C$ to $C_{\mathrm{dm}}$ and the chirality blocks to the chirality blocks. The intertwiners change coordinates only; they do not make the octonion product associative.

### 3.4 Verification record

Both algebra implementations build the matrices independently: the Wolfram package wolfram/Dirac16ComplexAlgebra.wl and the Python module scripts/d16c_exact.py (exact rationals and Gaussian rationals, standard library only). Python writes the exact fixture algebra-fixture.json ($\eta$, $\sigma$, $\tau_a$, $\bar\tau_a$, the gammas of all three pictures, $C$, the chirality, the 28 $S^{ab}$, $B$ and both intertwiners), and the Wolfram verifier compares every fixture matrix with its own construction: 75 of 75 matrices agree by name, none disagree and none is unmatched (ALG_fixtureAgreement in wolfram-algebra-report.json). In the other direction, the Python checker reads the Wolfram report and requires the same K_clifford, K_octonion and chirality, the same verdict for all 20 check names both reports contain, and agreement of 47 shared measurements; all 47 agree (ALG_wolframAgreement in python-algebra-report.json).

## 4. Definition of dirac16complex

### 4.1 The field

**Definition.** dirac16complex is the field

$$
\Psi=(\Psi_0,\Psi_1,\dots,\Psi_{15})^T,
$$

whose components are complex-valued Grassmann-odd (anticommuting) fields on an 8-dimensional manifold $M$ with a metric of signature (4,4):

$$
\begin{aligned}
&\Psi_a\Psi_b=-\Psi_b\Psi_a,\qquad \Psi_a\Psi_b^\ast=-\Psi_b^\ast\Psi_a,\qquad \Psi_a^\ast\Psi_b^\ast=-\Psi_b^\ast\Psi_a^\ast,\\
&(\theta_1\theta_2)^\ast=\theta_2^\ast\theta_1^\ast .
\end{aligned}
$$

Complex conjugation is an involution of the Grassmann algebra that reverses the order of products. We write $\Psi^\dagger=(\Psi^\ast)^T$ and $\bar\Psi=\Psi^\dagger C$. The components transform under Pin(4,4) through the Clifford module of Section 3 (Section 4.2); for the determinant-1 transformations, Spin(4,4), the module splits into the two chirality blocks (Section 4.4). The conjugation rules, including the product rule and the involution property, are checked in an explicit Grassmann algebra (GR_conjugationRules).

### 4.2 The action of Pin(4,4) and the two lifts

Pin(4,4) is the group generated, inside $\mathrm{Cl}(4,4)$, by the unit vectors $u=u_a\gamma^a$ with $n(u):=\eta(u,u)=\pm1$, so that $u^2=n(u)$. It acts on dirac16complex by Clifford multiplication, $\rho(u)\Psi=u\Psi$. Spin(4,4) is the subgroup of products of an even number of unit vectors. Pin(4,4) is the double cover of the orthogonal group O(4,4) and Spin(4,4) is the double cover of SO(4,4). Vectors transform by the twisted adjoint action $v\mapsto\alpha(g)vg^{-1}$, where $\alpha$ is the parity automorphism; a unit vector $u$ then acts as the reflection in the hyperplane orthogonal to $u$, and the kernel is $\{\pm1\}$ (standard facts, not machine-checked). The untwisted adjoint action $v\mapsto gvg^{-1}$ gives, for a unit vector, minus that reflection. Because $-1_8$ lies in the identity component $SO_0(4,4)$ (it is the product of rotations by $\pi$ in the planes $(0,1)$, $(2,3)$, $(4,5)$ and $(6,7)$), the untwisted action also maps Pin(4,4) onto O(4,4). For every tested unit vector the untwisted matrix is exactly in O(4,4) (ALG_pinLiftCharacter). The choice of lift matters for the sign characters of Section 7.7.

### 4.3 Irreducibility under Pin(4,4)

**Theorem 4.1.** $\mathbb C^{16}$, with Pin(4,4) acting through the gamma matrices, is an irreducible complex representation of Pin(4,4).

*Proof.* Every monomial $\gamma^{a_1}\cdots\gamma^{a_k}$ is, up to sign, a product of unit vectors, so the linear span of Pin(4,4) is the span of the 256 monomials. By Result 3.2 these are linearly independent, so they span $\mathrm{Mat}_{16}(\mathbb R)$, and over $\mathbb C$ they span $\mathrm{Mat}_{16}(\mathbb C)$. A subspace of $\mathbb C^{16}$ invariant under Pin(4,4) is invariant under all of $\mathrm{Mat}_{16}(\mathbb C)$, hence it is $0$ or $\mathbb C^{16}$. Equivalently (Schur's lemma), the commutant $\{X:X\gamma^a=\gamma^aX\ \forall a\}$ consists of the scalars.

**Result 4.1.** The commutant of the eight gammas on $\mathbb C^{16}$ has dimension exactly 1 and consists of the scalar matrices. The dimension is computed over $\mathbb Q$; the coefficient matrix of the equations is rational, so its rank, and hence the solution dimension, is the same over $\mathbb C$.

```
checks
  ALG_pinIrreducibleComplex, ALG_faithful: wolfram-algebra, python-algebra
```

### 4.4 Two inequivalent 8-dimensional modules under Spin(4,4)

**Theorem 4.2.** Under Spin(4,4), $\mathbb C^{16}=\mathbb C^8_-\oplus\mathbb C^8_+$ (the images of $P_-$ and $P_+$), and the two summands are irreducible and inequivalent.

*Proof.* Spin(4,4) is generated by even elements, and every even element commutes with $\gamma^8$, so the two chirality blocks are invariant. The even monomials restricted to each block span an algebra of rank 64 $=\dim\mathrm{End}(\mathbb C^8)$, so each block is irreducible, and each block's commutant is one-dimensional. If the two blocks were equivalent, the commutant on $\mathbb C^{16}$ would be $\mathrm{Mat}_2(\mathbb C)$, of dimension 4. It has dimension 2, spanned by $P_-$ and $P_+$, and the intertwiners between the blocks form the zero space in both directions, so the blocks are inequivalent.

**Result 4.2.** The commutant of the 28 spin generators $S^{ab}$ has dimension 2 and is spanned by $P_-$ and $P_+$; every $S^{ab}$ and every even monomial is block diagonal; the block commutants have dimensions (1, 1); the even-algebra ranks on the blocks are (64, 64); the cross-intertwiner dimensions are (0, 0).

```
checks
  ALG_spinDecomposition: wolfram-algebra, python-algebra
```

The same statements hold for the identity component, which is generated by the $\exp(\theta S^{ab})$, and for the full group, whose elements lie in the even algebra.

### 4.5 The spinor bundle

On a manifold with a spin structure $P_{\mathrm{Spin}}(M)$ for the (4,4) frame bundle (assumed to exist), dirac16complex is a section, with values in the odd part of a complex Grassmann algebra, of the bundle

$$
S_{\mathbb C}=P_{\mathrm{Spin}}(M)\times_\rho(\mathbb C\otimes\Delta_{\mathbb R}),\qquad \Delta_{\mathbb R}=\Delta_-\oplus\Delta_+,
$$

where $\Delta_{\mathbb R}\cong\mathbb R^{16}$ is the real module on which the real gammas act and $\Delta_\mp$ are its chirality halves. The spin connection of Section 5 preserves $\Delta_-$ and $\Delta_+$ because every $\Omega_\mu$ is even.

## 5. Canonical spin connection and covariant derivative

### 5.1 Vielbein, metric and Christoffel symbols

The gravitational field is a vielbein $e_\mu{}^a(x)$ (row index $\mu$) with inverse $e_a{}^\mu$:

$$
\begin{aligned}
&g_{\mu\nu}=e_\mu{}^a\eta_{ab}e_\nu{}^b,\qquad \gamma^\mu=e_a{}^\mu\gamma^a,\qquad \{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu},\\
&\Gamma^\rho{}_{\mu\nu}=\tfrac12g^{\rho\sigma}\bigl(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\mu\sigma}-\partial_\sigma g_{\mu\nu}\bigr).
\end{aligned}
$$

The Christoffel symbols are those of the torsion-free metric-compatible (Levi-Civita) connection.

### 5.2 The vielbein postulate and the canonical spin connection

The canonical spin connection is defined by the vielbein postulate: the total covariant derivative of the vielbein, built with the Christoffel symbols on the curved index and the spin connection on the frame index, is zero,

$$
\nabla_\mu e_\nu{}^a:=\partial_\mu e_\nu{}^a-\Gamma^\rho{}_{\mu\nu}e_\rho{}^a+\omega_\mu{}^a{}_b\,e_\nu{}^b=0 .
$$

Multiplying by the inverse vielbein solves it uniquely:

$$
\omega_\mu{}^a{}_b=e_b{}^\nu\bigl(\Gamma^\rho{}_{\mu\nu}e_\rho{}^a-\partial_\mu e_\nu{}^a\bigr),\qquad \omega_{\mu ab}:=\eta_{ac}\,\omega_\mu{}^c{}_b=-\omega_{\mu ba}.
$$

The antisymmetry in $(a,b)$ follows from metric compatibility.

**Result 5.1.** In every test geometry all $8\cdot8\cdot8=512$ components of the vielbein postulate vanish together with their 4096 first derivatives, and $\omega_{\mu ab}=-\omega_{\mu ba}$. The Python checker computes $\omega$ by two routes, from the Christoffel symbols and from the anholonomy coefficients, and they agree. The number of nonzero $\omega_{\mu ab}$ is 448 at each G1 point and 24 in G2.

```
checks
  GEO_vielbeinPostulate_G1, GEO_vielbeinPostulate_G2,
  GEO_omegaAntisymmetry_G1, GEO_omegaAntisymmetry_G2: wolfram-geometry, python-geometry
```

### 5.3 Spinor connection and covariant derivatives

$$
\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}=\tfrac18\omega_{\mu ab}[\gamma^a,\gamma^b],\qquad D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi,\qquad D_\mu\bar\Psi=\partial_\mu\bar\Psi-\bar\Psi\,\Omega_\mu .
$$

The sums run over all ordered pairs $(a,b)$; with a sum over $a<b$ only, the coefficient of $[\gamma^a,\gamma^b]$ is $\tfrac14$. The rule for $\bar\Psi$ follows from $\Psi^\dagger\Omega_\mu^\dagger C=-\bar\Psi\,\Omega_\mu$, which holds because $S^{ab}$ is real and $(S^{ab})^TC=-CS^{ab}$ (Result 3.5).

### 5.4 Covariant constancy of the gammas and the divergence identity

**Result 5.2.** The curved gammas are covariantly constant,

$$
D_\mu\gamma^\nu:=\partial_\mu\gamma^\nu+\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda+[\Omega_\mu,\gamma^\nu]=0,
$$

in all 64 pairs $(\mu,\nu)$ of every test geometry. This identity is equivalent to the vielbein postulate, since $[\Omega_\mu,\gamma^b]=-\omega_\mu{}^b{}_c\gamma^c$ by Result 3.5.

```
checks
  GEO_gammaCovariantConstancy_G1,
  GEO_gammaCovariantConstancy_G2: wolfram-geometry, python-geometry
```

**Result 5.3 (divergence identity).** Contracting $D_\mu\gamma^\mu=0$ and using $\partial_\mu\sqrt{|g|}=\sqrt{|g|}\,\Gamma^\rho{}_{\rho\mu}$ gives

$$
\partial_\mu\bigl(\sqrt{|g|}\,\gamma^\mu\bigr)=\sqrt{|g|}\,[\gamma^\mu,\Omega_\mu],
$$

which holds exactly in every test geometry; the Wolfram check also verifies $\partial_\mu\sqrt{|g|}=\sqrt{|g|}\,\Gamma^\rho{}_{\rho\mu}$. This identity is used twice: in the proof that Lg[] is empty (Section 6) and in the derivation of the field equations (Section 8).

```
checks
  GEO_divergenceIdentity_G1, GEO_divergenceIdentity_G2: wolfram-geometry, python-geometry
```

### 5.5 Local spin transformations and curvature

Under a local spin transformation $R(x)$,

$$
\Psi\to R\Psi,\qquad \Omega_\mu\to R\,\Omega_\mu R^{-1}-(\partial_\mu R)R^{-1},\qquad D_\mu\Psi\to R\,D_\mu\Psi .
$$

**Result 5.4.** For a finite local transformation $R=\gamma(n)\gamma(m)$, $\gamma(n):=n_a\gamma^a$, built from exact rational unit vector fields $n(x)$ and $m(x)$, recomputing $\Omega$ from the rotated frame gives exactly $\Omega'=R\Omega R^{-1}-(\partial R)R^{-1}$, $\gamma'^\mu=R\gamma^\mu R^{-1}$ and an unchanged metric; for $\eta(n,n)\,\eta(m,m)=+1$ the Lagrangian of Section 7 is unchanged (value and first derivatives). A first-order check with exact dual numbers ($\kappa^2=0$) gives zero first-order change of the Lagrangian.

```
checks
  LAG_localSpinInvariance_G1, LAG_localSpinInvariance_G2: wolfram-geometry
```

The curvature of the spinor connection is

$$
\begin{aligned}
&F_{\mu\nu}=\partial_\mu\Omega_\nu-\partial_\nu\Omega_\mu+[\Omega_\mu,\Omega_\nu]=+\tfrac12R_{ab\mu\nu}S^{ab},\\
&R_{ab\mu\nu}:=\eta_{ac}\,e_\rho{}^c R^\rho{}_{\sigma\mu\nu}e_b{}^\sigma,
\end{aligned}
$$

with $R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$, Ricci tensor $R_{\sigma\nu}=R^\rho{}_{\sigma\rho\nu}$ and scalar curvature $R=g^{\sigma\nu}R_{\sigma\nu}$.

**Result 5.5.** The form with $+\tfrac12$ holds at all six Wolfram points and at the Python points; the form with $-\tfrac12$ and the form without $\eta$ (mixed indices) fail. The frame curvature equals the Riemann tensor and the Ricci tensor is symmetric.

```
checks
  GEO_curvature_G1, GEO_curvature_G2: wolfram-geometry, python-geometry
```

### 5.6 The notebook contraction and why it is wrong

The notebook's ωmat[[μ,a,b]] is the mixed connection $\omega_\mu{}^a{}_b$, and Lg[] contracts it with SAB[[a,b]] $=S^{ab}$ (both indices up):

$$
\Omega^{\mathrm{nb}}_\mu=\tfrac12\,\omega_\mu{}^a{}_b\,S^{ab}\qquad\text{(one }\eta\text{ is missing).}
$$

Since $\omega_\mu{}^a{}_b=\eta^{aa}\omega_{\mu ab}$ (no sum), the mixed components are symmetric in $(a,b)$ whenever $\eta^{aa}=-\eta^{bb}$, that is for every space-time (boost) pair, and the antisymmetric $S^{ab}$ deletes them. For time-time pairs ($a,b\ge4$) the sign is reversed. So $\Omega^{\mathrm{nb}}_\mu$ equals the space-space part of $\Omega_\mu$ minus its time-time part, and has no boost part (derived from the index placement).

**Result 5.6.** With the notebook contraction the gammas are not covariantly constant: $D_\mu\gamma^\nu\ne0$ in all 64 pairs $(\mu,\nu)$ at every G1 point, with 4096 nonzero matrix entries, and in 15 pairs with 288 nonzero entries in G2. The largest violation $\max|D_\mu\gamma^\nu|$ is $2/3$, $1/5$ and $9/5$ at the three G2 points and approximately 1.46822, 1.52979 and 1.68937 at the three G1 points. The symmetric part of $\omega_\mu{}^a{}_b$ that the contraction deletes has 256 nonzero entries at each G1 point and 12 in G2. In the primordial field the notebook contraction gives $\gamma^\mu\Omega^{\mathrm{nb}}_\mu=\tfrac{3H}2(\gamma^0+a_4'\gamma^4)$ instead of the correct $3H\gamma^0$, and it breaks local spin invariance already at first order. Replacing $\Omega$ by $\Omega^{\mathrm{nb}}$ makes all eleven connection-sensitive G2 checks fail.

```
checks
  GEO_notebookContractionFails_G1,
  GEO_notebookContractionFails_G2: wolfram-geometry, python-geometry
  NEG_notebookConnectionDetected_G2: wolfram-geometry
```

### 5.7 Test geometries

**G1** is a generic non-diagonal vielbein,

$$
\begin{aligned}
&e_\mu{}^a=\delta_\mu{}^a+P_\mu{}^a(x),\qquad P_\mu{}^a=\tfrac1{10}\bigl((\mu+1)x_a-(a+1)x_\mu\bigr)+\tfrac1{20}x_\mu x_a+\tfrac1{30}x_{(\mu+a)\bmod8}^2\quad(\mu\ne a),\\
&P_\mu{}^\mu=\tfrac1{10}x_\mu^2+\tfrac1{40}x_{(\mu+1)\bmod8},
\end{aligned}
$$

evaluated at three rational points:

```
p1 = (1/7, -2/9, 1/5, 3/11, -1/13, 2/17, -3/19, 1/23)
p2 = (-1/3, 1/4, 2/7, -1/5, 1/6, -2/11, 1/9, 3/13)
p3 = (2/9, 1/8, -1/7, 1/10, -3/14, 1/12, 2/15, -1/16)
```

At each point $\det e$ is an exact positive rational (approximately 1.49738, 1.85501 and 1.37123), the metric has inertia (4, 4, 0), $g^{44}\ne0$, and the scalar curvature is approximately $-2.42693$, $13.2081$ and $36.6612$. The exact rationals are in the reports, and the two implementations agree on them exactly (Section 11.6).

```
checks
  GEO_frameNondegenerate_G1: wolfram-geometry, python-geometry
  GEO_sqrtgSquaredEqualsDetg_G1: python-geometry
```

**G2** is the primordial field of Stage 2 with an arbitrary function $a_4$:

$$
e_\mu{}^a=\mathrm{diag}\bigl(\cot z,\ s^{1/6}e^{a_4}\ (\times3),\ 1,\ s^{1/6}e^{-a_4}\ (\times3)\bigr),\qquad z=6Hx_0,\quad t=Hx_4,\quad s=\sin z .
$$

Wolfram evaluates it at three exact points; Python keeps $\sin^{1/6}z$, $\cos z$, $e^{a_4}$, $a_4'$, $a_4''$, $a_4'''$ and $H$ as symbols. The results are $\sqrt{|g|}=\cos z$, $R=6H^2(a_4'^2-7)$ (at the three Wolfram points $R$ = $-2672/147$, $-1102/675$ and $-834/49$) and $\gamma^\mu\Omega_\mu=3H\gamma^0$.

```
checks
  GEO_primordialInvariants_G2, GEO_diagonalSlashFormula_G2: wolfram-geometry,
      python-geometry
  GEO_symbolicJetAgreement_G2, GEO_frameNondegenerate_G2: wolfram-geometry
  GEO_sqrtgSquaredEqualsDetg_G2: python-geometry
```

**G3** is a homogeneous diagonal frame, $ds^2=-N^2dx_4^2+\sum_{i\ne4}\eta_{ii}h_i^2dx_i^2$, evaluated at $N=1$, $h_i=1+x_4^2/(i+2)$ and $x_4\in\{1/3,-2/5,3/7\}$. Fully symbolic diagonal frames are used for the metric variation (Section 9.1).

Field data at each point (the values of $\Psi$, $\Psi^\dagger$ and their first and second derivatives) are independent exact random rationals from recorded seeds: a documented 64-bit linear congruential generator in Wolfram, recorded seeds in Python. The Wolfram parameters are $m\in\{3/7,-2/5,5/9\}$ and $\lambda\in\{5/11,7/13,-3/8\}$ at p1, p2, p3.

## 6. Why the notebook Lagrangian Lg[] is empty for a Grassmann field

### 6.1 The notebook Lagrangian, verbatim

The task quotes the notebook's Lagrangian as expression [2]. Verbatim in WolframScript (the line breaks are inserted only for the page width; joining the lines without any separator gives the expression character for character):

```
Lg[]:=Sqrt[detgg] *( Transpose[\[CapitalPsi]16].\[Sigma]16.
Sum[FullSimplify[((T16^\[Alpha])[\[Alpha]1-1]/.sg),constraintVars].
(D[ \[CapitalPsi]16,X[[\[Alpha]1]]]+(Q1/2)*Sum[\[Omega]mat[[\[Alpha]1,a,b]]*SAB[[a,
b]].\[CapitalPsi]16,{a,1,8},{b,1,8}]),{\[Alpha]1,1,Length[X]}]+
(H*M)*Transpose[\[CapitalPsi]16].\[Sigma]16.\[CapitalPsi]16)//Simplify[#,
constraintVars]&
```

This is the definition in notebook cell 1064 (In[1034]); its InputForm there reads Lg[] := (Simplify[#1, constraintVars] &)[Sqrt[detgg]*(...)], and both forms parse to the identical held expression in WolframScript 1.14 (a one-off comparison made while writing this document, not one of the recorded checks). In the notation of this document, with Q1 = 1 and $m=-HM$,

$$
\mathrm{Lg}=\sqrt{|g|}\,\Bigl[\Psi^T C\gamma^\mu\bigl(\partial_\mu\Psi+\Omega^{\mathrm{nb}}_\mu\Psi\bigr)-m\,\Psi^T C\Psi\Bigr],
$$

where the notebook's Ψ16 is a real 16-component column and (T16^α)[μ] is the curved gamma $\gamma^\mu$. The notebook treats the components f16[k] as commuting functions. For a fermion they must anticommute, and then Lg[] carries no dynamics at all.

### 6.2 Lemmas

Let $\Psi$ be a real 16-component column of Grassmann-odd fields.

**Lemma 6.1.** For every matrix $M$, $\Psi^TM\Psi=\Psi^TM_A\Psi$ with $M_A=\tfrac12(M-M^T)$. In particular $\Psi^TC\Psi\equiv0$, because $C$ is symmetric.

*Proof.* $\Psi^TM\Psi=\sum_{ab}\Psi_aM_{ab}\Psi_b=-\sum_{ab}\Psi_bM_{ab}\Psi_a=-\Psi^TM^T\Psi$, so the symmetric part drops out.

**Lemma 6.2.** For an antisymmetric matrix function $A(x)$, $\Psi^TA\,\partial_\mu\Psi=\tfrac12\partial_\mu(\Psi^TA\Psi)-\tfrac12\Psi^T(\partial_\mu A)\Psi$.

*Proof.* $\partial_\mu\Psi^T A\Psi=-\Psi^TA^T\partial_\mu\Psi=\Psi^TA\,\partial_\mu\Psi$ by the anticommutation of the components and $A^T=-A$; the product rule gives the claim.

**Lemma 6.3.** $C\gamma^cS^{ab}=\tfrac12C\{\gamma^c,S^{ab}\}+\tfrac12C[\gamma^c,S^{ab}]$, where the first term is symmetric and the second antisymmetric (Result 3.5). Hence $\Psi^TC\gamma^\mu\Omega_\mu\Psi=\tfrac12\Psi^TC[\gamma^\mu,\Omega_\mu]\Psi$.

### 6.3 Theorem

**Theorem 6.1.** For a real Grassmann-odd $\Psi$ and the canonical spin connection, Lg[] (which already contains the factor Sqrt[detgg]) is a pure divergence,

$$
\mathrm{Lg}=\partial_\mu V^\mu,\qquad V^\mu=\tfrac12\sqrt{|g|}\,\Psi^TC\gamma^\mu\Psi,
$$

so its Euler-Lagrange operator vanishes identically: the field equations are $0=0$.

*Proof.* The mass term vanishes by Lemma 6.1. With $A^\mu=\sqrt{|g|}\,C\gamma^\mu$, which is antisymmetric by expression [1], Lemma 6.2 gives $\sqrt{|g|}\,\Psi^TC\gamma^\mu\partial_\mu\Psi=\tfrac12\partial_\mu(\Psi^TA^\mu\Psi)-\tfrac12\Psi^TC\,\partial_\mu(\sqrt{|g|}\gamma^\mu)\Psi$. By Lemma 6.3 and the divergence identity (Result 5.3) the connection term is $\sqrt{|g|}\,\Psi^TC\gamma^\mu\Omega_\mu\Psi=\tfrac12\Psi^TC\,\partial_\mu(\sqrt{|g|}\gamma^\mu)\Psi$, which cancels the second term exactly. The Euler-Lagrange operator of a total divergence is identically zero.

With the notebook's own contraction $\Omega^{\mathrm{nb}}$ in place of $\Omega$ the cancellation fails, but what remains has no derivatives: the Euler-Lagrange equations become the algebraic equations $X\Psi=0$ with $X=\sqrt{|g|}\,C\sum_\alpha[\gamma^\alpha,\Omega^{\mathrm{nb}}_\alpha-\Omega_\alpha]$. Either way Lg[] gives no wave equation for a Grassmann field.

### 6.4 Machine verification

**Result 6.1.** In a genuine Grassmann algebra (real $\Psi$ and its jets as odd generators; 720 generators in the Python jet space):

1. $\Psi^TC\Psi$ has 0 monomials, while each $\Psi^TC\gamma^a\Psi$ has 8 monomials with coefficients $\pm2$; for a random integer matrix only the antisymmetric part survives.
2. $\Psi^TA\,\partial_\mu\Psi=\tfrac12\partial_\mu(\Psi^TA\Psi)$ for each constant $C\gamma^a$ and a random antisymmetric matrix, with identically vanishing Euler-Lagrange expression; with the symmetric $C$ instead, the kinetic term does not reduce and its Euler-Lagrange expression is $2(C\partial_0\Psi)_0\ne0$.
3. For Lg[] itself in curved space (G1 at p1 and the symbolic G2): with the canonical $\Omega$, 0 of the 16 Euler-Lagrange components are nonzero, and Lg[] equals $\partial_\mu V^\mu$ exactly. With the notebook contraction all 16 components are nonzero, contain no derivative, and equal $X\Psi$ with the $X$ above.
4. The Wolfram geometry verifier repeats the computation at all six G1 and G2 points in its own Grassmann algebra: the Euler-Lagrange operator vanishes identically with the canonical $\Omega$; with the notebook contraction it is $X\Psi$ with $X$ of rank 16, $\max|X|$ approximately 9.927, 12.36 and 10.72 at the G1 points and $3\sqrt{455}/32\approx1.99976$ at the first G2 point.

```
checks
  GR_massTermVanishesReal, GR_bilinearOnlyAntisymmetricPartSurvives: grassmann-demo
  ALG_grassmannLemmas: wolfram-geometry
  GR_kineticTotalDerivativeReal, GR_kineticSymmetricMatrixContrast: grassmann-demo
  GR_notebookLgELTrivial, GR_notebookLgPureDivergence: grassmann-demo
  LAG_notebookLgGrassmannTrivial_G1, LAG_notebookLgGrassmannTrivial_G2: wolfram-geometry
```

Since $X$ has rank 16 at every tested point, the equations $X\Psi=0$ admit only $\Psi=0$ there.

### 6.5 Remark on commuting fields

For commuting components (the notebook's actual use) Lemma 6.1 is reversed: only the symmetric part of a bilinear survives. The mass term $\Psi^TC\Psi$ then survives, and from the connection term only $\tfrac12C\{\gamma^\mu,\Omega_\mu\}$ survives; it contains only the totally antisymmetric part $\omega_{[cab]}$ of the connection, which vanishes for every diagonal vielbein (for G2, $\sum_\mu\{\gamma^\mu,\Omega_\mu\}=0$ for both contractions: GEO_anticommutatorGammaOmegaVanishesDiagonal_G2). In the notebook's diagonal fields the gravitational term in its Euler-Lagrange equations therefore comes from $\partial_\mu(\sqrt{|g|}\gamma^\mu)$, not from the spin connection. This remark is derived from the lemmas; it is not a separate machine check.

## 7. The dirac16complex Lagrangian

### 7.1 Formula

The Lagrangian density of dirac16complex in an arbitrary gravitational field is

$$
\begin{aligned}
&\mathcal L=\sqrt{|g|}\,\Bigl[\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)-m\,\bar\Psi\Psi-U(\bar\Psi\Psi)\Bigr],\\
&\bar\Psi=\Psi^\dagger C,\qquad U(S)=\tfrac\lambda2S^2 .
\end{aligned}
$$

We write $S=\bar\Psi\Psi$, $\mathcal L_s=\mathcal L/\sqrt{|g|}$ and $M_{\mathrm{eff}}=m+U'(S)$, and $K=\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)$ for the kinetic term.

### 7.2 WolframScript form in the notebook's variable names

The same Lagrangian, written with the notebook's variable names (1-based lists, as in Lg[]):

```
(* dirac16complex Lagrangian density in the notebook's variable names.     *)
(* Lists are 1-based as in the notebook: SAB[[a,b]] is S^(a-1,b-1).        *)
\[CapitalPsi]16 = (f16[#] @@ X &) /@ Range[0, 15];   (* all eight coordinates *)
(* lowered spin connection omega_{mu ab} = eta_{ac} omega_mu^c_b *)
\[Omega]low = Table[Sum[\[Eta]4488[[a, c]] \[Omega]mat[[\[Alpha]1, c, b]], {c, 1, 8}],
   {\[Alpha]1, 1, 8}, {a, 1, 8}, {b, 1, 8}];
\[CapitalOmega]16[\[Alpha]1_] := (1/2) Sum[\[Omega]low[[\[Alpha]1, a, b]] SAB[[a, b]],
   {a, 1, 8}, {b, 1, 8}];
\[CapitalPsi]16bar = ConjugateTranspose[\[CapitalPsi]16].\[Sigma]16;
D\[CapitalPsi]16[\[Alpha]1_] := D[\[CapitalPsi]16, X[[\[Alpha]1]]] +
   \[CapitalOmega]16[\[Alpha]1].\[CapitalPsi]16;
D\[CapitalPsi]16bar[\[Alpha]1_] := D[\[CapitalPsi]16bar, X[[\[Alpha]1]]] -
   \[CapitalPsi]16bar.\[CapitalOmega]16[\[Alpha]1];
S16 = \[CapitalPsi]16bar.\[CapitalPsi]16;               (* S = Psibar Psi *)
U[s_] := (\[Lambda]/2) s^2;                             (* default potential *)
m = -H*M;                                               (* mass, m = -H M *)
Ldirac16complex[] := Sqrt[Abs[detgg]]*(
   (1/2) Sum[
      \[CapitalPsi]16bar.(T16^\[Alpha])[\[Alpha]1 - 1].D\[CapitalPsi]16[\[Alpha]1] -
      D\[CapitalPsi]16bar[\[Alpha]1].(T16^\[Alpha])[\[Alpha]1 - 1].\[CapitalPsi]16,
      {\[Alpha]1, 1, Length[X]}] -
   m S16 - U[S16])
```

The field depends on all eight coordinates, so Ψ16 is redefined accordingly, and the curved gammas (T16^α)[μ] are those of the arbitrary vielbein (no /.sg specialization). Mathematica's Times and Dot treat these symbols as commuting, so this code is a transcription that keeps every $\bar\Psi$ factor to the left of every $\Psi$ factor; it is not executed as a Grassmann computation. The verified implementation is wolfram/Dirac16ComplexGeometry.wl, which carries its own exact Grassmann algebra (convention.grassmann in wolfram-geometry-report.json).

### 7.3 Relation to Lg[], term by term

| Lg[] | dirac16complex |
| --- | --- |
| Transpose[Ψ16] | ConjugateTranspose[Ψ16] |
| real commuting $\Psi$ | complex Grassmann $\Psi$ |
| Transpose[Ψ16].σ16 | $\bar\Psi=\Psi^\dagger C$, the same $C=\sigma_{16}$ |
| unsymmetrized $\Psi^TC\gamma^\mu D_\mu\Psi$ | symmetrized $\tfrac12(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi)$ |
| ωmat, mixed $\omega_\mu{}^a{}_b$ | ωlow, lowered $\omega_{\mu ab}=\eta_{ac}\omega_\mu{}^c{}_b$ |
| (Q1/2) with a switch Q1 | the fixed factor $\tfrac12$ of $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$ |
| Sqrt[detgg] | Sqrt[Abs[detgg]] |
| +(H M) Transpose[Ψ16].σ16.Ψ16 | $-m\bar\Psi\Psi$ with $m=-HM$ (same sign) |
| no self-interaction | $-U(\bar\Psi\Psi)$, $U=\tfrac\lambda2S^2$ |

### 7.4 Hermiticity

No factor $i$ is needed. $C$ is real symmetric and $C\gamma^a$ is real antisymmetric (expression [1]), hence anti-Hermitian, and with the conjugation rule $(\theta_1\theta_2)^\ast=\theta_2^\ast\theta_1^\ast$ the symmetrized kinetic term is Hermitian. $S=\bar\Psi\Psi$ is Hermitian.

**Result 7.1.** $(C\gamma^a)^\dagger=-C\gamma^a$ and $C^\dagger=C$; at the coefficient level the Lagrangian has the form $\bar\Psi K_0\Psi+\bar\Psi K^\mu\partial_\mu\Psi+\partial_\mu\bar\Psi L^\mu\Psi$ with $K_0=K_0^\dagger$ and $L^\mu=(K^\mu)^\dagger$. In the Grassmann algebra $\mathcal L^\ast=\mathcal L$ exactly, and $S$ is Hermitian with 16 monomials. As a negative control, the unsymmetrized kinetic term $\bar\Psi\gamma^\mu D_\mu\Psi$ alone is not Hermitian.

```
checks
  LAG_hermiticity_G1, LAG_hermiticity_G2: wolfram-geometry
  GR_lagrangianHermitian, GR_scalarBilinearHermitian,
  GR_unsymmetrizedKineticNotHermitian: grassmann-demo
```

### 7.5 Symmetries

- **Local spin transformations.** $\mathcal L$ is invariant under every local $R(x)$ of spinor norm $+1$, in particular under the identity component $\mathrm{Spin}_0(4,4)$ (derived from $R^TCR=C$ and the transformation law of $\Omega_\mu$; tested in Result 5.4 for finite products of two unit vector fields and infinitesimally). Elements of spinor norm $-1$ are treated in Section 7.7.
- **Diffeomorphisms.** $\mathcal L$ is a scalar density by construction (not a separate check).
- **U(1).** $\Psi\to e^{i\alpha}\Psi$ leaves $\mathcal L$ invariant. The Noether current $J^\mu=-i\bar\Psi\gamma^\mu\Psi$ is Hermitian (GR_currentHermitian; QNT_currentHermiticity) and is conserved on shell (derived from the field equations of Section 8).

### 7.6 The potential: polynomials only

$S=\bar\Psi\Psi$ is even, of Grassmann degree 2. At a point the algebra is generated by 32 odd elements ($\Psi_a$ and $\Psi_a^\ast$), so $S^{17}=0$ and every function of $S$ is a polynomial of degree at most 16. We require $U(0)=U'(0)=0$: no constant term (no cosmological constant) and no second mass term. The default $U=\tfrac\lambda2S^2$ is a four-fermion contact interaction.

**Result 7.2.** $(\bar\Psi\Psi)^k$ has $\binom{16}{k}$ nonzero monomials with coefficients of absolute value $k!$ for $k=1,\dots,16$, namely 16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440, 8008, 4368, 1820, 560, 120, 16 and 1, and $(\bar\Psi\Psi)^{17}=0$. The Grassmann derivatives of the quartic term are $\partial(\tfrac\lambda2S^2)/\partial\Psi^\dagger_a=\lambda S(C\Psi)_a$ (left derivative) and $\lambda S\bar\Psi_a$ (right derivative with respect to $\Psi_a$), and $S$ commutes with $\Psi$.

```
checks
  GR_quarticTermPolynomial: grassmann-demo
  ALG_grassmannLemmas: wolfram-geometry
```

### 7.7 Discrete maps: the chirality map and the Pin characters

**Chirality map.** Under $\Psi\to\gamma^8\Psi$ one has $\bar\Psi\to\bar\Psi\gamma^8$ (because $(\gamma^8)^TC=C\gamma^8$), $\gamma^8$ commutes with $D_\mu$, every kinetic matrix changes sign and $S$ is unchanged. Hence

$$
\begin{aligned}
&\mathcal L_{m,U}[\gamma^8\Psi]=-\mathcal L_{-m,-U}[\Psi],\\
&\mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi]\qquad\text{for }U=\tfrac\lambda2S^2 .
\end{aligned}
$$

The simpler form $\mathcal L_m\to-\mathcal L_{-m}$ holds only for $U=0$. The energy-momentum tensor of Section 9 is built from the same bilinears and maps the same way, $T^{(m,\lambda)}_{\mu\nu}[\gamma^8\Psi]=-T^{(-m,-\lambda)}_{\mu\nu}[\Psi]$ (derived). If $\Psi$ solves the field equations with $(m,\lambda)$, then $\gamma^8\Psi$ solves them with $(-m,-\lambda)$. This pairing of $\pm m$ is a structural property of the equations and not a physical claim. The measured signs are $-1$ for every kinetic matrix and $+1$ for the mass and potential terms.

```
checks
  ALG_gamma8Map: wolfram-algebra, python-algebra
```

**Pin characters.** For a unit vector $u$ with $u^2=n(u)$, $\Psi\to u\Psi$ gives $\bar\Psi\Psi\to-n(u)\,\bar\Psi\Psi$. With the untwisted lift the kinetic term picks up the same factor $-n(u)$, so the free Lagrangian goes to $-n(u)\mathcal L$ and the free field equations are Pin(4,4)-covariant; with the twisted lift the kinetic factor is $+n(u)$, opposite to the mass factor. For a product $u_1u_2$ the factor is the spinor norm $n(u_1)n(u_2)$; the 16 products $e_ae_b$ with $a<4\le b$ have spinor norm $-1$ and change the sign of both terms. The even potential does not change sign: for a transformation with character $-1$,

$$
\mathcal L_{m,\lambda}\to-\mathcal L_{m,-\lambda},
$$

and the interacting field equation is mapped to the one with $\lambda\to-\lambda$. Exact covariance of the interacting theory under character $-1$ holds only for $U=0$ or an odd $U$; elements with character $+1$, in particular all of $\mathrm{Spin}_0(4,4)$, are exact symmetries. In the geometry verifier, a local $R=\gamma(n)\gamma(m)$ with $\eta(n,n)\,\eta(m,m)=-1$ maps $\mathcal L[m,\lambda]$ exactly to $-\mathcal L[m,-\lambda]$, and the naive $-\mathcal L[m,\lambda]$ fails for $\lambda\ne0$.

```
checks
  ALG_pinLiftCharacter: wolfram-algebra, python-algebra
  LAG_localSpinInvariance_G1, LAG_localSpinInvariance_G2: wolfram-geometry
```

## 8. Euler-Lagrange equations in an arbitrary gravitational field

### 8.1 Derivation

Vary $\Psi^\dagger$ (left derivative) and $\Psi$ (right derivative) independently. The terms of $\mathcal L$ that contain $\Psi^\dagger$ are $\tfrac12\sqrt{|g|}\,\Psi^\dagger C\gamma^\mu D_\mu\Psi$, $-\tfrac12\sqrt{|g|}\,(\partial_\mu\Psi^\dagger C-\Psi^\dagger C\Omega_\mu)\gamma^\mu\Psi$ and $-\sqrt{|g|}\,(mS+U)$. Integrating the derivative term by parts and using the divergence identity $\partial_\mu(\sqrt{|g|}\gamma^\mu)=\sqrt{|g|}[\gamma^\mu,\Omega_\mu]$,

$$
\begin{aligned}
E&:=\frac{\partial_L\mathcal L}{\partial\Psi^\dagger}-\partial_\mu\frac{\partial_L\mathcal L}{\partial(\partial_\mu\Psi^\dagger)}\\
&=\sqrt{|g|}\,C\Bigl[\tfrac12\gamma^\mu D_\mu\Psi+\tfrac12\Omega_\mu\gamma^\mu\Psi-(m+U'(S))\Psi\Bigr]+\tfrac12\partial_\mu\bigl(\sqrt{|g|}\,C\gamma^\mu\Psi\bigr)\\
&=\sqrt{|g|}\,C\Bigl[\tfrac12\gamma^\mu D_\mu\Psi+\tfrac12\Omega_\mu\gamma^\mu\Psi+\tfrac12\gamma^\mu\partial_\mu\Psi+\tfrac12[\gamma^\mu,\Omega_\mu]\Psi-(m+U'(S))\Psi\Bigr]\\
&=\sqrt{|g|}\,C\bigl[\gamma^\mu D_\mu\Psi-(m+U'(S))\Psi\bigr].
\end{aligned}
$$

$C$ is invertible, so $E$ vanishes exactly when the Dirac equation below holds. The quartic term contributes $\lambda S\,C\Psi$ (Result 7.2). The variation with respect to $\Psi$ gives the conjugate equation in the same way.

### 8.2 The covariant field equations

$$
\gamma^\mu D_\mu\Psi=\bigl(m+U'(\bar\Psi\Psi)\bigr)\Psi,\qquad (D_\mu\bar\Psi)\gamma^\mu=-\bigl(m+U'(\bar\Psi\Psi)\bigr)\bar\Psi,
$$

with $U'(S)=\lambda S$ for the default potential. The second equation is the Dirac conjugate of the first: $(\gamma^\mu D_\mu\Psi)^\dagger C=-(D_\mu\bar\Psi)\gamma^\mu$ by expression [1] and Result 3.5.

**Result 8.1.** At every G1 and G2 point, with $\lambda\ne0$, the Euler-Lagrange expression with respect to $\Psi^\dagger_a$ equals $\sqrt{|g|}\bigl(C(\gamma^\mu D_\mu\Psi-(m+\lambda S)\Psi)\bigr)_a$, and the one with respect to $\Psi_a$ equals $\sqrt{|g|}\bigl((D_\mu\bar\Psi)\gamma^\mu+(m+\lambda S)\bar\Psi\bigr)_a$. The Wolfram verifier works in a genuine Grassmann algebra and computes each Euler-Lagrange operator in two independent ways (direct total derivative and a jet-commutator identity), which agree. The Python geometry checker evaluates the same expressions with commuting exact numbers, which is exact here because the Lagrangian is bilinear with every $\bar\Psi$ factor on the left (measurement LAG_commutingProxyJustification), and the Grassmann demonstration repeats them in a genuine Grassmann algebra at G1 p1 and in the symbolic G2.

```
checks
  LAG_eulerLagrangePsibar_G1,
  LAG_eulerLagrangePsibar_G2, LAG_eulerLagrangePsi_G1,
  LAG_eulerLagrangePsi_G2: wolfram-geometry, python-geometry
  GR_complexLagrangianNonTrivial, GR_complexQuarticEL,
  GR_complexPsiEquation: grassmann-demo
```

### 8.3 Component form

$$
\begin{aligned}
&\gamma^\mu D_\mu\Psi=e_a{}^\mu\gamma^a\Bigl(\partial_\mu+\tfrac18\omega_{\mu bc}[\gamma^b,\gamma^c]\Bigr)\Psi,\\
&\omega_{\mu bc}=\eta_{bd}\,e_c{}^\nu\bigl(\Gamma^\rho{}_{\mu\nu}e_\rho{}^d-\partial_\mu e_\nu{}^d\bigr).
\end{aligned}
$$

Written out, the 16 component equations are

$$
\begin{aligned}
&\sum_{\mu=0}^{7}\sum_{a=0}^{7}\sum_{k=0}^{15}e_a{}^\mu(\gamma^a)_{jk}\Bigl(\partial_\mu\Psi_k+\sum_{l=0}^{15}(\Omega_\mu)_{kl}\Psi_l\Bigr)=\bigl(m+\lambda S\bigr)\Psi_j\qquad(j=0,\dots,15),\\
&S=\sum_{k,l=0}^{15}\Psi_k^\ast C_{kl}\Psi_l .
\end{aligned}
$$

### 8.4 Non-triviality in an arbitrary gravitational field

**Theorem 8.1.** (a) The spin connection is locally pure gauge, $\Omega_\mu=-(\partial_\mu R)R^{-1}$ for some local spin transformation $R$, if and only if the Riemann tensor vanishes. (b) In a curved field no local spin transformation removes the spin connection from the field equations, and the squared Dirac operator contains the scalar curvature:

$$
(\gamma^\mu D_\mu)^2\Psi=g^{\mu\nu}\bigl(D_\mu D_\nu\Psi-\Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi\bigr)+c\,R\,\Psi,\qquad c=-\tfrac14 .
$$

*Proof.* (a) A pure-gauge connection has $F_{\mu\nu}=0$ (direct computation). Conversely $F_{\mu\nu}=\tfrac12R_{ab\mu\nu}S^{ab}$ (Result 5.5), and the 28 matrices $S^{ab}$, $a<b$, are linearly independent (Result 3.2), so $F=0$ forces the Riemann tensor to vanish; a flat connection is locally pure gauge. (b) If $\Omega$ could be gauged away the curvature would vanish, contradicting (a) in a curved field. The Lichnerowicz form follows from $\gamma^\mu\gamma^\nu=g^{\mu\nu}+\tfrac12[\gamma^\mu,\gamma^\nu]$, $D_\mu\gamma^\nu=0$ and $[D_\mu,D_\nu]\Psi=F_{\mu\nu}\Psi$; the constant $c$ is fixed by the measurement below. Consequently, for $U=0$, every solution satisfies $g^{\mu\nu}\bigl(D_\mu D_\nu\Psi-\Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi\bigr)-\tfrac14R\,\Psi=m^2\Psi$: the curvature enters the second-order equation explicitly.

**Result 8.2.** $c=-1/4$ exactly at G1 p1, p2, p3 and at the three Wolfram G2 points and the symbolic Python G2 point, and $c=+1/4$ fails. In curved space $\gamma^\mu\Omega_\mu\ne0$: it has 128 nonzero entries at G1 p1 and equals $3H\gamma^0$ in G2, and the spin-connection term of the $\Psi^\dagger$ equation is nonzero in all 16 components at every G1 point and G2 sample.

```
checks
  GEO_lichnerowicz_G1, GEO_lichnerowicz_G2: wolfram-geometry, python-geometry
  GEO_lichnerowiczConstantSameG1G2: python-geometry
  LAG_eulerLagrangePsibar_spinConnectionTermNonzeroComponents:
      python-geometry measurements
```

### 8.5 Diagonal vielbeins

For a diagonal vielbein $e_\mu{}^a=\mathrm{diag}(h_0,\dots,h_7)(x)$ the anticommutator part vanishes, $\{\gamma^\mu,\Omega_\mu\}=0$, and

$$
\gamma^\mu\Omega_\mu=\frac1{2\sqrt{|g|}}\,\partial_\mu\bigl(\sqrt{|g|}\gamma^\mu\bigr)=\frac12\sum_{b=0}^{7}\frac1{h_b}\,\partial_b\ln\Bigl(\prod_{c\ne b}h_c\Bigr)\gamma^b .
$$

In the primordial field this is $3H\gamma^0$, independent of $a_4$.

```
checks
  GEO_diagonalSlashFormula_G2: wolfram-geometry, python-geometry
  GEO_diagonalSlashFormula_G3,
  GEO_anticommutatorGammaOmegaVanishesDiagonal_G2: python-geometry
```

## 9. Energy-momentum tensor operator, energies, pressure and equation of state

### 9.1 Derivation from the metric variation

The energy-momentum tensor is defined by $T_{\mu\nu}=-\frac{2}{\sqrt{|g|}}\frac{\delta\mathcal S}{\delta g^{\mu\nu}}$ with $\mathcal S=\int d^8x\,\mathcal L$. For a spinor the metric is varied through the vielbein, $\delta e_a{}^\mu=\tfrac12e_{a\nu}\,\delta g^{\mu\nu}$ (the antisymmetric part of $\delta e$ is an infinitesimal local frame rotation, under which $\mathcal S$ is invariant). The explicit $e_a{}^\mu$ in $\gamma^\mu=e_a{}^\mu\gamma^a$ contributes $\tfrac12(\bar\Psi\gamma^aD_\mu\Psi-(D_\mu\bar\Psi)\gamma^a\Psi)\,\delta e_a{}^\mu$ and $\delta\sqrt{|g|}=-\tfrac12\sqrt{|g|}\,g_{\mu\nu}\delta g^{\mu\nu}$; the variation of $\Omega_\mu$ enters the symmetrized kinetic term only through the totally antisymmetric part of the connection and, by the standard argument, does not contribute to the symmetric tensor (for diagonal metrics the reduced Lagrangian contains no metric derivatives at all, Result 9.1). With $e_{a\nu}\gamma^a=\gamma_\nu$ this gives the formula below.

**Result 9.1.** For diagonal metrics the variation is carried out explicitly and reproduces the formula off shell and on shell: in the minisuperspace $h_\mu(x_4)$ with lapse $N=h_4$, $\rho=-\frac{N}{\sqrt{|g|}}\frac{\partial L}{\partial N}$ and $T^i{}_i=\frac{h_i}{\sqrt{|g|}}\frac{\partial L}{\partial h_i}$ (no sum), and Python repeats it for a local diagonal frame with symbolic $h_\mu$ and all $\partial_\nu h_\mu$. The reduced Lagrangian does not depend on the metric velocities. The off-diagonal components are not varied explicitly; they are tested through symmetry, Hermiticity and on-shell conservation in G1 (Limitations).

```
checks
  EMT_variation_G3 (and measurement emt.signConvention): wolfram-geometry
  EMT_variation: python-geometry
```

### 9.2 Formula

$$
\begin{aligned}
&T_{\mu\nu}=-\tfrac14\Bigl[\bar\Psi\gamma_\mu D_\nu\Psi+\bar\Psi\gamma_\nu D_\mu\Psi-(D_\mu\bar\Psi)\gamma_\nu\Psi-(D_\nu\bar\Psi)\gamma_\mu\Psi\Bigr]+g_{\mu\nu}\mathcal L_s,\\
&\mathcal L_s=K-mS-U(S).
\end{aligned}
$$

On shell $K=M_{\mathrm{eff}}S$ (contract the two field equations with $\bar\Psi$ and $\Psi$), hence $\mathcal L_s=SU'(S)-U(S)$ on shell. The sign is fixed so that the energy density is $T_{44}$; for the homogeneous zero mode this is $mS+U$ (Section 9.7).

```
checks
  EMT_onshellLagrangianSUprimeMinusU_G1,
  EMT_onshellLagrangianSUprimeMinusU_G2: python-geometry
```

### 9.3 Properties

**Result 9.2.**

1. **Symmetric:** $T_{\mu\nu}=T_{\nu\mu}$.
2. **Hermitian:** at the coefficient level $T_{\mu\nu}=\bar\Psi K_{\mu\nu}\Psi+\dots$ with Hermitian $K_{\mu\nu}$ and mutually adjoint derivative coefficients, and $T_{\mu\nu}^\ast=T_{\mu\nu}$ in the Grassmann algebra.
3. **Conserved on shell:** $\nabla^\mu T_{\mu\nu}=0$ when the field equations and their first derivatives hold, solved exactly at the point for the $x_4$-derivatives; as a negative control the off-shell divergence is nonzero.
4. **Trace:** off shell $T^\mu{}_\mu=7K-8(mS+U)$; on shell

$$
T^\mu{}_\mu=-mS+7SU'(S)-8U(S)=-mS+3\lambda S^2\quad\text{for }U=\tfrac\lambda2S^2
$$

The off-shell trace follows from $\gamma^\mu\gamma_\mu=8$: $T^\mu{}_\mu=-K+8\mathcal L_s$ (measurement emt.trace records the on-shell formula).

```
checks
  EMT_symmetric_G1, EMT_symmetric_G2: python-geometry
  EMT_symmetricHermitian_G1, EMT_symmetricHermitian_G2: wolfram-geometry
  GR_emtHermitian: grassmann-demo
  EMT_conservation_G1, EMT_conservation_G2: wolfram-geometry, python-geometry
  EMT_onshellJetSolve_G1, EMT_onshellJetSolve_G2: python-geometry
  EMT_traceOffShellIdentity_G1, EMT_traceOffShellIdentity_G2: python-geometry
  EMT_trace_G1, EMT_trace_G2: wolfram-geometry, python-geometry
```

### 9.4 Observer decomposition

Take Gaussian normal time, $g_{44}=-1$, $g_{4i}=0$, and the observer $u=\partial_4$. Then

$$
\rho=T_{\mu\nu}u^\mu u^\nu=T_{44},\qquad p_{(i)}=T^i{}_i\ \ (\text{no sum},\ i\ne4),\qquad \bar p=\tfrac17\sum_{i\ne4}p_{(i)} .
$$

There are seven transverse directions: four space-like ($i=0,1,2,3$) and three time-like ($i=5,6,7$). The equation of state is $w=p/\rho$ when the transverse pressures are equal, and $w_{(i)}=p_{(i)}/\rho$ or $\bar w=\bar p/\rho$ otherwise.

### 9.5 Kinetic and potential energy: two splits

Split the kinetic term into its $x_4$ part and the rest, $K=K_4+K_\perp$, with

$$
K_4=\tfrac12\bigl(\bar\Psi\gamma^{x_4}D_4\Psi-(D_4\bar\Psi)\gamma^{x_4}\Psi\bigr),\qquad K_\perp=\tfrac12\sum_{\mu\ne4}\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr).
$$

- **(A) Lagrangian split.** $\mathrm{KE}_L:=\tfrac12K_4$ (half of the time-derivative part of the kinetic term) and $\mathrm{PE}_L:=\rho-\mathrm{KE}_L$. This is the exact analogue of the scalar field's $\tfrac12\dot\phi^2$ and $V$: $\rho=\mathrm{KE}_L+\mathrm{PE}_L$ by definition, and for a homogeneous isotropic state on shell also $p=\mathrm{KE}_L-\mathrm{PE}_L$ (Section 9.6).
- **(B) Hamiltonian split.** $\mathrm{KE}_H:=-K_\perp$ (gradient and transverse-connection energy) and $\mathrm{PE}_H:=mS+U$ (mass and self-interaction energy). In Gaussian normal time, $\gamma_4=-\gamma^{x_4}$ and $g_{44}=-1$ turn the formula of Section 9.2 into $T_{44}=K_4-\mathcal L_s=-K_\perp+mS+U$, so

$$
\rho=T_{44}=\mathrm{KE}_H+\mathrm{PE}_H\qquad\text{identically (off shell)}.
$$

This identity is derived here from the verified formula; it is the energy density as the Hamiltonian density of Section 10.4. The time derivatives do not appear in split (B): for a first-order field they are not an energy.

### 9.6 Equation of state

For a homogeneous isotropic state on shell (Section 9.7):

$$
\begin{aligned}
&\rho=mS+U,\qquad p=SU'-U,\\
&w=\frac{p}{\rho}=\frac{SU'-U}{mS+U}=\frac{\mathrm{KE}_L-\mathrm{PE}_L}{\mathrm{KE}_L+\mathrm{PE}_L},\\
&\mathrm{KE}_L=\tfrac12S\,(m+U'),\qquad \mathrm{PE}_L=\tfrac12\bigl(mS+2U-SU'\bigr),\qquad \mathrm{KE}_H=0,\qquad \mathrm{PE}_H=\rho .
\end{aligned}
$$

- **Free massive field ($U=0$).** $\mathrm{KE}_L=\mathrm{PE}_L=\tfrac12mS$, $p=0$, $w=0$: dust.
- **Default potential.** $\rho=mS+\tfrac\lambda2S^2$, $p=\tfrac\lambda2S^2$, $w=\dfrac{\lambda S}{2m+\lambda S}$, $\mathrm{KE}_L=\tfrac12S(m+\lambda S)$, $\mathrm{PE}_L=\tfrac12mS$.
- **Limits.** $w\to-1$ when $\mathrm{KE}_L/\mathrm{PE}_L\to0$ and $w\to+1$ when $\mathrm{PE}_L/\mathrm{KE}_L\to0$, as for the scalar field.
- **Phantom criterion.** $\rho+p=2\,\mathrm{KE}_L=S(m+U')$. For $\rho>0$ the state is phantom ($w<-1$) exactly when $\mathrm{KE}_L<0$, that is when $S(m+U')<0$. Unlike $\tfrac12\dot\phi^2$, $\mathrm{KE}_L$ has no fixed sign, because $S=\Psi^\dagger C\Psi$ is built from $C$ of signature (8,8) (Result 3.3).

**Consequence (derived from the verified formulas, not machine-checked).** Section 9.7 gives $\partial_4\rho+\sum_{i\ne4}H_i(\rho+p_i)=0$; with $\rho+p=S(m+U')$ this becomes $(m+U')\bigl(\partial_4S+S\sum_iH_i\bigr)=0$, so $S\sqrt{|g|}$ is constant wherever $m+U'\ne0$: $S$ dilutes as the inverse 7-volume. For the default potential $w=\lambda S/(2m+\lambda S)$ therefore changes as the 7-volume changes. For example, with $m>0$, $\lambda<0$ and $x=|\lambda|S/m$: $w=-x/(2-x)$, the state is phantom with $\rho>0$ for $1<x<2$, $w=-1$ at $x=1$, and $w\to0$ as $x\to0$. Whether such states are physically admissible (energy conditions, stability, the quantum Krein structure) is not decided here.

### 9.7 Homogeneous diagonal backgrounds

For a diagonal Gaussian-normal frame $h_i(x_4)$, $h_4=N=1$, with Hubble rates $H_i=\partial_4h_i/h_i$, and a homogeneous $\Psi(x_4)$:

$$
\begin{aligned}
&\rho=mS+U\ \ (\text{off shell}),\qquad p_{(i)}=\mathcal L_s\ \ (\text{off shell})=SU'-U\ \ (\text{on shell, all seven }i\ne4),\\
&T_{ij}=\tfrac14(H_i-H_j)\,\bar\Psi\gamma_i\gamma_j\gamma^{x_4}\Psi\quad(i\ne j,\ i,j\ne4),\qquad \gamma_i=g_{ii}\gamma^{x_i},\\
&T_{4i}=-\tfrac14\bigl(\bar\Psi\gamma_i\partial_4\Psi-\partial_4\bar\Psi\,\gamma_i\Psi\bigr)\ \ (\text{off shell}),\qquad T_{4i}=0\ \ (\text{on shell}),\\
&\partial_4\rho+\sum_{i\ne4}H_i\,(\rho+p_{(i)})=0,\\
&\partial_4\bigl(\bar\Psi\gamma^i\gamma^j\gamma^4\Psi\bigr)=-\Bigl(\sum_kH_k\Bigr)\bar\Psi\gamma^i\gamma^j\gamma^4\Psi\qquad(\text{frame gammas, on shell}).
\end{aligned}
$$

The pressure is isotropic in all seven transverse directions although the $h_i$ differ. The off-diagonal $T_{4i}$ vanish on shell because $\{\gamma_i,\gamma^{x_4}\}=0$. The $T_{ij}$ are proportional to a tensor bilinear that decays like the inverse 7-volume, so zero initial data stay zero, and a diagonal metric is consistent with states for which this bilinear vanishes. In the flat-gamma notation of the Python checker the same component reads $T_{ij}=\tfrac14\eta_{ii}\eta_{jj}h_ih_j(H_i-H_j)\,\bar\Psi\gamma^i\gamma^j\gamma^4\Psi$; the two forms are identical because $\gamma_i=\eta_{ii}h_i\gamma^i$ (notation conversion recorded in stage1-summary.json).

**Result 9.3.** The Wolfram verifier checks all of these at the three G3 times, off and on shell as indicated. The Python checker independently checks, with its own random on-shell data at three G3 times, the energy density, the seven equal pressures, $\mathrm{KE}_L$, $\mathrm{PE}_L$, $\rho=\mathrm{KE}_L+\mathrm{PE}_L$, $p=\mathrm{KE}_L-\mathrm{PE}_L$ and the off-diagonal forms; the off-shell forms $\rho=mS+U$ and $p_{(i)}=\mathcal L_s$ are part of its metric-variation check. For generic states the $T_{ij}$ are nonzero in 42 of 42 ordered pairs and the $T_{4i}$ vanish on shell. A sample: at $x_4=1/3$ with $m=4$, $\lambda=7/6$ and $S=-75899/7560$ the Python report gives $\rho=260864863/13996800$, $\mathrm{KE}_L=3793356121/97977600$, $\mathrm{PE}_L=-75899/3780$ and $w=75899/24059$.

```
checks
  EMT_homogeneousReduction_G3: wolfram-geometry
  EMT_homogeneousReduction, EMT_homogeneousTimeSpaceVanishesOnShell_G3: python-geometry
  EMT_homogeneous_G3_q1 (measurement): python-geometry
```

### 9.8 Side-by-side with the scalar field of the PDF

| Quantity | Scalar field (PDF) | dirac16complex (homogeneous, on shell) |
| --- | --- | --- |
| Lagrangian | $\tfrac12\dot\phi^2-V(\phi)$ | $\mathcal L_s=K-mS-U(S)$ |
| energy density | $\rho_\phi=\tfrac12\dot\phi^2+V$ | $\rho=mS+U$ |
| pressure | $P_\phi=\tfrac12\dot\phi^2-V=\mathcal L_\phi$ | $p=SU'-U=\mathcal L_s$ |
| kinetic energy | $\tfrac12\dot\phi^2\ge0$ | $\mathrm{KE}_L=\tfrac12S(m+U')$, either sign |
| potential energy | $V$ | $\mathrm{PE}_L=\tfrac12(mS+2U-SU')$ |
| $\rho=\mathrm{KE}+\mathrm{PE}$, $p=\mathrm{KE}-\mathrm{PE}$ | yes | yes (split A) |
| Hamiltonian split | $\tfrac12\dot\phi^2+V$ | $\mathrm{KE}_H=0$, $\mathrm{PE}_H=mS+U$ |
| equation of state | $w_\phi=\dfrac{\tfrac12\dot\phi^2-V}{\tfrac12\dot\phi^2+V}$ | $w=\dfrac{SU'-U}{mS+U}$ |
| $w\to-1$ | $\dot\phi^2\ll V$ | $\lvert\mathrm{KE}_L\rvert\ll\mathrm{PE}_L$ |
| $w\to+1$ | $\dot\phi^2\gg V$ (kination) | $\mathrm{PE}_L\ll\mathrm{KE}_L$ |
| phantom $w<-1$ | impossible for a canonical field | possible: $\mathrm{KE}_L<0$ with $\rho>0$ |
| equation of motion | $\ddot\phi+3H\dot\phi+V'(\phi)=0$ | $\gamma^\mu D_\mu\Psi=(m+U')\Psi$ |
| dilution | depends on $V$ | $S\propto1/\sqrt{\lvert g\rvert}$ (derived, 9.6) |

**Exact analogy.** In both cases the energy density is the Hamiltonian density ($T_{44}$) and, for a homogeneous state, the pressure equals the Lagrangian density; the Lagrangian split gives $\rho=\mathrm{KE}+\mathrm{PE}$ and $p=\mathrm{KE}-\mathrm{PE}$, hence the same formula for $w$. **Difference.** The fermion Lagrangian is first order in time. Its time-derivative term is not a positive kinetic energy: in the Hamiltonian split it contributes nothing to $\rho$, and in the Lagrangian split $\mathrm{KE}_L=\tfrac12S(m+U')$ can be negative. The canonical scalar field satisfies $w\ge-1$ whenever $\rho>0$; dirac16complex can cross $w=-1$ at the level of these classical (mean-field) formulas.

## 10. Canonical quantization in 4+4 dimensions

### 10.1 Slicing and momenta

We quantize with respect to $x_4$ on the 7-dimensional slices $x_4=\text{const}$, with coordinates $(x_0,x_1,x_2,x_3,x_5,x_6,x_7)$. This requires $g^{44}\ne0$ (the slices are non-characteristic). Split $\mathcal L$ into its $x_4$ part and the rest and add the total derivative $\tfrac12\partial_4\bigl(\sqrt{|g|}\,\bar\Psi\gamma^{x_4}\Psi\bigr)$:

$$
\mathcal L'=\mathcal L+\tfrac12\partial_4\bigl(\sqrt{|g|}\,\bar\Psi\gamma^{x_4}\Psi\bigr)=\sqrt{|g|}\,\Psi^\dagger C\gamma^{x_4}\partial_4\Psi+(\text{terms without }\partial_4\Psi\text{ or }\partial_4\Psi^\dagger).
$$

The momentum conjugate to $\Psi$ (right derivative) is $\Pi=\sqrt{|g|}\,\Psi^\dagger C\gamma^{x_4}$, and $\mathcal L'$ does not depend on $\partial_4\Psi^\dagger$.

**Result 10.1.** In a genuine Grassmann algebra, $\Pi_a=\partial_R\mathcal L'/\partial(\partial_4\Psi_a)=\sqrt{|g|}(\Psi^\dagger C\gamma^{x_4})_a$ and $\partial_L\mathcal L'/\partial(\partial_4\Psi^\dagger_a)=0$ at every G1 and G2 point.

```
checks
  QNT_canonicalMomentum_G1, QNT_canonicalMomentum_G2: wolfram-geometry
```

### 10.2 Constraints and Dirac brackets

The momenta do not contain velocities, so there are primary constraints $\chi_a=\Pi_a-\sqrt{|g|}(\Psi^\dagger C\gamma^{x_4})_a\approx0$ and $\bar\chi_a=\Pi_{\Psi^\dagger,a}\approx0$. Their graded Poisson brackets form, up to sign and transposition, the matrix $\mathcal K=\sqrt{|g|}\,C\gamma^{x_4}$. It is invertible exactly when $g^{44}\ne0$, because

$$
(C\gamma^{x_4})(\gamma^{x_4}C)=(\gamma^{x_4}C)(C\gamma^{x_4})=g^{44}\,I_{16},\qquad (C\gamma^{x_4})^{-1}=\frac{\gamma^{x_4}C}{g^{44}},
$$

so the constraints are second class. The Dirac bracket eliminates them, and the quantization rule $\{\cdot,\cdot\}_+=i\{\cdot,\cdot\}_D$ gives the anticommutators below. The matrix identity is verified symbolically for an arbitrary $e_a{}^4$ and at the G1 points. The graded constraint-matrix computation itself is not a separate machine check; the verifiers check the result as the matrix identity $\{\Psi,\Psi^\dagger\}=i\mathcal K^{-1}$ that follows from the first-order form of $\mathcal L'$.

```
checks
  QNT_curvedAnticommutatorMatrix: wolfram-algebra
```

### 10.3 Equal-x4 anticommutators in curved space

For $x$ and $y$ on the same slice ($\hbar=1$):

$$
\begin{aligned}
&\bigl\{\Psi_a(x),\Psi^\dagger_b(y)\bigr\}=i\bigl[(C\gamma^{x_4})^{-1}\bigr]_{ab}\frac{\delta^7(x-y)}{\sqrt{|g|}}=i\,\frac{[\gamma^{x_4}C]_{ab}}{g^{44}}\,\frac{\delta^7(x-y)}{\sqrt{|g|}},\\
&\{\Psi_a(x),\Psi_b(y)\}=\{\Psi^\dagger_a(x),\Psi^\dagger_b(y)\}=0 .
\end{aligned}
$$

The matrix $i(\sqrt{|g|}C\gamma^{x_4})^{-1}$ is Hermitian. In Gaussian normal gauge ($g^{44}=-1$ and $\gamma^{x_4}=\gamma^4$, as in the primordial field G2) this becomes

$$
\bigl\{\Psi_a(x),\Psi^\dagger_b(y)\bigr\}=B_{ab}\,\frac{\delta^7(x-y)}{\sqrt{|g|}},\qquad B:=-iC\gamma^4 .
$$

**Result 10.2.** $B$ is Hermitian, $B^2=1$, its eigenvalues are $+1$ and $-1$ with multiplicity 8 each (characteristic polynomial $(x-1)^8(x+1)^8$), $[C,B]=0$ and $BC=-i\gamma^4$. The Gaussian-normal reduction of the anticommutator to $B/\sqrt{|g|}$ is checked in the primordial field.

```
checks
  ALG_chargeFormB: wolfram-algebra, python-algebra
  QNT_canonicalMomentum_G1, QNT_canonicalMomentum_G2: wolfram-geometry
```

### 10.4 Hamiltonian and Heisenberg equations

The canonical Hamiltonian density is $\mathcal H=\Pi\,\partial_4\Psi-\mathcal L'$. Using the split of Section 9.5 (derived here, not a separate machine check):

$$
\begin{aligned}
\mathcal H&=\sqrt{|g|}\,\bigl(\mathrm{KE}_H+\mathrm{PE}_H\bigr)\\
&\quad-\tfrac12\sqrt{|g|}\,\bar\Psi\{\gamma^{x_4},\Omega_4\}\Psi-\tfrac12\bar\Psi\,\partial_4\bigl(\sqrt{|g|}\gamma^{x_4}\bigr)\Psi .
\end{aligned}
$$

The last two terms come from the connection along $x_4$ and from the explicit $x_4$-dependence of the added total derivative. In flat space in Cartesian coordinates both vanish and $\mathcal H=T_{44}=\rho$. There, with $\{\Psi_a,\Psi^\dagger_b\}=B_{ab}\delta^7$ and $U=0$, $H=\int d^7x\,\Psi^\dagger(mC-C\gamma^j\partial_j)\Psi$ (sum over $j\ne4$), and the Heisenberg equation gives

$$
\partial_4\Psi=i[H,\Psi]=-iB\,(mC-C\gamma^j\partial_j)\Psi=-m\gamma^4\Psi+\gamma^4\gamma^j\partial_j\Psi,
$$

which is the field equation $\gamma^\mu\partial_\mu\Psi=m\Psi$ multiplied by $\gamma^4$ (using $BC=-i\gamma^4$ and $(\gamma^4)^2=-1$).

### 10.5 Krein structure

**Theorem 10.1.** Every Spin(4,4)-invariant Hermitian form on $\mathbb C^{16}$ is even in chirality, whereas $\gamma^4$ is odd. Consequently every charge density of the form $\mathrm{Herm}(c\,H\gamma^4)$ built from an invariant form $H$ is indefinite, of signature (8,8), or vanishes. The canonical state space is therefore a Krein space; this is intrinsic to signature (4,4) and not a consequence of the particular choice $B$.

**Result 10.3.** The Spin(4,4)-invariant bilinear forms form a 2-dimensional space spanned by $CP_-$ and $CP_+$ (both symmetric and block diagonal in chirality); an invariant Hermitian form is $H=\alpha CP_-+\beta CP_+$ with real $\alpha,\beta$; $H\gamma^4$ is block off-diagonal, traceless and similar to its negative, with $(H\gamma^4)^2=-\alpha\beta I_{16}$; and for every constant $c$ the Hermitian part of $cH\gamma^4$ is traceless with square $|k|^2I_{16}$, $k=\tfrac12(\bar c\beta-c\alpha)$, hence has signature (8,8) unless it vanishes.

```
checks
  ALG_invariantForms: wolfram-algebra, python-algebra
```

The canonical anticommutator defines the Krein form $[f,h]=f^\dagger Bh$ on the one-particle space. $J=B$ is a fundamental symmetry ($J=J^\dagger=J^{-1}$), and the associated positive Hilbert product is $[f,Jh]=f^\dagger h$, the standard one. In a Hilbert-space representation the Hilbert adjoint of $\Psi$ is $\chi:=\Psi^\dagger B$, with $\{\Psi_a,\chi_b\}=\delta_{ab}\delta^7$ (Gaussian normal gauge, flat): the canonical $\Psi^\dagger=\chi B$ is the Krein adjoint of $\Psi$, not its Hilbert adjoint.

**Result 10.4.** At rest the positive- and negative-frequency spaces (the eigenspaces of $-i\gamma^4$, since $h_0=m(-i\gamma^4)$) are 8-dimensional, $B$ preserves them, and the $B$-form on each has signature (4,4). The same (4,4) holds for moving states in the good sector: at $m=1$, $k=(1,1,2,3)$, $E=4$ for both signs of the energy, and at $m=3$, $k=(1,1,1,2)$, $E=4$ for positive energy. The Krein form is thus indefinite even among positive-energy states.

```
checks
  QNT_kreinSignature: wolfram-algebra, python-algebra
```

### 10.6 Flat-space modes and the good sector

In flat space the field equation takes the Schrödinger form $i\partial_4\Psi=h\Psi$ with, for a plane wave $e^{ik_jx^j}$ ($j\in\{0,1,2,3,5,6,7\}$),

$$
\begin{aligned}
&h_k=-im\gamma^4-\gamma^4\sum_{j\ne4}k_j\gamma^j,\qquad [h_k,B]=2i\sum_{j=5}^{7}k_jC\gamma^j,\\
&h_k^2=\bigl(m^2+k_0^2+k_1^2+k_2^2+k_3^2-k_5^2-k_6^2-k_7^2\bigr)I_{16} .
\end{aligned}
$$

The anti-Hermitian part of $h_k$ is $-\gamma^4(k_5\gamma^5+k_6\gamma^6+k_7\gamma^7)$, whose square is $-(k_5^2+k_6^2+k_7^2)I_{16}$. Hence $h_k$ is Hermitian, and commutes with $B$, if and only if $k_5=k_6=k_7=0$.

**Result 10.5.** These identities hold exactly for symbolic $m$ and $k$ (Wolfram) and by a structural proof for all real $m,k$ plus 10 exact samples (Python); 2 of the samples with extra-time momentum have $E^2<0$.

```
checks
  QNT_flatModeHamiltonian: wolfram-algebra, python-algebra
```

**The good sector** is the sector of fields that do not depend on $x_5,x_6,x_7$ ($k_5=k_6=k_7=0$). There $h_k$ is Hermitian and traceless with $h_k^2=E_k^2$, $E_k=\sqrt{m^2+k_0^2+k_1^2+k_2^2+k_3^2}$, so its eigenvalues are $+E_k$ and $-E_k$ with multiplicity 8 each: 8 particle and 8 antiparticle states for every momentum $k=(k_0,k_1,k_2,k_3)$.

### 10.7 Fock space, Dirac sea and normal ordering

In the good sector (flat space, Gaussian normal time) let $u_s(k)$ and $v_s(k)$, $s=0,\dots,7$, be orthonormal (for $f^\dagger h$) eigenvectors of $h_k$ with eigenvalues $+E_k$ and $-E_k$. The mode expansion

$$
\begin{aligned}
&\Psi(x)=\int\frac{d^4k}{(2\pi)^4}\sum_{s=0}^{7}\Bigl[b_s(k)\,u_s(k)\,e^{-iE_kx_4}+d_s(-k)^\ast\,v_s(k)\,e^{iE_kx_4}\Bigr]e^{ik\cdot x},\\
&\{b_s(k),b_{s'}(k')^\ast\}=\{d_s(k),d_{s'}(k')^\ast\}=\delta_{ss'}(2\pi)^4\delta^4(k-k'),
\end{aligned}
$$

with the Hilbert adjoints ${}^\ast$ of the positive structure $J=B$, realizes $\{\Psi_a,\chi_b\}=\delta_{ab}\delta^4$ on a positive-definite Fock space. The vacuum $|0\rangle$ is annihilated by all $b_s(k)$ and $d_s(k)$: the negative-energy states are filled (Dirac sea), and $d^\ast$ creates antiparticles. After normal ordering

$$
H=\int\frac{d^4k}{(2\pi)^4}\,E_k\sum_{s=0}^{7}\bigl(b_s(k)^\ast b_s(k)+d_s(k)^\ast d_s(k)\bigr)\ \ge0 .
$$

This construction is derived here from Results 10.2, 10.4 and 10.5; it is not a separate machine check.

### 10.8 Unitary and Krein-unitary symmetries

A spin transformation $\Psi\to R\Psi$ preserves the canonical anticommutator iff $RBR^\dagger=B$, equivalently $R^\dagger BR=B$ (Krein-unitary). It is implemented unitarily on the positive Fock space iff in addition $R$ is unitary for $f^\dagger h$ and commutes with $J=B$ (derived). For $R=\exp(\theta S^{ab})$ the conditions concern the generators.

**Result 10.6.**

1. Exactly 13 of the 28 generators $S^{ab}$ commute with $B$: the 6 of so(4) ($a,b\in\{0,1,2,3\}$), the 3 of so(3) ($a,b\in\{5,6,7\}$) and the 4 boosts $S^{a4}$, $a\in\{0,1,2,3\}$. Since $B\propto\gamma^0\gamma^1\gamma^2\gamma^3\gamma^4$, the boosts $S^{a4}$ anticommute with $C$ and with $\gamma^4$ and therefore commute with $B$; they are Hermitian, so $\exp(\theta S^{a4})$ is neither unitary nor Krein-unitary.
2. Exactly 9 generators are anti-Hermitian (unitary for $\Psi^\dagger\Psi$) and commute with $B$. They generate the unitarily implemented group Spin(4) x Spin(3). The literal claim "exactly 9 of the 28 $S^{ab}$ commute with $B$" is false and is recorded as false in both reports.
3. Exactly 21 generators, those with $a,b\ne4$, satisfy the Krein condition $(S^{ab})^\dagger B+BS^{ab}=0$. They generate the Krein-unitary slice group Spin(4,3). The Krein condition fails for all 7 generators $S^{4b}$.
4. Exactly 12 generators are anti-Hermitian for $\Psi^\dagger\Psi$ (so(4) and so(4) on the directions 4 to 7).

Both algebra reports use this meaning of the check, as recorded in stage1-summary.json. Time translations in the good sector are unitary ($h_k$ Hermitian), and the U(1) phase is unitary.

```
checks
  QNT_unitaryAndKreinSubgroups: wolfram-algebra, python-algebra
```

### 10.9 The U(1) current and charge

$J^\mu=-i\bar\Psi\gamma^\mu\Psi$ is Hermitian, and in Gaussian normal gauge $J^4=\Psi^\dagger B\Psi$: all eight current matrices are Hermitian and the matrix of $J^4$ is $B$. The conserved charge is $Q=\int d^7x\,\sqrt{|g|}\,J^4$. As a quadratic form in classical spinors it is indefinite (signature (8,8)); in the Hilbert representation of Section 10.5, $\Psi^\dagger B\Psi=\chi\Psi$, and after normal ordering $Q=\sum(b^\ast b-d^\ast d)$: particles have charge $+1$ and antiparticles $-1$ (derived).

```
checks
  QNT_currentHermiticity: wolfram-algebra, python-algebra
  GR_currentHermitian: grassmann-demo
```

### 10.10 The extra-time sector

For momenta along $x_5,x_6,x_7$ the operator $h_k$ is not Hermitian and does not commute with $B$ (Result 10.5), and $E^2=m^2+k_0^2+\dots+k_3^2-k_5^2-k_6^2-k_7^2$ can be negative: two of the Python samples have $E^2=-271/196$ and $E^2=-3$. The corresponding frequencies are imaginary and the modes grow exponentially in $x_4$. This is the ill-posedness of the initial-value problem for ultrahyperbolic equations: the slice $x_4=\text{const}$ contains three time-like directions. The positive Fock space of Section 10.7 exists only in the good sector.

### 10.11 Expectation values

In the Hilbert representation the canonical bilinear is $\Psi^\dagger M\Psi=\chi BM\Psi$. For a normalized one-particle state with wave function $u$ ($u^\dagger u=1$, positive energy, normal ordering),

$$
\bigl\langle\Psi^\dagger M\Psi\bigr\rangle=u^\dagger BM\,u .
$$

Examples (derived): the charge ($M=B$) gives $u^\dagger u=1$; the energy ($M=Bh$) gives $u^\dagger h u=E$; the scalar density ($M=C$) gives $u^\dagger BCu=u^\dagger(-i\gamma^4)u$, which is $+1$ for a positive-energy state at rest with $m>0$, so $\langle\rho\rangle=m\langle S\rangle=m=E$. The naive density $\Psi^\dagger\Psi$ gives $u^\dagger Bu$, which is indefinite even on positive-energy states (Result 10.4); it is not the physical density.

## 11. Verification records

All five reports have schemaVersion 1, and every check in them is true. The counts below are those of stage1-summary.json, which re-reads the five reports, re-compares the key measurements and records an empty list of disagreements:

```
report                         producer                                    checks true
wolfram-algebra-report.json    scripts/verify_dirac16complex_algebra.wls   21 of 21
wolfram-geometry-report.json   scripts/verify_dirac16complex_geometry.wls  43 of 43
python-algebra-report.json     scripts/check_dirac16complex_algebra.py     21 of 21
python-geometry-report.json    scripts/check_dirac16complex_geometry.py    52 of 52
grassmann-demo-report.json     scripts/demo_grassmann_lagrangians.py       16 of 16
stage1-summary.json            scripts/build_stage1_summary.py             153 of 153
```

The producers record Wolfram Language 15.0.1 and Python 3.14.5, sympy 1.14.0, numpy 2.4.6.

### 11.1 WolframScript, algebra

The Wolfram algebra verifier uses exact integer, rational and Gaussian-rational arithmetic. Commutants, intertwiners and invariant forms are exact null spaces of integer coefficient matrices, and signatures come from exact characteristic polynomials. Files and checks:

```
wolfram/Dirac16ComplexAlgebra.wl
scripts/verify_dirac16complex_algebra.wls
```

```
wolfram-algebra: ALG_clifford ALG_gammaTransposeSymmetry ALG_chargeMatrix ALG_expression1
    ALG_spinTransposeProperties ALG_chirality ALG_faithful ALG_pinIrreducibleComplex
    ALG_spinDecomposition ALG_cliffordPictureIntertwiner ALG_octonionPictureIntertwiner
    ALG_chargeFormB ALG_invariantForms ALG_gamma8Map ALG_pinLiftCharacter
    QNT_curvedAnticommutatorMatrix QNT_flatModeHamiltonian QNT_kreinSignature
    QNT_unitaryAndKreinSubgroups QNT_currentHermiticity ALG_fixtureAgreement
```

### 11.2 WolframScript, geometry

Every derived object of the Wolfram geometry verifier is an exact order-1 jet (value and eight first derivatives) at the test point, and the G2 arithmetic is exact in $\mathbb Q(\cos z)$. The Euler-Lagrange, canonical-momentum and Lg[] checks use a genuine Grassmann algebra; the energy-momentum, Lichnerowicz and invariance checks use commuting exact numbers, which is exact for bilinears with $\Psi^\dagger$ on the left and $\Psi$ on the right (measurement convention.commutingEvaluation). Files and checks:

```
wolfram/Dirac16ComplexGeometry.wl
scripts/verify_dirac16complex_geometry.wls
```

```
wolfram-geometry: ALG_chargeMatrix ALG_cliffordRelations ALG_grassmannLemmas
    EMT_conservation_G1 EMT_conservation_G2 EMT_homogeneousReduction_G3
    EMT_symmetricHermitian_G1 EMT_symmetricHermitian_G2 EMT_trace_G1 EMT_trace_G2
    EMT_variation_G3 GEO_curvature_G1 GEO_curvature_G2 GEO_diagonalSlashFormula_G2
    GEO_divergenceIdentity_G1 GEO_divergenceIdentity_G2 GEO_frameNondegenerate_G1
    GEO_frameNondegenerate_G2 GEO_gammaCovariantConstancy_G1
    GEO_gammaCovariantConstancy_G2 GEO_lichnerowicz_G1 GEO_lichnerowicz_G2
    GEO_notebookContractionFails_G1 GEO_notebookContractionFails_G2
    GEO_omegaAntisymmetry_G1 GEO_omegaAntisymmetry_G2 GEO_primordialInvariants_G2
    GEO_symbolicJetAgreement_G2 GEO_vielbeinPostulate_G1 GEO_vielbeinPostulate_G2
    LAG_eulerLagrangePsibar_G1 LAG_eulerLagrangePsibar_G2 LAG_eulerLagrangePsi_G1
    LAG_eulerLagrangePsi_G2 LAG_hermiticity_G1 LAG_hermiticity_G2
    LAG_localSpinInvariance_G1 LAG_localSpinInvariance_G2
    LAG_notebookLgGrassmannTrivial_G1 LAG_notebookLgGrassmannTrivial_G2
    NEG_notebookConnectionDetected_G2 QNT_canonicalMomentum_G1 QNT_canonicalMomentum_G2
```

### 11.3 Python, algebra

The Python algebra checker uses the standard library only (exact rationals, no floating point). Files and checks:

```
scripts/d16c_exact.py
scripts/build_dirac16complex_fixture.py
scripts/check_dirac16complex_algebra.py
```

```
python-algebra: ALG_clifford ALG_gammaTransposeSymmetry ALG_chargeMatrix ALG_expression1
    ALG_spinTransposeProperties ALG_chirality ALG_faithful ALG_pinIrreducibleComplex
    ALG_spinDecomposition ALG_cliffordPictureIntertwiner ALG_octonionPictureIntertwiner
    ALG_chargeFormB ALG_invariantForms ALG_gamma8Map ALG_pinLiftCharacter
    QNT_flatModeHamiltonian QNT_kreinSignature QNT_unitaryAndKreinSubgroups
    QNT_currentHermiticity ALG_fixtureAgreement ALG_wolframAgreement
```

### 11.4 Python, geometry

The Python geometry checker uses sympy with exact rationals: G1 by exact truncated Taylor jets, and G2 at a fully symbolic point in $\mathbb Q(w,c,E,A_1,A_2,A_3,H)$ with $w=\sin^{1/6}z$, $c=\cos z$, $E=e^{a_4}$ and $A_k$ the derivatives of $a_4$. The relation $w^{12}+c^2=1$ was needed in 0 of its zero tests. Files and checks:

```
scripts/d16c_geometry_sympy.py
scripts/check_dirac16complex_geometry.py
```

```
python-geometry: ALG_cliffordRelations ALG_sigma16EqualsGamma0123
    ALG_CSymmetricInvolution ALG_expression1CgammaAntisymmetric ALG_gammaSymmetryPattern
    ALG_CSabAntisymmetric ALG_chiralityDiag ALG_CAnticommutatorGammaSSymmetric
    ALG_CCommutatorGammaSAntisymmetric ALG_SabGammaCommutator GEO_frameNondegenerate_G1
    GEO_vielbeinPostulate_G1 GEO_omegaAntisymmetry_G1 GEO_gammaCovariantConstancy_G1
    GEO_notebookContractionFails_G1 GEO_divergenceIdentity_G1
    GEO_sqrtgSquaredEqualsDetg_G1 GEO_curvature_G1 GEO_lichnerowicz_G1
    LAG_eulerLagrangePsibar_G1 LAG_eulerLagrangePsi_G1 EMT_onshellJetSolve_G1
    EMT_symmetric_G1 EMT_trace_G1 EMT_traceOffShellIdentity_G1
    EMT_onshellLagrangianSUprimeMinusU_G1 EMT_conservation_G1 GEO_vielbeinPostulate_G2
    GEO_omegaAntisymmetry_G2 GEO_gammaCovariantConstancy_G2
    GEO_notebookContractionFails_G2 GEO_divergenceIdentity_G2
    GEO_sqrtgSquaredEqualsDetg_G2 GEO_curvature_G2
    GEO_anticommutatorGammaOmegaVanishesDiagonal_G2 GEO_primordialInvariants_G2
    GEO_diagonalSlashFormula_G2 GEO_lichnerowicz_G2 LAG_eulerLagrangePsibar_G2
    LAG_eulerLagrangePsi_G2 EMT_onshellJetSolve_G2 EMT_symmetric_G2 EMT_trace_G2
    EMT_traceOffShellIdentity_G2 EMT_onshellLagrangianSUprimeMinusU_G2
    EMT_conservation_G2 GEO_lichnerowiczConstantSameG1G2 EMT_homogeneousReduction
    GEO_diagonalSlashFormula_G3 EMT_homogeneousTimeSpaceVanishesOnShell_G3 EMT_variation
    GEO_wolframAgreement
```

### 11.5 Python, Grassmann demonstrations

The demonstrations work in exact Grassmann algebras with 720 generators for real $\Psi$ jets and 1440 for complex $(\Psi,\Psi^\ast)$ jets. Files and checks:

```
scripts/grassmann_algebra.py
scripts/demo_grassmann_lagrangians.py
```

```
grassmann-demo: GR_conjugationRules GR_massTermVanishesReal
    GR_bilinearOnlyAntisymmetricPartSurvives GR_kineticTotalDerivativeReal
    GR_kineticSymmetricMatrixContrast GR_quarticTermPolynomial GR_scalarBilinearHermitian
    GR_currentHermitian GR_notebookLgELTrivial GR_notebookLgPureDivergence
    GR_complexLagrangianNonTrivial GR_complexQuarticEL GR_complexPsiEquation
    GR_lagrangianHermitian GR_emtHermitian GR_unsymmetrizedKineticNotHermitian
```

### 11.6 Agreement between the implementations

The cross-implementation checks:

```
ALG_fixtureAgreement (wolfram-algebra):  Wolfram reads the Python fixture;
    75 of 75 matrices agree by name
ALG_wolframAgreement (python-algebra):   Python reads the Wolfram algebra report;
    K_clifford, K_octonion and the chirality agree; 20 shared check names
    with equal verdicts; 47 of 47 shared measurements agree
GEO_wolframAgreement (python-geometry):  Python reads the Wolfram geometry report;
    26 shared check names with equal verdicts;
    84 of 84 shared measurements agree
```

The geometry comparison covers the G1 point data, the nonzero counts, the Lichnerowicz constant, the curvature sign, the Python G2 formulas evaluated at the exact Wolfram points, and the energy-momentum sign and trace conventions. The field-dependent values (traces, $\rho$, $p$, KE and PE at the test points) are not compared between the implementations, because each draws its own random field data and parameters; they are compared through the formulas that both verify. stage1-summary.json records 30 agreed key measurements, the hash links between the reports, and the equivalences that hold after a notation conversion.

### 11.7 Files and hashes

sha256 of the reports, of the fixture and of the producers, as recorded in the reports and in stage1-summary.json:

```
artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
  d43adeeba580bdd8cec56fac5fa74906b7578c06c8589e52dbe3da1404cd49e7
artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json
  cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac
artifacts/dirac16complex/arbitrary-field/python-algebra-report.json
  3275b2af1a2f56f9bd779ad359e7ed078cb2c64c744863732f789f410bb50c97
artifacts/dirac16complex/arbitrary-field/python-geometry-report.json
  deec576c1613bb06ce8ac4ad9f89a7b008239bd9d4b624bea14728fa77b2a197
artifacts/dirac16complex/arbitrary-field/grassmann-demo-report.json
  b83997857ccfc9fb71f05efbcaebe16f29bf36687cc08c16e0823a26a6369f09
artifacts/dirac16complex/arbitrary-field/stage1-summary.json
  a65972b5a52f947d9bee9f67e09f7151fff617c03f496ba313e07db168c10770
artifacts/dirac16complex/arbitrary-field/algebra-fixture.json
  8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b
wolfram/Dirac16ComplexAlgebra.wl
  ba0d00c818fa3707f04f7b2a7478b0c635fbf9fdaaa08b2e036d2704180f2262
scripts/verify_dirac16complex_algebra.wls
  86904ac07e1237cf0dec14431a3707d7bf24f951e12def504705d331c934949a
wolfram/Dirac16ComplexGeometry.wl
  f5b674665eee4000750161e6ab6312c38bfac9da7a17450a2b3bdd88ef292af2
scripts/verify_dirac16complex_geometry.wls
  81b1b0febf1a5d6956f042179dff4eed949718cc15955e0753c71606f3f09953
scripts/d16c_exact.py
  eb2fcbe498b6ae927df61f73abcee4e58c319984fb8f6e1b28defcd0ca13a3f5
scripts/build_dirac16complex_fixture.py
  585051a6b2e01ab1d8ae92ae5e1949c4d0c23e37815332c44dc5af525a36d776
scripts/check_dirac16complex_algebra.py
  3d2fd639b655491897b68f8719db3618d638248b2b1176f22668723e273bea12
scripts/d16c_geometry_sympy.py
  4f7eca4cf247354650ed9beb0b9c46530d14c9965f095979ea5ee24651af9f25
scripts/check_dirac16complex_geometry.py
  ac26111ce6758cebdf473e943d1cd4f1e14f87e4961ee694623d888742824653
scripts/grassmann_algebra.py
  dfce851d3dc7ab82202a62d414cc259644a64a101f08e9ba80ed747faa8bc24c
scripts/demo_grassmann_lagrangians.py
  3053c7011037e29cd9efa7c2067aafd23ebc67c6156eb581fef184810ef1515a
dirac-main/artifacts/exact/cl44-seed.json
  52e7a73b14467435d7986b33bf29547510b321853ffbd76121896d70b796d133
dirac-main/artifacts/exact/split-octonion.json
  cbc28db6709ec1fc35ccfcc26353d1952b42bb516f6c50d6a52e2d6d355be710
dirac-main/artifacts/exact/triality44.json
  a8c31c07809fc884ae0495d91f4105fac0909c954bb185c643306c57699cd395
```

## 12. Reproduction

Run every command from the repository root. The Wolfram report path is a plain positional argument: WolframScript 1.14 drops "--" and every argument after it when it is combined with -file. The gates set PYTHONUTF8=1 for their own process; set it yourself for single steps, because Python output contains Greek letters.

### 12.1 PowerShell

The Stage-1 gate runs all eleven steps through the logging wrapper scripts/run_logged.ps1, with the logs in build/logs/, and then audits the five reports and the cross-implementation checks:

```
pwsh -NoProfile -File scripts/verify_stage1_arbitrary_field.ps1
```

Its last line is

```
stage1_arbitrary_field_verification=OK
```

The individual steps:

```
$env:PYTHONUTF8 = "1"
$a = "artifacts/dirac16complex/arbitrary-field"
python scripts/build_dirac16complex_fixture.py
python scripts/check_dirac16complex_algebra.py --wolfram-report=
wolframscript -file scripts/verify_dirac16complex_algebra.wls `
    "$a/wolfram-algebra-report.json"
wolframscript -file scripts/verify_dirac16complex_geometry.wls `
    "$a/wolfram-geometry-report.json"
python scripts/check_dirac16complex_geometry.py --wolfram-report `
    "$a/wolfram-geometry-report.json"
python scripts/demo_grassmann_lagrangians.py
python scripts/check_dirac16complex_algebra.py --wolfram-report `
    "$a/wolfram-algebra-report.json"
python -m unittest discover -s tests -p "test_d16c_[ag]*.py" -v
python -m unittest discover -s tests -p "test_publication_tooling.py" -v
python scripts/build_stage1_summary.py --output "$a/stage1-summary.json"
python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md
```

### 12.2 Git Bash

The Git Bash twin runs the same steps through scripts/run_logged.sh and ends with the same line:

```
bash scripts/verify_stage1_arbitrary_field.sh
```

The individual steps:

```
export PYTHONUTF8=1
a=artifacts/dirac16complex/arbitrary-field
python scripts/build_dirac16complex_fixture.py
python scripts/check_dirac16complex_algebra.py --wolfram-report=
wolframscript -file scripts/verify_dirac16complex_algebra.wls \
    "$a/wolfram-algebra-report.json"
wolframscript -file scripts/verify_dirac16complex_geometry.wls \
    "$a/wolfram-geometry-report.json"
python scripts/check_dirac16complex_geometry.py --wolfram-report \
    "$a/wolfram-geometry-report.json"
python scripts/demo_grassmann_lagrangians.py
python scripts/check_dirac16complex_algebra.py --wolfram-report \
    "$a/wolfram-algebra-report.json"
python -m unittest discover -s tests -p "test_d16c_[ag]*.py" -v
python -m unittest discover -s tests -p "test_publication_tooling.py" -v
python scripts/build_stage1_summary.py --output "$a/stage1-summary.json"
python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md
```

Each verifier prints check_count and failed_check_count and exits nonzero if a check fails. The first algebra step runs without the Wolfram comparison (--wolfram-report= with an empty value), because the Wolfram report on disk may predate the run; the second one compares with the report just written. The PDF step builds this document twice (two builder runs, three pdflatex passes each), requires warning-free logs and byte-identical PDFs, and compares the result with the registered edition dirac16complex-arbitrary-field in provenance/pdf-specifications.json. After an edit of this document the edition is registered again with

```
python scripts/build_provenance_pdf.py --register \
    provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md
```

(in PowerShell the line continuation is a backtick instead of the backslash), and the sha256 pins in tests/test_d16c_arbitrary_field_publication.py are updated.

## 13. Limitations

1. The general statements of Sections 5 to 9 are proved by the arguments given here and checked exactly at test points: three points of one generic non-diagonal vielbein (G1), the primordial family (G2, symbolic in Python) and three times of a diagonal frame (G3). The checks are not a symbolic verification for every vielbein.
2. The metric variation of the action is carried out explicitly only for diagonal metrics. The off-diagonal components of $T_{\mu\nu}$ are tested through symmetry, Hermiticity and on-shell conservation in G1, and through the homogeneous forms of $T_{ij}$ and $T_{4i}$.
3. Conservation of $T_{\mu\nu}$ is checked with on-shell jets at points, not as an off-shell Noether identity.
4. The energy-momentum, Lichnerowicz and invariance checks evaluate bilinears with commuting exact numbers, which is exact because $\Psi^\dagger$ is always on the left and $\Psi$ on the right; the field equations, the canonical momentum and Lg[] are checked in genuine Grassmann algebras.
5. The Dirac-bracket computation, the Hamiltonian density, the Heisenberg equations, the mode expansion, the Fock space and the expectation-value rule of Section 10 are derivations; only their algebraic ingredients (Results 10.1 to 10.6) are machine-checked.
6. The quantization is formal: the state space is a Krein space, the extra-time sector has complex frequencies, and no interacting theory, regularization or renormalization is constructed.
7. The homogeneous-sector formulas treat bilinears as classical mean-field quantities; the quantum expectation values of Section 10.11 are one-particle statements.
8. The signature (4,4) is not observed spacetime, and nothing here is compared with data. The connection to dark energy or dark matter, and the stability of solutions, are not decided in this document.
9. The cross-checks against dirac-main's published fixtures need the git-ignored dirac-main folder; in a fresh clone these sub-checks record "not-run" (measurement referenceFilesPresent in wolfram-algebra-report.json).
