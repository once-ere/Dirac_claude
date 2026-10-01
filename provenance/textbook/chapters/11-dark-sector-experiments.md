## 11. The five dark-sector experiments

### 11.1 What this chapter answers

Astronomers infer two things about the universe that ordinary matter does not explain. First, galaxies and clusters of galaxies move and bend light as if they contained much more gravitating mass than the stars and gas that can be seen; the missing part is called **dark matter**. It clusters like ordinary matter and has almost no pressure. Second, the light of distant exploding stars (supernovae) shows that the expansion of the universe is speeding up; whatever causes this is called **dark energy**. It must have a large negative pressure. This chapter asks whether the field dirac16complex of the earlier chapters can play either role, and it answers with numbers, not words.

Stage 3 of the project posed the question in these words: “in detail, investigate, determine and discuss, using numerical solutions and graphs, the physical behaviour and changing nature of pressure and energy density in this framework; is there any connection to dark matter and/or dark energy?” To answer it, five **experiments** (numbered EXP-1 to EXP-5) were run. Each one is a system of ordinary differential equations that a computer program integrates, as described in Chapter 10.

| Experiment | Background (the gravitational field) | Question |
| --- | --- | --- |
| EXP-1 | the primordial pair-creation field of the author's notebook | what do energy density and pressure do there, and what source would the field need? |
| EXP-2 | a homogeneous 8-dimensional universe solved together with Einstein's equations | does a self-gravitating condensate make the universe isotropic, and what would a 3-space observer infer? |
| EXP-3 | a 4-dimensional late universe with frozen extra dimensions | can the condensate be the dark energy of the quoted supernova fits? |
| EXP-4 | an expanding 3-space: a radiation era, and inflation followed by radiation | do the quanta behave like dark matter, and how many does the expansion create? |
| EXP-5 | deflating extra times | why must everything be restricted to modes without momentum along the extra times? |

The answer, which Sections 11.13 and 11.14 argue in full:

- **Dark matter: a qualified yes.** In the sector without momentum along the extra times, and with the extra dimensions held static by assumption, a gas of dirac16complex quanta turns from radiation-like into dust-like, and the expansion of the universe creates such quanta for every mass $m>0$. That is a dark-matter-like equation of state and a production mechanism. It is not a dark-matter model: the abundance, the darkness, the stabilisation of the extra dimensions and the growth of structure were neither computed nor derived.
- **Dark energy: no, within everything computed.** Negative pressure arises only from an attractive self-interaction. Tuned to today's quoted value $w_0=-0.861$ it evolves about eight times too fast, and a short distance into the past (redshift $z=0.026$) it leaves the regime in which its approximation is valid.

Every number in this chapter is copied from a committed output file of the repository. The files are the summary.json and python-check-report.json of each experiment under `artifacts/dirac16complex/numerics/exp1` to `exp5`, the fits file `artifacts/dirac16complex/numerics/exp3/fits.json`, and the collected `artifacts/dirac16complex/numerics/numerics-summary.json`. The scientific document of Stage 3 is `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md` (below: the Stage-3 document), and its companion `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` shows how to rerun everything. When we write “Stage-3 document §4.6” we mean its numbered part 4.6; “Section 11.4” always means a section of this book. Where a statement below is derived by hand rather than checked by a program, the text says so.

### 11.2 The words and numbers of cosmology

This section defines the handful of cosmological notions that the experiments use. Nothing here is specific to dirac16complex.

**Scale factor.** A universe that looks the same at every point (homogeneous) and in every direction (isotropic) can only change by a common stretching of all distances. The stretching factor $a(t)$ is the **scale factor**: two distant galaxies at rest in the expanding space are a distance proportional to $a(t)$ apart. By convention $a=1$ today.

**Hubble rate.** The relative growth rate $H=\dot a/a$ (a dot means $d/dt$) is the **Hubble rate**; $H_0$ is its value today. If $H$ is constant, $a=e^{Ht}$ grows exponentially; this is called de Sitter expansion, and a phase of it in the early universe is called inflation.

**Redshift.** Light that left a galaxy when the scale factor was $a$ arrives today with its wavelength stretched by the factor $1/a$. Astronomers call $z$ with $1+z=1/a$ the **redshift**. For example $a=0.5$ gives $z=1$, and $z=0.026$ gives $a=1/1.026=0.975$: a very recent epoch.

**Comoving quantities.** Coordinates that expand with the universe, in which galaxies at rest in the expanding space keep fixed coordinate values, are called **comoving**, and so are the quantities measured in them. A comoving distance or volume stays fixed as $a$ grows; the physical one is $a$ (or $a^3$) times it. A comoving momentum $k$ corresponds to the physical momentum $K=k/a$, and a comoving number density $na^3$ (the number per unit comoving volume) stays fixed as long as no particles are created or destroyed. A comoving temperature describes the occupations of the states as a function of the comoving momentum $k$; at $a=1$, where $K=k$, it is the physical temperature.

**Units and the Hubble length.** A parsec (pc) is $3.086\times10^{16}$ m and 1 Mpc $=10^6$ pc, so $H_0=67.4$ km/s/Mpc means that galaxies 1 Mpc apart recede from each other at 67.4 km/s. The **Hubble length** $c/H$, with $c$ the speed of light, is the distance light travels in one expansion time $1/H$. (In this section $c$ is the speed of light; from Section 11.3 on we use units in which the speed of light is 1, and $c$ then names the scale factor of the extra times.) A wave is **inside the horizon** when its physical wavelength is much shorter than $c/H$ ($K\gg H$ in units with $c=1$), and it is stretched beyond the Hubble length when the expansion makes its wavelength longer than $c/H$.

**A fluid and its equation of state.** On large scales matter is described as a fluid with an **energy density** $\rho$ (energy per volume) and a **pressure** $p$ (the flux of momentum through a surface). Their ratio

$$
w=\frac{p}{\rho}
$$

is the **equation-of-state parameter**. Three standard cases: dust (slow particles, including ordinary and dark matter) has $w=0$; radiation (particles moving at the speed of light) has $w=1/3$; a cosmological constant has $w=-1$.

**How a fluid dilutes.** In an expanding 3-space, energy conservation reads $\dot\rho=-3H(\rho+p)$. (The energy $\rho a^3$ in a unit comoving volume, whose physical volume is $a^3$, changes by the work of the pressure, $d(\rho a^3)=-p\,d(a^3)$, that is $\dot\rho a^3+3\rho a^2\dot a=-3pa^2\dot a$; divide by $a^3$ and use $\dot a/a=H$.) For constant $w$ divide by $\rho$: $d\ln\rho/dt=-3(1+w)\,d\ln a/dt$, so

$$
\rho\propto a^{-3(1+w)} .
$$

Dust dilutes as $a^{-3}$ (a fixed number of particles in a volume that grows as $a^3$), radiation as $a^{-4}$ (the same, and each photon's energy also falls as $1/a$), and a cosmological constant not at all. Worked example: for $w=-0.861$ the exponent is $-3(0.139)=-0.417$, so at $a=0.5$ the density was $2^{0.417}=1.335$ times today's value.

**Friedmann equations.** Einstein's equations (Chapter 4) for such a universe with 3 space dimensions reduce to

$$
H^2=\frac{\kappa_4}{3}\,\rho_{\mathrm{tot}},\qquad \frac{\ddot a}{a}=-\frac{\kappa_4}{6}\,(\rho_{\mathrm{tot}}+3p_{\mathrm{tot}}),
$$

with $\kappa_4=8\pi G$. Section 11.7 shows that these are the $D=4$ case of the equations that EXP-2 solves in $D=8$. The second equation says that the expansion **accelerates** ($\ddot a>0$) only if $\rho+3p<0$; for a single component with $\rho>0$ that means $w<-1/3$. This is why dark energy needs negative pressure.

**Density parameters and $\mathcal E(a)$.** The critical density is $\rho_{\mathrm{crit}}=3H_0^2/\kappa_4$, and $\Omega_i=\rho_i(a=1)/\rho_{\mathrm{crit}}$ is the density parameter of component $i$. Dividing the first Friedmann equation by $H_0^2$ gives $\mathcal E^2:=H^2/H_0^2=\sum_i\rho_i(a)/\rho_{\mathrm{crit}}$; for radiation, matter and a component $\psi$ this is $\mathcal E^2=\Omega_ra^{-4}+\Omega_ma^{-3}+\rho_\psi(a)/\rho_{\mathrm{crit}}$, and $\mathcal E(1)=1$ requires $\sum_i\Omega_i=1$ (a spatially flat universe). (The reports and figures write this ratio as $E$; we write a curly $\mathcal E$ because from Section 11.3 on $E$ is the energy of a mode.)

**Deceleration parameter.** $q_{\mathrm{dec}}=-a\ddot a/\dot a^2$. From the two Friedmann equations, $q_{\mathrm{dec}}=(\rho_{\mathrm{tot}}+3p_{\mathrm{tot}})/(2\rho_{\mathrm{tot}})$: positive when the expansion slows down, negative when it speeds up.

**Phantom.** A fluid with $\rho>0$ and $w<-1$ (equivalently $\rho+p<0$) is called **phantom**. The condition $\rho+p\ge0$ is the null energy condition. A canonical scalar field, the usual model of dark energy, has $\rho+p=\dot\phi^2\ge0$ and can never be phantom.

**The CPL form and the quoted supernova numbers.** A slowly changing $w$ is often summarised by the Chevallier-Polarski-Linder (CPL) form

$$
w(a)=w_0+w_a\,(1-a),\qquad \frac{dw}{da}=-w_a .
$$

The reference document of Stage 3 is an e-mail about the equation of state (a PDF in the author's working folder, a private input that is not committed). It quotes, for the “Unite” supernova compilation, the CPL fit $w_0=-0.861$, $w_a=-0.60$, and a constant-$w$ fit $w=-0.764$, “roughly two standard deviations” from $-1$ (a standard deviation, or one sigma, measures the statistical uncertainty of a fitted number). It gives no error bars on $(w_0,w_a)$ and cites no primary publication, so the project did not check these values against one; this chapter uses them only as quoted (Stage-3 document §3.3). Since $a$ grows with time, a field whose $w$ rises from $-1$ (called thawing) has $dw/da>0$, that is $w_a<0$. The e-mail's table writes the opposite signs; this book follows the formula: **thawing means $w_a<0$, freezing means $w_a>0$.**

**Distances.** Light from redshift $z$ has travelled the comoving distance $D_C(z)=\int_0^z c\,dz'/H(z')$. In a flat universe the luminosity distance is $d_L=(1+z)D_C$. (Light moves on $ds^2=0$; in a flat universe with the metric $ds^2=-c^2dt^2+a^2\,d\chi^2$ along its path, with $\chi$ the comoving distance, this gives $c\,dt=a\,d\chi$. With $dt=da/(aH)$, $D_C=\int c\,dt/a=\int_a^1c\,da'/(a'^2H)=\int_0^zc\,dz'/H$, since $z=1/a-1$ gives $dz=-da/a^2$. Today, with $a=1$, the light emitted by a source of luminosity $L$ (emitted power) is spread over a sphere of area $4\pi D_C^2$, and the flux $F$ (received power per area) is lowered by one factor $1+z$ from the redshift of each photon's energy and by another from the slower arrival rate of the photons: $F=L/\bigl(4\pi D_C^2(1+z)^2\bigr)$. Defining $d_L$ by $F=L/(4\pi d_L^2)$ gives $d_L=(1+z)D_C$.) Astronomers quote the **distance modulus** $\mathrm{DM}=5\log_{10}(d_L/10\,\mathrm{pc})$. DM is measured in magnitudes (mag), the logarithmic brightness unit of astronomy. A constant shift of DM is not measured independently (it depends on $H_0$ and on the true brightness of the supernovae), so fits “profile” it: they subtract the best constant offset.

**The standard model of cosmology**, called $\Lambda$CDM, contains radiation, ordinary matter, cold dark matter (CDM) and a cosmological constant $\Lambda$ ($w=-1$); it is the reference against which a varying $w$ is compared.

**What each role needs.** A dark-matter candidate must have $w\approx0$ at late times, the right abundance, (almost) no interaction with light, a long lifetime, and small enough random velocities to let structures form. A dark-energy candidate must have $\rho>0$ and $w$ near $-1$ today, stable small fluctuations, and a history in which matter dominated earlier. Sections 11.13 and 11.14 go through these lists.

### 11.3 The field in a homogeneous background: the mode equation

We now recall the field and put it into the simplest gravitational fields. Chapters 2, 4, 6 and 7 derive everything we quote here.

**A note on letters.** Cosmology and the field theory of the earlier chapters each have their customary letters, and some of them collide in this chapter. Where a collision would be confusing we rename; the letters that still have more than one meaning are listed here, with the way to tell the meanings apart.

- $c$ is the speed of light in Section 11.2 only. From here on the speed of light is 1, and $c=h_5=h_6=h_7$ is the scale factor of the extra times. Chapter 9 writes a linear $a_4$ as $ct$; this chapter writes the slope as $a_4'$ instead.
- $z$ is always the redshift of Section 11.2. Chapter 9 also calls $z=6Hx_0$ the hidden angle of the primordial field; this chapter writes that field with the proper hidden coordinate $\zeta$ and does not use the angle.
- $h$ or $h(t)$ without an index is the 16 by 16 mode Hamiltonian; $h_i$ with a direction index $i$ is a scale factor (with $h_4=1$). The real and imaginary parts of the mode Hamiltonian are written $h_{\mathrm{re}}$ and $h_{\mathrm{im}}$, and the step size of CVODE, which Chapter 10 calls $h_n$, is written $\Delta t_n$.
- $K$ and $K_j$ are physical momenta. The kinetic term of the Lagrangian, which Chapters 6 and 7 write $K$, is written $\mathcal K$ here.
- $E$ is the energy of a mode; the expansion rate relative to today is $\mathcal E=H/H_0$ (Section 11.2).
- $H$ is a Hubble rate: $H_i$ that of direction $i$ ($H_a$, $H_b$, $H_c$ for the three groups of directions), $H_0$ today's, $H_{\mathrm{in}}$ the one at the start of EXP-4a and $H_{\mathrm{inf}}$ the one during inflation; in EXP-1 and EXP-5 $H$ is the constant rate of the background. The subscript “in” also marks the starting values $t_{\mathrm{in}}$, $T_{\mathrm{in}}$ and $E_{\mathrm{in}}$ of EXP-4a.
- $\alpha$ and $\beta$ are the amplitudes of the positive- and the negative-energy level in a mode (Sections 11.6, 11.10 and 11.11). The two constants of the exact EXP-2 solution are written $\alpha_2$ and $\beta_2$ (the 2 stands for EXP-2), and the amplitude of the sudden-start wave of EXP-4a is written $\delta_k$.
- $A$ is the amplitude of the primordial window of EXP-1 (the profiles A1 and A2 of the reports); the constant $mS_0$ of EXP-3 is written $A_\psi$. The mass term of the mode Hamiltonian is written with $Z=-i\gamma^4$.
- $\varepsilon(u)$ is the energy of one quantum. The signs of the metric are $\eta_{ii}$, as in Chapters 4 and 7, and the expansion parameter of EXP-4c is $\epsilon_H=-\dot H/H^2$.
- $w$ is the equation-of-state parameter; the weights of the quadrature rule of EXP-4a are written $\omega_n$.
- $C$ is the charge matrix. $x_0$ is the hidden coordinate; in EXP-2 and EXP-3, where nothing depends on that coordinate, $x_0$ is also, as in the reports, the dimensionless coupling $x_0=\lambda S_0/(2m)$ (Section 11.7), and apart from the differential $dx_0$ in the metric it always means the coupling there.
- $T_{\mu\nu}$ is the energy–momentum tensor and $T$ without an index the set of the seven directions other than $x_4$, except in two places: in Section 11.7 $T=T^\mu{}_\mu$ is its trace, and in EXP-4a (and where Sections 11.13 and 11.15 sum it up) $T$ is a temperature.
- $\gamma^a$ with an index is a gamma matrix; the bare $\gamma$ of Section 11.9 is the exponent of a deflation. $\Omega_\mu$ is the spinor connection, and $\Omega_r$, $\Omega_m$, $\Omega_\psi$ are the density parameters of Section 11.2. $V$ is the 7-volume, and $V(\phi)$ the potential of a scalar field.

**The field.** dirac16complex is a column $\Psi=(\Psi_0,\dots,\Psi_{15})$ of 16 complex Grassmann-odd components on an 8-dimensional spacetime with coordinates $x_0,\dots,x_7$. The flat metric is $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$: directions 0 to 3 are space-like, directions 4 to 7 time-like. $x_4$ is the time $t$; $x_0$ is a hidden space direction, $x_1,x_2,x_3$ are ordinary 3-space, and $x_5,x_6,x_7$ are three extra times. We write $T=\{0,1,2,3,5,6,7\}$ for the seven directions other than $x_4$. The gamma matrices $\gamma^0,\dots,\gamma^7$ are real 16 by 16 matrices with $\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}$; $\gamma^0,\dots,\gamma^3$ are symmetric and $\gamma^4,\dots,\gamma^7$ antisymmetric (Chapter 2). The charge matrix is $C=\gamma^0\gamma^1\gamma^2\gamma^3$, the adjoint is $\bar\Psi=\Psi^\dagger C$, and $S=\bar\Psi\Psi$ is the scalar density.

**The Lagrangian and the field equation** (Chapters 6 and 7):

$$
\mathcal L=\sqrt{|g|}\Bigl[\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)-m\,S-U(S)\Bigr],\qquad U(S)=\tfrac{\lambda}{2}S^2,
$$

$$
\gamma^\mu D_\mu\Psi=M_{\mathrm{eff}}\,\Psi,\qquad M_{\mathrm{eff}}=m+U'(S)=m+\lambda S .
$$

$m$ is the mass and $\lambda$ the strength of a four-fermion contact interaction: $\lambda<0$ is attractive, $\lambda>0$ repulsive. Because $S$ is Grassmann-even of degree 2 and the algebra at a point has 32 odd generators, $S^{17}=0$, so every function $U(S)$ is a polynomial of degree at most 16 (Section 5.9 and Chapter 6). The model requires $U(0)=U'(0)=0$ (Chapter 6; Stage-1 document §7.6): no second mass term and no constant term, so **this Lagrangian contains no cosmological constant, by choice.** The Grassmann algebra itself would allow a constant term $-\sqrt{|g|}\,U(0)$, which would act as a cosmological constant. $M_{\mathrm{eff}}$ is the effective mass: the interaction shifts the mass in proportion to $S$.

**The backgrounds.** EXP-2 to EXP-5 use a homogeneous, diagonal metric with lapse 1:

$$
ds^2=-dt^2+\sum_{i\in T}\eta_{ii}\,h_i(t)^2\,dx_i^2,\qquad \eta_{ii}=+1\ (i\le3),\qquad \eta_{ii}=-1\ (i\ge5),
$$

where the signs $\eta_{ii}$ are the diagonal entries of the flat metric $\eta$ (no sum over $i$).

EXP-1 uses the warped primordial field of Section 11.6, which has the same form along $x_1,\dots,x_3,x_5,\dots,x_7$ but whose scale factors also depend on the hidden coordinate $\zeta$; Section 11.6 reduces it to the same mode equation.

$h_i(t)$ is the scale factor of direction $i$. Its Hubble rate is $H_i=\dot h_i/h_i$, the total expansion rate is $\Theta=\sum_{i\in T}H_i$, and the 7-volume is $V=\prod_{i\in T}h_i$. Taking the logarithm, $\ln V=\sum_i\ln h_i$, and differentiating gives $\dot V/V=\Theta$. The experiments group the directions: $b=h_0$ (hidden space), $a=h_1=h_2=h_3$ (3-space) and $c=h_5=h_6=h_7$ (extra times), so that $\Theta=H_b+3H_a+3H_c$ and $V=b\,a^3c^3$.

**Vielbein and connection.** The vielbein (Chapter 4) is $e^4=dt$ and $e^i=h_i\,dx_i$, so that $ds^2=\eta_{ab}e^ae^b$. The gamma matrices with a curved index are $\gamma^{x_4}=\gamma^4$ and $\gamma^{x_i}=\gamma^i/h_i$. For a diagonal vielbein $e^b=h_b\,dx_b$ Chapter 4 (and Stage-1 document §8.5) gives

$$
\gamma^\mu\Omega_\mu=\frac12\sum_{b=0}^{7}\frac{1}{h_b}\,\partial_b\ln\Bigl(\prod_{c\ne b}h_c\Bigr)\,\gamma^b .
$$

Here everything depends on $t=x_4$ only, so only $b=4$ contributes, with $h_4=1$ and $\prod_{c\ne4}h_c=V$:

$$
\gamma^\mu\Omega_\mu=\tfrac12\,\frac{\dot V}{V}\,\gamma^4=\tfrac12\,\Theta\,\gamma^4 .
$$

**The mode ansatz.** Take a plane wave with coordinate momentum $k_j$ along the directions $j\in T$,

$$
\Psi=V^{-1/2}\,e^{i\sum_jk_jx_j}\,u(t),
$$

where $u(t)$ is an ordinary column of 16 complex numbers (the **mode amplitude**). The Grassmann nature of the field enters only through the counting of states and through the expectation-value rule of Section 11.4. Insert the ansatz into $\gamma^\mu D_\mu\Psi=\gamma^{x_4}\partial_4\Psi+\sum_j\gamma^{x_j}\partial_j\Psi+\gamma^\mu\Omega_\mu\Psi$, one term at a time, and drop the common factor $V^{-1/2}e^{ik\cdot x}$:

1. time derivative: $\partial_4(V^{-1/2}u)=V^{-1/2}\bigl(\dot u-\tfrac12\Theta u\bigr)$, which gives $\gamma^4\dot u-\tfrac12\Theta\gamma^4u$;
2. space derivatives: $\partial_j\Psi=ik_j\Psi$ and $\gamma^{x_j}=\gamma^j/h_j$ give $i\sum_jK_j\gamma^ju$, where $K_j:=k_j/h_j$ is the **physical momentum** along $j$;
3. connection: $+\tfrac12\Theta\gamma^4u$.

The two $\Theta$ terms cancel exactly; that is why the factor $V^{-1/2}$ was put in front. What remains is $\gamma^4\dot u+i\sum_jK_j\gamma^ju=M_{\mathrm{eff}}u$. Multiply from the left by $\gamma^4$ and use $(\gamma^4)^2=-1$: $-\dot u+i\sum_jK_j\gamma^4\gamma^ju=M_{\mathrm{eff}}\gamma^4u$. Multiply by $-i$ and rearrange:

$$
i\,\dot u=h(t)\,u,\qquad h(t)=-iM_{\mathrm{eff}}\gamma^4-\sum_{j\in T}K_j\,\gamma^4\gamma^j .
$$

This looks like a Schrödinger equation with a 16 by 16 **mode Hamiltonian** $h(t)$.

**The square of $h$.** Write $Z=-i\gamma^4$, so that the mass term of $h$ is $M_{\mathrm{eff}}Z$, and $P_j=-K_j\gamma^4\gamma^j$. Three small computations with the Clifford relation, using $\gamma^j\gamma^4=-\gamma^4\gamma^j$ for $j\ne4$ and hence $\gamma^4\gamma^j\gamma^4=-\gamma^4\gamma^4\gamma^j=\gamma^j$:

- $(M_{\mathrm{eff}}Z)^2=-M_{\mathrm{eff}}^2(\gamma^4)^2=M_{\mathrm{eff}}^2$;
- $ZP_j+P_jZ=iK_j\bigl(\gamma^4\gamma^4\gamma^j+\gamma^4\gamma^j\gamma^4\bigr)=iK_j(-\gamma^j+\gamma^j)=0$;
- $P_jP_l+P_lP_j=K_jK_l\bigl(\gamma^4\gamma^j\gamma^4\gamma^l+\gamma^4\gamma^l\gamma^4\gamma^j\bigr)=K_jK_l(\gamma^j\gamma^l+\gamma^l\gamma^j)=2\eta^{jl}K_jK_l$.

Expanding $h^2=(M_{\mathrm{eff}}Z+\sum_jP_j)^2$ and collecting terms:

$$
h^2=E^2\cdot1,\qquad E^2=M_{\mathrm{eff}}^2+\sum_{j=0}^{3}K_j^2-\sum_{j=5}^{7}K_j^2 .
$$

