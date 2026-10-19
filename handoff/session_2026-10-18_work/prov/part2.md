# Ingredients from the author (AUTHOR)

## Coordinates and signature

The author's coordinates (notebook `Dirac_Einstein-Lovelock_4+4_Nash.nb`, `X = {x0[], x1[], ..., x7[]}`) are

$$
X = \{x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7\},\qquad z = 6Hx_0,\qquad 0 < z < \pi
$$

<!-- symbols: Xcoord, x0, x1, x2, x3, x4, x5, x6, x7, zvar, Hconst, pi -->

with $x_0$ a hidden space-like direction, $x_1, x_2, x_3$ ordinary space, $x_4$ the time and $x_5, x_6, x_7$ three extra
time-like directions; the interval $0 < z < \pi$ is one period of $x_0$, of length $\pi/(6H)$. The orthonormal frame
metric, with the frame directions aligned with $x_0, \dots, x_7$ in this order, is

$$
\eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)
$$

<!-- symbols: eta, ia, ib, diag -->

## The primordial metric of the notebooks

The notebook `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb` (the author's local notebook) gives the primordial metric

$$
\begin{aligned}
g_{\mathrm{nb}} = \mathrm{diag}\big(&\cot^2z,\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},
 \ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\\
&-1,\ -\mathrm{e}^{-2a_4}(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}(\sin^2z)^{1/6}\big)
\end{aligned}
$$

<!-- symbols: mod_gnb, diag, zvar, euler, a4 -->

with the vielbein $\mathrm{diag}\big(\cot z$, three times $\mathrm{e}^{a_4}(\sin^2z)^{1/12}$, $1$, three times
$\mathrm{e}^{-a_4}(\sin^2z)^{1/12}\big)$ and $a_4 = a_4(x_4)$. By the author's orders of 2026-10-14 a second function
$b_4(x_4) > 0$ multiplies the extra-time components ("b4 is a function of x4; b4 is NEVER 1"), and $(\sin z)^{1/3}$ means
$(\sin^2z)^{1/6}$, the positive branch, for every real $z$. The metric that UM-2 uses, the corrected metric of the Revision
record (FE-31), is written out in section 5.

## The Einstein-Lovelock equations, the weights and the cosmological term

The notebook writes the vacuum Einstein-Lovelock equations (after Lovelock and Rund) as

$$
0 = -10\,\delta^M_N + \frac{w_{(1)}}{H^2}\,\mathcal{E}_{(1)}{}^M{}_N + \frac{w_{(2)}}{H^4}\,\mathcal{E}_{(2)}{}^M{}_N
 + \frac{w_{(3)}}{H^6}\,\mathcal{E}_{(3)}{}^M{}_N,\qquad
w_{(1)} = 1,\quad w_{(2)} = \frac{1}{32},\quad w_{(3)} = \frac{1}{1152}
$$

<!-- symbols: delta, iM, iN, wL, Hconst, LovE -->

where the notebook's tensor "Lovelock$p$" is the Lovelock tensor $\mathcal{E}_{(p)}{}^M{}_N$ of order $p$. In the notebook
`Dirac_Einstein-Lovelock_4+4_Nash.nb` (In[133] to In[136]) the author sets $w_{(1)} = 1$, $w_{(2)} = 1/2^5$ and solves the
vacuum equations on the history $a_4 = Hx_4$, $b_4 = 1$ of the notebook metric for $w_{(3)}$ and for the cosmological
number (In[134]); In[136] factors $1152 = 2^7\,3^2$; the Revision specification records the solution $w_{(3)} = 1/1152$
and the number $10$. Multiplying by $H^2$ and writing the equations as the Einstein-Lovelock equations with a source gives
the couplings and the cosmological constant of UM-2,

$$
\alpha_{(p)} = w_{(p)}\,H^{2-2p},\qquad \Lambda = -10H^2
$$

<!-- symbols: alphaL, wL, Hconst, ip, Lambda -->

which enter the action term IN-2 (section 6). With these couplings and the source of all matter, the notebook's equations
become the field equations of gravity of UM-2, with the Lovelock tensors written with the generalised Kronecker delta:

@@FE-1@@

That this normalisation reproduces the record's field equations (which were checked against the notebook) is verified
exactly by `um2_geometry.py` (checks `record_equation constraint_x4`, `record_equation space_x1_eq_x2_eq_x3`,
`record_equation hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7`). UM-2 keeps the author's weights and $\Lambda$ unchanged; an
earlier model of this repository (UM-1) had changed $w_{(3)}$ and $\Lambda$.

