---
title: "UM-2 provenance"
subtitle: "Where every ingredient, equation and number of the universe model UM-2 comes from, how it was computed, and how it was verified"
author:
  - "Underlying theory: Patrick L. Nash"
  - "Derived and verified by Claude (Anthropic)"
  - "Provenance, version 2, 2026-10-18 (version 1: 2026-10-17)"
  - "Repository once-ere/Dirac_claude, folder universe_model_2"
---

# How to read this document

This document records the provenance of UM-2, a model of the Universe built on the author's 4+4-dimensional
Einstein-Lovelock theory and his dirac16complex field. For every ingredient it states where it comes from, writes the
ingredient out as an equation, names the computation that produced or used it, and states how it was verified. The
document is self-contained: every equation it mentions is written here.

Version 2 (2026-10-18) contains three generations of quarks and leptons and three neutrino flavours with their mixing and
their flavour conversion, ordered by the author on 2026-10-18; it removes the chiral tip $Z$ portal of version 1. What
changed, and why, is listed in the section on corrections (item 21); the independent review of version 2 and its fixes,
among them the finding that the relic abundance of the dark matter cannot be produced by the gauge-kinetic portal within
perturbative unitarity, are item 22.

Labels used throughout:

* **AUTHOR**: taken from the author's Mathematica notebooks or the author's written orders;
* **RECORD**: taken from the Revision record of this repository (earlier work carried out under the author's orders,
  with its own verification);
* **STANDARD**: textbook physics or a measured value; measured values are marked *verified* (read from the source on
  2026-10-17 or 2026-10-18) or *from memory* (quoted from memory of the standard tables, to be checked against the current
  editions);
* **ASSUMED**: a modelling choice made for UM-2;
* **INVENTED**: a new phenomenological interaction of UM-2;
* **DERIVED**: computed and verified in UM-2;
* **ESTIMATE**: an order-of-magnitude evaluation, not a precision computation;
* **OPEN**: not resolved in this version.

Units: $\hbar = c = 1$; $H$ is the author's constant (an inverse length); in the numerical work $H = 1$ unless a
physical unit is stated.

Symbols with more than one use: $k$ is the block variable $1/f^2$, the Lovelock order as the index of $\alpha_k$ and $E_{(k)}$,
and the momentum of a mode along $x_1, x_2, x_3$ in $e^{ikx_1}$ and $h_j$; $\Lambda = -10H^2$ is the eight-dimensional
cosmological constant, $\Lambda = (m\,fL)^2$ in the $x_0$ eigenvalue problems a dimensionless eigenvalue, and $\Lambda_\star$ the
scale of the effective interactions; $\xi = y/L$ is the scaled hidden coordinate (primes denote $d/d\xi$ in the methods),
while the subscript $t$ ($p_t$, $v_t$, $x_t$) refers to the extra times and $s_h$, $t_h$ are the $4\times4$ blocks of the gamma
matrices; $\rho$ is an energy density, except for the electroweak parameter $\rho = \Lambda_W/(\Lambda_Z\cos^2\theta_W)$ (measured value
$\rho_0$), and $\varrho$ a probability density in $\xi$; $\theta_W$ is the angle of the gauge couplings; $n$ is a number density, except
as a level index ($u_n$, $h^{(1,n)}$, $n \ge 1$) and as the basis size in the Richardson formula, where $p$ is the order;
$w_k$ are the Lovelock weights, $w = 1/2$ the weight of a fold parity, $w = \sqrt{c^2 - e^2}$ in the fermion mass condition and
$w$ an equation-of-state parameter in the supernova fits; $\sigma$ is the radion in the metric expansion and, with indices,
an uncertainty or a Pauli matrix; $i, j = 1, 2, 3$ label generations and neutrino mass states and $\alpha \in \{e, \mu, \tau\}$ flavours;
$U$ is the PMNS and $V$ the CKM matrix (a matter potential carries a subscript, $V_{CC}$); $\kappa$ ($\kappa_\nu$, $\kappa_e$, $\kappa_u$, $\kappa_d$,
$\kappa_f$) is a tip matrix; $e$ is the eigenvalue $\varepsilon fL$ of a fermion, the electron and the elementary charge; $\mu$ is a bulk
mass and the muon, $\mu_N$ the dark-matter-nucleon reduced mass, and $\mu = \sqrt2G_Fn_{\nu_e}$ (no subscript) the unit of the neutrino
self-interaction in the supernova analysis. The time is always $x_4$ (dots denote $d/dx_4$), and the symmetry axis of the fast-flavour
analysis is $x_3$; $A = \dot a_4$ and $h = \dot f/f$ are the expansion rates of 3-space and of the block ($h_\nu$, with a subscript, the comoving
heating of the neutrinos); $H$ is the author's constant, except in the neutrino-decoupling equations, where $H = \sqrt{8\pi\rho/3}/M_{Pl}$ is
the Hubble rate ($H_0$ the Hubble constant today); $F(T_1, T_2)$ is the energy-transfer kernel of the decoupling equations, $F_h$ the
decoupling factor of $\Delta N_{eff}$ and $F_{\mu\nu}$ a field strength; $G(k)$ is the Einstein-Hilbert coefficient of the block, $G(u)$ the
electron-lepton-number distribution of the fast-flavour analysis with its moments $J_n$, $I_n$ and $\Lambda^\mu$ (upper index), and $G_N$, $G_F$,
$G_g$, $G_W$, $G_B$ are couplings; $\eta = HL = 3$ is the depth of the cell and $\eta^{\mu\nu} = \mathrm{diag}(1, -1)$ the flat metric on $(x_4, x_3)$
in the dispersion relation; $\alpha$ is a flavour index, the fine-structure constant and, in the fast-flavour analysis, the density
ratio $n_{\bar\nu_e}/n_{\nu_e}$ ($\alpha_s$ the strong coupling).

# The orders

## The order of 2026-10-17

The model answers the author's order of 2026-10-17. Its key parts, in the author's words: "Create a new model of the
Universe that includes [a] gravity (Einstein-Lovelock gravity); [b] the dirac16complex quantized spinor field (which is
hypothesied to represent dark matter); the dirac16complex is coupled to gravity using a non-trivial canonical spin
connection; ... interactions of gravity and dirac16complex with SOME of the following Standard Model particles: [c]
photons; [d] neutrinos; [e] electrons; [f] quarks (only up and down, for the protons and neutrons); [g] the 3 weak
interaction gauge bosons, the W and Z 'particles'. However do NOT include the Higgs particle. You must invent/create
new phenomenological interactions ... consistent with qcd and electro-weak models. You want to be able to model: CMB,
CNB, BAO, so your model for the metric tensor ... must be very general, but perhaps expressible as a power series of
terms of decreasing magnitude. Put each and every interaction in equation form, and explain and analyze it in
documentation and provenance files; these should be both markdown and latex file types; compile all latex to pdf.
NEVER refer the reader to some other file! PUT EVERY EQUATION you create and/or use IN THESE FILES. CRITICALLY
IMPORTANT: Mass will be given to all non-massless particles, (except the massless particles: graviton, photon and
perhaps the quanta of the dirac16complex field), by appropriate wave function dependence on the space coordinate x0
... periodic in x0 with period $\pi/(6H)$. Localization with respect to x0 implies, using Heisenberg ...
$\Delta x_0\,\Delta p_{x_0} \ge \hbar/2$ ... [2] push your new, improved, model ... along with provenance (both .md
and .pdf files). [3] Compute the coupled field equations and push to repo; create concomitant documention (both .md
and .pdf files) and push. [4] Compute an accurate approximate solution to the coupled field equations (use Kohn-Sham
theory for the dirac16complex field, which couples to all other fields) and push ... Check and verify this repo."

Further orders of the same day: "analyze the x0 mass mechanism, and ... analyze the validity of associating dark
matter (and dark energy) with dirac16complex"; "the $W^+$ and $W^-$ bosons carry positive and negative electric
charges. Do not forget this"; the coordinates are always the author's $\{x_0, x_1, \dots, x_7\}$ of the notebook
`Dirac_Einstein-Lovelock_4+4_Nash.nb`, never relabelled; every verified result is pushed to the repository as soon as
it is obtained; no single calculation runs longer than 7 minutes and 3 seconds (423 s) (this limit was lifted on 2026-10-18).

## The orders of 2026-10-18: three neutrino flavours

On 2026-10-18 the author stated that neutrino flavour and flavour conversion are critically important in this project and
asked that the paper of Gogilashvili and Tamborra on neutrino flavour conversion in core-collapse supernovae (his file
"Neutrino Flavor Conversion.pdf", arXiv:2605.16504; not committed, it is a third-party paper) be read, understood and
remembered (paraphrase). He then ordered, in his words: "correct universe model 2 to include three neutrino flavors with mixing
and flavor conversion. this is your first and only priority!! ... do correct universe model 2 to include three neutrino
flavors with mixing and flavor conversion NOW." Two ways were put to him: (A) three full generations of quarks and leptons,
anomaly free generation by generation; (B) three lepton generations with the single quark generation of version 1, whose
gauge anomalies would have to be cancelled by an added Wess-Zumino term. His answer: "NOT (B). USE (A)!!!". Version 2
implements (A). A flavour is defined by the charged lepton produced with the neutrino in a charged-current process, so
three neutrino flavours require the muon and the tau; with them, anomaly freedom requires the second and third quark
generations (a single quark generation would leave $\mathcal A_{SU(2)^2U(1)} = -1$ and $\mathcal A_{U(1)^3} = 3/2$; DERIVED).

# Who did what

* The 4+4 framework, the coordinates, the primordial metric of the notebooks, the Einstein-Lovelock action with its
  weights and $\Lambda$, the dirac16complex field and its $Cl(4,4)$ gamma matrices, the mass parameter $M$, the idea
  that masses come from the $x_0$ dependence of wave functions periodic with period $\pi/(6H)$, the dark-matter
  hypothesis and the demand for three neutrino flavours with mixing and flavour conversion are the AUTHOR's (Patrick L.
  Nash).
* The corrected primordial metric (version 2), the regular tip cutoff, the Dirac-type Lagrangian with the canonical
  spin connection, the $2\times2$ block reduction of the Kohn-Sham problem and its conventions are RECORD items:
  produced earlier in this repository under the author's orders and verified there.
* Everything labelled ASSUMED, INVENTED or DERIVED below, all the code of UM-2 and all its documents are by Claude
  (Anthropic), working in this repository on 2026-10-17 (version 1) and 2026-10-18 (version 2).

# Ingredients from the author (AUTHOR)

## Coordinates and signature

The author's coordinates (notebook `Dirac_Einstein-Lovelock_4+4_Nash.nb`, `X = {x0[], x1[], ..., x7[]}`) are
$$ X = \{x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7\}: $$
$x_0$ a hidden space-like direction, $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ three extra
time-like directions. The orthonormal frame metric is
$$ \eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1), \qquad a, b = 0, \dots, 7 \text{ aligned with } x_0, \dots, x_7 .$$
The hidden coordinate enters through $z = 6Hx_0$; one period of $x_0$ is $\ell_0 = \pi/(6H)$.

## The primordial metric of the notebooks

The notebook `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb` (the author's local notebook) gives the primordial
metric
$$ \begin{aligned} g^{\text{nb}} = \mathrm{diag}\big(&\cot^2 z,\; e^{2a_4}(\sin^2 z)^{1/6},\; e^{2a_4}(\sin^2 z)^{1/6},\; e^{2a_4}(\sin^2 z)^{1/6},\\
   &-1,\; -e^{-2a_4}(\sin^2 z)^{1/6},\; -e^{-2a_4}(\sin^2 z)^{1/6},\; -e^{-2a_4}(\sin^2 z)^{1/6}\big), \end{aligned} $$
with vielbein $\mathrm{diag}(\cot z, e^{a_4}(\sin^2z)^{1/12}\times3, 1, e^{-a_4}(\sin^2z)^{1/12}\times3)$ and $a_4 = a_4(x_4)$.
By the author's orders of 2026-10-14 a second function $b_4(x_4) > 0$ multiplies the extra-time components ("b4 is a
function of x4; b4 is NEVER 1"), and $(\sin z)^{1/3}$ means $(\sin^2 z)^{1/6}$, the positive branch, for every real $z$.

## The Einstein-Lovelock action, weights and cosmological term

The notebook writes the Einstein-Lovelock vacuum equations (after Lovelock and Rund) as
$$ 0 = -\Lambda^{\text{nb}} + H^{-2}w_1\,\text{Lovelock1} + H^{-4}w_2\,\text{Lovelock2} + H^{-6}w_3\,\text{Lovelock3}, $$
where Lovelock$k$ denotes the notebook's Lovelock tensor of order $k$, the tensor $E_{(k)}{}^M{}_N$ below,
with $(w_1, w_2, w_3, \Lambda^{\text{nb}}) = (1, 1/32, 1/1152, 10)$: in the notebook `Dirac_Einstein-Lovelock_4+4_Nash.nb`
(In[133] to In[136]) the author sets $w_1 = 1$, $w_2 = 1/2^5$ and solves the vacuum equations on the history
$a_4 = Hx_4$, $b_4 = 1$ of the notebook metric for $w_3$ and $\Lambda^{\text{nb}}$ (In[134]); In[136] factors
$1152 = 2^7\,3^2$; the Revision specification records the solution $w_3 = 1/1152$, $\Lambda^{\text{nb}} = 10$.
Multiplying by $H^2$ and writing the equations as
$\sum_k\alpha_kE_{(k)}{}^M{}_N + \Lambda\,\delta^M_N = \kappa T^M{}_N$ gives the UM-2 form
$$ \alpha_k = w_kH^{2-2k}, \qquad w = \Big(1, \frac1{32}, \frac1{1152}\Big), \qquad \Lambda = -\Lambda^{\text{nb}}H^2 = -10H^2 , $$
where
$$ E_{(k)}{}^M{}_N = -\frac{1}{2^{k+1}}\,\delta^{MA_1B_1\cdots A_kB_k}_{NC_1D_1\cdots C_kD_k}\,R^{C_1D_1}{}_{A_1B_1}\cdots R^{C_kD_k}{}_{A_kB_k},$$
$$ \mathcal L_{(k)} = \frac{1}{2^k}\,\delta^{A_1B_1\cdots A_kB_k}_{C_1D_1\cdots C_kD_k}\,R^{C_1D_1}{}_{A_1B_1}\cdots R^{C_kD_k}{}_{A_kB_k} ,$$
$\delta^{\cdots}_{\cdots}$ being the generalised Kronecker delta (the determinant of ordinary deltas); $E_{(1)}$ is the
Einstein tensor, $\mathcal L_{(1)} = R$, $\mathcal L_{(2)} = R^2 - 4R_{AB}R^{AB} + R_{ABCD}R^{ABCD}$. That the UM-2
normalisation reproduces the record's equations (which were checked against the notebook) is verified exactly
(script `um2_geometry.py`, checks `record_equation`). UM-2 keeps the author's weights and $\Lambda$
unchanged; an earlier model of this repository (UM-1) had changed $w_3$ and $\Lambda$.

## The gamma matrices of $Cl(4,4)$

The author's notebooks (*Dirac_Einstein-Lovelock_4+4_Nash.nb* and *WaveFunctionUniverse-4+4-Einstein-Lovelock.nb*)
build real $16\times16$ matrices from ($h = 1, 2, 3$; $p, q = 1, \dots, 4$; $\epsilon$ the Levi-Civita symbol)
$$ Q_a(h,p,q) = \epsilon_{hpq4},\qquad Q_b(h,p,q) = \delta_{p4}\delta_{qh} - \delta_{ph}\delta_{q4},\qquad
   s_h = Q_a - Q_b,\quad t_h = Q_a + Q_b , $$
$$ \zeta_0 = I_8,\quad \zeta_{7-h} = \begin{pmatrix} 0 & t_h\\ -t_h & 0\end{pmatrix},\quad
   \zeta_h = \begin{pmatrix} 0 & s_h\\ s_h & 0\end{pmatrix},\quad \zeta_7 = \zeta_1\zeta_2\zeta_3\zeta_4\zeta_5\zeta_6,\quad
   \sigma = \begin{pmatrix} 0 & I_4\\ I_4 & 0\end{pmatrix}, $$
$$ \tau_0 = I_8,\quad \tau_A = \zeta_A,\quad \bar\tau_A = \sigma\,\tau_A^T\,\sigma,\qquad
   \gamma^{x_A} \equiv T16[A] = \begin{pmatrix} 0 & \bar\tau_A\\ \tau_A & 0\end{pmatrix}\quad (A = 0, \dots, 7). $$
They satisfy $\{\gamma^a, \gamma^b\} = 2\eta^{ab}I_{16}$ and the notebook identities
$\tfrac12(\tau_A\bar\tau_B + \tau_B\bar\tau_A) = \eta_{AB}I_8$, $\sigma = \tau_1\tau_2\tau_3 = \tau_4\tau_5\tau_6\tau_7$ (notebook
Out[322] to Out[324]). Derived objects used by UM-2:
$$ C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3} = \begin{pmatrix} -\sigma & 0\\ 0 & \sigma\end{pmatrix},\qquad
   \Gamma = \gamma^{x_0}\cdots\gamma^{x_7} = \mathrm{diag}(-I_8, I_8),\qquad B = -iC\gamma^{x_4},\qquad S^{ab} = \tfrac14[\gamma^a, \gamma^b] . $$

