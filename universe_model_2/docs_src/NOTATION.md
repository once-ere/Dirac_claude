# UM-2 version 4: notation

This file records the notation of the version-4 documents of UM-2 (rule S2 of `STYLE_V4.md`: one symbol, one meaning).
Every symbol of the field equations has one entry in the registry `docs_src/symbols/core.json` (the key is given in the
tables below); the inventory of the field equations and interaction terms is `docs_src/equations.json` (FE-1 to FE-136,
IN-1 to IN-18). When text of version 3 is reused, it is translated with the table of section 3.

## 1. General conventions

**Typography.** Euler's number is `\mathrm{e}` ($\mathrm{e}^{2a_4}$), the imaginary unit `\mathrm{i}`, the differential
`\mathrm{d}` ($\mathrm{d}x_0$, $\mathrm{d}f/\mathrm{d}x_4$). A word or a particle name in a subscript or superscript is
upright: $M_{\mathrm{eff}}$, $M_{\mathrm{Pl}}$, $\delta_{\mathrm{tip}}$, $m_{\mathrm{W}}$, $n_{\mathrm{e}}$, $m_{\mathrm{s}}$ (the
strange quark), $T_{\mathrm{c}}$. An italic letter in a subscript or superscript is an index (section 4): $m_s$ is the mass of the
species $s$, $m_{\mathrm{s}}$ the mass of the strange quark. Names of portals are upright (I11, I12, I13, $S_{\mathrm{I11}}$).

**Coordinates.** The author's coordinates $X = \{x_0, x_1, \dots, x_7\}$, always with the hidden direction first: $x_0$ the
hidden space-like direction (period $\pi/(6H)$, angle variable $z = 6Hx_0$, chart $y = \ln\lvert\sin z\rvert/(6H)$,
$\xi = y/L$), $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the three extra times. There is no $x_8$. Signature
$(+,+,+,+,-,-,-,-)$ in this order; the four observable coordinates $x_1, \dots, x_4$ have the signature $(+,+,+,-)$.

**Derivatives and marks.** A dot is $\mathrm{d}/\mathrm{d}x_4$. A prime is used only in the cosmological perturbation equations, as
$\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$ (conformal time); a derivative with respect to $\xi$ is always written
$\mathrm{d}/\mathrm{d}\xi$. $\Delta$ is a change (first-order perturbation, level shift, difference: $\Delta K$, $\Delta\rho$,
$\Delta\varepsilon_o$, $\Delta m_{21}^2$); $\delta$ is the Kronecker delta (and its generalisation); $\delta_{\mathrm{D}}$ is the
Dirac delta function; $\Delta_{ij}$ (with its two indices) is the oscillation phase of neutrinos.

**Units and normalisations.** Natural units $\hbar = c = 1$. In eight dimensions $[\Psi] = [\psi] = \mathrm{GeV}^{7/2}$,
$[\kappa] = \mathrm{GeV}^{-6}$, $[\lambda] = \mathrm{GeV}^{-6}$. The gauge fields $G$, $W$, $B$ are in the geometric normalisation
(the couplings $1/\hat g_i^2$ stand in front of the kinetic terms, $[G_M] = \mathrm{GeV}$, $[\hat g_i] = \mathrm{GeV}^{-2}$), in eight
and in four dimensions alike (the gauge zero modes are flat in $x_0$, so $G^A_{\mu\nu}$ is the same field); the four-dimensional
couplings are $g_i^2 = \hat g_i^2/V_\perp$. The physical electroweak fields $W^\pm$, $Z$, $A$ and the massive-vector field
strength $F^V_{\mu\nu}$ are canonically normalised (divided by the coupling), and the I12 couplings $G_{\mathrm{g}}$,
$G_{\mathrm{W}}$, $G_{\mathrm{B}}$ refer to canonically normalised gauge fields. (Version 3 wrote both normalisations with the same
letters.) The overlap integrals $\tilde I_{of}$, $\tilde I^{(b)}_{of}$, $\tilde I_\lambda$ carry the factor $1/H$ explicitly, so
they are dimensionless (version 3: "in units of $H$").