## The gamma matrices of the Clifford algebra of signature (4, 4)

Both notebooks of the author named above build real $16\times16$ matrices in three steps. First, two real $4\times4$
matrices for each $h = 1, 2, 3$ (the notebook's arrays `s` and `t`, built as `Qa - Qb` and `Qa + Qb` from the Levi-Civita
array `Qa` and a second array `Qb` of Kronecker deltas):

$$
(\mathsf{s}_h)_{kq} = \epsilon_{\mathrm{LC}}^{hkq4} - \delta_{k4}\delta_{qh} + \delta_{kh}\delta_{q4},\qquad
(\mathsf{t}_h)_{kq} = \epsilon_{\mathrm{LC}}^{hkq4} + \delta_{k4}\delta_{qh} - \delta_{kh}\delta_{q4}
$$

<!-- symbols: mod_sh, mod_th, mod_ih, mod_ikq, mod_epsLC, delta -->

Second, eight real $8\times8$ matrices and the matrix that pairs them (the notebook's arrays `zeta` and `tau`, which are
equal, and `sigma`; the identity $\mathbf{1}$ is $8\times8$ for $\mathsf{Z}_0$ and $4\times4$ inside $\mathsf{S}$):

$$
\mathsf{Z}_0 = \mathbf{1},\qquad
\mathsf{Z}_h = \begin{pmatrix}0 & \mathsf{s}_h\\ \mathsf{s}_h & 0\end{pmatrix},\qquad
\mathsf{Z}_{7-h} = \begin{pmatrix}0 & \mathsf{t}_h\\ -\mathsf{t}_h & 0\end{pmatrix},\qquad
\mathsf{Z}_7 = \mathsf{Z}_1\mathsf{Z}_2\mathsf{Z}_3\mathsf{Z}_4\mathsf{Z}_5\mathsf{Z}_6,\qquad
\mathsf{S} = \begin{pmatrix}0 & \mathbf{1}\\ \mathbf{1} & 0\end{pmatrix}
$$

<!-- symbols: mod_Za, identity, mod_ih, mod_sh, mod_th, mod_Ssf -->

Third, the gamma matrices along the frame directions $a = 0, \dots, 7$ (the notebook's `T16`):

$$
\bar{\mathsf{Z}}_a = \mathsf{S}\,\mathsf{Z}_a^T\,\mathsf{S},\qquad
\gamma^a = \begin{pmatrix}0 & \bar{\mathsf{Z}}_a\\ \mathsf{Z}_a & 0\end{pmatrix}
$$

<!-- symbols: mod_Zbar, mod_Ssf, mod_Za, ia, transpose, gamma -->

They satisfy the Clifford algebra and the notebook identities (notebook Out[322] to Out[324]; the identity $\mathbf{1}$ is
$16\times16$ in the first relation and $8\times8$ in the second):

$$
\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,\mathbf{1},\qquad
\tfrac12\big(\mathsf{Z}_a\bar{\mathsf{Z}}_b + \mathsf{Z}_b\bar{\mathsf{Z}}_a\big) = \eta_{ab}\,\mathbf{1},\qquad
\mathsf{S} = \mathsf{Z}_1\mathsf{Z}_2\mathsf{Z}_3 = \mathsf{Z}_4\mathsf{Z}_5\mathsf{Z}_6\mathsf{Z}_7
$$

<!-- symbols: gamma, ia, ib, eta, identity, mod_Za, mod_Zbar, mod_Ssf -->

The derived matrices that UM-2 uses (the matrix of the Dirac adjoint, the chirality of eight dimensions, the author's
operator that separates the two halves of dirac16complex, and the generators of frame rotations) are, with the author's
matrices,

$$
C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3} = \begin{pmatrix}-\mathsf{S} & 0\\ 0 & \mathsf{S}\end{pmatrix},\qquad
\Gamma_8 = \gamma^{x_0}\gamma^{x_1}\cdots\gamma^{x_7} = \begin{pmatrix}-\mathbf{1} & 0\\ 0 & \mathbf{1}\end{pmatrix},\qquad
\mathcal{B} = -\mathrm{i}C\gamma^{x_4},\qquad \mathcal{S}^{ab} = \tfrac14\big[\gamma^a, \gamma^b\big]
$$

<!-- symbols: Cmat, gamma, x0, x1, x2, x3, x7, mod_Ssf, mod_Gamma8, identity, calB, imag, x4, calS, ia, ib -->

