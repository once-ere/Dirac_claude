# The $x_0$ mass mechanism

The author's requirement (order of 2026-10-18): "Mass will be given to all non-massless particles (except the massless particles:
graviton, photon and perhaps the quanta of the dirac16complex field), by appropriate wave function dependence on the space coordinate
x0 (either explicit, derived, or assumed), which must be periodic in x0 with period pi/(6H)." This section presents the mechanism
in three steps: the author's uncertainty argument, written as equations; the exact $x_0$ eigenvalue equations of UM-2, which give every
mass, the mixing matrices and the massless zero modes; and precisely what the uncertainty relation does and does not bound.

## The author's argument: localisation in $x_0$ and the uncertainty relation (AUTHOR)

**Step 1: every wave function is periodic in $x_0$.** Every field of UM-2 depends on $x_0$ through $z = 6Hx_0$ and $y(z)$ (the section on
space and coordinates): the profile $F$ of a boson and the block spinor $\chi$ of a fermion are functions of $y$, so

$$
F\big(y(6Hx_0 + \pi)\big) = F\big(y(6Hx_0)\big),\qquad \chi\big(y(6Hx_0 + \pi)\big) = \chi\big(y(6Hx_0)\big) :
$$
<!-- symbols: AUTO -->

every wave function is periodic in $x_0$ with the period $\pi/(6H)$.

**Step 2: localisation and the uncertainty relation.** A wave function localised in $x_0$ (well inside one period) with the spread
$\Delta x_0$ has a spread $\Delta k_{x_0}$ of the momentum along $x_0$ (the author's $(p)_{x_0}$; in UM-2 the letter $p$ is a pressure and
$k$ a momentum) that obeys the Heisenberg uncertainty relation

$$
\Delta x_0\,\Delta k_{x_0} \ge \frac{\hbar}{2},\qquad \big(\Delta x_0\big)^2 = \langle x_0^2\rangle - \langle x_0\rangle^2,\qquad
\big(\Delta k_{x_0}\big)^2 = \langle k_{x_0}^2\rangle - \langle k_{x_0}\rangle^2,\qquad k_{x_0} = -\mathrm{i}\hbar\,\frac{\partial}{\partial x_0}
$$
<!-- symbols: AUTO -->

($\langle\cdots\rangle$ the expectation value in the wave function; here $\Delta$ is the spread, the root-mean-square deviation).

**Step 3: momentum is proportional to mass.** The momentum along the hidden direction is invisible to a four-dimensional observer; its
energy is rest energy. For a mode of bulk mass $M$ (the mass function of the field; zero for the gauge fields and the graviton) in a
flat hidden direction the dispersion relation of eight dimensions, seen at rest in four dimensions ($\vec k = 0$), gives the effective
mass

$$
E^2 = \lvert\vec k\rvert^2 + k_{x_0}^2 + M^2\qquad\Rightarrow\qquad m_{\mathrm{eff}}^2 = \langle k_{x_0}^2\rangle + M^2 :
$$
<!-- symbols: AUTO -->

without a bulk mass the hidden momentum is the mass.

**Step 4: the kinetic energy is proportional to the momentum squared over the mass.** For a hidden momentum small against the bulk
mass the hidden kinetic energy adds to the rest energy:

$$
m_{\mathrm{eff}} \simeq M + E_{\mathrm{kin}},\qquad E_{\mathrm{kin}} = \frac{\langle k_{x_0}^2\rangle}{2M}\qquad \big(\langle k_{x_0}^2\rangle \ll M^2\big).
$$
<!-- symbols: AUTO -->

**Step 5: the bound.** Since $\langle k_{x_0}^2\rangle \ge (\Delta k_{x_0})^2$, a localised wave function receives an effective mass

$$
\langle k_{x_0}^2\rangle \ge \big(\Delta k_{x_0}\big)^2 \ge \frac{\hbar^2}{4\big(\Delta x_0\big)^2}\qquad\Rightarrow\qquad
m_{\mathrm{eff}} \ge \frac{\hbar}{2\,\Delta x_0}\qquad (M = 0).
$$
<!-- symbols: AUTO -->

