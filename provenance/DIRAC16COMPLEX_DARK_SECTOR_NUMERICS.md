# dirac16complex and the dark sector: pressure, energy density and equation of state from numerical solutions

## Five CVODE experiments, their independent verification, and whether the framework is connected to dark matter or dark energy

## Abstract

This is the Stage-3 document of the dirac16complex project. It asks how the pressure and the energy density of dirac16complex behave and change in gravitational backgrounds, and whether the framework has any connection to dark matter or dark energy. dirac16complex is the complex, Grassmann-odd, 16-component spinor of Spin(4,4) of Stages 1 and 2. Five experiments were solved as ordinary differential equations with the pure-Rust SUNDIALS 7.8.0 CVODE engine of the rustSolveIt repositories. EXP-1 puts the field in the primordial pair-creation background of the author's notebook. EXP-2 is a self-consistent homogeneous 8-dimensional Einstein cosmology sourced by a mean-field condensate. EXP-3 is a 4-dimensional effective late universe in which the condensate plays the role of dark energy, compared with the Unite supernova results $(w_0,w_a)=(-0.861,-0.60)$ and $w=-0.764$. EXP-4 follows a thermal Fermi gas of dirac16complex quanta and their gravitational pair creation at the end of inflation. EXP-5 follows the modes with momentum along the extra times. All 69 self-checks of the Rust program pass, as do all 162 checks of five independent numpy checkers (including repeat-run byte identity and refined-tolerance convergence), all 9 checks of the EXP-3 analysis, all 70 assertions of a Jupyter notebook and all 49 checks of a Mathematica notebook that re-derives every reduced equation symbolically and re-integrates the solutions with NDSolve. **Dark matter:** in the sector without extra-time momentum the quanta are ordinary massive fermions. Their gas has $w=0.3329$ at temperature $T=10m$ and $w=0.0359$ after the scale factor has grown a hundredfold, and expansion creates them for $m>0$ (comoving number $na^3$ between $1.45\times10^{-3}$ and $4.99\times10^{-3}$ in units of $H_{\mathrm{inf}}^3$) but not for $m=0$. That is a dark-matter-like equation of state and a production mechanism, not a dark-matter model: the abundance, the darkness, and the stabilisation of the extra dimensions that dust-like dilution in 3-space needs were neither computed nor derived. **Dark energy:** negative pressure arises only from an attractive four-fermion interaction, and then with a crossing of $w=-1$ at the instant where the effective mass vanishes. Tuned to the Unite value $w_0=-0.861$, the condensate has $w_a=-4.81$, crosses $w=-1$ at redshift $z=0.026$, has negative energy density beyond $z=0.293$ and a bounce ($H=0$) at $z=0.388$, so the model has no matter era; its adiabatic sound speed squared today is $-12.4$. Deflating extra times reproduce the Unite tangent of $p/\rho$ but violate 4-dimensional energy conservation, imply $\dot G/G=2.63\,H_0$ and need a negative 8-dimensional energy density. Within everything computed here the framework does not provide viable dark energy, and it reproduces neither the Unite $(w_0,w_a)$ nor $w=-0.764$ consistently. All results are homogeneous and mean-field; no perturbations and no data likelihood were computed.

## 1. The question and the short answer

The question of this stage is: *in detail, investigate, determine and discuss, using numerical solutions and graphs, the physical behaviour and changing nature of pressure and energy density in this framework; is there any connection to dark matter and/or dark energy?*

The short answer, which Section 12 argues in full:

- **What makes $\rho$ and $p$ change?** The 7-volume $V$ (the condensate density obeys $SV=$ const), the redshift of momenta, and the self-interaction $\lambda$.
- **Does anything behave like dark matter?** Yes in its equation of state: free condensates are exact dust, a gas of quanta goes from $w=1/3$ to $w\to0$, and pairs are created gravitationally for $m>0$.
- **Is it a dark-matter model?** No: the abundance, the darkness, the stabilisation of the extra dimensions and the perturbations are not established.
- **Does anything give $w<-1/3$?** Only an attractive four-fermion term ($\lambda<0$), and, as a dilution effect only, the frozen density of the primordial field.
- **Does it fit Unite?** No: $w_0=-0.861$ forces $w_a=-4.81$, negative energy density beyond $z=0.293$ and a bounce at $z=0.388$.
- **Deflating extra times?** They match the Unite tangent of $p/\rho$ but break 4D energy conservation, the constancy of $G_N$ and the 8D energy bound.

## 2. Scope and non-claims

**Scope.** The object is the Stage-1 field with the Lagrangian of Section 4.1. The backgrounds are homogeneous. Every computed number in this document is copied from a committed output: the summary.json files of the Rust study, the python-check-report.json files of the independent checkers, fits.json of the EXP-3 analysis, numerics-summary.json, notebook-report.json and mathematica-report.json (Section 14). The Unite values and the scalar-field formulas are quoted from the reference PDF (Section 3.3). Where a statement is derived here from those numbers or from verified closed forms rather than machine-checked, the text says so.

**Non-claims.**

1. No claim is made that dirac16complex is dark matter or dark energy. The computations show which equations of state the framework can produce and what goes wrong.
2. The signature (4,4) is not observed spacetime. EXP-3 and EXP-4 assume that the hidden space and the extra times are static (stabilised). That assumption is not derived; EXP-2 shows that 8-dimensional Einstein gravity with this matter does not stabilise them.
3. All condensate results are mean-field: the bilinears are evaluated on one c-number mode by the expectation-value rule of Section 4.6. The gas and pair-creation results are sums over free modes. No interacting quantum field theory, renormalisation or loop correction is computed.
4. No perturbations, no structure formation, no CMB, BAO or supernova likelihood and no parameter estimation were computed. The distance-modulus fits of EXP-3 are fits of noise-free model curves with equal weights.
5. The Unite numbers and the scalar-field formulas are taken from the reference PDF (Section 3.3); they are not re-derived from data here.

## 3. Notation and conventions

### 3.1 Coordinates, units and matrices

- Everything is counted from 0: coordinates $x_0,\dots,x_7$, frame indices $a=0,\dots,7$, spinor components $\Psi_0,\dots,\Psi_{15}$. The tangent metric is $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$: directions 0 to 3 are space-like, 4 to 7 time-like. $x_4$ is the evolution time $t$; $x_0$ is the hidden space, $x_1,x_2,x_3$ are 3-space and $x_5,x_6,x_7$ are the three extra times.
- $\gamma^a$ are the real integer 16 by 16 gamma matrices of the split-octonion (notebook) basis, $\{\gamma^a,\gamma^b\}=2\eta^{ab}$. $C=\gamma^0\gamma^1\gamma^2\gamma^3$ is the charge (adjoint) matrix, $\bar\Psi=\Psi^\dagger C$, and $B=-iC\gamma^4$ is Hermitian with $B^2=1$ and eigenvalues $\pm1$ (8 each). $u^\dagger u$ is the Hilbert norm and $u^\dagger Bu$ the Krein norm of a mode amplitude $u\in\mathbb C^{16}$.
- Units: EXP-1 uses $H=m=\kappa=1$ with $t=Hx_4$; EXP-2 uses $m=\kappa_8=1$; EXP-3 uses $H_0=c=1$ and densities in units of $3H_0^2/\kappa_4$; EXP-4 uses $m=1$ for the gas and $H_{\mathrm{inf}}=1$ for pair creation; EXP-5 uses $H=m=1$.

### 3.2 Symbols that are used twice

- $x_0$ is the hidden coordinate, and in EXP-2 and EXP-3 also the dimensionless coupling $x_0=\lambda S_0/(2m)$ (the reports call it x0). The coupling always appears as a number, for example $x_0=-0.462654$.
- $z=6Hx_0$ in the primordial field (Stage 2); $z$ is the redshift in EXP-3.
- $\mu$ is the reduced spinor frequency of EXP-3; the distance modulus is written $\mathrm{DM}(z)$.
- $K$ is the hidden-space momentum in EXP-1 and the physical momentum $k/a$ in EXP-4.
- $q$ is the extra-time momentum of EXP-5; the deceleration parameter is written $q_{\mathrm{dec}}$.
- $\gamma$ is also the extra-time deflation index of the EXP-3 variant ($c\propto a^{-\gamma}$); it never carries an index there.
- $H$ is the notebook's inverse length in EXP-1, $H_i$ are Hubble rates, $H_0$ is today's Hubble rate and $H_{\mathrm{inf}}$ the de Sitter rate of EXP-4. $\varkappa(t)$ is the WKB growth rate of EXP-5.

### 3.3 The reference PDF, the CPL form and a sign discrepancy

The reference on the equation of state is the PDF in the repository root whose name begins with "Gmail - w = equation of state parameter" (an input, git-ignored and not committed). It treats a canonical scalar field with $\mathcal L_\phi=\tfrac12\partial_\mu\phi\,\partial^\mu\phi-V(\phi)$ in signature $(+,-,-,-)$, for which $\rho_\phi=\tfrac12\dot\phi^2+V$, $P_\phi=\tfrac12\dot\phi^2-V$, $w_\phi=P_\phi/\rho_\phi$ and $\ddot\phi+3H\dot\phi+V'(\phi)=0$. Our conventions (mostly plus for space, $\mathcal L=-\tfrac12g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi-V$) give the same $\rho$ and $p$. The PDF states that a canonical field has $w\ge-1$ and that crossing the phantom divide $w=-1$ needs non-canonical physics.

The PDF uses the Chevallier-Polarski-Linder (CPL) form $w(a)=w_0+w_a(1-a)$. It quotes the Unite supernova compilation (Pantheon+ and DES-SN5YR combined): the time-evolving fit $w_0=-0.861$ (also written $\approx-0.86$), $w_a=-0.60$, hence $w_0+w_a=-1.461$ in the deep past (phantom); and a constant-$w$ (wCDM) fit $w=-0.764$ of the supernovae alone, "roughly two standard deviations" from $-1$. No error bars on $(w_0,w_a)$ are given in the PDF. It lists the $\Lambda$CDM components as radiation $w=1/3$, matter $w=0$, dark matter $w=0$ and the cosmological constant $w=-1$.

**Sign discrepancy in the PDF.** From its own formula, $dw/da=-w_a$. Since $a$ grows with time, a field whose $w$ starts near $-1$ and increases (thawing) has $w_a<0$, and a field whose $w$ approaches $-1$ from above (freezing) has $w_a>0$. The PDF's table of thawing and freezing models writes the opposite: thawing "($w_a>0$)" and freezing "($w_a<0$)". This document uses the formula-consistent signs throughout: **thawing means $w_a<0$, freezing means $w_a>0$.** The Unite fit ($w_a=-0.60$) is thawing in this sense, and so is every attractive dirac16complex condensate of EXP-3.

## 4. The framework

### 4.1 Field and Lagrangian

$\Psi=(\Psi_0,\dots,\Psi_{15})^T$ has complex Grassmann-odd components and is a section of the complex spinor bundle of Spin(4,4). It couples to gravity through the vielbein $e_\mu{}^a$ and the canonical spin connection $\Omega_\mu=\tfrac12\omega_{\mu ab}S^{ab}$, $S^{ab}=\tfrac14[\gamma^a,\gamma^b]$, with $D_\mu\Psi=\partial_\mu\Psi+\Omega_\mu\Psi$ (Stage 1). The Lagrangian is

$$
\begin{aligned}
&\mathcal L=\sqrt{|g|}\,\Bigl[\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)-m\,\bar\Psi\Psi-U(\bar\Psi\Psi)\Bigr],\\
&\bar\Psi=\Psi^\dagger C,\qquad S=\bar\Psi\Psi,\qquad U(S)=\tfrac\lambda2S^2,\qquad M_{\mathrm{eff}}=m+U'(S)=m+\lambda S .
\end{aligned}
$$

There is no factor $i$ ($C\gamma^a$ is real antisymmetric) and no cosmological constant: for a Grassmann field $U$ must be a polynomial with $U(0)=U'(0)=0$. $\lambda<0$ is an attractive and $\lambda>0$ a repulsive four-fermion contact interaction.

### 4.2 Field equations

$$
\gamma^\mu D_\mu\Psi=(m+\lambda S)\Psi,\qquad (D_\mu\bar\Psi)\gamma^\mu=-(m+\lambda S)\bar\Psi .
$$

The spin connection cannot be gauged away in a curved field: $(\gamma^\mu D_\mu)^2\Psi=g^{\mu\nu}(D_\mu D_\nu\Psi-\Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi)-\tfrac14R\,\Psi$ (Stage 1, Lichnerowicz coefficient $-1/4$). For a diagonal vielbein $e_\mu{}^a=\mathrm{diag}(h_0,\dots,h_7)$, $\gamma^\mu\Omega_\mu=\tfrac12\sum_b h_b^{-1}\partial_b\ln(\prod_{c\ne b}h_c)\,\gamma^b$.

### 4.3 Energy-momentum tensor, energy density and pressures

$$
\begin{aligned}
&T_{\mu\nu}=-\tfrac14\Bigl[\bar\Psi\gamma_\mu D_\nu\Psi+\bar\Psi\gamma_\nu D_\mu\Psi-(D_\mu\bar\Psi)\gamma_\nu\Psi-(D_\nu\bar\Psi)\gamma_\mu\Psi\Bigr]+g_{\mu\nu}\mathcal L_s,\\
&\mathcal L_s=\mathcal L/\sqrt{|g|}\ \overset{\text{on shell}}{=}\ SU'(S)-U(S),\qquad T^\mu{}_\mu\ \overset{\text{on shell}}{=}\ -mS+3\lambda S^2 .
\end{aligned}
$$

With Gaussian normal time ($g_{44}=-1$) and the observer $u=\partial_4$: $\rho=T_{44}$, $p_{(i)}=T^i{}_i$ (no sum) for the seven transverse directions $i\ne4$ (four space-like, three time-like), $\bar p=\tfrac17\sum_{i\ne4}p_{(i)}$ and $w=p/\rho$ (or $\bar w=\bar p/\rho$ when the pressures differ).

### 4.4 Kinetic and potential energy, and the equation of state

