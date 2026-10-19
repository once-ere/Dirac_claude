
# A. The $x_0$ mass mechanism {-}

## A.1 The periodic hidden coordinate, the fold and the tip {-}

The hidden coordinate enters the metric through the angle variable $z = 6Hx_0$. The order-0 metric of UM-2, the first term
of the power series of the metric, is in the author's coordinates (AUTHOR)

@@FE-31@@

and in the chart $y$, which measures the hidden direction in proper units of the block, with the block scale $f$ and the
rates of the background (DERIVED)

@@FE-32@@

One period $0 < z < \pi$ of $x_0$, of coordinate length $\pi/(6H) = 3.663\times10^{-5}$ GeV$^{-1}$ $= 7.23\times10^{-21}$ m,
consists of two halves joined at the fold $y = 0$ ($z = \pi/2$); each half ends at a tip ($y \to -\infty$), which UM-2 replaces
by a regular cutoff at $y = -L$ with $HL = 3$ (ASSUMED). Every function of $y(z)$ is periodic in $x_0$ with the period
$\pi/(6H)$, and so is every wave function of UM-2: the author's periodicity requirement is built into the geometry. On the
stabilised block, $f = f_* = 0.215556$, the proper depth of one half is $fL = 8.926\times10^{-21}$ m, i.e.
$1/(fL) = 22.11$ TeV (DERIVED).

## A.2 The author's argument in equations {-}

The author's order of 2026-10-18 gives the reason for the masses in three steps (AUTHOR). First, a particle whose wave
function is localised with respect to $x_0$ obeys the uncertainty relation for the coordinate $x_0$ and the component
$k_{x_0}$ of its momentum along $x_0$ (with $\hbar = 1$ the momentum and the wave number coincide):

$$ \Delta x_0\,\Delta k_{x_0} \ge \frac{\hbar}{2} $$
<!-- symbols: AUTO -->

Second, the momentum may be thought of as proportional to the mass, and the kinetic energy as proportional to the momentum
squared divided by the mass:

$$ k_{x_0} \propto m_{\mathrm{eff}},\qquad E_{\mathrm{kin}} \propto \frac{k_{x_0}^2}{m_{\mathrm{eff}}} $$
<!-- symbols: AUTO -->

Third, hence every particle whose wave function depends on $x_0$, periodically with the period $\pi/(6H)$, has an
effective mass, of the order of the momentum spread that its localisation forces (up to factors of order one, in natural
units):

$$ m_{\mathrm{eff}} \sim \Delta k_{x_0} \ge \frac{\hbar}{2\Delta x_0} $$
<!-- symbols: AUTO -->

This holds, the author states, for all particles except the graviton, the photon and perhaps the quanta of dirac16complex.
The coordinate $x_0$ is not a proper length (its proper element $f\cot z\,\mathrm{d}x_0$ vanishes at the fold and diverges at
the tips; section A.6), so version 3 applied the argument to the proper hidden length $fy$, the proper distance from the fold,
and defined the author's estimate of the mass of a state as (DERIVED from the AUTHOR argument)

$$ m_{\mathrm{Heis}} = \frac{\hbar}{2\Delta(fy)},\qquad \Delta(fy) = fL\,\Delta\xi,\qquad \Delta\xi^2 = \int_{-1}^{0}\xi^2\varrho_\xi\,\mathrm{d}\xi $$
<!-- symbols: AUTO -->

where $\Delta(fy)$ is the root-mean-square proper distance from the fold and $\varrho_\xi$ the probability density of the state
in $\xi$ on one half of the period, in the measure in which the hidden kinetic energy is a plain $\int(\mathrm{d}/\mathrm{d}\xi)^2$:

$$ \varrho_\xi = \frac{\tilde F^2}{\int_{-1}^{0}\tilde F^2\,\mathrm{d}\xi}\ \ (\text{boson},\ F = \mathrm{e}^{-3HL\xi/2}\tilde F),\qquad \varrho_\xi = \frac{\chi^\dagger\chi}{\int_{-1}^{0}\chi^\dagger\chi\,\mathrm{d}\xi}\ \ (\text{fermion}) $$
<!-- symbols: AUTO -->

Over the full period the density is symmetric about the fold, so $\Delta\xi$ is also the spread of the full-period profile.
The argument is a heuristic. UM-2 tests it in two steps: every mass is computed exactly as an eigenvalue of the $x_0$
operator of its field (section A.3), and each eigenvalue is split exactly into the hidden kinetic energy, which the
uncertainty relation bounds, and the remaining terms of the operator, which it does not (section A.4).

## A.3 Every mass is an $x_0$ eigenvalue: the exact equations {-}

### The tip of the cell: electroweak symmetry breaking without a Higgs particle (INVENTED) {-}

The masses of $W^\pm$, $Z$ and of all fermions originate at the regular tip $y = -L$ of the cell, where a non-linear sigma field
carries the electroweak symmetry breaking and couples the doublet zero modes to the singlet zero modes:

@@IN-13@@

with the covariant derivative and the gauge transformation of the sigma field

@@IN-14@@

$\Sigma$ has no radial mode, so there is no Higgs particle; its three would-be Goldstone modes become the longitudinal $W^+$, $W^-$
and $Z$. Every tip term is gauge invariant for arbitrary complex tip matrices (DERIVED with random group elements, deviation
$1.1\times10^{-14}$). In the unitary gauge the first term is the tip mass term of the weak bosons (DERIVED):

@@IN-15@@

$W^+$ and $W^-$ share one mass (they are particle and antiparticle), the $Z$ is heavier by $1/\cos\theta_{\mathrm{W}}$ at leading order
(custodial symmetry), and the photon receives no tip term and stays massless. On the static block these tip terms become
the Robin conditions of the $W^\pm$ and $Z$ profiles (FE-51) and the tip mixing conditions of the fermions (FE-30), both written
out below.

### Gauge bosons and the graviton (DERIVED) {-}

A four-dimensional component of a gauge field with the $x_0$ profile $F$ (in the gauge where the $y$ component of the field
vanishes), and equally the transverse-traceless graviton, obeys on the static block the $x_0$ eigenvalue equation

@@FE-50@@

with the conditions at the fold and at the tip

@@FE-51@@

The tip condition is the natural boundary condition of the tip mass term of the sigma field: $\beta = 0$ for the photon, the
gluons and the graviton, $\beta_{\mathrm{W}}$ for $W^+$ and $W^-$ (one value for both: they are particle and antiparticle), and
$\beta_{\mathrm{Z}}$ for the $Z$. With the rescaled profile $\tilde F$ the solutions are elementary and the eigenvalue
conditions are

@@FE-52@@

For $\beta = 0$ the flat profile is an exact eigenfunction with $\tilde m = 0$: the graviton, the photon and the gluons are
exactly massless, protected by four-dimensional general covariance and gauge invariance. The first even level has
$\tilde m_1^2 = 30.1196$, the first odd level $\tilde m^2 = 27.0890$, and the gap of the operator is $9H^2L^2/4 = 20.25$
(finite elements agree to $5\times10^{-10}$). The $W^\pm$ and $Z$ masses fix the tip parameter and the scale:

@@FE-55@@

