# UM-1: the coupled field equations

Version 1.1 of 2026-10-17, for the model of `MODEL.md` (1.1: the statement of check D3 in section 5 corrected after `ANALYSIS.md`). Derived by `field_equations/derive_field_equations.py` (sympy;
13 checks, all PASS, 2.7 s; outputs `field_equations/field-equations.json` with every equation as a sympy string and
`field_equations/reports/field-equations-checks.json`). Labels as in `MODEL.md`: DERIVED (computed here), TAKEN (from
the Revision record), ASSUMED, OPEN. Run: `python Revision/universe_model/field_equations/derive_field_equations.py`.

## 1. Notation

The author's coordinates $x_0, \dots, x_7$ ($x_0$ hidden, period $\ell_0 = \pi/(6H)$; $x_4$ the time). The hidden
coordinate $y = \ln|\sin z|/(6H) \in [-L, 0]$ on each half of the cell ($dy = \cot z\,dx_0$, fold $y = 0$, regular tip
$y = -L$). The background functions $a_4(x_4)$, $b_4(x_4)$; dots or primes on them are $d/dx_4$;
$u = \dot b_4/b_4$, $v = \dot u$, $k = e^{2a_4}/b_4$; the block scale factor $f = e^{-a_4}b_4^{1/2}$ and its rate
$h_4 = \dot f/f = u/2 - \dot a_4$.

In the $y$ chart the background metric is, for EVERY real $z$ (DERIVED, check A3 and the chart remark of the script),

$$ \bar g = \mathrm{diag}\big(e^{-2a_4}b_4,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\ -1,\ -e^{-2a_4}b_4e^{2Hy},\ -e^{-2a_4}b_4e^{2Hy},\ -e^{-2a_4}b_4e^{2Hy}\big), $$

because $g_{00}dx_0^2 = e^{-2a_4}b_4\,dy^2$ and $(\sin^2 z)^{1/6} = e^{2Hy}$; the measure is
$\sqrt{|g|}\,dx_0 = e^{-a_4}b_4^2e^{3Hy}\,dy$ (check A3). The mixed tensor components are the same in both charts.

## 2. Gravity: the background (order $\epsilon^0$)

* The Einstein tensor, recomputed here from the metric with its own Christoffel symbols, equals the record
  (`Revision/field_equations_a4/a4-equations.json`, key einstein; check A1):
  $$ G^{x_4}{}_{x_4} = 3\dot a_4^2 + 6H^2k - \tfrac32 u^2,\quad G^{x_1}{}_{x_1} = -5\dot a_4^2 + 2\ddot a_4 + 6\dot a_4u - \tfrac52u^2 - 2v + 6H^2k,\quad G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5} = -3\dot a_4^2 + \tfrac32\dot a_4u - \tfrac32u^2 - \tfrac32 v + 3H^2k $$
  and every off-diagonal component vanishes.
* The Einstein-Lovelock equations $\sum_k\alpha_k E_{(k)}{}^M{}_N + \Lambda\delta^M_N = \kappa T^M{}_N$ have three
  independent components, $x_4$ (a first-order CONSTRAINT), $x_1 = x_2 = x_3$ and $x_0 = x_5 = x_6 = x_7$ (the latter two
  linear in $(\ddot a_4, v)$); their full forms with the author's weights are TAKEN from the record (generalSource:
  constraint_x4, space_x1_eq_x2_eq_x3, hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7), and `SOLUTION.md` integrates them.
* With $u = 2(h_4 + \dot a_4)$ the Einstein constraint reads (check A2)
  $$ 3\dot a_4^2 + 12\,\dot a_4h_4 + 6h_4^2 - 6H^2k = \kappa\rho + \Lambda . $$
  For a static block ($h_4 = 0$) it is the Friedmann equation with the effective cosmological constant
  $\Lambda_{eff} = \Lambda + 6H^2k$.
* The source must be diagonal, independent of $x_0$ and have $p_0 = p_t$ (TAKEN: hiddenEqualsExtraTimes, offDiagonal,
  x0_dependence). Sources that violate this at a small level (the interacting Kohn-Sham states of $\Psi$, the
  localised Standard-Model fermions) drive the $x_0$-dependent and the block-anisotropic metric corrections of
  order $\epsilon$ and higher (OPEN beyond the zero-mode averages used in `SOLUTION.md`).

## 3. Sources, species and the four-dimensional observer