Two exact splits are used, as in Stage 1. With $K_4=\tfrac12(\bar\Psi\gamma^{x_4}D_4\Psi-(D_4\bar\Psi)\gamma^{x_4}\Psi)$ and $K_\perp$ the other seven terms of the kinetic term:

- **(A) Lagrangian split**, the exact analogue of the scalar field's $\tfrac12\dot\phi^2$ and $V$: $\mathrm{KE}_L=\tfrac12K_4$, $\mathrm{PE}_L=\rho-\mathrm{KE}_L$.
- **(B) Hamiltonian split**: $\mathrm{KE}_H=-K_\perp$ (momentum or gradient energy), $\mathrm{PE}_H=mS+U$ (rest mass and interaction), and $\rho=\mathrm{KE}_H+\mathrm{PE}_H$ identically.

For a homogeneous isotropic condensate on shell:

$$
\begin{aligned}
&\rho=mS+\tfrac\lambda2S^2,\qquad p=\tfrac\lambda2S^2,\qquad w=\frac{\lambda S}{2m+\lambda S}=\frac{\mathrm{KE}_L-\mathrm{PE}_L}{\mathrm{KE}_L+\mathrm{PE}_L},\\
&\mathrm{KE}_L=\tfrac12S(m+\lambda S),\qquad \mathrm{PE}_L=\tfrac12mS,\qquad \mathrm{KE}_H=0,\qquad \mathrm{PE}_H=\rho,\qquad \rho+p=2\,\mathrm{KE}_L=S\,M_{\mathrm{eff}} .
\end{aligned}
$$

So a free condensate ($\lambda=0$) is exact dust ($\mathrm{KE}_L=\mathrm{PE}_L$, $w=0$), a repulsive one is stiffer than dust ($0<w<1$), and an attractive one has negative pressure. For $\rho>0$ the state is phantom ($w<-1$) exactly when $\mathrm{KE}_L<0$, that is when $M_{\mathrm{eff}}=m+\lambda S<0$. Unlike $\tfrac12\dot\phi^2$, $\mathrm{KE}_L$ has no fixed sign, because the fermion Lagrangian is first order in time. For a gas of free quanta, $\mathrm{KE}_L=\mathrm{PE}_L=\rho/2$ for every mode, so the relation $p=\mathrm{KE}-\mathrm{PE}$ of split (A) holds only for homogeneous condensates; the Hamiltonian split then gives $\mathrm{KE}_H=3p$ and $\mathrm{PE}_H=\rho-3p$.

### 4.5 Homogeneous backgrounds, dilution and the mode equation

All experiments use a homogeneous diagonal metric with lapse 1,

$$
ds^2=-dt^2+\sum_{i\in T}\epsilon_i\,h_i(t)^2dx_i^2,\qquad T=\{0,1,2,3,5,6,7\},\quad \epsilon_i=+1\ (i\le3),\ -1\ (i\ge5),
$$

with Hubble rates $H_i=\dot h_i/h_i$, expansion $\Theta=\sum_iH_i$ and 7-volume $V=\prod_ih_i$. The groups are $b=h_0$ (hidden space), $a=h_1=h_2=h_3$ (3-space) and $c=h_5=h_6=h_7$ (extra times), so $\Theta=H_b+3H_a+3H_c$ and $\gamma^\mu\Omega_\mu=\tfrac12\Theta\gamma^4$. A mode $\Psi=V^{-1/2}e^{ik\cdot x}u(t)$ obeys

$$
i\dot u=h(t)\,u,\qquad h(t)=-iM_{\mathrm{eff}}\gamma^4-\gamma^4\sum_{j\in T}\frac{k_j}{h_j}\gamma^j .
$$

$h$ is Hermitian exactly when $k_5=k_6=k_7=0$. Per mode, $\varepsilon(u)=u^\dagger hu$, $p_j(u)=-(k_j/h_j)\,u^\dagger\gamma^4\gamma^ju$ (equal to $(k_j/h_j)^2/E$ on eigenmodes) and $s(u)=u^\dagger(-i\gamma^4)u$ (equal to $M_{\mathrm{eff}}/E$ on positive-energy eigenmodes). For the condensate ($k=0$) $h$ is a multiple of $-i\gamma^4$, so $s(u)$ is conserved and $S\propto1/V$ exactly, for any $M_{\mathrm{eff}}(t)$; Stage 1 derives the same law from the continuity equation $\partial_4\rho+\sum_iH_i(\rho+p_{(i)})=0$ with $\rho+p=SM_{\mathrm{eff}}$ wherever $M_{\mathrm{eff}}\ne0$. **This dilution law drives almost everything below**: $mS\propto V^{-1}$ behaves like dust, while $\tfrac\lambda2S^2\propto V^{-2}$ dominates at small volume and dies away at large volume.

### 4.6 Quantization, the good sector and the expectation-value rule

Canonical quantization with respect to $x_4$ gives $\{\Psi,\Psi^\dagger\}=B\,\delta^7/\sqrt{|g|}$ in Gaussian normal gauge. The canonical state space is a Krein space of signature (8,8) per mode. In the sector without extra-time momentum (the good sector) the single-particle Hamiltonian is Hermitian, the dispersion is $E^2=m^2+k_0^2+\dots+k_3^2$, and there is an ordinary Fock space with particles and antiparticles of energy $\sqrt{m^2+k^2}$ above a filled Dirac sea. Modes with extra-time momentum have $E^2=m^2+\dots-k_5^2-k_6^2-k_7^2$, which can become negative (Section 10). The unitarily implemented symmetry of the positive structure is Spin(4)$\times$Spin(3), generated by the 9 compact $S^{ab}$ that commute with $B$; the 4 boosts $S^{a4}$ ($a\le3$) also commute with $B$ but are Hermitian, not unitary (Stage 1, erratum E1).

**Expectation-value rule.** In the positive-norm quantization a one-particle state built on a normalised mode $u$ has $\langle\Psi^\dagger M\Psi\rangle=u^\dagger BMu$, normal ordered relative to the Dirac sea. Hence the scalar density is $s(u)=u^\dagger BCu=u^\dagger(-i\gamma^4)u$ (equal to 1 on positive-energy rest eigenvectors), never $u^\dagger Cu$ (identically 0 there). The mean-field condensate is $S=S_0(V_0/V)\,s(u)$.

### 4.7 dirac16complex beside a canonical scalar field

| Quantity | Scalar field (PDF) | dirac16complex |
| --- | --- | --- |
| energy density | $\tfrac12\dot\phi^2+V$ | $mS+\tfrac\lambda2S^2$ |
| pressure | $\tfrac12\dot\phi^2-V$ | $\tfrac\lambda2S^2$ |
| kinetic energy | $\tfrac12\dot\phi^2\ge0$ | $\mathrm{KE}_L=\tfrac12SM_{\mathrm{eff}}$, either sign |
| potential energy | $V$ | $\mathrm{PE}_L=\tfrac12mS$ |
| $w\to-1$ | $\dot\phi^2\ll V$ | $M_{\mathrm{eff}}\to0$ |
| phantom $w<-1$ | impossible for $\rho>0$ | $M_{\mathrm{eff}}<0<\rho$ |
| dilution | depends on $V(\phi)$ | $S\propto1/V$ always |
| cosmological constant | $V=$ const | absent ($U(0)=0$) |

## 5. Numerical method, software and verification strategy

### 5.1 Engine and pinned commits

Every ordinary differential equation below is integrated by CVODE of the pure-Rust SUNDIALS 7.8.0 engine (sundials_rs) from the rustSolveIt repositories of once-ere; nothing is stepped by hand. The setup scripts setup_solver.ps1 and setup_solver.sh in scripts/ clone the platform repository at a pinned commit into the git-ignored vendor/rustSolveIt:

```
https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0
  a8fdff459adfe181573d7924b18bffbdf378fdb3
https://github.com/once-ere/rustSolveIt_macos-silicon_SUNDIALS_7_8_0
  5360157f4f6160978f66400566c31b2ae25dd44d
https://github.com/once-ere/rustSolveIt_linux_SUNDIALS_7_8_0
  6f58e02e53717a51375bd4bc5918edc57088d922
```

All three vendor the same sundials_rs. The engine is BSD-3-Clause and is fetched at build time, not redistributed.

Two CVODE configurations are used (src/driver.rs of the study):

- **BDF + Newton + dense direct linear solver** with CVODE's difference-quotient Jacobian (EXP-1).
- **Adams-Moulton + fixed-point (functional) iteration**, without a linear solver (EXP-2 to EXP-5). This is the classical choice for non-stiff oscillatory problems: the Jacobian $-ih$ of the mode equation has imaginary eigenvalues in the good sector. EXP-4 selects it by a recorded test against BDF (Section 9.4).

### 5.2 The Rust study

The crate studies/dirac16complex_cosmology (edition 2021, unsafe code forbidden, warnings denied, its own workspace, compiled with the target feature +fma set in .cargo/config.toml) has this command line:

```
dirac16complex_cosmology <print-config|exp1|exp2|exp3|exp4|exp5|all>
    [--output DIR] [--rtol X] [--atol X] [--refined]
```

The refined option divides rtol and atol by 10 and max_step by 2. Following the planet_Mercury contract of rustSolveIt, every self-check prints a PASS or FAIL line and the last stdout line is SUCCESS or FAILURE. The gamma matrices, $C$, $\gamma^8$ and $B$ are generated from the Stage-1 algebra fixture into src/generated.rs, which records the fixture sha256. Outputs are deterministic: CSV with a header row, 17 significant digits, LF line ends, and one summary.json per experiment with parameters, tolerances, solver counters, the fixture hash, every check and the verdict; no timing or absolute path is written. The outputs live in the directories exp1 to exp5 under artifacts/dirac16complex/numerics.

Solver work over the five canonical runs: $2.897\times10^8$ steps and $4.374\times10^8$ right-hand-side evaluations, almost all of them in the 48 thermal modes and the 64 pair-creation modes per mass of EXP-4.

### 5.3 Independent checkers, determinism and convergence

For each experiment an independent checker (numpy and the standard library only) rebuilds the gamma matrices from the fixture and recomputes every physical quantity from the raw spinor columns of the CSV files, never from the derived columns. It checks finite-difference residuals of the right-hand side, exact or closed-form solutions and invariants, and two further properties:

- **repeat-run byte identity**: it reruns the binary into a fresh directory and requires every output file to be byte-identical;
- **refined-tolerance convergence**: it reruns with the refined option and requires the errors to shrink or, where a floor is identified, to stay within it.

An analysis script does the EXP-3 fits (Nelder-Mead in numpy; no scipy) and writes fits.json with its own 9 validation checks, and a collector writes numerics-summary.json:

```
scripts/check_dirac16complex_exp1.py ... scripts/check_dirac16complex_exp5.py
scripts/analyze_dirac16complex_exp3.py
studies/dirac16complex_cosmology/tools/build_numerics_summary.py
```

Totals: 69 of 69 Rust self-checks, 162 of 162 checker checks and 9 of 9 analysis checks true; verdict SUCCESS.

### 5.4 Notebooks and figures

Two notebooks in notebooks/ re-examine the results independently (Section 11). The Jupyter notebook dirac16complex_dark_sector.ipynb is adapted from rustSolveIt planet_Mercury/notebook: the build_notebook.py helpers md() and code(), find_binary() and run() with the last-line SUCCESS contract, a gauntlet() of assertions, the headless standard-library executor run_notebook.py and the auditor check_notebook.py. They were copied with attribution (BSD-3-Clause per the rustSolveIt Cargo manifests; author once-ere). The notebook produced the 17 figures in artifacts/dirac16complex/numerics/figures.

**None of the three rustSolveIt repositories (Win11 a8fdff45, macOS 5360157f, Linux 6f58e02e) contains a Mathematica notebook (.nb, .wl or .wls)**: this was verified by listing their full git trees, and each has 294 Jupyter notebooks. The Mathematica notebook Dirac16ComplexDarkSector.nb is therefore new. It is modelled on dirac-main's notebooks/DiracTriality.nb and its build and verify scripts build_mathematica_notebook.wls and verify_mathematica_notebook.wls (RunProcess plus Import of CSV and RawJSON). It produced the 8 figures in figures/mathematica.

## 6. EXP-1: the frozen field in the primordial pair-creation background

### 6.1 Purpose

The primordial field of the notebook inflates 3-space while three extra times deflate and the 7-volume stays constant. EXP-1 asks what dirac16complex does there and what source 8-dimensional Einstein gravity would need to produce this field.

### 6.2 Equations solved

The background (Stage 2, $t=Hx_4$, $H=1$) has scale factors $e^{a_4}$ for 3-space and $e^{-a_4}$ for the extra times (the constant factors $s^{1/6}$ dropped), so $V$ is constant, with the primordial window

$$
\begin{aligned}
&a_4'(t)=\tfrac A4\Bigl(1+\tanh\tfrac{t-t_1}{\Delta}\Bigr)\Bigl(1-\tanh\tfrac{t-t_2}{\Delta}\Bigr),\qquad A\in\{1,2\},\ t_1=2,\ t_2=7,\ \Delta=0.5,\\
&a_4(t)=\frac{A\Delta\,\bigl[\ell\bigl(2(t-t_1)/\Delta\bigr)-\ell\bigl(2(t-t_2)/\Delta\bigr)\bigr]}{2\bigl(1-e^{-2(t_2-t_1)/\Delta}\bigr)},\qquad \ell(x)=\ln(1+e^x).
\end{aligned}
$$

In the sector without 3-space and extra-time momentum, a hidden-space plane wave in the proper hidden coordinate $\zeta=\ln(\sin z)/(6H)$ reduces the Dirac equation exactly (verified in Stage 2 and again symbolically in the Mathematica notebook) to

$$
\Psi=e^{-3H\zeta}e^{iK\zeta}u(t):\qquad \gamma^4\dot u=(M_{\mathrm{eff}}-iK\gamma^0)\,u\quad\Longleftrightarrow\quad i\dot u=hu,\qquad h=-iM_{\mathrm{eff}}\gamma^4-K\gamma^4\gamma^0 .
$$

CVODE integrates the 32 real components of $u$ (state layout: re $u_0,\dots,u_{15}$, then im $u_0,\dots,u_{15}$). With the fixed density factor $S_0$ and $M_{\mathrm{eff}}=m+\lambda S$, $S=S_0s(u)$:

$$
\begin{aligned}
&\rho=S_0\,u^\dagger hu-\tfrac\lambda2S^2,\qquad p_j=S_0\,p_j(u)+\tfrac\lambda2S^2,\qquad \bar p=\tfrac17\sum_{j\in T}p_j,\qquad w=\bar p/\rho,\\
&\mathrm{KE}_L=\tfrac12S_0\,u^\dagger hu,\quad \mathrm{PE}_L=\rho-\mathrm{KE}_L,\quad \mathrm{KE}_H=S_0\sum_jp_j(u),\quad \mathrm{PE}_H=mS+\tfrac\lambda2S^2 .
\end{aligned}
$$

For constant $M_{\mathrm{eff}}$, $h$ is constant with $h^2=E^2$, $E=\sqrt{M_{\mathrm{eff}}^2+K^2}$, and the exact solution is $u(t)=(\cos Et-i\sin Et\,h/E)\,u_0$. The source that 8D Einstein gravity $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ would need is

$$
\begin{aligned}
&\rho_{\mathrm{req}}=-\frac{3H^2(7+a_4'^2)}{\kappa},\qquad p_{\mathrm{req},0}=-\frac{3H^2(a_4'^2-5)}{\kappa},\\
&p_{\mathrm{req},1..3}=\frac{H^2(15-3a_4'^2+a_4'')}{\kappa},\qquad p_{\mathrm{req},5..7}=\frac{H^2(15-3a_4'^2-a_4'')}{\kappa}.
\end{aligned}
$$

### 6.3 Initial data and parameters

$H=m=\kappa=1$; $t\in[0,10]$ with 200 output intervals (201 samples); hidden momenta $K\in\{0,0.5,2\}$; $S_0=1$. Four initial spinors per $(A,K)$: joint eigenvectors of $h$ and $B$ with (energy, Krein) signs $(+,+)$, $(+,-)$ and $(-,+)$, and a generic normalised mixture of both energy signs. One extra run per profile has $\lambda=0.5$, $K=0.5$: its initial state is the positive-energy eigenvector of the self-consistent mass $M_\ast=1+\lambda S_0M_\ast/\sqrt{M_\ast^2+K^2}$, $M_\ast=1.47348266406420$. In total 26 runs.

### 6.4 Solver settings and statistics

BDF + Newton + dense linear solver, rtol $10^{-12}$, atol $10^{-14}$, max_step 0.02: 33866 steps and 34950 right-hand-side evaluations over the 26 runs. At rtol $10^{-10}$ the norm and energy drifts were about $4\times10^{-8}$, above the a priori conservation limit $10^{-8}$; the tolerance was tightened rather than the limit relaxed.

### 6.5 Results

![EXP-1 observables. (a) energy density, (b) mean transverse pressure, (c) Lagrangian split, (d) equation of state $w=\bar p/\rho$, (e) and (f) drifts of $\rho$ and of the Hilbert and Krein norms over all 26 runs. Profile $A=1$ is shown; $A=2$ is bit-identical.](artifacts/dirac16complex/numerics/figures/exp1_frozen_observables.png)

- **Frozen observables.** $\rho=S_0u^\dagger hu$ is constant for every initial spinor (maximum drift $4.19\times10^{-9}$), because $h$ is constant and Hermitian. The pressures and $S$ are constant for energy eigenstates (drift $2.64\times10^{-9}$). For the mixed state with $K\ne0$ the hidden-space pressure $p_0$ and $S$ oscillate at frequency $2E$ (interference of the $+E$ and $-E$ sectors, a Zitterbewegung): the range of $p_0$ is 0.803 for $K=2$ and 0.341 for $K=0.5$, and the checker's exact solution reproduces the range to $3.7\times10^{-10}$.
- **Eigenmode laws.** For $K=0$: $\rho=1$, $p=0$, $w=0$, $\mathrm{KE}_L=\mathrm{PE}_L=0.5$ (dust). For $K=0.5$: $\rho=E=1.1180$, $p_0=K^2/E=0.2236$, $w=K^2/(7E^2)=0.02857$. For $K=2$: $\rho=2.2361$, $p_0=1.7889$, $w=0.11429$. In the Lagrangian split every free eigenmode has $\mathrm{KE}_L=\mathrm{PE}_L$ ($w_L=0$) whatever $K$ is; the actual mean pressure is the hidden-space momentum flux.
- **Repulsive interaction.** The $\lambda=0.5$ run has $\rho=1.3318$, $\bar p=0.2471$, $w=0.1856$, $\mathrm{KE}_L=0.7780$ and $\mathrm{PE}_L=0.5538$; the six pressures $p_1,\dots,p_7$ equal $\tfrac\lambda2S^2=0.2242$. $M_{\mathrm{eff}}$ stays at $M_\ast$ to $1.3\times10^{-9}$.
- **Profile independence.** $a_4$ enters $h$ only through $k_j/h_j$ with $k_j=0$, so the $A=1$ and $A=2$ spinors are bit-identical (difference 0.0): no spurious $a_4$ coupling exists.
- **Negative-energy states.** The $(-,+)$ runs have $\rho=-E$ in this c-number reading; physically an antiparticle is a hole in such a mode and carries $+E$ (EXP-4). They are integrated as controls.

