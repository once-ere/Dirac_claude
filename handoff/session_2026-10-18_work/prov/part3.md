# The action of UM-2 term by term, and the origin of each interaction

The action of UM-2 consists of the 18 interaction terms IN-1 to IN-18 below, each written out with its symbols and
followed by its origin. Varying the action with respect to every field gives the field equations FE-1 to FE-30; the other
field equations are their exact reductions on the static block and the equations of the four-dimensional effective theory
(section 8). The terms labelled INVENTED are the new phenomenological interactions that the author's orders require; for
each the reason for its form and its consistency with QCD and the electroweak model are stated.

## IN-1: the action

@@IN-1@@

**Origin (ASSUMED).** The choice of the terms is the model: the author's gravity (IN-2, IN-3); a stabiliser of the block
(IN-4); the record's dirac16complex field with its gamma matrices and its coupling to gravity (IN-5 to IN-7); the gauge
fields and the three generations of the Standard Model in eight dimensions (IN-8 to IN-12); the tip sigma field in place of
a Higgs field (IN-13 to IN-15); and three portals between dirac16complex and the Standard Model (IN-16 to IN-18). There is no
Higgs field: the orders exclude the Higgs particle. The chiral tip $Z$ portal I9 of version 1 is no longer part of the action
(its coefficients are zero; the end of this section).

## IN-2: Einstein-Lovelock gravity with the author's weights

@@IN-2@@

**Origin (AUTHOR).** The author's Einstein-Lovelock action (section 4): the weights $w_{(p)}$ and the cosmological constant
$\Lambda = -10H^2$ are the author's, unchanged. Its metric variation is the left side of FE-1, verified by four routes
(pairing formula, Ricci tensor, explicit Gauss-Bonnet tensor, minisuperspace variation with a lapse), by the Bianchi
identities and against the record's equations (`um2_geometry.py`, 25 checks).

## IN-3: the Lovelock densities

@@IN-3@@

