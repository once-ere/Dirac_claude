# Dimensional reduction and the four-dimensional constants

The good sector (no dependence on $x_5$, $x_6$, $x_7$) is kept (ASSUMED): a mode with the wave number $k_{\mathrm{t}}$ along the extra times has
the squared energy

$$
\varepsilon^2 = M^2 + k^2 - \frac{k_{\mathrm{t}}^2}{f^2}
$$
<!-- symbols: AUTO -->

and is tachyonic for $k_{\mathrm{t}} > fM$ (OPEN). The extra times are compact with the coordinate volume $v_{\mathrm{t}}$ (ASSUMED). Integrating
over one period of $x_0$ (both halves) and the extra times, the four-dimensional theory on the static block has (DERIVED)

@@FE-49@@

with the reduced Planck mass

$$
\bar M_{\mathrm{Pl}}^2 = \frac{\mathcal{G}(K_*)\,V_\perp}{\kappa} = \frac{1}{8\pi G_{\mathrm{N}}} .
$$
<!-- symbols: AUTO -->

Every four-dimensional constant depends on the block (DERIVED): $\alpha_{\mathrm{em}}$ and the gauge couplings $\propto f^{-4}$; Newton's constant
$G_{\mathrm{N}} \propto f^{+2.05}$, because the Lovelock factor varies too,

$$
\frac{\mathrm{d}\ln G_{\mathrm{N}}}{\mathrm{d}\ln f} = -4 + 2\,\frac{\mathrm{d}\ln\mathcal{G}}{\mathrm{d}\ln K}\Big\vert_{K = K_*} = 2.05 ;
$$
<!-- symbols: AUTO -->

the Kaluza-Klein masses $\propto f^{-1}$, $m_{\mathrm{W}} \propto f^{-0.501}$, $M_{\mathrm{DM}} \propto f^{-0.772}$, and the fermion masses
$m = \tilde\varepsilon/(fL)$, from the first-order root of the mass condition (written out again)

@@FE-59@@

with localisations $c = f\mu L$ proportional to $f$:

@@FE-85@@

$-6.8$ (top quark) to $-41.0$ (lightest neutrino), with $-20.5$ for the electron. The masses are constant only because the block is
stabilised. A continuing deflation today is excluded (ESTIMATE, bounds from memory): since $\mathrm{d}\ln X/\mathrm{d}x_4 = (\mathrm{d}\ln X/\mathrm{d}\ln f)\,
\mathcal{H}_f$ for every quantity $X$, the atomic-clock bound $\lvert\mathrm{d}\ln\alpha_{\mathrm{em}}/\mathrm{d}x_4\rvert < 10^{-17}$ per year requires
$\lvert\mathcal{H}_f\rvert < 2.5\times10^{-18}$ per year $= 3.6\times10^{-8}\,\mathcal{H}_0$, and lunar ranging
($\lvert\mathrm{d}\ln G_{\mathrm{N}}/\mathrm{d}x_4\rvert < 10^{-13}$ per year) requires $\lvert\mathcal{H}_f\rvert < 7.1\times10^{-4}\,\mathcal{H}_0$; a block deflating at the
Hubble rate would change the electron mass by $1.4\times10^{-9}$ per year. The extra times are irrelevant at low energies not because they keep
deflating but because they are small (the proper half cell $f_*L = 8.9\times10^{-21}$ m, Kaluza-Klein masses above 100 TeV) and frozen.

# Gravity: the background, the stabilised block, the deflating extra times and four-dimensional gravity

## The background field equations and their solutions (DERIVED)

### The field equations of the order-0 metric

The gravitational field equations are the Einstein-Lovelock equations with the source of all fields (written out again):

@@FE-1@@

@@FE-2@@

For the order-0 metric the curvature is pair-diagonal, with the sectional curvatures (written out again)

@@FE-33@@

and for a pair-diagonal curvature the Lovelock densities and tensors are sums over disjoint pairs (written out again):

