## 13. The Kohn–Sham approximation for dirac16complex in the primordial field

### 13.1 What this chapter computes, and the status of its numbers

This chapter applies the density functional theory of Chapter 12 to dirac16complex. The system is a finite number $N$ of dirac16complex quanta (particles above the Dirac sea, Chapter 8) held in the **static** member of the notebook's primordial gravitational field (Chapter 9), extended by the notebook's mirror construction, a **Z2 brane**. The quanta interact through the contact potential $U(S)=\tfrac\lambda2S^2$ of the Lagrangian (Chapter 6). We derive, step by step: the reduction of the 16-component field equation to eight copies of a $2\times2$ first-order system in one coordinate; the boundary conditions; exact solutions at zero momentum; the Hartree and the exact exchange energy of the contact interaction for the uniform gas, which gives a local density approximation without any fitted number; Mermin's finite-temperature Kohn–Sham functional and its equations; and the energy–momentum tensor of the resulting state. Then we report what the computer found: ground states, first excited states (Kohn–Sham gap, particle–hole list and Delta-SCF), thermodynamics, and the comparison with the source that Einstein gravity would need to produce the field.

**Sources.** The binding specification is `handoff/specs/STAGE4_SPEC.md`, including its errata E4.1 to E4.12 (its §7 to §9), which override its earlier text. The exact theory is `wolfram/Dirac16ComplexKohnSham.wl` with the verifier `scripts/verify_dirac16complex_kohn_sham.wls`, whose report `artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json` has 125 of 125 checks true, and the independent sympy checker `scripts/check_dirac16complex_kohn_sham_theory.py`, whose report `artifacts/dirac16complex/kohn-sham/python-theory-report.json` has 157 of 157 checks true. The exact formulas are collected in `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json`. Check names in typewriter type beginning with `KS_` are checks of these two reports. The numbers come from the Rust solver `studies/dirac16complex_kohn_sham` (its `README.md` describes the implementation), whose canonical outputs are under `artifacts/dirac16complex/kohn-sham/rust/`.

**Status of the numbers (read this first).** When this chapter was written, the Stage-4 cross-check against an independent Python reference solver (`scripts/ks_reference_solver.py` with the checker `scripts/check_dirac16complex_kohn_sham.py`) and the Stage-4 gate (`scripts/verify_stage4_kohn_sham.ps1` and `.sh`) were **still being completed**. An earlier quick cross-check passed 65 of its 69 checks (`handoff/reviews/stage4_crosscheck_quick_2026-09-30.log`); the four disagreements were diagnosed and fixed in the code (errata E4.8 to E4.12), and the reruns were in progress. Every number below is therefore **as computed by the Rust solver**, verified by the solver's own checks: all checks of the five subcommands pass (33 in `spectrum`, 137 in `scf`, 65 in `excited`, 102 in `thermo`, 60 in `emt`; the `summary.json` file of each subfolder), a repeated run is byte-identical in all 327 files compared, and a run with ten times tighter tolerances agrees to $6.0\times10^{-8}$ relative in every energy (`rust/determinism-report.json`). Where the cross-check was still open (one Delta-SCF value, Section 13.12) we say so at the number.

**What is not done here.** The metric is a fixed background: the quanta do not act back on it. The Kohn–Sham state is a static mean-field state with the exact exchange of the uniform gas and **no correlation energy** (Section 13.8 explains why). No claim is made that such a state existed in any universe.

**Units and conventions.** $H=1$ (the notebook's inverse length); the mass is $m=1$ or $m=3$ in these units, and energies, momenta and temperatures are quoted in units of $m$. The coupling is given as the dimensionless $\hat\lambda=\lambda m^6$. Coordinates are $x_0,\dots,x_7$ with $x_4$ the time, $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$, the gammas are the notebook's $\gamma^a$ (Chapter 2), $C=\gamma^0\gamma^1\gamma^2\gamma^3$, $\bar\Psi=\Psi^\dagger C$, and $B=-iC\gamma^4$ (Chapter 8). The letter $l$ is used as an index for the 3-space directions, $l\in\{1,2,3\}$; the letter $j$ is reserved for the block type of Section 13.4.

### 13.2 The static primordial field, the hidden coordinate and the brane

**The static field.** The notebook's primordial metric (Chapter 9) contains a free function $a_4(t)$ of the time $t=Hx_4$. A stationary ground state needs a metric that does not change in time, so Stage 4 takes the **static member** $a_4=a_{4,0}$, a constant ($a_4'=a_4''=0$).

**The hidden coordinate $y$.** With $z=6Hx_0\in(0,\pi/2)$ define

$$
y=\frac{\ln\sin z}{6H}\in(-\infty,0],\qquad \sin z=e^{6Hy},\qquad dy=\cot z\,dx_0 .
$$

(Differentiate: $dy/dx_0=\frac1{6H}\cdot\frac{\cos z}{\sin z}\cdot6H=\cot z$.) Then $g_{00}\,dx_0^2=\cot^2z\,dx_0^2=dy^2$ and $(\sin z)^{1/3}=e^{2Hy}$, and the line element of Chapter 9 becomes the **warped form**

$$
ds^2=dy^2-dx_4^2+e^{2Hy}\Bigl[e^{2a_{4,0}}\bigl(dx_1^2+dx_2^2+dx_3^2\bigr)-e^{-2a_{4,0}}\bigl(dx_5^2+dx_6^2+dx_7^2\bigr)\Bigr].
$$

The factor $W(y)=e^{Hy}$ is the **warp**. The square root of the determinant is the product of the eight scale factors, $\sqrt{|g|}=(e^{Hy+a_{4,0}})^3\cdot1\cdot1\cdot(e^{Hy-a_{4,0}})^3=W^6=e^{6Hy}$ (`KS_geometry_sqrtDetG_W6`): the proper 7-volume per unit coordinate volume. It tends to 0 as $y\to-\infty$ ($z\to0$), where the transverse space pinches off; we call this end the **tip**. The notebook's coordinate patch ends at $y=0$ ($z=\pi/2$), where $\cot z=0$ and the $x_0$ chart degenerates, although the $y$ form of the metric is regular there.

**Curvature and the required source.** Setting $a_4'=a_4''=0$ in the curvature of Chapter 9, $R=6H^2(a_4'^2-7)$, $G^0{}_0=-3H^2(a_4'^2-5)$, $G^1{}_1=G^2{}_2=G^3{}_3=H^2(15-3a_4'^2+a_4'')$, $G^4{}_4=3H^2(7+a_4'^2)$ and $G^5{}_5=G^6{}_6=G^7{}_7=H^2(15-3a_4'^2-a_4'')$, gives

$$
R=-42H^2,\qquad G^\mu{}_\nu=\mathrm{diag}(15,15,15,15,21,15,15,15)\,H^2
$$

in the order $(y,x_1,x_2,x_3,x_4,x_5,x_6,x_7)$ (`KS_geometry_ricciScalarMinus42H2`, `KS_geometry_einsteinMixedDiag`). There is a short way to see this. The seven directions other than $x_4$ form a space of constant curvature $-H^2$ (`KS_geometry_constantCurvatureSevenSpace`), for which $R_{\mu\nu}=-(7-1)H^2g_{\mu\nu}=-6H^2g_{\mu\nu}$, while the time $x_4$ is flat, $R^4{}_4=0$. So $R=7\cdot(-6H^2)=-42H^2$, and $G^\mu{}_\nu=R^\mu{}_\nu-\tfrac12\delta^\mu{}_\nu R$ is $-6H^2+21H^2=15H^2$ on the seven directions and $0+21H^2=21H^2$ on $x_4$. If 8-dimensional Einstein gravity $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ produced this field, the source would have to be (erratum E4.3; `KS_geometry_requiredSource`, `KS_geometry_rhoRequiredNegative`)

$$
\rho_{\text{req}}=-T^4{}_4=-\frac{21H^2}\kappa<0,\qquad p_{\text{req}}=T^\mu{}_\mu=+\frac{15H^2}\kappa\quad(\text{all seven }\mu\ne4),\qquad w_{\text{req}}=-\frac57 .
$$

A **negative** energy density is required. Section 13.14 compares this with the Kohn–Sham state.

**Extrinsic curvature.** A surface $y=\text{const}$ with the unit normal $\partial_y$ has the extrinsic curvature $K_{\mu\nu}=\tfrac12\partial_yg_{\mu\nu}$. For the six warped directions $g_{\mu\mu}=\pm e^{2Hy\pm2a_{4,0}}$, so $K_{\mu\mu}=Hg_{\mu\mu}$ (no sum) and $K^\mu{}_\nu=H\,\delta^\mu{}_\nu$ there, while $K^4{}_4=0$; the trace is $K=6H$ (`KS_geometry_extrinsicCurvature`).

**The Z2 brane.** The notebook's hypothesis speaks of a pair of universes. Stage 4 realizes a geometric version of it (extension E2 of the specification): two copies of the patch $y\le0$ glued at $y=0$, with the warp $W=e^{-H|y|}$ on both sides. The surface $y=0$ is then a **brane**, a wall at which the extrinsic curvature jumps. With the normal $n=+\partial_y$ pointing from $y<0$ to $y>0$, $K^\mu{}_\mu(0^-)=+H$ and $K^\mu{}_\mu(0^+)=-H$ (no sum) on the six warped directions, so the jump $[X]=X(0^+)-X(0^-)$ is $[K^\mu{}_\mu]=-2H$ there, $0$ on $x_4$, and $[K]=6\cdot(-2H)=-12H$. The **Israel junction condition**, with the convention $[K_{\mu\nu}]-h_{\mu\nu}[K]=-\kappa S_{\mu\nu}$ ($h_{\mu\nu}$ the induced metric of the brane, $S_{\mu\nu}$ the stress carried by the brane, $\mu,\nu\ne y$), gives

$$
\begin{aligned}
&S^\mu{}_\nu=-\frac1\kappa\bigl([K^\mu{}_\nu]-\delta^\mu{}_\nu[K]\bigr):\\
&S^\mu{}_\mu=-\frac{-2H+12H}\kappa=-\frac{10H}\kappa\ \ (\text{six warped directions}),\qquad S^4{}_4=-\frac{0+12H}\kappa=-\frac{12H}\kappa ,
\end{aligned}
$$

so the brane carries the energy density $\rho_{\text{brane}}=-S^4{}_4=+12H/\kappa>0$ and the pressures $-10H/\kappa$ (`KS_geometry_israelJump`, `KS_geometry_israelStress`, `KS_geometry_braneEnergyPositive`; the same convention gives the Randall–Sundrum brane a positive tension, `KS_geometry_israelConventionRandallSundrum`). This is a statement about what the glued geometry would need; the chapter does not derive that such a brane exists. On the $y>0$ side the field equation below has the same form with $y\to-y$, so the Kohn–Sham problem is solved on $y\in[-L,0]$ with boundary conditions at the brane (Section 13.5).

### 13.3 The stationary ansatz and the reduced equation

**The field equation.** In the mean field the quanta obey the Dirac equation of Chapter 7 with an effective mass: $\gamma^\mu D_\mu\Psi=M_{\text{eff}}\Psi$, where $M_{\text{eff}}=m+\lambda S$ at the Hartree level (Section 13.8 adds the exchange). We work in the **good sector**: $\Psi$ does not depend on the extra times $x_5,x_6,x_7$. Modes with momentum along the extra times have a non-Hermitian single-particle operator and grow without bound (Chapter 8), so they are excluded.

**The pieces of the Dirac operator.** The vielbein is diagonal, with the entries (in the order $y,x_1,\dots,x_7$)

$$
h=\bigl(1,\ e^{Hy+a_{4,0}},\ e^{Hy+a_{4,0}},\ e^{Hy+a_{4,0}},\ 1,\ e^{Hy-a_{4,0}},\ e^{Hy-a_{4,0}},\ e^{Hy-a_{4,0}}\bigr),
$$

so the curved gammas are $\gamma^y=\gamma^0$, $\gamma^{x_l}=e^{-Hy-a_{4,0}}\gamma^l$ for $l=1,2,3$, $\gamma^{x_4}=\gamma^4$, and $\gamma^{x_l}=e^{-Hy+a_{4,0}}\gamma^l$ for $l=5,6,7$. The spin connection enters only through the contraction $\gamma^\mu\Omega_\mu$ (Chapters 4 and 9). For a diagonal vielbein that depends on one coordinate only, the formula of Chapter 4, $\gamma^\mu\Omega_\mu=\tfrac12\sum_b\frac1{h_b}\,\partial_b\ln\bigl(\prod_{c\ne b}h_c\bigr)\gamma^b$, has a single term, $b=y$, and $\prod_{c\ne y}h_c=e^{6Hy}$:

$$
\gamma^\mu\Omega_\mu=\tfrac12\,\partial_y(6Hy)\,\gamma^0=3H\gamma^0
$$

(`KS_reduction_gammaSlashOmega3Hgamma0`).

**The ansatz.** Stationary in time with frequency $\varepsilon$, a plane wave with 3-momentum $\mathbf k=(k_1,k_2,k_3)$ along 3-space, and a factor that will cancel the spin connection:

$$
\Psi=e^{-i\varepsilon x_4}\,e^{i\mathbf k\cdot\mathbf x}\,W(y)^{-3}\,\chi(y),\qquad W^{-3}=e^{-3Hy},
$$

