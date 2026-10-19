# Cosmology: the CMB, the CNB and the BAO

## The content and the equations (STANDARD equations, DERIVED content)

The four-dimensional effective theory of UM-2 is general relativity (FE-49) with photons; the three neutrino mass states ($1.000$,
$8.712$ and $50.140$ meV, with the heated spectrum of the electron-positron annihilation: $N_{\mathrm{eff}} = 3.0432$); the fold bands
produced by freeze-in (massless, $\Delta N_{\mathrm{eff}} = 0.0010$), so $N_{\mathrm{eff}} = 3.0442$ in all; the baryons; the dark matter
(the odd quanta of $\Psi_A$ and $\Psi_B$, cold); and the cosmological term $\Lambda_4$. The order-1 terms of the metric series, the
perturbations of this content, obey the standard Einstein-Boltzmann equations in the Newtonian gauge (STANDARD, Ma and Bertschinger).
They are written here for one Fourier mode of the comoving wave number $k$, with the conformal time $\tau_{\mathrm{c}}$ (a prime is
$\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$ and nothing else). The metric:

@@FE-89@@

The Einstein equations, summed over all species:

@@FE-90@@

The dark matter, cold (the Kohn-Sham states of quanta at rest have $w_{\mathrm{KS}} = 0$):

@@FE-91@@

The baryons, coupled to the photons by Thomson scattering:

@@FE-92@@

The photons: density and velocity, the temperature hierarchy and the polarisation hierarchy:

@@FE-93@@

@@FE-94@@

@@FE-95@@

The cosmic neutrino background: one hierarchy for each neutrino mass state, whose unperturbed distribution is the heated spectrum
of the section on the three neutrino flavours; the fold bands produced by freeze-in obey its massless limit $E^{\mathrm{c}}_i = k_\nu$:

@@FE-96@@

The background expansion, the neutrino temperature and the primordial spectrum, which is an input of UM-2 (Planck 2018), not a
prediction:

@@FE-97@@

## The solution (DERIVED, 8 checks)

The equations were solved with the Einstein-Boltzmann code CAMB 2.0.5 (default accuracy, about $10^{-3}$; lensing included) at the
Planck 2018 values (STANDARD) $\Omega_{\mathrm{b}}h_{100}^2 = 0.02237$, $\Omega_{\mathrm{DM}}h_{100}^2 = 0.1200$, $100\,\theta_{\mathrm{MC}} =
1.04092$ (the angular size of the sound horizon at last scattering, held fixed, so that $\mathcal{H}_0$ is an output), the optical depth
to reionisation $0.0544$, $\ln(10^{10}A_{\mathrm{s}}) = 3.044$ and $n_{\mathrm{s}} = 0.9649$. Each neutrino mass state is evolved separately
with the degeneracy $N_{\mathrm{eff}}/3 = 1.0144$; CAMB gives each the density of a Fermi-Dirac gas of the temperature $T_\nu$ times the
degeneracy, so its masses were iterated (13 iterations, to $7.8\times10^{-12}$) until the late-time density equals that of the heated
spectrum. The comparison model is $\Lambda$CDM with the Planck 2018 parameters (one neutrino of $0.06$ eV, $N_{\mathrm{eff}} = 3.044$).

| model | $\mathcal{H}_0$ (km/s/Mpc) | $\Omega_{\mathrm{m}}$ | $N_{\mathrm{eff}}$ | age (Gyr) | $r_{\mathrm{d}}$ (Mpc) | $\chi_{\mathrm{BAO}}^2$ (13 points) | $\sigma_8$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\Lambda$CDM | $67.34$ | $0.3154$ | $3.044$ | $13.799$ | $147.103$ | $32.55$ | $0.8109$ |
| UM-2 | $67.38$ | $0.3150$ | $3.0442$ | $13.796$ | $147.104$ | $31.49$ | $0.8118$ |
| UM-2 without the freeze-in fold bands | $67.37$ | $0.3151$ | $3.0432$ | $13.797$ | $147.109$ | $31.72$ | $0.8119$ |

**The CMB.** The TT and EE spectra of UM-2 agree with Planck $\Lambda$CDM to $2.5\times10^{-4}$ and $2.7\times10^{-4}$ (multipoles 30 to
2500; for TT at most $0.007$ of the cosmic variance $\sqrt{2/(2l + 1)}$ of a single multipole $l$; the binned cosmic-variance $\chi^2$, the
sum over bins of 50 multipoles of the squared mean relative deviation over the cosmic variance of the bin, is $0.020$). By themselves,
the three mass states instead of one state of 60 meV move TT and EE by $2.6\times10^{-4}$ and $2.3\times10^{-4}$, and
$N_{\mathrm{eff}} = 3.0432$ instead of $3.044$ by $1.3\times10^{-4}$; without the freeze-in fold bands the deviations would be
$2.8\times10^{-4}$ (TT and EE), and the fold bands themselves move TT by at most $1.6\times10^{-4}$. UM-2 reproduces the CMB of $\Lambda$CDM.
Its $N_{\mathrm{eff}} = 3.0442$ lies 1.4 standard deviations above the ACT DR6 value $2.86 \pm 0.13$ (STANDARD, from memory). A fold band
thermalised in the early Universe, which UM-2 does not contain, would be excluded: decoupled above the electroweak scale
($\Delta N_{\mathrm{eff}} = 0.0958$) or just above the QCD crossover ($0.1963$) it moves TT by up to 1.5 % and 3.1 % at fixed Planck
parameters (0.8 and 1.5 cosmic-variance units of a single multipole; binned $\chi^2 = 293$ and $1208$) and lies 2.1 and 2.9 standard
deviations above ACT DR6; its BAO $\chi_{\mathrm{BAO}}^2$ would be lower ($15.4$ and $10.7$), but these variants are not fits to the CMB.