So the only possible eigenvalues of $h$ are $+E$ and $-E$. Because $h$ has zero trace (the diagonal of the antisymmetric $\gamma^4$ is zero, and $\mathrm{tr}(\gamma^4\gamma^j)=-\mathrm{tr}(\gamma^j\gamma^4)=-\mathrm{tr}(\gamma^4\gamma^j)$ forces $\mathrm{tr}(\gamma^4\gamma^j)=0$), each occurs eight times when $E\ne0$.

**When is $h$ Hermitian?** A real symmetric matrix is Hermitian, a real antisymmetric one satisfies $M^\dagger=-M$. Since $\gamma^4$ is real antisymmetric, $(-iM_{\mathrm{eff}}\gamma^4)^\dagger=iM_{\mathrm{eff}}(-\gamma^4)=-iM_{\mathrm{eff}}\gamma^4$: Hermitian. For $j\le3$, $(\gamma^4\gamma^j)^\dagger=(\gamma^j)^T(\gamma^4)^T=\gamma^j(-\gamma^4)=\gamma^4\gamma^j$: Hermitian. For $j\ge5$, $(\gamma^4\gamma^j)^\dagger=(-\gamma^j)(-\gamma^4)=\gamma^j\gamma^4=-\gamma^4\gamma^j$: anti-Hermitian. Hence

$$
h^\dagger=h\quad\Longleftrightarrow\quad K_5=K_6=K_7=0 .
$$

The modes without momentum along the extra times form the **good sector**. There $E^2>0$, and the **Hilbert norm** $u^\dagger u$ is conserved: $\frac{d}{dt}(u^\dagger u)=\dot u^\dagger u+u^\dagger\dot u=(-ihu)^\dagger u+u^\dagger(-ihu)=i\,u^\dagger(h^\dagger-h)\,u=0$.

**The Krein norm.** The matrix $B=-iC\gamma^4$ is Hermitian with $B^2=1$ and has eigenvalues $+1$ and $-1$, eight each (Chapters 2 and 8). $C$ contains $\gamma^0,\dots,\gamma^3$ once each; moving $\gamma^a$ with $a\le3$ through $C$ meets three gammas that anticommute with it, so $C\gamma^a=-\gamma^aC$ for $a\le3$, while for $a\ge4$ all four gammas of $C$ anticommute with $\gamma^a$, the four signs cancel, and $C\gamma^a=\gamma^aC$. It follows that $\gamma^4$ and $\gamma^j$ ($j\le3$) commute with $B$ and $\gamma^j$ ($j\ge5$) anticommutes with it; for example, for $j\ge5$, $\gamma^jB=-i\gamma^jC\gamma^4=-iC\gamma^j\gamma^4=iC\gamma^4\gamma^j=-B\gamma^j$. Now check $h^\dagger B=Bh$ term by term. The term $-iM_{\mathrm{eff}}\gamma^4$ is Hermitian and commutes with $B$. For $j\le3$ the term $-K_j\gamma^4\gamma^j$ is Hermitian and commutes with $B$. For $j\ge5$ it is anti-Hermitian and anticommutes with $B$, so $(\gamma^4\gamma^j)^\dagger B=-\gamma^4\gamma^jB=B\gamma^4\gamma^j$. Hence $h^\dagger B=Bh$ for every momentum. Then $\frac{d}{dt}(u^\dagger Bu)=i\,u^\dagger(h^\dagger B-Bh)\,u=0$: the **Krein norm** $u^\dagger Bu$, which can be positive, negative or zero, is conserved always, in and out of the good sector.

**What the computer integrates.** A computer program integrates real numbers. Write $u=x+iy$ and $h=h_{\mathrm{re}}+i\,h_{\mathrm{im}}$ with real columns $x,y$ and real matrices $h_{\mathrm{re}},h_{\mathrm{im}}$ (not to be confused with the scale factors $h_i$). The real and imaginary parts of $i(\dot x+i\dot y)=(h_{\mathrm{re}}+i\,h_{\mathrm{im}})(x+iy)$ give

$$
\dot x=h_{\mathrm{re}}\,y+h_{\mathrm{im}}\,x,\qquad \dot y=h_{\mathrm{im}}\,y-h_{\mathrm{re}}\,x .
$$

The state is 32 real numbers: $\mathrm{Re}\,u_0,\dots,\mathrm{Re}\,u_{15}$ and then $\mathrm{Im}\,u_0,\dots,\mathrm{Im}\,u_{15}$, the columns `u_re_0` to `u_re_15` and `u_im_0` to `u_im_15` of the output files. For $h=-iM_{\mathrm{eff}}\gamma^4-\sum_jK_j\gamma^4\gamma^j$ the pieces are $h_{\mathrm{im}}=-M_{\mathrm{eff}}\gamma^4$ and $h_{\mathrm{re}}=-\sum_jK_j\gamma^4\gamma^j$.

### 11.4 Energy density, pressure and the expectation-value rule

**The energy-momentum tensor.** Chapter 7 derives the energy-momentum tensor of the field:

$$
T_{\mu\nu}=-\tfrac14\Bigl[\bar\Psi\gamma_\mu D_\nu\Psi+\bar\Psi\gamma_\nu D_\mu\Psi-(D_\mu\bar\Psi)\gamma_\nu\Psi-(D_\nu\bar\Psi)\gamma_\mu\Psi\Bigr]+g_{\mu\nu}\,\mathcal L_s,\qquad \mathcal L_s=\mathcal K-mS-U(S),
$$

where $\mathcal K=\tfrac12\bigl(\bar\Psi\gamma^\mu D_\mu\Psi-(D_\mu\bar\Psi)\gamma^\mu\Psi\bigr)$ is the kinetic term (Chapters 6 and 7 write it $K$; in this chapter $K$ is a momentum). An observer at rest in the coordinates (whose 8-velocity is $\partial_4$, a unit time-like vector because $g_{44}=-1$) measures the energy density $\rho=T_{44}$ and, in each of the seven directions $i\in T$, the pressure $p_{(i)}=T^i{}_i$ (no sum over $i$). Four of these directions are space-like and three are time-like. When the pressures differ one uses the mean $\bar p=\tfrac17\sum_{i\in T}p_{(i)}$ and $\bar w=\bar p/\rho$.

**The homogeneous condensate.** Contracting the field equation with $\bar\Psi$, and its adjoint with $\Psi$, gives on shell $\mathcal K=M_{\mathrm{eff}}S$, hence $\mathcal L_s=M_{\mathrm{eff}}S-mS-U=SU'(S)-U(S)$. For a state that depends on $t$ only (a homogeneous condensate) in the diagonal backgrounds of Section 11.3, Section 7.10 shows that the kinetic bracket contributes nothing to the seven transverse diagonal components: the field does not depend on $x_i$, so only the connection $\Omega_i$ enters $T_{ii}$, through the anticommutator $\{\gamma_i,\Omega_i\}$, which vanishes. So $T^i{}_i=\mathcal L_s$ for every $i\in T$ (also Stage-1 document §9.7, where it is checked in exact arithmetic at three test times of a homogeneous diagonal frame: checks `EMT_homogeneousReduction_G3` of the Wolfram geometry verifier and `EMT_homogeneousReduction` of the Python geometry checker, reports under `artifacts/dirac16complex/arbitrary-field/`). The trace of $T$ supplies the time-time component: $g^{\mu\nu}\gamma_\mu=\gamma^\nu$ turns the bracket into $-\mathcal K$ and $g^{\mu\nu}g_{\mu\nu}=8$, so $T^\mu{}_\mu=-\mathcal K+8\mathcal L_s$. Subtracting the seven transverse components, $T^4{}_4=-\mathcal K+\mathcal L_s$, and with $T_{44}=g_{44}T^4{}_4=-T^4{}_4$,

