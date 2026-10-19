# Space, coordinates and the periodic hidden direction

## The coordinates (AUTHOR)

The author's coordinates are $X = \{x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7\}$ (in the author's notebook
`X = {x0[], x1[], ..., x7[]}`):

* $x_0$: the hidden space-like direction; the angle variable $z = 6Hx_0$ takes every real value;
* $x_1$, $x_2$, $x_3$: ordinary 3-space;
* $x_4$: the time;
* $x_5$, $x_6$, $x_7$: three extra time-like directions.

$H > 0$ is the author's constant (an inverse length; in UM-2 $H = 14.296$ TeV, fixed by the measured masses). Frame indices
$a = 0, \dots, 7$ are aligned with $x_0, \dots, x_7$, and the frame metric is

$$
\eta_{ab} = \mathrm{diag}(+1,\ +1,\ +1,\ +1,\ -1,\ -1,\ -1,\ -1)
$$
<!-- symbols: AUTO -->

in the order $x_0, x_1, \dots, x_7$: four space-like directions ($x_0$, $x_1$, $x_2$, $x_3$) and four time-like ones ($x_4$, $x_5$, $x_6$,
$x_7$).

## The hidden coordinate $y$, the fold and the tips (DERIVED)

The metric depends on $x_0$ only through $\lvert\sin z\rvert$ and $\cot^2z$. On every interval of $z$ on which $\sin z \ne 0$ the
hidden coordinate $y$ of the $y$ chart, the scaled coordinate $\xi$, the block scale $f$, the block variable $K$ and the two rates of
the background are defined by

@@FE-32@@

One period $0 < z < \pi$ of $x_0$ (length $\pi/(6H)$) consists of two halves, $0 < z < \pi/2$ and $\pi/2 < z < \pi$, joined at the
**fold** $z = \pi/2$, where $\cos z = 0$ and $y = 0$. Each half ends at a **tip** ($z \to 0^+$ or $z \to \pi^-$, where $y \to -\infty$),
at infinite proper distance from the fold. As in the Kohn-Sham record of this repository the tip is replaced by a regular cutoff at
$y = -L$ (RECORD), with

$$
\lvert\sin z\rvert = \mathrm{e}^{6Hy},\qquad -L \le y \le 0,\qquad HL = 3
$$
<!-- symbols: AUTO -->

so that $\xi = y/L$ runs from $-1$ (the tip) to $0$ (the fold) on each half. The **fold reflection** $z \mapsto \pi - z$ (that is,
$x_0 \mapsto \pi/(6H) - x_0$) maps the two halves onto each other; the modes of a field on one period are even or odd under it.
Because $y$ is a function of $\lvert\sin z\rvert$,

$$
y(z + \pi) = y(z),\qquad y(\pi - z) = y(z),\qquad z = 6Hx_0 :
$$
<!-- symbols: AUTO -->

every function of $y(z)$ is periodic in $x_0$ with the period $\pi/(6H)$, which is the author's requirement on every wave function
of the model. The proper length of one half, $fL$, is $8.926\times10^{-21}$ m on the stabilised block, and one coordinate period
of $x_0$ is $\pi/(6H) = 7.227\times10^{-21}$ m (DERIVED).

# The metric as a power series of terms of decreasing magnitude

The author asks for a metric general enough to model the CMB, the CNB and the BAO, perhaps expressible as a power series of
terms of decreasing magnitude. UM-2 writes the metric as such a series (DERIVED for the sizes of the terms):

@@FE-87@@

The bookkeeping parameter $\epsilon \sim 10^{-5}$ is the size of the CMB temperature anisotropy (STANDARD); the first-order term is
expanded in the $x_0$ profiles $F_n$ of the hidden direction (the flat profile $F_0 = 1$ and the Kaluza-Klein profiles $F_n$,
$n \ge 1$, below).

## Order 0: the corrected primordial metric (AUTHOR coordinates, DERIVED properties)

In the author's chart, with two general functions $a_4(x_4)$ and $b_4(x_4) > 0$ of the time, the order-0 metric is

@@FE-31@@

where $(\sin^2z)^{1/6}$ is the positive branch. This is the metric of the Revision record of 2026-10-16 (version 2), whose sources
are all diagonal. The notebook metric