With the measured $m_{\mathrm{W}} = 80.3625$ GeV, $m_{\mathrm{Z}} = 91.1879$ GeV and $\rho_{\mathrm{EW},0} - 1 = 0.00038$ (STANDARD) the
fit gives $\cos^2\theta_{\mathrm{W}} = 0.776368$, $\beta_{\mathrm{W}} = 0.011912$, $\beta_{\mathrm{Z}} = 0.015343$,
$\tilde m_{\mathrm{W}}^2 = 1.32149\times10^{-5}$, $\tilde m_{\mathrm{Z}}^2 = 1.70150\times10^{-5}$, $m_{\mathrm{KK}} = 121.32$ TeV and
$H = 14.296$ TeV, and both masses are reproduced (DERIVED). The residuals of the stored eigenvalues in their exact
conditions are $5.9\times10^{-12}$ ($W$) and $1.4\times10^{-12}$ ($Z$). The angle of the couplings of this $x_0$ problem,
$\sin^2\theta_{\mathrm{W}} = 0.223632$, is the on-shell value, while the widths and couplings of the electroweak sector use the
$\overline{\mathrm{MS}}$ value 0.23122; the $Z$ width moves by 0.83 % between the two, within the electroweak loop corrections that
UM-2 does not compute (residual analysis).

### The fermions of three generations (DERIVED) {-}

