# Step 3: the Kohn-Sham states of dirac16complex coupled to all fields

dirac16complex $\Psi$ is a 16-component complex spinor field of the author's Clifford algebra $Cl(4,4)$; it couples to
gravity through the canonical spin connection, to itself through a contact self-interaction, and to the Standard-Model
fields through the three portals I11, I12 and I13. Its interacting many-body states on the block are described by
Kohn-Sham theory; step 3 solves the Kohn-Sham equations and returns their energy-momentum tensor to the gravitational
equations of step 1.

## The field equations of step 3

@@T:The dirac16complex field@@

@@T:The Clifford algebra@@

@@T:The canonical spin connection@@

@@T:Portal I11@@

@@T:Portal I12@@

@@T:Portal I13@@

The field equation of dirac16complex, its boundary conditions and its coupling to the order-0 metric:

@@dirac16@@

@@bc_psi@@

@@gomega@@

Its energy-momentum tensor, the source that it returns to the gravitational equations:

@@t_psi@@

The exact reduction to the block Hamiltonian (step 2) turns the field equation into two-component equations in $y$; the
interacting many-body state is described by Kohn-Sham orbitals of this Hamiltonian with the local mean fields of the
self-interaction and of the portals:

@@ferm_red@@

@@ks@@

@@ks_mean@@

@@ks_dens@@

@@ks_energy@@

@@ks_tmn@@

@@ks_id@@

@@ks_bc@@

## The approximation of step 3

* *Kohn-Sham mean field.* The contact self-interaction enters through its Hartree term and its exact local exchange (the
  functional of the record, which gives the coefficients $15/16$ and $-1/16$ of the mean fields); correlation beyond the local
  exchange is not estimated (OPEN).
* *The static block.* The orbitals live on the static block of step 1 ($\mathcal{H} = \mathcal{H}_f = 0$; $a_4 = 0$ in the
  cell), whose response to their energy-momentum tensor is computed at first order below.
* *A periodic cell in 3-space.* The momenta along $x_1, x_2, x_3$ are restricted to the lattice $\vec k_o = k_{\mathrm{lat}}\,
  \vec n_o$ with $k_{\mathrm{lat}} = 0.25\,H$; a state is a set of occupied orbitals in a cell of the normalisation volume
  $\mathrm{Vol}_7$.
* *A finite basis.* The orbitals are expanded in 60, 120 and 240 exact free eigenfunctions per sector and extrapolated in the
  basis size (Richardson); the remaining basis error is at most $1.5\times10^{-9}$ (relative) for the energies.
* *The portal fields as external first-order mean fields.* The Standard-Model fields enter through their densities and
  condensates; their responses are linear (Hellmann-Feynman) and are evaluated with the physical strengths in step 8.
*The self-coupling.* The Kohn-Sham machinery is tested with the benchmark $\lambda_{\mathrm{test}} = 7\times10^{-5}\,H^{-6}$ and
with stress couplings; the cosmology of step 9 requires $\lambda \le 1.4\times10^{-10}\,H^{-6}$ (for $v_{\mathrm{t}} = H^{-3}$),
at which the self-interaction mean field of the densest state below is

$$
\frac{\max\lvert M_{\mathrm{eff}} - m_\Psi\rvert}{m_\Psi} = 2.7\times10^{-9}
$$

<!-- symbols: AUTO -->

so for the cosmological states of UM-2 the self-interaction mean fields are negligible.

## The solution of step 3

### The numerical method

The orbitals are expanded in the exact free eigenfunctions of each sector and iterated to self-consistency (tolerance
$10^{-13}$ in the maximum norm, safeguarded Anderson mixing). The momentum shells have the degeneracy
$d_o = 4r_3(\lvert\vec n_o\rvert^2)$, $r_3$ the number of representations of an integer as a sum of three squares; the factor
$\tfrac12$ in the densities is the weight of each fold parity; and $\mathrm{Vol}_7 = (2\pi/k_{\mathrm{lat}})^3v_{\mathrm{t}}f_*^4
= 34.27$ ($v_{\mathrm{t}} = 1$, $a_4 = 0$, units $H = 1$; the proper seven-volume of a cell is $2\,\mathrm{Vol}_7(1 -
\mathrm{e}^{-3HL})/(3H)$).

### Validation against the record

The solver reproduces the record's two reference states (at $f = 1$, $a_4 = 0$): 8 quanta with $\lambda = 157.7$:
$E_{\mathrm{KS}} = -0.037786682923$ (reference $-0.037786682923$), the highest occupied and lowest unoccupied levels (HOMO,
LUMO) to $10^{-14}$, the integrated $p_0$ $-0.08860537545$ (reference $-0.08860537548$); 592 quanta with $\lambda = 2.131$:
$E_{\mathrm{KS}} = 358.30104644787$ (identical), integrated $p_0$ $-6.7691415097$ (reference $-6.7691415108$) (DERIVED).