Only the proper hidden length $fy$ is free of the choice of chart (below), so the author's estimate of a mass is written with the
root-mean-square proper distance $\Delta(fy)$ of the state from the fold, computed with the probability density $\varrho_\xi$ of its
$x_0$ profile (in the flat measure; symmetric about the fold over the full period):

$$
m_{\mathrm{Heis}} = \frac{\hbar}{2\,\Delta(fy)},\qquad \Delta(fy) = fL\,\Delta\xi,\qquad \big(\Delta\xi\big)^2 = \int_{-1}^{0}\xi^2\varrho_\xi\,\mathrm{d}\xi .
$$
<!-- symbols: AUTO -->

**Step 6: the exceptions.** A wave function whose $x_0$ dependence costs no energy is massless even when it is localised: the
graviton and the photon (and the gluons, whose colour symmetry is never broken), whose flat profile is an exact eigenfunction with the
eigenvalue zero, protected by four-dimensional general covariance and gauge invariance; and the fold bands of dirac16complex, chiral zero
modes that are massless for every mass profile. This is the author's list of exceptions ("graviton, photon and perhaps the quanta of the
dirac16complex field"), made precise by the exact equations: the gluons belong to it, and of the quanta of dirac16complex the fold bands
are massless while the bulk band (the dark matter) is massive. For these massless states the estimate $m_{\mathrm{Heis}}$ is NOT the mass
(70.6 TeV for the photon): the argument is a heuristic, and the exact $x_0$ equations below decide.

**Proper versus coordinate localisation (DERIVED).** The photon zero mode, localised at the fold in proper length, has 61.9 % of its
probability within $\pi/8$ of the tips in the coordinate $z = 6Hx_0$: localisation in the coordinate $x_0$ depends on the chart, because the
proper hidden length $f\lvert\cot z\rvert\,\mathrm{d}x_0$ vanishes at the fold and diverges at the tips. A profile confined to a small proper
distance from the fold ($\Delta\xi = 0.157$) extends over almost the whole coordinate range of $z$. Only the proper hidden length enters the
masses; "$\Delta x_0$ small" must therefore be read as "$\Delta(fy)$ small".

## The exact $x_0$ eigenvalue equations and what they give

Throughout this section the block is static ($f = f_*$), $\xi = y/L \in [-1, 0]$ on each half of a period, and the eigenvalues are
dimensionless in units of the proper half cell: $\tilde m = m\,fL$ for bosons and $\tilde\varepsilon = \varepsilon\,fL$ for fermions.

### Gauge fields and the graviton (DERIVED)

A four-dimensional component of a gauge field with the profile $F$ (gauge $A_y = 0$) has a reduced action per half whose stationary
points are the eigenfunctions of the $x_0$ operator; the transverse-traceless graviton obeys the same operator in Einstein gravity:

@@FE-50@@

with the fold and tip conditions (the tip condition is the natural boundary condition of the tip mass term of IN-15)

@@FE-51@@

With the rescaled profile the solutions are elementary and the eigenvalue conditions are

@@FE-52@@

($\varpi = \mathrm{i}\lvert\varpi\rvert$ below the gap $9H^2L^2/4$).

**Massless particles.** For $\beta = 0$ the flat profile $F = $ const is an exact eigenfunction with $\tilde m = 0$: the **graviton, the photon
and the gluons are exactly massless**; their masslessness is protected by four-dimensional general covariance and gauge invariance. The
excited levels are $\tilde m_n^2 = 9H^2L^2/4 + n^2\pi^2$ (even, $n \ge 1$) and the roots of $\varpi\cot\varpi = -3HL/2$ (odd); for $HL = 3$:
$\tilde m_1^2 = 30.1196$, the first odd level $27.0890$, the gap $20.25$ (DERIVED, finite elements agree to $5\times10^{-10}$). The Kaluza-Klein
scale is $m_{\mathrm{KK}} = \tilde m_1/(fL)$.

**$W^\pm$ and $Z$.** The tip term gives $\beta_{\mathrm{W}}$ for $W^+$ and $W^-$ (one value for both) and, by custodial symmetry,
$\beta_{\mathrm{Z}} = \beta_{\mathrm{W}}/\cos^2\theta_{\mathrm{W}}$, with $\theta_{\mathrm{W}}$ the angle of the gauge couplings. At small $\beta$

