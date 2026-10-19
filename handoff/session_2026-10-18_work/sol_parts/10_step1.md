# Step 1: the background and the primordial era

## The field equations of step 1

The gravitational field is the metric $g_{MN}$ of the eight coordinates. Its action is the Einstein-Lovelock action with the
author's weights, and the block of the hidden direction and the extra times is held by a stabiliser:

@@T:Einstein-Lovelock gravity@@

@@T:The Lovelock densities@@

@@T:The block stabiliser@@

Varying the action with respect to the metric gives the Einstein-Lovelock equations, sourced by the energy-momentum tensor
of all fields:

@@el@@

@@tmn_def@@

@@t_total@@

At order 0 the source is dominated by the stabiliser, whose energy-momentum tensor is exact:

@@t_stab@@

The Lovelock tensors are divergence-free, so the source is conserved:

@@conservation@@

At order 0 the metric is the corrected primordial metric of the record, with two functions $a_4(x_4)$ and $b_4(x_4)$ of the
time. In the chart of the hidden coordinate $y$ it is a warped product of an expanding 3-space with the block:

@@bg_metric@@

@@bg_ychart@@

Its curvature is pair-diagonal and does not depend on $x_0$; the Lovelock densities and tensors are then sums of products
of the sectional curvatures:

@@sectional@@

@@lov_pair@@

@@lov_E1@@

@@lov_E2@@

@@lov_E3@@

With the author's weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ and $\Lambda = -10H^2$, the field equations of the order-0
metric are three ordinary differential equations: the $x_4$ component is a constraint, and the 3-space and hidden
components are linear in $\dot{\mathcal{H}}$ and $\dot{\mathcal{H}}_f$ (the extra-time components $x_5$, $x_6$, $x_7$ have the same
left side as the hidden one). These are the equations that step 1 solves:

@@bg_x4@@

@@bg_x1@@

@@bg_x0@@

@@bg_cons@@

## The approximation of step 1

