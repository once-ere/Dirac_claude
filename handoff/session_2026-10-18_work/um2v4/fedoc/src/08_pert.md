
# The linear perturbations

## The metric as a power series

@FE-87

**The terms.** The metric of UM-2 is the order-0 metric (FE-31) plus terms of decreasing magnitude, counted by the bookkeeping
parameter $\epsilon \sim 10^{-5}$ (the size of the cosmological potentials). Each term is expanded in the $x_0$ profiles $F_n$ of FE-50:
$n = 0$ is the flat profile (four-dimensional gravity, the cosmological perturbations below), $n \ge 1$ are the Kaluza-Klein gravitons of
FE-53. Status: DERIVED. The terms decrease strictly: order 0 is 1, order 1 is at most $2.4\times10^{-5}$ on cosmological scales (the rms
potential, FE-98), the Kaluza-Klein terms have ranges below $1.6\times10^{-21}$ m, the radion term is at most $1.1\times10^{-34}$, and order 2 is
estimated as the square of order 1, $5.8\times10^{-10}$ (ESTIMATE). Residual (the first omitted order relative to the kept one)
$2.4\times10^{-5}$; at a neutron star order 2 is 0.03 of order 0, and there full nonlinear general relativity applies.

@FE-88

**The terms.** The order-1, $n = 0$ term in eight dimensions, in the Newtonian gauge: $\Phi$ is the Newtonian potential (in the time
component), $\Psi_{\mathrm{N}}$ the curvature potential of ordinary space, $h^{\mathrm{TT}}$ the transverse-traceless tensor of gravitational
waves, and $\sigma_{\mathrm{r}}$ the radion, a common change of the block scale. The radion is massive (48.42 TeV, FE-44): its static
response to matter is at most $1.1\times10^{-34}$, so it is absent on every observable scale; the tensor amplitude is an input,
bounded by the tensor-to-scalar ratio below 0.036. Status: DERIVED.

@FE-89

**The terms.** The four-dimensional part of FE-88 in the conformal time $\tau_{\mathrm{c}}$ of the expanding Universe ($\mathrm{d}x_4 =
\mathrm{e}^{a_4}\mathrm{d}\tau_{\mathrm{c}}$), the form used by the Einstein-Boltzmann codes. A prime denotes the derivative with respect to
$\tau_{\mathrm{c}}$; $a_4'$ is the conformal expansion rate. Status: STANDARD (Newtonian gauge, Ma and Bertschinger).

## The Einstein-Boltzmann equations

The order-1, $n = 0$ part of FE-1, reduced on the stabilised block (FE-49), is general relativity with the four-dimensional
energy-momentum tensor of all species; for one Fourier mode $k$:

@FE-90

**The terms.** The four linearised Einstein equations: the energy constraint (the change $\Delta\rho$ of the total energy density sources
$\Psi_{\mathrm{N}}$, the Poisson equation inside the horizon), the momentum constraint (the velocity divergence $\theta_{\mathrm{tot}}$ of the total
fluid), the pressure equation (the change $\Delta p$ of the total pressure) and the anisotropic-stress equation ($\sigma_{\mathrm{an}}$ makes $\Phi$
and $\Psi_{\mathrm{N}}$ differ; it comes from the free-streaming neutrinos and photons). All species of UM-2 contribute to the sources:
the dark matter, the baryons, the photons, the three neutrino mass states and the fold bands produced by freeze-in. Status: STANDARD
(solved with CAMB 2.0.5 at the Planck 2018 parameters; the TT and EE spectra agree with Planck $\Lambda$CDM to $2.5\times10^{-4}$ and
$2.7\times10^{-4}$).

@FE-91

**The terms.** The dark matter (the lowest odd quanta of $\Psi_A$ and $\Psi_B$) is cold: its density contrast $\delta_{\mathrm{DM}}$ changes with
its velocity divergence $\theta_{\mathrm{DM}}$ and the change of the curvature potential, and its velocity responds only to the expansion and
to the gradient of $\Phi$; it has no pressure (Kohn-Sham: $p_3 = 0$ for quanta at rest) and no interaction at these energies (its portal
couplings are of order $10^{-9}$ GeV$^{-2}$ and below). Status: STANDARD.

@FE-92