Every fermion of UM-2, dirac16complex included, reduces exactly to a $2\times2$ block Hamiltonian (all eight blocks, general
$a_4(x_4)$, $b_4(x_4)$, $M(y)$ and $v(y)$; checked with the author's matrices):

@@FE-56@@

For a Standard-Model multiplet $M = \mu_{\psi i}$ and $v = 0$. Its chiral zero modes are

@@FE-57@@

massless four-dimensional particles with the energy $\mathrm{e}^{-a_4}\lvert k\rvert$ for every localisation $c$; a doublet zero
mode with $c_L > 0$ and a singlet zero mode with $c_R < 0$ are both localised at the fold. The tip Yukawa terms of the
sigma field are equivalent to the self-adjoint mixing conditions (the choice of the tip matrices is ASSUMED)

@@FE-30@@

At $k = 0$ the doublet and singlet solutions that satisfy the fold conditions $b(0) = 0$ (doublet) and $a(0) = 0$ (singlet)
reach the tip with

@@FE-58@@

and the tip conditions give the exact mass condition of one generation and its first-order root

@@FE-59@@

For three generations the conditions hold for the vectors of tip values over the generations:

@@FE-60@@

With one doublet bulk mass per sector and unitary tip matrices the determinant factorises into the one-generation conditions
with $\mathcal{K} = 1$, so every mass is a one-generation root and the left-handed rotation of a sector is its tip matrix. The
localisations that reproduce the measured masses (STANDARD targets, tree level) are the doublet localisations
$c_\ell = 5.9529$ (leptons) and $c_Q = 3.3823$ (quarks) and the singlet localisations $c_R$ (DERIVED):

| lepton | $\nu_1$ | $\nu_2$ | $\nu_3$ | electron | muon | tau |
| ---- | --- | --- | --- | --- | --- | --- |
| mass | $1.000$ meV | $8.712$ meV | $50.140$ meV | $0.511$ MeV | $105.66$ MeV | $1776.93$ MeV |
| $c_R$ | $-35.0452$ | $-32.8481$ | $-31.0702$ | $-14.5539$ | $-8.9809$ | $-5.9529$ |

| quark | up | charm | top | down | strange | bottom |
| ---- | --- | --- | --- | --- | --- | --- |
| mass | $2.16$ MeV | $1.273$ GeV | $172.56$ GeV | $4.70$ MeV | $93.5$ MeV | $4.183$ GeV |
| $c_R$ | $-15.4300$ | $-8.7683$ | $-3.3823$ | $-14.6258$ | $-11.5158$ | $-7.5005$ |

The heaviest member of each sector has $c_R = -c_L$; the lightest neutrino mass $m_1 = 1$ meV is ASSUMED, and $m_2$, $m_3$
follow from the measured splittings (section A.7). The roots of the $3\times3$ determinant agree with the one-generation roots,
both refined in the same 50-digit computation, to $3.0\times10^{-42}$; the residual of the stored masses in their exact
conditions is at most $5.4\times10^{-11}$ (for $\nu_1$; $1.2\times10^{-11}$ for the three-generation determinants) (DERIVED).

### The quanta of dirac16complex (DERIVED) {-}

dirac16complex has the same block Hamiltonian with $M = m_\Psi$ (for the free spectrum) and the boundary conditions

@@FE-28@@

which in block form read

@@FE-69@@

Its exact spectrum at $k = 0$ is

@@FE-62@@

At the stabilised block $c_\Psi = 0.646667$: the fold band (the even zero mode, in all eight blocks) is massless, the lowest
odd level, $\varepsilon = 3.102204\,m_\Psi = 44.35$ TeV ($\varpi = 1.89901$), is the dark matter of part B, and the lowest even
bulk level is $4.959981\,m_\Psi$. The residual of the stored spectrum in its exact conditions is $8.5\times10^{-13}$.

### The masses (DERIVED) {-}

The photon, the gluons and the graviton are exactly massless (flat profile); the fold bands of dirac16complex are exactly
massless (chiral zero modes, energy $\mathrm{e}^{-a_4}\lvert k\rvert$); $W^\pm$ ($80.36$ GeV) and $Z$ ($91.19$ GeV) are reproduced; the
twelve fermions have the masses of the tables above; the dark matter has $44.35$ TeV; the Kaluza-Klein levels start at
$121.3$ TeV, and every odd mode and every excitation of the gauge fields and the graviton lies above the gap
$3H/(2f_*) = 99.48$ TeV; the excitations of dirac16complex start at its lowest odd level, $44.35$ TeV. Every one of these
masses is an eigenvalue of an $x_0$ operator acting on wave functions periodic in $x_0$ with the period $\pi/(6H)$.

The approximation: the spectra are computed on the static block $f = f_*$ (the block responds to matter by at most
$\Delta\ln f = 1.1\times10^{-34}$, section A.9), at tree level (the measured masses are tree-level targets; radiative running is
not included), and with the mixing of the zero modes with the Kaluza-Klein modes neglected (its relative size
$(m/m_{\mathrm{KK}})^2$ is at most $2.0\times10^{-6}$, for the top quark). In concert with the other field equations (residual analysis): the
twelve fermion masses enter the thermal history of part B unchanged (to $3.1\times10^{-12}$), the neutrino masses and the PMNS matrix
enter the flavour evolution, the cosmic neutrino background and the CMB computation unchanged (to $5.7\times10^{-12}$ and
$8.2\times10^{-13}$), and the dark-matter mass enters the Kohn-Sham states and the Boltzmann equation unchanged (to $8.1\times10^{-13}$).

## A.4 What the uncertainty relation gives quantitatively {-}

### The exact decomposition of every mass (DERIVED) {-}

For a boson write $F = \mathrm{e}^{-3HL\xi/2}\tilde F$. The exact identity

$$ \mathrm{e}^{3HL\xi}\Big(\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)^2 = \Big(\frac{\mathrm{d}\tilde F}{\mathrm{d}\xi}\Big)^2 + \frac{9H^2L^2}{4}\,\tilde F^2 - \frac{3HL}{2}\,\frac{\mathrm{d}\big(\tilde F^2\big)}{\mathrm{d}\xi} $$
<!-- symbols: AUTO -->

turns the Rayleigh quotient of the eigenvalue equation (FE-50) with the tip condition (FE-51),

$$ \tilde m^2 = \frac{\int_{-1}^{0}\mathrm{e}^{3HL\xi}\big(\mathrm{d}F/\mathrm{d}\xi\big)^2\,\mathrm{d}\xi + \beta\,\mathrm{e}^{-3HL}F(-1)^2}{\int_{-1}^{0}\mathrm{e}^{3HL\xi}F^2\,\mathrm{d}\xi}, $$
<!-- symbols: AUTO -->

into the decomposition

$$ \tilde m^2 = \langle k_\xi^2\rangle + \frac{9H^2L^2}{4} - \frac{3HL}{2}\,\varrho_\xi(0) + \Big(\frac{3HL}{2} + \beta\Big)\varrho_\xi(-1),\qquad \langle k_\xi^2\rangle = \frac{\int_{-1}^{0}\big(\mathrm{d}\tilde F/\mathrm{d}\xi\big)^2\,\mathrm{d}\xi}{\int_{-1}^{0}\tilde F^2\,\mathrm{d}\xi} $$
<!-- symbols: AUTO -->

of the eigenvalue into the hidden kinetic energy $\langle k_\xi^2\rangle$, the constant warp $9H^2L^2/4$ of the three extra times,
an attractive point term at the fold and a repulsive one at the tip. For a fermion mode of the block Hamiltonian with a
constant mass, i.e. a localisation $c$ (or $c_\Psi$), the corresponding exact decomposition is

$$ \tilde\varepsilon^2 = \langle k_\xi^2\rangle + c^2 - c\,\frac{\big[\chi^\dagger\sigma_3\chi\big]_{-1}^{0}}{\int_{-1}^{0}\chi^\dagger\chi\,\mathrm{d}\xi},\qquad \langle k_\xi^2\rangle = \frac{\int_{-1}^{0}\big(\mathrm{d}\chi/\mathrm{d}\xi\big)^\dagger\big(\mathrm{d}\chi/\mathrm{d}\xi\big)\,\mathrm{d}\xi}{\int_{-1}^{0}\chi^\dagger\chi\,\mathrm{d}\xi} $$
<!-- symbols: AUTO -->

(the hidden kinetic energy, the bulk mass and a boundary term). Only the hidden kinetic term is bounded by the uncertainty
relation.

### The uncertainty relation on the cell (DERIVED, a theorem) {-}

On the cell, which ends at the tip, the uncertainty relation acquires a tip term:

$$ \sqrt{\langle k_\xi^2\rangle}\;\Delta\xi \ge \frac{1 - \varrho_\xi(-1)}{2} $$
<!-- symbols: AUTO -->

It follows from an integration by parts (the fold end $\xi = 0$ contributes nothing) and the Cauchy-Schwarz inequality:

$$ 1 = \int_{-1}^{0}\varrho_\xi\,\mathrm{d}\xi = \varrho_\xi(-1) - \int_{-1}^{0}\xi\,\frac{\mathrm{d}\varrho_\xi}{\mathrm{d}\xi}\,\mathrm{d}\xi,\qquad \Big\lvert\int_{-1}^{0}\xi\,\frac{\mathrm{d}\varrho_\xi}{\mathrm{d}\xi}\,\mathrm{d}\xi\Big\rvert \le 2\,\Delta\xi\,\sqrt{\langle k_\xi^2\rangle} $$
<!-- symbols: AUTO -->

The familiar form $\langle k_\xi^2\rangle\Delta\xi^2 \ge 1/4$ is guaranteed only for profiles negligible at the tip. It can hold
otherwise (the first even Kaluza-Klein mode, with $\varrho_\xi(-1) = 0.655$, has $\langle k_\xi^2\rangle\Delta\xi^2 = 4.59$), while the
broad fold zero mode of dirac16complex violates it ($\langle k_\xi^2\rangle\Delta\xi^2 = 0.097$, $\varrho_\xi(-1) = 0.489$) and
satisfies the relation with the tip term.

### The lower bound for a localised state (DERIVED) {-}

If the hidden kinetic energy were the whole mass, $\tilde m^2 = \langle k_\xi^2\rangle$, the relation on the cell would bound the
mass by the author's estimate:

$$ m = \frac{\sqrt{\langle k_\xi^2\rangle}}{fL} \ge \big(1 - \varrho_\xi(-1)\big)\,m_{\mathrm{Heis}},\qquad m_{\mathrm{Heis}} = \frac{\hbar}{2fL\,\Delta\xi} \ge \frac{\hbar}{2fL} = 11.05\ \text{TeV} $$
<!-- symbols: AUTO -->

The last inequality holds because $\Delta\xi \le 1$ on the half cell. The author's estimate is therefore precisely the lower
bound that the uncertainty relation sets on the hidden kinetic energy of a state that is negligible at the tip, and no
profile on the cell can make it smaller than $11.05$ TeV. The actual masses differ from this bound by the other terms of the
decompositions: the warp, the fold and the tip terms of a boson, the bulk mass and the boundary term of a fermion. They were
computed for every class of particle (DERIVED; the sum rules reproduce the boson eigenvalues $\tilde m^2$ to $1.0\times10^{-8}$
in absolute value, the discretisation error of the finite-element profiles (relative $7.8\times10^{-4}$ for $W^\pm$ and
$6.0\times10^{-4}$ for $Z$, whose eigenvalues are only $1.3$ and $1.7\times10^{-5}$, and below $3\times10^{-11}$ for the
excitations), and the dark matter to $1.2\times10^{-11}$ relative; the relation with the tip term holds for every tabulated
state, with the smallest margin $0.057$ for the fold band of dirac16complex).

Bosons (the warp term is $9H^2L^2/4 = 20.25$ for every mode):

| state | $\langle k_\xi^2\rangle$ | fold term | tip term | $\tilde m^2$ | $m/m_{\mathrm{Heis}}$ |
| ---------- | ---- | ---- | ---- | ---- | ---- |
| photon, gluons, graviton | $20.250$ | $-40.505$ | $0.0050$ | $0$ | $0$ |
| $W^\pm$ | $20.250$ | $-40.505$ | $0.0050$ | $1.32\times10^{-5}$ | $1.14\times10^{-3}$ |
| $Z$ | $20.250$ | $-40.505$ | $0.0050$ | $1.70\times10^{-5}$ | $1.29\times10^{-3}$ |
| first even Kaluza-Klein mode | $9.870$ | $-2.949$ | $2.949$ | $30.120$ | $7.49$ |
| first odd mode | $4.891$ | $0$ | $1.948$ | $27.089$ | $6.47$ |

The chiral zero modes of the fermions: each alone is massless, its hidden kinetic energy $\langle k_\xi^2\rangle$ equals the
bulk term $c^2$ and the boundary term is $-2c^2$; one doublet zero mode serves the three generations of a sector, and every
fermion has its own singlet zero mode (a singlet zero mode is right-handed with $c_R < 0$; its profile is that of a doublet
zero mode with $c = -c_R$):

| zero mode | $c$ | $\langle k_\xi^2\rangle$ | boundary term | $\Delta(fy)$ (m) | $m_{\mathrm{Heis}}$ (GeV) | $\varrho_\xi(-1)$ | $\langle k_\xi^2\rangle\Delta\xi^2$ |
| ---------------- | -------- | -------- | --------- | ----------- | --------- | ----------- | --------- |
| lepton doublet | $5.9529$ | $35.437$ | $-70.874$ | $1.06\times10^{-21}$ | $93\,080$ | $8.0\times10^{-5}$ | $0.4997$ |
| quark doublet | $3.3823$ | $11.440$ | $-22.880$ | $1.83\times10^{-21}$ | $53\,800$ | $7.8\times10^{-3}$ | $0.4829$ |
| $\nu_1$ singlet | $35.0452$ | $1228.16$ | $-2456.33$ | $1.80\times10^{-22}$ | $547\,816$ | $2.5\times10^{-29}$ | $0.5000$ |
| $\nu_2$ singlet | $32.8481$ | $1079.00$ | $-2157.99$ | $1.92\times10^{-22}$ | $513\,472$ | $1.9\times10^{-27}$ | $0.5000$ |
| $\nu_3$ singlet | $31.0702$ | $965.36$ | $-1930.71$ | $2.03\times10^{-22}$ | $485\,680$ | $6.4\times10^{-26}$ | $0.5000$ |
| electron singlet | $14.5539$ | $211.82$ | $-423.63$ | $4.34\times10^{-22}$ | $227\,503$ | $6.6\times10^{-12}$ | $0.5000$ |
| muon singlet | $8.9809$ | $80.657$ | $-161.314$ | $7.03\times10^{-22}$ | $140\,388$ | $2.8\times10^{-7}$ | $0.5000$ |
| tau singlet | $5.9529$ | $35.437$ | $-70.874$ | $1.06\times10^{-21}$ | $93\,080$ | $8.0\times10^{-5}$ | $0.4997$ |
| up singlet | $15.4300$ | $238.09$ | $-476.17$ | $4.09\times10^{-22}$ | $241\,198$ | $1.2\times10^{-12}$ | $0.5000$ |
| charm singlet | $8.7683$ | $76.883$ | $-153.766$ | $7.20\times10^{-22}$ | $137\,064$ | $4.2\times10^{-7}$ | $0.5000$ |
| top singlet | $3.3823$ | $11.440$ | $-22.880$ | $1.83\times10^{-21}$ | $53\,800$ | $7.8\times10^{-3}$ | $0.4829$ |
| down singlet | $14.6258$ | $213.91$ | $-427.83$ | $4.32\times10^{-22}$ | $228\,626$ | $5.8\times10^{-12}$ | $0.5000$ |
| strange singlet | $11.5158$ | $132.61$ | $-265.23$ | $5.48\times10^{-22}$ | $180\,012$ | $2.3\times10^{-9}$ | $0.5000$ |
| bottom singlet | $7.5005$ | $56.258$ | $-112.516$ | $8.41\times10^{-22}$ | $117\,248$ | $4.6\times10^{-6}$ | $0.5000$ |

A zero mode localised exponentially at the fold, $\varrho_\xi \propto \mathrm{e}^{2c\xi}$, has

$$ \Delta\xi^2 \simeq \frac{1}{2c^2},\qquad \langle k_\xi^2\rangle\,\Delta\xi^2 \simeq \frac12\qquad (c \gg 1), $$
<!-- symbols: AUTO -->

twice the minimum $1/4$ of the familiar relation. The fermions, their uncertainty estimates (that of the broader of their two
zero modes, i.e. the smaller $m_{\mathrm{Heis}}$) and their sensitivities to the localisation and to the block:

| fermion | mass | $m_{\mathrm{Heis}}$ (GeV) | $m/m_{\mathrm{Heis}}$ | $\frac{\mathrm{d}\ln m}{\mathrm{d}\ln(-c_R)}$ | $\frac{\mathrm{d}\ln m}{\mathrm{d}\ln f}$ |
| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| $\nu_1$ | $1.000$ meV | $93\,080$ | $1.1\times10^{-17}$ | $-34.55$ | $-41.0$ |
| $\nu_2$ | $8.712$ meV | $93\,080$ | $9.4\times10^{-17}$ | $-32.35$ | $-38.8$ |
| $\nu_3$ | $50.140$ meV | $93\,080$ | $5.4\times10^{-16}$ | $-30.57$ | $-37.0$ |
| electron | $0.511$ MeV | $93\,080$ | $5.5\times10^{-9}$ | $-14.05$ | $-20.5$ |
| muon | $105.66$ MeV | $93\,080$ | $1.1\times10^{-6}$ | $-8.48$ | $-14.9$ |
| tau | $1776.93$ MeV | $93\,080$ | $1.9\times10^{-5}$ | $-5.45$ | $-11.9$ |
| up | $2.16$ MeV | $53\,800$ | $4.0\times10^{-8}$ | $-14.93$ | $-18.8$ |
| charm | $1.273$ GeV | $53\,800$ | $2.4\times10^{-5}$ | $-8.27$ | $-12.2$ |
| top | $172.56$ GeV | $53\,800$ | $3.2\times10^{-3}$ | $-2.89$ | $-6.8$ |
| down | $4.70$ MeV | $53\,800$ | $8.7\times10^{-8}$ | $-14.13$ | $-18.0$ |
| strange | $93.5$ MeV | $53\,800$ | $1.7\times10^{-6}$ | $-11.02$ | $-14.9$ |
| bottom | $4.183$ GeV | $53\,800$ | $7.8\times10^{-5}$ | $-7.00$ | $-10.9$ |

(The sensitivity to the singlet localisation is that of the singlet tip density with the doublet fixed, written out in
section A.5; the doublet localisation enters every mass of its sector with $-5.45$ (leptons) and $-2.89$ (quarks); the block
sensitivity follows from (FE-85) in section A.8.) The bosons and the states of dirac16complex:

| state | $\Delta(fy)$ (m) | $m_{\mathrm{Heis}}$ (GeV) | $\varrho_\xi(-1)$ | $\langle k_\xi^2\rangle\Delta\xi^2$ |
| ---------- | ---- | ---- | ---- | ---- |
| photon, gluons, graviton; $W^\pm$; $Z$ | $1.40\times10^{-21}$ | $70\,560$ | $1.1\times10^{-3}$ | $0.497$ |
| first even Kaluza-Klein mode | $6.09\times10^{-21}$ | $16\,204$ | $0.655$ | $4.59$ |
| first odd mode | $5.55\times10^{-21}$ | $17\,771$ | $0.433$ | $1.89$ |
| fold band of dirac16complex | $4.31\times10^{-21}$ | $22\,903$ | $0.489$ | $0.097$ |
| dark matter (lowest odd level) | $5.09\times10^{-21}$ | $19\,395$ | $0.772$ | $0.847$ |

and the decomposition of the two states of dirac16complex (both halves; the bulk term is $c_\Psi^2 = (f_*m_\Psi L)^2 = 0.418$):

| state | $\langle k_\xi^2\rangle$ | bulk $c_\Psi^2$ | boundary term | $\tilde\varepsilon^2$ | $m/m_{\mathrm{Heis}}$ |
| ---------- | ---- | ---- | ---- | ---- | ---- |
| fold band | $0.418$ | $0.418$ | $-0.836$ | $0$ | $0$ |
| dark matter | $2.608$ | $0.418$ | $0.998$ | $4.024$ | $2.29$ |

## A.5 Where the argument fails, and what replaces it {-}

### Three classes of states (DERIVED) {-}

* **Massless although localised.** The photon, the gluons and the graviton are localised at the fold
  ($\Delta(fy) = 1.40\times10^{-21}$ m, $m_{\mathrm{Heis}} = 70.6$ TeV, $\langle k_\xi^2\rangle\Delta\xi^2 = 0.497$), yet exactly massless:
  the fold term cancels the hidden kinetic energy and the warp. The cancellation is exact because the flat profile is an
  eigenfunction with $\tilde m = 0$, protected by four-dimensional gauge invariance and general covariance. The fold bands of
  dirac16complex are massless for the analogous chiral reason (the zero mode $\chi = (\mathrm{e}^{c_\Psi\xi}, 0)^T$ of (FE-62) solves
  the block equation with both boundary conditions for every mass profile), and so is every fermion zero mode before the tip
  mixes it with its partner.
* **Heavy: the uncertainty estimate lies below the mass.** Every $x_0$ excitation of the gauge fields and the graviton lies
  above the gap of their operator: for every tip parameter $\beta$ from $0$ to $10^6$ exactly one even level lies below
  $9H^2L^2/4$ (the zero mode, lifted only by the tip) and no odd level does (the gap theorem, DERIVED), so every odd mode and
  every excitation of these fields has $m \ge 3H/(2f_*) = 99.5$ TeV. The Dirac operator of dirac16complex has no such warp gap;
  its excitations start at the lowest odd level, $3.10\,m_\Psi = 44.35$ TeV (the dark matter). For the computed states
  $m_{\mathrm{Heis}}$ is exceeded by factors 2.3 to 7.5 (dark matter 2.29, first odd mode 6.47, first even mode 7.49): the author's
  estimate lies below these masses (observed for these states, not derived for all), and the dark-matter mass is an $x_0$
  mass in the author's sense, since its hidden wave number carries $\varpi^2/\tilde\varepsilon^2 = 0.896$ of $\tilde\varepsilon^2$.
* **Light: the mass comes from the tip, not from the localisation.** For $W^\pm$, $Z$ and the twelve fermions the $x_0$
  dependence that costs energy sits at the tip, where the probability is small: $m/m_{\mathrm{Heis}} = 1.1\times10^{-3}$ ($W^\pm$),
  $1.3\times10^{-3}$ ($Z$), $3.2\times10^{-3}$ (the top quark, a factor 312 below the estimate) down to $1.1\times10^{-17}$ ($\nu_1$).
  For the fermions a sharper localisation gives a LIGHTER particle: $\mathrm{d}\ln m/\mathrm{d}\ln c < 0$ for every zero mode
  (from $-2.89$ for the quark doublet and the top singlet to $-34.55$ for the $\nu_1$ singlet), the reverse of the Heisenberg
  intuition. The lightest particles of all, the neutrinos, have the most sharply localised singlet partners
  ($\Delta(fy) \approx 2\times10^{-22}$ m, $m_{\mathrm{Heis}} \approx 0.5$ PeV).

![The $x_0$ mass mechanism: the actual masses against the uncertainty estimate $m_{\mathrm{Heis}} = \hbar/(2\Delta(fy))$ (circles: bosons and dirac16complex; squares: the twelve fermions, with the $m_{\mathrm{Heis}}$ of their broader zero mode); the excitations and the dark matter lie above the line $m = m_{\mathrm{Heis}}$, the light particles far below. The axis labels are in the plain-text notation of the plotting script: "hbar c/(2 Delta s)" is $m_{\mathrm{Heis}}$ and "m\_H" is $m_{\mathrm{Heis}}$.](figures/fig_analysis_heisenberg.png)

### Why the light fermions must be zero modes whose masses come from the tip (DERIVED) {-}

The lower bound of section A.4 makes the argument quantitative. The hidden kinetic energy of any profile on the cell that is
negligible at the tip is at least that of a mass $m_{\mathrm{Heis}} \ge 1/(2fL) = 11.05$ TeV; for the actual zero modes it is
that of $54$ to $548$ TeV. Every observed fermion mass is at least 64 times smaller than $11.05$ TeV (the top quark) and up to
$10^{16}$ times smaller (the lightest neutrino). A light fermion is therefore possible only if the other terms of its $x_0$
operator cancel its hidden kinetic energy, and the cancellation must be exact up to the tiny remainder: the profile must be
an exact zero mode of the $x_0$ operator. The chiral zero modes of (FE-57) are exactly such profiles: $h\chi = 0$ at $k = 0$, so
the kinetic term $c^2$ and the bulk term $c^2$ are cancelled by the boundary term $-2c^2$, for every localisation. They are
"flat relative to the geometry" in the same sense as the flat profile of the photon: in $\chi = \mathrm{e}^{c\xi}(1, 0)^T$ the
whole $x_0$ dependence is the exponential that the bulk mass itself generates, and it costs no four-dimensional energy. A
zero mode is massless and chiral; a mass requires a term that couples the doublet zero mode to a singlet zero mode of the
opposite chirality, and in UM-2 the only such term is the tip Yukawa coupling of the sigma field (the tip conditions
(FE-30)). The mass it produces is proportional to the product of the amplitudes of the two zero modes at the tip: this is the
first-order root of the exact mass condition, written out again:

@@FE-59@@

For $c \gg 1$ the tip density of a zero mode is exponentially small, and so are the masses and their sensitivities to the
localisation:

$$ \mathcal{Z}(c)^2 = \frac{c\,\mathrm{e}^{-c}}{\sinh c} \simeq 2c\,\mathrm{e}^{-2c},\qquad m = \frac{\tilde\varepsilon}{fL},\qquad \frac{\mathrm{d}\ln m}{\mathrm{d}\ln c} = \frac12\,\frac{\mathrm{d}\ln\mathcal{Z}(c)^2}{\mathrm{d}\ln c} \simeq \frac12 - c\qquad (c \gg 1) $$
<!-- symbols: AUTO -->

($c = -c_R$ for a singlet with the doublet fixed; $-34.55$ for the $\nu_1$ singlet, $-2.89$ for the top singlet). The masses of
the light fermions are thus tip effects of zero modes, not localisation energies: the uncertainty relation does not produce
them, and a sharper localisation lowers them. The same holds for $W^\pm$ and $Z$, whose profiles are the photon's flat zero mode
bent by the tip parameter $\beta$: their masses are the small tip-induced bending ($m/m_{\mathrm{Heis}} \approx 10^{-3}$).

### The hierarchy of the masses (DERIVED) {-}

Because the tip densities depend exponentially on the localisations, bulk masses of order one produce the whole hierarchy:
the twelve fermion masses span fourteen orders of magnitude, from $\nu_1$ to the top quark, with bulk masses between $5.2H$
(the quark doublets, $\mu_Q = 5.2304\,H$) and $54.2H$ in magnitude (the $\nu_1$ singlet), and within a sector the lighter
fermion has the sharper singlet localisation. The doublet bulk masses are $\mu_\ell = 9.2055\,H$ and $\mu_Q = 5.2304\,H$. The
first-order root of (FE-59) agrees with the exact roots to $1.1\times10^{-3}$ for the top quark and to better than
$3\times10^{-4}$ for every other fermion. The hierarchy is the exponential response of the tip densities to order-one bulk masses;
it is not explained further by the mechanism (the bulk masses are fitted).

### The mixing matrices (DERIVED, ASSUMED inputs) {-}

With the doublet shared by the three generations of a sector, the charged current between the mass states $\nu_j$ and the
charged leptons of the generation $i$ carries $\sum_\alpha(\mathcal{K}_\nu)^*_{\alpha j}(\mathcal{K}_e)_{\alpha i}$, and the mixing
matrices are the tip matrices (from (FE-60)):

$$ U = \mathcal{K}_e^\dagger\mathcal{K}_\nu = \mathcal{K}_\nu,\qquad V_{\mathrm{CKM}} = \mathcal{K}_u^\dagger\mathcal{K}_d = \mathcal{K}_d\qquad (\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}) $$
<!-- symbols: AUTO -->