### Ground states on the stabilised block

Two families of states (the eight $k = 0$ fold zero modes, 8 quanta; a fold-band gas, 592 quanta) with $\lambda = 0$, the
benchmark $\pm\lambda_{\mathrm{test}}$ (mean fields below 5 % of $m_\Psi$) and the record's coupling scaled to the block (stress
test, $\lambda = 157.7f_*^4 = 0.3405\,H^{-6}$ and $2.131f_*^4 = 0.00460\,H^{-6}$) (DERIVED; 120 functions per sector, relative
Richardson errors below $2.2\times10^{-9}$). $E_{\mathrm{int}} = 2\,\mathrm{Vol}_7\int_{-L}^0\mathrm{e}^{3Hy}e_{\mathrm{int}}\,
\mathrm{d}y$ is the interaction energy, units $H = 1$:

| state | $E_{\mathrm{KS}}$ | $E_{\mathrm{int}}$ | HOMO | LUMO | iterations |
| --- | --- | --- | --- | --- | --- |
| 8 quanta, $\lambda = 0$ | $0$ | $0$ | $0$ | $0.25$ | 1 |
| 8 quanta, $+\lambda_{\mathrm{test}}$ | $-2.053\times10^{-4}$ | $-2.053\times10^{-4}$ | $-5.13\times10^{-5}$ | $0.24995$ | 14 |
| 8 quanta, $-\lambda_{\mathrm{test}}$ | $2.053\times10^{-4}$ | $2.053\times10^{-4}$ | $5.13\times10^{-5}$ | $0.25005$ | 14 |
| 8 quanta, stress | $-0.70123$ | $-0.42170$ | $-0.14037$ | $0.10859$ | 57 |
| 592 quanta, $\lambda = 0$ | $361.11614$ | $0$ | $0.79057$ | $0.82916$ | 1 |
| 592 quanta, $+\lambda_{\mathrm{test}}$ | $359.99060$ | $-1.12646$ | $0.78676$ | $0.82535$ | 14 |
| 592 quanta, $-\lambda_{\mathrm{test}}$ | $362.23906$ | $1.12121$ | $0.79436$ | $0.83295$ | 13 |
| 592 quanta, stress | $307.67139$ | $-32.2217$ | $0.64506$ | $0.68347$ | 56 |

| state | $\int p_3$ | $\int p_5$ | $\int p_0$ | $\max\lvert M_{\mathrm{eff}} - m_\Psi\rvert$ | $\max\lvert v\rvert$ |
| --- | --- | --- | --- | --- | --- |
| 8 quanta, $+\lambda_{\mathrm{test}}$ | $-2.05\times10^{-4}$ | $-2.05\times10^{-4}$ | $-4.447\times10^{-4}$ | $2.4\times10^{-7}$ | $6.7\times10^{-4}$ |
| 8 quanta, $-\lambda_{\mathrm{test}}$ | $2.05\times10^{-4}$ | $2.05\times10^{-4}$ | $4.447\times10^{-4}$ | $2.4\times10^{-7}$ | $6.7\times10^{-4}$ |
| 8 quanta, stress | $-0.4217$ | $-0.4217$ | $-1.30076$ | $1.98$ | $1.83$ |
| 592 quanta, $\lambda = 0$ | $120.372$ | $0$ | $-1.1\times10^{-12}$ | $0$ | $0$ |
| 592 quanta, $+\lambda_{\mathrm{test}}$ | $119.245$ | $-1.1265$ | $-2.43688$ | $1.3\times10^{-3}$ | $0.050$ |
| 592 quanta, $-\lambda_{\mathrm{test}}$ | $121.493$ | $1.1212$ | $2.43174$ | $1.3\times10^{-3}$ | $0.050$ |
| 592 quanta, stress | $87.614$ | $-32.222$ | $-97.8188$ | $2.09$ | $1.88$ |