**Order 0 of the metric series.** The background keeps only the order-0 term of the metric series (written out in "The
approximation scheme"). The order-1 terms average to zero in the block-averaged background equations, and their
back-reaction is of second order: on cosmological scales the omitted order is
$\Phi_{\mathrm{rms}}^2 = 5.8\times10^{-10}$ of the background, i.e. $2.4\times10^{-5}$ of the kept first order (step 10).

**A block-isotropic source.** The hidden and extra-time components of the order-0 Lovelock tensors coincide identically,
so the order-0 metric admits only sources with $p_0 = p_5$; for $p_0 \ne p_5$ the hidden component is the variation with
respect to the common block scale $f$, with the hidden pressure $\bar p = (p_0 + 3p_5)/4$, and the difference $p_0 - p_5$
drives a block-shape mode outside the order-0 metric (OPEN). This difference is not small against the kept hidden pressure
(0.9 for the self-interacting Kohn-Sham test states of step 3 and 4 for dark matter at rest, whose $p_5 = 0$), but its
absolute size is suppressed like that of $\bar p$, by $10^{-32}$ or more against the stabiliser (below).

**The static block plus its first-order response.** After the primordial era the matter sources are tiny against the
stabiliser: with the constraint $3\mathcal{G}(K_*)\,\mathcal{H}^2 = \kappa\Delta\rho$ of the response,

$$
\frac{\kappa\Delta\rho}{\kappa\rho_{\mathrm{stab}}(f_*)} = 0.7592\,\frac{\mathcal{H}^2}{H^2}:\qquad
\begin{aligned}&2.96\times10^{-32}\ \ \text{at the dark-matter freeze-out},\\
&2.4\times10^{-93}\ \ \text{for the cosmic mean today},\end{aligned}
$$

<!-- symbols: AUTO -->

so the block responds linearly. The terms of second order in the sources are smaller than the first-order response by a
factor of the same size ($2.3\times10^{-32}$ at the freeze-out, the largest source of the model), and the response is adiabatic: the
inertia of the block, $\Delta\ddot K$ against $\omega_{\mathrm{r}}^2\Delta K$, is of the relative size

$$
\frac{\lvert\Delta\ddot K\rvert}{\omega_{\mathrm{r}}^2\,\lvert\Delta K\rvert} \sim \frac{\mathcal{H}^2}{\omega_{\mathrm{r}}^2}
 = 3.4\times10^{-33}\ \ \text{at the dark-matter freeze-out}.
$$

<!-- symbols: AUTO -->

**The primordial era** is solved without approximation in the order-0 equations (numerically); the radiation of zero modes
that is added in one run changes the final block by $1.0\times10^{-6}$.

## The solution of step 1

### The static block

For $\mathcal{H}_f = 0$ and $\dot{\mathcal{H}} = 0$ the three background equations become algebraic:

@@static@@

Without a source and with $\mathcal{H} = 0$ the only static block is $K = 1/(4w_{(2)}) = 8$, which would need
$\Lambda = -24H^2$ and has $\mathcal{G} = -1$: four-dimensional gravity would be repulsive. The stabiliser removes this
obstruction with the author's weights and $\Lambda = -10H^2$ unchanged (DERIVED):

@@stabiliser@@

$\mathcal{G}(K_*) = 13.8081 > 0$: four-dimensional gravity is attractive. The normalisation of the stabiliser is
$\kappa\rho_{\mathrm{stab}}(f_*) = 54.566\,H^2$.

### Stability: the radion

Linearised about the static block, the background equations give a closed system for $(\Delta\mathcal{H},
\Delta\mathcal{H}_f, \Delta K)$ with the eigenvalues $0$ and $\pm\mathrm{i}\,\omega_{\mathrm{r}}$ (DERIVED, exact):

@@radion@@

The block is stable and oscillates with the radion frequency $\omega_{\mathrm{r}} = 3.38705\,H$, i.e. the radion mass
$48.42$ TeV; the zero eigenvalue belongs to $\Delta\mathcal{H}$ (a small four-dimensional cosmological term). Every
stabiliser of the family whose hidden pressure is a fixed multiple, from $1/4$ to $3$, of its energy density gives a stable
block, with $\omega_{\mathrm{r}} = 3.33\,H$ to $4.10\,H$ (DERIVED).

### The primordial era: the deflating extra times

The three background equations, with the stabiliser $\kappa\rho_{\mathrm{stab}} = \kappa\rho_{\mathrm{stab}}(f_*)\,(K/K_*)^4$,
$p_3 = -\rho_{\mathrm{stab}}$, $\bar p = \rho_{\mathrm{stab}}$ (plus radiation where stated), were integrated from an
expanding 3-space and a block larger than the stabilised one ($K < K_*$ at the start, $x_4 = 0$) that deflates at the rate
$\mathcal{H}_f = -H/2$, $-H/3$ or $-H/10$ (DERIVED; DOP853, relative tolerance $10^{-11}$). The value of $K$ at
$x_4 = 60/H$:

| start $K$ | $\mathcal{H}_f = -H/10$ at the start | $\mathcal{H}_f = -H/3$ | $\mathcal{H}_f = -H/2$ |
| --- | --- | --- | --- |
| 1.5 | singular at $x_4 = 1.44/H$ | singular at $1.26/H$ | singular at $1.14/H$ |
| 2.3 | singular at $0.33/H$ | singular at $0.31/H$ | no expanding start |
| 2.7 | $21.415$ | $21.435$ | $21.451$ |
| 3 | $21.412$ | $21.434$ | $21.455$ |
| 6 | $21.405$ | $21.453$ | $21.500$ |
| 10 | $21.446$ | $21.541$ | $21.584$ |
| 20 | $21.634$ | $21.640$ | $21.638$ |

Every start above the separatrix $K_{\mathrm{sep}} = 2.5301$, $2.5991$, $2.6983$ (for the initial rates $-H/10$, $-H/3$,
$-H/2$; just above the unstable static block $K_- = 2.4781$) ends at the stable block: the extra times $x_5, x_6, x_7$ and
the hidden direction $x_0$ deflate at rates up to $\lvert\mathcal{H}_f\rvert = 2.63\,H$ (in the stored runs with the start
$K = 3, 5, 10$), by up to the factor $f(K_{\mathrm{sep}})/f_* = 2.917$, reach $K_*$ within $x_4 < 1/H$, and then oscillate
about it with the radion frequency ($3.3868\,H$ measured, $3.3870\,H$ linear), while 3-space keeps expanding; the
oscillation energy redshifts like dust ($\mathcal{H}\,x_4 \to 0.667$ to $0.670$; $2/3$ for dust). The extra times therefore
deflate only in a short primordial era and are then frozen: the masses, all of which depend on $f$ (step 2), become constant.

![The primordial era: the block scale $f$, the expansion rate $\mathcal{H}$ of 3-space and the block rate $\mathcal{H}_f$ for the starts $K = 3, 5, 10$ with the initial rate $\mathcal{H}_f = -H/3$ (one with radiation), from the full nonlinear Einstein-Lovelock equations with the author's weights. The panels label $K$, $\mathcal{H}$ and $\mathcal{H}_f$ with the letters $k$, $A$ and $h$ of version 3.](figures/fig_primordial_history.png)

### The response of the block to matter

To first order about the static block, with the block-averaged matter sources and $\mathcal{H}^2$ counted as of first order
(the constraint gives $3\mathcal{G}(K_*)\,\mathcal{H}^2 = \kappa\Delta\rho$ because $\mathrm{d}[6H^2K(1 - 2w_{(2)}K) +
\kappa\rho_{\mathrm{stab}}]/\mathrm{d}K$ vanishes at $K_*$), the block obeys a driven oscillator equation (DERIVED, exact):

@@response@@

@@response_coeffs@@

For a slowly varying source the block follows it adiabatically, and 3-space obeys the four-dimensional Friedmann
acceleration equation exactly:

@@adiabatic@@

with $c_\rho = 0.035852$, $c_3 = -0.107556$, $c_p = -0.140028$: radiation ($\Delta p_3 = \Delta\rho/3$) drops out exactly
($c_3 = -3c_\rho$), so only the trace $\Delta\rho - 3\Delta p_3$ and the hidden pressure move the block. The hidden-pressure
part alone is $\Delta K = \kappa\Delta\bar p/(3H^2 - 4\kappa\rho_{\mathrm{stab}}(f_*)/K_*)$, a stiffness of $-7.1414\,H^2$.

### Four-dimensional gravity

On a product of a four-dimensional metric with the static block the Lovelock densities factorise, and the eight-dimensional
action becomes the Einstein-Hilbert action with the coefficient $\mathcal{G}(K)$ (DERIVED, exact):

@@reduction@@

@@einstein4@@

Four-dimensional gravity on the stabilised block is general relativity, with $\Lambda_4 = 0$ at the static point. The
observed dark energy needs $\Lambda_4/H^2 \sim (\mathcal{H}_0/H)^2 = 1.0\times10^{-92}$, a tuned residual (OPEN).

## The check of step 1

**In its own equations.**

* *The static block in the background equations.* Substituted into the printed $x_4$, $x_1$ and $x_0$ equations, the stored
  $K_* = 21.5219045714$ and $\kappa\rho_{\mathrm{stab}}(f_*) = 54.5657137142\,H^2$ leave the residual $3.9\times10^{-13}$ of
  the largest term ($1.2\times10^{-16}$ with the closed forms), and the printed polynomials equal the code's symbolic field
  equations exactly (DERIVED, `um2_residuals.py`).
* *The primordial trajectories in the background equations.* The constraint $x_4$ holds at the 1604 stored samples to
  $3.6\times10^{-12}$ of the sum of its terms ($5.6\times10^{-10}$ absolute over the whole integration), and the one-step
  defect of the stored trajectory, re-integrated over $0.1/H$ from every fifth sample, is $1.3\times10^{-11}$ in units of $H$
  (DERIVED).
* *The first-order response in the nonlinear equations.* The adiabatic solution substituted into the full nonlinear
  equations leaves a residual of second order, as it must: for sources $\kappa(\Delta\rho, \Delta p_3, \Delta\bar p) =
  \epsilon(1, 0.2, 0.7)\,H^2$ the residual is $1.4\times10^{-6}$ at $\epsilon = 10^{-4}$ and $1.4\times10^{-7}$ at
  $\epsilon = 10^{-5}$ (ratio $0.10$), and the cancellation of radiation, $c_3 + 3c_\rho$, holds to $2\times10^{-13}$ (DERIVED).
* *The four-dimensional reduction.* $\Lambda_4(K_*) = 0$ and $\mathrm{d}[6H^2K(1 - 2w_{(2)}K) + \kappa\rho_{\mathrm{stab}}]
  /\mathrm{d}K = 0$ at $K_*$ hold to $3.9\times10^{-13}$ of the largest term with the stored numbers and to $1.2\times10^{-16}$
  with the closed forms (the exact values are 0; version 3 quoted the stored $-6\times10^{-12}$ of the derivative, which is
  this rounding), and the coefficient of $R^{(4)}$ equals $\mathcal{G}(K)$ symbolically (DERIVED).

**In concert with the other field equations.**

*The spinor equations on the static block.* Every spinor of UM-2 couples to the metric through the canonical spin
connection, which on the order-0 metric is exactly

@@gomega@@

On the static block ($\dot a_4 = \dot b_4 = 0$) it reduces to $\tfrac32(H/f_*)\gamma^{x_0}$, which the factor
$\mathrm{e}^{-\frac32Hy}$ of the reduction of step 2 removes exactly; the masses of step 2 and the Kohn-Sham states of
step 3 are therefore solutions on this background.

* *The radion frequency of the linear analysis and of the nonlinear integration.* The closed form
  $\omega_{\mathrm{r}} = 3.387049962\,H$ and the frequency $3.386781524\,H$ measured from the zero crossings of the nonlinear
  primordial oscillation (relative amplitude $3\times10^{-3}$) agree to $7.9\times10^{-5}$ (DERIVED).
* *The block scale in every other equation.* The block scale $f_* = 0.215555768391$ of the static block is the one used in
  the $x_0$ spectra (step 2), the Kohn-Sham states (step 3) and the metric series (step 10), to $2.2\times10^{-12}$; the
  response coefficients used in steps 3 and 8 are those of the background equations to $2\times10^{-13}$ (the printed six
  decimals within $2.6\times10^{-7}$) (DERIVED).
* *The Friedmann equation of the thermal history.* At the dark-matter freeze-out the four-dimensional Friedmann equation with
  $8\pi G_{\mathrm{N}} = \kappa/(\mathcal{G}(K_*)V_\perp)$ and all species gives an expansion rate $1.7\times10^{-4}$ above
  the one used in the Boltzmann equation of step 9, because the thermal history leaves out the fold bands of dirac16complex
  ($3.5\times10^{-4}$ of the energy density then); the relic density moves by about the same relative amount, a tenth of the
  precision of the measured dark-matter density (DERIVED).

## The status of step 1

DERIVED (exact, symbolic): the Lovelock tensors of the order-0 metric, the three background equations, the static block and
$K_*$, $\mathcal{G}(K_*)$, the radion frequency, the first-order and the adiabatic response, the four-dimensional reduction.
DERIVED (numerical): the primordial era. ASSUMED: the stabiliser (its microscopic origin is OPEN). OPEN: the block-shape mode
driven by $p_0 - p_5$; the tuning of $\Lambda_4$ (dark energy).