* Every species $i$ (photons, neutrinos, electrons, baryons, the $\Psi$ components) contributes $(\rho_i, p_{3i},
  p_{0i} = p_{ti})$; each obeys (check B1)
  $$ \dot\rho_i = -3\dot a_4(\rho_i + p_{3i}) - 4h_4(\rho_i + p_{0i}) + Q_i,\qquad \sum_i Q_i = 0, $$
  with $Q_i$ the energy exchanged through the portal interactions. The four-dimensional density
  $\rho_{4i} = V_\perp\rho_i$, $V_\perp \propto f^4$, obeys $\dot\rho_{4i} = -3\dot a_4(\rho_{4i} + p_{3,4i}) - 4h_4
  p_{0,4i} + Q_{4i}$: the standard law for every species without hidden or extra-time pressure.
* The observer's Friedmann equation (Einstein part): $3\dot a_4^2 = \rho_4/M_{Pl}^2 + \Lambda_{eff} - 12\dot a_4h_4 -
  6h_4^2$ with $M_{Pl}^2 = V_\perp/\kappa = 2f^4v_t(1 - e^{-3HL})/(3H\kappa)$.
* The drifts (check B2): $\dot k = -2kh_4$ and $(f^4)^\cdot = 4h_4f^4$. A deflating block changes $\Lambda_{eff}$, the
  Planck mass and every $x_0$-generated mass ($\propto 1/f$): the observations need $|h_4| \ll \dot a_4$ after the
  primordial era.
* The block is NOT free: the $x_0$ component is its equation of motion. For a static block and Einstein gravity it
  reduces to $6\dot a_4^2 + 3\ddot a_4 = 3H^2k + \Lambda - \kappa p_0$; matter with $p_0 = 0$ in an expanding
  universe cannot keep the left-hand side constant, so the Standard-Model matter DRIVES the block (the radion problem of
  every compactification). `SOLUTION.md` integrates the full system.

## 4. Gravity at order $\epsilon$: scalar perturbations

The metric $g = \bar g + \epsilon\,\delta g$ with $\delta g_{44} = -2\Phi$, $\delta g_{ii} = -2\Psi_Ne^{2a_4}$
($i = 1, 2, 3$), $\delta g_{00} = 2\sigma\bar g_{00}$, $\delta g_{tt} = 2\sigma\bar g_{tt}$ ($t = 5, 6, 7$), with
$\Phi, \Psi_N, \sigma$ functions of $(x_4, x_1)$ (zero modes of $x_0$; one Fourier direction suffices for the scalar
sector). The linearised Einstein tensor, computed from the metric (check C1; free of $x_0$; $\delta G^{x_4}{}_{x_0} =
\delta G^{x_1}{}_{x_0} = 0$; $\delta G^{x_0}{}_{x_0} = \delta G^{x_5}{}_{x_5}$), with $\nabla^2 = e^{-2a_4}\partial_1^2$:

$$ \delta G^4{}_4 = 3\big(u^2 - 2\dot a_4^2\big)\Phi + 3(2u - 2\dot a_4)\dot\Psi_N - 6u\dot\sigma - 12H^2k\sigma - 2\nabla^2\Psi_N + 4\nabla^2\sigma $$

$$ \delta G^4{}_1 = \partial_1\big[2(\dot a_4 - u)\Phi - 2\dot\Psi_N + (2u - 8\dot a_4)\sigma + 4\dot\sigma\big] $$

$$ \delta G^1{}_1 - \delta G^2{}_2 = \nabla^2\big(\Psi_N - \Phi - 4\sigma\big) $$

The full $\delta G^1{}_1$ and $\delta G^0{}_0 = \delta G^5{}_5$ are in `field-equations.json` (key order_epsilon_scalar).
The equations are $\delta G^M{}_N = \kappa\,\delta T^M{}_N$ ($\delta T^4{}_4 = -\delta\rho$, $\delta T^4{}_1$ the momentum
density, $\delta T^1{}_1 = \delta p_3$, $\delta T^0{}_0 = \delta T^5{}_5 = \delta p_0$).

* Static block, no radion (check C2): $\delta G^4{}_4 = 6\dot a_4(\dot\Psi_N + \dot a_4\Phi) - 2\nabla^2\Psi_N$ and
  $\delta G^4{}_1 = -2\partial_1(\dot\Psi_N + \dot a_4\Phi)$: the Newtonian-gauge equations of four-dimensional
  general relativity with $H_{obs} = \dot a_4$. The CMB and BAO physics of `SOLUTION.md` uses this limit.
* Without anisotropic stress the slip is $\Psi_N = \Phi + 4\sigma$ (DERIVED): a radion perturbation is observable as a
  gravitational slip.