$$
\rho=\mathcal K-\mathcal L_s=M_{\mathrm{eff}}S-(SU'-U)=mS+U,\qquad p=\mathcal L_s=SU'-U .
$$

For $U=\tfrac\lambda2S^2$:

$$
\rho=mS+\tfrac\lambda2S^2,\qquad p=\tfrac\lambda2S^2,\qquad w=\frac{\lambda S}{2m+\lambda S} .
$$

So a free condensate ($\lambda=0$) is dust, a repulsive one ($\lambda>0$) has positive pressure, and an attractive one ($\lambda<0$) has negative pressure. The pressure is the same in all seven directions although the scale factors differ.

**Kinetic and potential energy.** A canonical scalar field with the potential $V(\phi)$ (Section 5.8; not the 7-volume) has $\rho=\tfrac12\dot\phi^2+V(\phi)$ and $p=\tfrac12\dot\phi^2-V(\phi)$. Stage 1 defines two exact analogues for dirac16complex (Chapter 7). Split the kinetic term into its time part and the rest, $\mathcal K=\mathcal K_4+\mathcal K_\perp$, with $\mathcal K_4=\tfrac12\bigl(\bar\Psi\gamma^{x_4}D_4\Psi-(D_4\bar\Psi)\gamma^{x_4}\Psi\bigr)$.

- **(A) Lagrangian split:** $\mathrm{KE}_L=\tfrac12\mathcal K_4$ and $\mathrm{PE}_L=\rho-\mathrm{KE}_L$.
- **(B) Hamiltonian split:** $\mathrm{KE}_H=-\mathcal K_\perp$ (momentum or gradient energy) and $\mathrm{PE}_H=mS+U$ (rest mass and interaction). $\rho=\mathrm{KE}_H+\mathrm{PE}_H$ holds identically.

For the condensate $\mathcal K_\perp=0$ (Section 7.10): it has no momentum, and the connection terms cancel in the antisymmetrised combination; equivalently, $\mathrm{KE}_H=\rho-\mathrm{PE}_H=0$ because $\rho=mS+U$ above. So $\mathcal K_4=\mathcal K=M_{\mathrm{eff}}S$ and

$$
\mathrm{KE}_L=\tfrac12S\,M_{\mathrm{eff}},\qquad \mathrm{PE}_L=mS+\tfrac\lambda2S^2-\tfrac12(m+\lambda S)S=\tfrac12mS,\qquad \mathrm{KE}_H=0,\qquad \mathrm{PE}_H=\rho .
$$

Then $\mathrm{KE}_L+\mathrm{PE}_L=\rho$ and $\mathrm{KE}_L-\mathrm{PE}_L=\tfrac12\lambda S^2=p$, exactly as for the scalar field, and

$$
\rho+p=2\,\mathrm{KE}_L=S\,M_{\mathrm{eff}} .
$$

**Phantom criterion.** For $\rho>0$, $w<-1$ holds exactly when $\rho+p<0$, that is when $\mathrm{KE}_L<0$, that is when $S\,M_{\mathrm{eff}}<0$. Unlike $\tfrac12\dot\phi^2$, $\mathrm{KE}_L$ has no fixed sign. Worked example with $m=1$ and $S>0$: for $\lambda S=-1.5$ we get $M_{\mathrm{eff}}=-0.5$, $\rho=S(1-0.75)=0.25\,S>0$, $p=-0.75\,S$ and $w=-1.5/0.5=-3$, a phantom value; for $\lambda S=-0.5$ we get $M_{\mathrm{eff}}=0.5$ and $w=-0.5/1.5=-1/3$, not phantom. Whether the phantom case describes a physical state is the question of the mean-field limits below.

**Per-mode quantities and the expectation-value rule.** Chapter 8 quantises the field with respect to $t=x_4$. The anticommutator is $\{\Psi,\Psi^\dagger\}=B\,\delta^7/\sqrt{|g|}$, and because $B$ has eigenvalues of both signs the state space carries an indefinite inner product (a Krein space). In the good sector there is nevertheless an ordinary Fock space: particles and antiparticles of energy $\sqrt{m^2+K^2}$ above a filled **Dirac sea** of negative-energy states. Energies are measured relative to the filled sea (**normal ordering**). In this positive-norm quantisation a one-particle state built on a normalised positive-energy mode $u$ ($u^\dagger u=1$) has the **expectation-value rule**

$$
\langle\Psi^\dagger M\Psi\rangle=u^\dagger BM\,u
$$

for any 16 by 16 matrix $M$ (Section 8.12 derives it; also Stage-3 document §4.6). Since $C$ commutes with $\gamma^4$ and $C^2=1$, $BC=-iC\gamma^4C=-i\gamma^4$. Three quantities per mode follow:

$$
s(u)=u^\dagger BC\,u=u^\dagger(-i\gamma^4)\,u,\qquad \varepsilon(u)=u^\dagger h\,u,\qquad p_j(u)=-K_j\,u^\dagger\gamma^4\gamma^ju\quad(\text{no sum}),
$$

the scalar density, the energy and the pressure along $j$ of one quantum.

**Why $\varepsilon$ and $p_j$ are the energy and the pressure.** The formula for $T_{\mu\nu}$ above, with $\gamma_4=g_{44}\gamma^{x_4}=-\gamma^4$ and $g^{jj}\gamma_j=\gamma^{x_j}$, gives

$$
T_{44}=\mathcal K_4-\mathcal L_s,\qquad T^j{}_j=-\tfrac12\bigl(\bar\Psi\gamma^{x_j}D_j\Psi-(D_j\bar\Psi)\gamma^{x_j}\Psi\bigr)+\mathcal L_s\quad(\text{no sum}),
$$

and for $\lambda=0$ the on-shell $\mathcal L_s=SU'-U$ vanishes. Take $\Psi=V^{-1/2}e^{ik\cdot x}u$ in a good-sector background of Section 11.3. The real factor $V^{-1/2}$ drops out of these antisymmetric combinations, because its derivative gives $-\tfrac12\Theta$ times the same bilinear in both terms. The connection terms drop out too. By Section 4.12, $\Omega_\mu$ is the sum over $b\ne\mu$ of $\omega_{\mu\mu b}S^{\mu b}$ with $S^{\mu b}=\tfrac12\gamma^\mu\gamma^b$ and $\omega_{\mu\mu b}$ proportional to $\partial_bh_\mu$. Here $h_4=1$, so $\Omega_4=0$, and $\Omega_j$ is a multiple of $\gamma^j\gamma^4$. With $D_j\bar\Psi=\partial_j\bar\Psi-\bar\Psi\Omega_j$ (Chapter 6) the connection enters $T^j{}_j$ only as $\bar\Psi\{\gamma^{x_j},\Omega_j\}\Psi$, which vanishes because $\gamma^j$ anticommutes with $\gamma^j\gamma^4$. What remains is evaluated with $\dot u=-ihu$, $\partial_j\Psi=ik_j\Psi$ and the rule, using $BC\gamma^4=(-i\gamma^4)\gamma^4=i$.

- **Time part.** $\Psi^\dagger C\gamma^4\partial_4\Psi\mapsto u^\dagger(BC\gamma^4)(-ih)u=u^\dagger(i)(-ih)u=u^\dagger hu$. Next, $(\partial_4\Psi)^\dagger=i\Psi^\dagger h$ ($h$ is Hermitian), and $B$ commutes with $h$ in the good sector (from $h^\dagger B=Bh$ and $h^\dagger=h$), so $-(\partial_4\Psi^\dagger)C\gamma^4\Psi\mapsto-i\,u^\dagger BhC\gamma^4u=-i\,u^\dagger h(BC\gamma^4)u=u^\dagger hu$. Hence $\mathcal K_4\mapsto\tfrac12(u^\dagger hu+u^\dagger hu)=\varepsilon(u)$.
- **Space part.** $\partial_j\Psi=ik_j\Psi$ and $\partial_j\bar\Psi=-ik_j\bar\Psi$ turn the bracket into $2ik_j\bar\Psi\gamma^{x_j}\Psi=2iK_j\Psi^\dagger C\gamma^j\Psi$ (with $\gamma^{x_j}=\gamma^j/h_j$ and $K_j=k_j/h_j$). So $T^j{}_j=-iK_j\Psi^\dagger C\gamma^j\Psi\mapsto-iK_j\,u^\dagger(BC)\gamma^ju=-iK_j\,u^\dagger(-i\gamma^4)\gamma^ju=-K_j\,u^\dagger\gamma^4\gamma^ju=p_j(u)$.

For $\lambda\ne0$ the same steps, with $\mathcal L_s=SU'-U=\tfrac\lambda2S^2$, give the recorded $\rho=S_0\varepsilon-\tfrac\lambda2S^2$ and $p_j=S_0\,p_j(u)+\tfrac\lambda2S^2$ of Section 11.6 (there the factor $e^{-3H\zeta}$ plays the role of $V^{-1/2}$, and $\Omega_j$ also contains a multiple of $\gamma^j\gamma^0$, which anticommutes with $\gamma^j$ as well).

Reading off the definition of $h$, the three quantities satisfy $\varepsilon=M_{\mathrm{eff}}\,s+\sum_jp_j$. On a normalised good-sector eigenmode $hu=Eu$ they take simple values. The anticommutators computed in Section 11.3 give $\{h,Z\}=2M_{\mathrm{eff}}$ with $Z=-i\gamma^4$ (only the mass term $M_{\mathrm{eff}}Z$ survives, since $Z^2=1$ and $Z$ anticommutes with every $\gamma^4\gamma^j$). Sandwich this between $u^\dagger$ and $u$ and use $hu=Eu$ and $u^\dagger h=Eu^\dagger$ ($h$ Hermitian): $2E\,s=2M_{\mathrm{eff}}$, so $s=M_{\mathrm{eff}}/E$. In the same way $\{h,-\gamma^4\gamma^j\}=2K_j$ for $j\le3$ gives $p_j=K_j^2/E$. So a quantum at rest has $s=1$ and $\varepsilon=M_{\mathrm{eff}}$, and a moving one has a pressure equal to its momentum flux.

**Worked example: a quantum at rest.** For $K=0$, $h=-iM\gamma^4$, and a positive-energy eigenvector satisfies $-i\gamma^4u=u$. The program's standard choice is

$$
u_0=\tfrac12\bigl(e_0-e_4-i\,e_9-i\,e_{13}\bigr),
$$

where $e_n$ is the column with 1 in place $n$ (counting from 0). Only four rows of $\gamma^4$ matter: $(\gamma^4v)_0=-v_{13}$, $(\gamma^4v)_4=+v_9$, $(\gamma^4v)_9=-v_4$ and $(\gamma^4v)_{13}=+v_0$ (the tables of Chapter 2 and of the student guide, §6.3). Then $(\gamma^4u_0)_0=-(-i/2)=i/2$, so $(-i\gamma^4u_0)_0=1/2=(u_0)_0$; similarly $(-i\gamma^4u_0)_4=-i(-i/2)=-1/2$, $(-i\gamma^4u_0)_9=-i(1/2)=-i/2$ and $(-i\gamma^4u_0)_{13}=-i/2$, which are the components of $u_0$. Hence $hu_0=Mu_0$ and $s(u_0)=u_0^\dagger u_0=4\cdot\tfrac14=1$. The same four rows of $B$, $(Bv)_0=iv_9$, $(Bv)_4=-iv_{13}$, $(Bv)_9=-iv_0$ and $(Bv)_{13}=iv_4$, give $Bu_0=u_0$: $u_0$ has Krein sign $+1$.

**The dilution law.** At $K=0$, $h=M_{\mathrm{eff}}(t)\,(-i\gamma^4)$ is a multiple of $-i\gamma^4$ at every time. Then $\frac{d}{dt}s(u)=i\,u^\dagger\bigl[h,(-i\gamma^4)\bigr]u=0$ (the same computation as for the Hilbert norm, with $h$ Hermitian), for any $M_{\mathrm{eff}}(t)$. The bilinear of $\Psi=V^{-1/2}u$ carries the factor $1/V$, so

$$
S=S_0\,\frac{V_0}{V}\,s(u),\qquad S\,V=\text{constant}.
$$

**This law drives almost everything that follows.** The mass term $mS\propto V^{-1}$ dilutes like dust in the 7-volume, while the interaction term $\tfrac\lambda2S^2\propto V^{-2}$ dominates at small volume and dies away at large volume. (Stage 1 derives the same law from energy conservation, $\partial_4\rho+\sum_iH_i(\rho+p_{(i)})=0$ with $\rho+p=SM_{\mathrm{eff}}$, wherever $M_{\mathrm{eff}}\ne0$.)

**The mean-field picture and its three limits.** In EXP-1 to EXP-3 one mode stands for a macroscopic density of quanta, with $S$ in $M_{\mathrm{eff}}=m+\lambda S$ replaced by its average value. This is a **mean-field** (Hartree) approximation: each quantum moves in the average field of all the others (Chapter 12 introduces the Hartree idea in general). The density is written $S=S_0\,s(u)$ (times $V_0/V$). Three limits decide what the results mean (Stage-3 document §4.6).

1. **The occupied level must stay a positive-energy level.** At $K=0$ the rest eigenvector only changes its phase, $u(t)=e^{-i\int M_{\mathrm{eff}}dt}u_0$, so $s(u)=1$ stays fixed while $M_{\mathrm{eff}}$ may change sign. When $M_{\mathrm{eff}}<0$, $\varepsilon=u^\dagger hu=M_{\mathrm{eff}}<0$: the single occupied mode has become a negative-energy state of the instantaneous $h$. The expectation-value rule is stated for a quantum above the sea, so it no longer describes the state. Every row with $M_{\mathrm{eff}}<0$ in EXP-2 and EXP-3, which includes every phantom row and every row with $\rho<0$, is therefore an **artefact of the mean field with fixed normal ordering**, not an established property of the field.
2. **The Pauli principle.** For a Grassmann field each state is occupied at most once, and there are 8 positive-energy states per momentum ($h$ has the eigenvalue $+E$ eight times). A finite density of quanta cannot all sit in the $K=0$ mode. The homogeneous state of lowest energy that obeys the Pauli principle is a **filled Fermi sea**: every positive-energy state with a momentum of size $|K|<k_F$ is occupied once and every state with $|K|>k_F$ is empty, where the **Fermi momentum** $k_F$ is fixed by the density (Chapter 12 calls the filled ball of momenta the Fermi sphere, Section 12.12). The quanta of a Fermi sea therefore move even at zero temperature, and their momentum flux is a pressure, the **degeneracy pressure**, which the one-mode picture leaves out; it is negligible only when $k_F\ll m$. This pressure was not computed. For the free condensate of EXP-3 an order-of-magnitude estimate (fits.json, `meanFieldScales`, with today's Hubble rate $H_0=67.4$ km/s/Mpc) gives $k_F=0.57$ meV at $m=1$ eV (an electron-volt, eV, is the energy unit of particle physics, and 1 meV $=10^{-3}$ eV), and $k_F/m\le0.1$ for $m\ge21$ meV. The interaction is also treated only at Hartree level; the exchange (Fock) term, the correction that the antisymmetry of fermion states adds to the average-field energy (Section 12.6), is for a contact interaction of the same order and is not included.
3. **The strength of the tuned coupling.** When the attractive models of EXP-3 are tuned to the quoted $w_0$, the coupling in physical units comes out as $\lambda m^2=-0.497\,(m/2.25\ \mathrm{meV})^4$ (fits.json, `meanFieldScales`). Here $\lambda$ is the coupling of the 3-space density $S$ of EXP-3, with the static extra dimensions absorbed. In units with $\hbar$ and the speed of light equal to 1 every quantity is a power of a mass, and that power is its **mass dimension**: a mass or a momentum has mass dimension 1, a length or a time $-1$. This $\lambda$ has mass dimension $-2$, so $\lambda m^2$ is a pure number. (In the 8-dimensional Lagrangian $\lambda$ has mass dimension $-6$, Section 13.8.) Where the Pauli caveat is negligible this is ultra-strong: at $m=24$ meV (where $k_F/m=0.1$ for that model) $\lambda m^2=-6.8\times10^{3}$. Conversely $|\lambda|m^2\le2$ needs $m\le3.2$ meV, where $k_F/m\ge1.5$. So no mass makes both the one-mode picture and a weak Hartree interaction self-consistent for those models. These are estimates from closed forms, not results of the differential equations.

**States of definite particle number are never phantom** (derived in Stage-3 document §4.4, not machine-checked). Take a state in which each positive-energy mode is either occupied or empty, with occupation numbers $n$, at Hartree level. Each occupied mode contributes its energy $E$ to $\rho$ and its momentum flux, $K^2/(dE)$ after averaging over $d$ directions, to $p$. The interaction adds $-\tfrac\lambda2S^2$ to $\rho$ (the Hartree double-counting correction) and $+\tfrac\lambda2S^2$ to $p$, which cancel in the sum:

$$
\rho+p=\sum n\,\Bigl(E+\frac{K^2}{d\,E}\Bigr)\ \ge\ 0 .
$$

Superpositions of the vacuum and pair states (such as the states created in EXP-4b) are allowed states of the same theory whose pressure contains a term linear in the pair amplitude; they can have $\rho+p<0$ with $\rho>0$ for a while, a known effect in quantum field theory. That is not the mechanism of the phantom rows of EXP-2 and EXP-3, which lie where the occupied rest level has become a negative-energy level.

### 11.5 How the five experiments were computed and checked

Every differential equation below is integrated by CVODE, the solver of the pure-Rust SUNDIALS 7.8.0 engine of the rustSolveIt repositories (Chapter 10 explains how such a solver works). The setup scripts `scripts/setup_solver.ps1` and `scripts/setup_solver.sh` clone the engine at a pinned commit into the git-ignored folder `vendor/rustSolveIt`; the committed outputs were produced with the Windows 11 engine (commit a8fdff45), which reproduces them byte for byte on Windows and Linux. To get byte identity, install that engine explicitly (`bash scripts/setup_solver.sh win11`; `scripts/setup_solver.ps1` defaults to it). Without the argument `setup_solver.sh` installs the platform's own engine. With the Linux engine all checks pass, but 14 committed files differ in their last digits and the Jupyter notebook stops at its byte-identity assertion (measured; student guide §4.5). The macOS engine is identical to the Linux one and is expected to behave the same way, but it was not run. Two CVODE configurations are used: BDF with Newton iteration and a dense linear solver (EXP-1), and Adams-Moulton with fixed-point iteration (EXP-2 to EXP-5), the classical choice for non-stiff oscillations. The program is the Rust crate `studies/dirac16complex_cosmology`; its gamma matrices, $C$, $\gamma^8$ and $B$ are generated from the exact Stage-1 fixture `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`, and every output records the fixture's sha256.

| Experiment | CVODE method | rtol, atol | max step | steps | right-hand sides |
| --- | --- | --- | --- | --- | --- |
| EXP-1 | BDF + Newton | $10^{-12}$, $10^{-14}$ | 0.02 | 33866 | 34950 |
| EXP-2 | Adams + fixed point | $10^{-12}$, $10^{-15}$ | 0.02 | 1779784 | 1781396 |
| EXP-3 | Adams + fixed point | $10^{-11}$, $10^{-13}$ | 0.01 in $N$ | 6074 | 10115 |
| EXP-4 | Adams + fixed point | $10^{-13}$, $10^{-14}$ | 2.0 | 339071692 | 511425232 |
| EXP-5 | Adams + fixed point | $10^{-10}$, $10^{-12}$ | 0.02 | 2548 | 4800 |

Three layers of checking stand behind every number:

1. **Self-checks of the program.** Each experiment tests its own results against exact solutions, conserved quantities and a priori limits and prints PASS or FAIL; the last line is SUCCESS or FAILURE. 69 of 69 self-checks pass (10, 15, 14, 23 and 7 for EXP-1 to EXP-5).
2. **Independent checkers.** `scripts/check_dirac16complex_exp1.py` to `check_dirac16complex_exp5.py` use only numpy and the standard library. Each rebuilds the gamma matrices from the fixture and recomputes every physical quantity from the raw spinor columns of the output files, never from the program's derived columns. Each also reruns the program into a fresh folder and requires every file to be byte-identical (**repeat-run byte identity**), and reruns it with ten times tighter tolerances and requires the errors to shrink or to stay at an identified floor (**refined convergence**). 167 of 167 checks pass (25, 35, 32, 54 and 21). The EXP-3 fit analysis `scripts/analyze_dirac16complex_exp3.py` passes its own 10 of 10 checks.
3. **Two notebooks.** The Jupyter notebook `notebooks/dirac16complex_dark_sector.ipynb` reruns everything, recomputes the physics and draws the 17 figures of `artifacts/dirac16complex/numerics/figures/` (71 of 71 assertions, `notebook-report.json`). The Mathematica notebook `notebooks/Dirac16ComplexDarkSector.nb` re-derives every reduced equation symbolically and re-integrates the solutions with NDSolve (49 of 49 checks, `mathematica-report.json`). None of the three rustSolveIt repositories contains a Mathematica notebook, so this one is new.

The collected verdict in `numerics-summary.json` is SUCCESS. Chapter 19 lists the commands that reproduce all of this.

### 11.6 EXP-1: the frozen field in the primordial background

**Purpose.** The primordial field of the author's notebook (Chapter 9) inflates 3-space while the three extra times deflate, and the 7-volume stays constant. EXP-1 asks what dirac16complex does in this field, and what source 8-dimensional Einstein gravity would need to produce the field.

**The background.** With $H=1$ and $t=Hx_4$, and with the proper hidden coordinate $\zeta=\ln\bigl(\sin(6Hx_0)\bigr)/(6H)$, which runs from $-\infty$ to 0 (Chapter 9, which calls $6Hx_0$ the hidden angle $z$; here $z$ is the redshift), the metric is

$$
ds^2=d\zeta^2-dt^2+e^{2H\zeta}\Bigl[e^{2a_4(t)}\bigl(dx_1^2+dx_2^2+dx_3^2\bigr)-e^{-2a_4(t)}\bigl(dx_5^2+dx_6^2+dx_7^2\bigr)\Bigr].
$$

3-space grows as $e^{a_4}$ and the extra times shrink as $e^{-a_4}$, so the product of the seven scale factors does not depend on $t$: the 7-volume is constant. The experiment uses a **primordial window**, a smooth switch-on and switch-off of the expansion,

$$
a_4'(t)=\tfrac A4\Bigl(1+\tanh\tfrac{t-t_1}{\Delta}\Bigr)\Bigl(1-\tanh\tfrac{t-t_2}{\Delta}\Bigr),\qquad A\in\{1,2\},\quad t_1=2,\quad t_2=7,\quad \Delta=0.5 .
$$

Between $t_1$ and $t_2$ both brackets are close to 2, so $a_4'\approx A$ and 3-space grows by about $e^{A(t_2-t_1)}=e^{5A}$ in total. The program uses the exact integral of this formula, $a_4(t)=A\Delta\,[\ell(2(t-t_1)/\Delta)-\ell(2(t-t_2)/\Delta)]/\bigl(2(1-e^{-2(t_2-t_1)/\Delta})\bigr)$ with $\ell(x)=\ln(1+e^x)$ (Stage-3 document §6.2).

**The reduction to a mode equation.** Here the vielbein depends on $\zeta$ and $t$: $h_0=1$ for the $\zeta$ direction, $h_{1,2,3}=e^{H\zeta+a_4}$ and $h_{5,6,7}=e^{H\zeta-a_4}$. Apply the connection formula of Section 11.3 with $b=0$ and $b=4$. For $b=0$: $\prod_{c\ne0}h_c=e^{3(H\zeta+a_4)}e^{3(H\zeta-a_4)}=e^{6H\zeta}$, and $\partial_\zeta\ln e^{6H\zeta}=6H$. For $b=4$: $\prod_{c\ne4}h_c=e^{6H\zeta}$ does not depend on $t$. Hence

$$
\gamma^\mu\Omega_\mu=3H\,\gamma^0 ,
$$

and **$a_4$ has dropped out**. Take a wave in the hidden direction and no momentum elsewhere, $\Psi=e^{-3H\zeta}e^{iK\zeta}u(t)$. The $\zeta$-derivative gives $\gamma^0(-3H+iK)\Psi$; the $-3H$ cancels the connection term $3H\gamma^0\Psi$ (the factor $e^{-3H\zeta}$ plays the role of $V^{-1/2}$), and what remains is

$$
\gamma^4\dot u=(M_{\mathrm{eff}}-iK\gamma^0)\,u\quad\Longleftrightarrow\quad i\dot u=h\,u,\qquad h=-iM_{\mathrm{eff}}\gamma^4-K\gamma^4\gamma^0 .
$$

This is the equation of Section 11.3 with the single momentum $K_0=K$. Stage 2 verified the reduction exactly (Wolfram check `P_modes_exactReduction`) for $\lambda=0$, and the Mathematica notebook derives it again symbolically. For $\lambda\ne0$ it holds only pointwise: the scalar density of this mode is $S=S_0\,s(u)\,e^{-6H\zeta}$ (the square of the factor $e^{-3H\zeta}$), which depends on $x_0$, so $M_{\mathrm{eff}}=m+\lambda S$ is not the same at every $x_0$, and the one run with $\lambda\ne0$ treats $S_0$ as the local density factor at one fixed $x_0$ (a mean-field approximation). For the same reason the $K=0$ state is not a homogeneous condensate: its density varies as $e^{-6H\zeta}$ along the hidden direction.

**What is recorded.** With the density factor $S_0$ and $S=S_0\,s(u)$ (Stage-3 document §6.2):

$$
\rho=S_0\,u^\dagger hu-\tfrac\lambda2S^2,\qquad p_j=S_0\,p_j(u)+\tfrac\lambda2S^2,\qquad \bar p=\tfrac17\sum_{j\in T}p_j,\qquad w=\frac{\bar p}{\rho},
$$

and $\mathrm{KE}_L=\tfrac12S_0\,u^\dagger hu$, $\mathrm{PE}_L=\rho-\mathrm{KE}_L$, $\mathrm{KE}_H=S_0\sum_jp_j(u)$, $\mathrm{PE}_H=mS+\tfrac\lambda2S^2$. The term $-\tfrac\lambda2S^2$ in $\rho$ corrects the double counting of the interaction in $u^\dagger hu$, which contains $M_{\mathrm{eff}}s$.

**The exact solution.** For constant $M_{\mathrm{eff}}$ the matrix $h$ is constant and $h^2=E^2$ with $E=\sqrt{M_{\mathrm{eff}}^2+K^2}$. The solution of $i\dot u=hu$ is $u(t)=e^{-iht}u_0$. In the power series of the exponential, even powers of $h$ are powers of $E^2$ and odd powers are powers of $E^2$ times $h$, so

$$
u(t)=\Bigl(\cos(Et)-i\,\sin(Et)\,\frac hE\Bigr)u_0 .
$$

Since this matrix is unitary ($h$ is Hermitian) and commutes with $h$, $\varepsilon=u^\dagger hu$ is constant for every initial spinor. An eigenvector of $h$ only changes its phase, so all its bilinears are constant. A mixture $u=\alpha u_++\beta u_-$ of a $+E$ and a $-E$ eigenvector has bilinears with cross terms $\alpha^\ast\beta\,e^{2iEt}u_+^\dagger Mu_-$ and their conjugates, which oscillate at the frequency $2E$. This interference of the positive- and negative-energy parts is called Zitterbewegung (German for trembling motion).

**The source the geometry would need.** Chapter 9 (and the Stage-2 document) gives the Einstein tensor of the primordial field (primes are $d/dt$):

$$
G^4{}_4=3H^2(7+a_4'^2),\quad G^0{}_0=-3H^2(a_4'^2-5),\quad G^i{}_i=H^2(15-3a_4'^2+a_4''),\quad G^j{}_j=H^2(15-3a_4'^2-a_4''),
$$

for $i=1,2,3$ and $j=5,6,7$. With $G^\mu{}_\nu=\kappa T^\mu{}_\nu$ and $T^4{}_4=-\rho$, the required energy density and pressures are

$$
\rho_{\mathrm{req}}=-\frac{3H^2(7+a_4'^2)}{\kappa},\qquad p_{\mathrm{req},0}=-\frac{3H^2(a_4'^2-5)}{\kappa},\qquad p_{\mathrm{req},i}=\frac{G^i{}_i}{\kappa},\qquad p_{\mathrm{req},j}=\frac{G^j{}_j}{\kappa}.
$$

$\rho_{\mathrm{req}}$ is negative for every $a_4$. Average the seven pressures (with $\kappa=H=1$): $\bar p_{\mathrm{req}}=\tfrac17[-3(a_4'^2-5)+3(15-3a_4'^2+a_4'')+3(15-3a_4'^2-a_4'')]=\tfrac17(105-21a_4'^2)=15-3a_4'^2$; the $a_4''$ terms cancel. Hence

$$
w_{\mathrm{req}}=\frac{\bar p_{\mathrm{req}}}{\rho_{\mathrm{req}}}=-\frac{5-a_4'^2}{7+a_4'^2}.
$$

Worked values: $a_4'=0$ gives $\rho_{\mathrm{req}}=-21$ and $w_{\mathrm{req}}=-5/7=-0.714$; $a_4'=1$ gives $-24$ and $-4/8=-0.5$; $a_4'=2$ gives $-33$ and $-1/11=-0.091$.

**Initial data.** $H=m=\kappa=1$, $S_0=1$, $t\in[0,10]$ with 201 samples, hidden momenta $K\in\{0,0.5,2\}$ and both profiles $A=1,2$. For each $(A,K)$ four initial spinors: a joint eigenvector of $h$ and $B$ with energy $+E$ and Krein sign $+1$ (run name `pos_Bp`), energy $+E$ and Krein sign $-1$ (`pos_Bm`), energy $-E$ and Krein sign $+1$ (`neg_Bp`), and a normalised generic mixture of both energy signs (`mix`). Only the positive-energy eigenstates are one-particle states; the `neg_Bp` runs are numerical controls (in the quantum theory those levels are filled by the sea). One more run per profile has $\lambda=0.5$ and $K=0.5$ and starts on the positive-energy eigenvector of the self-consistent mass $M_\ast=1+\lambda S_0M_\ast/\sqrt{M_\ast^2+K^2}$, solved by Newton's method: $M_\ast=1.47348266406420$. In total 26 runs. At rtol $10^{-10}$ the drifts of the conserved quantities exceeded the a priori limit $10^{-8}$, so the tolerance was tightened to $10^{-12}$ rather than the limit relaxed (Stage-3 document §6.4).

![EXP-1 observables for profile $A=1$ (profile $A=2$ is bit-identical): (a) energy density, (b) mean transverse pressure, (c) Lagrangian split, (d) $w=\bar p/\rho$, (e) and (f) drifts of $\rho$ and of the Hilbert and Krein norms over all 26 runs.](artifacts/dirac16complex/numerics/figures/exp1_frozen_observables.png)

**Results** (exp1/summary.json and exp1/python-check-report.json).

- **Frozen observables.** $\rho$ is constant for every initial spinor (largest drift $4.19\times10^{-9}$), because $h$ is constant and Hermitian. The pressures and $S$ are constant for the eigenstates (largest drift $2.64\times10^{-9}$). For the mixtures with $K\ne0$ the hidden-space pressure $p_0$ and $S$ oscillate at $2E$: the range of $p_0$ is 0.803 for $K=2$ and 0.341 for $K=0.5$, and the checker's exact solution reproduces the range to $3.7\times10^{-10}$.
- **Eigenmode laws.** $K=0$: $\rho=1$, $p=0$, $w=0$, $\mathrm{KE}_L=\mathrm{PE}_L=0.5$ (dust). $K=0.5$: $\rho=E=1.1180$, $p_0=K^2/E=0.2236$, $w=K^2/(7E^2)=0.02857$. $K=2$: $\rho=2.2361$, $p_0=1.7889$, $w=4/35=0.11429$. Every free eigenmode has $\mathrm{KE}_L=\mathrm{PE}_L$ whatever $K$ is; the actual pressure is the hidden-space momentum flux.
- **Repulsive interaction.** The $\lambda=0.5$ run (pointwise mean field) has $\rho=1.3318$, $\bar p=0.2471$, $w=0.1856$, $\mathrm{KE}_L=0.7780$ and $\mathrm{PE}_L=0.5538$; the six pressures $p_1,\dots,p_7$ equal $\tfrac\lambda2S^2=0.2242$, and $M_{\mathrm{eff}}$ stays at $M_\ast$ to $1.3\times10^{-9}$.
- **Profile independence.** $a_4$ enters $h$ only through $k_j/h_j$ with $k_j=0$, so the $A=1$ and $A=2$ spinors are bit-identical (difference 0.0).
- **Mixed states are coherent pair states.** A mixture $u=\alpha u_++\beta u_-$ is not a state of one quantum. It does describe a state of the positive-norm Fock space: the Dirac sea with its level $u_-$ replaced by $u$, a superposition of the vacuum and one particle-antiparticle pair. Its normal-ordered expectation values are the output columns minus a constant, so the $2E$ oscillation of $p_0$ and $S$ is physical in that state: an interference of its vacuum and pair parts. The mixtures take negative values of $p_0$, $\bar p$ and $S$ at some times, and carry tensor bilinears that the eigenstates do not have.
- **Negative-energy controls.** The `neg_Bp` runs have $\rho=-E$ in this reading; physically an antiparticle is a hole in such a level and carries $+E$.
- **The required source has negative energy.** $\rho_{\mathrm{req}}$ lies in $[-24.0,-21.0]$ for $A=1$ and in $[-33.0,-21.0]$ for $A=2$; its largest value is $-21.000000000113$. $w_{\mathrm{req}}$ lies in $[-0.714,-0.500]$ and $[-0.714,-0.091]$. It is negative because $\rho_{\mathrm{req}}<0$ while the mean required pressure is positive, not because the pressure is negative. $a_4$ reaches 5.0 ($A=1$) and 10.0 ($A=2$), so 3-space grows by $e^5$ and $e^{10}$, while $V/V_0-1$ stays at $6.7\times10^{-16}$.

![EXP-1 background and Einstein requirement: (a) the window $a_4'(t)$, (b) the 3-space factor $e^{a_4}$, the extra-time factor $e^{-a_4}$ and the constant 7-volume, (c) $\rho_{\mathrm{req}}$ for both profiles beside the energy density of the free $K=0$ field, (d) $w_{\mathrm{req}}$.](artifacts/dirac16complex/numerics/figures/exp1_einstein_requirement.png)

**Can dirac16complex supply that source?** Not with the positive-energy states integrated here: they have $\rho>0$, while $\rho_{\mathrm{req}}\le-21$. Stage 2 settles the question for states that depend on $x_0$ and $x_4$ only wherever $a_4''\ne0$ (Stage-2 document §15.5, Chapter 9). No such state can source the field on a time interval where $a_4''\ne0$, because such states have $T^i{}_i=T^j{}_j$ while $G^i{}_i-G^j{}_j=2H^2a_4''$. For a linear $a_4$, with a constant slope $a_4'$ and so $a_4''=0$ (Chapter 9 writes $a_4=ct$, with the slope $c=a_4'$), Stage 2 analyses only two families. No plane wave with a real hidden momentum $K$ is a source. The state that does not depend on $x_0$ (the wave above with $K=-3iH$, whose prefactor is 1) is an exact source when three conditions on its bilinears and parameters hold, and then its energy density is $\rho=-3H^2(7+a_4'^2)/\kappa<0$. Other states of $x_0$ and $x_4$, for example the plane waves with $\mathrm{Im}\,K=-3H$ and $\mathrm{Re}\,K\ne0$, are not analysed (Section 9.12; Stage-2 document §20, item 2). The exact sources need $mS<0$, which is possible because the indefinite $C$ lets $S$ take either sign. The window of EXP-1 has $a_4''\ne0$ except at one instant: writing $\tau_1=\tanh((t-t_1)/\Delta)$, $\tau_2=\tanh((t-t_2)/\Delta)$ and using $d\tanh(x)/dx=(1-\tanh x)(1+\tanh x)$,

$$
a_4''=\frac{A}{4\Delta}(1+\tau_1)(1-\tau_2)\bigl[(1-\tau_1)-(1+\tau_2)\bigr]=-\frac{A}{4\Delta}(1+\tau_1)(1-\tau_2)(\tau_1+\tau_2),
$$

which vanishes only where $\tau_1=-\tau_2$, that is at $t=(t_1+t_2)/2=4.5$ (derived here; the brackets $1+\tau_1$ and $1-\tau_2$ are always positive). Every time interval contains an open piece with $a_4''\ne0$, so no state of this kind can source the EXP-1 background on any time interval.

**Verification.** The program passes 10 of 10 self-checks and the checker 25 of 25; among them:

```
exp1/summary.json (Rust)     exact_solution_all_runs, rho_frozen_all_runs,
                             a4_profile_independence, einstein_source_negative_energy,
                             seven_volume_constant
exp1/python-check-report.json
                             exactSolution, eigenmodeLaws, einsteinSourceNegative,
                             mixedStateOscillationMatchesExact, repeatByteIdentity,
                             refinedConvergence
```

The largest distance from the exact propagator is $6.25\times10^{-9}$ (limit $10^{-7}$); a five-point finite-difference residual of $i\dot u=hu$ is at most 0.63 of its truncation bound. The Mathematica notebook re-integrates all 26 runs with NDSolve (largest state deviation from the Rust result $2.92\times10^{-9}$).

![Mathematica cross-check of the mixed state with $K=2$: $\rho$ frozen and $p_0$ oscillating at $2E$; dots are the Rust samples, lines the independent NDSolve solution.](artifacts/dirac16complex/numerics/figures/mathematica/exp1_mixed_state_rho_p0.png)

**What EXP-1 shows.** In the primordial field the 7-volume is constant, so the dilution law $SV=$ constant freezes the field: energy density and pressure do not change at all while 3-space inflates by up to $e^{10}$. The frozen equation of state of the positive-energy eigenstates is dust ($K=0$) or slightly stiff ($K\ne0$, or $\lambda>0$); none of them has negative pressure. **What it does not show.** It does not produce the primordial field: that geometry needs a source of negative energy density, which the positive-energy states cannot be. The frozen density matters for dark energy only as a dilution effect seen from 3-space (Section 11.14).

### 11.7 EXP-2: an eight-dimensional universe that feels the condensate

**Purpose.** EXP-2 lets the geometry respond to the matter. It couples the condensate to 8-dimensional Einstein gravity, with the hidden space, 3-space and the extra times free to evolve, and asks how $\rho$, $p$ and the anisotropy evolve, whether the extra times keep deflating, and what a 3-space observer would infer.

**The metric and Einstein's equations.** With $\kappa=\kappa_8=1$ and $m=1$,

$$
ds^2=-dt^2+b^2dx_0^2+a^2\bigl(dx_1^2+dx_2^2+dx_3^2\bigr)-c^2\bigl(dx_5^2+dx_6^2+dx_7^2\bigr),\qquad V=b\,a^3c^3 .
$$

**The curvature of a diagonal metric that depends on $t$ only.** We compute it for the general metric of Section 11.3 with the diagonal formulas of Section 4.5, with $h_4=1$, $\eta_{44}=-1$ and $g_{ii}=\eta_{ii}h_i^2$ for $i\in T$ (no sum). Every $h_i$ depends on $t=x_4$ only, so case (a) gives nothing ($\partial_4\ln h_4=0$ and $\partial_i\ln h_i=0$), case (b) gives only $\partial_4\ln h_i$, case (c) gives only symbols with the upper index 4, and case (d) gives zero. The only nonzero Christoffel symbols are therefore

$$
\Gamma^4{}_{ii}=-\eta_{44}\,\eta_{ii}\,\frac{h_i}{h_4^2}\,\partial_4h_i=\eta_{ii}\,h_i\dot h_i\quad\text{(case (c))},\qquad \Gamma^i{}_{4i}=\Gamma^i{}_{i4}=\partial_4\ln h_i=H_i\quad\text{(case (b))},
$$

for $i\in T$ (no sum). In particular $\Gamma^\lambda{}_{44}=0$ for every $\lambda$, and $\Gamma^\rho{}_{\rho4}=\sum_{i\in T}H_i=\Theta$. The Ricci tensor is $R_{\sigma\nu}=R^\rho{}_{\sigma\rho\nu}$ with the Riemann formula of Section 4.7:

$$
R_{\sigma\nu}=\partial_\rho\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\rho\sigma}+\Gamma^\rho{}_{\rho\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\rho\sigma},
$$

and nothing depends on the $x_i$, so every derivative along an $x_i$ vanishes. For $R_{44}$ the first and third terms contain $\Gamma^\lambda{}_{44}=0$, the second is $-\partial_4\Theta=-\sum_i\dot H_i$, and in the fourth, $-\sum_{\rho,\lambda}\Gamma^\rho{}_{4\lambda}\Gamma^\lambda{}_{\rho4}$, only $\rho=\lambda=i$ contributes, giving $-\sum_iH_i^2$. So, as in the primordial example of Section 4.7,

$$
R_{44}=-\partial_4\Theta-\sum_iH_i^2=-\sum_{i\in T}\bigl(\dot H_i+H_i^2\bigr).
$$

For $R_{ii}$ (no sum) the first term is $\partial_4\Gamma^4{}_{ii}$, the second is a derivative along $x_i$ and vanishes, the third is $\Gamma^\rho{}_{\rho4}\Gamma^4{}_{ii}=\Theta\,\Gamma^4{}_{ii}$, and in the fourth only $(\rho,\lambda)=(4,i)$ and $(\rho,\lambda)=(i,4)$ contribute, each with $\Gamma^4{}_{ii}H_i$. With $h_i\dot h_i=h_i^2H_i$ and $\tfrac{d}{dt}(h_i\dot h_i)=\dot h_i^2+h_i\ddot h_i=h_i^2(\dot H_i+2H_i^2)$ (because $\dot H_i=\ddot h_i/h_i-H_i^2$):

$$
R_{ii}=\partial_4\Gamma^4{}_{ii}+\Theta\,\Gamma^4{}_{ii}-2\,\Gamma^4{}_{ii}H_i=\eta_{ii}\Bigl(\tfrac{d}{dt}(h_i\dot h_i)+\Theta h_i\dot h_i-2h_i\dot h_iH_i\Bigr)=\eta_{ii}h_i^2\bigl(\dot H_i+H_i\Theta\bigr).
$$

For $\mu\ne\nu$, $R_{\mu\nu}=0$, because every term then contains a derivative along some $x_i$ or a vanishing Christoffel symbol. Raising an index with $g^{44}=-1$ and $g^{ii}=\eta_{ii}/h_i^2$ (the $\eta_{ii}$ cancel, since $\eta_{ii}^2=1$),

$$
R^4{}_4=\sum_i\bigl(\dot H_i+H_i^2\bigr),\qquad R^i{}_i=\dot H_i+H_i\Theta\quad(\text{no sum}),\qquad R=R^4{}_4+\sum_iR^i{}_i=2\sum_i\dot H_i+\sum_iH_i^2+\Theta^2 .
$$

Since $\Theta^2=\sum_iH_i^2+2\sum_{i<j}H_iH_j$,

$$
G^4{}_4=R^4{}_4-\tfrac12R=\tfrac12\Bigl(\sum_iH_i^2-\Theta^2\Bigr)=-\sum_{i<j}H_iH_j ,
$$

the sum over the 21 unordered pairs of the seven directions. The EXP-2 checker recomputes the Einstein tensor from the metric independently (check `einsteinTensorFromMetric`), and the Mathematica notebook derives it symbolically.

Einstein's equation $G_{\mu\nu}=\kappa T_{\mu\nu}$ in $D$ dimensions can be rewritten with its trace: $g^{\mu\nu}$ applied to $R_{\mu\nu}-\tfrac12g_{\mu\nu}R=\kappa T_{\mu\nu}$ gives $R(1-D/2)=\kappa T$, so $R_{\mu\nu}=\kappa\bigl(T_{\mu\nu}-g_{\mu\nu}T/(D-2)\bigr)$. With the isotropic pressure of the condensate, $T=T^\mu{}_\mu=-\rho+(D-1)p$ and $T^i{}_i-T/(D-2)=(\rho-p)/(D-2)$. Hence, for $D=8$:

$$
\sum_{i<j}H_iH_j=\kappa\rho,\qquad \dot H_i=-H_i\Theta+\frac{\kappa}{6}(\rho-p),\qquad \dot h_i=H_ih_i .
$$

The first is a **constraint** (it contains no second derivatives and must hold at every time); the others are **evolution equations**. Counting the pairs by groups (hidden-3-space: 3 pairs; hidden-extra-time: 3; within 3-space: 3; within the extra times: 3; 3-space-extra-time: 9) gives

$$
\sum_{i<j}H_iH_j=3H_bH_a+3H_bH_c+3H_a^2+3H_c^2+9H_aH_c .
$$

**The Friedmann equations as a check.** The same equations with $D=4$ and three equal directions give $3H^2=\kappa\rho$ and $\dot H=-3H^2+\tfrac\kappa2(\rho-p)$. Then $\ddot a/a=\dot H+H^2=-\tfrac23\kappa\rho+\tfrac\kappa2(\rho-p)=-\tfrac\kappa6(\rho+3p)$: exactly the Friedmann equations of Section 11.2.

**Matter.** The condensate is the $K=0$ mode: $h=-iM_{\mathrm{eff}}\gamma^4$, $S=S_0(V_0/V)s(u)$ with $V_0=1$, $\rho=mS+\tfrac\lambda2S^2$ and $p=\tfrac\lambda2S^2$. Note that $\rho-p=mS$ does not depend on $\lambda$. CVODE integrates 38 real numbers: $\ln b$, $\ln a$, $\ln c$, $H_b$, $H_a$, $H_c$ and the 32 components of $u$.

**Is a diagonal metric consistent?** Only the diagonal Einstein equations are integrated, so the off-diagonal stresses must vanish. For a homogeneous state Stage 1 gives $T_{ij}=\tfrac14(H_i-H_j)\,\bar\Psi\gamma_i\gamma_j\gamma^{x_4}\Psi$ for $i\ne j$. They vanish if the tensor bilinears $u^\dagger BC\gamma^i\gamma^j\gamma^4u$ vanish in the 15 planes $(i,j)$ between directions of different groups. Since $u(t)$ is $u(0)$ times a phase, zero stays zero. This is a real condition on $u(0)$: a generic vector of the same joint eigenspace ($h=+M_{\mathrm{eff}}$, $B=+1$) has nonzero bilinears in the planes $(0,1)$, $(0,2)$ and $(0,3)$. The chosen $u(0)=u_0$ of Section 11.4 has zero bilinears in all 21 planes (check `offDiagonalStressVanishes`, value 0.0 in every row).

**The exact solution** (derived in the study and re-derived by the checker, check `closedFormVerified`). Multiply the evolution equation by $V$ and use $\dot V=\Theta V$:

$$
\frac{d}{dt}(H_iV)=\dot H_iV+H_i\Theta V=\frac{\kappa}{6}(\rho-p)V=\frac{\kappa}{6}\,mSV=\frac{\kappa mS_0}{6}=:\beta_2 ,
$$

a constant, because $SV=S_0$ ($s(u)=1$ for the rest eigenvector). So $H_iV=H_{i0}+\beta_2 t$. Summing over the seven directions, $\Theta V=\dot V$ obeys $\ddot V=7\beta_2$, and with $V(0)=1$, $\dot V(0)=\Theta_0$:

$$
V(t)=1+\Theta_0t+\alpha_2 t^2,\qquad \alpha_2=\frac{7\beta_2}{2},\qquad H_i(t)=\frac{H_{i0}+\beta_2 t}{V(t)},\qquad u(t)=e^{-i\int_0^tM_{\mathrm{eff}}\,dt'}u_0 .
$$

The program uses this closed form only for its self-checks and to place the output times; CVODE integrates the full system of 38 equations.

**The singularity and Kasner exponents.** Backward in time $V$ reaches 0 at the root of $\alpha_2 t^2+\Theta_0t+1=0$ nearest to 0, $t_s=-2/(\Theta_0+\sqrt{\mathcal D})$ with the discriminant $\mathcal D:=\Theta_0^2-4\alpha_2$ (the root formula with the square root moved into the denominator; we write $\mathcal D$ because $D$ is the number of dimensions). Near it $V\approx\dot V(t_s)(t-t_s)$ with $\dot V(t_s)=\Theta_0+2\alpha_2 t_s=\sqrt{\mathcal D}$, so $H_i\approx p^{\mathrm K}_i/(t-t_s)$ and $h_i\propto(t-t_s)^{p^{\mathrm K}_i}$, with the **Kasner exponents** $p^{\mathrm K}_i$ (the superscript K distinguishes them from the pressures $p_{(i)}$ and $p_j$ of this chapter)

$$
p^{\mathrm K}_i=\frac{H_{i0}+\beta_2 t_s}{\sqrt{\mathcal D}} .
$$

Their sum is $\sum_ip^{\mathrm K}_i=(\Theta_0+7\beta_2 t_s)/\sqrt{\mathcal D}=(\Theta_0+2\alpha_2 t_s)/\sqrt{\mathcal D}=1$. For the sum of squares use $\sum_i(p^{\mathrm K}_i)^2=\bigl(\sum_ip^{\mathrm K}_i\bigr)^2-2\sum_{i<j}p^{\mathrm K}_ip^{\mathrm K}_j$. By the formula for the exponents, $\sum_{i<j}p^{\mathrm K}_ip^{\mathrm K}_j$ is $1/\mathcal D$ times $\sum_{i<j}(H_{i0}+\beta_2 t_s)(H_{j0}+\beta_2 t_s)$, and expanding (with the constraint above at $t=0$, $\sum_{i<j}H_{i0}H_{j0}=\kappa\rho_0$), $\sum_{i<j}(H_{i0}+\beta_2 t_s)(H_{j0}+\beta_2 t_s)=\kappa\rho_0+6\beta_2\Theta_0t_s+21\beta_2^2t_s^2$ (each direction lies in 6 of the 21 pairs). Multiplying $\alpha_2 t_s^2+\Theta_0t_s+1=0$ by $6\beta_2$ and using $6\alpha_2\beta_2=21\beta_2^2$ shows $6\beta_2\Theta_0t_s+21\beta_2^2t_s^2=-6\beta_2=-\kappa mS_0$. Define the dimensionless coupling $x_0:=\lambda S_0/(2m)$, the interaction energy relative to the rest energy (the same letter as the hidden coordinate; the reports call it x0, and as a coupling it always appears as a number). Then $\rho_0=mS_0+\tfrac\lambda2S_0^2=mS_0(1+x_0)$, the expanded sum is $\kappa mS_0(1+x_0)-\kappa mS_0=\kappa mS_0x_0$, and

$$
\sum_i(p^{\mathrm K}_i)^2=1-\frac{2\kappa m\,x_0S_0}{\mathcal D} .
$$

For the free condensate ($x_0=0$) this is the vacuum Kasner relation $\sum_ip^{\mathrm K}_i=\sum_i(p^{\mathrm K}_i)^2=1$: near the singularity the dust term is negligible. The interaction term $\tfrac\lambda2S^2$ is a stiff ($w=1$) component there and changes the exponents. **Late times:** $V\approx\alpha_2 t^2$ and $H_i\approx\beta_2 t/(\alpha_2 t^2)=(2/7)/t$ in every direction: isotropic 8-dimensional dust.

**What a 3-space observer infers.** An observer who knows only 3-space and assumes $\rho\propto a^{-3(1+w_{\mathrm{eff}})}$ infers $d\ln\rho/d\ln a=-3(1+w_{\mathrm{eff}})$. The true dilution follows from energy conservation, $\dot\rho=-\Theta(\rho+p)$, so $d\ln\rho/d\ln a=-\Theta(1+w)/H_a$, and

$$
w_{\mathrm{eff}}=-1+\frac{\Theta}{3H_a}(1+w) .
$$

This is a dilution measure, not the deceleration of 3-space. If $\Theta=3H_a$ (static extra dimensions) then $w_{\mathrm{eff}}=w$; at late times in EXP-2, $\Theta\to7H_a$ and dust ($w=0$) appears as $w_{\mathrm{eff}}\to-1+7/3=4/3$.

**An energy bound** (derived here from the constraint, and monitored by the program as the quantity bound). Expanding the square, $\Theta^2=H_b^2+9H_a^2+9H_c^2+6H_bH_a+6H_bH_c+18H_aH_c$, while twice the constraint is $2\kappa\rho=6H_bH_a+6H_bH_c+6H_a^2+6H_c^2+18H_aH_c$. Subtracting,

$$
\Theta^2-3H_a^2-2\kappa\rho=H_b^2+3H_c^2\ \ge\ 0 .
$$

So wherever $\rho\ge0$ (and $H_a,\Theta>0$), $\Theta\ge\sqrt3\,H_a$, and for $1+w\ge0$ this gives $w_{\mathrm{eff}}\ge-1+(1+w)/\sqrt3$; for dust $-1+1/\sqrt3=-0.42265$. A 3-space observer can see dust dilute like a cosmological constant ($w_{\mathrm{eff}}$ near $-1$) only if the 8-dimensional energy density is negative.

**Initial data.** $\ln b=\ln a=\ln c=0$, $H_b=0$, $H_a=1$ and $H_c=-0.2$: 3-space expands and the extra times start out deflating. $u(0)=u_0$, a positive-energy quantum at rest with $s=1$. Then $\Theta_0=0+3-0.6=2.4$, and the left side of the constraint at $t=0$ is $\sum_{i<j}H_{i0}H_{j0}=3(1)+3(0.04)+9(1)(-0.2)=1.32$. The constraint must hold initially: $\kappa\rho_0=mS_0(1+x_0)=1.32$, so

$$
S_0=\frac{1.32}{1+x_0},\qquad \lambda=\frac{2m\,x_0}{S_0},\qquad M_{\mathrm{eff}}(0)=m+\lambda S_0=m(1+2x_0),\qquad \beta_2=\frac{S_0}{6},\qquad \alpha_2=\frac{7S_0}{12}.
$$

Three runs, from exp2/summary.json:

| Run | $S_0$ | $\lambda$ | $M_{\mathrm{eff}}(0)$ | $\beta_2$ | $\alpha_2$ | $t_s$ |
| --- | --- | --- | --- | --- | --- | --- |
| $x_0=0$ (dust) | 1.32 | 0 | 1 | 0.22 | 0.77 | $-0.4954$ |
| $x_0=-0.4$ (attractive) | 2.2 | $-0.3636$ | 0.2 | 0.3667 | 1.2833 | $-0.6266$ |
| $x_0=+0.5$ (repulsive) | 0.88 | 1.1364 | 2 | 0.1467 | 0.5133 | $-0.4624$ |

The Kasner exponents of the formula above, for the same three runs (exp2/summary.json):

| Run | $p^{\mathrm K}_b$ | $p^{\mathrm K}_a$ | $p^{\mathrm K}_c$ | $\sum_i(p^{\mathrm K}_i)^2$ |
| --- | --- | --- | --- | --- |
| $x_0=0$ | $-0.066576$ | 0.544271 | $-0.188746$ | 1 |
| $x_0=-0.4$ | $-0.290250$ | 0.972978 | $-0.542895$ | 3.80851 |
| $x_0=+0.5$ | $-0.035225$ | 0.484182 | $-0.139107$ | 0.76259 |

The output times are uniform in $\ln V$ with step 0.05 on $[-7,18.5]$ (511 rows). Backward the run stops at $V/V_0=e^{-7}$, about $10^{-3}$ in $t$ above $t_s$; forward it ends at $V/V_0=e^{18.5}$, at $t=11855.5$, 9183.5 and 14519.6. The step cap 0.02 is needed: without it Adams takes steps of about 0.045 and its small amplitude error per step on the oscillating spinor drifts $s(u)$ by $1.7\times10^{-7}$ over $t\sim10^4$ (Stage-3 document §7.4).

**Where the attractive run leaves the mean field.** With $V_0=1$ and $s=1$, $S=S_0/V$, so $M_{\mathrm{eff}}=m(1+2x_0/V)$ and $\rho=mS(1+x_0/V)$. For $x_0=-0.4$: $M_{\mathrm{eff}}<0$ for $V<0.8$, and $\rho<0$ for $V<0.4$.

![EXP-2 Hubble rates of the hidden space, 3-space and the extra times against $t-t_s$ (top), and $H_i(t-t_s)$ with the Kasner exponents dotted and the 8-dimensional dust value $2/7$ dashed (bottom), for the three runs.](artifacts/dirac16complex/numerics/figures/exp2_hubble.png)

**Results** (exp2/summary.json).

- **Isotropisation.** From $H_iV=H_{i0}+\beta_2 t$, the anisotropy $(H_i-H_j)V=H_{i0}-H_{j0}$ is constant (measured drift $6.2\times10^{-10}$), so $H_i-H_j$ decays as $1/V$. At the forward end the relative anisotropy $7\max|H_i-H_j|/\Theta$ is $4.6\times10^{-4}$, $3.6\times10^{-4}$ and $5.6\times10^{-4}$; $H_it$ approaches $2/7=0.2857$, and $w_{\mathrm{eff}}=1.33275$, 1.33288 and 1.33261 approaches $4/3$.
- **The extra times turn from deflation to expansion** where $H_c=0$, that is at $t=0.2/\beta_2=0.9091$, 0.5455 and 1.3636 (measured on the output grid: 0.9095, 0.5457, 1.3639). Nothing in this dynamics keeps them deflating.
- **Kasner exponents.** Extrapolating the CVODE solution to $V=0$ reproduces the closed-form exponents of the second table above to $2.9\times10^{-7}$.
- **Equation of state.** The dust run keeps $w=0$. The repulsive run is stiff near the singularity ($w\to1$) and dust at late times. The attractive run is dust at late times; backward it becomes phantom ($w<-1$ with $\rho>0$) for $0.4<V/V_0<0.8$ (14 output rows, measured volumes 0.407 to 0.779) and has negative energy density for $V/V_0<0.4$ (122 rows), down to $\rho=-1.06\times10^{6}$ at $V=e^{-7}$. Among the rows with $\rho>0$, the phantom rows are exactly the rows with $\mathrm{KE}_L<0$ (Rust check `phantom_iff_negative_kinetic_energy`); all 136 rows with $M_{\mathrm{eff}}<0$, including the 122 with $\rho<0$ (where $w>1$, because $\rho-p=mS>0$ gives $p<\rho<0$), have $\mathrm{KE}_L=\tfrac12SM_{\mathrm{eff}}<0$. **These backward rows are outside the domain of the mean field**: in all $14+122$ rows with $M_{\mathrm{eff}}<0$ the output has $s(u)=1$ and mode energy $u^\dagger hu=M_{\mathrm{eff}}<0$, so the occupied mode is a negative-energy level (Section 11.4, limit 1).
- **The energy bound.** For dust the smallest $w_{\mathrm{eff}}$ is $-0.38732>-0.42265$, and the smallest $\Theta/(3H_a)$ over rows with $\rho>0$ is 0.61268. In the attractive run the 14 phantom rows have $w_{\mathrm{eff}}<-1+(1+w)/\sqrt3$ (the bound assumes $1+w\ge0$), and $\Theta<\sqrt3H_a$ occurs where $\rho<0$: over all rows $\Theta/(3H_a)$ falls to 0.344, while $\Theta^2-3H_a^2-2\kappa\rho$ itself stays non-negative. Both happen in the artefact region.

![EXP-2 (a) the 7-volume against $t-t_s$ with the exact quadratic, (b) energy density and pressure against $V/V_0$, (c) conservation of $SV$.](artifacts/dirac16complex/numerics/figures/exp2_volume_density.png)

![EXP-2 (a) $w=p/\rho$ and (b) the dilution-inferred $w_{\mathrm{eff}}$ against $\ln V$, with the lines $4/3$, $-1+1/\sqrt3$ and $-1$, and (c) the relative constraint residual with the limit $10^{-9}$.](artifacts/dirac16complex/numerics/figures/exp2_eos_constraint.png)

**Verification.** 15 of 15 self-checks and 35 of 35 checker checks; among them:

```
exp2/summary.json (Rust)     constraint_preserved, S_times_V_constant, exact_solution,
                             backward_kasner_exponents, extra_times_turn_to_expansion,
                             phantom_iff_negative_kinetic_energy
exp2/python-check-report.json
                             constraintPreserved, einsteinTensorFromMetric,
                             diracEquationFd, kasnerExponents, phantomStructure,
                             boundNonnegative
```

The relative constraint residual is at most $1.26\times10^{-10}$ (limit $10^{-9}$) and $|SV/(S_0V_0)-1|$ at most $4.03\times10^{-10}$. One subtlety teaches something about numerics: the spinor's phase error of $2.24\times10^{-7}$ at $t\sim10^4$ does not shrink in the refined run ($2.71\times10^{-7}$), while its shape error shrinks from $2.0\times10^{-10}$ to $5.2\times10^{-11}$. The checker identified the cause: the rounding of CVODE's internal time $t_{n+1}=t_n+\Delta t_n$ (with the step size $\Delta t_n$; Section 10.10 explains the effect), accumulated over the many capped steps (1779784 in the three runs), not a truncation error; it stays below the predicted rounding bound $1.32\times10^{-6}$ (checks `spinorPhaseWithinTimeRounding` and `phaseDriftIsTimeRounding`). The Mathematica notebook agrees with the Rust solution to $3.16\times10^{-8}$ in $\ln h_i$.

**What EXP-2 shows.** In a self-consistent 8-dimensional cosmology the condensate's energy density falls as $1/V$ and its pressure as $1/V^2$, so every run ends as isotropic 8-dimensional dust whatever $\lambda$ is; $\lambda$ matters only near the singularity. Two consequences matter for the dark sector. First, the extra times do not stay deflating: 8-dimensional gravity with this matter drives all seven directions to the same expansion, and a 3-space observer then sees the dust dilute like $a^{-7}$ ($w_{\mathrm{eff}}\to4/3$), not like $a^{-3}$. Dust-like behaviour in 3-space therefore requires extra dimensions that are held static by something; EXP-3 and EXP-4 assume this, and nothing computed here provides it. Second, with $\rho\ge0$, $w\ge-1$ and $H_a,\Theta>0$, a 3-space observer can never infer $w_{\mathrm{eff}}<-1+(1+w)/\sqrt3$. **What it does not show.** The phantom stage and the negative energy density of the attractive run are artefacts of the one-mode approximation, not properties of the field.

### 11.8 EXP-3: the condensate as late-time dark energy

**Purpose and assumptions.** EXP-3 asks whether an attractive condensate can be the dark energy of the quoted supernova fits. It **assumes** that the hidden space and the extra times are static ($b$, $c$ constant), so that the 4-dimensional Friedmann equation of Section 11.2 applies with the condensate as one more component. This is an assumption of the experiment, not a consequence of the 8-dimensional equations; EXP-2 showed that those do not keep the extra dimensions static.

**The model.** With $b$, $c$ constant, $V\propto a^3$ and $S\propto a^{-3}$. Units: $H_0=1$ and the speed of light equal to 1 (here $c$ is the extra-time scale factor), densities in units of $3H_0^2/\kappa_4$. The independent variable is the number of e-folds $N=\ln a$ ($N=0$ today). Write $\sigma=S/S_0$ (equal to $a^{-3}$ in exact arithmetic) and $x_0=\lambda S_0/(2m)$ as in EXP-2. Then $\rho_\psi=mS+\tfrac\lambda2S^2=mS_0\,\sigma(1+x_0\sigma)$. Requiring $\rho_\psi(a=1)=\Omega_\psi$ fixes $mS_0=\Omega_\psi/(1+x_0)=:A_\psi$, and

$$
\rho_\psi=A_\psi\,\sigma(1+x_0\sigma),\qquad p_\psi=A_\psi\,x_0\sigma^2,\qquad w=\frac{x_0\sigma}{1+x_0\sigma}=\frac{x_0}{a^3+x_0},
$$

$$
\mathcal E^2=\frac{H^2}{H_0^2}=\Omega_ra^{-4}+\Omega_ma^{-3}+\rho_\psi,\qquad \mathrm{KE}_L=\frac{A_\psi}2\,\sigma(1+2x_0\sigma),\qquad \mathrm{PE}_L=\frac{A_\psi}2\,\sigma .
$$

(The splits follow from $\mathrm{KE}_L=\tfrac12SM_{\mathrm{eff}}$ with $M_{\mathrm{eff}}=m(1+2x_0\sigma)$ and $\mathrm{PE}_L=\tfrac12mS$.) **A check of energy conservation:** $d\rho_\psi/dN=A_\psi(-3\sigma-6x_0\sigma^2)=-3A_\psi\sigma(1+2x_0\sigma)=-3(\rho_\psi+p_\psi)$, the 4-dimensional continuity equation, as it must be for $\sigma=a^{-3}$.

**What the computer integrates.** The condensate is not assumed; it is obtained from the evolving spinor, $\sigma=a^{-3}s(u)/s(u_0)$. Since $dN=H\,dt=H_0\mathcal E\,dt$, every time derivative becomes $d/dN=(1/(H_0\mathcal E))\,d/dt$. The state has 35 real components: the time $H_0t$, the comoving distance $D_C$ (in units of today's Hubble length $1/H_0$), the 32 components of $u$, and $\ln\sigma$:

$$
\begin{aligned}
&\frac{d(H_0t)}{dN}=\frac1{\mathcal E},\qquad \frac{dD_C}{dN}=-\frac{1}{a\mathcal E},\qquad \frac{du}{dN}=-i\,\frac{M_{\mathrm{eff}}}{H_0}\,\frac{(-i\gamma^4)\,u}{\mathcal E},\\
&\frac{d\ln\sigma}{dN}=-3+\frac{2\,\mathrm{Re}\bigl(u^\dagger(-i\gamma^4)\,du/dN\bigr)}{s(u)} .
\end{aligned}
$$

The distance equation follows from $dD_C=dz/\mathcal E$ and $z=e^{-N}-1$, so $dz=-e^{-N}dN=-dN/a$. The last equation is the derivative of $\ln\sigma=-3N+\ln s(u)-\ln s(u_0)$, with $ds/dN=2\,\mathrm{Re}(u^\dagger(-i\gamma^4)\,du/dN)$ because $-i\gamma^4$ is Hermitian. The spinor frequency is $M_{\mathrm{eff}}/H_0=\mu(1+2x_0\sigma)/(1+2x_0)$, where $\mu=M_{\mathrm{eff}}(a=1)/H_0\in\{3,7\}$ is a **reduced frequency**: real fermions have $m/H_0>10^{30}$, which no integrator could follow, and two small values show that $\rho$, $p$ and $w$ do not depend on the spinor's phase. The distance modulus is $\mathrm{DM}(z)=5\log_{10}((1+z)D_C)$ plus a constant.

**Closed-form diagnostics** (derived here from the formulas above; the program and the checker test the zero of $\rho_\psi$, the crossing of $w=-1$, the bounce, the zeros of $q_{\mathrm{dec}}$ and the tangent parameters against the CVODE solutions, checks `rhoZeroLocation`, `phantomCrossing`, `bounceAndStop`, `decelerationRoots` and `tangentCPL`). $\rho_\psi=0$ where $a^3=-x_0$, at $a=|x_0|^{1/3}$. $w=-1$ where $x_0/(a^3+x_0)=-1$, that is $a^3=-2x_0$, at $a=(2|x_0|)^{1/3}$; there $M_{\mathrm{eff}}=m(1+2x_0a^{-3})=0$. A **bounce** ($\mathcal E^2=0$, the expansion rate reaches zero): multiplying $\mathcal E^2=0$ by $a^6$ gives $(\Omega_m+A_\psi)a^3+\Omega_ra^2+A_\psi x_0=0$. The deceleration parameter follows from the Friedmann equations with radiation ($\rho+3p=2\rho_r$) and matter ($\rho+3p=\rho_m$):

$$
q_{\mathrm{dec}}=\frac{2\Omega_ra^{-4}+\Omega_ma^{-3}+\rho_\psi+3p_\psi}{2\mathcal E^2}.
$$

The adiabatic sound speed is $c_s^2=dp_\psi/d\rho_\psi=(dp_\psi/d\sigma)/(d\rho_\psi/d\sigma)=2x_0\sigma/(1+2x_0\sigma)$. The **tangent CPL parameters** at $a=1$: $w_0=w(1)=x_0/(1+x_0)$, and from $dw/da=-3a^2x_0/(a^3+x_0)^2$,

$$
w_a=-\frac{dw}{da}\Big|_{a=1}=\frac{3x_0}{(1+x_0)^2} .
$$

**Worked example: the model tuned to $w_0=-0.861$.** Inverting $w_0=x_0/(1+x_0)$ gives $x_0=w_0/(1-w_0)=-0.861/1.861=-0.462654$. Then $1+x_0=0.537346$, $w_a=3(-0.462654)/0.288741=-4.807$, $c_s^2=-0.925308/0.074692=-12.39$, $\rho_\psi=0$ at $a=0.462654^{1/3}=0.7734$ ($z=0.293$), $w=-1$ at $a=0.925308^{1/3}=0.9745$ ($z=0.026$), and $A_\psi=0.69491/0.537346=1.2932$. Neglecting the tiny $\Omega_r$, the bounce is at $a^3=A_\psi|x_0|/(\Omega_m+A_\psi)=0.59832/1.59823=0.3744$, $a=0.721$ ($z=0.388$). Today $p_\psi=A_\psi x_0=-0.59832$, so $q_{\mathrm{dec}}=(0.00018+0.305+0.69491-1.79495)/2=-0.397$. All of these agree with the committed values below.

**Initial data.** $\Omega_r=0.00009$, $\Omega_m=0.305$, $\Omega_\psi=0.69491$ (flat); these are inputs chosen by the numerical programme, since the e-mail gives no $\Omega_m$. Five couplings: $x_0=-0.462654$, $-0.433107$, $-0.3$, $-0.2$ and 0. The first reproduces $w_0=-0.861$, the second $w_0=-0.764$, and $x_0=0$ is dust. With $\mu\in\{3,7\}$ that makes 10 runs. The initial spinor is the positive-energy rest eigenvector with $B=+1$; as in EXP-2 its tensor bilinears vanish in the 12 planes between 3-space and the static directions (checker: 0.0 in every row). Each run goes from $N=0$ backward (towards $a=1/3.5$) and forward (to $a=2$). For every $x_0<0$ the backward run meets the bounce before $a=1/3.5$; smaller $a$ does not exist in these models, so the run stops just after it ($N\ge N_b+0.01$), and a check confirms that the stop sits exactly there. Only the dust model reaches $a=1/3.5$.

**Results** (exp3/summary.json and fits.json). Tangent parameters and today's sound speed:

| $x_0$ | $w_0$ | $w_a$ (tangent) | $c_s^2$ today |
| --- | --- | --- | --- |
| $-0.462654$ | $-0.861$ | $-4.807$ | $-12.39$ |
| $-0.433107$ | $-0.764$ | $-4.043$ | $-6.47$ |
| $-0.3$ | $-0.4286$ | $-1.837$ | $-1.50$ |
| $-0.2$ | $-0.25$ | $-0.9375$ | $-0.667$ |
| 0 | 0 | 0 | 0 |

The characteristic epochs, as redshift $z$ and scale factor $a$:

| $x_0$ | $\rho_\psi=0$ | $w=-1$ | bounce $\mathcal E^2=0$ |
| --- | --- | --- | --- |
| $-0.462654$ | $z=0.293$, $a=0.773$ | $z=0.0262$, $a=0.974$ | $z=0.388$, $a=0.721$ |
| $-0.433107$ | $z=0.322$, $a=0.757$ | $z=0.0490$, $a=0.953$ | $z=0.423$, $a=0.703$ |
| $-0.3$ | $z=0.494$, $a=0.669$ | $z=0.186$, $a=0.843$ | $z=0.633$, $a=0.612$ |
| $-0.2$ | $z=0.710$, $a=0.585$ | $z=0.357$, $a=0.737$ | $z=0.890$, $a=0.529$ |
| 0 | none | none | none |

Deceleration and the bare masses $m/H_0=\mu/(1+2x_0)$ of the two runs per coupling:

| $x_0$ | $q_{\mathrm{dec}}$ today | $q_{\mathrm{dec}}=0$ at | $m/H_0$ ($\mu=3$, 7) |
| --- | --- | --- | --- |
| $-0.462654$ | $-0.397$ | $z=-0.126$, $a=1.144$ | 40.2, 93.7 |
| $-0.433107$ | $-0.296$ | $z=-0.103$, $a=1.115$ | 22.4, 52.3 |
| $-0.3$ | 0.0533 | $z=0.0290$, $a=0.972$ | 7.5, 17.5 |
| $-0.2$ | 0.239 | $z=0.191$, $a=0.840$ | 5.0, 11.7 |
| 0 | 0.500 | none | 3, 7 |

![EXP-3 $w(a)=p_\psi/\rho_\psi$ of the condensate for the five couplings, with the quoted CPL line $w_0=-0.861$, $w_a=-0.60$ and the quoted constant $w=-0.764$. The shaded band ($\pm0.118$) is only an approximate one-sigma band inferred from the phrase “roughly two standard deviations from $-1$”; no band is drawn for the CPL line because the e-mail gives no error bars. The curves have a pole where $\rho_\psi=0$ and end at the bounce.](artifacts/dirac16complex/numerics/figures/exp3_w_of_a.png)

![EXP-3 (a) the condensate energy density $\rho_\psi(a)$, which changes sign at $a=\lvert x_0\rvert^{1/3}$ (circles), and (b) $\mathcal E^2=H^2/H_0^2$ (labelled $E^2$ in the figure), which reaches zero at the bounce for every attractive model.](artifacts/dirac16complex/numerics/figures/exp3_rho_psi.png)

![EXP-3 Lagrangian split: $\mathrm{KE}_L$ (solid) turns negative, and $w$ drops below $-1$, for $a<(2\lvert x_0\rvert)^{1/3}$, where the mean-field mode is a negative-energy level; $\mathrm{PE}_L$ (dashed) stays positive.](artifacts/dirac16complex/numerics/figures/exp3_ke_pe.png)

- **The changing equation of state.** For $x_0<0$, $w$ rises with time ($w_a<0$, the thawing sign of $w_a$, but not a thawing field in the usual sense, which starts at $w\approx-1$ and stays at or above it). In the equations $w$ comes up from $-\infty$ at the pole where $\rho_\psi=0$, crosses $-1$ where $M_{\mathrm{eff}}=0$, passes $w_0$ today, and tends to 0 in the future, because $p_\psi\propto a^{-6}$ dies away faster than $\rho_\psi$. Energy density and pressure change for one reason only: $\sigma=a^{-3}$.
- **Validity of the mean field.** Before the crossing ($a<(2|x_0|)^{1/3}$), $M_{\mathrm{eff}}<0$ while $s(u)=1$: the occupied mode is a negative-energy level (Section 11.4, limit 1). In the committed output of every attractive run all phantom rows and all rows with $\rho_\psi<0$ lie there, for example all rows with $a\le0.973$ for $x_0=-0.462654$. **The phantom epoch, the negative energy density and the bounce are therefore artefacts of the mean field**; the model tuned to $w_0=-0.861$ leaves the valid regime at $z=0.026$.
- **Acceleration.** The two models tuned to the quoted values accelerate today ($q_{\mathrm{dec}}=-0.397$ and $-0.296$) and all the way back to the bounce, and begin to decelerate again at $a=1.144$ and 1.115 when the condensate becomes dust-like. Neither has a matter-dominated era in these equations, and before $z=0.026$ and $z=0.049$ neither is inside the validity of the mean field. The weaker couplings decelerate today and accelerate only in the past, near the bounce.
- **Phase independence.** $\mu=3$ and $\mu=7$ give the same $\rho$, $p$ and $w$ to a few times $10^{-9}$ (check `rho_p_w_mu_independent`, checker `muIndependence`): only $s(u)=1$ matters, not the phase.
- **Sound speed.** $c_s^2$ is negative today for every $x_0<0$. In a fluid description a negative $c_s^2$ means that small density fluctuations grow instead of oscillating (a gradient instability); the fluctuations themselves were not computed.

### 11.9 EXP-3 continued: the quoted supernova fits and the deflating-extra-times variant

**The fits the programme asked for do not exist.** The numerical programme asked for (1) a least-squares CPL fit of $w(a)$ on $a\in[1/3.26,1]$, and (2) CPL and constant-$w$ fits of $\mathrm{DM}(z)$ on $z\in[0.01,2.26]$ with the offset profiled; the analysis `scripts/analyze_dirac16complex_exp3.py` implements its own Nelder-Mead minimiser in numpy (a method that finds the minimum of a function without derivatives, by moving and shrinking a small cluster of trial points). A fit of $w(a)$ over a range that contains the pole $a=|x_0|^{1/3}$ diverges; the pole lies inside $[1/3.26,1]$ exactly when $|x_0|>(1/3.26)^3=0.028863$. A fit of distances up to $z=2.26$ needs the model to exist up to that redshift; for $x_0<-0.041024$ the bounce comes first. So for all four attractive couplings the requested fits are undefined (fits.json records the reason for each). The supplementary fits (fits.json, `wFitRestricted` and `muFitRestricted`) use, for $w(a)$, the range $a\ge\max\bigl(1/3.26,(4|x_0|/3)^{1/3}\bigr)$, which stops where $w=-3$ (there $a^3+x_0=-x_0/3$) and so avoids the pole, and, for the distances, $z\in[0.01,\min(2.26,z_b)]$, which stops at the bounce redshift $z_b$ (for $x_0=0$ both are the requested ranges). They only show that the CPL form does not describe these models:

| $x_0$ | $w(a)$ fit, $(w_0,w_a)$ | DM fit, $(w_0,w_a)$ | DM fit, constant $w$ |
| --- | --- | --- | --- |
| $-0.462654$ | $(-0.605,-12.83)$ | $(2.106,-48.18)$ | $-2.764$ |
| $-0.433107$ | $(-0.485,-11.68)$ | $(1.846,-39.84)$ | $-2.478$ |
| $-0.3$ | $(-0.074,-7.583)$ | $(1.164,-18.11)$ | $-1.524$ |
| $-0.2$ | $(0.130,-5.267)$ | $(0.871,-9.943)$ | $-1.012$ |
| 0 | $(0,0)$ | $(0,0)$ | 0 |

A scan over 491 couplings $x_0\in[-0.49,0]$ in steps of 0.001 (`exp3/fits_scan.csv`) finds $x_0=-0.4626545$ for $w_0=-0.861$, with tangent $w_a=-4.807$, and $x_0=-0.4331066$ for $w_0=-0.764$.

**Reading the numbers.** Matching today's quoted $w_0=-0.861$ forces $w_a=-4.81$: the condensate evolves about eight times faster than the quoted fit ($w_a=-0.60$). Its effective mass vanishes and $w=-1$ at $z=0.026$ (the quoted CPL line crosses $-1$ at $a=0.768$), and beyond that redshift the mean field is outside its valid regime. The model therefore describes nothing beyond $z=0.026$ and cannot be confronted with supernovae up to $z=2.26$, let alone with the cosmic microwave background. The quoted constant $w=-0.764$ is reproduced only as today's value ($x_0=-0.433107$, with $w_a=-4.04$), and a constant-$w$ fit to that model's own distances gives $-2.48$.

**How $-0.764$ relates to the CPL numbers depends on $\Omega_m$.** This is a fact about the quoted numbers, not about dirac16complex. With $\Omega_m=0.305$ fixed and noise-free, equally weighted distances, the best constant $w$ for the distances of the quoted CPL model is $-1.028$ (offset profiled), $-0.975$ (offset fixed at 0) or $-0.979$ (a grid uniform in $\ln z$). With $\Omega_m$ free it is $-0.9115$ (best $\Omega_m=0.2777$), $-0.8788$ or $-0.8721$: about $-0.9$, not $-0.764$. Freeing $\Omega_m$ closes 44%, 46% and 50% of the gap. How the quoted constant-$w$ fit treated $\Omega_m$ is not stated in the e-mail, so the remaining difference cannot be judged without the supernova likelihood, its errors and its $\Omega_m$.

![EXP-3 distance modulus minus that of the quoted CPL model ($\Omega_m=0.305$) for the five couplings, a constant $w=-0.764$ and $\Lambda$CDM: (a) same $H_0$, curves ending at the bounce; (b) with each curve's mean offset removed. The dash-dot $w=-0.764$ curve uses the assumed $\Omega_m=0.305$ and differs from the CPL curve by up to 0.084 mag with the offset profiled; the dashed one uses $\Omega_m=0.240$, which best fits the CPL distances, and differs by at most 0.019 mag.](artifacts/dirac16complex/numerics/figures/exp3_distance_modulus.png)

**The deflating-extra-times variant.** The numerical programme also examined one way to give the condensate's $p/\rho$ the quoted tangent: let the extra times keep deflating. Take $c\propto a^{-\gamma}$ with $b$ static. Then $V\propto a^3c^3\propto a^{3(1-\gamma)}$ and $\sigma\propto a^{-n}$ with $n=3(1-\gamma)<3$: the condensate dilutes more slowly than $a^{-3}$. Now $w(a)=x_0/(a^n+x_0)$, so $w_0=x_0/(1+x_0)$ as before, and differentiating, $w_a=-dw/da|_1=n\,x_0/(1+x_0)^2$. Requiring $(w_0,w_a)=(-0.861,-0.60)$ gives $x_0=-0.4626545$, then $n=-0.60(1+x_0)^2/x_0=0.374457$, and $\gamma=1-n/3=0.875181$. By construction the tangent of $p/\rho$ equals the quoted values (analysis check `gammaVariantReproducesUniteTangent`). It fails in five ways (fits.json, `gammaVariant`; Stage-3 document §12.5):

1. **Like for like it does not match.** The quoted numbers are fit parameters over a data range, not a tangent. The least-squares CPL fit of the variant's own $p/\rho$ over $a\in[1/3.26,1]$ gives $(w_0,w_a)=(-0.640,-1.98)$ (rms residual 0.154), far from $(-0.861,-0.60)$.
2. **4-dimensional energy conservation fails.** $d\rho_\psi/dN=-nA_\psi\sigma(1+2x_0\sigma)$ while $\rho_\psi+p_\psi=A_\psi\sigma(1+2x_0\sigma)$, so $d\rho_\psi/dN+3(\rho_\psi+p_\psi)=(3-n)A_\psi\sigma(1+2x_0\sigma)\ne0$: energy flows to or from the extra dimensions. Today its value is 0.254 in units of $3H_0^2/\kappa_4$. Distances then measure $w_{\mathrm{eff}}=-1-\tfrac13\,d\ln\rho_\psi/d\ln a$, whose tangent is $(-0.9827,-0.0749)$, not the quoted pair.
3. **Newton's constant varies.** In a higher-dimensional theory the 4-dimensional $G_N$ is the higher-dimensional one divided by the volume of the extra dimensions, $G_N=G_8/V_{\mathrm{extra}}$ with $V_{\mathrm{extra}}=bc^3\propto a^{-3\gamma}$. So $G_N\propto a^{3\gamma}$ and $\dot G_N/G_N=3\gamma H_0=2.63\,H_0$, about $1.8\times10^{-10}$ per year for $H_0=67.4$ km/s/Mpc, some 1800 times the order-of-magnitude bound of $10^{-13}$ per year from lunar laser ranging (timing laser pulses reflected from the Moon) recorded in fits.json; and $G_N(z=1)/G_N(0)=2^{-3\gamma}=0.162$. The constant-$G_N$ Friedmann equation used in EXP-3 is itself inconsistent with this.
4. **It needs negative 8-dimensional energy.** Insert $H_b=0$ and $H_c=-\gamma H_a$ into the EXP-2 constraint: $\kappa\rho_8=3H_a^2+3\gamma^2H_a^2-9\gamma H_a^2=3H_a^2(1-3\gamma+\gamma^2)$. For $\gamma=0.875$ this is $-2.579\,H_a^2<0$. The quadratic $1-3\gamma+\gamma^2$ is negative for every $\gamma$ between its roots $(3-\sqrt5)/2=0.382$ and $(3+\sqrt5)/2=2.618$, so any sustained deflation in that range needs negative total energy density; and EXP-2 showed that the extra times turn to expansion by themselves.
5. **Its own history.** Its $\rho_\psi$ is negative beyond $z=6.83$, and its $p/\rho$ crosses $-1$ at $z=0.230$.

Its distances are close to those of the quoted CPL model (largest difference 0.021 mag, 0.011 mag with the offset profiled), but so are those of $\Lambda$CDM (0.024 and 0.013 mag), so distances at this level do not distinguish it from a cosmological constant; its own distance fits give CPL $(-0.9707,-0.1611)$ and constant $w=-1.0159$.

![EXP-3 $(w_0,w_a)$ plane: (a) the tangent CPL parameters of the condensate for $x_0\in[-0.49,0]$ with the five canonical couplings, the quoted point, $\Lambda$CDM, the line $w_0+w_a=-1$ and the distance-inferred point of the deflation variant; (b) the supplementary restricted fits of the scan, far from the quoted point for every $x_0<0$.](artifacts/dirac16complex/numerics/figures/exp3_w0wa_plane.png)

**Verification of EXP-3.** 14 of 14 self-checks (for example `sigma_from_spinor_equals_a_minus_3`, `rho_p_w_match_closed_form`, `phantom_crossing_at_cube_root_2abs_x0`, `hubble_positive_backward_stop_at_predicted_bounce`), 32 of 32 checker checks and 10 of 10 analysis checks. $\sigma$ computed from the spinor agrees with $a^{-3}$ to $2.50\times10^{-9}$ (refined run: $2.10\times10^{-10}$); the time and distance agree with independent quadratures to about $10^{-9}$; the Nelder-Mead minimiser recovers synthetic CPL and constant-$w$ curves to about $10^{-12}$. The Mathematica notebook derives the Friedmann constraint, the continuity equation, $w$ and $q_{\mathrm{dec}}$ symbolically and agrees with the Rust solution to $2.12\times10^{-8}$ in the spinor.

**What EXP-3 shows.** The attractive condensate is the only object in this framework whose own pressure is negative. Its negative pressure $\tfrac\lambda2S^2\propto a^{-6}$ matters only at high density, that is in the past, and there it wins over the positive $mS$: going back in time the effective mass passes through zero. Today's $w_0$ can be tuned to any value in $(-1,0)$ by the single parameter $x_0$, but then $w_a=3x_0/(1+x_0)^2$ is fixed, and the evolution is fast. **What it does not show.** The crossing of $w=-1$ is not an established phantom crossing: it is the instant where the effective mass vanishes, and beyond it the single mean-field mode occupies a negative-energy level. Everything computed there (phantom $w$, $\mathrm{KE}_L<0$, $\rho_\psi<0$, the bounce) is an artefact of the approximation. No fluctuations, no fit to data and no likelihood were computed.

### 11.10 EXP-4a: a thermal gas of quanta

**Purpose and assumptions.** EXP-4 looks at quanta instead of a condensate. It assumes a 3-space universe of the Friedmann type with the hidden space and the extra times static ($b=c=1$), and asks how the equation of state of a gas of quanta changes as the universe expands (EXP-4a), and how many quanta the end of inflation creates (EXP-4b and EXP-4c, Section 11.11). Only momenta in 3-space are used: the hidden-space momentum $k_0$ is set to zero. The hidden direction is space-like and in the good sector, so this is an **assumption**, not a consequence: it holds for a small compact hidden dimension whose lowest excitation energy is much larger than the temperatures and Hubble rates used, or it is imposed by hand. With $k_0$ allowed, the relativistic 3-space pressure would be $\rho/4$ instead of $\rho/3$.

**The mode equation.** A mode with comoving momentum $k$ along $x_1$ has physical momentum $K=k/a$, which redshifts as $\dot K=-KH$, and

$$
i\dot u=h(t)\,u,\qquad h=-im\gamma^4-K\gamma^4\gamma^1,\qquad h^2=E^2,\qquad E=\sqrt{m^2+K^2}.
$$

**Eight copies of a two-level system.** Let $Z=-i\gamma^4$ (as in Section 11.3) and $X=-\gamma^4\gamma^1$, so that $h=mZ+KX$. Then $Z^2=-(\gamma^4)^2=1$, $X^2=\gamma^4\gamma^1\gamma^4\gamma^1=\gamma^1\gamma^1=1$ (using $\gamma^4\gamma^1\gamma^4=\gamma^1$), and $ZX+XZ=i(\gamma^4\gamma^4\gamma^1+\gamma^4\gamma^1\gamma^4)=i(-\gamma^1+\gamma^1)=0$. Two anticommuting matrices that square to 1 obey the same rules as the Pauli matrices $\sigma_z$ and $\sigma_x$ (Chapter 2). We now show that the 16 components split into 8 two-component blocks on each of which $Z$ and $X$ act as $\sigma_z$ and $\sigma_x$. Both matrices are Hermitian (Section 11.3: $-i\gamma^4$ and $\gamma^4\gamma^j$ for $j\le3$). Since $Z$ is Hermitian with $Z^2=1$, its eigenvalues are $\pm1$, and its two eigenspaces are orthogonal. If $Zv=v$ then $Z(Xv)=-XZv=-Xv$, and $X^2=1$, so $X$ maps the $+1$ eigenspace one-to-one onto the $-1$ eigenspace (and back), and each has dimension 8. Take an orthonormal basis $v_1,\dots,v_8$ of the $+1$ eigenspace. The vectors $Xv_1,\dots,Xv_8$ are orthonormal, because $(Xv_n)^\dagger(Xv_l)=v_n^\dagger X^\dagger Xv_l=v_n^\dagger X^2v_l=v_n^\dagger v_l$, and together the 16 vectors form an orthonormal basis. On each pair $(v_n,Xv_n)$, $Z$ multiplies the first vector by $+1$ and the second by $-1$, and $X$ sends the first to the second and the second back to the first ($X(Xv_n)=X^2v_n=v_n$): in this pair of basis vectors $Z=\sigma_z$ and $X=\sigma_x$. So in this basis $h=(m\sigma_z+K\sigma_x)\otimes I_8$; since $Z$ and $X$ do not depend on $t$, the same basis serves at every time (the study also verified this numerically). So there are **8 spin states per momentum**, each a two-level system with energies $\pm E$. The relation $Ch^\ast C=-h$ maps particles to antiparticles.

**Per mode.** $\varepsilon=u^\dagger hu$, $p_1=-K\,u^\dagger\gamma^4\gamma^1u$ and $s=u^\dagger(-i\gamma^4)u$, with $\varepsilon=ms+p_1$ (Section 11.4).

**Counting states and the thermal sums.** In a box, the number of momentum states per unit volume in $d^3K$ is $d^3K/(2\pi)^3$. (In units with $\hbar=1$, as in Chapter 8, momentum and wave number coincide. In a periodic box of side $L_{\mathrm{box}}$ a plane wave $e^{iK\cdot x}$ must repeat after $L_{\mathrm{box}}$ in each direction, so the allowed momenta are $K=2\pi n/L_{\mathrm{box}}$ with integer components $n$: one state per volume $(2\pi/L_{\mathrm{box}})^3$ of momentum space, that is $L_{\mathrm{box}}^3\,d^3K/(2\pi)^3$ states in $d^3K$, and $d^3K/(2\pi)^3$ per unit volume of space.) For an isotropic distribution $d^3K=4\pi K^2dK$, which gives $K^2dK/(2\pi^2)$ per state label. With $K=k/a$ this is $k^2dk/(2\pi^2a^3)$. There are 16 states per momentum (8 particle and 8 antiparticle states), and each is occupied with the Fermi-Dirac probability $f=1/(e^{E/T}+1)\le1$: the Pauli principle. (At temperature $T$, in units with Boltzmann's constant 1 and with equal numbers of particles and antiparticles, so that the chemical potential is zero, a fermion state of energy $E$ is occupied with probability $1/(e^{E/T}+1)$, never more than 1; Section 12.14 derives this Fermi-Dirac distribution.) The pressure of an isotropic gas is the average momentum flux: a particle with momentum $K$ and speed $v=K/E$ carries $K_xv_x$ across a plane perpendicular to $x$, and averaging over directions gives $Kv/3=K^2/(3E)$. The program integrates a mode moving along $x_1$ and divides its $p_1$ by 3. The gas is treated as **collisionless** (an assumption of EXP-4: the quanta are free, and the $\lambda$ interaction between them is not included): after $a=1$ nothing changes the occupation of a comoving mode, so $f$ keeps its initial value $f(k)=1/(e^{E_{\mathrm{in}}/T_{\mathrm{in}}}+1)$ (here $E_{\mathrm{in}}=\sqrt{m^2+k^2}$ at $a=1$), while each mode's energy and pressure evolve. The integrals over $k$ are done with **Gauss-Legendre quadrature**: 48 nodes $k_n$ and weights $\omega_n$ on $[0,k_{\max}]$, chosen so that $\sum_n\omega_nF(k_n)$ equals $\int_0^{k_{\max}}F\,dk$ exactly for every polynomial $F$ of degree up to 95 (we write the weights $\omega_n$ because $w$ is the equation of state). With $W_n=\tfrac{16}{2\pi^2}\omega_nk_n^2f_n$:

$$
\rho=\frac{1}{a^3}\sum_nW_n\,\varepsilon_n,\qquad p=\frac{1}{3a^3}\sum_nW_n\,p_{1,n},\qquad \mathrm{KE}_H=3p,\qquad \mathrm{PE}_H=\rho-3p,
$$

compared with the kinetic-theory integrals

$$
\rho_{\mathrm{kin}}=\frac{16}{2\pi^2a^3}\int_0^{k_{\max}}k^2f\,E\,dk,\qquad p_{\mathrm{kin}}=\frac{16}{2\pi^2a^3}\int_0^{k_{\max}}k^2f\,\frac{K^2}{3E}\,dk .
$$

**The two limits.** When $K\gg m$, $E\approx K$ and each mode has $p/\rho=K^2/(3E\cdot E)\approx1/3$: radiation, and $\rho\propto a^{-3}\cdot a^{-1}=a^{-4}$ because each energy redshifts as $1/a$. When $K\ll m$, $E\approx m$ and $p/\rho\approx K^2/(3m^2)\to0$: dust, and $\rho\propto a^{-3}$.

**Parameters.** $m=1$; radiation era $a(t)=(t/t_{\mathrm{in}})^{1/2}$ with $t_{\mathrm{in}}=1/(2H_{\mathrm{in}})=10$, so $H_{\mathrm{in}}=0.05$; comoving temperature $T_{\mathrm{in}}=10$ at $a=1$ (relativistic); $a$ from 1 to 100 ($t$ from 10 to $10^5$), 61 samples uniform in $\ln a$; $k_{\max}=12T_{\mathrm{in}}=120$. Each mode starts from the positive-energy $B=+1$ eigenvector of $h(t_{\mathrm{in}})$. Extras: a second spin state for four nodes, a negative-energy mode for one node, and the first-order adiabatic vacuum (Section 11.11) for two nodes. Each thermal mode turns through about $10^5$ radians, which is why the tolerance is $10^{-13}$: at $10^{-10}$ the Hilbert norm drifted by $2.4\times10^{-4}$.

![EXP-4 thermal gas: (a) $w=p/\rho$ of the CVODE mode sum and of kinetic theory against $a$, from $1/3$ towards 0; (b) relative deviations of $\rho$ (about $10^{-8}$) and of $p$ (up to $1.9\times10^{-5}$, the sudden-start wave) from kinetic theory.](artifacts/dirac16complex/numerics/figures/exp4_thermal_w.png)

![EXP-4 thermal gas scaling: (a) $\rho a^4$, constant while the gas is relativistic, and (b) $\rho a^3$, constant once it is non-relativistic.](artifacts/dirac16complex/numerics/figures/exp4_thermal_scaling.png)

![EXP-4 kinetic and potential energy of the gas: $\mathrm{KE}_H/\rho=3w$ (momentum energy) falls from 1 and $\mathrm{PE}_H/\rho$ (rest mass) rises towards 1, while the Lagrangian split stays at $\mathrm{KE}_L/\rho=\mathrm{PE}_L/\rho=1/2$.](artifacts/dirac16complex/numerics/figures/exp4_thermal_split.png)

**Results** (exp4/summary.json, key thermal).

- **From radiation to dust.** $w=0.3328543348$ at $a=1$ (kinetic theory: the same to ten digits; slightly below $1/3$ because $m=T_{\mathrm{in}}/10$ is not zero) and $w=0.0359224$ at $a=100$ (kinetic theory 0.0359223), both on the grid $k\le k_{\max}$. $\rho a^4$ is constant early and $\rho a^3$ late. The momentum energy $\mathrm{KE}_H=3p$ gives way to rest-mass energy: $\mathrm{KE}_H/\rho=3w$ falls from about 1 to about 0.11. For every mode of a free gas $\mathrm{KE}_L=\mathrm{PE}_L=\rho/2$, so the scalar-field relation $p=\mathrm{KE}-\mathrm{PE}$ of split (A) holds only for condensates.
- **Agreement with kinetic theory.** $\rho$ agrees to $1.98\times10^{-8}$. $p$ deviates by up to $1.87\times10^{-5}$, independently of the tolerance. The cause is physical, not numerical: starting a mode on the instantaneous eigenvector leaves a small admixture $\beta$ of the other energy level, which enters the pressure $p_1$ at first order but the energy $\varepsilon$ only at second order (both are derived after this list). The deviation stays inside the envelope that the checker predicts from the first-order term (ratio 0.28, check `thermalPressureMatchesKineticTheoryPlusFreeWave`), and the runs that start in the adiabatic vacuum reduce the single-mode pressure deviation from 1.78 to 0.12 relative.
- **No spurious particle production.** The occupation-weighted $|\beta|^2$ is $3.7\times10^{-8}$, and the adiabatic-vacuum runs end at $5.6\times10^{-8}$. The largest single-mode value, $6.37\times10^{-5}$ at $k=0.953$, is 0.779 times $4\delta_k^2$, where $\delta_k=mkH_{\mathrm{in}}/(4E_{\mathrm{in}}^3)$ is the amplitude of the sudden-start wave (derived after this list; Exercise 11.11 evaluates $\delta_k^2$): a free wave left by the start, not particle production.
- **Exact symmetries.** Spin independence and particle-antiparticle symmetry hold exactly (deviation 0.0).
- **Momentum truncation.** The cut $k\le12T_{\mathrm{in}}$ misses $2.4\times10^{-3}$ of $\rho$ at $a=1$ and, at $a=100$, $9.0\times10^{-4}$ of $\rho$ and $5.3\times10^{-3}$ of $p$. Without the cut the gas has $w=0.0361$ at $a=100$ instead of 0.0359. The truncation is reported, not corrected.

**The sudden-start wave.** Its size follows from the adiabatic expansion of Section 11.11, which we use here ahead of its derivation. A mode that is not excited is not exactly the instantaneous positive-energy eigenvector: to first order it carries a small admixture of the other level, the **adiabatic dressing**, of size $\delta_k(t):=|\dot\theta|/(4E)=mKH/(4E^3)$ at the time $t$ (Section 11.11, with $\dot\theta=-mKH/E^2$). Such an unexcited mode is the first-order adiabatic vacuum. The program starts each thermal mode exactly on the instantaneous eigenvector of $h(t_{\mathrm{in}})$, so the start differs from the adiabatic vacuum by the dressing at the start, evaluated at $a=1$ where $K=k$:

$$
\delta_k:=\delta_k(t_{\mathrm{in}})=\frac{mkH_{\mathrm{in}}}{4E_{\mathrm{in}}^3},\qquad E_{\mathrm{in}}=\sqrt{m^2+k^2}.
$$

This difference then travels along with the mode as a free wave of the negative-energy level with the constant amplitude $\delta_k$. Measured in the first-order adiabatic basis, the final $|\beta|^2$ of every thermal mode with $\delta_k^2\ge10^{-10}$ equals $\delta_k^2$ to 1.2% (`thermalSuddenStartMaxRelDev` in `exp4/python-check-report.json`). The program measures $|\beta|$ in the instantaneous basis, and there it sees the free wave plus the instantaneous dressing $\delta_k(t)$, with a relative phase that oscillates. At the start the two parts have the same size (and cancel, since the mode starts on the eigenvector). Afterwards the dressing only shrinks: in the radiation era $H=H_{\mathrm{in}}/a^2$ and $K=k/a$, so that $\delta_k(t)=\frac{mH_{\mathrm{in}}}{4k^2}\bigl(\frac KE\bigr)^3$, and $K/E=K/\sqrt{m^2+K^2}$ falls as $K$ falls. Hence

$$
|\beta|\le\delta_k+\delta_k(t)\le2\delta_k,\qquad |\beta|^2\le(2\delta_k)^2=4\delta_k^2 ,
$$

which is the origin of the factor 4. The bound is approached about half an oscillation after the start, when the two parts first come into phase; the output samples do not resolve that moment, and the checker's dense sampling finds $7.49\times10^{-5}$ there in the mode $k=0.953$, 0.917 times $4\delta_k^2$. The checker tests the envelope $(1.1\,\delta_k+\delta_k(t))^2$, which allows 10% on the free-wave amplitude (check `thermalBetaPerModeIsSuddenStartWave`).

**Why the pressure feels the wave and the energy does not.** Work in one two-level block of this section, where $Z=\sigma_z$, $X=\sigma_x$ and $h=m\sigma_z+K\sigma_x=E(\cos\theta\,\sigma_z+\sin\theta\,\sigma_x)$ with $\cos\theta=m/E$ and $\sin\theta=K/E$. Its eigenvectors are $u_+=(\cos\tfrac\theta2,\sin\tfrac\theta2)$ with energy $+E$ and $u_-=(-\sin\tfrac\theta2,\cos\tfrac\theta2)$ with energy $-E$ (Exercise 11.12 checks this; Section 11.11 uses the same basis). The pressure of the mode is $p_1=-K\,u^\dagger\gamma^4\gamma^1u=K\,u^\dagger Xu$. Since $\sigma_x$ exchanges the two components, $\sigma_x(a,b)=(b,a)$,

$$
\begin{aligned}
&u_+^\dagger Xu_+=2\cos\tfrac\theta2\sin\tfrac\theta2=\sin\theta=\frac KE,\qquad u_-^\dagger Xu_-=-\sin\theta=-\frac KE,\\
&u_+^\dagger Xu_-=u_-^\dagger Xu_+=\cos^2\tfrac\theta2-\sin^2\tfrac\theta2=\cos\theta=\frac mE .
\end{aligned}
$$

Write the mode as $u=\alpha u_++\beta u_-$ with complex amplitudes and $|\alpha|^2+|\beta|^2=1$ (a normalised mode). Expanding $u^\dagger Xu$ and using $|\alpha|^2=1-|\beta|^2$,

$$
p_1=K\Bigl[(|\alpha|^2-|\beta|^2)\frac KE+(\alpha^\ast\beta+\alpha\beta^\ast)\frac mE\Bigr]=(1-2|\beta|^2)\frac{K^2}{E}+2\,\mathrm{Re}(\alpha^\ast\beta)\,\frac{mK}{E},
$$

while $\varepsilon=u^\dagger hu=E(|\alpha|^2-|\beta|^2)=E(1-2|\beta|^2)$, because $hu_\pm=\pm Eu_\pm$ and $u_+^\dagger u_-=0$. The energy changes only at second order in $\beta$. The pressure has the term $2\,\mathrm{Re}(\alpha^\ast\beta)\,mK/E$, linear in $\beta$, which oscillates with the relative phase of the two levels. This linear term is what the pressure envelope bounds: the checker inserts the bound $|\beta|\le1.1\,\delta_k+\delta_k(t)$ into $|p_1-K^2/E|\le2|\beta|\,mK/E+2|\beta|^2K^2/E$ and sums over the modes, and the measured deviation of the gas pressure reaches at most 0.28 of this envelope.

### 11.11 EXP-4b and EXP-4c: quanta created by the end of inflation

**Pair creation in plain words.** In an expanding universe the Hamiltonian $h(t)$ of every mode changes with time. If it changes slowly, a state that starts in the positive-energy level stays in the positive-energy level of the instantaneous $h$ (this is the adiabatic theorem of quantum mechanics). If it changes quickly, part of the state ends in the other level. Apply this to the Dirac sea: every filled negative-energy state ends with a small weight on the positive-energy level. A particle has appeared, and the hole it leaves behind is an antiparticle. This is **gravitational pair creation**; nothing but the expansion is needed.

**Instantaneous levels.** Since $h^2=E^2$, the matrices $P_\pm=\tfrac12(1\pm h/E)$ satisfy $P_\pm^2=\tfrac14(1\pm2h/E+h^2/E^2)=P_\pm$: they project onto the positive- and negative-energy levels. For a mode that starts in its positive-energy level (in the adiabatic vacuum defined below), the weight it ends with on the negative-energy level is

$$
|\beta_k|^2=\frac{|P_-u|^2}{|u|^2}.
$$

In each two-level block the evolution over the whole run is a 2 by 2 unitary matrix $U$ (because $h$ is Hermitian). Its first column and its first row are both unit vectors, so $|U_{++}|^2+|U_{-+}|^2=1=|U_{++}|^2+|U_{+-}|^2$ and hence $|U_{-+}|=|U_{+-}|$: the weight that a filled negative-energy state ends with on the positive-energy level equals $|\beta_k|^2$. With 8 filled sea states per $k$, the expansion leaves $8|\beta_k|^2$ particles and $8|\beta_k|^2$ antiparticles per momentum, and the comoving number density of the created quanta is

$$
na^3=\frac{16}{2\pi^2}\int k^2\,|\beta_k|^2\,dk .
$$

**The adiabatic expansion** (derived here in outline, following the Stage-3 study). In one block write $h=E(\cos\theta\,\sigma_z+\sin\theta\,\sigma_x)$ with $\tan\theta=K/m$. Its eigenvectors are $u_+=(\cos\tfrac\theta2,\sin\tfrac\theta2)$ with energy $+E$ and $u_-=(-\sin\tfrac\theta2,\cos\tfrac\theta2)$ with energy $-E$, and they rotate as $\dot u_+=\tfrac{\dot\theta}2u_-$, $\dot u_-=-\tfrac{\dot\theta}2u_+$. Insert $u=\alpha(t)e^{-i\varphi}u_++\beta(t)e^{i\varphi}u_-$ with $\varphi=\int E\,dt$ into $i\dot u=hu$. The terms with $E$ cancel, and comparing the coefficients of $u_+$ and $u_-$ gives

$$
\dot\alpha=\frac{\dot\theta}{2}\,\beta\,e^{2i\varphi},\qquad \dot\beta=-\frac{\dot\theta}{2}\,\alpha\,e^{-2i\varphi}.
$$

From $\theta=\arctan(K/m)$ and $\dot K=-KH$, $\dot\theta=m\dot K/(m^2+K^2)=-mKH/E^2$. With $\alpha\approx1$, $\beta(t)=-\int^t\tfrac{\dot\theta}2e^{-2i\varphi}dt'$. Integrate by parts using $e^{-2i\varphi}=\frac{d}{dt}(e^{-2i\varphi})/(-2iE)$:

$$
\beta(t)=\frac{\dot\theta}{4iE}\,e^{-2i\varphi}+\int^t e^{-2i\varphi}\,\frac{d}{dt'}\Bigl(\frac{i\dot\theta}{4E}\Bigr)dt' .
$$

The first term, of size $|\dot\theta|/(4E)=mKH/(4E^3)$, is present at every instant and disappears when the expansion stops; it is the **adiabatic dressing** of an unexcited mode, not created particles. The program therefore measures $|\beta_k|^2$ in the **first-order adiabatic basis**, which removes this term. The remaining integral is small as long as $\dot\theta/E$ changes smoothly. Integrating by parts once more shows what happens at a kink: if $\frac{d}{dt}(\dot\theta/E)$ jumps at $t=0$, the boundary terms at $t=0^-$ and $t=0^+$ no longer cancel and leave a created amplitude of size $|\Delta\ddot\theta|/(8E^2)$, where $\Delta\ddot\theta$ is the jump of $\ddot\theta$ ($E$ and $\dot\theta$ are continuous).

**The sudden end of inflation (EXP-4b).** The background is de Sitter, $a=e^{H_{\mathrm{inf}}t}$ for $t<0$, glued at $t=0$ to radiation, $a=(1+2H_{\mathrm{inf}}t)^{1/2}$. Both give $a(0)=1$ and $H(0)=H_{\mathrm{inf}}$ (for radiation $H=H_{\mathrm{inf}}/(1+2H_{\mathrm{inf}}t)$), so $a$ and $H$ are continuous; but $\dot H$ jumps from 0 to $-2H_{\mathrm{inf}}^2$. This is called a $C^1$ junction. A function is $C^1$ if it and its first derivative are continuous (and $C^2$ if its second derivative is continuous as well); here $a(t)$ and $\dot a=aH$ are continuous, but $\ddot a$ jumps at $t=0$, from $+H_{\mathrm{inf}}^2$ to $-H_{\mathrm{inf}}^2$, and with it $\dot H=\ddot a/a-H^2$; so $a$ is $C^1$ but not $C^2$. Differentiating $\dot\theta=-mKH/E^2$, the only discontinuous piece of $\ddot\theta$ is $-mK\dot H/E^2$, so $\Delta\ddot\theta=2mKH_{\mathrm{inf}}^2/E^2$, and at $a=1$ ($K=k$) the created weight is

$$
|\beta_k|^2\approx\Bigl(\frac{mk\,H_{\mathrm{inf}}^2}{4E^4}\Bigr)^2 ,\qquad E=\sqrt{m^2+k^2},
$$

the **kink formula**. It is the leading term of an expansion that is valid for $E\gg H_{\mathrm{inf}}$, so it describes the large-$k$ tail. Integrated over all $k$ it gives $na^3=H_{\mathrm{inf}}^4/(64\pi m)$ (Exercise 11.13): the number that the jump of $\dot H$ alone would create.

**Parameters.** $H_{\mathrm{inf}}=1$, masses $m/H_{\mathrm{inf}}\in\{0,0.1,0.5,1,2\}$, 64 Gauss-Legendre nodes in $\ln k$ on $[10^{-3},40]$. Each mode starts in the first-order adiabatic vacuum when it is deep inside the horizon, at $k/a=200H_{\mathrm{inf}}$, and the run ends when $H=10^{-4}m$, that is at $a_{\mathrm{end}}^2=10^4H_{\mathrm{inf}}/m$ (for $m=0$ the end of $m=0.1$ is used). The integration is restarted at $t=0$. The analytic kink tail beyond $k=40$ is added separately as a correction.

**The same transition made smooth (EXP-4c).** To measure how much of the yield is due to the sharp junction, every mode is integrated again in a background in which the transition takes about one Hubble time:

$$
\frac1H=\frac{1}{H_{\mathrm{inf}}}+\tau\ln\bigl(1+e^{2t/\tau}\bigr),\qquad \epsilon_H:=-\frac{\dot H}{H^2}=\frac{d}{dt}\Bigl(\frac1H\Bigr)=1+\tanh\frac t\tau,\qquad \tau=\frac{1}{H_{\mathrm{inf}}},
$$

which is de Sitter ($\epsilon_H=0$) long before $t=0$ and radiation ($\epsilon_H=2$) long after. Here $\ln a$ has no closed form and is integrated by CVODE as a 33rd state component. Because $H_{\mathrm{smooth}}\le H_{\mathrm{sudden}}$ at every time, the smooth universe expands less, and its late-time $a$ is smaller by the constant factor 0.656. An abundance depends on the number density at a given $H$, so the comparison “at the same final $H$” multiplies the smooth $na^3$ by $0.656^{-3}$.

**Results** (exp4/summary.json, key pair). The sudden transition, on the grid $k\le40$, final spectrum in the first-order adiabatic basis:

| $m/H_{\mathrm{inf}}$ | $na^3$ in units of $H_{\mathrm{inf}}^3$ | largest final $\lvert\beta_k\rvert^2$ |
| --- | --- | --- |
| 0 | $1.8\times10^{-24}$ | $7.7\times10^{-25}$ |
| 0.1 | $1.454\times10^{-3}$ | 0.347 |
| 0.5 | $4.990\times10^{-3}$ | 0.0510 |
| 1 | $4.412\times10^{-3}$ | 0.00588 |
| 2 | $2.421\times10^{-3}$ | $3.54\times10^{-4}$ |

The smooth transition, compared at the same final $H$, and the kink formula integrated over all $k$:

| $m/H_{\mathrm{inf}}$ | $na^3$ smooth | sudden / smooth | $H_{\mathrm{inf}}^4/(64\pi m)$ |
| --- | --- | --- | --- |
| 0.1 | $1.074\times10^{-3}$ | 1.35 | $4.97\times10^{-2}$ |
| 0.5 | $1.536\times10^{-3}$ | 3.25 | $9.95\times10^{-3}$ |
| 1 | $3.327\times10^{-4}$ | 13.3 | $4.97\times10^{-3}$ |
| 2 | $3.043\times10^{-6}$ | 796 | $2.49\times10^{-3}$ |

The equation of state of the created gas, from its final (frozen) spectrum; “$w$ at $a=1$” evaluates that spectrum at $a=1$, a hypothetical value, because the occupation of the long-wavelength modes is not yet final there:

| $m/H_{\mathrm{inf}}$ | $w$ at $a=1$ | $w$ at the end | $\rho a^3$ at the end |
| --- | --- | --- | --- |
| 0 | $1/3$ | $1/3$ | $1.3\times10^{-26}$ |
| 0.1 | 0.3081 | $1.20\times10^{-4}$ | $1.454\times10^{-4}$ |
| 0.5 | 0.2539 | $1.14\times10^{-4}$ | $2.495\times10^{-3}$ |
| 1 | 0.2386 | $1.62\times10^{-4}$ | $4.413\times10^{-3}$ |
| 2 | 0.2395 | $3.02\times10^{-4}$ | $4.845\times10^{-3}$ |

![EXP-4 pair creation by the de Sitter to radiation transition: $\lvert\beta_k\rvert^2$ at the end (first-order adiabatic basis) for $m/H_{\mathrm{inf}}=0.1$, 0.5, 1 and 2, with the kink tail (dashed) and the spectra of the smooth transition (dotted); for $m=0$, $\lvert\beta_k\rvert^2\le7.7\times10^{-25}$ (no production).](artifacts/dirac16complex/numerics/figures/exp4_pair_spectra.png)

![EXP-4 (a) the created comoving number density $na^3$ (adiabatic basis solid, instantaneous basis dashed), and (b) the equation of state of the created gas with its final spectrum, from nearly $1/3$ when evaluated at $a=1$ to dust.](artifacts/dirac16complex/numerics/figures/exp4_pair_density.png)

- **Production for $m>0$ only.** For $m=0$, $h=K(t)\,\sigma_x\otimes I_8$: its eigenvectors, those of $\sigma_x$, do not depend on $K$, so $\theta=\pi/2$ is constant, $\dot\theta=0$, and no state ever leaves its level. This is the conformal invariance of the massless equation (it does not change when all lengths are rescaled by a time-dependent factor, and an expanding universe of this type is flat space rescaled in this way), and the measured $|\beta_k|^2$ ($8.5\times10^{-25}$ at most over the run) is roundoff. For $m>0$ the sudden transition gives a few $10^{-3}H_{\mathrm{inf}}^3$, and $|\beta_k|^2\le1$ everywhere, as the Pauli principle requires (check `pairPauli`).
- **What sets the yield.** The large-$k$ tail follows the kink formula to 4.2% (limit 35%; checks `pair_tail_matches_kink_theory` and `pairTailMatchesKinkTheory`). For $m\gtrsim H_{\mathrm{inf}}$ the whole sudden yield is the response to the jump of $\dot H$: the kink formula integrated over all $k$ is 1.13 and 1.03 times the computed $na^3$ for $m=1$ and 2, and the smooth transition gives 13.3 and 796 times fewer quanta at the same final $H$. For $m=0.5$ the sharpness still matters (factor 3.25). Only the light field, $m=0.1$, is robust: its production comes from small $k$, from modes that were stretched beyond the Hubble length during inflation, and the smooth transition changes its largest $|\beta_k|^2$ only from 0.347 to 0.346 and its $na^3$ by a factor 1.35. So the ranking of the sudden yields (largest near $m=0.5H_{\mathrm{inf}}$) and their size for $m\gtrsim0.5H_{\mathrm{inf}}$ are properties of the chosen junction; the sudden values are the yields of an idealised instantaneous end of inflation.
- **The created gas becomes dust.** Its $w$ is between 0.24 and 0.31 when its final spectrum is evaluated at $a=1$ and about $10^{-4}$ at the end, and $\rho a^3$ approaches $m\,na^3$ (for $m=1$: $4.413\times10^{-3}$ against $na^3=4.412\times10^{-3}$).
- **Basis and truncation.** The literal instantaneous-basis final $|\beta_k|^2$ includes the adiabatic dressing at the end of the run and gives almost the same numbers ($na^3=1.455\times10^{-3}$, $4.991\times10^{-3}$, $4.414\times10^{-3}$ and $2.422\times10^{-3}$). The analytic tail beyond $k=40$ adds $1.05\times10^{-6}$ to $na^3$ for $m=2$ (a fraction $4.3\times10^{-4}$).

**Verification of EXP-4.** 23 of 23 self-checks and 54 of 54 checker checks. The checker recomputes every mode sum from the raw spinors, re-derives kinetic theory with its own quadrature, and re-integrates every one of the 320 sudden and 320 smooth pair modes with an independent fourth-order Magnus method (a step-by-step integrator for linear equations whose steps are exactly unitary) for the two-level reduction: the final $|\beta_k|^2$ agree with the Rust values to $10^{-6}$ relative (checks `pairSuddenSpectrumMagnusReference` and `pairSmoothTransitionReference`). Unitarity holds to $2.4\times10^{-7}$ (thermal) and $4.1\times10^{-8}$ (pairs). The thermal modes carry a phase error of at most $6.5\times10^{-6}$ rad at $a=100$ that the refined run does not reduce (the same time-rounding effect as in EXP-2); only phase-independent quantities ($\varepsilon$, $p_1$, $s$, $|\beta|^2$) enter the results. The Mathematica notebook re-integrates four thermal nodes and ten pair modes with NDSolve (the two hardest thermal nodes only up to $a=10$, so for them the cross-check is partial).

**What EXP-4 shows.** In the good sector, with the extra dimensions held static and no hidden-space momentum, dirac16complex quanta are an ordinary gas of massive fermions with 16 states per momentum. Their pressure is momentum flux and redshifts away, so the equation of state goes continuously from radiation to dust. The expansion itself creates such quanta for every $m>0$. **What it does not show.** No relic density in physical units: that needs physical values of $m$ and $H_{\mathrm{inf}}$ and the history after inflation, none of which the framework fixes; and for $m\gtrsim0.5H_{\mathrm{inf}}$ the yield depends strongly on how inflation ends. Whether such a relic would be hot, warm or cold dark matter depends on its free streaming, which was not computed.

### 11.12 EXP-5: momentum along an extra time

**Purpose.** Every result above uses the good sector. EXP-5 shows why: a mode with momentum along an extra time becomes unstable once the extra times have deflated enough.

**Equations.** The extra times deflate as $c=h_5=h_6=h_7=e^{-Ht}$ ($H=1$), and a mode has momentum $q$ along $x_5$ and none elsewhere ($m=1$). Its physical momentum is $Q(t)=q/h_5=q\,e^{Ht}$, and by Section 11.3 (with $\eta^{55}=-1$)

$$
h(t)=-im\gamma^4-Q(t)\,\gamma^4\gamma^5,\qquad h^2=E^2(t)=m^2-q^2e^{2Ht},\qquad E^2<0\ \text{for}\ t>t_\ast=\frac{\ln(m/q)}{H}.
$$

$h$ is not Hermitian (Section 11.3), so the Hilbert norm $u^\dagger u$ is not conserved; but $h^\dagger B=Bh$, so the Krein norm $u^\dagger Bu$ is. After $t_\ast$ the eigenvalues of $h$ are $\pm i\varkappa$ with $\varkappa=\sqrt{Q^2-m^2}$, and $i\dot u=\pm i\varkappa u$ gives $u\propto e^{\pm\int\varkappa\,dt}$: one part grows. At leading order in the WKB approximation (the approximation that the coefficients change slowly compared with the local rate), $d\ln(u^\dagger u)/dt=2\varkappa$; at the next order $2\varkappa-m^2/\varkappa^2$. The growth exponent $W(t)=\int_{t_\ast}^t\varkappa\,dt'$ has a closed form: with $dQ=QH\,dt$,

$$
W(t)=\frac1H\int_m^{Q(t)}\frac{\sqrt{Q'^2-m^2}}{Q'}\,dQ'=\frac1H\Bigl[\sqrt{Q^2-m^2}-m\arccos\frac mQ\Bigr],
$$

as one checks by differentiating (with $\frac{d}{dQ}\arccos(m/Q)=m/(Q\sqrt{Q^2-m^2})$):

$$
\frac{d}{dQ}\Bigl[\sqrt{Q^2-m^2}-m\arccos\frac mQ\Bigr]=\frac{Q}{\sqrt{Q^2-m^2}}-\frac{m^2}{Q\sqrt{Q^2-m^2}}=\frac{\sqrt{Q^2-m^2}}{Q}.
$$

**Initial data.** $q\in\{0.05,0.1\}$, so $t_\ast=\ln20=2.99573$ and $\ln10=2.30259$; $t$ runs from 0 to $t_\ast+3$ with 601 samples. The initial spinor is a positive-energy eigenvector of $h(0)$, with $E_0=\sqrt{m^2-q^2}=0.998749$ and 0.994987, that is also an eigenvector of $C$ with eigenvalue $\pm1$ (possible because $C$ commutes with $\gamma^4$ and $\gamma^5$, hence with $h(t)$). Its Krein norm is not zero: from $hu=E_0u$ and $u^\dagger u=1$, $E_0=u^\dagger hu=m\,s(u)-q\,u^\dagger\gamma^4\gamma^5u$; the first term is real, and the second is imaginary because $\gamma^4\gamma^5$ is real antisymmetric, so $s(u)=E_0/m$. With $Cu=\pm u$, $Bu=-i\gamma^4Cu=\pm(-i\gamma^4)u$ and $u^\dagger Bu=\pm E_0/m$. Four runs. The WKB comparison uses the window from the first output time at or after $t_\ast+1.5$ to $t_\ast+3$, away from the turning point.

![EXP-5 (a) $\ln(u^\dagger u)$ for both momenta and both $C$ signs with the WKB curve $2W(t)$, and (b) $E^2(t)$, which turns negative at $t_\ast=\ln(m/q)/H$ (dotted).](artifacts/dirac16complex/numerics/figures/exp5_growth.png)

![EXP-5 (a) the Krein-norm drift divided by $\max(u^\dagger u,1)$, below $10^{-8}$ throughout, and (b) the Krein norm, drawn while $u^\dagger u<10^8$, which stays at its initial value $\pm E_0/m$. Later, when $u^\dagger u$ approaches $10^{16}$, the computed $u^\dagger Bu$ is a difference of numbers of that size and loses its digits to rounding (absolute drift up to 1.005, `kreinDrift.maxAbs` in `exp5/summary.json`), which is why panel (a) divides the drift by $\max(u^\dagger u,1)$.](artifacts/dirac16complex/numerics/figures/exp5_krein.png)

**Results** (exp5/summary.json).

- $u^\dagger u$ reaches $1.258\times10^{16}$ ($q=0.05$) and $1.313\times10^{16}$ ($q=0.1$). The average growth rate of $\ln(u^\dagger u)$ is 2.37 ($q=0.05$) and 2.40 ($q=0.1$) over the first unit of time after $t_\ast$, and 25.3 over the last unit: ratios 10.7 and 10.6. The growth is faster than exponential.
- Over the WKB window, $\Delta\ln(u^\dagger u)=30.9922$ against the leading WKB value 31.0241 (relative deviation $1.03\times10^{-3}$) and the first-order value 30.99986 ($2.47\times10^{-4}$) for $q=0.05$; 30.9455 against 30.9770 and 30.9530 for $q=0.1$. The late rate matches $2\varkappa-m^2/\varkappa^2$ to $4.6\times10^{-6}$.
- The Krein norm is conserved: its drift divided by $\max(u^\dagger u,1)$ is at most $1.08\times10^{-9}$, and its absolute drift up to $t_\ast$ at most $1.28\times10^{-9}$. At the end the absolute drift is about 1 because $u^\dagger Bu$ is then a difference of two numbers of order $10^{16}$, the limit of 16-digit arithmetic.

**Verification.** 7 of 7 self-checks (for example `energy_squared_changes_sign_at_tstar`, `hilbert_norm_superexponential_growth`, `growth_matches_wkb_leading_order`) and 21 of 21 checker checks (for example `kreinConservedNormalized`, `wkbLeading`, `wkbFirstOrder`, `wkbLateRate`); an independent Runge-Kutta reference agrees to $3.34\times10^{-8}$ relative. The Mathematica notebook verifies $h^2=(m^2-Q^2)\cdot1$, $h^\dagger B=Bh$ and that $h$ is not Hermitian, and a 32-digit run agrees with machine precision to $1.8\times10^{-14}$.

**What EXP-5 shows.** A mode with extra-time momentum stops oscillating and grows once the extra-time scale factor has shrunk enough. Because the indefinite Krein norm is conserved, the growth is a growing positive-norm part together with a growing negative-norm part: the ill-posedness of wave equations with more than one time (called ultrahyperbolic). No positive Fock space exists for these modes. Any cosmology built on this field must exclude them, and every result of EXP-1 to EXP-4 is restricted to the good sector. **What it does not show.** The restriction is imposed by hand, not derived; whether some dynamical mechanism suppresses the extra-time sector is an open problem (Chapter 18).

### 11.13 What the experiments show about dark matter, and what they do not

**How pressure and energy density behave.** Three mechanisms control everything the five experiments found.

- **Dilution.** $SV$ is constant, so the mass term $mS$ behaves like dust in the 7-volume and the interaction term $\tfrac\lambda2S^2$ like a stiff fluid in the 7-volume.
- **Redshift.** The pressure of quanta is momentum flux, and momenta fall as $1/a$, so the pressure of a gas falls faster than its energy density.
- **Geometry.** What a 3-space observer infers depends on how the 7-volume grows compared with the 3-volume, $w_{\mathrm{eff}}=-1+\Theta(1+w)/(3H_a)$. In EXP-1 $\Theta=0$; in EXP-2 $\Theta\to7H_a$; in EXP-3 and EXP-4 $\Theta=3H_a$ by assumption.

Case by case:

- **Free condensate, any background (one-mode mean field):** $\rho=mS\propto1/V$ and $p=0$, dust, up to the degeneracy pressure of a Pauli-consistent state (the momentum flux of a filled Fermi sea, Section 11.4, limit 2), which was not computed.
- **Repulsive condensate:** $w\to1$ at small $V$ and $w\to0$ at large $V$ (EXP-1 pointwise, EXP-2).
- **Attractive condensate:** $p<0$, and $w\to0$ at large $V$; where $M_{\mathrm{eff}}<0$ the equations give phantom $w$ and then $\rho<0$, but these are mean-field artefacts (EXP-2, EXP-3).
- **Primordial field:** $V$ constant, so $\rho$ and $p$ are frozen: dust or slightly stiff for the positive-energy eigenstates (EXP-1).
- **Thermal gas:** $\rho\propto a^{-4}$ early and $a^{-3}$ late; $w$ falls from 0.3329 to 0.0359 (EXP-4a).
- **Created pairs:** dust ($w\approx10^{-4}$) by the end of each run, with $\rho a^3\to m\,na^3$ (EXP-4b).
- **Extra-time modes:** no positive norm and faster-than-exponential growth; $\rho$ and $p$ are not defined in a positive Fock space (EXP-5).

**What behaves like dark matter.**

1. A Pauli-consistent gas of quanta ($f\le1$, 8 + 8 states per momentum, $k_0=0$) goes from radiation to dust: $w=0.3329$ at $T=10m$ and $w=0.0359$ after a hundredfold expansion on the momentum grid (0.0361 without the cut), in agreement with kinetic theory; the momentum-energy fraction $\mathrm{KE}_H/\rho=3w$ falls from about 1 to about 0.11 (EXP-4a). This result does not depend on the one-mode picture.
2. The end of inflation creates quanta for every $m>0$ and none for $m=0$: with the sudden junction $na^3=1.454\times10^{-3}$, $4.990\times10^{-3}$, $4.412\times10^{-3}$ and $2.421\times10^{-3}\,H_{\mathrm{inf}}^3$ for $m/H_{\mathrm{inf}}=0.1$, 0.5, 1 and 2, and a transition lasting one Hubble time gives 1.35, 3.25, 13.3 and 796 times fewer at the same final $H$. The created gas is dust by the end of each run (EXP-4b, EXP-4c).
3. The free condensate is dust in every background in the one-mode picture (EXP-1 with $K=0$, EXP-2 and EXP-3 with $x_0=0$); an order-of-magnitude estimate says that its degeneracy pressure (Section 11.4, limit 2) is negligible for the free EXP-3 condensate if $m\ge21$ meV.
4. Every condensate, repulsive or attractive, becomes dust at large volume, because the interaction energy dilutes faster (EXP-2, EXP-3).

**What is not established.**

1. **Abundance.** No relic density was computed. The yields are per comoving volume in units of $H_{\mathrm{inf}}^3$; turning them into the observed dark-matter density needs physical values of $m$ and $H_{\mathrm{inf}}$ and the history after inflation, and for $m\gtrsim0.5H_{\mathrm{inf}}$ the yield itself depends strongly on how inflation ends.
2. **Darkness.** The framework has no coupling to the Standard Model of particle physics, so the quanta are dark by construction; no bounds on interactions, on annihilation through the $\lambda$ term or on decays were derived.
3. **Static extra dimensions.** In self-consistent 8-dimensional gravity all seven directions end up expanding equally, and a 3-space observer then sees dust dilute like $a^{-7}$ ($w_{\mathrm{eff}}\to4/3$, EXP-2). Dust-like dilution in 3-space, which dark matter needs, requires static extra dimensions; EXP-3 and EXP-4 assume them, nothing derives them.
4. **The extra-time sector** must be excluded by hand (EXP-5).
5. **Structure formation**, the free streaming of the quanta and their clustering were not computed.
6. **The hidden-space momentum** $k_0$ was set to zero in EXP-4; with it the relativistic pressure would be $\rho/4$.

**The answer on dark matter: a qualified yes.** In the good sector, with stabilised extra dimensions and no hidden-space momentum, dirac16complex quanta are pressureless matter at late times, and the expansion of the universe produces them gravitationally. That is a dark-matter-like equation of state and a production mechanism. It is not a dark-matter model, and nothing computed here predicts the observed amount of dark matter.

### 11.14 What the experiments show about dark energy, and what they do not

**Which mechanisms give negative pressure or $w<-1/3$.**

1. **The attractive four-fermion interaction** ($\lambda<0$) is the only mechanism with genuinely negative pressure, $p=\tfrac\lambda2S^2<0$. At low density $w=x_0\sigma/(1+x_0\sigma)$ lies between $-1$ and 0. At higher density $M_{\mathrm{eff}}$ passes through zero, and beyond that point the equations give $w<-1$ with $\rho>0$, then $\rho<0$, and in EXP-3 a bounce. **This phantom crossing is a mean-field artefact**: in all those rows the single occupied mode is a negative-energy level, outside the domain of the expectation-value rule, whereas a state with definite occupation numbers of positive-energy quanta always has $\rho+p\ge0$ (Section 11.4).
2. **The frozen density of the primordial field.** In EXP-1 $\Theta=0$, so a 3-space observer would infer $w_{\mathrm{eff}}=-1+0\cdot(1+w)=-1$, the dilution of a cosmological constant (derived here from the formula of Section 11.7, not a separate machine check). But the actual pressure is zero or positive, and the geometry is not self-consistent: 8-dimensional Einstein gravity would need $\rho_{\mathrm{req}}\le-21$.
3. **Deflating extra times** (the EXP-3 variant) give $p/\rho$ the quoted tangent by construction, but its fit over the data range is $(-0.640,-1.98)$, and it violates 4-dimensional energy conservation, the constancy of Newton's constant and the 8-dimensional energy bound (Section 11.9).

The Lagrangian has no cosmological-constant term ($U(0)=0$ is a choice of the model, Chapter 6 and Stage-1 document §7.6; adding a cosmological constant would be a new assumption, not a property of the field), and a condensate has $w=-1$ only at the instant where $M_{\mathrm{eff}}=0$.

**Where the condensate fails as dark energy** (Stage-3 document §12.5):

1. **Too fast.** $w_a=3x_0/(1+x_0)^2$ is fixed by $w_0$; at the quoted $w_0=-0.861$ it is $-4.81$ instead of $-0.60$.
2. **It leaves its domain.** Going back in time $M_{\mathrm{eff}}$ vanishes at $z=0.026$; beyond it the phantom epoch, the negative energy density beyond $z=0.293$ and the bounce at $z=0.388$ are artefacts, and the model gives no matter era and no early universe.
3. **Negative sound speed squared** today for every attractive model ($-12.39$, $-6.47$, $-1.50$, $-0.667$): in a fluid description, growing fluctuations (not computed).
4. **The 8-dimensional energy bound** forbids a 3-space observer from inferring $w_{\mathrm{eff}}<-1+(1+w)/\sqrt3$ when $\rho\ge0$, $w\ge-1$ and $H_a,\Theta>0$; the deflation variant needs negative 8-dimensional energy density.
5. **Newton's constant** would vary about 1800 times faster than the lunar-laser-ranging bound allows in the deflation variant.
6. **4-dimensional energy conservation** fails in the deflation variant.
7. **The coupling is outside the approximation.** For the tuned models the contact coupling is so strong wherever the Pauli caveat is negligible that no mass makes the Hartree description self-consistent (Section 11.4, limit 3).
8. **Only the good sector**, imposed by hand (EXP-5).
9. **Homogeneous mean field only**: no quantum corrections, exchange terms, stability of the condensate or inhomogeneities.
10. **No data likelihood**: the distance comparisons use noise-free curves with equal weights and the assumed $\Omega_m=0.305$ (except the $\Omega_m$-free projections of Section 11.9).

**The answer on dark energy: no, within everything computed.** The only negative pressure comes from an attractive four-fermion interaction. Tuned to the quoted $w_0=-0.861$ it evolves eight times too fast, has a negative sound speed squared, and its effective mass vanishes at $z=0.026$, where the single mean-field mode stops being a positive-energy level. The phantom crossing, the negative energy density at earlier times and the bounce that the equations then give are artefacts of the approximation, not properties of the field. The frozen density of the primordial field mimics a cosmological constant only in its dilution, in a geometry that needs negative energy. The framework reproduces neither the quoted $(w_0,w_a)$ nor the quoted $w=-0.764$ consistently. This “no” refers to the mechanisms available in this Lagrangian and these backgrounds; a different potential, inhomogeneous states, other couplings or a mechanism that stabilises the extra dimensions were not examined.

### 11.15 What we proved and what we assumed

**Proved (derived exactly in this chapter, in earlier chapters or in the cited stage documents).** The mode equation $i\dot u=hu$ in every homogeneous diagonal background, with $h^2=E^2$, $E^2=M_{\mathrm{eff}}^2+\sum_{j\le3}K_j^2-\sum_{j\ge5}K_j^2$; $h$ is Hermitian exactly in the good sector, where the Hilbert norm is conserved, and the Krein norm is conserved always ($h^\dagger B=Bh$). The per-mode energy $\varepsilon(u)=u^\dagger hu$ and pressure $p_j(u)$ as the images of $T_{44}$ and $T^j{}_j$ under the expectation-value rule of Section 8.12 (for $\lambda=0$; for $\lambda\ne0$ with the $\tfrac\lambda2S^2$ terms of Section 11.6). The dilution law $SV=$ constant at zero momentum. The curvature of a diagonal metric that depends on $t$ only ($R_{44}$, $R_{ii}$, $R^i{}_i=\dot H_i+H_i\Theta$, $G^4{}_4=-\sum_{i<j}H_iH_j$), hence the EXP-2 equations and the Friedmann equations. The split of $h=mZ+KX$ into eight two-level blocks. For a homogeneous condensate, with $T^i{}_i=\mathcal L_s$ (Section 7.10): $\rho=mS+\tfrac\lambda2S^2$, $p=\tfrac\lambda2S^2$, $\rho+p=2\,\mathrm{KE}_L=SM_{\mathrm{eff}}$ and the phantom criterion. The exact EXP-2 solution $V=1+\Theta_0t+\alpha t^2$, its Kasner exponents with $\sum_ip^{\mathrm K}_i=1$ and $\sum_i(p^{\mathrm K}_i)^2=1-2\kappa mx_0S_0/\mathcal D$, the energy bound $\Theta^2-3H_a^2-2\kappa\rho=H_b^2+3H_c^2$, and the dilution-inferred $w_{\mathrm{eff}}$. The EXP-1 requirement $\rho_{\mathrm{req}}=-3H^2(7+a_4'^2)/\kappa<0$ and $w_{\mathrm{req}}=-(5-a_4'^2)/(7+a_4'^2)$. The closed forms of EXP-3 (zeros, crossing, bounce cubic, tangent CPL parameters, sound speed) and of the deflation variant. No production for $m=0$; the equality of particle and antiparticle weights by unitarity; the WKB exponent of EXP-5; the pressure of one EXP-4a mode in terms of its level amplitudes, $p_1=(1-2|\beta|^2)K^2/E+2\,\mathrm{Re}(\alpha^\ast\beta)\,mK/E$, and its energy $\varepsilon=E(1-2|\beta|^2)$. Derived in outline, with its formula confirmed numerically only in the large-$k$ tail: the kink formula of EXP-4b. Derived in outline from the first-order adiabatic expansion, and confirmed by the checker's envelope: the amplitude $\delta_k$ of the sudden-start wave and the bound $|\beta|^2\le4\delta_k^2$. Derived at Hartree level but not machine-checked: $\rho+p\ge0$ for states with definite occupation numbers.

**Computed (numbers from the committed reports, verified by 69 self-checks, 167 independent checks, 10 analysis checks and two notebooks).** All the values quoted in Sections 11.6 to 11.12.

**Assumed.** $U(0)=U'(0)=0$ (no cosmological-constant term and no second mass term), a choice of the model. Homogeneous backgrounds in EXP-2 to EXP-5; in EXP-1 the prescribed warped primordial field, at one fixed $x_0$ for the $\lambda\ne0$ run; the 3-space expansion is prescribed in EXP-3 and EXP-4; only EXP-2 solves Einstein's equations, and without Einstein-Lovelock terms. Static hidden space and extra times in EXP-3 and EXP-4 (not derived; EXP-2 contradicts it for 8-dimensional Einstein gravity). The good sector only (imposed). The one-mode mean field at Hartree level, without the Pauli principle for the condensate (no Fermi sea and no degeneracy pressure), without exchange and with fixed normal ordering; its results are meaningful only while $M_{\mathrm{eff}}>0$. $k_0=0$ in EXP-4. A $C^1$ junction as the end of inflation ($a$ and $H$ continuous, $\dot H$ jumping; Section 11.11), plus one smooth comparison. The density parameters $\Omega_r=0.00009$, $\Omega_m=0.305$, $\Omega_\psi=0.69491$. The supernova numbers $(w_0,w_a)=(-0.861,-0.60)$ and $w=-0.764$ as quoted in a private e-mail without a primary reference, without error bars and without a likelihood. No fluctuations, no structure formation and no fit to real data were computed. **Not claimed:** that dirac16complex is dark matter or dark energy; that the (4,4) signature is the observed spacetime.

### 11.16 Exercises

Units as in the experiments ($m=1$ unless stated). Answers are in Section 11.17.

**Exercise 11.1.** *Energies of a mode.* For $h=-iM\gamma^4-K_0\gamma^4\gamma^0$ with $M=3$ and $K_0=4$, what are the eigenvalues of $h$ and how many times does each occur? Repeat for $h=-iM\gamma^4-K_5\gamma^4\gamma^5$ with $M=3$, $K_5=4$. Which of the two matrices is Hermitian, and what happens to $u^\dagger u$ in the second case?

**Exercise 11.2.** *Conservation laws.* Show that a solution of $i\dot u=hu$ keeps $u^\dagger u$ constant when $h^\dagger=h$, and keeps $u^\dagger Bu$ constant when $h^\dagger B=Bh$.

**Exercise 11.3.** *Condensate equations of state.* With $m=1$ and $S=1$, compute $M_{\mathrm{eff}}$, $\rho$, $p$, $w$, $\mathrm{KE}_L$ and $\mathrm{PE}_L$ for $\lambda=0.5$, $-0.5$, $-1.5$ and $-2.5$. Which cases are phantom, which have $\rho<0$, and which can the one-mode mean field describe?

**Exercise 11.4.** *An EXP-1 eigenmode.* For $K=0.5$, $\lambda=0$, $S_0=1$, predict $E$, $\rho$, $p_0$, $\bar p$, $w$, $\mathrm{KE}_L$, $\mathrm{PE}_L$ and $s$ of the positive-energy eigenmode.

**Exercise 11.5.** *The EXP-1 interaction run.* For $\lambda=0.5$, $K=0.5$, $S_0=1$, check that $M_\ast=1.47348266406420$ solves $M_\ast=1+\lambda S_0M_\ast/\sqrt{M_\ast^2+K^2}$, and compute $\rho$, the pressures $p_j$ ($j\ne0$) and $p_0$, $\bar p$ and $w$.

**Exercise 11.6.** *The primordial source on the plateau.* Where $a_4'=1$ and $a_4''=0$ (with $H=\kappa=1$), compute the seven required pressures, $\rho_{\mathrm{req}}$ and $w_{\mathrm{req}}$.

**Exercise 11.7.** *EXP-2 by hand.* For $x_0=-0.4$ compute $S_0$, $\lambda$, $\beta_2$, $\alpha_2$, the discriminant $\mathcal D$, $t_s$, the Kasner exponents $(p^{\mathrm K}_b,p^{\mathrm K}_a,p^{\mathrm K}_c)$, $\sum_ip^{\mathrm K}_i$ and $\sum_i(p^{\mathrm K}_i)^2$ (both ways), the time at which the extra times stop deflating, and the volumes at which $M_{\mathrm{eff}}=0$ and $\rho=0$.

**Exercise 11.8.** *A different start.* In EXP-2 with $x_0=0$, change the initial extra-time rate to $H_c=-0.3$. Predict the left side $\sum_{i<j}H_{i0}H_{j0}=\kappa\rho_0$ of the constraint at $t=0$, $\Theta_0$, $S_0$, $\beta_2$, $\alpha_2$ and the time at which $H_c$ changes sign. (The student guide, its exercise 13.4, shows how to run this modified case.)

**Exercise 11.9.** *EXP-3 with $x_0=-0.25$.* Predict $w_0$, $w_a$, the redshifts where $\rho_\psi=0$ and where $w=-1$, today's $c_s^2$, today's $q_{\mathrm{dec}}$, and the bounce. Compare with the row $x_0=-0.25$ of `artifacts/dirac16complex/numerics/exp3/fits_scan.csv`.

**Exercise 11.10.** *Closer to $-1$.* Which $x_0$ gives $w_0=-0.9$, and what is its tangent $w_a$? What does this say about approaching a cosmological constant with this model?

**Exercise 11.11.** *The sudden-start wave.* The admixture left by starting a thermal mode on the instantaneous eigenvector has the amplitude $\delta_k=mkH_{\mathrm{in}}/(4E^3)$ with $E=\sqrt{m^2+k^2}$ (Section 11.10). Find the $k$ at which $\delta_k$ is largest and the largest value of $\delta_k^2$ for $H_{\mathrm{in}}/m=0.05$.

**Exercise 11.12.** *Rotating eigenvectors.* For $h=E(\cos\theta\,\sigma_z+\sin\theta\,\sigma_x)$, verify that $u_+=(\cos\tfrac\theta2,\sin\tfrac\theta2)$ and $u_-=(-\sin\tfrac\theta2,\cos\tfrac\theta2)$ are eigenvectors with eigenvalues $\pm E$, and that $\dot u_+=\tfrac{\dot\theta}2u_-$. Why does this give no pair creation for $m=0$?

**Exercise 11.13.** *The kink formula integrated.* Show that $na^3=\frac{16}{2\pi^2}\int_0^\infty k^2\bigl(\frac{mkH^2}{4E^4}\bigr)^2dk=\frac{H^4}{64\pi m}$, using the substitution $k=m\tan\theta$. Compare with the computed yields for $m=0.1$, 1 and 2 ($H=1$).

**Exercise 11.14.** *The EXP-5 growth.* For $q=0.05$, compute $t_\ast$, $W(t_\ast+2)$ and $W(t_\ast+3)$, the WKB average growth rate of $\ln(u^\dagger u)$ over $[t_\ast+2,t_\ast+3]$, and $e^{2W(t_\ast+3)}$. Compare with the committed results. Why is the WKB rate over $[t_\ast,t_\ast+1]$ less reliable?

**Exercise 11.15.** *The initial Krein norm in EXP-5.* For $q=0.1$ compute $E_0$ and the Krein norm $u^\dagger Bu$ of the two initial spinors.

**Exercise 11.16.** *The deflation variant.* From $(w_0,w_a)=(-0.861,-0.60)$ find $x_0$, $n$ and $\gamma$; then $\kappa\rho_8/H_a^2$, $\dot G_N/(G_NH_0)$ and $G_N(z=1)/G_N(0)$.

**Exercise 11.17.** *What a 3-space observer sees.* Compute $w_{\mathrm{eff}}$ for dust when $\Theta=0$ (EXP-1), $\Theta=3H_a$ (EXP-3 and EXP-4), $\Theta=\sqrt3H_a$, and $\Theta=7H_a$ (late EXP-2).

**Exercise 11.18.** *The artefact.* Explain in three sentences why the phantom rows of the attractive EXP-2 run are not a prediction of the theory.

**Exercise 11.19.** *From candidate to model.* List what would have to be computed or derived to turn the dark-matter-like result of EXP-4 into a dark-matter model.

**Exercise 11.20.** *The dark-energy verdict.* Give two independent reasons, each sufficient by itself, why the tuned condensate of EXP-3 is not viable dark energy.

### 11.17 Answers to the exercises

**Answer 11.1.** From Section 11.3, $h^2=(M^2+K_0^2)\cdot1=25$, so the eigenvalues are $+5$ and $-5$, eight times each (the Stage-2 verifier evaluates exactly this case). In the second case $E^2=M^2-K_5^2=9-16=-7$: the eigenvalues are $\pm i\sqrt7=\pm2.6458\,i$, eight each. The first matrix is Hermitian; the second is not ($\gamma^4\gamma^5$ is anti-Hermitian). In the second case the part of $u$ along the eigenvalue $+i\sqrt7$ grows like $e^{\sqrt7t}$, so $u^\dagger u$ grows like $e^{2\sqrt7t}$, while $u^\dagger Bu$ stays constant.

**Answer 11.2.** $\frac{d}{dt}(u^\dagger Xu)=\dot u^\dagger Xu+u^\dagger X\dot u$ with $\dot u=-ihu$ and $\dot u^\dagger=iu^\dagger h^\dagger$ gives $i\,u^\dagger(h^\dagger X-Xh)u$. For $X=1$ this vanishes when $h^\dagger=h$; for $X=B$ when $h^\dagger B=Bh$.

**Answer 11.3.** With $M_{\mathrm{eff}}=1+\lambda$, $\rho=1+\lambda/2$, $p=\lambda/2$, $\mathrm{KE}_L=M_{\mathrm{eff}}/2$, $\mathrm{PE}_L=1/2$: $\lambda=0.5$: $M_{\mathrm{eff}}=1.5$, $\rho=1.25$, $p=0.25$, $w=0.2$, $\mathrm{KE}_L=0.75$. $\lambda=-0.5$: $0.5$, $0.75$, $-0.25$, $w=-1/3$, $\mathrm{KE}_L=0.25$. $\lambda=-1.5$: $-0.5$, $0.25$, $-0.75$, $w=-3$ (phantom), $\mathrm{KE}_L=-0.25$. $\lambda=-2.5$: $-1.5$, $\rho=-0.25<0$, $p=-1.25$, $w=5$, $\mathrm{KE}_L=-0.75$. $\mathrm{PE}_L=0.5$ in all four. Only the first two have $M_{\mathrm{eff}}>0$; in the other two the occupied rest level has negative energy, so the mean field does not describe a physical state there.

**Answer 11.4.** $E=\sqrt{1.25}=1.118034=\rho$; $p_0=K^2/E=0.223607$; $\bar p=p_0/7=0.031944$; $w=K^2/(7E^2)=1/35=0.028571$; $\mathrm{KE}_L=\mathrm{PE}_L=E/2=0.559017$; $s=M/E=0.894427$. These are the values of run A1_K0p5_pos_Bp in exp1/summary.json (key `initial`), collected under `freeEigenmodes` in numerics-summary.json.

**Answer 11.5.** $E_\ast=\sqrt{M_\ast^2+0.25}=1.556005$ and $S=s=M_\ast/E_\ast=0.946965$, so $1+0.5\cdot0.946965=1.473483=M_\ast$. Then $\tfrac\lambda2S^2=0.224186$, $\rho=E_\ast-0.224186=1.331819$, $p_j=0.224186$ for the six directions $j\ne0$, $p_0=K^2/E_\ast+0.224186=0.384854$, $\bar p=(0.384854+6\cdot0.224186)/7=0.247138$, $w=0.18556$, $\mathrm{KE}_L=E_\ast/2=0.778002$ and $\mathrm{PE}_L=0.553817$: the committed 1.3318, 0.2471, 0.1856, 0.7780 and 0.5538.

**Answer 11.6.** $p_{\mathrm{req},0}=-3(1-5)=12$, $p_{\mathrm{req},i}=15-3=12$, $p_{\mathrm{req},j}=12$: isotropic $p=12$; $\rho_{\mathrm{req}}=-3(7+1)=-24$; $w_{\mathrm{req}}=-1/2$. The pressure is positive; $w$ is negative only because $\rho$ is.

**Answer 11.7.** $S_0=1.32/0.6=2.2$, $\lambda=-0.8/2.2=-0.363636$, $\beta_2=2.2/6=0.366667$, $\alpha_2=1.283333$, $\mathcal D=5.76-5.133333=0.626667$, $\sqrt{\mathcal D}=0.791623$, $t_s=-2/3.191623=-0.626640$. $p^{\mathrm K}_b=(0-0.229768)/0.791623=-0.290250$, $p^{\mathrm K}_a=(1-0.229768)/0.791623=0.972978$, $p^{\mathrm K}_c=(-0.2-0.229768)/0.791623=-0.542895$. $\sum_ip^{\mathrm K}_i=-0.290250+3(0.972978)+3(-0.542895)=1.000000$; $\sum_i(p^{\mathrm K}_i)^2=3.808511$, and $1-2(-0.4)(2.2)/0.626667=3.808511$. $H_c=0$ at $t=0.2/\beta_2=0.545455$. $M_{\mathrm{eff}}=1+2x_0/V=0$ at $V=0.8$; $\rho\propto1+x_0/V=0$ at $V=0.4$. All agree with Section 11.7.

**Answer 11.8.** $\kappa\rho_0=\sum_{i<j}H_{i0}H_{j0}=3+3(0.09)+9(-0.3)=0.57$, $\Theta_0=3-0.9=2.1$, $S_0=0.57$, $\beta_2=0.095$, $\alpha_2=7S_0/12=0.3325$, and $H_c=0$ at $t=0.3/0.095=3.158$.

**Answer 11.9.** $w_0=-0.25/0.75=-1/3$; $w_a=3(-0.25)/0.5625=-4/3$; $\rho_\psi=0$ at $a=0.25^{1/3}=0.629961$, $z=0.587401$; $w=-1$ at $a=0.5^{1/3}=0.793701$, $z=0.259921$; $c_s^2=2x_0/(1+2x_0)=-0.5/0.5=-1$. Since $1+3w_0=0$, the condensate neither accelerates nor decelerates today and $q_{\mathrm{dec}}=(2\Omega_r+\Omega_m)/2=0.15259$. With $A_\psi=0.69491/0.75=0.926547$ the bounce cubic $1.231547\,a^3+0.00009\,a^2-0.231637=0$ gives $a_b=0.5729$, $z_b=0.7454$. The committed row gives $-0.3333$, $-1.3333$, $z=0.587401$, $z=0.259921$, $c_s^2=-1$, $q_0=0.15259$ and $z_b=0.745419$. Beyond $z=0.26$ the run would be outside the one-mode picture.

**Answer 11.10.** $x_0=w_0/(1-w_0)=-0.9/1.9=-0.473684$ and $w_a=3x_0/(1+x_0)^2=-5.13$; the scan row $x_0=-0.474$ gives $w_0=-0.90114$ and $w_a=-5.1396$. The closer $w_0$ is to $-1$, the faster the condensate evolves: the opposite of a slowly varying dark energy near a cosmological constant.

**Answer 11.11.** Maximise $k/E^3=k(m^2+k^2)^{-3/2}$: the derivative is $(m^2+k^2)^{-5/2}(m^2+k^2-3k^2)$, zero at $k=m/\sqrt2$, where $E^2=3m^2/2$. There $\delta_k=\frac{H_{\mathrm{in}}}{4\sqrt2(3/2)^{3/2}m}=\frac{H_{\mathrm{in}}}{10.39\,m}$, so for $H_{\mathrm{in}}/m=0.05$ the largest $\delta_k^2$ is $(0.05/10.39)^2=2.3\times10^{-5}$ (the value recorded in the EXP-4 findings of exp4/summary.json). At $k=0.9525$ the same formula gives $4\delta_k^2=8.17\times10^{-5}$, and the measured $6.37\times10^{-5}$ is 0.779 of it.

**Answer 11.12.** $hu_+=E(\cos\theta\cos\tfrac\theta2+\sin\theta\sin\tfrac\theta2,\ \sin\theta\cos\tfrac\theta2-\cos\theta\sin\tfrac\theta2)=E(\cos\tfrac\theta2,\sin\tfrac\theta2)$ by the difference formulas for cosine and sine; similarly $hu_-=-Eu_-$. Differentiating, $\dot u_+=\tfrac{\dot\theta}2(-\sin\tfrac\theta2,\cos\tfrac\theta2)=\tfrac{\dot\theta}2u_-$. For $m=0$, $h=K\sigma_x$, so $\cos\theta=m/E=0$ and $\sin\theta=K/E=1$: $\theta=\pi/2$ for every $K>0$. Then $\dot\theta=0$, the eigenvectors never rotate, and $\dot\beta=0$: no pairs.

**Answer 11.13.** With $E^2=m^2+k^2$: $na^3=\frac{16}{2\pi^2}\frac{m^2H^4}{16}\int_0^\infty\frac{k^4}{(m^2+k^2)^4}dk$. Put $k=m\tan\theta$, $dk=m\,d\theta/\cos^2\theta$, $m^2+k^2=m^2/\cos^2\theta$: the integral becomes $m^{-3}\int_0^{\pi/2}\sin^4\theta\cos^2\theta\,d\theta=m^{-3}(I_4-I_6)$, since $\cos^2\theta=1-\sin^2\theta$, with $I_n:=\int_0^{\pi/2}\sin^n\theta\,d\theta$. The $I_n$ follow from integration by parts (Section 1.10): write $\sin^n\theta=\sin^{n-1}\theta\cdot\sin\theta$ and integrate the factor $\sin\theta$ to $-\cos\theta$. The boundary term $\bigl[-\sin^{n-1}\theta\cos\theta\bigr]_0^{\pi/2}$ vanishes for $n\ge2$, so $I_n=(n-1)\int_0^{\pi/2}\sin^{n-2}\theta\cos^2\theta\,d\theta=(n-1)(I_{n-2}-I_n)$, that is $I_n=\frac{n-1}{n}\,I_{n-2}$. From $I_0=\pi/2$: $I_2=\pi/4$, $I_4=\tfrac34I_2=\tfrac{3\pi}{16}$ and $I_6=\tfrac56I_4=\tfrac{5\pi}{32}$. So the integral is $m^{-3}\bigl(\tfrac{3\pi}{16}-\tfrac{5\pi}{32}\bigr)=\frac{\pi}{32m^3}$. So $na^3=\frac{m^2H^4}{2\pi^2}\frac{\pi}{32m^3}=\frac{H^4}{64\pi m}$. For $m=1$: $4.97\times10^{-3}$, 1.13 times the computed $4.412\times10^{-3}$; for $m=2$: $2.49\times10^{-3}$, 1.03 times $2.421\times10^{-3}$; for $m=0.1$: $4.97\times10^{-2}$, 34 times the computed $1.454\times10^{-3}$. The formula assumes $E\gg H$, which fails for the small momenta that dominate the light field's production.

**Answer 11.14.** $t_\ast=\ln20=2.995732$. Since $Q=qe^{t}=e^{t-t_\ast}$: $W(t_\ast+2)=\sqrt{e^4-1}-\arccos(e^{-2})=5.88603$ and $W(t_\ast+3)=\sqrt{e^6-1}-\arccos(e^{-3})=18.53964$. The average rate is $2(18.53964-5.88603)=25.307$, against the committed 25.306. $e^{2W(t_\ast+3)}=e^{37.079}=1.27\times10^{16}$, the same order as the committed final $u^\dagger u=1.258\times10^{16}$; the leading WKB estimate ignores the amplitude factor and the region near $t_\ast$, so only the order of magnitude should be compared. Over $[t_\ast,t_\ast+1]$ WKB gives $2W(t_\ast+1)=2.667$ against the measured 2.37: near the turning point $\varkappa$ changes as fast as the solution itself, which violates the slow-change assumption of WKB.

**Answer 11.15.** $E_0=\sqrt{1-0.01}=0.994987$; $u^\dagger Bu=\pm E_0/m=\pm0.994987$ (the summary's `kreinNorm0` for runs `q0p1_Cp` and `q0p1_Cm`).

**Answer 11.16.** $x_0=-0.861/1.861=-0.462654$; $n=w_a(1+x_0)^2/x_0=0.374457$; $\gamma=1-n/3=0.875181$; $\kappa\rho_8/H_a^2=3(1-3\gamma+\gamma^2)=-2.5788$; $\dot G_N/(G_NH_0)=3\gamma=2.6255$; $G_N(z=1)/G_N(0)=(1+z)^{-3\gamma}=2^{-2.6255}=0.162$.

**Answer 11.17.** $w_{\mathrm{eff}}=-1+\Theta/(3H_a)$ for dust: $-1$ ($\Theta=0$), 0 ($\Theta=3H_a$), $-1+1/\sqrt3=-0.42265$ ($\Theta=\sqrt3H_a$), $-1+7/3=4/3$ ($\Theta=7H_a$).

**Answer 11.18.** The phantom rows all have $M_{\mathrm{eff}}<0$, while the occupied rest mode keeps $s(u)=1$ because it only changes its phase. Its energy $u^\dagger hu=M_{\mathrm{eff}}$ is then negative, so the one quantum of the mean-field picture sits in a negative-energy level, outside the domain of the expectation-value rule. A state with definite occupation numbers of positive-energy quanta has $\rho+p\ge0$ and cannot be phantom.

**Answer 11.19.** Physical values of $m$ and $H_{\mathrm{inf}}$ and the post-inflationary history, giving a relic density to compare with the observed one; a derived mechanism that keeps the hidden space and the extra times static; the couplings to ordinary matter and the resulting bounds (darkness, stability, annihilation through $\lambda$); the treatment of the hidden-space momentum; a justification for excluding the extra-time sector; and the growth of fluctuations and the free streaming that decide whether the relic is cold, warm or hot.

**Answer 11.20.** For example: (a) matching $w_0=-0.861$ forces $w_a=-4.81$, eight times the quoted $-0.60$, so the model cannot follow the quoted evolution; (b) the model leaves the validity of its own approximation at $z=0.026$ and gives no matter era; (c) its $c_s^2=-12.39$ today signals growing fluctuations in a fluid description; (d) no mass makes the tuned Hartree description self-consistent.

### 11.18 Repository files used in this chapter

The chapter's numbers and figures come from these committed files; Chapter 19 gives the commands that regenerate and check them.

```
provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md      the Stage-3 document
provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md             running and checking, step by step
handoff/specs/NUMERICS_CONTRACT.md                     the numerical programme and errata
studies/dirac16complex_cosmology/src/exp1.rs ... exp5.rs
                                                       the five experiments
artifacts/dirac16complex/numerics/exp1/ ... exp5/      CSV, summary.json, checker reports
artifacts/dirac16complex/numerics/exp3/fits.json       EXP-3 fits and estimates
artifacts/dirac16complex/numerics/exp3/fits_scan.csv   the 491-coupling scan
artifacts/dirac16complex/numerics/numerics-summary.json
                                                       all checks, verdict SUCCESS
artifacts/dirac16complex/numerics/figures/             the 17 notebook figures
artifacts/dirac16complex/numerics/figures/mathematica/ the Mathematica figures
scripts/check_dirac16complex_exp1.py ... exp5.py       independent checkers
scripts/analyze_dirac16complex_exp3.py                 fits (numpy Nelder-Mead)
notebooks/dirac16complex_dark_sector.ipynb             Jupyter notebook (71 assertions)
notebooks/Dirac16ComplexDarkSector.nb                  Mathematica notebook (49 checks)
provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md          Stage 2: sources of the field
provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md           Stage 1: T, splits, quantization
```
