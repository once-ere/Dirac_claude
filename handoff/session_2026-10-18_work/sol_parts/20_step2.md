# Step 2: the masses from the $x_0$ dependence of the wave functions

Every four-dimensional mass of UM-2 is an eigenvalue of the $x_0$ operator of its field on the static block of step 1. The
eigenfunctions depend on $x_0$ through $y(z)$, $z = 6Hx_0$, and are periodic with the period $\pi/(6H)$ (the author's
requirement): a field that is localised in $x_0$ carries an $x_0$ momentum and hence a four-dimensional mass, while a flat
profile is massless. Step 2 solves the field equations of the gauge bosons, the graviton, the twelve fermions of three
generations and dirac16complex for their $x_0$ eigenvalues.

## The field equations of step 2

**Gauge bosons and the graviton.** The gauge fields of the Standard Model live in the eight dimensions; the tip sigma field
$\Sigma$ (no radial mode, hence no Higgs particle) gives $W^+$, $W^-$ and $Z$ a mass term at the tip $y = -L$ and the photon
none:

@@T:The gauge fields of SU(3)@@

@@T:The physical electroweak fields@@

@@T:The tip sigma field and the tip Yukawa@@

@@T:The tip mass term@@

The Yang-Mills equations of the gluons, of the $SU(2)$ field and of the hypercharge field, with the fermion currents and the tip
current:

@@ym_gluon@@

@@ym_su2@@

@@ym_b@@

To linear order in the fields (the non-abelian terms and I12 neglected, as for a mass eigenvalue), they become the field
equations of $W^+$, $W^-$, $Z$ and the photon with their tip mass terms (the gluon equation, which has no tip term, is that of the
photon with the colour index):

@@ym_lin@@

@@bc_boson@@

**The fermions of three generations.** The quark and lepton multiplets have bulk masses $\mu_{\psi i}$ (the doublets of a
sector share one) and are mixed at the tip by the tip Yukawa couplings:

@@T:The Standard-Model fermions: three generations@@

@@dirac_Q@@

@@dirac_uR@@

@@dirac_dR@@

@@dirac_l@@

@@dirac_eR@@

@@dirac_nuR@@

@@bc_sm@@

@@bc_tip@@

**dirac16complex** obeys its own Dirac equation with the canonical spin connection, the self-coupling and the portals; for
its free spectrum the self-coupling and the portal fields are set to zero (their effect is step 3 and step 8):

@@dirac16@@

@@bc_psi@@

## The approximation of step 2

The $x_0$ reductions below are exact on the static block (order 0 of the metric series): no approximation enters the
eigenvalue problems themselves, and the eigenvalues are computed as exact roots. What step 2 leaves out is, first, *the mixing of the zero modes with the Kaluza-Klein modes* through the interactions, of
the relative size $(m/m_{\mathrm{KK}})^2$, largest for the top quark:

$$
\Big(\frac{m_{\mathrm{t}}}{m_{\mathrm{KK}}}\Big)^2 = 2.0\times10^{-6}
$$

<!-- symbols: AUTO -->

It further leaves out the following.

* *Radiative corrections.* The masses are tree-level eigenvalues fitted to the measured values used as tree-level targets;
  the electroweak parameter $\rho_{\mathrm{EW},0} - 1 = 3.8\times10^{-4}$ is fitted, not computed from loops.
* *The mean fields of the environment.* The $W$ eigenvalue moves by the dark-matter kinetic function of step 8 by at most
  $1.9\times10^{-17}$ of itself (at the dark-matter freeze-out), and the dark-matter level by the Standard-Model mean fields by
  at most $1.5\times10^{-6}$ of itself (step 8).
* *The Lovelock corrections to the graviton operator* are not estimated (OPEN): the graviton profiles below are those of
  Einstein gravity on the block.

The first-order formula of the fermion masses (written out below) is not used for the masses; it differs from the exact
roots by up to $1.1\times10^{-3}$ (top quark) and serves for the block sensitivities of step 8.

## The solution of step 2

### The $x_0$ eigenvalue problem of the gauge bosons and the graviton

A four-dimensional component with the $x_0$ profile $F(y)$ (in the gauge with no $y$ component) has a reduced action whose
stationarity gives a Sturm-Liouville problem in $\xi = y/L$; the tip mass term becomes the Robin condition at $\xi = -1$
(DERIVED):

