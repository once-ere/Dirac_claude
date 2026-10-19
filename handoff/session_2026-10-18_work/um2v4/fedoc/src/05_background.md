
# The background

The background is order 0 of the metric power series (FE-87): the homogeneous metric of the author with the block of the
hidden direction and the three extra times, sourced by the block-averaged energy-momentum tensor of every field. Its equations
are exact; they are solved in closed form for the static block and numerically for the primordial approach to it.

## The order-0 metric and its curvature

@FE-31

**The terms.** The diagonal entries are, in the order $x_0, x_1, \dots, x_7$: the hidden direction, whose metric coefficient
$\mathrm{e}^{-2a_4}b_4\cot^2z$ depends on $x_0$ through the angle $z = 6Hx_0$ and on the time through $a_4(x_4)$ and $b_4(x_4)$; ordinary
space with the scale factor $\mathrm{e}^{a_4}$; the time $x_4$; and the three extra times, whose coefficient depends on $x_0$ through
$(\sin^2z)^{1/6}$. The metric is periodic in $x_0$ with the period $\pi/(6H)$. It is the metric of the gravitational field only: every
other field enters through the right side of FE-1. Status: AUTHOR (the corrected primordial metric of the record, in the author's
coordinates).

@FE-32

**The terms.** $y$ is the proper hidden coordinate in units of the block scale: in it the hidden direction and the extra times
form the block $f^2[\mathrm{d}y^2 - \mathrm{e}^{2Hy}(\dots)]$, a four-dimensional space of constant curvature $-H^2/f^2$ scaled by one
function $f$, the block scale. The variable $K = 1/f^2$ measures the curvature of the block, $\mathcal{H}$ is the expansion rate of
ordinary space (the Hubble rate) and $\mathcal{H}_f$ the rate of change of the block. One period of $x_0$ is two halves joined at
the fold $y = 0$ (where $\sin^2z = 1$); each half is closed by the regular tip $y = -L$, with $HL = 3$ (ASSUMED). The last line is
the volume element in both charts. Status: DERIVED (exact change of chart).

@FE-33

**The terms.** The curvature of the order-0 metric is pair-diagonal: the only non-zero components of the Riemann tensor are the
sectional curvatures of the coordinate planes, five kinds in all. $\mathcal{H}^2$ is the curvature of a plane of ordinary space,
$\mathcal{H}^2 + \dot{\mathcal{H}}$ that of a space-time plane, $\mathcal{H}\mathcal{H}_f$ that of a plane spanned by ordinary space and a block
direction, $\mathcal{H}_f^2 + \dot{\mathcal{H}}_f$ that of the plane of the time and a block direction, and $\mathcal{H}_f^2 - H^2K$ that of a
plane of two block directions, which contains the constant curvature of the block. None of them depends on $x_0$: the metric
depends on $x_0$, its curvature does not. Status: DERIVED (sympy, identical in both charts; 25 checks of the geometry).

@FE-34

**The terms.** For a pair-diagonal curvature the Lovelock density of order $p$ is $2^pp!$ times the sum over all sets of $p$
disjoint coordinate pairs of the product of their sectional curvatures, and the diagonal component $\mathcal{E}_{(p)}{}^c{}_c$ is
$-2^{p-1}p!$ times the same sum restricted to the pairs that avoid the direction $c$. This turns the Lovelock tensors of the
order-0 metric into polynomials of the five curvatures of FE-33. Status: DERIVED (checked against the Ricci route for $p = 1$, the
explicit Gauss-Bonnet tensor for $p = 2$, the Bianchi identities and the minisuperspace variation with a lapse for $p = 1, 2, 3$).

## The Lovelock tensors of the order-0 metric

@FE-35

**The terms.** The Einstein tensor of the order-0 metric. The $x_4$ component contains no time derivative of the rates (it is a
constraint); the $x_1$ and $x_0$ components contain $\dot{\mathcal{H}}$ and $\dot{\mathcal{H}}_f$. The term $6KH^2$ (and $3KH^2$) is the
curvature of the block. Every off-diagonal component vanishes, and the $x_0$ component equals the $x_5$, $x_6$, $x_7$ components:
all four block directions have the same left side. Status: DERIVED (exact).

