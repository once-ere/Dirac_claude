# The fields of UM-2 and the action

The author's order of 2026-10-18 lists the coupled fields: gravity (Einstein-Lovelock gravity, which couples to all fields), the
dirac16complex quantized fermion spinor field (which couples to all other fields), the three-flavour left-handed neutrinos, the
left-handed electrons, the right-handed electron singlet, three quark generations, gluons, photons and the three weak gauge bosons
$W^+$, $W^-$ and $Z$, and no Higgs particle. UM-2 realises this list as follows (the other two lepton generations and their
right-handed partners, the right-handed neutrinos, the tip sigma field and the block stabiliser are those of version 3):

| the author's field | the field of UM-2 | content | couples to | four-dimensional masses |
| --- | --- | --- | --- | --- |
| Einstein-Lovelock gravity | the metric $g_{MN}$ (vielbein $\mathbf{e}^a{}_M$) | the graviton, the Kaluza-Klein gravitons, the radion | every field, through $\sqrt{\lvert g\rvert}$, $g^{MN}$ and the spin connection in every action; the stabiliser | graviton 0; Kaluza-Klein gravitons from 121.32 TeV; radion 48.42 TeV |
| dirac16complex | $\Psi$, 16 complex Grassmann components, halves $\Psi_A$ and $\Psi_B$ | fold bands (massless), bulk band (dark matter) | gravity (spin connection), itself ($\lambda$), every fermion (I11), the quarks (I13), gluons, $W$ and $B$ (I12) | fold bands 0; dark matter 44.35 TeV |
| three-flavour left-handed neutrinos | the upper components of the lepton doublets $\ell_i$ | $\nu_e$, $\nu_\mu$, $\nu_\tau$ (flavour states) $= U(\nu_1, \nu_2, \nu_3)$ (mass states) | $W^\pm$, $Z$, gravity, $\Psi$ (I11), $\Sigma$ at the tip | $1.000$, $8.712$, $50.140$ meV |
| left-handed electrons | the lower component of $\ell_1$ | the left-handed electron, charge $-1$ | photon, $W^\pm$, $Z$, gravity, $\Psi$ (I11), $\Sigma$ | $0.51100$ MeV (with $e_R$) |
| right-handed electron singlet | $e_{R1}$ | the right-handed electron, charge $-1$ | photon, $Z$, gravity, $\Psi$ (I11), $\Sigma$ | (the electron) |
| the other two lepton generations and their right-handed partners | $\ell_2$, $\ell_3$, $e_{R2}$, $e_{R3}$ | muon and tau, left- and right-handed | as the electron | $105.658$ MeV, $1776.93$ MeV |
| right-handed neutrinos | $\nu_{R1}$, $\nu_{R2}$, $\nu_{R3}$ | gauge singlets | gravity, $\Psi$ (I11), $\Sigma$ at the tip | (Dirac partners of the neutrinos) |
| three quark generations | $Q_i$, $u_{Ri}$, $d_{Ri}$ | up, down, charm, strange, top, bottom, three colours each | gluons, photon, $W^\pm$, $Z$, gravity, $\Psi$ (I11, I13), $\Sigma$ | from $2.16$ MeV (up) to $172.56$ GeV (top) |
| gluons | $G^A_M$, $A = 1, \dots, 8$ | eight massless gluons | quarks, themselves, $\Psi$ (I12), gravity | 0 |
| photons | $A_M$ (a combination of $W^3_M$ and $B_M$) | the photon | charged fermions, $W^\pm$, $\Psi$ (I12), gravity | 0 |
| $W^+$, $W^-$, $Z$ | $W^\pm_M$ (from $W^1_M$, $W^2_M$), $Z_M$ (from $W^3_M$, $B_M$) | $W^+$ charge $+e$, $W^-$ charge $-e$, $Z$ neutral | fermions, photon, each other, $\Sigma$ at the tip, $\Psi$ (I12), gravity | $80.3625$, $80.3625$, $91.1879$ GeV |
| no Higgs particle | the tip sigma field $\Sigma \in SU(2)$, without a radial mode | three would-be Goldstone modes, the longitudinal $W^+$, $W^-$, $Z$ | $W$, $B$, the fermions (tip Yukawa terms), gravity | no particle |
| (version 3) | the block stabiliser $\rho_{\mathrm{stab}}(f)$ | a vacuum energy of the hidden block | gravity | none |