All of these relations are verified exactly with the rebuilt matrices by `um2_algebra.py` (31 checks, among them
`tau_relations_of_the_notebook`, `notebook_identities_sigma`, `clifford_relations`, `identical_to_record_gammas`,
`C_is_sigma16`, `chirality_diag`); the matrices enter the action through IN-6 (section 6).

## The mass parameter, the $x_0$ mass idea and the dark-matter hypothesis

The mass of dirac16complex is written $m_\Psi = 3H\mathcal{M}$ in the author's notebooks (the action term IN-5). The orders
require every non-massless particle to get its mass from the dependence of its wave function on $x_0$, periodic with the
period $\pi/(6H)$, with the uncertainty relation of $x_0$ and its momentum as the physical reason, and state the hypothesis
that the quanta of dirac16complex represent dark matter (and ask for the validity of a dark-energy association to be
analysed).

# Ingredients from the Revision record (RECORD)

## The corrected primordial metric

The author's order of 2026-10-16: "a diagonal form for the metric of the primordial gravitational field is only
self-consistent if all off-diagonal terms of all source terms in the Einstein field equations ARE ZERO. This is not the
case here. I task you to: [1] find the simplest modification for the current metric of the primordial gravitational field
that is probably self-consistent with the Einstein field equations". The metric of 2026-10-14 (the notebook metric with
$b_4$) has an off-diagonal Lovelock component $\mathcal{E}_{(p)}{}^{x_4}{}_{x_0} \propto \cot z\,\dot b_4/b_4$ at every
Lovelock order $p$. The record examined the family of diagonal metrics with $g_{x_4x_4} = -1$ and

$$
\begin{aligned}
&g_{x_0x_0} = b_4^{2\mathfrak{p}}\,\mathrm{e}^{2\mathfrak{q}a_4}\cot^2z,\qquad
 g_{x_1x_1} = g_{x_2x_2} = g_{x_3x_3} = \mathrm{e}^{2a_4}(\sin^2z)^{3\mathfrak{a}},\\
&g_{x_5x_5} = g_{x_6x_6} = g_{x_7x_7} = -\mathrm{e}^{-2a_4}b_4\,(\sin^2z)^{3\mathfrak{b}}
\end{aligned}
$$

<!-- symbols: metric, x0, x1, x2, x3, x5, x6, x7, b4, prov_family, euler, a4, zvar -->

whose mixed curvature (3-space with the hidden direction, and the extra times with the hidden direction) vanishes for
every $a_4(x_4)$ and $b_4(x_4)$ only if

$$
\mathfrak{a}\Big((\mathfrak{q} - 1)\,\dot a_4 + \mathfrak{p}\,\frac{\dot b_4}{b_4}\Big) = 0,\qquad
\mathfrak{b}\Big((\mathfrak{q} + 1)\,\dot a_4 + \big(\mathfrak{p} - \tfrac12\big)\frac{\dot b_4}{b_4}\Big) = 0
$$

<!-- symbols: prov_family, a4dot, b4dot, b4 -->

Keeping the warp of the extra times ($\mathfrak{b} = 1/6$) forces $\mathfrak{a} = 0$, $\mathfrak{q} = -1$,
$\mathfrak{p} = 1/2$: the record's current metric, the order-0 metric of UM-2,

@@FE-31@@

Every off-diagonal component of $\mathcal{E}_{(1)}$, $\mathcal{E}_{(2)}$, $\mathcal{E}_{(3)}$ vanishes identically for all
$a_4(x_4)$, $b_4(x_4) > 0$ and every real $z$ (record: sympy 14/14, Wolfram 13/13; re-derived in UM-2 by `um2_geometry.py`,
checks `y_chart_pair_diagonal`, `author_chart_pair_diagonal`, `charts_agree`). The alternative K of the record (hidden
component $\mathrm{e}^{2a_4}\cot^2z$, 3-space components $\mathrm{e}^{2a_4}(\sin^2z)^{1/6}$, extra-time components
$-\mathrm{e}^{-2a_4}b_4$) is also diagonal at every order; the record leaves the choice to the author, and UM-2 uses the
metric FE-31 (status AUTHOR in the inventory: the author's coordinates and functions, corrected by the record under his
order).

## The hidden coordinate, the fold and the regular tip

On every interval with $\sin z \ne 0$ the record introduces the hidden coordinate $y$ and the block scale $f$:

@@FE-32@@