in the standard parametrisation (STANDARD; the same form for $V_{\mathrm{CKM}}$)

@@FE-61@@

with $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{23} = 0.470$, $\sin^2\theta_{13} = 0.02215$, $\delta_{\mathrm{CP}} = 212^\circ$ for the PMNS
matrix (NuFIT 6.0, normal ordering; $J_{\mathrm{CP}} = -0.01777$) and $s_{12} = 0.22501$, $s_{13} = 0.003732$, $s_{23} = 0.04183$,
$\delta_{\mathrm{CP}} = 1.147$ for the CKM matrix (PDG global fit; $J_{\mathrm{CP}} = 3.117\times10^{-5}$), both unitary to $1.1\times10^{-16}$:

$$ \lvert U\rvert = \begin{pmatrix} 0.8226 & 0.5488 & 0.1488\\ 0.3351 & 0.6543 & 0.6779\\ 0.4594 & 0.5203 & 0.7199\end{pmatrix},\qquad \lvert V_{\mathrm{CKM}}\rvert = \begin{pmatrix} 0.97435 & 0.22501 & 0.00373\\ 0.22488 & 0.97349 & 0.04183\\ 0.00858 & 0.04111 & 0.99912\end{pmatrix} $$
<!-- symbols: AUTO -->

The angles and phases are inputs of UM-2, not predictions: the mechanism explains the masses through the localisations, but
not the mixing, which is the choice of the tip matrices (OPEN: their origin). The right-handed rotations are trivial, and
because the doublets of a sector share one bulk mass the first even Kaluza-Klein gauge mode couples to every left-handed
lepton with the same relative strength $0.14434$ and to every left-handed quark with $-0.30066$, so there are no
flavour-changing neutral currents at tree level (the largest off-diagonal coupling in the mass basis is $10^{-17}$, round-off;
different doublet bulk masses would create off-diagonal couplings up to $0.033$) (DERIVED).