The action of UM-2 is the sum of all terms (IN-1); varying it gives every field equation of the model:

@@IN-1@@

The following sections write out every term and the field equation of every field; the section on the interactions then writes
out, explains and analyses every interaction.

# Gravity and the block stabiliser

## Einstein-Lovelock gravity, which couples to all fields (AUTHOR weights)

The gravitational action is the Einstein-Lovelock action with the author's weights:

@@IN-2@@

with the Lovelock densities (generalised Kronecker delta: the determinant of the matrix of ordinary Kronecker deltas)

@@IN-3@@

$\mathcal{L}_{(3)}$ is the cubic Lovelock density. (The author's notebook writes $\Lambda = 10$ with the opposite sign convention for
$\Lambda$.) UM-2 keeps these values. Gravity couples to every field through the volume element $\sqrt{\lvert g\rvert}$, the inverse
metric in every kinetic term and the canonical spin connection of every spinor (IN-7 in the section on dirac16complex). Varying the
action with respect to the metric gives the Einstein-Lovelock equations,

@@FE-1@@

$\mathcal{E}_{(1)}$ being the Einstein tensor, with the energy-momentum tensor of all matter defined and decomposed as

@@FE-2@@

The total source is the sum of the energy-momentum tensors of every term of the action (each written out with its field below):

@@FE-3@@

Every Lovelock tensor is divergence-free identically, so the field equations imply the conservation of the source, which holds on
the matter field equations (DERIVED for the order-0 metric for $p = 1, 2, 3$):

@@FE-11@@

**For a pair-diagonal curvature (DERIVED).** When the Riemann tensor is pair-diagonal (the order-0 metric), the Lovelock densities
and the diagonal Lovelock tensors are sums of products of sectional curvatures,

@@FE-34@@

which was checked against the Einstein tensor from the Ricci tensor ($p = 1$), against the explicit Gauss-Bonnet tensor ($p = 2$),
against the Bianchi identities ($p = 1, 2, 3$), against the Euler-Lagrange equations of the action with a lapse ($p = 1, 2, 3$) and
against the record's equations (all exact).

## The block stabiliser (ASSUMED)

A source term, a vacuum energy of the hidden block, stabilises the block:

@@IN-4@@

Its energy-momentum tensor is

@@FE-4@@

It is conserved: the conservation law of the order-0 source,

@@FE-41@@

gives, with $p_3 = -\rho_{\mathrm{stab}}$ and $\bar p = \rho_{\mathrm{stab}}$, $\dot\rho = -8\mathcal{H}_f\rho$, i.e. $\rho_{\mathrm{stab}} \propto f^{-8}$. It is
four-dimensionally Lorentz invariant ($p_3 = -\rho$), isotropic in the block ($p_0 = p_5$), as the order-0 field equations require
(the section on gravity), and independent of $x_0$. The $f^{-8}$ law is that of an eight-dimensional energy density whose only scale
is the size of the block (a Casimir-type or flux energy). Its normalisation is fixed by the static block,
$\kappa\rho_{\mathrm{stab}}(f_*) = (26 + 4\sqrt{51})H^2$ at $f_* = K_*^{-1/2}$. Its microscopic origin is OPEN (a Casimir energy of the
fields of the cell or a flux are natural candidates; neither was computed in UM-2).

# The dirac16complex field, which couples to all other fields

## The Clifford algebra of the author (AUTHOR, DERIVED verification)

The author's real $16\times16$ matrices are built from real $4\times4$ matrices $\mathsf{s}_h$ and $\mathsf{t}_h$ ($h = 1, 2, 3$; matrix
indices $k, q = 1, \dots, 4$; $\epsilon_{\mathrm{LC}}$ the Levi-Civita symbol):