@@FE-34@@

The three Lovelock tensors of the order-0 metric are therefore (exact, sympy, four routes)

@@FE-35@@

@@FE-36@@

@@FE-37@@

Every off-diagonal component of every Lovelock tensor vanishes and the hidden and extra-time components coincide, so the source must
be diagonal, independent of $x_0$ and block-isotropic ($p_0 = p_5$ in FE-2). The three independent components are the $x_4$
constraint (first order in time derivatives), the 3-space component and the block component; the last two are linear in
$(\dot{\mathcal{H}}, \dot{\mathcal{H}}_f)$. With the author's weights and $\Lambda = -10H^2$ they are (DERIVED, sympy):

@@FE-38@@

@@FE-39@@

@@FE-40@@

and the source is conserved:

@@FE-41@@

A source with $p_0 \ne p_5$ (the Kohn-Sham states of $\Psi$ and the matter at the fold have it; the dark matter has $p_0/\rho = 0.772$,
$p_5 = 0$) acts on the common block scale $f$ through the block-averaged pressure $\bar p = (p_0 + 3p_5)/4$ (the variation of the action with
respect to $f$), while $p_0 - p_5$ drives a block-shape mode that the order-0 metric does not contain (OPEN). The residual analysis quantifies
it: the shape source is about 4 times the kept $\bar p$ for non-relativistic dark matter (0.9 for the self-interacting test states), with an
absolute size suppressed like that of $\bar p$ ($\kappa p/\kappa\rho_{\mathrm{stab}} \le 3\times10^{-32}$ at the freeze-out), if the shape mode is stable
(OPEN); for matter its size relative to the stabiliser is of order $(\mathcal{H}/H)^2$, $10^{-92}$ today.

To first order about the static block with block-averaged matter sources ($\mathcal{H}^2$ counts as first order: the $x_4$ constraint gives
$3\mathcal{G}(K_*)\mathcal{H}^2 = \kappa\Delta\rho$, because the $K$ derivative of the static balance vanishes at $K_*$) the equations give (DERIVED)

@@FE-45@@

with the coefficients (exact, sympy; numerically $0.272956H^2$, $0.266522H^2$, $-0.006853$, $0.038221$, $-0.045997$, $0.028666$, $0.037320$,
$-0.009555$)

@@FE-46@@

In the adiabatic response (the second time derivative of $\Delta K$ neglected) the block shifts and 3-space obeys exactly the
four-dimensional Friedmann acceleration equation (with $c_\rho = 0.035852$, $c_3 = -0.107556$, $c_p = -0.140028$):

@@FE-47@@

with $8\pi G_{\mathrm{N}} = \kappa/(\mathcal{G}(K_*)V_\perp)$. Radiation ($p_3 = \rho/3$) drops out of the block response exactly ($c_3 = -3c_\rho$).

### The static block and attractive gravity with the author's weights (DERIVED)

For a static block ($\mathcal{H}_f = 0$, $K$ constant) and $\dot{\mathcal{H}} = 0$ the components are

@@FE-42@@

$\mathcal{G}(K)$ is the coefficient of the four-dimensional Einstein-Hilbert term (FE-48 below): four-dimensional gravity is attractive for
$\mathcal{G} > 0$. Without sources the only static block with $\mathcal{H} = 0$ is $K = 1/(4w_{(2)}) = 8$, which needs the cosmological constant
$-24H^2$ and has $\mathcal{G} = -1$: with the author's weights the sourceless block has REPULSIVE gravity, and the author's $\Lambda = -10H^2$ is
not the value it needs. For the author's weights $\mathcal{G}(K) = (K^2 - 12K + 16)/16$, positive only for $K < 6 - 2\sqrt5$ or
$K > 6 + 2\sqrt5 = 10.47$. With the block stabiliser ($p_3 = -\rho_{\mathrm{stab}}$, $p_0 = p_5 = \rho_{\mathrm{stab}}$) and $\mathcal{H} = 0$ the two
conditions give the stabilised block:

@@FE-43@@

The upper root is the UM-2 vacuum, with attractive four-dimensional gravity and the author's weights and $\Lambda$ unchanged; the lower root
$K_- = 2.4781$ has $\mathcal{G} = -0.4748$.

### Stability: the radion (DERIVED)

Linearising the 3-space and block components (solved for $\dot{\mathcal{H}}$ and $\dot{\mathcal{H}}_f$) with $\dot K = -2K\mathcal{H}_f$ and
$\rho_{\mathrm{stab}} \propto K^4$ about $K_*$:

@@FE-44@@

with the eigenvalues $0$ and $\pm\mathrm{i}\,\omega_{\mathrm{r}}$: the block is stable and oscillates; the zero eigenvalue is the direction of a small
four-dimensional cosmological term. The radion (the quantum of block-size oscillations) has the mass $\omega_{\mathrm{r}} = 3.38705H = 48.42$ TeV.
Stability holds for each of the stabiliser laws whose hidden pressure is $\frac14$, $\frac12$, $\frac34$, $1$, $\frac54$, $\frac32$, $2$ or $3$ times their
energy density (radion masses $3.33H$ to $4.10H$).

### The deflating extra times (DERIVED, full nonlinear equations)

The full nonlinear equations FE-38 to FE-40 of this section (all three components, the $x_4$ constraint preserved to $6\times10^{-10}$) were integrated from an
expanding 3-space ($\mathcal{H}$ from the constraint) and a block LARGER than the stabilised one ($K < K_*$ initially, i.e. $f > f_*$) that
deflates at $\mathcal{H}_f = -H/2$, $-H/3$, $-H/10$, for initial $K$ from 1.5 to 20. Every start with $K$ above the separatrix $2.6983$, $2.5991$,
$2.5301$ (for the three initial rates; just above the unstable static block $K_- = 2.4781$, whose stable manifold the separatrix is) ends at
$K_*$: $x_5$, $x_6$, $x_7$ and $x_0$ deflate (at rates up to $\lvert\mathcal{H}_f\rvert = 2.63H$ in the stored runs) by up to the factor
$(K_*/2.6983)^{1/2} = 2.917$, reach $K_*$ for the first time within $x_4 < 1/H$, and then oscillate about $K_*$ with the radion frequency
($3.3868H$ measured, $3.3870H$ linear; the relative difference $7.9\times10^{-5}$ is the anharmonicity of a finite oscillation, residual
analysis), while 3-space keeps expanding; the oscillation energy redshifts like dust ($\mathcal{H}x_4 = 0.667$ to $0.670$ late, $2/3$ for dust).
Starts below the separatrix (still larger blocks) become singular within $x_4 = 0.2/H$ to $1.4/H$ or admit no expanding initial data. The
extra times therefore deflate exponentially only for a short primordial era and are then frozen, which is what the constancy of the masses
requires (the previous section).

![Deflation of the extra times into the stabilised block (full nonlinear Einstein-Lovelock equations with the author's weights).](figures/fig_primordial_history.png)

## The four-dimensional effective gravity (DERIVED)

On a product of a four-dimensional metric with the static block (constant curvature $-H^2K$), the Lovelock densities factorise; the
four-dimensional quadratic density is topological and the cubic one vanishes in four dimensions, so the reduced Lagrangian (gravity plus the
stabiliser, in units of $1/(2\kappa)$) is

@@FE-48@@

and the four-dimensional gravity of UM-2 is EXACTLY general relativity (written out again):

@@FE-49@@

The cosmological term $\Lambda_4$ vanishes at the static point by construction. The observed dark energy is a small residual of this balance,
$\Lambda_4/H^2 \sim (\mathcal{H}_0/H)^2 = 1.0\times10^{-92}$: tuned (the cosmological-constant problem, OPEN).