@@x0_boson@@

@@x0_boson_bc@@

@@x0_boson_eig@@

The operator with $\beta = 0$ is also the $x_0$ operator of the graviton; its levels form the Kaluza-Klein tower, whose first level
fixes the scale $m_{\mathrm{KK}}$ of UM-2:

@@kk_tower@@

With the depth of the cell $HL = 3$ (ASSUMED) the eigenvalues are (DERIVED):

| mode ($HL = 3$) | $\tilde m^2 = (m\,fL)^2$ | status |
| --- | --- | --- |
| photon, gluons, graviton ($\beta = 0$, flat profile) | $0$ exactly | DERIVED |
| first even Kaluza-Klein level | $9H^2L^2/4 + \pi^2 = 30.1196$ | DERIVED (finite elements $1.9\times10^{-10}$) |
| first odd level | $27.0890$ ($\varpi\cot\varpi = -9/2$) | DERIVED (finite elements $4.5\times10^{-10}$) |
| gap | $9H^2L^2/4 = 20.25$ | DERIVED |
| $W^+$, $W^-$ ($\beta_{\mathrm{W}} = 0.011912$) | $1.32149\times10^{-5}$ | DERIVED (fit; finite elements $3\times10^{-14}$) |
| $Z$ ($\beta_{\mathrm{Z}} = \beta_{\mathrm{W}}/\cos^2\theta_{\mathrm{W}} = 0.015343$) | $1.70150\times10^{-5}$ | DERIVED |
| Dirichlet bound ($\beta \to \infty$) | $0.010016$: $m_{\mathrm{W}} \le 0.01824\,m_{\mathrm{KK}}$ | DERIVED |

Here $\theta_{\mathrm{W}}$ is the angle of the couplings, $\cos^2\theta_{\mathrm{W}} = \hat g_2^2/(\hat g_2^2 + \hat g_1^2)$. The
bending of the tip-localised profiles moves the mass ratio $m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2 = \tilde m_{\mathrm{W}}^2/\tilde
m_{\mathrm{Z}}^2$ away from $\cos^2\theta_{\mathrm{W}}$, so the electroweak parameter exceeds 1: $\rho_{\mathrm{EW}} - 1 =
3.2\times10^{-8}$ at $\beta_{\mathrm{W}} = 10^{-6}$ (custodial symmetry at leading order), $6.4\times10^{-5}$ at
$\beta_{\mathrm{W}} = 0.002$, $3.2\times10^{-3}$ at $0.1$. This tree-level custodial violation is fitted to the measured
$\rho_{\mathrm{EW},0} - 1 = 0.00038$ (the violation beyond the Standard-Model loops), and the angle of the couplings is fixed
by the measured masses:

@@wz_fit@@

i.e. $\cos^2\theta_{\mathrm{W}} = 0.776368$ (the on-shell ratio $m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2 = 0.776663$); both masses
are then reproduced. With $m_{\mathrm{W}} = 80.3625$ GeV (STANDARD, PDG 2026) the scales of UM-2 are (DERIVED):

| quantity | value |
| --- | --- |
| first Kaluza-Klein level $m_{\mathrm{KK}} = m_{\mathrm{W}}\,\tilde m_1/\tilde m_{\mathrm{W}}$ | $121.32$ TeV |
| the author's constant $H = 3f_*\,m_{\mathrm{KK}}/\tilde m_1$ | $14.296$ TeV |
| proper half cell $fL$; period of $x_0$, $\pi/(6H)$ | $8.926\times10^{-21}$ m; $7.227\times10^{-21}$ m |
| gap $3H/(2f_*)$ | $99.48$ TeV |
| radion mass $\omega_{\mathrm{r}} = 3.387\,H$ | $48.42$ TeV |
| $m_{\mathrm{Z}} = m_{\mathrm{W}}\,\tilde m_{\mathrm{Z}}/\tilde m_{\mathrm{W}}$ | $91.1879$ GeV (the measured value, reproduced) |

### The fermions: the exact reduction and the zero modes

With the factors of the ansatz below, the eight-dimensional Dirac equation, the canonical spin connection included, is
EXACTLY a two-component equation in each of the eight blocks of the spinor (DERIVED, all blocks, general $a_4(x_4)$,
$b_4(x_4)$, $M(y)$, $v(y)$):