### The massless zero modes (DERIVED) {-}

The exactly massless states of UM-2 are the zero modes of $x_0$ operators that no term of the action lifts: the photon and
the gluons (flat profiles with $\beta = 0$, protected by the unbroken gauge invariance; the tip terms give mass to $W^\pm$ and $Z$
only), the graviton (flat profile, protected by four-dimensional general covariance), and the fold bands of both halves of
dirac16complex (chiral zero modes; no tip operator acts on them, the scalar density of a chiral zero mode vanishes, and I13
acts only on the lower component; part B). These are exactly the exceptions named by the author: the graviton, the photon
and the quanta of dirac16complex, more precisely its massless fold bands, while its odd quanta are massive (the dark matter).

## A.6 Proper versus coordinate localisation (DERIVED) {-}

The proper element of the hidden direction is

$$ f\,\mathrm{d}y = f\cot z\,\mathrm{d}x_0 $$
<!-- symbols: AUTO -->

which vanishes at the fold and diverges at the tips. The photon zero mode, localised at the fold in proper length, has
61.9 % of its probability within $\pi/8$ of the tips in the coordinate $z = 6Hx_0$: localisation in the coordinate $x_0$ is chart
dependent. A profile confined to a small proper distance from the fold ($\Delta\xi = 0.157$, i.e. $\lvert y\rvert \lesssim 0.47/H$,
$\sin z \gtrsim \mathrm{e}^{-2.8}$) extends over almost the whole coordinate range of $z$, and its probability per unit $z$ is
largest near the tips. Only the proper hidden length enters the masses; the author's "$\Delta x_0$ small" must be read as
"$\Delta(fy)$ small".