The fold is $z = \pi/2$ ($y = 0$); the tips are $z \to 0^+$ and $z \to \pi^-$ ($y \to -\infty$). The record replaces each tip
by a regular cutoff at $y = -L$ with $HL = 3$, a chosen depth (the extended levels depend on it like those of a box of
proper length $fL$). UM-2 keeps $HL = 3$ (ASSUMED).

## The dirac16complex Lagrangian and the canonical spin connection

The specification of the record (under the author's orders) fixes the Dirac-type Lagrangian of dirac16complex with the
contact self-interaction and the canonical (vielbein-postulate, torsion-free) spin connection: the action term IN-5 with the
connection IN-7, written out in section 6. The record chose the Dirac-type form because the notebook's real Majorana-type
Lagrangian is a total derivative for anticommuting real fields (it has no field equations), and it uses the canonical
connection rather than the notebook's contraction of the mixed connection coefficients, which lacks a metric factor. The
field equation of the record is $\gamma^MD_M\Psi = (m_\Psi + \lambda\bar\Psi\Psi)\Psi$, the part of the dirac16complex field
equation FE-12 without the portals.

## Canonical quantisation and the Krein metric

With $x_4$ as the evolution time, the canonical anticommutator of $\Psi$ and $\Psi^\dagger$ on a slice $x_4 = $ const is the
matrix $\mathcal{B}$ times the Dirac delta function of the seven remaining coordinates divided by $\sqrt{\lvert g\rvert}$;
$\mathcal{B}$ has the eigenvalues $+1$ (8 times) and $-1$ (8 times), so the inner product is indefinite (a Krein space). The
record works in the good sector (no extra-time momentum), counts the positive-energy branch of every block as particles,
and evaluates the expectation values of bilinears with the Krein metric $\mathcal{B}$ inserted between the spinors of the
modes (`um2_algebra.py`, checks `B_hermitian_involution`, `B_signature_8_8`, `B_gamma4_gamma_a_hermitian`).

## The Kohn-Sham reduction

For the corrected metric the record reduces the 16-component field equation, in the eight blocks of the commuting
operators $\gamma^{x_0}\gamma^{x_1}\gamma^{x_4}$, $\gamma^{x_2}\gamma^{x_3}$, $\gamma^{x_5}\gamma^{x_6}$ (eigenvalues $\varsigma$,
$\mathrm{i}\varsigma_2$ and $\mathrm{i}\varsigma_3$, each sign $\pm1$), to $2\times2$ block Hamiltonians; UM-2 re-derived the
reduction exactly for all eight blocks and general $a_4$, $b_4$ (`um2_fields.py`, check `dirac_reduction_exact`;
`um2_algebra.py`, checks `block_basis_unitary` to `block_form B gamma^(x0) = j s2 sigma3`):

@@FE-56@@

The record treats the contact interaction in the Hartree-plus-exchange (local) approximation; its mean fields are the
first terms of $M_{\mathrm{eff}}$ and $v$ in FE-64, to which UM-2 adds the mean fields of the portals I11, I12 and I13
(DERIVED):

@@FE-64@@

The densities, the momentum shells, the normalisation volume of a cell and the occupations, and the Kohn-Sham energy, are
the record's (both parities at the fold are filled, each with the weight $\frac12$; the record's mass is $m_\Psi = 3H\mathcal{M}$
with $\mathcal{M} = 1/3$, i.e. $m_\Psi = H$, which UM-2 keeps, ASSUMED):

@@FE-65@@

@@FE-66@@

Two reference states of the record (at $f = 1$, $a_4 = 0$: 8 particles in a cell with $\lambda = 157.7\,H^{-6}$, and 592
particles with $\lambda = 2.131\,H^{-6}$) serve as validation targets of the independent UM-2 solver: both are reproduced to
$10^{-13}$ in the energy, the highest occupied and the lowest unoccupied level and to $10^{-9}$ in the integrated hidden
pressure (`um2_ks_jobs.py validate`, checks `validate_N8_lamp1_a00`, `validate_N592_lamp1_a00`). The proper seven-volume of
a cell is $2\,\mathrm{Vol}_7(1 - \mathrm{e}^{-3HL})/(3H)$.

## Earlier work used only for comparison

The first universe model of this repository (UM-1, folder `Revision/universe_model`) is not an input of UM-2. UM-2 differs
from it in keeping the author's weights and $\Lambda$, in the electroweak sector, in the number of generations and in the
dark-matter candidate. Version 1 of UM-2 (2026-10-17, one generation) is superseded; its differences are item 21 of the
corrections.

