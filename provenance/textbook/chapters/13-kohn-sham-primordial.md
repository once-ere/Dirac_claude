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

**The pieces of the Dirac operator.** The vielbein is diagonal with entries $h=(1,\ e^{Hy+a_{4,0}}\,(\times3),\ 1,\ e^{Hy-a_{4,0}}\,(\times3))$, so the curved gammas are $\gamma^y=\gamma^0$, $\gamma^{x_l}=e^{-Hy-a_{4,0}}\gamma^l$ for $l=1,2,3$, $\gamma^{x_4}=\gamma^4$, and $\gamma^{x_l}=e^{-Hy+a_{4,0}}\gamma^l$ for $l=5,6,7$. The spin connection enters only through the contraction $\gamma^\mu\Omega_\mu$ (Chapters 4 and 9). For a diagonal vielbein that depends on one coordinate only, the formula of Chapter 4, $\gamma^\mu\Omega_\mu=\tfrac12\sum_b\frac1{h_b}\,\partial_b\ln\bigl(\prod_{c\ne b}h_c\bigr)\gamma^b$, has a single term, $b=y$, and $\prod_{c\ne y}h_c=e^{6Hy}$:

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