## A.7 The neutrinos: masses, mixing and flavour conversion as $x_0$ effects {-}

The three neutrino masses are $x_0$ eigenvalues of the same kind as the charged-fermion masses: Dirac masses produced at the
tip by the overlap of the lepton-doublet zero mode ($c_\ell = 5.9529$) with three right-handed singlet zero modes localised
very sharply at the fold ($c_R = -35.05$, $-32.85$, $-31.07$). With the lightest mass ASSUMED and the measured splittings
(STANDARD, NuFIT 6.0, normal ordering):

@@FE-100@@

The right-handed neutrinos are gauge singlets and are never in thermal equilibrium (their interactions are the tip mixing,
whose rate is suppressed by $(m_i/T)^2$, STANDARD, and the portal I11 with the $B - L$ charge $-1$, through which the dark matter
annihilates into right-handed neutrino pairs at only $2.0\times10^{-17}$ of its I13 rate into quarks, DERIVED; part B), so they
add no radiation. The PMNS matrix is the tip matrix $\mathcal{K}_\nu$ (section A.5); its angles and phase are inputs. Given the
masses and $U$, the flavour conversion follows from the four-dimensional effective theory (STANDARD):

@@FE-104@@

with the potentials of coherent forward scattering in matter

@@FE-103@@

(the neutral-current potential is common to the three flavours and drops out of the conversion; for antineutrinos
$U \to U^*$ and $V \to -V$). The oscillation phases $\Delta_{21}$, $\Delta_{31}$, $\Delta_{32}$ contain the differences of squared
$x_0$ eigenvalues, so oscillation experiments measure the $x_0$ spectrum directly. These differences are the quantities of
UM-2 most sensitive to the block scale (DERIVED):

$$ \begin{aligned} &\frac{\mathrm{d}\ln\big(m_j^2 - m_i^2\big)}{\mathrm{d}\ln f} = \frac{2}{m_j^2 - m_i^2}\Big(m_j^2\,\frac{\mathrm{d}\ln m_j}{\mathrm{d}\ln f} - m_i^2\,\frac{\mathrm{d}\ln m_i}{\mathrm{d}\ln f}\Big):\\
&\frac{\mathrm{d}\ln\Delta m_{21}^2}{\mathrm{d}\ln f} = -77.5,\qquad \frac{\mathrm{d}\ln\Delta m_{31}^2}{\mathrm{d}\ln f} = -74.0,\qquad \frac{\mathrm{d}\ln\Delta m_{32}^2}{\mathrm{d}\ln f} = -73.9 \end{aligned} $$
<!-- symbols: AUTO -->

