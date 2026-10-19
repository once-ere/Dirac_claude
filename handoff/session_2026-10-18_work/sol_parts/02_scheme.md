# The approximation scheme

The coupled field equations are solved in a hierarchy that uses the small parameters of the problem. Each step of the
solution states its own approximation in its second part, with the size of the neglected terms; the five parameters that
organise the whole solution are these.

**The metric is a power series of terms of decreasing magnitude.** Order 0 is the background (step 1); order 1 with $n = 0$
carries the CMB, the CNB and the BAO (step 6); the terms with $n \ge 1$ are the Kaluza-Klein gravitons, and order 2 is the
first omitted order (step 10):

@@series@@

**After the primordial era the matter sources are tiny compared with the stabiliser of the block.** The constraint
$3\mathcal{G}(K_*)\,\mathcal{H}^2 = \kappa\Delta\rho$ of the first-order block response (step 1) fixes their ratio by the
expansion rate of 3-space; today the rate is the Hubble constant $\mathcal{H}_0$, and the ratio is $10^{-92}$:

$$
\frac{\kappa\Delta\rho}{\kappa\rho_{\mathrm{stab}}(f_*)} = \frac{3\mathcal{G}(K_*)\,\mathcal{H}^2}{\kappa\rho_{\mathrm{stab}}(f_*)}
 = 0.7592\,\frac{\mathcal{H}^2}{H^2},\qquad \frac{\mathcal{H}_0^2}{H^2} = 1.0\times10^{-92}
$$

<!-- symbols: AUTO -->

so the block responds linearly and adiabatically to every source, and the block scale moves by at most
$\lvert\Delta\ln f\rvert = 1.1\times10^{-34}$ in any environment of the model (step 8).

**The Standard-Model masses lie far below the gap of the $x_0$ operators.** The lightest massive Kaluza-Klein state has the
mass $3H/(2f_*) = 99.48$ TeV (the gap) and the first Kaluza-Klein level $m_{\mathrm{KK}} = 121.32$ TeV, while the heaviest
Standard-Model particle, the top quark, has $172.56$ GeV; the four-dimensional fields are the zero modes of the $x_0$
operators, and the exchange of Kaluza-Klein modes corrects the four-dimensional interactions at the relative order

$$
\Big(\frac{m_{\mathrm{W}}}{m_{\mathrm{KK}}}\Big)^2 = 4.39\times10^{-7},\qquad
\Big(\frac{2f_*\,m_{\mathrm{t}}}{3H}\Big)^2 = 3.0\times10^{-6}
$$

<!-- symbols: AUTO -->

(step 2; the largest off-diagonal coupling of the first Kaluza-Klein gauge mode in the mass basis is $1.0\times10^{-17}$).

**dirac16complex is treated by Kohn-Sham theory on the static block.** Its many-body state is described by Kohn-Sham orbitals
in the local mean fields of its contact self-interaction and of the portals I11, I12 and I13, through which the
Standard-Model fields enter with their densities and condensates (steps 3 and 8). The portal mean fields are external
fields of first order: the dark-matter level moves by at most

$$
\frac{\lvert\Delta\varepsilon_{\mathrm{DM}}\rvert}{M_{\mathrm{DM}}} \le 1.5\times10^{-6}
$$

<!-- symbols: AUTO -->

(at the dark-matter freeze-out; below $10^{-15}$ in every cold environment), and the response of a level to them is
screened by the self-interaction by only $3.5\times10^{-4}$ (step 8).

**The neutrinos are ultra-relativistic and their flavour evolution is coherent.** For every source of UM-2 the energy
exceeds the masses by many orders ($m_3/E = 1.3\times10^{-8}$ for reactor antineutrinos of 4 MeV), and outside the early
Universe the collisions are negligible against the forward scattering (step 5).

The hierarchy of the solution follows from these parameters: (1) the background and the primordial era; (2) the $x_0$
spectra, i.e. all masses and the mixing matrices; (3) the Kohn-Sham states of dirac16complex coupled to gravity and to the
Standard-Model fields, and their back-reaction on the block; (4) the electroweak sector; (5) the flavour conversion of the
three neutrinos, $N_{\mathrm{eff}}$ and the CNB; (6) the linear cosmology (CMB, CNB, BAO); (7) the dark-matter relic through
I12 and its detection; (8) the coupled solution in environments, iterated to self-consistency; (9) the thermal history and
the relic with I13; (10) the magnitudes of the terms of the metric series. Each step uses the results of the earlier ones,
and its check in concert returns its results to the equations of the other steps.
