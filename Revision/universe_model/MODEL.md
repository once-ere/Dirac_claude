# UM-1: a 4+4 model of the Universe with Einstein-Lovelock gravity, the dirac16complex field and an x0-generated mass spectrum

Version 1.3 of 2026-10-17: version 1 plus the two changes that the solution forces (marked CHANGED in sections 4.1
and 8; the reasons are in `SOLUTION.md` section 3), (1.2) the corrections of the analysis `ANALYSIS.md` to sections
1, 4.4, 6 and 8 and the new section 9, and (1.3) the closing of the gaps that the analysis found (`GAPS.md`): the
resolved tip (section 4.4) and the vector portal P1 on the lepton multiplets (section 4.5). Written at
the author's order of 2026-10-17 ("create a new model of the Universe"). This
document DEFINES the model. Its field equations are derived in `FIELD_EQUATIONS.md` (scripts in `field_equations/`),
an approximate solution is computed in `SOLUTION.md` (scripts in `solution/`), and the origin of every ingredient is in
`PROVENANCE.md`. Every statement below is labelled as one of: DERIVED (computed in this repository, with the file
named), TAKEN (from the Revision record, file named), STANDARD (textbook physics, used as input), ASSUMED (a choice of
this model), INVENTED (a new phenomenological ingredient of this model) or OPEN.

## 1. Summary

The model lives on an eight-dimensional space with the author's coordinates $x_0, x_1, \dots, x_7$: $x_0$ is the hidden
space-like direction, $x_1, x_2, x_3$ are ordinary space, $x_4$ is the time and $x_5, x_6, x_7$ are three extra
time-like directions that deflate exponentially. Gravity is Einstein-Lovelock gravity in eight dimensions with the
author's couplings. The dirac16complex field $\Psi$, a 16-component spinor of $Cl(4,4)$ coupled to gravity through the
canonical spin connection, is the dark-matter candidate: its heavy odd quanta conditionally, its massless fold band as
dark radiation, and none of its states as dark energy (`ANALYSIS.md`, section 9 below). Photons, neutrinos, electrons, up and down quarks, the gluons
(required for consistency with QCD), and the $W^\pm$ and $Z$ bosons are eight-dimensional fields of the gauge group
$SU(3)_c \times SU(2)_L \times U(1)_Y$. There is NO Higgs field and no Higgs particle.