* The Gauss-Bonnet and cubic Lovelock contributions at order $\epsilon$, and the vector and tensor sectors, are OPEN in
  version 1; at late times their background coefficients enter through $\alpha_2\dot a_4^2$, $\alpha_2H^2k$ and the
  like (the record's components), which `SOLUTION.md` evaluates.

## 5. The $x_0$ mass mechanism (the author's idea, as equations)

* Gauge fields (check D1): a four-dimensional component $A_\mu(x)u(y)$ (gauge $A_{x_0} = 0$) has, on each half of the
  cell, the action $\int_{-L}^0 dy\,e^{3Hy}\big[u'^2/f^2 - m^2u^2\big] + c_{tip}u(-L)^2$, hence
  $$ -\frac{1}{f^2}e^{-3Hy}\big(e^{3Hy}u'\big)' = m^2u,\qquad u'(0) = 0,\qquad \frac{e^{-3HL}}{f^2}u'(-L) = c_{tip}\,u(-L) . $$
* Massless zero modes (check D2): $c_{tip} = 0$ admits $u = $ const, $m = 0$: the photon, the gluons and (for $g_{MN}$)
  the graviton. To first order in $c_{tip}$: $m^2 = c_{tip}/\int_{-L}^0 e^{3Hy}dy = 3Hc_{tip}/(1 - e^{-3HL})$; the tip
  sigma field gives $c_{tip}(W) = \hat g^2v_\Sigma^2w_{tip}/4$, $c_{tip}(Z) = (\hat g^2 + \hat g'^2)v_\Sigma^2w_{tip}/4$,
  $c_{tip}(\gamma) = 0$, so $m_Z/m_W = 1/\cos\theta_W$ ($\rho = 1$) at this order; the bending of the profiles beyond it
  is computed in `SOLUTION.md`.
* Fermions (check D4): the block $h = -(i/f)\sigma_1\partial_y + \mu\sigma_2$ annihilates $(e^{f\mu y}, 0)$ (fold
  $b(0) = 0$, tip $b(-L) = 0$; left-handed) and $(0, e^{-f\mu y})$ (fold $a(0) = 0$, tip $a(-L) = 0$; right-handed,
  theorem T3). Their normalised tip values are $\zeta(\mu)^2 = 2f\mu\,e^{-2f\mu L}/(1 - e^{-2f\mu L})$, and the tip
  coupling gives $m_f = \lambda_f\,\zeta(\mu_L)\,\zeta(\mu_R)$: exponentially small masses for $f\mu L \gg 1$.
* The uncertainty relation (check D3): on a flat line, $\langle p^2\rangle\,\Delta s^2 \geq 1/4$ with equality for a
  Gaussian, which is the author's estimate $m \geq \hbar/(2c\,\Delta s)$ when $m^2 = \langle p^2\rangle$. CORRECTED
  (`ANALYSIS.md` sections 3 to 6): in the warped cell the Rayleigh quotient of a bosonic mode is the WEIGHTED mean
  $\int e^{3Hy}|\partial_su|^2/\int e^{3Hy}|u|^2$, the hidden momentum relative to the geometric zero mode, not the mean
  squared momentum $\langle\hat p^2\rangle$ of the proper density. In the flat measure
  $m^2 = \langle\hat p^2\rangle + (3H/2f)^2 - (3H/f)\rho(\text{fold}) + (3H/f)\rho(\text{tips}) + (\text{tip field})$.
  The estimate is a bound for every odd mode and excitation ($m \geq 3H/(2f)$). It fails for the zero modes: the photon,
  gluon and graviton zero mode is localised at the fold within $\Delta s = 0.157\,fL$ and massless. A CHIRAL fermion
  zero mode behaves the same way: its hidden momentum is cancelled by the bulk mass ($h\chi = 0$), it is massless
  however localised it is, and its mass comes from its value at the tip (DERIVED; `SOLUTION.md` section 4 quantifies
  it).

## 6. dirac16complex: the Kohn-Sham equations coupled to all fields

The good-sector reduction of the record (TAKEN, `Revision/kohn_sham/ks-theory.json`) with the portal mean fields
(DERIVED from P1, P2, P5 of `MODEL.md`):

$$ h_j = j\big[-(i/f)\sigma_1\partial_y + M_{eff}(y)\sigma_2 + \kappa k\sigma_3\big] + v_v(y),\qquad \kappa = e^{-a_4}, $$

$$ M_{eff} = m + \tfrac{15}{16}\lambda S(y) + g_S\sum_f s_f\,\delta_{tip}(y) + g_D\sum_f m_f s_f(y),\qquad v_v = -\tfrac{1}{16}\lambda n(y) + g_V\sum_f q_f n_f(y), $$

with $n_f(y) = n_f|\chi_f(y)|^2$ the Standard-Model fermion densities in their $x_0$ zero modes, $s_f$ their scalar
densities, $g_V = c_V/\Lambda_D^6$, $g_S = c_S/\Lambda_D^6$, $g_D = c_D/\Lambda_D^7$. P3 and P4 have no mean field in a
neutral, unpolarised background with $\Sigma = 1$ and act through scattering. The back-reaction: the Standard-Model
masses shift by $g_SS_\Psi(-L)\zeta_L\zeta_R + g_Dm_f\langle S_\Psi\rangle_f$, the vector potentials by
$g_Vq_fn_\Psi(y)$, and the gravitational source is the total $T^M{}_N$ (the portal energy counted once). The
Kohn-Sham energy-momentum of $\Psi$ ($\rho = \sum wgf\varepsilon n_o - e_{int}$, $p_3$, $p_t = e_{int}$, $p_0$; record)
enters section 3 as one species; its $p_0 \neq p_t$ in interacting states is a source of order-$\epsilon$ block
anisotropy.

## 7. The Standard-Model equations (ASSUMED structure, standard form in the curved eight-dimensional background)

* Fermions: $\gamma^MD_M\psi - \mu_\psi\psi - (\text{tip terms})\,\delta_{tip} - (\text{portal terms}) = 0$ with
  $D_M = \partial_M + \Omega_M - i\hat g_sG^\alpha_MT^\alpha - i\hat gW^a_M\tau^a/2 - i\hat g'YB_M$.
* Gauge fields: $\frac{1}{\sqrt{|g|}}\partial_M\big(\sqrt{|g|}F^{MN}\big) + [\,A_M, F^{MN}] = J^N_{SM} + J^N_{portal} +
  J^N_{tip}\delta_{tip}$, with the portal current of P3, $J^N \ni \frac{\mu_D}{\Lambda_D^3}\nabla_M(\bar\Psi
  S^{MN}\Psi)$ for $B$, and the sigma-field current at the tip.
* The tip sigma field: $D_\mu\big(\Sigma^\dagger D^\mu\Sigma\big) = 0$ plus the fermion and portal terms (its
  equation of motion; unitary gauge $\Sigma = 1$).

## 8. Gauge invariance and the $W$

* The tip Yukawa terms $\bar L\Sigma\Lambda_\ell\ell_R$, $\bar Q\Sigma\Lambda_qq_R$ and the operator
  $\mathrm{tr}(\Sigma^\dagger D\Sigma\tau^3)$ are invariant under $SU(2)_L\times U(1)_Y$ to $10^{-15}$ in an explicit
  representation with 20 random group elements (check E1); P1, P3, P5 are products of the singlet
  $\bar\Psi\Gamma\Psi$ with invariant Standard-Model operators.
* A $\Psi$ bilinear is neutral, so a vertex with one $W^\pm$ needs a charged Standard-Model pair: the $W$ enters the
  portal only through the covariant derivative of P5 and through the gauge self-couplings (check E2).

## 9. The coupled system

| equation | unknowns | couples to |
| --- | --- | --- |
| Einstein-Lovelock background (3 components) | $a_4$, $b_4$ | every species through $\rho, p_3, p_0 = p_t$ |
| species conservation | $\rho_i$ | $a_4$, $h_4$, the portal exchanges $Q_i$ |
| order-$\epsilon$ scalar equations | $\Phi$, $\Psi_N$, $\sigma$ | $\delta\rho_i$, velocities, $\delta p_{0}$ |
| $x_0$ eigenproblems | masses, profiles | $f$ (hence $h_4$), $H$, $L$, $c_{tip}$, $\mu_\psi$, $\lambda_f$ |
| Kohn-Sham equations of $\Psi$ | levels, $n$, $S$ of $\Psi$ | the Standard-Model densities (portals), $a_4$, $f$ |
| Standard-Model field equations | $\psi$, $A$, $\Sigma$ | $\Psi$ (portals), the metric |

OPEN in version 1: the Lovelock terms and the vector and tensor sectors at order $\epsilon$; the $x_0$-dependent
metric response to the localised sources; the derivation of the portal and tip coefficients.

## 10. Checks (`field_equations/reports/field-equations-checks.json`, 13 of 13 PASS)

A1 background Einstein tensor = record; A2 constraint in $h_4$; A3 the measure in $y$; B1 four-dimensional
conservation; B2 the drifts of $k$ and the Planck mass; C1 linear scalar perturbations; C2 the static-block limit is
four-dimensional general relativity, slip $\Psi_N = \Phi + 4\sigma$; D1 the gauge $x_0$ operator and its boundary
conditions; D2 massless zero modes, the leading $W$, $Z$ masses, $\rho = 1$; D3 the uncertainty bound on a flat line (corrected for the warped cell in `ANALYSIS.md`); D4 the fermion
zero modes and tip values; E1 gauge invariance; E2 the $W$ and charge conservation.