The light neutrino states also mix with the Kaluza-Klein excitations of the lepton fields, which makes the $3\times3$ PMNS
matrix non-unitary at the relative order $(m_i/m_{\mathrm{KK}})^2 \le 1.7\times10^{-31}$ (ESTIMATE; $2.0\times10^{-6}$ for the top
quark, the largest of all fermions): unobservable. The flavour conversion of UM-2 is therefore that of the three-flavour
Standard Model with Dirac neutrinos, which UM-2 computes for the vacuum, the Earth, the Sun, the early Universe and supernovae.

**Dirac or Majorana (DERIVED).** The $x_0$ mechanism explains the small Dirac masses by the localisation of the right-handed
singlets with tip couplings of order one. Without right-handed neutrinos the masses would be Majorana masses from the
gauge-invariant tip operator (the tip form of the Weinberg operator; not part of UM-2)

$$ S_{\mathrm{M}} = -\frac12\int_{y=-L}\mathrm{d}^7X_{\mathrm{tip}}\sqrt{\lvert g_{\mathrm{tip}}\rvert}\,\sum_{i,j=1}^{3}m^{\mathrm{M}}_{ij}\,\tilde\nu_i\tilde\nu_j + \text{h.c.},\qquad \tilde\nu_i = \big(\Sigma^\dagger\ell_i\big)_1 $$
<!-- symbols: AUTO -->

(the upper component of $\Sigma^\dagger\ell_i$ is neutral, since $\Sigma \to U_L\Sigma U_Y^\dagger$ absorbs both the SU(2) and the
hypercharge transformations of $\ell_i$), which gives, to first order in the tip value of the doublet zero mode,

$$ m_i = \mathcal{K}_{\mathrm{M}}^{(i)}\,\frac{\mathcal{Z}(c_L)^2}{fL},\qquad \mathcal{Z}(c_L)^2 = 8.04\times10^{-5},\qquad \frac{1}{fL} = 22.11\ \text{TeV}, $$
<!-- symbols: AUTO -->

so the measured masses need $\mathcal{K}_{\mathrm{M}}^{(i)} = 5.6\times10^{-13}$, $4.9\times10^{-12}$, $2.8\times10^{-11}$: a hierarchy of tip
couplings that the mechanism does not explain. The $x_0$ mechanism therefore favours Dirac neutrinos. The Majorana case would
show up in neutrinoless double-beta decay with

$$ m_{\beta\beta} = \Big\lvert\sum_{i=1}^{3}U_{ei}^2\,m_i\,\mathrm{e}^{\mathrm{i}\varphi^{\mathrm{M}}_i}\Big\rvert $$
<!-- symbols: AUTO -->

between $0.84$ and $4.41$ meV over all Majorana phases ($\lvert U_{ei}\rvert^2m_i = 0.677$, $2.624$, $1.111$ meV), below the reach of
present experiments, and in a twice larger capture rate of the non-relativistic cosmic neutrino background; the flavour
conversion is the same.

## A.8 The mass mechanism, the block and the deflating extra times {-}

Every mass and coupling depends on the block scale $f$ (DERIVED). A fermion mass $m = \tilde\varepsilon/(fL)$, with the
first-order root of (FE-59) and localisations $c = f\mu L$ proportional to $f$, has the block sensitivity

@@FE-85@@

the Kaluza-Klein masses $m^{\mathrm{KK}}_n = \tilde m_n/(fL)$ scale as $f^{-1}$, and the four-dimensional couplings and Newton's
constant follow from the reduction on the block

@@FE-49@@

so that the gauge couplings scale as $g_3^2, g_2^2, g_1^2 \propto 1/V_\perp \propto f^{-4}$, and

$$ \frac{\mathrm{d}\ln G_{\mathrm{N}}}{\mathrm{d}\ln f} = -4 + \frac{2K_*}{\mathcal{G}(K_*)}\,\frac{\mathrm{d}\mathcal{G}}{\mathrm{d}K}\Big\vert_{K = K_*} = +2.05 $$
<!-- symbols: AUTO -->

(the Lovelock factor $\mathcal{G}$ of the four-dimensional Newton constant varies with the block too):

| quantity | $\mathrm{d}\ln(\cdot)/\mathrm{d}\ln f$ |
| ---------- | ---------- |
| Kaluza-Klein masses, the gap $3H/(2f)$ | $-1$ |
| $m_{\mathrm{W}}$ (and $m_{\mathrm{Z}}$) | $-0.501$ |
| $m_1$, $m_2$, $m_3$ | $-41.0$, $-38.8$, $-37.0$ |
| electron, muon, tau masses | $-20.5$, $-14.9$, $-11.9$ |
| up, charm, top masses | $-18.8$, $-12.2$, $-6.8$ |
| down, strange, bottom masses | $-18.0$, $-14.9$, $-10.9$ |
| $M_{\mathrm{DM}}$ | $-0.772$ |
| $\alpha_{\mathrm{em}}$ and the gauge couplings | $-4$ |
| $G_{\mathrm{N}}$ | $+2.05$ |

The author's metric lets the extra times $x_5, x_6, x_7$ (and, in the corrected metric, $x_0$ with them) deflate
exponentially. In UM-2 they do so in the primordial era: the full nonlinear equations take a large block into the stabilised
one at rates up to $\lvert\mathcal{H}_f\rvert = 2.63H$ (in the stored runs), deflating by up to the factor 2.917 in $f$ (the
largest block that still reaches the stabilised one), after which the block oscillates about $f_*$ (the
radion, $\omega_{\mathrm{r}} = 3.387H = 48.42$ TeV) and stays frozen. A continuing deflation today is excluded (ESTIMATE, bounds
FROM MEMORY): since

$$ \frac{\mathrm{d}\ln m}{\mathrm{d}x_4} = \frac{\mathrm{d}\ln m}{\mathrm{d}\ln f}\,\mathcal{H}_f,\qquad \frac{\mathrm{d}\ln\alpha_{\mathrm{em}}}{\mathrm{d}x_4} = -4\,\mathcal{H}_f,\qquad \frac{\mathrm{d}\ln G_{\mathrm{N}}}{\mathrm{d}x_4} = 2.05\,\mathcal{H}_f, $$
<!-- symbols: AUTO -->

the atomic-clock bound $\lvert\mathrm{d}\ln\alpha_{\mathrm{em}}/\mathrm{d}x_4\rvert < 10^{-17}$/yr requires
$\lvert\mathcal{H}_f\rvert < 2.5\times10^{-18}$/yr $= 3.6\times10^{-8}\,\mathcal{H}_0$ ($\mathcal{H}_0 = 6.90\times10^{-11}$/yr), lunar ranging
($\lvert\mathrm{d}\ln G_{\mathrm{N}}/\mathrm{d}x_4\rvert < 10^{-13}$/yr) requires $\lvert\mathcal{H}_f\rvert < 4.9\times10^{-14}$/yr
$= 7.1\times10^{-4}\,\mathcal{H}_0$, and a block deflating at the Hubble rate ($\lvert\mathcal{H}_f\rvert = \mathcal{H}_0$) would change the
electron mass by $20.5\,\mathcal{H}_0 = 1.4\times10^{-9}$ per year. The extra times are irrelevant at low energies not because they
keep deflating but because they are small (the proper half cell $f_*L = 3f_*/H = 8.9\times10^{-21}$ m, Kaluza-Klein masses above
100 TeV) and frozen. The price is the stabiliser (ASSUMED, origin OPEN) and the radion left over from the deflation, whose
Planck-suppressed decay is estimated (ESTIMATE) as