**Physics conventions.** $W^+$ carries the electric charge $+e$ and $W^-$ the charge $-e$ ($W^\pm = (W^1 \mp \mathrm{i}W^2)/
(\sqrt2\,\hat g_2)$). There is no Higgs particle: the tip sigma field $\Sigma$ (unitary, $\Sigma^\dagger\Sigma = \mathbf{1}$) gives the
$W^\pm$ and $Z$ masses and the tip Yukawa terms. $\kappa = 8\pi G_8$ always. $H$ is always the author's constant
(14.296 TeV); the Hubble rate is $\mathcal{H}$ ($= \dot a_4$), its value today $\mathcal{H}_0$. The identity matrix is $\mathbf{1}$.

**Glyph variants are different symbols.** $\varepsilon$ (energy of a mode) and $\epsilon$ (bookkeeping parameter of the metric
series); $\rho$ (energy density) and $\varrho$ (profile density of a zero mode); $\sigma$ (cross-section; $\sigma_1, \sigma_2,
\sigma_3$ the Pauli matrices of a block) and $\varsigma$ (block sign); $\theta$ (mixing angle) and $\vartheta$ (U(1)$_Y$ gauge
parameter); $\pi$ and $\varpi$ ($x_0$ wave number); $\phi$ (Kohn-Sham occupation) and $\Phi$ (lapse potential); $\varphi$ is not
used.

## 2. Main decisions

* The block variable $1/f^2$ is $K$ (was $k$); $k$ is only a wave number (momentum).
* The Hubble rate is $\mathcal{H}$, the rate of the block scale $\mathcal{H}_f = \dot f/f$ (were $H$ or $A$, and $h$).
* The Lovelock order is the index $p$ in brackets: $\alpha_{(p)}$, $w_{(p)}$, $\mathcal{L}_{(p)}$, $\mathcal{E}_{(p)}$ (was $k$).
* The energy-momentum tensor is $\mathcal{T}^M{}_N$ (was $T$), because $T$ is the temperature; the pressure of the extra times is
  $p_5$ (was $p_t$); the stabiliser density is $\rho_{\mathrm{stab}}$ (was $\rho_b$, which is now the baryon density).