with $\chi(y)$ a column of 16 complex functions of $y$ alone. Now compute each term. $\partial_y\bigl(e^{-3Hy}\chi\bigr)=e^{-3Hy}(\chi'-3H\chi)$, so $\gamma^0\partial_y\Psi+3H\gamma^0\Psi$ equals the common factor $e^{-i\varepsilon x_4}e^{i\mathbf k\cdot\mathbf x}e^{-3Hy}$ times $\gamma^0\chi'$: the $-3H$ from the derivative cancels the $+3H$ of the spin connection. The time derivative gives $\gamma^4\partial_4\to-i\varepsilon\gamma^4$ and the 3-space derivatives give $\gamma^{x_l}\partial_l\to ik_le^{-Hy-a_{4,0}}\gamma^l$. Dividing by the common factor,

$$
\gamma^0\chi'+i\kappa(y)\sum_{l=1}^3k_l\gamma^l\chi-i\varepsilon\gamma^4\chi=M_{\text{eff}}(y)\,\chi,\qquad \kappa(y)=e^{-Hy-a_{4,0}}
$$

(`KS_reduction_ansatzRemoves3H`, `KS_reduction_reducedEquationODEForm`; without the factor $W^{-3}$ the term $3H\gamma^0$ would survive, `KS_reduction_withoutW3the3HTermSurvives`). Multiplying by $\gamma^0$, whose square is $+1$ because $\eta^{00}=+1$, gives an ordinary differential equation for $\chi$:

$$
\chi'=\gamma^0\Bigl[M_{\text{eff}}\chi-i\kappa\sum_{l=1}^3k_l\gamma^l\chi+i\varepsilon\gamma^4\chi\Bigr].
$$

**Three properties.** (i) **Flat measure.** $\sqrt{|g|}\,\Psi^\dagger\Psi=e^{6Hy}e^{-6Hy}\chi^\dagger\chi=\chi^\dagger\chi$, so an orbital is normalized by $\int_{-L}^0\chi^\dagger\chi\,dy=1$ with the ordinary measure $dy$ (`KS_reduction_flatMeasure`). (ii) **Confinement.** The momentum enters with the weight $\kappa(y)=e^{-Hy-a_{4,0}}$, which grows toward the tip: a given momentum costs more energy far from the brane, which pushes the quanta toward $y=0$. (iii) **The constant $a_{4,0}$ is a rescaling.** It appears only in $\kappa$, as $k\,e^{-a_{4,0}}$ (`KS_reduction_a4IsMomentumRescaling`); the canonical runs use $a_{4,0}=0$, and Section 13.15 checks the equivalence numerically.

**Choosing the direction of $\mathbf k$.** Rotations of $(x_1,x_2,x_3)$ are symmetries, so the spectrum depends only on $k=|\mathbf k|$ (`KS_reduction_rotationalSymmetry`), and we take $\mathbf k=(k,0,0)$. Then only $\gamma^0$, $\gamma^1$ and $\gamma^4$ appear:

$$
\chi'=\bigl[M_{\text{eff}}\,A_0-i\kappa k\,A_1+i\varepsilon A_4\bigr]\chi,\qquad A_0=\gamma^0,\quad A_1=\gamma^0\gamma^1,\quad A_4=\gamma^0\gamma^4 .
$$

On the mirror side $y>0$ of the Z2 geometry the same equation holds with $\kappa(y)=e^{Hy-a_{4,0}}$: $\kappa$ is an even function of $y$ (`KS_reduction_mirrorPatchSameForm`).

### 13.4 Eight $2\times2$ blocks

The reduced equation still couples 16 components. This section shows that a fixed change of basis splits it into eight independent systems of two components each, and computes them exactly.

**Two rules for products of gamma matrices.** Let $P=\gamma^{a_1}\gamma^{a_2}\cdots\gamma^{a_k}$ be a product of $k$ different frame gammas. Moving one gamma $\gamma^c$ from the left of $P$ to its right, it passes each factor once; it anticommutes with every factor $\gamma^{a}\ne\gamma^c$ and commutes with itself. Hence

$$
\gamma^cP=(-1)^{k-1}P\gamma^c\ \ \text{if }\gamma^c\text{ is a factor of }P,\qquad
\gamma^cP=(-1)^{k}P\gamma^c\ \ \text{if it is not}.
$$

Reversing the order of the $k$ factors needs $k(k-1)/2$ swaps, so $P^2=(-1)^{k(k-1)/2}\,(\gamma^{a_1})^2\cdots(\gamma^{a_k})^2$, where $(\gamma^a)^2=\eta^{aa}=+1$ for $a\le3$ and $-1$ for $a\ge4$.

**The algebra of the equation.** With these rules: $A_0^2=(\gamma^0)^2=1$; $A_1^2=(\gamma^0\gamma^1)^2=(-1)^1\cdot1\cdot1=-1$; $A_4^2=(\gamma^0\gamma^4)^2=(-1)\cdot1\cdot(-1)=+1$; and the three matrices anticommute pairwise (for example $A_0A_1=\gamma^1$ while $A_1A_0=\gamma^0\gamma^1\gamma^0=-\gamma^1$). Three pairwise anticommuting matrices with squares $+1,-1,+1$ generate a Clifford algebra of signature (2,1), whose dimension is 8 (`KS_reduction_algebraDim8`).

**Three commuting labels.** Define

$$
J=\gamma^0\gamma^1\gamma^4,\qquad K_1=\gamma^2\gamma^3,\qquad K_2=\gamma^5\gamma^6 .
$$

By the first rule, $J$ ($k=3$) commutes with its own factors $\gamma^0,\gamma^1,\gamma^4$ and anticommutes with the other five gammas; $K_1$ ($k=2$) anticommutes with $\gamma^2,\gamma^3$ and commutes with the other six; $K_2$ anticommutes with $\gamma^5,\gamma^6$ and commutes with the other six. Therefore all three commute with $A_0$, $A_1$, $A_4$ (products of $\gamma^0,\gamma^1,\gamma^4$), with $C=\gamma^0\gamma^1\gamma^2\gamma^3$ (for $J$ the two anticommuting factors $\gamma^2,\gamma^3$ give two signs, which cancel) and with $B=-iC\gamma^4$, and they commute with each other (`KS_reduction_JK1K2commute`). By the second rule, $J^2=(-1)^3\cdot(1\cdot1\cdot(-1))=+1$, $K_1^2=(-1)\cdot1\cdot1=-1$ and $K_2^2=(-1)\cdot(-1)(-1)=-1$. So $J$ has the eigenvalues $j=\pm1$, and $K_1$, $K_2$ have the eigenvalues $i s_2$, $i s_3$ with $s_2,s_3=\pm1$.

**The projectors have rank 2.** The joint eigenspace with labels $(j,s_2,s_3)$ is the range of

$$
P(j,s_2,s_3)=\frac{1+jJ}2\cdot\frac{1-is_2K_1}2\cdot\frac{1-is_3K_2}2 .
$$

(On a vector with $K_1v=is_2v$ the middle factor gives $(1-is_2\cdot is_2)/2=1$, on one with $K_1v=-is_2v$ it gives 0; likewise for the other two factors.) Multiplying out, $P$ is $\tfrac18$ times the sum of $1$ and seven products of distinct gammas, $J$, $K_1$, $K_2$, $JK_1$, $JK_2$, $K_1K_2$, $JK_1K_2$ (with coefficients). Each of these seven anticommutes with some $\gamma^c$ by the first rule: $J$, $K_1$, $JK_2$ and $K_1K_2$ with $\gamma^2$; $K_2$ and $JK_1$ with $\gamma^5$; and $JK_1K_2$, which contains every gamma except $\gamma^7$, with $\gamma^7$. A matrix $X$ that anticommutes with an invertible $\gamma^c$ is traceless: $\mathrm{tr}\,X=\mathrm{tr}\bigl(\gamma^cX(\gamma^c)^{-1}\bigr)=-\mathrm{tr}\,X$. Hence $\mathrm{tr}\,P=\tfrac18\,\mathrm{tr}\,1=16/8=2$: each of the eight label combinations has a 2-dimensional eigenspace (`KS_reduction_projectorsRank2`), and the eight spaces together fill $\mathbb C^{16}$.

**The basis in each block.** Inside one block the matrices $A_0,A_1,A_4$ still satisfy the algebra above. $A_1$ anticommutes with $A_0$ and is invertible, so it maps the $A_0=+1$ eigenvector to an $A_0=-1$ eigenvector; each eigenvalue of $A_0$ therefore occurs once in the block. Choose $v_+$ with $A_0v_+=v_+$ and set $v_-=A_1v_+$. Then $A_0v_-=A_0A_1v_+=-A_1A_0v_+=-v_-$, $A_1v_+=v_-$ and $A_1v_-=A_1^2v_+=-v_+$. In the basis $(v_+,v_-)$, with the Pauli matrices $\sigma_1,\sigma_2,\sigma_3$ of Chapter 2,

$$
A_0\to\sigma_3,\qquad A_1\to\begin{pmatrix}0&-1\\1&0\end{pmatrix}=-i\sigma_2 .
$$

$A_4$ anticommutes with $\sigma_3$, so it is off-diagonal, and it is fixed by one product: $A_0A_1A_4=\gamma^0(\gamma^0\gamma^1)(\gamma^0\gamma^4)=\gamma^1\gamma^0\gamma^4=-J$, which is the number $-j$ in the block. Since $\sigma_3(-i\sigma_2)=-i\sigma_3\sigma_2=-i(-i\sigma_1)=-\sigma_1$, the condition $-\sigma_1A_4=-j$ gives $A_4\to j\sigma_1$ (`KS_reduction_blocksA0A1A4`). The same way we get the matrices of the expectation-value rule. $C=\gamma^0\gamma^1\gamma^2\gamma^3=A_1K_1\to(-i\sigma_2)(is_2)=s_2\sigma_2$. Moving $\gamma^4$ to the right past $\gamma^2\gamma^3$ (two swaps) shows $JK_1=\gamma^0\gamma^1\gamma^2\gamma^3\gamma^4=C\gamma^4$, so $B=-iC\gamma^4=-iJK_1\to-i\,j\,(is_2)=js_2$, a number. Then

$$
C\to s_2\sigma_2,\qquad B\to js_2,\qquad BC\to j\sigma_2,\qquad \gamma^4\gamma^1\to-j\sigma_3
$$

(`KS_reduction_blocksBC`; for the last one $\gamma^4=A_0A_4\to ij\sigma_2$ and $\gamma^1=A_0A_1\to-\sigma_1$).

**A concrete block.** The exact theory builds the basis as $v_+=8P(j,s_2,s_3)\tfrac12(1+\gamma^0)e_c$ with the first standard unit vector $e_c$ that gives a nonzero result, and $v_-=\gamma^0\gamma^1v_+$; every entry is $0$, $\pm1$ or $\pm i$, and $|v_\pm|^2=8$. For the block $(j,s_2,s_3)=(1,1,1)$ ($c=4$, counting components from 0):

$$
\begin{aligned}
v_+&=(0,0,0,0,\,1,i,-1,i,\,0,0,0,0,\,1,i,-1,i)^T,\\
v_-&=(i,-1,-i,-1,\,0,0,0,0,\,-i,1,i,1,\,0,0,0,0)^T .
\end{aligned}
$$

With the gammas of the fixture `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` one checks $\gamma^0v_+=v_+$, $Jv_+=v_+$, $K_1v_+=iv_+$, $K_2v_+=iv_+$ and $Bv_+=v_+$ (the Krein sign $js_2=1$ of this block), and that the $2\times2$ matrices in the normalized basis $(v_+,v_-)/\sqrt8$ are exactly the ones above with $j=s_2=1$. All eight blocks are listed in `kohn-sham-theory.json` (keys `reduction`, `blockDiagonalisation`); the $16\times16$ matrix with the columns $v_\pm/\sqrt8$ is unitary and makes $A_0,A_1,A_4,B,C$ block diagonal (`KS_reduction_basisUnitary`, `KS_reduction_fiveMatricesBlockDiagonal`, `KS_reduction_reconstructFromBlocks`).

![Moduli of the matrix entries of the $y$-current matrix $\gamma^0\gamma^4$ in the original spinor basis (left) and in the block basis (middle), and of the operator of the reduced equation in the block basis at one sample point (right): eight $2\times2$ blocks along the diagonal (figure `block_structure.png` of `artifacts/dirac16complex/kohn-sham/figures`).](artifacts/dirac16complex/kohn-sham/figures/block_structure.png)

**Two types of block.** For the $y$ equation only $A_0,A_1,A_4$ matter, and their block forms depend on $j$ alone: there are **two inequivalent block types**, $j=+1$ (four blocks) and $j=-1$ (four blocks) (`KS_reduction_blockTypes`, erratum E4.4). Including $B$ and $C$ there are four types $(j,s_2)$ of two blocks each. The chirality $\gamma^8$ anticommutes with $J$ (a product of three gammas) and commutes with $K_1,K_2$, so it maps the block $(j,s_2,s_3)$ onto $(-j,s_2,s_3)$ (`KS_reduction_gamma8SwapsJ`); this is the seed of the pairing of Section 13.14 and Chapter 15.

**Convention of the Rust code.** The Rust module `studies/dirac16complex_kohn_sham/src/blocks.rs` labels its blocks by the eigenvalue $s$ of $A_0A_1A_4$, which is $-J$; hence $s=-j$ (recorded as the label relation in `rust/spectrum/theory-agreement.json`), and its block forms read $A_4\to-s\sigma_1$, $BC\to-s\sigma_2$. The two descriptions are identical; this book uses $j$ throughout and converts the Rust labels.

### 13.5 The block equation, its Hamiltonian, the current and the boundary conditions

**The block equation.** In a block of type $j$, with $\chi=(\chi_1,\chi_2)^T$ the two components in the basis $(v_+,v_-)$ and with the exchange potential $v(y)$ of Section 13.8 included ($\varepsilon\to\varepsilon-v$),

$$
\chi'=N\chi,\qquad N=M_{\text{eff}}(y)\,\sigma_3-\kappa(y)\,k\,\sigma_2+ij\bigl(\varepsilon-v(y)\bigr)\sigma_1
$$

(`KS_reduction_blockODEMatrix`), since $-i\kappa k(-i\sigma_2)=-\kappa k\sigma_2$. In components,

$$
\chi_1'=M_{\text{eff}}\chi_1+i\bigl(\kappa k+jE\bigr)\chi_2,\qquad \chi_2'=-M_{\text{eff}}\chi_2+i\bigl(jE-\kappa k\bigr)\chi_1,\qquad E=\varepsilon-v .
$$

Writing $\chi=(a,\,ib)$ with real $a,b$ makes the system real:

$$
a'=M_{\text{eff}}\,a-(jE+\kappa k)\,b,\qquad b'=(jE-\kappa k)\,a-M_{\text{eff}}\,b .
$$

(With the Rust label $s=-j$ this is the system $a'=Ma+(sE-\kappa k)b$, $b'=-(sE+\kappa k)a-Mb$ printed in `blocks.rs`.)

**The Hamiltonian form.** The same equation is an eigenvalue problem $h_j\chi=\varepsilon\chi$ with

$$
h_j=j\Bigl[-i\sigma_1\frac d{dy}+M_{\text{eff}}(y)\,\sigma_2+\kappa(y)\,k\,\sigma_3\Bigr]+v(y).
$$

To see it, write $h_j\chi=\varepsilon\chi$ as $-i\sigma_1\chi'=jE\chi-M_{\text{eff}}\sigma_2\chi-\kappa k\sigma_3\chi$ (using $j^2=1$) and multiply by $i\sigma_1$: with $\sigma_1\sigma_2=i\sigma_3$ and $\sigma_1\sigma_3=-i\sigma_2$ one gets $\chi'=ijE\sigma_1\chi+M_{\text{eff}}\sigma_3\chi-\kappa k\sigma_2\chi$, the block equation (`KS_reduction_blockHamiltonianEquivalentToODE`).

**Symmetries of the spectrum.** Write $h_j-v=jD_k$ with $D_k=-i\sigma_1\,d/dy+M_{\text{eff}}\sigma_2+\kappa k\sigma_3$, which does not depend on $j$. Two facts follow. (i) $h_{-1}-v=-(h_{+1}-v)$: the two block types carry opposite spectra of $h-v$ (`KS_reduction_hMinusEqualsMinusHPlus`); when $v=0$ the spectrum of $j=-1$ is the negative of that of $j=+1$. (ii) Conjugation with $\sigma_3$ gives $\sigma_3D_k\sigma_3=+i\sigma_1\,d/dy-M_{\text{eff}}\sigma_2+\kappa k\sigma_3=-D_{-k}$, and the boundary conditions below are unchanged by $\chi\to\sigma_3\chi$. Hence the orbital $\sigma_3\chi$ of $(-k,-j)$ has the same energy and the same $|\chi|^2$ as the orbital $\chi$ of $(k,j)$ (`KS_reduction_sigma3ConjugationFlipsK`). So at a fixed momentum $\mathbf k=(k,0,0)$ every level is 4-fold (the four blocks of one type), and over a closed shell of momenta $\{\mathbf k,-\mathbf k,\dots\}$ and at $k=0$ the levels are 8-fold (erratum E4.4).

**The $y$-current.** The current of the U(1) charge along the hidden direction is $J^y=-i\bar\Psi\gamma^y\Psi=-i\Psi^\dagger C\gamma^0\Psi$. By the expectation-value rule of Section 13.7 its matrix is $B(-iC\gamma^0)=-iBC\gamma^0=-i(-i\gamma^4)\gamma^0=-\gamma^4\gamma^0=\gamma^0\gamma^4=A_4$, which is $j\sigma_1$ in the block (erratum E4.5; `KS_boundary_currentMatrix`, `KS_boundary_currentBlockForm`). The current density of an orbital is proportional to $\chi^\dagger\sigma_1\chi=2\,\mathrm{Re}(\chi_1^*\chi_2)$. It is **constant in $y$** for every solution: $\frac d{dy}(\chi^\dagger\sigma_1\chi)=\chi^\dagger(N^\dagger\sigma_1+\sigma_1N)\chi$, and with $N^\dagger=M_{\text{eff}}\sigma_3-\kappa k\sigma_2-ijE\sigma_1$ (real $M_{\text{eff}}$, $\kappa$, $k$, $E$) the anticommutation of the Pauli matrices gives $N^\dagger\sigma_1+\sigma_1N=M_{\text{eff}}\{\sigma_3,\sigma_1\}-\kappa k\{\sigma_2,\sigma_1\}+ijE(\sigma_1\sigma_1-\sigma_1\sigma_1)=0$ (`KS_boundary_currentConservedAlongY`). The plain density $\chi^\dagger\chi$, in contrast, is not constant in $y$ (`KS_boundary_hilbertNormNotConservedAlongY`).

**Boundary conditions at the brane.** On the Z2 geometry one asks $\Psi(-y)=\pm\gamma^0\Psi(y)$, which at $y=0$ means $(1\mp\gamma^0)\chi(0)=0$; since $\gamma^0=A_0=\sigma_3$ in every block,

$$
\text{parity }+:\ \chi_2(0)=0\ \ (b(0)=0),\qquad \text{parity }-:\ \chi_1(0)=0\ \ (a(0)=0)
$$

(`KS_boundary_parityProjectorsBlockForm`). Either condition kills the current at the brane, because $\chi^\dagger\sigma_1\chi=2\mathrm{Re}(\chi_1^*\chi_2)$ vanishes when one component vanishes (`KS_boundary_parityKillsCurrent`). A caution from the exact theory (erratum E4.6): the reflection $\chi(y)\to\gamma^0\chi(-y)$ maps solutions with the mass function $M(y)$ onto solutions with $-M(-y)$ (use $\sigma_3\sigma_{1,2}\sigma_3=-\sigma_{1,2}$ and the evenness of $\kappa$), so it is a **symmetry** only when the mass function is odd, which is the case of a $\pm M$ mirror pair (`KS_boundary_parityA_symmetryIffMassOdd`). For an even mass function (an identical mirror copy) the symmetry is instead $\chi(y)\to i\gamma^0\gamma^8\chi(-y)$, which couples the blocks $j$ and $-j$ (`KS_boundary_parityB_symmetryForEvenMass`, `KS_boundary_parityB_couplesJBlocks`). The Kohn–Sham problem therefore uses the two parities as **boundary conditions** at $y=0$ and computes both; it does not assume a reflection symmetry.

**Boundary condition at the tip.** At the cutoff $y=-L$ the solver imposes the **bag condition** $\chi_2(-L)=0$ ($b(-L)=0$, equivalently $\gamma^0\chi(-L)=+\chi(-L)$). It is the member $\theta=0$ of the family $(1-Q(\theta))\chi(-L)=0$ with $Q(\theta)=\cos\theta\,\sigma_3+\sin\theta\,\sigma_2$ (`KS_boundary_bagFamily`, `KS_boundary_bagThetaZeroIsEvenParity`). Every member kills the current: $Q$ is Hermitian, $Q^2=1$ and $Q$ anticommutes with $\sigma_1$, so for $Q\chi=\chi$ we get $\chi^\dagger\sigma_1\chi=\chi^\dagger\sigma_1Q\chi=-\chi^\dagger Q\sigma_1\chi=-(Q\chi)^\dagger\sigma_1\chi=-\chi^\dagger\sigma_1\chi$, hence 0. The choice $\theta=0$ admits the brane zero mode of Section 13.6 for every $L$ and, for $M_{\text{eff}}>0$, no artificial mode localized at the cutoff (the header of `src/shooting.rs`). The tip is a genuinely singular end of the geometry ($W^6\to0$); the cutoff $L$ regularizes it, and the results are reported for $L=2,3,4$ (Section 13.15).

**Self-adjointness.** For two functions $\varphi,\chi$ on $[-L,0]$, integrating by parts,

$$
\langle\varphi|h_j\chi\rangle-\langle h_j\varphi|\chi\rangle=-ij\int_{-L}^0\bigl(\varphi^\dagger\sigma_1\chi'+\varphi'^\dagger\sigma_1\chi\bigr)dy=-ij\bigl[\varphi^\dagger\sigma_1\chi\bigr]_{-L}^{0}
$$

(the terms without derivatives cancel because $\sigma_2,\sigma_3$ and the real functions are Hermitian). If both functions satisfy the same condition at each end (one of the two components zero), then $\varphi^\dagger\sigma_1\chi=\varphi_1^*\chi_2+\varphi_2^*\chi_1=0$ there, and $h_j$ is self-adjoint (`KS_boundary_selfAdjointBoundaryTerm`). Consequently the levels $\varepsilon$ are real and the orbitals of different levels are orthogonal (Section 12.2).

### 13.6 Exact solutions at zero momentum and the brane band

Before any interaction, take $k=0$, a constant mass $M_{\text{eff}}=M>0$ and $v=0$. The block equation can then be solved by hand, and the results are the backbone of every numerical run.

**Eliminating one component.** From $\chi_2'=-M\chi_2+ij\varepsilon\chi_1$ we get $\chi_1=(\chi_2'+M\chi_2)/(ij\varepsilon)$ for $\varepsilon\ne0$. Inserting this into $\chi_1'=M\chi_1+ij\varepsilon\chi_2$ and multiplying by $ij\varepsilon$ gives $\chi_2''+M\chi_2'=M\chi_2'+M^2\chi_2+(ij)^2\varepsilon^2\chi_2$, that is