@FE-36

**The terms.** The Gauss-Bonnet tensor: products of two sectional curvatures, so every term is of fourth order in the rates and
$H$ (with at most one time derivative of a rate). It is weighted by $\alpha_{(2)} = H^{-2}/32$ in FE-1. Status: DERIVED (sympy, four
routes).

@FE-37

**The terms.** The cubic Lovelock tensor: products of three sectional curvatures (sixth order), weighted by
$\alpha_{(3)} = H^{-4}/1152$. In eight dimensions it is the highest Lovelock order that contributes to the field equations. Status:
DERIVED (sympy, four routes).

## The background equations

On the order-0 metric every source is diagonal, $\mathcal{T}^{x_4}{}_{x_4} = -\rho$, $\mathcal{T}^{x_1}{}_{x_1} = p_3$,
$\mathcal{T}^{x_0}{}_{x_0} = p_0$, $\mathcal{T}^{x_5}{}_{x_5} = p_5$ (FE-2), and the field equations FE-1 reduce to one equation for each
kind of direction:

@@
\begin{aligned}
&\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\rho,\qquad
 \sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^{x_1}{}_{x_1} + \Lambda = \kappa p_3,\\
&\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^{x_0}{}_{x_0} + \Lambda = \kappa p_0,\qquad
 \sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^{x_5}{}_{x_5} + \Lambda = \kappa p_5.
\end{aligned}
@@

With the tensors of FE-35 to FE-37, the author's weights and $\Lambda = -10H^2$ they are:

@FE-38

**The terms.** The constraint: the terms divided by $H^4$ come from the cubic Lovelock tensor, those divided by $H^2$ from the
Gauss-Bonnet tensor, the others from the Einstein tensor; the terms with $K$ and $K^2$ are the curvature of the block entering
through the plane curvatures $\mathcal{H}_f^2 - H^2K$; $-10H^2$ is the cosmological constant. The right side is the total energy
density of every field (FE-3). Status: DERIVED. The residual of the stored static block in this equation is $3.9\times10^{-13}$ of
its largest term (from the twelve stored digits of $K_*$; with the closed form $1.2\times10^{-16}$), and the printed polynomial equals
the one in the code symbolically.

@FE-39

**The terms.** The 3-space equation is linear in $\dot{\mathcal{H}}$ and $\dot{\mathcal{H}}_f$ with coefficients that depend on the rates and on
$K$; it is the equation of motion of the scale factor of ordinary space, with the pressure $p_3$ of all matter along ordinary
space as its source. Status: DERIVED. With FE-40 it is solved for the two rates; the integration from the primordial block to the
static block preserves the constraint FE-38 to $6\times10^{-10}$.

@FE-40