(The integrals are $2\,\mathrm{Vol}_7\int_{-L}^0\mathrm{e}^{3Hy}(\cdot)\,\mathrm{d}y$; the state of 8 quanta with $\lambda = 0$
has all of them zero.) The free gas has $\int p_3/\int\rho = 1/3$ exactly: four-dimensional radiation. The self-interaction
shifts the fold-band levels almost rigidly (the spacing between $k = 0$ and the first shell is $0.25$ free, $0.25000$ at
$\lambda_{\mathrm{test}}$, $0.2490$ in the stress state of 8 quanta). A scalar mean field cannot gap the fold band at $k = 0$:
$\chi = (\exp(f\int M_{\mathrm{eff}}\,\mathrm{d}y),\ 0)^T$ solves $\varsigma[-(\mathrm{i}/f)\sigma_1\partial_y +
M_{\mathrm{eff}}\sigma_2]\chi = 0$ with both boundary conditions for every $M_{\mathrm{eff}}(y)$.

### The dark-matter quanta

Eight quanta in the lowest odd level at $k = 0$ on the ground state of 8 quanta add exactly $8\varepsilon_{\mathrm{DM}} =
24.817633063$ (computed $24.817633063$) at $\lambda = 0$ and $24.81833$ at $+\lambda_{\mathrm{test}}$; they are cold,
$p_3/\rho = 0$ ($2.8\times10^{-5}$ with $\lambda_{\mathrm{test}}$), and their hidden pressure equals the block sensitivity of
the $x_0$ eigenvalue of step 2, obtained independently:

$$
\frac{p_0}{\rho} = -\frac{\mathrm{d}\ln\varepsilon_{\mathrm{DM}}}{\mathrm{d}\ln f} = 0.772034343\qquad \text{(dark-matter quanta at rest)}
$$

<!-- symbols: AUTO -->

(DERIVED): the dark-matter mass is an $x_0$ eigenvalue, and it pushes on the block.

### The Standard-Model fields acting on dirac16complex

The portal mean fields were applied with the amplitude $A_{\mathrm{mf}}$ and the shapes of the sources: for I11 the proper
densities of the zero modes times $\mathrm{e}^{-3Hy}/\mathrm{Vol}_7$, with the density of an unpolarised fermion the average
of its doublet and singlet zero-mode densities, $\varrho(y; c) = (2c/L)\,\mathrm{e}^{2cy/L}/(1 - \mathrm{e}^{-2c})$ for the
localisation $c$: the electron $\frac12[\varrho(y; c_L) + \varrho(y; -c_R)]$ ($c_L = 5.9529$, $-c_R = 14.5539$), the up
quark $\frac12[\varrho(y; c_L) + \varrho(y; -c_R)]$ ($c_L = 3.3823$, $-c_R = 15.4300$) and the neutrinos, produced
left-chiral, $\varrho(y; c_L)$; for I12 a uniform gluon condensate. The level of a Kohn-Sham orbital responds linearly
(Hellmann-Feynman):

@@levelshift@@

The responses of the lowest odd level (DERIVED; equal to the Hellmann-Feynman expectation of the perturbation to
$10^{-8}$):

| portal mean field | $\mathrm{d}\varepsilon_{\mathrm{DM}}/\mathrm{d}A_{\mathrm{mf}}$ | change of the fold-band gap |
| --- | --- | --- |
| I11, electron density ($v$) | $0.824779$ | $7.9\times10^{-11}$ |
| I11, up-quark density ($v$) | $4.328803$ | $3.0\times10^{-9}$ |
| I11, neutrino density ($v$, lepton doublet zero mode) | $1.252406$ | $-9.3\times10^{-11}$ |
| I12, gluon condensate (uniform $M_{\mathrm{eff}}$) | $0.707196$ | $-1.4\times10^{-10}$ |

(The changes of the fold-band gap are at the rounding level of the finite differences; in exact arithmetic every one is zero.)
The broad quark doublet zero mode ($c_L = 3.38$) overlaps the dark-matter orbital most. The fold band stays massless under
every portal. Every orbital has $\chi_2(-L) = 0$, so the scalar density vanishes at the tip: no tip operator built on
$\bar\Psi\Psi$ reaches dirac16complex; the upper component does not vanish there, so a chiral tip current would reach
$\Psi_A$ (the projector $P_L = (1 + \Gamma_4)/2 = (1 - \mathcal{B}\gamma^{x_0})/2$ annihilates every $\Psi_B$ orbital at the
tip), but UM-2 contains none (step 4). The I12 response defines the four-dimensional coefficient of the dark-matter operator,
$\mathcal{O}_{\mathrm{DM}} = 0.7072$:

@@i12dm@@

### The back-reaction on the block

A Kohn-Sham state with the block-averaged sources $\rho$, $p_3$ and the hidden pressure $\bar p = (p_0 + 3p_5)/4$ displaces
the block by the adiabatic response of step 1:

@@adiabatic@@

