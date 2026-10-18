# dirac16complex in the primordial gravitational field: Kohn–Sham density-functional theory of the ground and first excited states

## The static warped field and its brane, the exact reduction to eight two-component blocks, the exactly local exchange, the Kohn–Sham fermion-gas thermodynamics pseudo-potential, two independent solvers, and the comparison with the source the field requires

## Abstract

This is the Stage-4 document of the dirac16complex project. It records every idea and every result of a Kohn–Sham treatment (Mermin's finite-temperature density-functional theory) of the ground and first excited states of dirac16complex, the complex Grassmann-odd 16-component spinor field of Pin(4,4) of Stages 1 to 3, in the static member of the author's primordial gravitational field. In the proper hidden coordinate $y=\ln(\sin z)/(6H)\le0$ the field is the warped product $ds^2=dy^2-dx_4^2+e^{2Hy}[e^{2a_4}d\vec x^{\,2}-e^{-2a_4}d\vec y^{\,2}]$ with $R=-42H^2$; 8-dimensional Einstein gravity would need the source $\rho_{\mathrm{req}}=-21H^2/\kappa<0$, $p_{\mathrm{req}}=+15H^2/\kappa$. Two copies glued at $y=0$ (the notebook's pair of universes) make $y=0$ a brane with the Israel stress $\rho_{\mathrm{brane}}=+12H/\kappa$, $p_{\mathrm{brane}}=-10H/\kappa$, and the tip $y\to-\infty$, where the transverse space pinches off, is cut off at $y=-L$. The stationary ansatz $\Psi=e^{-i\varepsilon x_4}e^{i\vec k\cdot\vec x}e^{-3Hy}\chi(y)$ removes the spin connection exactly, and an explicit unitary basis splits the 16-component equation into eight $2\times2$ blocks of two inequivalent types $j=\pm1$, $\chi'=[M_{\mathrm{eff}}\sigma_3-\kappa k\sigma_2+ij(\varepsilon-v_v)\sigma_1]\chi$ with $\kappa(y)=e^{-Hy-a_4}$. The Fock exchange of the contact interaction $U=\tfrac\lambda2S^2$ of the uniform gas is exactly local at every temperature, $e_x=-(\lambda/32)(n^2+S^2)$ (a filled shell at one momentum has $E_x=-E_H/8$); the Kohn–Sham fermion-gas thermodynamics pseudo-potential is the local pair $M_{\mathrm{eff}}=m+\tfrac{15}{16}\lambda S_p$, $v_x=v_v=-\lambda n_p/16$. No correlation term is included: the contact interaction beyond Hartree–Fock is not renormalisable in 8 dimensions. The equations were solved by CVODE shooting in a Rust program, independently by a staggered-grid matrix solver in numpy, and in part by a Mathematica notebook. For $m=H=1$, $L=3$ and a 3-torus with $\Delta k=0.25m$: the ground states are dominated by the massless brane band $\varepsilon=\pm ck$, $c=1.9051482536$; without interaction the ground-state energies are $0$, $61.090723$ and $1127.136625$ (in units of $m$) for the closed shells $N=8$, 112 and 1016, with Kohn–Sham gaps $0.4307337$, $0.0955462$ and $0.0530077$; between 86.7 % and 96.2 % of the particles lie within $1/H$ of the brane. With the attractive coupling $-\hat\lambda_2$ at $N=1016$ an 8-fold $k=0$ level crosses the 192-fold band at the Fermi level under self-consistency; that ground state is converged with an occupation smearing of $10^{-3}m$ at the physical $T=0$, and its Kohn–Sham gap $0.0412551$ and Delta-SCF $0.0436184$ refer to this ensemble. Every state with bulk levels has a positive proper-volume average of the energy density ($\langle\rho\rangle=0.0230891$ for $N=112$), so the required source would need $\kappa=-909.5$, a negative gravitational coupling; for $N=8$ the average vanishes or is tiny ($-3.7\times10^{-7}$). The static sourcing conditions of erratum E4.1, $mS=-36H^2/\kappa$ and $\lambda S^2=30H^2/\kappa$, are met in no run: they would need couplings $10^3$ to $10^4$ times the largest used. All 125 exact Wolfram checks, all 157 independent sympy checks, all 397 self-checks of the Rust program and all 94 checks of the Mathematica notebook pass; a repeated Rust run is byte-identical in 330 files and a run with tighter tolerances agrees to $5.96\times10^{-8}$. The run-by-run cross-check against the reference solver (python-check-report.json) was being regenerated when this edition was written; Section 13.4 states exactly what it contains and what is pending.

## 1. The question and the short answer

The question of this stage is: *compute, by a Kohn–Sham (density-functional) approximation, the ground state and the first excited state of dirac16complex in the primordial gravitational field, with an exchange functional derived from the thermodynamics of the uniform dirac16complex gas, and state what the result means for the field.*

The short answer, which Sections 4 to 12 argue in full:

- **The problem is exactly two-dimensional in spinor space.** The static field is a warped product, the stationary ansatz removes the spin connection, and an explicit basis reduces the 16-component equation to eight $2\times2$ blocks of two inequivalent types (Section 5).
- **The exchange is exactly local.** For the contact interaction the Fock energy of the isotropic uniform gas is $-(\lambda/32)(n^2+S^2)$ at every temperature, so the "fermion-gas thermodynamics pseudo-potential" is a closed-form local pair, not a fitted table (Section 6).
- **The ground state lives on the brane.** The $k=0$ chiral zero mode $\chi=(e^{My},0)$ and the band $\varepsilon=\pm ck$ that grows out of it hold the particles near $y=0$; the momentum is confined by $\kappa(y)=e^{-Hy}$, which grows toward the tip (Sections 5.7 and 8).
- **The first excited state is a particle-hole excitation across the shell gap of the torus** (Section 9); interaction changes it at the $10^{-2}$ level, except at $N=1016$ with the attractive $-\hat\lambda_2$, where a level crossing at the Fermi level makes the exact $T=0$ aufbau oscillate and an occupation-smeared ensemble is the converged ground state (Section 9.3).
- **The field is not sourced by this state.** The field needs $\rho_{\mathrm{req}}=-21H^2/\kappa<0$; every Kohn–Sham state with bulk levels has $\langle\rho\rangle>0$, so the match would need $\kappa<0$, and the E4.1 conditions under which a homogeneous condensate can source the field are not met by any computed state (Section 11).
- **Everything is verified twice or more**: exact theory in Wolfram and sympy, a Rust shooting solver, an independent matrix solver, a Mathematica notebook and a Jupyter notebook (Section 13).

## 2. Scope and sources of this document

**Scope.** The object is the Stage-1 field with the Lagrangian of Section 6.1 in the static primordial field of Section 4. Only the good sector (no dependence on the extra times $x_5,x_6,x_7$) is treated. The many-body approximation is Kohn–Sham at the level of Hartree plus the exact local exchange (Section 6). All results are for a finite coordinate 3-torus and a finite tip cutoff $L$.

**Sources of the numbers.** Every computed number in this document is copied from a committed output: the exact reports `wolfram-kohn-sham-report.json`, `python-theory-report.json` and `kohn-sham-theory.json`; the Rust summaries `rust/{spectrum,scf,excited,thermo,emt}/summary.json` with their per-run files and `rust/determinism-report.json`; the reference outputs `reference/reference-summary.json`; `notebook-report.json` and `mathematica-report.json` (all under `artifacts/dirac16complex/kohn-sham/`; full list with hashes in Section 14). A number derived here by one arithmetic step from those files (a difference, a ratio) is marked as derived. Statements of method are taken from the module headers of the programs named in Section 7. The binding specifications are the Stage-4 specification with its errata E4.1 to E4.13, the physics contract with its errata E1 to E5 and the numerics contract of Stage 3 (all in `handoff/specs/`).

**Status of this edition.** Parts of the Stage-4 outputs were being regenerated by the lead when this edition was written: the reference run `m1_L3_N1016_lamm2_T0` (moved to finer grids by erratum E4.13), the reference summary, the cross-checker report `python-check-report.json` (not yet committed) and, following them, `notebook-report.json` and the notebook figure `rust_vs_reference.png`. Every number quoted from those files is pinned by the test `tests/test_d16c_kohn_sham_primordial_publication.py`, which names each quoted number that no longer matches after the regeneration.

## 3. Notation and conventions

### 3.1 Coordinates, frame and gamma matrices

- Everything is counted from 0: coordinates $x_0,\dots,x_7$, frame indices $a=0,\dots,7$, spinor components $\Psi_0,\dots,\Psi_{15}$. The tangent metric is $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$: directions 0 to 3 are space-like, 4 to 7 time-like. $x_4$ is the evolution time, $x_0$ the hidden space, $x_1,x_2,x_3$ the 3-space (written $\vec x$) and $x_5,x_6,x_7$ the three extra times (written $\vec y$ in the line element only).
- $\gamma^a$ are the real integer $16\times16$ matrices of the split-octonion (notebook) basis of the committed algebra fixture, $\{\gamma^a,\gamma^b\}=2\eta^{ab}$; $(\gamma^0)^2=+1$ and $(\gamma^4)^2=-1$. $C=\gamma^0\gamma^1\gamma^2\gamma^3$ is the charge matrix, $\bar\Psi=\Psi^\dagger C$, $B=-iC\gamma^4$ is Hermitian with $B^2=1$, and $BC=-i\gamma^4$. The chirality is $\gamma^8=\gamma^0\cdots\gamma^7=\mathrm{diag}(-I_8,I_8)$.
- **Expectation-value rule** (numerics contract): for a one-particle state built on a Hilbert-normalised mode $u$, $\langle\Psi^\dagger M\Psi\rangle=u^\dagger BMu$. Hence the number density of a mode is $u^\dagger u\ge0$, its scalar density $u^\dagger BCu$, its y-current $u^\dagger\gamma^0\gamma^4u$ and its $x_1$-current $u^\dagger(-\gamma^4\gamma^1)u$.
- Spin connection $\Omega_\mu=\tfrac18\omega_{\mu ab}[\gamma^a,\gamma^b]$ with $\omega_{\mu ab}=\eta_{ac}\,\omega_\mu{}^c{}_b$ (the notebook's contraction $\omega_\mu{}^a{}_bS^{ab}$ is wrong; physics contract Section 3).
- Einstein equations $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ with $\kappa$ the 8-dimensional gravitational coupling; $\rho=-T^4{}_4$ and $p_{(i)}=T^i{}_i$ (no sum) for the observer $u=\partial_4$.

### 3.2 Units and parameters

- $H=1$ throughout the numerics; $m/H\in\{1,3\}$. Energies, momenta and temperatures are quoted in units of $m$; densities per unit coordinate 3-volume and unit coordinate extra-time volume carry powers of $m$ (proper densities $n_p$, $S_p$ in $m^7$, energy densities in $m^8$ when $m=H=1$).
- The dimensionless coupling is $\hat\lambda=\lambda m^6$; $[\lambda]=\mathrm{mass}^{-6}$ because $[\Psi]=7/2$ in 8 dimensions. The values $\hat\lambda_1$ and $\hat\lambda_2=10\hat\lambda_1$ are set per configuration $(m,L,N)$ (Section 7.1); run labels write them as `lamp1`, `lamm1`, `lamp2`, `lamm2` for $+\hat\lambda_1$, $-\hat\lambda_1$, $+\hat\lambda_2$, $-\hat\lambda_2$ and `lam0` for $\lambda=0$.
- **Sign convention for the coupling:** $\lambda>0$ is repulsive and $\lambda<0$ attractive (the Hartree mass shift $\lambda S$ raises the energy of a state with positive scalar density for $\lambda>0$).
- A run label such as `m1_L3_N112_lamp2_T0` gives $m/H$, $L$, $N$, the coupling and $T/m$ (`T0p3` is $T=0.3m$); the suffix `_g601` marks a 601-point grid, `_a40p5` the run with $a_{4,0}=0.5$ and `dk0p125` the torus with $\Delta k=0.125m$.

### 3.3 Two labellings of the block type

The exact theory labels the two inequivalent block types by the eigenvalue $j=\pm1$ of $J=\gamma^0\gamma^1\gamma^4$. The Rust program and the reference solver label them by $s=-j$ (measured and recorded in `rust/spectrum/theory-agreement.json`, note `labelRelation`, and by the Mathematica check `rustLabelSIsMinusJEigenvalue`). Both types enter every sum with the same multiplicity, so no result depends on the label; this document uses $j$ in formulas and names $s$ only where a program output is quoted.

### 3.4 Symbols that are used twice

- $\kappa$ is the gravitational coupling; $\kappa(y)=e^{-Hy-a_4}$ is the momentum weight of the reduced equation. The function always carries its argument.
- $S$ is the scalar density $\bar\Psi\Psi$; $S_{\mathrm{ent}}$ is the entropy. $s$ is the Rust block label and also the scalar density of one orbital in Section 5.8; the context says which.
- $c$ is the slope of the brane band (Section 5.7) and $c_\beta$ the y-current density of block $\beta$.
- $z=6Hx_0$ is the notebook's hidden-space variable (there is no redshift in this document).
- $n$ is a density ($n_c$ coordinate, $n_p$ proper) and also a level index; $N$ is the particle number.

## 4. The static primordial field

### 4.1 The static member of the notebook family

The author's notebook defines the primordial (pair-creation) field on the patch $z=6Hx_0\in(0,\pi/2)$ with $t=Hx_4$:

$$
g=\mathrm{diag}\bigl(\cot^2z,\ s^{1/3}e^{2a_4(t)}\ (\times3),\ -1,\ -s^{1/3}e^{-2a_4(t)}\ (\times3)\bigr),\qquad s=\sin z .
$$

Stage 2 verified its geometry for an arbitrary $a_4(t)$. A stationary ground state needs a time-independent metric, so Stage 4 takes the **static member** $a_4=a_{4,0}$, a constant ($a_4'=a_4''=0$). The canonical runs use $a_{4,0}=0$; Section 5.10 shows that any other constant is a rescaling of the momenta.

### 4.2 The proper hidden coordinate and the warped form

Define the proper hidden coordinate

$$
y=\frac{\ln\sin z}{6H}\in(-\infty,0],\qquad \sin z=e^{6Hy},\qquad dy=\cot z\,dx_0 .
$$

Then $g_{00}\,dx_0^2=\cot^2z\,dx_0^2=dy^2$ and $s^{1/3}=e^{2Hy}$, and the line element becomes the warped product

$$
ds^2=dy^2-dx_4^2+e^{2Hy}\Bigl[e^{2a_{4,0}}\bigl(dx_1^2+dx_2^2+dx_3^2\bigr)-e^{-2a_{4,0}}\bigl(dx_5^2+dx_6^2+dx_7^2\bigr)\Bigr]
$$

with the warp $W(y)=e^{Hy}$ and the diagonal vielbein $h=(1,\,e^{Hy+a_{4,0}}\ (\times3),\,1,\,e^{Hy-a_{4,0}}\ (\times3))$ in the order $(y,x_1,\dots,x_7)$. The square root of the determinant is $\sqrt{|g|}=W^6=e^{6Hy}$, the proper 7-volume per unit coordinate volume (Wolfram check `KS_geometry_sqrtDetG_W6`). The notebook chart ends at $y=0$ ($z=\pi/2$, where $\cot z=0$), although the $y$ form of the metric is regular there.

### 4.3 Curvature and the Einstein source the field requires

The Christoffel symbols have 18 nonzero components, $\Gamma^y{}_{ii}=-Hg_{ii}$ and $\Gamma^i{}_{yi}=\Gamma^i{}_{iy}=H$ for the six warped directions $i\in\{x_1,x_2,x_3,x_5,x_6,x_7\}$. The seven directions other than $x_4$ form a space of constant sectional curvature $-H^2$ and signature (4,3), times the flat time line $x_4$. Hence (exact, in the order $y,x_1,\dots,x_7$)

$$
\begin{aligned}
&R=-42H^2,\qquad R^\mu{}_\nu=\mathrm{diag}(-6,-6,-6,-6,0,-6,-6,-6)\,H^2,\\
&G^\mu{}_\nu=\mathrm{diag}(15,15,15,15,21,15,15,15)\,H^2,\\
&R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=84H^4,\qquad R_{\mu\nu}R^{\mu\nu}=252H^4 .
\end{aligned}
$$

All invariants are constant: the field is a regular homogeneous space, and $y=0$ is the end of the notebook chart, not a curvature singularity. If 8-dimensional Einstein gravity produced this field, its source would have to be

$$
\rho_{\mathrm{req}}=-T^4{}_4=-\frac{21H^2}{\kappa}<0,\qquad p_{\mathrm{req}}=T^i{}_i=+\frac{15H^2}{\kappa}\quad(\text{all seven }i\ne x_4),\qquad w_{\mathrm{req}}=-\frac57 .
$$

**Erratum E4.3.** The Stage-4 specification (Section 1) wrote $p_{\mathrm{req}}=-15H^2/\kappa$; the exact mixed components give $+15H^2/\kappa$ in all seven transverse directions. The same values are re-derived numerically from the Christoffel symbols by the Rust program (`rust/spectrum/geometry.json`: $R=-42$, $G^\mu{}_\nu=(15,15,15,15,21,15,15,15)$, $\rho_{\mathrm{req}}=-21$ and $p_{\mathrm{req}}=15$ for $\kappa=H=1$, numerical curvature defect $8.3\times10^{-12}$).

### 4.4 The tip

As $y\to-\infty$ ($z\to0$) the warp $W^6=e^{6Hy}$ tends to zero: the transverse 6-space pinches off at infinite proper distance. This end is called the **tip**. It is a genuine singular end of the transverse geometry, and the proper densities of any normalisable orbital grow there like $e^{-6Hy}$ times the coordinate density. The Kohn–Sham problem is therefore solved on $y\in[-L,0]$ with a cutoff $L\in\{2,3,4\}/H$ and a current-free bag condition at $y=-L$ (Section 5.9); Section 8.6 reports the dependence on $L$.

### 4.5 Extrinsic curvature and the two extensions beyond y = 0

A surface $y=\mathrm{const}$ with the unit normal $n=+\partial_y$ has $K_{ij}=\tfrac12\partial_yg_{ij}$, hence $K^i{}_j=H\delta^i{}_j$ on the six warped directions and $K^4{}_4=0$ ($K=6H$). Two continuations past $y=0$ are documented; the Kohn–Sham problem uses the second:

- **(E1) smooth:** $W=e^{Hy}$ for all real $y$ (the $\zeta$ chart of Stage 2 continued). No brane; the geometry is the homogeneous space of Section 4.3 on the whole line.
- **(E2) Z2 mirror:** $W=e^{-H|y|}$, two copies of the notebook patch glued at $y=0$. This is the notebook's hypothesis of a pair of universes, realised as a geometry. The surface $y=0$ is then a brane at which the extrinsic curvature jumps.

### 4.6 The Z2 brane and its Israel stress

**Sign convention** (fixed once, recorded in `kohn-sham-theory.json`): $[X]=X(0^+)-X(0^-)$, the normal $n=+\partial_y$ points from $y<0$ to $y>0$, $K_{ij}=h_i{}^\mu h_j{}^\nu\nabla_\mu n_\nu=\tfrac12\partial_yg_{ij}$, and the Israel junction condition reads $[K_{ij}]-h_{ij}[K]=-\kappa S_{ij}$ with $h_{ij}$ the induced metric and $S_{ij}$ the stress carried by the brane. With $W=e^{-H|y|}$, $K^i{}_i(0^-)=+H$ and $K^i{}_i(0^+)=-H$ (no sum) on the six warped directions and $0$ on $x_4$, so $[K^i{}_i]=-2H$ there and $[K]=-12H$. Therefore

$$
S^i{}_j=-\frac1\kappa\bigl([K^i{}_j]-\delta^i{}_j[K]\bigr)=-\frac{H}{\kappa}\,\mathrm{diag}(10,10,10,12,10,10,10)\quad\text{on }(x_1,x_2,x_3,x_4,x_5,x_6,x_7),
$$

and the brane carries the energy density $\rho_{\mathrm{brane}}=-S^4{}_4=+12H/\kappa>0$ and the pressure $p_{\mathrm{brane}}=-10H/\kappa$ in all six warped directions. It is not a pure tension ($\rho_{\mathrm{brane}}\ne-p_{\mathrm{brane}}$). The same convention gives the Randall–Sundrum brane a positive tension $6k/\kappa$. The Rust program reproduces the stress from the numerical jump with defect $0$ (`geometry.json`). This is a statement about what the glued geometry would need; Stage 4 does not show that such a brane exists or is sourced. The induced metric of the brane is flat (`KS_geometry_inducedMetricFlat`).

On the $y>0$ side the reduced equation of Section 5.3 has the same form with $\kappa(y)=e^{Hy-a_{4,0}}$, an even function of $y$ (`KS_reduction_mirrorPatchSameForm`); the problem is solved on $y\le0$ with boundary conditions at the brane.

### 4.7 The ±M mirror pair: a structural remark

**This remark is structural, not physical.** The map $\Psi\to\gamma^8\Psi$ sends the Lagrangian $\mathcal L_{m,U}$ to $-\mathcal L_{-m,-U}$ (physics contract, erratum E2): a mirror copy carrying $\gamma^8\Psi$ has mass $-m$ (and coupling $-\lambda$ for $U=\tfrac\lambda2S^2$), the notebook's "$\pm M$ pair". In the reduced problem the brane reflection $\chi(y)\to\gamma^0\chi(-y)$ maps a solution with the mass function $M(y)$ onto one with $-M(-y)$: it is a symmetry exactly when $M_{\mathrm{eff}}$ is odd across the brane, that is, when the mirror universe carries the opposite mass (erratum E4.6, Section 5.9). Section 11.4 states the Kohn–Sham form of this map. Nothing in Stage 4 shows that a big bang produces such a pair, or that the mirror copy exists.

## 5. Sector, ansatz and the exact reduction to 2×2 blocks

### 5.1 Field equation and the spin connection

In the mean field the quanta obey the Stage-1 field equation with an effective mass, $\gamma^\mu D_\mu\Psi=M_{\mathrm{eff}}\Psi$, $M_{\mathrm{eff}}=m+U'(S)$ at the Hartree level (Section 6 adds the exchange). In the static field the vielbein postulate holds in all 512 components, 12 components $\omega_{\mu ab}$ are nonzero, and

$$
\begin{aligned}
&\Omega_y=\Omega_4=0,\qquad \Omega_{x_i}=-He^{Hy+a_{4,0}}S^{0i}\ (i=1,2,3),\qquad \Omega_{x_j}=+He^{Hy-a_{4,0}}S^{0j}\ (j=5,6,7),\\
&\gamma^\mu\Omega_\mu=3H\gamma^0 ,
\end{aligned}
$$

independent of $a_{4,0}$, with $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$. The divergence identity $\partial_\mu(\sqrt{|g|}\gamma^\mu)=\sqrt{|g|}[\gamma^\mu,\Omega_\mu]$ holds (Wolfram checks `KS_reduction_vielbeinPostulate512`, `KS_reduction_OmegaClosedForms`, `KS_reduction_gammaSlashOmega3Hgamma0`, `KS_reduction_divergenceIdentity`).

### 5.2 The good sector and the stationary ansatz

**Sector.** $\Psi$ does not depend on the extra times $x_5,x_6,x_7$ (extra-time momenta $q=0$). Modes with $q\ne0$ have a non-Hermitian single-particle operator and grow without bound (Stage 1 and the Stage-3 experiment EXP-5), so they are excluded. The 3-space is a coordinate torus of size $\ell$ with $\vec k\in(2\pi/\ell)\mathbb Z^3$; $\ell$ is chosen so that $\Delta k=2\pi/\ell=0.25m$.

**Ansatz.**

$$
\Psi=e^{-i\varepsilon x_4}\,e^{i\vec k\cdot\vec x}\,W(y)^{-3}\,\chi(y),\qquad W^{-3}=e^{-3Hy},
$$

with $\chi(y)\in\mathbb C^{16}$. The factor $W^{-3}$ is chosen so that the derivative $\partial_y(e^{-3Hy}\chi)=e^{-3Hy}(\chi'-3H\chi)$ cancels the spin-connection term $3H\gamma^0$ exactly; without it the term survives (`KS_reduction_ansatzRemoves3H`, `KS_reduction_withoutW3the3HTermSurvives`).

### 5.3 The reduced equation

Dividing the field equation by the common factor gives

$$
\gamma^0\chi'+i\kappa(y)\,k_j\gamma^j\chi-i\varepsilon\gamma^4\chi=M_{\mathrm{eff}}(y)\chi,\qquad \kappa(y)=e^{-Hy-a_{4,0}},
$$

and since $(\gamma^0)^2=+1$, an ordinary differential equation $\chi'=\gamma^0[M_{\mathrm{eff}}\chi-i\kappa k_j\gamma^j\chi+i\varepsilon\gamma^4\chi]$. Three properties:

1. **Flat measure.** $\sqrt{|g|}\,\Psi^\dagger\Psi=\chi^\dagger\chi$, so an orbital is normalised by $\int_{-L}^0\chi^\dagger\chi\,dy=1$ with the ordinary measure (`KS_reduction_flatMeasure`).
2. **Confinement.** The momentum enters with the weight $\kappa(y)=e^{-Hy-a_{4,0}}$, which grows toward the tip: momentum costs more energy far from the brane, so the quanta are pushed toward $y=0$.
3. **Rotations.** The spectrum depends on $|\vec k|$ only (`KS_reduction_rotationalSymmetry`); all computations take $\vec k=(k,0,0)$, and then only $A_0=\gamma^0$, $A_1=\gamma^0\gamma^1$ and $A_4=\gamma^0\gamma^4$ appear: $\chi'=[M_{\mathrm{eff}}A_0-i\kappa kA_1+i(\varepsilon-v_v)A_4]\chi$, where the vector exchange potential $v_v$ of Section 6.5 has been included.

### 5.4 Block diagonalisation: commuting operators and the explicit basis

The operators

$$
J=\gamma^0\gamma^1\gamma^4\ (J^2=1),\qquad K_1=\gamma^2\gamma^3\ (K_1^2=-1),\qquad K_2=\gamma^5\gamma^6\ (K_2^2=-1)
$$

commute with each other and with $\gamma^0$, $\gamma^0\gamma^1$, $\gamma^0\gamma^4$, $B$ and $C$. Their joint eigenspaces are the ranges of the rank-2 projectors

$$
P(j,s_2,s_3)=\tfrac12(1+jJ)\cdot\tfrac12(1-is_2K_1)\cdot\tfrac12(1-is_3K_2),\qquad j,s_2,s_3=\pm1,
$$

eight blocks whose projectors sum to 1. In each block the basis is

$$
v_+=8P(j,s_2,s_3)\tfrac12(1+\gamma^0)e_c,\qquad v_-=\gamma^0\gamma^1v_+ ,
$$

with $e_c$ the first standard basis vector with a nonzero image. The entries are in $\{0,\pm1,\pm i\}$ and $|v_\pm|^2=8$, so the matrix $V=[v_+\,v_-\,\cdots]/(2\sqrt2)$ is unitary, and $\chi_{16}=V\chi_{\mathrm{block}}$. The block index is $\beta=4(1-j)/2+2(1-s_2)/2+(1-s_3)/2$, that is

$$
\begin{aligned}
(j,s_2,s_3)={}&(1,1,1),\ (1,1,-1),\ (1,-1,1),\ (1,-1,-1),\\
&(-1,1,1),\ (-1,1,-1),\ (-1,-1,1),\ (-1,-1,-1)
\end{aligned}
$$

for $\beta=0,\dots,7$. The unnormalised basis matrix $2\sqrt2\,V$ (rows: spinor components $\Psi_0,\dots,\Psi_{15}$; columns: $v_+,v_-$ of block 0, then block 1, and so on), exported exactly in `kohn-sham-theory.json`, is

```text
        blk0    blk1    blk2    blk3    blk4    blk5    blk6    blk7
row 0:   0  i    1  0    1  0    0 -i    1  0    0  i    0 -i    1  0
row 1:   0 -1   -i  0    i  0    0 -1    i  0    0  1    0  1   -i  0
row 2:   0 -i    1  0    1  0    0  i   -1  0    0  i    0 -i   -1  0
row 3:   0 -1    i  0   -i  0    0 -1    i  0    0 -1    0 -1   -i  0
row 4:   1  0    0  i    0 -i    1  0    0  i    1  0    1  0    0 -i
row 5:   i  0    0  1    0  1   -i  0    0 -1   -i  0    i  0    0 -1
row 6:  -1  0    0  i    0 -i   -1  0    0 -i    1  0    1  0    0  i
row 7:   i  0    0 -1    0 -1   -i  0    0 -1    i  0   -i  0    0 -1
row 8:   0 -i    1  0    1  0    0  i    1  0    0 -i    0  i    1  0
row 9:   0  1   -i  0    i  0    0  1    i  0    0 -1    0 -1   -i  0
row 10:  0  i    1  0    1  0    0 -i   -1  0    0 -i    0  i   -1  0
row 11:  0  1    i  0   -i  0    0  1    i  0    0  1    0  1   -i  0
row 12:  1  0    0 -i    0  i    1  0    0 -i    1  0    1  0    0  i
row 13:  i  0    0 -1    0 -1   -i  0    0  1   -i  0    i  0    0  1
row 14: -1  0    0 -i    0  i   -1  0    0  i    1  0    1  0    0 -i
row 15:  i  0    0  1    0  1   -i  0    0  1    i  0   -i  0    0  1
```

(the seed columns $c$ are 4, 0, 0, 4, 0, 4, 4, 0 for $\beta=0,\dots,7$). The Wolfram verifier proves that $V$ is unitary, is a joint eigenbasis, block-diagonalises the five matrices $\gamma^0,\gamma^0\gamma^1,\gamma^0\gamma^4,B,C$ and reconstructs them from their blocks; $\gamma^2\gamma^3$ itself is not block diagonal (checks `KS_reduction_basisUnitary` to `KS_reduction_gamma2gamma3NotBlockDiagonal`). The real algebra generated by $A_0,A_1,A_4$ has dimension 8; its commutant has dimension 32, and 16 together with $B$ and $C$. The chirality $\gamma^8$ anticommutes with $J$ and commutes with $K_1$, $K_2$: it maps block $(j,s_2,s_3)$ onto $(-j,s_2,s_3)$. The Rust constants generator verifies the same reduction in Gaussian-integer arithmetic for its own basis (`rust/generator-report.json`), and the programs' block forms agree with this basis (Section 13.1).

### 5.5 The block matrices, the block equation and the block Hamiltonian

In every block (exact):

| operator | block form | operator | block form |
| --- | --- | --- | --- |
| $A_0=\gamma^0$ | $\sigma_3$ | $B$ | $js_2$ (a number) |
| $A_1=\gamma^0\gamma^1$ | $-i\sigma_2$ | $C$ | $s_2\sigma_2$ |
| $A_4=\gamma^0\gamma^4$ | $j\sigma_1$ | $BC=-i\gamma^4$ | $j\sigma_2$ |
| $\gamma^4\gamma^1$ | $-j\sigma_3$ | $J,\ K_1,\ K_2$ | $j,\ is_2,\ is_3$ |

Hence the 16-component equation is eight copies of the **block equation** (erratum E4.7)

$$
\chi'=N\chi,\qquad N=M_{\mathrm{eff}}(y)\,\sigma_3-\kappa(y)\,k\,\sigma_2+ij\bigl(\varepsilon-v_v(y)\bigr)\sigma_1 ,
$$

in components $\chi_1'=M_{\mathrm{eff}}\chi_1+(i\kappa k+ij(\varepsilon-v_v))\chi_2$ and $\chi_2'=-M_{\mathrm{eff}}\chi_2+(-i\kappa k+ij(\varepsilon-v_v))\chi_1$. It is equivalent to the eigenvalue problem of the block Hamiltonian

$$
h_j\chi=\varepsilon\chi,\qquad h_j=j\Bigl[-i\sigma_1\frac{d}{dy}+M_{\mathrm{eff}}(y)\,\sigma_2+\kappa(y)\,k\,\sigma_3\Bigr]+v_v(y)
$$

(`KS_reduction_blockODEMatrix`, `KS_reduction_blockHamiltonianEquivalentToODE`).

**Real form used by the programs.** With $\chi=(a,ib)$ and the program label $s=-j$ the system is real, $a'=M_{\mathrm{eff}}a+(s(\varepsilon-v_x)-\kappa k)b$, $b'=-(s(\varepsilon-v_x)+\kappa k)a-M_{\mathrm{eff}}b$ (the equation printed by `print-config`; Mathematica check `realFormIsBlockODEWithSMinusJ`).

### 5.6 Two block types and the degeneracy

For the y-equation the eight blocks form two inequivalent types, $j=+1$ (blocks 0 to 3) and $j=-1$ (blocks 4 to 7), four blocks each; together with $B$ and $C$ there are four types $(j,s_2)$ of two blocks each. The two $j$-types have opposite Hamiltonians up to the vector potential (erratum E4.4):

$$
h_{-1}-v_v=-(h_{+1}-v_v),\qquad \mathrm{spec}(h_{-1}-v_v)=-\mathrm{spec}(h_{+1}-v_v).
$$

At a fixed $\vec k=(k,0,0)$ every level of $h_{+1}$ is 4-fold (blocks 0 to 3) and every level of $h_{-1}$ is 4-fold. The map $\sigma_3N(k,j)\sigma_3=N(-k,-j)$ at fixed $\varepsilon$ makes the $(k,j)$ and $(-k,-j)$ orbitals equal in $\lvert\chi\rvert^2$ and in their scalar densities, so every level is 8-fold at $k=0$ and over every closed lattice shell $\{\vec k,-\vec k\}$. A lattice shell $\lvert\vec k\rvert^2=(\Delta k)^2n_2$ with $r_3(n_2)$ lattice vectors contributes $4r_3(n_2)$ states per level of each type.

### 5.7 Exact solutions at k = 0 and the brane band

For $k=0$, a constant $M_{\mathrm{eff}}=M$, $v_v=0$, the even brane parity $\chi_2(0)=0$ and the tip bag $\chi_2(-L)=0$ (Section 5.9) the spectrum is exact:

- the **chiral zero mode** $\varepsilon=0$, $\chi=(e^{My},0)$, normalisable on $(-\infty,0]$ for $M>0$ and localised at the brane; its proper density is $n_p\propto e^{(2M-6H)y}$, which grows toward the tip for $M<3H$;
- the massive levels $\varepsilon=\pm\sqrt{M^2+(n\pi/L)^2}$, $n=1,2,\dots$, with $\chi_2=\sin(n\pi y/L)$;
- with the odd brane parity $\chi_1(0)=0$ and the same tip condition the levels solve $\tan(pL)=-p/M$, $p^2=\varepsilon^2-M^2$ (Mathematica check `parityMinusIsTanPLMinusPOverM`).

Each level is 4-fold per $j$, 8-fold in total. For $k\ne0$ the zero mode splits linearly (first-order Hellmann–Feynman in $k$):

$$
\frac{d\varepsilon_0}{dk}\Big|_{k=0}=j\,c,\qquad c=\frac{\int_{-L}^0e^{-Hy-a_{4,0}}e^{2My}dy}{\int_{-L}^0e^{2My}dy}=e^{-a_{4,0}}\,\frac{2M}{2M-H}\,\frac{1-e^{-(2M-H)L}}{1-e^{-2ML}}>0 .
$$

For $M=H=1$, $L=3$ this is $c=2/(1+e^{-3})=1.9051482536$ (exact theory; Mathematica check `splittingAtM1H1L3Is2Over1PlusExpMinus3`). The zero-mode band $\varepsilon=\pm ck+O(k^2)$, four states at $+ck$ and four at $-ck$ for each $\vec k$, is the massless brane fermion of the orbifold. The Rust program measures the slope $-1.9051482524522905$ for its $s=+1$ blocks (theory: $+c$ for $j=+1$, i.e. $s=-1$), and the Mathematica notebook's NDSolve shooting agrees with the closed form to $1.6\times10^{-7}$.

### 5.8 Densities and currents of an orbital

For a Hilbert-normalised block orbital ($\int\chi^\dagger\chi\,dy=1$) the expectation-value rule gives the proper densities (per unit coordinate 3-volume)

$$
n=\frac{e^{-6Hy}}{\ell^3}\chi^\dagger\chi,\qquad s=\frac{e^{-6Hy}}{\ell^3}\chi^\dagger(j\sigma_2)\chi,\qquad t=\frac{e^{-6Hy}}{\ell^3}\chi^\dagger(j\sigma_3)\chi,\qquad c=\frac{e^{-6Hy}}{\ell^3}\chi^\dagger(j\sigma_1)\chi ,
$$

the number, scalar, $x_1$-current and y-current densities ($s=u^\dagger BCu$, $t=u^\dagger B(-\gamma^4\gamma^1)u$, $c=u^\dagger B(-iC\gamma^0)u$). The coordinate densities are $n_c=e^{6Hy}n_p$, $S_c=e^{6Hy}S_p$. **The y-current** is $J^y=-i\bar\Psi\gamma^0\Psi$; after the expectation rule its matrix is $A_4=\gamma^0\gamma^4$ ($B$ is absorbed: $B(-iC\gamma^0)=-\gamma^4\gamma^0$; erratum E4.5 corrects the specification's "$B\gamma^4\gamma^0$"), with the block form $j\sigma_1$. For real $\varepsilon$, $M_{\mathrm{eff}}$ and $v_v$, $N^\dagger A_4+A_4N=0$, so $\chi^\dagger A_4\chi$ is constant in $y$ for every solution, while the Hilbert norm density $\chi^\dagger\chi$ is not (`KS_boundary_currentConservedAlongY`, `KS_boundary_hilbertNormNotConservedAlongY`).

### 5.9 Boundary conditions

**At the brane** the Z2 parity conditions $\Psi(-y)=\pm\gamma^0\Psi(y)$ become $(1\mp\gamma^0)\chi(0)=0$, and since $\gamma^0=\sigma_3$ in every block: **even parity $\chi_2(0)=0$, odd parity $\chi_1(0)=0$** (in the real form $b(0)=0$ and $a(0)=0$). Either condition kills the current $\chi^\dagger\sigma_1\chi=2\,\mathrm{Re}(\chi_1^{\ast}\chi_2)$ at $y=0$. Both parities are solved and filled together as one system.

**Parities are boundary conditions, not symmetries (erratum E4.6).** The reflection $P_A:\chi(y)\to\gamma^0\chi(-y)$ maps a solution with the mass function $M(y)$ onto one with $-M(-y)$; it is a symmetry of the Z2 problem only for an odd mass function (the $\pm M$ mirror pair of Section 4.7). Under $P_A$ the number density and the $x_1$-current are even and the scalar density and the y-current odd, consistent with an odd Hartree shift $\lambda S_p$. The symmetry of an even mass function (an identical mirror universe) is $P_B:\chi(y)\to i\gamma^0\gamma^8\chi(-y)$; it also kills the current, but it anticommutes with $J$ and couples block $(j,s_2,s_3)$ with $(-j,s_2,s_3)$, so the Kohn–Sham problem would become a $4\times4$ system on block pairs. The Kohn–Sham problem uses the block-level conditions of $P_A$ type.

**At the tip** the chiral-bag family

$$
\bigl(1-Q(\theta)\bigr)\chi(-L)=0,\qquad Q(\theta)=\cos\theta\,\sigma_3+\sin\theta\,\sigma_2,\qquad Q^\dagger=Q,\ Q^2=1,\ \{Q,\sigma_1\}=0,
$$

kills the current, since $\chi^\dagger\sigma_1\chi=\chi^\dagger\sigma_1Q\chi=-\chi^\dagger Q\sigma_1\chi=-\chi^\dagger\sigma_1\chi$ for $Q\chi=\chi$. In the 16-component form $Q(\theta)=\cos\theta\,\gamma^0+i\sin\theta\,\gamma^0\gamma^1$. The canonical choice is $\theta=0$: $\gamma^0\chi(-L)=+\chi(-L)$, i.e. $\chi_2(-L)=0$ ($b(-L)=0$), the even-parity condition at the tip. For $M>0$ it admits no tip-localised zero mode and it admits the brane zero mode $e^{My}$ for every $L$. In signature (4,4) $(\gamma^0)^2=+1$, so this MIT-type condition carries no factor $i$. With any pair of current-killing end conditions the boundary term $-ij[\phi^\dagger\sigma_1\chi]$ of $\langle\phi|h\chi\rangle-\langle h\phi|\chi\rangle$ vanishes, $h_j$ is self-adjoint, the levels are real and orbitals of different $\varepsilon$ are orthogonal in the flat measure (`KS_boundary_selfAdjointBoundaryTerm`).

### 5.10 The constant $a_{4,0}$ is a momentum rescaling

$a_{4,0}$ enters only through $\kappa(y)$, as $k\to ke^{-a_{4,0}}$ (`KS_reduction_a4IsMomentumRescaling`). A run with $a_{4,0}=0.5$ is therefore exactly equivalent to the $a_{4,0}=0$ problem with $\Delta k\,e^{-0.5}$, $\ell\,e^{0.5}$ and $\lambda\,e^{1.5}$ (erratum E4.10: the partner torus is larger by $e^{1.5}$ in coordinate volume, so the same Hartree and exchange potentials need $\lambda e^{1.5}$; label `lamp1rescaled`). Section 8.6 reports the numerical equivalence.

## 6. The interaction: Hartree term, exact local exchange and the pseudo-potential

### 6.1 The Lagrangian and the mean-field equation

The field is the Stage-1 dirac16complex field with its Hermitian first-order Lagrangian and the contact self-interaction $U(S)=\tfrac\lambda2S^2$:

$$
\mathcal L=\sqrt{|g|}\Bigl[\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)-m\,\bar\Psi\Psi-\frac\lambda2\bigl(\bar\Psi\Psi\bigr)^2\Bigr],\qquad S=\bar\Psi\Psi ,
$$

with the field equation $\gamma^\mu D_\mu\Psi=(m+\lambda S)\Psi$ (Stage-1 document, Section 7). In 8 dimensions $[\Psi]=7/2$, so $[\lambda]=\mathrm{mass}^{-6}$ (`KS_exchange_couplingDimension`) and the dimensionless coupling is $\hat\lambda=\lambda m^6$. All operators are normal ordered with respect to the free Dirac sea. A Kohn–Sham state is described by its one-body density matrix $\rho=\sum_nf_nu_nu_n^\dagger$ over Hilbert-normalised modes $u_n$ with occupations $f_n$; by the expectation-value rule $\langle\Psi^\dagger X\Psi\rangle=\mathrm{Tr}(BX\rho)$.

### 6.2 The Hartree–Fock energy of the contact interaction

For a Slater determinant, and with occupations $f_n$ for the Mermin ensemble, the fermionic Wick theorem gives the interaction energy density

$$
e_{\mathrm{int}}=\frac\lambda2\Bigl[\bigl(\mathrm{Tr}\,BC\rho\bigr)^2-\mathrm{Tr}\bigl(BC\rho\,BC\rho\bigr)\Bigr],\qquad S=\mathrm{Tr}\,BC\rho ,
$$

the Hartree (direct) term minus the Fock (exchange) term. It was verified exactly on a Fock space of four modes for one-, two- and three-particle Slater determinants (`KS_exchange_wickTheoremHF`). Three consequences follow.

- **Hartree term.** $E_H=\tfrac\lambda2\int S_p^2\,dV_7$ with $dV_7=e^{6Hy}\ell^3dy$, and the Hartree mass shift is $M_H=\lambda S_p$.
- **The Fock term of a contact interaction is local.** Both density matrices are taken at the same point. In the block basis, with the $2\times2$ block density matrix $\rho_\beta=\tfrac12(n_\beta+s_\beta\sigma_2+t_\beta\sigma_3+c_\beta\sigma_1)$ (number, scalar, $x_1$-current and y-current densities of block $\beta$),

$$
E_x^{\mathrm{HF}}=-\frac\lambda4\int dV_7\sum_{\beta=0}^{7}\bigl(n_\beta^2+s_\beta^2-t_\beta^2-c_\beta^2\bigr)
$$

(`KS_exchange_blockFormOfFockTerm`). The y-current densities $c_\beta$ vanish for the standing waves of Section 5.9, and the $x_1$-current densities cancel in the sum over a closed shell $\{\vec k,-\vec k\}$; their squares do not.
- **A filled shell.** Eight positive-energy states at one momentum $p$ have $\mathrm{Tr}(BCP_+)=8m/E_p$ and $\mathrm{Tr}(BCP_+BCP_+)=8m^2/E_p^2=S^2/8$, so $E_x=-E_H/8$ (`KS_exchange_filledShellOneEighth`; the Rust program measures the defect $3.6\times10^{-15}$, `rust/spectrum/exchange-check.json`).

### 6.3 The uniform gas: the exchange is exactly local at every temperature

The local-density approximation needs the exchange energy of the uniform gas. Take the 8-fold degenerate relativistic gas of mass $M$ with the normal-ordered density matrix $\rho=\int\frac{d^dp}{(2\pi)^d}\bigl[f_+(p)P_+(p)-f_-(p)P_-(p)\bigr]$, where $P_\pm=\tfrac12(1\pm h_p/E_p)$, $h_p=-iM\gamma^4-\gamma^4\gamma^jp_j$, $E_p=\sqrt{M^2+p^2}$, and $f_\pm$ are the Fermi–Dirac occupations of particles and of antiparticles (holes of the sea). The exact trace identity

$$
\mathrm{Tr}\bigl[BC\,P_a(p)\,BC\,P_b(q)\bigr]=4\Bigl[1+ab\,\frac{M^2-p\cdot q}{E_pE_q}\Bigr],\qquad a,b=\pm1
$$

(`KS_exchange_kernelPlusPlus`, `KS_exchange_kernelPlusMinus`) makes the double momentum integral separable. For isotropic occupations the angular average kills $p\cdot q$ (`KS_exchange_angularAverageOfPdotQVanishes`), and

$$
e_x(n,S)=-\frac{\lambda}{32}\bigl(n^2+S^2\bigr),\qquad n=8\int\frac{d^dp}{(2\pi)^d}\,(f_+-f_-),\qquad S=8\int\frac{d^dp}{(2\pi)^d}\,\frac M{E_p}\,(f_++f_-)
$$

holds exactly, at every temperature and for every isotropic occupation (`KS_exchange_uniformGasClosedForm`, `KS_exchange_antiparticleConvention`). The temperature enters only through $n$ and $S$; antiparticles count negatively in $n$ and positively in $S$. The vector part $-\lambda n^2/32$ and the scalar part $-\lambda S^2/32$ come from the two terms of the kernel, and the closed form does not depend on the number $d$ of momentum dimensions. In the four spatial dimensions $(y,x_1,x_2,x_3)$ of the exact theory the $T=0$ gas has $n=k_F^4/(4\pi^2)$, $S=\frac{M}{3\pi^2}\bigl[(k_F^2-2M^2)\sqrt{M^2+k_F^2}+2M^3\bigr]$ and $dS/dn=M/E_F$ (`KS_exchange_T0_density`, `KS_exchange_T0_scalarDensity`, `KS_exchange_T0_dSdn`); for $k_F\to0$ the gas is at rest, $S=n$ and $e_x=-e_H/8$, the filled-shell result (`KS_exchange_restGasLimit`).

**Independent cross-check: the exchange table.** The independent sympy checker tabulates $e_x(n,T)$ by direct double momentum quadrature with the raw kernel and an exact angular rule (`exchange-table.json`: tables `d4` and `d3` of 290 rows each). Its largest relative deviation from the closed form is $5.1\times10^{-15}$ (recorded in the file); the Rust program reads the table and finds $5.3\times10^{-15}$ (`d4`) and $1.7\times10^{-14}$ (`d3`) (`rust/spectrum/exchange-table-check.json`). Because the closed form is exact, both solvers implement it directly and keep the table only as this cross-check (erratum E4.7).

![The exchange energy density of the uniform 8-fold gas. Left: $-e_x/\lambda$ against the number density at $T/m=0$, $0.3$, $1$ and $2$, closed form (lines) and the double quadrature of the table (markers). Right: the relative deviation of every table row from the closed form, both tables (an exactly vanishing deviation is drawn at $10^{-18}$).](artifacts/dirac16complex/kohn-sham/figures/exchange_uniform_gas.png)

### 6.4 The Kohn–Sham fermion-gas thermodynamics pseudo-potential

**Definition.** The local-density approximation evaluates the uniform-gas functional at the local proper densities $n_p(y)$ and $S_p(y)$. Its functional derivatives are two local potentials,

$$
v_s=\frac{\partial e_x}{\partial S}=-\frac{\lambda}{16}\,S_p\quad(\text{mass type}),\qquad v_v=\frac{\partial e_x}{\partial n}=-\frac{\lambda}{16}\,n_p\quad(\text{vector type}),
$$

and the **Kohn–Sham fermion-gas thermodynamics pseudo-potential** of this document is the local pair

$$
M_{\mathrm{eff}}(y)=m+\lambda S_p(y)+v_s(y)=m+\tfrac{15}{16}\,\lambda S_p(y),\qquad v_x(y):=v_v(y)=-\tfrac1{16}\,\lambda\,n_p(y),
$$

built from the Hartree–Fock thermodynamics of the uniform dirac16complex gas (the Mermin functional of Section 6.5), together with the gravitational terms that the reduction already contains: the spin connection $3H\gamma^0$, absorbed by $W^{-3}$; the momentum weight $\kappa(y)$; and the boundary conditions. $M_{\mathrm{eff}}$ enters as the mass and $v_x$ as $\varepsilon\to\varepsilon-v_x(y)$ (Section 5.5). The pair is exact for the uniform gas at every temperature. It is a thermodynamic potential in the sense that it is the derivative of the exchange free energy of the gas at the local $(n,S)$; the temperature acts only through the local densities.

**Which equation is solved (a recorded deviation from the specification).** The specification (Section 3) recommended the variant with $M_{\mathrm{eff}}=m+\lambda S_p$ and the single potential $v_x=de_x(n,T)/dn$, evaluated with the uniform-gas scalar density $S_u(n,T)$ (variant V). Because the uniform-gas exchange is an exact local function of both densities, the functional of Section 6.5 has both derivatives, and its stationarity gives the pair above (variant VS; `KS_functional_stationarityGivesKSEquation`). Variant V is also derived exactly (`KS_functional_variantV`) and is available in the reference solver as an option, but every canonical run of both solvers uses VS. The exact Hartree–Fock alternative, the matrix potential $-\lambda\,BC\rho(y)BC$ (block form $-\lambda\sigma_2\rho_\beta\sigma_2$), differs from VS by the $t_\beta^2$ terms and by the block resolution of the densities; it is not used.

**Strength.** Per unit $\hat\lambda$ the pair $(M_{\mathrm{eff}}-m,v_x)$ has the size $\max_y\max\bigl(\tfrac{15}{16}|S_p|,\,n_p/16\bigr)/m^7$ in units of $m$, which Section 7.1 uses to set the couplings. The proper densities are the coordinate densities times $e^{-6Hy}$, so the pseudo-potential is largest near the tip, not at the brane where most particles are (Section 8.3).

**Signs.** For $\lambda>0$ the vector potential $v_x$ is negative everywhere and lowers every level in proportion to the proper density it sees; $M_{\mathrm{eff}}-m$ has the sign of $\lambda S_p$. The scalar density of a positive-energy orbital is positive for the massive bulk levels, exactly zero for the $k=0$ zero modes and negative for the brane band (Section 11.4), so the scalar and vector parts do not simply add.

### 6.5 The Mermin–Kohn–Sham functional and equations

With orbitals $\chi_n$ of block type $j_n$ and momentum $k_n$ and occupations $f_n$, the Mermin free-energy functional is

$$
F\bigl[\{\chi_n\},\{f_n\}\bigr]=\sum_nf_n\langle\chi_n|h_0|\chi_n\rangle-TS_{\mathrm{ent}}[f]+E_H[S_p]+E_x[n_p,S_p],
$$

with $h_0=j\bigl[-i\sigma_1\tfrac{d}{dy}+m\sigma_2+\kappa(y)k\sigma_3\bigr]$, $S_{\mathrm{ent}}=-\sum_n\bigl[f_n\ln f_n+(1-f_n)\ln(1-f_n)\bigr]$, $E_H=\tfrac\lambda2\int S_p^2\,dV_7$ and $E_x=-\tfrac\lambda{32}\int(n_p^2+S_p^2)\,dV_7$, under the constraints $\int\chi_n^\dagger\chi_n\,dy=1$ (multipliers $\varepsilon_n$) and $\sum_nf_n=N$ (multiplier $\mu$). Its stationarity gives, exactly (`KS_functional_stationarityGivesKSEquation`, `KS_functional_stationarityConjugate`, `KS_functional_fermiDiracOccupations`):

1. the block Kohn–Sham equations $\chi_n'=\bigl[M_{\mathrm{eff}}\sigma_3-\kappa k_n\sigma_2+ij_n(\varepsilon_n-v_x)\sigma_1\bigr]\chi_n$ of Section 5.5; the factor $e^{-6Hy}$ of the proper densities cancels the $e^{6Hy}$ of $dV_7$, so the equation is local with the flat measure;
2. the Fermi–Dirac occupations $f_n=1/(e^{(\varepsilon_n-\mu)/T}+1)$, with $\mu$ fixed by the particle number;
3. the energy with the double-counting correction $E=\sum_nf_n\varepsilon_n-E_H-E_x$ (`KS_functional_totalEnergyDoubleCounting`), the free energy $F=E-TS_{\mathrm{ent}}$ and the grand potential $\Omega=F-\mu N$ (`KS_functional_merminStructure`).

At the self-consistent state the Hellmann–Feynman (envelope) identities hold: $dF/d\lambda=(E_H+E_x)/\lambda$, $dF/dm=\int S_p\,dV_7$, $dF/dT=-S_{\mathrm{ent}}$, and at fixed potentials $d\varepsilon_n/dk=j\int\kappa\,\chi_n^\dagger\sigma_3\chi_n\,dy$ (the three Wolfram checks `KS_functional_hellmannFeynman*`). The Rust program checks $dE/dm$ (Section 13.2) and the cross-checker checks the first two by finite differences of self-consistent reference runs (Section 13.4).

**Normal ordering, branches and the particle number.** Occupations are counted with respect to the free Dirac sea. A level is a particle state if its non-interacting partner, the level with the same shell, parity, block type and Prüfer (rank) index at $\lambda=0$, has $\varepsilon\ge0$, and a sea state otherwise; the sign of the interacting $\varepsilon$ is not used (for $\lambda>0$ the vector potential moves the $k=0$ zero modes to $\varepsilon=\langle v_x\rangle<0$, and they stay particle states). A particle state carries the weight $w=f(\varepsilon)$, a sea state $w=-(1-f(\varepsilon))$, because a hole in the sea is an antiparticle; $N=\sum\mathrm{mult}\cdot w$ is the net particle number, and the entropy runs over all states. At $T=0$ the sea stays full and the particle states are filled in the order of $\varepsilon$ (aufbau); a shell that straddles $N$ is filled equally and fractionally. In the real form $\chi=(a,ib)$ of Section 5.5 the densities are $n_c(y)=\sum\mathrm{mult}\cdot w\,(a^2+b^2)/\ell^3$ and $S_c(y)=\sum\mathrm{mult}\cdot w\,(-2sab)/\ell^3$, with the proper densities $n_p=e^{-6Hy}n_c$ and $S_p=e^{-6Hy}S_c$ (per unit coordinate extra-time volume).

### 6.6 What is neglected

- **Correlation.** No correlation functional is added. With $[\lambda]=\mathrm{mass}^{-6}$ the contact interaction beyond Hartree–Fock is not renormalisable in 8 dimensions, so there is no uniform-gas correlation energy to build a functional from. The Kohn–Sham levels of this document are those of Hartree plus local exchange.
- **The structure of the exact Fock term.** The exact Fock term of an inhomogeneous state is local in $y$ but depends on the block-resolved densities $(n_\beta,s_\beta,t_\beta)$ of Section 6.2; the local-density approximation uses only the totals $n_p$ and $S_p$. The size of the difference is not computed here.
- Everything listed in Section 12: the fixed field without back-reaction, the good sector, the finite torus and tip cutoff, and the static member of the field.

## 7. Numerical method and parameters

### 7.1 Parameters, closed shells and couplings

**Fixed parameters** (every canonical run unless a label says otherwise): $H=1$, $a_{4,0}=0$, $\Delta k=2\pi/\ell=0.25m$ (for $m=1$: $\ell=8\pi=25.1327$, coordinate 3-volume $\ell^3=15875.21$), tip cutoff $L=3$, the canonical bag $\chi_2(-L)=0$, both brane parities filled together, potentials on a grid of 301 points in $y\in[-L,0]$. Varied: $L\in\{2,3,4\}$, $m/H\in\{1,3\}$, $N$, $\hat\lambda$ and $T/m\in\{0,0.1,0.3,1\}$, plus three convergence runs (a 601-point grid, $\Delta k=0.125m$, and $a_{4,0}=0.5$ with its exact rescaling partner).

**Closed shells.** The particle numbers are closed shells of the non-interacting aufbau at $L=3$ (`rust/spectrum/closed-shells-m1-L3.csv`, `closed-shells-m3-L3.csv`). For $m=1$ the shells close at $N=8$, 32, 80, 112, 136, 232, 328, 376, 496, 592, 688, 696, 728, 824, 1016, 1040, 1048, 1072, 1264, 1408 (twenty entries); for $m=3$ at 8, 32, 80, 112, 136, ... (twenty-two entries). The study uses $N=8$ (the eight $k=0$ zero modes, one shell), $N_{\mathrm{mid}}=112$ (the closed shell nearest 100, for both masses) and $N_{\mathrm{large}}=1016$ (the closed shell nearest 1000, for $m=1$), where the Fermi level lies at $\varepsilon_{\mathrm{HOMO}}=0$, $0.7040996$ and $1.3859192$ for $m=1$ and $0$ and $1.5420110$ for $m=3$ ($N=8$, 112, 1016 and $N=8$, 112).

**Couplings** (Rust `runs.rs`; the reference solver applies the same rule to its own free states). No single $\hat\lambda$ keeps the pseudo-potential in the window $0.1$ to $1\,m$ of the specification for all configurations: the proper densities near the tip scale like $e^{6HL}$ and grow with $N$ (measured: the $N=112$ value gives $|\lambda S_p|/m=11$ in the free $N=1016$ state, and the attractive self-consistent loop at that coupling runs away). The couplings are therefore set per configuration $(m,L,N)$ from the free ground state of that configuration: $\mathrm{strength}=\max_y\max\bigl(\tfrac{15}{16}|S_p|,\,n_p/16\bigr)/m^7$, $\hat\lambda_1=0.1/\mathrm{strength}$, $\hat\lambda_2=1/\mathrm{strength}$, so that the pseudo-potential reaches $0.1m$ and $1m$ at first order. For $N=8$ the free scalar density vanishes exactly (the zero modes have $s=0$) and the vector part sets the scale. The values (from `rust/spectrum/summary.json` and the `run.json` of each run) are:

```text
 m  L     N   strength [m per lambda_hat]   lambda_hat_1      lambda_hat_2
 1  3     8   10.27760799                   9.729890471e-3    9.729890471e-2
 1  3   112   10.45176178                   9.567764950e-3    9.567764950e-2
 1  3  1016   634.1388136                   1.576941797e-4    1.576941797e-3
 1  2     8   0.1912777276                  0.5228000209      -
 1  2   112   2.375459679                   4.209711529e-2    -
 1  4     8   559.9352972                   1.785920632e-4    -
 1  4   112   559.9352992                   1.785920626e-4    -
 3  3     8   2.333010339e-6                42863.07623       -
 3  3   112   1.172828328e-4                852.6397056       -
```

The self-consistent values of $\max_y|\lambda S_p|/m$ and $\max_y|v_x|/m$ are recorded in every `run.json` and reach $1.37$ and $1.50$ at most ($N=1016$, $-\hat\lambda_2$). For $m=3$ the zero mode $(e^{My},0)$ has the proper density $e^{(2M-6H)y}$, which is constant for $M=3H$; the free proper densities are then small everywhere and the per-configuration rule gives the large values of the last two rows (the dimensionless $\hat\lambda=\lambda m^6$ carries the factor $3^6=729$). The convergence runs reuse the values of $(m,L,N)=(1,3,112)$; the $a_{4,0}=0.5$ partner uses $\hat\lambda_1e^{1.5}$ (erratum E4.10). The thermodynamics uses two further fixed couplings (Section 10.1).

**Solver tolerances.** CVODE relative and absolute tolerances $10^{-12}$ and $10^{-14}$ with the maximum step $0.05$ (`--refined`: both divided by 10 and the step halved); self-consistency tolerance $10^{-10}$; Anderson mixing $\beta=0.4$ with a history of 6; at most 80 iterations; a loop without a factor-2 improvement in 20 iterations is stopped as stagnant; at $T>0$ the energy window keeps every level with $f>f_{\mathrm{cut}}=10^{-8}$.

### 7.2 The Rust solver: Prüfer shooting with CVODE

The crate `studies/dirac16complex_kohn_sham` solves every eigenvalue problem by shooting in $y$ from the tip to the brane on the pinned pure-Rust SUNDIALS 7.8.0 CVODE engine (`vendor/rustSolveIt`, Win11 commit `a8fdff45`); nothing is discretised into a matrix. For the block type $s=+1$ the real form of Section 5.5 is written in the Prüfer variables $a=r\cos\theta$, $b=-r\sin\theta$:

$$
\theta'=\bigl(\varepsilon-v_x(y)\bigr)+\kappa(y)k\cos2\theta-M_{\mathrm{eff}}(y)\sin2\theta,\qquad(\ln r)'=M_{\mathrm{eff}}\cos2\theta+\kappa k\sin2\theta,\qquad\theta(-L)=0,
$$

where $\theta(-L)=0$ is the tip bag $b(-L)=0$. Since $\partial\theta'/\partial\varepsilon=1>0$, the end angle $\Theta(\varepsilon)=\theta(0;\varepsilon)$ is strictly increasing (comparison theorem); the levels of the even parity are the solutions of $\Theta(\varepsilon)=n\pi$ and those of the odd parity of $\Theta(\varepsilon)=\pi/2+n\pi$, one for every integer $n$ (an oscillation theorem for the one-dimensional Dirac operator). Every level in an energy window is therefore found and none is missed, and $n$ is a continuous label of the level (the Prüfer index). The $s=-1$ levels are those of the $s=+1$ problem with $\varepsilon\to-\varepsilon$ and $v_x\to-v_x$ (Section 5.6). A level is bracketed by step doubling and located by Illinois regula falsi; CVODE integrates with the Adams method on non-stiff shells and BDF otherwise. The orbital is integrated once more as the linear system together with the accumulators $\int(a^2+b^2)$, $\int(-2ab)$ and $\int(-\kappa k(a^2-b^2))$, re-initialised whenever the amplitude leaves $[10^{-40},10^{40}]$, and normalised to $\int(a^2+b^2)\,dy=1$; its matching residual, the node count of the profile and the Prüfer index must agree (the run files record the residuals, below $3.2\times10^{-9}$ in every scf run). The potentials live on the 301-point grid as natural cubic splines and the integrals use the Simpson rule; the design order of the scheme in the grid spacing is $p=2$, because the splines are $O(h^4)$ inside but $O(h^2)$ near the ends (erratum E4.14).

**Shells and windows.** The levels are computed for $\vec k=(k,0,0)$ with $k=\Delta k\sqrt{n_2}$ on every lattice shell $n_2=n_1^2+n_2^2+n_3^2$ (multiplicity $4r_3(n_2)$ per level and block type, Section 5.6) inside an energy window that reaches down to $-(2.5m+2\pi/L)$; at $T=0$ the canonical $m=1$, $L=3$ runs use 182 shells and 786 to 792 states (576 in the smeared run of Section 9.3, whose window is narrower), the $T=m$ runs about 75000 levels. Shells are distributed over worker threads in fixed blocks and merged in shell order, so the output does not depend on the thread count.

**Determinism.** Every output is written deterministically (CSV with 17 significant digits, JSON with insertion order, LF, no absolute paths, no timings), so a repeated run is byte-identical (Section 13.2). The release build uses the repository's `.cargo/config.toml` (the `+fma` target feature); the committed outputs were produced with the Win11 engine on Windows and are reproduced byte for byte on Linux.

### 7.3 Self-consistency, occupations and the $T=0$ fallback

Each iteration computes the levels in the current potentials, fills them (Section 6.5: aufbau at $T=0$, Fermi–Dirac with $\mu$ from bisection on $N$ at $T>0$), rebuilds $n_c$, $S_c$ and from them $M_{\mathrm{eff}}$ and $v_x$, and mixes the pair $(n_c,S_c)$ by Anderson (Pulay) mixing. The loop has converged when $\max|\Delta n_c|/D<10^{-10}$ and $\max|\Delta S_c|/D<10^{-10}$ with $D=\max(\max|n_c|,\max|S_c|)$. The free levels that define the particle and sea branches are computed first and warm-start the interacting levels. At $T>0$ an interacting run starts from the free state at the same $T$.

**The $T=0$ fallback (erratum E4.8).** A degenerate level crossing at the Fermi level makes the exact $T=0$ occupations flip between iterations (charge sloshing that no mixing parameter cures), and the loop is stopped as stagnant. The ground state is then defined as the self-consistent branch connected to $\lambda=0$: the function `solve_ground` continues in the coupling ($\lambda/4$, $\lambda/2$, $3\lambda/4$, $\lambda$, each step started from the previous solution, mixing $\beta/4$, up to 200 iterations), first with exact occupations and, where they slosh, with a Fermi–Dirac occupation smearing of $10^{-3}m$ and then $10^{-2}m$; at the last step a smeared result is followed by one more exact attempt from it. The path is recorded in `run.json` (`zeroTemperatureFallbackStage`, `occupationSmearing`, `mixBeta`, `exactZeroTemperatureOccupations`). The energies use the physical $T=0$ ($F=E$); the smearing entropy is reported. Exactly one ground state of the canonical matrix needed the fallback: $N=1016$ at $-\hat\lambda_2$, converged with the smearing $10^{-3}m$ (Section 9.3); every other run converged with exact aufbau occupations.

**First excited state.** The KS gap is $\varepsilon_{\mathrm{LUMO}}-\varepsilon_{\mathrm{HOMO}}$. The particle-hole list pairs every hole with every particle level of a $T=0$ run, where a hole has $f>10^{-12}$ and a particle $f<1-10^{-12}$ (erratum E4.9; at $T>0$ holes have $f\ge\tfrac12$ and particles $f<\tfrac12$). The $\Delta$SCF state keeps the occupations fixed by level identity (shell, parity, block type, Prüfer index) with one particle moved from the HOMO group to the LUMO group, spread equally over each group, and is converged self-consistently; $\Delta\mathrm{SCF}=E_1-E_0$.

### 7.4 The independent reference solver

`scripts/ks_reference_solver.py` (numpy only) solves the same Kohn–Sham problems by a different method and shares nothing with the Rust code except the algebra fixture and the conventions. It derives its own block reduction from the fixture and discretises the Hermitian block operator on a staggered (Yee) grid: one component on the nodes $y_j=-L+jh$, the other on the half nodes, $h=L/N$. With the second component multiplied by $i$ the matrix is real symmetric; the generalised problem with the quadrature weights is diagonalised densely by LAPACK. The free dispersion of the scheme, $\varepsilon(p)=\pm\sqrt{M^2+(2/h)^2\sin^2(ph/2)}$, is monotonic on the Brillouin zone, so there is no fermion doubler and no Wilson term. Every quantity is computed on three grids $N_0$, $2N_0$, $4N_0$ and extrapolated by eliminating $h^2$ and $h^3$; $N_0=60$, so that every coarse node is a node of the Rust grid, except $N_0=120$ for $m=3$ and for the smeared run `m1_L3_N1016_lamm2_T0` (erratum E4.13). Up to 300 shells are diagonalised exactly and the rest of a window by Chebyshev interpolation in $|k|$ (32 nodes, with the error recorded); the $T=m$ runs diagonalise every shell exactly. It has its own Anderson-mixed self-consistency, its own $T=0$ fallback (smearing $10^{-4}m$, then $10^{-3}m$), its own particle/sea assignment (by rank against the free spectrum) and its own couplings (the same rule, evaluated on its own free states). Its canonical set is the Rust matrix label by label plus six single-parity runs of the $L$ series, 56 runs in `reference/reference-summary.json` (which declares itself complete).

### 7.5 The Mathematica and Jupyter notebooks

The Mathematica notebook `notebooks/Dirac16ComplexKohnSham.nb` is generated by `scripts/build_dirac16complex_ks_mathematica_notebook.wls` and evaluated headless by `scripts/verify_dirac16complex_ks_mathematica_notebook.wls` (Wolfram 15.0). It re-derives the geometry, the reduced equation, the block diagonalisation, the real two-component form and the Prüfer form symbolically, solves the $k=0$, $\lambda=0$ problem exactly, shoots the free spectra with `NDSolve` and compares them level by level with the Rust files, and runs its own self-consistent loop in Wolfram Language on the discrete problem of the Rust code for $N=8$ at $+\hat\lambda_2$ (Section 13.3). The Jupyter notebook `notebooks/dirac16complex_kohn_sham.ipynb` (builder `notebooks/build_dirac16complex_kohn_sham_notebook.py`, runner `notebooks/run_notebook.py`, auditor `notebooks/check_dirac16complex_kohn_sham_notebook.py`) re-runs the Rust `print-config` and `spectrum` subcommands, reads every committed output, recomputes key quantities independently, compares the Rust and reference trees with the cross-checker's own comparison function, draws the 14 figures of this document and ends with a gauntlet of 60 checks.

### 7.6 The run matrix

```text
subcommand  runs  content
spectrum      -   reduction, geometry, exchange checks, free spectra m = 1, 3 at
                  L = 2, 3, 4, closed shells, theory agreement (15 files)
scf          33   m = 1, L = 3: N = 8, 112, 1016 x {0, +-lh1, +-lh2} (15 runs);
                  L = 2, 4: N = 8, 112 x {0, +lh1} (8); m = 3, L = 3: N = 8, 112
                  x {0, +-lh1} (6); a4_0 = 0.5 and its rescaled partner (2);
                  601-point grid (1); Delta k = 0.125 m, N = 896 (1)
excited      16   KS gap, particle-hole list, Delta-SCF for the 15 runs of
                  m = 1, L = 3, plus the 601-point run of N = 1016, -lh2
thermo       22   T/m = 0, 0.1, 0.3, 1 for N = 8, 112: series lam0 (8 runs), lamp1
                  (6; T = m not run, Section 10.1) and lamh (8)
emt          10   N = 8, 112, 1016 x {0, +-lh1} at T = 0, and N = 112, +lh1 at
                  T = 0.3 m
```

The Rust subcommands record 33, 137, 65, 102 and 60 self-checks (397 in all); the solver statistics are in each `summary.json` (for example $4.81\times10^9$ CVODE steps for `scf` and $3.77\times10^{10}$ for `thermo`).

## 8. Results: the ground state

### 8.1 The non-interacting spectrum and the closed shells

Without interaction ($\lambda=0$, $M_{\mathrm{eff}}=m$, $v_x=0$) the spectrum is that of Sections 5.6 and 5.7. For $m=H=1$ and $L=3$ the $k=0$ levels are the eight zero modes at $\varepsilon=0$ and the massive levels at $\pm1.2922928$, $\pm2.0106286$, $\pm2.9119359$ (odd brane parity, roots of $\tan pL=-p/M$) and $\pm1.4479719$, $\pm2.3208815$ (even brane parity, $\sqrt{M^2+(n\pi/L)^2}$ for $n=1,2$), each 8-fold (`rust/spectrum/free-spectrum-m1-L3.csv`). For $k\neq0$ the zero modes become the brane band, $\varepsilon=+ck+O(k^2)$ in the block type $j=+1$ (program label $s=-1$) and $-ck$ in $j=-1$, with $c=1.9051482536$. Its first shell, $k=\Delta k=0.25m$ ($n_2=1$, $r_3=6$, 24 states), lies at $\varepsilon=0.4307337$, below the linear value $c\Delta k=0.476$ (derived) because of the $O(k^2)$ term.

The aufbau fills the particle states in this order. The first ten shells after the zero modes are all brane-band levels ($n_2=1,\dots,6,8,\dots,11$; the shell $n_2=7$ does not exist, since $7$ is not a sum of three squares), which closes the shells $N=32$, 80, 112, 136, 232, 328, 376, 496, 592 and 688. The shell $N=696$ adds the first bulk level, the $k=0$ odd-parity level at $1.2922928$ (8 states), and the band shells $n_2=12$, 13 and 14 ($k=0.866$, $0.901$, $0.935$; 32, 96 and 192 states) close $N=728$, 824 and 1016. The next particle levels are the $k=\Delta k$ odd-parity level at $1.4389268$ (24 states, $N=1040$) and the $k=0$ even-parity level at $1.4479719$ (8 states, $N=1048$). So the ground state of $N=8$ consists of the zero modes, that of $N=112$ of the zero modes and three band shells, and that of $N=1016$ of the zero modes, ten band shells, one $k=0$ bulk level and three more band shells. The scalar charge $\int(-2sab)\,dy$ of a free level is $0$ for the zero modes, between $-0.18$ and $-0.25$ for the band levels and between $+0.69$ and $+0.86$ for the bulk levels listed above (column `scalar_charge` of the same file).

![The Kohn–Sham spectrum $\varepsilon_n(k)$ for $|\varepsilon|<3m$, $m=1$, $L=3$, per brane parity (rows) and block type (circles $s=+1$, triangles $s=-1$; the two types are offset by $\pm0.006$ in $k$ for visibility). Left: the free spectrum on the shells $n_2\le16$ with the closed-form band $\pm ck$ near $k=0$ (dashed). Right: the self-consistent spectrum of $N=112$ at $+\hat\lambda_2$ on all shells, with the chemical potential (dotted).](artifacts/dirac16complex/kohn-sham/figures/ks_spectrum.png)

### 8.2 Ground-state energies, chemical potentials and Kohn–Sham gaps

The self-consistent ground states for $m=H=1$, $L=3$ (`rust/scf/summary.json`; energies, $\mu$ and gaps in units of $m$; `brane` is the fraction of the particles within $1/H$ of the brane, Section 8.3; `it` the number of iterations; `lh1`, `lh2` stand for $\hat\lambda_1$, $\hat\lambda_2$):

```text
    N  coupling         E_0           mu       KS gap   max|lS|/m  max|vx|/m  it   brane
    8  0            0.000000    0.0000000    0.4307337    0.0000     0.0000    3  0.8668
    8  +lh1        -0.000987   -0.0002456    0.4309439    0.0165     0.0988   10  0.8668
    8  -lh1         0.000987    0.0002456    0.4305159    0.0165     0.0988   10  0.8668
    8  +lh2        -0.007830   -0.0016858    0.4318987    0.6468     0.5913   19  0.8679
    8  -lh2         0.007830    0.0016858    0.4291374    0.6468     0.5913   19  0.8679
  112  0           61.090723    0.7040996    0.0955462    0.0000     0.0000    3  0.9237
  112  +lh1        61.113212    0.7044757    0.0954841    0.0592     0.1115   11  0.9234
  112  -lh1        61.068610    0.7037362    0.0956051    0.0583     0.0882   11  0.9240
  112  +lh2        61.328311    0.7083837    0.0948132    1.3585     0.8927   20  0.9202
  112  -lh2        60.891305    0.7009659    0.0960102    0.4522     0.3488   13  0.9264
 1016  0         1127.136625    1.3859192    0.0530077    0.0000     0.0000    3  0.9615
 1016  +lh1      1127.160980    1.3859343    0.0532575    0.1004     0.0347   10  0.9616
 1016  -lh1      1127.111039    1.3859040    0.0527200    0.1136     0.0420   10  0.9615
 1016  +lh2      1127.342203    1.3860704    0.0544240    0.6650     0.1962   10  0.9617
 1016  -lh2      1126.858093    1.3895672    0.0412551    1.3718     1.5000   44  0.9577
```

All 33 scf runs converged, 32 with exact aufbau occupations; the one exception is $N=1016$ at $-\hat\lambda_2$ (Section 9.3), whose $\varepsilon_{\mathrm{HOMO}}=1.3894608$ lies below $\mu=1.3895672$ because its HOMO level is fractionally occupied. In every other $T=0$ run $\mu=\varepsilon_{\mathrm{HOMO}}$. Without interaction the energies are $E_0=0$, $61.090723$ and $1127.136625$ and the KS gaps $0.4307337$, $0.0955462$ and $0.0530077$ for $N=8$, 112 and 1016. The gap shrinks with $N$ because the band shells crowd together at larger $k$ (figure in Section 9.1).

### 8.3 Profiles and brane localisation

The particles sit at the brane. The fraction of $N$ within $1/H$ of the brane, $\int_{-1/H}^0n_c\,dy\,\ell^3/N$, is $0.8668$ for $N=8$, $0.9237$ for $N=112$ and $0.9615$ for $N=1016$ without interaction, and it changes by less than $0.004$ with the coupling (table of Section 8.2); for $m=3$ it is $0.9975$ to $0.9993$ (Section 8.5). For $N=8$ the free state consists of the zero modes $\chi=(e^{My},0)$, whose fraction is exactly $(1-e^{-2M/H})/(1-e^{-2ML})$ (derived), $0.86681$ for $M=H=1$ and $L=3$, as measured. The fraction within $1/H$ of the tip cutoff is $0.016$, $0.0021$ and $0.0023$ for $N=8$, 112 and 1016 at $\lambda=0$ (`run.json`: `tipFraction_within_1_over_H_of_cutoff`).

The proper densities behave in the opposite way. A zero mode has the coordinate density $e^{2My}$ and the proper density $e^{(2M-6H)y}$, which grows toward the tip for $M<3H$; the proper densities $n_p$ and $|S_p|$ of every state are therefore largest at $y=-L$, and so is the pseudo-potential (Section 6.4). For $N=112$ at $+\hat\lambda_2$ the self-consistent $\max|\lambda S_p|/m$ is $1.3585$ and $\max|v_x|/m$ is $0.8927$; for $N=1016$ at $-\hat\lambda_2$ they are $1.3718$ and $1.5000$; near the brane both potentials are small (figure below). The scalar density is negative near the brane, where the band levels dominate, and positive near the tip for $N=1016$, where the $k=0$ bulk level contributes.

![Self-consistent ground states, $m=1$, $L=3$ (solid: $\lambda=0$; dashed: $+\hat\lambda_2$; dotted: $-\hat\lambda_2$). Top: the coordinate density $n_c$ (particles per unit $y$ and coordinate 3-volume), the proper density $n_p$ and the proper scalar density $S_p$ (symmetric logarithmic scale) for $N=8$, 112 and 1016. Bottom: the pseudo-potential pair $M_{\mathrm{eff}}-m=\tfrac{15}{16}\lambda S_p$ and $v_x=-\lambda n_p/16$ at $\pm\hat\lambda_2$, and the HOMO orbital $a^2+b^2$ against $z=6Hx_0$ (the brane is at $z=\pi/2$).](artifacts/dirac16complex/kohn-sham/figures/density_profiles.png)

![Brane localisation. Left: the fraction of the particles within the distance $d$ of the brane for $N=8$, 112 and 1016 at $m=1$ and for $N=112$ at $m=3$ ($\lambda=0$, $L=3$). Right: the fraction within $1/H$ against the coupling.](artifacts/dirac16complex/kohn-sham/figures/brane_localisation.png)

### 8.4 Attractive and repulsive coupling

The interaction changes the ground-state energy at the level of $10^{-3}$ to $10^{-4}$ of $E_0$ for $N\ge112$ (derived from the table: $E_0(\pm\hat\lambda_1)-E_0(0)=+0.022489$ and $-0.022113$ for $N=112$, $+0.024355$ and $-0.025586$ for $N=1016$; at $\pm\hat\lambda_2$: $+0.237588$ and $-0.199418$ for $N=112$, $+0.205578$ and $-0.278532$ for $N=1016$). The first-order (Hellmann–Feynman) slope at $\lambda=0$ is $dE_0/d\lambda=(E_H+E_x)/\lambda=\int\bigl(\tfrac{15}{32}S_p^2-\tfrac1{32}n_p^2\bigr)dV_7$ on the free state (derived from Section 6.5), so its sign is set by the competition between the scalar part, dominated by the Hartree term, and the vector exchange. Evaluated with the Simpson rule on the free `profiles.csv` (derived) it is $dE_0/d\hat\lambda=-0.1019$, $+2.3321$ and $+158.22$ for $N=8$, 112 and 1016 at $m=1$. The self-consistent shifts at $\pm\hat\lambda_1$ agree with this slope to between 0.5 % and 2.6 %, those at $\pm\hat\lambda_2$ to between 6 % and 21 % (derived; figure below).

![Ground-state energy, $m=1$, $L=3$. Left: $E_0$ of the free closed shells against $N$ with the self-consistent values at $\pm\hat\lambda_2$. Right: the interaction energy $E_0(\lambda)-E_0(0)$ against $\hat\lambda/\hat\lambda_1$ for $N=8$, 112 and 1016, self-consistent (solid) and first order in $\lambda$ (dashed).](artifacts/dirac16complex/kohn-sham/figures/ground_state_energy.png)

- **$N=8$.** The free scalar density vanishes, so the vector exchange dominates: a repulsive $\lambda>0$ lowers the energy ($E_0=-0.000987$ at $+\hat\lambda_1$). The energies are exactly antisymmetric in $\lambda$, $E_0(-\hat\lambda)=-E_0(\hat\lambda)$ to every printed digit. Derived explanation: with $M_{\mathrm{eff}}$ fixed, $v_x\to-v_x$ and the block type exchanged, $h_{-j}(M,-v)=-h_j(M,v)$ (Section 5.6), so the map $(\lambda,v_x,S_p)\to(-\lambda,-v_x,-S_p)$ with the same orbitals negates every level and maps a self-consistent state onto one; for $N=8$ it maps the eight occupied zero modes onto themselves, and $E=\sum f\varepsilon-E_H-E_x$ changes sign term by term.
- **$N=112$ and $N=1016$.** The scalar part dominates: repulsion raises and attraction lowers the energy, and the Fermi level follows ($\mu$ rises from $0.7040996$ to $0.7083837$ at $+\hat\lambda_2$ for $N=112$). The attractive $-\hat\lambda_2$ at $N=1016$ pulls the $k=0$ even-parity bulk level down to the Fermi level (Section 9.3).

### 8.5 The mass $m/H$

For $m=3H$ the energies in the files are in units of $H=m/3$. The first band shell lies at $0.8958328\,H$ ($k=\Delta k=0.75H$), consistent with the slope $c(M=3H,L=3)=\tfrac65(1-e^{-15})/(1-e^{-18})\approx1.2$ (derived), and the particles are almost entirely at the brane (fractions $0.9975$ to $0.9993$). Without interaction $E_0(N=112)=131.448295\,H$ with the KS gap $0.2342638\,H$. For $M=3H$ the zero mode has a constant proper density, so for $N=8$ the exchange potential is a constant shift: the self-consistent $N=8$ states at $\pm\hat\lambda_1$ have $\varepsilon_{\mathrm{HOMO}}=\mu=\mp0.3H$ (that is $v_x=\mp0.1m$, the first-order design value) and $E_0=\mp1.2H=Nv_x/2$, with an unchanged gap (derived: $E=\sum f\varepsilon-E_x$ with $E_x=\tfrac12\int v_xn_p\,dV_7=Nv_x/2$ for a constant $v_x$ and $S_p=0$). The other $m$- and $L$-variants and the convergence runs ($E_0$, $\mu$ and gaps in units of $H$):

```text
run                          E_0         mu     KS gap max|lS|/m max|vx|/m   brane
L = 2, N = 8, 0              0.000000  0.0000000  0.4243017   0.0000    0.0000  0.8808
L = 2, N = 8, +lh1          -0.007294 -0.0018154  0.4248395   0.0161    0.0989  0.8810
L = 4, N = 8, 0              0.000000  0.0000000  0.4307456   0.0000    0.0000  0.8650
L = 4, N = 8, +lh1          -0.000134 -0.0000332  0.4307783   0.0165    0.0988  0.8650
L = 2, N = 112, 0           60.725616  0.7023656  0.0962973   0.0000    0.0000  0.9243
L = 2, N = 112, +lh1        60.786393  0.7036066  0.0961777   0.1131    0.0364  0.9231
L = 4, N = 112, 0           61.091032  0.7040996  0.0955462   0.0000    0.0000  0.9236
L = 4, N = 112, +lh1        61.091334  0.7041065  0.0955450   0.0166    0.0991  0.9236
m = 3, N = 8, 0              0.000000  0.0000000  0.8958328   0.0000    0.0000  0.9975
m = 3, N = 8, +lh1          -1.200000 -0.3000000  0.8958328   0.0000    0.1000  0.9975
m = 3, N = 8, -lh1           1.200000  0.3000000  0.8958328   0.0000    0.1000  0.9975
m = 3, N = 112, 0          131.448295  1.5420110  0.2342638   0.0000    0.0000  0.9990
m = 3, N = 112, +lh1       127.409027  1.4739375  0.2350337   0.1694    0.0280  0.9983
m = 3, N = 112, -lh1       135.701558  1.6170194  0.2336533   0.0819    0.0292  0.9993
a4_0 = 0.5, N = 112, +lh1   39.008843  0.4514218  0.0620127   0.3874    0.2298  0.8994
partner, Delta k e^-0.5     39.008843  0.4514218  0.0620127   0.3874    0.2298  0.8994
601 points, N = 112, +lh1   61.113212  0.7044757  0.0954841   0.0592    0.1115  0.9234
Delta k = m/8, N = 896     521.396546  0.7542028  0.0000000   0.1044    0.0277  0.9268
```

### 8.6 Convergence: the tip cutoff, the grid, the torus and the rescaling identity

**Tip cutoff $L$.** The couplings are set per configuration, so only the $\lambda=0$ runs compare like with like. For $N=8$ the KS gap is $0.4243017$, $0.4307337$ and $0.4307456$ at $L=2$, 3 and 4, and for $N=112$ the energy is $60.725616$, $61.090723$ and $61.091032$ with the gaps $0.0962973$, $0.0955462$ and $0.0955462$; from $L=3$ to $L=4$ the $N=112$ energy changes by $3.1\times10^{-4}$ and its gap by $2.9\times10^{-8}$ (derived). The density profiles of $L=2$, 3 and 4 coincide near the brane (figure). The tip is a genuine singular end of the transverse geometry (Section 4.4); the proper densities near $y=-L$ grow with $L$, which is why the per-configuration couplings fall from $\hat\lambda_1=0.5228$ at $L=2$ to $9.73\times10^{-3}$ at $L=3$ and $1.79\times10^{-4}$ at $L=4$ for $N=8$.

![Tip-cutoff convergence, $L=2$, 3, 4: the KS gaps of $N=8$ and $N=112$ at $\lambda=0$ and $+\hat\lambda_1$ (left), $|E_0(L)-E_0(L=4)|$ (middle) and the coordinate density $n_c(y)$ of $N=112$ at $+\hat\lambda_1$ (right). The couplings $\hat\lambda_1$ differ between the cutoffs (Section 7.1).](artifacts/dirac16complex/kohn-sham/figures/convergence.png)

**Grid.** The 601-point run of $N=112$ at $+\hat\lambda_1$ changes $E_0$ by $2.8\times10^{-9}$, $\mu$ by $9.7\times10^{-12}$ and the gap by $3.8\times10^{-13}$ (derived from the two runs); the hardest case, the smeared $N=1016$ run at $-\hat\lambda_2$, changes $E_0$ by $4.0\times10^{-6}$ and the $\Delta$SCF energy by $9.4\times10^{-7}$ (Section 9.3). The cross-checker turns these differences into per-level grid uncertainties (erratum E4.14, Section 13.4).

**Torus.** The run with $\Delta k=0.125m$ and $N=896$ ($8\times112$, the same particle density as $N=112$ on a torus of eight times the volume, $+\hat\lambda_1$ of $N=112$) is an open shell of the aufbau: 80 of the 192 states at $k=0.4677$ are occupied, equally ($f=0.416667$), so its KS gap is zero by definition (erratum E4.11). Its energy per particle, $0.581916$, differs from that of $N=112$, $0.545654$, by 6.6 % (derived): the shell spacing of the finite torus is not negligible at these particle numbers.

**The $a_{4,0}$ rescaling.** The run with $a_{4,0}=0.5$ and its partner with $a_{4,0}=0$, $\Delta k\,e^{-0.5}$, $\ell\,e^{0.5}$ and $\hat\lambda_1e^{1.5}$ (Section 5.10) have the same 2098 levels to $1.6\times10^{-10}$ and the same energy $39.008843$ to $1.8\times10^{-11}$ (derived; Rust check `a4_rescaling_pair_exact`).

**Tolerances and self-consistency.** The `--refined` Rust run (tolerances divided by 10, maximum step halved) is reported in Section 13.2. The self-consistent loops reach the tolerance $10^{-10}$ in 3 iterations at $\lambda=0$ and for $m=3$, $N=8$ (where the potential is a constant shift), in 10 to 20 iterations otherwise, and in 44 for the smeared run.

![Self-consistent convergence: the density residual $\max|\Delta n_c|/D$ per iteration at $+\hat\lambda_2$ (left) and $-\hat\lambda_2$ (right) for $N=8$, 112 and 1016; the $N=1016$, $-\hat\lambda_2$ loop is the coupling continuation with occupation smearing of Section 9.3.](artifacts/dirac16complex/kohn-sham/figures/scf_history.png)

## 9. Results: the first excited state

### 9.1 Kohn–Sham gap, $\Delta$SCF and particle-hole excitations

The first excited state is computed three ways (Section 7.3): the KS gap $\varepsilon_{\mathrm{LUMO}}-\varepsilon_{\mathrm{HOMO}}$, the particle-hole list, and the self-consistent $\Delta$SCF state with one particle promoted. For $m=H=1$, $L=3$ (`rust/excited/summary.json` and `excitations.csv`; `difference` is $\Delta\mathrm{SCF}$ minus the KS gap, derived; `lowest p-h` the lowest entry of the particle-hole list; the last row is the 601-point run):

```text
    N  coupling      KS gap     Delta-SCF    difference           E_1   lowest p-h
    8  0           0.4307337   0.4307337       0.0e+00      0.430734    0.4307337
    8  +lh1        0.4309439   0.4309381      -5.8e-06      0.429951    0.4309439
    8  -lh1        0.4305159   0.4305234       7.5e-06      0.431510    0.4305159
    8  +lh2        0.4318987   0.4319459       4.7e-05      0.424115    0.4318987
    8  -lh2        0.4291374   0.4291607       2.3e-05      0.436991    0.4291374
  112  0           0.0955462   0.0955462       2.2e-16     61.186269    0.0955462
  112  +lh1        0.0954841   0.0954842       5.8e-08     61.208696    0.0954841
  112  -lh1        0.0956051   0.0956051      -5.2e-08     61.164216    0.0956051
  112  +lh2        0.0948132   0.0948140       8.4e-07     61.423125    0.0948132
  112  -lh2        0.0960102   0.0960098      -3.3e-07     60.987315    0.0960102
 1016  0           0.0530077   0.0530077      -3.7e-10   1127.189632    0.0530077
 1016  +lh1        0.0532575   0.0532689       1.1e-05   1127.214249    0.0532575
 1016  -lh1        0.0527200   0.0527082      -1.2e-05   1127.163747    0.0527200
 1016  +lh2        0.0544240   0.0545261       1.0e-04   1127.396729    0.0544240
 1016  -lh2        0.0412551   0.0436184       2.4e-03   1126.901711      6.6e-12
 1016  -lh2 601    0.0412551   0.0436194       2.4e-03   1126.901708      1.7e-12
```

**What the excitation is.** Without interaction the first excitation moves one particle from the HOMO shell to the next level of the torus. For $N=8$ that is a zero mode promoted to the first band shell ($0.4307337$); for $N=112$ a particle from the band shell $k=0.433$ ($n_2=3$) to $k=0.5$ ($n_2=4$, $0.0955462$); for $N=1016$ a particle from the band shell $k=0.935$ ($n_2=14$) to the odd-parity bulk level at $k=\Delta k$ ($1.4389268$; gap $0.0530077$). The first excited state is therefore a particle-hole excitation across the shell gap of the finite torus: its energy is set by the spacing of the lattice shells, which is proportional to $\Delta k$, and by the slope of the band.

**The effect of the interaction.** At $\lambda=0$ the $\Delta$SCF energy equals the KS gap (exactly for $N=8$ and 112, to $3.7\times10^{-10}$ for $N=1016$, the precision of the eigenvalues). With interaction the orbital relaxation $\Delta\mathrm{SCF}-\mathrm{gap}$ is small: at most $8.4\times10^{-7}$ for $N=112$, $4.7\times10^{-5}$ for $N=8$ and $1.0\times10^{-4}$ for $N=1016$, except at $N=1016$, $-\hat\lambda_2$ ($2.4\times10^{-3}$, Section 9.3). Its sign differs between the cases. The gaps themselves change by up to 0.4 % ($N=8$), 0.8 % ($N=112$) and 2.7 % ($N=1016$, $+\hat\lambda_2$) at $\pm\hat\lambda_2$ (derived), again except the level-crossing case. In every run except that case the lowest particle-hole excitation is the KS gap.

![First excited states, $m=1$, $L=3$. Left: the KS gap (filled) and the $\Delta$SCF energy (open) against $\hat\lambda/\hat\lambda_1\in\{-10,-1,0,1,10\}$ for $N=8$, 112 and 1016; the smeared ensemble of Section 9.3 is marked. Middle: the same against $N$. Right: the orbital relaxation $\Delta\mathrm{SCF}-\mathrm{gap}$ (zero at $\lambda=0$).](artifacts/dirac16complex/kohn-sham/figures/ks_gap_delta_scf.png)

### 9.2 The $\Delta$SCF state

The $\Delta$SCF state keeps the occupations of the ground state, identified by the level key (shell, parity, block type, Prüfer index), moves one particle from the HOMO group to the LUMO group, spreads it equally over each degenerate group and converges the densities self-consistently with these fixed occupations; the energy is $E_1$ and $\Delta\mathrm{SCF}=E_1-E_0$. The key identification keeps the excited configuration well defined while the levels move. Every $\Delta$SCF loop converged (checks `*_delta_scf_converged`), and every $\Delta$SCF energy is positive (`*_delta_scf_positive`). For a smeared ground state the constrained occupations are the Fermi–Dirac occupations of that ground state with one particle moved; both solvers build them from the ground state of their own grid (erratum E4.14).

### 9.3 $N=1016$ at $-\hat\lambda_2$: a level crossing at the Fermi level

This is the one case that needs care (erratum E4.8). In the free $N=1016$ state the HOMO is the 192-fold band shell at $k=0.935$ ($\varepsilon=1.3859192$), and the $k=0$ even-parity bulk level ($1.4479719$, 8 states) lies $0.062$ above it. The bulk level has a large positive scalar charge ($+0.69$, against $-0.25$ for the band shell), so the attractive coupling $-\hat\lambda_2$, whose mass shift $\tfrac{15}{16}\lambda S_p$ is negative where $S_p>0$, pulls it down by about $0.06$, while the band shell moves by only $1.5\times10^{-4}$. Under self-consistency the two levels meet at the Fermi level: whichever of them is filled last, the self-consistent potential moves the other one below it. The exact $T=0$ aufbau then flips the occupations between iterations and the loop stagnates; no mixing parameter cures this.

The ground state is defined by the continuation of Section 7.3. The branch connected to $\lambda=0$ converges, after the exact-occupation attempts had sloshed, with the Fermi–Dirac occupation smearing $10^{-3}m$ at the physical $T=0$ (`run.json`: `occupationSmearing` $0.001$, `zeroTemperatureFallbackStage` 1, `exactZeroTemperatureOccupations` false; $F=E$), in 44 iterations. Its levels at the Fermi level (`rust/excited/m1_L3_N1016_lamm2_T0/levels.csv`):

```text
level                              eps [m]        states   occupation f
band, k = 0.935 (n2 = 14)          1.3857700         192   0.978059
bulk, k = 0, even parity           1.3894608           8   0.526580
bulk, k = 0.25, odd parity         1.4307159          24   1.3e-18
```

The aufbau count closes exactly at the band ($8+\dots+192=1016$ states up to and including the band), but the smeared ensemble moves $192\times(1-0.978059)=4.21$ particles from the band into the $k=0$ level, which then holds $8\times0.526580=4.21$ particles (derived). This is not an open shell of the aufbau: it is the self-consistent ensemble of a degenerate crossing. Its quantities refer to this ensemble:

- the KS gap $0.0412551$, from the fractionally occupied $k=0$ level to the next level at $1.4307159$;
- the particle-hole list, which starts inside the fractionally occupied levels: first a zero-energy rearrangement between the two halves of the exactly degenerate $k=0$ level (the two block types; numerically split by $6.6\times10^{-12}$ in Rust and $2.8\times10^{-14}$ in the reference), then $3.69080\times10^{-3}$ from the band into the $k=0$ level, then the KS gap (holes have $f>10^{-12}$ and particles $f<1-10^{-12}$, erratum E4.9; the Fermi–Dirac tails of the smearing are excluded);
- the $\Delta$SCF energy $0.0436184$ on 301 grid points and $0.0436194$ on 601 points, with $E_0=1126.858093$ and $1126.858089$.

The ensemble is reproducible but not unique in principle. An exploratory reference run on twice finer grids, which converged the exact aufbau from its own start, found a state about $1.01m$ higher (`handoff/reviews/stage4_refgrid_N0120_exploratory.log`, erratum E4.8); the continuation from $\lambda=0$ is the definition used here. The reference solver, run on the grids $N_0=120$, 240, 480 with the smearing $10^{-3}m$ given directly (erratum E4.13), converges to the same ensemble; its numbers are compared in Section 13.4.

![The level crossing at the Fermi level: the particle levels near the Fermi level (marker area proportional to the number of states, colour the occupation). Left: the free $N=1016$ state with exact aufbau occupations. Right: the self-consistent smeared ensemble at $-\hat\lambda_2$, with $\mu$ (dashed), the 192-fold band at $f=0.978$ and the 8-fold $k=0$ level at $f=0.527$.](artifacts/dirac16complex/kohn-sham/figures/fermi_level_N1016_lamm2.png)

## 10. Results: finite temperature

### 10.1 The temperature series and their couplings

The Mermin states are computed for $T/m\in\{0,0.1,0.3,1\}$, $m=1$, $L=3$, $N=8$ and 112, in three series of fixed coupling, so that $F(T)$, $S_{\mathrm{ent}}(T)$ and $C_V(T)$ of one series belong to one Hamiltonian (`rust/thermo/summary.json`, `seriesRule`):

- `lam0`: $\lambda=0$;
- `lamp1`: the $T=0$ coupling $\hat\lambda_1$ of the configuration. A point is run only when its first-order pseudo-potential $\hat\lambda_1\cdot\mathrm{strength}_{\mathrm{free}}(T)$ is at most $1m$, the upper edge of the window of the specification. At $T=m$ the thermal pair plasma multiplies the free $\max|S_p|$ to $4504$ ($N=8$), so the first-order pseudo-potential would be $41.09m$ ($N=8$) and $40.41m$ ($N=112$); these two points are not run, and the skipped runs and their estimates are listed in `skippedRuns`;
- `lamh`: the hot-calibrated coupling $\hat\lambda_{\mathrm{hot}}=0.1/\mathrm{strength}_{\mathrm{free}}(T=m)$, $2.3680199\times10^{-5}$ ($N=8$) and $2.3679222\times10^{-5}$ ($N=112$), which keeps the whole series inside the window at first order.

At $T>0$ the net number $N=\sum\mathrm{mult}\cdot w$ is fixed, and the thermal particles and antiparticles (holes of the sea) are part of the state. An interacting point at $T>0$ starts from the free state at the same $T$. At $T=m$ the window keeps about 75000 levels.

### 10.2 Energy, free energy, entropy and heat capacity

From `rust/thermo/thermodynamics.csv` (energies in units of $m$; `levels` is the number of levels in the window; $C_V$ is the self-consistent central difference $dE/dT|_N$ with $\delta=0.05T$ for $T\le0.3m$ and the fixed-spectrum derivative $C_V^{(0)}=\sum\mathrm{mult}\,(df/dT)|_N\langle h_0\rangle$ at $T=m$):

```text
   N series T/m         mu             E             F      S_ent        C_V levels
   8 lam0     0  0.0000000      0.000000      0.000000     0.0000 0.0000e+00    788
   8 lam0   0.1  0.1304195      1.031867     -0.393979    14.2585 3.3618e+01    606
   8 lam0   0.3  0.0132868    108.734599    -30.511503   464.1537 1.7541e+03   2445
   8 lam0     1  0.0003756  46811.736659 -11447.695463 58259.4321 2.3833e+05  74945
   8 lamp1    0 -0.0002456     -0.000987     -0.000987     0.0000 0.0000e+00    788
   8 lamp1  0.1  0.1303310      1.030518     -0.394615    14.2513 3.3620e+01    618
   8 lamp1  0.3  0.0132713    108.682302    -30.503671   463.9532 1.7526e+03   2442
   8 lamh     0 -0.0000006     -0.000002     -0.000002     0.0000 0.0000e+00    788
   8 lamh   0.1  0.1304192      1.031864     -0.393980    14.2584 3.3618e+01    618
   8 lamh   0.3  0.0132871    108.734530    -30.511486   464.1534 1.7541e+03   2443
   8 lamh     1  0.0003756  46810.542709 -11447.481378 58258.0241 2.3832e+05  74947
 112 lam0     0  0.7040996     61.090723     61.090723     0.0000 0.0000e+00    788
 112 lam0   0.1  0.6973343     69.509378     53.971643   155.3773 1.5775e+02    689
 112 lam0   0.3  0.3169320    167.712442    -12.419875   600.4411 1.4657e+03   2540
 112 lam0     1  0.0101406  46813.933096 -11447.146034 58261.0791 2.3832e+05  75007
 112 lamp1    0  0.7044757     61.113212     61.113212     0.0000 0.0000e+00    789
 112 lamp1  0.1  0.6976130     69.537986     53.988581   155.4940 1.5787e+02    689
 112 lamp1  0.3  0.3169925    167.661096    -12.410339   600.2381 1.4642e+03   2466
 112 lamh     0  0.7041005     61.090779     61.090779     0.0000 0.0000e+00    788
 112 lamh   0.1  0.6973350     69.509447     53.971685   155.3776 1.5775e+02    688
 112 lamh   0.3  0.3169331    167.713178    -12.419884   600.4435 1.4657e+03   2467
 112 lamh     1  0.0101425  46812.783610 -11446.934440 58259.7181 2.3831e+05  74944
```

- **Monotonicity and signs.** In every series $F$ decreases with $T$, $S_{\mathrm{ent}}\ge0$ and $C_V\ge0$ (Rust checks `*_free_energy_decreases`, `*_entropy_positive`, `*_heat_capacity_positive`).
- **Low temperature.** At $T=0.1m$ the $N=8$ state excites particles from the zero modes into the first band shell; its chemical potential, $0.1304$, lies inside the gap of $0.43$. For $N=112$ at $T=0.1m$, $\mu=0.6973$ lies just below the free HOMO $0.7041$, so the HOMO shell is less than half occupied.
- **The hot plasma.** At $T=m$ the state is a thermal particle-antiparticle plasma: $E=46811.7$ and $46813.9$, $S_{\mathrm{ent}}=58259.4$ and $58261.1$ for $N=8$ and 112, almost independent of the net particle number, with $\mu\approx0$ ($3.8\times10^{-4}$ and $1.0\times10^{-2}$). The equation-of-state ratios of the plasma approach $w_y=0.2539$ and $w_3=0.2445$ (column `w_y`, `w_3`), close to the value $1/4$ of an isotropic ultrarelativistic gas in four spatial dimensions (a comparison, not a fit).
- **Heat capacity.** The three estimates agree where they are defined. At $\lambda=0$ the two fixed-spectrum forms $C_V^{(0)}$ and $C_V^{(S)}=T\,dS/dT$ coincide and the central difference agrees with them to $O(\delta^2)$: $33.618$ against $33.500$ ($N=8$, $T=0.1m$), $1754.07$ against $1745.07$ ($N=8$, $T=0.3m$), $157.752$ against $157.739$ and $1465.74$ against $1454.70$ ($N=112$; columns `C_V_fd`, `C_V_fixed_spectrum`, `C_V_fixed_spectrum_entropy`).
- **Interaction.** With $\hat\lambda_1$ the energies at $0<T\le0.3m$ change by $3\times10^{-4}$ to $1.3\times10^{-3}$ of $E$, and with $\hat\lambda_{\mathrm{hot}}$ by at most $2.6\times10^{-5}$ (derived from the table).
- **The KS gap at $T>0$** is defined between the highest particle level with $f\ge\tfrac12$ and the lowest with $f<\tfrac12$. For $N=112$ it grows from $0.0955$ ($T=0$) to $0.1161$ ($T=0.1m$, the HOMO shell has $f<\tfrac12$) and $0.4307$ ($T\ge0.3m$, where $\mu$ has dropped below the first band shell).

### 10.3 The excitation spectrum at finite temperature

The file `levels.csv` of every thermo run is the Kohn–Sham quasi-particle excitation spectrum at that $T$: every level with its Fermi–Dirac occupation $f$ (particle branch) or hole occupation $1-f$ (sea branch, the thermal antiparticles), multiplicity, Prüfer index and charges. The figure shows the occupations of $N=8$ at $\lambda=0$: at $T=0.1m$ the zero modes are partly emptied into the band; at $T=m$ the sea levels with $-4m<\varepsilon<0$ have $f$ between $0.98$ and $0.61$ (so up to 39 % of them are thermal antiparticles), and the particle levels are populated with $f=0.12$ at $2m$ and $0.018$ at $4m$ (`rust/thermo/m1_L3_N8_lam0_T1/levels.csv`; the window reaches $\pm18.9m$).

![Mermin–Kohn–Sham thermodynamics, $m=1$, $L=3$, $N=8$ and 112 (filled symbols: `lam0`; open: `lamp1`, `lamh`): $E$, $F=E-TS_{\mathrm{ent}}$, $S_{\mathrm{ent}}$, $C_V$ and the KS gap against $T$ (symmetric logarithmic scales where needed), and the occupation of the levels of $N=8$, $\lambda=0$ at $T/m=0.1$, $0.3$ and $1$ (sea levels $\varepsilon<0$: $f<1$ means thermal antiparticles).](artifacts/dirac16complex/kohn-sham/figures/thermodynamics.png)

## 11. The energy-momentum tensor and the source the field requires

### 11.1 The energy-momentum tensor of a Kohn–Sham state

The Stage-2 energy-momentum tensor, with the expectation-value rule, gives for one stationary mode in the real block form ($n=a^2+b^2$, $S=-2sab$, $P_1=-s\kappa k(a^2-b^2)$; per unit proper volume after the factor $e^{-6Hy}/\ell^3$) $\rho=\varepsilon n$, $p_1=P_1$, $p_y=(\varepsilon-v_x)n-P_1-M_{\mathrm{eff}}S$ (the local virial relation of the reduced equation) and $p_t=0$ in the extra-time directions ($q=0$). Summing over the occupied modes with the normal-ordered weights and adding the on-shell interaction density $L_s=\tfrac\lambda2S_p^2+e_x(n_p,S_p)$ with the sign of the physics contract ($\rho=-T^4{}_4$):

$$
\begin{aligned}
\rho(y)&=\frac{e^{-6Hy}}{\ell^3}\sum\mathrm{mult}\cdot w\,\varepsilon\,n-L_s(y),\\
p_y(y)&=\frac{e^{-6Hy}}{\ell^3}\sum\mathrm{mult}\cdot w\,\bigl[(\varepsilon-v_x)n-P_1-M_{\mathrm{eff}}S\bigr]+L_s(y),\\
p_3(y)&=\frac{e^{-6Hy}}{3\ell^3}\sum\mathrm{mult}\cdot w\,P_1+L_s(y),\qquad p_t(y)=L_s(y),
\end{aligned}
$$

where $p_3$ is the pressure in each 3-space direction (the closed shells are isotropic) and $p_t$ the pressure in each extra-time direction. The Wolfram verifier derives these reductions from the full tensor (the 22 checks `KS_emt_*`: the diagonal components contain only the physical densities, the off-diagonal $T^y{}_4$ and $T^y{}_1$ are proportional to the y-current, which vanishes, and $T^4{}_1$ cancels over a closed shell). Two identities hold for the self-consistent state: $\int\rho\,dV_7=E$, the Kohn–Sham energy, exactly; and the y-component of $\nabla_\mu T^\mu{}_\nu=0$, $p_y'+6Hp_y-3Hp_3-3Hp_t=0$, because the potentials are linear in the densities and the force terms cancel against $L_s'$. The Rust program checks both in every emt run: $\int\rho\,dV_7$ equals $E$ to $7.7\times10^{-10}$ relative at most, and the normalised conservation residual is at most $2.1\times10^{-5}$ (`run.json`: `energyFromRho`, `conservationResidualMax_normalised`). The proper-volume average is $\langle X\rangle=\int X\,e^{6Hy}dy\big/\int e^{6Hy}dy$, and the equation-of-state ratios are $w_y=\langle p_y\rangle/\langle\rho\rangle$, $w_3=\langle p_3\rangle/\langle\rho\rangle$ and $w_t=\langle p_t\rangle/\langle\rho\rangle$.

### 11.2 Averages and equations of state

From `rust/emt/summary.json` ($m=H=1$, $L=3$; densities per unit proper volume in units of $m^8$; $\kappa(\rho)$ is the gravitational coupling that $\rho_{\mathrm{req}}=-21H^2/\kappa$ would need, $\kappa=-21/\langle\rho\rangle$, undefined where $\langle\rho\rangle=0$):

```text
   N  coupling       <rho>      <p_y>      <p_3>      <p_t>     w_y     w_3  kappa(rho)
   8  0            0.000e+00  0.000e+00  0.000e+00  0.000e+00       -       -           -
   8  +lh1        -3.730e-07 -3.360e-06 -3.695e-07 -3.695e-07  9.0099  0.9907  5.6305e+07
   8  -lh1         3.730e-07  3.360e-06  3.695e-07  3.695e-07  9.0099  0.9907 -5.6305e+07
 112  0            2.309e-02  1.037e-02  6.865e-03  0.000e+00  0.4493  0.2973     -909.52
 112  +lh1         2.310e-02  1.044e-02  6.868e-03  8.562e-06  0.4518  0.2973     -909.19
 112  -lh1         2.308e-02  1.032e-02  6.862e-03 -8.278e-06  0.4469  0.2973     -909.85
1016  0            4.260e-01  1.429e-01  1.234e-01  0.000e+00  0.3356  0.2897     -49.296
1016  +lh1         4.260e-01  1.430e-01  1.234e-01  8.988e-06  0.3356  0.2898     -49.295
1016  -lh1         4.260e-01  1.429e-01  1.234e-01 -9.918e-06  0.3355  0.2897     -49.297
 112  +lh1, T=0.3  6.337e-02  2.038e-02  1.736e-02  2.918e-06  0.3217  0.2739      -331.4
```

- **States with bulk levels** ($N=112$, 1016, and $N=112$ at $T=0.3m$) have $\langle\rho\rangle>0$ and positive pressures in the hidden direction and in 3-space: $w_y=0.45$ and $0.34$, $w_3=0.297$ and $0.290$ for $N=112$ and 1016 at $\lambda=0$. The extra-time pressure is pure interaction, $p_t=L_s$, and vanishes at $\lambda=0$; at $\pm\hat\lambda_1$ it is of order $10^{-5}$ with the sign of $\lambda$.
- **$N=8$.** The zero modes have $\varepsilon=0$, so $\langle\rho\rangle=0$ without interaction and every $w$ is undefined. At $\pm\hat\lambda_1$ the vector potential moves the zero modes to $\varepsilon=\pm\langle v_x\rangle$ and $\langle\rho\rangle=\mp3.73\times10^{-7}$: negative for the repulsive coupling. The ratios $w_y=9.01$ and $w_3=w_t=0.991$ of these tiny averages carry no physical weight.
- **Profiles.** The energy density is largest near the tip in proper units and, weighted with the proper volume ($\rho\,e^{6Hy}$, the energy per unit $y$), largest at the brane (figure). Near the tip the local ratios $p/\rho$ of the interacting states vary strongly and become negative ($w_y$ reaches about $-0.8$ for $N=112$ near $y=-2.8$).

![Energy-momentum tensor of the ground states at $+\hat\lambda_1$, $m=1$, $L=3$: the proper densities $\rho$, $p_y$, $p_3$ and $p_t$ of $N=112$ and $N=1016$ (symmetric logarithmic scale), the local ratios $w_y(y)$ and $w_3(y)$ with $w_{\mathrm{req}}=-5/7$ (dotted), and the energy per unit $y$, $\rho\,e^{6Hy}$.](artifacts/dirac16complex/kohn-sham/figures/emt_profiles.png)

### 11.3 Comparison with the source the field requires

The static field needs, in 8-dimensional Einstein gravity, the source $\rho_{\mathrm{req}}=-21H^2/\kappa<0$ with $p_{\mathrm{req}}=+15H^2/\kappa$ and $w_{\mathrm{req}}=-5/7$ (Section 4.3). The Kohn–Sham states do not provide it:

1. **Sign.** Every state with bulk levels has $\langle\rho\rangle>0$, so the match would need $\kappa=-909.5$ ($N=112$), $-49.30$ ($N=1016$) or $-331.4$ ($N=112$, $T=0.3m$): a negative gravitational coupling. The specification expected a positive Kohn–Sham energy density in every case; measured, this holds for 8 of the 10 emt runs and fails for $N=8$ at $\lambda=0$ ($\langle\rho\rangle=0$) and at $+\hat\lambda_1$ ($\langle\rho\rangle<0$) (`rust/emt/summary.json`: `positiveRhoExpectation`).
2. **Magnitude.** For $\kappa=H=1$ the required $|\rho_{\mathrm{req}}|=21$ exceeds $\langle\rho\rangle=0.0231$ ($N=112$) by the factor 909 and $0.426$ ($N=1016$) by 49 (derived from the table).
3. **Equation of state.** Even where the sign is compatible ($N=8$, $+\hat\lambda_1$, $\kappa=5.6\times10^7$) the pressures are not: the Kohn–Sham states have $w_y$ and $w_3$ between $0.27$ and $0.45$ (and the meaningless $9.01$ and $0.991$ of $N=8$), never near $-5/7$.

This is a statement about these Kohn–Sham states only. Erratum E4.1 shows that a homogeneous condensate can source the field under exact conditions, which Section 11.4 evaluates.

![The Kohn–Sham states (emt runs) against the source the static field requires: $\langle\rho\rangle$ against $\rho_{\mathrm{req}}$ at $\kappa=1$; $w_y$ and $w_3$ against $w_{\mathrm{req}}=-5/7$; the $\kappa$ that each condition would need (from $\rho_{\mathrm{req}}$ and from the E4.1 mass condition); and $\lambda\langle S_p\rangle/m$ against the value $-5/6$ that E4.1 requires.](artifacts/dirac16complex/kohn-sham/figures/einstein_source.png)

### 11.4 The E4.1 sourcing conditions, the sign of $S$ and the mirror sector

**The conditions.** For the static field ($a_4'=0$) a homogeneous state sources the field in all 64 Einstein components exactly when $mS=-36H^2/\kappa$ and $\lambda S^2=30H^2/\kappa$ (erratum E4.1, with $\kappa>0$), which together require $\lambda S/m=-5/6$ and $mS<0$. The Rust program evaluates them on the proper-volume average $\langle S_p\rangle$ of every emt run (`run.json`: `emt.E41_sourcingConditions`): the coupling each condition would need, $\kappa_{\mathrm{mass}}=-36H^2/(m\langle S_p\rangle)$ and $\kappa_{\mathrm{coupling}}=30H^2/(\lambda\langle S_p\rangle^2)$, the ratio $\lambda\langle S_p\rangle/m$, and the first-order estimate $\hat\lambda_{\mathrm{needed}}=-\tfrac56m^7/\langle S_p\rangle$ of the coupling at which the two would coincide (first order, because the self-consistent $\langle S_p\rangle$ itself changes with $\lambda$). The verdict "met" requires both $\kappa$ finite, positive and equal to $10^{-6}$ relative; together with $\rho_{\mathrm{req}}$ a third value of $\kappa$ must agree. From `rust/emt/summary.json` (`l<S_p>/m` is $\lambda\langle S_p\rangle/m$, `lh needed` is $\hat\lambda_{\mathrm{needed}}$, `ratio` is $\hat\lambda_{\mathrm{needed}}/\hat\lambda_2$ of the same $N$, derived):

```text
   N  coupling       <S_p>  l<S_p>/m  kappa(mass)  kappa(coupl.)  lh needed     ratio
   8  0            0.000e+00         0            -              -          -         -
   8  +lh1         2.987e-06  2.91e-08   -1.205e+07      3.455e+14 -2.789e+05 -2.87e+06
   8  -lh1        -2.987e-06  2.91e-08    1.205e+07     -3.455e+14  2.789e+05  2.87e+06
 112  0           -7.881e-03         0         4568              -      105.7  1.11e+03
 112  +lh1        -7.916e-03 -7.57e-05         4548      5.003e+07      105.3   1.1e+03
 112  -lh1        -7.847e-03  7.51e-05         4588     -5.092e+07      106.2  1.11e+03
1016  0           -8.723e-02         0        412.7              -      9.553  6.06e+03
1016  +lh1        -8.724e-02 -1.38e-05        412.7        2.5e+07      9.552  6.06e+03
1016  -lh1        -8.723e-02  1.38e-05        412.7       -2.5e+07      9.553  6.06e+03
 112  +lh1, T=0.3 -9.079e-03 -8.69e-05         3965      3.804e+07      91.78       959
```

The conditions are met in no run. In the states with bulk levels $\langle S_p\rangle<0$, so $mS<0$ and the mass condition alone gives a positive $\kappa$ (4568 for $N=112$, 412.7 for $N=1016$), but the energy condition needs a negative one (Section 11.3), and the coupling condition needs the repulsive coupling $\hat\lambda\approx106$ ($N=112$) or $9.55$ ($N=1016$) at first order, about $1.1\times10^3$ and $6.1\times10^3$ times the largest coupling used ($\hat\lambda_2$). For $N=8$, $\lambda\langle S_p\rangle/m=+2.9\times10^{-8}$ for both signs of $\lambda$: positive, while the conditions require $-5/6$.

**The sign of $S$ (measured; erratum E4.1 expected otherwise).** Erratum E4.1 expected the scalar density of a positive-energy orbital to be positive for $m>0$, so that sourcing solutions would need the $m<0$ or negative-energy sector. The measured signs are more varied: the massive bulk levels have positive scalar charge ($M/\varepsilon$ at $k=0$), the $k=0$ zero modes exactly zero, and the brane band $\varepsilon=+ck$ negative scalar charge, because $d\varepsilon/dM=k\,dc/dM<0$: the exact $c(M)=\frac{2M}{2M-H}\frac{1-e^{-(2M-H)L}}{1-e^{-2ML}}$ decreases toward 1 as $M$ grows, since a larger mass localises the mode more strongly (Hellmann–Feynman, Section 6.5; Rust unit test in `emt.rs`). The band-dominated ground states of this study therefore have $\langle S_p\rangle<0$; a state dominated by bulk levels would have $\langle S_p\rangle>0$ and would need $\kappa<0$ already in the mass condition.

**The mirror sector: the Kohn–Sham form of the $\gamma^8$ map (derived in the `emt.rs` header).** In a block, the swap $(a,b)\to(b,a)$ turns the real system $a'=Ma+(E-\kappa k)b$, $b'=-(E+\kappa k)a-Mb$ into the same system with $(M,E)\to(-M,-E)$, and $s\to-s$ maps $E=s(\varepsilon-v_x)$ to $-E$ at fixed $\varepsilon$. The swap together with $s\to-s$ therefore maps the Kohn–Sham problem $(m,\lambda)$ with the tip bag $b(-L)=0$ exactly onto $(-m,\lambda)$ with the opposite bag $a(-L)=0$ and exchanged brane parities: identical energies, number densities and 3-space pressures, $S\to-S$ (since $-2sab$ changes sign), and $M_{\mathrm{eff}}=m+\tfrac{15}{16}\lambda S_p\to-M_{\mathrm{eff}}$ self-consistently with the same $\lambda$. Hence $mS$, $\lambda S^2$ and the E4.1 verdict are the same in the mirror sector, and the $m<0$ sector of Section 4.7 offers no Kohn–Sham state that the computed ones do not already represent. The operator identity $\mathcal L_{m,U}[\gamma^8\Psi]=-\mathcal L_{-m,-U}[\Psi]$ of the physics contract (erratum E2) carries an overall sign of $\mathcal L$, which reverses the Krein sign of the canonical anticommutator and with it the sign of the expectation-value rule; at the mean-field level the coupling therefore keeps its sign. In the exact theory $\gamma^8$ maps block $(j,s_2,s_3)$ onto $(-j,s_2,s_3)$ (Section 5.4) and the bag $Q(\theta)$ onto $Q(\pi-\theta)$. Nothing here shows that such a mirror universe exists.

## 12. Limitations and non-claims

1. **The static member is not a model of the author's field.** Stage 4 computes the Kohn–Sham states in the static member $a_4=a_{4,0}$ of the primordial family (Section 4.1), with frozen extra times. On 2026-09-30, after this stage was specified, the author corrected the model: "x5, x6, x7 are the three extra times that exponentially deflate." With that correction a static member is not a model of the author's field (`provenance/ERRATA_FIRST_EDITION_TEXTBOOK.md`, entries (a), a1 and a2; `handoff/specs/DEFLATION_SPEC.md`). The author's field is treated anew in the later record `Revision/` (since 2026-10-14 with the second metric function $b_4(x_4)$), whose Kohn–Sham record (`Revision/kohn_sham/`, document `Revision/docs/KOHN_SHAM_DEFLATING_FIELD`) computes instantaneous Kohn–Sham states along the deflating history. This document completes the old Stage 4 as specified, for the static member, and its results should be read as those of that member only.
2. **Fixed field, no back-reaction.** The metric is prescribed; the Kohn–Sham states do not act back on it, and Section 11 shows that they could not be its Einstein source.
3. **The good sector only.** Modes with momenta along the extra times are excluded because their single-particle operator is not Hermitian and they grow without bound (Stage 1, Stage-3 EXP-5).
4. **The brane and the tip are assumptions.** The Z2 gluing at $y=0$ (the notebook's pair of universes realised as a geometry) needs a brane with the Israel stress of Section 4.6, whose existence and source are not shown. The tip $y\to-\infty$ is a singular end of the transverse geometry and is replaced by a cutoff $L$ with a chosen bag condition ($\theta=0$ of the chiral-bag family). The brane conditions are of the block-diagonal type $P_A$, a symmetry only for a mass function that is odd across the brane (erratum E4.6); the even-mass alternative $P_B$ couples block pairs and is not computed. Both brane parities are filled together.
5. **Finite torus and finite cutoff.** All results are for $\Delta k=0.25m$ and $L\le4$; the first excited state is a shell effect of the torus, and halving $\Delta k$ at fixed density changes the energy per particle by 6.6 % (Section 8.6). The dependence on $L$ is compared like with like only at $\lambda=0$, because the couplings are set per configuration (Section 7.1); no single physical coupling is held fixed across $N$ and $L$.
6. **The functional.** The exchange is the exact Hartree–Fock exchange of the uniform gas evaluated at the local densities (variant VS, a recorded deviation from the specification's variant V, Section 6.4); the block-resolved structure of the exact Fock term and every correlation effect are not included, and the contact interaction beyond Hartree–Fock is not renormalisable in 8 dimensions. The Dirac sea is normal ordered with respect to the free sea and enters only through holes at $T>0$; vacuum polarisation is not included.
7. **Mean-field excitations.** The KS gap, the particle-hole energies and $\Delta$SCF are mean-field estimates of the first excitation, not exact excitation energies.
8. **The level-crossing ensemble.** The ground state of $N=1016$ at $-\hat\lambda_2$ is defined by continuation from $\lambda=0$ with an occupation smearing of $10^{-3}m$ (Section 9.3); a state about $1.01m$ higher exists, and other definitions of the ground state at a degenerate crossing are possible.
9. **Thermodynamics.** At $T=m$ the energy window neglects levels with $f<10^{-8}$; the neglected Boltzmann tail is estimated in the crate documentation as about $10^{-5}$ of $E$. The coupling $\hat\lambda_1$ is not run at $T=m$ (Section 10.1).
10. **No physical claims beyond the computation.** Nothing in this document shows that the primordial field, the brane, the mirror universe or the $\pm M$ pair exists, that a big bang produces them, or that dirac16complex is dark matter or dark energy. The (4,4) signature is not the observed spacetime.

## 13. Verification

### 13.1 The exact theory

- **Wolfram.** `wolfram/Dirac16ComplexKohnSham.wl` with the verifier `scripts/verify_dirac16complex_kohn_sham.wls` passes 125 of 125 exact checks (`wolfram-kohn-sham-report.json`): fixture 4, internal 2, geometry 18, reduction 32, boundary conditions 18, exchange 20, functional 9 and energy-momentum tensor 22. It exports every explicit matrix of Sections 4 to 6 to `kohn-sham-theory.json`.
- **sympy, independent.** `scripts/check_dirac16complex_kohn_sham_theory.py` re-derives the same theory without Wolfram and passes 157 of 157 checks (`python-theory-report.json`), among them 20 comparisons with the exported Wolfram values (Einstein tensor, required source, extrinsic curvature, brane stress, the block basis vector by vector, the block matrices, the zero-mode splitting, the parity projectors, the filled-shell ratio, the exchange closed form, the kernels and the off-diagonal energy-momentum coefficients) and the summary check `KS_agreesWithWolfram`. It also writes the exchange table of Section 6.3.
- **The programs' block forms.** The Rust constants generator verifies the exact $2\times2$ reduction of its own basis in Gaussian-integer arithmetic (`rust/generator-report.json`, 30 of 30 checks). The Rust `spectrum` subcommand compares its reduction with `kohn-sham-theory.json` (the 15 checks `theory_*` of `rust/spectrum/summary.json`) and records the relation of the labels in `rust/spectrum/theory-agreement.json`: measured on the theory's basis, the theory's block labels are $j=-J_{\mathrm{measured}}$, $s_2=-c_1$ and $s_3=-c_2$ in all eight blocks. This note was corrected on 2026-10-18: before, it recorded 0 blocks for both signs, because the program compared the measured labels, which equal $\pm1$ only to round-off, with exact equality; the comparison now uses the tolerance $10^{-12}$ (`theory::LABEL_TOLERANCE`, commit `f5bd84b`), and the other 14 files of the `spectrum` tree were reproduced byte for byte. The reference solver derives its own reduction from the fixture, and the Mathematica notebook proves $s=-j$ for the Rust basis (`rustLabelSIsMinusJEigenvalue`).

### 13.2 The Rust program

- **Self-checks.** The five subcommands pass all 397 of their own checks (spectrum 33, scf 137, excited 65, thermo 102, emt 60), among them: the reduction exact to $10^{-14}$, the curvature, required source and brane stress re-derived numerically, the exchange identities, the free $k=0$ spectra against the closed forms, the level residuals, convergence and particle-number conservation of every run, $\int\rho\,dV_7=E$ and the y-conservation of the energy-momentum tensor, the Hellmann–Feynman identity $dE/dm=\int S_p\,dV_7$ (five-point finite difference with the step $10^{-3}m$ for $N=112$ at $\lambda=0$ and $+\hat\lambda_1$, tolerance $10^{-5}$ relative), the $a_{4,0}$ rescaling pair, the grid refinements, positive $\Delta$SCF energies and gaps, $F(T)$ decreasing, $S_{\mathrm{ent}}\ge0$ and $C_V\ge0$, and the E4.1 evaluation.
- **Unit tests, format and lints.** `cargo test --release`, `cargo clippy --release --all-targets -- -D warnings` and `cargo fmt --check` (results in Section 13.5).
- **Determinism and tolerance convergence** (`rust/determinism-report.json`, written by `studies/dirac16complex_kohn_sham/tools/compare_runs.py`): a second complete run is byte-identical to the committed tree in every file the summaries list, and a `--refined` run agrees with it within $10^{-7}$ relative in the energies and $10^{-7}$ absolute in the eigenvalues (values in Section 13.5).
- **Provenance of the committed tree.** `spectrum`, `scf` and `thermo` were produced by one release build, `emt` by a later build that differs only in the emt bookkeeping, and `excited` by the build that added the occupation-floor particle-hole rule and the 601-point refinement run (crate `README.md`); the file `spectrum/theory-agreement.json` was regenerated on 2026-10-18 by the build with the label-tolerance fix. Every subcommand is reproduced with the final build by the determinism run and by the Stage-4 gate.

### 13.3 The notebooks

- **Mathematica** (`mathematica-report.json`, Wolfram 15.0): 94 of 94 checks. The 352 exact $k=0$ box levels agree with the Rust $k=0$ levels to $2.8\times10^{-10}$, and the notebook's `NDSolve` shooting reproduces the exact box to $5.2\times10^{-12}$. Over the six free spectra ($m=1,3$, $L=2,3,4$; 2818 levels with identical keys) the notebook's shooting agrees with the Rust levels to $1.17\times10^{-9}$, with the scalar charges to $1.3\times10^{-10}$ and with the pressure charges to $1.0\times10^{-9}$. The zero-mode slopes agree with $\mp c$ to $1.6\times10^{-7}$, and the closed-shell tables (20 and 22 entries) with the Rust tables to $5.3\times10^{-11}$. Its own self-consistent loop in Wolfram Language on the discrete problem of the Rust code ($N=8$, $+\hat\lambda_2$; 20 iterations to the residual $6.1\times10^{-13}$) reproduces the Rust $\varepsilon_{\mathrm{HOMO}}$ to $1.2\times10^{-14}$, $E_0$ to $3.4\times10^{-12}$ ($4.3\times10^{-10}$ relative), $M_{\mathrm{eff}}$ to $1.1\times10^{-8}$ (tolerance $6.1\times10^{-6}$), $v_x$ to $3.2\times10^{-9}$, the 788 levels of the final potential to $5.4\times10^{-10}$ and the KS gap to $5.0\times10^{-12}$. The notebook also runs the Rust binary (`print-config`) and checks the printed equations, boundary conditions, exchange formulas and parameters against its own derivations.
- **Jupyter** (`notebook-report.json`): the audit of the executed notebook and its gauntlet (Section 13.5).