**The terms.** The block equation is linear in $\dot{\mathcal{H}}$ and $\dot{\mathcal{H}}_f$ as well; it is the equation of motion of the
block scale. Its source is the pressure along the block: $p_0$ for the $x_0$ component and $p_5$ for the $x_5$, $x_6$, $x_7$
components. The left sides of the four block components are identical, so the order-0 metric (one scale $f$ for all four) solves
them all only for a block-isotropic source, $p_0 = p_5$; in general $f$ obeys the average with $\bar p$ (subsection "The block
pressures" below). Status: DERIVED. The primordial solutions of FE-38 to FE-40 (with the stabiliser and radiation) have a one-step
defect of $1.3\times10^{-11}$ and a constraint residual of $3.6\times10^{-12}$ when they are re-integrated from the stored samples.

@FE-41

**The terms.** The conservation law FE-11 on the order-0 metric: the energy density decreases by the work done by the pressure
along each direction, $p_3$ along the three directions of ordinary space (rate $\mathcal{H}$), $p_0$ along the hidden direction and $p_5$
along the three extra times (rate $\mathcal{H}_f$); the four block terms combine to $4\mathcal{H}_f(\rho + \bar p)$. For the stabiliser
($p_0 = p_5 = \rho_{\mathrm{stab}}$, $p_3 = -\rho_{\mathrm{stab}}$) it gives $\dot\rho_{\mathrm{stab}} = -8\mathcal{H}_f\rho_{\mathrm{stab}}$, so
$\rho_{\mathrm{stab}} \propto f^{-8}$ as assumed in IN-4. Status: DERIVED.

## The block pressures

The block scale $f$ multiplies the four block directions together, so the action depends on it through the sum of the four
block components. For a change $\Delta\ln f$ of the block scale ($\Delta g^{MM} = -2g^{MM}\Delta\ln f$ for the four block directions),
the change of the action is the sum of the four block equations, and because their left sides are equal,

@@
\begin{aligned}
\frac{\Delta S}{\Delta\ln f} &= -\frac{1}{\kappa}\sqrt{\lvert g\rvert}\sum_{M\in\{x_0,\,x_5,\,x_6,\,x_7\}}
 \Big(\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^M{}_M + \Lambda - \kappa\,\mathcal{T}^M{}_M\Big)\\
 &= -\frac{4}{\kappa}\sqrt{\lvert g\rvert}\,\Big(\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^{x_0}{}_{x_0} + \Lambda -
 \kappa\bar p\Big),\qquad \bar p = \tfrac14\big(p_0 + 3p_5\big).
\end{aligned}
@@

So the equation of motion of $f$ is the block equation FE-40 with the hidden pressure $\bar p$, the average of the block pressures.
The difference of the block pressures,

@@
p_0 = \bar p + \tfrac34\big(p_0 - p_5\big),\qquad p_5 = \bar p - \tfrac14\big(p_0 - p_5\big),
@@

cannot be absorbed by $f$: it would change the shape of the block (the proper length of the hidden direction against that of the
extra times), a mode outside the order-0 metric. This block-shape mode and its response to $p_0 - p_5$ are not computed in UM-2
(OPEN). The physically correct block equations are therefore: the $x_0$ component with $p_0$, the extra-time components with $p_5$,
and, for the order-0 metric, their average with $\bar p$.

The sources of UM-2 are:

* the stabiliser: block-isotropic, $p_0 = p_5 = \rho_{\mathrm{stab}}$, so $\bar p = p_0 = p_5$ and its static block (FE-42, FE-43) is an
  exact solution of all eight components;
* the Standard-Model plasma and matter, and the dark matter: the masses of the zero modes and of the dark matter depend on the
  proper length of the hidden direction only (they are $x_0$ eigenvalues), so their mass terms contribute to $p_0$ only, $p_0 =
  -(\rho - 3p_3)\,\mathrm{d}\ln m/\mathrm{d}\ln f$ for an ideal gas, and nothing to $p_5$ for quanta without momentum along the extra times;
  the parts of the plasma pressure that depend on the gauge couplings (the four-dimensional couplings scale with the volume
  $V_\perp$ of all four block directions, FE-82, and with them the QCD scale, FE-84) contribute to $p_0$ and $p_5$ alike; for the dark
  matter at rest $p_0/\rho = -\mathrm{d}\ln\varepsilon_{\mathrm{DM}}/\mathrm{d}\ln f = 0.772034$ and $p_5 = 0$, so $\bar p = p_0/4$ and
  $\lvert p_0 - p_5\rvert/\bar p = 4$;
* the Kohn-Sham states of dirac16complex: $p_0$ and $p_5$ from FE-67; for the self-interacting test states
  $\lvert p_0 - p_5\rvert/\bar p = 0.90$.

The block-shape source is therefore not small compared with the hidden pressure that is kept; its absolute size is suppressed like
that of $\bar p$, at most $3\times10^{-32}$ of the stabiliser (at the dark-matter freeze-out), if the shape mode is stable (OPEN).

**What the code does.** The background code `um2_background.py` writes the block equation once, for "$x_0 = x_5 = x_6 = x_7$", with
one symbol for the block pressure; it is used only for block-isotropic sources: the stabiliser ($p_0 = p_5 = \rho_{\mathrm{stab}}$; and
the stability family $p_0 = p_5 = \nu\rho_{\mathrm{stab}}$, $\nu = \frac14$ to 3), for which that symbol equals $p_0$, $p_5$ and $\bar p$ alike.
Its first-order response to matter (FE-45 to FE-47) is written for $\Delta\bar p = \frac14(\Delta p_0 + 3\Delta p_5)$. The Kohn-Sham job
`um2_ks_jobs.py` (feedback) forms $\bar p = \frac14(p_0 + 3p_5)$ from the cell averages of FE-67 and stores $p_0 - p_5$ separately; the
coupled solution `um2_coupled.py` uses $\bar p = \frac14\,\mathrm{d}p/\mathrm{d}\ln f$ at fixed temperature (FE-81), which is
$\frac14(p_0 + 3p_5)$ for every source, because a change of $\ln f$ scales the four block directions together (for the mass terms
$p_5 = 0$ and it is $p_0/4$); and the residual analysis `um2_residuals.py` recomputes the response with
$\bar p = \frac14(p_0 + 3p_5)$ and reports the block-shape source. No stored number rests on an inconsistent choice of the block
pressure. Version 3 of the UM-2 documents wrote $\kappa\bar p$ in the block equation of the static block and the stabiliser, and in one
place $\kappa p_0$: both are correct there, because the stabiliser is block-isotropic, and $K_\pm$, $\mathcal{G}(K_*)$, $\kappa\rho_{\mathrm{stab}}(f_*)$ and $\omega_{\mathrm{r}}$
do not depend on the choice.

## The static block and the stabiliser

A static block has $\mathcal{H}_f = 0$ and $\dot{\mathcal{H}}_f = 0$. With $\dot{\mathcal{H}} = 0$ the background equations become:

@FE-42

**The terms.** $\mathcal{G}(K)$ multiplies $\mathcal{H}^2$ in the constraint; it is the coefficient of the four-dimensional Einstein-Hilbert term
(FE-48), so four-dimensional gravity is attractive where $\mathcal{G} > 0$, i.e. for $K < 6 - 2\sqrt5$ or $K > 6 + 2\sqrt5 = 10.47$. The
term $6H^2K(1 - 2w_{(2)}K)$ is the curvature energy of the block (Einstein and Gauss-Bonnet); in the block equation $3H^2K$. The
sources are $\kappa\rho$ (constraint), $\kappa p_3$ (3-space), $\kappa p_0$ (hidden direction) and $\kappa p_5$ (extra times). Without
sources and with $\mathcal{H} = 0$ the only static block is $K = 8$, which would need $\Lambda = -24H^2$ (not the author's $-10H^2$) and has
$\mathcal{G} = -1$, repulsive gravity: with the author's weights the block must be held by a source. Status: DERIVED (exact).

At $\mathcal{H} = 0$ the constraint and the block equation read

@@
x_4:\ 6H^2K - \tfrac38H^2K^2 - 10H^2 = -\kappa\rho,\qquad x_0:\ 3H^2K - 10H^2 = \kappa p_0,
@@

and with the stabiliser as the only source ($\rho = p_0 = p_5 = \rho_{\mathrm{stab}}$, $p_3 = -\rho_{\mathrm{stab}}$, FE-4) they require

@@
10H^2 - 6H^2K + \tfrac38H^2K^2 = 3H^2K - 10H^2\quad\Leftrightarrow\quad 3K^2 - 72K + 160 = 0\quad\Leftrightarrow\quad
K = 12 \pm \tfrac43\sqrt{51}:
@@

@FE-43

**The terms.** The first line gives the stabiliser density required by the constraint and by the block equations; the
stabiliser is block-isotropic, so the $x_0$ and the extra-time equations coincide and the static block is an exact solution of
all components (the 3-space equation is the constraint with $-\kappa p_3 = \kappa\rho_{\mathrm{stab}}$). Of the two roots, $K_*$ (upper)
is the vacuum of UM-2: four-dimensional gravity is attractive there ($\mathcal{G}(K_*) = 13.8081$) and the stabiliser energy is
positive, $\kappa\rho_{\mathrm{stab}} = 54.566\,H^2$; the lower root $K_- = 2.4781$ has $\mathcal{G} = -0.4748$. The block scale $f_* = 0.215556$
fixes the proper size of the hidden direction, $f_*L = 3f_*/H = 8.926\times10^{-21}$ m on each half. Status: DERIVED (closed form;
the stabiliser itself ASSUMED).

## The radion and the response of the block to matter

@FE-44

**The terms.** Linearising FE-38 to FE-40 about the stabilised block (with $\rho_{\mathrm{stab}} \propto K^4$, from FE-41) gives a closed
linear system for the changes of the two rates and of $K$: $\Xi_{\mathcal{H}K}$ and $\Xi_{fK}$ are the restoring coefficients, and
$\Delta\dot K = -2K_*\Delta\mathcal{H}_f$ is the definition of $\mathcal{H}_f$. The block oscillates with the frequency $\omega_{\mathrm{r}}$: the radion,
the quantum of the block scale, with the mass $m_{\mathrm{r}} = \omega_{\mathrm{r}} = 3.38705\,H = 48.42$ TeV. The eigenvalues are 0 and
$\pm\mathrm{i}\omega_{\mathrm{r}}$: the block is stable, and it is stable for every block-isotropic stabiliser law $p_0 = p_5 = \nu\rho_{\mathrm{stab}}$
with $\nu = \frac14$ to 3 ($\omega_{\mathrm{r}} = 3.33$ to $4.10\,H$). The full nonlinear evolution gives $3.3868\,H$ (linear and nonlinear
frequencies agree to $7.9\times10^{-5}$). Status: DERIVED.

@FE-45

**The terms.** Matter on top of the stabiliser changes the sources by $\kappa\Delta\rho$, $\kappa\Delta p_3$ and $\kappa\Delta\bar p$ (the
block-averaged changes; the shape source $\Delta p_0 - \Delta p_5$ is outside the order-0 metric). Each enters both rates with the
coefficients of FE-46; $\mathcal{H}^2$ is of first order and is fixed by the constraint, $3\mathcal{G}(K_*)\mathcal{H}^2 = \kappa\Delta\rho$. The last
line is the radion equation with matter as its source. Status: DERIVED (exact to first order). The residual of the adiabatic
solution in the full nonlinear equations is $1.4\times10^{-7}$ for sources of $10^{-5}\,H^2$ and falls by the factor 10 with the sources
(it is of second order).

@FE-46

**The terms.** The exact coefficients (rational numbers and $\sqrt{51}$, from $K_* = 12 + \frac43\sqrt{51}$): numerically $\Xi_{\mathcal{H}K} =
0.272956\,H^2$, $\Xi_{fK} = 0.266522\,H^2$, $\Xi_{\mathcal{H}3} = -0.006853$, $\Xi_{\mathcal{H}p} = 0.038221$, $\Xi_{\mathcal{H}\rho} = -0.045997$,
$\Xi_{f3} = 0.028666$, $\Xi_{fp} = 0.037320$, $\Xi_{f\rho} = -0.009555$. Status: DERIVED (sympy).

For a source that changes slowly compared with $1/\omega_{\mathrm{r}}$ the radion follows it adiabatically, $\Delta\ddot K = 0$:

@@
\begin{aligned}
&\Delta K = -\frac{2K_*}{\omega_{\mathrm{r}}^2}\big(\Xi_{f3}\,\kappa\Delta p_3 + \Xi_{fp}\,\kappa\Delta\bar p +
 \Xi_{f\rho}\,\kappa\Delta\rho\big):\\
&c_3 = -\frac{2K_*\Xi_{f3}H^2}{\omega_{\mathrm{r}}^2},\qquad c_p = -\frac{2K_*\Xi_{fp}H^2}{\omega_{\mathrm{r}}^2},\qquad
 c_\rho = -\frac{2K_*\Xi_{f\rho}H^2}{\omega_{\mathrm{r}}^2}.
\end{aligned}
@@

The hidden-pressure coefficient can be read off the block equation directly: with $\Delta\rho = \Delta p_3 = 0$ (so $\mathcal{H} = 0$)
the block equation at $K_* + \Delta K$ with the stabiliser $\rho_{\mathrm{stab}} \propto K^4$ and the extra hidden pressure gives

@@
3H^2\Delta K - \kappa\,\frac{\mathrm{d}\rho_{\mathrm{stab}}}{\mathrm{d}K}\,\Delta K = \kappa\Delta\bar p,\qquad
\frac{\mathrm{d}\rho_{\mathrm{stab}}}{\mathrm{d}K} = \frac{4\rho_{\mathrm{stab}}}{K}\quad\Rightarrow\quad
c_p = \frac{H^2}{3H^2 - 4\kappa\rho_{\mathrm{stab}}/K_*} = -0.140028,
@@

with the stiffness $3H^2 - 4\kappa\rho_{\mathrm{stab}}/K_* = -7.1414\,H^2$.

@FE-47

**The terms.** The adiabatic response of the block: $c_\rho = 0.0358521$, $c_3 = -0.107556$, $c_p = -0.140028$. Because $c_3 = -3c_\rho$
exactly, the block responds only to the trace $\rho - 3p_3$ and to the hidden pressure $\bar p$: radiation (traceless, $\bar p = 0$)
drops out. A positive hidden pressure lowers $K$, i.e. enlarges the block. The last relation is the four-dimensional Friedmann
acceleration equation: with $\kappa\Delta\rho = 8\pi G_{\mathrm{N}}\mathcal{G}(K_*)\rho_4$ (FE-80) it is $\dot{\mathcal{H}} = -4\pi G_{\mathrm{N}}(\rho_4 +
p_4)$ of general relativity, and the constraint is $\mathcal{H}^2 = \frac{8\pi G_{\mathrm{N}}}{3}\rho_4$. Status: DERIVED (exact for a slowly
varying source; the neglected inertia is $(\mathcal{H}/m_{\mathrm{r}})^2 \approx 3\times10^{-33}$ at the freeze-out). The Kohn-Sham sources enter
through it with residual $1.4\times10^{-12}$ (the response recomputed from the stored cell averages); the block-shape source
$\lvert p_0 - p_5\rvert$ is up to 4 times $\bar p$ (OPEN, see "The block pressures").

## Four-dimensional gravity

On the static block the Lovelock densities split into a four-dimensional part and a part of the block. For a block of constant
curvature the internal densities are numbers:

@FE-48

**The terms.** $\mathcal{L}^{(4)}_{(p)}$ are the Lovelock densities of the four observable dimensions ($R^{(4)}$ the scalar curvature; the
four-dimensional Gauss-Bonnet density is topological, the cubic one vanishes), $\mathcal{L}^{(\mathrm{int})}_{(p)}$ those of the block.
The coefficient of $R^{(4)}$ is $1 + \alpha_{(2)}(-24H^2K) + \alpha_{(3)}72H^4K^2 = \mathcal{G}(K)$, and the constant terms combine into the
four-dimensional cosmological constant $\Lambda_4$, whose numerator is the constraint at $\mathcal{H} = 0$: $\Lambda_4 = 0$ exactly on the
stabilised block. The observed dark energy needs $\Lambda_4/H^2 \sim 10^{-92}$, a tuned residual (OPEN). Status: DERIVED. Residual
$6.9\times10^{-13}$ (the stored block in $\Lambda_4$ and in the stationarity of the constraint).

@FE-49

**The terms.** Four-dimensional gravity on the stabilised block is general relativity with Newton's constant
$8\pi G_{\mathrm{N}} = \kappa/(\mathcal{G}(K_*)V_\perp)$, where $V_\perp$ is the proper volume of the block (both halves of the period, the four
block scale factors $f^4$, the coordinate volume $v_{\mathrm{t}}$ of the extra times); $\kappa/V_\perp = 2.328\times10^{-36}$ GeV$^{-2}$ reproduces
$M_{\mathrm{Pl}} = 1.22091\times10^{19}$ GeV. The four-dimensional energy-momentum tensor is the eight-dimensional one integrated over the
block, and the four-dimensional gauge couplings are the eight-dimensional ones divided by the same volume (they run below
$m_{\mathrm{KK}}$ as in the Standard Model without a Higgs particle, FE-77, FE-83; at the scale $2M_{\mathrm{DM}} = 88.7$ TeV of the portal
I12, $g_3^2 = 0.7786$, $g_2^2 = 0.3781$, $g_1^2 = 0.1380$). Status: DERIVED. Its linear perturbations are FE-90.