i.e. $\Delta K = [c_\rho\,\kappa(\rho - 3p_3) + c_p\,\kappa\bar p]/H^2$ (the hidden-pressure part has the stiffness
$-7.1414\,H^2$), without changing the four-dimensional cosmological term at linear order (the derivative of the $x_4$ balance
vanishes at $K_*$). Cell averages (units of the Kohn-Sham calculation, $H = 1$; DERIVED):

| state | $\rho - 3p_3$ | $\bar p$ | $p_0 - p_5$ | $\Delta K$ |
| --- | --- | --- | --- | --- |
| 8 quanta, $+\lambda_{\mathrm{test}}$ | $1.80\times10^{-5}$ | $-1.16\times10^{-5}$ | $-1.05\times10^{-5}$ | $2.27\times10^{-6}\,\kappa$ |
| 592 quanta, $+\lambda_{\mathrm{test}}$ | $0.0987$ | $-0.0636$ | $-0.0574$ | $0.0125\,\kappa$ |
| 592 quanta, $\lambda = 0$ (free gas) | $0$ | $0$ | $0$ | $-5\times10^{-13}\,\kappa$ (the numerical zero) |

The shift is negligible for any realistic density (relative size $(\mathcal{H}/H)^2$, step 1). The difference $p_0 - p_5$
drives a block-shape mode outside the order-0 metric (OPEN).

## The check of step 3

**In its own equations.**

* *Self-consistency.* The state of 8 quanta at $+\lambda_{\mathrm{test}}$, re-solved with the same solver (one BLAS thread), reproduces
  the stored $E_{\mathrm{KS}}$, HOMO, LUMO and the integrated $p_0$ and $\rho$ to $7.4\times10^{-14}$ (absolute, units $H$; another
  BLAS kernel rounds the eigenvalues of these matrices, whose basis energies reach $583\,H$, differently by up to about
  $5\times10^{-13}\,H$); one further Kohn-Sham map of the converged densities moves them by $1.8\times10^{-14}$ of their maximum
  (DERIVED).
* *The identities of a Kohn-Sham state.* The energy identity $E_{\mathrm{KS}} = 2\,\mathrm{Vol}_7\int\mathrm{e}^{3Hy}\rho\,
  \mathrm{d}y$ holds to the storage precision for all eight stored states ($4\times10^{-15}$ in the computation), and the
  $y$-conservation law to $8.8\times10^{-8}$ (Richardson; the raw residual falls like the inverse cube of the basis size); the
  observed basis orders are 4.96 (energy; 4.956 after the precision fix, version 3 quoted 4.95) and 2.97 (hidden pressure);
  the record states agree to $4.1\times10^{-10}$ (DERIVED).

**In concert with the other field equations.**

* *The Kohn-Sham source in the gravitational equations.* The block averages $\rho$, $p_3$, $\bar p$ of the Kohn-Sham states
  that enter the block response are the integrals of the Kohn-Sham energy-momentum tensor divided by the cell weight, to
  $3.4\times10^{-12}$; the block shifts recomputed from the stored integrals with the coefficients of the background equations
  agree with the stored ones to $1.4\times10^{-12}$, and for the free gas ($p_3 = \rho/3$) the response vanishes to
  $9.1\times10^{-13}$ of $c_\rho\kappa\rho$, as the exact cancellation of radiation requires (DERIVED).
* *The hidden pressure of the dark matter in three field equations.* The ratio $p_0/\rho$ of the Kohn-Sham stress tensor
  ($0.772034343201$), the block sensitivity of the $x_0$ eigenvalue in closed form ($0.772034343201$) and by finite difference
  ($0.772034343206$), and the value that the coupled block response of step 8 uses, agree to $6.1\times10^{-12}$ (DERIVED).
* *The portal responses.* The Hellmann-Feynman responses of the Kohn-Sham jobs equal the overlaps used in the coupled
  solution of step 8 to $3.0\times10^{-12}$, and $\mathcal{O}_{\mathrm{DM}} = \partial\varepsilon_{\mathrm{DM}}/\partial
  m_\Psi = 0.707196002672$ (Kohn-Sham, closed form, and the integral of the scalar density that enters the $W$ problem of step
  8) agrees with the rounded $0.7072$ of the relic and mean-field computations to $5.7\times10^{-6}$ (DERIVED).

## The status of step 3

DERIVED: the Kohn-Sham states, their energies, energy-momentum tensors and identities, the dark-matter quanta and their
hidden pressure, the portal responses, the block response to the Kohn-Sham sources. RECORD: the Kohn-Sham functional and the
reference states. INVENTED: the portals. ASSUMED: the bound on the self-coupling (step 9). OPEN: correlation beyond the local
exchange; the block-shape mode driven by $p_0 - p_5$.