## The mass parameter, the $x_0$ mass idea and the dark-matter hypothesis

The dirac16complex mass is written $m = 3HM$ in the author's notebooks. The order requires every non-massless
particle to get its mass from the dependence of its wave function on $x_0$, periodic with period $\pi/(6H)$, with the
uncertainty relation $\Delta x_0\,\Delta p_{x_0} \ge \hbar/2$ as the physical reason, and states the hypothesis that
the quanta of dirac16complex represent dark matter (and asks for the validity of a dark-energy association to be
analysed).

# Ingredients from the Revision record (RECORD)

## The corrected primordial metric (version 2)

The author's order of 2026-10-16: "a diagonal form for the metric of the primordial gravitational field is only
self-consistent if all off-diagonal terms of all source terms in the Einstein field equations ARE ZERO. This is not the
case here. I task you to: [1] find the simplest modification for the current metric of the primordial gravitational
field that is probably self-consistent with the Einstein field equations". The metric of 2026-10-14 (the notebook metric
with $b_4$) has the off-diagonal component $E_{(k)}{}^{x_4}{}_{x_0} \propto \cot z\;\dot b_4/b_4$ at every Lovelock order.
In the family (with $g_{44} = -1$)
$$ g_{00} = b_4^{2p}e^{2qa_4}\cot^2z,\qquad g_{ii} = e^{2a_4}(\sin^2z)^{3\alpha},\qquad g_{tt} = -e^{-2a_4}b_4(\sin^2z)^{3\beta} $$
the mixed curvature is proportional to $\alpha\big((q-1)\dot a_4 + p\,\dot b_4/b_4\big)$ (3-space) and
$\beta\big((q+1)\dot a_4 + (p - \tfrac12)\dot b_4/b_4\big)$ (extra times). Keeping the warp of the extra times
($\beta = 1/6$) forces $\alpha = 0$, $q = -1$, $p = 1/2$: the record's current metric, used by UM-2,
$$ \bar g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2z,\; e^{2a_4},\; e^{2a_4},\; e^{2a_4},\; -1,\; -e^{-2a_4}b_4(\sin^2z)^{1/6},\;
   -e^{-2a_4}b_4(\sin^2z)^{1/6},\; -e^{-2a_4}b_4(\sin^2z)^{1/6}\big) .$$
Every off-diagonal component of $E_{(1)}, E_{(2)}, E_{(3)}$ vanishes identically for all $a_4(x_4)$, $b_4(x_4) > 0$
and every real $z$ (record: sympy 14/14, Wolfram 13/13; re-derived in UM-2, `um2_geometry.py`). The alternative K of the
record ($g_{00} = e^{2a_4}\cot^2z$, $g_{ii} = e^{2a_4}(\sin^2z)^{1/6}$, $g_{tt} = -e^{-2a_4}b_4$) is also diagonal at every
order; the record leaves the choice to the author, and UM-2 uses version 2.

## The hidden coordinate, the fold and the regular tip

On every interval with $\sin z \ne 0$,
$$ y = \frac{\ln\lvert\sin z\rvert}{6H} \in (-\infty, 0],\qquad dy = \cot z\,dx_0,\qquad f = e^{-a_4}b_4^{1/2},$$
$$ ds^2 = e^{2a_4}d\vec x^{\,2} - dx_4^2 + f^2\big[dy^2 - e^{2Hy}(dx_5^2 + dx_6^2 + dx_7^2)\big] .$$
The fold is $z = \pi/2$ ($y = 0$); the tips are $z \to 0^+$ and $z \to \pi^-$ ($y \to -\infty$). The record replaces the
tip by a regular cutoff at $y = -L$ with
$$ \eta \equiv HL = 3 , $$
a chosen cutoff (the extended levels depend on it like those of a box of proper length $fL$). UM-2 keeps $\eta = 3$
(ASSUMED).

## The dirac16complex Lagrangian and the canonical spin connection