$$
\tilde m^2 \simeq \beta\,\frac{3HL\,\mathrm{e}^{-3HL}}{1 - \mathrm{e}^{-3HL}}\qquad (\beta \ll 1),
$$
<!-- symbols: AUTO -->

and $m_{\mathrm{Z}}/m_{\mathrm{W}} = 1/\cos\theta_{\mathrm{W}}$. Beyond leading order the bending of the profiles moves the mass ratio
$m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2 = \tilde m_{\mathrm{W}}^2/\tilde m_{\mathrm{Z}}^2$ away from $\cos^2\theta_{\mathrm{W}}$: the electroweak parameter exceeds 1.
This tree-level custodial violation is what the measured $\rho_{\mathrm{EW},0} - 1 = 0.00038$ constrains, and the fit is (written out again)

@@FE-55@@

With the measured masses (STANDARD: $m_{\mathrm{W}} = 80.3625$ GeV, $m_{\mathrm{Z}} = 91.1879$ GeV, PDG 2026) the angle of the couplings is
$\cos^2\theta_{\mathrm{W}} = 0.776368$ (the on-shell value $m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2$ is $0.776663$), and the fit gives (DERIVED)
$\beta_{\mathrm{W}} = 0.011912$, $\tilde m_{\mathrm{W}}^2 = 1.32149\times10^{-5}$, $m_{\mathrm{KK}} = 121.32$ TeV, with both masses reproduced
($m_{\mathrm{Z}} = 91.1879$ GeV). A positive tip term cannot make the $W$ heavier than the Dirichlet limit ($F(-1) = 0$, $\tilde m^2 = 0.010016$),
i.e. $m_{\mathrm{W}} \le 0.01824\,m_{\mathrm{KK}}$. The angle of the couplings of this fit, $\sin^2\theta_{\mathrm{W}} = 0.223632$, differs from the
$\overline{\mathrm{MS}}$ value $0.23122$ used in the couplings to the fermions (the residual analysis: two values of one angle, of the size of
the electroweak loop corrections that UM-2 does not compute; they change the total tree-level $Z$ width by 0.82 %, 0.83 % with the QCD factor).

### Fermions (DERIVED)