$$
\big(\mathsf{s}_h\big)_{kq} = \epsilon_{\mathrm{LC}}^{hkq4} - \delta_{k4}\delta_{qh} + \delta_{kh}\delta_{q4},\qquad
\big(\mathsf{t}_h\big)_{kq} = \epsilon_{\mathrm{LC}}^{hkq4} + \delta_{k4}\delta_{qh} - \delta_{kh}\delta_{q4},
$$
<!-- symbols: AUTO -->

then the real $8\times8$ matrices $\mathsf{Z}_a$ ($a = 0, \dots, 7$; $\mathbf{1}$ the identity of the size of the block) and the
$16\times16$ gamma matrices:

$$
\begin{aligned}
&\mathsf{Z}_0 = \mathbf{1},\qquad \mathsf{Z}_h = \begin{pmatrix}0 & \mathsf{s}_h\\ \mathsf{s}_h & 0\end{pmatrix},\qquad
 \mathsf{Z}_{7-h} = \begin{pmatrix}0 & \mathsf{t}_h\\ -\mathsf{t}_h & 0\end{pmatrix}\quad (h = 1, 2, 3),\qquad
 \mathsf{Z}_7 = \mathsf{Z}_1\mathsf{Z}_2\mathsf{Z}_3\mathsf{Z}_4\mathsf{Z}_5\mathsf{Z}_6,\\
&\mathsf{S} = \begin{pmatrix}0 & \mathbf{1}\\ \mathbf{1} & 0\end{pmatrix},\qquad \bar{\mathsf{Z}}_a = \mathsf{S}\,\mathsf{Z}_a^T\,\mathsf{S},\qquad
 \gamma^a = \begin{pmatrix}0 & \bar{\mathsf{Z}}_a\\ \mathsf{Z}_a & 0\end{pmatrix}\quad (a = 0, \dots, 7).
\end{aligned}
$$
<!-- symbols: AUTO -->

The frame matrix along $x_0$ is written $\gamma^{x_0} = \gamma^0$, and so on up to $\gamma^{x_7} = \gamma^7$ (the notebook's `T16[A]`).
They satisfy (DERIVED, exact; 31 checks)

$$
\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,\mathbf{1},\qquad
\tfrac12\big(\mathsf{Z}_a\bar{\mathsf{Z}}_b + \mathsf{Z}_b\bar{\mathsf{Z}}_a\big) = \eta_{ab}\,\mathbf{1},\qquad
\mathsf{S} = \mathsf{Z}_1\mathsf{Z}_2\mathsf{Z}_3 = \mathsf{Z}_4\mathsf{Z}_5\mathsf{Z}_6\mathsf{Z}_7 .
$$
<!-- symbols: AUTO -->

The Clifford algebra, the Dirac adjoint, the four-dimensional chirality and the author's operator $\mathcal{B}$, whose eigenspaces are
the two halves of dirac16complex, are

@@IN-6@@

With the author's matrices

$$
\begin{aligned}
&C = \begin{pmatrix}-\mathsf{S} & 0\\ 0 & \mathsf{S}\end{pmatrix},\qquad
 \Gamma_8 = \gamma^{x_0}\gamma^{x_1}\cdots\gamma^{x_7} = \mathrm{diag}\big(-\mathbf{1},\ \mathbf{1}\big),\\
&C^T = C,\quad C^2 = \mathbf{1},\quad \big(C\gamma^a\big)^T = -C\gamma^a,\quad \mathcal{B}^\dagger = \mathcal{B},\quad \mathcal{B}^2 = \mathbf{1},
\end{aligned}
$$
<!-- symbols: AUTO -->

and $\mathcal{B}$ has the signature $(8, 8)$. Since every $C\gamma^a$ is real and antisymmetric, $\bar\Psi\gamma^a\Psi$ is anti-Hermitian and
the Hermitian vector currents are $\mathrm{i}\bar\Psi\gamma^a\Psi$; $\bar\Psi\Psi$ is Hermitian. The 16-dimensional representation is
irreducible under Pin(4,4) (commutant of dimension 1), the double cover of $O(4,4)$, and it splits under Spin(4,4), the double
cover of $SO(4,4)$, into two inequivalent irreducible 8-dimensional representations, the eigenspaces $\Gamma_8 = \mp1$ (commutant of
dimension 2, intertwiner of dimension 0).

## The Lagrangian and the canonical spin connection

$\Psi$ has 16 complex anticommuting (Grassmann) components. It couples to gravity through the canonical (metric-compatible,
torsion-free) spin connection, which couples every spinor of UM-2 to gravity:

@@IN-7@@

it makes $\gamma^N$ covariantly constant, $\partial_M\gamma^N + \Gamma^N{}_{MP}\gamma^P + \Omega_M\gamma^N - \gamma^N\Omega_M = 0$ (DERIVED).
The action of dirac16complex is the record's:

@@IN-5@@

The mass parameter is the author's $m_\Psi = 3H\mathcal{M}$; UM-2 uses $\mathcal{M} = 1/3$, i.e. $m_\Psi = H$ (RECORD, the value of the
Kohn-Sham record). $\lambda$ is the contact self-coupling. It lets the dark matter annihilate into the fold bands, so the cosmology
bounds it: $G_\lambda = \lambda H\tilde I_\lambda/(2f^4v_{\mathrm{t}}) \le 2.3\times10^{-15}$ GeV$^{-2}$ (ASSUMED; the dark sector), i.e.
$\lambda \le 1.4\times10^{-10}H^{-6}$ for $v_{\mathrm{t}} = H^{-3}$; the value $\lambda_{\mathrm{test}} = 7\times10^{-5}H^{-6}$ of the
Kohn-Sham tests is a numerical test value. Varying the action (with the portals of the section on the interactions) gives the
field equation of dirac16complex,