![EXP-1 background and Einstein requirement. (a) the window $a_4'(t)$, (b) the 3-space factor $e^{a_4}$, the extra-time factor $e^{-a_4}$ and the constant 7-volume, (c) $\rho_{\mathrm{req}}$ for both profiles beside the energy density of the free $K=0$ field, (d) $w_{\mathrm{req}}=\bar p_{\mathrm{req}}/\rho_{\mathrm{req}}$.](artifacts/dirac16complex/numerics/figures/exp1_einstein_requirement.png)

- **The required source has negative energy.** $\rho_{\mathrm{req}}$ lies in $[-24.0,-21.0]$ for $A=1$ and in $[-33.0,-21.0]$ for $A=2$; its maximum is $-21.000000000113<0$. The ratio $w_{\mathrm{req}}$ lies in $[-0.714,-0.500]$ for $A=1$ and in $[-0.714,-0.091]$ for $A=2$. It is negative because $\rho_{\mathrm{req}}<0$ while the mean required pressure is positive (all seven required pressures equal 15 where $a_4'=a_4''=0$), not because the pressure is negative. $a_4$ reaches 5.0 ($A=1$) and 10.0 ($A=2$), so 3-space grows by $e^5$ and $e^{10}$ while $V/V_0-1$ stays at $6.7\times10^{-16}$.

### 6.6 Verification

The Rust program passes 10 of 10 self-checks and the EXP-1 checker 25 of 25. The checker recomputes the background, integrating $a_4'$ by its own quadrature ($1.1\times10^{-14}$); recomputes every derived column from the raw spinor ($8.9\times10^{-16}$); evaluates a five-point finite-difference residual of $i\dot u=hu$ and of the literal reduced equation (worst ratio to the truncation bound 0.63) and of the kinetic term from the time derivative (0.31); compares with the exact propagator (maximum error $6.25\times10^{-9}$, limit $10^{-7}$); and checks the frozen quantities, the eigenmode laws ($1.9\times10^{-9}$), the norms (drift $2.70\times10^{-9}$), the self-consistent mass, the profile independence, repeat-run byte identity, and refined convergence (every run's exact error strictly improved; largest refined-minus-canonical difference $6.13\times10^{-9}$). The Mathematica notebook derives the reduction symbolically, reproduces the Stage-2 Einstein tensor, re-integrates all 26 runs with an order-8 explicit Runge-Kutta NDSolve (maximum state deviation from Rust $2.92\times10^{-9}$; its own exact error $4.3\times10^{-14}$ against Rust's $6.25\times10^{-9}$) and passes a 9-point finite-difference residual test ($1.04\times10^{-10}$ relative over 5018 resolved rows) whose negative control with a flipped mass sign fails as it should (1.19).

![Mathematica cross-check of the mixed state with $K=2$: $\rho$ frozen and $p_0$ oscillating at $2E$; dots are the Rust CSV samples, lines the independent NDSolve solution.](artifacts/dirac16complex/numerics/figures/mathematica/exp1_mixed_state_rho_p0.png)

![Mathematica cross-check of the Einstein requirement $\rho_{\mathrm{req}}=-G^4{}_4/\kappa$ computed from the metric: always negative.](artifacts/dirac16complex/numerics/figures/mathematica/exp1_einstein_requirement.png)

### 6.7 Physical interpretation

In the primordial field the 7-volume is constant, so the dilution law $S\propto1/V$ freezes the condensate: energy density and pressure do not change at all while 3-space inflates by up to $e^{10}$. Only interference between energy signs makes pressures oscillate. The frozen field's own equation of state is dust ($K=0$) or slightly stiff ($K\ne0$, or $\lambda>0$); none of these states has negative pressure. The geometry itself would need a source of negative energy density in 8D Einstein gravity, which positive-energy dirac16complex states cannot supply (Stage 2 found an exact source only for linear $a_4$, and it too has negative energy). The frozen density matters for dark energy only as a dilution effect seen from 3-space (Section 12.3).

## 7. EXP-2: self-consistent 8-dimensional Einstein cosmology

### 7.1 Purpose

EXP-2 couples the condensate to 8-dimensional Einstein gravity with the hidden space, 3-space and extra times free, and asks how $\rho$, $p$ and the anisotropy evolve, whether the extra times keep deflating, and what a 3-space observer would infer.

### 7.2 Equations solved

$\kappa=\kappa_8=1$, $ds^2=-dt^2+b^2dx_0^2+a^2(dx_1^2+dx_2^2+dx_3^2)-c^2(dx_5^2+dx_6^2+dx_7^2)$, $V=ba^3c^3$. The mixed Einstein tensor gives

$$
\begin{aligned}
&\text{constraint:}\quad \sum_{i<j}H_iH_j=3H_bH_a+3H_bH_c+3H_a^2+3H_c^2+9H_aH_c=\kappa\rho,\\
&\text{evolution:}\quad \dot H_i=-H_i\Theta+\tfrac{\kappa}{6}(\rho-p),\qquad \dot h_i=H_ih_i\qquad(\tfrac16=\tfrac1{D-2},\ D=8),\\
&\text{matter:}\quad i\dot u=hu,\ \ h=-iM_{\mathrm{eff}}\gamma^4,\ \ S=S_0\frac{V_0}{V}s(u),\ \ \rho=mS+\tfrac\lambda2S^2,\ \ p=\tfrac\lambda2S^2 .
\end{aligned}
$$

CVODE integrates 38 reals: $\ln b$, $\ln a$, $\ln c$, $H_b$, $H_a$, $H_c$ and the 32 components of $u$. Also recorded: $w=p/\rho$, $\mathrm{KE}_L=\tfrac12SM_{\mathrm{eff}}$, $\mathrm{PE}_L=\tfrac12mS$, the bound $\Theta^2-3H_a^2-2\kappa\rho$ (equal to $H_b^2+3H_c^2\ge0$ on the constraint surface) and the dilution-inferred 3-space equation of state

$$
w_{\mathrm{eff}}=-1+\frac{\Theta}{3H_a}(1+w),
$$

which is what an observer who assumes $\rho\propto a^{-3(1+w_{\mathrm{eff}})}$ in 3-space would infer. It is a dilution measure, not the deceleration of 3-space.

**Exact solution** (derived in the study and re-derived by the checker). Because $\rho-p=mS$ does not depend on $\lambda$ and $SV$ is constant, $\ddot V=\tfrac76\kappa mS_0$ and $(H_iV)^{\cdot}=\beta=\kappa mS_0/6$: $V(t)=1+\Theta_0t+\alpha t^2$ with $\alpha=7\beta/2$, $H_i=(H_{i0}+\beta t)/V$ and $u(t)=e^{-i\int M_{\mathrm{eff}}dt}u_0$. Backward in time $V\to0$ linearly at the Kasner-type singularity $t_s=-2/(\Theta_0+\sqrt D)$, $D=\Theta_0^2-4\alpha$, with exponents $p_i=(H_{i0}+\beta t_s)/\sqrt D$, $\sum p_i=1$ and $\sum p_i^2=1-2\kappa mx_0S_0/D$. Late times: $H_it\to2/7$ (isotropic 8D dust) and $w_{\mathrm{eff}}\to4/3$. The Rust code uses this closed form only for self-checks and to place the output times; CVODE integrates the full system.

### 7.3 Initial data and parameters

$m=1$; $H_b=0$, $H_a=1$, $H_c=-0.2$ (extra times initially deflating), $\ln b=\ln a=\ln c=0$; $u(0)$ is the first vector of the joint $(h=+M_{\mathrm{eff}},B=+1)$ eigenspace. The constraint left-hand side is $C_0=1.32$ and fixes $S_0=C_0/(1+x_0)$, with $\lambda=2mx_0/S_0$, $\rho(0)=1.32$ and $M_{\mathrm{eff}}(0)=m(1+2x_0)=1$, 0.2 and 2 for the three runs:

| Run | $S_0$, $\lambda$ | $\alpha$, $\beta$ | $t_s$ |
| --- | --- | --- | --- |
| $x_0=0$ (dust) | 1.32, 0 | 0.77, 0.22 | $-0.4954$ |
| $x_0=-0.4$ (attractive) | 2.2, $-0.3636$ | 1.2833, 0.3667 | $-0.6266$ |
| $x_0=+0.5$ (repulsive) | 0.88, 1.1364 | 0.5133, 0.1467 | $-0.4624$ |

The output grid is uniform in $\ln V$ with step 0.05 on $[-7,18.5]$ (140 backward and 370 forward intervals, 511 rows). Backward the run stops at $V/V_0=e^{-7}$, about $10^{-3}$ in $t$ above $t_s$; forward it ends at $V/V_0=e^{18.5}$, $t_{\mathrm{end}}=11855.5$, 9183.5 and 14519.6.

### 7.4 Solver settings and statistics

Adams + fixed point, rtol $10^{-12}$, atol $10^{-15}$, max_step 0.02: 1779784 steps and 1781396 right-hand-side evaluations. The step cap is needed: without it Adams takes steps of about 0.045 and accumulates an amplitude error of about $5\times10^{-13}$ per step on the oscillating spinor, which drifts $s(u)$ by $1.7\times10^{-7}$ over $t\sim10^4$ and pushes the constraint residual to $3\times10^{-8}$.

### 7.5 Results

![EXP-2 Hubble rates of the hidden space, 3-space and the extra times against $t-t_s$ (top, symmetric log scale), and $H_i(t-t_s)$ with the Kasner exponents dotted and the 8D dust value $2/7$ dashed (bottom), for the three runs.](artifacts/dirac16complex/numerics/figures/exp2_hubble.png)

- **Isotropisation.** The anisotropy $(H_i-H_j)V$ is conserved (drift $6.2\times10^{-10}$), so it decays as $1/V$. At the forward end the relative anisotropy $7\max|H_i-H_j|/\Theta$ is $4.6\times10^{-4}$, $3.6\times10^{-4}$ and $5.6\times10^{-4}$, $H_it$ approaches $2/7=0.2857$, and $w_{\mathrm{eff}}=1.33275$, 1.33288 and 1.33261 approaches $4/3$.
- **The extra times turn from deflation to expansion** at $t=0.2/\beta=0.9091$, 0.5455 and 1.3636 (measured on the output grid: 0.9095, 0.5457, 1.3639). Nothing in this dynamics keeps them deflating.
- **Kasner singularity.** The exponents $(p_b,p_a,p_c)$ are $(-0.066576,0.544271,-0.188746)$ with $\sum p_i^2=1$ (vacuum Kasner) for $x_0=0$; $(-0.290250,0.972978,-0.542895)$ with $\sum p_i^2=3.80851$ for $x_0=-0.4$; and $(-0.035225,0.484182,-0.139107)$ with $\sum p_i^2=0.76259$ for $x_0=+0.5$. The $\lambda S^2/2$ term is a stiff ($w=1$) component near the singularity. Extrapolating the CVODE solution to $V=0$ reproduces them to $2.9\times10^{-7}$.

![EXP-2 (a) the 7-volume against $t-t_s$ with the exact quadratic, (b) energy density and pressure against $V/V_0$ (symmetric log scale), (c) conservation of $SV$.](artifacts/dirac16complex/numerics/figures/exp2_volume_density.png)

![EXP-2 (a) $w=p/\rho$ and (b) the dilution-inferred $w_{\mathrm{eff}}$ against $\ln V$, with the lines $4/3$, $-1+1/\sqrt3$ and $-1$, and (c) the relative Hamiltonian constraint residual with the limit $10^{-9}$.](artifacts/dirac16complex/numerics/figures/exp2_eos_constraint.png)

- **Equation of state.** The dust run keeps $w=0$. The repulsive run is stiff near the singularity ($w\to1$) and dust at late times. The attractive run is dust at late times; backward it becomes phantom ($w<-1$ with $\rho>0$, equivalently $\mathrm{KE}_L<0$ and $M_{\mathrm{eff}}<0$) for $0.4<V/V_0<0.8$ (14 output rows, measured volume range 0.407 to 0.779) and has negative energy density for $V/V_0<0.4$ (122 rows), down to $\rho=-1.06\times10^{6}$ at $V=e^{-7}$. The rows with $w<-1$ and $\rho>0$ are exactly the rows with $\mathrm{KE}_L<0$.
- **The 8D energy bound.** On the constraint surface $\Theta^2-3H_a^2-2\kappa\rho=H_b^2+3H_c^2\ge0$, so wherever $\rho\ge0$, $\Theta\ge\sqrt3H_a$ and $w_{\mathrm{eff}}\ge-1+(1+w)/\sqrt3$. For dust the minimum measured $w_{\mathrm{eff}}$ is $-0.38732>-1+1/\sqrt3=-0.42265$, and the minimum of $\Theta/(3H_a)$ over rows with $\rho>0$ is 0.61268. The bound fails only where $\rho<0$: over all rows of the attractive run $\Theta/(3H_a)$ falls to 0.344, while the bound itself stays non-negative (minimum $1.5\times10^{-9}$).

### 7.6 Verification

The Rust program passes 15 of 15 self-checks and the EXP-2 checker 34 of 34. Relative constraint residual at most $1.26\times10^{-10}$ (limit $10^{-9}$); $|SV/(S_0V_0)-1|$ at most $4.03\times10^{-10}$; exact volume at most $1.0\times10^{-10}$; finite-difference residuals of continuity $2.1\times10^{-10}$, of the Einstein evolution $5.1\times10^{-11}$ and of the Dirac equation $2.6\times10^{-8}$ (559 rows); an Einstein tensor computed from the metric agrees to $1.1\times10^{-10}$. The spinor needs care: its shape error (phase invariant) is $2.0\times10^{-10}$, and its phase error of $2.24\times10^{-7}$ at $t\sim10^4$ stays below the bound $\max|M_{\mathrm{eff}}|N_{\mathrm{steps}}\,\mathrm{ulp}(t_{\mathrm{end}})/2=1.32\times10^{-6}$. This phase error is the rounding of CVODE's internal time $t_n\mathrel{+}=h$ with the capped step, not truncation: it does not shrink in the refined run ($2.71\times10^{-7}$), while the shape error shrinks to $5.2\times10^{-11}$ and the gravity error from $1.6\times10^{-11}$ to $3.5\times10^{-12}$. The checker confirms the cause: the per-binade drift rates match an exact rational-arithmetic prediction to 1.7% over 21 binades. Repeat-run byte identity holds.

The Mathematica notebook derives the constraint and the evolution equations from the metric and verifies that the closed form solves and propagates them. NDSolve agrees with Rust to $3.16\times10^{-8}$ in $\ln h_i$ and $3.24\times10^{-8}$ in $H_i/\Theta$. These largest deviations sit at the backward end, where the problem is ill-conditioned; divided by the amplification factor $1+|t_s|/(t-t_s)$ (the measure of the Rust self-check) Rust's error against the closed form is $1.1\times10^{-11}$; NDSolve's own error against the closed form is $2.7\times10^{-11}$ in $\ln h_i$, so the raw deviation is on the Rust side. The spinor agrees to $1.08\times10^{-7}$ raw and $4.2\times10^{-10}$ after phase alignment, and the Mathematica exact-spinor calculation reproduces Rust's own maximum exact-spinor error to $8\times10^{-17}$.

![Mathematica cross-check of the dust run: $H_i/\Theta$ from the Kasner-type singularity to isotropic 8D dust ($1/7$); dots Rust, lines NDSolve.](artifacts/dirac16complex/numerics/figures/mathematica/exp2_anisotropy_fractions.png)

### 7.7 Physical interpretation

In a self-consistent 8D cosmology the condensate's energy density falls as $1/V$ and its pressure as $1/V^2$, so every run ends as isotropic 8D dust whatever $\lambda$ is. $\lambda$ only matters near the singularity: repulsion makes the matter stiff, attraction makes it phantom and then negative. Two conclusions matter for the dark sector. First, the extra times do not stay deflating: 8D gravity with this matter drives all seven directions to the same expansion, and a 3-space observer then sees the dust dilute like $a^{-7}$ ($w_{\mathrm{eff}}\to4/3$), not like $a^{-3}$. Dust-like behaviour in 3-space therefore requires stabilised extra dimensions, which EXP-3 and EXP-4 assume and nothing here provides. Second, with non-negative energy density a 3-space observer can never infer $w_{\mathrm{eff}}<-1+(1+w)/\sqrt3$; for dust that is $-0.42265$. Apparent dark-energy-like dilution close to $w_{\mathrm{eff}}=-1$ needs negative 8D energy density.

## 8. EXP-3: the condensate as late-time dark energy

### 8.1 Purpose

EXP-3 assumes stabilised extra dimensions ($b$, $c$ constant) and a 4-dimensional effective Friedmann equation, and asks whether an attractive condensate can be the dark energy measured by Unite.

### 8.2 Equations solved

With $N=\ln a$ ($a=1$ today), $\sigma=S/S_0$ and $A=\Omega_\psi/(1+x_0)$:

$$
\begin{aligned}
&E^2=\frac{H^2}{H_0^2}=\Omega_ra^{-4}+\Omega_ma^{-3}+\rho_\psi,\qquad \rho_\psi=A\,\sigma(1+x_0\sigma),\qquad p_\psi=A\,x_0\sigma^2,\qquad w=\frac{x_0\sigma}{1+x_0\sigma},\\
&\mathrm{KE}_L=\frac{\Omega_\psi}{2}\,\frac{\sigma(1+2x_0\sigma)}{1+x_0},\qquad \mathrm{PE}_L=\frac{\Omega_\psi}{2}\,\frac{\sigma}{1+x_0},\qquad \mathrm{KE}_H=0,\qquad \mathrm{PE}_H=\rho_\psi .
\end{aligned}
$$

The condensate is obtained from the evolving spinor, not assumed: $\sigma=a^{-3}s(u)/s(u_0)$. The ODE state (35 reals, independent variable $N$) is

$$
\begin{aligned}
&\frac{d(H_0t)}{dN}=\frac1E,\qquad \frac{dD_C}{dN}=-\frac{1}{aE},\qquad \frac{du}{dN}=-i\,\frac{M_{\mathrm{eff}}}{H_0}\,\frac{(-i\gamma^4)u}{E},\qquad \frac{M_{\mathrm{eff}}}{H_0}=\mu\,\frac{1+2x_0\sigma}{1+2x_0},\\
&\frac{d\ln\sigma}{dN}=-3+\frac{2\,\mathrm{Re}\bigl(u^\dagger(-i\gamma^4)\,du/dN\bigr)}{s(u)},
\end{aligned}
$$

with $D_C$ the comoving distance in units of $c/H_0$ and $\mathrm{DM}(z)=5\log_{10}((1+z)D_C)$ plus a constant. $\mu=M_{\mathrm{eff}}(a=1)/H_0\in\{3,7\}$ is a reduced frequency, used to show that $\rho$, $p$ and $w$ do not depend on the spinor phase (real fermions have $m/H_0>10^{30}$). Further diagnostics: $\rho_\psi=0$ at $a=|x_0|^{1/3}$; $w=-1$ (where $M_{\mathrm{eff}}=0$) at $a=(2|x_0|)^{1/3}$; a bounce $E^2=0$ at the root in $(0,1)$ of $(\Omega_m+A)a^3+\Omega_ra^2+Ax_0=0$; $q_{\mathrm{dec}}=(2\Omega_ra^{-4}+\Omega_ma^{-3}+\rho_\psi+3p_\psi)/(2E^2)$; the adiabatic sound speed $c_s^2=dp/d\rho=2x_0\sigma/(1+2x_0\sigma)$; and the tangent CPL parameters $w_0=w(1)=x_0/(1+x_0)$, $w_a=-dw/da|_1=3x_0/(1+x_0)^2$.

### 8.3 Initial data and parameters

$\Omega_r=0.00009$, $\Omega_m=0.305$, $\Omega_\psi=0.69491$ (flat). $x_0\in\{-0.462654,-0.433107,-0.3,-0.2,0\}$: the first reproduces $w_0=-0.861$, the second $w_0=-0.764$, and $x_0=0$ is dust. $\mu\in\{3,7\}$, so 10 runs. The initial spinor is the positive-energy rest eigenvector of $h(a=1)$ with $B=+1$. Each run is integrated from $N=0$ backward (320 intervals towards $a=1/3.5$) and forward (160 intervals to $a=2$).

**Deviation from the programme.** For every $x_0<0$ the attractive term $\rho_\psi\propto-a^{-6}$ dominates in the past and $E^2$ reaches zero at a bounce $a_b>1/3.5$. Smaller $a$ does not exist in these models, so the backward branch stops at the last grid point with $N\ge N_b+0.01$, and a check confirms that the stop sits exactly there. Only the dust model reaches $a=1/3.5$.

### 8.4 Solver settings and statistics

Adams + fixed point, rtol $10^{-11}$, atol $10^{-13}$, max_step 0.01 in $N$: 6074 steps and 10115 right-hand-side evaluations over 20 integrations.

### 8.5 Results

| $x_0$ | $w_0$ | $w_a$ (tangent) | $c_s^2$ today |
| --- | --- | --- | --- |
| $-0.462654$ | $-0.861$ | $-4.807$ | $-12.39$ |
| $-0.433107$ | $-0.764$ | $-4.043$ | $-6.47$ |
| $-0.3$ | $-0.4286$ | $-1.837$ | $-1.50$ |
| $-0.2$ | $-0.25$ | $-0.9375$ | $-0.667$ |
| 0 | 0 | 0 | 0 |

The characteristic epochs, as redshift $z$ and scale factor $a$:

| $x_0$ | $\rho_\psi=0$ | $w=-1$ | bounce $E^2=0$ |
| --- | --- | --- | --- |
| $-0.462654$ | $z=0.293$, $a=0.773$ | $z=0.0262$, $a=0.974$ | $z=0.388$, $a=0.721$ |
| $-0.433107$ | $z=0.322$, $a=0.757$ | $z=0.0490$, $a=0.953$ | $z=0.423$, $a=0.703$ |
| $-0.3$ | $z=0.494$, $a=0.669$ | $z=0.186$, $a=0.843$ | $z=0.633$, $a=0.612$ |
| $-0.2$ | $z=0.710$, $a=0.585$ | $z=0.357$, $a=0.737$ | $z=0.890$, $a=0.529$ |
| 0 | none | none | none |

The deceleration and the bare masses of the two runs per coupling:

| $x_0$ | $q_{\mathrm{dec}}$ today | $q_{\mathrm{dec}}=0$ at | $m/H_0$ ($\mu=3$, 7) |
| --- | --- | --- | --- |
| $-0.462654$ | $-0.397$ | $z=-0.126$, $a=1.144$ | 40.2, 93.7 |
| $-0.433107$ | $-0.296$ | $z=-0.103$, $a=1.115$ | 22.4, 52.3 |
| $-0.3$ | 0.0533 | $z=0.0290$, $a=0.972$ | 7.5, 17.5 |
| $-0.2$ | 0.239 | $z=0.191$, $a=0.840$ | 5.0, 11.7 |
| 0 | 0.500 | none | 3, 7 |

![EXP-3 $w(a)=p_\psi/\rho_\psi$ of the condensate for the five couplings, with the Unite CPL line $w_0=-0.861$, $w_a=-0.60$ and the Unite constant $w=-0.764$. The shaded band around $-0.764$ ($\pm0.118$) is only an approximate one-sigma band inferred from the PDF's statement "roughly two standard deviations from $-1$"; the PDF gives no error bars for $(w_0,w_a)$, so none is drawn for the CPL line. The curves have a pole where $\rho_\psi=0$ and end at the bounce.](artifacts/dirac16complex/numerics/figures/exp3_w_of_a.png)

![EXP-3 (a) the condensate energy density $\rho_\psi(a)$, which changes sign at $a=\lvert x_0\rvert^{1/3}$ (circles), and (b) $E^2=H^2/H_0^2$, which reaches zero at the bounce for every attractive model (triangles: last point before the bounce).](artifacts/dirac16complex/numerics/figures/exp3_rho_psi.png)

![EXP-3 Lagrangian split: $\mathrm{KE}_L$ (solid) turns negative, and $w$ drops below $-1$, for $a<(2\lvert x_0\rvert)^{1/3}$; $\mathrm{PE}_L$ (dashed) stays positive.](artifacts/dirac16complex/numerics/figures/exp3_ke_pe.png)

- **The changing equation of state.** For $x_0<0$, $w$ rises with time (thawing, $w_a<0$): it comes up from $-\infty$ at the pole where $\rho_\psi=0$, crosses $-1$ where $M_{\mathrm{eff}}=0$ ($\mathrm{KE}_L=0$), passes $w_0$ today and tends to 0 in the future, because $p_\psi\propto a^{-6}$ dies away faster than $\rho_\psi$. Energy density and pressure change for one reason only: $\sigma=a^{-3}$.
- **Acceleration.** The two Unite-tuned models accelerate today ($q_{\mathrm{dec}}=-0.397$ and $-0.296$) and all the way back to the bounce, and they start to decelerate again at $a=1.144$ and 1.115 when the condensate becomes dust-like. Neither has a matter-dominated era. The weaker couplings decelerate today and accelerate only in the past, near the bounce.
- **Phase independence.** $\mu=3$ and $\mu=7$ give the same $\rho$ ($1.74\times10^{-9}$), $p$ ($3.00\times10^{-9}$) and $w$ ($2.77\times10^{-9}$, condition-scaled): only $s(u)=1$ matters, not the phase.
- **Sound speed.** $c_s^2=dp/d\rho$ is negative today for every $x_0<0$ ($-12.39$ for the Unite-tuned model). In a fluid description that is a gradient instability of perturbations; perturbations themselves were not computed.

![EXP-3 distance modulus minus that of the Unite CPL model ($\Omega_m=0.305$ fixed) for the five couplings, a constant $w=-0.764$ and $\Lambda$CDM: (a) same $H_0$, curves ending at the bounce; (b) with the mean offset over each curve's redshift range removed ($H_0$ and absolute magnitude free).](artifacts/dirac16complex/numerics/figures/exp3_distance_modulus.png)

![EXP-3 $(w_0,w_a)$ plane. (a) the tangent CPL parameters of the condensate for $x_0\in[-0.49,0]$ with the canonical couplings, the Unite point, $\Lambda$CDM, the line $w_0+w_a=-1$ and the distance-inferred point of the deflation variant; (b) the supplementary restricted fits of the fine scan, far from Unite for every $x_0<0$.](artifacts/dirac16complex/numerics/figures/exp3_w0wa_plane.png)

The fits and the comparison with Unite are tabulated in Section 12.4.

### 8.6 Verification

The Rust program passes 14 of 14 self-checks, the EXP-3 checker 31 of 31 and the analysis 9 of 9 (Nelder-Mead recovers synthetic CPL and constant-$w$ curves to $2.0\times10^{-12}$ and $1.4\times10^{-12}$; Rust distances match an independent quadrature to $1.7\times10^{-9}$). $\sigma$ from the spinor agrees with $a^{-3}$ to $2.50\times10^{-9}$ (refined: $2.10\times10^{-10}$) and $\exp(\ln\sigma)$ to $1.95\times10^{-14}$. The time and distance agree with independent quadratures to $1.11\times10^{-9}$ and $1.75\times10^{-9}$, the spinor with its exact phase to $5.48\times10^{-8}$ (refined $6.41\times10^{-9}$). The roots are reproduced to $2.6\times10^{-9}$ ($\rho_\psi=0$), $2.3\times10^{-9}$ ($w=-1$) and $1.5\times10^{-9}$ ($q_{\mathrm{dec}}=0$), the tangent $w_a$ to $2.8\times10^{-7}$ relative, and the bounce stop to $1.5\times10^{-15}$. The Mathematica notebook derives the Friedmann constraint, the continuity equation, $w$ and $q_{\mathrm{dec}}$ symbolically; NDSolve agrees to $2.12\times10^{-8}$ in the spinor ($1.25\times10^{-9}$ phase aligned) and to $1.95\times10^{-14}$ in $\ln\sigma$, and its exact spinor error is $2.0\times10^{-12}$. The finite-difference negative control with a flipped mass sign fails as it should (2.0). The 4D-effective Friedmann equation with stabilised extra dimensions is an assumption of this experiment, not a consequence of the 8D equations; the Mathematica notebook states this too.

![Mathematica cross-check of $w(a)$: dots Rust CSV, lines NDSolve, with the Unite CPL line for reference; clipped to $[-3,1]$.](artifacts/dirac16complex/numerics/figures/mathematica/exp3_equation_of_state.png)

### 8.7 Physical interpretation

The attractive condensate is the only object in this framework whose own pressure is negative. Its negative pressure is $\tfrac\lambda2S^2\propto a^{-6}$, so it matters only at high density, that is in the past, and there it wins over the positive $mS$: going back in time the energy density turns negative and $H$ reaches zero. Today's $w_0$ can be tuned to any value in $(-1,0)$ and to the phantom side by the single parameter $x_0$, but $w_a=3x_0/(1+x_0)^2$ is then fixed, and the evolution is fast because the negative-pressure part dilutes like $a^{-6}$. The crossing of $w=-1$ is not the smooth crossing of a non-canonical scalar: it happens where the effective mass passes through zero, just before the energy density does.

## 9. EXP-4: dirac16complex quanta as dark matter

### 9.1 Purpose

EXP-4 assumes a 3-space FRW universe with the hidden space and the extra times static ($b=c=1$) and asks two things: how the equation of state of a thermal gas of quanta changes from relativistic to non-relativistic, and how many quanta the end of inflation creates.

### 9.2 Equations solved

A mode with comoving momentum $k$ along $x_1$ and physical momentum $K=k/a$ obeys

$$
i\dot u=h(t)u,\qquad h=-im\gamma^4-K\gamma^4\gamma^1,\qquad h^2=E^2,\qquad E=\sqrt{m^2+K^2},\qquad \dot K=-KH .
$$

Per mode $\varepsilon=u^\dagger hu$, $p_1=-K\,u^\dagger\gamma^4\gamma^1u$, $s=u^\dagger(-i\gamma^4)u$, with the identity $\varepsilon=ms+p_1$; $|\beta_k|^2=|P_-u|^2/|u|^2$ is the weight on the instantaneous negative-energy subspace. Structure used for the counting and verified numerically: $h=(m\sigma_z+K\sigma_x)\otimes I_8$ with $\sigma_z=-i\gamma^4$ and $\sigma_x=-\gamma^4\gamma^1$, so there are 8 spin states per $k$, and $Ch^\ast C=-h$ maps particles to antiparticles.

**(a) Thermal gas.** $a(t)=(t/t_i)^{1/2}$ with $t_i=1/(2H_i)$, and with $W_n=\tfrac{16}{2\pi^2}w_nk_n^2f_n$, $f=1/(e^{E_i/T_i}+1)$ and 16 states per $k$ (8 particles and 8 antiparticles):

$$
\rho=\frac{1}{a^3}\sum_nW_n\varepsilon_n,\qquad p=\frac{1}{3a^3}\sum_nW_np_{1,n},\qquad \mathrm{KE}_H=3p,\qquad \mathrm{PE}_H=\rho-3p,
$$

compared with the kinetic-theory integrals

$$
\rho_{\mathrm{kin}}=\frac{16}{2\pi^2a^3}\int k^2f\,E\,dk,\qquad p_{\mathrm{kin}}=\frac{16}{2\pi^2a^3}\int k^2f\,\frac{K^2}{3E}\,dk .
$$

**(b) Pair creation.** $a=e^{H_{\mathrm{inf}}t}$ for $t<0$, glued $C^1$ at $t=0$ to $a=(1+2H_{\mathrm{inf}}t)^{1/2}$: $a$ and $H$ are continuous and $\dot H$ jumps from 0 to $-2H_{\mathrm{inf}}^2$. The integration is restarted at $t=0$. Each mode starts in the first-order adiabatic vacuum at $k/a(t_0)=200H_{\mathrm{inf}}$. With 8 filled negative-energy states per $k$ in the Dirac sea, each ending with weight $|\beta_k|^2$ on the positive-energy subspace,

$$
na^3=\frac{16}{2\pi^2}\int k^2|\beta_k|^2dk,\qquad \rho a^3=\frac{16}{2\pi^2}\int k^2|\beta_k|^2E_k(a)\,dk,\qquad pa^3=\frac{16}{2\pi^2}\int k^2|\beta_k|^2\frac{K^2}{3E}\,dk,
$$

counting particles and antiparticles. For large $k$ the kink at $t=0$ predicts $|\beta_k|^2\to(mk/(4E^4))^2$ at $a=1$.

### 9.3 Initial data and parameters

**(a)** $m=1$, comoving temperature $T_i=10$ at $a=1$, $H_i=0.05$, $t_i=10$, $a$ from 1 to 100 ($t_{\mathrm{end}}=10^5$), 60 output intervals uniform in $\ln a$; 48 Gauss-Legendre nodes on $[0,k_{\max}]$, $k_{\max}=12T_i=120$. Each mode starts from the positive-energy $B=+1$ eigenvector of $h(t_i)$. Extras: a second spin state for four nodes, a negative-energy mode for one node, and the first-order adiabatic vacuum for two trans-relativistic nodes. **(b)** $H_{\mathrm{inf}}=1$, $m/H_{\mathrm{inf}}\in\{0,0.1,0.5,1,2\}$, 64 Gauss-Legendre nodes in $\ln k$ on $[10^{-3},40]$; the run ends when $H=10^{-4}m$ ($a_{\mathrm{end}}^2=10^4H_{\mathrm{inf}}/m$; for $m=0$ the $m=0.1$ value); antiparticle runs for three nodes at $m=1$.

### 9.4 Solver settings and statistics

Adams + fixed point, rtol $10^{-13}$, atol $10^{-14}$, max_step 2.0; 287898778 steps and 435564940 right-hand-side evaluations. Adams was selected by a recorded test at the default tolerances against a reference run at rtol/10: for node 2 ($k=0.9525$) Adams had error $1.25\times10^{-12}$ with 1370 evaluations against BDF's $2.27\times10^{-10}$ with 4730 (plus 2464 for the Jacobian); for node 47 ($k=119.93$) $1.71\times10^{-9}$ with 88979 against $1.84\times10^{-8}$ with 313247 (plus 164384). The tolerance is tight because each thermal mode turns through about $10^5$ radians: $\max|u^\dagger u-1|$ is $2.4\times10^{-4}$ at rtol $10^{-10}$ and $2.4\times10^{-7}$ at $10^{-13}$.

### 9.5 Results

![EXP-4 thermal gas. (a) $w=p/\rho$ of the CVODE mode sum and of kinetic theory against $a$, from $1/3$ towards 0; (b) relative deviations of $\rho$ (about $10^{-8}$) and of $p$ (up to $1.9\times10^{-5}$, the sudden-start free wave) from kinetic theory.](artifacts/dirac16complex/numerics/figures/exp4_thermal_w.png)

![EXP-4 thermal gas scaling: (a) $\rho a^4$, constant while the gas is relativistic, and (b) $\rho a^3$, constant once it is non-relativistic.](artifacts/dirac16complex/numerics/figures/exp4_thermal_scaling.png)

![EXP-4 kinetic and potential energy of the gas: $\mathrm{KE}_H/\rho=3w$ (momentum energy) falls from 1 and $\mathrm{PE}_H/\rho$ (rest mass) rises towards 1, while the Lagrangian split stays at $\mathrm{KE}_L/\rho=\mathrm{PE}_L/\rho=1/2$.](artifacts/dirac16complex/numerics/figures/exp4_thermal_split.png)

- **Relativistic to dust.** $w=0.3328543348$ at $a=1$ (kinetic theory: the same to ten digits) and $w=0.0359224$ at $a=100$ (kinetic theory 0.0359223). $\rho a^4$ is constant early and $\rho a^3$ late. The momentum energy $\mathrm{KE}_H=3p$ gives way to rest-mass energy.
- **Agreement with kinetic theory.** $\rho$ agrees to $1.98\times10^{-8}$. $p$ deviates by up to $1.87\times10^{-5}$, independent of the tolerance: the start from the instantaneous eigenvector leaves a free negative-frequency wave that enters $p_1$ and $s$ at first order, $p_1=(1-2|\beta|^2)K^2/E+2\,\mathrm{Re}(\alpha^\ast\beta)\,mK/E$, while $\varepsilon$ has no such term. The deviation stays inside the independently predicted interference envelope (ratio 0.28), and the adiabatic-vacuum runs reduce the single-mode pressure deviation from 1.78 to 0.12 relative.
- **No spurious particle production in the gas.** The occupation-weighted $|\beta|^2$ is $3.7\times10^{-8}$ and the adiabatic-vacuum runs end at $5.6\times10^{-8}$. The largest single-mode value, $6.37\times10^{-5}$ at $k=0.953$, is 0.998 times $4|c|^2$ with $|c|^2=(mkH_i/(4E_i^3))^2$, the sudden-start wave, not particle production.
- Spin independence and particle-antiparticle symmetry are exact (deviation 0.0). Truncating the momenta at $k_{\max}$ misses $2.4\times10^{-3}$ of $\rho$ at $a=1$, which is reported, not corrected.

![EXP-4 pair creation by the de Sitter to radiation transition: $|\beta_k|^2$ at the end (first-order adiabatic basis) for $m/H_{\mathrm{inf}}=0.1$, 0.5, 1 and 2, with the kink tail $(mk/(4E^4))^2$ for $k\ge8$; for $m=0$, $|\beta_k|^2\le7.7\times10^{-25}$ (no production).](artifacts/dirac16complex/numerics/figures/exp4_pair_spectra.png)

![EXP-4 (a) the produced comoving number density $na^3$ (adiabatic basis solid, instantaneous basis dashed), and (b) the equation of state of the produced gas with its frozen spectrum, from nearly $1/3$ at $a=1$ to dust.](artifacts/dirac16complex/numerics/figures/exp4_pair_density.png)

| $m/H_{\mathrm{inf}}$ | $na^3$ in $H_{\mathrm{inf}}^3$ | $\max\lvert\beta_k\rvert^2$ | $a_{\mathrm{end}}^2$ |
| --- | --- | --- | --- |
| 0 | $1.8\times10^{-24}$ | $8.5\times10^{-25}$ | $10^5$ |
| 0.1 | $1.455\times10^{-3}$ | 0.348 | $10^5$ |
| 0.5 | $4.991\times10^{-3}$ | 0.0640 | $2\times10^4$ |
| 1 | $4.414\times10^{-3}$ | 0.0138 | $10^4$ |
| 2 | $2.422\times10^{-3}$ | 0.00265 | $5\times10^3$ |

The equation of state of the produced gas, with its final (frozen) spectrum:

| $m/H_{\mathrm{inf}}$ | $w$ at $a=1$ | $w$ at the end | $\rho a^3$ at the end |
| --- | --- | --- | --- |
| 0 | $1/3$ | $1/3$ | $1.3\times10^{-26}$ |
| 0.1 | 0.3095 | $3.09\times10^{-4}$ | $1.456\times10^{-4}$ |
| 0.5 | 0.2544 | $1.28\times10^{-4}$ | $2.496\times10^{-3}$ |
| 1 | 0.2390 | $1.70\times10^{-4}$ | $4.415\times10^{-3}$ |
| 2 | 0.2397 | $3.09\times10^{-4}$ | $4.845\times10^{-3}$ |

- **Production for $m>0$ only.** For $m=0$ the mode equation is conformally invariant, $h=K(t)\sigma_x\otimes I_8$ has time-independent eigenvectors, and the measured $|\beta|^2$ ($8.5\times10^{-25}$) is roundoff. For $m>0$ the yield $na^3$ is a few $10^{-3}H_{\mathrm{inf}}^3$, largest near $m=0.5H_{\mathrm{inf}}$; the maximum $|\beta_k|^2\le1$ respects the Pauli principle. The high-$k$ tail follows the kink prediction to 4.2% (limit 35%).
- **The produced gas becomes dust**: $w$ falls from values between 0.24 and 0.31 at $a=1$ to about $10^{-4}$ at the end, and $\rho a^3$ approaches $m\,na^3$ (for $m=1$: $4.415\times10^{-3}$ against $na^3=4.414\times10^{-3}$).

### 9.6 Verification

The Rust program passes 23 of 23 self-checks and the EXP-4 checker 51 of 51. The checker recomputes the grids, the initial states, every derived column and every mode sum from the raw spinors (to $2.5\times10^{-15}$), re-derives kinetic theory with an independent Gauss-Legendre quadrature (quadrature error $1.2\times10^{-11}$ in $\rho$), checks unitarity ($2.4\times10^{-7}$ thermal, $4.1\times10^{-8}$ pair) and the Krein norm, integrates selected modes with an independent RK4 with Richardson estimate ($1.74\times10^{-9}$ thermal, $6.2\times10^{-10}$ pair) because the CSV sampling is too sparse for finite differences, and checks repeat-run byte identity and refined convergence (thermal $\rho$ and $p$ change by $3.0\times10^{-8}$ and $3.7\times10^{-8}$ relative, unitarity improves from $2.4\times10^{-7}$ to $4.4\times10^{-8}$, pair $|\beta|^2$ changes by $1.8\times10^{-9}$ relative). The Mathematica notebook derives the mode equation symbolically, re-integrates four thermal nodes and ten pair modes with NDSolve (thermal: $2.62\times10^{-6}$ raw, $5.9\times10^{-8}$ phase aligned; NDSolve Adams against order-8 Runge-Kutta on node 2: $6.6\times10^{-9}$, so the raw deviation is on the Rust side, plausibly the same time-accumulation rounding as in EXP-2 but not proven; pair: $7.6\times10^{-9}$ phase aligned and $1.9\times10^{-9}$ relative in $|\beta|^2$, massless $|\beta|^2=0$), and recomputes kinetic theory with NIntegrate ($\rho$: $1.98\times10^{-8}$, $p$: $1.87\times10^{-5}$, the free-wave effect above).

![Mathematica cross-check of the thermal gas: $w$ of the 48-mode Rust sum (dots) against NIntegrate kinetic theory (line).](artifacts/dirac16complex/numerics/figures/mathematica/exp4_thermal_equation_of_state.png)

![Mathematica cross-check of the pair spectra for $m/H_{\mathrm{inf}}=0.5$, 1 and 2: lines Rust, dots NDSolve subset.](artifacts/dirac16complex/numerics/figures/mathematica/exp4_pair_spectrum.png)

### 9.7 Physical interpretation

In the good sector, with the extra dimensions held static, dirac16complex quanta are an ordinary gas of massive fermions with 16 states per momentum. Their pressure is momentum flux and redshifts away, so the equation of state changes continuously from radiation to dust: the gas is hot, then warm, then cold. The expansion itself creates such quanta when inflation ends, for any $m>0$, in amounts of order $10^{-3}H_{\mathrm{inf}}^3$ per comoving volume at the end of inflation, and the created gas is dust soon after. This is the behaviour a gravitationally produced, heavy, weakly coupled dark-matter candidate needs. What it does not give is a relic density in physical units: that would require $H_{\mathrm{inf}}$ and $m$ in physical units and the post-inflationary history, none of which the framework fixes.

## 10. EXP-5: the extra-time instability

### 10.1 Purpose

Every result above uses the sector without extra-time momentum. EXP-5 shows why: a mode with momentum along an extra time is unstable once the extra times have deflated enough.

### 10.2 Equations solved

The extra times deflate as $c=h_5=h_6=h_7=e^{-Ht}$ ($H=1$), and a mode has momentum $q$ along $x_5$ ($k=0$, $m=1$), so $k_5/h_5=Q(t)=qe^{Ht}$ and

$$
h(t)=-im\gamma^4-Q(t)\gamma^4\gamma^5,\qquad h^2=E^2(t)=m^2-q^2e^{2Ht},\qquad t_\ast=\frac{\ln(m/q)}{H}.
$$

$h$ is not Hermitian ($\gamma^4\gamma^5$ is real antisymmetric) but it is $B$-pseudo-Hermitian, $h^\dagger B=Bh$: the Krein norm $u^\dagger Bu$ is conserved exactly and the Hilbert norm $u^\dagger u$ is not. For $t>t_\ast$, with $\varkappa=\sqrt{Q^2-m^2}$ and $W(t)=\int_{t_\ast}^t\varkappa\,dt'=H^{-1}[\sqrt{Q^2-m^2}-m\arccos(m/Q)]$, the WKB growth is $d\ln(u^\dagger u)/dt=2\varkappa$ at leading order and $2\varkappa-m^2/\varkappa^2$ at first adiabatic order.

### 10.3 Initial data and parameters

$q\in\{0.05,0.1\}$, so $t_\ast=2.99573$ and 2.30259; integration from $t=0$ to $t_\ast+3$ with 600 output intervals. The initial spinor is the positive-energy eigenvector of $h(0)$ ($E_0=\sqrt{m^2-q^2}=0.998749$ and 0.994987) that is also an eigenvector of $C$ with eigenvalue $\pm1$ ($C$ commutes with $h(t)$ for momentum along $x_5$), so $u^\dagger Bu=\pm E_0/m\ne0$. Four runs. The WKB comparison uses the window $[t_\ast+1.5,t_\ast+3]$, away from the turning point.

### 10.4 Solver settings and statistics

Adams + fixed point, rtol $10^{-10}$, atol $10^{-12}$, max_step 0.02: 2548 steps and 4800 right-hand-side evaluations.

### 10.5 Results

![EXP-5 (a) $\ln(u^\dagger u)$ for both momenta and both $C$ signs with the WKB curve $2W(t)$, and (b) $E^2(t)$, which turns negative at $t_\ast=\ln(m/q)/H$ (dotted).](artifacts/dirac16complex/numerics/figures/exp5_growth.png)

![EXP-5 (a) the Krein-norm drift normalised by $\max(u^\dagger u,1)$, below $10^{-8}$ throughout, and (b) the Krein norm, which stays at its initial value while $u^\dagger u$ grows.](artifacts/dirac16complex/numerics/figures/exp5_krein.png)

- $u^\dagger u$ reaches $1.258\times10^{16}$ ($q=0.05$) and $1.313\times10^{16}$ ($q=0.1$). The growth rate $d\ln(u^\dagger u)/dt$ rises from 2.37 ($q=0.05$) and 2.40 ($q=0.1$) early to 25.3 late, ratios 10.7 and 10.6: super-exponential growth.
- Over the window, $\Delta\ln(u^\dagger u)=30.9922$ against the leading WKB value 31.0241 (relative deviation $1.03\times10^{-3}$) and the first-order value 30.99986 ($2.47\times10^{-4}$) for $q=0.05$; 30.9455 against 30.9770 and 30.9530 for $q=0.1$. The late rate matches $2\varkappa-m^2/\varkappa^2$ to $4.6\times10^{-6}$.
- The Krein norm is conserved: normalised drift at most $1.08\times10^{-9}$, absolute drift up to $t_\ast$ at most $1.28\times10^{-9}$. At the end the absolute drift is 1.005 because $u^\dagger Bu$ is then an O(1) difference of terms of order $10^{16}$, the float64 cancellation floor.

### 10.6 Verification

The Rust program passes 7 of 7 self-checks and the EXP-5 checker 21 of 21 (finite-difference residual ratio 0.71; independent RK4 reference $3.34\times10^{-8}$ relative, refined $2.28\times10^{-9}$; closed-form WKB against quadrature $1.1\times10^{-14}$; repeat-run byte identity). The Mathematica notebook verifies $h^2=(m^2-Q^2)I$, $h^\dagger B=Bh$ and that $h$ is not Hermitian; NDSolve agrees to $3.34\times10^{-8}$ relative and a WorkingPrecision-32 run agrees with machine precision to $1.8\times10^{-14}$.

![Mathematica cross-check of the Hilbert-norm growth: Rust (dots), NDSolve (lines) and the leading WKB curve.](artifacts/dirac16complex/numerics/figures/mathematica/exp5_hilbert_norm_growth.png)

### 10.7 Physical interpretation

A mode with extra-time momentum stops oscillating and grows once the extra-time scale factor has deflated enough. The growth conserves the indefinite Krein norm, so it is a growing positive-norm part and a growing negative-norm part together: the ultrahyperbolic ill-posedness of the (4,4) signature. No positive Fock space exists for these modes. Any cosmology built on this field must exclude them, and every result of EXP-1 to EXP-4 is restricted to the good sector. This restriction is imposed, not derived; whether a dynamical mechanism suppresses the extra-time sector is open.

## 11. Independent cross-checks: the Jupyter and Mathematica notebooks

### 11.1 The Jupyter notebook

The Jupyter notebook and its tools are these files:

```
notebooks/dirac16complex_dark_sector.ipynb        the executed notebook
notebooks/build_dirac16complex_notebook.py        writes the notebook
notebooks/run_notebook.py                         headless executor
notebooks/check_notebook.py                       auditor
```

The notebook has 23 cells (15 markdown, 8 code; kernel python3). It runs every subcommand of the Rust program into the git-ignored build/notebook-run and requires all 65 written files (62 from the program, 3 from the EXP-3 analysis) to be byte-identical to the committed ones. It then recomputes the physics from the raw spinor columns with the fixture's gamma matrices, for example the exact EXP-1 propagator ($3.12\times10^{-9}$) and its own Gauss-Legendre quadrature of the EXP-3 comoving distance ($1.7\times10^{-9}$ from CVODE), and writes the 17 figures with fixed metadata. A gauntlet of 70 assertions covers every Rust, checker and analysis check, the Stage-1 results (153 of 153 checks), the fixture hash across all reports, the notebook's own recomputations and the 64 numbers quoted in its markdown. The notebook was executed headless by run_notebook.py and by python -m nbconvert. The auditor checked both executed copies (verdict SUCCESS, identical gauntlet results and figure hashes) and wrote notebook-report.json.

### 11.2 The Mathematica notebook

The Mathematica notebook and its two scripts are these files:

```
notebooks/Dirac16ComplexDarkSector.nb                     the notebook
scripts/build_dirac16complex_mathematica_notebook.wls     writes it deterministically
scripts/verify_dirac16complex_mathematica_notebook.wls    evaluates it headless
```

The verifier fails on any message, any failed evaluation or any false check. The notebook loads the Stage-1 packages Dirac16ComplexAlgebra.wl and Dirac16ComplexGeometry.wl from wolfram/. It reads the gamma matrices, $C$, $\gamma^8$ and $B$ back from src/generated.rs of the study and requires them to equal the package matrices exactly. It derives every reduced system from $\gamma^\mu D_\mu\Psi=M_{\mathrm{eff}}\Psi$ with the package geometry and compares it exactly with the Rust form. It runs the binary with RunProcess (print-config: exit code 0, last line SUCCESS, fixture hash and tolerances equal to the summaries). All 49 checks are true. The independent integrations (NDSolve against Rust unless stated):

| Quantity compared | Maximum deviation |
| --- | --- |
| EXP-1 spinor state | $2.92\times10^{-9}$ |
| EXP-1 exact-propagator error, Rust | $6.25\times10^{-9}$ |
| EXP-1 exact-propagator error, NDSolve | $4.3\times10^{-14}$ |
| EXP-2 $\ln h_i$ | $3.16\times10^{-8}$ |
| EXP-2 $H_i/\Theta$ | $3.24\times10^{-8}$ |
| EXP-2 $\ln h_i$ against the closed form, NDSolve | $2.7\times10^{-11}$ |
| EXP-2 spinor, raw | $1.08\times10^{-7}$ |
| EXP-2 spinor, phase aligned | $4.2\times10^{-10}$ |
| EXP-2 spinor against the exact solution, Rust | $2.24\times10^{-7}$ |
| EXP-2 the same, NDSolve | $7.7\times10^{-10}$ |
| EXP-3 spinor | $2.12\times10^{-8}$ |
| EXP-3 $\ln\sigma$ | $1.95\times10^{-14}$ |
| EXP-3 spinor against the exact solution, Rust | $5.48\times10^{-8}$ |
| EXP-3 the same, NDSolve | $2.0\times10^{-12}$ |
| EXP-4 thermal modes, raw | $2.62\times10^{-6}$ |
| EXP-4 thermal modes, phase aligned | $5.9\times10^{-8}$ |
| EXP-4 NDSolve Adams against Runge-Kutta | $6.6\times10^{-9}$ |
| EXP-4 kinetic theory, $\rho$ (relative) | $1.98\times10^{-8}$ |
| EXP-4 kinetic theory, $p$ (relative) | $1.87\times10^{-5}$ |
| EXP-4 pair modes, phase aligned | $7.6\times10^{-9}$ |
| EXP-4 pair $\lvert\beta\rvert^2$ (relative) | $1.9\times10^{-9}$ |
| EXP-5 state (relative) | $3.34\times10^{-8}$ |
| EXP-5 machine against 32-digit precision | $1.8\times10^{-14}$ |

The finite-difference right-hand-side test uses 9-point stencils; rows the output grid cannot resolve (rate times stencil width above 4) are excluded and counted, and EXP-4, whose sampling is too sparse, uses one-interval NDSolve propagation instead ($1.3\times10^{-10}$). Two environment details are documented in the notebook: the first PNG export in a headless kernel raises one named message about an optional paclet, which is silenced by name while the file is written, and the high-precision runs use exact coefficients.

![Agreement of NDSolve with the Rust CVODE solutions, as digits of agreement $-\log_{10}$ of the maximum deviation, for each experiment.](artifacts/dirac16complex/numerics/figures/mathematica/cross_check_deviations.png)

## 12. Synthesis: pressure, energy density, dark matter and dark energy

### 12.1 How pressure and energy density behave and change

- **Free condensate, any background:** $\rho=mS\propto1/V$ and $p=0$ exactly: dust, whatever the geometry does.
- **Repulsive condensate ($\lambda>0$):** $\rho=mS+\tfrac\lambda2S^2$ and $p=\tfrac\lambda2S^2>0$; $w\to1$ (stiff) at small $V$ and $w\to0$ at large $V$ (EXP-1, EXP-2).
- **Attractive condensate ($\lambda<0$):** $p<0$; phantom where $M_{\mathrm{eff}}<0<\rho$; $\rho<0$ at still smaller $V$; $w\to0$ at large $V$ (EXP-2, EXP-3).
- **Primordial field:** $V$ is constant, so $\rho$ and $p$ are frozen; dust or slightly stiff, with a $2E$ oscillation of the pressure for superpositions of the energy signs (EXP-1).
- **Thermal gas:** $\rho\propto a^{-4}$ early and $\propto a^{-3}$ late; $w$ falls from 0.3329 to 0.0359 as the momenta redshift (EXP-4).
- **Created pairs:** $w$ falls from values between 0.24 and 0.31 at the end of inflation to about $10^{-4}$, and $\rho a^3\to m\,na^3$ (EXP-4).
- **Extra-time modes:** no positive norm and super-exponential growth after $t_\ast$; $\rho$ and $p$ are not defined in a positive Fock space (EXP-5).

Three mechanisms control everything. **Dilution:** $SV$ is constant, so the mass term behaves like dust in the 7-volume and the four-fermion term like a stiff fluid in the 7-volume. **Redshift:** the pressure of quanta is momentum flux and falls faster than their energy. **Geometry:** what a 3-space observer infers depends on how the 7-volume relates to the 3-space volume, $w_{\mathrm{eff}}=-1+\Theta(1+w)/(3H_a)$. In EXP-1 $\Theta=0$, in EXP-2 $\Theta\to7H_a$, and in EXP-3 and EXP-4 $\Theta=3H_a$ by assumption.

### 12.2 Dark matter

**What behaves like dark matter.**

- The free condensate is exact dust in every background: $w=0$, $\mathrm{KE}_L=\mathrm{PE}_L=\rho/2$, $\mathrm{KE}_H=0$, $\mathrm{PE}_H=\rho$ (EXP-1 with $K=0$, EXP-2 and EXP-3 with $x_0=0$).
- A gas of quanta has a time-varying equation of state, relativistic to dust: $w=0.3329$ at $T=10m$ and $0.0359$ after a hundredfold expansion, in agreement with kinetic theory; $\mathrm{KE}_H/\rho=3w$ falls from 1 to about 0.11 while the rest-mass fraction $\mathrm{PE}_H/\rho$ rises (EXP-4a).
- Gravitational pair creation at the end of inflation gives $na^3=1.455\times10^{-3}$, $4.991\times10^{-3}$, $4.414\times10^{-3}$ and $2.422\times10^{-3}\,H_{\mathrm{inf}}^3$ for $m/H_{\mathrm{inf}}=0.1$, 0.5, 1 and 2, and nothing for $m=0$ (EXP-4b). The produced gas is dust ($w\approx10^{-4}$) by the end of each run.
- Any repulsive or attractive condensate becomes dust at large volume (EXP-2, EXP-3), because the interaction energy dilutes faster.

**What is not established.**

1. **Abundance.** No relic density $\Omega_{\mathrm{DM}}h^2$ was computed. The yields are per comoving volume in units of $H_{\mathrm{inf}}^3$ at the end of de Sitter; converting them requires physical values of $m$ and $H_{\mathrm{inf}}$ and the reheating history.
2. **Darkness.** The framework has no coupling to the standard model, so the quanta are dark by construction; no bounds on interactions, annihilation through the $\lambda$ term or decays were derived.
3. **Stabilised extra dimensions.** In self-consistent 8D gravity (EXP-2) all seven directions end up expanding equally, and a 3-space observer sees the dust dilute like $a^{-7}$ ($w_{\mathrm{eff}}\to4/3$). Dust-like dilution in 3-space, which dark matter needs, requires static extra dimensions; that was assumed in EXP-3 and EXP-4, not derived.
4. **The extra-time sector** must be excluded by hand (EXP-5).
5. **Structure formation**, free streaming of the warm phase and clustering were not computed.

**Answer on dark matter.** There is a qualitative connection: in the good sector, with stabilised extra dimensions, dirac16complex quanta and free condensates are pressureless matter, and expansion produces the quanta gravitationally. The connection is an equation of state and a production mechanism, not a dark-matter model, and nothing computed here predicts the observed dark-matter density.

### 12.3 Dark energy: which mechanisms give negative pressure or $w<-1/3$

1. **Attractive four-fermion interaction ($\lambda<0$).** The only mechanism with genuinely negative pressure, $p=\tfrac\lambda2S^2<0$. $w=x_0\sigma/(1+x_0\sigma)$ lies in $(-1,0)$ at low density and below $-1$ (phantom) where $\mathrm{KE}_L=\tfrac12SM_{\mathrm{eff}}<0$ with $\rho>0$. The phantom crossing happens where $M_{\mathrm{eff}}=0$, is immediately followed by $\rho<0$ at higher density, and in EXP-3 by a bounce (EXP-2: phantom for $0.4<V/V_0<0.8$ and $\rho<0$ below 0.4).
2. **Frozen density in the primordial field.** In EXP-1 the 7-volume is constant ($\Theta=0$), so the density does not dilute while 3-space inflates. For a 3-space observer that is the dilution of a cosmological constant: $w_{\mathrm{eff}}=-1+\Theta(1+w)/(3H_a)=-1$ (derived here from the EXP-2 definition and the EXP-1 background, not a separate machine check). The actual pressure is zero or positive, and the geometry is not self-consistent: 8D Einstein gravity would need $\rho_{\mathrm{req}}\le-21$ (Section 6.5).
3. **Deflating extra times** (EXP-3 variant). With $c\propto a^{-\gamma}$, $\sigma\propto a^{-n}$, $n=3(1-\gamma)<3$, the density dilutes more slowly than $a^{-3}$. $\gamma=0.875181$ ($n=0.374457$, $x_0=-0.4626545$) reproduces the Unite tangent of $p/\rho$ exactly, and distances measure $w_{\mathrm{eff}}$ with tangent $(-0.9827,-0.0749)$. Section 12.5 lists why it fails.

The Lagrangian has no cosmological-constant term ($U(0)=0$ is forced for a Grassmann field), and a condensate has $w=-1$ only at the instant $M_{\mathrm{eff}}=0$.

### 12.4 Quantitative comparison with Unite

The fitted and tangent parameters per scenario. "Requested" fits are the programme's: least-squares CPL fit of $w(a)$ on $a\in[1/3.26,1]$, and CPL and constant-$w$ fits of $\mathrm{DM}(z)$ on $z\in[0.01,2.26]$ with the offset profiled. For $x_0<-0.028863$ the $w(a)$ fit does not exist ($w$ has a pole at $a=|x_0|^{1/3}$ inside the range) and for $x_0<-0.041024$ the $\mathrm{DM}(z)$ fits do not exist (the bounce lies at $z_b<2.26$). The restricted fits use the largest range on which each model is defined ($w\ge-3$; $z<z_b$); they are supplementary and not the programme's fits.

Tangent parameters and the status of the requested fits:

| $x_0$ | tangent $w_0$ | tangent $w_a$ | requested fits |
| --- | --- | --- | --- |
| $-0.462654$ | $-0.861$ | $-4.807$ | undefined |
| $-0.433107$ | $-0.764$ | $-4.043$ | undefined |
| $-0.3$ | $-0.4286$ | $-1.837$ | undefined |
| $-0.2$ | $-0.25$ | $-0.9375$ | undefined |
| 0 | 0 | 0 | $(0,0)$ and $w=0$ |

Restricted least-squares CPL fit of $w(a)$ (supplementary):

| $x_0$ | range of $a$ | $w_0$ | $w_a$ |
| --- | --- | --- | --- |
| $-0.462654$ | $[0.851,1]$ | $-0.605$ | $-12.83$ |
| $-0.433107$ | $[0.833,1]$ | $-0.485$ | $-11.68$ |
| $-0.3$ | $[0.737,1]$ | $-0.074$ | $-7.583$ |
| $-0.2$ | $[0.644,1]$ | 0.130 | $-5.267$ |
| 0 | $[0.307,1]$ | 0 | 0 |

Restricted CPL fit of $\mathrm{DM}(z)$ with the offset profiled (supplementary):

| $x_0$ | range of $z$ | $(w_0,w_a)$ | rms residual |
| --- | --- | --- | --- |
| $-0.462654$ | $[0.01,0.388]$ | $(2.106,-48.18)$ | 0.078 mag |
| $-0.433107$ | $[0.01,0.423]$ | $(1.846,-39.84)$ | 0.074 mag |
| $-0.3$ | $[0.01,0.633]$ | $(1.164,-18.11)$ | 0.062 mag |
| $-0.2$ | $[0.01,0.890]$ | $(0.871,-9.943)$ | 0.056 mag |
| 0 | $[0.01,2.26]$ | $(0,0)$ | 0 |

Restricted constant-$w$ fit of $\mathrm{DM}(z)$ and the largest distance-modulus difference from the Unite CPL model over the same range (same $H_0$):

| $x_0$ | constant $w$ | rms residual | $\max\lvert\Delta\mathrm{DM}\rvert$ |
| --- | --- | --- | --- |
| $-0.462654$ | $-2.764$ | 0.120 mag | 0.832 mag |
| $-0.433107$ | $-2.478$ | 0.115 mag | 0.785 mag |
| $-0.3$ | $-1.524$ | 0.099 mag | 0.549 mag |
| $-0.2$ | $-1.012$ | 0.090 mag | 0.329 mag |
| 0 | 0 | 0 | 0.795 mag |

References and the deflation variant:

| Reference or variant | $(w_0,w_a)$ | constant $w$ |
| --- | --- | --- |
| Unite CPL (PDF) | $(-0.861,-0.60)$ | none |
| Unite wCDM (PDF) | none | $-0.764$ |
| best constant $w$ for the Unite CPL distances | none | $-1.0277$ |
| the same with the offset fixed at 0 | none | $-0.9747$ |
| the same on a log-uniform $z$ grid | none | $-0.9790$ |
| $\Lambda$CDM | $(-1,0)$ | $-1$ |
| deflation variant, $p/\rho$ | $(-0.861,-0.60)$ | none |
| deflation variant, tangent of $w_{\mathrm{eff}}$ | $(-0.9827,-0.0749)$ | none |
| deflation variant, $w_{\mathrm{eff}}(a)$ fit | $(-0.955,-0.247)$ | none |
| deflation variant, $\mathrm{DM}(z)$ fits | $(-0.9707,-0.1611)$ | $-1.0159$ |

For the Unite CPL, $w_0+w_a=-1.461$ and $w=-1$ at $a=0.768$. The deflation variant's $p/\rho$ reproduces the Unite tangent by construction.

The scan over $x_0\in[-0.49,0]$ in steps of 0.001 (491 models, fits_scan.csv) finds $x_0=-0.4626545$ for $w_0=-0.861$, with tangent $w_a=-4.807$, and $x_0=-0.4331066$ for $w_0=-0.764$.

**Reading the tables.**

- Matching today's Unite value $w_0=-0.861$ forces $w_a=-4.81$: the condensate evolves about eight times faster than the Unite fit. It crosses $w=-1$ at $z=0.026$ (the Unite CPL crosses at $a=0.768$), its energy density is negative beyond $z=0.293$ and the universe has a bounce at $z=0.388$. There is no matter era and no redshift beyond 0.388, so the model cannot be confronted with supernovae up to $z=2.26$, let alone with the CMB.
- The fits that the comparison was meant to use do not exist for any $x_0<-0.041$. The restricted fits give values such as $(w_0,w_a)=(2.1,-48)$ with residuals of 0.06 to 0.08 mag, which only show that the CPL form does not describe these models.
- **The benchmark $w=-0.764$.** The model reproduces it only as today's value ($x_0=-0.433107$), with $w_a=-4.04$; a constant-$w$ fit to that model's own distances gives $-2.48$. Moreover, $-0.764$ is not a constant-$w$ projection of the Unite CPL curve: the best constant $w$ for the CPL distances is $-1.028$ (uniform $z$), $-0.975$ (offset zero) or $-0.979$ (log-uniform $z$), with $\Omega_m=0.305$ fixed and noise-free equal weights. The PDF describes $-0.764$ as a direct wCDM fit of the supernovae alone, which is a different statistical question.
- Only the deflation variant comes close to Unite in distances ($\max|\Delta\mathrm{DM}|=0.021$ mag, 0.011 mag with the offset profiled), and its distances look like a mildly evolving $w\approx-0.97$ to $-1.02$, not like the Unite CPL; it fails for other reasons (Section 12.5).

### 12.5 Where the model fails

1. **Rapid evolution.** $w_a=3x_0/(1+x_0)^2$ is fixed by $w_0$; at the Unite $w_0$ it is $-4.81$ instead of $-0.60$.
2. **Negative energy density** beyond the zero of $\rho_\psi$ ($z=0.293$ for the Unite-tuned model), followed by a bounce ($z=0.388$): no matter era, no early universe.
3. **Sound speed.** $c_s^2=dp/d\rho=2x_0\sigma/(1+2x_0\sigma)$ is negative today for every attractive model ($-12.39$, $-6.47$, $-1.50$, $-0.667$). In a fluid description that is a gradient instability of perturbations (not computed); at the phantom crossing $1+2x_0\sigma=0$ the closed form diverges.
4. **The 8D Einstein bound.** With $\rho\ge0$, a 3-space observer cannot infer $w_{\mathrm{eff}}<-1+(1+w)/\sqrt3$ (EXP-2); for dust $-0.42265$. The deflation variant's $w_{\mathrm{eff}}\approx-0.98$ therefore needs negative 8D energy density: $\kappa\rho_8=3H_a^2(1-3\gamma+\gamma^2)=-2.579H_a^2$ for $\gamma=0.875$; sustained deflation with $\gamma$ between $(3-\sqrt5)/2=0.382$ and $(3+\sqrt5)/2=2.618$ always does. EXP-2 shows, moreover, that the extra times turn to expansion by themselves.
5. **Varying Newton constant.** $G_N=G_8/V_{\mathrm{extra}}\propto a^{3\gamma}$ gives $\dot G/G=3\gamma H_0=2.63H_0$, about $1.8\times10^{-10}$ per year for $H_0=67.4$ km/s/Mpc, some 1800 times the order-of-magnitude lunar-laser-ranging bound of $10^{-13}$ per year, and $G_N(z=1)/G_N(0)=0.162$. The constant-$G_N$ Friedmann equation used in EXP-3 is itself inconsistent with this.
6. **4D energy conservation.** For $n\ne3$ the condensate exchanges energy with the extra dimensions: $d\rho/dN+3(\rho+p)=0.254$ today in units of $3H_0^2/\kappa_4$. Distances then measure $w_{\mathrm{eff}}$, not $p/\rho$.
7. **Krein structure and the extra-time instability.** The canonical state space is indefinite; only the good sector has a positive Fock space, and modes with extra-time momentum grow super-exponentially (EXP-5). The restriction is imposed by hand.
8. **Homogeneous mean field only.** One c-number mode stands for the condensate; quantum corrections, the stability of the condensate and inhomogeneities were not computed.
9. **No perturbations and no data likelihood.** Nothing here is a fit to supernova, BAO or CMB data; the distance comparisons use noise-free curves with equal weights and fixed $\Omega_m$.

### 12.6 The answer

- **Dark matter: a qualified yes.** In the good sector, with stabilised extra dimensions, dirac16complex behaves like cold matter: free condensates are exact dust, a thermal gas turns from radiation into dust, and the end of inflation creates quanta for every $m>0$. This is a dark-matter-like equation of state and a gravitational production mechanism. The abundance, the absence of standard-model couplings, the stabilisation of the extra dimensions and the perturbations are not established, so it is not a dark-matter model.
- **Dark energy: no, within everything computed.** The only negative pressure comes from an attractive four-fermion interaction, and it comes with a phantom crossing where the effective mass vanishes, negative energy density at earlier times, a bounce instead of a matter era, and a negative sound speed squared. Tuned to Unite's $w_0=-0.861$ it evolves eight times too fast ($w_a=-4.81$ against $-0.60$). The frozen density of the primordial field mimics a cosmological constant only in its dilution, in a geometry that needs negative energy. Deflating extra times reproduce the Unite tangent in $p/\rho$ but violate energy conservation in 4D and the 8D energy bound, and they make $G_N$ vary about 1800 times faster than the lunar-laser-ranging bound allows. The framework reproduces neither Unite's $(w_0,w_a)$ nor $w=-0.764$ consistently.

## 13. Verification summary

| Experiment | Rust self-checks | Python checker | Mathematica |
| --- | --- | --- | --- |
| EXP-1 | 10 of 10 | 25 of 25 | 6 of 6 |
| EXP-2 | 15 of 15 | 34 of 34 | 5 of 5 |
| EXP-3 | 14 of 14 | 31 of 31 | 4 of 4 |
| EXP-4 | 23 of 23 | 51 of 51 | 5 of 5 |
| EXP-5 | 7 of 7 | 21 of 21 | 4 of 4 |
| total | 69 of 69 | 162 of 162 | 24 of 24 |

Every checker includes repeat-run byte identity and refined-tolerance convergence; for the EXP-2 spinor phase the refined run confirms the identified rounding floor instead of a smaller error. In addition: the EXP-3 analysis, 9 of 9 checks; the Jupyter notebook's gauntlet, 70 of 70 assertions in both executions, with 65 of 65 freshly written files byte-identical to the committed ones; and the remaining 25 of the Mathematica notebook's 49 checks (10 algebra, 7 Rust constants, 6 for the binary, 1 for the quoted parameters and 1 for the figures). Every report records the fixture sha256 of Section 14. Where the numerical programme's a priori expectations were contradicted by measurement, the checks test the measured truth and the reports record the deviation: in EXP-1 the pressures are frozen only for eigenstates; in EXP-2 the bound $\Theta>\sqrt3H_a$ holds only where $\rho\ge0$; in EXP-3 the backward range ends at the bounce and the requested fits do not exist; in EXP-4 the per-mode $|\beta|^2\le10^{-6}$ is unattainable at $H_i/m=0.05$ for a sudden start, and the pressure carries the free-wave interference; in EXP-5 the absolute Krein drift at late times is the float64 floor.

## 14. Files and hashes

sha256 of the inputs and outputs this document quotes. The fixture hash is the one recorded in every summary, every checker report and src/generated.rs; the hash of generated.rs itself was computed for this edition; the summaries, checker reports and fits.json carry the hashes recorded in numerics-summary.json. The publication test of this document recomputes all of them.

```
artifacts/dirac16complex/arbitrary-field/algebra-fixture.json
  8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b
studies/dirac16complex_cosmology/src/generated.rs
  29631bcd9e737b5fe57a41ae2750c7637e31580974577d34b26ada45c560a3ba
artifacts/dirac16complex/numerics/exp1/summary.json
  f8886625011a35c5ea31c89ffb623e4c6b0678adc300fc4b725179808601272a
artifacts/dirac16complex/numerics/exp1/python-check-report.json
  840fc6fb8797fa66cd043a199357b599c6b2202cbeef426f0ed9058d318fafe4
artifacts/dirac16complex/numerics/exp2/summary.json
  c8f7ecd95f7414f81e2569be7a41f2127d0c1cbd3a7a07b2c0dbcb667c43d5d0
artifacts/dirac16complex/numerics/exp2/python-check-report.json
  b2d0c6d55cc0a3f6ebe0fcd3c6de0221964e32a9607c07e374398dcac4e70d5d
artifacts/dirac16complex/numerics/exp3/summary.json
  7bfedf4bd5e5765c171dcc71896e4a9f481bfedfeafa6ddae04b924ca31081ee
artifacts/dirac16complex/numerics/exp3/python-check-report.json
  86e92fbf565cc6498aed329fc6d5506e8749c6a31a24ec41f2f8f84048263406
artifacts/dirac16complex/numerics/exp3/fits.json
  775bada287e5b48e89a7a218cfcdde524d8030eadf1606e1ecc37bcc2d884ce3
artifacts/dirac16complex/numerics/exp4/summary.json
  beaf5bad11dc9e49271a5c55e116fdc5e7661cbdf4ffdeb590be848290a78d07
artifacts/dirac16complex/numerics/exp4/python-check-report.json
  364993ae61e6f5658eb66e17b4be772d0a68e1f964b4f84dd2b89e37c3b2264c
artifacts/dirac16complex/numerics/exp5/summary.json
  bbddd4d4e0303c72d8d13494e2f4a54a730f0687fdba54a240156c7b0cfb1746
artifacts/dirac16complex/numerics/exp5/python-check-report.json
  bf7d379b6cf41da6984c1a3490aec5ffedf968295ee52c2c06dcb4f5d8128e03
```

The sha256 of each of the 17 figures is recorded in notebook-report.json, and the figures of the Mathematica notebook are listed in mathematica-report.json. build_provenance_pdf.py records the sha256 of every figure of this document in its build report.

## 15. Reproduction

Run every command from the repository root. The engine (once per clone):

```
.\scripts\setup_solver.ps1 -Platform win11
bash scripts/setup_solver.sh
```

(the first in PowerShell, the second in Git Bash, macOS or Linux; the platform is detected or given as win11, macos or linux). Build and run all five experiments, then the EXP-3 analysis:

```
cargo build --release --manifest-path studies/dirac16complex_cosmology/Cargo.toml
studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology all
python scripts/analyze_dirac16complex_exp3.py
```

The last line of the program is SUCCESS. The independent checkers, each with repeat-run byte identity and refined convergence (the scratch directories under build/ are git-ignored):

```
python scripts/check_dirac16complex_exp1.py --repeat build/repeat --refined build/refined
python scripts/check_dirac16complex_exp2.py --repeat build/repeat --refined build/refined
python scripts/check_dirac16complex_exp3.py --repeat build/repeat --refined build/refined
python scripts/check_dirac16complex_exp4.py --repeat build/repeat --refined build/refined
python scripts/check_dirac16complex_exp5.py --repeat build/repeat --refined build/refined
```

Each prints its check lines and exits 0 only if every check is true; it rewrites the committed python-check-report.json of its experiment.

The notebooks and this document:

```
python notebooks/run_notebook.py --quiet notebooks/dirac16complex_dark_sector.ipynb
python notebooks/check_notebook.py notebooks/dirac16complex_dark_sector.ipynb
wolframscript -file scripts/verify_dirac16complex_mathematica_notebook.wls
python -m unittest tests.test_d16c_numerics_publication -v
python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md
```

Running the Mathematica verifier rewrites mathematica-report.json and the figures under figures/mathematica (byte-identically). The PDF step builds this document twice (two builder runs, three pdflatex passes each, with the repository root as working directory so that the figures are found), requires warning-free logs and byte-identical PDFs, compares the result with the registered edition dirac16complex-dark-sector-numerics in provenance/pdf-specifications.json and prints provenance_pdf=OK. After an edit of this document the edition is registered again with

```
python scripts/build_provenance_pdf.py --register \
    provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md
```

(in PowerShell the two lines are written as one line), and the two sha256 pins in the publication test of this document are updated. The student guide of this stage, whose PDF lies next to this one in provenance/, gives every step in detail for Windows, macOS and Linux.

## 16. Limitations

1. **Backgrounds.** All experiments use homogeneous diagonal metrics. EXP-1 prescribes the primordial field, EXP-3 and EXP-4 prescribe 4D or 3-space FRW expansions with static extra dimensions, and only EXP-2 solves 8D Einstein gravity self-consistently. Einstein-Lovelock terms are not included.
2. **Mean field.** The condensate is one c-number mode with the expectation-value rule; its quantum stability, fluctuations and renormalisation are not studied. The gas and the pairs are free modes; the $\lambda$ interaction between quanta is not included in EXP-4.
3. **Good sector only.** Modes with extra-time momentum are excluded by hand because they are unstable (EXP-5); the Krein space is not given a physical interpretation beyond the good sector.
4. **Units and abundances.** The runs use $m$, $H$, $H_0$ or $H_{\mathrm{inf}}$ as units. The EXP-3 masses $m/H_0$ of 3 to 94 serve only to show phase independence, and no physical mass, relic abundance or inflation scale is predicted.
5. **Observational comparison.** The Unite numbers come from the reference PDF; no error bars, covariances or data were used. The $\pm0.118$ band of the $w(a)$ figure is an inferred approximation. The distance fits are equal-weight fits of noise-free curves with $\Omega_m=0.305$ fixed.
6. **Perturbations.** The sound speed is the adiabatic $dp/d\rho$ of the homogeneous solution; no perturbation equations, structure growth or CMB spectra were solved.
7. **Numerics.** The EXP-2 spinor phase is limited by the rounding of CVODE's internal time, and the raw EXP-4 thermal-mode deviation plausibly by the same effect (not proven); the EXP-5 absolute Krein drift at the end is limited by float64 cancellation, and the EXP-4 thermal energy density by the momentum cutoff ($2.4\times10^{-3}$ at $a=1$). These floors are identified and reported, not removed.
8. **Scope of the answer.** "No viable dark energy" refers to the mechanisms available in this Lagrangian and these backgrounds. A different potential, non-homogeneous states, other couplings or a mechanism that stabilises the extra dimensions were not examined.