The eight-dimensional Dirac equation with the canonical spin connection reduces EXACTLY (all eight blocks, general $a_4(x_4)$, $b_4(x_4)$,
$y$-dependent mass function $M(y)$ and potential $v(y)$; DERIVED with the author's matrices) to the block Hamiltonian:

@@FE-56@@

The factor $\mathrm{e}^{-\frac32Hy}$ removes the $\tfrac32(H/f)\gamma^{x_0}$ of the spin connection, and $\mathrm{e}^{a_4/2}b_4^{-1}$ removes its $\gamma^{x_4}$
part. For a constant bulk mass and $k = 0$ the general solution of $h\chi = 0$ is a combination of $(\mathrm{e}^{f\mu y}, 0)$ and
$(0, \mathrm{e}^{-f\mu y})$; the boundary conditions of the Standard-Model fermions (written out again)

@@FE-29@@

select one component, and the zero modes are

@@FE-57@@

the doublet zero mode is localised at the fold for $c_L > 0$ and the singlet zero mode for $c_R < 0$; at $k \ne 0$ the zero modes are massless
four-dimensional particles with the energy $\mathrm{e}^{-a_4}\lvert k\rvert$ (the physical momentum).

**Masses from the tip: one generation.** The tip Yukawa coupling turns the tip conditions into the self-adjoint mixing conditions
(written out again)

@@FE-30@@

with $\mathcal{K}$ the dimensionless tip mixing. At $k = 0$ the doublet ($c_L > 0$) and singlet ($c_R < 0$)
solutions that satisfy the fold conditions reach the tip with

@@FE-58@@

so the four-dimensional mass is the lowest root of the exact $x_0$ eigenvalue equation (DERIVED; direct shooting of the coupled
system agrees to $6\times10^{-10}$), whose first-order solution is the tip mixing times the tip amplitudes of the two chiral wave functions:

@@FE-59@@

(both zero modes are localised at the fold, so their tip amplitudes are exponentially small).

**Masses and mixing from the tip: three generations.** In each sector (neutrinos, charged leptons, up-type quarks, down-type quarks) the
tip coupling is a $3\times3$ matrix $\mathcal{K}$ (the dimensionless form of $\mathcal{Y}_\nu$, $\mathcal{Y}_e$, $\mathcal{Y}_u$, $\mathcal{Y}_d$), and the
conditions hold for the vectors of boundary values over the generations; they are self-adjoint for every complex $\mathcal{K}$ (DERIVED).
With the doublet amplitudes $\boldsymbol{\alpha}$ and the singlet amplitudes $\boldsymbol{\beta}$ of the solutions above,

@@FE-60@@

the masses are the roots of the determinant, and $\boldsymbol{\alpha}$ is the left-handed flavour content of each mass state. If the three
doublets of a sector share one bulk mass and $\mathcal{K}$ is unitary, the determinant factorises: each factor is the one-generation condition
with $\mathcal{K} = 1$, so the masses are the one-generation roots, the left-handed rotation of the sector is its tip matrix (so that the mixing
matrices are $U = \mathcal{K}_e^\dagger\mathcal{K}_\nu$ and $V_{\mathrm{CKM}} = \mathcal{K}_u^\dagger\mathcal{K}_d$), and the right-handed rotations are
trivial (DERIVED with mpmath at 50 digits: the roots of the $3\times3$ determinant equal the one-generation roots, both refined in the same
computation, to $3.0\times10^{-42}$ in all four sectors; the masses stored by the mass computation agree with them to $4.5\times10^{-11}$; the
null vectors equal the columns of $\mathcal{K}$ to $1.1\times10^{-16}$; for a random complex non-unitary $\mathcal{K}$ the exact roots agree with the
singular values of $\mathcal{Z}(c_L)\,\mathcal{K}\,\mathrm{diag}(\mathcal{Z}(-c_{R}))$ to $3.5\times10^{-5}$).

**The UM-2 choice (ASSUMED).** One doublet bulk mass per sector, common to the three generations ($c_L = f\mu_\ell L$ for the leptons,
$c_L = f\mu_QL$ for the quarks), fixed by the heaviest fermion of the sector with $c_R = -c_L$ (the tau and the top quark); unitary tip
matrices $\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}$, $\mathcal{K}_\nu = U$, $\mathcal{K}_d = V_{\mathrm{CKM}}$ (FE-30) in the basis in which the singlet bulk masses
are diagonal. The targets are the measured masses (STANDARD, the PDG 2025 values: electron, muon, tau; up, down and strange quark in
$\overline{\mathrm{MS}}$ at 2 GeV, charm and bottom at their own scale, the directly measured top mass, used as tree-level targets) and the
neutrino masses (ASSUMED lightest mass and normal ordering, measured splittings; written out again)

@@FE-100@@

They require (DERIVED; exact roots; the first-order formula agrees to $1.1\times10^{-3}$ for the top quark and better than
$3\times10^{-4}$ for every other fermion)

