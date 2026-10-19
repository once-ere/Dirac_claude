# Step 6: the CMB, the CNB and the BAO

On the stabilised block the four-dimensional effective theory is general relativity (step 1) with photons, baryons, the three
neutrino mass eigenstates (step 5), the dark matter (the odd quanta of $\Psi_A$ and $\Psi_B$, steps 2 and 3), the fold bands of
dirac16complex made by freeze-in (massless free-streaming radiation with $\Delta N_{\mathrm{eff}} = 0.001$, step 9) and the
four-dimensional cosmological term $\Lambda_4$. Step 6 solves the order-1, $n = 0$ term of the metric series: the linear
Einstein-Boltzmann equations that give the CMB, the CNB and the BAO.

## The field equations of step 6

The Einstein-Lovelock equations, whose order-1, $n = 0$ part this step solves through the four-dimensional gravity of the
stabilised block (step 1):

@@el@@

@@einstein4@@

The order-1, $n = 0$ term of the metric in the Newtonian gauge, in eight dimensions and in the four-dimensional conformal time:

@@newton8@@

@@newton4@@

The linearised Einstein equations and the equations of every species of UM-2:

@@pert_einstein@@

@@pert_dm@@

@@pert_baryon@@

@@pert_photon@@

@@pert_photon_hier@@

@@pert_pol@@

@@pert_nu@@

@@pert_bg@@

The amplitude of the matter fluctuations:

@@sigma8@@

## The approximation of step 6

* *First order in $\epsilon$.* The omitted order 2 is $\Phi_{\mathrm{rms}} = 2.4\times10^{-5}$ of the kept order on the largest
  scales (step 10).
* *Only the $n = 0$ term.* The Kaluza-Klein gravitons and gauge bosons ($\ge 99$ TeV) and the radion ($48$ TeV) are absent at
  cosmological scales; the radion responds statically, by at most $\Delta\ln f = 1.1\times10^{-34}$ (step 8).
* *The standard numerical solution.* CAMB 2.0.5 at its default accuracy (about $10^{-3}$), lensing included; the three neutrino
  masses are iterated to $7.8\times10^{-12}$.
* *The primordial spectrum is an input* (Planck 2018), not predicted by UM-2.

## The solution of step 6

The equations were solved with CAMB 2.0.5 at the Planck 2018 values (STANDARD) $\Omega_{\mathrm{b}}h_{100}^2 = 0.02237$,
$\Omega_{\mathrm{DM}}h_{100}^2 = 0.1200$, $100\,\theta_{\mathrm{MC}} = 1.04092$ (the angular size of the sound horizon at last
scattering, held fixed, so that $\mathcal{H}_0$ is an output, in km/s/Mpc), the optical depth to reionisation $0.0544$,
$\ln(10^{10}A_{\mathrm{s}}) = 3.044$ and $n_{\mathrm{s}} = 0.9649$. In UM-2 the three mass states are evolved separately, each
with the degeneracy $N_{\mathrm{eff}}/3 = 1.0144$ (the heated spectrum of step 5); CAMB gives each the density of a Fermi-Dirac
gas of the temperature $T_\nu = (4/11)^{1/3}T_\gamma$ times the degeneracy, so its masses are the UM-2 masses times the
degeneracy to the power $-1/4$, which reproduce the late-time density of the heated spectrum; CAMB finds them by inverting the
full (relativistic) density from the total neutrino density and the mass fractions, which were therefore iterated (13
iterations) until the masses agree to $7.8\times10^{-12}$ (DERIVED). The models are $\Lambda$CDM with the Planck 2018 parameters
(one neutrino of $0.06$ eV, $N_{\mathrm{eff}} = 3.044$: the CAMB defaults), UM-2 (the three mass states and the freeze-in fold
bands, $N_{\mathrm{eff}} = 3.0432 + 0.0010 = 3.0442$), UM-2 without the freeze-in fold bands (the neutrino content of version 2,
$N_{\mathrm{eff}} = 3.0432$), and two variants with a thermalised fold band of dirac16complex instead (two Weyl species, which
UM-2 does not contain; steps 4 and 9), decoupled above the electroweak scale ($\Delta N_{\mathrm{eff}} = 0.0958$) or just above
the QCD crossover ($\Delta N_{\mathrm{eff}} = 2(10.75/61.75)^{4/3}\times1.0095 = 0.1963$) (DERIVED, 8 checks).