The specification of the record (under the author's orders) fixes the Dirac-type Lagrangian
$$ \mathcal L_\Psi = \sqrt{\lvert g\rvert}\Big[\tfrac12\big(\bar\Psi\gamma^MD_M\Psi - (D_M\bar\Psi)\gamma^M\Psi\big) - m\,\bar\Psi\Psi - U(S)\Big],\qquad
   S = \bar\Psi\Psi,\quad U(S) = \frac{\lambda}{2}S^2,\quad \bar\Psi = \Psi^\dagger C , $$
$$ D_M\Psi = \partial_M\Psi + \Omega_M\Psi,\quad \Omega_M = \tfrac12\omega_{Mab}S^{ab},\quad \omega_M{}^a{}_b = e^a{}_N\big(\partial_Me_b{}^N + \Gamma^N{}_{ML}e_b{}^L\big),\quad \gamma^M = e_a{}^M\gamma^a , $$
the canonical (vielbein-postulate, torsion-free) spin connection. The record chose the Dirac-type form because the
notebook's real Majorana-type Lagrangian is a total derivative for anticommuting real fields (it has no field
equations), and it uses the canonical connection rather than the notebook's contraction of the mixed
$\omega_M{}^a{}_b$, which lacks a metric factor. The field equation is $\gamma^MD_M\Psi = (m + U'(S))\Psi$.

## Canonical quantisation and the Krein metric

With $x_4$ as the evolution time, $\{\Psi_r(x), \Psi_s^\dagger(x')\} = B_{rs}\,\delta^7(x - x')/\sqrt{\lvert g\rvert}$ ($r, s$ spinor indices) on a slice
$x_4 = \text{const}$; $B$ has eigenvalues $+1$ (8 times) and $-1$ (8 times), so the inner product is indefinite (a Krein
space). The record works in the good sector (no extra-time momentum), counts the positive-energy branch of every block
as particles, and evaluates expectation values as $\langle\Psi^\dagger M\Psi\rangle = u^\dagger BMu$.

## The Kohn-Sham reduction

For the corrected metric the record reduces the 16-component equation, with
$\Psi = e^{ikx_1}\,e^{-\frac32Hy}\,e^{a_4/2}b_4^{-1}\,V_\beta\,\chi(y, x_4)$ ($k$ the momentum along $x_1$), to the $2\times2$ block Hamiltonians
$$ h_j = j\Big[-\frac{i}{f}\sigma_1\partial_y + M(y)\,\sigma_2 + e^{-a_4}k\,\sigma_3\Big] + v(y), $$
in the blocks $(j, s_2, s_3)$ of the commuting set $J = \gamma^{x_0}\gamma^{x_1}\gamma^{x_4}$, $K_1 = \gamma^{x_2}\gamma^{x_3}$,
$K_2 = \gamma^{x_5}\gamma^{x_6}$ (eigenvalues $j$, $is_2$, $is_3$), with the contact-interaction mean fields of the
record's Hartree-plus-exchange treatment of the contact interaction
$$ e_{int} = \frac{15}{32}\lambda S^2 - \frac{1}{32}\lambda n^2,\qquad M_{eff} = m + \frac{15}{16}\lambda S,\qquad v = -\frac{\lambda}{16}n , $$
the fold conditions $\theta \in \{0, \pi\}$ (both parities filled, weight $w = 1/2$ each), the regular tip, and the
densities carrying $P = e^{-3Hy}/\mathrm{Vol}_7$, with $\mathrm{Vol}_7 = (2\pi/\Delta k)^3v_tf^4$ the normalisation volume of a cell
($\Delta k$ the spacing of the momentum lattice, $v_t$ the coordinate volume of the extra times, $a_4 = 0$; the proper
seven-volume of a cell is $2\,\mathrm{Vol}_7(1 - e^{-3\eta})/(3H)$). The record's mass is $m = 3HM$ with $M = 1/3$, i.e. $m = H$; UM-2
keeps it (ASSUMED). Two reference states of the record (at $f = 1$, $a_4 = 0$: $N = 8$ with $\lambda = 157.7$, and
$N = 592$ with $\lambda = 2.131$) serve as validation targets of the independent UM-2 solver.

## Earlier work used only for comparison

The first universe model of this repository (UM-1, folder `Revision/universe_model`) is not an input of UM-2. UM-2
differs from it in keeping the author's weights and $\Lambda$, in the electroweak sector, in the number of generations and in
the dark-matter candidate. Version 1 of UM-2 (2026-10-17, one generation) is superseded by version 2; its differences are
listed in item 21 of the corrections.

# Standard physics and measured values (STANDARD)

Every measured value enters UM-2 in one of three roles, never as a derived result: as the target of a fit (the $W^\pm$ and $Z$
masses with $\rho_0$, the twelve fermion masses, the two neutrino splittings with the chosen $m_1$, and $\Omega_ch^2$ for the freeze-out
requirement), as a direct input (the angles and phases of the PMNS and CKM matrices, $G_F$, the $\overline{MS}$ value of $\sin^2\theta_W$ in the
$Z$ widths, $\alpha_s$, $\alpha$, $T_0$, the Planck 2018 parameters of the cosmology, the effective couplings and kernel factors of the decoupling
equations, the matter densities and the supernova parameters), or as a comparison (the $Z$ widths, $N_\nu$, $N_{eff}$, the BAO, the
explosion statistics, the supernova dark-energy fits, the LZ limit).

| input | value used | source | status |
| --- | --- | --- | --- |
| $W^\pm$ mass | $80.3625 \pm 0.0077$ GeV | PDG 2026, OUR EVALUATION (pdgLive S043M) | verified |
| $Z$ mass | $91.1879 \pm 0.0020$ GeV | PDG 2026, OUR AVERAGE (pdgLive S044M) | verified |
| $\sin^2\theta_W$ ($\overline{MS}$, $M_Z$) | $0.23122 \pm 0.00004$ | PDG electroweak review | from memory |
| electroweak $\rho$ parameter | $\rho_0 - 1 = 0.00038 \pm 0.00020$ | PDG electroweak review (global fit) | from memory |
| charged-lepton masses | $m_e = 0.51099895000$ MeV, $m_\mu = 105.6583755$ MeV, $m_\tau = 1776.93 \pm 0.09$ MeV | PDG 2025 summary tables | verified |
| light-quark masses ($\overline{MS}$, 2 GeV) | $m_u = 2.16 \pm 0.07$ MeV, $m_d = 4.70 \pm 0.07$ MeV, $m_s = 93.5 \pm 0.8$ MeV | PDG 2025 summary tables | verified |
| heavy-quark masses | $m_c(m_c) = 1.2730 \pm 0.0046$ GeV, $m_b(m_b) = 4.183 \pm 0.007$ GeV, $m_t = 172.56 \pm 0.31$ GeV (direct) | PDG 2025 summary tables | verified |
| neutrino oscillation parameters (normal ordering) | $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{23} = 0.470$, $\sin^2\theta_{13} = 0.02215$, $\delta = 212^\circ$, $\Delta m^2_{21} = 7.49\times10^{-5}$ eV$^2$, $\Delta m^2_{31} = 2.513\times10^{-3}$ eV$^2$; inverted ordering $\Delta\chi^2 = 6.1$; $J_{max} = 0.0333 \pm 0.0007$ | NuFIT 6.0, arXiv:2410.05380 (JHEP 12 (2024) 216), Table 1, IC24 with SK atmospheric data | verified |
| lightest neutrino mass | $m_1 = 1.000$ meV | chosen | ASSUMED |
| sum of neutrino masses | $\sum m_\nu < 0.064$ eV (95 %, $\Lambda$CDM) | DESI DR2 Results II, arXiv:2503.14738 | verified |
| CKM parameters | $s_{12} = 0.22501$, $s_{13} = 0.003732$, $s_{23} = 0.04183$, $\delta = 1.147$ rad; $J = 3.12\times10^{-5}$ | PDG 2024 review "CKM quark-mixing matrix", global fit | verified |
| strong coupling | $\alpha_s(m_Z) = 0.1180$ | PDG world average | from memory |
| Fermi constant, electroweak scale | $G_F = 1.1663788\times10^{-5}$ GeV$^{-2}$, $v = 246.22$ GeV | PDG | from memory |
| fine-structure constant | $\alpha^{-1}(0) = 137.035999$ | CODATA | from memory |
| number of light neutrinos | $N_\nu = 2.9963 \pm 0.0074$ | PDG 2025 (Janot and Jadach, Phys. Lett. B803 (2020) 135319) | verified |
| (superseded, version 1) | $N_\nu = 2.9840 \pm 0.0082$ | LEP/SLD, Phys. Rept. 427 (2006) 257 | verified |
| $Z$ width and branching fractions | $\Gamma_Z = 2495.5 \pm 2.3$ MeV; invisible $20.000$ %, hadrons $69.911$ %, $\ell^+\ell^-$ $3.3658$ % | PDG 2025 $Z$ listing | verified |
| nucleon masses | $m_p = 938.272$ MeV, $m_n = 939.565$ MeV | PDG | from memory |
| $\hbar c$, $k_B$, $N_A$ | $1.973269804\times10^{-16}$ GeV m, $8.617333262\times10^{-5}$ eV/K, $6.02214076\times10^{23}$ | CODATA, SI | from memory |
| CMB temperature | $T_0 = 2.7255$ K | Fixsen 2009 | from memory |
| $N_{eff}$ in the Standard Model | $3.0432 \pm 0.0002$ (three flavours, oscillations, NLO) | Cielo, Escudero, Mangano, Pisanti, arXiv:2306.05460 | verified |
| $N_{eff}$ by the method of temperatures | $3.000$, $3.011$, $3.010$, $3.039$, $3.049$, $3.048$ (Table 1); couplings $g_{eL} = 0.727$, $g_{eR} = 0.233$, $g_{\mu L} = -0.273$, $g_{\mu R} = 0.233$; $f_a = 0.884$, $f_s = 0.829$ | Escudero, arXiv:2001.04466 | verified (2026-10-18) |
| finite-temperature QED pressure | $P_2$, $P_3$ of the $e^\pm\gamma$ plasma (formulas below) | Bennett et al., arXiv:1911.04504 | from memory; massless limits reproduced to $10^{-16}$ |
| $N_{eff}$ measured | $2.99 \pm 0.17$ (Planck 2018 + BAO); $2.86 \pm 0.13$ (ACT DR6) | Planck 2018 VI, A&A 641 (2020) A6; Calabrese et al., arXiv:2503.14454 | verified |
| Planck 2018 base parameters | $\omega_b = 0.02237$, $\omega_c = 0.1200$, $100\,\theta_{MC} = 1.04092$, $\tau_{reio} = 0.0544$, $\ln(10^{10}A_s) = 3.044$, $n_s = 0.9649$ | Planck 2018 results VI, Table 2 | from memory |
| BAO | DESI DR2: 13 measurements of $D_V/r_d$, $D_M/r_d$, $D_H/r_d$ (table below) | DESI collaboration, arXiv:2503.14738 | values verified (2026-10-17) against Table 2 of arXiv:2603.26861; correlations from memory |
| dark-matter density | $\Omega_ch^2 = 0.120$ | Planck 2018 | from memory |
| Planck mass (freeze-out) | $M_{Pl} = G_N^{-1/2} = 1.22091\times10^{19}$ GeV | | from memory |
| reduced Planck mass (radion decay) | $\bar M_{Pl} = (8\pi G_N)^{-1/2} = 2.435\times10^{18}$ GeV | | from memory |
| angle of the gauge couplings | $\cos^2\theta_W = (m_W^2/m_Z^2)/\rho_0 = 0.776368$ (used for $\beta_Z = \beta_W/\cos^2\theta_W$ and in $\rho = \Lambda_W/(\Lambda_Z\cos^2\theta_W)$); the on-shell value $m_W^2/m_Z^2 = 0.776663$ for comparison | computed from the $W^\pm$, $Z$ masses and $\rho_0$ above | computed |
| solar electron density | $n_e = 245\,N_A\,e^{-10.54\,r/R_\odot}$ cm$^{-3}$ outside the core, at most $100\,N_A$ cm$^{-3}$ (exponential fit) | after Bahcall | ASSUMED profile |
| matter of the Earth | $\rho = 2.6$ (T2K), $2.84$ (NOvA), $2.848$ (DUNE), $2.8$ g/cm$^3$ (resonance); $Y_e = 0.5$ | representative constant densities | ASSUMED |
| supernova envelope and neutrinospheres | $\rho(r) = 10^4\,(10^9\,\text{cm}/r)^3$ g/cm$^3$, $Y_e = 0.5$; $L = 6, 6, 4\times10^{52}$ erg/s, $\langle E\rangle = 11, 14, 15.5$ MeV ($\nu_e$, $\bar\nu_e$, $\nu_x$); $n_{\nu_e} = 10^{32}$ to $10^{33}$ cm$^{-3}$ | representative values | ASSUMED |
| supernova explosion statistics with flavour conversion | failed fractions $25.6$ % (none), $50.8$, $77.4$, $93.3$, $96.4$ % ($\rho_c = 10^9$ to $10^{13}$ g/cm$^3$); Salpeter-weighted $27.0$, $47.6$, $61.9$, $73.9$, $88.3$ % | Gogilashvili and Tamborra, arXiv:2605.16504 (the author's file) | verified (read 2026-10-18) |
| fast flavour instability criterion | instability if and only if the ELN distribution has a crossing | Morinaga, Phys. Rev. D 105 (2022) L101301 | from memory |
| direct-detection limit | LZ: $2.2\times10^{-48}$ cm$^2$ at 40 GeV, scaled linearly with the mass | LZ 2024 | from memory; the extrapolation is an ESTIMATE |
| nucleon gluon content, strong coupling | $f_{TG} = 0.92$, $\alpha_s = 0.3$ (low scale) | standard | from memory; ESTIMATE |
| dark-energy density | $\rho_\Lambda \approx 2.5\times10^{-47}$ GeV$^4$ | | from memory |
| supernova dark-energy fits | constant $w = -0.764$; $(w_0, w_a) = (-0.861, -0.60)$ | the author's private file (not in the repository) | AUTHOR |

The DESI DR2 BAO measurements used ($z$; $D_V/r_d$; $D_M/r_d$; $D_H/r_d$; correlation $r_{MH}$ of $D_M$ and $D_H$):

| tracer | $z$ | $D_V/r_d$ | $D_M/r_d$ | $D_H/r_d$ | $r_{MH}$ |
| --- | --- | --- | --- | --- | --- |
| BGS | 0.295 | $7.942 \pm 0.075$ | | | |
| LRG1 | 0.510 | | $13.588 \pm 0.167$ | $21.863 \pm 0.425$ | $-0.459$ |
| LRG2 | 0.706 | | $17.351 \pm 0.177$ | $19.455 \pm 0.330$ | $-0.404$ |
| LRG3+ELG1 | 0.934 | | $21.576 \pm 0.152$ | $17.641 \pm 0.193$ | $-0.416$ |
| ELG2 | 1.321 | | $27.601 \pm 0.318$ | $14.176 \pm 0.221$ | $-0.434$ |
| QSO | 1.484 | | $30.512 \pm 0.760$ | $12.817 \pm 0.516$ | $-0.500$ |
| Ly$\alpha$ | 2.330 | | $38.988 \pm 0.531$ | $8.632 \pm 0.101$ | $-0.431$ |

with
$$ \chi^2 = \sum_i (d_i - d_i^{th})^TC_i^{-1}(d_i - d_i^{th}),\qquad C_i = \begin{pmatrix}\sigma_M^2 & r_{MH}\sigma_M\sigma_H\\ r_{MH}\sigma_M\sigma_H & \sigma_H^2\end{pmatrix} $$
($d_i$ the measured and $d_i^{th}$ the computed pair of $D_M/r_d$, $D_H/r_d$) for the anisotropic tracers and $(d - d^{th})^2/\sigma_V^2$ for BGS, where $D_M(z) = \int_0^z c\,dz'/H(z')$ (flat),
$D_H = c/H(z)$, $D_V = (zD_M^2D_H)^{1/3}$.

Standard theory used: the Standard-Model gauge theory $SU(3)_c\times SU(2)_L\times U(1)_Y$ with three generations; QCD
confinement of the quarks into hadrons (protons and neutrons); the PMNS and CKM matrices in the standard parametrisation
$$ U = \begin{pmatrix} c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta}\\ -s_{12}c_{23} - c_{12}s_{23}s_{13}e^{i\delta} & c_{12}c_{23} - s_{12}s_{23}s_{13}e^{i\delta} & s_{23}c_{13}\\
   s_{12}s_{23} - c_{12}c_{23}s_{13}e^{i\delta} & -c_{12}s_{23} - s_{12}c_{23}s_{13}e^{i\delta} & c_{23}c_{13}\end{pmatrix} $$
($s_{ij} = \sin\theta_{ij}$, $c_{ij} = \cos\theta_{ij}$; the CKM matrix $V$ has the same form) with the Jarlskog invariant
$J = c_{12}s_{12}c_{23}s_{23}c_{13}^2s_{13}\sin\delta$; the flavour evolution of the amplitudes $\psi = (\psi_e, \psi_\mu, \psi_\tau)$ of a neutrino of energy $E$
along its path, $i\,d\psi/dx_4 = [U\,\mathrm{diag}(m_1^2, m_2^2, m_3^2)U^\dagger/(2E) + \mathrm{diag}(V_{CC}, 0, 0)]\psi$ with $V_{CC} = \sqrt2G_Fn_e$
(Wolfenstein, Mikheyev and Smirnov; antineutrinos $U \to U^*$, $V_{CC} \to -V_{CC}$); the tree-level $Z$ partial width
$\Gamma(Z\to f\bar f) = N_c\,G_Fm_Z^3(g_V^2 + g_A^2)/(6\sqrt2\pi)$, $g_V = T_3 - 2Q\sin^2\theta_W$ (with the $\overline{MS}$ value
$\sin^2\theta_W = 0.23122$), $g_A = T_3$; the radiative decay $\mathrm{BR}(\mu\to e\gamma) = \frac{3\alpha}{32\pi}\lvert\sum_iU^*_{\mu i}U_{ei}m_i^2/m_W^2\rvert^2$ for Dirac
neutrinos; the freeze-out of a relic (Kolb and Turner); the trace-anomaly nucleon matrix element; the Einstein-Boltzmann
equations of linear cosmological perturbations (solved by CAMB); the linearised equations of a dense neutrino gas (fast flavour
conversion); Higgsless electroweak symmetry breaking by a non-linear sigma field and fermion localisation in an extra dimension
(concepts only, no numbers).

# Ingredients new in UM-2 (ASSUMED and INVENTED)

## The metric as a power series (ASSUMED)

$$ g_{MN} = \bar g_{MN} + \epsilon\,h^{(1)}_{MN} + \epsilon^2h^{(2)}_{MN} + \dots,\qquad \epsilon \sim 10^{-5}\ \text{(the CMB anisotropy)},$$
$$ h^{(1)}_{MN}(x^\mu, x_0) = \sum_{n\ge0}h^{(1,n)}_{MN}(x^\mu)\,u_n(x_0), $$
with $u_n$ the eigenfunctions of the $x_0$ operator; the flat $n = 0$ term in the Newtonian gauge,
$$ ds^2 = e^{2a_4}\big[(1 - 2\epsilon\Psi_N)\delta_{ij} + \epsilon h^{TT}_{ij}\big]dx_idx_j - (1 + 2\epsilon\Phi)dx_4^2
   + f^2(1 + 2\epsilon\sigma)\big[dy^2 - e^{2Hy}d\vec x_t^{\,2}\big] , $$
carries the CMB, CNB and BAO physics; the radion $\sigma$ and the $n \ge 1$ Kaluza-Klein modes are massive.

## The block stabiliser (ASSUMED; its origin is OPEN)

$$ S_{stab} = -\int d^8x\sqrt{\lvert g\rvert}\;\rho_b(f),\qquad \kappa\rho_b(f) = \kappa\rho_b^*\Big(\frac{f_*}{f}\Big)^8,$$
$$ T^M{}_N[\text{stab}] = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho_b, p_t, p_t, p_t),\qquad p_3 = -\rho_b,\qquad p_0 = p_t = \rho_b . $$
It is conserved ($\dot\rho_b = -3A(\rho_b + p_3) - 4h(\rho_b + p_0) = -8h\rho_b$, so $\rho_b \propto f^{-8}$), four-dimensionally
Lorentz invariant ($p_3 = -\rho_b$) and isotropic in the block ($p_0 = p_t$). It was introduced because the author's
weights and $\Lambda$ admit no static block with attractive four-dimensional gravity without a source: the only
sourceless static block with $A = 0$ is $k_0 = 1/(4w_2) = 8$, where the coefficient of the four-dimensional
Einstein-Hilbert term is $G(k_0) = 1 - 24w_2k_0 + 72w_3k_0^2 = -1$ (repulsive), with $\Lambda_0 = -24H^2 \ne -10H^2$
(`um2_background.py`).
The family $p_0 = p_t = \nu\rho_b$, $\rho_b \propto f^{-4(1+\nu)}$, was also computed at $\nu = 1/4, 1/2, 3/4, 1, 5/4, 3/2, 2, 3$.

## The Standard-Model fields in eight dimensions (ASSUMED structure; boundary conditions INVENTED)