$$
\begin{aligned}
g_{\mathrm{nb}} = \mathrm{diag}\big(&\cot^2z,\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\\
 &-1,\ -\mathrm{e}^{-2a_4}(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}(\sin^2z)^{1/6}\big),
\end{aligned}
$$
<!-- symbols: AUTO -->

to whose extra-time components the author's order of 2026-10-14 added the factor $b_4$, differs from $\bar g_{MN}$ in the hidden
component and in the warp of 3-space. In the $y$ chart (written out again with its definitions):

@@FE-32@@

The block $\{x_0, x_5, x_6, x_7\}$ is $f^2$ times a four-dimensional space of constant curvature $-H^2$ and signature $(1, 3)$; $f$ is
its common scale factor ("the block"), $\mathcal{H}$ is the observer's Hubble rate, and $\mathcal{H}_f < 0$ means that the extra times
and $x_0$ deflate. The vielbein of the order-0 metric is

$$
\mathbf{e}^{0}{}_{x_0} = f\cot z,\qquad \mathbf{e}^{1}{}_{x_1} = \mathbf{e}^{2}{}_{x_2} = \mathbf{e}^{3}{}_{x_3} = \mathrm{e}^{a_4},\qquad
\mathbf{e}^{4}{}_{x_4} = 1,\qquad \mathbf{e}^{5}{}_{x_5} = \mathbf{e}^{6}{}_{x_6} = \mathbf{e}^{7}{}_{x_7} = f\,(\sin^2z)^{1/12}
$$
<!-- symbols: AUTO -->

(all other components zero). **Curvature (DERIVED; sympy, identical in both charts, 25 checks).** The Riemann tensor is
pair-diagonal, $R^{ab}{}_{cd} = 0$ unless $\{a, b\} = \{c, d\}$, and every sectional curvature is one of

@@FE-33@@

None depends on $x_0$; the curvature is the same on both halves of every period.

## Order 1: the observable perturbations and the hidden tower

The $n = 0$ term of the first-order metric has the flat profile $F_0 = 1$; in the Newtonian gauge its line element is

@@FE-88@@

with the lapse potential $\Phi$, the curvature potential $\Psi_{\mathrm{N}}$ (the factor $\epsilon$ is absorbed into them), the
transverse-traceless tensor $h^{\mathrm{TT}}$ and the radion $\sigma_{\mathrm{r}}$ (the relative fluctuation of the block size). The
scalar and tensor sectors carry the CMB, the CNB and the BAO; the radion is massive (48.42 TeV, the section on gravity) and does not
propagate at cosmological distances. The terms $n \ge 1$ are Kaluza-Klein modes with masses above the gap $3H/(2f_*) = 99.5$ TeV.
Order 2 contains the products of first-order terms and the back-reaction of $x_0$-localised sources; its magnitude is estimated
below, its detailed form is not computed (OPEN).

## The magnitudes of the terms (DERIVED; the order-2 sizes are ESTIMATES and the tensor bound is STANDARD)

The solution of the coupled equations fixes the size of every term (4 checks):

**Order 0**, $\bar g_{MN}$: magnitude 1.

**Order 1, $n = 0$** (the Newtonian potentials). On cosmological scales the size is the root-mean-square Weyl potential per
logarithmic interval of the comoving wavenumber $k$ today, from the linear solution (the section on cosmology):

@@FE-98@@

$\Phi_{\mathrm{rms}}$ is $2.42\times10^{-5}$, $2.28\times10^{-5}$, $1.51\times10^{-5}$, $4.12\times10^{-6}$, $1.74\times10^{-6}$,
$3.55\times10^{-7}$ and $5.03\times10^{-8}$ at $k = 10^{-4}$, $10^{-3}$, $10^{-2}$, $0.05$, $0.1$, $0.3$ and $1$ Mpc$^{-1}$. It agrees with the
Poisson form ($\Omega_{\mathrm{m}} = 0.3150$, $\mathcal{H}_0 = 67.38$ km/s/Mpc) applied to the linear matter density to $1.5\times10^{-6}$ for
$k \ge 10^{-2}$ Mpc$^{-1}$, and on the largest scales with the matter-era form ($\mathcal{R}$ from $A_{\mathrm{s}}$ and $n_{\mathrm{s}}$,
$k_0 = 0.05$ Mpc$^{-1}$) to $4.4\times10^{-5}$, where $D_+\mathrm{e}^{-a_4} = 0.7878$ today is the growth suppression by $\Lambda_4$.
Bound objects of mass $M_1$ and radius $r$ have the surface potential