@@ferm_red@@

For a Standard-Model multiplet $M = \mu_{\psi i}$ and $v = 0$; the zero modes are massless four-dimensional particles:

@@ferm_zero@@

### The masses of one generation

At $k = 0$ the doublet and singlet solutions that satisfy the fold conditions reach the tip with closed-form values, and the
tip mixing conditions give the exact mass condition (DERIVED):

@@ferm_k0@@

@@ferm_1gen@@

### Three generations: the masses and the mixing matrices

For three generations the tip conditions hold for the vectors of boundary values over the generations; for one doublet bulk
mass per sector and a unitary tip matrix the determinant factorises into the one-generation conditions with
$\mathcal{K} = 1$ (DERIVED, mpmath with 50 digits):

@@ferm_3gen@@

The masses are therefore the one-generation roots with $\mathcal{K} = 1$, the left-handed rotation of each sector is its tip
matrix, and $U = \mathcal{K}_e^\dagger\mathcal{K}_\nu$, $V_{\mathrm{CKM}} = \mathcal{K}_u^\dagger\mathcal{K}_d$; UM-2 takes
$\mathcal{K}_e = \mathcal{K}_u = 1$, $\mathcal{K}_\nu = U$, $\mathcal{K}_d = V_{\mathrm{CKM}}$ (ASSUMED). With one doublet bulk
mass per sector, fixed by the heaviest member with $c_R = -c_L$ ($\tau$, t), the masses require (DERIVED, exact roots):

| fermion | mass | doublet $c_L$ | singlet $c_R$ | $\mu_{\psi i}/H$ (singlet) | singlet width $fL/(2\lvert c_R\rvert)$ | $\tilde\varepsilon = m\,fL$ | first order |
| -- | --- | --- | --- | --- | --- | --- | -- |
| $\nu_1$ | $1.000$ meV | $5.95288$ | $-35.04518$ | $-54.194$ | $1.27\times10^{-22}$ m | $4.5235\times10^{-17}$ | $5.7\times10^{-7}$ |
| $\nu_2$ | $8.712$ meV | $5.95288$ | $-32.84810$ | $-50.796$ | $1.36\times10^{-22}$ m | $3.9409\times10^{-16}$ | $6.1\times10^{-7}$ |
| $\nu_3$ | $50.140$ meV | $5.95288$ | $-31.07017$ | $-48.047$ | $1.44\times10^{-22}$ m | $2.2681\times10^{-15}$ | $6.5\times10^{-7}$ |
| e | $0.51100$ MeV | $5.95288$ | $-14.55391$ | $-22.506$ | $3.07\times10^{-22}$ m | $2.3115\times10^{-8}$ | $1.4\times10^{-6}$ |
| $\mu$ | $105.658$ MeV | $5.95288$ | $-8.98093$ | $-13.888$ | $4.97\times10^{-22}$ m | $4.7795\times10^{-6}$ | $2.2\times10^{-6}$ |
| $\tau$ | $1776.93$ MeV | $5.95288$ | $-5.95288$ | $-9.205$ | $7.50\times10^{-22}$ m | $8.0380\times10^{-5}$ | $6.8\times10^{-6}$ |
| u | $2.16$ MeV | $3.38230$ | $-15.43001$ | $-23.861$ | $2.89\times10^{-22}$ m | $9.7708\times10^{-8}$ | $1.3\times10^{-4}$ |
| c | $1.2730$ GeV | $3.38230$ | $-8.76830$ | $-13.559$ | $5.09\times10^{-22}$ m | $5.7585\times10^{-5}$ | $2.2\times10^{-4}$ |
| t | $172.56$ GeV | $3.38230$ | $-3.38230$ | $-5.230$ | $1.32\times10^{-21}$ m | $7.8058\times10^{-3}$ | $1.1\times10^{-3}$ |
| d | $4.70$ MeV | $3.38230$ | $-14.62578$ | $-22.617$ | $3.05\times10^{-22}$ m | $2.1261\times10^{-7}$ | $1.3\times10^{-4}$ |
| s | $93.5$ MeV | $3.38230$ | $-11.51582$ | $-17.808$ | $3.88\times10^{-22}$ m | $4.2295\times10^{-6}$ | $1.7\times10^{-4}$ |
| b | $4.183$ GeV | $3.38230$ | $-7.50053$ | $-11.599$ | $5.95\times10^{-22}$ m | $1.8922\times10^{-4}$ | $2.6\times10^{-4}$ |