$$ \Gamma_{\mathrm{r}} = \frac{C_{\mathrm{r}}\,\omega_{\mathrm{r}}^3}{4\pi\bar M_{\mathrm{Pl}}^2},\qquad T_{\mathrm{RH}} = \Big(\frac{90}{\pi^2g_\rho}\Big)^{1/4}\sqrt{\Gamma_{\mathrm{r}}\bar M_{\mathrm{Pl}}} $$
<!-- symbols: AUTO -->

with the reduced Planck mass $\bar M_{\mathrm{Pl}} = 2.435\times10^{18}$ GeV, an order-one coupling factor $C_{\mathrm{r}}$ and
$g_\rho = 10.75$: the lifetime is $0.43\,\text{s}/C_{\mathrm{r}}$ and the reheating temperature $T_{\mathrm{RH}} = 1.85\sqrt{C_{\mathrm{r}}}$ MeV,
below the 4.7 MeV that nucleosynthesis needs unless $C_{\mathrm{r}} > 6.5$: a moduli problem (OPEN).

## A.9 The nucleon mass, the block response and the Kaluza-Klein gravitons {-}

Most of the visible mass is nucleon mass, i.e. QCD binding energy, which is not an $x_0$ eigenvalue of a field but follows from
the strong coupling by dimensional transmutation. In UM-2 the coupling is fixed at the Kaluza-Klein scale,
$g_3^2 = \hat g_3^2/V_\perp \propto f^{-4}$ (FE-49), so the QCD scale is an $x_0$ quantity too (ESTIMATE at one loop):

@@FE-83@@

and through the quark thresholds

@@FE-84@@

With $\alpha_3(m_{\mathrm{Z}}) = 0.1180$, i.e. $\alpha_3(m_{\mathrm{KK}}) = 0.0606$, the sigma terms $\sigma_{\pi N} = 45$ MeV and
$\sigma_{\mathrm{s}} = 40$ MeV (FROM MEMORY) and the quark sensitivities of (FE-85) ($-18.82$, $-18.01$, $-14.90$, $-12.15$, $-10.89$,
$-6.77$ for the up, down, strange, charm, bottom and top quarks), the QCD scale has the sensitivities $-60.2$ (six flavours),
$-55.6$, $-52.0$ and $-49.0$ (three flavours), and $\mathrm{d}\ln m_{\mathrm{p}}/\mathrm{d}\ln f = -46.1$: the nucleon mass is the most
block-sensitive mass of UM-2, more than the lightest neutrino ($-41.0$), and a block that drifted today would change the
proton-to-electron mass ratio by $(46.1 - 20.5)\lvert\mathcal{H}_f\rvert$ per unit time.

In the coupled solution the block responds to the block-averaged sources of all species with the adiabatic response of the
linearised background equations (DERIVED)

@@FE-80@@

in which radiation drops out exactly ($c_3 = -3c_\rho$), so that only the trace $\rho - 3p_3$ and the hidden pressure act; the
hidden pressure is the response of the pressure to the block scale at fixed temperature (DERIVED)

@@FE-81@@

It shifts the block by at most $\Delta\ln f = 1.1\times10^{-34}$ (at the dark-matter freeze-out, pushed by the hot plasma, whose
hidden pressure $\bar p = 3.1\times10^{12}$ GeV$^4$ is mostly the QCD interaction measure; $10^{-62}$ in the Earth), and the loop
mass $\to$ source $\to$ block $\to$ mass has the gain $1.1\times10^{-33}$ at most, so the masses are fixed to that accuracy. The
plasma energy density at the freeze-out differs by 0.13 % between the ideal-gas thermal history and these block sources, which
include the trace anomaly by design (residual analysis). The block-shape source $p_0 - p_5$, which the order-0 metric cannot
absorb, is about 4 times the kept $\bar p$ for non-relativistic dark matter (residual analysis; OPEN), but it is suppressed like
$\bar p$ itself ($\kappa p/(\kappa\rho_{\mathrm{stab}}) \le 3\times10^{-32}$ at the freeze-out) if the shape mode is stable (OPEN).

The Kaluza-Klein gravitons, the terms $n \ge 1$ of the metric series, couple to a source through the overlap of its $x_0$
profile with theirs (DERIVED):

@@FE-53@@

@@FE-54@@

Their profiles are orthogonal to the flat profile of the gauge zero modes in the measure $\mathrm{e}^{3HL\xi}$, so the gluon field
energy that makes up most of the nucleon mass excites none of them (DERIVED to $2\times10^{-10}$): gravity at short distances
feels only the localised quark and lepton zero modes. The first mode has $\mathcal{A}_1 = 0.0904$ between two masses with the
quark-doublet profile and $0.0208$ with the lepton-doublet profile, and the range $1/m_{\mathrm{KK}} = 1.63\times10^{-21}$ m:
$\mathrm{e}^{-m_{\mathrm{KK}}r} = \mathrm{e}^{-3.1\times10^{16}}$ at 50 micrometres, and Newton's law is exact at every measurable distance.

## A.10 Assessment of the mechanism {-}

The author's mechanism works in UM-2 in a precise sense: every mass is an $x_0$ eigenvalue, the period $\pi/(6H)$ is built into
every wave function, and the massless particles are exactly those protected by symmetry (the photon, the gluons, the
graviton and the fold bands of dirac16complex). The uncertainty relation, however, is the reason for the masses of the heavy
states only: for the Kaluza-Klein and odd excitations and for the dark matter the author's estimate $m_{\mathrm{Heis}}$ lies below
the mass (by factors 2.3 to 7.5). The light masses need two ingredients that are not consequences of the uncertainty
relation: exact chiral zero modes, whose hidden kinetic energy is cancelled exactly, and the tip of the cell, where the
electroweak symmetry is broken by the sigma field and the zero modes are mixed. Their overlap at the tip,
$\mathcal{Z}(c)^2 \simeq 2c\,\mathrm{e}^{-2c}$, produces the hierarchy of the twelve fermion masses, fourteen orders of magnitude from
$\nu_1$ to the top quark, from bulk masses between $5.2H$ and $54.2H$ in magnitude; a sharper localisation gives a lighter
fermion, the reverse of the Heisenberg intuition. The mixing matrices are tip matrices and are not explained by the mechanism.
The scales are not free: once the Kaluza-Klein scale is fitted ($m_{\mathrm{KK}} = 121.3$ TeV from $\rho_{\mathrm{EW},0}$), the
dark-matter mass ($44.35$ TeV) and the radion mass ($48.4$ TeV) follow. Three further results: the nucleon mass, the bulk of the
visible mass, depends on the block through the QCD scale more strongly than any $x_0$ eigenvalue ($-46.1$); the mechanism favours
Dirac over Majorana neutrinos; and in the coupled solution every back-reaction on the masses (the Standard-Model mean fields
on dirac16complex, dirac16complex on the gauge couplings, all species on the block) stays below $1.5\times10^{-6}$, so the $x_0$
spectra of the static block are the masses of the solution.