**Origin (STANDARD).** The Lovelock densities (Lovelock 1971), built with the generalised Kronecker delta (the definition of
the author's file `Generalized_Kronecker_Delta`, which is not committed). For the pair-diagonal curvature of the order-0
metric they reduce to the pairing formula FE-34 (DERIVED; `um2_geometry.py`, checks `einstein_from_ricci_equals_pairing_k1`,
`gauss_bonnet_tensor_equals_pairing_k2`).

## IN-4: the block stabiliser

@@IN-4@@

**Origin (ASSUMED; its microscopic origin is OPEN).** Introduced in version 1 because the author's weights and $\Lambda$
admit no static block with attractive four-dimensional gravity without a source: the only sourceless static block with
$\mathcal{H} = 0$ has $K = 1/(4w_{(2)}) = 8$, where the coefficient of the four-dimensional Einstein-Hilbert term is
$\mathcal{G} = -1$ (repulsive), and it would need $\Lambda = -24H^2 \ne -10H^2$ (`um2_background.py`, checks
`static_vacuum_general`, `newton_factor_at_vacuum`). The stabiliser is conserved ($\rho_{\mathrm{stab}} \propto f^{-8}$),
four-dimensionally Lorentz invariant ($p_3 = -\rho_{\mathrm{stab}}$) and isotropic in the block ($p_0 = p_5$); its
normalisation is fixed by the static block (FE-43). The family in which the hidden pressure is $w_{\mathrm{stab}}$ times the
energy density, $p_0 = p_5 = w_{\mathrm{stab}}\rho_{\mathrm{stab}}$ with $\rho_{\mathrm{stab}} \propto f^{-4(1 + w_{\mathrm{stab}})}$,
was also computed at $w_{\mathrm{stab}} = 1/4, 1/2, 3/4, 1, 5/4, 3/2, 2, 3$: every member has a linearly stable block with
attractive gravity (check `block_stable_family`); UM-2 uses $w_{\mathrm{stab}} = 1$.

## IN-5: the dirac16complex field

@@IN-5@@

**Origin (RECORD).** The record's Dirac-type Lagrangian (section 5) with the author's form of the mass, $m_\Psi = 3H\mathcal{M}$,
and the record's value $\mathcal{M} = 1/3$, which UM-2 keeps (ASSUMED). The contact self-coupling $\lambda$ is the record's;
UM-2 does not fix it: the Kohn-Sham machinery is tested with $\lambda = 0$ and $\lambda = \pm7\times10^{-5}H^{-6}$, and the
fold-band radiation of the self-interaction channel (FE-135, FE-136) requires $\lvert\lambda\rvert \le 1.4\times10^{-10}H^{-6}$
for the coordinate volume $v_{\mathrm{t}} = H^{-3}$ of the extra times (ASSUMED bound; corrections, item 24).

## IN-6: the Clifford algebra, the Dirac adjoint and the two halves of dirac16complex

@@IN-6@@

**Origin (AUTHOR).** The author's real $16\times16$ matrices of section 4 and the matrices $C$, $\Gamma_4$, $\mathcal{B}$ derived
from them. The Clifford algebra, the reality, $C^T = C$ and $C^2 = \mathbf{1}$, the antisymmetry of $C\gamma^a$, the
irreducibility of the 16-dimensional representation of Pin(4,4), the two inequivalent halves of Spin(4,4) and the block forms
are verified exactly (`um2_algebra.py`, 31 checks). The halves $\Psi_A$ and $\Psi_B$ are the eigenspaces of $\mathcal{B}$;
$\mathcal{B}$ commutes with every interaction of the good sector, so the numbers of quanta of the two halves are conserved
separately (computed with the author's matrices: `um2_analysis.py`, check `B5_stability_and_neutrality`;
`um2_electroweak.py`, checks `B_lorentz_invariant`, `Gamma4_equals_minus_B_gamma0`).

## IN-7: the canonical spin connection

@@IN-7@@

**Origin (STANDARD; chosen by the record).** The canonical (vielbein-postulate, torsion-free) spin connection, the standard
coupling of a spinor to gravity, chosen by the record instead of the notebook's contraction of the mixed connection
coefficients (section 5); the order of 2026-10-17 asks for a non-trivial canonical spin connection. On the order-0 metric
it makes $\gamma^N$ covariantly constant, gives FE-13 and vanishes only in flat 4+4 space (`um2_geometry.py`, checks
`gamma_covariantly_constant`, `gamma_mu_Omega_mu`, `nontrivial_unless_flat`).

## IN-8: the gauge fields in eight dimensions

@@IN-8@@

**Origin (ASSUMED structure; STANDARD form).** The gauge group of the Standard Model, $SU(3)_c\times SU(2)_L\times U(1)_Y$, in
eight dimensions with the standard Yang-Mills action in the geometric normalisation (the couplings $1/\hat g_i^2$ in front
of the kinetic terms). The gauge structure is that of QCD and of the electroweak model; the zero modes of the gauge fields
are flat in $x_0$ and are the four-dimensional gauge fields with the couplings $g_i^2 = \hat g_i^2/V_\perp$ (FE-49). The
gluons and the photon stay exactly massless (`um2_spectra.py`, check `massless_zero_mode`).

## IN-9: the field strengths

@@IN-9@@

**Origin (STANDARD).** The field strengths of the three gauge groups.

## IN-10: the physical electroweak fields

@@IN-10@@

**Origin (STANDARD).** The physical electroweak fields of the Standard Model, canonically normalised. $W^+$ carries the
electric charge $+e$ and $W^-$ the charge $-e$; $W^-$ is the antiparticle of $W^+$ (DERIVED: `um2_electroweak.py`, check
`W_charges`; the author's order "the W+ and W- bosons carry positive and negative electric charges. Do not forget this").
The angle of the couplings is fixed by the measured $W$ and $Z$ masses with the measured electroweak parameter (FE-55).

## IN-11: the Standard-Model fermions of three generations

@@IN-11@@

**Origin (ASSUMED).** Three generations of quarks and leptons (the author's choice (A) of 2026-10-18), each multiplet a
16-component spinor of the same Clifford algebra times its gauge indices, with bulk masses; one doublet bulk mass per
sector, $\mu_Q$ and $\mu_\ell$ (ASSUMED), and right-handed neutrinos $\nu_{Ri}$ for the Dirac masses of the neutrinos in the
$x_0$ mechanism (ASSUMED; the Majorana alternative without them is analysed). The hypercharges are those of the Standard
Model ($\frac16$, $\frac23$, $-\frac13$, $-\frac12$, $-1$, $0$ for $Q$, $u_R$, $d_R$, $\ell$, $e_R$, $\nu_R$), and every
generation is anomaly free (DERIVED: `um2_electroweak.py`, check `anomaly_cancellation`). The neutrinos of the lepton
doublets are the weak partners of the charged leptons (the flavours $\nu_e$, $\nu_\mu$, $\nu_\tau$), not the mass states
$\nu_1$, $\nu_2$, $\nu_3$.

## IN-12: the covariant derivative of a fermion and the electric charge

@@IN-12@@

**Origin (STANDARD).** The covariant derivative of the Standard Model with the spin connection; the electric charge
$Q_{\mathrm{em}} = T_3 + Y$ in every generation (`um2_electroweak.py`, checks `electric_charges`, `photon_coupling`,
`Z_coupling`).

## IN-13: the tip sigma field and the tip Yukawa couplings (no Higgs particle)

@@IN-13@@

**Origin (INVENTED for this geometry).** *Reason.* The orders exclude the Higgs particle, but $W^+$, $W^-$ and $Z$ are massive
and the quarks and leptons need their masses and mixing. UM-2 breaks the electroweak symmetry without a Higgs particle by a
unitary sigma field $\Sigma$ ($\Sigma^\dagger\Sigma = \mathbf{1}$: three Goldstone modes, which become the longitudinal
$W^+$, $W^-$ and $Z$, and no physical scalar) that lives only on the tip $y = -L$ of the $x_0$ cell. The concepts of
symmetry breaking by a non-linear sigma field and of fermion localisation in an extra dimension are STANDARD; their
realisation in this geometry is INVENTED. The tip Yukawa couplings $\mathcal{Y}_\nu$, $\mathcal{Y}_e$, $\mathcal{Y}_u$,
$\mathcal{Y}_d$ couple the doublets and the singlets at the tip; on the zero modes they become the tip mixing conditions
FE-30, whose tip matrices are the PMNS and the CKM matrices (ASSUMED values). *Consistency with the electroweak model and
QCD.* Every tip term is invariant under $SU(2)_L\times U(1)_Y$ for arbitrary complex tip matrices (DERIVED with random group
elements, deviation $1.1\times10^{-14}$: `um2_fields.py`, check `tip_terms_gauge_invariant`) and is a colour singlet; the
custodial symmetry of the sigma-field term gives $\rho_{\mathrm{EW}} = 1$ at leading order (`um2_spectra.py`, check
`custodial_leading_order`); the photon receives no tip term (IN-15). *Conflicts with data* (inherent in the specified
content, stated in every version): there is no Higgs boson, while one is observed at 125 GeV; without it the scattering of
longitudinal $W^+$ and $W^-$ violates perturbative unitarity near 1.2 TeV, far below the Kaluza-Klein scale of 121 TeV.

## IN-14: the covariant derivative of the sigma field and its gauge transformation

@@IN-14@@

**Origin (INVENTED).** The covariant derivative of the sigma field with the gauge transformations of the electroweak model
($U_L$ an $SU(2)_L$ matrix, $U_Y$ the hypercharge rotation by the angle $\vartheta$); with it every tip term is gauge
invariant (DERIVED, as for IN-13; the hypercharge phase of a fermion is $\psi \to \mathrm{e}^{\mathrm{i}Y\vartheta}\psi$,
corrections, item 1).

## IN-15: the tip mass term of $W^+$, $W^-$ and $Z$

@@IN-15@@

**Origin (DERIVED).** The sigma-field term of IN-13 in the unitary gauge: $W^+$ and $W^-$ share one mass (particle and
antiparticle), and the photon, the combination without a tip term, stays massless. On the static block the term becomes
the Robin condition FE-51 of the boson profiles (`um2_fields.py`, check `gauge_boundary_conditions`; `um2_spectra.py`,
checks `rho_fit`, `mZ_reproduced`). Its sign is that of the signature $(+,+,+,-)$ of $x_1, \dots, x_4$ (corrections, item 12).

## IN-16: portal I11, the vector contact portal to the $B - L$ currents

@@IN-16@@

**Origin (INVENTED; version 1, with its charges fixed in version 3).** *Reason.* A contact coupling of the conserved vector
current of the gauge-singlet field $\Psi$ to a gauge-invariant conserved current of all quarks and leptons, so that
dirac16complex feels every Standard-Model fermion. *Consistency with QCD and the electroweak model.* Both currents are singlets
of $SU(3)_c\times SU(2)_L\times U(1)_Y$; the $B - L$ charge is flavour universal and conserved by every interaction of the
Standard Model (STANDARD; with the right-handed neutrinos it is free of anomalies), so the portal breaks no gauge symmetry and
leaves the Standard-Model interactions unchanged; the currents are the Hermitian currents $\mathrm{i}\bar\Psi\gamma^M\Psi$ and
$\mathrm{i}\bar\psi\gamma_M\psi$ (corrections, item 13). Its effects on the Standard Model are mean fields of relative size
$10^{-17}$ at most in the fermion equations FE-14 to FE-19. *Strength.* On the zero modes it is the contact interaction FE-70
with $G_{\mathrm{V}} = c_{\mathrm{V}}H/(2f^4v_{\mathrm{t}}\Lambda_\star^6)$, set to the benchmark
$G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$, at which the freeze-in of the fold bands from the highest temperature
$T_{\mathrm{max}} = 10$ TeV adds $\Delta N_{\mathrm{eff}} = 0.001$ (both ASSUMED; FE-129). Version 2 had left the charges
general and set $c_{\mathrm{V}} = 0$.

## IN-17: portal I12, the gauge-kinetic scalar portal

@@IN-17@@

**Origin (INVENTED; version 1).** *Reason.* The coupling of the scalar density $\bar\Psi\Psi$ to the gauge-invariant kinetic
densities of the gluons and of the electroweak fields: the gauge-singlet field couples to the gauge bosons of all three
groups, its density makes the gauge couplings field dependent (FE-21), and the dark matter can annihilate into gauge bosons.
*Consistency with QCD and the electroweak model.* $G^A_{MN}G^{AMN}$, $W^I_{MN}W^{IMN}$ and $B_{MN}B^{MN}$ are gauge invariant
(the first is the operator of the QCD trace anomaly), so the portal preserves $SU(3)_c\times SU(2)_L\times U(1)_Y$ and keeps
the photon and the gluons exactly massless (`um2_coupled.py`, check `C5_WZ_and_photon`); the shifts of the couplings are at
most $1.7\times10^{-16}$ (FE-79). The power of the scale is $\Lambda_\star^3$ in the geometric normalisation (corrections,
item 10). *Strength.* The unitarity-safe benchmark $G_{\mathrm{I12}} = \pi/(2M_{\mathrm{DM}}^3)$ with the universal
coefficients $c_{\mathrm{G}} = c_{\mathrm{W}} = c_{\mathrm{B}} = c_{\mathrm{I12}}$ (ASSUMED; FE-127, FE-128). Version 2 found
that I12 alone cannot give the relic abundance within perturbative unitarity, because the operator annihilates a pair only
from the state $^3P_0$ (corrections, item 22); this led to I13.

## IN-18: portal I13, the $x_0$-chiral vector portal to the baryon-number current

@@IN-18@@

**Origin (INVENTED; version 3).** *Reason.* An s-wave annihilation of the dark matter into quarks, which gives the relic
abundance within partial-wave unitarity (FE-126 to FE-128). The $x_0$-chiral current $\mathrm{i}\bar\Psi\gamma^MP_b\Psi$ was
chosen because it is Hermitian for the seven directions $M \ne x_0$ (for $M = x_0$ the Hermitian conjugate of
$\mathrm{i}C\gamma^{x_0}P_b$ is $\mathrm{i}C\gamma^{x_0}P_a$, so the sum leaves that direction out; corrections, item 24), is
a four-dimensional vector, is diagonal in the halves on the zero modes and vanishes on the fold bands (to
$7\times10^{-14}$), so it cannot produce dark radiation; the baryon-number current was chosen because the $B - L$ current would
thermalise the right-handed neutrinos and add $\Delta N_{\mathrm{eff}} = 0.144$ (FE-131; corrections, item 23). *Consistency
with QCD and the electroweak model.* The baryon current is a colour singlet, flavour universal and invariant under
$SU(2)_L\times U(1)_Y$, and it is conserved in perturbation theory (STANDARD; its electroweak anomaly acts only through
non-perturbative processes); the algebra of the bilinear with the author's matrices is exact (`um2_coupled.py`, check
`C8_I13_algebra`). *Strength.* $G_{\mathrm{A}} = c_{\mathrm{A}}H/(2f^4v_{\mathrm{t}}\Lambda_\star^6) = 1.278\times10^{-9}$
GeV$^{-2}$, DERIVED from $\Omega_{\mathrm{DM}}h_{100}^2 = 0.120$; its physics accuracy is about 1 % (section 10).

## Removed and rejected operators

Removed in version 2 (corrections, item 21): the chiral tip $Z$ portal I9 of version 1,

$$
S_{\mathrm{I9}} = \int_{y=-L}\mathrm{d}^7X_{\mathrm{tip}}\sqrt{\lvert g_{\mathrm{tip}}\rvert}\;
 \big(c_{\mathrm{Z}} + \tilde c_{\mathrm{Z}}\,\varsigma_{\mathrm{t}}\big)\big(\mathrm{i}\bar\Psi\gamma^\mu P_L\Psi\big)\,
 \frac{\mathrm{i}v_\Sigma^2}{2}\,\mathrm{tr}\big(\Sigma^\dagger D_\mu\Sigma\,\tau^3\big),\qquad
c_{\mathrm{Z}} = \tilde c_{\mathrm{Z}} = 0
$$

<!-- symbols: mod_SI9, ycoord, Lcut, diff, Xtip, gtip, mod_cZ, mod_varsigmat, imag, Psi, gamma, imu, PLR, iL, vSigma, trace, Sigma, dagger, Dcov, tau -->

With three neutrinos it has no role left: its even part is bounded by the invisible width of the $Z$, and its oriented part
would thermalise the fold band of $\Psi_A$ (item 21); setting both coefficients to zero is a modelling choice (ASSUMED; item
22). Considered and rejected: a dipole portal $\bar\Psi\mathcal{S}^{MN}\Psi B_{MN}$ (it would thermalise the sterile fold
bands through the photon: too much dark radiation) and any operator coupling the neutral $\Psi$ to a single $W^+$ or $W^-$
(none is gauge invariant).

## Parameter choices (ASSUMED)

$HL = 3$ and $m_\Psi = H$ (from the record); the tip mixing $\mathcal{K} = 1$ of one generation, i.e. unitary tip matrices of
three generations with $\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}$, $\mathcal{K}_\nu = U$, $\mathcal{K}_d = V_{\mathrm{CKM}}$;
the doublet localisation $c_L$ of each sector fixed by its heaviest member ($c_R = -c_L$ for the tau and for the top quark);
the lightest neutrino mass $m_1 = 1$ meV and the normal ordering; the Kohn-Sham test value of the self-coupling,
$\lambda_{\mathrm{test}} = 7\times10^{-5}H^{-6}$ (mean fields below 5 % of $m_\Psi$ in the densest test state; it is only
the value with which the Kohn-Sham machinery is tested); the coordinate volume $v_{\mathrm{t}}$ of the extra times (it enters
only $V_\perp$ and the conversion of $c_{\mathrm{V}}$, $c_{\mathrm{A}}$ and $\lambda$ into $G_{\mathrm{V}}$, $G_{\mathrm{A}}$
and $G_\lambda$). Version 3: the I11 strength $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$ and the highest temperature
$T_{\mathrm{max}} = 10$ TeV of the hot Universe; the I12 strength $G_{\mathrm{I12}} = \pi/(2M_{\mathrm{DM}}^3)$ with universal
coefficients (chosen to respect the $^3P_0$ unitarity bound up to $E_{\mathrm{cm}} = 2.4M_{\mathrm{DM}}$); the bound
$G_\lambda = \lambda H\tilde I_\lambda/(2f^4v_{\mathrm{t}}) \le 2.3\times10^{-15}$ GeV$^{-2}$ on the self-interaction channel
(from $\Delta N_{\mathrm{eff}} \le 0.001$; item 24). The I13 strength is not a choice: it is DERIVED from the relic density.