$$
\chi_2''=\bigl(M^2-\varepsilon^2\bigr)\chi_2 .
$$

**Parity $+$: the zero mode and the massive levels.** The conditions are $\chi_2(0)=0$ and $\chi_2(-L)=0$. (i) If $\varepsilon=0$, the equations decouple: $\chi_1'=M\chi_1$ and $\chi_2'=-M\chi_2$, and $\chi_2\equiv0$ satisfies both conditions. This is the **zero mode**

$$
\varepsilon=0,\qquad \chi=\bigl(e^{My},\,0\bigr)^T ,
$$

which grows toward $y=0$: it is **localized at the brane** (`KS_reduction_k0ZeroMode`). (ii) If $\varepsilon^2>M^2$, write $p^2=\varepsilon^2-M^2$; then $\chi_2''=-p^2\chi_2$ with $\chi_2(0)=\chi_2(-L)=0$ gives $\chi_2=\sin(py)$ with $pL=n\pi$, so

$$
\varepsilon=\pm\sqrt{M^2+(n\pi/L)^2},\qquad \chi_2=\sin\frac{n\pi y}L,\qquad \chi_1=\frac{M\sin(k_ny)+k_n\cos(k_ny)}{ij\varepsilon},\quad k_n=\frac{n\pi}L,
$$

$n=1,2,\dots$ (`KS_reduction_k0MassiveLevels`). (iii) If $0<\varepsilon^2\le M^2$, the solutions of $\chi_2''=(M^2-\varepsilon^2)\chi_2$ that vanish at both ends are zero, and then $\chi_2\equiv0$ forces $\varepsilon\chi_1=0$: no level. So at $k=0$ the parity-$+$ spectrum is exactly $\{0\}\cup\{\pm\sqrt{M^2+(n\pi/L)^2}\}$, each level 4-fold per block type, 8-fold in total.

**Worked example.** For $M=m=1$, $L=3$: $\sqrt{1+(\pi/3)^2}=1.447972$ and $\sqrt{1+(2\pi/3)^2}=2.320881$. The Rust solver lists the first of these as $1.447972$ (the $k=0$, parity-$+$ level with Prüfer index 1 in `rust/scf/m1_L3_N1016_lam0_T0/levels.csv`).