| fermion | mass | doublet $c_L$ | singlet $c_R$ | $\mu_{\psi i}/H$ (singlet) | singlet width $fL/(2\lvert c_R\rvert)$ | $\tilde\varepsilon = m\,fL$ |
| -- | --- | --- | --- | --- | --- | --- |
| $\nu_1$ | $1.000$ meV | $5.9529$ | $-35.0452$ | $-54.194$ | $1.27\times10^{-22}$ m | $4.524\times10^{-17}$ |
| $\nu_2$ | $8.712$ meV | $5.9529$ | $-32.8481$ | $-50.796$ | $1.36\times10^{-22}$ m | $3.941\times10^{-16}$ |
| $\nu_3$ | $50.140$ meV | $5.9529$ | $-31.0702$ | $-48.047$ | $1.44\times10^{-22}$ m | $2.268\times10^{-15}$ |
| electron | $0.51100$ MeV | $5.9529$ | $-14.5539$ | $-22.506$ | $3.07\times10^{-22}$ m | $2.312\times10^{-8}$ |
| muon | $105.658$ MeV | $5.9529$ | $-8.9809$ | $-13.888$ | $4.97\times10^{-22}$ m | $4.779\times10^{-6}$ |
| tau | $1776.93$ MeV | $5.9529$ | $-5.9529$ | $-9.205$ | $7.50\times10^{-22}$ m | $8.038\times10^{-5}$ |
| up | $2.16$ MeV | $3.3823$ | $-15.4300$ | $-23.861$ | $2.89\times10^{-22}$ m | $9.771\times10^{-8}$ |
| charm | $1.2730$ GeV | $3.3823$ | $-8.7683$ | $-13.559$ | $5.09\times10^{-22}$ m | $5.758\times10^{-5}$ |
| top | $172.56$ GeV | $3.3823$ | $-3.3823$ | $-5.230$ | $1.32\times10^{-21}$ m | $7.806\times10^{-3}$ |
| down | $4.70$ MeV | $3.3823$ | $-14.6258$ | $-22.617$ | $3.05\times10^{-22}$ m | $2.126\times10^{-7}$ |
| strange | $93.5$ MeV | $3.3823$ | $-11.5158$ | $-17.808$ | $3.88\times10^{-22}$ m | $4.230\times10^{-6}$ |
| bottom | $4.183$ GeV | $3.3823$ | $-7.5005$ | $-11.599$ | $5.95\times10^{-22}$ m | $1.892\times10^{-4}$ |

The doublet bulk masses are $\mu_\ell = 9.2055\,H$ (width $7.50\times10^{-22}$ m) and $\mu_Q = 5.2304\,H$ (width $1.32\times10^{-21}$ m). Order-one
bulk masses give the whole hierarchy, because the tip amplitudes depend exponentially on $c$; within a sector the lighter fermion has the
sharper singlet localisation. The neutrinos are Dirac fermions; their right-handed partners $\nu_{Ri}$ are gauge singlets that are never
thermalised. (Version 1 gave every fermion its own $c_L = -c_R$; with three generations that rule would give the members of one doublet
different bulk masses, against the single bulk mass of a multiplet, and flavour-changing Kaluza-Klein couplings.)

**Mixing matrices (STANDARD parametrisation, measured values).** Both tip matrices are written in the standard form

@@FE-61@@

with, for the PMNS matrix (NuFIT 6.0, normal ordering), $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{23} = 0.470$, $\sin^2\theta_{13} = 0.02215$,
$\delta_{\mathrm{CP}} = 212^\circ$ ($\theta_{12} = 33.71^\circ$, $\theta_{23} = 43.28^\circ$, $\theta_{13} = 8.56^\circ$; $J_{\mathrm{CP}} = -0.01777$), and for the
CKM matrix (PDG global fit) $s_{12} = 0.22501$, $s_{13} = 0.003732$, $s_{23} = 0.04183$, $\delta_{\mathrm{CP}} = 1.147$ ($J_{\mathrm{CP}} = 3.117\times10^{-5}$).
Both are unitary to $1.1\times10^{-16}$ (DERIVED). The magnitudes are

$$
\lvert U\rvert = \begin{pmatrix} 0.8226 & 0.5488 & 0.1488\\ 0.3351 & 0.6543 & 0.6779\\ 0.4594 & 0.5203 & 0.7199\end{pmatrix},\qquad
\lvert V_{\mathrm{CKM}}\rvert = \begin{pmatrix} 0.97435 & 0.22501 & 0.00373\\ 0.22488 & 0.97349 & 0.04183\\ 0.00858 & 0.04111 & 0.99912\end{pmatrix}.
$$
<!-- symbols: AUTO -->

**No flavour-changing neutral currents at tree level (DERIVED).** Because the doublets of a sector share one bulk mass and the right-handed
rotations are trivial, the couplings of the Kaluza-Klein gauge modes are flavour diagonal in the mass basis to $10^{-17}$ (the section on the
interactions).

### The quanta of dirac16complex (DERIVED)

$\Psi$ has the same block Hamiltonian with $M = m_\Psi$ and the boundary conditions written out again:

@@FE-28@@

both parities being modes of the full period. With $c_\Psi = f\,m_\Psi L$ the exact $k = 0$ spectrum is

@@FE-62@@

The **fold band** $\varepsilon = \mathrm{e}^{-a_4}\lvert k\rvert$ is massless: 8 states per 3-momentum, 4 in $\Psi_A$ (two Weyl species with
$\Gamma_4 = +1$) and 4 in $\Psi_B$ (two Weyl species with $\Gamma_4 = -1$). The **bulk band** is massive; at the stabilised block
($f_* = 0.215556$, $c_\Psi = 0.646667$) its lowest level is the odd level $\varepsilon_{\mathrm{DM}} = 3.102204\,m_\Psi$ ($\varpi = 1.89901$, a hidden wave
number $\varpi/(fL) = 2.93661\,m_\Psi$), and the lowest even bulk level is $4.959981\,m_\Psi$. The odd level is the dark-matter candidate (the
section on the dark sector).

## What the uncertainty relation does and does not bound (DERIVED)

For a boson the eigenvalue problem is (written out again)

@@FE-50@@

@@FE-51@@

and the rescaled profile $\tilde F = \mathrm{e}^{3HL\xi/2}F$ obeys the exact identity

$$
\mathrm{e}^{3HL\xi}\Big(\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)^2 = \Big(\frac{\mathrm{d}\tilde F}{\mathrm{d}\xi}\Big)^2 + \frac{9H^2L^2}{4}\,\tilde F^2
 - \frac{3HL}{2}\,\frac{\mathrm{d}\big(\tilde F^2\big)}{\mathrm{d}\xi},
$$
<!-- symbols: AUTO -->

which turns the Rayleigh quotient of FE-50 with the conditions FE-51 into the decomposition of every bosonic eigenvalue into a hidden kinetic energy, a warp
term, a fold term and a tip term:

$$
\tilde m^2 = \langle k_\xi^2\rangle + \frac{9H^2L^2}{4} - \frac{3HL}{2}\,\varrho_\xi(0) + \Big(\frac{3HL}{2} + \beta\Big)\varrho_\xi(-1),\qquad
\langle k_\xi^2\rangle = \frac{\int_{-1}^{0}\big(\mathrm{d}\tilde F/\mathrm{d}\xi\big)^2\mathrm{d}\xi}{\int_{-1}^{0}\tilde F^2\mathrm{d}\xi},\qquad
\varrho_\xi = \frac{\tilde F^2}{\int_{-1}^{0}\tilde F^2\mathrm{d}\xi} .
$$
<!-- symbols: AUTO -->

For a fermion the eigenvalue problem is the block Hamiltonian (written out again)

@@FE-56@@

and for a fermion of localisation $c$ the same reasoning with $h$ at $k = 0$ gives

$$
\tilde\varepsilon^2 = \langle k_\xi^2\rangle + c^2 - c\,\frac{\big[\chi^\dagger\sigma_3\chi\big]_{-1}^{0}}{\int_{-1}^{0}\chi^\dagger\chi\,\mathrm{d}\xi},\qquad
\langle k_\xi^2\rangle = \frac{\int_{-1}^{0}\big(\mathrm{d}\chi/\mathrm{d}\xi\big)^\dagger\big(\mathrm{d}\chi/\mathrm{d}\xi\big)\,\mathrm{d}\xi}{\int_{-1}^{0}\chi^\dagger\chi\,\mathrm{d}\xi},\qquad
\varrho_\xi = \frac{\chi^\dagger\chi}{\int_{-1}^{0}\chi^\dagger\chi\,\mathrm{d}\xi} .
$$
<!-- symbols: AUTO -->

The uncertainty relation bounds only the hidden kinetic energy $\langle k_\xi^2\rangle$. On the cell, which ends at the tips, it reads

$$
\sqrt{\langle k_\xi^2\rangle}\;\Delta\xi \ge \frac{1 - \varrho_\xi(-1)}{2},\qquad \big(\Delta\xi\big)^2 = \int_{-1}^{0}\xi^2\varrho_\xi\,\mathrm{d}\xi,
$$
<!-- symbols: AUTO -->