$$
\Phi = \frac{G_{\mathrm{N}}M_1}{r} :
$$
<!-- symbols: AUTO -->

the Earth $7.0\times10^{-10}$, the Sun $2.1\times10^{-6}$, a white dwarf ($0.6$ solar masses, 8700 km) $1.0\times10^{-4}$, a neutron
star ($1.4$ solar masses, 12 km) $0.17$; in galaxies and clusters $\Phi$ is of the order of the squared velocity dispersion (in units
of the speed of light): $5.4\times10^{-7}$ (220 km/s) and $1.1\times10^{-5}$ (1000 km/s). The series converges quickly everywhere except near neutron stars
and black holes, where the full nonlinear equations apply.

**Order 1, $n \ge 1$** (the Kaluza-Klein gravitons). The graviton has no tip term ($\beta = 0$), so its even levels are

@@FE-53@@

with $\tilde m_n^2 = 30.1196$, $59.7284$, $109.0764$ for $n = 1, 2, 3$ (finite elements agree to $3.9\times10^{-9}$). Two static
masses $M_1$ and $M_2$ with the normalised $x_0$ profiles $\varrho_1$ and $\varrho_2$ attract at the distance $r$ with

@@FE-54@@

For two masses with the same profile the strength is $(N_0/N_n)(\int\varrho_1F_n\,\mathrm{d}\xi)^2$: $\mathcal{A}_n = 0.0728$, $0.1469$,
$0.1809$ for two sources at the fold, $0.0904$, $0.0136$, $0.0057$ for the quark-doublet zero-mode profile and $0.0208$, $0.0197$,
$0.0105$ for the lepton doublet; a source with the flat profile of the gauge zero modes (the gluon field energy, which makes up
most of the nucleon mass) excites none ($\int\mathrm{e}^{3HL\xi}F_n\,\mathrm{d}\xi = 0$, the orthogonality of $F_n$ to the flat profile,
verified to $2\times10^{-10}$). The first level is the Kaluza-Klein scale, $m^{\mathrm{KK}}_1 = m_{\mathrm{KK}} = 121.32$ TeV; its range
$1/m_{\mathrm{KK}} = 1.63\times10^{-21}$ m makes the Yukawa factor $\mathrm{e}^{-3.1\times10^{16}}$ at $50$ micrometres: Newton's law is exact
at every measurable distance.

**The radion** $\sigma_{\mathrm{r}}$: its static response to matter is at most $\Delta\ln f = 1.1\times10^{-34}$ (at the dark-matter
freeze-out, from the hidden pressure of the hot plasma; $10^{-62}$ for the Earth; the section on the coupled solution); its range is
$4.08\times10^{-21}$ m; the primordial oscillation decays (lifetime $0.43\,\text{s}/C_{\mathrm{r}}$, the last section).

**Order 2** (ESTIMATE: the squares of the first-order terms):

$$
\epsilon^2h^{(2)} \sim \Phi_{\mathrm{rms}}^2 = 5.8\times10^{-10}\quad \big(k = 10^{-4}\ \text{Mpc}^{-1}\big)
$$
<!-- symbols: AUTO -->

on the largest cosmological scales (the ratio of order 2 to order 1 is $2.4\times10^{-5}$, far below the $10^{-3}$ accuracy at which the
first-order cosmology is used; DERIVED in the residual analysis), $4.5\times10^{-12}$ at the Sun, $0.03$ at a neutron star.

**Tensor modes** $h^{\mathrm{TT}}$: their primordial amplitude is not predicted (the primordial spectrum is an input of UM-2); the
bound on the tensor-to-scalar ratio (STANDARD, from memory) gives

$$
h^{\mathrm{TT}}_{\mathrm{rms}} < \big(r_{\mathrm{ts}}A_{\mathrm{s}}\big)^{1/2} = 8.7\times10^{-6},\qquad r_{\mathrm{ts}} < 0.036 .
$$
<!-- symbols: AUTO -->

On cosmological scales the terms therefore decrease as $1$, $2.4\times10^{-5}$ (order 1), $5.8\times10^{-10}$ (order 2), $10^{-34}$ (radion)
and $0$ (Kaluza-Klein gravitons at any measurable distance): the $n = 0$ term of order 1 carries the CMB, the CNB and the BAO.