The central new idea (the author's): every field is a function of $x_0$ that is periodic with the period
$\ell_0 = \pi/(6H)$ of the metric. Expanding a field in the eigenfunctions of its $x_0$ operator turns the
eight-dimensional wave equation into a tower of four-dimensional fields whose masses are the eigenvalues. A mode that
does not depend on $x_0$ is massless (graviton, photon, gluon). A mode localised in $x_0$ carries a hidden momentum
$\Delta p_{x_0} \geq \hbar/(2\,\Delta x_0)$ and therefore an effective mass. The model makes this precise: the
four-dimensional mass of every massive particle is the lowest eigenvalue of its $x_0$ operator on the periodic cell,
with the boundary conditions at the two special points of the cell (the fold $z = \pi/2$ and the tip $z = 0$).
CORRECTED in version 1.2 (`ANALYSIS.md`): the uncertainty relation bounds the hidden kinetic part of every such
eigenvalue, and it bounds the mass itself for the $x_0$ excitations (every mode heavier than the gap $3H/(2f)$,
including the dark matter). It does not bound the masses of the protected zero modes, which are localised at the fold
yet massless, and the light masses ($W$, $Z$, $e$, $\nu$, $u$, $d$) come from the tip, not from localisation
(section 9).

## 2. Space, coordinates and the periodic cell

* Coordinates (TAKEN, `Revision/SPEC.md` section 1): $z = 6Hx_0$ takes every real value; the metric depends on $x_0$
  only through $\cot^2 z$ and $(\sin^2 z)^{1/6}$, both periodic with period $\pi$ in $z$, i.e. with period
  $\ell_0 = \pi/(6H)$ in $x_0$.
* The cell (TAKEN, `Revision/kohn_sham/ks-theory.json`, boundaryConditions): one period $0 < z < \pi$ consists of two
  halves, $0 < z < \pi/2$ and $\pi/2 < z < \pi$, joined at the FOLD $z = \pi/2$ ($\cos z = 0$, where $g_{00}$ and
  $\sqrt{|g|}$ vanish) and ending at the TIP $z \to 0, \pi$ ($\sin z \to 0$). The hidden coordinate
  $y = \ln|\sin z|/(6H) \in (-\infty, 0]$ measures the distance from the fold; $dy = \cot z\, dx_0$.
* A field periodic in $x_0$ with period $\ell_0$ is a field on the cell. Its two halves are related by the fold
  condition $(1 - Q(\theta))\chi(0) = 0$, $Q(\theta) = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2$, with $\theta = 0$
  (even) or $\theta = \pi$ (odd) (DERIVED in the Kohn-Sham record up to $\theta$). Periodicity in $x_0$ requires that the
  two tips of a cell ($z \to 0^+$ and $z \to \pi^-$) be identified; the proper distance to the tip is infinite, so the
  model replaces the tip by a regular cutoff at $y = -L$ (ASSUMED, as in the Kohn-Sham record; `tip_convergence/`
  measures the dependence on $L$).

## 3. The metric as a power series

The metric is written as a series of terms of decreasing magnitude (ASSUMED structure):

$$ g_{MN} = \bar g_{MN} + \epsilon\, h^{(1)}_{MN} + \epsilon^2 h^{(2)}_{MN} + \dots $$

* Order 0 (the background, TAKEN from `Revision/SPEC.md` section 1, the corrected primordial metric, version 2):
  $$ \bar g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\ -1,\ -e^{-2a_4}b_4(\sin^2 z)^{1/6},\ -e^{-2a_4}b_4(\sin^2 z)^{1/6},\ -e^{-2a_4}b_4(\sin^2 z)^{1/6}\big) $$
  with two GENERAL functions of the time, $a_4(x_4)$ (the observer's scale factor $a = e^{a_4}$) and $b_4(x_4) > 0$.
  The block $(x_0, x_5, x_6, x_7)$ has the common scale factor $f = e^{-a_4}b_4^{1/2}$ and the rate
  $h_4 = \dot f/f = u/2 - \dot a_4$, $u = \dot b_4/b_4$; the extra times deflate when $h_4 < 0$. The primordial history
  of the record is $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ ($h_4 = -H/3$). The model keeps $a_4$ and $b_4$ general and
  determines them from the field equations with all sources (section 7).
* Order 1: the cosmological perturbations, in the 3+1 decomposition of $(x_1, \dots, x_4)$: the scalar potentials
  $\Phi, \Psi_N$ (Newtonian gauge, $\delta g_{44} = -2\Phi$, $\delta g_{ij} = -2\Psi_N e^{2a_4}\delta_{ij}$), the
  tensor modes $h^{TT}_{ij}$, and the block perturbation $\delta b_4/b_4 = 2\sigma$ (a radion), all functions of
  $(x_1, \dots, x_4)$ times the flat $x_0$ zero-mode profile; the $x_0$-dependent parts of the sources drive
  $x_0$-dependent corrections, which are expanded in the same $x_0$ eigenfunctions as the fields and are heavy
  (section 5). The bookkeeping parameter $\epsilon$ is of the size of the CMB temperature anisotropy,
  $\epsilon \sim 10^{-5}$ (STANDARD).
* Order 2 and beyond: the products of order-1 quantities and the $x_0$-heavy modes; not computed in version 1 (OPEN).

## 4. Fields and action

$$ S = S_{EL}[g] + S_\Psi[g, \Psi] + S_{SM}[g, A, \psi] + S_{tip}[g, A, \psi, \Sigma] + S_{portal}[\Psi, A, \psi] $$

### 4.1 Einstein-Lovelock gravity (TAKEN)

$$ S_{EL} = \frac{1}{2\kappa}\int d^8x \sqrt{|g|}\,\Big(\sum_{k=1}^{3}\alpha_k\,\mathcal{L}_{(k)} - 2\Lambda\Big),\qquad \sum_k \alpha_k E_{(k)}{}^M{}_N + \Lambda\,\delta^M_N = \kappa\,T^M{}_N $$

with $\mathcal{L}_{(1)} = R$, $\mathcal{L}_{(2)}$ the Gauss-Bonnet and $\mathcal{L}_{(3)}$ the cubic Lovelock density, the
author's weights $\alpha_k = w_k H^{2-2k}$, $w = (1, 1/32, 1/1152)$, and $\Lambda = -10H^2$ in the convention of
`Revision/field_equations_a4/a4-equations.json`. The graviton is the $x_0$ zero mode of $g_{MN}$ and is massless.

CHANGED in version 1.1 (`SOLUTION.md` section 3, DERIVED there): with the author's weights the only static vacuum,
$k_0 = 1/(4w_2) = 8$ with $\Lambda_0 = -24H^2$, has the effective-Newton factor $G(k_0) = -5 + 9w_3/(2w_2^2) = -1$, i.e.
repulsive four-dimensional gravity, and $\Lambda = -10H^2$ admits no static block with a small cosmological term.
Version 1.1 uses $w = (1, 1/32, 1/768)$ ($G(k_0) = 1$, the Einstein value) and $\Lambda = -24H^2 + \delta\Lambda$, and
ASSUMES a block stabiliser (an extra potential for $k = e^{2a_4}/b_4$ with curvature above $k_0G(k_0)H^2/4 = 2H^2$,
since the block mode of the homogeneous reduction has $\lambda^2 = k_0G(k_0)H^2/4$: attractive gravity makes the
static block unstable). The origin of the stabiliser (the Casimir energy of the cell) is OPEN.

### 4.2 The dirac16complex field (TAKEN)

$$ S_\Psi = \int d^8x\sqrt{|g|}\,\Big[\tfrac12\big(\bar\Psi\gamma^M D_M\Psi - (D_M\bar\Psi)\gamma^M\Psi\big) - m\,\bar\Psi\Psi - \tfrac{\lambda}{2}(\bar\Psi\Psi)^2\Big],\quad D_M = \partial_M + \Omega_M,\ \Omega_M = \tfrac12\omega_M{}^{ab}S_{ab} $$

with $\bar\Psi = \Psi^\dagger C$, the author's $\gamma$ matrices (`Revision/algebra/gammas.json`) and the CANONICAL spin
connection of the diagonal vielbein of $\bar g$, which is non-trivial: $\gamma^M\Omega_M = \tfrac32 H e^{a_4}b_4^{-1/2}\gamma^{x_0} + (u - \tfrac12\dot a_4)\gamma^{x_4}$
(DERIVED, `Revision/lead_checks/`). $\Psi$ is a singlet of $SU(3)_c \times SU(2)_L \times U(1)_Y$ (ASSUMED: dark). Its
quanta are of three kinds (DERIVED in the Kohn-Sham record): the fold-band quanta, $\varepsilon = e^{-a_4}|k|$ exactly,
MASSLESS in four dimensions (the fold zero modes of the $x_0$ operator); the bulk-band quanta with
$\varepsilon \geq m$ (massive; the $x_0$ momentum adds $(l\pi/(fL))^2$ to $m^2$); and the homogeneous condensate
$S = \bar\Psi\Psi = S_0 e^{a_4}b_4^{-2}$.

### 4.3 The Standard-Model sector in eight dimensions (ASSUMED structure, STANDARD content)

* Gauge fields $G^\alpha_M$ ($SU(3)_c$), $W^a_M$ ($SU(2)_L$), $B_M$ ($U(1)_Y$) with
  $S_{gauge} = -\frac14\int d^8x\sqrt{|g|}\, g^{MP}g^{NQ}\big(\frac{1}{\hat g_s^2}G^\alpha_{MN}G^\alpha_{PQ} + \frac{1}{\hat g^2}W^a_{MN}W^a_{PQ} + \frac{1}{\hat g'^2}B_{MN}B_{PQ}\big)$;
  the four-dimensional couplings are $g^2 = \hat g^2/V_\perp$ etc. with $V_\perp$ the proper volume of the cell and the
  extra-time block (section 5).
* One generation of fermions, each an eight-dimensional spinor of $Cl(4,4)$ (16 components, the same algebra as $\Psi$):
  $L = (\nu, e)_L$ (doublet, $Y = -\frac12$), $e_R$ ($Y = -1$), $\nu_R$ ($Y = 0$), $Q = (u, d)_L$ (colour triplet,
  doublet, $Y = \frac16$), $u_R$ ($Y = \frac23$), $d_R$ ($Y = -\frac13$), with
  $S_\psi = \int d^8x\sqrt{|g|}\,\big[\bar\psi\gamma^M D_M\psi - \mu_\psi\,\bar\psi\psi\big]$, $D_M$ containing the
  same canonical spin connection and the gauge fields. Each species has a bulk mass $\mu_\psi$ (constant on the cell)
  and its own fold condition $\theta_\psi$ (INVENTED assignment): exactly as for $\Psi$, the reduced $x_0$ operator is
  the block $h = -(i/f)\sigma_1\partial_y + \mu_\psi\sigma_2$ and, with the regular tip $b(-L) = 0$, the condition
  $\theta = 0$ leaves the single zero mode $\chi = (e^{f\mu_\psi y}, 0)$ (DERIVED in the Kohn-Sham record), a chiral
  four-dimensional fermion localised at the fold for $\mu_\psi > 0$ and at the tip for $\mu_\psi < 0$. The doublets
  $L, Q$ carry the left-handed zero modes, the singlets $e_R, \nu_R, u_R, d_R$ the right-handed ones (the opposite
  $\gamma^{x_0}$ component, the zero mode $(0, e^{-f\mu_\psi y})$ with the other fold condition $a(0) = 0$ and the
  transformed tip condition $a(-L) = 0$: the map $\chi \to \sigma_2\chi$, $\mu \to -\mu$, fold and tip
  $\theta \to \pi - \theta$ of the Kohn-Sham theorem T3). Gauge-anomaly cancellation of the four-dimensional zero-mode theory is that of one Standard
  Model generation (STANDARD); anomalies of the eight-dimensional bulk theory are OPEN.
* The Higgs field is ABSENT. Electroweak symmetry is broken at the tip by a boundary condition: the tip carries a
  NON-LINEAR sigma field $\Sigma \in SU(2)$, $\Sigma^\dagger\Sigma = 1$, transforming as $\Sigma \to U_L\Sigma U_Y^\dagger$
  (INVENTED for this geometry; the structure is that of the electroweak chiral Lagrangian and of Higgsless boundary
  conditions, STANDARD). $\Sigma$ has no radial mode, hence no Higgs particle; in the unitary gauge $\Sigma = 1$.
  $$ S_{tip} = \int_{y=-L} d^4x\, d^3x_t\sqrt{|g_{tip}|}\Big[\frac{v_\Sigma^2}{4}\mathrm{tr}\big(D_\mu\Sigma^\dagger D^\mu\Sigma\big) - \big(\bar L\,\Sigma\,\Lambda_\ell\,\ell_R + \bar Q\,\Sigma\,\Lambda_q\,q_R + \mathrm{h.c.}\big)\Big] $$
  with the right-handed doublets $\ell_R = (\nu_R, e_R)$, $q_R = (u_R, d_R)$ and the diagonal coupling matrices
  $\Lambda_\ell = \mathrm{diag}(\lambda_\nu, \lambda_e)$, $\Lambda_q = \mathrm{diag}(\lambda_u, \lambda_d)$ (the
  Yukawa structure of the electroweak chiral Lagrangian, gauge invariant because $U(1)_Y$ acts on $\Sigma$ from the
  right).
  The first term gives the $W$ and $Z$ their masses with $m_Z = m_W/\cos\theta_W$ at tree level (custodial $SU(2)$ of
  $\Sigma$); the second gives the fermion masses through the values of the fermion profiles at the tip.
* QCD (STANDARD): the gluons are the massless $x_0$ zero modes of $G^\alpha_M$; below $\Lambda_{QCD}$ the $u$ and $d$
  quarks are confined into protons ($uud$) and neutrons ($udd$), whose masses come from QCD and are inputs of the
  cosmology (section 7).

### 4.4 The mass mechanism (the author's idea, made precise; DERIVED in `FIELD_EQUATIONS.md` section 4)

Every field is expanded on the cell, $\Phi(x) = \sum_n \phi_n(x_1, \dots, x_4)\,u_n(x_0)$, with $u_n$ the eigenfunctions
of its $x_0$ operator (periodic with period $\ell_0$, the fold and tip conditions). The four-dimensional mass is the
eigenvalue, $m_n^2 = \lambda_n$, and the Rayleigh quotient gives
$$ m^2 = \frac{\int dy\, w(y)\,|\partial_y u|^2/f^2 + \dots}{\int dy\, w(y)\,|u|^2},\qquad w(y) = e^{3Hy} \ (\text{the measure } \sqrt{|g|}\,dx_0 \propto e^{3Hy}dy) . $$
For a profile localised within a proper length $\Delta s = f\,\Delta y$ the uncertainty relation on the cell gives
$\langle \hat p^2\rangle \geq \hbar^2/(4\Delta s^2)$ for the hidden momentum in the orthonormal frame (the author's
estimate $m\,c^2 \geq \hbar c/(2\Delta s)$). CORRECTED in version 1.2 (`ANALYSIS.md` sections 3 to 6): in the flat
proper measure $v = e^{3Hy/2}u$ the mass is
$$ m^2 = \langle\hat p^2\rangle + \Big(\frac{3H}{2f}\Big)^2 - \frac{3H}{f}\,\rho(\text{fold}) + \frac{3H}{f}\,\rho(\text{tips}) + (\text{tip field}) , $$
with $\rho$ the normalised proper density: the warp of the extra times, an attractive point term at the fold and
repulsive tip terms (spin 1/2: the bulk mass and the kink of the Jackiw-Rebbi mechanism). The estimate bounds $m$ when
the fold term is absent or repulsive: every odd mode and every excitation, $m \geq 3H/(2f)$. For the zero modes the
fold term cancels the kinetic energy exactly, and the cancellation is protected by gauge invariance, general covariance
and chirality.
* MASSLESS (no $x_0$ dependence, or an exact zero eigenvalue): the graviton, the photon and the gluons (flat profiles of
  unbroken gauge generators), the fold-band quanta of $\Psi$ (the fold zero modes, $\varepsilon = e^{-a_4}|k|$).
* MASSIVE: $W^\pm$ and $Z$ (their profiles bend at the tip, where $\Sigma$ acts), $e$, $\nu$, $u$, $d$ (chiral zero modes
  localised by $\mu_\psi$, lifted by $\lambda_f$ at the tip: $m_f = \lambda_f\,\zeta_{fL}\zeta_{fR}$ with
  $\zeta(\mu)^2 = 2f\mu\,e^{-2f\mu L}/(1 - e^{-2f\mu L})$ the normalised value of the zero mode $(e^{f\mu y}, 0)$ at
  the tip), the bulk-band quanta of $\Psi$ and every excited $x_0$ mode (the Kaluza-Klein tower,
  $m_n \simeq n\pi/(fL)$ for $n \geq 1$).
* Because the profiles depend exponentially on $\mu_\psi f L$, order-one parameters produce the observed hierarchy
  $m_\nu \ll m_e \ll m_u, m_d \ll m_W$ (DERIVED as a fit in `SOLUTION.md`). The hierarchy runs AGAINST the
  uncertainty estimate: a sharper localisation (larger $\mu_\psi fL$) gives a lighter fermion, and the light masses lie
  $10^{-3}$ ($W$) to $10^{-16}$ ($\nu$) below $\hbar c/(2\Delta s)$ (`ANALYSIS.md` section 5).
* The resolved tip (1.3, `GAPS.md` section 2; DERIVED equivalence, INVENTED inner structure). The tip terms are the
  thin-layer limit of a tip layer in which the broken-generator profiles vanish (symmetry breaking by a boundary
  condition) and the chiral wave functions mix. Every mass of UM-1 is then the $x_0$ dependence of a wave function
  relative to the geometric zero mode, $m^2 = \sum P_{\text{region}}\langle\hat p^2\rangle_{\text{region}}$. Three
  classes follow:
  - MASSLESS: flat profiles;
  - HEAVY: dependence across the cell, $m \geq 3H/(2f)$;
  - LIGHT: dependence confined to the tip, where the probability $P_{tip}$ is tiny, so $m_W^2 = P_{tip}\langle\hat p^2\rangle_{tip}$.

  The fermion masses are the exact eigenvalues of the coupled $x_0$ Dirac problem with the tip mixing condition.
* Every $x_0$-generated mass depends on the block size $f$: $m \propto 1/f$ for Kaluza-Klein masses and
  $m \propto \exp(-\mu f L)$ factors for the localised fermions. A deflating block ($h_4 < 0$) therefore makes masses
  drift in time; the model requires $|h_4| \ll \dot a_4$ after the primordial era (section 7; the bound is computed
  in `SOLUTION.md`). The extra times keep deflating (never static), but slowly.

### 4.5 The portal interactions of $\Psi$ with the Standard Model (INVENTED; gauge invariant)

$\Psi$ is neutral, so every interaction with the Standard Model is through gauge-invariant composite operators. The
model contains the lowest ones (eight-dimensional coefficients; the four-dimensional couplings follow from the overlaps
of the $x_0$ profiles):

| | operator | couples $\Psi$ to | cosmological role |
| --- | --- | --- | --- |
| P1 | $\frac{c_V}{\Lambda_D^{6}}\,(\bar\Psi\gamma^M\Psi)\,(\bar\psi\gamma_M\psi)$, $\psi \in \{L, e_R\}$ (1.3; until 1.2 also $Q, u_R, d_R$) | $e$, $\nu$ (vector currents) | the decoupling of the fold band ($N_{eff}$) and the dark-matter relic abundance |
| P2 | $\frac{c_S}{\Lambda_D^{6}}\,(\bar\Psi\Psi)\,\big(\bar\psi_L\Sigma\psi_R + \mathrm{h.c.}\big)\big|_{tip}$ | $e$, $u$, $d$ (scalar densities) | spin-independent dark matter - nucleon scattering |
| P3 | $\frac{\mu_D}{\Lambda_D^{3}}\,\bar\Psi S^{MN}\Psi\, B_{MN}$ | photon and $Z$ ($B = \cos\theta_W A - \sin\theta_W Z$) | dark dipole: dark matter - photon drag, $Z$ decays |
| P4 | $\frac{c_Z}{\Lambda_D^{4}}\,(\bar\Psi\gamma^M\Psi)\,\frac{i v_\Sigma^2}{2}\mathrm{tr}\big(\Sigma^\dagger D_M\Sigma\,\tau^3\big)\big|_{tip}$ | $Z$ (directly) | $Z$-portal |
| P5 | $\frac{c_D}{\Lambda_D^{7}}\,(\bar\Psi\Psi)\,\big(\bar\psi\, i\gamma^M D_M\psi + \mathrm{h.c.}\big)$ | $W^\pm$, $Z$, $\gamma$, gluons with $e, \nu, u, d$ | charged-current contact vertices |

* Charge conservation forbids any gauge-invariant operator in which the neutral $\Psi$ couples to a single $W^\pm$
  without a charged pair of Standard-Model fermions; the $W^\pm$ enter the portal through the covariant derivative of
  P5 (vertices $\bar\Psi\Psi\,W^+\bar e\nu$, $\bar\Psi\Psi\,W^+\bar d u$) and through the gauge self-interactions
  (DERIVED in `FIELD_EQUATIONS.md` section 5).
* CHANGED in version 1.3 (`GAPS.md` section 3): P1 acts on the lepton multiplets only, which is gauge invariant
  multiplet by multiplet. $\Psi$ couples to the quarks through P2, P3, P4 and P5. With this choice, the portal that
  decouples the fold band for $N_{eff} = 2.99$ predicts the dark-matter abundance, $\Omega h^2 = 0.115$ (0.06 to 0.20
  over the QCD crossover), and direct detection is loop-suppressed ($8\times10^{-50}$ cm$^2$).
* The coefficients are free parameters bounded by cosmology and by laboratory limits (`SOLUTION.md` section 6). The
  word CRITICAL of the order is implemented as follows: these are the only couplings through which the dark sector
  exchanges energy and momentum with the visible sector; without them $\Psi$ interacts with the Standard Model only
  through gravity.

## 5. Dimensional reduction (DERIVED at leading order in `FIELD_EQUATIONS.md`)

* The four-dimensional theory is obtained by integrating over the cell and the extra-time block with the zero-mode
  profiles. The reduced Planck mass and gauge couplings carry the proper volume
  $V_\perp = 2\int_{-L}^{0} f\,e^{3Hy}\,dy \times f^3 v_t = 2 f^4 v_t (1 - e^{-3HL})/(3H)$ (2 for the two halves of a
  cell, $v_t$ the coordinate volume of the extra times; their compactness is ASSUMED, normalisation A of the dark-sector
  record): $M_{Pl}^2 = V_\perp/\kappa$, $g^2 = \hat g^2/V_\perp$.
* The extra times are TIME-LIKE. Modes with extra-time momentum $q$ have $\omega^2 = M^2 + k^2 - q^2$ and are tachyonic
  for $q > M$ (DERIVED in the dark-sector record); the model keeps only the good sector $q = 0$ (ASSUMED), as the
  Kohn-Sham record does. The stability of the full theory is OPEN.

## 6. The cosmological inventory

| component | field | $x_0$ mode | equation of state |
| --- | --- | --- | --- |
| photons (CMB) | $A_\mu$ zero mode | flat, massless | $w = 1/3$ |
| neutrinos (CNB) | $\nu_L$ zero mode | localised, $m_\nu \lesssim 0.1$ eV | relativistic, then non-relativistic |
| baryons | $u, d \to p, n$ | localised, QCD | $w = 0$ |
| electrons | $e$ | localised | $w = 0$ after $e^\pm$ annihilation |
| dark matter (CONDITIONAL, `ANALYSIS.md` section 8) | $\Psi$ bulk band, lightest odd level | massive, $\varepsilon \geq m$ | $w = 0$ on the static block; $-0.073$ while the block deflates |
| dark radiation | $\Psi$ fold band | massless zero modes | $w = 1/3$ ($\Delta N_{eff}$) |
| dark condensate | $\bar\Psi\Psi$ | homogeneous | $w_c = \lambda S/(2m + \lambda S)$, drifting; dust-like on the static block, NOT dark energy |
| hidden curvature | geometry, $6H^2 k$, $k = e^{2a_4}/b_4$ | - | acts like a cosmological term when $k$ is constant |
| dark energy | $\delta\Lambda$ (geometric, tuned) | - | $w = -1$; no $\Psi$ component qualifies (`ANALYSIS.md` section 9) |

## 7. What the model predicts and what it requires (statements to be computed)

* The background equations (DERIVED from the record, `FIELD_EQUATIONS.md` section 2): in Einstein gravity the
  $x_4$ constraint is $3\dot a_4^2 + 12\,\dot a_4 h_4 + 6h_4^2 - 6H^2 k = \kappa\rho + \Lambda$ with $k = e^{2a_4}/b_4$:
  a Friedmann equation with the extra term $12\dot a_4 h_4 + 6h_4^2$ of the deflating block and the hidden-curvature
  term $6H^2k$, which is constant when the block is static and acts like a cosmological constant.
* The masses: the $W$, $Z$ and fermion masses are fitted with order-one parameters; the photon, gluon and graviton are
  exactly massless (`SOLUTION.md` section 4).
* CMB, CNB and BAO: computed in the four-dimensional effective theory at order $\epsilon$ (`SOLUTION.md` section 5):
  the neutrino temperature $T_\nu = (4/11)^{1/3}T_\gamma$ (STANDARD, unchanged as long as $\Psi$ does not heat the
  neutrinos), the sound horizon at the drag epoch, the angular acoustic scale and the BAO scale, and the bounds that
  the deflation rate, the dark radiation and the portal couplings must respect.

## 8. Assumptions and open problems (honesty rule)

* ASSUMED: the regular tip at $y = -L$; the compact extra times (normalisation A) and the good sector $q = 0$; the kink
  bulk masses; the tip sigma field; the portal operators; one generation; the zero-mode truncation at order 1; (1.1) the
  block stabiliser and the exact fold-reflection parity that keeps the odd-parity dark matter stable ((1.2) exact to
  $2\times10^{-27}$ in amplitude for a lifetime above $10^{26}$ s, `ANALYSIS.md` section 8.3).
* REQUIRED (1.2, `ANALYSIS.md`): the exponential deflation of the primordial era ends long before nucleosynthesis (the
  electron mass changes like $f^{-22}$); the portal coefficients of the $\Psi$ fold band and of the $\Psi$ dark matter
  differ beyond their overlaps, or the one-half count $g_F = 4$ holds (otherwise the $N_{eff}$ portal makes the dark
  matter under-abundant and puts it at 1.6 times the LZ limit). (1.3: met by the lepton-only P1; the annihilation of
  the dark matter into fold-band pairs through $\lambda$ must stay below $6.7\times10^{-26}$ cm$^3$/s.)
* CHANGED (1.3): the vector portal P1 on the lepton multiplets only (section 4.5); the tip resolved as an $x_0$ layer
  (section 4.4; its inner structure INVENTED, only its strength physical).
* CHANGED (1.1): $w_3 = 1/768$ and $\Lambda = -24H^2 + \delta\Lambda$ (section 4.1). The solution also finds what the
  model requires of the data: $m_{KK} \approx 121$ TeV from $\rho_0$, and, with one generation, a decoupling of the
  $\Psi$ fold band inside the QCD crossover for $N_{eff} \approx 3$ (`SOLUTION.md` sections 4 and 6).
* OPEN: the stability of a theory with three time-like extra dimensions (ghosts and tachyons beyond the good sector);
  perturbative unitarity of $WW$ scattering without a Higgs (it holds up to the Kaluza-Klein scale $\sim \pi/(fL)$ only
  if that scale lies below about $4\pi v_\Sigma \approx 3$ TeV, as in all Higgsless models); a dynamical mechanism that
  slows the deflation of the block after the primordial era; the origin of the second and third generations; the
  derivation of the portal coefficients; the non-adiabatic evolution of $\Psi$; (1.2) the annihilation that fixes the
  dark-matter abundance ($6.5\times10^{-26}$ cm$^3$/s, 37 % of the s-wave unitarity limit; (1.3) supplied by the
  lepton-only P1 within the accuracy of the decoupling estimate, `GAPS.md` section 3).
* Consistency with QCD and the electroweak theory is at the level of the gauge group, the representations, anomaly
  cancellation and the electroweak chiral Lagrangian (no Higgs); precision electroweak constraints on Higgsless
  models (the $S$ parameter) apply and are OPEN for this geometry.

## 9. Analysis of the mass mechanism and of the dark associations (versions 1.2 and 1.3; `ANALYSIS.md`, `GAPS.md`)

* The mass mechanism. Every four-dimensional mass is an eigenvalue of an $x_0$ operator of a wave function periodic
  with $\pi/(6H)$: the author's requirement holds. Without a cutoff each period is a whole line in proper length, and
  every function of $y$ is periodic; the content of the requirement lies in the parities and boundary terms at the fold
  and the tips. The operator factorises as $A^\dagger A$: the mass is the $x_0$ dependence of the profile RELATIVE to the
  geometric zero mode. A mode localised as the geometry dictates is massless, and every deviation costs mass.
* The uncertainty relation is a true lower bound for the $x_0$ excitations ($m \geq 3H/(2f) = 99.4$ TeV; the estimate
  is exceeded by factors 2.6 to 7.5). The dark matter is one of them: 78.9 % of its $\varepsilon^2$ is $x_0$ momentum.
  The Kohn-Sham stress tensor confirms this: its hidden pressure $p_0/\rho = 0.6575394$ equals $-d\ln M_{DM}/d\ln f$ to
  $10^{-9}$.
* The uncertainty relation is not the origin of the light masses. The photon, gluon and graviton zero mode is
  localised within $1.4\times10^{-21}$ m and massless. The $W$ mass is 99.87 % tip term. The fermion masses fall as
  the localisation sharpens. Taken literally as a principle, the Heisenberg argument would put every massive particle
  above 99 TeV.
* Constancy: every $x_0$-generated mass tracks $f$ ($m_e \propto f^{-22}$, $\alpha, G_N \propto f^{-4}$); the late
  block deflation $h_4/A \approx -10^{-93}$ is far within the atomic-clock bound $1.2\times10^{-8}$, and the primordial
  deflation must end before nucleosynthesis.
* Dark matter: CONDITIONAL. The odd bulk quanta are cold on the static block, dark, collisionless and massive. They
  need three things: an exact fold parity (ASSUMED), an annihilation of natural cell strength ($G \approx 1.4/H^2$,
  OPEN), and portal coefficients that are not universal across $\Psi$ modes. The record's computed states are dark
  radiation.
* Dark energy: NOT SUPPORTED. No positive-energy $\Psi$ state has $w < 0$ on the static block. The $\lambda < 0$
  condensate tuned to $w_0 = -1$ has $w_a = -6$, and its energy turns negative at $z = 0.26$. The vacuum energy is the
  cosmological-constant problem. The dark energy of UM-1 is $\delta\Lambda$.
* Version 1.3 (`GAPS.md`) closes two gaps.
  - The light masses: with the tip resolved as an $x_0$ layer, every mass is the $x_0$ dependence of a wave function,
    $m_W^2 = P_{tip}\langle\hat p^2\rangle_{tip}$, and the fermion masses are exact $x_0$ eigenvalues.
  - The dark-matter conditions: the lepton-only P1 resolves the portal tension and predicts
    $\Omega_{DM}h^2 = 0.115$ from the $N_{eff}$ requirement.