* The gauge couplings are $g_3, g_2, g_1$ in four dimensions and $\hat g_3, \hat g_2, \hat g_1$ in eight (were $g_s$, $g$, $g'$),
  so that $g$ is only the metric; $\alpha_3, \alpha_2, \alpha_1$ the corresponding fine-structure constants, $\alpha_{\mathrm{em}}$
  the electromagnetic one.
* The tip mixing matrices are $\mathcal{K}$, $\mathcal{K}_\nu$, $\mathcal{K}_e$, $\mathcal{K}_u$, $\mathcal{K}_d$ (were $\kappa_f$,
  $\kappa_\nu$, ...), the tip Yukawa matrices of the action $\mathcal{Y}_\nu$, $\mathcal{Y}_e$, $\mathcal{Y}_u$, $\mathcal{Y}_d$
  (were $\lambda_\nu$, ... in $\Lambda_\ell$, $\Lambda_q$); $\kappa$ and $\lambda$ keep their main meanings.
* The scalar density of dirac16complex is $n^{\mathrm{sc}}$ (was $S$, $s_o$, $s_{DM}$, $s_{DF}$); $s$ is only the entropy density.
* The mass parameter of dirac16complex is $m_\Psi$ (was $m$), the record's dimensionless parameter $\mathcal{M}$ (was $M$).
* The four-dimensional dark-matter and fold-band fields are $\Psi_{\mathrm{DM}}$, $\Psi_{\mathrm{fold}}$, $\Psi_o$ (were $\chi$);
  $\chi$ is only the two-component block spinor.
* The dimensionless $x_0$ eigenvalue of a boson is $\tilde m^2 = (m\,fL)^2$ (was $\Lambda$), its wave number $\varpi$ (was $q$ or
  $p\,fL$), the profiles $F$, $F_n$ (were $u$, $u_n$).
* The Newtonian-gauge potentials are $\Phi$ (lapse) and $\Psi_{\mathrm{N}}$ (curvature) with the factor $\epsilon$ absorbed (were
  $\psi = \epsilon\Phi$, $\phi = \epsilon\Psi_N$); $\Psi_{\mathrm{N}}$ is not related to the field $\Psi$.

## 3. Version-3 symbols with more than one meaning, and their version-4 symbols

| version 3 | meaning in version 3 | version 4 | key |
| --- | --- | --- | --- |
| $a$ | scale factor $\mathrm{e}^{a_4}$ | $\mathrm{e}^{a_4}$ (written out) | `a4` |
| $a$ | $3\eta/2$ in the boson $x_0$ problem | $3HL/2$ (written out) | `Hconst`, `Lcut` |
| $a$, $b$ ($a_o$, $a_L$, $b_R$, ...) | components of a block spinor $(a, \mathrm{i}b)$ | $a$, $b$ (unchanged) | `ab` |
| $a_D$, $b_D$, $a_F$, $b_F$ | components of the dark-matter and fold orbitals | $a_{\mathrm{DM}}$, $b_{\mathrm{DM}}$, $a_{\mathrm{fold}}$, $b_{\mathrm{fold}}$ | `abDM`, `abfold` |
| $\mathcal{A}$, $\mathcal{B}$ | doublet and singlet amplitudes (three generations) | $\boldsymbol{\alpha}$, $\boldsymbol{\beta}$ | `bsalpha`, `bsbeta` |
| $A$ | expansion rate $\dot a_4$ | $\mathcal{H}$ | `Hubble` |
| $A$ | photon field | $A$ (unchanged) | `Aphoton` |
| $B$ | the author's operator $-\mathrm{i}C\gamma^{x_4}$ | $\mathcal{B}$ | `calB` |
| $B$ | hypercharge field | $B$ (unchanged) | `Bhyp` |
| $b$, $b_i$ | one-loop coefficients of the couplings | $b_3$, $b_2$, $b_1$, $b_{\mathrm{G}}$ | `bcoef` |
| $\beta$ | Robin parameter of a boson profile | $\beta$, $\beta_{\mathrm{W}}$, $\beta_{\mathrm{Z}}$ (unchanged) | `betaRobin`, `betaW`, `betaZ` |
| $\beta$ | velocity in the centre-of-mass frame | $\beta_{\mathrm{cm}}$ | `betacm` |
| $c$ ($c_L$, $c_R$, $c_Q$, $c_\psi$) | localisation $f\mu L$ | $c$, $c_L$, $c_R$; $c_\Psi$ for dirac16complex | `cloc`, `cPsi` |
| $c_{ij}$ | $\cos\theta_{ij}$ | $c_{ij}$ (unchanged) | `cij` |
| $c_V$, $c_A$, $c_G$, $c_W$, $c_B$ | portal coefficients | $c_{\mathrm{V}}$, $c_{\mathrm{A}}$, $c_{\mathrm{G}}$, $c_{\mathrm{W}}$, $c_{\mathrm{B}}$, $c_{\mathrm{I12}}$ | `cV`, ... |
| $C$ | Dirac-adjoint matrix $\gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}$ | $C$ (unchanged) | `Cmat` |
| $C$ | $\cosh w$ in the mass condition | written out | |
| $D(e)$ | mass function of one generation | $\mathcal{D}(\tilde\varepsilon)$ | `calD` |
| $D(1)$, $g(0)$ | growth factor | $D_+$ | `Dplus` |
| $\delta$ | variation or perturbation ($\delta k$, $\delta\rho$, $\delta\ln f$, $\delta\varepsilon$) | $\Delta$ | `Delta` |
| $\delta$ | Kronecker delta | $\delta$ (unchanged) | `delta` |
| $\delta(y + L)$ | Dirac delta function | $\delta_{\mathrm{D}}(y + L)$ | `deltaD` |
| $\delta$ | $\frac13\mathrm{d}\ln g_s/\mathrm{d}\ln T$ | written out | |
| $\delta_c$, $\theta_c$ | dark-matter perturbations | $\delta_{\mathrm{DM}}$, $\theta_{\mathrm{DM}}$ | `deltaDM` |
| $d$ | differential | $\mathrm{d}$ | `diff` |
| $e$ | Euler's number | $\mathrm{e}$ | `euler` |
| $e$ | elementary charge | $e$ | `eel` |
| $e$ | electron | upright $\mathrm{e}$ in names ($m_{\mathrm{e}}$, $n_{\mathrm{e}}$, $\rho_{\mathrm{e}}$); italic $e$ as a value of the flavour index | `ie` |
| $e$ | dimensionless fermion eigenvalue $\varepsilon fL$ | $\tilde\varepsilon$ | `epstilde` |
| $e$ | amplitude of the I12 mean field in the $W$, $Z$ problem | $A_{\mathrm{mf}}$ | `Amf` |
| $E_{(k)}$ | Lovelock tensors | $\mathcal{E}_{(p)}$ | `LovE` |
| $E_i$ | comoving energy of a neutrino | $E^{\mathrm{c}}_i$ | `Ec` |
| $\epsilon$, $\varepsilon$ | series parameter; energy of a mode | $\epsilon$; $\varepsilon$ | `epsser`; `varepsilon` |
| $\eta$ | $HL$ | $HL$ (written out) | |
| $f$ | block scale | $f$ (unchanged) | `fblock` |
| $f_o$ | occupation of an orbital | $\phi_o$ | `phiocc` |
| $f$ (in $S_f$, $T[f]$) | the Standard-Model fermions | upright: $S_{\mathrm{f}}$, $\mathcal{T}_{\mathrm{f}}$ | `Sf`, `Tf` |
| $\bar f_\nu$ | relic-neutrino distribution | $f_{\mathrm{FD}}$ | `fFD` |
| $F$ | field strength | $F^V_{\mu\nu}$ (massive vector), $F_{\mathrm{geo}}$ (geometric) | `FV`, `Fgeo` |
| $F(T_1, T_2)$ | energy-transfer kernel | $\mathcal{F}_{\mathrm{tr}}(T_{\mathrm{A}}, T_{\mathrm{B}})$ | `Ftr`, `TAB` |
| $g$ | metric | $g_{MN}$ (unchanged) | `metric` |
| $g$ | degeneracy of a momentum shell; internal states of a particle | $d_o$; $d_s$ | `ddeg` |
| $g$, $g'$, $g_s$; $\hat g$, $\hat g'$, $\hat g_s$ | gauge couplings | $g_2$, $g_1$, $g_3$; $\hat g_2$, $\hat g_1$, $\hat g_3$ | `g2`, `ghat2`, ... |
| $g_i$ | gauge couplings | $g_3$, $g_2$, $g_1$; generic $g_{\mathrm{G}}$ | `gG` |
| $g_*$ | degrees of freedom of the energy density | $g_\rho$ | `grho` |
| $G(k)$ | Einstein-Hilbert coefficient of the block | $\mathcal{G}(K)$ | `GK` |
| $G(u)$ | electron-lepton-number distribution | $G_{\mathrm{ELN}}(u)$ | `GELN` |
| $G$, $G_i$ | total and partial I12 strengths | $G_{\mathrm{I12}}$; $G_{\mathrm{g}}$, $G_{\mathrm{W}}$, $G_{\mathrm{B}}$ | `GI12`, `Gg`, ... |
| $G$ | dark-matter coupling of one $\nu_R$ | $G_\nu$ | `Gnu` |
| $G^\alpha$, $T^\alpha$ | gluon field, colour generators | $G^A$, $t^A$ | `Ggluon`, `tgen` |
| $\gamma$ | rate density (freeze-in, $\nu_R$ production) | $\Gamma_{\mathrm{fi}}$, $\Gamma_\nu$ | `Gammafi`, `Gammanu` |
| $h$ | rate of the block scale $\dot f/f$ | $\mathcal{H}_f$ | `Hf` |
| $h_j$ | block Hamiltonian | $h$ (the block sign $\varsigma$ inside) | `hblock` |
| $h$ | reduced Hubble constant | $h_{100}$ | `h100` |
| $H$ | the author's constant | $H$ (unchanged) | `Hconst` |
| $H$, $H_0$ | Hubble rate (decoupling, relic), Hubble constant | $\mathcal{H}$, $\mathcal{H}_0$ | `Hubble`, `H0` |
| $\mathcal{H}$ | conformal Hubble rate (perturbations) | $a_4'$ | `a4`, `prime` |
| $i$, $j$ | 3-space indices of the background curvatures | the coordinates written out ($R^{x_1x_2}{}_{x_1x_2}$) | `Riemann` |
| $j$ | block sign | $\varsigma$ (with $\varsigma_2$, $\varsigma_3$, were $s_2$, $s_3$) | `varsigma`, `varsigma2` |
| $J$ | Jarlskog invariant | $J_{\mathrm{CP}}$ | `JCP` |
| $J$ | block operator $\gamma^{x_0}\gamma^{x_1}\gamma^{x_4}$ | written out | |
| $J$ | total angular momentum of a partial wave | in words | |
| $k$ | block variable $1/f^2$ ($k_*$, $k_\pm$) | $K$, $K_*$, $K_\pm$ | `Kblock`, `Kstar`, `Kpm` |
| $k$ | Lovelock order ($\alpha_k$, $w_k$, $\mathcal{L}_{(k)}$) | index $p$: $\alpha_{(p)}$, $w_{(p)}$, $\mathcal{L}_{(p)}$ | `ip` |
| $k$ | momentum of a mode, comoving wave number | $k$ (unchanged) | `kwave` |
| $\Delta k$ | spacing of the momentum lattice | $k_{\mathrm{lat}}$ | `klat` |
| $K_{ij}$, $K_{i4}$, ... | sectional curvatures | $R^{ab}{}_{ab}$ | `Riemann` |
| $K_1$, $K_2$ | Bessel functions | $K_1$, $K_2$ (unchanged; not the block variable) | `Kbessel` |
| $\kappa$ | $8\pi G_8$ | $\kappa$ (unchanged) | `kappa` |
| $\kappa_f$, $\kappa_\nu$, $\kappa_e$, $\kappa_u$, $\kappa_d$ | tip mixing matrices | $\mathcal{K}$, $\mathcal{K}_\nu$, $\mathcal{K}_e$, $\mathcal{K}_u$, $\mathcal{K}_d$ | `Ktip` |
| $L$ | depth of the tip | $L$ (unchanged) | `Lcut` |
| $L_i$, $\ell_{Rj}$, $q_{Rj}$ | lepton doublet, singlets | $\ell_i$; $e_{Rj}$, $\nu_{Rj}$; $u_{Rj}$, $d_{Rj}$ | `ldoublet`, `eR`, `nuR`, `uR`, `dR` |
| $L$ | baseline of a neutrino | $L_{\mathrm{b}}$ | `Lb` |
| $\lambda$ | contact self-coupling | $\lambda$ (unchanged) | `lambda` |
| $\lambda_\nu$, $\lambda_e$, $\lambda_u$, $\lambda_d$ ($\Lambda_\ell$, $\Lambda_q$) | tip couplings of the action | $\mathcal{Y}_\nu$, $\mathcal{Y}_e$, $\mathcal{Y}_u$, $\mathcal{Y}_d$ | `Yuk` |
| $\Lambda$ | eight-dimensional cosmological constant | $\Lambda$ (unchanged) | `Lambda` |
| $\Lambda$ | dimensionless $x_0$ eigenvalue $(m\,fL)^2$ | $\tilde m^2$ ($\tilde m_{\mathrm{W}}^2$, $\tilde m_{\mathrm{Z}}^2$) | `mtilde`, `mtildeW` |
| $\Lambda^{(n_f)}$ | QCD scale | $\Lambda_{\mathrm{QCD}}^{(N_{\mathrm{f}})}$ | `rhoQCDscale` |
| $\Lambda^0$, $\Lambda^3$ | fast-flavour potentials | $\mathcal{I}_0$, $\mathcal{I}_1$ | `calI` |
| $m$ | mass parameter of dirac16complex | $m_\Psi$ | `mPsi` |
| $M$ | the record's mass parameter ($m = 3HM$) | $\mathcal{M}$ | `calM` |
| $M$ | mass function $M(y)$ | $M(y)$ (unchanged) | `Mfun` |
| $M$ | static source mass; dark-matter mass | $M_1$, $M_2$; $M_{\mathrm{DM}}$ | `M12`, `MDM` |
| $\mu$ | bulk mass ($\mu_\psi$, $\mu_L$, $\mu_Q$) | $\mu_{\psi i}$, $\mu_\ell$, $\mu_Q$ | `mubulk`, `muell`, `muQ` |
| $\mu$ | chemical potential (Mermin) | $\mu_{\mathrm{chem}}$ | `muchem` |
| $\mu_R$ | renormalisation scale | $\mu_{\mathrm{ren}}$ | `mu_ren` |
| $\mu$ | $\sqrt2G_Fn_{\nu_e}$ | written out | |
| $\mu$ | the muon | the flavour value $\mu$ in $\nu_\mu$, $U_{\mu 3}$, $V_\mu$, $T_{\nu_\mu}$ (registered names) | `nuflav`, `Upmns`, `Vmat`, `Tnua` |
| $n$ | number density | $n$ (unchanged) | `ndens` |
| $n$ | level number of the tower | index $n$ | `in` |
| $n_f$, $n_W$ | numbers of flavours, of Weyl species | $N_{\mathrm{f}}$, $N_{\mathrm{W}}$ | `Nf`, `NW` |
| $n_\chi$, $n_{\bar\chi}$, $n$ (dark matter) | densities of one species; of the two species together | $n_{\mathrm{DM}}$, $\bar n_{\mathrm{DM}}$ (one species); $n_{\mathrm{DM,tot}} = 2(n_{\mathrm{DM}} + \bar n_{\mathrm{DM}})$ | `nDM`, `nDMtot` |
| $\sum_{A,B}$ | sum over the two dark-matter species | the factor 2 | |
| $N_\chi$, $N_F$ | number of fold bands | $N_{\mathrm{fold}}$ | `Nfold` |
| $p$ | pressure ($p_0$, $p_3$, $\bar p$) | $p$ (unchanged) | `pressure`, `p0`, `p3`, `pbar` |
| $p_t$ | pressure of the extra times | $p_5$ | `p5` |
| $p_2^{(i)}$ | order-$\alpha$ pressure of a gauge plasma | $p_{\alpha,\mathrm{G}}$, $p_{\alpha,2}$, $p_{\alpha,1}$ | `palpha` |
| $p$ | momentum of a neutrino; integration variable of the gas integrals | $k$ | `kwave` |
| $p$ | hidden wave number of a level ($p\,fL = 1.899$) | $\varpi/(fL)$ | `varpi` |
| $p$ | centre-of-mass momentum | $k_{\mathrm{cm}}$ | `kcm` |
| $P$ | weight $\mathrm{e}^{-3Hy}/\mathrm{Vol}_7$ | written out | |
| $P_\pm$ | four-dimensional chiral projectors | $P_L$, $P_R$ | `PLR` |
| $\mathcal{P}(k)$ | primordial spectrum | $P_{\mathcal{R}}(k)$ | `PR` |
| $q$ | wave number of a boson profile | $\varpi$ | `varpi` |
| $q$ | comoving momentum of a neutrino | $k_\nu$ | `knu` |
| $Q$ | neutron-proton mass difference | $m_{\mathrm{n}} - m_{\mathrm{p}}$ | `mnucleon` |
| $\rho_b$, $\rho_b^*$ | stabiliser density | $\rho_{\mathrm{stab}}$, $\rho_{\mathrm{stab}}(f_*)$ | `rhostab` |
| $\rho_0$ | electroweak parameter | $\rho_{\mathrm{EW},0}$ ($\rho_{\mathrm{EW}}$) | `rhoEW0`, `rhoEW` |
| $\rho_{\vec p}$ | neutrino density matrix | $\boldsymbol{\rho}_{\vec k}$ | `boldrho` |
| $\varrho$ | profile density in $\xi$ or in $y$ | $\varrho_f(y)$ (in $y$); $\varrho_1$, $\varrho_2$ (in $\xi$) | `varrho`, `varrho12` |
| $s$ | entropy density | $s$ (unchanged) | `sentropy` |
| $s$ | Mandelstam variable | $E_{\mathrm{cm}}^2$ | `Ecm` |
| $s$ | $\sinh w/w$ ($s_L$, $s_R$) | written out | |
| $s$, $S$ ($s_o$, $s_{DM}$, $s_{DF}$) | scalar densities | $n^{\mathrm{sc}}$, $n^{\mathrm{sc}}_o$, $n^{\mathrm{sc}}_{\mathrm{DM}}$, $n^{\mathrm{sc}}_{\mathrm{DF}}$ | `nsc`, `nscDM`, `nscDF` |
| $t_o$ | momentum density of an orbital | $n^{\mathrm{t}}_o$ | `nt` |
| $S$ | action | $S$ (unchanged) | `Saction` |
| $S^{ab}$ | spinor generators | $\mathcal{S}^{ab}$ | `calS` |
| $S_B$, $S_{B-L}$ | sums of squared overlaps | $\mathcal{S}_B$, $\mathcal{S}_{B-L}$ | `SB` |
| $\sigma$ | anisotropic stress ($\sigma_\gamma$) | $\sigma_{\mathrm{an}}$, $\sigma_{\mathrm{an},\gamma}$ | `sigmaan`, `sigmaangamma` |
| $T^M{}_N$ | energy-momentum tensor | $\mathcal{T}^M{}_N$ ($\mathcal{T}_{\mathrm{stab}}$, $\mathcal{T}_\Psi$, ...) | `EMT`, `Tstab`, ... |
| $T$ | temperature | $T$ (unchanged) | `Temp` |
| $\tau$ | conformal time | $\tau_{\mathrm{c}}$ | `tauc` |
| $\tau^a$ | Pauli matrices of SU(2) | $\tau^I$ | `tau` |
| $\psi$, $\phi$ | Newtonian-gauge potentials (Ma-Bertschinger) | $\Phi$, $\Psi_{\mathrm{N}}$ ($\epsilon$ absorbed) | `Phi`, `PsiN` |
| $\psi_\alpha$ | flavour amplitudes | $\boldsymbol{\psi}$ | `bspsi` |
| $\psi$ | Standard-Model fermion field | $\psi$ (unchanged) | `psi` |
| $\Delta_\Phi(k)$ | root-mean-square potential | $\Phi_{\mathrm{rms}}(k)$ | `Phirms` |
| $\chi$, $\chi_D$, $\chi_F$, $\chi_o$ (four-dimensional) | dark-matter, fold and orbital fields | $\Psi_{\mathrm{DM}}$, $\Psi_{\mathrm{fold}}$, $\Psi_o$ | `PsiDM`, `Psifold`, `Psi` |
| $\chi$ | block spinor | $\chi$ (unchanged) | `chi` |
| $u$ | direction cosine of a neutrino | $u$ (unchanged) | `ucos` |
| $u$ | up quark | $u_R$, $u_{Ri}$; upright $\mathrm{u}$ in $m_{\mathrm{u}}$, $n_{\mathrm{u}}$ | `uR`, `mquarks`, `nquark` |
| $u(y)$, $u_n$ | boson profiles | $F$, $F_n$ | `Fprof` |
| $U$ | PMNS matrix | $U$ (unchanged) | `Upmns` |
| $V$ | CKM matrix | $V_{\mathrm{CKM}}$ | `VCKM` |
| $V_\beta$ | block basis | $\mathcal{V}$ | `calV` |
| $v$ | relative velocity $2\beta$ | $v_{\mathrm{rel}}$ | `vrel` |
| $w_k$ | Lovelock weights | $w_{(p)}$ | `wL` |
| $w$ | weight $\frac12$ of a fold parity | $\frac12$ (written out) | |
| $w$ | $\sqrt{c^2 - e^2}$ | $\upsilon_L$, $\upsilon_R$ | `upsilon` |
| $x_t$ | the extra times | $x_5$, $x_6$, $x_7$ | `x5`, ... |
| $Y$ | hypercharge; abundance $n/s$ | $Y$; $Y_{\mathrm{DM}}$ | `Yhyp`; `Yabund` |
| $\hat e_i$ | unit vector of a generation | $\mathbf{u}_i$ | `bfu` |
| $\zeta(c)$ | tip amplitude of a zero mode | $\mathcal{Z}(c)$ | `calZ` |
| $\zeta$ | primordial curvature perturbation | $\mathcal{R}$ | `calR` |
| $\alpha_k$ | Lovelock couplings | $\alpha_{(p)}$ | `alphaL` |
| $\alpha$, $\alpha_s$ | fine-structure constant, strong coupling | $\alpha_{\mathrm{em}}$, $\alpha_3$ ($\alpha_2$, $\alpha_1$) | `alphaem`, `alpha3` |
| $\alpha$ (on $G^\alpha$) | colour index | $A$ | `iA` |
| $\Lambda_W$ | $x_0$ eigenvalue of the $W$ | $\tilde m_{\mathrm{W}}^2$ | `mtildeW` |
| $G$, $W$, $B$, $W^\pm$, $Z$, $A$ | gauge fields in the geometric and in the canonical normalisation, written with the same letters | geometric: $G$, $W$, $B$ (eight and four dimensions); canonical: $W^\pm$, $Z$, $A$, $F^V$ | `Ggluon`, `Wpm`, `FV` |