**The BAO.** The distances (flat space, $c = 1$) in units of the sound horizon at the drag epoch $r_{\mathrm{d}}$,

$$
d_{\mathrm{M}}(z_{\mathrm{red}}) = \int_0^{z_{\mathrm{red}}}\frac{\mathrm{d}\tilde z_{\mathrm{red}}}{\mathcal{H}(\tilde z_{\mathrm{red}})},\qquad
d_{\mathrm{H}}(z_{\mathrm{red}}) = \frac{1}{\mathcal{H}(z_{\mathrm{red}})},\qquad
d_{\mathrm{V}}(z_{\mathrm{red}}) = \big(z_{\mathrm{red}}\,d_{\mathrm{M}}^2d_{\mathrm{H}}\big)^{1/3},
$$

<!-- symbols: AUTO -->

are compared with the DESI DR2 measurements (STANDARD, arXiv:2503.14738; the last column is the published correlation
coefficient of the pair $d_{\mathrm{M}}/r_{\mathrm{d}}$, $d_{\mathrm{H}}/r_{\mathrm{d}}$):

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

for the pairs of the anisotropic tracers (with the published errors and correlations in the covariance $\mathbf{C}$ of each tracer, and the
computed pair $\mathbf{d}^{\mathrm{th}}$), and the squared deviation over the variance of $d_{\mathrm{V}}/r_{\mathrm{d}}$ for BGS
(DERIVED):

| model | $\mathcal{H}_0$ | $\Omega_{\mathrm{m}}$ | $N_{\mathrm{eff}}$ | helium fraction | age (Gyr) | $z_{\mathrm{red},*}$ | $r_{\mathrm{d}}$ (Mpc) | $\chi_{\mathrm{BAO}}^2$ (13 points) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\Lambda$CDM | $67.34$ | $0.3154$ | $3.044$ | $0.24566$ | $13.799$ | $1089.91$ | $147.103$ | $32.55$ |
| UM-2 | $67.38$ | $0.3150$ | $3.0442$ | $0.24567$ | $13.796$ | $1089.91$ | $147.104$ | $31.49$ |
| UM-2 without the freeze-in fold bands (version 2) | $67.37$ | $0.3151$ | $3.0432$ | $0.24566$ | $13.797$ | $1089.91$ | $147.109$ | $31.72$ |
| UM-2 with a thermalised fold band (electroweak) | $68.48$ | $0.3050$ | $3.1390$ | $0.24693$ | $13.698$ | $1090.00$ | $146.630$ | $15.43$ |
| UM-2 with a thermalised fold band (QCD) | $69.65$ | $0.2948$ | $3.2395$ | $0.24824$ | $13.596$ | $1090.10$ | $146.133$ | $10.65$ |

($z_{\mathrm{red},*}$ the redshift of last scattering.) The neutrino density parameter of UM-2 in CAMB, $\Omega_\nu h_{100}^2 =
6.4511\times10^{-4}$, equals $6.4510\times10^{-4}$ from the CNB of step 5 times $(N_{\mathrm{eff}}/3)^{3/4}$; the mass sum $0.0599$
eV lies below the DESI DR2 bound $0.064$ eV, which would allow $m_1 < 4.1$ meV.

**The CMB.** The UM-2 TT and EE spectra agree with Planck $\Lambda$CDM to $2.5\times10^{-4}$ and $2.7\times10^{-4}$ (multipoles
30 to 2500; for TT at most $0.007$ of the cosmic variance $\sqrt{2/(2l + 1)}$ of a single multipole $l$; the binned full-sky
cosmic-variance $\chi^2$, the sum over bins of 50 multipoles of the squared mean relative deviation over the cosmic variance of
the bin, is $0.020$; without the freeze-in fold bands $2.8\times10^{-4}$, $2.8\times10^{-4}$ and $0.023$): UM-2 reproduces the
CMB of $\Lambda$CDM. By themselves the three mass states instead of one state of 60 meV move TT and EE by $2.6\times10^{-4}$ and
$2.3\times10^{-4}$, and $N_{\mathrm{eff}} = 3.0432$ instead of $3.044$ by $1.3\times10^{-4}$. The fold-band variants, at fixed
Planck $\Omega_{\mathrm{b}}h_{100}^2$, $\Omega_{\mathrm{DM}}h_{100}^2$ and $\theta_{\mathrm{MC}}$, move TT by up to $1.5$ % and $3.1$ %
($0.8$ and $1.5$ cosmic-variance units of a single multipole; binned $\chi^2 = 293$ and $1208$): they are not fits to the CMB,
and they lie $2.1$ and $2.9$ standard deviations above the ACT DR6 value $N_{\mathrm{eff}} = 2.86 \pm 0.13$ (UM-2: 1.4). The CNB
enters through $N_{\mathrm{eff}} = 3.0432$ and the three neutrino masses.