since $1 = \int\varrho_\xi\,\mathrm{d}\xi = \varrho_\xi(-1) - \int\xi\,(\mathrm{d}\varrho_\xi/\mathrm{d}\xi)\,\mathrm{d}\xi$ (integration by parts; the fold end
$\xi = 0$ contributes nothing) and the Cauchy-Schwarz inequality bounds $\lvert\int\xi\,(\mathrm{d}\varrho_\xi/\mathrm{d}\xi)\,\mathrm{d}\xi\rvert$ by
$2\Delta\xi\sqrt{\langle k_\xi^2\rangle}$; $\Delta(fy) = fL\,\Delta\xi$ is the root-mean-square proper distance from the fold. The familiar
$\langle k_\xi^2\rangle \ge 1/(4\Delta\xi^2)$ is guaranteed only for profiles negligible at the tip (it can hold otherwise: the first even
Kaluza-Klein mode, with $\varrho_\xi(-1) = 0.655$, has $\langle k_\xi^2\rangle\Delta\xi^2 = 4.59$); the photon zero mode has $0.497$, the broad fold zero
mode of $\Psi$ ($\varrho_\xi(-1) = 0.489$) only $0.097$. The relation with the tip term is a theorem; it is also checked numerically for each of
the 21 computed states (the zero mode of the photon, gluons and graviton, $W^\pm$, $Z$, the first even and odd Kaluza-Klein modes, the two
doublet zero modes, the twelve singlet zero modes of the fermions, the fold zero mode of $\Psi$ and the dark matter; DERIVED). Three
classes follow:

* **massless**: profiles flat relative to the geometry ($F = $ const or $h\chi = 0$): the fold term cancels the hidden kinetic energy and the
  warp exactly; the graviton, the photon, the gluons and the fold bands of $\Psi$. They are localised at the fold
  ($\Delta(fy) = 1.40\times10^{-21}$ m for the photon) and yet massless;
* **heavy**: the $x_0$ dependence fills the cell. For the gauge fields and the graviton every odd mode and every excitation has
  $m \ge 3H/(2f_*) = 99.5$ TeV (the gap theorem of the boson operator: one even level below the gap for every $\beta \ge 0$, no odd level); the
  excitations of $\Psi$ start at its lowest odd level, $3.10\,m_\Psi = 44.35$ TeV (the dark matter), since the Dirac operator has no warp gap.
  For the computed states of this class the author's estimate $m_{\mathrm{Heis}}$ lies below the mass (by factors 2.3 to 7.5, the dark matter
  included): the uncertainty argument is the reason of these masses (observed for these states, not derived for all);
* **light**: the $x_0$ dependence that costs mass sits at the tip, where the probability is tiny: $W^\pm$, $Z$ and the twelve fermions. Their
  masses lie $3\times10^{-3}$ (the top quark) to $10^{-17}$ (the lightest neutrino) below $m_{\mathrm{Heis}}$ (that of the broader of the fermion's
  two zero modes; $10^{-3}$ for $W^\pm$), and a sharper localisation of either zero mode gives a LIGHTER fermion ($\mathrm{d}\ln m/\mathrm{d}\ln c$ from
  $-2.9$ to $-34.5$): the reverse of the uncertainty intuition. These masses come from the tip of the cell, where electroweak symmetry is
  broken, and from the exponentially small overlap of the chiral zero modes there.

**Verdict.** Every four-dimensional mass of UM-2 is an $x_0$ eigenvalue of a wave function periodic in $x_0$ with the period $\pi/(6H)$, and
the massless particles are exactly those protected by symmetry (the author's mechanism holds in this precise sense). The uncertainty
relation bounds the hidden kinetic energy, not the mass: it is the reason of the heavy masses (the Kaluza-Klein modes, the odd modes, the
dark matter), while the light masses ($W^\pm$, $Z$ and all twelve fermions) need two further ingredients that do not follow from it, the tip
of the cell and the exponentially localised chiral zero modes, whose overlap at the tip produces the hierarchy of the fermion masses. The
mixing matrices are tip matrices and are not explained by the mechanism.