## 4. Index letters

A single letter in a subscript or superscript that is not a name is an index; each index letter has its own registry entry.
The same letter as a symbol (not an index) has another entry: for example the index $p$ (Lovelock order) and the pressure $p$, the
index $s$ (species) and the entropy density $s$, the index $n$ (level) and the density $n$.

| index | values | key |
| --- | --- | --- |
| $M, N, P, Q$ (also $M_1, \dots$) | $x_0, \dots, x_7$ | `iM`, `iN`, `iP`, `iQ` |
| $a, b, c, d$ | frame directions $0, \dots, 7$ | `ia`, `ib`, `ic`, `id` |
| $\mu, \nu$ | $x_1, \dots, x_4$ (the tip directions on the tip) | `imu`, `inu` |
| $A, B$ | colour (adjoint SU(3)), $1, \dots, 8$ | `iA`, `iB` |
| $I$ | weak isospin (adjoint SU(2)), $1, 2, 3$ | `iI` |
| $i, j$ | generations and neutrino mass states, $1, 2, 3$ | `ii`, `ij` |
| $\alpha, \beta$ | lepton flavours $e, \mu, \tau$ ($e$ itself: `ie`) | `ialpha`, `ibeta`, `ie` |
| $\psi$ | Standard-Model multiplet $Q, u_R, d_R, \ell, e_R, \nu_R$ | `ipsi` |
| $f$ | fermion species (multiplet of one generation, fermion of a medium) | `if` |
| $o$ | Kohn-Sham orbital | `io` |
| $n$ | Kaluza-Klein level $1, 2, 3, \dots$ | `in` |
| $p$ | Lovelock order $1, 2, 3$ | `ip` |
| $r$ | Lovelock order of the four-dimensional factor | `ir` |
| $l$ | multipole $0, 1, 2, \dots$ | `il` |
| $s$ | particle species of the plasma | `is` |
| $L$, $R$ | chirality labels | `iL`, `iR` |
| $V$ | vector coupling ($\tilde g^f_V$) | `iV` |
| $y$ | in $\partial_y$ | `iy` |