@@FE-12@@

and its conjugate. Its gravitational term is $\gamma^M\Omega_M$; for the order-0 metric (DERIVED, exact for every $a_4$, $b_4$ and on
both halves of a period)

@@FE-13@@

which vanishes only in flat 4+4 space ($H = 0$ with constant $a_4$, $b_4$): the coupling of $\Psi$ to gravity is non-trivial.
$\Psi$ is a singlet of the Standard-Model group, so it couples to the Standard Model only through the portals I11, I12 and I13. Its
energy-momentum tensor (the source of $\Psi$ in the gravitational equations) is

@@FE-5@@

and its boundary conditions at the fold ($y = 0$) and at the regular tip ($y = -L$) are

@@FE-28@@

(both parities are modes of the full period; the conditions are self-adjoint, DERIVED).

## The two halves $\Psi_A$ and $\Psi_B$ and the fold parity (DERIVED)

$\mathcal{B}$ commutes with every four-dimensional Lorentz generator $\gamma^a\gamma^b$ ($a, b \in \{1, 2, 3, 4\}$) and with $C$, so the
split $\Psi = \Psi_A + \Psi_B$ of IN-6 ($\mathcal{B}\Psi_A = -\Psi_A$, $\mathcal{B}\Psi_B = +\Psi_B$) gives two four-dimensionally
Lorentz-invariant halves of 8 components, and $\bar\Psi\Psi = \bar\Psi_A\Psi_A + \bar\Psi_B\Psi_B$ does not mix them. In the good sector (no
extra-time momenta) every interaction of UM-2 commutes with $\mathcal{B}$ (DERIVED with the author's matrices: $\mathcal{B}$ commutes with
$C$, with $\gamma^a$ and with $C\gamma^a$ for $a = 0, \dots, 4$ and anticommutes with them for $a = 5, 6, 7$, and $\gamma^M\Omega_M$ contains
$\gamma^{x_0}$ and $\gamma^{x_4}$ only), so the numbers of quanta of the two halves are separately conserved; extra-time
momenta would mix the halves. Under the fold reflection $z \mapsto \pi - z$ the modes are even or odd; the bulk Lagrangian is
symmetric under it.