(the last column is the relative difference of the first-order root $\mathcal{K}\,\mathcal{Z}(c_L)\mathcal{Z}(-c_R)$ from the
exact root; the doublets have $\mu_\ell = 9.2055\,H$ and $\mu_Q = 5.2304\,H$; the masses are the PDG values, the light-quark
masses in $\overline{\mathrm{MS}}$ at 2 GeV, $m_{\mathrm{c}}(m_{\mathrm{c}})$, $m_{\mathrm{b}}(m_{\mathrm{b}})$ and the directly
measured $m_{\mathrm{t}}$, used as tree-level targets; $m_1$ is ASSUMED and $m_2$, $m_3$ follow from the NuFIT 6.0 splittings
of step 5; the masses are STANDARD inputs, PDG 2025.) The mixing matrices have the standard form

@@pmns@@

with the NuFIT 6.0 values $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{23} = 0.470$, $\sin^2\theta_{13} = 0.02215$,
$\delta_{\mathrm{CP}} = 212^\circ$ ($J_{\mathrm{CP}} = -0.01777$; its largest value over the phase, $0.0335$ for these best-fit
angles, against NuFIT's marginalised $0.0333 \pm 0.0007$) for the PMNS matrix $U$, and the PDG values $s_{12} = 0.22501$,
$s_{13} = 0.003732$, $s_{23} = 0.04183$, $\delta_{\mathrm{CP}} = 1.147$ ($J_{\mathrm{CP}} = 3.117\times10^{-5}$) for the CKM
matrix $V_{\mathrm{CKM}}$, both unitary to $1.1\times10^{-16}$ (DERIVED). The first even Kaluza-Klein gauge mode couples to the
zero modes with the overlaps $0.14434$ (every left-handed lepton) and $-0.30066$ (every left-handed quark) relative to the
zero mode, and in the mass basis its largest off-diagonal coupling is $1.0\times10^{-17}$: no tree-level flavour-changing
neutral current (with the three charged-lepton $\lvert c_R\rvert$ used as different doublet localisations it would be $0.033$).
The rare decay $\mu \to e\gamma$, through the neutrino masses alone, has the branching ratio (flavour indices $\alpha = \mu$,
$\beta = e$)

$$
\mathrm{BR} = \frac{3\alpha_{\mathrm{em},0}}{32\pi}\Big\lvert\sum_{i=1}^{3}U_{\alpha i}^*U_{\beta i}\,\frac{m_i^2}{m_{\mathrm{W}}^2}\Big\rvert^2
 = 2.8\times10^{-55}
$$

<!-- symbols: AUTO -->

(DERIVED).

### The spectrum of dirac16complex

With $M = m_\Psi$ and $v = 0$ the exact spectrum at $k = 0$ is (DERIVED):

@@psi_spectrum@@

At the stabilised block $c_\Psi = f_*m_\Psi L = 0.646667$: the fold zero mode ($\varepsilon = 0$, all eight blocks); the even
bulk levels, the lowest $4.959981\,m_\Psi$; the odd levels, the lowest $3.102204\,m_\Psi$ ($\varpi/(fL) = 2.93661\,m_\Psi$,
$\varpi = 1.89901$), which is the dark matter of UM-2 (steps 3, 7, 9); and the fold band $\varepsilon = \mathrm{e}^{-a_4}\lvert
k\rvert$, massless, $\varepsilon/\lvert k\rvert = 1$ to $6\times10^{-14}$.

## The check of step 2

**In its own equations.**

* *The boson eigenvalues.* Every stored eigenvalue, substituted into its exact characteristic equation, has the implied
  relative error $\lvert F/(\tilde m^2\,\partial F/\partial\tilde m^2)\rvert$ (for the condition $F(\tilde m^2) = 0$) of at most
  $5.9\times10^{-12}$ ($W$; $Z$ $1.4\times10^{-12}$, the Kaluza-Klein levels $2.4\times10^{-13}$ to $1.8\times10^{-12}$, the
  Dirichlet bound $2.0\times10^{-12}$); the flat profile solves the problem with $\beta = 0$ and $\tilde m = 0$ exactly; finite
  elements agree to $5\times10^{-10}$ (DERIVED).
* *The fermion roots.* The implied relative root error $\lvert\mathcal{D}/(\tilde\varepsilon\,\mathrm{d}\mathcal{D}/
  \mathrm{d}\tilde\varepsilon)\rvert$ of the twelve stored roots is at most $5.4\times10^{-11}$ ($\nu_1$; $10^{-13}$ for $\tau$),
  and the three-generation determinant at the stored roots of the four sectors is zero to $1.2\times10^{-11}$ in the same
  measure; the roots of the $3\times3$ determinant agree with the one-generation roots, both refined in the same computation,
  to $3.0\times10^{-42}$, and the null vectors with the columns of the tip matrix to $1.1\times10^{-16}$; direct shooting of
  the coupled Dirac system agrees with the determinant to $6.1\times10^{-10}$ (e), $1.5\times10^{-11}$ ($\tau$),
  $5.6\times10^{-12}$ (t); for a random complex non-unitary tip matrix the exact roots agree with the singular values of
  $\mathcal{Z}(c_L)\,\mathcal{K}\,\mathrm{diag}(\mathcal{Z}(-c_{Ri}))$ to $3.5\times10^{-5}$, $2.8\times10^{-6}$, $2.0\times10^{-6}$
  (DERIVED).
* *The spectrum of dirac16complex.* The stored odd level, its $x_0$ momentum and the lowest even level agree with the closed
  forms to $8.5\times10^{-13}$, and the Kohn-Sham solver of step 3 reproduces them to $10^{-12}$ (DERIVED).

**In concert with the other field equations.**

* *The $Z$ mass in the $Z$ widths.* The $Z$ mass of the $x_0$ eigenvalues, $m_{\mathrm{W}}\tilde m_{\mathrm{Z}}/\tilde
  m_{\mathrm{W}} = 91.187900$ GeV, is the measured value used in the $Z$ widths of step 4, to $2.0\times10^{-12}$; the angle
  of the couplings of the $x_0$ problem ($\sin^2\theta_{\mathrm{W}} = 0.223632$) and the $\overline{\mathrm{MS}}$ value used in
  the widths ($0.23122$) are two values of one angle, and the difference changes the total width by $0.82$ % at tree level
  ($0.83$ % with the QCD factor on the quarks), the size of the electroweak loop corrections that UM-2 does not compute
  (step 4) (DERIVED).
* *The fermion masses in the thermal history.* The twelve masses of the exact roots are the masses of the ideal gases of
  step 9, of the quark components of I13 (step 9) and of the top threshold of step 4, to $3.1\times10^{-12}$ (DERIVED).
* *The neutrino masses and the PMNS matrix.* The three neutrino masses of the tip conditions, their sum and their splittings
  are those of the flavour evolution (step 5), the CNB (step 5) and the CMB computation (step 6), to $5.7\times10^{-12}$, and
  the neutrino tip matrix is the PMNS matrix of the flavour evolution and of the flavour content of the CNB, to
  $8.2\times10^{-13}$ (DERIVED).
* *The dark-matter mass.* The odd level $M_{\mathrm{DM}} = 3.102204\,m_\Psi = 44347.904991$ GeV ($m_\Psi = H$) is the mass of the
  Kohn-Sham quanta (step 3) and of the Boltzmann equation (steps 7 and 9), to $8.1\times10^{-13}$, and its block sensitivity
  $-\mathrm{d}\ln\varepsilon_{\mathrm{DM}}/\mathrm{d}\ln f = 0.772034343$ equals the hidden pressure of the Kohn-Sham quanta
  (step 3) to $6.1\times10^{-12}$ (DERIVED).

## The status of step 2

DERIVED: the exact $x_0$ reductions, the eigenvalue conditions and their roots, the factorisation of the three-generation
condition, the absence of tree-level flavour-changing neutral currents, the spectrum of dirac16complex. ASSUMED: the depth
$HL = 3$, one doublet bulk mass per sector, the tip matrices $\mathcal{K}_e = \mathcal{K}_u = 1$, $\mathcal{K}_\nu = U$,
$\mathcal{K}_d = V_{\mathrm{CKM}}$, the lightest neutrino mass. STANDARD: the measured masses, mixing angles and phases used
as inputs. INVENTED: the tip sigma field and the fermion boundary conditions. OPEN: the Lovelock corrections to the graviton
operator; the radiative corrections.