$$ S_{gauge} = -\frac14\int d^8x\sqrt{\lvert g\rvert}\,g^{MP}g^{NQ}\Big(\frac{1}{\hat g_s^2}G^\alpha_{MN}G^\alpha_{PQ} + \frac{1}{\hat g^2}W^a_{MN}W^a_{PQ} + \frac{1}{\hat g'^2}B_{MN}B_{PQ}\Big),$$
$$ S_f = \sum_{i=1}^3\sum_\psi\int d^8x\sqrt{\lvert g\rvert}\Big[\tfrac12\big(\bar\psi_i\gamma^MD_M\psi_i - (D_M\bar\psi_i)\gamma^M\psi_i\big) - \mu_{\psi i}\bar\psi_i\psi_i\Big],$$
$$ D_M = \partial_M + \Omega_M - iG^\alpha_MT^\alpha - iW^a_M\frac{\tau^a}{2} - iYB_M ,$$
for three generations $i = 1, 2, 3$ of $Q_i$ ($(u, d)_L$, $(c, s)_L$, $(t, b)_L$), $u_{Ri}$ ($u_R$, $c_R$, $t_R$), $d_{Ri}$ ($d_R$, $s_R$, $b_R$), $L_i$
($(\nu_e, e)_L$, $(\nu_\mu, \mu)_L$, $(\nu_\tau, \tau)_L$, the neutrinos here the weak partners, not the mass states $\nu_1, \nu_2, \nu_3$), $e_{Ri}$ ($e_R$, $\mu_R$, $\tau_R$) and
$\nu_{Ri}$ (hypercharges $1/6, 2/3, -1/3, -1/2, -1, 0$), each a 16-component spinor of the same Clifford algebra times its gauge indices,
with one doublet bulk mass per sector ($\mu_{Li} = \mu_L$, $\mu_{Qi} = \mu_Q$; ASSUMED). With the selection projector
$$ P_{sel} = \frac{1 + \Gamma_4\gamma^{x_0}}{2}\,\frac{1 - i\gamma^{x_5}\gamma^{x_6}}{2},\qquad \Gamma_4 = i\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}\gamma^{x_4}, $$
the conditions at the fold and the tip are, for doublets ($\mu_\psi > 0$),
$P_{sel}(1 - \gamma^{x_0})\psi = 0$, $(1 - P_{sel})(1 + \gamma^{x_0})\psi = 0$ at the fold and $(1 - \gamma^{x_0})\psi = 0$ at the tip,
and for singlets ($\mu_\psi < 0$) the same with $\gamma^{x_0} \to -\gamma^{x_0}$. The weak bosons are
$W^\pm = (W^1 \mp iW^2)/\sqrt2$, with electric charges $+e$ ($W^+$) and $-e$ ($W^-$).

## The tip sigma field and the tip matrices (INVENTED for this geometry; no Higgs particle)

$$ S_{tip} = \int_{y=-L}d^7x\sqrt{\lvert g_{tip}\rvert}\Big[-\frac{v_\Sigma^2}{4}\mathrm{tr}\big((D_\mu\Sigma)^\dagger D^\mu\Sigma\big)
   - \sum_{i,j=1}^3\big(\bar L_i\,\Sigma\,(\Lambda_\ell)_{ij}\,\ell_{Rj} + \bar Q_i\,\Sigma\,(\Lambda_q)_{ij}\,q_{Rj} + \text{h.c.}\big)\Big],\qquad \Sigma \in SU(2),$$
$$ D_\mu\Sigma = \partial_\mu\Sigma - iW^a_\mu\frac{\tau^a}{2}\Sigma + iB_\mu\Sigma\frac{\tau^3}{2},\qquad \Sigma \to U_L\Sigma U_Y^\dagger,\quad U_Y = e^{i\theta\tau^3/2} ,$$
with the singlets arranged as $SU(2)_R$-type doublets $\ell_{Rj} = (\nu_{Rj}, e_{Rj})$, $q_{Rj} = (u_{Rj}, d_{Rj})$ and
$(\Lambda_\ell)_{ij} = \mathrm{diag}((\lambda_\nu)_{ij}, (\lambda_e)_{ij})$, $(\Lambda_q)_{ij} = \mathrm{diag}((\lambda_u)_{ij}, (\lambda_d)_{ij})$ with four complex $3\times3$ tip coupling
matrices $\lambda_\nu$, $\lambda_e$, $\lambda_u$, $\lambda_d$ (the upper component of $\Sigma^\dagger L_i$ couples to $\nu_R$, the lower one to $e_R$). On the zero modes they become the tip conditions
$b_L = \kappa b_R$, $a_R = -\kappa^\dagger a_L$ with the tip matrices (ASSUMED values)
$$ \kappa_\nu = U_{PMNS},\qquad \kappa_e = 1,\qquad \kappa_u = 1,\qquad \kappa_d = V_{CKM} .$$

## The portal interactions (INVENTED)

$$ S_{I11} = \int d^8x\sqrt{\lvert g\rvert}\;\frac{c_V}{\Lambda_\star^6}(i\bar\Psi\gamma^M\Psi)\sum_{i=1}^3\sum_\psi q_\psi(i\bar\psi_i\gamma_M\psi_i),$$
$$ S_{I12} = -\int d^8x\sqrt{\lvert g\rvert}\;\frac{\bar\Psi\Psi}{\Lambda_\star^3}\big[c_GG^\alpha_{MN}G^{\alpha MN} + c_WW^a_{MN}W^{aMN} + c_BB_{MN}B^{MN}\big].$$
Removed in version 2 (DERIVED reasons in item 21): the chiral tip $Z$ portal of version 1,
$$ S_{I9} = \int_{y=-L}d^7x\sqrt{\lvert g_{tip}\rvert}\big[c_Z + c'_Z\varsigma\big](i\bar\Psi\gamma^\mu P_+\Psi)\,\frac{iv_\Sigma^2}{2}\mathrm{tr}\big(\Sigma^\dagger D_\mu\Sigma\,\tau^3\big),\qquad P_+ = \frac{1 + \Gamma_4}{2},\quad \varsigma = \pm1,$$
now $c_Z = c'_Z = 0$. Operators considered and rejected: a dipole portal $\bar\Psi S^{MN}\Psi B_{MN}$ (it would thermalise the sterile
fold bands through the photon: too much dark radiation) and any operator coupling the neutral $\Psi$ to a single $W^+$ or
$W^-$ (none is gauge invariant).

## Parameter choices (ASSUMED)

$\eta = 3$ and $m = H$ (from the record); the universal tip mixing $\kappa_f = 1$ (unitary tip matrices); the doublet localisations
fixed by the heaviest member of each sector, $c_R(\tau) = -c_L$ and $c_R(t) = -c_Q$; the lightest neutrino mass $1$ meV and the
normal ordering; $c_V = 0$ (benchmark); the Kohn-Sham benchmark self-coupling $\lambda_B = 7\times10^{-5}H^{-6}$ (mean fields
below 5 % of $m$ in the densest benchmark state); the extra-time coordinate volume $v_t$ (it enters only $V_\perp$).

# The computations and their verification (DERIVED)

All computations are Python scripts in the folder `universe_model_2/code`; each writes its numbers to
`universe_model_2/outputs` and a report of named checks (name, verdict, detail) to `universe_model_2/reports`. In total
205 checks, none failed.

| script | what it computes | method | checks |
| --- | --- | --- | --- |
| `um2_algebra.py` | the author's gamma matrices rebuilt from the notebook formulas; $C$, $\Gamma$, $B$; Pin(4,4) irreducibility; the two inequivalent Spin(4,4) halves; the $2\times2$ block basis and the block forms of every matrix the reductions use | sympy, exact | 31/31 |
| `um2_geometry.py` | Riemann tensor of $\bar g$ in two charts; Lovelock tensors by four routes (pairing formula, Ricci, explicit Gauss-Bonnet tensor, minisuperspace variation with a lapse); Bianchi identities; the record's equations; the static block; the canonical spin connection | sympy, exact | 25/25 |
| `um2_background.py` | the class-form background equations; the static block; the stabiliser and its family; the radion; the linear response of the block to matter sources; the dimensional reduction | sympy, exact; eigenvalues numerically | 22/22 |
| `um2_fields.py` | the exact $x_0$ reduction of the eight-dimensional Dirac equation (all blocks, general $a_4$, $b_4$, $M(y)$, $v(y)$); boundary conditions; zero modes; tip mixing for one and for three generations (self-adjointness with an arbitrary complex $3\times3$ matrix); the gauge $x_0$ operator; gauge invariance of the three-generation tip terms | sympy and numpy | 16/16 |
| `um2_spectra.py` | the $x_0$ spectra of gauge bosons and graviton; the $W^\pm$, $Z$ fit to $\rho_0$ with the angle of the couplings fixed by the measured masses (both masses reproduced); the twelve fermion masses as exact $x_0$ eigenvalues | mpmath root finding; quadratic finite elements with Richardson; ODE shooting | 14/14 |
| `um2_flavour.py` | the PMNS and CKM matrices; the exact three-generation tip determinant and its null vectors; a general complex tip matrix; flavour-changing couplings of the Kaluza-Klein gauge modes; $\mu\to e\gamma$; lepton universality | mpmath (50 digits), numpy | 7/7 |
| `um2_neutrino.py` | vacuum and matter oscillations, the MSW resonances, long-baseline appearance, the Sun, the onset of oscillations in the early Universe, neutrino decoupling and $N_{eff}$, the CNB, supernova resonances, the fast flavour instability, the heating behind the shock | exact matrix exponentials and layer products; LSODA; Gauss-Legendre panels; vectorised Newton iterations | 15/15 |
| `um2_ks_jobs.py` | Kohn-Sham: validation against the record (2/2), free spectrum (3/3), interacting ground states $N = 8$ (3/3) and $N = 592$ (4/4), dark-matter quanta (3/3), portal responses with the three-generation sources (5/5), block feedback (2/2) | Galerkin in the free basis, safeguarded Anderson self-consistency, Richardson in the basis size | 22/22 |
| `um2_electroweak.py` | charges ($W^+$: $+e$, $W^-$: $-e$), anomalies of three generations, couplings, $P_+$, $\Gamma_4 = -B\gamma^{x_0}$, chiral tip charges of $\Psi_A$, $\Psi_B$, $N_\nu$, the removal of the tip $Z$ portal, the $Z$ widths of three generations and their scheme dependence | sympy and numerics | 19/19 |
| `um2_primordial.py` | the nonlinear primordial evolution, the basin, the separatrix, the radion oscillation | DOP853 integration, bisection | 5/5 |
| `um2_cosmology.py` | TT and EE spectra with three massive neutrinos, BAO $\chi^2$, $N_{eff}$, helium, the attribution of the differences, the variants with a thermalised fold band | CAMB 2.0.5 | 6/6 |
| `um2_analysis.py` | the $x_0$ decompositions and the uncertainty relation on the cell (with its tip term); the gap theorem; sum rules; the twelve fermions against the uncertainty estimate; the conservation of the halves $\Psi_A$, $\Psi_B$; relic abundance of two species; direct detection; the condensate; the vacuum energy; the sensitivities to the block size (with the neutrino splittings); the bound on the block rate today; the radion decay | mpmath, numpy, sympy | 23/23 |

## The principal numbers and where they come from

| quantity | value | computed by |
| --- | --- | --- |
| static block $k_*$, $f_*$, $G(k_*)$, $\kappa\rho_b^*$ | $12 + \tfrac43\sqrt{51} = 21.5219$, $0.215556$, $\tfrac{20}{3} + \sqrt{51} = 13.8081$, $(26 + 4\sqrt{51})H^2$ | `um2_background.py` |
| radion | $\omega_r^2/H^2 = 31552/2249 - 2416\sqrt{51}/6747 = 11.4721$, $m_r = 3.387H = 48.42$ TeV | `um2_background.py`, `um2_spectra.py` |
| unbroken $x_0$ spectrum ($\eta = 3$) | $\Lambda = 0$; $\Lambda_1 = 30.1196$; odd $27.0890$; gap $20.25$ | `um2_spectra.py` |
| $W^\pm$, $Z$ | $\beta_W = 0.011912$, $\beta_Z = 0.015343$ ($\cos^2\theta_W = 0.776368$), $\Lambda_W = 1.32149\times10^{-5}$, $\Lambda_Z = 1.70150\times10^{-5}$, $\rho - 1 = 0.00038$, model $m_Z = 91.1879$ GeV; Dirichlet bound $\Lambda_D = 0.010016$ | `um2_spectra.py` |
| scales | $m_{KK} = 121.32$ TeV, $H = 14.296$ TeV, proper half cell $fL = 8.926\times10^{-21}$ m, $x_0$ period $7.227\times10^{-21}$ m, gap $99.48$ TeV | `um2_spectra.py` |
| fermion localisations ($\kappa_f = 1$) | doublets $c_L = 5.9529$, $c_Q = 3.3823$; singlets $c_R$: $\nu_1$ $-35.0452$, $\nu_2$ $-32.8481$, $\nu_3$ $-31.0702$, $e$ $-14.5539$, $\mu$ $-8.9809$, $\tau$ $-5.9529$, $u$ $-15.4300$, $c$ $-8.7683$, $t$ $-3.3823$, $d$ $-14.6258$, $s$ $-11.5158$, $b$ $-7.5005$ | `um2_spectra.py` |
| three generations | tip determinant roots equal the one-generation roots to $3.0\times10^{-42}$, null vectors the columns of $\kappa$ to $1.1\times10^{-16}$; general complex tip matrix: singular values to $3.5\times10^{-5}$ | `um2_flavour.py` |
| mixing | PMNS ($\theta_{12} = 33.71^\circ$, $\theta_{13} = 8.56^\circ$, $\theta_{23} = 43.28^\circ$, $\delta = 212^\circ$) unitary to $1.1\times10^{-16}$, $J = -0.01777$; CKM $J = 3.117\times10^{-5}$; Kaluza-Klein gauge overlaps $0.14434$ (leptons), $-0.30066$ (quarks), off-diagonal $1.0\times10^{-17}$; $\mathrm{BR}(\mu\to e\gamma) = 2.8\times10^{-55}$ | `um2_flavour.py` |
| neutrino masses | $1.000$, $8.712$, $50.140$ meV; $\sum m_\nu = 0.0599$ eV | `um2_spectra.py`, `um2_neutrino.py` |
| flavour conversion | 1-3 MSW resonance $11.135$ GeV (exact $11.133$ GeV) at $2.8$ g/cm$^3$; solar 1-2 resonance $1.93$ MeV; $P(\nu_\mu\to\nu_e)$: T2K $0.0517$, NOvA $0.0481$, DUNE $0.0701$ (antineutrinos $0.0313$, $0.0236$, $0.0195$); solar $P_{ee}$ from $0.5408$ (pp) to $0.3043$ ($^8$B, 15 MeV) | `um2_neutrino.py` |
| early Universe | oscillation onset $T = 4.99$ MeV (atmospheric), $2.39$ MeV (solar); $N_{eff} = 3.0476$ (separate temperatures), $3.0485$ (common); adopted $3.0432$ | `um2_neutrino.py` |
| CNB | $T_\nu = 1.9454$ K, $112.0$ cm$^{-3}$ per mass state, $\langle v\rangle = 0.435$, $0.0604$, $0.0105$; $\Omega_\nu h^2 = 6.382\times10^{-4}$ | `um2_neutrino.py` |
| supernovae | H resonance (20 MeV) at $1573$ g/cm$^3$, $\gamma = 178$; $P_{ee} = 0.02215$, $\bar P_{ee} = 0.677$; fast instability growth $0.0877\mu$ and $0.0979\mu$, e-folding $5.9\times10^{-10}$ to $5.9\times10^{-11}$ s; heating factors $0.884$, $0.760$ | `um2_neutrino.py` |
| dirac16complex at $f_*$ | $c_\psi = 0.646667$; $\varepsilon_{DM} = 3.102204\,m$ ($p = 2.93661\,m$); even bulk $4.959981\,m$; $x_0$-momentum fraction $0.896$ | `um2_ks_jobs.py spectrum` |
| dark matter | $M_{DM} = 44.35$ TeV (both halves); $w = 0$; $p_0/\rho = 0.772034343$ $= -d\ln\varepsilon_{DM}/d\ln f$ | `um2_ks_jobs.py darkmatter` |
| portal responses $d\varepsilon_{odd}/de$ | I11 electron $0.824779$, up quark $4.328803$, neutrino $1.252406$; I12 gluon condensate $0.707196$ | `um2_ks_jobs.py portals` |
| tip $Z$ portal (removed) | $N_\nu = 3 + 2r^2$, $r^2 < 0.0056$; at the bound decoupling at $14.7$ MeV and $\Delta N_{eff} = 2.02$; oriented part $\Delta N_{eff} = 0.0958$ to $0.1257$ | `um2_electroweak.py` |
| $Z$ widths | invisible $497.7$ MeV (measured $499.1$), total $2422.3$ MeV tree level, $2485.2$ MeV with $1 + \alpha_s/\pi$ (measured $2495.5$); $R_\ell = 20.83$ (measured $20.77$) | `um2_electroweak.py` |
| primordial era | separatrix $k_c = 2.6983, 2.5991, 2.5301$; deflation factor up to $2.9166$; radion $3.3868H$ measured | `um2_primordial.py` |
| cosmology | UM-2: $H_0 = 67.37$ km/s/Mpc, $\Omega_m = 0.3151$, $r_{drag} = 147.109$ Mpc, BAO $\chi^2 = 31.72$ (13 points; $\Lambda$CDM $32.55$), TT/EE within $2.8\times10^{-4}$ of $\Lambda$CDM | `um2_cosmology.py` |
| relic | two species, $x_f = 30.38$, $g_* = 105.75$, required $\langle\sigma v\rangle = 2.01\times10^{-25}$ cm$^3$/s per species, $(8G_g^2 + 3G_W^2 + G_B^2)^{1/2} = (15.5\ \text{TeV})^{-3}$; the $^3P_0$ unitarity bound $\sqrt{\pi x_f}/M^2 = 5.79\times10^{-26}$ cm$^3$/s is exceeded 3.47 times ($v_c = 0.263$, 79 % of the pairs above it): relic OPEN | `um2_analysis.py` |
| direct detection | $\sigma_{SI} = 6.3\times10^{-53}$ cm$^2$ (gluon-only) against $2.4\times10^{-45}$ cm$^2$ | `um2_analysis.py` |
| dark energy | condensate tuned to $w_0 = -1$: $w_a = -6$, energy zero at $z = 0.260$; vacuum-energy ratio $5.5\times10^{64}$; $(H_0/H)^2 = 1.0\times10^{-92}$ | `um2_analysis.py` |
| uncertainty relation | $m/m_H$: first KK $7.49$, first odd $6.47$, dark matter $2.29$, $W^\pm$ $1.14\times10^{-3}$, $Z$ $1.29\times10^{-3}$, top quark $3.2\times10^{-3}$, electron $5.5\times10^{-9}$, $\nu_1$ $1.1\times10^{-17}$; $\langle p^2\rangle\Delta\xi^2$: photon zero mode $0.497$, $\Psi$ fold zero mode $0.097$ ($\varrho(\text{tip}) = 0.489$); $\sqrt{\langle p^2\rangle}\Delta\xi \ge (1 - \varrho(\text{tip}))/2$ for every tabulated state | `um2_analysis.py` |
| sensitivities $d\ln X/d\ln f$ | KK $-1$, $m_W$ $-0.501$, fermions from $-6.8$ ($t$) to $-41.0$ ($\nu_1$), $m_e$ $-20.5$, $M_{DM}$ $-0.772$, $\alpha$ and the gauge couplings $-4$, $G_N$ $+2.05$; splittings $\Delta m^2_{21}$ $-77.5$, $\Delta m^2_{31}$ $-74.0$ | `um2_analysis.py` |
| block rate today (ESTIMATE) | $\lvert h\rvert < 3.6\times10^{-8}H_0$ (from $\lvert\dot\alpha/\alpha\rvert < 10^{-17}$/yr), $< 7.1\times10^{-4}H_0$ (from $\lvert\dot G/G\rvert < 10^{-13}$/yr) | `um2_analysis.py` |
| radion decay (ESTIMATE) | $\Gamma = C_r\,m_r^3/(4\pi\bar M_{Pl}^2)$, $T_{RH} = (90/(\pi^2g_*))^{1/4}\sqrt{\Gamma\bar M_{Pl}}$ ($g_* = 10.75$): $\tau = 0.43\,\text{s}/C_r$, $T_{RH} = 1.85\sqrt{C_r}$ MeV ($< 4.7$ MeV unless $C_r > 6.5$) | `um2_analysis.py` |
| first-order block response | $s_{h3} = 0.028666$, $s_{hp} = 0.037320$, $q_h = -0.009555$; adiabatic $\delta k = (-0.1076\,\kappa\delta p_3 - 0.1400\,\kappa\delta\bar p + 0.0359\,\kappa\delta\rho)/H^2$ | `um2_background.py` |

## Methods, with the equations they use

* **Exact checks.** Symbolic identities are verified with sympy by simplifying the difference to zero; matrix identities
  entry by entry.
* **Curvature and Lovelock tensors.** For the order-0 metric the Riemann tensor is pair-diagonal, $R^{ab}{}_{cd} = 0$ unless
  $\{a, b\} = \{c, d\}$, with the sectional curvatures $K_{ab} = R^{ab}{}_{ab}$ ($i, j \in \{1, 2, 3\}$; $B, B' \in \{0, 5, 6, 7\}$; $A = \dot a_4$, $h = \dot f/f$, $k = 1/f^2$)
  $$ K_{ij} = A^2,\quad K_{i4} = A^2 + \dot A,\quad K_{iB} = A h,\quad K_{4B} = h^2 + \dot h,\quad K_{BB'} = h^2 - H^2 k, $$
  and the Lovelock densities and tensors follow from the pairing formula
  $$ \mathcal L_{(k)} = 2^k k! \sum_{\text{k disjoint pairs}}\ \prod_{\text{pairs}} K_{ab}, \qquad
     E_{(k)}{}^h{}_h = -2^{k-1} k!\!\!\sum_{\text{k disjoint pairs avoiding } h}\ \prod_{\text{pairs}} K_{ab}, $$
  checked against the Einstein tensor from the Ricci tensor ($k = 1$), the explicit Gauss-Bonnet tensor ($k = 2$), the Bianchi identity
  $\nabla_ME_{(k)}{}^M{}_N = 0$ and the Euler-Lagrange equations of the action with a lapse ($k = 1, 2, 3$).
* **Boson eigenvalues.** With $\xi = y/L$, $u = e^{-3\eta\xi/2}\tilde u$, $q^2 = \Lambda - 9\eta^2/4$, the operator
  $-e^{-3\eta\xi}(e^{3\eta\xi}u')' = \Lambda u$ with $u'(0) = 0$ (even) or $u(0) = 0$ (odd) and $u'(-1) = \beta u(-1)$ has the
  eigenvalue conditions
  $\big[q^2 + \tfrac{3\eta}{2}(\beta + \tfrac{3\eta}{2})\big]\sin q - \beta q\cos q = 0$ (even) and
  $q\cos q + (\beta + \tfrac{3\eta}{2})\sin q = 0$ (odd), solved with mpmath at 30 digits. Cross-check: quadratic finite
  elements for $\int e^{3\eta\xi}u'^2d\xi + \beta e^{-3\eta}u(-1)^2 = \Lambda\int e^{3\eta\xi}u^2d\xi$ on 100, 200, 400 elements, the
  eigenvalue taken from the Rayleigh quotient of the gradient form and extrapolated by Richardson.
* **Richardson extrapolation.** For a quantity with error $C\,n^{-p}$: $x \approx x_{2n} + (x_{2n} - x_n)/(2^p - 1)$; the
  observed order is $\log_2[(x_n - x_{2n})/(x_{2n} - x_{4n})]$.
* **Fermion eigenvalues.** The exact condition
  $D(e) = e^2s_Ls_R - \kappa_f^2(C_L - c_Ls_L)(C_R + c_Rs_R)$, $s = \sinh w/w$, $C = \cosh w$, $w = \sqrt{c^2 - e^2}$, solved
  with mpmath; the first-order solution $e = \kappa_f\zeta(c_L)\zeta(-c_R)$, $\zeta(c)^2 = c\,e^{-c}/\sinh c$ ($c_L > 0$, $c_R < 0$); cross-check by
  direct integration of the coupled $(L, R)$ Dirac system (DOP853, relative tolerance $10^{-13}$). With the doublet value fixed
  by the heaviest member of a sector ($c_R = -c_L$ for $\tau$ and $t$), each lighter $c_R$ is found by root finding on the mass.
* **Three generations.** With the boundary values $(a_L, b_L) = (C_L - c_Ls_L, -s_Le)$, $(a_R, b_R) = (s_Re, C_R + c_Rs_R)$ at the tip,
  the conditions $b_L = \kappa b_R$, $a_R = -\kappa^\dagger a_L$ give the $3\times3$ problem
  $\big[\mathrm{diag}(b_{L\alpha}) + \kappa\,\mathrm{diag}(b_{Ri}/a_{Ri})\,\kappa^\dagger\,\mathrm{diag}(a_{L\alpha})\big]\mathcal A = 0$, whose determinant is evaluated with mpmath at
  50 digits and whose roots are found by the Illinois (modified regula falsi) method in a $\pm2$ % bracket around the one-generation
  roots; the null vectors (right singular vectors of the smallest singular value) are compared with the columns of $\kappa$. For a non-unitary random tip matrix the masses are compared with the singular values of
  $\zeta(c_L)\,\kappa\,\mathrm{diag}(\zeta(-c_{Ri}))$.
* **Flavour evolution.** With $\mathcal H = U\,\mathrm{diag}(m_1^2, m_2^2, m_3^2)\,U^\dagger/(2E) + \mathrm{diag}(V_{CC}, 0, 0)$, $S = e^{-i\mathcal HL}$ by diagonalisation of the
  Hermitian $\mathcal H$ for constant density and $P(\nu_\alpha\to\nu_\beta) = \lvert S_{\beta\alpha}\rvert^2$; the ordered product of layer operators (20000 and
  40000 layers) through the Sun with $n_e(r) = N_A\min(245\,e^{-10.54\,r/R_\odot}, 100)$ cm$^{-3}$, followed by the incoherent sum
  $P_{ee} = \sum_i\lvert U_{ei}\rvert^2P(\nu_i)$, compared with the adiabatic formula
  $$ P_{ee} = c_{13}^4\Big(\frac12 + \frac12\cos2\theta_{12}\cos2\theta^m_{12}(r_0)\Big) + s_{13}^4,$$
  $$ \cos2\theta^m_{12} = \frac{\cos2\theta_{12} - A}{\sqrt{(\cos2\theta_{12} - A)^2 + \sin^22\theta_{12}}},\qquad A = \frac{2EV_{CC}(r_0)c_{13}^2}{\Delta m^2_{21}} $$
  ($r_0$ the production radius); the 1-3 resonance condition $2EV_{CC} = \Delta m^2_{ee}\cos2\theta_{13}$, $\Delta m^2_{ee} = c_{12}^2\Delta m^2_{31} + s_{12}^2\Delta m^2_{32}$,
  against the exact three-flavour resonance $\lvert U^m_{e3}\rvert^2 = 1/2$ found by Brent's method; the onset of oscillations in the early Universe
  where the thermal potential of the $e^\pm$ plasma,
  $$ V_e - V_\mu = -\frac{8\sqrt2\,G_Fp}{3m_W^2}\,\frac{7\pi^2}{60}T^4 , $$
  falls below $\Delta m^2\cos2\theta/(2p)$ at the mean momentum $p = 3.15T$.
* **Supernovae.** In the envelope $\rho(r) = 10^4\,(10^9\,\text{cm}/r)^3$ g/cm$^3$, $Y_e = 0.5$, a two-flavour resonance ($\Delta m^2_{31}$, $\theta_{13}$ for H;
  $\Delta m^2_{21}$, $\theta_{12}$ for L) lies at $n_e = \Delta m^2\cos2\theta/(2\sqrt2\,G_FE)$, where $d\ln n_e/dr = -3/r$; its adiabaticity and jump probability are
  $$ \gamma = \frac{\Delta m^2\sin^22\theta}{2E\cos2\theta\,\lvert d\ln n_e/dr\rvert},\qquad P_{LZ} = e^{-\pi\gamma/2} ;$$
  with both resonances adiabatic (normal ordering) a $\nu_e$ leaves the star as $\nu_3$, $P(\nu_e\to\nu_e) = \lvert U_{e3}\rvert^2$, and an $\bar\nu_e$ as $\bar\nu_1$,
  $\bar P(\bar\nu_e\to\bar\nu_e) = \lvert U_{e1}\rvert^2$; the observed mean energies are
  $\langle E\rangle_{\nu_e} = [PN_e\langle E\rangle_e + (1 - P)N_x\langle E\rangle_x]/[PN_e + (1 - P)N_x]$ (and the same with $\bar P$, $N_{\bar e}$, $\langle E\rangle_{\bar e}$ for $\bar\nu_e$) with
  $N \propto L/\langle E\rangle$; the schematic charged-current heating $q \propto N_e\langle E^2\rangle_e + N_{\bar e}\langle E^2\rangle_{\bar e}$, $\langle E^2\rangle = \frac54\langle E\rangle^2$, becomes
  $q' = \frac13(N_e\langle E^2\rangle_e + 2N_x\langle E^2\rangle_x) + \frac13(N_{\bar e}\langle E^2\rangle_{\bar e} + 2N_x\langle E^2\rangle_x)$ under three-flavour equipartition and
  $q'' = (1 - \Delta/N_e)N_e\langle E^2\rangle_e + (1 - \Delta/N_{\bar e})N_{\bar e}\langle E^2\rangle_{\bar e}$, $\Delta = \frac23(N_{\bar e} - N_x)$, under pair conversion.
* **Neutrino decoupling.** The temperature equations of Escudero (MeV units; $H = \sqrt{8\pi\rho/3}/M_{Pl}$ the Hubble rate of the total density,
  $M_{Pl} = 1.22091\times10^{19}$ GeV)
  $$ \frac{dT_\gamma}{dx_4} = -\frac{4H\rho_\gamma + 3H(\rho_e + p_e) + 3HT_\gamma\frac{dP_{int}}{dT_\gamma} + \frac{\delta\rho_{\nu_e}}{\delta x_4} + 2\frac{\delta\rho_{\nu_\mu}}{\delta x_4}}
     {\frac{d\rho_\gamma}{dT_\gamma} + \frac{d\rho_e}{dT_\gamma} + T_\gamma\frac{d^2P_{int}}{dT_\gamma^2}},\qquad
     \frac{dT_{\nu_\alpha}}{dx_4} = -HT_{\nu_\alpha} + \frac{\delta\rho_{\nu_\alpha}/\delta x_4}{d\rho_{\nu_\alpha}/dT_{\nu_\alpha}}, $$
  $$ \frac{\delta\rho_{\nu_e}}{\delta x_4} = \frac{G_F^2}{\pi^5}\Big[4(g_{eL}^2 + g_{eR}^2)F(T_\gamma, T_{\nu_e}) + 2F(T_{\nu_\mu}, T_{\nu_e})\Big],\qquad
     \frac{\delta\rho_{\nu_\mu}}{\delta x_4} = \frac{G_F^2}{\pi^5}\Big[4(g_{\mu L}^2 + g_{\mu R}^2)F(T_\gamma, T_{\nu_\mu}) - F(T_{\nu_\mu}, T_{\nu_e})\Big], $$
  $$ F(T_1, T_2) = 32f_a(T_1^9 - T_2^9) + 56f_sT_1^4T_2^4(T_1 - T_2),\qquad f_a = 0.884,\quad f_s = 0.829, $$
  with $\rho_\gamma = \pi^2T_\gamma^4/15$, $\rho_{\nu_\alpha} = 7\pi^2T_{\nu_\alpha}^4/120$ per flavour ($\nu_\tau$ as $\nu_\mu$), the $e^\pm$ density and pressure with the electron
  mass, the effective couplings $g_{eL} = 0.727$, $g_{eR} = 0.233$, $g_{\mu L} = -0.273$, $g_{\mu R} = 0.233$ (or the UM-2 tree-level couplings
  $\frac12 + s^2$, $s^2$, $-\frac12 + s^2$, $s^2$, $s^2 = 0.22363$), and the QED interaction pressure $P_{int} = P_2 + P_3$,
  $$ P_2 = -\frac{e^2T^2}{12\pi^2}J_1 - \frac{e^2}{8\pi^4}J_1^2 + \frac{e^2m_e^2}{16\pi^4}J_2,\qquad P_3 = \frac{e^3T}{12\pi^4}I^{3/2},\qquad \rho_{int} = -P_{int} + T\frac{dP_{int}}{dT}, $$
  $$ J_1 = \int_0^\infty dp\,\frac{p^2}{E}n_D,\qquad J_2 = \int_0^\infty\!\!\int_0^\infty dp\,dq\,\frac{pq}{E_pE_q}\ln\Big\lvert\frac{p + q}{p - q}\Big\rvert n_D(p)n_D(q),\qquad
     I = \int_0^\infty dp\,\frac{p^2 + E^2}{E}n_D, $$
  $n_D = 2/(e^{E/T} + 1)$, $E = \sqrt{p^2 + m_e^2}$.
  The integrals are evaluated with Gauss-Legendre panels, the logarithmic singularity of $J_2$ removed by $q = p(1 - s^2)$; LSODA from
  20 MeV to 5 keV (relative tolerance $10^{-11}$);
  $$ N_{eff} = \Big(\frac{11}{4}\Big)^{4/3}\Big[\Big(\frac{T_{\nu_e}}{T_\gamma}\Big)^4 + 2\Big(\frac{T_{\nu_\mu}}{T_\gamma}\Big)^4\Big] ;$$
  for instantaneous decoupling the plasma entropy $a^3(\rho + p)/T$ is conserved and $T_\nu \propto 1/a$.
* **Cosmic neutrino background.** The three mass states with the Fermi-Dirac spectrum $f = 1/(e^{p/T_\nu} + 1)$:
  $$ T_\nu = \Big(\frac{4}{11}\Big)^{1/3}T_{CMB},\qquad n_i = \frac{3\zeta(3)}{2\pi^2}T_\nu^3\ (\nu_i + \bar\nu_i),\qquad
     \rho_i = 2\int\frac{d^3p}{(2\pi)^3}\sqrt{p^2 + m_i^2}\,f,\qquad \Omega_\nu h^2 = \frac{\sum_i\rho_i}{\rho_c/h^2}, $$
  $\rho_c/h^2 = 1.05368\times10^4$ eV/cm$^3$, and the mean velocity $\langle v\rangle = \int p^2(p/E)f\,dp/\!\int p^2f\,dp$, $E = \sqrt{p^2 + m_i^2}$.
* **Dark radiation of a thermalised species.** A species of $n_W$ Weyl fermions decoupled when the entropy degrees of freedom were $g_s$ adds
  $$ \Delta N_{eff} = n_W\Big(\frac{10.75}{g_s}\Big)^{4/3}F_h,\qquad F_h = \Big[\frac{T_\nu}{T_\gamma}\Big(\frac{11}{4}\Big)^{1/3}\Big/(1 + h_\nu)\Big]^4 = 1.0095 ,$$
  with the computed $T_\nu/T_\gamma = 0.71664$ and comoving heating $h_\nu = 0.00165$ of the common-temperature decoupling ($F_h$ corrects for the
  heating of the neutrinos by $e^+e^-$ annihilation that an earlier-decoupled species does not receive).
* **Fast flavour instability.** With the electron-lepton-number distribution $G(u) = \sqrt2G_F[n_{\nu_e}g_{\nu_e}(u) - n_{\bar\nu_e}g_{\bar\nu_e}(u)]$ over the
  direction cosine $u$ (in units of $\mu = \sqrt2G_Fn_{\nu_e}$; $\alpha = n_{\bar\nu_e}/n_{\nu_e}$), modes $e^{-i(\Omega x_4 - Kx_3)}$ along the symmetry axis $x_3$,
  $v = (1, u)$, $\Lambda^\mu = \int du/2\,G\,v^\mu$, $\omega = \Omega - \Lambda^0$, $k = K - \Lambda^3$ and $\eta^{\mu\nu} = \mathrm{diag}(1, -1)$ on $(x_4, x_3)$, the dispersion relation
  $$ \det\Pi = 0,\qquad \Pi^{\mu\nu} = \eta^{\mu\nu} + \int_{-1}^{1}\frac{du}{2}\,G(u)\,\frac{v^\mu v^\nu}{\omega - ku} $$
  has the axisymmetric branch $(1 + J_0)(-1 + J_2) - J_1^2 = 0$, $J_n = \int du/2\,G\,u^n/(\omega - ku)$, and the azimuthal branch
  $-1 + \int du/2\,G(1 - u^2)/(2(\omega - ku)) = 0$; it is solved for real $k$ by vectorised Newton iterations with the analytic derivative from a grid
  of complex starting points; cross-checks against the analytic growth $\frac12\sqrt{4I_1^2 - (I_0 + I_2)^2}$ ($I_n = \int du/2\,G\,u^n$) of the mode $K = \Lambda^3$
  and the eigenvalues of the discretised homogeneous equations
  $i\,dS_u/dx_4 = (\Lambda^0 - u\Lambda^3)S_u - \int du'/2\,G(u')(1 - uu')S_{u'}$ (300 nodes).
* **Kohn-Sham.** The orbitals $h_j\chi_o = \varepsilon_o\chi_o$ (fold $\chi_2(0) = 0$ even or $\chi_1(0) = 0$ odd, tip $\chi_2(-L) = 0$) build the densities
  $$ n = \sum_o w\,g\,f_o\,n_o,\quad S = \sum_o w\,g\,f_o\,s_o,\qquad n_o = P\chi_o^\dagger\chi_o,\quad s_o = P\chi_o^\dagger j\sigma_2\chi_o,\quad t_o = P\chi_o^\dagger j\sigma_3\chi_o,
     \quad P = \frac{e^{-3Hy}}{\mathrm{Vol}_7},$$
  ($w = 1/2$ per fold parity, $g = 4r_3(\lvert\vec n\rvert^2)$ the degeneracy of the momentum shell $\vec k = \Delta k\,\vec n$, $r_3$ the number of
  representations as a sum of three squares, $f_o$ the occupations), the energy and the energy-momentum tensor
  $$ E_{KS} = \sum_o g\,f_o\,\varepsilon_o - 2\,\mathrm{Vol}_7\int_{-L}^0e^{3Hy}e_{int}\,dy,\qquad e_{int} = \frac{15}{32}\lambda S^2 - \frac{1}{32}\lambda n^2,$$
  $$ \rho = \sum_o wgf_o\varepsilon_o\,n_o - e_{int},\qquad p_3 = \sum_o wgf_o\,\frac{e^{-a_4}\lvert k\rvert}{3}t_o + e_{int},\qquad p_t = e_{int},$$
  $$ p_0 = \sum_o wgf_o\big[(\varepsilon_o - v)n_o - M_{eff}s_o - e^{-a_4}\lvert k\rvert t_o\big] + e_{int} ,$$
  Orbitals of $h_j$ are expanded in the exact eigenfunctions of the free problem of each sector
  (60, 120 or 240 functions, quadrature with ten points per function), the mean fields
  $M_{eff} = m + \tfrac{15}{16}\lambda S$, $v = -\tfrac{1}{16}\lambda n$ (plus the portal mean fields $\langle\mathcal F\rangle/\Lambda_\star^3$ of I12 and
  $(c_V/\Lambda_\star^6)\sum_i\sum_\psi q_\psi n_{\psi i}$ of I11 where stated) are iterated to self-consistency (tolerance $10^{-13}$)
  with a safeguarded Anderson mixing and a fixed labelling of the occupied set; checks: the energy identity
  $E_{KS} = 2\,\mathrm{Vol}_7\int_{-L}^0e^{3Hy}\rho\,dy$, the $y$-conservation law
  $\big[e^{3Hy}p_0\big]_{-L}^{0} = 3H\int_{-L}^0e^{3Hy}p_t\,dy$, Richardson in the basis size, the Hellmann-Feynman theorem
  $d\varepsilon/de = \langle\chi\vert\partial h/\partial e\vert\chi\rangle$ for every portal mean field, and the reproduction of the
  record's two reference states to $10^{-13}$ (energies, HOMO, LUMO) and $10^{-9}$ (integrated hidden pressure). The portal sources
  are the zero-mode densities $\varrho_c(y) = (2c/L)e^{2cy/L}/(1 - e^{-2c})$: the electron $\frac12(\varrho_{c_L} + \varrho_{-c_R(e)})$, the up quark
  $\frac12(\varrho_{c_Q} + \varrho_{-c_R(u)})$, the neutrino $\varrho_{c_L}$.
* **Primordial era.** The three independent components of the field equations of the order-0 metric with the author's weights and
  $\Lambda = -10H^2$ (from the pairing formula and the sectional curvatures above; $\rho$, $p_3$ and $\bar p = (p_0 + 3p_t)/4$ the source)
  $$ \begin{aligned} x_4:\quad &- \frac{15 A^{2} h^{4}}{16 H^{4}} - \frac{5 A^{3} h^{3}}{4 H^{4}} - \frac{3 h^{4}}{8 H^{2}} - \frac{9 A h^{3}}{2 H^{2}} - \frac{27 A^{2} h^{2}}{4 H^{2}} + \frac{9 k A^{2} h^{2}}{8 H^{2}} \\
     &- \frac{3 h A^{3}}{2 H^{2}} + \frac{3 h k A^{3}}{4 H^{2}} - 6 h^{2} + \frac{3 k h^{2}}{4} - 12 A h + \frac{9 A h k}{2} \\
     &- 3 A^{2} + \frac{9 k A^{2}}{4} - \frac{3 A^{2} k^{2}}{16} - 10 H^{2} + 6 k H^{2} - \frac{3 H^{2} k^{2}}{8} \\
     &= -\kappa\rho \end{aligned} $$
  $$ \begin{aligned} x_1:\quad &\Big[- \frac{h^{4}}{8 H^{4}} - \frac{A h^{3}}{2 H^{4}} - \frac{3 h^{2}}{2 H^{2}} + \frac{k h^{2}}{4 H^{2}} - \frac{A h}{H^{2}} + \frac{A h k}{2 H^{2}} \\
     &\quad -2 + \frac{3 k}{2} - \frac{k^{2}}{8}\Big]\,\dot A \\
     &+ \Big[- \frac{A h^{3}}{2 H^{4}} - \frac{3 A^{2} h^{2}}{4 H^{4}} - \frac{3 h^{2}}{2 H^{2}} - \frac{3 A h}{H^{2}} + \frac{A h k}{2 H^{2}} - \frac{A^{2}}{2 H^{2}} \\
     &\quad + \frac{k A^{2}}{4 H^{2}} - 4 + \frac{3 k}{2}\Big]\,\dot h \\
     &- \frac{A h^{5}}{2 H^{4}} - \frac{19 A^{2} h^{4}}{16 H^{4}} - \frac{A^{3} h^{3}}{2 H^{4}} - \frac{15 h^{4}}{8 H^{2}} - \frac{6 A h^{3}}{H^{2}} + \frac{A k h^{3}}{2 H^{2}} \\
     &- \frac{17 A^{2} h^{2}}{4 H^{2}} + \frac{7 k A^{2} h^{2}}{8 H^{2}} - \frac{h A^{3}}{H^{2}} + \frac{h k A^{3}}{2 H^{2}} - 10 h^{2} + \frac{9 k h^{2}}{4} \\
     &- 8 A h + 3 A h k - 3 A^{2} + \frac{9 k A^{2}}{4} - \frac{3 A^{2} k^{2}}{16} - 10 H^{2} \\
     &+ 6 k H^{2} - \frac{3 H^{2} k^{2}}{8} \\
     &= \kappa p_3 \end{aligned} $$
  $$ \begin{aligned} x_0:\quad &\Big[- \frac{3 A h^{3}}{8 H^{4}} - \frac{9 A^{2} h^{2}}{16 H^{4}} - \frac{9 h^{2}}{8 H^{2}} - \frac{9 A h}{4 H^{2}} + \frac{3 A h k}{8 H^{2}} - \frac{3 A^{2}}{8 H^{2}} \\
     &\quad + \frac{3 k A^{2}}{16 H^{2}} - 3 + \frac{9 k}{8}\Big]\,\dot A \\
     &+ \Big[- \frac{9 A^{2} h^{2}}{16 H^{4}} - \frac{3 h A^{3}}{8 H^{4}} - \frac{3 h^{2}}{8 H^{2}} - \frac{9 A h}{4 H^{2}} - \frac{9 A^{2}}{8 H^{2}} + \frac{3 k A^{2}}{16 H^{2}} \\
     &\quad -3 + \frac{3 k}{8}\Big]\,\dot h \\
     &- \frac{9 A^{2} h^{4}}{16 H^{4}} - \frac{17 A^{3} h^{3}}{16 H^{4}} - \frac{9 A^{4} h^{2}}{16 H^{4}} - \frac{3 h^{4}}{8 H^{2}} - \frac{27 A h^{3}}{8 H^{2}} - \frac{45 A^{2} h^{2}}{8 H^{2}} \\
     &+ \frac{3 k A^{2} h^{2}}{16 H^{2}} - \frac{27 h A^{3}}{8 H^{2}} + \frac{9 h k A^{3}}{16 H^{2}} - \frac{3 A^{4}}{8 H^{2}} + \frac{3 k A^{4}}{16 H^{2}} - 6 h^{2} \\
     &+ \frac{3 k h^{2}}{8} - 9 A h + \frac{9 A h k}{8} - 6 A^{2} + \frac{9 k A^{2}}{4} - 10 H^{2} \\
     &+ 3 k H^{2} \\
     &= \kappa\bar p \end{aligned} $$
  are solved for $\dot A$, $\dot h$ (the 3-space and block components are linear in them), with $\dot k = -2kh$ and the stabiliser
  $\kappa\rho_b = \kappa\rho_b^*(k/k_*)^4$, $p_3 = -\rho_b$, $\bar p = \rho_b$ (plus radiation where stated); the $x_4$ constraint fixes the initial $A$ and is
  monitored (residual below $6\times10^{-10}$); the separatrix is found by bisection in the initial $k$.
* **Cosmology.** The linear perturbations obey the Einstein-Boltzmann equations (Newtonian gauge, conformal time $\tau$ with
  $dx_4 = a\,d\tau$, $\mathcal H = a'/a$, $ds^2 = a^2[-(1 + 2\psi)d\tau^2 + (1 - 2\phi)d\vec x^{\,2}]$, a Fourier mode $k$; Ma and Bertschinger)
  $$ k^2\phi + 3\mathcal H(\phi' + \mathcal H\psi) = -4\pi G_Na^2\delta\rho,\qquad k^2(\phi' + \mathcal H\psi) = 4\pi G_Na^2(\bar\rho + \bar P)\theta,$$
  $$ \phi'' + \mathcal H(\psi' + 2\phi') + (2\mathcal H' + \mathcal H^2)\psi + \frac{k^2}{3}(\phi - \psi) = 4\pi G_Na^2\delta P,\qquad k^2(\phi - \psi) = 12\pi G_Na^2(\bar\rho + \bar P)\sigma,$$
  with the cold dark matter $\delta_c' = -\theta_c + 3\phi'$, $\theta_c' = -\mathcal H\theta_c + k^2\psi$; the baryons and photons coupled by Thomson
  scattering ($n_e$ the free-electron density, $\sigma_T$ the Thomson cross-section, $R = 4\bar\rho_\gamma/(3\bar\rho_b)$, $c_s$ the baryon sound speed,
  $F_{\gamma l}$ and $G_{\gamma l}$ the temperature and polarisation multipoles, $F_{\gamma2} = 2\sigma_\gamma$),
  $$ \delta_b' = -\theta_b + 3\phi',\qquad \theta_b' = -\mathcal H\theta_b + c_s^2k^2\delta_b + R\,an_e\sigma_T(\theta_\gamma - \theta_b) + k^2\psi, $$
  $$ \delta_\gamma' = -\tfrac43\theta_\gamma + 4\phi',\qquad \theta_\gamma' = k^2\big(\tfrac14\delta_\gamma - \sigma_\gamma\big) + k^2\psi + an_e\sigma_T(\theta_b - \theta_\gamma), $$
  $$ F_{\gamma l}' = \frac{k}{2l + 1}\big[lF_{\gamma(l-1)} - (l + 1)F_{\gamma(l+1)}\big] - an_e\sigma_T\Big[F_{\gamma l} - \frac{\delta_{l2}}{10}\big(F_{\gamma2} + G_{\gamma0} + G_{\gamma2}\big)\Big]\quad (l \ge 2),$$
  $$ G_{\gamma l}' = \frac{k}{2l + 1}\big[lG_{\gamma(l-1)} - (l + 1)G_{\gamma(l+1)}\big] + an_e\sigma_T\Big[-G_{\gamma l} + \frac12\big(F_{\gamma2} + G_{\gamma0} + G_{\gamma2}\big)\Big(\delta_{l0} + \frac{\delta_{l2}}{5}\Big)\Big] ;$$
  and one massive hierarchy per neutrino mass state $i$ (comoving momentum $q$, energy $E_i = \sqrt{q^2 + a^2m_i^2}$,
  multipoles $\mathcal N^{(i)}_l$ of the perturbed Fermi-Dirac distribution $\bar f_\nu$):
  $\mathcal N^{(i)\prime}_0 = -\frac{qk}{E_i}\mathcal N^{(i)}_1 - \phi'\frac{d\ln\bar f_\nu}{d\ln q}$,
  $\mathcal N^{(i)\prime}_1 = \frac{qk}{3E_i}(\mathcal N^{(i)}_0 - 2\mathcal N^{(i)}_2) - \frac{E_ik}{3q}\psi\frac{d\ln\bar f_\nu}{d\ln q}$,
  $\mathcal N^{(i)\prime}_l = \frac{qk}{(2l+1)E_i}[l\mathcal N^{(i)}_{l-1} - (l+1)\mathcal N^{(i)}_{l+1}]$ ($l \ge 2$).
  CAMB 2.0.5 solves them with the Planck 2018 parameters above, $\theta_{MC}$ fixed (so $H_0$ is an output), $\ell_{max} = 2600$,
  lensing included. UM-2 has three massive eigenstates, each with the degeneracy $N_{eff}/3 = 1.0144$; CAMB gives each the density
  $\deg\times\rho_{FD}(m'; T_\nu)$, so the masses passed are $m'_i = m_i\deg^{-1/4}$; because CAMB recovers them by inverting the relativistic
  density from $\omega_\nu$ and the mass fractions, $\omega_\nu$ and the fractions are iterated (damped exponent 0.8, 13 iterations) until the
  masses agree to $7.8\times10^{-12}$. The comparison model is the CAMB default (one neutrino of $0.06$ eV, $N_{eff} = 3.044$).
* **Relic abundance.** For $\mathcal L = G\,\bar\chi\chi F_{\mu\nu}F^{\mu\nu}$ per abelian channel,
  $\sigma v = G^2s(s - 4M^2)/(4\pi) \to G^2M^4v^2/\pi$ (p-wave); in total
  $\sigma v = (M^4v^2/\pi)(8G_g^2 + 3G_W^2 + G_B^2)$, $\langle\sigma v\rangle(x) = 6b/x$ with $b = (M^4/\pi)(8G_g^2 + 3G_W^2 + G_B^2)$;
  freeze-out (Kolb and Turner, Dirac fermion, $g = 2$, $c = 1/2$):
  $x_f = \ln\big[0.038\,c(c + 2)\,g\,M_{Pl}M\langle\sigma v\rangle(x_f)/\sqrt{g_*x_f}\big]$,
  $\Omega h^2 = 2\times1.07\times10^9\,\text{GeV}^{-1}\,x_f/\big(\sqrt{g_*}\,M_{Pl}\,3b/x_f\big) = 0.060$ per species (two species), with $M_{Pl} = 1.22091\times10^{19}$ GeV and
  $g_* = 105.75$ (three generations without $\nu_R$, the gauge bosons; no Higgs; the fold bands not thermalised). Unitarity: the operator
  annihilates a pair only from $^3P_0$ ($J = 0$), so for unpolarised Dirac fermions $\sigma \le \pi/(4p^2)$, $p = Mv/2$, i.e. $\sigma v \le \pi/(M^2v)$, whose
  thermal average over $f(v) \propto v^2e^{-xv^2/4}$ is $\langle\pi/(M^2v)\rangle = \sqrt{\pi x}/M^2$ (checked by numerical averaging); the effective cross-section
  $G^2M^4v^2/\pi$, $G = (8G_g^2 + 3G_W^2 + G_B^2)^{1/2}$, exceeds the bound for $v > v_c = (\pi/(GM^3))^{2/3}$.
* **Direct detection** (ESTIMATE). Trace anomaly: $\langle N\vert G^\alpha G^\alpha\vert N\rangle = -\frac{8\pi}{9\alpha_s}m_Nf_{TG}$,
  $f_N = G_g\frac{8\pi}{9\alpha_s}m_Nf_{TG}$, $\sigma_{SI} = \mu_N^2f_N^2/\pi$ ($\mu_N$ the dark-matter-nucleon reduced mass; $f_{TG} = 0.92$, $\alpha_s = 0.3$,
  $m_N = 0.939$ GeV, $G_g = G/\sqrt8$ if the whole coupling were in gluons), against the LZ limit scaled linearly from $2.2\times10^{-48}$ cm$^2$ at 40 GeV.
* **Condensate.** A homogeneous condensate $S = \bar\Psi\Psi \propto a^{-3}$ with $U = \frac{\lambda}{2}S^2$ has $\rho = mS + U$, $p = S\,dU/dS - U = \frac{\lambda}{2}S^2$, so
  $$ w(a) = \frac{X(a)}{1 + X(a)},\qquad X(a) = \frac{\lambda S}{2m} = X_0a^{-3},\qquad X_0 = \frac{w_0}{1 - w_0},\qquad w_a \equiv -\frac{dw}{da}\Big\vert_{a=1} = \frac{3X_0}{(1 + X_0)^2},$$
  and the energy density $\rho = mS(1 + X)$ crosses zero at $a = (-X_0)^{1/3}$ when $\lambda < 0$.
* **Uncertainty relation.** For bosons, with $u = e^{-3\eta\xi/2}\tilde u$:
  $e^{3\eta\xi}u'^2 = \tilde u'^2 + \tfrac94\eta^2\tilde u^2 - \tfrac32\eta(\tilde u^2)'$, hence
  $(m\,fL)^2 = \langle p^2\rangle + \tfrac{9\eta^2}{4} - \tfrac{3\eta}{2}\varrho(\text{fold}) + (\tfrac{3\eta}{2} + \beta)\varrho(\text{tip})$ with
  $\langle p^2\rangle = \int\tilde u'^2/\!\int\tilde u^2$ and the normalised density $\varrho = \tilde u^2/\!\int\tilde u^2$ ($\varrho = \lvert\chi\rvert^2/\!\int\lvert\chi\rvert^2$ and
  $\langle p^2\rangle = \int\lvert\chi'\rvert^2/\!\int\lvert\chi\rvert^2$ for fermions); the Heisenberg estimate is $m_H = \hbar c/(2\Delta s)$ with
  $\Delta s = fL\,\Delta\xi$, $\Delta\xi^2 = \int\xi^2\varrho\,d\xi/\!\int\varrho\,d\xi$ the mean square distance from the fold. On the cell the
  relation reads $\sqrt{\langle p^2\rangle}\,\Delta\xi \ge (1 - \varrho(\text{tip}))/2$, from $1 = \varrho(\text{tip}) - \int\xi\varrho'\,d\xi$ and the
  Cauchy-Schwarz inequality (a theorem); it is also checked numerically for each of the 21 tabulated states (five boson modes,
  two doublet and twelve singlet zero modes, two states of $\Psi$).
* **$W^\pm$, $Z$ fit.** $\rho(\beta_W) - 1 = \Lambda_W(\beta_W)/[\Lambda_Z(\beta_W/\cos^2\theta_W)\cos^2\theta_W] - 1$ with
  $\cos^2\theta_W = (m_W^2/m_Z^2)/\rho_0$ is solved for $\rho - 1 = \rho_0 - 1$ by bisection in $\ln\beta_W$ (80 steps); the model's
  $m_Z = m_W\sqrt{\Lambda_Z/\Lambda_W}$ then equals the measured value to $10^{-8}$ (checked).
* **Cosmic variance.** The relative error of a single multipole is $\sqrt{2/(2\ell + 1)}$; the binned full-sky
  $\chi^2 = \sum_b(\bar\delta_b/\sigma_b)^2$ uses bins of $\Delta\ell = 50$, the mean relative deviation $\bar\delta_b$ and
  $\sigma_b = \sqrt{2/\sum_{\ell\in b}(2\ell + 1)}$.

## Corrections made during the work

1. The gauge-invariance test of the tip terms first used the wrong sign of the hypercharge phase; with
   $\psi \to e^{iY\theta}\psi$ every term is invariant to $4\times10^{-15}$.
2. The finite-element cross-check of $\Lambda_W$ was first limited by round-off; the gradient-form Rayleigh quotient with
   Richardson extrapolation (observed order 4.01) agrees with the exact value to $3\times10^{-14}$.
3. The Kohn-Sham basis convergence and the conservation law were first checked without extrapolation; Richardson in
   the basis size (observed orders 4.95 for the energy, 2.97 for the hidden pressure) was added.
4. The self-consistency loop did not converge for $N = 592$ at the record's coupling; a fixed labelling of the occupied
   set and a safeguarded Anderson mixing were introduced, the benchmark coupling $\lambda_B$ was adopted, and the
   record's coupling is kept as a stress test, which now converges.
5. A first statement that every primordial start above the unstable static block reaches the stable one was false in
   detail; the separatrix $k_c(h_0)$ was computed by bisection instead.
6. The primordial figure was first sampled too coarsely (aliasing of the radion oscillation) and is now densely sampled.
7. The sum rules of the uncertainty analysis were first imprecise for the sharp fermion zero modes; exact mpmath
   normalisation and the tip term fixed them ($10^{-8}$).
8. The radion quantity was stored under a wrong sign label; it is now stored as $\omega_r^2 = \det$ of the block Jacobian.
9. Portal names of the first universe model (P1 to P6) in two check texts were replaced by I9, I11, I12.
10. The gauge-kinetic portal was first written with the scale to the power 5, which is dimensionally wrong in the
    geometric normalisation of the gauge fields; it is $\bar\Psi\Psi\,F_{MN}F^{MN}/\Lambda_\star^3$, and the symbol of the
    portal scale was changed so that it no longer clashes with the Dirichlet bound $\Lambda_D$.
11. Before publication every number of the documents was compared with the computed outputs; four statements were
    corrected (the dark-matter momentum $p\,fL = 1.89901$, the finite-element agreement $5\times10^{-10}$, the TT and EE
    agreements of version 1, and the restriction $A = 0$ of the sourceless static block).
12. The kinetic term of the tip sigma field was first written with the sign of the signature $(+,-,-,-)$; in the
    signature $(+,+,+,-)$ of $x_1, \dots, x_4$ it is $-\frac{v_\Sigma^2}{4}\mathrm{tr}((D_\mu\Sigma)^\dagger D^\mu\Sigma)$, which gives the
    mass terms $-\frac12m^2V_\mu V^\mu$ with $m^2 > 0$ (the computations always used $m^2 > 0$).
13. With the real matrices $C\gamma^a$ antisymmetric, $\bar\Psi\gamma^a\Psi$ is anti-Hermitian; the portal currents are now
    written as the Hermitian currents $i\bar\Psi\gamma^M\Psi$ and the Standard-Model currents as $i\bar\psi\gamma^M\psi$.
14. The block response to the hidden pressure of a Kohn-Sham state first used $p_0$ alone; the common block scale is
    driven by the block-averaged pressure $\bar p = (p_0 + 3p_t)/4$, and $p_0 - p_t$ drives a block-shape mode outside the
    order-0 metric (OPEN). The linearised sourced equations were added (`um2_background.py`, 2 checks); they first
    omitted the density, which enters at first order through $3G(k_*)A^2 = \kappa\delta\rho$; with it the adiabatic response
    reproduces the four-dimensional Friedmann acceleration equation exactly.
15. The statement that $N_A$ and $N_B$ are separately conserved was first recorded as an asserted check; it is now
    computed with the author's matrices (commutators of $B$ with $C$, $\gamma^a$, $C\gamma^a$, $S^{ab}$), which also shows that
    extra-time momenta, outside the good sector, would mix the halves.
16. The radion lifetime was first quoted as an unverified estimate; it is now computed (ESTIMATE, with the coupling
    factor $C_r$ explicit), as is the bound on the block rate today.
17. Figures: the BAO legend showed the data label twice and two labels of the uncertainty figure overlapped; the
    condensate figure no longer draws the vertical lines where $w$ diverges.
18. An independent review of the five documents of version 1 against the outputs found, and the documents were corrected:
    the first-order fermion mass formula (it needs $\zeta(-c_R)$ for the singlet, $c_R < 0$; the code always used $\lvert c\rvert$); the gap
    statement, which holds for the boson operators but not for $\Psi$ (the dark matter, $44.35$ TeV, lies below the boson gap
    of $99.5$ TeV); the sensitivity of $G_N$ to the block, which is $d\ln G_N/d\ln f = -4 + 2k_*G'(k_*)/G(k_*) = +2.05$ and not
    $-4$ (recomputed; the lunar-ranging bound becomes $7.1\times10^{-4}H_0$); $\Delta N_{eff}$ of a thermalised fold band (recomputed);
    a level spacing ($0.25000$); a rounding ($1.948$); the definitions of $\bar M_{Pl}$, $M_{Pl}$, the radion formulas, $\Delta s$, the
    unitarity estimate and the cosmic-variance measure; the statement on proper and coordinate localisation; and several
    notational clashes ($\kappa = e^{-a_4}$ is now written out).
19. A second review of version 1 found, and the documents were corrected: the electroweak parameter was written
    $\rho = m_W^2/(m_Z^2\cos^2\theta_W)$ next to the on-shell definition $\cos^2\theta_W = m_W^2/m_Z^2$, which makes it identically 1; the
    computation always used $\rho = \Lambda_W/(\Lambda_Z\cos^2\theta_W)$. Checking the uncertainty relation for every state then showed
    that the bound $\langle p^2\rangle \ge 1/(4\Delta\xi^2)$ quoted for the hidden kinetic energy is not valid on the cell: the tip, where
    the cell ends, adds a boundary term, and the valid relation is $\sqrt{\langle p^2\rangle}\,\Delta\xi \ge (1 - \varrho(\text{tip}))/2$ (the broad
    fold zero mode of $\Psi$ has $\langle p^2\rangle\Delta\xi^2 = 0.097$); a computed check of it was added. Further: the $\overline{MS}$
    angle in the $Z$ widths, the shooting accuracy, the normalisation volume $\mathrm{Vol}_7$ (not the proper seven-volume), the
    occupations $f_o$, the coupling matrix $\Lambda_\ell$, and the notation (with a list of the symbols with more than one use in
    each document).
20. A third review of version 1 found, and the computations and documents were corrected: (a) the $W^\pm$, $Z$ fit set the
    angle of the gauge couplings equal to the on-shell angle of the measured masses and fitted the tree-level $\rho - 1$ to
    $\rho_0 - 1$, which put the model's $m_Z = 91.1706$ GeV $17$ MeV below the measured value; since $\rho_0$ measures the
    custodial violation beyond the Standard-Model loops, the angle of the couplings is now fixed by the measured masses,
    $\cos^2\theta_W = (m_W^2/m_Z^2)/\rho_0 = 0.776368$, and the model reproduces both masses (check `mZ_reproduced`); $\beta_W = 0.011912$
    and every scale in GeV moved by $+8.50\times10^{-4}$ ($m_{KK} = 121.32$ TeV, $H = 14.296$ TeV, gap $99.48$ TeV, radion $48.42$ TeV,
    $M_{DM} = 44.35$ TeV). The tree-level $Z$ widths with the angle of the couplings were added (check `Z_width_scheme`). (b) The
    familiar bound $\langle p^2\rangle \ge 1/(4\Delta\xi^2)$ is guaranteed only for profiles negligible at the tip. (c) Symbol lists and
    wording.
21. **Version 2 (2026-10-18): three generations and three neutrino flavours.** By the author's orders of 2026-10-18 (option A):
    (a) three generations of quarks and leptons with one doublet bulk mass per sector, the twelve masses as exact $x_0$ eigenvalues
    and the PMNS and CKM matrices as the tip matrices, proved exact for three generations (`um2_flavour.py`, new; `um2_spectra.py`,
    `um2_fields.py` extended); (b) the flavour conversion of the three neutrinos (`um2_neutrino.py`, new): vacuum, matter,
    accelerators, the Sun, the early Universe and $N_{eff}$, the CNB of three mass states, supernovae; (c) the chiral tip $Z$ portal
    I9 is removed: with three neutrinos it has no role left, its even part is bounded by the invisible width ($N_\nu = 3 + 2r^2$,
    $r^2 < 0.0056$) and would still keep the fold band in equilibrium to $14.7$ MeV ($\Delta N_{eff} = 2.02$), and its oriented part
    would thermalise the fold band through the decays of the odd $\Psi_A$ states ($\Delta N_{eff} = 0.0958$ to $0.1257$, $2.1$ to $2.4$
    standard deviations above ACT DR6); consequently both halves of $\Psi$ keep an exact fold parity and the dark matter consists of
    the lightest odd states of both halves (two species, relic recomputed: $x_f = 30.38$, $(15.5\ \text{TeV})^{-3}$); (d) the invisible
    width uses the PDG 2025 value $N_\nu = 2.9963 \pm 0.0074$ instead of the LEP 2006 value; (e) $N_{eff}$ is computed for three
    flavours ($3.0476$ to $3.0485$) and the precision value $3.0432$ (Cielo et al.) replaces $3.044$; (f) the cosmology has three massive
    neutrinos ($\sum m_\nu = 0.0599$ eV) instead of one of $0.05$ eV and no dark radiation; (g) the $Z$ widths of three generations
    ($2485.2$ MeV with the QCD factor) remove the one-generation conflict ($1232$ MeV); (h) the Kohn-Sham portal sources use the
    three-generation localisations. Errors found and corrected during the version-2 work: the 1-3 MSW resonance energy was first
    evaluated with a spurious factor $1/c_{13}^2$ ($11.49$ GeV); it is $E = \Delta m^2_{ee}\cos2\theta_{13}/(2V_{CC}) = 11.135$ GeV with
    $\Delta m^2_{ee} = c_{12}^2\Delta m^2_{31} + s_{12}^2\Delta m^2_{32}$, confirmed by the exact three-flavour root $11.133$ GeV (now a check); CAMB's
    built-in normal-hierarchy option put the mass in one eigenstate, so the three eigenstates are now set up explicitly with the
    iteration described in the methods; a check of the analysis (fermions below the uncertainty estimate) first used a threshold
    that the muon and the strange quark exceed and now tests the documented statement ($m/m_H < 0.01$ for every fermion); in the
    documents the muon eigenvalue ($4.7795\times10^{-6}$), the Landau-Zener bound ($P_{LZ} \le 2.6\times10^{-77}$) and the explanation of
    $\Omega_\nu h^2$ (the non-relativistic coefficient $94.06$ eV at the instantaneous-decoupling temperature, $93.14$ eV with the heating)
    were corrected; the published values of the decoupling method were read from the source (Escudero 2020, Table 1) and the
    separate-temperature value $3.048$ added to the validation.
22. **Independent review of version 2 (2026-10-18).** A review of the five documents of version 2 against the outputs found every
    computed number in agreement except three roundings, and found the following, all corrected in the documents: (a) the
    dark-matter relic: the operator $\bar\chi\chi F_{\mu\nu}F^{\mu\nu}$ annihilates a pair only from $^3P_0$, so the unitarity bound on the spin-averaged
    cross-section is $\sigma \le \pi/(4p^2)$ and $\langle\sigma v\rangle \le \sqrt{\pi x_f}/M^2 = 5.79\times10^{-26}$ cm$^3$/s; the freeze-out requirement
    $2.01\times10^{-25}$ cm$^3$/s exceeds it 3.47 times (the documents had compared it with $(4\pi/M^2)\sqrt{x_f/\pi} = 2.32\times10^{-25}$ cm$^3$/s, the
    bound of one helicity channel without the spin average, and called the requirement 87 % of it); the relic abundance of the dark
    matter is therefore OPEN in version 2, and the check `B3_relic_requirement_and_unitarity` of `um2_analysis.py` now computes the
    bound, its numerical thermal average, the crossing velocity $v_c = 0.263$ and the fraction (79 %) of pairs above it; (b) "no tip
    operator reaches $\Psi_B$" holds only for chiral $P_+$ tip currents and for operators built on $\bar\Psi\Psi$ (a non-chiral tip current would
    reach $\Psi_B$); (c) the fast-flavour dispersion relation is written with the upper-index shifts $\Lambda^0$, $\Lambda^3$ and the stated metric
    $\eta^{\mu\nu} = \mathrm{diag}(1, -1)$ on $(x_4, x_3)$; (d) $c_Z = c'_Z = 0$ is a modelling choice (ASSUMED): the invisible width bounds the even part
    and $N_{eff}$ disfavours, but does not exclude, the oriented part; (e) the coordinate rule: the flavour, decoupling and
    fast-flavour equations had written $t$ for $x_4$ and $z$ for the symmetry axis $x_3$; (f) roundings: the adiabatic solar $P_{ee}$ at 15 MeV
    ($0.306$), the $\tau$ singlet bulk mass ($-9.205H$), the Kohn-Sham accuracy ($2.2\times10^{-9}$ relative); (g) minor items: $J_{max}$ computed from the
    best-fit angles ($0.0335$) against NuFIT's marginalised value ($0.0333 \pm 0.0007$); the conventions of the supernova resonances
    (two-flavour conditions); the tip matrices equal the mixing matrices only with $\kappa_e = \kappa_u = 1$ (ASSUMED); the three roles of the
    measured values; the sum rules of the uncertainty analysis (absolute $1.0\times10^{-8}$, relative $7.8\times10^{-4}$ and $6.0\times10^{-4}$ for $W^\pm$ and
    $Z$); the 50-digit roots against the stored masses ($4.5\times10^{-11}$); the labels ESTIMATE and STANDARD; the number required for a single
    species ($(17.6\ \text{TeV})^{-3}$ with $g_* = 105.75$, not a version-1 value); further notational clashes added to the symbol lists; (h)
    self-containment: equations and inputs used but not written in a document (the relic and $\Delta N_{eff}$ formulas, the Einstein-Boltzmann
    equations, the BAO $\chi^2$ and data, the nonlinear background equations, the fermion equations with their boundary conditions, the
    decoupling equations, the CNB, Landau-Zener, adiabatic solar, condensate and pairing formulas, the Kohn-Sham equations behind the
    quoted equations of state) are now written out in every document that uses them.

## What is not in the repository, and why

By the author's instruction the following private inputs are never committed (they are git-ignored): the prompt files,
the author's private PDF with the supernova dark-energy fits, the folders `dirac-main/` and `vendor/`, the archive
`dirac-main_2.zip`, the files `Generalized_Kronecker_Delta.*`, and the notebook `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb`
with its `.mx` files. The paper "Neutrino Flavor Conversion.pdf" (Gogilashvili and Tamborra, arXiv:2605.16504) is a third-party
publication and is not committed either; UM-2 cites its results. UM-2 uses from these inputs only what is written out in this
document (the notebook formulas of the metric and of the gamma matrices, the two supernova fits, the explosion statistics).

## Reproduction

From the repository root, with Python 3 and the packages sympy, numpy, scipy, mpmath, matplotlib and camb installed
(`pip install sympy numpy scipy mpmath matplotlib camb`), the commands
```text
python universe_model_2/code/um2_algebra.py
python universe_model_2/code/um2_geometry.py
python universe_model_2/code/um2_background.py
python universe_model_2/code/um2_fields.py
python universe_model_2/code/um2_spectra.py
python universe_model_2/code/um2_flavour.py
python universe_model_2/code/um2_neutrino.py
python universe_model_2/code/um2_ks_jobs.py validate
python universe_model_2/code/um2_ks_jobs.py spectrum
python universe_model_2/code/um2_ks_jobs.py ground8
python universe_model_2/code/um2_ks_jobs.py ground592
python universe_model_2/code/um2_ks_jobs.py darkmatter
python universe_model_2/code/um2_ks_jobs.py portals
python universe_model_2/code/um2_ks_jobs.py feedback
python universe_model_2/code/um2_electroweak.py
python universe_model_2/code/um2_primordial.py
python universe_model_2/code/um2_cosmology.py
python universe_model_2/code/um2_analysis.py
python universe_model_2/tools/build_docs.py
```
rerun every computation in dependency order (each exits with code 0 if and only if all its checks pass) and rebuild
the PDF documents from the Markdown sources (pandoc and a TeX Live installation with the `lmodern` package are needed
for the last command). Version 1 was rerun from fresh clones of the repository (2026-10-17 at commit `b3c3c1a`; 2026-10-18 at
commits `fa7305f`, `9285bb6` and `5b73d16`), and version 2 on 2026-10-18 at commit `4a6421d` (every computation as a separate step,
1027 s in all, the longest the primordial integration with 268 s): every check passed (205 of 205 for version 2) and every stored
number was reproduced to a relative $10^{-9}$ or better (in the version-2 run all numbers were identical except one Kohn-Sham
integral, which differs by $1.1\times10^{-12}$ relative, because the threaded linear algebra does not sum in a fixed order), and the
LaTeX sources, the PDF documents and the figures were rebuilt byte-identical. After that run, `um2_analysis.py` gained the
$^3P_0$ unitarity bound of item 22 (new stored numbers, the same 23 checks, all passing when rerun). The document build is
deterministic: no dates in the LaTeX sources, PDF dates and trailer identifiers suppressed, a fixed `SOURCE_DATE_EPOCH`.

Software used: Python 3.13.16, sympy 1.14.0, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, matplotlib 3.11.2, camb 2.0.5,
pandoc 3.1.3, pdfTeX 1.40.25 (TeX Live 2023).

## History in the repository

UM-2 was started on top of commit `0cb4916`. Version 1: its computations were committed in the order algebra and geometry
(`ca523d9`), background gravity (`0b3e10d`), field reductions (`6fc35a0`), mass spectra (`dcfd528`), Kohn-Sham
(`2f3018e`), electroweak sector (`2e4c48d`), primordial era (`a502e62`), cosmology (`717b46e`), analysis (`a06b55e`),
followed by the corrections listed above and the documents MODEL, PROVENANCE, FIELD_EQUATIONS, SOLUTION and ANALYSIS
(Markdown, LaTeX and PDF each); the fixes of the three independent reviews are in `b386446`, `fa7305f`, `b0e686e`, `9285bb6`,
`d92a61b`, `c98de95`, `1561566`, `df358db` and `5b73d16`; a checklist for manual reruns and the comparison tool are in `7b86239`.
Version 2: three generations and the masses and mixing (`94621af`), the neutrino flavour conversion (`a0d750a`), the electroweak
sector of three generations (`cf824d5`), the removal of the tip $Z$ portal and the cosmology with three massive neutrinos
(`53c5139`), the dark matter of both halves, the twelve-fermion tables and the three-generation tip and gauge checks (`b755990`),
the corrected 1-3 resonance (`b999f57`), the documents MODEL (`9a5b92b`), FIELD_EQUATIONS (`79d9d31`), SOLUTION (`a3dcc6a`),
ANALYSIS (`df6d94a`) and PROVENANCE (`4a6421d`), and the fixes of the independent review of version 2 (item 22; the commit that
carries this text).