**Parity $-$.** Now $\chi_1(0)=0$ and $\chi_2(-L)=0$. The second condition gives $\chi_2=\sin\bigl(p(y+L)\bigr)$ with $p^2=\varepsilon^2-M^2$, and the first, via $\chi_1=(\chi_2'+M\chi_2)/(ij\varepsilon)$, becomes $\chi_2'(0)+M\chi_2(0)=0$:

$$
p\cos(pL)+M\sin(pL)=0\quad\Longleftrightarrow\quad \tan(pL)=-\frac pM .
$$

(For $\varepsilon^2<M^2$ the analogous condition with $\sinh$ and $\cosh$, $q\cosh(qL)+M\sinh(qL)=0$, has no solution with $q>0$, and $\varepsilon=0$ is excluded too: parity $-$ has no level with $|\varepsilon|<M$.) For $M=1$, $L=3$ the smallest root lies between $\pi/6$ and $\pi/3$; bisection gives $p=0.818548$ and $\varepsilon=\sqrt{1+p^2}=1.292293$. The Rust value of this level (8 states, occupied in the free $N=1016$ state, Section 13.11) is $1.292293$, the same to 12 digits.

**The brane band: the zero mode at small momentum.** For $k\ne0$ the zero mode moves. Its energy to first order in $k$ follows from the **Hellmann–Feynman** rule: if $h(k)\chi=\varepsilon(k)\chi$ with $\langle\chi|\chi\rangle=1$ and boundary conditions that do not depend on $k$, then $\varepsilon=\langle\chi|h\chi\rangle$ and $d\varepsilon/dk=\langle\chi|(\partial_kh)\chi\rangle$, because the terms with $d\chi/dk$ add up to $\varepsilon\,d\langle\chi|\chi\rangle/dk=0$ (self-adjointness, Section 13.5). Here $\partial_kh_j=j\kappa(y)\sigma_3$ and $\chi^\dagger\sigma_3\chi=e^{2My}$ for the zero mode, so

$$
\frac{d\varepsilon}{dk}\Big|_{k=0}=j\,c,\qquad c=\frac{\int_{-L}^0e^{-Hy-a_{4,0}}e^{2My}\,dy}{\int_{-L}^0e^{2My}\,dy}
=e^{-a_{4,0}}\,\frac{2M}{2M-H}\cdot\frac{1-e^{-(2M-H)L}}{1-e^{-2ML}}
$$

(`KS_reduction_zeroModeSplitting`). For $H=M=1$ and $a_{4,0}=0$: $c=2(1-e^{-L})/(1-e^{-2L})=2/(1+e^{-L})$, which is $1.761594$ for $L=2$, $1.905148$ for $L=3$ and $1.964028$ for $L=4$. The Rust solver measures $1.9051482525$ for $L=3$ against the exact $1.9051482536$ (`rust/spectrum/theory-agreement.json`). So the eight zero modes split into a **brane band** $\varepsilon=+ck$ (four states, $j=+1$) and $\varepsilon=-ck$ (four states, $j=-1$) at each momentum. The band is odd in $k$ (complex conjugation maps the block equation at $(k,\varepsilon)$ to the one at $(-k,-\varepsilon)$ when $v=0$), so the next correction is of order $k^3$. At the smallest torus momentum $k=\Delta k=0.25\,m$ (Section 13.7) the first-order value is $ck=0.476287\,m$, and the exact level found by the solver is $0.430734\,m$ (`rust/scf/m1_L3_N8_lam0_T0/run.json`, `epsLumo`). The brane band behaves like a massless fermion that lives on the brane; its states are the lowest positive levels at every $k\ne0$, and they are the ones the ground states of this chapter fill (Section 13.11).

![Kohn–Sham levels $\varepsilon_n(k)$ against the 3-momentum $k$ for parity $+$ (top) and parity $-$ (bottom), free ($m=1$, $L=3$, left) and self-consistent ($N=112$ with $+\hat\lambda_2$, right), for the two block types (circles and triangles). The dashed lines at the origin are the first-order brane band $\pm ck$; the dotted line is the chemical potential (file ks_spectrum.png in artifacts/dirac16complex/kohn-sham/figures).](artifacts/dirac16complex/kohn-sham/figures/ks_spectrum.png)

### 13.7 Densities, the torus, and particles above the sea

**The expectation-value rule.** In the positive-norm quantization of Chapter 8, a one-particle state built on a normalized mode $u$ above the Dirac sea has $\langle\Psi^\dagger X\Psi\rangle=u^\dagger BXu$ for every matrix $X$. The number (charge) density operator is $\Psi^\dagger B\Psi$, so its expectation is $u^\dagger B^2u=u^\dagger u\ge0$; the scalar density $\bar\Psi\Psi=\Psi^\dagger C\Psi$ gives $u^\dagger BCu$; the $y$-current gives $u^\dagger A_4u$ (Section 13.5). For a whole state with occupation weights $w_n$ the density matrix is $\rho=\sum_nw_nu_nu_n^\dagger$ and $\langle\Psi^\dagger X\Psi\rangle=\mathrm{Tr}(BX\rho)$.

**Densities of one orbital.** For a block orbital $\chi$ of type $j$ with $\int_{-L}^0\chi^\dagger\chi\,dy=1$, spread over a coordinate 3-volume $\ell^3$, the four **proper densities** (per unit proper volume) are

$$
n=\frac{e^{-6Hy}}{\ell^3}\chi^\dagger\chi,\qquad s=\frac{e^{-6Hy}}{\ell^3}\,j\chi^\dagger\sigma_2\chi,\qquad t=\frac{e^{-6Hy}}{\ell^3}\,j\chi^\dagger\sigma_3\chi,\qquad c=\frac{e^{-6Hy}}{\ell^3}\,j\chi^\dagger\sigma_1\chi :
$$

the number density, the scalar density (from $BC\to j\sigma_2$), the density of the 3-momentum current (from $-\gamma^4\gamma^1\to j\sigma_3$) and the $y$-current, which vanishes for every eigenstate (it is constant and zero at the ends). The factor $e^{-6Hy}=1/\sqrt{|g|}$ converts a density per unit $y$ into a density per unit proper volume. In the real form $\chi=(a,ib)$: $\chi^\dagger\chi=a^2+b^2$, $\chi^\dagger\sigma_2\chi=2ab$, $\chi^\dagger\sigma_3\chi=a^2-b^2$.

The **coordinate densities** $n_c=e^{6Hy}n_p$ and $S_c=e^{6Hy}S_p$ count particles per unit $y$ and unit coordinate 3-volume; the total particle number is $N=\ell^3\int_{-L}^0n_c\,dy$. Because the proper volume shrinks toward the tip, a state that is concentrated near the brane in $n_c$ can still have its largest **proper** densities at the tip; the interaction, which depends on the proper densities, is strongest there (Section 13.11).

**The torus and the shells.** The 3-space directions are a coordinate torus of size $\ell$, so $\mathbf k=\Delta k\,(n_1,n_2,n_3)$ with integers $n_l$ and $\Delta k=2\pi/\ell$ (Section 12.12). The runs use $\Delta k=0.25\,m$, that is $\ell=2\pi/(0.25\,m)=25.1327/m$. Since the spectrum depends only on $|\mathbf k|$, the momenta fall into **shells** $|\mathbf k|^2=\Delta k^2\,\nu$ with the integer $\nu=n_1^2+n_2^2+n_3^2$ (called `n2` in the Rust files), each with the number $g(\nu)$ of lattice vectors: $g(0)=1$, $g(1)=6$, $g(2)=12$, $g(3)=8$, $g(4)=6$, $g(5)=24$, $g(6)=24$, $g(8)=12$, $g(9)=30$, and so on. Each level of one block type at one lattice vector holds 4 states (the four blocks).

**Particles and the Dirac sea.** The quantization of Chapter 8 fills all negative-energy states (the Dirac sea) in the vacuum, and $N$ counts the quanta above it. The solver decides which levels belong to the sea by continuity from the free problem: a level is a **particle** level if its free partner (same shell, parity, block type and Prüfer index at $\lambda=0$, Section 13.10) has $\varepsilon_{\text{free}}\ge0$, and a **sea** level otherwise. The exact zero modes ($\varepsilon_{\text{free}}=0$) are counted as particle levels in both block types; this is a **convention** of the solver (the header of `src/scf.rs`). A particle level carries the weight $w=f(\varepsilon)$, the Fermi–Dirac occupation of Section 12.14, and a sea level the weight $w=-(1-f(\varepsilon))$: a hole in the sea, that is a thermal antiparticle, counts with a minus sign in the number of quanta (normal ordering). At $T=0$ the sea is full and contributes nothing.

**Closed shells.** At $T=0$ and $\lambda=0$ the $N$ lowest particle states are filled. A value of $N$ that fills complete levels is a **closed shell**; for it the Kohn–Sham gap is well defined. With the degeneracies above: $N=8$ fills the eight zero modes; the first band shell adds $4\cdot g(1)=24$ states ($N=32$), the next $4\cdot12=48$ ($N=80$), the next $4\cdot8=32$ ($N=112$), then $4\cdot6=24$ ($N=136$), and so on (the list `closedShells_m1_L3_N_epsHomo` in `rust/spectrum/summary.json`, up to $N=1408$). The study uses $N=8$ (the smallest closed shell), $N=112$ (the closed shell nearest to 100, `nMid` in the same file) and $N=1016$ (the one nearest to 1000, `nLarge`).

### 13.8 The interaction: Hartree energy and the exact exchange of the contact term

**The interaction and its size.** The Lagrangian contains $U(S)=\tfrac\lambda2S^2$ with $S=\bar\Psi\Psi$, normal ordered with respect to the free Dirac sea. In eight dimensions the action is dimensionless when $\Psi$ has the mass dimension $7/2$ (the kinetic term $\bar\Psi\gamma^\mu\partial_\mu\Psi$ must have dimension 8 to cancel $d^8x$), so $S^2$ has dimension 14 and $\lambda$ has dimension $-6$. The dimensionless strength is $\hat\lambda=\lambda m^6$ (`KS_exchange_couplingDimension`).

**Hartree–Fock energy of the contact term.** For a quasi-free state (a Slater determinant or a non-interacting ensemble) with the density matrix $\rho$ of Section 13.7, the expectation-value rule makes the two-point function $G_{ab}=\langle\Psi_a^\dagger\Psi_b\rangle=(\rho B)_{ba}$. Now $S^2=\Psi_a^\dagger C_{ab}\Psi_b\,\Psi_c^\dagger C_{cd}\Psi_d$ (sums over repeated spinor indices), and normal ordering moves $\Psi_b$ to the right of $\Psi_c^\dagger$ without the contraction, which gives $-\Psi_a^\dagger\Psi_c^\dagger\Psi_b\Psi_d$. Wick's theorem (Section 12.5) evaluates the four-operator expectation as $\langle\Psi_a^\dagger\Psi_c^\dagger\Psi_b\Psi_d\rangle=G_{ad}G_{cb}-G_{ab}G_{cd}$. Hence

$$
\langle{:}S^2{:}\rangle=C_{ab}C_{cd}\bigl(G_{ab}G_{cd}-G_{ad}G_{cb}\bigr)=\bigl[\mathrm{Tr}(BC\rho)\bigr]^2-\mathrm{Tr}(BC\rho\,BC\rho),
$$

using $\sum_{ab}C_{ab}(\rho B)_{ba}=\mathrm{Tr}(C\rho B)=\mathrm{Tr}(BC\rho)$ and the cyclic property of the trace for the second term. The **Hartree–Fock energy density** is therefore

$$
e_{HF}=\frac\lambda2\Bigl(S^2-\mathrm{Tr}(BC\rho\,BC\rho)\Bigr),\qquad S=\mathrm{Tr}(BC\rho),
$$

the Hartree term $e_H=\tfrac\lambda2S^2$ and the exchange (Fock) term $e_x=-\tfrac\lambda2\mathrm{Tr}(BC\rho BC\rho)$ (`KS_exchange_wickTheoremHF`, verified exactly on a Fock space of four modes for one-, two- and three-particle determinants). The Hartree term shifts the mass: $\partial e_H/\partial S=\lambda S$, so $M_{\text{eff}}=m+\lambda S$ as in Section 13.3.

**A filled shell: the ratio $1/8$.** Fill all eight positive-energy states at rest ($\mathbf p=0$). The rest Hamiltonian is $h_0=-im\gamma^4=m\,BC$ (Chapter 8), and $BC=-i\gamma^4$ is Hermitian, traceless and squares to 1 (since $(\gamma^4)^2=-1$). The projector onto its $+1$ eigenspace is $P_+=\tfrac12(1+BC)$, of rank 8, and $BC\,P_+=P_+$. With $\rho=P_+$:

$$
S=\mathrm{Tr}(BCP_+)=\tfrac12\mathrm{Tr}(BC)+\tfrac12\mathrm{Tr}(1)=8,\qquad \mathrm{Tr}(BCP_+BCP_+)=\mathrm{Tr}(P_+)=8=\frac{S^2}8 .
$$

So $e_x=-e_H/8$ (`KS_exchange_filledShellOneEighth`), the result $E_x=-E_H/g$ of Section 12.6 with $g=8$ internal states. (At a momentum $\mathbf p\ne0$ the same holds with $S=8m/E_p$, $E_p=\sqrt{m^2+p^2}$, `KS_exchange_filledShellScalarDensity`.)

**The uniform gas.** Now take the uniform gas of Section 12.12 for dirac16complex: all momenta $\mathbf p$ (in $d$ space dimensions), particle occupations $f_+(E_p)=1/(e^{(E_p-\mu)/T}+1)$ and antiparticle occupations $f_-(E_p)=1/(e^{(E_p+\mu)/T}+1)$ (the holes of the sea). With the projectors $P_\pm(\mathbf p)=\tfrac12(1\pm h_{\mathbf p}/E_p)$ onto the positive and negative energies of $h_{\mathbf p}=-im\gamma^4-\gamma^4\gamma^lp_l$, the normal-ordered density matrix is $\rho=\int\frac{d^dp}{(2\pi)^d}\bigl[f_+P_+(\mathbf p)-f_-P_-(\mathbf p)\bigr]$. The number and scalar densities follow from $\mathrm{Tr}\,P_\pm=8$ and $\mathrm{Tr}(BC\,P_\pm)=\pm8m/E_p$:

$$
n=\mathrm{Tr}\,\rho=8\int\frac{d^dp}{(2\pi)^d}\bigl(f_+-f_-\bigr),\qquad
S=\mathrm{Tr}(BC\rho)=8\int\frac{d^dp}{(2\pi)^d}\,\frac m{E_p}\bigl(f_++f_-\bigr).
$$

Antiparticles lower $n$ and raise $S$. The exchange term needs the **kernel**

$$
K_{ab}(\mathbf p,\mathbf q)=\mathrm{Tr}\bigl(P_a(\mathbf p)\,BC\,P_b(\mathbf q)\,BC\bigr)=4\Bigl[1+ab\,\frac{m^2-\mathbf p\cdot\mathbf q}{E_pE_q}\Bigr],\qquad a,b=\pm1
$$

(`KS_exchange_kernelPlusPlus`, `KS_exchange_kernelPlusMinus`; the Rust solver checks it with the full $16\times16$ projectors to $5\times10^{-15}$, `rust/spectrum/exchange-check.json`). Insert $\rho$ into $\mathrm{Tr}(BC\rho BC\rho)$: the four products of the two terms of $\rho$ give $f_+f_+'K_{++}-f_+f_-'K_{+-}-f_-f_+'K_{-+}+f_-f_-'K_{--}$ under the double integral (primes for the momentum $\mathbf q$). Collect the terms of the kernel:

$$
\mathrm{Tr}(BC\rho BC\rho)=4\!\int\!\!\int\Bigl[(f_+-f_-)(f_+'-f_-')+\frac{m^2-\mathbf p\cdot\mathbf q}{E_pE_q}(f_++f_-)(f_+'+f_-')\Bigr].
$$

For occupations that depend only on $|\mathbf p|$, the term with $\mathbf p\cdot\mathbf q$ integrates to zero, because the average of $\mathbf p\cdot\mathbf q$ over the directions of $\mathbf p$ vanishes (`KS_exchange_angularAverageOfPdotQVanishes`). The double integral then **factorizes** into $(n/8)^2$ and $(S/8)^2$:

$$
\mathrm{Tr}(BC\rho BC\rho)=4\Bigl[\bigl(\tfrac n8\bigr)^2+\bigl(\tfrac S8\bigr)^2\Bigr]=\frac{n^2+S^2}{16},\qquad
e_x(n,S)=-\frac\lambda{32}\bigl(n^2+S^2\bigr),\qquad e_H=\frac\lambda2S^2
$$

(erratum E4.7; `KS_exchange_uniformGasClosedForm`). This closed form holds **exactly at every temperature** and in any number of space dimensions, since only the isotropy of the occupations was used; the temperature enters only through $n$ and $S$. A gas at rest ($k_F\to0$) has $S=n$ and $e_x=-\tfrac\lambda{16}n^2=-e_H/8$, the filled-shell value (`KS_exchange_restGasLimit`). The independent sympy checker tabulated the double integral by direct quadrature, and the closed form reproduces all 580 rows of that table to $5\times10^{-15}$ relative (`python-theory-report.json`, entry `exchangeTable`; the table is `artifacts/dirac16complex/kohn-sham/exchange-table.json`).

![Left: the exchange energy density $-e_x/\lambda$ of the uniform 8-fold gas against the number density at four temperatures, closed form (lines) and quadrature (markers). Right: the relative difference between quadrature and closed form for every row of the two tables, below $10^{-12}$ everywhere (file exchange_uniform_gas.png in artifacts/dirac16complex/kohn-sham/figures).](artifacts/dirac16complex/kohn-sham/figures/exchange_uniform_gas.png)

**The local potentials.** Evaluated with the local proper densities $n_p(y)$ and $S_p(y)$, the closed form is the local density approximation of Section 12.12 for this system. Its two derivatives are the **exchange potentials**

$$
v_v=\frac{\partial e_x}{\partial n}=-\frac\lambda{16}\,n,\qquad v_s=\frac{\partial e_x}{\partial S}=-\frac\lambda{16}\,S
$$

(`KS_exchange_ldaPotentials`). The vector potential $v_v$ multiplies the number density matrix and enters the equation as $\varepsilon\to\varepsilon-v_v(y)$; the scalar potential $v_s$ multiplies the scalar density matrix $BC$ and adds to the mass. The Kohn–Sham equation used in all runs (called KS-VS in the theory file) is the block equation of Section 13.5 with

$$
M_{\text{eff}}(y)=m+\lambda S_p(y)+v_s(y)=m+\tfrac{15}{16}\lambda S_p(y),\qquad v(y)=v_v(y)=-\tfrac1{16}\lambda\,n_p(y).
$$

The specification calls this pair $(M_{\text{eff}},v_v)$, together with the gravitational terms, the **Kohn–Sham fermion-gas thermodynamic pseudo-potential**.

**How good is the local form?** For the contact interaction the exact Fock term is local in $y$ as well (Section 12.6): with the $2\times2$ density matrix $\rho_\beta=\tfrac12(n_\beta+s_\beta\sigma_2+t_\beta\sigma_3+c_\beta\sigma_1)$ of each block $\beta$ (up to the signs $j$), $E_x^{HF}=-\tfrac\lambda4\int dV\sum_\beta\bigl(n_\beta^2+s_\beta^2-t_\beta^2-c_\beta^2\bigr)$ (`KS_exchange_blockFormOfFockTerm`). If the eight blocks carry equal densities $n/8$ and $S/8$ and no momentum current, this is $-\tfrac\lambda4\cdot8\bigl[(n/8)^2+(S/8)^2\bigr]=-\tfrac\lambda{32}(n^2+S^2)$, the closed form. Otherwise the two differ by the $t_\beta^2$ terms and by the unequal occupation of the blocks. The Kohn–Sham scheme of this chapter uses the closed form; that choice is the **approximation** of the exchange part.

**No correlation term.** Beyond Hartree–Fock a contact interaction with a coupling of mass dimension $-6$ is not renormalizable: its higher-order corrections cannot be made finite with a finite number of parameters (the standard power-counting argument of quantum field theory, which we quote and do not derive). There is therefore no well-defined correlation energy to approximate, and the scheme is **exchange-only**: the uniform-gas Hartree–Fock energy written as a local functional of $n$ and $S$.

### 13.9 The Mermin–Kohn–Sham functional and its equations

**The functional.** Let the orbitals $\chi_n$ (each in one block, with a block type $j_n$, a momentum $k_n$ and a parity) be normalized, $\int\chi_n^\dagger\chi_n\,dy=1$, with occupations $f_n$, and let $dV=e^{6Hy}\ell^3dy$ be the proper volume element per unit coordinate extra-time volume. Mermin's free-energy functional (Section 12.14) is

$$
\begin{aligned}
F&=\sum_nf_n\langle\chi_n|h_0|\chi_n\rangle-T\,S_{\text{ent}}+E_H+E_x,\qquad h_0=j\Bigl[-i\sigma_1\frac d{dy}+m\sigma_2+\kappa k\sigma_3\Bigr],\\
E_H&=\frac\lambda2\int S_p^2\,dV,\qquad E_x=-\frac\lambda{32}\int\bigl(n_p^2+S_p^2\bigr)\,dV,\qquad S_{\text{ent}}=-\sum_n\bigl[f_n\ln f_n+(1-f_n)\ln(1-f_n)\bigr],
\end{aligned}
$$

with $n_p=e^{-6Hy}\sum_nf_n\chi_n^\dagger\chi_n/\ell^3$ and $S_p=e^{-6Hy}\sum_nf_n\chi_n^\dagger(j_n\sigma_2)\chi_n/\ell^3$ (`kohn-sham-theory.json`, key `functional`). (In the solver the sums run over the particle and sea levels with the weights $w_n$ of Section 13.7.)

**Stationarity with respect to the orbitals.** Vary $\chi_n^\dagger(y)$ with multipliers $f_n\varepsilon_n$ for the normalization. The derivative of $\int S_p^2\,dV$ is $2S_p(y)\cdot e^{6Hy}\ell^3\cdot e^{-6Hy}f_n(j_n\sigma_2)\chi_n(y)/\ell^3=2f_nS_p\,j_n\sigma_2\chi_n$: the factor $e^{6Hy}$ of the volume element cancels the $e^{-6Hy}$ of the density, so the equation is local with the flat measure $dy$. In the same way $E_x$ gives $-\tfrac\lambda{16}f_n\bigl(n_p+S_pj_n\sigma_2\bigr)\chi_n=f_n(v_v+v_sj_n\sigma_2)\chi_n$. Dividing by $f_n$:

$$
\Bigl[h_0+(\lambda S_p+v_s)\,j\sigma_2+v_v\Bigr]\chi_n=\varepsilon_n\chi_n
\quad\Longleftrightarrow\quad
j\Bigl[-i\sigma_1\frac d{dy}+M_{\text{eff}}\sigma_2+\kappa k\sigma_3\Bigr]\chi_n+v_v\chi_n=\varepsilon_n\chi_n ,
$$

the Hamiltonian form of Section 13.5 with the potentials of Section 13.8 (`KS_functional_stationarityGivesKSEquation`).

**Stationarity with respect to the occupations.** Exactly as in Section 12.14, $\partial F/\partial f_n=\varepsilon_n+T\ln\frac{f_n}{1-f_n}-\mu=0$ gives the Fermi–Dirac occupations $f_n=1/(e^{(\varepsilon_n-\mu)/T}+1)$, with $\mu$ fixed by the particle number (`KS_functional_fermiDiracOccupations`).

**Total energy.** Both interaction functionals are quadratic in the densities, so $\sum_nf_n\varepsilon_n=\sum_nf_n\langle h_0\rangle_n+2E_H+2E_x$ (each quadratic functional contributes twice itself through its potential). Hence

$$
E=\sum_nf_n\varepsilon_n-E_H-E_x,\qquad F=E-TS_{\text{ent}}
$$

(`KS_functional_totalEnergyDoubleCounting`). **Worked example.** For $N=112$ at $\hat\lambda_1$ the solver reports $\sum w\varepsilon=61.1358649$, $E_H=0.0342610$ and $E_x=-0.0116081$ (`rust/scf/m1_L3_N112_lamp1_T0/run.json`, keys `ksSum`, `hartreeEnergy`, `exchangeEnergy`). Then $E=61.1358649-0.0342610+0.0116081=61.1132120$, the value of the key `energy`.

**Hellmann–Feynman relations.** Because $F$ is stationary, its derivative with respect to a parameter is the explicit partial derivative (the envelope theorem of Section 12.14): $dF/d\lambda=(E_H+E_x)/\lambda$, $dF/dm=\int S_p\,dV$ (the total scalar charge), $dF/dT=-S_{\text{ent}}$, and for each level $d\varepsilon_n/dk=j\int\kappa\,\chi_n^\dagger\sigma_3\chi_n\,dy$ at fixed potentials (the checks `hellmannFeynmanLambda`, `hellmannFeynmanMass`, `hellmannFeynmanTemperature` and `merminStructure` of the family `KS_functional`). The Rust solver checks $dE/dm=\int S_p\,dV$ by finite differences in two runs (checks `m1_L3_N112_lam0_T0_hellmann_feynman_dE_dm` and `m1_L3_N112_lamp1_T0_hellmann_feynman_dE_dm` of `rust/scf/summary.json`). For $\lambda=0$ the scalar charge $\int\chi^\dagger j\sigma_2\chi\,dy$ of a single level is $d\varepsilon/dM$ (Hellmann–Feynman with $\partial h_j/\partial M=j\sigma_2$). At $k=0$ it is $M/\varepsilon$ for the parity-$+$ massive levels, whose energy $\sqrt{M^2+(n\pi/L)^2}$ was found in Section 13.6 (for example $1/1.447972=0.6906$); it is positive for the other massive levels too, 0 for the zero modes, and **negative** for the brane band, because $c(M)$ of Section 13.6 decreases toward 1 as $M$ grows, so $d\varepsilon/dM\approx k\,dc/dM<0$ (the header of `src/emt.rs`; column `scalar_charge` of the `levels.csv` files).

### 13.10 How the Rust solver computes the Kohn–Sham states

The solver `studies/dirac16complex_kohn_sham` integrates the block equation as an ordinary differential equation in $y$ with the CVODE engine of Chapter 10; nothing is discretized into a matrix. Its module headers contain the derivations summarized here.

**The Prüfer angle.** Write the real solution as $a=r\cos\theta$, $b=-r\sin\theta$. From the real system of Section 13.5, $\theta'=(ba'-ab')/r^2$ and $(\ln r)'=(aa'+bb')/r^2$. Inserting $a'$ and $b'$, and using $ab=-\tfrac12r^2\sin2\theta$ and $a^2-b^2=r^2\cos2\theta$,

$$
\theta'=-j\bigl(\varepsilon-v(y)\bigr)+\kappa(y)\,k\cos2\theta-M_{\text{eff}}(y)\sin2\theta,\qquad (\ln r)'=M_{\text{eff}}\cos2\theta+\kappa k\sin2\theta .
$$

The first equation does not contain $r$: the angle can be integrated alone. The tip condition $b(-L)=0$ is $\theta(-L)=0$. At the brane, parity $+$ ($b(0)=0$) means $\sin\theta(0)=0$ and parity $-$ ($a(0)=0$) means $\cos\theta(0)=0$. The solver treats the block type $j=-1$ (its $s=+1$), for which $\partial\theta'/\partial\varepsilon=+1>0$. Then the end value $\Theta(\varepsilon)=\theta(0;\varepsilon)$ **increases strictly** with $\varepsilon$ (a solution with a larger $\varepsilon$ can never be overtaken by one with a smaller $\varepsilon$, since at a crossing point it would have the larger slope), so

$$
\text{parity }+:\ \Theta(\varepsilon)=n\pi,\qquad \text{parity }-:\ \Theta(\varepsilon)=\tfrac\pi2+n\pi,\qquad n\in\mathbb Z,
$$

has exactly one solution for each integer $n$, the **Prüfer index** of the level. This is the oscillation theorem of the one-dimensional Dirac operator: every level in an energy window is found and none is missed. The block type $j=+1$ follows from $h_{+1}=-h_{-1}+2v$ (Section 13.5): its levels are those of the $j=-1$ problem with $\varepsilon\to-\varepsilon$ and $v\to-v$, with the same profiles.

**Finding a level and its profile.** For each momentum shell and parity, the solver brackets each target value of $\Theta$ by doubling the step in $\varepsilon$, then refines it by the Illinois variant of the regula falsi (a root finder that keeps the root bracketed). At the level it integrates the linear system for $(a,b)$ once more, together with the integrals $\int(a^2+b^2)$, $\int2ab$ and $\int\kappa k(a^2-b^2)$, rescales the solution whenever $a^2+b^2$ leaves $[10^{-40},10^{40}]$, and normalizes it. The CVODE tolerances are $10^{-12}$ (relative) and $10^{-14}$ (absolute) with the largest step $0.05$ (`rust/spectrum/summary.json`, key `tolerances`). The potentials $M_{\text{eff}}(y)$ and $v(y)$ are tabulated on 301 equally spaced points of $[-L,0]$ and interpolated by cubic splines between them; one run uses 601 points as a refinement (Section 13.15).

**The coupling strengths.** The proper densities near the tip grow like $e^{6HL}$ and with $N$, so one value of $\hat\lambda$ cannot give the same strength of interaction in every configuration. For each configuration $(m,L,N)$ the solver therefore measures, in the free ground state, the largest value of the pair $\bigl(\tfrac{15}{16}|S_p|,\ n_p/16\bigr)$ per unit $\hat\lambda$ (the **strength**, in units of $m$), and sets $\hat\lambda_1=0.1/\text{strength}$ and $\hat\lambda_2=1/\text{strength}$: at first order the pseudo-potential then reaches $0.1\,m$ and $1\,m$ (`couplingRule` in `rust/spectrum/summary.json`). For $m=1$, $L=3$ this gives $\hat\lambda_1=9.72989\times10^{-3}$ ($N=8$), $9.56776\times10^{-3}$ ($N=112$) and $1.57694\times10^{-4}$ ($N=1016$), and $\hat\lambda_2=10\,\hat\lambda_1$ in each case. Each configuration is solved for $\hat\lambda\in\{0,\pm\hat\lambda_1,\pm\hat\lambda_2\}$; $\hat\lambda>0$ is a repulsive and $\hat\lambda<0$ an attractive contact interaction.

**The self-consistent loop.** Starting from the free state, the loop of Section 12.11 is run with the densities $(n_c,S_c)$ as the iterated quantity and **Anderson mixing** (Section 12.13; mixing parameter 0.4, history of 6, at most 80 iterations; `parameters` in each `run.json`). It stops when the largest change of $n_c$ and of $S_c$, divided by the largest of $|n_c|$ and $|S_c|$, is below $10^{-10}$. At $T>0$ the chemical potential is found by bisection at every iteration (Section 12.14).

**The ground state when the loop cannot settle** (erratum E4.8). In one canonical run ($N=1016$, $-\hat\lambda_2$) two levels cross at the Fermi level during the iteration, the integer occupations flip back and forth, and the loop stagnates (Section 12.13). The **ground state** is then *defined* as the self-consistent solution reached by **continuation in the coupling** from $\lambda=0$: the solver solves at $\lambda/4$, $\lambda/2$, $3\lambda/4$ and $\lambda$, each step started from the previous solution with damped mixing, first with exact occupations and, where they slosh, with Fermi–Dirac occupation smearing of width $10^{-3}\,m$ (then $10^{-2}\,m$). That run converged with smearing $10^{-3}\,m$ at the physical temperature $T=0$ (so $F=E$); `run.json` records the path (`zeroTemperatureFallbackStage` 1, `occupationSmearing` 0.001, `exactZeroTemperatureOccupations` false). Section 13.11 describes the resulting ensemble.

**The solver's own checks.** Every self-consistent run is checked for convergence, for the particle number ($\sum w=N$ and $\ell^3\int n_c\,dy=N$), for the energy identity $\int\rho\,dV=E$ of Section 13.14, and for the conservation of the energy–momentum tensor. With the checks specific to each subcommand (spectrum and theory agreement, excited states, thermodynamics, energy–momentum tensor), all 397 checks of the five `summary.json` files pass. A second run of the same build is byte-identical in all 327 output files, and a run with tolerances divided by 10 and half the largest step agrees with the canonical one to $5.96\times10^{-8}$ relative in $E$ and $F$ (65 runs) and to $2.8\times10^{-8}$ absolute in 364829 eigenvalues (`rust/determinism-report.json`).

### 13.11 Ground states

The table lists the self-consistent ground states for $m=1$, $L=3$ (`rust/scf/summary.json`; the same numbers are in `rust/excited/excitations.csv`). $E_0$ is the total energy of Section 13.9 relative to the filled Dirac sea (normal ordering), $\varepsilon_{\text{HOMO}}$ the highest occupied particle level, $\Delta_{KS}$ the Kohn–Sham gap, and the last column is the largest Hartree mass shift reached, $\max_y|\lambda S_p|/m$. All energies are in units of $m$.

| $N$ | $\hat\lambda/\hat\lambda_1$ | $E_0$ | $\varepsilon_{\text{HOMO}}$ | $\Delta_{KS}$ | $\max\lvert\lambda S_p\rvert/m$ |
| --- | --- | --- | --- | --- | --- |
| 8 | 0 | 0 | 0 | 0.430734 | 0 |
| 8 | +1 | $-9.86833\times10^{-4}$ | $-2.45560\times10^{-4}$ | 0.430944 | 0.0165 |
| 8 | $-1$ | $+9.86833\times10^{-4}$ | $+2.45560\times10^{-4}$ | 0.430516 | 0.0165 |
| 8 | +10 | $-7.83039\times10^{-3}$ | $-1.68579\times10^{-3}$ | 0.431899 | 0.647 |
| 8 | $-10$ | $+7.83039\times10^{-3}$ | $+1.68579\times10^{-3}$ | 0.429137 | 0.647 |
| 112 | 0 | 61.090723 | 0.704100 | 0.0955462 | 0 |
| 112 | +1 | 61.113212 | 0.704476 | 0.0954841 | 0.0592 |
| 112 | $-1$ | 61.068610 | 0.703736 | 0.0956051 | 0.0583 |
| 112 | +10 | 61.328311 | 0.708384 | 0.0948132 | 1.358 |
| 112 | $-10$ | 60.891305 | 0.700966 | 0.0960102 | 0.452 |
| 1016 | 0 | 1127.136625 | 1.385919 | 0.0530077 | 0 |
| 1016 | +1 | 1127.160980 | 1.385934 | 0.0532575 | 0.100 |
| 1016 | $-1$ | 1127.111039 | 1.385904 | 0.0527200 | 0.114 |
| 1016 | +10 | 1127.342203 | 1.386070 | 0.0544240 | 0.665 |
| 1016 | $-10$ | 1126.858093 | 1.389461 | 0.0412551 | 1.372 |

($\hat\lambda/\hat\lambda_1=\pm10$ means $\pm\hat\lambda_2$. The last row is the smeared ensemble described below.) The largest exchange potential, $\max_y|v|/m$, is 0.591 for $N=8$ at $\pm\hat\lambda_2$, 0.893 for $N=112$ at $+\hat\lambda_2$ and 1.50 for $N=1016$ at $-\hat\lambda_2$: the chosen couplings put the pseudo-potential into the range from about $0.1\,m$ to $1.5\,m$, as intended.

**$N=8$: the brane zero modes.** Without interaction the ground state fills exactly the eight zero modes of Section 13.6; they have $\varepsilon=0$, so $E_0=0$, and their scalar density vanishes identically ($\chi_2\equiv0$ gives $\chi^\dagger\sigma_2\chi=0$). Their coordinate density is $n_c\propto e^{2my}$, so the fraction of the particles within the distance $1/H$ of the brane is $\int_{-1}^0e^{2y}dy\big/\int_{-3}^0e^{2y}dy=(1-e^{-2})/(1-e^{-6})=0.866813$; the solver reports $0.8668133$ (`braneFraction_within_1_over_H` in `rust/scf/m1_L3_N8_lam0_T0/run.json`). With interaction, the exchange potential $v=-\lambda n_p/16$ shifts the zero modes to $\varepsilon\approx\langle v\rangle$, negative for $\lambda>0$. The table shows $E_0(-\lambda)=-E_0(\lambda)$ to all printed digits; Exercise 13.9 derives this exact property of the $N=8$ state.

**$N=112$ and $N=1016$: the brane band.** The larger states fill the zero modes and then the brane band shell by shell (Section 13.7). For $\lambda=0$ the occupied particle levels of $N=112$ are the zero modes and the band at $k=0.25$, $0.354$ and $0.433\,m$ ($\varepsilon=0.430734$, $0.587957$, $0.704100$); the lowest empty level is the band at $k=0.5\,m$ ($0.799646$), so $\Delta_{KS}=0.0955462$. For $N=1016$ the band is filled up to $k=0.935\,m$ (a shell of 192 states at $\varepsilon=1.385919$), and in addition the eight parity-$-$ bulk states at $k=0$ with $\varepsilon=1.292293$ (Section 13.6) are occupied (`rust/scf/m1_L3_N1016_lam0_T0/levels.csv`). The interaction changes the energies by at most $0.3\,m$ out of 61 and 1127: the interaction is a perturbation, and the self-consistent energy shifts follow the first-order Hellmann–Feynman estimate $\lambda\,dE/d\lambda$ closely (figure `ground_state_energy.png` in `artifacts/dirac16complex/kohn-sham/figures`, not reproduced here). The fraction of particles within $1/H$ of the brane grows with $N$: 0.867 ($N=8$), 0.924 ($N=112$), 0.962 ($N=1016$) for $\lambda=0$; for $m=3$ it is 0.9975 ($N=8$) and 0.9990 ($N=112$), because a heavier zero mode $e^{My}$ is more strongly localized.

![Self-consistent ground states for $m=1$, $L=3$: the coordinate density $n_c$ (particles per unit $y$), the proper number density $n_p$, the proper scalar density $S_p$, the Hartree–exchange mass shift $M_{\text{eff}}-m=\tfrac{15}{16}\lambda S_p$, the exchange potential $v_x=-\lambda n_p/16$, and the highest occupied orbital against the notebook coordinate $z=6Hx_0$ (file density_profiles.png in artifacts/dirac16complex/kohn-sham/figures).](artifacts/dirac16complex/kohn-sham/figures/density_profiles.png)

**Where the interaction acts.** The figure shows the point of Section 13.7. The particles sit near the brane ($n_c$ largest at $y=0$), but the proper densities $n_p=e^{-6Hy}n_c$ are largest at the tip, so the pseudo-potential $(M_{\text{eff}}-m,\ v)$ is concentrated near $y=-L$. The scalar density is negative near the brane, where the brane band dominates, and for the larger $N$ it becomes positive near the tip, where the bulk levels contribute (Section 13.9).

**The level crossing at $N=1016$, $-\hat\lambda_2$** (erratum E4.8). The attraction pulls the 8-fold $k=0$ bulk level down from $1.447972$ to the Fermi level, where it meets the 192-fold band at $k=0.935\,m$. The converged smeared ensemble (Section 13.10) moves about 4.2 particles from the band (occupation 0.978059) into the $k=0$ level (occupation 0.526580, so $8\times0.526580=4.21$ particles), which lies $3.69\times10^{-3}\,m$ above the band (`rust/scf/m1_L3_N1016_lamm2_T0/levels.csv`, column `f`); its $\varepsilon_{\text{HOMO}}=1.389461$ is that fractionally occupied level, and its Kohn–Sham gap $0.0412551\,m$ is the distance to the band at $k=0.25\,m$ ($1.430716$). This is an ensemble with fractional occupations, not a single determinant, and its numbers refer to that ensemble. An exploratory reference computation on twice finer grids converged, from its own start, to a different self-consistent state about $1.01\,m$ higher (`handoff/reviews/stage4_refgrid_N0120_exploratory.log`): the nonlinear problem has more than one self-consistent solution here, and the continuation from $\lambda=0$ is what selects the one reported.

![The level crossing at the Fermi level for $N=1016$: particle levels near the Fermi level against $k$ (marker area proportional to the number of states, colour the occupation), free (left) and in the smeared self-consistent ensemble at $-\hat\lambda_2$ (right), where the 8-fold $k=0$ level and the 192-fold band at $k=0.935\,m$ share the particles (file fermi_level_N1016_lamm2.png in artifacts/dirac16complex/kohn-sham/figures).](artifacts/dirac16complex/kohn-sham/figures/fermi_level_N1016_lamm2.png)

![Convergence of the self-consistent loop: the density residual against the iteration for $+\hat\lambda_2$ (left) and $-\hat\lambda_2$ (right) and $N=8$, 112, 1016; the tolerance is $10^{-10}$. The slow, irregular curve is the $N=1016$ run at $-\hat\lambda_2$ with its level crossing (file scf_history.png in artifacts/dirac16complex/kohn-sham/figures).](artifacts/dirac16complex/kohn-sham/figures/scf_history.png)

### 13.12 First excited states: Kohn–Sham gap, particle–hole pairs and Delta-SCF

The three quantities of Section 12.15 are computed for every $T=0$ ground state of Section 13.11 (`rust/excited/`). The **particle–hole list** (`particle-hole.csv` of each run) contains the differences $\varepsilon_{\text{particle}}-\varepsilon_{\text{hole}}$ in increasing order, where a level counts as a possible hole if its occupation is $f>10^{-12}$ and as a possible particle if $f<1-10^{-12}$ (erratum E4.9; at $T>0$ the thresholds are $f\ge\tfrac12$ and $f<\tfrac12$). The **Delta-SCF** state fixes the occupations by the identity of the levels (shell, parity, block type, Prüfer index), moves one particle from the HOMO group to the LUMO group, and is converged again; $\Delta_{\text{SCF}}=E_1-E_0$ (the header of `src/scf.rs`).

| $N$ | $\hat\lambda/\hat\lambda_1$ | $\Delta_{KS}$ | $\Delta_{\text{SCF}}$ | $\Delta_{\text{SCF}}-\Delta_{KS}$ |
| --- | --- | --- | --- | --- |
| 8 | 0 | 0.430734 | 0.430734 | 0 |
| 8 | +1 | 0.430944 | 0.430938 | $-5.79\times10^{-6}$ |
| 8 | $-1$ | 0.430516 | 0.430523 | $+7.50\times10^{-6}$ |
| 8 | +10 | 0.431899 | 0.431946 | $+4.72\times10^{-5}$ |
| 8 | $-10$ | 0.429137 | 0.429161 | $+2.32\times10^{-5}$ |
| 112 | 0 | 0.0955462 | 0.0955462 | 0 |
| 112 | +1 | 0.0954841 | 0.0954842 | $+5.84\times10^{-8}$ |
| 112 | $-1$ | 0.0956051 | 0.0956051 | $-5.18\times10^{-8}$ |
| 112 | +10 | 0.0948132 | 0.0948140 | $+8.41\times10^{-7}$ |
| 112 | $-10$ | 0.0960102 | 0.0960098 | $-3.28\times10^{-7}$ |
| 1016 | 0 | 0.0530077 | 0.0530077 | $-3.7\times10^{-10}$ |
| 1016 | +1 | 0.0532575 | 0.0532689 | $+1.14\times10^{-5}$ |
| 1016 | $-1$ | 0.0527200 | 0.0527082 | $-1.18\times10^{-5}$ |
| 1016 | +10 | 0.0544240 | 0.0545261 | $+1.02\times10^{-4}$ |
| 1016 | $-10$ | 0.0412551 | 0.0436184 | $+2.36\times10^{-3}$ |

(Energies in units of $m$, $m=1$, $L=3$; `rust/excited/summary.json`. The last row belongs to the smeared ensemble.)

**What the first excited state is.** For $N=8$ the lowest particle–hole pair takes a particle out of a zero mode ($k=0$) and puts it into the first shell of the brane band ($k=0.25\,m$); the next pairs go to $k=0.354\,m$ (excitation $0.587957$) and so on (`rust/excited/m1_L3_N8_lam0_T0/particle-hole.csv`). For $N=112$ and $N=1016$ the first excitation moves a particle from the highest filled shell of the band to the next empty one. In all cases the first excited state is an excitation **within the brane band**: its energy is set by the spacing of the torus momenta ($\Delta k=0.25\,m$) along the band $\varepsilon\approx ck$. Without interaction the levels do not move, so $\Delta_{\text{SCF}}=\Delta_{KS}$ exactly (the value $-3.7\times10^{-10}$ in the row $N=1016$, $\hat\lambda=0$ is at the level of the numerical accuracy of the two separate solutions). With interaction the orbital relaxation of Section 12.15 is at most $1.02\times10^{-4}\,m$ in all states with a single determinant; its sign depends on the case.

**The ensemble at $N=1016$, $-\hat\lambda_2$.** Here the particle–hole list starts with $6.6\times10^{-12}\,m$: this is not an excitation but the difference between the two numerically split halves of the fractionally occupied $k=0$ level (Section 13.11). Next comes $3.69\times10^{-3}\,m$ (a particle from the band at $k=0.935\,m$ into the $k=0$ level), then the Kohn–Sham gap $0.0412551\,m$ (from the $k=0$ level into the band at $k=0.25\,m$). The Delta-SCF excitation of this ensemble is $0.0436184\,m$ on the standard grid of 301 points and $0.0436194\,m$ on 601 points (run `m1_L3_N1016_lamm2_T0_g601`, check `excited_grid_refinement_delta_scf`). **This is the one number of the chapter whose independent cross-check was open**: at the time of writing the Python reference solver gave a value about $3.3\times10^{-6}\,m$ higher, outside the cross-check tolerance of $10^{-6}$ (`HANDOFF.md`, Stage-4 row). Quoted to the digits on which the two solvers agree, $\Delta_{\text{SCF}}=0.04362\,m$ (erratum E4.8).

![Left: the Kohn–Sham gap (filled) and the Delta-SCF excitation energy (open) of the ground states of $N=8$, 112 and 1016 against $\hat\lambda/\hat\lambda_1$. Right: the orbital relaxation $\Delta_{\text{SCF}}-\Delta_{KS}$ on a signed logarithmic scale. The annotation in the left panel refers to the smeared ensemble of Section 13.11 (file ks_gap_delta_scf.png in artifacts/dirac16complex/kohn-sham/figures).](artifacts/dirac16complex/kohn-sham/figures/ks_gap_delta_scf.png)

### 13.13 Finite temperature

**The runs.** The subcommand `thermo` solves the Mermin–Kohn–Sham equations of Section 13.9 at $T/m\in\{0,0.1,0.3,1\}$ for $N=8$ and $N=112$ ($m=1$, $L=3$) in three series (`rust/thermo/summary.json`, key `seriesRule`): `lam0` without interaction; `lamp1` with the $T=0$ coupling $\hat\lambda_1$, run only at the temperatures where its first-order pseudo-potential stays below $1\,m$; and `lamh` with a smaller "hot" coupling, $\hat\lambda=2.368\times10^{-5}$, chosen so that the pseudo-potential is $0.1\,m$ at $T=m$ and the whole series belongs to one Hamiltonian. The `lamp1` points at $T=m$ were not run: there the first-order pseudo-potential would be $41.1\,m$ ($N=8$) and $40.4\,m$ ($N=112$), because thermal pairs raise the largest scalar density of the free state to about 4504 (key `skippedRuns`). At $T>0$ both particle and sea levels have fractional weights, $w=f$ and $w=-(1-f)$ (Section 13.7): the gas contains **thermal particle–antiparticle pairs**, which do not change $N$.

**Results without interaction** (`rust/thermo/thermodynamics.csv`, series 0; energies in units of $m$, $S$ dimensionless):

| $N$ | $T/m$ | $\mu$ | $E$ | $F$ | $S$ |
| --- | --- | --- | --- | --- | --- |
| 8 | 0.1 | 0.130419 | 1.031867 | $-0.393979$ | 14.25845 |
| 8 | 0.3 | 0.013287 | 108.7346 | $-30.51150$ | 464.1537 |
| 8 | 1 | 0.000376 | 46811.74 | $-11447.70$ | 58259.43 |
| 112 | 0.1 | 0.697334 | 69.50938 | 53.97164 | 155.3773 |
| 112 | 0.3 | 0.316932 | 167.7124 | $-12.41988$ | 600.4411 |
| 112 | 1 | 0.010141 | 46813.93 | $-11447.15$ | 58261.08 |

At $T=0$ the values are those of Section 13.11 ($F=E=0$ for $N=8$, $61.090723$ for $N=112$, $S=0$). **Worked check:** $F=E-TS$ for $N=8$ at $T=0.1$ gives $1.031867-0.1\times14.25845=-0.393978$, the tabulated $F$ to the last digit. The heat capacity $C_V=dE/dT$ is $33.618$, $1754.07$ and $2.383\times10^5$ for $N=8$ and $157.752$, $1465.74$ and $2.383\times10^5$ for $N=112$ at $T/m=0.1$, $0.3$ and $1$ (column `C_V`: a self-consistent central difference with step $0.05\,T$ for $T\le0.3\,m$, the exact fixed-spectrum formula of Exercise 12.9 at $T=m$). Without interaction the exact fixed-spectrum value, $33.500$ and $1745.07$ for $N=8$, agrees with the central difference within the 2 percent allowed by the check `cv_finite_difference_vs_exact` (the difference is the truncation error of the finite step).

**What the numbers say.** At $T=0.1\,m$ the gas is a slightly heated Fermi system near the brane. At $T=m$ it is a **plasma of thermal pairs**: the energy window of the solver then contains about 75000 levels (74945 for $N=8$, column `states`), $E$ and $S$ are almost the same for $N=8$ and $N=112$ (the eight or 112 extra particles are negligible against the pairs), and $\mu$ is close to 0 because the plasma is almost charge-symmetric. The free energy decreases with $T$ and the entropy is positive in every run (checks `free_energy_decreases`, `entropy_positive`, `heat_capacity_positive` of `rust/thermo/summary.json`, 102 of 102 true). The Kohn–Sham gap at finite $T$ is read with the threshold $f\ge\tfrac12$ (Section 12.15): for $N=112$ at $T=0.1\,m$ the chemical potential $0.697$ lies just below the band level $0.704$, so the HOMO is the band at $0.588$ and the gap is $0.116143$; at $T=0.3\,m$, $\mu=0.317$ and the gap becomes the distance $0.430734$ between the zero modes and the first band shell.

**With interaction.** The hot coupling changes $F$ at $T=m$ from $-11447.70$ to $-11447.48$ ($N=8$), with $\max|\lambda S_p|/m=0.104$; the $T=0$ coupling $\hat\lambda_1$ changes $F$ at $T=0.3\,m$ from $-30.5115$ to $-30.5037$ ($N=8$) and from $-12.4199$ to $-12.4103$ ($N=112$). The interaction stays a small correction at all temperatures computed.

![Mermin–Kohn–Sham thermodynamics for $m=1$, $L=3$: energy, free energy, entropy, heat capacity and Kohn–Sham gap against $T$ for $N=8$ and $N=112$ (filled: no interaction; open: with interaction), and the occupations of the $N=8$ levels at three temperatures, where the sea levels ($\varepsilon<0$) show their holes, the thermal antiparticles (file thermodynamics.png in artifacts/dirac16complex/kohn-sham/figures).](artifacts/dirac16complex/kohn-sham/figures/thermodynamics.png)

### 13.14 The energy–momentum tensor and the Einstein source

**The tensor of one orbital.** Insert the stationary orbital into the energy–momentum tensor of Chapter 7, $T_{\mu\nu}=-\tfrac14\bigl[\bar\Psi\gamma_\mu D_\nu\Psi+\bar\Psi\gamma_\nu D_\mu\Psi-(D_\mu\bar\Psi)\gamma_\nu\Psi-(D_\nu\bar\Psi)\gamma_\mu\Psi\bigr]+g_{\mu\nu}\mathcal L_s$, and use the expectation-value rule. The energy density is the simplest component. With $\gamma_4=-\gamma^4$, $D_4=\partial_4$ (the static connection has $\Omega_4=0$), $\partial_4\Psi=-i\varepsilon\Psi$ and $\partial_4\bar\Psi=+i\varepsilon\bar\Psi$, the bracket gives $-\tfrac14\bigl[2i\varepsilon\bar\Psi\gamma^4\Psi+2i\varepsilon\bar\Psi\gamma^4\Psi\bigr]=-i\varepsilon\Psi^\dagger C\gamma^4\Psi=\varepsilon\Psi^\dagger B\Psi$ (because $C\gamma^4=iB$), whose expectation is $\varepsilon\,u^\dagger B^2u=\varepsilon\,n$. With $g_{44}=-1$ the last term contributes $-\mathcal L_s$. On shell $\mathcal L_s=SU'(S)-U(S)$ (Chapter 7), and for $U=\tfrac\lambda2S^2$ this is $\tfrac\lambda2S^2$, whose expectation in the Kohn–Sham state is the interaction energy density of Section 13.8, $L_s=e_H+e_x=\tfrac\lambda2S_p^2-\tfrac\lambda{32}(n_p^2+S_p^2)$. The other components follow in the same way (they use the reduced equation of Section 13.3). The results for the Kohn–Sham state, a sum over all levels $n$ with the weights $w_n$ and the proper densities $n_n,s_n,t_n$ of Section 13.7, are

$$
\begin{aligned}
\rho(y)&=\sum_nw_n\,\varepsilon_n\,n_n(y)-L_s(y),\qquad
p_y(y)=\sum_nw_n\bigl[\varepsilon_nn_n-m\,s_n-\kappa k_n\,t_n\bigr]-L_s(y),\\
p_3(y)&=\tfrac13\sum_nw_n\,\kappa k_n\,t_n+L_s(y),\qquad p_t(y)=L_s(y),
\end{aligned}
$$

where $p_y=T^y{}_y$ is the pressure along the hidden direction, $p_3$ the average of the three 3-space pressures and $p_t$ the pressure along each extra time (`KS_emt_rho`, `KS_emt_py`, `KS_emt_p1`, `KS_emt_p2p3`, `KS_emt_pt`; `kohn-sham-theory.json`, keys `emt`, `ksState`). The off-diagonal components either are proportional to the $y$-current, which vanishes for eigenstates, or cancel over every closed shell $\{\mathbf k,-\mathbf k\}$ (`KS_emt_Ty4ProportionalToCurrent`, `KS_emt_Ty1ProportionalToCurrent`, `KS_emt_T41cancelsOverShell`, `KS_emt_offBlockComponentsVanishPerOrbital`). Without interaction $L_s=0$, so the extra times carry no pressure.

**Two identities that the solver checks.** (i) **Energy.** Each orbital has $\int n_n\,dV=\int e^{-6Hy}\chi_n^\dagger\chi_n\ell^{-3}\,e^{6Hy}\ell^3\,dy=1$, so $\int\rho\,dV=\sum_nw_n\varepsilon_n-E_H-E_x=E$, the total energy of Section 13.9 (check `energy_from_rho` of every run; for example $61.0907233$ both ways for $N=112$ at $\lambda=0$, `rust/emt/emt-summary.csv`). (ii) **Conservation.** For a static tensor that depends on $y$ only, $\nabla_\mu T^\mu{}_y=\partial_yT^y{}_y+\Gamma^\mu{}_{\mu y}T^y{}_y-\Gamma^\lambda{}_{\mu y}T^\mu{}_\lambda$. The Christoffel symbols of the warped metric are $\Gamma^\mu{}_{y\mu}=H$ on the six warped directions and $\Gamma^y{}_{\mu\mu}=-Hg_{\mu\mu}$ (`KS_geometry_christoffelClosedForms`), so $\Gamma^\mu{}_{\mu y}=6H$ and the last term is $H\bigl(3p_3+3p_t\bigr)$:

$$
p_y'+6H\,p_y-3H\,p_3-3H\,p_t=0 .
$$

The solver evaluates the left side for every self-consistent state (check `emt_conservation`); the normalized residual is at most $2.1\times10^{-5}$ (column `conservation_residual` of `emt-summary.csv`).

**Averages and equations of state.** Proper-volume averages are $\langle X\rangle=\int_{-L}^0X\,e^{6Hy}dy\big/\int_{-L}^0e^{6Hy}dy$, and $w_y=\langle p_y\rangle/\langle\rho\rangle$, $w_3=\langle p_3\rangle/\langle\rho\rangle$, $w_t=\langle p_t\rangle/\langle\rho\rangle$. The comparison with the required source asks which $\kappa$ would satisfy $\rho_{\text{req}}=-21H^2/\kappa=\langle\rho\rangle$, that is $\kappa_{\text{needed}}=-21H^2/\langle\rho\rangle$ (`rust/emt/emt-summary.csv`; $m=1$, $L=3$):

| $N$ | $\hat\lambda/\hat\lambda_1$ | $T/m$ | $\langle\rho\rangle$ | $w_y$ | $w_3$ | $\kappa_{\text{needed}}$ |
| --- | --- | --- | --- | --- | --- | --- |
| 8 | 0 | 0 | 0 | — | — | — |
| 8 | +1 | 0 | $-3.730\times10^{-7}$ | 9.01 | 0.991 | $+5.63\times10^{7}$ |
| 8 | $-1$ | 0 | $+3.730\times10^{-7}$ | 9.01 | 0.991 | $-5.63\times10^{7}$ |
| 112 | 0 | 0 | 0.0230891 | 0.449 | 0.297 | $-909.5$ |
| 112 | +1 | 0 | 0.0230976 | 0.452 | 0.297 | $-909.2$ |
| 112 | $-1$ | 0 | 0.0230807 | 0.447 | 0.297 | $-909.8$ |
| 112 | +1 | 0.3 | 0.0633668 | 0.322 | 0.274 | $-331.4$ |
| 1016 | 0 | 0 | 0.425999 | 0.336 | 0.290 | $-49.30$ |
| 1016 | +1 | 0 | 0.426008 | 0.336 | 0.290 | $-49.29$ |
| 1016 | $-1$ | 0 | 0.425989 | 0.336 | 0.290 | $-49.30$ |

**Reading the table.** Every state with band or bulk levels has a **positive** average energy density and positive pressures along the hidden direction and in 3-space ($w_y$ between 0.32 and 0.45, $w_3$ close to $0.3$): it is a gas of fast, nearly massless fermions, as the brane band suggests. The field needs the opposite sign, $\rho_{\text{req}}<0$. A positive $\langle\rho\rangle$ can match $\rho_{\text{req}}$ only with a **negative** gravitational coupling, $\kappa\approx-909$ for $N=112$ and $\kappa\approx-49$ for $N=1016$; with the physical sign $\kappa>0$ these states cannot be the source. For $N=8$ the energy density vanishes without interaction (the zero modes have $\varepsilon=0$), and with $\hat\lambda_1>0$ it is tiny and negative, $-3.73\times10^{-7}$, which would need $\kappa=5.6\times10^7$; but then the mass condition below gives the opposite sign of $\kappa$. There is a second, structural, obstacle: the required source is the same at every $y$, whereas the computed $\rho(y)$ changes by several orders of magnitude between the tip and the brane (figure below), so these states cannot match it point by point, and the comparison of averages is the most favourable one. (The specification had expected a positive Kohn–Sham energy density in every run; the measurement shows that this fails for $N=8$, `positiveRhoExpectation` in `rust/emt/summary.json`.)

**The sourcing conditions of erratum E4.1.** For the homogeneous state $\Psi=u(x_4)$ of Stage 2 the exact conditions under which dirac16complex sources the static field are $mS=-36H^2/\kappa$ and $\lambda S^2=30H^2/\kappa$ (Chapter 9); together they require $\lambda S/m=-5/6$ and $mS<0$. The solver evaluates them on the average scalar density $\langle S_p\rangle$ as a diagnostic (`E41_sourcingConditions` in each `run.json`). The ground states are dominated by the brane band, whose scalar charge is negative (Section 13.9), so $\langle S_p\rangle<0$: $-0.00788$ for $N=112$ and $-0.0872$ for $N=1016$ at $\lambda=0$. The mass condition alone then gives a positive $\kappa$ (4568 and 412.7), but the coupling condition needs $\lambda\langle S_p\rangle/m=-5/6$, whereas the computed states have $|\lambda\langle S_p\rangle/m|\le10^{-4}$ (the runs of `rust/emt/` use $\hat\lambda\in\{0,\pm\hat\lambda_1\}$). At first order the coupling would have to be $\hat\lambda\approx-\tfrac56m^7/\langle S_p\rangle=105.7$ ($N=112$) or $9.55$ ($N=1016$), about $10^3$ to $10^4$ times $\hat\lambda_2$, far outside the range in which this local scheme was set up. **In no computed run are the conditions met** (column `sourcing_conditions_met` of `emt-summary.csv` is 0 in every row). This is a statement about the computed states and couplings, not a proof that no Kohn–Sham state could ever source the field.

![Energy–momentum tensor of the ground states at $+\hat\lambda_1$ for $N=112$ and $N=1016$: the proper densities $\rho$, $p_y$, $p_3$, $p_t$ against $y$ (top), the local ratios $w_y(y)$ and $w_3(y)$ with the required value $w_{\text{req}}=-5/7$ (bottom left), and $\rho\,e^{6Hy}$, the energy per unit $y$ (bottom right) (file emt_profiles.png in artifacts/dirac16complex/kohn-sham/figures).](artifacts/dirac16complex/kohn-sham/figures/emt_profiles.png)

![The Kohn–Sham states against the source the static field requires: the proper-volume average of $\rho$ with $\rho_{\text{req}}$ for $\kappa=1$ (left), the $\kappa$ that would be needed (middle), and $\lvert\lambda\langle S_p\rangle/m\rvert$ against the value $5/6$ that erratum E4.1 requires (right) (file einstein_source.png in artifacts/dirac16complex/kohn-sham/figures).](artifacts/dirac16complex/kohn-sham/figures/einstein_source.png)

**The mirror sector: the Kohn–Sham form of the $\gamma^8$ map.** Chapter 15 proves that the chirality map $\Psi\to\gamma^8\Psi$ relates the theory with mass $m$ to the theory with mass $-m$. At the level of the $2\times2$ blocks this has a simple exact form, which we derive here (it is stated in the header of `src/emt.rs`). In the real system of Section 13.5 exchange the two components and the block type: $\tilde a=b$, $\tilde b=a$, $\tilde j=-j$. Then

$$
\begin{aligned}
\tilde a'&=b'=(jE-\kappa k)\,a-M_{\text{eff}}\,b=(jE-\kappa k)\,\tilde b-M_{\text{eff}}\,\tilde a\\
&=(-M_{\text{eff}})\,\tilde a-(\tilde jE+\kappa k)\,\tilde b,\\
\tilde b'&=a'=M_{\text{eff}}\,a-(jE+\kappa k)\,b=M_{\text{eff}}\,\tilde b-(jE+\kappa k)\,\tilde a\\
&=(\tilde jE-\kappa k)\,\tilde a-(-M_{\text{eff}})\,\tilde b ,
\end{aligned}
$$

which is the real system with the mass $-M_{\text{eff}}$, the same $\varepsilon$, $k$ and $v$. So every level of the problem with mass function $M_{\text{eff}}$ is also a level, with the same energy, of the problem with $-M_{\text{eff}}$, provided the boundary conditions are transformed as well: the tip condition $b(-L)=0$ becomes $\tilde a(-L)=0$ (the other bag, $\theta=\pi$), and the brane parities $+$ and $-$ are exchanged. The densities transform as $n\to n$ (since $a^2+b^2$ is symmetric) and $s\to-s$ (since $2jab\to2\tilde j\tilde a\tilde b=-2jab$). The map is consistent with self-consistency: $M_{\text{eff}}=m+\tfrac{15}{16}\lambda S_p$ becomes $-M_{\text{eff}}=-m+\tfrac{15}{16}\lambda(-S_p)$ **with the same $\lambda$**, and $v=-\lambda n_p/16$ is unchanged. Hence the Kohn–Sham problem $(m,\lambda)$ with the tip bag $b(-L)=0$ is mapped exactly onto the problem $(-m,\lambda)$ with the bag $a(-L)=0$: the same energies, number densities and pressures, the opposite scalar density, and therefore the same $mS$, the same $\lambda S^2$ and the same verdict on the E4.1 conditions. This is the Kohn–Sham shadow of the pairing theorems of Chapter 15; the full treatment there, including how the normal ordering and the particle–sea classification must be mapped, was still being completed when this chapter was written (`handoff/specs/STAGE5_SPEC.md`).

### 13.15 Convergence, reproducibility and the status of the cross-check

**Cutoff $L$.** The tip cutoff hardly matters once $L\ge3$: the Kohn–Sham gap of $N=8$ is $0.424302$, $0.430734$ and $0.430746\,m$ for $L=2$, 3 and 4, and the ground-state energy of $N=112$ is $60.725616$, $61.090723$ and $61.091032\,m$ (`rust/scf/summary.json`). Between $L=3$ and $L=4$ the energy changes by 5 parts in a million, because the brane band decays into the bulk like $e^{-(2M-H)|y|}$.

**Grid.** The run on 601 instead of 301 points ($N=112$, $\hat\lambda_1$) gives the same ground-state energy $61.1132120\,m$ to all printed digits (check `grid_refinement_energy`), and the hardest Delta-SCF changes from $0.0436184$ to $0.0436194\,m$ (Section 13.12).

**Torus spacing.** Halving $\Delta k$ to $0.125\,m$ at the same density means $N=8\cdot112=896$ (run `m1_L3_N896_lamp1_T0_dk0p125`). That value of $N$ is an **open** shell: 80 of the 192 states of the band shell at $k=0.468\,m$ are occupied, equally, so its Kohn–Sham gap is 0 by definition. Its energy per particle, $521.396546/896=0.581916\,m$, differs from the $N=112$ value $61.113212/112=0.545654\,m$ by 6.6 percent (erratum E4.11): the finite shell spacing of the torus still matters at this level of detail.

**The constant $a_{4,0}$.** The run with $a_{4,0}=0.5$ and its partner with $a_{4,0}=0$, $\Delta k\,e^{-0.5}=0.151633\,m$ and $\hat\lambda\,e^{1.5}$ (erratum E4.10; Exercise 13.12 explains the factors) have the same energy, $39.0088426\,m$, and the same levels (check `a4_rescaling_pair_exact`).

**Reproducibility.** Section 13.10 listed the determinism and refined-tolerance results. The canonical tree was produced with three release builds of the solver, which differ only in parts that do not change the other outputs; the solver's `README.md` records their provenance (section "Provenance of the canonical tree").

**The independent cross-check (status).** The Stage-4 plan requires every number to be reproduced by an independent Python reference solver, which uses a matrix method on a grid instead of shooting, and checked for the identities of this chapter (Hellmann–Feynman, current conservation, particle number, self-consistency) by `scripts/check_dirac16complex_kohn_sham.py`; the gate `scripts/verify_stage4_kohn_sham.ps1` (or `.sh`) then reproduces the Rust outputs byte for byte from a fresh copy of the repository. When this chapter was written these steps were **not finished**: the reference results under `artifacts/dirac16complex/kohn-sham/reference/` were being recomputed after the fixes of errata E4.8 to E4.12, and one comparison (the Delta-SCF of the smeared ensemble) was still outside its tolerance. The numbers of this chapter are those of the Rust solver with its own checks, and a reader should treat the final digits of the smeared-ensemble results as provisional until the Stage-4 gate reports `stage4_kohn_sham_verification=OK`.

### 13.16 What we proved and what we assumed

**Proved** (derived in this chapter step by step, and verified by the named checks of the two exact reports): the warped form of the static primordial field, its curvature $R=-42H^2$ and $G^\mu{}_\nu=\mathrm{diag}(15,15,15,15,21,15,15,15)H^2$, the required source $\rho_{\text{req}}=-21H^2/\kappa$, $p_{\text{req}}=+15H^2/\kappa$, the extrinsic curvature and the Israel stress of the Z2 brane in the stated sign convention; the removal of the spin connection by the factor $W^{-3}$ and the reduced equation; the splitting of the 16-component equation into eight $2\times2$ blocks with the explicit block forms of $A_0,A_1,A_4,B,C,BC$ and the two block types; the Hamiltonian form, the relation $h_{-1}-v=-(h_{+1}-v)$, the conservation of the $y$-current, the boundary conditions and the self-adjointness they give; the exact $k=0$ spectrum and the first-order splitting $\pm ck$ of the brane zero modes; the Hartree–Fock energy $\tfrac\lambda2[S^2-\mathrm{Tr}(BC\rho BC\rho)]$, the filled-shell ratio $1/8$ and the exact closed form $e_x=-\tfrac\lambda{32}(n^2+S^2)$ of the uniform gas at every temperature; the Kohn–Sham equations and Fermi–Dirac occupations from Mermin's functional, the double-counting formula and the Hellmann–Feynman relations; the energy density of an orbital, the identity $\int\rho\,dV=E$ and the conservation law $p_y'+6Hp_y-3Hp_3-3Hp_t=0$; the exact map of the Kohn–Sham problem $(m,\lambda)$ onto $(-m,\lambda)$ with exchanged boundary conditions; and (Exercise 13.9) the antisymmetry $E_0(-\lambda)=-E_0(\lambda)$ of the $N=8$ state.

**Computed** (by the Rust solver, with its own 397 checks, a byte-identical repeat and a refined-tolerance run; the independent cross-check and the Stage-4 gate were still being completed when this was written): the self-consistent ground states, the Kohn–Sham gaps, particle–hole lists and Delta-SCF energies, the finite-temperature thermodynamics, the energy–momentum tensor and its averages, and the comparison with the required source: positive $\langle\rho\rangle$ in every state with band or bulk levels (so a negative $\kappa$ would be needed), and the conditions of erratum E4.1 met in no run.

**Assumed or chosen:** the static member $a_4=\text{const}$ of the primordial family; the good sector without extra-time dependence; the Z2 gluing at $y=0$ with its brane; the tip cutoff $L$ and the bag condition $\theta=0$ there; the torus with $\Delta k=0.25\,m$ and the closed-shell particle numbers; the expectation-value rule and normal ordering against the free Dirac sea, with the zero modes counted as particle levels and the particle–sea classification by continuity from $\lambda=0$; the local (exchange-only) functional built on the uniform-gas closed form, with no correlation term; a fixed metric (no back-reaction); the definition of the ground state by continuation in $\lambda$ and the smeared ensemble at the one level crossing; and the use of Delta-SCF as the approximation to the first excited state. **Not claimed:** that such a Kohn–Sham state existed in any universe, that it sources the primordial field, or anything about the creation of universes; Chapters 15 and 16 treat the pairing questions.

### 13.17 Exercises

1. Using the two rules of Section 13.4, show that $J^2=1$ and $K_1^2=K_2^2=-1$, that $J$ commutes with $C$ and with $B$, and that $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7$ anticommutes with $J$ and commutes with $K_1$ and $K_2$.
2. Show that $A_0A_1A_4=-J$ and deduce $A_4\to j\sigma_1$ in the block basis.
3. From $C=A_1K_1$ and $B=-iJK_1$ derive the block forms of $C$, $B$ and $BC$.
4. Show that $\tilde\chi(y)=\sigma_3\chi(-y)$ solves the block equation with the mass function $-M(-y)$ if $\chi$ solves it with $M(y)$ (take $\kappa$ and $v$ even), and conclude when the reflection is a symmetry.
5. Check that $\chi=(e^{My},0)$ solves the block equation at $k=0$, $\varepsilon=0$, $v=0$ and satisfies the parity-$+$ and tip conditions. Compute its brane fraction (the fraction of $\int\chi^\dagger\chi\,dy$ within $|y|<1$) for $M=1$ and $L=2$ and $L=4$.
6. For $M=1$, $L=3$, compute the two lowest positive parity-$+$ levels and the lowest positive parity-$-$ level at $k=0$.
7. For $m=3$ ($H=1$) and $L=3$ compute $c$ and the first-order band energy $ck$ at the smallest torus momentum $k=0.25\,m=0.75\,H$. Compare with the Kohn–Sham gap $0.895833\,H$ of the free $N=8$ state for $m=3$ (`rust/scf/m3_L3_N8_lam0_T0/run.json`).
8. Prove $\frac d{dy}(\chi^\dagger\sigma_1\chi)=0$ for solutions of the block equation, and explain why a condition that kills the current at the tip makes it vanish everywhere.
9. Show that for $N=8$ at $T=0$ the ground states at $\lambda$ and $-\lambda$ are related by moving every occupied orbital from block type $j$ to $-j$, and deduce $E_0(-\lambda)=-E_0(\lambda)$ and $\varepsilon_{\text{HOMO}}(-\lambda)=-\varepsilon_{\text{HOMO}}(\lambda)$. Why does the argument fail for $N=112$?
10. Compute $S$ and $\mathrm{Tr}(BCP_+BCP_+)$ for the eight positive-energy states at rest, and the ratio $E_x/E_H$. Check that the uniform-gas closed form gives the same ratio when $S=n$.
11. Derive $E=\sum w\varepsilon-E_H-E_x$ and evaluate it for $N=8$ at $+\hat\lambda_1$, where the solver reports $\sum w\varepsilon=-0.00196448147$, $E_H=5.06259\times10^{-6}$ and $E_x=-0.000982711$.
12. Show that $a_{4,0}$ enters only through $k\,e^{-a_{4,0}}$, and that the problem with $a_{4,0}=0.5$ on the torus with $\Delta k=0.25\,m$ and coupling $\lambda$ is equivalent to the problem with $a_{4,0}=0$, $\Delta k'=0.25\,e^{-0.5}m$ and $\lambda'=\lambda\,e^{1.5}$.
13. Compute the $\kappa$ that the free $N=1016$ state would need to be the source, from $\langle\rho\rangle=0.425999$, and explain why its sign rules it out.
14. Repeat the Israel computation of Section 13.2 for the opposite gluing $W=e^{+H|y|}$ and find the sign of the brane energy density.
15. Check that the swap $(a,b,j)\to(b,a,-j)$ of Section 13.14 maps the tip condition $b(-L)=0$ to $\tilde a(-L)=0$, exchanges the brane parities, keeps $n$ and reverses $s$.

### 13.18 Answers to the exercises

1. $J$ is a product of $k=3$ gammas: $J^2=(-1)^{3}(\gamma^0)^2(\gamma^1)^2(\gamma^4)^2=(-1)(1)(1)(-1)=1$. For $K_1$ ($k=2$): $(-1)^1\cdot1\cdot1=-1$; for $K_2$: $(-1)^1(-1)(-1)=-1$. $J$ commutes with its factors $\gamma^0,\gamma^1$ and anticommutes with $\gamma^2,\gamma^3$, so moving $J$ through $C=\gamma^0\gamma^1\gamma^2\gamma^3$ gives the sign $(+1)(+1)(-1)(-1)=+1$; $J$ commutes with $\gamma^4$, hence with $B=-iC\gamma^4$. Every $\gamma^a$ is a factor of $\gamma^8$ ($k=8$), so $\gamma^a\gamma^8=(-1)^7\gamma^8\gamma^a$: $\gamma^8$ anticommutes with every gamma, hence with a product of three ($J$) and commutes with a product of two ($K_1$, $K_2$).
2. $A_0A_1A_4=\gamma^0\gamma^0\gamma^1\gamma^0\gamma^4=\gamma^1\gamma^0\gamma^4=-\gamma^0\gamma^1\gamma^4=-J$ (using $(\gamma^0)^2=1$ and one swap). In the block $J=j$, $A_0=\sigma_3$, $A_1=-i\sigma_2$, and $\sigma_3(-i\sigma_2)=-\sigma_1$; so $-\sigma_1A_4=-j$, and multiplying by $\sigma_1$ (with $\sigma_1^2=1$) gives $A_4=j\sigma_1$.
3. $C=\gamma^0\gamma^1\gamma^2\gamma^3=A_1K_1\to(-i\sigma_2)(is_2)=s_2\sigma_2$. $B=-iC\gamma^4=-iJK_1\to-i\cdot j\cdot is_2=js_2$. $BC\to js_2\cdot s_2\sigma_2=j\sigma_2$ (since $s_2^2=1$).
4. $\tilde\chi'(y)=-\sigma_3\chi'(-y)=-\sigma_3N(-y)\sigma_3\,\tilde\chi(y)$. With $\sigma_3\sigma_3\sigma_3=\sigma_3$ and $\sigma_3\sigma_{1,2}\sigma_3=-\sigma_{1,2}$, $-\sigma_3N(-y)\sigma_3=-M(-y)\sigma_3-\kappa(-y)k\sigma_2+ijE(-y)\sigma_1$, which for even $\kappa$ and $E$ is $N(y)$ with the mass function $-M(-y)$. The reflection maps the problem onto itself exactly when $M(y)=-M(-y)$, an odd mass function.
5. With $k=\varepsilon=v=0$ the block equation reads $\chi_1'=M\chi_1$, $\chi_2'=-M\chi_2$, solved by $(e^{My},0)$; $\chi_2=0$ at $y=0$ and $y=-L$. The fraction is $\int_{-1}^0e^{2y}dy\big/\int_{-L}^0e^{2y}dy=(1-e^{-2})/(1-e^{-2L})$: $0.880797$ for $L=2$ and $0.864955$ for $L=4$. The solver reports $0.8808$ and $0.8650$ for the free $N=8$ states (`rust/scf/m1_L2_N8_lam0_T0` and `m1_L4_N8_lam0_T0`), whose particles are exactly these zero modes.
6. Parity $+$: $\sqrt{1+(\pi/3)^2}=1.447972$ and $\sqrt{1+(2\pi/3)^2}=2.320881$. Parity $-$: the smallest positive root of $\tan(3p)=-p$ is $p=0.818548$, so $\varepsilon=\sqrt{1+p^2}=1.292293$.
7. $c=\frac{2M}{2M-H}\cdot\frac{1-e^{-(2M-H)L}}{1-e^{-2ML}}=\frac65\cdot\frac{1-e^{-15}}{1-e^{-18}}=1.1999997$, and $ck=0.9000\,H$ at $k=0.75\,H$. The exact level is $0.895833\,H$, only 0.5 percent lower. For $m=1$ the first-order value was 10.6 percent too high at the same $k/m$: the heavier zero mode is more strongly localized at the brane, where $\kappa\approx1$, so the linear approximation holds longer.
8. Section 13.5: $\frac d{dy}(\chi^\dagger\sigma_1\chi)=\chi^\dagger(N^\dagger\sigma_1+\sigma_1N)\chi=0$ because each Pauli matrix in $N$ anticommutes with $\sigma_1$ or, for the $\sigma_1$ term, appears with opposite signs in $N^\dagger$ and $N$. A quantity that is constant in $y$ and zero at $y=-L$ is zero everywhere, so the brane condition must, and does, also kill it; otherwise the eigenvalue problem would have no solution.
9. At $T=0$ only the eight zero-mode particle levels have nonzero weight (the sea is full, $w=-(1-f)=0$, and all other particle levels are empty). Move each occupied orbital $\chi$ unchanged from block type $j$ to $-j$ and replace $\lambda$ by $-\lambda$. Then $n_p$ is unchanged, $S_p\to-S_p$ (because $s=j\chi^\dagger\sigma_2\chi$), so $M_{\text{eff}}-m=\tfrac{15}{16}\lambda S_p$ is unchanged and $v=-\lambda n_p/16\to-v$. Writing $h_j=jD+v$ with $D$ built from $M_{\text{eff}}$, the new Hamiltonian is $-jD-v=-h_j$: the orbital is an eigenvector with the eigenvalue $-\varepsilon$, and the densities it produces are exactly those used, so the mapped state is self-consistent at $-\lambda$ (and it is the one reached by continuation, since both start from the same zero modes at $\lambda=0$; the zero modes are particle levels in both block types by convention). Then $\sum w\varepsilon\to-\sum w\varepsilon$, $E_H=\tfrac\lambda2\int S_p^2\to-E_H$ and $E_x\to-E_x$, so $E_0\to-E_0$, and $\varepsilon_{\text{HOMO}}\to-\varepsilon_{\text{HOMO}}$, as the table of Section 13.11 shows. For $N=112$ the occupied band levels have $\varepsilon>0$ and would be mapped to $\varepsilon<0$, which are sea levels; the mapped state is then not the ground state at $-\lambda$.
10. $S=\mathrm{Tr}(BCP_+)=8$ and $\mathrm{Tr}(BCP_+BCP_+)=\mathrm{Tr}(P_+)=8$ (Section 13.8), so $E_x/E_H=-\tfrac\lambda2\cdot8\big/\bigl(\tfrac\lambda2\cdot64\bigr)=-\tfrac18$. With $S=n$ the closed form gives $e_x=-\tfrac\lambda{32}\cdot2S^2=-\tfrac\lambda{16}S^2=-\tfrac18\cdot\tfrac\lambda2S^2$, the same ratio.
11. Section 13.9: the potentials of the two quadratic functionals contribute $2E_H+2E_x$ to $\sum w\varepsilon$. Numerically $E=-0.00196448147-0.00000506259+0.00098271090=-0.00098683316$, the reported $E_0=-9.86833\times10^{-4}$.
12. $a_{4,0}$ appears only in $\kappa=e^{-Hy-a_{4,0}}$ (the volume factor $e^{6Hy}$ does not contain it), so $\kappa k=e^{-Hy}(ke^{-a_{4,0}})$. The torus momenta $0.25\,m\,(n_1,n_2,n_3)$ become $0.25\,e^{-0.5}m\,(n_1,n_2,n_3)=0.151633\,m\,(n_1,n_2,n_3)$: the partner has $\Delta k'=0.151633\,m$ and $\ell'=\ell e^{0.5}$, with the same orbitals $\chi(y)$ and levels. Its proper densities $e^{-6Hy}\chi^\dagger\chi/\ell'^3$ are smaller by $e^{-1.5}$, so the potentials $\tfrac{15}{16}\lambda S_p$ and $-\lambda n_p/16$ agree only if $\lambda'=\lambda e^{1.5}$. The energies agree as well: $E_H\propto\lambda\int S_p^2e^{6Hy}\ell^3dy$ changes by $e^{1.5}\cdot e^{-3}\cdot e^{1.5}=1$, and likewise $E_x$.
13. $\kappa=-21H^2/\langle\rho\rangle=-21/0.425999=-49.30$. A negative $\kappa$ would reverse the sign of the gravitational coupling (a repulsive gravity for positive energy); with the physical sign $\kappa>0$ the required $\rho_{\text{req}}$ is negative, while this state has $\langle\rho\rangle>0$.
14. For $W=e^{+H|y|}$ the extrinsic curvature is $-H$ just below the brane and $+H$ just above, so $[K^\mu{}_\mu]=+2H$ on the six warped directions and $[K]=+12H$. Then $S^\mu{}_\mu=-(2H-12H)/\kappa=+10H/\kappa$ and $S^4{}_4=-(0-12H)/\kappa=+12H/\kappa$, so $\rho_{\text{brane}}=-S^4{}_4=-12H/\kappa<0$: this gluing would need a brane of negative energy. (It does not glue the notebook's patch, whose warp decreases toward the tip.)
15. The tip condition $b(-L)=0$ reads $\tilde a(-L)=0$ because $\tilde a=b$. At the brane, parity $+$ ($b(0)=0$) becomes $\tilde a(0)=0$, which is parity $-$ of the new system, and vice versa. $\tilde a^2+\tilde b^2=a^2+b^2$ keeps $n$, and $2\tilde j\tilde a\tilde b=-2jab$ reverses $s$.