![CMB temperature (left) and E-mode (right) spectra of UM-2 (three massive neutrinos), of Planck 2018 $\Lambda$CDM and of the variant with a fold band thermalised above the QCD crossover; lower panels: relative difference to $\Lambda$CDM with the cosmic variance of one multipole (dotted).](figures/fig_cmb_spectra.png)

![BAO distances divided by the square root of the redshift against the DESI DR2 measurements; the $\chi_{\mathrm{BAO}}^2$ uses $d_{\mathrm{V}}$ for BGS and $d_{\mathrm{M}}$, $d_{\mathrm{H}}$ with their correlation for the other tracers (the $d_{\mathrm{V}}$ points of the anisotropic tracers are shown for illustration).](figures/fig_bao.png)

**The matter power spectrum.** A separate CAMB run of each model without the CMB gives the linear matter power spectrum and
$\sigma_8 = 0.8118$ (UM-2), $0.8119$ (UM-2 without the freeze-in fold bands) and $0.8109$ ($\Lambda$CDM; Planck 2018: $0.811$,
STANDARD); the product of the growth rate $\mathrm{d}\ln D_+/\mathrm{d}a_4$ and $\sigma_8$ at the redshift $0.5$ is $0.4761$,
$0.4762$ and $0.4756$ (DERIVED). The fold bands produced by freeze-in through I11 (step 9) are massless free-streaming radiation
with $\Delta N_{\mathrm{eff}} = 0.001$: they move the TT spectrum by at most $1.6\times10^{-4}$ against the model without them
(DERIVED, 8 checks in all).

## The check of step 6

**In its own equations.** The first-order potential of the CAMB solution satisfies the Poisson equation of the first-order
density inside the horizon,

@@phi_rms@@

to $1.5\times10^{-6}$ for $k \ge 0.01$ Mpc$^{-1}$, and the matter-era form on the largest scale to $4.4\times10^{-5}$ (what it
neglects: the departure of the transfer function from 1 and the radiation, about $10^{-4}$ at $k = 10^{-4}$ Mpc$^{-1}$; the growth
factor $D_+\mathrm{e}^{-a_4} = 0.787828964553$ today, recomputed $0.787828964555$) (DERIVED).

**In concert with the other field equations.**

* *The neutrino masses of the tip conditions* (step 2) are the masses of the CAMB computation to $5.7\times10^{-12}$ (the mass
  iteration converges to $7.8\times10^{-12}$) (DERIVED).
* *$N_{\mathrm{eff}}$ of the decoupling and of the freeze-in* (steps 5 and 9) are the input of CAMB exactly ($5\times10^{-16}$); its
  neutrino density today equals the CNB of step 5 times $(N_{\mathrm{eff}}/3)^{3/4}$ to $1.9\times10^{-5}$ (DERIVED).
* *The relic density of the Boltzmann equation* (step 9, two species, $2\times0.060$) is the cold dark matter of the CMB
  computation ($0.1200$) to $3.1\times10^{-9}$ (DERIVED).
* *The radiation after decoupling* of the thermal history (step 9) differs from the CMB computation by $0.59$ % (the thermal history
  decouples the neutrinos instantaneously; it uses this only for the entropy today and the nucleosynthesis environment)
  (DERIVED).
* *The metric series* (step 10): the potentials, the block shift, the first Kaluza-Klein mass and $\sigma_8$ used there are those
  of this step, of step 8 and of step 2, to $4.7\times10^{-12}$ (DERIVED).

## The status of step 6

STANDARD: the linear Einstein-Boltzmann equations, CAMB, the Planck 2018 parameters, the DESI DR2 and ACT DR6 measurements. DERIVED:
the UM-2 spectra, distances and $\sigma_8$ with the UM-2 content (three mass states with the heated spectrum, the freeze-in fold
bands), their agreement with $\Lambda$CDM and with the BAO data, the exclusion of a thermalised fold band. OPEN: the joint CMB and
BAO fit of the fold-band variants; the primordial spectrum (an input).
