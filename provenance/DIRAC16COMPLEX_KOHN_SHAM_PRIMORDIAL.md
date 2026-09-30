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
&R=-42H^2,\qquad R^\mu{}_\nu=\mathrm{diag}(-6,-6,-6,-6,0,-6,-6,-6)\,H^2,\qquad G^\mu{}_\nu=\mathrm{diag}(15,15,15,15,21,15,15,15)\,H^2,\
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
\Omega_y=\Omega_4=0,\qquad \Omega_{x_i}=-He^{Hy+a_{4,0}}S^{0i}\ (i=1,2,3),\qquad \Omega_{x_j}=+He^{Hy-a_{4,0}}S^{0j}\ (j=5,6,7),\qquad \gamma^\mu\Omega_\mu=3H\gamma^0 ,
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

eight blocks whose projectors sum to 1. In each block the basis is $v_+=8P(j,s_2,s_3)\tfrac12(1+\gamma^0)e_c$ (with $e_c$ the first standard basis vector with nonzero image) and $v_-=\gamma^0\gamma^1v_+$; the entries are in $\{0,\pm1,\pm i\}$ and $|v_\pm|^2=8$, so $V=[v_+\,v_-\,\cdots]/(2\sqrt2)$ is unitary and $\chi_{16}=V\chi_{\mathrm{block}}$. The block index is $\beta=4(1-j)/2+2(1-s_2)/2+(1-s_3)/2$, i.e. $(j,s_2,s_3)=(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)$ for $\beta=0,\dots,7$. The unnormalised basis matrix $2\sqrt2\,V$ (rows: spinor components $\Psi_0,\dots,\Psi_{15}$; columns: $v_+,v_-$ of block 0, then block 1, and so on), exported exactly in `kohn-sham-theory.json`, is

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

(`KS_reduction_blockODEMatrix`, `KS_reduction_blockHamiltonianEquivalentToODE`). **Real form used by the programs.** With $\chi=(a,ib)$ and the program label $s=-j$ the system is real, $a'=M_{\mathrm{eff}}a+(s(\varepsilon-v_x)-\kappa k)b$, $b'=-(s(\varepsilon-v_x)+\kappa k)a-M_{\mathrm{eff}}b$ (the equation printed by `print-config`; Mathematica check `realFormIsBlockODEWithSMinusJ`).

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