## 5. Recommended symbols for quantities outside the inventory

These quantities appear in the documents but not in the field equations; the writers add them to their own registry file
(`model.json`, `solution.json`, `analysis.json`, `provenance.json`). The forms below avoid every symbol of `core.json`.

| quantity | version 3 | recommended version 4 |
| --- | --- | --- |
| redshift | $z$ | $z_{\mathrm{red}}$, with $1 + z_{\mathrm{red}} = \mathrm{e}^{-a_4}$ ($a_4 = 0$ today) |
| BAO distances, sound horizon | $D_M$, $D_H$, $D_V$, $r_d$ | $d_{\mathrm{M}}$, $d_{\mathrm{H}}$, $d_{\mathrm{V}}$, $r_{\mathrm{d}}$ ($D_M$ is the covariant derivative) |
| growth rate | $f$ | $f_{\mathrm{gr}} = \mathrm{d}\ln D_+/\mathrm{d}a_4$ |
| equation of state of dark energy | $w$, $w_0$, $w_a$ | $w_{\mathrm{de}}$, $w_{\mathrm{de},0}$, $w_{\mathrm{de},a}$ |
| tensor-to-scalar ratio, optical depth, acoustic angle | $r$, $\tau$, $\theta$ | $r_{\mathrm{ts}}$, $\tau_{\mathrm{reio}}$, $\theta_*$ |
| goodness of fit | $\chi^2$ | $\chi_{\mathrm{fit}}^2$ ($\chi$ is the block spinor) |
| freeze-out value of $x$, highest temperature | $x_f$, $T_{max}$ | $x_{\mathrm{f}}$, $T_{\mathrm{max}}$ |
| s-wave and p-wave coefficients of $\sigma v$ | $a$, $b$ | $a_{\mathrm{sw}}$, $b_{\mathrm{pw}}$ |
| dark-matter-nucleon reduced mass | $\mu_N$ | $\mu_{\mathrm{red}}$ |
| nucleon couplings of direct detection | $f_N$, $f_p$ | $f_{\mathrm{p}}$, $f_{\mathrm{n}}$ |
| proper hidden length and its spread | $s = fy$, $\Delta s$ | $fy$ and $\Delta(fy)$ (written out) |
| wave number conjugate to $\xi$ | $p$ ($\langle p^2\rangle$) | $k_\xi$ (register as a name) |
| particles of a Kohn-Sham cell | $N$ | $N_{\mathrm{KS}}$ |
| benchmark self-coupling | $\lambda_B$ | $\lambda_{\mathrm{test}}$ |
| Majorana tip coupling | $\kappa_M$ | $\mathcal{K}_{\mathrm{M}}$ |
| Hubble parameter today | $h$, $H_0$ | $h_{100}$, $\mathcal{H}_0$ |
| sum of neutrino masses, neutrino density | $\sum m_\nu$, $\Omega_\nu h^2$ | $\sum_im_i$, $\Omega_\nu h_{100}^2$ (register $\Omega_\nu$ as a name) |
| hadronic ratio of the $Z$ | $R_\ell$ | $R_\ell$ (a registered name, not the Ricci scalar) |