![CMB temperature (left) and E-mode (right) spectra of UM-2 (three massive neutrinos and the freeze-in fold bands), of Planck 2018 $\Lambda$CDM and of the variant with a fold band thermalised above the QCD crossover (not part of UM-2); the figure labels UM-2 "version 3", whose physics version 4 keeps; lower panels: the relative difference to $\Lambda$CDM, with the cosmic variance of one multipole (dotted).](figures/fig_cmb_spectra.png)

**The CNB.** The cosmic neutrino background enters through $N_{\mathrm{eff}} = 3.0432$ and the three masses. The neutrino density
parameter of UM-2 in CAMB, $\Omega_\nu h_{100}^2 = 6.4511\times10^{-4}$, equals the value $6.382\times10^{-4}$ of the CNB at the
temperature of instantaneous decoupling times $(N_{\mathrm{eff}}/3)^{3/4}$ ($6.4510\times10^{-4}$); the mass sum $0.0599$ eV lies below the
DESI DR2 bound $0.064$ eV (STANDARD, from memory), which would allow a lightest mass up to $4.1$ meV.

**The BAO.** The distances (flat space, $c = 1$) at the redshift $z_{\mathrm{red}}$,

$$
d_{\mathrm{M}}(z_{\mathrm{red}}) = \int_0^{z_{\mathrm{red}}}\frac{\mathrm{d}\tilde z_{\mathrm{red}}}{\mathcal{H}(\tilde z_{\mathrm{red}})},\qquad
d_{\mathrm{H}}(z_{\mathrm{red}}) = \frac{1}{\mathcal{H}(z_{\mathrm{red}})},\qquad
d_{\mathrm{V}}(z_{\mathrm{red}}) = \big(z_{\mathrm{red}}\,d_{\mathrm{M}}^2d_{\mathrm{H}}\big)^{1/3},
$$
<!-- symbols: AUTO -->

in units of the sound horizon at the drag epoch $r_{\mathrm{d}}$, are compared with the DESI DR2 measurements (STANDARD,
arXiv:2503.14738; the last column is the published correlation coefficient of the pair $d_{\mathrm{M}}/r_{\mathrm{d}}$,
$d_{\mathrm{H}}/r_{\mathrm{d}}$):

| tracer | $z_{\mathrm{red}}$ | $d_{\mathrm{V}}/r_{\mathrm{d}}$ | $d_{\mathrm{M}}/r_{\mathrm{d}}$ | $d_{\mathrm{H}}/r_{\mathrm{d}}$ | correlation |
| --- | --- | --- | --- | --- | --- |
| BGS | 0.295 | $7.942 \pm 0.075$ | | | |
| LRG1 | 0.510 | | $13.588 \pm 0.167$ | $21.863 \pm 0.425$ | $-0.459$ |
| LRG2 | 0.706 | | $17.351 \pm 0.177$ | $19.455 \pm 0.330$ | $-0.404$ |
| LRG3+ELG1 | 0.934 | | $21.576 \pm 0.152$ | $17.641 \pm 0.193$ | $-0.416$ |
| ELG2 | 1.321 | | $27.601 \pm 0.318$ | $14.176 \pm 0.221$ | $-0.434$ |
| QSO | 1.484 | | $30.512 \pm 0.760$ | $12.817 \pm 0.516$ | $-0.500$ |
| Ly$\alpha$ | 2.330 | | $38.988 \pm 0.531$ | $8.632 \pm 0.101$ | $-0.431$ |

through

$$
\chi_{\mathrm{BAO}}^2 = \sum_{\text{tracers}}\big(\mathbf{d} - \mathbf{d}^{\mathrm{th}}\big)^T\,\mathbf{C}^{-1}\,\big(\mathbf{d} - \mathbf{d}^{\mathrm{th}}\big),
\qquad \mathbf{d} = \Big(\frac{d_{\mathrm{M}}}{r_{\mathrm{d}}},\ \frac{d_{\mathrm{H}}}{r_{\mathrm{d}}}\Big)
$$
<!-- symbols: AUTO -->

for the anisotropic tracers (the covariance $\mathbf{C}$ of each tracer built from the published errors and correlation), plus the
squared deviation over the variance of $d_{\mathrm{V}}/r_{\mathrm{d}}$ for BGS: $\chi_{\mathrm{BAO}}^2 = 31.49$ for the 13 measurements
($\Lambda$CDM: $32.55$; without the freeze-in fold bands $31.72$) (DERIVED).

![BAO distances divided by the square root of the redshift, against the DESI DR2 measurements (the figure writes $D$ for the distances $d$ of the text); $\chi_{\mathrm{BAO}}^2$ uses $d_{\mathrm{V}}$ for BGS and $d_{\mathrm{M}}$, $d_{\mathrm{H}}$ with their correlation for the other tracers (the $d_{\mathrm{V}}$ points of the anisotropic tracers are shown for illustration).](figures/fig_bao.png)

**The matter fluctuations.** A separate CAMB run of each model gives the linear matter power spectrum and

@@FE-99@@

$\sigma_8 = 0.8118$ for UM-2 ($0.8119$ without the freeze-in fold bands) against $0.8109$ for $\Lambda$CDM (Planck 2018: $0.811$,
STANDARD, from memory); the product of the growth rate $\mathrm{d}\ln D_+/\mathrm{d}a_4$ and $\sigma_8$ at $z_{\mathrm{red}} = 0.5$ is $0.4761$
($0.4762$ without the fold bands) against $0.4756$. The sizes of the first-order potentials quoted in the section on the metric series
come from the same solution.