**The terms.** The baryons (the up and down quarks confined in protons and neutrons, and the electrons): the same continuity equation,
with the sound speed $c_{\mathrm{s}}$ of the baryon fluid and the Thomson drag of the photons ($n_{\mathrm{e}}$ the free-electron density,
$\sigma_{\mathrm{T}}$ the Thomson cross-section, $R_{\mathrm{b}}$ the ratio of the photon and baryon inertia). Status: STANDARD.

@FE-93

**The terms.** The photon density contrast and velocity divergence: radiation ($\frac43$), the pressure gradient $\frac14\delta_\gamma$, the
anisotropic stress $\sigma_{\mathrm{an},\gamma}$, gravity, and the Thomson scattering on the free electrons. Status: STANDARD.

@FE-94

**The terms.** The Legendre multipoles $F^\gamma_l$ of the photon temperature perturbation: free streaming couples each multipole to
its neighbours, Thomson scattering damps them, and the quadrupole is fed by the polarisation ($G^\gamma_0$, $G^\gamma_2$). Status:
STANDARD.

@FE-95

**The terms.** The multipoles $G^\gamma_l$ of the photon polarisation: free streaming and Thomson scattering, which generates
polarisation from the temperature quadrupole. Status: STANDARD.

@FE-96

**The terms.** Each neutrino mass state $\nu_i$ (after decoupling the flavour coherence is lost and each mass state propagates on its own)
has the multipoles $\mathcal{N}^{(i)}_l$ of its perturbed distribution at the comoving momentum $k_\nu$; $E^{\mathrm{c}}_i$ is its comoving
energy with the mass $m_i$ (FE-100), $f_{\mathrm{FD}}$ the Fermi-Dirac distribution. The masses make the neutrinos slow at late times
(they then cluster like matter). The fold bands of dirac16complex obey the massless limit. Status: STANDARD (each mass state with the
degeneracy $N_{\mathrm{eff}}/3 = 1.0144$; the masses in CAMB agree with the $x_0$ masses to $7.8\times10^{-12}$).

@FE-97

**The terms.** The four-dimensional Friedmann equation in conformal time (from FE-38 at first order with FE-80; $\Lambda_4$ the tuned
dark energy, FE-48), the temperature of the neutrinos after the electron-positron annihilation, and the primordial curvature spectrum
with the amplitude $A_{\mathrm{s}} = 2.099\times10^{-9}$ and the index $n_{\mathrm{s}} = 0.9649$ at the pivot $k_0$. Status: STANDARD (inputs: the
Planck 2018 primordial parameters; $N_{\mathrm{eff}} = 3.0432$ in the neutrinos and 0.0010 in the fold bands; results: $\mathcal{H}_0 = 67.38$
km/s/Mpc, the sound horizon at the drag epoch 147.10 Mpc, BAO $\chi^2 = 31.5$ for 13 DESI DR2 points).

@FE-98

**The terms.** The size of the first-order potentials: $\Phi_{\mathrm{rms}}$ is the rms Weyl potential $\Phi_{\mathrm{W}}$ per logarithmic
wavenumber, from its power spectrum $P_{\Phi_{\mathrm{W}}}$. Inside the horizon it follows from the matter density contrast $\delta_{\mathrm{m}}$
(the Poisson equation, from FE-90), on the largest scales from the primordial curvature perturbation $\mathcal{R}$ with the growth factor
$D_+$, which the dark energy suppresses at late times. The relations are written for the magnitudes: in the sign conventions of FE-89
and FE-90 the potential of an overdensity is negative; only the rms value is used. Status: STANDARD. $\Phi_{\mathrm{rms}} = 2.42\times10^{-5}$ at
$k = 10^{-4}$ Mpc$^{-1}$ down to $5.03\times10^{-8}$ at 1 Mpc$^{-1}$; the Poisson form agrees with the CAMB solution to $1.5\times10^{-6}$ for
$k \ge 0.01$ Mpc$^{-1}$ (the residual of the stored first-order solution in this equation) and the large-scale form to $4.4\times10^{-5}$ ($D_+\mathrm{e}^{-a_4}
= 0.7878$ today, with $\Omega_{\mathrm{m}} = 0.3150$).

@FE-99

**The terms.** The rms density fluctuation in spheres of radius $8\,h_{100}^{-1}$ Mpc, from the linear matter power spectrum $P_{\mathrm{m}}$ and the
top-hat window $W_{\mathrm{th}}$. Status: STANDARD. $\sigma_8 = 0.8118$ for UM-2 (0.8119 without the fold bands) against 0.8109 for
$\Lambda$CDM.
